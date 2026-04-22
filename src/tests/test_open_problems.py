"""
Tests for ave.axioms.open_problems

Verifies Strong CP, baryon asymmetry, and Hubble tension arguments.
"""

import pytest
import numpy as np
from ave.axioms.open_problems import (
    torus_knot_phase_winding,
    vacuum_angle_quantization,
    lattice_chirality,
    impedance_hubble_correction,
    full_open_problems_proof,
)


# ════════════════════════════════════════════════════════════════════
# Strong CP Problem
# ════════════════════════════════════════════════════════════════════


class TestStrongCP:

    def test_phase_winding_quantized(self):
        """Phase winding = qπ for (2,q) torus knot."""
        assert abs(torus_knot_phase_winding(3) - 3 * np.pi) < 1e-10
        assert abs(torus_knot_phase_winding(5) - 5 * np.pi) < 1e-10

    def test_rejects_even_q(self):
        """Even q is not a valid torus knot."""
        with pytest.raises(ValueError):
            torus_knot_phase_winding(4)

    def test_theta_is_zero(self):
        """Ground state vacuum angle θ = 0."""
        result = vacuum_angle_quantization()
        assert result["theta_ground_state"] == 0.0
        assert result["theta_is_zero"]

    def test_no_axion_needed(self):
        """AVE doesn't need an axion to solve Strong CP."""
        result = vacuum_angle_quantization()
        assert result["no_axion_needed"]

    def test_strong_cp_solved(self):
        """Strong CP problem is resolved."""
        result = vacuum_angle_quantization()
        assert result["STRONG_CP_SOLVED"]


# ════════════════════════════════════════════════════════════════════
# Baryon Asymmetry
# ════════════════════════════════════════════════════════════════════


class TestBaryonAsymmetry:

    def test_lattice_is_chiral(self):
        """SRS/K4 lattice is chiral."""
        result = lattice_chirality()
        assert result["lattice_is_chiral"]

    def test_cp_violated(self):
        """CP is violated by lattice chirality + torus knot chirality."""
        result = lattice_chirality()
        assert result["CP_violated"]

    def test_sakharov_conditions(self):
        """Sakharov conditions are met."""
        result = lattice_chirality()
        assert result["sakharov_conditions_met"]

    def test_eta_order_of_magnitude(self):
        """Predicted η is within 3 orders of magnitude of observed."""
        result = lattice_chirality()
        assert result["order_of_magnitude_match"]

    def test_eta_positive(self):
        """Predicted baryon-to-photon ratio is positive."""
        result = lattice_chirality()
        assert result["eta_predicted"] > 0


# ════════════════════════════════════════════════════════════════════
# Hubble Tension
# ════════════════════════════════════════════════════════════════════


class TestHubbleTension:

    def test_impedance_correction_positive(self):
        """Impedance-corrected H₀ > Planck H₀ (correction is positive)."""
        result = impedance_hubble_correction()
        assert result["H0_impedance_corrected"] >= result["H0_Planck"]

    def test_local_Z_higher_than_cmb(self):
        """Local impedance > CMB path impedance (higher n_e)."""
        result = impedance_hubble_correction()
        assert result["Z_local"] > result["Z_cmb"]

    def test_mechanism_is_physical(self):
        """There is a physical mechanism string."""
        result = impedance_hubble_correction()
        assert "impedance" in result["mechanism"].lower()


# ════════════════════════════════════════════════════════════════════
# Full Proof
# ════════════════════════════════════════════════════════════════════


class TestFullProof:

    def test_all_four_addressed(self):
        """All four areas are addressed."""
        proof = full_open_problems_proof()
        assert "Strong_CP" in proof
        assert "Baryon_Asymmetry" in proof
        assert "g_star_Prediction" in proof
        assert "Hubble_Tension" in proof

    def test_strong_cp_solved(self):
        """Strong CP is solved."""
        proof = full_open_problems_proof()
        assert proof["Strong_CP"]["SOLVED"]


# ════════════════════════════════════════════════════════════════════
# g* Testable Prediction
# ════════════════════════════════════════════════════════════════════


class TestGStarPrediction:

    def test_g_star_ave(self):
        """g*_AVE = 7³/4 = 85.75."""
        from ave.axioms.open_problems import g_star_prediction

        pred = g_star_prediction()
        assert pred["g_star_AVE"] == 85.75

    def test_delta_g_star(self):
        """21 fewer DOF than SM."""
        from ave.axioms.open_problems import g_star_prediction

        pred = g_star_prediction()
        assert pred["delta_g_star"] == 21.0

    def test_missing_weyl(self):
        """12 missing Weyl spinors."""
        from ave.axioms.open_problems import g_star_prediction

        pred = g_star_prediction()
        assert pred["missing_weyl_spinors"] == 12.0

    def test_gw_stronger(self):
        """Primordial GW background is stronger."""
        from ave.axioms.open_problems import g_star_prediction

        pred = g_star_prediction()
        assert pred["primordial_GW_stronger_pct"] > 0
