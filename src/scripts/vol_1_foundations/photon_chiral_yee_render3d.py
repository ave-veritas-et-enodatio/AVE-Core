"""
Path B 3D rendering — proper rifled-photon visualization.

Re-runs the photon_chiral_yee simulation but with 3D rendering that
actually shows the helical/rifled structure. Mimics parent's
visualize_photon_helicity.py + the very-early run_photon_rifling.py
(2026-02-13 commit 1aa9f87) — phase-colored stress scatter.

Three viewing modes:
  1. 3D parametric helix of E_y(x), E_z(x) along central propagation axis
     (actual FDTD output, shows the helix evolving in time)
  2. 3D scatter of cells where |E_perp| > threshold, colored by phase
     (cos(arctan2(Ez, Ey))) — shows the rifling spiral structure
  3. 2D phase-colored slice showing E rotation through transverse plane

Outputs:
  - assets/photon_chiral_yee_3d_RH.gif (helical streamlines)
  - assets/photon_chiral_yee_rifling_RH.gif (phase scatter)
  - LH variants
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (registers projection)

from ave.core.fdtd_3d import FDTD3DEngine
from ave.core.constants import V_YIELD


def run_simulation(handedness: str, nx=160, ny=48, nz=48, n_steps=300):
    """Lighter version of photon_chiral_yee.run_chiral_propagation,
    keeping FULL Ey/Ez/Hy/Hz fields for every recorded frame."""
    eng = FDTD3DEngine(nx, ny, nz, dx=0.01, linear_only=False,
                       use_pml=True, pml_layers=8)
    c = eng.c
    dt = eng.dt
    freq = 1.5e9
    omega = 2.0 * np.pi * freq
    src_x = 14
    sigma_yz = 4.0
    amp_E = 0.05 * V_YIELD / eng.dx
    R_helix = max(3, int(round((c / freq) / eng.dx / (2.0 * np.pi))))

    cy, cz = ny // 2, nz // 2
    j, k = np.indices((ny, nz), dtype=float)
    r2 = (j - cy) ** 2 + (k - cz) ** 2
    profile = np.exp(-r2 / (2.0 * sigma_yz ** 2))
    mask = (r2 <= R_helix ** 2).astype(float)

    sign = +1.0 if handedness == "RH" else -1.0

    t_ramp = 50 * dt
    frames = []
    for step in range(1, n_steps + 1):
        t = step * dt
        env = min(1.0, t / t_ramp) if t < t_ramp else 1.0
        Ey_inj = env * amp_E * np.sin(omega * t)
        Ez_inj = env * amp_E * sign * np.cos(omega * t)
        eng.Ey[src_x, :, :] = Ey_inj * profile * mask
        eng.Ez[src_x, :, :] = Ez_inj * profile * mask
        eng.step()
        if step % 6 == 0:
            frames.append({
                "t": t,
                "step": step,
                "Ey": np.array(eng.Ey),
                "Ez": np.array(eng.Ez),
                "Hy": np.array(eng.Hy),
                "Hz": np.array(eng.Hz),
            })

    return {
        "handedness": handedness,
        "nx": nx, "ny": ny, "nz": nz, "src_x": src_x,
        "frames": frames, "lambda_cells": (c / freq) / eng.dx,
    }


def render_helix_animation(result, out_gif):
    """3D parametric helix of (x, Ey(x), Ez(x)) — central axis only.
    Mimics parent's visualize_photon_helicity.py rendering style."""
    nx, ny, nz = result["nx"], result["ny"], result["nz"]
    cy, cz = ny // 2, nz // 2
    frames = result["frames"]
    src_x = result["src_x"]
    handedness = result["handedness"]

    # Find global E_max for stable scaling
    e_max = 1e-30
    for f in frames:
        m = max(np.abs(f["Ey"][:, cy, cz]).max(), np.abs(f["Ez"][:, cy, cz]).max())
        if m > e_max:
            e_max = m

    fig = plt.figure(figsize=(12, 7), facecolor="#0a0a1a")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#0a0a1a")

    x_range = np.arange(nx)
    scale = 8.0

    def update(frame_idx):
        ax.cla()
        ax.set_facecolor("#0a0a1a")
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor("#1a1a3a")
        ax.yaxis.pane.set_edgecolor("#1a1a3a")
        ax.zaxis.pane.set_edgecolor("#1a1a3a")

        f = frames[frame_idx]
        Ey_axis = f["Ey"][:, cy, cz]
        Ez_axis = f["Ez"][:, cy, cz]
        Hy_axis = f["Hy"][:, cy, cz]
        Hz_axis = f["Hz"][:, cy, cz]

        E_mag = np.sqrt(Ey_axis ** 2 + Ez_axis ** 2)
        H_mag = np.sqrt(Hy_axis ** 2 + Hz_axis ** 2)

        E_y_vis = cy + Ey_axis / e_max * scale
        E_z_vis = cz + Ez_axis / e_max * scale
        # H rotated 90° from E in physical Maxwell; show on inside of E helix
        H_y_vis = cy + Hy_axis / max(np.abs(np.array([f["Hy"][:, cy, cz] for f in frames])).max(), 1e-30) * scale * 0.5
        H_z_vis = cz + Hz_axis / max(np.abs(np.array([f["Hz"][:, cy, cz] for f in frames])).max(), 1e-30) * scale * 0.5

        # E helix — color by E_mag (inferno colormap)
        e_max_local = max(E_mag.max(), 1e-30)
        for i in range(len(x_range) - 1):
            c_val = E_mag[i] / e_max_local
            ax.plot(
                [x_range[i], x_range[i + 1]],
                [E_y_vis[i], E_y_vis[i + 1]],
                [E_z_vis[i], E_z_vis[i + 1]],
                color=cm.inferno(c_val * 0.85 + 0.1),
                lw=1.6, alpha=min(1.0, 0.3 + 0.7 * c_val),
            )

        # H helix — cyan/blue
        h_max_local = max(H_mag.max(), 1e-30)
        for i in range(len(x_range) - 1):
            c_val = H_mag[i] / h_max_local
            ax.plot(
                [x_range[i], x_range[i + 1]],
                [H_y_vis[i], H_y_vis[i + 1]],
                [H_z_vis[i], H_z_vis[i + 1]],
                color=cm.winter(c_val * 0.85 + 0.1),
                lw=1.0, alpha=min(0.8, 0.2 + 0.6 * c_val),
            )

        # Source plane marker
        ax.scatter([src_x], [cy], [cz], color="cyan", s=80, alpha=0.7, edgecolor="white")

        ax.set_xlabel("X (propagation, cells)", color="#888", fontsize=9)
        ax.set_ylabel("Y (E_y / scaled)", color="#888", fontsize=9)
        ax.set_zlabel("Z (E_z / scaled)", color="#888", fontsize=9)
        ax.tick_params(colors="#444466", labelsize=7)
        ax.set_xlim(0, nx)
        ax.set_ylim(cy - scale * 1.3, cy + scale * 1.3)
        ax.set_zlim(cz - scale * 1.3, cz + scale * 1.3)
        ax.set_title(
            f"Rifled Photon ({handedness}) — t={f['t']*1e9:.2f} ns, "
            f"step={f['step']}, λ={result['lambda_cells']:.0f} cells\n"
            f"E (red/orange) and H (cyan/blue) helical streamlines along propagation axis",
            color="#cccccc", fontsize=11,
        )
        return ax,

    anim = FuncAnimation(fig, update, frames=len(frames), interval=80, blit=False)
    writer = PillowWriter(fps=12)
    anim.save(out_gif, writer=writer)
    plt.close(fig)


def render_rifling_scatter_animation(result, out_gif, threshold_frac=0.10):
    """3D scatter of cells where |E_perp| > threshold, colored by phase
    angle atan2(Ez, Ey). Shows the spiral phase structure as colored
    points — direct analog to the original 2026-02-13 run_photon_rifling.py."""
    nx, ny, nz = result["nx"], result["ny"], result["nz"]
    src_x = result["src_x"]
    handedness = result["handedness"]
    frames = result["frames"]

    # Global E_perp_max
    e_max = 1e-30
    for f in frames:
        ep = np.sqrt(f["Ey"] ** 2 + f["Ez"] ** 2)
        m = ep.max()
        if m > e_max:
            e_max = m

    fig = plt.figure(figsize=(12, 7), facecolor="black")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("black")

    def update(frame_idx):
        ax.cla()
        ax.set_facecolor("black")
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False

        f = frames[frame_idx]
        Ey = f["Ey"]
        Ez = f["Ez"]
        E_perp = np.sqrt(Ey ** 2 + Ez ** 2)

        # Phase angle θ = atan2(Ez, Ey) ∈ [-π, π]
        # For RH: phase advances counterclockwise as t increases at fixed x
        phase = np.arctan2(Ez, Ey)

        threshold = threshold_frac * e_max
        mask = E_perp > threshold

        if not mask.any():
            ax.text2D(0.5, 0.5, "no cells above threshold yet",
                      transform=ax.transAxes, color="white", ha="center")
        else:
            xs, ys, zs = np.where(mask)
            phases = phase[xs, ys, zs]
            # Map phase to color via hue (HSV: hue from phase, fixed sat/val)
            # cos(phase) maps -1..+1 → blue..red (cool/warm)
            color_vals = (np.cos(phases) + 1.0) / 2.0  # 0..1
            colors = cm.coolwarm(color_vals)

            sizes = 18 + 30 * (E_perp[xs, ys, zs] / e_max)
            ax.scatter(xs, ys, zs, c=colors, s=sizes, alpha=0.7, edgecolor="none")

        # Propagation axis indicator
        ax.plot([0, nx], [ny // 2, ny // 2], [nz // 2, nz // 2],
                "w--", lw=0.8, alpha=0.4)
        ax.scatter([src_x], [ny // 2], [nz // 2],
                   color="cyan", s=120, alpha=0.9, edgecolor="white",
                   linewidths=1.5)

        ax.set_xlabel("X (propagation)", color="#cccccc", fontsize=9)
        ax.set_ylabel("Y", color="#cccccc", fontsize=9)
        ax.set_zlabel("Z", color="#cccccc", fontsize=9)
        ax.tick_params(colors="#888", labelsize=7)
        ax.set_xlim(0, nx)
        ax.set_ylim(0, ny)
        ax.set_zlim(0, nz)
        ax.set_title(
            f"Rifling — Photon ({handedness})  t={f['t']*1e9:.2f} ns, step={f['step']}\n"
            f"Color = cos(arctan2(Ez, Ey)) phase  →  spiral pattern reveals helicity",
            color="#cccccc", fontsize=11,
        )
        return ax,

    anim = FuncAnimation(fig, update, frames=len(frames), interval=80, blit=False)
    writer = PillowWriter(fps=12)
    anim.save(out_gif, writer=writer)
    plt.close(fig)


def main():
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    assets_dir = repo_root / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("3D rifled photon rendering — Yee FDTD with helical streamlines + phase scatter")
    print("=" * 72)

    for hand in ("RH", "LH"):
        print(f"\n── Running {hand} (160×48×48, 300 steps) ──")
        result = run_simulation(hand)
        print(f"  done: {len(result['frames'])} frames captured")

        out_helix = assets_dir / f"photon_chiral_yee_helix_{hand}.gif"
        out_rifling = assets_dir / f"photon_chiral_yee_rifling_{hand}.gif"

        print(f"  rendering helix → {out_helix}")
        render_helix_animation(result, str(out_helix))
        print(f"  rendering rifling-scatter → {out_rifling}")
        render_rifling_scatter_animation(result, str(out_rifling))

    print(f"\nOutputs in {assets_dir}/")


if __name__ == "__main__":
    main()
