"""
Window-blind / bounding-plane figure — the two orthogonal "3"s (WS-T).
======================================================================

One spring, TWO orthogonal DOF = the two "3"s (master-equation.md:20, Grant-ratified):
  STRETCH (length) -> eps -> C -> trampoline SHEET -> A1 dilatation-MASS "3" (m_e c^2),
                                                       translational/E sector = the CVR H(s).
  BOW (shape/buckle) -> microrotation omega -> mu -> L -> window BLINDS ->
                                                       Cosserat (2,3) WINDING-charge "3",
                                                       microrotational/B sector (charge = Beltrami helicity).

NOT two impedance branches (Z->0 vs Z->inf is GAUGE, not a branch -- trampoline-framework.md:6.1,
Mobius Z<->1/Z, |Gamma|=1). NOT wired together (never wire the winding into the breather's phasor
(V_inc,V_ref) -- the genesis-24/crystal w_pol=0 double-count).

Conceptual schematic; deterministic; re-runnable (the audit reproduces the figure).
    PYTHONPATH=$PWD/src python src/scripts/vol_1_foundations/window_blind_two_threes.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle  # noqa: E402

OUT = Path(__file__).parent / "_output"
OUT.mkdir(exist_ok=True)

E_COL = "#1f6fb4"   # E / epsilon / mass-dilatation sheet
B_COL = "#b4451f"   # B / mu / charge-winding blinds


def coil(ax, x0, x1, y0, n=9, amp=0.16, color="k", lw=2.0, arc=0.0):
    """Draw a coil spring from x0->x1 at height y0. arc!=0 bows the centerline."""
    t = np.linspace(0, 1, 400)
    x = x0 + (x1 - x0) * t
    spine = y0 + arc * np.sin(np.pi * t)            # bowed centerline if arc!=0
    y = spine + amp * np.sin(2 * np.pi * n * t)
    ax.plot(x, y, color=color, lw=lw, solid_capstyle="round")
    ax.plot([x0 - 0.12, x0], [y0, y0], color=color, lw=lw)  # leads
    ax.plot([x1, x1 + 0.12], [spine[-1], spine[-1]], color=color, lw=lw)


def panelA(ax):
    ax.set_title("STRETCH DOF  →  mass-dilatation \"3\"", fontsize=11, color=E_COL)
    coil(ax, 0.15, 1.55, 2.6, color=E_COL)
    ax.annotate("", xy=(1.55, 2.95), xytext=(0.15, 2.95),
                arrowprops=dict(arrowstyle="<->", color=E_COL, lw=1.3))
    ax.text(0.85, 3.05, "length (stretch)", ha="center", fontsize=8.5, color=E_COL)
    ax.annotate("", xy=(0.85, 1.95), xytext=(0.85, 2.35),
                arrowprops=dict(arrowstyle="-|>", color="grey", lw=1.4))
    # trampoline sheet (parallelogram + grid)
    sheet = Polygon([(0.25, 0.7), (1.55, 0.7), (1.85, 1.55), (0.55, 1.55)],
                    closed=True, fill=True, fc=E_COL, ec=E_COL, alpha=0.18, lw=1.5)
    ax.add_patch(sheet)
    for f in np.linspace(0.18, 0.82, 4):
        ax.plot([0.25 + 1.3 * f, 0.55 + 1.3 * f], [0.7, 1.55], color=E_COL, lw=0.6, alpha=0.6)
        ax.plot([0.25 + 0.3 * f, 1.55 + 0.3 * f], [0.7 + 0.85 * f, 0.7 + 0.85 * f],
                color=E_COL, lw=0.6, alpha=0.6)
    ax.text(1.05, 0.42, "trampoline SHEET\n(compliance)", ha="center", fontsize=8.5, color=E_COL)
    ax.text(1.05, 2.05, r"$\varepsilon \to C$", ha="center", fontsize=10, color=E_COL)
    ax.text(1.05, -0.05,
            "A1 dilatation-MASS \"3\"  ($m_e c^2$)\ntranslational / E sector\n= the CVR $H(s)$ breather",
            ha="center", fontsize=8.5, color=E_COL,
            bbox=dict(boxstyle="round", fc="white", ec=E_COL, alpha=0.9))
    ax.set_xlim(-0.2, 2.1); ax.set_ylim(-0.7, 3.3); ax.axis("off")


def panelB(ax):
    ax.set_title("BOW DOF  →  charge-winding \"3\"", fontsize=11, color=B_COL)
    coil(ax, 0.15, 1.55, 2.6, color=B_COL, arc=0.42)          # bowed spring
    # microrotation (twist) arrow
    ax.add_patch(FancyArrowPatch((0.7, 3.1), (1.0, 3.1), connectionstyle="arc3,rad=-0.9",
                                 arrowstyle="-|>", color=B_COL, lw=1.4, mutation_scale=12))
    ax.text(0.85, 3.32, r"microrotation $\omega$", ha="center", fontsize=8.5, color=B_COL)
    ax.annotate("", xy=(0.85, 1.95), xytext=(0.85, 2.35),
                arrowprops=dict(arrowstyle="-|>", color="grey", lw=1.4))
    # window blinds (angled slats = bounding-face orientation)
    for i, yb in enumerate(np.linspace(0.75, 1.5, 5)):
        sl = Rectangle((0.55, yb), 1.0, 0.10, angle=18, fc=B_COL, ec=B_COL, alpha=0.30, lw=1.0)
        ax.add_patch(sl)
    ax.text(1.05, 0.42, "window BLINDS\n(bounding-face angle)", ha="center", fontsize=8.5, color=B_COL)
    ax.text(1.7, 2.05, r"$\mu \to L$", ha="center", fontsize=10, color=B_COL)
    ax.text(1.05, -0.05,
            "Cosserat (2,3) WINDING \"3\"\nmicrorotational / B sector\ncharge = Beltrami helicity",
            ha="center", fontsize=8.5, color=B_COL,
            bbox=dict(boxstyle="round", fc="white", ec=B_COL, alpha=0.9))
    ax.set_xlim(-0.2, 2.3); ax.set_ylim(-0.7, 3.5); ax.axis("off")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle('Window-blind / bounding-plane: one spring, two orthogonal "3"s (A1 $\\perp$ T2)',
                 fontsize=13)
    panelA(axes[0])
    panelB(axes[1])
    # orthogonality + the rules, spanning the bottom
    fig.text(0.5, 0.045,
             r'ONE spring, TWO orthogonal DOF = the two "3"s (master-equation.md:20).  '
             r'$Z\!\to\!0$ vs $Z\!\to\!\infty$ and the $\Gamma$-sign are GAUGE (Möbius $Z\!\leftrightarrow\!1/Z$, '
             r'$|\Gamma|=1$; trampoline §6.1), NOT a physical branch.',
             ha="center", fontsize=8.8)
    fig.text(0.5, 0.012,
             r'RULE — the sheet (mass) and the blinds (charge) are NOT wired: never wire the winding into the '
             r"breather's phasor $(V_{inc},V_{ref})$ — the genesis-24 / $w_{pol}=0$ double-count.",
             ha="center", fontsize=8.8, color="#7a1010")
    fig.tight_layout(rect=[0, 0.075, 1, 0.96])
    fig.savefig(OUT / "window_blind_two_threes.png", dpi=130)
    plt.close(fig)
    print(f"[OK] wrote {OUT / 'window_blind_two_threes.png'}")


if __name__ == "__main__":
    main()
