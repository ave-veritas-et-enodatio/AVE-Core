"""Electron (2,3) soliton — E-field & B-field DENSITY heatmaps, lab-notebook palette.

A "version like the notebook template" (avenotebook.sty earth/electric-blue/yellow):
  * real engine solve  — CosseratField3D relaxation of the (2,3) sector to the
    Golden Torus (R=phi/2, r=(phi-1)/2, R*r=1/4). NO hardcoded physics.
  * E-DOF (capacitive)  = translational displacement field  |u|  and  V = div u
  * B-DOF (inductive)   = microrotation field  |B| = |omega|
  * field energy density = engine energy_density()  (capacitive + inductive)

Outputs (this dir):
  electron_field_density.png      static 3-panel: |E|~|u|, |B|=|omega|, energy
  electron_field_relax.{mp4,gif}  the fields FORM as the soliton relaxes to ground
  electron_field_sweep.{mp4,gif}  slice-sweep through z — the 3D torus in cross-section

Run from the engine env:  python3 electron_field_density_v2.py
"""

from __future__ import annotations

import os
import time

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FFMpegWriter, FuncAnimation, PillowWriter
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

from ave.core.constants import PHI  # golden ratio (canonical)
from ave.topological.cosserat_field_3d import CosseratField3D

# ── lab-notebook palette (avenotebook.sty, dark theme) ───────────────────────────
EARTHBG = "#1E1813"
INK = "#E8E0CE"
FAINT = "#9A8F76"
RUST = "#C96B3A"
YLW = "#FFD21E"
BLUE = "#2E72FF"
HALO = "#9CC0FF"
GRID = "#4A4230"

CMAP_E = LinearSegmentedColormap.from_list(
    "E", [(0, "#140F0B"), (0.30, "#5C2E1A"), (0.55, RUST), (0.80, YLW), (1, "#FFF4CC")]
)
CMAP_B = LinearSegmentedColormap.from_list(
    "B", [(0, "#0B0F1E"), (0.38, "#1E3A78"), (0.68, BLUE), (0.88, "#8FB6FF"), (1, "#EAF2FF")]
)
CMAP_U = LinearSegmentedColormap.from_list(
    "U", [(0, "#120D0A"), (0.45, "#6B4A2A"), (0.75, "#D79A4A"), (1, "#FFE9B0")]
)

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PHI_R = PHI / 2.0          # Golden-Torus major (ell_node units)
PHI_r = (PHI - 1.0) / 2.0  # Golden-Torus minor (ell_node units)

NX = 40
R_GRID = 8.0
SCALE = R_GRID / PHI_R                       # cells per ell_node
R_INIT = SCALE * PHI_R                        # = R_GRID
r_INIT = SCALE * PHI_r                        # = R_GRID / phi^2


# ═════════════════════════════════════════════════════════════════════════════
# Engine solve — chunked relaxation, capturing the formation movie + full volume
# ═════════════════════════════════════════════════════════════════════════════
def fields_now(s):
    """Return (V=div u, |u|, |B|=|omega|, energy density) full volumes."""
    strain = np.asarray(s.compute_strain())
    divu = strain[..., 0, 0] + strain[..., 1, 1] + strain[..., 2, 2]
    uabs = np.linalg.norm(np.asarray(s.u), axis=-1)
    bmag = np.linalg.norm(np.asarray(s.omega), axis=-1)
    edens = np.asarray(s.energy_density())
    return divu, uabs, bmag, edens


def solve(chunk=20, n_chunks=55):
    t0 = time.time()
    s = CosseratField3D(NX, NX, NX, dx=1.0, use_saturation=True)
    s.initialize_electron_2_3_sector(R_target=R_INIT, r_target=r_INIT)
    c = NX // 2
    relax_V, relax_B, iters, energies = [], [], [], []

    def snap(it):
        divu, uabs, bmag, edens = fields_now(s)
        relax_V.append(np.abs(divu[:, :, c]).copy())
        relax_B.append(bmag[:, :, c].copy())
        iters.append(it)
        energies.append(float(s.total_energy()))

    snap(0)
    total = 0
    for _ in range(n_chunks):
        res = s.relax_to_ground_state(max_iter=chunk, tol=1e-9, initial_lr=1e-3, verbose=False)
        total += int(res.get("iterations", chunk))
        snap(total)
    # final full volumes
    divu, uabs, bmag, edens = fields_now(s)
    print(f"  relaxed {total} iters, E={s.total_energy():.4g}, wall={time.time()-t0:.1f}s")
    print(f"  |B|max={bmag.max():.3f}  |u|max={uabs.max():.3f}  |div u|max={np.abs(divu).max():.3f}")
    return dict(
        V=divu, U=uabs, B=bmag, E=edens, c=c,
        relax_V=np.array(relax_V), relax_B=np.array(relax_B),
        iters=np.array(iters), energies=np.array(energies), n_iters=total,
    )


# ── normalization: percentile clip so smooth structure is visible ────────────────
def pnorm(F, lo=2, hi=99.5):
    a, b = np.percentile(F, lo), np.percentile(F, hi)
    if b <= a:
        b = a + 1e-12
    return np.clip((F - a) / (b - a), 0, 1)


def overlay(ax, half, tc, lattice=True):
    if lattice:
        g = np.arange(-np.floor(half), np.floor(half) + 0.01, 1.0)
        GX, GY = np.meshgrid(g, g)
        ax.scatter(GX, GY, s=4, c="white", alpha=0.08, linewidths=0, zorder=3)
    th = np.linspace(0, 2 * np.pi, 360)
    for rad in (PHI_R + PHI_r, PHI_R - PHI_r):
        ax.plot(rad * np.cos(th), rad * np.sin(th), color=tc, lw=0.8, alpha=0.45, zorder=4)
    ax.plot(PHI_R * np.cos(th), PHI_R * np.sin(th), color="white", lw=1.0, alpha=0.6,
            ls=(0, (4, 2)), zorder=4)
    ax.set_xlim(-half, half)
    ax.set_ylim(-half, half)
    ax.set_xticks([])
    ax.set_yticks([])


def phasor_2_3(n=2400):
    """Canonical (2,3) trajectory in the bond-LC (V_inc, V_ref) phasor plane —
    the 2-D shadow of the Golden-Torus trefoil. R_phase=phi/2, r_phase=(phi-1)/2.
    This is the electron's DEFINING topology (theory.md:16): a phase-space object,
    invisible to real-space |omega| (which sees only the w1=2 toroidal projection)."""
    t = np.linspace(0.0, 2.0 * np.pi, n)
    rad = PHI_R + PHI_r * np.cos(3.0 * t)   # poloidal "3"
    vinc = rad * np.cos(2.0 * t)            # toroidal "2"
    vref = rad * np.sin(2.0 * t)
    return t / (2.0 * np.pi), vinc, vref


def draw_phasor(ax, tc):
    ph, vi, vr = phasor_2_3()
    lim = (PHI_R + PHI_r) * 1.18
    # phase-colored trajectory (glow + core)
    pts = np.array([vi, vr]).T.reshape(-1, 1, 2)
    segs = np.concatenate([pts[:-1], pts[1:]], axis=1)
    for lw, a in ((6, 0.12), (2.2, 1.0)):
        lc = LineCollection(segs, cmap="turbo", linewidths=lw, alpha=a)
        lc.set_array(ph[:-1])
        ax.add_collection(lc)
    ax.set_facecolor(EARTHBG)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axhline(0, color=GRID, lw=0.6, alpha=0.5)
    ax.axvline(0, color=GRID, lw=0.6, alpha=0.5)
    ax.text(0.5, -0.085, r"$V_{\rm inc}$", transform=ax.transAxes, ha="center",
            color=FAINT, fontsize=10)
    ax.text(-0.06, 0.5, r"$V_{\rm ref}$", transform=ax.transAxes, va="center",
            rotation=90, color=FAINT, fontsize=10)
    for sp in ax.spines.values():
        sp.set_color("#3A3320")


# ═════════════════════════════════════════════════════════════════════════════
# Static 3-panel — real-space ENVELOPE (engine) vs the PHASE-SPACE (2,3) (canonical)
# ═════════════════════════════════════════════════════════════════════════════
def render_static(D):
    half = (NX / 2) / SCALE
    ext = [-half, half, -half, half]
    c = D["c"]
    env_panels = [
        (pnorm(D["U"][:, :, c]), CMAP_E, YLW, r"ELECTRIC FIELD ENVELOPE  $|E|\sim|u|$",
         "real space · capacitive E-DOF · continuum solve"),
        (pnorm(D["B"][:, :, c]), CMAP_B, BLUE, r"MAGNETIC FIELD ENVELOPE  $|B|=|\omega|$",
         r"real space · inductive B-DOF · only the $w_1{=}2$ toroidal projection"),
    ]
    fig, axs = plt.subplots(1, 3, figsize=(20, 7.3))
    fig.patch.set_facecolor(EARTHBG)

    # — two real-space envelope panels (engine continuum solve) —
    for ax, (F, cm, tc, title, sub) in zip(axs[:2], env_panels):
        ax.set_facecolor(EARTHBG)
        ax.imshow(F.T, origin="lower", extent=ext, cmap=cm, interpolation="bilinear", zorder=1)
        overlay(ax, half, tc)
        ax.set_title(title, color=INK, fontsize=14.5, fontweight="bold", pad=10)
        ax.text(0.5, -0.052, sub, transform=ax.transAxes, ha="center", va="top",
                color=FAINT, fontsize=9.2)
        for sp in ax.spines.values():
            sp.set_color("#3A3320")
    # ℓ_node scale bar + sub-cutoff note on the E panel
    axs[0].plot([-half + 0.4, -half + 1.4], [-half + 0.45, -half + 0.45], color=INK, lw=2.4)
    axs[0].text(-half + 0.9, -half + 0.66, r"$1\,\ell_{node}$", color=INK, ha="center", fontsize=8.5)
    axs[0].text(0.015, 0.965, r"mesh $dx\approx0.1\,\ell_{node}$ (sub-cutoff)",
                transform=axs[0].transAxes, color="#7E745C", fontsize=8, va="top")

    # — phase-space panel: the DEFINING (2,3), canonical —
    draw_phasor(axs[2], YLW)
    axs[2].set_title(r"THE $(2,3)$ IN PHASE SPACE", color=INK, fontsize=14.5,
                     fontweight="bold", pad=10)
    axs[2].text(0.5, -0.052, r"$(V_{\rm inc},V_{\rm ref})$ bond-LC phasor · canonical $(2,3)$ geometry (parametric) · no validated engine extraction",
                transform=axs[2].transAxes, ha="center", va="top", color=FAINT, fontsize=8.4)

    fig.suptitle("Electron soliton — real-space field envelope  vs.  the phase-space (2,3)",
                 color=INK, fontsize=18, fontweight="bold", y=0.985)
    fig.text(0.5, 0.052,
             r"Left/center: field ENVELOPE from continuum $\mathtt{CosseratField3D}$ relaxation "
             r"($R{=}\varphi/2,\,r{=}(\varphi{-}1)/2,\,R\!\cdot\!r{=}1/4$) at $dx\approx0.1\,\ell_{node}$ — "
             r"below the $\ell_{node}{=}\hbar/m_ec$ substrate cutoff, so sub-$\ell_{node}$ detail is continuum, "
             r"not granular substrate.",
             ha="center", color=HALO, fontsize=9.6)
    fig.text(0.5, 0.022,
             r"$\mathtt{CosseratField3D}$ has only real-space $u,\omega$ — no bonds, no $(V_{\rm inc},V_{\rm ref})$ — so the $(2,3)$ is "
             r"ABSENT from it, not merely unrendered [theory.md:16]. The heatmaps are the real-space $w_1{=}2$ envelope; the right panel is "
             r"canonical $(2,3)$ geometry (parametric) — no validated engine extraction of the phasor $(2,3)$ exists.",
             ha="center", color=HALO, fontsize=9.0)
    plt.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.13, wspace=0.06)
    out = os.path.join(OUTDIR, "electron_field_density.png")
    fig.savefig(out, dpi=150, facecolor=EARTHBG)
    plt.close(fig)
    print(f"  saved {out}")


# ═════════════════════════════════════════════════════════════════════════════
# Animation 1 — the fields FORM as the soliton relaxes
# ═════════════════════════════════════════════════════════════════════════════
def render_relax(D, fps=12):
    half = (NX / 2) / SCALE
    ext = [-half, half, -half, half]
    RV, RB = D["relax_V"], D["relax_B"]
    nf = len(RV)
    # consistent normalization across frames (use final-frame percentiles)
    def fixnorm(stack, lo=2, hi=99.5):
        a, b = np.percentile(stack[-1], lo), np.percentile(stack[-1], hi)
        b = b if b > a else a + 1e-12
        return a, b
    aV, bV = fixnorm(RV)
    aB, bB = fixnorm(RB)

    fig, axs = plt.subplots(1, 2, figsize=(13.6, 7.2))
    fig.patch.set_facecolor(EARTHBG)
    ims = []
    for ax, cm, tc, title, sub in [
        (axs[0], CMAP_E, YLW, r"ELECTRIC FIELD  $V=\nabla\!\cdot u$", "capacitive E-DOF · real-space envelope"),
        (axs[1], CMAP_B, BLUE, r"MAGNETIC FIELD  $|B|=|\omega|$", r"inductive B-DOF · real-space envelope ($w_1{=}2$)"),
    ]:
        ax.set_facecolor(EARTHBG)
        im = ax.imshow(np.zeros((NX, NX)).T, origin="lower", extent=ext, cmap=cm,
                       interpolation="bilinear", vmin=0, vmax=1, zorder=1)
        overlay(ax, half, tc)
        ax.set_title(title, color=INK, fontsize=14.5, fontweight="bold", pad=9)
        ax.text(0.5, -0.045, sub, transform=ax.transAxes, ha="center", va="top",
                color=FAINT, fontsize=9)
        for sp in ax.spines.values():
            sp.set_color("#3A3320")
        ims.append(im)
    sup = fig.suptitle("", color=INK, fontsize=16, fontweight="bold", y=0.97)
    foot = fig.text(0.5, 0.03, "", ha="center", color=HALO, fontsize=10.5, family="monospace")

    def update(f):
        ims[0].set_data((np.clip((RV[f] - aV) / (bV - aV), 0, 1)).T)
        ims[1].set_data((np.clip((RB[f] - aB) / (bB - aB), 0, 1)).T)
        sup.set_text("Relaxing the soliton to the Golden-Torus envelope (real space)")
        foot.set_text(f"gradient-relaxation step {D['iters'][f]:4d}      "
                      f"energy E = {D['energies'][f]:.4g}")
        return ims

    plt.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.1, wspace=0.05)
    anim = FuncAnimation(fig, update, frames=nf, blit=False)
    _save(anim, "electron_field_relax", fps)
    plt.close(fig)


# ═════════════════════════════════════════════════════════════════════════════
# Animation 2 — slice-sweep through z (the 3D torus in cross-section)
# ═════════════════════════════════════════════════════════════════════════════
def render_sweep(D, fps=15, n_interp=3):
    half = (NX / 2) / SCALE
    ext = [-half, half, -half, half]
    U, B = D["U"], D["B"]
    aU, bU = np.percentile(U, 2), np.percentile(U, 99.5)
    aB, bB = np.percentile(B, 2), np.percentile(B, 99.5)
    pml = 4
    zlo, zhi = pml, NX - pml - 1
    zs = np.linspace(zlo, zhi, (zhi - zlo) * n_interp)

    def slz(vol, z):
        z0 = int(np.floor(z)); z1 = min(z0 + 1, NX - 1); w = z - z0
        return (1 - w) * vol[:, :, z0] + w * vol[:, :, z1]

    fig, axs = plt.subplots(1, 2, figsize=(13.6, 7.2))
    fig.patch.set_facecolor(EARTHBG)
    imE = axs[0].imshow(np.zeros((NX, NX)).T, origin="lower", extent=ext, cmap=CMAP_E,
                        interpolation="bilinear", vmin=0, vmax=1, zorder=1)
    imB = axs[1].imshow(np.zeros((NX, NX)).T, origin="lower", extent=ext, cmap=CMAP_B,
                        interpolation="bilinear", vmin=0, vmax=1, zorder=1)
    for ax, tc, title, sub in [
        (axs[0], YLW, r"ELECTRIC FIELD ENVELOPE  $|E|\sim|u|$", "real-space · capacitive E-DOF"),
        (axs[1], BLUE, r"MAGNETIC FIELD ENVELOPE  $|B|=|\omega|$", r"real-space · inductive B-DOF ($w_1{=}2$)"),
    ]:
        ax.set_facecolor(EARTHBG)
        overlay(ax, half, tc)
        ax.set_title(title, color=INK, fontsize=14.5, fontweight="bold", pad=9)
        ax.text(0.5, -0.045, sub, transform=ax.transAxes, ha="center", va="top",
                color=FAINT, fontsize=9)
        for sp in ax.spines.values():
            sp.set_color("#3A3320")
    sup = fig.suptitle("Slice-sweep through the soliton — the 3D field envelope in cross-section",
                       color=INK, fontsize=15.5, fontweight="bold", y=0.97)
    foot = fig.text(0.5, 0.03, "", ha="center", color=HALO, fontsize=10.5, family="monospace")

    def update(f):
        z = zs[f]
        imE.set_data((np.clip((slz(U, z) - aU) / (bU - aU), 0, 1)).T)
        imB.set_data((np.clip((slz(B, z) - aB) / (bB - aB), 0, 1)).T)
        depth = (z - NX / 2) / SCALE
        foot.set_text(f"slice plane  z = {depth:+5.2f} ell_node   (perpendicular to the torus axis)")
        return imE, imB

    plt.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.1, wspace=0.05)
    anim = FuncAnimation(fig, update, frames=len(zs), blit=False)
    _save(anim, "electron_field_sweep", fps)
    plt.close(fig)


def _save(anim, name, fps):
    gif = os.path.join(OUTDIR, f"{name}.gif")
    mp4 = os.path.join(OUTDIR, f"{name}.mp4")
    anim.save(gif, writer=PillowWriter(fps=fps))
    print(f"  saved {gif}")
    try:
        anim.save(mp4, writer=FFMpegWriter(fps=fps, bitrate=4200))
        print(f"  saved {mp4}")
    except Exception as e:  # noqa: BLE001
        print(f"  (mp4 skipped: {e})")


def main():
    print("=" * 70)
    print("  Electron (2,3) field-density visuals  —  engine solve")
    print("=" * 70)
    cache = "/tmp/field_density_D.npz"
    if os.environ.get("USE_CACHE") and os.path.exists(cache):
        z = np.load(cache)
        D = {k: z[k] for k in z.files}
        D["c"] = int(D["c"]); D["n_iters"] = int(D["n_iters"])
        print(f"  loaded cached solve ({cache})")
    else:
        D = solve()
        np.savez(cache, **D)
    print("  static ..."); render_static(D)
    print("  relaxation movie ..."); render_relax(D)
    print("  slice-sweep ..."); render_sweep(D)
    print("=" * 70)
    print(f"  outputs in {OUTDIR}")


if __name__ == "__main__":
    main()
