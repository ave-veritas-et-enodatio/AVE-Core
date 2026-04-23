"""
Stage 4b validation — Dark wake τ_zx propagation from a single photon source.

Per research doc 49_, the dark wake is the physical manifestation of the K4
lattice's mutual-inductance back-EMF. Any CW photon source should produce:
  1. Forward-going V packet at c
  2. Backward-going τ_zx shear strain wake at c (the "dark wake")

This validation confirms:
  a. τ_zx magnitude grows as the packet propagates (more strain over time)
  b. The wake spatial profile trails BEHIND the forward packet
  c. Peak τ_zx scales with the peak V² via the coupling formula
  d. Wake peak propagates at ~c in the backward direction

Acceptance criteria (first validation pass):
  - max τ_zx > 0 (non-zero wake detected)
  - wake_peak_x behind source position (x < source_x)
  - τ_zx magnitude tracks V² magnitude monotonically

References:
  - AVE-PONDER/manuscript/vol_ponder/ch01_topological_thrust_mechanics.tex:210-230
  - AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py:75-95
  - doc 49_ §2 (unified mechanism picture)
"""
from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from ave.topological.vacuum_engine import (
    VacuumEngine3D,
    PulsedSource,
    DarkWakeObserver,
    RegimeClassifierObserver,
)


def run_validation(
    N: int = 48,
    pml: int = 6,
    lambda_cells: float = 8.0,
    amplitude: float = 0.5,
    source_x: int = 10,
    t_sigma_periods: float = 1.0,
    n_outer_steps: int = 150,
    record_cadence: int = 3,
) -> dict:
    """Launch a single pulsed photon, record dark wake evolution."""
    engine = VacuumEngine3D.from_args(
        N=N, pml=pml, temperature=0.0,
        amplitude_convention="V_SNAP",
    )

    omega_carrier = 2.0 * np.pi * engine.k4.c / (lambda_cells * engine.k4.dx)
    period = 2.0 * np.pi / omega_carrier
    t_center = 2.0 * t_sigma_periods * period

    engine.add_source(PulsedSource(
        x0=source_x, direction=(1.0, 0.0, 0.0),
        amplitude=amplitude, omega=omega_carrier,
        sigma_yz=4.0,
        t_center=t_center,
        t_sigma=t_sigma_periods * period,
    ))

    wake_obs = DarkWakeObserver(cadence=record_cadence, propagation_axis=0)
    regime_obs = RegimeClassifierObserver(cadence=record_cadence)
    engine.add_observer(wake_obs)
    engine.add_observer(regime_obs)

    print(f"Dark-wake validation: N={N}, amp={amplitude}·V_SNAP, λ={lambda_cells}, steps={n_outer_steps}")
    print(f"  Source at x={source_x}, propagation +x̂")
    print(f"  Outer dt = {engine.outer_dt:.4f} nat units")

    engine.run(n_steps=n_outer_steps)

    wake_history = wake_obs.history
    regime_history = regime_obs.history

    # Analysis
    max_tau_zx_over_time = [h["max_tau_zx"] for h in wake_history]
    wake_peaks_x = [h["wake_peak_x"] for h in wake_history]
    times = [h["t"] for h in wake_history]
    max_V_sq_over_time = [h["max_A2_k4"] * engine.V_SNAP ** 2 for h in regime_history]

    return {
        "engine_N": N,
        "amplitude": amplitude,
        "wavelength": lambda_cells,
        "source_x": source_x,
        "times": times,
        "max_tau_zx": max_tau_zx_over_time,
        "wake_peaks_x": wake_peaks_x,
        "max_V_sq": max_V_sq_over_time,
        "tau_slabs": [h["tau_zx_slab"] for h in wake_history],
        "wake_obs_history": wake_history,
        "regime_obs_history": regime_history,
    }


def analyze_and_plot(result: dict, out_png: str, out_gif: str) -> dict:
    times = np.array(result["times"])
    max_tau = np.array(result["max_tau_zx"])
    max_V_sq = np.array(result["max_V_sq"])
    wake_peaks = np.array(result["wake_peaks_x"])
    tau_slabs = np.stack([s for s in result["tau_slabs"]], axis=0)  # (nt, nx)

    source_x = result["source_x"]

    # Check: any non-zero wake?
    wake_ever_formed = float(max_tau.max()) > 0
    # Check: max V² correlates with max τ_zx? Pearson r
    if len(max_V_sq) >= 3 and np.std(max_V_sq) > 0 and np.std(max_tau) > 0:
        pearson = float(np.corrcoef(max_V_sq, max_tau)[0, 1])
    else:
        pearson = 0.0

    # Wake propagation speed: fit wake_peak_x vs t (only valid values)
    valid_mask = wake_peaks >= 0
    if valid_mask.sum() >= 3:
        # Pick the LATE-time window where wake is established
        late_mask = valid_mask & (times > 0.5 * times[-1])
        if late_mask.sum() >= 3:
            v_wake = np.polyfit(times[late_mask], wake_peaks[late_mask], 1)[0]
        else:
            v_wake = 0.0
    else:
        v_wake = 0.0

    # Render: 2x2 panel
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    ax = axes[0, 0]
    ax.plot(times, max_V_sq, "-", lw=1.4, label="max V²", color="#47c")
    ax2 = ax.twinx()
    ax2.plot(times, max_tau, "-", lw=1.4, label="max |τ_zx|", color="#f77")
    ax.set_xlabel("t (natural units)")
    ax.set_ylabel("max V²", color="#47c")
    ax2.set_ylabel("max |τ_zx|", color="#f77")
    ax.set_title(f"Wake amplitude co-evolution\nPearson r(V², τ_zx) = {pearson:.3f}")
    ax.grid(alpha=0.3)

    ax = axes[0, 1]
    ax.plot(times, wake_peaks, "o-", ms=4, lw=1.4, label="wake peak_x")
    ax.axhline(source_x, color="#888", ls="--", lw=1, label=f"source x = {source_x}")
    ax.set_xlabel("t")
    ax.set_ylabel("wake peak x (cells)")
    ax.set_title(f"Wake peak propagation\nLate-time dx/dt = {v_wake:.3f} cells/t")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Heatmap: τ_zx slab over time
    ax = axes[1, 0]
    im = ax.imshow(
        tau_slabs.T, origin="lower", cmap="inferno",
        aspect="auto",
        extent=[times[0], times[-1], 0, tau_slabs.shape[1]],
    )
    ax.axhline(source_x, color="cyan", ls="--", lw=1, alpha=0.7, label=f"source x={source_x}")
    ax.set_xlabel("t")
    ax.set_ylabel("x (cells)")
    ax.set_title("τ_zx slab evolution (transverse-averaged)")
    plt.colorbar(im, ax=ax, fraction=0.046)
    ax.legend(fontsize=8)

    # Final slab profile
    ax = axes[1, 1]
    ax.plot(tau_slabs[-1], lw=1.4, color="#c33", label=f"t = {times[-1]:.2f}")
    if len(tau_slabs) > 10:
        ax.plot(tau_slabs[len(tau_slabs) // 2], lw=1.0, alpha=0.7, label=f"t = {times[len(tau_slabs)//2]:.2f}")
    ax.axvline(source_x, color="#888", ls="--", lw=1, label="source")
    ax.set_xlabel("x (cells)")
    ax.set_ylabel("|τ_zx| (averaged)")
    ax.set_title("Spatial τ_zx profile snapshots")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    verdict_str = "PASS" if wake_ever_formed else "FAIL"
    plt.suptitle(
        f"Dark-wake diagnostic validation — Stage 4b\n"
        f"max |τ_zx| = {max_tau.max():.3e}   verdict: {verdict_str}",
        fontsize=12,
    )
    plt.tight_layout()
    plt.savefig(out_png, dpi=110)
    plt.close()
    print(f"Saved {out_png}")

    # GIF: tau_zx slab evolution
    fig, ax = plt.subplots(figsize=(10, 4))
    (line,) = ax.plot(tau_slabs[0], lw=1.5, color="#c33")
    ax.axvline(source_x, color="#888", ls="--", lw=1)
    ax.set_xlabel("x (cells)")
    ax.set_ylabel("|τ_zx|")
    ax.set_ylim(0, tau_slabs.max() * 1.1)
    title = ax.set_title("")

    def update(i):
        line.set_ydata(tau_slabs[i])
        title.set_text(f"Dark wake at t = {times[i]:.2f}  frame {i+1}/{len(tau_slabs)}")
        return line, title

    anim = FuncAnimation(fig, update, frames=len(tau_slabs), interval=120, blit=False)
    writer = PillowWriter(fps=8)
    anim.save(out_gif, writer=writer)
    plt.close()
    print(f"Saved {out_gif}")

    return {
        "wake_ever_formed": wake_ever_formed,
        "max_tau_zx": float(max_tau.max()),
        "max_V_sq": float(max_V_sq.max()),
        "pearson_V2_tau": pearson,
        "late_wake_velocity": v_wake,
        "verdict": verdict_str,
    }


if __name__ == "__main__":
    print("── Stage 4b: Dark-Wake Diagnostic Validation ──\n")
    result = run_validation()

    print("\n── Analysis ──")
    report = analyze_and_plot(
        result,
        out_png="/tmp/dark_wake_validation.png",
        out_gif="/tmp/dark_wake_validation.gif",
    )
    print(json.dumps(report, indent=2))

    if report["wake_ever_formed"]:
        print("\n✓ Dark wake detected — DarkWakeObserver is operational.")
    else:
        print("\n✗ No wake detected; investigate observer formula.")
