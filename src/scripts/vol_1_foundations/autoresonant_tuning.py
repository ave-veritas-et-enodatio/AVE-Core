"""
Stage 4c tuning — empirical calibration of AutoresonantCWSource K_drift gain.

Per the canonical autoresonant-rupture framework (separate propulsion
engineering compendium, summarized in `manuscript/backmatter/07_universal_saturation_kernel.tex`
A-034 autoresonant-rupture row), the autoresonant mechanism tracks
the vacuum's strain-induced resonance shift via:

    ω(t) = ω_0 · max(ε, 1 - K_drift · A²_probe(t))

The gain K_drift has no analytic derivation in the corpus. This script runs
a sweep over K_drift values and scores them by (a) is the autoresonant drive
stable (no runaway frequency), (b) does the Cosserat response differ from
fixed-f CW (evidence that tracking changed something), and (c) does the dark
wake behave reasonably (amplitude evolution).

Sweep: K_drift ∈ {0.0 (fixed-f baseline), 0.1, 0.3, 0.5, 1.0, 2.0}
Config: single source (not pair creation — that's 4d), T=0.1 thermal ω, λ=7.

Outputs:
    /tmp/autoresonant_tuning.png
    /tmp/autoresonant_tuning.npz
"""
from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.topological.vacuum_engine import (
    VacuumEngine3D,
    CWSource,
    AutoresonantCWSource,
    DarkWakeObserver,
    RegimeClassifierObserver,
    TopologyObserver,
)


def run_one(K_drift: float, N: int = 32, n_steps: int = 150,
            lambda_cells: float = 7.0, amplitude: float = 0.5,
            temperature: float = 0.1) -> dict:
    """Single config: one autoresonant CW source at (x=8, +x̂)."""
    engine = VacuumEngine3D.from_args(
        N=N, pml=5, temperature=temperature,
        amplitude_convention="V_SNAP",
    )
    omega_0 = 2.0 * np.pi * engine.k4.c / (lambda_cells * engine.k4.dx)
    t_ramp = 5 * (2.0 * np.pi / omega_0)   # 5 periods ramp
    t_sustain = 15 * (2.0 * np.pi / omega_0)

    if K_drift <= 0.0:
        # Fixed-f baseline — use regular CWSource
        src = CWSource(
            x0=8, direction=(1.0, 0.0, 0.0),
            amplitude=amplitude, omega=omega_0,
            sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        )
    else:
        src = AutoresonantCWSource(
            x0=8, direction=(1.0, 0.0, 0.0),
            amplitude=amplitude, omega=omega_0,
            sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
            K_drift=K_drift,
        )
    engine.add_source(src)

    regime_obs = RegimeClassifierObserver(cadence=3)
    wake_obs = DarkWakeObserver(cadence=3, propagation_axis=0)
    topo_obs = TopologyObserver(cadence=5, threshold_frac=0.6)
    engine.add_observer(regime_obs)
    engine.add_observer(wake_obs)
    engine.add_observer(topo_obs)

    engine.run(n_steps=n_steps)

    max_A2_tot = max(h["max_A2_total"] for h in regime_obs.history)
    max_A2_cos = max(h["max_A2_cos"] for h in regime_obs.history)
    max_A2_k4 = max(h["max_A2_k4"] for h in regime_obs.history)
    max_tau = max(h["max_tau_zx"] for h in wake_obs.history)
    max_cent = max(h["n_centroids"] for h in topo_obs.history)

    # ω-drift stability: did ω_current stay bounded?
    if isinstance(src, AutoresonantCWSource):
        omega_history = np.array(src._omega_history)
        omega_min = float(omega_history.min())
        omega_max = float(omega_history.max())
        omega_final_shift = omega_history[-1] / omega_0 - 1.0
        probe_A_sq_history = np.array(src._probe_A_sq_history)
    else:
        omega_history = np.array([omega_0] * n_steps)
        omega_min = omega_0
        omega_max = omega_0
        omega_final_shift = 0.0
        probe_A_sq_history = np.zeros(n_steps)

    return {
        "K_drift": K_drift,
        "omega_0": omega_0,
        "omega_history": omega_history,
        "probe_A_sq_history": probe_A_sq_history,
        "omega_min": omega_min,
        "omega_max": omega_max,
        "omega_final_shift": omega_final_shift,
        "max_A2_tot": max_A2_tot,
        "max_A2_cos": max_A2_cos,
        "max_A2_k4": max_A2_k4,
        "max_tau_zx": max_tau,
        "max_centroids": int(max_cent),
        "n_steps": n_steps,
        "regime_hist": regime_obs.history,
        "wake_hist": wake_obs.history,
    }


def run_sweep() -> list[dict]:
    K_drifts = [0.0, 0.1, 0.3, 0.5, 1.0, 2.0]
    results = []
    print(f"{'K_drift':>8}  {'stable':>7}  {'ω_min/ω_0':>10}  {'max A²_k4':>10}  "
          f"{'max A²_cos':>11}  {'max τ_zx':>10}  {'#cent':>5}")
    for K in K_drifts:
        r = run_one(K)
        stable = (r["omega_min"] > 0) and (r["omega_max"] < 3 * r["omega_0"])
        print(f"{K:>8.2f}  {'YES' if stable else 'NO':>7}  "
              f"{r['omega_min']/r['omega_0']:>10.3f}  "
              f"{r['max_A2_k4']:>10.3f}  {r['max_A2_cos']:>11.3f}  "
              f"{r['max_tau_zx']:>10.3e}  {r['max_centroids']:>5d}")
        r["stable"] = stable
        results.append(r)
    return results


def render(results: list[dict], out: str) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # Panel 1: ω(t) for each K_drift
    ax = axes[0, 0]
    for r in results:
        if r["K_drift"] > 0:
            ax.plot(r["omega_history"] / r["omega_0"], lw=1.2,
                    label=f"K_drift={r['K_drift']}")
    ax.axhline(1.0, color="k", ls="--", lw=0.8, alpha=0.6)
    ax.set_xlabel("step")
    ax.set_ylabel("ω / ω_0")
    ax.set_title("Autoresonant frequency tracking")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 2: probe A² for each K_drift
    ax = axes[0, 1]
    for r in results:
        ax.plot(r["probe_A_sq_history"], lw=1.2, label=f"K={r['K_drift']}")
    ax.set_xlabel("step")
    ax.set_ylabel("A²_probe (at probe plane)")
    ax.set_yscale("symlog", linthresh=1e-6)
    ax.set_title("Probe strain history")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 3: max_A²_total across K_drifts
    ax = axes[1, 0]
    K_list = [r["K_drift"] for r in results]
    ax.plot(K_list, [r["max_A2_k4"] for r in results], "o-", label="max A²_K4")
    ax.plot(K_list, [r["max_A2_cos"] for r in results], "o-", label="max A²_cos")
    ax.plot(K_list, [r["max_A2_tot"] for r in results], "o-", label="max A²_total")
    ax.set_xlabel("K_drift")
    ax.set_ylabel("peak A²")
    ax.set_title("Saturation response vs gain")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 4: max τ_zx across K_drifts
    ax = axes[1, 1]
    ax.plot(K_list, [r["max_tau_zx"] for r in results], "o-", lw=1.4, color="#c33")
    ax.set_xlabel("K_drift")
    ax.set_ylabel("max |τ_zx|")
    ax.set_title("Dark wake amplitude vs gain")
    ax.grid(alpha=0.3)

    plt.suptitle("Stage 4c: AutoresonantCWSource K_drift tuning", fontsize=12)
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


if __name__ == "__main__":
    import json
    print("── Stage 4c: AutoresonantCWSource K_drift tuning ──\n")
    results = run_sweep()
    render(results, out="/tmp/autoresonant_tuning.png")

    # Save raw summary
    summary = [
        {
            "K_drift": r["K_drift"],
            "stable": r["stable"],
            "omega_min_over_omega_0": r["omega_min"] / r["omega_0"],
            "omega_final_shift": r["omega_final_shift"],
            "max_A2_k4": r["max_A2_k4"],
            "max_A2_cos": r["max_A2_cos"],
            "max_A2_tot": r["max_A2_tot"],
            "max_tau_zx": r["max_tau_zx"],
            "max_centroids": r["max_centroids"],
        } for r in results
    ]
    print("\n── Summary ──")
    print(json.dumps(summary, indent=2))
