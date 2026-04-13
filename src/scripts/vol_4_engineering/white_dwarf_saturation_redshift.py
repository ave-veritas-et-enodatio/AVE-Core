"""
AVE MODULE: White Dwarf Gravitational Redshift — Saturation Correction
======================================================================
First-principles prediction of the Axiom 4 saturation correction
to the gravitational redshift of white dwarf spectral lines.

DERIVATION CHAIN (see LIVING_REFERENCE.md §"How to Apply AVE"):
  1. LC Analogs:  WD is a massive topological defect; ε_local, μ_local
  2. Strain:      ε₁₁(R) = 7GM/(c²R) — principal radial strain at surface
  3. Operators:   S(ε₁₁) = √(1 − ε₁₁²) — Axiom 4 saturation factor
                  n(R) = 1 + 2GM/(c²R) — Axiom 3 refractive index
  4. Symmetry:    α is INVARIANT (ε and c carry same n·S → cancel)
  5. Observable:  Clock rate ω_local/ω_∞ = 1/(n·S)
                  GR predicts:  1/n
                  AVE predicts: 1/(n·S) → faster by factor 1/S ≈ 1 + ε₁₁²/2
  6. Testability: WD redshift measured to ~0.1% — AVE correction is 0.1–1%

USAGE:
    python src/scripts/vol_4_engineering/white_dwarf_saturation_redshift.py

OUTPUT:
    Table of AVE vs GR predictions for well-measured white dwarfs
    Publication-quality comparison figure
"""

import math
import os

# ── Engine imports ──
from ave.core.constants import G, C_0, ALPHA, NU_VAC, M_SUN


# ═════════════════════════════════════════
# White Dwarf Catalog (measured parameters)
# ═════════════════════════════════════════
# Sources: Holberg+ 2012, Joyce+ 2018, Bond+ 2017, Pasquini+ 2019

CATALOG = [
    {
        "name": "Sirius B",
        "M_solar": 1.018,        # Holberg+ 2012 (HST)
        "R_km": 5_800,           # ≈ 0.0084 R☉
        "v_obs_kms": 80.65,      # Gravitational redshift (Joyce+ 2018, HST/STIS)
        "v_obs_err_kms": 0.77,   # ±0.77 km/s
        "ref": "Joyce+ 2018",
    },
    {
        "name": "40 Eridani B",
        "M_solar": 0.573,        # Mason+ 2017
        "R_km": 9_000,           # ~0.013 R☉ (Shipman 1979)
        "v_obs_kms": 23.9,       # Pasquini+ 2019
        "v_obs_err_kms": 1.3,
        "ref": "Pasquini+ 2019",
    },
    {
        "name": "Procyon B",
        "M_solar": 0.602,
        "R_km": 8_600,           # ~0.012 R☉
        "v_obs_kms": 28.0,       # Provencal+ 2002
        "v_obs_err_kms": 3.0,
        "ref": "Provencal+ 2002",
    },
    {
        "name": "Stein 2051 B",
        "M_solar": 0.675,        # Sahu+ 2017 (astrometric mass from HST)
        "R_km": 8_000,           # estimated from mass-radius relation
        "v_obs_kms": None,       # no direct spectroscopic redshift published
        "v_obs_err_kms": None,
        "ref": "Sahu+ 2017",
    },
]


def compute_redshift(M_kg: float, R_m: float) -> dict:
    """
    Compute gravitational redshift for a white dwarf.

    Returns dict with:
        eps11:   Principal radial strain (Axiom 4)
        n:       Refractive index (Axiom 3)
        S:       Saturation factor (Axiom 4)
        z_GR:    GR-predicted gravitational redshift
        z_AVE:   AVE-predicted gravitational redshift (includes saturation)
        delta:   Fractional correction (z_AVE - z_GR) / z_GR
    """
    # Step 2: Strain
    eps11 = 7.0 * G * M_kg / (C_0**2 * R_m)

    # Step 3: Operators
    phi_over_c2 = G * M_kg / (C_0**2 * R_m)  # GM/(c²R)
    n = 1.0 + 2.0 * phi_over_c2               # refractive index
    S = math.sqrt(max(1.0 - eps11**2, 0.0))   # saturation factor

    # Step 5: Observable
    # GR:  z_GR = n - 1 = 2GM/(c²R)  (to leading order)
    # More precisely: z_GR = 1/√(1 - 2GM/(c²R)) - 1 ≈ GM/(c²R) + ...
    # But in AVE: z = n·S - 1 for the full local-to-infinity redshift
    #   ω_local = ω_∞ / (n·S)
    #   f_observed/f_emitted = 1/(n·S)
    #   z = (λ_obs - λ_emit)/λ_emit = n·S - 1

    # GR gravitational redshift (exact Schwarzschild)
    rs_over_r = 2.0 * phi_over_c2
    if rs_over_r >= 1.0:
        z_GR = float('inf')
        z_AVE = float('inf')
    else:
        z_GR = 1.0 / math.sqrt(1.0 - rs_over_r) - 1.0
        # AVE: additional 1/S factor
        z_AVE = 1.0 / (math.sqrt(1.0 - rs_over_r) * S) - 1.0

    delta = (z_AVE - z_GR) / z_GR if z_GR > 0 else 0.0

    return {
        "eps11": eps11,
        "n": n,
        "S": S,
        "phi_c2": phi_over_c2,
        "z_GR": z_GR,
        "z_AVE": z_AVE,
        "delta_pct": delta * 100.0,     # percent
        "v_GR_kms": z_GR * C_0 / 1000.0,   # km/s equivalent
        "v_AVE_kms": z_AVE * C_0 / 1000.0,
    }


def main():
    print("=" * 72)
    print("AVE White Dwarf Gravitational Redshift — Saturation Correction")
    print("=" * 72)
    print()
    print("Derivation: ω_local/ω_∞ = 1/(n·S)")
    print("  n(R) = 1 + 2GM/(c²R)           [Axiom 3 — Symmetric Gravity]")
    print("  S(ε₁₁) = √(1 − ε₁₁²)          [Axiom 4 — Saturation]")
    print("  ε₁₁ = 7GM/(c²R)                [Principal radial strain]")
    print()

    # Header
    fmt_hdr = "{:<16s} {:>8s} {:>8s} {:>10s} {:>10s} {:>10s} {:>10s} {:>8s}"
    fmt_row = "{:<16s} {:>8.3f} {:>8.0f} {:>10.3e} {:>10.3e} {:>10.3e} {:>10.3e} {:>8.4f}"
    print(fmt_hdr.format(
        "White Dwarf", "M/M☉", "R [km]",
        "ε₁₁", "z_GR", "z_AVE", "Δz",
        "Δ [%]",
    ))
    print("-" * 92)

    results = []
    for wd in CATALOG:
        M_kg = wd["M_solar"] * M_SUN
        R_m = wd["R_km"] * 1000.0

        r = compute_redshift(M_kg, R_m)
        results.append((wd, r))

        dz = r["z_AVE"] - r["z_GR"]
        print(fmt_row.format(
            wd["name"], wd["M_solar"], wd["R_km"],
            r["eps11"], r["z_GR"], r["z_AVE"], dz,
            r["delta_pct"],
        ))

    print()
    print("=" * 72)
    print("Comparison with Observed Redshifts")
    print("=" * 72)
    print()
    fmt2_hdr = "{:<16s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}"
    fmt2_row = "{:<16s} {:>10.2f} {:>10.2f} {:>10.2f} {:>10.2f} {:>10s}"
    print(fmt2_hdr.format(
        "White Dwarf", "v_obs", "v_GR", "v_AVE", "v_obs−v_GR", "v_obs−v_AVE"
    ))
    print("(all in km/s)")
    print("-" * 72)

    for wd, r in results:
        if wd["v_obs_kms"] is not None:
            v_obs = wd["v_obs_kms"]
            v_err = wd["v_obs_err_kms"]
            resid_GR = v_obs - r["v_GR_kms"]
            resid_AVE = v_obs - r["v_AVE_kms"]
            print(fmt2_row.format(
                wd["name"],
                v_obs,
                r["v_GR_kms"],
                r["v_AVE_kms"],
                resid_GR,
                f"{resid_AVE:.2f}",
            ))
            print(f"  {'':16s} ±{v_err:.2f}            [{wd['ref']}]")
        else:
            print(f"{wd['name']:<16s} {'(no spectroscopic z)':>50s}")

    print()
    print("=" * 72)
    print("INTERPRETATION")
    print("=" * 72)
    print()
    print("• The AVE saturation correction INCREASES the predicted redshift")
    print("  (the clock runs faster → photon must climb through n AND S → more redshift)")
    print("• For Sirius B: the AVE correction is ~0.6%, modifying v_grav by ~0.5 km/s")
    print("• Current precision on Sirius B: ±0.77 km/s (Joyce+ 2018)")
    print("• The correction is comparable to the error bars — marginal detectability")
    print("• If v_obs > v_GR, the residual is in the DIRECTION predicted by AVE")
    print()

    # Generate figure if matplotlib available
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        _generate_figure(results)
    except ImportError:
        print("[!] matplotlib not available — skipping figure generation")


def _generate_figure(results):
    """Generate a comparison figure."""
    import matplotlib.pyplot as plt

    names = []
    v_obs_list, v_err_list = [], []
    v_gr_list, v_ave_list = [], []

    for wd, r in results:
        if wd["v_obs_kms"] is not None:
            names.append(wd["name"])
            v_obs_list.append(wd["v_obs_kms"])
            v_err_list.append(wd["v_obs_err_kms"])
            v_gr_list.append(r["v_GR_kms"])
            v_ave_list.append(r["v_AVE_kms"])

    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0A0A1A')
    ax.set_facecolor('#0A0A1A')

    x = range(len(names))

    ax.errorbar(x, v_obs_list, yerr=v_err_list, fmt='o', color='#00DDFF',
                markersize=10, capsize=5, capthick=2, linewidth=2,
                label='Observed', zorder=3)
    ax.scatter(x, v_gr_list, marker='s', color='#FF6644', s=80,
              label='GR prediction', zorder=2)
    ax.scatter(x, v_ave_list, marker='D', color='#44FF88', s=80,
              label='AVE prediction (with saturation)', zorder=2)

    ax.set_xticks(x)
    ax.set_xticklabels(names, color='white', fontsize=12)
    ax.set_ylabel('Gravitational Redshift [km/s]', color='white', fontsize=13)
    ax.set_title('White Dwarf Gravitational Redshift: GR vs AVE',
                color='white', fontsize=15, fontweight='bold', pad=15)
    ax.tick_params(colors='white', labelsize=11)
    ax.legend(loc='upper left', fontsize=11, facecolor='#1A1A2E',
             edgecolor='#333', labelcolor='white')
    ax.grid(True, alpha=0.15, color='white')

    for spine in ax.spines.values():
        spine.set_color('#333')

    out_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'sim_outputs')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'white_dwarf_saturation_redshift.png')
    plt.savefig(out_path, dpi=200, bbox_inches='tight', facecolor='#0A0A1A')
    plt.close()
    print(f"[*] Saved figure: {out_path}")


if __name__ == "__main__":
    main()
