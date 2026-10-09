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
    _val_and_grad_k4,
    _val_and_grad_saturated,
)
# B1 module-split: the K4 helpers now live in k4_quaternion; import from there.
# cosserat_field_3d re-exports them for back-compat, but new tests use the
# canonical home.
from ave.topological.k4_quaternion import (
    _quat_mul_np,
    _quat_exp_np,
    _left_torque_from_grad,
    _q_to_n_jax,
    _compute_strain_q_jax,
    _energy_density_k4_saturated,
    _total_energy_k4_jit,
    omega_eng_from_q,
    q_from_omega_eng,
    count_charge_k4,
    _bond_wryness_jax,
)
import jax.numpy as jnp

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

LARGE = os.environ.get("RUN_K4_LARGE", "0") == "1"

TETRA_OFFSETS = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def make_r1_solver(n: int = 16, **kw):
    """Factory for R1 tests: k_refl=0 asserted via read-back (v5 rule).

    Every R1 test that builds a solver uses this. The read-back assert fires
    before any physics, so a mutant that silently ignores the k_refl=0 kwarg
    (e.g. _k4_init hard-coding k_refl=1) trips here rather than producing a
    silently-reflecting run that still passes the downstream physics gates.
    pml_thickness=0 / damping_gamma=0 are the R1 conservative-dynamics defaults;
    callers may override via **kw (appended after, so keyword-only in effect).
    """
    kw.setdefault("pml_thickness", 0)
    kw.setdefault("damping_gamma", 0.0)
    cf = CosseratField3D(n, n, n, k_refl=0.0, rotation_storage="quaternion", **kw)
    assert cf.k_refl == 0.0, (
        f"make_r1_solver: k_refl read-back failed: {cf.k_refl!r} != 0.0 "
        "(is _k4_init ignoring the k_refl kwarg?)")
    return cf


def _pr_strain_batch(Fs, qs):
    """Center-site strain through the PR's own _compute_strain_q_jax.

    Builds a 4×4×4 u field from F = I + ∇u with CONSTANT ∇u, so the diamond
    tetrahedral gradient is exact at the center site (1,1,1): ε = Rᵀ(q)·F − I is
    read off the engine's own stencil, not a reimplemented matrix form. This is
    the R1-9 (v5) requirement — exercise cf's strain function, not a copy.
    Fs: (N,3,3) deformation gradients; qs: (N,4) quaternions → ε: (N,3,3).
    """
    N = len(Fs)
    u_arr = np.zeros((4 * N, 4, 4, 3))
    q_arr = np.zeros((4 * N, 4, 4, 4))
    q_arr[..., 0] = 1.0
    I, J, Kk = np.meshgrid(np.arange(4), np.arange(4), np.arange(4), indexing="ij")
    X = np.stack([I - 1, J - 1, Kk - 1], -1).astype(float)  # rel to center (1,1,1)
    for s in range(N):
        G = np.asarray(Fs[s]) - np.eye(3)  # ∇u (constant)
        u_arr[4 * s:4 * (s + 1)] = np.einsum("ij,abcj->abci", G, X)
        q_arr[4 * s:4 * (s + 1)] = qs[s]
    eps = np.asarray(_compute_strain_q_jax(jnp.asarray(u_arr), jnp.asarray(q_arr), 1.0))
    return eps[4 * np.arange(N) + 1, 1, 1]  # center site of each block


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


def _k4_omega_max(n: int = 16, iters: int = 20, seed: int = 0) -> float:
    """Spectral-radius Ω_max of the K4 stiffness about the vacuum state, by power
    iteration on the Hessian-vector product (jax.jvp of the K4 gradient).

    H·v = d/dt[grad_k4(state + t·v)]|_{t=0} = jvp(grad_k4, state, v)[1]. Power
    iterate 20× on a random v; Ω_max = √|λ_max(H)| with mass ρ_vac = I_ω = 1.
    Small grid (n=16) keeps it fast. Vacuum state: u=0, q=(1,0,0,0) at alive
    sites. The result sets the K4 time-step stability bound dt_K4 ≤ 0.25/Ω_max.
    """
    import jax

    cf = CosseratField3D(n, n, n, rotation_storage="quaternion",
                         pml_thickness=0, damping_gamma=0.0)
    mask = cf._mask_alive_jax
    args = (cf.dx, cf.G, cf.G_c, cf.gamma, cf.omega_yield, cf.epsilon_yield,
            cf.k_op10, cf.k_refl, cf.k_hopf)
    u0 = jnp.zeros((n, n, n, 3))
    q0 = jnp.asarray(cf.q)

    def grad_k4(state):
        u, q = state
        _, (du, dq) = _val_and_grad_k4(u, q, mask, *args)
        return (du, dq)

    def hvp(state, v):
        return jax.jvp(grad_k4, (state,), (v,))[1]

    rng = np.random.default_rng(seed)
    v = (jnp.asarray(rng.standard_normal((n, n, n, 3))),
         jnp.asarray(rng.standard_normal((n, n, n, 4))))

    def vnorm(w):
        return float(jnp.sqrt(sum(jnp.sum(x * x) for x in w)))

    v = tuple(x / (vnorm(v) + 1e-30) for x in v)
    lam = 0.0
    for _ in range(iters):
        Hv = hvp((u0, q0), v)
        lam = vnorm(Hv)
        v = tuple(x / (lam + 1e-30) for x in Hv)
    return float(np.sqrt(abs(lam)))  # mass = rho_vac = I_omega = 1


def _k4_omega_max_hh(n: int = 16, rc: int = 2, iters: int = 20) -> float:
    """Spectral-radius Ω_max of the K4 stiffness about a HEDGEHOG state.

    Proxy: n=16, rc=2 is the proportional scale-down of hedgehog(48,6)
    (ratio 1:3).  Unlike _k4_omega_max, this starts the power iteration at
    the hedgehog field, not the vacuum.  For DEFAULT parameters (k_op10=1,
    γ=1) core saturation clips S_eps_sq→0, so Ω_max_hh ≈ Ω_vac (exterior
    sites dominate) and dt = cfl/16 gives ~304 steps.  Using the hedgehog
    state is correct: a future high-γ/k_op10 configuration would give a
    larger Ω_max_hh than the vacuum and require a smaller dt.
    """
    from ave.topological.charge_counters import hedgehog as _hh
    import jax

    cf = CosseratField3D(n, n, n, k_refl=0.0, rotation_storage="quaternion",
                         pml_thickness=0, damping_gamma=0.0)
    assert cf.k_refl == 0.0, (
        f"_k4_omega_max_hh: k_refl read-back failed: {cf.k_refl!r} != 0.0 "
        "(reflection stiffness must be off to measure the R1 hedgehog Ω_max)")
    mask = cf._mask_alive_jax
    args = (cf.dx, cf.G, cf.G_c, cf.gamma, cf.omega_yield, cf.epsilon_yield,
            cf.k_op10, cf.k_refl, cf.k_hopf)
    u0 = jnp.zeros((n, n, n, 3))
    q0_np = _hh(n, rc).copy()
    q0_np[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
    q0 = jnp.asarray(q0_np)

    def grad_k4(state):
        u, q = state
        _, (du, dq) = _val_and_grad_k4(u, q, mask, *args)
        return (du, dq)

    # JIT the HVP to compile once and amortize the tracing cost across 20 iterations.
    hvp_jit = jax.jit(lambda state, v: jax.jvp(grad_k4, (state,), (v,))[1])

    rng = np.random.default_rng(0)
    v = (jnp.asarray(rng.standard_normal((n, n, n, 3))),
         jnp.asarray(rng.standard_normal((n, n, n, 4))))

    def vnorm(w):
        return float(jnp.sqrt(sum(jnp.sum(x * x) for x in w)))

    v = tuple(x / (vnorm(v) + 1e-30) for x in v)
    lam = 0.0
    for _ in range(iters):
        Hv = hvp_jit((u0, q0), v)
        lam = vnorm(Hv)
        v = tuple(x / (lam + 1e-30) for x in Hv)
    return float(np.sqrt(abs(lam)))


# ---------------------------------------------------------------------------
# O1 ruling: declared ω-engine map (spec A5.3, strain_ruling.py e92ca222be08)
# ---------------------------------------------------------------------------
# The strain ε = Rᵀ(q)·F − I is the O1 (objective) form (spec A5.3, K-R20).
# The engine's stored ω is the INVERSE of the rotation q encodes (K-R19):
#   ω_eng ≡ −2 Im log q,  i.e. q(ω_eng) = (cos|ω|/2, −ω̂ sin|ω|/2).
# At small angle: q ≈ (1, −ω_eng/2).  This map is the declared convention for
# every linear/spectral comparison between K4 and the ω engine:
#   Rᵀ·F built from q=(1,+ω/2):  |F_K4−F_ω| ~ O(θ)   (slope ≈ 1.0) — NO match
#   Rᵀ·F built from q=(1,−ω/2):  |F_K4−F_ω| ~ O(θ²)  (slope ≈ 2.0) — matches
# strain_ruling result at h=1e-6: max rel err ~2.8e-6 under the ω map.
_OMEGA_TO_Q_SIGN = -1.0  # omega-matched quaternion: q_vec = sign·ω/2 (O1 map)


def _q_from_omega(omega: np.ndarray) -> np.ndarray:
    """Build the omega-engine-matched unit quaternion q ≈ (1, −ω/2) (B7 note)."""
    q = np.zeros(omega.shape[:-1] + (4,))
    q[..., 0] = 1.0
    q[..., 1:] = _OMEGA_TO_Q_SIGN * omega / 2.0
    norms = np.linalg.norm(q, axis=-1, keepdims=True)
    return q / np.maximum(norms, 1e-30)


def _qstars_tets():
    """QSTARS + BCC_TETS matching the PR-A charge_counters test conventions."""
    from ave.topological.charge_counters import random_regular_values, _bcc_tets
    return random_regular_values(5, seed=20261008, max_q0=0.0), _bcc_tets()


def _energy_slope(energies):
    """Fit log-slope of energy over time; None if < 101 samples (ladder #11).

    Returns None → INCONCLUSIVE (insufficient samples). A float → the fitted
    d(log H)/dt slope over the recording window.
    """
    if energies is None or len(energies) < 101:
        return None
    arr = np.asarray(energies, dtype=float)
    t = np.arange(len(arr), dtype=float)
    valid = np.isfinite(arr) & (arr > 0)
    if int(np.sum(valid)) < 10:
        return None
    coeffs = np.polyfit(t[valid], np.log(arr[valid]), 1)
    return float(coeffs[0])


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
# R1-1: default ω path is a2be127d-identical + engine-coefficient hash
# ---------------------------------------------------------------------------


def test_r1_1_omega_path_reference():
    """R1-1 (v6): the default ω path reproduces the a2be127d reference.

    Loads src/tests/data/a2be127d_omega_ref.npz (10 default-dt + 10 fixed-dt
    steps on an 8³ grid, seeded random u/ω, with and without PML 4 / damping
    0.05). Pass: bit-exact if the npz platform tag matches the current machine/OS/
    JAX/NumPy; otherwise |delta| ≤ 1e-18 absolute on u, omega, u_dot.

    Rejects 6.6e-16 (the dt mutant moves 3.2e-16/4.7e-16; a real cross-platform
    diff is 6.8e-21, well within 1e-18).

    The in-process mutant kill (omega_path_dt_perturb) is in the companion test
    test_omega_step_dispatch_vs_direct_exact, which compares step(dt) dispatch
    against _step_omega(dt, apply_pml) direct on bitwise-identical copies —
    platform-independent since both use the same explicit dt.
    """
    import platform as _platform
    ref = np.load(os.path.join(DATA_DIR, "a2be127d_omega_ref.npz"))
    n = 8
    u0, w0, dt = ref["u0"], ref["w0"], float(ref["dt"])

    # Determine comparison mode from platform tag.
    tag_machine = str(ref["platform_machine"]) if "platform_machine" in ref else None
    tag_os = str(ref["platform_os"]) if "platform_os" in ref else None
    tag_jax = str(ref["platform_jax"]) if "platform_jax" in ref else None
    tag_numpy = str(ref["platform_numpy"]) if "platform_numpy" in ref else None
    import jax as _jax
    same_platform = (
        tag_machine == _platform.machine() and
        tag_os == _platform.system() and
        tag_jax == _jax.__version__ and
        tag_numpy == np.__version__
    )
    atol = 0.0 if same_platform else 1e-18
    mode = "bit-exact" if same_platform else f"|delta|≤1e-18 (cross-platform)"
    print(f"[R1-1] platform tag match={same_platform} → {mode}")

    # Case 1: default step() (dt=None → cfl_dt).
    cf = CosseratField3D(n, n, n, pml_thickness=0, damping_gamma=0.0)
    cf.u = u0.copy(); cf.omega = w0.copy()
    for _ in range(10):
        cf.step()
    np.testing.assert_allclose(cf.u, ref["u_def"], rtol=0, atol=atol,
        err_msg=f"R1-1 case1 u mismatch ({mode})")
    np.testing.assert_allclose(cf.omega, ref["om_def"], rtol=0, atol=atol,
        err_msg=f"R1-1 case1 omega mismatch ({mode})")
    np.testing.assert_allclose(cf.u_dot, ref["ud_def"], rtol=0, atol=atol,
        err_msg=f"R1-1 case1 u_dot mismatch ({mode})")

    # Case 2: explicit step(dt).
    cf2 = CosseratField3D(n, n, n, pml_thickness=0, damping_gamma=0.0)
    cf2.u = u0.copy(); cf2.omega = w0.copy()
    for _ in range(10):
        cf2.step(dt)
    np.testing.assert_allclose(cf2.u, ref["u_fix"], rtol=0, atol=atol,
        err_msg=f"R1-1 case2 u mismatch ({mode})")
    np.testing.assert_allclose(cf2.omega, ref["om_fix"], rtol=0, atol=atol,
        err_msg=f"R1-1 case2 omega mismatch ({mode})")

    # Case 3: PML=4 / damping=0.05.
    cf3 = CosseratField3D(n, n, n, pml_thickness=4, damping_gamma=0.05)
    cf3.u = u0.copy(); cf3.omega = w0.copy()
    for _ in range(10):
        cf3.step()
    np.testing.assert_allclose(cf3.u, ref["u_pml"], rtol=0, atol=atol,
        err_msg=f"R1-1 case3 PML u mismatch ({mode})")
    np.testing.assert_allclose(cf3.omega, ref["om_pml"], rtol=0, atol=atol,
        err_msg=f"R1-1 case3 PML omega mismatch ({mode})")

    # In-process: step() [default dt] vs step(cfl_dt) [explicit] must be bit-exact.
    cf_def = CosseratField3D(n, n, n, pml_thickness=0, damping_gamma=0.0)
    cf_exp = CosseratField3D(n, n, n, pml_thickness=0, damping_gamma=0.0)
    cf_def.u = u0.copy(); cf_def.omega = w0.copy()
    cf_exp.u = u0.copy(); cf_exp.omega = w0.copy()
    cf_def.step()
    cf_exp.step(cf_exp.cfl_dt)
    np.testing.assert_array_equal(cf_def.u, cf_exp.u,
        err_msg="R1-1: step() != step(cfl_dt) — default and explicit dt not bit-exact")
    np.testing.assert_array_equal(cf_def.omega, cf_exp.omega,
        err_msg="R1-1: step() omega != step(cfl_dt) omega")

    # k_refl read-back: k_refl=0 kwarg must survive the K4 constructor (v6 rule).
    cf_k4 = make_r1_solver(n)
    assert cf_k4.k_refl == 0.0, (
        f"R1-1 k_refl read-back: {cf_k4.k_refl!r} != 0.0")


def test_omega_step_dispatch_vs_direct_exact():
    """R1-1 (H1, in-process): step(dt) dispatch == _step_omega(dt, apply_pml) direct.

    Kills omega_path_dt_perturb (dt·(1+1e-12) in _step_dispatch's ω branch): the
    dispatch path adds the perturbation, the direct _step_omega call does not. The
    two clones diverge by ~5e-10 with the mutant, >> the zero difference without.

    Platform-independent: both clones run in the same process with the same
    explicit dt — no cfl_dt platform-float discrepancy.
    """
    ref = np.load(os.path.join(DATA_DIR, "a2be127d_omega_ref.npz"))
    n = 8
    u0, w0, dt = ref["u0"], ref["w0"], float(ref["dt"])

    # Dispatch clone: step(dt) → _step_dispatch → _step_omega(dt*(1+1e-12)) with mutant.
    cf_A = CosseratField3D(n, n, n, pml_thickness=0, damping_gamma=0.0)
    cf_A.u = u0.copy(); cf_A.omega = w0.copy()
    cf_A.step(dt)

    # Direct clone: _step_omega(dt, False) bypasses _step_dispatch entirely.
    cf_B = CosseratField3D(n, n, n, pml_thickness=0, damping_gamma=0.0)
    cf_B.u = u0.copy(); cf_B.omega = w0.copy()
    cf_B._step_omega(dt, False)

    np.testing.assert_array_equal(cf_A.u, cf_B.u)
    np.testing.assert_array_equal(cf_A.omega, cf_B.omega)


# Pinned sha256 of inspect.getsource(_energy_density_saturated) at HEAD 9f5540ca
# + this fix pass. Re-pin ONLY on an intentional energy-coefficient edit.
_ENERGY_COEF_HASH = "50b31cac13b5de3da8044a94c8db73d7df5f96e3a313b4cd762395e970b06b68"


def test_r1_1_engine_coefficient_hash():
    """R1-1 (ii, v5): hash of _energy_density_saturated source pins the coefficients.

    Kills coef_gamma_x2_omega_engine and any silent edit to the (2/3) Cauchy
    coefficient, the W_cauchy·G + W_micropolar·G_c combination, or the γ·S_κ²
    term: changing any constant in the energy-density body changes the sha256 of
    its source and trips this test. If an edit is intentional, re-pin the hash.
    """
    import inspect
    import hashlib
    from ave.topological.cosserat_field_3d import _energy_density_saturated
    src = inspect.getsource(_energy_density_saturated)
    h = hashlib.sha256(src.encode()).hexdigest()
    assert h == _ENERGY_COEF_HASH, (
        f"_energy_density_saturated source hash changed: {h!r} != {_ENERGY_COEF_HASH!r}. "
        "If the energy-coefficient block was edited intentionally, re-pin "
        "_ENERGY_COEF_HASH; otherwise this is coef_gamma_x2 or a silent coeff edit.")


def test_r1_7_determinism():
    """R1-7 (v5): bitwise run-to-run determinism; dt/2 agrees within O(dt²).

    Two identical K4 runs (same seed, same dt) give bit-identical fields. A dt/2
    run over the same physical time T agrees with the dt run to O(dt²) (the VV
    local error), not bit-for-bit. k_refl=0 via make_r1_solver.
    """
    n = 12

    def run(dt, n_steps):
        cf = make_r1_solver(n)
        rng = np.random.default_rng(20261009)
        dq = rng.standard_normal((n, n, n, 3)) * 1e-3
        cf.q[cf.mask_alive, 1:] = dq[cf.mask_alive]
        norms = np.linalg.norm(cf.q, axis=-1, keepdims=True)
        cf.q = cf.q / np.where(norms > 0, norms, 1.0)
        cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
        H0 = cf.total_energy_k4() + cf.kinetic_energy_k4()
        for _ in range(n_steps):
            cf.step(dt)
        return cf.q.copy(), cf.total_energy_k4() + cf.kinetic_energy_k4(), H0

    dt = make_r1_solver(n).cfl_dt / 8.0
    q_a, H_a, H0 = run(dt, 40)
    q_b, H_b, _ = run(dt, 40)
    np.testing.assert_array_equal(q_a, q_b)  # bitwise determinism
    assert H_a == H_b

    # dt/2 over the same T: O(dt²) agreement on the conserved energy.
    q_h, H_h, _ = run(dt / 2.0, 80)
    rel = abs(H_h - H_a) / max(abs(H0), 1e-30)
    print(f"[R1-7] bitwise OK; dt/2 vs dt energy rel diff = {rel:.3e}")
    assert rel < 1e-3, f"dt/2 energy disagreement {rel:.2e} larger than O(dt²) expected"


# ---------------------------------------------------------------------------
# (c) Norm preservation: |q| − 1 < 1e-12 at all alive sites after stepping
# ---------------------------------------------------------------------------


def test_k4_norm_preservation_vacuum():
    """Identity field stays unit norm under K4 VV (R1, k_refl=0 via make_r1_solver)."""
    cf = make_r1_solver(12)
    for _ in range(5):
        cf.step(dt=0.01)
    q_norms = np.linalg.norm(cf.q[cf.mask_alive], axis=-1)
    assert np.max(np.abs(q_norms - 1.0)) < 1e-12, (
        f"|q|-1 max = {np.max(np.abs(q_norms-1.0)):.2e}"
    )


def test_k4_norm_preservation_perturbed():
    """Small perturbation stays unit norm for R1-B (spec line #6)."""
    n = 16
    cf = make_r1_solver(n)
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
    """Vacuum field (identity) has Re(q̄q')=1 on all bonds (R1, k_refl=0)."""
    cf = make_r1_solver(12)
    for _ in range(5):
        cf.step(dt=0.01)
    re_min = _bond_re_min(cf.q, cf.mask_alive)
    assert re_min > 0.0, f"Min Re(q̄q') = {re_min:.4f}"


def test_k4_bond_re_positive_perturbed():
    """Small perturbation keeps Re(q̄q') > 0 (spec line #6)."""
    n = 16
    cf = make_r1_solver(n)
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
# F5: make_r1_solver read-back trip + F2: ω_eng map round-trip
# ---------------------------------------------------------------------------


def test_make_r1_solver_readback_trips_if_k4_init_ignores_krefl(monkeypatch):
    """F5: monkeypatch _k4_init to ignore k_refl; make_r1_solver must raise.

    The v5 rule requires every R1 solver to assert k_refl=0 at read-back time.
    A mutant that silently drops the kwarg (forces k_refl=1) is caught by the
    factory's own assertion BEFORE any physics runs — this test exercises that
    guard by patching _k4_init to always set k_refl=1.
    """
    import ave.topological.k4_quaternion as k4mod
    import ave.topological.cosserat_field_3d as cfmod
    original = k4mod._k4_init

    def _ignore_krefl(self, k_refl, rotation_storage):
        original(self, 1.0, rotation_storage)  # always k_refl=1

    monkeypatch.setattr(k4mod, "_k4_init", _ignore_krefl)
    monkeypatch.setattr(cfmod, "_k4_init", _ignore_krefl)
    with pytest.raises(AssertionError, match="k_refl"):
        make_r1_solver(n=8)


def test_omega_eng_round_trip():
    """F2: q_from_omega_eng ∘ omega_eng_from_q = id to ~1e-15 (Gate: 6.7e-16).

    ω → q → ω over random |ω| < π (short-arc branch); q → ω → q over random
    unit q with q0 ≥ 0. Also pins the convention q(ω_eng) = (cos|ω|/2, −ω̂ sin|ω|/2)
    (K-R19): a +θ ẑ rotation stores as ω_eng = −θ ẑ, i.e. q_vec sign is negative.
    """
    rng = np.random.default_rng(20261009)
    # ω → q → ω
    omega = rng.standard_normal((5000, 3))
    omega = (omega / np.linalg.norm(omega, axis=-1, keepdims=True)
             * rng.uniform(0.0, np.pi - 0.1, (5000, 1)))
    q = q_from_omega_eng(omega)
    assert np.max(np.abs(np.linalg.norm(q, axis=-1) - 1.0)) < 1e-14
    omega2 = omega_eng_from_q(q)
    err_wqw = float(np.max(np.abs(omega2 - omega)))
    assert err_wqw < 1e-14, f"ω→q→ω round-trip err = {err_wqw:.2e}"

    # q → ω → q (short-arc q0 ≥ 0; account for double cover via sign)
    qr = rng.standard_normal((5000, 4))
    qr = qr / np.linalg.norm(qr, axis=-1, keepdims=True)
    qr[:, 0] = np.abs(qr[:, 0])
    w = omega_eng_from_q(qr)
    qr2 = q_from_omega_eng(w)
    sgn = np.sign(np.sum(qr2 * qr, axis=-1, keepdims=True))
    err_qwq = float(np.max(np.abs(qr2 * sgn - qr)))
    assert err_qwq < 1e-14, f"q→ω→q round-trip err = {err_qwq:.2e}"

    # Convention pin: +θ ẑ → ω_eng = −θ ẑ (q_vec negative, K-R19).
    theta = 0.7
    q_rot = np.array([np.cos(theta / 2.0), 0.0, 0.0, np.sin(theta / 2.0)])
    w_rot = omega_eng_from_q(q_rot)
    np.testing.assert_allclose(w_rot, [0.0, 0.0, -theta], atol=1e-14)
    print(f"[omega_map] ω→q→ω={err_wqw:.2e}  q→ω→q={err_qwq:.2e}")


# ---------------------------------------------------------------------------
# (e) Hedgehog N=1 (static; small grid for CI)
# ---------------------------------------------------------------------------


def test_k4_hedgehog_n1_static():
    """Analytic degree-1 hedgehog gives c_det_alive4 ≈ 1 (R1-B sanity).

    Uses n=48, rc=6 (CI-safe size; see SPEC §6 line #6).
    NOTE: this static tolerance-0.15 check is the exact-count-independent sanity
    gate; the c_exact==1 exact count on the SAME static field is verified in
    test_k4_hedgehog_n1_exact_static.  The spec's full R1 run at 96³ r_c=12 is
    DEFERRED below.
    """
    from ave.topological.charge_counters import hedgehog, c_det_alive4, bcc_alive_mask

    n, rc = 48, 6
    q = hedgehog(n, rc)
    alive = bcc_alive_mask((n, n, n))
    N = c_det_alive4(q, alive, h=1.0)
    # Static analytic field: N should be close to 1 (first-order gradient error)
    assert abs(N - 1.0) < 0.15, f"Hedgehog static N = {N:.4f}, expected 1"


def test_k4_hedgehog_n1_exact_static():
    """B3: c_exact == 1 on the static degree-1 hedgehog (n=48, rc=6, BCC s=2).

    Replaces the tolerance-0.15 adjudication with the EXACT signed preimage
    count (c_exact), which resolves on this CI-safe field. Bond Re(q̄q') > 0 on
    every alive bond (the field sweeps q0 → −1 at the core but neighbors are
    never antipodal, so the short-arc invariant holds).
    """
    from ave.topological.charge_counters import (
        hedgehog, c_exact, c_det_alive4, bcc_alive_mask)

    n, rc = 48, 6
    q = hedgehog(n, rc)
    alive = bcc_alive_mask((n, n, n))
    qstars, tets = _qstars_tets()

    assert _bond_re_min(q, alive) > 0.0, "static hedgehog has an antipodal bond"
    result = c_exact(q, qstars, tets=tets, s=2)
    assert result["resolved"], (
        f"c_exact UNRESOLVED on static hedgehog: n_bad={result['n_bad']}, "
        f"n_degen={result['n_degen']}"
    )
    assert result["value"] == 1, f"c_exact value = {result['value']!r}, expected 1"
    N_det = c_det_alive4(q, alive, h=1.0)
    assert 0.5 < N_det < 1.5, f"c_det monitor out of band: {N_det:.4f}"


def test_r1_2e_collapse_detector():
    """R1-2e (v6): collapse detector and classify_checkpoint harness, T=2π.

    hedgehog(48,6), k_refl=0, T=2π, dt=cfl/2 (133 steps). A harness function
    from csk4_r2_config (shared with R2) returns min Re(q̄q') and a COLLAPSE
    flag each step; each checkpoint is RESOLVED(N), UNRESOLVED, or COLLAPSE.

    Pass:
      (a) collapse flag fires with t_first ∈ [3.4, 3.8] (Gate: 3.605)
      (b) from t_first on, every checkpoint is COLLAPSE or UNRESOLVED — never
          RESOLVED(+1), never C-link-only value, never unflagged N change.
          "Never C-link-only": classify with collapse_flagged=False must also
          return UNRESOLVED on every post-collapse checkpoint.
      (c) every resolved value before t_first is +1
      (d) r_eq (equivalent radius of q0<0 region) ≤ 3 at t_first
    Flip probe: t=0 hedgehog with one alive site q→−q must be flagged immediately.

    Mutants: M1 disable detector (collapse_check returns False; fails a);
             M2 fall back to C-link when C-exact UNRESOLVED (fails b — both the
             never-C-link-only check on every post-collapse checkpoint, and the
             explicit M2 probe assertion below).
    """
    from ave.topological.charge_counters import hedgehog, bcc_alive_mask
    from ave.topological.k4_quaternion import collapse_check
    from scripts.vol_4_engineering.csk4_r2_config import (
        classify_checkpoint, r_eq_from_q)

    n, rc = 48, 6
    cf = make_r1_solver(n)
    cf.q = hedgehog(n, rc).copy()
    cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
    alive = bcc_alive_mask((n, n, n))
    r_eq0 = r_eq_from_q(cf.q, alive)  # t=0 reference (BCC density ¼, dx=1)

    # r_eq(0) read-back: 228 alive sites with q0<0 → 6.016 (×4 BCC correction)
    assert abs(r_eq0 - 6.016) <= 0.005, (
        f"R1-2e r_eq(0) read-back: {r_eq0:.4f} != 6.016 ± 0.005 "
        f"(228 sites with q0<0; ×4 BCC correction missing?)")

    dt = cf.cfl_dt / 2.0
    n_steps = int(np.ceil(2.0 * np.pi / dt))
    # Checkpoint density: every ≤ 0.25 time units (≈5 steps at dt=cfl/2≈0.0474)
    ckpt_gap = max(1, int(0.25 / dt))

    collapse_flagged = False
    t_first = None
    r_eq_at_first = None
    rows = []           # (t, outcome, value) — all checkpoints
    post_ckpt_states = []  # (t, q_copy) for every post-collapse checkpoint

    for s in range(n_steps):
        cf.step(dt)
        cc = collapse_check(cf.q, alive)
        if cc["collapse"] and not collapse_flagged:
            collapse_flagged = True
            t_first = (s + 1) * dt
            r_eq_at_first = r_eq_from_q(cf.q, alive)

        t_step = (s + 1) * dt
        if (s + 1) % ckpt_gap == 0 or s == n_steps - 1:
            ck = classify_checkpoint(cf.q, alive, collapse_flagged)
            rows.append((t_step, ck["outcome"], ck["value"]))
            if collapse_flagged:
                post_ckpt_states.append((t_step, cf.q.copy()))

    # (a) early guard: M1 (disable detector) must trip here before any t_first formatting
    assert t_first is not None, (
        "R1-2e (a): collapse flag never fired over T=2π; expected t_first ≈ 3.605")

    print(f"[R1-2e] r_eq0={r_eq0:.3f} t_first={t_first:.4f} r_eq_at_first={r_eq_at_first:.3f} "
          f"n_checkpoints={len(rows)} post_collapse_ckpts={len(post_ckpt_states)}")
    print("[R1-2e] checkpoints (t, outcome, value):")
    for row in rows:
        print("  ", row)

    # (a) collapse flag fires in [3.4, 3.8] — not-None asserted above
    assert 3.4 <= t_first <= 3.8, (
        f"R1-2e (a): t_first={t_first:.3f} outside [3.4, 3.8] (Gate: 3.605)")

    # (d) r_eq at t_first ∈ [1.9, 2.4] (Gate v7: 2.122 from 10 alive sites with q0<0)
    assert r_eq_at_first is not None and 1.9 <= r_eq_at_first <= 2.4, (
        f"R1-2e (d): r_eq={r_eq_at_first:.4f} at t_first; expected ∈ [1.9, 2.4] "
        f"(Gate: 2.122, 10 sites; ×4 BCC correction missing gives 1.337)")

    # (c) all resolved values before t_first must be +1
    pre_collapse = [(t, o, v) for (t, o, v) in rows if t <= t_first]
    for t, outcome, val in pre_collapse:
        if outcome.startswith("RESOLVED"):
            assert val == 1, (
                f"R1-2e (c): resolved value ≠ +1 at t={t:.3f} (pre-collapse): "
                f"outcome={outcome!r} value={val!r}")

    # (b) from t_first on: every checkpoint is COLLAPSE or UNRESOLVED
    post_rows = [(t, o, v) for (t, o, v) in rows if t > t_first]
    for t, outcome, val in post_rows:
        assert outcome in ("COLLAPSE", "UNRESOLVED"), (
            f"R1-2e (b): post-collapse checkpoint at t={t:.3f} has outcome "
            f"{outcome!r} (must be COLLAPSE or UNRESOLVED)")

    # (b) "never C-link-only value": classify with collapse_flagged=False must
    # return UNRESOLVED on EVERY post-collapse checkpoint.  The M2 mutant
    # (fallback to c_link when c_exact UNRESOLVED) would return RESOLVED(0)
    # here and trip this assertion.  Also find the M2 probe state.
    m2_t = None
    m2_q = None
    m2_c_link_val = None
    for t_saved, q_saved in post_ckpt_states:
        ck_no = classify_checkpoint(q_saved, alive, False)
        assert ck_no["outcome"] == "UNRESOLVED", (
            f"R1-2e (b) never-C-link-only: at t={t_saved:.3f} "
            f"classify_checkpoint(collapse_flagged=False) returned "
            f"{ck_no['outcome']!r} (value={ck_no['value']!r}); "
            f"M2 mutant uses c_link as fallback")
        # Probe c_link to locate the M2 kill state (first where c_link resolves)
        if m2_q is None:
            r_probe = count_charge_k4(q_saved, alive)
            cl = r_probe.get("c_link_result") or {}
            if cl.get("resolved"):
                m2_t = t_saved
                m2_q = q_saved
                m2_c_link_val = cl.get("value")

    print(f"[R1-2e M2 probe] t={m2_t} c_link_val={m2_c_link_val}")
    # M2 probe: there MUST be at least one post-collapse state where c_link
    # resolves — ensures the M2 mutant kill is unconditional, not contingent.
    assert m2_q is not None, (
        "R1-2e M2 probe: no post-collapse checkpoint found where c_link resolves; "
        "expected c_link=0 to resolve post-collapse (Gate trace: t≈5.218); "
        "increase checkpoint density or extend T if c_link resolution window changed")
    ck_m2 = classify_checkpoint(m2_q, alive, False)
    assert ck_m2["outcome"] == "UNRESOLVED", (
        f"R1-2e M2 probe: classify_checkpoint returned {ck_m2['outcome']!r} "
        f"with collapse_flagged=False (c_link={m2_c_link_val}); "
        f"must return UNRESOLVED — M2 mutant uses c_link as fallback")

    # Flip probe: t=0 q→−q at one alive site must fire immediately.
    q_flip = hedgehog(n, rc).copy()
    q_flip[~alive] = np.array([1.0, 0.0, 0.0, 0.0])
    core_site = tuple(np.argwhere(alive)[0])
    q_flip[core_site] = -q_flip[core_site]
    cc_flip = collapse_check(q_flip, alive)
    assert cc_flip["collapse"], (
        f"R1-2e flip probe: q→−q at alive site {core_site} did not fire collapse "
        f"(min_re={cc_flip['min_re']:.4f})")


@pytest.mark.engine_sim
def test_r1_2d_static_128_derrick():
    """R1-2d static (v7, LOG-ONLY, OPT-IN): 128³ Derrick scan — 3-point scale test at rc=12.

    Static balance read-back, not a stability claim (K-R23).
    Seed: _hedgehog_at(128,12,(0,0,0),L=48), gamma=4320, k_op10=8.88e5.
    No time-stepping. The 3-point Derrick test logs s and d²E/dλ² (no assert on
    these values — v7 classifies this as log-only per K-R23). Seed bitwise
    read-back assert is kept (seed-cutoff mutant detection).

    Deselected from make test / serial tails by -m "not engine_sim".
    """
    from ave.topological.charge_counters import _hedgehog_at, bcc_alive_mask
    from ave.topological.k4_quaternion import _total_energy_k4_jit, TETRA_OFFSETS
    import jax; import jax.numpy as jnp

    n, rc = 128, 12
    L_seed = 48       # tanh cutoff for _hedgehog_at
    gamma = 4320.0
    k_op10 = 8.88e5

    cf_base = make_r1_solver(n)
    cf_base.gamma = gamma
    cf_base.k_op10 = k_op10

    # Seed: _hedgehog_at with explicit L=48 cutoff (NOT hedgehog(128,12) which uses L=64).
    q_base = _hedgehog_at(n, rc, (0, 0, 0), L=L_seed).copy()
    q_base[~cf_base.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
    alive = bcc_alive_mask((n, n, n))

    # seed_fn: the ONE callable that defines the scan seed, factored from the
    # baseline.  energy_at_lambda MUST use this, not _hedgehog_at independently,
    # so that a seed-cutoff mutant (hedgehog(128,12) → L=64) is caught by both
    # the read-back assertion and the energy scan.
    def seed_fn(rc_val, L_val):
        q = _hedgehog_at(n, rc_val, (0, 0, 0), L=L_val).copy()
        q[~cf_base.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
        return q

    # Read-back: seed_fn at λ=1 must equal q_base bitwise.
    # The seed-cutoff mutant (hedgehog(128,12), L=64) gives a different profile
    # and fails here.
    assert np.array_equal(seed_fn(rc, L_seed)[alive], q_base[alive]), (
        "R1-2d static: seed_fn(rc,L_seed) ≠ q_base on alive sites (seed-cutoff mismatch)")

    args = (cf_base.dx, cf_base.G, cf_base.G_c, cf_base.gamma,
            cf_base.omega_yield, cf_base.epsilon_yield,
            cf_base.k_op10, cf_base.k_refl, cf_base.k_hopf)
    mask_jax = jnp.asarray(cf_base.mask_alive)
    u_zero = jnp.zeros((n, n, n, 3))

    def energy_at_lambda(lam):
        # Proper Derrick scaling via seed_fn: rc → rc·λ, L → L·λ.
        q_s = seed_fn(rc * lam, L_seed * lam)
        return float(_total_energy_k4_jit(u_zero, jnp.asarray(q_s), mask_jax, *args))

    # Primary λ set (0.9, 1.0, 1.1) — Gate: s=1.005, d²E=+7.0e6
    lams = [0.9, 1.0, 1.1]
    Es = [energy_at_lambda(lam) for lam in lams]
    print(f"[R1-2d static] Derrick (0.9/1.0/1.1): λ={lams}  E={[f'{e:.4e}' for e in Es]}")
    A = np.vstack([[l**2, l, 1] for l in lams])
    a, b, _c = np.linalg.solve(A, Es)
    s = -b / (2 * a)
    d2E = 2 * a
    print(f"[R1-2d static] Derrick fit (0.9/1.0/1.1): s={s:.4f}  d²E/dλ²={d2E:.3e}")

    # Secondary λ set (0.95, 1.0, 1.05) — finer bracket, same pass criteria
    lams2 = [0.95, 1.0, 1.05]
    Es2 = [energy_at_lambda(lam) for lam in lams2]
    print(f"[R1-2d static] Derrick (0.95/1.0/1.05): λ={lams2}  E={[f'{e:.4e}' for e in Es2]}")
    A2 = np.vstack([[l**2, l, 1] for l in lams2])
    a2, b2, _c2 = np.linalg.solve(A2, Es2)
    s2 = -b2 / (2 * a2)
    d2E2 = 2 * a2
    print(f"[R1-2d static] Derrick fit (0.95/1.0/1.05): s={s2:.4f}  d²E/dλ²={d2E2:.3e}")

    # LOG-ONLY (K-R23): these are static balance read-backs, not stability claims.
    print(f"[R1-2d static] Derrick (0.9/1.0/1.1): s={s:.4f}  d²E/dλ²={d2E:.3e}  "
          f"(Gate: s≈1.005, d²E≈+7.0e6; LOG-ONLY, not asserted)")
    print(f"[R1-2d static] Derrick (0.95/1.0/1.05): s={s2:.4f}  d²E/dλ²={d2E2:.3e}")


def test_r1_2b_short_arc_through_resolution_window_krefl0():
    """R1-2a/2b/7 (v6): option (i) — pre-collapse, storage-only at T=1.8.

    hedgehog(48,6), k_refl=0, dt=min(cfl/16, 0.25/Ω_max_hh), T=1.8 (pre-collapse;
    first antipodal bond causes core collapse at t≈3.605). ~304 steps.

    Pass: ||q|-1| < 1e-12 every step; every alive bond Re(q̄q') > 0 at every step
    (R1-2a short-arc invariant); S_kappa² > 0 at every alive site at every step
    (bond wryness below saturation at T=1.8); two identical runs produce bit-identical
    q (R1-7 determinism). Label: "pre-collapse, storage-only".

    Mutants: additive_q_update (changes the Lie-group Verlet to additive; trips
    the |q|=1 invariant after a few steps); omega_storage_replay (hemisphere
    projection: after the K4 left-multiply, sites with q0<0 are flipped q→−q;
    destroys the continuous short-arc invariant by creating artificial sign
    discontinuities across bonds; trips `assert min_re_all > 0.0`).
    """
    from ave.topological.charge_counters import hedgehog, bcc_alive_mask

    T_PRE = 1.8  # pre-collapse (core collapse at t≈3.605)
    n, rc = 48, 6
    cf = make_r1_solver(n)
    cf.q = hedgehog(n, rc).copy()
    cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
    alive = bcc_alive_mask((n, n, n))

    # Ω_max measured on HEDGEHOG state (not vacuum): n=16, rc=2 proxy (1:3
    # scale-down of hedgehog(48,6)).  At DEFAULT params (k_op10=1, γ=1)
    # Ω_max_hh ≈ Ω_vac; a high-γ/k_op10 configuration would give larger Ω
    # and reduce dt below cfl/16 here.
    Omega_max_hh = _k4_omega_max_hh(n=16, rc=2)
    cfl_16 = cf.cfl_dt / 16.0
    dt = min(cfl_16, 0.25 / Omega_max_hh)
    n_steps = int(np.ceil(T_PRE / dt))
    assert n_steps * dt >= T_PRE
    if dt != cfl_16:
        print(f"[R1-2b WARNING] Omega_max_hh={Omega_max_hh:.4f} forced dt={dt:.4e} "
              f"below cfl/16={cfl_16:.4e}; n_steps={n_steps}; "
              "k_refl=0 should give Omega_max_hh≈Omega_vac and dt=cfl/16")
        pytest.fail(
            f"Omega_max_hh={Omega_max_hh:.4f} at k_refl=0 forces dt below "
            f"cfl/16={cfl_16:.4e}; test would exceed 60s — STOP and investigate")
    assert 290 <= n_steps <= 320, (
        f"R1-2b: n_steps={n_steps} outside [290, 320] "
        f"(Omega_max_hh={Omega_max_hh:.4f} dt={dt:.4e} cfl/16={cfl_16:.4e})")
    print(f"[R1-2b option-i] Omega_max_hh={Omega_max_hh:.4f} dt={dt:.4e} n_steps={n_steps}")

    import jax as _jax_r1_2b
    # Fuse all three per-step checks into ONE jit-compiled function returning
    # three scalars: (norm_err_max, min_re, s_kappa_min).  No per-step numpy
    # rolls or separate host round-trips beyond these three scalars.
    _alive_j = jnp.asarray(alive)
    _dx_val = float(cf.dx)
    _oy_val = float(cf.omega_yield)

    @_jax_r1_2b.jit
    def _fused_step_checks(q):
        # Norm check
        norms = jnp.sqrt(jnp.sum(q * q, axis=-1))
        norm_err_max = jnp.max(jnp.where(_alive_j, jnp.abs(norms - 1.0), 0.0))

        # Min Re over alive tetra bonds (replaces _bond_re_min numpy rolls)
        q_conj = q * jnp.array([1.0, -1.0, -1.0, -1.0])
        re_min = jnp.array(1.0)
        for (di, dj, dk) in TETRA_OFFSETS:
            qs = jnp.roll(jnp.roll(jnp.roll(q, -di, axis=0), -dj, axis=1),
                          -dk, axis=2)
            prod_re = (q_conj[..., 0] * qs[..., 0]
                       - q_conj[..., 1] * qs[..., 1]
                       - q_conj[..., 2] * qs[..., 2]
                       - q_conj[..., 3] * qs[..., 3])
            alive_re = jnp.where(_alive_j, prod_re, jnp.ones_like(prod_re))
            re_min = jnp.minimum(re_min, jnp.min(alive_re))

        # S_kappa² = 1 − κ²/ω_yield² (bond wryness below saturation)
        kappa_sq = jnp.sum(_bond_wryness_jax(q, _dx_val) ** 2, axis=(-1, -2))
        kappa_sq_max = jnp.max(jnp.where(_alive_j, kappa_sq, 0.0))
        s_kappa_min = 1.0 - kappa_sq_max / (_oy_val ** 2)

        return norm_err_max, re_min, s_kappa_min

    # Warm up JIT
    _norm0, _re0, _sk0 = _fused_step_checks(jnp.asarray(cf.q))
    _jax_r1_2b.block_until_ready((_norm0, _re0, _sk0))

    # --- Snapshot at step 60 for the R1-7 bitwise repeat (runs only 60 steps)
    _N_R17 = 60
    norm_err_max_all = 0.0
    min_re_all = float(_re0)
    min_s_kappa_sq = float(_sk0)
    for s in range(n_steps):
        cf.step(dt)
        ne, re, sk = _fused_step_checks(jnp.asarray(cf.q))
        _jax_r1_2b.block_until_ready((ne, re, sk))
        if float(ne) >= 1e-12:
            norm_err_max_all = max(norm_err_max_all, float(ne))
        min_re_all = min(min_re_all, float(re))
        min_s_kappa_sq = min(min_s_kappa_sq, float(sk))
        if s + 1 == _N_R17:
            q_snap60 = cf.q.copy()  # snapshot for R1-7

    norm_ok = norm_err_max_all < 1e-12
    q_run1 = cf.q.copy()
    print(f"[R1-2b option-i] n={n} rc={rc} dt={dt:.4e} n_steps={n_steps} "
          f"T={n_steps*dt:.4f} min_re={min_re_all:.4f} "
          f"min_s_kappa_sq={min_s_kappa_sq:.4f} "
          f"norm_err_max={norm_err_max_all:.2e} (pre-collapse, storage-only)")

    assert norm_ok, f"R1-2b: |q|=1 invariant broke (max err={norm_err_max_all:.2e})"
    assert min_re_all > 0.0, (
        f"R1-2b: short-arc antipodal bond found at T=1.8 pre-collapse window "
        f"(min_re={min_re_all:.4f}); the first antipodal bond is at t≈3.605")
    assert min_s_kappa_sq > 0.0, (
        f"R1-2b: S_kappa² saturation hit (min={min_s_kappa_sq:.4f}); "
        f"bond wryness exceeded omega_yield at T=1.8 pre-collapse window")

    # R1-7: bitwise determinism — second run for first 60 steps only.
    cf2 = make_r1_solver(n)
    cf2.q = hedgehog(n, rc).copy()
    cf2.q[~cf2.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
    for _ in range(_N_R17):
        cf2.step(dt)
    np.testing.assert_array_equal(q_snap60, cf2.q,
        err_msg="R1-7: two identical K4 option-(i) runs are not bit-exact at step 60")


# ---------------------------------------------------------------------------
# R1-2d opt-in: P-ii pre-flight + option (ii) dynamic (RUN_K4_LARGE=1)
# ---------------------------------------------------------------------------


@pytest.mark.skipif(not LARGE, reason="Opt-in: needs RUN_K4_LARGE=1 (Grant GO); STOPPED pending T-STAB trade")
def test_r1_2d_option_ii_pii_preflight():
    """Pre-registered A8 prediction (v7): P-ii 128³ pre-flight, T=0.25.

    Config from make_pii_config(); checkpoints from pf_checkpoint_times(0.25).
    Checks antipodal bonds every step; builds a trace dict; calls preflight_verdict.
    Asserts only gate != "INVALID". BREAKUP + CONFIRMED is the predicted outcome.
    Prints gate, a8, t_first, r_first, r_eq ratio and n_antipodal(T) for the PR body.

    NOT run in CI — needs RUN_K4_LARGE=1 + Grant GO. STOPPED.
    """
    import sys, os as _os
    sys.path.insert(0, _os.path.join(_os.path.dirname(__file__),
                                     '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import (make_pii_config, run_preflight, preflight_verdict,
                                 PII_SPEC)

    cfg_dict = make_pii_config(control=False)

    trace = run_preflight(cfg_dict, PII_SPEC, make_solver=make_r1_solver)
    result = preflight_verdict(trace, PII_SPEC)

    r_eq0 = trace.get('r_eq0', 0.0)
    t_first = trace.get('t_first')
    r_first = trace.get('r_first')
    n_antipodal_T = trace.get('n_antipodal_T', 0)
    r_eq_at_first = trace.get('r_eq_at_first')
    r_eq_ratio = r_eq_at_first / r_eq0 if (r_eq_at_first and r_eq0 > 0) else None
    print(f"[P-ii v7] gate={result['gate']} a8={result['a8']} "
          f"t_first={t_first} r_first={r_first} "
          f"r_eq_ratio={r_eq_ratio} n_antipodal_T={n_antipodal_T}")
    print(f"[P-ii v7] seed_sha1={trace.get('seed_sha1')}")
    print(f"[P-ii v7] reasons={result['reasons']}")

    assert result['gate'] != 'INVALID', (
        f"P-ii: gate=INVALID; reasons={result['reasons']}")


@pytest.mark.skipif(not LARGE,
                    reason="Opt-in: needs RUN_K4_LARGE=1 (Grant GO); "
                           "v7: expected NOT AVAILABLE (P-ii predicted BREAKUP, K-R23)")
def test_r1_2d_option_ii_dynamic():
    """R1-2d opt-in option-(ii) dynamic (v6): rc=12 confined hedgehog, 128³.

    Requires P-ii pre-flight (test_r1_2d_option_ii_pii_preflight) to have passed.
    rc=12, gamma=4320, k_op10=8.88e5, k_refl=0, 128³, L=48 seed, dt=1.65e-4.
    T=max(2π, 2 measured breathing periods), ≥38,150 steps.

    Pass: both counters RESOLVED +1 at ≥90% of checkpoints; all resolved values
    +1; no Re≤0; log r_eq. Synthetic 1→0 splice mutant must fire.
    Log drift at dt and dt/2 (no assert).

    NOT run in CI — needs RUN_K4_LARGE=1 + Grant GO.
    """
    import sys as _sys, os as _os2
    _sys.path.insert(0, _os2.path.join(_os2.path.dirname(__file__),
                                       '..', 'scripts', 'vol_4_engineering'))
    from ave.topological.k4_quaternion import collapse_check
    from csk4_r2_config import make_pii_config, preflight_initial_solver
    from scripts.vol_4_engineering.csk4_r2_config import r_eq_from_q

    n, rc = 128, 12
    dt = 1.65e-4
    T_min = max(2.0 * np.pi, 2 * 1.62)  # 2 breathing periods at rc=12 ≈ 1.62 tu
    n_steps = max(38150, int(np.ceil(T_min / dt)))
    ckpt_gap = max(1, n_steps // 50)  # ~50 checkpoints

    pii_cfg = make_pii_config(control=False)
    cf, setup = preflight_initial_solver(pii_cfg, n=n, rc=rc, make_solver=make_r1_solver)
    alive = setup['alive']

    H0 = cf.total_energy_k4() + cf.kinetic_energy_k4()
    re_min_all = 1.0
    rows = []  # (t, resolved, value, r_eq)

    for s in range(n_steps):
        cf.step(dt)
        cc = collapse_check(cf.q, alive)
        re_min_all = min(re_min_all, cc["min_re"])
        assert not cc["collapse"], (
            f"R1-2d option-ii: Re≤0 at step {s+1} t={(s+1)*dt:.4f}")
        if (s + 1) % ckpt_gap == 0 or s == n_steps - 1:
            r = count_charge_k4(cf.q, alive)
            r_eq = r_eq_from_q(cf.q, alive)
            rows.append(((s + 1) * dt, r["resolved"], r["value"], round(r_eq, 3)))

    print(f"[R1-2d option-ii] n_steps={n_steps} min_re={re_min_all:.4f}")
    print("  checkpoints (t, resolved, value, r_eq):")
    for row in rows:
        print("   ", row)

    # Drift log (no assert)
    H_final = cf.total_energy_k4() + cf.kinetic_energy_k4()
    dH_rel = abs(H_final - H0) / abs(H0) if abs(H0) > 1e-20 else float("nan")
    print(f"[R1-2d option-ii drift] dt={dt:.2e}  |ΔH/H0|={dH_rel:.3e}")

    n_resolved = sum(1 for (_, res, v, _) in rows if res)
    n_wrong = sum(1 for (_, res, v, _) in rows if res and v != 1)
    frac = n_resolved / max(len(rows), 1)
    assert frac >= 0.9, (
        f"R1-2d option-ii: only {n_resolved}/{len(rows)} checkpoints resolved "
        f"({frac:.0%} < 90%)")
    assert n_wrong == 0, (
        f"R1-2d option-ii: {n_wrong} resolved checkpoints ≠ +1 (charge flip)")

    # Synthetic 1→0 splice mutant: replace core with vacuum → must perturb verdict.
    q_splice = cf.q.copy()
    c = n // 2
    q_splice[c - rc:c + rc, c - rc:c + rc, c - rc:c + rc] = np.array([1.0, 0.0, 0.0, 0.0])
    q_splice[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
    r_sp = count_charge_k4(q_splice, alive)
    assert (not r_sp["resolved"]) or (r_sp["value"] != 1), (
        f"R1-2d option-ii splice: core→vacuum still reads +1; mutant did not fire")


@pytest.mark.skipif(not LARGE, reason="Opt-in: needs RUN_K4_LARGE=1 (Grant GO); STOPPED pending T-STAB trade")
def test_r1_2d_option_ii_pii_control():
    """Pre-registered A8 control (v7): P-ii-C 128³ Λ-8 control, T=0.25.

    Config from make_pii_config(control=True) (k_op10=5.59e4).
    Asserts gate != "INVALID" and no BREAKUP-class bond.
    INFALL is allowed and printed. Predicted outcome: INFALL near t≈0.1.

    NOT run in CI — needs RUN_K4_LARGE=1 + Grant GO. STOPPED.
    """
    import sys, os as _os
    sys.path.insert(0, _os.path.join(_os.path.dirname(__file__),
                                     '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import (make_pii_config, run_preflight, preflight_verdict,
                                 PII_C_SPEC)

    cfg_dict = make_pii_config(control=True)
    T = cfg_dict['t_end']

    trace = run_preflight(cfg_dict, PII_C_SPEC, make_solver=make_r1_solver)
    result = preflight_verdict(trace, PII_C_SPEC)

    r_eq0 = trace.get('r_eq0', 0.0)
    t_first = trace.get('t_first')
    r_first = trace.get('r_first')
    r_eq_at_first = trace.get('r_eq_at_first')
    r_eq_ratio = r_eq_at_first / r_eq0 if (r_eq_at_first and r_eq0 > 0) else None
    print(f"[P-ii-C v7] gate={result['gate']} a8={result['a8']} "
          f"t_first={t_first} r_first={r_first} r_eq_ratio={r_eq_ratio}")
    print(f"[P-ii-C v7] seed_sha1={trace.get('seed_sha1')}")
    print(f"[P-ii-C v7] reasons={result['reasons']}")

    assert result['gate'] != 'INVALID', (
        f"P-ii-C: gate=INVALID; reasons={result['reasons']}")
    assert result['gate'] != 'BREAKUP', (
        f"P-ii-C control: BREAKUP-class bond detected at t_first={t_first}; "
        f"control should have no BREAKUP-class bond through T={T}")


@pytest.mark.engine_sim
def test_r1_d_krefl1_log_only():
    """R1-D (v6, LOG-ONLY): hedgehog(48,6) at k_refl=1 on BOTH engines, dt ladder.

    K-R18/K-R21 record (dated 2026-10-09). Primary case: hedgehog(48,6), k_refl=1
    (constructor default), T≤1.8 (pre-collapse), ω-engine and K4-engine. At k_refl=1
    the reflection regulator W_refl ∝ 1/(S²+ε) is near-singular at the hedgehog
    core, so energy is not conserved at any CI-affordable dt (K-R18). This logs the
    raw behavior; asserts NOTHING in either direction about k_refl=1 conservation.

    The full 7-rung ladder at T=1.8 per rung needs Grant's GO; by default each rung
    is capped at 2000 steps (T≈0.4 at dt=2e-4). C∞-floor control: smooth sine field
    (n=24, k_refl=1, ω-engine), logged alongside at the same dt ladder, T=0.05/rung.

    dt ladder: 2e-4, 1e-4, 5e-5, 2.5e-5, 1.25e-5, 6.25e-6, 3.125e-6.
    Optional fine rung: 7.8e-7 behind R1D_FINE=1.

    Marked engine_sim (opt-in): deselected by -m "not engine_sim".
    """
    import time as _time
    from ave.topological.charge_counters import hedgehog, bcc_alive_mask

    # Full dt ladder; default = coarsest 2 rungs only; R1D_FULL=1 unlocks all.
    _dt_full = [2e-4, 1e-4, 5e-5, 2.5e-5, 1.25e-5, 6.25e-6, 3.125e-6]
    if os.environ.get("R1D_FINE", "0") == "1":
        _dt_full.append(7.8e-7)
    _full = os.environ.get("R1D_FULL", "0") == "1"
    dt_ladder = _dt_full if _full else _dt_full[:2]  # coarsest 2 by default

    T_HH = 1.8        # hedgehog primary: pre-collapse bound (collapse at t≈3.6)
    N_RUNG_CAP = 250   # per-rung step cap (2 engines × 2 rungs × 250 ≤ ~1000 steps)
    EVAL_EVERY = 50    # evaluate energy every k steps to reduce overhead
    T_CTRL = 0.05     # C∞-floor control window
    N_CTRL_CAP = 800
    WALL_BUDGET_S = 600.0  # hard wall-clock budget; stops ladder cleanly
    _t_start = _time.monotonic()

    n_hh, rc_hh = 48, 6
    q_hh = hedgehog(n_hh, rc_hh).copy()
    alive_hh = bcc_alive_mask((n_hh, n_hh, n_hh))
    _truncated = False

    # ── PRIMARY: hedgehog(48,6) at k_refl=1, ω and K4 ──────────────────────
    for mode in ("omega", "quaternion"):
        if _truncated:
            break
        for dt in dt_ladder:
            if _time.monotonic() - _t_start >= WALL_BUDGET_S:
                print(f"[R1-D] wall-clock budget {WALL_BUDGET_S:.0f}s reached — "
                      f"truncating ladder at dt={dt:.2e} mode={mode}")
                _truncated = True
                break
            n_steps = min(int(round(T_HH / dt)), N_RUNG_CAP)
            cf = CosseratField3D(n_hh, n_hh, n_hh, rotation_storage=mode,
                                 pml_thickness=0, damping_gamma=0.0)  # k_refl=1 default
            al = cf.mask_alive
            if mode == "omega":
                # short-arc ω representation of hedgehog (|ω|→0 at core, |ω|→π at rc)
                cf.omega = omega_eng_from_q(q_hh).copy()
                cf.omega[~al] = np.zeros(3)
                H0 = cf.total_energy() + cf.kinetic_energy()
            else:
                cf.q = q_hh.copy()
                cf.q[~al] = np.array([1.0, 0.0, 0.0, 0.0])
                H0 = cf.total_energy_k4() + cf.kinetic_energy_k4()

            H_prev = H0
            n_jump = 0
            max_jump = 0.0
            max_rel = 0.0
            _rung_t0 = _time.monotonic()
            _truncated_inner = False
            for si in range(n_steps):
                if (si + 1) % EVAL_EVERY == 0:
                    if _time.monotonic() - _t_start >= WALL_BUDGET_S:
                        print(f"[R1-D] in-loop budget reached at step {si+1} "
                              f"mode={mode} dt={dt:.2e}")
                        _truncated = True
                        _truncated_inner = True
                        break
                cf.step(dt)
                if (si + 1) % EVAL_EVERY == 0 or si == n_steps - 1:
                    if mode == "omega":
                        H = cf.total_energy() + cf.kinetic_energy()
                    else:
                        H = cf.total_energy_k4() + cf.kinetic_energy_k4()
                    jump = abs(H - H_prev) / max(abs(H0), 1e-30)
                    if jump > 1e-3:
                        n_jump += 1
                    max_jump = max(max_jump, jump)
                    max_rel = max(max_rel, abs(H - H0) / max(abs(H0), 1e-30))
                    H_prev = H
            if _truncated_inner:
                break

            rung_elapsed = _time.monotonic() - _rung_t0
            # Saturation count and min Re (end-of-rung snapshot)
            if mode == "omega":
                oy = cf.omega_yield
                sat_count = int(np.sum(
                    np.sum(cf.omega[al] ** 2, axis=-1) >= (1.0 - 1e-10) * oy ** 2
                ))
                extra = f" sat_count={sat_count}"
            else:
                sat_count = int(np.sum(cf.q[al, 0] ** 2 < 1e-10))
                min_re = _bond_re_min(cf.q, al)
                extra = f" min_Re={min_re:.4f} sat_count={sat_count}"

            print(f"[R1-D hedgehog k_refl=1] {mode:10s} dt={dt:.2e} steps={n_steps} "
                  f"elapsed={rung_elapsed:.1f}s "
                  f"max|dH/H0|={max_rel:.3e} jumps>1e-3={n_jump} "
                  f"max_step_jump={max_jump:.3e}{extra}")

    # ── C∞-floor CONTROL: smooth sine field (n=24, k_refl=1, ω-engine) ──────
    n_ctrl = 24
    x_ctrl = np.arange(n_ctrl)
    X_ctrl, Y_ctrl, _Z_ctrl = np.meshgrid(x_ctrl, x_ctrl, x_ctrl, indexing="ij")
    ax_ctrl = np.array([1.0, 2.0, 3.0]) / np.sqrt(14.0)
    amp_ctrl = 1.5  # near-saturation
    for dt in dt_ladder:
        if _time.monotonic() - _t_start >= WALL_BUDGET_S:
            print(f"[R1-D] wall-clock budget {WALL_BUDGET_S:.0f}s reached — "
                  f"truncating control ladder at dt={dt:.2e}")
            break
        n_steps_c = min(int(round(T_CTRL / dt)), N_CTRL_CAP)
        th = amp_ctrl * np.sin(2 * np.pi * X_ctrl / n_ctrl) * np.cos(2 * np.pi * Y_ctrl / n_ctrl)
        cf_c = CosseratField3D(n_ctrl, n_ctrl, n_ctrl, rotation_storage="omega",
                               pml_thickness=0, damping_gamma=0.0)  # k_refl=1 default
        al_c = cf_c.mask_alive
        cf_c.omega = (-th[..., None] * ax_ctrl) * al_c[..., None]
        H0_c = cf_c.total_energy() + cf_c.kinetic_energy()
        H_prev_c = H0_c
        n_jump_c = 0
        max_jump_c = 0.0
        max_rel_c = 0.0
        _rung_t0_c = _time.monotonic()
        _truncated_ctrl = False
        for si_c in range(n_steps_c):
            if (si_c + 1) % EVAL_EVERY == 0:
                if _time.monotonic() - _t_start >= WALL_BUDGET_S:
                    print(f"[R1-D] in-loop budget reached at ctrl step {si_c+1} "
                          f"dt={dt:.2e}")
                    _truncated_ctrl = True
                    break
            cf_c.step(dt)
            if (si_c + 1) % EVAL_EVERY == 0 or si_c == n_steps_c - 1:
                H_c = cf_c.total_energy() + cf_c.kinetic_energy()
                jump_c = abs(H_c - H_prev_c) / max(abs(H0_c), 1e-30)
                if jump_c > 1e-3:
                    n_jump_c += 1
                max_jump_c = max(max_jump_c, jump_c)
                max_rel_c = max(max_rel_c, abs(H_c - H0_c) / max(abs(H0_c), 1e-30))
                H_prev_c = H_c
        rung_elapsed_c = _time.monotonic() - _rung_t0_c
        oy_c = cf_c.omega_yield
        sat_c = int(np.sum(
            np.sum(cf_c.omega[al_c] ** 2, axis=-1) >= (1.0 - 1e-10) * oy_c ** 2
        ))
        print(f"[R1-D control   k_refl=1] omega      dt={dt:.2e} steps={n_steps_c} "
              f"elapsed={rung_elapsed_c:.1f}s "
              f"max|dH/H0|={max_rel_c:.3e} jumps>1e-3={n_jump_c} "
              f"max_step_jump={max_jump_c:.3e} sat_count={sat_c}")
        if _truncated_ctrl:
            break
    print(f"[R1-D] total elapsed {_time.monotonic() - _t_start:.1f}s")
    # NO assertion: K-R18/K-R21 diagnostic record only.


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


def _fit_freq_fft(sig: np.ndarray, dt: float) -> float:
    """Dominant angular frequency of a real signal via Hanning-windowed FFT with
    parabolic peak interpolation (sub-bin accuracy)."""
    sig = sig - np.mean(sig)
    win = np.hanning(len(sig))
    amp = np.abs(np.fft.rfft(sig * win))
    df = np.fft.rfftfreq(len(sig), d=dt)
    amp[0] = 0.0
    k = int(np.argmax(amp))
    if 0 < k < len(amp) - 1:
        a, b, c = amp[k - 1], amp[k], amp[k + 1]
        delta = 0.5 * (a - c) / (a - 2.0 * b + c + 1e-300)
    else:
        delta = 0.0
    bin_hz = df[1] - df[0]
    return 2.0 * np.pi * (k + delta) * bin_hz


def _fit_freq_lsq(sig: np.ndarray, dt: float) -> float:
    """Angular frequency of a near-sinusoidal signal by a 3-parameter
    least-squares fit A·sin(Ω·t + φ) + c0 (B1c C1 — supersedes the FFT-bin
    estimator for the gap-frequency absolute-value gate).

    The FFT+parabolic peak is bin-limited (~2e-3 absolute at the CI run length);
    a continuous nonlinear LS fit recovers Ω to the integrator's own precision,
    letting the measured value be compared against the Verlet-corrected EXACT
    discrete frequency Omega_num = (2/dt)·arcsin(Ω_cont·dt/2) rather than the
    continuum 2.0. The FFT peak seeds the nonlinear solve; curve_fit refines.
    """
    from scipy.optimize import curve_fit

    sig = np.asarray(sig, dtype=float)
    t = np.arange(len(sig), dtype=float) * dt
    c0 = float(np.mean(sig))
    s = sig - c0
    amp0 = float(np.sqrt(2.0 * np.mean(s ** 2))) or 1.0
    w0 = _fit_freq_fft(sig, dt)  # FFT seed for the nonlinear solve
    if w0 <= 0:
        w0 = 2.0 * np.pi / (len(sig) * dt)

    def model(tt, A, w, phi, off):
        return A * np.sin(w * tt + phi) + off

    try:
        popt, _ = curve_fit(
            model, t, sig, p0=[amp0, w0, 0.0, c0],
            maxfev=20000,
        )
        return abs(float(popt[1]))
    except Exception:
        return w0


def _omega_num(omega_cont: float, dt: float) -> float:
    """Velocity-Verlet EXACT discrete angular frequency for a harmonic mode of
    continuum frequency omega_cont integrated at step dt:
      Omega_num = (2/dt)·arcsin(omega_cont·dt/2).
    |Omega_num − omega_cont| = O(dt²) (the symplectic-shadow frequency shift)."""
    return (2.0 / dt) * np.arcsin(omega_cont * dt / 2.0)


def test_k4_dispersion_1e3():
    """K4 vs omega: twist plane-wave FREQUENCY match ≤ 1e-3 at ≥3 k values.

    Spec #5 (ladder R1): single-k small-amplitude (1e-3) twist plane wave,
    frequency fit from the time series (NOT a field-value comparison after a
    fixed step count — the prior test_k4_dispersion_match). The K4 comparison
    quaternion uses the B7-matched convention (q_vec = −ω/2); see _q_from_omega.
    """
    n = 24   # F-nit: 24³ (was 32³) keeps the per-test wall time under the 180 s
             # CI timeout; k₃ = 6π/24 = π/4 is exactly the BZ guard limit.
    dx = 1.0
    amplitude = 1e-3
    # k ≤ π/(4dx) ≈ 0.785; first 3 BZ modes on n=24 are 0.262, 0.524, 0.785.
    k_test = [2 * np.pi / n * m for m in (1, 2, 3)]
    assert all(k <= np.pi / (4 * dx) for k in k_test)

    rel_diffs = []
    for kx in k_test:
        cf_omega = CosseratField3D(
            n, n, n, rotation_storage="omega", pml_thickness=0, damping_gamma=0.0)
        cf_k4 = make_r1_solver(n)  # k_refl=0 read-back asserted (v5)

        xs = np.arange(n) * dx
        omega_seed = np.zeros((n, n, n, 3))
        omega_seed[:, :, :, 2] = amplitude * np.sin(kx * xs[:, None, None])
        cf_omega.omega = omega_seed.copy()
        q_seed = _q_from_omega(omega_seed)
        cf_k4.q = q_seed
        cf_k4.q[~cf_k4.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])

        dt = min(cf_omega.cfl_dt, cf_k4.cfl_dt)
        # ~6 periods of the gap-dominated mode (Ω≈2 → T≈π), capped for CI.
        n_steps = min(int(6 * (2 * np.pi / 2.0) / dt) + 10, 800)

        # Project the ω_z field onto the seeded spatial mode sin(kx·x) — the
        # pure single-frequency oscillator for this k. (A single-site probe can
        # land near a spatial node and pick the wrong FFT peak; the projection
        # is the robust observable.)
        weight = (np.sin(kx * xs[:, None, None]) * np.ones((n, n, n)))[cf_omega.mask_alive]
        om_series = np.zeros(n_steps)
        q_series = np.zeros(n_steps)
        for s in range(n_steps):
            cf_omega.step(dt)
            cf_k4.step(dt)
            om_series[s] = float(np.sum(cf_omega.omega[cf_omega.mask_alive, 2] * weight))
            q_series[s] = float(np.sum(
                cf_k4.q[cf_k4.mask_alive, 3] * 2.0 * _OMEGA_TO_Q_SIGN * weight))

        skip = n_steps // 5
        f_om = _fit_freq_fft(om_series[skip:], dt)
        f_k4 = _fit_freq_fft(q_series[skip:], dt)
        rel = abs(f_k4 - f_om) / f_om if f_om > 0 else abs(f_k4 - f_om)
        rel_diffs.append(rel)

    max_rel = max(rel_diffs)
    assert max_rel <= 1e-3, (
        f"K4 vs omega dispersion: max rel freq diff = {max_rel:.2e} at "
        f"k={k_test!r}; per-k={rel_diffs!r}; limit 1e-3"
    )


# ---------------------------------------------------------------------------
# Force identity: dW/du and dW/dq (→tau) agree with omega engine at 1e-3
# ---------------------------------------------------------------------------


def test_k4_force_amplitude_slope():
    """Force identity slope: |F_K4 − F_ω| ~ O(amplitude²).

    Fit log-log slope across ≥3 amplitudes; assert slope ≈ 2.0 ± 0.4.
    With the B7 objective strain (Rᵀ·F) and the omega-matched q (−ω/2), both
    forms agree with the omega engine at O(θ), so the force difference is the
    O(θ²) residual. (The +ω/2 convention would give slope ≈ 1 — see the B7
    convention note at top of file.)
    """
    n = 16
    rng = np.random.default_rng(42)
    amplitudes = [1e-4, 3e-4, 1e-3, 3e-3]

    diffs = []
    for amplitude in amplitudes:
        u = rng.standard_normal((n, n, n, 3)) * amplitude
        omega = rng.standard_normal((n, n, n, 3)) * amplitude
        cf = CosseratField3D(n, n, n)
        mask_alive = jnp.asarray(cf.mask_alive)

        _, (dW_du_omega, _) = _val_and_grad_saturated(
            jnp.asarray(u), jnp.asarray(omega), mask_alive,
            cf.dx, cf.G, cf.G_c, cf.gamma, cf.omega_yield, cf.epsilon_yield,
            cf.k_op10, cf.k_refl, cf.k_hopf,
        )
        q = _q_from_omega(omega)
        _, (dW_du_k4, _) = _val_and_grad_k4(
            jnp.asarray(u), jnp.asarray(q), mask_alive,
            cf.dx, cf.G, cf.G_c, cf.gamma, cf.omega_yield, cf.epsilon_yield,
            cf.k_op10, cf.k_refl, cf.k_hopf,
        )
        diffs.append(float(jnp.linalg.norm(
            jnp.asarray(dW_du_k4) - jnp.asarray(dW_du_omega))))

    slope, _ = np.polyfit(np.log10(amplitudes),
                          np.log10(np.maximum(diffs, 1e-100)), 1)
    assert abs(slope - 2.0) < 0.4, (
        f"Force diff log-log slope = {slope:.3f} (expected 2.0 ± 0.4); "
        f"amplitudes={amplitudes}, diffs={diffs}"
    )


def test_k4_force_convention_flip_trip():
    """Torque convention flip (right- vs left-trivialized) gives an O(1) relative
    torque difference at FINITE rotation — a Rule-10 trip on the τ=½Im(g⊗q̄)
    convention.

    The two conventions differ by terms ∝ g0·q_vec; near identity (q≈(1,0))
    they degenerate (correctly), so the trip must be exercised at a genuinely
    finite microrotation (|q_vec| ~ O(1)), where the difference is ~1.8× the
    correct torque.
    """
    n = 8
    rng = np.random.default_rng(99)
    # Finite random rotations: small scalar part → large rotation angle.
    q = rng.standard_normal((n, n, n, 4))
    q[..., 0] = np.abs(q[..., 0]) * 0.3
    q /= np.linalg.norm(q, axis=-1, keepdims=True)
    u = rng.standard_normal((n, n, n, 3)) * 0.1

    cf = CosseratField3D(n, n, n)
    mask = jnp.asarray(cf.mask_alive)

    _, (_, dW_dq) = _val_and_grad_k4(
        jnp.asarray(u), jnp.asarray(q), mask,
        cf.dx, cf.G, cf.G_c, cf.gamma, cf.omega_yield, cf.epsilon_yield,
        cf.k_op10, cf.k_refl, cf.k_hopf,
    )
    q_j = jnp.asarray(q)
    g_j = jnp.asarray(dW_dq)
    tau_correct = np.asarray(_left_torque_from_grad(g_j, q_j))

    def right_torque(g, q):
        """Wrong convention: τ'=½Im(q̄⊗g)."""
        g0, g1, g2, g3 = g[..., 0], g[..., 1], g[..., 2], g[..., 3]
        q0, q1, q2, q3 = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
        return jnp.stack([
            0.5 * (q0 * g1 - q1 * g0 - q2 * g3 + q3 * g2),
            0.5 * (q0 * g2 + q1 * g3 - q2 * g0 - q3 * g1),
            0.5 * (q0 * g3 - q1 * g2 + q2 * g1 - q3 * g0),
        ], axis=-1)

    tau_flip = np.asarray(right_torque(g_j, q_j))
    ratio = np.linalg.norm(tau_correct - tau_flip) / max(
        np.linalg.norm(tau_correct), 1e-30)
    assert ratio > 0.5, (
        f"Convention flip should give O(1) relative torque diff; got {ratio:.3e}"
    )


# ---------------------------------------------------------------------------
# B7: strain objectivity (Rᵀ·F is frame-objective; F·R is not)
# ---------------------------------------------------------------------------
# The objectivity property is a tensor identity, independent of the lattice: it
# is tested on CONSTANT (F, R) matrices with the SAME isotropic energy the
# engine uses. A lattice-grid rigid-rotation test would be dominated by the
# tetrahedral-gradient's fixed-axis artifact (the stencil cannot co-rotate with
# the frame), so it CANNOT isolate the R-vs-Rᵀ question — verified at authoring
# time: both forms shift energy by the same O(1) lattice artifact under a 30°
# grid rotation. The constant-matrix test is the lattice-artifact-free witness.

_ISO_ENERGY_G = 1.0
_ISO_ENERGY_GC = 1.0


def _iso_energy(E):
    """The engine's isotropic micropolar energy density on a strain matrix E
    (W_cauchy·G + W_micropolar·G_c at G=G_c=1), matching _energy_density_k4."""
    sym = 0.5 * (E + E.T)
    anti = 0.5 * (E - E.T)
    tr = np.trace(E)
    W_cauchy = (2.0 / 3.0) * tr ** 2 + np.sum(sym ** 2)
    W_micro = np.sum(anti ** 2)
    return _ISO_ENERGY_G * W_cauchy + _ISO_ENERGY_GC * W_micro


def _quat_to_R(q):
    q0, q1, q2, q3 = q
    return np.array([
        [1 - 2 * (q2 ** 2 + q3 ** 2), 2 * (q1 * q2 - q0 * q3), 2 * (q1 * q3 + q0 * q2)],
        [2 * (q1 * q2 + q0 * q3), 1 - 2 * (q1 ** 2 + q3 ** 2), 2 * (q2 * q3 - q0 * q1)],
        [2 * (q1 * q3 - q0 * q2), 2 * (q2 * q3 + q0 * q1), 1 - 2 * (q1 ** 2 + q2 ** 2)],
    ])


def test_strain_objectivity():
    """B7: Rᵀ·F−I is frame-objective; F·R−I is not.

    Under a spatial rigid rotation Q, the microrotation co-rotates (R→Q·R) and
    the deformation gradient transforms (F→Q·F). An OBJECTIVE strain's stored
    energy is invariant. Rᵀ·F−I → (Q·R)ᵀ(Q·F)−I = Rᵀ·F−I (literally invariant);
    F·R−I → Q·F·Q·R−I ≠ Q·(F·R) (not invariant).
    """
    rng = np.random.default_rng(5)
    F = np.eye(3) + 0.15 * rng.standard_normal((3, 3))  # finite deformation
    q = np.array([0.9, 0.2, 0.1, 0.3])
    q = q / np.linalg.norm(q)
    R = _quat_to_R(q)
    th = 0.4
    c, s = np.cos(th), np.sin(th)
    Q = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

    # Rᵀ·F (the engine's B7 form) — objective
    E_rtf = R.T @ F - np.eye(3)
    E_rtf_rot = (Q @ R).T @ (Q @ F) - np.eye(3)
    e0 = _iso_energy(E_rtf)
    e1 = _iso_energy(E_rtf_rot)
    assert abs(e1 - e0) < 1e-8 * max(e0, 1.0), (
        f"Rᵀ·F NOT objective: E0={e0:.6e} E1={e1:.6e}")

    # F·R (the old form) — NOT objective (fails by O(E0))
    E_fr = F @ R - np.eye(3)
    E_fr_rot = (Q @ F) @ (Q @ R) - np.eye(3)
    f0 = _iso_energy(E_fr)
    f1 = _iso_energy(E_fr_rot)
    assert abs(f1 - f0) > 0.01 * f0, (
        f"F·R unexpectedly objective: E0={f0:.6e} E1={f1:.6e}")


def test_strain_small_angle_limit():
    """B7: Rᵀ·F and F·R share the same leading-order strain (difference O(θ)).

    The symmetric-part relative difference scales LINEARLY with amplitude
    (verified: 1.78e-4 / 1.78e-3 / 1.78e-2 at amp 1e-4 / 1e-3 / 1e-2), i.e. the
    two forms agree to leading order and diverge only at the next order — the
    objectivity fix does not change the small-angle physics. The test asserts
    the O(θ) scaling (ratio ≈ constant across amplitudes) rather than a fixed
    tolerance.
    """
    from ave.topological.k4_quaternion import _tetrahedral_gradient
    n = 8
    cf = CosseratField3D(n, n, n)

    def sym_rel(amp):
        rng = np.random.default_rng(11)
        u = rng.standard_normal((n, n, n, 3)) * amp
        omega = rng.standard_normal((n, n, n, 3)) * amp
        q = _q_from_omega(omega)
        eps_rtf = np.asarray(_compute_strain_q_jax(
            jnp.asarray(u), jnp.asarray(q), cf.dx))
        q0, q1, q2, q3 = (q[..., i] for i in range(4))
        R = np.stack([
            np.stack([1 - 2 * (q2 ** 2 + q3 ** 2), 2 * (q1 * q2 - q0 * q3), 2 * (q1 * q3 + q0 * q2)], -1),
            np.stack([2 * (q1 * q2 + q0 * q3), 1 - 2 * (q1 ** 2 + q3 ** 2), 2 * (q2 * q3 - q0 * q1)], -1),
            np.stack([2 * (q1 * q3 - q0 * q2), 2 * (q2 * q3 + q0 * q1), 1 - 2 * (q1 ** 2 + q2 ** 2)], -1),
        ], -2)
        gu = np.asarray(_tetrahedral_gradient(jnp.asarray(u))) / cf.dx
        F = np.broadcast_to(np.eye(3), gu.shape).copy() + gu
        eps_fr = np.einsum("...ik,...kj->...ij", F, R) - np.broadcast_to(np.eye(3), gu.shape)
        s = lambda e: 0.5 * (e + np.swapaxes(e, -1, -2))
        return np.linalg.norm(s(eps_rtf) - s(eps_fr)) / max(np.linalg.norm(s(eps_rtf)), 1e-30)

    r_lo = sym_rel(1e-4)
    r_hi = sym_rel(1e-2)
    # O(θ): a 100× amplitude increase gives a ~100× relative-difference increase.
    assert r_lo < 1e-3, f"small-amp sym diff too large: {r_lo:.2e}"
    assert 50.0 < r_hi / r_lo < 200.0, (
        f"sym strain difference not O(θ): ratio {r_hi / r_lo:.1f} (expect ≈100)")


# ---------------------------------------------------------------------------
# R1-9: objectivity of ε = Rᵀ(q)·F − I (spec A5.3, O1 ruling)
# ---------------------------------------------------------------------------


def _Rq_batch(q):
    """Batch rotation matrices from quaternions, shape (N,3,3)."""
    q0, q1, q2, q3 = q[:, 0], q[:, 1], q[:, 2], q[:, 3]
    return np.stack([
        np.stack([1-2*(q2**2+q3**2), 2*(q1*q2-q0*q3), 2*(q1*q3+q0*q2)], axis=-1),
        np.stack([2*(q1*q2+q0*q3), 1-2*(q1**2+q3**2), 2*(q2*q3-q0*q1)], axis=-1),
        np.stack([2*(q1*q3-q0*q2), 2*(q2*q3+q0*q1), 1-2*(q1**2+q2**2)], axis=-1),
    ], axis=-2)


def _qmul_batch(a, b):
    """Batch quaternion product a⊗b, shape (N,4)."""
    a0, a1, a2, a3 = a[:, 0], a[:, 1], a[:, 2], a[:, 3]
    b0, b1, b2, b3 = b[:, 0], b[:, 1], b[:, 2], b[:, 3]
    return np.stack([
        a0*b0-a1*b1-a2*b2-a3*b3,
        a0*b1+a1*b0+a2*b3-a3*b2,
        a0*b2-a1*b3+a2*b0+a3*b1,
        a0*b3+a1*b2-a2*b1+a3*b0,
    ], axis=-1)


def _n_batch(q):
    """n = R(q)ẑ, shape (N,3)."""
    q0, q1, q2, q3 = q[:, 0], q[:, 1], q[:, 2], q[:, 3]
    return np.stack([
        2*(q1*q3+q0*q2), 2*(q2*q3-q0*q1), 1-2*(q1**2+q2**2),
    ], axis=-1)


def _eps_RtF_batch(F, q):
    """ε = Rᵀ(q)·F − I, shape (N,3,3). O1 form."""
    R = _Rq_batch(q)
    return np.einsum('...ki,...kj->...ij', R, F) - np.eye(3)[None]


def _iso_energy_batch(E):
    """Isotropic K4 pointwise energy (G=G_c=1), shape (N,)."""
    sym = 0.5 * (E + np.swapaxes(E, -1, -2))
    anti = 0.5 * (E - np.swapaxes(E, -1, -2))
    tr = np.trace(E, axis1=-2, axis2=-1)
    W_cauchy = (2.0/3.0) * tr**2 + np.sum(sym**2, axis=(-1, -2))
    W_micro = np.sum(anti**2, axis=(-1, -2))
    return W_cauchy + W_micro


def _iso_energy_W(E):
    """Engine isotropic micropolar energy (G=G_c=1) on a batch of strain (N,3,3)."""
    sym = 0.5 * (E + np.swapaxes(E, -1, -2))
    anti = 0.5 * (E - np.swapaxes(E, -1, -2))
    tr = np.trace(E, axis1=-2, axis2=-1)
    return (2.0 / 3.0) * tr ** 2 + np.sum(sym ** 2, axis=(-1, -2)) + np.sum(anti ** 2, axis=(-1, -2))


def test_r1_9_objectivity():
    """R1-9 (v5, spec A6.2 / A5.3 O1 ruling): objectivity through the PR's OWN functions.

    Everything goes through cf's own code: strain via _pr_strain_batch (which calls
    _compute_strain_q_jax on a linear-u field — the engine stencil, not a copied
    matrix form), director via _q_to_n_jax, and the small-angle ω map via
    omega_eng_from_q / q_from_omega_eng. ≥1000 random cases, rng 20261009,
    ‖∇u‖_F ≤ 0.5. Reports MEDIAN and p99 (not max — robust to the occasional
    ill-conditioned normalization).

    Clauses:
      (a) tensor + energy objectivity under F→QF, q→q_Q·q   (p99 ≤ 1e-11)
      (b) director co-rotation n(q_Q q) = Q n(q)            (p99 ≤ 1e-11)
      (c) small-angle ε vs cf:175-186 through the ω map     (max rel ≤ 3h, h∈{1e-3,1e-6})
      (d) pure rigid rotation F=Q, q=q_Q → ‖ε‖ ≈ 0          (p99 ≤ 1e-11)

    Trips (each must blow up to O(1)):
      · F·R and R·F strain forms (a,d)   — wrong strain tensor transform
      · q̄ k q director (b)                — inverse rotation, breaks co-rotation
      · harness law q·q̄_Q instead of q_Q·q (b) — wrong compounding order
      · dropped ω sign q_from_omega_eng(−ω) (c) — breaks the K-R19 map

    Lattice note: the 90° stencil-symmetry argument (B7) still applies; the
    _pr_strain_batch linear-u trick extracts the center-site strain exactly, so
    no lattice anisotropy contaminates the tensor identity.
    """
    rng = np.random.default_rng(20261009)
    N = 1000

    gu_raw = rng.uniform(-0.5, 0.5, (N, 3, 3))
    fro = np.linalg.norm(gu_raw.reshape(N, 9), axis=-1).reshape(N, 1, 1)
    gu = gu_raw / np.maximum(fro / 0.5, 1.0)   # ‖∇u‖_F ≤ 0.5
    F = np.eye(3)[None] + gu

    q = rng.standard_normal((N, 4)); q /= np.linalg.norm(q, axis=-1, keepdims=True)
    q_Q = rng.standard_normal((N, 4)); q_Q /= np.linalg.norm(q_Q, axis=-1, keepdims=True)
    R_Q = _Rq_batch(q_Q)
    QF = np.einsum('nij,njk->nik', R_Q, F)
    q_Qq = _qmul_batch(q_Q, q)

    def _pct(x):
        return float(np.median(x)), float(np.percentile(x, 99))

    # (a) tensor + energy objectivity (through _pr_strain_batch = cf's strain fn)
    eps = _pr_strain_batch(F, q)
    eps_rot = _pr_strain_batch(QF, q_Qq)
    t_rel = (np.linalg.norm((eps_rot - eps).reshape(N, 9), axis=-1)
             / np.maximum(np.linalg.norm(eps.reshape(N, 9), axis=-1), 1e-30))
    W, W_rot = _iso_energy_W(eps), _iso_energy_W(eps_rot)
    e_rel = np.abs(W_rot - W) / np.maximum(np.abs(W), 1e-6)
    med_t, p99_t = _pct(t_rel); med_e, p99_e = _pct(e_rel)
    print(f"[R1-9a] tensor med={med_t:.2e} p99={p99_t:.2e}  energy med={med_e:.2e} p99={p99_e:.2e}")
    assert p99_t <= 1e-11, f"R1-9(a) tensor p99={p99_t:.2e} (limit 1e-11)"
    assert p99_e <= 1e-11, f"R1-9(a) energy p99={p99_e:.2e} (limit 1e-11)"

    # (b) director co-rotation n(q_Q q) = Q n(q) via _q_to_n_jax (cf's n fn)
    n0 = np.asarray(_q_to_n_jax(jnp.asarray(q)))
    n_rot = np.asarray(_q_to_n_jax(jnp.asarray(q_Qq)))
    Qn = np.einsum('nij,nj->ni', R_Q, n0)
    n_err = np.linalg.norm(n_rot - Qn, axis=-1)
    med_n, p99_n = _pct(n_err)
    print(f"[R1-9b] n co-rotation med={med_n:.2e} p99={p99_n:.2e}")
    assert p99_n <= 1e-11, f"R1-9(b) n co-rotation p99={p99_n:.2e} (limit 1e-11)"

    # (c) small-angle ε vs cf:175-186 through omega_eng_from_q / q_from_omega_eng
    LC = np.zeros((3, 3, 3))
    LC[0, 1, 2] = LC[1, 2, 0] = LC[2, 0, 1] = 1.0
    LC[0, 2, 1] = LC[2, 1, 0] = LC[1, 0, 2] = -1.0
    for h in (1e-3, 1e-6):
        rc = np.random.default_rng(7 + abs(int(round(np.log10(h)))))
        M = 500
        gu_h = rc.standard_normal((M, 3, 3)) * h
        omega_h = rc.standard_normal((M, 3)) * h
        eps_eng = gu_h - np.einsum("ijk,nk->nij", LC, omega_h)   # cf:175-186
        q_h = q_from_omega_eng(omega_h)                          # declared ω map
        eps_k4 = _pr_strain_batch(np.eye(3)[None] + gu_h, q_h)
        denom = np.linalg.norm(eps_eng.reshape(M, 9), axis=-1)
        rel = (np.linalg.norm((eps_k4 - eps_eng).reshape(M, 9), axis=-1)
               / np.maximum(denom, 1e-30))
        max_h = float(np.max(rel))
        print(f"[R1-9c] h={h:.0e} max_rel={max_h:.3e} (limit {3*h:.0e})")
        assert max_h <= 3.0 * h, f"R1-9(c) h={h}: max_rel={max_h:.3e} > 3h={3*h:.3e}"

    # (d) pure rigid rotation F=Q (rotation matrix), q=q_Q → ‖ε‖ ≈ 0
    eps_d = _pr_strain_batch(R_Q, q_Q)
    d_norm = np.linalg.norm(eps_d.reshape(N, 9), axis=-1)
    med_d, p99_d = _pct(d_norm)
    print(f"[R1-9d] rigid med={med_d:.2e} p99={p99_d:.2e}")
    assert p99_d <= 1e-11, f"R1-9(d) rigid p99={p99_d:.2e} (limit 1e-11)"

    # ---- TRIPS ----
    # F·R and R·F forms (wrong strain transform) — must fail (a,d).
    def _eps_FR(Fs, qs):
        return np.einsum('nij,njk->nik', Fs, _Rq_batch(qs)) - np.eye(3)[None]

    def _eps_RF(Fs, qs):
        return np.einsum('nij,njk->nik', _Rq_batch(qs), Fs) - np.eye(3)[None]

    for name, fn, e_lim in (("FR", _eps_FR, 0.1), ("RF", _eps_RF, 0.1)):
        e0 = fn(F, q); e1 = fn(QF, q_Qq)
        tt = (np.linalg.norm((e1 - e0).reshape(N, 9), axis=-1)
              / np.maximum(np.linalg.norm(e0.reshape(N, 9), axis=-1), 1e-30))
        ee = np.abs(_iso_energy_W(e1) - _iso_energy_W(e0)) / np.maximum(np.abs(_iso_energy_W(e0)), 1e-6)
        mt, pt = _pct(tt); me, pe = _pct(ee)
        print(f"[R1-9 {name} trip] tensor med={mt:.2f} p99={pt:.2f}  energy med={me:.2f} p99={pe:.2f}")
        assert pt > e_lim, f"R1-9 {name} tensor trip: p99={pt:.3f} (must > {e_lim})"
        assert pe > e_lim, f"R1-9 {name} energy trip: p99={pe:.3f} (must > {e_lim})"

    # q̄ k q director (inverse rotation = R(q)ᵀ ẑ) — breaks co-rotation (b).
    def _n_qbar_k_q(qq):
        q0, q1, q2, q3 = qq[:, 0], qq[:, 1], qq[:, 2], qq[:, 3]
        return np.stack([
            2 * (q1 * q3 - q0 * q2), 2 * (q2 * q3 + q0 * q1), 1 - 2 * (q1 ** 2 + q2 ** 2),
        ], axis=-1)

    nw = _n_qbar_k_q(q); nw_rot = _n_qbar_k_q(q_Qq)
    nw_err = np.linalg.norm(nw_rot - np.einsum('nij,nj->ni', R_Q, nw), axis=-1)
    _, p99_nw = _pct(nw_err)
    print(f"[R1-9 q̄kq trip] n p99={p99_nw:.2f}")
    assert p99_nw > 0.1, f"R1-9 q̄kq trip: p99={p99_nw:.3f} (must > 0.1)"

    # Harness law q·q̄_Q instead of q_Q·q (wrong compounding order) — breaks (b).
    q_conj_Q = q_Q * np.array([[1.0, -1.0, -1.0, -1.0]])
    q_bad = _qmul_batch(q, q_conj_Q)
    n_bad = np.asarray(_q_to_n_jax(jnp.asarray(q_bad)))
    il_err = np.linalg.norm(n_bad - np.einsum('nij,nj->ni', R_Q, n0), axis=-1)
    _, p99_il = _pct(il_err)
    print(f"[R1-9 harness-law trip] n p99={p99_il:.2f}")
    assert p99_il > 0.1, f"R1-9 harness-law trip: p99={p99_il:.3f} (must > 0.1)"

    # Dropped ω sign: q_from_omega_eng(−ω) instead of (+ω) — breaks the K-R19 map (c).
    rc2 = np.random.default_rng(7 + 3)
    M = 500; h = 1e-3
    gu_s = rc2.standard_normal((M, 3, 3)) * h
    omega_s = rc2.standard_normal((M, 3)) * h
    eps_eng_s = gu_s - np.einsum("ijk,nk->nij", LC, omega_s)
    q_wrong = q_from_omega_eng(-omega_s)   # wrong sign
    eps_wrong = _pr_strain_batch(np.eye(3)[None] + gu_s, q_wrong)
    rel_w = (np.linalg.norm((eps_wrong - eps_eng_s).reshape(M, 9), axis=-1)
             / np.maximum(np.linalg.norm(eps_eng_s.reshape(M, 9), axis=-1), 1e-30))
    max_w = float(np.max(rel_w))
    print(f"[R1-9 dropped-sign trip] h={h} max_rel={max_w:.3f}")
    assert max_w > 0.1, f"R1-9 dropped-sign trip: {max_w:.3f} (must > 0.1)"


def test_k4_strain_small_angle_omega_map():
    """O1 ruling: ε = Rᵀ(q)·F − I matches cf:175-186 to O(h) under the ω map.

    Rewritten (v5) to go through the PR's own _compute_strain_q_jax (via
    _pr_strain_batch) and q_from_omega_eng, NOT a reimplemented matrix form. At
    h=1e-6 the max relative strain error is ≤ 3e-6 (strain_ruling.py ~2.8e-6,
    reproduced here = 2.515e-6). The ω map is q(ω_eng) = exp(−ω/2) (K-R19).
    """
    rng = np.random.default_rng(20261009)
    N = 2000
    h = 1e-6
    gu = rng.standard_normal((N, 3, 3)) * h
    omega = rng.standard_normal((N, 3)) * h

    LC = np.zeros((3, 3, 3))
    LC[0, 1, 2] = LC[1, 2, 0] = LC[2, 0, 1] = 1.0
    LC[0, 2, 1] = LC[2, 1, 0] = LC[1, 0, 2] = -1.0
    eps_engine = gu - np.einsum("ijk,nk->nij", LC, omega)   # cf:175-186

    q = q_from_omega_eng(omega)                             # declared ω map
    eps_k4 = _pr_strain_batch(np.eye(3)[None] + gu, q)      # cf's strain fn

    norms = np.linalg.norm(eps_engine.reshape(N, 9), axis=-1)
    rel = (np.linalg.norm((eps_k4 - eps_engine).reshape(N, 9), axis=-1)
           / np.maximum(norms, 1e-30))
    max_rel = float(np.max(rel))
    print(f"[strain_small_angle] h={h:.0e} max_rel={max_rel:.3e}")
    assert max_rel <= 3e-6, (
        f"small-angle strain vs cf:175-186 under ω map: max_rel={max_rel:.2e} "
        f"(limit 3e-6; strain_ruling h=1e-6 gives ~2.8e-6)")


# ---------------------------------------------------------------------------
# B2: ω-storage representation jump (static convention witness)
# ---------------------------------------------------------------------------
# The former dynamic q→−1 k_refl=1 asserting test (test_k4_q_reaches_minus1_
# dynamic) is retired; its |q|=1 invariant is covered by the norm-preservation
# tests and its k_refl=1 bond behavior is logged in test_r1_d_krefl1_log_only
# (K-R21). The static representation-jump witness below is convention-level.


def test_omega_storage_representation_jump():
    """B2: ω-storage shows an O(2π) bond discontinuity where K4 shows O(small).

    Neighboring sites holding q and −q represent the SAME physical rotation.
    In ω-storage (ω = 2·arccos(q0)·q⃗/|q⃗|) they differ by ≈2π (the double-cover
    seam). In K4 the short-arc bond log q̄⊗q′ flips the sign (q̄⊗(−q)=(−1,0,0,0)
    → short-arc → identity), so the bond log is ≈0. This is the representation
    trip the K4 storage removes.
    """
    n = 16
    q_val = np.array([0.05, 0.0, 0.0, 0.9987])
    q_val = q_val / np.linalg.norm(q_val)

    cf = CosseratField3D(n, n, n, rotation_storage="quaternion")
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if cf.mask_alive[i, j, k]:
                    cf.q[i, j, k] = q_val if ((i + j + k) % 8 < 4) else -q_val

    q = cf.q
    q0s = q[..., 0:1]
    q_vecs = q[..., 1:]
    theta_half = np.arccos(np.clip(q0s, -1 + 1e-10, 1 - 1e-10))
    norms = np.linalg.norm(q_vecs, axis=-1, keepdims=True)
    omega_rep = np.where(norms > 1e-10,
                         2.0 * theta_half * q_vecs / np.maximum(norms, 1e-30),
                         np.zeros_like(q_vecs))

    q_conj = q * np.array([1.0, -1.0, -1.0, -1.0])
    max_delta_omega = 0.0
    max_k4_log = 0.0
    alive = cf.mask_alive
    for (di, dj, dk) in TETRA_OFFSETS:
        q_sh = np.roll(np.roll(np.roll(q, -di, 0), -dj, 1), -dk, 2)
        om_sh = np.roll(np.roll(np.roll(omega_rep, -di, 0), -dj, 1), -dk, 2)
        d_om = np.linalg.norm(om_sh - omega_rep, axis=-1)
        max_delta_omega = max(max_delta_omega, float(d_om[alive].max()))

        prod = _quat_mul_np(q_conj, q_sh)
        prod = np.where(prod[..., 0:1] >= 0, prod, -prod)
        vec = prod[..., 1:]
        q0h = prod[..., 0:1]
        vn = np.linalg.norm(vec, axis=-1, keepdims=True)
        theta = np.arctan2(vn, q0h)
        k4_log = 2.0 * theta * np.where(vn > 1e-20, vec / np.maximum(vn, 1e-30), vec)
        k4_log_norm = np.linalg.norm(k4_log, axis=-1)
        max_k4_log = max(max_k4_log, float(k4_log_norm[alive].max()))

    assert max_delta_omega > np.pi, (
        f"ω-storage bond |Δω| = {max_delta_omega:.3f}, expected O(2π)")
    assert max_k4_log < 0.1, (
        f"K4 bond log = {max_k4_log:.3f}, expected O(small)")


# ---------------------------------------------------------------------------
# B6: 12 translation zero modes (ladder R1 line 6)
# ---------------------------------------------------------------------------
# The BCC alive set splits into 4 translation classes by site parity. A rigid
# shift of u on one class (one axis) leaves the K4 total energy unchanged → 12
# (4 classes × 3 axes) exact zero modes of the translation sector. The body-force
# trip injects a point force into the gradient at one class-0 site and verifies
# the per-class force sum localizes to class 0.


def _bcc_translation_classes(n, alive):
    """4 BCC translation-class labels (−1 off-lattice). Spec (ladder R1 line 6):
    even i → ((i+j+k)//2)%2;  odd i → 2 + ((i+j+k−3)//2)%2."""
    i, j, k = np.indices((n, n, n))
    even = (i % 2 == 0)
    cls = np.where(even, ((i + j + k) // 2) % 2, 2 + ((i + j + k - 3) // 2) % 2)
    return np.where(alive, cls, -1)


def test_k4_translation_zero_modes():
    """B6 (ladder R1 line 6): 12 translation zero modes of the K4 energy.

    A rigid shift of u restricted to ONE of the 4 BCC translation classes, along
    ONE axis, leaves the K4 total energy invariant — 12 exact zero modes.
    Measured: all 12 relative energy changes ≤ 1e-12 (actually ≤ ~4e-16, i.e.
    machine zero). Per-class force sums (−dE/du summed over a class) vanish to
    ≤1e-12. Body-force trip: injecting a point force f0 into the gradient at one
    class-0 site localizes the class-0 force sum to exactly that force while the
    other three classes stay ≈0.
    """
    n = 24
    cf = make_r1_solver(n)
    alive = cf.mask_alive
    cls = _bcc_translation_classes(n, alive)

    rng = np.random.default_rng(20261010)
    u = rng.standard_normal((n, n, n, 3)) * 1e-2
    q = np.zeros((n, n, n, 4))
    q[..., 0] = 1.0
    q[..., 1:] = rng.standard_normal((n, n, n, 3)) * 1e-3
    q = q / np.linalg.norm(q, axis=-1, keepdims=True)
    u[~alive] = 0.0
    q[~alive] = np.array([1.0, 0.0, 0.0, 0.0])

    args = (cf.dx, cf.G, cf.G_c, cf.gamma, cf.omega_yield, cf.epsilon_yield,
            cf.k_op10, cf.k_refl, cf.k_hopf)

    def E(u_):
        return float(_total_energy_k4_jit(
            jnp.asarray(u_), jnp.asarray(q), cf._mask_alive_jax, *args))

    E0 = E(u)
    assert abs(E0) > 1e-12, f"baseline energy too small: {E0:.2e}"
    delta = 1e-4

    mode_means = []
    for c in range(4):
        mask = (cls == c) & alive
        for ax in range(3):
            u_sh = u.copy()
            u_sh[mask, ax] += delta
            rel = abs(E(u_sh) - E0) / max(abs(E0), 1e-12)
            mode_means.append(rel)
            assert rel <= 1e-12, (
                f"translation zero mode (class {c}, axis {ax}) not flat: "
                f"relE={rel:.2e} (limit 1e-12)")
    print(f"[zero_modes:K4] 12 relative energy changes = "
          f"{['%.1e' % m for m in mode_means]}")

    # Per-class force sums vanish (translation invariance ⇒ zero net force per
    # class, per axis).
    _, (dW_du, _) = _val_and_grad_k4(
        jnp.asarray(u), jnp.asarray(q), cf._mask_alive_jax, *args)
    force = -np.asarray(dW_du)
    fnorm = float(np.linalg.norm(force))
    for c in range(4):
        mask = (cls == c) & alive
        for ax in range(3):
            s = abs(float(force[mask, ax].sum())) / max(fnorm, 1e-12)
            assert s <= 1e-12, (
                f"class {c} axis {ax} net force not zero: {s:.2e} (limit 1e-12)")

    # Body-force trip: subtract f0 from the gradient at ONE class-0 site. Since
    # force = −grad, the class-0 force sum picks up EXACTLY +f0 (the −f0 the spec
    # quotes is the GRADIENT change; the force sum is its negative). Other
    # classes stay ≈0.
    f0 = np.array([0.0, 0.0, 1e-2])
    grad = np.array(dW_du)  # writable copy
    idx = tuple(np.argwhere((cls == 0) & alive)[0])
    grad[idx] -= f0
    force_trip = -grad
    sum0 = np.array([force_trip[(cls == 0) & alive, ax].sum() for ax in range(3)])
    assert np.linalg.norm(sum0 - f0) <= 1e-12, (
        f"class-0 body-force sum = {sum0} should equal +f0={f0} "
        f"(−f0 is the gradient change); |Δ|={np.linalg.norm(sum0 - f0):.2e}")
    for c in (1, 2, 3):
        mask = (cls == c) & alive
        s = np.array([force_trip[mask, ax].sum() for ax in range(3)])
        assert np.linalg.norm(s) <= 1e-12, (
            f"class {c} force sum should stay ≈0 under class-0 trip: {s}")


def test_omega_translation_zero_modes():
    """B6 reference check: the ω engine has the same 12 translation zero modes.

    Same setup as test_k4_translation_zero_modes but through _val_and_grad_saturated
    (the ω storage path). Confirms the zero-mode structure is a property of the
    translation sector, not of the quaternion representation.
    """
    n = 24
    cf = CosseratField3D(n, n, n, pml_thickness=0, damping_gamma=0.0)
    alive = cf.mask_alive
    cls = _bcc_translation_classes(n, alive)

    rng = np.random.default_rng(20261010)
    u = rng.standard_normal((n, n, n, 3)) * 1e-2
    omega = rng.standard_normal((n, n, n, 3)) * 1e-3
    u[~alive] = 0.0
    omega[~alive] = 0.0

    args = (cf.dx, cf.G, cf.G_c, cf.gamma, cf.omega_yield, cf.epsilon_yield,
            cf.k_op10, cf.k_refl, cf.k_hopf)

    def E(u_):
        val, _ = _val_and_grad_saturated(
            jnp.asarray(u_), jnp.asarray(omega), cf._mask_alive_jax, *args)
        return float(val)

    E0 = E(u)
    assert abs(E0) > 1e-12, f"baseline energy too small: {E0:.2e}"
    delta = 1e-4

    mode_means = []
    for c in range(4):
        mask = (cls == c) & alive
        for ax in range(3):
            u_sh = u.copy()
            u_sh[mask, ax] += delta
            rel = abs(E(u_sh) - E0) / max(abs(E0), 1e-12)
            mode_means.append(rel)
            assert rel <= 1e-12, (
                f"ω translation zero mode (class {c}, axis {ax}) not flat: "
                f"relE={rel:.2e} (limit 1e-12)")
    print(f"[zero_modes:omega] 12 relative energy changes = "
          f"{['%.1e' % m for m in mode_means]}")


# ---------------------------------------------------------------------------
# B6: k=0 gap frequency + G_c=0 trip + energy drift + _energy_slope helper
# ---------------------------------------------------------------------------


def _gap_freq(cf, storage, amplitude=1e-3, n_periods=40, dt_override=None):
    """Drive the k=0 uniform z-rotation gap mode; return (angular frequency, dt).

    B1c C1: the frequency is now recovered by a 3-parameter least-squares
    sinusoid fit (_fit_freq_lsq) over ≥10 periods, not an FFT-bin peak — so the
    absolute value can be gated against the Verlet-corrected discrete frequency.
    Only the running scalar mean is held (no full field time series) to keep the
    RSS footprint flat (C5).

    dt_override (F8): run at an explicit dt instead of cfl_dt, so the Verlet
    shadow-frequency offset ratio off(dt)/off(dt/4) can be MEASURED from two
    engine runs rather than computed analytically from the continuum 2.0."""
    if storage == "omega":
        cf.omega[:, :, :, 2] = amplitude
    else:
        cf.q[:, :, :, 0] = np.sqrt(1.0 - (amplitude / 2.0) ** 2)
        cf.q[:, :, :, 3] = amplitude / 2.0
        cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
    dt = dt_override if dt_override is not None else cf.cfl_dt
    n_steps = int(n_periods * (2.0 * np.pi / 2.0) / dt) + 1
    series = np.zeros(n_steps)
    for s in range(n_steps):
        cf.step(dt)
        if storage == "omega":
            series[s] = float(np.mean(cf.omega[cf.mask_alive, 2]))
        else:
            series[s] = float(np.mean(cf.q[cf.mask_alive, 3])) * 2.0
    return _fit_freq_lsq(series[n_steps // 5:], dt), dt


def test_k4_gap_frequency():
    """B6: k=0 uniform-rotation gap frequency matches the Verlet-corrected exact
    discrete frequency to ≤1e-4 AND K4 == omega to <1e-4 (B1c C1).

    Derivation (spec §1 K4, ladder R1): W_micropolar = G_c|ε_antisym|² = 2G_c|ω|²;
    I_ω·ω̈ = −4G_c·ω → Ω_gap² = 4G_c/I_ω = 4 → Ω_gap(continuum) = 2.

    The velocity-Verlet integrator does NOT reproduce the continuum 2.0 exactly:
    a harmonic mode of continuum frequency Ω integrated at step dt oscillates at
    the EXACT discrete frequency Omega_num = (2/dt)·arcsin(Ω·dt/2), with
    |Omega_num − 2| = O(dt²). Measuring the gap frequency by a least-squares
    sinusoid fit (not an FFT-bin peak) recovers Ω to integrator precision, so the
    correct comparison is measured-vs-Omega_num (≤1e-4), NOT measured-vs-2.0. The
    O(dt²) nature of the 2.0 offset is itself verified by a MEASURED (not
    analytic) frequency-offset ratio: fit f(dt) and f(dt/4) from two engine runs,
    off = f − 2, and assert off(dt)/off(dt/4) ∈ [15, 17.5] (Gate: 16.31 ω). This
    ratio exercises the ENGINE at two step sizes, so a coefficient edit that
    shifts the actual frequency (e.g. γ×2 in W_micropolar) is caught here as well
    as by the |f_ω − Omega_num| ≤ 1e-4 clause. k_refl=0 cf_k4 via make_r1_solver.
    """
    cf_om = CosseratField3D(16, 16, 16, rotation_storage="omega",
                            pml_thickness=0, damping_gamma=0.0)
    cf_k4 = make_r1_solver(16)  # k_refl=0 read-back asserted (v5)
    f_om, dt_om = _gap_freq(cf_om, "omega")
    f_k4, dt_k4 = _gap_freq(cf_k4, "quaternion")

    # Verlet-corrected exact discrete frequency at the dt the omega run used.
    Omega_num = _omega_num(2.0, dt_om)

    assert abs(f_k4 - f_om) / max(f_om, 1e-30) < 1e-4, (
        f"K4 vs omega gap freq diverge: f_k4={f_k4:.6f} f_om={f_om:.6f}")
    assert abs(f_om - Omega_num) <= 1e-4, (
        f"gap frequency = {f_om:.6f} vs Verlet-exact Omega_num = {Omega_num:.6f} "
        f"(|Δ|={abs(f_om - Omega_num):.2e}, limit 1e-4; dt={dt_om:.6e})")

    # F8: MEASURED Verlet shadow-offset ratio off(dt)/off(dt/4). Second engine run
    # at dt/4 (n_periods=10 → same step count as the dt run). off = f_measured − 2;
    # the O(dt²) shadow shift gives off(dt)/off(dt/4) = 4² = 16 (Gate: 16.31).
    cf_om_dt4 = CosseratField3D(16, 16, 16, rotation_storage="omega",
                                pml_thickness=0, damping_gamma=0.0)
    f_om_dt4, _ = _gap_freq(cf_om_dt4, "omega", n_periods=10, dt_override=dt_om / 4.0)
    off_dt = abs(f_om - 2.0)
    off_dt4 = abs(f_om_dt4 - 2.0)
    ratio_dt = off_dt / max(off_dt4, 1e-300)
    print(f"[gap] f_om={f_om:.6f} f_k4={f_k4:.6f} off(dt)={off_dt:.3e} "
          f"off(dt/4)={off_dt4:.3e} measured ratio={ratio_dt:.2f}")
    assert 15.0 <= ratio_dt <= 17.5, (
        f"measured Verlet offset not O(dt²): off(dt)={off_dt:.3e} "
        f"off(dt/4)={off_dt4:.3e} ratio={ratio_dt:.2f} (expect ∈ [15, 17.5]; "
        f"Gate 16.31)")


def test_k4_gap_frequency_trip_gc0():
    """B6 trip: G_c = 0 → gap frequency collapses toward 0 (no restoring torque)."""
    cf = make_r1_solver(16)
    cf.G_c = 0.0
    f, _dt = _gap_freq(cf, "quaternion", n_periods=10)
    assert f < 0.5, f"G_c=0 gap trip: frequency = {f:.4f}, expected < 0.5 (≈0)"


def test_k4_energy_drift():
    """R1-4 (v6): MAX-over-T=2π |ΔH/H0| ≤ 1e-4 at cfl/16; dt×4 must EXCEED 1e-4.

    Fixed physical window T=2π: n_steps = ceil(2π/dt); assert n_steps·dt ≥ 2π.
    The drift metric is the MAXIMUM over the whole trajectory (not end-point value).
    Gate: 5.15e-5 at cfl/16 (1060 steps); 8.2e-4 at cfl/4 (265 steps).

    Mutants: dt_x4 (replaces dt_fine with dt_coarse; trips the ≤1e-4 pass);
             fixed_50_steps (sets n_steps=50 instead of ceil(2π/dt); trips the
             `assert n_steps*dt >= 2π` readback before any physics runs).

    k_refl=0 via make_r1_solver (v6 rule).
    """
    n = 16
    cfl_dt = make_r1_solver(n).cfl_dt
    dt_fine = cfl_dt / 16.0    # named dt (passes)
    dt_coarse = cfl_dt / 4.0   # dt_fine × 4 (must trip)

    def drift_max(dt):
        n_steps = int(np.ceil(2.0 * np.pi / dt))
        assert n_steps * dt >= 2.0 * np.pi, (   # fixed_50_steps mutant trips here
            f"drift_max: n_steps*dt={n_steps*dt:.6f} < 2π={2*np.pi:.6f}")
        cf = make_r1_solver(n)
        rng = np.random.default_rng(2026)
        dq = rng.standard_normal((n, n, n, 3)) * 1e-3
        cf.q[cf.mask_alive, 1:] = dq[cf.mask_alive]
        norms = np.linalg.norm(cf.q, axis=-1, keepdims=True)
        cf.q = cf.q / np.where(norms > 0, norms, 1.0)
        cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
        H0 = cf.total_energy_k4() + cf.kinetic_energy_k4()
        if abs(H0) < 1e-20:
            pytest.skip("Initial energy too small for drift test")
        max_rel = 0.0
        for _ in range(n_steps):
            cf.step(dt)
            H = cf.total_energy_k4() + cf.kinetic_energy_k4()
            max_rel = max(max_rel, abs(H - H0) / abs(H0))
        return max_rel

    rel_fine = drift_max(dt_fine)
    rel_coarse = drift_max(dt_coarse)
    print(f"[energy_drift] cfl/16={dt_fine:.3e} n={int(np.ceil(2*np.pi/dt_fine))} "
          f"max|ΔH/H0|={rel_fine:.3e}  "
          f"cfl/4={dt_coarse:.3e} n={int(np.ceil(2*np.pi/dt_coarse))} "
          f"max|ΔH/H0|={rel_coarse:.3e}")

    # PASS at the named dt (Gate: 5.15e-5).
    assert rel_fine <= 1e-4, (
        f"max|ΔH/H0| = {rel_fine:.2e} at cfl/16={dt_fine:.3e} (limit 1e-4, Gate: 5.15e-5)")

    # REAL TRIP: dt×4 = cfl/4 must EXCEED 1e-4 (Gate: 8.2e-4).
    assert rel_coarse > 1e-4, (
        f"dt×4 trip did not fire: cfl/4 max|ΔH/H0| = {rel_coarse:.2e} ≤ 1e-4 "
        f"(Gate: 8.2e-4). If the integrator now conserves this well at cfl/4, "
        f"pick the smallest named dt whose ×4 exceeds 1e-4, with numbers.")


def test_energy_slope_helper_none_when_few_samples():
    """B6: _energy_slope returns None when < 101 samples → INCONCLUSIVE."""
    assert _energy_slope(list(range(50))) is None


def test_energy_slope_helper_returns_value_when_enough():
    """B6: _energy_slope returns a float when ≥ 101 samples."""
    energies = [1.0 * np.exp(-i * 0.001) for i in range(110)]
    slope = _energy_slope(energies)
    assert slope is not None and isinstance(slope, float)


# ---------------------------------------------------------------------------
# B8: k_refl = 0 contributes zero reflection energy (linearity in k_refl)
# ---------------------------------------------------------------------------


def test_k4_krefl0_zero_reflection_energy():
    """B8: the reflection term is linear in k_refl and k_refl=0 removes it.

    W = … + k_refl·Σ W_refl + …, so E(k_refl) is affine in k_refl: verify
    E(2) = E(0) + 2·(E(1)−E(0)) exactly (the reflection contribution scales
    linearly), and E(1) ≥ E(0) (W_refl ≥ 0), i.e. k_refl=0 contributes zero.
    """
    n = 8
    rng = np.random.default_rng(42)
    u = rng.standard_normal((n, n, n, 3)) * 0.1
    omega = rng.standard_normal((n, n, n, 3)) * 0.1

    cf = CosseratField3D(n, n, n)
    mask = jnp.asarray(cf.mask_alive)
    q = _q_from_omega(omega)

    def k4_energy(k_refl):
        return float(jnp.sum(_energy_density_k4_saturated(
            jnp.asarray(u), jnp.asarray(q), mask, cf.dx,
            cf.G, cf.G_c, cf.gamma, cf.omega_yield, cf.epsilon_yield,
            k_op10=0.0, k_refl=float(k_refl), k_hopf=0.0,
        )))

    E0, E1, E2 = k4_energy(0.0), k4_energy(1.0), k4_energy(2.0)
    assert abs(E2 - (E0 + 2.0 * (E1 - E0))) < 1e-9 * max(abs(E2), 1e-9), (
        f"k_refl energy not linear: E0={E0:.6e} E1={E1:.6e} E2={E2:.6e}")
    assert E1 >= E0, f"E(k_refl=1)={E1:.4e} should be ≥ E(k_refl=0)={E0:.4e}"


# ---------------------------------------------------------------------------
# B9: R2 harness aggregator verdict logic (ladder §5 R2 #7)
# ---------------------------------------------------------------------------


def _agg():
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import aggregate_r2_periods
    return aggregate_r2_periods


def _res(value):
    """count_charge_k4-shaped RESOLVED result dict with the given integer value."""
    return {'resolved': True, 'value': value, 'reason': None,
            'c_exact_result': {'value': value}, 'c_link_result': {'value': value}}


def _unres(reason, c_link_value=None):
    """count_charge_k4-shaped UNRESOLVED result dict."""
    clk = {'value': c_link_value} if c_link_value is not None else None
    return {'resolved': False, 'value': None, 'reason': reason,
            'c_exact_result': None, 'c_link_result': clk}


def test_r2_aggregator_pass():
    """B9: ≥90% resolved + all +6 → PASS (adapter-dict format, F4)."""
    agg = _agg()
    periods = [_res(6) for _ in range(18)] + [_unres('NONUNIT: …') for _ in range(2)]
    out = agg(periods, expected_periods=20)
    assert out['verdict'] == 'PASS', out


def test_r2_aggregator_inconclusive():
    """B9: 17/20 resolved (<90%) → INCONCLUSIVE (adapter-dict format, F4)."""
    agg = _agg()
    periods = [_res(6) for _ in range(17)] + \
              [_unres('UNRESOLVED: c_exact BAD_TETS', c_link_value=7) for _ in range(3)]
    out = agg(periods, expected_periods=20)
    assert out['verdict'] == 'INCONCLUSIVE', out
    # Nit N3: the c_link value is logged on each UNRESOLVED period.
    assert any('c_link=7' in note for note in out['notes']), out['notes']


def test_r2_aggregator_fail():
    """B9: one resolved value ≠ +6 → FAIL (the only count FAIL)."""
    agg = _agg()
    periods = [_res(6) for _ in range(19)] + [_res(5)]
    out = agg(periods, expected_periods=20)
    assert out['verdict'] == 'FAIL', out


def test_r2_aggregator_clink_disagree_unresolved():
    """F4: c_exact=6 but c_link=5 (disagree) → adapter resolved=False → UNRESOLVED.

    Kills agg_clink_ignored: the old `ce!=6 or cl!=6` made a c_link-only
    disagreement a FAIL. The adapter returns resolved=False on disagreement, so
    the aggregator counts it UNRESOLVED (INCONCLUSIVE, not FAIL).
    """
    agg = _agg()
    disagree = _unres('UNRESOLVED: c_exact=6 disagrees with c_link=5', c_link_value=5)
    # Enough disagreements to drop below 90% resolved → INCONCLUSIVE, never FAIL.
    periods = [_res(6) for _ in range(17)] + [disagree for _ in range(3)]
    out = agg(periods, expected_periods=20)
    assert out['verdict'] == 'INCONCLUSIVE', out
    assert out['n_wrong'] == 0, (
        f"a c_link disagreement must NOT be a COUNT FAIL (n_wrong={out['n_wrong']})")
    assert out['n_unresolved'] == 3, out


def test_r2_aggregator_nan_period():
    """F4: a NONFINITE period → UNRESOLVED → drives the verdict."""
    agg = _agg()
    periods = [_res(6) for _ in range(17)] + \
              [_unres('NONFINITE: non-finite q on alive sites') for _ in range(3)]
    out = agg(periods, expected_periods=20)
    assert out['verdict'] == 'INCONCLUSIVE', out


def test_r2_aggregator_nonunit_period():
    """F4: a NONUNIT period → UNRESOLVED → drives the verdict."""
    agg = _agg()
    periods = [_res(6) for _ in range(17)] + \
              [_unres('NONUNIT: alive sites deviate from unit norm by 1.0e-02 (> 1e-6)')
               for _ in range(3)]
    out = agg(periods, expected_periods=20)
    assert out['verdict'] == 'INCONCLUSIVE', out


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
# D1: charge_counters_pin.json blob sha1 integrity (Gate C1)
# ---------------------------------------------------------------------------


def _charge_counters_blob_sha1() -> str:
    """Compute git blob sha1 of charge_counters.py in pure Python.
    git blob sha1: sha1(b"blob <len>\\0" + data)
    """
    import hashlib
    import os
    pin_dir = os.path.join(os.path.dirname(__file__),
                           '..', 'ave', 'topological')
    path = os.path.normpath(os.path.join(pin_dir, 'charge_counters.py'))
    with open(path, 'rb') as f:
        data = f.read()
    header = b"blob %d\0" % len(data)
    return hashlib.sha1(header + data).hexdigest()


def test_charge_counters_pin_blob_sha1():
    """D1 (Gate C1): charge_counters.py blob sha1 matches pin file.

    Prevents silent modification of charge_counters.py after the
    CONDITIONAL PASS gate at d2c7da09 (blob b0384af0ca7e…). Any edit
    voids the P1 pin; this test trips before the R2 run can proceed.
    """
    import json
    import os
    pin_dir = os.path.join(os.path.dirname(__file__),
                           '..', 'ave', 'topological')
    pin_path = os.path.normpath(os.path.join(pin_dir, 'charge_counters_pin.json'))
    with open(pin_path) as f:
        pin = json.load(f)
    expected = pin['blob_sha1']
    actual = _charge_counters_blob_sha1()
    assert actual == expected, (
        f"charge_counters.py has been modified since the Gate CONDITIONAL PASS "
        f"(d2c7da09). Expected blob sha1 {expected}, got {actual}. "
        "Any edit to charge_counters.py voids the pin. Update the pin file and "
        "re-run the Gate audit before proceeding.")


def test_charge_counters_pin_mutation_trip():
    """D1: a one-byte-mutated copy of charge_counters.py does NOT match the pin."""
    import hashlib
    import json
    import os
    pin_dir = os.path.join(os.path.dirname(__file__),
                           '..', 'ave', 'topological')
    path = os.path.normpath(os.path.join(pin_dir, 'charge_counters.py'))
    pin_path = os.path.normpath(os.path.join(pin_dir, 'charge_counters_pin.json'))
    with open(path, 'rb') as f:
        data = f.read()
    with open(pin_path) as f:
        pin = json.load(f)
    expected = pin['blob_sha1']
    # Mutate one byte
    mutated = bytearray(data)
    mutated[0] ^= 0x01
    mutated = bytes(mutated)
    header = b"blob %d\0" % len(mutated)
    mutated_sha = hashlib.sha1(header + mutated).hexdigest()
    assert mutated_sha != expected, (
        "Mutation trip failed: one-byte mutant produced the same blob sha1 — "
        "this should be impossible (sha1 collision).")


def test_r2_config_pin_refusal(tmp_path, monkeypatch):
    """D1: make_r2_solver raises RuntimeError when pin sha1 mismatches.

    Writes a pin file with a wrong blob_sha1 to tmp_path and patches
    csk4_r2_config._PIN_FILE to point there. Confirms the solver refuses.
    """
    import json
    import sys
    import os
    # Ensure csk4_r2_config is importable
    scripts_dir = os.path.join(os.path.dirname(__file__),
                               '..', 'scripts', 'vol_4_engineering')
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import importlib
    import csk4_r2_config
    importlib.reload(csk4_r2_config)

    bad_pin = {
        "path": "src/ave/topological/charge_counters.py",
        "commit": "d2c7da092f1a0577ab725b8a1d525726258416ab",
        "blob_sha1": "0000000000000000000000000000000000000000",
        "gate": "FAKE",
        "seeds": {}
    }
    pin_file = tmp_path / "charge_counters_pin.json"
    pin_file.write_text(json.dumps(bad_pin))

    monkeypatch.setattr(csk4_r2_config, '_PIN_FILE', str(pin_file))

    with pytest.raises(RuntimeError, match='charge_counters.py'):
        csk4_r2_config.make_r2_solver(nx=8, ny=8, nz=8)


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


# ---------------------------------------------------------------------------
# R2 aggregator: TypeError on legacy dicts + R2-C COLLAPSE outcome (v6)
# ---------------------------------------------------------------------------


def test_r2_pf_config_constants():
    """R2-PF (v7): make_r2_pf_config() returns 192³ config with seed + checkpoints."""
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import (make_r2_pf_config, NX_PF, NY_PF, NZ_PF,
                                 T_PF, DT, SEED_L_PF, K_OP10, K_OP10_PF_C)
    import math
    cfg = make_r2_pf_config()
    assert cfg["nx"] == 192 and cfg["ny"] == 192 and cfg["nz"] == 192
    assert cfg["t_end"] == T_PF
    assert cfg["dt"] == DT
    assert cfg["n_steps"] == math.ceil(T_PF / DT)
    assert cfg["k_refl"] == 0.0
    assert cfg["k_op10"] == K_OP10
    assert "seed" in cfg, "make_r2_pf_config must return a 'seed' dict"
    assert cfg["seed"]["constructor"] == "rational", (
        f"R2-PF seed constructor={cfg['seed']['constructor']!r} != 'rational' (G5)")
    assert cfg["seed"]["L"] == SEED_L_PF, (
        f"seed L={cfg['seed']['L']} != SEED_L_PF={SEED_L_PF}")
    assert "checkpoints" in cfg, "make_r2_pf_config must return 'checkpoints'"
    assert len(cfg["checkpoints"]) > 0

    # Control variant
    cfg_c = make_r2_pf_config(control=True)
    assert cfg_c["k_op10"] == K_OP10_PF_C, (
        f"R2-PF-C k_op10={cfg_c['k_op10']} != {K_OP10_PF_C}")


def test_r2_agg_typeerror_on_legacy_dict():
    """agg_clink_ignored_legacy (v6): non-adapter dict raises TypeError.

    aggregate_r2_periods accepts only count_charge_k4 result dicts (with
    'resolved' key). A legacy dict lacking 'resolved' raises TypeError.
    """
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import aggregate_r2_periods

    legacy = {"c_exact": {"resolved": True, "value": 6},
              "c_link": {"resolved": True, "value": 6}}
    with pytest.raises(TypeError, match="resolved"):
        aggregate_r2_periods([legacy], expected_periods=1)


def test_r2_agg_valid_pass():
    """aggregate_r2_periods: all-resolved +6 → PASS."""
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import aggregate_r2_periods

    results = [dict(resolved=True, value=6, reason=None,
                    c_link_result=dict(resolved=True, value=6),
                    c_exact_result=None)] * 10
    out = aggregate_r2_periods(results, expected_periods=10)
    assert out["verdict"] == "PASS"
    assert out["n_resolved"] == 10
    assert out["n_collapse"] == 0


def test_r2_agg_collapse_excluded_from_7():
    """R2-C (v7): any COLLAPSE period → run verdict COLLAPSE (fixes 3032a809 defect §3.4).

    [+6]×7 + [COLLAPSE]×2 with expected_periods=9 → "COLLAPSE"
    (at 3032a809 this asserted PASS; that was wrong).
    [COLLAPSE]×9 → "COLLAPSE" (never INCONCLUSIVE).
    """
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import aggregate_r2_periods

    good = dict(resolved=True, value=6, reason=None,
                c_link_result=dict(resolved=True, value=6), c_exact_result=None)
    collapse_r = dict(resolved=False, value=None, reason="COLLAPSE",
                      c_link_result=None, c_exact_result=None, collapse=True)

    # 7 good + 2 collapse → COLLAPSE (not PASS)
    results = [good] * 7 + [collapse_r] * 2
    out = aggregate_r2_periods(results, expected_periods=9)
    assert out["verdict"] == "COLLAPSE", (
        f"expected COLLAPSE with 2 collapse periods; got {out['verdict']}: {out['notes']}")
    assert out["n_collapse"] == 2
    assert out["n_resolved"] == 7
    assert out["n_wrong"] == 0

    # All COLLAPSE → COLLAPSE (not INCONCLUSIVE)
    out2 = aggregate_r2_periods([collapse_r] * 9, expected_periods=9)
    assert out2["verdict"] == "COLLAPSE", (
        f"expected COLLAPSE for all-collapse run; got {out2['verdict']}: {out2['notes']}")
    assert out2["n_collapse"] == 9


def test_r2_period_collapse_re_le_0():
    """G5 harness trip (Re≤0): period_collapse returns True when any alive bond Re≤0.

    A hedgehog at t=0 has no antipodal bonds (Re>0 everywhere).  Flipping one
    alive site q→−q creates an antipodal bond; period_collapse must detect it.
    r_eq0 set to the CURRENT r_eq so the size ratio is exactly 1.0 > 0.54 and
    cannot trigger — only the Re≤0 arm fires after the flip.
    """
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import period_collapse, r_eq_from_q
    from ave.topological.charge_counters import hedgehog, bcc_alive_mask

    n, rc = 16, 2
    alive = bcc_alive_mask((n, n, n))
    q = hedgehog(n, rc).copy()
    q[~alive] = np.array([1.0, 0.0, 0.0, 0.0])
    r_eq0 = r_eq_from_q(q, alive)  # ratio = 1.0 → size-ratio arm inactive

    assert not period_collapse(q, alive, r_eq0), (
        "static hedgehog with r_eq0=r_eq (ratio=1.0) should not trigger period_collapse")
    site = tuple(np.argwhere(alive)[len(np.argwhere(alive)) // 2])  # middle alive site
    q_flip = q.copy()
    q_flip[site] = -q_flip[site]
    assert period_collapse(q_flip, alive, r_eq0), (
        "Re≤0 bond (alive site q→−q) must trigger period_collapse via Re≤0 arm")


def test_r2_period_collapse_size_ratio():
    """G5 harness trip (size ratio): period_collapse fires when r_eq/r_eq0 < 0.54.

    Uses a vacuum field (q0>0 everywhere, no Re≤0 bonds) so that only the
    size-ratio arm can trigger.  r_eq of the vacuum is 0 (no q0<0 sites);
    instead we set r_eq0 to a value and use a state with known r_eq.

    Concrete test: use the static hedgehog as the "compressed" state.  Set
    r_eq0 = r_eq_now / 0.50 (ratio = 0.50 < 0.54) → COLLAPSE.
    Set r_eq0 = r_eq_now / 0.55 (ratio = 0.55 > 0.54, no Re≤0 bonds) → no COLLAPSE.
    """
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import period_collapse, r_eq_from_q
    from ave.topological.charge_counters import hedgehog, bcc_alive_mask

    n, rc = 16, 2
    alive = bcc_alive_mask((n, n, n))
    q = hedgehog(n, rc).copy()
    q[~alive] = np.array([1.0, 0.0, 0.0, 0.0])
    r_eq_now = r_eq_from_q(q, alive)
    assert r_eq_now > 0.0, "hedgehog(16,2) should have a non-empty q0<0 core"

    r_eq0_trigger = r_eq_now / 0.50   # ratio = 0.50 < 0.54 → COLLAPSE
    assert period_collapse(q, alive, r_eq0_trigger), (
        f"size ratio r_eq/r_eq0={r_eq_now/r_eq0_trigger:.3f} < 0.54 "
        f"should trigger period_collapse")

    r_eq0_ok = r_eq_now / 0.55        # ratio = 0.55 > 0.54, no Re≤0 bonds → no COLLAPSE
    assert not period_collapse(q, alive, r_eq0_ok), (
        f"size ratio r_eq/r_eq0={r_eq_now/r_eq0_ok:.3f} > 0.54 "
        f"should not trigger period_collapse")


def test_r_eq_from_q_hedgehog_calibration():
    """Item 1 (v6): r_eq_from_q(hedgehog(48,6)) matches the initial core radius rc=6.

    With BCC density correction (n_cells/n_alive ≈ 4), the equivalent radius of
    the q0<0 core region should reproduce the geometric core radius rc=6 to ±10%.
    Gate value: r_eq0 ≈ 6.0 for hedgehog(48,6).  Prints r_eq0 for comparison.
    """
    import sys, os as _os
    sys.path.insert(0, _os.path.join(_os.path.dirname(__file__),
                                     '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import r_eq_from_q
    from ave.topological.charge_counters import hedgehog, bcc_alive_mask

    n, rc = 48, 6
    q = hedgehog(n, rc).copy()
    alive = bcc_alive_mask((n, n, n))
    q[~alive] = np.array([1.0, 0.0, 0.0, 0.0])

    r_eq0 = r_eq_from_q(q, alive)
    print(f"[r_eq calibration] r_eq_from_q(hedgehog(48,6)) = {r_eq0:.3f}  "
          f"(Gate: ≈6.0, rc={rc})")
    assert 0.9 * rc <= r_eq0 <= 1.1 * rc, (
        f"r_eq_from_q(hedgehog(48,6)) = {r_eq0:.3f} outside ±10% of rc={rc}: "
        f"expected [{0.9*rc:.1f}, {1.1*rc:.1f}]; BCC density correction not applied?")


def test_r2_agg_later_periods_excluded():
    """R2-C (v7): any COLLAPSE → run verdict COLLAPSE; post-COLLAPSE periods excluded.

    [+6]×5 + COLLAPSE + [+5]×3 → "COLLAPSE", n_wrong=0.
    [+6]×5 + COLLAPSE + [+6]×3 → "COLLAPSE" (not PASS).
    r14_trip_period=2 with first COLLAPSE at 4 → "FAIL(#14)".
    """
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import aggregate_r2_periods

    good = dict(resolved=True, value=6, reason=None,
                c_link_result=dict(resolved=True, value=6), c_exact_result=None)
    wrong = dict(resolved=True, value=5, reason=None,
                 c_link_result=dict(resolved=True, value=5), c_exact_result=None)
    collapse_r = dict(resolved=False, value=None, reason="COLLAPSE",
                      c_link_result=None, c_exact_result=None, collapse=True)

    # [+6]×5 + COLLAPSE + [+5]×3 → COLLAPSE; post-collapse wrong periods excluded
    results = [good] * 5 + [collapse_r] + [wrong] * 3
    out = aggregate_r2_periods(results, expected_periods=9)
    assert out["verdict"] == "COLLAPSE", (
        f"expected COLLAPSE; got {out['verdict']}: {out['notes']}")
    assert out["n_collapse"] == 4, (
        f"expected n_collapse=4 (1 COLLAPSE + 3 post-COLLAPSE excluded); "
        f"got {out['n_collapse']}")
    assert out["n_resolved"] == 5, f"expected n_resolved=5; got {out['n_resolved']}"
    assert out["n_wrong"] == 0, f"expected n_wrong=0; got {out['n_wrong']}"

    # [+6]×5 + COLLAPSE + [+6]×3 → COLLAPSE (not PASS)
    results2 = [good] * 5 + [collapse_r] + [good] * 3
    out2 = aggregate_r2_periods(results2, expected_periods=9)
    assert out2["verdict"] == "COLLAPSE", (
        f"expected COLLAPSE (not PASS); got {out2['verdict']}: {out2['notes']}")

    # r14_trip_period=2 before first COLLAPSE at index 5 → FAIL(#14)
    results3 = [good] * 5 + [collapse_r] + [good] * 3
    out3 = aggregate_r2_periods(results3, expected_periods=9, r14_trip_period=2)
    assert out3["verdict"] == "FAIL(#14)", (
        f"expected FAIL(#14) when r14 trip at 2 < first COLLAPSE at 5; "
        f"got {out3['verdict']}: {out3['notes']}")


def test_r2_agg_period_rule():
    """Item 11 (v7): integer 90% rule and period-count read-back.

    9/9 → PASS; 8/9 (one UNRESOLVED) → INCONCLUSIVE; len=8 expected=9 → ValueError.
    18/20 and 17/20 tests (for a future 68-tu extended run) with expected_periods=20.
    """
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import aggregate_r2_periods

    good = dict(resolved=True, value=6, reason=None,
                c_link_result=dict(resolved=True, value=6), c_exact_result=None)
    unres = dict(resolved=False, value=None, reason="NONUNIT: test",
                 c_link_result=None, c_exact_result=None)

    # 9/9 → PASS (10·9 ≥ 9·9)
    out = aggregate_r2_periods([good] * 9, expected_periods=9)
    assert out["verdict"] == "PASS", f"9/9 expected PASS; got {out['verdict']}: {out['notes']}"

    # 8/9 (one UNRESOLVED) → INCONCLUSIVE (10·8=80 < 9·9=81)
    out2 = aggregate_r2_periods([good] * 8 + [unres], expected_periods=9)
    assert out2["verdict"] == "INCONCLUSIVE", (
        f"8/9 expected INCONCLUSIVE; got {out2['verdict']}: {out2['notes']}")

    # len=8 with expected=9 → ValueError
    import pytest as _pytest
    with _pytest.raises(ValueError, match="expected 9 periods, got 8"):
        aggregate_r2_periods([good] * 8, expected_periods=9)

    # 18/20 → PASS (10·18=180 ≥ 9·20=180)
    out3 = aggregate_r2_periods([good] * 18 + [unres] * 2, expected_periods=20)
    assert out3["verdict"] == "PASS", (
        f"18/20 expected PASS; got {out3['verdict']}: {out3['notes']}")

    # 17/20 → INCONCLUSIVE (10·17=170 < 9·20=180)
    out4 = aggregate_r2_periods([good] * 17 + [unres] * 3, expected_periods=20)
    assert out4["verdict"] == "INCONCLUSIVE", (
        f"17/20 expected INCONCLUSIVE; got {out4['verdict']}: {out4['notes']}")


# ---------------------------------------------------------------------------
# v7 new GATING unit tests (item 5, §3.2.5)
# ---------------------------------------------------------------------------

def _cfg():
    """Return the csk4_r2_config module (avoids repeated path wrangling)."""
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    import csk4_r2_config
    return csk4_r2_config


def test_r_eq_from_q_pins():
    """Item 5 (v7): r_eq_from_q pins — hedgehog(48,6) → 6.016 ± 0.005.

    Kills mutant: r_eq_miscounted (drop ×4, or count all sites).
    """
    cfg = _cfg()
    from ave.topological.charge_counters import hedgehog, bcc_alive_mask

    n, rc = 48, 6
    q = hedgehog(n, rc).copy()
    alive = bcc_alive_mask((n, n, n))
    q[~alive] = np.array([1.0, 0.0, 0.0, 0.0])

    r_eq0 = cfg.r_eq_from_q(q, alive)
    assert abs(r_eq0 - 6.016) <= 0.005, (
        f"test_r_eq_from_q_pins: hedgehog(48,6) → {r_eq0:.4f}, expected 6.016 ± 0.005; "
        f"missing ×4 BCC factor gives 3.790 instead")

    # Alive-mask read-back: on the RAW hedgehog the dead sublattice also carries
    # q0 < 0 (912 sites in total vs 228 alive), so a count over all sites gives
    # r_eq ≈ 9.55 instead of 6.016.  r_eq_from_q must count alive sites only.
    q_raw = hedgehog(n, rc).copy()
    assert int(np.sum(q_raw[~alive, 0] < 0)) > 0, "raw hedgehog: dead sites expected to carry q0<0"
    r_eq_raw = cfg.r_eq_from_q(q_raw, alive)
    assert abs(r_eq_raw - 6.016) <= 0.005, (
        f"test_r_eq_from_q_pins: raw hedgehog(48,6) → {r_eq_raw:.4f}, expected 6.016 ± 0.005 "
        f"(alive sites only); counting all sites gives ≈9.55")


def test_pf_checkpoint_times():
    """Item 5 (v7): pf_checkpoint_times spacing constraints.

    Kills mutant: checkpoints coarsened to 0.05.
    """
    cfg = _cfg()

    T = 0.25
    ckpts = cfg.pf_checkpoint_times(T)

    # Always includes T
    assert abs(ckpts[-1] - T) < 1e-9, (
        f"pf_checkpoint_times({T}): last entry {ckpts[-1]:.6f} ≠ T={T}")

    # Fine region [0, 0.1]: spacing ≤ 0.005
    fine = ckpts[ckpts <= 0.1 + 1e-9]
    if len(fine) > 1:
        max_spacing_fine = float(np.max(np.diff(fine)))
        assert max_spacing_fine <= 0.005 + 1e-9, (
            f"spacing in [0,0.1] = {max_spacing_fine:.4f} > 0.005")

    # Coarse region (0.1, T]: spacing ≤ 0.025
    coarse = ckpts[ckpts > 0.1 - 1e-9]
    if len(coarse) > 1:
        max_spacing_coarse = float(np.max(np.diff(coarse)))
        assert max_spacing_coarse <= 0.025 + 1e-9, (
            f"spacing after 0.1 = {max_spacing_coarse:.4f} > 0.025")

    # Short T (entirely in fine region)
    ckpts2 = cfg.pf_checkpoint_times(0.05)
    assert abs(ckpts2[-1] - 0.05) < 1e-9
    if len(ckpts2) > 1:
        assert float(np.max(np.diff(ckpts2))) <= 0.005 + 1e-9


def test_classify_first_bond():
    """Item 5 (v7): classify_first_bond boundary cases."""
    cfg = _cfg()
    clf = cfg.classify_first_bond

    assert clf(0.99, 1.0) == 'BREAKUP', "ratio=0.99 ≥ 0.85 → BREAKUP"
    assert clf(0.44, 1.0) == 'INFALL',  "ratio=0.44 < 0.85 → INFALL"
    assert clf(0.85, 1.0) == 'BREAKUP', "ratio=0.85 exactly → BREAKUP"
    assert clf(0.84, 1.0) == 'INFALL',  "ratio=0.84 < 0.85 → INFALL"
    assert clf(0.0,  1.0) == 'INFALL',  "r_eq_t=0 → INFALL"


def _make_pre_rows(N_pre, dH, r_eq0, t_first):
    """Two pre-bond checkpoint rows at t=0.005, 0.010 (before any t_first > 0.010).

    Used by tests that pass custom rows= to _pii_trace. For default rows
    (rows=None), _pii_trace generates dense rows at 0.005 intervals.
    """
    resolved = N_pre is not None
    return [
        {'t': 0.005, 'step': 31, 'N': N_pre, 'resolved': resolved,
         'dH': dH, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.010, 'step': 62, 'N': N_pre, 'resolved': resolved,
         'dH': dH, 'n_antipodal': 0, 'r_eq': r_eq0},
    ]


def _pii_trace(t_first=0.03, r_first=6.0, r_eq_ratio=0.98,
               n_antipodal_T=9, dH=1e-5, N_pre=1,
               rows=None, T=0.25, H0=1.0):
    """Synthetic PII trace (r_eq0 = R_EQ0_PII = 11.983) — rows-based format.

    Default rows (rows=None): dense rows at 0.005 intervals 0.005..0.100,
    marking each as pre-bond (t < t_first) or post-bond (t >= t_first).
    For STABLE (t_first=None), a final row at T is appended.
    This satisfies the Gap-B spacing check: [0]+rows_at_t≤0.1 have max gap ≤ 0.005.
    """
    cfg = _cfg()
    r_eq0 = cfg.R_EQ0_PII
    _dt = 1.65e-4

    if rows is not None:
        r = rows
    else:
        resolved_pre = N_pre is not None
        r = []
        for k in range(1, 21):  # t = 0.005, 0.010, ..., 0.100
            t = round(k * 0.005, 6)
            step = int(round(t / _dt))
            if t_first is None or t < t_first - 1e-9:
                r.append({'t': t, 'step': step, 'N': N_pre,
                          'resolved': resolved_pre, 'dH': dH,
                          'n_antipodal': 0, 'r_eq': r_eq0})
            else:
                r_eq_here = r_eq_ratio * r_eq0 if abs(t - t_first) < 0.005 + 1e-9 else r_eq0
                r.append({'t': t, 'step': step, 'N': None,
                          'resolved': False, 'dH': dH,
                          'n_antipodal': n_antipodal_T, 'r_eq': r_eq_here})
        if t_first is None:
            r.append({'t': T, 'step': int(round(T / _dt)), 'N': N_pre,
                      'resolved': resolved_pre, 'dH': dH,
                      'n_antipodal': 0, 'r_eq': r_eq0})

    return {
        'rows': r,
        'H0': H0,
        'r_eq0': r_eq0,
        't_first': t_first,
        'r_first': r_first,
        'r_eq_at_first': (r_eq_ratio * r_eq0) if t_first is not None else None,
        'n_antipodal_T': n_antipodal_T,
        'T': T,
    }


def test_preflight_verdict_pii_confirmed():
    """Item 5 row 1: PII bond at 0.03, all windows pass → BREAKUP/CONFIRMED."""
    cfg = _cfg()
    trace = _pii_trace()
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'BREAKUP', f"expected BREAKUP; got {out}"
    assert out['a8'] == 'CONFIRMED', f"expected CONFIRMED; got {out}"


def test_preflight_verdict_pii_miss_t_first():
    """Item 5 row 2: PII bond at 0.15 (outside window) → BREAKUP/MISS."""
    cfg = _cfg()
    trace = _pii_trace(t_first=0.15)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'BREAKUP', f"expected BREAKUP; got {out}"
    assert out['a8'] == 'MISS', f"expected MISS (t_first outside window); got {out}"
    assert any('t_first' in r for r in out['reasons']), (
        f"t_first should be mentioned in reasons; got {out['reasons']}")


def test_preflight_verdict_piic_control_pass():
    """Item 5 row 3: PII_C bond at 0.10, ratio 0.44 → INFALL/N/A (no BREAKUP-class bond)."""
    cfg = _cfg()
    trace = _pii_trace(t_first=0.10, r_first=0.9, r_eq_ratio=0.44)
    out = cfg.preflight_verdict(trace, cfg.PII_C_SPEC)
    assert out['gate'] == 'INFALL', f"expected INFALL; got {out}"
    assert out['a8'] == 'N/A', (
        f"control INFALL → a8 N/A (control passes); got {out}")


def test_preflight_verdict_piic_control_fail():
    """Item 5 row 4: PII_C bond at 0.03, ratio 0.98 → BREAKUP/MISS (control fail)."""
    cfg = _cfg()
    trace = _pii_trace(t_first=0.03, r_eq_ratio=0.98)
    out = cfg.preflight_verdict(trace, cfg.PII_C_SPEC)
    assert out['gate'] == 'BREAKUP', f"expected BREAKUP; got {out}"
    assert out['a8'] == 'MISS', (
        f"control BREAKUP-class bond → a8 MISS (control fail); got {out}")


def test_preflight_verdict_pii_stable():
    """Item 5 row 5: no bond, N +1 all, dH 1e-5 → STABLE/N/A."""
    cfg = _cfg()
    trace = _pii_trace(t_first=None, N_pre=1, dH=1e-5)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'STABLE', f"expected STABLE; got {out}"
    assert out['a8'] == 'N/A', f"expected N/A for STABLE; got {out}"


def test_preflight_verdict_invalid_spacing():
    """Item 5 row 6: checkpoint spacing > 0.005 at t ≤ 0.1 → INVALID (rows-based)."""
    cfg = _cfg()
    r_eq0 = cfg.R_EQ0_PII
    # Two early rows at t=0.05 and t=0.10 → spacing=0.05 > 0.005.
    # t_first=None so both rows are pre-bond (spacing check applies).
    sparse_rows = [
        {'t': 0.05, 'step': 303, 'N': 1, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.10, 'step': 606, 'N': 1, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.25, 'step': 1516, 'N': 1, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
    ]
    trace = _pii_trace(t_first=None, rows=sparse_rows)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'INVALID', (
        f"expected INVALID (spacing 0.05 > 0.005); got {out}")


def test_preflight_verdict_invalid_dh():
    """Item 5 row 7: dH 2e-3 before any bond → INVALID."""
    cfg = _cfg()
    trace = _pii_trace(t_first=None, dH=2e-3)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'INVALID', f"expected INVALID (dH 2e-3 > 1e-3); got {out}"


def test_preflight_verdict_r2pf_confirmed():
    """Item 5 row 8: R2PF bond at 0.02, r 14, ratio 0.97, n(T) 12, N +6 → BREAKUP/CONFIRMED."""
    cfg = _cfg()
    r_eq0 = cfg.R_EQ0_R2
    # rows-based format: N_expected=6 for R2PF_SPEC
    rows_r2pf = [
        {'t': 0.004, 'step': 18, 'N': 6, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.008, 'step': 36, 'N': 6, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.012, 'step': 54, 'N': 6, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.016, 'step': 71, 'N': 6, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.020, 'step': 89, 'N': None, 'resolved': False,
         'dH': 1e-5, 'n_antipodal': 12, 'r_eq': 0.97 * r_eq0},
    ]
    trace = {
        'rows': rows_r2pf,
        'H0': 1.0,
        'r_eq0': r_eq0,
        't_first': 0.02,
        'r_first': 14.0,
        'r_eq_at_first': 0.97 * r_eq0,
        'n_antipodal_T': 12,
        'T': 0.25,
    }
    out = cfg.preflight_verdict(trace, cfg.R2PF_SPEC)
    assert out['gate'] == 'BREAKUP', f"expected BREAKUP; got {out}"
    assert out['a8'] == 'CONFIRMED', f"expected CONFIRMED; got {out}"


def test_pf_config_readback():
    """Item 5 (v7): P-ii / P-ii-C / R2-PF / R2-PF-C config key read-backs."""
    import math as _math
    cfg = _cfg()

    # P-ii primary
    pii = cfg.make_pii_config(control=False)
    assert pii['k_op10'] == 8.88e5, f"P-ii k_op10 {pii['k_op10']}"
    assert pii['gamma'] == 4320
    assert pii['k_refl'] == 0.0
    assert pii['dt'] == 1.65e-4
    assert pii['t_end'] == 0.25
    assert pii['n_steps'] == _math.ceil(0.25 / 1.65e-4), (
        f"n_steps={pii['n_steps']} != ceil(0.25/1.65e-4)={_math.ceil(0.25/1.65e-4)}")
    assert pii['seed']['constructor'] == "_hedgehog_at", (
        f"P-ii seed constructor={pii['seed']['constructor']!r} != '_hedgehog_at'")
    assert pii['seed']['L'] == cfg.SEED_L_PII, (
        f"P-ii seed L={pii['seed']['L']} != SEED_L_PII={cfg.SEED_L_PII}")

    # P-ii-C control
    piic = cfg.make_pii_config(control=True)
    assert piic['k_op10'] == 5.59e4, f"P-ii-C k_op10 {piic['k_op10']}"
    assert piic['seed']['constructor'] == "_hedgehog_at", (
        f"P-ii-C seed constructor={piic['seed']['constructor']!r} != '_hedgehog_at'")

    # R2-PF primary
    r2pf = cfg.make_r2_pf_config(control=False)
    assert r2pf['k_op10'] == 1.415e6, f"R2-PF k_op10 {r2pf['k_op10']}"
    assert r2pf['gamma'] == 4320
    assert r2pf['k_refl'] == 0.0
    assert r2pf['seed']['constructor'] == "rational", (
        f"R2-PF seed constructor={r2pf['seed']['constructor']!r} != 'rational' (G5)")
    assert r2pf['seed']['L'] == cfg.SEED_L_PF, (
        f"R2-PF seed L={r2pf['seed']['L']} != SEED_L_PF={cfg.SEED_L_PF}")
    assert r2pf['t_end'] == 0.25
    assert r2pf['n_steps'] == _math.ceil(0.25 / r2pf['dt']), (
        f"n_steps={r2pf['n_steps']} != ceil(T/dt)")

    # R2-PF-C control
    r2pfc = cfg.make_r2_pf_config(control=True)
    assert r2pfc['k_op10'] == 3.93e4, f"R2-PF-C k_op10 {r2pfc['k_op10']}"


def test_seed_cutoff_readback():
    """G4/G5 (v7): seed read-back via build_pf_seed; kills the wrong-seed-cutoff mutant.

    32³ stand-ins avoid 128³/192³ construction cost:
      P-ii:   n=32, rc=3  (rc12→3, L/rc=4 → L_standin=12)
      R2-PF:  n=32, rc=4  (rc24→4, L/rc=4 → L_standin=16 = 32/2)

    r_eq(0) is cutoff-blind (Gate verified: L=48 and L=64 both give 1802 sites at
    128³/rc=12), so this test is purely bitwise.  The wrong-cutoff mutant is
    _hedgehog_at(128,12) with L=64 (n/2 default) instead of L=48.
    """
    import sys, os as _os
    sys.path.insert(0, _os.path.join(_os.path.dirname(__file__),
                                     '..', 'scripts', 'vol_4_engineering'))
    import math as _math
    from csk4_r2_config import (
        build_pf_seed, make_pii_config, make_r2_pf_config,
        SEED_L_PII, SEED_L_PF, SEED_L_PRIMARY, SEED_RC, NX_PRIMARY,
        SEED_P, SEED_QQ,
    )
    from ave.topological.charge_counters import _hedgehog_at, rational

    # Literal constant read-backs
    assert SEED_L_PII == 48,       "SEED_L_PII must be 48"
    assert SEED_L_PF == 96,        "SEED_L_PF must be 96"
    assert SEED_L_PRIMARY == 144,  "SEED_L_PRIMARY must be 144"

    # R2 primary: rational(n,rc) uses cutoff n/2; assert 288/2 == 144 == 6×24
    assert NX_PRIMARY // 2 == SEED_L_PRIMARY, (
        f"R2 primary: NX_PRIMARY/2={NX_PRIMARY//2} != SEED_L_PRIMARY={SEED_L_PRIMARY}; "
        "rational() cutoff is n/2")
    assert SEED_L_PRIMARY == 6 * SEED_RC, (
        f"SEED_L_PRIMARY={SEED_L_PRIMARY} != 6×SEED_RC={6*SEED_RC}")

    # P-ii stand-in: n=32, rc=3 → L_standin = 48*(3/12) = 12 = L/rc×rc = 4×3
    pii_cfg = make_pii_config(control=False)
    q_pii = build_pf_seed(pii_cfg, n=32, rc=3)
    q_pii_direct = _hedgehog_at(32, 3, (0, 0, 0), L=12)   # L/rc=4, pinned ratio
    q_pii_wrong  = _hedgehog_at(32, 3, (0, 0, 0), L=16)   # n/2 default — L=64 mutant at 128³
    assert np.array_equal(q_pii, q_pii_direct), (
        "build_pf_seed(pii_cfg, n=32, rc=3) != _hedgehog_at(32,3,(0,0,0),L=12); "
        "cutoff ratio L/rc=4 not preserved")
    assert not np.array_equal(q_pii, q_pii_wrong), (
        "build_pf_seed(pii_cfg, n=32, rc=3) == _hedgehog_at(32,3,...,L=16); "
        "wrong-cutoff mutant (L=64 at 128³) not distinguishable")

    # P-ii-C: same seed dict as P-ii primary
    piic_cfg = make_pii_config(control=True)
    q_piic = build_pf_seed(piic_cfg, n=32, rc=3)
    assert np.array_equal(q_piic, q_pii_direct), (
        "build_pf_seed(pii_c_cfg, n=32, rc=3) != _hedgehog_at(32,3,(0,0,0),L=12); "
        "control config should have the same seed")

    # R2-PF stand-in: n=32, rc=4 → L_standin = 96*(4/24) = 16 = 32/2
    # rational(32, 4) uses cutoff 32/2=16 — must match build_pf_seed exactly
    r2pf_cfg = make_r2_pf_config(control=False)
    q_r2pf = build_pf_seed(r2pf_cfg, n=32, rc=4)
    q_r2pf_direct = rational(32, 4, p=SEED_P, qq=SEED_QQ)
    assert np.array_equal(q_r2pf, q_r2pf_direct), (
        "build_pf_seed(r2pf_cfg, n=32, rc=4) != rational(32,4,...); "
        "R2-PF seed constructor mismatch or wrong scale")

    # R2-PF control has the same seed dict as primary
    r2pfc_cfg = make_r2_pf_config(control=True)
    assert r2pfc_cfg['seed'] == r2pf_cfg['seed'], (
        f"R2-PF control seed {r2pfc_cfg['seed']} != primary seed {r2pf_cfg['seed']}")


# ---------------------------------------------------------------------------
# G1 (6c): antipodal_bonds gating test — kills "detector off" mutant in the
# gating lane (antipodal_bonds() was previously only called by opt-in tests)
# ---------------------------------------------------------------------------


def test_antipodal_bonds_synthetic():
    """G1 (6c): antipodal_bonds gating test on a small synthetic grid.

    Kills the "detector off" mutant: if antipodal_bonds() (or collapse_check)
    is broken so it never reports a bond, part (b) of this test fails on a
    non-empty list and part (c) fails on the collapse/bond inconsistency.

    Grid: hedgehog(16, 3) with a BCC alive mask.  Centre = (8, 8, 8).

    (a) vacuum (all alive q = (1,0,0,0)) -> [] (no bonds in the vacuum state)
    (b) flip ONE alive site q -> -q -> non-empty list; every entry re <= 0;
        each listed bond involves the flipped site or its bond partner; r equals
        the distance from centre to bond midpoint (checked numerically for first).
    (c) bool(len(antipodal_bonds(...)) > 0) == collapse_check(q, alive)["collapse"]
        (the two share the bond definition so they must agree on bond presence).
    """
    import sys, os as _os
    sys.path.insert(0, _os.path.join(_os.path.dirname(__file__),
                                     '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import antipodal_bonds
    from ave.topological.charge_counters import hedgehog, bcc_alive_mask
    from ave.topological.k4_quaternion import collapse_check

    n, rc = 16, 3
    alive = bcc_alive_mask((n, n, n))
    centre = (n // 2, n // 2, n // 2)
    c_arr = np.array(centre, dtype=float)

    # (a) vacuum: all alive sites q = (1,0,0,0) -> no antipodal bonds
    q_vac = np.zeros((n, n, n, 4))
    q_vac[..., 0] = 1.0
    bonds_vac = antipodal_bonds(q_vac, alive, centre)
    assert bonds_vac == [], (
        f"vacuum (all q=(1,0,0,0)) should have no antipodal bonds; got {len(bonds_vac)}")

    # (b) flip ONE alive site: q -> -q creates a bond
    q = hedgehog(n, rc).copy()
    q[~alive] = np.array([1.0, 0.0, 0.0, 0.0])

    alive_sites = np.argwhere(alive)
    dists = np.linalg.norm(alive_sites - c_arr, axis=1)
    flip_site = tuple(alive_sites[int(np.argmin(dists))].tolist())

    q_flip = q.copy()
    q_flip[flip_site] = -q_flip[flip_site]

    bonds_flip = antipodal_bonds(q_flip, alive, centre)
    assert len(bonds_flip) > 0, (
        "flipping an alive site q->-q should create >=1 antipodal bond; got none"
        " -- detector may be off")

    for (site, p, re, r) in bonds_flip:
        assert re <= 0.0, (
            f"bond at site={site} offset={p} has re={re:.6f} > 0; "
            "antipodal bond must have re <= 0")

    fi, fj, fk = flip_site
    for (site, p, re, r) in bonds_flip:
        si, sj, sk = site
        di, dj, dk = p
        neighbour = ((si + di) % n, (sj + dj) % n, (sk + dk) % n)
        assert site == flip_site or neighbour == flip_site, (
            f"bond at site={site} p={p} does not involve flipped site {flip_site}")

    # Check r numerically for the first bond
    site0, p0, re0, r0 = bonds_flip[0]
    i0, j0, k0 = site0
    di0, dj0, dk0 = p0
    mid = np.array([i0 + di0 / 2.0, j0 + dj0 / 2.0, k0 + dk0 / 2.0])
    r_expected = float(np.linalg.norm(mid - c_arr))
    assert abs(r0 - r_expected) < 1e-10, (
        f"bond r={r0:.10f} != expected distance to midpoint {r_expected:.10f}")

    # (c) antipodal_bonds and collapse_check must agree on bond presence
    cc_flip = collapse_check(q_flip, alive)
    assert bool(len(bonds_flip) > 0) == cc_flip["collapse"], (
        f"antipodal_bonds found {len(bonds_flip)} bond(s) but collapse_check returned "
        f"collapse={cc_flip['collapse']}; they share the bond definition")

    # Sanity: confirm unflipped hedgehog agrees too
    bonds_hh = antipodal_bonds(q, alive, centre)
    cc_hh = collapse_check(q, alive)
    assert bool(len(bonds_hh) > 0) == cc_hh["collapse"], (
        f"antipodal_bonds/collapse_check disagree on unflipped hedgehog: "
        f"{len(bonds_hh)} bonds vs collapse={cc_hh['collapse']}")


# ---------------------------------------------------------------------------
# G2 (6c): preflight_verdict post_bond_dH_max flag
# ---------------------------------------------------------------------------


def test_preflight_verdict_post_bond_dh_flag():
    """G2 (6c, rows-updated): post-bond row dH > 1e-2 appends 'dH>1e-2 flag'.

    Does NOT change gate or a8.
    - CONFIRMED base + extra post-bond row dH=5e-2 → still BREAKUP/CONFIRMED, flag in reasons
    - CONFIRMED base + extra post-bond row dH=5e-3 → BREAKUP/CONFIRMED, flag NOT in reasons
    """
    cfg = _cfg()

    base = _pii_trace()  # t_first=0.03, rows include row at ~0.031
    # Add a post-bond row at t=0.05 with high dH
    post_hi = {'t': 0.05, 'step': 303, 'N': None, 'resolved': False,
               'dH': 5e-2, 'n_antipodal': 9, 'r_eq': 11.0}
    trace_hi = dict(base, rows=base['rows'] + [post_hi])
    out_hi = cfg.preflight_verdict(trace_hi, cfg.PII_SPEC)
    assert out_hi['gate'] == 'BREAKUP', f"expected BREAKUP; got {out_hi}"
    assert out_hi['a8'] == 'CONFIRMED', f"expected CONFIRMED; got {out_hi}"
    assert any('dH>1e-2 flag' in r for r in out_hi['reasons']), (
        f"post-bond dH=5e-2 > 1e-2 must append 'dH>1e-2 flag'; "
        f"reasons={out_hi['reasons']}")

    post_lo = {'t': 0.05, 'step': 303, 'N': None, 'resolved': False,
               'dH': 5e-3, 'n_antipodal': 9, 'r_eq': 11.0}
    trace_lo = dict(base, rows=base['rows'] + [post_lo])
    out_lo = cfg.preflight_verdict(trace_lo, cfg.PII_SPEC)
    assert out_lo['gate'] == 'BREAKUP', f"expected BREAKUP; got {out_lo}"
    assert out_lo['a8'] == 'CONFIRMED', f"expected CONFIRMED; got {out_lo}"
    assert not any('dH>1e-2 flag' in r for r in out_lo['reasons']), (
        f"post-bond dH=5e-3 <= 1e-2 must NOT append flag; "
        f"reasons={out_lo['reasons']}")


# ---------------------------------------------------------------------------
# G3 (6c): preflight_verdict missing/empty ckpt_spacings_early -> INVALID
# ---------------------------------------------------------------------------


def test_preflight_verdict_invalid_no_spacing():
    """G3 (6c, rows-updated): missing 'rows' key or empty rows → INVALID.

    A trace without rows cannot be judged. Gate must be INVALID.
    Also tests that empty rows (list present but []) → INVALID.
    """
    cfg = _cfg()
    r_eq0 = cfg.R_EQ0_PII

    # Missing 'rows' key → INVALID (missing required key)
    base_no_rows = {
        'H0': 1.0,
        'r_eq0': r_eq0,
        't_first': 0.03,
        'r_first': 6.0,
        'r_eq_at_first': 0.98 * r_eq0,
        'n_antipodal_T': 9,
        'T': 0.25,
    }
    out_missing = cfg.preflight_verdict(base_no_rows, cfg.PII_SPEC)
    assert out_missing['gate'] == 'INVALID', (
        f"missing 'rows' key must yield INVALID; got {out_missing}")
    assert any("rows" in r for r in out_missing['reasons']), (
        f"INVALID reason must mention 'rows'; got {out_missing['reasons']}")

    # Empty rows → INVALID
    out_empty = cfg.preflight_verdict(dict(base_no_rows, rows=[]), cfg.PII_SPEC)
    assert out_empty['gate'] == 'INVALID', (
        f"empty rows must yield INVALID; got {out_empty}")


# ---------------------------------------------------------------------------
# §11 item 1 — one seed builder: runner seed sha1 gating test
# ---------------------------------------------------------------------------


def test_preflight_runner_seed_sha1():
    """§11 item 1: run_preflight builds seed via build_pf_seed; sha1 pinned.

    Calls run_preflight at n=32, rc=3 stand-in (5 steps — no full physics).
    Asserts trace['seed_sha1'] equals sha1 of build_pf_seed(pii_cfg, 32, 3)
    with dead-site reset, and differs from the L=n/2 wrong-cutoff seed.

    Kills: runner-seed L=64 (n/2) bypass in run_preflight.
    Also kills: option-(ii) seed builder if it diverges from build_pf_seed.
    """
    import sys, os as _os, hashlib as _hashlib
    sys.path.insert(0, _os.path.join(_os.path.dirname(__file__),
                                     '..', 'scripts', 'vol_4_engineering'))
    import csk4_r2_config as cfg_mod
    from ave.topological.charge_counters import _hedgehog_at, bcc_alive_mask

    pii_cfg = cfg_mod.make_pii_config(control=False)
    n_si, rc_si = 32, 3  # stand-in: L_pinned=12 (4×rc_si), n/2=16 → distinguishable

    trace = cfg_mod.run_preflight(pii_cfg, cfg_mod.PII_SPEC, n=n_si, rc=rc_si, max_steps=5)
    assert 'seed_sha1' in trace, "run_preflight must return 'seed_sha1'"

    # Expected sha1: build_pf_seed with dead-site reset
    alive_si = bcc_alive_mask((n_si, n_si, n_si))
    q_exp = cfg_mod.build_pf_seed(pii_cfg, n=n_si, rc=rc_si)
    q_exp[~alive_si] = np.array([1.0, 0.0, 0.0, 0.0])
    expected_sha1 = _hashlib.sha1(q_exp.tobytes()).hexdigest()

    # Wrong sha1: L = n/2 = 16 (the L=64 mutant scaled to this stand-in)
    q_wrong = _hedgehog_at(n_si, rc_si, (0, 0, 0), L=n_si // 2)
    q_wrong[~alive_si] = np.array([1.0, 0.0, 0.0, 0.0])
    wrong_sha1 = _hashlib.sha1(q_wrong.tobytes()).hexdigest()

    assert trace['seed_sha1'] == expected_sha1, (
        f"run_preflight seed_sha1={trace['seed_sha1']!r} != "
        f"build_pf_seed sha1={expected_sha1!r}; runner may not use build_pf_seed")
    assert trace['seed_sha1'] != wrong_sha1, (
        f"run_preflight seed_sha1 == wrong L={n_si//2} sha1; "
        f"L=n/2 mutant not distinguishable at n={n_si}, rc={rc_si}")


# ---------------------------------------------------------------------------
# Gap-D + Gap-C — stub-solver test: checkpoint hits, dH vs H0, t_first,
#                 r_first, centre, N/resolved, seed_sha1 via preflight_setup
# ---------------------------------------------------------------------------


def test_run_preflight_stub_solver():
    """Gap-D (also Gap-C): run_preflight via injected stub verifies all trace fields.

    Stub: q setter ignores hedgehog q0 and initialises to identity field.
    step() advances a counter; at step 5 flips site (6,6,6) → −q, creating
    4 antipodal bonds.  Energy returns scripted (total, kinetic) by step index.

    Checkpoints [2.5dt, 4dt, 7.2dt] are NOT multiples of dt=0.01.
    First-step hits: s=3 (3dt=0.030≥0.025), s=4 (0.040≥0.040), s=8 (0.080≥0.072).

    Assertions:
      (1) 3 rows at steps 3, 4, 8 with stored checkpoint times (not s*dt)
      (2) each row's dH == |H(step)−H0|/H0 from script (kills dH-vs-H_prev mutant)
      (3) t_first == 5*dt (kills record-only-at-checkpoint mutant)
      (4) r_first == sqrt(3) to 1e-9 (kills centre=n//2 mutant);
          trace['centre'] == ((n-1)/2,)*3  (Gap-C)
      (5) N/resolved match count_charge_k4 on actual stub q states
      (6) seed_sha1 == preflight_setup sha1 (single builder path)
    """
    import sys, os as _os, math as _math
    sys.path.insert(0, _os.path.join(_os.path.dirname(__file__),
                                     '..', 'scripts', 'vol_4_engineering'))
    import csk4_r2_config as cfg_mod
    from ave.topological.charge_counters import bcc_alive_mask
    from ave.topological.k4_quaternion import count_charge_k4

    n, rc = 16, 3
    _dt = 0.01
    _n_steps = 10
    _flip_step = 5   # bond appears at step 5 → t_first = 5*dt = 0.05
    _flip_site = (6, 6, 6)  # all-even → BCC alive

    _ckpts = [2.5 * _dt, 4.0 * _dt, 7.2 * _dt]
    _cfg_stub = {
        'nx': n, 'ny': n, 'nz': n,
        'dt': _dt, 'n_steps': _n_steps, 't_end': _n_steps * _dt,
        'gamma': 1.0, 'G': 1.0, 'G_c': 1.0,
        'k_op10': 1.0, 'k_refl': 0.0, 'rotation_storage': 'quaternion',
        'seed': {'constructor': '_hedgehog_at', 'rc': rc, 'L': 12},
        'checkpoints': _ckpts,
    }
    # Scripted energy table: index = step_count at point of call
    # H0 = total[0]+kinetic[0] = 5.0
    # step 3: H=5.001  → dH=2e-4 (pre-bond, <1e-3)
    # step 4: H=5.0012 → dH=2.4e-4 (pre-bond)
    # step 8: H=5.075  → dH=1.5e-2 (post-bond, >1e-2 → dH flag)
    _H0 = 5.0
    _energy_by_step = {0: (4.0, 1.0), 3: (4.001, 1.0), 4: (4.0012, 1.0),
                       8: (4.075, 1.0)}
    _dH_expected = {3: abs(5.001 - _H0) / _H0,
                    4: abs(5.0012 - _H0) / _H0,
                    8: abs(5.075 - _H0) / _H0}

    class _StubSolver:
        def __init__(self, nn):
            self._step_count = 0
            self._q = None
            self.gamma = None
            self.k_op10 = None

        @property
        def q(self):
            return self._q

        @q.setter
        def q(self, val):
            # Ignore hedgehog q0 — use identity field for predictable bonds
            self._q = np.zeros(val.shape, dtype=np.float64)
            self._q[..., 0] = 1.0

        def step(self, dt):
            self._step_count += 1
            if self._step_count == _flip_step:
                i, j, k = _flip_site
                self._q[i, j, k] = -self._q[i, j, k]

        def total_energy_k4(self):
            return _energy_by_step.get(self._step_count, (4.0, 1.0))[0]

        def kinetic_energy_k4(self):
            return _energy_by_step.get(self._step_count, (4.0, 1.0))[1]

    _stub_spec = {'N_expected': None, 'r_eq0_pin': None,
                  'is_control': False, 'windows': []}

    trace = cfg_mod.run_preflight(
        _cfg_stub, _stub_spec, n=n, rc=rc, max_steps=_n_steps,
        make_solver=lambda nn: _StubSolver(nn),
    )

    # (1) Row count and checkpoint hit steps
    assert len(trace['rows']) == 3, (
        f"expected 3 rows (steps 3,4,8); got {len(trace['rows'])}")
    exp_steps = [3, 4, 8]
    for i, es in enumerate(exp_steps):
        assert trace['rows'][i]['step'] == es, (
            f"row {i} step={trace['rows'][i]['step']} != {es}")
    # Row times are stored checkpoint times, not s*dt
    assert trace['rows'][0]['t'] == pytest.approx(_ckpts[0]), "row 0 t"
    assert trace['rows'][1]['t'] == pytest.approx(_ckpts[1]), "row 1 t"
    assert trace['rows'][2]['t'] == pytest.approx(_ckpts[2]), "row 2 t"

    # (2) dH vs H0 (not H_prev)
    for i, s in enumerate([3, 4, 8]):
        exp_dH = _dH_expected[s]
        act_dH = trace['rows'][i]['dH']
        assert abs(act_dH - exp_dH) < 1e-12, (
            f"row {i} step {s}: dH={act_dH:.6e} != {exp_dH:.6e}")

    # (3) t_first = flip_step * dt (not first checkpoint after flip)
    assert trace['t_first'] == pytest.approx(_flip_step * _dt, abs=1e-12), (
        f"t_first={trace['t_first']} != {_flip_step * _dt}")

    # (4) r_first and centre
    expected_centre = tuple((n - 1) / 2.0 for _ in range(3))
    assert trace['centre'] == pytest.approx(expected_centre, abs=1e-12), (
        f"centre={trace['centre']} != {expected_centre}")
    # Nearest bond midpoint from (6,6,6) with offset (1,1,1): (6.5,6.5,6.5)
    # distance from centre (7.5,7.5,7.5) = sqrt((−1)²×3) = sqrt(3)
    expected_r_first = _math.sqrt(3)
    assert abs(trace['r_first'] - expected_r_first) < 1e-9, (
        f"r_first={trace['r_first']:.12f} != sqrt(3)={expected_r_first:.12f}")

    # (5) N/resolved from count_charge_k4 on actual stub q states
    alive_si = bcc_alive_mask((n, n, n))
    q_id = np.zeros((n, n, n, 4)); q_id[..., 0] = 1.0
    q_flip = q_id.copy(); q_flip[_flip_site] = -q_flip[_flip_site]
    r_pre = count_charge_k4(q_id, alive_si)
    r_post = count_charge_k4(q_flip, alive_si)

    exp_N_pre = r_pre.get('value') if r_pre.get('resolved') else None
    exp_N_post = r_post.get('value') if r_post.get('resolved') else None
    for i, (exp_N, exp_res) in enumerate([(exp_N_pre, bool(r_pre.get('resolved'))),
                                           (exp_N_pre, bool(r_pre.get('resolved'))),
                                           (exp_N_post, bool(r_post.get('resolved')))]):
        assert trace['rows'][i]['resolved'] == exp_res, (
            f"row {i} resolved={trace['rows'][i]['resolved']} != {exp_res}")
        assert trace['rows'][i]['N'] == exp_N, (
            f"row {i} N={trace['rows'][i]['N']} != {exp_N}")

    # n_antipodal_T = 8: 4 bonds FROM (6,6,6) to its alive tetra-neighbours,
    # plus 4 bonds from the 4 alive sites that each have (6,6,6) as their
    # tetra-neighbour under their respective offsets.
    assert trace['n_antipodal_T'] == 8, (
        f"n_antipodal_T={trace['n_antipodal_T']}, expected 8 from flip at (6,6,6)")
    assert trace['rows'][2]['n_antipodal'] == 8, (
        f"post-bond row n_antipodal={trace['rows'][2]['n_antipodal']}, expected 8")

    # (6) seed_sha1 matches preflight_setup (single builder path)
    exp_sha1 = cfg_mod.preflight_setup(_cfg_stub, n=n, rc=rc)['seed_sha1']
    assert trace['seed_sha1'] == exp_sha1, (
        f"seed_sha1 mismatch: {trace['seed_sha1']!r} != {exp_sha1!r}")


# ---------------------------------------------------------------------------
# §11 item 2 — per-checkpoint trace rows: N flip, UNRESOLVED, missing keys, dH row
# ---------------------------------------------------------------------------


def test_preflight_verdict_n_flip_invalid():
    """§11 item 2(i): N flipped at one interior pre-bond checkpoint → INVALID.

    One row with N=2 (wrong; N_expected=1) before t_first — never STABLE.
    Kills: v7_preflight_N_check_off mutant.
    """
    cfg = _cfg()
    r_eq0 = cfg.R_EQ0_PII
    rows_n_flip = [
        {'t': 0.005, 'step': 31, 'N': 1, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.010, 'step': 62, 'N': 2, 'resolved': True,   # N flipped to 2
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
    ]
    trace = _pii_trace(t_first=0.03, rows=rows_n_flip)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'INVALID', (
        f"N flip at pre-bond checkpoint must yield INVALID; got {out}")
    assert any('N=' in r or 'N_expected' in r for r in out['reasons']), (
        f"INVALID reason must mention N; got {out['reasons']}")

    # t_first=None (STABLE would be attempted): still INVALID due to N flip
    trace_stable = _pii_trace(t_first=None, rows=rows_n_flip + [
        {'t': 0.25, 'step': 1516, 'N': 2, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0}
    ])
    out2 = cfg.preflight_verdict(trace_stable, cfg.PII_SPEC)
    assert out2['gate'] == 'INVALID', (
        f"N flip before STABLE must still yield INVALID; got {out2}")


def test_preflight_verdict_unresolved_invalid():
    """§11 item 2(ii): UNRESOLVED at one pre-bond checkpoint → INVALID.

    Kills: v7_preflight_N_check_off mutant (UNRESOLVED path).
    """
    cfg = _cfg()
    r_eq0 = cfg.R_EQ0_PII
    rows_unres = [
        {'t': 0.005, 'step': 31, 'N': 1, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.010, 'step': 62, 'N': None, 'resolved': False,  # UNRESOLVED
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
    ]
    trace = _pii_trace(t_first=0.03, rows=rows_unres)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'INVALID', (
        f"UNRESOLVED pre-bond checkpoint must yield INVALID; got {out}")
    assert any('UNRESOLVED' in r for r in out['reasons']), (
        f"INVALID reason must mention UNRESOLVED; got {out['reasons']}")


def test_preflight_verdict_missing_keys_invalid():
    """§11 item 2(iii) + Gap-A: missing required trace/row keys → INVALID.

    Tests every required trace key ('rows','H0','r_eq0','t_first','T'), a row
    missing 'dH', and a bonded trace with r_first=None.
    Each missing/None independently produces INVALID.
    """
    cfg = _cfg()
    good = _pii_trace()

    # All required trace-level keys must be present
    for key in ('rows', 'H0', 'r_eq0', 't_first', 'T'):
        bad = {k: v for k, v in good.items() if k != key}
        out = cfg.preflight_verdict(bad, cfg.PII_SPEC)
        assert out['gate'] == 'INVALID', (
            f"missing key '{key}' must yield INVALID; got {out}")
        assert any(key in r for r in out['reasons']), (
            f"INVALID reason must mention '{key}'; got {out['reasons']}")

    # Row missing 'dH' → INVALID
    r_eq0 = cfg.R_EQ0_PII
    row_no_dh = {'t': 0.005, 'step': 31, 'N': 1, 'resolved': True,
                 'n_antipodal': 0, 'r_eq': r_eq0}  # 'dH' absent
    trace_bad_row = _pii_trace(rows=[row_no_dh,
                                     {'t': 0.010, 'step': 62, 'N': 1,
                                      'resolved': True, 'dH': 1e-5,
                                      'n_antipodal': 0, 'r_eq': r_eq0}])
    out_row = cfg.preflight_verdict(trace_bad_row, cfg.PII_SPEC)
    assert out_row['gate'] == 'INVALID', (
        f"row missing 'dH' must yield INVALID; got {out_row}")
    assert any('dH' in r for r in out_row['reasons']), (
        f"reason must mention 'dH'; got {out_row['reasons']}")

    # Bonded trace with r_first=None → INVALID
    trace_rfirst_none = dict(_pii_trace(t_first=0.03), r_first=None)
    out_rf = cfg.preflight_verdict(trace_rfirst_none, cfg.PII_SPEC)
    assert out_rf['gate'] == 'INVALID', (
        f"bonded trace with r_first=None must yield INVALID; got {out_rf}")
    assert any('r_first' in r for r in out_rf['reasons']), (
        f"reason must mention 'r_first'; got {out_rf['reasons']}")


def test_preflight_verdict_spacing_from_origin_invalid():
    """Gap-B(i): first row at 0.02 → gap from origin 0.02 > 0.005 → INVALID."""
    cfg = _cfg()
    r_eq0 = cfg.R_EQ0_PII
    # Single pre-bond row at t=0.02; origin is implicitly 0 → gap=0.02
    rows_sparse = [
        {'t': 0.020, 'step': 121, 'N': 1, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.025, 'step': 152, 'N': 1, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
    ]
    trace = _pii_trace(t_first=None, rows=rows_sparse + [
        {'t': 0.25, 'step': 1516, 'N': 1, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0}
    ])
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'INVALID', (
        f"first row at 0.02 (gap 0.02 from origin) must yield INVALID; got {out}")
    assert any('spacing' in r or '0.02' in r or '0.020' in r
               for r in out['reasons']), (
        f"reason must mention spacing; got {out['reasons']}")


def test_preflight_verdict_spacing_post_bond_invalid():
    """Gap-B(ii): coarse gap after bond but at t ≤ 0.1 → INVALID.

    Rows at 0.005..0.025 (pre-bond), then post-bond row at 0.060 — gap 0.035.
    """
    cfg = _cfg()
    r_eq0 = cfg.R_EQ0_PII
    pre = [
        {'t': round(k * 0.005, 6), 'step': k * 31, 'N': 1, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0}
        for k in range(1, 6)  # 0.005..0.025
    ]
    post = [
        {'t': 0.060, 'step': 364, 'N': None, 'resolved': False,
         'dH': 1e-5, 'n_antipodal': 3, 'r_eq': r_eq0 * 0.98},
    ]
    trace = _pii_trace(t_first=0.030, rows=pre + post)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'INVALID', (
        f"post-bond gap 0.025→0.060=0.035 > 0.005 must yield INVALID; got {out}")
    assert any('spacing' in r for r in out['reasons']), (
        f"reason must mention spacing; got {out['reasons']}")


def test_preflight_verdict_dh_row_invalid():
    """§11 item 2(iv): |dH| 2e-3 at one pre-bond row → INVALID.

    Kills: v7_preflight_dH_check_off mutant at the per-row level.
    """
    cfg = _cfg()
    r_eq0 = cfg.R_EQ0_PII
    rows_dh = [
        {'t': 0.005, 'step': 31, 'N': 1, 'resolved': True,
         'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0},
        {'t': 0.010, 'step': 62, 'N': 1, 'resolved': True,
         'dH': 2e-3, 'n_antipodal': 0, 'r_eq': r_eq0},   # dH too large
    ]
    trace = _pii_trace(t_first=0.03, rows=rows_dh)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'INVALID', (
        f"|dH|=2e-3 > 1e-3 pre-bond must yield INVALID; got {out}")
    assert any('dH' in r or '2e-3' in r or '2.00e-03' in r for r in out['reasons']), (
        f"INVALID reason must mention dH; got {out['reasons']}")


def test_preflight_verdict_stable_reaches_t():
    """§11 item 2: STABLE requires rows to reach T.

    If rows don't reach T (e.g., run stopped early), gate must be INVALID.
    """
    cfg = _cfg()
    r_eq0 = cfg.R_EQ0_PII
    # Dense early rows (spacing 0.005) up to t=0.10 only; T=0.25 not reached.
    # Spacing check passes (all 0.005); only "STABLE doesn't reach T" fires.
    short_rows = [
        {'t': round(0.005 * (i + 1), 6), 'step': 31 * (i + 1), 'N': 1,
         'resolved': True, 'dH': 1e-5, 'n_antipodal': 0, 'r_eq': r_eq0}
        for i in range(20)  # t=0.005..0.100, spacing=0.005, last=0.100
    ]
    trace = _pii_trace(t_first=None, rows=short_rows)  # T=0.25 by default
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'INVALID', (
        f"STABLE with rows not reaching T must yield INVALID; got {out}")
    assert any('T=' in r or 'reach' in r or 'STABLE' in r for r in out['reasons']), (
        f"INVALID reason must mention T or STABLE; got {out['reasons']}")


# ---------------------------------------------------------------------------
# §11 item 3 — checkpoint steps pure function test (F5)
# ---------------------------------------------------------------------------


def test_checkpoint_steps():
    """§11 item 3 (F5): checkpoint_steps pure function — first-step-at-or-after rule.

    For P-ii dt=1.65e-4 and R2-PF dt=2.24e-4 grids:
      - Every checkpoint t_k is recorded at step s with s*dt >= t_k.
      - No checkpoint is missed (all indices covered).
      - Each step s is the FIRST step with s*dt >= t_k (not the step before).
      - Spacing between checkpoint times <= 0.005 for t <= 0.1.

    Kills: checkpoint hit logic reverted to exact-equality (round(t,10) in ckpt_set).
    """
    import sys, os as _os
    sys.path.insert(0, _os.path.join(_os.path.dirname(__file__),
                                     '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import checkpoint_steps, pf_checkpoint_times

    for dt in (1.65e-4, 2.24e-4):
        ckpts = pf_checkpoint_times(0.25)
        mapping = checkpoint_steps(ckpts, dt)

        # Every checkpoint index must be covered
        assert set(mapping.values()) == set(range(len(ckpts))), (
            f"dt={dt:.2e}: not all checkpoint indices covered; "
            f"got indices {sorted(mapping.values())}")

        # Each mapped step satisfies s*dt >= t_k (hit condition)
        # and (s-1)*dt < t_k (first hit)
        for step, idx in mapping.items():
            t_k = float(ckpts[idx])
            assert step * dt >= t_k - 1e-12, (
                f"dt={dt:.2e}: step={step}, s*dt={step*dt:.6f} < t_k={t_k:.6f}")
            if step > 1:
                assert (step - 1) * dt < t_k + 1e-12, (
                    f"dt={dt:.2e}: step={step} is not first; "
                    f"(s-1)*dt={((step-1)*dt):.6f} >= t_k={t_k:.6f}")


# ---------------------------------------------------------------------------
# §11 item 3 — r_first centre offset (F8)
# ---------------------------------------------------------------------------


def test_r_first_centre_offset():
    """§11 item 3 (F8): hedgehog geometric centre is (n-1)/2.0, not n//2.

    `_hedgehog_at(n, rc, (0,0,0))` places the hedgehog core at grid coordinate
    (0,0,0), which is INDEX (n-1)/2.0 per axis (grid(n) uses X[i]=i-(n-1)/2).
    The old runner used n//2 as the reference, offset by 0.5 per axis → 0.87 lu.

    This test confirms:
    1. The grid geometric centre for even n is (n-1)/2.0 (not n//2).
    2. argmin(q0) is closer to (n-1)/2.0 than to n//2.
    3. (n-1)/2.0 is within sqrt(3)*0.5+0.1 lattice units of argmin(q0).

    Kills: centre reverted to n//2 in run_preflight.
    """
    import sys, os as _os
    sys.path.insert(0, _os.path.join(_os.path.dirname(__file__),
                                     '..', 'scripts', 'vol_4_engineering'))
    from ave.topological.charge_counters import _hedgehog_at

    n_si = 32
    q = _hedgehog_at(n_si, 4, (0, 0, 0))

    # Core = argmin(q0): the site most inverted (f≈π)
    core_idx = np.array(np.unravel_index(np.argmin(q[..., 0]), q.shape[:3]),
                        dtype=float)

    geometric_centre = (n_si - 1) / 2.0  # = 15.5
    wrong_centre = float(n_si // 2)        # = 16.0 (old code)

    dist_correct = np.linalg.norm(core_idx - geometric_centre)
    dist_wrong = np.linalg.norm(core_idx - wrong_centre)

    # geometric_centre must be strictly closer to the core than wrong_centre
    assert dist_correct < dist_wrong, (
        f"(n-1)/2.0={geometric_centre} dist={dist_correct:.4f} from core, "
        f"n//2={wrong_centre} dist={dist_wrong:.4f}; "
        f"expected (n-1)/2.0 to be closer")

    # The 3D offset from wrong_centre to correct: sqrt(3)*0.5 ≈ 0.866
    expected_offset = np.sqrt(3) * 0.5
    actual_offset = float(np.linalg.norm(np.array([geometric_centre] * 3)
                                         - np.array([wrong_centre] * 3)))
    assert abs(actual_offset - expected_offset) < 1e-9, (
        f"n//2 → (n-1)/2.0 offset = {actual_offset:.6f}, expected {expected_offset:.6f}")

    # (n-1)/2.0 centre is within 1 lattice unit of the core (per-axis)
    assert dist_correct < np.sqrt(3) * 0.5 + 0.1, (
        f"dist from (n-1)/2.0 to core = {dist_correct:.4f} > 0.97 lu; "
        "wrong centre formula in run_preflight")


# ---------------------------------------------------------------------------
# §11 item 4 — 4 untested verdict branches (F9)
# ---------------------------------------------------------------------------


def test_preflight_verdict_r_eq0_pin_invalid():
    """§11 item 4 (F9): r_eq0 outside pin tolerance → INVALID.

    Kills: v7_preflight_r_eq0_check_off mutant.
    """
    cfg = _cfg()
    # Use wrong r_eq0 (too far from R_EQ0_PII=11.983; tol=0.005)
    wrong_r_eq0 = cfg.R_EQ0_PII + 1.0  # 12.983, well outside ±0.005
    trace = _pii_trace()
    trace = dict(trace, r_eq0=wrong_r_eq0)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'INVALID', (
        f"r_eq0={wrong_r_eq0} outside pin {cfg.R_EQ0_PII}±0.005 must yield INVALID; "
        f"got {out}")
    assert any('r_eq0' in r for r in out['reasons']), (
        f"INVALID reason must mention r_eq0; got {out['reasons']}")


def test_preflight_verdict_r_first_miss():
    """§11 item 4 (F9): r_first outside window [4, 11] → MISS.

    Kills: v7_r_first_window_off mutant.
    """
    cfg = _cfg()
    # r_first=2.0 is outside [4, 11] for PII_SPEC
    trace = _pii_trace(t_first=0.03, r_first=2.0, r_eq_ratio=0.98, n_antipodal_T=9)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'BREAKUP', f"expected BREAKUP; got {out}"
    assert out['a8'] == 'MISS', (
        f"r_first=2.0 ∉ [4, 11] must yield MISS; got {out}")
    assert any('r_first' in r for r in out['reasons']), (
        f"MISS reason must mention r_first; got {out['reasons']}")


def test_preflight_verdict_n_antipodal_miss():
    """§11 item 4 (F9): n_antipodal_T below minimum (< 5) → MISS.

    Kills: v7_n_antipodal_window_off mutant.
    """
    cfg = _cfg()
    # n_antipodal_T=3 is below min=5 for PII_SPEC
    trace = _pii_trace(t_first=0.03, r_first=6.0, r_eq_ratio=0.98, n_antipodal_T=3)
    out = cfg.preflight_verdict(trace, cfg.PII_SPEC)
    assert out['gate'] == 'BREAKUP', f"expected BREAKUP; got {out}"
    assert out['a8'] == 'MISS', (
        f"n_antipodal_T=3 < 5 must yield MISS; got {out}")
    assert any('n_antipodal' in r for r in out['reasons']), (
        f"MISS reason must mention n_antipodal; got {out['reasons']}")


# ---------------------------------------------------------------------------
# §11 item 5 — aggregator pre-collapse FAIL (Gate correction of delta §3.1.6)
# ---------------------------------------------------------------------------


def test_agg_pre_collapse_fail():
    """§11 item 5: pre-collapse resolved ≠ +6 → FAIL, even with later COLLAPSE.

    [+6]×3 + [+5] + COLLAPSE + [+6]×4 (expected 9) → "FAIL".
    Precedence: FAIL(#14) > FAIL (pre-collapse wrong) > COLLAPSE.
    Existing COLLAPSE tests (no pre-collapse wrong) are unaffected.
    """
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    '..', 'scripts', 'vol_4_engineering'))
    from csk4_r2_config import aggregate_r2_periods

    good = dict(resolved=True, value=6, reason=None,
                c_link_result=dict(resolved=True, value=6), c_exact_result=None)
    wrong = dict(resolved=True, value=5, reason=None,
                 c_link_result=dict(resolved=True, value=5), c_exact_result=None)
    collapse_r = dict(resolved=False, value=None, reason="COLLAPSE",
                      c_link_result=None, c_exact_result=None, collapse=True)

    # [+6]×3 + [+5] + COLLAPSE + [+6]×4 → FAIL (pre-collapse +5 outranks COLLAPSE)
    results = [good] * 3 + [wrong] + [collapse_r] + [good] * 4
    out = aggregate_r2_periods(results, expected_periods=9)
    assert out['verdict'] == 'FAIL', (
        f"pre-collapse wrong value must yield FAIL (not {out['verdict']}); "
        f"notes={out['notes']}")
    assert out['n_wrong'] == 1, f"expected n_wrong=1; got {out['n_wrong']}"

    # With r14_trip_period=1 < first_collapse_idx=4 → FAIL(#14) wins over FAIL
    out2 = aggregate_r2_periods(results, expected_periods=9, r14_trip_period=1)
    assert out2['verdict'] == 'FAIL(#14)', (
        f"r14 trip before collapse must yield FAIL(#14); got {out2['verdict']}")

    # [+6]×7 + COLLAPSE×2 (no pre-collapse wrong) → COLLAPSE (unchanged)
    results_no_wrong = [good] * 7 + [collapse_r] * 2
    out3 = aggregate_r2_periods(results_no_wrong, expected_periods=9)
    assert out3['verdict'] == 'COLLAPSE', (
        f"no pre-collapse wrong: COLLAPSE expected; got {out3['verdict']}")


# ---------------------------------------------------------------------------
# §11 fix 7c — AST + runtime guard: opt-in pre-flight seed path
# ---------------------------------------------------------------------------


def test_preflight_optin_seed_path_guard():
    """AST + runtime guard: opt-in pre-flight tests must use only
    run_preflight or preflight_initial_solver for initial state.

    Gate probe killed: v7_optin_ii_dynamic_seed_L64 (survivor at 61ae6cf4).

    AST checks each opt-in test function for:
      (a) a call to run_preflight or preflight_initial_solver;
      (b) no call to _hedgehog_at, hedgehog, rational, build_pf_seed,
          or preflight_setup;
      (c) no subscript assignment to a 'q0' key; no attribute assignment
          to <anything>.q (direct seed injection).

    Runtime check: preflight_initial_solver(pii_cfg, n=24, rc=12) yields
    cf.q whose sha1 (dead sites reset) equals preflight_setup seed_sha1,
    and differs from the L=n//2=12 seed sha1.
    Mutants killed:
      - opt-in test adding seed override (cf.q=... or setup['q0']=...);
      - opt-in test calling _hedgehog_at or any seed constructor directly;
      - preflight_initial_solver setting cf.q from an L=n/2 seed.
    """
    import ast
    import inspect
    import textwrap
    import hashlib
    import sys, os as _os

    sys.path.insert(0, _os.path.join(_os.path.dirname(__file__),
                                     '..', 'scripts', 'vol_4_engineering'))
    import csk4_r2_config as _cfg_mod
    from ave.topological.charge_counters import bcc_alive_mask, _hedgehog_at

    _ALLOWED_CALLS = frozenset({'run_preflight', 'preflight_initial_solver'})
    _FORBIDDEN_CALLS = frozenset({'_hedgehog_at', 'hedgehog', 'rational',
                                   'build_pf_seed', 'preflight_setup'})

    def _fn_name(node):
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            return node.attr
        return None

    def _check_target(target, lineno, forbidden_assigns):
        # <anything>.q = ... (direct solver seed injection)
        if isinstance(target, ast.Attribute) and target.attr == 'q':
            forbidden_assigns.append(
                (f'.q attribute assignment at line {lineno}', lineno))
        # <anything>['q0'] = ... (seed dict override)
        if isinstance(target, ast.Subscript):
            sl = target.slice
            key_val = None
            if isinstance(sl, ast.Constant):
                key_val = sl.value
            elif hasattr(ast, 'Index') and isinstance(sl, ast.Index):
                inner = sl.value
                if isinstance(inner, ast.Constant):
                    key_val = inner.value
                elif hasattr(inner, 's'):  # ast.Str (Python ≤ 3.7)
                    key_val = inner.s
            if key_val == 'q0':
                forbidden_assigns.append(
                    (f"subscript['q0'] assignment at line {lineno}", lineno))

    def _audit_fn(fn):
        src = textwrap.dedent(inspect.getsource(fn))
        tree = ast.parse(src)
        calls_allowed = False
        forbidden_calls = []
        forbidden_assigns = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = _fn_name(node.func)
                if name in _ALLOWED_CALLS:
                    calls_allowed = True
                if name in _FORBIDDEN_CALLS:
                    forbidden_calls.append((name, getattr(node, 'lineno', '?')))
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    _check_target(target, node.lineno, forbidden_assigns)
            elif isinstance(node, ast.AugAssign):
                _check_target(node.target, node.lineno, forbidden_assigns)
            elif isinstance(node, ast.AnnAssign) and node.target is not None:
                _check_target(node.target, node.lineno, forbidden_assigns)
        return calls_allowed, forbidden_calls, forbidden_assigns

    opt_in_fns = [
        test_r1_2d_option_ii_dynamic,
        test_r1_2d_option_ii_pii_preflight,
        test_r1_2d_option_ii_pii_control,
    ]

    for fn in opt_in_fns:
        fn_name = fn.__name__
        calls_ok, bad_calls, bad_assigns = _audit_fn(fn)
        assert calls_ok, (
            f"{fn_name}: check (a) — does not call run_preflight or "
            f"preflight_initial_solver; opt-in tests must obtain initial "
            f"state only through those functions")
        assert not bad_calls, (
            f"{fn_name}: check (b) — forbidden seed-constructor calls: "
            f"{bad_calls}; opt-in tests must not build seeds directly")
        assert not bad_assigns, (
            f"{fn_name}: check (c) — forbidden seed assignments: "
            f"{bad_assigns}; opt-in tests must not assign .q or ['q0'] directly")

    # Runtime check: preflight_initial_solver uses correct L (not L=n//2).
    # n=24, rc=12: L_standin = SEED_L_PII*12/12 = 48; n//2 = 12 — distinguishable.
    pii_cfg = _cfg_mod.make_pii_config(control=False)
    n_si, rc_si = 24, 12

    class _StubMinimal:
        def __init__(self, nn):
            self._q = None
            self.gamma = None
            self.k_op10 = None

        @property
        def q(self):
            return self._q

        @q.setter
        def q(self, val):
            self._q = val.copy()

    cf_si, setup_si = _cfg_mod.preflight_initial_solver(
        pii_cfg, n=n_si, rc=rc_si,
        make_solver=lambda nn: _StubMinimal(nn))

    # sha1 of cf.q after dead-site reset
    alive_si = bcc_alive_mask((n_si, n_si, n_si))
    q_actual = cf_si.q.copy()
    q_actual[~alive_si] = np.array([1.0, 0.0, 0.0, 0.0])
    actual_sha1 = hashlib.sha1(q_actual.tobytes()).hexdigest()

    # Must equal preflight_setup seed_sha1 (single builder anchor)
    assert actual_sha1 == setup_si['seed_sha1'], (
        f"preflight_initial_solver: cf.q sha1={actual_sha1!r} != "
        f"setup['seed_sha1']={setup_si['seed_sha1']!r}; "
        "initial state diverged from preflight_setup")

    # Must differ from L=n//2 wrong seed (kills L=n/2 mutant in preflight_initial_solver)
    q_wrong = _hedgehog_at(n_si, rc_si, (0, 0, 0), L=n_si // 2)
    q_wrong[~alive_si] = np.array([1.0, 0.0, 0.0, 0.0])
    wrong_sha1 = hashlib.sha1(q_wrong.tobytes()).hexdigest()
    assert actual_sha1 != wrong_sha1, (
        f"preflight_initial_solver: cf.q sha1 == L={n_si // 2} (=n//2) wrong seed; "
        f"n={n_si}, rc={rc_si}; L=n//2 mutant in preflight_initial_solver not killed")
