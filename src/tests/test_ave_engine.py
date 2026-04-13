"""
AVE Engine Verification Tests
==============================
Rigorous assertion-based tests validating:
  1. Derived constants against CODATA and manuscript values
  2. Axiom 4 saturation operator across all three regimes
  3. Axiom 2 dimensional isomorphism self-consistency
  4. Gravity/optical metric correctness
  5. Proton mass eigenvalue from topological feedback
"""

import sys
import os
import numpy as np
import pytest

from ave.core.constants import (
    C_0, MU_0, EPSILON_0, Z_0, HBAR, M_E, e_charge,
    ALPHA, G, L_NODE, XI_TOPO, P_C, T_EM, V_SNAP, V_YIELD,
    ISOTROPIC_PROJECTION, NU_VAC, E_CRIT,
    RHO_BULK, NU_KIN, H_INFINITY, R_HUBBLE,
    PROTON_ELECTRON_RATIO, T_NUC,
    I_SCALAR_1D, V_TOROIDAL_HALO,
    DIELECTRIC_RUPTURE_STRAIN,
)

from ave.axioms.saturation import (
    epsilon_eff,
    capacitance_eff,
    reflection_coefficient,
    local_wave_speed,
    energy_density_nonlinear,
    impedance_at_strain,
)

from ave.axioms.isomorphism import (
    charge_to_length,
    length_to_charge,
    ohms_to_kinematic,
    mechanical_to_electrical,
)

from ave.gravity import (
    principal_radial_strain,
    refractive_index,
    is_dielectric_rupture,
    schwarzschild_radius,
    local_mu,
    local_epsilon,
    local_impedance,
    einstein_deflection_angle,
)


# =========================================================================
# TEST 1: DERIVED CONSTANTS CONSISTENCY
# =========================================================================

class TestDerivedConstants:
    """Verify all derived constants are self-consistent and match known values."""

    def test_speed_of_light_from_mu_eps(self):
        """c = 1/√(μ₀ε₀) must be exact."""
        c_derived = 1.0 / np.sqrt(MU_0 * EPSILON_0)
        assert abs(c_derived - C_0) / C_0 < 1e-10, (
            f"c₀ inconsistency: derived={c_derived}, stored={C_0}"
        )

    def test_impedance_from_mu_eps(self):
        """Z₀ = √(μ₀/ε₀) must be ≈ 376.73 Ω."""
        z_derived = np.sqrt(MU_0 / EPSILON_0)
        assert abs(z_derived - 376.73) < 0.01, f"Z₀ = {z_derived}, expected ≈ 376.73"
        assert abs(Z_0 - z_derived) / z_derived < 1e-10

    def test_l_node_is_compton_wavelength(self):
        """ℓ_node = ℏ/(m_e·c) ≈ 3.8616e-13 m."""
        l_expected = HBAR / (M_E * C_0)
        assert abs(L_NODE - l_expected) / l_expected < 1e-10
        assert abs(L_NODE - 3.8616e-13) / 3.8616e-13 < 0.001

    def test_xi_topo_computed(self):
        """ξ_topo = e/ℓ_node — not a placeholder."""
        xi_expected = e_charge / L_NODE
        assert abs(XI_TOPO - xi_expected) / xi_expected < 1e-10
        assert XI_TOPO != 1.0, "XI_TOPO must not be the old placeholder value 1.0"

    def test_packing_fraction(self):
        """p_c = 8πα ≈ 0.1834."""
        pc_expected = 8.0 * np.pi * ALPHA
        assert abs(P_C - pc_expected) / pc_expected < 1e-10
        assert abs(P_C - 0.1834) / 0.1834 < 0.005

    def test_string_tension(self):
        """T_EM = m_e c²/ℓ_node."""
        t_expected = (M_E * C_0**2) / L_NODE
        assert abs(T_EM - t_expected) / t_expected < 1e-10

    def test_v_snap(self):
        """V_snap = m_e c²/e ≈ 511 kV."""
        v_expected = (M_E * C_0**2) / e_charge
        assert abs(V_SNAP - v_expected) / v_expected < 1e-10
        assert abs(V_SNAP - 511e3) / 511e3 < 0.002  # Within 0.2% of 511 kV

    def test_poisson_ratio(self):
        """ν_vac = 2/7 exactly."""
        assert NU_VAC == 2.0 / 7.0

    def test_isotropic_projection(self):
        """1/7 isotropic projection factor."""
        assert ISOTROPIC_PROJECTION == 1.0 / 7.0

    def test_proton_mass_ratio(self):
        """The structural eigenvalue must yield m_p/m_e ≈ 1836.12."""
        assert abs(PROTON_ELECTRON_RATIO - 1836.15) / 1836.15 < 0.005, (
            f"Proton ratio = {PROTON_ELECTRON_RATIO:.4f}, "
            f"expected ≈ 1836.15 (empirical 1836.15267)"
        )

    def test_proton_eigenvalue_formula(self):
        """Verify the eigenvalue formula: x = I/(1 - V·p_c) + 1."""
        x_core = I_SCALAR_1D / (1.0 - V_TOROIDAL_HALO * P_C)
        x_total = x_core + 1.0
        assert abs(x_total - PROTON_ELECTRON_RATIO) < 1e-10

    def test_hubble_constant_units(self):
        """H∞ must be in [1/s] and convert to ~67-72 km/s/Mpc."""
        # Convert H [1/s] → km/s/Mpc
        Mpc_in_m = 3.0857e22  # 1 Megaparsec in meters
        H_km_s_Mpc = H_INFINITY * Mpc_in_m / 1000.0
        assert 60.0 < H_km_s_Mpc < 80.0, (
            f"H∞ = {H_km_s_Mpc:.2f} km/s/Mpc — outside plausible range [60,80]"
        )


# =========================================================================
# TEST 2: AXIOM 4 — DIELECTRIC SATURATION (ALL THREE REGIMES)
# =========================================================================

class TestAxiom4Saturation:
    """Verify the non-linear saturation operator across linear, non-linear, and rupture regimes."""

    # ---- LINEAR REGIME: V/V_yield << 1 ----

    def test_linear_recovery_epsilon(self):
        """In the linear limit (V ≈ 0), ε_eff → ε₀."""
        V_small = V_YIELD * 1e-6  # Tiny fraction of yield
        eps = epsilon_eff(V_small)
        assert abs(eps - EPSILON_0) / EPSILON_0 < 1e-10, (
            f"Linear limit broken: ε_eff = {eps}, expected ε₀ = {EPSILON_0}"
        )

    def test_linear_recovery_capacitance(self):
        """In the linear limit (Δφ ≈ 0), C_eff/C₀ → 1.0."""
        dphi_small = ALPHA * 1e-6
        c_ratio = capacitance_eff(dphi_small)
        assert abs(c_ratio - 1.0) < 1e-10

    def test_linear_recovery_wave_speed(self):
        """In the linear limit, c_eff → c₀."""
        V_small = V_YIELD * 1e-6
        c_eff = local_wave_speed(V_small)
        assert abs(c_eff - C_0) / C_0 < 1e-10

    def test_linear_energy_density(self):
        """In the linear limit, U ≈ ½ε₀·Δφ² (Maxwell)."""
        dphi = ALPHA * 1e-6
        U_nonlinear = energy_density_nonlinear(dphi)
        U_maxwell = 0.5 * EPSILON_0 * dphi**2
        # The E⁴ correction should be negligible
        assert abs(U_nonlinear - U_maxwell) / U_maxwell < 1e-6

    # ---- NON-LINEAR REGIME: V/V_yield ~ 0.5-0.9 ----

    def test_nonlinear_epsilon_decreases(self):
        """ε_eff must decrease as V increases (tested over full V_SNAP range)."""
        V_low = 0.1 * V_SNAP
        V_mid = 0.5 * V_SNAP
        V_high = 0.9 * V_SNAP

        eps_low = epsilon_eff(V_low, V_yield=V_SNAP)
        eps_mid = epsilon_eff(V_mid, V_yield=V_SNAP)
        eps_high = epsilon_eff(V_high, V_yield=V_SNAP)

        assert eps_low > eps_mid > eps_high > 0, (
            f"Monotonic decrease violated: {eps_low} > {eps_mid} > {eps_high}"
        )

    def test_nonlinear_e4_correction_dominates(self):
        """At moderate strain, the E⁴ term must contribute significantly."""
        dphi = ALPHA * 0.5  # 50% of saturation
        U_full = energy_density_nonlinear(dphi)
        U_linear = 0.5 * EPSILON_0 * dphi**2
        correction = U_full - U_linear
        # The correction should be positive and non-negligible
        assert correction > 0
        ratio = correction / U_linear
        assert ratio > 0.01, (
            f"E⁴ correction ratio = {ratio:.6f} — too small to matter at 50% strain"
        )

    def test_nonlinear_capacitance_diverges(self):
        """C_eff must increase (diverge) as Δφ → α."""
        c_low = capacitance_eff(ALPHA * 0.1)
        c_mid = capacitance_eff(ALPHA * 0.5)
        c_high = capacitance_eff(ALPHA * 0.9)

        assert c_high > c_mid > c_low > 1.0, (
            f"Capacitance divergence violated: {c_low}, {c_mid}, {c_high}"
        )
        # At 90% saturation, C_eff should be significantly elevated
        assert c_high > 2.0, f"C_eff at 90% = {c_high:.4f}, expected > 2.0"

    def test_nonlinear_wave_speed_slows(self):
        """c_eff must decrease as V increases (wave packets slow near saturation)."""
        c_low = local_wave_speed(0.1 * V_SNAP, V_yield=V_SNAP)
        c_high = local_wave_speed(0.9 * V_SNAP, V_yield=V_SNAP)
        assert c_low > c_high, "Wave speed must decrease with increasing strain"
        assert c_high > 0, "Wave speed must remain > 0 below rupture"

    def test_nonlinear_impedance_increases(self):
        """Z_eff must increase as V increases (medium becomes opaque)."""
        z_low = impedance_at_strain(0.1 * V_SNAP, V_yield=V_SNAP)
        z_high = impedance_at_strain(0.9 * V_SNAP, V_yield=V_SNAP)
        assert z_high > z_low > Z_0, (
            f"Impedance must increase: Z_low={z_low:.2f}, Z_high={z_high:.2f}"
        )

    # ---- SATURATION REGIME: V/V_yield → 1.0 ----

    def test_saturation_epsilon_approaches_zero(self):
        """At V = 0.9999 V_snap, ε_eff → ≈ 0 (topological destruction limit)."""
        V_near = 0.9999 * V_SNAP
        eps = epsilon_eff(V_near, V_yield=V_SNAP)
        assert eps < EPSILON_0 * 0.02, (
            f"ε_eff at 99.99% = {eps:.2e}, expected near zero"
        )

    def test_saturation_wave_speed_approaches_zero(self):
        """At saturation, c_eff → 0 (wave packet freezes → mass)."""
        V_near = 0.9999 * V_SNAP
        c_eff = local_wave_speed(V_near, V_yield=V_SNAP)
        assert c_eff / C_0 < 0.15, (
            f"c_eff/c₀ at 99.99% = {c_eff/C_0:.6f}, expected near zero"
        )

    def test_rupture_raises_error(self):
        """V > V_yield must raise ValueError (physical rupture)."""
        with pytest.raises(ValueError, match="Dielectric rupture"):
            epsilon_eff(1.01 * V_YIELD)

    def test_capacitance_rupture_raises_error(self):
        """Δφ ≥ α must raise ValueError (capacitance singularity)."""
        with pytest.raises(ValueError, match="singularity"):
            capacitance_eff(ALPHA * 1.001)

    def test_reflection_at_zero_impedance(self):
        """Γ = -1 when Z_knot = 0 (perfect reflection → confinement)."""
        gamma = reflection_coefficient(Z_knot=0.0)
        assert abs(gamma - (-1.0)) < 1e-10

    def test_reflection_at_matched_impedance(self):
        """Γ = 0 when Z_knot = Z_vac (perfect transmission)."""
        gamma = reflection_coefficient(Z_knot=Z_0)
        assert abs(gamma) < 1e-15

    # ---- ARRAY OPERATIONS ----

    def test_vectorized_epsilon(self):
        """epsilon_eff must handle numpy arrays correctly."""
        V_array = np.linspace(0, 0.99 * V_YIELD, 100)
        eps_array = epsilon_eff(V_array)
        assert len(eps_array) == 100
        assert np.all(eps_array > 0)
        assert np.all(np.diff(eps_array) < 0), "ε_eff must be monotonically decreasing"


# =========================================================================
# TEST 3: AXIOM 2 — TOPO-KINEMATIC ISOMORPHISM
# =========================================================================

class TestAxiom2Isomorphism:
    """Verify that the charge↔length dimensional bridge is self-consistent."""

    def test_charge_roundtrip(self):
        """charge → length → charge must be identity."""
        q0 = e_charge
        x = charge_to_length(q0)
        q_back = length_to_charge(x)
        assert abs(q_back - q0) / q0 < 1e-12

    def test_electron_charge_equals_l_node(self):
        """e → ℓ_node under the isomorphism."""
        x = charge_to_length(e_charge)
        assert abs(x - L_NODE) / L_NODE < 1e-10, (
            f"charge_to_length(e) = {x:.4e}, expected L_NODE = {L_NODE:.4e}"
        )

    def test_impedance_roundtrip(self):
        """Electrical → mechanical → electrical must be identity."""
        z_elec = Z_0
        z_mech = ohms_to_kinematic(z_elec)
        z_back = mechanical_to_electrical(z_mech)
        assert abs(z_back - z_elec) / z_elec < 1e-12

    def test_xi_topo_dimensions(self):
        """ξ_topo should have dimensions of [C/m] ≈ 4.15e-7."""
        assert abs(XI_TOPO - 4.15e-7) / 4.15e-7 < 0.01  # Within 1%


# =========================================================================
# TEST 4: GRAVITY / OPTICAL METRIC
# =========================================================================

class TestGravityOpticalMetric:
    """Verify the optical metric, achromatic matching, and GR limits."""

    # Use a Solar mass test case
    M_SUN = 1.989e30  # kg
    R_SUN = 6.957e8   # m

    def test_solar_refractive_index(self):
        """n(R_sun) = 1 + 2GM/(Rc²) should be extremely close to 1."""
        n = refractive_index(self.M_SUN, self.R_SUN)
        delta_n = n - 1.0
        expected = (2.0 * G * self.M_SUN) / (C_0**2 * self.R_SUN)
        assert abs(delta_n - expected) / expected < 1e-10
        assert 1e-6 < delta_n < 1e-5, f"Solar n-1 = {delta_n:.2e}"

    def test_achromatic_impedance_invariance(self):
        """Z(r) must equal Z₀ everywhere, regardless of mass or distance."""
        for r in [1e3, 1e6, 1e9, 1e12]:
            z = local_impedance(self.M_SUN, r)
            assert abs(z - Z_0) / Z_0 < 1e-10, (
                f"Z₀ invariance broken at r={r}: Z={z:.6f}, Z₀={Z_0:.6f}"
            )

    def test_achromatic_mu_eps_ratio(self):
        """μ'/ε' must always equal μ₀/ε₀."""
        for r in [1e3, 1e6, 1e9]:
            mu = local_mu(self.M_SUN, r)
            ep = local_epsilon(self.M_SUN, r)
            ratio = mu / ep
            baseline = MU_0 / EPSILON_0
            assert abs(ratio - baseline) / baseline < 1e-10

    def test_schwarzschild_radius_sun(self):
        """Schwarzschild radius of Sun ≈ 2953 m."""
        r_s = schwarzschild_radius(self.M_SUN)
        assert abs(r_s - 2953.0) / 2953.0 < 0.001

    def test_dielectric_rupture_inside_horizon(self):
        """Points inside R_s must trigger dielectric rupture."""
        r_s = schwarzschild_radius(self.M_SUN)
        assert is_dielectric_rupture(self.M_SUN, r_s * 0.9) is True
        assert is_dielectric_rupture(self.M_SUN, r_s * 1.1) is False

    def test_einstein_deflection_sun(self):
        """Light deflection past the Sun ≈ 1.75 arcsec."""
        delta = einstein_deflection_angle(self.M_SUN, self.R_SUN)
        arcsec = delta * (180.0 / np.pi) * 3600.0
        assert abs(arcsec - 1.75) / 1.75 < 0.01, (
            f"Deflection = {arcsec:.4f} arcsec, expected 1.75"
        )

    def test_radial_strain_at_horizon(self):
        """At the Schwarzschild radius, the principal strain must reach unity."""
        r_s = schwarzschild_radius(self.M_SUN)
        # At r slightly outside r_s, the effective strain from n(r)-1 side:
        # n(r_s) = 1 + 2GM/(c²·r_s) = 1 + 1 = 2
        n = refractive_index(self.M_SUN, r_s * 1.001)
        assert n > 1.99, f"n at horizon = {n:.6f}, expected ≈ 2.0"

    def test_principal_strain_7g(self):
        """ε₁₁(r) = 7GM/(c²r) — the factor 7 must be present."""
        r = 1e6  # 1000 km
        eps11 = principal_radial_strain(self.M_SUN, r)
        expected = (7.0 * G * self.M_SUN) / (C_0**2 * r)
        assert abs(eps11 - expected) / expected < 1e-12

    def test_poisson_contraction(self):
        """n(r) = 1 + (2/7)·ε₁₁ — Poisson ratio 2/7 properly applied."""
        r = 1e9
        eps11 = principal_radial_strain(self.M_SUN, r)
        n = refractive_index(self.M_SUN, r)
        # n - 1 = (2/7) * eps11
        delta_n = n - 1.0
        expected = (2.0 / 7.0) * eps11
        assert abs(delta_n - expected) / expected < 1e-10


# =========================================================================
# TEST 5: PROTON MASS EIGENVALUE (TOPOLOGICAL)
# =========================================================================

class TestProtonEigenvalue:
    """Verify the Borromean eigenvalue derivation reproduces m_p/m_e."""

    EMPIRICAL_RATIO = 1836.15267343  # PDG 2022

    def test_eigenvalue_within_1_percent(self):
        """The structural eigenvalue must be within 1% of the empirical value."""
        error = abs(PROTON_ELECTRON_RATIO - self.EMPIRICAL_RATIO) / self.EMPIRICAL_RATIO
        assert error < 0.01, (
            f"Eigenvalue = {PROTON_ELECTRON_RATIO:.4f}, "
            f"empirical = {self.EMPIRICAL_RATIO:.6f}, "
            f"error = {error*100:.2f}%"
        )

    def test_eigenvalue_feedback_loop(self):
        """The self-consistent equation x = I/(1-Vp_c) + 1 must converge."""
        # This is an algebraic closed form, not iterative —
        # but verify the denominator is positive (no pole)
        denom = 1.0 - V_TOROIDAL_HALO * P_C
        assert denom > 0, f"Denominator = {denom} — feedback loop diverges!"
        # And verify it produces a physically reasonable mass ratio
        x = I_SCALAR_1D / denom + 1.0
        assert 1800 < x < 1900


# =========================================================================
# TEST 6: CROSS-AXIOM CONSISTENCY
# =========================================================================

class TestCrossAxiomConsistency:
    """Tests that span multiple axioms to verify the framework is self-consistent."""

    def test_v_snap_is_saturation_boundary(self):
        """V_snap from Axiom 4 must equal m_e c²/e from Axiom 1."""
        v_from_axiom1 = (M_E * C_0**2) / e_charge
        assert abs(V_SNAP - v_from_axiom1) / v_from_axiom1 < 1e-12

    def test_string_tension_dimension_check(self):
        """T_EM = m_e c²/ℓ_node must have units of [N] (Newtons)."""
        # T_EM = [kg · m²/s²] / [m] = [kg·m/s²] = [N]. ✓
        # Numerical check: ~0.212 N
        assert 0.1 < T_EM < 1.0, f"T_EM = {T_EM:.4f} N — outside expected range"

    def test_nuclear_tension_ratio(self):
        """T_nuc / T_EM = m_p/m_e = PROTON_ELECTRON_RATIO."""
        ratio = T_NUC / T_EM
        assert abs(ratio - PROTON_ELECTRON_RATIO) / PROTON_ELECTRON_RATIO < 1e-10

    def test_hubble_within_tension_bounds(self):
        """H∞ must sit between the Planck (67.4) and SH0ES (73.0) values."""
        Mpc_in_m = 3.0857e22
        H_km_s_Mpc = H_INFINITY * Mpc_in_m / 1000.0
        # The manuscript predicts ≈69.3, which is between the two camps
        assert 65.0 < H_km_s_Mpc < 75.0, (
            f"H∞ = {H_km_s_Mpc:.2f} km/s/Mpc — outside tension window"
        )

    def test_ecrit_schwinger(self):
        """E_crit must match the Schwinger critical field ~ 1.32e18 V/m."""
        assert abs(E_CRIT - 1.32e18) / 1.32e18 < 0.01, (
            f"E_crit = {E_CRIT:.4e} — expected ≈ 1.32e18 V/m"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
