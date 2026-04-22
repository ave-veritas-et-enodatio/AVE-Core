"""
AVE SUBMODULE: FLUORINE-19 TOPOLOGICAL SOLVER
-------------------------------------------
Calculates the required macroscopic separation distance (R_halo) between the 
inert Oxygen-16 core (4 Alphas) and the bound Tritium outer ring 
to perfectly match the empirical CODATA mass defect of F-19.
"""

import numpy as np
from scipy.optimize import minimize

# Ensure the core framework is in PATH
import pathlib

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from periodic_table.simulations.simulate_element import get_nucleon_coordinates

# All constants imported from the physics engine — zero hardcoded values
from ave.core.constants import (
    K_MUTUAL,
    M_P_MEV_TARGET as M_P_RAW,
    M_N_MEV_TARGET as M_N_RAW,
    D_PROTON as D_0,
)

# Target Empirical CODATA Nuclear Mass for Fluorine-19 (MeV)
# 18.99840316273 amu * 931.494102 MeV/amu - (9 * 0.51099895 MeV)
TARGET_MASS_F19 = 17692.301503


def get_fluorine_19_nodes(r_halo):
    """
    Constructs the 19-nucleon array (Oxygen-16 core + Tritium Halo).
    """
    # 1. First, retrieve the perfectly balanced Oxygen-16 structural core
    # (This uses the hardcoded r_tet = 54.299234d internally)
    nodes_o16 = get_nucleon_coordinates(8, 16, D_0)

    # 2. Extract the geometric center of one of the Alpha clusters
    # to act as the origin vector for the halo binding. We'll use the first one.
    alpha_0_center = np.mean(nodes_o16[:4], axis=0)  # Barycenter of first alpha

    # Unit vector pointing from the main O16 origin outward through alpha_0
    v_out = alpha_0_center / np.linalg.norm(alpha_0_center)

    # 3. Construct the Tritium Halo (1 Proton, 2 Neutrons)
    # Fundamental geometry: An equilateral triangle of span 2d
    d = D_0
    halo_base = np.array([(0, d, d), (0, -d, d), (0, 0, -d)])  # P  # N  # N

    # 4. Translate the Tritium halo outward along the exit vector by R_halo
    halo_offset = alpha_0_center + (v_out * r_halo)

    nodes_f19 = list(nodes_o16)
    for node in halo_base:
        nodes_f19.append(node + halo_offset)

    return np.array(nodes_f19)


def calc_mass(r_halo):
    """
    Calculates the topological mass of the F-19 lattice given an R_halo separation.
    """
    nodes = get_fluorine_19_nodes(r_halo)

    raw_mass = (9 * M_P_RAW) + (10 * M_N_RAW)
    binding_energy = 0.0

    # Execute full O(n^2) topological mutual inductance calc
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = np.linalg.norm(nodes[i] - nodes[j])
            binding_energy += K_MUTUAL / dist

    return raw_mass - binding_energy


def optimize_topology():
    print(f"--- Optimizing Fluorine-19 ({TARGET_MASS_F19:.6f} MeV target) ---")

    # Error function to minimize
    def error_func(r_val):
        return abs(calc_mass(r_val[0]) - TARGET_MASS_F19)

    # Initial guess: 10 * D_0 outward from the alpha center
    res = minimize(error_func, [10.0 * D_0], method="Nelder-Mead", tol=1e-8)

    optimal_r = res.x[0]
    final_mass = calc_mass(optimal_r)

    print(f"Optimal R_halo: {optimal_r/D_0:.6f} d (Absolute: {optimal_r:.6f})")
    print(f"Topological Mass: {final_mass:.6f} MeV")
    print(f"Mass Mapping Error: {abs(final_mass - TARGET_MASS_F19)/TARGET_MASS_F19 * 100:.8f}%")
    return optimal_r


if __name__ == "__main__":
    optimize_topology()
