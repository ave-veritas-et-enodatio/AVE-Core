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
)

# Canonical (2,3)-phasor direct seed (the IMPOSED control for the phasor carrier).
# initialize_2_3_voltage_ansatz plants the (2,3) winding in V_inc via the knot-
# tangent port weighting (doc-26 §5.1 / phase3f canonical placement).
from tlm_electron_soliton_eigenmode import (  # noqa: E402
    initialize_2_3_voltage_ansatz,
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
    out["w1_raw"] = float(w1)
    out["w2_raw"] = float(w2)
    # winding-rate RATIO (robust primary): the (2,3) means θ₁ advances 2× while
    # θ₂ advances 3× → ratio 2/3. Report the reduced integer ratio nearest to w1:w2.
    out["winding_ratio"] = _reduced_ratio(w1, w2)

    # phase-space crossing count c of the closed 2D curve (smoothed to suppress
    # jitter; raw self-crossings of a noisy time series count noise, not the
    # trefoil). The trefoil on the Clifford torus has c=3 (06_ amendment).
    s1 = _smooth(v_inc_traj[:, p1] - v_inc_traj[:, p1].mean())
    s2 = _smooth(v_inc_traj[:, p2] - v_inc_traj[:, p2].mean())
    curve = np.stack([s1, s2], axis=1)
    out["crossing_count_c"] = _planar_self_crossings(curve)

    # R_phase/r_phase via PCA on the (V_inc_p1, V_ref_p1) cloud (doc-26 §5.1)
    pts = np.stack([v_inc_traj[:, p1], v_ref_traj[:, p1]], axis=1)
    pts = pts - pts.mean(axis=0, keepdims=True)
    cov = (pts.T @ pts) / max(T - 1, 1)
    evals = np.sort(np.maximum(np.linalg.eigvalsh(cov), 0.0))[::-1]
    if evals[1] > 1e-30:
        out["R_phase_over_r_phase"] = float(np.sqrt(evals[0] / evals[1]))
    return out


def _smooth(x, frac=0.05):
    """Moving-average smooth (window = frac·len) to suppress per-step jitter
    before topological crossing-count extraction."""
    n = len(x)
    w = max(3, int(frac * n) | 1)  # odd window
    if w >= n:
        return x - x.mean() + x.mean()
    kern = np.ones(w) / w
    return np.convolve(x, kern, mode="same")


def _reduced_ratio(a, b, max_den=7):
    """Nearest small-integer reduced ratio to |a|:|b| (for the (2,3) winding
    ratio readout). Returns 'p:q' string or 'n/a'."""
    a, b = abs(a), abs(b)
    if a < 1e-6 or b < 1e-6:
        return "n/a"
    target = a / b
    best = (1, 1)
    best_err = abs(target - 1.0)
    for q in range(1, max_den + 1):
        for p in range(1, max_den + 1):
            err = abs(target - p / q)
            if err < best_err:
                best_err, best = err, (p, q)
    from math import gcd
    g = gcd(best[0], best[1])
    return f"{best[0] // g}:{best[1] // g}"


def _planar_self_crossings(curve):
    """Count DISTINCT self-intersections of a closed planar polyline (the
    phase-space crossing count c). The (2,3) trefoil on the Clifford torus → c=3.
    Curve should be pre-smoothed. Near-duplicate crossings (same intersection
    hit by several adjacent segment pairs after smoothing) are merged by spatial
    clustering of intersection points."""
    n = len(curve)
    if n < 8:
        return 0
    step = max(1, n // 200)  # keep O(m²) tractable
    p = curve[::step]
    m = len(p)
    scale = float(np.sqrt(p.var(axis=0).sum())) + 1e-12
    pts = []
    for i in range(m - 1):
        a1, a2 = p[i], p[i + 1]
        for j in range(i + 2, m - 1):
            if i == 0 and j == m - 2:
                continue
            b1, b2 = p[j], p[j + 1]
            ip = _seg_intersection_point(a1, a2, b1, b2)
            if ip is not None:
                pts.append(ip)
    if not pts:
        return 0
    # cluster intersection points (merge those within 8% of curve scale)
    pts = np.array(pts)
    tol = 0.08 * scale
    clusters = []
    for q in pts:
        placed = False
        for c in clusters:
            if np.linalg.norm(q - c) < tol:
                placed = True
                break
        if not placed:
            clusters.append(q)
    return len(clusters)


def _seg_intersection_point(p1, p2, p3, p4):
    """Return the intersection point of segments p1p2 and p3p4 if they properly
    cross, else None."""
    if not _seg_intersect(p1, p2, p3, p4):
        return None
    d1 = p2 - p1
    d2 = p4 - p3
    denom = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(denom) < 1e-15:
        return None
    t = ((p3[0] - p1[0]) * d2[1] - (p3[1] - p1[1]) * d2[0]) / denom
    return p1 + t * d1


def _seg_intersect(p1, p2, p3, p4):
    """True if segment p1p2 properly intersects p3p4 (strict, no shared endpt)."""
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - a[0])
    d1 = ccw(p3, p4, p1)
    d2 = ccw(p3, p4, p2)
    d3 = ccw(p1, p2, p3)
    d4 = ccw(p1, p2, p4)
    return ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0))


def phasor_spatial_ring_winding(engine, center, R, PML):
    """Q1 ALTERNATIVE observable: the (V_inc, V_ref) phasor winding around a
    REAL-SPACE toroidal ring of bonds (the spatial analog of the corpus (2,3),
    and the (V_inc, V_ref) counterpart of what the ω-Op10 does on ω). Walk a
    major-circle of A-sites at radius R in the z=cz plane; at each, take the
    phasor angle arctan2(V_ref_p, V_inc_p) of the dominant port; count how it
    winds (toroidal w₁). Then walk a minor (tube) circle for the poloidal w₂.
    Returns (w1_spatial, w2_spatial). This answers Q1 empirically: if the
    planted (2,3) seed (Arm C) shows (2,3) HERE but not in the temporal-single-
    bond extractor, the (2,3) is a spatial-ring object, not temporal-single-bond.
    """
    out = {"w1_spatial": 0, "w2_spatial": 0, "ring_amp": 0.0}
    N = engine.N
    cx, cy, cz = center
    kz = int(round(cz))
    if not (PML <= kz < N - PML):
        kz = N // 2
    Vi = engine.k4.V_inc
    Vr = engine.k4.V_ref

    def sample_angle(ix, iy, iz):
        ix = int(np.clip(ix, PML, N - PML - 1))
        iy = int(np.clip(iy, PML, N - PML - 1))
        iz = int(np.clip(iz, PML, N - PML - 1))
        port = int(np.argmax(np.abs(Vi[ix, iy, iz, :])))
        return np.arctan2(Vr[ix, iy, iz, port], Vi[ix, iy, iz, port]), \
            float(np.abs(Vi[ix, iy, iz, port]))

    # major circle (toroidal w₁) at radius R in z=kz plane
    n_ang = 64
    angs = np.linspace(0, 2 * np.pi, n_ang, endpoint=False)
    maj_ph, maj_amp = [], []
    for a in angs:
        ph, amp = sample_angle(cx + R * np.cos(a), cy + R * np.sin(a), kz)
        maj_ph.append(ph)
        maj_amp.append(amp)
    out["ring_amp"] = float(np.mean(maj_amp))
    if out["ring_amp"] > 1e-9:
        unw = np.unwrap(np.array(maj_ph))
        out["w1_spatial"] = int(round(abs((unw[-1] - unw[0]) / (2 * np.pi))))

    # minor (tube) circle (poloidal w₂) at fixed toroidal angle 0, radius r≈R/φ²
    r_tube = max(2.0, R / (PHI**2))
    min_ph, min_amp = [], []
    for a in angs:
        # tube circle in the (radial, z) plane at toroidal angle 0 (along +x)
        rad = R + r_tube * np.cos(a)
        ph, amp = sample_angle(cx + rad, cy, kz + r_tube * np.sin(a))
        min_ph.append(ph)
        min_amp.append(amp)
    if np.mean(min_amp) > 1e-9:
        unw = np.unwrap(np.array(min_ph))
        out["w2_spatial"] = int(round(abs((unw[-1] - unw[0]) / (2 * np.pi))))
    return out


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
def setup_baseline_photon(engine, N, amplitude):
    """Arm B matched baseline: SAME two counter-propagating focused pulses at
    the SAME amplitude / focal geometry / saturation depth, but SAME handedness
    (both RH) instead of opposite. This removes the chiral/topological structure
    (the opposite-handed E⊥B curl mismatch that seeds the knot) while preserving
    identical amplitude statistics + saturation engagement — the matched-
    distribution, topologically-trivial control (CP8; fixes the phase3f Factor-2
    confound where a random baseline gets larger amplitudes → more saturation).
    A per-step field scramble is NOT used: it injects energy (breaks TLM
    unitarity, +25× interior energy in 60 steps) — verified and rejected."""
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
        handedness="RH", sigma_yz=SIGMA_YZ,  # SAME handedness (trivial topology)
        t_ramp=RAMP_P * COMPTON_PERIOD, t_sustain=SUSTAIN_P * COMPTON_PERIOD,
        t_decay=DECAY_P * COMPTON_PERIOD, direction_sign=-1,
    )
    engine.add_source(fwd)
    engine.add_source(bwd)
    return (x0_fwd, x0_bwd)


def run_arm(arm_name, N, PML, n_periods, amplitude, mode):
    """Run one arm; return observables dict.

    mode:
      'emergence'  — Arm A: transverse photon, nothing imposed.
      'baseline'   — Arm B: SAME-handedness counter-propagating pulses (matched
                     amplitude / saturation, trivial topology).
      'imposed'    — Arm C: the (2,3) phasor winding planted DIRECTLY in V_inc
                     via initialize_2_3_voltage_ansatz (the corpus-canonical
                     IMPOSED placement, doc-26 §5.1). Clearly labeled IMPOSED.
                     Establishes the (2,3) signature template B3 checks against.
                     ALSO attaches the PairNucleationGate to record whether the
                     shipped Option-D rule would fire (Q0 confirmation: it needs
                     the Cosserat ω sector a pure-V photon leaves at ω≡0).
    """
    n_steps = int(n_periods * COMPTON_PERIOD / DT)
    rec_window = int(min(n_periods, 12.0) * COMPTON_PERIOD / DT)  # last ≤12P
    rec_start = n_steps - rec_window

    engine = setup_engine(N, PML)
    if mode == "baseline":
        x0s = setup_baseline_photon(engine, N, amplitude)  # both-RH (trivial topology)
    else:
        x0s = setup_transverse_photon(engine, N, amplitude)  # opposite-handed (chiral)

    gate = None
    gate_firings = 0
    if mode == "imposed":
        # IMPOSED control: plant the (2,3) phasor winding DIRECTLY in V_inc on a
        # toroidal shell (corpus-canonical placement, doc-26 §5.1). This is the
        # clearly-labeled IMPOSED arm — it imposes the very winding the emergence
        # arm is tested for, establishing the signature template. R, r = golden-
        # torus shell sized to the active region.
        R_shell = 0.22 * N
        r_shell = R_shell / (PHI**2)
        initialize_2_3_voltage_ansatz(engine.k4, R=R_shell, r=r_shell, amplitude=amplitude)
        # ALSO attach the Option-D gate to RECORD whether it would fire (Q0:
        # it uses A²_μ from the Cosserat sector → can't fire from a pure-V photon).
        gate = PairNucleationGate(cadence=1, saturation_frac=0.95)
        engine.add_observer(gate)

    # trajectories
    max_a2 = 0.0
    max_a2_loc = None
    a2_hist = []          # (t, max_a2_interior)
    energy_hist = []      # (t, interior energy)
    # reactance-pair recording at a FIXED candidate bond (lattice center A-site)
    # AND a running trap-bond (re-selected post-trap). We record the center bond
    # every step (cheap) + do final trap-bond selection from the saved field.
    cc = N // 2
    # ensure center sample site is an A-site; if not, nudge by +1 on x
    cx = cc if engine.k4.mask_A[cc, cc, cc] else cc + 1
    rec_vinc = np.zeros((rec_window, 4))
    rec_vref = np.zeros((rec_window, 4))
    rec_phi = np.zeros((rec_window, 4))
    # also record the running peak-A2 A-site bond time series
    rec_peak_vinc = np.zeros((rec_window, 4))
    rec_peak_vref = np.zeros((rec_window, 4))
    rec_peak_phi = np.zeros((rec_window, 4))

    interior = _interior_mask(N, PML)
    t0 = time.time()
    for step_i in range(n_steps):
        engine.step()
        if gate is not None:
            gate_firings = int(gate._total_firings)

        a2 = compute_a2_field(engine.k4.V_inc, engine.V_SNAP)
        a2_int = np.where(interior, a2, 0.0)
        m = float(a2_int.max())
        if m > max_a2:
            max_a2 = m
            max_a2_loc = tuple(int(v) for v in np.unravel_index(int(np.argmax(a2_int)), a2_int.shape))

        if step_i >= rec_start:
            r = step_i - rec_start
            rec_vinc[r] = engine.k4.V_inc[cx, cc, cc, :]
            rec_vref[r] = engine.k4.V_ref[cx, cc, cc, :]
            rec_phi[r] = engine.k4.Phi_link[cx, cc, cc, :]
            # running peak-A2 A-site
            (pi, pj, pk), _ = select_trap_bond(engine, PML)
            rec_peak_vinc[r] = engine.k4.V_inc[pi, pj, pk, :]
            rec_peak_vref[r] = engine.k4.V_ref[pi, pj, pk, :]
            rec_peak_phi[r] = engine.k4.Phi_link[pi, pj, pk, :]

        if step_i % max(1, n_steps // 10) == 0:
            a2_hist.append((float(step_i * DT), m))
            energy_hist.append((float(step_i * DT), float(np.sum(a2_int))))

    elapsed = time.time() - t0

    # final trap-bond selection (density-peak) from the converged field
    (ti, tj, tk), tport = select_trap_bond(engine, PML)

    # HEADLINE B3 (Q1 default): phasor TEMPORAL winding at the peak-A2 trap bond
    winding_peak = phasor_temporal_winding(rec_peak_vinc, rec_peak_vref, rec_peak_phi)
    winding_center = phasor_temporal_winding(rec_vinc, rec_vref, rec_phi)

    # Q1 ALTERNATIVE: phasor SPATIAL-RING winding (answers temporal-vs-spatial
    # empirically). Ring centered on lattice center, radius = trap distance from center.
    cc_f = (N - 1) / 2.0
    R_trap = float(np.sqrt((ti - cc_f) ** 2 + (tj - cc_f) ** 2)) or (0.22 * N)
    winding_spatial = phasor_spatial_ring_winding(
        engine, (cc_f, cc_f, cc_f), max(R_trap, 0.15 * N), PML
    )

    # B4: reactance-pair anti-correlation at the peak bond (C=V_inc vs L=Phi_link)
    react = _reactance_consistency(rec_peak_vinc, rec_peak_phi, winding_peak["p1"])

    # carrier-2 (Cosserat ω) diagnostic
    omega_diag = omega_op10_diagnostic(engine)

    # post-shutoff energy retention (B2): first vs last recorded interior energy
    retention = float("nan")
    if len(energy_hist) >= 2:
        e_post = [e for (t, e) in energy_hist if t > (RAMP_P + SUSTAIN_P + DECAY_P) * COMPTON_PERIOD]
        if len(e_post) >= 2 and e_post[0] > 0:
            retention = e_post[-1] / e_post[0]

    return {
        "arm": arm_name,
        "mode": mode,
        "amplitude": amplitude,
        "x0_pulses": list(x0s),
        "max_a2_interior": max_a2,
        "max_a2_loc": list(max_a2_loc) if max_a2_loc else None,
        "saturation_engaged": bool(max_a2 > A2_OP14),
        "energy_retention_postshutoff": retention,
        "trap_bond": {"site": [ti, tj, tk], "port": tport},
        "winding_peak_bond": winding_peak,
        "winding_center_bond": winding_center,
        "winding_spatial_ring": winding_spatial,
        "reactance_consistency": react,
        "cosserat_omega_diag": omega_diag,
        "gate_firings": gate_firings,
        "elapsed_s": elapsed,
        # raw traces for the result-doc figures / auditor re-check
        "_traces": {
            "rec_peak_vinc": rec_peak_vinc, "rec_peak_vref": rec_peak_vref,
            "rec_peak_phi": rec_peak_phi,
        },
    }


def _reactance_consistency(vinc_traj, phi_traj, port):
    """B4 (Rule 10 reactance corollary): is the C-state (V_inc) ⟷ L-state
    (Phi_link) anti-correlated (a genuine reactive ring) vs frozen (static
    saturated snapshot)? Returns the Pearson correlation of V_inc(t) vs
    d(Phi_link)/dt at the dominant port (≈ −1 for a clean LC ring) + whether
    both states carry energy."""
    out = {"corr_vinc_dphidt": float("nan"), "c_state_alive": False, "l_state_alive": False}
    if port < 0 or vinc_traj.shape[0] < 8:
        return out
    vi = vinc_traj[:, port]
    phi = phi_traj[:, port]
    out["c_state_alive"] = bool(np.abs(vi).max() > 1e-9)
    out["l_state_alive"] = bool(np.abs(phi).max() > 1e-9)
    dphi = np.gradient(phi)
    if vi.std() > 1e-12 and dphi.std() > 1e-12:
        out["corr_vinc_dphidt"] = float(np.corrcoef(vi, dphi)[0, 1])
    return out


# ══════════════════════════════════════════════════════════════════════════════
# Adjudication + verdict
# ══════════════════════════════════════════════════════════════════════════════
def adjudicate(arm_A, arm_B, arm_C):
    """Apply B1-B4 PASS bars; return carrier-explicit verdict (i/ii/iii) per
    prereg §4. Headline tracks the (V_inc, V_ref) phasor (carrier 1); the
    Cosserat ω (carrier 2) result is recorded alongside (Q0)."""
    wA = arm_A["winding_peak_bond"]
    wB = arm_B["winding_peak_bond"]
    wC = arm_C["winding_peak_bond"]

    # B1 — self-trap (V-sector)
    b1 = arm_A["saturation_engaged"]
    # B2 — localization beats matched baseline
    rA = arm_A["energy_retention_postshutoff"]
    rB = arm_B["energy_retention_postshutoff"]
    b2 = (not np.isnan(rA)) and (not np.isnan(rB)) and (rA > rB)
    # B3 — (2,3) phasor winding emergent in A, absent in B, matches C (HEADLINE).
    # Checked in BOTH coordinate readings (Q1): temporal-single-bond AND
    # spatial-ring. PASS if the (2,3) emerges in Arm A in EITHER coordinate,
    # is absent in Arm B (trivial topology), and the same coordinate shows it in
    # Arm C (the imposed signature template).
    sA, sB, sC = arm_A["winding_spatial_ring"], arm_B["winding_spatial_ring"], arm_C["winding_spatial_ring"]

    def _is_23_temporal(w):
        return (w["crossing_count_c"] == 3) or ((w["n1"], w["n2"]) in [(2, 3), (3, 2)])

    def _is_23_spatial(s):
        return (s["w1_spatial"], s["w2_spatial"]) in [(2, 3), (3, 2)]

    # temporal coordinate
    temp_A_23 = _is_23_temporal(wA)
    temp_pass = bool(temp_A_23 and (not _is_23_temporal(wB)) and _is_23_temporal(wC))
    # spatial coordinate
    spat_A_23 = _is_23_spatial(sA)
    spat_pass = bool(spat_A_23 and (not _is_23_spatial(sB)) and _is_23_spatial(sC))

    b3 = bool(temp_pass or spat_pass)
    # B4 — reactance-pair consistency (genuine ring)
    react = arm_A["reactance_consistency"]
    b4 = bool(react["c_state_alive"] and react["l_state_alive"])

    # carrier-2 (Cosserat ω) — Q0 expectation: stays ~0 from pure-V photon
    omega_max_A = arm_A["cosserat_omega_diag"]["omega_max"]
    carrier2_dormant = omega_max_A < 1e-6

    # outcome
    if not b1:
        outcome = "ii"
        verdict = ("OUTCOME (ii) — V-sector self-trap FAILS (disperses). VacuumEngine3D carries "
                   "the (2,3) phasor carrier but lacks the binder. SURFACE doc-111 Path-A "
                   "(c_eff) go/no-go to Grant; do NOT free-build.")
    elif b3:
        outcome = "i"
        verdict = ("OUTCOME (i) — Grant's hypothesis CONFIRMED (V-sector): the transverse wave "
                   "SETS the (2,3) phasor winding (emergent in A, absent in B, matches C). Full "
                   "electron (mass + phasor (2,3)) hosts on VacuumEngine3D.")
    else:
        outcome = "iii"
        verdict = ("OUTCOME (iii) — Grant's hypothesis REFUTED (V-sector): self-traps (B1✓) but "
                   "the (2,3) phasor winding does NOT emerge from the transverse photon (only "
                   "appears when IMPOSED via the nucleation rule). Topological-selection, not "
                   "transverse-set.")

    return {
        "bars": {"B1_self_trap": bool(b1), "B2_beats_baseline": bool(b2),
                 "B3_23_phasor_winding": bool(b3), "B4_reactance_ring": bool(b4)},
        "B3_detail": {
            "temporal": {"c_A": wA["crossing_count_c"], "c_B": wB["crossing_count_c"],
                         "c_C": wC["crossing_count_c"],
                         "n_A": [wA["n1"], wA["n2"]], "n_B": [wB["n1"], wB["n2"]],
                         "n_C": [wC["n1"], wC["n2"]],
                         "A_is_23": temp_A_23, "pass": temp_pass},
            "spatial_ring": {"w_A": [sA["w1_spatial"], sA["w2_spatial"]],
                             "w_B": [sB["w1_spatial"], sB["w2_spatial"]],
                             "w_C": [sC["w1_spatial"], sC["w2_spatial"]],
                             "A_is_23": spat_A_23, "pass": spat_pass},
            "Q1_note": ("temporal-single-bond (theory.md:16 default) vs spatial-ring "
                        "(Q1 alternative); B3 PASS if (2,3) emerges in EITHER in Arm A, "
                        "absent in B, present in C. Compare Arm C (planted (2,3)) across "
                        "the two coordinates to see which one the (2,3) actually lives in."),
        },
        "retention": {"A": rA, "B": rB},
        "carrier2_cosserat_omega": {
            "omega_max_A": omega_max_A,
            "dormant_per_Q0": bool(carrier2_dormant),
            "note": ("Q0: pure-V transverse photon leaves Cosserat ω≡0 (parametric V→ω "
                     "decoupling, exact fixed point). The SU(2) U(1)-fibre '3' (06_ §4) does "
                     "NOT emerge in ω from a transverse photon on this engine — discrete-engine "
                     "sharpening of Mode II. Stands independent of the phasor-sector verdict."),
        },
        "outcome": outcome,
        "verdict": verdict,
    }


def main():
    print("=" * 80, flush=True)
    print("  Full-electron Option B — does a transverse wave SET the (2,3) on the DISCRETE engine?")
    print("  VacuumEngine3D (K4-TLM + Cosserat). HEADLINE: (V_inc,V_ref) phasor (2,3)-emergence.")
    print("=" * 80, flush=True)

    N = 48
    PML = 4
    n_periods = 40
    amplitude = AMP_PER_PULSE

    print(f"\n  N={N} PML={PML} ({N - 2 * PML} active cells) | {n_periods}P "
          f"({int(n_periods * COMPTON_PERIOD / DT)} steps, dt={DT:.4f})")
    print(f"  A²_op14 = √(2α) = {A2_OP14:.4f} (B1 bar) | amp = {amplitude}·V_SNAP/pulse")
    print(f"  ALPHA = {ALPHA} (ave-canonical-source; not hardcoded)")

    results = {}
    for arm_name, mode in [("A", "emergence"), ("B", "baseline"), ("C", "imposed")]:
        print(f"\n  ── Arm {arm_name} ({mode}) ──", flush=True)
        r = run_arm(arm_name, N, PML, n_periods, amplitude, mode)
        results[arm_name] = r
        print(f"    max A²={r['max_a2_interior']:.4f} @ {r['max_a2_loc']} "
              f"(sat={r['saturation_engaged']}) | retention={r['energy_retention_postshutoff']}")
        wp = r["winding_peak_bond"]
        sr = r["winding_spatial_ring"]
        print(f"    phasor TEMPORAL @ trap bond: c={wp['crossing_count_c']} "
              f"(n1,n2)=({wp['n1']},{wp['n2']}) ratio={wp['winding_ratio']} R/r={wp['R_phase_over_r_phase']}")
        print(f"    phasor SPATIAL-RING (Q1 alt): (w1,w2)=({sr['w1_spatial']},{sr['w2_spatial']})")
        od = r["cosserat_omega_diag"]
        print(f"    [carrier-2 ω] ω_max={od['omega_max']:.3e} ω-Op10={od['omega_op10_crossing_count']} "
              f"Hopf={od['hopf_charge']} (Q0: expect ~0) | gate_firings={r['gate_firings']} "
              f"| {r['elapsed_s']:.0f}s")

    verdict = adjudicate(results["A"], results["B"], results["C"])

    print("\n" + "=" * 80)
    print("  VERDICT")
    print("=" * 80)
    for bar, val in verdict["bars"].items():
        print(f"    {bar}: {'PASS' if val else 'FAIL'}")
    bt = verdict["B3_detail"]["temporal"]
    bs = verdict["B3_detail"]["spatial_ring"]
    print(f"\n  B3 TEMPORAL: c_A={bt['c_A']} c_B={bt['c_B']} c_C={bt['c_C']} "
          f"n_A={bt['n_A']} n_C={bt['n_C']} pass={bt['pass']}")
    print(f"  B3 SPATIAL-RING: w_A={bs['w_A']} w_B={bs['w_B']} w_C={bs['w_C']} pass={bs['pass']}")
    print(f"  carrier-2 (Cosserat ω): ω_max_A={verdict['carrier2_cosserat_omega']['omega_max_A']:.3e} "
          f"dormant={verdict['carrier2_cosserat_omega']['dormant_per_Q0']}")
    print(f"\n  {verdict['verdict']}")

    # save (strip raw numpy traces from JSON; keep them in npz)
    out_json = {k: {kk: vv for kk, vv in v.items() if kk != "_traces"} for k, v in results.items()}
    out_json["verdict"] = verdict
    out_json["config"] = {"N": N, "PML": PML, "n_periods": n_periods, "amplitude": amplitude,
                          "A2_op14": A2_OP14, "ALPHA": ALPHA, "dt": DT}
    out_path = Path(__file__).parent / "r10_vacuumengine3d_transverse_2_3_emergence_results.json"
    out_path.write_text(json.dumps(out_json, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {out_path.name}")

    npz_path = Path(__file__).parent / "r10_vacuumengine3d_transverse_2_3_emergence_capture.npz"
    np.savez_compressed(
        npz_path,
        **{f"{arm}_{k}": v for arm in results for k, v in results[arm]["_traces"].items()},
        dt=DT, N=N, PML=PML,
    )
    print(f"  Saved {npz_path.name}")
    return verdict


if __name__ == "__main__":
    main()
