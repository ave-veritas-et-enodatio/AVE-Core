"""
Foundation Audit Test 2 v2: plane-wave dispersion (corrected metric).

T2 v1 used "radius of max |V_inc|" as wave-front metric — but the pulse
on port 0 only creates asymmetric IC that doesn't form clean spherical
front. Max-field stayed near center even when energy was spreading.

T2 v2 corrections:
  1. SYMMETRIC pulse: V_inc at all 4 ports of center A-site (isotropic IC)
  2. Energy-in-shells tracking: |V_inc|²+|V_ref|² summed over concentric
     shells at radii r ∈ {1, 2, 3, 5, 7, 9, 11}
  3. First-arrival time at each shell: when shell energy first exceeds
     threshold (e.g., 10× initial-step shell energy floor)
  4. c_eff = (r_n - r_1) / (t_n - t_1) using arrival times

Predictions:
  - If linear Maxwell: c_eff = 1.0 (natural units) within ~few percent
  - Discrete K4-TLM may show small dispersion at short wavelengths
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
    print("  Foundation Audit Test 2 v2: corrected dispersion test")
    print("=" * 78, flush=True)

    N = 32
    PML = 4
    DT = 1.0 / np.sqrt(2.0)
    COMPTON_PERIOD = 2.0 * np.pi
    N_PERIODS = 30.0
    N_STEPS = int(N_PERIODS * COMPTON_PERIOD / DT)

    print(f"  Lattice: {N}³, PML={PML}, active region {N-2*PML}³ = 24³")
    print(f"  Recording {N_STEPS} steps ({N_PERIODS}P)")

    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=False,
    )

    center = (N // 2, N // 2, N // 2)
    v_pulse = 0.001

    # SYMMETRIC pulse: equal amplitude on all 4 ports
    for p in range(4):
        engine.k4.V_inc[center[0], center[1], center[2], p] = v_pulse
    print(f"  Symmetric pulse: V_inc[{center}, all 4 ports] = {v_pulse}")

    # Pre-compute distance grid
    ix, iy, iz = np.indices((N, N, N))
    r_grid = np.sqrt((ix - center[0])**2 + (iy - center[1])**2 + (iz - center[2])**2)
    active_mask = np.zeros((N, N, N), dtype=bool)
    active_mask[PML:N-PML, PML:N-PML, PML:N-PML] = True

    # Concentric shells (active-region only)
    shell_radii = [1.0, 2.0, 3.0, 5.0, 7.0, 9.0, 11.0]
    shell_masks = []
    for r_target in shell_radii:
        # ±0.5 around r_target
        m = (r_grid >= r_target - 0.5) & (r_grid < r_target + 0.5) & active_mask
        shell_masks.append(m)
        print(f"    Shell r≈{r_target}: {m.sum()} sites")

    # Track energy-per-shell over time
    energy_per_shell = np.zeros((N_STEPS, len(shell_radii)))

    print(f"\n  Recording...", flush=True)
    t0 = time.time()
    last = t0
    for i in range(N_STEPS):
        engine.step()
        v_field_sq = np.sum(engine.k4.V_inc**2 + engine.k4.V_ref**2, axis=-1)
        for s_idx, m in enumerate(shell_masks):
            energy_per_shell[i, s_idx] = v_field_sq[m].sum()

        if (time.time() - last) > 30.0:
            t_p = (i + 1) * DT / COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s")

    # First-arrival time at each shell: time when energy first exceeds threshold
    # Threshold: 10× the early-time floor (estimated from step 0 of each shell)
    print(f"\n  First-arrival time at each shell:")
    arrivals = []
    for s_idx, r in enumerate(shell_radii):
        floor = energy_per_shell[0, s_idx]
        # threshold = max(10× floor, max energy / 100)
        max_energy = energy_per_shell[:, s_idx].max()
        threshold = max(10 * floor, max_energy * 0.01)
        if max_energy < 1e-15:
            print(f"    r={r}: NO arrival (max energy ≈ 0)")
            arrivals.append(None)
            continue
        arrival_step = np.argmax(energy_per_shell[:, s_idx] > threshold)
        if energy_per_shell[arrival_step, s_idx] <= threshold:
            arrival_step = -1
        arrival_time = arrival_step * DT
        arrivals.append((arrival_step, arrival_time, max_energy))
        print(f"    r={r:.1f}: arrival at step {arrival_step} (t={arrival_time:.3f} natural), "
              f"max energy={max_energy:.4e}")

    # Linear fit: c_eff = (r_n - r_1) / (t_n - t_1)
    valid = [(r, a[1]) for r, a in zip(shell_radii, arrivals) if a is not None and a[0] > 0]
    if len(valid) >= 2:
        r_vals = np.array([v[0] for v in valid])
        t_vals = np.array([v[1] for v in valid])
        # Fit r = c_eff·t + offset
        c_eff_fit = np.polyfit(t_vals, r_vals, 1)
        c_eff = c_eff_fit[0]
        offset = c_eff_fit[1]
        print(f"\n  Linear fit r(t) = c_eff·t + offset:")
        print(f"    c_eff = {c_eff:.4f} (Maxwell predicts c = 1.0)")
        print(f"    offset = {offset:.4f}")
        print(f"    Deviation from c: {(c_eff - 1.0) * 100:+.2f}%")
    else:
        c_eff = None
        print(f"\n  Insufficient arrivals for fit")

    # Verdict
    if c_eff is not None:
        if abs(c_eff - 1.0) < 0.05:
            verdict = f"PASS — c_eff = {c_eff:.4f} within 5% of c (linear Maxwell baseline confirmed)"
        elif abs(c_eff - 1.0) < 0.15:
            verdict = f"PARTIAL — c_eff = {c_eff:.4f}, ~10-15% off c (substrate dispersion)"
        else:
            verdict = f"FAIL — c_eff = {c_eff:.4f}, large deviation from c"
    else:
        verdict = "INDETERMINATE"
    print(f"\n  Verdict: {verdict}")

    out = {
        "test": "Foundation Audit Test 2 v2: dispersion (corrected metric)",
        "N": N, "PML": PML, "v_pulse": v_pulse,
        "n_periods": N_PERIODS, "n_steps": N_STEPS,
        "elapsed_s": elapsed,
        "shell_radii": shell_radii,
        "shell_arrivals": [{"r": r, "step": a[0], "time": a[1], "max_energy": a[2]}
                            if a else {"r": r, "step": None, "time": None, "max_energy": None}
                            for r, a in zip(shell_radii, arrivals)],
        "c_eff_fit": float(c_eff) if c_eff is not None else None,
        "deviation_from_c_pct": float((c_eff - 1.0) * 100) if c_eff is not None else None,
        "verdict": verdict,
        "energy_per_shell_first_50_steps": energy_per_shell[:50].tolist(),
    }
    out_path = Path(__file__).parent / "r10_v8_foundation_audit_t2_v2_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
