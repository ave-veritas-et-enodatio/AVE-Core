"""
Test suite for the Scale-Invariant Impedance Operations module.

Verifies that:
  1. The universal functions produce correct boundary values
  2. They accept both scalars and numpy arrays
  3. The old module APIs still produce identical results (non-breaking refactor)
  4. Cross-scale identity: the SAME function works for particle confinement,
     seismic boundaries, and antenna S₁₁
"""

import numpy as np
import pytest

from ave.axioms.scale_invariant import (
    epsilon_eff,
    impedance,
    impedance_at_strain,
    local_wave_speed,
    reflection_coefficient,
    saturation_factor,
)
from ave.core.constants import C_0, EPSILON_0, MU_0, V_SNAP, Z_0

# ═══════════════════════════════════════════════════════════════
# impedance: Z = √(μ/ε)
# ═══════════════════════════════════════════════════════════════


class TestImpedance:
    """The universal impedance operator."""

    def test_vacuum_impedance(self):
        """Z₀ = √(μ₀/ε₀) ≈ 376.73 Ω — exact by definition."""
        assert impedance(MU_0, EPSILON_0) == pytest.approx(Z_0, rel=1e-12)

    def test_array_input(self):
        """Must accept arrays and return element-wise results."""
        mu = np.array([MU_0, 2 * MU_0])
        eps = np.array([EPSILON_0, 2 * EPSILON_0])
        result = impedance(mu, eps)
        assert result.shape == (2,)
        assert result[0] == pytest.approx(Z_0, rel=1e-12)
        assert result[1] == pytest.approx(Z_0, rel=1e-12)

    def test_high_epsilon_lowers_impedance(self):
        """Higher ε (more compliance) → lower Z."""
        Z_high_eps = impedance(MU_0, 10 * EPSILON_0)
        assert Z_high_eps < Z_0

    def test_high_mu_raises_impedance(self):
        """Higher μ (more inertia) → higher Z."""
        Z_high_mu = impedance(10 * MU_0, EPSILON_0)
        assert Z_high_mu > Z_0


# ═══════════════════════════════════════════════════════════════
# saturation_factor: √(1 − (A/A_yield)²) — the single nonlinearity
# ═══════════════════════════════════════════════════════════════


class TestSaturationFactor:
    """The universal saturation kernel — Axiom 4 at every scale."""

    def test_zero_amplitude_is_unity(self):
        """At A = 0, S = 1 (linear Maxwell recovered)."""
        assert float(saturation_factor(0.0)) == pytest.approx(1.0, rel=1e-15)

    def test_near_yield_approaches_zero(self):
        """At A → A_yield, S → 0."""
        S = float(saturation_factor(0.9999 * V_SNAP, V_SNAP))
        assert S < 0.02

    def test_monotonically_decreasing(self):
        """S must strictly decrease as A increases."""
        A = np.linspace(0, 0.99 * V_SNAP, 50)
        S = saturation_factor(A, V_SNAP)
        assert np.all(np.diff(S) < 0)

    def test_symmetry(self):
        """S(-A) = S(A) — even function of amplitude."""
        assert float(saturation_factor(0.5 * V_SNAP)) == pytest.approx(
            float(saturation_factor(-0.5 * V_SNAP)), rel=1e-12
        )

    def test_clip_mode_doesnt_raise(self):
        """With clip=True (default), exceeding yield clips instead of raising."""
        result = saturation_factor(1.1 * V_SNAP, V_SNAP, clip=True)
        assert float(result) >= 0.0

    def test_no_clip_mode_raises(self):
        """With clip=False, exceeding yield raises ValueError."""
        with pytest.raises(ValueError, match="Dielectric rupture"):
            saturation_factor(1.1 * V_SNAP, V_SNAP, clip=False)

    def test_arbitrary_yield_limit(self):
        """Works with any yield limit, not just V_SNAP."""
        # Seismic analogy: use arbitrary pressure values
        A = 50.0
        A_yield = 100.0
        S = float(saturation_factor(A, A_yield))
        expected = np.sqrt(1.0 - (50.0 / 100.0) ** 2)
        assert S == pytest.approx(expected, rel=1e-12)

    def test_array_input(self):
        """Must accept and return arrays."""
        A = np.array([0.0, 0.5 * V_SNAP, 0.9 * V_SNAP])
        result = saturation_factor(A, V_SNAP)
        assert result.shape == (3,)
        assert result[0] > result[1] > result[2]


# ═══════════════════════════════════════════════════════════════
# reflection_coefficient: Γ = (Z₂ − Z₁) / (Z₂ + Z₁)
# ═══════════════════════════════════════════════════════════════


class TestReflectionCoefficient:
    """The universal boundary operator — every scale, every domain."""

    def test_matched_impedance_is_zero(self):
        """Z₁ = Z₂ → Γ = 0 (perfect transmission)."""
        assert float(reflection_coefficient(Z_0, Z_0)) == pytest.approx(0.0, abs=1e-15)

    def test_short_circuit_is_minus_one(self):
        """Z₁ >> Z₂ → Γ → −1 (Pauli exclusion / total reflection)."""
        # Z1 = Z₀, Z2 = 0 → Γ = (0 - Z₀)/(0 + Z₀) = -1
        assert float(reflection_coefficient(Z_0, 0.0)) == pytest.approx(-1.0, rel=1e-12)

    def test_open_circuit_is_plus_one(self):
        """Z₂ >> Z₁ → Γ → +1."""
        assert float(reflection_coefficient(0.01, 1e12)) == pytest.approx(1.0, rel=1e-6)

    def test_moho_reflection(self):
        """Seismic Moho: Γ ≈ 0.17 for typical crust/mantle impedances."""
        Z_crust = 2900 * 6500  # Lower crust: ρ × V_p
        Z_mantle = 3300 * 8100  # Upper mantle: ρ × V_p
        gamma = float(reflection_coefficient(Z_crust, Z_mantle))
        assert 0.10 < gamma < 0.25  # Reasonable Moho value

    def test_default_Z2_is_Z0(self):
        """Without explicit Z2, defaults to vacuum impedance Z₀."""
        gamma = float(reflection_coefficient(100.0))
        expected = (Z_0 - 100.0) / (Z_0 + 100.0)
        assert gamma == pytest.approx(expected, rel=1e-12)

    def test_magnitude_bounded(self):
        """|Γ| ≤ 1 for all positive impedances."""
        for Z1, Z2 in [(0.01, Z_0), (Z_0, 0.01), (1.0, 1e6), (Z_0, Z_0)]:
            assert abs(float(reflection_coefficient(Z1, Z2))) <= 1.0 + 1e-12


# ═══════════════════════════════════════════════════════════════
# Cross-scale identity: saturation.py ≡ scale_invariant
# ═══════════════════════════════════════════════════════════════


class TestCrossScaleIdentity:
    """Prove that the old saturation.py API calls the same math."""

    def test_epsilon_eff_matches_saturation_module(self):
        """saturation.epsilon_eff ≡ scale_invariant.epsilon_eff for all V."""
        from ave.axioms.saturation import epsilon_eff as sat_epsilon_eff

        V_test = np.linspace(0, 0.99 * V_SNAP, 100)
        old = sat_epsilon_eff(V_test, V_SNAP)
        new = epsilon_eff(V_test, V_SNAP, EPSILON_0, clip=False)
        np.testing.assert_allclose(old, new, rtol=1e-12)

    def test_reflection_matches_saturation_module(self):
        """saturation.reflection_coefficient ≡ scale_invariant version."""
        from ave.axioms.saturation import reflection_coefficient as sat_gamma

        for Z in [0.0, 1.0, 100.0, Z_0, 1e6]:
            old = sat_gamma(Z, Z_0)
            new = float(reflection_coefficient(Z_0, Z))
            assert old == pytest.approx(new, rel=1e-12, abs=1e-15)

    def test_impedance_at_strain_matches(self):
        """saturation.impedance_at_strain ≡ scale_invariant version."""
        from ave.axioms.saturation import impedance_at_strain as sat_z_strain

        V_test = np.linspace(0, 0.99 * V_SNAP, 50)
        old = sat_z_strain(V_test, V_SNAP)
        new = impedance_at_strain(V_test, V_SNAP, Z_0, clip=True)
        np.testing.assert_allclose(old, new, rtol=1e-12)

    def test_local_wave_speed_matches(self):
        """saturation.local_wave_speed ≡ scale_invariant version."""
        from ave.axioms.saturation import local_wave_speed as sat_lws

        V_test = np.linspace(0, 0.99 * V_SNAP, 50)
        old = sat_lws(V_test, V_SNAP)
        new = local_wave_speed(V_test, V_SNAP, C_0, clip=True)
        np.testing.assert_allclose(old, new, rtol=1e-12)

    def test_seismic_uses_universal_gamma(self):
        """Seismic module produces same results through the universal function."""
        from ave.regime_2_nonlinear.seismic import PREM_LAYERS
        from ave.regime_2_nonlinear.seismic import reflection_coefficient as seismic_gamma

        # Compute Moho reflection manually
        Z1 = PREM_LAYERS[1].acoustic_impedance_p  # Lower crust
        Z2 = PREM_LAYERS[2].acoustic_impedance_p  # Upper mantle
        universal = float(reflection_coefficient(Z1, Z2))
        seismic = seismic_gamma(PREM_LAYERS[1], PREM_LAYERS[2], "p")
        assert universal == pytest.approx(seismic, rel=1e-12)
