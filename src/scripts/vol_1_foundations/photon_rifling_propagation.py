"""
Rifled photon propagation at c — proper visualization.

Diagnoses + fixes the prior photon_chiral_yee_render3d issues:
  1. Hard-overwrite source pinned the source plane → standing wave
  2. Sustained injection swamped the propagating wave with source-region E
  3. Fixed-threshold visualization clipped far-field rifling structure

Fix: Gaussian-windowed pulse + soft additive injection over a transverse
disk. Then visualize via per-frame normalization (each frame normalized
to its own max), so the propagating wavefront is visible at all distances.

The rifling structure (spiral phase advance k·z + m·θ) becomes visible
in the 3D scatter once the wave has propagated past the source region.

Outputs:
  - assets/photon_rifling_propagation_RH.gif (3D phase-colored scatter)
  - assets/photon_rifling_propagation_LH.gif
  - assets/photon_rifling_axis_RH.gif (3D helical streamlines)
  - assets/photon_rifling_axis_LH.gif
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

from ave.core.fdtd_3d import FDTD3DEngine
from ave.core.constants import V_YIELD


def run_pulsed_cp(handedness: str, nx=160, ny=48, nz=48, n_steps=350):
    """Soft Gaussian-windowed CP pulse, additive injection."""
    eng = FDTD3DEngine(nx, ny, nz, dx=0.01, linear_only=True,  # linear for clean propagation
                       use_pml=True, pml_layers=8)
    c = eng.c
    dt = eng.dt
    freq = 1.5e9
    omega = 2.0 * np.pi * freq
    src_x = 14
    sigma_yz = 3.5

    # Pulse parameters — short Gaussian (~5 cycles wide)
    n_cycles = 5
    period = 1.0 / freq
    t_sigma = n_cycles * period * 0.5
    t_center = 3.0 * t_sigma  # pulse centered at 3σ; trails off well before halfway

    amp_E = 0.05 * V_YIELD / eng.dx  # 5% of yield voltage per cell

    # Disk profile
    cy, cz = ny // 2, nz // 2
    j, k = np.indices((ny, nz), dtype=float)
    r2 = (j - cy) ** 2 + (k - cz) ** 2
    profile = np.exp(-r2 / (2.0 * sigma_yz ** 2))
    sign = +1.0 if handedness == "RH" else -1.0

    frames = []
    for step in range(1, n_steps + 1):
        t = step * dt
        env = np.exp(-((t - t_center) / t_sigma) ** 2)
        if env > 1e-6:
            Ey_inj = env * amp_E * np.sin(omega * t)
            Ez_inj = env * amp_E * sign * np.cos(omega * t)
            # Soft additive injection
            eng.Ey[src_x, :, :] += Ey_inj * profile
            eng.Ez[src_x, :, :] += Ez_inj * profile
        eng.step()
        if step % 6 == 0:
            frames.append({
                "t": t,
                "step": step,
                "Ey": np.array(eng.Ey),
                "Ez": np.array(eng.Ez),
                "wavefront_x": src_x + eng.c * t / eng.dx,
            })

    print(f"  {handedness}: dt={dt:.3e} s, expected wavefront at step {n_steps}: x = {src_x + eng.c*n_steps*dt/eng.dx:.1f}")
    return {
        "handedness": handedness,
        "nx": nx, "ny": ny, "nz": nz, "src_x": src_x,
        "frames": frames,
        "lambda_cells": (c / freq) / eng.dx,
        "c": c, "dt": dt,
    }


def render_rifling_scatter(result, out_gif):
    """3D scatter with PER-FRAME normalization showing rifling spiral."""
    nx, ny, nz = result["nx"], result["ny"], result["nz"]
    src_x = result["src_x"]
    handedness = result["handedness"]
    frames = result["frames"]
    cy, cz = ny // 2, nz // 2

    fig = plt.figure(figsize=(13, 7), facecolor="black")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("black")

    def update(frame_idx):
        ax.cla()
        ax.set_facecolor("black")
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False

        f = frames[frame_idx]
        Ey, Ez = f["Ey"], f["Ez"]
        E_perp = np.sqrt(Ey ** 2 + Ez ** 2)
        # Per-frame normalization — wavefront amplitude varies with distance
        e_max = E_perp.max()
        if e_max < 1e-30:
            return ax,

        # Adaptive threshold: lower for later frames so far-field shows
        threshold = 0.05 * e_max

        # Phase angle = atan2(Ez, Ey), color via cos(phase) → red/blue twist
        phase = np.arctan2(Ez, Ey)
        mask = E_perp > threshold

        if mask.any():
            xs, ys, zs = np.where(mask)
            phases = phase[xs, ys, zs]
            color_vals = (np.cos(phases) + 1.0) / 2.0
            colors = cm.coolwarm(color_vals)
            sizes = 6 + 25 * (E_perp[xs, ys, zs] / e_max)
            alphas = 0.3 + 0.65 * (E_perp[xs, ys, zs] / e_max)
            # Use scatter with per-point alpha by setting facecolors with alpha channel
            colors_with_alpha = np.column_stack([colors[:, :3], alphas])
            ax.scatter(xs, ys, zs, c=colors_with_alpha, s=sizes, edgecolor="none")

        # Propagation axis indicator
        ax.plot([0, nx], [cy, cy], [cz, cz], "w:", lw=0.6, alpha=0.4)
        ax.scatter([src_x], [cy], [cz], color="cyan", s=140, alpha=0.9,
                   edgecolor="white", linewidths=1.5)
        # Expected wavefront marker
        wf = min(nx - 1, f["wavefront_x"])
        ax.scatter([wf], [cy], [cz], color="yellow", s=80, alpha=0.7,
                   edgecolor="orange", linewidths=1.0, marker="^")

        ax.set_xlabel("X (propagation, cells)", color="#cccccc", fontsize=9)
        ax.set_ylabel("Y", color="#cccccc", fontsize=9)
        ax.set_zlabel("Z", color="#cccccc", fontsize=9)
        ax.tick_params(colors="#888", labelsize=7)
        ax.set_xlim(0, nx)
        ax.set_ylim(0, ny)
        ax.set_zlim(0, nz)
        ax.set_title(
            f"Rifled Photon ({handedness}) at c — t={f['t']*1e9:.2f} ns, "
            f"step={f['step']}, λ={result['lambda_cells']:.0f} cells\n"
            f"Cyan △ = source, Yellow ▲ = wavefront at c·t  |  "
            f"Color = cos(arctan2(Ez,Ey))  |  per-frame norm",
            color="#cccccc", fontsize=10,
        )
        return ax,

    anim = FuncAnimation(fig, update, frames=len(frames), interval=70, blit=False)
    writer = PillowWriter(fps=14)
    anim.save(out_gif, writer=writer)
    plt.close(fig)


def render_axis_helix(result, out_gif):
    """3D helix of (x, Ey(x), Ez(x)) along central axis with per-frame norm."""
    nx, ny, nz = result["nx"], result["ny"], result["nz"]
    cy, cz = ny // 2, nz // 2
    src_x = result["src_x"]
    handedness = result["handedness"]
    frames = result["frames"]

    fig = plt.figure(figsize=(13, 7), facecolor="#0a0a1a")
    ax = fig.add_subplot(111, projection="3d")

    scale = 6.0

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
        E_mag = np.sqrt(Ey_axis ** 2 + Ez_axis ** 2)
        e_max = max(E_mag.max(), 1e-30)

        E_y_vis = cy + Ey_axis / e_max * scale
        E_z_vis = cz + Ez_axis / e_max * scale

        x_range = np.arange(nx)
        for i in range(nx - 1):
            c_val = E_mag[i] / e_max
            if c_val < 0.02:
                continue  # skip near-zero cells for cleaner render
            ax.plot(
                [x_range[i], x_range[i + 1]],
                [E_y_vis[i], E_y_vis[i + 1]],
                [E_z_vis[i], E_z_vis[i + 1]],
                color=cm.inferno(c_val * 0.85 + 0.1),
                lw=2.0, alpha=min(1.0, 0.4 + 0.6 * c_val),
            )

        # Source + wavefront markers
        ax.scatter([src_x], [cy], [cz], color="cyan", s=120, alpha=0.9,
                   edgecolor="white")
        wf = min(nx - 1, f["wavefront_x"])
        ax.scatter([wf], [cy], [cz], color="yellow", s=70, alpha=0.7,
                   marker="^", edgecolor="orange")

        ax.set_xlabel("X (propagation, cells)", color="#888", fontsize=9)
        ax.set_ylabel("Y (E_y / scaled)", color="#888", fontsize=9)
        ax.set_zlabel("Z (E_z / scaled)", color="#888", fontsize=9)
        ax.tick_params(colors="#444466", labelsize=7)
        ax.set_xlim(0, nx)
        ax.set_ylim(cy - scale * 1.4, cy + scale * 1.4)
        ax.set_zlim(cz - scale * 1.4, cz + scale * 1.4)
        ax.set_title(
            f"E-field Helix ({handedness}) — t={f['t']*1e9:.2f} ns, "
            f"step={f['step']}, λ={result['lambda_cells']:.0f} cells\n"
            f"Cyan = source, Yellow ▲ = wavefront at c·t  |  per-frame normalized E",
            color="#cccccc", fontsize=11,
        )
        return ax,

    anim = FuncAnimation(fig, update, frames=len(frames), interval=70, blit=False)
    writer = PillowWriter(fps=14)
    anim.save(out_gif, writer=writer)
    plt.close(fig)


def main():
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    assets_dir = repo_root / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("Rifled photon propagation at c — soft pulse + per-frame norm rendering")
    print("=" * 72)

    for hand in ("RH", "LH"):
        print(f"\n── Running {hand} (160×48×48, soft pulse, 350 steps) ──")
        result = run_pulsed_cp(hand)
        print(f"  done: {len(result['frames'])} frames captured")

        out_scatter = assets_dir / f"photon_rifling_propagation_{hand}.gif"
        out_helix = assets_dir / f"photon_rifling_axis_{hand}.gif"

        print(f"  rendering rifling scatter → {out_scatter}")
        render_rifling_scatter(result, str(out_scatter))
        print(f"  rendering axis helix → {out_helix}")
        render_axis_helix(result, str(out_helix))

    print(f"\nOutputs in {assets_dir}/")


if __name__ == "__main__":
    main()
