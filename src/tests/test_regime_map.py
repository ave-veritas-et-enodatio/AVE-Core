"""
Tests for the Universal Regime Map
===================================
Verifies that every domain classifier maps known physical objects
to the correct regime.
"""

import pytest
import numpy as np
from ave.core.regime_map import (
    classify_regime,
    em_voltage_regime,
    em_field_regime,
    gravity_regime,
    bcs_regime,
    magnetic_regime,
    gw_regime,
    galactic_regime,
    identify_regime,
    REGIME_LINEAR,
    REGIME_NONLINEAR,
    REGIME_YIELD,
    REGIME_RUPTURED,
    R_LINEAR_MAX,
    R_NONLINEAR_MAX,
    R_YIELD_MAX,
    regime_equations,
    TRANSITION_NAMES,
)
from ave.core.constants import ALPHA


class TestClassifyRegime:
    """Core classification function."""

    def test_linear(self):
        info = classify_regime(0.05, 1.0)
        assert info.regime == REGIME_LINEAR
        assert info.S > 0.99

    def test_nonlinear(self):
        info = classify_regime(0.5, 1.0)
        assert info.regime == REGIME_NONLINEAR
        assert 0.4 < info.S < 1.0

    def test_yield(self):
        info = classify_regime(0.95, 1.0)
        assert info.regime == REGIME_YIELD
        assert info.S < 0.4

    def test_ruptured(self):
        info = classify_regime(1.5, 1.0)
        assert info.regime == REGIME_RUPTURED
        assert info.S == 0.0

    def test_exact_boundary(self):
        info = classify_regime(1.0, 1.0)
        assert info.regime == REGIME_RUPTURED

    def test_zero_amplitude(self):
        info = classify_regime(0.0, 1.0)
        assert info.regime == REGIME_LINEAR
        assert info.S == 1.0


class TestDerivedBoundaries:
    """Verify boundaries are derived from first principles."""

    def test_linear_boundary_is_sqrt_2alpha(self):
        assert abs(R_LINEAR_MAX - np.sqrt(2 * ALPHA)) < 1e-12

    def test_nonlinear_boundary_is_sqrt3_over_2(self):
        assert abs(R_NONLINEAR_MAX - np.sqrt(3) / 2) < 1e-12

    def test_yield_boundary_is_unity(self):
        assert R_YIELD_MAX == 1.0

    def test_at_linear_boundary_deltaS_equals_alpha(self):
        """At r = √(2α), the correction ΔS = r²/2 = α."""
        delta_S = R_LINEAR_MAX**2 / 2
        assert abs(delta_S - ALPHA) < 1e-12

    def test_at_nonlinear_boundary_Q_equals_2(self):
        """At r = √3/2, S = 1/2 → Q = 1/S = 2."""
        S = np.sqrt(1 - R_NONLINEAR_MAX**2)
        assert abs(S - 0.5) < 1e-12
        assert abs(1.0 / S - 2.0) < 1e-12


class TestTransitionBoundaries:
    """Verify transition (between-regime) boundary detection."""

    def test_near_linear_nonlinear_boundary(self):
        """r ≈ √(2α) should flag I↔II transition."""
        info = classify_regime(R_LINEAR_MAX, 1.0)
        assert info.near_boundary
        assert "I↔II" in info.boundary_name

    def test_near_nonlinear_yield_boundary(self):
        """r ≈ √3/2 should flag II↔III transition."""
        info = classify_regime(R_NONLINEAR_MAX * 0.95, 1.0)
        assert info.near_boundary
        assert "II↔III" in info.boundary_name

    def test_near_yield_ruptured_boundary(self):
        """r ≈ 1.0 should flag III↔IV transition."""
        info = classify_regime(0.98, 1.0)  # Within 10% of r=1.0, outside 10% of r=0.866
        assert info.near_boundary
        assert "III↔IV" in info.boundary_name

    def test_deep_linear_no_boundary(self):
        """r ≪ √(2α) should NOT flag transition."""
        info = classify_regime(0.01, 1.0)
        assert not info.near_boundary
        assert info.boundary_name is None

    def test_mid_nonlinear_no_boundary(self):
        """r = 0.5 is far from both boundaries — no transition."""
        info = classify_regime(0.5, 1.0)
        assert not info.near_boundary

    def test_summary_includes_transition(self):
        """The summary string should include TRANSITION for boundary cases."""
        info = classify_regime(R_LINEAR_MAX, 1.0)
        s = info.summary()
        assert "TRANSITION" in s
        assert "I↔II" in s

    def test_all_transition_names_defined(self):
        """All 3 boundary pairs should have transition names."""
        assert len(TRANSITION_NAMES) == 3
        assert (REGIME_LINEAR, REGIME_NONLINEAR) in TRANSITION_NAMES
        assert (REGIME_NONLINEAR, REGIME_YIELD) in TRANSITION_NAMES
        assert (REGIME_YIELD, REGIME_RUPTURED) in TRANSITION_NAMES


class TestIdentifyRegime:
    """Test the identify_regime() convenience startup function."""

    def test_em_voltage(self):
        info = identify_regime("em_voltage", verbose=False, V_local=30e3)
        assert info.regime == REGIME_NONLINEAR
        assert info.domain == "EM (dielectric)"

    def test_gravity(self):
        info = identify_regime("gravity", verbose=False, M_kg=1.989e30, r_meters=6.96e8)
        assert info.regime == REGIME_LINEAR

    def test_gw(self):
        info = identify_regime("gw", verbose=False, h_strain=1e-21)
        assert info.regime == REGIME_LINEAR

    def test_generic(self):
        info = identify_regime("generic", verbose=False, A=0.5, Ac=1.0)
        assert info.regime == REGIME_NONLINEAR

    def test_invalid_domain_raises(self):
        with pytest.raises(ValueError, match="Unknown domain"):
            identify_regime("invalid_domain", verbose=False, A=1.0)

    def test_verbose_prints(self, capsys):
        identify_regime("em_voltage", verbose=True, V_local=1000)
        captured = capsys.readouterr()
        assert "REGIME CLASSIFICATION" in captured.out


class TestEMDomain:
    """Electromagnetic regime classification."""

    def test_lab_voltage(self):
        info = em_voltage_regime(1000)  # 1kV
        assert info.regime == REGIME_LINEAR

    def test_ponder05_30kv(self):
        info = em_voltage_regime(30e3)
        assert info.regime == REGIME_NONLINEAR
        assert abs(info.r - 0.687) < 0.01

    def test_ponder05_43kv(self):
        info = em_voltage_regime(43e3)
        assert info.regime == REGIME_YIELD

    def test_lab_efield(self):
        info = em_field_regime(1e6)  # 1 MV/m
        assert info.regime == REGIME_LINEAR


class TestGravityDomain:
    """Gravitational regime classification."""

    def test_solar_surface(self):
        M_sun = 1.989e30
        r_sun = 6.96e8
        info = gravity_regime(M_sun, r_sun)
        assert info.regime == REGIME_LINEAR
        assert info.r < 1e-4

    def test_neutron_star(self):
        """A 1.4 M_sun NS at 10km: ε₁₁ = 7GM/(c²r) ≈ 1.46 → Regime IV.
        In AVE, the NS surface is INSIDE the saturation boundary, which
        is the AVE analog of the Buchdahl limit."""
        M_ns = 2.8e30  # ~1.4 M_sun
        r_ns = 1e4  # 10 km
        info = gravity_regime(M_ns, r_ns)
        assert info.regime == REGIME_RUPTURED
        assert info.r > 1.0

    def test_black_hole_horizon(self):
        """At r = r_s = 2GM/c², ε₁₁ = 7GM/(c²r) = 7/2 = 3.5 → Regime IV."""
        M = 10 * 1.989e30  # 10 solar masses
        G = 6.67430e-11
        r_s = 2 * G * M / (3e8) ** 2
        info = gravity_regime(M, r_s)
        assert info.regime == REGIME_RUPTURED


class TestMagneticDomain:

    def test_lab_magnet(self):
        info = magnetic_regime(10)  # 10 T
        assert info.regime == REGIME_LINEAR

    def test_magnetar(self):
        info = magnetic_regime(1e10)
        assert info.regime == REGIME_RUPTURED


class TestGWDomain:

    def test_ligo(self):
        info = gw_regime(1e-21)
        assert info.regime == REGIME_LINEAR

    def test_ns_merger(self):
        """NS merger at h=0.01: r = 0.117 < √(2α) = 0.121.
        Genuinely Linear — ΔS = r²/2 ≈ 0.007 < α ≈ 0.0073."""
        info = gw_regime(0.01)
        assert info.regime == REGIME_LINEAR

    def test_strong_merger(self):
        """A stronger source at h=0.02: r = 0.234 > √(2α) → Regime II."""
        info = gw_regime(0.02)
        assert info.regime == REGIME_NONLINEAR


class TestBCSDomain:

    def test_below_tc(self):
        info = bcs_regime(4.0, 9.2)  # Nb at 4K (Tc=9.2K)
        assert info.regime == REGIME_NONLINEAR

    def test_at_tc(self):
        info = bcs_regime(9.1, 9.2)  # Just below Tc
        assert info.regime == REGIME_YIELD


class TestGalacticDomain:
    """Galactic domain with derived a₀ = cH∞/(2π)."""

    def test_derived_a0_used(self):
        """Default a₀ should be derived, not empirical 1.2e-10."""
        info = galactic_regime(1e-10)
        # Derived a₀ ≈ 1.07e-10, so g_N=1e-10 gives r ≈ 0.93
        assert info.Ac < 1.15e-10  # derived, not 1.2e-10 empirical

    def test_inner_galaxy_newtonian(self):
        """Inner galaxy: g_N >> a₀ → Regime IV (Newtonian, no drag)."""
        info = galactic_regime(1e-9)  # 10× a₀
        assert info.regime == REGIME_RUPTURED

    def test_transition_boundary(self):
        """At g_N ≈ a₀: regime boundary (dark matter problem!)."""
        info = galactic_regime(1.07e-10)  # ≈ a₀
        assert info.regime in (REGIME_YIELD, REGIME_RUPTURED)

    def test_outer_galaxy_deep_mond(self):
        """Outer galaxy: g_N << a₀ → Regime I (deep MOND, full drag)."""
        info = galactic_regime(1e-12)  # 0.01× a₀
        assert info.regime == REGIME_LINEAR


class TestRegimeEquations:

    def test_linear_equations(self):
        eqs = regime_equations(REGIME_LINEAR)
        assert "ε_eff" in eqs
        assert "ε₀" in eqs["ε_eff"][0]

    def test_nonlinear_equations(self):
        eqs = regime_equations(REGIME_NONLINEAR)
        assert "√(1 - r²)" in eqs["ε_eff"][0]

    def test_all_regimes_valid(self):
        for r in [REGIME_LINEAR, REGIME_NONLINEAR, REGIME_YIELD, REGIME_RUPTURED]:
            eqs = regime_equations(r)
            assert len(eqs) == 5


class TestSummaryOutput:

    def test_summary_string(self):
        info = em_voltage_regime(30e3)
        s = info.summary()
        assert "NONLINEAR" in s or "Large-Signal" in s
        assert "30000" in s or "3.0000e+04" in s
