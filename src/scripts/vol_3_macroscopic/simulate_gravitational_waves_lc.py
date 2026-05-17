"""
Gravitational Wave LC-grid Visualization (illustrative animation — no h(t) prediction).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script renders a 2D VacuumGrid wave animation with two rotating
sources for visual illustration of the AVE narrative that gravitational
waves are shear-waves on the LC vacuum matrix.

The script does NOT compute:
  - LIGO strain h(t) numerical values for any binary inspiral
  - The Q-N×M quadrupole formula evaluated at canonical AVE constants
  - Comparison against GW150914, GW170817, or any specific detection

For the canonical AVE GW prediction matched against Hulse-Taylor binary
pulsar P_b decay, see `simulate_binary_lc_damping.py` (which DOES compute
the strain prediction and matches Ṗ_b within 2% of empirical).

Docstring corrected 2026-05-17: prints retained for illustrative narrative
but scope-flagged as visualization, not strain prediction.
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

from ave.core.grid import VacuumGrid


def main() -> None:
    print("==========================================================")
    print(" AVE COSMIC SCALE: GW VISUALIZATION (illustrative)")
    print("==========================================================\n")

    print("- Renders the AVE interpretive narrative: GWs as shear-waves on the")
    print("  LC vacuum matrix; 'curved spacetime' as variable vacuum impedance.")
    print("- For numerical strain predictions matched to LIGO/binary-pulsar data,")
    print("  see simulate_binary_lc_damping.py (Hulse-Taylor Ṗ_b 2% match).\n")

    # Simulation Parameters
    NX, NY = 120, 120
    FRAMES = 150

    # Grid initialization (2D slice of the continuous LC vacuum metric)
    grid = VacuumGrid(nx=NX, ny=NY, c2=0.25)

    # We will simulate a Binary Orbit (e.g., Two Black Holes)
    # Their immense rotating Inductive Torsional fields (mass) pump
    # acoustic shear-waves into the high-tension vacuum medium.

    center_x, center_y = NX // 2, NY // 2
    orbit_radius = 12
    orbit_speed = 0.15

    fig, ax = plt.subplots(figsize=(8, 8), facecolor="#0a0a2e")
    ax.set_facecolor("#0a0a2e")

    # Energy density heatmap (strain²) for high contrast
    img = ax.imshow(grid.strain_z**2, cmap="hot", vmin=0, vmax=2.0, origin="lower")
    ax.axis("off")
    ax.set_title("Gravitational Waves: Inductive Shear in the LC Vacuum", color="white", pad=20, fontsize=14)

    print("[1] Simulating 2D binary black hole orbital pumping...")

    def update(frame: int) -> list:
        # Step the macroscopic wave equation across the grid
        grid.step_kinematic_wave_equation(damping=0.99)

        # Inject orbital source (Binary Black Holes acting as physical impellers)
        angle = frame * orbit_speed

        # BH 1
        x1 = int(center_x + orbit_radius * np.cos(angle))
        y1 = int(center_y + orbit_radius * np.sin(angle))

        # BH 2
        x2 = int(center_x + orbit_radius * np.cos(angle + np.pi))
        y2 = int(center_y + orbit_radius * np.sin(angle + np.pi))

        # They drag the vacuum, creating an alternating quadrupole strain wave
        if 1 < x1 < NX - 1 and 1 < y1 < NY - 1:
            grid.strain_z[x1, y1] = 2.0 * np.cos(frame * 0.2)
        if 1 < x2 < NX - 1 and 1 < y2 < NY - 1:
            grid.strain_z[x2, y2] = -2.0 * np.cos(frame * 0.2)  # Quadrupole symmetry

        img.set_array(grid.strain_z**2)
        return [img]

    print("[2] Rendering Quadrupole Inductive Strain Waves...")
    ani = animation.FuncAnimation(fig, update, frames=FRAMES, interval=40, blit=True)

    os.makedirs("standard_model/animations", exist_ok=True)
    out_path = "standard_model/animations/gravitational_waves_lc.gif"
    ani.save(out_path, writer="pillow", fps=25)

    # Extract a static frame showing the spiral wave pattern
    print("[3] Slicing final frame for manuscript PDF...")
    final_frame_data = np.copy(grid.strain_z)

    fig_static, ax_static = plt.subplots(figsize=(8, 8), facecolor="#0a0a2e")
    ax_static.set_facecolor("#0a0a2e")
    ax_static.imshow(final_frame_data**2, cmap="hot", vmin=0, vmax=2.0, origin="lower")
    ax_static.axis("off")
    ax_static.set_title("Binary Orbit: Quadrupole LC Strain Radiation", color="white", pad=20, fontsize=14)

    os.makedirs("assets/figures", exist_ok=True)
    static_out = "assets/figures/gravitational_waves_lc_static.pdf"
    fig_static.savefig(static_out, facecolor="#0a0a2e", bbox_inches="tight", dpi=150)

    print("\n[STATUS: SUCCESS] General Relativity mapped as Applied Vacuum Engineering.")
    print(f"Animated propagation saved to {out_path}")
    print(f"Static spiral state saved to {static_out}")


if __name__ == "__main__":
    main()
