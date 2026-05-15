"""
Generate Figure 7 for trampoline-framework.md: cosmic boundary observability + God's Hand.

Visualizes the substrate-observability rule applied to OUR cosmic situation:
  - We sit inside the cosmic Γ=-1 boundary
  - The boundary has three integrated observables ℳ, 𝒬, 𝒥 (just like every other boundary)
  - 𝒥_cosmic = Ω_freeze · I_cosmic encodes the cosmological IC
  - "God's Hand" — the mechanism that set 𝒥_cosmic — is beyond the boundary, inaccessible
  - Three observational routes to constrain u_0*: α, G, cosmic 𝒥

Run from repo root:
  uv run --no-sync python src/scripts/trampoline_framework/generate_cosmic_ic.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Wedge

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


def fig_07_cosmic_ic():
    """Cosmic boundary with three observables + God's Hand beyond."""
    fig, ax = plt.subplots(figsize=(13, 10))
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.0, 3.0)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    # Background: "outside" — God's Hand region (cloudy / inaccessible)
    # Use light gradient + question marks scattered
    for r in np.linspace(2.8, 3.5, 50):
        circle = Circle((0, 0), r, fill=False, edgecolor=(0.92, 0.92, 0.96), linewidth=0.5)
        ax.add_patch(circle)

    # Scattered question marks beyond cosmic boundary
    rng = np.random.default_rng(7)
    for _ in range(15):
        angle = rng.uniform(0, 2 * np.pi)
        r = rng.uniform(2.5, 3.3)
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        ax.text(x, y, "?", fontsize=rng.choice([10, 12, 14, 16]), color="#aaa", alpha=0.5,
                ha="center", va="center", style="italic")

    # Cosmic boundary (Γ=-1 wall)
    cosmic_boundary = Circle((0, 0), 2.3, fill=False, edgecolor="red", linewidth=3.5, linestyle="-", zorder=5)
    ax.add_patch(cosmic_boundary)

    # Boundary envelope shading (annular)
    envelope_outer_pts = [(2.3 * np.cos(t), 2.3 * np.sin(t)) for t in np.linspace(0, 2 * np.pi, 100)]
    envelope_inner_pts = [(2.15 * np.cos(t), 2.15 * np.sin(t)) for t in np.linspace(2 * np.pi, 0, 100)]
    envelope_poly = Polygon(envelope_outer_pts + envelope_inner_pts, facecolor="#fdd", alpha=0.6, edgecolor="none", zorder=4)
    ax.add_patch(envelope_poly)

    # Inside: the observable universe (substrate region with stars / galaxies as dots)
    interior = Circle((0, 0), 2.15, fill=True, facecolor="#0a0a1f", edgecolor="none", zorder=3, alpha=0.92)
    ax.add_patch(interior)

    # Galaxies / stars inside
    rng = np.random.default_rng(42)
    for _ in range(180):
        angle = rng.uniform(0, 2 * np.pi)
        r = rng.uniform(0.2, 2.0)
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        sz = rng.choice([3, 5, 8, 12, 18])
        color = rng.choice(["#fff", "#fff8c0", "#aaccff", "#ffaa88"])
        ax.scatter(x, y, s=sz, c=color, alpha=0.7, zorder=4)

    # Cosmic rotation indication (subtle swirl) — to represent 𝒥_cosmic
    # Use arrows along the boundary
    for angle_deg in [30, 120, 210, 300]:
        angle = np.radians(angle_deg)
        x0 = 2.2 * np.cos(angle)
        y0 = 2.2 * np.sin(angle)
        # Tangent direction (CCW)
        tx = -np.sin(angle)
        ty = np.cos(angle)
        x1 = x0 + 0.25 * tx
        y1 = y0 + 0.25 * ty
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="->", color="#ff66aa", lw=2.2, alpha=0.9), zorder=10)

    # Earth / observer marker in the interior
    obs_x, obs_y = 0.45, -0.25
    ax.scatter(obs_x, obs_y, s=130, c="cyan", marker="*", edgecolors="white", linewidth=1.2, zorder=15)
    ax.text(obs_x + 0.18, obs_y - 0.10, "us\n(inside)", fontsize=9, color="cyan", fontweight="bold", zorder=15)

    # === Annotations ===

    # Cosmic boundary label
    ax.annotate(
        r"Cosmic $\Gamma = -1$ boundary $\partial\Omega$" "\n"
        r"$R_H \sim 10^{26}\,$m (parent BH's Schwarzschild radius)",
        xy=(0, 2.3),
        xytext=(0, 2.95),
        fontsize=10.5,
        color="red",
        fontweight="bold",
        ha="center",
        arrowprops=dict(arrowstyle="->", color="red", lw=1.2),
    )

    # Three observables — labels around the boundary
    # ℳ (mass)
    ax.annotate(
        r"$\mathcal{M}_{\text{cosmic}}$" "\n(total substrate strain)\n→ universe mass-energy",
        xy=(-1.95, 1.20),
        xytext=(-3.30, 1.85),
        fontsize=10,
        color="#d62728",
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="#d62728", lw=1.4),
    )

    # 𝒬 (charge)
    ax.annotate(
        r"$\mathcal{Q}_{\text{cosmic}}$" "\n(boundary linking)\n→ net charge $\\approx 0$",
        xy=(1.95, 1.20),
        xytext=(2.40, 1.85),
        fontsize=10,
        color="#2ca02c",
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="#2ca02c", lw=1.4),
    )

    # 𝒥 (angular momentum) — load-bearing for IC
    ax.annotate(
        r"$\mathcal{J}_{\text{cosmic}} = \Omega_{\text{freeze}} \cdot I_{\text{cosmic}}$" "\n"
        r"(boundary winding / spin)" "\n"
        r"$\to \Omega_{\text{freeze}}$ — the IC",
        xy=(0, -2.30),
        xytext=(0, -2.85),
        fontsize=11,
        color="#9467bd",
        fontweight="bold",
        ha="center",
        arrowprops=dict(arrowstyle="->", color="#9467bd", lw=1.6),
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#f5e6ff", edgecolor="#9467bd", linewidth=1.5, alpha=0.95),
    )

    # "God's Hand" annotation — the inaccessible region beyond
    ax.text(
        -2.85,
        -1.85,
        "God's Hand:\nwhat set $\\mathcal{J}_{\\text{cosmic}}$\nbeyond the boundary,\ninaccessible from inside",
        fontsize=10,
        color="#aa6600",
        fontweight="bold",
        ha="center",
        style="italic",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#fff8e0", edgecolor="#cc9933", alpha=0.92, linewidth=1.5),
    )

    # Three observational routes annotation (inside)
    routes_text = (
        "Three observational routes to $u_0^*$:" "\n\n"
        r"1. Electromagnetic — $\alpha$ to 12 dec." "\n"
        r"2. Gravitational — $G$ to ~4 dec." "\n"
        r"3. Cosmological — $\mathcal{J}_{\text{cosmic}}$ via CMB/LSS"
        "\n\n"
        "All three MUST give same $u_0^*$\n"
        "or framework fails (falsification)"
    )
    ax.text(
        2.85,
        -1.70,
        routes_text,
        fontsize=9,
        color="white",
        fontweight="normal",
        ha="center",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#1f2a44", edgecolor="cyan", alpha=0.95, linewidth=1.2),
    )

    # Substrate-observability rule reminder at top
    ax.text(
        0,
        2.65,
        "Substrate-observability rule applied to ourselves",
        fontsize=11,
        color="#444",
        ha="center",
        fontweight="bold",
        style="italic",
    )

    # Title
    ax.set_title(
        "Cosmic boundary observability — $\\Omega_{\\text{freeze}}$ as IC encoded in $\\mathcal{J}_{\\text{cosmic}}$\n"
        "We characterize the boundary from inside (3 observables); the mechanism that set it is on the other side",
        fontsize=12,
        pad=15,
    )

    plt.tight_layout()
    output_path = OUTDIR / "07_cosmic_ic_gods_hand.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"✓ {output_path}")


if __name__ == "__main__":
    fig_07_cosmic_ic()
