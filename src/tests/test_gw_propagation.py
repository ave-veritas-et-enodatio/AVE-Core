"""
Test suite for Gravitational Wave Propagation.

Verifies:
  1. Schwarzschild radius matches GR
  2. SYMMETRIC GRAVITY: Z ≡ Z₀ everywhere, Γ = 0 (no reflection)
  3. GW strain is far below saturation (linear propagation)
  4. Refractive index > 1 near mass (gravitational lensing)
  5. Local speed c_local = c/n decreases near mass
"""

import numpy as np
import pytest

from ave.core.constants import C_0, EPSILON_0, MU_0, V_SNAP, Z_0
from ave.gravity.gw_propagation import (
    epsilon_eff_schwarzschild,
    gravitational_impedance,
    gw_local_speed,
    gw_propagation_summary,
    gw_strain_to_voltage,
    horizon_reflection,
    is_linear_propagation,
    mu_eff_schwarzschild,
    radial_strain,
    refractive_index,
    saturation_radius,
    schwarzschild_radius,
    shear_horizon_reflection,
    shear_impedance,
    shear_wave_speed,
)

M_SUN = 1.989e30  # Solar mass [kg]


class TestSchwarzschildRadius:
    """r_s = 2GM/c² must match GR."""

    def test_sun(self) -> None:
        """For the Sun: r_s ≈ 2.95 km."""
        r_s = schwarzschild_radius(M_SUN)
        assert r_s == pytest.approx(2953, rel=0.01)

    def test_30_solar(self) -> None:
        """For a 30 M☉ black hole: r_s ≈ 88.6 km."""
        r_s = schwarzschild_radius(30 * M_SUN)
        assert r_s == pytest.approx(88600, rel=0.01)

    def test_proportional(self) -> None:
        """r_s scales linearly with M."""
        assert schwarzschild_radius(2 * M_SUN) == pytest.approx(2 * schwarzschild_radius(M_SUN), rel=1e-10)


class TestSymmetricGravity:
    """Symmetric Gravity: Z ≡ Z₀ everywhere, Γ = 0."""

    def test_far_field_vacuum(self) -> None:
        """Far from mass: ε → ε₀, μ → μ₀, Z → Z₀."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r = 1e6 * r_s  # Very far
        assert float(epsilon_eff_schwarzschild(r, r_s)) == pytest.approx(EPSILON_0, rel=1e-4)
        assert float(mu_eff_schwarzschild(r, r_s)) == pytest.approx(MU_0, rel=1e-4)
        assert float(gravitational_impedance(r, r_s)) == pytest.approx(Z_0, rel=1e-4)

    def test_impedance_constant_everywhere(self) -> None:
        """Z must equal Z₀ at ALL radii — this IS Symmetric Gravity."""
        r_s = schwarzschild_radius(30 * M_SUN)
        for mult in [1.01, 1.1, 2, 5, 10, 100, 1000]:
            r = mult * r_s
            Z = float(gravitational_impedance(r, r_s))
            assert Z == pytest.approx(Z_0, rel=1e-3), f"Z({mult}·r_s) = {Z:.2f}, expected {Z_0:.2f}"

    def test_gamma_em_zero_everywhere(self) -> None:
        """EM-channel Γ_EM = 0 at ALL radii — light transparent, no EM echoes.

        NOTE (channel-split): this is the EM channel ONLY. The shear/GW
        channel REFLECTS (Γ_shear = −1) — see TestChannelSplitReflection.
        """
        r_s = schwarzschild_radius(30 * M_SUN)
        for mult in [1.01, 1.1, 2, 5, 10, 100, 1000]:
            r = mult * r_s
            gamma = float(horizon_reflection(r, r_s))
            assert abs(gamma) < 0.01, f"Γ_EM({mult}·r_s) = {gamma:.6f}, expected ~0"

    def test_epsilon_mu_scale_symmetrically(self) -> None:
        """ε and μ must scale by the SAME factor n(r)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        for mult in [1.1, 2, 10, 100]:
            r = mult * r_s
            eps = float(epsilon_eff_schwarzschild(r, r_s))
            mu = float(mu_eff_schwarzschild(r, r_s))
            n_from_eps = eps / EPSILON_0
            n_from_mu = mu / MU_0
            assert n_from_eps == pytest.approx(
                n_from_mu, rel=1e-10
            ), f"Asymmetric scaling at {mult}·r_s: ε-factor={n_from_eps}, μ-factor={n_from_mu}"

    def test_near_horizon_epsilon_diverges(self) -> None:
        """Near horizon: ε >> ε₀ (metric is deeply strained)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r = 1.01 * r_s
        eps = float(epsilon_eff_schwarzschild(r, r_s))
        assert eps > 10 * EPSILON_0

    def test_near_horizon_mu_diverges(self) -> None:
        """Near horizon: μ >> μ₀ (symmetric with ε)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r = 1.01 * r_s
        mu = float(mu_eff_schwarzschild(r, r_s))
        assert mu > 10 * MU_0


class TestGWLinearPropagation:
    """LIGO GW must be in the linear regime (no saturation)."""

    def test_ligo_strain_is_linear(self) -> None:
        """h = 10⁻²¹ at 100 Hz must be linear."""
        assert is_linear_propagation(1e-21, 100.0)

    def test_strain_voltage_is_tiny(self) -> None:
        """V_GW / V_SNAP ~ 10⁻¹⁹ for LIGO GW."""
        V_gw = gw_strain_to_voltage(1e-21, 100.0)
        ratio = V_gw / V_SNAP
        assert ratio < 1e-10  # Many orders of magnitude below saturation

    def test_gw_always_below_saturation(self) -> None:
        """Even h = 1 produces V_gw << V_SNAP — GW can NEVER saturate."""
        V_gw = gw_strain_to_voltage(1.0, 100.0)
        ratio = V_gw / V_SNAP
        assert ratio < 1e-3, f"V_gw/V_SNAP = {ratio:.2e}, expected << 1"


class TestRefractiveIndex:
    """Gravity well must have n > 1 (lensing)."""

    def test_far_field_n_equals_one(self) -> None:
        """Far from mass: n → 1 (flat space)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        n = float(refractive_index(1e12 * r_s, r_s))
        assert n == pytest.approx(1.0, abs=1e-6)

    def test_near_mass_n_greater_than_one(self) -> None:
        """Near mass: n > 1 (light bends)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        n = float(refractive_index(10 * r_s, r_s))
        assert n > 1.0

    def test_monotonically_increasing_inward(self) -> None:
        """n increases as r decreases (stronger lensing)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r = np.array([100, 50, 20, 10, 5]) * r_s
        n = refractive_index(r, r_s)
        assert np.all(np.diff(n) > 0)  # n increases as r decreases


class TestLocalSpeed:
    """c_local = c/n must decrease near mass."""

    def test_far_field_speed_is_c(self) -> None:
        """Far from mass: c_local → c₀."""
        r_s = schwarzschild_radius(30 * M_SUN)
        c_local = gw_local_speed(1e12 * r_s, r_s)
        assert c_local == pytest.approx(C_0, rel=1e-6)

    def test_near_mass_speed_drops(self) -> None:
        """Near mass: c_local < c₀ (light slows)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        c_local = gw_local_speed(10 * r_s, r_s)
        assert c_local < C_0

    def test_near_horizon_speed_approaches_zero(self) -> None:
        """Near horizon: c_local → 0."""
        r_s = schwarzschild_radius(30 * M_SUN)
        c_local = gw_local_speed(1.01 * r_s, r_s)
        assert c_local < 0.02 * C_0


class TestSummary:
    """Summary function should produce complete output."""

    def test_summary_runs(self) -> None:
        """Summary should run without errors."""
        result = gw_propagation_summary(30.0, 1e-21)
        assert result["linear_propagation"] is True
        assert len(result["profiles"]) > 0
        assert result["r_s_m"] > 0

    def test_summary_no_em_echo_delay_key(self) -> None:
        """Summary should NOT contain an EM echo_delay key (EM Γ_EM = 0).

        The shear/GW channel reflects (Γ_shear = −1) and echoes ARE
        predicted, but the GW-echo is retrospective (reflect ⇒ echo) — no
        SHA-pinned forward prereg, so no numeric echo_delay_s is emitted.
        """
        result = gw_propagation_summary(30.0, 1e-21)
        assert "echo_delay_s" not in result

    def test_summary_carries_both_channels(self) -> None:
        """Each profile must surface BOTH channels (channel-split, not one)."""
        result = gw_propagation_summary(30.0, 1e-21)
        prof = result["profiles"][0]
        for key in ("gamma_em", "gamma_shear", "Z_em_ohm", "Z_shear", "c_shear"):
            assert key in prof, f"summary profile missing channel key {key!r}"
        assert "r_sat_m" in result


class TestChannelSplitReflection:
    """SIGN-GATE (analog of the #278 sign-gate): the substrate-forced
    channel-split at the BH horizon.

    EM-transverse channel:  Γ_EM = 0      (symmetric gravity, light transparent)
    Shear / GW channel:     Γ_shear = −1  (G_shear→0 ⇒ Z_shear→0 ⇒ Op3 short)

    Asserting BOTH simultaneously is the discriminator the old engine
    failed: it computed only the EM Γ=0 (right number, wrong channel) and
    declared "no black hole echoes." The shear channel reflects, so GW
    ringdown echoes are predicted (reflect ⇒ echo).
    """

    def test_r_sat_is_3p5_rs(self) -> None:
        """Shear/bulk rupture boundary r_sat = 7GM/c² = 3.5·r_s."""
        r_s = schwarzschild_radius(30 * M_SUN)
        assert saturation_radius(r_s) == pytest.approx(3.5 * r_s, rel=1e-12)

    def test_radial_strain_unity_at_r_sat(self) -> None:
        """ε₁₁ → 1 at r_sat (the rupture condition)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r_sat = saturation_radius(r_s)
        assert float(radial_strain(r_sat, r_s)) == pytest.approx(1.0, abs=1e-12)

    def test_shear_speed_collapses_at_r_sat(self) -> None:
        """c_shear → 0 at r_sat (shear restoring force vanishes)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r_sat = saturation_radius(r_s)
        assert float(shear_wave_speed(r_sat, r_s)) == pytest.approx(0.0, abs=1.0)
        # Far field: shear speed recovers to ~c.
        assert float(shear_wave_speed(1e6 * r_s, r_s)) == pytest.approx(C_0, rel=1e-3)

    def test_shear_impedance_collapses_at_r_sat(self) -> None:
        """Z_shear → 0 at r_sat (free surface / Op3 short)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r_sat = saturation_radius(r_s)
        Z_sat = float(shear_impedance(r_sat, r_s))
        Z_far = float(shear_impedance(1e6 * r_s, r_s))
        assert Z_sat < 1e-6 * Z_far, f"Z_shear(r_sat)={Z_sat:.3e} not collapsed vs far {Z_far:.3e}"

    def test_CHANNEL_SPLIT_em_zero_shear_minus_one_at_horizon(self) -> None:
        """THE SIGN-GATE: at the horizon Γ_EM = 0 AND Γ_shear = −1.

        This is the whole walk-back in one assertion. A single-channel
        "absorber" engine cannot pass this: it gives one Γ, not two.
        """
        r_s = schwarzschild_radius(30 * M_SUN)
        r_sat = saturation_radius(r_s)

        # EM channel: matched everywhere, including at r_sat.
        gamma_em = float(horizon_reflection(r_sat, r_s))
        assert abs(gamma_em) < 1e-3, f"Γ_EM(r_sat) = {gamma_em:.6f}, expected 0"

        # Shear channel: total reflection at r_sat.
        gamma_shear = float(shear_horizon_reflection(r_sat, r_s))
        assert gamma_shear == pytest.approx(-1.0, abs=1e-3), (
            f"Γ_shear(r_sat) = {gamma_shear:.6f}, expected −1 (GW reflect)"
        )

        # The two channels DISAGREE — that is the point (not one absorber).
        assert abs(gamma_em - gamma_shear) > 0.9

    def test_shear_gamma_negative_inside_horizon(self) -> None:
        """Γ_shear stays at the −1 short across the saturated interior."""
        r_s = schwarzschild_radius(30 * M_SUN)
        r_sat = saturation_radius(r_s)
        for mult in [1.0, 0.8, 0.5, 0.2]:  # at and inside r_sat
            r = mult * r_sat
            g = float(shear_horizon_reflection(r, r_s))
            assert g == pytest.approx(-1.0, abs=1e-3), f"Γ_shear({mult}·r_sat) = {g:.6f}"

    def test_shear_gamma_recovers_to_zero_far_field(self) -> None:
        """Far from the mass, the shear channel is matched too (Γ_shear → 0)."""
        r_s = schwarzschild_radius(30 * M_SUN)
        g = float(shear_horizon_reflection(1e6 * r_s, r_s))
        assert abs(g) < 1e-3, f"Γ_shear(far) = {g:.6f}, expected ~0"
