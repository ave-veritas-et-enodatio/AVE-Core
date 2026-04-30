"""
r10 EE Phase A — Control B5b: noise-floor reference.

V_AMP=0 control for B5 far-field test. Same engine config + recording
window as B5 main run, but IC seeds NO field (V_AMP=0). Measures
engine's intrinsic numerical noise floor for V_inc, V_ref, ω, u_dot
in the active region.

If B5b shows 1/r structure too: B5's 1/r decay is engine numerical
noise pattern, not real far-field signal. If B5b is flat or random:
B5's 1/r is real (chair-ring's displacement-current loop near-field).
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).parent))

from ave.topological.vacuum_engine import VacuumEngine3D

import r10_path_alpha_v8_corrected_measurements as v8


def main():
    print("=" * 78, flush=True)
    print("  r10 EE Phase A — Control B5b: noise-floor (V_AMP=0)")
    print("=" * 78, flush=True)

    nodes, _ = v8.build_chair_ring(v8.CENTER)
    _, centroid = v8.compute_a_0_at_ring_nodes(nodes, v8.A_AMP_POL, v8.HELICAL_PITCH)

    engine = VacuumEngine3D.from_args(
        N=v8.N_LATTICE, pml=v8.PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )
    # NO IC applied — engine starts with all fields at zero
    print("No IC applied — V_AMP=0 baseline (zero fields at t=0)", flush=True)

    N_STEPS = v8.N_RECORDING_STEPS
    sw_start = N_STEPS // 4
    nx = engine.k4.nx

    print(f"Recording {N_STEPS} steps; accumulating from step {sw_start}...", flush=True)

    V_inc_sum = np.zeros((nx, nx, nx, 4), dtype=np.float64)
    V_ref_sum = np.zeros((nx, nx, nx, 4), dtype=np.float64)
    omega_sum = np.zeros((nx, nx, nx, 3), dtype=np.float64)
    n_avg_steps = 0

    t0 = time.time()
    last = t0
    for i in range(N_STEPS):
        engine.step()
        if i >= sw_start:
            V_inc_sum += engine.k4.V_inc
            V_ref_sum += engine.k4.V_ref
            omega_sum += engine.cos.omega
            n_avg_steps += 1
        if (time.time() - last) > 30.0:
            t_p = (i + 1) * v8.DT / v8.COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)

    V_inc_DC = V_inc_sum / n_avg_steps
    V_ref_DC = V_ref_sum / n_avg_steps
    omega_DC = omega_sum / n_avg_steps

    # E vector reconstruction (same Moore-Penrose as B5)
    PORT_DIRS = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]],
                          dtype=np.float64) / np.sqrt(3.0)
    bond_length = np.sqrt(3.0)
    V_total_DC = V_inc_DC + V_ref_DC

    E_DC = np.zeros((nx, nx, nx, 3), dtype=np.float64)
    for p in range(4):
        for axis in range(3):
            E_DC[..., axis] += PORT_DIRS[p, axis] * V_total_DC[..., p] / bond_length
    E_DC *= (3.0 / 4.0)
    B_DC = omega_DC.copy()

    PML = v8.PML
    active_min = PML
    active_max = nx - PML
    active_mask = np.zeros((nx, nx, nx), dtype=bool)
    active_mask[active_min:active_max, active_min:active_max, active_min:active_max] = True

    cx, cy, cz = centroid
    ix, iy, iz = np.indices((nx, nx, nx))
    dx = ix - cx; dy = iy - cy; dz = iz - cz
    r = np.sqrt(dx**2 + dy**2 + dz**2)

    E_mag = np.linalg.norm(E_DC, axis=-1)
    B_mag = np.linalg.norm(B_DC, axis=-1)

    print()
    print("  Noise-floor: |E|_DC and |B|_DC per shell")
    print(f"  r       <|E|_DC>      <|B|_DC>      n_sites")

    r_bins = np.arange(3, 11)
    r_centers = (r_bins[:-1] + r_bins[1:]) / 2.0
    E_floor = []
    B_floor = []
    for r_low in r_bins[:-1]:
        r_high = r_low + 1
        shell_mask = (r >= r_low) & (r < r_high) & active_mask
        n_in_shell = int(shell_mask.sum())
        if n_in_shell > 0:
            E_floor.append(float(E_mag[shell_mask].mean()))
            B_floor.append(float(B_mag[shell_mask].mean()))
        else:
            E_floor.append(0.0)
            B_floor.append(0.0)
        print(f"    {r_low+0.5:.1f}   {E_floor[-1]:.4e}   {B_floor[-1]:.4e}   {n_in_shell:5d}")

    # Compare to B5 main run
    # B5 results (hardcoded for direct comparison; from main run output):
    b5_E = [2.8082e-08, 1.1300e-08, 1.5225e-08, 8.9369e-09, 1.1699e-08, 1.0032e-08, 6.3441e-09]
    b5_B = [3.7865e-06, 1.6215e-06, 1.8735e-06, 1.5491e-06, 1.5266e-06, 1.1339e-06, 1.1029e-06]

    print()
    print("  Comparison: B5 (V_AMP=0.95 trapped state) vs B5b (V_AMP=0 noise floor):")
    print(f"  r       B5 |E|         B5b |E|       ratio E   B5 |B|        B5b |B|       ratio B")
    for i, rc in enumerate(r_centers):
        ratio_E = b5_E[i] / max(E_floor[i], 1e-30)
        ratio_B = b5_B[i] / max(B_floor[i], 1e-30)
        print(f"    {rc:.1f}   {b5_E[i]:.3e}   {E_floor[i]:.3e}   {ratio_E:6.1f}   "
              f"{b5_B[i]:.3e}   {B_floor[i]:.3e}   {ratio_B:6.1f}")

    # Power-law fit on noise floor
    valid_E = [m > 1e-30 for m in E_floor]
    if sum(valid_E) >= 3:
        r_v = r_centers[valid_E]
        E_v = np.array(E_floor)[valid_E]
        slope_E, _ = np.polyfit(np.log(r_v), np.log(E_v), 1)
    else:
        slope_E = None
    valid_B = [m > 1e-30 for m in B_floor]
    if sum(valid_B) >= 3:
        r_v = r_centers[valid_B]
        B_v = np.array(B_floor)[valid_B]
        slope_B, _ = np.polyfit(np.log(r_v), np.log(B_v), 1)
    else:
        slope_B = None

    print()
    print(f"  Noise-floor power-law slopes:")
    print(f"    |E| slope: {slope_E:+.4f}" if slope_E is not None else "    |E| slope: N/A")
    print(f"    |B| slope: {slope_B:+.4f}" if slope_B is not None else "    |B| slope: N/A")
    print(f"  B5 main slopes were: |E| -1.10, |B| -1.04")

    # Verdict
    print()
    if E_floor[0] > 0 and b5_E[0] > 0:
        ratio_E_inner = b5_E[0] / E_floor[0]
        ratio_B_inner = b5_B[0] / B_floor[0]
        if ratio_E_inner > 5 and ratio_B_inner > 5:
            verdict = ("REAL SIGNAL: B5 fields are >5× above noise floor. "
                       "1/r structure is real loop-near-field signature, not engine noise.")
        elif ratio_E_inner > 2 or ratio_B_inner > 2:
            verdict = ("MARGINAL SIGNAL: B5 fields are 2-5× above noise. Real signal "
                       "above floor but precision limited.")
        else:
            verdict = ("AT NOISE FLOOR: B5 fields not significantly above engine "
                       "numerical noise; 1/r structure may be noise pattern.")
    else:
        verdict = "Indeterminate (zero values prevent ratio calculation)"
    print(f"  Verdict: {verdict}")

    out = {
        "test": "Control B5b: noise-floor (V_AMP=0)",
        "elapsed_recording_s": elapsed,
        "n_avg_steps": int(n_avg_steps),
        "E_floor_per_shell": E_floor,
        "B_floor_per_shell": B_floor,
        "B5_main_E_per_shell": b5_E,
        "B5_main_B_per_shell": b5_B,
        "E_signal_to_noise_per_shell": [b5_E[i]/max(E_floor[i],1e-30) for i in range(len(r_centers))],
        "B_signal_to_noise_per_shell": [b5_B[i]/max(B_floor[i],1e-30) for i in range(len(r_centers))],
        "noise_floor_E_slope": float(slope_E) if slope_E is not None else None,
        "noise_floor_B_slope": float(slope_B) if slope_B is not None else None,
        "B5_main_E_slope": -1.10,
        "B5_main_B_slope": -1.04,
        "verdict": verdict,
    }
    out_path = Path(__file__).parent / "r10_v8_ee_phase_a_b5b_noise_floor_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
