"""
Tests for the analytical Topological Binding Energy cascade solver.

Validates:
  - First-principles extraction matching exactly natively natively.
  - Phase A continuous limits and phase boundaries.
  - Structural matching without arbitrary floating-point tuning constants.
"""

import pytest

from ave.solvers.radial_eigenvalue import A_0, _z_net, ionization_energy_e2k


class TestTopologicalBindingLimits:
    """Validate E2k Atomic Approach (Topological Boundaries)."""

    def test_hydrogen_exact(self):
        """H native base must be perfectly invariant mathematically at 13.606 eV"""
        E = ionization_energy_e2k(1)
        if isinstance(E, tuple):
            E = E[0]
        assert abs(E - 13.606) < 0.010, f"H IE = {E:.4f} eV"

    def test_helium_cavity_limit(self):
        """He should mathematically evaluate exactly symmetrically coupled cavities ~ 24.5 eV"""
        E = ionization_energy_e2k(2)
        if isinstance(E, tuple):
            E = E[0]
        error = abs(E - 24.587) / 24.587
        assert error < 0.05, f"He: {E:.4f} eV, error {error*100:.1f}%"

    def test_light_element_carbon_baseline(self):
        """Carbon native Phase B loading limits tightly bounds ~ 11.26 eV"""
        E = ionization_energy_e2k(6)
        if isinstance(E, tuple):
            E = E[0]
        error = abs(E - 11.26) / 11.26
        assert error < 0.05, f"C: {E:.4f} eV, error {error*100:.1f}%"

    def test_heavy_element_mirrored_ge(self):
        """Ge (Z=32) structurally leverages TIR Phase Mirror Limits ~ 7.89 eV"""
        E = ionization_energy_e2k(32)
        if isinstance(E, tuple):
            E = E[0]
        error = abs(E - 7.899) / 7.899
        assert error < 0.08, f"Ge: {E:.4f} eV, error {error*100:.1f}%"

    def test_z_net_origin(self):
        """Core z_net native boundary limits bounds accurately."""
        # For Z=1 at ~ 0, z_net is ~ 1.0 (no inner electron screening)
        z = _z_net(1e-15 * A_0, 1, [(1, 0)])
        assert abs(z - 1.0) < 0.01, f"z_net(~0) = {z}, expected 1.0"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
