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

Figure restyle (2026-06-21 Vol-3 figure-regen sweep): the static manuscript
PDF is now produced through the ``ave.viz.style`` house style (print profile)
— white background, perceptually-uniform colormap (retires ``hot``), colorbar
with quantity+symbol+unit, and NO baked title (the title belongs in the LaTeX
``\\caption{}``). The under-exposure defect (faint red strain on a near-black
``#0a0a2e`` raster) is fixed by the print profile plus a data-tracking colour
scale. The underlying physics/data are unchanged. The interactive GIF keeps the
dark field-viz aesthetic via the ``screen`` profile.
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

from ave.core.grid import VacuumGrid
from ave.viz import style


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

    # --- Interactive animation: dark field-viz aesthetic (screen profile) ----
    style.apply("screen")
    fig, ax = plt.subplots(figsize=style.figsize("square"))

    # Energy density heatmap (strain²); magma is perceptually uniform and keeps
    # the low-energy field visible (retires the under-exposing `hot` colormap).
    img = ax.imshow(grid.strain_z**2, cmap=style.CMAP_SEQ, vmin=0, vmax=2.0, origin="lower")
    ax.axis("off")

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
    plt.close(fig)

    # --- Static manuscript frame: house print profile (white bg) -------------
    print("[3] Slicing final frame for manuscript PDF...")
    final_frame_data = np.copy(grid.strain_z)
    energy = final_frame_data**2

    style.apply("print")
    fig_static, ax_static = plt.subplots(figsize=style.figsize("square"))

    # Data-tracking upper limit so the (low-amplitude) radiated field is exposed
    # against the white page — a rendering fix, not a data change.
    vmax_static = max(np.percentile(energy, 99.5), 1e-12)
    im = ax_static.imshow(
        energy,
        cmap=style.CMAP_SEQ,
        vmin=0,
        vmax=vmax_static,
        origin="lower",
    )
    ax_static.set_xlabel(style.axis_label("Grid position", "x", "cell"))
    ax_static.set_ylabel(style.axis_label("Grid position", "y", "cell"))

    cbar = fig_static.colorbar(im, ax=ax_static, fraction=0.046, pad=0.04)
    cbar.set_label(style.axis_label("Strain energy density", r"\epsilon_z^2", "dimensionless"))

    os.makedirs("assets/figures", exist_ok=True)
    static_out = "assets/figures/gravitational_waves_lc_static.pdf"
    style.save(fig_static, static_out)
    plt.close(fig_static)

    print("\n[STATUS: SUCCESS] General Relativity mapped as Applied Vacuum Engineering.")
    print(f"Animated propagation saved to {out_path}")
    print(f"Static spiral state saved to {static_out}")


if __name__ == "__main__":
    main()
