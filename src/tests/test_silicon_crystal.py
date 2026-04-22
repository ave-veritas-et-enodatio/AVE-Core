"""
Test Silicon Crystal — AVE First Principles
=============================================

Validates silicon crystal bond parameters, diamond cubic structure,
and band gap from coordination-loaded coupled resonator model.

Phases 3-4 verification.
"""

import numpy as np

from ave.condensed.silicon_crystal import (
    A_LATTICE,
    A_LATTICE_EXP,
    B_SI_SI_EV,
    COORD_NUMBER,
    D_SI_SI,
    D_SI_SI_EXP,
    E_GAP_EXP,
    K_CRYSTAL,
    K_SI_SI,
    N_ATOMS_CELL,
    build_unit_cell_bonds,
    dispersion_periodic_lc,
    silicon_band_gap,
)

# ═══════════════════════════════════════════════════════════════════
# Si-Si Bond
# ═══════════════════════════════════════════════════════════════════


class TestSiSiBond:
    def test_bond_distance_within_15_pct(self):
        """Si-Si bond distance within 15% of experimental 2.352 Å."""
        err = abs(D_SI_SI - D_SI_SI_EXP) / D_SI_SI_EXP
        assert err < 0.15, f"Si-Si distance error {err:.1%} > 15%"

    def test_bond_energy_within_15_pct(self):
        """Bond energy within 15% of experimental ~3.39 eV."""
        err = abs(B_SI_SI_EV - 3.39) / 3.39
        assert err < 0.15, f"Bond energy error {err:.1%} > 15%"

    def test_coupling_positive(self):
        assert K_SI_SI > 0

    def test_coupling_less_than_1(self):
        assert K_SI_SI < 1.0

    def test_crystal_coupling_is_k_over_4(self):
        """k_crystal = k_molecular / N_coord."""
        np.testing.assert_allclose(K_CRYSTAL, K_SI_SI / 4.0)


# ═══════════════════════════════════════════════════════════════════
# Diamond Cubic Unit Cell
# ═══════════════════════════════════════════════════════════════════


class TestDiamondCubicUnitCell:
    def test_8_atoms(self):
        assert N_ATOMS_CELL == 8

    def test_coordination_4(self):
        assert COORD_NUMBER == 4

    def test_16_bonds(self):
        bonds = build_unit_cell_bonds()
        assert len(bonds) == 16

    def test_each_atom_has_4_bonds(self):
        """Every atom bonds to exactly 4 nearest neighbors."""
        bonds = build_unit_cell_bonds()
        bond_count = np.zeros(N_ATOMS_CELL)
        for i, j, _ in bonds:
            bond_count[i] += 1
            bond_count[j] += 1
        np.testing.assert_array_equal(bond_count, 4)

    def test_lattice_constant_within_15_pct(self):
        err = abs(A_LATTICE - A_LATTICE_EXP) / A_LATTICE_EXP
        assert err < 0.15, f"Lattice constant error {err:.1%} > 15%"


# ═══════════════════════════════════════════════════════════════════
# Band Gap — MEANS TEST
# ═══════════════════════════════════════════════════════════════════


class TestSiliconBandGap:
    def test_band_gap_positive(self):
        """Band gap must be positive (semiconductor, not metal)."""
        result = silicon_band_gap()
        assert result["E_gap_eV"] > 0

    def test_band_gap_within_50_pct(self):
        """PRIMARY MEANS TEST: band gap within 50% of 1.12 eV."""
        result = silicon_band_gap()
        err = abs(result["E_gap_eV"] - E_GAP_EXP) / E_GAP_EXP
        assert err < 0.50, f"Band gap error {err:.1%} > 50%"

    def test_band_gap_within_10_pct(self):
        """STRETCH TARGET: band gap within 10% of 1.12 eV."""
        result = silicon_band_gap()
        err = abs(result["E_gap_eV"] - E_GAP_EXP) / E_GAP_EXP
        assert err < 0.10, f"Band gap error {err:.1%} > 10%"

    def test_bonding_below_antibonding(self):
        result = silicon_band_gap()
        assert result["E_bonding_eV"] < result["E_antibonding_eV"]

    def test_coordination_number(self):
        result = silicon_band_gap()
        assert result["N_coord"] == 4


# ═══════════════════════════════════════════════════════════════════
# Dispersion Relation
# ═══════════════════════════════════════════════════════════════════


class TestDispersion:
    def test_two_branches(self):
        q = np.linspace(0, 1, 50)
        E_bond, E_anti = dispersion_periodic_lc(q)
        assert len(E_bond) == 50
        assert len(E_anti) == 50

    def test_bonding_below_antibonding_everywhere(self):
        q = np.linspace(0, 1, 50)
        E_bond, E_anti = dispersion_periodic_lc(q)
        assert np.all(E_bond <= E_anti + 1e-10)

    def test_all_energies_positive(self):
        q = np.linspace(0, 1, 50)
        E_bond, E_anti = dispersion_periodic_lc(q)
        assert np.all(E_bond > 0)
        assert np.all(E_anti > 0)
