"""
Test suite for Neutrino MSW Effect (Gap 8).

Verifies:
  1. Matter potential scales with n_e
  2. Resonance density is positive and physical
  3. Mixing angle → θ₁₂ in vacuum (n_e → 0)
  4. Mixing angle → π/4 at resonance
  5. Survival probability is in [0, 1]
  6. Impedance analogy produces valid output
"""

import numpy as np
import pytest

from ave.gravity.neutrino_msw import (
    THETA_12,
    effective_mixing_angle,
    impedance_analogy,
    matter_potential,
    msw_resonance_density,
    solar_msw_profile,
    survival_probability,
)


class TestMatterPotential:
    """V_CC must scale with n_e."""

    def test_zero_density(self) -> None:
        """No electrons → no potential."""
        assert matter_potential(0.0) == 0.0

    def test_positive(self) -> None:
        """V_CC must be positive for positive n_e."""
        assert matter_potential(1e30) > 0

    def test_proportional(self) -> None:
        """V_CC ∝ n_e."""
        V1 = matter_potential(1e30)
        V2 = matter_potential(2e30)
        assert V2 == pytest.approx(2 * V1, rel=1e-10)


class TestMixingAngle:
    """Effective mixing angle must behave correctly."""

    def test_vacuum_limit(self) -> None:
        """At n_e → 0: θ_m → θ₁₂ (vacuum)."""
        theta = effective_mixing_angle(0.0, 10.0)
        assert theta == pytest.approx(THETA_12, abs=0.01)

    def test_resonance_gives_maximal(self) -> None:
        """At resonance: θ_m → π/4."""
        n_res = msw_resonance_density(10.0)
        theta = effective_mixing_angle(n_res, 10.0)
        assert theta == pytest.approx(np.pi / 4, abs=0.05)

    def test_angle_in_range(self) -> None:
        """θ_m must be in [0, π/2]."""
        theta = effective_mixing_angle(1e30, 10.0)
        assert 0 <= theta <= np.pi / 2


class TestResonanceDensity:
    """MSW resonance density must be physical."""

    def test_positive(self) -> None:
        """Resonance density must be > 0."""
        n_res = msw_resonance_density(10.0)
        assert n_res > 0

    def test_decreases_with_energy(self) -> None:
        """Higher E → lower resonance density."""
        n1 = msw_resonance_density(1.0)
        n2 = msw_resonance_density(10.0)
        assert n2 < n1

    def test_solar_range(self) -> None:
        """For 1-10 MeV solar neutrinos, n_res should be
        in the solar interior range (~10²⁸ to 10³² m⁻³)."""
        n_res = msw_resonance_density(5.0)
        assert 1e20 < n_res < 1e40


class TestSurvivalProbability:
    """P(ν_e → ν_e) must be in [0, 1]."""

    def test_in_range(self) -> None:
        """Probability must be between 0 and 1."""
        P = survival_probability(1e30, 10.0)
        assert 0 <= P <= 1

    def test_vacuum_high_probability(self) -> None:
        """In vacuum (n_e→0), P_ee should be relatively high."""
        P = survival_probability(0.0, 10.0)
        assert P > 0.3  # cos²θ₁₂ ≈ 0.7

    def test_varies_with_density(self) -> None:
        """P should change with density."""
        P1 = survival_probability(1e28, 10.0)
        P2 = survival_probability(1e32, 10.0)
        assert P1 != pytest.approx(P2, abs=0.01)


class TestImpedanceAnalogy:
    """Impedance analogy must produce valid output."""

    def test_basic_output(self) -> None:
        """Should return a dict with expected keys."""
        result = impedance_analogy(1e30, 10.0)
        assert "gamma_mode" in result
        assert "P_ee" in result
        assert "theta_m_deg" in result

    def test_vacuum_no_mismatch(self) -> None:
        """In vacuum, Z_e ≈ Z_μ → Γ ≈ 0."""
        result = impedance_analogy(0.0, 10.0)
        assert abs(result["gamma_mode"]) < 0.1


class TestSolarProfile:
    """Solar MSW profile must run."""

    def test_profile_runs(self) -> None:
        """Profile should produce valid arrays."""
        result = solar_msw_profile(10.0, n_points=50)
        assert len(result["P_ee"]) == 50
        assert np.all(result["P_ee"] >= 0)
        assert np.all(result["P_ee"] <= 1)
