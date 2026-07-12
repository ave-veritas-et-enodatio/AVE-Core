"""Mass-sector × A1 port wire-in (prereg freeze b0c0153b)."""

from __future__ import annotations

import sys
from pathlib import Path

from ave.core.categorization import ClaimClass

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from mass_sector_a1_port import ArmForceReport, adjudicate, run_a1_arm, run_suite  # noqa: E402


def test_primary_d0_7_port_fails_passivity_at_mode_i_amp():
    a1 = run_a1_arm(n_transient=40, n_run=120)
    assert a1.passive is False
    assert a1.Hmax_over_H0 > 1.0 + 1e-3


def test_wide_d0_11_passivity_holds():
    a1 = run_a1_arm(d0=11, n_transient=40, n_run=120)
    assert a1.passive is True


def test_adjudicate_port_fail():
    sponge = ArmForceReport(
        "sponge", True, float("nan"), 2.0, 0.0, 0.0, "NULL", "x", 100, ClaimClass.CONSISTENCY.value
    )
    a1 = ArmForceReport(
        "a1", False, 1e6, 1.0, 1.0, 1.0, "MIXED", "y", 100, ClaimClass.CONSISTENCY.value
    )
    assert adjudicate(sponge=sponge, a1=a1) == "iii_FORCE_PORT_FAIL"


def test_run_suite_fast_primary_iii():
    out = run_suite(fast=True)
    assert out["bin"] == "iii_FORCE_PORT_FAIL"
    assert out["refuse_claim_class"] == ClaimClass.EMERGENCE.value
    assert out["flag_d0_11"]["a1_port"]["passive"] is True
