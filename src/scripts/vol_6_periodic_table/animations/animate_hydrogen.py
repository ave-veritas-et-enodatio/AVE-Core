import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

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
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
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
    fig.patch.set_facecolor("#0f0f0f")

    def update(frame):
        ax.clear()
        ax.set_facecolor("#0f0f0f")
        angle = frame * (2 * np.pi / frames)
        rotated_mesh = rotate_mesh_y(mesh_points, angle)

        density = calculate_vacuum_density_from_mesh(rotated_mesh, X, Y)
        cmap = plt.cm.inferno
        cmap.set_bad(color="#0f0f0f")
        ax.imshow(
            density,
            extent=[-bound, bound, -bound, bound],
            origin="lower",
            cmap=cmap,
            alpha=0.9,
            vmin=0.0,
        )

        grad_y, grad_x = np.gradient(density)
        ax.streamplot(
            x,
            y,
            grad_x,
            grad_y,
            color="#aaaaaa",
            linewidth=1.2,
            density=1.5,
            arrowstyle="->",
            arrowsize=1.5,
        )

        for cx, cy, cz in rotated_mesh:
            depth_scale = np.exp(-np.abs(cz))
            ax.scatter(cx, cy, color="#ff3366", s=50 * depth_scale, marker="o", linewidth=1, alpha=0.8)

        ax.set_title(
            "Hydrogen-1 ($^1H$): Dynamic Transverse Vacuum Strain",
            color="white",
            fontsize=16,
            pad=20,
        )
        ax.tick_params(colors="white")

    print("[*] Rendering Hydrogen-1 GIF...")
    anim = FuncAnimation(fig, update, frames=frames, interval=80, blit=False)
    outdir = "../figures"
    os.makedirs(outdir, exist_ok=True)
    anim.save(
        os.path.join(outdir, "hydrogen_1_dynamic_flux.gif"),
        writer="pillow",
        fps=15,
        savefig_kwargs={"facecolor": fig.get_facecolor()},
    )
    print("[*] Done.")
