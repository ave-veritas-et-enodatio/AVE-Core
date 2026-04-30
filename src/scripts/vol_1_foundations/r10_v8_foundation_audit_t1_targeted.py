"""
Foundation Audit T1 Extensions — targeted-frequency analysis.

Direct evaluation of FFT magnitude AT specific candidate substrate
frequencies, rather than rank-ordering top-N peaks (which gets confused
by broadband Nyquist + low-f clusters).

Candidate frequencies to evaluate (from Test 1 main + corpus):
  - ω = 0.577 ω_C   (ω_TL = c/bond_length, TLM bond traversal)
  - ω = 1.000 ω_C   (corpus ω_C / bootstrap chain bond-pair LC tank)
  - ω = 1.500 ω_C   (Test 1 main dominant non-Nyquist)
  - ω = 1.81  ω_C   (π/√3 — half-wave bond resonance)
  - ω = 2.96  ω_C   (2× 1.48, observed in T1.1 N=24)
  - ω = 4.44  ω_C   (Nyquist edge baseline)

For each engine setting, find FFT magnitude in a small window (±0.05·ω_C)
around each candidate. Compare magnitudes across settings.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D


CANDIDATE_OMEGAS = {
    "ω_TL = ω_C/√3": 1.0 / np.sqrt(3.0),
    "ω_C (corpus)": 1.0,
    "1.5·ω_C (Test 1 finding)": 1.5,
    "π/√3 (half-wave)": np.pi / np.sqrt(3.0),
    "2·1.48 = 2.96·ω_C": 2.96,
    "Nyquist π·√2": np.pi * np.sqrt(2.0),
}


def run_pulse_targeted(N, v_pulse, enable_cos_self, label, n_periods=100):
    PML = max(2, N // 4)
    DT = 1.0 / np.sqrt(2.0)
    COMPTON_PERIOD = 2.0 * np.pi
    N_STEPS = int(n_periods * COMPTON_PERIOD / DT)

    print(f"\n  [{label}] N={N}, PML={PML}, V_pulse={v_pulse}, cos_self={enable_cos_self}",
          flush=True)

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
    print(f"    elapsed {elapsed:.1f}s, RMS={np.sqrt(np.mean(v_traj**2)):.3e}")

    skip_steps = int(5.0 * COMPTON_PERIOD / DT)
    v_w = v_traj[skip_steps:] - v_traj[skip_steps:].mean()
    freqs = np.fft.rfftfreq(len(v_w), d=DT)
    spec = np.abs(np.fft.rfft(v_w))
    omegas_per_freq = 2 * np.pi * freqs

    # Mag at each candidate frequency: average over ±0.05 ω_C window
    half_window = 0.05
    candidate_mags = {}
    print(f"    {'Candidate':<26} {'ω_target':>9} {'mag':>11}")
    for name, omega_target in CANDIDATE_OMEGAS.items():
        mask = (omegas_per_freq >= omega_target - half_window) & \
               (omegas_per_freq <= omega_target + half_window)
        if mask.sum() == 0:
            mag = 0.0
        else:
            mag = float(spec[mask].max())  # max in window
        candidate_mags[name] = {"omega_target": omega_target, "mag": mag}
        print(f"    {name:<26} {omega_target:>9.4f} {mag:>11.4e}")

    return {
        "label": label, "N": N, "PML": PML, "v_pulse": v_pulse,
        "enable_cosserat_self_terms": enable_cos_self,
        "n_periods": n_periods, "elapsed_s": elapsed,
        "candidate_mags": candidate_mags,
        "v_traj_rms": float(np.sqrt(np.mean(v_traj**2))),
    }


def main():
    print("=" * 78, flush=True)
    print("  Foundation Audit T1 — targeted-frequency analysis")
    print("  Magnitude AT candidate substrate-resonance frequencies (±0.05 window)")
    print("=" * 78, flush=True)

    results = []

    print("\n=== T1.1: Lattice-size scan ===")
    for N in [8, 16, 24]:
        results.append(run_pulse_targeted(N=N, v_pulse=0.01, enable_cos_self=False,
                                           label=f"N={N}, V=0.01, CosSelf=False"))

    print("\n=== T1.3: Saturated amplitude ===")
    results.append(run_pulse_targeted(N=16, v_pulse=0.95, enable_cos_self=False,
                                       label="N=16, V=0.95, CosSelf=False"))

    print("\n=== T1.4: Cosserat self-terms enabled ===")
    results.append(run_pulse_targeted(N=16, v_pulse=0.01, enable_cos_self=True,
                                       label="N=16, V=0.01, CosSelf=True"))

    # Summary table: magnitude at each candidate ω across all settings
    print("\n" + "=" * 78, flush=True)
    print("  Cross-setting comparison: magnitude at each candidate ω")
    print("=" * 78, flush=True)
    print(f"  {'Setting':<32}", end="")
    for name in CANDIDATE_OMEGAS:
        print(f" {name[:14]:<14}", end="")
    print()

    for r in results:
        print(f"  {r['label']:<32}", end="")
        for name in CANDIDATE_OMEGAS:
            mag = r["candidate_mags"][name]["mag"]
            print(f" {mag:<14.3e}", end="")
        print()

    # Identify dominant non-Nyquist candidate per setting
    print("\n  Dominant non-Nyquist candidate per setting:")
    for r in results:
        non_nyq_mags = {n: r["candidate_mags"][n]["mag"] for n in CANDIDATE_OMEGAS
                        if "Nyquist" not in n}
        dominant = max(non_nyq_mags, key=non_nyq_mags.get)
        print(f"    {r['label']:<32} → {dominant} (mag {non_nyq_mags[dominant]:.3e})")

    # Stability of 1.5·ω_C across settings
    print("\n  1.5·ω_C peak stability across settings:")
    omega_15_mags = {}
    for r in results:
        omega_15_mags[r["label"]] = r["candidate_mags"]["1.5·ω_C (Test 1 finding)"]["mag"]
    print(f"    Magnitudes at ω=1.5: {omega_15_mags}")
    sorted_mags = sorted(omega_15_mags.values())
    if sorted_mags[0] > 0:
        ratio_max_min = sorted_mags[-1] / sorted_mags[0]
        print(f"    Max/Min ratio: {ratio_max_min:.2f}")
        print(f"    Mean: {np.mean(sorted_mags):.3e}, Std/Mean: "
              f"{np.std(sorted_mags)/np.mean(sorted_mags):.2f}")

    # Save
    out_path = Path(__file__).parent / "r10_v8_foundation_audit_t1_targeted_results.json"
    out_path.write_text(json.dumps({"candidate_omegas": {k: float(v) for k, v in CANDIDATE_OMEGAS.items()},
                                     "results": results}, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
