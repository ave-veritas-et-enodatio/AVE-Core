"""
Gaia DR3 FLOOR Test — Stratified |v_CMB| by Toomre-diagram velocity cuts.

SCOPE NOTE (2026-05-17 late evening — floor interpretation test):

Tests the FLOOR interpretation of the substrate-equilibrium velocity prediction
αc/(2π) ≈ 348.2 km/s by stratifying the existing 29,466-star Gaia DR3 sample
by Toomre-diagram |v_LSR| velocity cuts (which sort by dynamical class).

Pre-registered outcomes (see [`research/2026-05-17_substrate_equilibrium_velocity_FLOOR_test_prereg.md`]):
  - OUTCOME I-floor-confirmed: halo |v_CMB| median within 10 km/s of 348
    (floor) + monotone-decreasing trend from thin-disk → halo. STRONG positive
    for floor interpretation.
  - OUTCOME II-floor-partial: halo median between 350-365 km/s; qualitative
    positive trend without reaching floor.
  - OUTCOME III-flat: all populations cluster at ~375 km/s; A-center
    interpretation supported.
  - OUTCOME IV-mixed: halo has random kinematics with no preferred velocity;
    substrate-equilibrium interpretation falsified at halo scale.

INPUTS (empirical, honestly labeled):
  - /tmp/gaia_nearby_gk.csv (29,466 stars, same as prior directional test)
  - Sun's CMB velocity 370 km/s toward (l,b)=(264°,48°) — Planck 2018 empirical
  - Sun's LSR motion (Schönrich+ 2010): (U,V,W) = (11.1, 12.24, 7.25) km/s — empirical
  - IAU equatorial-to-galactic rotation matrix — standard

DERIVED (forward computation, no fit):
  - αc/(2π) = 348.18 km/s substrate-equilibrium floor (canonical)
  - Per-star |v_CMB| (forward calc)
  - Per-star |v_LSR| (forward calc, used for Toomre stratification)
  - Population statistics in 4 Toomre bins

NO FIT PARAMETERS. Distribution either supports floor interpretation
(monotone-decreasing trend toward 348 as |v_LSR| increases) or it doesn't.

Per ave-driver-script-honesty discipline.
"""

import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from ave.core.constants import ALPHA, C_0


V_SUBSTRATE_KMS = ALPHA * C_0 / (2 * np.pi) / 1000.0

# Sun's CMB velocity (Planck 2018)
SUN_CMB_MAG_KMS = 370.0
_l, _b = np.radians(264.0), np.radians(48.0)
SUN_CMB_VEC_GAL = SUN_CMB_MAG_KMS * np.array([
    np.cos(_b) * np.cos(_l),
    np.cos(_b) * np.sin(_l),
    np.sin(_b),
])

# Sun's LSR motion (Schönrich+ 2010): (U,V,W) = (11.1, 12.24, 7.25) km/s
SUN_LSR_UVW = np.array([11.1, 12.24, 7.25])

# IAU J2000 equatorial → galactic rotation matrix
R_EQ_TO_GAL = np.array([
    [-0.054876, -0.873437, -0.483835],
    [+0.494109, -0.444830, +0.746982],
    [-0.867666, -0.198076, +0.455984],
])


def parse_gaia_csv(path: Path) -> list[dict]:
    stars = []
    with path.open("r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                stars.append({k: float(row[k]) for k in [
                    "ra", "dec", "parallax", "pmra", "pmdec", "radial_velocity",
                ]})
            except (ValueError, KeyError):
                continue
    return stars


def heliocentric_velocity_galactic(s: dict) -> np.ndarray:
    ra, dec = np.radians(s["ra"]), np.radians(s["dec"])
    d_pc = 1000.0 / s["parallax"]
    v_alpha = 4.740470463e-3 * s["pmra"] * d_pc
    v_delta = 4.740470463e-3 * s["pmdec"] * d_pc
    v_r = s["radial_velocity"]
    cra, sra, cde, sde = np.cos(ra), np.sin(ra), np.cos(dec), np.sin(dec)
    v_eq = np.array([
        v_r * cde * cra - v_alpha * sra - v_delta * sde * cra,
        v_r * cde * sra + v_alpha * cra - v_delta * sde * sra,
        v_r * sde + v_delta * cde,
    ])
    return R_EQ_TO_GAL @ v_eq


def main() -> None:
    print("=" * 70)
    print("  GAIA DR3 FLOOR TEST — Toomre-stratified |v_CMB| distributions")
    print("=" * 70)
    print()
    print(f"AVE prediction: substrate-equilibrium FLOOR = αc/(2π) = {V_SUBSTRATE_KMS:.2f} km/s")
    print()

    csv_path = Path("/tmp/gaia_nearby_gk.csv")
    stars = parse_gaia_csv(csv_path)
    print(f"Loaded {len(stars)} stars")

    v_cmb_list = []
    v_lsr_list = []
    for s in stars:
        v_helio = heliocentric_velocity_galactic(s)
        v_cmb = v_helio + SUN_CMB_VEC_GAL
        v_lsr = v_helio + SUN_LSR_UVW  # star's velocity wrt LSR
        v_cmb_list.append(np.linalg.norm(v_cmb))
        v_lsr_list.append(np.linalg.norm(v_lsr))
    v_cmb = np.array(v_cmb_list)
    v_lsr = np.array(v_lsr_list)

    # Drop |v_CMB| > 1500 km/s outliers
    mask_ok = v_cmb < 1500
    v_cmb = v_cmb[mask_ok]
    v_lsr = v_lsr[mask_ok]
    print(f"After |v_CMB|<1500 cut: {len(v_cmb)} stars")
    print()

    # Toomre-diagram velocity bins
    bins = [
        ("Thin disk  (|v_LSR|<30)",       0,     30),
        ("Thick disk (30<|v_LSR|<70)",    30,    70),
        ("Thick disk (70<|v_LSR|<100)",   70,    100),
        ("Halo       (100<|v_LSR|<200)",  100,   200),
        ("Extreme halo (|v_LSR|>200)",    200,   1e9),
    ]

    print(f"{'Bin':35s} {'N':>6s} {'median |v_CMB|':>15s} {'mean':>8s} {'σ':>8s} {'Δ vs floor':>12s}")
    print("-" * 90)

    bin_results = []
    for label, lo, hi in bins:
        mask = (v_lsr >= lo) & (v_lsr < hi)
        if mask.sum() < 5:
            print(f"{label:35s} N=0 (insufficient)")
            continue
        v_cmb_bin = v_cmb[mask]
        median = float(np.median(v_cmb_bin))
        mean = float(np.mean(v_cmb_bin))
        std = float(np.std(v_cmb_bin))
        delta_floor = median - V_SUBSTRATE_KMS
        print(f"{label:35s} {mask.sum():>6d} {median:>13.2f}   {mean:>8.2f} {std:>8.2f} {delta_floor:>+10.2f}")
        bin_results.append((label, lo, hi, mask.sum(), median, mean, std, delta_floor))

    print()

    # Trend analysis
    print("Trend analysis (median |v_CMB| vs Toomre bin):")
    medians = [r[4] for r in bin_results]
    if len(medians) >= 3:
        # Check monotone-decreasing trend (floor interpretation)
        diffs = np.diff(medians)
        if all(d <= 0 for d in diffs):
            trend = "MONOTONE-DECREASING (floor interpretation supported)"
        elif all(d >= 0 for d in diffs):
            trend = "MONOTONE-INCREASING (floor interpretation FALSIFIED)"
        elif abs(max(medians) - min(medians)) < 5:
            trend = "FLAT within ±5 km/s (A-center supported; floor falsified)"
        else:
            trend = "NON-MONOTONE (mixed signal)"
        print(f"  {trend}")
    print()

    # Outcome categorization
    halo_bins = [r for r in bin_results if r[1] >= 100]
    if halo_bins:
        halo_median = np.median([r[4] for r in halo_bins])
        print(f"Halo aggregate median: {halo_median:.2f} km/s")
        delta = halo_median - V_SUBSTRATE_KMS
        if abs(delta) < 10:
            outcome = "I-floor-confirmed (halo within ±10 km/s of floor; STRONG positive)"
        elif delta < 0:
            outcome = "II-floor-undershoots (halo BELOW floor, may need fluctuation analysis)"
        elif delta < 20:
            outcome = "II-floor-partial (halo within 20 km/s of floor, qualitative positive)"
        elif delta < 30:
            outcome = "III-soft (halo 20-30 km/s above floor; trend partial)"
        else:
            outcome = "III-flat (halo not significantly closer to floor than thin-disk)"
        print(f"\nPRE-REGISTERED OUTCOME: {outcome}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: median |v_CMB| vs Toomre bin
    bin_centers = [(r[1] + r[2]) / 2 if r[2] < 1e8 else r[1] + 50 for r in bin_results]
    bin_medians = [r[4] for r in bin_results]
    bin_stds = [r[6] for r in bin_results]
    bin_ns = [r[3] for r in bin_results]
    axes[0].errorbar(bin_centers, bin_medians, yerr=bin_stds, fmt="o-", markersize=10,
                     capsize=5, color="steelblue", linewidth=2)
    axes[0].axhline(V_SUBSTRATE_KMS, color="red", linestyle="--", linewidth=2,
                    label=f"αc/(2π) FLOOR = {V_SUBSTRATE_KMS:.1f} km/s")
    axes[0].axhline(370, color="green", linestyle=":", linewidth=2,
                    label=f"Sun (370 km/s)")
    for x, y, n in zip(bin_centers, bin_medians, bin_ns):
        axes[0].annotate(f"N={n}", (x, y), textcoords="offset points",
                         xytext=(8, 6), fontsize=9)
    axes[0].set_xlabel("Toomre |v_LSR| bin center (km/s)", fontsize=11)
    axes[0].set_ylabel("Median |v_CMB| (km/s) ± σ", fontsize=11)
    axes[0].set_title("Floor test: |v_CMB| stratified by Toomre dynamical class")
    axes[0].legend(fontsize=10)
    axes[0].grid(alpha=0.3)

    # Plot 2: histograms by bin
    colors = plt.cm.viridis(np.linspace(0, 0.9, len(bin_results)))
    for (label, lo, hi, n, med, mean, std, _), color in zip(bin_results, colors):
        bin_mask = (v_lsr >= lo) & (v_lsr < hi)
        v_cmb_bin = v_cmb[bin_mask]
        axes[1].hist(v_cmb_bin, bins=60, range=(200, 700), histtype="step",
                     color=color, linewidth=2,
                     label=f"{label} (N={n}, median={med:.0f})", density=True)
    axes[1].axvline(V_SUBSTRATE_KMS, color="red", linestyle="--", linewidth=2,
                    label=f"αc/(2π) = {V_SUBSTRATE_KMS:.1f}")
    axes[1].set_xlabel("|v_CMB| (km/s)", fontsize=11)
    axes[1].set_ylabel("Density", fontsize=11)
    axes[1].set_title("Histograms by Toomre bin (normalized)")
    axes[1].legend(fontsize=8, loc="upper right")
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    out_path = Path(__file__).parent.parent.parent / "assets" / "sim_outputs" / "gaia_floor_test.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"\nSaved floor test plot to {out_path}")


if __name__ == "__main__":
    main()
