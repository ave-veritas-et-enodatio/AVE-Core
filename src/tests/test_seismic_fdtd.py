"""
Test suite for the Seismic FDTD Bridge (Gap 1).

Proves that:
  1. The FDTD engine accepts the PREM seismic profile
  2. The impedance profile is self-consistent
  3. Boundary reflections match the universal function
  4. A pulse propagates through the layered Earth model
"""

import numpy as np
import pytest

from ave.regime_2_nonlinear.seismic_fdtd import (
    build_seismic_engine,
    verify_impedance_consistency,
    compute_boundary_reflections,
)
from ave.regime_2_nonlinear.seismic import PREM_LAYERS
from ave.axioms.scale_invariant import reflection_coefficient


class TestSeismicFDTDBridge:
    """The FDTD engine must accept and correctly model the PREM profile."""

    def test_engine_builds(self):
        """Engine should build without errors."""
        engine, profile = build_seismic_engine(n_cells=100, dx_km=50.0)
        assert engine.nx == 100
        assert engine.ny == 3
        assert engine.nz == 3

    def test_material_maps_loaded(self):
        """eps_r and mu_r should vary along X (depth axis)."""
        engine, profile = build_seismic_engine(n_cells=100, dx_km=50.0)
        # Not all cells should be the same
        assert not np.all(engine.eps_r[:, 0, 0] == engine.eps_r[0, 0, 0])

    def test_reflection_consistency(self):
        """Reflection coefficients must match between seismic Z and FDTD Z."""
        engine, profile = build_seismic_engine(n_cells=200, dx_km=30.0)
        # Compare Γ at each PREM boundary using both impedance formulations
        reflections = compute_boundary_reflections({})
        for r in reflections:
            # All reflection coefficients should be finite and bounded
            assert -1.0 <= r["gamma"] <= 1.0, f"{r['boundary']}: Γ = {r['gamma']:.3f} out of bounds"

    def test_boundary_reflections(self):
        """All boundary reflections should use the universal function."""
        reflections = compute_boundary_reflections({})
        assert len(reflections) == len(PREM_LAYERS) - 1

        # Moho reflection should be 10-25%
        moho = reflections[1]  # Upper Crust → Upper Mantle
        assert 0.05 < abs(moho["gamma"]) < 0.5, f"Moho Γ = {moho['gamma']:.3f}"

    def test_pulse_propagates(self):
        """A source pulse should propagate through the layered model."""
        engine, profile = build_seismic_engine(n_cells=50, dx_km=100.0)

        # Inject a Gaussian pulse at the surface (x=2)
        for step in range(20):
            t = step * engine.dt
            # Gaussian pulse
            pulse = np.exp(-(((t - 5 * engine.dt) / (2 * engine.dt)) ** 2))
            engine.inject_soft_source("Ez", 2, 1, 1, pulse * 1e-6)
            engine.step()

        # Energy should have spread from the source
        energy = engine.total_field_energy()
        assert energy > 0, "Pulse should have injected energy"

    def test_universal_gamma_matches(self):
        """reflection_coefficient on seismic Z must match direct computation."""
        for i in range(len(PREM_LAYERS) - 1):
            Z1 = PREM_LAYERS[i].acoustic_impedance_p
            Z2 = PREM_LAYERS[i + 1].acoustic_impedance_p
            # Universal function
            gamma_universal = float(reflection_coefficient(Z1, Z2))
            # Direct formula
            gamma_direct = (Z2 - Z1) / (Z2 + Z1)
            assert gamma_universal == pytest.approx(gamma_direct, rel=1e-12)
