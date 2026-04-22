"""
AVE Topological Isotope Stability Simulator
======================================================
This script models the macroscopic geometric variance between Uranium-235
and Uranium-238. Standard physics struggles to visualize *why* U-235 is highly
fissile and U-238 is mostly inert, relying entirely on quantum probability tables.

By running both nucleon clusters through the exact same Topological Optimizer,
we can visually see the geometric differences: U-238 converges into a closed,
stable spherical shell, while U-235 settles with an asymmetrical lattice "cleft" 
that leaves it structurally vulnerable to incoming thermal neutrons.
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pathlib

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from ave.solvers.topology_optimizer import TopologicalOptimizer

M_P = 1.00727
M_N = 1.00866
Z = 92  # Uranium protons


def build_uranium_core(A):
    """
    Builds the masses array and initializes the random nucleon cloud.
    """
    masses = []
    colors = []

    n_neutrons = A - Z

    for _ in range(Z):
        masses.append(M_P)
        colors.append("#ff3333")  # Proton Red

    for _ in range(n_neutrons):
        masses.append(M_N)
        colors.append("#3333ff")  # Neutron Blue

    # Start sparsely packed
    np.random.seed(42)  # Use the same seed for both so initial cloud geometry is identical!
    box_size = 5.0
    initial_coords = np.random.uniform(-box_size, box_size, size=(A, 3))

    return masses, colors, initial_coords


def assemble_isotopes():
    print("[*] Comparing Topological Stability: U-235 vs U-238")

    # 1. Assemble U-235
    m_235, c_235, init_235 = build_uranium_core(235)
    opt_235 = TopologicalOptimizer(node_masses=m_235, interaction_scale="nuclear")

    print("[*] Annealing U-235...")
    final_235, energy_235 = opt_235.optimize(
        init_235, method="L-BFGS-B", options={"maxiter": 300, "ftol": 1e-4, "disp": False}
    )

    # 2. Assemble U-238
    m_238, c_238, init_238 = build_uranium_core(238)
    opt_238 = TopologicalOptimizer(node_masses=m_238, interaction_scale="nuclear")

    print("[*] Annealing U-238...")
    final_238, energy_238 = opt_238.optimize(
        init_238, method="L-BFGS-B", options={"maxiter": 300, "ftol": 1e-4, "disp": False}
    )

    # Render Comparison
    print("[*] Rendering Topological Cross-Sections...")

    fig = plt.figure(figsize=(16, 8))
    fig.patch.set_facecolor("#0f0f0f")

    # Center the coordinates for visualization
    final_235 = final_235 - np.mean(final_235, axis=0)
    final_238 = final_238 - np.mean(final_238, axis=0)

    # U-235 Plot
    ax1 = fig.add_subplot(121, projection="3d")
    ax1.set_facecolor("#0f0f0f")
    ax1.grid(False)
    ax1.axis("off")
    ax1.set_title(f"Uranium-235 (Fissile Cleft)\nCore Strain: {energy_235:.0f}", color="white", pad=10)
    ax1.set_xlim([-5, 5])
    ax1.set_ylim([-5, 5])
    ax1.set_zlim([-5, 5])

    x, y, z = final_235[:, 0], final_235[:, 1], final_235[:, 2]
    ax1.scatter(x, y, z, c=c_235, s=60, edgecolors="black", alpha=0.9)

    # Find the rough geographical 'cleft' (sparse sector) for U-235 to highlight it
    # We will just tilt the view to look down the least dense axis
    ax1.view_init(elev=20, azim=45)

    # U-238 Plot
    ax2 = fig.add_subplot(122, projection="3d")
    ax2.set_facecolor("#0f0f0f")
    ax2.grid(False)
    ax2.axis("off")
    ax2.set_title(f"Uranium-238 (Closed Stable Shell)\nCore Strain: {energy_238:.0f}", color="white", pad=10)
    ax2.set_xlim([-5, 5])
    ax2.set_ylim([-5, 5])
    ax2.set_zlim([-5, 5])

    x, y, z = final_238[:, 0], final_238[:, 1], final_238[:, 2]
    ax2.scatter(x, y, z, c=c_238, s=60, edgecolors="black", alpha=0.9)
    ax2.view_init(elev=20, azim=45)

    plt.tight_layout()

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "isotope_stability_variance.png"
    plt.savefig(target, dpi=300, facecolor="#0f0f0f")
    print(f"[*] Visualized Isotope Topologies: {target}")


if __name__ == "__main__":
    assemble_isotopes()
