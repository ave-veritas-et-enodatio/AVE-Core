"""
Phase III-B v3 — H1 centroid-threshold sensitivity probe.

Stage 5 Phase A of plan `review-the-collaboration-md-and-lexical-wombat.md`,
following [51_handoff_followups.md §1] (Hypothesis H1).

Question
--------
v2 reached A²_cos = 1.009 (rupture boundary) at λ=3.5, T=0.1, K_drift=0.5
but `find_soliton_centroids(threshold_frac=0.7)` returned zero centroids.
Either (a) pair-like structures exist below 70 % of max |ω|² and the
detector is too strict, or (b) A² saturates as a spatially distributed
plateau with no localized cores (thermal-noise peaks only).

H1 distinguishes these by re-running the v2 headline config and capturing
centroid positions at five thresholds {0.1, 0.2, 0.3, 0.5, 0.7} in the
SAME simulation (via the multi-threshold `TopologyObserver` extension).

Decision rule
-------------
- H1-PAIR:        Low-threshold centroids cluster near x=N/2 (collision
                  plane), count stable (~2) across low thresholds.
- H1-DISTRIBUTED: Low-threshold centroids scattered uniformly, count
                  grows monotonically as threshold drops (thermal noise).
- H1-AMBIGUOUS:   Partial clustering; needs a follow-up |ω|² spatial
                  heatmap to resolve.
"""
from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import time
from dataclasses import dataclass, field

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
class RunConfigV3:
    wavelength: float = 3.5           # v2 headline λ
    amplitude: float = 0.5            # v2 headline amp (× V_SNAP)
    temperature: float = 0.1          # v2 headline T (m_e c²)
    N: int = 40
    pml: int = 5
    t_ramp_periods: float = 3.0
    t_sustain_periods: float = 25.0
    n_outer_steps: int = 300
    record_cadence: int = 5
    K_drift: float = 0.5
    thresholds: list[float] = field(
        default_factory=lambda: [0.1, 0.2, 0.3, 0.5, 0.7]
    )

    @property
    def omega_carrier(self) -> float:
        return 2.0 * np.pi / self.wavelength


def run_h1(cfg: RunConfigV3) -> dict:
    engine = VacuumEngine3D.from_args(
        N=cfg.N, pml=cfg.pml,
        temperature=cfg.temperature,
        amplitude_convention="V_SNAP",
    )
    period = 2.0 * np.pi / cfg.omega_carrier
    t_ramp = cfg.t_ramp_periods * period
    t_sustain = cfg.t_sustain_periods * period
    source_offset = cfg.pml + 3

    # Identical source pair to v2 (counter-propagating along x̂)
    engine.add_source(AutoresonantCWSource(
        x0=source_offset, direction=(1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.5, t_ramp=t_ramp, t_sustain=t_sustain,
        K_drift=cfg.K_drift,
    ))
    engine.add_source(AutoresonantCWSource(
        x0=cfg.N - source_offset, direction=(-1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.5, t_ramp=t_ramp, t_sustain=t_sustain,
        K_drift=cfg.K_drift,
    ))

    regime_obs = RegimeClassifierObserver(cadence=cfg.record_cadence)
    topo_obs = TopologyObserver(
        cadence=cfg.record_cadence,
        threshold_fracs=cfg.thresholds,
    )
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

    max_A2_cos = max((h["max_A2_cos"] for h in regime_hist), default=0.0)
    max_A2_k4 = max((h["max_A2_k4"] for h in regime_hist), default=0.0)
    max_tau_zx = max((h["max_tau_zx"] for h in wake_hist), default=0.0)

    # Per-threshold aggregates
    per_thr_summary: dict[float, dict] = {}
    for tf in cfg.thresholds:
        ncs = [h["per_threshold"][tf]["n_centroids"] for h in topo_hist]
        max_n = max(ncs, default=0)
        final_n = ncs[-1] if ncs else 0
        # Accumulate all centroid positions across steps for spatial analysis
        all_centroids = []
        for h in topo_hist:
            for c in h["per_threshold"][tf]["centroids"]:
                all_centroids.append({
                    "t": h["t"],
                    "center": c["center"],
                    "peak_mag_sq": c["peak_mag_sq"],
                    "n_cells": c["n_cells"],
                })
        per_thr_summary[tf] = {
            "max_n_centroids": int(max_n),
            "final_n_centroids": int(final_n),
            "all_centroids": all_centroids,
        }

    # Adjudicate H1
    verdict = adjudicate_h1(per_thr_summary, cfg)

    print(f"── H1 Run (λ={cfg.wavelength}, T={cfg.temperature}, K_d={cfg.K_drift}) ──")
    print(f"  elapsed:       {elapsed:.1f} s")
    print(f"  max A²_k4:     {max_A2_k4:.3f}")
    print(f"  max A²_cos:    {max_A2_cos:.3f}")
    print(f"  max τ_zx:      {max_tau_zx:.3e}")
    print(f"  {'thr':>5}  {'max #cent':>10}  {'final #cent':>12}")
    for tf in cfg.thresholds:
        s = per_thr_summary[tf]
        print(f"  {tf:>5.2f}  {s['max_n_centroids']:>10d}  "
              f"{s['final_n_centroids']:>12d}")
    print(f"  verdict:       {verdict}")

    return {
        "config": {
            "wavelength": cfg.wavelength,
            "amplitude": cfg.amplitude,
            "temperature": cfg.temperature,
            "N": cfg.N,
            "pml": cfg.pml,
            "K_drift": cfg.K_drift,
            "thresholds": list(cfg.thresholds),
            "n_steps": cfg.n_outer_steps,
            "omega_tau": float(cfg.omega_carrier),
        },
        "elapsed_s": elapsed,
        "max_A2_cos": float(max_A2_cos),
        "max_A2_k4": float(max_A2_k4),
        "max_tau_zx": float(max_tau_zx),
        "per_threshold": per_thr_summary,
        "verdict": verdict,
    }


def adjudicate_h1(
    per_thr: dict[float, dict], cfg: RunConfigV3,
) -> str:
    """Classify result as H1-PAIR / H1-DISTRIBUTED / H1-AMBIGUOUS.

    Heuristic (in order of priority):
      1. H1-UNIFORM: no centroids at ANY threshold (field truly uniform).
      2. H1-DISTRIBUTED: at any threshold ≤ 0.3, max_n_centroids ≥ 10
         (explosion signals thermal-noise granularity, not pair cores).
         OR centroids at low thresholds scatter uniformly across the
         lattice (std_x ≥ N/4 with < 50 % near collision plane).
      3. H1-PAIR: low-threshold centroids cluster near x=N/2 AND every
         populated threshold has final_n_centroids in [2, 6].
      4. else H1-AMBIGUOUS.
    """
    N = cfg.N
    center_x = N / 2.0
    low_thr = [t for t in cfg.thresholds if t <= 0.3]
    if not low_thr:
        return "H1-AMBIGUOUS"

    # Collect centroid x-coords across low thresholds
    low_xs: list[float] = []
    low_final_counts: list[int] = []
    low_max_counts: list[int] = []
    for t in low_thr:
        low_final_counts.append(per_thr[t]["final_n_centroids"])
        low_max_counts.append(per_thr[t]["max_n_centroids"])
        for c in per_thr[t]["all_centroids"]:
            low_xs.append(c["center"][0])

    if not low_xs and all(per_thr[t]["max_n_centroids"] == 0 for t in cfg.thresholds):
        return "H1-UNIFORM"
    if not low_xs:
        return "H1-AMBIGUOUS"

    near_center = sum(1 for x in low_xs if abs(x - center_x) <= N / 4.0)
    near_frac = near_center / len(low_xs)
    std_x = float(np.std(low_xs))

    # H1-DISTRIBUTED: count explosion at ANY low threshold, OR uniform scatter
    if max(low_max_counts) >= 10:
        return "H1-DISTRIBUTED"
    if std_x >= N / 4.0 and near_frac < 0.5:
        return "H1-DISTRIBUTED"
    # H1-PAIR: spatially localized AND physical count range
    populated = [c for c in low_final_counts if c > 0]
    if near_frac >= 0.5 and populated and all(2 <= c <= 6 for c in populated):
        return "H1-PAIR"

    return "H1-AMBIGUOUS"


def render(result: dict, out: str = "/tmp/h1_threshold_summary.png") -> None:
    cfg = result["config"]
    per_thr = result["per_threshold"]
    thresholds = sorted(cfg["thresholds"])
    N = cfg["N"]
    center_x = N / 2.0

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # Panel 1: max #centroids vs threshold
    ax = axes[0]
    max_counts = [per_thr[t]["max_n_centroids"] for t in thresholds]
    final_counts = [per_thr[t]["final_n_centroids"] for t in thresholds]
    ax.plot(thresholds, max_counts, "o-", color="#c33", lw=1.8, label="max across run")
    ax.plot(thresholds, final_counts, "s--", color="#47c", lw=1.5, label="final step")
    ax.axhline(2, color="#2a7", ls=":", lw=1.0, label="pair threshold (n=2)")
    ax.set_xlabel("threshold_frac")
    ax.set_ylabel("# centroids")
    ax.set_title("Centroid count vs detection threshold\n"
                 f"(λ={cfg['wavelength']}, T={cfg['temperature']}, "
                 f"K_drift={cfg['K_drift']})")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    ax.set_xticks(thresholds)

    # Panel 2: spatial scatter at the LOWEST non-trivial threshold
    # Show all centroid positions across all recorded steps, color=threshold
    ax = axes[1]
    colormap = plt.get_cmap("viridis")
    for i, t in enumerate(thresholds):
        color = colormap(i / max(1, len(thresholds) - 1))
        xs = [c["center"][0] for c in per_thr[t]["all_centroids"]]
        yzs = [
            0.5 * (c["center"][1] + c["center"][2])
            for c in per_thr[t]["all_centroids"]
        ]
        if xs:
            ax.scatter(xs, yzs, s=18, color=color, alpha=0.55,
                       label=f"thr={t:.2f} ({len(xs)} pts)")
    ax.axvline(center_x, color="#2a7", ls="--", lw=1.2, alpha=0.7,
               label=f"collision plane x={center_x:.0f}")
    ax.set_xlabel("centroid x (lattice cells)")
    ax.set_ylabel("(y + z) / 2")
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_title(f"Spatial distribution of centroids across all recorded steps\n"
                 f"verdict: {result['verdict']}")
    ax.legend(fontsize=7, loc="upper right")
    ax.grid(alpha=0.3)

    plt.suptitle(
        f"H1 threshold sweep — max A²_cos = {result['max_A2_cos']:.3f}",
        fontsize=12,
    )
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


def _save_result(result: dict, out: str) -> None:
    """Save to .npz. Flatten per_threshold since numpy can't store nested
    dicts cleanly; we store thresholds + aggregate arrays + a JSON blob
    for the full centroid records."""
    import json
    cfg = result["config"]
    thresholds = np.array(cfg["thresholds"], dtype=float)
    max_counts = np.array(
        [result["per_threshold"][t]["max_n_centroids"] for t in cfg["thresholds"]],
        dtype=int,
    )
    final_counts = np.array(
        [result["per_threshold"][t]["final_n_centroids"] for t in cfg["thresholds"]],
        dtype=int,
    )
    # Serialize the full centroid records as JSON (cheap; ~few kB)
    full_records = {
        str(t): result["per_threshold"][t]["all_centroids"]
        for t in cfg["thresholds"]
    }
    np.savez(
        out,
        thresholds=thresholds,
        max_counts=max_counts,
        final_counts=final_counts,
        max_A2_cos=result["max_A2_cos"],
        max_A2_k4=result["max_A2_k4"],
        max_tau_zx=result["max_tau_zx"],
        verdict=result["verdict"],
        config_json=json.dumps(cfg),
        centroids_json=json.dumps(full_records),
    )
    print(f"Saved {out}")


if __name__ == "__main__":
    print("── Phase III-B v3: H1 centroid-threshold sensitivity probe ──\n")
    cfg = RunConfigV3()
    result = run_h1(cfg)
    _save_result(result, "/tmp/h1_threshold_sweep.npz")
    render(result)
    print(f"\nH1 verdict: {result['verdict']}")
