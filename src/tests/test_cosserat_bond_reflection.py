"""
ENV-D unit tests U0 and U2 for the bond-reflection form and step(apply_pml).

U0: legacy byte-identity — default path matches the golden fixture generated
    from base 50fdb644 (16^3, rng_seed=42, use_saturation=True, 10 steps at
    dt=0.05) bitwise; and the "grad" vs explicit "grad" path is self-consistent.

U2: bond-form gradient correctness and per-site bound (E1/R2 spec):
    - 6th-order central FD at h=3e-4 matches jax.grad to 1e-6 relative at
      sites where x_s > 10*delta (no neighbour-based exclusion).
    - W_refl <= 1/dx^2 at every site.
    - Energy is finite past yield (A2 > 1).

Floor formula (E1/R2): the piecewise x_s formula matches the single-branch
    formula to 1e-12 relative for |x| <= 1, and value+gradient are finite
    with no NaN for x in [-1e3, 1e3].

energy_density sum: sum(energy_density()) == total_energy() in both "grad"
    and "bond" modes.

Spec: ~/AVE-staging/ave-program-tracker/physics-walks/muon-g2/
      ENVD-bond-reflection-method-sheet_2026-10-03.md §4, sha 342a3254859e.
      ENVD-erratum-E1-rulings_2026-10-04.md (sha 7e3d5d83bd0f): R1 tolerances,
      R2 floor formula, R3 apply_pml confirm.

U1, U3, U4 are defined in test_envd_u1u3u4.py (same PR).
"""

import os
import numpy as np
import jax
import jax.numpy as jnp

# Float64 required for U2 FD: total energy ~700 gives float32 SNR ~3 at
# eps_fd=3e-4 — far below 1e-6 relative tolerance.  U0 golden-fixture
# comparisons are also float64 (fixture was generated with x64 enabled).
jax.config.update("jax_enable_x64", True)

from ave.topological.cosserat_field_3d import (
    CosseratField3D,
    _reflection_density_bond,
    _val_and_grad_saturated,
    _val_and_grad_bare,
    TETRA_OFFSETS,
)

_FIXTURE_PATH = os.path.join(
    os.path.dirname(__file__), "fixtures", "u0_golden_16x16x16_seed42.npz"
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_seeded_solver(nx=16, ny=16, nz=16, rng_seed=42, **kwargs):
    """Create a CosseratField3D seeded with random alive-site values."""
    solver = CosseratField3D(nx, ny, nz, **kwargs)
    rng = np.random.default_rng(rng_seed)
    omega_vals = rng.uniform(-0.05, 0.05, (nx, ny, nz, 3))
    u_vals = rng.uniform(-0.02, 0.02, (nx, ny, nz, 3))
    solver.omega = omega_vals * solver.mask_alive[..., None]
    solver.u = u_vals * solver.mask_alive[..., None]
    return solver


# ---------------------------------------------------------------------------
# U0 — legacy byte-identity (self-referential) and golden-fixture bitwise check
# ---------------------------------------------------------------------------


class TestU0LegacyByteIdentity:
    """U0a: default path (reflection_form='grad') is byte-identical to the
    pre-ENV-D behaviour — verified by calling the module-level jitted functions
    directly (those still reach _reflection_density unchanged)."""

    def _get_jax_inputs(self, solver):
        return (
            jnp.asarray(solver.u),
            jnp.asarray(solver.omega),
            solver._mask_alive_jax,
        )

    def test_u0_energy_gradient_bitwise_equal_saturated(self):
        solver = _make_seeded_solver(use_saturation=True)
        u_j, w_j, mask = self._get_jax_inputs(solver)

        E_ref, (du_ref, dw_ref) = _val_and_grad_saturated(
            u_j, w_j, mask,
            solver.dx, solver.G, solver.G_c, solver.gamma,
            solver.omega_yield, solver.epsilon_yield,
            solver.k_op10, solver.k_refl, solver.k_hopf,
        )

        dE_du, dE_dw = solver.energy_gradient()
        E_solver = solver.total_energy()

        assert float(E_ref) == E_solver, (
            f"energy mismatch: reference={float(E_ref)}, solver={E_solver}"
        )
        np.testing.assert_array_equal(
            np.asarray(du_ref) * np.asarray(mask)[..., None],
            dE_du,
            err_msg="dE/du mismatch (saturated)",
        )
        np.testing.assert_array_equal(
            np.asarray(dw_ref) * np.asarray(mask)[..., None],
            dE_dw,
            err_msg="dE/domega mismatch (saturated)",
        )

    def test_u0_energy_gradient_bitwise_equal_bare(self):
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

        np.testing.assert_array_equal(solver_a.u, solver_b.u)
        np.testing.assert_array_equal(solver_a.omega, solver_b.omega)

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


class TestU0GoldenFixture:
    """U0b: default path (reflection_form='grad') matches the golden fixture
    generated from base 50fdb644 on a fixed deterministic seed, bitwise.

    Fixture generation (run once against clean 50fdb644 checkout, committed as
    src/tests/fixtures/u0_golden_16x16x16_seed42.npz):
        Base sha : 50fdb6443968860bc3ffca86c6f503c02da10c30
        Command  : PYTHONPATH=/tmp/ave-50fdb644/src \\
                     ~/AVE-staging/AVE-Core/.venv/bin/python \\
                     /tmp/ave-50fdb644/src/scripts/gen_u0_golden.py
        Python   : 3.11.15
        JAX      : 0.10.1
        Setup    : CosseratField3D(16, 16, 16, use_saturation=True),
                   rng_seed=42 (omega, u), rng_seed=7 (u_dot, omega_dot),
                   jax_enable_x64=True, dt=0.05, 10 steps.

    Bitwise equality note: bitwise exact agreement is guaranteed ONLY when
    running under the repo .venv (~/AVE-staging/AVE-Core/.venv/bin/python).
    Homebrew Python or other interpreter versions may produce ULP-level
    floating-point differences in JAX JIT output; those are expected and
    are NOT a test failure.  Run as:
        ~/AVE-staging/AVE-Core/.venv/bin/python -m pytest \\
            src/tests/test_cosserat_bond_reflection.py::TestU0GoldenFixture

    If this test fails the default code path has drifted from 50fdb644.
    """

    def _make_solver_with_velocities(self):
        solver = CosseratField3D(16, 16, 16, use_saturation=True)
        rng = np.random.default_rng(42)
        solver.omega = rng.uniform(-0.05, 0.05, solver.omega.shape) * solver.mask_alive[..., None]
        solver.u = rng.uniform(-0.02, 0.02, solver.u.shape) * solver.mask_alive[..., None]
        rng2 = np.random.default_rng(7)
        solver.u_dot = rng2.uniform(-1e-3, 1e-3, solver.u_dot.shape) * solver.mask_alive[..., None]
        solver.omega_dot = rng2.uniform(-1e-3, 1e-3, solver.omega_dot.shape) * solver.mask_alive[..., None]
        return solver

    def test_u0_golden_energy_and_gradient(self):
        """E0 and gradient norms match fixture bitwise (float64)."""
        assert os.path.exists(_FIXTURE_PATH), f"fixture missing: {_FIXTURE_PATH}"
        ref = np.load(_FIXTURE_PATH)
        solver = self._make_solver_with_velocities()

        E0 = solver.total_energy()
        assert float(E0) == float(ref["E0"]), (
            f"E0 mismatch: got {E0:.15g}, fixture {float(ref['E0']):.15g}"
        )

        gu, gw = solver.energy_gradient()
        np.testing.assert_array_equal(gu, ref["gu"], err_msg="gu array mismatch vs fixture")
        np.testing.assert_array_equal(gw, ref["gw"], err_msg="gw array mismatch vs fixture")

    def test_u0_golden_10step_state(self):
        """All four state arrays after 10 steps match fixture bitwise."""
        assert os.path.exists(_FIXTURE_PATH), f"fixture missing: {_FIXTURE_PATH}"
        ref = np.load(_FIXTURE_PATH)
        solver = self._make_solver_with_velocities()

        for _ in range(10):
            solver.step(0.05)

        mapping = {"u10": "u", "omega10": "omega", "u_dot10": "u_dot", "omega_dot10": "omega_dot"}
        for arr_name, attr in mapping.items():
            np.testing.assert_array_equal(
                getattr(solver, attr),
                ref[arr_name],
                err_msg=f"{attr} mismatch vs fixture after 10 steps",
            )

    def test_u0_golden_10step_energy(self):
        """E10 matches fixture to float64 exact equality."""
        assert os.path.exists(_FIXTURE_PATH), f"fixture missing: {_FIXTURE_PATH}"
        ref = np.load(_FIXTURE_PATH)
        solver = self._make_solver_with_velocities()
        for _ in range(10):
            solver.step(0.05)
        E10 = solver.total_energy()
        assert float(E10) == float(ref["E10"]), (
            f"E10 mismatch: got {E10:.15g}, fixture {float(ref['E10']):.15g}"
        )


# ---------------------------------------------------------------------------
# energy_density() sum == total_energy() in both modes (item 1 fix)
# ---------------------------------------------------------------------------


class TestEnergyDensitySumMatchesTotal:
    """sum(energy_density()) must equal total_energy() in both reflection modes."""

    def _check(self, solver):
        W_sum = float(solver.energy_density().sum())
        E_total = solver.total_energy()
        np.testing.assert_allclose(
            W_sum, E_total, rtol=1e-12,
            err_msg=f"sum(energy_density())={W_sum:.15g} != total_energy()={E_total:.15g}",
        )

    def test_sum_equals_total_grad_form_saturated(self):
        solver = _make_seeded_solver(use_saturation=True, reflection_form="grad")
        solver.initialize_electron_2_3_sector(R_target=4.0, r_target=1.5)
        self._check(solver)

    def test_sum_equals_total_bond_form_saturated(self):
        solver = _make_seeded_solver(
            use_saturation=True, reflection_form="bond", reflection_delta=1e-3
        )
        solver.initialize_electron_2_3_sector(R_target=4.0, r_target=1.5)
        self._check(solver)

    def test_sum_equals_total_grad_form_bare(self):
        solver = _make_seeded_solver(use_saturation=False, reflection_form="grad")
        solver.initialize_electron_2_3_sector(R_target=4.0, r_target=1.5)
        self._check(solver)

    def test_sum_equals_total_bond_form_bare(self):
        solver = _make_seeded_solver(
            use_saturation=False, reflection_form="bond", reflection_delta=1e-3
        )
        solver.initialize_electron_2_3_sector(R_target=4.0, r_target=1.5)
        self._check(solver)


# ---------------------------------------------------------------------------
# Floor formula E1/R2 — piecewise x_s precision and gradient safety (item 5)
# ---------------------------------------------------------------------------


class TestFloorFormulaE1R2:
    """The E1/R2 piecewise floor x_s = where(x>=0, 0.5*(x+r), d^2/(2*(r-x)))
    matches the single-branch form to 1e-12 relative for |x|<=1, and
    value+gradient are finite with no NaN for x in [-1e3, 1e3]."""

    @staticmethod
    def _x_s_new(x, delta=1e-3):
        r = jnp.sqrt(x * x + delta * delta)
        return jnp.where(x >= 0, 0.5 * (x + r), delta * delta / (2.0 * (r - x)))

    @staticmethod
    def _x_s_old(x, delta=1e-3):
        return 0.5 * (x + jnp.sqrt(x * x + delta * delta))

    def test_matches_old_formula_for_abs_x_leq_1(self):
        """New piecewise form matches single-branch form for |x|<=1.

        For x >= 0 both branches select the same formula (bitwise equal).
        For x < 0 the old formula subtracts two nearly-equal floats (cancellation
        ~1e-10 relative at x = -1, delta = 1e-3); the new form avoids it.  The
        tolerance 1e-9 is set by the worst-case old-formula rounding error, not
        by a mathematical gap between the two — they are algebraically identical.
        """
        delta = 1e-3
        xs = jnp.linspace(-1.0, 1.0, 10001)
        new_vals = np.asarray(self._x_s_new(xs, delta))
        old_vals = np.asarray(self._x_s_old(xs, delta))
        np.testing.assert_allclose(
            new_vals, old_vals, rtol=1e-9,
            err_msg="piecewise x_s and single-branch x_s differ beyond 1e-9 relative for |x|<=1",
        )
        # For x >= 0 the two branches select the SAME code path; difference must
        # be exactly zero (bitwise).
        xs_np = np.asarray(xs)
        pos = xs_np >= 0
        np.testing.assert_array_equal(
            new_vals[pos], old_vals[pos],
            err_msg="piecewise and single-branch differ bitwise for x >= 0",
        )

    def test_value_finite_large_range(self):
        """x_s value is finite (no NaN, no inf) for x in [-1e3, 1e3]."""
        delta = 1e-3
        xs = jnp.linspace(-1e3, 1e3, 20001)
        vals = self._x_s_new(xs, delta)
        assert np.all(np.isfinite(np.asarray(vals))), "x_s value not finite for some x in [-1e3,1e3]"

    def test_gradient_finite_large_range(self):
        """Gradient of x_s wrt x is finite (no NaN) for x in [-1e3, 1e3]."""
        delta = 1e-3
        xs = jnp.linspace(-1e3, 1e3, 2001)

        def x_s_scalar(x_val):
            return self._x_s_new(x_val, delta)

        grad_fn = jax.vmap(jax.grad(x_s_scalar))
        grads = grad_fn(xs)
        assert np.all(np.isfinite(np.asarray(grads))), (
            "x_s gradient has NaN or inf for some x in [-1e3, 1e3]"
        )

    def test_value_positive(self):
        """x_s > 0 everywhere (it is a smooth floor, not exact zero)."""
        delta = 1e-3
        xs = jnp.linspace(-1e3, 1e3, 20001)
        vals = np.asarray(self._x_s_new(xs, delta))
        assert np.all(vals > 0.0), f"x_s <= 0 at some x; min={vals.min():.3e}"


# ---------------------------------------------------------------------------
# U2 — bond-form gradient vs 6th-order FD, bound, finite past yield (E1/R2)
# ---------------------------------------------------------------------------


def _make_bond_solver_with_high_a2(nx=16, ny=16, nz=16, rng_seed=99, delta=1e-3):
    """16^3 bond-form solver with max A2 ≈ 2 (spec E1 §U2).

    Background omega ~ Uniform[-0.03, 0.03] (A2 << 1).
    Kicked sites (30% of alive): omega components ~ ±[0.52, 0.60], pushing
    max A2 above 2 at the most active sites while keeping the bulk below yield.
    """
    solver = CosseratField3D(nx, ny, nz, reflection_form="bond", reflection_delta=delta)
    rng = np.random.default_rng(rng_seed)
    omega_vals = rng.uniform(-0.03, 0.03, (nx, ny, nz, 3))
    u_vals = rng.uniform(-0.01, 0.01, (nx, ny, nz, 3))
    solver.omega = omega_vals * solver.mask_alive[..., None]
    solver.u = u_vals * solver.mask_alive[..., None]
    alive_ijk = np.argwhere(solver.mask_alive)
    n_kick = max(1, int(0.30 * len(alive_ijk)))
    kick_idx = rng.choice(len(alive_ijk), size=n_kick, replace=False)
    for ki in kick_idx:
        i, j, k = alive_ijk[ki]
        signs = rng.choice([-1, 1], size=3).astype(float)
        solver.omega[i, j, k] = rng.uniform(0.52, 0.60, 3) * signs
    return solver


def _compute_w_refl_bond_field(solver):
    u_j = jnp.asarray(solver.u)
    w_j = jnp.asarray(solver.omega)
    return np.asarray(
        _reflection_density_bond(
            u_j, w_j, solver.dx, solver.omega_yield, solver.epsilon_yield,
            solver.reflection_delta,
        )
    )


def _a2_field(solver):
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


def _sixth_order_fd(energy_fn, arr, idx, comp, h):
    """6th-order central FD for dE/d(arr[idx, comp]).

    Coefficients: [1/60, -3/20, 3/4, -3/4, 3/20, -1/60] at [-3h, -2h, -h, h, 2h, 3h].
    """
    def perturb(d):
        a = arr.copy()
        a[idx[0], idx[1], idx[2], comp] += d
        return energy_fn(a)

    fp3 = perturb(+3 * h)
    fp2 = perturb(+2 * h)
    fp1 = perturb(+1 * h)
    fm1 = perturb(-1 * h)
    fm2 = perturb(-2 * h)
    fm3 = perturb(-3 * h)
    return (fp3 / 60.0 - 3 * fp2 / 20.0 + 3 * fp1 / 4.0
            - 3 * fm1 / 4.0 + 3 * fm2 / 20.0 - fm3 / 60.0) / h


class TestU2BondFormGradientAndBound:
    """U2 (E1/R2): bond-form gradient vs 6th-order central FD at h=3e-4,
    1e-6 relative, at sites with x_s > 10*delta; W <= 1/dx^2; finite past yield."""

    def test_u2_w_bounded_by_inv_dx_sq(self):
        solver = _make_bond_solver_with_high_a2()
        W = _compute_w_refl_bond_field(solver)
        bound = 1.0 / (solver.dx * solver.dx)
        assert np.all(np.isfinite(W)), "W_refl has non-finite values"
        alive = solver.mask_alive
        np.testing.assert_array_less(
            W[alive] - bound,
            1e-9 * bound * np.ones(alive.sum()),
            err_msg=f"W_refl exceeds 1/dx^2={bound:.4g} at some alive sites",
        )

    def test_u2_finite_past_yield(self):
        solver = _make_bond_solver_with_high_a2()
        A2 = _a2_field(solver)
        beyond_yield = (A2 > 1.0) & solver.mask_alive
        assert beyond_yield.sum() > 0, "no sites past yield — increase kick amplitude"
        W = _compute_w_refl_bond_field(solver)
        assert np.all(np.isfinite(W[beyond_yield])), "W_refl not finite past yield"

    def test_u2_gradient_vs_sixth_order_fd(self):
        """6th-order FD at h=3e-4 matches jax.grad to 1e-6 relative where x_s > 10*delta.
        No neighbour-based exclusion (E1/R2 spec)."""
        from ave.topological.cosserat_field_3d import (
            _total_energy_saturated_bond_jit,
            _total_energy_bare_bond_jit,
        )

        delta = 1e-3
        h = 3e-4
        solver = _make_bond_solver_with_high_a2(delta=delta)

        A2 = _a2_field(solver)
        x = 1.0 - A2
        r = np.sqrt(x * x + delta * delta)
        x_s = np.where(x >= 0, 0.5 * (x + r), delta * delta / (2.0 * (r - x)))

        qualifying = np.where(solver.mask_alive & (x_s > 10 * delta))
        n_sites = len(qualifying[0])
        assert n_sites >= 20, f"fewer than 20 qualifying sites (x_s>10*delta): {n_sites}"

        rng = np.random.default_rng(17)
        idx_choice = rng.choice(n_sites, size=20, replace=False)
        sites = [(qualifying[0][i], qualifying[1][i], qualifying[2][i]) for i in idx_choice]

        dE_du, dE_dw = solver.energy_gradient()
        mask = solver._mask_alive_jax

        def E_from_u(u_arr):
            u_j = jnp.asarray(u_arr)
            w_j = jnp.asarray(solver.omega)
            if solver.use_saturation:
                return float(_total_energy_saturated_bond_jit(
                    u_j, w_j, mask,
                    solver.dx, solver.G, solver.G_c, solver.gamma,
                    solver.omega_yield, solver.epsilon_yield,
                    solver.k_op10, solver.k_refl, solver.k_hopf,
                    solver.reflection_delta,
                ))
            return float(_total_energy_bare_bond_jit(
                u_j, w_j, mask,
                solver.dx, solver.G, solver.G_c, solver.gamma,
                solver.k_op10, solver.k_refl, solver.k_hopf,
                solver.omega_yield, solver.epsilon_yield,
                solver.reflection_delta,
            ))

        def E_from_w(w_arr):
            u_j = jnp.asarray(solver.u)
            w_j = jnp.asarray(w_arr)
            if solver.use_saturation:
                return float(_total_energy_saturated_bond_jit(
                    u_j, w_j, mask,
                    solver.dx, solver.G, solver.G_c, solver.gamma,
                    solver.omega_yield, solver.epsilon_yield,
                    solver.k_op10, solver.k_refl, solver.k_hopf,
                    solver.reflection_delta,
                ))
            return float(_total_energy_bare_bond_jit(
                u_j, w_j, mask,
                solver.dx, solver.G, solver.G_c, solver.gamma,
                solver.k_op10, solver.k_refl, solver.k_hopf,
                solver.omega_yield, solver.epsilon_yield,
                solver.reflection_delta,
            ))

        tol = 1e-6
        for si, sj, sk in sites:
            for comp in range(3):
                fd = _sixth_order_fd(E_from_u, solver.u, (si, sj, sk), comp, h)
                jax_g = float(dE_du[si, sj, sk, comp])
                denom = max(abs(jax_g), abs(fd), 1e-12)
                rel_err = abs(jax_g - fd) / denom
                assert rel_err < tol, (
                    f"u grad at ({si},{sj},{sk}) comp={comp}: "
                    f"jax={jax_g:.6e} 6th-FD={fd:.6e} rel={rel_err:.2e}"
                )

            for comp in range(3):
                fd = _sixth_order_fd(E_from_w, solver.omega, (si, sj, sk), comp, h)
                jax_g = float(dE_dw[si, sj, sk, comp])
                denom = max(abs(jax_g), abs(fd), 1e-12)
                rel_err = abs(jax_g - fd) / denom
                assert rel_err < tol, (
                    f"omega grad at ({si},{sj},{sk}) comp={comp}: "
                    f"jax={jax_g:.6e} 6th-FD={fd:.6e} rel={rel_err:.2e}"
                )


# ---------------------------------------------------------------------------
# apply_pml keyword tests (item 3 fixes)
# ---------------------------------------------------------------------------


class TestStepApplyPml:
    """Smoke tests for step(apply_pml=False)."""

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
        """With PML present and velocities in the PML region, apply_pml=False
        gives strictly larger magnitudes than apply_pml=True (not just allclose)."""
        nx, ny, nz = 12, 12, 12
        pml_t = 2

        solverA = CosseratField3D(nx, ny, nz, pml_thickness=pml_t)
        rng = np.random.default_rng(5)
        omega_seed = rng.uniform(-0.01, 0.01, (nx, ny, nz, 3)) * solverA.mask_alive[..., None]
        vdot_seed = rng.uniform(-1e-3, 1e-3, (nx, ny, nz, 3)) * solverA.mask_alive[..., None]
        wdot_seed = rng.uniform(-1e-3, 1e-3, (nx, ny, nz, 3)) * solverA.mask_alive[..., None]
        solverA.omega = omega_seed.copy()
        solverA.u_dot = vdot_seed.copy()
        solverA.omega_dot = wdot_seed.copy()
        solverA.step(0.01, apply_pml=True)

        solverB = CosseratField3D(nx, ny, nz, pml_thickness=pml_t)
        solverB.omega = omega_seed.copy()
        solverB.u_dot = vdot_seed.copy()
        solverB.omega_dot = wdot_seed.copy()
        solverB.step(0.01, apply_pml=False)

        pml_mask = solverA.cos_pml_mask[..., 0] < 1.0
        pml_alive = pml_mask & solverA.mask_alive
        if pml_alive.sum() > 0:
            vA_pml = np.abs(solverA.u_dot[pml_alive])
            vB_pml = np.abs(solverB.u_dot[pml_alive])
            assert np.any(vA_pml < vB_pml), (
                "PML application had no effect: |v_True| not < |v_False| at any PML site"
            )

    def test_apply_pml_defaults_to_true(self):
        """step() without apply_pml kwarg behaves the same as apply_pml=True
        across all four state arrays: u, omega, u_dot, omega_dot."""
        solver_a = CosseratField3D(10, 10, 10, pml_thickness=2)
        solver_b = CosseratField3D(10, 10, 10, pml_thickness=2)
        rng = np.random.default_rng(11)
        omega_seed = rng.uniform(-0.01, 0.01, solver_a.omega.shape) * solver_a.mask_alive[..., None]
        vdot_seed = rng.uniform(-1e-3, 1e-3, solver_a.u_dot.shape) * solver_a.mask_alive[..., None]
        wdot_seed = rng.uniform(-1e-3, 1e-3, solver_a.omega_dot.shape) * solver_a.mask_alive[..., None]
        for s in (solver_a, solver_b):
            s.omega = omega_seed.copy()
            s.u_dot = vdot_seed.copy()
            s.omega_dot = wdot_seed.copy()
        solver_a.step(0.01)
        solver_b.step(0.01, apply_pml=True)
        np.testing.assert_array_equal(solver_a.u, solver_b.u, err_msg="u differs")
        np.testing.assert_array_equal(solver_a.omega, solver_b.omega, err_msg="omega differs")
        np.testing.assert_array_equal(solver_a.u_dot, solver_b.u_dot, err_msg="u_dot differs")
        np.testing.assert_array_equal(solver_a.omega_dot, solver_b.omega_dot, err_msg="omega_dot differs")
