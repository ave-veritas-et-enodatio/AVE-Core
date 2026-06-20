"""Unit + validate-on-known tests for the shared ave.bench package.

Each test class targets one factored module and pins it against its NAMED
exemplar. The load-bearing tests are the validate-on-known regressions: they
drive the factored module with the SAME inputs the exemplar uses internally and
assert the factored module REPRODUCES the exemplar's numeric output. The
factoring is not done until proven faithful.

Exemplars:
  sweep.py     <- AVE-Bench-VacuumMirror/scripts/analytical_gamma_v_sweep.py
  apparatus.py <- AVE-Core src/scripts/vol_4_engineering/qg42_vsign_deltaf.py
  snr.py       <- AVE-Bench-VacuumMirror/scripts/apd_snr_sweep.py
  validate.py  <- AVE-Core src/scripts/verify/*_anchor.py (muon_g2_fermilab)
"""

from __future__ import annotations

from functools import partial

import numpy as np
import pytest

import ave.bench as bench
from ave.core.constants import EPSILON_0, L_NODE, V_YIELD

# ============================================================================
# VERBATIM exemplar reference functions for the validate-on-known regressions.
#
# These are copied verbatim from
#   AVE-Bench-VacuumMirror/scripts/analytical_gamma_v_sweep.py:29-119
# so the regression is self-contained / CI-portable (the test must not depend
# on a sibling repo being on sys.path). They reproduce the exemplar's Born
# engine (AVE) and EH+Kerr null (SM) sharing the IDENTICAL z-grid, K0, and
# e^(2ik0z) profile — the no-strawman invariant. The cross-repo live import was
# verified to reproduce these bit-for-bit at factoring time (max abs delta 0.0).
# ============================================================================
_LAMBDA_OPTICAL = 500e-9
_K0 = 2 * np.pi / _LAMBDA_OPTICAL


def _strain_profile_single(z, V_gap, R_tip, d_gap):  # exemplar :36-42
    half = d_gap / 2.0
    r1 = np.sqrt(half**2 + z**2)
    Q = 4 * np.pi * EPSILON_0 * R_tip * (V_gap / 2.0)
    E = 2 * Q * half / (4 * np.pi * EPSILON_0 * r1**3)
    return np.abs(E) * L_NODE / V_YIELD


def _delta_eps_single(z, V_gap, R_tip, d_gap):  # exemplar :45-49
    A = _strain_profile_single(z, V_gap, R_tip, d_gap)
    A = np.clip(A, 0, 0.99999)
    return np.sqrt(1 - A**2) - 1


def _gamma_single_tip(V_gap, R_tip, d_gap, n_pts=20000):  # exemplar :52-59
    z_span = 5 * d_gap
    z = np.linspace(-z_span, z_span, n_pts)
    dz = z[1] - z[0]
    deps = _delta_eps_single(z, V_gap, R_tip, d_gap)
    r = -(_K0 / 2.0) * np.sum(deps * np.exp(2j * _K0 * z)) * dz
    return float(np.abs(r) ** 2)


def _gamma_bragg_2d(V_gap, R_tip, d_gap, N_total):  # exemplar :62-69 (AVE)
    r_single = np.sqrt(_gamma_single_tip(V_gap, R_tip, d_gap))
    return (r_single * N_total) ** 2


def _delta_eps_sm(z, V_gap, R_tip, d_gap):  # exemplar :83-97
    from ave.core.constants import ALPHA
    from ave.core.constants import E_CRIT as E_SCHWINGER

    half = d_gap / 2.0
    r1 = np.sqrt(half**2 + z**2)
    Q = 4 * np.pi * EPSILON_0 * R_tip * (V_gap / 2.0)
    E = np.abs(2 * Q * half / (4 * np.pi * EPSILON_0 * r1**3))
    coeff = (4 * ALPHA**2) / 9.0
    return coeff * (E / E_SCHWINGER) ** 2


def _gamma_sm_single_tip(V_gap, R_tip, d_gap, n_pts=20000):  # exemplar :100-107
    z_span = 5 * d_gap
    z = np.linspace(-z_span, z_span, n_pts)
    dz = z[1] - z[0]
    deps = _delta_eps_sm(z, V_gap, R_tip, d_gap)
    r = -(_K0 / 2.0) * np.sum(deps * np.exp(2j * _K0 * z)) * dz
    return float(np.abs(r) ** 2)


def _gamma_sm_eh_kerr(V_gap, R_tip, d_gap, N_total):  # exemplar :110-119 (SM)
    r_single = np.sqrt(_gamma_sm_single_tip(V_gap, R_tip, d_gap))
    return (r_single * N_total) ** 2


class TestPackageSkeleton:
    """Commit-1 skeleton smoke: the package imports and exposes its contract."""

    def test_public_api_present(self):
        for name in [
            "run_divergence_sweep",
            "DivergenceSweepResult",
            "ApparatusCoupling",
            "saturation_amplitude",
            "v_yield_apparatus",
            "fn_dark_current",
            "fn_safe_max_amplitude",
            "snr_shot_noise",
            "time_to_n_sigma",
            "signal_vs_floor",
            "SNRPoint",
            "assert_recovers_known",
            "KnownComparison",
        ]:
            assert hasattr(bench, name), f"ave.bench missing public symbol {name}"

    def test_modules_importable(self):
        from ave.bench import apparatus, snr, sweep, validate  # noqa: F401

        assert callable(sweep.run_divergence_sweep)
        assert callable(apparatus.saturation_amplitude)
        assert callable(snr.snr_shot_noise)
        assert callable(validate.assert_recovers_known)


class TestSweep:
    """sweep.run_divergence_sweep <- analytical_gamma_v_sweep.py (gamma co-vary)."""

    # The exemplar's run_sweep geometry (analytical_gamma_v_sweep.py:126-131).
    R_TIP = 10e-9
    D_GAP = 10e-9
    N_RECOMMENDED = 10_000

    def _grid(self):
        # The exemplar's V_gap_array (analytical_gamma_v_sweep.py:131).
        return np.linspace(0.01 * V_YIELD, V_YIELD, 200)

    def test_validate_on_known_reproduces_exemplar(self):
        """VALIDATE-ON-KNOWN: factored sweep == exemplar's run_sweep output.

        Drives run_divergence_sweep with the SAME ave_fn/sm_fn/grid that
        analytical_gamma_v_sweep.run_sweep uses internally and asserts the
        factored module reproduces the exemplar's ave / sm / discrimination
        arrays. Live cross-repo import confirmed bit-for-bit (delta 0.0) at
        factoring time; this self-contained copy asserts the same.
        """
        V = self._grid()
        # Exemplar's own internal arrays (run_sweep :134-148).
        g_ave = np.array([_gamma_bragg_2d(v, self.R_TIP, self.D_GAP, self.N_RECOMMENDED) for v in V])
        g_sm = np.array([_gamma_sm_eh_kerr(v, self.R_TIP, self.D_GAP, self.N_RECOMMENDED) for v in V])
        discrim_ex = g_ave / np.maximum(g_sm, 1e-40)

        # Factored module driven with the SAME callables over the SAME grid.
        ave_fn = partial(_gamma_bragg_2d, R_tip=self.R_TIP, d_gap=self.D_GAP, N_total=self.N_RECOMMENDED)
        sm_fn = partial(_gamma_sm_eh_kerr, R_tip=self.R_TIP, d_gap=self.D_GAP, N_total=self.N_RECOMMENDED)
        res = bench.run_divergence_sweep(ave_fn, sm_fn, V)

        np.testing.assert_allclose(res.ave, g_ave, rtol=0, atol=0)
        np.testing.assert_allclose(res.sm, g_sm, rtol=0, atol=0)
        np.testing.assert_allclose(res.ratio, discrim_ex, rtol=0, atol=0)

    def test_discrimination_ratio_matches_canonical_v4(self):
        """Peak divergence ~ 8.38e12 (the qg42 V^4 discrimination ratio, qg42 :190)."""
        V = self._grid()
        ave_fn = partial(_gamma_bragg_2d, R_tip=self.R_TIP, d_gap=self.D_GAP, N_total=self.N_RECOMMENDED)
        sm_fn = partial(_gamma_sm_eh_kerr, R_tip=self.R_TIP, d_gap=self.D_GAP, N_total=self.N_RECOMMENDED)
        res = bench.run_divergence_sweep(ave_fn, sm_fn, V)
        # qg42 :190 expects Gamma ratio (V^4) = 8.381e12.
        assert res.max_divergence == pytest.approx(8.381e12, rel=1e-3)

    def test_result_dict_contract(self):
        """as_dict returns exactly {x, ave, sm, ratio}; ratio == ave / max(sm, floor)."""
        x = np.array([1.0, 2.0, 3.0])
        res = bench.run_divergence_sweep(lambda v: v**2, lambda v: v, x)
        d = res.as_dict()
        assert set(d.keys()) == {"x", "ave", "sm", "ratio"}
        np.testing.assert_allclose(d["ave"], [1.0, 4.0, 9.0])
        np.testing.assert_allclose(d["sm"], [1.0, 2.0, 3.0])
        np.testing.assert_allclose(d["ratio"], [1.0, 2.0, 3.0])

    def test_no_strawman_same_grid_both_callables(self):
        """No-strawman R1: sm_fn is driven over THE SAME grid as ave_fn.

        The signature only accepts callables — there is no array path. A
        spy records the x's each callable was evaluated at; both must be the
        identical grid (the contract that forbids a pre-baked independent SM
        curve on a different grid).
        """
        x = np.linspace(0.0, 5.0, 7)
        ave_seen, sm_seen = [], []

        def ave_fn(v):
            ave_seen.append(v)
            return v + 1.0

        def sm_fn(v):
            sm_seen.append(v)
            return v + 1.0

        bench.run_divergence_sweep(ave_fn, sm_fn, x)
        np.testing.assert_array_equal(np.array(ave_seen), x)
        np.testing.assert_array_equal(np.array(sm_seen), x)
        # And both were evaluated at the EXACT same points.
        np.testing.assert_array_equal(np.array(ave_seen), np.array(sm_seen))

    def test_ratio_floor_guards_zero_null(self):
        """A zero SM null does not produce inf/NaN (the np.maximum guard)."""
        x = np.array([1.0, 2.0])
        res = bench.run_divergence_sweep(lambda v: 1.0, lambda v: 0.0, x, ratio_floor=1e-40)
        assert np.all(np.isfinite(res.ratio))
        assert np.all(res.ratio == 1e40)

    def test_rejects_2d_grid(self):
        with pytest.raises(ValueError):
            bench.run_divergence_sweep(lambda v: v, lambda v: v, np.zeros((2, 2)))

    def test_rejects_empty_grid(self):
        with pytest.raises(ValueError):
            bench.run_divergence_sweep(lambda v: v, lambda v: v, np.array([]))
