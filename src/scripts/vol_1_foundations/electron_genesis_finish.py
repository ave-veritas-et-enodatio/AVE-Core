#!/usr/bin/env python3
r"""Electron genesis finish: post-snap persistence + ε→α target on native lane.

Prereg: research/2026-06-08_electron-genesis-finish-prereg.md

Chains: propagate sub-yield → position snap → zero-drive persistence window.
Sweeps trap_amp for closest approach to Theorem 3.1′ target Γ = −√(1−α).

Alpha comparison-only. No PairNucleationGate observer.
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

from native_electron_propagation import (  # noqa: E402
    apply_co_moving_longitudinal_drive,
    energy_centroid,
    interior_mask,
)
from native_k4_gamma_ceiling import (  # noqa: E402
    EPS_ALPHA_TARGET,
    GAMMA_FULL_TIR,
    bond_gamma_min,
    seed_sech_v_inc,
    verify_canonical_sources,
)

from ave.core.constants import ALPHA_COLD  # noqa: E402
from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402

OUT_DIR = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = OUT_DIR / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

N_LATTICE = 32
PML = 4
N_STEPS_PRE = 400
N_STEPS_POST = 600
CADENCE = 4
SEED_RADIUS = 2.5
SHELL_RADIUS = 6
V_DRIVE_PRE = 0.04
AMP_START = 0.48
TRIGGER_X = 14.0
CX0_FRAC = 0.28
TRAP_AMPS = [1.0, 1.25, 1.5, 1.75, 2.0, 2.5]

GAMMA_TARGET_ALPHA = -math.sqrt(1.0 - float(ALPHA_COLD))
EPS_TARGET_ALPHA = float(ALPHA_COLD)
Q_TARGET = 1.0 / EPS_TARGET_ALPHA


def _core_idx(cx: float, cy0: int, cz0: int, n: int) -> tuple[int, int, int]:
    return (
        min(max(int(round(cx)), PML), n - PML - 1),
        cy0,
        cz0,
    )


def run_finish(trap_amp: float) -> dict[str, Any]:
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
    phase = "pre"

    post_gamma: list[float] = []
    post_cx: list[float] = []
    post_steps: list[int] = []

    total_steps = N_STEPS_PRE + N_STEPS_POST

    for step in range(total_steps + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            cx, _, _ = energy_centroid(v_sq, mask)
            if np.isfinite(cx):
                last_cx = cx
            core = _core_idx(last_cx, cy0, cz0, n)
            g = bond_gamma_min(z, engine.k4.mask_active, core, SHELL_RADIUS)
            if snap_step is not None and g is not None:
                post_gamma.append(g)
                post_cx.append(last_cx)
                post_steps.append(step)

        if step < total_steps and snap_step is None and last_cx >= TRIGGER_X:
            core = _core_idx(last_cx, cy0, cz0, n)
            seed_sech_v_inc(engine, core, trap_amp, SEED_RADIUS)
            engine.cos.initialize_electron_unknot_sector(
                R_target=0.5, r_target=0.25, amplitude_scale=min(trap_amp, 1.0)
            )
            snap_step = step
            last_cx = float(core[0])
            phase = "post"

        if step < total_steps:
            if snap_step is None:
                apply_co_moving_longitudinal_drive(engine, last_cx, V_DRIVE_PRE)
            engine.step()

    gamma_min_post = float(min(post_gamma)) if post_gamma else None
    gamma_max_post = float(max(post_gamma)) if post_gamma else None
    gamma_final = post_gamma[-1] if post_gamma else None
    eps_min = float(1.0 - gamma_min_post**2) if gamma_min_post is not None else None
    eps_final = float(1.0 - gamma_final**2) if gamma_final is not None else None
    q_proxy = (1.0 / eps_min) if eps_min and eps_min > 1e-12 else None

    cx_delta_post = (post_cx[-1] - post_cx[0]) if len(post_cx) >= 2 else None
    pinned = bool(
        cx_delta_post is not None and np.isfinite(cx_delta_post) and abs(cx_delta_post) < 0.5
    )
    tir_held = bool(
        gamma_min_post is not None
        and gamma_min_post <= GAMMA_FULL_TIR
        and (gamma_final is None or gamma_final <= -0.95)
    )
    tir_decayed = bool(
        snap_step is not None
        and gamma_final is not None
        and gamma_final > -0.9
    )

    abs_eps_alpha = abs(eps_min - EPS_TARGET_ALPHA) if eps_min is not None else None
    abs_gamma_target = (
        abs(gamma_min_post - GAMMA_TARGET_ALPHA) if gamma_min_post is not None else None
    )

    if snap_step is None:
        verdict, outcome = "SNAP_NEVER_FIRED", "E"
    elif tir_decayed:
        verdict, outcome = "TRAP_DECAYED_POST_SNAP", "B"
    elif tir_held and pinned and abs_eps_alpha is not None and abs_eps_alpha < 0.01:
        verdict, outcome = "PERSISTENT_TRAP_NEAR_ALPHA", "A"
    elif tir_held and pinned:
        verdict, outcome = "PERSISTENT_TRAP_ALPHA_GAP", "C"
    elif tir_held:
        verdict, outcome = "PERSISTENT_TIR_NOT_PINNED", "D"
    else:
        verdict, outcome = "TRAP_NO_TIR", "F"

    return {
        "trap_amp": trap_amp,
        "snap_step": snap_step,
        "n_post_samples": len(post_gamma),
        "gamma_min_post": gamma_min_post,
        "gamma_max_post": gamma_max_post,
        "gamma_final_post": gamma_final,
        "gamma_target_for_alpha": GAMMA_TARGET_ALPHA,
        "abs_gamma_minus_target": abs_gamma_target,
        "eps_min_post": eps_min,
        "eps_final_post": eps_final,
        "abs_eps_minus_alpha": abs_eps_alpha,
        "q_eff_proxy": q_proxy,
        "q_target_1_over_alpha": Q_TARGET,
        "pinned_post": pinned,
        "cx_delta_post": cx_delta_post,
        "tir_held": tir_held,
        "tir_decayed": tir_decayed,
        "verdict": verdict,
        "outcome": outcome,
        "alpha_used_as_input": False,
    }


def classify(rows: list[dict[str, Any]]) -> dict[str, Any]:
    fired = [r for r in rows if r["snap_step"] is not None]
    persistent = [r for r in fired if r["tir_held"] and not r["tir_decayed"]]
    best = min(
        (r for r in persistent if r["abs_eps_minus_alpha"] is not None),
        key=lambda r: r["abs_eps_minus_alpha"],
        default=None,
    )

    if not fired:
        verdict, outcome = "FINISH_FAIL_NO_SNAP", "E"
    elif not persistent:
        verdict, outcome = "FINISH_TRAP_NOT_PERSISTENT", "B"
    elif best and best["abs_eps_minus_alpha"] < 0.01:
        verdict, outcome = "FINISH_NEAR_ALPHA_READOUT", "A"
    else:
        verdict, outcome = "FINISH_PERSISTENT_ALPHA_GAP", "C"

    return {
        "verdict": verdict,
        "outcome": outcome,
        "best_trap_amp": best["trap_amp"] if best else None,
        "best_abs_eps_minus_alpha": best["abs_eps_minus_alpha"] if best else None,
        "best_row": {k: v for k, v in best.items() if k != "post_gamma"} if best else None,
        "gamma_target_for_alpha": GAMMA_TARGET_ALPHA,
        "comparison_only_alpha": EPS_TARGET_ALPHA,
    }


def main() -> None:
    verify_canonical_sources()
    rows = [run_finish(amp) for amp in TRAP_AMPS]
    classification = classify(rows)
    payload = {
        "prereg": "research/2026-06-08_electron-genesis-finish-prereg.md",
        "trap_amps": TRAP_AMPS,
        "n_steps_post": N_STEPS_POST,
        "rows": rows,
        "classification": classification,
    }
    out_json = OUT_DIR / "electron_genesis_finish_results.json"
    out_json.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    print("Electron genesis finish (native persistence + eps target)")
    print(f"  Γ_target(α) = {GAMMA_TARGET_ALPHA:.6f}  ε_target = {EPS_TARGET_ALPHA}")
    for row in rows:
        q_str = f"  Q_proxy={row['q_eff_proxy']:.1f}" if row["q_eff_proxy"] else ""
        print(
            f"  trap={row['trap_amp']:.2f}  {row['verdict']} ({row['outcome']})"
            f"  Γ_min={row['gamma_min_post']}  |ε−α|={row['abs_eps_minus_alpha']}{q_str}"
        )
    print(f"  aggregate: {classification['verdict']} ({classification['outcome']})")
    if classification["best_trap_amp"] is not None:
        print(
            f"  best: trap={classification['best_trap_amp']}"
            f"  |ε−α|={classification['best_abs_eps_minus_alpha']:.5f}"
        )
    print(f"  wrote: {out_json}")


if __name__ == "__main__":
    main()
