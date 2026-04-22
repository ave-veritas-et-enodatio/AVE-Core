#!/usr/bin/env python3
import os

import matplotlib.pyplot as plt
import numpy as np

from src.ave.condensed.bjt_mechanics import bjt_current_gain
from src.scripts.vol_4_engineering.temperature_stress_test import ave_V_bi, classical_V_bi

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../assets/sim_outputs"))
os.makedirs(output_dir, exist_ok=True)


def generate_bjt_surface():
    """Generates the 3D Topological Beta Surface map"""
    print("Generating BJT Geometric Surface...")
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")

    # Emitter doping ratio sweeps from 1.0 to 30.0
    ratios = np.linspace(1.0, 30.0, 50)
    # N_gap sweeps from 1 to 5
    gaps = np.linspace(1, 5, 50)

    R, G = np.meshgrid(ratios, gaps)
    Z = np.zeros_like(R)

    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            # Get beta for each point
            res = bjt_current_gain(N_gap_hops=G[i, j], emitter_doping_ratio=R[i, j])
            Z[i, j] = res["Beta_common_emitter"]
            if Z[i, j] > 1000:
                Z[i, j] = 1000  # Cap for visual clarity

    surf = ax.plot_surface(R, G, Z, cmap="plasma", edgecolor="none", alpha=0.9)
    ax.set_xlabel("Emitter Overdrive Ratio ($N_E / N_B$)")
    ax.set_ylabel("Topological Base Matrix Depth ($N_{gap}$)")
    ax.set_zlabel(r"Macroscopic Current Gain ($\beta$)")
    ax.set_title("BJT Macroscopic Gain as Geometric Surface Constraint")

    # Restrict z-axis to standard power electronic bounds
    ax.set_zlim(0, 400)

    fig.colorbar(surf, shrink=0.5, aspect=5)

    path = os.path.join(output_dir, "bjt_geometric_beta_surface.png")
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved {path}")


def generate_thermal_rigidity():
    """Generates the absolute 0 K boundary falsification plot"""
    print("Generating Thermal Falsification Ridge...")
    temperatures = np.linspace(0.1, 800, 400)

    c_vbi = []
    a_vbi = []

    # Need to extract floats from the strings returned by the test script
    for T in temperatures:
        c_str = classical_V_bi(float(T))
        a_str = ave_V_bi(float(T))

        if c_str in ["MATH_COLLAPSE_0K", "STATISTICAL_FREEZE"]:
            c_vbi.append(0.0)
        else:
            c_vbi.append(float(c_str.replace(" V", "")))

        a_vbi.append(float(a_str.replace(" V", "")))

    plt.figure(figsize=(10, 6))

    plt.plot(
        temperatures,
        c_vbi,
        "r--",
        linewidth=2,
        label="Classical Model (Fermi-Dirac Statistical Gas)",
    )
    plt.plot(temperatures, a_vbi, "b-", linewidth=3, label="AVE Model (Macroscopic Phononic Dilation)")

    # Mark the Mathematical Collapse zone
    plt.axvspan(0, 50, color="red", alpha=0.2, label="Math Collapse Zone (< 50 K)")

    plt.title(r"Semiconductor Thermal Rigidity Falsification ($0\text{ K} \to 800\text{ K}$)")
    plt.xlabel("Matrix Phonon Temperature (K)")
    plt.ylabel(r"Macroscopic Reflection Barrier ($V_{bi}$)")
    plt.ylim(0, 1.2)
    plt.grid(True, linestyle=":", alpha=0.7)
    plt.legend(loc="lower right")

    # Add text annotation
    plt.text(400, 1.08, "AVE Absolute Rigid Boundary", color="blue", fontweight="bold")

    path = os.path.join(output_dir, "cryogenic_rigidity_falsification.png")
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved {path}")


def generate_spice_override():
    """Generates the Topological Matrix vs Exponential I-V Curve"""
    print("Generating SPICE Constraint Visualizer...")

    voltage = np.linspace(0, 1.15, 500)

    # Classical Shockley Equation
    I_s = 1e-12
    V_t = 0.02585  # 300K
    eta = 1.0

    I_classical = I_s * (np.exp(voltage / (eta * V_t)) - 1)

    # AVE SPICE geometric clipping. 1.0496 is the rigid boundary.
    # Below boundary: 0
    # Above boundary: vertical structural short

    I_ave = np.zeros_like(voltage)
    breakdown_idx = np.argmax(voltage >= 1.0496)
    I_ave[breakdown_idx:] = (voltage[breakdown_idx:] - 1.0496) * 1000000  # Huge slope to mimic M->inf structural short

    plt.figure(figsize=(8, 8))

    plt.plot(
        voltage,
        I_classical,
        "r--",
        linewidth=2,
        label="Classical Thermal Gas (Exponential Math Failure)",
    )
    plt.plot(voltage, I_ave, "g-", linewidth=4, label="AVE Macroscopic Dielectric Framework (.SUBCKT)")

    plt.axvline(x=1.0496, color="black", linestyle=":", label="Topological Latch Threshold (1.0496 V)")

    plt.title("Macroscopic Diode I-V Output Constraints")
    plt.xlabel("Transmission Forward Pressure (V)")
    plt.ylabel("Matrix Transport Cavity Array (A)")

    plt.yscale("symlog", linthresh=0.01)
    plt.ylim(-0.01, 1000)  # Show the classical explosion to 1000 amps
    plt.xlim(0.8, 1.1)

    plt.grid(True, linestyle="-", alpha=0.3)
    plt.legend(loc="upper left")

    path = os.path.join(output_dir, "spice_zener_override_comparison.png")
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved {path}")


if __name__ == "__main__":
    print(f"Outputting figures to {output_dir}")
    generate_bjt_surface()
    generate_thermal_rigidity()
    generate_spice_override()
    print("Done.")
