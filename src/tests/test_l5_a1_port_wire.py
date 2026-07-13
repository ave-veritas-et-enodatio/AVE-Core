"""L5×A1 port wire-in gates (prereg freeze 9cf436dc)."""

from __future__ import annotations

import sys
from pathlib import Path

from ave.core.categorization import ClaimClass

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from l5_a1_port_wire import (  # noqa: E402
    DELTA_FLOOR,
    ArmReport,
    adjudicate,
    run_a1_port_arm,
    run_sponge_arm,
    run_suite,
)


def test_a1_arm_passive():
    a1 = run_a1_port_arm(N=12, n_steps=200)
    assert a1.passive
    assert a1.R < 0.05


def test_sponge_and_a1_differ():
    sponge = run_sponge_arm(N=12, n_steps=200)
    a1 = run_a1_port_arm(N=12, n_steps=200)
    assert abs(sponge.R - a1.R) > DELTA_FLOOR or abs(sponge.R_sumV2 - a1.R_sumV2) > DELTA_FLOOR


def test_adjudicate_bins():
    sponge = ArmReport(
        "sponge", True, 0.2, 0.2, 1.0, 0.2, 1.0, None, 100, "sum_V2", ClaimClass.CONSISTENCY.value
    )
    a1 = ArmReport(
        "a1_port",
        True,
        1e-4,
        0.1,
        1.0,
        1e-4,
        1.0,
        None,
        100,
        "Newmark_H",
        ClaimClass.CONSISTENCY.value,
    )
    assert adjudicate(sponge=sponge, a1=a1) == "i_PORT_DECONVOLVED"
    a1_fail = ArmReport(
        "a1_port",
        False,
        0.5,
        0.5,
        1.0,
        0.5,
        1.1,
        None,
        100,
        "Newmark_H",
        ClaimClass.CONSISTENCY.value,
    )
    assert adjudicate(sponge=sponge, a1=a1_fail) == "iii_PORT_FAIL"


def test_adjudicate_requires_same_proxy_not_pure_definition_mismatch():
    """R9: a diff that lives ONLY in the cross-proxy dR (pure energy-definition
    mismatch) while the same-proxy dR_v2 is below floor must NOT pass — AND, not
    OR. Under the old OR logic this would have read bin (i)."""
    sponge = ArmReport(
        "sponge", True, 0.2, 0.30, 1.0, 0.2, 1.0, None, 100, "sum_V2", ClaimClass.CONSISTENCY.value
    )
    a1 = ArmReport(
        "a1_port", True, 1e-4, 0.30, 1.0, 1e-4, 1.0, None, 100, "Newmark_H", ClaimClass.CONSISTENCY.value
    )
    # dR = |0.2 - 1e-4| = 0.20 (cross-proxy, above floor);
    # dR_v2 = |0.30 - 0.30| = 0 (same-proxy, BELOW floor) -> pure definition mismatch.
    assert adjudicate(sponge=sponge, a1=a1) == "ii_PORT_INDISTINGUISHABLE"


def test_run_suite_fast_bin_i():
    out = run_suite(fast=True)
    assert out["bin"] == "i_PORT_DECONVOLVED"
    assert out["refuse_claim_class"] == ClaimClass.EMERGENCE.value
    assert out["a1_port"]["passive"]
    # R9: bin (i) now requires BOTH the same-proxy ΣV² diff AND another proxy.
    assert out["adjudicator_logic"]["same_proxy_ok"]
    assert out["adjudicator_logic"]["any_other_ok"]
    assert out["delta_R_sumV2"] > DELTA_FLOOR  # same-proxy (required)
    assert out["delta_R"] > DELTA_FLOOR  # any-other (this run)
