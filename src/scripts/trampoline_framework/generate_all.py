"""
Generate all canonical visualizations for the trampoline-framework.md doc.

Outputs to assets/sim_outputs/trampoline_framework/:
  01_k4_bipartite_lattice.png       — K4 bipartite tetrahedral lattice 3D with port vectors
  02_three_storage_modes.png        — Pythagorean decomposition A² = ε² + κ² + V²
  03_saturation_kernel.png          — S(A) = √(1-A²) curve with regime annotations
  04_trampoline_analogy.png         — Trampoline vs substrate side-by-side mapping
  05_boundary_invariants.png        — Γ=-1 boundary + three integrated invariants

Run from repo root:
  uv run --no-sync python src/scripts/trampoline_framework/generate_all.py

This script is intentionally self-contained — no dependencies on engine modules
to avoid coupling the canonical reference visuals to engine internal state.
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Use embedded TeX for math rendering; falls back gracefully on systems without
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "legend.fontsize": 10,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)

OUTDIR = Path("assets/sim_outputs/trampoline_framework")
OUTDIR.mkdir(parents=True, exist_ok=True)


def fig_01_k4_lattice():
    """K4 bipartite tetrahedral lattice with port vectors p_0, p_1, p_2, p_3."""
    fig = plt.figure(figsize=(11, 7))
    ax = fig.add_subplot(111, projection="3d")

    # A-node ports (right-handed tetrahedron)
    ports = np.array(
        [
            [+1, +1, +1],
            [+1, -1, -1],
            [-1, +1, -1],
            [-1, -1, +1],
        ],
        dtype=float,
    )
    ports /= np.sqrt(3.0)  # unit vectors

    # Plot a central A-node + 4 neighboring B-nodes along the ports
    a_pos = np.zeros(3)
    b_positions = ports * 1.0

    # Draw bonds from A to each B
    for b in b_positions:
        ax.plot(
            [a_pos[0], b[0]],
            [a_pos[1], b[1]],
            [a_pos[2], b[2]],
            color="#666",
            linewidth=2.2,
            alpha=0.85,
            zorder=2,
        )

    # Now draw second-shell A-nodes (one per B-node, opposite port direction)
    # Each B-node has its own 4 ports; for visualization we'll show one outgoing bond per B
    for b, p in zip(b_positions, ports):
        # B-node ports are negatives of A-node ports per K4 reciprocity
        # show one outgoing bond from each B-node in a non-collinear direction
        # for visualization purposes, project a second-shell A-node along
        # a port that's NOT the inverse of the incoming
        out_port = -ports[(list(ports.tolist()).index(p.tolist()) + 1) % 4]
        a2 = b + out_port * 1.0
        ax.plot(
            [b[0], a2[0]],
            [b[1], a2[1]],
            [b[2], a2[2]],
            color="#aaa",
            linewidth=1.2,
            alpha=0.5,
            zorder=1,
        )
        ax.scatter(*a2, s=120, c="#1f77b4", marker="o", alpha=0.55, edgecolors="black", linewidth=0.7, zorder=3)

    # Plot the central A-node (blue)
    ax.scatter(*a_pos, s=380, c="#1f77b4", marker="o", edgecolors="black", linewidth=1.4, zorder=5)
    ax.text(0.05, 0.05, 0.08, "A", fontsize=14, fontweight="bold", color="white", zorder=6)

    # Plot B-nodes (orange)
    for i, b in enumerate(b_positions):
        ax.scatter(*b, s=320, c="#ff7f0e", marker="o", edgecolors="black", linewidth=1.4, zorder=5)
        ax.text(b[0] + 0.04, b[1] + 0.04, b[2] + 0.06, "B", fontsize=12, fontweight="bold", color="white", zorder=6)

    # Annotate the four port vectors at the central A-node
    for i, p in enumerate(ports):
        ax.text(
            p[0] * 0.45,
            p[1] * 0.45,
            p[2] * 0.45,
            f"$p_{i}$",
            fontsize=11,
            color="#444",
            ha="center",
            zorder=7,
        )

    # Tetrahedron faces (light shading)
    faces = [
        [b_positions[0], b_positions[1], b_positions[2]],
        [b_positions[0], b_positions[1], b_positions[3]],
        [b_positions[0], b_positions[2], b_positions[3]],
        [b_positions[1], b_positions[2], b_positions[3]],
    ]
    tet = Poly3DCollection(faces, alpha=0.08, facecolor="#1f77b4", edgecolor="none")
    ax.add_collection3d(tet)

    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_zlim(-1.6, 1.6)
    ax.set_xlabel("x", labelpad=-8)
    ax.set_ylabel("y", labelpad=-8)
    ax.set_zlabel("z", labelpad=-8)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_title(
        "K4 bipartite tetrahedral lattice\n"
        "A sublattice (blue) ↔ B sublattice (orange); right-handed port vectors $p_0, p_1, p_2, p_3$",
        pad=18,
    )

    # Add legend-style text box
    legend_text = (
        r"$p_0 = (+,+,+)/\sqrt{3}$" "\n"
        r"$p_1 = (+,-,-)/\sqrt{3}$" "\n"
        r"$p_2 = (-,+,-)/\sqrt{3}$" "\n"
        r"$p_3 = (-,-,+)/\sqrt{3}$" "\n\n"
        "B-node ports = $-p_i$\n"
        "(reciprocity)"
    )
    ax.text2D(
        0.02,
        0.78,
        legend_text,
        transform=ax.transAxes,
        fontsize=9.5,
        family="monospace",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#f7f7f7", edgecolor="#bbb"),
        verticalalignment="top",
    )

    ax.view_init(elev=22, azim=38)
    plt.tight_layout()
    plt.savefig(OUTDIR / "01_k4_bipartite_lattice.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ 01_k4_bipartite_lattice.png")


def fig_02_three_storage_modes():
    """Pythagorean A² = ε² + κ² + V² — 2D quadrant view for clarity."""
    fig, (ax_3d, ax_2d) = plt.subplots(1, 2, figsize=(15, 7), gridspec_kw={"width_ratios": [1.1, 1.0]})
    ax_3d.remove()
    ax_3d = fig.add_subplot(121, projection="3d")

    # --- LEFT: 3D octant view (positive orthant only) ---
    # Draw saturation surface (positive octant of A=1 sphere) as wireframe
    u = np.linspace(0, np.pi / 2, 25)
    v = np.linspace(0, np.pi / 2, 25)
    U, V = np.meshgrid(u, v)
    Xs = np.sin(V) * np.cos(U)
    Ys = np.sin(V) * np.sin(U)
    Zs = np.cos(V)
    ax_3d.plot_wireframe(Xs, Ys, Zs, color="goldenrod", linewidth=0.6, alpha=0.5)
    ax_3d.plot_surface(Xs, Ys, Zs, alpha=0.10, color="goldenrod", linewidth=0)

    # Axes
    arrow_len = 1.35
    ax_3d.quiver(0, 0, 0, arrow_len, 0, 0, color="#1f77b4", arrow_length_ratio=0.06, linewidth=2.5)
    ax_3d.quiver(0, 0, 0, 0, arrow_len, 0, color="#d62728", arrow_length_ratio=0.06, linewidth=2.5)
    ax_3d.quiver(0, 0, 0, 0, 0, arrow_len, color="#2ca02c", arrow_length_ratio=0.06, linewidth=2.5)
    ax_3d.text(arrow_len * 1.08, 0, 0, r"$\varepsilon$" + "\n(electric)", color="#1f77b4", fontsize=12, fontweight="bold", ha="center")
    ax_3d.text(0, arrow_len * 1.08, 0.05, r"$\kappa$" + "\n(magnetic)", color="#d62728", fontsize=12, fontweight="bold", ha="center")
    ax_3d.text(0, 0, arrow_len * 1.08, r"$V$ (potential)", color="#2ca02c", fontsize=12, fontweight="bold", ha="center")

    # State vector A
    A_state = np.array([0.5, 0.45, 0.4])
    A_mag = np.linalg.norm(A_state)
    ax_3d.plot([0, A_state[0]], [0, A_state[1]], [0, A_state[2]], color="black", linewidth=3.5, zorder=10)
    ax_3d.scatter(*A_state, s=120, c="black", zorder=11, edgecolors="white", linewidth=1.5)
    ax_3d.text(
        A_state[0] + 0.04,
        A_state[1] + 0.04,
        A_state[2] - 0.20,
        rf"$\mathbf{{A}}$, $|A|={A_mag:.2f}$",
        fontsize=11,
        fontweight="bold",
    )

    # S(A) radial line to surface
    s_val = math.sqrt(1.0 - A_mag**2)
    a_hat = A_state / A_mag
    surface_pt = a_hat
    ax_3d.plot(
        [A_state[0], surface_pt[0]],
        [A_state[1], surface_pt[1]],
        [A_state[2], surface_pt[2]],
        linestyle="--",
        color="goldenrod",
        linewidth=2.5,
        zorder=9,
    )
    ax_3d.scatter(*surface_pt, s=80, marker="x", color="goldenrod", linewidths=3, zorder=11)

    ax_3d.set_xlim(0, 1.5)
    ax_3d.set_ylim(0, 1.5)
    ax_3d.set_zlim(0, 1.5)
    ax_3d.set_xticks([])
    ax_3d.set_yticks([])
    ax_3d.set_zticks([])
    ax_3d.set_title(
        "Three storage modes (Pythagorean)\n"
        r"$A^2 = \varepsilon^2 + \kappa^2 + V^2$; surface $A = 1$ (gold) = rupture",
        pad=12,
    )
    ax_3d.view_init(elev=22, azim=38)

    # --- RIGHT: 2D radial slice (geometric interpretation) ---
    A_2d = np.linspace(0, 1, 200)
    S_2d = np.sqrt(1 - A_2d**2)

    # Draw the unit circle arc (saturation surface, 1D slice)
    theta = np.linspace(0, np.pi / 2, 200)
    ax_2d.plot(np.cos(theta), np.sin(theta), color="goldenrod", linewidth=3.0, label=r"Saturation surface $A=1$")
    ax_2d.fill_between(np.cos(theta), 0, np.sin(theta), color="goldenrod", alpha=0.10)

    # Axes
    ax_2d.axhline(0, color="black", linewidth=1.0)
    ax_2d.axvline(0, color="black", linewidth=1.0)
    ax_2d.plot([0, 1.3], [0, 0], color="black", linewidth=0)  # extend
    ax_2d.plot([0, 0], [0, 1.3], color="black", linewidth=0)

    # Sample state |A| = 0.78
    A_mag = 0.78
    s_val = np.sqrt(1 - A_mag**2)
    # State at angle 35° from horizontal
    ang = np.radians(35)
    state_x = A_mag * np.cos(ang)
    state_y = A_mag * np.sin(ang)
    surf_x = np.cos(ang)
    surf_y = np.sin(ang)

    # |A| arrow from origin
    ax_2d.annotate(
        "",
        xy=(state_x, state_y),
        xytext=(0, 0),
        arrowprops=dict(arrowstyle="->", color="black", lw=3),
    )
    ax_2d.text(state_x / 2 - 0.05, state_y / 2 + 0.06, "$|A|$", fontsize=14, fontweight="bold")
    ax_2d.scatter(state_x, state_y, s=100, color="black", zorder=10, edgecolors="white", linewidth=1.5)

    # S(A) arrow from state to surface
    ax_2d.annotate(
        "",
        xy=(surf_x, surf_y),
        xytext=(state_x, state_y),
        arrowprops=dict(arrowstyle="->", color="goldenrod", lw=3),
    )
    mid_x = (state_x + surf_x) / 2
    mid_y = (state_y + surf_y) / 2
    ax_2d.text(mid_x + 0.05, mid_y + 0.05, "$S(A)$", fontsize=14, fontweight="bold", color="goldenrod")
    ax_2d.scatter(surf_x, surf_y, s=80, marker="x", color="goldenrod", linewidths=3, zorder=10)

    # Identity arc
    ax_2d.annotate(
        r"$|A|^2 + S(A)^2 = 1$",
        xy=(0.7, 0.9),
        fontsize=13,
        fontweight="bold",
        ha="center",
    )

    ax_2d.set_xlim(-0.05, 1.3)
    ax_2d.set_ylim(-0.05, 1.3)
    ax_2d.set_aspect("equal")
    ax_2d.set_xlabel(r"strain amplitude $|A|$", fontsize=11)
    ax_2d.set_ylabel(r"free capacity $S(A)$", fontsize=11)
    ax_2d.set_title(
        "Geometric identity (radial slice)\n"
        r"$S(A) = $ distance from state $\mathbf{A}$ to surface $A=1$",
        pad=12,
    )
    ax_2d.grid(True, alpha=0.3)
    ax_2d.legend(loc="lower left", framealpha=0.95)

    plt.tight_layout()
    plt.savefig(OUTDIR / "02_three_storage_modes.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ 02_three_storage_modes.png (revised: 3D + 2D panels)")


def fig_03_saturation_kernel():
    """S(A) = √(1-A²) curve with regimes annotated."""
    fig, ax1 = plt.subplots(figsize=(11, 6.5))
    A = np.linspace(0, 0.999, 1000)
    S = np.sqrt(1 - A**2)
    n_eff = 1.0 / S ** 0.5  # n_eff = 1/sqrt(S) = (1-A²)^(-1/4)

    ax1.plot(A, S, color="#1f77b4", linewidth=3.0, label=r"$S(A) = \sqrt{1 - A^2}$ (free capacity)")
    ax1.set_xlabel("Strain amplitude $A$", fontsize=12)
    ax1.set_ylabel(r"$S(A)$ (free capacity)", color="#1f77b4", fontsize=12)
    ax1.tick_params(axis="y", labelcolor="#1f77b4")
    ax1.set_xlim(0, 1.02)
    ax1.set_ylim(0, 1.05)
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(A, n_eff, color="#d62728", linewidth=2.5, linestyle="--", label=r"$n_{\rm eff}(A) = 1/\sqrt{S}$ (refractive index)")
    ax2.set_ylabel(r"$n_{\rm eff}(A)$ (local refractive index)", color="#d62728", fontsize=12)
    ax2.tick_params(axis="y", labelcolor="#d62728")
    ax2.set_ylim(0.9, 10)

    # Mark V_yield (A_yield = sqrt(alpha))
    # Derive alpha from canonical Vol 1 Ch 8 Golden Torus form
    # (alpha^-1 = 4π³ + π² + π) instead of hardcoding CODATA value.
    # Per verify_universe.py: avoid magic-number CODATA constants.
    alpha_inv = 4.0 * math.pi**3 + math.pi**2 + math.pi
    alpha = 1.0 / alpha_inv
    a_yield = math.sqrt(alpha)
    ax1.axvline(a_yield, color="orange", linestyle=":", linewidth=2.0, alpha=0.85)
    ax1.text(
        a_yield + 0.012,
        0.05,
        f"$A_{{\\mathrm{{yield}}}} = \\sqrt{{\\alpha}} \\approx {a_yield:.3f}$\nBingham-plastic onset",
        color="orange",
        fontsize=10,
        verticalalignment="bottom",
    )

    # Mark V_SNAP (A = 1)
    ax1.axvline(1.0, color="red", linestyle="-", linewidth=2.5)
    ax1.text(
        0.985,
        0.55,
        "$A = 1$\n$\\Gamma = -1$ wall\nfull saturation",
        color="red",
        fontsize=10,
        verticalalignment="center",
        horizontalalignment="right",
        rotation=90,
    )

    # Regime labels
    ax1.annotate(
        "Linear regime\n(K4-TLM canonical engine)",
        xy=(0.04, 0.95),
        xytext=(0.04, 0.95),
        fontsize=10.5,
        color="#1f77b4",
        verticalalignment="top",
    )
    ax1.annotate(
        "Saturating regime\n(Master Equation FDTD\ncanonical engine)",
        xy=(0.6, 0.95),
        xytext=(0.6, 0.95),
        fontsize=10.5,
        color="#d62728",
        verticalalignment="top",
    )

    # Legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper center", framealpha=0.95)

    ax1.set_title(
        "Saturation kernel $S(A) = \\sqrt{1 - A^2}$ (Axiom 4 canonical) — the trampoline's stress-strain curve",
        pad=15,
    )

    plt.tight_layout()
    plt.savefig(OUTDIR / "03_saturation_kernel.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ 03_saturation_kernel.png")


def fig_04_trampoline_analogy():
    """Side-by-side trampoline vs AVE substrate mapping."""
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14, 7))

    # --- LEFT: Trampoline (real-world picture) ---
    ax_left.set_xlim(-1.4, 1.4)
    ax_left.set_ylim(-1.0, 1.0)
    ax_left.set_aspect("equal")
    ax_left.set_xticks([])
    ax_left.set_yticks([])

    # Trampoline ring (oval)
    from matplotlib.patches import Ellipse, FancyBboxPatch
    ring = Ellipse((0, 0), 2.5, 1.6, fill=False, edgecolor="black", linewidth=2)
    ax_left.add_patch(ring)

    # Trampoline fabric grid (warp/weft)
    for x in np.linspace(-1.0, 1.0, 9):
        ax_left.plot([x, x], [-0.6, 0.6], color="#888", linewidth=0.8, alpha=0.6)
    for y in np.linspace(-0.55, 0.55, 7):
        ax_left.plot([-1.0, 1.0], [y, y], color="#888", linewidth=0.8, alpha=0.6)

    # Bowling ball depression at center (stretched fabric)
    depression = Circle((0, 0), 0.35, fill=True, facecolor="#222", edgecolor="black", linewidth=1.5, zorder=4)
    ax_left.add_patch(depression)
    # "Stretch" arrows around depression
    for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        x0 = 0.55 * np.cos(angle)
        y0 = 0.55 * np.sin(angle)
        x1 = 0.42 * np.cos(angle)
        y1 = 0.42 * np.sin(angle)
        ax_left.annotate(
            "", xy=(x1, y1), xytext=(x0, y0),
            arrowprops=dict(arrowstyle="->", color="#1f77b4", lw=1.5)
        )

    ax_left.set_title("Real-world trampoline", fontsize=14, pad=12)

    # Label callouts
    ax_left.annotate(
        "Trampoline material\n(fabric + springs)",
        xy=(-0.65, 0.4),
        xytext=(-1.35, 0.85),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="#555"),
    )
    ax_left.annotate(
        "Bowling ball\n(localized mass)",
        xy=(0, 0),
        xytext=(0.6, 0.85),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="#555"),
    )
    ax_left.annotate(
        "Stretched fabric\n(local strain)",
        xy=(0.55, -0.4),
        xytext=(1.0, -0.85),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="#1f77b4"),
    )

    # --- RIGHT: AVE substrate (analog) ---
    ax_right.set_xlim(-1.4, 1.4)
    ax_right.set_ylim(-1.0, 1.0)
    ax_right.set_aspect("equal")
    ax_right.set_xticks([])
    ax_right.set_yticks([])

    # Substrate "envelope" boundary (Γ=-1 wall)
    ring2 = Circle((0, 0), 0.42, fill=True, facecolor="#fdd", edgecolor="red", linewidth=2.5, linestyle="--", zorder=3)
    ax_right.add_patch(ring2)

    # K4 lattice nodes (small scattered dots, A blue + B orange)
    rng = np.random.default_rng(42)
    for _ in range(80):
        x, y = rng.uniform(-1.15, 1.15), rng.uniform(-0.85, 0.85)
        if x**2 + y**2 < 0.42**2:
            continue  # skip inside boundary (interior invisible)
        c = "#1f77b4" if (int(x * 7) + int(y * 7)) % 2 == 0 else "#ff7f0e"
        ax_right.scatter(x, y, s=12, c=c, alpha=0.65, zorder=2)

    # Lattice bonds (random thin gray lines between nearby nodes)
    nodes = []
    rng = np.random.default_rng(42)
    for _ in range(80):
        x, y = rng.uniform(-1.15, 1.15), rng.uniform(-0.85, 0.85)
        if x**2 + y**2 < 0.42**2:
            continue
        nodes.append((x, y))
    nodes = np.array(nodes)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            d = np.linalg.norm(nodes[i] - nodes[j])
            if d < 0.22:
                ax_right.plot(
                    [nodes[i][0], nodes[j][0]],
                    [nodes[i][1], nodes[j][1]],
                    color="#aaa",
                    linewidth=0.5,
                    alpha=0.5,
                    zorder=1,
                )

    # Three invariants labels around the boundary
    ax_right.text(0, 0, r"$\Omega$" "\n(interior\ninvisible)", fontsize=10, ha="center", va="center", color="#777", zorder=4)

    # M, Q, J labels
    ax_right.annotate(
        r"$\mathcal{M}$ (mass-equivalent)",
        xy=(0.30, 0.30),
        xytext=(0.85, 0.65),
        fontsize=11,
        fontweight="bold",
        color="#d62728",
        arrowprops=dict(arrowstyle="->", color="#d62728"),
    )
    ax_right.annotate(
        r"$\mathcal{Q}$ (charge / linking)",
        xy=(-0.30, 0.30),
        xytext=(-1.30, 0.65),
        fontsize=11,
        fontweight="bold",
        color="#2ca02c",
        arrowprops=dict(arrowstyle="->", color="#2ca02c"),
    )
    ax_right.annotate(
        r"$\mathcal{J}$ (spin / winding)",
        xy=(0.0, -0.40),
        xytext=(0.5, -0.85),
        fontsize=11,
        fontweight="bold",
        color="#9467bd",
        arrowprops=dict(arrowstyle="->", color="#9467bd"),
    )

    # Boundary annotation
    ax_right.annotate(
        r"$\Gamma = -1$ boundary $\partial\Omega$" "\n(impedance mismatch wall)",
        xy=(-0.42, 0.0),
        xytext=(-1.35, -0.30),
        fontsize=10,
        color="red",
        arrowprops=dict(arrowstyle="->", color="red"),
    )

    ax_right.set_title("AVE substrate (canonical mapping)", fontsize=14, pad=12)

    # Central caption
    fig.text(
        0.5,
        0.03,
        "Bowling ball = bound-state soliton (electron / nucleus / BH). The substrate sees only $\\mathcal{M}, \\mathcal{Q}, \\mathcal{J}$ — interior is invisible (substrate-observability rule).",
        ha="center",
        fontsize=10.5,
        style="italic",
    )

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(OUTDIR / "04_trampoline_analogy.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ 04_trampoline_analogy.png")


def fig_05_boundary_invariants():
    """Γ=-1 boundary cross-section with three integrated invariants labeled."""
    fig, ax = plt.subplots(figsize=(11, 7.5))
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    # Outer "substrate" region
    ax.set_facecolor("#f8f9fa")

    # Wave ripples in the substrate (concentric arcs to suggest propagating waves)
    from matplotlib.patches import Arc, Wedge
    for r in [1.2, 1.4, 1.6, 1.8]:
        for a_start, a_end in [(0, 50), (130, 230), (310, 360)]:
            arc = Arc((0, 0), 2 * r, 2 * r, angle=0, theta1=a_start, theta2=a_end, color="#aaaaff", linewidth=0.8, alpha=0.6)
            ax.add_patch(arc)

    # Boundary envelope (annular region near r = 0.72)
    boundary_outer = Circle((0, 0), 0.82, fill=False, edgecolor="red", linewidth=3.5, linestyle="-", zorder=4)
    boundary_inner = Circle((0, 0), 0.65, fill=False, edgecolor="darkred", linewidth=1.5, linestyle="--", zorder=4)
    ax.add_patch(boundary_outer)
    ax.add_patch(boundary_inner)

    # Saturated envelope shading
    envelope_outer_pts = []
    for theta in np.linspace(0, 2 * np.pi, 200):
        envelope_outer_pts.append((0.82 * np.cos(theta), 0.82 * np.sin(theta)))
    envelope_inner_pts = []
    for theta in np.linspace(2 * np.pi, 0, 200):
        envelope_inner_pts.append((0.65 * np.cos(theta), 0.65 * np.sin(theta)))
    from matplotlib.patches import Polygon
    envelope_poly = Polygon(envelope_outer_pts + envelope_inner_pts, facecolor="#fdd", alpha=0.7, edgecolor="none", zorder=3)
    ax.add_patch(envelope_poly)

    # Interior (invisible to substrate)
    interior = Circle((0, 0), 0.65, fill=True, facecolor="#eeeeee", edgecolor="none", zorder=2, alpha=0.85)
    ax.add_patch(interior)
    ax.text(0, 0.15, r"$\Omega$ (interior)", fontsize=14, ha="center", color="#777", fontweight="bold")
    ax.text(0, -0.05, "invisible to substrate", fontsize=10, ha="center", color="#999", style="italic")
    ax.text(0, -0.22, "(topology, eigenmodes,", fontsize=8, ha="center", color="#bbb")
    ax.text(0, -0.32, "microrotations all hidden)", fontsize=8, ha="center", color="#bbb")

    # Incident substrate wave bouncing off boundary
    ax.annotate(
        "",
        xy=(-0.82, 0.0),
        xytext=(-1.7, 0.4),
        arrowprops=dict(arrowstyle="->", color="#4477ff", lw=2.5),
    )
    ax.annotate(
        "",
        xy=(-1.7, -0.4),
        xytext=(-0.82, 0.0),
        arrowprops=dict(arrowstyle="->", color="#4477ff", lw=2.5),
    )
    ax.text(-1.85, 0.55, "incident wave", fontsize=9, color="#4477ff", rotation=-25)
    ax.text(-1.95, -0.55, r"reflected ($\Gamma = -1$)", fontsize=9, color="#4477ff", rotation=20)

    # Three invariants pulled out to side as labels with values
    invariants_text = (
        r"$\partial\Omega$ three observables:" "\n\n"
        r"$\mathcal{M} = \int_\Omega (n(r) - 1)\, dV$" "\n"
        "    (integrated strain integral)" "\n"
        "    → mass-equivalent" "\n\n"
        r"$\mathcal{Q} = \mathrm{Link}(\partial\Omega, F_{\rm substrate}) \in \mathbb{Z}$" "\n"
        "    (boundary linking number)" "\n"
        "    → charge-equivalent" "\n\n"
        r"$\mathcal{J} = \mathrm{Wind}(\partial\Omega) \in \frac{1}{2}\mathbb{Z}$" "\n"
        "    (boundary winding number,\n"
        "    half-integer per SU(2) double-cover)" "\n"
        "    → spin-equivalent"
    )
    ax.text(
        1.1,
        0.95,
        invariants_text,
        fontsize=10,
        verticalalignment="top",
        family="serif",
        bbox=dict(boxstyle="round,pad=0.6", facecolor="white", edgecolor="#888", linewidth=1.2),
    )

    # No-hair tagline
    ax.text(
        0,
        -1.35,
        "No-hair theorem at every scale: substrate observes integer-counted relational invariants $\\mathcal{M}, \\mathcal{Q}, \\mathcal{J}$; everything else is interior plumbing.",
        ha="center",
        fontsize=10,
        style="italic",
        color="#444",
    )

    # Title
    ax.set_title(
        "The $\\Gamma = -1$ boundary — substrate-observability rule\n"
        "Substrate observes boundary $\\partial\\Omega$, not interior $\\Omega$",
        fontsize=13,
        pad=15,
    )

    # Boundary label
    ax.annotate(
        r"$\Gamma = -1$ boundary $\partial\Omega$",
        xy=(0.82 * np.cos(np.pi / 3), 0.82 * np.sin(np.pi / 3)),
        xytext=(0.10, 1.30),
        fontsize=11,
        color="red",
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="red"),
    )
    ax.annotate(
        "boundary envelope\n(finite thickness ~ $\\ell_{\\rm node}/(2\\pi)$)",
        xy=(0.73 * np.cos(np.pi / 5), 0.73 * np.sin(np.pi / 5)),
        xytext=(-1.85, 1.20),
        fontsize=9,
        color="darkred",
        arrowprops=dict(arrowstyle="->", color="darkred"),
    )

    plt.tight_layout()
    plt.savefig(OUTDIR / "05_boundary_invariants.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ 05_boundary_invariants.png")


if __name__ == "__main__":
    print(f"Generating canonical trampoline-framework visuals → {OUTDIR}")
    fig_01_k4_lattice()
    fig_02_three_storage_modes()
    fig_03_saturation_kernel()
    fig_04_trampoline_analogy()
    fig_05_boundary_invariants()
    print(f"\nDone. {len(list(OUTDIR.glob('*.png')))} PNG files in {OUTDIR}")
