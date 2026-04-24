"""
Phase 5e driver v2: cool-from-above with Cosserat direct-ω seeding.

Step 5b per Grant's sequence. The v1 driver (phase5e_cool_from_above.py)
ran into a coupling-bootstrapping bottleneck: K4 sector saturates under
drive (S → 0.5), but Cosserat A²_μ only reaches 0.012 because the
K4→Cosserat coupling L_c = (V²/V_SNAP²)·W_refl is multiplicative and
needs pre-existing Cosserat reflection density to pump.

**v2 mitigation:** add CosseratBeltramiSource (commit e17b8cd) alongside
the K4 autoresonant sources. Directly injects helical ω into Cosserat
sector, bypassing the bootstrap problem. Tests whether the gate CAN fire
under a combined drive + direct seed, to distinguish:
  - Is the mechanism valid (gate fires when Cosserat genuinely saturates)?
  - Is the v1 failure purely a coupling-strength issue, or deeper?

**What this tests:**
  1. Can the gate fire at all (validates mechanism)?
  2. Does cool-from-above mechanism produce Phase B firings when both
     sectors are driven into saturation then released?
  3. Does the Cosserat ω direct seed survive post-drive via topological
     protection (Kelvin persistence, doc 54_ §10.5)?

**Not valid for P_phase5 adjudication** — uses auxiliary direct-ω
seeding not in the registered drive-from-below spec. This is an
investigative variant.

Usage:
  python src/scripts/vol_1_foundations/phase5e_cool_from_above_v2.py
    → writes /tmp/phase5e_cool_from_above_v2.png
    → writes /tmp/phase5e_cool_from_above_v2.npz
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
    CosseratBeltramiSource,
    NodeResonanceObserver,
    PairNucleationGate,
    RegimeClassifierObserver,
    VacuumEngine3D,
)


@dataclass
class RunConfig:
    wavelength: float = 3.5
    amplitude_k4: float = 0.9              # K4 autoresonant drive amplitude
    amplitude_cos: float = 2.0             # Cosserat ω direct-seed amplitude
    temperature: float = 0.1
    N: int = 32
    pml: int = 4
    t_ramp_periods: float = 2.0
    t_sustain_periods: float = 13.0
    t_cooling_periods: float = 20.0
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


def run_cool_from_above_v2(cfg: RunConfig) -> dict:
    engine = VacuumEngine3D.from_args(
        N=cfg.N, pml=cfg.pml,
        temperature=cfg.temperature,
        amplitude_convention="V_SNAP",
        use_memristive_saturation=True,
    )
    period = cfg.period
    t_ramp = cfg.t_ramp_periods * period
    t_sustain = cfg.t_sustain_periods * period
    src_offset = cfg.pml + 3

    # K4 autoresonant sources (head-on collision)
    engine.add_source(AutoresonantCWSource(
        x0=src_offset, direction=(1.0, 0.0, 0.0),
        amplitude=cfg.amplitude_k4, omega=cfg.omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period * 0.5,
    ))
    engine.add_source(AutoresonantCWSource(
        x0=cfg.N - src_offset, direction=(-1.0, 0.0, 0.0),
        amplitude=cfg.amplitude_k4, omega=cfg.omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period * 0.5,
    ))

    # Cosserat direct-ω seed at center — RH Beltrami at the collision plane
    # amp=2.0 above saturation amp_sat=π/k=λ/2=1.75 for A²_μ_base~1 per
    # CosseratBeltramiSource docstring
    engine.add_source(CosseratBeltramiSource(
        x0=cfg.N // 2,                    # center of lattice
        propagation_axis=0,                # along x (same as K4 drive)
        amplitude=cfg.amplitude_cos,
        omega=cfg.omega_carrier,
        handedness="RH",
        sigma_yz=3.0,
        t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period * 0.5,
    ))

    gate = PairNucleationGate(cadence=cfg.record_cadence)
    regime_obs = RegimeClassifierObserver(cadence=cfg.record_cadence)
    node_obs = NodeResonanceObserver(cadence=cfg.record_cadence)
    engine.add_observer(gate)
    engine.add_observer(regime_obs)
    engine.add_observer(node_obs)

    S_field_history = []
    A2_mu_history = []
    S_field_cadence = max(1, cfg.record_cadence * 5)

    t0 = time.time()
    for step in range(cfg.n_outer_steps):
        engine.step()
        if engine.step_count % S_field_cadence == 0:
            S_field_history.append({
                "t": engine.time,
                "S_min": float(engine.k4.S_field[engine.k4.mask_active].min()),
                "S_mean": float(engine.k4.S_field[engine.k4.mask_active].mean()),
            })
            A2_mu_field = gate._compute_A2_mu(engine)
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

    phase_A_firings = 0
    phase_B_firings = 0
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


if __name__ == "__main__":
    print("── Phase 5e v2 — cool-from-above with direct-ω Cosserat seed ──\n")
    cfg = RunConfig()
    print(f"Config: N={cfg.N}, pml={cfg.pml}")
    print(f"        K4 amp: {cfg.amplitude_k4}·V_SNAP")
    print(f"        Cos amp: {cfg.amplitude_cos} (direct ω — above A²_μ_base saturation amp_sat≈1.75)")
    print(f"        T={cfg.temperature}, λ={cfg.wavelength}")
    print(f"        Drive: ramp={cfg.t_ramp_periods}p, sustain={cfg.t_sustain_periods}p")
    print(f"        Cool: {cfg.t_cooling_periods}p\n")

    result = run_cool_from_above_v2(cfg)
    print(f"Sim elapsed: {result['elapsed_s']:.1f} s\n")

    S_hist = result["S_field_history"]
    A2_hist = result["A2_mu_history"]
    cfg = result["config"]

    print("── K4 sector ──")
    if S_hist:
        S_min_ever = min(h["S_min"] for h in S_hist)
        print(f"S_min ever:             {S_min_ever:.4f}")

    print("\n── Cosserat sector ──")
    if A2_hist:
        A2_peak = max(h["A2_mu_max"] for h in A2_hist)
        A2_peak_entry = max(A2_hist, key=lambda h: h["A2_mu_max"])
        n_above_c1 = max(h["n_above_c1"] for h in A2_hist)
        print(f"Max A²_μ (gate C1 input):   {A2_peak:.4f}   (C1 = 0.95)")
        print(f"  Peak at t/T = {A2_peak_entry['t']/cfg.period:.2f}")
        print(f"Peak # sites A²_μ ≥ 0.95:    {n_above_c1}")

    print("\n── Gate firings ──")
    print(f"Phase A (drive):        {result['phase_A_firings']}")
    print(f"Phase B (cooling):      {result['phase_B_firings']}")
    print(f"Total:                  {result['total_firings']}")

    print("\n── Interpretation ──")
    if result['total_firings'] > 0:
        print("✓ Gate fired. Mechanism confirmed operational.")
        if result['phase_B_firings'] > 0:
            print("  ★ Phase B firings — cool-from-above mechanism produces pairs!")
    else:
        if A2_hist:
            if A2_peak >= 0.95:
                print(f"⚠ Cosserat A²_μ crossed C1 (peak {A2_peak:.3f}) but gate didn't fire.")
                print("  Likely C2 (autoresonant lock) not engaged. Investigate Ω_node tracking.")
            elif A2_peak >= 0.5:
                print(f"⚠ Cosserat A²_μ reached {A2_peak:.3f} — approaching C1 but undershot.")
                print("  Try higher amp_cos or longer sustain.")
            else:
                print(f"✗ Cosserat A²_μ only {A2_peak:.3f} even with direct seed.")
                print("  Deep issue beyond coupling weakness.")
    print("\n✓ Driver ran cleanly.")
    sys.exit(0)
