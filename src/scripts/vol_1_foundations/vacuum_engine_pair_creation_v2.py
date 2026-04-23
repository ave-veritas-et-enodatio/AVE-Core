"""
Phase III-B v2 sweep — autoresonant CW sources + dark-wake observer.

Stage 4d of plan `document-list-for-next-chat-compressed-thunder.md`.

Direct v1 follow-up with three changes:
  1. CWSource → AutoresonantCWSource (PLL q-axis tracking per doc 49_ §2)
  2. Add DarkWakeObserver to diagnostic stack (ported from AVE-Propulsion)
  3. Longer runs (300 steps) to give PLL time to track

Pre-registered outcomes (from plan Stage 4d §):

  P_IIIb-v2-pair:  2+ spatially-localized centroids at collision,
                   A²_Cosserat localized (not distributed). Dark wake
                   shows constructive interference at collision plane.
                   → FIRST NUMERICAL AVE PAIR CREATION.

  P_IIIb-v2-partial: Cosserat response visibly different from v1 (more
                     localized, distinctive dark-wake signature) but no
                     clean pair. Mechanism active but insufficient.

  P_IIIb-v2-no-change: Same distributed-plateau result as v1. Autoresonance
                       didn't change anything. Would falsify AVE-Propulsion
                       Ch 5 interpretation; point to missing mechanism.

Configuration (8 configs = 4λ × 1amp × 2T, same amp=0.5 as v1's best):
  λ ∈ {3.5, 5, 7, 10}  (ω·τ ∈ {1.80, 1.26, 0.90, 0.63})
  amp = 0.5·V_SNAP
  T ∈ {0, 0.1} (m_e c² units)
  N = 40, pml = 5, n_steps = 300
  K_drift = 0.5 (default from Stage 4c tuning)
"""
from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import json
import time
from dataclasses import dataclass

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.topological.vacuum_engine import (
    VacuumEngine3D,
    AutoresonantCWSource,
    DarkWakeObserver,
    RegimeClassifierObserver,
    TopologyObserver,
    EnergyBudgetObserver,
)


@dataclass
class RunConfigV2:
    wavelength: float
    amplitude: float
    temperature: float
    N: int = 40
    pml: int = 5
    t_ramp_periods: float = 3.0
    t_sustain_periods: float = 25.0
    n_outer_steps: int = 300
    record_cadence: int = 5
    K_drift: float = 0.5

    @property
    def omega_carrier(self) -> float:
        return 2.0 * np.pi / self.wavelength

    @property
    def omega_tau(self) -> float:
        return self.omega_carrier


def run_one_config(cfg: RunConfigV2) -> dict:
    engine = VacuumEngine3D.from_args(
        N=cfg.N, pml=cfg.pml,
        temperature=cfg.temperature,
        amplitude_convention="V_SNAP",
    )
    period = 2.0 * np.pi / cfg.omega_carrier
    t_ramp = cfg.t_ramp_periods * period
    t_sustain = cfg.t_sustain_periods * period

    source_offset = cfg.pml + 3
    # Source at x_left moving +x̂
    engine.add_source(AutoresonantCWSource(
        x0=source_offset, direction=(1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.5, t_ramp=t_ramp, t_sustain=t_sustain,
        K_drift=cfg.K_drift,
    ))
    # Source at x_right moving -x̂
    engine.add_source(AutoresonantCWSource(
        x0=cfg.N - source_offset, direction=(-1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.5, t_ramp=t_ramp, t_sustain=t_sustain,
        K_drift=cfg.K_drift,
    ))

    regime_obs = RegimeClassifierObserver(cadence=cfg.record_cadence)
    topo_obs = TopologyObserver(cadence=cfg.record_cadence, threshold_frac=0.7)
    energy_obs = EnergyBudgetObserver(cadence=cfg.record_cadence)
    wake_obs = DarkWakeObserver(cadence=cfg.record_cadence, propagation_axis=0)
    engine.add_observer(regime_obs)
    engine.add_observer(topo_obs)
    engine.add_observer(energy_obs)
    engine.add_observer(wake_obs)

    t0 = time.time()
    engine.run(n_steps=cfg.n_outer_steps)
    elapsed = time.time() - t0

    regime_hist = regime_obs.history
    topo_hist = topo_obs.history
    wake_hist = wake_obs.history

    max_A2_total = max((h["max_A2_total"] for h in regime_hist), default=0.0)
    max_A2_cos = max((h["max_A2_cos"] for h in regime_hist), default=0.0)
    max_A2_k4 = max((h["max_A2_k4"] for h in regime_hist), default=0.0)
    max_centroids = max((h["n_centroids"] for h in topo_hist), default=0)
    max_Q_hopf = max((abs(h["Q_hopf"]) for h in topo_hist), default=0.0)
    max_tau_zx = max((h["max_tau_zx"] for h in wake_hist), default=0.0)
    final_centroids = topo_hist[-1]["n_centroids"] if topo_hist else 0

    # Verdict adjudication
    if max_A2_cos >= 0.5 and max_centroids >= 2:
        verdict = "P_IIIb-v2-pair"
    elif max_A2_cos > 1e-3:
        verdict = "P_IIIb-v2-partial"
    else:
        verdict = "P_IIIb-v2-no-change"

    print(f"  λ={cfg.wavelength:>4} T={cfg.temperature:>4.2f}: "
          f"max A²_K4={max_A2_k4:.3f}  A²_cos={max_A2_cos:.3f}  "
          f"max τ_zx={max_tau_zx:.3e}  #cent={max_centroids:>2d}  "
          f"verdict={verdict}  ({elapsed:.1f}s)")

    return {
        "config": {
            "wavelength": cfg.wavelength,
            "amplitude": cfg.amplitude,
            "temperature": cfg.temperature,
            "N": cfg.N,
            "K_drift": cfg.K_drift,
            "omega_tau": cfg.omega_tau,
            "n_steps": cfg.n_outer_steps,
        },
        "elapsed_s": elapsed,
        "max_A2_total": max_A2_total,
        "max_A2_cos": max_A2_cos,
        "max_A2_k4": max_A2_k4,
        "max_centroids": int(max_centroids),
        "final_centroids": int(final_centroids),
        "max_Q_hopf": float(max_Q_hopf),
        "max_tau_zx": float(max_tau_zx),
        "verdict": verdict,
    }


def run_sweep() -> list[dict]:
    wavelengths = [3.5, 5.0, 7.0, 10.0]
    amplitudes = [0.5]
    temperatures = [0.0, 0.1]

    results = []
    total = len(wavelengths) * len(amplitudes) * len(temperatures)
    print(f"Phase III-B v2 sweep: {total} configurations "
          f"(autoresonant + dark-wake)")
    print()

    for T in temperatures:
        print(f"T = {T}:")
        for amp in amplitudes:
            for wl in wavelengths:
                cfg = RunConfigV2(wavelength=wl, amplitude=amp, temperature=T)
                r = run_one_config(cfg)
                results.append(r)
    return results


def render(results: list[dict], out: str = "/tmp/phase_iiib_v2_summary.png") -> None:
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    wls = sorted(set(r["config"]["wavelength"] for r in results))
    temps = sorted(set(r["config"]["temperature"] for r in results))

    # Panel 1: max A²_cos vs ω·τ at each T (v1 vs v2 comparison structure)
    ax = axes[0, 0]
    for T, color in zip(temps, ["#47c", "#c33"]):
        omega_taus = []
        cos_vals = []
        for wl in wls:
            for r in results:
                if (r["config"]["temperature"] == T and
                    r["config"]["wavelength"] == wl):
                    omega_taus.append(r["config"]["omega_tau"])
                    cos_vals.append(r["max_A2_cos"])
        if omega_taus:
            ax.plot(omega_taus, cos_vals, "o-", lw=1.5, color=color,
                    label=f"T = {T}")
    ax.axvline(1.0, color="#888", ls="--", lw=0.8, alpha=0.7, label="ω·τ=1")
    ax.set_xlabel("ω·τ_relax")
    ax.set_ylabel("max A²_Cosserat")
    ax.set_title("σ(ω) — v2 autoresonant")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 2: max τ_zx vs ω·τ (new in v2)
    ax = axes[0, 1]
    for T, color in zip(temps, ["#47c", "#c33"]):
        omega_taus = []
        tau_vals = []
        for wl in wls:
            for r in results:
                if (r["config"]["temperature"] == T and
                    r["config"]["wavelength"] == wl):
                    omega_taus.append(r["config"]["omega_tau"])
                    tau_vals.append(r["max_tau_zx"])
        if omega_taus:
            ax.plot(omega_taus, tau_vals, "o-", lw=1.5, color=color,
                    label=f"T = {T}")
    ax.set_xlabel("ω·τ_relax")
    ax.set_ylabel("max |τ_zx|")
    ax.set_title("Dark-wake amplitude vs frequency")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 3: Verdict matrix
    ax = axes[1, 0]
    verdict_colors = {
        "P_IIIb-v2-pair": "#2a7",
        "P_IIIb-v2-partial": "#f90",
        "P_IIIb-v2-no-change": "#c33",
    }
    for r in results:
        T_val = r["config"]["temperature"]
        wl = r["config"]["wavelength"]
        color = verdict_colors.get(r["verdict"], "gray")
        ax.scatter(r["config"]["omega_tau"], T_val + np.random.uniform(-0.005, 0.005),
                    color=color, s=180, alpha=0.8,
                    edgecolors="black", linewidths=0.8)
    ax.axvline(1.0, color="#888", ls="--", lw=0.8, alpha=0.7)
    ax.set_xlabel("ω·τ_relax")
    ax.set_ylabel("Temperature (m_e c²)")
    ax.set_title("Verdict matrix\ngreen=pair, orange=partial, red=no-change")
    ax.grid(alpha=0.3)

    # Panel 4: centroid count
    ax = axes[1, 1]
    for T, color in zip(temps, ["#47c", "#c33"]):
        omega_taus = []
        cent_vals = []
        for wl in wls:
            for r in results:
                if (r["config"]["temperature"] == T and
                    r["config"]["wavelength"] == wl):
                    omega_taus.append(r["config"]["omega_tau"])
                    cent_vals.append(r["max_centroids"])
        if omega_taus:
            ax.plot(omega_taus, cent_vals, "o-", lw=1.5, color=color,
                    label=f"T = {T}")
    ax.axhline(2, color="#2a7", ls="--", lw=0.8, label="pair threshold")
    ax.set_xlabel("ω·τ_relax")
    ax.set_ylabel("# centroids")
    ax.set_title("Detected soliton count (threshold_frac=0.7)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    plt.suptitle(
        f"Phase III-B v2 — Autoresonant sources + Dark-wake diagnostic "
        f"({len(results)} configs)",
        fontsize=12,
    )
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


if __name__ == "__main__":
    print("── Phase III-B v2: Autoresonant + dark-wake sweep ──\n")
    results = run_sweep()

    np.savez("/tmp/phase_iiib_v2_sweep.npz",
             results=np.array(results, dtype=object))

    render(results)

    print("\n── Summary ──")
    verdict_counts = {}
    for r in results:
        verdict_counts[r["verdict"]] = verdict_counts.get(r["verdict"], 0) + 1
    for v, c in sorted(verdict_counts.items()):
        print(f"  {v:>22}: {c}")

    # Compare v2 to v1 at matched (λ, amp, T) if available
    print("\n── Summary stats ──")
    cold = [r for r in results if r["config"]["temperature"] == 0.0]
    hot = [r for r in results if r["config"]["temperature"] > 0.0]
    if cold:
        print(f"  Cold (T=0): max A²_cos = {max(r['max_A2_cos'] for r in cold):.3e}, "
              f"max #centroids = {max(r['max_centroids'] for r in cold)}")
    if hot:
        print(f"  Hot (T>0):  max A²_cos = {max(r['max_A2_cos'] for r in hot):.3e}, "
              f"max τ_zx = {max(r['max_tau_zx'] for r in hot):.3e}, "
              f"max #centroids = {max(r['max_centroids'] for r in hot)}")
