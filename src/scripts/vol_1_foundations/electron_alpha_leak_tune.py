#!/usr/bin/env python3
r"""CAST→TUNE: Theorem 3.1′ α leak per Compton cycle on trap shell.

Prereg: research/2026-06-08_electron-alpha-leak-tune-prereg.md

Compares baseline trap vs shell radiation leak (α/cycle, R=Z₀/4π corpus load).
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

import numpy as np

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from electron_alpha_leak_audit import (  # noqa: E402
    ALPHA_T,
    GAMMA_TARGET,
    N_LATTICE,
    N_STEPS_POST,
    N_STEPS_PRE,
    PML,
    SHELL_RADIUS,
    TRAP_AMP,
    TRIGGER_X,
    _core_idx,
    _per_cycle_slopes,
    _saturation_at_core,
)
from native_electron_propagation import (  # noqa: E402
    apply_co_moving_longitudinal_drive,
    energy_centroid,
    interior_mask,
)
from native_k4_gamma_ceiling import (  # noqa: E402
    GAMMA_FULL_TIR,
    bond_gamma_min,
    seed_sech_v_inc,
    verify_canonical_sources,
)
from radiation_leak_shell import apply_radiation_leak_shell, shell_mask  # noqa: E402

from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402

OUT_DIR = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = OUT_DIR / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CADENCE = 2
SEED_RADIUS = 2.5
V_DRIVE_PRE = 0.04
AMP_START = 0.48
CX0_FRAC = 0.28
REL_TOL = 0.10


def _run_variant(*, enable_leak: bool) -> dict[str, Any]:
    n = N_LATTICE
    cx0 = int(CX0_FRAC * n)
    cy0 = cz0 = n // 2
    engine = VacuumEngine3D.from_args(
        N=n,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
    seed_sech_v_inc(engine, (cx0, cy0, cz0), AMP_START, SEED_RADIUS)
    engine.cos.initialize_electron_unknot_sector(
        R_target=0.5, r_target=0.25, amplitude_scale=min(AMP_START, 1.0)
    )
    mask = interior_mask(n, PML) & engine.k4.mask_active

    snap_step: int | None = None
    last_cx = float(cx0)
    post_records: list[dict[str, Any]] = []
    leak_log: list[dict[str, float]] = []
    total_steps = N_STEPS_PRE + N_STEPS_POST

    for step in range(total_steps + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            cx, _, _ = energy_centroid(v_sq, mask)
            if np.isfinite(cx):
                last_cx = cx

            if snap_step is not None:
                z = np.asarray(engine.k4.z_local_field)
                core = _core_idx(last_cx, cy0, cz0, n)
                gamma = bond_gamma_min(z, engine.k4.mask_active, core, SHELL_RADIUS)
                sat = _saturation_at_core(engine, core)
                h_total = float(engine._coupled.total_hamiltonian())
                sh = shell_mask(v_sq.shape, core, SHELL_RADIUS, engine.k4.mask_active)
                e_shell = float(np.sum(v_sq[sh]))
                post_records.append(
                    {
                        "step": step,
                        "gamma_min": gamma,
                        "eps_gamma": float(1.0 - gamma**2) if gamma is not None else None,
                        "eps_S_combined": float(1.0 - sat["S_combined"] ** 2),
                        "E_shell": e_shell,
                        "H_total": h_total,
                    }
                )

        if step < total_steps and snap_step is None and last_cx >= TRIGGER_X:
            core = _core_idx(last_cx, cy0, cz0, n)
            seed_sech_v_inc(engine, core, TRAP_AMP, SEED_RADIUS)
            engine.cos.initialize_electron_unknot_sector(
                R_target=0.5, r_target=0.25, amplitude_scale=min(TRAP_AMP, 1.0)
            )
            snap_step = step
            last_cx = float(core[0])

        if step < total_steps:
            if snap_step is None:
                apply_co_moving_longitudinal_drive(engine, last_cx, V_DRIVE_PRE)
            engine.step()
            if snap_step is not None and enable_leak:
                core = _core_idx(last_cx, cy0, cz0, n)
                leak_log.append(apply_radiation_leak_shell(engine, core, SHELL_RADIUS))

    dt = float(engine._coupled.outer_dt)
    omega_y = float(engine.cos.omega_yield)
    steps_per_cycle = (2.0 * math.pi / omega_y) / dt if omega_y > 0 else None

    static = {
        "P1_eps_gamma": _mean(post_records, "eps_gamma"),
        "P2_eps_S_combined": _mean(post_records, "eps_S_combined"),
    }
    shell_slope = _per_cycle_slopes(
        [r["step"] for r in post_records],
        [r["E_shell"] for r in post_records],
        steps_per_cycle or 1.0,
    )
    h_slope = _per_cycle_slopes(
        [r["step"] for r in post_records],
        [r["H_total"] for r in post_records],
        steps_per_cycle or 1.0,
    )
    static["P5_shell_leak_per_cycle"] = shell_slope["mean_abs_fractional_per_cycle"]
    static["P6_H_leak_per_cycle"] = h_slope["mean_abs_fractional_per_cycle"]

    gammas = [r["gamma_min"] for r in post_records if r["gamma_min"] is not None]
    gamma_min = float(min(gammas)) if gammas else None
    gamma_final = gammas[-1] if gammas else None
    tir_held = bool(
        gamma_min is not None
        and gamma_min <= GAMMA_FULL_TIR
        and (gamma_final is None or gamma_final <= -0.95)
    )

    eps = static["P1_eps_gamma"]
    abs_eps_alpha = abs(eps - ALPHA_T) if eps is not None else None
    shell_leak = static.get("P5_shell_leak_per_cycle")
    leak_matches_alpha = bool(
        shell_leak is not None and abs(shell_leak - ALPHA_T) / ALPHA_T < REL_TOL
    )

    if not tir_held:
        verdict, outcome = "TIR_LOST_WITH_LEAK" if enable_leak else "TIR_LOST_BASELINE", "C"
    elif enable_leak and abs_eps_alpha is not None and abs_eps_alpha < 0.003:
        verdict, outcome = "TUNE_EPS_MATCHES_ALPHA", "A"
    elif enable_leak and leak_matches_alpha and abs_eps_alpha is not None and abs_eps_alpha > 0.003:
        verdict, outcome = "TUNE_LEAK_OK_EPS_GAP_REMAINS", "B"
    else:
        verdict, outcome = "BASELINE_OR_INCONCLUSIVE", "D" if not enable_leak else "B"

    return {
        "variant": "with_alpha_leak" if enable_leak else "baseline_no_leak",
        "enable_leak": enable_leak,
        "snap_step": snap_step,
        "n_post_samples": len(post_records),
        "gamma_min_post": gamma_min,
        "gamma_final_post": gamma_final,
        "gamma_target_for_alpha": GAMMA_TARGET,
        "tir_held": tir_held,
        "static_proxies": static,
        "abs_eps_gamma_minus_alpha": abs_eps_alpha,
        "shell_leak_matches_alpha": leak_matches_alpha,
        "mean_leak_per_step": (
            float(np.mean([x["leak_per_step"] for x in leak_log])) if leak_log else None
        ),
        "verdict": verdict,
        "outcome": outcome,
        "alpha_used_as_leak_rate_only": enable_leak,
    }


def _mean(records: list[dict], key: str) -> float | None:
    vals = [r[key] for r in records if r.get(key) is not None]
    return float(np.mean(vals)) if vals else None


def classify(baseline: dict, tune: dict) -> dict[str, Any]:
    eps_base = baseline.get("abs_eps_gamma_minus_alpha")
    eps_tune = tune.get("abs_eps_gamma_minus_alpha")
    improved = bool(
        eps_base is not None
        and eps_tune is not None
        and eps_tune < eps_base - 1e-4
    )
    if tune["outcome"] == "A":
        agg = "TUNE_SUCCESS_ALPHA_READOUT"
    elif tune["outcome"] == "B" and not improved:
        agg = "TUNE_LEAK_DECOUPLED_FROM_EPS"
    elif tune["outcome"] == "C":
        agg = "TUNE_DESTABILIZED_TRAP"
    elif improved:
        agg = "TUNE_PARTIAL_EPS_IMPROVEMENT"
    else:
        agg = "TUNE_INCONCLUSIVE"
    return {
        "aggregate_verdict": agg,
        "eps_improved": improved,
        "delta_abs_eps": (
            (eps_tune - eps_base) if eps_base is not None and eps_tune is not None else None
        ),
    }


def main() -> None:
    verify_canonical_sources()
    print("Electron alpha leak TUNE (Theorem 3.1' shell drain)")
    baseline = _run_variant(enable_leak=False)
    print(f"  baseline: {baseline['verdict']}  |ε−α|={baseline['abs_eps_gamma_minus_alpha']}")
    tune = _run_variant(enable_leak=True)
    print(f"  with leak: {tune['verdict']}  |ε−α|={tune['abs_eps_gamma_minus_alpha']}")
    print(f"  shell leak/cycle: {tune['static_proxies'].get('P5_shell_leak_per_cycle')}")
    classification = classify(baseline, tune)
    print(f"  aggregate: {classification['aggregate_verdict']}")

    payload = {
        "prereg": "research/2026-06-08_electron-alpha-leak-tune-prereg.md",
        "baseline": baseline,
        "tune": tune,
        "classification": classification,
        "comparison_only_alpha": ALPHA_T,
    }
    out_json = OUT_DIR / "electron_alpha_leak_tune_results.json"
    out_json.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")
    print(f"  wrote: {out_json}")


if __name__ == "__main__":
    main()
