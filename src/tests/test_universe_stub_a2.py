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
    run_sabotage_oneshot_frozen,
    run_sabotage_oversized_bias,
    run_suite,
)


def test_theta_star_is_frozen_engineering_literal_not_alpha_import():
    """R5: θ★ is a FROZEN IC-scale engineering literal near √α (θ★²=1/136.998),
    NOT √α (√ALPHA=0.08542454 → 1/137.036; off by 1.4e-4 rel). Value pinned to
    1e-12; label corrected; α-CLEAN verdict path (no ALPHA import)."""
    import universe_stub_a2 as m

    assert not hasattr(m, "ALPHA")
    assert abs(THETA_STAR - 0.08543648040856954) < 1e-12
    # It is NOT the canonical √α (would be ~0.0854245); receipt of the mismatch.
    assert abs(THETA_STAR - 0.085424543132) > 1e-5


def test_bias_on_keeps_a1_face_green():
    on = run_open_port_arm(bias=True, N=12, n_steps=400)
    assert on.passive
    assert on.R < 1e-2


def test_off_on_delta_above_floor():
    off = run_open_port_arm(bias=False, N=12, n_steps=400)
    on = run_open_port_arm(bias=True, N=12, n_steps=400)
    delta = max(abs(on.R - off.R), abs(on.A_asym - off.A_asym))
    assert delta > DELTA_FLOOR


def test_sabotage_oneshot_frozen_is_silent():
    """R4: the FROZEN one-shot sabotage (θ=10θ★ wrong-sign applied ONCE at t=0)
    NEVER injects (Hmax/H0=1.0) and leave-takes cleanly through the A1 port on the
    ON-arm's clearing window -> SILENT (trips=False). Under the frozen bin table
    this selects bin (ii) STUB-WEAK. (n_steps=400 = the fast ON-arm window where
    the legitimate bias R is a PASS; shorter windows are uncleared-residual, not
    injection — cf. R8.)"""
    r = run_sabotage_oneshot_frozen(N=12, n_steps=400)
    assert r.trips is False
    assert r.R < 1e-2  # radiates cleanly (below the R floor)
    assert r.Hmax_over_H0 <= 1.0 + 1e-3  # never injects (kinematically = the bias)


def test_sabotage_livepump_postfreeze_trips():
    """POST-FREEZE NEW AXIS: the live-pump miswiring (bias re-applied each step)
    trips loud (KEEP-BOTH alongside the frozen-axis bin (ii))."""
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


def test_run_suite_fast_frozen_bin_ii_keep_both():
    """R4 KEEP-BOTH: the FROZEN-AXIS verdict is bin (ii) STUB-WEAK (frozen one-shot
    sabotage silent), while the POST-FREEZE live-pump axis TRIPS. Δ_bias > floor
    and A1 face stays green either way."""
    out = run_suite(fast=True)
    # FROZEN-AXIS bin: one-shot sabotage silent -> STUB-WEAK.
    assert out["bin"] == "ii_STUB_WEAK"
    assert out["sabotage_frozen_oneshot"]["trips"] is False
    # POST-FREEZE NEW AXIS: live-pump miswiring trips (KEEP-BOTH).
    assert out["sabotage_postfreeze_livepump"]["trips"] is True
    assert out["postfreeze_livepump_axis"]["trips"] is True
    # The only frozen-criterion miss is the silent sabotage: Δ and face are green.
    assert out["delta_bias"] > DELTA_FLOOR
    assert out["arm_on"]["passive"]
    assert out["arm_on"]["R_pass"]
    assert out["refuse_claim_class"] == ClaimClass.EMERGENCE.value
