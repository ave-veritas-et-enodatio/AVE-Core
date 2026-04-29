import sys

import numpy as np
from scipy.optimize import basinhopping

# All constants imported from the physics engine — zero hardcoded values
from ave.core.constants import D_PROTON as D_MIN
from ave.core.constants import K_MUTUAL
from ave.core.constants import M_N_MEV_TARGET as M_N_RAW
from ave.core.constants import M_P_MEV_AVE as M_P_RAW


def evaluate_binding_energy(positions: np.ndarray) -> float:
    """
    Computes theoretical mass defect using EE Mutual Impedance.
    positions: 1D array of length 3N representing (x,y,z) for N nucleons.
    """
    nodes = np.array(positions).reshape(-1, 3)
    n_nodes = len(nodes)

    binding_energy = 0.0
    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            dist = np.linalg.norm(nodes[i] - nodes[j])

            # Repulsive hard sphere core to prevent overlap
            if dist < D_MIN:
                # Infinite penalty for overlapping nodes
                return -1e9

            binding_energy += K_MUTUAL / dist

    return binding_energy


def objective_function(positions: np.ndarray, Z: int, A: int, target_mass: float) -> float:
    """
    Minimizes the error between theoretical and empirical mass.
    Returns absolute error in MeV.
    """
    N = A - Z
    raw_mass = (Z * M_P_RAW) + (N * M_N_RAW)

    binding_energy = evaluate_binding_energy(positions)
    theo_mass = raw_mass - binding_energy

    # We want to minimize the difference between theoretical mass and target mass
    # Add a large penalty if atoms overlap (binding energy is negative)
    if binding_energy < 0:
        return 1e9

    return abs(theo_mass - target_mass)


def find_optimal_topology(Z: int, A: int, empirical_mass_mev: float, n_iter: int = 1000) -> np.ndarray | None:
    """
    Uses Basinhopping (global optimization) to find the spatial coordinates
    that perfectly match the empirical mass defect.
    """
    N_nucleons = A
    print(f"--- Solving Topological Geometry for Z={Z}, A={A} ---")
    print(f"Target Mass: {empirical_mass_mev:.3f} MeV")

    # Initial guess: random distribution in a small sphere
    np.random.seed(42)
    initial_guess = np.random.uniform(-5.0, 5.0, 3 * N_nucleons)

    # Define bounds to prevent particles from flying to infinity
    # Bounds: +/- 100d max radius
    bounds = [(-100.0, 100.0)] * (3 * N_nucleons)

    minimizer_kwargs = {"method": "L-BFGS-B", "bounds": bounds, "args": (Z, A, empirical_mass_mev)}

    # Run global optimization
    print(f"Running Basinhopping Global Optimizer ({n_iter} iterations)...")
    res = basinhopping(
        objective_function,
        initial_guess,
        minimizer_kwargs=minimizer_kwargs,
        niter=n_iter,
        stepsize=2.0,
    )

    if res.success:
        print("\n[+] Convergence Found!")
        final_positions = res.x.reshape(-1, 3)
        final_mass = (Z * M_P_RAW) + ((A - Z) * M_N_RAW) - evaluate_binding_energy(res.x)
        error = abs(final_mass - empirical_mass_mev)

        print(f"Optimal Mass: {final_mass:.3f} MeV")
        print(f"Mass Error:   {error:.6f} MeV")
        print("Generated Coordinates (x,y,z):")
        for i, pos in enumerate(final_positions):
            val = f"({pos[0]:.4f}, {pos[1]:.4f}, {pos[2]:.4f})"
            print(f"  Node {i+1}:\t{val}")

        return final_positions
    else:
        print("\n[-] Optimization Failed to Converge.")
        return None


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        # Nitrogen-14 (Z=7, A=14)
        # 1 amu = 931.494102 MeV/c^2
        # N-14 atomic mass = 14.003074 amu
        # Nucleus mass = N-14 atomic mass - 7 * electron mass
        n14_mass_mev = (14.003074 - (7 * 0.00054858)) * 931.494102

        find_optimal_topology(7, 14, n14_mass_mev, n_iter=10)
