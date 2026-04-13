"""
Test suite for Gravitational Wave Propagation.

Verifies:
  1. Schwarzschild radius matches GR
  2. SYMMETRIC GRAVITY: Z ≡ Z₀ everywhere, Γ = 0 (no reflection)
  3. GW strain is far below saturation (linear propagation)
  4. Refractive index > 1 near mass (gravitational lensing)
  5. Local speed c_local = c/n decreases near mass
"""

import numpy as np
import pytest

from ave.gravity.gw_propagation import (
    schwarzschild_radius,
    epsilon_eff_schwarzschild,
    mu_eff_schwarzschild,
    gravitational_impedance,
    horizon_reflection,
    gw_strain_to_voltage,
    is_linear_propagation,
    gw_local_speed,
    refractive_index,
    gw_propagation_summary,
)
from ave.core.constants import C_0, EPSILON_0, MU_0, Z_0, G, V_SNAP


M_SUN = 1.989e30  # Solar mass [kg]


class TestSchwarzschildRadius:
    """r_s = 2GM/c² must match GR."""

    def test_sun(self):
        """For the Sun: r_s ≈ 2.95 km."""
        r_s = schwarzschild_radius(M_SUN)
        assert r_s == pytest.approx(2953, rel=0.01)

    def test_30_solar(self):
        """For a 30 M☉ black hole: r_s ≈ 88.6 km."""
        r_s = schwarzschild_radius(30 * M_SUN)
        assert r_s == pytest.approx(88600, rel=0.01)

    def test_proportional(self):
        """r_s scales linearly with M."""
        assert schwarzschild_radius(2 * M_SUN) == pytest.approx(
            2 * schwarzschild_radius(M_SUN), rel=1e-10)


class TestSymmetricGravity:
    """Symmetric Gravity: Z ≡ Z₀ everywhere, Γ = 0."""

    def test_far_field_vacuum(self):
        """Far from mass: ε → ε₀, μ → μ₀, Z → Z₀."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r = 1e6 * r_s  # Very far
        assert float(epsilon_eff_schwarzschild(r, r_s)) == pytest.approx(
            EPSILON_0, rel=1e-4)
        assert float(mu_eff_schwarzschild(r, r_s)) == pytest.approx(
            MU_0, rel=1e-4)
        assert float(gravitational_impedance(r, r_s)) == pytest.approx(
            Z_0, rel=1e-4)

    def test_impedance_constant_everywhere(self):
        """Z must equal Z₀ at ALL radii — this IS Symmetric Gravity."""
        r_s = schwarzschild_radius(30 * M_SUN)
        for mult in [1.01, 1.1, 2, 5, 10, 100, 1000]:
            r = mult * r_s
            Z = float(gravitational_impedance(r, r_s))
            assert Z == pytest.approx(Z_0, rel=1e-3), \
                f"Z({mult}·r_s) = {Z:.2f}, expected {Z_0:.2f}"

    def test_gamma_zero_everywhere(self):
        """Γ = 0 at ALL radii — no reflection, no echoes."""
        r_s = schwarzschild_radius(30 * M_SUN)
        for mult in [1.01, 1.1, 2, 5, 10, 100, 1000]:
            r = mult * r_s
            gamma = float(horizon_reflection(r, r_s))
            assert abs(gamma) < 0.01, \
                f"Γ({mult}·r_s) = {gamma:.6f}, expected ~0"

    def test_epsilon_mu_scale_symmetrically(self):
        """ε and μ must scale by the SAME factor n(r)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        for mult in [1.1, 2, 10, 100]:
            r = mult * r_s
            eps = float(epsilon_eff_schwarzschild(r, r_s))
            mu = float(mu_eff_schwarzschild(r, r_s))
            n_from_eps = eps / EPSILON_0
            n_from_mu = mu / MU_0
            assert n_from_eps == pytest.approx(n_from_mu, rel=1e-10), \
                f"Asymmetric scaling at {mult}·r_s: ε-factor={n_from_eps}, μ-factor={n_from_mu}"

    def test_near_horizon_epsilon_diverges(self):
        """Near horizon: ε >> ε₀ (metric is deeply strained)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r = 1.01 * r_s
        eps = float(epsilon_eff_schwarzschild(r, r_s))
        assert eps > 10 * EPSILON_0

    def test_near_horizon_mu_diverges(self):
        """Near horizon: μ >> μ₀ (symmetric with ε)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r = 1.01 * r_s
        mu = float(mu_eff_schwarzschild(r, r_s))
        assert mu > 10 * MU_0


class TestGWLinearPropagation:
    """LIGO GW must be in the linear regime (no saturation)."""

    def test_ligo_strain_is_linear(self):
        """h = 10⁻²¹ at 100 Hz must be linear."""
        assert is_linear_propagation(1e-21, 100.0)

    def test_strain_voltage_is_tiny(self):
        """V_GW / V_SNAP ~ 10⁻¹⁹ for LIGO GW."""
        V_gw = gw_strain_to_voltage(1e-21, 100.0)
        ratio = V_gw / V_SNAP
        assert ratio < 1e-10  # Many orders of magnitude below saturation

    def test_gw_always_below_saturation(self):
        """Even h = 1 produces V_gw << V_SNAP — GW can NEVER saturate."""
        V_gw = gw_strain_to_voltage(1.0, 100.0)
        ratio = V_gw / V_SNAP
        assert ratio < 1e-3, f"V_gw/V_SNAP = {ratio:.2e}, expected << 1"


class TestRefractiveIndex:
    """Gravity well must have n > 1 (lensing)."""

    def test_far_field_n_equals_one(self):
        """Far from mass: n → 1 (flat space)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        n = float(refractive_index(1e12 * r_s, r_s))
        assert n == pytest.approx(1.0, abs=1e-6)

    def test_near_mass_n_greater_than_one(self):
        """Near mass: n > 1 (light bends)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        n = float(refractive_index(10 * r_s, r_s))
        assert n > 1.0

    def test_monotonically_increasing_inward(self):
        """n increases as r decreases (stronger lensing)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r = np.array([100, 50, 20, 10, 5]) * r_s
        n = refractive_index(r, r_s)
        assert np.all(np.diff(n) > 0)  # n increases as r decreases


class TestLocalSpeed:
    """c_local = c/n must decrease near mass."""

    def test_far_field_speed_is_c(self):
        """Far from mass: c_local → c₀."""
        r_s = schwarzschild_radius(30 * M_SUN)
        c_local = gw_local_speed(1e12 * r_s, r_s)
        assert c_local == pytest.approx(C_0, rel=1e-6)

    def test_near_mass_speed_drops(self):
        """Near mass: c_local < c₀ (light slows)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        c_local = gw_local_speed(10 * r_s, r_s)
        assert c_local < C_0

    def test_near_horizon_speed_approaches_zero(self):
        """Near horizon: c_local → 0."""
        r_s = schwarzschild_radius(30 * M_SUN)
        c_local = gw_local_speed(1.01 * r_s, r_s)
        assert c_local < 0.02 * C_0


class TestSummary:
    """Summary function should produce complete output."""

    def test_summary_runs(self):
        """Summary should run without errors."""
        result = gw_propagation_summary(30.0, 1e-21)
        assert result['linear_propagation'] is True
        assert len(result['profiles']) > 0
        assert result['r_s_m'] > 0

    def test_summary_no_echo_key(self):
        """Summary should NOT contain echo_delay (scrapped)."""
        result = gw_propagation_summary(30.0, 1e-21)
        assert 'echo_delay_s' not in result
