#!/usr/bin/env python3
"""
Black Hole as Macroscopic Electron Orbital — Visualisation
==========================================================

Generates a multi-panel figure demonstrating the scale-invariant
isomorphism between electron orbitals and black hole accretion disks
within the AVE impedance framework.

Panels:
  1. Reflection coefficient Γ(r):  smooth transition from flat space
     (Γ ≈ 0) through the photon sphere to the event horizon (Γ → +1).
  2. Quantised impedance band radii overlaid on refractive index n(r).
  3. QPO frequency predictions for GRS 1915+105 and Sgr A*.

All constants from ave.core.constants — zero free parameters.
"""

import os

import matplotlib.pyplot as plt
import numpy as np

# Ensure local ave package is in path
from ave.solvers.orbital_resonance import (
    M_SUN,
    impedance_orbital_radii,
    isco_radius,
    photon_sphere_radius,
    qpo_frequencies,
    reflection_coefficient,
    refractive_index,
    schwarzschild_radius,
)

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
# Standard AVE output directory
OUTPUT_DIR = os.path.join(project_root, "assets", "sim_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.style.use("dark_background")


def main():
    print("=" * 70)
    print("  BLACK HOLE AS MACROSCOPIC ELECTRON ORBITAL")
    print("  AVE Impedance Resonance Visualisation")
    print("=" * 70)

    # ── Target: GRS 1915+105 (14 M☉, a*≈0.7) ──
    M_grs = 14.0 * M_SUN
    a_grs = 0.7
    rs_grs = schwarzschild_radius(M_grs)
    rph_grs = photon_sphere_radius(M_grs)
    risco_grs = isco_radius(M_grs, a_grs)

    # ── Target: Sgr A* (4×10⁶ M☉, a*≈0.5) ──
    # M_sgr = 4.0e6 * M_SUN  # bulk lint fixup pass
    # a_sgr = 0.5  # bulk lint fixup pass

    # ─────────────────────────────────────────────
    # Figure: 3-panel diagnostic
    # ─────────────────────────────────────────────
    fig, axes = plt.subplots(1, 3, figsize=(22, 7))
    fig.patch.set_facecolor("#0a0a1a")
    for ax in axes:
        ax.set_facecolor("#0a0a1a")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 1: Reflection Coefficient Γ(r)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax1 = axes[0]
    r_norm = np.linspace(0.55, 15.0, 2000)  # in units of r_s
    r_phys = r_norm * rs_grs

    gamma_vals = reflection_coefficient(r_phys, M_grs)

    ax1.plot(r_norm, gamma_vals, color="#00ccff", linewidth=2.5, label=r"$\Gamma(r) = \frac{n-1}{n+1}$")

    # Mark key radii
    ax1.axvline(1.0, color="red", linestyle="--", alpha=0.8, label=r"Event Horizon ($r_s$)")
    ax1.axvline(
        rph_grs / rs_grs,
        color="#ffaa00",
        linestyle="--",
        alpha=0.8,
        label=r"Photon Sphere ($r_{ph}$)",
    )
    ax1.axvline(risco_grs / rs_grs, color="#00ff88", linestyle="--", alpha=0.8, label=r"ISCO")

    # Electron comparison annotation
    ax1.axhline(1.0, color="white", linestyle=":", alpha=0.3)
    ax1.text(8.0, 0.95, r"$\Gamma \to +1$ (Black Hole)", color="white", fontsize=10, alpha=0.6)
    ax1.text(8.0, 0.05, r"$\Gamma \to -1$ (Electron)", color="#ff66cc", fontsize=10, alpha=0.6)

    ax1.set_xlabel(r"$r / r_s$", fontsize=13, color="white")
    ax1.set_ylabel(r"Reflection Coefficient $\Gamma$", fontsize=13, color="white")
    ax1.set_title("Impedance Boundary:\nElectron vs. Black Hole", fontsize=14, color="white", pad=12)
    ax1.set_xlim(0.5, 15)
    ax1.set_ylim(-0.05, 1.1)
    ax1.legend(fontsize=9, loc="center right")
    ax1.grid(True, alpha=0.15)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 2: Refractive Index + Impedance Bands
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax2 = axes[1]
    n_vals = refractive_index(r_phys, M_grs)

    ax2.plot(r_norm, n_vals, color="#ff6600", linewidth=2.5, label=r"$n(r) = W^3/U$")

    # Overlay quantised impedance bands
    band_radii, band_modes = impedance_orbital_radii(M_grs, a_grs, n_modes=6)
    for i, (br, bm) in enumerate(zip(band_radii, band_modes)):
        br_norm = br / rs_grs
        n_at_band = refractive_index(np.array([br]), M_grs)[0]
        color = plt.cm.viridis(i / 6.0)
        ax2.axvline(br_norm, color=color, linestyle="-", alpha=0.6, linewidth=1.5)
        ax2.plot(br_norm, n_at_band, "o", color=color, markersize=8, zorder=5)
        ax2.text(br_norm + 0.15, n_at_band + 0.08, f"n={bm}", color=color, fontsize=9, fontweight="bold")

    ax2.axvline(1.0, color="red", linestyle="--", alpha=0.5)
    ax2.axvline(rph_grs / rs_grs, color="#ffaa00", linestyle="--", alpha=0.5)

    ax2.set_xlabel(r"$r / r_s$", fontsize=13, color="white")
    ax2.set_ylabel(r"Refractive Index $n(r)$", fontsize=13, color="white")
    ax2.set_title("Quantised Impedance Bands\n(Standing-Wave Resonance)", fontsize=14, color="white", pad=12)
    ax2.set_xlim(0.5, 30)
    ax2.set_ylim(0.9, 5.0)
    ax2.legend(fontsize=10, loc="upper right")
    ax2.grid(True, alpha=0.15)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 3: QPO Frequency Predictions
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax3 = axes[2]

    # GRS 1915+105
    freqs_grs, radii_grs, ratios_grs = qpo_frequencies(M_grs, a_grs, n_modes=6)
    modes_grs = np.arange(1, len(freqs_grs) + 1)

    ax3.plot(
        modes_grs,
        freqs_grs,
        "o-",
        color="#00ccff",
        markersize=10,
        linewidth=2,
        label="GRS 1915+105 (14 M☉)",
        zorder=5,
    )

    # Observed QPOs for GRS 1915+105
    # observed_qpo_grs = [67.0, 113.0]  # bulk lint fixup pass
    # observed_modes_grs = [1, 2]  # bulk lint fixup pass
    ax3.scatter(
        [1],
        [67.0],
        color="red",
        s=150,
        marker="*",
        zorder=10,
        label="Observed: 67 Hz",
        edgecolors="white",
        linewidths=0.5,
    )
    ax3.scatter(
        [2],
        [113.0],
        color="#ff4444",
        s=150,
        marker="*",
        zorder=10,
        label="Observed: 113 Hz",
        edgecolors="white",
        linewidths=0.5,
    )

    # Annotate ratio
    if len(freqs_grs) >= 2:
        ratio_12 = freqs_grs[0] / freqs_grs[1]
        ax3.text(
            1.5,
            max(freqs_grs[0], 80),
            f"Predicted ν₁/ν₂ = {ratio_12:.2f}\nObserved = {113/67:.2f}",
            color="white",
            fontsize=10,
            ha="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#1a1a3a", alpha=0.8),
        )

    ax3.set_xlabel("Mode Number $n$", fontsize=13, color="white")
    ax3.set_ylabel("QPO Frequency [Hz]", fontsize=13, color="white")
    ax3.set_title("QPO Frequency Prediction\nvs. Observed X-ray Data", fontsize=14, color="white", pad=12)
    ax3.set_yscale("log")
    ax3.legend(fontsize=9, loc="upper right")
    ax3.grid(True, alpha=0.15, which="both")

    # ── Final layout ──
    plt.tight_layout(pad=2.0)

    # Supertitle
    fig.suptitle(
        r"$\mathbf{Black\ Holes\ as\ Macroscopic\ Electron\ Orbitals}$" + "\n"
        r"AVE Impedance Resonance — Same $1/d$ Topology at $10^{40}$ Scale Ratio",
        color="white",
        fontsize=16,
        y=1.02,
    )

    out_path = os.path.join(OUTPUT_DIR, "bh_orbital_resonance.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(f"\n[*] Saved figure: {out_path}")

    # ── Console summary ──
    print("\n  GRS 1915+105 (14 M☉, a*=0.7):")
    print(f"    Mode 1 predicted: {freqs_grs[0]:.1f} Hz  (observed: 67 Hz)")
    if len(freqs_grs) >= 2:
        print(f"    Mode 2 predicted: {freqs_grs[1]:.1f} Hz  (observed: 113 Hz)")
        print(f"    Predicted ratio ν₁/ν₂ = {freqs_grs[0]/freqs_grs[1]:.3f}")
        print(f"    Observed  ratio        = {113.0/67.0:.3f}")

    print("\n" + "=" * 70)
    print("  DONE")
    print("=" * 70)


if __name__ == "__main__":
    main()
