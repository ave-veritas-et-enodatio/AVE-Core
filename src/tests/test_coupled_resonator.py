"""
Test Coupled Resonator Solver
==============================

Tests for the universal coupled resonator framework: nuclear binding,
atomic ionization energies, and molecular bond energies — all from
a single impedance coupling formalism.
"""

import numpy as np

from ave.solvers.coupled_resonator import (
    K_COUPLING,
    atom_port_impedance,
    complete_graph_eigenvalues,
    coupled_resonator_binding,
    hierarchical_binding,
    ionization_energy,
    molecular_bond_distance,
    molecular_bond_energy,
    nuclear_mass,
)

# ═══════════════════════════════════════════════════════════════════════
# Graph Theory
# ═══════════════════════════════════════════════════════════════════════

class TestCompleteGraphEigenvalues:
    def test_K2_eigenvalues(self) -> None:
        lam = complete_graph_eigenvalues(2)
        np.testing.assert_allclose(sorted(lam), [-1, 1])

    def test_K4_eigenvalues(self) -> None:
        lam = complete_graph_eigenvalues(4)
        np.testing.assert_allclose(sorted(lam), [-1, -1, -1, 3])

    def test_sum_is_zero(self) -> None:
        """Trace of adjacency matrix = 0."""
        for n in [2, 3, 5, 10]:
            assert abs(sum(complete_graph_eigenvalues(n))) < 1e-10

# ═══════════════════════════════════════════════════════════════════════
# Nuclear Binding
# ═══════════════════════════════════════════════════════════════════════

class TestNuclearBinding:
    def test_deuteron_binding_positive(self) -> None:
        B, _ = coupled_resonator_binding(2, K_COUPLING)
        assert B > 0, "Deuteron must be bound"

    def test_alpha_binding_greater_than_deuteron(self) -> None:
        B_d, _ = coupled_resonator_binding(2, K_COUPLING)
        B_a, _ = coupled_resonator_binding(4, K_COUPLING)
        assert B_a > B_d

    def test_nuclear_mass_helium_4(self) -> None:
        mass, binding = nuclear_mass(2, 4)
        assert binding > 0
        assert mass > 0

    def test_hierarchical_binding_positive(self) -> None:
        B, B_alpha, B_inter = hierarchical_binding(3)
        assert B > 0
        assert B_alpha > 0
        assert B_inter >= 0

# ═══════════════════════════════════════════════════════════════════════
# Atomic Ionization
# ═══════════════════════════════════════════════════════════════════════

class TestIonizationEnergy:
    def test_hydrogen_ie(self) -> None:
        IE = ionization_energy(1)
        assert 13.0 < IE < 14.0, f"H IE = {IE}, expected ~13.6 eV"

    def test_helium_ie_higher_than_hydrogen(self) -> None:
        IE_H = ionization_energy(1)
        IE_He = ionization_energy(2)
        assert IE_He > IE_H

    def test_lithium_ie_lower_than_helium(self) -> None:
        IE_He = ionization_energy(2)
        IE_Li = ionization_energy(3)
        assert IE_Li < IE_He, "Li IE < He IE (new shell)"

# ═══════════════════════════════════════════════════════════════════════
# Molecular Bonds
# ═══════════════════════════════════════════════════════════════════════

class TestMolecularBonds:
    def test_bond_distance_positive(self) -> None:
        r_A = 1e-10
        r_B = 1e-10
        d = molecular_bond_distance(r_A, r_B)
        assert d > 0

    def test_bond_energy_positive(self) -> None:
        r_A = 1e-10
        r_B = 1e-10
        d = molecular_bond_distance(r_A, r_B)
        B, k = molecular_bond_energy(13.6, 13.6, r_A, r_B, d)
        assert B > 0
        assert 0 < k <= 1

    def test_atom_port_impedance_positive(self) -> None:
        r = atom_port_impedance(6, 11.26)  # Carbon
        assert r > 0

    def test_universal_bond_loading_single_double_triple(self) -> None:
        # Retrieve port impedances for C and O using known MCL IEs
        IE_C = ionization_energy(6)
        IE_O = ionization_energy(8)
        r_C = atom_port_impedance(6, IE_C)
        r_O = atom_port_impedance(8, IE_O)

        # Test C-C (Order 1): NIST 1.540 A. N_eff = 3
        d_cc = molecular_bond_distance(r_C, r_C, Z_A=6, Z_B=6, bond_order=1)
        # 1.503 A (-2.4%)
        assert 1.45 < d_cc * 1e10 < 1.55

        # Test C=C (Order 2): NIST 1.340 A. N_eff = 5
        d_c_c = molecular_bond_distance(r_C, r_C, Z_A=6, Z_B=6, bond_order=2)
        # 1.294 A (-3.5%)
        assert 1.25 < d_c_c * 1e10 < 1.35

        # Test C#C (Order 3): NIST 1.200 A. N_eff = 7
        d_c_t_c = molecular_bond_distance(r_C, r_C, Z_A=6, Z_B=6, bond_order=3)
        # 1.148 A (-4.3%)
        assert 1.10 < d_c_t_c * 1e10 < 1.21

        # Test C=O (Order 2 heteronuclear): NIST 1.230 A. N_eff = 5
        d_c_o = molecular_bond_distance(r_C, r_O, Z_A=6, Z_B=8, bond_order=2)
        # 1.237 A (+0.6%)
        assert 1.20 < d_c_o * 1e10 < 1.28

        # Verify ordering
        assert d_cc > d_c_c > d_c_t_c
