import os
import numpy as np
import matplotlib.pyplot as plt

# Import exactly what simulate_element uses to ensure mathematical fidelity
from scripts.vol_6_periodic_table.simulations.simulate_element import (
    get_nucleon_coordinates,
    K_MUTUAL,
)


def calculate_network_parameters(Z, A):
    """
    Calculates the Theoretical EE Network Parameters for the given element topology.
    Returns:
        - U_stored: Total Reactive Stored Energy (Binding Energy / Mutual Inductance)
        - Q_factor: Quality Factor (Ratio of Stored Energy to Dissipated Energy per Radian)
        - S11_cross_section: Theoretical Scattering / Radar Cross-Section area.
    """
    nodes = get_nucleon_coordinates(Z, A)
    if not nodes:
        return 0, 0, 0

    N = len(nodes)

    # 1. Total Stored Reactive Energy (U_stored)
    # This is exactly equal to the mass defect (Binding Energy) calculated previously.
    # It represents the total Mutual Inductance (M_ij) of the network.
    U_stored = 0
    for i in range(N):
        for j in range(i + 1, N):
            pt1 = np.array(nodes[i])
            pt2 = np.array(nodes[j])
            dist = np.linalg.norm(pt1 - pt2)
            U_stored += K_MUTUAL / dist

    # 2. Network Quality Factor (Q)
    # Q = 2*pi * (Energy Stored / Energy Dissipated per cycle)
    # In the AVE frame, "dissipation" is the geometric strain radiation (acoustic drag)
    # scaling with the physical bounding radius of the topology.
    # A tightly bound, perfectly symmetric core (He4) leaks almost zero energy (High Q).
    # A widely separated, asymmetrical shell (Li7) leaks heavy strain (Low Q).

    # First, calculate the center of mass to find the boundary radius
    com = np.mean(nodes, axis=0)
    max_radius = 0
    for np_node in nodes:
        r = np.linalg.norm(np.array(np_node) - com)
        if r > max_radius:
            max_radius = r

    # Empirical scaling tuning: Let's assume the energy "loss" per radian scales
    # with the bounding perimeter length of the element (2 * pi * R).
    # The larger the element, the more surface area it exposes to vacuum friction.
    # Q_raw = U_stored / (Radius)
    # We add a small epsilon to radius for Hydrogen-1 (a single node at r=0)
    # Hydrogen-1's radius in this abstraction is the topological radius (~1.0d)
    effective_radius = max_radius if max_radius > 0.1 else 0.85

    # Q factor mathematically scales with stored reactive energy relative to the lossy perimeter.
    Q_factor = (U_stored / effective_radius) if U_stored > 0 else 1.0

    # 3. S11 Reflection Cross-Section (Scattering Parameter)
    # The physical "hardness" of the nucleus to incoming wave scattering.
    # Area = pi * r^2.
    S11_area = np.pi * (effective_radius**2)

    return U_stored, Q_factor, S11_area


if __name__ == "__main__":
    elements = [
        {"Z": 1, "A": 1, "name": "Hydrogen-1 (Protium)"},
        {"Z": 2, "A": 4, "name": "Helium-4 (Alpha Core)"},
        {"Z": 3, "A": 7, "name": "Lithium-7 (Asymmetric)"},
        {"Z": 4, "A": 9, "name": "Beryllium-9 (Dual-Core)"},
    ]

    names = []
    q_factors = []
    s11_areas = []

    print(f"{'Element':<25} | {'U_stored (M_ij)':<15} | {'Q-Factor (Stability)':<22} | {'S11 Section (Area)'}")
    print("-" * 90)

    for el in elements:
        u_str, q, s11 = calculate_network_parameters(el["Z"], el["A"])
        names.append(el["name"].split()[0])
        q_factors.append(q)
        s11_areas.append(s11)
        print(f"{el['name']:<25} | {u_str:>11.2f} MeV | {q:>20.2f} | {s11:>14.2f} d^2")

    # Generate Visual Plots for the Manuscript
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Q-Factor Plot
    # We normalize Q-factors relative to Helium-4 to show it as the "Indestructible Gold Standard"
    q_norm = [q / q_factors[1] for q in q_factors]

    bars1 = ax1.bar(names, q_norm, color=["silver", "gold", "lightcoral", "orchid"])
    ax1.set_title("Topological Quality Factor ($Q$)\n(Stability & Resonance)", fontsize=14)
    ax1.set_ylabel("Normalized $Q$ (Relative to $^4He$)", fontsize=12)
    ax1.grid(axis="y", linestyle="--", alpha=0.7)

    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2.0, yval, f"{yval:.2f}x", va="bottom", ha="center")

    # S11 Cross Section Plot
    bars2 = ax2.bar(names, s11_areas, color=["lightblue", "dodgerblue", "navy", "mediumblue"])
    ax2.set_title("Topological Scattering ($S_{11}$) Cross-Section\n(Radar/Acoustic Hardness)", fontsize=14)
    ax2.set_ylabel(r"Effective Area ($\pi r^2$)", fontsize=12)
    ax2.set_yscale("log")  # Log scale because Li7 is massive
    ax2.grid(axis="y", linestyle="--", alpha=0.7)

    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2.0, yval, f"{yval:.1f}", va="bottom", ha="center")

    plt.tight_layout()

    os.makedirs("tests/outputs", exist_ok=True)
    plt.savefig("tests/outputs/ee_network_analysis.png", dpi=300, bbox_inches="tight")
    print("\n[+] Exported graphical analysis to tests/outputs/ee_network_analysis.png")
