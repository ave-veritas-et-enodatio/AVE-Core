"""Unit tests for the shell-flux F1 measurement harness.

Tests (no Mac run, no long simulation):
  - Frozen tol math
  - Q/A fit correctness
  - 4-class alive partition (B0)
  - Empty-grid sanity at frozen DEFAULT_RADII (G5/B4)
  - Identity sanity (G5)
  - Force-stop classification via synthetic stop_info
  - RECEIPT_ONLY / IDENTITY_VIOLATION / INCONCLUSIVE / OUT_OF_SCOPE verdict logic
  - G1: injected-force positive control (B1)
  - G2: None energy slope gives INCONCLUSIVE
  - G9: vacuum drain gives INCONCLUSIVE; vacuum box (E_seed≤1e-12) gives INCONCLUSIVE
  - G10: retired PASS_F1/KILL_F1; RECEIPT_ONLY and IDENTITY_VIOLATION
  - G11: u-only delegation (B2)
  - G8: untie tau tracking (B6)
  - G5/B5: cold default amplitude
  - G3/B7: platform line x64

FREEZE: PROOF-LADDER-shell-flux-zero-2026-10-06.md (Math ACK 2026-10-06)
Gaps:   RULING-shell-flux-F1-run-02fc9794-2026-10-06.md §5 (G1–G12)
Fix:    FIX-BRIEF-PR1064-2026-10-07.md (B0–B7)
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
    COLD_AMPLITUDE_SCALE,
    CONSEC_REQUIRED,
    DEFAULT_RADII,
    EPS_MACHINE,
    F_STOP,
    K_TOL,
    MAX_ITER,
    SEED_STRAIN_FENCE,
    VACUUM_E_FLOOR_FRAC,
    VACUUM_OMEGA_FLOOR_FRAC,
    Verdict,
    _energy_slope_pct,
    alive_classes,
    compute_verdict,
    control_verdict,
    estimate_lambda_max_u,
    fit_qa,
    force_stop_relax,
    frozen_tol,
    make_engine_32_periodic,
    make_engine_64_periodic,
    run_empty_grid_sanity,
    run_identity_sanity,
    run_injected_force_control,
    seed_cold_knot,
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
        assert _energy_slope_pct([-10.0] * 50) is None

    def test_empty_history_returns_none(self):
        assert _energy_slope_pct([]) is None

    def test_tiny_e_start_returns_none(self):
        hist = [1e-15] * 200
        assert _energy_slope_pct(hist) is None

    def test_rising_energy_is_negative_slope(self):
        hist = [-9.0] * 100 + list(np.linspace(-9.0, -8.5, 101))
        slope = _energy_slope_pct(hist)
        assert slope is not None
        assert slope < 0.0


# ── B0: 4-class alive partition ───────────────────────────────────────────────

class TestAliveClassesPartition:
    """B0 acceptance: 4-class structure, per-class zero mode, estimate_lambda_max_u."""

    def test_alive_classes_partition(self):
        """All four assertions from B0 acceptance in one test."""
        engine = make_engine_32_periodic(use_saturation=True)
        classes = alive_classes(engine)
        alive = engine.mask_alive
        N_alive = int(alive.sum())

        # Each class has exactly N_alive/4 sites; no alive site is -1
        for c in range(4):
            n_c = int((classes == c).sum())
            assert n_c == N_alive // 4, (
                f"class {c}: {n_c} sites, expected {N_alive // 4}"
            )
        assert not np.any((classes == -1) & alive), "alive site has class -1"

        # Per-class |Σ dE/du| < 1e-12 at a random state
        rng = np.random.default_rng(3)
        engine.u = (rng.standard_normal(engine.u.shape) * 0.01 * alive[..., None]).astype(np.float64)
        engine.omega = (rng.standard_normal(engine.omega.shape) * 0.01 * alive[..., None]).astype(np.float64)
        dE_du = np.asarray(engine.energy_gradient()[0])
        for c in range(4):
            class_sum = np.abs(dE_du[classes == c].sum(axis=0)).max()
            assert class_sum < 1e-12, f"class {c} |Σ dE/du| = {class_sum:.3e} >= 1e-12"

        # Shift class 0 by constant → energy unchanged to 1e-12 * max(E, 1)
        engine_fresh = make_engine_32_periodic(use_saturation=True)
        rng2 = np.random.default_rng(3)
        engine_fresh.u = (rng2.standard_normal(engine_fresh.u.shape) * 0.01 * engine_fresh.mask_alive[..., None]).astype(np.float64)
        engine_fresh.omega = (rng2.standard_normal(engine_fresh.omega.shape) * 0.01 * engine_fresh.mask_alive[..., None]).astype(np.float64)
        classes_fresh = alive_classes(engine_fresh)
        E0 = float(engine_fresh.total_energy())
        shift = np.array([1e-3, -2e-3, 5e-4])
        engine_fresh.u[classes_fresh == 0] += shift
        E1 = float(engine_fresh.total_energy())
        assert abs(E1 - E0) < 1e-12 * max(abs(E0), 1.0), (
            f"class-0 shift changed E by {abs(E1-E0):.3e}"
        )

        # estimate_lambda_max_u on fresh 32³ (ω=0) within 2% of 3.318
        engine_lam = make_engine_32_periodic(use_saturation=True)
        lam = estimate_lambda_max_u(engine_lam)
        assert abs(lam / 3.318 - 1.0) < 0.02, (
            f"λ_max = {lam:.4f}, expected ≈ 3.318 (within 2%)"
        )


# ── G5: empty-grid sanity + identity sanity ───────────────────────────────────

class TestEmptyGridSanity:
    """G5/B4: Φ on a zero-initialized 64³ periodic engine at DEFAULT_RADII."""

    def test_default_radii_structure(self):
        result = run_empty_grid_sanity()
        assert [d["r"] for d in result["per_radius"]] == [12.0, 18.0, 24.0]

    def test_n_ball_positive(self):
        result = run_empty_grid_sanity()
        for d in result["per_radius"]:
            assert d["n_ball"] > 0, f"r={d['r']}: n_ball=0"

    def test_phi_below_float_tol(self):
        result = run_empty_grid_sanity()
        for d in result["per_radius"]:
            assert d["phi_norm"] < d["float_tol"], (
                f"r={d['r']}: phi_norm={d['phi_norm']:.3e} >= float_tol={d['float_tol']:.3e}"
            )

    def test_passes_sanity(self):
        result = run_empty_grid_sanity()
        assert result["passes_sanity"]


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
        # G10: self-bound knot path → RECEIPT_ONLY
        stop = _make_stop_ok()
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, stop["f_max"])
        v, notes = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII)
        assert v == Verdict.RECEIPT_ONLY
        assert any("receipt" in n.lower() for n in notes)

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
        # 0.5% drop → not INCONCLUSIVE on energy axis → RECEIPT_ONLY
        hist = [-10.0] * 100 + list(np.linspace(-10.0, -10.05, 101))
        stop = _make_stop_ok(energy_history=hist)
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, stop["f_max"])
        v, _ = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII)
        assert v == Verdict.RECEIPT_ONLY

    def test_none_slope_gives_inconclusive(self):
        # G2: short accepted-step history → slope is None → INCONCLUSIVE
        stop = _make_stop_ok(energy_history=[-10.0] * 10)
        v, notes = compute_verdict(stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE
        assert any("slope" in n.lower() or "unmeasurable" in n.lower() for n in notes)


# ── verdict logic ─────────────────────────────────────────────────────────────

class TestVerdictLogic:
    def test_receipt_only_default(self):
        """All phi pass → RECEIPT_ONLY."""
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        balls = _small_balls(radii, f_max)
        tol_rmin = frozen_tol(balls[0].n_ball, f_max)
        v, notes = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, radii)
        assert v == Verdict.RECEIPT_ONLY
        assert any("receipt" in n.lower() for n in notes)
        assert any("todo" in n.lower() for n in notes)

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

    def test_nonzero_phi_gives_identity_violation(self):
        """B3: nonzero A + tiny Q → phi > tol at some radii → IDENTITY_VIOLATION."""
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
        # B3: all paths with phi >= tol at a force-stopped state → IDENTITY_VIOLATION
        assert v == Verdict.IDENTITY_VIOLATION

    def test_out_of_scope_with_pins(self):
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        v, notes = compute_verdict(
            stop, _small_balls(), 0.0, 0.0, DEFAULT_RADII, has_pins=True
        )
        assert v == Verdict.OUT_OF_SCOPE
        assert any("pins" in n.lower() for n in notes)

    def test_pins_out_of_scope_precedes_identity_check(self):
        """OUT_OF_SCOPE fires before identity check even when phi >> tol."""
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        tol_min = frozen_tol(int(2 / 3 * np.pi * radii[0]**3), f_max)
        Q_norm = tol_min * 100.0
        balls = [_ball(r, f_max, Q_norm) for r in radii]
        v, _ = compute_verdict(stop, balls, Q_norm, 0.0, radii, has_pins=True)
        assert v == Verdict.OUT_OF_SCOPE

    def test_identity_violation_label(self):
        """phi >> tol at force-stopped state → IDENTITY_VIOLATION (code/engine bug)."""
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        radii = DEFAULT_RADII
        n_ball_min = int(2 / 3 * np.pi * radii[0]**3)
        tol_min = frozen_tol(n_ball_min, f_max)
        Q_norm = tol_min * 100.0
        balls = [_ball(r, f_max, Q_norm) for r in radii]
        v, notes = compute_verdict(stop, balls, Q_norm, 0.0, radii)
        assert v == Verdict.IDENTITY_VIOLATION
        assert any(
            "identity" in n.lower() or "violation" in n.lower() or "bug" in n.lower()
            for n in notes
        )

    def test_tol_uses_measured_fmax_not_fstop(self):
        f_max_tight = 5e-9
        f_max_loose = 5e-7
        N = int(2 / 3 * np.pi * DEFAULT_RADII[0]**3)
        assert frozen_tol(N, f_max_loose) > frozen_tol(N, f_max_tight)

    def test_verdict_enum_strings(self):
        assert not hasattr(Verdict, "PASS_F1")
        assert not hasattr(Verdict, "KILL_F1")
        assert Verdict.INCONCLUSIVE.value == "INCONCLUSIVE"
        assert Verdict.OUT_OF_SCOPE.value == "OUT_OF_SCOPE"
        assert Verdict.RECEIPT_ONLY.value == "RECEIPT_ONLY"
        assert Verdict.MONOPOLE_DETECTED.value == "MONOPOLE_DETECTED"
        assert Verdict.IDENTITY_VIOLATION.value == "IDENTITY_VIOLATION"
        assert Verdict.NO_MONOPOLE.value == "NO_MONOPOLE"
        assert Verdict.CONTROL_FAIL.value == "CONTROL_FAIL"


# ── G9: vacuum-PASS trap ──────────────────────────────────────────────────────

class TestVacuumPassTrap:
    """G9: a state that drained to vacuum cannot PASS or give RECEIPT_ONLY."""

    def _make_drained_stop(self, f_max: float = 5e-9) -> dict:
        stop = _make_stop_ok(f_max)
        stop["E_seed"] = 100.0
        stop["peak_omega_seed"] = 1.0
        stop["energy"] = 0.01
        stop["peak_omega"] = 0.001
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
        stop["energy"] = 80.0
        stop["peak_omega"] = 0.001
        balls = _small_balls()
        v, notes = compute_verdict(stop, balls, 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE
        assert any("vacuum" in n.lower() or "drain" in n.lower() for n in notes)

    def test_healthy_knot_not_blocked(self):
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        stop["E_seed"] = 100.0
        stop["peak_omega_seed"] = 1.0
        stop["energy"] = 60.0
        stop["peak_omega"] = 0.6
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, f_max)
        v, _ = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII)
        assert v == Verdict.RECEIPT_ONLY

    def test_no_seed_values_no_vacuum_check(self):
        stop = _make_stop_ok()
        balls = _small_balls()
        tol_rmin = frozen_tol(balls[0].n_ball, stop["f_max"])
        v, _ = compute_verdict(stop, balls, tol_rmin * 0.01, 0.0, DEFAULT_RADII)
        assert v == Verdict.RECEIPT_ONLY

    def test_vacuum_box_inconclusive(self):
        """B7/G9: E_seed <= 1e-12 (A=0) → INCONCLUSIVE with 'vacuum' note."""
        f_max = 5e-9
        stop = _make_stop_ok(f_max)
        stop["E_seed"] = 0.0
        stop["peak_omega_seed"] = 0.0
        balls = _small_balls()
        v, notes = compute_verdict(stop, balls, 0.0, 0.0, DEFAULT_RADII)
        assert v == Verdict.INCONCLUSIVE
        assert any("vacuum" in n.lower() for n in notes)

    def test_vacuum_box_real_run_note(self):
        """M2/G9: real amplitude_scale=0.0 run → E_seed≤1e-12 → INCONCLUSIVE 'vacuum' note
        fires before slope gate (not 'slope unmeasurable')."""
        from shell_flux_f1_harness import measure_shell_flux
        engine = make_engine_32_periodic(use_saturation=True)
        seed_cold_knot(engine, R=6, r=2, amplitude_scale=0.0)
        result = measure_shell_flux(engine, radii=(4.0, 8.0, 12.0), max_iter=50)
        assert result.verdict == Verdict.INCONCLUSIVE
        assert "vacuum" in result.notes[0].lower()


# ── G1/B1: injected-force positive control ───────────────────────────────────

class TestInjectedForceControl:
    """G1 (B1): per-class projection, closed-form phi_exp, control_verdict."""

    # Cached fixture: 32³, f0=(0,0,1e-2), radii (4,8,12), max_iter=3000
    _cached: dict | None = None

    @classmethod
    def _get_result(cls) -> dict:
        if cls._cached is None:
            engine = make_engine_32_periodic(use_saturation=True)
            cls._cached = run_injected_force_control(
                engine,
                f0=(0.0, 0.0, 1e-2),
                radii=(4.0, 8.0, 12.0),
                max_iter=3000,
            )
        return cls._cached

    def test_center_site_is_alive(self):
        """The injected site must be alive (fast — max_iter=1)."""
        engine = make_engine_32_periodic(use_saturation=True)
        result = run_injected_force_control(
            engine, f0=(0.0, 0.0, 1e-2), radii=(4.0, 8.0, 12.0), max_iter=1
        )
        ci, cj, ck = result["center_site"]
        assert engine.mask_alive[ci, cj, ck], "Center site is not alive"

    def test_control_reaches_f_stop(self):
        result = self._get_result()
        assert result["stop_reason"] == "force_stop", (
            f"Expected force_stop, got {result['stop_reason']!r}"
        )
        assert result["f_max"] < 1e-8, f"f_max={result['f_max']:.3e} not < 1e-8"

    def test_control_monopole_detected(self):
        result = self._get_result()
        assert result["verdict"] == Verdict.MONOPOLE_DETECTED, (
            f"Expected MONOPOLE_DETECTED, got {result['verdict']}. "
            f"Notes: {result['notes']}"
        )

    def test_control_phi_matches_class_formula(self):
        result = self._get_result()
        for i, (r, ball, phi_exp, tol) in enumerate(
            zip((4.0, 8.0, 12.0), result["ball_results"],
                result["phi_exps"], result["tols"])
        ):
            phi_vec = np.asarray(ball.phi_vec)
            phi_exp = np.asarray(phi_exp)
            resid = float(np.linalg.norm(phi_vec - phi_exp))
            assert resid < tol, (
                f"r={r}: resid={resid:.3e} >= tol={tol:.3e}"
            )
            # z-component ratio within 0.1%
            if abs(phi_exp[2]) > 1e-10:
                ratio = abs(phi_vec[2] / phi_exp[2] - 1.0)
                assert ratio < 1e-3, (
                    f"r={r}: phi_z/phi_exp_z ratio error = {ratio:.3e}"
                )

    def test_control_sign_is_minus_f0(self):
        """phi_z(r_min) < 0 for f0_z > 0."""
        result = self._get_result()
        phi_z_rmin = float(result["ball_results"][0].phi_vec[2])
        assert phi_z_rmin < 0.0, f"phi_z(r_min)={phi_z_rmin:.3e} not < 0"

    def test_control_verdict_rejects_wrong_estimators(self):
        """Pure control_verdict test: wrong phi_exp multiples → CONTROL_FAIL; ×1.0 → MONOPOLE."""
        result = self._get_result()
        phis = [np.asarray(br.phi_vec) for br in result["ball_results"]]
        phi_exps_real = [np.asarray(pe) for pe in result["phi_exps"]]
        tols = result["tols"]
        f0 = np.asarray(result["f0_vec"])

        for scale in [2.0, 0.5, -1.0, 0.0]:
            bad_exps = [pe * scale for pe in phi_exps_real]
            v, _ = control_verdict("force_stop", phis, bad_exps, tols, f0)
            assert v == Verdict.CONTROL_FAIL, (
                f"scale={scale}: expected CONTROL_FAIL, got {v}"
            )

        v, _ = control_verdict("force_stop", phis, phi_exps_real, tols, f0)
        assert v == Verdict.MONOPOLE_DETECTED, (
            f"scale=1.0: expected MONOPOLE_DETECTED, got {v}"
        )

    def test_control_verdict_not_force_stopped(self):
        """stop_reason=max_iter → INCONCLUSIVE."""
        result = self._get_result()
        phis = [np.asarray(br.phi_vec) for br in result["ball_results"]]
        phi_exps = [np.asarray(pe) for pe in result["phi_exps"]]
        tols = result["tols"]
        f0 = np.asarray(result["f0_vec"])
        v, _ = control_verdict("max_iter", phis, phi_exps, tols, f0)
        assert v == Verdict.INCONCLUSIVE

    def test_control_clean_field_no_monopole(self):
        """f0=(0,0,0) on 32³ → NO_MONOPOLE."""
        engine = make_engine_32_periodic(use_saturation=True)
        result = run_injected_force_control(
            engine, f0=(0.0, 0.0, 0.0), radii=(4.0, 8.0, 12.0), max_iter=3000
        )
        assert result["verdict"] == Verdict.NO_MONOPOLE, (
            f"Expected NO_MONOPOLE, got {result['verdict']}. Notes: {result['notes']}"
        )

    @pytest.mark.engine_sim
    def test_control_64_default_radii(self):
        """64³, DEFAULT_RADII, f0=1e-2 → MONOPOLE_DETECTED and f_max < 1e-8."""
        engine = make_engine_64_periodic(use_saturation=True)
        result = run_injected_force_control(
            engine, f0=(0.0, 0.0, 1e-2), radii=DEFAULT_RADII, max_iter=MAX_ITER
        )
        assert result["verdict"] == Verdict.MONOPOLE_DETECTED, (
            f"Expected MONOPOLE_DETECTED, got {result['verdict']}. "
            f"Notes: {result['notes']}"
        )
        assert result["f_max"] < 1e-8, f"f_max={result['f_max']:.3e}"


# ── G11/B2: u-only convergence ────────────────────────────────────────────────

class TestUOnlyConvergence:
    """B2: force_stop_relax(u_only=True) delegates to relax_u_only, stable lr."""

    def test_u_only_relax_converges_on_cold_seed(self):
        """32³ A=0.05 seed: u_only converges to F<1e-8, no divergence."""
        engine = make_engine_32_periodic(use_saturation=True)
        seed_cold_knot(engine, R=6, r=2, amplitude_scale=COLD_AMPLITUDE_SCALE)
        result = force_stop_relax(engine, u_only=True, max_iter=1500)
        assert result["stop_reason"] == "force_stop", (
            f"Expected force_stop, got {result['stop_reason']!r}"
        )
        assert result["f_max"] < 1e-8, f"f_max={result['f_max']:.3e}"
        assert result["lr_halvings"] == 0, (
            f"lr_halvings={result['lr_halvings']}, expected 0"
        )
        # Never diverges: max(f_max_history[k:]) <= 2*min(f_max_history[:k+1])
        hist = result["f_max_history"]
        running_min = float("inf")
        for k, fk in enumerate(hist):
            running_min = min(running_min, fk)
            tail_max = max(hist[k:]) if k < len(hist) else fk
            assert tail_max <= 2.0 * running_min + 1e-15, (
                f"k={k}: tail_max={tail_max:.3e} > 2×running_min={running_min:.3e}"
            )

    def test_u_only_lr_below_stability_limit(self):
        """Returned lr * lambda_max <= 1.0 + 1e-9."""
        engine = make_engine_32_periodic(use_saturation=True)
        seed_cold_knot(engine, R=6, r=2, amplitude_scale=COLD_AMPLITUDE_SCALE)
        result = force_stop_relax(engine, u_only=True, max_iter=200)
        lam = result.get("lambda_max", 3.318)
        assert result["lr"] * lam <= 1.0 + 1e-9, (
            f"lr={result['lr']:.4f}, λ_max={lam:.4f}, product={result['lr']*lam:.6f}"
        )


# ── G5/B5: cold default amplitude ────────────────────────────────────────────

class TestColdDefaultAmplitude:
    """B5: COLD_AMPLITUDE_SCALE=0.05, measured ratio in [0.17, 0.29]."""

    def test_default_seed_inside_band(self):
        """32³: seed with A=COLD_AMPLITUDE_SCALE → measured ratio ≈ 0.181."""
        from shell_flux_f1_harness import _measure_strain_metrics
        engine = make_engine_32_periodic(use_saturation=True)
        seed_cold_knot(engine, R=6, r=2, amplitude_scale=COLD_AMPLITUDE_SCALE)
        ratio, _, _ = _measure_strain_metrics(engine)
        assert 0.17 <= ratio <= 0.29, (
            f"seed eps ratio = {ratio:.4f} not in [0.17, 0.29]"
        )
        assert abs(ratio - 0.18099) < 2e-3, (
            f"seed eps ratio = {ratio:.5f}, expected ≈ 0.18099 (within 2e-3)"
        )

    def test_hot_seed_refused(self):
        """A=0.20 → measured ratio ≈ 0.724 → measure_shell_flux raises ValueError."""
        from shell_flux_f1_harness import measure_shell_flux
        engine = make_engine_32_periodic(use_saturation=True)
        seed_cold_knot(engine, R=6, r=2, amplitude_scale=0.20)
        with pytest.raises(ValueError, match="0.41"):
            measure_shell_flux(engine, radii=(4.0, 8.0, 12.0), max_iter=1)

    def test_fence_boundary(self):
        """A=0.11 → ratio≈0.398, accepted; A=0.12 → ratio≈0.434, refused."""
        from shell_flux_f1_harness import measure_shell_flux, _measure_strain_metrics
        engine_ok = make_engine_32_periodic(use_saturation=True)
        seed_cold_knot(engine_ok, R=6, r=2, amplitude_scale=0.11)
        ratio_ok, _, _ = _measure_strain_metrics(engine_ok)
        assert ratio_ok < SEED_STRAIN_FENCE, (
            f"A=0.11 → ratio={ratio_ok:.4f} expected < {SEED_STRAIN_FENCE}"
        )

        engine_bad = make_engine_32_periodic(use_saturation=True)
        seed_cold_knot(engine_bad, R=6, r=2, amplitude_scale=0.12)
        ratio_bad, _, _ = _measure_strain_metrics(engine_bad)
        assert ratio_bad >= SEED_STRAIN_FENCE, (
            f"A=0.12 → ratio={ratio_bad:.4f} expected >= {SEED_STRAIN_FENCE}"
        )
        with pytest.raises(ValueError, match="0.41"):
            measure_shell_flux(engine_bad, radii=(4.0, 8.0, 12.0), max_iter=1)


# ── G8/B6: untie tau tracking ─────────────────────────────────────────────────

class TestUntieTauTracking:
    """B6: tau_history appended at every crossing check; tau_at_stop correct."""

    def test_untie_requires_3_consecutive_and_logs_tau(self, monkeypatch):
        """Monkeypatch crossing count; verify 3-consecutive rule and tau records."""
        engine = make_engine_32_periodic(use_saturation=True)
        seed_cold_knot(engine, R=6, r=2, amplitude_scale=COLD_AMPLITUDE_SCALE)

        # Sequence: 3 (c_init), 2, 3, 2, 2, 2, 2, ... → untie at step 5
        crossing_vals = iter([3, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        monkeypatch.setattr(
            engine, "extract_crossing_count", lambda: next(crossing_vals)
        )

        result = force_stop_relax(engine, max_iter=500)

        assert result["stop_reason"] == "untied", (
            f"Expected untied, got {result['stop_reason']!r}"
        )
        assert result["crossing_history"] == [3, 2, 3, 2, 2, 2]   # stop at check index 5
        assert result["iter_at_stop"] == 5
        assert len(result["tau_history"]) == 6
        tau_hist = result["tau_history"]
        cross_hist = result["crossing_history"]
        assert len(tau_hist) == len(cross_hist), (
            f"len(tau_history)={len(tau_hist)} != len(crossing_history)={len(cross_hist)}"
        )
        # tau_history is non-decreasing
        for i in range(len(tau_hist) - 1):
            assert tau_hist[i] <= tau_hist[i + 1], (
                f"tau_history[{i}]={tau_hist[i]:.4f} > tau_history[{i+1}]={tau_hist[i+1]:.4f}"
            )
        assert result["tau_at_stop"] == pytest.approx(tau_hist[-1], rel=1e-9)
        assert result["tau_at_stop"] > 0.0, "tau_at_stop should be > 0"


# ── G3/B7: platform line ──────────────────────────────────────────────────────

class TestPlatformLine:
    def test_platform_line_x64(self):
        """_build_platform_line on 32³ engine contains 'x64=True' and 'u_dtype=float64'."""
        from shell_flux_f1_harness import _build_platform_line
        engine = make_engine_32_periodic(use_saturation=True)
        line = _build_platform_line(engine)
        assert "x64=True" in line, f"x64=True not found in: {line}"
        assert "u_dtype=float64" in line, f"u_dtype=float64 not found in: {line}"
