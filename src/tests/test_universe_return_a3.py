"""A3 universe-return gates (prereg FROZEN push-first — commit cfd2e690)."""

from __future__ import annotations

import sys
from pathlib import Path

from ave.core.categorization import ClaimClass

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from universe_return_a3 import (  # noqa: E402
    DELTA_E_ABS,
    OMEGA_RET,
    LeaveTakeReport,
    ReturnArmReport,
    SabotageReport,
    adjudicate,
    run_interior_sabotage,
    run_leave_take,
    run_null_arm,
    run_shell_return_arm,
    run_suite,
)


def test_leave_take_a1_green():
    _, leave = run_leave_take(N=12, n_clear=300)
    assert leave.passive
    assert leave.R_pass


def test_shell_return_received():
    leave, shell = run_shell_return_arm(N=12, n_clear=300, n_ret=120)
    assert leave.R_pass
    assert shell.source_is_exterior
    assert shell.received
    assert shell.delta_E_int > DELTA_E_ABS


def test_null_discrimination():
    _, shell = run_shell_return_arm(N=12, n_clear=300, n_ret=120)
    null = run_null_arm(N=12, n_clear=300, n_ret=120)
    assert (shell.delta_E_int - null.delta_E_int) > DELTA_E_ABS


def test_interior_sabotage_trips():
    sab = run_interior_sabotage(N=12, n_clear=300, n_ret=120)
    assert sab.trips_as_sabotage
    assert sab.source_is_exterior is False


def test_adjudicate_bins_frozen():
    leave = LeaveTakeReport(True, 1e-4, True, 1.0, 1e-4, 0.01, ClaimClass.CONSISTENCY.value)
    shell = ReturnArmReport(
        "shell", True, 0.1, 0.01, 0.11, 1e-4, 0.2, 2.0, True, ClaimClass.CONSISTENCY.value
    )
    null = ReturnArmReport(
        "null", False, 0.0, 0.01, 0.01, 1e-4, 1e-4, 1.0, False, ClaimClass.CONSISTENCY.value
    )
    sab = SabotageReport(True, False, 0.05, ClaimClass.CONSISTENCY.value)
    assert (
        adjudicate(leave=leave, shell=shell, null=null, sabotage=sab) == "i_RETURN_RECEIVED"
    )
    weak = SabotageReport(False, False, 0.0, ClaimClass.CONSISTENCY.value)
    assert (
        adjudicate(leave=leave, shell=shell, null=null, sabotage=weak) == "ii_RETURN_WEAK"
    )


def test_omega_ret_frozen_slow():
    assert abs(OMEGA_RET - 0.3) < 1e-12


def test_run_suite_fast_bin_i():
    out = run_suite(fast=True)
    assert out["bin"] == "i_RETURN_RECEIVED"
    assert out["refuse_claim_class"] == ClaimClass.EMERGENCE.value
    assert out["shell_return"]["received"]
    assert out["sabotage"]["trips_as_sabotage"]
    assert out["delta_vs_null"] > DELTA_E_ABS
