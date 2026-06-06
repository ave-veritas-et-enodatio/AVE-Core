"""
Generate Figure 8 for trampoline-framework.md (and the primer Step 3.5):
the gyroscope-fabric — the substrate's inductive (mu / L) sector.

Under the gyroscope-primary framing, this is the inductive counterpart to the
capacitive trampoline figures (01-05): it depicts what a flat sheet cannot — a spin.

3-panel schematic mechanism diagram (no physical-constant claims):
  Panel A — REST: rotors wound to a handed rest-angle theta by the chiral
            twist-lacing; rotation RATE omega = 0  ->  magnetically neutral.
  Panel B — SPIN-UP: an applied field / trapped soliton spins the rotors to net
            omega = magnetic moment mu (biased handed) = the electron flywheel L = I*omega.
  Panel C — WHERE THE 1/2 LIVES: spin-1/2 is the (2,3) phase-space Clifford-torus
            winding of the EXTENDED loop (closing after 720 deg), NOT any single
            rotor; real space (inset) is a plain 0_1 unknot.

Run from repo root:
  PYTHONPATH=src python src/scripts/trampoline_framework/generate_gyroscope_fabric.py
"""

import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch

from ave_path_util import SIM_OUTPUTS

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "legend.fontsize": 9,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)

OUTDIR = SIM_OUTPUTS / "trampoline_framework"
OUTDIR.mkdir(parents=True, exist_ok=True)

ROTOR_R = 0.34
TILT_DEG = 26.0  # handed rest-angle theta (illustrative; same handed tilt across rotors = chirality)
GYRO_BLUE = "#1f77b4"
SPIN_RED = "#d62728"
SPRING_GRAY = "#8c8c8c"
FIELD_GREEN = "#2ca02c"

# rotor cluster (a small tetrahedral-flavoured triangle: evokes the K4 sampling of the continuum)
TRI = np.array([[0.0, 0.95], [-0.92, -0.62], [0.92, -0.62]])


def _spring(ax, p0, p1, coils=7, amp=0.06):
    """Zigzag spring (the elastic compliance / twist-lacing) between two rotors."""
    p0, p1 = np.array(p0, float), np.array(p1, float)
    d = p1 - p0
    length = np.hypot(*d)
    u = d / length
    n = np.array([-u[1], u[0]])
    # shorten so the spring meets rotor rims, not centres
    p0e, p1e = p0 + u * ROTOR_R, p1 - u * ROTOR_R
    seg = np.hypot(*(p1e - p0e))
    ts = np.linspace(0, 1, coils * 2 + 1)
    pts = [p0e + u * (t * seg) + n * (amp * ((-1) ** i) if 0 < i < len(ts) - 1 else 0.0)
           for i, t in enumerate(ts)]
    pts = np.array(pts)
    ax.plot(pts[:, 0], pts[:, 1], color=SPRING_GRAY, lw=1.5, zorder=1)


def _rotor(ax, c, spinning):
    """A spherical gyroscope-rotor: disc + handed tilted spin axis.
    spinning=False -> wound at rest (omega=0); True -> spun up (omega, L=I*omega)."""
    c = np.array(c, float)
    ax.add_patch(Circle(c, ROTOR_R, facecolor="#eaf2fb", edgecolor=GYRO_BLUE, lw=2.0, zorder=3))
    th = math.radians(TILT_DEG)
    axis = np.array([math.sin(th), math.cos(th)])  # handed tilt (same for all = chirality)
    color = SPIN_RED if spinning else GYRO_BLUE
    a0, a1 = c - axis * ROTOR_R * 1.15, c + axis * ROTOR_R * 1.15
    ax.plot([a0[0], a1[0]], [a0[1], a1[1]], color=color, lw=2.2, zorder=4)
    if spinning:
        ax.add_patch(Arc(c, ROTOR_R * 1.5, ROTOR_R * 0.85, angle=TILT_DEG,
                         theta1=25, theta2=310, color=SPIN_RED, lw=1.8, zorder=4))
        tip = c + axis * ROTOR_R * 2.0
        ax.add_patch(FancyArrowPatch(c + axis * ROTOR_R * 1.15, tip, arrowstyle="-|>",
                                     mutation_scale=13, color=SPIN_RED, lw=2.0, zorder=5))


def panel_a(ax):
    """REST: wound, not spinning."""
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.55, 1.75)
    ax.set_aspect("equal")
    ax.axis("off")
    for pair in ((0, 1), (1, 2), (2, 0)):
        _spring(ax, TRI[pair[0]], TRI[pair[1]])
    for c in TRI:
        _rotor(ax, c, spinning=False)
    # rest-angle theta arc on the top rotor (from vertical to the handed axis)
    top = TRI[0]
    ax.plot([top[0], top[0]], [top[1], top[1] + ROTOR_R * 1.5], color="0.55", lw=1.0, ls=":")
    ax.add_patch(Arc(top, ROTOR_R * 1.7, ROTOR_R * 1.7, angle=90, theta1=-TILT_DEG, theta2=0,
                     color="0.4", lw=1.2))
    ax.text(top[0] + 0.16, top[1] + ROTOR_R * 1.35, r"$\theta$", fontsize=12, color="0.3")
    ax.text(0, -1.32,
            "REST — wound to a handed rest-angle $\\theta$ (the chirality)\n"
            r"rotation rate $\omega = 0$  $\Rightarrow$  no net $B$ (magnetically neutral)"
            "\nthe winding is stored elastic energy, not circulation",
            ha="center", va="top", fontsize=9.5, color=GYRO_BLUE)
    ax.set_title("(A)  The gyroscope-fabric at rest", fontsize=11.5, pad=8)


def panel_b(ax):
    """SPIN-UP: net omega = magnetic moment."""
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.55, 1.75)
    ax.set_aspect("equal")
    ax.axis("off")
    for pair in ((0, 1), (1, 2), (2, 0)):
        _spring(ax, TRI[pair[0]], TRI[pair[1]])
    for c in TRI:
        _rotor(ax, c, spinning=True)
    # applied field / soliton excitation arrow
    ax.add_patch(FancyArrowPatch((-1.65, 1.45), (-0.7, 1.45), arrowstyle="-|>",
                                 mutation_scale=15, color=FIELD_GREEN, lw=2.0))
    ax.text(-1.62, 1.55, "applied field / trapped soliton", fontsize=8.5, color=FIELD_GREEN)
    # net magnetic moment mu (the aligned handed axis)
    th = math.radians(TILT_DEG)
    mu = np.array([math.sin(th), math.cos(th)])
    base = np.array([1.15, 0.25])
    ax.add_patch(FancyArrowPatch(base, base + mu * 0.95, arrowstyle="-|>",
                                 mutation_scale=16, color=SPIN_RED, lw=2.6))
    ax.text(base[0] + 0.30, base[1] + 0.62, r"net $\mu$", fontsize=12, color=SPIN_RED, fontweight="bold")
    ax.text(0, -1.32,
            r"SPIN-UP — net $\omega$  $\Rightarrow$  magnetic moment $\mu$ (biased handed)"
            "\nthe electron flywheel $L = I\\omega$; Larmor-precesses under $B$"
            "\n$L = I\\omega$ is the inertia $\\to \\mu \\to$ inductance",
            ha="center", va="top", fontsize=9.5, color=SPIN_RED)
    ax.set_title("(B)  Spin-up = magnetic moment", fontsize=11.5, pad=8)


def panel_c(ax):
    """WHERE THE 1/2 LIVES: the (2,3) phase-space winding, not any single rotor."""
    t = np.linspace(0, 2 * math.pi, 2000)
    x = np.cos(2 * t)   # 2 windings on the d-axis
    y = np.sin(3 * t)   # 3 windings on the q-axis
    ax.plot(x, y, color="#6a3d9a", lw=2.4, zorder=2)
    ax.set_xlim(-1.55, 1.55)
    ax.set_ylim(-1.55, 1.6)
    ax.set_aspect("equal")
    ax.set_xlabel("$d$-axis (phase)")
    ax.set_ylabel("$q$-axis (phase)")
    ax.grid(True, alpha=0.25)
    ax.text(0, 1.36, r"spin-$\frac{1}{2}$ = the $(2,3)$ phase-space winding",
            ha="center", fontsize=10.5, color="#6a3d9a", fontweight="bold")
    ax.text(0, -1.46, "2 $d$-windings $\\times$ 3 $q$-windings — the EXTENDED loop,\n"
                      "closing only after the 720° double traversal",
            ha="center", va="top", fontsize=9.0, color="#6a3d9a")
    # real-space unknot inset (a plain loop — no knot)
    iax = ax.inset_axes([0.66, 0.66, 0.32, 0.32])
    ang = np.linspace(0, 2 * math.pi, 200)
    iax.plot(np.cos(ang), np.sin(ang), color="0.35", lw=1.8)
    iax.set_xlim(-1.4, 1.4)
    iax.set_ylim(-1.4, 1.4)
    iax.set_aspect("equal")
    iax.set_xticks([])
    iax.set_yticks([])
    iax.set_title("real space:\n$0_1$ unknot (no knot)", fontsize=7.5, pad=2)
    ax.set_title("(C)  The half lives in phase space, not the bead", fontsize=11.5, pad=8)


if __name__ == "__main__":
    fig, axes = plt.subplots(1, 3, figsize=(20, 7))
    panel_a(axes[0])
    panel_b(axes[1])
    panel_c(axes[2])
    fig.suptitle(
        "The gyroscope-fabric — the substrate's inductive ($\\mu$ / L) sector "
        "(what a flat trampoline-sheet cannot depict: a spin)",
        fontsize=14, fontweight="bold", y=1.02,
    )
    plt.tight_layout()
    output_path = OUTDIR / "08_gyroscope_fabric.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"✓ {output_path}")
