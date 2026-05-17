"""Photon propagation at saturation cusp — does substrate produce confined packet?

Companion to `photon_propagation.py` (Phase A linear vacuum baseline,
amp = 0.01·V_SNAP, Mode I propagation).

This script tests the corpus claim per
[Vol 2 Ch 1:160](../../manuscript/vol_2_subatomic/chapters/01_topological_matter.tex#L160) +
[doc 103 §3.2 + §4.2](../../research/_archive/L3_electron_soliton/103_substrate_perspective_electron.md):
when amplitude crosses the Op14 saturation cusp at √(2α) ≈ 0.35, the substrate's local
impedance Z_eff = Z_0/√S spikes, ∇Z_eff at the boundary creates a TIR wall, and the
field traps itself via self-formed cavity.

Pre-registered binary criteria:
  C1: Energy retention >> linear-vacuum baseline
      (linear: PML absorbs ~half over 17 periods; trap should retain ≥80%)
  C2: Spatial localization stable
      (linear: packet broadens as Gaussian + cardinal-axis dispersion;
       trap: width should stay finite, not broaden monotonically)
  C3: Centroid displacement < linear-baseline propagation distance
      (linear: centroid moves √2·c·t; trap: centroid stays near source)
  C4: Op14 saturation actually engages
      (max A²_local should reach ≥ √(2α) cusp at peak amplitude)

Configuration:
  N=96, pml=8, source_x=16 (same as baseline)
  amp_frac = 0.35 (cusp engagement) — vs baseline 0.01
  nonlinear = True (Axiom 4 ON) — vs baseline False
  240 steps (same as baseline, comparable timescale)

Visualization: animated GIF + 3D-style multi-slice diagnostic.

Per Rule 14 substrate-derives + Rule 11 clean-falsification:
  - If the substrate produces a confined packet → corpus claim about
    impedance-induced confinement empirically supported at K4 substrate scale
  - If the substrate disperses (same as baseline) → Op14 saturation alone
    is insufficient for topological confinement; the corpus claim's
    photon-helical-confinement → electron-formation chain has missing physics
  - Either result is informative; pre-registered criteria adjudicate
"""
from __future__ import annotations

import sys
from pathlib import Path
import json
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import C_0, V_SNAP, ALPHA
from photon_propagation import PlaneSource, xy_slice, packet_centroid_interior


def run_saturation_test(
    N: int = 96,
    pml: int = 8,
    lambda_cells: float = 10.0,
    sigma_yz: float = 8.0,
    t_sigma_periods: float = 0.75,
    amp_frac: float = 0.35,           # cusp: ~√(2α) ≈ 0.349
    source_x: int = 16,
    n_steps: int = 240,
    steps_per_frame: int = 3,
    out_gif: str = "/tmp/photon_propagation_saturated.gif",
    out_npz: str = "/tmp/photon_propagation_saturated.npz",
) -> dict:
    """Photon launched at saturation-cusp amplitude on nonlinear K4-TLM."""
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=True, pml_thickness=pml)
    dt = lattice.dt
    c = float(C_0)
    omega = 2.0 * np.pi * c / (lambda_cells * 1.0)
    period = 2.0 * np.pi / omega
    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma
    amp_volts = amp_frac * float(V_SNAP)

    # Saturation cusp threshold: A²_op14 = √(2α) per A47 v2 + doc 103 §4.6
    cusp_A2 = float(np.sqrt(2.0 * ALPHA))

    src = PlaneSource(
        x0=source_x, y_c=(N - 1) / 2.0, z_c=(N - 1) / 2.0,
        direction=(1.0, 0.0, 0.0), sigma_yz=sigma_yz,
        omega=omega, t_center=t_center, t_sigma=t_sigma,
        amplitude=amp_volts,
    )

    z_slice = N // 2
    frames: list[np.ndarray] = [xy_slice(lattice, z_slice).copy()]
    centroids: list[tuple[float, float]] = [packet_centroid_interior(lattice, source_x + 4, N - pml)]
    times: list[float] = [0.0]
    a2_max_history: list[float] = [0.0]

    for step in range(1, n_steps + 1):
        t_pre = step * dt
        src.apply(lattice, t_pre)
        lattice.step()

        # Track A² = |V_inc|²/V_SNAP² peak — does saturation engage?
        a2_local = np.sum(lattice.V_inc ** 2, axis=-1) / float(V_SNAP) ** 2
        a2_max_step = float(a2_local.max())

        if step % steps_per_frame == 0:
            frames.append(xy_slice(lattice, z_slice).copy())
            centroids.append(packet_centroid_interior(lattice, source_x + 4, N - pml))
            times.append(lattice.timestep * dt)
            a2_max_history.append(a2_max_step)

    frames_arr = np.stack(frames, axis=0)
    centroids_arr = np.asarray(centroids)
    times_arr = np.asarray(times)
    a2_max_arr = np.asarray(a2_max_history)

    # Energy retention: total energy at the end vs at peak (after source pulse)
    # After source ends (~t_center + 3·t_sigma), trapped state should hold energy
    source_end_step = int((t_center + 3 * t_sigma) / dt)
    source_end_frame = source_end_step // steps_per_frame
    if source_end_frame < len(frames_arr) - 1:
        # Peak energy in interior, post-source
        interior = (slice(pml, N - pml), slice(pml, N - pml))
        E_post_source = float(frames_arr[source_end_frame, interior[0], interior[1]].sum())
        E_final = float(frames_arr[-1, interior[0], interior[1]].sum())
        retention = E_final / max(E_post_source, 1e-30)
    else:
        retention = 0.0

    # Centroid displacement: how far did the packet center travel?
    # Source plane at x=16; baseline at √2·c·t_total ≈ √2·c·5.66e-7 ≈ 240 m → ~80 cells
    valid_centroids = centroids_arr[~np.isnan(centroids_arr).any(axis=1)]
    if len(valid_centroids) > 0:
        x_centroid_final = float(valid_centroids[-1, 0])
        x_centroid_displacement = x_centroid_final - source_x
    else:
        x_centroid_final = float("nan")
        x_centroid_displacement = float("nan")

    # Spatial localization: σ of the energy density along x-axis at final frame
    # Compare to t=0 IC σ (Gaussian σ_yz = 8 cells)
    final_frame = frames_arr[-1]
    x_marg = final_frame.sum(axis=1)  # marginal over y
    if x_marg.sum() > 0:
        x_grid = np.arange(N)
        x_mean = (x_marg * x_grid).sum() / x_marg.sum()
        x_var = (x_marg * (x_grid - x_mean) ** 2).sum() / x_marg.sum()
        x_sigma_final = float(np.sqrt(x_var))
    else:
        x_sigma_final = float("nan")

    # Pre-registered binary criteria evaluation
    C1_pass = retention >= 0.80  # ≥80% retention indicates trap, vs ~50% baseline
    C2_pass = x_sigma_final < 25.0  # initial σ_yz=8; baseline broadens to ~30+ cells; trap stays <25
    C3_pass = abs(x_centroid_displacement) < 30.0  # baseline travels ~60 cells; trap stays near source
    C4_pass = a2_max_arr.max() >= cusp_A2  # saturation cusp actually engaged

    summary = {
        "N": N, "pml": pml, "source_x": source_x,
        "amp_frac_vsnap": amp_frac,
        "amp_volts": amp_volts,
        "cusp_A2": cusp_A2,
        "lambda_cells": lambda_cells,
        "n_steps": n_steps,
        "total_time_s": float(times_arr[-1]),
        "a2_max_peak": float(a2_max_arr.max()),
        "a2_max_at_source_end": float(a2_max_arr[source_end_frame] if source_end_frame < len(a2_max_arr) else 0.0),
        "energy_retention_post_source": retention,
        "x_centroid_final": x_centroid_final,
        "x_centroid_displacement": x_centroid_displacement,
        "x_sigma_final": x_sigma_final,
        "C1_pass": bool(C1_pass), "C2_pass": bool(C2_pass),
        "C3_pass": bool(C3_pass), "C4_pass": bool(C4_pass),
        "all_criteria_pass": bool(C1_pass and C2_pass and C3_pass and C4_pass),
    }

    np.savez(
        out_npz,
        frames=frames_arr,
        centroids=centroids_arr,
        times=times_arr,
        a2_max_history=a2_max_arr,
        **{k: v for k, v in summary.items() if not isinstance(v, bool)},
    )

    _render_gif(frames_arr, centroids_arr, times_arr, a2_max_arr, summary, out_gif)
    return summary


def _render_gif(frames, centroids, times, a2_max, summary, out_path):
    """Three-panel animation: |V|² xy-slice + centroid x(t) + A²_max(t) saturation tracking."""
    fig, (ax_im, ax_tr, ax_sat) = plt.subplots(
        1, 3, figsize=(18, 5),
        gridspec_kw={"width_ratios": [1.4, 1, 1]}
    )

    vmax = max(frames.max(), 1e-30)
    vmin = max(vmax * 1e-4, 1e-30)
    im = ax_im.imshow(
        frames[0].T, origin="lower", cmap="inferno",
        norm=matplotlib.colors.LogNorm(vmin=vmin, vmax=vmax),
    )
    ax_im.set_xlabel("x (lattice cells)")
    ax_im.set_ylabel("y (lattice cells)")
    ax_im.axvline(summary["source_x"], color="cyan", lw=0.8, alpha=0.5, linestyle="--")
    title_im = ax_im.set_title(f"|V|² (z=N/2)  amp_frac = {summary['amp_frac_vsnap']:.2f} (cusp={summary['cusp_A2']:.3f})")
    plt.colorbar(im, ax=ax_im, fraction=0.046, pad=0.04, label="|V|²")

    ax_tr.set_xlim(times.min(), times.max())
    ax_tr.set_ylim(0, summary["N"])
    ax_tr.set_xlabel("t (s)")
    ax_tr.set_ylabel("centroid x (cells)")
    ax_tr.axhline(summary["source_x"], color="cyan", lw=0.6, alpha=0.5, linestyle="--", label="source")
    line_tr, = ax_tr.plot([], [], color="orange", lw=1.5)
    ax_tr.set_title("Interior centroid x(t)")
    ax_tr.legend(loc="upper left", fontsize=8)

    ax_sat.set_xlim(times.min(), times.max())
    ax_sat.set_ylim(0, max(a2_max.max() * 1.2, summary["cusp_A2"] * 1.2))
    ax_sat.set_xlabel("t (s)")
    ax_sat.set_ylabel("max A²_local")
    ax_sat.axhline(summary["cusp_A2"], color="red", lw=0.8, linestyle="--", label=f"cusp √(2α)={summary['cusp_A2']:.3f}")
    line_sat, = ax_sat.plot([], [], color="purple", lw=1.5)
    ax_sat.set_title("Saturation engagement")
    ax_sat.legend(loc="upper right", fontsize=8)

    def init():
        im.set_data(frames[0].T)
        line_tr.set_data([], [])
        line_sat.set_data([], [])
        return im, line_tr, line_sat

    def update(i):
        im.set_data(frames[i].T)
        x_to_i = times[: i + 1]
        c_to_i = centroids[: i + 1, 0]
        valid = ~np.isnan(c_to_i)
        line_tr.set_data(x_to_i[valid], c_to_i[valid])
        line_sat.set_data(x_to_i, a2_max[: i + 1])
        title_im.set_text(f"|V|² (z=N/2)  t={times[i]*1e9:.1f}ns  amp_frac={summary['amp_frac_vsnap']:.2f}")
        return im, line_tr, line_sat, title_im

    anim = FuncAnimation(fig, update, frames=len(frames), init_func=init, blit=False, interval=100)
    anim.save(out_path, writer=PillowWriter(fps=12), dpi=96)
    plt.close(fig)


if __name__ == "__main__":
    print("─" * 78)
    print("  Saturation-engaged photon propagation — does substrate trap the packet?")
    print(f"  amp_frac = √(2α) cusp engagement, nonlinear=True")
    print("─" * 78)

    summary = run_saturation_test(
        out_gif="/Users/grantlindblom/AVE-staging/AVE-Core/research/_archive/L3_electron_soliton/assets/photon_propagation_saturated.gif",
        out_npz="/Users/grantlindblom/AVE-staging/AVE-Core/research/_archive/L3_electron_soliton/assets/photon_propagation_saturated.npz",
    )
    print(json.dumps(summary, indent=2))
    print("\nPre-registered binary criteria:")
    print(f"  C1 (retention ≥ 0.80):       {'✓' if summary['C1_pass'] else '✗'}  ({summary['energy_retention_post_source']:.3f})")
    print(f"  C2 (σ_x < 25 cells):         {'✓' if summary['C2_pass'] else '✗'}  ({summary['x_sigma_final']:.2f})")
    print(f"  C3 (|displacement| < 30):    {'✓' if summary['C3_pass'] else '✗'}  ({summary['x_centroid_displacement']:.2f})")
    print(f"  C4 (saturation cusp engages): {'✓' if summary['C4_pass'] else '✗'}  (max A²={summary['a2_max_peak']:.4f}, cusp={summary['cusp_A2']:.3f})")
    print(f"  ALL PASS: {'✓ TOPOLOGICAL TRAP DETECTED' if summary['all_criteria_pass'] else '✗ no trap; substrate disperses like baseline'}")
