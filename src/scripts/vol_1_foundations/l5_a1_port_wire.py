#!/usr/bin/env python3
"""L5 Q/leakage × A1 port wire-in — sponge vs NativeCageIMEX leave-taking.

FROZEN prereg: research/2026-07-12_l5-a1-port-wire_prereg_FROZEN.md
(freeze-by-push BEFORE this driver — commit 9cf436dc).

Parallel arms on the L5 rest-scale sech. Does not rewrite 2026-06-07 L5 JSON.
α comparison-only; refuse EMERGENCE. HOLD — no merge until Grant.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np

from ave.core.categorization import ClaimClass
from ave.core.master_equation_fdtd import MasterEquationFDTD
from ave.solvers.native_cage_imex import NativeCageIMEX, NativeCageIMEXConfig

PREREG = "research/2026-07-12_l5-a1-port-wire_prereg_FROZEN.md"
FREEZE_COMMIT = "9cf436dc"
AMP_REST = 0.48
SEED_RADIUS = 2.5
EPS_INJ = 1e-3
DELTA_FLOOR = 1e-4
CLAIM = ClaimClass.CONSISTENCY


@dataclass(frozen=True)
class ArmReport:
    label: str
    passive: bool
    R: float
    R_sumV2: float
    H0: float
    H_end: float
    Hmax_over_H0: float
    tau: float | None
    n_steps: int
    energy_def: str
    claim_class: str


def _fit_tau(times: np.ndarray, H: np.ndarray) -> float | None:
    """Late-window log-linear energy lifetime; None if not decaying / too short."""
    if len(times) < 8:
        return None
    # Use last half of the trace.
    i0 = len(times) // 2
    t = times[i0:]
    h = np.maximum(H[i0:], 1e-30)
    if float(np.max(h)) / float(np.min(h) + 1e-30) < 1.01:
        return None  # flat
    y = np.log(h)
    # Only fit if overall trend is downward.
    if y[-1] > y[0]:
        return None
    A = np.vstack([t, np.ones_like(t)]).T
    slope, _ = np.linalg.lstsq(A, y, rcond=None)[0]
    if slope >= -1e-12:
        return None
    return float(-1.0 / slope)


def run_sponge_arm(
    *,
    N: int = 16,
    n_steps: int = 400,
    amplitude: float = AMP_REST,
) -> ArmReport:
    eng = MasterEquationFDTD(
        N=N,
        dx=0.5,
        V_yield=1.0,
        c0=1.0,
        pml_thickness=4,
        A_cap=0.99,
        S_min=0.05,
    )
    center = (N // 2, N // 2, N // 2)
    eng.inject_localized_blob(
        center=center, radius=SEED_RADIUS, amplitude=amplitude, profile="sech"
    )
    # MasterEquation.total_energy is ΣV² (documented crude proxy).
    H0 = float(eng.total_energy())
    Hmax = H0
    times: list[float] = []
    Hs: list[float] = []
    for step in range(n_steps + 1):
        H = float(eng.total_energy())
        Hmax = max(Hmax, H)
        if step % 4 == 0:
            times.append(float(eng.time))
            Hs.append(H)
        if step < n_steps:
            eng.step()
    H_end = float(eng.total_energy())
    R = H_end / max(H0, 1e-30)
    return ArmReport(
        label="sponge",
        passive=bool(Hmax <= H0 * (1.0 + EPS_INJ)),
        R=float(R),
        R_sumV2=float(R),
        H0=H0,
        H_end=H_end,
        Hmax_over_H0=float(Hmax / max(H0, 1e-30)),
        tau=_fit_tau(np.asarray(times), np.asarray(Hs)),
        n_steps=n_steps,
        energy_def="sum_V2",
        claim_class=CLAIM.value,
    )


def run_a1_port_arm(
    *,
    N: int = 16,
    n_steps: int = 400,
    amplitude: float = AMP_REST,
    port_sigma: float = 0.05,
) -> ArmReport:
    cfg = NativeCageIMEXConfig(N=N, dx=0.5, pml_thickness=4, port_sigma=port_sigma)
    eng = NativeCageIMEX(cfg)
    eng.seed_sech(amplitude=amplitude, radius=SEED_RADIUS)
    eng.set_dt_accuracy()
    H0 = float(eng.total_energy())
    V2_0 = float(np.sum(eng.V**2))
    Hmax = H0
    times: list[float] = []
    Hs: list[float] = []
    for step in range(n_steps + 1):
        H = float(eng.total_energy())
        Hmax = max(Hmax, H)
        if step % 4 == 0:
            times.append(float(eng.time))
            Hs.append(H)
        if step < n_steps:
            eng.step()
    H_end = float(eng.total_energy())
    V2_end = float(np.sum(eng.V**2))
    R = H_end / max(H0, 1e-30)
    R_v2 = V2_end / max(V2_0, 1e-30)
    return ArmReport(
        label="a1_port",
        passive=bool(Hmax <= H0 * (1.0 + EPS_INJ)),
        R=float(R),
        R_sumV2=float(R_v2),
        H0=H0,
        H_end=H_end,
        Hmax_over_H0=float(Hmax / max(H0, 1e-30)),
        tau=_fit_tau(np.asarray(times), np.asarray(Hs)),
        n_steps=n_steps,
        energy_def="Newmark_H_plus_sumV2_flag",
        claim_class=CLAIM.value,
    )


def adjudicate(*, sponge: ArmReport, a1: ArmReport) -> str:
    if not a1.passive:
        return "iii_PORT_FAIL"
    # Primary Δ on wave-energy R (A1) vs sponge ΣV² R — also require same-proxy
    # ΣV² comparison so the bin is not pure definition mismatch.
    dR = abs(sponge.R - a1.R)
    dR_v2 = abs(sponge.R_sumV2 - a1.R_sumV2)
    dtau = None
    if sponge.tau is not None and a1.tau is not None:
        dtau = abs(sponge.tau - a1.tau)
    delta_ok = (
        (dR > DELTA_FLOOR)
        or (dR_v2 > DELTA_FLOOR)
        or (dtau is not None and dtau > DELTA_FLOOR)
    )
    if not delta_ok:
        return "ii_PORT_INDISTINGUISHABLE"
    return "i_PORT_DECONVOLVED"


def run_suite(*, fast: bool = True) -> dict[str, Any]:
    N = 12 if fast else 16
    n_steps = 200 if fast else 500
    sponge = run_sponge_arm(N=N, n_steps=n_steps)
    a1 = run_a1_port_arm(N=N, n_steps=n_steps)
    bin_id = adjudicate(sponge=sponge, a1=a1)
    return {
        "prereg": PREREG,
        "freeze_commit": FREEZE_COMMIT,
        "amplitude": AMP_REST,
        "case": "rest_scale",
        "fast": fast,
        "sponge": asdict(sponge),
        "a1_port": asdict(a1),
        "delta_R": float(abs(sponge.R - a1.R)),
        "delta_R_sumV2": float(abs(sponge.R_sumV2 - a1.R_sumV2)),
        "delta_tau": (
            abs(sponge.tau - a1.tau)
            if sponge.tau is not None and a1.tau is not None
            else None
        ),
        "bin": bin_id,
        "note": (
            "Parallel wire-in only. Does not retire 2026-06-07 L5 JSON. "
            "Sponge energy_def=sum_V2; A1 primary R uses Newmark H (A1 honesty). "
            "delta_R_sumV2 is the same-proxy cross-check. Refuse EMERGENCE."
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
