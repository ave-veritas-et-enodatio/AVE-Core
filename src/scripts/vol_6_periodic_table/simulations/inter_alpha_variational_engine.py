"""
AVE MODULE: INTER-ALPHA VARIATIONAL EQUILIBRIUM ENGINE
======================================================
Configuration-determining variational engine for multi-alpha-cluster nuclei.

Architecture (per mad-design/inter-alpha-resonance/IMPLEMENTATION_PLAN.md):
    - Free 3D Cartesian relaxation of each alpha-cluster centroid (3·N_alpha DOFs)
    - Topology graph (which alphas are nearest-neighbour edges) is fixed input
    - Initial conditions: canonical Platonic / Archimedean vertex coordinates,
      scaled to the closed-form prediction R_pred = 40·pi·hbar*c / (g(1-alpha/3)·E_0)
    - Multi-port S_11 objective: per-node |Gamma_i|^2 from full Y-matrix +
      Coulomb / saturation / packing penalties
    - Reference admittance Y_0 prescription is selectable via enum (see §4):
        GEOMETRIC_MEAN, VACUUM_LATTICE, ARITHMETIC_MEAN, PARALLEL
    - Newton-Raphson + backtracking line search (port from
      AVE-Protein/engines/s11_fold_engine_v4_ymatrix.py::fold_eigenvalue_v5)

This module sits alongside (and does not replace) `alpha_cascade_engine.py`,
which only handles 1D ring cascades and is structurally inadequate for
non-ring topologies (Mg-24 octahedron, O-16 tetrahedron).

Entry point:
    solve_inter_alpha_equilibrium(name, n_alpha, topology_name,
                                  e_op=E_0, y0_prescription="geometric_mean",
                                  ...) -> dict

All physics derived from AVE Axioms 1-4 (no empirical tuning):
    Axiom 1 -> Z_0 = sqrt(mu0/eps0) = 377 Ohm (vacuum lattice)
    Axiom 2 -> alpha, K_MUTUAL, alpha*hbar*c
    Axiom 4 -> saturation kernel C_sat(D_intra/r)
"""

from __future__ import annotations

import math
import os
import time
from collections.abc import Callable
from enum import Enum
from typing import NamedTuple

# JAX-Metal does not implement int32-on-host scatter-add semantics required
# by our Y-matrix assembly (`Y.at[edges_i, edges_j].add(...)`).  The problem
# is tiny (N_alpha <= 7) so CPU is plenty fast — force CPU before importing
# JAX to avoid the Metal default-memory-space failure.
os.environ.setdefault("JAX_PLATFORMS", "cpu")

import jax  # noqa: E402
import jax.numpy as jnp  # noqa: E402
import numpy as np  # noqa: E402
from jax import grad, jit  # noqa: E402

# Enable double precision for stability of the multi-port S-extraction
jax.config.update("jax_enable_x64", True)

# AVE constants
from ave.core.constants import ALPHA, D_INTRA_ALPHA, E_0_NUCLEAR, HBAR_C_MEV_FM, K_MUTUAL
from ave.core.constants import Z_0 as Z_0_VAC

# Reuse the multiport S-extraction primitive from AVE-Core solvers
from ave.solvers.transmission_line import s_diagonal_from_y_matrix_jax

# Reuse topology constructors and binding evaluator (read-only) so the
# variational engine reports R against the same engine-fit convention
from scripts.vol_6_periodic_table.simulations.semiconductor_binding_engine import (
    ALPHA_HC,
    D_INTRA,
    M_ALPHA,
    V_BR,
    compute_binding,
)
from scripts.vol_6_periodic_table.simulations.semiconductor_binding_engine import d as D_PROTON_FM  # noqa: E402
from scripts.vol_6_periodic_table.simulations.semiconductor_binding_engine import (
    make_octahedron,
    make_pentagonal_bipyramid,
    make_ring,
    make_tetrahedron,
)

# =============================================================================
# CONSTANTS DERIVED FROM AXIOMS
# =============================================================================

# Vacuum free-space impedance (Axiom 1, scale-invariant)
Y_0_VAC: float = 1.0 / Z_0_VAC  # Siemens

# Operating frequency: passband center of the K_4 alpha tank (SOLUTION §1)
E_0_DEFAULT: float = float(E_0_NUCLEAR)  # ~301.582 MeV

# Q-factor of the alpha-cluster tank (SOLUTION §2 + IMPLEMENTATION_PLAN §3).
# The intra-alpha coupling k_intra = 0.01580 gives a passband fractional width
# of ~3 k_intra; Q_alpha = 1 / (3 k_intra) ~ 21.
K_INTRA: float = (K_MUTUAL / E_0_DEFAULT) / D_INTRA_ALPHA  # ~0.01580
Q_ALPHA: float = 1.0 / (3.0 * K_INTRA)  # ~21
NOISE_FLOOR: float = 1.0 / Q_ALPHA**2  # ~0.0023

# K_4 alpha-cluster passband edges (SOLUTION §2)
E_BOND: float = E_0_DEFAULT / math.sqrt(1.0 + 3.0 * K_INTRA)  # ~294.685 MeV
E_ANTI: float = E_0_DEFAULT / math.sqrt(1.0 - 3.0 * K_INTRA)  # ~308.999 MeV

# Closed-form scalar R prediction prefactor (SOLUTION §1):
#     R_pred = 40 * pi * hbar*c / (g * (1 - alpha/3) * E_op)
R_PRED_PREFACTOR: float = 40.0 * math.pi * HBAR_C_MEV_FM / (1.0 - ALPHA / 3.0)


def topology_factor_g(topology_name: str, n_alpha: int) -> float:
    """Closed-form topology factor g (SOLUTION §1).

    Used only for initial-scale guess; the engine relaxes freely from there.
    Falls back to 2 sin(pi/N) (planar ring) for unknown topologies — that is
    just a length scale, not a constraint.
    """
    name = topology_name.lower()
    if name in ("ring", "ring3", "ring5", "ring7"):
        return 2.0 * math.sin(math.pi / n_alpha)
    if name in ("tet", "tetrahedron"):
        return 2.0 * math.sqrt(2.0)
    if name in ("octahedron", "oct"):
        # Octahedron: nearest-neighbour edges at R*sqrt(2) (12 of them);
        # use sqrt(2) so initial R_pred * sqrt(2) gives a sensible NN length.
        return math.sqrt(2.0)
    if name in ("pent_bipyr", "pentagonal_bipyramid"):
        # Equatorial 5-ring is the dominant edge class
        return 2.0 * math.sin(math.pi / 5)
    # Default: planar ring formula
    return 2.0 * math.sin(math.pi / max(n_alpha, 2))


def closed_form_r_prediction(topology_name: str, n_alpha: int, e_op: float) -> float:
    """Inter-alpha distance R prediction (SOLUTION §1)."""
    g = topology_factor_g(topology_name, n_alpha)
    return R_PRED_PREFACTOR / (g * e_op)


# =============================================================================
# Y_0 PRESCRIPTIONS (IMPLEMENTATION_PLAN §4 fallback sequence)
# =============================================================================


class Y0Prescription(str, Enum):
    GEOMETRIC_MEAN = "geometric_mean"  # v1 default
    VACUUM_LATTICE = "vacuum_lattice"
    ARITHMETIC_MEAN = "arithmetic_mean"
    PARALLEL = "parallel"


Y0_PRESCRIPTIONS: tuple[Y0Prescription, ...] = (
    Y0Prescription.GEOMETRIC_MEAN,
    Y0Prescription.VACUUM_LATTICE,
    Y0Prescription.ARITHMETIC_MEAN,
    Y0Prescription.PARALLEL,
)


# =============================================================================
# TOPOLOGY LIBRARY (initial conditions + adjacency edges)
# =============================================================================
#
# Each entry returns:
#   (positions_init: (n_alpha, 3) ndarray, edges: list[(i, j)])
#
# Positions are produced by reusing semiconductor_binding_engine make_*
# constructors with R_factor chosen so the canonical edge length matches the
# closed-form R prediction (we relax freely from there).


def _scale_canonical(centers: np.ndarray, target_R: float) -> np.ndarray:
    """Rescale a unit-style vertex array so that the *centroid radius*
    equals target_R.  Used to seed the variational optimiser."""
    centroid = centers.mean(axis=0)
    rel = centers - centroid
    radii = np.linalg.norm(rel, axis=1)
    mean_r = float(np.mean(radii))
    if mean_r < 1e-12:
        return centers.copy()
    return centroid + rel * (target_R / mean_r)


def _ring_edges(n: int) -> list[tuple[int, int]]:
    return [(i, (i + 1) % n) for i in range(n)]


def _full_edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def _octahedron_edges() -> list[tuple[int, int]]:
    """Octahedron: 12 edges of length R*sqrt(2); the 3 antipodal pairs at
    distance 2R are *not* nearest neighbours (per SOLUTION §8.2 multi-edge-
    class observation, only NN edges enter the topology graph)."""
    # Vertices in make_octahedron order:
    # 0:(R,0,0), 1:(-R,0,0), 2:(0,R,0), 3:(0,-R,0), 4:(0,0,R), 5:(0,0,-R)
    # NN pairs: every pair *except* the antipodal (0,1), (2,3), (4,5)
    antipodes = {(0, 1), (2, 3), (4, 5)}
    edges = []
    for i in range(6):
        for j in range(i + 1, 6):
            if (i, j) not in antipodes:
                edges.append((i, j))
    return edges


def _pentagonal_bipyramid_edges() -> list[tuple[int, int]]:
    """5 equatorial nodes (0..4 ring) + 2 polar (5, 6).
    Edges: 5 equatorial ring edges + 10 polar-to-equator spokes.
    The polar pair (5,6) is NOT an NN edge (it crosses the cluster center).
    """
    edges = list(_ring_edges(5))  # equatorial ring
    for k in range(5):
        edges.append((k, 5))
        edges.append((k, 6))
    return edges


def build_topology(
    topology_name: str,
    n_alpha: int,
    initial_R: float,
) -> tuple[np.ndarray, list[tuple[int, int]]]:
    """Construct (initial_positions, edge_list) for a named topology.

    The optimiser then relaxes positions freely; edges remain the fixed
    adjacency graph throughout (per IMPLEMENTATION_PLAN §6).
    """
    name = topology_name.lower()
    if name in ("ring", "ring3", "ring5", "ring7"):
        # make_ring(n, R_factor) builds positions on a circle of radius R_factor*d,
        # so the center-to-center NN edge length is 2R*sin(pi/n).
        # We want the NN edge ~= R_NN := g_ring * initial_R = 2 sin(pi/n) * R_pred.
        # The simplest thing is to set R_factor*d = initial_R (centroid radius).
        R_factor = initial_R / D_PROTON_FM
        positions = make_ring(n_alpha, R_factor)
        edges = _ring_edges(n_alpha)
    elif name in ("tet", "tetrahedron"):
        R_factor = initial_R / D_PROTON_FM
        positions = make_tetrahedron(R_factor)
        edges = _full_edges(4)
    elif name in ("octahedron", "oct"):
        # make_octahedron places vertices at distance R from origin; the NN
        # edge length is R*sqrt(2).  We want the centroid radius = initial_R
        # (per the closed-form convention used everywhere else).
        R_factor = initial_R / D_PROTON_FM
        positions = make_octahedron(R_factor)
        edges = _octahedron_edges()
    elif name in ("pent_bipyr", "pentagonal_bipyramid"):
        R_factor = initial_R / D_PROTON_FM
        positions = make_pentagonal_bipyramid(R_factor)
        edges = _pentagonal_bipyramid_edges()
    else:
        raise ValueError(f"Unknown topology: {topology_name!r}")
    if positions.shape[0] != n_alpha:
        raise ValueError(
            f"Topology {topology_name!r} produced {positions.shape[0]} centers, " f"expected n_alpha={n_alpha}"
        )
    return np.asarray(positions, dtype=np.float64), edges


# =============================================================================
# Z_alpha(omega) — per-node alpha-cluster impedance (lumped tank, IMPL §3)
# =============================================================================


def z_alpha_lumped(omega_mev: float, e_op: float = E_0_DEFAULT, q: float = Q_ALPHA) -> complex:
    """Lumped parallel-LC tank model for the alpha-cluster impedance.

    At omega = e_op the impedance is purely real and equal to Z_0 (matched to
    the vacuum lattice — IMPLEMENTATION_PLAN §3 v1 assumption).  Off-center,
    the standard parallel-tank Z(omega) form applies:

        Z_alpha(omega) = Z_0 / (1 + j Q (omega/omega_0 - omega_0/omega))

    Returns a complex scalar [Ohm].
    """
    if omega_mev <= 0.0:
        return complex(Z_0_VAC, 0.0)
    x = omega_mev / e_op
    detune = x - 1.0 / x
    return Z_0_VAC / (1.0 + 1j * q * detune)


# =============================================================================
# Y-MATRIX ASSEMBLY FOR NUCLEAR EDGES (JAX, IMPL §4)
# =============================================================================
#
# Each edge i-j is a vacuum transmission-line section of length R_ij,
# characteristic impedance Z_0 = 377 Ohm, propagation
#     gamma * ell = (alpha_strain + j beta) * R_ij
# where beta = (omega/c)(1 + nu_vac) per Axiom 1+3 (already encoded in
# E_0_NUCLEAR) and the strain term encodes the |R - R_pred|/R_pred loss.
#
# ABCD->Y for a single TL section:
#     y_mutual = -1 / (Z_0 * sinh(gamma_l))
#     y_self_per_endpoint = cosh(gamma_l) / (Z_0 * sinh(gamma_l))    [coth(gamma_l)/Z_0]
#
# At each node we additionally add the alpha-cluster self admittance
#     y_alpha = 1 / Z_alpha(omega)
# to the diagonal.


def _beta_per_fm(e_op_mev: float) -> float:
    """Phase constant beta = E_op / (hbar*c) [1/fm]."""
    return e_op_mev / HBAR_C_MEV_FM


def _build_y_matrix_jax(
    positions: jax.Array,
    edges_i: jax.Array,
    edges_j: jax.Array,
    R_pred: float,
    e_op: float,
    z_alpha: complex,
) -> jax.Array:
    """Assemble the N x N nuclear Y-matrix (single-frequency).

    Args:
        positions: (n_alpha, 3) JAX array, alpha-cluster centroids in fm
        edges_i, edges_j: (n_edges,) static arrays of edge endpoints
        R_pred: closed-form predicted R (used for the strain-loss baseline)
        e_op: operating energy in MeV
        z_alpha: complex per-node alpha-cluster impedance at e_op
    """
    n = positions.shape[0]

    diff = positions[edges_i] - positions[edges_j]
    R_ij = jnp.sqrt(jnp.sum(diff * diff, axis=-1) + 1e-12)

    beta = _beta_per_fm(e_op)
    alpha_strain = jnp.abs(R_ij - R_pred) / (R_pred + 1e-12)
    gamma_l = alpha_strain + 1j * beta * R_ij

    sinh_gl = jnp.sinh(gamma_l)
    cosh_gl = jnp.cosh(gamma_l)

    Z0 = jnp.asarray(Z_0_VAC, dtype=jnp.complex128)
    y_mutual = -1.0 / (Z0 * sinh_gl + 1e-18)
    y_self_endpoint = cosh_gl / (Z0 * sinh_gl + 1e-18)  # coth(gamma_l) / Z0

    Y = jnp.zeros((n, n), dtype=jnp.complex128)

    # Off-diagonals (symmetric)
    Y = Y.at[edges_i, edges_j].add(y_mutual)
    Y = Y.at[edges_j, edges_i].add(y_mutual)

    # Diagonals: each segment contributes coth/Z0 to *both* endpoints
    Y = Y.at[edges_i, edges_i].add(y_self_endpoint)
    Y = Y.at[edges_j, edges_j].add(y_self_endpoint)

    # Per-node alpha-cluster self-admittance
    y_alpha = 1.0 / z_alpha
    diag_idx = jnp.arange(n)
    Y = Y.at[diag_idx, diag_idx].add(y_alpha)

    return Y


def _per_node_y0_reference(
    positions: jax.Array,
    edges_i: jax.Array,
    edges_j: jax.Array,
    n_alpha: int,
    prescription: Y0Prescription,
) -> jax.Array:
    """Per-node reference admittance Y_0,i (per IMPL §4 fallback sequence).

    Returns a (n_alpha,) complex array.
    """
    if prescription == Y0Prescription.VACUUM_LATTICE:
        return jnp.full((n_alpha,), Y_0_VAC, dtype=jnp.complex128)

    # All segments have characteristic Z = Z_0 (vacuum lattice, Axiom 1).
    # So per-node Y_seg incident is just Y_0_VAC counted by node degree.
    # The four prescriptions therefore differ in how degree enters:
    edges_i_np = edges_i  # (E,)
    edges_j_np = edges_j  # (E,)
    one = jnp.ones_like(edges_i_np, dtype=jnp.complex128)

    deg = jnp.zeros((n_alpha,), dtype=jnp.complex128)
    deg = deg.at[edges_i_np].add(one)
    deg = deg.at[edges_j_np].add(one)
    # avoid degree-0 division
    deg = jnp.where(jnp.abs(deg) < 1e-12, jnp.ones_like(deg), deg)

    Y_seg = Y_0_VAC

    if prescription == Y0Prescription.GEOMETRIC_MEAN:
        # geometric mean of n equal Y_seg entries == Y_seg
        return jnp.full((n_alpha,), Y_seg, dtype=jnp.complex128)
    if prescription == Y0Prescription.ARITHMETIC_MEAN:
        # arithmetic mean of n equal Y_seg entries == Y_seg
        return jnp.full((n_alpha,), Y_seg, dtype=jnp.complex128)
    if prescription == Y0Prescription.PARALLEL:
        # sum of incident segment admittances = degree * Y_seg
        return deg * Y_seg
    raise ValueError(f"Unknown Y0 prescription: {prescription}")


# =============================================================================
# AUXILIARY POTENTIALS (Coulomb, saturation, packing, exclusion)
# =============================================================================


def _aux_potentials(
    positions: jax.Array,
    edges_i: jax.Array,
    edges_j: jax.Array,
    n_alpha: int,
    R_pred: float,
) -> dict:
    """Compute scalar auxiliary penalties (per IMPLEMENTATION_PLAN §2 + §5).

    Returns a dict so the loss factory can weight components individually.
    """
    diff = positions[edges_i] - positions[edges_j]
    R_ij = jnp.sqrt(jnp.sum(diff * diff, axis=-1) + 1e-12)

    # Per-edge Op4 strong coupling (4x4 = 16 inter-alpha nucleon pairs per edge)
    sat_ratio = jnp.clip(D_INTRA_ALPHA / (R_ij + 1e-10), 0.0, 0.95)
    C_sat = 1.0 / jnp.sqrt(1.0 - sat_ratio * sat_ratio)
    U_strong = -16.0 * K_MUTUAL * C_sat / R_ij  # per-edge MeV

    # Per-edge Coulomb (f_pp = 0.25, p-p fraction in inter-alpha nucleon pairs)
    U_coul = 16.0 * 0.25 * ALPHA_HC / R_ij

    # Combined edge energy (sign: bound = negative; we minimise total loss)
    edge_energy = jnp.sum(U_strong + U_coul)

    # Macroscopic packing reflection (Op8 analog, IMPL §2 N3)
    # Compute cluster effective radius (geometric mean of |x_i - centroid|)
    centroid = jnp.mean(positions, axis=0)
    radii = jnp.sqrt(jnp.sum((positions - centroid) ** 2, axis=-1) + 1e-12)
    R_g = jnp.mean(radii)
    Gamma_pack = (R_g - R_pred) / (R_g + R_pred + 1e-12)

    # Soft pairwise exclusion (Op9): no two alphas may interpenetrate.
    # Cheap version using *all* unordered pairs (not just edges) so the
    # optimizer can't tunnel through non-adjacent pairs.
    P = positions[:, None, :] - positions[None, :, :]
    D_all = jnp.sqrt(jnp.sum(P * P, axis=-1) + 1e-12)
    iu = jnp.triu_indices(n_alpha, k=1)
    D_pairs = D_all[iu]
    floor = 2.0 * D_INTRA_ALPHA  # ~4.76 fm
    excl = jnp.maximum(0.0, floor - D_pairs)
    excl_pen = jnp.sum(excl * excl)  # quadratic wall

    return {
        "edge_energy": edge_energy,
        "Gamma_pack_sq": Gamma_pack * Gamma_pack,
        "excl_pen": excl_pen,
        "R_ij": R_ij,
    }


# =============================================================================
# LOSS FUNCTION (IMPLEMENTATION_PLAN §5)
# =============================================================================


class _LossWeights(NamedTuple):
    s11: float = 1.0
    pack: float = 0.0  # set in factory
    excl: float = 0.0  # set in factory
    edge_energy: float = 0.0  # absorb into objective only optionally


def _make_loss_fn(
    n_alpha: int,
    edges: list[tuple[int, int]],
    R_pred: float,
    e_op: float,
    prescription: Y0Prescription,
):
    """Compile a JAX-traceable scalar loss.

    Returns (loss_fn, loss_components_fn) where:
        loss_fn(pos_flat) -> scalar
        loss_components_fn(pos_flat) -> dict (for diagnostics)
    Both are jit-compatible.
    """
    edges_i = jnp.asarray([e[0] for e in edges], dtype=jnp.int32)
    edges_j = jnp.asarray([e[1] for e in edges], dtype=jnp.int32)

    # Static z_alpha (lumped, real at e_op)
    z_alpha = z_alpha_lumped(e_op, e_op=e_op)

    weights = _LossWeights(
        s11=1.0,
        pack=1.0 / max(n_alpha, 1),
        excl=V_BR / (D_INTRA_ALPHA * D_INTRA_ALPHA) * 1e-3,  # gentle wall
    )

    def _components(pos_flat: jax.Array) -> dict:
        positions = pos_flat.reshape(n_alpha, 3)
        Y = _build_y_matrix_jax(positions, edges_i, edges_j, R_pred, e_op, z_alpha)
        Y0_per_node = _per_node_y0_reference(positions, edges_i, edges_j, n_alpha, prescription)

        s_info = s_diagonal_from_y_matrix_jax(Y, Y0=Y0_per_node)
        s11_per_node = s_info["diag"]  # (n_alpha,) real |Gamma_i|^2
        s11_sum = jnp.sum(s11_per_node)
        s11_max = s_info["max"]

        aux = _aux_potentials(positions, edges_i, edges_j, n_alpha, R_pred)

        return {
            "s11_per_node": s11_per_node,
            "s11_sum": s11_sum,
            "s11_max": s11_max,
            "s11_eig_min": s_info["eig_min"],
            "Gamma_pack_sq": aux["Gamma_pack_sq"],
            "excl_pen": aux["excl_pen"],
            "edge_energy": aux["edge_energy"],
            "R_ij": aux["R_ij"],
        }

    def _scalar_loss(pos_flat: jax.Array) -> jax.Array:
        c = _components(pos_flat)
        return weights.s11 * c["s11_sum"] + weights.pack * c["Gamma_pack_sq"] + weights.excl * c["excl_pen"]

    return _scalar_loss, _components, weights


# =============================================================================
# NEWTON-RAPHSON + LINE SEARCH OPTIMISER (port from protein v5)
# =============================================================================


def _newton_raphson_with_linesearch(
    loss_fn: Callable[[jax.Array], jax.Array],
    pos0: np.ndarray,
    n_iter: int = 200,
    trust_radius: float = 1.0,  # fm (per IMPL §5: ~0.5 a_E0 ~ 1 fm)
    grad_tol: float = 1e-5,
    f_tol: float | None = None,
    verbose: bool = False,
) -> tuple[np.ndarray, dict]:
    """Newton-Raphson root-finding with backtracking line search.

    Following AVE-Protein/engines/s11_fold_engine_v4_ymatrix.py::fold_eigenvalue_v5
    `_newton_step`.  Step direction:  delta = -f * g / |g|^2  (Newton on |f|^2
    in the rank-1 approximation).  Trust region cap on ||delta||.  Inner
    backtracking line search halves alpha until f decreases or 25 trials
    exhausted.

    Returns final position (flat ndarray) and a diagnostics dict.
    """
    loss_jit = jit(loss_fn)
    grad_jit = jit(grad(loss_fn))

    pos = jnp.asarray(pos0.flatten(), dtype=jnp.float64)

    # JIT warmup
    _ = loss_jit(pos)
    _ = grad_jit(pos)

    history = {"f": [], "g_norm": [], "step": []}

    f_val = float(loss_jit(pos))
    history["f"].append(f_val)

    n_actual = 0
    converged = False

    for i in range(n_iter):
        n_actual = i + 1
        f_val_arr = loss_jit(pos)
        g_arr = grad_jit(pos)
        g_arr = jnp.where(jnp.isnan(g_arr), 0.0, g_arr)
        g_norm = float(jnp.sqrt(jnp.sum(g_arr * g_arr)))
        history["g_norm"].append(g_norm)

        f_val = float(f_val_arr)
        history["f"].append(f_val)

        if g_norm < grad_tol:
            converged = True
            break
        if f_tol is not None and abs(f_val) < f_tol:
            converged = True
            break

        # Newton direction: delta = -f * g / |g|^2
        g_norm_sq = float(jnp.sum(g_arr * g_arr) + 1e-12)
        direction = (-f_val) * g_arr / g_norm_sq

        # Trust region cap (||direction|| <= trust_radius in fm units)
        dir_norm = float(jnp.sqrt(jnp.sum(direction * direction) + 1e-12))
        if dir_norm > trust_radius:
            direction = direction * (trust_radius / dir_norm)

        # Backtracking line search: try alpha = 1, 0.5, 0.25, ...
        alpha = 1.0
        accepted = False
        for _bt in range(25):
            trial = pos + alpha * direction
            f_trial = float(loss_jit(trial))
            if f_trial < f_val:
                pos = trial
                f_val = f_trial
                accepted = True
                history["step"].append(alpha)
                break
            alpha *= 0.5
        if not accepted:
            history["step"].append(0.0)
            # No descent direction found — terminate
            break

        if verbose and (i % 25 == 0 or i == n_iter - 1):
            print(
                f"    iter {i:4d}  f={f_val:.6e}  |g|={g_norm:.3e}  step={alpha:.3e}",
                flush=True,
            )

    final_f = float(loss_jit(pos))
    final_g = float(jnp.sqrt(jnp.sum(grad_jit(pos) ** 2)))

    return np.asarray(pos), {
        "n_iter": n_actual,
        "converged": converged,
        "final_f": final_f,
        "final_grad_norm": final_g,
        "f_history": history["f"],
        "g_norm_history": history["g_norm"],
    }


# =============================================================================
# ENTRY POINT
# =============================================================================


def solve_inter_alpha_equilibrium(
    name: str,
    n_alpha: int,
    topology_name: str | None,
    e_op: float = E_0_DEFAULT,
    y0_prescription: str | Y0Prescription = Y0Prescription.GEOMETRIC_MEAN,
    initial_R: float | None = None,
    max_iter: int = 200,
    trust_radius: float = 1.0,
    grad_tol: float = 1e-5,
    verbose: bool = False,
) -> dict:
    """Variational equilibrium of an alpha-cluster nucleus.

    Args:
        name: e.g. "Mg-24" (display only)
        n_alpha: number of alpha clusters; n_alpha == 1 short-circuits (He-4)
        topology_name: required if n_alpha >= 2; one of
            "ring3", "ring5", "tetrahedron", "octahedron",
            "pentagonal_bipyramid"
        e_op: operating energy [MeV], default = E_0 (~301.582)
        y0_prescription: per IMPL §4 fallback enum; "geometric_mean" default
        initial_R: if None, use closed-form prediction
        max_iter, trust_radius, grad_tol: Newton-Raphson settings

    Returns:
        Dict with: positions (n_alpha,3), R_predicted_geometric_mean,
        R_initial, R_engine_equivalent, f_final, s11_per_node,
        edge_lengths, n_iter, converged, final_grad_norm,
        topology_score (=f_final), prescription, e_op, edges.
        For n_alpha == 1: returns degenerate dict with R values None.
    """
    if isinstance(y0_prescription, str):
        prescription = Y0Prescription(y0_prescription)
    else:
        prescription = y0_prescription

    # ---- He-4 short-circuit (IMPL §5 + IMPL §10 risk #5) ----
    if n_alpha == 1:
        return {
            "name": name,
            "n_alpha": 1,
            "topology": None,
            "degenerate": True,
            "positions": None,
            "R_predicted_geometric_mean": None,
            "R_initial": None,
            "R_engine_equivalent": None,
            "f_final": None,
            "s11_per_node": None,
            "edge_lengths": [],
            "n_iter": 0,
            "converged": True,
            "final_grad_norm": 0.0,
            "topology_score": 0.0,
            "prescription": prescription.value,
            "e_op": e_op,
            "edges": [],
            "note": "Single alpha — no inter-alpha graph; R undefined.",
        }

    if topology_name is None:
        raise ValueError("topology_name is required for n_alpha >= 2")

    # ---- Initial R: closed-form prediction (or user override) ----
    R_pred = closed_form_r_prediction(topology_name, n_alpha, e_op)
    R0 = float(initial_R) if initial_R is not None else R_pred

    # ---- Build initial positions + edge graph ----
    positions0, edges = build_topology(topology_name, n_alpha, R0)

    # ---- Compile loss + run Newton-Raphson ----
    loss_fn, components_fn, weights = _make_loss_fn(n_alpha, edges, R_pred, e_op, prescription)

    if verbose:
        print(
            f"  {name}/{topology_name}/{prescription.value}: "
            f"n_alpha={n_alpha}, |E|={len(edges)}, R0={R0:.3f} fm, R_pred={R_pred:.3f} fm",
            flush=True,
        )

    pos_final, diag = _newton_raphson_with_linesearch(
        loss_fn,
        positions0,
        n_iter=max_iter,
        trust_radius=trust_radius,
        grad_tol=grad_tol,
        verbose=verbose,
    )

    pos3d = pos_final.reshape(n_alpha, 3)

    # ---- Diagnostics ----
    components_jit = jit(components_fn)
    comps = components_jit(jnp.asarray(pos_final, dtype=jnp.float64))
    edge_lengths_arr = np.asarray(comps["R_ij"])
    s11_per_node = np.asarray(comps["s11_per_node"])

    # R_engine_equivalent: the "R" parameter that semiconductor_binding_engine
    # would have produced — it's the centroid radius of the cluster (since all
    # make_* functions place vertices at distance R_factor*d from origin).
    centroid = pos3d.mean(axis=0)
    rel = pos3d - centroid
    centroid_radii = np.linalg.norm(rel, axis=1)
    R_engine_equivalent = float(np.mean(centroid_radii))

    # R_predicted_geometric_mean: geometric mean of edge lengths
    if edge_lengths_arr.size > 0:
        R_NN_gm = float(np.exp(np.mean(np.log(edge_lengths_arr + 1e-12))))
    else:
        R_NN_gm = float("nan")

    return {
        "name": name,
        "n_alpha": n_alpha,
        "topology": topology_name,
        "degenerate": False,
        "positions": pos3d,
        "R_predicted_geometric_mean": R_NN_gm,
        "R_initial": R0,
        "R_pred_closed_form": R_pred,
        "R_engine_equivalent": R_engine_equivalent,
        "f_final": diag["final_f"],
        "f_initial": diag["f_history"][0] if diag["f_history"] else None,
        "s11_per_node": s11_per_node,
        "edge_lengths": edge_lengths_arr.tolist(),
        "n_iter": diag["n_iter"],
        "converged": diag["converged"],
        "final_grad_norm": diag["final_grad_norm"],
        "topology_score": diag["final_f"],
        "prescription": prescription.value,
        "e_op": e_op,
        "edges": edges,
    }


# =============================================================================
# DRIVER + VALIDATION (IMPLEMENTATION_PLAN §10 Phase 6)
# =============================================================================

# Engine-fit reference values — taken from semiconductor_binding_engine
# solve_element on the present codebase (regenerated at startup, not hard-
# coded, so any future re-calibration of M_ALPHA / K / V_BR auto-updates).

# Topology assignments per the user-resolved decisions in the dispatch:
#   - C-12: 3-ring
#   - O-16: tetrahedron
#   - Ne-20: 5-ring (engine canonical for v1, despite KB describing bipyramid)
#   - Mg-24: octahedron
#   - Si-28: pentagonal bipyramid
NUCLEUS_SPECS: tuple[tuple[str, int, str], ...] = (
    ("He-4", 1, None),
    ("C-12", 3, "ring3"),
    ("O-16", 4, "tetrahedron"),
    ("Ne-20", 5, "ring5"),
    ("Mg-24", 6, "octahedron"),
    ("Si-28", 7, "pentagonal_bipyramid"),
)


def _engine_fit_R(name: str) -> float | None:
    """Run the existing semiconductor engine to obtain its R_engine fit
    (the "comparison target" the variational engine should approximate)."""
    from scripts.vol_6_periodic_table.simulations.semiconductor_binding_engine import (
        make_octahedron,
        make_pentagonal_bipyramid,
        make_ring,
        make_tetrahedron,
        solve_element,
    )

    targets = {
        "He-4": (1, 2, 4, 3727.379, None),
        "C-12": (3, 6, 12, 11174.863, lambda R: make_ring(3, R)),
        "O-16": (4, 8, 16, 14895.080, lambda R: make_tetrahedron(R)),
        "Ne-20": (5, 10, 20, 18617.730, lambda R: make_ring(5, R)),
        "Mg-24": (6, 12, 24, 22335.793, lambda R: make_octahedron(R)),
        "Si-28": (7, 14, 28, 26053.188, lambda R: make_pentagonal_bipyramid(R)),
    }
    if name not in targets or targets[name][4] is None:
        return None
    n_alpha, Z, A, mass, geo_func = targets[name]
    R_factor, _ = solve_element(name, n_alpha, Z, A, mass, geo_func, verbose=False)
    return float(R_factor) * D_PROTON_FM


def validate_against_engine_fits(
    prescription: str | Y0Prescription = Y0Prescription.GEOMETRIC_MEAN,
    e_op: float = E_0_DEFAULT,
    max_iter: int = 200,
    grad_tol: float = 1e-5,
    verbose: bool = False,
) -> dict:
    """Run all 5 alpha-cluster nuclei + He-4 degeneracy check.

    Returns a per-nucleus result dict.  Used by sweep_y0_prescriptions and the
    standalone driver below.
    """
    results = {}
    for name, n_alpha, topo in NUCLEUS_SPECS:
        if n_alpha == 1:
            r = solve_inter_alpha_equilibrium(name, n_alpha, topo, e_op=e_op)
        else:
            r = solve_inter_alpha_equilibrium(
                name,
                n_alpha,
                topo,
                e_op=e_op,
                y0_prescription=prescription,
                max_iter=max_iter,
                grad_tol=grad_tol,
                verbose=verbose,
            )
        # Attach engine-fit comparison
        try:
            R_eng = _engine_fit_R(name)
        except Exception as exc:  # pragma: no cover
            R_eng = None
            r["engine_error"] = str(exc)
        r["R_engine"] = R_eng
        if R_eng is not None and r.get("R_engine_equivalent") is not None:
            r["error_pct"] = (r["R_engine_equivalent"] - R_eng) / R_eng * 100.0
        else:
            r["error_pct"] = None
        results[name] = r
    return results


def sweep_y0_prescriptions(e_op: float = E_0_DEFAULT, max_iter: int = 200, verbose: bool = False) -> dict:
    """Run all 4 §4 fallback prescriptions on all 5 nuclei.  Used to identify
    which prescription closes Mg-24 to ~1%."""
    out = {}
    for p in Y0_PRESCRIPTIONS:
        if verbose:
            print(f"\n=== Prescription: {p.value} ===", flush=True)
        out[p.value] = validate_against_engine_fits(prescription=p, e_op=e_op, max_iter=max_iter, verbose=verbose)
    return out


def _print_table(results: dict, prescription_name: str = "geometric_mean") -> None:
    """Pretty-print a per-nucleus prediction table."""
    print()
    print("=" * 100)
    print(f"Prescription: {prescription_name}")
    print("=" * 100)
    print(
        f"{'Nucleus':8s} {'n_α':>4s} {'Topology':>20s}  {'R_pred':>9s} {'R_engine':>9s}  "
        f"{'err%':>8s} {'R_NN':>9s}  {'|S11|sum':>10s} {'|∇U|':>10s} {'iters':>6s}"
    )
    print("-" * 100)
    for name, r in results.items():
        if r.get("degenerate"):
            print(
                f"{name:8s} {1:>4d} {'(single α)':>20s}   {'—':>9s} {'—':>9s}   {'—':>8s} {'—':>9s}  {'—':>10s} {'—':>10s} {'—':>6s}"
            )
            continue
        Rpr = r["R_engine_equivalent"]
        Reg = r["R_engine"]
        err = r.get("error_pct")
        R_nn = r["R_predicted_geometric_mean"]
        f_final = r["f_final"]
        gnorm = r["final_grad_norm"]
        n_it = r["n_iter"]
        err_str = f"{err:+8.3f}" if err is not None else "    n/a"
        Rpr_str = f"{Rpr:9.3f}"
        Reg_str = f"{Reg:9.3f}" if Reg is not None else "      n/a"
        Rnn_str = f"{R_nn:9.3f}"
        print(
            f"{name:8s} {r['n_alpha']:>4d} {r['topology']:>20s}  "
            f"{Rpr_str} {Reg_str}  {err_str} {Rnn_str}  "
            f"{f_final:10.3e} {gnorm:10.3e} {n_it:>6d}"
        )


# =============================================================================
# COMMAND-LINE DRIVER
# =============================================================================
if __name__ == "__main__":
    print("=" * 80)
    print("AVE INTER-ALPHA VARIATIONAL EQUILIBRIUM ENGINE")
    print("Configuration via S_11 minimisation; closed-form R is the seed only.")
    print("=" * 80)

    print(f"\nE_0       = {E_0_DEFAULT:.3f} MeV")
    print(f"K_intra   = {K_INTRA:.5f}")
    print(f"Q_alpha   = {Q_ALPHA:.2f}")
    print(f"E_bond    = {E_BOND:.3f} MeV")
    print(f"E_anti    = {E_ANTI:.3f} MeV")
    print(f"Z0_vac    = {Z_0_VAC} Ohm")
    print()

    t0 = time.time()
    sweep = sweep_y0_prescriptions(verbose=False, max_iter=200)
    dt = time.time() - t0
    for p_name, results in sweep.items():
        _print_table(results, prescription_name=p_name)
    print(f"\nTotal sweep time: {dt:.1f} s")
