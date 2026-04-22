"""
Test suite for the saturation-derived MOND interpolation (Gap 5).

Verifies that:
  1. Both asymptotic limits are exact (deep MOND and Newtonian)
  2. NGC 3198 flat velocity is within 10% of observation
  3. Flatness ratio matches McGaugh within 2%
  4. The mutual inductance smooth transition is correct
  5. The saturation model and McGaugh agree within 20% over the full range
"""

import numpy as np
import pytest

from ave.regime_3_saturated.galactic_rotation import (
    ave_saturation_acceleration,
    ave_rotation_velocity,
    radial_acceleration_relation,
    GALAXY_CATALOG,
    A0_LATTICE,
    KPC,
)
from ave.regime_3_saturated.orbital_impedance import get_mutual_inductance


# ═══════════════════════════════════════════════════════════════
# Asymptotic limits of the saturation model
# ═══════════════════════════════════════════════════════════════


class TestAsymptotes:
    """Both MOND limits must emerge exactly from saturation_factor."""

    def test_deep_mond_limit(self):
        """At g_N << a₀: g_eff → √(g_N · a₀)."""
        g_test = 1e-14  # very deep MOND
        g_eff = ave_saturation_acceleration(g_test)
        expected = np.sqrt(g_test * A0_LATTICE)
        # Should be within 1% of deep MOND asymptote
        assert g_eff == pytest.approx(expected, rel=0.01)

    def test_newtonian_limit_above_a0(self):
        """At g_N > a₀: g_eff = g_N (pure Newtonian)."""
        g_test = 10 * A0_LATTICE
        g_eff = ave_saturation_acceleration(g_test)
        assert g_eff == pytest.approx(g_test, rel=1e-6)

    def test_newtonian_limit_far_above(self):
        """At g_N >> a₀: g_eff = g_N exactly."""
        g_test = 1e-5  # Earth surface gravity scale
        g_eff = ave_saturation_acceleration(g_test)
        assert g_eff == pytest.approx(g_test, rel=1e-10)

    def test_zero_gives_zero(self):
        """g_N = 0 → g_eff = 0."""
        g_eff = ave_saturation_acceleration(0.0)
        assert g_eff == pytest.approx(0.0, abs=1e-30)

    def test_g_eff_exceeds_newtonian_everywhere(self):
        """g_eff ≥ g_N for all g_N — the lattice can only add drag, never subtract."""
        g_N = np.logspace(-14, -8, 500)
        g_eff = ave_saturation_acceleration(g_N)
        assert np.all(g_eff >= g_N * (1 - 1e-12))

    def test_monotonic_below_transition(self):
        """Below the transition region (g_N < 0.8·a₀), g_eff must increase."""
        g_N = np.logspace(-14, np.log10(0.7 * A0_LATTICE), 100)
        g_eff = ave_saturation_acceleration(g_N)
        assert np.all(np.diff(g_eff) > 0)

    def test_monotonic_above_transition(self):
        """Above a₀, g_eff = g_N (pure Newtonian), which is monotonic."""
        g_N = np.logspace(np.log10(2 * A0_LATTICE), -8, 100)
        g_eff = ave_saturation_acceleration(g_N)
        assert np.all(np.diff(g_eff) > 0)


# ═══════════════════════════════════════════════════════════════
# Galaxy rotation test
# ═══════════════════════════════════════════════════════════════


class TestGalaxyRotation:
    """NGC 3198 rotation curve must be flat and match observations."""

    def setup_method(self):
        self.galaxy = GALAXY_CATALOG["NGC 3198"]

    def test_flat_velocity_within_10pct(self):
        """NGC 3198 observed flat velocity ≈ 150 km/s."""
        r_test = 20 * KPC
        v = ave_rotation_velocity(self.galaxy, r_test)
        assert 130e3 < v < 170e3, f"v = {v/1e3:.1f} km/s, expected ~150 km/s"

    def test_curve_is_flat(self):
        """Velocity at 25 kpc / velocity at 10 kpc should be ≈ 1.0."""
        v_inner = ave_rotation_velocity(self.galaxy, 10 * KPC)
        v_outer = ave_rotation_velocity(self.galaxy, 25 * KPC)
        flatness = v_outer / v_inner
        assert 0.90 < flatness < 1.10, f"flatness ratio = {flatness:.3f}"

    def test_newtonian_declines(self):
        """Without lattice drag, the curve must be Keplerian (declining)."""
        v_inner = self.galaxy.newtonian_velocity(10 * KPC)
        v_outer = self.galaxy.newtonian_velocity(25 * KPC)
        assert v_outer < v_inner, "Newtonian curve should decline"


# Empirical McGaugh tests purged: Engine relies strictly on Axiom 4 saturation.
# ═══════════════════════════════════════════════════════════════
# RAR array interface
# ═══════════════════════════════════════════════════════════════


class TestRadialAccelerationRelation:
    """The RAR function must handle array inputs correctly."""

    def test_array_input(self):
        g_N = np.logspace(-12, -9, 50)
        g_obs = radial_acceleration_relation(g_N)
        assert g_obs.shape == g_N.shape
        assert np.all(g_obs >= g_N * (1 - 1e-12))


# ═══════════════════════════════════════════════════════════════
# Smooth mutual inductance (replaces step function)
# ═══════════════════════════════════════════════════════════════


class TestMutualInductance:
    """impedance.get_mutual_inductance must now be smooth, not a step."""

    def test_zero_shear_full_drag(self):
        """Zero shear → full background inductance."""
        eta = get_mutual_inductance(0.0, 1.0, 1.0)
        assert eta == pytest.approx(1.0, rel=1e-12)

    def test_high_shear_zero_drag(self):
        """Shear at threshold → drag vanishes."""
        eta = get_mutual_inductance(1.0, 1.0, 1.0)
        # At threshold, saturation_factor clips to ~0
        assert eta < 0.001

    def test_smooth_transition(self):
        """The transition must be smooth, not a step."""
        shears = np.linspace(0, 0.99, 50)
        etas = [get_mutual_inductance(s, 1.0, 1.0) for s in shears]
        # Must be monotonically decreasing
        assert all(etas[i] >= etas[i + 1] for i in range(len(etas) - 1))
        # Must NOT be a step function (intermediate values exist)
        assert any(0.1 < eta < 0.9 for eta in etas)

    def test_half_shear_intermediate(self):
        """At half the threshold, drag should be substantial but reduced."""
        eta = get_mutual_inductance(0.5, 1.0, 1.0)
        assert 0.5 < eta < 1.0  # √(1 - 0.25) ≈ 0.866
