"""Tests for the F6 certified-κ recurrence sweep (the SUFFICIENT counting-arrow test).

Prereg (FROZEN): research/2026-07-18_f6-certified-kappa-sweep_prereg_FROZEN.md
Driver: src/scripts/vol_1_foundations/f6_certified_kappa_sweep.py
Instrument: src/ave/thermal/f6_bath_meter.py (BYTE-UNTOUCHED).

Fast unit tests (default suite) guard the FROZEN thresholds against retune (Rule 11)
and exercise the §4 decision-tree PRECEDENCE byte-faithfully (the #722 R-10 lesson: a
fire-condition set is not a classifier — the tree + precedence are the classifier).
Two opt-in `engine_sim` tests run lattice cells and assert (a) the sparsest/two-tank
controls reproduce the reval-banked X4 numbers bit-for-bit, and (b) the full frozen
grid returns FOREIGN-EATER with the byte-faithful self-check green. NO meter/engine edit.
"""

from __future__ import annotations

import pytest

from scripts.vol_1_foundations import f6_certified_kappa_sweep as sweep


# --- FROZEN thresholds must equal the prereg §4 values (guard against retune) --
def test_frozen_thresholds_match_prereg():
    """Rule 11: the shipped thresholds are the prereg §4 frozen values, unchanged."""
    assert sweep.KAPPA_SWEEP == 0.030          # the single certified point [0.030,0.030]
    assert sweep.SEED_SCALE_MILD == 0.6        # MILD, A_max≈0.10 — the certified cell
    assert sweep.CONS_TOL == 1e-3
    assert sweep.T63_GATE == 0.5               # DERIVED regime gate
    assert sweep.NOCC_GATE == 10               # DERIVED regime gate
    assert sweep.E_BATH_MIN == 1e-2
    assert sweep.SPARSE_RETURN_MIN == 0.70
    assert sweep.COLLAPSE_SPREAD_MAX == 0.30
    assert (sweep.TRANSITION_LO, sweep.TRANSITION_HI) == (0.7, 1.5)
    assert sweep.DENSE_PLATEAU_MAX == 0.30
    assert sweep.OFF_DRIFT_MAX == 1e-10
    assert sweep.BIAS_TARE_TOL == 0.05
    assert sweep.DETUNE_M == 32                 # frozen detuned-probe (§7 placement)
    assert sweep.DETUNE_DW == 0.030


def _base_crit() -> dict:
    """A criteria dict on which every §4 gate PASSES ⇒ COUNTING-ARROW."""
    return {
        "nan_seen": False, "cons_ok": True,
        "t63_gate_ok": True, "nocc_gate_ok": True, "transfer_ok": True,
        "grid_return_ok": True, "dense_pins_low": True,
        "collapse_ok": True, "transition_ok": True, "controls_ok": True,
        "off_ok": True, "mode_count_ok": True, "bias_ok": True, "det_gated": True,
    }


def _verdict(crit: dict) -> str:
    return sweep.self_check({"criteria": crit, "verdict": None})["recomputed"]


# --- §4 decision-tree PRECEDENCE, byte-faithful (the #722 R-10 lesson) ---------
def test_tree_all_pass_is_counting_arrow():
    assert _verdict(_base_crit()) == "COUNTING-ARROW"


@pytest.mark.parametrize("flip", ["cons_ok", "nan_seen"])
def test_tree_ledger_first(flip):
    """Precedence 1: a broken ledger (bin ii) precedes ALL physics."""
    c = _base_crit()
    c[flip] = (not c[flip])
    # also break a downstream gate to prove ledger wins the precedence
    c["t63_gate_ok"] = False
    assert _verdict(c) == "NUMERICAL/DETONATE"


@pytest.mark.parametrize("gate", ["t63_gate_ok", "nocc_gate_ok", "transfer_ok"])
def test_tree_regime_gate_before_any_physics_bin(gate):
    """Precedence 2 (the #722 lesson): a failed regime gate ⇒ REGIME-NOT-REACHED
    (question unasked), checked BEFORE any physics bin — even when a physics gate
    would otherwise fire a bin."""
    c = _base_crit()
    c[gate] = False
    c["grid_return_ok"] = False   # would fire FOREIGN-EATER if reached — regime wins
    c["collapse_ok"] = False
    assert _verdict(c) == "REGIME-NOT-REACHED"


def test_tree_foreign_eater_grid_wide_step3():
    """Precedence 3: grid-wide return failure ⇒ FOREIGN-EATER (faithful, not narrowed)."""
    c = _base_crit()
    c["grid_return_ok"] = False
    assert _verdict(c) == "FOREIGN-EATER"


def test_tree_no_arrow_step4():
    """Precedence 4: echo home before the recurrence ⇒ NO-ARROW."""
    c = _base_crit()
    c["dense_pins_low"] = False
    assert _verdict(c) == "NO-ARROW"


@pytest.mark.parametrize("gate", ["collapse_ok", "transition_ok", "controls_ok",
                                  "off_ok", "mode_count_ok", "bias_ok", "det_gated"])
def test_tree_residual_is_foreign_eater_step6(gate):
    """Precedence 6: regime reached + grid returns + dense pins low, but a COUNTING
    conjunct fails ⇒ FOREIGN-EATER (returns present but NOT tracking x — #722 signature)."""
    c = _base_crit()
    c[gate] = False
    assert _verdict(c) == "FOREIGN-EATER"


# --- opt-in engine cells: reproduce the reval bank + the frozen verdict --------
@pytest.mark.engine_sim
def test_sparsest_and_two_tank_reproduce_reval_x4():
    """The sparsest comb + two-tank controls reproduce the #724 reval-banked X4
    numbers (0.890 / 0.989) — independent evidence the sweep plant matches the
    certified κ=0.030 MILD configuration; and conservation holds (#721 R-1)."""
    sparsest = sweep.run_comb(0.080)
    assert sparsest.peak_frac == pytest.approx(0.169, abs=2e-3)   # reval X4 sparse_peakfrac
    assert sparsest.r_cum_table[10.0] == pytest.approx(0.890, abs=5e-3)  # reval X4 sparse R_cum
    assert sparsest.max_cons_drift < sweep.CONS_TOL
    two_tank = sweep.run_comb(sweep.TWO_TANK_DW, horizon_recurrences=sweep.TWO_TANK_RECURRENCES,
                              omega_min=sweep.TWO_TANK_OMEGA_MIN, m=sweep.TWO_TANK_M)
    assert two_tank.r_cum_table[10.0] == pytest.approx(0.989, abs=5e-3)  # reval X4 two-tank


@pytest.mark.engine_sim
def test_full_sweep_is_foreign_eater_self_check_green():
    """The full frozen grid returns FOREIGN-EATER with the byte-faithful classifier
    cross-check green (self_check.match), the regime gate PASSING (question asked),
    and the collapse decisively absent."""
    out = sweep.run_sweep()
    check = sweep.self_check(out)
    assert check["match"] is True
    assert out["verdict"] == "FOREIGN-EATER"
    c = out["criteria"]
    # regime gate PASSED — the question was genuinely asked (unlike #722)
    assert c["t63_gate_ok"] and c["nocc_gate_ok"] and c["transfer_ok"]
    # the SUFFICIENT collapse is decisively absent
    assert not c["collapse_ok"]
    assert c["collapse_spread"] > sweep.COLLAPSE_SPREAD_MAX
    # ledger intact + resonance-gated (live coupling, not a blow-up / broadband dump)
    assert c["cons_ok"] and c["det_gated"]
