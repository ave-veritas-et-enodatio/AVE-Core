"""
Foundation Audit Test 2: plane-wave dispersion / Maxwell linearity check.

Most basic engine-validity test: at LOW amplitude (linear Maxwell regime,
S(A) ≈ 1, no saturation), does the engine propagate waves at c?

Test design:
  - Inject single delta pulse at lattice center, port 0, amplitude 0.001 V_SNAP
  - Record |V_inc| field across the whole lattice every step
  - Track wave-front radius (location of peak |V_inc|) vs time
  - Fit r_front(t): slope = c_eff in natural units (should be 1.0)

Predictions:
  - If engine implements linear Maxwell correctly: c_eff = 1.0 ± few%
  - If c_eff < 1: engine has propagation slowdown (would indicate dispersion
    or numerical artifact at short wavelengths)
  - If c_eff > 1: engine violates causality (engine bug)

Engine config: pure K4-TLM (disable_cosserat_lc_force=True,
enable_cosserat_self_terms=False) — bench test of the K4-TLM
scatter+connect implementation alone.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D


def main():
    print("=" * 78, flush=True)
    print("  Foundation Audit Test 2: plane-wave dispersion / Maxwell linearity")
    print("=" * 78, flush=True)

    N = 32
    PML = 4
    DT = 1.0 / np.sqrt(2.0)
    COMPTON_PERIOD = 2.0 * np.pi
    N_PERIODS = 20.0  # enough for wave to propagate to ~r=14 in active region
    N_STEPS = int(N_PERIODS * COMPTON_PERIOD / DT)

    print(f"  Lattice: {N}³, PML={PML}, active region {N-2*PML}³")
    print(f"  Recording {N_STEPS} steps ({N_PERIODS}P)")
    print()

    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=False,
    )

    center = (N // 2, N // 2, N // 2)
    v_pulse = 0.001  # very low amplitude — deeply linear Maxwell regime
    engine.k4.V_inc[center[0], center[1], center[2], 0] = v_pulse
    print(f"  Pulse: V_inc[{center[0]},{center[1]},{center[2]}, port=0] = {v_pulse}")
    print(f"  V_pulse << V_yield = V_SNAP → S(A) ≈ 1 (linear Maxwell)")

    # Precompute distance-from-center for every lattice site
    ix, iy, iz = np.indices((N, N, N))
    dx_c = ix - center[0]
    dy_c = iy - center[1]
    dz_c = iz - center[2]
    r_grid = np.sqrt(dx_c**2 + dy_c**2 + dz_c**2)

    # Active mask (exclude PML)
    active_mask = np.zeros((N, N, N), dtype=bool)
    active_mask[PML:N-PML, PML:N-PML, PML:N-PML] = True

    # Track wave-front radius per step
    n_record = N_STEPS
    front_radius = np.zeros(n_record)
    max_field_per_step = np.zeros(n_record)
    energy_inside_r = []  # snapshot at periodic intervals

    snapshot_periods = [1, 2, 5, 10, 15, 20]
    snapshot_steps = [int(p * COMPTON_PERIOD / DT) for p in snapshot_periods]
    snapshots = {}

    t0 = time.time()
    last = t0
    for i in range(n_record):
        engine.step()

        # Compute |V_inc| field at every active site (port-summed magnitude)
        v_field_sq = np.sum(engine.k4.V_inc**2, axis=-1)  # (N,N,N)
        v_field = np.sqrt(v_field_sq)
        v_field_active = v_field * active_mask

        # Wave front: radius of the maximum-field site
        max_idx = np.argmax(v_field_active.flatten())
        r_max = float(r_grid.flatten()[max_idx])
        front_radius[i] = r_max
        max_field_per_step[i] = float(v_field.flatten()[max_idx])

        # Snapshot energy distribution
        if i in snapshot_steps:
            t_p = (i + 1) * DT / COMPTON_PERIOD
            r_bins = np.arange(0, N//2 + 1)
            energy_per_shell = []
            for r_low in r_bins[:-1]:
                shell_mask = (r_grid >= r_low) & (r_grid < r_low + 1) & active_mask
                if shell_mask.sum() > 0:
                    energy_per_shell.append(float(v_field_sq[shell_mask].mean()))
                else:
                    energy_per_shell.append(0.0)
            snapshots[f"t={t_p:.1f}P"] = {
                "step": i,
                "r_max_field": r_max,
                "max_field": float(v_field.flatten()[max_idx]),
                "energy_per_shell": energy_per_shell,
            }

        if (time.time() - last) > 30.0:
            t_p = (i + 1) * DT / COMPTON_PERIOD
            print(f"    step {i}/{n_record}, t={t_p:.1f}P, "
                  f"front r={r_max:.2f}, max field={max_field_per_step[i]:.3e}, "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last = time.time()

    elapsed = time.time() - t0
    print(f"\n  Recording done at {elapsed:.1f}s")

    # Linear fit of front_radius vs time
    t_vec = np.arange(n_record) * DT
    # Fit only the early part where front is propagating outward (before reaching active boundary)
    # Active region radius from center ≈ N/2 - PML = 16 - 4 = 12 ℓ_node
    # Use range where front_radius < active_max - 1
    active_max_r = N // 2 - PML - 1
    fit_mask = (front_radius > 1) & (front_radius < active_max_r)
    if fit_mask.sum() > 5:
        c_eff_fit = np.polyfit(t_vec[fit_mask], front_radius[fit_mask], 1)
        c_eff = c_eff_fit[0]  # slope = c_eff in natural units (where c=1)
    else:
        c_eff = None

    print()
    print(f"  Wave-front radius vs time:")
    print(f"    Active region max r ≈ {active_max_r}")
    print(f"    Fit range: t ∈ [{t_vec[fit_mask][0]:.3f}, {t_vec[fit_mask][-1]:.3f}]")
    print(f"    Number of fit points: {fit_mask.sum()}")
    if c_eff is not None:
        print(f"    c_eff fit slope: {c_eff:.4f} (Maxwell predicts c = 1.0)")
        print(f"    Deviation from c: {(c_eff - 1.0) * 100:+.2f}%")

    # Snapshot summary
    print()
    print(f"  Wave-front position at snapshots:")
    print(f"    {'time':<12} {'r_max_field':>12} {'max field':>15}")
    for label, snap in snapshots.items():
        print(f"    {label:<12} {snap['r_max_field']:>12.2f} {snap['max_field']:>15.4e}")

    # Verdicts
    print()
    if c_eff is not None:
        if abs(c_eff - 1.0) < 0.05:
            verdict = "PASS — engine propagates at c (linear Maxwell baseline confirmed within 5%)"
        elif abs(c_eff - 1.0) < 0.15:
            verdict = f"PARTIAL — engine c_eff = {c_eff:.4f}, ~10-15% off from c (possible discrete-substrate dispersion at short wavelengths)"
        else:
            verdict = f"FAIL — engine c_eff = {c_eff:.4f}, substantial deviation from c (engine bug or numerical artifact)"
    else:
        verdict = "INSUFFICIENT DATA — fit window had too few points"
    print(f"  Verdict: {verdict}")

    out = {
        "test": "Foundation Audit Test 2: plane-wave dispersion (low amplitude)",
        "N": N, "PML": PML, "v_pulse": v_pulse,
        "n_periods": N_PERIODS, "n_steps": N_STEPS,
        "elapsed_s": elapsed,
        "front_radius_per_step_first_50": front_radius[:50].tolist(),
        "front_radius_per_step_last_50": front_radius[-50:].tolist(),
        "c_eff_fit": float(c_eff) if c_eff is not None else None,
        "deviation_from_c_pct": float((c_eff - 1.0) * 100) if c_eff is not None else None,
        "fit_n_points": int(fit_mask.sum()),
        "snapshots": snapshots,
        "verdict": verdict,
    }
    out_path = Path(__file__).parent / "r10_v8_foundation_audit_t2_dispersion_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
