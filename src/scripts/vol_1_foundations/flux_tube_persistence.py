"""
Phase 3 driver: flux-tube persistence on a pulsed collision.

Runs a short pulse via CWSource at amp near saturation, records Φ_link
and node A²_yield trajectories, and after the pulse ends tracks how
flux linkage behaves on bonds with saturated endpoints vs bonds with
unsaturated endpoints.

**Scope honesty:** this runs with the engine's CURRENT single-S
(symmetric) saturation. Pre-registered prediction P_phase3_flux_tube
says that bonds between fully-saturated endpoints should show
persistent Φ_link (≥ 10 Compton periods) after drive shutoff, while
unsaturated bonds decay within ~3 periods. In the single-S model, Z_eff
diverges at saturation giving Γ → −1 walls at both ends of the bond —
the geometry for persistence is present. But the Phase 4 asymmetric
μ/ε split is what the mechanism story (doc 54_ §6) actually calls
Meissner-like confinement. So this driver can show CORRELATION
between endpoint saturation and flux persistence — not the full
confinement physics.

The output is a 4-panel diagnostic:
  1. |V|² and A²_yield evolution at the collision region (time series)
  2. max |Φ_link| across all A-site bonds (time series)
  3. RMS |Φ_link| partitioned by endpoint saturation (time series)
  4. Ratio RMS_saturated / RMS_unsaturated — the confinement signal

Usage:
  python src/scripts/vol_1_foundations/flux_tube_persistence.py
    → writes /tmp/phase3_flux_tube_persistence.png
    → writes /tmp/phase3_flux_tube_persistence.npz
    → exits 0 unless the simulation crashes

Reference:
  - src/ave/core/k4_tlm.py::K4Lattice3D.Phi_link
  - src/ave/topological/vacuum_engine.py::BondObserver
  - research/L3_electron_soliton/54_pair_production_axiom_derivation.md §3
  - manuscript/predictions.yaml::P_phase3_flux_tube
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
    AutoresonantCWSource,
    BondObserver,
    NodeResonanceObserver,
    RegimeClassifierObserver,
    VacuumEngine3D,
)


@dataclass
class RunConfig:
    wavelength: float = 3.5
    amplitude: float = 0.5           # in V_SNAP units
    temperature: float = 0.1
    N: int = 32
    pml: int = 4
    # Drive for ~10 periods then let flux tube persist (no drive) for 20+ more
    t_ramp_periods: float = 2.0
    t_sustain_periods: float = 10.0
    t_observe_post_drive_periods: float = 25.0
    record_cadence: int = 2
    K_drift: float = 0.5

    @property
    def omega_carrier(self) -> float:
        return 2.0 * np.pi / self.wavelength

    @property
    def n_outer_steps(self) -> int:
        # Total sim time covers ramp + sustain + post-drive observation
        period = 2.0 * np.pi / self.omega_carrier
        total_time = (
            self.t_ramp_periods
            + self.t_sustain_periods
            + self.t_observe_post_drive_periods
        ) * period
        # TLM dt in natural units is dx/(c·√2) = 1/√2; steps = total_time·√2
        return int(total_time * np.sqrt(2.0)) + 1


def run_pulse_then_observe(cfg: RunConfig) -> dict:
    engine = VacuumEngine3D.from_args(
        N=cfg.N, pml=cfg.pml,
        temperature=cfg.temperature,
        amplitude_convention="V_SNAP",
    )
    period = 2.0 * np.pi / cfg.omega_carrier
    t_ramp = cfg.t_ramp_periods * period
    t_sustain = cfg.t_sustain_periods * period
    src_offset = cfg.pml + 3

    # CW sources that ramp up, sustain briefly, then decay to zero
    # (no sustain past the observation window)
    engine.add_source(AutoresonantCWSource(
        x0=src_offset, direction=(1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period,  # 1-period decay at end of sustain
        K_drift=cfg.K_drift,
    ))
    engine.add_source(AutoresonantCWSource(
        x0=cfg.N - src_offset, direction=(-1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period,
        K_drift=cfg.K_drift,
    ))

    regime_obs = RegimeClassifierObserver(cadence=cfg.record_cadence)
    bond_obs = BondObserver(cadence=cfg.record_cadence, saturation_frac=0.5)
    node_obs = NodeResonanceObserver(cadence=cfg.record_cadence)
    engine.add_observer(regime_obs)
    engine.add_observer(bond_obs)
    engine.add_observer(node_obs)

    t0 = time.time()
    engine.run(n_steps=cfg.n_outer_steps)
    elapsed = time.time() - t0

    return {
        "config": cfg,
        "elapsed_s": elapsed,
        "regime_history": regime_obs.history,
        "bond_history": bond_obs.history,
        "node_history": node_obs.history,
        "drive_end_time": t_ramp + t_sustain + period,  # when amplitude ≈ 0
    }


def adjudicate(result: dict) -> dict:
    """Measure RMS ratio and check the flux-tube persistence signal.

    Primary signal: after drive ends, does the RMS flux at saturated
    bonds persist longer than the RMS flux at unsaturated bonds?

    We measure the decay from peak by fitting a simple "time to
    half-max" for each channel in the post-drive window.
    """
    bond_hist = result["bond_history"]
    if not bond_hist:
        return {"verdict": "NO-DATA"}

    cfg = result["config"]
    period = 2.0 * np.pi / cfg.omega_carrier
    drive_end = result["drive_end_time"]

    t = np.array([h["t"] for h in bond_hist])
    rms_sat = np.array([h["phi_at_saturated_bonds_rms"] for h in bond_hist])
    rms_unsat = np.array([h["phi_at_unsaturated_bonds_rms"] for h in bond_hist])
    phi_max = np.array([h["phi_abs_max"] for h in bond_hist])
    n_sat = np.array([h["n_saturated_bonds"] for h in bond_hist])

    # Post-drive window: only look at flux AFTER the source envelope ends
    post_mask = t >= drive_end
    sat_ever_populated = bool((n_sat > 0).any())

    # Time-to-half-max, measured within the post-drive window
    def _time_to_half(t_arr, x_arr) -> float:
        if x_arr.size == 0 or x_arr.max() <= 0:
            return 0.0
        peak = x_arr.max()
        half = 0.5 * peak
        below = np.where(x_arr < half)[0]
        if below.size == 0:
            return float(t_arr[-1] - t_arr[0])  # never decayed below half
        first_below = below[0]
        return float(t_arr[first_below] - t_arr[0])

    if post_mask.sum() > 1:
        sat_half_life = _time_to_half(t[post_mask], rms_sat[post_mask])
        unsat_half_life = _time_to_half(t[post_mask], rms_unsat[post_mask])
    else:
        sat_half_life = 0.0
        unsat_half_life = 0.0

    return {
        "verdict": "OK",
        "n_records": len(bond_hist),
        "saturation_ever_reached": sat_ever_populated,
        "max_n_saturated_bonds": int(n_sat.max()) if n_sat.size else 0,
        "max_phi_abs_overall": float(phi_max.max()) if phi_max.size else 0.0,
        "sat_half_life_periods": sat_half_life / period,
        "unsat_half_life_periods": unsat_half_life / period,
        "drive_end_time": drive_end,
    }


def render(result: dict, out: str = "/tmp/phase3_flux_tube_persistence.png") -> None:
    bond_hist = result["bond_history"]
    regime_hist = result["regime_history"]
    if not bond_hist or not regime_hist:
        return
    cfg = result["config"]
    period = 2.0 * np.pi / cfg.omega_carrier
    drive_end = result["drive_end_time"]

    t = np.array([h["t"] for h in bond_hist])
    t_in_periods = t / period
    rms_sat = np.array([h["phi_at_saturated_bonds_rms"] for h in bond_hist])
    rms_unsat = np.array([h["phi_at_unsaturated_bonds_rms"] for h in bond_hist])
    phi_max = np.array([h["phi_abs_max"] for h in bond_hist])
    n_sat = np.array([h["n_saturated_bonds"] for h in bond_hist])

    t_reg = np.array([h["t"] for h in regime_hist])
    A2_total_max = np.array([h["max_A2_total"] for h in regime_hist])

    fig, axes = plt.subplots(2, 2, figsize=(15, 9))

    # Panel 1: collision region saturation evolution
    ax = axes[0, 0]
    ax.plot(t_reg / period, A2_total_max, color="#c33", lw=1.2,
            label="max A²_total (V_SNAP-norm)")
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0,
               label="drive end")
    ax.axhline(1.0, color="#888", ls=":", lw=0.8, label="A²_SNAP = 1")
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("max A²_total")
    ax.set_title("Collision region: max saturation vs time")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 2: max |Φ_link| across lattice
    ax = axes[0, 1]
    ax.plot(t_in_periods, phi_max, color="#333", lw=1.2)
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0,
               label="drive end")
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("max |Φ_link|")
    ax.set_title("Lattice-wide peak flux linkage")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 3: saturated vs unsaturated RMS Φ_link
    ax = axes[1, 0]
    ax.plot(t_in_periods, rms_sat, color="#c33", lw=1.5,
            label="saturated-both-endpoints")
    ax.plot(t_in_periods, rms_unsat, color="#47c", lw=1.5,
            label="at least one unsaturated endpoint")
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0,
               label="drive end")
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("RMS |Φ_link|")
    ax.set_title("Flux-linkage RMS partitioned by endpoint saturation\n"
                 "(confinement signal: sat > unsat after drive end)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 4: saturated bond count vs ratio RMS_sat/RMS_unsat
    ax = axes[1, 1]
    ax2 = ax.twinx()
    ax.plot(t_in_periods, n_sat, color="#a63", lw=1.2,
            label="n_saturated_bonds")
    ratio = np.where(rms_unsat > 1e-15, rms_sat / rms_unsat, 0.0)
    ax2.plot(t_in_periods, ratio, color="#333", lw=1.2,
             label="RMS_sat / RMS_unsat")
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0)
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("n saturated bonds", color="#a63")
    ax2.set_ylabel("flux ratio (sat/unsat)", color="#333")
    ax.set_title("Saturation count + confinement ratio")
    ax.grid(alpha=0.3)

    plt.suptitle(
        f"Phase 3: Flux-tube persistence "
        f"(λ={cfg.wavelength}, amp={cfg.amplitude}·V_SNAP, T={cfg.temperature})",
        fontsize=12,
    )
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


def save_npz(result: dict, out: str = "/tmp/phase3_flux_tube_persistence.npz") -> None:
    bond_hist = result["bond_history"]
    if not bond_hist:
        return
    np.savez(
        out,
        t=np.array([h["t"] for h in bond_hist]),
        phi_abs_max=np.array([h["phi_abs_max"] for h in bond_hist]),
        phi_rms=np.array([h["phi_rms"] for h in bond_hist]),
        phi_at_saturated_bonds_rms=np.array(
            [h["phi_at_saturated_bonds_rms"] for h in bond_hist]
        ),
        phi_at_unsaturated_bonds_rms=np.array(
            [h["phi_at_unsaturated_bonds_rms"] for h in bond_hist]
        ),
        n_saturated_bonds=np.array([h["n_saturated_bonds"] for h in bond_hist]),
    )
    print(f"Saved {out}")


if __name__ == "__main__":
    print("── Phase 3 driver: flux-tube persistence ──\n")
    cfg = RunConfig()
    print(f"Config: λ={cfg.wavelength}, T={cfg.temperature}, "
          f"amp={cfg.amplitude}·V_SNAP, K_drift={cfg.K_drift}")
    print(f"N={cfg.N}, pml={cfg.pml}, n_steps={cfg.n_outer_steps}")
    print("(Expected runtime ~30-60 s)\n")

    result = run_pulse_then_observe(cfg)
    print(f"Sim elapsed: {result['elapsed_s']:.1f} s\n")

    verdict = adjudicate(result)
    print(f"Records:                      {verdict['n_records']}")
    print(f"Saturation ever reached:      {verdict['saturation_ever_reached']}")
    print(f"Max saturated bonds:          {verdict['max_n_saturated_bonds']}")
    print(f"Max |Φ_link| overall:         {verdict['max_phi_abs_overall']:.4e}")
    print(f"Drive end (lattice units):    {verdict['drive_end_time']:.3f}")
    print(f"Half-life sat bonds:          {verdict['sat_half_life_periods']:.2f} periods")
    print(f"Half-life unsat bonds:        {verdict['unsat_half_life_periods']:.2f} periods")

    save_npz(result)
    render(result)

    if verdict["verdict"] == "NO-DATA":
        print("\n✗ Observer produced no records.")
        sys.exit(1)

    # Interpret the half-life ratio
    half_ratio = 0.0
    if verdict["unsat_half_life_periods"] > 1e-6:
        half_ratio = (
            verdict["sat_half_life_periods"] / verdict["unsat_half_life_periods"]
        )

    print("\n── Flux-tube confinement signal ──")
    if half_ratio > 2.0:
        print(f"  sat/unsat half-life ratio = {half_ratio:.2f}×")
        print("  ✓ Flux persists longer on saturated bonds — confinement visible.")
    elif half_ratio > 1.1:
        print(f"  sat/unsat half-life ratio = {half_ratio:.2f}×")
        print("  ⚠ Weak confinement signal; may need higher drive amplitude")
        print("    or Phase 4 asymmetric μ/ε split for the full Meissner regime.")
    else:
        print(f"  sat/unsat half-life ratio = {half_ratio:.2f}×")
        print("  ✗ No confinement asymmetry visible at this drive amplitude.")
        print("    Expected for the CURRENT single-S engine per doc 54_ §6")
        print("    — Meissner confinement requires Phase 4's asymmetric μ/ε")
        print("    tracks. P_phase3_flux_tube awaits Phase 4 for meaningful")
        print("    pass/fail adjudication.")

    print("\n✓ Driver ran cleanly. Artifacts saved to /tmp/phase3_*.")
    sys.exit(0)
