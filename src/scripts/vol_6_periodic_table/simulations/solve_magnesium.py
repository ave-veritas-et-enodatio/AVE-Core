"""
AVE SUBMODULE: MAGNESIUM-24 TOPOLOGICAL SOLVER
----------------------------------------------
Calculates the required macroscopic separation distance (R_oct) 
for the 6-Alpha Octahedral matrix to mathematically match the empirical 
CODATA mass defect of Mg-24.
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

# Target Empirical CODATA Nuclear Mass for Magnesium-24 (MeV)
# 23.985041699 amu * 931.494102 MeV/amu - (12 * 0.51099895 MeV)
TARGET_MASS_MG24 = 22335.792891


def get_magnesium_24_nodes(r_oct):
    """
    Constructs the 24-nucleon array (6-Alpha Octahedron).
    """
    d = D_0

    alpha_base = np.array([(d, d, d), (-d, -d, d), (-d, d, -d), (d, -d, -d)])

    macro_centers = np.array(
        [
            (r_oct, 0, 0),
            (-r_oct, 0, 0),
            (0, r_oct, 0),
            (0, -r_oct, 0),
            (0, 0, r_oct),
            (0, 0, -r_oct),
        ]
    )

    nodes_mg24 = []
    for center in macro_centers:
        for node in alpha_base:
            nodes_mg24.append(node + center)

    return np.array(nodes_mg24)


def calc_mass(r_oct):
    nodes = get_magnesium_24_nodes(r_oct)
    raw_mass = (12 * M_P_RAW) + (12 * M_N_RAW)
    binding_energy = 0.0

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = np.linalg.norm(nodes[i] - nodes[j])
            binding_energy += K_MUTUAL / dist

    return raw_mass - binding_energy


def optimize_topology():
    print(f"--- Optimizing Magnesium-24 ({TARGET_MASS_MG24:.6f} MeV target) ---")

    def error_func(r_val):
        return abs(calc_mass(r_val[0]) - TARGET_MASS_MG24)

    res = minimize(error_func, [80.0 * D_0], method="Nelder-Mead", tol=1e-8)

    optimal_r = res.x[0]
    final_mass = calc_mass(optimal_r)

    print(f"Optimal R_octahedron: {optimal_r/D_0:.6f} d (Absolute: {optimal_r:.6f})")
    print(f"Topological Mass: {final_mass:.6f} MeV")
    print(f"Mass Mapping Error: {abs(final_mass - TARGET_MASS_MG24)/TARGET_MASS_MG24 * 100:.8f}%")
    return optimal_r


if __name__ == "__main__":
    optimize_topology()
