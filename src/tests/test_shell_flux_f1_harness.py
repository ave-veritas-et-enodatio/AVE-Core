"""Unit tests for the shell-flux F1 measurement harness.

Tests (no Mac run, no long simulation):
  - Frozen tol math
  - Q/A fit correctness
  - Empty-grid sanity + identity sanity (G5)
  - Force-stop classification via synthetic stop_info
  - PASS / KILL / INCONCLUSIVE / OUT_OF_SCOPE / RECEIPT_ONLY verdict logic
  - G1: injected-force positive control (replaces test_kill_f1_large_q)
  - G2: None energy slope gives INCONCLUSIVE
  - G9: vacuum drain gives INCONCLUSIVE
  - G10: receipt_only=True returns RECEIPT_ONLY

FREEZE: PROOF-LADDER-shell-flux-zero-2026-10-06.md (Math ACK 2026-10-06)
Gaps:   RULING-shell-flux-F1-run-02fc9794-2026-10-06.md §5 (G1–G12)
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
    GRAD_NORM_SWITCH_F,
    K_TOL,
    MAX_ITER,
    SEED_STRAIN_FENCE,
    VACUUM_E_FLOOR_FRAC,
    VACUUM_OMEGA_FLOOR_FRAC,
    Verdict,
    _energy_slope_pct,
    compute_verdict,
    fit_qa,
    frozen_tol,
    make_engine_32_periodic,
    make_engine_64_periodic,
    run_empty_grid_sanity,
    run_identity_sanity,
    run_injected_force_control,
)


# ── helpers ───────────────────────────────────────────────────────────────────

def _make_stop_ok(f_max: float = 5e-9, energy_history: list | None = None) -> dict:
    """Synthetic stop_info representing a successful force-stop."""
    if energy_history is None:
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
    """Synthetic BallSumResult; phi_norm defaults to 1% of tol."""
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
        assert 2e-4 < tol < 5e-4

    def test_budget_r24(self):
        tol = frozen_tol(29_000, F_STOP)
        assert 5e-4 < tol < 1.5e-3


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
        # 200 entries, all -10.0: slope = 0.0 (not None — history is long enough)
        hist = [-10.0] * 200
        result = _energy_slope_pct(hist)
        assert result == 0.0

    def test_5pct_drop(self):
        hist = [-10.0] * 100 + list(np.linspace(-10.0, -10.5, 101))
        slope = _energy_slope_pct(hist)
        assert slope is not None
        assert abs(slope - 5.0) < 0.1

    def test_0p5pct_drop(self):
        hist = [-10.0] * 100 + list(np.linspace(-10.0, -10.05, 101))
        slope = _energy_slope_pct(hist)
        assert slope is not None
        assert abs(slope - 0.5) < 0.05

    def test_too_short_history_returns_none(self):
        # G2: fewer than window+1 entries → returns None (not 0.0)
        assert _energy_slope_pct([-10.0] * 50) is None

    def test_empty_history_returns_none(self):
        # G2: empty history → None
        assert _energy_slope_pct([]) is None

    def test_tiny_e_start_returns_none(self):
        # G2: |E_start| below 1e-12 floor → None
        hist = [1e-15] * 200
        assert _energy_slope_pct(hist) is None

    def test_rising_energy_is_negative_slope(self):
        hist = [-9.0] * 100 + list(np.linspace(-9.0, -8.5, 101))
        slope = _energy_slope_pct(hist)
        assert slope is not None
        assert slope < 0.0


# ── empty-grid sanity + identity sanity (G5) ─────────────────────────────────

class TestEmptyGridSanity:
    """G5: Φ on a zero-initialized 64³ periodic engine is machine-zero."""

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


class TestIdentitySanity:
    """G5: random (u, ω) gives global sum of ∂E/∂u = 0 (translation identity)."""

    def test_global_sum_near_zero(self):
        result = run_identity_sanity(seed=42)
        assert result["passes"], (
            f"global_norm={result['global_norm']:.3e} > 1e-12 — "
            f"translation identity violated"
        )

    def test_global_norm_bound(self):
        result = run_identity_sanity(seed=0)
        assert result["global_norm"] <= 1e-12

    def test_global_sum_shape(self):
        result = run_identity_sanity(seed=1)
        assert result["global_sum"].shape == (3,)


# ── force-stop classification ─────────────────────────────────────────────────

class TestForceStopClassification:
    """Verdict depends on stop_reason and n_consec; synthetic stop_info only."""

    def test_no_force_stop_gives_inconclusive(self):
        stop = _make_stop_ok()
        stop["stop_reason"] = "max_iter"
        stop["n_consec"] = 0
        v, _ = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE

    def test_force_stop_exactly_3_consec_receipt_only(self):
        # G10: self-bound knot path → RECEIPT_ONLY (not PASS_F1)
        stop = _make_stop_ok()
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, stop["f_max"])
        v, notes = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII,
                                   receipt_only=True)
        assert v == Verdict.RECEIPT_ONLY
        assert any("receipt" in n.lower() for n in notes)

    def test_force_stop_exactly_3_consec_pass_f1_when_not_receipt(self):
        # receipt_only=False restores legacy PASS_F1 path
        stop = _make_stop_ok()
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, stop["f_max"])
        v, _ = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII,
                               receipt_only=False)
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
        hist = [-10.0] * 100 + list(np.linspace(-10.0, -10.5, 101))
        stop = _make_stop_ok(energy_history=hist)
        v, notes = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE
        assert any("energy" in n.lower() for n in notes)

    def test_energy_slope_below_1pct_gives_receipt_only(self):
        # G10: 0.5% drop → not INCONCLUSIVE on energy axis, receipt_only=True → RECEIPT_ONLY
        hist = [-10.0] * 100 + list(np.linspace(-10.0, -10.05, 101))
        stop = _make_stop_ok(energy_history=hist)
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, stop["f_max"])
        v, _ = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII,
                               receipt_only=True)
        assert v == Verdict.RECEIPT_ONLY

    def test_none_slope_gives_inconclusive(self):
        # G2: short accepted-step history → slope is None → INCONCLUSIVE
        stop = _make_stop_ok(energy_history=[-10.0] * 10)  # < window+1 = 101
        v, notes = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE
        assert any("slope" in n.lower() or "unmeasurable" in n.lower() for n in notes)


# ── verdict logic ─────────────────────────────────────────────────────────────

class TestVerdictLogic:
    def test_receipt_only_default(self):
        """Default receipt_only=True → RECEIPT_ONLY when all phi pass."""
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        balls = _small_balls(radii, f_max)
        tol_rmin = frozen_tol(balls[0].n_ball, f_max)
        v, notes = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, radii)
        assert v == Verdict.RECEIPT_ONLY
        assert any("receipt" in n.lower() for n in notes)
        assert any("todo" in n.lower() for n in notes)

    def test_pass_f1_clean(self):
        # receipt_only=False → legacy PASS_F1
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        balls = _small_balls(radii, f_max)
        tol_rmin = frozen_tol(balls[0].n_ball, f_max)
        tol_rmax = frozen_tol(balls[-1].n_ball, f_max)
        Q_norm = tol_rmin * 0.01
        A_norm = tol_rmax / (max(radii)**3) * 0.01
        v, notes = compute_verdict(stop, balls, Q_norm, A_norm, radii,
                                   receipt_only=False)
        assert v == Verdict.PASS_F1
        assert any("clean" in n.lower() for n in notes)

    def test_pass_f1_primary_when_q_fails_clean(self):
        """Primary PASS sufficient even if Q > tol(r_min) — receipt_only=False."""
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        balls = _small_balls(radii, f_max)
        tol_rmin = frozen_tol(balls[0].n_ball, f_max)
        Q_norm = tol_rmin * 2.0
        v, notes = compute_verdict(stop, balls, Q_norm, 0.0, radii, receipt_only=False)
        assert v == Verdict.PASS_F1
        assert any("primary" in n.lower() for n in notes)

    def test_kill_f1_large_q(self):
        # KILL_F1 path still reachable with receipt_only=False and not-all-phi-pass
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        n_ball_min = int(2 / 3 * np.pi * radii[0]**3)
        tol_min = frozen_tol(n_ball_min, f_max)
        Q_norm = tol_min * 100.0
        balls = [_ball(r, f_max, Q_norm) for r in radii]
        v, notes = compute_verdict(stop, balls, Q_norm, 0.0, radii, receipt_only=False)
        assert v == Verdict.KILL_F1
        assert any("kill" in n.lower() for n in notes)

    def test_inconclusive_no_force_stop(self):
        stop = _make_stop_ok()
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
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        n_ball_max = int(2 / 3 * np.pi * radii[-1]**3)
        tol_max = frozen_tol(n_ball_max, f_max)
        A_norm = tol_max * 5.0 / radii[-1]**3
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
        Q_norm = tol_rmin * 0.001
        v, _ = compute_verdict(stop, balls, Q_norm, A_norm, radii)
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
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        tol_min = frozen_tol(int(2 / 3 * np.pi * radii[0]**3), f_max)
        Q_norm = tol_min * 100.0
        balls = [_ball(r, f_max, Q_norm) for r in radii]
        v, _ = compute_verdict(stop, balls, Q_norm, 0.0, radii, has_pins=True)
        assert v == Verdict.OUT_OF_SCOPE

    def test_tol_uses_measured_fmax_not_fstop(self):
        f_max_tight = 5e-9
        f_max_loose = 5e-7
        N = int(2 / 3 * np.pi * DEFAULT_RADII[0]**3)
        assert frozen_tol(N, f_max_loose) > frozen_tol(N, f_max_tight)

    def test_verdict_enum_strings(self):
        assert Verdict.PASS_F1.value == "PASS_F1"
        assert Verdict.KILL_F1.value == "KILL_F1"
        assert Verdict.INCONCLUSIVE.value == "INCONCLUSIVE"
        assert Verdict.OUT_OF_SCOPE.value == "OUT_OF_SCOPE"
        assert Verdict.RECEIPT_ONLY.value == "RECEIPT_ONLY"
        assert Verdict.MONOPOLE_DETECTED.value == "MONOPOLE_DETECTED"


# ── G9: vacuum-PASS trap ──────────────────────────────────────────────────────

class TestVacuumPassTrap:
    """G9: a state that drained to vacuum cannot PASS or give RECEIPT_ONLY."""

    def _make_drained_stop(self, f_max: float = 5e-9) -> dict:
        """Stop_info representing a force-stopped but drained state."""
        stop = _make_stop_ok(f_max)
        stop["E_seed"] = 100.0          # high seed energy
        stop["peak_omega_seed"] = 1.0   # high seed omega
        stop["energy"] = 0.01           # << 0.5 * E_seed
        stop["peak_omega"] = 0.001      # << 0.5 * peak_omega_seed
        return stop

    def test_drained_energy_gives_inconclusive(self):
        stop = self._make_drained_stop()
        balls = _small_balls()
        v, notes = compute_verdict(stop, balls, 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE
        assert any("vacuum" in n.lower() or "drain" in n.lower() for n in notes)

    def test_drained_omega_gives_inconclusive(self):
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        stop["E_seed"] = 100.0
        stop["peak_omega_seed"] = 1.0
        stop["energy"] = 80.0           # fine (not energy-drained)
        stop["peak_omega"] = 0.001      # drained on omega axis
        balls = _small_balls()
        v, notes = compute_verdict(stop, balls, 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE
        assert any("vacuum" in n.lower() or "drain" in n.lower() for n in notes)

    def test_healthy_knot_not_blocked(self):
        # E_stop >= 0.5*E_seed and peak_omega >= 0.5*peak_seed → not drained
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        stop["E_seed"] = 100.0
        stop["peak_omega_seed"] = 1.0
        stop["energy"] = 60.0           # > 50 = 0.5 * 100
        stop["peak_omega"] = 0.6        # > 0.5 = 0.5 * 1.0
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, f_max)
        v, _ = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII,
                               receipt_only=True)
        assert v == Verdict.RECEIPT_ONLY

    def test_no_seed_values_no_vacuum_check(self):
        # If E_seed/peak_omega_seed absent, vacuum check is skipped
        stop = _make_stop_ok()  # no E_seed / peak_omega_seed keys
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, stop["f_max"])
        v, _ = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII,
                               receipt_only=True)
        assert v == Verdict.RECEIPT_ONLY


# ── G1: injected-force positive control ──────────────────────────────────────

class TestInjectedForceControl:
    """G1: replaces test_kill_f1_large_q; tests a control that can actually fail.

    Uses 32³ grid with small radii (3,4,5).  64³ exceeds the 300s test timeout;
    32³ reaches F_STOP_CONTROL = 1e-6 in ~500 steps (~11s total including JIT).
    The K4 periodic alive mask has an acoustic long-wavelength mode that stalls
    gradient descent near 8e-7 for F_STOP=1e-8, but F_STOP_CONTROL=1e-6 is
    reachable and sufficient for Q_norm to converge within 1% of f0_norm.
    On a periodic grid the translation identity Σ(dE/du)=0 creates a uniform
    residual -f0/N_alive; the harness removes it via mean-subtraction so that
    the centered gradient converges.  The Q/A fit absorbs the r³ volume correction
    into A; Q_norm ≈ f0_norm within ~1% at force-stop.
    """

    @classmethod
    def _engine_and_result(cls):
        """Shared fixture: 32³ + f0=(0,0,1e-3) + small radii (cached — runs once)."""
        if not hasattr(cls, "_cached_result"):
            engine = make_engine_32_periodic(use_saturation=True)  # 64³ too slow
            f0 = (0.0, 0.0, 1e-3)
            radii = (3.0, 4.0, 5.0)
            result = run_injected_force_control(
                engine, f0=f0, radii=radii, max_iter=1000
            )
            cls._cached_result = (engine, f0, radii, result)
        return cls._cached_result

    def test_center_site_is_alive(self):
        """The injected site must be an alive site (fast — no relaxation needed)."""
        engine = make_engine_32_periodic(use_saturation=True)
        result = run_injected_force_control(
            engine, f0=(0.0, 0.0, 1e-3), radii=(3.0, 4.0, 5.0), max_iter=1
        )
        ci, cj, ck = result["center_site"]
        assert engine.mask_alive[ci, cj, ck], "Center site is not alive"

    def test_monopole_detected(self):
        """32³ engine with injected force → MONOPOLE_DETECTED."""
        _, _, _, result = self._engine_and_result()
        assert result["verdict"] == Verdict.MONOPOLE_DETECTED, (
            f"Expected MONOPOLE_DETECTED, got {result['verdict']}. "
            f"Notes: {result['notes']}"
        )

    def test_q_norm_near_f0_norm(self):
        """Q_norm ≈ f0_norm (Q/A fit absorbs volume correction into A; <0.01% error on 32³)."""
        _, f0, _, result = self._engine_and_result()
        f0_norm = float(np.linalg.norm(np.asarray(f0)))
        assert abs(result["Q_norm"] - f0_norm) < f0_norm * 0.01, (
            f"Q_norm={result['Q_norm']:.3e} not near f0_norm={f0_norm:.3e}"
        )

    def test_a_term_small_relative_to_q(self):
        """A*r_max³ < 10% of Q_norm (monopole, not volume-dominated)."""
        _, _, radii, result = self._engine_and_result()
        r_max = max(radii)
        a_r3 = result["A_norm"] * r_max**3
        assert a_r3 < result["Q_norm"] * 0.1, (
            f"A*r³={a_r3:.3e} not << Q_norm={result['Q_norm']:.3e}"
        )

    def test_force_stop_reached(self):
        """Control must reach force-stop at F_STOP_CONTROL=1e-6, not max_iter."""
        _, _, _, result = self._engine_and_result()
        assert result["stop_reason"] == "force_stop", (
            f"Expected force_stop, got {result['stop_reason']!r}"
        )
