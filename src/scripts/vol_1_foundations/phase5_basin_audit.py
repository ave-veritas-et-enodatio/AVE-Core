"""Stage 0 basin-mapping audit — empirical characterization of W functional stationary states.

Per [doc 71_](../../research/L3_electron_soliton/71_basin_audit_methodology.md):
Round 7 Stage 0 precondition. Round 6 closure + Phase 5 case (b') + F17-K v3 (i)
all converge on "corpus-canonical seeds dissolve under engine self-dynamics."
This audit characterizes WHERE the engine's W functional actually has stationary
states under TDI gradient flow, before R7.1 (sparse eigensolver linearization)
or R7.2 ((2,3)/Hopf injection at GT geometry) commit to corpus GT as the
linearization point.

Pre-registered prediction P_basin_audit_GT_stationarity (manuscript/predictions.yaml):
GT-family triplet {GT_corpus, GT_perturb_+5%, GT_perturb_-5%} converges under TDI
to a common (R★, r★) at corpus GT (R=φ², r=1/φ²) with c★=3 preserved and
substantial energy relaxation. Falsification mode resolution per doc 71_ §6.

Driver protocol (single fresh-session run):
1. Build VacuumEngine3D at N=24, A28+self-terms enabled, NO drive sources.
2. Set engine.cos.damping_gamma = 0.1 (TDI mode).
3. For each seed in {GT_corpus, GT_perturb_+5%, GT_perturb_-5%, F17K_cos, F17K_s11, vacuum}:
     a. Initialize ω/u via initialize_electron_2_3_sector or bespoke seeder.
     b. **A26 contamination guard**: assert peak |ω| ∈ [0.85, 1.15]·0.3π for GT-family seeds.
     c. Run TDI to convergence (ΔE/E < 1e-6 over 50 steps AND |velocity| < 1e-3) or 1000-step cap.
     d. Record (R, r, c, E, |ω|_peak, S_peak) trajectory; final state + convergence flag + saturation label.
4. Evaluate falsification predicates (a)+(b)+(c) for the GT-family triplet.
5. Emit ASCII summary + write phase5_basin_audit_results.json next to driver.

NO drive sources. NO saturation pin. NO multi-bond seeds. NO engine code changes.
Single-bond, central-cell, single-resolution N=24. Saturation-pin variant + larger-N
sensitivity are deferred follow-ups per doc 71_ §8.

References:
- research/L3_electron_soliton/71_basin_audit_methodology.md (this audit's methodology)
- research/L3_electron_soliton/66_single_electron_first_pivot.md §16 (TDI baseline)
- research/L3_electron_soliton/67_lc_coupling_reciprocity_audit.md §17-§26 (F17-K arc)
- src/ave/topological/cosserat_field_3d.py:1228-1284 (TDI step implementation)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D


# ─── Pre-registered constants (frozen at commit time, per doc 71_ §3, §4, §6) ───

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI                 # ≈ 2.618 — corpus GT major radius
INV_PHI_SQ = 1.0 / PHI_SQ          # ≈ 0.382 — corpus GT minor radius
GT_PEAK_OMEGA = 0.3 * np.pi        # ≈ 0.9425 — bound-state amplitude per doc 34_ §9.4
A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)   # ≈ 0.3464 (recovers 0.3π peak from √3/2·π canonical)

DAMPING_GAMMA = 0.1                # TDI gradient-flow rate per doc 66_ §16
N_LATTICE = 24                     # matches Phase 5 registered config
PML = 4
MAX_STEPS = 1000                   # convergence cap
CONVERGENCE_WINDOW = 50            # steps over which ΔE/E and velocity are checked
DELTA_E_REL_THRESH = 1e-6
VELOCITY_THRESH = 1e-3
RECORD_CADENCE = 10                # record trajectory every N steps

A26_GUARD_LOW = 0.85 * GT_PEAK_OMEGA
A26_GUARD_HIGH = 1.15 * GT_PEAK_OMEGA
SATURATION_FREE_THRESH = 0.95      # S★ > 0.95 → "free" basin; below → "manifold-bound"

# Falsification tolerances (per doc 71_ §6)
COMMON_R_TOL = 0.10 * PHI_SQ       # ≈ 0.262
COMMON_r_TOL = 0.05 / PHI_SQ       # ≈ 0.019
GT_R_TOL = 0.10
GT_r_TOL = 0.05
ENERGY_RELAXATION_FACTOR = 0.5

OUTPUT_JSON = Path(__file__).parent / "phase5_basin_audit_results.json"


# ─── Seed builders ────────────────────────────────────────────────────────────


def _build_engine() -> VacuumEngine3D:
    """Construct the audit engine: A28 + self-terms, no sources, TDI mode."""
    engine = VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,    # A28 — Op14 z_local is the coupling channel
        enable_cosserat_self_terms=True,   # Cosserat self-terms restored under A28
    )
    engine.cos.damping_gamma = DAMPING_GAMMA
    return engine


def _seed_gt_family(engine: VacuumEngine3D, R: float, r: float) -> None:
    """GT-family seeder: corpus (2,3) hedgehog at given (R, r) with A26-corrected amplitude."""
    engine.cos.initialize_electron_2_3_sector(
        R_target=R, r_target=r, use_hedgehog=True,
        amplitude_scale=A26_AMP_SCALE,
    )


def _seed_F17K_endpoint(engine: VacuumEngine3D, R: float, r: float) -> None:
    """F17-K endpoint seeder: same hedgehog form but at v2-v2's reported (R, r) endpoints.
    Amplitude held at the same A26-corrected value for cross-comparability with GT family.
    """
    engine.cos.initialize_electron_2_3_sector(
        R_target=R, r_target=r, use_hedgehog=True,
        amplitude_scale=A26_AMP_SCALE,
    )


def _seed_random_low_amplitude(engine: VacuumEngine3D, peak: float = 0.05) -> None:
    """Vacuum sanity seeder: small uniform random ω across the alive mask, |u|=0."""
    rng = np.random.default_rng(seed=42)
    omega = rng.uniform(-peak, peak, size=engine.cos.omega.shape)
    omega *= engine.cos.mask_alive[..., None]
    engine.cos.omega = omega
    engine.cos.omega_dot[...] = 0.0
    engine.cos.u[...] = 0.0
    engine.cos.u_dot[...] = 0.0


# ─── Diagnostics ──────────────────────────────────────────────────────────────


def _local_saturation_at_peak(engine: VacuumEngine3D) -> float:
    """Local saturation S = √(1 - A²) at the lattice site of peak |ω|.
    A² = (|ω|/V_SNAP_natural)² in engine-natural units (V_SNAP=1 here).
    Returns S in [0, 1]; S>0.95 indicates "free" stationary point off the saturation manifold,
    S<0.95 indicates "manifold-bound" (system has settled at a saturation-clipped attractor).
    """
    omega_mag = np.linalg.norm(np.asarray(engine.cos.omega), axis=-1)
    A_sq_local = np.minimum(omega_mag * omega_mag, 1.0)
    peak_idx = np.unravel_index(np.argmax(omega_mag), omega_mag.shape)
    return float(np.sqrt(max(0.0, 1.0 - A_sq_local[peak_idx])))


def _measure_state(engine: VacuumEngine3D) -> dict:
    """Snapshot of (R, r, c, E, |ω|_peak, S_peak, |velocity|_max) at current step."""
    omega_arr = np.asarray(engine.cos.omega)
    u_dot_arr = np.asarray(engine.cos.u_dot)
    omega_dot_arr = np.asarray(engine.cos.omega_dot)
    R, r = engine.cos.extract_shell_radii()
    return {
        "step": int(getattr(engine, "step_count", 0)),
        "t": float(getattr(engine, "time", 0.0)),
        "R": float(R),
        "r": float(r),
        "c": int(engine.cos.extract_crossing_count()),
        "E_cos": float(engine.cos.total_energy()),
        "|ω|_peak": float(np.linalg.norm(omega_arr, axis=-1).max()),
        "S_peak": _local_saturation_at_peak(engine),
        "|velocity|_max": float(max(np.abs(u_dot_arr).max(), np.abs(omega_dot_arr).max())),
    }


def _converged(history: list[dict]) -> bool:
    """ΔE/|E| < 1e-6 across last 50 records AND |velocity|_max < 1e-3 at tail."""
    if len(history) < (CONVERGENCE_WINDOW // RECORD_CADENCE) + 1:
        return False
    tail = history[-(CONVERGENCE_WINDOW // RECORD_CADENCE):]
    E_tail = np.array([h["E_cos"] for h in tail])
    if E_tail[-1] == 0.0:
        return tail[-1]["|velocity|_max"] < VELOCITY_THRESH
    rel_drift = float(np.abs(E_tail.max() - E_tail.min()) / max(abs(E_tail[-1]), 1e-12))
    return (rel_drift < DELTA_E_REL_THRESH) and (tail[-1]["|velocity|_max"] < VELOCITY_THRESH)


# ─── Per-seed runner ──────────────────────────────────────────────────────────


def _run_seed(name: str, seeder, gt_family: bool) -> dict:
    """Build engine, apply seeder, A26 guard if GT-family, run TDI to convergence or cap."""
    print(f"\n  ── seed: {name} ──")
    engine = _build_engine()
    seeder(engine)

    state_seed = _measure_state(engine)
    print(f"    seed state: R={state_seed['R']:.3f} r={state_seed['r']:.3f} "
          f"c={state_seed['c']} E={state_seed['E_cos']:.4f} "
          f"|ω|_peak={state_seed['|ω|_peak']:.4f} S_peak={state_seed['S_peak']:.3f}")

    # A26 contamination guard (per doc 71_ §4)
    if gt_family:
        peak_omega = state_seed["|ω|_peak"]
        if not (A26_GUARD_LOW <= peak_omega <= A26_GUARD_HIGH):
            raise AssertionError(
                f"A26 GUARD FAILED for seed '{name}': peak |ω|={peak_omega:.4f} "
                f"outside [{A26_GUARD_LOW:.4f}, {A26_GUARD_HIGH:.4f}] "
                f"(target 0.3π={GT_PEAK_OMEGA:.4f}). "
                f"Verify amplitude_scale={A26_AMP_SCALE:.4f} is being applied."
            )
        print(f"    A26 guard OK (peak |ω|={peak_omega:.4f} ∈ [{A26_GUARD_LOW:.4f}, {A26_GUARD_HIGH:.4f}])")

    history = [state_seed]
    t0 = time.time()
    converged = False
    for step in range(1, MAX_STEPS + 1):
        engine.step()
        if step % RECORD_CADENCE == 0:
            history.append(_measure_state(engine))
            if _converged(history):
                converged = True
                break
    elapsed = time.time() - t0

    final = history[-1]
    label = "free" if final["S_peak"] > SATURATION_FREE_THRESH else "manifold-bound"
    e_ratio = final["E_cos"] / max(state_seed["E_cos"], 1e-12)
    print(f"    final state ({elapsed:.1f}s, {final['step']} steps, "
          f"{'CONVERGED' if converged else 'CAP REACHED'}):")
    print(f"      R★={final['R']:.3f} r★={final['r']:.3f} c★={final['c']} "
          f"E★/E₀={e_ratio:.3f} S★={final['S_peak']:.3f} → {label}")

    return {
        "seed_name": name,
        "gt_family": gt_family,
        "seed_state": state_seed,
        "final_state": final,
        "trajectory": history,
        "converged": converged,
        "elapsed_seconds": elapsed,
        "saturation_label": label,
        "energy_ratio": e_ratio,
    }


# ─── Falsification adjudication ──────────────────────────────────────────────


def _evaluate_falsification(results: dict) -> dict:
    """Compute (a) common-attractor / (b) at-corpus-GT / (c) topology+relaxation predicates.
    Per doc 71_ §6 — frozen at commit time.
    """
    gt_runs = [results[k] for k in ("GT_corpus", "GT_perturb_+5%", "GT_perturb_-5%")]
    R_finals = np.array([run["final_state"]["R"] for run in gt_runs])
    r_finals = np.array([run["final_state"]["r"] for run in gt_runs])
    c_finals = np.array([run["final_state"]["c"] for run in gt_runs])
    E_ratios = np.array([run["energy_ratio"] for run in gt_runs])

    # (a) common attractor across the three GT-family runs
    R_spread = float(R_finals.max() - R_finals.min())
    r_spread = float(r_finals.max() - r_finals.min())
    common = (R_spread < COMMON_R_TOL) and (r_spread < COMMON_r_TOL)

    # (b) common attractor at corpus GT
    R_mean = float(R_finals.mean())
    r_mean = float(r_finals.mean())
    at_gt = (abs(R_mean - PHI_SQ) < GT_R_TOL) and (abs(r_mean - INV_PHI_SQ) < GT_r_TOL)

    # (c) topology preserved + substantial energy relaxation
    topology_preserved = bool(np.all(c_finals == 3))
    energy_relaxed = bool(np.all(E_ratios < ENERGY_RELAXATION_FACTOR))
    topo_and_relax = topology_preserved and energy_relaxed

    predicates = {
        "(a) common attractor": {
            "pass": common,
            "R_spread": R_spread, "R_tol": COMMON_R_TOL,
            "r_spread": r_spread, "r_tol": COMMON_r_TOL,
        },
        "(b) at corpus GT": {
            "pass": at_gt,
            "R_mean": R_mean, "phi_sq": PHI_SQ, "R_tol": GT_R_TOL,
            "r_mean": r_mean, "inv_phi_sq": INV_PHI_SQ, "r_tol": GT_r_TOL,
        },
        "(c) topology + relaxation": {
            "pass": topo_and_relax,
            "topology_preserved": topology_preserved,
            "c_finals": c_finals.tolist(),
            "energy_relaxed": energy_relaxed,
            "E_ratios": E_ratios.tolist(),
        },
    }
    overall_pass = common and at_gt and topo_and_relax
    return {"overall_pass": overall_pass, "predicates": predicates}


# ─── Main ────────────────────────────────────────────────────────────────────


def main() -> dict:
    print("=" * 78)
    print("  Stage 0 basin-mapping audit — P_basin_audit_GT_stationarity")
    print("  Pre-registered per doc 71_ §6; frozen at commit time")
    print("=" * 78)
    print(f"  Lattice: N={N_LATTICE}, pml={PML}, T=0, A28+self-terms ON, NO drive sources")
    print(f"  Integrator: TDI, damping_gamma={DAMPING_GAMMA}, max steps={MAX_STEPS}")
    print(f"  Convergence: ΔE/|E|<{DELTA_E_REL_THRESH} over {CONVERGENCE_WINDOW} steps "
          f"AND |velocity|<{VELOCITY_THRESH}")
    print(f"  A26 guard: peak |ω| ∈ [{A26_GUARD_LOW:.4f}, {A26_GUARD_HIGH:.4f}] "
          f"for GT-family seeds (target 0.3π={GT_PEAK_OMEGA:.4f})")

    # F17-K v2-v2 endpoints — inferred from R/r ratios at the same major scale as GT.
    # v2-v2 reported R/r=3.40 (Cosserat-energy descent) and R/r=1.03 (coupled-S₁₁ descent).
    # Use R = φ² as the major-axis anchor; back out r from each ratio.
    # (Result of audit will tell us if the ratios are themselves attractors regardless of R anchor.)
    F17K_COS_R, F17K_COS_r = PHI_SQ, PHI_SQ / 3.40
    F17K_S11_R, F17K_S11_r = PHI_SQ, PHI_SQ / 1.03

    seed_specs = [
        ("GT_corpus", lambda e: _seed_gt_family(e, PHI_SQ, INV_PHI_SQ), True),
        ("GT_perturb_+5%", lambda e: _seed_gt_family(e, 1.05 * PHI_SQ, 1.05 * INV_PHI_SQ), True),
        ("GT_perturb_-5%", lambda e: _seed_gt_family(e, 0.95 * PHI_SQ, 0.95 * INV_PHI_SQ), True),
        ("F17K_cos_endpoint", lambda e: _seed_F17K_endpoint(e, F17K_COS_R, F17K_COS_r), False),
        ("F17K_s11_endpoint", lambda e: _seed_F17K_endpoint(e, F17K_S11_R, F17K_S11_r), False),
        ("random_low_amp", lambda e: _seed_random_low_amplitude(e, peak=0.05), False),
    ]

    results: dict[str, dict] = {}
    for name, seeder, gt_family in seed_specs:
        results[name] = _run_seed(name, seeder, gt_family)

    # ── Falsification adjudication ────────────────────────────────────────
    print("\n" + "=" * 78)
    print("  Falsification predicates (per doc 71_ §6)")
    print("=" * 78)
    adjudication = _evaluate_falsification(results)
    for pred_name, pred in adjudication["predicates"].items():
        flag = "PASS" if pred["pass"] else "FAIL"
        print(f"  {pred_name}: {flag}")
        for k, v in pred.items():
            if k == "pass":
                continue
            print(f"    {k}: {v}")
    overall = "PASS" if adjudication["overall_pass"] else "FAIL"
    print(f"\n  P_basin_audit_GT_stationarity → {overall}")
    if not adjudication["overall_pass"]:
        print("    Falsification mode resolution per doc 71_ §6:")
        if not adjudication["predicates"]["(a) common attractor"]["pass"]:
            print("    → (a) failed: GT region is not a basin (ridge or fragmented landscape).")
        elif not adjudication["predicates"]["(b) at corpus GT"]["pass"]:
            print("    → (b) failed with (a) passing: engine basin ≠ corpus GT.")
            print(f"      Actual attractor at (R★, r★) ≈ "
                  f"({adjudication['predicates']['(b) at corpus GT']['R_mean']:.3f}, "
                  f"{adjudication['predicates']['(b) at corpus GT']['r_mean']:.3f}).")
        if not adjudication["predicates"]["(c) topology + relaxation"]["pass"]:
            print("    → (c) failed: topology not preserved or seed didn't relax.")

    payload = {
        "pre_registration": "P_basin_audit_GT_stationarity",
        "doc": "research/L3_electron_soliton/71_basin_audit_methodology.md",
        "constants": {
            "PHI_SQ": PHI_SQ, "INV_PHI_SQ": INV_PHI_SQ,
            "GT_PEAK_OMEGA": GT_PEAK_OMEGA, "A26_AMP_SCALE": A26_AMP_SCALE,
            "DAMPING_GAMMA": DAMPING_GAMMA, "N_LATTICE": N_LATTICE,
            "MAX_STEPS": MAX_STEPS,
            "COMMON_R_TOL": COMMON_R_TOL, "COMMON_r_TOL": COMMON_r_TOL,
            "GT_R_TOL": GT_R_TOL, "GT_r_TOL": GT_r_TOL,
            "ENERGY_RELAXATION_FACTOR": ENERGY_RELAXATION_FACTOR,
        },
        "results": results,
        "adjudication": adjudication,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"\n  Results written to {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
