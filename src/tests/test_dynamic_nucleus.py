"""
Dynamic Nucleus Visualizer
--------------------------
Generates animated 360-degree rotating GIFs of the 3D topological
Nucleon knots (e.g., Helium-4 Alpha Core, Lithium-7 Dual-Shell)
to allow the user to observe the complex intersecting geometry
from all structural angles.
"""

import os

import matplotlib.patheffects as pe
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
            "label": "Proton",
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
            "label": "Neutron",
        },
        {
            "shift": [shift_distance, -shift_distance, -shift_distance],
            "rot": [0, np.pi / 2, 0],
            "color": "#00ffcc",
        },
    ]
    return NucleonCombiner.assemble_cluster(FundamentalTopologies.generate_borromean_6_3_2, placements)


def construct_lithium_7(shift_distance: float):
    core_shift = shift_distance
    outer_shift = shift_distance * 2.2
    placements = [
        # Core
        {
            "shift": [core_shift, core_shift, core_shift],
            "rot": [0, 0, 0],
            "color": "#ff3366",
            "label": "Core Proton",
        },
        {
            "shift": [-core_shift, -core_shift, core_shift],
            "rot": [0, 0, np.pi / 2],
            "color": "#ff3366",
        },
        {
            "shift": [-core_shift, core_shift, -core_shift],
            "rot": [np.pi / 2, 0, 0],
            "color": "#00ffcc",
            "label": "Core Neutron",
        },
        {
            "shift": [core_shift, -core_shift, -core_shift],
            "rot": [0, np.pi / 2, 0],
            "color": "#00ffcc",
        },
        # Outer Shell
        {
            "shift": [outer_shift, -outer_shift, outer_shift],
            "rot": [0, np.pi / 4, 0],
            "color": "#ff99aa",
            "label": "Outer Proton",
        },
        {
            "shift": [-outer_shift, -outer_shift, -outer_shift],
            "rot": [np.pi / 4, 0, 0],
            "color": "#99ffee",
            "label": "Outer Neutron",
        },
        {
            "shift": [outer_shift, outer_shift, -outer_shift],
            "rot": [0, 0, np.pi / 4],
            "color": "#99ffee",
        },
    ]
    return NucleonCombiner.assemble_cluster(FundamentalTopologies.generate_borromean_6_3_2, placements)


def create_nucleus_gif(nucleus_cluster, output_name: str, title: str, bound=4.5):
    """
    Renders the static 3D mesh and animates the camera azimuth to output a GIF.
    """
    fig = plt.figure(figsize=(10, 10))
    fig.patch.set_facecolor("#0f0f0f")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#0f0f0f")

    # 1. Base Rendering
    for nucleon in nucleus_cluster:
        rings = nucleon["mesh"]
        color = nucleon["color"]

        # Bounding sphere for visual depth
        all_points = np.vstack(rings)
        centroid = np.mean(all_points, axis=0)
        u = np.linspace(0, 2 * np.pi, 30)
        v = np.linspace(0, np.pi, 20)
        r_bound = 1.3
        sx = centroid[0] + r_bound * np.outer(np.cos(u), np.sin(v))
        sy = centroid[1] + r_bound * np.outer(np.sin(u), np.sin(v))
        sz = centroid[2] + r_bound * np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(sx, sy, sz, color=color, alpha=0.08, edgecolor="none")

        # The 6^3_2 Knot Meshes
        for i, ring_coords in enumerate(rings):
            lbl = nucleon.get("label", "") if i == 0 else ""
            ax.plot(
                ring_coords[:, 0],
                ring_coords[:, 1],
                ring_coords[:, 2],
                color=color,
                linewidth=2.5,
                alpha=0.9,
                label=lbl,
                path_effects=[pe.Stroke(linewidth=4.5, foreground="black"), pe.Normal()],
            )

    ax.set_title(title, color="white", fontsize=18, pad=20)

    # Legend deduplication
    handles, labels = ax.get_legend_handles_labels()
    unique_labels = {}
    for h, l in zip(handles, labels):
        if l and l not in unique_labels:
            unique_labels[l] = h
    if unique_labels:
        ax.legend(
            unique_labels.values(),
            unique_labels.keys(),
            facecolor="#111111",
            edgecolor="#333333",
            labelcolor="white",
            loc="upper left",
            bbox_to_anchor=(0.0, 1.0),
        )

    # Clean formatting
    ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.grid(False)
    ax.axis("off")
    ax.set_xlim([-bound, bound])
    ax.set_ylim([-bound, bound])
    ax.set_zlim([-bound, bound])

    # 2. Animation Logic
    frames = 180  # Number of frames for 360 rotation

    def update(frame):
        # Calculate angle
        azim = frame * (360.0 / frames)
        # Gentle bobbing on elevation to see "over" the top slightly
        elev = 15 + 5 * np.sin(frame * (2 * np.pi / frames))
        ax.view_init(elev=elev, azim=azim)
        return (fig,)

    print(f"[*] Compiling frames for {output_name}...")
    anim = FuncAnimation(fig, update, frames=frames, interval=80, blit=False)

    os.makedirs("tests/outputs/gifs", exist_ok=True)
    out_path = os.path.join("tests/outputs/gifs", output_name)

    # Export via Pillow
    anim.save(out_path, writer="pillow", fps=15, savefig_kwargs={"facecolor": fig.get_facecolor()})
    plt.close()
    print(f"[*] Successfully saved GIF: {out_path}")


if __name__ == "__main__":
    # --- Execute Render Queue ---

    # 1. Helium-4
    he4_cluster = construct_helium_4(shift_distance=0.85)
    create_nucleus_gif(
        he4_cluster,
        "helium_4_rotation.gif",
        title="Helium-4 (Alpha Particle)\nTetrahedral Closed Topology",
        bound=3.0,
    )

    # 2. Lithium-7
    li7_cluster = construct_lithium_7(shift_distance=0.85)
    create_nucleus_gif(
        li7_cluster,
        "lithium_7_rotation.gif",
        title="Lithium-7 (Dual-Shell)\nAsymmetrical Topological Binding",
        bound=4.5,
    )
