"""
Phase 3.5.A.0 — v2 headline reproducibility check.

Runs the v2 headline config (λ=3.5, T=0.1, K_drift=0.5, amp=0.5·V_SNAP,
N=40, 300 steps) with 20 explicit RNG seeds and records the max A²_cos
distribution. Goal: verify that the post-Phase-2 engine can still reach
A²_cos = 1.009 under some seed, or at least bracket the actual reachable
range.

Background: doc 52_ §3.3 noted that a single-seed rerun during H1 work
produced A²_cos = 0.877 (vs v2's 1.009). The Phase 3 _connect_all change
and Phase 2 NodeResonanceObserver plumbing may have further perturbed
the trajectory.

If 1.009 sits outside the seed-distribution IQR, that's a real regression
and Stage 6 must diff-bisect against an earlier commit (pre-Phase-2).

Output:
  /tmp/v2_reproducibility_sweep.npz  — {seed, max_A2_cos, max_A2_k4, max_tau_zx, ...}
  /tmp/v2_reproducibility_sweep.png  — histogram of max A²_cos

Expected runtime: ~90s × 20 seeds ≈ 30 min.
"""
from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import time
from dataclasses import dataclass

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.topological.vacuum_engine import (
    VacuumEngine3D,
    AutoresonantCWSource,
    RegimeClassifierObserver,
    DarkWakeObserver,
)


@dataclass
class V2HeadlineConfig:
    wavelength: float = 3.5
    amplitude: float = 0.5
    temperature: float = 0.1
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


def run_one_seed(cfg: V2HeadlineConfig, seed: int) -> dict:
    """Run the v2 headline config with an explicit RNG seed."""
    # Construct engine (auto-calls initialize_thermal(T, seed=None)).
    engine = VacuumEngine3D.from_args(
        N=cfg.N, pml=cfg.pml,
        temperature=cfg.temperature,
        amplitude_convention="V_SNAP",
    )
    # Override with explicit seed
    engine.initialize_thermal(cfg.temperature, seed=seed)

    period = 2.0 * np.pi / cfg.omega_carrier
    t_ramp = cfg.t_ramp_periods * period
    t_sustain = cfg.t_sustain_periods * period
    src_offset = cfg.pml + 3

    engine.add_source(AutoresonantCWSource(
        x0=src_offset, direction=(1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.5, t_ramp=t_ramp, t_sustain=t_sustain,
        K_drift=cfg.K_drift,
    ))
    engine.add_source(AutoresonantCWSource(
        x0=cfg.N - src_offset, direction=(-1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.5, t_ramp=t_ramp, t_sustain=t_sustain,
        K_drift=cfg.K_drift,
    ))

    regime_obs = RegimeClassifierObserver(cadence=cfg.record_cadence)
    wake_obs = DarkWakeObserver(cadence=cfg.record_cadence, propagation_axis=0)
    engine.add_observer(regime_obs)
    engine.add_observer(wake_obs)

    t0 = time.time()
    engine.run(n_steps=cfg.n_outer_steps)
    elapsed = time.time() - t0

    regime_hist = regime_obs.history
    wake_hist = wake_obs.history
    max_A2_cos = max((h["max_A2_cos"] for h in regime_hist), default=0.0)
    max_A2_k4 = max((h["max_A2_k4"] for h in regime_hist), default=0.0)
    max_A2_total = max((h["max_A2_total"] for h in regime_hist), default=0.0)
    max_tau_zx = max((h["max_tau_zx"] for h in wake_hist), default=0.0)

    return {
        "seed": seed,
        "max_A2_cos": float(max_A2_cos),
        "max_A2_k4": float(max_A2_k4),
        "max_A2_total": float(max_A2_total),
        "max_tau_zx": float(max_tau_zx),
        "elapsed_s": elapsed,
    }


def render(results: list[dict], out: str = "/tmp/v2_reproducibility_sweep.png") -> None:
    seeds = np.array([r["seed"] for r in results])
    A2_cos = np.array([r["max_A2_cos"] for r in results])

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # Panel 1: scatter vs seed
    ax = axes[0]
    ax.scatter(seeds, A2_cos, s=30, color="#c33", alpha=0.8)
    ax.axhline(1.009, color="#47c", ls="--", lw=1.2, label="v2 headline (1.009)")
    ax.axhline(1.0, color="#888", ls=":", lw=0.8, label="rupture boundary (A²=1)")
    ax.axhline(float(np.median(A2_cos)), color="#2a7", ls="-", lw=1.0,
               label=f"this-run median ({np.median(A2_cos):.3f})")
    ax.set_xlabel("seed")
    ax.set_ylabel("max A²_cos")
    ax.set_title("Max A²_cos per seed (v2 headline)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 2: histogram
    ax = axes[1]
    ax.hist(A2_cos, bins=15, color="#47c", edgecolor="black", alpha=0.8)
    ax.axvline(1.009, color="#c33", ls="--", lw=1.5, label="v2 headline (1.009)")
    ax.axvline(float(np.median(A2_cos)), color="#2a7", ls="-", lw=1.2,
               label=f"median ({np.median(A2_cos):.3f})")
    q25, q75 = np.percentile(A2_cos, [25, 75])
    ax.axvspan(q25, q75, color="#2a7", alpha=0.15, label=f"IQR [{q25:.3f}, {q75:.3f}]")
    ax.set_xlabel("max A²_cos")
    ax.set_ylabel("count")
    ax.set_title(f"Distribution across {len(results)} seeds")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    plt.suptitle(
        f"Phase 3.5.A.0 — v2 headline reproducibility sweep",
        fontsize=12,
    )
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


def adjudicate(results: list[dict]) -> dict:
    A2_cos = np.array([r["max_A2_cos"] for r in results])
    q25, q50, q75 = np.percentile(A2_cos, [25, 50, 75])
    headline = 1.009
    above_headline = int(np.sum(A2_cos >= headline))
    within_tol = int(np.sum(np.abs(A2_cos - headline) <= 0.05))
    inside_iqr = q25 <= headline <= q75

    if above_headline > 0 or within_tol >= len(results) // 4:
        verdict = "REPRODUCES"
    elif inside_iqr:
        verdict = "PARTIALLY-REPRODUCES (headline within IQR but not commonly reached)"
    else:
        verdict = "REGRESSION (headline outside IQR)"

    return {
        "verdict": verdict,
        "n_seeds": len(results),
        "min": float(A2_cos.min()),
        "max": float(A2_cos.max()),
        "median": float(q50),
        "q25": float(q25),
        "q75": float(q75),
        "iqr": float(q75 - q25),
        "above_headline_count": above_headline,
        "within_tol_count": within_tol,
        "headline_in_iqr": bool(inside_iqr),
    }


if __name__ == "__main__":
    print("── v2 headline reproducibility seed sweep ──\n")
    cfg = V2HeadlineConfig()
    print(f"Config: λ={cfg.wavelength}, T={cfg.temperature}, amp={cfg.amplitude}·V_SNAP, "
          f"K_drift={cfg.K_drift}, N={cfg.N}, n_steps={cfg.n_outer_steps}")

    n_seeds = int(os.environ.get("N_SEEDS", "20"))
    print(f"Running {n_seeds} seeds (expected ~{90 * n_seeds / 60:.0f} min)\n")

    results = []
    t0 = time.time()
    for seed in range(n_seeds):
        r = run_one_seed(cfg, seed)
        results.append(r)
        print(f"  seed {seed:>2d}: max A²_cos = {r['max_A2_cos']:.4f}  "
              f"(max A²_k4 = {r['max_A2_k4']:.3f}, elapsed {r['elapsed_s']:.1f}s)")
    total = time.time() - t0
    print(f"\nTotal elapsed: {total:.1f}s ({total/60:.1f} min)\n")

    # Save raw
    np.savez("/tmp/v2_reproducibility_sweep.npz",
             seeds=np.array([r["seed"] for r in results]),
             max_A2_cos=np.array([r["max_A2_cos"] for r in results]),
             max_A2_k4=np.array([r["max_A2_k4"] for r in results]),
             max_A2_total=np.array([r["max_A2_total"] for r in results]),
             max_tau_zx=np.array([r["max_tau_zx"] for r in results]))
    print("Saved /tmp/v2_reproducibility_sweep.npz")

    render(results)

    verdict = adjudicate(results)
    print(f"\n── Adjudication ──")
    print(f"  verdict:        {verdict['verdict']}")
    print(f"  n_seeds:        {verdict['n_seeds']}")
    print(f"  range:          [{verdict['min']:.4f}, {verdict['max']:.4f}]")
    print(f"  median:         {verdict['median']:.4f}")
    print(f"  IQR:            [{verdict['q25']:.4f}, {verdict['q75']:.4f}]")
    print(f"  headline:       1.009  (v2 documented)")
    print(f"  at-or-above:    {verdict['above_headline_count']}/{verdict['n_seeds']}")
    print(f"  within ±0.05:   {verdict['within_tol_count']}/{verdict['n_seeds']}")
    print(f"  headline IQR-in: {verdict['headline_in_iqr']}")

    if verdict["verdict"] == "REGRESSION (headline outside IQR)":
        print("\n✗ REGRESSION FLAG. v2 headline no longer reachable.")
        print("  Diff-bisect Stage 6 commits to find the perturbation.")
        sys.exit(1)
    if verdict["verdict"] == "PARTIALLY-REPRODUCES (headline within IQR but not commonly reached)":
        print("\n⚠ Partial reproduce. v2's 1.009 was a tail outcome, not typical.")
        sys.exit(0)
    print("\n✓ v2 headline reproduces.")
    sys.exit(0)
