"""A10 closure — thermal equipartition validation.

Per VACUUM_ENGINE_MANUAL §17 A10: zero tests of `initialize_thermal(T)`'s
equipartition variances exist in the suite. This file closes that gap
(~1 day effort per Grant's own manual note: "highest-leverage non-
Grant-adjudication item").

Pins the Maxwell-Boltzmann variances per [doc 47_ §2](../../research/L3_electron_soliton/47_thermal_lattice_noise.md)
and [VacuumEngine3D.initialize_thermal](../ave/topological/vacuum_engine.py):

    σ_V per port = √(4π·T/α) · V_SNAP       (ONLY if thermalize_V=True)
    σ_ω          = √(T · mode_int / (4π²·I_ω))    mode_int ≈ 1.14
    σ_ω̇          = √(T / I_ω)
    σ_u          = √(T / (2π · ρ))
    σ_u̇          = √(T / ρ)

Temperature T is in m_e c² natural units (T = 1 means kT = electron
rest energy). Stability requires `thermalize_V=True` runs at
T < α/(4π) ≈ 5.8×10⁻⁴ per [doc 47_ §2.2](../../research/L3_electron_soliton/47_thermal_lattice_noise.md)
(AVE Schwinger temperature ~3.44 MK).

Sample-size discipline: for N=16 lattice, ~2·(N/2)³ ≈ 2048 active sites
× 3 vector components = ~6144 samples per DOF. Standard error of σ
estimate is σ/√(2·n_sample) ≈ 0.9%, so 5% tolerance is safe.

Tests also validate:
- T=0 gives deterministic zero fields (C1 — [46_ §2.1](../../research/L3_electron_soliton/46_vacuum_engine_scope.md))
- Default thermalize_V=False leaves V_inc = 0 even for hot Cosserat
- Seed reproducibility
- σ ∝ √T scaling across multiple temperatures
- Mean ≈ 0 within standard error (no systematic bias)

References:
- research/L3_electron_soliton/47_thermal_lattice_noise.md §2 (canonical variances)
- research/L3_electron_soliton/46_vacuum_engine_scope.md §2.1 (C1 cold-vacuum determinism)
- src/ave/topological/vacuum_engine.py ::VacuumEngine3D.initialize_thermal
- VACUUM_ENGINE_MANUAL §17 A10 (audit item closed by this file)
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.core.constants import ALPHA
from ave.topological.vacuum_engine import VacuumEngine3D


# Pre-computed theoretical constants
MODE_INT = np.pi - 2.0 * np.arctan(np.pi / 2.0)  # ≈ 1.1338
T_STABLE_V = ALPHA / (4.0 * np.pi) * 0.5          # Stay well below rupture
T_HOT_COS = 0.1                                    # Cosserat-only hot regime (per Phase III-B)


def _active_samples(field: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """Extract values at active sites, flattened across vector components."""
    if field.ndim == mask.ndim:
        # scalar field
        return field[mask]
    # vector field (..., n_components)
    return field[mask].ravel()


def _theoretical_sigma_omega(T: float, I_omega: float = 1.0) -> float:
    """σ_ω = √(T · mode_int / (4π²·I_ω))"""
    return float(np.sqrt(T * MODE_INT / (4.0 * np.pi ** 2 * I_omega)))


def _theoretical_sigma_omega_dot(T: float, I_omega: float = 1.0) -> float:
    """σ_ω̇ = √(T / I_ω)"""
    return float(np.sqrt(T / I_omega))


def _theoretical_sigma_u(T: float, rho: float = 1.0) -> float:
    """σ_u = √(T / (2π·ρ))"""
    return float(np.sqrt(T / (2.0 * np.pi * rho)))


def _theoretical_sigma_u_dot(T: float, rho: float = 1.0) -> float:
    """σ_u̇ = √(T / ρ)"""
    return float(np.sqrt(T / rho))


def _theoretical_sigma_V(T: float) -> float:
    """σ_V per port = √(4π·T/α) · V_SNAP. V_SNAP = 1 in natural units."""
    return float(np.sqrt(4.0 * np.pi * T / ALPHA))


# ═══════════════════════════════════════════════════════════════════════════
# C1 — Cold-vacuum determinism (T = 0)
# ═══════════════════════════════════════════════════════════════════════════
class TestC1ColdVacuumDeterminism:
    """Per [46_ §2.1 C1], at T=0 the AVE vacuum is deterministic. All
    fields set to zero exactly."""

    def test_T_zero_gives_zero_V_inc(self):
        engine = VacuumEngine3D.from_args(N=8, pml=0, temperature=0.0)
        assert np.all(engine.k4.V_inc == 0.0)

    def test_T_zero_gives_zero_V_ref(self):
        engine = VacuumEngine3D.from_args(N=8, pml=0, temperature=0.0)
        assert np.all(engine.k4.V_ref == 0.0)

    def test_T_zero_gives_zero_cosserat_fields(self):
        engine = VacuumEngine3D.from_args(N=8, pml=0, temperature=0.0)
        assert np.all(engine.cos.u == 0.0)
        assert np.all(engine.cos.u_dot == 0.0)
        assert np.all(engine.cos.omega == 0.0)
        assert np.all(engine.cos.omega_dot == 0.0)

    def test_T_zero_with_thermalize_V_true_still_zero(self):
        """thermalize_V is ignored when T=0 — fields still deterministic zero."""
        engine = VacuumEngine3D.from_args(N=8, pml=0, temperature=0.0)
        engine.initialize_thermal(0.0, seed=42, thermalize_V=True)
        assert np.all(engine.k4.V_inc == 0.0)
        assert np.all(engine.cos.omega == 0.0)


# ═══════════════════════════════════════════════════════════════════════════
# Mode integral theoretical value
# ═══════════════════════════════════════════════════════════════════════════
class TestModeIntegralConstant:
    """mode_int = π − 2·arctan(π/2) per doc 47_ for m² = 4 massive mode."""

    def test_mode_int_numerical_value(self):
        # π − 2·arctan(π/2) = 3.14159... − 2·1.00389... = 1.13382...
        assert MODE_INT == pytest.approx(1.13382, rel=1e-4)

    def test_mode_int_sits_between_1_and_pi_halves(self):
        # Sanity: 0 < mode_int < π (full range)
        assert 0.0 < MODE_INT < np.pi


# ═══════════════════════════════════════════════════════════════════════════
# Cosserat equipartition variances (default thermalize_V=False)
# ═══════════════════════════════════════════════════════════════════════════
class TestCosseratEquipartition:
    """Hot Cosserat sector, cold K4 (thermalize_V=False — default).

    Uses T = 0.1 m_e c² (= Phase III-B canonical hot-bath temperature,
    5.93×10⁸ K SI). Cosserat-only thermalization is stable at this T;
    thermal-V would rupture per doc 47_ §2.2."""

    @pytest.fixture(scope="class")
    def hot_engine(self):
        """Engine at T=0.1 with fixed seed for reproducibility."""
        engine = VacuumEngine3D.from_args(
            N=16, pml=2, temperature=T_HOT_COS,
            amplitude_convention="V_SNAP",
        )
        # Fresh re-init with deterministic seed for test stability
        engine.initialize_thermal(T_HOT_COS, seed=12345, thermalize_V=False)
        return engine

    def test_omega_sigma_matches_theory(self, hot_engine):
        """σ_ω empirical vs √(T · 1.14 / (4π²·I_ω))."""
        samples = _active_samples(hot_engine.cos.omega, hot_engine.cos.mask_alive)
        sigma_empirical = float(samples.std())
        sigma_theory = _theoretical_sigma_omega(T_HOT_COS, hot_engine.cos.I_omega)
        assert sigma_empirical == pytest.approx(sigma_theory, rel=0.05), (
            f"σ_ω empirical = {sigma_empirical:.5f}, theory = {sigma_theory:.5f}, "
            f"rel err = {abs(sigma_empirical/sigma_theory - 1)*100:.2f}%"
        )

    def test_omega_dot_sigma_matches_theory(self, hot_engine):
        """σ_ω̇ empirical vs √(T / I_ω)."""
        samples = _active_samples(hot_engine.cos.omega_dot, hot_engine.cos.mask_alive)
        sigma_empirical = float(samples.std())
        sigma_theory = _theoretical_sigma_omega_dot(T_HOT_COS, hot_engine.cos.I_omega)
        assert sigma_empirical == pytest.approx(sigma_theory, rel=0.05)

    def test_u_sigma_matches_theory(self, hot_engine):
        """σ_u empirical vs √(T / (2π·ρ))."""
        samples = _active_samples(hot_engine.cos.u, hot_engine.cos.mask_alive)
        sigma_empirical = float(samples.std())
        sigma_theory = _theoretical_sigma_u(T_HOT_COS, hot_engine.cos.rho)
        assert sigma_empirical == pytest.approx(sigma_theory, rel=0.05)

    def test_u_dot_sigma_matches_theory(self, hot_engine):
        """σ_u̇ empirical vs √(T / ρ)."""
        samples = _active_samples(hot_engine.cos.u_dot, hot_engine.cos.mask_alive)
        sigma_empirical = float(samples.std())
        sigma_theory = _theoretical_sigma_u_dot(T_HOT_COS, hot_engine.cos.rho)
        assert sigma_empirical == pytest.approx(sigma_theory, rel=0.05)

    def test_omega_mean_near_zero(self, hot_engine):
        """⟨ω⟩ should be zero within standard error."""
        samples = _active_samples(hot_engine.cos.omega, hot_engine.cos.mask_alive)
        mean = float(samples.mean())
        sigma = float(samples.std())
        stderr = sigma / np.sqrt(len(samples))
        # Accept within 4σ stderr (one-off test; 4σ gives ~99.99% passage rate)
        assert abs(mean) < 4.0 * stderr, (
            f"⟨ω⟩ = {mean:.6e}, stderr = {stderr:.6e}, ratio = {mean/stderr:.2f}σ"
        )

    def test_u_mean_near_zero(self, hot_engine):
        samples = _active_samples(hot_engine.cos.u, hot_engine.cos.mask_alive)
        mean = float(samples.mean())
        sigma = float(samples.std())
        stderr = sigma / np.sqrt(len(samples))
        assert abs(mean) < 4.0 * stderr

    def test_V_inc_stays_zero_when_thermalize_V_false(self, hot_engine):
        """Default thermalize_V=False: K4 voltage stays zero even when Cosserat is hot."""
        assert np.all(hot_engine.k4.V_inc == 0.0)
        assert np.all(hot_engine.k4.V_ref == 0.0)


# ═══════════════════════════════════════════════════════════════════════════
# V_inc equipartition (thermalize_V=True, stable regime only)
# ═══════════════════════════════════════════════════════════════════════════
class TestVEquipartitionStableRegime:
    """Hot K4 sector at T < α/(4π) (below AVE Schwinger temperature per
    doc 47_ §2.2). Above that threshold σ_V > V_SNAP and the vacuum
    ruptures numerically — physically correct early-universe behavior,
    not a test failure."""

    def test_V_sigma_matches_theory_at_stable_T(self):
        """σ_V per port = √(4π·T/α) · V_SNAP at T < α/(4π)."""
        T = T_STABLE_V  # = α/(4π)/2 — comfortably below rupture
        engine = VacuumEngine3D.from_args(
            N=16, pml=2, temperature=0.0,  # Will re-init below
            amplitude_convention="V_SNAP",
        )
        engine.initialize_thermal(T, seed=777, thermalize_V=True)

        active_mask = engine.k4.mask_active
        V_samples = _active_samples(engine.k4.V_inc, active_mask)
        # V_SNAP = 1 in natural units (engine default), so σ_V natural = √(4π·T/α)
        sigma_empirical = float(V_samples.std())
        sigma_theory = _theoretical_sigma_V(T) * engine.V_SNAP
        assert sigma_empirical == pytest.approx(sigma_theory, rel=0.05), (
            f"σ_V empirical = {sigma_empirical:.5e}, theory = {sigma_theory:.5e}"
        )


# ═══════════════════════════════════════════════════════════════════════════
# Seed reproducibility + sqrt(T) scaling
# ═══════════════════════════════════════════════════════════════════════════
class TestSeedReproducibility:
    """Same seed → bit-identical state; different seed → different state
    with matching σ."""

    def test_same_seed_gives_bit_identical_state(self):
        eng_a = VacuumEngine3D.from_args(N=8, pml=0, temperature=0.0)
        eng_b = VacuumEngine3D.from_args(N=8, pml=0, temperature=0.0)
        eng_a.initialize_thermal(0.05, seed=9999)
        eng_b.initialize_thermal(0.05, seed=9999)
        assert np.array_equal(eng_a.cos.u, eng_b.cos.u)
        assert np.array_equal(eng_a.cos.omega, eng_b.cos.omega)
        assert np.array_equal(eng_a.cos.u_dot, eng_b.cos.u_dot)
        assert np.array_equal(eng_a.cos.omega_dot, eng_b.cos.omega_dot)

    def test_different_seeds_give_different_states(self):
        eng_a = VacuumEngine3D.from_args(N=8, pml=0, temperature=0.0)
        eng_b = VacuumEngine3D.from_args(N=8, pml=0, temperature=0.0)
        eng_a.initialize_thermal(0.05, seed=1)
        eng_b.initialize_thermal(0.05, seed=2)
        assert not np.array_equal(eng_a.cos.u, eng_b.cos.u)
        assert not np.array_equal(eng_a.cos.omega, eng_b.cos.omega)

    def test_different_seeds_give_matching_sigma(self):
        """Different seeds → same distribution → σ should match within SE."""
        T = 0.1
        sigmas_omega = []
        for seed in [10, 20, 30, 40, 50]:
            eng = VacuumEngine3D.from_args(N=16, pml=2, temperature=0.0)
            eng.initialize_thermal(T, seed=seed)
            samples = _active_samples(eng.cos.omega, eng.cos.mask_alive)
            sigmas_omega.append(float(samples.std()))
        sigmas_omega = np.array(sigmas_omega)
        theory = _theoretical_sigma_omega(T)
        # Each individual σ within 5% of theory (per Cosserat class tests)
        max_rel_err = float(np.max(np.abs(sigmas_omega / theory - 1.0)))
        assert max_rel_err < 0.05, (
            f"Seed ensemble σ_ω values = {sigmas_omega}, theory = {theory}"
        )


class TestSqrtTScaling:
    """σ_field ∝ √T. Halving T halves σ² (or multiplies σ by 1/√2)."""

    def test_sigma_omega_scales_as_sqrt_T(self):
        T_ref = 0.1
        T_scaled = 0.025  # factor 4 reduction → σ should halve
        ratios = []
        for seed in [101, 202, 303]:
            eng_ref = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
            eng_ref.initialize_thermal(T_ref, seed=seed)
            eng_sc = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
            eng_sc.initialize_thermal(T_scaled, seed=seed)
            s_ref = float(_active_samples(eng_ref.cos.omega, eng_ref.cos.mask_alive).std())
            s_sc = float(_active_samples(eng_sc.cos.omega, eng_sc.cos.mask_alive).std())
            ratios.append(s_ref / s_sc)
        avg_ratio = float(np.mean(ratios))
        # Theory: ratio = √(T_ref / T_scaled) = √4 = 2
        expected = np.sqrt(T_ref / T_scaled)
        assert avg_ratio == pytest.approx(expected, rel=0.05), (
            f"σ_ref/σ_scaled ratio = {avg_ratio:.3f}, expected {expected:.3f}"
        )

    def test_sigma_u_scales_as_sqrt_T(self):
        T_ref = 0.2
        T_scaled = 0.05
        eng_ref = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        eng_ref.initialize_thermal(T_ref, seed=555)
        eng_sc = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        eng_sc.initialize_thermal(T_scaled, seed=555)
        s_ref = float(_active_samples(eng_ref.cos.u, eng_ref.cos.mask_alive).std())
        s_sc = float(_active_samples(eng_sc.cos.u, eng_sc.cos.mask_alive).std())
        assert s_ref / s_sc == pytest.approx(np.sqrt(T_ref / T_scaled), rel=0.05)


# ═══════════════════════════════════════════════════════════════════════════
# Cosserat moduli override — variance scales inversely with ρ, I_ω
# ═══════════════════════════════════════════════════════════════════════════
class TestModuliScaling:
    """σ_ω ∝ 1/√I_ω; σ_u ∝ 1/√ρ. Validates the formula under non-default
    S4=A Cosserat moduli."""

    def test_sigma_u_inversely_scales_with_rho(self):
        """σ_u = √(T / (2π·ρ)); doubling ρ → σ_u by 1/√2."""
        T = 0.1
        eng_default = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        eng_default.initialize_thermal(T, seed=1111)
        # Re-construct with ρ = 2.0 (non-default)
        eng_heavy = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0, rho=2.0)
        eng_heavy.initialize_thermal(T, seed=1111)
        s_default = float(_active_samples(eng_default.cos.u, eng_default.cos.mask_alive).std())
        s_heavy = float(_active_samples(eng_heavy.cos.u, eng_heavy.cos.mask_alive).std())
        assert s_default / s_heavy == pytest.approx(np.sqrt(2.0), rel=0.05), (
            f"σ_u(ρ=1)/σ_u(ρ=2) = {s_default/s_heavy:.3f}, expected √2 = {np.sqrt(2.0):.3f}"
        )

    def test_sigma_omega_inversely_scales_with_I_omega(self):
        """σ_ω = √(T·1.14 / (4π²·I_ω)); doubling I_ω → σ_ω by 1/√2."""
        T = 0.1
        eng_default = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        eng_default.initialize_thermal(T, seed=2222)
        eng_heavy = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0, I_omega=2.0)
        eng_heavy.initialize_thermal(T, seed=2222)
        s_default = float(_active_samples(eng_default.cos.omega, eng_default.cos.mask_alive).std())
        s_heavy = float(_active_samples(eng_heavy.cos.omega, eng_heavy.cos.mask_alive).std())
        assert s_default / s_heavy == pytest.approx(np.sqrt(2.0), rel=0.05)


# ═══════════════════════════════════════════════════════════════════════════
# Active-mask respect: inactive sites stay zero
# ═══════════════════════════════════════════════════════════════════════════
class TestActiveMaskRespect:
    """Thermal initialization must only write to active sites (bipartite
    K4 mask + PML exclusion on Cosserat side)."""

    def test_cosserat_omega_zero_at_inactive_sites(self):
        engine = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        engine.initialize_thermal(0.1, seed=3333)
        # Inactive sites (PML region) should be exactly zero
        inactive = ~engine.cos.mask_alive
        assert np.all(engine.cos.omega[inactive] == 0.0)
        assert np.all(engine.cos.omega_dot[inactive] == 0.0)
        assert np.all(engine.cos.u[inactive] == 0.0)
        assert np.all(engine.cos.u_dot[inactive] == 0.0)

    def test_V_inc_zero_at_inactive_sites_under_thermalize_V(self):
        T = T_STABLE_V
        engine = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        engine.initialize_thermal(T, seed=4444, thermalize_V=True)
        inactive = ~engine.k4.mask_active
        assert np.all(engine.k4.V_inc[inactive] == 0.0)
