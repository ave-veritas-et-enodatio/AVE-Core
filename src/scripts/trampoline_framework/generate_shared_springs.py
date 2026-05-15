"""
Generate Figure 6 for trampoline-framework.md: shared springs and gravity projection.

3-panel diagram showing:
  Panel A — One A-node + its 4 primary K4 bonds (each shared with one B-cell)
  Panel B — Two A-nodes coupled through a shared B-neighbor (1.187·d effective distance)
  Panel C — Mass at A₀ creates strain field propagating outward through shared bonds (1/r gravity)

Run from repo root:
  uv run --no-sync python src/scripts/trampoline_framework/generate_shared_springs.py
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "legend.fontsize": 9,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)

OUTDIR = Path("assets/sim_outputs/trampoline_framework")
OUTDIR.mkdir(parents=True, exist_ok=True)


def panel_a(ax):
    """One cell = one node + 4 primary bonds (each shared with one neighbor)."""
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    # Focal A-node
    ax.scatter(0, 0, s=400, c="#1f77b4", marker="o", edgecolors="black", linewidth=1.5, zorder=10)
    ax.text(0, 0, "A", color="white", fontsize=12, fontweight="bold", ha="center", va="center", zorder=11)

    # 4 B-neighbors in tetrahedral projection (project 3D → 2D)
    # 109.47° tetrahedron projected onto plane
    b_angles = [0, 2 * np.pi / 3, 4 * np.pi / 3]  # 3 in plane
    b_positions = [(np.cos(a) * 1.1, np.sin(a) * 1.1) for a in b_angles]
    b_positions.append((0, -1.3))  # 4th out of plane (drawn below for visibility)

    for i, (bx, by) in enumerate(b_positions):
        # Bond from focal A to this B
        ax.plot([0, bx], [0, by], color="#666", linewidth=2.5, zorder=5)
        # B-node
        ax.scatter(bx, by, s=300, c="#ff7f0e", marker="o", edgecolors="black", linewidth=1.5, zorder=10)
        ax.text(bx, by, "B", color="white", fontsize=10, fontweight="bold", ha="center", va="center", zorder=11)

    # Annotate that each bond is shared
    ax.annotate(
        "← each bond shared\n   with this neighbor's cell",
        xy=(b_positions[0][0] * 0.5, b_positions[0][1] * 0.5),
        xytext=(1.1, 1.15),
        fontsize=8.5,
        ha="center",
        arrowprops=dict(arrowstyle="->", color="#555", lw=1.0),
    )

    # Shade the "cell" lightly
    ax.fill([0, b_positions[0][0], b_positions[1][0], b_positions[2][0], b_positions[3][0]],
            [0, b_positions[0][1], b_positions[1][1], b_positions[2][1], b_positions[3][1]],
            color="#1f77b4", alpha=0.06, zorder=1)

    ax.set_title(
        "(A) One cell = one node + 4 primary bonds\n"
        "Each bond also belongs to the B-neighbor's cell",
        fontsize=11,
        pad=10,
    )


def panel_b(ax):
    """Two A-nodes coupled through a shared B-node at distance 1.187·d."""
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    # Two A-nodes
    a1_pos = (-1.5, 0)
    a2_pos = (1.5, 0)
    b_shared = (0, 1.0)

    # Primary bonds A1-B and B-A2 (solid, thick)
    ax.plot([a1_pos[0], b_shared[0]], [a1_pos[1], b_shared[1]], color="#666", linewidth=3.0, zorder=5)
    ax.plot([b_shared[0], a2_pos[0]], [b_shared[1], a2_pos[1]], color="#666", linewidth=3.0, zorder=5)

    # Label primary bond distances
    midL = ((a1_pos[0] + b_shared[0]) / 2, (a1_pos[1] + b_shared[1]) / 2)
    midR = ((a2_pos[0] + b_shared[0]) / 2, (a2_pos[1] + b_shared[1]) / 2)
    ax.text(midL[0] - 0.4, midL[1] + 0.1, "$d$", fontsize=12, color="#444")
    ax.text(midR[0] + 0.25, midR[1] + 0.1, "$d$", fontsize=12, color="#444")

    # Effective coupling A1-A2 (dashed, through B)
    # Show as curved dashed line going UP through B
    theta = np.linspace(np.pi, 0, 50)
    arc_x = b_shared[0] + 1.5 * np.cos(theta)
    arc_y = b_shared[1] + 0.3 * np.sin(theta) + 0.0
    # Better: simple dashed straight line A1-A2 with annotation
    ax.plot([a1_pos[0], a2_pos[0]], [a1_pos[1], a2_pos[1]], color="#d62728", linewidth=2.0, linestyle="--", alpha=0.7, zorder=4)

    # Distance annotation for A1-A2
    ax.text(
        0,
        -0.30,
        r"effective coupling distance $\approx 1.187\,d$"
        "\n(geometric A₁→B→A₂ path)",
        ha="center",
        fontsize=10,
        color="#d62728",
        fontweight="bold",
    )

    # Nodes
    ax.scatter(*a1_pos, s=400, c="#1f77b4", marker="o", edgecolors="black", linewidth=1.5, zorder=10)
    ax.text(*a1_pos, "A₁", color="white", fontsize=12, fontweight="bold", ha="center", va="center", zorder=11)
    ax.scatter(*a2_pos, s=400, c="#1f77b4", marker="o", edgecolors="black", linewidth=1.5, zorder=10)
    ax.text(*a2_pos, "A₂", color="white", fontsize=12, fontweight="bold", ha="center", va="center", zorder=11)
    ax.scatter(*b_shared, s=400, c="#ff7f0e", marker="o", edgecolors="black", linewidth=1.5, zorder=10)
    ax.text(*b_shared, "B", color="white", fontsize=12, fontweight="bold", ha="center", va="center", zorder=11)

    # Microrotation symbol at B
    ax.annotate(
        r"shared $\omega_B$" "\n(microrotation field\ncouples A₁ to A₂)",
        xy=(b_shared[0] + 0.18, b_shared[1] + 0.15),
        xytext=(0.55, 1.30),
        fontsize=9,
        color="#2ca02c",
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="#2ca02c"),
    )

    # Curved arrow showing rotation
    arc = Arc(b_shared, 0.5, 0.5, angle=0, theta1=30, theta2=300, color="#2ca02c", linewidth=2)
    ax.add_patch(arc)

    ax.set_title(
        "(B) Two A-nodes share a B-neighbor → coupled through $\\omega_B$\n"
        "No separate \"secondary spring\" — shared-B-node IS the coupling",
        fontsize=11,
        pad=10,
    )


def panel_c(ax):
    """Mass at A₀ → strain propagates outward through shared bonds → gravity."""
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    # Generate a hexagonal-like lattice of nodes (simplified K4 projection)
    rng = np.random.default_rng(7)
    grid_radius = 2.3
    nodes_a = []
    nodes_b = []
    for ring in range(1, 5):
        n_in_ring = 6 * ring
        for j in range(n_in_ring):
            angle = 2 * np.pi * j / n_in_ring
            r = ring * 0.55
            x = r * np.cos(angle) + rng.uniform(-0.04, 0.04)
            y = r * np.sin(angle) + rng.uniform(-0.04, 0.04)
            if x**2 + y**2 < grid_radius**2:
                if ring % 2 == 0:
                    nodes_a.append((x, y))
                else:
                    nodes_b.append((x, y))

    nodes_a_arr = np.array(nodes_a)
    nodes_b_arr = np.array(nodes_b)

    # Draw bonds between nearby A and B nodes
    for a in nodes_a_arr:
        for b in nodes_b_arr:
            d = np.linalg.norm(a - b)
            if d < 0.75:
                ax.plot([a[0], b[0]], [a[1], b[1]], color="#bbb", linewidth=0.6, alpha=0.7, zorder=1)

    # Plot nodes (smaller)
    ax.scatter(nodes_a_arr[:, 0], nodes_a_arr[:, 1], s=35, c="#1f77b4", alpha=0.7, zorder=2)
    ax.scatter(nodes_b_arr[:, 0], nodes_b_arr[:, 1], s=35, c="#ff7f0e", alpha=0.7, zorder=2)

    # Mass at center (A₀ — focal mass source)
    ax.scatter(0, 0, s=500, c="black", marker="o", edgecolors="darkred", linewidth=2.0, zorder=10)
    ax.text(0, 0, "M", color="white", fontsize=13, fontweight="bold", ha="center", va="center", zorder=11)

    # Concentric strain contours (1/r decay visualization)
    for r in [0.55, 1.05, 1.55, 2.05]:
        theta = np.linspace(0, 2 * np.pi, 100)
        intensity = 1.0 / r
        ax.plot(
            r * np.cos(theta),
            r * np.sin(theta),
            color="darkred",
            linewidth=2.0 * intensity,
            alpha=0.4 + 0.6 * intensity / 2,
            zorder=3,
        )

    # Outward-radiating arrows (strain propagation through shared bonds)
    for angle in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        x0 = 0.35 * np.cos(angle)
        y0 = 0.35 * np.sin(angle)
        x1 = 1.0 * np.cos(angle)
        y1 = 1.0 * np.sin(angle)
        ax.annotate(
            "",
            xy=(x1, y1),
            xytext=(x0, y0),
            arrowprops=dict(arrowstyle="->", color="darkred", lw=1.5, alpha=0.7),
        )

    # Annotation
    ax.text(
        0,
        -2.30,
        r"strain field $u(r) \propto 1/r$"
        "\n(continuum limit = $n(r) = 1 + 2GM/c^2 r$)"
        "\nGravity propagates via shared K4 bonds",
        ha="center",
        fontsize=9.5,
        color="darkred",
        fontweight="bold",
    )

    ax.set_title(
        "(C) Localized mass M → strain field propagating outward through shared springs\n"
        "Each shared K4 bond transmits force + torque to neighbor cells → macroscopic gravity",
        fontsize=11,
        pad=10,
    )


if __name__ == "__main__":
    fig, axes = plt.subplots(1, 3, figsize=(20, 7))
    panel_a(axes[0])
    panel_b(axes[1])
    panel_c(axes[2])

    fig.suptitle(
        "Shared springs and gravity projection — the K4 substrate's inter-cell coupling mechanism",
        fontsize=14,
        fontweight="bold",
        y=1.02,
    )

    plt.tight_layout()
    output_path = OUTDIR / "06_shared_springs_gravity.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"✓ {output_path}")
