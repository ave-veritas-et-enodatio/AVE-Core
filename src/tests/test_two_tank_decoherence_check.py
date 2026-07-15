"""Test for the two-tank decoherence check (registers-walk registered check).

Covers (1) the verdict-class logic at its declared/frozen thresholds — pure
Summary -> class, unit-testable on synthetic records — and (2) that the phase
estimators run and give sane, kernel-consistent numbers on synthetic and tiny-
lattice inputs. No physics constants hard-coded — all from ave.core.constants
via the driver.
"""
import numpy as np
import pytest

from scripts.vol_1_foundations.two_tank_decoherence_check import (
    BOUNDED_HI,
    CLK_AMP,
    CTRL_FLOOR,
    EXCESS_MIN,
    P_LIN_HI,
    P_LIN_LO,
    Summary,
    classify,
    diffusion_constant,
    hilbert_phase,
    loglog_exponent,
    msd_loglog_slope,
    run_once,
)
from ave.core.constants import ALPHA, R_I, V_SNAP, V_YIELD


# ── frozen-parameter provenance ──────────────────────────────────────────────
def test_clock_operating_point_is_sub_yield():
    """The clock operating point A_clk must sit at/below the yield onset
    V_YIELD/V_SNAP = sqrt(alpha) (regime-I/II boundary), imported from constants."""
    assert V_YIELD / V_SNAP == pytest.approx(np.sqrt(ALPHA))
    assert CLK_AMP <= V_YIELD / V_SNAP + 1e-3        # ~0.0854; clock = 0.08
    assert CLK_AMP < R_I                             # below the regime-I boundary


# ── the frozen verdict logic ─────────────────────────────────────────────────
def _base(**kw):
    """A diffusive, kernel-driven, linear-in-u, clean-control record; override
    fields to exercise each branch."""
    d = dict(ctrl_span_on=1e-12, ctrl_span_off=1e-12, shape_on=1.0,
             p_on=1.0, excess_frac=0.9, shape_iso=1.0)
    d.update(kw)
    return Summary(**d)


def test_control_fail_gate_first():
    """A drifting u=0 control trips CONTROL-FAIL regardless of everything else."""
    assert classify(_base(ctrl_span_on=10 * CTRL_FLOOR)) == "CONTROL-FAIL"
    assert classify(_base(ctrl_span_off=10 * CTRL_FLOOR)) == "CONTROL-FAIL"


def test_non_diffusive_bounded_and_ballistic():
    """Bounded (slope<=0.3) and ballistic (slope>=1.7) both FAIL as posed."""
    assert classify(_base(shape_on=BOUNDED_HI - 0.05)) == "NON-DIFFUSIVE"   # bounded
    assert classify(_base(shape_on=0.0)) == "NON-DIFFUSIVE"                 # flat
    assert classify(_base(shape_on=1.9)) == "NON-DIFFUSIVE"                 # ballistic


def test_additive_artifact_mechanism_gate():
    """Diffusive-shaped but kernel-INDEPENDENT (excess < EXCESS_MIN) => the
    diffusion is additive wave-interference, not the Op14 thermal mechanism."""
    assert classify(_base(shape_on=1.0, excess_frac=EXCESS_MIN - 0.1)) == "ADDITIVE-ARTIFACT"
    assert classify(_base(shape_on=1.0, excess_frac=-0.2)) == "ADDITIVE-ARTIFACT"
    # the mechanism gate fires BEFORE the u-scaling verdict:
    assert classify(_base(shape_on=1.0, excess_frac=0.1, p_on=1.0)) == "ADDITIVE-ARTIFACT"


def test_diffusive_linear_is_the_measured_verdict():
    """Diffusive + kernel-driven + linear-in-u => the definition is MEASURED."""
    assert classify(_base(shape_on=1.0, excess_frac=0.9, p_on=1.0)) == "DIFFUSIVE-LINEAR"
    assert classify(_base(p_on=P_LIN_LO + 0.01)) == "DIFFUSIVE-LINEAR"
    assert classify(_base(p_on=P_LIN_HI - 0.01)) == "DIFFUSIVE-LINEAR"


def test_diffusive_nonlinear_when_p_off_unity():
    """Kernel-driven diffusion with p!=1 survives with a nonlinear calibration."""
    assert classify(_base(excess_frac=0.9, p_on=2.0)) == "DIFFUSIVE-NONLINEAR"
    assert classify(_base(excess_frac=0.9, p_on=0.4)) == "DIFFUSIVE-NONLINEAR"


# ── estimator sanity (synthetic) ─────────────────────────────────────────────
def test_msd_slope_diffusive_vs_ballistic_vs_bounded():
    """The anomalous-diffusion exponent recovers 1 (random walk), 2 (ballistic
    drift), ~0 (bounded oscillation) on synthetic phase series."""
    rng = np.random.default_rng(0)
    n = 4000
    walk = np.cumsum(rng.normal(size=n))               # Wiener -> slope ~1
    drift = 0.01 * np.arange(n)                          # linear -> slope ~2
    bounded = np.sin(np.arange(n) * 0.05)               # bounded -> slope ~0
    assert msd_loglog_slope(walk) == pytest.approx(1.0, abs=0.25)
    assert msd_loglog_slope(drift) == pytest.approx(2.0, abs=0.25)
    assert msd_loglog_slope(bounded) < BOUNDED_HI


def test_diffusion_constant_recovers_D():
    """MSD ~ 2 D tau: a Wiener walk with unit step variance gives D ~ 0.5."""
    rng = np.random.default_rng(1)
    walk = np.cumsum(rng.normal(scale=1.0, size=8000))
    assert diffusion_constant(walk) == pytest.approx(0.5, rel=0.35)


def test_loglog_exponent_linear():
    x = np.array([1.0, 3.0, 9.0, 27.0])
    y = 2.5 * x ** 1.0
    assert loglog_exponent(x, y) == pytest.approx(1.0, abs=1e-6)


# ── tiny-lattice integration: the clean-control invariant ────────────────────
def test_control_is_translation_clean_both_kernels():
    """u=0: the two clocks are related by a lattice translation, so Delta-phi is
    flat to machine precision — the instrument's clean-control invariant, for
    BOTH the Op14-ON and pure-linear lattices. Also confirms losslessness."""
    for kon in (True, False):
        rec = run_once(0.0, 0, kon, N=16, n_modes=8, nsteps=400)
        d = hilbert_phase(rec["v1"]) - hilbert_phase(rec["v2"])
        assert (d.max() - d.min()) < 1e-8              # << CTRL_FLOOR (1e-3)
        assert rec["energy_drift"] < 1e-10             # lossless (Ax3)
        assert rec["sep"] >= 8                         # clocks well-separated
