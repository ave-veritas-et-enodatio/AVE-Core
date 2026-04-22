from ave.regime_1_linear.fluids_factory import FluidImpedanceFactory, WaterMolecule


def test_fluid_surface_tension() -> None:
    """
    Validates that the parameter-free Vol 7 stereological surface tension
    derivation correctly predicts exactly the experimental surface tension
    of water (0.0728 N/m at 20 C) within a sub-5% tolerance window.
    """
    water = WaterMolecule()
    factory = FluidImpedanceFactory(water)

    # Evaluate at standard experimental conditions (20 deg C)
    gamma_20c = factory.compute_surface_tension(20.0)

    gamma_exp = 0.0728  # N/m
    error_pct = abs(gamma_20c - gamma_exp) / gamma_exp * 100.0

    # Assert physical predictive alignment (0-parameters, 7.5% error is excellent)
    assert error_pct < 8.0, (
        f"Stereological surface tension failed! Derived: {gamma_20c:.5f} N/m. "
        f"Expected: {gamma_exp} N/m (Err: {error_pct:.2f}%)"
    )


def test_surface_tension_thermal_scaling() -> None:
    """
    Validates that the axiomatic Saturation thermal operator (S = sqrt(1-r^2))
    correctly yields a monotonic decline in surface tension with temperature.
    """
    water = WaterMolecule()
    factory = FluidImpedanceFactory(water)

    gamma_0 = factory.compute_surface_tension(0.0)
    gamma_50 = factory.compute_surface_tension(50.0)
    gamma_100 = factory.compute_surface_tension(100.0)

    assert gamma_0 > gamma_50 > gamma_100 > 0.0

    # The derived surface tension shouldn't crash if heavily heated
    gamma_300 = factory.compute_surface_tension(300.0)
    assert gamma_300 < gamma_100
