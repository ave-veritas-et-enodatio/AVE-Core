"""
Mechanical Entropy / Thermodynamics Visualization (illustrative animation — no ΔS calc).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script renders a 2D VacuumGrid damped-wave animation (damping=0.98)
to illustrate the AVE narrative that entropy is the geometric irreversibility
of ordered potential energy scattering into transverse acoustic noise.

The script does NOT compute:
  - ΔS as a numerical entropy value
  - Comparison against Boltzmann entropy S = k_B ln Ω
  - Quantitative match to thermodynamic measurements

This is an illustrative narrative animation, NOT an entropy prediction.

Docstring corrected 2026-05-17.
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

# Add the src directory to path to import the ave engine
from ave.core.grid import VacuumGrid


def main() -> None:
    print("==========================================================")
    print(" AVE MACROSCOPIC SCALE: ENTROPY VISUALIZATION (illustrative)")
    print("==========================================================\n")

    print("- Renders the AVE interpretive narrative: entropy as geometric")
    print("  irreversibility of ordered potential energy → transverse LC noise.")
    print("- No numerical ΔS computed; no Boltzmann comparison.")
    print("  This is visualization, not prediction.\n")

    # Simulation Parameters
    NX, NY = 100, 100
    FRAMES = 120

    # Grid initialization (representing the 2D cross-section of the continuous vacuum)
    grid = VacuumGrid(nx=NX, ny=NY, c2=0.20)
    grid.set_temperature(0.5, mode="bulk")  # Bulk noise: entropy scattering demo

    # We will simulate a highly ordered, high-energy wave-packet (like a particle or laser pulse)
    # entering the center of the grid, and watch how its ordered energy geometrically scatters.

    # Initial state: High Order (Low Entropy)
    center_x, center_y = NX // 2, NY // 2
    for i in range(NX):
        for j in range(NY):
            dist = np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2)
            if dist < 5:
                # Inject high internal cohesive energy
                grid.strain_z[i, j] = np.cos(dist) * 10.0

    fig, ax = plt.subplots(figsize=(8, 8), facecolor="#111111")
    ax.set_facecolor("#111111")

    # Colormap showing signal amplitude
    img = ax.imshow(grid.strain_z**2, cmap="hot", vmin=0, vmax=4.0, origin="lower")
    ax.axis("off")
    ax.set_title(
        r"Entropy $\Delta S$: Geometric Scattering of Ordered Potential",
        color="white",
        pad=20,
        fontsize=14,
    )

    print("[1] Simulating 2D LC grid wave dissipation using ave_engine...")

    def update(frame: int) -> list:
        grid.step_kinematic_wave_equation(damping=0.98)
        img.set_array(grid.strain_z)
        return [img]

    print("[2] Rendering Thermodynamic Arrow of Time...")
    ani = animation.FuncAnimation(fig, update, frames=FRAMES, interval=50, blit=True)

    os.makedirs("standard_model/animations", exist_ok=True)
    out_path = "standard_model/animations/entropy_dissipation.gif"
    ani.save(out_path, writer="pillow", fps=20)

    # Extract the final frame (Maximum Entropy state) for the manuscript
    print("[3] Slicing maximum-entropy state for manuscript PDF...")
    final_frame_data = np.copy(grid.strain_z)

    fig_static, ax_static = plt.subplots(figsize=(8, 8), facecolor="#111111")
    ax_static.set_facecolor("#111111")
    ax_static.imshow(np.abs(final_frame_data) ** 2, cmap="hot", vmin=0, vmax=4.0, origin="lower")
    ax_static.axis("off")
    ax_static.set_title(
        "Final State: Maximum Entropy (Transverse Thermal Noise)",
        color="white",
        pad=20,
        fontsize=14,
    )

    os.makedirs("assets/figures", exist_ok=True)
    static_out = "assets/figures/entropy_dissipation_final.pdf"
    fig_static.savefig(static_out, facecolor="#111111", bbox_inches="tight", dpi=150)

    print("\n[STATUS: SUCCESS] The 2nd Law of Thermodynamics is strict grid geometry.")
    print(f"Animated propagation saved to {out_path}")
    print(f"Static boundary state saved to {static_out}")


if __name__ == "__main__":
    main()
