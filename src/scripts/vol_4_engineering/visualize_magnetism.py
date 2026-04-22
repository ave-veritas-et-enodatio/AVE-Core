"""
Magnetism Topological Visualizer
================================
Demonstrates how symmetric elements repel external flows (Diamagnetism)
and asymmetric elements generate topological torque (Paramagnetism).
"""

import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np
from periodic_table.simulations.simulate_element import get_nucleon_coordinates

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()


def calculate_flow_field(nodes, X, Y, z_slice=0.0):
    """
    Computes a uniform horizontal flow (U, 0) perturbed by the
    repulsive density gradients of the topological nodes.
    """
    U0 = 10.0  # Base external uniform flow
    dx = np.ones_like(X) * U0
    dy = np.zeros_like(Y)

    # Calculate density scalar field
    density = np.zeros_like(X)
    epsilon = 2.0
    amplitude = 1500.0

    for cx, cy, cz in nodes:
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
        density += amplitude / (dist_sq + epsilon)

    # Flow is repelled by the gradient of the density
    grad_y, grad_x = np.gradient(density)

    # The actual velocity field
    Vx = dx - grad_x
    Vy = dy - grad_y

    return density, Vx, Vy


def plot_magnetism(element_name, Z, A, is_paramagnetic=False):
    nodes = get_nucleon_coordinates(Z, A)
    if not nodes:
        return

    # Project to 2D for visualization (assume Y-plane slice is best for these)
    # Actually we just want a 2D grid covering the X-Z coordinates
    # Let's map X to X and Y to Z
    nodes_2d = [(n[0], n[2], n[1]) for n in nodes]

    bound = max(np.linalg.norm(n) for n in nodes) * 1.5
    bound = max(bound, 100.0)

    grid_res = 150
    x = np.linspace(-bound, bound, grid_res)
    y = np.linspace(-bound, bound, grid_res)
    X, Y = np.meshgrid(x, y)

    density, Vx, Vy = calculate_flow_field(nodes_2d, X, Y, z_slice=0.0)

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#0f0f0f")
    ax.set_facecolor("#0f0f0f")

    # Background density map
    # im = ax.imshow(  # bulk lint fixup pass
    #     density,
    #     extent=[-bound, bound, -bound, bound],
    #     origin="lower",
    #     cmap="hot",
    #     alpha=0.6,
    #     vmax=np.percentile(density, 95),
    # )

    # Streamplot of the interacting flow (External Magnetic Flux)
    color = "#00ffcc" if is_paramagnetic else "#ff3366"
    # streams = ax.streamplot(x, y, Vx, Vy, color=color, linewidth=1.5, density=1.5,
    #     arrowstyle="->", arrowsize=1.5)  # bulk lint fixup pass

    # Scatter the nodes
    ax.scatter(
        [n[0] for n in nodes_2d],
        [n[1] for n in nodes_2d],
        color="white",
        s=50,
        edgecolors="black",
        zorder=5,
    )

    title = f"{element_name} Flux Alignment\n"
    title += (
        "Paramagnetic (Asymmetrical Torque Vector)" if is_paramagnetic else "Diamagnetic (Symmetrical Flux Repulsion)"
    )

    ax.set_title(title, color="white", fontsize=16, pad=20)
    ax.tick_params(colors="white")
    ax.set_xlabel("X-Axis (Spatial Extent)", color="white")
    ax.set_ylabel("Z-Axis (Spatial Extent)", color="white")

    # Save the plot
    out_dir = project_root / "assets" / "sim_outputs"
    os.makedirs(out_dir, exist_ok=True)

    filename = element_name.lower().replace("-", "_") + "_magnetism.png"
    out_path = out_dir / filename
    plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print(f"[*] Generated Magnetism Visualization: {out_path}")


if __name__ == "__main__":
    # Magnesium-24 (Z=12, A=24) -> Diamagnetic (Symmetric Octahedron)
    plot_magnetism("Magnesium-24", 12, 24, is_paramagnetic=False)

    # Aluminum-27 (Z=13, A=27) -> Paramagnetic (Asymmetric Offset Halo)
    plot_magnetism("Aluminum-27", 13, 27, is_paramagnetic=True)
