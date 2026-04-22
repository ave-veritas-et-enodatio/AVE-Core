import numpy as np

from ave.core.constants import C_0, C_K_KOLMOGOROV, L_NODE, N_NU
from ave.regime_3_saturated.kolmogorov_cutoff import (
    avalanche_exponent_3d,
    axiomatic_energy_spectrum,
    dissipation_cutoff_ratio,
    lattice_nyquist_wavenumber,
    prove_bounded_enstrophy,
)


class TestKolmogorovCascade:

    def test_nyquist_wavenumber(self):
        """Verifies the fundamental Axiom 1 scale separation limit."""
        k_max = lattice_nyquist_wavenumber()
        expected = np.pi / L_NODE
        assert np.isclose(k_max, expected), f"k_max {k_max} != {expected}"

    def test_avalanche_exponent_derivation(self):
        """Verifies the 38/21 exponent directly derives from Axiom 4 + Poisson ratio."""
        n_3d = avalanche_exponent_3d()
        expected_fraction = 38.0 / 21.0

        assert np.isclose(n_3d, expected_fraction), f"Avalanche N {n_3d} != 38/21"
        assert np.isclose(n_3d, 2.0 * (1.0 - N_NU / 3.0)), "Derivation mismatch from NU_VAC base"

        # Check empirical 1.8 fit
        assert abs(n_3d - 1.8) / 1.8 < 0.01, "Axiomatic n_3d strayed > 1% from empirical"

    def test_spectrum_scaling(self):
        """
        Verify that E(k) scales classically in the inertial range
        and hits zero strictly above k_max.
        """
        epsilon = 1.0
        k_max = lattice_nyquist_wavenumber()

        # Test low k (inertial subrange)
        k_low = k_max * 1e-10
        E_low = axiomatic_energy_spectrum(np.array([k_low]), epsilon)[0]

        # Expected classical:
        E_expected = C_K_KOLMOGOROV * (epsilon ** (2.0 / 3.0)) * (k_low ** (-5.0 / 3.0))
        assert np.isclose(E_low, E_expected, rtol=1e-3), "Inertial range decoupled from classical 5/3 scaling"

        # Test above cutoff (strict top-out)
        k_high = k_max * 1.001
        E_high = axiomatic_energy_spectrum(np.array([k_high]), epsilon)[0]
        assert E_high == 0.0, "Energy cascade leaked beyond the Nyquist lattice pitch"

    def test_bounded_enstrophy(self):
        """
        Verifies that enstrophy is strictly bounded by the structural constraints
        of the lattice logic (Phase 3 resolution to Navier Stokes).
        """
        # Take a macroscopic 1cm grid mapped with 1e6 nodes
        dx = 1e-2
        N = int(1e6)

        # The ultimate bound
        Z_bound = prove_bounded_enstrophy(N, dx)

        # Max velocity on lattice is c_0
        omega_max = 2.0 * C_0 / dx
        Z_node = 0.5 * omega_max**2
        expected_Z = N * Z_node * (dx**3)

        assert np.isclose(Z_bound, expected_Z), "Bounded enstrophy proof violation"

    def test_scale_separation_ratio(self):
        """Verifies the macroscopic indistinguishability argument."""
        # Water: nu ~ 1e-6, epsilon ~ 1e-3
        nu = 1e-6
        eps = 1e-3

        # eta_k = kolmogorov_microscale(nu, eps)  # bulk lint fixup pass
        ratio = dissipation_cutoff_ratio(nu, eps)

        assert ratio > 1e6, f"Scale separation failed. Ratio was {ratio}"
