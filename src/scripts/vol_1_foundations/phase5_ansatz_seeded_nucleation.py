"""Phase 5 ansatz-seeded pair-nucleation driver — Round 6 closure follow-up.

Per [doc 70_](../../research/_archive/L3_electron_soliton/70_phase5_resume_methodology.md):
applies Round 6's ansatz-initialization finding to pair-nucleation. Decouples
gate-mechanism (α)+(β) from threshold-chase (γ). The pre-Round-6
phase5_pair_nucleation.py gave NO-FIRE because C1 was undershot at registered
config (max A²=0.75-0.91 < sat_frac=0.95). This driver SEEDS the gate's
post-firing state directly, marks the seeded bond as already nucleated, and
tests:

  (α) Does the seeded Beltrami pair PERSIST under autoresonant drive?
      — peak |ω| at endpoints stable; Φ_link[A→B] retains magnitude.
  (β) Does the seeded pair PERSIST POST-DRIVE? — Kelvin topological-
      protection claim per Bingham-plastic framing (Vol 4 Ch 1:189-203).
  (γ) Does the seeded saturation propagate so OTHER bonds nucleate
      under drive? — drive-induced cascade test.

Adjudication tree:
  (a) Pair persists during AND post-drive, no other bonds fire wildly →
      Phase 5 mechanism validated; next experiment is amplitude/N sweep
      against P_phase5_nucleation.
  (b) Pair dissolves during drive or fails to even seed cleanly →
      C1/C2 logic itself needs revision (R5.10 Readings reopen at
      threshold-revision level).
  (c) Pair persists during drive but dissolves post-drive →
      Kelvin protection claim falsified empirically; revise
      Bingham-plastic framing.

NO changes to PairNucleationGate code or any engine code. NO changes to
F17-K research infrastructure. Driver-only experiment using existing seeders
+ existing gate. Reuses the ansatz-initialization template from F17-K Round 6
(_project_omega_to_saturation pattern, doc 34_ X4 algebraic-pin pattern).

Reference:
- research/_archive/L3_electron_soliton/70_phase5_resume_methodology.md (this doc)
- src/ave/topological/vacuum_engine.py::PairNucleationGate (gate code, unchanged)
- src/scripts/vol_1_foundations/phase5_pair_nucleation.py (pre-Round-6 driver — NO-FIRE)
- research/_archive/L3_electron_soliton/67_lc_coupling_reciprocity_audit.md §17-§26 (F17-K arc)
"""
from __future__ import annotations

import sys
import time

import numpy as np

sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src/scripts/vol_1_foundations")

from ave.topological.vacuum_engine import (
    AutoresonantCWSource,
    NodeResonanceObserver,
    PairNucleationGate,
    RegimeClassifierObserver,
    VacuumEngine3D,
)


PHI_CRITICAL = 1.0  # gate's default
BELTRAMI_AMP = float(np.sqrt(2.0))  # gate's default — calibrated to m_e c² in natural units
PORT_VECTORS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float)


def find_central_bond(engine: VacuumEngine3D) -> tuple[tuple, int, tuple]:
    """Find an A-B bond near the lattice center. Returns (A_idx, port, B_idx)."""
    nx = engine.k4.nx
    cx = nx // 2
    for di in range(-2, 3):
        for dj in range(-2, 3):
            for dk in range(-2, 3):
                i, j, k = cx + di, cx + dj, cx + dk
                if not (0 < i < nx - 1 and 0 < j < nx - 1 and 0 < k < nx - 1):
                    continue
                if not engine.k4.mask_A[i, j, k]:
                    continue
                for port in range(4):
                    p = PORT_VECTORS[port].astype(int)
                    ib, jb, kb = i + p[0], j + p[1], k + p[2]
                    if not (0 <= ib < nx and 0 <= jb < nx and 0 <= kb < nx):
                        continue
                    if engine.k4.mask_B[ib, jb, kb]:
                        return (i, j, k), port, (ib, jb, kb)
    raise RuntimeError("No viable A-B bond found near center")


def seed_beltrami_pair_ansatz(
    engine: VacuumEngine3D,
    A_idx: tuple, port: int, B_idx: tuple,
    amp: float = BELTRAMI_AMP, phi_critical: float = PHI_CRITICAL,
) -> None:
    """Seed Beltrami-bound-pair ansatz matching gate's _inject_pair output.

    LH at A, RH at B per doc 54_ §7. Match the gate's internal injection
    so the seeded state IS the post-firing configuration.
    """
    p_vec = PORT_VECTORS[port]
    p_hat = p_vec / np.linalg.norm(p_vec)

    engine.cos.omega[A_idx[0], A_idx[1], A_idx[2], :] = -amp * p_hat
    engine.cos.omega[B_idx[0], B_idx[1], B_idx[2], :] = +amp * p_hat
    engine.cos.omega_dot[A_idx[0], A_idx[1], A_idx[2], :] = 0.0
    engine.cos.omega_dot[B_idx[0], B_idx[1], B_idx[2], :] = 0.0

    sign = +1 if (port % 2 == 0) else -1
    engine.k4.Phi_link[A_idx[0], A_idx[1], A_idx[2], port] = sign * phi_critical


def measure_pair_state(
    engine: VacuumEngine3D, A_idx: tuple, port: int, B_idx: tuple,
) -> dict:
    """Snapshot diagnostics at the seeded bond."""
    omega_A = engine.cos.omega[A_idx[0], A_idx[1], A_idx[2], :]
    omega_B = engine.cos.omega[B_idx[0], B_idx[1], B_idx[2], :]
    phi_link = float(engine.k4.Phi_link[A_idx[0], A_idx[1], A_idx[2], port])
    return {
        "t": float(engine.time),
        "step": int(engine.step_count),
        "|ω|_A": float(np.linalg.norm(omega_A)),
        "|ω|_B": float(np.linalg.norm(omega_B)),
        "ω_A": [float(x) for x in omega_A],
        "ω_B": [float(x) for x in omega_B],
        "Phi_link[A→B]": phi_link,
        "peak|ω|_global": float(np.max(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1))),
        "peak|V|_global": float(np.max(np.abs(np.asarray(engine.k4.V_inc)))),
        "E_cos": float(engine.cos.total_energy()),
        "c_cos_global": int(engine.cos.extract_crossing_count()),
    }


def main(
    N: int = 24,
    pml: int = 4,
    amplitude: float = 0.5,
    wavelength: float = 3.5,
    t_ramp_periods: float = 3.0,
    t_sustain_periods: float = 15.0,
    t_post_drive_periods: float = 15.0,
    record_cadence: int = 2,
) -> dict:
    print("=" * 78)
    print("  Phase 5 ansatz-seeded pair-nucleation driver")
    print("=" * 78)
    print(f"  N={N}, pml={pml}, amp={amplitude}·V_SNAP, λ={wavelength}")
    print(f"  Drive: ramp {t_ramp_periods} + sustain {t_sustain_periods} + decay 1 periods")
    print(f"  Post-drive observation: {t_post_drive_periods} periods")
    print()

    omega_carrier = 2.0 * np.pi / wavelength
    period = 2.0 * np.pi / omega_carrier
    t_ramp = t_ramp_periods * period
    t_sustain = t_sustain_periods * period
    drive_end_time = (t_ramp_periods + t_sustain_periods + 1.0) * period
    total_time = drive_end_time + t_post_drive_periods * period
    n_outer_steps = int(total_time * np.sqrt(2.0)) + 1

    # Build engine with A28 + self-terms (per F17-K Round 6 default for any
    # coupled-engine work going forward — engine code unchanged but flags set)
    engine = VacuumEngine3D.from_args(
        N=N, pml=pml, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )

    # Find candidate bond + seed Beltrami-bound-pair ansatz
    A_idx, port, B_idx = find_central_bond(engine)
    print(f"  Seeded bond: A={A_idx}, port={port}, B={B_idx}")
    seed_beltrami_pair_ansatz(engine, A_idx, port, B_idx)

    state_seed = measure_pair_state(engine, A_idx, port, B_idx)
    print(f"  Initial seed state:")
    print(f"    |ω|_A = {state_seed['|ω|_A']:.4f}, |ω|_B = {state_seed['|ω|_B']:.4f}")
    print(f"    Φ_link[A→B] = {state_seed['Phi_link[A→B]']:+.4f}")
    print(f"    peak|ω|_global = {state_seed['peak|ω|_global']:.4f}")
    print()

    # Add gate (mark seeded bond as already-nucleated to prevent re-firing)
    gate = PairNucleationGate(cadence=record_cadence)
    bond_key = (A_idx[0], A_idx[1], A_idx[2], port)
    gate._nucleated_bonds.add(bond_key)
    engine.add_observer(gate)

    # Auxiliary observers
    regime_obs = RegimeClassifierObserver(cadence=record_cadence)
    node_obs = NodeResonanceObserver(cadence=record_cadence)
    engine.add_observer(regime_obs)
    engine.add_observer(node_obs)

    # Drive: head-on autoresonant collision (same as registered Phase 5 config)
    src_offset = pml + 3
    engine.add_source(AutoresonantCWSource(
        x0=src_offset, direction=(1.0, 0.0, 0.0),
        amplitude=amplitude, omega=omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period,
    ))
    engine.add_source(AutoresonantCWSource(
        x0=N - src_offset, direction=(-1.0, 0.0, 0.0),
        amplitude=amplitude, omega=omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period,
    ))

    # Run + record per-step pair-state snapshots
    pair_trajectory: list[dict] = [state_seed]
    print(f"  Running {n_outer_steps} steps ({total_time:.2f} natural-time-units)...")
    t0 = time.time()
    for _ in range(n_outer_steps):
        engine.step()
        if engine.step_count % record_cadence == 0:
            pair_trajectory.append(measure_pair_state(engine, A_idx, port, B_idx))
    elapsed = time.time() - t0
    print(f"  Elapsed: {elapsed:.2f}s")
    print()

    # Identify drive-end and post-drive snapshots
    drive_end_step = int(drive_end_time * np.sqrt(2.0))
    drive_end_idx = min(
        range(len(pair_trajectory)),
        key=lambda i: abs(pair_trajectory[i]["step"] - drive_end_step),
    )
    final_idx = len(pair_trajectory) - 1
    state_drive_end = pair_trajectory[drive_end_idx]
    state_final = pair_trajectory[final_idx]

    # Adjudication metrics
    omega_A_drive_ratio = state_drive_end["|ω|_A"] / max(state_seed["|ω|_A"], 1e-12)
    omega_A_final_ratio = state_final["|ω|_A"] / max(state_seed["|ω|_A"], 1e-12)
    phi_drive_ratio = abs(state_drive_end["Phi_link[A→B]"]) / max(abs(state_seed["Phi_link[A→B]"]), 1e-12)
    phi_final_ratio = abs(state_final["Phi_link[A→B]"]) / max(abs(state_seed["Phi_link[A→B]"]), 1e-12)

    # Other-bond firings (cascade test): gate.history shows what fired
    other_firings = sum(h["n_fired_this_step"] for h in gate.history)
    other_fired_bonds = []
    for h in gate.history:
        for fb in h["fired_bonds"]:
            if fb != bond_key:
                other_fired_bonds.append(fb)

    # Adjudicate
    PERSIST_THRESH = 0.5
    if (
        omega_A_drive_ratio > PERSIST_THRESH
        and phi_drive_ratio > PERSIST_THRESH
        and omega_A_final_ratio > PERSIST_THRESH
        and phi_final_ratio > PERSIST_THRESH
    ):
        verdict = "(a) PERSISTS during AND post-drive — Phase 5 mechanism validated"
    elif omega_A_drive_ratio < PERSIST_THRESH or phi_drive_ratio < PERSIST_THRESH:
        verdict = "(b) DISSOLVES during drive — C1/C2 logic needs revision"
    elif omega_A_final_ratio < PERSIST_THRESH or phi_final_ratio < PERSIST_THRESH:
        verdict = "(c) DISSOLVES post-drive — Kelvin protection falsified"
    else:
        verdict = "AMBIGUOUS — between persistence thresholds"

    print(f"  Adjudication metrics:")
    print(f"    |ω|_A   seed → drive-end → final = {state_seed['|ω|_A']:.3f} → "
          f"{state_drive_end['|ω|_A']:.3f} ({omega_A_drive_ratio:.2f}×) → "
          f"{state_final['|ω|_A']:.3f} ({omega_A_final_ratio:.2f}×)")
    print(f"    Φ_link  seed → drive-end → final = {state_seed['Phi_link[A→B]']:+.3f} → "
          f"{state_drive_end['Phi_link[A→B]']:+.3f} ({phi_drive_ratio:.2f}×) → "
          f"{state_final['Phi_link[A→B]']:+.3f} ({phi_final_ratio:.2f}×)")
    print(f"    Other-bond firings during run: {other_firings} (cascade test)")
    print(f"    Final peak|ω|_global = {state_final['peak|ω|_global']:.3f}")
    print(f"    Final peak|V|_global = {state_final['peak|V|_global']:.3f}")
    print(f"    Final c_cos = {state_final['c_cos_global']}")
    print(f"    Final E_cos = {state_final['E_cos']:.3e}")
    print()
    print(f"  ⟹ Verdict: {verdict}")

    return {
        "config": {
            "N": N, "pml": pml, "amplitude": amplitude, "wavelength": wavelength,
            "t_ramp_periods": t_ramp_periods, "t_sustain_periods": t_sustain_periods,
            "t_post_drive_periods": t_post_drive_periods,
        },
        "seeded_bond": {"A_idx": A_idx, "port": port, "B_idx": B_idx},
        "pair_trajectory": pair_trajectory,
        "state_seed": state_seed,
        "state_drive_end": state_drive_end,
        "state_final": state_final,
        "metrics": {
            "omega_A_drive_ratio": omega_A_drive_ratio,
            "omega_A_final_ratio": omega_A_final_ratio,
            "phi_drive_ratio": phi_drive_ratio,
            "phi_final_ratio": phi_final_ratio,
            "other_firings": other_firings,
            "other_fired_bonds": other_fired_bonds,
        },
        "verdict": verdict,
        "elapsed_s": elapsed,
        "drive_end_idx": drive_end_idx,
    }


if __name__ == "__main__":
    main()
