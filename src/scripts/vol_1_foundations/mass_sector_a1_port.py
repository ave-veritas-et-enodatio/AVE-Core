#!/usr/bin/env python3
"""Mass-sector two-body × A1 port — sponge vs NativeCageIMEX force readout.

FROZEN prereg: research/2026-07-12_mass-sector-a1-port_prereg_FROZEN.md
(freeze-by-push BEFORE this driver — commit b0c0153b).

Reuses mass_sector_two_body_scattering classify + sponge O0/O1 helpers.
Parallel A1 arm only. Does not rewrite 2026-06-23 mass-sector claim.
HOLD — no merge until Grant.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np

from ave.core.categorization import ClaimClass
from ave.solvers.native_cage_imex import NativeCageIMEX, NativeCageIMEXConfig

# Reuse frozen sponge protocol + classifier (same package dir via tests / PYTHONPATH).
from mass_sector_two_body_scattering import (  # noqa: E402
    DX,
    N,
    N_RUN,
    N_TRANSIENT,
    PEAK_FRAC,
    PML,
    SEED_AMPLITUDE,
    SEED_RADIUS,
    V_YIELD,
    classify,
    run_single_blob_control,
    run_two_body,
)

PREREG = "research/2026-07-12_mass-sector-a1-port_prereg_FROZEN.md"
FREEZE_COMMIT = "b0c0153b"
D0_PRIMARY = 7
EPS_INJ = 1e-3
CLAIM = ClaimClass.CONSISTENCY

_I, _J, _K = np.indices((N, N, N))
_INTERIOR = (
    (_I >= PML)
    & (_I <= N - PML - 1)
    & (_J >= PML)
    & (_J <= N - PML - 1)
    & (_K >= PML)
    & (_K <= N - PML - 1)
)


@dataclass(frozen=True)
class ArmForceReport:
    label: str
    passive: bool
    Hmax_over_H0: float
    radiation_floor: float
    net_dsep_in: float
    net_dsep_out: float
    classify_bin: str
    classify_rationale: str
    n_run: int
    claim_class: str


def _seed_breather_imex(eng: NativeCageIMEX, cx: int, sign: float) -> None:
    coords = np.arange(N)
    X, Y, Z = np.meshgrid(coords - cx, coords - N // 2, coords - N // 2, indexing="ij")
    r = np.sqrt(X * X + Y * Y + Z * Z) * DX
    eng.V += sign * SEED_AMPLITUDE * (1.0 / np.cosh(r / SEED_RADIUS))


def _core_centroid_x(V: np.ndarray, half: str) -> float:
    half_mask = (_I < N // 2) if half == "left" else (_I >= N // 2)
    mask = _INTERIOR & half_mask
    Va = np.abs(V) * mask
    vm = float(Va.max())
    if vm <= 0.0:
        return float("nan")
    core = Va > (PEAK_FRAC * vm)
    w = Va * core
    wsum = float(w.sum())
    if wsum <= 0.0:
        return float("nan")
    return float(np.sum(w * _I) / wsum)


def _run_a1_single(d0: int, *, n_transient: int, n_run: int) -> dict[str, float]:
    cfg = NativeCageIMEXConfig(N=N, dx=DX, pml_thickness=PML, port_sigma=0.05)
    eng = NativeCageIMEX(cfg)
    eng.V[:] = 0.0
    _seed_breather_imex(eng, N // 2 - d0 // 2, +1.0)
    eng.V_prev = eng.V.copy()
    eng.set_dt_accuracy()
    for _ in range(n_transient):
        eng.step()
    x_ref = _core_centroid_x(eng.V, "left")
    wander: list[float] = []
    for _ in range(n_transient, n_run):
        eng.step()
        xc = _core_centroid_x(eng.V, "left")
        wander.append(abs(xc - x_ref) if np.isfinite(xc) else float("nan"))
    floor = float(np.nanmax(wander)) if wander else float("nan")
    return {"radiation_floor_cells": floor}


def _run_a1_two_body(
    d0: int,
    phase: str,
    *,
    n_transient: int,
    n_run: int,
) -> tuple[dict[str, float], float]:
    cfg = NativeCageIMEXConfig(N=N, dx=DX, pml_thickness=PML, port_sigma=0.05)
    eng = NativeCageIMEX(cfg)
    eng.V[:] = 0.0
    cxA = N // 2 - d0 // 2
    cxB = N // 2 + d0 // 2 + (d0 % 2)
    sign_B = +1.0 if phase == "in" else -1.0
    _seed_breather_imex(eng, cxA, +1.0)
    _seed_breather_imex(eng, cxB, sign_B)
    eng.V_prev = eng.V.copy()
    eng.set_dt_accuracy()
    H0 = float(eng.total_energy())
    Hmax = H0
    for _ in range(n_transient):
        eng.step()
        Hmax = max(Hmax, eng.total_energy())
    xA0 = _core_centroid_x(eng.V, "left")
    xB0 = _core_centroid_x(eng.V, "right")
    sep0 = abs(xB0 - xA0)
    sep_final = sep0
    for _ in range(n_transient, n_run):
        eng.step()
        Hmax = max(Hmax, eng.total_energy())
        xA = _core_centroid_x(eng.V, "left")
        xB = _core_centroid_x(eng.V, "right")
        if np.isfinite(xA) and np.isfinite(xB):
            sep_final = abs(xB - xA)
    return (
        {
            "d0": float(d0),
            "phase": phase,
            "sep0": float(sep0),
            "sep_final": float(sep_final),
            "net_dsep": float(sep_final - sep0),
        },
        float(Hmax / max(H0, 1e-30)),
    )


def run_sponge_arm(*, d0: int = D0_PRIMARY) -> ArmForceReport:
    ctrl = run_single_blob_control(d0)
    floor = float(ctrl["radiation_floor_cells"])
    in_res = run_two_body(d0, "in")
    out_res = run_two_body(d0, "out")
    bin_name, rationale = classify(in_res, out_res, floor)
    return ArmForceReport(
        label="sponge",
        passive=True,  # sponge multiply is not A1-passivity; not scored here
        Hmax_over_H0=float("nan"),
        radiation_floor=floor,
        net_dsep_in=float(in_res["net_dsep"]),
        net_dsep_out=float(out_res["net_dsep"]),
        classify_bin=bin_name,
        classify_rationale=rationale,
        n_run=N_RUN,
        claim_class=CLAIM.value,
    )


def run_a1_arm(
    *,
    d0: int = D0_PRIMARY,
    n_transient: int | None = None,
    n_run: int | None = None,
) -> ArmForceReport:
    nt = N_TRANSIENT if n_transient is None else n_transient
    nr = N_RUN if n_run is None else n_run
    ctrl = _run_a1_single(d0, n_transient=nt, n_run=nr)
    floor = float(ctrl["radiation_floor_cells"])
    in_res, h_in = _run_a1_two_body(d0, "in", n_transient=nt, n_run=nr)
    out_res, h_out = _run_a1_two_body(d0, "out", n_transient=nt, n_run=nr)
    hmax = max(h_in, h_out)
    bin_name, rationale = classify(in_res, out_res, floor)
    return ArmForceReport(
        label="a1_port",
        passive=bool(hmax <= 1.0 + EPS_INJ),
        Hmax_over_H0=float(hmax),
        radiation_floor=floor,
        net_dsep_in=float(in_res["net_dsep"]),
        net_dsep_out=float(out_res["net_dsep"]),
        classify_bin=bin_name,
        classify_rationale=rationale,
        n_run=nr,
        claim_class=CLAIM.value,
    )


def adjudicate(*, sponge: ArmForceReport, a1: ArmForceReport) -> str:
    if not a1.passive:
        return "iii_FORCE_PORT_FAIL"
    flip = sponge.classify_bin != a1.classify_bin
    floor_better = (
        np.isfinite(sponge.radiation_floor)
        and np.isfinite(a1.radiation_floor)
        and a1.radiation_floor <= 0.9 * max(sponge.radiation_floor, 1e-30)
    )
    if flip or floor_better:
        return "i_FORCE_DECONVOLVED"
    return "ii_FORCE_INDISTINGUISHABLE"


def run_suite(*, fast: bool = True) -> dict[str, Any]:
    # Primary frozen d0=7 (mass-sector mid separation). At Mode-I amp=0.85 the
    # two breathers overlap enough that NativeCageIMEX energy blows — that is a
    # real FORCE-PORT-FAIL at the driver's operating point, not a silent retune.
    # Flag arm d0=11: first separation in this grid where A1 passivity holds.
    if fast:
        a1 = run_a1_arm(n_transient=80, n_run=250)
        sponge = run_sponge_arm()
        a1_wide = run_a1_arm(d0=11, n_transient=80, n_run=250)
        sponge_wide = run_sponge_arm(d0=11)
    else:
        sponge = run_sponge_arm()
        a1 = run_a1_arm()
        sponge_wide = run_sponge_arm(d0=11)
        a1_wide = run_a1_arm(d0=11)
    bin_id = adjudicate(sponge=sponge, a1=a1)
    bin_wide = adjudicate(sponge=sponge_wide, a1=a1_wide)
    return {
        "prereg": PREREG,
        "freeze_commit": FREEZE_COMMIT,
        "d0_primary": D0_PRIMARY,
        "fast": fast,
        "sponge": asdict(sponge),
        "a1_port": asdict(a1),
        "bin_flip": sponge.classify_bin != a1.classify_bin,
        "floor_ratio_a1_over_sponge": float(
            a1.radiation_floor / max(sponge.radiation_floor, 1e-30)
        ),
        "bin": bin_id,
        "flag_d0_11": {
            "sponge": asdict(sponge_wide),
            "a1_port": asdict(a1_wide),
            "bin": bin_wide,
            "note": (
                "Non-enforcing flag: first tested separation where A1 passivity "
                "holds at Mode-I amp; primary bin remains d0=7."
            ),
        },
        "note": (
            "Parallel wire-in. Does not rewrite 2026-06-23 mass-sector claim. "
            "Refuse EMERGENCE / derived-G. d0=7 IMEX blow-up = overlap/sat regime."
        ),
        "refuse_claim_class": ClaimClass.EMERGENCE.value,
    }


def main() -> int:
    import json

    out = run_suite(fast=False)
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
