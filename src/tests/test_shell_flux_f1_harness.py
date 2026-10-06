"""Unit tests for the shell-flux F1 measurement harness.

Tests (no Mac run, no long simulation):
  - Frozen tol math
  - Q/A fit correctness
  - Empty-grid sanity (Φ ~ 0 on zero state)
  - Force-stop classification via synthetic stop_info
  - PASS / KILL / INCONCLUSIVE / OUT_OF_SCOPE verdict logic with synthetic Φ/Q/A

FREEZE: PROOF-LADDER-shell-flux-zero-2026-10-06.md (Math ACK 2026-10-06)
Plan:   HARNESS-PLAN-shell-flux-F1-2026-10-06.md
"""
from __future__ import annotations

import os
import sys

import numpy as np
import pytest

# ── import harness ────────────────────────────────────────────────────────────
_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.join(_HERE, "..", "scripts", "verify")
if _VERIFY not in sys.path:
    sys.path.insert(0, os.path.abspath(_VERIFY))

from shell_flux_f1_harness import (  # noqa: E402
    BallSumResult,
    C_TOL,
    CONSEC_REQUIRED,
    DEFAULT_RADII,
    EPS_MACHINE,
    F_STOP,
    K_TOL,
    Verdict,
    _energy_slope_pct,
    compute_verdict,
    fit_qa,
    frozen_tol,
    run_empty_grid_sanity,
)


# ── helpers ───────────────────────────────────────────────────────────────────

def _make_stop_ok(f_max: float = 5e-9, energy_history: list | None = None) -> dict:
    """Synthetic stop_info representing a successful force-stop."""
    if energy_history is None:
        # Flat history → 0 % drop
        energy_history = [-10.0] * 200
    return {
        "stop_reason": "force_stop",
        "n_consec": CONSEC_REQUIRED,
        "f_max": f_max,
        "f_rms": f_max * 0.5,
        "energy": energy_history[-1],
        "energy_history": energy_history,
        "crossings": 3,
        "peak_omega": 0.5,
    }


def _ball(r: float, f_max: float, phi_norm_override: float | None = None) -> BallSumResult:
    """Synthetic BallSumResult; phi_norm defaults to 1 % of tol."""
    n_ball = int(2 / 3 * np.pi * r**3)
    tol = frozen_tol(n_ball, f_max)
    pn = phi_norm_override if phi_norm_override is not None else tol * 0.01
    return BallSumResult(
        radius=r,
        n_ball=n_ball,
        phi_vec=np.array([pn, 0.0, 0.0]),
        phi_norm=pn,
        tol=tol,
        passes=(pn < tol),
    )


def _small_balls(
    radii: tuple = DEFAULT_RADII,
    f_max: float = 5e-9,
    phi_norm_override: float | None = None,
) -> list:
    return [_ball(r, f_max, phi_norm_override) for r in radii]


# ── frozen tol ────────────────────────────────────────────────────────────────

class TestFrozenTol:
    def test_formula_exact(self):
        N, F = 3600, 1e-8
        expected = K_TOL * (N * F + C_TOL * EPS_MACHINE * np.sqrt(N))
        assert abs(frozen_tol(N, F) - expected) < 1e-25

    def test_zero_fmax_gives_positive(self):
        tol = frozen_tol(1000, 0.0)
        assert tol > 0.0
        expected = K_TOL * C_TOL * EPS_MACHINE * np.sqrt(1000)
        assert abs(tol - expected) < 1e-30

    def test_k3_not_k5(self):
        """Freeze uses k=3, not tone k=5."""
        N, F = 10_000, 1e-8
        tol3 = frozen_tol(N, F)
        tol5_val = 5 * (N * F + C_TOL * EPS_MACHINE * np.sqrt(N))
        assert abs(tol3 / tol5_val - 3 / 5) < 1e-12

    def test_scales_with_n_ball(self):
        F = 1e-8
        assert frozen_tol(10_000, F) > frozen_tol(1_000, F)

    def test_budget_r12(self):
        """Budget example from ladder table: r=12, N≈3600, F_max=F_stop."""
        tol = frozen_tol(3600, F_STOP)
        assert 8e-5 < tol < 1.5e-4  # ladder: ≈ 1.1×10⁻⁴

    def test_budget_r18(self):
        tol = frozen_tol(12_000, F_STOP)
        assert 2e-4 < tol < 5e-4  # ladder: ≈ 3.7×10⁻⁴

    def test_budget_r24(self):
        tol = frozen_tol(29_000, F_STOP)
        assert 5e-4 < tol < 1.5e-3  # ladder: ≈ 8.7×10⁻⁴


# ── Q/A fit ───────────────────────────────────────────────────────────────────

class TestFitQA:
    def test_pure_monopole(self):
        radii = list(DEFAULT_RADII)
        Q_true = np.array([0.1, -0.05, 0.02])
        phi_vecs = [Q_true.copy() for _ in radii]
        Q_fit, A_fit = fit_qa(radii, phi_vecs)
        np.testing.assert_allclose(Q_fit, Q_true, atol=1e-12)
        np.testing.assert_allclose(A_fit, np.zeros(3), atol=1e-12)

    def test_pure_volume(self):
        radii = list(DEFAULT_RADII)
        A_true = np.array([0.0, 0.0, 1e-5])
        phi_vecs = [A_true * r**3 for r in radii]
        Q_fit, A_fit = fit_qa(radii, phi_vecs)
        np.testing.assert_allclose(Q_fit, np.zeros(3), atol=1e-10)
        np.testing.assert_allclose(A_fit, A_true, atol=1e-15)

    def test_mixed_qa(self):
        radii = list(DEFAULT_RADII)
        Q_true = np.array([1e-5, 0.0, -2e-5])
        A_true = np.array([0.0, 3e-8, 0.0])
        phi_vecs = [Q_true + A_true * r**3 for r in radii]
        Q_fit, A_fit = fit_qa(radii, phi_vecs)
        np.testing.assert_allclose(Q_fit, Q_true, atol=1e-12)
        np.testing.assert_allclose(A_fit, A_true, atol=1e-20)

    def test_zero_phi(self):
        radii = list(DEFAULT_RADII)
        phi_vecs = [np.zeros(3) for _ in radii]
        Q_fit, A_fit = fit_qa(radii, phi_vecs)
        np.testing.assert_allclose(Q_fit, np.zeros(3), atol=1e-30)
        np.testing.assert_allclose(A_fit, np.zeros(3), atol=1e-30)

    def test_four_radii(self):
        """fit_qa handles more than 3 radii."""
        radii = [10.0, 15.0, 20.0, 25.0]
        Q_true = np.array([0.001, 0.0, -0.002])
        A_true = np.array([0.0, 5e-7, 0.0])
        phi_vecs = [Q_true + A_true * r**3 for r in radii]
        Q_fit, A_fit = fit_qa(radii, phi_vecs)
        np.testing.assert_allclose(Q_fit, Q_true, atol=1e-10)
        np.testing.assert_allclose(A_fit, A_true, atol=1e-18)


# ── energy slope ─────────────────────────────────────────────────────────────

class TestEnergySlopePct:
    def test_flat(self):
        hist = [-10.0] * 200
        assert _energy_slope_pct(hist) == 0.0

    def test_5pct_drop(self):
        # Energy: flat at -10, then drops to -10.5 over 101 steps
        hist = [-10.0] * 100 + list(np.linspace(-10.0, -10.5, 101))
        slope = _energy_slope_pct(hist)
        assert abs(slope - 5.0) < 0.1

    def test_0p5pct_drop(self):
        hist = [-10.0] * 100 + list(np.linspace(-10.0, -10.05, 101))
        slope = _energy_slope_pct(hist)
        assert abs(slope - 0.5) < 0.05

    def test_too_short_history(self):
        # Fewer than window+1 entries → returns 0
        assert _energy_slope_pct([-10.0] * 50) == 0.0

    def test_rising_energy_is_negative_slope(self):
        # If energy RISES, slope < 0 (not "dropping")
        hist = [-9.0] * 100 + list(np.linspace(-9.0, -8.5, 101))  # less negative
        slope = _energy_slope_pct(hist)
        assert slope < 0.0


# ── empty-grid sanity ─────────────────────────────────────────────────────────

class TestEmptyGridSanity:
    """Φ on a zero-initialized engine is machine-zero (gradient = 0 exactly)."""

    def test_passes_float_tol(self):
        result = run_empty_grid_sanity(radius=6.0)
        assert result["passes_sanity"], (
            f"phi_norm={result['phi_norm']:.3e} >= float_tol={result['float_tol']:.3e}"
        )

    def test_phi_is_machine_zero(self):
        result = run_empty_grid_sanity(radius=6.0)
        assert result["phi_norm"] < 1e-14, (
            f"Expected machine zero, got phi_norm={result['phi_norm']}"
        )

    def test_n_ball_positive(self):
        result = run_empty_grid_sanity(radius=6.0)
        assert result["n_ball"] > 0

    def test_phi_vec_shape(self):
        result = run_empty_grid_sanity(radius=6.0)
        assert result["phi_vec"].shape == (3,)


# ── force-stop classification ─────────────────────────────────────────────────

class TestForceStopClassification:
    """Verdict depends on stop_reason and n_consec; synthetic stop_info only."""

    def test_no_force_stop_gives_inconclusive(self):
        stop = _make_stop_ok()
        stop["stop_reason"] = "max_iter"
        stop["n_consec"] = 0
        v, _ = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE

    def test_force_stop_exactly_3_consec_passes(self):
        stop = _make_stop_ok()
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, stop["f_max"])
        v, _ = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII)
        assert v == Verdict.PASS_F1

    def test_force_stop_2_consec_inconclusive(self):
        stop = _make_stop_ok()
        stop["n_consec"] = 2
        v, _ = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE

    def test_lr_underflow_inconclusive(self):
        stop = _make_stop_ok()
        stop["stop_reason"] = "lr_underflow"
        stop["n_consec"] = 0
        v, _ = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE

    def test_untied_inconclusive(self):
        stop = _make_stop_ok()
        stop["stop_reason"] = "untied"
        stop["n_consec"] = 0
        v, _ = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE

    def test_energy_slope_above_1pct_inconclusive(self):
        # 5 % drop over last 100 steps at stop → INCONCLUSIVE
        hist = [-10.0] * 100 + list(np.linspace(-10.0, -10.5, 101))
        stop = _make_stop_ok(energy_history=hist)
        v, notes = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE
        assert any("energy" in n.lower() for n in notes)

    def test_energy_slope_below_1pct_not_inconclusive_on_this_axis(self):
        # 0.5 % drop → does not trigger energy-slope INCONCLUSIVE
        hist = [-10.0] * 100 + list(np.linspace(-10.0, -10.05, 101))
        stop = _make_stop_ok(energy_history=hist)
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, stop["f_max"])
        v, _ = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII)
        assert v == Verdict.PASS_F1


# ── verdict logic ─────────────────────────────────────────────────────────────

class TestVerdictLogic:
    def test_pass_f1_clean(self):
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        balls = _small_balls(radii, f_max)  # phi = 1 % of tol → passes
        tol_rmin = frozen_tol(balls[0].n_ball, f_max)
        tol_rmax = frozen_tol(balls[-1].n_ball, f_max)
        Q_norm = tol_rmin * 0.01
        A_norm = tol_rmax / (max(radii)**3) * 0.01
        v, notes = compute_verdict(stop, balls, Q_norm, A_norm, radii)
        assert v == Verdict.PASS_F1
        assert any("clean" in n.lower() for n in notes)

    def test_pass_f1_primary_when_q_fails_clean(self):
        """Primary PASS sufficient even if Q > tol(r_min)."""
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        balls = _small_balls(radii, f_max)  # all phi < tol
        tol_rmin = frozen_tol(balls[0].n_ball, f_max)
        Q_norm = tol_rmin * 2.0    # Q > tol(r_min) — clean fails
        A_norm = 0.0
        v, notes = compute_verdict(stop, balls, Q_norm, A_norm, radii)
        assert v == Verdict.PASS_F1
        assert any("primary" in n.lower() for n in notes)

    def test_kill_f1_large_q(self):
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        n_ball_min = int(2 / 3 * np.pi * radii[0]**3)
        tol_min = frozen_tol(n_ball_min, f_max)
        Q_norm = tol_min * 100.0   # 100× tol → KILL
        # phi_norm = Q_norm at each r (constant monopole → all fail tol)
        balls = [_ball(r, f_max, Q_norm) for r in radii]
        A_norm = 0.0
        v, notes = compute_verdict(stop, balls, Q_norm, A_norm, radii)
        assert v == Verdict.KILL_F1
        assert any("kill" in n.lower() for n in notes)

    def test_inconclusive_no_force_stop(self):
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        stop["stop_reason"] = "max_iter"
        stop["n_consec"] = 0
        v, _ = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE

    def test_inconclusive_energy_slope(self):
        hist = [-10.0] * 100 + list(np.linspace(-10.0, -10.5, 101))
        stop = _make_stop_ok(energy_history=hist)
        v, _ = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE

    def test_inconclusive_nonzero_a_tiny_q(self):
        """Nonzero A + tiny Q → INCONCLUSIVE if not all phi pass."""
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        n_ball_max = int(2 / 3 * np.pi * radii[-1]**3)
        tol_max = frozen_tol(n_ball_max, f_max)
        # A such that A*r_max³ = 5×tol_max (large volume term)
        A_norm = tol_max * 5.0 / radii[-1]**3
        # phi_norm = A_norm * r³ for each r — grows with r
        balls = []
        for r in radii:
            pn = A_norm * r**3
            n_ball = int(2 / 3 * np.pi * r**3)
            tol_r = frozen_tol(n_ball, f_max)
            balls.append(BallSumResult(
                radius=r, n_ball=n_ball,
                phi_vec=np.array([pn, 0.0, 0.0]),
                phi_norm=pn, tol=tol_r, passes=(pn < tol_r),
            ))
        tol_rmin = frozen_tol(balls[0].n_ball, f_max)
        Q_norm = tol_rmin * 0.001  # tiny Q
        v, notes = compute_verdict(stop, balls, Q_norm, A_norm, radii)
        # At r_max phi >> tol → not all pass → cannot be PASS_F1
        # Q << tol → not KILL
        # → INCONCLUSIVE
        assert v == Verdict.INCONCLUSIVE

    def test_out_of_scope_with_pins(self):
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        v, notes = compute_verdict(
            stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII, has_pins=True
        )
        assert v == Verdict.OUT_OF_SCOPE
        assert any("pins" in n.lower() for n in notes)

    def test_kill_requires_no_pins(self):
        """If has_pins=True, verdict is OUT_OF_SCOPE even if Q would be KILL."""
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        tol_min = frozen_tol(int(2 / 3 * np.pi * radii[0]**3), f_max)
        Q_norm = tol_min * 100.0
        balls = [_ball(r, f_max, Q_norm) for r in radii]
        v, _ = compute_verdict(stop, balls, Q_norm, 0.0, radii, has_pins=True)
        assert v == Verdict.OUT_OF_SCOPE

    def test_tol_uses_measured_fmax_not_fstop(self):
        """tol is built from measured f_max; a higher f_max gives looser tol."""
        f_max_tight = 5e-9   # well below F_STOP
        f_max_loose = 5e-7   # above F_STOP
        N = int(2 / 3 * np.pi * DEFAULT_RADII[0]**3)
        tol_tight = frozen_tol(N, f_max_tight)
        tol_loose = frozen_tol(N, f_max_loose)
        assert tol_loose > tol_tight

    def test_verdict_enum_strings(self):
        assert Verdict.PASS_F1.value == "PASS_F1"
        assert Verdict.KILL_F1.value == "KILL_F1"
        assert Verdict.INCONCLUSIVE.value == "INCONCLUSIVE"
        assert Verdict.OUT_OF_SCOPE.value == "OUT_OF_SCOPE"
