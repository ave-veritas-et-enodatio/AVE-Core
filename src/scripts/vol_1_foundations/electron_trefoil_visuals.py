"""
Electron soliton (2,3) trefoil — premium static hero + animation.

Renders the AVE electron as the (2,3) torus knot at Golden-Torus ropelength
(R = phi/2, r = (phi-1)/2) living ON the Clifford torus T^2, with the geometric
Q-factor decomposition

    alpha^-1_ideal = Lambda_vol + Lambda_surf + Lambda_line = 4*pi^3 + pi^2 + pi
                   ~= 137.0363

shown as a legible stacked bar, and the CMB-strain correction down to the
observed CODATA value.

HONESTY (Class-B, see manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md):
  The (2,3) trefoil TOPOLOGY of the electron is canonical (theory.md:16 — the
  trefoil lives in the bond-pair LC tank's (V_inc,V_ref) phasor trajectory).
  The alpha NUMBER, however, rests on the screening identification R*r = 1/4,
  which the substrate does NOT independently select (honest-alpha relabel,
  2026-06-02; ropelength-alone lands at alpha^-1 ~= 5.87). So this figure shows
  the GEOMETRIC Q-FACTOR OF THE GOLDEN-TORUS MODEL given R*r = 1/4 — it is NOT a
  zero-parameter derivation of alpha. Captions say exactly that.

Outputs (assets/sim_outputs/electron_trefoil/):
  electron_trefoil_hero.png      static hero (tube knot on golden torus + alpha bar)
  electron_trefoil_draw.gif/.mp4 the (2,3) phasor draws the knot, camera orbits
  electron_trefoil_spin.gif/.mp4 turntable of the finished tube

Run:  python3 src/scripts/vol_1_foundations/electron_trefoil_visuals.py
"""

from __future__ import annotations

import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FFMpegWriter, FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# ── Canonical constants (NEVER hard-code: ave-canonical-source discipline) ───────
from ave.core.constants import (
    ALPHA,
    ALPHA_COLD_INV,
    DELTA_STRAIN,
    PHI,
    R_GOLDEN_TORUS,
    R_GOLDEN_TORUS_MINOR,
    RR_GOLDEN_TORUS,
)

R_GT = R_GOLDEN_TORUS  # major radius = phi/2
r_gt = R_GOLDEN_TORUS_MINOR  # minor radius = (phi-1)/2

# Palette
BG = "#0a0e14"
ACCENT = "#00ffcc"
BLUE = "#58a6ff"
TORUS_C = "#1f6f78"
SEG_COLORS = ["#ff8c42", "#ffd166", "#8ecae6"]  # vol / surf / line

OUTDIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),
    "assets",
    "sim_outputs",
    "electron_trefoil",
)


# ═════════════════════════════════════════════════════════════════════════════
# Geometry
# ═════════════════════════════════════════════════════════════════════════════
def trefoil_centerline(n: int = 1000):
    """(2,3) torus knot on the Golden Torus. Returns P (n,3), phase t, strain."""
    t = np.linspace(0.0, 2.0 * np.pi, n)
    u = 2.0 * t  # toroidal winding "2"
    v = 3.0 * t  # poloidal winding "3"
    x = (R_GT + r_gt * np.cos(v)) * np.cos(u)
    y = (R_GT + r_gt * np.cos(v)) * np.sin(u)
    z = r_gt * np.sin(v)
    P = np.column_stack([x, y, z])
    # local bending strain (curvature magnitude), normalized — the "energy density"
    d1 = np.gradient(P, axis=0)
    d2 = np.gradient(d1, axis=0)
    strain = np.linalg.norm(d2, axis=1)
    strain /= strain.max()
    return P, t, strain


def rmf_frames(P):
    """Rotation-minimizing (Bishop) frame along a closed curve. Returns N1, N2 (n,3)."""
    n = len(P)
    T = np.gradient(P, axis=0)
    T /= np.linalg.norm(T, axis=1, keepdims=True)
    N1 = np.zeros_like(P)
    # seed normal: any vector not parallel to T[0]
    seed = np.array([0.0, 0.0, 1.0])
    if abs(np.dot(seed, T[0])) > 0.9:
        seed = np.array([0.0, 1.0, 0.0])
    n0 = seed - np.dot(seed, T[0]) * T[0]
    N1[0] = n0 / np.linalg.norm(n0)
    # double-reflection RMF propagation
    for i in range(n - 1):
        v1 = P[i + 1] - P[i]
        c1 = np.dot(v1, v1)
        if c1 < 1e-18:
            N1[i + 1] = N1[i]
            continue
        rL = N1[i] - (2.0 / c1) * np.dot(v1, N1[i]) * v1
        tL = T[i] - (2.0 / c1) * np.dot(v1, T[i]) * v1
        v2 = T[i + 1] - tL
        c2 = np.dot(v2, v2)
        if c2 < 1e-18:
            N1[i + 1] = rL
        else:
            N1[i + 1] = rL - (2.0 / c2) * np.dot(v2, rL) * v2
        N1[i + 1] /= np.linalg.norm(N1[i + 1])
    N2 = np.cross(T, N1)
    N2 /= np.linalg.norm(N2, axis=1, keepdims=True)
    return N1, N2


def tube_mesh(P, N1, N2, tube_r=0.085, m=26):
    """Sweep a circle of radius tube_r along the centerline. Returns X,Y,Z (n,m)."""
    theta = np.linspace(0.0, 2.0 * np.pi, m)
    ct, st = np.cos(theta), np.sin(theta)
    ring = tube_r * (N1[:, None, :] * ct[None, :, None] + N2[:, None, :] * st[None, :, None])
    pts = P[:, None, :] + ring
    return pts[..., 0], pts[..., 1], pts[..., 2]


def torus_surface(nu=140, nv=70):
    """The Golden Torus T^2 (the Clifford torus the electron lives on)."""
    u = np.linspace(0, 2 * np.pi, nu)
    v = np.linspace(0, 2 * np.pi, nv)
    u, v = np.meshgrid(u, v)
    x = (R_GT + r_gt * np.cos(v)) * np.cos(u)
    y = (R_GT + r_gt * np.cos(v)) * np.sin(u)
    z = r_gt * np.sin(v)
    return x, y, z


def style_3d(ax):
    ax.set_facecolor(BG)
    ax.grid(False)
    lim = R_GT + r_gt + 0.06
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-0.55, 0.55)
    ax.set_box_aspect((1, 1, 0.55))
    ax.set_axis_off()  # remove panes, ticks, and the bounding-box edges entirely


# ═════════════════════════════════════════════════════════════════════════════
# Constants cross-check (ave-canonical-source: verify before plotting)
# ═════════════════════════════════════════════════════════════════════════════
def verify_constants():
    assert np.isclose(R_GT - r_gt, 0.5), "self-avoidance R - r = 1/2 violated"
    assert np.isclose(RR_GOLDEN_TORUS, 0.25), "screening R*r = 1/4 violated"
    lam_vol = 16.0 * np.pi**3 * RR_GOLDEN_TORUS
    lam_surf = 4.0 * np.pi**2 * RR_GOLDEN_TORUS
    lam_line = np.pi
    total = lam_vol + lam_surf + lam_line
    assert np.isclose(total, ALPHA_COLD_INV, rtol=1e-12), "Lambda sum != ALPHA_COLD_INV"
    assert np.isclose(total, 4 * np.pi**3 + np.pi**2 + np.pi, rtol=1e-12)
    print(f"  R = phi/2 = {R_GT:.6f}   r = (phi-1)/2 = {r_gt:.6f}   R*r = {RR_GOLDEN_TORUS:.6f}")
    print(f"  Lambda_vol  4pi^3 = {lam_vol:9.5f}")
    print(f"  Lambda_surf pi^2  = {lam_surf:9.5f}")
    print(f"  Lambda_line pi    = {lam_line:9.5f}")
    print(f"  alpha^-1_ideal    = {total:.6f}   (ALPHA_COLD_INV = {ALPHA_COLD_INV:.6f})")
    print(f"  x (1 - delta)     = {total * (1 - DELTA_STRAIN):.6f}   (CODATA = {1/ALPHA:.6f})")
    return lam_vol, lam_surf, lam_line, total


# ═════════════════════════════════════════════════════════════════════════════
# Static hero
# ═════════════════════════════════════════════════════════════════════════════
def render_hero(lam_vol, lam_surf, lam_line, total):
    P, t, strain = trefoil_centerline(900)
    N1, N2 = rmf_frames(P)
    X, Y, Z = tube_mesh(P, N1, N2, tube_r=0.085, m=28)
    tx, ty, tz = torus_surface()

    fig = plt.figure(figsize=(15, 9), dpi=170)
    fig.patch.set_facecolor(BG)
    gs = fig.add_gridspec(1, 2, width_ratios=[2.05, 1.0], wspace=0.02)

    # ── 3D knot panel ──
    ax = fig.add_subplot(gs[0, 0], projection="3d")
    style_3d(ax)
    ax.plot_surface(
        tx, ty, tz, color=TORUS_C, alpha=0.14, linewidth=0, antialiased=True,
        rcount=70, ccount=70, shade=False, zorder=1,
    )
    ax.plot_wireframe(tx, ty, tz, color="#2b7d86", alpha=0.10, linewidth=0.4,
                      rcount=18, ccount=24, zorder=2)
    cmap = plt.get_cmap("inferno")
    fc = cmap(0.18 + 0.82 * strain)[:, None, :].repeat(X.shape[1], axis=1)
    ax.plot_surface(
        X, Y, Z, facecolors=fc, rcount=X.shape[0], ccount=X.shape[1],
        linewidth=0, antialiased=True, shade=True, zorder=5,
    )
    ax.view_init(elev=24, azim=40)
    ax.text2D(0.02, 0.95, "The electron is a knot in the vacuum",
              transform=ax.transAxes, color=ACCENT, fontsize=20, weight="bold")
    ax.text2D(0.02, 0.905,
              r"$(2,3)$ torus knot  ·  Golden-Torus ropelength  $R=\varphi/2,\ r=(\varphi{-}1)/2$",
              transform=ax.transAxes, color="white", fontsize=12.5)
    ax.text2D(0.02, 0.025,
              "Curve = electron centerline (unknot in real space, carrying the "
              r"$(2,3)$ winding in the bond LC-tank $(V_{\rm inc},V_{\rm ref})$ phasor)."
              "\nSurface = the Clifford torus $T^2\\subset S^3$ it rings on.  "
              "Color = bending-strain (ropelength energy density).",
              transform=ax.transAxes, color="#9fb3c8", fontsize=9.5)

    # ── alpha decomposition panel ──
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_facecolor(BG)
    for s in ax2.spines.values():
        s.set_visible(False)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    ax2.text(0.5, 0.95, "Geometric Q-factor of the model",
             ha="center", color=ACCENT, fontsize=14.5, weight="bold")
    ax2.text(0.5, 0.905,
             r"$\alpha^{-1}_{\rm ideal}=\Lambda_{\rm vol}+\Lambda_{\rm surf}+\Lambda_{\rm line}"
             r"=4\pi^3+\pi^2+\pi$",
             ha="center", color="white", fontsize=12)

    # stacked horizontal bar (log-ish: use sqrt to keep pi visible next to 4pi^3)
    segs = [("$\\Lambda_{\\rm vol}=4\\pi^3$", lam_vol, "3-torus phase volume"),
            ("$\\Lambda_{\\rm surf}=\\pi^2$", lam_surf, "Clifford-torus surface (spin-½ half-cover)"),
            ("$\\Lambda_{\\rm line}=\\pi$", lam_line, "core magnetic moment")]
    x0, x1 = 0.07, 0.93
    bar_y, bar_h = 0.70, 0.075
    widths = np.array([s[1] for s in segs])
    fracs = widths / widths.sum()
    left = x0
    for (label, val, _desc), frac, col in zip(segs, fracs, SEG_COLORS):
        w = frac * (x1 - x0)
        ax2.add_patch(plt.Rectangle((left, bar_y), w, bar_h, color=col, ec=BG, lw=1.2))
        if frac > 0.04:
            ax2.text(left + w / 2, bar_y + bar_h / 2, f"{val:.2f}",
                     ha="center", va="center", color="#101418", fontsize=9.5, weight="bold")
        left += w
    ax2.text((x0 + x1) / 2, bar_y + bar_h + 0.035, f"= {total:.4f}",
             ha="center", color="white", fontsize=13, weight="bold")

    # legend rows
    ly = 0.575
    for (label, val, desc), col in zip(segs, SEG_COLORS):
        ax2.add_patch(plt.Rectangle((x0, ly - 0.012), 0.035, 0.028, color=col))
        ax2.text(x0 + 0.05, ly, label, color="white", fontsize=11, va="center")
        ax2.text(x0 + 0.05, ly - 0.035, desc, color="#9fb3c8", fontsize=8.3, va="center")
        ly -= 0.085

    # CMB strain correction -> CODATA
    ax2.add_patch(plt.Rectangle((x0, 0.235), x1 - x0, 0.085, color="#11161d", ec="#243040"))
    ax2.text((x0 + x1) / 2, 0.298, r"$\times\,(1-\delta_{\rm strain})$,  "
             rf"$\delta_{{\rm strain}}\approx{DELTA_STRAIN:.2e}$",
             ha="center", color=BLUE, fontsize=10)
    ax2.text((x0 + x1) / 2, 0.258,
             rf"$\alpha^{{-1}}_{{\rm obs}} = {1/ALPHA:.6f}$  (CODATA)",
             ha="center", color="white", fontsize=12.5, weight="bold")

    # honesty note
    ax2.text((x0 + x1) / 2, 0.105,
             "Canonical $(2,3)$ geometry, parametric — no validated engine extraction exists.\n"
             "Class-B identification: $R\\cdot r=1/4$ is imposed (screening),\n"
             "not substrate-selected — ropelength alone gives $\\alpha^{-1}\\!\\approx\\!5.87$.\n"
             "This is the model's geometric Q-factor, not a derivation of $\\alpha$.",
             ha="center", va="center", color="#6e7d8f", fontsize=7.6, style="italic")

    out = os.path.join(OUTDIR, "electron_trefoil_hero.png")
    fig.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print(f"  saved {out}")
    return out


# ═════════════════════════════════════════════════════════════════════════════
# Animation 1 — the (2,3) phasor draws the knot, camera orbits
# ═════════════════════════════════════════════════════════════════════════════
def render_draw(total, n_frames=150, fps=25):
    P, t, strain = trefoil_centerline(900)
    tx, ty, tz = torus_surface(nu=120, nv=60)
    cmap = plt.get_cmap("turbo")
    phase = t / (2 * np.pi)  # 0..1 along the knot

    fig = plt.figure(figsize=(11, 9), dpi=130)
    fig.patch.set_facecolor(BG)
    ax = fig.add_subplot(111, projection="3d")
    style_3d(ax)
    ax.plot_surface(tx, ty, tz, color=TORUS_C, alpha=0.09, linewidth=0,
                    antialiased=True, rcount=60, ccount=60, shade=False)

    title = ax.text2D(0.02, 0.95, "Drawing the electron",
                      transform=ax.transAxes, color=ACCENT, fontsize=18, weight="bold")
    readout = ax.text2D(0.02, 0.045, "", transform=ax.transAxes,
                        color="#9fb3c8", fontsize=10.5, family="monospace")

    init_seg = [P[0:2]]  # non-empty so add_collection3d can autoscale
    glow = Line3DCollection(init_seg, linewidths=7, alpha=0.16, zorder=4)
    core = Line3DCollection(init_seg, linewidths=2.6, alpha=1.0, zorder=6)
    ax.add_collection3d(glow)
    ax.add_collection3d(core)
    (marker,) = ax.plot([], [], [], "o", color="white", ms=9, zorder=10)
    (marker_h,) = ax.plot([], [], [], "o", color=ACCENT, ms=15, alpha=0.35, zorder=9)

    def segs_to(k):
        pts = P[: k + 1]
        if len(pts) < 2:
            return np.empty((0, 2, 3)), np.empty((0,))
        s = np.stack([pts[:-1], pts[1:]], axis=1)
        return s, phase[:k]

    def update(f):
        frac = f / (n_frames - 1)
        k = max(1, int(frac * (len(P) - 1)))
        s, ph = segs_to(k)
        core.set_segments(s)
        glow.set_segments(s)
        if len(ph):
            cols = cmap(ph)
            core.set_color(cols)
            glow.set_color(cols)
        mx, my, mz = P[k]
        marker.set_data_3d([mx], [my], [mz])
        marker_h.set_data_3d([mx], [my], [mz])
        ax.view_init(elev=22, azim=30 + 360.0 * 1.25 * frac)
        n1 = 2.0 * frac
        n2 = 3.0 * frac
        readout.set_text(
            f"toroidal winding  n1 = {n1:4.2f} / 2\n"
            f"poloidal winding  n2 = {n2:4.2f} / 3\n"
            f"arc drawn         {100*frac:5.1f} %"
        )
        if frac > 0.985:
            title.set_text("The electron is a knot in the vacuum")
            readout.set_text(
                "(2,3) torus knot complete\n"
                f"geometric Q-factor  a^-1 = {total:.3f}\n"
                "= 4pi^3 + pi^2 + pi"
            )
        return core, glow, marker, marker_h, readout, title

    anim = FuncAnimation(fig, update, frames=n_frames, blit=False)
    gif = os.path.join(OUTDIR, "electron_trefoil_draw.gif")
    mp4 = os.path.join(OUTDIR, "electron_trefoil_draw.mp4")
    anim.save(gif, writer=PillowWriter(fps=fps))
    print(f"  saved {gif}")
    try:
        anim.save(mp4, writer=FFMpegWriter(fps=fps, bitrate=4200))
        print(f"  saved {mp4}")
    except Exception as e:  # noqa: BLE001
        print(f"  (mp4 skipped: {e})")
    plt.close(fig)
    return gif


# ═════════════════════════════════════════════════════════════════════════════
# Animation 2 — turntable of the finished tube
# ═════════════════════════════════════════════════════════════════════════════
def render_spin(n_frames=120, fps=25):
    P, t, strain = trefoil_centerline(700)
    N1, N2 = rmf_frames(P)
    X, Y, Z = tube_mesh(P, N1, N2, tube_r=0.085, m=24)
    tx, ty, tz = torus_surface(nu=110, nv=55)
    cmap = plt.get_cmap("inferno")
    fc = cmap(0.18 + 0.82 * strain)[:, None, :].repeat(X.shape[1], axis=1)

    fig = plt.figure(figsize=(10, 9), dpi=130)
    fig.patch.set_facecolor(BG)
    ax = fig.add_subplot(111, projection="3d")

    def update(f):
        ax.clear()
        style_3d(ax)
        ax.plot_surface(tx, ty, tz, color=TORUS_C, alpha=0.09, linewidth=0,
                        antialiased=True, rcount=55, ccount=55, shade=False, zorder=1)
        ax.plot_surface(X, Y, Z, facecolors=fc, rcount=X.shape[0], ccount=X.shape[1],
                        linewidth=0, antialiased=True, shade=True, zorder=5)
        ax.view_init(elev=20 + 8 * np.sin(2 * np.pi * f / n_frames),
                     azim=360.0 * f / n_frames)
        ax.text2D(0.02, 0.95, "Electron soliton  (2,3) trefoil",
                  transform=ax.transAxes, color=ACCENT, fontsize=16, weight="bold")
        return ()

    anim = FuncAnimation(fig, update, frames=n_frames, blit=False)
    gif = os.path.join(OUTDIR, "electron_trefoil_spin.gif")
    mp4 = os.path.join(OUTDIR, "electron_trefoil_spin.mp4")
    anim.save(gif, writer=PillowWriter(fps=fps))
    print(f"  saved {gif}")
    try:
        anim.save(mp4, writer=FFMpegWriter(fps=fps, bitrate=4200))
        print(f"  saved {mp4}")
    except Exception as e:  # noqa: BLE001
        print(f"  (mp4 skipped: {e})")
    plt.close(fig)
    return gif


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    print("=" * 70)
    print("  Electron (2,3) trefoil — constants cross-check")
    print("=" * 70)
    lam_vol, lam_surf, lam_line, total = verify_constants()
    print("-" * 70)
    print("  rendering static hero ...")
    render_hero(lam_vol, lam_surf, lam_line, total)
    print("  rendering draw animation ...")
    render_draw(total)
    print("  rendering turntable ...")
    render_spin()
    print("=" * 70)
    print(f"  all outputs in {OUTDIR}")


if __name__ == "__main__":
    main()
