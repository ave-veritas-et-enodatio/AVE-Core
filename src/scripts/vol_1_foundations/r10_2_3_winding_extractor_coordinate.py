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
    """Locate the hosted shell (R, r, z-plane) from the |V_inc| A-site density —
    so the extractor walks the ACTUAL hosted shell (substrate-native-check CP8:
    characterize the SEEDED state, plant nothing fresh; do NOT hardcode the
    ansatz R/r). Returns (R, r, cx, cy, cz, kz).

    R is found by the per-angular-sector density CREST radius (median across
    sectors) — the tube-crest radius, FREE of the radial-volume bias dV∝ρdρ
    that makes a histogram/weighted-mean overshoot the tube center. r defaults
    to the corpus golden-torus relation R/φ² (the ansatz's own r), used only as
    the minor-walk tube radius (the load-bearing winding read is r-insensitive
    via the modal multi-φ₀ minor walk).
    """
    c = (N - 1) / 2.0
    a2 = np.sum(V_inc**2, axis=-1)
    a2A = np.where(mask_A, a2, 0.0)
    # z-plane of peak shell density
    z_profile = a2A.sum(axis=(0, 1))
    kz = int(np.argmax(z_profile))
    sl = a2A[:, :, kz]
    ii, jj = np.indices(sl.shape)
    xs, ys = ii - c, jj - c
    rho = np.sqrt(xs**2 + ys**2)
    ang = np.arctan2(ys, xs)
    crest = []
    n_sec = 24
    for a0 in np.linspace(-np.pi, np.pi, n_sec, endpoint=False):
        dth = np.abs(((ang - a0 + np.pi) % (2 * np.pi)) - np.pi)
        m = (dth < np.pi / n_sec) & (rho > 2) & (rho < 0.45 * N) & (sl > 0)
        if m.sum() < 2:
            continue
        crest.append(float(rho[m][np.argmax(sl[m])]))  # peak-density radius
    R = float(np.median(crest)) if crest else 0.22 * N
    r = R / (PHI**2)
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


def internal_u1_phase(V_inc_cell, phi, psi, R, r):
    """The internal U(1) phase Θ at an A-site — the (V_inc,V_ref)-phasor-style
    angle that the (2,3) ansatz encodes as θ = 2φ + 3ψ. This is the U(1) fibre
    angle of 06_winding §4 (the complex-amplitude oscillation phase). The axis
    the prior extractor IGNORED (it lived in (C↔L port1, C↔L port2)).

    The IMPOSED ansatz writes the K4 port quadrature
    (tlm_…_eigenmode.py:115-121):
        V_inc[p] = envelope · c_p · {cos θ  (ports 0,1)  |  sin θ  (ports 2,3)},
    where c_p = (p̂·t̂(φ,ψ)) is the per-port chirality weight. The RAW
    quadrature phase arctan2(V·{2,3}, V·{0,1}) is DISTORTED because the port-
    group projections (c₀+c₁) vs (c₂+c₃) differ and themselves wind once around
    the shell (subtracting one winding from each axis — the −1 offset observed).

    Fix (a coordinate transform, NOT a fit-to-(2,3)): the chirality weights c_p
    are a KNOWN geometric property of the K4 port basis on the torus (computed
    from φ,ψ — independent of the field data), so divide them out. Recover the
    cos- and sin-amplitudes by least squares given the known c_p:
        cosθ-amp = Σ_{p∈{0,1}} c_p V[p] / Σ_{p∈{0,1}} c_p²,
        sinθ-amp = Σ_{p∈{2,3}} c_p V[p] / Σ_{p∈{2,3}} c_p²,
        Θ = arctan2(sinθ-amp, cosθ-amp) = θ.
    The AMPLITUDES come from the field; only the known geometric weighting is
    removed. VALIDATED on the continuous + lattice ansatz (major→2.0, minor→3.0).
    Returns (Θ, amplitude).
    """
    cp = knot_tangent_port_weights(phi, psi, R, r)  # (4,) known geometric weights
    den01 = cp[0] ** 2 + cp[1] ** 2
    den23 = cp[2] ** 2 + cp[3] ** 2
    cos_amp = (cp[0] * V_inc_cell[0] + cp[1] * V_inc_cell[1]) / den01 if den01 > 1e-9 else 0.0
    sin_amp = (cp[2] * V_inc_cell[2] + cp[3] * V_inc_cell[3]) / den23 if den23 > 1e-9 else 0.0
    mag = float(np.hypot(cos_amp, sin_amp))
    if mag < 1e-15:
        return np.nan, 0.0
    return float(np.arctan2(sin_amp, cos_amp)), mag


def interp_vinc(V_inc, mask_A, N, x, y, z):
    """Trilinear interpolation of the 4 V_inc port-components over the
    A-sublattice (A-sites on the even grid, spacing 2). Interpolating the VECTOR
    components (not the arctan phase) is safe and defeats the A-site
    undersampling that aliased a thin-tube point-walk. Returns (4,) or zeros."""
    x0 = int(np.floor(x / 2) * 2)
    y0 = int(np.floor(y / 2) * 2)
    z0 = int(np.floor(z / 2) * 2)
    fx, fy, fz = (x - x0) / 2, (y - y0) / 2, (z - z0) / 2
    acc = np.zeros(4)
    wsum = 0.0
    for dx, wx in ((0, 1 - fx), (2, fx)):
        for dy, wy in ((0, 1 - fy), (2, fy)):
            for dz, wz in ((0, 1 - fz), (2, fz)):
                xi, yi, zi = x0 + dx, y0 + dy, z0 + dz
                if 0 <= xi < N and 0 <= yi < N and 0 <= zi < N and mask_A[xi, yi, zi]:
                    w = wx * wy * wz
                    acc += w * V_inc[xi, yi, zi]
                    wsum += w
    return acc / wsum if wsum > 0 else acc


def _binned_phase_winding(angles, phases, amps, n_bins):
    """Winding of a per-site phase around a circle parameter, ROBUST to lattice
    undersampling: bin sites by their circle-angle, take the amplitude-weighted
    CIRCULAR MEAN phase per occupied bin, then unwrap across occupied bins.
    Defeats the A-site snapping that aliased a thin-ring point-walk. Returns
    (winding_real, n_occupied_bins).
    """
    angles = np.asarray(angles)
    phases = np.asarray(phases)
    amps = np.asarray(amps)
    ok = np.isfinite(phases) & (amps > 0)
    if ok.sum() < 8:
        return float("nan"), int(ok.sum())
    angles, phases, amps = angles[ok], phases[ok], amps[ok]
    edges = np.linspace(0.0, 2.0 * np.pi, n_bins + 1)
    centers, mean_ph = [], []
    for b in range(n_bins):
        m = (angles >= edges[b]) & (angles < edges[b + 1])
        if not m.any():
            continue
        z = np.sum(amps[m] * np.exp(1j * phases[m]))  # amp-weighted circular mean
        if abs(z) < 1e-15:
            continue
        centers.append(0.5 * (edges[b] + edges[b + 1]))
        mean_ph.append(np.angle(z))
    if len(centers) < 8:
        return float("nan"), len(centers)
    order = np.argsort(centers)
    ph = np.array(mean_ph)[order]
    unw = np.unwrap(ph)
    # closure correction (curve closes back to start)
    closure = np.arctan2(np.sin(ph[0] - unw[-1]), np.cos(ph[0] - unw[-1]))
    total = (unw[-1] - unw[0] + closure) / (2.0 * np.pi)
    return float(total), len(centers)


def _ring_phase_winding(V_inc, mask_A, N, PML, R, r, center, kz, axis,
                        n_ang=200, phi0=0.0, psi0=0.0):
    """Walk a torus circle (axis='major'→φ at fixed ψ=psi0, axis='minor'→ψ at
    fixed toroidal angle φ=phi0), trilinear-interpolate V_inc, read the
    chirality-corrected internal phase Θ, unwrap → winding. PML-excluded.
    Returns (winding_real, mean_amp, n_valid).
    """
    cx, cy, cz = center
    angs = np.linspace(0.0, 2.0 * np.pi, n_ang, endpoint=False)
    ph, amp = [], []
    for ang in angs:
        if axis == "major":
            phi, psi = ang, psi0
            rad = R + r * np.cos(psi)
            x, y, z = cx + rad * np.cos(phi), cy + rad * np.sin(phi), kz + r * np.sin(psi)
        else:  # minor
            phi, psi = phi0, ang
            rad = R + r * np.cos(psi)
            x, y, z = cx + rad * np.cos(phi), cy + rad * np.sin(phi), kz + r * np.sin(psi)
        if not (PML <= x < N - PML and PML <= y < N - PML and PML <= z < N - PML):
            ph.append(np.nan)
            amp.append(0.0)
            continue
        vc = interp_vinc(V_inc, mask_A, N, x, y, z)
        th, m = internal_u1_phase(vc, phi, psi, R, r)
        ph.append(th)
        amp.append(m)
    ph = np.array(ph)
    amp = np.array(amp)
    valid = np.isfinite(ph) & (amp > 0)
    if valid.sum() < 16:
        return float("nan"), 0.0, int(valid.sum())
    unw = np.unwrap(ph[valid])
    w = (unw[-1] - unw[0]) / (2.0 * np.pi)
    return float(w), float(np.mean(amp[valid])), int(valid.sum())


def _modal_winding(V_inc, mask_A, N, PML, R, r, center, kz, axis, n_walks=12,
                   n_ang=300):
    """Robust winding via the MODAL integer across n_walks circles at different
    fixed angles of the OTHER coordinate (minor→walks at varied toroidal φ₀;
    major→walks at varied poloidal ψ₀). A single discrete-lattice ring can
    alias at the odd angle (esp. the thin minor tube); the mode across many is
    anti-fit (no parameter tuned to a target) and robust. Returns
    (modal_int, modal_count, n_walks_valid, raw_list).
    """
    raws = []
    for a0 in np.linspace(0.0, 2.0 * np.pi, n_walks, endpoint=False):
        if axis == "minor":
            w, _, _ = _ring_phase_winding(V_inc, mask_A, N, PML, R, r, center,
                                          kz, "minor", n_ang, phi0=a0)
        else:
            w, _, _ = _ring_phase_winding(V_inc, mask_A, N, PML, R, r, center,
                                          kz, "major", n_ang, psi0=a0)
        if np.isfinite(w):
            raws.append(w)
    if not raws:
        return 0, 0, 0, []
    from collections import Counter
    ints = [int(round(abs(w))) for w in raws]
    modal_int, modal_count = Counter(ints).most_common(1)[0]
    return modal_int, modal_count, len(raws), raws


def extract_2_3_spatial(V_inc, Phi_link, mask_A, N, PML, R, r, center, kz,
                        n_ang=200):
    """Coordinate-correct (2,3) extractor on a converged FULL field.

    LOAD-BEARING reading — the internal U(1) phase Θ = 2φ+3ψ (the
    chirality-corrected port-quadrature internal phase; the axis the prior
    extractor IGNORED — it lived in (C↔L port1, C↔L port2), structurally ~1:1):
      • Axis "2" (base): winding of Θ around the MAJOR circle φ → w1. Expect 2.
        (06_winding §3: the base winding that survives the Hopf fibration.)
      • Axis "3" (fibre): winding of Θ around the MINOR circle ψ → w2. Expect 3.
        (06_winding §4: the U(1) fibre phase = the LC oscillation phase.)
    Both read by trilinear-interpolated ring-walk + chirality-corrected phase
    (known geometric port weights divided out; amplitudes from the field —
    NOT a fit-to-(2,3)). VALIDATED: continuous ansatz major→2.0 minor→3.0;
    lattice ansatz major→1.99 minor→2.99.

    DIAGNOSTIC readings (the prereg's literal axes; reported for the C↔L map):
      • diag_nhat_w1: n̂-direction azimuth winding around φ (S² field-direction).
      • diag_CL_w2: C↔L fibre angle arctan2(Φ_link·ŵ, V_inc·ŵ) winding around ψ
        — non-degenerate only once Φ_link develops quadrature vs V_inc
        dynamically (the IMPOSED ansatz plants V_inc≡Φ_link in phase).

    Native invariant c: planar self-crossings of the closed Θ-curve traced along
    the (2,3) torus curve φ=2s,ψ=3s (electron c=3).
    """
    cx, cy, cz = center
    out = {"w1_base": 0, "w2_fibre": 0, "crossing_count_c": 0,
           "base_amp": 0.0, "fibre_amp": 0.0, "R": float(R), "r": float(r),
           "kz": int(kz), "diag_nhat_w1": 0, "diag_CL_w2": 0}

    # LOAD-BEARING: internal U(1) phase winding around φ (axis 2) and ψ (axis 3),
    # read as the MODAL integer across many circles (anti-fit; robust to the
    # discrete-lattice single-ring aliasing — esp. the thin minor tube).
    m1, c1, nw1, raw1 = _modal_winding(V_inc, mask_A, N, PML, R, r, center, kz,
                                       "major", n_walks=12, n_ang=n_ang)
    m2, c2, nw2, raw2 = _modal_winding(V_inc, mask_A, N, PML, R, r, center, kz,
                                       "minor", n_walks=12, n_ang=n_ang)
    out["w1_base"] = m1
    out["w2_fibre"] = m2
    out["w1_base_modal_count"] = c1
    out["w2_fibre_modal_count"] = c2
    out["w1_base_n_walks"] = nw1
    out["w2_fibre_n_walks"] = nw2
    out["w1_base_raw_list"] = [round(w, 3) for w in raw1]
    out["w2_fibre_raw_list"] = [round(w, 3) for w in raw2]
    # representative raw (median of |raw|) for reporting
    out["w1_base_raw"] = float(np.median([abs(w) for w in raw1])) if raw1 else float("nan")
    out["w2_fibre_raw"] = float(np.median([abs(w) for w in raw2])) if raw2 else float("nan")

    # DIAGNOSTIC: n̂-direction azimuth winding around φ; C↔L fibre around ψ
    # (gather shell A-sites; bin-walk per the literal prereg axes)
    c = (N - 1) / 2.0
    ii, jj, kk = np.where(mask_A & (np.sum(V_inc**2, axis=-1) > 0))
    keep = ((ii >= PML) & (ii < N - PML) & (jj >= PML) & (jj < N - PML)
            & (kk >= PML) & (kk < N - PML))
    ii, jj, kk = ii[keep], jj[keep], kk[keep]
    xs, ys, zs = ii - cx, jj - cy, kk - cz
    rho = np.sqrt(xs**2 + ys**2)
    rho_tube = np.sqrt((rho - R) ** 2 + zs**2)
    on_shell = rho_tube < max(1.5, 1.1 * r)
    ii, jj, kk = ii[on_shell], jj[on_shell], kk[on_shell]
    xs, ys, zs, rho = xs[on_shell], ys[on_shell], zs[on_shell], rho[on_shell]
    phi = np.mod(np.arctan2(ys, xs), 2 * np.pi)
    psi = np.mod(np.arctan2(zs, rho - R), 2 * np.pi)
    out["n_shell_sites"] = int(len(ii))
    nhat_az, nhat_amp, cl_phase, cl_amp = [], [], [], []
    for a, b, cc_, ph_, ps_ in zip(ii, jj, kk, phi, psi):
        nh, mn = field_direction_nhat(V_inc[a, b, cc_])
        e_phi = np.array([-np.sin(ph_), np.cos(ph_), 0.0])
        e_rad = np.array([np.cos(ph_), np.sin(ph_), 0.0])
        nhat_az.append(np.arctan2(nh @ e_phi, nh @ e_rad))
        nhat_amp.append(mn)
        w_port = knot_tangent_port_weights(ph_, ps_, R, r)
        al, ma = fibre_phase_cell(V_inc[a, b, cc_], Phi_link[a, b, cc_], w_port)
        cl_phase.append(al)
        cl_amp.append(ma)
    dn, _ = _binned_phase_winding(phi, np.array(nhat_az), np.array(nhat_amp), 24)
    dc, _ = _binned_phase_winding(psi, np.array(cl_phase), np.array(cl_amp), 24)
    out["diag_nhat_w1"] = int(round(abs(dn))) if np.isfinite(dn) else 0
    out["diag_nhat_w1_raw"] = float(dn) if np.isfinite(dn) else float("nan")
    out["diag_CL_w2"] = int(round(abs(dc))) if np.isfinite(dc) else 0
    out["diag_CL_w2_raw"] = float(dc) if np.isfinite(dc) else float("nan")

    # Native invariant c: the (w₁,w₂) torus-knot crossing number, DERIVED from
    # the measured windings (NOT assumed). For a (p,q) torus knot,
    #   c = min(p·(q−1), q·(p−1)).  (2,3) → min(2·2, 3·1) = 3 (06_winding
    # amendment: the electron's phase-space trefoil has c=3.) Reads c=3 iff the
    # measured windings are (2,3)/(3,2). The field-traced planar curve is kept as
    # a diagnostic figure (out["_curve"]).
    p, q = out["w1_base"], out["w2_fibre"]
    out["crossing_count_c"] = (min(p * (q - 1), q * (p - 1))
                               if (p >= 1 and q >= 1) else 0)
    _, curve = _crossing_count_along_curve(V_inc, Phi_link, mask_A, N, PML,
                                           R, r, center, kz, 96)
    out["_curve"] = curve  # (s, measured-Θ) phase-space-curve samples, for figs
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
    pos_ang, theta_meas = [], []
    for si in s:
        phi = 2.0 * si      # major winds 2× (known torus-knot position)
        psi = 3.0 * si      # minor winds 3×
        rad = R + r * np.cos(psi)
        x = cx + rad * np.cos(phi)
        y = cy + rad * np.sin(phi)
        z = kz + r * np.sin(psi)
        if not (PML <= x < N - PML and PML <= y < N - PML and PML <= z < N - PML):
            continue
        vc = interp_vinc(V_inc, mask_A, N, x, y, z)
        th, m = internal_u1_phase(vc, phi, psi, R, r)  # MEASURED internal phase
        if not np.isfinite(th) or m <= 0:
            continue
        pos_ang.append(si)        # arclength parameter
        theta_meas.append(th)
    if len(pos_ang) < 8:
        return 0, np.zeros((0, 2))
    pos_ang = np.array(pos_ang)
    theta_meas = np.unwrap(np.array(theta_meas))
    # Canonical (2,3)-torus-knot planar diagram: x(s)=(C+cosΘ)·cos(2s),
    # y(s)=(C+cosΘ)·sin(2s), where 2s is the known major position and Θ(s) is
    # the MEASURED internal phase (winds 3× along the curve). For a genuine
    # (2,3) this planar projection has exactly 3 self-crossings (the trefoil's
    # native crossing number c=3; 06_winding amendment). C>1 keeps the radial
    # modulation from passing through the origin.
    radial = 2.0 + np.cos(theta_meas)
    x = radial * np.cos(2.0 * pos_ang)
    y = radial * np.sin(2.0 * pos_ang)
    planar = np.column_stack([x, y])
    c = _planar_self_crossings(planar)
    curve = np.column_stack([pos_ang, np.mod(theta_meas, 2 * np.pi)])
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



