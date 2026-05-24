"""
AVE Asteroid Belt and Oort Cloud Accumulation — illustrative (Gaussians pre-placed).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script renders an illustrative inductive-drag profile around the Sun
using two GAUSSIANS CENTERED BY HAND at known empirical accumulation
locations: 2.5 AU (asteroid belt centroid) and 10^4.2 AU (Oort cloud
centroid). The visualization supports the AVE narrative that the impedance
slipstream falls off as 1/r and hits Z_0 background at these boundaries —
but the script does NOT DERIVE the boundary locations from the Sun's
solar-strain gradient. It pre-positions them at empirical observation
sites.

A genuine AVE falsification protocol would compute:
  - The exact 1/r → Z_0 transition radius from solar GM and substrate
    impedance Z_0 (= sqrt(μ_0/ε_0))
  - Predict the accumulation centroid WITHOUT inputting the empirical 2.5 AU
  - Match the predicted vs observed boundary within some tolerance

That derivation lives in the queue (parallel to SPARC ingest pattern for
the solar-system sector). This script remains illustrative until the
derivation closes.

Docstring corrected 2026-05-17: was "Falsification Protocol" — softened
to "Illustrative accumulation visualization" since the Gaussian centers
are inputs, not predictions.
"""

import os

import matplotlib.pyplot as plt
import numpy as np


def simulate_accumulation_boundaries() -> None:
    print("==========================================================")
    print(" AVE MACRO-FLUIDICS: OORT CLOUD DETRITUS TRAPPING")
    print("==========================================================")

    # Radial distance from the Sun (Astronomical Units - AU)
    # Log scale to capture both Asteroid Belt (~2-3 AU) and Oort Cloud (~10,000 AU)
    r = np.logspace(-1, 5, 2000)

    # 1. Solar Gravitational Phase Strain (Simplified)
    # Scales as 1/r, fading into the cosmic background
    strain_solar = 100.0 / r
    strain_background = 0.05  # Galactic baseline

    # The actual encountered strain is the transition between the two
    strain_total = np.maximum(strain_solar, strain_background)

    # 2. Impedance Transition (Inductive Drag / Friction Profile)
    # The drag coefficient spikes severely where the gradient changes abruptly.
    # In fluidic terms, this is the sheer layer where the solar slipstream rubs against
    # the static deep-space vacuum.
    # We take the derivative of the strain to find the transition sheer.

    # Smooth transition derivative proxy:
    # High transition gradient happens where Solar Strain crosses Background Strain

    # Asteroid belt happens where inner-solar radiation pressure aligns with gravity rupture
    # Oort cloud happens at the absolute termination boundary (Heliopause equivalent)

    # We model the Inductive Drag (Energy Shedding Rate) as a non-linear spike
    # at the cross-over boundaries.

    # Model 1: The Inner boundary (Asteroid Belt cross-over ~ 2.5 AU)
    drag_asteroid = np.exp(-1.0 * (r - 2.5) ** 2)

    # Model 2: The Outer boundary (Oort/Heliopause cross-over ~ 10^4 AU)
    drag_oort = np.exp(-0.005 * (np.log10(r) - 4.2) ** 2)

    drag_total = drag_asteroid + drag_oort

    # Detritus Accumulation Probability is heavily correlated to Drag Spikes
    trap_prob = drag_total / np.max(drag_total)

    # --- Visualization ---
    fig, ax1 = plt.subplots(figsize=(14, 7), facecolor="#0B0F19")
    fig.suptitle(
        "AVE Topological Trapping: Orbital Detritus Accumulation",
        color="white",
        fontsize=20,
        weight="bold",
        y=0.95,
    )

    ax1.set_facecolor("#0B0F19")

    # Plot the background strain
    ax1.loglog(r, strain_total, color="cyan", lw=3, label=r"Solar Dielectric Strain Field ($h_\perp$)")
    ax1.axhline(strain_background, color="gray", ls="--", label="Galactic Background Impedance Floor")

    ax1.set_xlabel("Orbital Radius from Sun (AU)", color="gray", fontsize=12)
    ax1.set_ylabel("Normalized Metric Strain Magnitude", color="cyan", fontsize=12)
    ax1.tick_params(axis="y", labelcolor="cyan", colors="gray")
    ax1.tick_params(axis="x", colors="gray")
    ax1.set_ylim(1e-2, 1e4)

    # Twin axis for the Accumulation Probability
    ax2 = ax1.twinx()
    ax2.fill_between(r, 0, trap_prob, color="#FF3366", alpha=0.3)
    ax2.plot(
        r,
        trap_prob,
        color="#FF3366",
        lw=3,
        label="Inductive Drag (Detritus Accumulation Probability)",
    )

    ax2.set_ylabel("Detritus Trapping Probability (0-100%)", color="#FF3366", fontsize=12)
    ax2.tick_params(axis="y", labelcolor="#FF3366")
    ax2.set_ylim(0, 1.2)

    # Annotations
    ax2.axvline(2.5, color="white", linestyle=":", alpha=0.5)
    ax2.text(
        2.5,
        1.05,
        "Asteroid Belt\n(Inner Slipstream Ring)",
        color="white",
        ha="center",
        weight="bold",
    )

    ax2.axvline(15000, color="white", linestyle=":", alpha=0.5)
    ax2.text(
        15000,
        1.05,
        "Oort Cloud\n(Termination Bow Shock)",
        color="white",
        ha="center",
        weight="bold",
    )

    # Legends
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(
        lines + lines2,
        labels + labels2,
        loc="upper right",
        facecolor="#111111",
        edgecolor="gray",
        labelcolor="white",
    )

    ax1.grid(True, ls=":", color="#333333", alpha=0.5)
    for ax in [ax1, ax2]:
        for spine in ax.spines.values():
            spine.set_color("#333333")

    plt.tight_layout(rect=[0, 0.03, 1, 0.92])

    # --- Standard AVE output directory ---


def _find_repo_root() -> str:
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, "pyproject.toml")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.abspath(__file__))


OUTPUT_DIR = os.path.join(_find_repo_root(), "assets", "sim_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
# --- End standard output directory ---

if __name__ == "__main__":
    simulate_accumulation_boundaries()
