# simulate_3d_lattice.py
# Simulates the fundamental topological substrate of the Trace-Reversed
# Chiral LC Network. We rigidly use the mathematical SRS net (Laves K4 crystal),
# which is the definitive algebraically continuous, 3D isotropic, highly-symmetric
# chiral graph manifold.

import matplotlib.pyplot as plt
import numpy as np

from ave.viz import style
from ave_path_util import sim_output

style.apply("print")  # white-background print profile (house style)


def generate_k4_chiral_lattice(grid_size: int = 2) -> np.ndarray:
    """
    Algebraically constructs the exact SRS (Laves K4) 3D Chiral Isotropic Graph.
    Uses the precise Wyckoff 8a coordinate positions mapped to a cubic unit cell.
    """
    # Base fractional coordinates of the 8 nodes in the chiral unit cell (Space Group I4_1 32)
    srs_basis = (
        np.array(
            [
                [1, 1, 1],
                [5, 3, 7],
                [7, 5, 3],
                [3, 7, 5],
                [7, 7, 7],
                [3, 5, 1],
                [1, 3, 5],
                [5, 1, 3],
            ],
            dtype=float,
        )
        / 8.0
    )

    nodes = []
    # Tile the unit cell to form the macroscopic continuous chiral manifold
    for i in range(grid_size):
        for j in range(grid_size):
            for k in range(grid_size):
                offset = np.array([i, j, k], dtype=float)
                for pt in srs_basis:
                    nodes.append(pt + offset)

    return np.array(nodes)


def plot_chiral_lattice_manifold() -> None:
    print("Evaluating Continuous Spatial Manifold as a Discrete Chiral Graph (SRS Net)...")

    fig = plt.figure(figsize=style.figsize("square"))
    ax = fig.add_subplot(111, projection="3d")
    # 3D panes are not fully governed by rcParams — set them explicitly so the
    # print-profile white background is honoured on every face (gotcha 5).
    ax.set_facecolor("white")
    for pane in (ax.xaxis, ax.yaxis, ax.zaxis):
        pane.set_pane_color((1.0, 1.0, 1.0, 1.0))

    # View Angle emphasizing the geometric helical channels built into the K4 lattice
    ax.view_init(elev=22, azim=60)

    # Generate nodes. A 3x3x3 tiling is the smallest sub-manifold in which the
    # SRS chiral helical channels and the exact 3-coordination of every node
    # remain visually legible — at the prior 4x4x4 the nodes overplotted into an
    # opaque blob and the K4 topology (the point of the figure) was lost. This is
    # a presentation/readability choice; the lattice construction is unchanged.
    grid_size = 3
    all_nodes = generate_k4_chiral_lattice(grid_size=grid_size)

    # Render discrete coordinate nodes (points)
    ax.scatter(
        all_nodes[:, 0],
        all_nodes[:, 1],
        all_nodes[:, 2],
        color=style.COLORS["ave"],
        s=22,
        alpha=0.95,
        edgecolors=style.COLORS["data"],
        linewidths=0.4,
        zorder=5,
    )

    # Mathematical linkage logic (Nearest neighbors in K4)
    # Every node in the continuous chiral manifold connects exactly to 3 adjacent neighbors
    diff = all_nodes[:, np.newaxis, :] - all_nodes[np.newaxis, :, :]
    dist_mat = np.sqrt(np.sum(diff**2, axis=-1))

    edges_plotted = 0
    # Add exactly 3 nearest neighbors for every node
    for i in range(len(all_nodes)):
        # Get indices of the 3 closest nodes (excluding itself at index 0)
        closest_indices = np.argsort(dist_mat[i])[1:4]
        for j in closest_indices:
            # Only plot each edge once to avoid drawing double-lines
            if i < j:
                p1 = all_nodes[i]
                p2 = all_nodes[j]
                # Render the topological tensor connection (lines)
                ax.plot(
                    [p1[0], p2[0]],
                    [p1[1], p2[1]],
                    [p1[2], p2[2]],
                    color=style.COLORS["comparison"],
                    linewidth=1.6,
                    alpha=0.7,
                    zorder=1,
                )
                edges_plotted += 1

    print(f"Rendered {len(all_nodes)} Discrete Nodes and {edges_plotted} Chiral Tensor Linkages.")

    # No baked title — the caption lives in the LaTeX \caption{} (house style).
    ax.set_axis_off()

    ax.set_box_aspect([1, 1, 1])

    # Bound Scaling tightly to avoid edge artifacts
    ax.set_xlim(0, float(grid_size))
    ax.set_ylim(0, float(grid_size))
    ax.set_zlim(0, float(grid_size))

    # Mathematical Legend (No visual spring representations)
    from matplotlib.lines import Line2D

    custom_lines = [
        Line2D(
            [0],
            [0],
            color=style.COLORS["ave"],
            marker="o",
            linestyle="None",
            markersize=8,
            label=r"Discrete Coordinate Node",
        ),
        Line2D(
            [0],
            [0],
            color=style.COLORS["comparison"],
            lw=2.0,
            alpha=0.85,
            label=r"LC Differential Tensor Line (Flux Junction)",
        ),
    ]
    # Legend placed outside the 3D data box (house style; "right" suits a single
    # panel). bbox_inches="tight" in style.save captures it.
    style.legend(ax, handles=custom_lines, where="right")

    output_path = sim_output("lattice_structure_3d.png")
    style.save(fig, output_path)
    print(f"Saved chiral graph manifold (schematic) to: {output_path}")


if __name__ == "__main__":
    plot_chiral_lattice_manifold()
