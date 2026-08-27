"""BUILD-EO1-T2X — the tone-solve harness on the TRANSVERSE VECTOR container.

═══════════════════════════════════════════════════════════════════════════════
INSTRUMENT FENCE (read before quoting anything this module returns)
═══════════════════════════════════════════════════════════════════════════════
INSTRUMENT-GRADE INFRASTRUCTURE. This module MINTS NO PHYSICS CLAIMS, adjudicates
NO FORK, and runs no discriminator. It is a port of an existing harness onto an
existing container; every number it can produce is either (i) an implementation
identity of the shipped operator or (ii) a validate-on-known reproduction of a
number some OTHER lane already banked. The discriminator that will consume it is
pre-registered separately and runs after this lane, on frozen geometry.

WHAT IT IS: `solve_tone_vector` / `VectorTermination` / `interface_two_port_vector`
are the (N, degree, 2) transverse-vector twins of the (N, degree) SCALAR
harness in `ave.solvers.harmonic_balance_srs` (`solve_tone`, `Termination`,
`interface_two_port`). The port is SMALL BY CONSTRUCTION because
`harmonic_balance_srs.apply_M` is literally the c = 1 case of
`transverse_graded_scatter.vector_graded_step`: the same scatter einsum and the
same directed-edge CONNECT permutation, both already dtype-generic and therefore
already complex-safe. Nothing about the operator is re-derived here.

WHAT IT REUSES, UNTOUCHED (never re-implemented):
  * the graded scatter + connect step, the SO(2)-equivariance gate and the
    admittance/loading maps -- `ave.solvers.transverse_graded_scatter`
    (`vector_graded_step`, `scatter_coeffs`, `bond_admittance`,
    `saturation_kernel`, `gate_so2_equivariance`, `energy_Y`);
  * the undirected-bond tables, the plane-crossing port finder and the scalar
    wave-fit / de-embedding algebra -- `ave.solvers.harmonic_balance_srs`
    (`build_bond_table`, `crossing_ports`, `fit_two_waves`, `fit_k`,
    `interface_two_port`, `signed_gamma`).

═══════════════════════════════════════════════════════════════════════════════
SECTOR HEADER (wall-taxonomy.md:160 -- a claim missing any of the three is not
yet a claim about a wall; stated here so no consumer has to reconstruct it)
═══════════════════════════════════════════════════════════════════════════════
  CHANNEL     : TRANSVERSE (the 2-component polarization pair of the ratified
                vector-TLM container, chiral_lattice_vector.py:4-5). NOT the
                A1/longitudinal scalar slot -- that is the scalar harness's
                channel, reached here only as the c = 1 restriction used for
                parity. NOT the Cosserat micro-rotation: the polarization pair
                is def-0pt1ac-fenced optical activity, which this module does
                not even implement (no per-node twist is wired). A1 _|_ T2; no
                winding, charge or spin observable exists anywhere in this file.
  AXIS        : the x-directed propagation axis of the carrier net, with the
                grading applied per UNDIRECTED BOND (never per node -- see the
                structural-null guard below).
  PHASE-STATE : COLD-to-GRADED steady state. Every solve is an AC steady state
                (a phasor fixed point, "everything moves, nothing changes"): no
                time axis, no transient, no damping device. The only energy exit
                is a declared TERMINATION, which is a boundary condition and
                never a bulk loss term. Ax3 losslessness is untouched by
                construction (S_u^2 = I even when graded) and is a computed
                receipt (`energy_Y_phasor`), not an assumption.

═══════════════════════════════════════════════════════════════════════════════
THE FOUR GUARDS, CARRIED EXPLICITLY
═══════════════════════════════════════════════════════════════════════════════
(b) STRUCTURAL-NULL TRAP -- harmonic_balance_srs.py:191-195 verbatim: "any null
    obtained through a per-node broadcast is an artifact, not a result." This
    module inherits the trap in full: a per-node-UNIFORM admittance CANCELS
    identically in a_j = 2 Y_j / sum_k Y_k (transverse_graded_scatter.py:29-36,
    gate_t1a_global_uniform). CONSEQUENCE FOR THIS FILE'S OWN NEGATIVE CONTROL:
    the A = 0 control (`|Gamma| == 0`) is a UNIFORM-BROADCAST NULL. It is
    guaranteed by that cancellation identity and is therefore an INSTRUMENT
    CONTROL -- it demonstrates the measurement chain adds no spurious echo of
    its own. It is NOT evidence about any wall, and must never be quoted as one.
    A physics null on this instrument must be shown non-broadcast BY
    CONSTRUCTION (a grading that is genuinely per-bond-mixed, receipted by
    `transverse_graded_scatter.gate_t1b_boundary_set`), which is the
    discriminator lane's job, not this one's.
(c) ALPHA-ECHO TRAP -- the module is alpha-FREE BY CONSTRUCTION (import guard
    below; the same triad the scalar harness and the graded scatter assert). A
    is a dimensionless per-bond grading amplitude; no dimensionful V_yield /
    V_snap, hence no ALPHA, is reachable from this namespace. Nothing here maps
    a residual imbalance onto |Gamma|^2 = 1 - alpha, and no consumer may: the
    engine's radiative leak is literally `1.0 - alpha` (cvr_model.py:161), so
    that reading is an INSTRUMENT ECHO, adjudicated CIRCULAR, "do NOT pose it".
(d) FREEZE + FENCE -- the validate-on-known geometry is FROZEN in this module as
    `KNOWN_CASE_CHAIN` (a module constant, not a per-test literal), so a
    validation number cannot be produced against a quietly-retuned geometry. The
    instrument fence is the block at the top of this docstring.
(e) FL-4, THE LIVE SILENT-ZERO TRAP -- see `solve_tone_vector`. MEASURED on this
    branch, scalar harness, ring[12] at the exact ring mode:
    `solve_tone(..., term=None)` returns ||v|| = 0.000e+00 with converged=True
    AND residual_rel = 0.000e+00 in FOUR configurations (warmstart 0/50, x0 None,
    and x0 warm-started AT the true mode). Cause: theta is an INPUT
    (harmonic_balance_srs.py:534,:537), so with no imposed drive the system is
    HOMOGENEOUS and 0 is its exact solution; the relative-residual receipt then
    divides 0 by a 1e-300 floor and reads as a perfect solve. The port FIXES
    this rather than documenting it -- `solve_tone_vector` refuses the
    homogeneous case by default and always carries a computed `nontrivial`
    receipt. "converged" is not "non-zero" (R58 section 4).

═══════════════════════════════════════════════════════════════════════════════
R40-B2a CARRIED STAMP (cite, never load-bear silently)
═══════════════════════════════════════════════════════════════════════════════
This module poses phasor KCL on the same n-port amplitude space as the vacuum
varactor scatter, whose (V_inc, V_ref) port-phasor reading carries the in-file
demotion stamp (vacuum_varactor_scatter.py:72, family longitudinal-TLM-port,
BIAS-DEBT), scoped to the A1/longitudinal carrier reading. What is load-borne
here is only the network ALGEBRA -- ports as wave amplitudes, the
admittance-weighted shunt KCL, the connect permutation. No bulk-wave-carrier
interpretation is asserted anywhere in this file.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.solvers.harmonic_balance_srs import (
    build_bond_table,
    crossing_ports,
    fit_two_waves,
    interface_two_port,
    signed_gamma,
)
from ave.solvers.transverse_graded_scatter import (
    LOADS,
    bond_admittance,
    saturation_kernel,
    scatter_coeffs,
    vector_graded_step,
)

# ---------------------------------------------------------------------------
# ANTI-LEAK IMPORT-GUARD (guard (c)): the tone solve is alpha-FREE BY
# CONSTRUCTION -- the same triad the scalar harness and the graded scatter
# assert. A is dimensionless; no dimensionful V_yield / V_snap is reachable.
# ---------------------------------------------------------------------------
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported here"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"
assert "V_SNAP" not in globals(), "alpha-adjacent-leak: dimensionful V_SNAP must NOT be imported"

__all__ = [
    "KNOWN_CASE_CHAIN",
    "VectorTermination",
    "VectorToneSolution",
    "apply_M_vector",
    "bond_gamma_vector",
    "build_bond_table",
    "crossing_ports",
    "energy_Y_phasor",
    "fit_k_vector",
    "fit_two_waves_vector",
    "graded_coeffs",
    "interface_two_port_vector",
    "make_vector_termination",
    "node_voltage_vector",
    "plane_binned_voltage_vector",
    "port_admittance",
    "signed_gamma",
    "solve_tone_vector",
]

# ---------------------------------------------------------------------------
# FROZEN VALIDATE-ON-KNOWN GEOMETRY (guard (d)). Pinned here, in the module, so
# a validation number can never be produced against a quietly-retuned geometry.
# The carrier is the degree-2 ring FIXTURE (harmonic_balance_srs.build_ring_net,
# carrier tag "ring-z2-fixture" -- a known-case fixture, NOT a physics carrier),
# on which the plane terminations are EXACT matched absorbers (a directed bond
# is the only DOF crossing the cut) and the graded/cold junction's reflection is
# the ANALYTIC Fresnel step Gamma = (sqrt(S) - 1)/(sqrt(S) + 1) with no fitting
# and no de-embedding needed -- which is what makes it a known case.
# ---------------------------------------------------------------------------
KNOWN_CASE_CHAIN = {
    "N": 48,          # ring nodes (one bond per unit x)
    "theta": 0.4,     # posited tone, rad/step (canonical (0, pi))
    "x_src": 5.5,     # source plane: +x drive imposed, backward slot absorbed
    "x_I": 20.0,      # the cold -> graded interface plane
    "x_grade_hi": 44.0,  # upper edge of the graded region (bond midpoints)
    "x_abs": 34.5,    # far-side load plane (inside the graded medium)
    "feed_fit": (7.0, 19.0),   # cold-side fit window (cells)
    "slab_fit": (21.0, 33.0),  # graded-side fit window (cells)
    "probe_bonds": (10.5, 14.5, 18.5, 19.5),  # cold-side exact-port probes
}


# ═════════════════════════════════════════════════════════════════════════════
# 1. GRADING -> PER-PORT ADMITTANCE -> PER-NODE SCATTER COEFFICIENTS
#    (a two-line bridge between the scalar harness's BondTable and the
#    transverse module's loading maps; no new arithmetic)
# ═════════════════════════════════════════════════════════════════════════════
def port_admittance(bt, A_bond: np.ndarray, load: str, *, Y0: float = 1.0) -> np.ndarray:
    """(N, degree) per-directed-port admittance from a per-BOND grading.

    Y_b comes from `transverse_graded_scatter.bond_admittance` UNCHANGED (the
    load string is asserted there -- sign-lock w35sn2bq3 -- so a typo raises
    rather than silently building the wrong-sign wall), and is gathered onto the
    directed ports through the scalar harness's own `port_bond` table. Both end
    ports of a bond therefore share ONE Y_b, and both polarization components
    see the same Y (the component-scalar T2 fence: Y carries no component axis).
    """
    A_bond = np.asarray(A_bond, dtype=np.float64)
    if A_bond.shape != (bt.n_bonds,):
        raise ValueError(f"A_bond must be per-bond {(bt.n_bonds,)}; got {A_bond.shape}")
    if load not in LOADS:  # defensive twin of the sign-lock raise (fail before the gather)
        raise ValueError(f"load must be one of {LOADS}; got {load!r} (sign-lock w35sn2bq3)")
    return bond_admittance(A_bond, load, Y0=Y0)[bt.port_bond]


def graded_coeffs(bt, A_bond: np.ndarray, load: str, *, Y0: float = 1.0):
    """(a_nodes, Y_port) for a per-bond grading: a[u, j] = 2 Y_j / sum_k Y_k.

    `scatter_coeffs` is the transverse module's own function, reused untouched
    (it asserts passivity: sum Y finite and positive at every node)."""
    Y_port = port_admittance(bt, A_bond, load, Y0=Y0)
    return scatter_coeffs(Y_port), Y_port


# ═════════════════════════════════════════════════════════════════════════════
# 2. THE ONE-STEP OPERATOR IN PHASOR FORM ON THE VECTOR CONTAINER
# ═════════════════════════════════════════════════════════════════════════════
def apply_M_vector(a_nodes: np.ndarray, conn: tuple, v: np.ndarray) -> np.ndarray:
    """One scatter+connect application M v on (N, degree, 2) COMPLEX phasors.

    This IS `transverse_graded_scatter.vector_graded_step` -- the shipped
    engine step -- called on a complex array. Both of its operations are
    dtype-generic: the scatter einsum "nd,ndc->nc" promotes real coefficients
    against complex phasors, and the CONNECT permutation is an index gather into
    `np.zeros_like(V_inc)`, which preserves the complex dtype. So the real-field
    engine step and the complex phasor step are literally the SAME code path;
    the scalar harness's `apply_M` is its c = 1 restriction (parity receipt in
    the test suite, both directions).

    The only thing added here is the dtype promotion, so that a caller passing a
    real array does not silently get a real-only propagation of a complex
    problem."""
    return vector_graded_step(np.asarray(v, dtype=np.complex128), a_nodes, conn)


def node_voltage_vector(a_nodes: np.ndarray, v: np.ndarray) -> np.ndarray:
    """(N, 2) common node-voltage phasor V_u = sum_j a_j v_j per component --
    the shunt-junction KCL voltage 2 sum Y V^inc / sum Y, per polarization
    component (vacuum_varactor_scatter.py:162-165 tensored with I_2)."""
    return np.einsum("nd,ndc->nc", a_nodes, np.asarray(v, dtype=np.complex128))


def energy_Y_phasor(v: np.ndarray, Y_port: np.ndarray) -> float:
    """Y-weighted line-power norm for COMPLEX phasors:
    E_Y = sum_{u,p,c} Y_{b(u,p)} |v[u,p,c]|^2.

    The real-field twin `transverse_graded_scatter.energy_Y` is reused as-is for
    real fields; it computes `V * V`, which is |V|^2 only on the reals, so the
    phasor ledger needs |v|^2 explicitly. Agreement of the two on a real field
    is a test receipt, so this is an extension of the existing gate and not a
    reimplementation of it. Conservation under `apply_M_vector` is a gate."""
    Y = np.asarray(Y_port, dtype=np.float64)[:, :, None]
    return float((Y * np.abs(np.asarray(v)) ** 2).sum())
