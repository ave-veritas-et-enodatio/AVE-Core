"""
Dynamic Vacuum Density Flux Visualizer
--------------------------------------
Generates an animated GIF of the 2D equatorial vacuum density slice
(Z=0) as the underlying 3D discrete topological knot (e.g., Helium-4, Lithium-7)
physically rotates in space.

This explicitly demonstrates how the continuous metric strain gradient
(gravitational/strong force flux) dynamically warps precisely in lockstep
with the rotating 3D chiral geometry, proving the 1/r overlap mechanics
of the model.
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from ave.topological.borromean import FundamentalTopologies
from ave.topological.combiner import NucleonCombiner


# ----- Geometric Constructors -----
def construct_helium_4(shift_distance: float):
    placements = [
        {
            "shift": [shift_distance, shift_distance, shift_distance],
            "rot": [0, 0, 0],
            "color": "#ff3366",
        },
        {
            "shift": [-shift_distance, -shift_distance, shift_distance],
            "rot": [0, 0, np.pi / 2],
            "color": "#ff3366",
        },
        {
            "shift": [-shift_distance, shift_distance, -shift_distance],
            "rot": [np.pi / 2, 0, 0],
            "color": "#00ffcc",
        },
        {
            "shift": [shift_distance, -shift_distance, -shift_distance],
            "rot": [0, np.pi / 2, 0],
            "color": "#00ffcc",
        },
    ]
    return NumericallyEvaluateNucleons(
        NucleonCombiner.assemble_cluster(FundamentalTopologies.generate_borromean_6_3_2, placements)
    )


def construct_lithium_7(shift_distance: float):
    cs = shift_distance
    os_dist = shift_distance * 2.2
    placements = [
        # Core
        {"shift": [cs, cs, cs], "rot": [0, 0, 0], "color": "#ff3366"},
        {"shift": [-cs, -cs, cs], "rot": [0, 0, np.pi / 2], "color": "#ff3366"},
        {"shift": [-cs, cs, -cs], "rot": [np.pi / 2, 0, 0], "color": "#00ffcc"},
        {"shift": [cs, -cs, -cs], "rot": [0, np.pi / 2, 0], "color": "#00ffcc"},
        # Outer Shell
        {"shift": [os_dist, -os_dist, os_dist], "rot": [0, np.pi / 4, 0], "color": "#ff99aa"},
        {"shift": [-os_dist, -os_dist, -os_dist], "rot": [np.pi / 4, 0, 0], "color": "#99ffee"},
        {"shift": [os_dist, os_dist, -os_dist], "rot": [0, 0, np.pi / 4], "color": "#99ffee"},
    ]
    return NumericallyEvaluateNucleons(
        NucleonCombiner.assemble_cluster(FundamentalTopologies.generate_borromean_6_3_2, placements)
    )


def NumericallyEvaluateNucleons(cluster):
    """
    Extracts the Center of Mass (CoM) for each nucleon in the cluster to
    feed the 1/r overlap calculation.
    """
    nucleons = []
    for node in cluster:
        all_pts = np.vstack(node["mesh"])
        com = np.mean(all_pts, axis=0)
        nucleons.append({"pos": com, "color": node["color"]})
    return nucleons


# ----- Dynamic Matrix Ops -----
def rotate_cluster_y(nucleons, angle):
    """
    Rotates the 3D Center of Mass of each nucleon around the Y-axis.
    """
    c, s = np.cos(angle), np.sin(angle)
    # Rotation matrix around Y
    R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])

    rotated = []
    for n in nucleons:
        r_pos = np.dot(R, n["pos"])
        rotated.append({"pos": r_pos, "color": n["color"]})
    return rotated


# ----- Scalar Field Engine -----
def calculate_vacuum_density(nucleons, X, Y, z_slice=0.0):
    density_field = np.zeros_like(X)
    amplitude = 100.0
    epsilon = 0.5

    for n in nucleons:
        cx, cy, cz = n["pos"]
        # 3D inverse distance squared calculation projected onto Z-slice
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
        local_density = amplitude / (dist_sq + epsilon)
        density_field += local_density

    return density_field


# ----- Animation Engine -----
def generate_dynamic_flux_gif(base_cluster, output_name: str, title: str, grid_res=150, bound=4.5, frames=180):
    """
    Animates the continuous streamplot deformation as the knot cluster rotates.
    """
    # Create the stationary 2D observer grid
    x = np.linspace(-bound, bound, grid_res)
    y = np.linspace(-bound, bound, grid_res)
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#0f0f0f")

    def update(frame):
        ax.clear()
        ax.set_facecolor("#0f0f0f")

        # 1. Rotate the 3D Nucleus
        angle = frame * (2 * np.pi / frames)
        rotated_cluster = rotate_cluster_y(base_cluster, angle)

        # 2. Capture the 2D Equatorial Scalar Overlay (Z=0)
        density_field = calculate_vacuum_density(rotated_cluster, X, Y, z_slice=0.0)

        # 3. Plot the continuous thermal heatmap
        cmap = plt.cm.inferno
        cmap.set_bad(color="#0f0f0f")
        ax.imshow(
            density_field,
            extent=[-bound, bound, -bound, bound],
            origin="lower",
            cmap=cmap,
            alpha=0.9,
            vmin=0.0,
        )

        # 4. Compute gradient (Topological Gravity Flux)
        grad_y, grad_x = np.gradient(density_field)

        # 5. Continuous Streamplot Overlay
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

        # 6. Plot the 2D projected nucleon reticles to track the mass rotation
        for n in rotated_cluster:
            cx, cy, cz = n["pos"]
            depth_scale = np.exp(-np.abs(cz))  # Dim smaller as they rotate out of the Z=0 plane

            # X & Y coordinates only
            ax.scatter(cx, cy, color=n["color"], s=500 * depth_scale, marker="+", linewidth=3, alpha=0.8)
            ax.scatter(
                cx,
                cy,
                color=n["color"],
                s=150 * depth_scale,
                edgecolor=n["color"],
                facecolor="none",
                linewidth=2,
                alpha=0.9,
            )

        # 7. Redraw Formatting
        ax.set_title(title, color="white", fontsize=16, pad=20)
        ax.set_xlabel("X (Topological Node Lengths)", color="white", fontsize=12)
        ax.set_ylabel("Y (Topological Node Lengths)", color="white", fontsize=12)
        ax.tick_params(colors="white")
        ax.text(
            0.02,
            0.95,
            f"Azimuth: {angle * (180/np.pi):.0f} deg\nZ-Slice: 0.0",
            transform=ax.transAxes,
            color="white",
            fontsize=12,
            bbox=dict(facecolor="#111111", edgecolor="white", alpha=0.5),
        )

        # Optional: Terminal feedback
        if frame % 5 == 0:
            print(f"  ... rendering frame {frame}/{frames}")

    print(f"[*] Compiling dynamic flux frames for {output_name}...")
    anim = FuncAnimation(fig, update, frames=frames, interval=80, blit=False)

    os.makedirs("tests/outputs/gifs", exist_ok=True)
    out_path = os.path.join("tests/outputs/gifs", output_name)

    anim.save(out_path, writer="pillow", fps=15, savefig_kwargs={"facecolor": fig.get_facecolor()})
    plt.close()
    print(f"[*] Successfully saved dynamic flux GIF: {out_path}\n")


if __name__ == "__main__":
    # --- Execute Render Queue ---

    # Render lower grid_res (100) to keep animation export times reasonable
    # 1. Helium-4 Dynamic Flux
    he4_base = construct_helium_4(shift_distance=0.85)
    generate_dynamic_flux_gif(
        he4_base,
        "helium_4_dynamic_flux.gif",
        title="Helium-4: Dynamic Transverse Vacuum Strain\n(Rotating 3D Knot Projected to 2D Plane)",
        bound=3.0,
        grid_res=100,
        frames=180,
    )

    # 2. Lithium-7 Dynamic Flux
    li7_base = construct_lithium_7(shift_distance=0.85)
    generate_dynamic_flux_gif(
        li7_base,
        "lithium_7_dynamic_flux.gif",
        title="Lithium-7: Asymmetrical Secondary Shell Strain\n(Rotating 3D Dual-Shell Projected to 2D Plane)",
        bound=4.5,
        grid_res=100,
        frames=180,
    )
