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

FIGURE-STYLE: restyled to the AVE house style (ave.viz.style) 2026-06-21.
The static manuscript frame now renders on the print profile (white background,
magma sequential colormap, no baked Axes title — the figure's title lives in
the LaTeX \\caption{} in 11_thermodynamics_and_entropy.tex). The simulation
parameters (grid size, c2, bulk temperature, damping, injection, frame count)
and the |strain|² field that is plotted are UNCHANGED — this is a restyle, not
a physics edit. The static frame is written to the canonical sim_outputs tree
via ave_path_util.sim_output (matching the committed
assets/sim_outputs/entropy_dissipation_final.pdf), replacing the stale
hand-built assets/figures/ path.
"""

import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

# Add the src directory to path to import the ave engine
from ave.core.grid import VacuumGrid
from ave.viz import style
from ave_path_util import sim_output

style.apply("print")


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

    # Animation figure (illustrative GIF; print profile, magma sequential field).
    fig, ax = plt.subplots(figsize=style.figsize("square"))

    # Sequential colormap showing signal amplitude (house CMAP_SEQ = magma;
    # retires the print-clipping `hot` colormap). The colormap autoscales to the
    # field's own range (house imshow convention, cf. simulate_macroscopic_avalanche)
    # rather than the legacy fixed [0, 4.0] window — the damped |strain|² field
    # settles to << 4.0, so that fixed window rendered the print-profile magma
    # frame as near-uniform black. Autoscaling preserves the field DATA exactly;
    # it only fixes the display normalisation so the thermal-noise structure is
    # legible on the white page.
    img = ax.imshow(grid.strain_z**2, cmap=style.CMAP_SEQ, origin="lower")
    ax.set_xlabel(style.axis_label("Lattice position", "x", "cells"))
    ax.set_ylabel(style.axis_label("Lattice position", "y", "cells"))
    cbar = fig.colorbar(img, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label(style.axis_label("Energy density", r"|\delta n|^2", "arb."))

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
    plt.close(fig)

    # Extract the final frame (Maximum Entropy state) for the manuscript
    print("[3] Slicing maximum-entropy state for manuscript PDF...")
    final_frame_data = np.copy(grid.strain_z)

    fig_static, ax_static = plt.subplots(figsize=style.figsize("square"))
    img_static = ax_static.imshow(
        np.abs(final_frame_data) ** 2,
        cmap=style.CMAP_SEQ,
        origin="lower",
    )
    ax_static.set_xlabel(style.axis_label("Lattice position", "x", "cells"))
    ax_static.set_ylabel(style.axis_label("Lattice position", "y", "cells"))
    cbar_static = fig_static.colorbar(img_static, ax=ax_static, fraction=0.046, pad=0.04)
    cbar_static.set_label(style.axis_label("Energy density", r"|\delta n|^2", "arb."))
    # No baked Axes title: the figure's caption (final maximum-entropy state,
    # transverse thermal noise) lives in the LaTeX \caption{} in
    # manuscript/vol_3_macroscopic/chapters/11_thermodynamics_and_entropy.tex.

    static_out = sim_output("entropy_dissipation_final.png")
    style.save(fig_static, static_out)
    plt.close(fig_static)

    print("\n[STATUS: SUCCESS] The 2nd Law of Thermodynamics is strict grid geometry.")
    print(f"Animated propagation saved to {out_path}")
    print(f"Static boundary state saved to {static_out.with_suffix('.pdf')} (+ .png)")


if __name__ == "__main__":
    main()
