"""Unit tests for F6 field-channel first-rung classify() + smoke run."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_SCRIPT = _ROOT / "scripts" / "vol_1_foundations" / "f6_field_channel.py"


def _load():
    import sys

    spec = importlib.util.spec_from_file_location("f6_field_channel", _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def f6():
    return _load()


def test_classify_channel_bounded(f6):
    RunOut = f6.RunOut
    good = RunOut(0.2, 0.8, 1.0, 0.0, 1.0, 1.0, 0.99, False, True)
    off = RunOut(0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.99, False, True)
    assert f6.classify(good, off, good, off) == "CHANNEL-BOUNDED"


def test_classify_null(f6):
    RunOut = f6.RunOut
    null = RunOut(0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.99, False, True)
    off = RunOut(0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.99, False, True)
    assert f6.classify(null, off, null, off) == "NULL"


def test_classify_detonate(f6):
    RunOut = f6.RunOut
    boom = RunOut(0.2, 0.8, 1.0, 0.0, 1.0, 1.0, 0.99, True, False)
    off = RunOut(0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.99, False, True)
    assert f6.classify(boom, off, boom, off) == "DETONATE"


def test_classify_bias_moved(f6):
    RunOut = f6.RunOut
    on = RunOut(0.2, 0.8, 1.0, 0.0, 1.0, 1.0, 0.90, False, True)
    off = RunOut(0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.99, False, True)
    assert f6.classify(on, off, on, off) == "BIAS-MOVED"


def test_smoke_run_fires_channel_bounded(f6):
    """Live lattice + occupancy-slaved ledger should bank CHANNEL-BOUNDED at freeze κ."""
    off = f6.run_channel(kappa=0.0, seed_blob=False, n_steps=50)
    on = f6.run_channel(kappa=f6.KAPPA, seed_blob=False, n_steps=50)
    off_blob = f6.run_channel(kappa=0.0, seed_blob=True, n_steps=50)
    on_blob = f6.run_channel(kappa=f6.KAPPA, seed_blob=True, n_steps=50)
    verdict = f6.classify(on, off, on_blob, off_blob)
    assert verdict == "CHANNEL-BOUNDED"
    assert on.E_bath_final > f6.NULL_FLOOR
    assert on.ledger_residual <= f6.TOL_CONS
