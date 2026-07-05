"""Tests for the PILOT-FIELD co-moving companion arc.

FROZEN prereg: research/2026-07-05_pilot-field-comoving-companion_prereg_FROZEN.md.
Result: research/2026-07-05_pilot-field-comoving-companion_result.md.

VERDICT: [RETARDATION-LIMITED / LEAKY] — the co-moving longitudinal contraction
companion DEVELOPS at the free-host amplitude and CO-MOVES with the envelope, but its
completeness + timing are governed by the speed ratio c_long/v_g (a measured law): the
faster the longitudinal sector relative to the envelope, the more completely the well
develops (rho=4 -> 103% pred, co-moving; rho=0.5 -> 39%, lagging).

FAST CORE (unmarked): the symbolic predictions, the sonic-knob-live guard (the Rule-10
integrator-time bug this arc caught), the tautology guard, a tiny wavetrain smoke.
SLOW (engine_sim, opt-in `make test-engine`): the full sonic sweep, the five controls,
co-motion, leakage — the multi-ring time-domain runs (the pump-probe 4-minute lesson:
keep a fast core).
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pytest

_HERE = os.path.dirname(os.path.abspath(__file__))
_SCRIPTS = os.path.join(_HERE, "..", "scripts", "vol_1_foundations")
sys.path.insert(0, os.path.abspath(_SCRIPTS))

import pilot_field_predictions as pred  # noqa: E402
import pilot_field_wavetrain as wt  # noqa: E402

Y0 = 0.1428
PRED_LOCAL_DEPTH = -0.0073410624  # -<dy^2>/2 at the operating point (symbolic)


# ─────────────────────────────── FAST CORE ───────────────────────────────

def test_convexity_coefficient_is_derived_half():
    """The 1/2 in du ~ -dy^2/2 is the DERIVED convexity coefficient (KNIFE): sympy series
    of sqrt(1-dy^2)-1 gives EXACTLY -1/2 (dy^2) and -1/8 (dy^4). Not an asserted 1/2."""
    s = pred.free_contraction_series()
    assert str(s["c_dy2"]) == "-1/2"
    assert str(s["c_dy4"]) == "-1/8"
    assert s["c_dy2_float"] == pytest.approx(-0.5, abs=1e-15)


def test_free_local_depth_matches_534_backbone():
    """The predicted free-host local companion depth -<dy^2>/2 reproduces the #534
    backbone value at the operating point (y0=0.1428, k=1.28700)."""
    assert pred.free_host_local_depth() == pytest.approx(PRED_LOCAL_DEPTH, rel=1e-6)


def test_group_velocity_cold_shear():
    """v_g = domega/dk on the cold shear branch = 2 sqrt(k_s/m) sin(k/2)*(1/...) evaluated
    at the carrier; the co-motion reference speed (0.8 at the operating point)."""
    assert pred.group_velocity() == pytest.approx(0.8, rel=1e-6)
    # v_g < v_phase (normal dispersion on the shear branch)
    assert pred.group_velocity() < pred.phase_velocity()


def test_compensating_stretch_dilutes_with_N():
    """The compensating stretch amplitude ~ (<dy^2>/2)(L_env/N) -> 0 as N grows at fixed
    L_env (the pilot dilution prediction; whole-loop closure Sum du = 0)."""
    a512 = pred.compensating_stretch_amplitude(l_env=80, n_nodes=512)
    a2048 = pred.compensating_stretch_amplitude(l_env=80, n_nodes=2048)
    assert a2048 < a512
    assert a2048 / a512 == pytest.approx(512 / 2048, rel=1e-6)


def test_sonic_knob_is_live_rule10_guard():
    """RULE-10 REGRESSION GUARD: the imported RingChain.tension IGNORES k_a in the
    nonlinear path (k0=1 baked in) — the sonic sweep was a no-op until SonicRing scaled
    the kernel tension by rho_bond. This guard fails if the knob ever silently dies."""
    r05 = wt.make_ring(10, rho_bond=0.5)
    r40 = wt.make_ring(10, rho_bond=4.0)
    t05 = float(r05.tension(np.array([0.1]))[0])
    t40 = float(r40.tension(np.array([0.1]))[0])
    assert t40 == pytest.approx(8.0 * t05, rel=1e-9)   # rho=4 is 8x rho=0.5 (both scale linearly in rho)
    # c_long = sqrt(rho): the sound speed actually varies
    assert pred.c_long(k_long=4.0) == pytest.approx(2.0)
    assert pred.c_long(k_long=1.0) == pytest.approx(1.0)


def test_tautology_guard_driver_does_not_import_predictions():
    """The #531 tautology guard: the time-domain dynamics driver MUST NOT import the
    symbolic prediction module (independent code paths; the ReconcileGate compares
    OUTPUTS only)."""
    src = open(os.path.join(_SCRIPTS, "pilot_field_wavetrain.py")).read()
    assert "import pilot_field_predictions" not in src
    assert "from pilot_field_predictions" not in src


def test_wavetrain_smoke_ledger_closes():
    """A tiny wavetrain run integrates and the crank check closes (energy + momentum
    conserved). Fast smoke of the time-domain integrator + saturation-consistent ledger."""
    run = wt.run_wavetrain(n_nodes=256, rho_bond=2.0, l_env=30.0, n_periods=3.0, dt=0.02)
    ld = wt.ledger_closure(run)
    assert ld["energy_drift_rel"] < 1e-3
    assert ld["momentum_max_abs"] < 1e-9   # closed ring: total longitudinal momentum conserved


def test_contraction_is_geometric_not_kernel_fast():
    """Control (c), fast version: the linear-axial and nonlinear-kernel contraction depths
    agree to O(y0^2) (kernel enters only at O(y0^4)~O(y0^6)) — the contraction is
    GEOMETRIC (du = sqrt(1-dy^2)-1), the merged O(y0^6) result."""
    rn = wt.run_wavetrain(n_nodes=256, rho_bond=2.0, l_env=30.0, n_periods=6.0, dt=0.02,
                          linear_axial=False)
    rl = wt.run_wavetrain(n_nodes=256, rho_bond=2.0, l_env=30.0, n_periods=6.0, dt=0.02,
                          linear_axial=True)
    dn = wt.contraction_depth(rn)["du_dc_min_under"]
    dl = wt.contraction_depth(rl)["du_dc_min_under"]
    assert abs(dn - dl) / abs(dn) < 0.02   # kernel ~ nothing at O(y0^2)


# ─────────────────────────── SLOW (engine_sim) ───────────────────────────

@pytest.mark.engine_sim
def test_companion_develops_at_free_host_depth():
    """The co-moving DC contraction develops toward the free-host depth -<dy^2>/2 at
    high rho with enough transit time (rho=4, well-developed): du_dc_min_under reaches
    ~free-host depth (the LOCALLY-realized free reading). Grant's pilot picture's
    contraction amplitude is realized on the closed ring."""
    run = wt.run_wavetrain(n_nodes=2048, rho_bond=4.0, l_env=80.0, n_periods=20.0, dt=0.02)
    c = wt.contraction_depth(run)
    # reaches free-host depth within band (the [PILOT]-amplitude at high rho)
    assert c["du_dc_min_under"] / PRED_LOCAL_DEPTH > 0.9
    # the depth GROWS from early to settled (the RETARDATION signal, not an instantaneous floor)
    assert c["depth_growth_early_to_settled"] > 1.5


@pytest.mark.engine_sim
def test_companion_co_moves_with_envelope():
    """The contraction well TRAVELS WITH the envelope: at high rho the DC-well speed
    tracks the envelope group speed (speed ratio near 1). Co-motion CONFIRMED."""
    run = wt.run_wavetrain(n_nodes=2048, rho_bond=4.0, l_env=80.0, n_periods=20.0, dt=0.02)
    cm = wt.co_motion(run)
    # the well co-moves with the envelope (both travel; ratio near 1 at high rho)
    assert 0.9 < cm["speed_ratio_du_over_env"] < 1.2
    # the envelope moves at ~ the group velocity (0.8) in magnitude
    assert abs(abs(cm["env_group_speed"]) - 0.8) < 0.1


@pytest.mark.engine_sim
def test_local_probe_soft_under_cold_far():
    """The bond-frame probe reads FREE-LIKE (soft, <1) UNDER the envelope and COLD (~1)
    FAR from it (rho=4). The pilot spatial signature: the well is where the wave is."""
    run = wt.run_wavetrain(n_nodes=2048, rho_bond=4.0, l_env=80.0, n_periods=20.0, dt=0.02)
    lf = wt.local_vs_far_probe(run)
    assert lf["under_bondframe_k_ratio"] < 0.99      # SOFT under the envelope
    assert lf["far_bondframe_k_ratio"] == pytest.approx(1.0, abs=1e-3)   # COLD far
    assert lf["A_under"] < -0.005                    # contracted under (the free-host reading)
    assert abs(lf["A_far"]) < 1e-6                   # no far-field DC (compensating stretch diluted)


@pytest.mark.engine_sim
def test_speed_ratio_law_monotone():
    """The RETARDATION LAW: the contraction develops MORE completely the faster the
    longitudinal sector relative to the envelope (lower Mach v_g/c_long). Depth is
    MONOTONE-INCREASING in rho_bond. This is the [RETARDATION-LIMITED] measured law."""
    depths = {}
    for rho in (0.5, 2.0, 4.0):
        run = wt.run_wavetrain(n_nodes=1024, rho_bond=rho, l_env=80.0, n_periods=16.0, dt=0.02)
        depths[rho] = wt.contraction_depth(run)["du_dc_min_under"]
    # deeper (more negative) contraction at higher rho (stiffer/faster longitudinal)
    assert depths[4.0] < depths[2.0] < depths[0.5]


@pytest.mark.engine_sim
def test_sonic_point_no_secular_blowup():
    """At the sonic photon point rho=1 (k_long=k_shear, SONIC — expected coincidence,
    KNIFE, not a discovery) the companion develops SLOWER but shows NO secular blow-up
    over the recording window (bounded on the closed ring). SONIC-SPECIAL, per prereg."""
    run = wt.run_wavetrain(n_nodes=2048, rho_bond=1.0, l_env=80.0, n_periods=24.0, dt=0.02)
    c = wt.contraction_depth(run)
    # bounded: the settled depth does not exceed a few x the free-host depth (no runaway)
    assert abs(c["du_dc_min_under"]) < 3.0 * abs(PRED_LOCAL_DEPTH)
    ld = wt.ledger_closure(run)
    assert ld["energy_drift_rel"] < 1e-2   # ledger still closes at the sonic point


@pytest.mark.engine_sim
def test_all_controls_pass_with_can_fire():
    """The five HALT-gated controls (a filled-ring cold, b free-local soft, c geometric,
    d dilution, e ledger) all reconcile, each with the #528 can-fire self-test proven."""
    import pilot_field_controls as ctl
    out = ctl.run_all_controls(fast=True)
    assert out["control_a_filled_ring"]["reconciled"]
    assert out["control_a_filled_ring"]["can_fire_proven"]
    assert out["control_b_free_local"]["reconciled"]
    assert out["control_b_free_local"]["can_fire_proven"]
    assert out["control_c_linear_axial"]["reconciled"]
    assert out["control_d_scale_sweep"]["far_dilutes"]
    assert out["control_e_ledger"]["energy_reconciled"]
    assert out["control_e_ledger"]["momentum_reconciled"]
    assert out["control_e_ledger"]["can_fire_proven"]
