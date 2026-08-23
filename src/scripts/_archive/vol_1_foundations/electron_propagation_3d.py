#!/usr/bin/env python3
r"""
3D electron-defect packet propagation on the K4-TLM substrate.

Visualizes a localized T₂-projected wave packet traversing a 3D diamond
lattice — the substrate-native picture of a *sub-yield* electron-defect
moving through vacuum, emitting a transverse wake.

HONEST FRAMING (load-bearing)
-----------------------------
This is NOT a from-scratch emergent Γ=-1 self-trapped soliton (c_local→0
pins saturated cores per motion_stability_bemf_longitudinal_probe). It IS
real K4-TLM propagation physics for a localized defect packet below V_YIELD,
analogous to the moving-defect / wake picture in k4tlm_double_slit_dark_wake.

AVE-native setup:
  - K4Lattice3D, linear vacuum (nonlinear=False), amp < V_YIELD
  - T₂-projected injection (Σw=0) — transverse sector, not A₁ bulk mode
  - Canonical constants from ave.core.constants (comparison-only in labels)

Output: assets/sim_outputs/electron_propagation_3d.gif
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors
from matplotlib.animation import FuncAnimation, PillowWriter

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from photon_propagation import forward_port_weights  # noqa: E402

from ave.core.constants import ALPHA, C_0, V_SNAP, V_YIELD  # noqa: E402
from ave.core.k4_tlm import K4Lattice3D  # noqa: E402
from ave_path_util import sim_output  # noqa: E402


def verify_constants(amp_frac: float) -> dict:
    amp = amp_frac * float(V_SNAP)
    assert amp < float(V_YIELD), f"amp {amp} must stay < V_YIELD {V_YIELD}"
    return {
        "ALPHA": float(ALPHA),
        "V_YIELD_V": float(V_YIELD),
        "V_SNAP_V": float(V_SNAP),
        "drive_amp_V": float(amp),
        "drive_amp_over_V_YIELD": float(amp / V_YIELD),
        "axiom4_dormant": True,
    }


class MovingBlobSource:
    """Gaussian 3D blob injector with T₂ port pattern, translating along +x."""

    def __init__(
        self,
        *,
        sigma: float,
        omega: float,
        amplitude: float,
        direction: tuple[float, float, float] = (1.0, 0.0, 0.0),
        burst_center_step: int,
        burst_sigma_steps: int,
        x0: float,
        y0: float,
        z0: float,
        v_cells_per_step: float,
    ) -> None:
        self.sigma = sigma
        self.omega = omega
        self.amplitude = amplitude
        self.port_w = forward_port_weights(direction, project_T2=True)
        self.burst_center_step = burst_center_step
        self.burst_sigma_steps = burst_sigma_steps
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.v = v_cells_per_step

    def _burst_envelope(self, step: int) -> float:
        return float(
            np.exp(-0.5 * ((step - self.burst_center_step) / self.burst_sigma_steps) ** 2)
        )

    def center_at(self, step: int) -> tuple[float, float, float]:
        return (
            self.x0 + step * self.v,
            self.y0,
            self.z0,
        )

    def apply(self, lattice: K4Lattice3D, step: int) -> None:
        env_t = self._burst_envelope(step)
        if env_t < 1e-4:
            return
        t = step * lattice.dt
        osc = np.sin(self.omega * t)
        amp_t = self.amplitude * env_t * osc
        if abs(amp_t) < 1e-30:
            return

        cx, cy, cz = self.center_at(step)
        r = int(max(3, np.ceil(3.0 * self.sigma)))
        nx, ny, nz = lattice.nx, lattice.ny, lattice.nz

        for ix in range(max(0, int(cx) - r), min(nx, int(cx) + r + 1)):
            for iy in range(max(0, int(cy) - r), min(ny, int(cy) + r + 1)):
                for iz in range(max(0, int(cz) - r), min(nz, int(cz) + r + 1)):
                    if not lattice.mask_active[ix, iy, iz]:
                        continue
                    dist2 = (ix - cx) ** 2 + (iy - cy) ** 2 + (iz - cz) ** 2
                    g = np.exp(-dist2 / (2.0 * self.sigma**2))
                    inj = amp_t * g
                    for n in range(4):
                        if self.port_w[n] != 0.0:
                            lattice.V_inc[ix, iy, iz, n] += self.port_w[n] * inj


def energy_centroid(rho: np.ndarray, mask: np.ndarray) -> tuple[float, float, float]:
    vals = rho * mask
    total = float(vals.sum())
    if total <= 0.0:
        return (np.nan, np.nan, np.nan)
    ix, iy, iz = np.indices(rho.shape)
    cx = float((ix * vals).sum() / total)
    cy = float((iy * vals).sum() / total)
    cz = float((iz * vals).sum() / total)
    return cx, cy, cz


def sample_scatter_points(
    rho: np.ndarray,
    mask: np.ndarray,
    *,
    percentile: float = 92.0,
    max_points: int = 1200,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    interior = mask & (rho > 0)
    if not interior.any():
        return (
            np.array([]),
            np.array([]),
            np.array([]),
            np.array([]),
        )
    vals = rho[interior]
    thr = float(np.percentile(vals, percentile))
    sel = interior & (rho >= thr)
    xs, ys, zs = np.where(sel)
    if len(xs) > max_points:
        idx = np.linspace(0, len(xs) - 1, max_points, dtype=int)
        xs, ys, zs = xs[idx], ys[idx], zs[idx]
    cs = rho[xs, ys, zs]
    return xs.astype(float), ys.astype(float), zs.astype(float), cs


def run(
    *,
    N: int = 56,
    pml: int = 8,
    sigma_blob: float = 4.0,
    lambda_cells: float = 10.0,
    amp_frac: float = 0.05,
    burst_center_step: int = 16,
    burst_sigma_steps: int = 8,
    n_steps: int = 280,
    steps_per_frame: int = 4,
    fps: int = 12,
    out_gif: Path | None = None,
) -> dict:
    if out_gif is None:
        out_gif = sim_output("electron_propagation_3d.gif")

    meta = verify_constants(amp_frac)
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=pml)
    omega = 2.0 * np.pi * lattice.c / (lambda_cells * lattice.dx)
    # T₂ cardinal +x group speed ≈ c → ~1/√2 cells per step in this unit system.
    v_cells = lattice.c * lattice.dt / lattice.dx

    y0 = z0 = (N - 1) / 2.0
    x0 = float(pml + 6)
    src = MovingBlobSource(
        sigma=sigma_blob,
        omega=omega,
        amplitude=amp_frac * float(V_SNAP),
        burst_center_step=burst_center_step,
        burst_sigma_steps=burst_sigma_steps,
        x0=x0,
        y0=y0,
        z0=z0,
        v_cells_per_step=v_cells,
    )

    interior_mask = np.zeros((N, N, N), dtype=bool)
    interior_mask[pml : N - pml, pml : N - pml, pml : N - pml] = True
    interior_mask &= lattice.mask_active

    frames_xy: list[np.ndarray] = []
    frames_xz: list[np.ndarray] = []
    frames_yz: list[np.ndarray] = []
    scatter_frames: list[tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]] = []
    centroids: list[tuple[float, float, float]] = []
    times: list[float] = []

    iz = N // 2
    iy = N // 2
    ix_ref = N // 2

    for step in range(n_steps + 1):
        if step > 0:
            src.apply(lattice, step)
            lattice.step()
        if step % steps_per_frame != 0:
            continue

        rho = lattice.get_energy_density()
        # imshow uses [vertical, horizontal]; store (row, col) = (z or y, x or y).
        frames_xy.append(rho[:, :, iz].T.copy())  # (ny, nx)
        frames_xz.append(rho[:, iy, :].T.copy())  # (nz, nx) at y = iy
        frames_yz.append(rho[ix_ref, :, :].T.copy())  # (nz, ny) at x = ix_ref
        scatter_frames.append(sample_scatter_points(rho, interior_mask))
        centroids.append(energy_centroid(rho, interior_mask))
        times.append(lattice.timestep * lattice.dt)

    frames_xy_arr = np.stack(frames_xy)
    frames_xz_arr = np.stack(frames_xz)
    frames_yz_arr = np.stack(frames_yz)
    vmax = float(np.percentile(frames_xy_arr, 99.5))
    vmin = max(vmax * 1e-4, 1e-30)

    _render(
        frames_xy_arr,
        frames_xz_arr,
        frames_yz_arr,
        scatter_frames,
        centroids,
        times,
        dict(
            N=N,
            pml=pml,
            vmax=vmax,
            vmin=vmin,
            fps=fps,
            iz=iz,
            iy=iy,
            ix_ref=ix_ref,
            lambda_cells=lambda_cells,
            v_cells_per_step=v_cells,
            **meta,
        ),
        out_gif,
    )

    cx = np.array([c[0] for c in centroids])
    cy = np.array([c[1] for c in centroids])
    cz = np.array([c[2] for c in centroids])
    valid = np.isfinite(cx)
    summary = {
        **meta,
        "N": N,
        "pml": pml,
        "n_steps": n_steps,
        "steps_per_frame": steps_per_frame,
        "lambda_cells": lambda_cells,
        "sigma_blob": sigma_blob,
        "amp_frac_vsnap": amp_frac,
        "burst_center_step": burst_center_step,
        "v_cells_per_step": float(v_cells),
        "n_frames": len(times),
        "total_time_s": float(times[-1]) if times else 0.0,
        "centroid_x_start": float(cx[valid][0]) if valid.any() else None,
        "centroid_x_end": float(cx[valid][-1]) if valid.any() else None,
        "out_gif": str(out_gif),
    }
    return summary


def _render(
    frames_xy: np.ndarray,
    frames_xz: np.ndarray,
    frames_yz: np.ndarray,
    scatter_frames: list,
    centroids: list,
    times: list,
    cfg: dict,
    out_path: Path,
) -> None:
    N = cfg["N"]
    fig = plt.figure(figsize=(14, 10))
    fig.patch.set_facecolor("#0a0a12")
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1], width_ratios=[1, 1], hspace=0.22, wspace=0.18)

    ax_xy = fig.add_subplot(gs[0, 0])
    ax_xz = fig.add_subplot(gs[0, 1])
    ax_yz = fig.add_subplot(gs[1, 0])
    ax_3d = fig.add_subplot(gs[1, 1], projection="3d")

    slice_axes = (ax_xy, ax_xz, ax_yz)
    titles = (
        f"xy @ z={cfg['iz']}",
        f"xz @ y={cfg['iy']}",
        f"yz @ x={cfg['ix_ref']}",
    )
    slice_data = (frames_xy, frames_xz, frames_yz)
    ims = []
    for ax, title, data in zip(slice_axes, titles, slice_data):
        ax.set_facecolor("#111118")
        ax.tick_params(colors="#bbb", labelsize=7)
        for spine in ax.spines.values():
            spine.set_edgecolor("#444")
        frame0 = data[0]
        im = ax.imshow(
            frame0,
            origin="lower",
            cmap="inferno",
            norm=mcolors.LogNorm(vmin=cfg["vmin"], vmax=cfg["vmax"]),
            extent=[0, N, 0, N],
            aspect="equal",
        )
        ax.set_title(title, color="#eee", fontsize=10)
        xlab = "x" if ax is not ax_yz else "y"
        ylab = "y" if ax is ax_xy else "z"
        ax.set_xlabel(xlab, color="#aaa")
        ax.set_ylabel(ylab, color="#aaa")
        ims.append(im)

    ax_3d.set_facecolor("#111118")
    ax_3d.tick_params(colors="#bbb", labelsize=7)
    ax_3d.set_xlim(0, N)
    ax_3d.set_ylim(0, N)
    ax_3d.set_zlim(0, N)
    ax_3d.set_xlabel("x", color="#aaa")
    ax_3d.set_ylabel("y", color="#aaa")
    ax_3d.set_zlabel("z", color="#aaa")
    sc = ax_3d.scatter([], [], [], c=[], cmap="plasma", s=8, alpha=0.75)
    (trail,) = ax_3d.plot([], [], [], color="#00e5ff", lw=1.2, alpha=0.8)

    fig.suptitle(
        "AVE: 3D electron-defect packet on K4-TLM  (T₂ sub-yield, linear vacuum)",
        color="#eee",
        fontsize=13,
        y=0.98,
    )
    honesty = (
        "Localized T₂ packet — not a Γ=−1 self-trapped soliton. "
        f"amp = {cfg['drive_amp_over_V_YIELD']:.2f}×V_YIELD  |  "
        f"λ ≈ {cfg['lambda_cells']:.0f} cells"
    )
    fig.text(0.5, 0.01, honesty, ha="center", color="#888", fontsize=8)
    time_txt = fig.text(0.02, 0.94, "", color="#ffcc66", fontsize=9, family="monospace")
    cent_txt = fig.text(0.02, 0.91, "", color="#aaa", fontsize=8, family="monospace")

    trail_x: list[float] = []
    trail_y: list[float] = []
    trail_z: list[float] = []

    def update(i: int):
        ims[0].set_data(frames_xy[i])
        ims[1].set_data(frames_xz[i])
        ims[2].set_data(frames_yz[i])
        xs, ys, zs, cs = scatter_frames[i]
        if len(xs):
            sc._offsets3d = (xs, ys, zs)
            sc.set_array(cs)
            sc.set_clim(cfg["vmin"], cfg["vmax"])
        cx, cy, cz = centroids[i]
        if np.isfinite(cx):
            trail_x.append(cx)
            trail_y.append(cy)
            trail_z.append(cz)
            trail.set_data(trail_x, trail_y)
            trail.set_3d_properties(trail_z)
        t_ns = times[i] * 1e9
        time_txt.set_text(f"t = {t_ns:7.1f} ns   frame {i+1}/{len(times)}")
        if np.isfinite(cx):
            cent_txt.set_text(f"⟨x,y,z⟩ = ({cx:.1f}, {cy:.1f}, {cz:.1f})")
        return (*ims, sc, trail, time_txt, cent_txt)

    anim = FuncAnimation(fig, update, frames=len(times), interval=1000 / cfg["fps"], blit=False)
    writer = PillowWriter(fps=cfg["fps"])
    anim.save(out_path, writer=writer, dpi=110, savefig_kwargs={"facecolor": "#0a0a12"})
    plt.close(fig)


def main() -> None:
    summary = run()
    out_json = sim_output("electron_propagation_3d_results.json")
    out_json.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    print(f"\nGIF: {summary['out_gif']}")


if __name__ == "__main__":
    main()
