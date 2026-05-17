"""
SPARC Catalog Ingest + AVE Benchmark (C13a Promotion: 5-galaxy hard-code -> 175-galaxy fit).

Per closure-roadmap §0.5 open scope-correction item: "5-galaxy -> SPARC catalog
ingestion (C13a row): current 'validation' is 5 hard-coded galaxies in
galactic_rotation.py; promotion to full forward-prediction status requires real
SPARC catalog (175+ galaxies, public) ingestion + benchmark."

This script:
  1. Parses SPARC_Lelli2016c.mrt (175 late-type galaxies, Lelli+2016)
  2. For each galaxy: extracts Rdisk (disk scale length), L[3.6] (stellar
     luminosity), MHI (HI gas mass), Vflat (asymptotic flat velocity)
  3. Computes baryonic mass M_disk = (M*/L)_36 × L_36 + 1.33 × MHI
     where M*/L = 0.5 (standard SPARC assumption per McGaugh+2016) and
     1.33× corrects for He contribution to gas mass
  4. Builds GalaxyModel using ave.regime_3_saturated.galactic_rotation engine
  5. Computes AVE-predicted V_flat at r = 5×R_disk (deep MOND regime where
     V_AVE ≈ (G M_baryonic a_0)^(1/4))
  6. Compares predicted vs observed; reports residual statistics

Outputs:
  - Per-galaxy table: name, M_disk, Rdisk, V_obs, V_AVE, residual (fraction)
  - Statistics: mean residual, RMS residual, distribution histogram, Q-flag binning
  - Status: pass/fail vs C13a row's "~17% offset on 5 hard-coded galaxies" benchmark

Status (2026-05-17): green-field engineering work. C13a promotes from
partial-PASS (5 hardcode) to forward-prediction status if SPARC mean residual
< 20% with reasonable scatter. AVE-distinct test: zero-parameter fit (no
per-galaxy M*/L tuning), single canonical a_0 = c H_inf/(2pi) for all 175.

Data source: SPARC database (Lelli, McGaugh, Schombert 2016 AJ 152 157).
URL: https://astroweb.cwru.edu/SPARC/
File: data/SPARC/SPARC_Lelli2016c.mrt (downloaded 2026-05-17)
"""

import sys
from pathlib import Path

import numpy as np

# Allow running as module or script
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

from ave.core.constants import M_SUN, G  # noqa: E402
from ave.regime_3_saturated.galactic_rotation import (  # noqa: E402
    A0_LATTICE,
    GalaxyModel,
    ave_rotation_velocity,
)

# Constants
KPC = 3.0857e19  # m
ML_RATIO_36 = 0.5  # Standard SPARC M*/L assumption at 3.6 μm per McGaugh+2016
HE_CORRECTION = 1.33  # Multiplies HI mass to account for primordial He
SPARC_FILE = REPO_ROOT / "data" / "SPARC" / "SPARC_Lelli2016c.mrt"


def parse_sparc_table1(path: Path) -> list[dict]:
    """
    Parse SPARC_Lelli2016c.mrt machine-readable table.

    Field order per file documentation:
        Galaxy(A11) T(I2) D(F6.2) e_D(F5.2) f_D(I2) Inc(F4.1) e_Inc(F4.1)
        L[3.6](F7.3) e_L[3.6](F7.3) Reff(F5.2) SBeff(F8.2) Rdisk(F5.2)
        SBdisk(F8.2) MHI(F7.3) RHI(F5.2) Vflat(F5.1) e_Vflat(F5.1) Q(I3) Ref(A14)

    Note: MRT byte positions in the spec do NOT match the actual data file
    (known SPARC formatting issue). Parsing by whitespace-split + field order
    is more robust. Galaxy name field uses leading spaces which we handle by
    taking the first field after stripping.

    Returns list of dicts (one per galaxy).
    """
    galaxies = []
    in_data = False
    separator_count = 0
    with open(path) as f:
        for line in f:
            if line.startswith("-" * 5):
                separator_count += 1
                # 1st separator = before byte table; 2nd = after byte table
                if separator_count == 2:
                    in_data = True
                continue
            if not in_data:
                continue
            # Skip Note(N): blocks
            if line.startswith("Note") or line.strip() == "":
                continue
            # Data row: whitespace-split into fields
            parts = line.split()
            # Expected field count: 19 if Ref present, 18 if absent
            if len(parts) < 18:
                continue
            try:
                # parts[0] = name (after leading-whitespace strip)
                # parts[1] = T (Hubble type)
                # parts[2] = D (distance)
                # parts[5] = Inc
                # parts[7] = L[3.6]
                # parts[11] = Rdisk
                # parts[13] = MHI
                # parts[15] = Vflat
                # parts[16] = e_Vflat
                # parts[17] = Q
                name = parts[0]
                distance = float(parts[2])
                l36 = float(parts[7])
                rdisk = float(parts[11])
                mhi = float(parts[13])
                vflat = float(parts[15])
                q = int(parts[17])
                if vflat <= 0 or rdisk <= 0:
                    continue
                if l36 <= 0 and mhi <= 0:
                    continue
                galaxies.append({
                    "name": name,
                    "distance_Mpc": distance,
                    "L36_1e9_Lsun": l36,
                    "Rdisk_kpc": rdisk,
                    "MHI_1e9_Msun": mhi,
                    "Vflat_kms": vflat,
                    "Q": q,
                })
            except (ValueError, IndexError):
                continue
    return galaxies


def baryonic_mass_kg(galaxy_dict: dict) -> float:
    """Total baryonic mass: M_stellar + 1.33 × M_HI."""
    m_star = ML_RATIO_36 * galaxy_dict["L36_1e9_Lsun"] * 1e9 * M_SUN
    m_gas = HE_CORRECTION * galaxy_dict["MHI_1e9_Msun"] * 1e9 * M_SUN
    return m_star + m_gas


def benchmark_galaxy(galaxy_dict: dict, eval_radius_scale: float = 5.0) -> dict:
    """
    Compute AVE-predicted Vflat for one galaxy, compare to observed.

    Args:
        galaxy_dict: parsed SPARC row
        eval_radius_scale: r/R_disk at which to evaluate AVE prediction
                          (5.0 is deep into flat-rotation regime)

    Returns:
        dict with prediction + residual
    """
    M_baryonic = baryonic_mass_kg(galaxy_dict)
    R_d = galaxy_dict["Rdisk_kpc"] * KPC
    model = GalaxyModel(name=galaxy_dict["name"], M_disk=M_baryonic, R_d=R_d)
    r_eval = eval_radius_scale * R_d
    v_ave = ave_rotation_velocity(model, r_eval, a0=A0_LATTICE) / 1000.0  # m/s -> km/s
    v_obs = galaxy_dict["Vflat_kms"]
    residual = (v_ave - v_obs) / v_obs if v_obs > 0 else 0.0
    return {
        "name": galaxy_dict["name"],
        "Q": galaxy_dict["Q"],
        "M_baryonic_1e9_Msun": M_baryonic / (1e9 * M_SUN),
        "Rdisk_kpc": galaxy_dict["Rdisk_kpc"],
        "Vflat_obs_kms": v_obs,
        "Vflat_AVE_kms": v_ave,
        "residual_fractional": residual,
    }


def main():
    print("=" * 80)
    print("SPARC Catalog AVE Benchmark — C13a Promotion (5-galaxy -> 175-galaxy)")
    print("=" * 80)
    print(f"Source: {SPARC_FILE}")
    print(f"Engine: ave.regime_3_saturated.galactic_rotation")
    print(f"a_0 = {A0_LATTICE:.4e} m/s^2 (canonical, no free parameters)")
    print(f"M*/L_3.6 = {ML_RATIO_36} M_sun/L_sun (standard SPARC)")
    print(f"He correction: 1.33 × M_HI")
    print(f"Eval radius: 5 × R_disk (deep MOND regime)")
    print()

    if not SPARC_FILE.exists():
        print(f"ERROR: {SPARC_FILE} not found.")
        print("Download from https://astroweb.cwru.edu/SPARC/SPARC_Lelli2016c.mrt")
        sys.exit(1)

    galaxies = parse_sparc_table1(SPARC_FILE)
    print(f"Parsed {len(galaxies)} galaxies from SPARC catalog")
    print()

    results = [benchmark_galaxy(g) for g in galaxies]

    # Filter to galaxies with valid V_AVE prediction
    valid = [r for r in results if r["Vflat_AVE_kms"] > 0 and r["Vflat_obs_kms"] > 0]
    print(f"Valid predictions: {len(valid)} / {len(results)}")
    print()

    # Statistics on residuals
    residuals = np.array([r["residual_fractional"] for r in valid])
    abs_residuals = np.abs(residuals)
    print("=" * 80)
    print("Residual Statistics: (V_AVE - V_obs) / V_obs")
    print("=" * 80)
    print(f"Mean residual:       {np.mean(residuals):+.4f}  ({np.mean(residuals)*100:+.2f}%)")
    print(f"Median residual:     {np.median(residuals):+.4f}  ({np.median(residuals)*100:+.2f}%)")
    print(f"Mean |residual|:     {np.mean(abs_residuals):.4f}  ({np.mean(abs_residuals)*100:.2f}%)")
    print(f"RMS residual:        {np.sqrt(np.mean(residuals**2)):.4f}  ({np.sqrt(np.mean(residuals**2))*100:.2f}%)")
    print(f"Std of residual:     {np.std(residuals):.4f}  ({np.std(residuals)*100:.2f}%)")
    print(f"Min residual:        {np.min(residuals):+.4f}  ({np.min(residuals)*100:+.2f}%)")
    print(f"Max residual:        {np.max(residuals):+.4f}  ({np.max(residuals)*100:+.2f}%)")
    print()

    # Quality-flag binning
    print("=" * 80)
    print("Residuals by SPARC Quality Flag (Q=1 best, Q=3 worst)")
    print("=" * 80)
    for q in [1, 2, 3]:
        subset = [r for r in valid if r["Q"] == q]
        if subset:
            subset_res = np.array([r["residual_fractional"] for r in subset])
            print(f"Q={q}: n={len(subset):3d}  mean={np.mean(subset_res):+.3f}  "
                  f"RMS={np.sqrt(np.mean(subset_res**2)):.3f}  "
                  f"mean|res|={np.mean(np.abs(subset_res)):.3f}")
    print()

    # Compare to C13a row's benchmark
    print("=" * 80)
    print("C13a Row Comparison (~17% offset on 5 hard-coded galaxies)")
    print("=" * 80)
    print(f"5-galaxy hard-coded benchmark (prior C13a row):  ~17% offset")
    print(f"175-galaxy SPARC benchmark (this script):        {np.mean(abs_residuals)*100:.2f}% mean |res|")
    print(f"                                                 {np.sqrt(np.mean(residuals**2))*100:.2f}% RMS")
    print()

    # Sample table
    print("=" * 80)
    print("Sample (first 20 galaxies, sorted by name)")
    print("=" * 80)
    print(f"{'Galaxy':<12} {'Q':>2} {'M_bar':>8} {'R_d':>6} {'V_obs':>7} {'V_AVE':>7} {'res':>8}")
    print(f"{'':<12} {'':>2} {'1e9Msun':>8} {'kpc':>6} {'km/s':>7} {'km/s':>7} {'frac':>8}")
    print("-" * 80)
    sorted_valid = sorted(valid, key=lambda r: r["name"])
    for r in sorted_valid[:20]:
        print(f"{r['name']:<12} {r['Q']:>2} {r['M_baryonic_1e9_Msun']:>8.2f} "
              f"{r['Rdisk_kpc']:>6.2f} {r['Vflat_obs_kms']:>7.1f} "
              f"{r['Vflat_AVE_kms']:>7.1f} {r['residual_fractional']:>+8.3f}")
    print(f"... ({len(sorted_valid)-20} more not shown)")
    print()

    # Status verdict
    print("=" * 80)
    print("Status verdict")
    print("=" * 80)
    mean_abs = np.mean(abs_residuals) * 100
    if mean_abs < 20:
        verdict = "PASS"
        msg = f"AVE matches SPARC 175-galaxy catalog at {mean_abs:.2f}% mean |residual| (< 20% threshold)"
    elif mean_abs < 35:
        verdict = "PARTIAL"
        msg = f"AVE matches SPARC at {mean_abs:.2f}% mean |residual| (between 20% and 35%)"
    else:
        verdict = "FAIL"
        msg = f"AVE differs from SPARC by {mean_abs:.2f}% mean |residual| (> 35% threshold)"
    print(f"{verdict}: {msg}")
    print()

    return results


if __name__ == "__main__":
    main()
