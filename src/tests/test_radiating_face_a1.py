"""A1 radiating-face gates (prereg FROZEN push-first on analysis/radiating-face-a1)."""

from __future__ import annotations

import sys
from pathlib import Path

from ave.core.categorization import ClaimClass

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from radiating_face_a1 import (  # noqa: E402
    adjudicate,
    run_closed_box,
    run_open_port_pulse,
    run_sabotage_multiply,
    run_suite,
)
from radiating_face_a1 import ClosedBoxReport, OpenPortReport, SabotageReport  # noqa: E402


def test_closed_box_control_passes():
    r = run_closed_box(N=12, n_steps=150)
    assert r.passed
    assert abs(r.rel_drift_end) < 1e-3
    assert r.claim_class == ClaimClass.CERTIFICATION_ENTAILED.value


def test_open_port_passive_and_R_below_floor():
    r = run_open_port_pulse(N=12, n_steps=400)
    assert r.passive
    assert r.R < 1e-2
    assert r.claim_class != ClaimClass.EMERGENCE.value


def test_sabotage_trips():
    r = run_sabotage_multiply(N=12, n_steps=80)
    assert r.trips is True
    assert r.Hmax_over_H0 > 1.0 + 1e-3


def test_adjudicate_bins_frozen():
    closed = ClosedBoxReport(True, 0.0, ClaimClass.CERTIFICATION_ENTAILED.value)
    open_ok = OpenPortReport(
        True, 1e-4, True, 1.0, 1.0, 1.0, 0.1, 0.0, 0.01, ClaimClass.CONSISTENCY.value
    )
    open_mis = OpenPortReport(
        True, 0.5, False, 1.0, 1.0, 1.0, 0.5, 0.0, 0.01, ClaimClass.CONSISTENCY.value
    )
    sab = SabotageReport(True, 2.0, ClaimClass.CONSISTENCY.value)
    assert adjudicate(closed=closed, open_port=open_ok, sabotage=sab) == "i_FACE_PASSIVE_MATCHED"
    assert (
        adjudicate(closed=closed, open_port=open_mis, sabotage=sab)
        == "ii_FACE_PASSIVE_MISMATCHED"
    )
    bad_closed = ClosedBoxReport(False, 0.1, ClaimClass.CERTIFICATION_ENTAILED.value)
    assert (
        adjudicate(closed=bad_closed, open_port=open_ok, sabotage=sab) == "iv_CLOSED_BOX_FAIL"
    )


def test_run_suite_fast_bin_i():
    out = run_suite(fast=True)
    assert out["bin"] == "i_FACE_PASSIVE_MATCHED"
    assert out["refuse_claim_class"] == ClaimClass.EMERGENCE.value
    assert out["closed_box"]["passed"]
    assert out["open_port"]["passive"]
    assert out["sabotage"]["trips"]
