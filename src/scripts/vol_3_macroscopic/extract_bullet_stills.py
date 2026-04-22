"""
Generates annotated 2D static stills of the Axiom 4 Bullet Cluster collision sequence
to embed directly into the manuscript.
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Ensure local ave package is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from ave.core.constants import M_SUN, G
from ave.regime_3_saturated.galactic_rotation import ave_saturation_acceleration, A0_LATTICE


def extract_bullet_stills():
    """
    Renders 3 explicit 2D collision phases (Entry, Crossing, Exit)
    annotated with the formal saturation limits.
    """
    KPC = 3.086e19  # m
    GRID_MIN, GRID_MAX, GRID_RES = -1500 * KPC, 1500 * KPC, 250
    x = np.linspace(GRID_MIN, GRID_MAX, GRID_RES)
    y = np.linspace(GRID_MIN, GRID_MAX, GRID_RES)
    X_si, Y_si = np.meshgrid(x, y)
    X_kpc = X_si / KPC
    Y_kpc = Y_si / KPC

    mass_main = 1e14 * M_SUN
    mass_bullet = 1e13 * M_SUN

    # 3 Distinct time snapshots (Positions in KPC)
    # 0 = Approaching, 1 = Cores Overlapping, 2 = Exiting (Offset map)
    phases = [
        {
            "main_x": -900,
            "bullet_x": 900,
            "title": "Phase 1: Pre-Collision Vectors\nDark Matter Halos (Back-EMF) Intact",
        },
        {
            "main_x": -100,
            "bullet_x": 100,
            "title": "Phase 2: Kinematic Crossing\nGas Cores Stall, Linear Halos Superimpose",
        },
        {
            "main_x": 400,
            "bullet_x": -500,
            "title": "Phase 3: Spatial Offset\nHalos cross through unobstructed (Bullet Cluster Map)",
        },
    ]

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for i, phase in enumerate(phases):
        pos_m_si = phase["main_x"] * KPC
        pos_b_si = phase["bullet_x"] * KPC

        # Calculate Bare Mass
        r_main = np.sqrt((X_si - pos_m_si) ** 2 + Y_si**2)
        r_main = np.maximum(r_main, 20 * KPC)
        g_N_main = G * mass_main / (r_main**2)

        r_bullet = np.sqrt((X_si - pos_b_si) ** 2 + Y_si**2)
        r_bullet = np.maximum(r_bullet, 20 * KPC)
        g_N_bullet = G * mass_bullet / (r_bullet**2)

        # Saturation Mapping
        g_eff_main = np.vectorize(lambda g: ave_saturation_acceleration(g, a0=A0_LATTICE))(g_N_main)
        g_eff_bullet = np.vectorize(lambda g: ave_saturation_acceleration(g, a0=A0_LATTICE))(g_N_bullet)

        total_drag = (g_eff_main - g_N_main) + (g_eff_bullet - g_N_bullet)
        norm_factor = np.max(total_drag) if np.max(total_drag) > 0 else 1

        # Plot as a 2D Heatmap
        ax = axes[i]
        c = ax.contourf(X_kpc, Y_kpc, total_drag / norm_factor, levels=30, cmap="magma", vmin=0, vmax=0.7)

        # Overlay the baryonic point masses
        ax.scatter(
            [phase["main_x"]],
            [0],
            color="cyan",
            marker="o",
            s=100,
            edgecolor="white",
            label="Main Baryonic Core",
        )
        ax.scatter(
            [phase["bullet_x"]],
            [0],
            color="lime",
            marker="o",
            s=60,
            edgecolor="white",
            label="Bullet Baryonic Core",
        )

        # Add explicit Annotations
        if i == 1:
            ax.annotate(
                "Linear Superposition\n(No Shock Damping)",
                xy=(0, 200),
                xytext=(0, 700),
                arrowprops=dict(facecolor="white", shrink=0.05),
                color="white",
                ha="center",
            )
        if i == 2:
            ax.annotate(
                "Offset Halo\n(True Dark Matter)",
                xy=(phase["main_x"], 150),
                xytext=(phase["main_x"], 600),
                arrowprops=dict(facecolor="white", shrink=0.05),
                color="white",
                ha="center",
            )
            ax.annotate(
                "Stalled Gas",
                xy=(phase["main_x"] - 200, 0),
                xytext=(phase["main_x"] - 200, -500),
                arrowprops=dict(facecolor="red", shrink=0.05),
                color="red",
                ha="center",
            )

        ax.set_title(phase["title"], color="white", pad=15)
        ax.set_facecolor("black")
        ax.axis("off")
        if i == 0:
            ax.legend(loc="lower left")

    fig.patch.set_facecolor("black")
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), "../../../assets/sim_outputs/bullet_annotated_stills.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
    print(f"Annotated stills saved to {output_path}")


if __name__ == "__main__":
    extract_bullet_stills()
