"""
O.1 — (2,3) Electron Soliton IC + Closed Evolution Stability Test.

Per Rule 14 axiom-canonical bound-state test:
- Ax 1: K4 LC lattice as substrate
- Ax 2: (2,3) winding number = topological charge invariant Q = 1·e
- Ax 3: Noether on Q during evolution; energy conservation of m_e c²
- Ax 4: vacuum yield limit holds the trap (passive role)

Uses existing corpus-canonical IC seeder `initialize_2_3_voltage_ansatz`
from tlm_electron_soliton_eigenmode.py:33-122 — encodes:
  1. Power-law hedgehog magnitude envelope (NOT Gaussian)
  2. Quadrature phase: cos(θ) on ports 0,1; sin(θ) on ports 2,3
  3. Chirality: per-port weighting by (2,3) tangent direction projection

== Pre-registered observables (per Rule 10 + A39 v2) ==

PRIMARY:
  (1) Does the soliton SUSTAIN over 50P closed evolution?
      Track total energy on shell: stable → sustained; decaying → dissipative
  (2) Does the (2,3) topology persist? Op10 c at multiple time points.

SECONDARY:
  (3) Shell localization: fraction of energy in toroidal shell vs bulk
  (4) Frequency content at shell: dominant ω near ω_C?
  (5) Does Cosserat ω develop spontaneously (couples via Op14)?

== Configuration ==

- N=48, PML=4
- Cosserat ON, A28-corrected
- temperature = 0 (deterministic, IC-only)
- NO SOURCE — closed evolution
- IC: initialize_2_3_voltage_ansatz with R=8, r=4, amplitude=0.3
  (R, r chosen for cells well within active region; amplitude in
   linear-but-significant regime, A² peak ~ 0.09 below saturation)
- Run: 50 Compton periods

== Compute estimate ==

~3 min wall clock at N=48.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
from ave.topological.vacuum_engine import VacuumEngine3D
from scripts.vol_1_foundations.tlm_electron_soliton_eigenmode import (
    initialize_2_3_voltage_ansatz,
)


ALPHA = 1.0 / 137.035999
V_YIELD = float(np.sqrt(ALPHA))
A2_OP14 = float(np.sqrt(2.0 * ALPHA))
OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)


def main():
    print("=" * 78, flush=True)
    print("  O.1 — (2,3) Electron IC + Closed Evolution (Ax-canonical Regime I bound state)")
    print("=" * 78, flush=True)

    N, PML = 48, 4
    n_steps = int(50 * COMPTON_PERIOD / DT)
    R_torus = 8.0
    r_torus = 4.0
    amp_ic = 0.3

    print(f"\n  Lattice: N={N}, PML={PML}")
    print(f"  IC: (2,3) torus-knot ansatz, R={R_torus}, r={r_torus}, amp={amp_ic}")
    print(f"  No source — closed evolution")
    print(f"  V_yield={V_YIELD:.4f}, A²_op14={A2_OP14:.4f}")

    t_start = time.time()
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )

    # Apply (2,3) IC seeder
    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_torus, r=r_torus, amplitude=amp_ic,
    )

    # Verify IC engaged
    init_a2 = np.sum(engine.k4.V_inc ** 2, axis=-1)
    init_a2_int = init_a2 * engine.k4.mask_active.astype(float)
    init_a2_int[:PML, :, :] = 0; init_a2_int[N-PML:, :, :] = 0
    init_a2_int[:, :PML, :] = 0; init_a2_int[:, N-PML:, :] = 0
    init_a2_int[:, :, :PML] = 0; init_a2_int[:, :, N-PML:] = 0
    print(f"\n  IC verification:")
    print(f"    A²_max(t=0): {init_a2_int.max():.4f}")
    print(f"    A²_mean (active): {init_a2_int[init_a2_int>0].mean():.4f}")
    print(f"    Total energy(t=0): {init_a2_int.sum():.4f}")

    # Identify shell cells (within toroidal shell within tolerance)
    cx_, cy_, cz_ = (N-1)/2, (N-1)/2, (N-1)/2
    idx = np.indices((N, N, N))
    xx, yy, zz = idx[0]-cx_, idx[1]-cy_, idx[2]-cz_
    rho_xy = np.sqrt(xx**2 + yy**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R_torus)**2 + zz**2)
    shell_mask = (rho_tube < 1.5 * r_torus) & engine.k4.mask_active

    # Captures
    energy_total_traj = []
    energy_shell_traj = []
    a2_max_traj = []
    cos_omega_max_traj = []   # Cosserat coupling check

    capture_cadence = 5
    print(f"\n  Running...", flush=True)

    for step_i in range(n_steps):
        engine.step()

        if step_i % capture_cadence == 0:
            t_now = step_i * DT
            a2 = np.sum(engine.k4.V_inc ** 2, axis=-1)
            a2_int = a2 * engine.k4.mask_active.astype(float)
            a2_int[:PML, :, :] = 0; a2_int[N-PML:, :, :] = 0
            a2_int[:, :PML, :] = 0; a2_int[:, N-PML:, :] = 0
            a2_int[:, :, :PML] = 0; a2_int[:, :, N-PML:] = 0

            e_total = float(a2_int.sum())
            e_shell = float(a2_int[shell_mask].sum())
            a2_max = float(a2_int.max())
            omega_max = float(np.abs(engine.cos.omega).max())

            energy_total_traj.append((t_now, e_total))
            energy_shell_traj.append((t_now, e_shell))
            a2_max_traj.append((t_now, a2_max))
            cos_omega_max_traj.append((t_now, omega_max))

            if step_i % 50 == 0:
                t_p = t_now / COMPTON_PERIOD
                shell_frac = e_shell / max(e_total, 1e-30)
                print(f"    t={t_p:5.2f}P  E_total={e_total:.3e}  "
                      f"E_shell={e_shell:.3e} ({shell_frac:.3f})  "
                      f"A²_max={a2_max:.3f}  ω_max={omega_max:.3e}  "
                      f"({time.time() - t_start:.0f}s)", flush=True)

    elapsed = time.time() - t_start
    print(f"\n  Engine evolution complete in {elapsed:.0f}s")

    # Adjudication
    e_first = energy_total_traj[0][1]
    e_last = energy_total_traj[-1][1]
    retention = e_last / max(e_first, 1e-30)
    e_shell_last = energy_shell_traj[-1][1]
    shell_localization_last = e_shell_last / max(e_last, 1e-30)

    try:
        c_op10 = int(engine.cos.extract_crossing_count())
    except Exception:
        c_op10 = -1

    print(f"\n  PRIMARY (1) — Energy retention over 50P:")
    print(f"    E(t=0) = {e_first:.3e}")
    print(f"    E(t=50P) = {e_last:.3e}")
    print(f"    Retention: {retention:.3f}")
    print(f"  PRIMARY (2) — Topology at end:")
    print(f"    Op10 c = {c_op10} (target=3 per (2,3) IC)")

    print(f"\n  SECONDARY:")
    print(f"    Shell localization (fraction of E in shell at t=50P): {shell_localization_last:.3f}")
    print(f"    Cosserat ω_max at end: {cos_omega_max_traj[-1][1]:.3e}")

    # Verdict
    print(f"\n  Sustenance: {'YES' if retention > 0.3 else 'PARTIAL' if retention > 0.05 else 'NO'}")
    print(f"  Topology preserved: {'YES (c=3)' if c_op10 == 3 else f'CHANGED (c={c_op10})'}")

    out = {
        "test": "O.1: (2,3) IC + closed evolution",
        "config": {"N": N, "PML": PML, "R": R_torus, "r": r_torus, "amp_ic": amp_ic},
        "energy_retention": {
            "e_initial": float(e_first),
            "e_final": float(e_last),
            "retention_50P": float(retention),
        },
        "topology": {"c_op10_final": int(c_op10), "preserved": c_op10 == 3},
        "shell_localization_final": float(shell_localization_last),
        "trajectory_summary": {
            "energy_total_traj": [[float(t), float(e)] for t, e in energy_total_traj],
            "energy_shell_traj": [[float(t), float(e)] for t, e in energy_shell_traj],
            "a2_max_traj": [[float(t), float(a)] for t, a in a2_max_traj],
            "cos_omega_max_traj": [[float(t), float(o)] for t, o in cos_omega_max_traj],
        },
        "elapsed_total_s": float(elapsed),
    }
    out_path = Path(__file__).parent / "r10_v8_o1_electron_ic_stability_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
