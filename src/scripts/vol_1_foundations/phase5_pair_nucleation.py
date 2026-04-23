"""
Phase 5 driver: pair nucleation under collision drive.

Runs the PairNucleationGate observer on a head-on AutoresonantCWSource
collision at amp = 0.5·V_SNAP (per P_phase5_nucleation registration),
records gate firings + C1/C2 diagnostics, then — after the drive
switches off — tracks vortex-pair persistence at the injection sites.

**What this tests (two distinct claims):**

  (1) **Primary: P_phase5_nucleation.** Under autoresonant drive at
      amp=0.5·V_SNAP, ω=ω_C, does the gate fire within 50 Compton
      periods? Falsification: never fires while C1 is met, or fires
      aggressively (> 1 pair / period).

  (2) **Secondary (Kelvin discrete-lattice test).** If the gate fires,
      does the injected Beltrami pair persist ≥ 10 Compton periods
      after drive shutoff? Kelvin's 1867 "On Vortex Atoms" claim is
      that knotted vortices in a frictionless fluid cannot unravel
      (topological protection, "multiple continuity"). The AVE Bingham-
      plastic vacuum has a frictionless slipstream regime only INSIDE
      the saturated capsule (Vol 4 Ch 1:189-203). This driver checks
      whether the point-rotation Beltrami profile survives ≥ 10 Compton
      periods post-drive at discrete lattice resolution. If no: upgrade
      injection profile to Hopf fibration / (2,3) torus-knot per
      STAGE6_V4_HANDOFF §9 G-13.

**Scope honesty:**
  - N=24 lattice — coarse enough that continuum Meissner thresholds
    (doc 54_ §6: S_μ<0.1 across a domain) don't resolve at N=24.
    Firing detection is still valid since the gate uses per-site A²_μ,
    which IS meaningful at any N. Persistence is the open question.
  - Amplitude 0.5·V_SNAP might not drive A²_μ to 1.0 at collision
    peak in this engine size. Record max A²_μ and adjudicate honestly.

Usage:
  python src/scripts/vol_1_foundations/phase5_pair_nucleation.py
    → writes /tmp/phase5_pair_nucleation.png
    → writes /tmp/phase5_pair_nucleation.npz
    → exits 0 unless the simulation crashes

Reference:
  - src/ave/topological/vacuum_engine.py::PairNucleationGate
  - research/L3_electron_soliton/54_pair_production_axiom_derivation.md §7
  - manuscript/predictions.yaml::P_phase5_nucleation
  - Kelvin 1867 "On Vortex Atoms" (topological protection)
"""
from __future__ import annotations

import argparse
import sys
import time
from dataclasses import dataclass

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.topological.vacuum_engine import (
    AutoresonantCWSource,
    NodeResonanceObserver,
    PairNucleationGate,
    RegimeClassifierObserver,
    VacuumEngine3D,
)


@dataclass
class RunConfig:
    wavelength: float = 3.5
    amplitude: float = 0.5           # V_SNAP units (P_phase5 registration)
    temperature: float = 0.1
    N: int = 24
    pml: int = 4
    # Drive envelope: ramp → sustain → decay → post-drive observation
    t_ramp_periods: float = 3.0
    t_sustain_periods: float = 20.0
    t_observe_post_drive_periods: float = 15.0
    record_cadence: int = 2

    @property
    def omega_carrier(self) -> float:
        return 2.0 * np.pi / self.wavelength

    @property
    def period(self) -> float:
        return 2.0 * np.pi / self.omega_carrier

    @property
    def n_outer_steps(self) -> int:
        total_time = (
            self.t_ramp_periods
            + self.t_sustain_periods
            + self.t_observe_post_drive_periods
        ) * self.period
        return int(total_time * np.sqrt(2.0)) + 1

    @property
    def drive_end_time(self) -> float:
        # Drive envelope hits zero at end of sustain + decay
        return (self.t_ramp_periods + self.t_sustain_periods + 1.0) * self.period


def run_collision(cfg: RunConfig) -> dict:
    engine = VacuumEngine3D.from_args(
        N=cfg.N, pml=cfg.pml,
        temperature=cfg.temperature,
        amplitude_convention="V_SNAP",
    )
    period = cfg.period
    t_ramp = cfg.t_ramp_periods * period
    t_sustain = cfg.t_sustain_periods * period
    src_offset = cfg.pml + 3

    # Head-on autoresonant CW pair, decay=1 period
    engine.add_source(AutoresonantCWSource(
        x0=src_offset, direction=(1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period,
    ))
    engine.add_source(AutoresonantCWSource(
        x0=cfg.N - src_offset, direction=(-1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period,
    ))

    gate = PairNucleationGate(cadence=cfg.record_cadence)
    regime_obs = RegimeClassifierObserver(cadence=cfg.record_cadence)
    node_obs = NodeResonanceObserver(cadence=cfg.record_cadence)
    engine.add_observer(gate)
    engine.add_observer(regime_obs)
    engine.add_observer(node_obs)

    # Sample |ω|² at any fired injection sites in a separate post-step hook
    omega_sq_at_fired_sites: list[list[float]] = []  # [ [site0, site1, ...], ... ]
    fired_site_list: list[tuple[int, int, int]] = []

    t0 = time.time()
    # Manual stepping so we can record per-site |ω|² at injection sites
    for _ in range(cfg.n_outer_steps):
        engine.step()
        if engine.step_count % cfg.record_cadence != 0:
            continue
        # Refresh fired-site list from latest gate history (idempotent)
        if gate.history:
            latest = gate.history[-1]
            if latest["n_fired_this_step"] > 0:
                for key in latest["fired_bonds"]:
                    Ai, Aj, Ak, port = key
                    p = PairNucleationGate._PORT_VECTORS[port].astype(int)
                    fired_site_list.append((Ai, Aj, Ak))
                    fired_site_list.append(
                        (Ai + p[0], Aj + p[1], Ak + p[2])
                    )
        # Record |ω|² at each known fired site
        row = []
        for site in fired_site_list:
            w_here = engine.cos.omega[site[0], site[1], site[2], :]
            row.append(float(np.sum(w_here * w_here)))
        omega_sq_at_fired_sites.append(row)
    elapsed = time.time() - t0

    return {
        "config": cfg,
        "elapsed_s": elapsed,
        "gate_history": gate.history,
        "regime_history": regime_obs.history,
        "node_history": node_obs.history,
        "omega_sq_at_fired_sites": omega_sq_at_fired_sites,
        "fired_site_list": fired_site_list,
        "drive_end_time": cfg.drive_end_time,
        "total_firings": gate._total_firings,
    }


def adjudicate(result: dict) -> dict:
    cfg = result["config"]
    period = cfg.period
    drive_end = result["drive_end_time"]

    gate_hist = result["gate_history"]
    regime_hist = result["regime_history"]

    if not gate_hist:
        return {"verdict": "NO-DATA"}

    t_gate = np.array([h["t"] for h in gate_hist])
    n_fired = np.array([h["n_fired_this_step"] for h in gate_hist])
    n_total = np.array([h["n_nucleated_total"] for h in gate_hist])

    # First firing time
    fired_mask = n_fired > 0
    first_fire_t = float(t_gate[fired_mask][0]) if fired_mask.any() else None
    first_fire_periods = (
        first_fire_t / period if first_fire_t is not None else None
    )

    # Max firing rate (pairs per period)
    # Bin firings into 1-period windows post-ramp
    total_periods = (t_gate[-1] / period) if t_gate.size else 0.0
    if total_periods >= 1.0 and n_fired.sum() > 0:
        period_bins = int(np.floor(total_periods)) + 1
        firings_per_period = np.zeros(period_bins)
        for t, k in zip(t_gate, n_fired):
            bin_idx = int(np.floor(t / period))
            if 0 <= bin_idx < period_bins:
                firings_per_period[bin_idx] += k
        max_rate = float(firings_per_period.max())
    else:
        max_rate = 0.0

    # Max A²_μ achieved anywhere (via regime observer's A²_total as a proxy
    # in symmetric-saturation; Phase 4 asymmetric's A²_μ isn't exposed on
    # RegimeClassifier, so we use A²_total as a floor)
    max_A2 = float(np.max(
        [h["max_A2_total"] for h in regime_hist]
    )) if regime_hist else 0.0

    # Persistence: for each fired site, |ω|² trajectory post-drive
    fired_sites = result["fired_site_list"]
    omega_sq_traj = result["omega_sq_at_fired_sites"]
    # Convert ragged-list into per-site trajectories (each site appears once
    # in fired_site_list; traj starts once the site was added)
    persistence_periods = None
    if fired_sites and any(len(r) > 0 for r in omega_sq_traj):
        # Find trajectory for the FIRST fired site (index 0)
        traj_times = []
        traj_omega_sq = []
        for step_idx, row in enumerate(omega_sq_traj):
            if len(row) == 0:
                continue
            # step_idx maps back to a gate_history entry (same cadence)
            if step_idx < len(t_gate):
                traj_times.append(t_gate[step_idx])
                traj_omega_sq.append(row[0])  # first fired site
        if len(traj_times) >= 2:
            traj_times = np.array(traj_times)
            traj_omega_sq = np.array(traj_omega_sq)
            # Post-drive window
            post_mask = traj_times >= drive_end
            if post_mask.sum() > 1 and traj_omega_sq[post_mask].max() > 0:
                post_times = traj_times[post_mask]
                post_w2 = traj_omega_sq[post_mask]
                peak = post_w2.max()
                half = 0.5 * peak
                below = np.where(post_w2 < half)[0]
                if below.size == 0:
                    # Never decayed below half during observation
                    persistence_periods = (
                        float(post_times[-1] - drive_end) / period
                    )
                else:
                    first_below = below[0]
                    persistence_periods = (
                        float(post_times[first_below] - drive_end) / period
                    )

    # Verdict logic (P_phase5 registration)
    registered_window_periods = 50.0
    if first_fire_periods is None:
        primary_verdict = "NO-FIRE"
    elif first_fire_periods > registered_window_periods:
        primary_verdict = "LATE-FIRE"
    elif max_rate > 1.0:
        primary_verdict = "OVERFIRE"
    else:
        primary_verdict = "PASS"

    return {
        "verdict": "OK",
        "primary_verdict": primary_verdict,
        "first_fire_periods": first_fire_periods,
        "max_rate_per_period": max_rate,
        "total_firings": int(n_total[-1]) if n_total.size else 0,
        "max_A2_total_achieved": max_A2,
        "persistence_periods_first_site": persistence_periods,
        "drive_end_time": drive_end,
        "drive_end_periods": drive_end / period,
        "total_observation_periods": float(t_gate[-1] / period) if t_gate.size else 0.0,
    }


def render(result: dict, out: str = "/tmp/phase5_pair_nucleation.png") -> None:
    cfg = result["config"]
    period = cfg.period
    drive_end = result["drive_end_time"]

    gate_hist = result["gate_history"]
    regime_hist = result["regime_history"]
    node_hist = result["node_history"]

    if not gate_hist or not regime_hist:
        return

    t_gate = np.array([h["t"] for h in gate_hist]) / period
    n_fired = np.array([h["n_fired_this_step"] for h in gate_hist])
    n_total = np.array([h["n_nucleated_total"] for h in gate_hist])

    t_reg = np.array([h["t"] for h in regime_hist]) / period
    A2_total_max = np.array([h["max_A2_total"] for h in regime_hist])

    t_node = np.array([h["t"] for h in node_hist]) / period
    omega_ratio_min = np.array([h["omega_ratio_min"] for h in node_hist])

    fig, axes = plt.subplots(2, 2, figsize=(15, 9))

    # Panel 1: max A²_total vs time (C1 approach)
    ax = axes[0, 0]
    ax.plot(t_reg, A2_total_max, color="#c33", lw=1.2)
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0, label="drive end")
    ax.axhline(0.95, color="#888", ls=":", lw=0.8, label="sat_frac=0.95")
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("max A²_total")
    ax.set_title("C1 approach: max saturation vs time")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 2: omega_ratio_min (C2 approach — Duffing softening)
    ax = axes[0, 1]
    ax.plot(t_node, omega_ratio_min, color="#47c", lw=1.2)
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0, label="drive end")
    ax.axhline(1.0, color="#888", ls=":", lw=0.8, label="unsaturated")
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("Ω_node/ω_0  (min across lattice)")
    ax.set_title("C2 approach: Duffing softening at hottest site")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 3: gate firings
    ax = axes[1, 0]
    ax.plot(t_gate, n_total, color="#333", lw=1.5, label="cumulative")
    ax.bar(t_gate, n_fired, width=0.3, color="#c33", alpha=0.5, label="per step")
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0)
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("pair nucleations")
    ax.set_title("PairNucleationGate firings")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 4: |ω|² at first fired injection site (persistence)
    ax = axes[1, 1]
    fired_sites = result["fired_site_list"]
    omega_sq_traj = result["omega_sq_at_fired_sites"]
    if fired_sites and any(len(r) > 0 for r in omega_sq_traj):
        traj_t = []
        traj_w = []
        for step_idx, row in enumerate(omega_sq_traj):
            if len(row) == 0 or step_idx >= len(t_gate):
                continue
            traj_t.append(t_gate[step_idx])
            traj_w.append(row[0])
        ax.plot(traj_t, traj_w, color="#a63", lw=1.2)
        ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0,
                   label="drive end")
        ax.axhline(2.0, color="#888", ls=":", lw=0.8, label="|ω|²=2 (injection)")
        ax.set_xlabel("time (Compton periods)")
        ax.set_ylabel("|ω|² at first-fired A-site")
        ax.set_title("Beltrami persistence (Kelvin discrete-lattice test)")
        ax.legend(fontsize=9); ax.grid(alpha=0.3)
    else:
        ax.text(0.5, 0.5, "No firings recorded\n(nothing to track for persistence)",
                ha="center", va="center", transform=ax.transAxes, fontsize=11)
        ax.set_title("Beltrami persistence (no data)")

    plt.suptitle(
        f"Phase 5: Pair nucleation under collision drive "
        f"(λ={cfg.wavelength}, amp={cfg.amplitude}·V_SNAP, T={cfg.temperature}, N={cfg.N})",
        fontsize=12,
    )
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


def save_npz(result: dict, out: str = "/tmp/phase5_pair_nucleation.npz") -> None:
    gate_hist = result["gate_history"]
    if not gate_hist:
        return
    np.savez(
        out,
        t_gate=np.array([h["t"] for h in gate_hist]),
        n_fired=np.array([h["n_fired_this_step"] for h in gate_hist]),
        n_nucleated_total=np.array([h["n_nucleated_total"] for h in gate_hist]),
        max_A2_total=np.array(
            [h["max_A2_total"] for h in result["regime_history"]]
        ),
        omega_ratio_min=np.array(
            [h["omega_ratio_min"] for h in result["node_history"]]
        ),
    )
    print(f"Saved {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Phase 5 pair-nucleation driver"
    )
    parser.add_argument(
        "--stress", action="store_true",
        help=(
            "Stress config: amp=0.8·V_SNAP (above registered spec) to verify "
            "end-to-end gate firing + Beltrami persistence. Not for P_phase5 "
            "adjudication — use default for that."
        ),
    )
    args = parser.parse_args()

    print("── Phase 5 driver: pair nucleation under autoresonant collision ──\n")
    cfg = RunConfig()
    if args.stress:
        cfg.amplitude = 0.8
        print("[STRESS MODE] amp=0.8·V_SNAP (above P_phase5 registration);")
        print("              verifying gate firing + persistence end-to-end.\n")
    print(f"Config: λ={cfg.wavelength}, T={cfg.temperature}, "
          f"amp={cfg.amplitude}·V_SNAP")
    print(f"N={cfg.N}, pml={cfg.pml}, n_steps={cfg.n_outer_steps}")
    print(f"Drive envelope: ramp={cfg.t_ramp_periods}p, "
          f"sustain={cfg.t_sustain_periods}p, "
          f"post={cfg.t_observe_post_drive_periods}p")
    print("(Expected runtime ~3-5 min)\n")

    result = run_collision(cfg)
    print(f"Sim elapsed: {result['elapsed_s']:.1f} s")
    print(f"Total firings:             {result['total_firings']}\n")

    verdict = adjudicate(result)

    print("── P_phase5_nucleation adjudication ──")
    print(f"Max A²_total (proxy for A²_μ peak):  {verdict['max_A2_total_achieved']:.4f}")
    print(f"Drive end:                           {verdict['drive_end_periods']:.1f} periods")
    print(f"Total observation window:            {verdict['total_observation_periods']:.1f} periods")
    if verdict["first_fire_periods"] is not None:
        print(f"First firing at:                     {verdict['first_fire_periods']:.2f} periods")
    else:
        print(f"First firing at:                     NEVER (within window)")
    print(f"Max firing rate:                     {verdict['max_rate_per_period']:.3f} pairs/period")
    print(f"Total pairs nucleated:               {verdict['total_firings']}")
    if verdict["persistence_periods_first_site"] is not None:
        print(
            f"Beltrami persistence (first site):   "
            f"{verdict['persistence_periods_first_site']:.2f} periods post-drive"
        )
    else:
        print(f"Beltrami persistence:                N/A (no firings or no trajectory)")

    suffix = "_stress" if args.stress else ""
    save_npz(result, out=f"/tmp/phase5_pair_nucleation{suffix}.npz")
    render(result, out=f"/tmp/phase5_pair_nucleation{suffix}.png")

    print(f"\n── Primary verdict: {verdict['primary_verdict']} ──")
    if verdict["primary_verdict"] == "PASS":
        print("  ✓ Gate fired within 50 Compton periods, rate ≤ 1/period.")
        print("  P_phase5_nucleation passes on this run.")
    elif verdict["primary_verdict"] == "NO-FIRE":
        print("  ⚠ Gate never fired. Check that C1 was reachable at this amp:")
        print(f"    max A²_total = {verdict['max_A2_total_achieved']:.3f}")
        print(f"    sat_frac = 0.95 threshold")
        if verdict["max_A2_total_achieved"] < 0.95:
            print("  → C1 never met at this resolution/amp; bigger N or higher amp needed.")
        else:
            print("  → C1 was met but C2 (autoresonant lock within δ_lock=α·ω) did not")
            print("    engage. Possible causes: K_drift=0.5 shift too strong, or")
            print("    PLL not converging within observation window.")
    elif verdict["primary_verdict"] == "LATE-FIRE":
        print(f"  ⚠ Gate fired but at {verdict['first_fire_periods']:.1f} periods > 50 window.")
        print("  P_phase5_nucleation mild-fail — may indicate engine size / resolution.")
    elif verdict["primary_verdict"] == "OVERFIRE":
        print(f"  ✗ Gate fired at rate {verdict['max_rate_per_period']:.2f}/period > 1.")
        print("  P_phase5_nucleation fails (nucleation too aggressive) —")
        print("  gate thresholds need to be tightened.")

    if verdict["persistence_periods_first_site"] is not None:
        persist_p = verdict["persistence_periods_first_site"]
        print(f"\n── Secondary (Kelvin topological-protection) ──")
        if persist_p >= 10.0:
            print(f"  ✓ Beltrami pair persisted {persist_p:.1f} periods ≥ 10 target.")
            print("    Kelvin's topological-protection claim holds at this lattice scale")
            print("    for the point-rotation Beltrami profile.")
        else:
            print(f"  ⚠ Beltrami pair persisted only {persist_p:.1f} periods < 10 target.")
            print("    Indicates point-rotation Beltrami is NOT stable at discrete")
            print("    lattice resolution. Per STAGE6_V4_HANDOFF §9 G-13: upgrade")
            print("    injection profile to localized Hopf fibration or (2,3) torus-")
            print("    knot for true topological protection.")

    print("\n✓ Driver ran cleanly. Artifacts saved to /tmp/phase5_*.")
    sys.exit(0)
