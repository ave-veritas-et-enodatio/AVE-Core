"""R7.2 (2,3)/Hopf topologically-protected pair injection driver — VACUUM_ENGINE_MANUAL §9 G-13.

Per `P_phase5_topological_injection` (frozen at commit 1c89fa1) +
[doc 70_ §7.6](../../research/L3_electron_soliton/70_phase5_resume_methodology.md#L7).

Replaces the gate's point-rotation Beltrami `_inject_pair` profile (which
was empirically falsified as fundamentally unstable in Cosserat self-dynamics
per Phase 5 case (b'), commit ede4008 — |ω|_A drops 93% in ONE Velocity-Verlet
step) with topologically-richer (2,3) torus-knot seeded at chirality-matched
bond endpoints (LH at A, RH at B).

DUAL-CRITERION PASS (per A39 v2 + frozen pred):
  - Frequency persistence: peak |ω|_A AND |ω|_B at endpoints stay
    ≥ 0.5·seed amplitude for ≥ 10 Compton periods post-drive
  - AND
  - Topology preservation: c_eigvec = 3 preserved throughout drive +
    post-drive observation

Mode I (G-13 works): both criteria PASS
Mode II: frequency persists, topology lost
Mode III: frequency dissolves at same timescale as Beltrami (~1-3 Compton periods)

Reuses Phase 5 ansatz-seeded driver infrastructure (commit ede4008) +
F17-K (2,3) hedgehog seeders.

References:
  - VACUUM_ENGINE_MANUAL §9 G-13 (contingency activated empirically)
  - doc 70_ §7.6 (Round 7 Stage 2 candidate scope)
  - phase5_ansatz_seeded_nucleation.py (commit ede4008 — Beltrami baseline)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import (
    AutoresonantCWSource, NodeResonanceObserver,
    PairNucleationGate, RegimeClassifierObserver, VacuumEngine3D,
)


# ─── Pre-registered constants (frozen) ────────────────────────────────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI
A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)
GT_PEAK_OMEGA = 0.3 * np.pi  # ≈ 0.9425

# R7.2 dual-criterion PASS (per pred body)
PERSIST_FRAC_THRESH = 0.5     # peak |ω| ≥ 0.5·seed for ≥ 10 Compton periods
PERSIST_PERIODS_REQ = 10      # at least 10 Compton periods post-drive
TOPOLOGY_TARGET_C = 3         # (2,3) winding number preserved throughout

PORT_VECTORS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float)

OUTPUT_JSON = Path(__file__).parent / "phase5_topological_pair_injection_results.json"


# ─── Bond finding (reused from phase5_ansatz_seeded_nucleation.py) ───────────


def find_central_bond(engine):
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


# ─── (2,3) torus-knot ansatz at bond endpoints ────────────────────────────────


def seed_2_3_torus_knot_at_bond(
    engine, A_idx, port, B_idx,
    R_target=4.0, r_target=4.0/PHI_SQ,
):
    """Seed (2,3) torus-knot ansatz at BOTH endpoints A, B.

    Each endpoint gets a localized (2,3) hedgehog centered at that endpoint's
    lattice position, with chirality matched (LH at A, RH at B).

    Reuses initialize_electron_2_3_sector (which centers the hedgehog at the
    LATTICE CENTER) but applied to two superposed configurations — one
    centered at A, one at B, with opposite chirality.

    Implementation note: initialize_electron_2_3_sector centers at lattice
    center. To seed at arbitrary positions, we manually compute the hedgehog
    pattern at each endpoint location.
    """
    N = engine.cos.nx
    cx_A, cy_A, cz_A = float(A_idx[0]), float(A_idx[1]), float(A_idx[2])
    cx_B, cy_B, cz_B = float(B_idx[0]), float(B_idx[1]), float(B_idx[2])

    # Compute (2,3) hedgehog per-endpoint analogous to
    # initialize_electron_2_3_sector but centered at the endpoint
    i, j, k = engine.cos._i, engine.cos._j, engine.cos._k

    # Endpoint A — LH chirality (positive winding sign)
    x_A = i - cx_A
    y_A = j - cy_A
    z_A = k - cz_A
    rho_xy_A = np.sqrt(x_A**2 + y_A**2)
    rho_tube_A = np.sqrt((rho_xy_A - R_target) ** 2 + z_A**2)
    phi_A = np.arctan2(y_A, x_A)
    psi_A = np.arctan2(z_A, rho_xy_A - R_target)
    envelope_A = A26_AMP_SCALE * (np.sqrt(3.0) / 2.0) * np.pi / (1.0 + (rho_tube_A / r_target) ** 2)
    theta_A = 2.0 * phi_A + 3.0 * psi_A   # (2,3) winding
    omega_A = np.zeros((N, N, N, 3))
    omega_A[..., 0] = envelope_A * np.cos(theta_A)
    omega_A[..., 1] = envelope_A * np.sin(theta_A)
    omega_A[..., 2] = 0.0

    # Endpoint B — RH chirality (negative winding sign)
    x_B = i - cx_B
    y_B = j - cy_B
    z_B = k - cz_B
    rho_xy_B = np.sqrt(x_B**2 + y_B**2)
    rho_tube_B = np.sqrt((rho_xy_B - R_target) ** 2 + z_B**2)
    phi_B = np.arctan2(y_B, x_B)
    psi_B = np.arctan2(z_B, rho_xy_B - R_target)
    envelope_B = A26_AMP_SCALE * (np.sqrt(3.0) / 2.0) * np.pi / (1.0 + (rho_tube_B / r_target) ** 2)
    theta_B = -(2.0 * phi_B + 3.0 * psi_B)  # opposite winding
    omega_B = np.zeros((N, N, N, 3))
    omega_B[..., 0] = envelope_B * np.cos(theta_B)
    omega_B[..., 1] = envelope_B * np.sin(theta_B)
    omega_B[..., 2] = 0.0

    # Superpose
    omega_total = omega_A + omega_B
    omega_total *= engine.cos.mask_alive[..., None]
    engine.cos.omega = omega_total
    engine.cos.omega_dot[...] = 0.0
    engine.cos.u[...] = 0.0


# ─── Diagnostics ──────────────────────────────────────────────────────────────


def measure_state(engine, A_idx, B_idx):
    omega_A = engine.cos.omega[A_idx[0], A_idx[1], A_idx[2], :]
    omega_B = engine.cos.omega[B_idx[0], B_idx[1], B_idx[2], :]
    return {
        "t": float(engine.time),
        "step": int(engine.step_count),
        "|ω|_A": float(np.linalg.norm(omega_A)),
        "|ω|_B": float(np.linalg.norm(omega_B)),
        "peak|ω|_global": float(np.max(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1))),
        "c_cos_global": int(engine.cos.extract_crossing_count()),
        "E_cos": float(engine.cos.total_energy()),
    }


# ─── Main ────────────────────────────────────────────────────────────────────


def main(
    N=24, pml=4, amplitude=0.5, wavelength=3.5,
    t_ramp_periods=3.0, t_sustain_periods=15.0, t_post_drive_periods=15.0,
    record_cadence=2,
):
    print("=" * 78, flush=True)
    print(f"  R7.2 (2,3) torus-knot pair injection driver")
    print(f"  P_phase5_topological_injection (frozen at 1c89fa1)")
    print("=" * 78, flush=True)
    print(f"  Replaces Beltrami point-rotation profile (Phase 5 case b')")
    print(f"  per VACUUM_ENGINE_MANUAL §9 G-13 contingency.")
    print()
    print(f"  N={N}, amp={amplitude}·V_SNAP, λ={wavelength}")
    print(f"  Drive: {t_ramp_periods} ramp + {t_sustain_periods} sustain + 1 decay periods")
    print(f"  Post-drive observation: {t_post_drive_periods} periods")
    print(f"  Pred PASS: peak |ω|_A,B ≥ {PERSIST_FRAC_THRESH}·seed for ≥ {PERSIST_PERIODS_REQ} Compton periods")
    print(f"             AND c_cos preserved at {TOPOLOGY_TARGET_C} throughout")
    print()

    omega_carrier = 2.0 * np.pi / wavelength
    period = 2.0 * np.pi / omega_carrier
    t_ramp = t_ramp_periods * period
    t_sustain = t_sustain_periods * period
    drive_end_time = (t_ramp_periods + t_sustain_periods + 1.0) * period
    total_time = drive_end_time + t_post_drive_periods * period
    n_outer_steps = int(total_time * np.sqrt(2.0)) + 1

    engine = VacuumEngine3D.from_args(
        N=N, pml=pml, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )

    A_idx, port, B_idx = find_central_bond(engine)
    print(f"  Seeded bond: A={A_idx}, port={port}, B={B_idx}")

    # Seed (2,3) torus-knot at both endpoints
    seed_2_3_torus_knot_at_bond(engine, A_idx, port, B_idx)
    state_seed = measure_state(engine, A_idx, B_idx)
    print(f"  Initial seed state:")
    print(f"    |ω|_A = {state_seed['|ω|_A']:.4f}  (target ~0.3π = {GT_PEAK_OMEGA:.4f})")
    print(f"    |ω|_B = {state_seed['|ω|_B']:.4f}")
    print(f"    peak|ω|_global = {state_seed['peak|ω|_global']:.4f}")
    print(f"    c_cos = {state_seed['c_cos_global']} (target {TOPOLOGY_TARGET_C})")
    print()

    # Add gate (mark seeded bond as already-nucleated to prevent re-firing)
    gate = PairNucleationGate(cadence=record_cadence)
    bond_key = (A_idx[0], A_idx[1], A_idx[2], port)
    gate._nucleated_bonds.add(bond_key)
    engine.add_observer(gate)

    # Drive: head-on autoresonant collision
    src_offset = pml + 3
    engine.add_source(AutoresonantCWSource(
        x0=src_offset, direction=(1.0, 0.0, 0.0),
        amplitude=amplitude, omega=omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain, t_decay=period,
    ))
    engine.add_source(AutoresonantCWSource(
        x0=N - src_offset, direction=(-1.0, 0.0, 0.0),
        amplitude=amplitude, omega=omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain, t_decay=period,
    ))

    # Run
    trajectory = [state_seed]
    print(f"  Running {n_outer_steps} steps ({total_time:.2f} natural-time-units)...")
    t0 = time.time()
    for _ in range(n_outer_steps):
        engine.step()
        if engine.step_count % record_cadence == 0:
            trajectory.append(measure_state(engine, A_idx, B_idx))
    elapsed = time.time() - t0
    print(f"  Elapsed: {elapsed:.1f}s")
    print()

    # Adjudication: dual criterion
    drive_end_step = int(drive_end_time * np.sqrt(2.0))
    omega_seed = state_seed['|ω|_A']
    threshold_omega = PERSIST_FRAC_THRESH * omega_seed

    # Find post-drive trajectory and check persistence
    post_drive = [s for s in trajectory if s['step'] >= drive_end_step]
    n_post = len(post_drive)

    # Frequency persistence: peak |ω|_A AND |ω|_B ≥ threshold throughout post-drive
    omega_A_post = [s['|ω|_A'] for s in post_drive]
    omega_B_post = [s['|ω|_B'] for s in post_drive]
    freq_pass_A = all(om >= threshold_omega for om in omega_A_post)
    freq_pass_B = all(om >= threshold_omega for om in omega_B_post)

    # Compton periods covered in post-drive
    if n_post > 1:
        post_drive_duration = post_drive[-1]['t'] - post_drive[0]['t']
        compton_periods_covered = post_drive_duration / period
    else:
        compton_periods_covered = 0.0
    period_check = compton_periods_covered >= PERSIST_PERIODS_REQ

    frequency_pass = bool(freq_pass_A and freq_pass_B and period_check)

    # Topology preservation: c_cos = 3 throughout drive + post-drive
    c_values = [s['c_cos_global'] for s in trajectory]
    topology_preserved = all(c == TOPOLOGY_TARGET_C for c in c_values)
    min_c = min(c_values) if c_values else None
    max_c = max(c_values) if c_values else None
    c_at_end = c_values[-1] if c_values else None

    print("=" * 78, flush=True)
    print("  R7.2 dual-criterion adjudication")
    print("=" * 78, flush=True)
    print(f"  Compton periods covered post-drive: {compton_periods_covered:.2f} (req ≥ {PERSIST_PERIODS_REQ})")
    print(f"  |ω|_A post-drive: min={min(omega_A_post) if omega_A_post else 0:.4f}, "
          f"threshold={threshold_omega:.4f}, all-above={freq_pass_A}")
    print(f"  |ω|_B post-drive: min={min(omega_B_post) if omega_B_post else 0:.4f}, "
          f"threshold={threshold_omega:.4f}, all-above={freq_pass_B}")
    print(f"  Frequency persistence: {'PASS' if frequency_pass else 'FAIL'}")
    print()
    print(f"  c_cos trajectory: min={min_c}, max={max_c}, end={c_at_end}, target={TOPOLOGY_TARGET_C}")
    print(f"  Topology preservation: {'PASS' if topology_preserved else 'FAIL'}")
    print()

    if frequency_pass and topology_preserved:
        mode = "I"
        verdict = ("MODE I — G-13 contingency works. Topologically-richer (2,3) torus-knot "
                   "ansatz persists where Beltrami didn't. Both frequency and topology "
                   "preserved post-drive. Canonical pair-nucleation mechanism: (2,3) torus-knot "
                   "injection profile.")
    elif frequency_pass and not topology_preserved:
        mode = "II"
        verdict = ("MODE II — Frequency persistence PASS but topology preservation FAIL. "
                   f"c_cos drifted from {TOPOLOGY_TARGET_C} (min={min_c}, max={max_c}). "
                   "Cosserat self-dynamics preserves magnitude pattern but not winding. "
                   "Round 8 question: what additional dynamics needed to preserve topology?")
    else:
        mode = "III"
        verdict = ("MODE III — Frequency dissolves at same timescale as Beltrami "
                   "(case b'). Topologically-richer ansatz also dissolves. Coupling-depth "
                   "issue, not injection-profile issue. Same physics as F17-K (2,3) electron "
                   "Cosserat dissolution at step ~11. The bound state requires more than "
                   "topological richness in the injection profile.")
    print(f"  {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase5_topological_injection",
        "frozen_at_commit": "1c89fa1",
        "N": N,
        "amplitude": amplitude,
        "compton_periods_covered_post_drive": compton_periods_covered,
        "omega_seed": omega_seed,
        "threshold_omega": threshold_omega,
        "min_omega_A_post_drive": float(min(omega_A_post) if omega_A_post else 0),
        "min_omega_B_post_drive": float(min(omega_B_post) if omega_B_post else 0),
        "frequency_pass_A": bool(freq_pass_A),
        "frequency_pass_B": bool(freq_pass_B),
        "frequency_pass": frequency_pass,
        "min_c_cos": min_c,
        "max_c_cos": max_c,
        "c_cos_at_end": c_at_end,
        "topology_preserved": bool(topology_preserved),
        "mode": mode,
        "verdict": verdict,
        "trajectory_length": len(trajectory),
        "elapsed_seconds": elapsed,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
