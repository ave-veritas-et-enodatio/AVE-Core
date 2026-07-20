"""Tests for the F6 thermal-floor arm — revival-vs-floor (STAGE 3).

Result: research/2026-07-19_f6-thermal-floor-arm_result.md
Data:   research/2026-07-19_f6-thermal-floor-arm_result.json
Driver: src/scripts/vol_1_foundations/f6_thermal_floor_arm.py
Prereg: research/2026-07-19_f6-thermal-floor-arm_prereg_FROZEN.md (FROZEN)
Instrument: src/ave/thermal/f6_bath_meter.py (BYTE-UNTOUCHED; floor = config-only)

These tests LOCK the NEGATIVE (NO-SUPPRESSION; FLOOR-ARROW falsified):

  (a) ★INDEPENDENT re-derivation from the RAW banked per-ρ series (NOT the driver's
      own verdict/self_check booleans — the #726 F9 lesson): the POST-HOC coherent
      revival (ensemble-average-first; invented at fire time, NOT pre-registered —
      PR#734 R-1) is FLAT ~0.90 across ρ∈[0,5] (non-decreasing); the frozen §4 tree
      returns NO-SUPPRESSION (disclosed DEGENERATE, S clips to 0 in the interior —
      PR#734 finding 6); every cell conserves with no clamp; ρ=0 is a seed no-op
      (self-comparison, NOT #726 value reproduction — PR#734 R-4); the detuned
      transfer is resonance-gated (its R_rev is the disclosed artifact).
  (b) ★LIVE cross-check: a live ρ=0 and ρ=5 primary cell — the coherent revival does
      NOT drop as the floor rises (locks the mechanism, not the classifier's word).

Locking the negative + the flat coherent revival prevents a silent rescue toward a
FLOOR-ARROW claim (Rule 11). NO meter file is edited. Fast (banked JSON + 2 live cells).
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
_DRIVER = _REPO / "src" / "scripts" / "vol_1_foundations" / "f6_thermal_floor_arm.py"
_JSON = _REPO / "research" / "2026-07-19_f6-thermal-floor-arm_result.json"

LEDGER_ID_TOL = 1e-6
E_BATH_MIN = 1e-2
RIDE_ON_TOP = 0.80


@pytest.fixture(scope="module")
def arm():
    spec = importlib.util.spec_from_file_location("f6_thermal_floor_arm", _DRIVER)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def banked():
    assert _JSON.exists(), f"banked arm JSON missing: {_JSON}"
    return json.loads(_JSON.read_text())


def _ladder(banked):
    return [str(r) for r in banked["meta"]["rho_ladder"]]


# --- (a) INDEPENDENT re-derivation from the raw banked series --------------------
def test_coherent_revival_is_flat_not_decaying(banked):
    """The CLEAN coherent revival (ensemble-average-first) is FLAT ~0.90 across ρ∈[0,5]
    and NON-DECREASING — FLOOR-ARROW (decay with ρ) is falsified from the raw series."""
    eaf = banked["ens_avg_first_primary"]
    vals = [eaf[r] for r in _ladder(banked)]
    assert min(vals) > 0.80                       # a real revival exists
    assert (max(vals) - min(vals)) < 0.05         # flat
    # non-decreasing (does NOT decay with ρ): last >= first within tolerance
    assert vals[-1] >= vals[0] - 0.02


def test_frozen_tree_no_suppression_from_raw(banked):
    """Re-derive the frozen §4 verdict from the raw S(ρ): S does not decrease
    (S(5)/S(0) >= 0.80) ⇒ NO-SUPPRESSION."""
    S = banked["S_primary"]
    lad = _ladder(banked)
    s0, s5 = S[lad[0]], S[lad[-1]]
    # S does not decrease -> not real_suppression -> NO-SUPPRESSION
    ratio = (s5 / s0) if s0 > 1e-9 else float("inf")
    assert ratio >= RIDE_ON_TOP
    assert banked["verdict"] == "NO-SUPPRESSION"
    assert banked["self_check"]["match"] is True


def test_every_cell_conserves_no_clamp(banked):
    """Validity gates from the raw ensemble fields: every ρ conserves (<1e-6), no clamp
    (the arm ran entirely inside FLOOR-METER-VALID-BAND[0,5])."""
    for r in _ladder(banked):
        assert banked["ensemble_primary"][r]["max_drift"] < LEDGER_ID_TOL
        assert banked["ensemble_primary"][r]["any_clamped"] is False
        assert banked["ensemble_sparse"][r]["any_clamped"] is False
    assert banked["criteria"]["conservation_ok"] is True
    assert banked["criteria"]["clamp_never"] is True


def test_cold_control_bitforbit(banked):
    """ρ=0 seed no-op == ρ=0 un-seeded, bit-for-bit. This establishes SEEDING IS A NO-OP
    at ρ=0 (a self-comparison that cannot fail); it does NOT establish #726 value
    reproduction (arm ρ=0 revival 0.899 != #726 R_cum[10]=0.932, different observables —
    PR#734 R-4)."""
    assert banked["cold_control_bitforbit_diff"] == 0.0
    assert banked["criteria"]["cold_reproduces"] is True


def test_detuned_transfer_gated_rrev_is_artifact(banked):
    """The detuned control IS resonance-gated at ρ=0 (excess plateau < 1e-2), so its
    blown-up R_rev is the disclosed NORMALIZATION artifact, not a gating failure."""
    d0 = banked["ensemble_detuned"]["0.0"]
    assert d0["excess_plateau_mean"] < E_BATH_MIN     # transfer gated
    assert d0["r_rev_mean"] > 0.5                     # yet R_rev blows up (the artifact)
    assert banked["criteria"]["detuned_valid"] is False  # the artifact symptom, disclosed


def test_reactance_pair_live_oscillator(banked):
    """Rule-10 reactance pair banked (C-state AND L-state across the window) at ρ∈{0,1,5}
    on the primary comb — the bath is a LIVE oscillator, not a static snapshot."""
    for rho in ("0.0", "1.0", "5.0"):
        rp = banked["reactance_pair"][rho]
        c = list(rp["c"].values())
        ll = list(rp["l"].values())
        assert len(c) > 3 and len(ll) > 3
        assert (max(c) - min(c)) > 0.0 or (max(ll) - min(ll)) > 0.0  # C<->L exchange


# --- (b) LIVE cross-check: the coherent revival does not drop with the floor ------
def test_live_coherent_revival_no_drop(arm):
    """LIVE: the ensemble-average-first coherent revival at ρ=5 is NOT below ρ=0 — the
    floor does not suppress the revival (the mechanism, not the label)."""
    seeds = arm.SEEDS
    cells0 = [arm.run_cell("primary", arm.PRIMARY_DW, 0.0, s, want_traj=True) for s in seeds]
    cells5 = [arm.run_cell("primary", arm.PRIMARY_DW, 5.0, s, want_traj=True) for s in seeds]
    eaf0 = arm._ens_avg_first(cells0)
    eaf5 = arm._ens_avg_first(cells5)
    assert eaf0 > 0.80
    assert eaf5 >= eaf0 - 0.05   # does NOT drop as the floor rises to 5x signal
    # and every live cell conserves with no clamp
    for c in cells0 + cells5:
        assert c.max_cons_drift < LEDGER_ID_TOL
        assert c.clamped is False


def test_live_rho0_reproduces_banked(arm, banked):
    """LIVE ρ=0 coherent revival reproduces the banked eaf[ρ=0] (bit-for-bit determinism)."""
    seeds = arm.SEEDS
    cells0 = [arm.run_cell("primary", arm.PRIMARY_DW, 0.0, s, want_traj=True) for s in seeds]
    eaf0 = arm._ens_avg_first(cells0)
    assert abs(eaf0 - banked["ens_avg_first_primary"]["0.0"]) < 1e-12
