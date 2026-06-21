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


class TestApparatus:
    """apparatus.py <- qg42_vsign_deltaf.py (G_geom / a_rms / FN ceiling)."""

    # qg42 PONDER operating point (qg42_vsign_deltaf.py:162-166).
    BETA_TIP = 1.0e3
    Q_BUILD = 1.0e4
    G_GEOM_PONDER = BETA_TIP * Q_BUILD  # 1e7
    V_BENCH = 30.0e3
    D_BENCH = 1.0e-3

    def test_validate_on_known_a_rms_ponder(self):
        """VALIDATE-ON-KNOWN: saturation_amplitude reproduces qg42 a_rms_local.

        qg42 a_rms_local(G_GEOM_PONDER, V_BENCH, D_BENCH) = 2.6539...e-3 at the
        PONDER operating point (qg42 :73-81, :193). Confirmed bit-for-bit
        against the live exemplar at factoring time.
        """
        a = bench.saturation_amplitude(self.G_GEOM_PONDER, self.V_BENCH, self.D_BENCH)
        assert a == pytest.approx(0.002653902994320631, rel=0, abs=0)

    def test_g_geom_decomposition(self):
        """G_geom = beta * Q_build (qg42 :166)."""
        app = bench.ApparatusCoupling(beta=self.BETA_TIP, q_build=self.Q_BUILD, d_gap=self.D_BENCH)
        assert app.g_geom == self.G_GEOM_PONDER
        assert app.saturation_amplitude(self.V_BENCH) == pytest.approx(0.002653902994320631, rel=0, abs=0)

    def test_v_yield_apparatus_inverse(self):
        """v_yield_apparatus drives A exactly to 1.0 (the knee)."""
        vy = bench.v_yield_apparatus(self.G_GEOM_PONDER, self.D_BENCH)
        a_at_vy = bench.saturation_amplitude(self.G_GEOM_PONDER, vy, self.D_BENCH)
        assert a_at_vy == pytest.approx(1.0, rel=1e-12)
        # And via the dataclass.
        app = bench.ApparatusCoupling(beta=self.BETA_TIP, q_build=self.Q_BUILD, d_gap=self.D_BENCH)
        assert app.v_yield_apparatus() == pytest.approx(vy, rel=0, abs=0)

    def test_v_yield_apparatus_rejects_zero_g_geom(self):
        with pytest.raises(ValueError):
            bench.v_yield_apparatus(0.0, self.D_BENCH)

    def test_validate_on_known_fn_safe_max(self):
        """VALIDATE-ON-KNOWN: fn_safe_max_amplitude reproduces qg42 a_fn_safe_max.

        qg42 a_fn_safe_max() = E_FN_SAFE_CEILING / E_YIELD = 1.1589e-8
        (qg42 :132-139). Confirmed bit-for-bit at factoring time.
        """
        assert bench.fn_safe_max_amplitude() == pytest.approx(1.1588709741866756e-08, rel=0, abs=0)

    def test_validate_on_known_fn_table(self):
        """VALIDATE-ON-KNOWN: fn_dark_current reproduces the qg42 FN table.

        qg42 j_fn(beta, e_gap) at e_gap = V_YIELD/100um reproduces the canonical
        FN table (beta=3 SAFE, beta=6 MARGINAL, beta=50 DESTRUCTIVE; qg42
        :207-211). Confirmed bit-for-bit at factoring time.
        """
        e_gap = V_YIELD / 100e-6
        assert bench.fn_dark_current(3, e_gap) == pytest.approx(1.4007e-10, rel=1e-3)
        assert bench.fn_dark_current(6, e_gap) == pytest.approx(3.6267e1, rel=1e-3)
        assert bench.fn_dark_current(50, e_gap) == pytest.approx(8.2209e12, rel=1e-3)

    def test_fn_dark_current_monotone_and_floor(self):
        """FN dark current rises with beta; non-positive field returns 0.0."""
        e_gap = V_YIELD / 100e-6
        assert bench.fn_dark_current(3, e_gap) < bench.fn_dark_current(6, e_gap) < bench.fn_dark_current(50, e_gap)
        assert bench.fn_dark_current(0.0, e_gap) == 0.0
        assert bench.fn_dark_current(3, 0.0) == 0.0

    def test_fn_safe_field_ceiling(self):
        """fn_safe gate at the E_FN_SAFE_CEILING field (electropolished beta~3)."""
        from ave.bench.apparatus import E_FN_SAFE_CEILING, fn_safe

        # E_local = beta * e_gap just at the ceiling -> safe.
        assert fn_safe(beta=1.0, e_gap=E_FN_SAFE_CEILING) is True
        # Above the ceiling -> unsafe.
        assert fn_safe(beta=2.0, e_gap=E_FN_SAFE_CEILING) is False


class TestSNR:
    """snr.py <- apd_snr_sweep.py (snr_direct / t_detection / signal-vs-floor)."""

    # apd_snr_sweep reference point: signal_rate(V_yield, N=1e4) detected rate,
    # and the SPCM-AQRH-14 dark floor (apd_snr_sweep.py:44, :181). The signal
    # rate is a LABELED known captured from the exemplar at factoring time
    # (confirmed bit-for-bit via the exemplar's own snr_direct/t_detection).
    SIGNAL_REF = 17487.575495998968  # Hz, exemplar signal_rate(V_yield, 1e4)
    DARK_FLOOR = 100.0  # Hz, exemplar DARK_RATE

    def test_validate_on_known_snr_direct(self):
        """VALIDATE-ON-KNOWN: snr_shot_noise reproduces apd_snr_sweep.snr_direct.

        Same (signal, dark-floor) the exemplar uses at V_yield, N=1e4; the
        factored SNR over t=1/0.1/60 s reproduces snr_direct bit-for-bit
        (confirmed against the live exemplar at factoring time).
        """
        assert bench.snr_shot_noise(self.SIGNAL_REF, self.DARK_FLOOR, 1.0) == pytest.approx(131.8641, rel=1e-5)
        assert bench.snr_shot_noise(self.SIGNAL_REF, self.DARK_FLOOR, 0.1) == pytest.approx(41.69909, rel=1e-5)
        assert bench.snr_shot_noise(self.SIGNAL_REF, self.DARK_FLOOR, 60.0) == pytest.approx(1021.415, rel=1e-5)

    def test_validate_on_known_time_to_5sigma(self):
        """VALIDATE-ON-KNOWN: time_to_n_sigma reproduces apd_snr_sweep.t_detection.

        t(5sigma) = sigma^2 (s+d)/s^2 at the same reference signal/floor
        (apd_snr_sweep.py:94-95). Confirmed bit-for-bit at factoring time.
        """
        assert bench.time_to_n_sigma(self.SIGNAL_REF, self.DARK_FLOOR, 5.0) == pytest.approx(1.437761e-03, rel=1e-5)
        assert bench.time_to_n_sigma(self.SIGNAL_REF, self.DARK_FLOOR, 3.0) == pytest.approx(5.175941e-04, rel=1e-5)

    def test_snr_inverse_consistency(self):
        """SNR at time_to_n_sigma(sigma) equals sigma (the inversion is exact)."""
        for sigma in (5.0, 3.0, 1.0):
            t = bench.time_to_n_sigma(self.SIGNAL_REF, self.DARK_FLOOR, sigma)
            assert bench.snr_shot_noise(self.SIGNAL_REF, self.DARK_FLOOR, t) == pytest.approx(sigma, rel=1e-9)

    def test_time_to_n_sigma_inf_on_zero_signal(self):
        """Zero signal -> no detection possible -> inf (apd_snr_sweep.py:92-93)."""
        assert bench.time_to_n_sigma(0.0, self.DARK_FLOOR, 5.0) == float("inf")
        assert np.isinf(bench.time_to_n_sigma(0.0, 0.0, 5.0))

    def test_snr_zero_total_returns_zero(self):
        """Non-positive total counted rate -> 0.0 (apd_snr_sweep.py:86 guard)."""
        assert bench.snr_shot_noise(0.0, 0.0, 1.0) == 0.0
        assert bench.snr_shot_noise(5.0, 5.0, 0.0) == 0.0

    def test_signal_vs_floor(self):
        """signal/floor ratio; inf when floor <= 0 (the static margin)."""
        assert bench.signal_vs_floor(self.SIGNAL_REF, self.DARK_FLOOR) == pytest.approx(174.8757, rel=1e-5)
        assert np.isinf(bench.signal_vs_floor(1.0, 0.0))

    def test_snr_surface_matches_pointwise(self):
        """snr_surface[i,j] == snr_shot_noise(signals[i], floor, t[j])."""
        from ave.bench.snr import snr_surface

        signals = np.array([10.0, 100.0, 1000.0])
        t_grid = np.logspace(-3, 1, 5)
        surf = snr_surface(signals, self.DARK_FLOOR, t_grid)
        assert surf.shape == (3, 5)
        for i, s in enumerate(signals):
            for j, t in enumerate(t_grid):
                assert surf[i, j] == pytest.approx(bench.snr_shot_noise(float(s), self.DARK_FLOOR, float(t)))


class TestValidate:
    """validate.py <- src/scripts/verify/*_anchor.py (recover-a-known gate)."""

    def test_validate_on_known_muon_anchor_deviation(self):
        """VALIDATE-ON-KNOWN: compare_to_known reproduces the muon-anchor numbers.

        muon_g2_fermilab_anchor.py compare_to_fermilab_eeplus_baseline computes,
        for ave_prediction = 5.017805951650532e-09 vs Fermilab e+e- observed
        tension 2.45e-9 +/- 5.6e-10 (muon_g2_fermilab_anchor_results.json):
          deviation     = +2.567805951650532e-09
          deviation_pct = +104.80840618981763
          n_sigma       = +4.585367770804521
        The factored compare_to_known must reproduce these exactly.
        """
        from ave.bench.validate import compare_to_known

        cmp = compare_to_known(
            value=5.017805951650532e-09,
            reference=2.45e-09,
            tol=1.0,  # tolerance not under test here; deviation math is.
            label="muon a_mu (Fermilab e+e- baseline)",
            uncertainty=5.6e-10,
        )
        assert cmp.deviation == pytest.approx(2.567805951650532e-09, rel=0, abs=0)
        assert cmp.deviation_pct == pytest.approx(104.80840618981763, rel=1e-12)
        assert cmp.n_sigma == pytest.approx(4.585367770804521, rel=1e-12)

    def test_recover_a_known_pass_within_tol(self):
        """assert_recovers_known returns the record when within tol (PASS)."""
        # qg42 :189 quotes the V^2 discrimination ratio = 2.895e6; recover it
        # to within 0.1% as a recover-a-known PASS exemplar.
        cmp = bench.assert_recovers_known(
            value=2.8946e6, reference=2.895e6, tol=1e-3, label="qg42 V^2 discrimination ratio"
        )
        assert cmp.passed is True
        assert "PASS" in cmp.summary()

    def test_recover_a_known_raises_outside_tol(self):
        """assert_recovers_known raises with full breakdown when outside tol (FLAG)."""
        with pytest.raises(AssertionError) as exc:
            bench.assert_recovers_known(value=1.10, reference=1.00, tol=1e-3, label="off-by-10pct")
        msg = str(exc.value)
        assert "recover-a-known FAILED" in msg
        assert "off-by-10pct" in msg
        assert "rel_error" in msg

    def test_compare_to_known_does_not_raise(self):
        """compare_to_known is the non-raising sibling (returns FLAG record)."""
        from ave.bench.validate import compare_to_known

        cmp = compare_to_known(value=1.10, reference=1.00, tol=1e-3, label="off")
        assert cmp.passed is False
        assert "FLAG" in cmp.summary()

    def test_zero_reference_is_inf_not_nan(self):
        """A zero reference yields inf rel_error (FLAG), never NaN/divide error."""
        from ave.bench.validate import compare_to_known

        cmp = compare_to_known(value=1.0, reference=0.0, tol=1e-3, label="zero-ref")
        assert np.isinf(cmp.rel_error)
        assert np.isinf(cmp.deviation_pct)
        assert cmp.passed is False

    def test_n_sigma_none_without_uncertainty(self):
        """n_sigma is None when no uncertainty is supplied (PDG-anchor optional)."""
        cmp = bench.assert_recovers_known(value=1.0001, reference=1.0, tol=1e-3, label="no-unc")
        assert cmp.n_sigma is None
        assert "sigma" not in cmp.summary()


# ============================================================================
# birefringence.py — vacuum-birefringence bench physics (AVE vs QED).
# Validate-on-known: the QED model must recover the PVLAS A_e ~ 1.32e-24 T^-2,
# and the substrate identity (E_crit/E_yield)^2 == 1/alpha must hold.
# ============================================================================
class TestBirefringence:
    def test_validate_on_known_pvlas_A_e(self):
        """The QED magnetic birefringence constant recovers the PVLAS textbook
        value 1.32e-24 T^-2 (the load-bearing validate-on-known gate)."""
        A_e = bench.vacuum_magnetic_birefringence_constant()
        bench.assert_recovers_known(
            value=A_e, reference=1.32e-24, tol=0.01,
            label="PVLAS vacuum magnetic birefringence A_e [T^-2]",
        )

    def test_validate_on_known_qed_magnetic_delta_n_at_1T(self):
        """delta_n_QED = 3 A_e B^2 recovers the textbook ~4e-24 at B = 1 T."""
        dn = float(bench.delta_n_qed_magnetic(1.0))
        bench.assert_recovers_known(
            value=dn, reference=3.97e-24, tol=0.02,
            label="QED magnetic differential delta_n at 1 T",
        )

    def test_substrate_identity_holds(self):
        """(E_crit/E_yield)^2 == 1/alpha AND c*B_crit == E_crit (the ratio
        collapse + field-energy equivalence)."""
        assert bench.substrate_identity_holds() is True

    def test_ave_retardance_is_negative_and_E2_leading(self):
        """delta_n_AVE < 0 (vacuum softens) and scales as E^2 at small field
        (the leading term, NOT E^4 — the retracted framing)."""
        E1, E2 = 1e13, 2e13
        dn1 = float(bench.delta_n_ave_exact(E1))
        dn2 = float(bench.delta_n_ave_exact(E2))
        assert dn1 < 0 and dn2 < 0
        # doubling E quadruples |delta_n| (E^2 leading), not 16x (E^4).
        assert np.isclose(dn2 / dn1, 4.0, rtol=1e-3)

    def test_ave_retardance_small_field_precision(self):
        """The expm1/log1p form is exact at small A where the naive
        (1-A^2)^(1/4)-1 underflows to a spurious 0 (the precision-guard regression)."""
        E = 1e9  # A ~ 8.8e-9
        dn = float(bench.delta_n_ave_exact(E))
        dn_lead = float(bench.delta_n_ave_leading(E))
        assert dn != 0.0  # must NOT underflow to zero
        assert np.isclose(dn, dn_lead, rtol=1e-4)  # leading term is exact there

    def test_ave_retardance_nan_past_yield(self):
        """A >= 1 (E >= E_YIELD) returns NaN (optical observable undefined past yield)."""
        from ave.core.constants import E_YIELD

        assert np.isnan(float(bench.delta_n_ave_exact(2.0 * E_YIELD)))

    def test_coefficient_ratio_is_1_over_4_aEH_alpha3(self):
        """The field-independent ratio = 1/(4 a_EH alpha^3) ~ 4.1e6 at a_EH=7/45."""
        from ave.core.constants import ALPHA

        a_eh = 7.0 / 45.0
        assert np.isclose(bench.coefficient_ratio(a_eh), 1.0 / (4.0 * a_eh * ALPHA**3))
        # and equals the swept |dn_AVE_leading|/dn_QED ratio (field-independent).
        E = np.array([1e12, 1e14])
        r = np.abs(bench.delta_n_ave_leading(E)) / bench.delta_n_qed(E, a_eh)
        assert np.allclose(r, r[0], rtol=1e-9)
        assert np.isclose(r[0], bench.coefficient_ratio(a_eh), rtol=1e-6)

    def test_optical_activity_is_parity_odd(self):
        """The rotation sign flips between enantiomorphs (parity-odd FORM)."""
        rR = bench.optical_activity_rate_deg_per_m("right")
        rL = bench.optical_activity_rate_deg_per_m("left")
        assert rR > 0 and rL < 0
        assert np.isclose(rR, -rL)

    def test_qed_rotation_is_identically_zero(self):
        """QED vacuum produces ZERO optical-activity rotation (the SM-counterfactual)."""
        for L in (1e-3, 1.0, 1e3):
            assert bench.optical_activity_rotation_qed(L) == 0.0

    def test_optical_activity_scales_with_path_and_fraction(self):
        """theta = rate * path * chirality_fraction (linear in both)."""
        t1 = bench.optical_activity_rotation_deg(1.0, "right", chirality_fraction=1e-12)
        t2 = bench.optical_activity_rotation_deg(2.0, "right", chirality_fraction=1e-12)
        t3 = bench.optical_activity_rotation_deg(1.0, "right", chirality_fraction=2e-12)
        assert np.isclose(t2, 2.0 * t1)
        assert np.isclose(t3, 2.0 * t1)

    def test_a_eh_band_includes_pvlas_and_single_mode(self):
        """The reported a_EH band spans the single-mode 3/45 and PVLAS ~1.45 convs."""
        band = bench.A_EH_LITERATURE
        assert any(np.isclose(v, 3.0 / 45.0) for v in band.values())
        assert any(1.4 < v < 1.5 for v in band.values())  # the PVLAS A_e differential
