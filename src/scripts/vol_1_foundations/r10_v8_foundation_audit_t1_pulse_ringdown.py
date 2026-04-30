"""
Foundation Audit Test 1: Single-pulse ringdown.

Most fundamental engine bench test. Pulse a single K4 bond port at one
site at LOW amplitude (linear regime, well below saturation). Record
V_inc trajectory at the pulse site. FFT the ringdown to find the
substrate's natural resonance frequency at the local bond-pair scale.

Predictions (one of these should land):
  - ω_TL = c/bond_length = ω_C/√3 ≈ 0.577·ω_C   (TLM bond traversal)
  - ω_C = c/ℓ_node                              (corpus bootstrap-chain bond-pair LC tank)
  - πc/bond_length = (π/√3)·ω_C ≈ 1.81·ω_C       (half-wave bond resonance)
  - πc/(2·bond_length) = (π/(2√3))·ω_C ≈ 0.907·ω_C  (quarter-wave)
  - Some other lattice-mode frequency

Conditions:
  - Lattice: 16³ with PML thickness=4 (active region 8³)
  - Pulse amplitude: 0.01 V_SNAP (linear regime, S(A)≈1)
  - Pulse location: A-site at lattice center, port 0 only
  - Recording: 100 Compton periods at engine DT
  - Cosserat: enable_cosserat_self_terms=False, disable_cosserat_lc_force=True
    (pure K4-TLM K4 scatter+connect, no Cosserat coupling distorting the
    bond-pair test)

Decision criteria:
  - Find dominant FFT peak frequency at center site
  - Compare to predicted candidate frequencies
  - Establish baseline "the substrate naturally rings at f_X when pulsed"
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
    print("  Foundation Audit Test 1: single-pulse ringdown")
    print("=" * 78, flush=True)

    # Lattice config
    N = 16
    PML = 4
    DT = 1.0 / np.sqrt(2.0)
    COMPTON_PERIOD = 2.0 * np.pi  # ω_C = 1, T = 2π in natural units
    N_PERIODS = 100.0
    N_STEPS = int(N_PERIODS * COMPTON_PERIOD / DT)

    print(f"  Lattice: {N}³, PML={PML} (active region {N-2*PML}³)")
    print(f"  Engine DT = {DT:.4f} natural units, recording {N_STEPS} steps ({N_PERIODS} P)")
    print()

    # Engine: pure K4-TLM, no Cosserat coupling distorting the test
    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=False,
    )

    # Single pulse at center, port 0, low amplitude (linear regime)
    center = (N // 2, N // 2, N // 2)
    v_pulse = 0.01  # 1% of V_SNAP — well below saturation, linear Maxwell regime
    print(f"  Initial pulse: V_inc[{center[0]},{center[1]},{center[2]}, port=0] = {v_pulse}")
    print(f"  Linear regime (V_pulse << V_yield = V_SNAP since amplitude_convention='V_SNAP')")
    engine.k4.V_inc[center[0], center[1], center[2], 0] = v_pulse

    # Record V_inc at center port 0 over time
    print()
    print("Recording...", flush=True)
    v_traj = np.zeros(N_STEPS)

    t0 = time.time()
    last = t0
    for i in range(N_STEPS):
        engine.step()
        v_traj[i] = engine.k4.V_inc[center[0], center[1], center[2], 0]
        if (time.time() - last) > 30.0:
            t_p = (i + 1) * DT / COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)

    # Statistics on V at center
    print()
    print(f"  V_inc at center over recording:")
    print(f"    initial: {v_traj[0]:+.4e}")
    print(f"    max abs: {np.max(np.abs(v_traj)):+.4e}")
    print(f"    final: {v_traj[-1]:+.4e}")
    print(f"    RMS over full window: {np.sqrt(np.mean(v_traj**2)):.4e}")

    # FFT — full window first
    freqs_full = np.fft.rfftfreq(N_STEPS, d=DT)
    f_C = 1.0 / (2 * np.pi)  # Compton frequency in cycles/time-unit (since ω_C = 1 in natural)
    spec_full = np.abs(np.fft.rfft(v_traj - v_traj.mean()))

    # FFT — also windowed to skip initial pulse transient (first 5 P)
    skip_steps = int(5.0 * COMPTON_PERIOD / DT)
    v_windowed = v_traj[skip_steps:] - v_traj[skip_steps:].mean()
    freqs_w = np.fft.rfftfreq(len(v_windowed), d=DT)
    spec_w = np.abs(np.fft.rfft(v_windowed))

    def find_peaks(spec, freqs, k=5):
        idxs = np.argsort(spec)[::-1][:k]
        return [(int(i), float(freqs[i]), float(spec[i])) for i in idxs]

    peaks_full = find_peaks(spec_full, freqs_full)
    peaks_w = find_peaks(spec_w, freqs_w)

    print()
    print("  Top 5 FFT peaks (full window):")
    print(f"    idx       f (cycles/t)   ω/ω_C        magnitude")
    for p in peaks_full:
        ratio = (2 * np.pi * p[1]) / 1.0  # ω = 2π·f, normalize by ω_C=1
        print(f"    {p[0]:5d}    {p[1]:.6f}      {ratio:.4f}       {p[2]:.4e}")
    print()
    print(f"  Top 5 FFT peaks (windowed, skip first 5P transient):")
    print(f"    idx       f (cycles/t)   ω/ω_C        magnitude")
    for p in peaks_w:
        ratio = (2 * np.pi * p[1]) / 1.0
        print(f"    {p[0]:5d}    {p[1]:.6f}      {ratio:.4f}       {p[2]:.4e}")

    # Compare to candidate frequencies
    candidates = {
        "ω_TL = ω_C/√3 (TLM bond traversal)": 1.0 / np.sqrt(3.0),
        "ω_C (corpus bond-pair LC tank)": 1.0,
        "π/√3 · ω_C (half-wave bond res.)": np.pi / np.sqrt(3.0),
        "π/(2√3) · ω_C (quarter-wave)": np.pi / (2.0 * np.sqrt(3.0)),
        "2π/√3 · ω_C (full-wave)": 2.0 * np.pi / np.sqrt(3.0),
        "ω_C·√3 (sqrt-3 multiple)": np.sqrt(3.0),
    }

    dominant_omega = 2 * np.pi * peaks_w[0][1]
    print()
    print(f"  Dominant ω (windowed) = {dominant_omega:.4f} ω_C-natural")
    print(f"  Comparison to candidate frequencies:")
    print(f"    {'Candidate':<40} {'ω_pred':>10} {'pct off':>10}")
    for name, omega_pred in candidates.items():
        pct_off = abs(dominant_omega - omega_pred) / omega_pred * 100
        flag = " ★" if pct_off < 5 else ""
        print(f"    {name:<40} {omega_pred:>10.4f} {pct_off:>9.2f}%{flag}")

    # Save
    out = {
        "test": "Foundation Audit Test 1: single-pulse ringdown",
        "N": N,
        "PML": PML,
        "v_pulse_amplitude": v_pulse,
        "n_periods": N_PERIODS,
        "n_steps": N_STEPS,
        "DT": DT,
        "elapsed_recording_s": elapsed,
        "v_traj_first_100": v_traj[:100].tolist(),
        "v_traj_last_100": v_traj[-100:].tolist(),
        "v_traj_max_abs": float(np.max(np.abs(v_traj))),
        "v_traj_rms": float(np.sqrt(np.mean(v_traj**2))),
        "peaks_full": peaks_full,
        "peaks_windowed": peaks_w,
        "dominant_omega_windowed_in_omega_C_units": dominant_omega,
        "candidate_comparison": {
            name: {
                "omega_pred": float(omega_pred),
                "pct_off": float(abs(dominant_omega - omega_pred) / omega_pred * 100),
            }
            for name, omega_pred in candidates.items()
        },
    }
    out_path = Path(__file__).parent / "r10_v8_foundation_audit_t1_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
