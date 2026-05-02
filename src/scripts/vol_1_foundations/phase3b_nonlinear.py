"""
Phase 3b X1 — node-level Axiom 4 saturation (nonlinear=True).

Same grid as `phase3b_axiom_compliant.py` (3 envelopes × 3 amplitudes
at N=72, pml=0, op3_bond_reflection=True, 3 Op6 iterations, 150 TLM
steps) but with `nonlinear=True`: the K4 node scattering matrix becomes
saturation-aware via `build_scattering_matrix(z_local)` rather than
using the linear S = (1/2)𝟙 − I.

Pre-registered expectations (from §9.5 of 32_phase3b_axiom_compliant_redesign.md):

  - R/r shifts toward 2.618 (Golden Torus)  → Phase 3b closes, mechanism confirmed
  - R/r shifts toward 2.0 (classical Clifford) → self-avoidance via node sat confirmed
                                                   but spin-½ projection still missing
  - R/r stays at ≈3.4 (§8 baseline)         → node sat isn't the bottleneck
  - Degrades (more divergence)               → node sat destabilizes; diagnose

Results appended to 32_phase3b_axiom_compliant_redesign.md §10 after run.
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.core.constants import V_SNAP, ALPHA

# Reuse the §8 machinery — only the nonlinear flag differs
from phase3b_axiom_compliant import (
    op6_iteration, ENVELOPES, plot_convergence_grid, plot_seed_independence,
)
from tlm_electron_soliton_eigenmode import extract_alpha_inverse

PHI = (1.0 + np.sqrt(5.0)) / 2.0
ALPHA_INV_TARGET = 1.0 / ALPHA


def main():
    print("=" * 72)
    print("PHASE 3b X1 — nonlinear=True (node-level Axiom 4 saturation)")
    print("Pre-registered in research/L3_electron_soliton/"
          "32_phase3b_axiom_compliant_redesign.md §9.5")
    print("=" * 72)

    envelopes = list(ENVELOPES.keys())
    amplitudes = [0.2, 0.3, 0.48]
    N = 72
    n_steps = 150
    max_iter = 3

    print(f"\nGrid: {len(envelopes)} envelopes × {len(amplitudes)} amplitudes"
          f" × up to {max_iter} Op6 iterations")
    print(f"Lattice: N={N}, pml=0 (periodic), op3_bond_reflection=True,"
          f" nonlinear=True")
    print(f"Inner: {n_steps} TLM steps per iteration")
    print(f"Baseline (nonlinear=False) attractor from §8: R/r ≈ 3.4-3.7")

    results = []
    for env in envelopes:
        for amp in amplitudes:
            print(f"\n--- envelope={env}, strain_target={amp}, "
                  f"nonlinear=True ---")
            res = op6_iteration(
                envelope_name=env,
                strain_target=amp,
                N=N,
                n_steps=n_steps,
                max_iter=max_iter,
                nonlinear=True,
            )
            results.append(res)

    # --- Results table ---
    print()
    print("=" * 72)
    print("X1 RESULTS (nonlinear=True) per (envelope, amplitude)")
    print("=" * 72)
    print(
        f"{'env':>12} {'A_tgt':>6} {'conv':>5} {'iter':>5} "
        f"{'R_final':>8} {'r_final':>8} {'R/r':>7} "
        f"{'α⁻¹_geom':>10}"
    )
    for res in results:
        alpha = extract_alpha_inverse(res["final_R"], res["final_r"], c=3)
        alpha_inv = alpha["alpha_inv"] if alpha["valid"] else float("nan")
        print(
            f"{res['envelope']:>12} {res['strain_target']:>6} "
            f"{'Y' if res['converged'] else 'N':>5} "
            f"{res['iterations']:>5} "
            f"{res['final_R']:>8.3f} {res['final_r']:>8.3f} "
            f"{res['final_R']/max(res['final_r'],1e-9):>7.3f} "
            f"{alpha_inv:>10.2f}"
        )

    # Seed-independence check per amplitude
    print()
    print("Seed-independence (X1, nonlinear=True):")
    for amp in amplitudes:
        at_amp = [r for r in results if r["strain_target"] == amp]
        if not at_amp:
            continue
        R_final = [r["final_R"] for r in at_amp]
        r_final = [r["final_r"] for r in at_amp]
        ratio = [R / max(rr, 1e-9) for R, rr in zip(R_final, r_final)]
        R_spread = (max(R_final) - min(R_final)) / max(np.mean(R_final), 1e-9)
        ratio_spread = (max(ratio) - min(ratio)) / max(np.mean(ratio), 1e-9)
        seed_indep = R_spread < 0.05 and ratio_spread < 0.05
        print(
            f"  A_target={amp}:  "
            f"R_final range [{min(R_final):.3f}, {max(R_final):.3f}]  "
            f"R/r range [{min(ratio):.3f}, {max(ratio):.3f}]  "
            f"ΔR/mean={R_spread:.2%}  Δ(R/r)/mean={ratio_spread:.2%}  "
            f"{'✓ seed-indep' if seed_indep else '✗ NOT seed-indep'}"
        )

    # Compare to §8 baseline at each amplitude (baseline from log)
    baseline_Rr = {
        0.20: {"hedgehog": 2.467, "gaussian": 3.700, "exponential": 3.700},
        0.30: {"hedgehog": 1.500, "gaussian": 3.364, "exponential": 3.364},
        0.48: {"hedgehog": 1.286, "gaussian": 3.389, "exponential": 1.152},
    }
    print()
    print("Δ(R/r) from §8 baseline (nonlinear=False → True):")
    for res in results:
        env = res["envelope"]
        amp = res["strain_target"]
        ratio_x1 = res["final_R"] / max(res["final_r"], 1e-9)
        ratio_baseline = baseline_Rr.get(amp, {}).get(env, float("nan"))
        delta = ratio_x1 - ratio_baseline
        print(f"  {env:>12} A={amp}:  baseline={ratio_baseline:.3f}  "
              f"X1={ratio_x1:.3f}  Δ={delta:+.3f}")

    # Verdict per pre-registered predictions
    print()
    print("Pre-registered prediction evaluation:")
    converged_ratios = [r["final_R"] / max(r["final_r"], 1e-9)
                        for r in results if r["converged"]]
    all_final_ratios = [r["final_R"] / max(r["final_r"], 1e-9) for r in results]
    any_golden = any(2.5 < rr < 2.7 for rr in all_final_ratios)
    any_classical = any(1.85 < rr < 2.15 for rr in all_final_ratios)
    still_33_ish = all(3.0 < rr < 4.0 or rr < 1.5 for rr in all_final_ratios)
    if any_golden:
        verdict = "Golden Torus regime reached — Phase 3b closes via X1"
    elif any_classical:
        verdict = "Classical full-Clifford reached — node sat self-avoidance works; spin-½ still missing"
    elif still_33_ish:
        verdict = "Same regime as §8 — node sat NOT the bottleneck; proceed to X2"
    else:
        verdict = "Ambiguous — inspect trajectories"
    print(f"  → {verdict}")

    # Save raw data + figures (separate files from §8 baseline)
    save_dict = {}
    for res in results:
        tag = f"{res['envelope']}_{res['strain_target']}"
        traj = np.array(res["trajectory"])
        save_dict[f"{tag}_trajectory"] = traj
        save_dict[f"{tag}_converged"] = np.array([res["converged"]])
        save_dict[f"{tag}_final_R"] = np.array([res["final_R"]])
        save_dict[f"{tag}_final_r"] = np.array([res["final_r"]])
    np.savez("/tmp/phase3b_nonlinear.npz", **save_dict)

    plot_convergence_grid(results, "/tmp/phase3b_nonlinear_traces.png")
    plot_seed_independence(results, "/tmp/phase3b_nonlinear_seed_indep.png")

    print()
    print("Raw data: /tmp/phase3b_nonlinear.npz")
    print("Figures:  /tmp/phase3b_nonlinear_traces.png")
    print("          /tmp/phase3b_nonlinear_seed_indep.png")


if __name__ == "__main__":
    main()
