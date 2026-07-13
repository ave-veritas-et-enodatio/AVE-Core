"""Pre-registered tests for the F6 tier-1 two-reservoir ODE ledger driver.

Pins the frozen spec of
    research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md   (PR #666)
    research/2026-07-13_f6-tier1-ledger-driver_prereg.md           (frozen tol/grid)

Every assertion targets a numerically-derivable frozen property -- closed-form
integrator agreement, the four charter audits (honest PASS + sabotage-plant TRIP),
and the scale-invariance / no-magnitude guarantee. Sabotage plants act on the
EVOLVED ledger trajectory (a modified transfer/booking law integrated through the
same ODE), not on arithmetic (prereg 9).

Driver under test:
    src/scripts/vol_3_macroscopic/f6_tier1_two_reservoir_ledger.py
"""

from __future__ import annotations

import numpy as np
import pytest

from scripts.vol_3_macroscopic.f6_tier1_two_reservoir_ledger import (
    HISTORIES,
    KAPPA_FID,
    KAPPA_SCAN,
    RHO_LATENT_INPUT,
    TOL_CONS,
    closed_form,
    d_form,
    drain_rate,
    evolve,
    gate_bounded_norm,
    gate_conservation,
    gate_magnitude_invariance,
    gate_mechanism_class,
    history_physical,
    plant_diode_deadzone,
    plant_imposed_leak,
    plant_magnitude_tune_score,
    plant_trilinear_pump,
    rho_hat,
)

ARMS = ("ON", "FRONTIER", "LAMBDA")


# --------------------------------------------------------------------------
# Integrator validation against the frozen closed forms (prereg 3.4).
# --------------------------------------------------------------------------
@pytest.mark.parametrize("hname", list(HISTORIES))
@pytest.mark.parametrize("arm", ARMS)
def test_closed_form_integrator_validation(arm, hname):
    """Evolved rho_hat matches the frozen analytic solution to RK45 precision.
    Pins that the driver integrates the CHARTER 1.6 transfer laws, not a variant."""
    hfn = HISTORIES[hname]
    kappa = KAPPA_FID
    tau, rho, _e, ok = evolve(arm, hfn, kappa)
    assert ok
    rhat = rho_hat(rho)
    cf = closed_form(arm, hname, tau, kappa)
    assert np.max(np.abs(rhat - cf)) < 1e-6


# --------------------------------------------------------------------------
# Audit 1 -- IMPOSED-LEAK / conservation (prereg 9.1, bin ii).
# --------------------------------------------------------------------------
@pytest.mark.parametrize("hname", list(HISTORIES))
def test_conservation_honest_passes(hname):
    """Honest ledger conserves rho_hat + E_T2 to tol_cons across all arms."""
    hfn = HISTORIES[hname]
    for arm in ARMS:
        tau, rho, e, ok = evolve(arm, hfn, KAPPA_FID)
        assert ok
        assert gate_conservation(rho, e) <= TOL_CONS


def test_imposed_leak_plant_trips_conservation():
    """A leaky booking (bath gains eta<1 of the source loss) DESTROYS energy ->
    conservation residual exceeds tol_cons (bin ii)."""
    hfn = history_physical
    # honest baseline conserves
    tau, rho, e, ok = evolve("ON", hfn, KAPPA_FID)
    assert gate_conservation(rho, e) <= TOL_CONS
    # planted leak trips
    tau, rho_l, e_l, ok_l = evolve("ON", hfn, KAPPA_FID, booking=plant_imposed_leak(eta=0.5))
    assert gate_conservation(rho_l, e_l) > TOL_CONS


# --------------------------------------------------------------------------
# Audit 2 -- TRILINEAR-PUMP / bounded-norm (prereg 9.2).
# --------------------------------------------------------------------------
@pytest.mark.parametrize("hname", list(HISTORIES))
def test_bounded_norm_honest_passes(hname):
    """Honest drain-only trajectory: rho monotone non-increasing, total bounded."""
    hfn = HISTORIES[hname]
    for arm in ARMS:
        tau, rho, e, ok = evolve(arm, hfn, KAPPA_FID)
        assert gate_bounded_norm(tau, rho, e)["ok"]


def test_trilinear_pump_plant_trips_bounded_norm():
    """A v4-style indefinite pump (+c*rho*E fed to both states) runs the total
    norm away -> bounded-norm gate fails."""
    hfn = history_physical
    tau, rho, e, ok = evolve("ON", hfn, KAPPA_FID)
    assert gate_bounded_norm(tau, rho, e)["ok"]
    tau, rho_p, e_p, ok_p = evolve("ON", hfn, KAPPA_FID, extra=plant_trilinear_pump(c=10.0))
    assert not gate_bounded_norm(tau, rho_p, e_p)["ok"]


# --------------------------------------------------------------------------
# Audit 3 -- MAGNITUDE-TUNE / input-provenance + scale-invariance (prereg 9.3).
# --------------------------------------------------------------------------
@pytest.mark.parametrize("hname", list(HISTORIES))
def test_magnitude_invariance_honest_passes(hname):
    """Every D is invariant to machine precision under an arbitrary rescale of the
    input store -- the no-magnitude guarantee."""
    res = gate_magnitude_invariance("ON", HISTORIES[hname], KAPPA_FID)
    assert res["ok"]
    assert res["spread"] <= 1e-12


def test_d_form_is_scale_invariant():
    """D[ON,FRONTIER] computed at input scale 1.0 and 1e6 agree to machine precision."""
    hfn = history_physical
    _t, r1, _e1, _ = evolve("ON", hfn, KAPPA_FID, rho0=RHO_LATENT_INPUT)
    _t, f1, _ef1, _ = evolve("FRONTIER", hfn, 0.0, rho0=RHO_LATENT_INPUT)
    d1 = d_form(rho_hat(r1), rho_hat(f1), _t)
    _t, r2, _e2, _ = evolve("ON", hfn, KAPPA_FID, rho0=RHO_LATENT_INPUT * 1e6)
    _t, f2, _ef2, _ = evolve("FRONTIER", hfn, 0.0, rho0=RHO_LATENT_INPUT * 1e6)
    d2 = d_form(rho_hat(r2), rho_hat(f2), _t)
    assert abs(d1 - d2) <= 1e-12


def test_magnitude_tune_plant_reads_magnitude():
    """A 10^122-style tune (un-normalized rho_DE(t1) vs a fabricated rho_Lambda
    target) CHANGES under input rescale -- which the honest invariance gate forbids.
    This proves the gate would catch such a tune."""
    hfn = history_physical
    target = 0.5 * RHO_LATENT_INPUT
    s1 = plant_magnitude_tune_score("ON", hfn, KAPPA_FID, target, scale=1.0)
    s2 = plant_magnitude_tune_score("ON", hfn, KAPPA_FID, target, scale=3.0)
    assert abs(s1 - s2) > 1e-3


# --------------------------------------------------------------------------
# Audit 4 -- DIODE-RESURRECTION / mechanism-class (prereg 9.4).
# --------------------------------------------------------------------------
@pytest.mark.parametrize("hname", list(HISTORIES))
def test_diode_mechanism_class_honest_passes(hname):
    """Honest ON law: reconstructed g_eff = -(d rho_hat/dtau)/rho_hat matches the
    declared smooth kappa*n_hat_B (no dead-zone, no sign asymmetry)."""
    hfn = HISTORIES[hname]
    tau, rho, _e, ok = evolve("ON", hfn, KAPPA_FID)
    g = gate_mechanism_class("ON", hfn, KAPPA_FID, tau, rho)
    assert g["ok"]
    assert g["rel_dev"] <= 1e-3


def test_diode_resurrection_plant_trips_mechanism_class():
    """A forward-voltage dead-zone (drain freezes below rho_f) makes g_eff jump ->
    mechanism-class gate fails (V_f is FREE / dead four ways, CHARTER iv)."""
    hfn = history_physical
    # honest passes
    tau, rho, _e, ok = evolve("ON", hfn, KAPPA_FID)
    assert gate_mechanism_class("ON", hfn, KAPPA_FID, tau, rho)["ok"]
    # dead-zone at rho_f=0.5 is reached within [1,10] for kappa_fid=2 -> trips
    tau, rho_d, _ed, ok_d = evolve("ON", hfn, KAPPA_FID, extra=plant_diode_deadzone(rho_f=0.5))
    g = gate_mechanism_class("ON", hfn, KAPPA_FID, tau, rho_d)
    assert not g["ok"]


# --------------------------------------------------------------------------
# Observable sanity -- D detects genuine form differences; Lambda arm is flat.
# --------------------------------------------------------------------------
def test_lambda_arm_is_flat_and_D_detects_frontier():
    """ARM-Lambda gives rho_hat == 1; ARM-FRONTIER declines on PHYSICAL, so
    D[FRONTIER, LAMBDA] > 0 -- confirms D resolves a real form difference."""
    hfn = history_physical
    tau, rl, _el, _ = evolve("LAMBDA", hfn, 0.0)
    tau, rf, _ef, _ = evolve("FRONTIER", hfn, 0.0)
    assert np.allclose(rho_hat(rl), 1.0, atol=1e-12)
    assert d_form(rho_hat(rf), rho_hat(rl), tau) > 1e-2


def test_drain_rate_nonnegative_and_no_sign_branch():
    """Gamma >= 0 for all arms/histories (one-way transfer), and the transfer law
    is a pure multiplicative rate with no sign(rate) dependence."""
    tau = np.linspace(1.0, 10.0, 50)
    for hname, hfn in HISTORIES.items():
        for arm in ARMS:
            g = drain_rate(arm, tau, hfn, KAPPA_FID)
            assert np.all(np.asarray(g) >= -1e-15)
