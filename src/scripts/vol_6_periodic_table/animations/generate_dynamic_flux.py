import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pathlib

# Ensure the core framework is in PATH
project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

output_dir = os.path.join(project_root, "periodic_table", "figures")
os.makedirs(output_dir, exist_ok=True)


def rotate_cluster_y(nodes, angle):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    return [np.dot(R, n) for n in nodes]


def calculate_vacuum_density(nodes, X, Y, z_slice=0.0):
    density_field = np.zeros_like(X)
    amplitude, epsilon = 100.0, 0.5
    for cx, cy, cz in nodes:
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
        density_field += amplitude / (dist_sq + epsilon)
    return density_field


def get_tetrahedron(center, scale=1.0):
    # 4 nucleons in an alpha particle
    t = 1.0 / np.sqrt(2.0)
    pts = [np.array([1, 0, -t]), np.array([-1, 0, -t]), np.array([0, 1, t]), np.array([0, -1, t])]
    return [p * scale + center for p in pts]


def animate_beryllium_8_decay():
    print("[*] Generating Beryllium-8 Alpha Decay Transient Animation...")
    bound, grid_res, frames = 15.0, 80, 60
    x = np.linspace(-bound, bound, grid_res)
    y = np.linspace(-bound, bound, grid_res)
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#0f0f0f")

    def update(frame):
        ax.clear()
        ax.set_facecolor("#0f0f0f")

        # Calculate transient separation radius
        # Frames 0-25: Strained phase-lock
        # Frames 25-60: Dielectric Rupture (Exponential Separation)
        if frame < 25:
            R = 3.0
        else:
            R = 3.0 + ((frame - 25) ** 2) * 0.02

        alpha1 = get_tetrahedron(np.array([-R, 0, 0]), scale=0.8)
        alpha2 = get_tetrahedron(np.array([R, 0, 0]), scale=0.8)
        nodes = alpha1 + alpha2

        # Rotate entire system slowly
        angle = frame * (2 * np.pi / frames)
        rotated_nodes = rotate_cluster_y(nodes, angle)

        density = calculate_vacuum_density(rotated_nodes, X, Y)
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

        for cx, cy, cz in rotated_nodes:
            depth_scale = np.exp(-np.abs(cz / (bound / 3.0)))
            ax.scatter(cx, cy, color="#00ffcc", s=300 * depth_scale, marker="+", linewidth=2, alpha=0.8)
            ax.scatter(
                cx,
                cy,
                color="#00ffcc",
                s=100 * depth_scale,
                edgecolor="#00ffcc",
                facecolor="none",
                linewidth=1.5,
                alpha=0.9,
            )

        status = "Phase-Locked (Strained)" if frame < 25 else "M_ij DIELECTRIC RUPTURE"
        color = "white" if frame < 25 else "red"
        ax.set_title(
            f"Beryllium-8 ($^8Be \\rightarrow 2\\alpha$) Transient Decay\\nStatus: {status}",
            color=color,
            fontsize=16,
            pad=20,
        )
        ax.tick_params(colors="white")

    anim = FuncAnimation(fig, update, frames=frames, interval=80, blit=False)
    anim.save(
        os.path.join(output_dir, "be8_decay_transient.gif"),
        writer="pillow",
        fps=15,
        savefig_kwargs={"facecolor": fig.get_facecolor()},
    )
    print("[*] Beryllium-8 Decay Animation Complete.")


def animate_tritium_decay():
    print("[*] Generating Tritium Beta- Decay Transient Animation...")
    bound, grid_res, frames = 8.0, 80, 60
    x = np.linspace(-bound, bound, grid_res)
    y = np.linspace(-bound, bound, grid_res)
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#0f0f0f")

    def update(frame):
        ax.clear()
        ax.set_facecolor("#0f0f0f")

        # Tritium is 3 nucleons.
        # Frames 0-25: Asymmetric tight cluster
        # Frames 25-60: Beta ejection and relaxation to equilateral He-3

        if frame < 25:
            # Strained asymmetric state
            n1 = np.array([0, 1.2, 0])
            n2 = np.array([-1.0, -0.8, 0])
            n3 = np.array([1.5, -0.8, 0])  # Bulging unstable neutron
            e_pos = None
        else:
            # Relaxing to He-3 equilateral
            progress = min(1.0, (frame - 25) / 20.0)
            n1 = np.array([0, 1.2, 0])
            n2 = np.array([-1.0, -0.8, 0])
            # Neutron 3 moves into symmetric position
            target_n3 = np.array([1.0, -0.8, 0])
            start_n3 = np.array([1.5, -0.8, 0])
            n3 = start_n3 + (target_n3 - start_n3) * progress

            # Ejected electron flies away from N3
            e_velocity = np.array([0.4, 0.2, 0])
            e_pos = start_n3 + e_velocity * (frame - 25)

        nodes = [n1, n2, n3]

        # Rotate
        angle = frame * (2 * np.pi / frames)
        rotated_nodes = rotate_cluster_y(nodes, angle)

        density = calculate_vacuum_density(rotated_nodes, X, Y)
        # Add electron density if ejected
        if e_pos is not None:
            rotated_e = np.dot(
                np.array(
                    [
                        [np.cos(angle), 0, np.sin(angle)],
                        [0, 1, 0],
                        [-np.sin(angle), 0, np.cos(angle)],
                    ]
                ),
                e_pos,
            )
            dist_sq = (X - rotated_e[0]) ** 2 + (Y - rotated_e[1]) ** 2 + (0 - rotated_e[2]) ** 2
            density += 20.0 / (dist_sq + 0.1)  # small sharp spike

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

        # Draw Nucleons
        for cx, cy, cz in rotated_nodes:
            depth_scale = np.exp(-np.abs(cz / (bound / 3.0)))
            ax.scatter(cx, cy, color="#00ffcc", s=300 * depth_scale, marker="+", linewidth=2, alpha=0.8)
            ax.scatter(
                cx,
                cy,
                color="#00ffcc",
                s=100 * depth_scale,
                edgecolor="#00ffcc",
                facecolor="none",
                linewidth=1.5,
                alpha=0.9,
            )

        target_color = "white"
        status = "Asymmetric Target"

        if e_pos is not None:
            depth_scale = np.exp(-np.abs(rotated_e[2] / (bound / 3.0)))
            ax.scatter(
                rotated_e[0],
                rotated_e[1],
                color="yellow",
                s=150 * depth_scale,
                marker="o",
                alpha=1.0,
            )
            target_color = "yellow"
            status = "BETA EMISSION (Relaxing to $^3He$)"

        ax.set_title(
            f"Tritium ($^3H \\rightarrow ^3He + e^-$) Transient Decay\\nStatus: {status}",
            color=target_color,
            fontsize=16,
            pad=20,
        )
        ax.tick_params(colors="white")

    anim = FuncAnimation(fig, update, frames=frames, interval=80, blit=False)
    anim.save(
        os.path.join(output_dir, "h3_decay_transient.gif"),
        writer="pillow",
        fps=15,
        savefig_kwargs={"facecolor": fig.get_facecolor()},
    )
    print("[*] Tritium Decay Animation Complete.")


if __name__ == "__main__":
    animate_beryllium_8_decay()
    animate_tritium_decay()
