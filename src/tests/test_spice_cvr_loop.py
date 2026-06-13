"""
SPICE-CVR constitutive-loop keeper tests.

Prereg: research/2026-06-13_spice-cvr-constitutive-loop_prereg.md
Harness: ave.solvers.spice_cvr_loop (Python ODE ladder; ngspice uses scaled TAU).
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.constants import TAU_RELAX_SI
from ave.solvers.spice_cvr_loop import (
    EPS_BR,
    EPS_LOOP,
    OMEGA_TAU_GRID,
    analytic_l1_loop_area_small_omega,
    branch_hysteresis_area,
    run_ladder_battery,
    s_eq,
    simulate_arm,
)


class TestSaturationKernel:
    def test_s_eq_at_origin(self) -> None:
        assert s_eq(0.0) == pytest.approx(1.0)

    def test_tau_relax_si_canonical(self) -> None:
        assert TAU_RELAX_SI == pytest.approx(1.288e-21, rel=1e-2)


class TestL0Baseline:
    def test_l0_zero_loop_and_br(self) -> None:
        _, _, m = simulate_arm("L0", omega_tau=0.5)
        assert m.loop_area < EPS_LOOP
        assert m.b_r < EPS_BR


class TestL1Memristor:
    def test_l1_area_grows_with_drive_rate(self) -> None:
        areas = [simulate_arm("L1", omega_tau=w)[2].loop_area for w in OMEGA_TAU_GRID]
        assert areas[-2] > areas[0] + EPS_LOOP
        assert max(areas) >= EPS_LOOP

    def test_l1_pinched_at_slow_rate(self) -> None:
        _, _, m = simulate_arm("L1", omega_tau=OMEGA_TAU_GRID[0])
        assert m.b_r < EPS_BR

    def test_l1_planted_area_order_of_magnitude(self) -> None:
        omega = 0.5
        _, _, m = simulate_arm("L1", omega_tau=omega)
        analytic = analytic_l1_loop_area_small_omega(omega)
        assert m.loop_area >= analytic * 0.5


class TestL2Snap:
    def test_l2_imposed_clamp_produces_br(self) -> None:
        """Imposed min(S,S_latched) ratchet — auditor: tautology, not emergence."""
        _, _, m = simulate_arm("L2", omega_tau=0.7)
        assert m.b_r >= EPS_BR


class TestFrozenBattery:
    def test_physics_bin_dissipative_only(self) -> None:
        r = run_ladder_battery()
        assert r["verdict"] == "DISSIPATIVE-ONLY"
        assert "IMPOSED-LATCH" in r["l2_emergence_read"]
        assert r["frozen_gates"]["H0_L0_area_zero"]
        assert r["frozen_gates"]["H0_L0_br_zero"]
        assert r["frozen_gates"]["H1_L1_area_monotone"]
        assert r["frozen_gates"]["bin_DISSIPATIVE_ONLY"]
        assert not r["frozen_gates"]["bin_REMANENT_LOOP"]
        assert r["l2_max_br_omega_tau"] == pytest.approx(0.7, rel=1e-6)
        assert r["l2_max_br"] == pytest.approx(0.2877418292124396, rel=1e-4)

    def test_branch_area_zero_for_single_valued_l0(self) -> None:
        r = np.linspace(0, 0.8, 50)
        s = np.array([s_eq(x) for x in r])
        assert branch_hysteresis_area(r, s) < 1e-9
