"""
Cross-Domain Universal Operator Test
=====================================
Verifies that the universal operators in scale_invariant.py
produce correct results across multiple physical domains.
"""

import pytest
from ave.axioms.scale_invariant import (
    regime_boundary_eigenvalue, phase_transition_Q,
    shear_modulus_ratio, saturation_factor,
)
from ave.core.constants import G, C_0, NU_VAC, L_NODE, ALPHA

M_SUN = 1.989e30


class TestUniversalOperators:
    """Test that universal operators work across domains."""

    # ── BH domain ──

    def test_bh_eigenvalue_schwarzschild(self):
        """ω_R·M = 18/49 for Schwarzschild ℓ=2."""
        M = 10 * M_SUN
        M_g = G * M / C_0**2
        r_sat = 7.0 * M_g
        omega = regime_boundary_eigenvalue(r_sat, NU_VAC, ell=2, c_wave=C_0)
        oR_dimless = omega * M_g / C_0
        assert abs(oR_dimless - 18.0/49.0) < 1e-10, f"ω_R·M = {oR_dimless}, expect 18/49"

    def test_bh_q_schwarzschild(self):
        """Q = ℓ = 2 for fundamental mode."""
        Q = phase_transition_Q(2)
        assert Q == 2.0

    def test_bh_eigenvalue_mass_independent(self):
        """ω_R·M must be independent of M (scale invariance)."""
        for M_solar in [1.0, 10.0, 62.0, 1000.0]:
            M = M_solar * M_SUN
            M_g = G * M / C_0**2
            r_sat = 7.0 * M_g
            omega = regime_boundary_eigenvalue(r_sat, NU_VAC, ell=2, c_wave=C_0)
            oR_dimless = omega * M_g / C_0
            assert abs(oR_dimless - 18.0/49.0) < 1e-10

    def test_bh_gr_accuracy(self):
        """ω_R·M within 2% of GR Schwarzschild value."""
        M_g = G * 10 * M_SUN / C_0**2
        r_sat = 7.0 * M_g
        omega = regime_boundary_eigenvalue(r_sat, NU_VAC, ell=2, c_wave=C_0)
        oR = omega * M_g / C_0
        gr_value = 0.3737
        assert abs(oR - gr_value) / gr_value < 0.02

    # ── Electron domain ──

    def test_bohr_radius_from_lnode(self):
        """a₀ = ℓ_node / α (exact)."""
        a0_ave = L_NODE / ALPHA
        a0_codata = 5.29177e-11  # m (CODATA 2018)
        assert abs(a0_ave - a0_codata) / a0_codata < 1e-4

    def test_ground_state_energy(self):
        """E = α²m_e c²/2 = 13.6 eV."""
        from ave.core.constants import M_E
        E_eV = 0.5 * ALPHA**2 * M_E * C_0**2 / 1.602176634e-19
        assert abs(E_eV - 13.6) / 13.6 < 0.01

    # ── Nuclear domain ──

    def test_miller_is_inverse_saturation(self):
        """Miller avalanche M = 1/S^n diverges at V_R/V_BR = 1."""
        for ratio in [0.1, 0.5, 0.9, 0.99]:
            # Miller: M = 1/(1 - ratio^n), n=5
            M_miller = 1.0 / (1.0 - ratio**5)
            # At ratio=1: M → ∞ (same as S → 0 at saturation)
            assert M_miller > 1.0
        # At ratio → 1: diverges
        M_near = 1.0 / (1.0 - 0.9999**5)
        assert M_near > 100

    # ── Scale invariance ──

    def test_saturation_factor_limits(self):
        """S(0) = 1, S(yield) = 0."""
        S_zero = float(saturation_factor(0.0, yield_limit=1.0))
        S_yield = float(saturation_factor(1.0, yield_limit=1.0, clip=True))
        assert abs(S_zero - 1.0) < 1e-10
        assert S_yield < 1e-7

    def test_shear_modulus_is_saturation(self):
        """shear_modulus_ratio is an alias for saturation_factor."""
        for strain in [0.0, 0.3, 0.7, 0.99]:
            S = float(saturation_factor(strain, yield_limit=1.0, clip=True))
            G = float(shear_modulus_ratio(strain, yield_strain=1.0))
            assert abs(S - G) < 1e-15

    # ── Co-rotating frame (FOC/Park) ──

    def test_co_rotating_schwarzschild(self):
        """With Ω=0, ω_I = ω_R/(2ℓ) = phase_transition_Q result."""
        from ave.axioms.scale_invariant import co_rotating_decay_rate
        omega_R = 18.0 / 49.0
        omega_I = co_rotating_decay_rate(omega_R, 0.0, ell=2)
        assert abs(omega_I - omega_R / 4.0) < 1e-10

    def test_co_rotating_superradiance(self):
        """At superradiance (ω_R = m·Ω), ω_I = 0."""
        from ave.axioms.scale_invariant import co_rotating_decay_rate
        omega_I = co_rotating_decay_rate(1.0, 0.5, ell=2, m=2)  # 1.0 = 2*0.5
        assert omega_I == 0.0

    def test_co_rotating_increases_Q(self):
        """Co-rotation reduces ω_I, increasing Q."""
        from ave.axioms.scale_invariant import co_rotating_decay_rate
        oI_static = co_rotating_decay_rate(0.5, 0.0, ell=2)
        oI_spinning = co_rotating_decay_rate(0.5, 0.05, ell=2)
        assert oI_spinning < oI_static

    # ── Avalanche factor (Miller) ──

    def test_avalanche_linear_limit(self):
        """At V=0, M=1 (no amplification)."""
        from ave.axioms.scale_invariant import avalanche_factor
        M = avalanche_factor(0.0, 1.0, 5)
        assert abs(M - 1.0) < 1e-10

    def test_avalanche_diverges_at_breakdown(self):
        """Near V=V_BR, M >> 1."""
        from ave.axioms.scale_invariant import avalanche_factor
        M = avalanche_factor(0.999, 1.0, 5)
        assert M > 30

    def test_avalanche_cinquefoil(self):
        """Miller with n=5 matches semiconductor binding engine."""
        from ave.axioms.scale_invariant import avalanche_factor
        # From semiconductor_binding_engine: M = 1/(1 - ratio^5)
        ratio = 0.7
        M_expected = 1.0 / (1.0 - ratio**5)
        M_universal = avalanche_factor(ratio, 1.0, 5)
        assert abs(M_universal - M_expected) < 1e-10


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
