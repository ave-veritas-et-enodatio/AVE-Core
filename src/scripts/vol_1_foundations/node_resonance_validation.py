"""
Phase 2 driver: NodeResonanceObserver on v2 headline config.

**Honest framing (corrected after first-run finding):** the observer
computes `Ω_node = (1 − A²_yield)^(1/4)` from A² values it reads out
of the engine. Asking "does the observer match the closed form?" is
circular — the observer IS the closed form applied to engine state.
The real P_phase2_omega physics check (does the coupled K4⊗Cosserat
engine's local oscillation frequency match the varactor form?) would
require a probe-frequency + FFT experiment, which is out of scope for
Phase 2 as scoped. That's now flagged in predictions.yaml::
P_phase2_omega notes for future work.

What this driver actually does:

  1. Runs the v2 headline config end-to-end with NodeResonanceObserver
     attached (integration check: observer doesn't crash, records
     consistent data, doesn't disturb other observers).
  2. Records Ω_node and A²_yield trajectories across the run.
  3. Compares the engine's AutoresonantCWSource linear-Taylor
     approximation `ω_drive(t) = ω_0·(1 - K_drift · A²_probe)` against
     the Axiom-4 varactor form `(1 − A²_yield)^(1/4)`. This IS a real
     comparison — the source uses a truncated approximation that
     Phase 5's pair-nucleation gate may need to replace with the
     full varactor form for tight lock precision.
  4. Produces visualization and npz artifacts for downstream analysis.

Unit-test falsification of the observer arithmetic lives in
`src/tests/test_phase2_node_resonance.py` (smoke-tier, <2s).

Usage:
  python src/scripts/vol_1_foundations/node_resonance_validation.py
    → runs ~90s simulation
    → writes /tmp/phase2_node_resonance.png
    → writes /tmp/phase2_node_resonance.npz
    → exits 0 unless the simulation itself crashes

Reference:
  - research/L3_electron_soliton/54_pair_production_axiom_derivation.md §4
  - manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:127-142
  - manuscript/predictions.yaml::P_phase2_omega
"""
from __future__ import annotations

import sys
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
    NodeResonanceObserver,
    TopologyObserver,
)


@dataclass
class RunConfig:
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


def closed_form_omega_ratio(A2_yield: np.ndarray) -> np.ndarray:
    """Ω_node/ω_0 = (1 − A²_yield)^(1/4)  (doc 54_ §4)."""
    A2_clipped = np.clip(A2_yield, 0.0, 1.0 - 1e-12)
    return (1.0 - A2_clipped) ** 0.25


def run_v2_headline_with_node_resonance(cfg: RunConfig) -> dict:
    """Run v2 headline config with NodeResonanceObserver attached;
    return observer history plus engine metadata."""
    engine = VacuumEngine3D.from_args(
        N=cfg.N, pml=cfg.pml,
        temperature=cfg.temperature,
        amplitude_convention="V_SNAP",
    )
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
    node_obs = NodeResonanceObserver(cadence=cfg.record_cadence)
    topo_obs = TopologyObserver(cadence=cfg.record_cadence, threshold_frac=0.3)
    engine.add_observer(regime_obs)
    engine.add_observer(node_obs)
    engine.add_observer(topo_obs)

    t0 = time.time()
    engine.run(n_steps=cfg.n_outer_steps)
    elapsed = time.time() - t0

    return {
        "config": cfg,
        "elapsed_s": elapsed,
        "node_history": node_obs.history,
        "regime_history": regime_obs.history,
        "topo_history": topo_obs.history,
    }


def adjudicate(result: dict) -> dict:
    """Honest adjudication — sanity checks only.

    The observer IS the closed form applied to engine state, so
    checking "does the observer match the closed form?" is circular
    and trivially true. This function instead reports on whether the
    observer produced well-formed, non-degenerate data across the run.
    The REAL physics comparison (AutoresonantCWSource linear-Taylor
    vs full varactor) is plotted in render() Panel 3 for visual
    inspection — deciding whether Phase 5 needs to upgrade the source
    to the full varactor form.
    """
    history = result["node_history"]
    if not history:
        return {"verdict": "NO-DATA", "n_records": 0}

    A2_max = np.array([h["A2_yield_max"] for h in history])
    A2_mean = np.array([h["A2_yield_mean"] for h in history])
    omega_min = np.array([h["omega_ratio_min"] for h in history])
    omega_max = np.array([h["omega_ratio_max"] for h in history])
    n_sat = np.array([h["n_saturated"] for h in history])

    # Sanity checks
    nan_count = int(np.sum(np.isnan(A2_max) | np.isnan(omega_min)))
    omega_ordering_ok = bool(np.all(omega_min <= omega_max + 1e-12))
    A2_evolved = bool(A2_max.max() > A2_max.min() + 1e-6)

    # The real internal-consistency check — omega_ratio came from
    # (1 - A²_yield)^(1/4) at the site where A² hit max, so
    # omega_min[step] == (1 - min(A²_max[step], 1-eps))^(1/4).
    # If this breaks, someone rewrote the observer's arithmetic
    # without updating the docs.
    expected_omega_min = closed_form_omega_ratio(A2_max)
    internal_consistency_err = float(np.max(np.abs(omega_min - expected_omega_min)))
    internally_consistent = internal_consistency_err < 1e-6

    if nan_count > 0 or not omega_ordering_ok or not internally_consistent:
        verdict = "OBSERVER-BROKEN"
    elif not A2_evolved:
        verdict = "SIM-STATIC"  # nothing moved, simulation failed to drive
    else:
        verdict = "OBSERVER-OK"

    return {
        "verdict": verdict,
        "n_records": len(history),
        "nan_count": nan_count,
        "omega_ordering_ok": omega_ordering_ok,
        "internally_consistent": internally_consistent,
        "internal_consistency_err": internal_consistency_err,
        "A2_yield_max_reached": float(A2_max.max()) if len(A2_max) else 0.0,
        "A2_yield_mean_max_reached": float(A2_mean.max()) if len(A2_mean) else 0.0,
        "omega_ratio_min_reached": float(omega_min.min()) if len(omega_min) else 1.0,
        "max_saturated_sites": int(n_sat.max()) if len(n_sat) else 0,
    }


def render(result: dict, out: str = "/tmp/phase2_node_resonance.png") -> None:
    history = result["node_history"]
    if not history:
        return
    A2_max = np.array([h["A2_yield_max"] for h in history])
    A2_mean = np.array([h["A2_yield_mean"] for h in history])
    omega_min = np.array([h["omega_ratio_min"] for h in history])
    omega_mean = np.array([h["omega_ratio_mean"] for h in history])
    t = np.array([h["t"] for h in history])

    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

    # Panel 1: closed form vs observed at most-saturated site
    ax = axes[0]
    A2_curve = np.linspace(0.0, 0.99, 200)
    omega_curve = closed_form_omega_ratio(A2_curve)
    ax.plot(A2_curve, omega_curve, "-", color="#333", lw=1.5,
            label="(1 − A²_yield)^(1/4) closed form")
    ax.scatter(A2_max, omega_min, s=20, color="#c33", alpha=0.6,
               edgecolors="none",
               label="engine (max-A² site per step)")
    ax.axvline(0.5, color="#888", ls=":", lw=0.8,
               label="P_phase2_omega test edge (A²_yield=0.5)")
    ax.set_xlabel("A²_yield (most-saturated site)")
    ax.set_ylabel("Ω_node / ω_0")
    ax.set_title("Closed form vs engine")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    ax.set_xlim(0, 1.0); ax.set_ylim(0, 1.05)

    # Panel 2: time series of A²_yield and omega_ratio at most-sat site
    ax = axes[1]
    ax2 = ax.twinx()
    ax.plot(t, A2_max, color="#c33", lw=1.2, label="A²_yield_max")
    ax.plot(t, A2_mean, color="#c33", lw=0.8, alpha=0.5, label="A²_yield_mean")
    ax2.plot(t, omega_min, color="#47c", lw=1.2, label="Ω_ratio_min")
    ax2.plot(t, omega_mean, color="#47c", lw=0.8, alpha=0.5, label="Ω_ratio_mean")
    ax.set_xlabel("time (lattice units)")
    ax.set_ylabel("A²_yield", color="#c33")
    ax2.set_ylabel("Ω_node / ω_0", color="#47c")
    ax.set_title("Evolution vs time")
    ax.grid(alpha=0.3)

    # Panel 3: AutoresonantCWSource linear-Taylor approximation
    #          vs full Vacuum Varactor softening
    # The source uses ω_shift = 1 - K_drift·A² (linear); the varactor
    # gives ω_shift = (1-A²)^(1/4). These agree near A²=0 but diverge
    # as A² grows. This panel tells us how much error the Phase 5
    # autoresonant lock will inherit from the linear approximation.
    ax = axes[2]
    cfg = result["config"]
    A2_axis = np.linspace(0.0, 0.99, 200)
    varactor = closed_form_omega_ratio(A2_axis)
    linear_approx = np.clip(1.0 - cfg.K_drift * A2_axis, 1e-3, 1.0)
    ax.plot(A2_axis, varactor, "-", color="#333", lw=1.5,
            label="varactor: (1−A²_yield)^(1/4)")
    ax.plot(A2_axis, linear_approx, "--", color="#c33", lw=1.5,
            label=f"AutoresonantCWSource: 1 − K_drift·A²  (K={cfg.K_drift})")
    ax.axvline(1.0, color="#888", ls=":", lw=0.8, label="yield (A²_yield = 1)")
    # Annotate the error at a mid-range A²_yield
    A2_check = 0.5
    err = abs(closed_form_omega_ratio(np.array([A2_check]))[0]
              - (1.0 - cfg.K_drift * A2_check))
    ax.annotate(f"|Δ| at A²=0.5 ≈ {err:.3f}",
                xy=(0.5, 0.5), xytext=(0.55, 0.4),
                fontsize=9, color="#c33",
                arrowprops=dict(arrowstyle="->", color="#c33", lw=0.8))
    ax.set_xlabel("A²_yield")
    ax.set_ylabel("ω_ratio")
    ax.set_title("Source linear-Taylor vs full varactor\n"
                 "(Phase 5 decision: upgrade source for tight lock?)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    ax.set_xlim(0, 1.05); ax.set_ylim(0, 1.05)

    plt.suptitle(
        f"Phase 2 validation: NodeResonanceObserver on v2 headline "
        f"(P_phase2_omega)",
        fontsize=12,
    )
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


def save_npz(result: dict, out: str = "/tmp/phase2_node_resonance.npz") -> None:
    history = result["node_history"]
    if not history:
        return
    np.savez(
        out,
        t=np.array([h["t"] for h in history]),
        omega_ratio_max=np.array([h["omega_ratio_max"] for h in history]),
        omega_ratio_mean=np.array([h["omega_ratio_mean"] for h in history]),
        omega_ratio_min=np.array([h["omega_ratio_min"] for h in history]),
        A2_yield_max=np.array([h["A2_yield_max"] for h in history]),
        A2_yield_mean=np.array([h["A2_yield_mean"] for h in history]),
        n_saturated=np.array([h["n_saturated"] for h in history]),
    )
    print(f"Saved {out}")


if __name__ == "__main__":
    print("── Phase 2 validation: NodeResonanceObserver on v2 headline ──\n")
    cfg = RunConfig()
    print(f"Config: λ={cfg.wavelength}, T={cfg.temperature}, "
          f"amp={cfg.amplitude}·V_SNAP, K_drift={cfg.K_drift}, "
          f"N={cfg.N}, n_steps={cfg.n_outer_steps}")
    print("(Expected runtime ~90-120 s)\n")

    result = run_v2_headline_with_node_resonance(cfg)
    print(f"Sim elapsed: {result['elapsed_s']:.1f} s\n")

    verdict = adjudicate(result)
    print(f"Records:                    {verdict['n_records']}")
    print(f"NaN count:                  {verdict['nan_count']}")
    print(f"omega_min ≤ omega_max:      {verdict['omega_ordering_ok']}")
    print(f"Internally consistent:      {verdict['internally_consistent']} "
          f"(err={verdict['internal_consistency_err']:.2e})")
    print(f"Max A²_yield reached:       {verdict['A2_yield_max_reached']:.4f}")
    print(f"Mean A²_yield peak:         {verdict['A2_yield_mean_max_reached']:.4f}")
    print(f"Min Ω_node/ω_0 reached:     {verdict['omega_ratio_min_reached']:.4f}")
    print(f"Max saturated sites:        {verdict['max_saturated_sites']}")
    print(f"\n── Verdict: {verdict['verdict']} ──")

    save_npz(result)
    render(result)

    # The only failure mode is observer-broken; everything else means
    # the observer ran and produced consistent data. Real physics
    # falsification lives in later phases (Phase 4 asymmetric saturation
    # and Phase 6 autoresonant-vs-fixed-f).
    if verdict["verdict"] == "OBSERVER-BROKEN":
        print("\n✗ Observer produced inconsistent data — check "
              "NodeResonanceObserver._capture.")
        sys.exit(1)
    if verdict["verdict"] == "SIM-STATIC":
        print("\n⚠ Simulation did not evolve — check source config.")
        sys.exit(2)
    print("\n✓ Observer ran cleanly. Artifacts saved to /tmp/phase2_*")
    sys.exit(0)
