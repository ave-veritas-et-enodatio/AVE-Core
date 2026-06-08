#!/usr/bin/env python3
r"""Native electron model v2 — boundary leak + back-EMF + Lagrangian EMF channels.

Extends native_electron_model.py with the three missing physics channels from
the handoff Tier-1 stack. Tests whether they improve 4-property identification
on the canonical Golden-Torus joint seed (amp=0.92, zero drive).

SCOPE NOTE: forward channel tests; α comparison-only; does not claim derivation.

Prereg: research/2026-06-08_native-electron-model-v2-prereg.md
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

from back_emf_feedback import apply_dark_wake_back_emf  # noqa: E402
from electron_genesis_phasor_gif import _pca_ellipse, _sample_phasor, _shell_mask  # noqa: E402
from native_electron_model import (  # noqa: E402
    CADENCE,
    N_LATTICE,
    N_STEPS,
    PML,
    SAMPLE_PORT,
    SHELL_RADIUS,
    _find_central_bond,
    _seed_canonical,
)
from native_electron_propagation import energy_centroid, interior_mask  # noqa: E402
from native_k4_gamma_ceiling import GAMMA_FULL_TIR, bond_gamma_min, verify_canonical_sources  # noqa: E402
from radiation_leak_boundary import apply_radiation_leak_boundary  # noqa: E402

from ave.core.constants import ALPHA_COLD, PHI  # noqa: E402

PHI_SQ = PHI * PHI
from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402

OUT_DIR = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = OUT_DIR / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

AMPLITUDE = 0.92
ALPHA_T = float(ALPHA_COLD)
R_OVER_R_TOL = 0.15
GAMMA_TARGET = -math.sqrt(1.0 - ALPHA_T)


def _build_engine(*, lagrangian_emf: bool = False) -> VacuumEngine3D:
    return VacuumEngine3D.from_args(
        N=N_LATTICE,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
        use_lagrangian_emf_coupling=lagrangian_emf,
    )


def _core_from_cx(cx: float, cy0: int, cz0: int) -> tuple[int, int, int]:
    return (
        min(max(int(round(cx)), PML), N_LATTICE - PML - 1),
        cy0,
        cz0,
    )


def _score_records(
    records: list[dict[str, Any]],
    *,
    bond_vi: list[float],
    bond_vr: list[float],
    omega0: float,
    omega_f: float,
) -> dict[str, Any]:
    shell_vi = np.array([r["shell_phasor"][0] for r in records], dtype=float)
    shell_vr = np.array([r["shell_phasor"][1] for r in records], dtype=float)
    pca_shell = _pca_ellipse(shell_vi, shell_vr)
    pca_bond = _pca_ellipse(np.array(bond_vi), np.array(bond_vr))

    gammas = [r["gamma_min"] for r in records if r["gamma_min"] is not None]
    gamma_min = float(min(gammas)) if gammas else None
    gamma_final = gammas[-1] if gammas else None
    eps_mean = float(
        np.mean([r["eps_gamma"] for r in records if r["eps_gamma"] is not None])
    ) if records else None

    tir_held = bool(
        gamma_min is not None
        and gamma_min <= GAMMA_FULL_TIR
        and (gamma_final is None or gamma_final <= -0.95)
    )
    localized = bool(
        records
        and records[-1]["e_shell_fraction"] is not None
        and records[-1]["e_shell_fraction"] > 0.35
    )
    t2_dominant = bool(
        records
        and records[-1]["omega_shell_mean"] is not None
        and records[-1]["u_shell_mean"] is not None
        and records[-1]["omega_shell_mean"] > 3.0 * max(records[-1]["u_shell_mean"], 1e-12)
    )
    rr_shell_ok = bool(
        math.isfinite(pca_shell["R_over_r"])
        and abs(pca_shell["R_over_r"] - PHI_SQ) / PHI_SQ < R_OVER_R_TOL
    )
    rr_bond_ok = bool(
        math.isfinite(pca_bond["R_over_r"])
        and abs(pca_bond["R_over_r"] - PHI_SQ) / PHI_SQ < R_OVER_R_TOL
    )
    omega_persist = omega_f / max(omega0, 1e-30)

    props = {
        "P1_unknot_localized": localized,
        "P2_shell_Rr_near_phi_sq": rr_shell_ok,
        "P2_bond_Rr_near_phi_sq": rr_bond_ok,
        "P3_TIR_held": tir_held,
        "P4_T2_omega_dominates_u": t2_dominant,
        "P4b_omega_persistence_ge_0p5": omega_persist >= 0.5,
    }
    n_pass = sum(1 for k, v in props.items() if k.startswith("P") and not k.endswith("b") and v)

    if n_pass >= 4 and props["P4b_omega_persistence_ge_0p5"]:
        verdict, outcome = "MODEL_V2_FOUR_PROPERTY_PLUS_CIRCULATION", "A"
    elif n_pass >= 4:
        verdict, outcome = "MODEL_V2_FOUR_PROPERTY_NO_CIRCULATION", "B"
    elif tir_held and localized and n_pass >= 2:
        verdict, outcome = "MODEL_V2_PARTIAL_TRAP", "C"
    elif tir_held:
        verdict, outcome = "MODEL_V2_TIR_ONLY", "D"
    else:
        verdict, outcome = "MODEL_V2_CHANNEL_DESTABILIZED", "E"

    return {
        "gamma_min": gamma_min,
        "gamma_final": gamma_final,
        "eps_gamma_mean": eps_mean,
        "abs_eps_minus_alpha": abs(eps_mean - ALPHA_T) if eps_mean is not None else None,
        "omega_persistence_ratio": omega_persist,
        "pca_shell": pca_shell,
        "pca_bond": pca_bond,
        "property_checks": props,
        "properties_passed": n_pass,
        "verdict": verdict,
        "outcome": outcome,
    }


def run_channel_arm(
    name: str,
    *,
    boundary_leak: bool = False,
    bemf_feedback: bool = False,
    lagrangian_emf: bool = False,
    bemf_gain: float = 0.12,
) -> dict[str, Any]:
    engine = _build_engine(lagrangian_emf=lagrangian_emf)
    _seed_canonical(engine, amplitude=AMPLITUDE)

    n = N_LATTICE
    cy0 = cz0 = n // 2
    mask = interior_mask(n, PML) & engine.k4.mask_active
    bond_a, bond_port = _find_central_bond(engine)

    records: list[dict[str, Any]] = []
    bond_vi: list[float] = []
    bond_vr: list[float] = []
    last_cx = float(n // 2)

    omega0 = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())

    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            cx, _, _ = energy_centroid(v_sq, mask)
            if np.isfinite(cx):
                last_cx = cx
            core = _core_from_cx(last_cx, cy0, cz0)
            gamma = bond_gamma_min(z, engine.k4.mask_active, core, SHELL_RADIUS)
            vi, vr = _sample_phasor(engine, core, SAMPLE_PORT, shell_radius=SHELL_RADIUS)
            ax, ay, az = bond_a
            bond_vi.append(float(engine.k4.V_inc[ax, ay, az, bond_port]))
            bond_vr.append(float(engine.k4.V_ref[ax, ay, az, bond_port]))

            omega = np.asarray(engine.cos.omega)
            u = np.asarray(engine.cos.u)
            sh = _shell_mask(v_sq.shape, core, SHELL_RADIUS, engine.k4.mask_active)
            omega_shell = float(np.mean(np.linalg.norm(omega[sh], axis=-1))) if np.any(sh) else 0.0
            u_shell = float(np.mean(np.linalg.norm(u[sh], axis=-1))) if np.any(sh) else 0.0
            e_tot = float(np.sum(v_sq))
            e_shell_frac = float(np.sum(v_sq[sh]) / max(e_tot, 1e-30)) if np.any(sh) else None

            records.append(
                {
                    "step": step,
                    "gamma_min": gamma,
                    "eps_gamma": float(1.0 - gamma**2) if gamma is not None else None,
                    "shell_phasor": [vi, vr],
                    "omega_shell_mean": omega_shell,
                    "u_shell_mean": u_shell,
                    "e_shell_fraction": e_shell_frac,
                }
            )

        if step < N_STEPS:
            engine.step()
            core = _core_from_cx(last_cx, cy0, cz0)
            if bemf_feedback:
                apply_dark_wake_back_emf(engine, gain=bemf_gain)
            if boundary_leak:
                apply_radiation_leak_boundary(engine, core, SHELL_RADIUS)

    omega_f = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    scored = _score_records(records, bond_vi=bond_vi, bond_vr=bond_vr, omega0=omega0, omega_f=omega_f)

    return {
        "variant": name,
        "amplitude_V_SNAP": AMPLITUDE,
        "channels": {
            "boundary_leak_V_ref_only": boundary_leak,
            "dark_wake_bemf_on_u": bemf_feedback,
            "lagrangian_emf_coupling": lagrangian_emf,
            "bemf_gain": bemf_gain if bemf_feedback else None,
        },
        "n_steps": N_STEPS,
        "gamma_target_for_alpha": GAMMA_TARGET,
        "comparison_only_alpha": ALPHA_T,
        "alpha_used_as_input": boundary_leak,
        **scored,
    }


def classify(rows: list[dict[str, Any]]) -> dict[str, Any]:
    baseline = next((r for r in rows if r["variant"] == "baseline"), None)
    best = max(rows, key=lambda r: (r["properties_passed"], r["property_checks"].get("P4b_omega_persistence_ge_0p5", False)))
    improved_eps = bool(
        baseline
        and best
        and baseline.get("abs_eps_minus_alpha") is not None
        and best.get("abs_eps_minus_alpha") is not None
        and best["abs_eps_minus_alpha"] < baseline["abs_eps_minus_alpha"] - 1e-4
    )
    improved_omega = bool(
        baseline
        and best
        and best["omega_persistence_ratio"] > baseline["omega_persistence_ratio"] + 0.05
    )
    stable = [r for r in rows if r["property_checks"]["P3_TIR_held"] and r["gamma_final"] is not None and r["gamma_final"] <= -0.95]
    if best["outcome"] == "A":
        agg = "V2_CHANNELS_LANDED_ELECTRON_MODEL"
    elif stable and all(r["properties_passed"] <= 2 for r in stable):
        agg = "V2_CHANNELS_NO_BREAKTHROUGH"
    elif improved_eps:
        agg = "V2_CHANNELS_EPS_IMPROVED"
    else:
        agg = "V2_CHANNELS_DESTABILIZED_TRAP"
    return {
        "aggregate_verdict": agg,
        "best_variant": best["variant"],
        "best_properties_passed": best["properties_passed"],
        "best_omega_persistence": best["omega_persistence_ratio"],
        "baseline_omega_persistence": baseline["omega_persistence_ratio"] if baseline else None,
        "improved_omega": improved_omega,
        "improved_eps": improved_eps,
    }


def main() -> None:
    verify_canonical_sources()
    print("Native electron model v2 (boundary leak + BEMF + EMF channels)")
    arms = [
        ("baseline", dict()),
        ("boundary_leak", dict(boundary_leak=True)),
        ("bemf_feedback", dict(bemf_feedback=True)),
        ("leak_plus_bemf", dict(boundary_leak=True, bemf_feedback=True)),
        ("leak_bemf_emf", dict(boundary_leak=True, bemf_feedback=True, lagrangian_emf=True)),
    ]
    rows = [run_channel_arm(name, **kwargs) for name, kwargs in arms]
    classification = classify(rows)

    payload = {
        "prereg": "research/2026-06-08_native-electron-model-v2-prereg.md",
        "parent": "native_electron_model.py",
        "rows": rows,
        "classification": classification,
    }
    out_json = OUT_DIR / "native_electron_model_v2_results.json"
    out_json.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    for row in rows:
        print(
            f"  {row['variant']}: {row['verdict']} pass={row['properties_passed']}/4"
            f"  ω_persist={row['omega_persistence_ratio']:.3f}"
            f"  ε̄={row['eps_gamma_mean']:.4f}"
            f"  Γ_min={row['gamma_min']}"
            f"  bond R/r={row['pca_bond']['R_over_r']:.2f}"
        )
    print(f"  aggregate: {classification['aggregate_verdict']}")
    print(f"  wrote: {out_json}")


if __name__ == "__main__":
    main()
