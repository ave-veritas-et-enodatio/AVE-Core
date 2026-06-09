# simulate_3d_lattice.py
#
# ⚠ SUPERSEDED FRAMING (legacy z=3 visualization, retained for reference).
# This driver renders the degree-3 chiral SRS / "Laves K4" net (it wires exactly
# 3 nearest neighbors per node, below). Per the 2026-06-07 lattice-net
# resolution-of-record (_orchestration/2026-06-07_lattice-net-resolution.md), the
# canonical substrate is the degree-4 ACHIRAL diamond net (Fd-3m) that the engine
# actually computes on (src/ave/.../k4_tlm.py); chirality is an EXCITED Cosserat
# order-parameter (k_chi), not a cold-lattice property. The z=3 srs framing here
# is the numerological outlier. A canonical rebuild on the diamond net (4 nearest
# neighbors) is queued as follow-up.
#
# Simulates the fundamental topological substrate of the Trace-Reversed
# Chiral LC Network. We rigidly use the mathematical SRS net (Laves K4 crystal),
# which is the definitive algebraically continuous, 3D isotropic, highly-symmetric
# chiral graph manifold.

import matplotlib.pyplot as plt
import numpy as np

from ave_path_util import sim_output

plt.style.use("dark_background")


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

    fig = plt.figure(figsize=(12, 12), facecolor="#050510")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#050510")

    # View Angle emphasizing the geometric helical channels built into the K4 lattice
    ax.view_init(elev=22, azim=60)

    # Generate nodes
    grid_size = 4
    all_nodes = generate_k4_chiral_lattice(grid_size=grid_size)

    # Render discrete coordinate nodes (points)
    ax.scatter(
        all_nodes[:, 0],
        all_nodes[:, 1],
        all_nodes[:, 2],
        color="#00ffff",
        s=50,
        alpha=0.9,
        edgecolors="white",
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
                    color="#ff00aa",
                    linewidth=2.0,
                    alpha=0.7,
                    zorder=1,
                )
                edges_plotted += 1

    print(f"Rendered {len(all_nodes)} Discrete Nodes and {edges_plotted} Chiral Tensor Linkages.")

    ax.set_title(
        r"Topological LC Chiral Network: Coordinate Graph Manifold",
        color="white",
        fontsize=18,
        pad=20,
        weight="bold",
    )
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
            color="#00ffff",
            marker="o",
            linestyle="None",
            markersize=9,
            label=r"Discrete Coordinate Node",
        ),
        Line2D(
            [0],
            [0],
            color="#ff00aa",
            lw=2.5,
            alpha=0.8,
            label=r"LC Differential Tensor Line (Flux Junction)",
        ),
    ]
    ax.legend(
        handles=custom_lines,
        loc="lower left",
        facecolor="black",
        edgecolor="white",
        labelcolor="white",
        fontsize=12,
    )

    output_path = sim_output("lattice_structure_3d.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight")
    print(f"Saved pure mathematical chiral graph simulation to: {output_path}")


if __name__ == "__main__":
    plot_chiral_lattice_manifold()
