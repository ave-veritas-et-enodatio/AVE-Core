"""
Tests for derived electroweak constants and gauge couplings.

Verifies that the AVE-derived values match PDG measurements
within the documented error bounds.
"""

import numpy as np
from ave.core.constants import (
    ALPHA,
    ALPHA_S,
    SIN2_THETA_W,
    NU_VAC,
    M_W_MEV,
    M_Z_MEV,
    HIGGS_VEV_MEV,
    M_HIGGS_MEV,
    LAMBDA_HIGGS,
    N_K4,
    G_F,
)


# ════════════════════════════════════════════════════════════════════
# Gauge Couplings
# ════════════════════════════════════════════════════════════════════


class TestGaugeCouplings:

    def test_alpha_exact(self):
        """α = 1/137.036 — exact by calibration."""
        assert abs(ALPHA - 1 / 137.036) < 1e-6

    def test_sin2_theta_w(self):
        """sin²θ_W = 2/9 ≈ 0.2222 (PDG: 0.2230, Δ=0.35%)."""
        assert SIN2_THETA_W == 2 / 9
        pdg = 0.2230
        err = abs(SIN2_THETA_W - pdg) / pdg
        assert err < 0.005  # < 0.5%

    def test_alpha_s_from_compliance(self):
        """α_s = α^(3/7) ≈ 0.1214 (PDG: 0.1179, Δ=2.97%)."""
        assert abs(ALPHA_S - ALPHA ** (3 / 7)) < 1e-12  # exact formula
        pdg = 0.1179
        err = abs(ALPHA_S - pdg) / pdg
        assert err < 0.04  # < 4%

    def test_alpha_s_exponent_is_spatial_fraction(self):
        """The 3/7 exponent = d/n: 3 spatial dim / 7 compliance modes."""
        n_modes = 7  # from ν_vac = 2/7
        d_spatial = 3
        assert abs(ALPHA_S - ALPHA ** (d_spatial / n_modes)) < 1e-12


# ════════════════════════════════════════════════════════════════════
# Electroweak Boson Masses
# ════════════════════════════════════════════════════════════════════


class TestBosonMasses:

    def test_w_boson_mass(self):
        """M_W ≈ 79,923 MeV (PDG: 80,379, Δ=0.57%)."""
        pdg = 80379  # MeV
        err = abs(M_W_MEV - pdg) / pdg
        assert err < 0.01  # < 1%

    def test_z_boson_mass(self):
        """M_Z ≈ 90,624 MeV (PDG: 91,188, Δ=0.62%)."""
        pdg = 91188  # MeV
        err = abs(M_Z_MEV - pdg) / pdg
        assert err < 0.01  # < 1%

    def test_z_from_w_and_mixing(self):
        """M_Z = M_W × 3/√7 (from sin²θ_W = 2/9)."""
        ratio = M_Z_MEV / M_W_MEV
        expected = 3.0 / np.sqrt(7.0)
        assert abs(ratio - expected) < 1e-10

    def test_higgs_vev(self):
        """v ≈ 248,833 MeV (PDG: 246,220, Δ=1.1%)."""
        pdg = 246220  # MeV
        err = abs(HIGGS_VEV_MEV - pdg) / pdg
        assert err < 0.02  # < 2%

    def test_fermi_constant_positive(self):
        """G_F > 0 and in correct order of magnitude."""
        assert G_F > 0
        # PDG: 1.1664e-5 GeV⁻²
        pdg = 1.1664e-5
        err = abs(G_F - pdg) / pdg
        assert err < 0.03  # < 3%


# ════════════════════════════════════════════════════════════════════
# Higgs Mass from K4 Breathing Mode
# ════════════════════════════════════════════════════════════════════


class TestHiggsMass:

    def test_n_k4_is_4(self):
        """K4 unit cell has 4 nodes."""
        assert N_K4 == 4

    def test_lambda_is_one_eighth(self):
        """λ_H = 1/(2N_K4) = 1/8."""
        assert LAMBDA_HIGGS == 1 / 8

    def test_higgs_mass_is_v_over_2(self):
        """m_H = v/√N_K4 = v/2."""
        expected = HIGGS_VEV_MEV / np.sqrt(N_K4)
        assert abs(M_HIGGS_MEV - expected) < 1e-6

    def test_higgs_mass_accuracy(self):
        """m_H ≈ 124,417 MeV (PDG: 125,100, Δ=0.55%)."""
        pdg = 125100  # MeV
        err = abs(M_HIGGS_MEV - pdg) / pdg
        assert err < 0.01  # < 1%

    def test_higgs_mass_from_sm_relation(self):
        """m_H = √(2λ)v reproduces m_H = v/2."""
        m_h_sm = np.sqrt(2 * LAMBDA_HIGGS) * HIGGS_VEV_MEV
        assert abs(m_h_sm - M_HIGGS_MEV) < 1e-6
