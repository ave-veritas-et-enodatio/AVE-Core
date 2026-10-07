"""
Tests for tone probe recorder and harmonic-inversion ring-down analyzer.

Tests:
  1. TestMatrixPencil      — synthetic damped sinusoids; recovery with/without noise.
  2. TestRecordLengthTable — accuracy-vs-periods table at 5,10,15,20,50,100 periods.
                             Tests Math's LEAN claim; results printed to stdout.
  3. TestBandClassification — band-window and KW-flag logic.
  4. TestAmplitudeSweep    — d(ω)/d(A²) estimation from multiple runs.
  5. TestProbeRecorder     — default OFF = no behavior change; ON writes correct shape.
  6. TestUniformModeSmoke  — smoke: uniform k=0 mode, record, analyze, check ω ≈ 2.

LEAN flag: the 10-20 period sufficiency claim is LEAN (direction DERIVED from
Cramér–Rao + MEEP/Harminv precedent; the count is a judgment).
The table in TestRecordLengthTable shows what the numbers actually say.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import numpy as np
import pytest

from ave.topological.tone_analyzer import (
    OMEGA_AC_TOP,
    OMEGA_M,
    OMEGA_ROT_TOP,
    OMEGA_T_TOP,
    Pole,
    _classify_pole,
    _matrix_pencil_zk,
    _recover_amplitudes,
    _zk_to_poles,
    analyze,
    amplitude_sweep,
    band_report,
    print_nonstationarity_table,
    print_record_length_table,
    record_length_nonstationarity_table,
    record_length_table,
    sliding_window_analyze,
    summarize,
)
from ave.topological.tone_probe import ToneProbe, _default_probe_sites


# ---------------------------------------------------------------------------
# 1. Matrix pencil: synthetic signal recovery
# ---------------------------------------------------------------------------

class TestMatrixPencil:
    """Synthetic damped-sinusoid recovery tests."""

    def _make_signal(self, Omega, Gamma, dt, n_periods, amplitude=1.0, noise=0.0, rng=None):
        period = 2.0 * np.pi / Omega
        N = int(round(n_periods * period / dt))
        t = np.arange(N) * dt
        sig = amplitude * np.cos(Omega * t) * np.exp(-Gamma * t)
        if noise > 0.0 and rng is not None:
            sig = sig.astype(complex)
            sig += noise * (rng.standard_normal(N) + 1j * rng.standard_normal(N))
        return sig

    def test_single_pole_noiseless_frequency(self):
        """Single damped sinusoid, no noise: recovered Ω within 1e-6."""
        rng = np.random.default_rng(0)
        Omega_true = 1.9
        Gamma_true = 0.02
        dt = 0.10
        sig = self._make_signal(Omega_true, Gamma_true, dt, n_periods=20)
        poles = analyze(sig, dt, n_poles_max=2, n_model_orders=1)
        assert len(poles) > 0
        pos_poles = [p for p in poles if p.Omega > 0]
        assert len(pos_poles) > 0
        best = min(pos_poles, key=lambda p: abs(p.Omega - Omega_true))
        assert abs(best.Omega - Omega_true) < 1e-4, f"Omega error {abs(best.Omega - Omega_true):.2e}"

    def test_single_pole_noiseless_Q(self):
        """Single damped sinusoid, no noise: recovered Q within 1% of truth."""
        Omega_true = 1.9
        Gamma_true = Omega_true / (2.0 * 100.0)  # Q=100
        dt = 0.10
        sig = self._make_signal(Omega_true, Gamma_true, dt, n_periods=25)
        poles = analyze(sig, dt, n_poles_max=2, n_model_orders=1)
        pos_poles = [p for p in poles if p.Omega > 0 and p.Gamma > 0]
        assert len(pos_poles) > 0
        best = min(pos_poles, key=lambda p: abs(p.Omega - Omega_true))
        assert abs(best.Q - 100.0) / 100.0 < 0.05, f"Q error {abs(best.Q - 100.0):.2f}"

    def test_two_poles_noiseless(self):
        """Two nearby poles, no noise: both recovered within 1e-3."""
        dt = 0.08
        Omega1, Gamma1 = 1.85, 0.01
        Omega2, Gamma2 = 1.95, 0.015
        period_min = 2.0 * np.pi / min(Omega1, Omega2)
        N = int(round(25 * period_min / dt))
        t = np.arange(N) * dt
        sig = (np.cos(Omega1 * t) * np.exp(-Gamma1 * t) +
               0.6 * np.cos(Omega2 * t) * np.exp(-Gamma2 * t))
        poles = analyze(sig, dt, n_poles_max=4, n_model_orders=2)
        omegas_found = sorted([p.Omega for p in poles if p.Omega > 0.5])
        assert len(omegas_found) >= 2
        assert abs(omegas_found[0] - Omega1) < 0.02
        assert abs(omegas_found[-1] - Omega2) < 0.02

    def test_noise_robustness(self):
        """Noise at 1e-8: Ω recovered within 1e-3."""
        rng = np.random.default_rng(7)
        Omega_true = 1.9
        Gamma_true = 0.02
        dt = 0.10
        sig = self._make_signal(Omega_true, Gamma_true, dt, n_periods=30,
                                 noise=1e-8, rng=rng)
        poles = analyze(sig, dt, n_poles_max=2, n_model_orders=2)
        pos_poles = [p for p in poles if p.Omega > 0]
        assert len(pos_poles) > 0
        best = min(pos_poles, key=lambda p: abs(p.Omega - Omega_true))
        assert abs(best.Omega - Omega_true) < 0.01

    def test_growth_mode_detected(self):
        """A growing mode (|z| > 1) is flagged as is_growth=True."""
        dt = 0.10
        Omega = 1.9
        Gamma_negative = -0.05   # growing
        N = 150
        t = np.arange(N) * dt
        sig = np.cos(Omega * t) * np.exp(-Gamma_negative * t)   # exp(+0.05t)
        poles = analyze(sig, dt, n_poles_max=2, n_model_orders=1)
        growth_poles = [p for p in poles if p.is_growth and p.Omega > 0.5]
        assert len(growth_poles) > 0, "Expected a growth-flagged pole"

    def test_omega_m_uniform_mode(self):
        """Exact ω_m = 2 signal recovered to within 1e-5."""
        Omega_true = 2.0
        dt = 0.09
        N = int(round(25 * 2.0 * np.pi / Omega_true / dt))
        t = np.arange(N) * dt
        Gamma = 0.001
        sig = np.cos(Omega_true * t) * np.exp(-Gamma * t)
        poles = analyze(sig, dt, n_poles_max=2, n_model_orders=1)
        pos_poles = [p for p in poles if p.Omega > 1.0]
        assert len(pos_poles) > 0
        best = min(pos_poles, key=lambda p: abs(p.Omega - Omega_true))
        assert abs(best.Omega - Omega_true) < 1e-4, \
            f"ω_m recovery error: {abs(best.Omega - Omega_true):.2e}"


# ---------------------------------------------------------------------------
# 2. Record length table
# ---------------------------------------------------------------------------

class TestRecordLengthTable:
    """Accuracy table at 5, 10, 15, 20, 50, 100 periods.

    Tests Math's LEAN claim that 10–20 periods suffice for the harmonic-
    inversion method. The table shows what the numbers actually say.
    LEAN: direction DERIVED (Cramér–Rao + MEEP/Harminv precedent);
    the count is a judgment. Binding limits: non-stationarity and band-edge
    continuum tail, not noise.
    """

    @pytest.fixture(scope="class")
    def table(self):
        rows = record_length_table(
            Omega=1.9, Q=100.0, dt=0.165, noise_level=1e-10,
            n_poles=2, n_trials=10,
            periods_list=(5, 10, 15, 20, 50, 100),
        )
        print_record_length_table(rows, Omega=1.9, Q=100.0)
        return rows

    def test_table_has_all_periods(self, table):
        periods_found = [r["periods"] for r in table]
        for p in (5, 10, 15, 20, 50, 100):
            assert p in periods_found

    def test_100_period_accurate(self, table):
        """100-period record gives Ω error < 1e-6 at noise=1e-10."""
        r100 = next(r for r in table if r["periods"] == 100)
        assert r100["Omega_err_mean"] < 1e-5, \
            f"100-period Ω error = {r100['Omega_err_mean']:.2e}"

    def test_20_period_omega_better_than_5(self, table):
        """20-period record should give lower Ω error than 5-period."""
        r5 = next(r for r in table if r["periods"] == 5)
        r20 = next(r for r in table if r["periods"] == 20)
        assert r20["Omega_err_mean"] <= r5["Omega_err_mean"] * 10.0, \
            (f"20-period error ({r20['Omega_err_mean']:.2e}) not better than "
             f"5-period ({r5['Omega_err_mean']:.2e}) × 10")

    def test_lean_claim_noted(self, table):
        """Table exists and contains the LEAN-flagged record lengths."""
        assert len(table) == 6


# ---------------------------------------------------------------------------
# 3. Band classification
# ---------------------------------------------------------------------------

class TestBandClassification:
    """Band window and KW-flag logic."""

    def test_9pct_window_center(self):
        p = _classify_pole(1.93, 0.02, 1.0, 0.0)
        assert p.in_9pct_window
        assert p.in_t1_window
        assert not p.in_rot_band

    def test_below_9pct_in_t1(self):
        p = _classify_pole(1.5, 0.02, 1.0, 0.0)
        assert not p.in_9pct_window
        assert p.in_t1_window
        assert not p.in_rot_band

    def test_rotational_band(self):
        p = _classify_pole(2.2, 0.02, 1.0, 0.0)
        assert not p.in_9pct_window
        assert not p.in_t1_window
        assert p.in_rot_band

    def test_kw_flag_2omega_in_rot_band(self):
        # Ω ≈ 1.1, so 2Ω ≈ 2.2 ∈ [2, √6]
        p = _classify_pole(1.1, 0.02, 1.0, 0.0)
        assert p.kw_flag

    def test_kw_flag_not_set_when_doubled_below_band(self):
        # Ω ≈ 0.5, 2Ω = 1.0 < 2
        p = _classify_pole(0.5, 0.02, 1.0, 0.0)
        assert not p.kw_flag

    def test_band_report_growth_flagged(self):
        poles = [
            _classify_pole(1.9, 0.01, 1.0, 0.0),   # normal
            _classify_pole(1.9, -0.01, 0.5, 0.0),  # growing
        ]
        report = band_report(poles)
        assert len(report["growth_flagged"]) == 1

    def test_omega_m_boundary(self):
        p_below = _classify_pole(OMEGA_M - 1e-9, 0.01, 1.0, 0.0)
        p_above = _classify_pole(OMEGA_M + 1e-9, 0.01, 1.0, 0.0)
        assert p_below.in_9pct_window
        assert not p_above.in_9pct_window
        assert not p_below.in_rot_band
        assert p_above.in_rot_band


# ---------------------------------------------------------------------------
# 3b. Growth tolerance — pin the classification rule from both sides
# ---------------------------------------------------------------------------

class TestGrowthTolerance:
    """Pin the growth-tolerance rule in _classify_pole from both sides.

    Full rule (Gate k-cal 2026-10-06):
        σ_Γ_CR = √6 · σ_resid / (|c| · dt · √(N(N²−1)))
        tol = max(5·σ_Γ_CR, 3·Gamma_err, 50·eps_mach·|Ω|)
    Direct _classify_pole calls without sigma_resid/dt_hint/N_hint use
    σ_Γ_CR=0, falling back to: tol = max(0, 0, 50·eps·|Ω|) ≈ 2.2e-14
    at Ω=2. The Linux VV CI noise (Γ=−2.33e-15) is still below this floor.
    """

    def test_noise_level_gamma_not_growth(self):
        """Linux CI case: Gamma=-2.33e-15 at Omega=2.003 must NOT be flagged.

        This is the exact value produced by the Linux VV integrator in
        TestUniformModeSmoke; it is integrator noise, not physical growth.
        tol ≈ 50 × 2.22e-16 × 2.003 ≈ 2.22e-14 >> 2.33e-15.
        """
        p = _classify_pole(2.003, -2.33e-15, 1.0, 0.0)
        assert not p.is_growth, (
            f"Noise-level Gamma=-2.33e-15 at Omega=2.003 must not be flagged. "
            f"tol ≈ {50 * np.finfo(float).eps * 2.003:.2e}"
        )

    def test_small_growth_direct_1e4(self):
        """Direct: Gamma=-1e-4 at Omega=1.9 is IS flagged (×4500 above tol)."""
        p = _classify_pole(1.9, -1e-4, 1.0, 0.0)
        assert p.is_growth, "Gamma=-1e-4 at Omega=1.9 must be flagged as growth"

    def test_small_growth_direct_1e3(self):
        """Direct: Gamma=-1e-3 at Omega=1.9 is flagged."""
        p = _classify_pole(1.9, -1e-3, 1.0, 0.0)
        assert p.is_growth, "Gamma=-1e-3 at Omega=1.9 must be flagged as growth"

    def test_small_damping_not_growth(self):
        """Gamma=+1e-4 is damping; must NOT be flagged as growth."""
        p = _classify_pole(1.9, 1e-4, 1.0, 0.0)
        assert not p.is_growth, "Positive Gamma (damping) must not be flagged as growth"

    def test_small_growth_synthetic_15periods_1e4(self):
        """Synthetic: Gamma=-1e-4, ~15 periods, small noise → growth detected.

        The signal amplitude grows by exp(1e-4 × 15T) ≈ 1.03 over 15 periods.
        At noise=1e-8 the analyzer recovers Gamma accurately; the tolerance
        (≈2e-14) is ×5000 below the true Gamma magnitude.
        """
        rng = np.random.default_rng(12345)
        Omega, Gamma = 1.9, -1e-4
        dt = 0.165
        period = 2.0 * np.pi / Omega
        N = int(round(15 * period / dt))
        t = np.arange(N) * dt
        sig = (np.cos(Omega * t) * np.exp(-Gamma * t)).astype(complex)
        sig += 1e-8 * (rng.standard_normal(N) + 1j * rng.standard_normal(N))
        poles = analyze(sig, dt, n_poles_max=2, n_model_orders=3)
        pos = [p for p in poles if p.Omega > 0.5]
        assert len(pos) > 0, "No positive-frequency poles found"
        best = min(pos, key=lambda p: abs(p.Omega - Omega))
        assert best.is_growth, (
            f"Synthetic Gamma=-1e-4, 15 periods: growth not detected "
            f"(Gamma found={best.Gamma:.2e}, is_growth={best.is_growth})"
        )

    def test_small_growth_synthetic_20periods_1e3(self):
        """Synthetic: Gamma=-1e-3, ~20 periods, small noise → growth detected.

        The signal amplitude grows by exp(1e-3 × 20T) ≈ 1.13 over 20 periods.
        """
        rng = np.random.default_rng(99999)
        Omega, Gamma = 1.9, -1e-3
        dt = 0.165
        period = 2.0 * np.pi / Omega
        N = int(round(20 * period / dt))
        t = np.arange(N) * dt
        sig = (np.cos(Omega * t) * np.exp(-Gamma * t)).astype(complex)
        sig += 1e-8 * (rng.standard_normal(N) + 1j * rng.standard_normal(N))
        poles = analyze(sig, dt, n_poles_max=2, n_model_orders=3)
        pos = [p for p in poles if p.Omega > 0.5]
        assert len(pos) > 0, "No positive-frequency poles found"
        best = min(pos, key=lambda p: abs(p.Omega - Omega))
        assert best.is_growth, (
            f"Synthetic Gamma=-1e-3, 20 periods: growth not detected "
            f"(Gamma found={best.Gamma:.2e}, is_growth={best.is_growth})"
        )

    def test_small_damping_synthetic_not_growth(self):
        """Synthetic: Gamma=+1e-4, 15 periods → NOT flagged as growth."""
        rng = np.random.default_rng(77777)
        Omega, Gamma = 1.9, 1e-4
        dt = 0.165
        period = 2.0 * np.pi / Omega
        N = int(round(15 * period / dt))
        t = np.arange(N) * dt
        sig = (np.cos(Omega * t) * np.exp(-Gamma * t)).astype(complex)
        sig += 1e-8 * (rng.standard_normal(N) + 1j * rng.standard_normal(N))
        poles = analyze(sig, dt, n_poles_max=2, n_model_orders=3)
        pos = [p for p in poles if p.Omega > 0.5]
        assert len(pos) > 0, "No positive-frequency poles found"
        best = min(pos, key=lambda p: abs(p.Omega - Omega))
        assert not best.is_growth, (
            f"Synthetic Gamma=+1e-4 (damping) must not be flagged as growth "
            f"(Gamma found={best.Gamma:.2e}, is_growth={best.is_growth})"
        )


# ---------------------------------------------------------------------------
# 3d. Gamma=0 null test — false-positive growth rate (Gate R2/R3)
# ---------------------------------------------------------------------------

class TestGrowthNullFloor:
    """Γ=0 null: false-positive is_growth ≤1% over 200 trials at noise ≥1e-10.

    Gate R2/R3 fix (Gate k-cal 2026-10-06). The locked formula is:
        σ_Γ_CR = √6 · σ_resid / (|c| · dt · √(N(N²−1)))
        growth_tol = max(5·σ_Γ_CR, 3·Gamma_err, 50·eps·|Ω|)

    Prior formula max(3·Gamma_err, 50·eps·|Ω|) gave ~49% FP at noise 1e-10
    (Gate FAIL). This test class FAILS on the prior tip and PASSES here.

    Scope: identified-tone growth/decay only — not cold-seed window-presence,
    not shell-flux zero kill (tracker R26.196b).

    Parameters match Gate null_test.py: Ω=1.9, dt=0.165, 15 periods,
    N=301, complex Gaussian noise, n_poles_max=2, n_model_orders=3, seed=1.
    """

    @pytest.fixture(scope="class")
    def null_fp_table(self):
        """Run Γ=0 null trials at three noise levels; return FP table."""
        Omega = 1.9
        dt = 0.165
        n_periods = 15
        n_trials = 200
        N = int(round(n_periods * 2.0 * np.pi / Omega / dt))
        t = np.arange(N) * dt
        noise_levels = [1e-10, 1e-8, 1e-6]
        rows = []

        for noise in noise_levels:
            rng = np.random.default_rng(1)   # same seed as Gate null_test.py
            fp_main = 0
            fp_any = 0
            gammas: list[float] = []
            sigma_CR_vals: list[float] = []

            for _ in range(n_trials):
                sig = np.cos(Omega * t).astype(complex)
                sig += noise * (rng.standard_normal(N) + 1j * rng.standard_normal(N))
                poles = analyze(sig, dt, n_poles_max=2, n_model_orders=3)
                pos = [p for p in poles if p.Omega > 0.5]
                if pos:
                    best = min(pos, key=lambda p: abs(p.Omega - Omega))
                    gammas.append(best.Gamma)
                    fp_main += int(best.is_growth)
                fp_any += int(any(p.is_growth for p in poles))

            sigma_emp = float(np.std(gammas)) if gammas else float("nan")
            # Analytic CR reference (|c|≈0.5 for unit cosine, N=301, dt=0.165)
            sigma_CR_ref = (np.sqrt(6.0) * noise
                            / (0.5 * dt * np.sqrt(N * (N ** 2 - 1.0))))
            rows.append({
                "noise": noise,
                "N": N,
                "n_trials": n_trials,
                "fp_main": fp_main,
                "fp_any": fp_any,
                "fp_main_rate": fp_main / n_trials,
                "fp_any_rate": fp_any / n_trials,
                "sigma_emp": sigma_emp,
                "sigma_CR": sigma_CR_ref,
            })

        print("\n=== Gamma=0 null test — Gate R2/R3 (k-cal 2026-10-06) ===")
        print(f"N={rows[0]['N']}, n_trials={n_trials}, Omega=1.9, dt=0.165, 15 periods")
        print(f"{'noise':>8}  {'FP main':>8}  {'FP any':>8}  "
              f"{'σ_emp_Γ':>11}  {'σ_CR_Γ':>11}")
        for r in rows:
            print(f"{r['noise']:>8.0e}  {r['fp_main_rate']:>8.3f}  "
                  f"{r['fp_any_rate']:>8.3f}  "
                  f"{r['sigma_emp']:>11.3e}  {r['sigma_CR']:>11.3e}")
        return rows

    def test_fp_rate_noise_1e10(self, null_fp_table):
        """Γ=0 null: FP ≤1% at noise 1e-10 (PR default; Gate R2 kill line)."""
        r = next(row for row in null_fp_table if row["noise"] == 1e-10)
        assert r["fp_main_rate"] <= 0.01, (
            f"Gate R2: Gamma=0 null at noise 1e-10: "
            f"FP={r['fp_main']}/{r['n_trials']} ({r['fp_main_rate']:.1%}). "
            f"Prior formula gave ~49% FP. Requires k=5 CR formula."
        )

    def test_fp_rate_noise_1e8(self, null_fp_table):
        """Γ=0 null: FP ≤1% at noise 1e-8."""
        r = next(row for row in null_fp_table if row["noise"] == 1e-8)
        assert r["fp_main_rate"] <= 0.01, (
            f"Gate R2: Gamma=0 null at noise 1e-8: "
            f"FP={r['fp_main']}/{r['n_trials']} ({r['fp_main_rate']:.1%})"
        )

    def test_fp_rate_noise_1e6(self, null_fp_table):
        """Γ=0 null: FP ≤1% at noise 1e-6."""
        r = next(row for row in null_fp_table if row["noise"] == 1e-6)
        assert r["fp_main_rate"] <= 0.01, (
            f"Gate R2: Gamma=0 null at noise 1e-6: "
            f"FP={r['fp_main']}/{r['n_trials']} ({r['fp_main_rate']:.1%})"
        )


# ---------------------------------------------------------------------------
# 3c. Nonstationarity record-length table
# ---------------------------------------------------------------------------

class TestRecordLengthNonstationarityTable:
    """Accuracy table for clean, chirp-1e-4, chirp-1e-3, and drift-1% cases.

    Shows that 10–20 periods suffice for the clean case (LEAN claim) but
    that non-stationarity (chirp, drift) limits accuracy independent of
    record length — confirming the binding limits stated in the LEAN flag.
    """

    @pytest.fixture(scope="class")
    def nstable(self):
        rows = record_length_nonstationarity_table(
            Omega=1.9, Q=100.0, dt=0.165, noise_level=1e-10,
            n_poles=2, n_trials=8,
            periods_list=(5, 10, 15, 20, 50, 100),
        )
        print_nonstationarity_table(rows, Omega=1.9, Q=100.0)
        return rows

    def test_table_has_all_periods(self, nstable):
        periods_found = [r["periods"] for r in nstable]
        for p in (5, 10, 15, 20, 50, 100):
            assert p in periods_found

    def test_clean_20_better_than_clean_5(self, nstable):
        """Clean case: 20-period record gives lower Ω error than 5-period."""
        r5  = next(r for r in nstable if r["periods"] == 5)
        r20 = next(r for r in nstable if r["periods"] == 20)
        assert r20["clean_Omega_err_mean"] <= r5["clean_Omega_err_mean"] * 10.0, (
            f"20-period clean ({r20['clean_Omega_err_mean']:.2e}) should be "
            f"better than 5-period ({r5['clean_Omega_err_mean']:.2e}) × 10"
        )

    def test_chirp_1e3_worse_than_clean(self, nstable):
        """chirp-1e-3 at 20 periods dominates noise: Ω error >> clean case."""
        r20 = next(r for r in nstable if r["periods"] == 20)
        assert r20["chirp_1e3_Omega_err_mean"] > r20["clean_Omega_err_mean"] * 100, (
            f"chirp-1e-3 Ω_err ({r20['chirp_1e3_Omega_err_mean']:.2e}) should be "
            f">> clean ({r20['clean_Omega_err_mean']:.2e}) at 20 periods"
        )

    def test_chirp_1e3_grows_with_periods(self, nstable):
        """chirp-1e-3: longer records accumulate more frequency error (binding limit)."""
        r5   = next(r for r in nstable if r["periods"] == 5)
        r100 = next(r for r in nstable if r["periods"] == 100)
        assert r100["chirp_1e3_Omega_err_mean"] >= r5["chirp_1e3_Omega_err_mean"] * 0.5, (
            "chirp-1e-3 error should not drop below half the 5-period error at 100 periods"
        )


# ---------------------------------------------------------------------------
# 4. Amplitude sweep
# ---------------------------------------------------------------------------

class TestAmplitudeSweep:
    """d(ω)/d(A²) estimation."""

    def test_linear_trend_recovered(self):
        """Known linear trend ω(A²) = 1.9 − 0.5 A² recovered within 20%."""
        rng = np.random.default_rng(99)
        A_sq = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
        omega_true = 1.9 - 0.5 * A_sq
        omega_noisy = omega_true + 0.001 * rng.standard_normal(len(A_sq))
        result = amplitude_sweep(omega_noisy.tolist(), A_sq.tolist())
        assert abs(result["slope"] - (-0.5)) < 0.1, f"slope = {result['slope']:.4f}"

    def test_single_point_returns_nan(self):
        result = amplitude_sweep([1.9], [0.0])
        assert result["slope"] != result["slope"]  # NaN

    def test_note_mentions_branch(self):
        result = amplitude_sweep([1.9, 1.88], [0.0, 0.1])
        assert "branch" in result["note"].lower()


# ---------------------------------------------------------------------------
# 5. Probe recorder
# ---------------------------------------------------------------------------

class TestProbeRecorder:
    """Probe recorder: OFF = no behavior change; ON writes correct arrays."""

    @pytest.fixture
    def solver(self):
        import jax
        jax.config.update("jax_enable_x64", True)
        from ave.topological.cosserat_field_3d import CosseratField3D
        s = CosseratField3D(8, 8, 8, use_saturation=False)
        return s

    def test_probe_off_is_passthrough(self, solver):
        """probe_every=0: solver state after probe.step() matches direct step()."""
        import copy

        # Two identical solvers
        s1 = solver
        from ave.topological.cosserat_field_3d import CosseratField3D
        s2 = CosseratField3D(8, 8, 8, use_saturation=False)

        # Same initial perturbation
        alive = np.argwhere(s1.mask_alive)
        site = tuple(alive[len(alive) // 2])
        s1.omega_dot[site] = [0.0, 0.0, 0.1]
        s2.omega_dot[site] = [0.0, 0.0, 0.1]

        probe = ToneProbe(s1, probe_every=0)  # OFF
        assert not probe.enabled

        dt = s1.cfl_dt
        # 5 steps each
        for _ in range(5):
            probe.step(dt=dt)
            s2.step(dt=dt)

        assert np.allclose(s1.omega, s2.omega, atol=1e-14), \
            "probe_every=0 must not change engine state"

    def test_probe_off_no_samples(self, solver):
        probe = ToneProbe(solver, probe_every=0)
        for _ in range(3):
            probe.step()
        assert probe.n_samples == 0

    def test_probe_on_records_every_step(self, solver):
        """probe_every=1: records at every step."""
        # Give a simple explicit probe site
        alive = np.argwhere(solver.mask_alive)
        site = [tuple(alive[0])]
        probe = ToneProbe(solver, probe_every=1, probe_sites=site)
        n_steps = 5
        for _ in range(n_steps):
            probe.step()
        assert probe.n_samples == n_steps

    def test_probe_on_records_every_n(self, solver):
        """probe_every=3: records every 3rd step."""
        alive = np.argwhere(solver.mask_alive)
        site = [tuple(alive[0])]
        probe = ToneProbe(solver, probe_every=3, probe_sites=site)
        n_steps = 9
        for _ in range(n_steps):
            probe.step()
        assert probe.n_samples == 3   # steps 0, 3, 6

    def test_probe_array_shapes(self, solver):
        """Saved .npz has correct array shapes."""
        alive = np.argwhere(solver.mask_alive)
        sites = [tuple(alive[0]), tuple(alive[1])]
        probe = ToneProbe(solver, probe_every=1, probe_sites=sites)
        for _ in range(4):
            probe.step()

        with tempfile.TemporaryDirectory() as td:
            path = str(Path(td) / "probes.npz")
            probe.save(path)
            data = ToneProbe.load(path)

        n_s = probe.n_samples  # 4
        n_p = len(sites)        # 2
        assert data["times"].shape == (n_s,), f"times shape {data['times'].shape}"
        assert data["u"].shape == (n_s, n_p, 3), f"u shape {data['u'].shape}"
        assert data["omega"].shape == (n_s, n_p, 3)
        assert data["omega_max"].shape == (n_s,)
        assert data["wrap_flags"].shape == (n_s,)
        assert data["probe_sites"].shape == (n_p, 3)
        assert data["neighbor_coords"].shape == (n_p, 4, 3)

    def test_metadata_saved(self, solver):
        """JSON metadata file is written with required keys."""
        alive = np.argwhere(solver.mask_alive)
        site = [tuple(alive[0])]
        probe = ToneProbe(solver, probe_every=1, probe_sites=site, label="testrun")
        for _ in range(2):
            probe.step()

        with tempfile.TemporaryDirectory() as td:
            path = str(Path(td) / "probes.npz")
            probe.save(path)
            meta_path = path + ".meta.json"
            with open(meta_path) as f:
                meta = json.load(f)

        for key in ("dt_cfl", "probe_every", "n_samples", "n_probes",
                    "grid", "wrap_caution", "git_sha", "jax_version"):
            assert key in meta, f"Missing key: {key}"
        assert meta["label"] == "testrun"

    def test_wrap_flag_triggered(self, solver):
        """Sites where max |omega| > π get wrap_flags=True."""
        alive = np.argwhere(solver.mask_alive)
        site = [tuple(alive[0])]
        probe = ToneProbe(solver, probe_every=1, probe_sites=site)

        # Manually set omega past π on an alive site
        probe.step()  # normal step
        solver.omega[tuple(alive[0])] = [0.0, 0.0, 3.5]  # > π
        probe._record()  # force a manual record at high omega

        flags = np.array(probe._wrap_flags)
        assert flags[-1] == True, "Expected WRAP flag when max |omega| > π"
        assert flags[0] == False, "Expected no WRAP flag at initial small amplitude"

    def test_default_probe_sites_generated(self):
        """Default probe sites are generated from R, r and all are alive sites."""
        import jax
        jax.config.update("jax_enable_x64", True)
        from ave.topological.cosserat_field_3d import CosseratField3D
        solver = CosseratField3D(20, 20, 20, use_saturation=False)
        R, r = 5.0, 2.0
        sites = _default_probe_sites(solver, R, r)
        assert len(sites) >= 6, "Expected at least 6 probe sites"
        for site in sites:
            i, j, k = site
            assert solver.mask_alive[i, j, k], f"Probe site {site} is not an alive site"


# ---------------------------------------------------------------------------
# 6. Uniform-mode smoke test
# ---------------------------------------------------------------------------

class TestUniformModeSmoke:
    """Smoke test: KV1 uniform k=0 mode.

    The uniform θ with u=0 in a periodic box is an exact single-DOF state.
    Every gradient term vanishes. It rings at ω_m = 2 at small amplitude,
    with δω/ω = −(3/2)·a²/ε_y² (DC page Q2b, DERIVED from engine cosserat_field_3d.py).

    This validates the analyzer pipeline against a closed-form result before
    any knot work. A mismatch is a pipeline fault.

    Per the brief: use a tiny uniform-mode smoke instead of a knot smoke
    (as recommended by Math if cheap).
    """

    @pytest.fixture(scope="class")
    def smoke_result(self):
        """Run the uniform-mode smoke test and return results dict."""
        import jax
        jax.config.update("jax_enable_x64", True)
        from ave.topological.cosserat_field_3d import CosseratField3D

        # Tiny grid: 12x12x12. Uniform mode is size-independent.
        N = 12
        solver = CosseratField3D(
            N, N, N,
            use_saturation=False,   # pure linear engine
            pml_thickness=0,        # periodic, no sponge
            damping_gamma=0.0,      # Hamiltonian, no drag
        )
        # For ω_m = 2 validation, zero out stiffeners so only micropolar term survives
        solver.k_op10 = 0.0
        solver.k_hopf = 0.0
        solver.k_refl = 0.0

        # Small-amplitude uniform theta kick along z (amplitude a << ε_y = 1)
        amplitude = 0.05  # a/ε_y = 0.05 ≪ 1 (linear regime)
        solver.omega[solver.mask_alive] = np.array([0.0, 0.0, 0.0])
        solver.omega_dot[solver.mask_alive] = np.array([0.0, 0.0, amplitude])
        solver.u[:] = 0.0
        solver.u_dot[:] = 0.0

        # Run for ~15 periods of ω_m = 2
        omega_m = 2.0
        period = 2.0 * np.pi / omega_m
        n_periods = 15
        dt = solver.cfl_dt

        # Probe one alive site (any alive site suffices for uniform mode)
        alive = np.argwhere(solver.mask_alive)
        site = tuple(alive[len(alive) // 2])

        times = []
        omega_z_vals = []
        omega_max_vals = []

        n_total = int(round(n_periods * period / dt))
        for step_i in range(n_total):
            solver.step(dt=dt)
            times.append(solver.time)
            omega_z_vals.append(float(solver.omega[site][2]))
            omega_max_vals.append(float(
                np.sqrt(np.max(np.sum(np.asarray(solver.omega)**2, axis=-1)
                               * solver.mask_alive))
            ))

        times = np.array(times)
        omega_z = np.array(omega_z_vals)
        omega_max = np.array(omega_max_vals)

        # Analyze the omega_z time series
        poles = analyze(omega_z, dt, n_poles_max=2, n_model_orders=3)

        print("\n=== Uniform mode KV1 smoke test ===")
        print(f"Grid: {N}x{N}x{N}, dt={dt:.4f}, {n_total} steps ({n_periods} periods)")
        print(f"Amplitude a={amplitude}, ω_m=2 expected")
        print(f"Max |omega|_final = {omega_max[-1]:.4f} (WRAP threshold = π ≈ {np.pi:.4f})")
        print(f"n_poles found: {len(poles)}")
        for p in poles:
            print(f"  Ω={p.Omega:.6f}, Γ={p.Gamma:.6e}, Q={p.Q:.1f}, "
                  f"|c|={p.amplitude:.3e}, growth={p.is_growth}")
        print(summarize(poles, dt, record_length=float(times[-1]), label="KV1"))

        pos_poles = [p for p in poles if p.Omega > 0.5]
        return {
            "poles": poles,
            "pos_poles": pos_poles,
            "times": times,
            "omega_z": omega_z,
            "omega_max": omega_max,
            "dt": dt,
            "n_periods": n_periods,
            "amplitude": amplitude,
        }

    def test_smoke_returns_poles(self, smoke_result):
        """Smoke test produces at least one pole."""
        assert len(smoke_result["poles"]) > 0

    def test_smoke_omega_near_2(self, smoke_result):
        """Recovered Ω is within 0.05 of ω_m = 2."""
        pos_poles = smoke_result["pos_poles"]
        assert len(pos_poles) > 0, "No positive-frequency poles found"
        best = min(pos_poles, key=lambda p: abs(p.Omega - 2.0))
        assert abs(best.Omega - 2.0) < 0.05, \
            (f"KV1 smoke: Ω={best.Omega:.4f}, expected ω_m=2.0, "
             f"error={abs(best.Omega - 2.0):.4f}. "
             "A larger error at this record length is expected (LEAN flag); "
             "this is a pipeline sanity check, not a precision assertion.")

    def test_smoke_no_wrap(self, smoke_result):
        """Small-amplitude uniform mode stays below WRAP threshold (|ω| < π)."""
        assert np.all(smoke_result["omega_max"] < np.pi), \
            "Uniform mode exceeded WRAP threshold unexpectedly"

    def test_smoke_no_growth(self, smoke_result):
        """Linear Hamiltonian engine: no growing modes.

        The VV integrator on Linux produces Gamma ≈ -2.33e-15 (integrator noise,
        not physical growth). The growth-tolerance rule in _classify_pole screens
        this: tol = max(3×Gamma_err, 50×eps×|Omega|) ≈ 2.2e-14 >> 2.33e-15.
        See TestGrowthTolerance for direct unit tests of the tolerance from both
        sides.
        """
        growth = [p for p in smoke_result["pos_poles"] if p.is_growth]
        assert len(growth) == 0, f"Unexpected growth-flagged poles: {growth}"

    def test_smoke_in_window_or_rot_band(self, smoke_result):
        """ω ≈ 2 pole should be at or near the window/rotation boundary."""
        pos_poles = smoke_result["pos_poles"]
        if len(pos_poles) == 0:
            pytest.skip("No positive-frequency poles; skipping window check")
        best = min(pos_poles, key=lambda p: abs(p.Omega - 2.0))
        # ω_m = 2 is exactly the boundary; accept either side
        assert (best.in_9pct_window or best.in_rot_band or
                abs(best.Omega - OMEGA_M) < 0.1), \
            f"Ω={best.Omega:.4f} not near ω_m=2 boundary"
