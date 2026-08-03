"""
Tests for ave.gravity.solar_impedance
"""

import pytest

from ave.core.constants import Z_0
from ave.gravity.solar_impedance import (
    A0_LATTICE,
    AU,
    OUMUAMUA,
    R_SUN,
    heliospheric_impedance_profile,
    kirkwood_gap_radius,
    kirkwood_impedance_model,
    oort_cloud_prediction,
    oumuamua_impedance_acceleration,
    oumuamua_radiation_acceleration,
    oumuamua_summary,
    saturation_radius_au,
    solar_radiation_pressure,
    solar_wind_density,
    solar_wind_impedance,
    solar_wind_plasma_frequency,
)


class TestSolarWind:
    """Solar wind plasma properties."""

    def test_density_1au(self) -> None:
        """Density at 1 AU should be ~5×10⁶ m⁻³."""
        n = solar_wind_density(AU)
        assert abs(n - 5e6) / 5e6 < 0.01

    def test_density_falls_as_r2(self) -> None:
        """Density ∝ 1/r²."""
        n1 = solar_wind_density(1 * AU)
        n2 = solar_wind_density(2 * AU)
        assert abs(n1 / n2 - 4.0) < 0.01

    def test_density_raises_below_sun(self) -> None:
        with pytest.raises(ValueError):
            solar_wind_density(R_SUN * 0.5)

    def test_plasma_frequency_positive(self) -> None:
        fp = solar_wind_plasma_frequency(AU)
        assert fp > 0

    def test_plasma_frequency_decreases_with_r(self) -> None:
        fp1 = solar_wind_plasma_frequency(1 * AU)
        fp2 = solar_wind_plasma_frequency(10 * AU)
        assert fp2 < fp1

    def test_impedance_approaches_Z0(self) -> None:
        """Far from Sun (low density), Z → Z₀."""
        Z = solar_wind_impedance(100 * AU, freq_hz=1e9)
        assert abs(Z - Z_0) / Z_0 < 0.01

    def test_impedance_evanescent_below_cutoff(self) -> None:
        """Very low frequency at high density → evanescent."""
        Z = solar_wind_impedance(0.1 * AU, freq_hz=1.0)
        assert Z == 0.0


class TestHeliosphericProfile:
    """Full radial impedance profile."""

    def test_profile_shape(self) -> None:
        p = heliospheric_impedance_profile(n_points=100)
        assert len(p["r_au"]) == 100
        assert len(p["Z_sw"]) == 100
        assert len(p["g_solar"]) == 100

    def test_density_monotonically_decreases(self) -> None:
        p = heliospheric_impedance_profile(n_points=100)
        for i in range(len(p["n_e"]) - 1):
            assert p["n_e"][i] >= p["n_e"][i + 1]

    def test_gravity_monotonically_decreases(self) -> None:
        p = heliospheric_impedance_profile(n_points=100)
        for i in range(len(p["g_solar"]) - 1):
            assert p["g_solar"][i] >= p["g_solar"][i + 1]

    def test_heliopause_reflection(self) -> None:
        """Heliopause should have a measurable Γ."""
        p = heliospheric_impedance_profile()
        assert p["Gamma_heliopause"] != 0.0


class TestOumuamua:
    """'Oumuamua anomalous acceleration."""

    def test_area_to_mass(self) -> None:
        """A/m should be ≥ 1 m²/kg for thin body."""
        assert OUMUAMUA.area_to_mass >= 1.0

    def test_radiation_pressure_positive(self) -> None:
        P = solar_radiation_pressure(AU)
        assert P > 0

    def test_radiation_pressure_at_1au(self) -> None:
        """Solar radiation pressure at 1 AU ≈ 4.6 μPa."""
        P = solar_radiation_pressure(AU)
        assert abs(P - 4.56e-6) / 4.56e-6 < 0.05

    def test_oumuamua_acceleration_order(self) -> None:
        """Acceleration at 1 AU should be ~10⁻⁶ to 10⁻⁵ m/s²."""
        a = oumuamua_radiation_acceleration(AU)
        assert 1e-7 < a < 1e-4

    def test_oumuamua_matches_observation(self) -> None:
        """Predicted acceleration should match Micheli et al. within 50%."""
        summary = oumuamua_summary()
        ratio = summary["ratio_predicted_observed"]
        assert 0.5 < ratio < 2.0, f"Ratio = {ratio:.2f}"

    def test_oumuamua_scales_as_1_over_r2(self) -> None:
        """Acceleration should scale as 1/r²."""
        a1 = oumuamua_radiation_acceleration(1 * AU)
        a2 = oumuamua_radiation_acceleration(2 * AU)
        ratio = a1 / a2
        assert abs(ratio - 4.0) < 0.01

    def test_impedance_acceleration_equals_radiation(self) -> None:
        """In AVE, impedance acceleration IS radiation pressure."""
        a_rad = oumuamua_radiation_acceleration(AU)
        a_imp = oumuamua_impedance_acceleration(AU)
        assert abs(a_rad - a_imp) / a_rad < 0.01


class TestSolarAxiom4OnsetRadius:
    """
    Solar Axiom-4 onset radius (internal-field keying).

    🔴 Class renamed from TestOortCloud 2026-08-03 (Oort containment-retraction
    lane). The Oort *containment* claim — "inner Oort Cloud coincides with the
    g = a₀ transition" — was retracted; what these tests pin is a solar-FIELD
    radius, not a population edge. See ave/gravity/solar_impedance.py
    oort_cloud_prediction() for the full retraction record, and note that the
    radius's existence is gated by the unadjudicated internal-vs-total-field
    keying fork (T4), routed to Grant 2026-08-03.
    """

    def test_saturation_radius_order(self) -> None:
        """Saturation radius should be ~10³-10⁵ AU. (Sanity floor, kept.)"""
        r = saturation_radius_au()
        assert 1e3 < r < 1e5, f"r_sat = {r:.0f} AU"

    def test_saturation_radius_pin(self) -> None:
        """
        Pin r_sat = √(GM_☉/a₀) at the honest a₀-provenance band.

        Canonical-chain value: 7438.9 AU, from a₀ = c·H_∞/2π = 1.0719e-10
        m/s² (ave/regime_3_saturated/galactic_rotation.py:56) and G, M_SUN
        from ave.core.constants.

        TOLERANCE, STATED (this is a physics band, not a float-drift band):
        a₀ is itself 10.7% BELOW the empirical MOND a₀ = 1.2e-10 m/s², a
        deficit disclosed at manuscript/ave-kb/vol3/claim-quality.md:259
        ("value is 10.7% below the empirical a₀ ≈ 1.2e-10 m/s²"). Since
        r ∝ a₀^(-1/2), that 10.7% propagates to 5.49% on r_sat: on the
        empirical a₀ the same formula gives 7030.7 AU. The pin is therefore
        asserted at ±5.5% around 7438.9 AU — the number is not meaningful
        to any tighter tolerance, and asserting tighter would overstate it.

        A separate, tighter assertion below pins the CANONICAL CHAIN itself
        (not the physics): if C_0, H_INFINITY, G or M_SUN move, that
        assertion fires and forces a deliberate update rather than silent
        drift. It is labelled as a chain pin, not an accuracy claim.
        """
        r = saturation_radius_au()

        # (i) Physics band: ±5.5% = the a₀-provenance band, derived above.
        r_canonical = 7438.9
        band = 0.055
        assert abs(r - r_canonical) / r_canonical < band, (
            f"r_sat = {r:.1f} AU is outside the stated a₀-provenance band "
            f"{r_canonical} ± {band * 100:.1f}% "
            f"[{r_canonical * (1 - band):.1f}, {r_canonical * (1 + band):.1f}] AU"
        )

        # (ii) Chain pin (NOT an accuracy claim): catches constant drift.
        assert abs(r - r_canonical) < 0.1, (
            f"canonical-chain drift: r_sat = {r:.4f} AU, expected 7438.9 AU. "
            "One of C_0 / H_INFINITY / G / M_SUN moved — update this pin "
            "deliberately, do not widen it."
        )

    def test_onset_prediction_structure(self) -> None:
        """
        Structure of the onset-radius dict AFTER the 2026-08-03 retraction.

        The Hills-cloud comparands (r_hills_inner_au / r_hills_outer_au) were
        DELETED with the containment claim they existed to be compared
        against; this test asserts their absence so they cannot be silently
        reintroduced.
        """
        p = oort_cloud_prediction()
        assert "r_saturation_au" in p
        assert "g_at_saturation" in p
        assert p["g_at_saturation"] == A0_LATTICE

        # Deleted with the retracted containment claim — must stay deleted.
        assert "r_hills_inner_au" not in p
        assert "r_hills_outer_au" not in p

        # And the prediction string must not re-assert population containment.
        assert isinstance(p["prediction"], str)
        assert "coincide" not in p["prediction"].lower()


class TestKirkwoodGaps:
    """Kirkwood gaps as cavity resonances."""

    def test_3_1_resonance(self) -> None:
        """3:1 gap should be at ~2.50 AU."""
        r = kirkwood_gap_radius(3, 1)
        assert abs(r - 2.50) < 0.02

    def test_2_1_resonance(self) -> None:
        """2:1 gap should be at ~3.28 AU."""
        r = kirkwood_gap_radius(2, 1)
        assert abs(r - 3.28) < 0.02

    def test_5_2_resonance(self) -> None:
        """5:2 gap should be at ~2.82 AU."""
        r = kirkwood_gap_radius(5, 2)
        assert abs(r - 2.82) < 0.02

    def test_all_gaps_match(self) -> None:
        """All predicted gaps within 1% of observed."""
        gaps = kirkwood_impedance_model()
        for gap in gaps:
            if gap["r_observed_au"] is not None:
                assert gap["error_pct"] < 1.0, f"{gap['resonance']}: {gap['error_pct']:.2f}% error"

    def test_gap_count(self) -> None:
        gaps = kirkwood_impedance_model()
        assert len(gaps) == 5
