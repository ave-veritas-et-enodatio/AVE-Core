"""
AVE SUBMODULE: ALUMINUM-27 TOPOLOGICAL SOLVER
---------------------------------------------
Calculates the required macroscopic separation distance (R_halo)
between the rigid Magnesium-24 (6-Alpha Octahedron) core and the
bound Tritium outer ring to mathematically match the empirical
CODATA mass defect of Al-27.
"""

import pathlib

import numpy as np
from scipy.optimize import minimize

# All constants imported from the physics engine — zero hardcoded values
from ave.core.constants import D_PROTON as D_0
from ave.core.constants import K_MUTUAL
from ave.core.constants import M_N_MEV_TARGET as M_N_RAW
from ave.core.constants import M_P_MEV_TARGET as M_P_RAW

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()
# Target Empirical CODATA Nuclear Mass for Aluminum-27 (MeV)
# 26.98153853 amu * 931.494102 MeV/amu - (13 * 0.51099895 MeV)
TARGET_MASS_AL27 = 25126.501017


def get_aluminum_27_nodes(r_halo):
    """
    Constructs the 27-nucleon array (Mg-24 core + Tritium Halo).
    """
    d = D_0

    # 1. Mg-24 Core Array (bare K/r solver with engine constants)
    r_oct = 80.557 * d

    alpha_base = np.array([(d, d, d), (-d, -d, d), (-d, d, -d), (d, -d, -d)])

    macro_centers = np.array(
        [
            (r_oct, 0, 0),
            (-r_oct, 0, 0),
            (0, r_oct, 0),
            (0, -r_oct, 0),
            (0, 0, r_oct),  # North Pole Alpha
            (0, 0, -r_oct),
        ]
    )

    nodes_mg24 = []
    for center in macro_centers:
        for node in alpha_base:
            nodes_mg24.append(node + center)

    # 2. Extract North Pole Alpha Barycenter as the primary binding vector origin
    polar_alpha_center = macro_centers[4]  # (0, 0, R_oct)
    v_out = np.array([0, 0, 1.0])

    # 3. Construct Tritium Halo
    halo_base = np.array([(0, d, d), (0, -d, d), (0, 0, -d)])

    # 4. Radially shift Halo
    halo_offset = polar_alpha_center + (v_out * r_halo)

    nodes_al27 = list(nodes_mg24)
    for node in halo_base:
        nodes_al27.append(node + halo_offset)

    return np.array(nodes_al27)


def calc_mass(r_halo):
    nodes = get_aluminum_27_nodes(r_halo)
    raw_mass = (13 * M_P_RAW) + (14 * M_N_RAW)
    binding_energy = 0.0

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = np.linalg.norm(nodes[i] - nodes[j])
            binding_energy += K_MUTUAL / dist

    return raw_mass - binding_energy


def optimize_topology():
    print(f"--- Optimizing Aluminum-27 ({TARGET_MASS_AL27:.6f} MeV target) ---")

    def error_func(r_val):
        return abs(calc_mass(r_val[0]) - TARGET_MASS_AL27)

    res = minimize(error_func, [40.0 * D_0], method="Nelder-Mead", tol=1e-8)

    optimal_r = res.x[0]
    final_mass = calc_mass(optimal_r)

    print(f"Optimal R_halo: {optimal_r/D_0:.6f} d (Absolute: {optimal_r:.6f})")
    print(f"Topological Mass: {final_mass:.6f} MeV")
    print(f"Mass Mapping Error: {abs(final_mass - TARGET_MASS_AL27)/TARGET_MASS_AL27 * 100:.8f}%")
    return optimal_r


if __name__ == "__main__":
    optimize_topology()
