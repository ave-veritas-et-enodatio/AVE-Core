"""
Phase B — polished photon-cruise animation for human-readable viewing.

Builds on the Phase A launcher infrastructure. Produces a cleaner,
longer animation showing a single T₂-pure photon packet traversing
an empty linear-vacuum lattice.

Panel layout:
  Left:  |V|² xy-slice at z = N/2 (log scale, inferno cmap)
  Right: x-marginal |V|²(x) profile (same time), showing the packet
         envelope moving rightward along x at c·√2 (K4 cardinal axis)

Timescale: ~15 ns per frame × ~40 frames ≈ 600 ns total, at 10 fps
giving a 4-second animation. Comfortable for human comprehension.

AVE fidelity (all per Axiom 1 substrate, no SM/QED imports):
  - K4Lattice3D linear mode (nonlinear=False) — Axiom 1 pure propagation
  - T₂-projected launcher (Σw_n = 0) — orthogonal to A₁ common mode
  - Amplitude ≪ V_YIELD — linear regime, no Axiom-4 engagement
  - Gaussian-modulated sinusoidal plane source — classical wave injection
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib import colors as mcolors

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import C_0, V_SNAP
from photon_propagation import PlaneSource, xy_slice


def run(
    N: int = 128,
    pml: int = 10,
    lambda_cells: float = 14.0,
    sigma_yz: float = 10.0,
    t_sigma_periods: float = 0.9,
    amp_frac: float = 0.005,
    source_x: int = 18,
    n_steps: int = 360,
    steps_per_frame: int = 4,
    fps: int = 10,
    out_gif: str = "/tmp/photon_cruise.gif",
    out_npz: str = "/tmp/photon_cruise.npz",
) -> dict:
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=pml)
    c = float(C_0)
    dx = lattice.dx
    dt = lattice.dt

    omega = 2.0 * np.pi * c / (lambda_cells * dx)
    period = 2.0 * np.pi / omega
    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma
    amp_volts = amp_frac * float(V_SNAP)

    src = PlaneSource(
        x0=source_x,
        y_c=(N - 1) / 2.0,
        z_c=(N - 1) / 2.0,
        direction=(1.0, 0.0, 0.0),
        sigma_yz=sigma_yz,
        omega=omega,
        t_center=t_center,
        t_sigma=t_sigma,
        amplitude=amp_volts,
    )

    z_slice = N // 2
    frames: list[np.ndarray] = []
    x_profiles: list[np.ndarray] = []
    times: list[float] = []
    peak_xs: list[float] = []

    # Capture t=0
    rho_xy = xy_slice(lattice, z_slice).copy()
    rho_x = lattice.get_energy_density().sum(axis=(1, 2))
    frames.append(rho_xy)
    x_profiles.append(rho_x)
    times.append(0.0)
    peak_xs.append(float(np.argmax(rho_x)) if rho_x.max() > 0 else np.nan)

    for step in range(1, n_steps + 1):
        t_pre = step * dt
        src.apply(lattice, t_pre)
        lattice.step()
        if step % steps_per_frame == 0:
            rho_xy = xy_slice(lattice, z_slice).copy()
            rho_x = lattice.get_energy_density().sum(axis=(1, 2))
            frames.append(rho_xy)
            x_profiles.append(rho_x)
            times.append(lattice.timestep * dt)
            peak_xs.append(float(np.argmax(rho_x)) if rho_x.max() > 0 else np.nan)

    frames_arr = np.stack(frames, axis=0)
    x_profiles_arr = np.stack(x_profiles, axis=0)
    times_arr = np.asarray(times)
    peak_xs_arr = np.asarray(peak_xs)

    summary = {
        "N": N, "pml": pml, "source_x": source_x,
        "lambda_cells": lambda_cells, "sigma_yz": sigma_yz,
        "t_sigma_periods": t_sigma_periods,
        "omega_rad_s": omega, "period_s": period,
        "dt_s": dt, "amp_volts": amp_volts, "amp_frac_vsnap": amp_frac,
        "n_steps": n_steps, "steps_per_frame": steps_per_frame,
        "fps": fps, "total_time_s": float(times_arr[-1]),
        "source_center_s": float(src.t_center),
        "source_end_s": float(src.t_center + 3 * src.t_sigma),
    }

    np.savez(out_npz, frames=frames_arr, x_profiles=x_profiles_arr,
             times=times_arr, peak_xs=peak_xs_arr,
             **{k: v for k, v in summary.items()})

    _render(frames_arr, x_profiles_arr, times_arr, peak_xs_arr, summary, out_gif)
    return summary


def _render(
    frames: np.ndarray,
    x_profiles: np.ndarray,
    times: np.ndarray,
    peak_xs: np.ndarray,
    summary: dict,
    out_path: str,
) -> None:
    N = summary["N"]
    source_x = summary["source_x"]
    fig, (ax_im, ax_pr) = plt.subplots(
        1, 2, figsize=(13, 5), gridspec_kw={"width_ratios": [1.3, 1]}
    )
    fig.patch.set_facecolor("#111")
    for ax in (ax_im, ax_pr):
        ax.set_facecolor("#1a1a1a")
        ax.tick_params(colors="#ccc")
        for spine in ax.spines.values():
            spine.set_edgecolor("#666")

    # Left panel: |V|² xy-slice
    vmax = max(frames.max(), 1e-30)
    vmin = max(vmax * 1e-4, 1e-30)
    im = ax_im.imshow(
        frames[0].T, origin="lower", cmap="inferno",
        norm=mcolors.LogNorm(vmin=vmin, vmax=vmax),
        extent=[0, N, 0, N],
    )
    ax_im.axvline(source_x, color="cyan", lw=0.8, alpha=0.6, linestyle="--")
    ax_im.set_xlabel("x (cells)", color="#ccc")
    ax_im.set_ylabel("y (cells)", color="#ccc")
    title_im = ax_im.set_title("|V|² on z = N/2 slice", color="#eee")
    cbar = plt.colorbar(im, ax=ax_im, fraction=0.046, pad=0.04)
    cbar.set_label("|V|²  (log)", color="#ccc")
    cbar.ax.yaxis.set_tick_params(color="#ccc")
    for lbl in cbar.ax.yaxis.get_ticklabels():
        lbl.set_color("#ccc")

    # Right panel: x-marginal profile
    x_axis = np.arange(N)
    pr_max = max(x_profiles.max(), 1e-30)
    ax_pr.set_xlim(0, N)
    ax_pr.set_ylim(pr_max * 1e-4, pr_max * 2)
    ax_pr.set_yscale("log")
    ax_pr.set_xlabel("x (cells)", color="#ccc")
    ax_pr.set_ylabel("Σ|V|² (y, z)  (log)", color="#ccc")
    ax_pr.axvline(source_x, color="cyan", lw=0.8, alpha=0.6, linestyle="--")
    ax_pr.axvspan(0, summary["pml"], color="#444", alpha=0.3)
    ax_pr.axvspan(N - summary["pml"], N, color="#444", alpha=0.3)
    (line_pr,) = ax_pr.plot(x_axis, x_profiles[0], color="#f77", lw=1.4)
    (dot_pr,) = ax_pr.plot([], [], "o", color="yellow", markersize=7)
    ax_pr.grid(alpha=0.15, color="#666")
    c_ratio_text = ax_pr.text(
        0.02, 0.95,
        f"λ = {summary['lambda_cells']:.0f} cells   pulse σ_t = "
        f"{summary['t_sigma_periods']:.1f} periods",
        transform=ax_pr.transAxes, color="#ccc", fontsize=9, va="top"
    )
    t_text = ax_pr.text(
        0.02, 0.88, "", transform=ax_pr.transAxes, color="yellow",
        fontsize=10, va="top"
    )

    src_end_ns = summary["source_end_s"] * 1e9

    def update(i):
        im.set_data(frames[i].T)
        line_pr.set_ydata(x_profiles[i])
        if np.isfinite(peak_xs[i]):
            dot_pr.set_data([peak_xs[i]], [x_profiles[i, int(peak_xs[i])]])
        t_ns = times[i] * 1e9
        src_state = "source ON" if t_ns < src_end_ns else "source off"
        title_im.set_text(f"|V|² slice    t = {t_ns:6.1f} ns    [{src_state}]")
        t_text.set_text(f"peak at x = {peak_xs[i]:.0f}" if np.isfinite(peak_xs[i]) else "")
        return im, line_pr, dot_pr, title_im, t_text

    anim = FuncAnimation(fig, update, frames=len(frames),
                         interval=1000 / summary["fps"], blit=False)
    writer = PillowWriter(fps=summary["fps"])
    anim.save(out_path, writer=writer, savefig_kwargs={"facecolor": "#111"})
    plt.close(fig)


if __name__ == "__main__":
    import json
    summary = run()
    print(json.dumps(summary, indent=2))
    print(f"\nAnimation: /tmp/photon_cruise.gif  ({summary['fps']} fps)")
    print(f"Total time:   {summary['total_time_s']*1e9:.1f} ns")
    print(f"Source OFF:   {summary['source_end_s']*1e9:.1f} ns")
