"""Move 5 — Single-electron self-consistent orbit hunt at corpus GT.

Per `P_phase6_self_consistent_orbit_hunt` (frozen at this commit).

Hypothesis: the corpus (2,3) electron is a self-stable NONLINEAR standing-wave
orbit at corpus GT (R=10, r=R/φ² ≈ 3.82). Round 7 tested:
  - Linearized eigenmodes around static V=0 seed (V-block, Cos-block) → Mode III
  - Driven CW response at single bond / bond cluster → Mode III-spatial
  - Pair injection (R7.2, G-13 (2,3)/Hopf) → dissolves at Beltrami timescale

NONE tested SINGLE-electron self-consistent orbit at corpus GT WITHOUT external
drive. If the orbit is nonlinear self-trapped (only stable at finite amplitude),
linearization around any static seed necessarily misses it. Move 5 is the
direct time-domain test of corpus's actual standing-wave claim.

METHODOLOGY:
  Seed both V_inc (corpus (2,3) voltage ansatz at amp ≈ 0.14 → peak v_total
  ≈ 0.5·V_SNAP, mid Regime II, saturation engaged) AND ω (corpus (2,3)
  hedgehog at peak |ω| = 0.3π via A26 amplitude scale).

  The phase-quadrature pattern in initialize_2_3_voltage_ansatz (cos on
  ports 0,1; sin on ports 2,3) corresponds to one phase of the proposed
  standing-wave cycle. The two seeds together encode the joint (V_inc, ω)
  state at one instant of a hypothetical periodic orbit.

  Engine: VacuumEngine3D at N=32, A28 + Cosserat self-terms (post-Round-6
  default). NO external drive — pure self-dynamics. Run 200 Compton periods
  (= 200·2π natural-time-units, ≈ 1777 steps at dt = 1/√2).

  Sample at t = {0, 5, 10, 25, 50, 100, 150, 200} Compton periods:
    - peak |ω| (max over lattice of ‖ω(x)‖)
    - peak |V_inc| (max over lattice of ‖V_inc(x, :)‖)
    - c via engine.cos.extract_crossing_count() (corpus-canonical Op10)
    - shell-localized ω-energy fraction (sanity diagnostic)

ADJUDICATION (4-mode):
  Mode I-orbit:   peak |ω|(t=200) ≥ 0.80·peak |ω|(t=0)        [persistence]
                  AND c = 3 at every sample with t ≥ 10           [topology]
                  → CORPUS VINDICATED. Single-electron orbit IS a self-
                    stable nonlinear soliton at corpus GT. R7.1 eigsolve
                    Mode III was correct (no LINEAR mode) but missed the
                    NONLINEAR self-trapped orbit.
  Mode II-orbit:  peak |ω|(t=200) ≥ 0.50·peak |ω|(t=0)
                  AND c ≠ 3 at any sample with t ≥ 10
                  → orbit exists but topology drifts; not corpus (2,3)
  Mode III-orbit: peak |ω|(t=200) < 0.50·peak |ω|(t=0)
                  → orbit dissolves; corpus single-electron NOT self-stable
                    at corpus GT under engine self-dynamics
  Mode IV-orbit:  persistence ∈ [0.50, 0.80) AND c = 3 throughout post-transient
                  → marginally stable; topology preserved but amplitude
                    decays; warrants longer-time investigation
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.vacuum_engine import VacuumEngine3D
from tlm_electron_soliton_eigenmode import initialize_2_3_voltage_ansatz


# ─── Constants per pred ───────────────────────────────────────────────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI
ALPHA = 1.0 / 137.036

# Lattice
N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ                      # ≈ 3.82

# Seeds (corpus GT geometry)
A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)       # peak |ω| = 0.3π
GT_PEAK_OMEGA = 0.3 * np.pi
A26_GUARD_LOW = 0.85 * GT_PEAK_OMEGA
A26_GUARD_HIGH = 1.15 * GT_PEAK_OMEGA
V_AMP_INIT = 0.14                                # peak v_total ≈ 0.5·V_SNAP, mid Regime II

# Topology target (corpus-canonical via Op10, Doc 07_)
TOPOLOGY_TARGET_C = 3

# Time evolution
OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
N_PERIODS_TOTAL = 200.0
DT = 1.0 / np.sqrt(2.0)
N_STEPS = int(N_PERIODS_TOTAL * COMPTON_PERIOD / DT) + 1

# Sample at these Compton-period marks (post-transient at 10 periods)
SAMPLE_PERIODS = [0.0, 5.0, 10.0, 25.0, 50.0, 100.0, 150.0, 200.0]

# Adjudication thresholds
PERSISTENCE_MODE_I = 0.80
PERSISTENCE_MODE_II_III = 0.50

OUTPUT_JSON = Path(__file__).parent / "r8_self_consistent_orbit_hunt_results.json"


def build_engine():
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_corpus_2_3_joint(engine):
    """Seed both V_inc and ω with corpus (2,3) ansatz at corpus GT."""
    # ω sector: corpus (2,3) hedgehog at A26-canonical 0.3π peak
    engine.cos.initialize_electron_2_3_sector(
        R_target=R_ANCHOR, r_target=R_MINOR,
        use_hedgehog=True, amplitude_scale=A26_AMP_SCALE,
    )
    # V_inc sector: corpus (2,3) chiral-phasor voltage ansatz
    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_ANCHOR, r=R_MINOR, amplitude=V_AMP_INIT,
    )


def a26_guard_omega(engine):
    peak = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    if not (A26_GUARD_LOW <= peak <= A26_GUARD_HIGH):
        raise AssertionError(
            f"A26 guard FAILED: peak |ω|={peak:.4f} not in "
            f"[{A26_GUARD_LOW:.4f}, {A26_GUARD_HIGH:.4f}]"
        )
    return peak


def measure_state(engine):
    """Snapshot of orbit observables."""
    omega = np.asarray(engine.cos.omega)
    v_inc = np.asarray(engine.k4.V_inc)

    peak_omega = float(np.linalg.norm(omega, axis=-1).max())
    peak_vinc = float(np.linalg.norm(v_inc, axis=-1).max())
    v_total_peak = float(np.sqrt(np.sum(v_inc ** 2, axis=-1)).max())

    c = int(engine.cos.extract_crossing_count())

    # Shell-localized ω-energy fraction (sanity diagnostic)
    nx = engine.cos.nx
    cx = (nx - 1) / 2.0
    i, j, k = np.indices((nx, nx, nx))
    rho_xy = np.sqrt((i - cx) ** 2 + (j - cx) ** 2)
    rho_tube = np.sqrt((rho_xy - R_ANCHOR) ** 2 + (k - cx) ** 2)
    shell_mask = rho_tube < (1.5 * R_MINOR)
    omega_energy = np.sum(omega ** 2, axis=-1)
    e_shell = float(omega_energy[shell_mask].sum())
    e_total = float(omega_energy.sum())
    shell_frac = e_shell / max(e_total, 1e-30)

    return {
        "peak_omega": peak_omega,
        "peak_vinc": peak_vinc,
        "v_total_peak": v_total_peak,
        "c": c,
        "shell_frac": shell_frac,
    }


def main():
    print("=" * 78, flush=True)
    print(f"  Move 5 — Single-electron self-consistent orbit hunt at corpus GT")
    print(f"  P_phase6_self_consistent_orbit_hunt")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, pml={PML}")
    print(f"  Corpus GT: R={R_ANCHOR}, r={R_MINOR:.4f} (R/φ²)")
    print(f"  Seed ω: peak {GT_PEAK_OMEGA:.4f} via A26 scale {A26_AMP_SCALE:.4f}")
    print(f"  Seed V_inc: amp={V_AMP_INIT} → peak v_total ~0.5·V_SNAP (Regime II)")
    print(f"  Evolution: {N_PERIODS_TOTAL} Compton periods, NO external drive")
    print(f"  Adjudication thresholds: I ≥ {PERSISTENCE_MODE_I}, II/III ≥ "
          f"{PERSISTENCE_MODE_II_III}, c target = {TOPOLOGY_TARGET_C}")
    print()

    engine = build_engine()
    seed_corpus_2_3_joint(engine)
    omega_peak_init = a26_guard_omega(engine)
    print(f"  A26 guard OK (peak |ω|_0 = {omega_peak_init:.4f})")

    initial_state = measure_state(engine)
    print(f"  Initial: peak |ω|={initial_state['peak_omega']:.4f}, "
          f"peak v_total={initial_state['v_total_peak']:.4f}, "
          f"c={initial_state['c']}, shell_frac={initial_state['shell_frac']:.4f}")
    print()

    samples = [{"t_period": 0.0, "step": 0, **initial_state}]
    sample_steps = sorted({int(p * COMPTON_PERIOD / DT) for p in SAMPLE_PERIODS if p > 0})

    print(f"  Running {N_STEPS} steps...")
    t0 = time.time()
    last_progress = t0
    for step in range(1, N_STEPS + 1):
        engine.step()
        if step in sample_steps:
            t_period = step * DT / COMPTON_PERIOD
            state = measure_state(engine)
            samples.append({"t_period": float(t_period), "step": int(step), **state})
            print(f"    t={t_period:6.1f} P  step={step:5d}  "
                  f"peak |ω|={state['peak_omega']:.4f}  "
                  f"peak v_total={state['v_total_peak']:.4f}  "
                  f"c={state['c']}  shell_frac={state['shell_frac']:.4f}",
                  flush=True)
            last_progress = time.time()
        elif (time.time() - last_progress) > 30.0:
            t_period = step * DT / COMPTON_PERIOD
            print(f"    [progress] t={t_period:6.1f} P  step={step:5d}  "
                  f"elapsed {time.time() - t0:.1f}s",
                  flush=True)
            last_progress = time.time()
    elapsed = time.time() - t0
    print(f"  Elapsed: {elapsed:.1f}s")
    print()

    # ─── Adjudication ─────────────────────────────────────────────────────────
    final_state = samples[-1]
    persistence = final_state['peak_omega'] / max(omega_peak_init, 1e-30)

    post_transient_samples = [s for s in samples if s['t_period'] >= 10.0]
    c_post_transient = [s['c'] for s in post_transient_samples]
    topology_preserved = all(c == TOPOLOGY_TARGET_C for c in c_post_transient)

    print("=" * 78, flush=True)
    print("  Adjudication")
    print("=" * 78, flush=True)
    print(f"  Persistence: peak |ω|(t={final_state['t_period']:.0f}P) / peak |ω|(t=0) "
          f"= {final_state['peak_omega']:.4f} / {omega_peak_init:.4f} = {persistence:.4f}")
    print(f"  Topology (c at t≥10P): {c_post_transient}")
    print(f"  c=3 preserved: {topology_preserved}")
    print()

    if persistence >= PERSISTENCE_MODE_I and topology_preserved:
        mode = "I-orbit"
        verdict = (
            f"MODE I-orbit — CORPUS VINDICATED. Single-electron self-consistent "
            f"orbit at corpus GT IS self-stable. peak |ω| persists at "
            f"{persistence:.2%} of initial after {final_state['t_period']:.0f} "
            f"Compton periods, AND c=3 preserved at all post-transient samples. "
            f"R7.1 eigsolve Mode III was correct on the linearized question (no "
            f"LINEAR eigenmode at corpus GT) but missed the NONLINEAR self-trapped "
            f"orbit, which only exists at finite amplitude. Round 7 closure "
            f"narrative changes substantially."
        )
    elif persistence < PERSISTENCE_MODE_II_III:
        mode = "III-orbit"
        verdict = (
            f"MODE III-orbit — Single-electron orbit DISSOLVES. peak |ω| decays to "
            f"{persistence:.2%} of initial within {final_state['t_period']:.0f} "
            f"Compton periods (below {PERSISTENCE_MODE_II_III:.0%} threshold). "
            f"In addition to R7.1's eigsolve Mode III, the corpus single-electron "
            f"is not self-stable as a nonlinear orbit either. This combined with "
            f"R7.1+R7.2+§10 closure means: no LINEAR mode AND no NONLINEAR orbit "
            f"at corpus GT. Round 8 entry candidates (Move 3 hybrid eigsolve, "
            f"Move 4 (p,q) sweep) become the cleaner follow-ups."
        )
    elif persistence >= PERSISTENCE_MODE_I:
        mode = "II-orbit"
        verdict = (
            f"MODE II-orbit — Orbit persists ({persistence:.2%} ≥ "
            f"{PERSISTENCE_MODE_I:.0%}) but topology drifts. c trajectory: "
            f"{c_post_transient}. Self-consistent standing wave exists at corpus "
            f"GT but it's NOT (2,3) winding. Substantively informative: the "
            f"engine hosts SOME self-stable orbit at this geometry but not the "
            f"corpus-claimed one."
        )
    else:
        # persistence in [0.5, 0.8)
        if topology_preserved:
            mode = "IV-orbit"
            verdict = (
                f"MODE IV-orbit — Marginally stable. peak |ω| at "
                f"{persistence:.2%} (in [{PERSISTENCE_MODE_II_III:.0%}, "
                f"{PERSISTENCE_MODE_I:.0%})) AND c=3 preserved throughout. "
                f"Topology held but amplitude decays. Warrants longer-time "
                f"investigation (e.g., 1000 Compton periods) to determine "
                f"whether decay continues to dissolution or settles at finite "
                f"non-zero amplitude (true marginal orbit)."
            )
        else:
            mode = "II-orbit"
            verdict = (
                f"MODE II-orbit — Orbit semi-persists ({persistence:.2%}) but "
                f"topology drifts. c trajectory: {c_post_transient}. Marginal "
                f"stability without topology preservation."
            )

    print(f"  {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase6_self_consistent_orbit_hunt",
        "test": "Move 5 — single-electron self-consistent orbit hunt at corpus GT",
        "N": N_LATTICE,
        "R": R_ANCHOR,
        "r": R_MINOR,
        "phi_sq": PHI_SQ,
        "v_amp_init": V_AMP_INIT,
        "a26_amp_scale": A26_AMP_SCALE,
        "n_periods_total": N_PERIODS_TOTAL,
        "n_steps": N_STEPS,
        "dt": DT,
        "elapsed_seconds": elapsed,
        "samples": samples,
        "omega_peak_init": omega_peak_init,
        "persistence": float(persistence),
        "c_post_transient": c_post_transient,
        "topology_preserved": bool(topology_preserved),
        "topology_target_c": TOPOLOGY_TARGET_C,
        "persistence_mode_I_threshold": PERSISTENCE_MODE_I,
        "persistence_mode_II_III_threshold": PERSISTENCE_MODE_II_III,
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
