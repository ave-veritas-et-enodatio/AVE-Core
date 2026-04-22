"""
AVE SUBMODULE: SILICON-28 TOPOLOGICAL SOLVER
--------------------------------------------
Calculates the required macroscopic separation distance (R_bipyr) 
for the 7-Alpha Pentagonal Bipyramid matrix to mathematically match 
the empirical CODATA mass defect of Si-28.
"""

import pathlib

import numpy as np
from scipy.optimize import minimize

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

# All constants imported from the physics engine — zero hardcoded values
from ave.core.constants import D_PROTON as D_0
from ave.core.constants import K_MUTUAL
from ave.core.constants import M_N_MEV_TARGET as M_N_RAW
from ave.core.constants import M_P_MEV_TARGET as M_P_RAW

# Target Empirical CODATA Nuclear Mass for Silicon-28 (MeV)
# 27.976926535 amu * 931.494102 MeV/amu - (14 * 0.51099895 MeV)
TARGET_MASS_SI28 = 26053.188074


def get_silicon_28_nodes(r_bipyr):
    """
    Constructs the 28-nucleon array (7-Alpha Pentagonal Bipyramid).
    """
    d = D_0

    alpha_base = np.array([(d, d, d), (-d, -d, d), (-d, d, -d), (d, -d, -d)])

    # 5 Equator Nodes + 2 Polar Nodes
    equator_angles = np.linspace(0, 2 * np.pi, 5, endpoint=False)
    macro_centers = []

    # Poles
    macro_centers.append((0, 0, r_bipyr))
    macro_centers.append((0, 0, -r_bipyr))

    # Equator
    for theta in equator_angles:
        x_c = r_bipyr * np.cos(theta)
        y_c = r_bipyr * np.sin(theta)
        macro_centers.append((x_c, y_c, 0.0))

    macro_centers = np.array(macro_centers)

    nodes_si28 = []
    for center in macro_centers:
        for node in alpha_base:
            nodes_si28.append(node + center)

    return np.array(nodes_si28)


def calc_mass(r_bipyr):
    nodes = get_silicon_28_nodes(r_bipyr)
    raw_mass = (14 * M_P_RAW) + (14 * M_N_RAW)
    binding_energy = 0.0

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = np.linalg.norm(nodes[i] - nodes[j])
            binding_energy += K_MUTUAL / dist

    return raw_mass - binding_energy


def optimize_topology():
    print(f"--- Optimizing Silicon-28 ({TARGET_MASS_SI28:.6f} MeV target) ---")

    def error_func(r_val):
        return abs(calc_mass(r_val[0]) - TARGET_MASS_SI28)

    res = minimize(error_func, [80.0 * D_0], method="Nelder-Mead", tol=1e-8)

    optimal_r = res.x[0]
    final_mass = calc_mass(optimal_r)

    print(f"Optimal R_bipyramid: {optimal_r/D_0:.6f} d (Absolute: {optimal_r:.6f})")
    print(f"Topological Mass: {final_mass:.6f} MeV")
    print(f"Mass Mapping Error: {abs(final_mass - TARGET_MASS_SI28)/TARGET_MASS_SI28 * 100:.8f}%")
    return optimal_r


if __name__ == "__main__":
    optimize_topology()
