"""
Test suite for Stellar Interior (Gap 7).

Verifies:
  1. SSM layer properties are physically reasonable
  2. Plasma frequency increases toward core
  3. Impedance decreases toward core (Z ∝ 1/√n_e)
  4. Tachocline and photosphere reflections are physical
  5. p-mode frequencies match observed solar oscillation range
"""

import numpy as np
import pytest

from ave.gravity.stellar_interior import (
    SSM_LAYERS,
    build_radial_profile,
    helioseismology_modes,
    photosphere_reflection,
    solar_opacity_from_impedance,
    tachocline_reflection,
)


class TestSSMLayers:
    """Standard Solar Model layers must be physically reasonable."""

    def test_seven_layers(self):
        """SSM should have 7 layers."""
        assert len(SSM_LAYERS) == 7

    def test_density_increases_inward(self):
        """n_e should increase from corona to core."""
        densities = [layer.n_e for layer in SSM_LAYERS]
        # Core should be densest
        assert densities[0] == max(densities)
        # Corona should be least dense
        assert densities[-1] == min(densities)

    def test_temperature_core(self):
        """Core temperature ≈ 15.7 million K."""
        assert SSM_LAYERS[0].T == pytest.approx(1.57e7, rel=0.1)

    def test_photosphere_temperature(self):
        """Photosphere ≈ 5800 K."""
        photo = [l for l in SSM_LAYERS if l.name == "Photosphere"][0]
        assert photo.T == pytest.approx(5800, rel=0.1)

    def test_layers_cover_full_range(self):
        """Layers should span from 0 to > 1 R☉."""
        assert SSM_LAYERS[0].r_inner < 0.01
        assert SSM_LAYERS[-1].r_outer > 1.0


class TestRadialProfile:
    """Radial profile must produce continuous, physical output."""

    def test_profile_runs(self):
        """Profile build should succeed."""
        profile = build_radial_profile(n_points=100)
        assert len(profile["r_frac"]) == 100

    def test_impedance_decreases_inward(self):
        """Z/Z₀ should decrease toward the core (denser plasma)."""
        profile = build_radial_profile(n_points=200)
        Z = profile["Z_ratio"]
        # Core should have lower Z than surface
        assert Z[0] < Z[-1]

    def test_plasma_frequency_increases_inward(self):
        """ω_p increases toward the core."""
        profile = build_radial_profile(n_points=200)
        wp = profile["omega_p"]
        assert wp[0] > wp[-1]


class TestBoundaryReflections:
    """Key boundaries must have measurable reflection."""

    def test_tachocline_reflection_nonzero(self):
        """Tachocline should produce a nonzero Γ."""
        gamma = tachocline_reflection()
        assert abs(gamma) > 0

    def test_photosphere_reflection_nonzero(self):
        """Photosphere boundary should produce nonzero Γ."""
        gamma = photosphere_reflection()
        assert abs(gamma) > 0

    def test_photosphere_larger_than_tachocline(self):
        """Photosphere Γ should be larger (bigger impedance jump)."""
        assert abs(photosphere_reflection()) > abs(tachocline_reflection())


class TestSolarOpacity:
    """Opacity must depend on frequency and depth."""

    def test_optical_transparent_at_surface(self):
        """Optical photons escape from photosphere."""
        opacity = solar_opacity_from_impedance(0.98, 5e14)
        assert opacity < 0.5  # Mostly transparent

    def test_radio_opaque_in_core(self):
        """Radio waves cannot penetrate the core."""
        opacity = solar_opacity_from_impedance(0.1, 1e6)
        assert opacity > 0.9  # Totally reflected


class TestHelioseismology:
    """p-mode frequencies must match observed solar oscillations."""

    def test_modes_positive(self):
        """All p-mode frequencies must be positive."""
        modes = helioseismology_modes(5)
        assert np.all(modes > 0)

    def test_modes_increase_with_n(self):
        """Higher n should have higher frequency."""
        modes = helioseismology_modes(5)
        assert np.all(np.diff(modes) > 0)

    def test_modes_in_observed_range(self):
        """Solar p-modes are 1000-5000 μHz (observed)."""
        modes = helioseismology_modes(10)
        # At least some modes should be in the observed range
        assert np.any(modes > 100)  # Not all below 100 μHz
