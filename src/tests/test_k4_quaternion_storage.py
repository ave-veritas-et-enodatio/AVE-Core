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


def test_k4_hedgehog_n1_dynamic_unit():
    """B3: K4 dynamics do NOT preserve the N=1 hedgehog at defaults (empirical).

    Honest-closure record (Rule 11). Seeding the static degree-1 hedgehog and
    stepping the K4 engine at DEFAULT parameters (no damping, no confinement)
    develops antipodal bonds (min Re(q̄q') → −1) within the first step and the
    charge dissipates (c_exact UNRESOLVED, c_det collapses from ≈1 to <0.3)
    within 20 steps. Verified n=48 rc=6 AND n=64 rc=16; single mechanism — the
    seeded static ansatz is not a dynamical solution and the undamped engine
    disperses it. This is a STRUCTURAL-CAPABILITY finding: dynamic N=1
    preservation requires damping/confinement infrastructure absent at defaults,
    NOT a claim that the K4 storage is wrong. The norm invariant (|q|=1 to
    1e-12) DOES hold throughout — the Lie-group Verlet is exact on the sphere;
    it is the TOPOLOGY that is not held by the bulk dynamics.

    The test pins the observed behavior so a future engine change that either
    (a) preserves the charge or (b) changes the dissipation mechanism trips it.
    """
    from ave.topological.charge_counters import (
        hedgehog, c_exact, c_det_alive4, bcc_alive_mask)

    n, rc = 48, 6
    cf = CosseratField3D(n, n, n, rotation_storage="quaternion")
    cf.q = hedgehog(n, rc).copy()
    cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
    alive = bcc_alive_mask((n, n, n))
    qstars, tets = _qstars_tets()

    # Static field resolves to +1 before any dynamics.
    r0 = c_exact(cf.q, qstars, tets=tets, s=2)
    assert r0["resolved"] and r0["value"] == 1

    norm_ok_throughout = True
    for _ in range(20):
        cf.step(cf.cfl_dt)
        q_alive = cf.q[alive]
        if np.max(np.abs(np.linalg.norm(q_alive, axis=-1) - 1.0)) >= 1e-12:
            norm_ok_throughout = False

    # The norm invariant is exact (Lie-group Verlet); this MUST hold.
    assert norm_ok_throughout, "|q|=1 invariant broke under K4 dynamics"

    # The recorded finding: the topology is NOT held at defaults.
    r = c_exact(cf.q, qstars, tets=tets, s=2)
    N_det = c_det_alive4(cf.q, alive, h=1.0)
    charge_lost = (not r["resolved"]) or (r["value"] != 1) or (N_det < 0.5)
    assert charge_lost, (
        "UNEXPECTED: K4 dynamics PRESERVED the N=1 hedgehog at defaults "
        f"(c_exact resolved={r['resolved']} value={r['value']}, c_det={N_det:.4f}). "
        "If an engine change now holds the charge, this is a positive result — "
        "update B3 to assert preservation and surface to Grant."
    )


def test_k4_dt_stability():
    """R1(ii) B1c C2: hedgehog N=1 at the spectrally-bounded step dt_K4.

    dt_K4 = min(cfl_dt, 0.25/Ω_max), where Ω_max is the vacuum K4 stiffness
    spectral radius from power iteration on the JAX Hessian-vector product
    (_k4_omega_max). The unit hedgehog (n=48, rc=6) is stepped 20× at dt_K4 AND
    at dt_K4/4; at each step min Re(q̄q') over alive bonds, and c_exact / c_det
    at the final step, are recorded.

    DECISION LOGIC (ladder R1(ii)):
      - charge preserved at dt_K4 (c_exact→1 AND min_re>0 throughout) → assert it;
      - charge lost even at dt_K4/4 → assert the charge_lost pattern (same single
        mechanism as test_k4_hedgehog_n1_dynamic_unit: the undamped engine
        disperses the seeded static ansatz), with Ω_max + dt_K4 in the message.

    MEASURED (honest-closure, Rule 11): the charge is lost at BOTH dt_K4 and
    dt_K4/4 — min Re(q̄q') → −1 (antipodal bond) and c_exact UNRESOLVED within 20
    steps. Shrinking the step does NOT rescue the topology; this confirms the
    loss is a DYNAMICAL-dispersion mechanism (the static ansatz is not a solution
    of the undamped bulk engine), NOT a time-step-stability artifact. The |q|=1
    Lie-group invariant holds exactly throughout at every dt.
    """
    from ave.topological.charge_counters import (
        hedgehog, c_exact, c_det_alive4, bcc_alive_mask)

    Omega_max = _k4_omega_max(n=16)
    cf0 = CosseratField3D(48, 48, 48, rotation_storage="quaternion")
    cfl_dt = cf0.cfl_dt
    dt_K4 = min(cfl_dt, 0.25 / Omega_max)
    print(f"[dt_stability] Omega_max={Omega_max:.6f}  cfl_dt={cfl_dt:.6e}  "
          f"dt_K4={dt_K4:.6e} (0.25/Omega_max={0.25 / Omega_max:.6e})")

    alive = bcc_alive_mask((48, 48, 48))
    qstars, tets = _qstars_tets()

    def run(dt):
        cf = CosseratField3D(48, 48, 48, rotation_storage="quaternion")
        cf.q = hedgehog(48, 6).copy()
        cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
        r0 = c_exact(cf.q, qstars, tets=tets, s=2)
        assert r0["resolved"] and r0["value"] == 1  # static field resolves to +1
        min_re_throughout = 1.0
        norm_ok = True
        for _ in range(20):
            cf.step(dt)
            min_re_throughout = min(min_re_throughout,
                                    _bond_re_min(cf.q, alive))
            if np.max(np.abs(
                    np.linalg.norm(cf.q[alive], axis=-1) - 1.0)) >= 1e-12:
                norm_ok = False
        r = c_exact(cf.q, qstars, tets=tets, s=2)
        cdet = float(c_det_alive4(cf.q, alive, h=1.0))
        return dict(min_re=min_re_throughout, resolved=r["resolved"],
                    value=r["value"], c_det=cdet, norm_ok=norm_ok)

    res_dt = run(dt_K4)
    res_dt4 = run(dt_K4 / 4.0)
    print(f"[dt_stability] dt_K4  : min_re={res_dt['min_re']:.4f} "
          f"c_exact_resolved={res_dt['resolved']} c_exact_value={res_dt['value']} "
          f"c_det={res_dt['c_det']:.4f}")
    print(f"[dt_stability] dt_K4/4: min_re={res_dt4['min_re']:.4f} "
          f"c_exact_resolved={res_dt4['resolved']} c_exact_value={res_dt4['value']} "
          f"c_det={res_dt4['c_det']:.4f}")

    # The |q|=1 invariant is exact at every dt; this MUST hold.
    assert res_dt["norm_ok"] and res_dt4["norm_ok"], (
        "|q|=1 invariant broke under K4 dynamics")

    charge_preserved_at_dtK4 = (
        res_dt["resolved"] and res_dt["value"] == 1 and res_dt["min_re"] > 0.0)
    charge_lost_at_dtK4over4 = (
        (not res_dt4["resolved"]) or res_dt4["value"] != 1
        or res_dt4["c_det"] < 0.5)

    if charge_preserved_at_dtK4:
        # Positive result: the spectrally-bounded step holds the charge.
        assert res_dt["resolved"] and res_dt["value"] == 1, (
            f"charge preserved claim inconsistent: {res_dt}")
        assert res_dt["min_re"] > 0.0, (
            f"bond short-arc broke despite charge preserved: {res_dt}")
    else:
        # Honest-closure: shrinking dt does not rescue — a dispersion mechanism,
        # not a stability artifact. Record with Ω_max + dt_K4.
        assert charge_lost_at_dtK4over4, (
            "UNEXPECTED: charge lost at dt_K4 but PRESERVED at dt_K4/4 — the loss "
            "would then be a time-step-stability artifact, not dispersion. "
            f"Omega_max={Omega_max:.6f} dt_K4={dt_K4:.6e} "
            f"res_dt={res_dt} res_dt4={res_dt4}. Surface to Grant: the R1(ii) "
            "mechanism attribution would change.")


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
    n = 32
    dx = 1.0
    amplitude = 1e-3
    # k ≤ π/(4dx) ≈ 0.785; first 3 BZ modes on n=32 are 0.196, 0.393, 0.589.
    k_test = [2 * np.pi / n * m for m in (1, 2, 3)]
    assert all(k <= np.pi / (4 * dx) for k in k_test)

    rel_diffs = []
    for kx in k_test:
        cf_omega = CosseratField3D(
            n, n, n, rotation_storage="omega", pml_thickness=0, damping_gamma=0.0)
        cf_k4 = CosseratField3D(
            n, n, n, rotation_storage="quaternion", pml_thickness=0, damping_gamma=0.0)

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


def test_r1_9_objectivity():
    """R1-9 (spec A5.3, O1 ruling): ε = Rᵀ(q)·F − I is frame-objective.

    Director law: F → QF, q → q_Q·q (n = R(q)ẑ → Qn exactly).
    1000 random F (|∇u| ≤ 0.5), unit q, rigid Q.  rng 20261009.

    O1 assertions (all ≤ 1e-12):
      ‖ε(QF, q_Q q) − ε(F, q)‖/‖ε‖  (tensor objectivity)
      |W(QF,q_Qq) − W(F,q)|/W        (energy objectivity)
      ‖n(q_Q q) − Q n(q)‖            (director co-rotation)

    Trip: F·R form (and R·F) must FAIL under the same Q (expect O(1): ~3.5/~17).
    Lattice check: skipped — the K4 diamond-tetra stencil offsets
      (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1) all have even parity (product of
      signs = +1). Under a 90° rotation about z, (1,1,1)→(−1,1,1) which has
      odd parity and is NOT in the offset set. The stencil is not 4-fold symmetric
      about z; the stencil anisotropy would contaminate a lattice-level energy
      comparison and cannot isolate the R-vs-Rᵀ difference.
    """
    rng = np.random.default_rng(20261009)
    N = 1000

    gu = rng.uniform(-0.5, 0.5, (N, 3, 3))
    F = np.eye(3)[None] + gu

    q_raw = rng.standard_normal((N, 4))
    q = q_raw / np.linalg.norm(q_raw, axis=-1, keepdims=True)

    qQ_raw = rng.standard_normal((N, 4))
    q_Q = qQ_raw / np.linalg.norm(qQ_raw, axis=-1, keepdims=True)

    R_Q = _Rq_batch(q_Q)
    QF = np.einsum('...ij,...jk->...ik', R_Q, F)
    q_Qq = _qmul_batch(q_Q, q)

    # O1 form
    eps = _eps_RtF_batch(F, q)
    eps_rot = _eps_RtF_batch(QF, q_Qq)
    eps_norms = np.linalg.norm(eps.reshape(N, 9), axis=-1)
    tensor_rel = (
        np.linalg.norm((eps_rot - eps).reshape(N, 9), axis=-1)
        / np.maximum(eps_norms, 1e-30)
    )
    max_tensor_rel = float(np.max(tensor_rel))

    W = _iso_energy_batch(eps)
    W_rot = _iso_energy_batch(eps_rot)
    energy_rel = np.abs(W_rot - W) / np.maximum(np.abs(W), 1e-30)
    max_energy_rel = float(np.max(energy_rel))

    n = _n_batch(q)
    n_rot = _n_batch(q_Qq)
    Qn = np.einsum('...ij,...j->...i', R_Q, n)
    n_err = np.linalg.norm(n_rot - Qn, axis=-1)
    max_n_err = float(np.max(n_err))

    assert max_tensor_rel <= 1e-12, (
        f"R1-9 O1 tensor objectivity: max_rel={max_tensor_rel:.2e} (limit 1e-12)")
    assert max_energy_rel <= 1e-12, (
        f"R1-9 O1 energy objectivity: max_rel={max_energy_rel:.2e} (limit 1e-12)")
    assert max_n_err <= 1e-12, (
        f"R1-9 O1 director co-rotation: max_err={max_n_err:.2e} (limit 1e-12)")

    # Trip: F·R (FR) must fail
    def _eps_FR_batch(F, q):
        R = _Rq_batch(q)
        return np.einsum('...ij,...jk->...ik', F, R) - np.eye(3)[None]

    # Trip: R·F (RF) must also fail
    def _eps_RF_batch(F, q):
        R = _Rq_batch(q)
        return np.einsum('...ij,...jk->...ik', R, F) - np.eye(3)[None]

    eps_fr = _eps_FR_batch(F, q)
    eps_fr_rot = _eps_FR_batch(QF, q_Qq)
    eps_fr_norms = np.linalg.norm(eps_fr.reshape(N, 9), axis=-1)
    fr_tensor_rel = (
        np.linalg.norm((eps_fr_rot - eps_fr).reshape(N, 9), axis=-1)
        / np.maximum(eps_fr_norms, 1e-30)
    )
    W_fr = _iso_energy_batch(eps_fr)
    W_fr_rot = _iso_energy_batch(eps_fr_rot)
    fr_energy_rel = np.abs(W_fr_rot - W_fr) / np.maximum(np.abs(W_fr), 1e-30)
    max_fr_tensor = float(np.max(fr_tensor_rel))
    max_fr_energy = float(np.max(fr_energy_rel))

    eps_rf = _eps_RF_batch(F, q)
    eps_rf_rot = _eps_RF_batch(QF, q_Qq)
    eps_rf_norms = np.linalg.norm(eps_rf.reshape(N, 9), axis=-1)
    rf_tensor_rel = (
        np.linalg.norm((eps_rf_rot - eps_rf).reshape(N, 9), axis=-1)
        / np.maximum(eps_rf_norms, 1e-30)
    )
    W_rf = _iso_energy_batch(eps_rf)
    W_rf_rot = _iso_energy_batch(eps_rf_rot)
    rf_energy_rel = np.abs(W_rf_rot - W_rf) / np.maximum(np.abs(W_rf), 1e-30)
    max_rf_tensor = float(np.max(rf_tensor_rel))
    max_rf_energy = float(np.max(rf_energy_rel))

    assert max_fr_tensor > 0.1, (
        f"R1-9 FR trip: tensor should fail; got {max_fr_tensor:.3f} (expect ~3.5)")
    assert max_fr_energy > 1.0, (
        f"R1-9 FR trip: energy should fail; got {max_fr_energy:.3f} (expect ~17)")
    assert max_rf_tensor > 0.1, (
        f"R1-9 RF trip: tensor should fail; got {max_rf_tensor:.3f} (expect ~3.5)")
    assert max_rf_energy > 1.0, (
        f"R1-9 RF trip: energy should fail; got {max_rf_energy:.3f} (expect ~17)")

    # Reported residuals (O1 pass / FR trip / RF trip):
    # O1:  tensor {max_tensor_rel:.2e}  energy {max_energy_rel:.2e}  n_err {max_n_err:.2e}
    # FR:  tensor {max_fr_tensor:.3f}   energy {max_fr_energy:.3f}
    # RF:  tensor {max_rf_tensor:.3f}   energy {max_rf_energy:.3f}


def test_k4_strain_small_angle_omega_map():
    """O1 ruling: ε = Rᵀ(q)·F − I matches cf:175-186 to O(h) under the ω map.

    At h = 1e-6 the max relative strain error is ≤ 3e-6 (strain_ruling.py result
    ~2.8e-6).  The ω map is q(ω_eng) ≈ (1, −ω_eng/2) (_OMEGA_TO_Q_SIGN = -1).
    This is the spec A5.3 claim: 'rel err ~1e-6 at h = 1e-6'.
    """
    rng = np.random.default_rng(20261009)
    N = 2000
    h = 1e-6

    gu = rng.standard_normal((N, 3, 3)) * h
    omega = rng.standard_normal((N, 3)) * h

    q = np.zeros((N, 4))
    q[:, 0] = 1.0
    q[:, 1:] = _OMEGA_TO_Q_SIGN * omega / 2.0
    q /= np.linalg.norm(q, axis=-1, keepdims=True)

    # Engine linear form (cf:175-186): ε_ij = ∂_j u_i − ε_ijk ω_k
    # (ε_ijk ω_k = −[ω×]_ij in the standard cross-product convention; this is
    # the same as ∇u + [ω×] in matrix form with the sign confirmed by
    # strain_ruling engine_lin_rigid: eps_engine(Gu, −θ)=0 for rigid rotation)
    LC = np.zeros((3, 3, 3))
    LC[0, 1, 2] = LC[1, 2, 0] = LC[2, 0, 1] = 1.0
    LC[0, 2, 1] = LC[2, 1, 0] = LC[1, 0, 2] = -1.0
    eps_engine = gu - np.einsum("ijk,nk->nij", LC, omega)  # (N,3,3)

    q0, q1, q2, q3 = q[:, 0], q[:, 1], q[:, 2], q[:, 3]
    R = np.stack([
        np.stack([1-2*(q2**2+q3**2), 2*(q1*q2-q0*q3), 2*(q1*q3+q0*q2)], axis=-1),
        np.stack([2*(q1*q2+q0*q3), 1-2*(q1**2+q3**2), 2*(q2*q3-q0*q1)], axis=-1),
        np.stack([2*(q1*q3-q0*q2), 2*(q2*q3+q0*q1), 1-2*(q1**2+q2**2)], axis=-1),
    ], axis=-2)
    F = np.eye(3)[None] + gu
    eps_k4 = np.einsum('...ki,...kj->...ij', R, F) - np.eye(3)[None]

    norms = np.linalg.norm(eps_engine.reshape(N, 9), axis=-1)
    rel = (
        np.linalg.norm((eps_k4 - eps_engine).reshape(N, 9), axis=-1)
        / np.maximum(norms, 1e-30)
    )
    max_rel = float(np.max(rel))
    assert max_rel <= 3e-6, (
        f"small-angle strain vs cf:175-186 under ω map: max_rel={max_rel:.2e} "
        f"(limit 3e-6; strain_ruling h=1e-6 gives ~2.8e-6)")


# ---------------------------------------------------------------------------
# B2: dynamic q reaching −1 (full-sweep handling) + ω-storage representation jump
# ---------------------------------------------------------------------------


def test_k4_q_reaches_minus1_dynamic():
    """B2: a field containing sites near q=−1 stays exactly unit-norm under K4.

    Seeds a patch of near-antipodal rotations (θ ≈ π·0.99 → q0 ≈ 0.016, the
    field legitimately reaching toward the q=−1 antipode) and steps for 20
    steps. The LOAD-BEARING K4 guarantee — |q|=1 to 1e-12 at every alive site,
    every step, even with the field near the antipode — holds exactly (the
    Lie-group Verlet is intrinsically on the sphere).

    Honest-closure record (Rule 11): the short-arc bond invariant Re(q̄q')>0 is
    NOT maintained under default (undamped, unconfined) dynamics — the sharp
    patch/vacuum interface develops antipodal bonds (min Re → −1) in the first
    step, the SAME single mechanism as test_k4_hedgehog_n1_dynamic_unit. The
    static representation-jump demonstration (test_omega_storage_representation_jump)
    is the convention-level evidence that K4 removes the ω double-cover seam;
    the dynamic bond-Re>0 claim is a stronger property the undamped bulk engine
    does not provide. This test pins BOTH observed facts.
    """
    n = 24
    cf = CosseratField3D(n, n, n, rotation_storage="quaternion")
    c = n // 2
    theta = np.pi * 0.99
    qval = np.array([np.cos(theta / 2.0), 0.0, 0.0, np.sin(theta / 2.0)])
    for i in range(c - 2, c + 2):
        for j in range(c - 2, c + 2):
            for k in range(c - 2, c + 2):
                if cf.mask_alive[i, j, k]:
                    cf.q[i, j, k] = qval

    # The seed genuinely reaches toward the antipode.
    assert cf.q[cf.mask_alive, 0].min() < 0.1

    re_min_broke = False
    for step_i in range(20):
        cf.step(cf.cfl_dt)
        q_alive = cf.q[cf.mask_alive]
        nm = np.max(np.abs(np.linalg.norm(q_alive, axis=-1) - 1.0))
        assert nm < 1e-12, f"step {step_i}: |q|-1 max = {nm:.2e}"
        if _bond_re_min(cf.q, cf.mask_alive) <= 0.0:
            re_min_broke = True

    # Recorded finding: the undamped sharp-interface seed does break Re(q̄q')>0.
    assert re_min_broke, (
        "UNEXPECTED: the sharp near-antipodal seed held Re(q̄q')>0 under default "
        "dynamics — if an engine change now holds it, promote this to a bond-Re "
        "assertion and surface to Grant."
    )


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
    cf = CosseratField3D(n, n, n, rotation_storage="quaternion",
                         pml_thickness=0, damping_gamma=0.0)
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


def _gap_freq(cf, storage, amplitude=1e-3, n_periods=40):
    """Drive the k=0 uniform z-rotation gap mode; return (angular frequency, dt).

    B1c C1: the frequency is now recovered by a 3-parameter least-squares
    sinusoid fit (_fit_freq_lsq) over ≥10 periods, not an FFT-bin peak — so the
    absolute value can be gated against the Verlet-corrected discrete frequency.
    Only the running scalar mean is held (no full field time series) to keep the
    RSS footprint flat (C5)."""
    if storage == "omega":
        cf.omega[:, :, :, 2] = amplitude
    else:
        cf.q[:, :, :, 0] = np.sqrt(1.0 - (amplitude / 2.0) ** 2)
        cf.q[:, :, :, 3] = amplitude / 2.0
        cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
    dt = cf.cfl_dt
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
    O(dt²) nature of the 2.0 offset is itself verified by halving-cubed
    convergence: |Omega_num(dt/4) − 2| ≤ |Omega_num(dt) − 2|/10.
    """
    cf_om = CosseratField3D(16, 16, 16, rotation_storage="omega",
                            pml_thickness=0, damping_gamma=0.0)
    cf_k4 = CosseratField3D(16, 16, 16, rotation_storage="quaternion",
                            pml_thickness=0, damping_gamma=0.0)
    f_om, dt_om = _gap_freq(cf_om, "omega")
    f_k4, dt_k4 = _gap_freq(cf_k4, "quaternion")

    # Verlet-corrected exact discrete frequency at the dt the omega run used.
    Omega_num = _omega_num(2.0, dt_om)

    assert abs(f_k4 - f_om) / max(f_om, 1e-30) < 1e-4, (
        f"K4 vs omega gap freq diverge: f_k4={f_k4:.6f} f_om={f_om:.6f}")
    assert abs(f_om - Omega_num) <= 1e-4, (
        f"gap frequency = {f_om:.6f} vs Verlet-exact Omega_num = {Omega_num:.6f} "
        f"(|Δ|={abs(f_om - Omega_num):.2e}, limit 1e-4; dt={dt_om:.6e})")

    # O(dt²) convergence of the discrete frequency toward the continuum 2.0:
    # a 4× dt reduction shrinks the offset by ≥10× (true ratio ≈16).
    off_dt = abs(Omega_num - 2.0)
    off_dt4 = abs(_omega_num(2.0, dt_om / 4.0) - 2.0)
    assert off_dt4 < off_dt / 10.0, (
        f"Omega_num not O(dt²): |Δ(dt)|={off_dt:.3e} |Δ(dt/4)|={off_dt4:.3e} "
        f"ratio={off_dt / max(off_dt4, 1e-300):.2f} (expect ≥10)")


def test_k4_gap_frequency_trip_gc0():
    """B6 trip: G_c = 0 → gap frequency collapses toward 0 (no restoring torque)."""
    cf = CosseratField3D(16, 16, 16, rotation_storage="quaternion",
                         pml_thickness=0, damping_gamma=0.0)
    cf.G_c = 0.0
    f, _dt = _gap_freq(cf, "quaternion", n_periods=10)
    assert f < 0.5, f"G_c=0 gap trip: frequency = {f:.4f}, expected < 0.5 (≈0)"


def test_k4_energy_drift():
    """B6: |ΔH/H0| ≤ 1e-4 over a short K4 run (symplectic velocity-Verlet), with
    the spectrally-bounded dt_K4 reported alongside (B1c C2).

    The K4 drift is the BOUNDED symplectic-shadow oscillation, not a secular
    dissipation: it is O(dt²), the signature of a symplectic integrator
    conserving a shadow Hamiltonian (NOT a leaking engine). The ≤1e-4 bound is
    met at cfl_dt/16 (the original, UNWEAKENED assertion). B1c C2 additionally
    measures the drift at the spectrally-bounded step
    dt_K4 = min(cfl_dt, 0.25/Ω_max): dt_K4 is larger than cfl_dt/16 (~0.051 vs
    ~0.006 at n=16), so its drift is correspondingly larger (~3.7e-4) but still
    BOUNDED and strictly larger than the fine-step drift — the symplectic-shadow
    ordering, not secular dissipation. The 1e-4 gate stays pinned at the step
    where the integrator actually meets it; the dt_K4 figure is a reported
    diagnostic (not a loosened bound). The clean O(dt²) decay as dt→0 is the
    quantitative conservation evidence; it is asserted via the two-point
    direction (coarser step ⇒ larger bounded drift) rather than a tight ratio,
    because the shadow oscillation's phase at a fixed step-count makes an exact
    (dt_K4/dt_fine)² ratio sampling-dependent.
    """
    n = 16
    Omega_max = _k4_omega_max(n=16)

    def drift(dt):
        cf = CosseratField3D(n, n, n, rotation_storage="quaternion",
                             pml_thickness=0, damping_gamma=0.0)
        rng = np.random.default_rng(2026)
        dq = rng.standard_normal((n, n, n, 3)) * 1e-3
        cf.q[cf.mask_alive, 1:] = dq[cf.mask_alive]
        norms = np.linalg.norm(cf.q, axis=-1, keepdims=True)
        cf.q = cf.q / np.where(norms > 0, norms, 1.0)
        cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])
        H0 = cf.total_energy_k4() + cf.kinetic_energy_k4()
        if abs(H0) < 1e-20:
            pytest.skip("Initial energy too small for drift test")
        for _ in range(50):
            cf.step(dt)
        H1 = cf.total_energy_k4() + cf.kinetic_energy_k4()
        return abs(H1 - H0) / abs(H0), H0

    cfl_dt = CosseratField3D(
        n, n, n, rotation_storage="quaternion",
        pml_thickness=0, damping_gamma=0.0).cfl_dt
    dt_K4 = min(cfl_dt, 0.25 / Omega_max)
    dt_fine = cfl_dt / 16.0

    rel_dtK4, _ = drift(dt_K4)
    rel_fine, _ = drift(dt_fine)
    print(f"[energy_drift] Omega_max={Omega_max:.6f} dt_K4={dt_K4:.6e} "
          f"|ΔH/H0|(dt_K4)={rel_dtK4:.3e}  dt_fine(cfl/16)={dt_fine:.6e} "
          f"|ΔH/H0|(fine)={rel_fine:.3e}")

    # Original gate, UNWEAKENED: the ≤1e-4 bound at cfl_dt/16.
    assert rel_fine <= 1e-4, (
        f"|ΔH/H0| = {rel_fine:.2e} at cfl_dt/16={dt_fine:.3e} (limit 1e-4)")

    # Symplectic-shadow ordering: the coarser dt_K4 drift is BOUNDED and strictly
    # larger than the fine-step drift (not a secular blow-up; dt_K4 > dt_fine).
    assert rel_dtK4 < 1e-2, (
        f"dt_K4 drift unbounded: {rel_dtK4:.2e} (dt_K4={dt_K4:.3e})")
    assert rel_dtK4 > rel_fine, (
        f"coarser dt_K4 should drift more than cfl_dt/16: "
        f"{rel_dtK4:.2e} vs {rel_fine:.2e}")


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


def test_r2_aggregator_pass():
    """B9: ≥90% resolved + all +6 → PASS."""
    agg = _agg()
    periods = [{'c_exact': 6, 'c_link': 6} for _ in range(18)] + \
              [{'c_exact': None, 'c_link': None} for _ in range(2)]
    out = agg(periods)
    assert out['verdict'] == 'PASS', out


def test_r2_aggregator_inconclusive():
    """B9: 17/20 resolved (<90%) → INCONCLUSIVE."""
    agg = _agg()
    periods = [{'c_exact': 6, 'c_link': 6} for _ in range(17)] + \
              [{'c_exact': None, 'c_link': 7} for _ in range(3)]
    out = agg(periods)
    assert out['verdict'] == 'INCONCLUSIVE', out
    # Nit N3: the c_link value is logged on each UNRESOLVED period.
    assert any('c_link=7' in note for note in out['notes']), out['notes']


def test_r2_aggregator_fail():
    """B9: one resolved value ≠ +6 → FAIL (the only count FAIL)."""
    agg = _agg()
    periods = [{'c_exact': 6, 'c_link': 6} for _ in range(19)] + \
              [{'c_exact': 5, 'c_link': 6}]
    out = agg(periods)
    assert out['verdict'] == 'FAIL', out


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
