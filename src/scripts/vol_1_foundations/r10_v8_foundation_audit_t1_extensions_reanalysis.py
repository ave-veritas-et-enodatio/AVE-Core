"""
Foundation Audit T1 Extensions — re-analysis with proper band-pass filter.

Original t1_extensions analysis only filtered Nyquist edge but picked up
low-frequency FFT leakage as dominant. Re-running the same engine setups
with band-pass filter on FFT (skip ω < 0.5 and ω > 4 = exclude both
low-f leakage and Nyquist artifact) to find the physical resonance.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D


def run_pulse_with_bandpass(N, v_pulse, enable_cos_self, label, n_periods=100):
    """Same as Test 1 main but with proper band-pass FFT analysis."""
    PML = max(2, N // 4)
    DT = 1.0 / np.sqrt(2.0)
    COMPTON_PERIOD = 2.0 * np.pi
    N_STEPS = int(n_periods * COMPTON_PERIOD / DT)

    print(f"\n  [{label}] N={N}, PML={PML}, V_pulse={v_pulse}, "
          f"cosserat_self={enable_cos_self}, recording {n_periods}P", flush=True)

    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=enable_cos_self,
    )

    center = (N // 2, N // 2, N // 2)
    engine.k4.V_inc[center[0], center[1], center[2], 0] = v_pulse

    v_traj = np.zeros(N_STEPS)
    t0 = time.time()
    for i in range(N_STEPS):
        engine.step()
        v_traj[i] = engine.k4.V_inc[center[0], center[1], center[2], 0]
    elapsed = time.time() - t0

    # FFT, skip 5P transient
    skip_steps = int(5.0 * COMPTON_PERIOD / DT)
    v_w = v_traj[skip_steps:] - v_traj[skip_steps:].mean()
    freqs = np.fft.rfftfreq(len(v_w), d=DT)
    spec = np.abs(np.fft.rfft(v_w))

    # Band-pass: ω ∈ [0.5, 3.0] ω_C-natural — excludes low-f leakage AND
    # full Nyquist cluster (Nyquist cluster extends from ~3.5 to π·√2 ≈ 4.44)
    omega_per_freq = 2 * np.pi * freqs
    bandpass = (omega_per_freq >= 0.5) & (omega_per_freq <= 3.0)
    spec_bp = spec * bandpass

    # Top 5 in band-pass
    top_idxs = np.argsort(spec_bp)[::-1][:5]
    peaks = [(int(i), float(freqs[i]), float(spec[i]), float(omega_per_freq[i]))
             for i in top_idxs]

    print(f"    elapsed {elapsed:.1f}s")
    print(f"    Top 5 BAND-PASS peaks (0.5 ≤ ω ≤ 4.0 ω_C):")
    for p in peaks:
        print(f"      idx={p[0]:5d}  ω/ω_C={p[3]:.4f}  mag={p[2]:.3e}")

    return {
        "label": label,
        "N": N, "PML": PML, "v_pulse": v_pulse,
        "enable_cosserat_self_terms": enable_cos_self,
        "n_periods": n_periods, "elapsed_s": elapsed,
        "bandpass_top5_omega": [p[3] for p in peaks],
        "bandpass_top5_mag": [p[2] for p in peaks],
        "v_traj_max_abs": float(np.max(np.abs(v_traj))),
    }


def main():
    print("=" * 78, flush=True)
    print("  Foundation Audit Test 1 Extensions — band-pass re-analysis")
    print("  Filter: ω ∈ [0.5, 4.0] ω_C (exclude low-f leakage + Nyquist)")
    print("=" * 78, flush=True)

    results = []

    print("\n=== T1.1: Lattice-size scan ===")
    for N in [8, 16, 24]:
        results.append(run_pulse_with_bandpass(N=N, v_pulse=0.01, enable_cos_self=False,
                                                label=f"T1.1 N={N}"))

    print("\n=== T1.3: Saturated amplitude ===")
    results.append(run_pulse_with_bandpass(N=16, v_pulse=0.95, enable_cos_self=False,
                                            label="T1.3 V_pulse=0.95"))

    print("\n=== T1.4: Cosserat self-terms enabled ===")
    results.append(run_pulse_with_bandpass(N=16, v_pulse=0.01, enable_cos_self=True,
                                            label="T1.4 Cosserat ON"))

    # Summary
    print("\n" + "=" * 78, flush=True)
    print("  Summary: dominant band-pass ω across variations")
    print("  Baseline (Test 1 main, N=16, V=0.01, CosSelf=False, 100P): ω=1.50·ω_C")
    print("=" * 78, flush=True)
    print(f"  {'Label':<28} {'N':>3} {'V_pulse':>8} {'CosSelf':>7} {'ω_dom':>8} {'Δ %':>8}")
    omega_baseline = 1.50
    for r in results:
        cos_str = "True" if r["enable_cosserat_self_terms"] else "False"
        omega = r["bandpass_top5_omega"][0]
        delta = (omega - omega_baseline) / omega_baseline * 100
        flag = " ★" if abs(delta) < 5 else " ⚠"
        print(f"  {r['label']:<28} {r['N']:>3} {r['v_pulse']:>8.3f} {cos_str:>7} "
              f"{omega:>8.4f} {delta:>+7.2f}%{flag}")

    print()
    print("Verdicts:")

    if all(abs(r["bandpass_top5_omega"][0] - omega_baseline) / omega_baseline < 0.05
           for r in results if r["v_pulse"] == 0.01 and not r["enable_cosserat_self_terms"]):
        print("  T1.1 lattice scan: ω stays constant within 5% across N → substrate-intrinsic confirmed")

    sat_omega = next((r["bandpass_top5_omega"][0] for r in results
                       if r["label"].startswith("T1.3")), None)
    if sat_omega is not None:
        delta = (sat_omega - omega_baseline) / omega_baseline * 100
        if abs(delta) < 5:
            print(f"  T1.3 saturated: ω = {sat_omega:.3f} ({delta:+.1f}% from baseline) → "
                  f"persists at saturation, confirms substrate-intrinsic regardless of regime")
        else:
            print(f"  T1.3 saturated: ω = {sat_omega:.3f} ({delta:+.1f}% from baseline) → "
                  f"shifts at saturation; nonlinear regime modifies frequency")

    cos_omega = next((r["bandpass_top5_omega"][0] for r in results
                       if r["label"].startswith("T1.4")), None)
    if cos_omega is not None:
        delta = (cos_omega - omega_baseline) / omega_baseline * 100
        if abs(delta) < 5:
            print(f"  T1.4 Cosserat ON: ω = {cos_omega:.3f} ({delta:+.1f}% from baseline) → "
                  f"K4-Cosserat coupling does NOT distort substrate-intrinsic K4-TLM frequency")
        else:
            print(f"  T1.4 Cosserat ON: ω = {cos_omega:.3f} ({delta:+.1f}% from baseline) → "
                  f"Cosserat coupling shifts the resonance; coupling matters")

    out_path = Path(__file__).parent / "r10_v8_foundation_audit_t1_extensions_bandpass_results.json"
    out_path.write_text(json.dumps({"baseline": "Test 1 main: ω=1.50",
                                     "results": results}, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
