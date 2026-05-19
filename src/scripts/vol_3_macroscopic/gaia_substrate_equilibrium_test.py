"""
Gaia DR3 Substrate-Equilibrium Velocity Test (forward-prediction, zero-parameter).

SCOPE NOTE (2026-05-17 evening — substrate-equilibrium velocity test):
Tests the AVE-distinct prediction `v_substrate = αc/(2π) ≈ 348.2 km/s` (the
electron's Schwinger anomalous-moment substrate velocity, derived in
`research/2026-05-17_C14-DAMA_amplitude_result.md`) against the CMB-frame
velocity distribution of nearby thin-disk G/K dwarfs from Gaia DR3.

INPUTS (all empirical, honestly labeled):
  - Gaia DR3 catalog query: nearby G/K dwarfs with full 6D kinematics
    (parallax > 10 mas, has radial_velocity, bp_rp in [0.6, 1.2],
    quality cuts). N = 29,466 stars at 2026-05-17.
  - Sun's CMB velocity: 370 km/s toward (l, b) = (264°, 48°) (Planck 2018,
    Hinshaw 2009) — empirical input, NOT derived.
  - IAU J2000 equatorial-to-galactic rotation matrix (standard).

DERIVED (axiom-canonical, no fit):
  - αc/(2π) = 348.18 km/s (pure α + c, both canonical AVE constants).
  - Per-star CMB-frame velocity vector via standard Gaia astrometry transform
    + vector addition with Sun's CMB velocity.

WHAT THIS SCRIPT DOES NOT DO:
  - No fit parameters. AVE prediction is forward, not inverse.
  - No DM-halo fitting per star (parallel SPARC pattern: zero-parameter
    AVE prediction vs observed distribution).
  - No tuning of αc/(2π) — it's the canonical Schwinger anomalous-moment
    velocity scale, fixed by α + c.

OUTCOMES (pre-registered, see GAIA prereg doc):
  A — sharp cluster at 348 ± 20 km/s: AVE positive prediction validated
  B — broad cluster at 348 ± 50 km/s: validated qualitatively
  C — ambiguous multi-peak distribution: framework refinement needed
  D — cluster outside [200, 500] km/s: AVE Sun-velocity prediction falsified

Outcome categorization is purely on the data; this script does not adjust
the prediction to match.

Per ave-driver-script-honesty skill: this script computes forward predictions
from canonical AVE constants (α, c) against empirical Gaia data. The energy
scale α m_e c² = 3.728 keV (DAMA-window) and velocity scale αc/(2π) = 348 km/s
(this test) are zero-parameter substrate-native quantities derived from the
canonical Schwinger anomalous-moment chain at `simulate_g2.py`.
"""

import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from ave.core.constants import ALPHA, C_0


# AVE prediction (zero-parameter, canonical)
V_SUBSTRATE_MS = ALPHA * C_0 / (2 * np.pi)
V_SUBSTRATE_KMS = V_SUBSTRATE_MS / 1000.0


# Sun's CMB velocity (Planck 2018, Hinshaw 2009): 370 km/s toward (l,b)=(264°, 48°)
# Convert to galactic Cartesian (x toward GC, y toward galactic rotation, z toward N gal pole)
SUN_CMB_MAG_KMS = 370.0
SUN_CMB_L_DEG = 264.0
SUN_CMB_B_DEG = 48.0

_l = np.radians(SUN_CMB_L_DEG)
_b = np.radians(SUN_CMB_B_DEG)
SUN_CMB_VEC_GAL = np.array([
    SUN_CMB_MAG_KMS * np.cos(_b) * np.cos(_l),
    SUN_CMB_MAG_KMS * np.cos(_b) * np.sin(_l),
    SUN_CMB_MAG_KMS * np.sin(_b),
])


# IAU J2000 equatorial-to-galactic rotation matrix (standard)
# Transforms an equatorial-Cartesian vector to galactic-Cartesian.
R_EQ_TO_GAL = np.array([
    [-0.054876, -0.873437, -0.483835],
    [+0.494109, -0.444830, +0.746982],
    [-0.867666, -0.198076, +0.455984],
])


def parse_gaia_csv(path: Path) -> list[dict]:
    """Parse Gaia DR3 TAP CSV output. Returns list of dicts with parsed fields."""
    stars = []
    with path.open("r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                stars.append({
                    "ra": float(row["ra"]),
                    "dec": float(row["dec"]),
                    "parallax": float(row["parallax"]),
                    "pmra": float(row["pmra"]),
                    "pmdec": float(row["pmdec"]),
                    "radial_velocity": float(row["radial_velocity"]),
                    "bp_rp": float(row["bp_rp"]),
                    "phot_g_mean_mag": float(row["phot_g_mean_mag"]),
                })
            except (ValueError, KeyError):
                continue
    return stars


def heliocentric_velocity_galactic(star: dict) -> np.ndarray:
    """
    Compute star's heliocentric velocity vector in galactic Cartesian (km/s).

    Inputs (per star):
      - ra, dec [deg], parallax [mas]
      - pmra, pmdec [mas/yr]
      - radial_velocity [km/s]

    Returns: 3-vector (vx, vy, vz) in galactic Cartesian, km/s.
    """
    ra = np.radians(star["ra"])
    dec = np.radians(star["dec"])
    parallax_mas = star["parallax"]
    pmra = star["pmra"]  # mas/yr (cos(dec)-corrected per Gaia convention)
    pmdec = star["pmdec"]  # mas/yr
    v_r = star["radial_velocity"]  # km/s

    # Distance in pc
    d_pc = 1000.0 / parallax_mas

    # Tangential velocities (km/s) from proper motion + distance
    # Conversion: 4.740470 km/s = (1 mas/yr) × (1 kpc); for d in pc, use 4.74e-3
    v_alpha = 4.740470463 * pmra * d_pc / 1000.0  # km/s in +RA direction
    v_delta = 4.740470463 * pmdec * d_pc / 1000.0  # km/s in +Dec direction

    # Heliocentric velocity in equatorial Cartesian
    # Convention: x toward (RA=0, Dec=0); y toward (RA=90°, Dec=0); z toward Dec=+90°
    cos_ra, sin_ra = np.cos(ra), np.sin(ra)
    cos_dec, sin_dec = np.cos(dec), np.sin(dec)

    vx_eq = v_r * cos_dec * cos_ra - v_alpha * sin_ra - v_delta * sin_dec * cos_ra
    vy_eq = v_r * cos_dec * sin_ra + v_alpha * cos_ra - v_delta * sin_dec * sin_ra
    vz_eq = v_r * sin_dec + v_delta * cos_dec

    v_eq = np.array([vx_eq, vy_eq, vz_eq])

    # Rotate to galactic Cartesian
    v_gal = R_EQ_TO_GAL @ v_eq
    return v_gal


def cmb_frame_velocity_kms(star: dict) -> float:
    """Return magnitude of star's velocity through CMB rest frame (km/s)."""
    v_helio_gal = heliocentric_velocity_galactic(star)
    v_cmb = v_helio_gal + SUN_CMB_VEC_GAL
    return float(np.linalg.norm(v_cmb))


def main() -> None:
    print("=" * 70)
    print("  GAIA DR3 SUBSTRATE-EQUILIBRIUM VELOCITY TEST")
    print("  (forward-prediction, zero-parameter)")
    print("=" * 70)
    print()
    print(f"AVE prediction: v_substrate = αc/(2π) = {V_SUBSTRATE_KMS:.3f} km/s")
    print(f"               (pure α + c; canonical AVE substrate equilibrium velocity)")
    print()
    print(f"Sun's CMB velocity (Planck 2018 input): "
          f"{SUN_CMB_MAG_KMS} km/s toward (l,b)=({SUN_CMB_L_DEG}°, {SUN_CMB_B_DEG}°)")
    print(f"   In galactic Cartesian: ({SUN_CMB_VEC_GAL[0]:.1f}, "
          f"{SUN_CMB_VEC_GAL[1]:.1f}, {SUN_CMB_VEC_GAL[2]:.1f}) km/s")
    print()

    # Load Gaia data
    csv_path = Path("/tmp/gaia_nearby_gk.csv")
    if not csv_path.exists():
        print(f"ERROR: {csv_path} not found. Download via TAP first.")
        return
    stars = parse_gaia_csv(csv_path)
    print(f"Loaded {len(stars)} stars from {csv_path}")
    print()

    # Compute |v_CMB| per star
    v_cmb_kms = np.array([cmb_frame_velocity_kms(s) for s in stars])

    # Drop outliers (|v_CMB| > 1500 km/s = clearly halo / accreted / data-bad)
    mask = v_cmb_kms < 1500
    v_cmb_clean = v_cmb_kms[mask]
    print(f"After cut (|v_CMB| < 1500 km/s): {len(v_cmb_clean)} stars")
    print()

    # Distribution statistics
    print("Distribution statistics (|v_CMB|, km/s):")
    print(f"  Mean:    {np.mean(v_cmb_clean):.2f}")
    print(f"  Median:  {np.median(v_cmb_clean):.2f}")
    print(f"  Std:     {np.std(v_cmb_clean):.2f}")
    print(f"  Min:     {np.min(v_cmb_clean):.2f}")
    print(f"  Max:     {np.max(v_cmb_clean):.2f}")
    print(f"  5%ile:   {np.percentile(v_cmb_clean, 5):.2f}")
    print(f"  25%ile:  {np.percentile(v_cmb_clean, 25):.2f}")
    print(f"  75%ile:  {np.percentile(v_cmb_clean, 75):.2f}")
    print(f"  95%ile:  {np.percentile(v_cmb_clean, 95):.2f}")
    print()

    # Test vs AVE prediction
    print(f"AVE prediction: {V_SUBSTRATE_KMS:.2f} km/s")
    print(f"Median deviation: {np.median(v_cmb_clean) - V_SUBSTRATE_KMS:+.2f} km/s "
          f"({(np.median(v_cmb_clean) - V_SUBSTRATE_KMS)/V_SUBSTRATE_KMS*100:+.2f}%)")
    print(f"Mean deviation:   {np.mean(v_cmb_clean) - V_SUBSTRATE_KMS:+.2f} km/s "
          f"({(np.mean(v_cmb_clean) - V_SUBSTRATE_KMS)/V_SUBSTRATE_KMS*100:+.2f}%)")

    # Mode estimate via histogram bin
    hist, bin_edges = np.histogram(v_cmb_clean, bins=100, range=(0, 800))
    mode_bin_center = (bin_edges[np.argmax(hist)] + bin_edges[np.argmax(hist) + 1]) / 2
    print(f"Mode (histogram peak): {mode_bin_center:.2f} km/s "
          f"({(mode_bin_center - V_SUBSTRATE_KMS)/V_SUBSTRATE_KMS*100:+.2f}%)")
    print()

    # Pre-registered outcome categorization
    median = np.median(v_cmb_clean)
    if abs(median - V_SUBSTRATE_KMS) < 20:
        outcome = "A — sharp cluster (median within ±20 km/s of prediction)"
    elif abs(median - V_SUBSTRATE_KMS) < 50:
        outcome = "B — broad cluster (median within ±50 km/s)"
    elif 200 < median < 500:
        outcome = "C — ambiguous (in [200, 500] but not within ±50 of prediction)"
    else:
        outcome = "D — FALSIFIED (median outside [200, 500] window)"
    print(f"PRE-REGISTERED OUTCOME: {outcome}")
    print()

    # Generate distribution plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Full distribution
    ax1.hist(v_cmb_clean, bins=100, range=(0, 800), color="steelblue", alpha=0.7, edgecolor="black")
    ax1.axvline(V_SUBSTRATE_KMS, color="red", linestyle="--", linewidth=2,
                label=f"AVE prediction: αc/(2π) = {V_SUBSTRATE_KMS:.1f} km/s")
    ax1.axvline(SUN_CMB_MAG_KMS, color="green", linestyle=":", linewidth=2,
                label=f"Sun CMB velocity: 370 km/s")
    ax1.axvline(np.median(v_cmb_clean), color="orange", linestyle="-", linewidth=2,
                label=f"Sample median: {np.median(v_cmb_clean):.1f} km/s")
    ax1.set_xlabel("|v_CMB| (km/s)", fontsize=12)
    ax1.set_ylabel("# stars", fontsize=12)
    ax1.set_title(f"Gaia DR3 nearby G/K dwarfs (N={len(v_cmb_clean)}) — CMB-frame velocity")
    ax1.legend(fontsize=10)
    ax1.grid(alpha=0.3)

    # Zoom into 200-600 km/s
    ax2.hist(v_cmb_clean, bins=80, range=(200, 600), color="steelblue", alpha=0.7, edgecolor="black")
    ax2.axvline(V_SUBSTRATE_KMS, color="red", linestyle="--", linewidth=2,
                label=f"αc/(2π) = {V_SUBSTRATE_KMS:.1f} km/s")
    ax2.axvline(SUN_CMB_MAG_KMS, color="green", linestyle=":", linewidth=2,
                label=f"Sun: 370 km/s")
    ax2.axvline(np.median(v_cmb_clean), color="orange", linestyle="-", linewidth=2,
                label=f"Median: {np.median(v_cmb_clean):.1f}")
    ax2.set_xlabel("|v_CMB| (km/s)", fontsize=12)
    ax2.set_ylabel("# stars", fontsize=12)
    ax2.set_title(f"Zoom: 200-600 km/s range")
    ax2.legend(fontsize=10)
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    out_path = Path(__file__).parent.parent.parent / "assets" / "sim_outputs" / "gaia_substrate_equilibrium_test.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved distribution plot to {out_path}")


if __name__ == "__main__":
    main()
