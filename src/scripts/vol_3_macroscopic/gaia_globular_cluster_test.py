"""
Globular Cluster Substrate-Equilibrium Velocity Test — αc/(2π) vs MW GC population

SCOPE NOTE (2026-05-17 night — Tier-2 #5 followup to cycle-12 thread):

Tests the αc/(2π) ≈ 348.2 km/s substrate-equilibrium velocity prediction at the
MW globular cluster (GC) population — the most-decoupled-from-disk stellar
class available in our Galaxy. Path to SPARC-parity foreword promotion if GC
population clusters near αc/(2π) rather than LSR-class bulk velocity or
quadrature-overlay.

Pre-registered at:
  research/2026-05-17_substrate_equilibrium_velocity_GLOBULAR_CLUSTER_prereg.md

Pre-registered outcomes:
  - OUTCOME I (FLOOR-confirmed): GC median |v_CMB| in 338-358 km/s →
    foreword promotion as 2nd SPARC-class empirical anchor
  - OUTCOME II (canonical confirmed): GC median in 390-430 km/s → current
    interpretation validated (quadrature with MW barycenter motion)
  - OUTCOME III (cosmic-flow dominated): GC median in 480-560 km/s →
    substrate-velocity walks back to LSR-only scope
  - OUTCOME IV (wide scatter): σ ≥ 200 km/s with no clear cluster → inconclusive

INPUTS (empirical):
  - /tmp/baumgardt_gc_orbits.txt — Baumgardt+Vasiliev MW globular cluster
    catalog (Vasiliev & Baumgardt 2021, arXiv:2105.04580; downloaded from
    https://people.smp.uq.edu.au/HolgerBaumgardt/globular/orbits_table.txt)
  - 165 MW globular clusters with Gaia EDR3-based 6D phase-space measurements
  - Sun's CMB velocity 370 km/s toward (l, b) = (264°, 48°) — Planck 2018
  - IAU J2000 equatorial-to-galactic rotation matrix — standard

DERIVED (forward computation, no fit):
  - αc/(2π) = 348.18 km/s substrate-equilibrium velocity prediction (canonical)
  - Per-GC heliocentric velocity in galactic Cartesian frame (forward calc)
  - Per-GC |v_CMB| (forward calc)
  - Population statistics: median, mean, σ, distribution histogram
  - Outcome categorization per pre-reg

NO FIT PARAMETERS. Distribution either supports one of the 4 pre-registered
outcomes or it doesn't.

Per ave-driver-script-honesty discipline + full 6-skill pre-derivation stack
per Grant directive "full skills ahead" 2026-05-17 night.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from ave.core.constants import ALPHA, C_0


V_SUBSTRATE_KMS = ALPHA * C_0 / (2 * np.pi) / 1000.0  # canonical: 348.18 km/s

# Sun's CMB velocity (Planck 2018) in galactic coordinates
SUN_CMB_MAG_KMS = 370.0
_l, _b = np.radians(264.0), np.radians(48.0)
SUN_CMB_VEC_GAL = SUN_CMB_MAG_KMS * np.array([
    np.cos(_b) * np.cos(_l),
    np.cos(_b) * np.sin(_l),
    np.sin(_b),
])

# IAU J2000 equatorial → galactic rotation matrix (standard)
R_EQ_TO_GAL = np.array([
    [-0.054876, -0.873437, -0.483835],
    [+0.494109, -0.444830, +0.746982],
    [-0.867666, -0.198076, +0.455984],
])


def parse_baumgardt_gc_catalog(path: Path) -> list[dict]:
    """Parse the Baumgardt+Vasiliev MW globular cluster orbits table.

    Format: space-separated, with 3 header lines (starting with #).
    Columns: Cluster RA DEC l b Rsun Delta_R R_GC <RV> ERV mualpha Del_mu
             mu_delta Del_mu corr X Delta_X Y Delta_Y Z Delta_Z U Delta_U
             V Delta_V W Delta_W R_Per Delta_R R_Apo Delta_R
    """
    gcs = []
    with path.open("r") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.split()
            if len(parts) < 14:
                continue
            try:
                gcs.append({
                    "name": parts[0],
                    "ra": float(parts[1]),
                    "dec": float(parts[2]),
                    "l": float(parts[3]),
                    "b": float(parts[4]),
                    "d_helio_kpc": float(parts[5]),
                    "rv": float(parts[8]),
                    "pmra": float(parts[10]),
                    "pmdec": float(parts[12]),
                })
            except (ValueError, IndexError):
                continue
    return gcs


def heliocentric_velocity_galactic(gc: dict) -> np.ndarray:
    """Compute heliocentric velocity vector in galactic Cartesian frame.

    Reuses the chain from gaia_floor_test.py heliocentric_velocity_galactic
    but uses distance in kpc (converted to pc).
    """
    ra, dec = np.radians(gc["ra"]), np.radians(gc["dec"])
    d_pc = gc["d_helio_kpc"] * 1000.0
    v_alpha = 4.740470463e-3 * gc["pmra"] * d_pc
    v_delta = 4.740470463e-3 * gc["pmdec"] * d_pc
    v_r = gc["rv"]
    cra, sra, cde, sde = np.cos(ra), np.sin(ra), np.cos(dec), np.sin(dec)
    v_eq = np.array([
        v_r * cde * cra - v_alpha * sra - v_delta * sde * cra,
        v_r * cde * sra + v_alpha * cra - v_delta * sde * sra,
        v_r * sde + v_delta * cde,
    ])
    return R_EQ_TO_GAL @ v_eq


def main() -> None:
    print("=" * 78)
    print("  GLOBULAR CLUSTER SUBSTRATE-EQUILIBRIUM VELOCITY TEST")
    print("  Tier-2 #5 followup to cycle-12 canonization (2026-05-17 night)")
    print("=" * 78)
    print()
    print(f"AVE prediction: substrate-equilibrium velocity = αc/(2π) = {V_SUBSTRATE_KMS:.2f} km/s")
    print()

    catalog_path = Path("/tmp/baumgardt_gc_orbits.txt")
    gcs = parse_baumgardt_gc_catalog(catalog_path)
    print(f"Loaded {len(gcs)} MW globular clusters from Baumgardt+Vasiliev catalog")
    print()

    # Compute |v_CMB| per GC
    v_cmb_list = []
    v_helio_mag_list = []
    gc_names_kept = []
    for gc in gcs:
        try:
            v_helio = heliocentric_velocity_galactic(gc)
            v_cmb = v_helio + SUN_CMB_VEC_GAL
            v_helio_mag_list.append(float(np.linalg.norm(v_helio)))
            v_cmb_list.append(float(np.linalg.norm(v_cmb)))
            gc_names_kept.append(gc["name"])
        except (ValueError, ZeroDivisionError):
            continue

    v_cmb = np.array(v_cmb_list)
    v_helio_mag = np.array(v_helio_mag_list)
    print(f"Computed |v_CMB| for {len(v_cmb)} GCs (after outlier filtering: none required)")
    print()

    # Population statistics
    median_v_cmb = float(np.median(v_cmb))
    mean_v_cmb = float(np.mean(v_cmb))
    std_v_cmb = float(np.std(v_cmb))
    min_v_cmb = float(np.min(v_cmb))
    max_v_cmb = float(np.max(v_cmb))
    p25 = float(np.percentile(v_cmb, 25))
    p75 = float(np.percentile(v_cmb, 75))

    print("POPULATION STATISTICS:")
    print(f"  N                = {len(v_cmb)}")
    print(f"  median |v_CMB|   = {median_v_cmb:.2f} km/s")
    print(f"  mean   |v_CMB|   = {mean_v_cmb:.2f} km/s")
    print(f"  σ      |v_CMB|   = {std_v_cmb:.2f} km/s")
    print(f"  range            = [{min_v_cmb:.2f}, {max_v_cmb:.2f}] km/s")
    print(f"  IQR              = [{p25:.2f}, {p75:.2f}] km/s (25%-75% percentiles)")
    print()

    # Compare to prediction + alternatives
    print("COMPARISON TO PREDICTIONS:")
    print(f"  AVE substrate prediction        = {V_SUBSTRATE_KMS:.2f} km/s")
    print(f"  LSR-class thin-disk reference   = 375.18 km/s (per FLOOR test result)")
    print(f"  Quadrature with σ_GC=150        = {np.sqrt(375.18**2 + 150**2):.2f} km/s")
    print(f"  Quadrature with σ_GC=200        = {np.sqrt(375.18**2 + 200**2):.2f} km/s")
    print(f"  Local Group flow approx         = 543 km/s")
    print()
    print(f"  Δ(median vs αc/(2π))            = {median_v_cmb - V_SUBSTRATE_KMS:+.2f} km/s "
          f"({100*(median_v_cmb-V_SUBSTRATE_KMS)/V_SUBSTRATE_KMS:+.1f}%)")
    print(f"  Δ(median vs thin-disk)          = {median_v_cmb - 375.18:+.2f} km/s")
    print(f"  Δ(median vs quad σ=150)         = {median_v_cmb - np.sqrt(375.18**2 + 150**2):+.2f} km/s")
    print(f"  Δ(median vs Local Group flow)   = {median_v_cmb - 543.0:+.2f} km/s")
    print()

    # Pre-registered outcome categorization
    print("PRE-REGISTERED OUTCOME ADJUDICATION:")
    if 338 <= median_v_cmb <= 358:
        outcome = "OUTCOME I — FLOOR-confirmed (median in 338-358 km/s range)"
        promotion = "→ FOREWORD PROMOTION as 2nd SPARC-class empirical anchor"
    elif 390 <= median_v_cmb <= 430:
        outcome = "OUTCOME II — Canonical interpretation confirmed (median in 390-430 km/s range, quadrature with MW barycenter)"
        promotion = "→ no foreword promotion; framework consistent with current canonical interpretation"
    elif 480 <= median_v_cmb <= 560:
        outcome = "OUTCOME III — Cosmic-flow dominated (median in 480-560 km/s range)"
        promotion = "→ substrate-velocity prediction walks back to LSR-class-only scope"
    elif std_v_cmb >= 200:
        outcome = f"OUTCOME IV — Wide scatter (σ = {std_v_cmb:.1f} km/s ≥ 200)"
        promotion = "→ test inconclusive; GC population too diverse"
    else:
        outcome = (f"OUTCOME UNCATEGORIZED — median {median_v_cmb:.1f} km/s, "
                   f"σ {std_v_cmb:.1f} km/s; intermediate between pre-registered categories")
        promotion = "→ partial-information outcome; sub-cycle audit needed"

    print(f"  {outcome}")
    print(f"  {promotion}")
    print()

    # Comparison with FLOOR test thin-disk + halo populations
    print("CONTEXT (from FLOOR test 2026-05-17 late evening):")
    print(f"  Thin disk (|v_LSR|<30)     N=11690, median 375.18 km/s, σ=11.24")
    print(f"  Thick disk (30-70)         N=14013, median 382.22 km/s, σ=21.65")
    print(f"  Thick disk (70-100)        N=2786,  median 399.33 km/s, σ=31.08")
    print(f"  Halo (100-200)             N=899,   median 426.96 km/s, σ=43.40")
    print(f"  Extreme halo (>200)        N=78,    median 574.08 km/s, σ=84.47")
    print(f"  GLOBULAR CLUSTERS (this)   N={len(v_cmb):<5d}, median {median_v_cmb:.2f} km/s, σ={std_v_cmb:.2f}")
    print()

    # Print the 5 lowest + 5 highest GCs for sanity check
    sorted_indices = np.argsort(v_cmb)
    print("FIVE LOWEST |v_CMB| GCs:")
    for i in sorted_indices[:5]:
        print(f"  {gc_names_kept[i]:18s} |v_CMB| = {v_cmb[i]:6.2f} km/s, |v_helio| = {v_helio_mag[i]:6.2f} km/s")
    print()
    print("FIVE HIGHEST |v_CMB| GCs:")
    for i in sorted_indices[-5:]:
        print(f"  {gc_names_kept[i]:18s} |v_CMB| = {v_cmb[i]:6.2f} km/s, |v_helio| = {v_helio_mag[i]:6.2f} km/s")
    print()

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: histogram with predictions overlaid
    axes[0].hist(v_cmb, bins=30, range=(0, max(v_cmb) + 50), color="steelblue",
                 alpha=0.7, edgecolor="black", linewidth=0.5)
    axes[0].axvline(V_SUBSTRATE_KMS, color="red", linestyle="--", linewidth=2,
                    label=f"αc/(2π) AVE pred = {V_SUBSTRATE_KMS:.1f}")
    axes[0].axvline(375.18, color="green", linestyle=":", linewidth=2,
                    label=f"Thin-disk ref = 375.18")
    axes[0].axvline(np.sqrt(375.18**2 + 150**2), color="orange", linestyle="-.",
                    linewidth=2, label=f"Quadrature σ=150 = {np.sqrt(375.18**2 + 150**2):.1f}")
    axes[0].axvline(median_v_cmb, color="black", linestyle="-", linewidth=2,
                    label=f"Observed median = {median_v_cmb:.1f}")
    axes[0].set_xlabel("|v_CMB| (km/s)", fontsize=11)
    axes[0].set_ylabel("Count", fontsize=11)
    axes[0].set_title(f"MW Globular Cluster |v_CMB| Distribution (N={len(v_cmb)})")
    axes[0].legend(fontsize=9, loc="upper right")
    axes[0].grid(alpha=0.3)

    # Right: comparison panel with thin-disk + halo bins
    contexts = [
        ("Thin disk\n(N=11690)", 375.18, 11.24, "lightblue"),
        ("Thick disk\n(30-70)\n(N=14013)", 382.22, 21.65, "skyblue"),
        ("Thick disk\n(70-100)\n(N=2786)", 399.33, 31.08, "steelblue"),
        ("Halo\n(100-200)\n(N=899)", 426.96, 43.40, "navy"),
        ("Extreme halo\n(>200)\n(N=78)", 574.08, 84.47, "darkblue"),
        (f"GC\n(this test)\n(N={len(v_cmb)})", median_v_cmb, std_v_cmb, "red"),
    ]
    xs = np.arange(len(contexts))
    medians = [c[1] for c in contexts]
    stds = [c[2] for c in contexts]
    labels = [c[0] for c in contexts]
    colors = [c[3] for c in contexts]

    axes[1].bar(xs, medians, yerr=stds, color=colors, edgecolor="black",
                linewidth=1, capsize=5)
    axes[1].axhline(V_SUBSTRATE_KMS, color="red", linestyle="--", linewidth=2,
                    label=f"αc/(2π) = {V_SUBSTRATE_KMS:.1f}")
    axes[1].set_xticks(xs)
    axes[1].set_xticklabels(labels, fontsize=8, rotation=0)
    axes[1].set_ylabel("Median |v_CMB| ± σ (km/s)", fontsize=11)
    axes[1].set_title("Population comparison: GCs vs FLOOR test stellar bins")
    axes[1].legend(fontsize=10)
    axes[1].grid(alpha=0.3, axis="y")

    plt.tight_layout()
    out_path = (Path(__file__).parent.parent.parent / "assets" / "sim_outputs"
                / "gaia_globular_cluster_test.png")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved plot to: {out_path}")
    print()
    print("=" * 78)


if __name__ == "__main__":
    main()
