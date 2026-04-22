import os

import matplotlib.pyplot as plt
import numpy as np

from scripts.vol_6_periodic_table.simulations.simulate_element import (
    M_N_RAW,
    M_P_RAW,
    calculate_topological_mass,
    get_nucleon_coordinates,
)

def compute_topology(Z: int, A: int) -> tuple[float, float, float]:
    N = A - Z
    raw_mass = (Z * M_P_RAW) + (N * M_N_RAW)
    theo_mass = calculate_topological_mass(Z, A)
    binding_energy = raw_mass - theo_mass

    # Calculate effective radius and Q-Factor
    nodes = get_nucleon_coordinates(Z, A)
    if len(nodes) > 1:
        com = np.mean(nodes, axis=0)
        max_radius = max([np.linalg.norm(np.array(n) - com) for n in nodes])
    else:
        max_radius = 0.85

    effective_radius = max_radius if max_radius > 0.1 else 0.85
    q_factor = (binding_energy / effective_radius) if binding_energy > 0 else 1.0

    return theo_mass, binding_energy, q_factor

if __name__ == "__main__":
    os.makedirs("tests/outputs", exist_ok=True)

    # Analyze Beta-Decay: Tritium -> Helium-3
    t_mass, t_be, t_q = compute_topology(1, 3)
    he3_mass, he3_be, he3_q = compute_topology(2, 3)

    # Analyze Fission: Beryllium-8 -> 2 x Helium-4
    be8_mass, be8_be, be8_q = compute_topology(4, 8)
    he4_mass, he4_be, he4_q = compute_topology(2, 4)
    two_he4_mass = 2 * he4_mass

    print("=======================================")
    print("RADIOACTIVE DECAY IMPEDANCE MISMATCH")
    print("=======================================\n")

    print("1. BETA DECAY: Tritium (3H) -> Helium-3 (3He) + e-")
    print(f"   Tritium Mass:   {t_mass:.3f} MeV (Binding E = {t_be:.3f} MeV, Q = {t_q:.2f})")
    print(f"   Helium-3 Mass:  {he3_mass:.3f} MeV (Binding E = {he3_be:.3f} MeV, Q = {he3_q:.2f})")
    print(f"   Decay Energy:   {t_mass - he3_mass:.3f} MeV (Spontaneous Exothermic Release!)\n")

    print("2. FISSION DECAY: Beryllium-8 (8Be) -> 2 x Helium-4 (4He)")
    print(f"   Beryllium-8:    {be8_mass:.3f} MeV (Binding E = {be8_be:.3f} MeV, Q = {be8_q:.2f})")
    print(f"   2 x Helium-4:   {two_he4_mass:.3f} MeV (Binding E = {2*he4_be:.3f} MeV, Q = {he4_q:.2f})")
    print(f"   Decay Energy:   {be8_mass - two_he4_mass:.3f} MeV (Cores immediately repel!)\n")

    # Plot the Decay Transition Dynamics
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Tritium Beta Decay
    ax1.bar(
        ["$^3H$ (Tritium)\nUnstable Topology", "$^3He$ (Helium-3)\nStable Topology"],
        [t_q, he3_q],
        color=["lightcoral", "dodgerblue"],
    )
    ax1.set_title(
        "Beta Decay Transition: $^3H$ $\\rightarrow$ $^3He$\n(Topological Q-Factor Optimization)",
        fontsize=13,
    )
    ax1.set_ylabel("Topological Quality Factor ($Q$)", fontsize=12)
    ax1.grid(axis="y", linestyle="--", alpha=0.7)

    target_mass_drop = t_mass - he3_mass
    ax1.annotate(
        f"Spontaneous Beta Decay\n$\\Delta E = {target_mass_drop:.3f}$ MeV",
        xy=(1, he3_q),
        xytext=(0, he3_q + 1),
        arrowprops=dict(facecolor="black", shrink=0.05),
        horizontalalignment="center",
        fontsize=11,
        fontweight="bold",
    )

    # Beryllium-8 Fission
    ax2.bar(
        [
            "$^8Be$ (No Bridge Neutron)\nRepelling Alphas",
            "2 x $^4He$ (Alpha Particles)\nHigh-Resonance Fragments",
        ],
        [be8_q, he4_q * 2.0],
        color=["orchid", "gold"],
    )
    ax2.set_title(
        "Alpha Fission: $^8Be$ $\\rightarrow$ $2\\alpha$\n(Missing Wheatstone Bridge $M_{bridge}$)",
        fontsize=13,
    )
    ax2.set_ylabel("Total Network Q-Factor ($Q$)", fontsize=12)
    ax2.grid(axis="y", linestyle="--", alpha=0.7)

    fission_drop = be8_mass - two_he4_mass
    ax2.annotate(
        f"Instantaneous Cleavage\n$\\Delta E = {fission_drop:.3f}$ MeV",
        xy=(1, he4_q * 2.0),
        xytext=(0, he4_q * 2.0 + 2),
        arrowprops=dict(facecolor="black", shrink=0.05),
        horizontalalignment="center",
        fontsize=11,
        fontweight="bold",
    )

    plt.tight_layout()
    plt.savefig("tests/outputs/isotope_decay_analytics.png", dpi=300, bbox_inches="tight")
    print("[+] Exported plot to tests/outputs/isotope_decay_analytics.png")
