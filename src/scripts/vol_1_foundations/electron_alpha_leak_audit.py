#!/usr/bin/env python3
r"""Alpha leak proxy audit on persistent native electron trap.

Prereg: research/2026-06-08_electron-alpha-leak-audit-prereg.md

Measures multiple α-free leak proxies post-snap; scores vs ALPHA_COLD only.
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
    bond_gamma_min,
    seed_sech_v_inc,
    verify_canonical_sources,
)

from ave.core.constants import ALPHA_COLD, Z_0  # noqa: E402
from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402

OUT_DIR = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = OUT_DIR / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

N_LATTICE = 32
PML = 4
N_STEPS_PRE = 400
N_STEPS_POST = 800
CADENCE = 2
SEED_RADIUS = 2.5
SHELL_RADIUS = 6
V_DRIVE_PRE = 0.04
AMP_START = 0.48
TRAP_AMP = 1.5
TRIGGER_X = 14.0
CX0_FRAC = 0.28

ALPHA_T = float(ALPHA_COLD)
GAMMA_TARGET = -math.sqrt(1.0 - ALPHA_T)
REL_TOL = 0.10


def _core_idx(cx: float, cy0: int, cz0: int, n: int) -> tuple[int, int, int]:
    return (
        min(max(int(round(cx)), PML), n - PML - 1),
        cy0,
        cz0,
    )


def _shell_mask(
    shape: tuple[int, int, int],
    center: tuple[int, int, int],
    radius: int,
    active: np.ndarray,
) -> np.ndarray:
    cx, cy, cz = center
    i, j, k = np.indices(shape)
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    return (r <= radius) & active


def _saturation_at_core(engine: VacuumEngine3D, core: tuple[int, int, int]) -> dict[str, float]:
    import jax.numpy as jnp

    from ave.topological.cosserat_field_3d import _update_saturation_kernels

    V_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
    S_mu, S_eps = _update_saturation_kernels(
        jnp.asarray(engine.cos.u),
        jnp.asarray(engine.cos.omega),
        jnp.asarray(V_sq),
        engine.cos.dx,
        engine.V_SNAP,
        engine.cos.omega_yield,
        engine.cos.epsilon_yield,
        engine._coupled.kappa_chiral,
    )
    S_mu = float(np.asarray(S_mu)[core])
    S_eps = float(np.asarray(S_eps)[core])
    S_combined = math.sqrt(max(S_mu * S_eps, 1e-30))
    z_local = float(np.asarray(engine.k4.z_local_field)[core])
    return {
        "S_mu": S_mu,
        "S_eps": S_eps,
        "S_combined": S_combined,
        "z_local": z_local,
    }


def _per_cycle_slopes(
    steps: list[int],
    values: list[float],
    steps_per_cycle: float,
) -> dict[str, float | None]:
    if len(values) < 4 or steps_per_cycle <= 0:
        return {"mean_abs_fractional_per_cycle": None, "n_windows": 0}

    arr = np.asarray(values, dtype=float)
    st = np.asarray(steps, dtype=float)
    window = max(2, int(round(steps_per_cycle)))
    fracs: list[float] = []
    for i in range(0, len(arr) - 1, max(1, window // CADENCE)):
        j = min(i + window // CADENCE, len(arr) - 1)
        if j <= i:
            continue
        e0, e1 = arr[i], arr[j]
        if abs(e0) < 1e-30:
            continue
        dt_steps = st[j] - st[i]
        if dt_steps <= 0:
            continue
        frac = abs((e1 - e0) / e0) * (steps_per_cycle / dt_steps)
        fracs.append(float(frac))

    if not fracs:
        return {"mean_abs_fractional_per_cycle": None, "n_windows": 0}
    return {
        "mean_abs_fractional_per_cycle": float(np.mean(fracs)),
        "n_windows": len(fracs),
    }


def run_audit() -> dict[str, Any]:
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
    total_steps = N_STEPS_PRE + N_STEPS_POST

    post_records: list[dict[str, Any]] = []

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
                shell = _shell_mask(v_sq.shape, core, SHELL_RADIUS, engine.k4.mask_active)
                gamma = bond_gamma_min(z, engine.k4.mask_active, core, SHELL_RADIUS)
                sat = _saturation_at_core(engine, core)
                e_shell = float(np.sum(v_sq[shell]))
                h_total = float(engine._coupled.total_hamiltonian())
                e_k4 = float(engine.k4.total_energy())
                e_cos = float(engine.cos.total_energy())

                post_records.append(
                    {
                        "step": step,
                        "gamma_min": gamma,
                        "eps_gamma": float(1.0 - gamma**2) if gamma is not None else None,
                        "one_minus_abs_gamma": float(1.0 - abs(gamma)) if gamma is not None else None,
                        "eps_S_combined": float(1.0 - sat["S_combined"] ** 2),
                        "eps_S_mu": float(1.0 - sat["S_mu"] ** 2),
                        "eps_S_eps": float(1.0 - sat["S_eps"] ** 2),
                        "inv_z_squared": float(1.0 / max(sat["z_local"] ** 2, 1e-30)),
                        "E_shell": e_shell,
                        "H_total": h_total,
                        "E_K4": e_k4,
                        "E_cos": e_cos,
                        "S_mu": sat["S_mu"],
                        "S_eps": sat["S_eps"],
                        "z_local": sat["z_local"],
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

    dt = float(engine._coupled.outer_dt)
    omega_y = float(engine.cos.omega_yield)
    steps_per_cycle = (2.0 * math.pi / omega_y) / dt if omega_y > 0 else None

    # Time-averaged static proxies (post-snap)
    def _mean(key: str) -> float | None:
        vals = [r[key] for r in post_records if r.get(key) is not None]
        return float(np.mean(vals)) if vals else None

    static_proxies = {
        "P1_eps_gamma": _mean("eps_gamma"),
        "P2_eps_S_combined": _mean("eps_S_combined"),
        "P3_eps_S_mu": _mean("eps_S_mu"),
        "P4_eps_S_eps": _mean("eps_S_eps"),
        "P7_one_minus_abs_gamma": _mean("one_minus_abs_gamma"),
        "P9_inv_z_squared": _mean("inv_z_squared"),
    }

    h_slope = _per_cycle_slopes(
        [r["step"] for r in post_records],
        [r["H_total"] for r in post_records],
        steps_per_cycle or 1.0,
    )
    shell_slope = _per_cycle_slopes(
        [r["step"] for r in post_records],
        [r["E_shell"] for r in post_records],
        steps_per_cycle or 1.0,
    )
    static_proxies["P5_shell_leak_per_cycle"] = shell_slope["mean_abs_fractional_per_cycle"]
    static_proxies["P6_H_leak_per_cycle"] = h_slope["mean_abs_fractional_per_cycle"]
    if shell_slope["mean_abs_fractional_per_cycle"] is not None:
        static_proxies["P8_Q_from_shell_decay"] = 1.0 / max(
            shell_slope["mean_abs_fractional_per_cycle"], 1e-30
        )

    # Score vs alpha
    scored: list[dict[str, Any]] = []
    for name, val in static_proxies.items():
        if val is None:
            continue
        err = abs(val - ALPHA_T)
        scored.append(
            {
                "proxy": name,
                "value": val,
                "abs_err_vs_alpha": err,
                "rel_err_vs_alpha": err / ALPHA_T,
                "within_10pct": err / ALPHA_T < REL_TOL,
                "Q_proxy": 1.0 / val if val > 1e-12 else None,
            }
        )

    scored.sort(key=lambda x: x["abs_err_vs_alpha"])
    best = scored[0] if scored else None

    h_leak = static_proxies.get("P6_H_leak_per_cycle")
    lossless = bool(h_leak is not None and h_leak < 1e-4)

    if best and best["within_10pct"]:
        verdict, outcome = "LEAK_PROXY_MATCH", "A"
    elif best and best["proxy"] == "P1_eps_gamma":
        verdict, outcome = "EPS_GAMMA_BEST_BUT_GAP", "B"
    elif lossless:
        verdict, outcome = "LOSSLESS_NO_PER_CYCLE_LEAK", "C"
    else:
        verdict, outcome = "LEAK_PROXY_NONE_MATCH", "D"

    return {
        "trap_amp": TRAP_AMP,
        "snap_step": snap_step,
        "n_post_samples": len(post_records),
        "dt_outer": dt,
        "omega_yield": omega_y,
        "steps_per_compton_cycle": steps_per_cycle,
        "gamma_target_for_alpha": GAMMA_TARGET,
        "comparison_only_alpha": ALPHA_T,
        "comparison_Z0_over_4pi": float(Z_0 / (4.0 * math.pi)),
        "static_proxies": static_proxies,
        "proxy_scores": scored,
        "best_proxy": best,
        "hamiltonian_lossless": lossless,
        "shell_leak_windows": shell_slope["n_windows"],
        "verdict": verdict,
        "outcome": outcome,
        "alpha_used_as_input": False,
        "interpretation": (
            "Theorem 3.1' expects per-cycle leak 1/Q=alpha through R=Z0/(4pi). "
            "If P6~0 and no static proxy matches alpha, gap is lossless dynamics + wrong observable."
        ),
    }


def main() -> None:
    verify_canonical_sources()
    result = run_audit()
    out_json = OUT_DIR / "electron_alpha_leak_audit_results.json"
    out_json.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")

    print("Electron alpha leak proxy audit")
    print(f"  verdict: {result['verdict']} ({result['outcome']})")
    print(f"  lossless H: {result['hamiltonian_lossless']}")
    print(f"  steps/cycle: {result['steps_per_compton_cycle']}")
    if result["best_proxy"]:
        b = result["best_proxy"]
        print(
            f"  best: {b['proxy']} = {b['value']:.6g}"
            f"  |err|={b['abs_err_vs_alpha']:.6g}"
            f"  Q_proxy={b.get('Q_proxy')}"
        )
    print("  all proxies:")
    for row in result["proxy_scores"]:
        print(
            f"    {row['proxy']:22s}  val={row['value']:.6g}"
            f"  |Δα|={row['abs_err_vs_alpha']:.6g}"
            f"  within10%={row['within_10pct']}"
        )
    print(f"  wrote: {out_json}")


if __name__ == "__main__":
    main()
