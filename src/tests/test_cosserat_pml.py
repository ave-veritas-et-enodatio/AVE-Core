"""
Cosserat-sector PML tests — pins the Perfectly Matched Layer derived in
[doc 58_](research/L3_electron_soliton/58_cosserat_pml_derivation.md).

Tests the four properties specified in doc 58_ §10.4:
  1. Interior energy conservation (pml_thickness=0 or d >= pml_thickness)
  2. Boundary kinetic-energy dissipation (monotonic in PML region)
  3. pml_thickness=0 disables (legacy behavior preserved)
  4. Composition with Ax4 saturation (no spurious drift when both active)

Plus a structural test:
  5. cos_pml_mask has the right quadratic-rolloff form

Reference:
  - src/ave/topological/cosserat_field_3d.py::CosseratField3D.__init__
  - src/ave/topological/cosserat_field_3d.py::_zero_velocities_outside_alive
  - research/L3_electron_soliton/58_cosserat_pml_derivation.md

Scope:
  All tests use CosseratField3D directly (not via CoupledK4Cosserat) to
  isolate the PML behavior from K4-Cosserat coupling dynamics. Ax3 scale-
  free action guarantees PML behavior is sector-local; testing it in
  isolation is sufficient.
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.topological.cosserat_field_3d import CosseratField3D


# ═══════════════════════════════════════════════════════════════════════════
# 1. Structural tests — mask construction
# ═══════════════════════════════════════════════════════════════════════════
class TestCosPMLMaskStructure:
    """The cos_pml_mask must match the K4 Sponge PML quadratic-rolloff formula."""

    def test_pml_thickness_zero_mask_is_all_ones(self):
        cos = CosseratField3D(nx=8, ny=8, nz=8, pml_thickness=0)
        assert np.all(cos.cos_pml_mask == 1.0)

    def test_pml_thickness_positive_mask_has_interior_ones(self):
        """Interior cells (d >= pml_thickness) should have mask = 1."""
        N, pml = 12, 3
        cos = CosseratField3D(nx=N, ny=N, nz=N, pml_thickness=pml)
        # Interior region: pml <= i,j,k < N-pml
        interior = cos.cos_pml_mask[pml:N-pml, pml:N-pml, pml:N-pml, 0]
        assert np.all(interior == 1.0)

    def test_pml_mask_zero_at_edge(self):
        """Outer edge (d = 0) should have mask = 0 (full absorption)."""
        cos = CosseratField3D(nx=10, ny=10, nz=10, pml_thickness=3)
        # The outermost layer (i=0 or i=N-1 etc.) should be zero
        edge_mask = cos.cos_pml_mask[0, 0, 0, 0]
        assert edge_mask == pytest.approx(0.0, abs=1e-12)

    def test_pml_mask_quadratic_rolloff_form(self):
        """Rolloff follows 1 - ((pml - d)/pml)^2 for d < pml_thickness."""
        N, pml = 12, 4
        cos = CosseratField3D(nx=N, ny=N, nz=N, pml_thickness=pml)
        # Sample along one axis at mid-plane
        for d in range(pml):
            expected = 1.0 - ((pml - d) / pml) ** 2
            # Cell at (d, N//2, N//2): min distance to boundary is d (assuming d < N-1-d)
            actual = cos.cos_pml_mask[d, N//2, N//2, 0]
            assert actual == pytest.approx(expected, abs=1e-12), (
                f"At d={d}: expected {expected}, got {actual}"
            )

    def test_pml_mask_monotonic_from_edge_inward(self):
        """mask should increase monotonically from edge toward interior."""
        cos = CosseratField3D(nx=10, ny=10, nz=10, pml_thickness=3)
        # Sample mask along x-axis at (i, N//2, N//2) from i=0 to i=pml
        axis_slice = cos.cos_pml_mask[:4, 5, 5, 0]
        diffs = np.diff(axis_slice)
        assert np.all(diffs >= 0), (
            f"Mask not monotonic along axis: {axis_slice}"
        )


# ═══════════════════════════════════════════════════════════════════════════
# 2. Legacy behavior — pml_thickness=0 preserves prior dynamics
# ═══════════════════════════════════════════════════════════════════════════
class TestCosPMLLegacyBehavior:
    """With pml_thickness=0, Cosserat evolution must match pre-PML behavior."""

    def test_default_is_pml_disabled(self):
        """Default pml_thickness=0 → Cosserat has no PML."""
        cos = CosseratField3D(nx=8, ny=8, nz=8)
        assert cos.pml_thickness == 0
        assert np.all(cos.cos_pml_mask == 1.0)

    def test_step_with_pml_zero_matches_no_pml(self):
        """Two engines with identical state, one pml=0, one no-PML-kwarg should
        produce bit-identical results after step()."""
        cos_default = CosseratField3D(nx=8, ny=8, nz=8)
        cos_pml0 = CosseratField3D(nx=8, ny=8, nz=8, pml_thickness=0)

        # Poke identical initial state
        np.random.seed(42)
        init_u = np.random.randn(8, 8, 8, 3) * 0.01
        init_omega = np.random.randn(8, 8, 8, 3) * 0.01

        cos_default.u = init_u.copy()
        cos_default.omega = init_omega.copy()
        cos_pml0.u = init_u.copy()
        cos_pml0.omega = init_omega.copy()

        cos_default.step(dt=0.01)
        cos_pml0.step(dt=0.01)

        np.testing.assert_allclose(cos_default.u, cos_pml0.u, rtol=1e-14)
        np.testing.assert_allclose(cos_default.omega, cos_pml0.omega, rtol=1e-14)


# ═══════════════════════════════════════════════════════════════════════════
# 3. Interior energy conservation — PML has zero effect in the interior
# ═══════════════════════════════════════════════════════════════════════════
class TestCosPMLInteriorConservation:
    """For cells with d >= pml_thickness, cos_pml_mask = 1 → kinetic-energy
    evolution is identical to the pml_thickness=0 baseline."""

    def test_interior_only_wavepacket_unaffected_by_pml(self):
        """A wavepacket localized in the deep interior should evolve identically
        in pml=0 and pml>0 engines."""
        N, pml = 16, 3
        cos_nopml = CosseratField3D(nx=N, ny=N, nz=N, pml_thickness=0)
        cos_withpml = CosseratField3D(nx=N, ny=N, nz=N, pml_thickness=pml)

        # Localized ω perturbation at the deep center
        center = (N // 2, N // 2, N // 2)
        amp = 1e-3
        cos_nopml.omega[center[0], center[1], center[2], 2] = amp
        cos_withpml.omega[center[0], center[1], center[2], 2] = amp

        # Step for a FEW steps — wavepacket should remain in interior
        # (propagation distance ≈ c * steps * dt ≈ ~1-2 cells total)
        for _ in range(4):
            cos_nopml.step(dt=0.01)
            cos_withpml.step(dt=0.01)

        # The u_dot, omega_dot fields in the deep interior should match
        deep_slice = slice(pml + 2, N - pml - 2)
        np.testing.assert_allclose(
            cos_nopml.u_dot[deep_slice, deep_slice, deep_slice, :],
            cos_withpml.u_dot[deep_slice, deep_slice, deep_slice, :],
            rtol=1e-12, atol=1e-14,
            err_msg="Interior u_dot should match pml=0 baseline"
        )
        np.testing.assert_allclose(
            cos_nopml.omega_dot[deep_slice, deep_slice, deep_slice, :],
            cos_withpml.omega_dot[deep_slice, deep_slice, deep_slice, :],
            rtol=1e-12, atol=1e-14,
            err_msg="Interior omega_dot should match pml=0 baseline"
        )


# ═══════════════════════════════════════════════════════════════════════════
# 4. Boundary dissipation — kinetic energy decays in the PML region
# ═══════════════════════════════════════════════════════════════════════════
class TestCosPMLBoundaryDissipation:
    """Waves propagating INTO the PML region should be attenuated.
    Kinetic-energy density in the PML monotonically decreases toward the edge."""

    def test_velocity_field_in_pml_attenuates(self):
        """Poke a large u̇ in the PML region; after one step, it should be
        attenuated by the mask factor."""
        N, pml = 16, 3
        cos = CosseratField3D(nx=N, ny=N, nz=N, pml_thickness=pml)

        # Pick an active site inside the PML region (d=1 from edge)
        # mask factor there = 1 - ((3-1)/3)^2 = 1 - 4/9 = 5/9 ≈ 0.5556
        # Find an A-site (even coords) at (2, 2, 2) — d=2 from all edges
        pml_site = (2, 2, 2)
        assert cos.mask_alive[pml_site], "Test site must be active"

        # Manually apply the mask via _zero_velocities_outside_alive
        # to verify the mask multiplication
        initial_u_dot = 1.0
        cos.u_dot[pml_site[0], pml_site[1], pml_site[2], 0] = initial_u_dot
        cos.omega_dot[pml_site[0], pml_site[1], pml_site[2], 0] = initial_u_dot

        cos._zero_velocities_outside_alive()

        # Mask at d=2 from edge: 1 - ((3-2)/3)^2 = 1 - 1/9 = 8/9 ≈ 0.889
        expected_mask = 1.0 - ((3 - 2) / 3) ** 2
        actual_u_dot = cos.u_dot[pml_site[0], pml_site[1], pml_site[2], 0]
        assert actual_u_dot == pytest.approx(
            initial_u_dot * expected_mask, rel=1e-10
        ), (
            f"Expected u_dot = {initial_u_dot * expected_mask:.6f}, "
            f"got {actual_u_dot:.6f}"
        )

    def test_pml_attenuation_profile_monotonic(self):
        """Poke uniform u_dot across a slice; after PML application, magnitude
        profile should be monotonic (non-decreasing from edge to interior)."""
        N, pml = 12, 3
        cos = CosseratField3D(nx=N, ny=N, nz=N, pml_thickness=pml)

        # Set u_dot = 1 everywhere (will be zeroed outside mask_alive)
        cos.u_dot[...] = 1.0
        cos._zero_velocities_outside_alive()

        # Sample along x-axis at an active-site row in y,z plane
        # Pick y=z=N//2 if that's an active site (even parity match)
        y = 0 if N // 2 % 2 != 0 else N // 2  # ensure even
        z = 0 if N // 2 % 2 != 0 else N // 2
        # Find an A-site row
        for y_try in [N // 2, N // 2 - 1, 0, 2]:
            if (y_try % 2 == 0):
                y = y_try
                z = y_try
                break
        # Sample u_dot[:, y, z, 0] (the x-axis, A-sites only)
        sample = cos.u_dot[::2, y, z, 0]  # every-other (A-sites at even i)
        # Magnitude should be monotonic from edge inward across PML
        # (values at i=0, 2, 4, 6, ...) -- first pml/2 + 1 samples in PML
        pml_samples = sample[:pml + 1]  # samples in or just past PML
        diffs = np.diff(pml_samples)
        assert np.all(diffs >= -1e-10), (
            f"PML attenuation profile not monotonic: {pml_samples}"
        )


# ═══════════════════════════════════════════════════════════════════════════
# 5. Composition with saturation (Ax4 / Op14 independence)
# ═══════════════════════════════════════════════════════════════════════════
class TestCosPMLSaturationComposition:
    """PML affects kinetic fields (u̇, ω̇); saturation affects coordinate-
    derived quantities (κ, ε). They operate on orthogonal state; no coupling
    interference should occur."""

    def test_pml_mask_matches_k4_pml_mask_shape(self):
        """The cos_pml_mask quadratic-rolloff formula matches K4's to float
        precision, mandated by Ax3 (scale-free action, same rule every sector)."""
        from ave.core.k4_tlm import K4Lattice3D

        N, pml = 10, 3
        k4 = K4Lattice3D(nx=N, ny=N, nz=N, pml_thickness=pml)
        cos = CosseratField3D(nx=N, ny=N, nz=N, pml_thickness=pml)

        np.testing.assert_array_equal(
            k4.pml_mask, cos.cos_pml_mask,
            err_msg="K4 and Cosserat PML masks must be bit-identical (Ax3 requirement)"
        )

    def test_saturation_kernels_unaffected_by_pml(self):
        """Op14 saturation depends on (u, omega) — NOT on kinetic fields. PML
        damps kinetic only. So a state with identical (u, omega) but different
        PML should produce identical saturation kernels."""
        from ave.topological.cosserat_field_3d import _update_saturation_kernels
        import jax.numpy as jnp

        N = 8
        cos_nopml = CosseratField3D(nx=N, ny=N, nz=N, pml_thickness=0)
        cos_withpml = CosseratField3D(nx=N, ny=N, nz=N, pml_thickness=2)

        # Identical (u, omega) state
        np.random.seed(0)
        u = np.random.randn(N, N, N, 3) * 0.1
        omega = np.random.randn(N, N, N, 3) * 0.1

        cos_nopml.u, cos_nopml.omega = u.copy(), omega.copy()
        cos_withpml.u, cos_withpml.omega = u.copy(), omega.copy()

        V_sq = np.zeros((N, N, N))  # no K4 contribution

        S_mu_a, S_eps_a = _update_saturation_kernels(
            jnp.asarray(cos_nopml.u), jnp.asarray(cos_nopml.omega),
            jnp.asarray(V_sq), cos_nopml.dx, 1.0,
            cos_nopml.omega_yield, cos_nopml.epsilon_yield,
        )
        S_mu_b, S_eps_b = _update_saturation_kernels(
            jnp.asarray(cos_withpml.u), jnp.asarray(cos_withpml.omega),
            jnp.asarray(V_sq), cos_withpml.dx, 1.0,
            cos_withpml.omega_yield, cos_withpml.epsilon_yield,
        )

        np.testing.assert_allclose(np.asarray(S_mu_a), np.asarray(S_mu_b), rtol=1e-14)
        np.testing.assert_allclose(np.asarray(S_eps_a), np.asarray(S_eps_b), rtol=1e-14)


# ═══════════════════════════════════════════════════════════════════════════
# 6. Integration with VacuumEngine3D — PML inherited from K4 pml
# ═══════════════════════════════════════════════════════════════════════════
class TestCosPMLEngineIntegration:
    """CoupledK4Cosserat should wire pml_thickness from K4 to Cosserat."""

    def test_cosserat_inherits_pml_from_coupled_engine(self):
        from ave.topological.vacuum_engine import VacuumEngine3D
        engine = VacuumEngine3D.from_args(N=8, pml=2, temperature=0.0)
        assert engine.cos.pml_thickness == 2
        # Cosserat PML mask should be non-trivial
        assert np.any(engine.cos.cos_pml_mask < 1.0)

    def test_cosserat_pml_zero_when_engine_pml_zero(self):
        from ave.topological.vacuum_engine import VacuumEngine3D
        engine = VacuumEngine3D.from_args(N=8, pml=0, temperature=0.0)
        assert engine.cos.pml_thickness == 0
        assert np.all(engine.cos.cos_pml_mask == 1.0)

    def test_engine_step_with_pml_runs_without_nan(self):
        """End-to-end: engine steps with Cosserat PML active + K4 PML active,
        no NaN or inf anywhere after a handful of steps."""
        from ave.topological.vacuum_engine import VacuumEngine3D
        engine = VacuumEngine3D.from_args(N=12, pml=3, temperature=0.0)
        # Poke some initial Cosserat energy near boundary
        engine.cos.omega[1, 1, 1, 2] = 0.01
        engine.run(n_steps=5)
        assert np.all(np.isfinite(engine.cos.u))
        assert np.all(np.isfinite(engine.cos.omega))
        assert np.all(np.isfinite(engine.cos.u_dot))
        assert np.all(np.isfinite(engine.cos.omega_dot))
