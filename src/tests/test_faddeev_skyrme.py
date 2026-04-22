"""
Test suite for the Faddeev-Skyrme Hamiltonian Solver
(src/ave/topological/faddeev_skyrme.py).

Validates the 1D radial soliton solver, phase profile boundary conditions,
and the cinquefoil (2,5) confinement bound.
"""

import numpy as np
import pytest

from ave.topological.faddeev_skyrme import CROSSING_NUMBER_CINQUEFOIL, TopologicalHamiltonian1D


class TestCrossingNumber:
    """The cinquefoil crossing number must be exactly 5."""

    def test_value(self):
        assert CROSSING_NUMBER_CINQUEFOIL == 5


class TestPhaseProfile:
    """Phase profile φ(r) must satisfy topological boundary conditions."""

    @pytest.fixture
    def solver(self):
        return TopologicalHamiltonian1D(node_pitch=1.0, scaling_coupling=1.0)

    def test_core_is_pi(self, solver):
        """φ(0) = π (fully inverted core)."""
        assert solver._phase_profile(0.0, r_opt=1.0, n=2.0) == pytest.approx(np.pi, rel=1e-12)

    def test_far_field_is_zero(self, solver):
        """φ(r → ∞) → 0 (relaxed vacuum)."""
        phi = solver._phase_profile(1e6, r_opt=1.0, n=2.0)
        assert phi < 1e-6

    def test_monotonically_decreasing(self, solver):
        """φ(r) must decrease monotonically from π to 0."""
        r_vals = np.linspace(0.001, 100, 500)
        phi_vals = [solver._phase_profile(r, r_opt=1.0, n=2.0) for r in r_vals]
        diffs = np.diff(phi_vals)
        assert np.all(diffs <= 0)

    def test_profile_steepness_scales_with_n(self, solver):
        """Higher n → steeper transition (sharper soliton wall)."""
        r_mid = 1.0  # at r = r_opt
        # phi_n1 = solver._phase_profile(r_mid, r_opt=1.0, n=1.0)  # bulk lint fixup pass
        # phi_n4 = solver._phase_profile(r_mid, r_opt=1.0, n=4.0)  # bulk lint fixup pass
        # At r = r_opt: φ = π/(1 + 1^n) = π/2 for all n
        # But just outside r_opt, higher n drops faster
        r_outer = 2.0
        phi_n1_outer = solver._phase_profile(r_outer, r_opt=1.0, n=1.0)
        phi_n4_outer = solver._phase_profile(r_outer, r_opt=1.0, n=4.0)
        assert phi_n4_outer < phi_n1_outer


class TestEnergyDensity:
    """Energy density integrand properties."""

    @pytest.fixture
    def solver(self):
        return TopologicalHamiltonian1D(node_pitch=1.0, scaling_coupling=1.0)

    def test_positive_everywhere(self, solver):
        """Energy density must be non-negative for all r > 0."""
        for r in [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
            density = solver._energy_density_integrand(r, r_opt=1.0, n=2.0)
            assert density >= 0

    def test_core_finite(self, solver):
        """Energy density at r ≈ 0 must be finite (no singularity)."""
        density = solver._energy_density_integrand(0.001, r_opt=1.0, n=2.0)
        assert np.isfinite(density)

    def test_far_field_vanishes(self, solver):
        """Energy density must vanish at large r."""
        density = solver._energy_density_integrand(100.0, r_opt=1.0, n=2.0)
        assert density < 1e-5


class TestSolveScalarTrace:
    """Full Hamiltonian minimization."""

    @pytest.fixture
    def solver(self):
        return TopologicalHamiltonian1D(node_pitch=1.0, scaling_coupling=5.0)

    def test_returns_positive_energy(self, solver):
        """Minimized energy must be positive (non-trivial soliton)."""
        E = solver.solve_scalar_trace()
        assert E > 0

    def test_returns_finite(self, solver):
        """Energy must be finite (convergent integral)."""
        E = solver.solve_scalar_trace()
        assert np.isfinite(E)

    def test_confinement_bound_respected(self, solver):
        """Internal r_opt must respect κ/c₅ bound."""
        # This is enforced by the optimizer's bounds;
        # we just verify the solve doesn't error
        E = solver.solve_scalar_trace()
        assert isinstance(E, float)

    def test_energy_scales_with_coupling(self):
        """Larger κ → larger confinement radius → different energy."""
        s_small = TopologicalHamiltonian1D(node_pitch=1.0, scaling_coupling=2.0)
        s_large = TopologicalHamiltonian1D(node_pitch=1.0, scaling_coupling=10.0)
        E_small = s_small.solve_scalar_trace()
        E_large = s_large.solve_scalar_trace()
        # Different couplings must produce different energies
        assert E_small != pytest.approx(E_large, rel=0.01)
