import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Ensure the core framework is in PATH
project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

output_dir = os.path.join(project_root, "periodic_table", "figures")
os.makedirs(output_dir, exist_ok=True)


def calculate_vacuum_density(nodes, X, Y, z_slice=0.0):
    density_field = np.zeros_like(X)
    amplitude, epsilon = 100.0, 0.5
    for cx, cy, cz in nodes:
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
        density_field += amplitude / (dist_sq + epsilon)
    return density_field


def animate_dt_fusion_transient():
    print("[*] Generating D-T Fusion FDTD Macro-Merger Animation...")
    bound, grid_res, frames = 8.0, 80, 80
    x = np.linspace(-bound, bound, grid_res)
    y = np.linspace(-bound, bound, grid_res)
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#0f0f0f")

    # Target stable He-4 nodes (equilateral tetrahedron cross-section)
    he4_target = [
        np.array([-0.7, 0.7, 0.0]),
        np.array([0.7, 0.7, 0.0]),
        np.array([-0.7, -0.7, 0.0]),
        np.array([0.7, -0.7, 0.0]),
    ]

    def update(frame):
        ax.clear()
        ax.set_facecolor("#0f0f0f")

        # Collision phases:
        # 0 - 30: Inbound acceleration (D and T array closing)
        # 30 - 45: The He-5 unstable intermediate squeeze ($V_{yield}$ saturation)
        # 45 - 80: The relaxation: snapping into He-4 Phase-Lock, and Neutron ejection

        nodes = []
        ejected_n = None
        status = ""
        color = "white"

        if frame < 30:
            # 1. Approach
            progress = frame / 30.0

            # Tritium (Right side, moving left slightly)
            tx = 3.0 - (1.5 * progress)
            t_nodes = [
                np.array([tx, 1.0, 0]),
                np.array([tx - 0.866, -0.5, 0]),
                np.array([tx + 0.866, -0.5, 0]),
            ]

            # Deuterium (Left side, moving right fast)
            dx = -5.0 + (3.5 * progress)
            d_nodes = [np.array([dx, 0.75, 0]), np.array([dx, -0.75, 0])]

            nodes = t_nodes + d_nodes
            status = f"Inbound AC Ponderomotive Forcing"
            color = "white"

        elif frame < 45:
            # 2. He-5 Squeeze (Dielectric Tension)
            progress = (frame - 30) / 15.0

            # They converge into a highly strained 5-node cluster at center
            # Nodes jitter and compress
            nodes = [
                np.array([0 + np.random.uniform(-0.1, 0.1), 1.0 + np.random.uniform(-0.1, 0.1), 0]),
                np.array([-0.5 + np.random.uniform(-0.1, 0.1), -0.5 + np.random.uniform(-0.1, 0.1), 0]),
                np.array([0.5 + np.random.uniform(-0.1, 0.1), -0.5 + np.random.uniform(-0.1, 0.1), 0]),
                np.array([-0.8 + np.random.uniform(-0.1, 0.1), 0.5 + np.random.uniform(-0.1, 0.1), 0]),
                np.array(
                    [1.0 + np.random.uniform(-0.1, 0.1), 0.2 + np.random.uniform(-0.1, 0.1), 0]
                ),  # The parasitic neutron
            ]
            status = "Unstable $^5He$ Intermediate ($V_{yield}$ Tension!)"
            color = "red"

        else:
            # 3. Relaxation and Ejection
            progress = min(1.0, (frame - 45) / 15.0)

            # First 4 nodes map to He4 Target smoothly
            start_nodes = [
                np.array([0, 1.0, 0]),
                np.array([-0.5, -0.5, 0]),
                np.array([0.5, -0.5, 0]),
                np.array([-0.8, 0.5, 0]),
            ]
            for i in range(4):
                n_pos = start_nodes[i] + (he4_target[i] - start_nodes[i]) * progress
                nodes.append(n_pos)

            # The 5th node (Neutron) is violently ejected to the right
            e_velocity = np.array([0.5, 0.1, 0])
            ejected_n = np.array([1.0, 0.2, 0]) + e_velocity * (frame - 45)

            status = "Phase-Lock ($^4He$ + Ejected Neutron)"
            color = "#00ffcc"

        # Calculate density
        density = calculate_vacuum_density(nodes, X, Y)
        if ejected_n is not None:
            dist_sq = (X - ejected_n[0]) ** 2 + (Y - ejected_n[1]) ** 2 + (0 - ejected_n[2]) ** 2
            density += 50.0 / (dist_sq + 0.1)  # sharp pulse for the flying neutron

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

        # Plot markers
        for n in nodes:
            ax.scatter(n[0], n[1], color="#00ffcc", s=300, marker="+", linewidth=2, alpha=0.8)
            ax.scatter(
                n[0],
                n[1],
                color="#00ffcc",
                s=100,
                edgecolor="#00ffcc",
                facecolor="none",
                linewidth=1.5,
                alpha=0.9,
            )

        if ejected_n is not None:
            ax.scatter(ejected_n[0], ejected_n[1], color="#00ffcc", s=150, marker="o", alpha=1.0)

        ax.set_title(f"D-T Fusion Topological Merger\\nStatus: {status}", color=color, fontsize=16, pad=20)
        ax.tick_params(colors="white")

    anim = FuncAnimation(fig, update, frames=frames, interval=80, blit=False)
    anim.save(
        os.path.join(output_dir, "dt_fusion_transient.gif"),
        writer="pillow",
        fps=15,
        savefig_kwargs={"facecolor": fig.get_facecolor()},
    )
    print("[*] D-T Fusion Animation Complete.")


if __name__ == "__main__":
    animate_dt_fusion_transient()
