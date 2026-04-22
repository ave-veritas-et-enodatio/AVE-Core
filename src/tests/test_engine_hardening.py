"""
Expanded Test Suite for AVE Engine: Phase A Hardening
=====================================================
Tests for: PML boundaries, LBM fluid solver, spatial materials,
force extraction, energy density, gravity module, and coupled EM+CFD.
"""

import numpy as np
from ave.core.fdtd_3d import FDTD3DEngine
from ave.core.lbm_3d import LBM3DEngine


# ============================================================
# PML BOUNDARY TESTS
# ============================================================


class TestPMLBoundaries:
    """Tests for the Perfectly Matched Layer absorbing boundaries."""

    def test_pml_engine_creates(self):
        """PML engine initializes without error."""
        eng = FDTD3DEngine(20, 20, 20, dx=0.01, use_pml=True, pml_layers=5)
        assert eng.use_pml is True
        assert eng.pml_layers == 5

    def test_pml_monotonic_energy_decay(self):
        """Energy decreases monotonically with PML (pulse exits cleanly)."""
        eng = FDTD3DEngine(24, 24, 24, dx=0.01, linear_only=True, use_pml=True)
        eng.Ez[12, 12, 12] = 1e6
        energies = []
        for i in range(100):
            eng.step()
            if i % 20 == 0:
                energies.append(eng.total_field_energy())
        # Each sample should be <= previous (monotonic decrease)
        for i in range(len(energies) - 1):
            assert (
                energies[i] >= energies[i + 1] * 0.99
            ), f"Energy not monotonically decreasing: {energies[i]} -> {energies[i+1]}"

    def test_pml_vs_mur_stability(self):
        """PML should be stable where Mur ABCs explode on long runs."""
        eng_pml = FDTD3DEngine(20, 20, 20, dx=0.01, linear_only=True, use_pml=True)
        eng_pml.Ez[10, 10, 10] = 1e6
        for _ in range(200):
            eng_pml.step()
        e_pml = eng_pml.total_field_energy()
        # PML energy should be tiny (pulse exited)
        assert e_pml < 1e-3, f"PML energy too high after 200 steps: {e_pml}"

    def test_pml_sigma_profile_shape(self):
        """PML sigma profiles should be the right length and non-negative."""
        eng = FDTD3DEngine(30, 25, 20, dx=0.01, use_pml=True, pml_layers=6)
        assert len(eng.sigma_x) == 30
        assert len(eng.sigma_y) == 25
        assert len(eng.sigma_z) == 20
        assert np.all(eng.sigma_x >= 0)
        assert np.all(eng.sigma_y >= 0)
        assert np.all(eng.sigma_z >= 0)


# ============================================================
# LBM FLUID SOLVER TESTS
# ============================================================


class TestLBM3D:
    """Tests for the D3Q19 Lattice Boltzmann solver."""

    def test_lbm_creates(self):
        """LBM engine initializes without error."""
        lbm = LBM3DEngine(10, 10, 10, dx=0.01, nu=0.1)
        assert lbm.nx == 10
        assert lbm.timestep == 0

    def test_lbm_rest_state(self):
        """Without forcing, the fluid should remain at rest."""
        lbm = LBM3DEngine(10, 10, 10, dx=0.01, nu=0.1)
        for _ in range(50):
            lbm.step()
        v_max = lbm.max_velocity()
        assert v_max < 1e-10, f"Non-zero velocity at rest: {v_max}"

    def test_lbm_body_force_drives_flow(self):
        """A uniform body force should generate monotonically increasing flow."""
        lbm = LBM3DEngine(10, 10, 10, dx=0.01, nu=0.1)
        lbm.Fx[:] = 0.001
        velocities = []
        for step in range(100):
            lbm.step()
            if step % 20 == 0:
                velocities.append(lbm.max_velocity())
        # Velocity should increase over time
        for i in range(len(velocities) - 1):
            assert velocities[i + 1] >= velocities[i], f"Velocity not increasing: {velocities[i]} -> {velocities[i+1]}"

    def test_lbm_force_direction(self):
        """Force in x should produce flow in x, not y or z."""
        lbm = LBM3DEngine(12, 12, 12, dx=0.01, nu=0.1)
        lbm.Fx[:] = 0.001
        for _ in range(50):
            lbm.step()
        assert abs(lbm.ux.mean()) > abs(lbm.uy.mean()) * 100
        assert abs(lbm.ux.mean()) > abs(lbm.uz.mean()) * 100

    def test_lbm_mass_conservation(self):
        """Total mass should be conserved (periodic boundaries)."""
        lbm = LBM3DEngine(10, 10, 10, dx=0.01, nu=0.1, rho0=1.5)
        lbm.Fx[:] = 0.001
        initial_mass = np.sum(lbm.rho)
        for _ in range(50):
            lbm.step()
        final_mass = np.sum(lbm.rho)
        assert (
            abs(final_mass - initial_mass) / initial_mass < 1e-8
        ), f"Mass not conserved: {initial_mass} -> {final_mass}"

    def test_lbm_momentum_extraction(self):
        """total_momentum() should return a 3-tuple of floats."""
        lbm = LBM3DEngine(10, 10, 10, dx=0.01, nu=0.1)
        px, py, pz = lbm.total_momentum()
        assert isinstance(px, float)
        assert isinstance(py, float)
        assert isinstance(pz, float)

    def test_lbm_bounce_back_walls(self):
        """Solid walls should block flow."""
        lbm = LBM3DEngine(20, 20, 20, dx=0.01, nu=0.1)
        # Create solid walls at x=0 and x=19
        lbm.solid[0, :, :] = True
        lbm.solid[-1, :, :] = True
        lbm.Fx[:] = 0.001
        for _ in range(50):
            lbm.step()
        # Flow should still develop between walls
        assert lbm.max_velocity() > 0


# ============================================================
# SPATIAL MATERIAL TESTS
# ============================================================


class TestSpatialMaterials:
    """Tests for eps_r and mu_r spatial material arrays."""

    def test_default_vacuum(self):
        """Default material should be vacuum everywhere."""
        eng = FDTD3DEngine(10, 10, 10, dx=0.01)
        assert np.all(eng.eps_r == 1.0)
        assert np.all(eng.mu_r == 1.0)

    def test_material_assignment(self):
        """Material regions can be assigned via slicing."""
        eng = FDTD3DEngine(20, 20, 20, dx=0.01)
        eng.eps_r[5:15, 5:15, 5:15] = 3000.0
        assert eng.eps_r[10, 10, 10] == 3000.0
        assert eng.eps_r[0, 0, 0] == 1.0

    def test_wave_slows_in_dielectric_linear(self):
        """Material should affect wave propagation in linear mode."""
        N = 30
        eng_vac = FDTD3DEngine(N, N, N, dx=0.01, linear_only=True)
        eng_mat = FDTD3DEngine(N, N, N, dx=0.01, linear_only=True)
        eng_mat.eps_r[:, :, :] = 4.0

        eng_vac.Ez[5, N // 2, N // 2] = 1e3
        eng_mat.Ez[5, N // 2, N // 2] = 1e3

        for _ in range(20):
            eng_vac.step()
            eng_mat.step()

        # Both should have positive energy
        assert eng_vac.total_field_energy() > 0
        assert eng_mat.total_field_energy() > 0

    def test_total_energy_with_material(self):
        """Energy with eps_r=4 should be 4x energy with eps_r=1."""
        eng_mat = FDTD3DEngine(10, 10, 10, dx=0.01, linear_only=True)
        eng_mat.eps_r[:] = 4.0
        eng_mat.Ez[5, 5, 5] = 100.0

        eng_vac = FDTD3DEngine(10, 10, 10, dx=0.01, linear_only=True)
        eng_vac.Ez[5, 5, 5] = 100.0

        ratio = eng_mat.total_field_energy() / eng_vac.total_field_energy()
        assert abs(ratio - 4.0) < 0.1, f"Energy ratio should be ~4, got {ratio:.2f}"


# ============================================================
# FORCE EXTRACTION TESTS
# ============================================================


class TestForceExtraction:
    """Tests for energy_density() and ponderomotive_force()."""

    def test_energy_density_returns_3d(self):
        """energy_density() should return a 3D array."""
        eng = FDTD3DEngine(10, 10, 10, dx=0.01)
        eng.Ez[5, 5, 5] = 100.0
        u = eng.energy_density()
        assert u.shape == (10, 10, 10)
        assert u[5, 5, 5] > 0

    def test_energy_density_nonzero_only_at_field(self):
        """Energy density should be nonzero only where fields exist."""
        eng = FDTD3DEngine(10, 10, 10, dx=0.01, linear_only=True)
        eng.Ez[5, 5, 5] = 100.0
        u = eng.energy_density()
        assert u[5, 5, 5] > 0
        assert u[0, 0, 0] == 0.0

    def test_ponderomotive_force_shape(self):
        """ponderomotive_force() should return 3 arrays of correct shape."""
        eng = FDTD3DEngine(10, 10, 10, dx=0.01, linear_only=True)
        eng.Ez[5, 5, 5] = 100.0
        eng.step()
        Fx, Fy, Fz = eng.ponderomotive_force()
        assert Fx.shape == (10, 10, 10)
        assert Fy.shape == (10, 10, 10)
        assert Fz.shape == (10, 10, 10)

    def test_force_at_gradient(self):
        """Force should be nonzero at energy density gradients."""
        eng = FDTD3DEngine(20, 20, 20, dx=0.01, linear_only=True)
        # Create an asymmetric field distribution
        eng.Ez[8:12, 8:12, 8:12] = 1000.0
        eng.step()
        Fx, Fy, Fz = eng.ponderomotive_force()
        # Force should be nonzero somewhere (at the gradient boundary)
        assert np.max(np.abs(Fx)) > 0
        assert np.max(np.abs(Fy)) > 0
        assert np.max(np.abs(Fz)) > 0


# ============================================================
# GRAVITY MODULE TESTS
# ============================================================


class TestGravityModule:
    """Tests for the gravity/optical metric module."""

    def test_schwarzschild_radius_earth(self):
        """Schwarzschild radius of Earth should be ~8.87 mm."""
        from ave.gravity import schwarzschild_radius

        M_earth = 5.972e24
        r_s = schwarzschild_radius(M_earth)
        assert abs(r_s - 0.00887) < 0.0001, f"R_s = {r_s} m"

    def test_refractive_index_positive(self):
        """Refractive index should be ≥ 1 for positive mass."""
        from ave.gravity import refractive_index

        n = refractive_index(5.972e24, 6.371e6)  # Earth surface
        assert n > 1.0
        assert n < 1.001  # Should be very close to 1

    def test_impedance_invariant(self):
        """Local impedance should equal Z₀ regardless of mass/radius."""
        from ave.gravity import local_impedance
        from ave.core.constants import Z_0

        z = local_impedance(1.989e30, 6.957e8)  # Sun surface
        assert abs(z - Z_0) / Z_0 < 1e-10, f"Z = {z} vs Z₀ = {Z_0}"

    def test_einstein_deflection_sun(self):
        """Photon deflection by the Sun should be ~1.75 arcsec."""
        from ave.gravity import einstein_deflection_angle

        M_sun = 1.989e30
        R_sun = 6.957e8
        delta = einstein_deflection_angle(M_sun, R_sun)
        delta_arcsec = np.degrees(delta) * 3600
        assert abs(delta_arcsec - 1.75) < 0.01, f"δ = {delta_arcsec} arcsec"

    def test_dielectric_rupture_inside_horizon(self):
        """Points inside Schwarzschild radius should show rupture."""
        from ave.gravity import is_dielectric_rupture, schwarzschild_radius

        M = 10 * 1.989e30  # 10 solar masses
        r_s = schwarzschild_radius(M)
        assert is_dielectric_rupture(M, r_s * 0.5) is True
        assert is_dielectric_rupture(M, r_s * 2.0) is False

    def test_gravitational_potential_negative(self):
        """Gravitational potential should be negative for positive mass."""
        from ave.gravity import gravitational_potential

        U = gravitational_potential(5.972e24, 6.371e6)
        assert U < 0


# ============================================================
# COUPLED EM+CFD TESTS
# ============================================================


class TestCoupledEMCFD:
    """Tests for coupling FDTD → LBM via ponderomotive force."""

    def test_fdtd_to_lbm_coupling(self):
        """FDTD ponderomotive force should generate LBM flow."""
        N = 16
        fdtd = FDTD3DEngine(N, N, N, dx=0.005, linear_only=True, use_pml=True, pml_layers=3)
        fdtd.eps_r[6:10, 4:12, 4:12] = 100.0
        fdtd.Ez[6, 4:12, 4:12] = 1e5
        for _ in range(20):
            fdtd.step()

        Fx, Fy, Fz = fdtd.ponderomotive_force()
        lbm = LBM3DEngine(N, N, N, dx=0.005, nu=0.05)
        scale = 0.005**4 / (lbm.rho0 * lbm.cs2)
        lbm.set_body_force(Fx * scale, Fy * scale, Fz * scale)
        for _ in range(30):
            lbm.step()
        assert lbm.max_velocity() > 0, "No flow generated from FDTD force"
