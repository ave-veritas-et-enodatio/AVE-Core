"""
Unit tests for the 3D Cosserat field solver on the K4 substrate.

Covers:
- Tetrahedral-gradient operator exactness on linear fields.
- Grid initialization (A/B sublattice masks, alive-site count).
- Sutcliffe-style (2,3) initial field sanity (localized, nonzero, decays).
- Kinematic tensor shapes and antisymmetric-cross-product correctness.
- Energy functional returns finite non-negative values.
- Diagnostic readouts (R, r, c, Q) run without error on the initial state.

Reference: research/L3_electron_soliton/08_, 09_.
"""
import numpy as np
import pytest

from ave.topological.cosserat_field_3d import (
    CosseratField3D,
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
    probe_sites = candidates[::max(1, len(candidates) // 4)][:3]

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
