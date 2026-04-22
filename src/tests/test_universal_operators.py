"""
Test Universal Topological Operators
=====================================

Tests for the three fundamental scale-invariant operators (impedance,
saturation, reflection) and the full 3-regime pairwise potential,
as defined in ``ave.core.universal_operators``.

These operators are the Tier 1 foundation — every domain solver
delegates to them. Getting these right means getting everything right.
"""

import numpy as np
import pytest

from ave.core.constants import EPSILON_0, MU_0, V_SNAP, Z_0
from ave.core.universal_operators import (
    universal_impedance,
    universal_pairwise_energy,
    universal_pairwise_gradient,
    universal_reflection,
    universal_saturation,
)

# ═══════════════════════════════════════════════════════════════════════
# 1. IMPEDANCE OPERATOR
# ═══════════════════════════════════════════════════════════════════════


class TestUniversalImpedance:
    """Z = sqrt(mu/eps) — the foundation of all AVE physics."""

    def test_vacuum_impedance(self):
        """Z₀ = sqrt(μ₀/ε₀) ≈ 376.73 Ω."""
        Z = universal_impedance(MU_0, EPSILON_0)
        assert abs(Z - Z_0) / Z_0 < 1e-10, f"Z={Z}, expected {Z_0}"

    def test_equal_impedances(self):
        """Z(mu, mu) = 1 for any mu."""
        assert abs(universal_impedance(5.0, 5.0) - 1.0) < 1e-15

    def test_array_input(self):
        """Works with numpy arrays."""
        mu = np.array([1.0, 4.0, 9.0])
        eps = np.array([1.0, 1.0, 1.0])
        Z = universal_impedance(mu, eps)
        np.testing.assert_allclose(Z, [1.0, 2.0, 3.0])

    def test_positive_definite(self):
        """Impedance is always positive for physical inputs."""
        Z = universal_impedance(0.001, 100.0)
        assert Z > 0


# ═══════════════════════════════════════════════════════════════════════
# 2. SATURATION OPERATOR
# ═══════════════════════════════════════════════════════════════════════


class TestUniversalSaturation:
    """S = sqrt(1 - (A/A_yield)²) — Axiom 4 at every scale."""

    def test_zero_strain(self):
        """S(0) = 1 (linear Maxwell recovered)."""
        S = universal_saturation(0.0, V_SNAP)
        assert abs(S - 1.0) < 1e-15

    def test_yield_strain(self):
        """S(A_yield) = 0 (dielectric collapse)."""
        S = universal_saturation(V_SNAP, V_SNAP)
        assert abs(S) < 1e-6

    def test_half_yield(self):
        """S(A_yield/2) = sqrt(3/4) ≈ 0.866."""
        S = universal_saturation(V_SNAP / 2, V_SNAP)
        expected = np.sqrt(1 - 0.25)
        assert abs(S - expected) < 1e-10

    def test_negative_amplitude(self):
        """Saturation is symmetric: S(-A) = S(A)."""
        S_pos = universal_saturation(100.0, V_SNAP)
        S_neg = universal_saturation(-100.0, V_SNAP)
        assert abs(S_pos - S_neg) < 1e-15

    def test_over_yield_clipped(self):
        """Beyond yield, clipped to 0 (no imaginary numbers)."""
        S = universal_saturation(V_SNAP * 1.5, V_SNAP)
        assert S >= 0.0
        assert S < 1e-6

    def test_array_input(self):
        """Works with numpy arrays."""
        A = np.array([0.0, V_SNAP / 2, V_SNAP])
        S = universal_saturation(A, V_SNAP)
        assert S[0] == pytest.approx(1.0, abs=1e-10)
        assert S[1] == pytest.approx(np.sqrt(0.75), abs=1e-10)
        assert S[2] == pytest.approx(0.0, abs=1e-6)

    def test_monotonically_decreasing(self):
        """S must decrease as amplitude increases."""
        A = np.linspace(0, V_SNAP * 0.99, 100)
        S = universal_saturation(A, V_SNAP)
        assert np.all(np.diff(S) <= 0), "Saturation must be monotonically decreasing"


# ═══════════════════════════════════════════════════════════════════════
# 3. REFLECTION OPERATOR
# ═══════════════════════════════════════════════════════════════════════


class TestUniversalReflection:
    """Γ = (Z₂ - Z₁)/(Z₂ + Z₁) — at every boundary, every scale."""

    def test_matched_impedance(self):
        """Γ = 0 when Z₁ = Z₂ (no reflection)."""
        Gamma = universal_reflection(Z_0, Z_0)
        assert abs(Gamma) < 1e-10

    def test_open_circuit(self):
        """Γ → +1 when Z₂ >> Z₁ (open circuit / particle boundary)."""
        Gamma = universal_reflection(1.0, 1e12)
        assert abs(Gamma - 1.0) < 1e-6

    def test_short_circuit(self):
        """Γ → −1 when Z₂ → 0 (short circuit / Pauli exclusion)."""
        Gamma = universal_reflection(Z_0, 1e-12)
        assert abs(Gamma + 1.0) < 1e-6

    def test_antisymmetric(self):
        """Swapping Z₁ and Z₂ flips the sign."""
        G1 = universal_reflection(100.0, 200.0)
        G2 = universal_reflection(200.0, 100.0)
        assert abs(G1 + G2) < 1e-10, "Reflection must be antisymmetric"

    def test_bounded(self):
        """|Γ| ≤ 1 for all physical impedances."""
        for Z1, Z2 in [(1, 100), (100, 1), (0.01, 1000)]:
            Gamma = universal_reflection(Z1, Z2)
            assert abs(Gamma) <= 1.0 + 1e-10


# ═══════════════════════════════════════════════════════════════════════
# 4. PAIRWISE ENERGY AND GRADIENT
# ═══════════════════════════════════════════════════════════════════════


class TestUniversalPairwiseEnergy:
    """U(r) = -(K/r)(T² - Γ²) — the full 3-regime impedance potential."""

    def test_far_field_coulomb(self):
        """At r >> d_sat: Γ ≈ 0, so U ≈ -K/r (pure Coulomb)."""
        K, d_sat = 1.0, 1e-15
        r = 1e-10  # 100,000× d_sat
        U = universal_pairwise_energy(r, K, d_sat)
        U_coulomb = -K / r
        assert abs(U - U_coulomb) / abs(U_coulomb) < 0.01

    def test_wall_repulsion(self):
        """At r ≤ d_sat: U > 0 (Pauli repulsive wall)."""
        K, d_sat = 1.0, 1e-15
        U = universal_pairwise_energy(d_sat * 0.5, K, d_sat)
        assert U > 0, "Must be repulsive inside saturation radius"

    def test_gradient_negative_far(self):
        """dU/dr > 0 far from wall (attractive force pulls inward)."""
        K, d_sat = 1.0, 1e-15
        r = 1e-10
        dUdr = universal_pairwise_gradient(r, K, d_sat)
        assert dUdr > 0, "Gradient should be positive (force toward center)"

    def test_array_input(self):
        """Energy works with arrays."""
        K, d_sat = 1.0, 1e-15
        r = np.array([1e-14, 1e-13, 1e-12, 1e-10])
        U = universal_pairwise_energy(r, K, d_sat)
        assert len(U) == 4
        assert U[-1] < 0, "Far-field should be attractive (negative energy)"
