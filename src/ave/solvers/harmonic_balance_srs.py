"""Harmonic-Balance Solver on the graded srs TLM network — phasor-domain KCL fixed point.

Build brief: _orchestration/2026-08-24_static-existence-build-brief.md (Stage 2).
Design ruling: research/2026-08-24_g1-ac-steady-state-walk_RECORD.md (the AC-steady-state
reframe; "everything moves, nothing changes" — the phasor description is a fixed point).
Epic: _orchestration/2026-08-24_static-existence-epic.md (guards 1-8 travel with any use).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS MODULE IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
GOAL  : pose the graded srs network's steady state DIRECTLY in the phasor domain:
        posit a tone set {theta_m} (rad/step), write per-tone Kirchhoff on the
        admittance-weighted shunt-junction scatter + directed-edge CONNECT map, and
        solve the algebraic fixed point

            e^{i theta_m} v_m = M(S) v_m + sources ,   M(S) = C @ blockdiag(S_u(Y)) ,

        with the varactor map Y_bond = Y0/sqrt(S(A_bond)) reading a per-bond
        saturation field. The S-field is itself an unknown of the SELF-CONSISTENT
        mode: A_bond is the cycle time-average envelope of the solution's own tone
        phasors (DP-1, below), so the tones couple through the shared S-field —
        the kernel's inter-tone coupling. No time axis. No damping device anywhere:
        the operator is the lossless scatter+connect map itself (Ax3 untouched by
        construction); the only energy exit is a declared matched TERMINATION
        (a boundary condition, never a bulk loss term).

NOT   : the P2 existence solve. This module is INSTRUMENT-GRADE INFRASTRUCTURE
        (means-test class A-prime): it mints no physics claims, adjudicates no fork,
        and runs no (2,3) tone set. The P2 run is gated on the G2 frozen prereg
        (build brief Stage 3), which is not this module's scope. Validation here is
        implementation-verification only (consistency-vs-emergence: consistency /
        instrument cross-validation classes; nothing in the emergence class).

═══════════════════════════════════════════════════════════════════════════════
THE PHASOR FIXED POINT (exact statement)
═══════════════════════════════════════════════════════════════════════════════
Time-domain step (the certified engine, chiral_lattice.py:294-300):
    V_ref[u] = S_u @ V_inc[u]   per node (shunt scatter),
    V_inc'.flat[dst] = V_ref.flat[src]   (CONNECT, a pure permutation, no sign).
Graded scatter (vacuum_varactor_scatter.py:156-185, the Class-C machinery,
research/drivers/engine_gamma_meanstest.py:289-308):
    S_ij = 2 Y_j / (sum_k Y_k) - delta_ij ,  per-DIRECTED-BOND admittance Y.
A steady tone V(t) = Re[v e^{i theta t}] (theta in rad/step; one step = one bond
transit) therefore satisfies the algebraic fixed point
    e^{i theta} v = M v ,        M = C @ blockdiag(S_u)          (autonomous)
    e^{i theta} v_F = (M v)_F ,  v_T = s_hat                     (source-terminated)
where T is the set of terminated incident slots (the scaffold: imposed incident
phasors; the paired outgoing wave is absorbed matched at the bond's own Y — the
KUBC / voltage-clamped boundary-condition CLASS, canon's homogenization row at
manuscript/ave-kb/common/translation-tables/translation-circuit.md:196,404; the
phrase "source termination" is the G1 walk's. The KUBC/SUBC Hill-Huet two-sided
BOUND is static/DC-fenced and is NOT used here — termination is a boundary
condition only, never an effective-property bound).

Losslessness: S_u^2 = I even when graded (S = 1 a^T - I with sum a_j = 2), and the
graded step conserves the Y-weighted energy E_Y = sum Y_p V_p^2 (the Class-C
driver's ledger, engine_gamma_meanstest.py:17-18). No damping exists in M; the
solve's only sink is the declared termination — power accounting is a computed
receipt, not an assumption.

═══════════════════════════════════════════════════════════════════════════════
THE S-FIELD RULE (DP-1, Grant-ratified — the envelope, NOT a snapshot)
═══════════════════════════════════════════════════════════════════════════════
The Axiom-4 argument A is the cycle time-average reactive-amplitude ENVELOPE of
the (V_inc, Phi_link)-type tank, per-sector against its own yield, "NOT an
instantaneous phase snapshot" (DP-1, manuscript/ave-kb/vol2/particle-physics/
ch01-topological-matter/substrate-perspective-electron.md:62; echoed at
common/saturation-rim-inversion.md:35). Its canonical C-state projection is
A^2_local = (sum_ports V_inc^2)/V_SNAP^2 (same leaf, :55-60). For a tone set with
distinct per-step phases the cross-tone terms time-average to zero, so the
envelope rule is DERIVED, not chosen:

    A_bond^2 = sum_m ( |v_m[fwd]|^2 + |v_m[bwd]|^2 ) / (2 * v_norm^2) ,

the bond-restricted DP-1 projection (fwd/bwd = the bond's two directed incident
ports; |v|^2/2 = the cycle mean of Re[v e^{i theta t}]^2). Because S is a
functional of the ENVELOPE, S is STATIC in steady state and each tone sees the
same graded network: the inter-tone coupling is the shared S-field. v_norm keys
the per-sector yield (DP-1 is per-sector): engine-natural default 1.0 == V_SNAP
in engine units for the scalar/A1-adjacent channel (the A1 bond compliance
saturates at V_snap, NOT V_yield — nonlinear-vacuum-capacitance.md:18; keying
this channel to V_yield would overstate saturation by 1/sqrt(alpha) ~ 11.7x).

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-NATIVE-CHECK (walked BEFORE any numerical code)
═══════════════════════════════════════════════════════════════════════════════
  * dynamics    : discrete srs scatter+connect TLM wave propagation, posed in the
                  phasor domain. The operator IS the certified one-step map — NOT
                  a Lagrangian minimization, NOT gradient descent, NOT a continuum
                  Helmholtz problem. The graph-Laplacian omega = sqrt(lambda) model
                  is REJECTED canon (fails the frozen 1/sqrt(3) velocity gate,
                  gives 1/sqrt(2) — srs-band-structure.md:49-67); the cold linear
                  limit of THIS operator is the arccos transmission-line map
                  omega_n(k) = omega_link * arccos(mu_n(k)/3), which validation
                  gate 1 computes against.
  * sector      : SCALAR channel on the srs-z3 carrier (the Class-C lane's), the
                  A1-adjacent longitudinal slot. The T2/Cosserat channel is NOT
                  wired in (A1 perpendicular to T2, master-equation.md:20); no
                  winding observable exists here. R40-B2a stamps on the
                  longitudinal-TLM-port reading travel with this reuse — see the
                  dated note at the end of this file (cite, never load-bear
                  silently; epic guard 6).
  * objective   : phasor-domain Kirchhoff fixed point on the Op5 shunt-junction
                  admittance scatter with the Op2/Axiom-4 varactor kernel —
                  AVE-native. Source-idle = scaffold-removability of the solution
                  ("the mirror is made of the thing it confines", G1 walk §2),
                  NOT an energy-functional minimum.
  * coordinates : unknowns are phasors on the directed ports = the (V_inc, V_ref)
                  phase-space coordinates, the impedance-matching frame. Any
                  comparison against a time-domain measurement must declare its
                  coordinate map (the gate-2 map: time-window isolation of the
                  front echo == matched-local-z absorption behind the interface).
  * Op14        : saturation enters ONLY as the per-bond admittance
                  Y = Y0/sqrt(S(A)) — the mu-load, Z_bond = Z0*sqrt(S) -> 0,
                  Gamma -> -1 (the SHORT). The reciprocal epsilon-load
                  (Z -> inf, Gamma -> +1) is FORBIDDEN (crystal_engine.py:466-468);
                  so is the transverse Op14 form Z_eff = Z0/sqrt(S) on this bond
                  grading (that cross-wiring is the genesis-24 double-count,
                  ave-kb CLAUDE.md INVARIANT-S2).
  * per-bond    : a per-NODE-uniform admittance CANCELS at the shunt junction
                  (vacuum_varactor_scatter.py:54 — the structural-null trap; epic
                  guard 4). Grading enters per DIRECTED bond; the cancellation is
                  a validated gate, and any null obtained through a per-node
                  broadcast is an artifact, not a result.
  * boundary    : confinement/reflection/absorption are BOUNDARY CONDITIONS
                  (Gamma at an interface, matched termination at a cut) — never a
                  bulk force term. No dS/dA force exists anywhere in this module.
  * observables : every receipt is computed from the solved state and the operator
                  itself (residual norms, power ledgers, fitted wave amplitudes) —
                  no algebraic-heuristic observables, no self-declared passes.
  * alpha-free  : the solver reads dimensionless A only; ALPHA / Q_TANK / ELECTRON
                  are never imported (guard asserts below). Tones are POSITED
                  numbers (rad/step): harmonic balance posits tones, not tube
                  phases (epic guard 8 — the alpha-agnostic imposition).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core.chiral_lattice import LatticeNet
from ave.solvers.vacuum_varactor_scatter import (
    bond_admittance_from_saturation,
    saturation_kernel,
)

# ─────────────────────────────────────────────────────────────────────────────
# ANTI-LEAK IMPORT-GUARD: alpha-FREE BY CONSTRUCTION (same triad as the varactor
# scatter). The solver reads dimensionless A and posited tones only.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported into the HB solver"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"
assert "V_SNAP" not in globals(), "alpha-adjacent-leak: dimensionful V_SNAP must NOT be imported (v_norm is engine-natural)"


# ═════════════════════════════════════════════════════════════════════════════
# 1. BOND BOOKKEEPING — undirected-bond tables on a LatticeNet
#    (engine-native re-derivation of the Class-C driver's Rig tables; the driver
#    research/drivers/engine_gamma_meanstest.py:191-243 is prereg-frozen
#    run-of-record code and is deliberately NOT imported.)
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class BondTable:
    """Undirected-bond bookkeeping for a LatticeNet.

    port_bond[u, p] : undirected bond id of directed port (u, p).
    bond_ports[b]   : the bond's two flat directed-port indices (u*d+p, v*d+q).
    b_x0, b_dx      : unwrapped x endpoint / minimum-image x span (CELL units).
    b_mid           : bond midpoint x, wrapped into [0, box_cells) (CELL units).
    """

    n_nodes: int
    degree: int
    box_cells: float
    port_bond: np.ndarray
    bond_ports: np.ndarray
    b_x0: np.ndarray
    b_dx: np.ndarray
    b_mid: np.ndarray

    @property
    def n_bonds(self) -> int:
        return len(self.b_x0)


def build_bond_table(net: LatticeNet) -> BondTable:
    """Canonical (min,max)-keyed undirected-bond tables from the net's own
    neighbor lists (never a Cartesian distance posit)."""
    N, d = net.n_nodes, net.degree
    a = net.a_cell
    box_cells = net.box / a
    bond_id: dict = {}
    b_x0, b_dx = [], []
    port_bond = np.zeros((N, d), dtype=np.int64)
    bond_ports_list: list[list[int]] = []
    for u in range(N):
        for pp, v in enumerate(net.neighbors[u]):
            key = (min(u, v), max(u, v))
            if key not in bond_id:
                bond_id[key] = len(b_x0)
                u0, u1 = key
                dx = net.pos[u1, 0] - net.pos[u0, 0]
                dx -= net.box * np.round(dx / net.box)  # minimum image
                b_x0.append(net.pos[u0, 0] / a)
                b_dx.append(dx / a)
                bond_ports_list.append([-1, -1])
            bi = bond_id[key]
            port_bond[u, pp] = bi
            # slot 0 = the (min u) endpoint's port, slot 1 = the (max u) endpoint's
            slot = 0 if u == key[0] else 1
            bond_ports_list[bi][slot] = u * d + pp
    b_x0 = np.array(b_x0)
    b_dx = np.array(b_dx)
    bond_ports = np.array(bond_ports_list, dtype=np.int64)
    if np.any(bond_ports < 0):
        raise ValueError("bond table incomplete: some bond saw only one directed port")
    return BondTable(
        n_nodes=N,
        degree=d,
        box_cells=box_cells,
        port_bond=port_bond,
        bond_ports=bond_ports,
        b_x0=b_x0,
        b_dx=b_dx,
        b_mid=np.mod(b_x0 + 0.5 * b_dx, box_cells),
    )


def bond_admittance(A_bond: np.ndarray, *, Y0: float = 1.0, A_cap=None, S_min=None) -> np.ndarray:
    """Per-UNDIRECTED-bond varactor admittance Y_b = Y0/sqrt(S(A_b)).

    Delegates to the canonical imported kernel (vacuum_varactor_scatter.py:125-150,
    S(A) = sqrt(1 - A^2) clipped — crystal_engine.py:191, the A-034 kernel). The
    Class-C driver's exact-unclipped kernel_S (engine_gamma_meanstest.py:177-180)
    is IDENTICAL on the measured grid A in [0, 0.99] (cap at 0.99 and floor at
    S_min = 0.05 are both inactive there); A_cap/S_min pass through for parity
    checks."""
    if A_cap is None and S_min is None:
        return bond_admittance_from_saturation(np.asarray(A_bond, dtype=np.float64), Y0=Y0)
    S = saturation_kernel(np.asarray(A_bond, dtype=np.float64), A_cap=A_cap, S_min=S_min)
    return Y0 / np.sqrt(S)


def scatter_weights(bt: BondTable, Yb: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Per-node scatter weights a_nodes from per-bond admittances.

    Returns (a_nodes, Yp): Yp[u,p] = Y of port (u,p)'s bond (both end-ports share
    the bond's Y — the Class-C convention, engine_gamma_meanstest.py:295-297);
    a_nodes = 2*Yp/sum_ports(Yp), so S_ij = a_j - delta_ij per node (the
    admittance-weighted shunt scatter, vacuum_varactor_scatter.py:156-185)."""
    Yp = np.asarray(Yb, dtype=np.float64)[bt.port_bond]
    a_nodes = 2.0 * Yp / Yp.sum(axis=1, keepdims=True)
    return a_nodes, Yp


# ═════════════════════════════════════════════════════════════════════════════
# 2. TONES + TERMINATIONS (the scaffold)
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class ToneSet:
    """The POSITED tone set: per-step phase advances theta_m (rad/step).

    Harmonic balance posits tones, not tube phases (epic guard 8): a ToneSet is a
    tuple of dimensionless numbers, nothing more. Distinct tones are assumed
    non-degenerate (the DP-1 cross-term cancellation requires theta_m != theta_n)."""

    thetas: tuple

    def __post_init__(self):
        th = tuple(float(t) for t in self.thetas)
        object.__setattr__(self, "thetas", th)
        if len(set(th)) != len(th):
            raise ValueError("degenerate tones: the DP-1 envelope rule needs distinct thetas")

    @property
    def n_tones(self) -> int:
        return len(self.thetas)


@dataclass(frozen=True)
class Termination:
    """Source/absorber termination: a set of INCIDENT slots with imposed phasors.

    ports  : flat directed-port indices (u*degree+p) whose incident wave is imposed.
    paired : for each terminated slot, the flat SRC port whose V_ref would have
             CONNECTed into it (the wave the scaffold absorbs, matched at the
             bond's own Y — the boundary-condition rendering; checkpoint 10).
    drive  : (n_tones, len(ports)) complex imposed incident phasors s_hat
             (zeros = pure absorber)."""

    ports: np.ndarray
    paired: np.ndarray
    drive: np.ndarray

    def __post_init__(self):
        object.__setattr__(self, "ports", np.asarray(self.ports, dtype=np.int64))
        object.__setattr__(self, "paired", np.asarray(self.paired, dtype=np.int64))
        object.__setattr__(self, "drive", np.asarray(self.drive, dtype=np.complex128))
        if self.drive.ndim != 2 or self.drive.shape[1] != len(self.ports):
            raise ValueError("drive must be (n_tones, n_terminated_ports)")
        if len(self.paired) != len(self.ports):
            raise ValueError("paired must match ports")


def crossing_ports(net: LatticeNet, bt: BondTable, plane_cells: float) -> tuple[np.ndarray, np.ndarray]:
    """Flat incident-slot indices for bonds crossing the plane x = plane_cells.

    Returns (fwd, bwd): fwd = incident slots AT the +x-side node (waves traveling
    +x across the plane); bwd = incident slots at the -x-side node (waves
    traveling -x). Mirrors the Class-C driver's _crossing_ports
    (engine_gamma_meanstest.py:245-263) on the engine-native bond table."""
    d = net.degree
    x0, x1 = bt.b_x0, bt.b_x0 + bt.b_dx
    crossing = np.where((x0 - plane_cells) * (x1 - plane_cells) < 0.0)[0]
    fwd, bwd = [], []
    for bi in crossing:
        p_min_flat, p_max_flat = bt.bond_ports[bi]
        # source-side endpoint = smaller unwrapped x
        if x0[bi] < x1[bi]:
            flat_minus, flat_plus = p_min_flat, p_max_flat
        else:
            flat_minus, flat_plus = p_max_flat, p_min_flat
        # incident slot at the +x node is the port facing the -x node = that
        # node's own slot on this bond
        fwd.append(flat_plus)
        bwd.append(flat_minus)
    return np.array(fwd, dtype=np.int64), np.array(bwd, dtype=np.int64)


def make_termination(
    net: LatticeNet,
    bt: BondTable,
    conn: tuple,
    specs: list,
    n_tones: int,
) -> Termination:
    """Assemble a Termination from per-plane specs.

    specs: list of (flat_incident_slots, drive_per_tone) where drive_per_tone is
    (n_tones,) complex applied uniformly over those slots, or an
    (n_tones, n_slots) array. The paired src ports are resolved from the connect
    map (dst -> src)."""
    src_flat, dst_flat = conn
    dst_to_src = {int(dj): int(sj) for sj, dj in zip(src_flat, dst_flat)}
    ports, drives = [], []
    for slots, drive in specs:
        slots = np.asarray(slots, dtype=np.int64)
        drive = np.asarray(drive, dtype=np.complex128)
        if drive.ndim == 1:
            drive = np.repeat(drive[:, None], len(slots), axis=1)
        if drive.shape != (n_tones, len(slots)):
            raise ValueError(f"drive shape {drive.shape} != {(n_tones, len(slots))}")
        ports.append(slots)
        drives.append(drive)
    ports_all = np.concatenate(ports) if ports else np.zeros(0, dtype=np.int64)
    if len(np.unique(ports_all)) != len(ports_all):
        raise ValueError("terminated slots overlap between specs")
    drive_all = (
        np.concatenate(drives, axis=1) if drives else np.zeros((n_tones, 0), dtype=np.complex128)
    )
    paired = np.array([dst_to_src[int(t)] for t in ports_all], dtype=np.int64)
    return Termination(ports=ports_all, paired=paired, drive=drive_all)


# ═════════════════════════════════════════════════════════════════════════════
# 3. THE ONE-STEP OPERATOR IN PHASOR FORM (matrix-free, complex-safe)
# ═════════════════════════════════════════════════════════════════════════════
def apply_M(a_nodes: np.ndarray, conn: tuple, v: np.ndarray) -> np.ndarray:
    """One scatter+connect application M v on (N, degree) complex phasors.

    Identical arithmetic to the certified step (scatter S_ij = a_j - delta_ij,
    then the CONNECT permutation; engine_gamma_meanstest.py:302-308 /
    chiral_lattice.py:294-300), applied to complex phasor arrays."""
    src_flat, dst_flat = conn
    w = (a_nodes * v).sum(axis=1)
    V_ref = w[:, None] - v
    V_new = np.zeros_like(v)
    V_new.flat[dst_flat] = V_ref.flat[src_flat]
    return V_new


def node_voltage(a_nodes: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Common node voltage phasor V_u = sum_j a_j v_j (= 2 sum Y v / sum Y — the
    shunt-junction KCL voltage, vacuum_varactor_scatter.py:162-165)."""
    return (a_nodes * v).sum(axis=1)


# ═════════════════════════════════════════════════════════════════════════════
# 4. PER-TONE LINEAR SOLVE — the algebraic fixed point, with computed receipts
# ═════════════════════════════════════════════════════════════════════════════
@dataclass
class ToneSolution:
    """One tone's phasor solution + its fixed-point receipts (always computed)."""

    theta: float
    v: np.ndarray  # (N, degree) complex
    residual_rel: float  # ||e^{i theta} v - M v||_F(free slots) / ||v||
    converged: bool
    n_matvec: int
    method: str


def _term_mask(ndof: int, term: "Termination | None") -> np.ndarray:
    mask = np.zeros(ndof, dtype=bool)
    if term is not None and len(term.ports):
        mask[term.ports] = True
    return mask


def solve_tone(
    a_nodes: np.ndarray,
    conn: tuple,
    theta: float,
    term: "Termination | None" = None,
    tone_index: int = 0,
    *,
    tol: float = 1e-11,
    maxiter: int = 20000,
    warmstart: int = 0,
    x0: "np.ndarray | None" = None,
) -> ToneSolution:
    """Solve the source-terminated phasor fixed point at one tone.

    Equations: e^{i theta} v_F = (M v)_F on free slots F; v_T = s_hat on
    terminated slots T (imposed incident phasors). Eliminating v_T gives the
    linear system (e^{i theta} I - M_FF) x = M_FT s_hat, solved matrix-free
    (scipy LGMRES; an optional physical-transient warm start iterates
    v <- e^{-i theta}(P_free M v + inject), the damped power iteration whose
    contraction IS the termination's absorption). The residual receipt is
    computed from the operator on the assembled full solution — the solve is
    solver-agnostic evidence-wise: whatever produced v, the receipt is the norm
    of the fixed-point defect."""
    from scipy.sparse.linalg import LinearOperator, lgmres

    N, d = a_nodes.shape
    ndof = N * d
    mask_T = _term_mask(ndof, term)
    mask_F = ~mask_T
    eith = np.exp(1j * float(theta))

    v_s = np.zeros(ndof, dtype=np.complex128)
    if term is not None and len(term.ports):
        v_s[term.ports] = term.drive[tone_index]

    def M_flat(vflat: np.ndarray) -> np.ndarray:
        return apply_M(a_nodes, conn, vflat.reshape(N, d)).ravel()

    b = M_flat(v_s)[mask_F]
    nF = int(mask_F.sum())

    def matvec(x: np.ndarray) -> np.ndarray:
        vx = np.zeros(ndof, dtype=np.complex128)
        vx[mask_F] = x
        return eith * x - M_flat(vx)[mask_F]

    n_mv = [1]  # b cost

    def counted(x):
        n_mv[0] += 1
        return matvec(x)

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

    A = LinearOperator((nF, nF), matvec=counted, dtype=np.complex128)
    x, info = lgmres(A, b, x0=x_init, rtol=tol, atol=0.0, maxiter=maxiter)
    v = _embed(x, v_s, mask_F)

    # fixed-point defect receipt, computed on the assembled solution
    defect = (eith * v - M_flat(v))[mask_F]
    vnorm = float(np.linalg.norm(v))
    residual_rel = float(np.linalg.norm(defect)) / max(vnorm, 1e-300)
    return ToneSolution(
        theta=float(theta),
        v=v.reshape(N, d),
        residual_rel=residual_rel,
        converged=bool(info == 0),
        n_matvec=int(n_mv[0]),
        method="lgmres" + (f"+warmstart{warmstart}" if warmstart else ""),
    )


def _embed(x_free: np.ndarray, v_s: np.ndarray, mask_F: np.ndarray) -> np.ndarray:
    v = v_s.copy()
    v[mask_F] = x_free
    return v


# ═════════════════════════════════════════════════════════════════════════════
# 5. THE S-FIELD: DP-1 ENVELOPE + SELF-CONSISTENT OUTER FIXED POINT
# ═════════════════════════════════════════════════════════════════════════════
def envelope_A_bond(
    bt: BondTable, sols: list, *, v_norm: float = 1.0
) -> np.ndarray:
    """Per-bond DP-1 envelope from the tone phasors (module header, S-FIELD RULE):

        A_b^2 = sum_m (|v_m[fwd_b]|^2 + |v_m[bwd_b]|^2) / (2 v_norm^2).

    |v|^2/2 is the cycle mean of Re[v e^{i theta t}]^2; cross-tone terms
    time-average to zero for distinct tones (ToneSet enforces distinctness), so
    the multi-tone rule is derived, not chosen. v_norm keys the per-sector yield
    (engine-natural 1.0 == V_SNAP for this scalar channel)."""
    acc = np.zeros(bt.n_bonds, dtype=np.float64)
    fwd = bt.bond_ports[:, 0]
    bwd = bt.bond_ports[:, 1]
    for sol in sols:
        vflat = sol.v.ravel()
        acc += (np.abs(vflat[fwd]) ** 2 + np.abs(vflat[bwd]) ** 2) / 2.0
    return np.sqrt(acc) / float(v_norm)


@dataclass
class HBResult:
    """Self-consistent solve result: per-tone solutions + the S-field + receipts."""

    sols: list
    A_bond: np.ndarray
    S_bond: np.ndarray
    converged: bool
    n_outer: int
    history: list  # per-outer-iteration dicts: dA_inf, tone residuals


def solve_self_consistent(
    net: LatticeNet,
    bt: BondTable,
    tones: ToneSet,
    term: "Termination | None",
    *,
    A_init: "np.ndarray | None" = None,
    relax: float = 0.5,
    v_norm: float = 1.0,
    outer_tol: float = 1e-10,
    max_outer: int = 200,
    Y0: float = 1.0,
    solve_kwargs: "dict | None" = None,
) -> HBResult:
    """The outer S-field fixed point (Picard with under-relaxation).

    Unknowns = tone phasors + the S-field (build brief Stage 2). Each outer
    iteration: A -> Y = Y0/sqrt(S(A)) -> per-tone linear phasor KCL solves ->
    DP-1 envelope -> A'. Convergence receipt: ||A' - A||_inf < outer_tol, with
    the per-tone fixed-point residuals carried per iteration. relax=1 is plain
    Picard; smaller values damp envelope feedback near strong saturation."""
    conn = net.connect_index()
    solve_kwargs = dict(solve_kwargs or {})
    A = np.zeros(bt.n_bonds) if A_init is None else np.asarray(A_init, dtype=np.float64).copy()
    history: list = []
    sols: list = []
    converged = False
    n_outer = 0
    for n_outer in range(1, int(max_outer) + 1):
        Yb = bond_admittance(A, Y0=Y0)
        a_nodes, _Yp = scatter_weights(bt, Yb)
        prev = {s.theta: s.v for s in sols}
        sols = [
            solve_tone(
                a_nodes,
                conn,
                th,
                term,
                tone_index=m,
                x0=prev.get(th),
                **solve_kwargs,
            )
            for m, th in enumerate(tones.thetas)
        ]
        A_new = envelope_A_bond(bt, sols, v_norm=v_norm)
        dA = float(np.max(np.abs(A_new - A))) if bt.n_bonds else 0.0
        history.append(
            {
                "dA_inf": dA,
                "residuals": [s.residual_rel for s in sols],
                "A_max": float(A_new.max()) if bt.n_bonds else 0.0,
            }
        )
        A = (1.0 - relax) * A + relax * A_new
        if dA < outer_tol:
            converged = True
            break
    return HBResult(
        sols=sols,
        A_bond=A,
        S_bond=saturation_kernel(A),
        converged=converged,
        n_outer=n_outer,
        history=history,
    )


# ═════════════════════════════════════════════════════════════════════════════
# 6. SOURCE-IDLE MACHINERY — computed observables, caller-supplied thresholds
# ═════════════════════════════════════════════════════════════════════════════
def source_idle_report(
    a_nodes: np.ndarray,
    conn: tuple,
    term: "Termination | None",
    sols: list,
    Yp: np.ndarray,
) -> dict:
    """The scaffold-removability observables at a solution (G1 walk §2 step 4).

    Per tone, all COMPUTED from the solved state (no self-declared fields):
      source_amp    : max |s_hat| over terminated slots (the scaffold's drive);
      exchange_amp  : max |V_ref| arriving AT the scaffold (what it absorbs);
      P_in / P_out  : cycle-mean wave power injected / absorbed by the scaffold,
                      P = sum_T Y_T |.|^2 / 2 in the Y-weighted ledger;
      r_auto        : ||e^{i theta} v - M_full v|| / ||v|| with the FULL
                      (uncut) connect map — the homogeneous/autonomous defect.
                      r_auto ~ 0 means v is a source-free solution of the intact
                      network: the scaffold is removable.
    Idle-ness is adjudicated by the CALLER against declared thresholds
    (idle_verdict); this function only measures."""
    N, d = a_nodes.shape
    per_tone = []
    for m, sol in enumerate(sols):
        v = sol.v
        w = (a_nodes * v).sum(axis=1)
        V_ref = w[:, None] - v
        if term is not None and len(term.ports):
            s_hat = term.drive[m]
            out = V_ref.ravel()[term.paired]
            Y_T = Yp.ravel()[term.ports]
            source_amp = float(np.max(np.abs(s_hat))) if len(s_hat) else 0.0
            exchange_amp = float(np.max(np.abs(out))) if len(out) else 0.0
            P_in = float(np.sum(Y_T * np.abs(s_hat) ** 2) / 2.0)
            P_out = float(np.sum(Y_T * np.abs(out) ** 2) / 2.0)
        else:
            source_amp = exchange_amp = P_in = P_out = 0.0
        Mv = apply_M(a_nodes, conn, v)
        vnorm = float(np.linalg.norm(v))
        r_auto = float(np.linalg.norm(np.exp(1j * sol.theta) * v - Mv)) / max(vnorm, 1e-300)
        per_tone.append(
            {
                "theta": sol.theta,
                "source_amp": source_amp,
                "exchange_amp": exchange_amp,
                "P_in": P_in,
                "P_out": P_out,
                "P_net": P_in - P_out,
                "r_auto": r_auto,
                "v_norm": vnorm,
            }
        )
    return {
        "per_tone": per_tone,
        "max_source_amp": max((t["source_amp"] for t in per_tone), default=0.0),
        "max_exchange_amp": max((t["exchange_amp"] for t in per_tone), default=0.0),
        "max_r_auto": max((t["r_auto"] for t in per_tone), default=0.0),
    }


def idle_verdict(report: dict, *, source_tol: float, exchange_tol: float, r_auto_tol: float) -> dict:
    """Computed idle adjudication against caller-DECLARED thresholds.

    idle <=> the scaffold drives nothing (source_amp <= source_tol), nothing hits
    it (exchange_amp <= exchange_tol), and the solution solves the intact network
    autonomously (r_auto <= r_auto_tol). Thresholds are inputs, never baked-in
    result literals (reconcile-don't-declare)."""
    checks = {
        "source_quiet": report["max_source_amp"] <= source_tol,
        "scaffold_untouched": report["max_exchange_amp"] <= exchange_tol,
        "autonomous_solution": report["max_r_auto"] <= r_auto_tol,
    }
    return {
        **{k: bool(v) for k, v in checks.items()},
        "idle": bool(all(checks.values())),
        "thresholds": {
            "source_tol": source_tol,
            "exchange_tol": exchange_tol,
            "r_auto_tol": r_auto_tol,
        },
    }


# ═════════════════════════════════════════════════════════════════════════════
# 7. WAVE-FIT INSTRUMENTS — k(theta) and Gamma extraction from a solved state
# ═════════════════════════════════════════════════════════════════════════════
def plane_binned_voltage(
    net: LatticeNet, a_nodes: np.ndarray, v: np.ndarray, x_lo_cells: float, x_hi_cells: float
) -> tuple[np.ndarray, np.ndarray]:
    """Node-voltage phasors averaged over thin x-planes in [x_lo, x_hi] (cells).

    Averaging over each distinct x-plane (y, z, and motif) isolates the
    x-directed plane-wave content; returns (x in CARTESIAN length where one bond
    = 1.0, mean V phasor per plane)."""
    xu = net.pos[:, 0] / net.a_cell
    Vn = node_voltage(a_nodes, v)
    m = (xu >= x_lo_cells) & (xu <= x_hi_cells)
    xr = np.round(xu[m], 6)
    xs = np.unique(xr)
    Vb = np.array([Vn[m][xr == x].mean() for x in xs])
    return xs * net.a_cell, Vb


def fit_two_waves(x: np.ndarray, V: np.ndarray, k: float) -> dict:
    """Least-squares fit V(x) ~ a e^{-ikx} + b e^{+ikx} (+x-traveling incident a,
    -x-traveling reflected b, under the V(t)=Re[v e^{+i theta t}] convention).
    Returns a, b and the relative fit residual (computed receipt)."""
    E = np.column_stack([np.exp(-1j * k * x), np.exp(+1j * k * x)])
    coef, *_ = np.linalg.lstsq(E, V, rcond=None)
    resid = float(np.linalg.norm(E @ coef - V)) / max(float(np.linalg.norm(V)), 1e-300)
    return {"a": complex(coef[0]), "b": complex(coef[1]), "k": float(k), "resid_rel": resid}


def fit_k(x: np.ndarray, V: np.ndarray, k_lo: float, k_hi: float) -> dict:
    """Measure k by minimizing the two-wave fit residual over [k_lo, k_hi]
    (bounded scalar minimization; the fit at the optimum is returned whole)."""
    from scipy.optimize import minimize_scalar

    res = minimize_scalar(
        lambda k: fit_two_waves(x, V, k)["resid_rel"],
        bounds=(float(k_lo), float(k_hi)),
        method="bounded",
        options={"xatol": 1e-10},
    )
    return fit_two_waves(x, V, float(res.x))


def gamma_at_plane(fit: dict, x_ref: float) -> complex:
    """Reflection coefficient referenced at plane x_ref (Cartesian):
    Gamma = (b/a) e^{2 i k x_ref}."""
    a, b, k = fit["a"], fit["b"], fit["k"]
    if abs(a) == 0.0:
        raise ValueError("no incident-wave content: |a| = 0")
    return (b / a) * np.exp(2j * k * x_ref)


def interface_two_port(runs: list) -> dict:
    """Multi-load de-embedding of an interface's OWN two-port response.

    THE COORDINATE MAP THIS IMPLEMENTS (phase-space-coordinate-check): the
    Class-C measurement isolated the FRONT-FACE echo by time-windowing; a steady
    state has no time axis, so the isolation is done instead by measuring the
    interface as a linear two-port in the single-Bloch-mode basis and removing
    the scaffold's own load reflections algebraically. Each run r (same
    interface, DIFFERENT absorber/load position) supplies the four wave phasors
    referenced at the interface plane: a (incident, feed side), b (reflected,
    feed side), c (transmitted, far side), d (returning from the load, far
    side). The interface relations

        b = Gamma a + T' d ,     c = T a + Gamma' d

    are solved for (Gamma, T, Gamma', T') by least squares over all runs.
    Gamma is then the interface's own reflection WITH THE FAR SIDE MATCHED
    (d = 0) — exactly the front-face quantity the time-windowed measurement
    reports. With >= 3 loads the system is OVERDETERMINED and the returned
    resid_rel is the computed receipt that the single-mode two-port model
    holds (reconcile-don't-declare: the model's validity is measured, never
    assumed). Bond-matched terminations are imperfect absorbers of the Bloch
    wave (they reflect O(10%)); this de-embedding is what makes that scaffold
    artifact — and the source plane's own re-reflection — drop out of Gamma."""
    if len(runs) < 2:
        raise ValueError("need >= 2 load positions to separate Gamma from the load reflection")
    M = np.array([[r["a"], r["d"]] for r in runs], dtype=np.complex128)
    y_b = np.array([r["b"] for r in runs], dtype=np.complex128)
    y_c = np.array([r["c"] for r in runs], dtype=np.complex128)
    coef_b, *_ = np.linalg.lstsq(M, y_b, rcond=None)
    coef_c, *_ = np.linalg.lstsq(M, y_c, rcond=None)
    r_b = float(np.linalg.norm(M @ coef_b - y_b)) / max(float(np.linalg.norm(y_b)), 1e-300)
    r_c = float(np.linalg.norm(M @ coef_c - y_c)) / max(float(np.linalg.norm(y_c)), 1e-300)
    return {
        "gamma": complex(coef_b[0]),
        "t_reverse": complex(coef_b[1]),
        "t": complex(coef_c[0]),
        "gamma_reverse": complex(coef_c[1]),
        "resid_rel": max(r_b, r_c),
        "n_loads": len(runs),
    }


def signed_gamma(gamma: complex) -> tuple[float, float]:
    """Map a complex interface Gamma to the measurement's signed-real convention
    (engine_gamma_meanstest result §4: Gamma < 0 = polarity-inverted echo).
    Returns (signed value, phase): -|Gamma| if the phase lies in the inverted
    half-plane (Re < 0), else +|Gamma|. The phase is returned so the caller can
    verify the quasi-static limit (phase -> pi or 0) as a computed receipt."""
    ph = float(np.angle(gamma))
    sign = -1.0 if np.cos(ph) < 0.0 else 1.0
    return sign * float(np.abs(gamma)), ph


# ═════════════════════════════════════════════════════════════════════════════
# 8. BLOCH ADJACENCY — the analytic arccos reference, built from the net itself
# ═════════════════════════════════════════════════════════════════════════════
def bloch_adjacency(net: LatticeNet, kvec: np.ndarray) -> np.ndarray:
    """Bloch adjacency A(k)[a,b] = sum_{bonds a->b} e^{i k . delta} over motif
    classes (nodes grouped by fractional position within one cell), with delta
    the minimum-image Cartesian bond vector. Built from the net's OWN neighbor
    lists (never a Cartesian posit). Hermiticity is verified (receipt), not
    assumed. The canonical scalar dispersion is
    omega_n(k) = omega_link * arccos(mu_n(k)/3) with mu_n = eig(A(k))
    (srs-band-structure.md:38-39; srs_band_survey.py is the standing reference
    implementation on the 4-site primitive cell — this one runs on the
    conventional-cell classes of any built net, so bands appear folded)."""
    kvec = np.asarray(kvec, dtype=np.float64)
    frac = np.mod(net.pos / net.a_cell, 1.0)
    keys = np.round(frac, 6)
    uniq, cls = np.unique(keys, axis=0, return_inverse=True)
    nc = len(uniq)
    H = np.zeros((nc, nc), dtype=np.complex128)
    seen = set()
    for u in range(net.n_nodes):
        cu = int(cls[u])
        if cu in seen:
            continue
        seen.add(cu)
        for pp, vnode in enumerate(net.neighbors[u]):
            delta = net.pos[vnode] - net.pos[u]
            delta -= net.box * np.round(delta / net.box)  # minimum image
            H[cu, int(cls[vnode])] += np.exp(1j * float(np.dot(kvec, delta)))
        if len(seen) == nc:
            break
    herm_defect = float(np.max(np.abs(H - H.conj().T)))
    if herm_defect > 1e-9:
        raise ValueError(f"Bloch adjacency not Hermitian (defect {herm_defect:.2e})")
    return H


def bloch_mu(net: LatticeNet, kvec: np.ndarray) -> np.ndarray:
    """Real Bloch-adjacency eigenvalues mu_n(k), ascending."""
    return np.linalg.eigvalsh(bloch_adjacency(net, kvec))


def arccos_theta(mu, z: int = 3) -> np.ndarray:
    """The canonical transmission-line dispersion map theta = arccos(mu/z)
    (rad/step; srs-band-structure.md:38 — NOT the rejected graph-Laplacian
    sqrt(lambda) map, which fails the frozen 1/sqrt(3) velocity gate)."""
    return np.arccos(np.clip(np.asarray(mu, dtype=np.float64) / float(z), -1.0, 1.0))


# ═════════════════════════════════════════════════════════════════════════════
# 9. KNOWN-CASE FIXTURE — the lossless ring (validation gate 3's trivial side)
# ═════════════════════════════════════════════════════════════════════════════
def build_ring_net(N: int) -> LatticeNet:
    """Degree-2 lossless ring: the known driven-vs-autonomous fixture.

    scatter_matrix(2) = [[0,1],[1,0]] is pure pass-through, so a ring mode
    advances one bond per step: theta = k = 2 pi m / N exactly. An initialized
    ring mode is a source-free fixed point of the intact network (r_auto = 0):
    the 'initialized lossless ring trivially [goes source-idle]' side of the
    brief's known pair. Fixture-grade: carrier tag says so."""
    if N < 3:
        raise ValueError("ring needs N >= 3 (distinct neighbors)")
    neighbors = [[(u - 1) % N, (u + 1) % N] for u in range(N)]
    reverse_port = [[1, 0] for _ in range(N)]
    ex = np.array([1.0, 0.0, 0.0])
    bond_unit = [[-ex, ex] for _ in range(N)]
    pos = np.array([[float(u), 0.0, 0.0] for u in range(N)])
    return LatticeNet(
        name=f"ring[{N}]",
        handedness="achiral (cycle)",
        degree=2,
        pos=pos,
        neighbors=neighbors,
        reverse_port=reverse_port,
        bond_unit=bond_unit,
        box=float(N),
        a_cell=1.0,
        interior_mask=np.ones(N, dtype=bool),
        carrier="ring-z2-fixture",  # known-case fixture, NOT a physics carrier
    )


def ring_mode(N: int, m: int) -> tuple[np.ndarray, float]:
    """The exact +x-traveling ring eigenmode: v[u,0] = e^{-i k u}, v[u,1] = 0,
    theta = k = 2 pi m / N (derived in build_ring_net's docstring convention:
    port 0 carries the wave arriving from u-1)."""
    k = 2.0 * np.pi * m / N
    v = np.zeros((N, 2), dtype=np.complex128)
    v[:, 0] = np.exp(-1j * k * np.arange(N))
    return v, float(k)


# --------------------------------------------------------------------------
# R40 batch-2a --- carried stamp on machinery reuse (2026-08-24)
# --------------------------------------------------------------------------
# CLASS: carry-forward citation. This note demotes nothing new, mints nothing,
# and moves no solidity number. It exists because epic guard 6
# (_orchestration/2026-08-24_static-existence-epic.md:145-146) requires the
# R40-B2a stamps on the Class-C machinery to TRAVEL with any reuse: "cite,
# never load-bear silently."
#
# WHAT IS REUSED: this module poses phasor-domain KCL on the same n-port
# amplitude space as the vacuum-varactor scatter (vacuum_varactor_scatter.py,
# whose :72 row --- "the scatter lives in n-PORT amplitude space = the
# (V_inc,V_ref) phasor coordinates" --- is stamped DEMOTED 2026-08-11, R40-B2a:
# NEEDS RE-DERIVATION, family longitudinal-TLM-port, BIAS-DEBT). Under Axiom 5
# clause G the A1/bulk slot is a BOUND RESPONSE (no independent propagating
# branch, no port, zero longitudinal characteristic speed), so the BULK-WAVE
# CARRIER reading of these ports owes re-derivation, with THE BIAS PROPAGATION
# THEOREM standing as Axiom 5's named-open debt (eq_axiom_5.tex clause (c1)).
#
# WHAT THIS MODULE LOAD-BEARS: only the network/scatter ALGEBRA --- ports as
# wave amplitudes of the scalar srs-z3 carrier, the admittance-weighted shunt
# KCL, and the C_eff = C0/S bond-compliance reactance (the surviving object per
# the banked rationale). No bulk-wave-carrier interpretation is asserted
# anywhere in this module; the demoted reading is cited here, not load-borne.
#
# RECORDS: ruling R40; research/drivers/r40_sweep_worklist_verified.json;
# _orchestration/2026-08-12_r40-sweep-batch2a.md.
# --------------------------------------------------------------------------
