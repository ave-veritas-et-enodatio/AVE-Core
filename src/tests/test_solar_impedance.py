"""
Tests for ave.gravity.solar_impedance
"""

import pytest
from ave.gravity.solar_impedance import (
    solar_wind_density,
    solar_wind_plasma_frequency,
    solar_wind_impedance,
    heliospheric_impedance_profile,
    solar_radiation_pressure,
    oumuamua_radiation_acceleration,
    oumuamua_impedance_acceleration,
    oumuamua_summary,
    saturation_radius_au,
    oort_cloud_prediction,
    kirkwood_gap_radius,
    kirkwood_impedance_model,
    OUMUAMUA,
    AU,
    R_SUN,
    A0_LATTICE,
)
from ave.core.constants import Z_0


class TestSolarWind:
    """Solar wind plasma properties."""

    def test_density_1au(self):
        """Density at 1 AU should be ~5×10⁶ m⁻³."""
        n = solar_wind_density(AU)
        assert abs(n - 5e6) / 5e6 < 0.01

    def test_density_falls_as_r2(self):
        """Density ∝ 1/r²."""
        n1 = solar_wind_density(1 * AU)
        n2 = solar_wind_density(2 * AU)
        assert abs(n1 / n2 - 4.0) < 0.01

    def test_density_raises_below_sun(self):
        with pytest.raises(ValueError):
            solar_wind_density(R_SUN * 0.5)

    def test_plasma_frequency_positive(self):
        fp = solar_wind_plasma_frequency(AU)
        assert fp > 0

    def test_plasma_frequency_decreases_with_r(self):
        fp1 = solar_wind_plasma_frequency(1 * AU)
        fp2 = solar_wind_plasma_frequency(10 * AU)
        assert fp2 < fp1

    def test_impedance_approaches_Z0(self):
        """Far from Sun (low density), Z → Z₀."""
        Z = solar_wind_impedance(100 * AU, freq_hz=1e9)
        assert abs(Z - Z_0) / Z_0 < 0.01

    def test_impedance_evanescent_below_cutoff(self):
        """Very low frequency at high density → evanescent."""
        Z = solar_wind_impedance(0.1 * AU, freq_hz=1.0)
        assert Z == 0.0


class TestHeliosphericProfile:
    """Full radial impedance profile."""

    def test_profile_shape(self):
        p = heliospheric_impedance_profile(n_points=100)
        assert len(p["r_au"]) == 100
        assert len(p["Z_sw"]) == 100
        assert len(p["g_solar"]) == 100

    def test_density_monotonically_decreases(self):
        p = heliospheric_impedance_profile(n_points=100)
        for i in range(len(p["n_e"]) - 1):
            assert p["n_e"][i] >= p["n_e"][i + 1]

    def test_gravity_monotonically_decreases(self):
        p = heliospheric_impedance_profile(n_points=100)
        for i in range(len(p["g_solar"]) - 1):
            assert p["g_solar"][i] >= p["g_solar"][i + 1]

    def test_heliopause_reflection(self):
        """Heliopause should have a measurable Γ."""
        p = heliospheric_impedance_profile()
        assert p["Gamma_heliopause"] != 0.0


class TestOumuamua:
    """'Oumuamua anomalous acceleration."""

    def test_area_to_mass(self):
        """A/m should be ≥ 1 m²/kg for thin body."""
        assert OUMUAMUA.area_to_mass >= 1.0

    def test_radiation_pressure_positive(self):
        P = solar_radiation_pressure(AU)
        assert P > 0

    def test_radiation_pressure_at_1au(self):
        """Solar radiation pressure at 1 AU ≈ 4.6 μPa."""
        P = solar_radiation_pressure(AU)
        assert abs(P - 4.56e-6) / 4.56e-6 < 0.05

    def test_oumuamua_acceleration_order(self):
        """Acceleration at 1 AU should be ~10⁻⁶ to 10⁻⁵ m/s²."""
        a = oumuamua_radiation_acceleration(AU)
        assert 1e-7 < a < 1e-4

    def test_oumuamua_matches_observation(self):
        """Predicted acceleration should match Micheli et al. within 50%."""
        summary = oumuamua_summary()
        ratio = summary["ratio_predicted_observed"]
        assert 0.5 < ratio < 2.0, f"Ratio = {ratio:.2f}"

    def test_oumuamua_scales_as_1_over_r2(self):
        """Acceleration should scale as 1/r²."""
        a1 = oumuamua_radiation_acceleration(1 * AU)
        a2 = oumuamua_radiation_acceleration(2 * AU)
        ratio = a1 / a2
        assert abs(ratio - 4.0) < 0.01

    def test_impedance_acceleration_equals_radiation(self):
        """In AVE, impedance acceleration IS radiation pressure."""
        a_rad = oumuamua_radiation_acceleration(AU)
        a_imp = oumuamua_impedance_acceleration(AU)
        assert abs(a_rad - a_imp) / a_rad < 0.01


class TestOortCloud:
    """Oort Cloud as saturation boundary."""

    def test_saturation_radius_order(self):
        """Saturation radius should be ~10³-10⁵ AU."""
        r = saturation_radius_au()
        assert 1e3 < r < 1e5, f"r_sat = {r:.0f} AU"

    def test_oort_prediction_structure(self):
        p = oort_cloud_prediction()
        assert "r_saturation_au" in p
        assert "g_at_saturation" in p
        assert p["g_at_saturation"] == A0_LATTICE


class TestKirkwoodGaps:
    """Kirkwood gaps as cavity resonances."""

    def test_3_1_resonance(self):
        """3:1 gap should be at ~2.50 AU."""
        r = kirkwood_gap_radius(3, 1)
        assert abs(r - 2.50) < 0.02

    def test_2_1_resonance(self):
        """2:1 gap should be at ~3.28 AU."""
        r = kirkwood_gap_radius(2, 1)
        assert abs(r - 3.28) < 0.02

    def test_5_2_resonance(self):
        """5:2 gap should be at ~2.82 AU."""
        r = kirkwood_gap_radius(5, 2)
        assert abs(r - 2.82) < 0.02

    def test_all_gaps_match(self):
        """All predicted gaps within 1% of observed."""
        gaps = kirkwood_impedance_model()
        for gap in gaps:
            if gap["r_observed_au"] is not None:
                assert gap["error_pct"] < 1.0, f"{gap['resonance']}: {gap['error_pct']:.2f}% error"

    def test_gap_count(self):
        gaps = kirkwood_impedance_model()
        assert len(gaps) == 5
