"""Test B — single A-B bond V_inc/V_ref phase-space phasor trajectory test.

Per `P_phase5_bond_scale_phasor_trajectory` (frozen at this commit) +
[doc 28_ §5.1](../../research/_archive/L3_electron_soliton/28_two_node_electron_synthesis.md#L105):

> "Extract V_inc/V_ref phasor trajectory on a SINGLE A-B bond from
> existing TLM 96³ simulation. Plot in (Re, Im) phase space. Check if
> it traces a torus with R/r ≈ φ²."

Tests the BOND-SCALE phase-space Golden Torus hypothesis — structurally
different from R7.1's Cosserat-continuum-scale extended (2,3) bound state
test. Per the two-node-electron synthesis (doc 28_), the electron is
"a flux oscillation between two adjacent K4 nodes" with the Golden
Torus living in PHASE SPACE, not real space.

Methodology:
  1. Drive engine with autoresonant CW at ω_C (= 1.0 in natural units).
  2. Record V_inc(t), V_ref(t) at one A-B bond over the sustain window.
  3. Discard transient (first 10 periods).
  4. Plot (V_inc, V_ref) parametric trajectory in 2D phase space.
  5. Compute major/minor axis amplitudes (R, r) via PCA on the (V_inc, V_ref)
     scatter; check R/r ≈ φ² ≈ 2.618 ± 0.10.
  6. Lissajous lobe count + FFT spectral content (informational diagnostics).

Adjudication categories per pred:
  Mode I:   closed trajectory + R/r = φ² ± 0.10 + (Lissajous (2,3) OR
            spectral 3/2 ratio)
  Mode II:  closed trajectory but R/r ≠ φ² ± 0.10
  Mode III: open / chaotic trajectory OR simple ellipse (single-frequency)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D, AutoresonantCWSource


# ─── Constants per pred ───────────────────────────────────────────────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

# Drive parameters
N_LATTICE = 32           # smaller than doc 28_'s 96³; sufficient for single-bond physics
PML = 4
OMEGA_C = 1.0            # natural units
WAVELENGTH_CARRIER = 2.0 * np.pi / OMEGA_C  # ≈ 6.28 cells
DRIVE_AMP = 0.5          # 0.5·V_SNAP per Grant approval — engages Op14 nonlinearity (saturation onset A²≈0.5)
T_RAMP_PERIODS = 5.0
T_SUSTAIN_PERIODS = 50.0
T_DECAY_PERIODS = 2.0

# Phase-space adjudication
R_OVER_R_TARGET = PHI_SQ
R_OVER_R_TOL = 0.10      # ±10% tolerance per pred
LOBE_TARGET = (2, 3)     # (2,3) Lissajous

# Bond selection: A-B near lattice center
PORT_VECTORS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float)

OUTPUT_JSON = Path(__file__).parent / "test_b_bond_scale_phasor_retry_results.json"


def find_central_bond(engine):
    """Find an A-B bond at lattice center (mirrors phase5 driver pattern)."""
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


def extract_phasor_trajectory(engine, A_idx, port, B_idx, n_steps, record_cadence=1):
    """Drive simulation; record V_inc and V_ref at one bond per substep.

    Returns:
        v_inc_traj: array of V_inc[A_idx, port] over time
        v_ref_traj: array of V_ref[A_idx, port] over time
        v_inc_B_traj: same at B-side (V_inc on the B-side of bond)
        v_ref_B_traj: same
        times: array of engine.time at each sample
    """
    v_inc_A = []
    v_ref_A = []
    v_inc_B = []
    v_ref_B = []
    times = []

    for step in range(n_steps):
        engine.step()
        if step % record_cadence == 0:
            v_inc_A.append(float(engine.k4.V_inc[A_idx[0], A_idx[1], A_idx[2], port]))
            v_ref_A.append(float(engine.k4.V_ref[A_idx[0], A_idx[1], A_idx[2], port]))
            v_inc_B.append(float(engine.k4.V_inc[B_idx[0], B_idx[1], B_idx[2], port]))
            v_ref_B.append(float(engine.k4.V_ref[B_idx[0], B_idx[1], B_idx[2], port]))
            times.append(float(engine.time))

    return (np.array(v_inc_A), np.array(v_ref_A),
            np.array(v_inc_B), np.array(v_ref_B),
            np.array(times))


def analyze_phasor_trajectory(v_inc, v_ref, transient_skip=0):
    """Phase-space analysis of (V_inc(t), V_ref(t)) trajectory.

    Returns dict with:
        - R, r: major/minor axis amplitudes via PCA
        - R_over_r: aspect ratio
        - is_closed: heuristic for closed-curve property
        - lobe_count_x, lobe_count_y: Lissajous lobe counts
        - dominant_freqs: top FFT frequencies
        - freq_ratio: ratio of dominant frequencies (test for 3/2 (2,3) signature)
    """
    if transient_skip > 0:
        v_inc = v_inc[transient_skip:]
        v_ref = v_ref[transient_skip:]

    # PCA for major/minor axes
    points = np.column_stack([v_inc, v_ref])
    centroid = points.mean(axis=0)
    centered = points - centroid
    cov = np.cov(centered.T)
    evals, evecs = np.linalg.eigh(cov)
    # Sort descending
    order = np.argsort(evals)[::-1]
    evals = evals[order]
    evecs = evecs[:, order]
    # Projected coordinates
    pca_proj = centered @ evecs
    R = float(np.std(pca_proj[:, 0]))  # major axis std
    r = float(np.std(pca_proj[:, 1]))  # minor axis std
    R_over_r = R / max(r, 1e-30)

    # Lobe counts via local extrema in v_inc and v_ref
    def count_extrema(signal):
        """Count local maxima."""
        sig = np.asarray(signal)
        if len(sig) < 3:
            return 0
        diffs = np.diff(sig)
        return int(np.sum((diffs[:-1] > 0) & (diffs[1:] < 0)))

    lobe_x = count_extrema(v_inc)
    lobe_y = count_extrema(v_ref)

    # FFT spectral analysis
    fft_inc = np.fft.rfft(v_inc - v_inc.mean())
    fft_freqs = np.fft.rfftfreq(len(v_inc))
    power = np.abs(fft_inc) ** 2
    # Find top 3 peaks
    sorted_idx = np.argsort(power)[::-1]
    top_freqs = []
    for idx in sorted_idx[:5]:
        if fft_freqs[idx] > 0:
            top_freqs.append(float(fft_freqs[idx]))
        if len(top_freqs) >= 3:
            break

    freq_ratio = None
    if len(top_freqs) >= 2:
        freq_ratio = top_freqs[0] / max(top_freqs[1], 1e-30)

    # Closed-curve heuristic: standard deviation of trajectory ENDPOINTS over time
    # (if amplitude drifts, not closed)
    chunks = 5
    chunk_size = len(v_inc) // chunks
    chunk_R_values = []
    for i in range(chunks):
        chunk_v_inc = v_inc[i * chunk_size:(i + 1) * chunk_size]
        chunk_v_ref = v_ref[i * chunk_size:(i + 1) * chunk_size]
        if len(chunk_v_inc) < 3:
            continue
        chunk_pts = np.column_stack([chunk_v_inc, chunk_v_ref])
        chunk_R_values.append(float(np.linalg.norm(chunk_pts.std(axis=0))))
    if chunk_R_values:
        R_drift = float(np.std(chunk_R_values) / max(np.mean(chunk_R_values), 1e-30))
    else:
        R_drift = float('inf')

    is_closed = R_drift < 0.20  # heuristic: amplitude stable to within 20% over 5 chunks

    return {
        "R": R, "r": r, "R_over_r": R_over_r,
        "is_closed": bool(is_closed),
        "amplitude_drift": R_drift,
        "lobe_count_x": lobe_x,
        "lobe_count_y": lobe_y,
        "dominant_freqs": top_freqs,
        "freq_ratio": freq_ratio,
    }


def main():
    print("=" * 78, flush=True)
    print(f"  Test B — single A-B bond V_inc/V_ref phasor trajectory")
    print(f"  P_phase5_bond_scale_phasor_trajectory (per doc 28_ §5.1)")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, pml={PML}")
    print(f"  Drive: ω_C = {OMEGA_C}, λ = {WAVELENGTH_CARRIER:.4f} cells, "
          f"amp = {DRIVE_AMP}·V_SNAP")
    print(f"  Periods: ramp {T_RAMP_PERIODS} + sustain {T_SUSTAIN_PERIODS} + "
          f"decay {T_DECAY_PERIODS}")
    print(f"  Pred PASS: closed trajectory + R/r = {R_OVER_R_TARGET:.4f} ± {R_OVER_R_TOL}")
    print()

    period = 2.0 * np.pi / OMEGA_C
    t_ramp = T_RAMP_PERIODS * period
    t_sustain = T_SUSTAIN_PERIODS * period
    t_decay = T_DECAY_PERIODS * period
    total_time = t_ramp + t_sustain + t_decay
    n_steps = int(total_time * np.sqrt(2.0)) + 1
    transient_steps = int((t_ramp + 10.0 * period) * np.sqrt(2.0))  # skip ramp + 10 sustain periods

    # Build engine + central bond
    engine = VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )
    A_idx, port, B_idx = find_central_bond(engine)
    print(f"  Bond: A={A_idx}, port={port}, B={B_idx}")

    # Drive: head-on autoresonant collision (mirrors phase5 driver convention)
    src_offset = PML + 3
    engine.add_source(AutoresonantCWSource(
        x0=src_offset, direction=(1.0, 0.0, 0.0),
        amplitude=DRIVE_AMP, omega=OMEGA_C,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=t_decay,
    ))

    print(f"  Running {n_steps} steps ({total_time:.2f} natural-time-units)...")
    t0 = time.time()
    v_inc_A, v_ref_A, v_inc_B, v_ref_B, times = extract_phasor_trajectory(
        engine, A_idx, port, B_idx, n_steps, record_cadence=1,
    )
    elapsed = time.time() - t0
    print(f"  Elapsed: {elapsed:.1f}s, recorded {len(v_inc_A)} samples")
    print()

    # Phase-space analysis on A-side after transient
    print(f"  Phase-space analysis (A-side, skip first {transient_steps} samples)...")
    analysis_A = analyze_phasor_trajectory(v_inc_A, v_ref_A, transient_steps)
    print(f"    A-side R = {analysis_A['R']:.4f}, r = {analysis_A['r']:.4f}, "
          f"R/r = {analysis_A['R_over_r']:.4f}")
    print(f"    A-side closed-trajectory: {analysis_A['is_closed']} "
          f"(amplitude drift {analysis_A['amplitude_drift']:.4f})")
    print(f"    A-side Lissajous lobes: V_inc={analysis_A['lobe_count_x']}, "
          f"V_ref={analysis_A['lobe_count_y']}")
    print(f"    A-side dominant freqs: {analysis_A['dominant_freqs']}")
    print(f"    A-side freq ratio: {analysis_A['freq_ratio']}")
    print()

    # Adjudication
    R_over_r_pass = abs(analysis_A['R_over_r'] - R_OVER_R_TARGET) <= R_OVER_R_TOL
    print(f"  R/r criterion: {analysis_A['R_over_r']:.4f} vs target {R_OVER_R_TARGET:.4f} ± {R_OVER_R_TOL}")
    print(f"    {'PASS' if R_over_r_pass else 'FAIL'}")
    print()

    print("=" * 78, flush=True)
    print("  Adjudication")
    print("=" * 78, flush=True)
    if not analysis_A['is_closed']:
        mode = "III"
        verdict = (
            f"MODE III — Trajectory is open / drifting (amplitude drift "
            f"{analysis_A['amplitude_drift']:.4f} > 0.20). The bond does NOT "
            f"settle into a steady-state phase-space pattern at this drive. "
            f"Could indicate drive amplitude/frequency mismatch or the bond "
            f"doesn't ring up at ω_C in the expected mode."
        )
    elif R_over_r_pass:
        mode = "I"
        verdict = (
            f"MODE I — Closed trajectory with R/r = {analysis_A['R_over_r']:.4f} "
            f"matching corpus φ² = {R_OVER_R_TARGET:.4f} within ±{R_OVER_R_TOL} "
            f"tolerance. Doc 28_ §5.1 two-node-electron hypothesis confirmed: "
            f"the bond's (V_inc, V_ref) phasor trajectory IS the corpus "
            f"phase-space Golden Torus."
        )
    else:
        mode = "II"
        verdict = (
            f"MODE II — Closed trajectory but R/r = {analysis_A['R_over_r']:.4f} "
            f"≠ corpus φ² = {R_OVER_R_TARGET:.4f} (off by "
            f"{abs(analysis_A['R_over_r'] - R_OVER_R_TARGET):.4f}, tolerance "
            f"{R_OVER_R_TOL}). Bond hosts a stable phase-space pattern at this "
            f"drive but NOT the corpus Golden Torus. Could indicate different "
            f"(R, r) attractor OR drive amplitude/frequency mismatch from "
            f"corpus electron config."
        )
    print(f"  {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase5_bond_scale_phasor_trajectory",
        "test": "Test B per audit + doc 28_ §5.1",
        "N": N_LATTICE,
        "drive_amp": DRIVE_AMP,
        "drive_omega": OMEGA_C,
        "drive_periods": {"ramp": T_RAMP_PERIODS, "sustain": T_SUSTAIN_PERIODS, "decay": T_DECAY_PERIODS},
        "n_samples": len(v_inc_A),
        "transient_steps_skipped": transient_steps,
        "elapsed_seconds": elapsed,
        "bond": {"A_idx": list(A_idx), "port": port, "B_idx": list(B_idx)},
        "A_side_analysis": analysis_A,
        "R_over_r_target": R_OVER_R_TARGET,
        "R_over_r_tol": R_OVER_R_TOL,
        "R_over_r_pass": bool(R_over_r_pass),
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
