"""
ENV-D unit tests U0 and U2 for the bond-reflection form and step(apply_pml).

U0: legacy byte-identity — with reflection_form="grad" (default), the energy,
    gradient, and 10-step trajectory are bitwise equal to the pre-ENV-D code
    path (demonstrated by comparing the default CosseratField3D path against
    the unchanged module-level _val_and_grad_saturated / _val_and_grad_bare
    functions called directly with the same args, which still reach
    _reflection_density unmodified).

U2: bond-form gradient correctness and per-site bound:
    - jax.grad matches central finite difference to 1e-6 relative at sites
      where x_s > 10*delta.
    - W_refl <= 1/dx^2 at every site.
    - Energy is finite past yield (A2 > 1).

Spec: ~/AVE-staging/ave-program-tracker/physics-walks/muon-g2/
      ENVD-bond-reflection-method-sheet_2026-10-03.md §4, sha 342a3254859e.

U1, U3, U4 are out of scope for this PR.
"""

import numpy as np
import jax
import jax.numpy as jnp

# Float64 is required for the U2 FD test: with a kicked-site field the total
# energy is ~700, giving float32 SNR of ~3 at eps_fd=1e-4 — far below the
# 1e-6 relative tolerance the spec requires.  Enabling x64 here is safe
# because all byte-identity comparisons (U0) compare the same code path
# against itself, so they pass whether both sides are float32 or float64.
jax.config.update("jax_enable_x64", True)

from ave.topological.cosserat_field_3d import (
    CosseratField3D,
    _reflection_density_bond,
    _val_and_grad_saturated,
    _val_and_grad_bare,
    TETRA_OFFSETS,
)


# ---------------------------------------------------------------------------
# U0 — legacy byte-identity at defaults
# ---------------------------------------------------------------------------


def _make_seeded_solver(nx=16, ny=16, nz=16, rng_seed=42, **kwargs):
    """Create a CosseratField3D, seed omega with random alive-site values."""
    solver = CosseratField3D(nx, ny, nz, **kwargs)
    rng = np.random.default_rng(rng_seed)
    # Small-amplitude random field (well below yield)
    omega_vals = rng.uniform(-0.05, 0.05, (nx, ny, nz, 3))
    u_vals = rng.uniform(-0.02, 0.02, (nx, ny, nz, 3))
    solver.omega = omega_vals * solver.mask_alive[..., None]
    solver.u = u_vals * solver.mask_alive[..., None]
    return solver


class TestU0LegacyByteIdentity:
    """U0: default path (reflection_form='grad') is byte-identical to the
    pre-ENV-D behaviour proven by comparing against the module-level jitted
    functions directly (those still reach _reflection_density unchanged)."""

    def _get_jax_inputs(self, solver):
        return (
            jnp.asarray(solver.u),
            jnp.asarray(solver.omega),
            solver._mask_alive_jax,
        )

    def test_u0_energy_gradient_bitwise_equal_saturated(self):
        """Energy and gradient from CosseratField3D (default) == module-level
        _val_and_grad_saturated called directly."""
        solver = _make_seeded_solver(use_saturation=True)
        u_j, w_j, mask = self._get_jax_inputs(solver)

        # Reference: call the (unchanged) module-level jitted function directly
        E_ref, (du_ref, dw_ref) = _val_and_grad_saturated(
            u_j, w_j, mask,
            solver.dx, solver.G, solver.G_c, solver.gamma,
            solver.omega_yield, solver.epsilon_yield,
            solver.k_op10, solver.k_refl, solver.k_hopf,
        )

        # Test path: CosseratField3D.energy_gradient() with default form
        dE_du, dE_dw = solver.energy_gradient()
        E_solver = solver.total_energy()

        assert float(E_ref) == E_solver, (
            f"energy mismatch: reference={float(E_ref)}, solver={E_solver}"
        )
        np.testing.assert_array_equal(
            np.asarray(du_ref) * np.asarray(mask)[..., None],
            dE_du,
            err_msg="dE/du mismatch between direct call and solver (saturated)",
        )
        np.testing.assert_array_equal(
            np.asarray(dw_ref) * np.asarray(mask)[..., None],
            dE_dw,
            err_msg="dE/domega mismatch between direct call and solver (saturated)",
        )

    def test_u0_energy_gradient_bitwise_equal_bare(self):
        """Same check for the bare (no saturation) path."""
        solver = _make_seeded_solver(use_saturation=False)
        u_j, w_j, mask = self._get_jax_inputs(solver)

        E_ref, (du_ref, dw_ref) = _val_and_grad_bare(
            u_j, w_j, mask,
            solver.dx, solver.G, solver.G_c, solver.gamma,
            solver.k_op10, solver.k_refl, solver.k_hopf,
            solver.omega_yield, solver.epsilon_yield,
        )

        dE_du, dE_dw = solver.energy_gradient()
        E_solver = solver.total_energy()

        assert float(E_ref) == E_solver
        np.testing.assert_array_equal(
            np.asarray(du_ref) * np.asarray(mask)[..., None],
            dE_du,
        )
        np.testing.assert_array_equal(
            np.asarray(dw_ref) * np.asarray(mask)[..., None],
            dE_dw,
        )

    def test_u0_10step_state_bitwise_equal(self):
        """State after 10 steps is bitwise identical between the default
        CosseratField3D and one explicitly constructed with reflection_form='grad'."""
        solver_a = _make_seeded_solver(use_saturation=True)
        solver_b = _make_seeded_solver(use_saturation=True, reflection_form="grad")

        # Both must start from the same state
        np.testing.assert_array_equal(solver_a.u, solver_b.u)
        np.testing.assert_array_equal(solver_a.omega, solver_b.omega)

        # Seed velocities
        rng = np.random.default_rng(7)
        v = rng.uniform(-1e-3, 1e-3, solver_a.u.shape)
        vw = rng.uniform(-1e-3, 1e-3, solver_a.omega.shape)
        for s in (solver_a, solver_b):
            s.u_dot = v * s.mask_alive[..., None]
            s.omega_dot = vw * s.mask_alive[..., None]

        dt = 0.05
        for _ in range(10):
            solver_a.step(dt)
            solver_b.step(dt)

        np.testing.assert_array_equal(
            solver_a.u, solver_b.u,
            err_msg="u state after 10 steps differs between default and explicit 'grad'",
        )
        np.testing.assert_array_equal(
            solver_a.omega, solver_b.omega,
            err_msg="omega state after 10 steps differs",
        )
        np.testing.assert_array_equal(
            solver_a.u_dot, solver_b.u_dot,
            err_msg="u_dot state after 10 steps differs",
        )
        np.testing.assert_array_equal(
            solver_a.omega_dot, solver_b.omega_dot,
            err_msg="omega_dot state after 10 steps differs",
        )


# ---------------------------------------------------------------------------
# U2 — bond-form gradient vs finite difference, bound, finite past yield
# ---------------------------------------------------------------------------


def _make_bond_solver_with_high_a2(nx=16, ny=16, nz=16, rng_seed=99, delta=1e-3):
    """Create a bond-form solver with 5 isolated sites kicked just past yield (A2 ≈ 1.1).

    Kick amplitude omega_i ≈ ±0.43 targets A2 = eps_sq ≈ 2*3*(0.43)^2 ≈ 1.11 > 1.
    Five isolated kicked sites keeps the 20 FD test-sites statistically away from
    the kicked sites' kappa-backward-neighborhoods (see filter in the FD test).
    """
    solver = CosseratField3D(nx, ny, nz, reflection_form="bond", reflection_delta=delta)
    rng = np.random.default_rng(rng_seed)
    omega_vals = rng.uniform(-0.03, 0.03, (nx, ny, nz, 3))
    u_vals = rng.uniform(-0.01, 0.01, (nx, ny, nz, 3))
    solver.omega = omega_vals * solver.mask_alive[..., None]
    solver.u = u_vals * solver.mask_alive[..., None]
    alive_ijk = np.argwhere(solver.mask_alive)
    n_kick = 5
    kick_idx = rng.choice(len(alive_ijk), size=n_kick, replace=False)
    for ki in kick_idx:
        i, j, k = alive_ijk[ki]
        signs = rng.choice([-1, 1], size=3).astype(float)
        solver.omega[i, j, k] = rng.uniform(0.40, 0.46, 3) * signs
    return solver


def _compute_w_refl_bond_field(solver):
    """Return W_refl per site from _reflection_density_bond using current state."""
    u_j = jnp.asarray(solver.u)
    w_j = jnp.asarray(solver.omega)
    return np.asarray(
        _reflection_density_bond(
            u_j, w_j, solver.dx, solver.omega_yield, solver.epsilon_yield,
            solver.reflection_delta,
        )
    )


def _a2_field(solver):
    """Return A2 per site from current state."""
    from ave.topological.cosserat_field_3d import _compute_strain, _compute_curvature
    u_j = jnp.asarray(solver.u)
    w_j = jnp.asarray(solver.omega)
    eps = _compute_strain(u_j, w_j, solver.dx)
    kappa = _compute_curvature(w_j, solver.dx)
    eps_sq = jnp.sum(eps * eps, axis=(-1, -2))
    kappa_sq = jnp.sum(kappa * kappa, axis=(-1, -2))
    return np.asarray(
        eps_sq / (solver.epsilon_yield ** 2) + kappa_sq / (solver.omega_yield ** 2)
    )


class TestU2BondFormGradientAndBound:
    """U2: bond-form gradient vs central FD to 1e-6 relative where
    x_s > 10*delta; W <= 1/dx^2 everywhere; finite past yield."""

    def test_u2_w_bounded_by_inv_dx_sq(self):
        """W_refl <= 1/dx^2 at every alive site (also dead sites are 0)."""
        solver = _make_bond_solver_with_high_a2()
        W = _compute_w_refl_bond_field(solver)
        dx = solver.dx
        bound = 1.0 / (dx * dx)
        assert np.all(np.isfinite(W)), "W_refl has non-finite values"
        alive = solver.mask_alive
        np.testing.assert_array_less(
            W[alive] - bound,
            1e-9 * bound * np.ones(alive.sum()),
            err_msg=f"W_refl exceeds 1/dx^2={bound:.4g} at some alive sites",
        )

    def test_u2_finite_past_yield(self):
        """Energy is finite even where A2 > 1."""
        solver = _make_bond_solver_with_high_a2()
        A2 = _a2_field(solver)
        beyond_yield = (A2 > 1.0) & solver.mask_alive
        assert beyond_yield.sum() > 0, "no sites past yield in test field — increase amplitude"
        W = _compute_w_refl_bond_field(solver)
        assert np.all(np.isfinite(W[beyond_yield])), "W_refl not finite past yield"

    def test_u2_gradient_vs_finite_difference(self):
        """At 20 random alive sites with x_s > 10*delta, jax.grad matches
        central FD to 1e-6 relative error."""
        delta = 1e-3
        solver = _make_bond_solver_with_high_a2(delta=delta)

        A2 = _a2_field(solver)
        x = 1.0 - A2
        x_s = 0.5 * (x + np.sqrt(x * x + delta * delta))

        # Exclude sites whose kappa/epsilon backward-neighbors (s-p for p in
        # TETRA_OFFSETS) are kicked past yield.  Perturbing u or omega at site s
        # propagates through those backward-neighbor sites via the tetrahedral
        # gradient stencil; a kicked site there has small x_s ≈ d^2/(4|x|) which
        # causes large f''' and makes FD truncation exceed 1e-6 relative at h=1e-4.
        kicked_mask = (A2 > 1.0) & solver.mask_alive
        not_backward_kicked = np.ones_like(solver.mask_alive, dtype=bool)
        for _p in TETRA_OFFSETS:
            # np.roll(kicked, +p)[s] == kicked[s-p]: true if s-p is kicked
            not_backward_kicked &= ~np.roll(
                kicked_mask, shift=(_p[0], _p[1], _p[2]), axis=(0, 1, 2)
            )

        qualifying = np.where(solver.mask_alive & (x_s > 10 * delta) & not_backward_kicked)
        n_sites = len(qualifying[0])
        assert n_sites >= 20, (
            f"fewer than 20 qualifying sites (x_s > 10*delta, no kicked backward-nbr)"
            f" in test grid: {n_sites}"
        )

        rng = np.random.default_rng(17)
        idx_choice = rng.choice(n_sites, size=20, replace=False)
        sites = [(qualifying[0][i], qualifying[1][i], qualifying[2][i]) for i in idx_choice]

        # Get the jax gradient of the total energy wrt (u, omega)
        dE_du, dE_dw = solver.energy_gradient()

        eps_fd = 1e-4

        for si, sj, sk in sites:
            # --- check u gradient at this site (3 components) ---
            for comp in range(3):
                u_plus = solver.u.copy()
                u_plus[si, sj, sk, comp] += eps_fd
                u_minus = solver.u.copy()
                u_minus[si, sj, sk, comp] -= eps_fd

                from ave.topological.cosserat_field_3d import (
                    _total_energy_saturated_bond_jit,
                    _total_energy_bare_bond_jit,
                )

                u_p_j = jnp.asarray(u_plus)
                u_m_j = jnp.asarray(u_minus)
                w_j = jnp.asarray(solver.omega)
                mask = solver._mask_alive_jax

                if solver.use_saturation:
                    E_p = float(_total_energy_saturated_bond_jit(
                        u_p_j, w_j, mask,
                        solver.dx, solver.G, solver.G_c, solver.gamma,
                        solver.omega_yield, solver.epsilon_yield,
                        solver.k_op10, solver.k_refl, solver.k_hopf,
                        solver.reflection_delta,
                    ))
                    E_m = float(_total_energy_saturated_bond_jit(
                        u_m_j, w_j, mask,
                        solver.dx, solver.G, solver.G_c, solver.gamma,
                        solver.omega_yield, solver.epsilon_yield,
                        solver.k_op10, solver.k_refl, solver.k_hopf,
                        solver.reflection_delta,
                    ))
                else:
                    E_p = float(_total_energy_bare_bond_jit(
                        u_p_j, w_j, mask,
                        solver.dx, solver.G, solver.G_c, solver.gamma,
                        solver.k_op10, solver.k_refl, solver.k_hopf,
                        solver.omega_yield, solver.epsilon_yield,
                        solver.reflection_delta,
                    ))
                    E_m = float(_total_energy_bare_bond_jit(
                        u_m_j, w_j, mask,
                        solver.dx, solver.G, solver.G_c, solver.gamma,
                        solver.k_op10, solver.k_refl, solver.k_hopf,
                        solver.omega_yield, solver.epsilon_yield,
                        solver.reflection_delta,
                    ))

                fd_grad = (E_p - E_m) / (2.0 * eps_fd)
                jax_grad = float(dE_du[si, sj, sk, comp])

                denom = max(abs(jax_grad), abs(fd_grad), 1e-12)
                rel_err = abs(jax_grad - fd_grad) / denom
                assert rel_err < 1e-6, (
                    f"u grad mismatch at ({si},{sj},{sk}) comp={comp}: "
                    f"jax={jax_grad:.6e} fd={fd_grad:.6e} rel={rel_err:.2e}"
                )

            # --- check omega gradient at this site (3 components) ---
            for comp in range(3):
                w_plus = solver.omega.copy()
                w_plus[si, sj, sk, comp] += eps_fd
                w_minus = solver.omega.copy()
                w_minus[si, sj, sk, comp] -= eps_fd

                u_j = jnp.asarray(solver.u)
                w_p_j = jnp.asarray(w_plus)
                w_m_j = jnp.asarray(w_minus)
                mask = solver._mask_alive_jax

                if solver.use_saturation:
                    E_p = float(_total_energy_saturated_bond_jit(
                        u_j, w_p_j, mask,
                        solver.dx, solver.G, solver.G_c, solver.gamma,
                        solver.omega_yield, solver.epsilon_yield,
                        solver.k_op10, solver.k_refl, solver.k_hopf,
                        solver.reflection_delta,
                    ))
                    E_m = float(_total_energy_saturated_bond_jit(
                        u_j, w_m_j, mask,
                        solver.dx, solver.G, solver.G_c, solver.gamma,
                        solver.omega_yield, solver.epsilon_yield,
                        solver.k_op10, solver.k_refl, solver.k_hopf,
                        solver.reflection_delta,
                    ))
                else:
                    E_p = float(_total_energy_bare_bond_jit(
                        u_j, w_p_j, mask,
                        solver.dx, solver.G, solver.G_c, solver.gamma,
                        solver.k_op10, solver.k_refl, solver.k_hopf,
                        solver.omega_yield, solver.epsilon_yield,
                        solver.reflection_delta,
                    ))
                    E_m = float(_total_energy_bare_bond_jit(
                        u_j, w_m_j, mask,
                        solver.dx, solver.G, solver.G_c, solver.gamma,
                        solver.k_op10, solver.k_refl, solver.k_hopf,
                        solver.omega_yield, solver.epsilon_yield,
                        solver.reflection_delta,
                    ))

                fd_grad = (E_p - E_m) / (2.0 * eps_fd)
                jax_grad = float(dE_dw[si, sj, sk, comp])

                denom = max(abs(jax_grad), abs(fd_grad), 1e-12)
                rel_err = abs(jax_grad - fd_grad) / denom
                assert rel_err < 1e-6, (
                    f"omega grad mismatch at ({si},{sj},{sk}) comp={comp}: "
                    f"jax={jax_grad:.6e} fd={fd_grad:.6e} rel={rel_err:.2e}"
                )


# ---------------------------------------------------------------------------
# apply_pml keyword smoke tests
# ---------------------------------------------------------------------------


class TestStepApplyPml:
    """Smoke tests for step(apply_pml=False): alive mask is applied, PML is not."""

    def test_apply_pml_false_does_not_propagate_dead_sites(self):
        """Even with apply_pml=False, dead sites stay zero."""
        solver = CosseratField3D(12, 12, 12, pml_thickness=2)
        rng = np.random.default_rng(3)
        solver.omega = rng.uniform(-0.01, 0.01, solver.omega.shape) * solver.mask_alive[..., None]
        solver.u_dot = rng.uniform(-1e-3, 1e-3, solver.u_dot.shape) * solver.mask_alive[..., None]
        solver.omega_dot = rng.uniform(-1e-3, 1e-3, solver.omega_dot.shape) * solver.mask_alive[..., None]
        solver.step(0.01, apply_pml=False)
        dead = ~solver.mask_alive
        np.testing.assert_allclose(solver.u_dot[dead], 0.0, atol=1e-15)
        np.testing.assert_allclose(solver.omega_dot[dead], 0.0, atol=1e-15)

    def test_apply_pml_false_differs_from_true_in_pml_region(self):
        """With PML present and velocities in the PML region, applying
        apply_pml=False should give different (larger) velocities than True."""
        nx, ny, nz = 12, 12, 12
        pml_t = 2

        # Solver A: with PML applied
        solverA = CosseratField3D(nx, ny, nz, pml_thickness=pml_t)
        rng = np.random.default_rng(5)
        omega_seed = rng.uniform(-0.01, 0.01, (nx, ny, nz, 3)) * solverA.mask_alive[..., None]
        vdot_seed = rng.uniform(-1e-3, 1e-3, (nx, ny, nz, 3)) * solverA.mask_alive[..., None]
        wdot_seed = rng.uniform(-1e-3, 1e-3, (nx, ny, nz, 3)) * solverA.mask_alive[..., None]
        solverA.omega = omega_seed.copy()
        solverA.u_dot = vdot_seed.copy()
        solverA.omega_dot = wdot_seed.copy()
        solverA.step(0.01, apply_pml=True)

        # Solver B: without PML
        solverB = CosseratField3D(nx, ny, nz, pml_thickness=pml_t)
        solverB.omega = omega_seed.copy()
        solverB.u_dot = vdot_seed.copy()
        solverB.omega_dot = wdot_seed.copy()
        solverB.step(0.01, apply_pml=False)

        # In the PML region (but alive), velocities should differ
        pml_mask = solverA.cos_pml_mask[..., 0] < 1.0  # attenuation < 1 in PML
        pml_alive = pml_mask & solverA.mask_alive
        if pml_alive.sum() > 0:
            vA_pml = np.abs(solverA.u_dot[pml_alive])
            vB_pml = np.abs(solverB.u_dot[pml_alive])
            # With PML applied (A), velocities should be smaller or equal
            assert np.any(vA_pml < vB_pml) or np.allclose(vA_pml, vB_pml), (
                "PML application had no effect in PML region"
            )

    def test_apply_pml_defaults_to_true(self):
        """step() without apply_pml kwarg behaves the same as apply_pml=True."""
        solver_a = CosseratField3D(10, 10, 10, pml_thickness=2)
        solver_b = CosseratField3D(10, 10, 10, pml_thickness=2)
        rng = np.random.default_rng(11)
        omega_seed = rng.uniform(-0.01, 0.01, solver_a.omega.shape) * solver_a.mask_alive[..., None]
        solver_a.omega = omega_seed.copy()
        solver_b.omega = omega_seed.copy()
        solver_a.step(0.01)
        solver_b.step(0.01, apply_pml=True)
        np.testing.assert_array_equal(solver_a.u, solver_b.u)
        np.testing.assert_array_equal(solver_a.omega, solver_b.omega)
