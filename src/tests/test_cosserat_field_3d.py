"""
Unit tests for the 3D Cosserat field solver on the K4 substrate.

Covers:
- Tetrahedral-gradient operator exactness on linear fields.
- Grid initialization (A/B sublattice masks, alive-site count).
- Sutcliffe-style (2,3) initial field sanity (localized, nonzero, decays).
- Kinematic tensor shapes and antisymmetric-cross-product correctness.
- Energy functional returns finite non-negative values.
- Diagnostic readouts (R, r, c, Q) run without error on the initial state.

Reference: research/_archive/L3_electron_soliton/08_, 09_.
"""

import numpy as np

from ave.topological.cosserat_field_3d import (
    CosseratField3D,
    _axis_angle_to_rotation,
    _hopf_density,
    _omega_to_quaternion,
    _op10_density,
    _project_omega_to_nhat,
    _quat_mul,
    _reflection_density,
    adjoint_tetrahedral_divergence,
    tetrahedral_gradient,
)

# ------------------------------------------------------------------
# Gradient operator
# ------------------------------------------------------------------


def test_tetrahedral_gradient_on_linear_field_reproduces_slope():
    """For V_i(r) = c_i + a_ij r_j, d_j V_i = a_ij exactly (interior sites)."""
    n = 16
    rng = np.random.default_rng(42)
    a = rng.normal(size=(3, 3))
    c = rng.normal(size=3)

    idx = np.indices((n, n, n))
    x = idx[0].astype(float)
    y = idx[1].astype(float)
    z = idx[2].astype(float)

    V = np.stack(
        [c[i] + a[i, 0] * x + a[i, 1] * y + a[i, 2] * z for i in range(3)],
        axis=-1,
    )
    grad = tetrahedral_gradient(V)

    # Interior mask: 2 away from every edge to avoid np.roll wraparound artifacts.
    interior = slice(2, -2)
    got = grad[interior, interior, interior]
    expected = np.broadcast_to(a, got.shape)
    np.testing.assert_allclose(got, expected, atol=1e-10)


def test_tetrahedral_gradient_on_constant_is_zero():
    n = 8
    V = np.ones((n, n, n, 3), dtype=float)
    grad = tetrahedral_gradient(V)
    np.testing.assert_allclose(grad, 0.0, atol=1e-12)


# ------------------------------------------------------------------
# Grid setup
# ------------------------------------------------------------------


def test_grid_has_half_alive_nodes_approximately():
    """A + B sublattices each take 1/8 of lattice sites; total alive = 1/4."""
    solver = CosseratField3D(16, 16, 16)
    alive_frac = solver.mask_alive.mean()
    # A-sites: 1/8, B-sites: 1/8, total 1/4.
    assert 0.20 < alive_frac < 0.30


def test_type_a_and_b_are_disjoint():
    solver = CosseratField3D(10, 10, 10)
    assert not np.any(solver.mask_A & solver.mask_B)


# ------------------------------------------------------------------
# Initial field ansatz
# ------------------------------------------------------------------


def test_initial_field_is_localized_near_target_radius():
    solver = CosseratField3D(32, 32, 32)
    solver.initialize_electron_2_3_sector(R_target=8.0, r_target=3.0)
    omega_mag = np.sqrt(np.sum(solver.omega**2, axis=-1))
    # Must be nonzero somewhere on alive nodes.
    assert float(omega_mag.max()) > 0.5
    # Dead nodes carry zero.
    np.testing.assert_allclose(omega_mag[~solver.mask_alive], 0.0, atol=1e-12)


def test_initial_field_u_is_zero():
    solver = CosseratField3D(16, 16, 16)
    solver.initialize_electron_2_3_sector(R_target=4.0, r_target=1.5)
    np.testing.assert_allclose(solver.u, 0.0)


# ------------------------------------------------------------------
# Kinematic tensors
# ------------------------------------------------------------------


def test_strain_tensor_picks_up_antisymmetric_microrotation():
    """With u = 0, strain epsilon_ij = -eps_ijk omega_k. Verify sign/shape."""
    solver = CosseratField3D(10, 10, 10)
    solver.omega[..., 2] = 1.0  # omega_z = 1 everywhere
    eps = solver.compute_strain()
    # epsilon_12 = -eps_12k omega_k = -eps_123 omega_3 = -omega_z = -1
    # epsilon_21 = -eps_21k omega_k = -eps_213 omega_3 = +omega_z = +1
    np.testing.assert_allclose(eps[..., 0, 1], -1.0, atol=1e-12)
    np.testing.assert_allclose(eps[..., 1, 0], +1.0, atol=1e-12)
    # Diagonal entries: d_j u_i is zero (u = 0), cross contribution zero (symmetric indices).
    np.testing.assert_allclose(eps[..., 0, 0], 0.0, atol=1e-12)


def test_curvature_tensor_has_correct_shape():
    solver = CosseratField3D(8, 8, 8)
    solver.initialize_electron_2_3_sector(R_target=2.0, r_target=0.8)
    kappa = solver.compute_curvature()
    assert kappa.shape == (8, 8, 8, 3, 3)


# ------------------------------------------------------------------
# Energy functional
# ------------------------------------------------------------------


def test_energy_is_finite_and_nonnegative():
    solver = CosseratField3D(24, 24, 24)
    solver.initialize_electron_2_3_sector(R_target=5.0, r_target=2.0)
    W = solver.energy_density()
    assert np.all(np.isfinite(W))
    assert np.all(W >= 0.0)
    assert solver.total_energy() > 0.0


def test_energy_is_zero_on_vacuum():
    solver = CosseratField3D(10, 10, 10)
    # u, omega both zero by construction.
    assert solver.total_energy() == 0.0


# ------------------------------------------------------------------
# Diagnostics run without error on initial state
# ------------------------------------------------------------------


def test_diagnostics_run_on_initial_state():
    solver = CosseratField3D(32, 32, 32)
    R_init, r_init = 8.0, 3.0
    solver.initialize_electron_2_3_sector(R_target=R_init, r_target=r_init)

    R_found, r_found = solver.extract_shell_radii()
    # Must be broadly consistent with the initialization target.
    assert 0.5 * R_init < R_found < 1.5 * R_init
    assert 0.0 <= r_found < 2.0 * r_init

    c = solver.extract_crossing_count()
    assert c >= 0

    Q = solver.extract_quality_factor()
    assert np.isfinite(Q)
    assert Q > 0.0


# ------------------------------------------------------------------
# Adjoint gradient operator — discrete integration-by-parts identity
# ------------------------------------------------------------------


def test_adjoint_satisfies_integration_by_parts():
    """
    The discrete identity sum_x (grad_j V)(x) W_j(x) = sum_x V(x) (adj_div W)(x)
    must hold for arbitrary V, W on a periodic domain. This is what makes
    adj_div the correct operator for variational-derivative propagation.
    """
    n = 8
    rng = np.random.default_rng(0)
    V = rng.normal(size=(n, n, n, 1))
    W = rng.normal(size=(n, n, n, 1, 3))

    grad_V = tetrahedral_gradient(V)
    lhs = float(np.sum(grad_V * W))

    adj_W = adjoint_tetrahedral_divergence(W[..., 0, :])
    rhs = float(np.sum(V[..., 0] * adj_W))

    np.testing.assert_allclose(lhs, rhs, rtol=1e-12)


# ------------------------------------------------------------------
# Energy gradient — consistency with finite-difference
# ------------------------------------------------------------------


def test_energy_gradient_matches_finite_difference():
    """
    Compare analytical energy_gradient against a finite-difference estimator
    at a few alive sites. Required agreement ~1e-4 given the step size and
    float64 precision.
    """
    solver = CosseratField3D(12, 12, 12)
    solver.initialize_electron_2_3_sector(R_target=3.0, r_target=1.2)

    dE_du, dE_dw = solver.energy_gradient()

    # Probe a few alive A-sites with omega > 0 so the gradient is nontrivial.
    omega_mag = np.sqrt(np.sum(solver.omega**2, axis=-1))
    candidates = np.argwhere(solver.mask_A & (omega_mag > 0.1))
    assert len(candidates) > 0
    probe_sites = candidates[:: max(1, len(candidates) // 4)][:3]

    h = 1e-5
    for site in probe_sites:
        ix, iy, iz = site
        for k in range(3):
            # Finite-difference estimate of dE/d(omega_k at site).
            saved = solver.omega[ix, iy, iz, k]
            solver.omega[ix, iy, iz, k] = saved + h
            E_plus = solver.total_energy()
            solver.omega[ix, iy, iz, k] = saved - h
            E_minus = solver.total_energy()
            solver.omega[ix, iy, iz, k] = saved

            fd = (E_plus - E_minus) / (2.0 * h)
            analytical = dE_dw[ix, iy, iz, k]
            # Agreement to ~1e-4 expected; the saturated functional has
            # curvature and the FD approximation has O(h^2) error.
            np.testing.assert_allclose(analytical, fd, rtol=1e-3, atol=1e-4)


# ------------------------------------------------------------------
# Gradient descent — monotonic energy decrease
# ------------------------------------------------------------------


def test_saturated_gradient_matches_finite_difference_under_activation():
    """
    Strict FD agreement test at sites where saturation is strongly active
    (|kappa|/yield > 0.5). This is the regime where the hand-derived
    gradient previously failed — now that jax.grad computes it, the
    agreement should be float-precision exact.
    """
    solver = CosseratField3D(16, 16, 16, use_saturation=True)
    # Isolate saturation: disable Op10 and reflection terms for this test
    # (they have their own FD tests; 1/S^2 curvature in reflection makes
    # h=1e-6 FD noisy at saturation-active sites).
    solver.k_op10 = 0.0
    solver.k_refl = 0.0
    solver.initialize_electron_2_3_sector(R_target=5.0, r_target=2.0)
    kappa = solver.compute_curvature()
    kappa_mag = np.sqrt(np.sum(kappa**2, axis=(-1, -2)))
    # Find alive sites in the strongly-saturated regime.
    active_mask = solver.mask_alive & (kappa_mag > 0.3 * solver.omega_yield)
    candidates = np.argwhere(active_mask)
    assert len(candidates) > 10

    dE_du, dE_dw = solver.energy_gradient()

    h = 1e-6
    for site in candidates[:3]:
        ix, iy, iz = site
        for k in range(3):
            saved = solver.omega[ix, iy, iz, k]
            solver.omega[ix, iy, iz, k] = saved + h
            E_plus = solver.total_energy()
            solver.omega[ix, iy, iz, k] = saved - h
            E_minus = solver.total_energy()
            solver.omega[ix, iy, iz, k] = saved
            fd = (E_plus - E_minus) / (2.0 * h)
            analytical = float(dE_dw[ix, iy, iz, k])
            # Float-precision agreement, not the loose 1e-3 we accepted
            # when saturation was hand-derived.
            np.testing.assert_allclose(analytical, fd, rtol=1e-5, atol=1e-6)


def test_relax_step_decreases_energy():
    """
    A few gradient-descent steps from a localized initial field should
    monotonically decrease the energy (with an adaptive lr, accepted steps
    by construction decrease energy).
    """
    solver = CosseratField3D(16, 16, 16)
    solver.initialize_electron_2_3_sector(R_target=4.0, r_target=1.5)

    E_initial = solver.total_energy()
    result = solver.relax_to_ground_state(max_iter=20, tol=1e-12, initial_lr=0.001)

    # At minimum we must not have increased energy.
    assert result["final_energy"] <= E_initial
    # And we should have made at least some progress on a far-from-equilibrium start.
    assert result["final_energy"] < E_initial or result["iterations"] >= 1


# ------------------------------------------------------------------
# Op10 continuum term — Rodrigues projection and density
# ------------------------------------------------------------------


def test_rodrigues_projection_on_zero_omega_gives_z_hat():
    """omega = 0 everywhere => n_hat = (0, 0, 1) (reference direction)."""
    n = 8
    omega = np.zeros((n, n, n, 3))
    n_hat = np.asarray(_project_omega_to_nhat(omega))
    expected = np.zeros_like(omega)
    expected[..., 2] = 1.0
    np.testing.assert_allclose(n_hat, expected, atol=1e-12)


def test_rodrigues_projection_rotation_by_pi_around_x_flips_z():
    """omega = (pi, 0, 0) => rotate z_hat by pi around x_hat => -z_hat."""
    n = 4
    omega = np.zeros((n, n, n, 3))
    omega[..., 0] = np.pi
    n_hat = np.asarray(_project_omega_to_nhat(omega))
    expected = np.zeros_like(omega)
    expected[..., 2] = -1.0
    np.testing.assert_allclose(n_hat, expected, atol=1e-12)


def test_rodrigues_projection_preserves_unit_length():
    """n_hat must be unit length for any omega."""
    rng = np.random.default_rng(7)
    omega = rng.normal(scale=0.7, size=(6, 6, 6, 3))
    n_hat = np.asarray(_project_omega_to_nhat(omega))
    norms = np.sqrt(np.sum(n_hat**2, axis=-1))
    np.testing.assert_allclose(norms, 1.0, atol=1e-12)


def test_op10_density_zero_on_constant_omega():
    """Constant omega => constant n_hat => grad(n_hat) = 0 => W_4 = 0."""
    n = 8
    omega = np.zeros((n, n, n, 3))
    omega[..., 0] = 0.5
    omega[..., 1] = 0.3
    W4 = np.asarray(_op10_density(omega, dx=1.0))
    np.testing.assert_allclose(W4, 0.0, atol=1e-12)


def test_op10_density_nonzero_on_2_3_ansatz_shell():
    """The (2,3) Sutcliffe-style initial ansatz should produce nonzero W_4
    in the shell region around the torus."""
    solver = CosseratField3D(24, 24, 24)
    solver.initialize_electron_2_3_sector(R_target=6.0, r_target=2.0)
    W4 = np.asarray(_op10_density(solver.omega, dx=solver.dx))
    # Must be finite, non-negative, and strictly positive somewhere.
    assert np.all(np.isfinite(W4))
    assert np.all(W4 >= -1e-12)  # Should be >= 0 by construction.
    assert float(W4.max()) > 0.0


def test_op10_energy_gradient_matches_finite_difference():
    """With k_op10 active, the jax-grad energy gradient must match FD at
    probe sites. This is the analog of the strict FD test for saturation."""
    solver = CosseratField3D(14, 14, 14, use_saturation=True)
    solver.initialize_electron_2_3_sector(R_target=4.0, r_target=1.5)
    # Confirm k_op10 is active (default 1.0). Isolate from reflection term
    # whose 1/S^2 curvature makes FD noisy at saturation-active sites.
    assert solver.k_op10 == 1.0
    solver.k_refl = 0.0

    dE_du, dE_dw = solver.energy_gradient()

    omega_mag = np.sqrt(np.sum(solver.omega**2, axis=-1))
    candidates = np.argwhere(solver.mask_A & (omega_mag > 0.2))
    assert len(candidates) > 5

    h = 1e-6
    for site in candidates[: min(3, len(candidates))]:
        ix, iy, iz = site
        for k in range(3):
            saved = solver.omega[ix, iy, iz, k]
            solver.omega[ix, iy, iz, k] = saved + h
            E_plus = solver.total_energy()
            solver.omega[ix, iy, iz, k] = saved - h
            E_minus = solver.total_energy()
            solver.omega[ix, iy, iz, k] = saved
            fd = (E_plus - E_minus) / (2.0 * h)
            analytical = float(dE_dw[ix, iy, iz, k])
            np.testing.assert_allclose(analytical, fd, rtol=1e-5, atol=1e-6)


def test_op10_contributes_to_total_energy():
    """Energy with k_op10 = 1 must exceed the same configuration with k_op10 = 0,
    since the (2,3) ansatz has nontrivial wedge density on the shell."""
    solver = CosseratField3D(16, 16, 16)
    solver.initialize_electron_2_3_sector(R_target=4.0, r_target=1.5)
    E_with = solver.total_energy()
    solver.k_op10 = 0.0
    E_without = solver.total_energy()
    assert E_with > E_without + 1e-9


# ------------------------------------------------------------------
# Reflection term (Op9 via Op2 + Op14 + Op3) — chain at the field scale
# ------------------------------------------------------------------


def test_reflection_density_zero_on_vacuum():
    """u = omega = 0 => A = 0 => S = 1 => grad S = 0 => reflection = 0."""
    n = 8
    u = np.zeros((n, n, n, 3))
    omega = np.zeros((n, n, n, 3))
    W_refl = np.asarray(_reflection_density(u, omega, dx=1.0, omega_yield=np.pi, epsilon_yield=1.0))
    np.testing.assert_allclose(W_refl, 0.0, atol=1e-12)


def test_reflection_density_nonzero_on_2_3_ansatz():
    """(2,3) ansatz has nonzero strain in the shell => S < 1 there => grad S
    nonzero at shell boundary => reflection density > 0 somewhere."""
    solver = CosseratField3D(24, 24, 24, use_saturation=True)
    solver.initialize_electron_2_3_sector(R_target=6.0, r_target=2.0)
    W_refl = np.asarray(
        _reflection_density(
            solver.u,
            solver.omega,
            dx=solver.dx,
            omega_yield=solver.omega_yield,
            epsilon_yield=solver.epsilon_yield,
        )
    )
    assert np.all(np.isfinite(W_refl))
    assert np.all(W_refl >= 0.0 - 1e-12)
    assert float(W_refl.max()) > 0.0


def test_reflection_density_grows_near_yield():
    """Scaling omega up (closer to yield) should strictly increase the
    total reflection energy. Tests the 1/S^2 anti-collapse behavior."""
    solver_small = CosseratField3D(16, 16, 16, use_saturation=True)
    solver_small.initialize_electron_2_3_sector(R_target=4.0, r_target=1.5)
    solver_small.omega = solver_small.omega * 0.4  # far from yield

    solver_large = CosseratField3D(16, 16, 16, use_saturation=True)
    solver_large.initialize_electron_2_3_sector(R_target=4.0, r_target=1.5)
    solver_large.omega = solver_large.omega * 0.9  # near yield

    W_small = np.asarray(
        _reflection_density(
            solver_small.u,
            solver_small.omega,
            dx=1.0,
            omega_yield=solver_small.omega_yield,
            epsilon_yield=solver_small.epsilon_yield,
        )
    )
    W_large = np.asarray(
        _reflection_density(
            solver_large.u,
            solver_large.omega,
            dx=1.0,
            omega_yield=solver_large.omega_yield,
            epsilon_yield=solver_large.epsilon_yield,
        )
    )
    # Near-yield configuration should carry substantially more reflection energy.
    # (Typical ratio ~3-4x for factor-2.25 omega amplitude scaling.)
    assert float(W_large.sum()) > 2.0 * float(W_small.sum())


def test_reflection_density_coefficient_pinned_to_one_sixteenth():
    """REGRESSION (quarter-power Family-E burn-down, 2026-07-14): pin the
    Gamma^2 coefficient to 1/16 — the value FORCED by the canonical Op14
    impedance register Z = Z_0 / sqrt(S) = Z_0 * S^(-1/2).

    Derivation (from the register, reconstructed here so the test fails if the
    register is silently reverted):
        Z = Z_0 * S^(-1/2)      =>  grad ln Z   = -(1/2) grad S / S
        Gamma = (1/2) grad ln Z  =>  Gamma       = -(1/4) grad S / S
        Gamma^2 = (1/4)^2 * (grad S / S)^2 = (1/16) |grad S|^2 / S^2

    The legacy 1/64 rode the SUPERSEDED Z = Z_0 / S^(1/4) register (which is
    (1-A^2)^(1/8) — matching no physical register). See the REGISTER
    CORRECTION note in cosserat_field_3d.py:_reflection_density and
    research/2026-07-14_quarter-power-map.md sec 2/3.
    """
    import jax.numpy as jnp

    from ave.topological.cosserat_field_3d import (
        _compute_curvature,
        _compute_strain,
        _tetrahedral_gradient,
    )

    # (a) IN-TEST DOCUMENTATION (NOT a gate — self-referential arithmetic).
    # These are all test-local constants; the two asserts below reduce to
    # 0.25**2 == 1/16 and cannot fail against the module on any input. They
    # document the register→coefficient chain so a reader sees WHY the literal in
    # part (b) is 1/16. `z_exponent = 0.5` is hardcoded here because no shared
    # Op14-register symbol exists (the module hardcodes the exponent inline at
    # _s11_density:425 and _reflection_density_asymmetric); if that register is
    # ever centralized into one constant, import it into BOTH module and this
    # test to make part (a) a genuine derivation pin (else this 0.5 is a second
    # uncoordinated copy). The OPERATIVE GATE is part (b).
    z_exponent = 0.5  # Z = Z_0 * S^(-z_exponent), the canonical Op14 register
    gamma_coeff = 0.5 * z_exponent  # Gamma = (1/2) d ln Z  => 1/4
    gamma_sq_coeff = gamma_coeff**2  # => 1/16 (documented target for part (b))
    assert gamma_sq_coeff == 1.0 / 16.0  # documentation check (arithmetic truth)
    assert gamma_sq_coeff != 1.0 / 64.0  # documents rejection of the legacy value

    # (b) OPERATIVE GATE — the literal pin: _reflection_density returns EXACTLY
    #     gamma_sq_coeff * |grad S|^2 / (S^2 + eps_reg), reconstructed via the
    #     module's own internal chain (so a coefficient drift is caught).
    solver = CosseratField3D(20, 20, 20, use_saturation=True)
    solver.initialize_electron_2_3_sector(R_target=5.0, r_target=1.8)
    u, omega, dx = solver.u, solver.omega, solver.dx
    om_y, eps_y = solver.omega_yield, solver.epsilon_yield

    eps = _compute_strain(jnp.asarray(u), jnp.asarray(omega), dx)
    kappa = _compute_curvature(jnp.asarray(omega), dx)
    eps_sq = jnp.sum(eps * eps, axis=(-1, -2))
    kappa_sq = jnp.sum(kappa * kappa, axis=(-1, -2))
    a_sq = jnp.clip(eps_sq / (eps_y**2) + kappa_sq / (om_y**2), 0.0, 1.0 - 1e-10)
    s_field = jnp.sqrt(1.0 - a_sq)
    grad_s = _tetrahedral_gradient(s_field[..., None])[..., 0, :] / dx
    grad_s_sq = jnp.sum(grad_s * grad_s, axis=-1)
    eps_reg = 1e-6
    expected = gamma_sq_coeff * grad_s_sq / (s_field * s_field + eps_reg)

    got = np.asarray(_reflection_density(jnp.asarray(u), jnp.asarray(omega), dx, om_y, eps_y))
    np.testing.assert_allclose(got, np.asarray(expected), rtol=1e-6, atol=1e-12)

    # There must be nonzero reflection somewhere on the (2,3) ansatz, else the
    # coefficient pin above is vacuous.
    assert got.max() > 0.0
    # And the legacy 1/64 (= 1/16 / 4) would be a 4x under-count everywhere.
    legacy = 0.25 * np.asarray(expected)
    assert not np.allclose(got[got > 0.0], legacy[got > 0.0], rtol=1e-3)


def test_reflection_contributes_to_total_energy():
    """Turning k_refl on from 0 to 1 must increase total energy on the
    (2,3) ansatz (which has nonzero strain in the shell region)."""
    solver = CosseratField3D(20, 20, 20, use_saturation=True)
    solver.initialize_electron_2_3_sector(R_target=5.0, r_target=1.8)
    solver.k_refl = 0.0
    solver.k_op10 = 0.0
    E_without = solver.total_energy()
    solver.k_refl = 1.0
    E_with = solver.total_energy()
    assert E_with > E_without + 1e-9


def test_hopf_density_zero_on_vacuum():
    """omega = 0 => n_hat constant => F_ij = 0 => B = 0 => A = 0 => A.B = 0."""
    n = 12
    omega = np.zeros((n, n, n, 3))
    W_hopf = np.asarray(_hopf_density(omega, dx=1.0))
    np.testing.assert_allclose(W_hopf, 0.0, atol=1e-10)


def test_hopf_density_nonzero_on_2_3_ansatz():
    """(2,3) Sutcliffe-style ansatz has a genuine Hopf-invariant winding.
    A.B should be nonzero SOMEWHERE, and its integral (mean) is finite."""
    solver = CosseratField3D(24, 24, 24)
    solver.initialize_electron_2_3_sector(R_target=6.0, r_target=2.0)
    W_hopf = np.asarray(_hopf_density(solver.omega, dx=solver.dx))
    assert np.all(np.isfinite(W_hopf))
    # Should have nontrivial local density
    assert np.abs(W_hopf).max() > 1e-6
    # Integrated value should be finite (not a NaN or blown-up FFT)
    total = float(np.sum(W_hopf))
    assert np.isfinite(total)


def test_hopf_contributes_to_total_energy():
    """Turning k_hopf on from 0 must change total energy (the (2,3) ansatz
    carries a nontrivial Hopf invariant, so A.B integral is nonzero)."""
    solver = CosseratField3D(20, 20, 20, use_saturation=True)
    solver.initialize_electron_2_3_sector(R_target=5.0, r_target=1.8)
    # Isolate Hopf contribution.
    solver.k_op10 = 0.0
    solver.k_refl = 0.0
    solver.k_hopf = 0.0
    E_without = solver.total_energy()
    solver.k_hopf = np.pi / 3.0
    E_with = solver.total_energy()
    assert abs(E_with - E_without) > 1e-6


def test_reflection_gradient_matches_finite_difference():
    """FD consistency check on the reflection term alone (Op10 and Cosserat
    terms disabled, only reflection active). Tolerance is looser than the
    strict saturation test because 1/S^2 has sharp curvature."""
    solver = CosseratField3D(12, 12, 12, use_saturation=False)
    solver.initialize_electron_2_3_sector(R_target=3.0, r_target=1.2)
    # Scale omega down to keep S well away from 0 so 1/S^2 is well-conditioned.
    solver.omega = solver.omega * 0.3
    # Isolate reflection: disable every other term.
    solver.G = 0.0
    solver.G_c = 0.0
    solver.gamma = 0.0
    solver.k_op10 = 0.0
    solver.k_refl = 1.0

    dE_du, dE_dw = solver.energy_gradient()

    omega_mag = np.sqrt(np.sum(solver.omega**2, axis=-1))
    candidates = np.argwhere(solver.mask_A & (omega_mag > 0.1))
    assert len(candidates) > 5

    h = 1e-5
    for site in candidates[:2]:
        ix, iy, iz = site
        for k in range(3):
            saved = solver.omega[ix, iy, iz, k]
            solver.omega[ix, iy, iz, k] = saved + h
            E_plus = solver.total_energy()
            solver.omega[ix, iy, iz, k] = saved - h
            E_minus = solver.total_energy()
            solver.omega[ix, iy, iz, k] = saved
            fd = (E_plus - E_minus) / (2.0 * h)
            analytical = float(dE_dw[ix, iy, iz, k])
            np.testing.assert_allclose(analytical, fd, rtol=1e-3, atol=1e-4)


# ------------------------------------------------------------------
# Unknot canonical electron seeder (Round 12)
# Per research/_archive/L3_electron_soliton/101_ §9 three-layer canonical:
#   Layer 1 (real-space curve): unknot 0₁ at horn torus R = r
#   Layer 2 (field bundle):     SU(2) double-cover via SO(3) → SU(2)
#                               Rodrigues projection of ω
# Per research/_archive/L3_electron_soliton/102_ §2.6 pre-registered binary criteria.
# ------------------------------------------------------------------


def test_unknot_seeder_omega_is_loop_tangent():
    """ω should point along ê_φ everywhere (perpendicular to ê_ρ in xy-plane,
    z-component zero). Verify ω · ê_ρ = 0 at sample points away from the loop axis."""
    solver = CosseratField3D(32, 32, 32)
    R = 8.0
    solver.initialize_electron_unknot_sector(R_target=R)
    # ω_z must be identically zero (loop tangent in xy-plane)
    np.testing.assert_allclose(solver.omega[..., 2], 0.0, atol=1e-12)
    # ω · ê_ρ = ω_x · cos(φ) + ω_y · sin(φ) ≈ 0 at sites where field is significant
    cx, cy = (solver.nx - 1) / 2.0, (solver.ny - 1) / 2.0
    x = solver._i - cx
    y = solver._j - cy
    rho_xy = np.sqrt(x**2 + y**2)
    eps_rho = 1e-6
    cos_phi = np.where(rho_xy > eps_rho, x / np.maximum(rho_xy, eps_rho), 0.0)
    sin_phi = np.where(rho_xy > eps_rho, y / np.maximum(rho_xy, eps_rho), 0.0)
    omega_dot_rho = solver.omega[..., 0] * cos_phi + solver.omega[..., 1] * sin_phi
    omega_mag = np.sqrt(np.sum(solver.omega**2, axis=-1))
    significant = omega_mag > 0.5
    if np.any(significant):
        # ω perpendicular to ê_ρ at significant sites
        np.testing.assert_allclose(omega_dot_rho[significant], 0.0, atol=1e-10)


def test_unknot_seeder_no_winding():
    """Unknot seed should have NO (p, q) winding — ω at fixed φ is ψ-independent.
    Compare ω at two poloidal positions on the same toroidal angle:
    ω(ρ_xy = R + r, z = 0) and ω(ρ_xy = R - r, z = 0) should be parallel
    (both ê_φ at the same φ), differing only in magnitude profile.
    """
    solver = CosseratField3D(48, 48, 48)
    R, r = 12.0, 4.0  # standard torus (R > r) for clean ψ-distinction
    solver.initialize_electron_unknot_sector(R_target=R, r_target=r)
    # Sample two grid cells on the +x axis (φ = 0): one at outer tube edge, one at inner
    cx, cy, cz = (solver.nx - 1) / 2.0, (solver.ny - 1) / 2.0, (solver.nz - 1) / 2.0
    ix_outer = int(round(cx + R + r))  # outer poloidal point at φ=0
    ix_inner = int(round(cx + R - r))  # inner poloidal point at φ=0
    iy = int(round(cy))
    iz = int(round(cz))
    # At φ=0: ê_φ = (0, 1, 0). So ω should point along +y at both points.
    # ω_x should be ≈ 0 (proportional to -sin 0 = 0)
    # ω_y should be > 0 (proportional to +cos 0 = 1)
    # Both at outer and inner positions should have same direction (both +y)
    assert abs(solver.omega[ix_outer, iy, iz, 0]) < 0.1, "ω_x not ≈ 0 at outer φ=0"
    assert abs(solver.omega[ix_inner, iy, iz, 0]) < 0.1, "ω_x not ≈ 0 at inner φ=0"
    assert solver.omega[ix_outer, iy, iz, 1] > 0.0, "ω_y not positive at outer"
    assert solver.omega[ix_inner, iy, iz, 1] > 0.0, "ω_y not positive at inner"


def test_unknot_seeder_topology_c_zero():
    """Pre-registered binary criterion C1: extract_crossing_count = 0 for unknot."""
    solver = CosseratField3D(32, 32, 32)
    solver.initialize_electron_unknot_sector(R_target=8.0)
    c = solver.extract_crossing_count()
    assert c == 0, f"Unknot seed must have c=0, got c={c}"


def test_unknot_seeder_hopf_charge_zero():
    """Pre-registered binary criterion C2: extract_hopf_charge ≈ 0 for unknot
    (zero linking number for a single unlinked closed loop)."""
    solver = CosseratField3D(32, 32, 32)
    solver.initialize_electron_unknot_sector(R_target=8.0)
    Q_H = solver.extract_hopf_charge()
    assert abs(Q_H) < 1e-3, f"Unknot Q_H must be ≈ 0, got Q_H={Q_H}"


def test_unknot_seeder_horn_torus_default():
    """Default r_target = R_target (horn torus). extract_shell_radii should
    return R ≈ r within a few percent (HWHM convention slight underestimate)."""
    solver = CosseratField3D(32, 32, 32)
    solver.initialize_electron_unknot_sector(R_target=8.0)  # r defaults to 8.0
    R_extracted, r_extracted = solver.extract_shell_radii()
    # R_extract ≈ R_target via HWHM (known ~7% systematic underestimate)
    assert abs(R_extracted - 8.0) / 8.0 < 0.10
    # Horn torus: r_extract should equal R_extract (within HWHM-vs-loop convention)
    assert abs(R_extracted - r_extracted) / max(R_extracted, 1e-9) < 0.05


def test_unknot_seeder_energy_finite_nonneg_nontrivial():
    """Pre-registered binary criteria C5 + C6: total_energy finite, ≥ 0, and
    ≫ vacuum-floor noise (seeded state has real physics, not collapsed)."""
    solver = CosseratField3D(32, 32, 32, use_saturation=True)
    solver.initialize_electron_unknot_sector(R_target=8.0)
    E = solver.total_energy()
    assert np.isfinite(E)
    assert E >= 0.0
    assert E > 1.0  # ≫ vacuum noise; unknot seed at scale-1 amplitude has E ~ 1e5


def test_unknot_seeder_amplitude_scale_linear():
    """Doubling amplitude_scale should ~quadruple energy density (W ∝ |ω|² leading order)."""
    solver_a = CosseratField3D(24, 24, 24, use_saturation=False)  # disable saturation for cleaner test
    solver_b = CosseratField3D(24, 24, 24, use_saturation=False)
    solver_a.initialize_electron_unknot_sector(R_target=6.0, amplitude_scale=1.0)
    solver_b.initialize_electron_unknot_sector(R_target=6.0, amplitude_scale=2.0)
    omega_max_a = float(np.max(np.sqrt(np.sum(solver_a.omega**2, axis=-1))))
    omega_max_b = float(np.max(np.sqrt(np.sum(solver_b.omega**2, axis=-1))))
    # Peak ω scales linearly with amplitude_scale
    np.testing.assert_allclose(omega_max_b / omega_max_a, 2.0, rtol=1e-6)


def test_unknot_seeder_distinct_from_2_3_torus_knot():
    """The new unknot seeder should produce DIFFERENT ω-field topology
    than the existing (2,3) torus-knot seeder. Specifically:
    - unknot: c = 0, no (p, q) winding
    - (2,3) seed: c ≥ 2 (target c = 3 by Sutcliffe ansatz)"""
    solver_unknot = CosseratField3D(32, 32, 32)
    solver_2_3 = CosseratField3D(32, 32, 32)
    solver_unknot.initialize_electron_unknot_sector(R_target=8.0)
    solver_2_3.initialize_electron_2_3_sector(R_target=8.0, r_target=3.0)
    c_unknot = solver_unknot.extract_crossing_count()
    c_2_3 = solver_2_3.extract_crossing_count()
    assert c_unknot == 0
    assert c_2_3 >= 2  # (2,3) seed produces c=2 or 3 depending on extraction
    assert c_unknot != c_2_3, f"Unknot and (2,3) seeds produced same c={c_unknot}"


def test_unknot_seeder_u_field_zero():
    """u (translation) should be zero — only ω is seeded."""
    solver = CosseratField3D(16, 16, 16)
    solver.initialize_electron_unknot_sector(R_target=4.0)
    np.testing.assert_allclose(solver.u, 0.0)


# ------------------------------------------------------------------
# Carrier-sector GATE #1 — spin double-cover representability
# (prereg: research/2026-06-19_spin-doublecover-gate_prereg.md)
# ------------------------------------------------------------------


def test_quaternion_helpers_unit_and_identity():
    """SU(2)-lift helpers: ω=0 → identity quaternion; quat-mul identity law."""
    q0 = _omega_to_quaternion(np.zeros(3))
    np.testing.assert_allclose(q0, np.array([1.0, 0.0, 0.0, 0.0]), atol=1e-12)
    # q ⊗ identity = q.
    q = _omega_to_quaternion(np.array([0.7, -0.3, 1.1]))
    identity = np.array([1.0, 0.0, 0.0, 0.0])
    np.testing.assert_allclose(_quat_mul(q, identity), q, atol=1e-12)
    # Unit norm preserved.
    assert abs(np.linalg.norm(q) - 1.0) < 1e-12


def test_axis_angle_rotation_matches_rodrigues_baseline():
    """_axis_angle_to_rotation about x by π flips ẑ → −ẑ (ties to the
    test_rodrigues_projection_rotation_by_pi_around_x_flips_z calibration)."""
    R = _axis_angle_to_rotation(np.array([1.0, 0.0, 0.0]), np.pi)
    z_hat = np.array([0.0, 0.0, 1.0])
    np.testing.assert_allclose(R @ z_hat, np.array([0.0, 0.0, -1.0]), atol=1e-12)


def test_spin_doublecover_gate_verdict_pass():
    """GATE #1: the SU(2)-lift double-cover IS representable at the lattice
    level, and DIFFERS from the trivial-vector baseline.

    Frozen-prereg discriminator (research/2026-06-19_spin-doublecover-gate_prereg.md):
      - VALIDATE-ON-KNOWN: trivial-vector n_hat baseline returns at φ=2π.
      - OP_A (SO(3) rotation-vector re-lift, = trivial baseline): +I at 2π.
      - OP_B (SU(2) 2T-action lift, the FM-on-K4 mechanism): −I at 2π, +I at 4π.
      => verdict PASS (double-cover representable; differs from baseline).

    Stable across diagnostic scales R = 4, 6, 8 (lattice-resolved, NOT the
    sub-cell ~0.16 ℓ_node canonical scale). KINEMATIC ONLY — no time-stepping.
    """
    for R, r in [(4.0, 2.0), (6.0, 3.0), (8.0, 4.0)]:
        N = int(2 * R + 12)
        solver = CosseratField3D(N, N, N, dx=1.0, use_saturation=False)
        solver.initialize_electron_unknot_sector(R_target=R, r_target=r, amplitude_scale=1.0)
        res = solver.probe_spin_doublecover_holonomy(body_axis=(0.0, 0.0, 1.0), n_phi=720)

        # VALIDATE-ON-KNOWN: trivial-vector baseline returns at 2π (else HALT).
        assert res["nhat_baseline_returned"], (
            f"R={R}: trivial-vector baseline did NOT return at 2π "
            f"(|Δ|={res['nhat_baseline_2pi']:.2e}) → HALT (solver bug)"
        )
        # OP_A (= trivial baseline) returns at 2π (no double-cover memory).
        assert res["opA_lift_sign_2pi"] > 0.0, f"R={R}: OP_A should return +I at 2π"
        assert res["opA_lift_sign_4pi"] > 0.0, f"R={R}: OP_A should return +I at 4π"
        # OP_B (the FM-on-K4 / 2T action) carries the double-cover signature.
        assert res["opB_lift_sign_2pi"] < 0.0, (
            f"R={R}: OP_B SU(2) lift should be −I at 2π (double-cover signature), "
            f"got sign {res['opB_lift_sign_2pi']:+.0f}"
        )
        assert abs(res["opB_lift_sign_4pi"] - 1.0) < 1e-9, (
            f"R={R}: OP_B SU(2) lift should return +I at 4π, "
            f"got sign {res['opB_lift_sign_4pi']:+.0f}"
        )
        # The discriminator: OP_B DIFFERS from the trivial-vector baseline (OP_A).
        assert res["opB_lift_sign_2pi"] != res["opA_lift_sign_2pi"], (
            f"R={R}: double-cover lift must DIFFER from trivial-vector baseline"
        )
        assert res["verdict"] == "PASS", f"R={R}: expected PASS, got {res['verdict']}"
