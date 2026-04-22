"""
AVE Physics Engine: 3D Polyhedral RLVG (Metric Gradient Compass)
Author: AI (Antigravity Assistant)
Based on: Vol 4, Section 12.4.3 - Applied RLVG Telemetry
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Add src to path to import ave packages
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from ave.core.constants import C_0

# Set up output directory
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "assets", "sim_outputs"))
os.makedirs(OUTPUT_DIR, exist_ok=True)


def simulate_polyhedral_rlvg():
    print("Simulating 3D Polyhedral RLVG Metric Gradient Compass...")

    # Simulation Parameters
    wavelength = 1550e-9  # 1550 nm telecom laser
    cavity_arm_length = 0.5  # 50 cm arm length for the polyhedron

    # 3D Grid for the metric gradient (e.g. diving into a gravitational well)
    z_dist = np.linspace(0.1, 10.0, 500)  # distance in meters from a massive body/drive

    # Define an artificial metric gradient (Z(r))
    # Standard spacetime impedance Z0 = 376.73 Ohms

    # Induced phase shift from gradient
    # A steep metric gradient induces localized phase shear proportional to 1/r^2 (gravitational) or artificial drive strain
    phase_shear_x = np.zeros_like(z_dist)
    phase_shear_y = np.zeros_like(z_dist)
    phase_shear_z = np.zeros_like(z_dist)

    # Assuming the craft is aligned along the z-axis diving into the gradient:
    # The gradient dz is steep, dx and dy are symmetric

    # Artificial gradient strength parameter G_metric (strain/m)
    G_metric = 1.5e-7 * (1 / z_dist**2)

    for i, z in enumerate(z_dist):
        # 3D Tensor phase accumulation (Sagnac anomaly)
        # Phase shift Delta Phi = (4 pi L / lambda c) * v_draft
        v_draft_z = G_metric[i] * C_0 * 1e-3  # simulated draft velocity effect

        # Polyhedral arms
        # X and Y arms experience minimal differential strain
        # Z arm along the gradient experiences maximum shear
        phase_shear_x[i] = (4 * np.pi * cavity_arm_length / (wavelength * C_0)) * (v_draft_z * 0.01)
        phase_shear_y[i] = (4 * np.pi * cavity_arm_length / (wavelength * C_0)) * (v_draft_z * 0.01)
        phase_shear_z[i] = (4 * np.pi * cavity_arm_length / (wavelength * C_0)) * v_draft_z

    # Plotting the 3D phase-shear tensor resolution
    plt.figure(figsize=(10, 6))

    plt.plot(z_dist, phase_shear_z * 1e9, "r-", linewidth=2.5, label="Z-Axis (Gradient Heading)")
    plt.plot(z_dist, phase_shear_x * 1e9, "b--", linewidth=1.5, label="X/Y-Axes (Transverse)")

    plt.title("3D Polyhedral RLVG: Phase-Shear Tensor Resolution", fontsize=14, fontweight="bold")
    plt.xlabel("Distance from Metric Gradient Source (m)", fontsize=12)
    plt.ylabel("Optical Phase Shear $\\Delta\\Phi$ (nRad)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=11)

    # Highlight the divergence
    plt.fill_between(z_dist, phase_shear_z * 1e9, phase_shear_x * 1e9, color="red", alpha=0.1)
    plt.text(
        2,
        max(phase_shear_z * 1e9) * 0.8,
        "Gradient Vector Resolution\n$\\nabla Z(r)$",
        fontsize=12,
        color="darkred",
        bbox=dict(facecolor="white", alpha=0.8, edgecolor="none"),
    )

    plt.tight_layout()

    output_path = os.path.join(OUTPUT_DIR, "polyhedral_rlvg_compass.png")
    plt.savefig(output_path, dpi=300)
    print(f"Plot saved to '{output_path}'")


if __name__ == "__main__":
    simulate_polyhedral_rlvg()
