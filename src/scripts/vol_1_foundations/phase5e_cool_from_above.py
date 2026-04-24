"""
Phase 5e driver: cool-from-above pair nucleation experiment.

First empirical test of the lattice-genesis / BEMF-driven-defect-freezing
mechanism per doc 59_ §5.4-§5: initialize vacuum above yield (driven into
the Ax4 slipstream regime), then let it cool through the rupture boundary
and observe topological pair-capsule nucleation at yield-heal crossings.

**Axiom chain under test (from doc 59_ + doc 62_ §10):**
  - Ax1 K4 LC lattice provides bipartite A-B structure
  - Ax3 scale-free action sets τ_relax = ℓ_node/c minimum relaxation
  - Ax4 saturation kernel + memristive Op14 integration (doc 59_ §9)
  - BEMF-blocked topology-unwinding during yield-heal window (doc 59_ §5)
  - Interface scattering entropy per Ch 11 operator (doc 62_ §10; doc 61_
    |Γ|² = 1/2 framework)

**What's different from Phase 5 driver (phase5_pair_nucleation.py):**
  - Uses memristive Op14 K4 (commit 49917ff, opt-in via
    use_memristive_saturation=True). Stabilizes sustained supersaturation
    drive. Addresses Flag D from doc 59_.
  - Uses Cosserat-sector PML (commit 03cb9d5, automatic when pml>0).
    Enables Cosserat thermal energy to drain out of the simulation so
    cooling through yield actually happens.
  - Two-phase drive profile:
    (a) DRIVE TO SATURATION: push well above yield via autoresonant
        sources at amp=0.9·V_SNAP (above P_phase5 registration at 0.5).
        Runs for ~15 Compton periods.
    (b) COOL THROUGH YIELD: turn off sources abruptly. PML drains
        energy; lattice cools. Saturated regions retreat toward
        V < V_yield. Observe gate firings during the retreat.

**Status honesty:**
  - Cosserat-sector memristive kernels (doc 59_ §10.2) are NOT yet
    implemented. Phase 4 asymmetric S_μ/S_ε kernels run instantaneous.
    First-pass experiment acceptable; later refinement possible.
  - Not registered as P_phase5e yet (that prediction defined in doc 59_
    but not added to predictions.yaml). This is the experimental
    precursor that would generate the data for P_phase5e registration.

**Expected dynamics:**
  - Phase A (drive on, 0-15 periods): A²_total ramps up to >1, memristive
    S(t) lags saturated values, gate C1 condition may meet but gate
    typically fires at startup then goes dormant due to re-fire prevention.
  - Phase B (drive off, 15+ periods): Cosserat PML absorbs thermal/
    residual energy. Saturated regions shrink. Memristive S(t) relaxes
    toward unsaturated. **Key observable:** do gate firings occur during
    the cooling process? Where?

Usage:
  python src/scripts/vol_1_foundations/phase5e_cool_from_above.py
    → writes /tmp/phase5e_cool_from_above.png (4-panel diagnostic)
    → writes /tmp/phase5e_cool_from_above.npz (time-series)
    → exits 0 unless simulation crashes

Reference:
  - research/L3_electron_soliton/59_memristive_yield_crossing_derivation.md
  - research/L3_electron_soliton/58_cosserat_pml_derivation.md
  - research/L3_electron_soliton/62_ruptured_plasma_bh_entropy_derivation.md §10
  - commit 03cb9d5 (Cosserat PML)
  - commit 49917ff (Memristive Op14 K4)
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
    NodeResonanceObserver,
    PairNucleationGate,
    RegimeClassifierObserver,
    VacuumEngine3D,
)


@dataclass
class RunConfig:
    wavelength: float = 3.5
    amplitude: float = 0.9                 # Stress config, above P_phase5 0.5
    temperature: float = 0.1               # Thermal noise background
    N: int = 32                            # Bigger than Phase 5's N=24
    pml: int = 4                           # Cosserat PML activates automatically
    t_ramp_periods: float = 2.0
    t_sustain_periods: float = 13.0        # Drive phase
    t_cooling_periods: float = 20.0        # Cool-through-yield phase
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
            self.t_ramp_periods + self.t_sustain_periods + self.t_cooling_periods
        ) * self.period
        return int(total_time * np.sqrt(2.0)) + 1

    @property
    def drive_end_time(self) -> float:
        return (self.t_ramp_periods + self.t_sustain_periods) * self.period


def run_cool_from_above(cfg: RunConfig) -> dict:
    engine = VacuumEngine3D.from_args(
        N=cfg.N, pml=cfg.pml,
        temperature=cfg.temperature,
        amplitude_convention="V_SNAP",
        use_memristive_saturation=True,    # Phase 5.6 — stabilizes sustained drive
    )
    period = cfg.period
    t_ramp = cfg.t_ramp_periods * period
    t_sustain = cfg.t_sustain_periods * period
    src_offset = cfg.pml + 3

    # Head-on collision — identical to Phase 5 driver
    engine.add_source(AutoresonantCWSource(
        x0=src_offset, direction=(1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period * 0.5,              # Faster decay — abrupt cooling
    ))
    engine.add_source(AutoresonantCWSource(
        x0=cfg.N - src_offset, direction=(-1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period * 0.5,
    ))

    gate = PairNucleationGate(cadence=cfg.record_cadence)
    regime_obs = RegimeClassifierObserver(cadence=cfg.record_cadence)
    node_obs = NodeResonanceObserver(cadence=cfg.record_cadence)
    engine.add_observer(gate)
    engine.add_observer(regime_obs)
    engine.add_observer(node_obs)

    # Track firings vs time, segmented by phase
    phase_A_firings = 0      # During drive
    phase_B_firings = 0      # During cooling

    # Also track S_field evolution (memristive state) AND Cosserat A²_μ
    # (the gate's actual C1 input — step 5a diagnostic)
    S_field_history = []
    A2_mu_history = []
    S_field_cadence = max(1, cfg.record_cadence * 5)

    t0 = time.time()
    for step in range(cfg.n_outer_steps):
        engine.step()

        # Capture S_field + A²_μ snapshot at lower cadence
        if engine.step_count % S_field_cadence == 0:
            S_field_history.append({
                "t": engine.time,
                "S_min": float(engine.k4.S_field[engine.k4.mask_active].min()),
                "S_mean": float(engine.k4.S_field[engine.k4.mask_active].mean()),
            })
            # Compute Cosserat A²_μ directly — what the gate actually checks
            A2_mu_field = gate._compute_A2_mu(engine)
            # Mask to active Cosserat sites for statistics
            active = engine.cos.mask_alive
            if active.any():
                A2_mu_active = A2_mu_field[active]
                A2_mu_history.append({
                    "t": engine.time,
                    "A2_mu_max": float(A2_mu_active.max()),
                    "A2_mu_mean": float(A2_mu_active.mean()),
                    "n_above_c1": int((A2_mu_active >= 0.95).sum()),
                })

    elapsed = time.time() - t0

    # Segment firings by phase
    drive_end = cfg.drive_end_time
    for entry in gate.history:
        if entry["n_fired_this_step"] > 0:
            if entry["t"] < drive_end:
                phase_A_firings += entry["n_fired_this_step"]
            else:
                phase_B_firings += entry["n_fired_this_step"]

    return {
        "config": cfg,
        "elapsed_s": elapsed,
        "gate_history": gate.history,
        "regime_history": regime_obs.history,
        "node_history": node_obs.history,
        "S_field_history": S_field_history,
        "A2_mu_history": A2_mu_history,
        "phase_A_firings": phase_A_firings,
        "phase_B_firings": phase_B_firings,
        "total_firings": gate._total_firings,
        "drive_end_time": drive_end,
    }


def adjudicate(result: dict) -> dict:
    cfg = result["config"]
    period = cfg.period
    regime_hist = result["regime_history"]
    S_hist = result["S_field_history"]

    max_A2_ever = max(h["max_A2_total"] for h in regime_hist) if regime_hist else 0.0

    # S_field stats: did it dip below 0.5 (indicating significant saturation)?
    S_min_ever = min(h["S_min"] for h in S_hist) if S_hist else 1.0

    # Cooling progress: S_field at end vs during drive
    if S_hist and len(S_hist) > 5:
        S_during_drive = np.median([h["S_min"] for h in S_hist
                                     if h["t"] < result["drive_end_time"]])
        S_after_drive = np.median([h["S_min"] for h in S_hist
                                    if h["t"] >= result["drive_end_time"]])
        # Cooling happened if S rose (de-saturation) post-drive
        cooled_through_yield = S_after_drive > S_during_drive + 0.05
    else:
        S_during_drive = S_min_ever
        S_after_drive = S_min_ever
        cooled_through_yield = False

    return {
        "max_A2_ever": float(max_A2_ever),
        "S_min_ever": float(S_min_ever),
        "S_during_drive": float(S_during_drive) if S_hist else None,
        "S_after_drive": float(S_after_drive) if S_hist else None,
        "cooled_through_yield": bool(cooled_through_yield),
        "phase_A_firings": int(result["phase_A_firings"]),
        "phase_B_firings": int(result["phase_B_firings"]),
        "total_firings": int(result["total_firings"]),
    }


def render(result: dict, out: str = "/tmp/phase5e_cool_from_above.png") -> None:
    cfg = result["config"]
    period = cfg.period
    drive_end = result["drive_end_time"]

    gate_hist = result["gate_history"]
    regime_hist = result["regime_history"]
    node_hist = result["node_history"]
    S_hist = result["S_field_history"]

    if not gate_hist or not regime_hist or not S_hist:
        print("No history — skipping gif.")
        return

    t_gate = np.array([h["t"] for h in gate_hist]) / period
    n_fired = np.array([h["n_fired_this_step"] for h in gate_hist])
    n_total = np.array([h["n_nucleated_total"] for h in gate_hist])

    t_reg = np.array([h["t"] for h in regime_hist]) / period
    A2_total_max = np.array([h["max_A2_total"] for h in regime_hist])

    t_S = np.array([h["t"] for h in S_hist]) / period
    S_min = np.array([h["S_min"] for h in S_hist])
    S_mean = np.array([h["S_mean"] for h in S_hist])

    fig, axes = plt.subplots(2, 2, figsize=(15, 9))

    # Panel 1: max A²_total vs time (C1 crossing behavior)
    ax = axes[0, 0]
    ax.plot(t_reg, A2_total_max, color="#c33", lw=1.2)
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0, label="drive end")
    ax.axhline(0.95, color="#888", ls=":", lw=0.8, label="C1 threshold (0.95)")
    ax.axhline(1.0, color="#444", ls="-", lw=0.6)
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("max A²_total")
    ax.set_title("C1 behavior under drive then cool\n"
                 "(memristive K4 should stabilize amp=0.9)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 2: S_field (memristive saturation state)
    ax = axes[0, 1]
    ax.plot(t_S, S_min, color="#c33", lw=1.5, label="S_min (most saturated)")
    ax.plot(t_S, S_mean, color="#47c", lw=1.2, label="S_mean")
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0, label="drive end")
    ax.axhline(1.0, color="#888", ls=":", lw=0.8, label="unsaturated")
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("S_field value")
    ax.set_title("Memristive S(t) evolution\n(post-drive rise = cooling back to unsat)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    ax.set_ylim(-0.05, 1.1)

    # Panel 3: gate firings
    ax = axes[1, 0]
    ax.plot(t_gate, n_total, color="#333", lw=1.5, label="cumulative")
    if n_fired.max() > 0:
        ax.bar(t_gate, n_fired, width=0.5, color="#c33", alpha=0.5, label="per step")
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0)
    ax.axvspan(0, drive_end / period, color="#fde", alpha=0.3, label="drive")
    ax.axvspan(drive_end / period, t_gate[-1] if t_gate.size else 1,
               color="#def", alpha=0.3, label="cooling")
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("pair nucleations")
    ax.set_title("Gate firings (Phase A vs B)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    # Panel 4: Ω_node resonance tracking
    ax = axes[1, 1]
    t_node = np.array([h["t"] for h in node_hist]) / period
    omega_ratio_min = np.array([h["omega_ratio_min"] for h in node_hist])
    ax.plot(t_node, omega_ratio_min, color="#47c", lw=1.2)
    ax.axvline(drive_end / period, color="#2a7", ls="--", lw=1.0, label="drive end")
    ax.axhline(1.0, color="#888", ls=":", lw=0.8, label="unsaturated")
    ax.set_xlabel("time (Compton periods)")
    ax.set_ylabel("Ω_node/ω_0 (min)")
    ax.set_title("Duffing softening\n(min across lattice)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    plt.suptitle(
        f"Phase 5e cool-from-above (N={cfg.N}, amp={cfg.amplitude}·V_SNAP, memristive K4 + Cosserat PML)",
        fontsize=12,
    )
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


def save_npz(result: dict, out: str = "/tmp/phase5e_cool_from_above.npz") -> None:
    gate_hist = result["gate_history"]
    regime_hist = result["regime_history"]
    S_hist = result["S_field_history"]
    if not gate_hist:
        return
    np.savez(
        out,
        t_gate=np.array([h["t"] for h in gate_hist]),
        n_fired=np.array([h["n_fired_this_step"] for h in gate_hist]),
        n_total=np.array([h["n_nucleated_total"] for h in gate_hist]),
        max_A2_total=np.array([h["max_A2_total"] for h in regime_hist]) if regime_hist else np.array([]),
        t_S=np.array([h["t"] for h in S_hist]),
        S_min=np.array([h["S_min"] for h in S_hist]),
        S_mean=np.array([h["S_mean"] for h in S_hist]),
    )
    print(f"Saved {out}")


if __name__ == "__main__":
    print("── Phase 5e cool-from-above driver ──\n")
    cfg = RunConfig()
    print(f"Config: N={cfg.N}, pml={cfg.pml} (Cosserat PML active)")
    print(f"        amp={cfg.amplitude}·V_SNAP (STRESS — above P_phase5's 0.5)")
    print(f"        T={cfg.temperature}, λ={cfg.wavelength}")
    print(f"        Drive: ramp={cfg.t_ramp_periods}p, sustain={cfg.t_sustain_periods}p")
    print(f"        Cool:  {cfg.t_cooling_periods}p post-drive")
    print(f"        use_memristive_saturation=True (K4 sector only — Cosserat still instant)")
    print(f"        n_steps={cfg.n_outer_steps}\n")

    result = run_cool_from_above(cfg)
    print(f"Sim elapsed: {result['elapsed_s']:.1f} s\n")

    verdict = adjudicate(result)
    print("── Diagnostic summary ──")
    print(f"Max A²_total ever:      {verdict['max_A2_ever']:.4f}  (> 1.0 = saturated)")
    print(f"Min S_field ever:       {verdict['S_min_ever']:.4f}  (< 0.5 = near rupture)")
    if verdict['S_during_drive'] is not None:
        print(f"S_min during drive:     {verdict['S_during_drive']:.4f}")
        print(f"S_min after drive:      {verdict['S_after_drive']:.4f}")
        delta = verdict['S_after_drive'] - verdict['S_during_drive']
        trend = "↑ cooled" if delta > 0.01 else "→ no change" if abs(delta) < 0.01 else "↓ got more saturated?!"
        print(f"                        Δ = {delta:+.4f}  [{trend}]")
    print(f"Cooled through yield:   {verdict['cooled_through_yield']}")
    print()
    print(f"Phase A firings (drive):    {verdict['phase_A_firings']}")
    print(f"Phase B firings (cooling):  {verdict['phase_B_firings']}")
    print(f"Total firings:              {verdict['total_firings']}")

    # Cosserat A²_μ diagnostic — step 5a: is Cosserat also saturating?
    A2_mu_hist = result.get("A2_mu_history", [])
    if A2_mu_hist:
        A2_mu_peak = max(h["A2_mu_max"] for h in A2_mu_hist)
        A2_mu_peak_time = max((h for h in A2_mu_hist), key=lambda h: h["A2_mu_max"])["t"]
        n_above_c1_peak = max(h["n_above_c1"] for h in A2_mu_hist)
        print(f"\n── Cosserat A²_μ diagnostic (step 5a) ──")
        print(f"Max A²_μ ever (gate's C1 input):   {A2_mu_peak:.4f}  (C1 threshold: 0.95)")
        print(f"  Reached at t/T = {A2_mu_peak_time/cfg.period:.2f}")
        print(f"Peak # sites with A²_μ ≥ 0.95:     {n_above_c1_peak}")
        if A2_mu_peak < 0.5:
            print(f"  → Cosserat A²_μ stays LINEAR even though K4 saturates.")
            print(f"    K4→Cosserat coupling too weak, OR coupling has unit issue")
            print(f"    analogous to Flag-5e-A. Step 5b needs Cosserat-side fix.")
        elif A2_mu_peak < 0.95:
            print(f"  → Cosserat A²_μ reaches {A2_mu_peak:.2f} — approaching C1 but undershoots.")
            print(f"    Likely just needs stronger drive or larger N.")
        else:
            print(f"  → Cosserat A²_μ crosses C1. Gate should fire if C2 also met.")

    save_npz(result)
    render(result)

    print("\n── Interpretation ──")
    if verdict['max_A2_ever'] > 1.5:
        print(f"⚠ A²_total reached {verdict['max_A2_ever']:.2f} — even with memristive K4, dynamics")
        print(f"  exceeded the saturation regime. Check for divergence or if engine went supercritical.")
    elif verdict['max_A2_ever'] < 0.8:
        print(f"⚠ Max A² only {verdict['max_A2_ever']:.3f} — didn't reach saturation.")
        print(f"  Cool-from-above mechanism can't be tested if system never entered slipstream.")
        print(f"  Try higher amp or larger N.")
    else:
        print(f"✓ Max A²={verdict['max_A2_ever']:.3f} — reached saturation regime.")

    if verdict['phase_A_firings'] > 0 or verdict['phase_B_firings'] > 0:
        print(f"✓ Gate fired — {verdict['phase_A_firings']} during drive, "
              f"{verdict['phase_B_firings']} during cooling.")
        if verdict['phase_B_firings'] > 0:
            print("  ★ PHASE B FIRINGS observed — cool-from-above mechanism produced pair(s)!")
            print("    This is the first empirical evidence for doc 59_'s yield-heal BEMF mechanism.")
    else:
        print("✗ Gate never fired. Possible reasons:")
        print("  1. C1 threshold (A²_μ ≥ 0.95) not reached despite saturated state")
        print("  2. C2 (autoresonant lock) doesn't engage when drive is off")
        print("  3. Memristive K4 lag prevents quick C1 satisfaction")
        if verdict['cooled_through_yield']:
            print("  - Cooling DID happen (S_field recovered toward 1)")
            print("  - But gate mechanism may not trigger during cooling without active drive")

    print("\n✓ Driver ran cleanly. Artifacts saved to /tmp/phase5e_*.")
    sys.exit(0)
