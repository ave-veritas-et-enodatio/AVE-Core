"""
r10 EE Phase A — Control B6: long-window stability test for BEMF feedback.

Grant 2026-04-29 question: does V_DC stay bounded (some feedback working)
or grow linearly (no Faraday BEMF / no proper back-reaction)?

The chair-ring trapped state at v8 config has V_DC ≈ 0.158·V_AMP at A-sites
over a 200P recording. If this is a true equilibrium (feedback bounding it),
V_DC should stay constant across longer recording windows. If it's an early
snapshot of a slowly drifting configuration, V_DC will change over time.

Test: 800P recording at v8 baseline (UNCHANGED). Compute V_DC per 100P window
(7 sliding windows). Check stability across windows.

This complements the B2 result (Faraday's law violated 99.98% on the
discrete loop): even though Faraday-law BEMF is absent, Op14 z_local
impedance modulation per Q1 resolution may provide an alternative
feedback mechanism that bounds the saturation rectification.

If V_DC stable across 700P → some feedback works (likely Op14)
If V_DC drifts → no proper feedback, 200P snapshot was misleading
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
    print("  r10 EE Phase A — Control B6: long-window stability (BEMF test)")
    print("=" * 78, flush=True)

    nodes, bonds = v8.build_chair_ring(v8.CENTER)
    a_0_per_node, centroid = v8.compute_a_0_at_ring_nodes(
        nodes, v8.A_AMP_POL, v8.HELICAL_PITCH
    )

    engine = VacuumEngine3D.from_args(
        N=v8.N_LATTICE, pml=v8.PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )
    print("Applying v8 helical Beltrami IC (UNCHANGED)...", flush=True)
    v8.initialize_helical_beltrami_ic(
        engine, nodes, bonds, a_0_per_node,
        v8.K_BELTRAMI, v8.V_AMP, v8.PHI_AMP,
    )

    # 800P recording = 4× the v8 baseline window
    N_PERIODS = 800.0
    N_STEPS = int(N_PERIODS * v8.COMPTON_PERIOD / v8.DT)
    print(f"Recording {N_STEPS} steps ({N_PERIODS}P)...", flush=True)

    # Capture only ring nodes (small memory)
    v_inc_ring = np.zeros((N_STEPS, 6, 4), dtype=np.float32)
    omega_ring = np.zeros((N_STEPS, 6, 3), dtype=np.float32)

    t0 = time.time()
    last = t0
    for i in range(N_STEPS):
        engine.step()
        for n_idx, node in enumerate(nodes):
            ix, iy, iz = node
            v_inc_ring[i, n_idx, :] = engine.k4.V_inc[ix, iy, iz, :]
            omega_ring[i, n_idx, :] = engine.cos.omega[ix, iy, iz, :]
        if (time.time() - last) > 60.0:
            t_p = (i + 1) * v8.DT / v8.COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)

    # Identify A-sites (3 of 6 ring nodes)
    a_site_indices = [i for i, n in enumerate(nodes) if all(c % 2 == 0 for c in n)]
    print(f"  A-site indices: {a_site_indices}")

    # Compute V_DC per port per A-site for sliding 100P windows
    steps_per_period = v8.COMPTON_PERIOD / v8.DT
    window_size_steps = int(100.0 * steps_per_period)  # 100P window
    n_windows = int(N_PERIODS // 100) - 1  # skip first 100P transient
    print(f"  Windows: {n_windows}, each {window_size_steps} steps (100P)")
    print(f"  Window 0 = [100P, 200P], Window 1 = [200P, 300P], ... etc.")

    # V_DC per A-site per port per window: shape (n_windows, n_a_sites, 4)
    V_DC_windows = np.zeros((n_windows, len(a_site_indices), 4), dtype=np.float64)
    omega_DC_windows = np.zeros((n_windows, 6, 3), dtype=np.float64)

    for w in range(n_windows):
        start = (w + 1) * window_size_steps  # skip 100P transient
        end = (w + 2) * window_size_steps
        for a_i, ring_idx in enumerate(a_site_indices):
            V_DC_windows[w, a_i, :] = v_inc_ring[start:end, ring_idx, :].mean(axis=0)
        omega_DC_windows[w, :, :] = omega_ring[start:end, :, :].mean(axis=0)

    # Print V_DC magnitude per A-site per window
    print()
    print("  V_DC magnitude per A-site, per 100P window:")
    print(f"    Window:        ", " ".join([f"[{w*100+100:3d},{w*100+200:3d}]P" for w in range(n_windows)]))
    for a_i, ring_idx in enumerate(a_site_indices):
        mags = [float(np.linalg.norm(V_DC_windows[w, a_i, :])) for w in range(n_windows)]
        mag_str = "  ".join([f"{m:.4f}    " for m in mags])
        print(f"    A_{ring_idx} (node {ring_idx}): {mag_str}")

    # Drift analysis: linear fit through windows for each A-site
    print()
    print("  V_DC magnitude drift analysis (linear fit across windows):")
    drifts = []
    for a_i, ring_idx in enumerate(a_site_indices):
        mags = np.array([float(np.linalg.norm(V_DC_windows[w, a_i, :])) for w in range(n_windows)])
        if len(mags) >= 2:
            slope = np.polyfit(np.arange(len(mags)), mags, 1)[0]
            mean_mag = mags.mean()
            relative_drift = slope / max(mean_mag, 1e-12)
            drifts.append({"a_site": ring_idx, "slope_per_window": float(slope),
                           "mean": float(mean_mag), "relative_drift": float(relative_drift)})
            print(f"    A_{ring_idx}: slope = {slope:+.5f}/window  mean = {mean_mag:.5f}  "
                  f"relative drift = {relative_drift*100:+.3f}% per 100P")

    # ω_DC drift at each ring node
    print()
    print("  |ω_DC| per ring node, per 100P window:")
    print(f"    Window:        ", " ".join([f"[{w*100+100:3d},{w*100+200:3d}]P" for w in range(n_windows)]))
    omega_drifts = []
    for ring_idx in range(6):
        mags = np.array([float(np.linalg.norm(omega_DC_windows[w, ring_idx, :])) for w in range(n_windows)])
        mag_str = "  ".join([f"{m:.3e}" for m in mags])
        print(f"    Node {ring_idx}: {mag_str}")
        if len(mags) >= 2:
            slope = np.polyfit(np.arange(len(mags)), mags, 1)[0]
            omega_drifts.append(float(slope))

    # Verdict
    max_relative_drift = max(abs(d["relative_drift"]) for d in drifts) if drifts else 0
    max_relative_drift_pct = max_relative_drift * 100

    print()
    print(f"  Max V_DC relative drift across 700P (window 0 → window {n_windows-1}):")
    print(f"    {max_relative_drift_pct:+.3f}% per 100P window")
    print(f"    Total drift over {n_windows*100}P: ~{max_relative_drift_pct * n_windows:+.2f}%")

    if max_relative_drift_pct < 1:
        verdict = (f"STABLE: V_DC drift < 1% per 100P (~{max_relative_drift_pct*n_windows:+.1f}% "
                   f"over {n_windows*100}P). Some feedback mechanism (likely Op14 z_local "
                   f"per Q1) is bounding the saturation rectification, even without proper "
                   f"Faraday-law BEMF.")
    elif max_relative_drift_pct < 5:
        verdict = (f"PARTIALLY DRIFTING: V_DC drift {max_relative_drift_pct:.1f}% per 100P. "
                   f"Feedback is partial; equilibrium not fully reached at 200P recording.")
    else:
        verdict = (f"DRIFTING: V_DC drift {max_relative_drift_pct:.1f}% per 100P. "
                   f"No proper feedback; 200P snapshot was misleading; configuration is "
                   f"slowly evolving.")
    print(f"\n  Verdict: {verdict}")

    out = {
        "test": "Control B6: long-window stability (BEMF feedback test)",
        "elapsed_recording_s": elapsed,
        "n_periods_total": N_PERIODS,
        "n_windows": n_windows,
        "window_size_periods": 100,
        "V_DC_windows": V_DC_windows.tolist(),
        "omega_DC_windows": omega_DC_windows.tolist(),
        "V_DC_drifts": drifts,
        "max_relative_drift_per_100P_pct": max_relative_drift_pct,
        "verdict": verdict,
    }
    out_path = Path(__file__).parent / "r10_v8_ee_phase_a_b6_long_window_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
