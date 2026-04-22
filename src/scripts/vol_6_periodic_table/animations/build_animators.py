import os

output_dir = "periodic_table/animations"
os.makedirs(output_dir, exist_ok=True)

# 1. Hydrogen (Uses mesh rotation)
h1_code = """import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pathlib

# Ensure the core framework is in PATH
project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from ave.topological.borromean import FundamentalTopologies

def rotate_mesh_y(mesh, angle):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    return mesh.dot(R.T)

def calculate_vacuum_density_from_mesh(mesh_points, X, Y, z_slice=0.0):
    density_field = np.zeros_like(X)
    amplitude = 100.0 / len(mesh_points)
    epsilon = 0.5
    for pt in mesh_points:
        cx, cy, cz = pt
        dist_sq = (X - cx)**2 + (Y - cy)**2 + (z_slice - cz)**2
        density_field += amplitude / (dist_sq + epsilon)
    return density_field

if __name__ == "__main__":
    bound, grid_res, frames = 3.0, 80, 60
    x = np.linspace(-bound, bound, grid_res)
    y = np.linspace(-bound, bound, grid_res)
    X, Y = np.meshgrid(x, y)

    rings = FundamentalTopologies.generate_borromean_6_3_2(radius=1.0, resolution=100)
    mesh_points = np.array([pt for ring in rings for pt in ring[::5]]) * 1.2

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor('#0f0f0f')

    def update(frame):
        ax.clear()
        ax.set_facecolor('#0f0f0f')
        angle = frame * (2 * np.pi / frames)
        rotated_mesh = rotate_mesh_y(mesh_points, angle)

        density = calculate_vacuum_density_from_mesh(rotated_mesh, X, Y)
        cmap = plt.cm.inferno
        cmap.set_bad(color='#0f0f0f')
        ax.imshow(density, extent=[-bound, bound, -bound, bound], origin='lower', cmap=cmap, alpha=0.9, vmin=0.0)

        grad_y, grad_x = np.gradient(density)
        ax.streamplot(x, y, grad_x, grad_y, color='#aaaaaa', linewidth=1.2, density=1.5, arrowstyle='->', arrowsize=1.5)

        for cx, cy, cz in rotated_mesh:
            depth_scale = np.exp(-np.abs(cz))
            ax.scatter(cx, cy, color='#ff3366', s=50 * depth_scale, marker='o', linewidth=1, alpha=0.8)

        ax.set_title("Hydrogen-1 ($^1H$): Dynamic Transverse Vacuum Strain", color='white', fontsize=16, pad=20)
        ax.tick_params(colors='white')

    print("[*] Rendering Hydrogen-1 GIF...")
    anim = FuncAnimation(fig, update, frames=frames, interval=80, blit=False)
    outdir = "../figures"
    os.makedirs(outdir, exist_ok=True)
    anim.save(os.path.join(outdir, "hydrogen_1_dynamic_flux.gif"), writer='pillow', fps=15,
        savefig_kwargs={'facecolor': fig.get_facecolor()})
    print("[*] Done.")
"""

# Base Template for multi-node elements
base_template = """import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pathlib

# Ensure the core framework is in PATH
project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from periodic_table.simulations.simulate_element import get_nucleon_coordinates

def rotate_cluster_y(nodes, angle):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    return [np.dot(R, n) for n in nodes]

def calculate_vacuum_density(nodes, X, Y, z_slice=0.0):
    density_field = np.zeros_like(X)
    amplitude, epsilon = 100.0, 0.5
    for cx, cy, cz in nodes:
        dist_sq = (X - cx)**2 + (Y - cy)**2 + (z_slice - cz)**2
        density_field += amplitude / (dist_sq + epsilon)
    return density_field

if __name__ == "__main__":
    Z, A = {Z}, {A}
    bound, grid_res, frames = {BOUND}, 80, 60
    name = "{NAME}"
    title = "{TITLE}"

    nodes = get_nucleon_coordinates(Z, A)
    if not nodes:
        print(f"Error: No coordinates for Z={{Z}}, A={{A}}")
        sys.exit(1)

    x = np.linspace(-bound, bound, grid_res)
    y = np.linspace(-bound, bound, grid_res)
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor('#0f0f0f')

    def update(frame):
        ax.clear()
        ax.set_facecolor('#0f0f0f')
        angle = frame * (2 * np.pi / frames)
        rotated_nodes = rotate_cluster_y(nodes, angle)

        density = calculate_vacuum_density(rotated_nodes, X, Y)
        cmap = plt.cm.inferno
        cmap.set_bad(color='#0f0f0f')
        ax.imshow(density, extent=[-bound, bound, -bound, bound], origin='lower', cmap=cmap, alpha=0.9, vmin=0.0)

        grad_y, grad_x = np.gradient(density)
        ax.streamplot(x, y, grad_x, grad_y, color='#aaaaaa', linewidth=1.2, density=1.5, arrowstyle='->', arrowsize=1.5)

        for cx, cy, cz in rotated_nodes:
            depth_scale = np.exp(-np.abs(cz / (bound/3.0)))
            ax.scatter(cx, cy, color='#00ffcc', s=300 * depth_scale, marker='+', linewidth=2, alpha=0.8)
            ax.scatter(cx, cy, color='#00ffcc', s=100 * depth_scale, edgecolor='#00ffcc',
                facecolor='none', linewidth=1.5, alpha=0.9)

        ax.set_title(title, color='white', fontsize=16, pad=20)
        ax.tick_params(colors='white')

    print(f"[*] Rendering {name} GIF...")
    anim = FuncAnimation(fig, update, frames=frames, interval=80, blit=False)
    outdir = "../figures"
    os.makedirs(outdir, exist_ok=True)
    anim.save(os.path.join(outdir, "{NAME}_dynamic_flux.gif"), writer='pillow', fps=15,
        savefig_kwargs={'facecolor': fig.get_facecolor()})
    print("[*] Done.")
"""

elements = [
    (2, 4, 3.0, "helium_4", "Helium-4 ($^4He$): Dynamic Transverse Vacuum Strain"),
    (3, 7, 15.0, "lithium_7", "Lithium-7 ($^7Li$): Asymmetrical Secondary Shell Strain"),
    (4, 9, 10.0, "beryllium_9", "Beryllium-9 ($^9Be$): Stretched Dual-Core Strain"),
    (5, 11, 15.0, "boron_11", "Boron-11 ($^{11}B$): Massive Parasitic Halo Strain"),
    (6, 12, 65.0, "carbon_12", "Carbon-12 ($^{12}C$): Subcritical $3\\\\alpha$ Ring Strain"),
    (7, 14, 15.0, "nitrogen_14", "Nitrogen-14 ($^{14}N$): Optimized Asymmetric Mesh Strain"),
    (8, 16, 75.0, "oxygen_16", "Oxygen-16 ($^{16}O$): $4\\\\alpha$ Macro-Tetrahedron Strain"),
]

with open(f"{output_dir}/animate_hydrogen.py", "w") as f:
    f.write(h1_code)

for Z, A, bound, name, title in elements:
    code = base_template.replace("{Z}", str(Z)).replace("{A}", str(A))
    code = code.replace("{BOUND}", str(bound)).replace("{NAME}", name).replace("{TITLE}", title)
    filename = name.split("_")[0]
    with open(f"{output_dir}/animate_{filename}.py", "w") as f:
        f.write(code)

print("Generated all standalone scripts.")
