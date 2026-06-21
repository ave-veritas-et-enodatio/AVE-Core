"""
Ideal Gas Law LC Mapping — illustrative N-body (NOT a PV=nRT verification).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script runs a simple N-body hard-sphere simulation with a moving wall
to illustrate the AVE narrative that the Ideal Gas Law (PV=nRT) maps onto
LC vacuum energy density: P↔transverse ponderomotive force, V↔grid cavity,
n↔trapped topological nodes, T↔transverse RMS jitter.

The script does NOT compute:
  - PV=nRT relationship verified numerically (no P vs V/T sweep)
  - R = 8.314 J/(mol·K) recovered from the LC mapping
  - Comparison against standard kinetic theory predictions

This is an illustrative narrative animation, NOT a PV=nRT derivation. All
quantities (box size, jitter "temperature", pressure reading) are in arbitrary
illustrative units, so there is no physical constant to import here — the figure
makes no quantitative claim against canon.

Docstring corrected 2026-05-17.

FIGURE RESTYLE (2026-06-21, Vol-3 Phase-3b figure regen):
The static manuscript figure is restyled through ``ave.viz.style`` (house print
profile — white background, Okabe-Ito palette), replacing the hand-set dark
``#111111`` facecolor / white title text / cyan-magenta off-palette. The baked
"Final State: V=..., P=..." title is removed: the caption lives in the LaTeX
``\\caption{}`` of chapter 12, not in the raster (ave-figure-discipline Axis 4).
The static figure now writes to the canonical, manuscript-cited output path
``assets/sim_outputs/ideal_gas_compressed_static.pdf`` via ``ave_path_util``
(previously a stray, untracked ``assets/figures/`` path). Physics/data unchanged.
"""

import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

# Resolve the repo's src/ so `ave` + `ave_path_util` import when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ave.viz import style  # noqa: E402
from ave_path_util import sim_output  # noqa: E402


def main() -> None:
    print("==========================================================")
    print(" AVE THERMODYNAMIC SCALE: PV=nRT VISUALIZATION (illustrative)")
    print("==========================================================\n")

    print("- Renders AVE narrative: P↔ponderomotive force, V↔LC cavity,")
    print("  n↔trapped topological nodes, T↔transverse RMS jitter.")
    print("- No quantitative PV=nRT verification or R recovery.")
    print("  Illustrative animation, not derivation.\n")

    style.apply()  # house print profile (white background) FIRST

    # Simulation Parameters
    num_particles = 150
    box_size = 10.0
    dt = 0.05
    time_steps = 300

    # Initialize Random Particle Positions
    positions = np.random.uniform(1, box_size - 1, (num_particles, 2))

    # Initial Temperature (Kinetic Average Base Jitter)
    T_initial = 2.0

    # Random velocity directions, scaled by Temperature
    angles = np.random.uniform(0, 2 * np.pi, num_particles)
    speeds = np.random.normal(T_initial, 0.5, num_particles)
    velocities = np.column_stack((speeds * np.cos(angles), speeds * np.sin(angles)))

    # We will simulate a wall compressing (Reducing Volume V)
    # This should functionally raise the Pressure (P) on the walls.
    # We track total momentum exchange with the walls.

    fig, ax = plt.subplots(figsize=style.figsize("square"))

    scatter = ax.scatter(
        positions[:, 0], positions[:, 1], s=30,
        color=style.COLORS["ave"], edgecolors=style.COLORS["data"], linewidths=0.4,
    )

    # Moving wall properties
    wall_x = box_size
    (wall_line,) = ax.plot(
        [wall_x, wall_x], [0, box_size],
        color=style.COLORS["comparison"], lw=4, label="Compressing wall",
    )

    ax.set_xlim(0, box_size)
    ax.set_ylim(0, box_size)
    ax.set_xlabel(style.axis_label("Cavity width", "x", "grid units"))
    ax.set_ylabel(style.axis_label("Cavity height", "y", "grid units"))
    ax.set_aspect("equal")

    print("[1] Simulating 2D Gas Kinematics within the LC Grid...")

    pressure_accumalator = 0
    pressure_reading = 0.0

    def update(frame: int) -> tuple:
        nonlocal positions, velocities, wall_x, pressure_accumalator, pressure_reading

        # Move the right wall slowly inward (Decreasing Volume V)
        if frame > 20 and frame < 200:
            wall_x -= 0.02
            wall_line.set_data([wall_x, wall_x], [0, box_size])

        # Update positions
        positions += velocities * dt

        # Boundary Collisions (Calculating Pressure P)
        # Pressure occurs when a topological node transfers inductive strain (momentum) into a boundary

        # Left wall
        mask_left = positions[:, 0] <= 0
        positions[mask_left, 0] = np.abs(positions[mask_left, 0])
        velocities[mask_left, 0] *= -1
        pressure_accumalator += np.sum(2 * np.abs(velocities[mask_left, 0]))

        # Right wall (Moving)
        mask_right = positions[:, 0] >= wall_x
        positions[mask_right, 0] = wall_x - (positions[mask_right, 0] - wall_x)
        velocities[mask_right, 0] *= -1
        pressure_accumalator += np.sum(2 * np.abs(velocities[mask_right, 0]))

        # Bottom wall
        mask_bottom = positions[:, 1] <= 0
        positions[mask_bottom, 1] = np.abs(positions[mask_bottom, 1])
        velocities[mask_bottom, 1] *= -1
        pressure_accumalator += np.sum(2 * np.abs(velocities[mask_bottom, 1]))

        # Top wall
        mask_top = positions[:, 1] >= box_size
        positions[mask_top, 1] = box_size - (positions[mask_top, 1] - box_size)
        velocities[mask_top, 1] *= -1
        pressure_accumalator += np.sum(2 * np.abs(velocities[mask_top, 1]))

        scatter.set_offsets(positions)

        # Smooth out pressure readings (Moving Average over 10 frames)
        if frame % 10 == 0:
            # Pressure = Total Force / Boundary Perimeter
            perimeter = 2 * (wall_x + box_size)
            pressure_reading = pressure_accumalator / perimeter
            pressure_accumalator = 0  # reset

        return scatter, wall_line

    print("[2] Rendering Cavity Volume compression...")
    ani = animation.FuncAnimation(fig, update, frames=time_steps, interval=30, blit=False)

    os.makedirs("standard_model/animations", exist_ok=True)
    out_path = "standard_model/animations/ideal_gas_pv_lc.gif"
    ani.save(out_path, writer="pillow", fps=30)
    plt.close(fig)

    print("[3] Slicing compressed state for manuscript...")
    fig_static, ax_static = plt.subplots(figsize=style.figsize("square"))

    # Map final state (house palette: nodes = AVE blue, wall = vermillion,
    # cavity boundary = muted gray guides).
    ax_static.scatter(
        positions[:, 0], positions[:, 1], s=30,
        color=style.COLORS["ave"], edgecolors=style.COLORS["data"], linewidths=0.4,
        label="Trapped topological nodes $N$",
    )
    ax_static.plot(
        [wall_x, wall_x], [0, box_size],
        color=style.COLORS["comparison"], lw=4, label="Compressing wall",
    )  # Final Wall
    ax_static.plot([0, 0], [0, box_size], color=style.COLORS["muted"], lw=1)  # Left
    ax_static.plot([0, wall_x], [0, 0], color=style.COLORS["muted"], lw=1)  # Bottom
    ax_static.plot([0, wall_x], [box_size, box_size], color=style.COLORS["muted"], lw=1)  # Top

    ax_static.set_xlim(0, box_size)
    ax_static.set_ylim(0, box_size)
    ax_static.set_xlabel(style.axis_label("Cavity width", "x", "grid units"))
    ax_static.set_ylabel(style.axis_label("Cavity height", "y", "grid units"))
    ax_static.set_aspect("equal")
    style.legend(ax_static, where="below", ncol=2)

    # Canonical, manuscript-cited output (chapter 12 \includegraphics).
    static_out = sim_output("ideal_gas_compressed_static")
    written = style.save(fig_static, static_out)
    plt.close(fig_static)

    print("\n[STATUS: SUCCESS] Illustrative LC-cavity compression rendered")
    print("(narrative mapping of PV=nRT onto continuous macroscopic LC impedance).")
    print(f"Animated propagation saved to {out_path}")
    for p in written:
        print(f"wrote {p}")


if __name__ == "__main__":
    main()
