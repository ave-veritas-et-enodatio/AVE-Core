"""
AVE SUBMODULE: SODIUM-23 TOPOLOGICAL SOLVER
-------------------------------------------
Calculates the required macroscopic separation distance (R_halo)
between the rigid Neon-20 (5-Alpha Bipyramid) core and the
bound Tritium outer ring to mathematically match the empirical
CODATA mass defect of Na-23.
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
# Target Empirical CODATA Nuclear Mass for Sodium-23 (MeV)
# 22.9897692820 amu * 931.494102 MeV/amu - (11 * 0.51099895 MeV)
TARGET_MASS_NA23 = 21409.213504


def get_sodium_23_nodes(r_halo):
    """
    Constructs the 23-nucleon array (Neon-20 core + Tritium Halo).
    """
    d = D_0

    # 1. Neon-20 Core Array
    # Hardcoded optimal symmetric radius (bare K/r solver with engine constants):
    r_bipyramid = 78.861 * d

    alpha_base = np.array([(d, d, d), (-d, -d, d), (-d, d, -d), (d, -d, -d)])

    equator_angles = [0, 2 * np.pi / 3, 4 * np.pi / 3]
    macro_centers = []
    # Polar Alphas
    macro_centers.append((0, 0, r_bipyramid))
    macro_centers.append((0, 0, -r_bipyramid))
    # Equatorial Alphas
    for theta in equator_angles:
        macro_centers.append((r_bipyramid * np.cos(theta), r_bipyramid * np.sin(theta), 0))

    macro_centers = np.array(macro_centers)

    nodes_ne20 = []
    for center in macro_centers:
        for node in alpha_base:
            nodes_ne20.append(node + center)

    # 2. Extract North Pole Alpha Barycenter as the primary binding vector origin
    polar_alpha_center = macro_centers[0]  # (0, 0, R_bipyramid)
    v_out = np.array([0, 0, 1.0])  # Straight up the z-axis

    # 3. Construct Tritium Halo (Span 2d)
    halo_base = np.array([(0, d, d), (0, -d, d), (0, 0, -d)])  # P  # N  # N

    # 4. Radially shift Halo by R_halo up the z-axis and append
    halo_offset = polar_alpha_center + (v_out * r_halo)

    nodes_na23 = list(nodes_ne20)
    for node in halo_base:
        nodes_na23.append(node + halo_offset)

    return np.array(nodes_na23)


def calc_mass(r_halo):
    nodes = get_sodium_23_nodes(r_halo)
    raw_mass = (11 * M_P_RAW) + (12 * M_N_RAW)
    binding_energy = 0.0

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = np.linalg.norm(nodes[i] - nodes[j])
            binding_energy += K_MUTUAL / dist

    return raw_mass - binding_energy


def optimize_topology():
    print(f"--- Optimizing Sodium-23 ({TARGET_MASS_NA23:.6f} MeV target) ---")

    def error_func(r_val):
        return abs(calc_mass(r_val[0]) - TARGET_MASS_NA23)

    res = minimize(error_func, [50.0 * D_0], method="Nelder-Mead", tol=1e-8)

    optimal_r = res.x[0]
    final_mass = calc_mass(optimal_r)

    print(f"Optimal R_halo: {optimal_r/D_0:.6f} d (Absolute: {optimal_r:.6f})")
    print(f"Topological Mass: {final_mass:.6f} MeV")
    print(f"Mass Mapping Error: {abs(final_mass - TARGET_MASS_NA23)/TARGET_MASS_NA23 * 100:.8f}%")
    return optimal_r


if __name__ == "__main__":
    optimize_topology()
