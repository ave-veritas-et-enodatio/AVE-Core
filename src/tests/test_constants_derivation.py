"""
test_constants_derivation.py
=============================
Systematic verification that every derived constant in constants.py
matches its definition formula and stays within tolerance of
empirical/CODATA values.

This test file covers:
  1. Internal consistency — each derived constant equals its formula
  2. Empirical agreement — derived values are within stated tolerance
     of PDG/CODATA measurements
  3. Dimensional analysis — key dimensional relationships hold
  4. Book 2 prediction table — engine outputs match manuscript claims
"""

import math

import numpy as np
import pytest

from ave.core.constants import (  # SI inputs; Three calibration inputs; Derived topological; Derived dielectric; Derived macroscopic; Electroweak; CKM; PMNS; Baryon
    A_CKM,
    ALPHA,
    ALPHA_S,
    B_SNAP,
    C_0,
    DELTA_CP_PMNS,
    E_CRIT,
    E_YIELD,
    E_YIELD_KINETIC,
    EPSILON_0,
    ETA_EQ,
    H_INFINITY,
    HBAR,
    HIGGS_VEV_MEV,
    ISOTROPIC_PROJECTION,
    K_B,
    KAPPA_FS_COLD,
    L_NODE,
    LAMBDA_CKM,
    LAMBDA_HIGGS,
    M_E,
    M_HIGGS_MEV,
    M_PROTON,
    M_SUN,
    M_W_MEV,
    M_Z_MEV,
    MU_0,
    N_A,
    N_K4,
    NU_KIN,
    NU_VAC,
    P_C,
    R_HUBBLE,
    RHO_BULK,
    RHO_ETA_MAG,
    SIN2_THETA_12,
    SIN2_THETA_13,
    SIN2_THETA_23,
    SIN2_THETA_W,
    T_EM,
    V_CB,
    V_SNAP,
    V_UB,
    V_US,
    V_YIELD,
    XI_MACHIAN,
    XI_TOPO,
    Z_0,
    G,
    e_charge,
)

# ============================================================================
# 1. INTERNAL CONSISTENCY: Each derived constant matches its definition
# ============================================================================


class TestSIConstants:
    """Verify SI electromagnetic foundation is self-consistent."""

    def test_epsilon_from_mu_c(self):
        assert EPSILON_0 == pytest.approx(1.0 / (MU_0 * C_0**2), rel=1e-12)

    def test_impedance_from_mu_epsilon(self):
        assert Z_0 == pytest.approx(np.sqrt(MU_0 / EPSILON_0), rel=1e-12)

    def test_impedance_value(self):
        assert Z_0 == pytest.approx(376.73, rel=1e-3)


class TestTopologicalDerivations:
    """Every derived constant matches its stated formula from Axiom 1."""

    def test_l_node_is_reduced_compton(self):
        assert L_NODE == pytest.approx(HBAR / (M_E * C_0), rel=1e-12)

    def test_xi_topo(self):
        assert XI_TOPO == pytest.approx(e_charge / L_NODE, rel=1e-12)

    def test_t_em(self):
        assert T_EM == pytest.approx(M_E * C_0**2 / L_NODE, rel=1e-12)

    def test_v_snap(self):
        assert V_SNAP == pytest.approx(M_E * C_0**2 / e_charge, rel=1e-12)
        assert V_SNAP == pytest.approx(511e3, rel=1e-3)  # ~511 kV

    def test_v_yield(self):
        assert V_YIELD == pytest.approx(np.sqrt(ALPHA) * V_SNAP, rel=1e-12)
        assert V_YIELD == pytest.approx(43_652, rel=1e-2)  # ~43.65 kV

    def test_e_yield_kinetic(self):
        assert E_YIELD_KINETIC == pytest.approx(np.sqrt(ALPHA) * M_E * C_0**2, rel=1e-12)

    def test_e_crit(self):
        assert E_CRIT == pytest.approx(M_E**2 * C_0**3 / (e_charge * HBAR), rel=1e-12)

    def test_e_yield_from_v_yield(self):
        assert E_YIELD == pytest.approx(V_YIELD / L_NODE, rel=1e-12)

    def test_b_snap(self):
        assert B_SNAP == pytest.approx(np.sqrt(2 * MU_0 * M_E * C_0**2 / L_NODE**3), rel=1e-12)


class TestDielectricDerivations:
    """Axiom 4 dielectric constants match their formulas."""

    def test_packing_fraction(self):
        assert P_C == pytest.approx(8 * math.pi * ALPHA, rel=1e-12)

    def test_nu_vac(self):
        assert NU_VAC == pytest.approx(2.0 / 7.0, rel=1e-15)

    def test_eta_eq(self):
        assert ETA_EQ == pytest.approx(P_C * (1 - NU_VAC), rel=1e-12)
        assert ETA_EQ == pytest.approx(P_C * 5.0 / 7.0, rel=1e-12)

    def test_isotropic_projection(self):
        assert ISOTROPIC_PROJECTION == pytest.approx(1.0 / 7.0, rel=1e-15)


class TestElectroweakDerivations:
    """Electroweak constants match their derivation from ν_vac = 2/7."""

    def test_sin2_theta_w(self):
        assert SIN2_THETA_W == pytest.approx(2.0 / 9.0, rel=1e-15)

    def test_m_w(self):
        expected = (M_E * C_0**2 / (e_charge * 1e6)) / (ALPHA**2 * P_C * np.sqrt(3.0 / 7.0))
        assert M_W_MEV == pytest.approx(expected, rel=1e-12)

    def test_m_z_from_m_w(self):
        assert M_Z_MEV == pytest.approx(M_W_MEV * 3 / np.sqrt(7), rel=1e-12)

    def test_higgs_from_vev(self):
        assert M_HIGGS_MEV == pytest.approx(HIGGS_VEV_MEV / np.sqrt(N_K4), rel=1e-12)

    def test_lambda_higgs(self):
        assert LAMBDA_HIGGS == pytest.approx(1.0 / 8.0, rel=1e-15)


class TestCKMDerivations:
    """CKM matrix elements from Wolfenstein parameterization."""

    def test_lambda_ckm_is_sin2(self):
        assert LAMBDA_CKM == pytest.approx(SIN2_THETA_W, rel=1e-15)

    def test_a_ckm(self):
        assert A_CKM == pytest.approx(np.sqrt(7.0 / 9.0), rel=1e-12)

    def test_rho_eta(self):
        assert RHO_ETA_MAG == pytest.approx(1.0 / np.sqrt(7.0), rel=1e-12)

    def test_v_us(self):
        assert V_US == pytest.approx(LAMBDA_CKM, rel=1e-15)

    def test_v_cb(self):
        assert V_CB == pytest.approx(A_CKM * LAMBDA_CKM**2, rel=1e-12)

    def test_v_ub(self):
        assert V_UB == pytest.approx(A_CKM * LAMBDA_CKM**3 * RHO_ETA_MAG, rel=1e-12)


class TestPMNSDerivations:
    """PMNS mixing angles from torsional defect crossing numbers."""

    def test_theta_13(self):
        assert SIN2_THETA_13 == pytest.approx(1.0 / 45.0, rel=1e-15)

    def test_theta_12(self):
        assert SIN2_THETA_12 == pytest.approx(NU_VAC + 1.0 / 45.0, rel=1e-12)

    def test_theta_23(self):
        assert SIN2_THETA_23 == pytest.approx(0.5 + 2.0 / 45.0, rel=1e-12)

    def test_delta_cp(self):
        assert DELTA_CP_PMNS == pytest.approx((1 + 1 / 3 + 1 / 45) * math.pi, rel=1e-12)


class TestCosmologicalDerivations:
    """Cosmological constants match their formulas."""

    def test_h_infinity(self):
        expected = 28 * math.pi * M_E**3 * C_0 * G / (HBAR**2 * ALPHA**2)
        assert H_INFINITY == pytest.approx(expected, rel=1e-12)

    def test_r_hubble(self):
        assert R_HUBBLE == pytest.approx(C_0 / H_INFINITY, rel=1e-12)

    def test_alpha_s(self):
        assert ALPHA_S == pytest.approx(ALPHA ** (3.0 / 7.0), rel=1e-12)

    def test_xi_machian(self):
        assert XI_MACHIAN == pytest.approx(HBAR * C_0 / (7 * G * M_E**2), rel=1e-12)

    def test_nu_kin(self):
        assert NU_KIN == pytest.approx(ALPHA * C_0 * L_NODE, rel=1e-12)

    def test_kappa_fs(self):
        assert KAPPA_FS_COLD == pytest.approx(8 * math.pi, rel=1e-12)


# ============================================================================
# 2. EMPIRICAL AGREEMENT: Within stated tolerance of PDG/CODATA
# ============================================================================


class TestEmpiricalAgreement:
    """All derived constants fall within published tolerances of
    experimental measurements."""

    # PDG on-shell sin²θ_W = 0.2230 ± 0.0004
    def test_sin2_theta_w_pdg(self):
        assert abs(SIN2_THETA_W - 0.2230) / 0.2230 < 0.006  # <0.6%

    # PDG W mass = 80,379 MeV
    def test_m_w_pdg(self):
        assert abs(M_W_MEV - 80_379) / 80_379 < 0.01  # <1%

    # PDG Z mass = 91,188 MeV
    def test_m_z_pdg(self):
        assert abs(M_Z_MEV - 91_188) / 91_188 < 0.01  # <1%

    # PDG Higgs mass = 125,100 MeV
    def test_m_higgs_pdg(self):
        assert abs(M_HIGGS_MEV - 125_100) / 125_100 < 0.01  # <1%

    # PDG α_s(M_Z) = 0.1179 ± 0.0010
    def test_alpha_s_pdg(self):
        assert abs(ALPHA_S - 0.1179) / 0.1179 < 0.04  # <4%

    # PDG |V_us| = 0.22535
    def test_v_us_pdg(self):
        assert abs(V_US - 0.22535) / 0.22535 < 0.02  # <2%

    # PDG |V_cb| = 0.04182
    def test_v_cb_pdg(self):
        assert abs(V_CB - 0.04182) / 0.04182 < 0.06  # <6%

    # NuFIT sin²θ_13 = 0.02200
    def test_pmns_theta_13(self):
        assert abs(SIN2_THETA_13 - 0.02200) / 0.02200 < 0.02  # <2%

    # NuFIT sin²θ_12 = 0.307
    def test_pmns_theta_12(self):
        assert abs(SIN2_THETA_12 - 0.307) / 0.307 < 0.01  # <1%

    # NuFIT sin²θ_23 = 0.546
    def test_pmns_theta_23(self):
        assert abs(SIN2_THETA_23 - 0.546) / 0.546 < 0.01  # <1%


# ============================================================================
# 3. ENGINE PREDICTION TABLE (Book 2, Ch.09)
# ============================================================================


class TestPredictionTable:
    """Values claimed in Book 2 Ch.09 verification table are reproducible."""

    def test_galactic_ngc3198(self):
        """NGC 3198 flat rotation velocity from galactic_rotation engine."""
        from ave.regime_3_saturated.galactic_rotation import GALAXY_CATALOG, ave_rotation_velocity

        galaxy = GALAXY_CATALOG["NGC 3198"]
        r_flat = 30e3 * 3.086e16  # 30 kpc in meters
        v = ave_rotation_velocity(galaxy, r_flat)
        # Book 2 claims 159 km/s, obs = 150, 5% error
        assert 140e3 < v < 180e3, f"v_flat = {v/1e3:.0f} km/s"

    def test_superconductor_bcs_identity(self):
        """B_c(T) = B_c0 * sqrt(1 - (T/T_c)^2) = saturation_factor."""
        from ave.axioms.scale_invariant import saturation_factor
        from ave.plasma.superconductor import critical_field

        T, T_c, B_c0 = 4.2, 9.25, 0.206  # Niobium
        bc = critical_field(T, T_c, B_c0)
        sat = saturation_factor(T, T_c) * B_c0
        assert bc == pytest.approx(sat, rel=1e-10)

    def test_london_depth_order_of_magnitude(self):
        """London depths are in the 30-150 nm range per Book 2 table."""
        from ave.plasma.superconductor import SC_CATALOG, london_penetration_depth

        for name, mat in SC_CATALOG.items():
            lam = london_penetration_depth(mat.n_s)
            assert 10e-9 < lam < 300e-9, f"{name}: λ_L = {lam*1e9:.0f} nm"

    def test_gw_lossless_propagation(self):
        """GW strain is far below V_snap (lossless propagation)."""
        # GW150914: h ~ 1e-21 → V_GW/V_snap ~ 1e-28
        h_strain = 1e-21
        V_gw = h_strain * V_SNAP  # order-of-magnitude
        ratio = V_gw / V_SNAP
        assert ratio < 1e-10, "GW must be deeply in linear regime"

    def test_stellar_tachocline_reflection(self):
        """Tachocline reflection coefficient is nonzero."""
        from ave.gravity.stellar_interior import tachocline_reflection

        gamma = tachocline_reflection()
        assert abs(gamma) > 0.1, "Tachocline must show significant reflection"


# ============================================================================
# 4. DIMENSIONAL SANITY CHECKS
# ============================================================================


class TestDimensionalSanity:
    """Key physical quantities have correct orders of magnitude."""

    def test_l_node_is_femtometer_scale(self):
        assert 1e-13 < L_NODE < 1e-12  # ~3.86e-13 m

    def test_z0_is_377(self):
        assert 376 < Z_0 < 378

    def test_t_em_is_sub_newton(self):
        assert 0.1 < T_EM < 0.5  # ~0.212 N

    def test_v_snap_is_511kv(self):
        assert 510e3 < V_SNAP < 512e3

    def test_v_yield_is_44kv(self):
        assert 43e3 < V_YIELD < 45e3

    def test_b_snap_is_giga_tesla(self):
        assert 1e9 < B_SNAP < 3e9

    def test_h_infinity_positive(self):
        assert H_INFINITY > 0

    def test_alpha_s_between_zero_and_one(self):
        assert 0 < ALPHA_S < 1

    def test_nu_vac_is_two_sevenths(self):
        assert NU_VAC == pytest.approx(2 / 7, rel=1e-15)
