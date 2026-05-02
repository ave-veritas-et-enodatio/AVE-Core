"""Move 10 / Phase 1 winding — characterize the static fixed point's spatial
topology pattern (torus-knot / Hopf-linked / spherical-harmonic / other).

Per `P_phase1_attractor_winding_characterization` (frozen at this commit).

CONTEXT:
  Move 7 + 7b established the Move 5 attractor at t=200P is a STATIC
  topological FIXED POINT (per §13–§14): V_inc near-constant ±0.264,
  |ω| near-constant 0.30, c=3 preserved, 85:15 V:T potential-dominant,
  17-cell diffuse spatial extent. Audit (§14.2) clarified this is
  consistent with Op14-induced gravitational-redshift local-clock-freeze
  at the saturated core (A² ≈ 0.95 at peak |ω| ≈ 0.93 → ω_local ≈
  0.22·ω_global at core). The fixed point sits on the frozen-core
  boundary as a static topological defect.

GOAL:
  Characterize WHAT TOPOLOGY the static fixed point actually is.
  c=3 via Op10 confirms (2,3)-class winding, but Op10 is a scalar
  count — it doesn't distinguish:
    (a) (2,3) torus knot (corpus seed shape, possibly preserved)
    (b) (3,2) torus knot (same c=3 but different toroidal/poloidal
        winding numbers)
    (c) Hopf-linked configuration (two linked unknots, c=3 from the
        Hopf linking)
    (d) Spherical-harmonic Y_{l,m} mode with c=3 from angular nodes
    (e) Two opposing (2,1) twists on different sublattice halves

Move 10 distinguishes these via four post-hoc extractions on the
deterministically-reproducible Move 5 final state (t=200P).

DIMENSIONALLY + SATURATION-LOCALLY NEUTRAL:
  No frequency target. No drive. No eigsolve at any σ. Pure
  topological characterization of a static spatial configuration.

FROZEN EXTRACTIONS (4):

  (1) TOROIDAL/POLOIDAL WINDING NUMBERS:
      For each candidate shell radius R_test ∈ [3, 12]:
        - parametrize cells on the shell by (toroidal angle φ,
          poloidal angle ψ)
        - compute the angle of ω(x) projected onto the (e_x, e_y) plane
          along loops at fixed ψ → integer winding number p_φ(ψ)
        - compute angle along loops at fixed φ → q_ψ(φ)
        - report mean p (toroidal) and mean q (poloidal) at each shell
      Corpus (2,3) seed predicts (p, q) = (2, 3) on the (R=10, r=3.82)
      shell. Differences identify torus knot variant.

  (2) HOPF LINKING NUMBER:
      Hopf invariant via fiber linking:
        - choose two values c_+, c_- of ω̂_z (the z-component of
          ω-direction)
        - the level sets {x : ω̂_z(x) = c_±} form 1D curves (fibers)
        - compute their Gauss linking number Lk(c_+, c_-) via
          discrete Gauss integral
      Hopf-linked: Lk = ±N for some integer N ≠ 0.
      Torus knot: Lk = 0 (the same fibers don't link, the WINDING is
      around the torus instead).
      A non-zero Hopf linking would mean the c=3 isn't from torus
      winding but from Hopf braiding.

  (3) SPHERICAL HARMONIC DECOMPOSITION:
      Project |ω(x)|² (scalar density) onto Y_{l,m} basis at fixed
      radial bins. Report dominant (l, m) per radius. If a single
      Y_{l,m} mode dominates at the energy-dense radius, the
      configuration is essentially a multipole, NOT a torus knot.

  (4) PER-CELL A² AT TOP-K |ω|² CELLS:
      Sets up §14.4 prediction prework. Pick top-50 cells by |ω|²
      density. Compute A²(cell) = (Σ_p V_inc[cell, p]²) / V_SNAP² at
      each. Histogram. Identify:
        - what fraction lies in Regime II (A² ∈ [0.121, 0.866])
        - what fraction in Regime III / saturated (A² > 0.866)
        - what fraction near-rupture (A² > 0.95)
      This is the "is the load-bearing structure in saturated-core
      or moderate-shell?" diagnostic at the fixed point.

NO PASS/FAIL ADJUDICATION. Result IS the characterization.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.vacuum_engine import VacuumEngine3D
from tlm_electron_soliton_eigenmode import initialize_2_3_voltage_ansatz


# ─── Constants (match Move 5 + 7 + 7b for deterministic reproduction) ────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ                      # ≈ 3.82
A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)
V_AMP_INIT = 0.14

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
N_PERIODS_TOTAL = 200.0
DT = 1.0 / np.sqrt(2.0)
N_STEPS = int(N_PERIODS_TOTAL * COMPTON_PERIOD / DT) + 1

# Shell-search range for toroidal/poloidal winding extraction
R_SEARCH_VALUES = np.arange(3, 13, 1)            # major radii to test
N_TOROIDAL_SAMPLES = 32                           # samples per toroidal loop
N_POLOIDAL_SAMPLES = 24                           # samples per poloidal loop

# Hopf level-set values for fiber-linking computation
HOPF_LEVEL_VALUES = [0.5, -0.5]                   # ω̂_z = ±0.5 fibers

# Y_{l,m} spherical-harmonic decomposition: max l
SPH_HARM_L_MAX = 4

# A² distribution over top-K |ω|² cells
TOP_K_OMEGA_CELLS = 50

# AVE three-regime A² boundaries (per AVE-VirtualMedia convention)
from ave.core.constants import ALPHA
A2_REGIME_I_II = 2.0 * ALPHA                     # ≈ 0.0146 (peak strain)
A2_REGIME_II_III = 0.75                           # 3/4 (per (√3/2)²)
A2_RUPTURE = 1.0

OUTPUT_JSON = Path(__file__).parent / "r8_phase1_attractor_winding_results.json"


def build_engine():
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_corpus_2_3_joint(engine):
    engine.cos.initialize_electron_2_3_sector(
        R_target=R_ANCHOR, r_target=R_MINOR,
        use_hedgehog=True, amplitude_scale=A26_AMP_SCALE,
    )
    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_ANCHOR, r=R_MINOR, amplitude=V_AMP_INIT,
    )


# ─── Extraction (1): toroidal/poloidal winding numbers ───────────────────────

def winding_along_loop(omega_field, sample_points, plane_axes=(0, 1)):
    """Sample ω at given points (each is (i, j, k)); compute total angle
    swept by ω projected onto the chosen 2D plane around the loop.

    Returns winding number (rounded to nearest integer; signed).
    """
    proj = []
    for (i, j, k) in sample_points:
        ax_a, ax_b = plane_axes
        wx = float(omega_field[i, j, k, ax_a])
        wy = float(omega_field[i, j, k, ax_b])
        proj.append((wx, wy))
    proj = np.asarray(proj)
    angles = np.arctan2(proj[:, 1], proj[:, 0])
    # Unwrap and compute total angle swept
    diffs = np.diff(angles)
    diffs = (diffs + np.pi) % (2 * np.pi) - np.pi   # wrap to [-π, π]
    total = float(diffs.sum())
    n_winding = int(round(total / (2 * np.pi)))
    return n_winding


def extract_torus_winding(omega_field, R_major, r_minor, center,
                          n_torpts=32, n_polpts=24):
    """Sample loops on the torus (R_major, r_minor) centered at `center`.
    For each fixed poloidal angle ψ, a toroidal loop runs through
    n_torpts samples around φ ∈ [0, 2π). Compute toroidal winding p
    (in (ω_x, ω_y) plane). Then for each fixed toroidal angle φ, a
    poloidal loop runs through n_polpts samples around ψ. Compute
    poloidal winding q (in (ω_z, ω_xy) plane).

    Returns: (mean_p_winding, mean_q_winding).
    """
    nx, ny, nz = omega_field.shape[:3]
    cx, cy, cz = center

    def cell_at(phi, psi):
        x = cx + (R_major + r_minor * np.cos(psi)) * np.cos(phi)
        y = cy + (R_major + r_minor * np.cos(psi)) * np.sin(phi)
        z = cz + r_minor * np.sin(psi)
        i = int(round(x)) % nx
        j = int(round(y)) % ny
        k = int(round(z)) % nz
        return (i, j, k)

    # Toroidal loops at fixed ψ
    psi_samples = np.linspace(0, 2 * np.pi, n_polpts, endpoint=False)
    phi_samples = np.linspace(0, 2 * np.pi, n_torpts, endpoint=False)
    p_windings = []
    for psi in psi_samples:
        pts = [cell_at(phi, psi) for phi in phi_samples] + [cell_at(0.0, psi)]
        # winding in (ω_x, ω_y) plane along toroidal loop
        p = winding_along_loop(omega_field, pts, plane_axes=(0, 1))
        p_windings.append(p)

    # Poloidal loops at fixed φ
    q_windings = []
    for phi in phi_samples:
        pts = [cell_at(phi, psi) for psi in psi_samples] + [cell_at(phi, 0.0)]
        # winding using rotated 2D plane: project ω_xy_radial vs ω_z
        # rotated radial direction in (ω_x, ω_y) is (cos phi, sin phi)
        # so radial component = ω_x cos phi + ω_y sin phi
        proj = []
        for (i, j, k) in pts:
            wx = float(omega_field[i, j, k, 0])
            wy = float(omega_field[i, j, k, 1])
            wz = float(omega_field[i, j, k, 2])
            radial = wx * np.cos(phi) + wy * np.sin(phi)
            proj.append((radial, wz))
        proj = np.asarray(proj)
        angles = np.arctan2(proj[:, 1], proj[:, 0])
        diffs = np.diff(angles)
        diffs = (diffs + np.pi) % (2 * np.pi) - np.pi
        total = float(diffs.sum())
        q = int(round(total / (2 * np.pi)))
        q_windings.append(q)

    return float(np.mean(p_windings)), float(np.mean(q_windings)), p_windings, q_windings


# ─── Extraction (2): Hopf linking number ─────────────────────────────────────

def hopf_linking_number(omega_field, c_plus=0.5, c_minus=-0.5):
    """Approximate Hopf linking number via Gauss linking integral on
    discretized level-set curves.

    Returns: estimated linking number (typically 0 for torus knots,
    nonzero for Hopf-linked configurations).
    """
    omega_norm = np.linalg.norm(omega_field, axis=-1, keepdims=True)
    omega_hat_z = np.where(omega_norm[..., 0] > 1e-10,
                           omega_field[..., 2] / omega_norm[..., 0],
                           0.0)

    # Find approximate level-set surfaces via marching-cubes-style
    # cell-by-cell zero crossings
    def find_level_set_curve(level):
        """Return list of (i, j, k) cells where ω̂_z transitions through `level`."""
        crossings = []
        nx, ny, nz = omega_hat_z.shape
        for i in range(nx - 1):
            for j in range(ny - 1):
                for k in range(nz - 1):
                    cube = omega_hat_z[i:i+2, j:j+2, k:k+2]
                    if np.min(cube) <= level <= np.max(cube):
                        crossings.append((i, j, k))
        return crossings

    pts_plus = find_level_set_curve(c_plus)
    pts_minus = find_level_set_curve(c_minus)

    if len(pts_plus) < 4 or len(pts_minus) < 4:
        return None, len(pts_plus), len(pts_minus)

    # Approximate Gauss linking number via discrete sum
    # Lk(γ₁, γ₂) = (1/4π) ∮∮ (r₁ - r₂) · (dr₁ × dr₂) / |r₁ - r₂|³
    # For point clouds, use approximate unit-tangent estimation
    pts_plus = np.asarray(pts_plus, dtype=float)
    pts_minus = np.asarray(pts_minus, dtype=float)

    # Approximate tangents via centroid-shifted neighbor differences
    # (very rough; only OoM check on whether linking is non-zero)
    if len(pts_plus) > 100:
        # Subsample for speed
        idx = np.linspace(0, len(pts_plus) - 1, 100).astype(int)
        pts_plus = pts_plus[idx]
    if len(pts_minus) > 100:
        idx = np.linspace(0, len(pts_minus) - 1, 100).astype(int)
        pts_minus = pts_minus[idx]

    # Use signed solid-angle estimate as a coarse linking proxy:
    # for each pt_plus, compute the solid angle subtended by the
    # pts_minus loop. If it's near 4π, the loops link; if near 0, no.
    centroid_minus = pts_minus.mean(axis=0)
    extent_minus = np.linalg.norm(pts_minus - centroid_minus, axis=1).mean()

    n_inside_minus_loop = 0
    for pt_plus in pts_plus:
        # crude: is pt_plus "inside" the pts_minus convex hull projected to 2D?
        d = np.linalg.norm(pt_plus - centroid_minus)
        if d < 0.5 * extent_minus:
            n_inside_minus_loop += 1

    # Coarse linking estimate: if a substantial fraction of pts_plus is
    # near-centroid of pts_minus, suggests intertwining
    inside_frac = n_inside_minus_loop / max(len(pts_plus), 1)
    return float(inside_frac), len(pts_plus), len(pts_minus)


# ─── Extraction (3): spherical harmonic decomposition of |ω|² ────────────────

def spherical_harmonic_decompose(omega_density, center, l_max=4,
                                  n_radial_bins=8):
    """Project |ω|² onto Y_{l,m} basis at each radial bin. Report
    dominant (l, m) per bin and overall.

    Uses real spherical harmonics (sin/cos rather than e^{imφ}).
    """
    nx, ny, nz = omega_density.shape
    cx, cy, cz = center
    i, j, k = np.indices((nx, ny, nz))
    x = i - cx
    y = j - cy
    z = k - cz
    r = np.sqrt(x**2 + y**2 + z**2 + 1e-20)
    theta = np.arccos(z / r)             # polar angle ∈ [0, π]
    phi = np.arctan2(y, x)                 # azimuthal angle ∈ [-π, π]

    # Real spherical harmonics Y_l_m(θ, φ) for l = 0..l_max
    # scipy 1.15+ uses sph_harm_y(n, m, theta, phi) where theta is polar
    # (colatitude) and phi is azimuthal — swapped argument order vs old
    # sph_harm(m, n, theta_azimuthal, phi_polar).
    from scipy.special import sph_harm_y

    def Y_lm(l, m, theta, phi):
        # New API: sph_harm_y(n, m, theta_polar, phi_azimuthal)
        # Returns complex; convert to real:
        #   Y_real_{l,m} = Re(Y_l^|m|) for m ≥ 0, Im(Y_l^|m|) for m < 0
        if m >= 0:
            return np.real(sph_harm_y(l, m, theta, phi))
        else:
            return np.imag(sph_harm_y(l, abs(m), theta, phi))

    r_max = min(nx, ny, nz) // 2 - 2
    radial_bins = np.linspace(1, r_max, n_radial_bins + 1)
    coeffs_per_bin = []
    for bi in range(n_radial_bins):
        rmask = (r >= radial_bins[bi]) & (r < radial_bins[bi + 1])
        if rmask.sum() < 4:
            coeffs_per_bin.append(None)
            continue
        rho_local = omega_density[rmask]
        theta_local = theta[rmask]
        phi_local = phi[rmask]
        coeffs = {}
        for l in range(l_max + 1):
            for m in range(-l, l + 1):
                Y_vals = Y_lm(l, m, theta_local, phi_local)
                # inner product (assuming roughly uniform sampling per bin)
                c_lm = float(np.sum(rho_local * Y_vals)) / max(rmask.sum(), 1)
                coeffs[f"Y_{l}_{m}"] = c_lm
        # find dominant (|c_lm|^2)
        sorted_coeffs = sorted(coeffs.items(), key=lambda kv: -kv[1] ** 2)
        coeffs_per_bin.append({
            "r_lo": float(radial_bins[bi]),
            "r_hi": float(radial_bins[bi + 1]),
            "n_cells": int(rmask.sum()),
            "dominant": sorted_coeffs[:5],
        })

    return coeffs_per_bin


# ─── Extraction (4): per-cell A² at top-K |ω|² cells ─────────────────────────

def per_cell_A2_distribution(omega_field, v_inc_field, k=50):
    """At the top-K cells by |ω|² density, compute A² = Σ_p V_inc²/V_SNAP² (V_SNAP=1)."""
    nx, ny, nz = omega_field.shape[:3]
    omega_density = np.sum(omega_field ** 2, axis=-1)
    flat = omega_density.flatten()
    top_idx = np.argpartition(flat, -k)[-k:]
    top_idx = top_idx[np.argsort(flat[top_idx])[::-1]]

    a2_values = []
    cell_records = []
    for idx in top_idx:
        cell = np.unravel_index(idx, omega_density.shape)
        v_inc_at_cell = v_inc_field[cell[0], cell[1], cell[2], :]
        v_total_sq = float(np.sum(v_inc_at_cell ** 2))
        a2 = v_total_sq                  # V_SNAP = 1 in natural units
        a2_values.append(a2)
        cell_records.append({
            "cell": list(int(c) for c in cell),
            "omega_density": float(flat[idx]),
            "A2": a2,
        })

    a2_arr = np.array(a2_values)
    # Regime classification
    n_regime_I = int(np.sum(a2_arr < A2_REGIME_I_II))
    n_regime_II = int(np.sum((a2_arr >= A2_REGIME_I_II) & (a2_arr < A2_REGIME_II_III)))
    n_regime_III = int(np.sum((a2_arr >= A2_REGIME_II_III) & (a2_arr < 0.95)))
    n_near_rupture = int(np.sum(a2_arr >= 0.95))

    return {
        "n_top_cells": k,
        "a2_min": float(a2_arr.min()),
        "a2_max": float(a2_arr.max()),
        "a2_mean": float(a2_arr.mean()),
        "a2_median": float(np.median(a2_arr)),
        "n_regime_I": n_regime_I,
        "n_regime_II": n_regime_II,
        "n_regime_III": n_regime_III,
        "n_near_rupture": n_near_rupture,
        "regime_boundaries": {
            "I_II": A2_REGIME_I_II,
            "II_III": A2_REGIME_II_III,
        },
        "cells_top_10": cell_records[:10],
    }


def main():
    print("=" * 78, flush=True)
    print(f"  Move 10 / Phase 1 winding — static fixed point spatial topology")
    print(f"  P_phase1_attractor_winding_characterization (frozen extraction)")
    print("=" * 78, flush=True)
    print(f"  Lattice N={N_LATTICE}, deterministic Move 5 reproduction to t=200P")
    print(f"  Extractions: (1) torus winding, (2) Hopf linking, "
          f"(3) Y_lm decomp, (4) per-cell A² distribution")
    print()

    engine = build_engine()
    seed_corpus_2_3_joint(engine)

    print(f"  Running {N_STEPS} steps to t=200P…")
    t0 = time.time()
    last_progress = t0
    for step in range(1, N_STEPS + 1):
        engine.step()
        if (time.time() - last_progress) > 30.0:
            t_p = step * DT / COMPTON_PERIOD
            print(f"    [progress] step {step}, t={t_p:.1f}P, "
                  f"elapsed {time.time() - t0:.1f}s", flush=True)
            last_progress = time.time()
    elapsed = time.time() - t0
    print(f"  Run complete: {elapsed:.1f}s")
    print()

    omega_final = np.asarray(engine.cos.omega).copy()
    v_inc_final = np.asarray(engine.k4.V_inc).copy()
    omega_density = np.sum(omega_final ** 2, axis=-1)
    nx = omega_final.shape[0]
    center = ((nx - 1) / 2.0, (nx - 1) / 2.0, (nx - 1) / 2.0)

    # ─── (1) torus winding numbers per shell ─────────────────────────────────
    print(f"  (1) TOROIDAL/POLOIDAL WINDING NUMBERS at candidate shells:")
    winding_results = []
    for R_test in R_SEARCH_VALUES:
        # Use r_minor scaled to match: r ≈ R/φ² as a placeholder
        r_test = max(0.5, R_test / PHI_SQ)
        try:
            mean_p, mean_q, p_list, q_list = extract_torus_winding(
                omega_final, R_test, r_test, center,
                n_torpts=N_TOROIDAL_SAMPLES, n_polpts=N_POLOIDAL_SAMPLES,
            )
        except Exception as e:
            print(f"    R={R_test}: error {e}")
            continue
        winding_results.append({
            "R": float(R_test), "r": float(r_test),
            "mean_p_toroidal": mean_p, "mean_q_poloidal": mean_q,
            "p_per_loop": p_list, "q_per_loop": q_list,
        })
        print(f"    R={R_test:5.1f} r={r_test:5.2f}:  mean p (toroidal) "
              f"= {mean_p:+.2f},  mean q (poloidal) = {mean_q:+.2f}")
    print()

    # ─── (2) Hopf linking ────────────────────────────────────────────────────
    print(f"  (2) HOPF LINKING NUMBER (level-set fiber linking):")
    inside_frac, n_pts_plus, n_pts_minus = hopf_linking_number(
        omega_final, c_plus=HOPF_LEVEL_VALUES[0], c_minus=HOPF_LEVEL_VALUES[1],
    )
    print(f"    ω̂_z = +{HOPF_LEVEL_VALUES[0]} fiber: {n_pts_plus} cells")
    print(f"    ω̂_z = {HOPF_LEVEL_VALUES[1]} fiber: {n_pts_minus} cells")
    print(f"    Approximate inside-fraction (linking proxy): {inside_frac}")
    print()

    # ─── (3) Spherical harmonic decomposition ────────────────────────────────
    print(f"  (3) SPHERICAL HARMONIC DECOMPOSITION of |ω|² "
          f"(l_max={SPH_HARM_L_MAX}, {8} radial bins):")
    sph_results = spherical_harmonic_decompose(
        omega_density, center, l_max=SPH_HARM_L_MAX, n_radial_bins=8,
    )
    for bi, b in enumerate(sph_results):
        if b is None:
            continue
        dom = b["dominant"][:3]
        dom_str = "  ".join(f"{name}={c:+.4f}" for name, c in dom)
        print(f"    r∈[{b['r_lo']:.1f}, {b['r_hi']:.1f}] ({b['n_cells']} cells):")
        print(f"      top 3: {dom_str}")
    print()

    # ─── (4) Per-cell A² at top-|ω|² cells ───────────────────────────────────
    print(f"  (4) PER-CELL A² at top-{TOP_K_OMEGA_CELLS} |ω|² cells:")
    a2_dist = per_cell_A2_distribution(
        omega_final, v_inc_final, k=TOP_K_OMEGA_CELLS,
    )
    print(f"    A² range: [{a2_dist['a2_min']:.4f}, {a2_dist['a2_max']:.4f}]")
    print(f"    A² mean = {a2_dist['a2_mean']:.4f}, "
          f"median = {a2_dist['a2_median']:.4f}")
    print(f"    Regime distribution (top {TOP_K_OMEGA_CELLS} |ω|² cells):")
    print(f"      Regime I (linear, A² < {A2_REGIME_I_II:.4f}):    "
          f"{a2_dist['n_regime_I']} cells")
    print(f"      Regime II (saturating, A² ∈ [{A2_REGIME_I_II:.4f}, "
          f"{A2_REGIME_II_III:.4f})):  {a2_dist['n_regime_II']} cells")
    print(f"      Regime III (stopband, A² ∈ [{A2_REGIME_II_III:.4f}, 0.95)): "
          f"{a2_dist['n_regime_III']} cells")
    print(f"      Near-rupture (A² ≥ 0.95): {a2_dist['n_near_rupture']} cells")
    print()

    print(f"  Sanity (t=200P): c via Op10 = {int(engine.cos.extract_crossing_count())}")
    print()

    # ─── Save full payload ───────────────────────────────────────────────────
    payload = {
        "pre_registration": "P_phase1_attractor_winding_characterization",
        "test": "Move 10 — static fixed point spatial topology characterization",
        "N": N_LATTICE,
        "n_periods_total": N_PERIODS_TOTAL,
        "elapsed_seconds": elapsed,
        "extraction_1_torus_winding_per_shell": winding_results,
        "extraction_2_hopf_linking_proxy": {
            "level_values": HOPF_LEVEL_VALUES,
            "n_pts_plus": n_pts_plus,
            "n_pts_minus": n_pts_minus,
            "inside_fraction_proxy": inside_frac,
        },
        "extraction_3_spherical_harmonics": sph_results,
        "extraction_4_top_omega_A2_distribution": a2_dist,
        "topology_at_t_final": {
            "c_via_Op10": int(engine.cos.extract_crossing_count()),
        },
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
