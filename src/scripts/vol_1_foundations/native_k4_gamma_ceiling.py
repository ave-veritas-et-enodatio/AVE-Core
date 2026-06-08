#!/usr/bin/env python3
r"""Native K4 bond-Γ ceiling test on VacuumEngine3D.

SCOPE NOTE (2026-06-07):
Tests whether the coupled K4+Cosserat engine can reach Γ → −1 so that
ε = 1−Γ² → α is measurable. Alpha is comparison-only.

Prereg: research/2026-06-07_native-k4-gamma-ceiling-prereg.md
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np

import ave.core.constants as _avc
from ave.core.constants import ALPHA_COLD
from ave.topological.vacuum_engine import VacuumEngine3D


PROJECT_ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = PROJECT_ROOT / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PORT_SHIFTS = np.array(
    [
        [1, 1, 1],
        [1, -1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
    ],
    dtype=int,
)

AMPLITUDES = [0.2, 0.48, 0.85, 1.0, 1.5, 2.0, 3.0]
N_LATTICE = 32
PML = 4
N_STEPS = 800
CADENCE = 4
SEED_RADIUS = 2.5
SHELL_RADIUS = 8
GAMMA_FULL_TIR = -0.99
EPS_ALPHA_TARGET = float(ALPHA_COLD)


def verify_canonical_sources() -> None:
    path = Path(_avc.__file__).as_posix()
    if not path.endswith("src/ave/core/constants.py"):
        raise RuntimeError(f"unexpected constants path: {path}")


def bond_gamma_min(z: np.ndarray, mask: np.ndarray, center: tuple[int, int, int], radius: int) -> float | None:
    cx, cy, cz = center
    i, j, k = np.indices(z.shape)
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    shell = (r <= radius) & mask
    gamma = np.full(z.shape, np.nan, dtype=float)
    for shift in PORT_SHIFTS:
        z_nb = np.roll(z, shift=shift, axis=(0, 1, 2))
        denom = z_nb + z
        with np.errstate(divide="ignore", invalid="ignore"):
            g = (z_nb - z) / denom
        valid = mask & (np.abs(denom) > 1e-15)
        update = valid & (np.isnan(gamma) | (g < gamma))
        gamma[update] = g[update]
    vals = gamma[shell]
    vals = vals[np.isfinite(vals)]
    if len(vals) == 0:
        return None
    return float(np.min(vals))


def seed_sech_v_inc(engine: VacuumEngine3D, center: tuple[int, int, int], amplitude: float, radius: float) -> None:
    cx, cy, cz = center
    i, j, k = np.indices((engine.N, engine.N, engine.N))
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    envelope = amplitude / np.cosh(r / radius)
    envelope = envelope * engine.k4.mask_active.astype(float)
    for port in range(4):
        engine.k4.V_inc[..., port] = envelope / 2.0
        engine.k4.V_ref[..., port] = 0.0
    engine.k4.V_inc[~engine.k4.mask_active] = 0.0
    engine.k4.V_ref[~engine.k4.mask_active] = 0.0


def run_amplitude(amplitude: float) -> dict[str, Any]:
    center = (N_LATTICE // 2, N_LATTICE // 2, N_LATTICE // 2)
    engine = VacuumEngine3D.from_args(
        N=N_LATTICE,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
    seed_sech_v_inc(engine, center, amplitude, SEED_RADIUS)
    # Engage magnetic sector for Meissner path (S_μ → 0)
    engine.cos.initialize_electron_unknot_sector(R_target=0.5, r_target=0.25, amplitude_scale=min(amplitude, 1.0))

    gamma_trace: list[float | None] = []
    a2_trace: list[float] = []

    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            gamma_trace.append(bond_gamma_min(z, engine.k4.mask_active, center, SHELL_RADIUS))
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            a2_trace.append(float(np.max(v_sq[engine.k4.mask_active])))
        if step < N_STEPS:
            engine.step()

    gamma_min = float(np.min([g for g in gamma_trace if g is not None])) if any(g is not None for g in gamma_trace) else None
    eps = float(1.0 - gamma_min**2) if gamma_min is not None else None
    a2_peak = float(np.max(a2_trace)) if a2_trace else 0.0

    return {
        "amplitude_V_SNAP": amplitude,
        "A_squared_peak_v_inc": a2_peak,
        "gamma_min_trace": gamma_min,
        "eps_gamma": eps,
        "abs_eps_minus_alpha": abs(eps - EPS_ALPHA_TARGET) if eps is not None else None,
        "gamma_full_tir_pass": bool(gamma_min is not None and gamma_min <= GAMMA_FULL_TIR),
        "alpha_used_as_input": False,
    }


def classify(rows: list[dict[str, Any]]) -> dict[str, Any]:
    best = min(
        (r for r in rows if r.get("abs_eps_minus_alpha") is not None),
        key=lambda r: r["abs_eps_minus_alpha"],
        default=None,
    )
    any_full_tir = any(r.get("gamma_full_tir_pass") for r in rows)
    gammas = [r["gamma_min_trace"] for r in rows if r.get("gamma_min_trace") is not None]
    plateau = (
        len(gammas) >= 3
        and abs(gammas[-1] - gammas[-2]) < 0.02
        and abs(gammas[-2] - gammas[-3]) < 0.02
    )

    if any_full_tir:
        verdict = "GAMMA_CEILING_NOT_BLOCKING"
        outcome = "A"
    elif plateau and gammas and gammas[-1] > GAMMA_FULL_TIR:
        verdict = "GAMMA_CEILING_BLOCKS_ALPHA_READOUT"
        outcome = "B"
    else:
        verdict = "GAMMA_CEILING_PARTIAL"
        outcome = "C"

    return {
        "verdict": verdict,
        "outcome": outcome,
        "any_full_tir": any_full_tir,
        "gamma_plateau_at_high_amp": plateau,
        "best_eps_to_alpha": best,
        "comparison_only_alpha": EPS_ALPHA_TARGET,
        "gamma_full_tir_threshold": GAMMA_FULL_TIR,
    }


def main() -> None:
    verify_canonical_sources()
    rows = [run_amplitude(amp) for amp in AMPLITUDES]
    classification = classify(rows)
    payload = {
        "scope": "native K4 gamma ceiling; VacuumEngine3D asymmetric Meissner",
        "amplitudes_V_SNAP": AMPLITUDES,
        "rows": rows,
        "classification": classification,
    }
    out_path = OUT_DIR / "native_k4_gamma_ceiling_results.json"
    out_path.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    print("Native K4 gamma ceiling")
    print(f"  verdict: {classification['verdict']} ({classification['outcome']})")
    for row in rows:
        print(
            f"  amp={row['amplitude_V_SNAP']:.2f}  A2_v={row['A_squared_peak_v_inc']:.3f}"
            f"  gamma_min={row['gamma_min_trace']}  eps={row['eps_gamma']}"
        )
    if classification["best_eps_to_alpha"]:
        b = classification["best_eps_to_alpha"]
        print(f"  closest to alpha: amp={b['amplitude_V_SNAP']} |eps-alpha|={b['abs_eps_minus_alpha']:.4f}")
    print(f"  wrote: {out_path}")


if __name__ == "__main__":
    main()
