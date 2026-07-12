#!/usr/bin/env python3
"""A2 universe stub — projected Ω_freeze IC on A1 NativeCageIMEX face.

FROZEN prereg: research/2026-07-12_universe-stub-a2_prereg_FROZEN.md
(freeze-by-push BEFORE this driver — commit 257c3141 on analysis/universe-stub-a2).

Rule-14: reuse A1 radiating face. Projected IC only (Decision-5 scale θ★=√α as
frozen literal). No live Machian integral, no outer mesh, no fourth engine.
α-CLEAN on the verdict path: no ALPHA import.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np

from ave.core.categorization import ClaimClass
from ave.solvers.native_cage_imex import NativeCageIMEX, NativeCageIMEXConfig

# A1 closed-box reuse (same package dir when launched via tests / __main__).
from radiating_face_a1 import run_closed_box  # noqa: E402

PREREG = "research/2026-07-12_universe-stub-a2_prereg_FROZEN.md"
# Frozen √α ≈ sqrt(1/137.035999177) — IC scale only; not imported from ALPHA.
THETA_STAR = 0.08543648040856954
OMEGA_HAT = +1.0
R_FLOOR = 1e-2
EPS_INJ = 1e-3
DELTA_FLOOR = 1e-6
CLAIM = ClaimClass.CONSISTENCY
CLAIM_RULE10 = ClaimClass.CERTIFICATION_ENTAILED


@dataclass(frozen=True)
class ArmReport:
    passive: bool
    R: float
    R_pass: bool
    H0: float
    Hmax_over_H0: float
    A_asym: float
    bias_on: bool
    theta: float
    omega_sign: float
    claim_class: str


@dataclass(frozen=True)
class SabotageReport:
    trips: bool
    R: float
    Hmax_over_H0: float
    claim_class: str


def _mesh_z(eng: NativeCageIMEX) -> np.ndarray:
    N, dx = eng.N, eng.dx
    center = N // 2
    coords = (np.arange(N) - center) * dx
    _, _, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    return Z


def apply_projected_omega_freeze_bias(
    eng: NativeCageIMEX,
    *,
    theta: float = THETA_STAR,
    omega_sign: float = OMEGA_HAT,
) -> None:
    """Projected Ω_freeze IC: preferred-axis velocity kick at t=0 (at-rest → slow).

    Cage V is scalar; Decision-5 planar rotation on srs becomes a z-hat shear
    kick scaled by sin(θ). Keeps energy mostly kinetic so the A1 port can still
    leave-take the pulse (DC-only bias would fake a high R residual).
    """
    Z = _mesh_z(eng)
    axis = omega_sign * Z / (float(np.max(np.abs(Z))) + 1e-30)
    peak = float(np.max(np.abs(eng.V))) + 1e-30
    # Envelope with the seed so the kick lives on the soliton, not the pad.
    env = np.abs(eng.V) / peak
    kick = float(np.sin(theta)) * peak * 0.08 * axis * env
    # V_prev = V - kick ⇒ initial ∂tV ∝ +kick (Newmark first-step sense).
    eng.V_prev = eng.V - kick


def axis_asymmetry(eng: NativeCageIMEX) -> float:
    """⟨V·ẑ⟩ / (‖V‖₁ · ⟨|ẑ|⟩) on PML-excluded interior — frozen OFF–ON observable."""
    Z = _mesh_z(eng)
    mask = eng.interior
    V = eng.V[mask]
    z = Z[mask]
    den = (float(np.sum(np.abs(V))) * float(np.mean(np.abs(z))) + 1e-30)
    return float(np.sum(V * z) / den)


def run_open_port_arm(
    *,
    bias: bool,
    theta: float = THETA_STAR,
    omega_sign: float = OMEGA_HAT,
    N: int = 16,
    port_sigma: float = 0.05,
    amplitude: float = 0.05,
    n_steps: int = 600,
) -> ArmReport:
    cfg = NativeCageIMEXConfig(N=N, dx=0.5, pml_thickness=4, port_sigma=port_sigma)
    eng = NativeCageIMEX(cfg)
    eng.seed_sech(amplitude=amplitude, radius=2.0)
    if bias:
        apply_projected_omega_freeze_bias(eng, theta=theta, omega_sign=omega_sign)
    eng.set_dt_accuracy()

    H0 = eng.total_energy()
    Hmax = H0
    H_end = H0
    mid = max(1, n_steps // 2)
    a_asym = 0.0
    for i in range(n_steps):
        eng.step()
        H_end = eng.total_energy()
        Hmax = max(Hmax, H_end)
        if i + 1 == mid:
            a_asym = axis_asymmetry(eng)

    R = float(H_end / max(H0, 1e-30))
    return ArmReport(
        passive=bool(Hmax <= H0 * (1.0 + EPS_INJ)),
        R=R,
        R_pass=bool(R < R_FLOOR),
        H0=float(H0),
        Hmax_over_H0=float(Hmax / max(H0, 1e-30)),
        A_asym=float(a_asym),
        bias_on=bias,
        theta=float(theta if bias else 0.0),
        omega_sign=float(omega_sign if bias else 0.0),
        claim_class=CLAIM.value,
    )


def run_sabotage_oversized_bias(
    *,
    N: int = 16,
    n_steps: int = 400,
) -> SabotageReport:
    """Sabotage: wrong-sign oversized θ wired as a *live* pump (re-applied each step).

    One-shot IC — even 10×θ★ — can still leave-take through the A1 port on a long
    window (honest: projected IC is not automatically destructive). The dangerous
    miswiring is treating the cosmic projection as a continuous drive; that must
    TRIP passivity or the R floor (Discriminator-7: gate must be able to FAIL).
    """
    cfg = NativeCageIMEXConfig(N=N, dx=0.5, pml_thickness=4, port_sigma=0.05)
    eng = NativeCageIMEX(cfg)
    eng.seed_sech(amplitude=0.05, radius=2.0)
    eng.set_dt_accuracy()
    H0 = eng.total_energy()
    Hmax = H0
    H_end = H0
    for _ in range(n_steps):
        apply_projected_omega_freeze_bias(
            eng, theta=10.0 * THETA_STAR, omega_sign=-1.0
        )
        eng.step()
        H_end = eng.total_energy()
        Hmax = max(Hmax, H_end)
    R = float(H_end / max(H0, 1e-30))
    ratio = float(Hmax / max(H0, 1e-30))
    trips = bool(ratio > 1.0 + EPS_INJ) or bool(R >= R_FLOOR)
    return SabotageReport(
        trips=trips,
        R=R,
        Hmax_over_H0=ratio,
        claim_class=CLAIM.value,
    )


def adjudicate(
    *,
    closed_passed: bool,
    on: ArmReport,
    off: ArmReport,
    sabotage: SabotageReport,
) -> str:
    """Frozen bins (i)–(iii)."""
    if not closed_passed:
        return "iii_STUB_BREAKS_FACE"  # closed-box fail ⇒ face/stack unsafe
    if not on.passive or not on.R_pass:
        return "iii_STUB_BREAKS_FACE"
    delta = max(abs(on.R - off.R), abs(on.A_asym - off.A_asym))
    if not sabotage.trips:
        return "ii_STUB_WEAK"
    if delta <= DELTA_FLOOR:
        return "ii_STUB_WEAK"
    return "i_STUB_PASSIVE_BIASED"


def run_suite(*, fast: bool = True) -> dict[str, Any]:
    N = 12 if fast else 16
    n_box = 200 if fast else 400
    n_port = 400 if fast else 800
    n_sab = 200 if fast else 400

    closed = run_closed_box(N=N, n_steps=n_box)
    off = run_open_port_arm(bias=False, N=N, n_steps=n_port)
    on = run_open_port_arm(bias=True, N=N, n_steps=n_port)
    sabotage = run_sabotage_oversized_bias(N=N, n_steps=n_sab)
    delta = max(abs(on.R - off.R), abs(on.A_asym - off.A_asym))
    bin_id = adjudicate(
        closed_passed=closed.passed,
        on=on,
        off=off,
        sabotage=sabotage,
    )

    return {
        "prereg": PREREG,
        "freeze_commit": "257c3141",
        "carrier": "NativeCageIMEX",
        "theta_star": THETA_STAR,
        "omega_hat": OMEGA_HAT,
        "fast": fast,
        "closed_box": asdict(closed),
        "arm_off": asdict(off),
        "arm_on": asdict(on),
        "delta_bias": float(delta),
        "sabotage": asdict(sabotage),
        "bin": bin_id,
        "xi_machian_fence": (
            "XI_MACHIAN is a named hierarchy fence only — not bias amplitude, "
            "not a derived-G claim (G MIXED / Stage-3 fence)."
        ),
        "note": (
            "A2 = projected Ω_freeze IC on A1 face. PASS ≠ live Machian / "
            "outer mesh / emergence of G or u0*. α enters only as frozen θ★."
        ),
        "refuse_claim_class": ClaimClass.EMERGENCE.value,
        "closed_claim_class": CLAIM_RULE10.value,
    }


def main() -> int:
    import json

    out = run_suite(fast=False)
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
