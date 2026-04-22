"""
Tests for ave.axioms.spectral_gap

Verifies the 4-step mass gap argument:
  1. Lattice existence (finite DOF)
  2. Discrete dispersion (spectral gap)
  3. Confinement (Γ → -1)
  4. Positive mass gap for all crossing numbers
"""

import numpy as np
import pytest

from ave.axioms.spectral_gap import (
    boundary_reflection_coefficient,
    brillouin_zone_edge,
    confinement_radius,
    lattice_degrees_of_freedom,
    lattice_dispersion,
    mass_gap_energy,
    mass_gap_is_positive,
    maximum_frequency,
    minimum_excitation_energy,
    minimum_excitation_energy_eV,
)
from ave.core.constants import C_0, KAPPA_FS, L_NODE, M_E

# ── Step 1: Lattice Existence ──


class TestLatticeExistence:

    def test_dof_positive(self):
        """Any finite volume has finite DOF."""
        N = lattice_degrees_of_freedom(1.0)  # 1 m³
        assert N > 0
        assert np.isfinite(N)

    def test_dof_scales_with_volume(self):
        """DOF scales linearly with volume."""
        N1 = lattice_degrees_of_freedom(1.0)
        N2 = lattice_degrees_of_freedom(2.0)
        assert abs(N2 / N1 - 2.0) < 1e-10

    def test_dof_per_cell(self):
        """One cell = one DOF."""
        V_cell = L_NODE**3
        assert abs(lattice_degrees_of_freedom(V_cell) - 1.0) < 1e-10


# ── Step 2: Discrete Dispersion ──


class TestDispersion:

    def test_zero_at_zero(self):
        """ω(k=0) = 0 — the DC mode."""
        assert lattice_dispersion(0.0) == 0.0

    def test_low_k_linear(self):
        """At low k, ω ≈ ck (recovers continuum Maxwell)."""
        k = 1e6  # Much less than π/ℓ ≈ 8.13e12
        omega = lattice_dispersion(k)
        omega_continuum = C_0 * k
        assert abs(omega / omega_continuum - 1.0) < 1e-6

    def test_brillouin_zone_maximum(self):
        """Maximum frequency at k = π/ℓ."""
        k_max = brillouin_zone_edge()
        omega_max = lattice_dispersion(k_max)
        assert abs(omega_max - maximum_frequency()) < 1.0  # numerics

    def test_dispersion_bounded(self):
        """ω cannot exceed 2c/ℓ (the UV cutoff)."""
        omega_max = maximum_frequency()
        # Try k beyond the Brillouin zone — should fold back
        k_values = np.linspace(0, 3 * brillouin_zone_edge(), 1000)
        omegas = lattice_dispersion(k_values)
        assert np.all(omegas <= omega_max + 1.0)

    def test_minimum_energy_is_electron_mass(self):
        """E_min = ℏc/ℓ_node = m_e c²."""
        E_min = minimum_excitation_energy()
        E_electron = M_E * C_0**2
        assert abs(E_min / E_electron - 1.0) < 1e-10

    def test_minimum_energy_eV(self):
        """E_min ≈ 511 keV."""
        E_eV = minimum_excitation_energy_eV()
        assert abs(E_eV / 511e3 - 1.0) < 0.01  # Within 1%


# ── Step 3: Confinement ──


class TestConfinement:

    def test_confinement_decreases_with_crossing(self):
        """Higher crossing number → smaller confinement radius."""
        r5 = confinement_radius(KAPPA_FS, 5)
        r7 = confinement_radius(KAPPA_FS, 7)
        r9 = confinement_radius(KAPPA_FS, 9)
        assert r7 < r5
        assert r9 < r7

    def test_confinement_positive(self):
        """Confinement radius is always positive."""
        for c in [3, 5, 7, 9, 11, 13]:
            assert confinement_radius(KAPPA_FS, c) > 0

    def test_confinement_rejects_low_crossing(self):
        """Crossing number < 3 is invalid."""
        with pytest.raises(ValueError):
            confinement_radius(KAPPA_FS, 2)

    def test_total_reflection_at_boundary(self):
        """Γ → -1 when Z_knot → 0 (total reflection)."""
        Gamma = boundary_reflection_coefficient(Z_knot=0.0)
        assert abs(Gamma - (-1.0)) < 1e-10

    def test_near_total_reflection(self):
        """Γ ≈ -1 for very small Z_knot (total reflection)."""
        Gamma = boundary_reflection_coefficient(Z_knot=1e-10)
        # For Z_knot → 0, the explicit Z=0 branch returns -1.
        # For infinitesimally small Z_knot, |Γ| → 1 (total reflection).
        assert abs(Gamma) > 0.99


# ── Step 4: Mass Gap ──


class TestMassGap:

    def test_electron_mass_gap(self):
        """Δ(c=3) ≈ 0.511 MeV (electron mass)."""
        delta = mass_gap_energy(crossing_number=3)
        assert abs(delta - 0.511) < 0.01  # Within 10 keV

    def test_proton_mass_gap(self):
        """Δ(c=5) ≈ 938 MeV (proton mass)."""
        delta = mass_gap_energy(crossing_number=5)
        assert abs(delta / 938.0 - 1.0) < 0.01  # Within 1%

    def test_gap_positive_all_crossings(self):
        """Mass gap Δ > 0 for all crossing numbers 3-13."""
        result = mass_gap_is_positive(max_crossing=13)
        assert result["gap_positive"] is True
        for c, data in result["crossings"].items():
            assert data["gap_positive"] is True
            assert data["mass_MeV"] > 0

    def test_mass_increases_with_crossing(self):
        """Higher crossing number → heavier particle."""
        m3 = mass_gap_energy(3)
        m5 = mass_gap_energy(5)
        m7 = mass_gap_energy(7)
        assert m5 > m3
        assert m7 > m5

    def test_gap_is_electron(self):
        """The absolute minimum mass is the electron."""
        result = mass_gap_is_positive()
        assert result["gap_particle"] == "electron"
        assert result["mass_gap_MeV"] < 1.0  # < 1 MeV
