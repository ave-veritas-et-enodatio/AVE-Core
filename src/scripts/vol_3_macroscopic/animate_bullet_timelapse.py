"""
30-Second Bullet Cluster Timelapse.
Computes a high-fidelity continuous cinematic animation mapping 
the Linear Superposition offset physics of Macroscopic Lensing haloss.
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

# Ensure local ave package is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from ave.core.constants import M_SUN, G
from ave.regime_3_saturated.galactic_rotation import ave_saturation_acceleration, A0_LATTICE


def animate_bullet_cluster():
    KPC = 3.086e19  # m
    GRID_MIN, GRID_MAX, GRID_RES = -1500 * KPC, 1500 * KPC, 120
    x = np.linspace(GRID_MIN, GRID_MAX, GRID_RES)
    y = np.linspace(GRID_MIN, GRID_MAX, GRID_RES)
    X_si, Y_si = np.meshgrid(x, y)
    X_kpc = X_si / KPC
    Y_kpc = Y_si / KPC

    mass_main = 1e14 * M_SUN
    mass_bullet = 1e13 * M_SUN

    # Animation Setup
    FRAMES = 300
    FPS = 10

    # Pre-calculate boundary paths for the collision logic
    start_main = -1200 * KPC
    end_main = 300 * KPC
    start_bullet = 1200 * KPC
    end_bullet = -900 * KPC

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    # Persistent axis tracking text
    # title_text = ax.text(  # bulk lint fixup pass
    #     0.5,
    #     1.05,
    #     "",
    #     transform=ax.transAxes,
    #     color="white",
    #     fontsize=14,
    #     ha="center",
    #     fontweight="bold",
    # )
    # phase_text = ax.text(0.5, 0.95, "", transform=ax.transAxes, color="cyan", fontsize=12, ha="center")  # bulk lint fixup pass

    print(f"Executing 30s High-Fidelity Physics Render ({FRAMES} Frames)...")
    writer = PillowWriter(fps=FPS)
    output_path = os.path.join(os.path.dirname(__file__), "../../../assets/sim_outputs/bullet_timelapse.gif")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with writer.saving(fig, output_path, dpi=120):
        for i in range(FRAMES):
            ratio = i / float(FRAMES - 1)  # 0 to 1

            # Kinematics
            pos_main_x = start_main + (end_main - start_main) * ratio
            pos_bullet_x = start_bullet + (end_bullet - start_bullet) * ratio

            if np.abs(pos_main_x - pos_bullet_x) < 200 * KPC:
                baryon_state = "Kinematic Friction (Baryonic Core Stalling)"
            else:
                baryon_state = "Constant Velocity"

            # Bare Mass Profiles
            r_main = np.sqrt((X_si - pos_main_x) ** 2 + Y_si**2)
            r_main = np.maximum(r_main, 25 * KPC)  # Core sink prevention
            g_N_main = G * mass_main / (r_main**2)

            r_bullet = np.sqrt((X_si - pos_bullet_x) ** 2 + Y_si**2)
            r_bullet = np.maximum(r_bullet, 25 * KPC)
            g_N_bullet = G * mass_bullet / (r_bullet**2)

            # Saturation Topo-Expansion Profiles
            g_eff_main = np.vectorize(lambda g: ave_saturation_acceleration(g, a0=A0_LATTICE))(g_N_main)
            g_eff_bullet = np.vectorize(lambda g: ave_saturation_acceleration(g, a0=A0_LATTICE))(g_N_bullet)

            # Dark Matter superposed footprint
            total_drag = (g_eff_main - g_N_main) + (g_eff_bullet - g_N_bullet)
            norm_factor = np.max(total_drag) if np.max(total_drag) > 0 else 1

            ax.clear()
            ax.contourf(X_kpc, Y_kpc, total_drag / norm_factor, levels=25, cmap="magma", vmin=0, vmax=0.7)

            # Render Core bounds
            ax.scatter(
                [pos_main_x / KPC],
                [0],
                color="cyan",
                marker="o",
                s=150,
                edgecolor="white",
                label="Main Cluster Core",
            )
            ax.scatter(
                [pos_bullet_x / KPC],
                [0],
                color="lime",
                marker="o",
                s=80,
                edgecolor="white",
                label="Bullet Core",
            )

            # Add tracking
            ax.set_title("First-Principles Topological Lensing (A0 Metric Extension)", color="white", pad=35)
            ax.text(
                0.5,
                1.02,
                baryon_state,
                transform=ax.transAxes,
                color="gray",
                fontsize=10,
                ha="center",
            )

            ax.axis("off")
            ax.legend(loc="lower left", facecolor="black", edgecolor="white", labelcolor="white")

            writer.grab_frame()
            if i % 10 == 0:
                print(f"Rendered: {i}/{FRAMES} Frames")

    plt.close(fig)
    print(f"Complete. 30s Visual simulation saved to {output_path}")


if __name__ == "__main__":
    animate_bullet_cluster()
