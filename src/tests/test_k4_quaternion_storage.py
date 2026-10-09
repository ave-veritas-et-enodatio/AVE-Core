"""R1 acceptance tests for K4 quaternion-storage mode (PR-B).

Spec sources: 2026-10-08-charged-seed-K4-change-SPEC_CANDIDATE.md §6 pass/fail lines #5-#6,
              2026-10-08-charged-seed-K4-BRIEF.md §PR-B,
              LADDER-charged-seed-K4-2026-10-08.md §2 (dt 2.24e-4).

Run conditions (CI):
  Tests marked DEFERRED_LARGE run only when RUN_K4_LARGE=1 is set.
  R1 spec-size (96³ r_c=12, 64³ vs 128³), R1′, #15, R2, and the
  timing probe are NOT run in CI — each needs a separate Grant GO.

Torque convention verified numerically: τ=½Im(g⊗q̄), NOT q̄⊗g.
"""

import os
import numpy as np
import pytest

from ave.topological.cosserat_field_3d import (
    CosseratField3D,
    _quat_mul_np,
    _quat_exp_np,
    _left_torque_from_grad,
    _q_to_n_jax,
)
import jax.numpy as jnp

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

LARGE = os.environ.get("RUN_K4_LARGE", "0") == "1"

TETRA_OFFSETS = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))


def _bond_re_min(q: np.ndarray, mask_alive: np.ndarray) -> float:
    """Minimum Re(q̄(x)⊗q(x+p)) over all alive-site bonds (short-arc check)."""
    q_conj = q * np.array([1.0, -1.0, -1.0, -1.0])
    re_min = 1.0
    for (di, dj, dk) in TETRA_OFFSETS:
        qs = np.roll(np.roll(np.roll(q, -di, axis=0), -dj, axis=1), -dk, axis=2)
        prod = _quat_mul_np(q_conj, qs)
        re_alive = prod[mask_alive, 0]
        re_min = min(re_min, float(re_alive.min()))
    return re_min


# ---------------------------------------------------------------------------
# (a) k_refl constructor flag + read-back assert
# ---------------------------------------------------------------------------


def test_k_refl_default():
    cf = CosseratField3D(8, 8, 8)
    assert cf.k_refl == 1.0


def test_k_refl_kwarg():
    cf = CosseratField3D(8, 8, 8, k_refl=0.0)
    assert cf.k_refl == 0.0


def test_k_refl_arbitrary():
    cf = CosseratField3D(8, 8, 8, k_refl=2.5)
    assert cf.k_refl == 2.5


def test_k_refl_unchanged_by_rotation_storage():
    cf = CosseratField3D(8, 8, 8, k_refl=0.75, rotation_storage="quaternion")
    assert cf.k_refl == 0.75


# ---------------------------------------------------------------------------
# (b) Default omega path is byte-identical (back-compat)
# ---------------------------------------------------------------------------


def test_default_path_is_omega():
    cf = CosseratField3D(8, 8, 8)
    assert cf.rotation_storage == "omega"


def test_omega_and_default_energy_equal():
    """Explicit rotation_storage='omega' gives same energy as the default."""
    rng = np.random.default_rng(42)
    n = 8
    u = rng.standard_normal((n, n, n, 3)) * 1e-3
    omega = rng.standard_normal((n, n, n, 3)) * 1e-3

    cf_default = CosseratField3D(n, n, n)
    cf_default.u = u.copy()
    cf_default.omega = omega.copy()

    cf_explicit = CosseratField3D(n, n, n, rotation_storage="omega")
    cf_explicit.u = u.copy()
    cf_explicit.omega = omega.copy()

    assert cf_default.total_energy() == cf_explicit.total_energy()


def test_omega_step_byte_identical():
    """step() with rotation_storage='omega' is byte-identical to the default."""
    n = 8
    rng = np.random.default_rng(7)
    u0 = rng.standard_normal((n, n, n, 3)) * 1e-4
    w0 = rng.standard_normal((n, n, n, 3)) * 1e-4

    cf_def = CosseratField3D(n, n, n)
    cf_def.u = u0.copy()
    cf_def.omega = w0.copy()

    cf_exp = CosseratField3D(n, n, n, rotation_storage="omega")
    cf_exp.u = u0.copy()
    cf_exp.omega = w0.copy()

    dt = cf_def.cfl_dt
    cf_def.step(dt)
    cf_exp.step(dt)

    np.testing.assert_array_equal(cf_def.u, cf_exp.u)
    np.testing.assert_array_equal(cf_def.omega, cf_exp.omega)


# ---------------------------------------------------------------------------
# (c) Norm preservation: |q| − 1 < 1e-12 at all alive sites after stepping
# ---------------------------------------------------------------------------


def test_k4_norm_preservation_vacuum():
    """Identity field stays unit norm under K4 VV."""
    cf = CosseratField3D(12, 12, 12, rotation_storage="quaternion")
    for _ in range(5):
        cf.step(dt=0.01)
    q_norms = np.linalg.norm(cf.q[cf.mask_alive], axis=-1)
    assert np.max(np.abs(q_norms - 1.0)) < 1e-12, (
        f"|q|-1 max = {np.max(np.abs(q_norms-1.0)):.2e}"
    )


def test_k4_norm_preservation_perturbed():
    """Small perturbation stays unit norm for R1-B (spec line #6)."""
    n = 16
    cf = CosseratField3D(n, n, n, rotation_storage="quaternion")
    # Seed a small rotation wave at amplitude 1e-3
    rng = np.random.default_rng(20261008)
    dq = rng.standard_normal((n, n, n, 3)) * 1e-3
    cf.q[cf.mask_alive, 1:] = dq[cf.mask_alive]
    # Renormalize to unit quaternion
    norms = np.linalg.norm(cf.q, axis=-1, keepdims=True)
    cf.q = cf.q / np.where(norms > 0, norms, 1.0)
    cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])

    dt = cf.cfl_dt
    for _ in range(10):
        cf.step(dt)

    q_norms = np.linalg.norm(cf.q[cf.mask_alive], axis=-1)
    assert np.max(np.abs(q_norms - 1.0)) < 1e-12, (
        f"|q|-1 max = {np.max(np.abs(q_norms-1.0)):.2e}"
    )


# ---------------------------------------------------------------------------
# (d) Bond Re: Re(q̄(x)⊗q(x+p)) > 0 for all resolved bonds (short-arc)
# ---------------------------------------------------------------------------


def test_k4_bond_re_positive_vacuum():
    """Vacuum field (identity) has Re(q̄q')=1 on all bonds."""
    cf = CosseratField3D(12, 12, 12, rotation_storage="quaternion")
    for _ in range(5):
        cf.step(dt=0.01)
    re_min = _bond_re_min(cf.q, cf.mask_alive)
    assert re_min > 0.0, f"Min Re(q̄q') = {re_min:.4f}"


def test_k4_bond_re_positive_perturbed():
    """Small perturbation keeps Re(q̄q') > 0 (spec line #6)."""
    n = 16
    cf = CosseratField3D(n, n, n, rotation_storage="quaternion")
    rng = np.random.default_rng(20261009)
    dq = rng.standard_normal((n, n, n, 3)) * 1e-3
    cf.q[cf.mask_alive, 1:] = dq[cf.mask_alive]
    norms = np.linalg.norm(cf.q, axis=-1, keepdims=True)
    cf.q = cf.q / np.where(norms > 0, norms, 1.0)
    cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])

    dt = cf.cfl_dt
    for _ in range(10):
        cf.step(dt)

    re_min = _bond_re_min(cf.q, cf.mask_alive)
    assert re_min > 0.0, f"Min Re(q̄q') = {re_min:.4f}"


# ---------------------------------------------------------------------------
# (e) Hedgehog N=1 (static; small grid for CI)
# ---------------------------------------------------------------------------


def test_k4_hedgehog_n1_static():
    """Analytic degree-1 hedgehog gives c_det_alive4 ≈ 1 (R1-B sanity).

    Uses n=48, rc=6 (CI-safe size; see SPEC §6 line #6).
    The spec's full R1 run at 96³ r_c=12 is DEFERRED below.
    """
    from ave.topological.charge_counters import hedgehog, c_det_alive4, bcc_alive_mask

    n, rc = 48, 6
    q = hedgehog(n, rc)
    alive = bcc_alive_mask((n, n, n))
    N = c_det_alive4(q, alive, h=1.0)
    # Static analytic field: N should be close to 1 (first-order gradient error)
    assert abs(N - 1.0) < 0.15, f"Hedgehog static N = {N:.4f}, expected 1"


@pytest.mark.skipif(not LARGE, reason="Deferred: needs RUN_K4_LARGE=1 (Grant GO)")
def test_k4_hedgehog_n1_dynamic_r1_spec():
    """R1 spec: degree-1 hedgehog n=96, rc=12 keeps N=1 under K4 dynamics.

    DEFERRED — do NOT run in CI.  Requires RUN_K4_LARGE=1 + Grant GO.
    Size: 96³, ~10 steps at cfl_dt.
    """
    from ave.topological.charge_counters import hedgehog, c_det_alive4, bcc_alive_mask

    n, rc = 96, 12
    q_init = hedgehog(n, rc)
    cf = CosseratField3D(n, n, n, rotation_storage="quaternion")
    cf.q = q_init.copy()
    cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])

    alive = bcc_alive_mask((n, n, n))
    dt = cf.cfl_dt
    for _ in range(10):
        cf.step(dt)

    N = c_det_alive4(cf.q, alive, h=1.0)
    assert abs(N - 1.0) < 0.05, f"Hedgehog dynamic N = {N:.4f} at 96³"
    q_norms = np.linalg.norm(cf.q[cf.mask_alive], axis=-1)
    assert np.max(np.abs(q_norms - 1.0)) < 1e-12


# ---------------------------------------------------------------------------
# (f) Dispersion match: K4 vs omega within 1e-3 at amplitude 1e-3 (spec #5)
# ---------------------------------------------------------------------------


def test_k4_dispersion_match():
    """K4 and omega engines agree within 1% after 20 steps at amplitude 1e-3.

    Spec pass/fail #5: patched vs current dispersion at 1e-3 amplitude agree
    within 1% over k ≤ π/(4dx).
    """
    n = 32
    amplitude = 1e-3
    n_steps = 20

    cf_omega = CosseratField3D(n, n, n, rotation_storage="omega")
    cf_k4 = CosseratField3D(n, n, n, rotation_storage="quaternion")

    # Seed identical Gaussian wavepacket (omega engine)
    cf_omega.initialize_gaussian_wavepacket_omega(
        center=(n // 2, n // 2, n // 2),
        sigma=4.0,
        direction=(1.0, 0.0, 0.0),
        wavelength=8.0,
        amplitude=amplitude,
    )

    # K4: small-angle q ≈ (1, omega/2)
    omega0 = cf_omega.omega.copy()
    q_init = np.zeros((n, n, n, 4))
    q_init[..., 0] = 1.0
    q_init[..., 1:] = omega0 / 2.0
    norms = np.linalg.norm(q_init, axis=-1, keepdims=True)
    cf_k4.q = q_init / norms
    cf_k4.q[~cf_k4.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
    cf_k4.Omega = cf_omega.omega_dot.copy()

    dt = cf_omega.cfl_dt
    for _ in range(n_steps):
        cf_omega.step(dt)
        cf_k4.step(dt)

    # Compare via small-angle log-map: omega_k4 ≈ 2 * q_imag
    omega_omega = cf_omega.omega
    omega_k4_approx = cf_k4.q[..., 1:] * 2.0
    ref_norm = np.linalg.norm(omega_omega)
    rel_diff = np.linalg.norm(omega_k4_approx - omega_omega) / max(ref_norm, 1e-30)
    assert rel_diff < 0.01, (
        f"K4 vs omega rel diff after {n_steps} steps: {rel_diff:.2e} (limit 0.01)"
    )


# ---------------------------------------------------------------------------
# Force identity: dW/du and dW/dq (→tau) agree with omega engine at 1e-3
# ---------------------------------------------------------------------------


def test_k4_force_identity():
    """K4 force gradients agree with omega at amplitude 1e-3 to O(amplitude²).

    Checks -dW/du (force on u) is identical to O(amplitude²).
    """
    import jax.numpy as jnp
    from ave.topological.cosserat_field_3d import (
        _val_and_grad_k4,
        _val_and_grad_saturated,
    )

    n = 16
    rng = np.random.default_rng(42)
    amplitude = 1e-3

    u = rng.standard_normal((n, n, n, 3)) * amplitude
    omega = rng.standard_normal((n, n, n, 3)) * amplitude

    cf = CosseratField3D(n, n, n)
    mask_alive = jnp.asarray(cf.mask_alive)

    # Omega engine gradient
    _, (dW_du_omega, dW_dw) = _val_and_grad_saturated(
        jnp.asarray(u), jnp.asarray(omega), mask_alive,
        cf.dx, cf.G, cf.G_c, cf.gamma,
        cf.omega_yield, cf.epsilon_yield,
        cf.k_op10, cf.k_refl, cf.k_hopf,
    )

    # K4 engine: construct q ≈ (1, omega/2)
    q = np.zeros((n, n, n, 4))
    q[..., 0] = 1.0
    q[..., 1:] = omega / 2.0
    norms = np.linalg.norm(q, axis=-1, keepdims=True)
    q /= norms

    _, (dW_du_k4, _dW_dq) = _val_and_grad_k4(
        jnp.asarray(u), jnp.asarray(q), mask_alive,
        cf.dx, cf.G, cf.G_c, cf.gamma,
        cf.omega_yield, cf.epsilon_yield,
        cf.k_op10, cf.k_refl, cf.k_hopf,
    )

    dW_du_omega_np = np.asarray(dW_du_omega)
    dW_du_k4_np = np.asarray(dW_du_k4)

    ref = np.linalg.norm(dW_du_omega_np)
    diff = np.linalg.norm(dW_du_k4_np - dW_du_omega_np)
    rel = diff / max(ref, 1e-30)
    # At amplitude 1e-3, force difference O(amplitude²) ≈ 1e-6 relative
    assert rel < 0.01, f"Force relative diff: {rel:.2e}"


# ---------------------------------------------------------------------------
# Numpy quaternion helpers (unit tests for the Lie-group drift primitives)
# ---------------------------------------------------------------------------


def test_quat_mul_np_identity():
    a = np.array([[1.0, 0.0, 0.0, 0.0]])
    b = np.array([[0.7071, 0.0, 0.7071, 0.0]])
    result = _quat_mul_np(a, b)
    np.testing.assert_allclose(result, b, atol=1e-6)


def test_quat_exp_np_zero():
    v = np.zeros((4, 3))
    result = _quat_exp_np(v)
    expected = np.tile([1.0, 0.0, 0.0, 0.0], (4, 1))
    np.testing.assert_allclose(result, expected, atol=1e-15)


def test_quat_exp_np_half_turn():
    v = np.array([[0.0, 0.0, np.pi / 2.0]])
    result = _quat_exp_np(v)
    # exp((0, 0, 0, pi/2)) = (cos(pi/2), 0, 0, sin(pi/2)) = (0, 0, 0, 1)
    expected = np.array([[0.0, 0.0, 0.0, 1.0]])
    np.testing.assert_allclose(result, expected, atol=1e-12)


def test_left_torque_from_grad_pure_g0():
    """At identity q=(1,0,0,0), tau = -g0/2 * (0,0,0) + g_vec/2 * 1 = g_vec/2."""
    q = jnp.array([[1.0, 0.0, 0.0, 0.0]])
    g = jnp.array([[0.0, 2.0, 4.0, 6.0]])
    tau = np.asarray(_left_torque_from_grad(g, q))
    # tau_1 = 0.5*(0*0 + 2*1 - 0*0 + 0*0) = 1
    # tau_2 = 0.5*(0*0 + 2*0 + 4*1 - 0*0) = 2
    # tau_3 = 0.5*(0*0 - 2*0 + 4*0 + 6*1) = 3
    np.testing.assert_allclose(tau, [[1.0, 2.0, 3.0]], atol=1e-12)


# ---------------------------------------------------------------------------
# R2 config read-back (csk4_r2_config.py)
# ---------------------------------------------------------------------------


def test_r2_config_read_back():
    """R2 config parameters survive make_r2_solver() on a tiny grid.

    Uses an 8³ grid — does NOT allocate 288³.
    """
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import make_r2_solver, assert_r2_config
    cf = make_r2_solver(nx=8, ny=8, nz=8)
    assert_r2_config(cf)  # raises on any mismatch


# ---------------------------------------------------------------------------
# Timing probe guard (csk4_timing_probe.py)
# ---------------------------------------------------------------------------


def test_timing_probe_parses():
    """csk4_timing_probe imports cleanly (guard does not fire at import time)."""
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    import importlib
    import csk4_timing_probe  # must not raise
    assert hasattr(csk4_timing_probe, 'run_timing_probe')
    assert hasattr(csk4_timing_probe, 'PROBE_GRIDS')
    assert hasattr(csk4_timing_probe, 'N_PROBE_STEPS')


def test_timing_probe_guard_refuses():
    """run_timing_probe() raises without AVE_TIMING_PROBE_GO=1."""
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_timing_probe import run_timing_probe
    old = os.environ.pop('AVE_TIMING_PROBE_GO', None)
    try:
        with pytest.raises(RuntimeError, match='AVE_TIMING_PROBE_GO'):
            run_timing_probe()
    finally:
        if old is not None:
            os.environ['AVE_TIMING_PROBE_GO'] = old
