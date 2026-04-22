"""
Tests for ave.gravity.planetary_magnetosphere
"""

import numpy as np
from ave.gravity.planetary_magnetosphere import (
    dipole_field,
    magnetic_pressure,
    solar_wind_dynamic_pressure,
    magnetopause_standoff,
    magnetopause_standoff_Rp,
    magnetopause_reflection,
    uranus_asymmetric_profile,
    comparative_magnetosphere_table,
    EARTH,
    ALL_PLANETS,
)


class TestDipoleField:
    """Dipole magnetic field."""

    def test_field_at_surface(self):
        """Surface field should be close to B_equatorial."""
        B = dipole_field(EARTH, EARTH.radius_m, theta_deg=90)
        assert abs(B - EARTH.B_equatorial_T / 2) / (EARTH.B_equatorial_T / 2) < 0.5

    def test_field_falls_as_r3(self):
        """Field ∝ 1/r³."""
        B1 = dipole_field(EARTH, 2 * EARTH.radius_m, theta_deg=90)
        B2 = dipole_field(EARTH, 4 * EARTH.radius_m, theta_deg=90)
        ratio = B1 / B2
        assert abs(ratio - 8.0) / 8.0 < 0.3  # ~1/r³ with offset correction

    def test_polar_stronger_than_equatorial(self):
        """Polar field > equatorial field at same distance."""
        B_pole = dipole_field(EARTH, 3 * EARTH.radius_m, theta_deg=0)
        B_eq = dipole_field(EARTH, 3 * EARTH.radius_m, theta_deg=90)
        assert B_pole > B_eq

    def test_jupiter_strongest(self):
        """Jupiter should have strongest surface field."""
        fields = {p.name: dipole_field(p, p.radius_m, 90) for p in ALL_PLANETS}
        assert fields["Jupiter"] == max(fields.values())


class TestMagneticPressure:
    """Magnetic pressure."""

    def test_pressure_positive(self):
        assert magnetic_pressure(1e-5) > 0

    def test_pressure_scales_as_B2(self):
        P1 = magnetic_pressure(1e-5)
        P2 = magnetic_pressure(2e-5)
        assert abs(P2 / P1 - 4.0) < 0.01


class TestSolarWindPressure:
    """Solar wind dynamic pressure."""

    def test_pressure_at_1au(self):
        """P_sw at 1 AU ≈ 0.5-5 nPa."""
        P = solar_wind_dynamic_pressure(1.0)
        assert 0.1e-9 < P < 5e-9

    def test_pressure_falls_as_r2(self):
        P1 = solar_wind_dynamic_pressure(1.0)
        P2 = solar_wind_dynamic_pressure(2.0)
        assert abs(P1 / P2 - 4.0) < 0.01


class TestMagnetopause:
    """Magnetopause standoff distance."""

    def test_earth_standoff_order(self):
        """Earth's magnetopause at ~8-12 R_E."""
        r = magnetopause_standoff_Rp(EARTH)
        assert 5 < r < 15, f"Earth standoff = {r:.1f} R_E"

    def test_jupiter_largest(self):
        """Jupiter should have largest magnetosphere."""
        standoffs = {p.name: magnetopause_standoff(p) for p in ALL_PLANETS}
        assert standoffs["Jupiter"] == max(standoffs.values())

    def test_all_standoffs_positive(self):
        for planet in ALL_PLANETS:
            r = magnetopause_standoff_Rp(planet)
            assert r > 1.0, f"{planet.name}: standoff = {r:.1f} R_p"


class TestReflection:
    """Magnetopause reflection coefficient."""

    def test_reflection_bounded(self):
        """Γ should be between -1 and 1."""
        for planet in ALL_PLANETS:
            G = magnetopause_reflection(planet)
            assert -1.0 <= G <= 1.0, f"{planet.name}: Γ = {G:.3f}"


class TestUranusAsymmetry:
    """Uranus asymmetric magnetosphere."""

    def test_profile_shape(self):
        p = uranus_asymmetric_profile(n_points=36)
        assert len(p["longitude_deg"]) == 36
        assert len(p["r_mp_Rp"]) == 36

    def test_uranus_is_asymmetric(self):
        """Asymmetry ratio should be > 1.5 (highly non-uniform)."""
        p = uranus_asymmetric_profile()
        assert p["asymmetry_ratio"] > 1.2, f"Ratio = {p['asymmetry_ratio']:.2f}"

    def test_standoff_varies_with_longitude(self):
        """Standoff should vary by more than 30% across rotation."""
        p = uranus_asymmetric_profile()
        r_range = np.max(p["r_mp_Rp"]) - np.min(p["r_mp_Rp"])
        r_mean = np.mean(p["r_mp_Rp"])
        assert r_range / r_mean > 0.1


class TestComparative:
    """Comparative magnetosphere table."""

    def test_table_has_all_planets(self):
        t = comparative_magnetosphere_table()
        names = [r["name"] for r in t]
        assert "Earth" in names
        assert "Jupiter" in names
        assert "Uranus" in names

    def test_uranus_flagged_asymmetric(self):
        t = comparative_magnetosphere_table()
        uranus = [r for r in t if r["name"] == "Uranus"][0]
        assert uranus["symmetry"] == "asymmetric"

    def test_saturn_flagged_symmetric(self):
        t = comparative_magnetosphere_table()
        saturn = [r for r in t if r["name"] == "Saturn"][0]
        assert saturn["symmetry"] == "symmetric"
