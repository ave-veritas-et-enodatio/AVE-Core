"""Substrate-native graded-vacuum impedance-network operator + isolation eigensolver.

Build-A (Stages 0-3) of the electron-Q coupled-network discriminating test.
Prereg: research/2026-06-19_electron-Q-coupled-network_prereg.md
        (frozen commit 4ae50ba0; the FIRST commit of this branch).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS MODULE IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
GOAL  : derive the electron bound-mode Q from the substrate-native graded-vacuum
        impedance network. CHORD = alpha moves echo->chord (Q ~ 1/alpha = 137 from
        alpha-FREE inputs). ECHO = it does not. PRIOR = ECHO (the alpha-free cold
        cage gives Q ~ 30.8, NOT 137; test_l3_mass_cage.py:25).

SCOPE : Build-A = Stages 0-3 ONLY. This module builds:
          * STAGE 1: L_native = adjoint_tetrahedral_divergence . D . tetrahedral_gradient
                     on the diamond/srs tetrahedral stencil (NOT the Cartesian
                     7-pt Laplacian). D block-diagonal in (bulk K / shear G).
          * STAGE 2: the NON-HERMITIAN generalized eigenproblem for the ISOLATION
                     leg (H_couple OFF, circulator OFF): bulk channel with the
                     mu-load SHORT Gamma=-1 confinement BC + an EM matched
                     loss-port (Gamma_EM=0 boundary admittance making L non-Hermitian).
                     Q = |Re omega| / (2 |Im omega|).
          * STAGE 3: lossless (EM port closed -> Q=inf) + Nyquist sanity.
        H_couple, the coupled solve, and Fork-A coupling are Build-B -- NOT here.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-NATIVE-CHECK (walked BEFORE any numerical code, per operating principle 1)
═══════════════════════════════════════════════════════════════════════════════
  * K4 / stencil : the spatial operator is the TETRAHEDRAL gradient/divergence on
                   the diamond-K4 stencil (4 tetrahedral diagonal offsets,
                   TETRA_OFFSETS, cosserat_field_3d.py:134). The composition
                   adjoint_div . grad is the native diamond Laplacian
                   (div(grad) r^2 = const, div(grad) linear = 0, verified). The
                   Cartesian 7-pt Laplacian (crystal_engine.py:154,
                   master_equation_fdtd.py:124) is FORBIDDEN (HR1) and never imported.
  * Cosserat     : two ORTHOGONAL grades carried by D (block-diagonal):
                   - bulk scalar V  = the A1 dilatation MASS-3 (Heaviside scalar),
                   - shear/Cosserat = the (2,3) micro-rotation CHARGE-3 winding.
                   Never a shared (V_inc, V_ref) phasor (A1-perp-T2,
                   master-equation.md:20; the genesis-24 double-count caution).
  * Op14         : the confinement wall = a mu-load SHORT (Z_core->0, Gamma->-1,
                   settled PR#260). The Op14 saturation exponent is swept per
                   DEC-1 (sqrt(S) primary, S^{1/4} sensitivity).
  * phase vs real: the eigenproblem is posed in REAL-space on the lattice field
                   (the complex-omega of a spatial operator). Q = |Re w|/(2|Im w|)
                   is a coordinate-free spectral ratio; no phase-space phi^2 claim
                   is at issue at the isolation rung.

═══════════════════════════════════════════════════════════════════════════════
THE ALPHA-LEAK + THE alpha-FREE RATIO MANDATE (HR2, Finding 1)
═══════════════════════════════════════════════════════════════════════════════
RHO_BULK = xi^2 mu_0 / (P_C ell^2) with P_C = 8 pi alpha (constants.py:664,400),
so RHO_BULK ~ 1/(8 pi alpha) and EVERY bare impedance magnitude
(Z_shear = rho_bulk c_shear, Z_bulk = sqrt2 rho_bulk c_0) CARRIES alpha.

This module therefore uses ONLY the DIMENSIONLESS, rho-CANCELLING impedance RATIO
between the two MECHANICAL channels (DEC-4: bulk K + shear G):

    Z_bulk / Z_shear = (rho c_L) / (rho c_T) = c_L / c_T = sqrt(10/3) = 1.825742...

  alpha-FREE provenance of the ratio (crystal_engine.py:27, DERIVED, not knob-set):
    c_L^2 / c_T^2 = 2(1-nu)/(1-2 nu) = (K + 4G/3)/G |_{K=2G} = 10/3  at nu_vac=2/7.
  rho (= RHO_BULK, the ONLY alpha-carrier) cancels identically in the ratio, so
  the ratio is exactly alpha-INVARIANT. No bare RHO_BULK / Z magnitude ever enters.

  RECONCILIATION FLAG (surfaced, not silently fixed): the prereg's headline figure
  Z_bulk/Z_shear = sqrt2 * sqrt(10/3) = 2.582 COMPOUNDS two distinct transverse
  references -- the EM-PHOTON speed sqrt(G/rho)=c0 (the sqrt2 = c_bulk/c_photon =
  sqrt(K/G), _bulk.py:102) AND the MECHANICAL-SHEAR speed c_T (crystal_engine.py:96).
  For the TWO-MECHANICAL-CHANNELS build (bulk K vs mechanical shear G, DEC-4) the
  physically-correct channel ratio is c_L/c_T = sqrt(10/3) alone. Both candidates
  are alpha-free and alpha-invariant, so the ambiguity does NOT affect any
  chord/echo bin -- it would only shift the bulk/shear gap LOCATION. The module
  exposes BOTH (RATIO_BULK_SHEAR_MECH primary; RATIO_BULK_SHEAR_PHOTON sensitivity).

═══════════════════════════════════════════════════════════════════════════════
ALLOWED alpha-FREE INPUTS (HR2; each greppably provenanced)
═══════════════════════════════════════════════════════════════════════════════
  Z_0           constants.py:99    characteristic impedance (used only as a LABEL;
                                   never as a bare magnitude in a Q-determining ratio)
  c_0           constants.py:95    speed of light (sets dimensionless dispersion only)
  nu_vac = 2/7  constants.py:532   -> c_L/c_T via 2(1-nu)/(1-2nu)=10/3
  kappa_tilde   cosserat_field_3d.py:94  = 6/5 (electron (2,3) torus, pq/(p+q)) -- the
    = 6/5                          chiral coupling; provenance crystal-graft-v2_result.md
  L_NODE        constants.py:257   lattice pitch (dimensionless dx only)
  lattice geom  chiral_lattice.build_srs_net / build_diamond_net, TETRA_OFFSETS
FORBIDDEN: Q_TANK=1/ALPHA (cvr_model.py:72), coupled_resonator k=2*alpha defaults,
  any bare RHO_BULK / Z_shear / Z_bulk magnitude. None are imported (import-guarded).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# alpha-FREE inputs ONLY (HR2). NU_VAC=2/7 (constants.py:532), C_0/Z_0 as labels.
from ave.core.constants import C_0, NU_VAC, Z_0
from ave.topological.cosserat_field_3d import (
    KAPPA_TILDE_ELECTRON,  # = 6/5, alpha-free electron (2,3) torus factor (:94)
    TETRA_OFFSETS,
    adjoint_tetrahedral_divergence,
    tetrahedral_gradient,
)

# ─────────────────────────────────────────────────────────────────────────────
# IMPORT-GUARD (anti-circularity, HR2): assert no alpha-carrier leaked into globals.
# Q_TANK (=1/alpha) and the ELECTRON instance must NOT be reachable here.
# ─────────────────────────────────────────────────────────────────────────────
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported"
assert "RHO_BULK" not in globals(), "second-leak: bare RHO_BULK magnitude must NOT be imported"

# ─────────────────────────────────────────────────────────────────────────────
# alpha-FREE dimensionless ratios (the ONLY Q-determining mechanical quantities).
# ─────────────────────────────────────────────────────────────────────────────
#   c_L^2/c_T^2 = 2(1-nu)/(1-2nu) = 10/3 at nu_vac=2/7 (crystal_engine.py:27, DERIVED).
CL2_OVER_CT2: float = 2.0 * (1.0 - NU_VAC) / (1.0 - 2.0 * NU_VAC)  # = 10/3
#   primary channel ratio: bulk(K) vs MECHANICAL shear(G); rho cancels -> alpha-free.
RATIO_BULK_SHEAR_MECH: float = float(np.sqrt(CL2_OVER_CT2))  # = sqrt(10/3) ~ 1.82574
#   sensitivity: bulk vs EM-PHOTON reference (the sqrt2 = sqrt(K/G), _bulk.py:102).
RATIO_BULK_SHEAR_PHOTON: float = float(np.sqrt(2.0) * np.sqrt(CL2_OVER_CT2))  # ~ 2.58199


def _native_scalar_laplacian(field: np.ndarray) -> np.ndarray:
    """The substrate-native diamond/srs Laplacian on a SCALAR field:
        L = adjoint_tetrahedral_divergence ( tetrahedral_gradient(field) ).
    Uses the tetrahedral stencil (TETRA_OFFSETS, 4 diamond diagonals) ONLY --
    the Cartesian 7-pt Laplacian is FORBIDDEN (HR1) and never called.

    Numerically verified: L(linear) = 0 (interior, machine eps); L(r^2) = const
    (uniform, zero std). Symmetric POSITIVE-semidefinite (it IS the stiffness form
    = grad^T grad up to the discrete inner product), so the eigenproblem is
    L x = omega^2 M x with omega^2 >= 0 -- NO sign flip needed. (Verified by
    test_native_laplacian_is_symmetric_positive_semidefinite; the nullspace is the
    constant/rigid modes.)

    Args:
        field: (N, N, N) real scalar (the A1 dilatation amplitude).
    Returns:
        (N, N, N) real: the native Laplacian-action.
    """
    grad = tetrahedral_gradient(field[..., None])  # (N,N,N,1,3)
    div_in = np.asarray(grad)[..., 0, :]  # (N,N,N,3)
    return np.asarray(adjoint_tetrahedral_divergence(div_in))


def _native_vector_laplacian(field: np.ndarray) -> np.ndarray:
    """Native diamond/srs Laplacian on a VECTOR field (the shear/Cosserat omega
    grade), applied component-wise with the SAME tetrahedral stencil.

    Args:
        field: (N, N, N, 3) real (the Cosserat micro-rotation amplitude).
    Returns:
        (N, N, N, 3) real.
    """
    out = np.empty_like(field)
    for c in range(field.shape[-1]):
        out[..., c] = _native_scalar_laplacian(field[..., c])
    return out


@dataclass(frozen=True)
class NativeOperatorConfig:
    """Frozen geometry/constitutive config for the native operator (alpha-free).

    N            : cube edge (lattice sites per side).
    dx           : dimensionless lattice pitch (1.0; physical L_NODE folds out of Q).
    ratio_bs     : bulk/shear impedance RATIO (default = mechanical, sqrt(10/3)).
    kappa_tilde  : chiral coupling 6/5 (electron (2,3) torus, alpha-free); carried
                   for Build-B H_couple, NOT used in the isolation D-block.
    """

    N: int = 16
    dx: float = 1.0
    ratio_bs: float = RATIO_BULK_SHEAR_MECH
    kappa_tilde: float = KAPPA_TILDE_ELECTRON

    def assert_alpha_free(self) -> None:
        """Hard assert: every config number is alpha-free + the ratio is finite."""
        assert np.isfinite(self.ratio_bs) and self.ratio_bs > 0
        assert abs(self.kappa_tilde - 6.0 / 5.0) < 1e-12, "kappa_tilde must be 6/5"
        # ratio_bs must equal one of the two alpha-free derived ratios.
        assert any(
            abs(self.ratio_bs - r) < 1e-9
            for r in (RATIO_BULK_SHEAR_MECH, RATIO_BULK_SHEAR_PHOTON)
        ), "ratio_bs must be an alpha-free derived ratio (mech or photon)"


def stencil_provenance() -> dict:
    """Return the native-stencil provenance (for the no-Cartesian-Laplacian gate).

    Confirms TETRA_OFFSETS are the 4 diamond tetrahedral diagonals and that this
    module routes through the tetrahedral operators, never the Cartesian 7-pt.
    """
    return {
        "tetra_offsets": tuple(tuple(int(x) for x in p) for p in TETRA_OFFSETS),
        "n_offsets": len(TETRA_OFFSETS),
        "operator": "adjoint_tetrahedral_divergence . tetrahedral_gradient",
        "cartesian_7pt_imported": False,
    }


# ═════════════════════════════════════════════════════════════════════════════
# STAGE 2 -- the ISOLATION-leg non-Hermitian eigensolver
# ═════════════════════════════════════════════════════════════════════════════
# H_couple OFF, circulator OFF (DEC-2). Bulk channel ONLY, with:
#   * the mu-load SHORT Gamma=-1 confinement (Z_core->0): a saturated Gaussian core
#     where S(A)->0 raises the local stiffness c_eff^2 = c0^2 / S(A), gapping a
#     bound breathing mode above the continuum (the canonical wall,
#     crystal_engine.gamma_bulk: Z_eff=sqrt(S)->0 => Gamma->-1).
#   * an EM matched loss-port (Gamma_EM=0): a boundary admittance -i*sigma on the
#     outer layer (radiative absorption), making the operator NON-HERMITIAN ->
#     complex omega -> finite Q. This is a BARE matched loss-port (DEC-4),
#     NOT a TKI transducer (avoids the units-bridge-Q hazard F4).
# Q = |Re omega| / (2 |Im omega|).
# ═════════════════════════════════════════════════════════════════════════════


def saturation_kernel(A: np.ndarray, *, exponent: float, S_min: float) -> np.ndarray:
    """The Op14 saturation kernel S(A) = (1 - A^2)^exponent, clipped to [S_min, 1].

    DEC-1: run BOTH exponents -- exponent=0.5 (sqrt(S), primary, mu-load-justified)
    and exponent=0.25 (S^{1/4}, sensitivity). alpha-FREE: pure (1-A^2) kernel, no
    Q_TANK, no gamma_em_sq.
    """
    base = np.maximum(1.0 - A**2, 0.0)
    S = base**exponent
    return np.clip(S, S_min, 1.0)


def saturated_core_strain(N: int, *, frac: float, sigma: float) -> np.ndarray:
    """A POSITED saturated longitudinal-bulk core (Gaussian dilatation well, the
    consistency-class POSIT, DEC-3 single-node 0_1 unknot, ASSUMED-not-derived,
    falsifier F8). A(r) = frac * exp(-r^2 / (2 sigma^2)), centred. alpha-FREE
    (geometry only)."""
    c = N // 2
    i, j, k = np.indices((N, N, N))
    r2 = (i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2
    return frac * np.exp(-r2 / (2.0 * sigma**2))


def stiffness_profile(
    A: np.ndarray, *, exponent: float, S_min: float
) -> np.ndarray:
    """Local bulk stiffness c_eff^2 / c0^2 = 1 / S(A) (the bulk-trap: ->1/S_min in
    the saturated core, =1 in vacuum). This is the DIMENSIONLESS stiffness field
    D(r) in L_native = adjoint_div . D . grad. alpha-FREE (kernel only)."""
    S = saturation_kernel(A, exponent=exponent, S_min=S_min)
    return 1.0 / S


def _native_laplacian_with_stiffness(field: np.ndarray, D: np.ndarray) -> np.ndarray:
    """Variable-coefficient native operator  L[field] = adjoint_div( D * grad(field) )
    on the diamond tetrahedral stencil. D is the per-site stiffness c_eff^2/c0^2.

    This is the SELF-ADJOINT divergence-form Laplacian (the discrete analogue of
    div(D grad)), which keeps the stiffness-weighted operator SYMMETRIC (so the
    Hermitian part stays a proper stiffness; loss enters ONLY via the EM port).
    """
    grad = np.asarray(tetrahedral_gradient(field[..., None]))[..., 0, :]  # (N,N,N,3)
    flux = D[..., None] * grad  # D * grad  (divergence-form coefficient)
    return np.asarray(adjoint_tetrahedral_divergence(flux))


def em_loss_port_mask(N: int, *, port_thickness: int) -> np.ndarray:
    """Boundary-layer mask for the EM matched loss-port (Gamma_EM=0): the outer
    `port_thickness` shell of the cube. The non-Hermitian admittance -i*sigma acts
    ONLY here -- a matched radiative port (DEC-4), NOT a transducer. alpha-FREE."""
    mask = np.zeros((N, N, N), dtype=bool)
    t = port_thickness
    mask[:t, :, :] = mask[-t:, :, :] = True
    mask[:, :t, :] = mask[:, -t:, :] = True
    mask[:, :, :t] = mask[:, :, -t:] = True
    return mask


@dataclass(frozen=True)
class IsolationConfig:
    """ISOLATION-leg config (validate-on-known, GATE1). Cold-cage inputs.

    Defaults track the prereg GATE1 spec scaled to a tractable dense eigensolve.
    The FULL GATE1 spec is N=72; dense eig at N=72 is 72^3 ~ 3.7e5 DOF (intractable
    dense), so the dense path runs a reduced N and the result's Q is asserted to be
    the SAME ORDER (the validate-on-known band [20,45] is order-of-magnitude, not a
    knife-edge -- HR3). A convergence sweep over N witnesses Q-stability.
    """

    N: int = 24
    frac: float = 0.999  # A_cap (saturated core amplitude)
    sigma: float = 3.0  # core width (lattice units)
    S_min: float = 1e-3
    exponent: float = 0.5  # Op14: sqrt(S) primary (DEC-1)
    port_thickness: int = 4  # EM matched loss-port shell (proxy for pml=12 @ N=72)
    sigma_port: float = 0.15  # matched-port admittance strength (Gamma_EM=0 scale)
    em_port_closed: bool = False  # GATE2: True => Gamma_EM=-1 (lossless), Q=inf

    def assert_inputs_alpha_free(self) -> None:
        """Hard guard: every isolation input is alpha-free + physically sane.
        The kernel is pure (1-A^2)^exp clipped to [S_min,1]; NO Q_TANK / gamma_em_sq
        / 137 enters. exponent is one of the two DEC-1 values."""
        assert 0.0 < self.frac < 1.0
        assert self.sigma > 0 and self.S_min > 0
        assert self.exponent in (0.5, 0.25), "DEC-1: exponent must be 0.5 or 0.25"
        assert self.port_thickness >= 1 and 2 * self.port_thickness < self.N
        assert self.sigma_port >= 0.0


def _build_isolation_matrices(cfg: IsolationConfig):
    """Assemble the dense (L, M, port_diag) for the isolation eigenproblem.

    L = the symmetric divergence-form native stiffness adjoint_div(D grad), with D
        the saturated-core stiffness profile c_eff^2/c0^2 = 1/S(A). REAL symmetric.
    M = mass = identity (dimensionless rho=1; rho cancels from Q -- alpha-free).
    port = the EM matched-loss diagonal (boundary admittance). The non-Hermitian
        operator is H = L - i*sigma_port*diag(port)  (open port) or H = L (closed).
    Returns (L, M, port_diag, A_field).
    """
    N = cfg.N
    ndof = N**3
    A = saturated_core_strain(N, frac=cfg.frac, sigma=cfg.sigma)
    D = stiffness_profile(A, exponent=cfg.exponent, S_min=cfg.S_min)

    def apply_L(vec):
        f = vec.reshape(N, N, N)
        return _native_laplacian_with_stiffness(f, D).reshape(ndof)

    # Build the dense matrix column-by-column (linear operator).
    eye = np.eye(ndof)
    L = np.column_stack([apply_L(eye[:, k]) for k in range(ndof)])
    L = 0.5 * (L + L.T)  # enforce exact symmetry (machine-eps asymmetry from roll)

    port = em_loss_port_mask(N, port_thickness=cfg.port_thickness).reshape(ndof).astype(float)
    M = np.eye(ndof)
    return L, M, port, A


def _build_sparse_stiffness(cfg: IsolationConfig):
    """Assemble the divergence-form native stiffness L = adjoint_div(D grad) as an
    EXPLICIT SCIPY SPARSE (csr) matrix, by probing the linear operator with batched
    unit impulses on a periodic cube. The stencil is short-range (4 tetrahedral
    diagonals), so the matrix is sparse (<= ~27 nonzeros/row after div.grad).

    Built sparse so scipy shift-invert eigs can reach the prereg N regime (N~72 is
    ~3.7e5 DOF, impossible dense; sparse + shift-invert finds only the few modes
    near omega~2.87). alpha-FREE: D = 1/S(A), pure (1-A^2)^exp kernel.

    Returns (L_csr, port_diag, A_field).
    """
    from scipy import sparse

    N = cfg.N
    ndof = N**3
    A = saturated_core_strain(N, frac=cfg.frac, sigma=cfg.sigma)
    D = stiffness_profile(A, exponent=cfg.exponent, S_min=cfg.S_min)

    # ---- vectorized factored build: L = Div @ diag(D_exp) @ Grad ----------------
    # tetrahedral_gradient: grad[...,j] += 0.25*p_j*(roll(V,-p) - V)  for each p.
    # adjoint_tetrahedral_divergence: out += 0.25*p_j*(roll(T_j,+p) - T_j).
    # Build Grad (3*ndof x ndof) and Div (ndof x 3*ndof) as offset-diagonal sparse
    # operators (periodic roll = permutation), with NO per-site Python loop.
    lin = np.arange(ndof)

    def roll_perm(shift):
        """Permutation index for jnp.roll(field, shift, axes=(0,1,2)) on the
        flattened (N,N,N) C-order array."""
        idx3 = np.unravel_index(lin, (N, N, N))
        ri = ((idx3[0] - shift[0]) % N, (idx3[1] - shift[1]) % N, (idx3[2] - shift[2]) % N)
        return np.ravel_multi_index(ri, (N, N, N))

    I = sparse.identity(ndof, format="csr")
    grad_blocks = [sparse.csr_matrix((ndof, ndof)) for _ in range(3)]
    for p in TETRA_OFFSETS:
        # roll(V, -p): value at site x is V(x+p). As an operator on the column
        # vector V, (roll(V,-p))[x] = V[(x+p) mod N] => permutation with shift -p.
        P = sparse.csr_matrix(
            (np.ones(ndof), (lin, roll_perm((-p[0], -p[1], -p[2])))), shape=(ndof, ndof)
        )
        delta = P - I  # roll(V,-p) - V
        for j in range(3):
            if p[j] != 0:
                grad_blocks[j] = grad_blocks[j] + 0.25 * p[j] * delta
    Grad = sparse.vstack(grad_blocks, format="csr")  # (3*ndof, ndof)

    div_blocks = [sparse.csr_matrix((ndof, ndof)) for _ in range(3)]
    for p in TETRA_OFFSETS:
        # roll(T, +p): (roll(T,+p))[x] = T[(x-p) mod N] => permutation with shift +p.
        Pp = sparse.csr_matrix(
            (np.ones(ndof), (lin, roll_perm((p[0], p[1], p[2])))), shape=(ndof, ndof)
        )
        delta = Pp - I  # roll(T,+p) - T
        for j in range(3):
            if p[j] != 0:
                div_blocks[j] = div_blocks[j] + 0.25 * p[j] * delta
    Div = sparse.hstack(div_blocks, format="csr")  # (ndof, 3*ndof)

    Dexp = sparse.diags(np.tile(D.reshape(ndof), 3))  # diag(D) on each component
    L = (Div @ Dexp @ Grad).tocsr()
    L = 0.5 * (L + L.T)  # symmetrize (machine-eps asymmetry)
    port = em_loss_port_mask(N, port_thickness=cfg.port_thickness).reshape(ndof).astype(float)
    return L, port, A


def _select_bound_mode(omega, vecs, cfg, port):
    """Pick the gapped bound breathing mode: localised on the saturated core,
    away from the EM port boundary. Returns the best dict or None."""
    N = cfg.N
    c = N // 2
    i, j, k = np.indices((N, N, N))
    r = np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2).reshape(-1)
    core_mask = r <= max(cfg.sigma * 1.5, 2.0)
    port_mask = port.astype(bool)
    best = None
    for idx in range(len(omega)):
        w = omega[idx]
        if w.real <= 1e-6:
            continue
        v = np.abs(vecs[:, idx]) ** 2
        v = v / (v.sum() + 1e-30)
        core_frac = float(v[core_mask].sum())
        port_frac = float(v[port_mask].sum())
        loc = core_frac - port_frac
        if best is None or (loc > best["loc"] and core_frac > 0.05):
            best = {"idx": idx, "omega": complex(w), "loc": loc,
                    "core_frac": core_frac, "port_frac": port_frac}
    return best


def solve_isolation_Q_sparse(cfg: IsolationConfig, *, k: int = 24, omega_guess: float = 2.87) -> dict:
    """Sparse shift-invert isolation solve -- reaches the prereg N regime.

    H x = omega^2 x with H = L - i*sigma_port*diag(port) (open) or L (closed).
    scipy.sparse.linalg.eigs with sigma=omega_guess^2 finds the k eigenpairs nearest
    the cold-cage bound frequency. Q = |Re omega|/(2|Im omega|).
    """
    from scipy.sparse import diags
    from scipy.sparse.linalg import eigs

    cfg.assert_inputs_alpha_free()
    L, port, A = _build_sparse_stiffness(cfg)
    if cfg.em_port_closed:
        H = L.astype(complex)
    else:
        H = L.astype(complex) - 1j * cfg.sigma_port * diags(port)
    H = H.tocsc()
    shift = float(omega_guess) ** 2
    try:
        lam, vecs = eigs(H, k=min(k, H.shape[0] - 2), sigma=shift, which="LM")
    except Exception as exc:  # pragma: no cover -- solver fallback
        return {"ok": False, "reason": f"eigs failed: {exc}"}
    omega = np.sqrt(lam.astype(complex))
    omega = np.where(omega.real < 0, -omega, omega)
    best = _select_bound_mode(omega, vecs, cfg, port)
    if best is None:
        return {"ok": False, "reason": "no localised bound mode found"}
    w = best["omega"]
    re, im = float(w.real), float(abs(w.imag))
    Q = re / (2.0 * im) if im > 1e-30 else float("inf")
    return {
        "ok": True, "method": "sparse-shift-invert", "exponent": cfg.exponent, "N": cfg.N,
        "omega_re": re, "omega_im": im, "omega": w, "Q": float(Q),
        "core_frac": best["core_frac"], "port_frac": best["port_frac"],
        "loc": best["loc"], "em_port_closed": cfg.em_port_closed,
    }


def solve_isolation_Q(cfg: IsolationConfig) -> dict:
    """Solve the ISOLATION-leg non-Hermitian eigenproblem and return the bound-mode
    Q = |Re omega| / (2 |Im omega|).

    H x = omega^2 M x, with H = L - i*sigma_port*diag(port) (EM matched loss-port
    open) or H = L (closed, GATE2). The bound mode is selected as the lowest
    NON-NULLSPACE eigenvalue whose eigenvector is LOCALISED on the saturated core
    interior (PML/port-excluded peak), gapped above omega~0.

    Returns a dict with omega (complex), Q, the real/imag parts, the mode-selection
    diagnostics (peak bin, localisation), and the dt-Nyquist witness.
    """
    cfg.assert_inputs_alpha_free()
    L, M, port, A = _build_isolation_matrices(cfg)
    N = cfg.N

    if cfg.em_port_closed:
        H = L.astype(complex)  # Gamma_EM = -1: closed, lossless reactive cage
    else:
        H = L.astype(complex) - 1j * cfg.sigma_port * np.diag(port)

    # Generalized eigenproblem H x = lam M x  (M = I -> standard).
    lam, vecs = np.linalg.eig(H)
    omega = np.sqrt(lam.astype(complex))  # omega^2 = lam
    # physical branch: Re(omega) > 0
    omega = np.where(omega.real < 0, -omega, omega)

    # ---- mode selection: the gapped bound breathing mode localised on the core ----
    c = N // 2
    i, j, k = np.indices((N, N, N))
    r = np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2).reshape(-1)
    core_mask = (r <= max(cfg.sigma * 1.5, 2.0))
    port_mask = port.astype(bool)

    best = None
    for idx in range(len(lam)):
        w = omega[idx]
        if w.real <= 1e-6:  # skip nullspace / near-zero (constant/rigid modes)
            continue
        v = np.abs(vecs[:, idx]) ** 2
        v = v / (v.sum() + 1e-30)
        core_frac = float(v[core_mask].sum())
        port_frac = float(v[port_mask].sum())
        # localisation score: energy on the core, away from the port boundary.
        loc = core_frac - port_frac
        if best is None or (loc > best["loc"] and core_frac > 0.05):
            best = {
                "idx": idx,
                "omega": complex(w),
                "loc": loc,
                "core_frac": core_frac,
                "port_frac": port_frac,
            }

    if best is None:  # pragma: no cover -- degenerate solve
        return {"ok": False, "reason": "no localised bound mode found"}

    w = best["omega"]
    re, im = float(w.real), float(abs(w.imag))
    Q = re / (2.0 * im) if im > 1e-30 else float("inf")
    return {
        "ok": True,
        "exponent": cfg.exponent,
        "N": N,
        "omega_re": re,
        "omega_im": im,
        "omega": w,
        "Q": float(Q),
        "core_frac": best["core_frac"],
        "port_frac": best["port_frac"],
        "loc": best["loc"],
        "em_port_closed": cfg.em_port_closed,
    }
