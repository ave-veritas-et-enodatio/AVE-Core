"""
AVE Framework: Cosmological Equilibrium Visualization (illustrative — NOT a derivation driver).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script visualizes the AVE narrative that H(t) settles to a steady-state
H_∞ ≈ 69.32 km/s/Mpc via thermodynamic equilibrium between latent-heat
generation and holographic boundary cooling. The H_∞ value is imported from
`ave.core.constants.H_INFINITY` (the canonical H_0 = 28π × M_E^3 × C_0 × G /
(ℏ^2 α^2), in SI s⁻¹) and converted to km/s/Mpc here. This script does NOT
re-derive that value — it plots a phenomenological exponential approach
`H(t) = H_∞ × (1 − exp(−t))` for pedagogical illustration.

Specifically:
  - H_baseline = H_INFINITY × (Mpc in km) — sourced from constants.py, not re-derived
  - The exponential approach curve is phenomenological (NOT axiom-derived)
  - G_normalized(t) is a normalized illustration, not a G derivation

For the actual AVE derivation of H_0 and G, see:
  - simulate_cosmology_bao.py (zero-parameter derivation chain)
  - simulate_vacuum_mirror.py (G from K=2G operating point)

Title "Deriving Macroscopic Gravity (G)" was misleading; corrected to
"Cosmological Equilibrium Visualization" 2026-05-17. The narrative still
serves the manuscript's pedagogical purpose, with honest scope.

FIGURE-STYLE: restyled to the AVE house style (ave.viz.style) 2026-06-21.
H_∞ continues to come from ave.core.constants.H_INFINITY; the approach curve
and normalized-G curve remain phenomenological/illustrative (no value change).
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import H_INFINITY
from ave.viz import style
from ave_path_util import sim_output

style.apply("print")

# Megaparsec in km, for converting H_∞ from SI [s⁻¹] to astronomical [km/s/Mpc].
# 1 Mpc = 3.0856775814913673e22 m = 3.0856775814913673e19 km (IAU 2015).
_MPC_IN_KM = 3.0856775814913673e19


def simulate_cosmological_equilibrium() -> None:
    """
    Simulates the heat equation of the expanding lattice.
    Latent heat generation scales with Volume (R^3).
    Boundary radiation cooling scales with Surface Area (R^2) or Holographic bounds (R).
    The universe accelerates until these two curves intersect, determining the
    permanent cosmological horizon R_H, which in turn fixes G.
    """
    print("==========================================================")
    print("   AVE FRAMEWORK: COSMOLOGICAL EQUILIBRIUM VISUALIZATION   ")
    print("   (illustrative — H_∞ literal from simulate_cosmology_bao)")
    print("==========================================================")

    # 1. Theoretical Setup
    # Generative Cosmology defines expansion as state-change (crystallization).
    # Power generated P_gen = k_g * d(Volume)/dt
    # Power radiated P_cool = k_c * Surface_Area

    # Using arbitrary structural units to demonstrate the algebraic intersection
    # where the derivative of expansion becomes zero (Steady State limit)

    time_steps = np.linspace(0.1, 10.0, 500)

    # Phenomenological model of latent heat thermal back-pressure
    # Early universe: high temperature, slow crystallization
    # Late universe: cold, fast crystallization approaching equilibrium

    # Expansion Rate (Hubble Parameter H)
    # Starts low (CMB phase), accelerates, then asymptotes to H_infinity.
    # H_baseline is the canonical asymptotic Hubble constant H_∞ = 28π × M_E³ ×
    # C_0 × G / (ℏ² α²), imported from constants.py (SI s⁻¹) and converted to
    # km/s/Mpc here. Evaluates to ≈ 69.32 km/s/Mpc.
    H_baseline = H_INFINITY * _MPC_IN_KM

    # Modeled acceleration curve based on thermodynamic cooling
    H_t = H_baseline * (1.0 - np.exp(-time_steps))

    # The effective measured G is inversely proportional to the expansion boundary
    # G_eff(t) = c^3 / (M_universe * H_t)
    # Here we plot the normalized stabilization of the geometric tensor
    G_normalized = 1.0 / (1.0 - 0.9 * np.exp(-time_steps))

    print("Plotting phenomenological approach to thermodynamic equilibrium...")
    print(f"H_∞ (from constants.H_INFINITY): {H_baseline:.2f} km/s/Mpc")
    print("(Canonical AVE claim: equilibrium R_H fixes G via G = c^3/(M_universe·H_∞);")
    print("  G-derivation chain lives in simulate_cosmology_bao.py + simulate_vacuum_mirror.py)")

    # 2. Visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=style.figsize("wide"))

    # ----- Plot 1: The Hubble Acceleration to Equilibrium -----
    ax1.plot(
        time_steps,
        H_t,
        color=style.COLORS["ave"],
        linewidth=2.5,
        label=r"Topological genesis rate $H(t)$",
    )
    ax1.axhline(
        H_baseline,
        color=style.COLORS["muted"],
        linestyle="--",
        label=r"Thermodynamic limit ($H_0 \approx 69.32$)",
    )

    ax1.set_xlabel(style.axis_label("Cosmological time", "t", "arb."))
    ax1.set_ylabel(style.axis_label("Expansion rate", "H(t)", "km/s/Mpc"))
    style.legend(ax1, where="below", fontsize=8)
    ax1.grid(True, alpha=0.3)

    # ----- Plot 2: The Stabilization of Macroscopic G -----
    ax2.plot(
        time_steps,
        G_normalized,
        color=style.COLORS["accent"],
        linewidth=2.5,
        label=r"Effective macroscopic tensor $G(t)$",
    )
    ax2.axhline(
        1.0,
        color=style.COLORS["muted"],
        linestyle="--",
        label=r"Present-day fundamental constant ($G_0$)",
    )

    ax2.set_xlabel(style.axis_label("Cosmological time", "t", "arb."))
    ax2.set_ylabel(style.axis_label("Normalized coupling", "G(t)/G_0", ""))
    style.legend(ax2, where="below", fontsize=8)
    ax2.grid(True, alpha=0.3)

    # Save the output
    output_path = sim_output("simulate_cosmological_equilibrium.png")
    style.save(fig, output_path)
    plt.close(fig)

    print(f"\nSaved cosmological equilibrium plot to {output_path}")
    print("\nNOTE: Plot is illustrative — H_∞ is a literal from simulate_cosmology_bao.py;")
    print("approach curve is phenomenological. G(t) is normalized for visual comparison,")
    print("not derived. The underlying AVE claim (G = c^3/(M_universe·H_∞), equilibrium")
    print("between latent-heat generation and holographic boundary cooling) is canonical.")


if __name__ == "__main__":
    simulate_cosmological_equilibrium()
