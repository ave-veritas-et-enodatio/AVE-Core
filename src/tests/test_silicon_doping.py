"""
Test Silicon Doping & p-n Junction — AVE First Principles
=========================================================

Validates dopant impurity levels and p-n junction properties.
Phase 5 verification.
"""

import numpy as np
from ave.condensed.silicon_doping import (
    Z_BORON,
    Z_PHOSPHORUS,
    R_VAL_BORON,
    R_VAL_PHOSPHORUS,
    boron_impurity_level,
    phosphorus_impurity_level,
    pn_junction,
    diode_iv,
)


# ═══════════════════════════════════════════════════════════════════
# Dopant Properties
# ═══════════════════════════════════════════════════════════════════


class TestDopantConstants:
    def test_boron_Z(self):
        assert Z_BORON == 5

    def test_phosphorus_Z(self):
        assert Z_PHOSPHORUS == 15

    def test_port_impedances_positive(self):
        assert R_VAL_BORON > 0
        assert R_VAL_PHOSPHORUS > 0


# ═══════════════════════════════════════════════════════════════════
# Impurity Levels
# ═══════════════════════════════════════════════════════════════════


class TestBoronImpurity:
    def test_acceptor_type(self):
        result = boron_impurity_level()
        assert result["type"] == "acceptor (hole)"

    def test_above_valence_band(self):
        result = boron_impurity_level()
        assert result["position"] == "above valence band"

    def test_delta_E_positive(self):
        result = boron_impurity_level()
        assert result["delta_E_eV"] >= 0

    def test_delta_E_less_than_gap(self):
        """Impurity level must be within the gap, not above it."""
        result = boron_impurity_level()
        assert result["delta_E_eV"] < result["E_gap_Si_eV"]


class TestPhosphorusImpurity:
    def test_donor_type(self):
        result = phosphorus_impurity_level()
        assert result["type"] == "donor (electron)"

    def test_below_conduction_band(self):
        result = phosphorus_impurity_level()
        assert result["position"] == "below conduction band"

    def test_delta_E_positive(self):
        result = phosphorus_impurity_level()
        assert result["delta_E_eV"] >= 0

    def test_delta_E_less_than_gap(self):
        result = phosphorus_impurity_level()
        assert result["delta_E_eV"] < result["E_gap_Si_eV"]


# ═══════════════════════════════════════════════════════════════════
# p-n Junction
# ═══════════════════════════════════════════════════════════════════


class TestPNJunction:
    def test_built_in_potential_positive(self):
        """Built-in potential must be positive (P-side higher)."""
        junction = pn_junction()
        assert junction["V_bi_eV"] > 0

    def test_built_in_potential_less_than_gap(self):
        """V_bi must be less than the band gap."""
        junction = pn_junction()
        assert junction["V_bi_eV"] < junction["E_gap_eV"]

    def test_transmission_coefficient_range(self):
        """T² must be between 0 and 1."""
        junction = pn_junction()
        assert 0 < junction["T_sq_junction"] <= 1.0


# ═══════════════════════════════════════════════════════════════════
# Diode I-V Characteristic
# ═══════════════════════════════════════════════════════════════════


class TestDiodeIV:
    def test_zero_current_at_zero_voltage(self):
        I = diode_iv(np.array([0.0]))
        np.testing.assert_allclose(I, 0.0, atol=1e-10)

    def test_forward_current_positive(self):
        I = diode_iv(np.array([0.5]))
        assert I[0] > 0

    def test_reverse_current_small(self):
        """Reverse current should be much smaller than forward."""
        I_fwd = diode_iv(np.array([0.3]))
        I_rev = diode_iv(np.array([-0.3]))
        assert abs(I_rev[0]) < abs(I_fwd[0])

    def test_diode_shape(self):
        """Forward current >> reverse current (rectification)."""
        V = np.linspace(-0.5, 0.5, 100)
        I = diode_iv(V)
        max_forward = np.max(I)
        min_reverse = np.min(I)
        # Forward current should dominate
        assert max_forward > abs(min_reverse) * 10
