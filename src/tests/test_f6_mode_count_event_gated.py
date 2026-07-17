"""Tests for F6 mode-count Arm A (event-gated occupancy)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "vol_1_foundations"
    / "f6_mode_count_event_gated.py"
)


@pytest.fixture(scope="module")
def arm():
    spec = importlib.util.spec_from_file_location("f6_mode_count_a", _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_classify_bounded(arm):
    RunOut = arm.RunOut
    on = RunOut(0.1, 0.9, 1.0, 0.2, 0.2, 0.01, 0.99, 0, 4, 10, False, True)
    off = RunOut(0.0, 1.0, 1.0, 0.2, 0.2, 0.0, 0.99, 0, 0, 0, False, True)
    assert arm.classify(on, off) == "CHANNEL-BOUNDED"


def test_classify_friction_renamed(arm):
    RunOut = arm.RunOut
    # bath energy without mode-count increase
    on = RunOut(0.1, 0.9, 1.0, 0.2, 0.2, 0.01, 0.99, 0, 0, 10, False, True)
    off = RunOut(0.0, 1.0, 1.0, 0.2, 0.2, 0.0, 0.99, 0, 0, 0, False, True)
    assert arm.classify(on, off) == "FRICTION-RENAMED"


def test_classify_friction_renamed_field_drop(arm):
    """Prereg §2 '(or field drop)' disjunct: field energy vanishing WITHOUT any
    bath credit and without a mode-count rise must bin FRICTION-RENAMED, not NULL
    (PR #711 review finding 10)."""
    RunOut = arm.RunOut
    # E_bath = 0 (< NULL_FLOOR), field dropped 7.68 -> 0.01, dN = 0.
    on = RunOut(0.0, 0.01, 7.68, 0.2, 0.2, 0.0, 0.99, 0, 0, 10, False, True)
    off = RunOut(0.0, 7.68, 7.68, 0.2, 0.2, 0.0, 0.99, 0, 0, 0, False, True)
    assert arm.classify(on, off) == "FRICTION-RENAMED"


def test_classify_null_silent_gate(arm):
    """NULL is reserved for a genuinely silent gate: no bath AND no field drop."""
    RunOut = arm.RunOut
    on = RunOut(0.0, 7.68, 7.68, 0.2, 0.2, 0.0, 0.99, 0, 0, 0, False, True)
    off = RunOut(0.0, 7.68, 7.68, 0.2, 0.2, 0.0, 0.99, 0, 0, 0, False, True)
    assert arm.classify(on, off) == "NULL"


def test_sabotage_friction_can_fail(arm):
    """Discriminator 7: FRICTION-RENAMED must be able to fire when modes are skipped."""
    off = arm.run_once(kappa=0.0, seed=3, n_steps=60, credit_modes=True)
    on = arm.run_once(kappa=arm.KAPPA, seed=3, n_steps=60, credit_modes=False)
    v = arm.classify(on, off)
    assert v == "FRICTION-RENAMED" or (
        v == "NULL" and on.E_bath < arm.NULL_FLOOR
    ), f"sabotage should fire FRICTION-RENAMED (or NULL if gate silent), got {v}"
    if on.E_bath >= arm.NULL_FLOOR:
        assert on.N_occ_final - on.N_occ_initial < 1


def test_smoke(arm):
    off = arm.run_once(kappa=0.0, seed=2, n_steps=40)
    on = arm.run_once(kappa=arm.KAPPA, seed=2, n_steps=40)
    v = arm.classify(on, off)
    assert v in {
        "CHANNEL-BOUNDED",
        "NULL",
        "BIAS-MOVED",
        "ELECTRON-DRAIN",
        "DETONATE",
        "FRICTION-RENAMED",
    }
    assert on.finite and off.finite
