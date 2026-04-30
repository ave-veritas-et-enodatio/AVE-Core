"""
Foundation Audit T1 — N=24 saturated + Cosserat ON/OFF gap fill.

Per auditor 2026-04-30 Flag 1 + missing-comparison note: the chair-ring
data is at N≥24 + saturation, but Test 1 extensions table only has N=24
linear and N=16 saturated. Without N=24 saturated, the "chair-ring IC
preferentially selects 1.5·ω_C from broad saturation spectrum" synthesis
is interpolating across two axes (lattice + amplitude) that varied one
at a time.

This run fills the gap:
  - N=24 V=0.95 CosSelf=False  (saturated, no Cosserat coupling — bare K4 substrate)
  - N=24 V=0.95 CosSelf=True   (saturated, Cosserat self-terms enabled — K4↔Cosserat coupling)

Discriminates:
  (a) If N=24 saturated bare shows 1.5·ω_C dominant: chair-ring just amplifies
      what the substrate already prefers at this lattice + amplitude
  (b) If N=24 saturated bare shows multi-mode broadening (like N=16 sat):
      chair-ring's 99.99% ℓ=2 Fourier IS doing real selection work against
      saturation broadening
  (c) If Cosserat ON shifts the mode spectrum: K4↔Cosserat coupling at
      saturation contributes to mode selection
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
    "1.5·ω_C": 1.5,
    "π/√3 (1.81)": np.pi / np.sqrt(3.0),
    "2.96·ω_C": 2.96,
    "Nyquist": np.pi * np.sqrt(2.0),
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

    half_window = 0.05
    candidate_mags = {}
    print(f"    {'Candidate':<22} {'ω_target':>9} {'mag':>11}")
    for name, omega_target in CANDIDATE_OMEGAS.items():
        mask = (omegas_per_freq >= omega_target - half_window) & \
               (omegas_per_freq <= omega_target + half_window)
        mag = float(spec[mask].max()) if mask.sum() > 0 else 0.0
        candidate_mags[name] = {"omega_target": float(omega_target), "mag": mag}
        print(f"    {name:<22} {omega_target:>9.4f} {mag:>11.4e}")

    return {
        "label": label, "N": N, "PML": PML, "v_pulse": v_pulse,
        "enable_cosserat_self_terms": enable_cos_self,
        "n_periods": n_periods, "elapsed_s": elapsed,
        "candidate_mags": candidate_mags,
        "v_traj_rms": float(np.sqrt(np.mean(v_traj**2))),
    }


def main():
    print("=" * 78, flush=True)
    print("  Foundation Audit T1 — N=24 saturated + Cosserat ON/OFF gap fill")
    print("=" * 78, flush=True)

    results = []

    print("\n=== N=24 saturated, Cosserat OFF (bare K4-TLM at chair-ring lattice/amplitude) ===")
    results.append(run_pulse_targeted(N=24, v_pulse=0.95, enable_cos_self=False,
                                       label="N=24 V=0.95 CosSelf=False"))

    print("\n=== N=24 saturated, Cosserat ON ===")
    results.append(run_pulse_targeted(N=24, v_pulse=0.95, enable_cos_self=True,
                                       label="N=24 V=0.95 CosSelf=True"))

    # Combined comparison table — pull in prior data
    prior_results_path = Path(__file__).parent / "r10_v8_foundation_audit_t1_targeted_results.json"
    if prior_results_path.exists():
        with open(prior_results_path) as f:
            prior_data = json.load(f)
        prior_results = prior_data["results"]
    else:
        prior_results = []

    all_results = prior_results + results

    print("\n" + "=" * 78, flush=True)
    print("  Cross-setting comparison (combined with prior runs)")
    print("=" * 78, flush=True)
    print(f"  {'Setting':<32}", end="")
    for name in CANDIDATE_OMEGAS:
        print(f" {name[:14]:<14}", end="")
    print()
    for r in all_results:
        print(f"  {r['label']:<32}", end="")
        for name in CANDIDATE_OMEGAS:
            mag = r["candidate_mags"][name]["mag"]
            print(f" {mag:<14.3e}", end="")
        print()

    # Identify dominant non-Nyquist for the new N=24 sat results
    print("\n  Dominant non-Nyquist candidate for new N=24 saturated runs:")
    for r in results:
        non_nyq = {n: r["candidate_mags"][n]["mag"] for n in CANDIDATE_OMEGAS
                    if "Nyquist" not in n}
        dominant = max(non_nyq, key=non_nyq.get)
        sorted_vals = sorted(non_nyq.values(), reverse=True)
        ratio = sorted_vals[0] / sorted_vals[1] if sorted_vals[1] > 0 else float("inf")
        print(f"    {r['label']}: dominant = {dominant} (mag {non_nyq[dominant]:.3e}, "
              f"ratio to 2nd = {ratio:.2f})")

    # Discriminator: compare N=24 sat vs N=16 sat (saturation broadening) and vs N=24 lin (lattice mode)
    print("\n  Discriminator analysis:")
    n24_sat_off = next((r for r in results if r["label"] == "N=24 V=0.95 CosSelf=False"), None)
    n16_sat = next((r for r in prior_results
                     if r["label"] == "N=16, V=0.95, CosSelf=False"), None)
    n24_lin = next((r for r in prior_results
                     if r["label"] == "N=24, V=0.01, CosSelf=False"), None)
    if n24_sat_off and n16_sat and n24_lin:
        # Ratio of 1.5·ω_C peak to ω_TL peak — high ratio = 1.5 dominant; low ratio = ω_TL dominant
        def ratio_15_to_TL(r):
            return (r["candidate_mags"]["1.5·ω_C"]["mag"] /
                    max(r["candidate_mags"]["ω_TL = ω_C/√3"]["mag"], 1e-30))
        r_n24_sat = ratio_15_to_TL(n24_sat_off)
        r_n16_sat = ratio_15_to_TL(n16_sat)
        r_n24_lin = ratio_15_to_TL(n24_lin)
        print(f"    Ratio 1.5·ω_C / ω_TL (= 1.5 mode strength relative to 0.577 mode):")
        print(f"      N=24 V=0.95 (saturated): {r_n24_sat:.2f}")
        print(f"      N=16 V=0.95 (saturated): {r_n16_sat:.2f}")
        print(f"      N=24 V=0.01 (linear):    {r_n24_lin:.2f}")
        print()
        if r_n24_sat > 2.0:
            print(f"      → N=24 saturated bare-substrate ALREADY prefers 1.5·ω_C over ω_TL")
            print(f"        Reading: chair-ring's 1.48 dominance is N=24+saturation lattice mode,")
            print(f"        IC + symmetry don't need to do selection work")
        elif r_n24_sat < 0.5:
            print(f"      → N=24 saturated bare-substrate prefers ω_TL > 1.5·ω_C")
            print(f"        Reading: chair-ring IC + symmetry IS doing selection work to")
            print(f"        elevate 1.5 above bare substrate's preference")
        else:
            print(f"      → N=24 saturated bare-substrate has 1.5 and ω_TL within factor ~2")
            print(f"        Reading: ambiguous — modest IC + symmetry effect, modest substrate preference")

    # Cosserat ON vs OFF at N=24 saturated
    n24_sat_on = next((r for r in results if r["label"] == "N=24 V=0.95 CosSelf=True"), None)
    if n24_sat_on and n24_sat_off:
        print("\n  Cosserat ON/OFF comparison at N=24 saturated:")
        print(f"    {'ω':<22} {'OFF mag':>11} {'ON mag':>11} {'ratio':>8}")
        for name in CANDIDATE_OMEGAS:
            if "Nyquist" in name:
                continue
            off = n24_sat_off["candidate_mags"][name]["mag"]
            on = n24_sat_on["candidate_mags"][name]["mag"]
            ratio = on / max(off, 1e-30)
            flag = " ★" if abs(ratio - 1.0) > 0.2 else ""
            print(f"    {name:<22} {off:>11.4e} {on:>11.4e} {ratio:>8.3f}{flag}")

    out_path = Path(__file__).parent / "r10_v8_foundation_audit_t1_n24_saturated_results.json"
    out_path.write_text(json.dumps({"new_results": results,
                                     "prior_results": prior_results}, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
