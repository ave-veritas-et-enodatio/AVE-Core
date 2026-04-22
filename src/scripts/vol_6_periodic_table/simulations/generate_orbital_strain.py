"""
AVE MODULE: ORBITAL STRAIN VISUALIZER
--------------------------------------
Generates the 'topological strain' figures for the Periodic Table chapters.
These visualize the electron orbital topology around each nucleus:
  - The 1/r nuclear metric gradient (gravitational/Coulomb well)
  - Electron orbital tracks (Trefoil soliton standing-wave positions)
  - Dielectric saturation boundary (Axiom 4 p_c limit per shell)
  - Shell structure (1s, 2s, 2p harmonic resonances)

Each figure shows the continuous metric strain field M_A with electron
positions overlaid as physical geometric objects, not probability clouds.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from matplotlib.collections import LineCollection
import os
import sys

# AVE constants (imported from physics engine for traceability)
from ave.core.constants import ALPHA

A0_RELATIVE = 1.0 / ALPHA  # Bohr radius in units of l_node (~137)

# ---- Element definitions ----
# Each element defines:
#   Z, A: proton/nucleon count
#   shells: list of (n, l_label, count, radius_a0, color) for electron shells
#   title: figure title
#   caption_hint: what the captions originally said (for reference)

ELEMENTS = {
    "hydrogen": {
        "Z": 1,
        "A": 1,
        "shells": [
            (1, "1s", 1, 1.0, "#00DDFF"),
        ],
        "title": "Hydrogen ($^1$H): Topological Strain Field",
        "subtitle": "Single Trefoil ($3_1$) surfing the $1/r$ metric gradient at $a_0$",
    },
    "helium": {
        "Z": 2,
        "A": 4,
        "shells": [
            (1, "1s²", 2, 0.59, "#00DDFF"),
        ],
        "title": "Helium ($^4$He): Topological Strain Field",
        "subtitle": "Antipodal phase-locked Trefoils saturate the $1s$ shell",
    },
    "lithium": {
        "Z": 3,
        "A": 7,
        "shells": [
            (1, "1s²", 2, 0.37, "#00DDFF"),
            (2, "2s¹", 1, 3.10, "#FF6644"),
        ],
        "title": "Lithium ($^7$Li): Topological Strain Field",
        "subtitle": "Saturated inner metric reflects 3rd electron to $n=2$",
    },
    "beryllium": {
        "Z": 4,
        "A": 9,
        "shells": [
            (1, "1s²", 2, 0.31, "#00DDFF"),
            (2, "2s²", 2, 2.40, "#FF6644"),
        ],
        "title": "Beryllium ($^9$Be): Topological Strain Field",
        "subtitle": "Perpendicular harmonic phase-locking at $n=2$",
    },
    "boron": {
        "Z": 5,
        "A": 11,
        "shells": [
            (1, "1s²", 2, 0.27, "#00DDFF"),
            (2, "2s²2p¹", 3, 1.74, "#FF6644"),
        ],
        "title": "Boron ($^{11}$B): Topological Strain Field",
        "subtitle": "Trigonal $120°$ resonance in the crowded $n=2$ track",
    },
    "carbon": {
        "Z": 6,
        "A": 12,
        "shells": [
            (1, "1s²", 2, 0.23, "#00DDFF"),
            (2, "2s²2p²", 4, 1.45, "#FF6644"),
        ],
        "title": "Carbon ($^{12}$C): Topological Strain Field",
        "subtitle": "Tetrahedral packing of four solitons → $sp^3$ geometry",
    },
}


def generate_strain_figure(name, info, output_dir):
    """Generate a single orbital strain figure."""
    Z = info["Z"]
    shells = info["shells"]

    # Determine plot bounds based on outermost shell
    max_r = max(s[3] for s in shells)
    bounds = max_r * 2.0
    if bounds < 3.0:
        bounds = 3.0

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 10), facecolor="#0A0A1A")
    ax.set_facecolor("#0A0A1A")
    ax.set_aspect("equal")

    # ---- 1. Background metric strain field (1/r gradient from nucleus) ----
    grid = 500
    x = np.linspace(-bounds, bounds, grid)
    y = np.linspace(-bounds, bounds, grid)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    R_clamped = np.clip(R, 0.05, None)

    # Nuclear potential: Z/r (screened Coulomb)
    strain = Z / R_clamped

    # Normalize for visualization
    strain_norm = np.log1p(strain * 2.0)
    vmax = np.percentile(strain_norm, 99)

    # Plot the gradient field
    ax.imshow(
        strain_norm,
        extent=[-bounds, bounds, -bounds, bounds],
        origin="lower",
        cmap="inferno",
        alpha=0.6,
        vmin=0,
        vmax=vmax,
    )

    # ---- 2. Equipotential contour rings ----
    levels = np.linspace(0.5, vmax * 0.9, 12)
    ax.contour(X, Y, strain_norm, levels=levels, colors="white", linewidths=0.3, alpha=0.15)

    # ---- 3. Dielectric saturation boundaries (shell limits) ----
    for n, label, count, radius, color in shells:
        # Draw the orbital track as a glowing ring
        for width, alpha_val in [(4.0, 0.15), (2.5, 0.3), (1.5, 0.7)]:
            circle = Circle(
                (0, 0),
                radius,
                fill=False,
                edgecolor=color,
                linewidth=width,
                alpha=alpha_val,
                linestyle="-",
            )
            ax.add_patch(circle)

        # Draw saturation boundary (dashed outer limit)
        sat_circle = Circle(
            (0, 0),
            radius * 1.08,
            fill=False,
            edgecolor=color,
            linewidth=0.8,
            alpha=0.4,
            linestyle="--",
        )
        ax.add_patch(sat_circle)

        # Place electron markers along the orbital track
        if count == 1:
            angles = [0]
        elif count == 2:
            angles = [0, np.pi]  # Antipodal
        elif count == 3:
            angles = [0, 2 * np.pi / 3, 4 * np.pi / 3]  # Trigonal
        elif count == 4:
            # Tetrahedral projected to 2D → 90° cross
            angles = [0, np.pi / 2, np.pi, 3 * np.pi / 2]
        else:
            angles = np.linspace(0, 2 * np.pi, count, endpoint=False)

        for ang in angles:
            ex = radius * np.cos(ang)
            ey = radius * np.sin(ang)

            # Glow
            ax.plot(ex, ey, "o", color=color, markersize=14, alpha=0.2)
            ax.plot(ex, ey, "o", color=color, markersize=10, alpha=0.4)
            # Core
            ax.plot(ex, ey, "o", color="white", markersize=5, alpha=0.9)

            # Trefoil knot indicator (small 3-lobe pattern)
            for k in range(3):
                lobe_ang = ang + k * 2 * np.pi / 3
                lx = ex + 0.08 * bounds * np.cos(lobe_ang)
                ly = ey + 0.08 * bounds * np.sin(lobe_ang)
                ax.plot([ex, lx], [ey, ly], color=color, linewidth=0.6, alpha=0.3)

        # Shell label
        label_x = radius * np.cos(np.pi / 4) + bounds * 0.03
        label_y = radius * np.sin(np.pi / 4) + bounds * 0.03
        ax.text(
            label_x,
            label_y,
            f"$n={n}$: {label}",
            color=color,
            fontsize=11,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#0A0A1A", edgecolor=color, alpha=0.7),
        )

    # ---- 4. Central nucleus ----
    # Bright core
    for size, alpha_val in [(20, 0.1), (14, 0.2), (8, 0.5)]:
        ax.plot(0, 0, "o", color="#FFD700", markersize=size, alpha=alpha_val)
    ax.plot(0, 0, "o", color="white", markersize=4, alpha=0.9)

    # Nucleus label
    ax.text(bounds * 0.04, -bounds * 0.06, f"$Z={Z}$", color="#FFD700", fontsize=10, fontweight="bold")

    # ---- 5. Labels and formatting ----
    ax.set_xlim(-bounds, bounds)
    ax.set_ylim(-bounds, bounds)
    ax.set_xlabel("Spatial Radius ($a_0$)", color="white", fontsize=12)
    ax.set_ylabel("Spatial Radius ($a_0$)", color="white", fontsize=12)
    ax.tick_params(colors="white", labelsize=9)

    # Title
    ax.set_title(info["title"], color="white", fontsize=14, fontweight="bold", pad=15)
    ax.text(
        0.5,
        1.01,
        info["subtitle"],
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        color="#AAAAAA",
        fontsize=10,
        style="italic",
    )

    # Legend note
    legend_text = "● Trefoil ($3_1$) soliton  —— Orbital track  " "- - Saturation boundary"
    ax.text(
        0.5,
        -0.04,
        legend_text,
        transform=ax.transAxes,
        ha="center",
        va="top",
        color="#888888",
        fontsize=8,
    )

    # Save
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, f"{name}_topological_strain.png")
    # Special naming for Be, B, C (their .tex uses shorter names)
    if name == "beryllium":
        filepath = os.path.join(output_dir, "beryllium_strain.png")
    elif name == "boron":
        filepath = os.path.join(output_dir, "boron_strain.png")
    elif name == "carbon":
        filepath = os.path.join(output_dir, "carbon_strain.png")

    plt.savefig(filepath, dpi=300, bbox_inches="tight", facecolor="#0A0A1A")
    plt.close()
    print(f"[*] Saved: {filepath}")
    return filepath


if __name__ == "__main__":
    import pathlib

    repo_root = pathlib.Path(__file__).parent.parent.parent.parent.absolute()
    output_dir = str(repo_root / "periodic_table")

    print("--- AVE Orbital Strain Figure Generator ---")
    print(f"Output: {output_dir}/")
    print()

    for name, info in ELEMENTS.items():
        generate_strain_figure(name, info, output_dir)

    print()
    print("--- Generation Complete ---")
    print(f"Generated {len(ELEMENTS)} orbital strain figures.")
