import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Ensure local ave package is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from ave.solvers.fdtd_lc_network import FDTDLattice1D


def run_simulation():
    """
    Simulates a Gaussian EM pulse traveling through a 1D gravitational metric
    (a gradient of optical density).
    """
    GRID_SIZE = 400
    RESOLUTION = 0.01  # 1 cm resolution
    PULSE_WIDTH = 20

    # Instantiate the lattice with a dense mass in the center
    # Mass scaled to force n(r)=2.0 near the center for visual dramatic effect
    MASS_CENTER_KG = 6.7e26

    lattice = FDTDLattice1D(size=GRID_SIZE, grid_resolution=RESOLUTION, mass_center_kg=MASS_CENTER_KG)

    # Initialize a Gaussian pulse on the left side (E field)
    pulse_idx = 40
    for i in range(GRID_SIZE):
        lattice.E[i] = np.exp(-0.5 * ((i - pulse_idx) / PULSE_WIDTH) ** 2)

    # We want to save snapshots of the E-field as it propagates
    snapshots = []

    # Run simulation for enough steps to cross the center mass
    STEPS = 650
    for t in range(STEPS):
        # We manually step the FDTD equations here for a Gaussian rather than a sine source
        lattice.H[:] += lattice.ch[:] * (lattice.E[1:] - lattice.E[:-1])
        lattice.E[0] = lattice.E[1]
        lattice.E[-1] = lattice.E[-2]
        lattice.E[1:-1] += lattice.ce[1:-1] * (lattice.H[1:] - lattice.H[:-1])

        if t % 130 == 0:
            snapshots.append(lattice.E.copy())

    # Visualize
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Plot Refractive Index profile
    x_axis = np.linspace(-GRID_SIZE / 2 * RESOLUTION, GRID_SIZE / 2 * RESOLUTION, GRID_SIZE)
    ax1.plot(x_axis, lattice.n_refractive, color="purple", label="Refractive Index $n(r)$")
    ax1.set_title("Macroscopic Vacuum Impedance / Refractive Gradient")
    ax1.set_ylabel("Optical Strain $n(r)$")
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # Plot pulse propagation
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    for idx, snap in enumerate(snapshots):
        ax2.plot(x_axis, snap, color=colors[idx % len(colors)], alpha=0.8, label=f"t={idx*130}")

    ax2.set_title("Achromatic Pulse Propagation (No Reflection)")
    ax2.set_xlabel("Distance from Center of Mass (m)")
    ax2.set_ylabel("Electric Field Amplitude")
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), "../assets/sim_outputs/achromatic_fdtd_refraction.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300)
    print(f"Saved visualization to {output_path}")


if __name__ == "__main__":
    run_simulation()
