"""
AVE SUBMODULE: OXYGEN-16 TOPOLOGICAL SOLVER
-------------------------------------------
Calculates the required macroscopic separation distance (R_tet) between the
four constituent Alpha-particle cores in Oxygen-16 to perfectly match the
empirical CODATA mass defect (Binding Energy) using purely electrical 1/d_ij coupling.
"""

import numpy as np
from scipy.optimize import minimize

# All constants imported from the physics engine — zero hardcoded values
from ave.core.constants import D_PROTON as D_0
from ave.core.constants import K_MUTUAL
from ave.core.constants import M_N_MEV_TARGET as M_N_RAW
from ave.core.constants import M_P_MEV_TARGET as M_P_RAW

# Target Empirical CODATA Mass for Oxygen-16 (MeV)
# 15.99491461957 amu * 931.494102 MeV/amu - (8 * 0.51099895 MeV)
TARGET_MASS_O16 = 14895.080


def get_oxygen_16_nodes(r_tet: float) -> np.ndarray:
    """
    Constructs the 16-nucleon array (4 Alphas arranged in a giant tetrahedron).
    """
    # Standard Alpha Core Geometry (Tetrahedron of span 2d)
    d = D_0
    alpha_base = np.array([(d, d, d), (-d, -d, d), (-d, d, -d), (d, -d, -d)])

    # The Macro-Tetrahedron (The positions of the 4 Alpha centers)
    # R_tet is the radial distance from the origin (0,0,0) to each Alpha center
    macro_centers = np.array(
        [
            (r_tet / np.sqrt(3), r_tet / np.sqrt(3), r_tet / np.sqrt(3)),
            (-r_tet / np.sqrt(3), -r_tet / np.sqrt(3), r_tet / np.sqrt(3)),
            (-r_tet / np.sqrt(3), r_tet / np.sqrt(3), -r_tet / np.sqrt(3)),
            (r_tet / np.sqrt(3), -r_tet / np.sqrt(3), -r_tet / np.sqrt(3)),
        ]
    )

    nodes = []
    # Translate the baseline alpha core to each of the 4 macroscopic vertices
    for center in macro_centers:
        for node in alpha_base:
            nodes.append(node + center)

    return np.array(nodes)


def calc_mass(r_tet: float) -> float:
    """
    Calculates the topological mass of the O-16 lattice given an R_tet separation.
    """
    nodes = get_oxygen_16_nodes(r_tet)

    raw_mass = (8 * M_P_RAW) + (8 * M_N_RAW)
    binding_energy = 0.0

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = np.linalg.norm(nodes[i] - nodes[j])
            binding_energy += K_MUTUAL / dist

    return raw_mass - binding_energy


def optimize_topology() -> float:
    print(f"--- Optimizing Oxygen-16 ({TARGET_MASS_O16} MeV target) ---")

    # Error function to minimize
    def error_func(r_val):
        return abs(calc_mass(r_val[0]) - TARGET_MASS_O16)

    # Initial guess: 10 * D_0
    res = minimize(error_func, [10.0 * D_0], method="Nelder-Mead", tol=1e-8)

    optimal_r = res.x[0]
    final_mass = calc_mass(optimal_r)

    print(f"Optimal R_tet: {optimal_r:.6f} d (where d={D_0} fm)")
    print(f"Topological Mass: {final_mass:.6f} MeV")
    print(f"Mass Mapping Error: {abs(final_mass - TARGET_MASS_O16)/TARGET_MASS_O16 * 100:.8f}%")
    return optimal_r


if __name__ == "__main__":
    optimize_topology()
