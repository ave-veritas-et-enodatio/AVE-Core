"""Tests for the pump-probe T-slot adjudication.

Locks: (1) the FROZEN prediction module (the freeze proof — arms pinned before the
dynamics run); (2) the honest-dynamics measurement (COLD=1, DC-liveness sees the
tension, SWR≈1, dt-converged); (3) the #528 ReconcileGate + bin selector (can-fire
proven on dropped-term / sign-flip synthetics; no fall-through; HALT reachable).

The #531 tautology guard is enforced structurally: the dynamics module
(`pump_probe_chain`) does NOT import the prediction module (`pump_probe_predictions`);
test_tautology_guard_no_cross_import asserts it.
"""
from __future__ import annotations

import pytest

from ave.validation.reconcile_gate import DiscrepantHalt, ReconcileGate
from scripts.vol_1_foundations import pump_probe_chain as dyn
from scripts.vol_1_foundations import pump_probe_predictions as pred


# ── FROZEN prediction module: symbolic backbone (5 exact-zero residuals) ──────
def test_symbolic_backbone_all_exact_zero():
    for name, val in pred.symbolic_backbone().items():
        assert val == 0, f"{name} must be exactly 0, got {val}"


# ── FROZEN prediction numbers (the arms, pinned before the dynamics) ──────────
def test_cold_prediction_is_ks():
    assert pred.k_trans_cold() == pytest.approx(1.0, abs=1e-15)


def test_dc_liveness_prediction_tent_edge():
    assert pred.k_trans_dc_liveness(pred.Y0_TENT) == pytest.approx(1.0376370905760846, rel=1e-12)
    assert pred.k_trans_dc_liveness(pred.Y0_TENT) > pred.k_trans_cold()


def test_pump_arms_tent_edge():
    assert pred.k_trans_pump_dc_only() == pytest.approx(1.0, abs=1e-15)
    assert pred.k_trans_pump_extended(pred.Y0_TENT) == pytest.approx(1.02039184, rel=1e-12)


def test_arm_separation_tent_edge_is_2pct_and_knife_clean():
    sep = pred.arm_separation(pred.Y0_TENT)
    assert sep == pytest.approx(0.02039184, rel=1e-9)
    assert sep == pytest.approx(pred.Y0_TENT**2, rel=1e-12)  # a derived geometric factor
    for target in (0.5, 0.25, 2 / 7, 9.7734):
        assert abs(sep - target) > 0.1, f"separation must NOT land on canon target {target}"


def test_held_bow_is_twice_pump_second_order():
    y = 0.05
    L, A_bond = pred.held_bow_geometry(y)
    held = float(pred.bond_tension(A_bond)) / L   # the geometric tension term T/L
    pump = pred.arm_separation(y)                 # the pump's rectified mean (k_a/ℓ)y²
    assert held == pytest.approx(2.0 * pump, rel=2e-2)


# ── the #531 tautology guard: dynamics must NOT import the prediction module ──
def test_tautology_guard_no_cross_import():
    import inspect
    src = inspect.getsource(dyn)
    # the ONLY place the prediction module may be IMPORTED is inside adjudicate() (the
    # comparator), NEVER in the force/dynamics path. Assert no import statement for it
    # appears before def adjudicate (docstring mentions by name are fine — we grep the
    # actual `import` token, not any textual mention).
    top = src.split("def adjudicate")[0]
    import_lines = [ln for ln in top.splitlines()
                    if "import" in ln and "pump_probe_predictions" in ln]
    assert not import_lines, (
        "TAUTOLOGY GUARD VIOLATION: the dynamics/force path IMPORTS the prediction "
        f"module: {import_lines}. The measurement must not consume the slot formulas "
        "it adjudicates.")
    # and confirm the comparator DOES import it (so the guard is meaningful, not vacuous)
    assert "from scripts.vol_1_foundations import pump_probe_predictions" in src


# ── honest dynamics: the load-bearing measurements ───────────────────────────
# The full-chain integration runs (~5s each) are marked engine_sim (T2 driver
# cost+role, CI-partition convention conftest.py:§engine_sim); routed to the opt-in
# `make test-engine` lane. The fast prediction / gate-plumbing / synthetic-HALT
# tests above and below STAY in the gating lane.
@pytest.fixture(scope="module")
def run_A():
    return dyn.run_three_states(shear_saturates=True)


@pytest.fixture(scope="module")
def run_B():
    return dyn.run_three_states(shear_saturates=False)


@pytest.mark.engine_sim
def test_cold_recovers_ks_from_dynamics(run_A):
    assert run_A["cold"]["k_trans"] == pytest.approx(1.0, abs=1e-12)


@pytest.mark.engine_sim
def test_dc_liveness_probe_sees_held_tension(run_A):
    # the uniform-stretch control MUST reproduce the merged #526 form k_s + T/L,
    # and MUST exceed cold by well over the derived band — the instrument is LIVE.
    s = run_A["dc_bias_stretch"]
    assert s["k_trans"] == pytest.approx(s["merged_526_form"], rel=1e-4)
    assert s["k_trans"] - 1.0 > 10 * dyn.DERIVED_BAND, "probe must see a large tension excess"


@pytest.mark.engine_sim
def test_swr_near_one_in_measurement_window(run_A, run_B):
    assert run_A["pump"]["swr"] == pytest.approx(1.0, abs=0.05), "pump must be genuinely traveling"
    assert run_B["pump"]["swr"] == pytest.approx(1.0, abs=0.05)


@pytest.mark.engine_sim
def test_energy_drift_bounded(run_A):
    assert run_A["energy_drift_undriven"] < 1e-3, "symplectic drift must be bounded"


@pytest.mark.engine_sim
def test_pump_excludes_dc_only_both_keyings(run_A, run_B):
    # the robust, keying-INDEPENDENT finding: the traveling wave moves the stiffness UP
    # (excludes DC_ONLY = 1.000 by more than the derived band on BOTH keyings).
    for run in (run_A, run_B):
        assert run["pump"]["k_trans"] - 1.0 > dyn.DERIVED_BAND


@pytest.mark.engine_sim
def test_dt_convergence():
    base = dyn.run_three_states(shear_saturates=True)["pump"]["k_trans"]
    fine = dyn.run_three_states(shear_saturates=True, dt=0.0025)["pump"]["k_trans"]
    assert abs(fine - base) < 1e-4, "measurement must be dt-converged"


# ── the bin selector + #528 ReconcileGate ────────────────────────────────────
@pytest.mark.engine_sim
def test_bin_selector_keying_A_is_NEITHER():
    binv, _, gate = dyn.adjudicate(shear_saturates=True)
    assert binv == "NEITHER"
    assert gate["excludes_dc_only"] is True


@pytest.mark.engine_sim
def test_bin_selector_keying_B_is_EXTENDED():
    binv, _, gate = dyn.adjudicate(shear_saturates=False)
    assert binv == "EXTENDED-CONFIRMED"
    assert gate["excludes_dc_only"] is True


def test_reconcile_gate_can_fire_on_dropped_term():
    # dropped-term synthetic: claim = cold (dropped the tension term) vs the true
    # merged form → the gate MUST fire (DiscrepantHalt).
    with pytest.raises(DiscrepantHalt):
        ReconcileGate(label="dropped_term", claimed=1.0, independent=1.0786, rtol=1e-4).enforce()


def test_reconcile_gate_can_fire_on_sign_flip():
    # sign-flip synthetic: claim = 1 − excess (compression, wrong sign) vs the true
    # 1 + excess (tension) → the gate MUST fire.
    with pytest.raises(DiscrepantHalt):
        ReconcileGate(label="sign_flip", claimed=1.0 - 0.0786, independent=1.0786, rtol=1e-4).enforce()


@pytest.mark.engine_sim
def test_bin_selector_halts_on_broken_cold(monkeypatch):
    # inject a COLD that isn't 1 → the structural HALT must fire before any verdict.
    orig = dyn.run_three_states

    def broken(**kw):
        r = orig(**kw)
        r["cold"]["k_trans"] = 1.5
        return r

    monkeypatch.setattr(dyn, "run_three_states", broken)
    with pytest.raises(dyn.DiscrepantHaltBin):
        dyn.adjudicate(shear_saturates=True)


@pytest.mark.engine_sim
def test_bin_selector_halts_on_blind_instrument(monkeypatch):
    # inject a DC-bias liveness that does NOT exceed cold → instrument blind → HALT.
    orig = dyn.run_three_states

    def blind(**kw):
        r = orig(**kw)
        r["dc_bias_stretch"]["k_trans"] = 1.0 + 0.5 * dyn.DERIVED_BAND  # below the band
        return r

    monkeypatch.setattr(dyn, "run_three_states", blind)
    with pytest.raises(dyn.DiscrepantHaltBin):
        dyn.adjudicate(shear_saturates=True)


def test_derived_band_below_arm_separation():
    # the #531 discipline: the band must be strictly below the 2.04% arm separation
    # (else the arms are unresolvable and the verdict is vacuous).
    assert dyn.DERIVED_BAND < pred.arm_separation(pred.Y0_TENT)
