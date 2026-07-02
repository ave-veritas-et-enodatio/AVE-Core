"""Cleave-01 registry-pump Chern number — dual-reading (sliding vs locked) driver.

Executes the FROZEN prereg `research/2026-07-02_cleave-registry-pump-chern_prereg.md`
(Grant ruling (b), 2026-07-02): does the Cleave readout boundary loop, swept
adiabatically through the srs chiral ground state, accumulate a nonzero integer
`C.e` of `Link(dOmega, F)` per registry period — and in which substrate reading
(SLIDING/Eulerian vs LOCKED/Lagrangian)?  Whichever setup reproduces the KNOWN OA
anchor (bulk g0 = 2.21589 rad/lattice-z-unit, holonomy +-0.256776 rad) earns the
canon slot — doc-109 adjudicated by the engine, not fiat.

Receipts: `research/2026-07-02_cleave-coupling-derivation_adjudication.md`.
Verdict on paper: UNDECIDABLE-AT-PAPER; sole surviving mechanism class = an
adiabatic Thouless-class registry pump over the 4_1 screw texture.

substrate-native-check walk (Operating Principle 1; done before this code):
  * Dynamics  : adiabatic spectral-flow / Berry-curvature integral over a closed
                (k_z, theta) torus — the substrate-native reading of a Thouless
                charge pump.  NOT Lagrangian minimization / gradient-descent /
                continuum-Helmholtz / energy-basin.
  * Sector    : T2 Cosserat micro-rotation WINDING (charge = Link(dOmega,F) in Z),
                sector-ORTHOGONAL to the A1 dilatation-mass "3".  No A1 cross-wiring.
  * Carrier   : the CHIRAL srs net (I4_1 32; find_screw_operator / srs_motif),
                the free-mode carrier — z=3, do NOT flip to z=4.
  * Coords A46: the Chern number lives on the (k_z, theta) registry-torus PHASE
                space; the OA anchor g0 is a holonomy (rad/z-unit, phase).  Both
                invariants are phase-space quantities — matched coordinates.  The
                real-space bench slope (fC/um) is derived FROM the phase invariant
                x the substrate-native period (a_cell or p), an explicit phase->real
                bridge, NOT a coordinate-mismatched comparison.

FROZEN gates (prereg SS2-SS5):
  GATE-TOY (validate-on-known): a Rice-Mele/Thouless toy pump MUST read C=+-1 (and
    flip sign with pump direction) in the SAME run before any srs verdict counts.
  ANCHOR   : each setup's srs screw-pitch must reproduce g0=2.21589 rad/z-unit to
    0.25% AND flip sign R<->L to earn the canon slot.
  ENANTIOMORPH-ODD: any reported C!=0 MUST flip sign srs-R <-> srs-L; same-sign is
    a RED FLAG -> INCONCLUSIVE.

Outcome bins (frozen, no post-hoc edits): NULL-DERIVED / CANON-CANDIDATE /
BOTH-NONZERO / INCONCLUSIVE.  Expected slope (NOT the bench 414.9): C x {146.7
(full-cell a_cell) | 586.8 (quarter-pitch p)} fC/um.

Driver-honesty (ave-driver-script-honesty): every printed number is computed
in-run; ALL constants imported from ave.core.constants (never hard-coded).

Heavy srs (k_z, theta) eigensolves route to the engine_sim CI lane via the
conftest _ENGINE_SIM_FILES partition (see src/tests/test_cleave_registry_pump_chern.py).
"""

from __future__ import annotations

import numpy as np

from ave.core import chiral_lattice_dynamics as cld
from ave.core.constants import L_NODE, XI_TOPO, e_charge

# ── frozen geometric periods (from canonical constants; prereg SS5) ──────────
A_CELL = 2.0 * np.sqrt(2.0) * L_NODE          # full srs cell period
T_Z = 0.25                                     # 4_1 screw fractional z-translation
P_QUARTER = T_Z * A_CELL                        # quarter screw-pitch period
G0_ANCHOR_RAD_PER_ZUNIT = 2.21589              # OA anchor (chiral-vector-tlm-phase1_result.md:23)
HOLONOMY_ANCHOR_RAD = 0.256776                 # OA loop holonomy (:23)
C_M_TO_FC_PER_UM = 1.0e9                        # C/m -> fC/um  (1e15 fC/C * 1e-6 m/um)


def expected_slopes_fc_per_um() -> dict:
    """The three frozen slope candidates, computed in-run from canonical constants.

    Returns C=1 values; the pumped slope is C x these.  The bench's 414.9 fC/um
    requires a NON-INTEGER C (2*sqrt2 full-cell or 1/sqrt2 quarter-pitch) — it is
    NOT reachable by any integer-C Chern pump (prereg SS5, the pre-frozen G7 FAIL).
    """
    return {
        "bench_e_over_lnode": XI_TOPO * C_M_TO_FC_PER_UM,          # 414.9 (NOT integer-C-reachable)
        "full_cell_e_over_acell": (e_charge / A_CELL) * C_M_TO_FC_PER_UM,   # 146.7  (Angle A)
        "quarter_e_over_p": (e_charge / P_QUARTER) * C_M_TO_FC_PER_UM,      # 586.8  (Angle C)
    }


# ═════════════════════════════════════════════════════════════════════════════
#  GATE-TOY — validate-on-known: Rice-Mele / Thouless charge pump, C = +-1
# ═════════════════════════════════════════════════════════════════════════════
def rice_mele_chern(pump_sign: int = +1, n_k: int = 24, n_phi: int = 24) -> dict:
    """Occupied-band Chern number of a Rice-Mele / Thouless charge pump over its
    (k, phi) torus, by Fukui-Hatsugai plaquette integration.  Known result C=+-1.

    The 2-band Bloch Hamiltonian is H(k, phi) = d.sigma with a pump loop in
    (delta, m) parameter space that encircles the gap-closing point once:
        d_x = t + t' cos k ,  d_y = t' sin k ,  d_z = m(phi)  with
        (t'-t, m) tracing a circle of radius r0 about the origin as phi: 0->2pi.
    Encircling the Dirac point once pumps exactly one charge -> C=+-1 (sign set by
    pump_sign, the traversal direction).  This is the SAME plaquette integrator
    used on the srs torus — the trustworthiness gate.
    """
    ks = np.linspace(0.0, 2.0 * np.pi, n_k, endpoint=False)
    phis = np.linspace(0.0, 2.0 * np.pi, n_phi, endpoint=False)
    t = 1.0
    r0 = 0.8  # < t so the loop encircles the origin (t'-t, m)=(0,0) exactly once

    def occ_eigvec(k: float, phi: float) -> np.ndarray:
        # pump loop in (t'-t, m); t' = t + r0 cos(sign*phi), m = r0 sin(sign*phi)
        tp = t + r0 * np.cos(pump_sign * phi)
        m = r0 * np.sin(pump_sign * phi)
        dx = t + tp * np.cos(k)
        dy = tp * np.sin(k)
        dz = m
        H = np.array([[dz, dx - 1j * dy], [dx + 1j * dy, -dz]], dtype=complex)
        w, v = np.linalg.eigh(H)
        return v[:, 0]  # lower (occupied) band

    return _fukui_hatsugai_chern(occ_eigvec, ks, phis)


def _fukui_hatsugai_chern(occ_eigvec, us, vs) -> dict:
    """Fukui-Hatsugai lattice Chern number for a single occupied band over a
    periodic (u, v) torus.  occ_eigvec(u, v) -> normalized occupied eigenvector.

    Gauge-invariant plaquette field-strength summed over the torus / 2pi.  Returns
    the (near-integer) Chern number, its integer round, and the max plaquette
    imaginary log magnitude (a convergence diagnostic: << pi/2 means the grid
    resolves the curvature).
    """
    nu, nv = len(us), len(vs)
    grid = np.empty((nu, nv), dtype=object)
    for i, u in enumerate(us):
        for j, v in enumerate(vs):
            grid[i, j] = occ_eigvec(u, v)

    def link(a, b):
        z = np.vdot(a, b)
        return z / abs(z) if abs(z) > 1e-14 else 1.0 + 0j

    field = np.zeros((nu, nv))
    for i in range(nu):
        for j in range(nv):
            ip, jp = (i + 1) % nu, (j + 1) % nv
            u1 = link(grid[i, j], grid[ip, j])
            u2 = link(grid[ip, j], grid[ip, jp])
            u3 = link(grid[ip, jp], grid[i, jp])
            u4 = link(grid[i, jp], grid[i, j])
            field[i, j] = np.angle(u1 * u2 * u3 * u4)  # in (-pi, pi]
    chern = float(np.sum(field) / (2.0 * np.pi))
    return {
        "chern": chern,
        "chern_int": int(np.round(chern)),
        "max_plaquette": float(np.max(np.abs(field))),
        "n_grid": (nu, nv),
    }
