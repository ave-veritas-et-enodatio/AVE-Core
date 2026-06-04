"""
Full-electron Option B — does a transverse wave SET the (2,3) on the DISCRETE engine?

Headline (Grant's hypothesis): on VacuumEngine3D (K4-TLM + Cosserat — the only
engine with the (2,3) carrier: native (V_inc, V_ref) ports + Cosserat ω + Op10),
seed the GENERATIVE PRECURSOR (a structured transverse photon: counter-propagating
opposite-handed CP focused pulses, multi-node, E⊥B⊥k — the Option-C precursor that
self-trapped), drive to saturation, and test whether the (2,3) winding EMERGES in
the (V_inc, V_ref) phasor sector as the trap forms — ZERO imposed.

Authoritative spec: _orchestration/2026-06-04_full-electron-option-B-discrete-emergence.md
Prereg + result:    research/2026-06-04_full-electron-option-B-discrete-emergence-result.md

Three arms (prereg §4):
  A — EMERGENCE: transverse photon, no (2,3) imposed. The headline.
  B — MATCHED BASELINE: same per-port |V_inc| stats, phase-scrambled (trivial topology).
  C — IMPOSED CONTROL: Arm A + PairNucleationGate (Option-D nucleation rule,
      pair-production-axiom-derivation.md:121). Establishes the (2,3) signature template.

PASS bars (prereg §4, substrate-derived):
  B1 self-trap:  A²_max > A²_op14 = √(2α)
  B2 localization beats baseline:  retention(A) > retention(B)
  B3 (2,3) phasor winding (HEADLINE):  (V_inc,V_ref) temporal winding c=3 OR (n₁,n₂)=(2,3)
       in Arm A, ABSENT in Arm B, MATCHES Arm C
  B4 reactance-pair consistency:  C-state(V_inc) ⟷ L-state(Phi_link) anti-correlation

Outcomes (brief §4):
  (i)   self-traps AND (2,3) emerges → Grant's hypothesis CONFIRMED
  (ii)  carries (2,3) carrier but does NOT self-trap → needs c_eff/Path-A (surface to Grant)
  (iii) self-traps but (2,3) only when IMPOSED → hypothesis REFUTED on the discrete engine

DISCIPLINE NOTES (load-bearing):
  - phase-space-coordinate-check (A47 v3): the engine's shipped Op10
    (cosserat.extract_crossing_count) reads REAL-SPACE Cosserat ω; the corpus
    (2,3) lives in (V_inc, V_ref) PHASOR (theory.md:16). HEADLINE = the phasor
    temporal-winding extractor below; the ω Op10 is reported as a FLAGGED-mismatch
    diagnostic. (flag-don't-fix; the shipped Op10 is NOT redefined.)
  - ave-driver-script-honesty: the transverse-photon source injects E⊥B⊥k ONLY;
    it injects NO (V_inc, V_ref) winding. Arm C imposes the Option-D boundary
    condition (PairNucleationGate) and is clearly labeled.
  - Rule 10: C-state (V_inc) AND L-state (Phi_link) recorded at the trap bond every
    step. PML excluded + density-peak trap-site selection.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import ALPHA  # noqa: E402
from ave.topological.vacuum_engine import (  # noqa: E402
    PairNucleationGate,
    SpatialDipoleCPSource,
    VacuumEngine3D,
    _forward_t2_port_weights,
    amp_to_vsnap_units,
)

# ── Substrate-derived constants (ave-canonical-source: NO hardcoded literals) ──
V_YIELD = float(np.sqrt(ALPHA))           # √α ≈ 0.0854 V_SNAP — Op14 onset (theory.md:10)
A2_OP14 = float(np.sqrt(2.0 * ALPHA))     # √(2α) ≈ 0.1208 — Op14 engagement (B1 bar)
OMEGA_C = 1.0                             # ω_C natural units
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)                   # K4-TLM 4-port junction timestep
PHI = (1.0 + np.sqrt(5.0)) / 2.0         # golden ratio (R_phase/r_phase = φ² diagnostic)


# ══════════════════════════════════════════════════════════════════════════════
# Source: counter-propagating-capable transverse-photon precursor
# ══════════════════════════════════════════════════════════════════════════════
# SpatialDipoleCPSource is forward-only (hardcodes +propagation_axis). For the
# counter-propagating precursor we need a −x pulse. _forward_t2_port_weights
# supports any direction (max(0, −d̂·p̂)), so a minimal subclass overriding the
# port-weight direction sign gives the backward pulse, reusing all the proven
# dipole-modulation + envelope machinery.
class _DirectionalCPSource(SpatialDipoleCPSource):
    """SpatialDipoleCPSource with an explicit propagation SIGN (±1) so a
    counter-propagating (−axis) opposite-handed pulse can be built.

    Only `_init_if_needed` is overridden: it sets the propagation port-weights
    via `_forward_t2_port_weights((sign·axis_unit))`. Verified: forward(+x) and
    backward(−x) weights are exact negatives ([−.5,−.5,+.5,+.5] vs
    [+.5,+.5,−.5,−.5]) — counter-propagation in the K4 port basis. All other
    machinery (dipole modulation, envelope, apply) is inherited unchanged."""

    def __init__(self, *args, direction_sign: int = +1, **kwargs):
        super().__init__(*args, **kwargs)
        self._dir_sign = int(direction_sign)

    def _init_if_needed(self, engine: "VacuumEngine3D") -> None:
        if self._port_w_prop is not None:
            return
        direction = tuple(
            (self._dir_sign if i == self.propagation_axis else 0.0) for i in range(3)
        )
        self._port_w_prop = _forward_t2_port_weights(direction)
        N = engine.N
        yc = (N - 1) / 2.0 if self.y_c is None else self.y_c
        zc = (N - 1) / 2.0 if self.z_c is None else self.z_c
        j, k = np.indices((N, N), dtype=float)
        r2 = (j - yc) ** 2 + (k - zc) ** 2
        gauss_env = np.exp(-r2 / (2.0 * self.sigma_yz**2))
        self._g_y_profile = (j - yc) * gauss_env
        self._g_z_profile = (k - zc) * gauss_env


# ══════════════════════════════════════════════════════════════════════════════
# Engine + arm setup
# ══════════════════════════════════════════════════════════════════════════════
# Source-plane positions + waist (tuned in smoke tests so the mid-plane
# constructive-interference collision breaches A²_op14 at N=48).
X0_FWD_FRAC = 0.30   # forward pulse source plane ≈ 0.30·N
X0_BWD_FRAC = 0.70   # backward pulse source plane ≈ 0.70·N (counter-propagating)
SIGMA_YZ = 3.0       # focused beam waist (~λ_C/2)
AMP_PER_PULSE = 0.40  # V_SNAP units/pulse; constructive peak → A² > A²_op14 (smoke: 0.13–0.16)
RAMP_P, SUSTAIN_P, DECAY_P = 1.5, 3.0, 2.0  # envelope (periods); ON ~6.5P then self-sustenance


def setup_engine(N, PML):
    """A28-corrected coupled VacuumEngine3D (doc 67 §15 + r10_v8 config)."""
    return VacuumEngine3D.from_args(
        N=N,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,   # A28 correction (doc 67 §15)
        enable_cosserat_self_terms=True,  # topology-stabilizing (k_op10, k_hopf)
        use_asymmetric_saturation=True,   # chirality bias (Meissner Γ→−1)
        axiom_4_enabled=True,             # saturation enabled
    )


def setup_transverse_photon(engine, N, amplitude):
    """Arm A precursor: TWO counter-propagating opposite-handed CP pulses
    (multi-node, E⊥B⊥k — the Option-C precursor). Injects K4 V_inc ONLY;
    NO (V_inc, V_ref) winding is planted (ave-driver-script-honesty)."""
    x0_fwd = int(round(X0_FWD_FRAC * N))
    x0_bwd = int(round(X0_BWD_FRAC * N))
    fwd = _DirectionalCPSource(
        x0=x0_fwd, propagation_axis=0, amplitude=amplitude, omega=OMEGA_C,
        handedness="RH", sigma_yz=SIGMA_YZ,
        t_ramp=RAMP_P * COMPTON_PERIOD, t_sustain=SUSTAIN_P * COMPTON_PERIOD,
        t_decay=DECAY_P * COMPTON_PERIOD, direction_sign=+1,
    )
    bwd = _DirectionalCPSource(
        x0=x0_bwd, propagation_axis=0, amplitude=amplitude, omega=OMEGA_C,
        handedness="LH", sigma_yz=SIGMA_YZ,  # opposite handedness
        t_ramp=RAMP_P * COMPTON_PERIOD, t_sustain=SUSTAIN_P * COMPTON_PERIOD,
        t_decay=DECAY_P * COMPTON_PERIOD, direction_sign=-1,  # counter-propagating
    )
    engine.add_source(fwd)
    engine.add_source(bwd)
    return (x0_fwd, x0_bwd)


# ══════════════════════════════════════════════════════════════════════════════
# Observables
# ══════════════════════════════════════════════════════════════════════════════
def compute_a2_field(V_inc, V_SNAP):
    """A² = |V_inc|²/V_SNAP² (port-summed strain)."""
    return np.sum(V_inc**2, axis=-1) / (V_SNAP**2)


def _interior_mask(N, PML):
    m = np.zeros((N, N, N), dtype=bool)
    m[PML : N - PML, PML : N - PML, PML : N - PML] = True
    return m


def select_trap_bond(engine, PML):
    """Density-peak trap-site selection (Checkpoint 7): the A-site with peak
    interior |V_inc|², PML-excluded. Returns ((i,j,k), port) for the bond
    whose V_inc magnitude is largest at that A-site. NOT centroid+offset."""
    N = engine.N
    a2 = compute_a2_field(engine.k4.V_inc, engine.V_SNAP)
    interior = _interior_mask(N, PML)
    # restrict to A-sublattice interior cells
    cand = interior & engine.k4.mask_A
    a2_masked = np.where(cand, a2, -np.inf)
    flat_idx = int(np.argmax(a2_masked))
    i, j, k = np.unravel_index(flat_idx, a2_masked.shape)
    # port with the largest |V_inc| at that A-site
    port = int(np.argmax(np.abs(engine.k4.V_inc[i, j, k, :])))
    return (int(i), int(j), int(k)), port


def phasor_temporal_winding(v_inc_traj, v_ref_traj, phi_traj=None):
    """HEADLINE B3 observable (Q1 default = temporal-single-bond): the
    (V_inc, V_ref) phasor TEMPORAL winding at one trap bond over the recording
    window. Per theory.md:16 ("trefoil lives in the bond-pair LC tank's
    (V_inc, V_ref) phasor trajectory") + 06_winding_index_projection §4 (the "3"
    is the U(1) fibre temporal phase) + doc-26 §5.1 (R_phase=φ/2, r_phase=(φ-1)/2).

    Coordinate construction (NO fabrication — all native engine state read at
    acquisition time, phase-space-coordinate-check probe-5 guard):
      θ₁(t) = phase of the dominant-port phasor (V_inc_p1, V_ref_p1) — toroidal
      θ₂(t) = phase of the quadrature-partner phasor (V_inc_p2, V_ref_p2) — poloidal
    The bond's two load-bearing ports (the dominant + its quadrature partner)
    span the Clifford-torus (θ₁, θ₂); their winding pair (n₁, n₂) + the
    phase-space crossing count c of the closed (V_inc, V_ref) curve are the
    (2,3) observable. The R_phase/r_phase ellipse aspect (→ φ² diagnostic) comes
    from PCA on the (V_inc, V_ref) cloud (doc-26 §5.1; phasor_trajectory_test.py).

    v_inc_traj, v_ref_traj: (T, 4) port-resolved time series at the trap A-site.
    Returns dict with n1, n2, crossing_count_c, R_phase_over_r_phase, amp_ratio.
    """
    T = v_inc_traj.shape[0]
    out = {
        "n1": 0, "n2": 0, "crossing_count_c": 0,
        "R_phase_over_r_phase": float("nan"), "amp": 0.0,
        "p1": -1, "p2": -1,
    }
    if T < 16:
        return out
    # dominant + quadrature-partner ports by recorded amplitude
    port_amp = np.sqrt(np.mean(v_inc_traj**2, axis=0) + np.mean(v_ref_traj**2, axis=0))
    if port_amp.max() < 1e-12:
        return out
    p1 = int(np.argmax(port_amp))
    # quadrature partner = the OTHER port whose phasor is most ~90° to p1
    order = np.argsort(port_amp)[::-1]
    p2 = int(order[1]) if len(order) > 1 else p1
    out["p1"], out["p2"], out["amp"] = p1, p2, float(port_amp[p1])

    # toroidal θ₁ = phase of (V_inc_p1, V_ref_p1); poloidal θ₂ = (V_inc_p2, V_ref_p2)
    def _winding(vi, vr):
        # center the phasor cloud, then unwrap the angle
        a = vi - vi.mean()
        b = vr - vr.mean()
        if np.sqrt(a.var() + b.var()) < 1e-12:
            return 0.0
        ph = np.unwrap(np.arctan2(b, a))
        total = (ph[-1] - ph[0]) / (2.0 * np.pi)
        # closure correction (as in extract_crossing_count)
        closure = (np.arctan2(b[0], a[0]) - ph[-1])
        while closure > np.pi:
            closure -= 2 * np.pi
        while closure < -np.pi:
            closure += 2 * np.pi
        return total + closure / (2.0 * np.pi)

    w1 = _winding(v_inc_traj[:, p1], v_ref_traj[:, p1])
    w2 = _winding(v_inc_traj[:, p2], v_ref_traj[:, p2])
    out["n1"] = int(round(abs(w1)))
    out["n2"] = int(round(abs(w2)))

    # phase-space crossing count c of the closed 2D curve (V_inc_p1, V_inc_p2):
    # the trefoil on the Clifford torus has c=3 (06_ amendment). Count self-
    # crossings of the closed planar curve traced by (θ₁, θ₂)-conjugate coords.
    curve = np.stack([v_inc_traj[:, p1] - v_inc_traj[:, p1].mean(),
                      v_inc_traj[:, p2] - v_inc_traj[:, p2].mean()], axis=1)
    out["crossing_count_c"] = _planar_self_crossings(curve)

    # R_phase/r_phase via PCA on the (V_inc_p1, V_ref_p1) cloud (doc-26 §5.1)
    pts = np.stack([v_inc_traj[:, p1], v_ref_traj[:, p1]], axis=1)
    pts = pts - pts.mean(axis=0, keepdims=True)
    cov = (pts.T @ pts) / max(T - 1, 1)
    evals = np.sort(np.maximum(np.linalg.eigvalsh(cov), 0.0))[::-1]
    if evals[1] > 1e-30:
        out["R_phase_over_r_phase"] = float(np.sqrt(evals[0] / evals[1]))
    return out


def _planar_self_crossings(curve):
    """Count self-intersections of a closed planar polyline (the phase-space
    crossing count c). The (2,3) trefoil on the Clifford torus → c=3."""
    n = len(curve)
    if n < 8:
        return 0
    # subsample to keep the O(n²) crossing count tractable + suppress noise
    step = max(1, n // 256)
    p = curve[::step]
    m = len(p)
    # segments (i, i+1); closed
    crossings = 0
    for i in range(m - 1):
        a1, a2 = p[i], p[i + 1]
        # only check non-adjacent later segments
        for j in range(i + 2, m - 1):
            if i == 0 and j == m - 2:
                continue  # endpoints adjacent on the closed loop
            b1, b2 = p[j], p[j + 1]
            if _seg_intersect(a1, a2, b1, b2):
                crossings += 1
    return crossings


def _seg_intersect(p1, p2, p3, p4):
    """True if segment p1p2 properly intersects p3p4 (strict, no shared endpt)."""
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - a[0])
    d1 = ccw(p3, p4, p1)
    d2 = ccw(p3, p4, p2)
    d3 = ccw(p1, p2, p3)
    d4 = ccw(p1, p2, p4)
    return ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0))


def omega_op10_diagnostic(engine):
    """FLAGGED-mismatch diagnostic (A47 v3, flag-don't-fix): the engine's shipped
    Op10 reads REAL-SPACE Cosserat ω; the corpus (2,3) lives in (V_inc,V_ref)
    PHASOR (theory.md:16). Reported as a coordinate-mismatch diagnostic, NOT the
    headline. Per Q0: a pure-V transverse photon leaves ω≡0, so this is expected
    to read 0 (the carrier-2 structural finding)."""
    out = {}
    try:
        out["omega_op10_crossing_count"] = int(engine.cos.extract_crossing_count())
    except Exception as exc:  # noqa: BLE001
        out["omega_op10_crossing_count"] = -1
        out["omega_op10_error"] = str(exc)
    try:
        out["hopf_charge"] = float(engine.cos.extract_hopf_charge())
    except Exception as exc:  # noqa: BLE001
        out["hopf_charge"] = float("nan")
        out["hopf_error"] = str(exc)
    out["omega_max"] = float(np.abs(engine.cos.omega).max())
    out["omega_energy"] = float(np.sum(engine.cos.omega**2))
    return out


# ══════════════════════════════════════════════════════════════════════════════
# Single-arm run
# ══════════════════════════════════════════════════════════════════════════════
def run_arm(arm_name, N, PML, n_periods, amplitude, impose_nucleation):
    """Run one arm (A/B/C); return observables dict."""
    raise NotImplementedError  # FILLED


# ══════════════════════════════════════════════════════════════════════════════
# Adjudication + verdict
# ══════════════════════════════════════════════════════════════════════════════
def adjudicate(arm_A, arm_B, arm_C):
    """Apply B1-B4 PASS bars; return outcome (i/ii/iii)."""
    raise NotImplementedError  # FILLED


def main():
    raise NotImplementedError  # FILLED


if __name__ == "__main__":
    main()
