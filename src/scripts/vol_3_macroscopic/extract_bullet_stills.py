"""
Generates 2D static stills of the Axiom-4 Bullet-Cluster collision sequence
to embed directly into the manuscript.

Each panel shows the AVE saturation "drag" field (g_eff - g_N, the back-EMF
lattice response summed over both colliding cores) as a heatmap, with the two
baryonic point masses overlaid. Three phases trace the collision: pre-collision,
kinematic crossing, and the post-crossing spatial offset that is the
Bullet-Cluster signature.

Physics is unchanged from the original driver; this version restyles through the
shared house style (ave.viz.style) — white print background, Okabe-Ito palette,
perceptually-uniform sequential colormap — and moves the per-phase titles out of
the raster into the LaTeX caption (ave-figure-discipline Axis 4).
"""

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import M_SUN, G
from ave.regime_3_saturated.galactic_rotation import A0_LATTICE, ave_saturation_acceleration
from ave.viz import style
from ave_path_util import sim_output


def extract_bullet_stills() -> None:
    """
    Renders 3 explicit 2D collision phases (Entry, Crossing, Exit) showing the
    AVE saturation drag field with the baryonic cores overlaid.
    """
    style.apply()  # white print profile

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
        {"main_x": -900, "bullet_x": 900},   # Phase 1: Pre-Collision
        {"main_x": -100, "bullet_x": 100},   # Phase 2: Kinematic Crossing
        {"main_x": 400, "bullet_x": -500},   # Phase 3: Spatial Offset
    ]

    fig, axes = plt.subplots(1, 3, figsize=style.figsize("wide"))

    # First pass: compute every phase's drag field so the heatmaps share one
    # normalisation (a common colour scale across panels is comparable).
    drag_fields = []
    for phase in phases:
        pos_m_si = phase["main_x"] * KPC
        pos_b_si = phase["bullet_x"] * KPC

        # Bare (Newtonian) acceleration of each core, softened at the centre.
        r_main = np.maximum(np.sqrt((X_si - pos_m_si) ** 2 + Y_si**2), 20 * KPC)
        g_N_main = G * mass_main / (r_main**2)

        r_bullet = np.maximum(np.sqrt((X_si - pos_b_si) ** 2 + Y_si**2), 20 * KPC)
        g_N_bullet = G * mass_bullet / (r_bullet**2)

        # Saturation mapping (Axiom-4 lattice response) per core.
        g_eff_main = np.vectorize(
            lambda g: ave_saturation_acceleration(g, a0=A0_LATTICE)
        )(g_N_main)
        g_eff_bullet = np.vectorize(
            lambda g: ave_saturation_acceleration(g, a0=A0_LATTICE)
        )(g_N_bullet)

        # The drag (back-EMF excess of the saturated field over the bare field).
        total_drag = (g_eff_main - g_N_main) + (g_eff_bullet - g_N_bullet)
        drag_fields.append(total_drag)

    vmax = max(float(np.max(d)) for d in drag_fields)
    vmax = vmax if vmax > 0 else 1.0

    im = None
    for i, (phase, total_drag) in enumerate(zip(phases, drag_fields)):
        ax = axes[i]

        im = ax.contourf(
            X_kpc, Y_kpc, total_drag, levels=30,
            cmap=style.CMAP_SEQ, vmin=0, vmax=vmax,
        )

        # Overlay the baryonic point masses (paired marker + colour, never
        # colour alone — ave-figure-discipline Axis 4).
        ax.scatter(
            [phase["main_x"]], [0],
            color=style.COLORS["ave"], marker="o", s=110,
            edgecolor="white", linewidth=1.0, zorder=5,
            label="Main baryonic core",
        )
        ax.scatter(
            [phase["bullet_x"]], [0],
            color=style.COLORS["accent"], marker="s", s=70,
            edgecolor="white", linewidth=1.0, zorder=5,
            label="Bullet baryonic core",
        )

        # Phase-specific guide annotations (data-anchored callouts, not titles).
        if i == 1:
            ax.annotate(
                "Linear superposition\n(no shock damping)",
                xy=(0, 200), xytext=(0, 850),
                arrowprops=dict(facecolor=style.COLORS["muted"],
                                edgecolor=style.COLORS["muted"], shrink=0.05),
                color=style.COLORS["muted"], ha="center",
            )
        if i == 2:
            ax.annotate(
                "Offset halo\n(saturation drag)",
                xy=(phase["main_x"], 150), xytext=(phase["main_x"], 850),
                arrowprops=dict(facecolor=style.COLORS["muted"],
                                edgecolor=style.COLORS["muted"], shrink=0.05),
                color=style.COLORS["muted"], ha="center",
            )
            ax.annotate(
                "Stalled gas",
                xy=(phase["main_x"] - 200, 0), xytext=(phase["main_x"] - 200, -850),
                arrowprops=dict(facecolor=style.COLORS["comparison"],
                                edgecolor=style.COLORS["comparison"], shrink=0.05),
                color=style.COLORS["comparison"], ha="center",
            )

        ax.set_xlabel(style.axis_label("Position", "x", "kpc"))
        if i == 0:
            ax.set_ylabel(style.axis_label("Position", "y", "kpc"))
        ax.set_aspect("equal")

    # One shared colorbar for the drag field (quantity + symbol + unit).
    cbar = fig.colorbar(im, ax=axes, fraction=0.025, pad=0.02)
    cbar.set_label(style.axis_label("Saturation drag", r"g_{\rm eff}-g_N", r"m/s$^2$"))

    # Single figure-level legend for the baryonic-core markers, below all panels
    # and clear of the per-panel x-axis labels (ave-figure-discipline Axis 3:
    # legend outside the data, no overlap).
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2,
               bbox_to_anchor=(0.5, -0.08))

    output_path = sim_output("bullet_annotated_stills.png")
    style.save(fig, output_path)
    print(f"Annotated stills saved to {output_path}")


if __name__ == "__main__":
    extract_bullet_stills()
