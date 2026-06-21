"""
Neon-20 poly-alpha bipyramid geometry plotter (illustrative — geometry only).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script renders the trigonal-bipyramid geometry of the 5-alpha-particle
^20Ne structure with normalized geometric parameters (r=1.0, h=1.5 arbitrary
units). The "Manuscript-pinned mass = 18617.730 MeV" tech-box annotation cites a
manuscript-pinned value (canonical leaf
manuscript/ave-kb/vol1/operators-and-regimes/ch5-universal-spatial-tension/),
NOT a value computed by this script. The mass derivation chain (sum of
topological pairwise binding energies over the 5-alpha bipyramid) lives in
`solve_neon.py` / `simulate_atomic_spectra.py` and corpus leaves at
`manuscript/ave-kb/vol6/period-2/neon/*.md`.
"""

import matplotlib.pyplot as plt
import numpy as np

from ave.viz import style
from ave_path_util import SIM_OUTPUTS

# assets/figures (repo-root-anchored sibling of assets/sim_outputs).
_FIGURES_DIR = SIM_OUTPUTS.parent / "figures"

# Manuscript-pinned ^20Ne mass [MeV] — canonical value (NOT computed here).
NEON20_MASS_MEV = 18617.730


def _style_3d_axes(ax) -> None:
    """Make a 3D Axes legible on the white print background.

    The print rcParams do not reach 3D panes / pane edges / tick colours, so set
    them explicitly: transparent panes, light pane edges, black ticks.
    """
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        axis.pane.set_edgecolor(style.COLORS["muted"])
        axis.pane.set_alpha(0.15)


def create_neon20_plot() -> None:
    style.apply("print")

    fig = plt.figure(figsize=style.figsize("square"))
    ax = fig.add_subplot(111, projection="3d")
    _style_3d_axes(ax)

    # Trigonal bipyramid geometry for the 5 alpha particles (arbitrary units).
    r = 1.0
    h = 1.5

    eq1 = np.array([r, 0, 0])
    eq2 = np.array([-0.5 * r, r * np.sqrt(3) / 2, 0])
    eq3 = np.array([-0.5 * r, -r * np.sqrt(3) / 2, 0])
    p1 = np.array([0, 0, h])
    p2 = np.array([0, 0, -h])
    points = [eq1, eq2, eq3, p1, p2]

    bonds = [
        (eq1, eq2), (eq2, eq3), (eq3, eq1),
        (eq1, p1), (eq2, p1), (eq3, p1),
        (eq1, p2), (eq2, p2), (eq3, p2),
    ]
    for pA, pB in bonds:
        ax.plot(
            [pA[0], pB[0]], [pA[1], pB[1]], [pA[2], pB[2]],
            color=style.COLORS["ave"], lw=2.5, alpha=0.85,
        )

    # Alpha particles as spheres.
    u, v = np.mgrid[0 : 2 * np.pi : 30j, 0 : np.pi : 15j]
    sphere_r = 0.25
    for p in points:
        xs = p[0] + sphere_r * np.cos(u) * np.sin(v)
        ys = p[1] + sphere_r * np.sin(u) * np.sin(v)
        zs = p[2] + sphere_r * np.cos(v)
        ax.plot_surface(
            xs, ys, zs, color=style.COLORS["comparison"], alpha=0.9,
            edgecolor=style.COLORS["data"], lw=0.3,
        )

    label_color = style.COLORS["data"]
    ax.text(eq1[0] * 1.4, eq1[1] * 1.4, eq1[2], r"$\alpha_1$", color=label_color, fontsize=13, fontweight="bold")
    ax.text(eq2[0] * 1.4, eq2[1] * 1.4, eq2[2], r"$\alpha_2$", color=label_color, fontsize=13, fontweight="bold")
    ax.text(eq3[0] * 1.4, eq3[1] * 1.4, eq3[2], r"$\alpha_3$", color=label_color, fontsize=13, fontweight="bold")
    ax.text(p1[0], p1[1], p1[2] * 1.3, r"$\alpha_{North}$", color=label_color, fontsize=13, fontweight="bold")
    ax.text(p2[0], p2[1], p2[2] * 1.3, r"$\alpha_{South}$", color=label_color, fontsize=13, fontweight="bold")

    def annotate_bond(pA: np.ndarray, pB: np.ndarray, label: str) -> None:
        mid = (pA + pB) / 2
        ax.text(
            mid[0] * 1.1, mid[1] * 1.1, mid[2] * 1.1, label,
            color=style.COLORS["ave"], fontsize=12,
            bbox=dict(facecolor="white", edgecolor=style.COLORS["muted"], alpha=0.85),
        )

    annotate_bond(eq1, eq2, "$d_{eq}$")
    annotate_bond(eq1, p1, "$d_{polar}$")

    ax.text2D(
        0.02,
        0.92,
        "Neon-20 ($^{20}$Ne): trigonal bipyramid (5 $\\alpha$ particles)\n"
        "Total binding energy $= \\sum M_{topo}(d_{ij})$\n"
        f"Manuscript-pinned mass: {NEON20_MASS_MEV:.3f} MeV\n"
        "(derivation in solve_neon.py)",
        transform=ax.transAxes,
        color=style.COLORS["data"],
        fontsize=10,
        va="top",
        bbox=dict(facecolor="white", edgecolor=style.COLORS["comparison"], boxstyle="round,pad=0.4"),
    )

    ax.set_axis_off()
    ax.view_init(elev=20.0, azim=45)

    _FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    out_path = _FIGURES_DIR / "neon20_bipyramid.png"
    style.save(fig, out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    create_neon20_plot()
