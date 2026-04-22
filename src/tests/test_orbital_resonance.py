"""
Test Orbital Resonance Solver
==============================

Tests for the black hole orbital resonance framework: Schwarzschild radii,
ISCO, kerr photon sphere, QPO frequencies, and QNM eigenvalues.
"""

import numpy as np
import pytest
from ave.core.constants import M_SUN
from ave.solvers.orbital_resonance import (
    schwarzschild_radius,
    photon_sphere_radius,
    isco_radius,
    refractive_index,
    qnm_eigenvalue,
    ringdown_frequency,
    ringdown_Q_and_decay,
    hawking_temperature,
    kerr_photon_sphere,
    regge_wheeler_potential,
)


class TestCharacteristicRadii:
    def test_schwarzschild_radius_proportional_to_mass(self):
        rs1 = schwarzschild_radius(M_SUN)
        rs2 = schwarzschild_radius(2 * M_SUN)
        assert rs2 == pytest.approx(2 * rs1, rel=1e-10)

    def test_schwarzschild_radius_sun(self):
        rs = schwarzschild_radius(M_SUN)
        assert 2900 < rs < 3100, f"r_s(Sun) = {rs} m, expected ~2953 m"

    def test_photon_sphere_is_1_5_rs(self):
        rs = schwarzschild_radius(M_SUN)
        rph = photon_sphere_radius(M_SUN)
        assert rph == pytest.approx(1.5 * rs, rel=1e-10)

    def test_isco_schwarzschild_is_3_rs(self):
        rs = schwarzschild_radius(M_SUN)
        r_isco = isco_radius(M_SUN, a_star=0.0)
        assert r_isco == pytest.approx(3.0 * rs, rel=1e-10)

    def test_isco_decreases_with_spin(self):
        r0 = isco_radius(M_SUN, a_star=0.0)
        r7 = isco_radius(M_SUN, a_star=0.7)
        assert r7 < r0

    def test_kerr_photon_sphere_decreases_with_spin(self):
        rph_0 = kerr_photon_sphere(M_SUN, 0.0)
        rph_7 = kerr_photon_sphere(M_SUN, 0.7)
        assert rph_7 < rph_0


class TestRefractiveIndex:
    def test_far_field_approaches_1(self):
        r_far = 1e15  # Very far from Sun
        n = refractive_index(r_far, M_SUN)
        assert abs(n - 1.0) < 1e-6

    def test_increases_near_horizon(self):
        rs = schwarzschild_radius(M_SUN)
        n_far = refractive_index(100 * rs, M_SUN)
        n_near = refractive_index(2 * rs, M_SUN)
        assert n_near > n_far


class TestQNMEigenvalue:
    def test_schwarzschild_fundamental(self):
        """ω_R M ≈ 0.37 for ℓ=2 Schwarzschild."""
        M = 10 * M_SUN
        f, tau, Q, oR, oI = qnm_eigenvalue(M, a_star=0.0)
        assert 0.30 < oR < 0.45, f"ω_R·M = {oR}, expected ~0.37"
        assert Q > 1

    def test_frequency_scales_inversely_with_mass(self):
        f10 = ringdown_frequency(10 * M_SUN)
        f20 = ringdown_frequency(20 * M_SUN)
        assert f10 == pytest.approx(2 * f20, rel=0.01)

    def test_kerr_higher_frequency_than_schwarzschild(self):
        f_s = ringdown_frequency(10 * M_SUN, a_star=0.0)
        f_k = ringdown_frequency(10 * M_SUN, a_star=0.7)
        assert f_k > f_s

    def test_Q_and_decay_returns_positive(self):
        Q, tau, f = ringdown_Q_and_decay(10 * M_SUN, a_star=0.5)
        assert Q > 0
        assert tau > 0
        assert f > 0


class TestHawkingTemperature:
    def test_positive(self):
        T = hawking_temperature(M_SUN)
        assert T > 0

    def test_decreases_with_mass(self):
        T1 = hawking_temperature(M_SUN)
        T10 = hawking_temperature(10 * M_SUN)
        assert T1 > T10


class TestReggeWheeler:
    def test_potential_zero_at_horizon(self):
        """V(x=2) should be close to 0 (horizon)."""
        V = regge_wheeler_potential(2.001)
        assert abs(V) < 0.1

    def test_potential_positive_peak(self):
        x = np.linspace(3, 20, 100)
        V = regge_wheeler_potential(x)
        assert np.max(V) > 0, "Regge-Wheeler potential must have a positive peak"
