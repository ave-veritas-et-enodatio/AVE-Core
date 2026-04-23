"""
Pre-registered unit tests for the Axiom 4 Vacuum Varactor — Stage 6 Phase 1.

Pins the load-bearing Axiom-4 forms used by Stage 6's pair-production
engine work before any engine code lands:

  1. Vacuum Varactor constitutive equation  C_eff(V) = C_0/S(V)
     where S(V) = √(1-(V/V_yield)²)                               (Axiom 4)
  2. Taylor expansion to 4th order matching Vol 4 Ch 1:139       (Axiom 4)
  3. Node LC-tank resonance softening Ω_node(V) = ω_0·S(V)^(1/2) (Axiom 4)
  4. Boundary conditions and monotonicity                         (Axiom 4)
  5. Engine saturation_factor matches the closed-form curve       (Axiom 1+4)

Phase 1 convention for new test_*.py files in Stage 6:
  - Filename: test_axiom_N_<feature>.py or test_phaseN_<feature>.py
  - Class: TestAxiomN_<Feature> or TestPhaseN_<Feature>
  - Each test method docstring cites:
      * the axiom being pinned
      * the manuscript file:line being verified
      * the engine file:line being verified (if applicable)
  - Each test method asserts against a numerically-derivable target;
    no qualitative assertions.

Reference:
  - manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:127-142
    (Vacuum Varactor, eq:varactor, eq:varactor_taylor)
  - research/L3_electron_soliton/54_pair_production_axiom_derivation.md §4
    (Ω_node(V) derivation)
  - src/ave/axioms/scale_invariant.py::saturation_factor
    (engine kernel; yield_limit argument gates V_SNAP vs V_yield convention)

Predictions.yaml entry: P_phase0_varactor.
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.axioms.scale_invariant import saturation_factor
from ave.core.constants import ALPHA, V_SNAP, V_YIELD


# ───────────────────────────────────────────────────────────────────────────
# Closed-form Axiom-4 references (duplicated here deliberately so the test
# pins the FORM, not just that the engine agrees with itself).
# ───────────────────────────────────────────────────────────────────────────

def _closed_form_S(V: float, V_yield_: float = V_YIELD) -> float:
    """S(V) = √(1-(V/V_yield)²) per Vol 4 Ch 1:132."""
    r2 = (V / V_yield_) ** 2
    return float(np.sqrt(max(0.0, 1.0 - r2)))


def _closed_form_C_ratio(V: float, V_yield_: float = V_YIELD) -> float:
    """C_eff/C_0 = 1/√(1-(V/V_yield)²) per Vol 4 Ch 1:132."""
    return 1.0 / _closed_form_S(V, V_yield_)


def _closed_form_omega_ratio(V: float, V_yield_: float = V_YIELD) -> float:
    """Ω_node/ω_0 = S(V)^(1/2) = (1-(V/V_yield)²)^(1/4) per doc 54_ §4."""
    return _closed_form_S(V, V_yield_) ** 0.5


# ═══════════════════════════════════════════════════════════════════════════
# 1. S(V) boundary conditions and monotonicity
# ═══════════════════════════════════════════════════════════════════════════
class TestAxiom4SaturationKernel:
    """Pins S(V) = √(1 - (V/V_yield)²) from Vol 4 Ch 1:132."""

    def test_s_at_zero_is_unity(self):
        """V = 0 → S = 1 (Axiom 4; Vol 4 Ch 1:132 linear limit)."""
        assert _closed_form_S(0.0) == pytest.approx(1.0, abs=1e-12)

    def test_s_at_half_yield(self):
        """V = V_yield/2 → S = √(3/4) = √3/2 ≈ 0.866 (Axiom 4)."""
        assert _closed_form_S(V_YIELD / 2.0) == pytest.approx(
            np.sqrt(3.0) / 2.0, rel=1e-12
        )

    def test_s_at_yield_over_sqrt2(self):
        """V = V_yield/√2 → S = √(1/2) ≈ 0.707 (Axiom 4)."""
        assert _closed_form_S(V_YIELD / np.sqrt(2.0)) == pytest.approx(
            1.0 / np.sqrt(2.0), rel=1e-12
        )

    def test_s_approaches_zero_near_yield(self):
        """V → V_yield → S → 0 (Axiom 4; Regime IV boundary per Vol 4 Ch 1:132)."""
        assert _closed_form_S(0.999 * V_YIELD) < 0.05

    def test_s_monotonically_decreases(self):
        """S(V) strictly decreases as |V| → V_yield (Axiom 4)."""
        Vs = np.linspace(0.0, 0.999 * V_YIELD, 50)
        S_vals = np.array([_closed_form_S(v) for v in Vs])
        assert np.all(np.diff(S_vals) < 0)

    def test_s_is_even(self):
        """S(-V) = S(V) (quadratic dependence per Axiom 4)."""
        assert _closed_form_S(0.5 * V_YIELD) == pytest.approx(
            _closed_form_S(-0.5 * V_YIELD), rel=1e-12
        )


# ═══════════════════════════════════════════════════════════════════════════
# 2. Vacuum Varactor C_eff(V) constitutive equation
# ═══════════════════════════════════════════════════════════════════════════
class TestAxiom4VacuumVaractor:
    """Pins C_eff(V) = C_0/S(V) from Vol 4 Ch 1:127-142 (eq:varactor)."""

    def test_ratio_is_unity_at_zero_drive(self):
        """C_eff/C_0 = 1 at V = 0 (Vol 4 Ch 1:132 linear vacuum limit)."""
        assert _closed_form_C_ratio(0.0) == pytest.approx(1.0, abs=1e-12)

    def test_ratio_diverges_approaching_yield(self):
        """C_eff/C_0 → ∞ as V → V_yield (Vol 4 Ch 1:132 varactor divergence)."""
        # At r = 0.999, Vol 4 Ch 1:147 table gives C_eff/C_0 ≈ 22.37
        assert _closed_form_C_ratio(0.999 * V_YIELD) == pytest.approx(22.37, rel=1e-3)

    def test_ratio_matches_vol4_ch1_table(self):
        """C_eff/C_0 at representative drive levels matches Vol 4 Ch 1:147 table values."""
        # Table rows from Vol 4 Ch 1 lines 151-158:
        #   r = V/V_yield    C_eff/C_0
        #     0.10            1.005
        #     0.50            1.155
        #     0.90            2.294
        table_rows = [(0.10, 1.005), (0.50, 1.155), (0.90, 2.294)]
        for r, expected in table_rows:
            ratio = _closed_form_C_ratio(r * V_YIELD)
            assert ratio == pytest.approx(expected, rel=5e-4), (
                f"r={r}: expected C_eff/C_0 = {expected}, got {ratio:.4f}"
            )


# ═══════════════════════════════════════════════════════════════════════════
# 3. Taylor expansion to 4th order (Vol 4 Ch 1:139 eq:varactor_taylor)
# ═══════════════════════════════════════════════════════════════════════════
class TestAxiom4VaractorTaylorExpansion:
    """Pins the 2nd and 4th order Taylor coefficients per Vol 4 Ch 1:139."""

    @staticmethod
    def _taylor_to_4th(r: float) -> float:
        """C_eff/C_0 ≈ 1 + (1/2)r² + (3/8)r⁴  (Vol 4 Ch 1:139)."""
        return 1.0 + 0.5 * r**2 + (3.0 / 8.0) * r**4

    def test_second_order_coefficient(self):
        """d²(C_eff/C_0)/dr² at r=0 equals 1 (coefficient 1/2 × 2 = 1)."""
        # Numerical second derivative of 1/√(1-r²) at r=0 is exactly 1.
        eps = 1e-4
        f = _closed_form_C_ratio
        center = f(0.0)
        plus = f(eps * V_YIELD)
        # d²f/dr² ≈ 2·(plus - center)/eps² at r=0 (f is even)
        d2 = 2.0 * (plus - center) / eps**2
        assert d2 == pytest.approx(1.0, rel=5e-3)

    def test_fourth_order_matches_taylor(self):
        """At small r (r ≤ 0.2), varactor ≈ 4th-order Taylor to < 1e-4 relative."""
        for r in [0.05, 0.10, 0.15, 0.20]:
            closed = _closed_form_C_ratio(r * V_YIELD)
            taylor = self._taylor_to_4th(r)
            rel_err = abs(closed - taylor) / closed
            # 4th-order truncation error is O(r⁶); at r=0.2, that's ~6e-5
            assert rel_err < 2e-4, (
                f"r={r}: closed={closed:.6f}, taylor-4={taylor:.6f}, "
                f"rel_err={rel_err:.2e}"
            )

    def test_euler_heisenberg_correspondence(self):
        """At V << V_yield the leading correction is quadratic, matching
        the Euler-Heisenberg QED effective Lagrangian structure
        (Vol 4 Ch 1:142 explicit cross-reference)."""
        r_small = 0.01
        closed = _closed_form_C_ratio(r_small * V_YIELD)
        quadratic_only = 1.0 + 0.5 * r_small**2
        # At r=0.01 the 4th-order term is ~3.75e-9 — negligible.
        assert abs(closed - quadratic_only) < 1e-7


# ═══════════════════════════════════════════════════════════════════════════
# 4. Node LC-tank resonance softening Ω_node(V) per doc 54_ §4
# ═══════════════════════════════════════════════════════════════════════════
class TestAxiom4NodeResonanceSoftening:
    """Pins Ω_node(V) = ω_0·S(V)^(1/2) = ω_0·(1-(V/V_yield)²)^(1/4) per
    research/L3_electron_soliton/54_pair_production_axiom_derivation.md §4.

    Derivation: Ω_node = 1/√(L_e·C_eff) = ω_0·√S(V)  (L_e unchanged, C_eff = C_0/S).
    """

    def test_omega_at_zero_drive_is_bare_frequency(self):
        """V = 0 → Ω_node/ω_0 = 1 (Compton frequency, unsaturated tank)."""
        assert _closed_form_omega_ratio(0.0) == pytest.approx(1.0, abs=1e-12)

    def test_omega_at_half_yield(self):
        """V = V_yield/2 → Ω_node/ω_0 = (3/4)^(1/4) ≈ 0.931."""
        expected = (3.0 / 4.0) ** 0.25
        assert _closed_form_omega_ratio(V_YIELD / 2.0) == pytest.approx(
            expected, rel=1e-12
        )
        assert expected == pytest.approx(0.9306, abs=1e-4)

    def test_omega_at_yield_over_sqrt2(self):
        """V = V_yield/√2 → Ω_node/ω_0 = (1/2)^(1/4) ≈ 0.841."""
        expected = 0.5 ** 0.25
        assert _closed_form_omega_ratio(V_YIELD / np.sqrt(2.0)) == pytest.approx(
            expected, rel=1e-12
        )
        assert expected == pytest.approx(0.8409, abs=1e-4)

    def test_omega_crashes_near_yield(self):
        """V → V_yield → Ω_node/ω_0 → 0 (tank resonance crashes to DC; doc 54_ §4)."""
        assert _closed_form_omega_ratio(0.999 * V_YIELD) < 0.25

    def test_omega_monotonically_decreases(self):
        """Ω_node(V) strictly decreases as |V| → V_yield (Axiom 4 softening)."""
        Vs = np.linspace(0.0, 0.99 * V_YIELD, 50)
        omegas = np.array([_closed_form_omega_ratio(v) for v in Vs])
        assert np.all(np.diff(omegas) < 0)

    def test_omega_is_quartic_root_of_1_minus_r_squared(self):
        """Ω_node/ω_0 = (1 - r²)^(1/4) exactly, per doc 54_ §4 derivation."""
        for r in [0.1, 0.3, 0.5, 0.7, 0.9]:
            omega_ratio = _closed_form_omega_ratio(r * V_YIELD)
            expected = (1.0 - r**2) ** 0.25
            assert omega_ratio == pytest.approx(expected, rel=1e-12)


# ═══════════════════════════════════════════════════════════════════════════
# 5. Engine's saturation_factor agrees with the closed-form kernel
# ═══════════════════════════════════════════════════════════════════════════
class TestAxiom4EngineKernelAgreement:
    """The engine's saturation_factor (scale_invariant.py) must reproduce
    S(V) = √(1-(V/V_yield)²) exactly when called with yield_limit=V_YIELD."""

    def test_engine_matches_closed_form_scalar(self):
        """Scalar call: saturation_factor(V, V_YIELD) = S_closed(V)."""
        for r in [0.0, 0.1, 0.3, 0.5, 0.7, 0.9]:
            V = r * V_YIELD
            engine_S = float(saturation_factor(V, V_YIELD))
            closed_S = _closed_form_S(V)
            assert engine_S == pytest.approx(closed_S, rel=1e-12)

    def test_engine_matches_closed_form_array(self):
        """Vector call: saturation_factor broadcasts correctly."""
        Vs = np.linspace(0.0, 0.95 * V_YIELD, 20)
        engine_S = saturation_factor(Vs, V_YIELD)
        closed_S = np.array([_closed_form_S(v) for v in Vs])
        assert np.allclose(engine_S, closed_S, rtol=1e-12)

    def test_engine_with_v_snap_is_not_v_yield(self):
        """Sanity: calling saturation_factor(V, V_SNAP) gives a DIFFERENT
        result than saturation_factor(V, V_YIELD). This pins the
        V_SNAP vs V_yield convention issue flagged in doc 54_ §5 — the
        two normalizations are NOT interchangeable."""
        V = 0.5 * V_YIELD  # same physical voltage
        S_with_yield = float(saturation_factor(V, V_YIELD))
        S_with_snap = float(saturation_factor(V, V_SNAP))
        # S with V_yield norm: √(1 - 0.25) = 0.866
        # S with V_SNAP norm: √(1 - 0.25·α) ≈ √(1 - 1.8e-3) ≈ 0.999
        assert S_with_yield == pytest.approx(np.sqrt(0.75), rel=1e-12)
        assert S_with_snap == pytest.approx(np.sqrt(1.0 - 0.25 * ALPHA), rel=1e-12)
        assert S_with_snap > S_with_yield  # V_SNAP norm is far from saturation
