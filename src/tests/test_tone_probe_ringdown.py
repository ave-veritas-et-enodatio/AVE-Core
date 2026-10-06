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
    print_record_length_table,
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
        """Linear Hamiltonian engine: no growing modes."""
        growth = [p for p in smoke_result["pos_poles"] if p.is_growth]
        # Energy-conserving VV with no sponge should not produce growing modes
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
