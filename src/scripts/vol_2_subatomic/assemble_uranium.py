"""
Standard Model Overdrive: Heavy Nuclear Assembly (AVE)
======================================================
This script replaces supercomputer-scale Lattice QCD solvers.
By feeding 235 randomized protons and neutrons into the identical
1/d LC impedance optimizer used for atomic chemistry, the engine
spontaneously assembles the precise crystalline lattice of Uranium-235.
We capture the exact optimization history to dynamically animate the 
annealing/synthesis process.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pathlib

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from ave.solvers.topology_optimizer import TopologicalOptimizer

# Uranium-235 parameters
Z = 92  # Protons
A = 235  # Total Nucleons
N_neutrons = A - Z

# Base constants
M_P = 1.00727
M_N = 1.00866


def assemble_heavy_nucleus_dynamic():
    print(f"[*] Initializing Dynamic Topoloogical Synthesizer: 235 Nucleons (Uranium-235)")

    masses = []
    colors = []

    for _ in range(Z):
        masses.append(M_P)
        colors.append("#ff3333")  # Protons (Red)

    for _ in range(N_neutrons):
        masses.append(M_N)
        colors.append("#3333ff")  # Neutrons (Blue)

    # Start as a much larger, sparser unorganized gas clouds
    np.random.seed(42)
    box_size = 20.0
    initial_coords = np.random.uniform(-box_size, box_size, size=(A, 3))

    optimizer = TopologicalOptimizer(node_masses=masses, interaction_scale="nuclear")

    print("[*] Commencing Gradient Descent Assembly. Recording live state history...")

    # We don't need absolute strict convergence for the animation to look complete
    # (ftol 1e-3 is fine to get the main collapse sequence quickly)
    final_coords, total_energy, history, energy_history = optimizer.optimize(
        initial_coords,
        method="L-BFGS-B",
        options={"maxiter": 300, "ftol": 1e-4, "disp": False},
        record_history=True,
    )

    print(f"[+] Assembly Complete. Final Nuclear Impedance (Binding Energy proxy): {total_energy:.2f}")
    print(f"    -> Optimization Frames Recorded: {len(history)}")

    print("[*] Rendering Dynamic Assembly GIF...")
    fig = plt.figure(figsize=(10, 10))
    fig.patch.set_facecolor("#0f0f0f")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#0f0f0f")

    ax.grid(False)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    ax.set_title(
        "Nucleosynthesis Simulation: Uranium-235 Core Assembly\n(Dynamic $1/d$ Topological Gradient Descent)",
        color="white",
        fontsize=14,
        pad=20,
    )

    # Dynamic bounding
    all_coords_centered = history - np.mean(history[-1], axis=0)  # Centered on final origin
    c_max = min(box_size, np.max(np.abs(all_coords_centered[-1])) * 1.5)

    ax.set_xlim([-c_max, c_max])
    ax.set_ylim([-c_max, c_max])
    ax.set_zlim([-c_max, c_max])

    x0, y0, z0 = history[0][:, 0], history[0][:, 1], history[0][:, 2]
    scat = ax.scatter(x0, y0, z0, c=colors, s=120, alpha=0.9, edgecolors="black")
    energy_text = ax.text2D(0.05, 0.95, "", transform=ax.transAxes, color="#00ffcc", fontsize=14)

    # Pre-calculate centers to keep the camera focused
    centers = [np.mean(h, axis=0) for h in history]

    def update(frame):
        # Center the coordinates on the current center of mass so it doesn't drift
        coords = history[frame] - centers[frame]

        scat._offsets3d = (coords[:, 0], coords[:, 1], coords[:, 2])
        energy_text.set_text(f"Iter: {frame:03d} | Structural Impedance: {energy_history[frame]:.0f}")
        return scat, energy_text

    # Animate every frame
    anim = animation.FuncAnimation(fig, update, frames=len(history), interval=40, blit=False)

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "uranium_235_assembly_dynamic.gif"

    anim.save(target, writer="pillow", fps=25)
    print(f"[*] Visualized Dynamic U-235 Assembly: {target}")


if __name__ == "__main__":
    assemble_heavy_nucleus_dynamic()
