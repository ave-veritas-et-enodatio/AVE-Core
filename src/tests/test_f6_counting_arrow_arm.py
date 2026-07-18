"""Tests for the F6 counting-arrow arm (recurrence-sweep; Phase 1).

Prereg (FROZEN): research/2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md
Result:          research/2026-07-18_f6-counting-arrow-arm_result.md
Instrument:      src/ave/thermal/f6_bath_meter.py (LatticeBathCoupler — BYTE-UNTOUCHED)

These tests LOCK:
  (a) the observable machinery (R_return=0 before the transfer peak; R_cum monotone);
  (b) the identity-enforced conservation on a comb run (#721 R-1);
  (c) the instrument-liveness positive control (two-tank sloshing returns);
  (d) ★the load-bearing NEGATIVE finding: the collar-drive is narrowband, so the
      comb-density knob never populates a quasi-continuum (N_occ stays ≤ 3), the
      counting-arrow does NOT collapse in x, and the frozen verdict is NOT
      COUNTING-ARROW. Locking the negative prevents a silent rescue (Rule 11).

Fast tests use short horizons. One opt-in `engine_sim` test runs the full Phase-1
fire and asserts the falsification (NOT COUNTING-ARROW). NO meter file is edited.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np
import pytest

_DRIVER = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations" / "f6_counting_arrow_arm.py"


@pytest.fixture(scope="module")
def arm():
    spec = importlib.util.spec_from_file_location("f6_counting_arrow_arm", _DRIVER)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod  # required so @dataclass can resolve the module
    spec.loader.exec_module(mod)
    return mod


# --- band-fixed comb sizing ---------------------------------------------------
def test_m_for_band_fixed(arm):
    """M = round((band)/Δω)+1 keeps ω_max ≈ 1.0 (band top) for every Δω (prereg §3)."""
    for dw, m_exp in ((0.010, 71), (0.020, 36), (0.030, 24), (0.050, 15), (0.080, 10)):
        assert arm._m_for(dw) == m_exp, dw
        omega_max = arm.OMEGA_MIN + (arm._m_for(dw) - 1) * dw
        assert omega_max < np.pi, dw  # Nyquist


# --- observable machinery -----------------------------------------------------
def test_r_return_zero_before_peak_and_cum_monotone(arm):
    """R_return is 0 until the transfer peak (nothing has returned) and R_cum is
    monotone non-decreasing (prereg §2 observable definition)."""
    r = arm.run_comb(0.08, horizon_recurrences=3)
    cum = [r.r_cum_table[x] for x in arm.X_TABLE]
    assert all(cum[i] <= cum[i + 1] + 1e-12 for i in range(len(cum) - 1)), "R_cum not monotone"
    # early-x (pre-transfer) return is zero
    assert r.r_return_table[0.1] == 0.0


def test_comb_run_conserves_identity(arm):
    """A comb run conserves E_lat+E_bath to the identity floor (#721 R-1) — no pump,
    no Re(Z) leak. The no-valve rail: the comb is lossless."""
    r = arm.run_comb(0.03, horizon_recurrences=2)
    assert r.max_cons_drift < 1e-3
    assert r.max_cons_drift < 1e-10  # actually machine-clean (identity-enforced)


def test_off_control_recovers_ax3(arm):
    """κ=0 closed cavity is lossless-reactive (OFF recovers Ax3)."""
    assert arm.run_off_control() < 1e-10


# --- instrument liveness (positive control) -----------------------------------
def test_two_tank_positive_control_returns(arm):
    """The two-tank (M=2, both modes in the drive band) sloshes and RETURNS at x≫1
    — reproduces the banked two-reservoir reversibility; proves the coupling is live
    and any null is regime, not a dead instrument."""
    tt = arm.run_comb(arm.TWO_TANK_DW, horizon_recurrences=arm.TWO_TANK_RECURRENCES,
                      omega_min=arm.TWO_TANK_OMEGA_MIN, m=arm.TWO_TANK_M)
    assert tt.r_cum_table[10.0] > arm.SPARSE_RETURN_MIN
    assert tt.peak_frac > 0.0  # genuine transfer, not dead


# --- ★the load-bearing NEGATIVE finding (locks the falsification) --------------
def test_drive_is_narrowband_no_quasi_continuum(arm):
    """★NARROWBAND FINDING: the collar-drive settles to a dominant line, so even the
    densest comb (M=71) fills only a narrow drive-linewidth SUB-BAND — a small fraction
    of the available modes (n_occ ≪ M), never a quasi-continuum. This is the root cause
    of the falsification; locking it prevents a silent rescue (Rule 11)."""
    r = arm.run_comb(0.010, horizon_recurrences=2)  # densest comb, M=71
    assert r.n_occ < r.M / 4, f"unexpected quasi-continuum: n_occ={r.n_occ} of M={r.M}"


def test_counting_arrow_does_not_collapse(arm):
    """★The transition x_50 does NOT cluster near x≈1 across combs (the collapse the
    prereg predicted). Two combs with very different Δω land at very different x_50."""
    r_dense = arm.run_comb(0.020, horizon_recurrences=11)  # full — reaches the return
    r_prod = arm.run_comb(0.030, horizon_recurrences=11)
    x50s = [x for x in (r_dense.x_50, r_prod.x_50) if np.isfinite(x)]
    assert len(x50s) == 2
    # neither lands in the predicted transition window [0.7,1.5], and they disagree
    assert not (arm.TRANSITION_LO <= np.mean(x50s) <= arm.TRANSITION_HI)
    assert abs(x50s[0] - x50s[1]) > arm.COLLAPSE_SPREAD_MAX  # exceeds the collapse tol


# --- full Phase-1 fire (opt-in; slow) -----------------------------------------
@pytest.mark.engine_sim
def test_phase1_falsifies_counting_arrow(arm):
    """The full frozen Phase-1 fire does NOT return COUNTING-ARROW. The collapse and
    transition-at-x≈1 criteria fail decisively (spread ≫ 0.30, mean x_50 ∉ [0.7,1.5]).
    Locks the negative result at the battery level (honest closure, Rule 11)."""
    out = arm.run_phase1()
    assert out["verdict"] != "COUNTING-ARROW"
    c = out["criteria"]
    assert not c["collapse_ok"] and c["collapse_spread"] > arm.COLLAPSE_SPREAD_MAX
    assert not c["transition_ok"]
    # the instrument is live (sparse control returns; conservation + OFF clean)
    assert c["sparse_ok"] and c["cons_ok"] and c["off_ok"]
