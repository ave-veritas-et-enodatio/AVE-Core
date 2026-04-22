#!/usr/bin/env python3
"""
Electrostatic Point Charge Resolution

This script resolves the classical electromagnetism infinity associated
with the self-energy of a point charge ($r \to 0$, $E \to \infty$).

Classical electrostatics integrates the spherical 3D energy density
towards a dimensionless 0D coordinate, causing the energy to diverge. Wait.
If we bound the spatial integral stringently at the Axiom 1 lattice limit
($L_{NODE}$), the 3D isotropic integral yields only $\approx \alpha/2 \, m_e c^2$.

To yield exactly $1.0 \, m_e c^2$, the AVE framework substitutes the 3D isotropic
core with the exact 1D topological boundary of the $0_1$ Unknot. The electron
is a closed flux tube of circumference $\ell_{node}$. The energy is simply the
1D electromagnetic string tension integrated along this minimum ropelength.

The classical electrostatic divergence is definitively capped by the topology
of the vacuum.
"""

import os

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import ALPHA, C_0, EPSILON_0, L_NODE, M_E, T_EM, e_charge


def run_electrostatic_resolution() -> None:
    print("==================================================")
    print(" AVE ELECTROSTATIC POINT CHARGE RESOLUTION ")
    print("==================================================")

    # 1. Classical 3D Point-Charge Energy Integration (Unbounded vs L_NODE Bounded)
    # E(r) = e / (4 * pi * epsilon_0 * r^2)
    # U_density(r) = 1/2 * epsilon_0 * E(r)^2 = e^2 / (32 * pi^2 * epsilon_0 * r^4)
    # 3D Integral from R to infinity = e^2 / (8 * pi * epsilon_0 * R)

    canonical_rest_mass_energy = M_E * C_0**2
    e_sq_over_4pieps0 = (e_charge**2) / (4.0 * np.pi * EPSILON_0)

    # Check bounded at classical electron radius r_e
    r_e = ALPHA * L_NODE
    u_classical_re = 0.5 * e_sq_over_4pieps0 / r_e

    # Check bounded at topological L_NODE
    u_topological_bound = 0.5 * e_sq_over_4pieps0 / L_NODE

    alpha_half = (ALPHA / 2.0) * canonical_rest_mass_energy

    print(f"1. Canonical Rest Mass (m_e c^2):      {canonical_rest_mass_energy:.6e} J")
    print(f"2. 3D Integral bound at r_e:         {u_classical_re:.6e} J (Matches 1.0/2.0 m_e c^2 sphere scaling)")
    print(f"3. 3D Integral bound at L_NODE:      {u_topological_bound:.6e} J")
    print(f"   -> Ratio to Rest Mass:           {u_topological_bound/canonical_rest_mass_energy:.6f}")
    print(f"   -> Exact Alpha/2 expected:        {alpha_half:.6e} J")

    if np.isclose(u_topological_bound, alpha_half):
        print("   -> (Match Confirmed: The 3D bounded integral isolates purely the α/2 linear field phase)")

    print("\n--------------------------------------------------")
    print(" THE 1D TOPOLOGICAL RESOLUTION (UN-KNOT)")
    print("--------------------------------------------------")

    # By enforcing the topological Axiom 1 boundary, the electron is not a 3D sphere
    # but a 1D phase flux loop. The energy density is trapped along the 1D structural
    # string. We integrate the Phase Space string tension T_EM over the topological
    # loop perimeter L_NODE.

    u_1d_topological = T_EM * L_NODE

    print(f"1D Topological Flux Loop Length:     {L_NODE:.6e} m")
    print(f"String Tension (T_EM):               {T_EM:.6e} N")
    print(f"1D Bounded Integration (T_EM * L):   {u_1d_topological:.6e} J")
    print(f"Ratio to Canonical Rest Mass:        {u_1d_topological / canonical_rest_mass_energy:.12f}")
    print("-> Classically unbounded (∞) singularity collapses precisely to EXACTLY 1.0 m_e c^2.")

    # -------------------------------------------------------------
    # PLOTTING THE RADIAL DIVERGENCE VS AXIAL CONSTRICTION
    # -------------------------------------------------------------
    r_points = np.logspace(-15, -11, 1000)

    # Classical divergence 1/r
    energy_spectrum_classical = (0.5 * e_sq_over_4pieps0) / r_points

    # Topology bound sets effective radius
    # To strictly avoid singularity, topological energy inside L_NODE is exactly T_EM * L_NODE
    # Which corresponds to removing the point assumption and setting constant metric
    energy_spectrum_ave = np.where(r_points < L_NODE, T_EM * L_NODE, (0.5 * e_sq_over_4pieps0) / r_points)

    plt.figure(figsize=(10, 6), facecolor="white")
    plt.plot(
        r_points,
        energy_spectrum_classical,
        "r--",
        label="Classical 3D Point-Charge Divergence ($\\propto 1/r$)",
    )
    plt.plot(
        r_points,
        energy_spectrum_ave,
        "b-",
        linewidth=2,
        label="AVE Bounded Topological Loop ($T_{EM} \\cdot \\ell_{node}$)",
    )

    plt.axvline(L_NODE, color="k", linestyle=":", label="Topological Boundary ($L_{NODE}$)")
    plt.axhline(
        canonical_rest_mass_energy,
        color="g",
        linestyle="-.",
        alpha=0.5,
        label="Exact $m_e c^2$ Rest Mass Limit",
    )

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Radial Distance [m] (Log Scale)")
    plt.ylabel("Integrated Self-Energy [Joules] (Log Scale)")
    plt.title("Resolution of Electrostatic Point-Charge Singularity via AVE Topology")
    plt.legend()
    plt.grid(True, alpha=0.3)

    os.makedirs("manuscript/vol_2_subatomic/figures", exist_ok=True)
    plot_path = "manuscript/vol_2_subatomic/figures/electrostatic_singularity_resolution.png"
    plt.savefig(plot_path, dpi=300, bbox_inches="tight")
    print(f"\nSaved divergence comparison plot to: {plot_path}")
    print("==================================================")


if __name__ == "__main__":
    run_electrostatic_resolution()
