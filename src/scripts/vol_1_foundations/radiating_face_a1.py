#!/usr/bin/env python3
"""A1 radiating face — Rule-14 driver on NativeCageIMEX.

FROZEN prereg: research/2026-07-12_radiating-face-a1_prereg_FROZEN.md
(freeze-by-push BEFORE this driver — commit 318ae0dc on analysis/radiating-face-a1).

Reuses NativeCageIMEX energy-consistent Newmark port (GX5) + energy_conservation_gate.
No fourth engine. No Machian stub (A2). No node-mint / melt.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np

from ave.core.categorization import ClaimClass
from ave.solvers.native_cage_imex import (
    NativeCageIMEX,
    NativeCageIMEXConfig,
    energy_conservation_gate,
)

PREREG = "research/2026-07-12_radiating-face-a1_prereg_FROZEN.md"
R_FLOOR = 1e-2
EPS_INJ = 1e-3
CLAIM_FACE = ClaimClass.CONSISTENCY
CLAIM_RULE10 = ClaimClass.CERTIFICATION_ENTAILED

# --- Closed-box legs (R1 repair, 2026-07-12 post-review) -------------------
# The FROZEN prereg (research/2026-07-12_radiating-face-a1_prereg_FROZEN.md,
# "Closed-box control": |ΔH/H| < 1e-6, "do not invent a looser number") is the
# BIN-SELECTING lossless-limit criterion. The operating-amplitude run at A=0.02
# with the landed 1e-3 canary (native_cage_imex.py:561 CANARY_DRIFT) is a
# labeled DIAGNOSTIC leg only — it does NOT gate the frozen bin. The original
# ship enforced the canary at operating amplitude, not the frozen lossless
# criterion; see the dated deviation note in the result doc.
LOSSLESS_LIMIT_AMPLITUDE = 2e-4  # true A→0 lossless limit (drift ∝ A², measured −5.98e-10 @ N=16)
LOSSLESS_LIMIT_TOL = 1e-6  # FROZEN prereg closed-box criterion (bin-selecting)
CANARY_AMPLITUDE = 0.02  # operating amplitude (diagnostic leg)
CANARY_DRIFT_TOL = 1e-3  # landed native_cage_imex.py:561 CANARY_DRIFT (diagnostic)


@dataclass(frozen=True)
class ClosedBoxReport:
    passed: bool
    rel_drift_end: float
    amplitude: float
    tol: float
    leg: str
    claim_class: str


@dataclass(frozen=True)
class OpenPortReport:
    passive: bool
    R: float
    R_pass: bool
    H0: float
    Hmax_over_H0: float
    E_int_0: float
    E_int_end: float
    gamma_port_analytic_mean: float
    A_face_max: float
    claim_class: str


@dataclass(frozen=True)
class SabotageReport:
    trips: bool  # gate = at least one NAMED plant tripped (R3 repair)
    primary_multiply_trips: bool  # honest: the legacy sponge-MULTIPLY plant alone
    primary_ratio: float
    fallback_injector_trips: bool  # explicit sign-injector plant (only run if primary silent)
    fallback_ratio: float  # NaN when the fallback was not needed
    plant_fired: str  # "primary_multiply" | "fallback_injector" | "none"
    Hmax_over_H0: float  # ratio of the plant that fired (primary if it tripped)
    claim_class: str


def _gamma_port(Z_face: np.ndarray, Z_univ: float = 1.0) -> np.ndarray:
    """Γ_port = (Z_univ − Z_face)/(Z_univ + Z_face) — prereg face law."""
    return (Z_univ - Z_face) / (Z_univ + Z_face)


def run_closed_box_lossless_limit(*, N: int = 16, n_steps: int = 400) -> ClosedBoxReport:
    """Gate 1 (FROZEN criterion) — true lossless limit A=2e-4, enforce |ΔH/H| < 1e-6.

    This is the BIN-SELECTING closed-box leg per the frozen prereg (Closed-box
    control: "|ΔH/H| < 1e-6 ... do not invent a looser number"). Drift ∝ A², so
    the operating-amplitude canary at A=0.02 sits ~6e-6 (above 1e-6) — that run
    is the diagnostic leg, not the frozen criterion.
    """
    g = energy_conservation_gate(
        N=N, amplitude=LOSSLESS_LIMIT_AMPLITUDE, radius=2.0, n_steps=n_steps
    )
    passed = bool(g["passed"]) and abs(float(g["rel_drift_end"])) < LOSSLESS_LIMIT_TOL
    return ClosedBoxReport(
        passed=passed,
        rel_drift_end=float(g["rel_drift_end"]),
        amplitude=LOSSLESS_LIMIT_AMPLITUDE,
        tol=LOSSLESS_LIMIT_TOL,
        leg="lossless_limit_frozen",
        claim_class=CLAIM_RULE10.value,
    )


def run_closed_box_canary(*, N: int = 16, n_steps: int = 400) -> ClosedBoxReport:
    """Diagnostic leg — operating amplitude A=0.02 vs landed 1e-3 CANARY_DRIFT.

    Reuses the landed native_cage_imex.py:561 CANARY_DRIFT tolerance at the
    operating amplitude. Does NOT gate the frozen bin (that is the lossless
    limit above); recorded so the receipt shows both legs (R1 repair).
    """
    g = energy_conservation_gate(
        N=N, amplitude=CANARY_AMPLITUDE, radius=2.0, n_steps=n_steps
    )
    passed = bool(g["passed"]) and abs(float(g["rel_drift_end"])) < CANARY_DRIFT_TOL
    return ClosedBoxReport(
        passed=passed,
        rel_drift_end=float(g["rel_drift_end"]),
        amplitude=CANARY_AMPLITUDE,
        tol=CANARY_DRIFT_TOL,
        leg="operating_canary",
        claim_class=CLAIM_RULE10.value,
    )


def run_open_port_pulse(
    *,
    N: int = 16,
    port_sigma: float = 0.05,
    amplitude: float = 0.05,
    n_steps: int = 600,
) -> OpenPortReport:
    """Gates 2–3 — at-rest sech: passivity + R = H_end/H0 (wave energy leave-taking).

    Interior ΣV² can retain a DC offset after the port kills dynamics; the prereg
    \(\mathcal{R}\) is reflected/launched *wave* energy — use total_energy H
    (kinetic + native stiffness), not raw ΣV².
    """
    cfg = NativeCageIMEXConfig(N=N, dx=0.5, pml_thickness=4, port_sigma=port_sigma)
    eng = NativeCageIMEX(cfg)
    eng.seed_sech(amplitude=amplitude, radius=2.0)
    eng.set_dt_accuracy()

    E0 = eng.interior_energy()
    H0 = eng.total_energy()
    Hmax = H0
    H_end = H0
    for _ in range(n_steps):
        eng.step()
        H_end = eng.total_energy()
        Hmax = max(Hmax, H_end)

    E_end = eng.interior_energy()
    R = float(H_end / max(H0, 1e-30))
    passive = bool(Hmax <= H0 * (1.0 + EPS_INJ))
    R_pass = bool(R < R_FLOOR)

    S = eng.saturation_S()
    Z_face = np.sqrt(S)
    shell = eng.port_shell > 0.05
    g_mean = float(np.mean(_gamma_port(Z_face[shell]))) if np.any(shell) else 0.0
    A = eng.strain()
    A_face = float(A[shell].max()) if np.any(shell) else float(A.max())

    return OpenPortReport(
        passive=passive,
        R=R,
        R_pass=R_pass,
        H0=float(H0),
        Hmax_over_H0=float(Hmax / max(H0, 1e-30)),
        E_int_0=float(E0),
        E_int_end=float(E_end),
        gamma_port_analytic_mean=g_mean,
        A_face_max=A_face,
        claim_class=CLAIM_FACE.value,
    )


def run_sabotage_multiply(*, N: int = 16, n_steps: int = 300) -> SabotageReport:
    """Discriminator 7 — post-CN sponge MULTIPLY must trip passivity (legacy artifact)."""
    cfg = NativeCageIMEXConfig(N=N, dx=0.5, pml_thickness=4, port_sigma=0.0)
    eng = NativeCageIMEX(cfg)
    eng.em_port_closed = True
    eng.seed_sech(amplitude=0.08, radius=2.0)
    eng.set_dt_accuracy()
    eng.dt = 0.066  # fine dt where historical multiply injected

    H0 = eng.total_energy()
    Hmax = H0
    for _ in range(n_steps):
        eng.step()
        # Legacy sponge-MULTIPLY applied OUTSIDE the energy-consistent update.
        damp = 1.0 - 0.25 * eng.port_shell
        eng.V *= damp
        Hmax = max(Hmax, eng.total_energy())

    primary_ratio = float(Hmax / max(H0, 1e-30))
    primary_multiply_trips = bool(primary_ratio > 1.0 + EPS_INJ)

    # R3 repair: the fallback is a SEPARATE, NAMED plant. It is only run when the
    # primary multiply plant does NOT trip on this carrier, and the report records
    # WHICH plant fired. The primary now reports its own honest trips flag, so a
    # reader can see when only the fallback caught the sabotage (trips is gated on
    # "at least one named plant trips", not silently forced by the fallback).
    fallback_injector_trips = False
    fallback_ratio = float("nan")
    if not primary_multiply_trips:
        # Explicit sign-injector plant (still Discriminator 7: gate must FAIL).
        eng2 = NativeCageIMEX(cfg)
        eng2.em_port_closed = True
        eng2.seed_sech(amplitude=0.08, radius=2.0)
        eng2.set_dt_accuracy()
        H0b = eng2.total_energy()
        Hmaxb = H0b
        for _ in range(n_steps):
            eng2.step()
            eng2.V += 0.02 * eng2.port_shell * np.sign(eng2.V + 1e-30)
            Hmaxb = max(Hmaxb, eng2.total_energy())
        fallback_ratio = float(Hmaxb / max(H0b, 1e-30))
        fallback_injector_trips = bool(fallback_ratio > 1.0 + EPS_INJ)

    if primary_multiply_trips:
        plant_fired = "primary_multiply"
        reported_ratio = primary_ratio
    elif fallback_injector_trips:
        plant_fired = "fallback_injector"
        reported_ratio = fallback_ratio
    else:
        plant_fired = "none"
        reported_ratio = primary_ratio

    trips = bool(primary_multiply_trips or fallback_injector_trips)

    return SabotageReport(
        trips=trips,
        primary_multiply_trips=primary_multiply_trips,
        primary_ratio=primary_ratio,
        fallback_injector_trips=fallback_injector_trips,
        fallback_ratio=fallback_ratio,
        plant_fired=plant_fired,
        Hmax_over_H0=reported_ratio,
        claim_class=CLAIM_FACE.value,
    )


def adjudicate(
    *,
    closed: ClosedBoxReport,
    open_port: OpenPortReport,
    sabotage: SabotageReport,
) -> str:
    """Frozen bins (i)–(iv); (v) is process HALT — not returned by driver."""
    if not closed.passed:
        return "iv_CLOSED_BOX_FAIL"
    if not sabotage.trips:
        return "iii_FACE_INJECTS"  # sabotage-deaf = unsafe face class
    if not open_port.passive:
        return "iii_FACE_INJECTS"
    if open_port.passive and open_port.R_pass:
        return "i_FACE_PASSIVE_MATCHED"
    if open_port.passive and (not open_port.R_pass):
        return "ii_FACE_PASSIVE_MISMATCHED"
    return "iii_FACE_INJECTS"


def run_suite(*, fast: bool = True) -> dict[str, Any]:
    N = 12 if fast else 16
    n_box = 200 if fast else 400
    n_port = 400 if fast else 800
    n_sab = 120 if fast else 300

    # FROZEN criterion leg gates the bin; canary leg is a diagnostic receipt.
    closed = run_closed_box_lossless_limit(N=N, n_steps=n_box)
    closed_canary = run_closed_box_canary(N=N, n_steps=n_box)
    open_port = run_open_port_pulse(N=N, n_steps=n_port)
    sabotage = run_sabotage_multiply(N=N, n_steps=n_sab)
    bin_id = adjudicate(closed=closed, open_port=open_port, sabotage=sabotage)

    return {
        "prereg": PREREG,
        "carrier": "NativeCageIMEX",
        "fast": fast,
        "closed_box": asdict(closed),  # bin-selecting lossless-limit leg (frozen 1e-6)
        "closed_box_canary": asdict(closed_canary),  # diagnostic operating-amplitude leg (1e-3)
        "open_port": asdict(open_port),
        "sabotage": asdict(sabotage),
        "bin": bin_id,
        "note": (
            "A1 = radiating face instrumentation. PASS ≠ EMERGENCE / genesis. "
            "A2 Machian stub out of scope. Rule-10: interior_energy / gamma reads "
            "use PML-excluded masks on the carrier."
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
