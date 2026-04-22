"""
Test suite for Axiom 4: Dielectric Saturation (src/ave/axioms/saturation.py).

Locks in the six saturation functions' boundary conditions, limiting
behaviors, and mathematical identities that follow from the AVE axioms.
"""

import numpy as np
import pytest

from ave.axioms.saturation import (
    capacitance_eff,
    energy_density_nonlinear,
    epsilon_eff,
    impedance_at_strain,
    local_wave_speed,
    reflection_coefficient,
)
from ave.core.constants import ALPHA, C_0, EPSILON_0, V_YIELD, Z_0

# ---------------------------------------------------------------------------
# epsilon_eff: ε_eff(V) = ε₀ √(1 − (V/V_yield)²)
# ---------------------------------------------------------------------------


class TestEpsilonEff:
    """Non-linear permittivity under dielectric saturation."""

    def test_zero_strain_recovers_maxwell(self):
        """At V = 0, ε_eff must equal free-space ε₀ exactly."""
        assert epsilon_eff(0.0) == pytest.approx(EPSILON_0, rel=1e-12)

    def test_monotonically_decreasing(self):
        """ε_eff must strictly decrease as V increases toward V_yield."""
        voltages = np.linspace(0, 0.99 * V_YIELD, 50)
        eps = epsilon_eff(voltages)
        assert np.all(np.diff(eps) < 0)

    def test_near_yield_approaches_zero(self):
        """At 99.9% of V_yield, ε_eff → 0."""
        eps = epsilon_eff(0.999 * V_YIELD)
        assert eps < 0.05 * EPSILON_0

    def test_rupture_raises(self):
        """Exceeding V_yield must raise ValueError (lattice rupture)."""
        with pytest.raises(ValueError, match="Dielectric rupture"):
            epsilon_eff(1.01 * V_YIELD)

    def test_array_input(self):
        """Must accept numpy arrays and return element-wise results."""
        V = np.array([0.0, 0.5 * V_YIELD, 0.9 * V_YIELD])
        result = epsilon_eff(V)
        assert result.shape == (3,)
        assert result[0] > result[1] > result[2]

    def test_symmetry(self):
        """ε_eff(-V) = ε_eff(V) (even function of strain)."""
        assert epsilon_eff(0.5 * V_YIELD) == pytest.approx(epsilon_eff(-0.5 * V_YIELD), rel=1e-12)


# ---------------------------------------------------------------------------
# capacitance_eff: C_eff(Δφ) = 1/√(1 − (Δφ/α)²)
# ---------------------------------------------------------------------------


class TestCapacitanceEff:
    """Non-linear capacitance (inverse relationship to ε_eff)."""

    def test_zero_strain_is_unity(self):
        """At zero displacement, C_eff/C₀ = 1."""
        assert capacitance_eff(0.0) == pytest.approx(1.0, rel=1e-12)

    def test_diverges_near_alpha(self):
        """Near saturation (Δφ → α), capacitance diverges."""
        C = capacitance_eff(0.999 * ALPHA)
        assert C > 10.0  # strongly divergent

    def test_singularity_raises(self):
        """At |Δφ| = α, must raise ValueError."""
        with pytest.raises(ValueError, match="singularity"):
            capacitance_eff(ALPHA)

    def test_monotonically_increasing(self):
        """C_eff must strictly increase with |Δφ|."""
        dphi = np.linspace(0.0, 0.98 * ALPHA, 50)
        C = capacitance_eff(dphi)
        assert np.all(np.diff(C) > 0)


# ---------------------------------------------------------------------------
# reflection_coefficient: Γ = (Z_knot − Z_vac) / (Z_knot + Z_vac)
# ---------------------------------------------------------------------------


class TestReflectionCoefficient:
    """Transmission-line reflection coefficient Γ."""

    def test_matched_is_zero(self):
        """Z_knot = Z_vac → Γ = 0 (perfect transmission)."""
        assert reflection_coefficient(Z_0, Z_0) == pytest.approx(0.0, abs=1e-15)

    def test_short_is_minus_one(self):
        """Z_knot = 0 → Γ = −1 (total reflection, Pauli exclusion)."""
        assert reflection_coefficient(0.0, Z_0) == pytest.approx(-1.0, rel=1e-12)

    def test_open_is_plus_one(self):
        """Z_knot → ∞ → Γ = +1."""
        assert reflection_coefficient(1e12, Z_0) == pytest.approx(1.0, rel=1e-6)

    def test_bound_magnitude(self):
        """Γ must always satisfy |Γ| ≤ 1 for physical impedances."""
        for Z in [0.01, 1.0, 100.0, Z_0, 1e6]:
            assert abs(reflection_coefficient(Z)) <= 1.0 + 1e-12


# ---------------------------------------------------------------------------
# local_wave_speed: c_eff(V) = c₀ · (1 − (V/V_yield)²)^(1/4)
# ---------------------------------------------------------------------------


class TestLocalWaveSpeed:
    """Effective local phase velocity under saturation."""

    def test_zero_strain_is_c(self):
        """At V = 0, c_eff = c₀."""
        assert local_wave_speed(0.0) == pytest.approx(C_0, rel=1e-12)

    def test_near_yield_freezes(self):
        """Near V_yield, c_eff → 0 (mass formation)."""
        c = local_wave_speed(0.9999 * V_YIELD)
        assert c < 0.15 * C_0

    def test_explicit_formula(self):
        """c_eff = c₀ · (1 − (V/V_yield)²)^(1/4) — verify the exact formula."""
        V_test = 0.5 * V_YIELD
        c = local_wave_speed(V_test)
        x = V_test / V_YIELD
        expected = C_0 * (1.0 - x**2) ** 0.25
        assert c == pytest.approx(expected, rel=1e-10)

    def test_monotonically_decreasing(self):
        """c_eff must decrease as strain increases."""
        V = np.linspace(0, 0.99 * V_YIELD, 50)
        c = local_wave_speed(V)
        assert np.all(np.diff(c) < 0)


# ---------------------------------------------------------------------------
# impedance_at_strain: Z_eff(V) = Z₀ / (1 − (V/V_yield)²)^(1/4)
# ---------------------------------------------------------------------------


class TestImpedanceAtStrain:
    """Local impedance under saturation."""

    def test_zero_strain_is_z0(self):
        """At V = 0, Z_eff = Z₀."""
        assert impedance_at_strain(0.0) == pytest.approx(Z_0, rel=1e-12)

    def test_rises_with_strain(self):
        """Z_eff must increase as V approaches V_yield."""
        V = np.linspace(0, 0.99 * V_YIELD, 50)
        Z = impedance_at_strain(V)
        assert np.all(np.diff(Z) > 0)

    def test_explicit_formula(self):
        """Z_eff = Z₀ / (1 − (V/V_yield)²)^(1/4) — verify the exact formula."""
        V_test = 0.5 * V_YIELD
        Z = impedance_at_strain(V_test)
        x = V_test / V_YIELD
        expected = Z_0 / (1.0 - x**2) ** 0.25
        assert Z == pytest.approx(expected, rel=1e-10)


# ---------------------------------------------------------------------------
# energy_density_nonlinear: U ≈ ½ε₀(Δφ)² + (3/8α²)ε₀(Δφ)⁴
# ---------------------------------------------------------------------------


class TestEnergyDensityNonlinear:
    """Full non-linear energy density with E⁴ correction."""

    def test_zero_field_is_zero(self):
        """No field → no energy."""
        assert energy_density_nonlinear(0.0) == pytest.approx(0.0, abs=1e-30)

    def test_small_field_is_linear(self):
        """For tiny Δφ, the E⁴ term is negligible → U ≈ ½ε₀Δφ²."""
        dphi = 1e-10
        U = energy_density_nonlinear(dphi)
        U_linear = 0.5 * EPSILON_0 * dphi**2
        assert U == pytest.approx(U_linear, rel=1e-6)

    def test_large_field_exceeds_linear(self):
        """For larger Δφ, the E⁴ correction makes U > ½ε₀Δφ²."""
        dphi = ALPHA * 0.5
        U = energy_density_nonlinear(dphi)
        U_linear = 0.5 * EPSILON_0 * dphi**2
        assert U > U_linear

    def test_always_positive(self):
        """Energy density must be non-negative for all fields."""
        dphi = np.linspace(-ALPHA * 0.99, ALPHA * 0.99, 100)
        U = energy_density_nonlinear(dphi)
        assert np.all(U >= 0)
