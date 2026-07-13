"""Tests for the T1 atom-Q cascade gate.

Discipline (x42 P11): a gate that cannot FIRE is a checklist. The load-bearing tests here are the
FIREABILITY proofs -- that the SAME instrument returns a finite in-window Q on a finite barrier
(so the atom's Q_wall->inf is a PHYSICS verdict, not an instrument that cannot fire bin (i)), and
that the adjudicator REACHES bin (i) on a synthetic finite value. Only then is the bin-(ii) kill
a demonstration rather than a foregone conclusion.
"""

import math

import numpy as np
import pytest

from ave.core.constants import A_0, ALPHA
from scripts.vol_2_subatomic.t1_atom_q_cascade_gate import (
    BIN_I_HI,
    BIN_I_LO,
    BIN_II_HI,
    adjudicate,
    gamow_Q,
    positive_control_Q,
    radiative_diagnostic_Q,
    run_gate,
    wall_leakage_Q,
)

# --------------------------------------------------------------------------------------------
# LEG A -- the atom's wall-Q collapses onto the intrinsic endpoint (bin (ii))
# --------------------------------------------------------------------------------------------


@pytest.mark.parametrize("Z,n", [(1, 1), (1, 2), (2, 1)])
def test_wall_Q_diverges_to_intrinsic_endpoint(Z, n):
    """Leg A: I(R) grows without bound and Q_wall crosses the bin-(ii) endpoint threshold."""
    d = wall_leakage_Q(Z=Z, n=n)
    Is = [row["I"] for row in d["rows"]]
    assert d["diverges"] is True
    assert Is == sorted(Is) and Is[-1] > 5 * Is[0]  # monotone, unbounded growth (no plateau)
    assert d["Q_verdict"] >= BIN_II_HI  # >= 1e12 : collapse toward intrinsic Q->inf


def test_wall_Q_slope_is_the_hydrogenic_decay_constant():
    """dI/dR -> kappa_inf = 1/(n a0) (the known hydrogenic evanescent tail) -- the divergence is
    the real asymptotic decay, not a grid artifact."""
    for Z, n, expect in [(1, 1, 1.0), (1, 2, 0.5), (2, 1, 2.0)]:
        d = wall_leakage_Q(Z=Z, n=n)
        assert d["dI_dR_a0"] == pytest.approx(expect, rel=0.02)
        assert d["kappa_inf_a0"] == pytest.approx(expect, rel=1e-6)


def test_wall_Q_divergence_is_coupling_independent():
    """Z-independence of the divergence: I(R) at matched R/r_turn is IDENTICAL for H (Z=1) and
    He+ (Z=2). The leakage is a pure geometric property of the sub-threshold bound state, carrying
    NO Z*alpha coupling signature -- the structural proof that Q_wall is alpha-free (not an
    alpha-seeded value)."""
    dH = wall_leakage_Q(Z=1, n=1)
    dHe = wall_leakage_Q(Z=2, n=1)
    for rowH, rowHe in zip(dH["rows"], dHe["rows"]):
        assert rowH["R_over_rturn"] == rowHe["R_over_rturn"]
        assert rowH["I"] == pytest.approx(rowHe["I"], rel=1e-9)  # identical dimensionless leakage


def test_wall_Q_divergence_survives_reduced_mass():
    """Probe-mass invariance: the m_e -> m_r,H reduced-mass correction does not change the
    divergence (the wall stays lossless)."""
    d = run_gate()["legA"]["H_1s_reduced_mass"]
    assert d["diverges"] is True and d["Q_verdict"] >= BIN_II_HI


# --------------------------------------------------------------------------------------------
# FIREABILITY -- the gate can produce bin (i); the kill is therefore a real verdict (x42 P11)
# --------------------------------------------------------------------------------------------


def test_positive_control_fires_bin_i():
    """Leg B: the SAME gamow_Q integrator on a FINITE barrier returns a finite in-window Q.
    THIS is the fireability proof -- without it, Leg A's inf would be an unfireable checklist."""
    b = positive_control_Q()
    assert math.isfinite(b["Q_control"])
    assert BIN_I_LO <= b["Q_control"] <= BIN_I_HI  # a DISTINCT intermediate value IS reportable


def test_gate_discriminates_finite_vs_infinite_barrier():
    """The gate distinguishes a distinct-value case from an endpoint-collapse case, using the
    identical integrator:
      * finite forbidden region  -> finite Q -> adjudicate -> bin (i)
      * infinite forbidden region -> Q=inf   -> adjudicate -> bin (ii)."""
    kappa_sq = (2.0 / A_0) ** 2  # some positive |k|^2

    def finite_neg_k2(r):
        return np.full_like(np.asarray(r, float), kappa_sq)

    _, _, Q_finite = gamow_Q(finite_neg_k2, 0.0, 3.0 * A_0)  # width 3 a0 -> finite
    _, _, Q_infinite = gamow_Q(finite_neg_k2, 0.0, 1e4 * A_0)  # width 1e4 a0 -> underflow -> inf
    assert math.isfinite(Q_finite)
    assert Q_infinite == float("inf")
    assert "(i)" in adjudicate(Q_finite, Q_finite)["bin"]
    assert "(ii)" in adjudicate(Q_infinite, Q_finite)["bin"]


def test_adjudicator_reaches_bin_i_on_synthetic_in_window_value():
    """The adjudicator REACHES bin (i) for a synthetic finite in-window Q_wall -- bin (i) is not
    dead code."""
    assert "(i)" in adjudicate(1e7, 1e6)["bin"]
    assert "(ii)" in adjudicate(float("inf"), 1e6)["bin"]
    assert "(ii)" in adjudicate(1e2, 1e6)["bin"]  # low-endpoint collapse also fires (ii)


# --------------------------------------------------------------------------------------------
# LEG C -- the observed ~1e7 rung is the alpha-echo, and it must NOT flip the verdict
# --------------------------------------------------------------------------------------------


def test_radiative_diagnostic_is_alpha_cubed_echo():
    """Q_rad = 4 alpha^-3 (classical Lyman-alpha); the QM value ~ 9.6 alpha^-3 ~ 2.5e7 = the
    measured rung. Confirms the observed ~1e7 is alpha-SOURCED, not substrate-distinct."""
    c = radiative_diagnostic_Q()
    assert c["Q_rad_times_alpha3"] == pytest.approx(4.0, rel=1e-3)  # Q_rad ∝ alpha^-3
    assert 1e7 <= c["Q_rad_QM_with_f"] <= 5e7  # lands on the observed atom rung
    assert c["alpha_inv_cubed"] == pytest.approx(ALPHA**-3)


def test_radiative_value_does_NOT_flip_the_verdict():
    """RAIL: Q_rad lies in [1e5,1e9], but it is alpha-sourced and NOT a bin-(i) candidate. The
    adjudicator reads ONLY Q_wall; a bin-(i)-magnitude Q_rad must not manufacture a pass."""
    c = radiative_diagnostic_Q()
    assert BIN_I_LO <= c["Q_rad_classical"] <= BIN_I_HI  # it IS in the window...
    # ...yet the verdict on the wall channel stays (ii): adjudicate never consumes Q_rad
    assert "(ii)" in adjudicate(float("inf"), positive_control_Q()["Q_control"])["bin"]


# --------------------------------------------------------------------------------------------
# END-TO-END -- the frozen bins yield bin (ii), instrument fireable
# --------------------------------------------------------------------------------------------


def test_end_to_end_bin_ii_with_fireable_instrument():
    R = run_gate()
    adj = R["adjudication"]
    assert "(ii)" in adj["bin"]  # the kill-shape fires
    assert adj["instrument_fireable"] is True  # ...and it was fireable (Leg B in-window)
    assert R["legC"]["Q_rad_times_alpha3"] == pytest.approx(4.0, rel=1e-3)
