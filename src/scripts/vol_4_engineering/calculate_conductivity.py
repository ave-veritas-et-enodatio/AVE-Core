import numpy as np
import sys
import pathlib

# Setup paths
project_root = pathlib.Path(__file__).parent.absolute()

from periodic_table.simulations.simulate_element import get_nucleon_coordinates


def calculate_vacuum_density(nodes, X, Y, z_slice):
    density_field = np.zeros_like(X)
    amplitude, epsilon = 100.0, 0.5
    for cx, cy, cz in nodes:
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
        density_field += amplitude / (dist_sq + epsilon)
    return density_field


def get_structural_variance(Z, A):
    nodes = get_nucleon_coordinates(Z, A)
    if not nodes:
        return float("inf")

    bound, grid_res = 180.0, 80
    x = np.linspace(-bound, bound, grid_res)
    z = np.linspace(-bound, bound, grid_res)
    X, Z_mesh = np.meshgrid(x, z)

    # Sweep through the bounding box of the nucleus
    z_min = min(n[1] for n in nodes) - 1.0
    z_max = max(n[1] for n in nodes) + 1.0

    y_slices = np.linspace(z_min, z_max, 30)

    # Calculate density gradients across all slices
    global_variances = []

    for y_slice in y_slices:
        density = calculate_vacuum_density([(n[0], n[2], n[1]) for n in nodes], X, Z_mesh, y_slice)
        # We want the variance of the gradient (how "bumpy" or "unpredictable" the acoustic impedance is)
        grad_x, grad_z = np.gradient(density)
        grad_magnitude = np.sqrt(grad_x**2 + grad_z**2)

        # We only care about the variance inside the actual bounding field, not empty space
        mask = density > np.mean(density) * 0.1
        if np.any(mask):
            global_variances.append(np.var(grad_magnitude[mask]))

    return np.mean(global_variances) if global_variances else float("inf")


print(f"Structural Acoustic/Electrical Impedance Variances (Lower = Better Conductor):")
print("-" * 60)

elements = [
    ("Boron-11 (Metalloid / Semiconductor)", 5, 11),
    ("Carbon-12 (Non-Metal / Poor Conductor)", 6, 12),
    ("Neon-20 (Noble Gas / Insulator)", 10, 20),
    ("Magnesium-24 (Alkaline Earth Metal)", 12, 24),
    ("Aluminum-27 (Post-Transition Metal)", 13, 27),
    ("Silicon-28 (Metalloid / Semiconductor)", 14, 28),
]

for name, Z, A in elements:
    var = get_structural_variance(Z, A)
    print(f"{name:<40}: {var:.4f}")
