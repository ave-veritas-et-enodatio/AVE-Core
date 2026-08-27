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
    engine's radiative leak is literally `return 1.0 - alpha`
    (src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py:171-178 -- line number
    VERIFIED on this branch; the brief's ":161" points at gamma_of_A's
    docstring, not at the leak), so that reading is an INSTRUMENT ECHO,
    adjudicated CIRCULAR, "do NOT pose it".
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
    "known_case_chain",
    "make_vector_termination",
    "node_voltage_vector",
    "plane_binned_voltage_vector",
    "plane_termination",
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


# ═════════════════════════════════════════════════════════════════════════════
# 3. TERMINATIONS ON THE VECTOR CONTAINER (the scaffold)
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class VectorTermination:
    """Source/absorber termination: incident PORT slots with imposed 2-vectors.

    The transverse twin of `harmonic_balance_srs.Termination`. One structural
    difference, and it is deliberate: a terminated slot is a directed PORT, and
    the imposed quantity is that port's full incident polarization 2-vector.

    WHY PER-PORT AND NOT PER-COMPONENT: a bond has ONE impedance, so the
    scaffold that terminates it is one physical boundary condition on the whole
    transverse field there -- a per-COMPONENT termination would smuggle in
    un-owned birefringent structure exactly the way a per-component loading map
    would (the T2 component-scalar fence, transverse_graded_scatter.py:37-41).
    A linearly polarized launch is expressed as drive = (s, 0): component 1 is
    imposed to ZERO, which is a boundary condition, not an absence of one.

    ports  : (n_T,) flat directed-port indices (u*degree + p) whose incident
             wave is imposed.
    paired : (n_T,) for each terminated slot, the flat SRC port whose V_ref
             would have CONNECTed into it -- the wave the scaffold absorbs,
             matched at the bond's own Y. A boundary condition, never a bulk
             loss term (Ax3 untouched).
    drive  : (n_tones, n_T, 2) complex imposed incident phasors s_hat. An
             all-zero drive is a pure absorber -- and makes the tone problem
             HOMOGENEOUS, which `solve_tone_vector` refuses by default (FL-4).
    """

    ports: np.ndarray
    paired: np.ndarray
    drive: np.ndarray

    def __post_init__(self):
        object.__setattr__(self, "ports", np.asarray(self.ports, dtype=np.int64))
        object.__setattr__(self, "paired", np.asarray(self.paired, dtype=np.int64))
        object.__setattr__(self, "drive", np.asarray(self.drive, dtype=np.complex128))
        if self.drive.ndim != 3 or self.drive.shape[1:] != (len(self.ports), 2):
            raise ValueError(
                f"drive must be (n_tones, n_terminated_ports, 2); got {self.drive.shape} "
                f"for {len(self.ports)} ports"
            )
        if len(self.paired) != len(self.ports):
            raise ValueError("paired must match ports")

    @property
    def n_tones(self) -> int:
        return int(self.drive.shape[0])

    def is_homogeneous(self, tone_index: int = 0) -> bool:
        """True when this termination imposes NO drive at the given tone -- i.e.
        the tone's fixed-point problem is homogeneous and 0 solves it exactly
        (the FL-4 condition; see `solve_tone_vector`)."""
        return not (len(self.ports) and bool(np.any(self.drive[tone_index])))


def make_vector_termination(net, bt, conn: tuple, specs: list, n_tones: int) -> VectorTermination:
    """Assemble a VectorTermination from per-slot-set specs.

    specs : list of (flat_incident_slots, drive) where drive is either
            (n_tones, 2) -- applied uniformly over those slots -- or
            (n_tones, n_slots, 2). Overlapping slot sets are rejected (a slot
            can carry only one boundary condition). The paired SRC ports are
            resolved from the connect map (dst -> src), exactly as the scalar
            twin does."""
    src_flat, dst_flat = conn
    dst_to_src = {int(dj): int(sj) for sj, dj in zip(src_flat, dst_flat)}
    ports, drives = [], []
    for slots, drive in specs:
        slots = np.asarray(slots, dtype=np.int64)
        drive = np.asarray(drive, dtype=np.complex128)
        if drive.shape == (n_tones, 2):
            drive = np.repeat(drive[:, None, :], len(slots), axis=1)
        if drive.shape != (n_tones, len(slots), 2):
            raise ValueError(f"drive shape {drive.shape} != {(n_tones, len(slots), 2)}")
        ports.append(slots)
        drives.append(drive)
    ports_all = np.concatenate(ports) if ports else np.zeros(0, dtype=np.int64)
    if len(np.unique(ports_all)) != len(ports_all):
        raise ValueError("terminated slots overlap between specs")
    drive_all = (
        np.concatenate(drives, axis=1)
        if drives
        else np.zeros((n_tones, 0, 2), dtype=np.complex128)
    )
    missing = [int(t) for t in ports_all if int(t) not in dst_to_src]
    if missing:
        raise ValueError(f"terminated slots absent from the connect map: {missing[:5]}")
    paired = np.array([dst_to_src[int(t)] for t in ports_all], dtype=np.int64)
    return VectorTermination(ports=ports_all, paired=paired, drive=drive_all)


def plane_termination(net, bt, conn: tuple, planes_drives: list, n_tones: int) -> VectorTermination:
    """Convenience assembler: terminate the incident slots of every bond
    crossing each named x-plane.

    planes_drives : list of (plane_cells, drive_fwd, drive_bwd), each drive
                    (n_tones, 2) complex OR None. fwd = the +x-traveling
                    incident slots at the plane, bwd = the -x-traveling ones
                    (the split is `harmonic_balance_srs.crossing_ports`, reused
                    untouched -- including its fail-loud empty-crossing guard
                    and its wrap-aware plane test).

    None means DO NOT TERMINATE that direction, and it is load-bearing: a
    far-side load plane must leave the +x direction FREE (imposing 0 there
    would delete the transmitted wave instead of absorbing it, and the
    "absorber" would be a perfect mirror wearing an absorber's name). A
    one-sided cut is the matched absorber; a two-sided cut is a hard boundary.

    This lives in the module rather than in a test helper so the known-case
    scaffold pattern is FROZEN with the geometry (guard (d)), not re-typed per
    caller."""
    specs = []
    for plane, drive_fwd, drive_bwd in planes_drives:
        f, b = crossing_ports(net, bt, plane)
        for slots, drive in ((f, drive_fwd), (b, drive_bwd)):
            if drive is None:
                continue
            specs.append((slots, np.asarray(drive, dtype=np.complex128)))
    if not specs:
        raise ValueError("plane_termination: every direction was None -- no boundary condition")
    return make_vector_termination(net, bt, conn, specs, n_tones)


# ═════════════════════════════════════════════════════════════════════════════
# 4. PER-TONE LINEAR SOLVE ON THE VECTOR CONTAINER
#    (the algebraic fixed point, with computed receipts and the FL-4 fix)
# ═════════════════════════════════════════════════════════════════════════════
@dataclass
class VectorToneSolution:
    """One tone's transverse phasor solution + its receipts (always computed).

    v            : (N, degree, 2) complex incident-port phasors.
    v_norm       : ||v||_F -- carried EXPLICITLY because the relative residual
                   alone cannot distinguish "solved" from "identically zero".
    nontrivial   : v_norm > v_floor (COMPUTED, never declared). See the FL-4
                   block in `solve_tone_vector`.
    homogeneous  : the tone's problem had no imposed drive, so 0 is an exact
                   solution of it.
    residual_abs : ||e^{i theta} v - M v|| on the free slots.
    residual_rel : residual_abs / v_norm -- and +inf when the solution is
                   trivial, so a gate written as `residual_rel < tol` FAILS on
                   a silent zero instead of passing it. (The scalar twin
                   divides by a 1e-300 floor and returns 0.0 there, which reads
                   as a perfect solve; that is exactly FL-4.)
    converged    : the LINEAR SOLVER's own flag, verbatim. It is NOT a verdict:
                   `converged and not nontrivial` is the FL-4 signature.
    """

    theta: float
    v: np.ndarray
    v_norm: float
    nontrivial: bool
    homogeneous: bool
    residual_abs: float
    residual_rel: float
    converged: bool
    n_matvec: int
    method: str


def _embed(x_free: np.ndarray, v_s: np.ndarray, mask_F: np.ndarray) -> np.ndarray:
    v = v_s.copy()
    v[mask_F] = x_free
    return v


def solve_tone_vector(
    a_nodes: np.ndarray,
    conn: tuple,
    theta: float,
    term: "VectorTermination | None" = None,
    tone_index: int = 0,
    *,
    tol: float = 1e-11,
    maxiter: int = 20000,
    warmstart: int = 0,
    x0: "np.ndarray | None" = None,
    require_nontrivial: bool = True,
    v_floor: float = 1e-12,
) -> VectorToneSolution:
    """Solve the source-terminated transverse phasor fixed point at one tone.

    Equations, per polarization component and coupled only through the shared
    per-node coefficients (the operator is S_u (x) I_2):

        e^{i theta} v_F = (M v)_F   on free port slots F,
        v_T             = s_hat     on terminated port slots T.

    Eliminating v_T gives (e^{i theta} I - M_FF) x = M_FT s_hat, solved
    matrix-free (scipy LGMRES) with an optional physical-transient warm start
    v <- e^{-i theta}(P_free M v + inject) -- the damped power iteration whose
    contraction IS the termination's absorption. The residual receipt is
    computed from the operator on the ASSEMBLED solution, so the evidence is
    solver-agnostic: whatever produced v, the receipt is the norm of the
    fixed-point defect.

    ┌── GUARD (e): FL-4, THE SILENT-ZERO TRAP -- FIXED HERE, NOT DOCUMENTED ──┐
    │ theta is an INPUT, not an eigenvalue. With no imposed drive the system  │
    │ is HOMOGENEOUS: (e^{i theta} I - M) x = 0, whose exact solution is      │
    │ x = 0, which the linear solver duly returns with info == 0. MEASURED on │
    │ the scalar twin (ring[12] at the exact ring mode, this branch):         │
    │ ||v|| = 0.000e+00, converged = True, residual_rel = 0.000e+00 in FOUR   │
    │ configurations -- warmstart 0 and 50 from a zero start, AND warm-started│
    │ AT the true mode with x0 = v_true. A warm start cannot rescue it: the   │
    │ right-hand side is zero, so the Krylov solve has nothing to build on.   │
    │                                                                         │
    │ THE FIX (two layers, both fail-loud):                                   │
    │   1. the homogeneous case is DETECTED BEFORE the solve and REFUSED by   │
    │      default -- a source-free fixed point at a POSITED theta is an      │
    │      EIGENPROBLEM, not a linear solve, and asking this function for one │
    │      is a category error that should raise, not return a zero;          │
    │   2. every returned solution carries a COMPUTED `nontrivial` receipt,   │
    │      and `residual_rel` is +inf (never 0.0) when the solution is        │
    │      trivial, so a downstream gate written as `residual_rel < tol`      │
    │      fails on a silent zero instead of passing it.                      │
    │ `require_nontrivial=False` re-opens the degenerate branch for a caller  │
    │ that deliberately wants it (a null control); the receipts still say so. │
    │ "converged" is not "non-zero" (R58 section 4).                          │
    └─────────────────────────────────────────────────────────────────────────┘
    """
    from scipy.sparse.linalg import LinearOperator, lgmres

    a_nodes = np.asarray(a_nodes, dtype=np.float64)
    N, d = a_nodes.shape
    n_ports = N * d
    ndof = n_ports * 2

    homogeneous = term is None or term.is_homogeneous(tone_index)
    if homogeneous and require_nontrivial:
        raise ValueError(
            "solve_tone_vector: the tone problem is HOMOGENEOUS (no imposed drive at "
            f"tone_index={tone_index}; term is {'None' if term is None else 'all-zero'}). "
            "theta is an INPUT here, so (e^{i theta} I - M) x = 0 and the linear solver "
            "returns the exact solution x = 0 with converged=True and a relative residual "
            "of 0.0 -- the FL-4 silent zero, measured in four configurations on the scalar "
            "twin including a warm start AT the true mode. A source-free fixed point at a "
            "posited theta is an EIGENPROBLEM, not a linear solve: impose a drive through "
            "a VectorTermination, or pass require_nontrivial=False if the trivial branch is "
            "genuinely what you want (the returned receipts will say nontrivial=False)."
        )

    mask_port = np.zeros(n_ports, dtype=bool)
    if term is not None and len(term.ports):
        mask_port[term.ports] = True
    # flatten order of (N, degree, 2) is port-major, component-minor
    mask_T = np.repeat(mask_port, 2)
    mask_F = ~mask_T
    eith = np.exp(1j * float(theta))

    v_s = np.zeros(ndof, dtype=np.complex128)
    if term is not None and len(term.ports):
        v_s.reshape(-1, 2)[term.ports] = term.drive[tone_index]

    def M_flat(vflat: np.ndarray) -> np.ndarray:
        return apply_M_vector(a_nodes, conn, vflat.reshape(N, d, 2)).ravel()

    b = M_flat(v_s)[mask_F]
    nF = int(mask_F.sum())
    n_mv = [1]  # the b evaluation

    def matvec(x: np.ndarray) -> np.ndarray:
        n_mv[0] += 1
        vx = np.zeros(ndof, dtype=np.complex128)
        vx[mask_F] = x
        return eith * x - M_flat(vx)[mask_F]

    x_init = None
    if x0 is not None:
        x_init = np.asarray(x0, dtype=np.complex128).ravel()[mask_F]
    if warmstart > 0:
        v_w = np.zeros(ndof, dtype=np.complex128) if x_init is None else _embed(x_init, v_s, mask_F)
        inv_eith = np.exp(-1j * float(theta))
        for _ in range(int(warmstart)):
            v_new = inv_eith * M_flat(v_w)
            v_new[mask_T] = v_s[mask_T]
            v_w = v_new
            n_mv[0] += 1
        x_init = v_w[mask_F]

    A = LinearOperator((nF, nF), matvec=matvec, dtype=np.complex128)
    x, info = lgmres(A, b, x0=x_init, rtol=tol, atol=0.0, maxiter=maxiter)
    v = _embed(x, v_s, mask_F)

    defect = (eith * v - M_flat(v))[mask_F]
    v_norm = float(np.linalg.norm(v))
    residual_abs = float(np.linalg.norm(defect))
    nontrivial = bool(v_norm > float(v_floor))
    residual_rel = residual_abs / v_norm if nontrivial else float("inf")

    if not nontrivial and require_nontrivial:
        raise ValueError(
            f"solve_tone_vector: the assembled solution is numerically ZERO "
            f"(||v|| = {v_norm:.3e} <= v_floor = {v_floor:.1e}) while the linear solver "
            f"reported info={info}. This is the FL-4 signature -- converged is not "
            "non-zero (R58 section 4). Check that the termination actually imposes a "
            "drive at this tone_index; pass require_nontrivial=False to accept it."
        )

    return VectorToneSolution(
        theta=float(theta),
        v=v.reshape(N, d, 2),
        v_norm=v_norm,
        nontrivial=nontrivial,
        homogeneous=bool(homogeneous),
        residual_abs=residual_abs,
        residual_rel=float(residual_rel),
        converged=bool(info == 0),
        n_matvec=int(n_mv[0]),
        method="lgmres" + (f"+warmstart{warmstart}" if warmstart else ""),
    )


# ═════════════════════════════════════════════════════════════════════════════
# 5. WAVE-FIT + DE-EMBEDDING INSTRUMENTS ON THE VECTOR CONTAINER
# ═════════════════════════════════════════════════════════════════════════════
def plane_binned_voltage_vector(net, a_nodes: np.ndarray, v: np.ndarray,
                                x_lo_cells: float, x_hi_cells: float):
    """Node-voltage phasors averaged over thin x-planes in [x_lo, x_hi] (cells).

    The transverse twin of `harmonic_balance_srs.plane_binned_voltage`:
    averaging each distinct x-plane (over y, z and motif) isolates the
    x-directed plane-wave content. Returns (x in CARTESIAN length where one
    bond = 1.0, V of shape (n_planes, 2) -- the mean node-voltage phasor per
    plane, PER POLARIZATION COMPONENT). The component axis is carried through
    the average untouched: no polarization observable is formed here."""
    xu = net.pos[:, 0] / net.a_cell
    Vn = node_voltage_vector(a_nodes, v)
    m = (xu >= x_lo_cells) & (xu <= x_hi_cells)
    if not np.any(m):
        raise ValueError(f"no nodes in the fit window [{x_lo_cells}, {x_hi_cells}] cells")
    xr = np.round(xu[m], 6)
    xs = np.unique(xr)
    Vb = np.array([Vn[m][xr == x].mean(axis=0) for x in xs])
    return xs * net.a_cell, Vb


def fit_two_waves_vector(x: np.ndarray, V: np.ndarray, k: float) -> dict:
    """Least-squares fit V(x)[:, c] ~ a_c e^{-ikx} + b_c e^{+ikx}, both
    components at once against ONE k.

    ONE k, not two, because the container's dispersion is component-blind by
    construction (the graded step is S_u (x) I_2 and commutes with a global
    SO(2) polarization rotation -- transverse_graded_scatter.gate_so2_equivariance,
    reused as-is). Fitting a per-component k would manufacture a birefringence
    the operator cannot express.

    Returns a, b as (2,) complex arrays and the JOINT relative fit residual
    (a computed receipt over both components together). Per-component agreement
    with the scalar `harmonic_balance_srs.fit_two_waves` is a test receipt."""
    x = np.asarray(x, dtype=np.float64)
    V = np.asarray(V, dtype=np.complex128)
    if V.ndim != 2 or V.shape[1] != 2:
        raise ValueError(f"V must be (n_planes, 2); got {V.shape}")
    E = np.column_stack([np.exp(-1j * k * x), np.exp(+1j * k * x)])
    coef, *_ = np.linalg.lstsq(E, V, rcond=None)
    resid = float(np.linalg.norm(E @ coef - V)) / max(float(np.linalg.norm(V)), 1e-300)
    return {"a": coef[0].copy(), "b": coef[1].copy(), "k": float(k), "resid_rel": resid}


def fit_k_vector(x: np.ndarray, V: np.ndarray, k_lo: float, k_hi: float) -> dict:
    """Measure k by minimizing the JOINT two-wave fit residual over [k_lo, k_hi]
    (bounded scalar minimization; the fit at the optimum is returned whole)."""
    from scipy.optimize import minimize_scalar

    res = minimize_scalar(
        lambda k: fit_two_waves_vector(x, V, k)["resid_rel"],
        bounds=(float(k_lo), float(k_hi)),
        method="bounded",
        options={"xatol": 1e-10},
    )
    return fit_two_waves_vector(x, V, float(res.x))


def bond_gamma_vector(net, bt, v: np.ndarray, plane_cells: float, k: float,
                      x_ref_cells: float, *, amp_floor: float = 1e-14) -> dict:
    """The EXACT (V_inc, V_ref) port-phasor reflection reading at a single-bond
    cut, referenced to the plane x_ref.

    SCOPE FENCE, enforced: this is the ONE-DIMENSIONAL known-case reading. It
    requires the plane to cross EXACTLY ONE bond, because then the bond's two
    directed incident phasors ARE the forward and backward wave amplitudes --
    no fitting, no de-embedding, no plane-wave assumption. On a multi-bond cut
    (any 3-D carrier) that identification is false and this function raises;
    use the fit + `interface_two_port_vector` chain there instead.

        Gamma_c = (v_bwd_c / v_fwd_c) e^{2 i k (x_ref - x_mid)}

    A component with no forward content (|v_fwd_c| <= amp_floor -- e.g. the
    idle component of a linearly polarized launch) returns NaN and is reported
    False in `excited`, rather than returning a 0/0 artifact.

    NOTE on the cold reading: on a cold uniform chain the backward phasor is
    IDENTICALLY 0.0 (nothing scatters backward at all), so the cold control
    returns |Gamma| == 0 EXACTLY, bit-level. That exactness is the
    uniform-broadcast cancellation identity showing itself -- guard (b): it is
    an instrument control, not evidence about any wall."""
    f, b = crossing_ports(net, bt, plane_cells)
    if len(f) != 1:
        raise ValueError(
            f"bond_gamma_vector: plane x={plane_cells} crosses {len(f)} bonds; the exact "
            "port-phasor reading is defined only on a SINGLE-bond (1-D chain) cut. Use "
            "plane_binned_voltage_vector + fit_k_vector + interface_two_port_vector on a "
            "multi-bond cut."
        )
    vf = np.asarray(v, dtype=np.complex128).reshape(-1, 2)[f[0]]
    vb = np.asarray(v, dtype=np.complex128).reshape(-1, 2)[b[0]]
    bond = int(bt.port_bond.ravel()[f[0]])
    x_mid = float(bt.b_x0[bond] + 0.5 * bt.b_dx[bond])
    phase = np.exp(2j * float(k) * (float(x_ref_cells) - x_mid) * net.a_cell)
    excited = np.abs(vf) > float(amp_floor)
    gamma = np.where(excited, vb / np.where(excited, vf, 1.0) * phase, np.nan + 0j)
    return {"gamma": gamma, "excited": excited, "v_fwd": vf, "v_bwd": vb,
            "x_mid": x_mid, "x_ref": float(x_ref_cells), "k": float(k)}


def interface_two_port_vector(runs: list, *, per_component: bool = False,
                              amp_floor: float = 1e-14) -> dict:
    """Multi-load de-embedding of a transverse interface's own two-port response.

    `runs` is a list of dicts with keys a, b, c, d, each a (2,) complex
    polarization vector referenced at the interface plane (feed-side incident /
    reflected, far-side transmitted / returning), i.e. the vector twin of the
    scalar de-embedder's run record.

    DEFAULT (per_component=False) -- ONE scalar (Gamma, T, Gamma', T') fitted
    over ALL components of ALL runs. This is not an averaging convenience: it
    is the S_u (x) I_2 MODEL, which the shipped operator satisfies by
    construction, and the returned `resid_rel` is the COMPUTED receipt that the
    model held on this data. A polarization-dependent interface would show up
    as residual rather than be silently averaged into a wrong scalar
    (reconcile-don't-declare). The scalar algebra itself is
    `harmonic_balance_srs.interface_two_port`, called untouched on the stacked
    rows -- so there is exactly one de-embedding implementation in the tree.

    per_component=True -- de-embed each EXCITED component separately and report
    `anisotropy` = |Gamma_0 - Gamma_1| (NaN when only one component carries
    content, e.g. a linearly polarized launch). Use it to test the isotropy
    rather than assume it; the default already fails loudly through resid_rel.
    Its `gamma` key is the mean of the two component Gammas when both are
    excited (the single excited one otherwise) -- a CONVENIENCE only, and
    meaningless unless `anisotropy` is small, which is why `anisotropy` is
    returned beside it and never folded into it.

    Rows whose feed-side and far-side content are both below `amp_floor` carry
    no information and are dropped (an idle polarization component contributes
    an all-zero row that would otherwise inflate the row count without
    constraining anything); `n_rows` reports how many survived."""
    if len(runs) < 2:
        raise ValueError("need >= 2 load positions to separate Gamma from the load reflection")
    arr = [{key: np.asarray(r[key], dtype=np.complex128).reshape(2) for key in "abcd"}
           for r in runs]

    def _rows(comps):
        out = []
        for r in arr:
            for c in comps:
                if abs(r["a"][c]) <= amp_floor and abs(r["d"][c]) <= amp_floor:
                    continue
                out.append({k: complex(r[k][c]) for k in "abcd"})
        return out

    if not per_component:
        rows = _rows((0, 1))
        if len(rows) < 2:
            raise ValueError(
                f"interface_two_port_vector: only {len(rows)} rows carry content above "
                f"amp_floor={amp_floor:.1e} -- the de-embedding is underdetermined"
            )
        out = dict(interface_two_port(rows))
        out.update({"n_rows": len(rows), "n_runs": len(arr), "per_component": None})
        return out

    per = {}
    for c in (0, 1):
        rows = _rows((c,))
        per[c] = interface_two_port(rows) if len(rows) >= 2 else None
    g0 = per[0]["gamma"] if per[0] else None
    g1 = per[1]["gamma"] if per[1] else None
    aniso = abs(g0 - g1) if (g0 is not None and g1 is not None) else float("nan")
    return {"per_component": per, "anisotropy": float(aniso), "n_runs": len(arr),
            "gamma": g0 if g1 is None else (g1 if g0 is None else 0.5 * (g0 + g1))}


# ═════════════════════════════════════════════════════════════════════════════
# 6. THE FROZEN KNOWN-CASE FIXTURE (guard (d))
# ═════════════════════════════════════════════════════════════════════════════
def known_case_chain(A: float, load: str = "magnetic", *, Y0: float = 1.0) -> dict:
    """Build the FROZEN validate-on-known chain at grading amplitude A.

    Carrier: `harmonic_balance_srs.build_ring_net(KNOWN_CASE_CHAIN["N"])` -- the
    degree-2 ring FIXTURE, carrier tag "ring-z2-fixture", explicitly NOT a
    physics carrier. It is chosen precisely because it makes the answer known:

      * a plane cut crosses exactly ONE bond, so an imposed-incident termination
        is an EXACT matched absorber (the bond amplitude is the only DOF
        crossing the cut) -- no scaffold reflection to de-embed;
      * at the cold/graded junction the shunt algebra gives, exactly,
            Gamma = (Y_cold - Y_graded)/(Y_cold + Y_graded) = (sqrt(S) - 1)/(sqrt(S) + 1)
        under the magnetic (mu-load) map Y = Y0/sqrt(S) -- the ANALYTIC Fresnel
        step, with no fitted quantity anywhere in it;
      * the TLM bond transit is one step regardless of admittance, so the
        grading changes impedance and NOT delay: k = theta on both sides, which
        removes the last free parameter from the check.

    Returns net, bt, conn, a_nodes, Y_port and the frozen geometry, plus the
    analytic target `gamma_analytic` for this A and load."""
    from ave.solvers.harmonic_balance_srs import build_ring_net

    g = KNOWN_CASE_CHAIN
    net = build_ring_net(int(g["N"]))
    bt = build_bond_table(net)
    conn = net.connect_index()
    A_bond = np.zeros(bt.n_bonds)
    A_bond[(bt.b_mid > g["x_I"]) & (bt.b_mid < g["x_grade_hi"])] = float(A)
    a_nodes, Y_port = graded_coeffs(bt, A_bond, load, Y0=Y0)
    S = float(saturation_kernel(np.asarray(float(A))))
    # z = Z_graded/Z_cold: sqrt(S) for the magnetic (mu) map, 1/sqrt(S) for electric
    z = np.sqrt(S) if load == "magnetic" else 1.0 / np.sqrt(S)
    return {
        "net": net, "bt": bt, "conn": conn, "a_nodes": a_nodes, "Y_port": Y_port,
        "A_bond": A_bond, "A": float(A), "load": load, "S": S,
        "gamma_analytic": float((z - 1.0) / (z + 1.0)), "geom": dict(g),
    }
