"""Tests for F6 field-channel rung-2."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations" / "f6_field_channel_rung2.py"


@pytest.fixture(scope="module")
def r2():
    spec = importlib.util.spec_from_file_location("f6_rung2", _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_classify_bounded(r2):
    RunOut = r2.RunOut
    on = RunOut(0.1, 0.9, 1.0, 0.2, 0.2, 0.0, 0.99, False, True)
    off = RunOut(0.0, 1.0, 1.0, 0.2, 0.2, 0.0, 0.99, False, True)
    assert r2.classify(on, off) == "CHANNEL-BOUNDED"


def test_classify_drain(r2):
    RunOut = r2.RunOut
    on = RunOut(0.1, 0.9, 1.0, 0.1, 0.2, 0.0, 0.99, False, True)
    off = RunOut(0.0, 1.0, 1.0, 0.2, 0.2, 0.0, 0.99, False, True)
    assert r2.classify(on, off) == "ELECTRON-DRAIN"


def test_smoke(r2):
    off = r2.run_once(kappa=0.0, seed=2, n_steps=40)
    on = r2.run_once(kappa=r2.KAPPA, seed=2, n_steps=40)
    v = r2.classify(on, off)
    assert v in {"CHANNEL-BOUNDED", "NULL", "BIAS-MOVED", "ELECTRON-DRAIN", "DETONATE"}
    assert on.finite and off.finite
    if v == "CHANNEL-BOUNDED":
        assert on.E_bath > r2.NULL_FLOOR
