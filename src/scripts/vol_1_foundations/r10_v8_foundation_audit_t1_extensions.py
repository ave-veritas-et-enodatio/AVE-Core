"""
Foundation Audit Test 1 Extensions.

Per doc 96 §6 follow-ups to Test 1's substrate-intrinsic 1.50·ω_C finding:
  T1.1 — Lattice-size scan (N = 8, 16, 24): does 1.50·ω_C stay constant
         (substrate-intrinsic) or scale with lattice size (artifact)?
  T1.3 — Saturated-amplitude test (V_pulse = 0.95): does 1.50·ω_C persist
         in saturation regime, or shift due to Ax 4 nonlinearity?
  T1.4 — Cosserat self-terms enabled: does activating Cosserat coupling
         shift the substrate-intrinsic resonance?

T1.2 (DT scaling) deferred — would require dx overriding which is more
intrusive; covered partially by T1.1's N-scan since DT is computed from dx.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D


def run_pulse_ringdown(N, v_pulse, enable_cos_self, label, n_periods=50):
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

    # FFT, skip 5P transient, find non-Nyquist peaks
    skip_steps = int(5.0 * COMPTON_PERIOD / DT)
    v_w = v_traj[skip_steps:] - v_traj[skip_steps:].mean()
    freqs = np.fft.rfftfreq(len(v_w), d=DT)
    spec = np.abs(np.fft.rfft(v_w))

    # Filter Nyquist edge (top 1% of frequencies = numerical baseline)
    nyquist_cutoff = 0.99 * freqs[-1]
    physical_mask = freqs < nyquist_cutoff
    spec_phys = spec * physical_mask
    top_idxs = np.argsort(spec_phys)[::-1][:5]
    peaks = [(int(i), float(freqs[i]), float(spec[i]), 2 * np.pi * float(freqs[i]))
             for i in top_idxs]

    print(f"    elapsed {elapsed:.1f}s")
    print(f"    Top 5 non-Nyquist peaks (idx, f, mag, ω/ω_C):")
    for p in peaks:
        print(f"      idx={p[0]:5d}  f={p[1]:.5f}  mag={p[2]:.3e}  ω={p[3]:.4f}")

    return {
        "label": label,
        "N": N,
        "PML": PML,
        "v_pulse": v_pulse,
        "enable_cosserat_self_terms": enable_cos_self,
        "n_periods": n_periods,
        "elapsed_s": elapsed,
        "top5_peaks_omega_C": [p[3] for p in peaks],
        "top5_magnitudes": [p[2] for p in peaks],
        "v_traj_max_abs": float(np.max(np.abs(v_traj))),
        "v_traj_rms": float(np.sqrt(np.mean(v_traj**2))),
        "dominant_omega_non_nyquist": peaks[0][3] if peaks else None,
    }


def main():
    print("=" * 78, flush=True)
    print("  Foundation Audit Test 1 Extensions")
    print("=" * 78, flush=True)
    print("  Baseline (Test 1): N=16, V_pulse=0.01, no Cosserat self-terms")
    print("  Baseline dominant non-Nyquist ω: 1.50·ω_C")
    print()

    results = []

    # T1.1 — Lattice-size scan
    print("\n=== T1.1: Lattice-size scan ===")
    for N in [8, 16, 24]:
        results.append(run_pulse_ringdown(N=N, v_pulse=0.01, enable_cos_self=False,
                                          label=f"T1.1 N={N}"))

    # T1.3 — Saturated amplitude
    print("\n=== T1.3: Saturated amplitude ===")
    results.append(run_pulse_ringdown(N=16, v_pulse=0.95, enable_cos_self=False,
                                      label="T1.3 V_pulse=0.95 (saturated)"))

    # T1.4 — Cosserat self-terms enabled
    print("\n=== T1.4: Cosserat self-terms enabled ===")
    results.append(run_pulse_ringdown(N=16, v_pulse=0.01, enable_cos_self=True,
                                      label="T1.4 Cosserat self-terms ON"))

    # Summary
    print("\n" + "=" * 78, flush=True)
    print("  Summary: dominant non-Nyquist ω across all variations")
    print("=" * 78, flush=True)
    print(f"  {'Label':<40} {'N':>3} {'V_pulse':>8} {'CosSelf':>7} {'ω_dom/ω_C':>10}")
    for r in results:
        cos_str = "True" if r["enable_cosserat_self_terms"] else "False"
        omega = r["dominant_omega_non_nyquist"] or 0.0
        print(f"  {r['label']:<40} {r['N']:>3} {r['v_pulse']:>8.3f} {cos_str:>7} {omega:>10.4f}")

    # Stability check on substrate-intrinsic interpretation
    print()
    print("  Substrate-intrinsic test:")
    print("  - If 1.50·ω_C stays constant across N: substrate-intrinsic confirmed")
    print("  - If shifts with N: lattice-mode artifact (eigenvalue depends on N)")
    print("  - If shifts with V_pulse=0.95: nonlinear-saturation correction")
    print("  - If shifts with Cosserat: K4-Cosserat coupling distorts intrinsic frequency")

    omegas = [r["dominant_omega_non_nyquist"] for r in results]
    omega_baseline = 1.50  # from Test 1 main run
    print()
    print(f"  Baseline (Test 1 main): ω = {omega_baseline:.4f}·ω_C")
    print(f"  Variations:")
    for r, omega in zip(results, omegas):
        if omega is None:
            continue
        delta_pct = (omega - omega_baseline) / omega_baseline * 100
        flag = " ★ stable" if abs(delta_pct) < 5 else " ⚠ shift"
        print(f"    {r['label']:<40} ω={omega:.4f}  Δ={delta_pct:+.2f}%{flag}")

    out_path = Path(__file__).parent / "r10_v8_foundation_audit_t1_extensions_results.json"
    out_path.write_text(json.dumps({"baseline": "Test 1 main: ω=1.50",
                                     "results": results}, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
