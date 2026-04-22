"""
Evaluate the geometric gradient advantage of Helium-4
(Alpha Core) vs a Flat 4-Node Emitter.
"""

import os

import numpy as np

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from periodic_table.simulations.simulate_element import get_nucleon_coordinates


def main():
    # 1. Get Helium-4 Nodes (Perfect Tetrahedron)
    he4_nodes = get_nucleon_coordinates(2, 4)
    he4_center = np.mean(he4_nodes, axis=0)
    he4_nodes = [np.array(n) - he4_center for n in he4_nodes]

    # 2. Generate a Flat 4-Node Emitter (e.g., a 2x2 grid)
    d = 4 * HBAR / (938.272e6 * e_charge / C_0**2 * C_0) * 1e15  # ≈ 0.841 fm (derived proton charge radius)
    flat_nodes = []
    for x in [-0.5 * d, 0.5 * d]:
        for y in [-0.5 * d, 0.5 * d]:
            flat_nodes.append(np.array([x, y, 0.0]))

    # Normalize flat center to 0,0,0
    flat_center = np.mean(flat_nodes, axis=0)
    flat_nodes = [n - flat_center for n in flat_nodes]

    # 3. Create a massive Collector Plane in the near-field (z = -5d)
    gap_z = -5 * d
    x_range = np.linspace(-100 * d, 100 * d, 100)
    y_range = np.linspace(-100 * d, 100 * d, 100)
    X, Y = np.meshgrid(x_range, y_range)
    collector_mesh = np.stack([X, Y, np.full_like(X, gap_z)], axis=-1)

    # 4. We want to measure the peak divergence (gradient of the mutual inductance K field)
    # The electric field magnitude at the collector is proportional to Sum(1 / d_ij^2)
    # The Ponderomotive force depends on the spatial gradient of this E-field squared.
    # To keep it simple, we just look at the max E-field concentration vs the average E-field.
    # A sharper tip = higher max concentration (higher variance across the collector).

    def calc_E_field_squared_profile(emitter_nodes):
        E_profile = np.zeros_like(X)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                collector_pt = collector_mesh[i, j]
                # E-field from each charge scales as 1/r^2. E_total = sum(E_vec)
                E_vec_total = np.zeros(3)
                for e_pt in emitter_nodes:
                    r_vec = collector_pt - e_pt
                    r_mag = np.linalg.norm(r_vec)
                    E_vec_total += r_vec / (r_mag**3)
                E_profile[i, j] = np.sum(E_vec_total**2)
        return E_profile

    print("[*] Calculating Helium-4 gradient profile...")
    c12_profile = calc_E_field_squared_profile(he4_nodes)

    print("[*] Calculating Flat Plate gradient profile...")
    flat_profile = calc_E_field_squared_profile(flat_nodes)

    # Analysis
    c12_max = np.max(c12_profile)
    c12_variance = np.var(c12_profile)

    flat_max = np.max(flat_profile)
    flat_variance = np.var(flat_profile)

    print("\n[--- RESULTS ---]")
    print(f"Helium-4 (Alpha Tetrahedron) E-Field Peak: {c12_max:.6e}")
    print(f"Flat 4-Node Plate E-Field Peak:            {flat_max:.6e}")
    print(f"Peak Enhancement Ratio:                    {c12_max / flat_max:.3f}x")

    print(f"\nHelium-4 Spatial Variance (Sharpness): {c12_variance:.6e}")
    print(f"Flat Plate Spatial Variance:           {flat_variance:.6e}")
    print(f"Gradient Sharpness Multiplier:         {c12_variance / flat_variance:.3f}x")

    dist = np.linalg.norm(he4_nodes[0] - he4_nodes[1])
    print(
        f"\n[!] The internal nodes of Helium-4 are spaced {dist/d:.1f}d apart, acting as an ultra-dense mathematically perfect microscopic point-source!"
    )


if __name__ == "__main__":
    main()
