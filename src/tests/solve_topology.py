from typing import Any

import numpy as np
from vol_6_periodic_table.simulations.simulate_element import M_N_RAW, M_P_RAW

# Exact K_MUTUAL derived from the perfect Alpha particle (Helium-4)
K_MUTUAL = 11.3378

d = 0.85  # Topological nodal offset (fm)


def solve_topology_for_mass(Z: int, A: int, empirical_mass_mev: float, nodes_generator: Any) -> float:
    """
    Reverse-engineers the required internal spatial arrangement of a given topology
    to match the empirical CODATA mass defect.
    """
    raw_mass = (Z * M_P_RAW) + ((A - Z) * M_N_RAW)
    target_binding_energy = raw_mass - empirical_mass_mev

    print(f"--- Solving Topology for Z={Z}, A={A} ---")
    print(f"Empirical Mass: {empirical_mass_mev:.3f} MeV")
    print(f"Raw Mass: {raw_mass:.3f} MeV")
    print(f"Target Binding Energy (Mutual Impedance): {target_binding_energy:.3f} MeV\n")

    best_param = None
    min_error = float("inf")
    best_be = 0

    # We sweep the spatial parameter (radius or offset)
    for param in np.linspace(10.0, 50.0, 100000):
        nodes = nodes_generator(param)

        binding_energy = 0.0
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                dist = np.linalg.norm(np.array(nodes[i]) - np.array(nodes[j]))
                if dist > 0:
                    binding_energy += K_MUTUAL / dist

        error = abs(binding_energy - target_binding_energy)
        if error < min_error:
            min_error = error
            best_param = param
            best_be = binding_energy

    print(f"Best Parameter: {best_param:.4f}")
    print(f"Resulting Binding Energy: {best_be:.3f} MeV (Error: {min_error:.4f} MeV)\n")
    return best_param


# --- Carbon-12 (3 Alpha Ring) ---
# Carbon-12 mass from CODATA
CARBON_12_MASS_MEV = 11174.862


def carbon_12_ring(ring_radius: float) -> list[tuple[float, float, float]]:
    """
    Carbon-12 is 3 Alpha particles arranged in an equilateral triangle/ring.
    The parameter is the distance from the center to each Alpha core.
    """
    alpha = [(d, d, d), (-d, -d, d), (-d, d, -d), (d, -d, -d)]
    nodes = []

    for i in range(3):
        angle = i * (2 * np.pi / 3)
        cx = ring_radius * np.cos(angle)
        cy = ring_radius * np.sin(angle)
        cz = 0

        for n in alpha:
            nodes.append((n[0] + cx, n[1] + cy, n[2] + cz))

    return nodes


if __name__ == "__main__":
    r_carbon = solve_topology_for_mass(6, 12, CARBON_12_MASS_MEV, carbon_12_ring)
    print(f"[*] Carbon-12 3-Alpha Ring Radius: {r_carbon/d:.4f} * d")
