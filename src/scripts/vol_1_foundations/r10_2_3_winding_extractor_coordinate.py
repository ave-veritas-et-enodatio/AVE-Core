"""
Coordinate-correct (2,3)-winding extractor + VALIDATION GATE.

Prereg (FROZEN): research/2026-06-05_2-3-winding-extractor-coordinate-prereg.md
Brief:           _orchestration/2026-06-05_2-3-winding-extractor.md
Resolves the prior run's auditor #1 (BLOCKING): the (2,3)-winding extractor was
UNVALIDATED — the shipped `phasor_temporal_winding`
(r10_vacuumengine3d_transverse_2_3_emergence.py) read `(8,0)/c=16` on the
Arm-C KNOWN-IMPOSED (2,3) bond. An extractor that cannot see a known-imposed
(2,3) cannot certify its absence.

KEEP-BOTH (audit-trail continuity): this is a NEW module. The shipped
`phasor_temporal_winding` is NOT redefined.

────────────────────────────────────────────────────────────────────────────
THE COORDINATE DIAGNOSIS (phase-space-coordinate-check — THE load-bearing skill)
────────────────────────────────────────────────────────────────────────────
The (2,3) is a PAIR of DISTINCT windings on the Clifford torus
(06_winding_index_projection.md §3-4):

  • Axis "2" (BASE): winding of the field-DIRECTION n̂ — the S² polarization /
    E-field direction unit vector that SURVIVES the Hopf fibration. NOT a port
    phasor angle.
  • Axis "3" (FIBRE): the U(1) internal phase — the C↔L / LC-slosh phase, built
    from the C-state `V_inc` vs the L-state `Phi_link`. The information LOST in
    the Hopf projection (§4); the axis the prior extractor IGNORED
    (`phi_traj` was an unused optional arg).

The prior extractor set θ₁ = port-1 (V_inc,V_ref) phasor angle, θ₂ = port-2
phasor angle. A port's (V_inc,V_ref) phasor angle IS that port's C↔L angle
(transmission-line identity: (V_inc,V_ref) is a 45° rotation of (V, Z₀I) =
(C-state, L-state)). Two ports of one bond ring at the SAME LC frequency →
ratio structurally ~1:1, never (2,3). Wrong axes: it lived in (C↔L, C↔L).

THE ANSATZ IS SPATIAL. `initialize_2_3_voltage_ansatz` plants
`theta_wind = 2φ + 3ψ` where φ = toroidal (major-circle) angle and
ψ = poloidal (minor-circle) angle ON A TOROIDAL SHELL. At any single fixed
bond, φ and ψ are constants → `theta_wind` is a constant → a single-bond TIME
series carries NO 2φ+3ψ winding (only the temporal LC slosh). The (2,3) is a
SPATIAL standing pattern; it must be read by WALKING THE SHELL, not by watching
one bond oscillate in time. This is why the capture npz (single-bond time
series only) cannot host V0 — and why this extractor reads the FULL FIELD.

────────────────────────────────────────────────────────────────────────────
WHAT THIS EXTRACTOR READS (the fix)
────────────────────────────────────────────────────────────────────────────
On the converged FULL field of the Arm-C bound state:

  • Axis "2" (base): walk the major circle φ at the shell's tube; at each site
    reconstruct n̂ = Σ_p V_inc[p]·p̂ / |·| (port-weighted tetrahedral direction =
    the polarization/E-field direction); project into the local toroidal tangent
    frame and unwrap the azimuth → w₁. Expect 2.
  • Axis "3" (fibre): walk the minor circle ψ; at each site form a PORT-COHERENT
    fibre phase α = arctan2(Φ_link·ŵ, V_inc·ŵ) (C-state V_inc vs L-state
    Φ_link, coherent knot-tangent port projection ŵ — NOT per-site argmax,
    which scrambles the structure); unwrap → w₂. Expect 3.
  • Native invariant c: planar self-crossing count of the closed curve in the
    correct (base-azimuth, fibre-phase) plane along the (2,3) curve. Electron
    c = 3.

V0 (BLOCKING anti-fit gate): on Arm C this must recover c=3 (±0) OR (w₁,w₂)=
(2,3), where the legacy read `(8,0)/c=16`. This is a forward READ of a KNOWN
signal — no optimizer is run onto (2,3) (ave-driver-script-honesty).
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import ALPHA  # noqa: E402

# ── Substrate-derived constants (ave-canonical-source: NO hardcoded literals) ──
PHI = (1.0 + np.sqrt(5.0)) / 2.0          # golden ratio (R/r torus aspect)
A2_OP14 = float(np.sqrt(2.0 * ALPHA))     # √(2α) — Op14 engagement
DT = 1.0 / np.sqrt(2.0)                    # K4-TLM 4-port junction timestep
COMPTON_PERIOD = 2.0 * np.pi

# K4 tetrahedral A-site port directions (A→B bond vectors); the n̂ field
# direction is the V_inc-weighted sum of these (tlm_…_eigenmode.py:99-104).
PORT_DIRS = np.array([
    [+1.0, +1.0, +1.0],
    [+1.0, -1.0, -1.0],
    [-1.0, +1.0, -1.0],
    [-1.0, -1.0, +1.0],
]) / np.sqrt(3.0)


# ══════════════════════════════════════════════════════════════════════════════
# Shell geometry + per-site field-direction n̂ and fibre phase
# ══════════════════════════════════════════════════════════════════════════════
def field_direction_nhat(V_inc_cell):
    """The S² field-DIRECTION n̂ at one A-site (axis "2" base quantity).

    n̂ = (Σ_p V_inc[p]·p̂) / |Σ_p V_inc[p]·p̂|, the port-weighted tetrahedral
    direction — the polarization / E-field direction unit vector. This is the
    Level-2 (Hopf-base) S² object of 06_winding §3 (the winding that SURVIVES
    the fibration). Returns (n̂ (3,), magnitude).  NOT a port phasor angle.
    """
    vec = PORT_DIRS.T @ V_inc_cell  # (3,)
    mag = float(np.linalg.norm(vec))
    if mag < 1e-12:
        return np.zeros(3), 0.0
    return vec / mag, mag


def fibre_phase_cell(V_inc_cell, Phi_link_cell, w_port):
    """The U(1) fibre phase at one A-site (axis "3" fibre quantity).

    α = arctan2(Φ_link·ŵ, V_inc·ŵ) — the C-state (V_inc) vs L-state (Φ_link)
    angle, projected onto a COHERENT port weight ŵ (the knot-tangent port
    projection). Coherent projection (not per-site argmax) is required: the
    dominant port FLIPS sign with the chirality_weight as we walk the shell, so
    an argmax-per-site read scrambles the 2φ+3ψ structure (the legacy
    spatial-ring extractor's `(0,0)` failure mode).

    This is the axis the prior extractor IGNORED. Per prereg §2 the C↔L↔fibre
    identification is the one mapping to PIN (Grant 2026-06-05): built here from
    V_inc (C) vs Phi_link (L), the two halves of the K4 LC reactance pair.
    Returns (α, projected reactive magnitude).
    """
    c_state = float(V_inc_cell @ w_port)        # C-state projection
    l_state = float(Phi_link_cell @ w_port)     # L-state projection
    mag = float(np.hypot(c_state, l_state))
    if mag < 1e-15:
        return 0.0, 0.0
    return float(np.arctan2(l_state, c_state)), mag


def knot_tangent_port_weights(phi, psi, R, r):
    """Coherent port weight ŵ(φ,ψ) = projection of each K4 port direction onto
    the (2,3) knot-tangent t̂(φ,ψ) — the SAME weighting the ansatz uses
    (tlm_…_eigenmode.py:112-121). Using it as the coherent fibre projection
    follows the field's own chirality structure around the shell instead of
    fighting it with an argmax. Returns (4,) port weights.
    """
    dphi = np.array([-(R + r * np.cos(psi)) * np.sin(phi),
                     (R + r * np.cos(psi)) * np.cos(phi), 0.0])
    dpsi = np.array([-r * np.sin(psi) * np.cos(phi),
                     -r * np.sin(psi) * np.sin(phi), r * np.cos(psi)])
    t = 2.0 * dphi + 3.0 * dpsi
    tn = np.linalg.norm(t)
    if tn < 1e-12:
        return np.ones(4) / 2.0
    t_hat = t / tn
    return PORT_DIRS @ t_hat  # (4,)  per-port chirality weight


def shell_params_from_field(V_inc, mask_A, N):
    """Estimate the shell (R, r, z-plane) from the |V_inc| A-site density —
    so the extractor walks the ACTUAL hosted shell (substrate-native-check CP8:
    characterize the SEEDED state, plant nothing fresh; do NOT hardcode the
    ansatz R/r). Returns (R, r, cz, cx, cy, kz).
    """
    c = (N - 1) / 2.0
    a2 = np.sum(V_inc**2, axis=-1)
    a2A = np.where(mask_A, a2, 0.0)
    # z-plane of peak shell density
    z_profile = a2A.sum(axis=(0, 1))
    kz = int(np.argmax(z_profile))
    # radial profile in that z-plane
    sl = a2A[:, :, kz]
    ii, jj = np.indices(sl.shape)
    rho = np.sqrt((ii - c) ** 2 + (jj - c) ** 2)
    rmax = float(rho.max())
    nb = max(8, int(round(rmax)))
    edges = np.linspace(0, rmax, nb + 1)
    w, _ = np.histogram(rho.ravel(), bins=edges, weights=sl.ravel())
    cnt, _ = np.histogram(rho.ravel(), bins=edges)
    prof = np.where(cnt > 0, w / np.maximum(cnt, 1), 0.0)
    centers = 0.5 * (edges[:-1] + edges[1:])
    R = float(centers[np.argmax(prof)]) if prof.max() > 0 else 0.22 * N
    # tube half-width via FWHM of the radial peak
    half = 0.5 * prof.max()
    above = centers[prof >= half] if prof.max() > 0 else np.array([R])
    r = float(max((above.max() - above.min()) / 2.0, R / (PHI**2)))
    return R, r, c, c, c, kz


# ══════════════════════════════════════════════════════════════════════════════
# The coordinate-correct (2,3) extractor (the fix)
# ══════════════════════════════════════════════════════════════════════════════
def _sample_cell(V_inc, Phi_link, mask_A, N, PML, x, y, z):
    """Nearest interior A-site to a continuous (x,y,z); PML-excluded
    (Rule 10 PML corollary). Returns (i,j,k) or None."""
    i = int(np.clip(round(x), PML, N - PML - 1))
    j = int(np.clip(round(y), PML, N - PML - 1))
    k = int(np.clip(round(z), PML, N - PML - 1))
    # snap to nearest A-site (A: all-even) within a small neighborhood
    best = None
    best_a2 = -1.0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            for dk in (-1, 0, 1):
                ii, jj, kk = i + di, j + dj, k + dk
                if not (PML <= ii < N - PML and PML <= jj < N - PML
                        and PML <= kk < N - PML):
                    continue
                if not mask_A[ii, jj, kk]:
                    continue
                a2 = float(np.sum(V_inc[ii, jj, kk] ** 2))
                if a2 > best_a2:
                    best_a2, best = a2, (ii, jj, kk)
    return best


def extract_2_3_spatial(V_inc, Phi_link, mask_A, N, PML, R, r, center, kz,
                        n_ang=96):
    """Coordinate-correct (2,3) extractor on a converged FULL field.

    Axis "2" (base, n̂ DIRECTION) — walk the MAJOR circle φ on the tube
    (ψ=0, radius R+r in the kz plane); at each site reconstruct n̂ and unwrap
    its azimuth in the local toroidal tangent frame → w1. (06_winding §3: the
    base-space n̂ winding survives the Hopf fibration; w1=2.)

    Axis "3" (fibre, C↔L PHASE) — walk the MINOR circle ψ at a fixed toroidal
    angle (in the (radial,z) tube cross-section); at each site form the
    coherent fibre phase α = arctan2(Φ_link·ŵ, V_inc·ŵ) and unwrap → w2.
    (06_winding §4: U(1) fibre phase = the LC/C↔L slosh; w2=3.)

    Native invariant c: planar self-crossings of the closed (base-azimuth,
    fibre-phase) curve traced along the (2,3) torus curve (electron c=3).

    Returns dict (w1_base, w2_fibre, crossing_count_c, base_amp, fibre_amp,
    closed-curve samples for the result-doc figure).
    """
    cx, cy, cz = center
    out = {"w1_base": 0, "w2_fibre": 0, "crossing_count_c": 0,
           "base_amp": 0.0, "fibre_amp": 0.0, "R": float(R), "r": float(r),
           "kz": int(kz), "n_sampled": 0}

    angs = np.linspace(0.0, 2.0 * np.pi, n_ang, endpoint=False)

    # ── Axis "2": n̂-direction azimuth around the MAJOR circle φ (ψ=0 tube top)
    base_az, base_amp = [], []
    for phi in angs:
        rad = R + r  # tube on the outer equator (ψ=0)
        x = cx + rad * np.cos(phi)
        y = cy + rad * np.sin(phi)
        cell = _sample_cell(V_inc, Phi_link, mask_A, N, PML, x, y, kz)
        if cell is None:
            base_az.append(np.nan)
            base_amp.append(0.0)
            continue
        nhat, mag = field_direction_nhat(V_inc[cell])
        # local toroidal tangent frame at φ: ê_φ (azimuthal), ê_r (radial)
        e_phi = np.array([-np.sin(phi), np.cos(phi), 0.0])
        e_rad = np.array([np.cos(phi), np.sin(phi), 0.0])
        az = np.arctan2(nhat @ e_phi, nhat @ e_rad)  # n̂ azimuth in tangent plane
        base_az.append(az)
        base_amp.append(mag)
    base_az = np.array(base_az)
    valid_b = ~np.isnan(base_az)
    out["base_amp"] = float(np.nanmean(base_amp)) if valid_b.any() else 0.0
    if valid_b.sum() >= 8 and out["base_amp"] > 1e-9:
        unw = np.unwrap(base_az[valid_b])
        out["w1_base"] = int(round((unw[-1] - unw[0]) / (2.0 * np.pi)))
        out["w1_base_raw"] = float((unw[-1] - unw[0]) / (2.0 * np.pi))

    # ── Axis "3": coherent fibre phase around the MINOR circle ψ (toroidal angle 0)
    fib_ph, fib_amp = [], []
    phi0 = 0.0
    for psi in angs:
        rad = R + r * np.cos(psi)
        x = cx + rad * np.cos(phi0)
        y = cy + rad * np.sin(phi0)
        z = kz + r * np.sin(psi)
        cell = _sample_cell(V_inc, Phi_link, mask_A, N, PML, x, y, z)
        if cell is None:
            fib_ph.append(np.nan)
            fib_amp.append(0.0)
            continue
        w_port = knot_tangent_port_weights(phi0, psi, R, r)
        alpha, mag = fibre_phase_cell(V_inc[cell], Phi_link[cell], w_port)
        fib_ph.append(alpha)
        fib_amp.append(mag)
    fib_ph = np.array(fib_ph)
    valid_f = ~np.isnan(fib_ph)
    out["fibre_amp"] = float(np.nanmean(fib_amp)) if valid_f.any() else 0.0
    if valid_f.sum() >= 8 and out["fibre_amp"] > 1e-12:
        unw = np.unwrap(fib_ph[valid_f])
        out["w2_fibre"] = int(round((unw[-1] - unw[0]) / (2.0 * np.pi)))
        out["w2_fibre_raw"] = float((unw[-1] - unw[0]) / (2.0 * np.pi))

    out["n_sampled"] = int(valid_b.sum() + valid_f.sum())

    # ── Native invariant c: crossing count of the closed (base, fibre) curve
    # along the (2,3) torus curve φ(s)=s, ψ(s)=s (the curve the knot traces).
    cc, curve = _crossing_count_along_curve(V_inc, Phi_link, mask_A, N, PML,
                                            R, r, center, kz, n_ang)
    out["crossing_count_c"] = cc
    out["_curve"] = curve  # (M,2) closed (base-azimuth, fibre-phase) samples
    return out


def _crossing_count_along_curve(V_inc, Phi_link, mask_A, N, PML, R, r,
                                center, kz, n_ang):
    """Trace the (2,3) torus curve φ(s)=2s, ψ(s)=3s for s∈[0,2π) and at each
    point read (n̂-azimuth, fibre-phase). The native invariant c is the planar
    self-crossing count of THAT closed curve (06_winding amendment: electron
    has c=3, the phase-space trefoil on the Clifford torus).

    The trefoil is the (2,3) curve; reading the two correct coordinates along
    it gives a closed planar curve whose self-crossings are the topological
    invariant. Returns (c, curve(M,2)).
    """
    cx, cy, cz = center
    s = np.linspace(0.0, 2.0 * np.pi, n_ang, endpoint=False)
    pts = []
    for si in s:
        phi = 2.0 * si      # major winds 2×
        psi = 3.0 * si      # minor winds 3×
        rad = R + r * np.cos(psi)
        x = cx + rad * np.cos(phi)
        y = cy + rad * np.sin(phi)
        z = kz + r * np.sin(psi)
        cell = _sample_cell(V_inc, Phi_link, mask_A, N, PML, x, y, z)
        if cell is None:
            continue
        nhat, _ = field_direction_nhat(V_inc[cell])
        e_phi = np.array([-np.sin(phi), np.cos(phi), 0.0])
        e_rad = np.array([np.cos(phi), np.sin(phi), 0.0])
        az = np.arctan2(nhat @ e_phi, nhat @ e_rad)
        w_port = knot_tangent_port_weights(phi, psi, R, r)
        alpha, _ = fibre_phase_cell(V_inc[cell], Phi_link[cell], w_port)
        pts.append([az, alpha])
    if len(pts) < 8:
        return 0, np.zeros((0, 2))
    curve = np.array(pts)
    # the (az, alpha) live on a torus; embed each angle on its own circle so the
    # crossing count is metric-meaningful and wrap-robust
    emb = np.column_stack([
        np.cos(curve[:, 0]), np.sin(curve[:, 0]),
        np.cos(curve[:, 1]), np.sin(curve[:, 1]),
    ])
    # project the 4D torus-embedded curve to its 2 dominant PCA axes for a
    # planar crossing count (the trefoil's c is projection-stable for a generic
    # 2-plane); center + PCA
    emb = emb - emb.mean(axis=0, keepdims=True)
    _, _, vt = np.linalg.svd(emb, full_matrices=False)
    planar = emb @ vt[:2].T  # (M,2)
    c = _planar_self_crossings(planar)
    return c, curve


def _planar_self_crossings(curve):
    """Count DISTINCT self-intersections of a CLOSED planar polyline. Near-
    duplicate crossings (same point hit by adjacent segment pairs) are merged
    by spatial clustering. The (2,3) trefoil → c=3."""
    n = len(curve)
    if n < 8:
        return 0
    # close the loop
    p = np.vstack([curve, curve[:1]])
    m = len(p)
    scale = float(np.sqrt(curve.var(axis=0).sum())) + 1e-12
    pts = []
    for i in range(m - 1):
        a1, a2 = p[i], p[i + 1]
        for j in range(i + 2, m - 1):
            if i == 0 and j == m - 2:  # adjacent across the closure
                continue
            ip = _seg_intersection_point(a1, a2, p[j], p[j + 1])
            if ip is not None:
                pts.append(ip)
    if not pts:
        return 0
    pts = np.array(pts)
    tol = 0.08 * scale
    clusters = []
    for q in pts:
        if not any(np.linalg.norm(q - c) < tol for c in clusters):
            clusters.append(q)
    return len(clusters)


def _seg_intersection_point(p1, p2, p3, p4):
    if not _seg_intersect(p1, p2, p3, p4):
        return None
    d1, d2 = p2 - p1, p4 - p3
    denom = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(denom) < 1e-15:
        return None
    t = ((p3[0] - p1[0]) * d2[1] - (p3[1] - p1[1]) * d2[0]) / denom
    return p1 + t * d1


def _seg_intersect(p1, p2, p3, p4):
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - a[0])
    d1, d2 = ccw(p3, p4, p1), ccw(p3, p4, p2)
    d3, d4 = ccw(p1, p2, p3), ccw(p1, p2, p4)
    return ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0))


def is_2_3(result):
    """V0/V1 adjudication: does the extractor read a (2,3)? PASS bar (prereg
    §4): c=3 (±0) OR (w1,w2) ∈ {(2,3),(3,2)}."""
    c = result.get("crossing_count_c", 0)
    w1, w2 = result.get("w1_base", 0), result.get("w2_fibre", 0)
    return (c == 3) or ((abs(w1), abs(w2)) in [(2, 3), (3, 2)])



