"""
r10 EE Phase A — Control B1: HELICAL_PITCH=0 FFT control.

Tests whether the engine's V_inc dominant frequency at 1.5·ω_C is
substrate-forced (cavity mode) vs helical-IC-driven (toroidal-component
artifact). HELICAL_PITCH=0 zeroes the IC's toroidal component while
keeping V_AMP = 0.95 unchanged. If FFT still shows 1.5·ω_C dominant,
substrate-forced. If shifts, helical-IC-driven.
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
    print("  r10 EE Phase A — Control B1: HELICAL_PITCH=0 FFT")
    print("  V_AMP = 0.95 (unchanged), HELICAL_PITCH = 0.0 (no toroidal)")
    print("=" * 78, flush=True)

    nodes, bonds = v8.build_chair_ring(v8.CENTER)
    a_0_per_node, _ = v8.compute_a_0_at_ring_nodes(
        nodes, v8.A_AMP_POL, helical_pitch=0.0,  # ← key change
    )

    engine = VacuumEngine3D.from_args(
        N=v8.N_LATTICE, pml=v8.PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )
    print("Applying v8 helical Beltrami IC with HELICAL_PITCH=0...", flush=True)
    v8.initialize_helical_beltrami_ic(
        engine, nodes, bonds, a_0_per_node,
        v8.K_BELTRAMI, v8.V_AMP, v8.PHI_AMP,
    )

    N_STEPS = v8.N_RECORDING_STEPS
    print(f"Recording {N_STEPS} steps...", flush=True)
    v_inc = np.zeros((N_STEPS, 6, 4), dtype=np.float32)
    omega = np.zeros((N_STEPS, 6, 3), dtype=np.float32)

    t0 = time.time()
    last = t0
    for i in range(N_STEPS):
        engine.step()
        for n_idx, node in enumerate(nodes):
            ix, iy, iz = node
            v_inc[i, n_idx, :] = engine.k4.V_inc[ix, iy, iz, :]
            omega[i, n_idx, :] = engine.cos.omega[ix, iy, iz, :]
        if (time.time() - last) > 30.0:
            t_p = (i + 1) * v8.DT / v8.COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)

    # FFT at ring node 0
    sw_start = N_STEPS // 4
    v_inc_n0 = np.linalg.norm(v_inc[sw_start:, 0, :], axis=1)
    omega_n0 = np.linalg.norm(omega[sw_start:, 0, :], axis=1)
    n_samples = len(v_inc_n0)
    freqs = np.fft.rfftfreq(n_samples, d=v8.DT)
    f_C = 1.0 / (2 * np.pi)

    def fft_mag(x):
        return np.abs(np.fft.rfft(x - x.mean()))

    def find_peaks(spec, k=3):
        idxs = np.argsort(spec)[::-1][:k]
        return [(int(i), float(freqs[i]), float(spec[i])) for i in idxs]

    fft_v_inc = fft_mag(v_inc_n0)
    fft_omega = fft_mag(omega_n0)
    v_inc_peaks = find_peaks(fft_v_inc)
    omega_peaks = find_peaks(fft_omega)

    print()
    print("=" * 78, flush=True)
    print("  Control B1 FFT result")
    print("=" * 78, flush=True)
    print(f"  HELICAL_PITCH = 0.0")
    print(f"  V_inc top-3 peaks (idx, f, mag, ratio to f_C):")
    for p in v_inc_peaks:
        ratio = p[1] / f_C
        print(f"    idx={p[0]:5d}, f={p[1]:.6f}, mag={p[2]:.4e}, f/f_C = {ratio:.4f}")
    print(f"  ω top-3 peaks (idx, f, mag, ratio to f_C):")
    for p in omega_peaks:
        ratio = p[1] / f_C
        print(f"    idx={p[0]:5d}, f={p[1]:.6f}, mag={p[2]:.4e}, f/f_C = {ratio:.4f}")

    # Compare to baseline (HELICAL_PITCH=1/(2π))
    baseline_v_inc_top = 1.4798  # from prior run
    new_top_ratio = v_inc_peaks[0][1] / f_C
    delta = new_top_ratio - baseline_v_inc_top
    print()
    print(f"  Baseline V_inc dominant (HELICAL_PITCH=1/2π): {baseline_v_inc_top:.4f} × f_C")
    print(f"  Control V_inc dominant (HELICAL_PITCH=0):     {new_top_ratio:.4f} × f_C")
    print(f"  Δ from baseline: {delta:+.4f} × f_C")

    if abs(delta) < 0.05:
        verdict = "SUBSTRATE-FORCED — engine frequency unchanged with HELICAL_PITCH=0"
    elif abs(delta) > 0.2:
        verdict = "IC-DRIVEN — engine frequency shifts substantially with HELICAL_PITCH"
    else:
        verdict = "MIXED — partial dependence on HELICAL_PITCH"
    print(f"  Verdict: {verdict}")

    out = {
        "test": "Control B1: HELICAL_PITCH=0 FFT control",
        "V_AMP": 0.95,
        "HELICAL_PITCH": 0.0,
        "n_steps": N_STEPS,
        "elapsed_recording_s": elapsed,
        "v_inc_top3_peaks": v_inc_peaks,
        "omega_top3_peaks": omega_peaks,
        "v_inc_dominant_ratio_to_fC": new_top_ratio,
        "baseline_v_inc_dominant_ratio_to_fC": baseline_v_inc_top,
        "delta_from_baseline": delta,
        "verdict": verdict,
    }
    out_path = Path(__file__).parent / "r10_v8_ee_phase_a_b1_pitch0_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
