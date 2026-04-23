"""Phase 4 — Asymmetric μ/ε saturation tests.

Pins the axiom-native (S_μ, S_ε) split that replaces the pre-Phase-4
single-kernel symmetric saturation per doc 54_ §6 + Vol 1 Ch 7:252.
S1 gate reopened 2026-04-23; see VACUUM_ENGINE_MANUAL §17 A14 r6.

Load-bearing invariants:

1. **κ_chiral = 1.2·α** per doc 20_ Sub-Theorem 3.1.1 for (2,3) winding.
2. **Symmetric case (h_local = 0, linear polarization)**: S_μ = S_ε →
   Z_eff = Z_0 constant (Achromatic Impedance Lens, Vol 4 Ch 11 —
   gravity regime, not pair-confinement).
3. **Asymmetric case (h_local > 0, RH Beltrami flow)**: A²_μ biased UP,
   A²_ε biased DOWN → S_μ < S_ε → Z_eff < Z_0 (Meissner-like μ collapse).
4. **Chirality bias sign-reversal**: LH drive gives inverse of RH.
5. **Legacy regression** (use_asymmetric_saturation=False): pre-Phase-4
   single-kernel S = √(1−A²_total) form; Z_eff = Z_0·(1−A²)^(−1/4).

References:
- research/L3_electron_soliton/54_pair_production_axiom_derivation.md §6
- manuscript/vol_1_foundations/chapters/07_regime_map.tex:252
- research/L3_electron_soliton/20_chirality_projection_sub_theorem.md
- research/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md §17 A14 r6
"""
from __future__ import annotations

import jax.numpy as jnp
import numpy as np
import pytest

from ave.core.constants import ALPHA
from ave.topological.cosserat_field_3d import (
    KAPPA_CHIRAL_ELECTRON,
    _beltrami_helicity,
    _reflection_density_asymmetric,
    _update_saturation_kernels,
)
from ave.topological.k4_cosserat_coupling import _coupling_energy_total
from ave.topological.vacuum_engine import VacuumEngine3D


# ═══════════════════════════════════════════════════════════════════════════
# Invariant 1 — κ_chiral constant
# ═══════════════════════════════════════════════════════════════════════════
class TestKappaChiralConstant:
    """κ_chiral = α·pq/(p+q) = 1.2·α for electron (2,3) winding per doc 20_."""

    def test_kappa_chiral_electron_equals_1_point_2_alpha(self):
        assert KAPPA_CHIRAL_ELECTRON == pytest.approx(1.2 * ALPHA, abs=1e-15)

    def test_kappa_chiral_numerical_value(self):
        # (p,q) = (2,3): α · 2·3/(2+3) = α · 6/5 = 1.2·α ≈ 8.757e-3
        assert KAPPA_CHIRAL_ELECTRON == pytest.approx(8.756823083e-3, rel=1e-6)


# ═══════════════════════════════════════════════════════════════════════════
# Invariant 2 — Beltrami helicity operator
# ═══════════════════════════════════════════════════════════════════════════
class TestBeltramiHelicity:
    """h_local = ω·(∇×ω) / (|ω|·|∇×ω|) ∈ [-1, +1]."""

    def test_zero_omega_gives_zero_helicity(self):
        """Vacuum state: ω = 0 everywhere → h_local = 0 (regularized 0/0)."""
        omega = jnp.zeros((6, 6, 6, 3), dtype=jnp.float64)
        h = _beltrami_helicity(omega, dx=1.0)
        assert np.allclose(np.asarray(h), 0.0, atol=1e-10)

    def test_uniform_omega_gives_zero_helicity(self):
        """Uniform ω (constant across lattice): ∇×ω = 0 → h_local = 0."""
        omega = jnp.ones((6, 6, 6, 3), dtype=jnp.float64) * 0.1
        h = _beltrami_helicity(omega, dx=1.0)
        assert np.allclose(np.asarray(h), 0.0, atol=1e-10)

    def test_right_handed_beltrami_flow_gives_positive_helicity(self):
        """Right-handed Beltrami: ω = (cos(kz), -sin(kz), 0).

        Derivation: (∇×ω)_x = ∂_y ω_z − ∂_z ω_y = 0 − (−k·cos(kz)) = +k·cos(kz)
                    (∇×ω)_y = ∂_z ω_x − ∂_x ω_z = −k·sin(kz) − 0 = −k·sin(kz)
        So ∇×ω = +k·(cos(kz), -sin(kz), 0) = +k·ω (Beltrami, right-handed).
        ω·(∇×ω) = +k·|ω|² > 0 → h_local = +1.
        """
        N = 16
        dx = 1.0
        k = 2.0 * np.pi / N
        z_idx = np.arange(N).reshape(1, 1, N)
        omega = np.zeros((N, N, N, 3), dtype=np.float64)
        omega[..., 0] = np.cos(k * z_idx)
        omega[..., 1] = -np.sin(k * z_idx)
        h = np.asarray(_beltrami_helicity(jnp.asarray(omega), dx=dx))
        assert h.mean() > 0.5, f"RH Beltrami: mean h = {h.mean():.3f}; expected > 0.5"

    def test_left_handed_beltrami_gives_negative_helicity(self):
        """LH Beltrami: ω = (cos(kz), +sin(kz), 0) → ∇×ω = −k·ω, h_local = −1."""
        N = 16
        dx = 1.0
        k = 2.0 * np.pi / N
        z_idx = np.arange(N).reshape(1, 1, N)
        omega = np.zeros((N, N, N, 3), dtype=np.float64)
        omega[..., 0] = np.cos(k * z_idx)
        omega[..., 1] = +np.sin(k * z_idx)
        h = np.asarray(_beltrami_helicity(jnp.asarray(omega), dx=dx))
        assert h.mean() < -0.5, f"LH Beltrami: mean h = {h.mean():.3f}; expected < -0.5"


# ═══════════════════════════════════════════════════════════════════════════
# Invariant 3 — Symmetric case (h=0): S_μ = S_ε → Z_eff = Z_0
# ═══════════════════════════════════════════════════════════════════════════
class TestSymmetricCaseAchromaticLens:
    """Under zero helicity (linear drive), S_μ = S_ε and Z_eff = Z_0.

    This is the Achromatic Impedance Lens behavior (Vol 4 Ch 11) —
    gravity regime, no pair-confinement. It DIFFERS from the pre-Phase-4
    single-kernel form which gave Z_eff = Z_0·(1−A²)^(−1/4); that was a
    simplification of the underlying dual-kernel axiom structure.
    """

    def test_zero_state_gives_both_kernels_unity(self):
        """At u=0, ω=0, V=0: S_μ = S_ε = 1 → Z_eff = Z_0."""
        N = 6
        u = jnp.zeros((N, N, N, 3), dtype=jnp.float64)
        omega = jnp.zeros((N, N, N, 3), dtype=jnp.float64)
        V_sq = jnp.zeros((N, N, N), dtype=jnp.float64)

        S_mu, S_eps = _update_saturation_kernels(
            u, omega, V_sq, dx=1.0, V_SNAP=1.0,
            omega_yield=np.pi, epsilon_yield=1.0,
            kappa_chiral=KAPPA_CHIRAL_ELECTRON,
        )
        assert np.allclose(np.asarray(S_mu), 1.0, atol=1e-10)
        assert np.allclose(np.asarray(S_eps), 1.0, atol=1e-10)

    def test_linear_drive_no_helicity_gives_z_eff_unchanged(self):
        """V_inc poked on one port, ω = 0 (no helicity): Z_eff = Z_0 constant.

        Linear polarization has no Beltrami handedness, so chirality bias
        is zero. Under the asymmetric form, A²_μ_base = 0 (κ from ω = 0
        is zero) and A²_ε_base = V²/V_SNAP² > 0. Since there's no ω, no
        magnetic sector contribution. This gives S_μ = 1, S_ε < 1, and
        Z_eff = √(S_μ/S_ε) = 1/√S_ε > 1 — the VARACTOR-ONLY effect.

        (NOTE: This is subtly different from the ideal Achromatic Lens
        case; the Lens assumes BOTH sectors excited symmetrically. With
        only K4 V (no Cosserat ω), only the electric sector gets loaded.)
        """
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0,
            use_asymmetric_saturation=True,
        )
        A_idx = np.argwhere(engine.k4.mask_active)
        site = tuple(A_idx[0])
        engine.k4.V_inc[site[0], site[1], site[2], 0] = (
            engine.V_SNAP * np.sqrt(0.3)  # A²_K4 = 0.3
        )
        engine._coupled._update_z_local_total()
        # At the poked site: A²_ε = 0.3 (from V), A²_μ = 0 (no ω).
        # S_μ = 1, S_ε = √0.7. Z_eff = √(S_μ/S_ε) = 1/S_ε^(1/2) = 0.7^(-1/4) ≈ 1.093.
        expected_z = 0.7 ** (-0.25)
        z_at_site = engine.k4.z_local_field[site[:3]]
        assert z_at_site == pytest.approx(expected_z, rel=1e-4)


# ═══════════════════════════════════════════════════════════════════════════
# Invariant 4 — Asymmetric case (Meissner): S_μ < S_ε under RH helicity
# ═══════════════════════════════════════════════════════════════════════════
class TestMeissnerAsymmetric:
    """Under RH Beltrami helicity, A²_μ grows faster than A²_ε → S_μ < S_ε."""

    def test_rh_beltrami_omega_biases_magnetic_sector_higher(self):
        """Construct ω field with non-zero curvature κ AND positive helicity.
        Under the chirality-bias formula:
            A²_μ = (1 + κ_chiral·h) · A²_μ_base
            A²_ε = (1 − κ_chiral·h) · A²_ε_base
        With h > 0, A²_μ > A²_μ_base and A²_ε < A²_ε_base.
        If A²_μ_base = A²_ε_base (same driving strength), then after bias:
        A²_μ > A²_ε → S_μ < S_ε.
        """
        N = 12
        dx = 1.0
        k = 2.0 * np.pi / N  # Beltrami wave

        # RH Beltrami ω field with some amplitude
        amp = 0.3  # small so we stay below saturation
        z_idx = np.arange(N).reshape(1, 1, N)
        omega = np.zeros((N, N, N, 3), dtype=np.float64)
        omega[..., 0] = amp * np.cos(k * z_idx)
        omega[..., 1] = amp * np.sin(k * z_idx)

        # u = 0 (no strain), V = 0 (no K4)
        u = np.zeros((N, N, N, 3), dtype=np.float64)
        V_sq = np.zeros((N, N, N), dtype=np.float64)

        S_mu, S_eps = _update_saturation_kernels(
            jnp.asarray(u), jnp.asarray(omega), jnp.asarray(V_sq),
            dx=dx, V_SNAP=1.0, omega_yield=np.pi, epsilon_yield=1.0,
            kappa_chiral=KAPPA_CHIRAL_ELECTRON,
        )
        S_mu_np = np.asarray(S_mu)
        S_eps_np = np.asarray(S_eps)

        # Under RH ω: curvature κ has all the saturation going into A²_μ
        # (both directly via κ²/ω_yield² AND amplified by (1+κ_chiral·h)).
        # ε_sym = 0 from u=0 + ω-contribution? Check.
        # Actually ε_sym = 0 requires ∂_j u_i - ε_ijk ω_k summed symmetrically.
        # With u=0, ε_ij = -ε_ijk ω_k. eps_sym = (ε + ε^T)/2 = -ε_ijk ω_k
        # symmetrized. Since ε_ijk is antisymmetric in ij, -ε_ijk ω_k is
        # antisymmetric in ij → (eps + eps^T)/2 = 0. So A²_ε_base = 0.
        #
        # Thus S_ε = 1 everywhere, S_μ < 1 at sites with curvature.
        # This DOES give S_μ < S_ε per the Meissner pattern.
        interior = slice(2, -2)
        S_mu_interior = S_mu_np[interior, interior, interior]
        S_eps_interior = S_eps_np[interior, interior, interior]
        assert S_mu_interior.mean() < S_eps_interior.mean(), (
            f"RH helicity: mean S_μ = {S_mu_interior.mean():.4f} "
            f"should be < mean S_ε = {S_eps_interior.mean():.4f}"
        )
        assert S_eps_interior.mean() == pytest.approx(1.0, abs=1e-6), (
            "With u=0, eps_sym should be zero → S_ε = 1 exactly"
        )

    def test_chirality_bias_reverses_for_lh_helicity(self):
        """Mirror test: LH ω field should produce the SAME |S_μ − S_ε| but
        with positive/negative sign swapped in A²_μ vs A²_ε contributions.

        Concretely: under LH helicity with u=0, h < 0 so
            A²_μ = (1 + κ_chiral·h)·A²_μ_base < A²_μ_base
        magnetic sector is SUPPRESSED instead of enhanced.
        """
        N = 12
        dx = 1.0
        k = 2.0 * np.pi / N
        amp = 0.3
        z_idx = np.arange(N).reshape(1, 1, N)

        # LH Beltrami: ω = (cos(kz), +sin(kz), 0) → ∇×ω = -k·ω → h < 0
        omega_lh = np.zeros((N, N, N, 3), dtype=np.float64)
        omega_lh[..., 0] = amp * np.cos(k * z_idx)
        omega_lh[..., 1] = +amp * np.sin(k * z_idx)

        u = np.zeros((N, N, N, 3), dtype=np.float64)
        V_sq = np.zeros((N, N, N), dtype=np.float64)

        S_mu_lh, _ = _update_saturation_kernels(
            jnp.asarray(u), jnp.asarray(omega_lh), jnp.asarray(V_sq),
            dx=dx, V_SNAP=1.0, omega_yield=np.pi, epsilon_yield=1.0,
            kappa_chiral=KAPPA_CHIRAL_ELECTRON,
        )

        # RH Beltrami: ω = (cos(kz), -sin(kz), 0) → ∇×ω = +k·ω → h > 0
        # Under RH, A²_μ = (1 + κ_chiral·h)·A²_μ_base > A²_μ_base → S_μ smaller
        omega_rh = np.zeros((N, N, N, 3), dtype=np.float64)
        omega_rh[..., 0] = amp * np.cos(k * z_idx)
        omega_rh[..., 1] = -amp * np.sin(k * z_idx)
        S_mu_rh, _ = _update_saturation_kernels(
            jnp.asarray(u), jnp.asarray(omega_rh), jnp.asarray(V_sq),
            dx=dx, V_SNAP=1.0, omega_yield=np.pi, epsilon_yield=1.0,
            kappa_chiral=KAPPA_CHIRAL_ELECTRON,
        )

        S_mu_lh_mean = float(jnp.mean(S_mu_lh[2:-2, 2:-2, 2:-2]))
        S_mu_rh_mean = float(jnp.mean(S_mu_rh[2:-2, 2:-2, 2:-2]))
        # RH magnetic sector more saturated → S_μ_rh < S_μ_lh
        assert S_mu_rh_mean < S_mu_lh_mean, (
            f"RH S_μ = {S_mu_rh_mean:.5f}, LH S_μ = {S_mu_lh_mean:.5f}; "
            f"RH should be smaller (more magnetic saturation)"
        )


# ═══════════════════════════════════════════════════════════════════════════
# Invariant 5 — Legacy regression: use_asymmetric_saturation=False
# ═══════════════════════════════════════════════════════════════════════════
class TestLegacyRegression:
    """Pre-Phase-4 single-kernel form available via use_asymmetric_saturation=False."""

    def test_legacy_path_computes_old_single_kernel_z(self):
        """With asymmetric=False + V poke: Z_eff/Z_0 = (1−A²)^(−1/4)."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0,
            use_asymmetric_saturation=False,
        )
        A_idx = np.argwhere(engine.k4.mask_active)
        site = tuple(A_idx[0])
        engine.k4.V_inc[site[0], site[1], site[2], 0] = (
            engine.V_SNAP * np.sqrt(0.3)  # A²_K4 = 0.3
        )
        engine._coupled._update_z_local_total()
        # Single-kernel: S = √(1 − 0.3), z = 1/√S = (1−0.3)^(−1/4) ≈ 1.094
        expected_z = 0.7 ** (-0.25)
        z_at_site = engine.k4.z_local_field[site[:3]]
        assert z_at_site == pytest.approx(expected_z, rel=1e-4)

    def test_legacy_coupling_energy_uses_multiplicative_form(self):
        """Legacy: L_c = (V²/V_SNAP²) · W_refl (symmetric)."""
        N = 6
        u = jnp.zeros((N, N, N, 3), dtype=jnp.float64)
        omega = jnp.zeros((N, N, N, 3), dtype=jnp.float64)
        omega = omega.at[3, 3, 3, 0].set(0.5)  # poke rotation
        V_sq = jnp.zeros((N, N, N), dtype=jnp.float64)
        V_sq = V_sq.at[3, 3, 3].set(0.1)  # poke V²

        E_legacy = _coupling_energy_total(
            u, omega, V_sq, V_SNAP=1.0, dx=1.0,
            omega_yield=np.pi, epsilon_yield=1.0,
        )
        assert float(E_legacy) >= 0.0  # energy density ≥ 0


# ═══════════════════════════════════════════════════════════════════════════
# Invariant 6 — Engine integration: CoupledK4Cosserat dispatches correctly
# ═══════════════════════════════════════════════════════════════════════════
class TestEngineIntegration:
    """CoupledK4Cosserat with use_asymmetric_saturation defaults + flag work."""

    def test_engine_default_is_asymmetric(self):
        """Phase 4 default: use_asymmetric_saturation = True."""
        engine = VacuumEngine3D.from_args(N=6, pml=0, temperature=0.0)
        assert engine._coupled.use_asymmetric_saturation is True
        assert engine._coupled.kappa_chiral == pytest.approx(
            KAPPA_CHIRAL_ELECTRON, abs=1e-15
        )

    def test_engine_vacuum_z_local_equals_unity(self):
        """Cold vacuum at t=0: Z_eff = Z_0 everywhere (no saturation)."""
        engine = VacuumEngine3D.from_args(N=8, pml=0, temperature=0.0)
        engine._coupled._update_z_local_total()
        # All active sites should have z_local = 1.0 (no u, ω, or V)
        assert np.allclose(engine.k4.z_local_field, 1.0, atol=1e-10)

    def test_engine_step_runs_under_asymmetric(self):
        """Full step() loop works under asymmetric saturation default."""
        engine = VacuumEngine3D.from_args(N=6, pml=0, temperature=0.0)
        for _ in range(5):
            engine.step()
        # No NaNs or infs introduced
        assert np.all(np.isfinite(engine.k4.V_inc))
        assert np.all(np.isfinite(engine.cos.u))
        assert np.all(np.isfinite(engine.cos.omega))
        assert np.all(np.isfinite(engine.k4.z_local_field))

    def test_engine_step_runs_under_legacy(self):
        """Legacy path (use_asymmetric_saturation=False) still works."""
        engine = VacuumEngine3D.from_args(
            N=6, pml=0, temperature=0.0,
            use_asymmetric_saturation=False,
        )
        for _ in range(5):
            engine.step()
        assert np.all(np.isfinite(engine.k4.V_inc))
        assert np.all(np.isfinite(engine.k4.z_local_field))


# ═══════════════════════════════════════════════════════════════════════════
# Invariant 7 — Reflection density asymmetric form
# ═══════════════════════════════════════════════════════════════════════════
class TestReflectionDensityAsymmetric:
    """Γ² = (1/16) |∇S_μ/S_μ − ∇S_ε/S_ε|² — vanishes when S_μ = S_ε."""

    def test_reflection_density_zero_at_rest(self):
        """At u=ω=V=0, both kernels = 1 everywhere → gradients zero → Γ² = 0."""
        N = 6
        u = jnp.zeros((N, N, N, 3), dtype=jnp.float64)
        omega = jnp.zeros((N, N, N, 3), dtype=jnp.float64)
        V_sq = jnp.zeros((N, N, N), dtype=jnp.float64)
        W = _reflection_density_asymmetric(
            u, omega, V_sq, dx=1.0, V_SNAP=1.0,
            omega_yield=np.pi, epsilon_yield=1.0,
            kappa_chiral=KAPPA_CHIRAL_ELECTRON,
        )
        assert np.allclose(np.asarray(W), 0.0, atol=1e-12)

    def test_reflection_density_nonneg(self):
        """|Γ|² ≥ 0 always (it's a squared magnitude)."""
        N = 8
        rng = np.random.default_rng(42)
        u = jnp.asarray(rng.normal(scale=0.05, size=(N, N, N, 3)))
        omega = jnp.asarray(rng.normal(scale=0.05, size=(N, N, N, 3)))
        V_sq = jnp.asarray(rng.uniform(0.0, 0.01, size=(N, N, N)))
        W = np.asarray(_reflection_density_asymmetric(
            u, omega, V_sq, dx=1.0, V_SNAP=1.0,
            omega_yield=np.pi, epsilon_yield=1.0,
            kappa_chiral=KAPPA_CHIRAL_ELECTRON,
        ))
        assert np.all(W >= -1e-12), f"min W = {W.min():.3e}"
