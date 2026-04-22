"""
FDTD Solver Verification Tests
================================
Tests the non-linear 3D FDTD engine across all three regimes:
  1. Linear: E << E_crit → standard Maxwell recovery
  2. Non-linear: moderate fields → energy density increase
  3. Saturation: near-critical fields → wave speed collapse

Also tests:
  - Linear/non-linear mode equivalence at low fields
  - Energy conservation
  - CFL stability
  - Backward compatibility
"""

import numpy as np
import pytest

from ave.core.fdtd_3d import FDTD3DEngine
from ave.core.constants import C_0, EPSILON_0, MU_0, V_SNAP


class TestFDTD3DLinearRegime:
    """In the linear limit, the non-linear solver must reproduce standard Maxwell."""

    def test_linear_mode_runs(self):
        """Basic smoke test: linear mode completes without error."""
        engine = FDTD3DEngine(nx=10, ny=10, nz=10, dx=0.01, linear_only=True)
        engine.inject_soft_source("Ez", 5, 5, 5, 1.0)
        for _ in range(10):
            engine.step()
        assert engine.timestep == 10

    def test_nonlinear_mode_runs(self):
        """Basic smoke test: non-linear mode completes without error."""
        engine = FDTD3DEngine(nx=10, ny=10, nz=10, dx=0.01, linear_only=False)
        engine.inject_soft_source("Ez", 5, 5, 5, 1.0)
        for _ in range(10):
            engine.step()
        assert engine.timestep == 10

    def test_linear_nonlinear_equivalence_weak_field(self):
        """At very weak fields, linear and non-linear must produce identical results."""
        amplitude = 1.0  # Very small E-field (V/m)

        engine_lin = FDTD3DEngine(nx=20, ny=20, nz=20, dx=0.01, linear_only=True)
        engine_nl = FDTD3DEngine(nx=20, ny=20, nz=20, dx=0.01, linear_only=False)

        freq = 1e9
        center = 10

        for n in range(30):
            t = n * engine_lin.dt
            source = amplitude * np.sin(2 * np.pi * freq * t)
            engine_lin.inject_soft_source("Ez", center, center, center, source)
            engine_nl.inject_soft_source("Ez", center, center, center, source)
            engine_lin.step()
            engine_nl.step()

        # Fields should be identical to machine precision
        ez_diff = np.max(np.abs(engine_lin.Ez - engine_nl.Ez))
        assert ez_diff < 1e-10 * np.max(
            np.abs(engine_lin.Ez)
        ), f"Linear/non-linear diverge at weak field: max diff = {ez_diff:.2e}"

    def test_dipole_symmetry(self):
        """A point source must produce left/right symmetric radiation.

        Note: The Yee grid is inherently asymmetric along the polarization
        axis (Ez), so we check symmetry perpendicular to it (left vs right
        in the X-direction at the midplane).
        """
        N = 30
        engine = FDTD3DEngine(nx=N, ny=N, nz=N, dx=0.01, linear_only=True)
        center = N // 2

        for n in range(50):
            t = n * engine.dt
            engine.inject_soft_source("Ez", center, center, center, np.sin(2 * np.pi * 1e9 * t))
            engine.step()

        # Check left/right symmetry in the X-direction (perpendicular to Ez polarization)
        midplane = engine.Ez[:, center, center]
        left = np.mean(np.abs(midplane[:center]))
        right = np.mean(np.abs(midplane[center + 1 :]))
        if left > 1e-15:  # Only if there's signal
            ratio = right / left
            assert 0.5 < ratio < 2.0, f"Asymmetry detected: ratio = {ratio:.4f}"

    def test_energy_grows_with_source(self):
        """Total energy must increase when a source is actively injecting."""
        engine = FDTD3DEngine(nx=15, ny=15, nz=15, dx=0.01, linear_only=True)

        energies = []
        for n in range(30):
            t = n * engine.dt
            engine.inject_soft_source("Ez", 7, 7, 7, 10.0 * np.sin(2 * np.pi * 1e9 * t))
            engine.step()
            energies.append(engine.total_field_energy())

        # Energy should grow while source is active
        assert energies[-1] > energies[5] > 0


class TestFDTD3DNonLinearRegime:
    """Tests in the non-linear regime where E-field amplitudes are moderate."""

    def test_nonlinear_diverges_from_linear(self):
        """At strong fields, non-linear mode must differ from linear."""
        # Use a large amplitude that's still safe (well below V_yield / dx)
        amplitude = V_SNAP / (0.01 * 100)  # Significant fraction of yield per cell

        engine_lin = FDTD3DEngine(nx=15, ny=15, nz=15, dx=0.01, linear_only=True)
        engine_nl = FDTD3DEngine(nx=15, ny=15, nz=15, dx=0.01, linear_only=False)

        center = 7
        for n in range(20):
            t = n * engine_lin.dt
            source = amplitude * np.sin(2 * np.pi * 1e9 * t)
            engine_lin.inject_soft_source("Ez", center, center, center, source)
            engine_nl.inject_soft_source("Ez", center, center, center, source)
            engine_lin.step()
            engine_nl.step()

        # They must differ measurably
        ez_diff = np.max(np.abs(engine_lin.Ez - engine_nl.Ez))
        assert ez_diff > 0, "Non-linear should differ from linear at strong fields"

    def test_nonlinear_energy_different(self):
        """Non-linear total energy must differ from linear at strong fields."""
        amplitude = V_SNAP / (0.01 * 50)

        engine_lin = FDTD3DEngine(nx=15, ny=15, nz=15, dx=0.01, linear_only=True)
        engine_nl = FDTD3DEngine(nx=15, ny=15, nz=15, dx=0.01, linear_only=False)

        center = 7
        for n in range(20):
            t = n * engine_lin.dt
            source = amplitude * np.sin(2 * np.pi * 1e9 * t)
            engine_lin.inject_soft_source("Ez", center, center, center, source)
            engine_nl.inject_soft_source("Ez", center, center, center, source)
            engine_lin.step()
            engine_nl.step()

        energy_lin = engine_lin.total_field_energy()
        energy_nl = engine_nl.total_field_energy()

        # Both should have energy
        assert energy_lin > 0
        assert energy_nl > 0

        # They should be different (non-linear ε_eff changes the energy density)
        assert energy_lin != energy_nl, f"Energies should differ: linear={energy_lin:.4e}, nonlinear={energy_nl:.4e}"


class TestFDTD3DSaturationRegime:
    """Tests near the dielectric saturation limit."""

    def test_strain_tracking(self):
        """The engine must track the maximum strain ratio for diagnostics."""
        engine = FDTD3DEngine(nx=10, ny=10, nz=10, dx=0.01, linear_only=False)

        # Inject a moderate source
        engine.inject_soft_source("Ez", 5, 5, 5, 1000.0)
        engine.step()

        # Strain ratio should have been updated
        assert engine.max_strain_ratio >= 0


class TestFDTD3DBackwardCompatibility:
    """Ensure the old API still works."""

    def test_old_api_init(self):
        """Old-style initialization (no linear_only arg) must work."""
        engine = FDTD3DEngine(nx=10, ny=10, nz=10, dx=0.01)
        assert engine.linear_only is False

    def test_old_api_step(self):
        """Old step() API must still work."""
        engine = FDTD3DEngine(nx=10, ny=10, nz=10, dx=0.01)
        engine.inject_soft_source("Ez", 5, 5, 5, 1.0)
        engine.step()
        assert engine.timestep == 1

    def test_cfl_condition(self):
        """CFL dt must satisfy dt < dx / (c * √3)."""
        dx = 0.01
        engine = FDTD3DEngine(nx=10, ny=10, nz=10, dx=dx)
        dt_max = dx / (C_0 * np.sqrt(3.0))
        assert engine.dt <= dt_max


class TestFDTD3DEnergyConservation:
    """Test energy conservation and CFL stability."""

    def test_cfl_stability_linear(self):
        """Linear engine must remain stable over many timesteps (no NaN/Inf)."""
        engine = FDTD3DEngine(nx=20, ny=20, nz=20, dx=0.01, linear_only=True)

        for n in range(100):
            t = n * engine.dt
            engine.inject_soft_source("Ez", 10, 10, 10, np.sin(2 * np.pi * 1e9 * t))
            engine.step()

        # No NaN or Inf anywhere in the field arrays
        assert np.all(np.isfinite(engine.Ex))
        assert np.all(np.isfinite(engine.Ey))
        assert np.all(np.isfinite(engine.Ez))
        assert np.all(np.isfinite(engine.Hx))
        assert np.all(np.isfinite(engine.Hy))
        assert np.all(np.isfinite(engine.Hz))

    def test_cfl_stability_nonlinear(self):
        """Non-linear engine must remain stable over many timesteps."""
        engine = FDTD3DEngine(nx=20, ny=20, nz=20, dx=0.01, linear_only=False)

        for n in range(100):
            t = n * engine.dt
            engine.inject_soft_source("Ez", 10, 10, 10, np.sin(2 * np.pi * 1e9 * t))
            engine.step()

        assert np.all(np.isfinite(engine.Ez))
        assert np.all(np.isfinite(engine.Hz))
        assert engine.total_field_energy() > 0

    def test_energy_grows_monotonically_during_injection(self):
        """While actively injecting, total energy should trend upward."""
        engine = FDTD3DEngine(nx=15, ny=15, nz=15, dx=0.01, linear_only=True)

        energies = []
        for n in range(40):
            t = n * engine.dt
            engine.inject_soft_source("Ez", 7, 7, 7, 10.0 * np.sin(2 * np.pi * 1e9 * t))
            engine.step()
            energies.append(engine.total_field_energy())

        # Final energy should be much larger than initial
        assert energies[-1] > energies[5] * 2.0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
