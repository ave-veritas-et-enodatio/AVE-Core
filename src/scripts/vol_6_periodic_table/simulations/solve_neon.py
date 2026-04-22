"""
AVE SUBMODULE: NEON-20 TOPOLOGICAL SOLVER
-------------------------------------------
Calculates the required macroscopic separation distance (R_bipyramid) 
for the 5 constituent Alpha-particle cores in Neon-20 
arranged in a Triangular Bipyramid.
"""

# Ensure the core framework is in PATH
import pathlib

import numpy as np
from scipy.optimize import minimize

# All constants imported from the physics engine — zero hardcoded values
from ave.core.constants import D_PROTON as D_0
from ave.core.constants import K_MUTUAL
from ave.core.constants import M_N_MEV_TARGET as M_N_RAW
from ave.core.constants import M_P_MEV_TARGET as M_P_RAW


project_root = pathlib.Path(__file__).parent.parent.parent.absolute()
# Target Empirical CODATA Nuclear Mass for Neon-20 (MeV)
# 19.9924401762 amu * 931.494102 MeV/amu - (10 * 0.51099895 MeV)
TARGET_MASS_NE20 = 18617.730119


def get_neon_20_nodes(r_bipyramid):
    """
    Constructs the 20-nucleon array (5 Alphas in a Triangular Bipyramid).
    """
    # 1. Base Alpha Geometry (Tetrahedron of span 2d)
    d = D_0
    alpha_base = np.array([(d, d, d), (-d, -d, d), (-d, d, -d), (d, -d, -d)])

    # 2. Triangular Bipyramid Vertices at radius R
    # 2 polar nodes (z-axis), 3 equatorial nodes (xy-plane)
    equator_angles = [0, 2 * np.pi / 3, 4 * np.pi / 3]

    macro_centers = []
    # Polar
    macro_centers.append((0, 0, r_bipyramid))
    macro_centers.append((0, 0, -r_bipyramid))

    # Equatorial
    for theta in equator_angles:
        macro_centers.append((r_bipyramid * np.cos(theta), r_bipyramid * np.sin(theta), 0))

    macro_centers = np.array(macro_centers)

    # 3. Compile the 20 nodes
    nodes = []
    for center in macro_centers:
        for node in alpha_base:
            nodes.append(node + center)

    return np.array(nodes)


def calc_mass(r_bipyramid):
    nodes = get_neon_20_nodes(r_bipyramid)
    raw_mass = (10 * M_P_RAW) + (10 * M_N_RAW)
    binding_energy = 0.0

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = np.linalg.norm(nodes[i] - nodes[j])
            binding_energy += K_MUTUAL / dist

    return raw_mass - binding_energy


def optimize_topology():
    print(f"--- Optimizing Neon-20 ({TARGET_MASS_NE20:.6f} MeV target) ---")

    def error_func(r_val):
        return abs(calc_mass(r_val[0]) - TARGET_MASS_NE20)

    res = minimize(error_func, [20.0 * D_0], method="Nelder-Mead", tol=1e-8)

    optimal_r = res.x[0]
    final_mass = calc_mass(optimal_r)

    print(f"Optimal R_bipyramid: {optimal_r/D_0:.6f} d (Absolute: {optimal_r:.6f})")
    print(f"Topological Mass: {final_mass:.6f} MeV")
    print(f"Mass Mapping Error: {abs(final_mass - TARGET_MASS_NE20)/TARGET_MASS_NE20 * 100:.8f}%")
    return optimal_r


if __name__ == "__main__":
    optimize_topology()
