import os
import sys
import matplotlib.pyplot as plt
import pathlib

# Ensure the core framework is in PATH
project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from ave.topological.borromean import FundamentalTopologies
from periodic_table.simulations.simulate_element import get_nucleon_coordinates


def rotate_coordinates(mesh, rx, ry, rz):
    Rx = np.array([[1, 0, 0], [0, np.cos(rx), -np.sin(rx)], [0, np.sin(rx), np.cos(rx)]])
    Ry = np.array([[np.cos(ry), 0, np.sin(ry)], [0, 1, 0], [-np.sin(ry), 0, np.cos(ry)]])
    Rz = np.array([[np.cos(rz), -np.sin(rz), 0], [np.sin(rz), np.cos(rz), 0], [0, 0, 1]])
    R = Rz.dot(Ry).dot(Rx)
    return mesh.dot(R.T)


def plot_combined_mesh(nodes, title, filename, exploded_factor=1.0):
    """
    Renders the unified 3D Borromean mesh manifold for a given set of nucleon coordinates.
    `exploded_factor` > 1.0 radially scales the node coordinates for an exploded diagram context.
    """
    fig = plt.figure(figsize=(12, 12), facecolor="black")
    ax = fig.add_subplot(111, projection="3d")

    # Get base 6^3_2 Borromean Link mesh (Proton topology returns 3 intersecting rings)
    base_rings = FundamentalTopologies.generate_borromean_6_3_2(radius=1.0, resolution=200)

    # Render each nucleon in the active element array
    for nx, ny, nz in nodes:
        # Scale coordinates for exploded view if requested
        sx, sy, sz = nx * exploded_factor, ny * exploded_factor, nz * exploded_factor

        # Apply slight random orientation jitter for structural noise visual variety
        rx = np.random.uniform(0, np.pi / 4)
        ry = np.random.uniform(0, np.pi / 4)

        # Plot each ring within the Borromean triplet
        for ring in base_rings:
            rotated = rotate_coordinates(ring, rx, ry, 0)
            translated = rotated + np.array([sx, sy, sz])

            # Extract x, y, z arrays from the resulting N x 3 mesh
            X_sh = translated[:, 0]
            Y_sh = translated[:, 1]
            Z_sh = translated[:, 2]

            # Plot ribbon
            ax.plot(X_sh, Y_sh, Z_sh, color="cyan", alpha=0.6, linewidth=0.5)
            # Plot volumetric density scatter
            ax.scatter(X_sh[::4], Y_sh[::4], Z_sh[::4], color="blue", s=0.1, alpha=0.1)

    # Styling
    ax.set_facecolor("black")
    ax.grid(False)
    ax.axis("off")

    # Calculate bounding box for consistent scaling
    if exploded_factor > 1.0:
        bounds = max([np.linalg.norm(n) for n in nodes]) * exploded_factor + 2
    else:
        bounds = max([np.linalg.norm(n) for n in nodes]) + 2

    ax.set_xlim([-bounds, bounds])
    ax.set_ylim([-bounds, bounds])
    ax.set_zlim([-bounds, bounds])
    ax.set_title(title, color="white", pad=20)

    # Set viewing angle
    ax.view_init(elev=20, azim=45)

    # Ensure export directory
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename, dpi=300, bbox_inches="tight", facecolor="black")
    plt.close()
    print(f"[*] Saved 3D Mesh: {filename}")


if __name__ == "__main__":
    import numpy as np  # Ensure local scope

    elements = [
        {"name": "Hydrogen-1", "Z": 1, "A": 1},
        {"name": "Helium-4", "Z": 2, "A": 4},
        {"name": "Lithium-7", "Z": 3, "A": 7},
        {"name": "Beryllium-9", "Z": 4, "A": 9},
        {"name": "Boron-11", "Z": 5, "A": 11},
        {"name": "Carbon-12", "Z": 6, "A": 12},
        {"name": "Nitrogen-14", "Z": 7, "A": 14},
    ]

    outdir = "periodic_table/figures"

    print("--- AVE Unified 3D Mesh Generator ---")
    np.random.seed(42)  # Lock rotations for canonical diagrams

    for el in elements:
        print(f"Generating 3D manifolds for {el['name']} (Z={el['Z']})...")
        nodes = get_nucleon_coordinates(el["Z"], el["A"])
        if not nodes:
            continue

        # Generate the standard bound structural mesh
        bound_file = f"{outdir}/{el['name'].lower().replace('-','_')}_bound.png"
        plot_combined_mesh(nodes, f"{el['name']} Bound Topology ($6^3_2$ Interlocking Manifold)", bound_file, 1.0)

        # If the nucleus is multi-nucleon, generate an exploded structural mesh for clarity
        if len(nodes) > 1:
            exploded_file = f"{outdir}/{el['name'].lower().replace('-','_')}_exploded.png"
            plot_combined_mesh(nodes, f"{el['name']} Exploded Topology (Visual Node Spacing)", exploded_file, 3.0)

    print("--- Generation Complete ---")
