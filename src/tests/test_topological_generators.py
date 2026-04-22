"""
Test Script: Visualizing Fundamental Topological Generators.
Uses the `src/ave/topological/borromean.py` engine to extract
and plot the 3D coordinate meshes of the Unknot and Borromean knots.
"""

import os

import matplotlib.pyplot as plt

from ave.topological.borromean import FundamentalTopologies


def plot_unknot():
    coords = FundamentalTopologies.generate_unknot_0_1(radius=1.0)

    fig = plt.figure(figsize=(8, 8))
    fig.patch.set_facecolor("#0f0f0f")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#0f0f0f")

    # Plot the continuous knot curve
    ax.plot(
        coords[:, 0],
        coords[:, 1],
        coords[:, 2],
        color="#00ffcc",
        linewidth=4,
        alpha=0.9,
        label=r"$0_1$ Unknot (Electron)",
    )

    ax.set_title("Fundamental Lepton Topology", color="white", fontsize=14)
    ax.legend(facecolor="#111111", edgecolor="#333333", labelcolor="white")

    # Clean up axes
    _clean_axes(ax)

    os.makedirs("tests/outputs", exist_ok=True)
    plt.savefig("tests/outputs/unknot_0_1_validation.png", dpi=300, facecolor=fig.get_facecolor())
    plt.close()
    print("[*] Saved Unknot Validation Plot.")


def plot_borromean():
    rings = FundamentalTopologies.generate_borromean_6_3_2(radius=1.0)

    fig = plt.figure(figsize=(8, 8))
    fig.patch.set_facecolor("#0f0f0f")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#0f0f0f")

    colors = ["#ff3366", "#33ccff", "#ffcc00"]

    for i, ring_coords in enumerate(rings):
        ax.plot(
            ring_coords[:, 0],
            ring_coords[:, 1],
            ring_coords[:, 2],
            color=colors[i],
            linewidth=4,
            alpha=0.8,
            label=f"Loop {i+1}",
        )

    ax.set_title(r"Fundamental Baryon Topology ($6^3_2$ Borromean Link)", color="white", fontsize=14)
    ax.legend(facecolor="#111111", edgecolor="#333333", labelcolor="white")

    # Clean up axes
    _clean_axes(ax)

    os.makedirs("tests/outputs", exist_ok=True)
    plt.savefig("tests/outputs/borromean_6_3_2_validation.png", dpi=300, facecolor=fig.get_facecolor())
    plt.close()
    print("[*] Saved Borromean Validation Plot.")


def _clean_axes(ax):
    """Helper to enforce dark-mode aesthetic boundaries"""
    ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.grid(False)
    ax.axis("off")

    # Enforce cubic bounds to prevent aspect stretching
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])


if __name__ == "__main__":
    plot_unknot()
    plot_borromean()
