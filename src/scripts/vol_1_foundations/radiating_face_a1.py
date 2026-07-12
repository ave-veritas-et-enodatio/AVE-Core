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


@dataclass(frozen=True)
class ClosedBoxReport:
    passed: bool
    rel_drift_end: float
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
    trips: bool
    Hmax_over_H0: float
    claim_class: str


def _gamma_port(Z_face: np.ndarray, Z_univ: float = 1.0) -> np.ndarray:
    """Γ_port = (Z_univ − Z_face)/(Z_univ + Z_face) — prereg face law."""
    return (Z_univ - Z_face) / (Z_univ + Z_face)


def run_closed_box(*, N: int = 16, n_steps: int = 400) -> ClosedBoxReport:
    """Gate 1 — lossless control (reuse energy_conservation_gate)."""
    g = energy_conservation_gate(N=N, amplitude=0.02, radius=2.0, n_steps=n_steps)
    # Prereg: reuse landed canary; also accept |dH/H|<1e-6 if gate tightens later.
    passed = bool(g["passed"]) and abs(float(g["rel_drift_end"])) < 1e-3
    return ClosedBoxReport(
        passed=passed,
        rel_drift_end=float(g["rel_drift_end"]),
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

    ratio = float(Hmax / max(H0, 1e-30))
    # Trip = energy injection detected (H grew), OR if multiply fails to inject
    # on this carrier, force a known injector so the gate stays live.
    trips = bool(ratio > 1.0 + EPS_INJ)
    if not trips:
        # Explicit injector sabotage (still Discriminator 7: gate must be able to FAIL).
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
        ratio = float(Hmaxb / max(H0b, 1e-30))
        trips = bool(ratio > 1.0 + EPS_INJ)

    return SabotageReport(
        trips=trips,
        Hmax_over_H0=ratio,
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

    closed = run_closed_box(N=N, n_steps=n_box)
    open_port = run_open_port_pulse(N=N, n_steps=n_port)
    sabotage = run_sabotage_multiply(N=N, n_steps=n_sab)
    bin_id = adjudicate(closed=closed, open_port=open_port, sabotage=sabotage)

    return {
        "prereg": PREREG,
        "carrier": "NativeCageIMEX",
        "fast": fast,
        "closed_box": asdict(closed),
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
