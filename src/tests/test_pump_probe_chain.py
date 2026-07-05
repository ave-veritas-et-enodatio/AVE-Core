"""Tests for the pump-probe T-slot adjudication.

SKELETON: locks the FROZEN prediction module now (the freeze commit); the dynamics
+ gate tests land in the incremental commits. The prediction tests here are the
freeze proof — they pin the arms' numbers BEFORE the dynamics run.
"""
from __future__ import annotations

import numpy as np
import pytest

from scripts.vol_1_foundations import pump_probe_predictions as pred


# ── FROZEN prediction module: the symbolic backbone (5 exact-zero residuals) ──
def test_symbolic_backbone_all_exact_zero():
    resid = pred.symbolic_backbone()
    for name, val in resid.items():
        assert val == 0, f"{name} must be exactly 0, got {val}"


# ── FROZEN prediction numbers (the arms, pinned before the dynamics) ──────────
def test_cold_prediction_is_ks():
    assert pred.k_trans_cold() == pytest.approx(1.0, abs=1e-15)


def test_dc_liveness_prediction_tent_edge():
    # honest held-bow geometry: both terms (constitutive + T/ℓ geometric)
    assert pred.k_trans_dc_liveness(pred.Y0_TENT) == pytest.approx(1.0376370905760846, rel=1e-12)
    # MUST exceed cold — the structural-null stencil guard signal
    assert pred.k_trans_dc_liveness(pred.Y0_TENT) > pred.k_trans_cold()


def test_pump_arms_tent_edge():
    assert pred.k_trans_pump_dc_only() == pytest.approx(1.0, abs=1e-15)
    assert pred.k_trans_pump_extended(pred.Y0_TENT) == pytest.approx(1.02039184, rel=1e-12)


def test_arm_separation_tent_edge_is_2pct():
    sep = pred.arm_separation(pred.Y0_TENT)
    assert sep == pytest.approx(0.02039184, rel=1e-9)
    # knife: 2.04% is (0.1428)^2, a derived geometric factor — NOT 1/2, 1/4, 2/7, 9.7734
    assert sep == pytest.approx(pred.Y0_TENT**2, rel=1e-12)
    for target in (0.5, 0.25, 2 / 7, 9.7734):
        assert abs(sep - target) > 0.1, f"separation must NOT land on canon target {target}"


def test_held_bow_is_twice_pump_second_order():
    # held-bow tension ≈ 2y², pump rectified mean ≈ y² (the ⟨sin²⟩=½ factor)
    y = 0.05  # small-bow limit where the 2nd-order relation is clean
    L, A_bond = pred.held_bow_geometry(y)
    held = float(pred.bond_tension(A_bond)) / L
    pump = pred.arm_separation(y)  # = (k_a/ℓ)y²
    assert held == pytest.approx(2.0 * pump, rel=2e-2)


# ── dynamics + gate tests (SKELETON — land in incremental commits) ────────────
@pytest.mark.skip(reason="skeleton: dynamics land in the dynamics commit")
def test_cold_recovers_ks_from_dynamics():
    ...


@pytest.mark.skip(reason="skeleton: dynamics land in the dynamics commit")
def test_dc_liveness_probe_sees_held_tension():
    ...


@pytest.mark.skip(reason="skeleton: gate lands in the gate commit")
def test_swr_near_one_in_measurement_window():
    ...


@pytest.mark.skip(reason="skeleton: gate lands in the gate commit")
def test_reconcile_gate_can_fire_on_dropped_and_flipped_terms():
    ...


@pytest.mark.skip(reason="skeleton: bin selector lands in the gate commit")
def test_bin_selector_no_fallthrough_and_halt_reachable():
    ...
