"""
simulate_optical_caustic.py
Volume 4 Engineering: Optical Caustic Resolution Demonstration

This script demonstrates how Axiom 4 saturation boundaries prevent classical 
infinite-intensity focal points. It computes the actual focal intensity using
the 1D transmission line solver (`AxiomaticCausticSolver`).

Classical ray optics predicts: E ~ 1/z, Area ~ z^2.
Axiomatic optics demonstrates impedance reflection diffusing the focal point.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from ave.regime_4_rupture.caustic_solver import AxiomaticCausticSolver
from ave.core.constants import E_YIELD, Z_0


def main():
    solver = AxiomaticCausticSolver()

    # 10 Petawatt conceptual laser focusing
    # We want to show a clear divergence in classical vs AVE regimes
    initial_power = 10e15  # Watts
    NA = 0.5

    # We will simulate the last 10 microns of focus
    z_start = 10e-6
    z_end = 1e-18
    num_steps = 2000

    print("Running Axiomatic Caustic Solver...")
    result = solver.resolve_focal_intensity(
        initial_power=initial_power,
        numerical_aperture=NA,
        z_start=z_start,
        z_end=z_end,
        num_steps=num_steps,
    )

    z_vals = result["z"]

    # Calculate classical predictions
    area_classical = np.pi * (z_vals * NA) ** 2
    # Prevent divide by zero warning in classical calculation
    safe_area = np.maximum(area_classical, 1e-30)
    E_classical = np.sqrt(2.0 * Z_0 * initial_power / safe_area)

    # Prepare plot
    plt.style.use("dark_background")
    fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

    # Convert z to nanometers for easier reading
    z_nm = z_vals * 1e9

    # Plot 1: Electric Field
    ax1 = axes[0]
    ax1.plot(z_nm, E_classical, "w--", alpha=0.5, label="Classical Ray Optics (Infinite)")
    ax1.plot(z_nm, result["E_field"], "c-", linewidth=2, label="AVE Axiomatic Limit")
    ax1.axhline(E_YIELD, color="r", linestyle=":", label="E_YIELD Limit")
    ax1.set_ylabel("Electric Field [V/m]")
    ax1.set_yscale("log")
    ax1.set_title("Optical Caustic Singularity Resolution")
    ax1.legend()
    ax1.grid(alpha=0.2)

    # Plot 2: Impedance and Reflection
    ax2 = axes[1]
    color = "tab:orange"
    ax2.set_ylabel("Effective Impedance Z_eff [Ohm]", color=color)
    ax2.plot(z_nm, result["Z_eff"], color=color, linewidth=2)
    ax2.tick_params(axis="y", labelcolor=color)
    ax2.set_yscale("log")

    ax2_twin = ax2.twinx()
    color = "tab:pink"
    ax2_twin.set_ylabel("Reflection Coefficient Gamma", color=color)
    ax2_twin.plot(z_nm, result["Gamma"], color=color, linestyle="--")
    ax2_twin.tick_params(axis="y", labelcolor=color)
    ax2_twin.set_ylim(0, 1.1)

    # Plot 3: Power Transmission
    ax3 = axes[2]
    ax3.plot(z_nm, result["power"] / 1e15, "g-", linewidth=2, label="Transmitted Power")
    ax3.plot(
        z_nm,
        np.full_like(z_vals, initial_power / 1e15),
        "w--",
        alpha=0.5,
        label="Classical Constant Power",
    )
    ax3.set_ylabel("Beam Power [Petawatts]")
    ax3.set_xlabel("Distance from Geometric Focus z [nm]")
    ax3.invert_xaxis()  # Beam travels towards z=0
    ax3.legend()
    ax3.grid(alpha=0.2)

    plt.tight_layout()

    # Save output
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "optical_caustic_resolution.png")
    plt.savefig(out_path, dpi=300)
    print(f"Saved visualization to: {out_path}")


if __name__ == "__main__":
    main()
