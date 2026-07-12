"""A2 universe-stub gates (prereg FROZEN push-first — commit 257c3141)."""

from __future__ import annotations

import sys
from pathlib import Path

from ave.core.categorization import ClaimClass

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from universe_stub_a2 import (  # noqa: E402
    DELTA_FLOOR,
    THETA_STAR,
    ArmReport,
    SabotageReport,
    adjudicate,
    run_open_port_arm,
    run_sabotage_oversized_bias,
    run_suite,
)


def test_theta_star_is_frozen_literal_not_alpha_import():
    import universe_stub_a2 as m

    assert not hasattr(m, "ALPHA")
    assert abs(THETA_STAR - 0.08543648040856954) < 1e-12


def test_bias_on_keeps_a1_face_green():
    on = run_open_port_arm(bias=True, N=12, n_steps=400)
    assert on.passive
    assert on.R < 1e-2


def test_off_on_delta_above_floor():
    off = run_open_port_arm(bias=False, N=12, n_steps=400)
    on = run_open_port_arm(bias=True, N=12, n_steps=400)
    delta = max(abs(on.R - off.R), abs(on.A_asym - off.A_asym))
    assert delta > DELTA_FLOOR


def test_sabotage_trips():
    r = run_sabotage_oversized_bias(N=12, n_steps=200)
    assert r.trips is True


def test_adjudicate_bins_frozen():
    on_ok = ArmReport(
        True, 1e-4, True, 1.0, 1.0, 0.01, True, THETA_STAR, 1.0, ClaimClass.CONSISTENCY.value
    )
    off = ArmReport(
        True, 1e-4, True, 1.0, 1.0, 0.0, False, 0.0, 0.0, ClaimClass.CONSISTENCY.value
    )
    sab = SabotageReport(True, 0.05, 1.0, ClaimClass.CONSISTENCY.value)
    assert (
        adjudicate(closed_passed=True, on=on_ok, off=off, sabotage=sab)
        == "i_STUB_PASSIVE_BIASED"
    )
    sab_silent = SabotageReport(False, 1e-4, 1.0, ClaimClass.CONSISTENCY.value)
    assert (
        adjudicate(closed_passed=True, on=on_ok, off=off, sabotage=sab_silent)
        == "ii_STUB_WEAK"
    )
    on_break = ArmReport(
        False, 0.5, False, 1.0, 1.1, 0.01, True, THETA_STAR, 1.0, ClaimClass.CONSISTENCY.value
    )
    assert (
        adjudicate(closed_passed=True, on=on_break, off=off, sabotage=sab)
        == "iii_STUB_BREAKS_FACE"
    )


def test_run_suite_fast_bin_i():
    out = run_suite(fast=True)
    assert out["bin"] == "i_STUB_PASSIVE_BIASED"
    assert out["refuse_claim_class"] == ClaimClass.EMERGENCE.value
    assert out["delta_bias"] > DELTA_FLOOR
    assert out["sabotage"]["trips"]
    assert out["arm_on"]["passive"]
    assert out["arm_on"]["R_pass"]
