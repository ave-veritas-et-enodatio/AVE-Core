#!/usr/bin/env python3
r"""Projection vs native bond-Γ gate (why −0.63 vs −0.99?).

At matched amplitudes, compare:
  - **Projection:** MasterEquationFDTD scalar → PhasorBridge z(S(|V|)) → bond Γ_min
  - **Native:** VacuumEngine3D coupled z_local_total → bond Γ_min

Hypothesis: projection uses scalar-only S_ε; native asymmetric Meissner reaches
full TIR when amp ≥ 1.

Alpha comparison-only.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from native_k4_gamma_ceiling import (  # noqa: E402
    bond_gamma_min,
    seed_sech_v_inc,
    verify_canonical_sources,
)

import ave.core.constants as _avc
from ave.core.constants import ALPHA_COLD
from ave.core.master_equation_fdtd import MasterEquationFDTD
from ave.core.master_fdtd_phasor_bridge import MasterFDTDPhasorBridge
from ave.topological.vacuum_engine import VacuumEngine3D

OUT_DIR = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = OUT_DIR / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

AMPLITUDES = [0.48, 1.0, 1.5, 3.0]
N = 32
PML = 4
N_STEPS = 600
CADENCE = 4
SEED_RADIUS = 2.5
SHELL_RADIUS = 8
GAMMA_FULL_TIR = -0.99


def seed_scalar_fdtd(engine: MasterEquationFDTD, center: tuple[int, int, int], amp: float) -> None:
    cx, cy, cz = center
    i, j, k = np.indices(engine.V.shape)
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    # amplitude is V_SNAP fraction; engine uses natural units with V_yield=1
    envelope = amp / np.cosh(r / SEED_RADIUS)
    engine.V += envelope
    engine.V_prev = engine.V.copy()


def run_projection(amplitude: float) -> dict[str, Any]:
    center = (N // 2, N // 2, N // 2)
    engine = MasterEquationFDTD(N=N, dx=1.0, V_yield=1.0, c0=1.0, pml_thickness=PML)
    bridge = MasterFDTDPhasorBridge(N, N, N, dx=engine.dx, V_yield=engine.V_yield, dt=engine.dt)
    seed_scalar_fdtd(engine, center, amplitude)

    gamma_trace: list[float | None] = []
    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            bridge.project_from_scalar(engine.V, engine.V_prev)
            g = bridge.bond_gamma_min_in_shell(
                engine.V,
                center=center,
                radius=SHELL_RADIUS,
                threshold_frac=0.1,
            )
            gamma_trace.append(g)
        if step < N_STEPS:
            engine.step()
            bridge.project_from_scalar(engine.V, engine.V_prev)

    gammas = [g for g in gamma_trace if g is not None]
    gamma_min = float(min(gammas)) if gammas else None
    return {
        "lane": "projection",
        "amplitude_V_SNAP": amplitude,
        "gamma_min": gamma_min,
        "eps_gamma": float(1.0 - gamma_min**2) if gamma_min is not None else None,
        "gamma_full_tir": bool(gamma_min is not None and gamma_min <= GAMMA_FULL_TIR),
    }


def run_native(amplitude: float) -> dict[str, Any]:
    center = (N // 2, N // 2, N // 2)
    engine = VacuumEngine3D.from_args(
        N=N,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
    seed_sech_v_inc(engine, center, amplitude, SEED_RADIUS)
    engine.cos.initialize_electron_unknot_sector(
        R_target=0.5, r_target=0.25, amplitude_scale=min(amplitude, 1.0)
    )

    gamma_trace: list[float | None] = []
    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            gamma_trace.append(bond_gamma_min(z, engine.k4.mask_active, center, SHELL_RADIUS))
        if step < N_STEPS:
            engine.step()

    gammas = [g for g in gamma_trace if g is not None]
    gamma_min = float(min(gammas)) if gammas else None
    return {
        "lane": "native",
        "amplitude_V_SNAP": amplitude,
        "gamma_min": gamma_min,
        "eps_gamma": float(1.0 - gamma_min**2) if gamma_min is not None else None,
        "gamma_full_tir": bool(gamma_min is not None and gamma_min <= GAMMA_FULL_TIR),
    }


def classify(pairs: list[dict[str, Any]]) -> dict[str, Any]:
    splits = []
    for amp in AMPLITUDES:
        proj = next(r for r in pairs if r["lane"] == "projection" and r["amplitude_V_SNAP"] == amp)
        nat = next(r for r in pairs if r["lane"] == "native" and r["amplitude_V_SNAP"] == amp)
        delta = None
        if proj["gamma_min"] is not None and nat["gamma_min"] is not None:
            delta = float(nat["gamma_min"] - proj["gamma_min"])
        splits.append(
            {
                "amplitude": amp,
                "gamma_projection": proj["gamma_min"],
                "gamma_native": nat["gamma_min"],
                "delta_native_minus_projection": delta,
                "native_tir": nat["gamma_full_tir"],
                "projection_tir": proj["gamma_full_tir"],
            }
        )

    wall_split = [s for s in splits if s["amplitude"] >= 1.0 and s["delta_native_minus_projection"] is not None]
    native_reaches_tir = any(s["native_tir"] for s in splits)
    proj_stalls = all(
        not s["projection_tir"] for s in splits if s["amplitude"] >= 2.0
    ) or any(
        s["gamma_projection"] is not None and s["gamma_projection"] > -0.7
        for s in splits
        if s["amplitude"] >= 2.0
    )

    if native_reaches_tir and proj_stalls and wall_split:
        verdict = "LANE_SPLIT_CONFIRMED"
        outcome = "A"
    elif native_reaches_tir:
        verdict = "NATIVE_TIR_PROJECTION_MIXED"
        outcome = "B"
    else:
        verdict = "GATE_INCONCLUSIVE"
        outcome = "C"

    return {
        "verdict": verdict,
        "outcome": outcome,
        "splits": splits,
        "comparison_only_alpha": float(ALPHA_COLD),
    }


def main() -> None:
    verify_canonical_sources()
    pairs: list[dict[str, Any]] = []
    for amp in AMPLITUDES:
        pairs.append(run_projection(amp))
        pairs.append(run_native(amp))
        print(
            f"  amp={amp:.2f}  proj_Γ={pairs[-2]['gamma_min']}  native_Γ={pairs[-1]['gamma_min']}"
        )

    classification = classify(pairs)
    payload = {"pairs": pairs, "classification": classification}
    out_json = OUT_DIR / "projection_native_gamma_gate_results.json"
    out_json.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    print(f"Projection vs native gamma gate: {classification['verdict']} ({classification['outcome']})")
    for s in classification["splits"]:
        print(
            f"  amp={s['amplitude']:.2f}  ΔΓ={s['delta_native_minus_projection']}"
            f"  proj={s['gamma_projection']}  native={s['gamma_native']}"
        )
    print(f"  wrote: {out_json}")


if __name__ == "__main__":
    main()
