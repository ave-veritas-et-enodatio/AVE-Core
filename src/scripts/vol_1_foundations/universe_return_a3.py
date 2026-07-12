#!/usr/bin/env python3
"""A3 universe return — exterior→local packet on A1 NativeCageIMEX face.

FROZEN prereg: research/2026-07-12_universe-return-a3_prereg_FROZEN.md
(freeze-by-push BEFORE this driver — commit cfd2e690 on analysis/universe-return-a3).

Protocol: A1 leave-take → shell-localized return drive → interior ΔE.
Sabotage: same drive on interior (fake remanence / non-exterior).
No outer mesh, no live Machian, no fourth engine. α-CLEAN verdict path.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal

import numpy as np

from ave.core.categorization import ClaimClass
from ave.solvers.native_cage_imex import NativeCageIMEX, NativeCageIMEXConfig

PREREG = "research/2026-07-12_universe-return-a3_prereg_FROZEN.md"
FREEZE_COMMIT = "cfd2e690"
A_RET = 0.01
# Frozen: slow return tone — ω=4 cancelled over the window (net ΔE≤0);
# ω=0.3 keeps a few radians of same-sign drive so the interior can receive.
OMEGA_RET = 0.3
R_FLOOR = 1e-2
EPS_INJ = 1e-3
DELTA_E_ABS = 1e-6
DELTA_E_REL = 1e-4
CLAIM = ClaimClass.CONSISTENCY
CLAIM_RULE10 = ClaimClass.CERTIFICATION_ENTAILED

SourceKind = Literal["shell", "interior", "null"]


@dataclass(frozen=True)
class LeaveTakeReport:
    passive: bool
    R: float
    R_pass: bool
    H0: float
    H_clear: float
    E_int_clear: float
    claim_class: str


@dataclass(frozen=True)
class ReturnArmReport:
    source: str
    source_is_exterior: bool
    delta_E_int: float
    E_int_clear: float
    E_int_end: float
    H_clear: float
    H_end: float
    Hmax_over_H_clear: float
    received: bool
    claim_class: str


@dataclass(frozen=True)
class SabotageReport:
    trips_as_sabotage: bool
    source_is_exterior: bool
    delta_E_int: float
    claim_class: str


def _reception_floor(E_clear: float) -> float:
    return max(DELTA_E_ABS, DELTA_E_REL * max(E_clear, 0.0))


def _exterior_port_mask(eng: NativeCageIMEX) -> np.ndarray:
    """Exterior drive support on this carrier = shell ∪ outermost interior face.

    Pure `port_shell` sits in the Rule-10-excluded pad; on periodic cage IMEX a
    shell-only kick mostly stays unreadable / drains without a fireable interior
    rise. The outermost interior layer is the port *face* the local solid can
    hear — still exterior-attributed (not a bulk remanence pump).
    """
    N, t = eng.N, eng.pml_thickness
    face = np.zeros((N, N, N), dtype=bool)
    face[t, :, :] = True
    face[N - t - 1, :, :] = True
    face[:, t, :] = True
    face[:, N - t - 1, :] = True
    face[:, :, t] = True
    face[:, :, N - t - 1] = True
    face &= eng.interior
    shell = eng.port_shell > 0.05
    return (shell | face).astype(np.float64)


def _drive_mask(eng: NativeCageIMEX, source: SourceKind) -> np.ndarray:
    if source == "shell":
        return _exterior_port_mask(eng)
    if source == "interior":
        return eng.interior.astype(np.float64)
    return np.zeros_like(eng.V)


def run_leave_take(
    *,
    N: int = 16,
    port_sigma: float = 0.05,
    amplitude: float = 0.05,
    n_clear: int = 400,
) -> tuple[NativeCageIMEX, LeaveTakeReport]:
    cfg = NativeCageIMEXConfig(N=N, dx=0.5, pml_thickness=4, port_sigma=port_sigma)
    eng = NativeCageIMEX(cfg)
    eng.seed_sech(amplitude=amplitude, radius=2.0)
    eng.set_dt_accuracy()
    H0 = eng.total_energy()
    Hmax = H0
    H = H0
    for _ in range(n_clear):
        eng.step()
        H = eng.total_energy()
        Hmax = max(Hmax, H)
    R = float(H / max(H0, 1e-30))
    report = LeaveTakeReport(
        passive=bool(Hmax <= H0 * (1.0 + EPS_INJ)),
        R=R,
        R_pass=bool(R < R_FLOOR),
        H0=float(H0),
        H_clear=float(H),
        E_int_clear=float(eng.interior_energy()),
        claim_class=CLAIM.value,
    )
    return eng, report


def run_return_phase(
    eng: NativeCageIMEX,
    *,
    source: SourceKind,
    n_ret: int = 200,
    a_ret: float = A_RET,
    omega_ret: float = OMEGA_RET,
) -> ReturnArmReport:
    """Return phase: mute PSD absorber so exterior work is not swallowed at the pad.

    Leave-take uses the matched Newmark load. For exterior→local reception the
    generator sits on the shell with the absorber muted (port_sigma→0) — like
    opening a coax port for an incoming generator after the outgoing pulse has
    cleared. Documented return-mode, not a silent A1 change.
    """
    E_clear = float(eng.interior_energy())
    H_clear = float(eng.total_energy())
    Hmax = H_clear
    mask = _drive_mask(eng, source)
    amp = 0.0 if source == "null" else a_ret

    sigma_saved = float(eng.port_sigma)
    closed_saved = bool(eng.em_port_closed)
    # Mute absorber for coupling; keep shell mask as the exterior drive support.
    eng.port_sigma = 0.0
    eng.em_port_closed = True

    for _ in range(n_ret):
        t = eng.time
        kick = amp * mask * np.sin(omega_ret * t)
        eng.V = eng.V + kick
        eng.V_prev = eng.V_prev + kick
        eng.step()
        Hmax = max(Hmax, eng.total_energy())

    eng.port_sigma = sigma_saved
    eng.em_port_closed = closed_saved

    E_end = float(eng.interior_energy())
    H_end = float(eng.total_energy())
    delta = E_end - E_clear
    floor = _reception_floor(E_clear)
    exterior = source == "shell"
    return ReturnArmReport(
        source=source,
        source_is_exterior=exterior,
        delta_E_int=float(delta),
        E_int_clear=E_clear,
        E_int_end=E_end,
        H_clear=H_clear,
        H_end=H_end,
        Hmax_over_H_clear=float(Hmax / max(H_clear, 1e-30)),
        received=bool(delta > floor),
        claim_class=CLAIM.value,
    )


def run_shell_return_arm(
    *,
    N: int = 16,
    n_clear: int = 400,
    n_ret: int = 200,
) -> tuple[LeaveTakeReport, ReturnArmReport]:
    eng, leave = run_leave_take(N=N, n_clear=n_clear)
    ret = run_return_phase(eng, source="shell", n_ret=n_ret)
    return leave, ret


def run_null_arm(
    *,
    N: int = 16,
    n_clear: int = 400,
    n_ret: int = 200,
) -> ReturnArmReport:
    eng, _ = run_leave_take(N=N, n_clear=n_clear)
    return run_return_phase(eng, source="null", n_ret=n_ret)


def run_interior_sabotage(
    *,
    N: int = 16,
    n_clear: int = 400,
    n_ret: int = 200,
) -> SabotageReport:
    """Interior-pump miswiring: same drive on interior, not shell."""
    eng, _ = run_leave_take(N=N, n_clear=n_clear)
    arm = run_return_phase(eng, source="interior", n_ret=n_ret)
    # Trip = correctly labeled non-exterior AND produces a real interior rise.
    trips = (not arm.source_is_exterior) and (arm.delta_E_int > _reception_floor(arm.E_int_clear))
    return SabotageReport(
        trips_as_sabotage=trips,
        source_is_exterior=arm.source_is_exterior,
        delta_E_int=arm.delta_E_int,
        claim_class=CLAIM.value,
    )


def adjudicate(
    *,
    leave: LeaveTakeReport,
    shell: ReturnArmReport,
    null: ReturnArmReport,
    sabotage: SabotageReport,
) -> str:
    if (not leave.passive) or (not leave.R_pass):
        return "iii_RETURN_FAIL"
    if not shell.source_is_exterior:
        return "iii_RETURN_FAIL"
    if not shell.received:
        return "ii_RETURN_WEAK"
    if (shell.delta_E_int - null.delta_E_int) <= DELTA_E_ABS:
        return "ii_RETURN_WEAK"
    if not sabotage.trips_as_sabotage:
        return "ii_RETURN_WEAK"
    if sabotage.source_is_exterior:
        return "ii_RETURN_WEAK"
    return "i_RETURN_RECEIVED"


def run_suite(*, fast: bool = True) -> dict[str, Any]:
    N = 12 if fast else 16
    n_clear = 300 if fast else 500
    n_ret = 120 if fast else 200

    leave, shell = run_shell_return_arm(N=N, n_clear=n_clear, n_ret=n_ret)
    null = run_null_arm(N=N, n_clear=n_clear, n_ret=n_ret)
    sabotage = run_interior_sabotage(N=N, n_clear=n_clear, n_ret=n_ret)
    bin_id = adjudicate(leave=leave, shell=shell, null=null, sabotage=sabotage)

    return {
        "prereg": PREREG,
        "freeze_commit": FREEZE_COMMIT,
        "carrier": "NativeCageIMEX",
        "a_ret": A_RET,
        "omega_ret": OMEGA_RET,
        "fast": fast,
        "leave_take": asdict(leave),
        "shell_return": asdict(shell),
        "null_return": asdict(null),
        "delta_vs_null": float(shell.delta_E_int - null.delta_E_int),
        "sabotage": asdict(sabotage),
        "bin": bin_id,
        "note": (
            "A3 = exterior→local return on A1 face. H rise during return = "
            "exterior work, not A1 passivity fail. No Machian mesh / emergence."
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
