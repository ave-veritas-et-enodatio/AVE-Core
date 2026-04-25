"""F17-K Phase 5c — coupled K4+Cosserat S₁₁ relaxation eigenmode finder.

Per [doc 68_ §7](../../research/L3_electron_soliton/68_phase_quadrature_methodology.md#L7)
the AVE-native (Axiom-3 / Effective Action Principle) eigenmode finder
for the coupled engine is **gradient descent on |S₁₁|²** over the joint
state (V_inc, u, ω), not raw VacuumEngine3D.step() time-evolution.

Mirrors `cosserat_field_3d.py:relax_s11` (Cosserat-only, validated by
[doc 34_ X4b](../../research/L3_electron_soliton/34_x4_constrained_s11.md))
and extends to coupled engine by composing total saturation:

    A²_total(x) = V_sq(x)/V_SNAP² + ε²(x)/ε_yield² + κ²(x)/ω_yield²

where V_sq(x) = Σ_p V_inc[..., p]² (engine convention per
`k4_cosserat_coupling.py:_v_squared_per_site`). Saturation
S = √(1-A²_total), Op14 impedance Z_eff = 1/√S, Op3 reflection per
tetrahedral neighbor. Coupled S₁₁ = Σ_x mask_alive(x) · Σ_p |Γ_p|².

Note: V_ref is NOT in the gradient descent state. V_ref is a derived
quantity from V_inc via TLM scatter+connect; it gets reset each
engine.step() call (which we don't call during S11 relaxation —
relaxation is gradient descent, not time-evolution).
"""
from __future__ import annotations
import sys

import jax
import jax.numpy as jnp
import numpy as np

sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src/scripts/vol_1_foundations")

from ave.topological.cosserat_field_3d import (
    _compute_strain, _compute_curvature, TETRA_OFFSETS,
)
from ave.topological.vacuum_engine import VacuumEngine3D


@jax.jit
def _coupled_a_sq(
    u: jnp.ndarray, omega: jnp.ndarray, V_inc: jnp.ndarray,
    dx: float, omega_yield: float, epsilon_yield: float, V_SNAP: float,
) -> jnp.ndarray:
    """A²_total(x) = V_sq/V_SNAP² + ε²/ε_yield² + κ²/ω_yield² per site."""
    eps = _compute_strain(u, omega, dx)
    kappa = _compute_curvature(omega, dx)
    eps_sq = jnp.sum(eps * eps, axis=(-1, -2))
    kappa_sq = jnp.sum(kappa * kappa, axis=(-1, -2))
    A_sq_cos = eps_sq / (epsilon_yield ** 2) + kappa_sq / (omega_yield ** 2)
    A_sq_k4 = jnp.sum(V_inc ** 2, axis=-1) / (V_SNAP ** 2)
    return A_sq_cos + A_sq_k4


@jax.jit
def _s11_density_coupled(
    u: jnp.ndarray, omega: jnp.ndarray, V_inc: jnp.ndarray,
    dx: float, omega_yield: float, epsilon_yield: float, V_SNAP: float,
) -> jnp.ndarray:
    """Σ_p |Γ_p|² per site (Op14+Op3 chain on coupled A²).

    Mirrors cosserat_field_3d._s11_density but uses coupled A².
    """
    A_sq = _coupled_a_sq(u, omega, V_inc, dx, omega_yield, epsilon_yield, V_SNAP)
    A_sq_clipped = jnp.clip(A_sq, 0.0, 1.0 - 1e-10)
    S = jnp.sqrt(1.0 - A_sq_clipped)
    S_safe = jnp.maximum(S, 1e-6)
    Z_eff = 1.0 / jnp.sqrt(S_safe)

    gamma_sq_total = jnp.zeros_like(Z_eff)
    for p in TETRA_OFFSETS:
        Z_neighbor = jnp.roll(Z_eff, shift=(-p[0], -p[1], -p[2]), axis=(0, 1, 2))
        gamma = (Z_neighbor - Z_eff) / (Z_neighbor + Z_eff + 1e-12)
        gamma_sq_total = gamma_sq_total + gamma * gamma
    return gamma_sq_total


@jax.jit
def _total_s11_coupled(
    u: jnp.ndarray, omega: jnp.ndarray, V_inc: jnp.ndarray,
    mask_alive: jnp.ndarray, dx: float, omega_yield: float,
    epsilon_yield: float, V_SNAP: float,
) -> jnp.ndarray:
    rho = _s11_density_coupled(u, omega, V_inc, dx, omega_yield, epsilon_yield, V_SNAP)
    return jnp.sum(rho * mask_alive.astype(rho.dtype))


_val_and_grad_s11_coupled = jax.jit(
    jax.value_and_grad(_total_s11_coupled, argnums=(0, 1, 2))
)


def total_s11_coupled(engine: VacuumEngine3D) -> float:
    """Field-level coupled S11 objective on (u, ω, V_inc) joint state."""
    u_j = jnp.asarray(engine.cos.u)
    w_j = jnp.asarray(engine.cos.omega)
    V_j = jnp.asarray(engine.k4.V_inc)
    return float(_total_s11_coupled(
        u_j, w_j, V_j,
        engine.cos._mask_alive_jax,
        engine.cos.dx,
        engine.cos.omega_yield, engine.cos.epsilon_yield,
        float(engine.V_SNAP),
    ))


def s11_gradient_coupled(
    engine: VacuumEngine3D,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Joint gradient (∂S11/∂u, ∂S11/∂ω, ∂S11/∂V_inc) via JAX autodiff."""
    u_j = jnp.asarray(engine.cos.u)
    w_j = jnp.asarray(engine.cos.omega)
    V_j = jnp.asarray(engine.k4.V_inc)
    _, (dS_du, dS_dw, dS_dV) = _val_and_grad_s11_coupled(
        u_j, w_j, V_j,
        engine.cos._mask_alive_jax,
        engine.cos.dx,
        engine.cos.omega_yield, engine.cos.epsilon_yield,
        float(engine.V_SNAP),
    )
    cos_mask = engine.cos._mask_alive_jax[..., None].astype(dS_du.dtype)
    k4_mask = jnp.asarray(engine.k4.mask_active).astype(dS_dV.dtype)[..., None]
    return (
        np.asarray(dS_du * cos_mask),
        np.asarray(dS_dw * cos_mask),
        np.asarray(dS_dV * k4_mask),
    )


def relax_s11_coupled(
    engine: VacuumEngine3D,
    max_iter: int = 500,
    tol: float = 1e-8,
    initial_lr: float = 1e-3,
    verbose: bool = False,
    track_every: int = 25,
) -> dict:
    """Joint gradient descent on coupled total_s11 over (u, ω, V_inc).

    Backtracking line-search: accept step if S11_new ≤ S11_prev (with
    noise floor); else halve lr and retry. Same structure as
    `cosserat_field_3d.py:relax_s11`.

    Returns dict with iterations, final_s11, converged bool, history,
    trajectory (per-track_every snapshot of S11 + topology + amplitudes),
    lr_final.
    """
    lr = initial_lr
    history: list[float] = []
    trajectory: list[dict] = []

    S11_prev = total_s11_coupled(engine)
    history.append(S11_prev)
    noise_floor = 1e-12 * max(abs(S11_prev), 1.0)

    def _snapshot(step: int, S11: float, lr_now: float) -> dict:
        c_cos = int(engine.cos.extract_crossing_count())
        peak_omega = float(np.max(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1)))
        peak_V = float(np.max(np.abs(np.asarray(engine.k4.V_inc))))
        E_cos = float(engine.cos.total_energy())
        E_k4 = float(np.sum(np.asarray(engine.k4.V_inc) ** 2))
        return {
            "step": step, "S11": S11, "c_cos": c_cos,
            "peak_omega": peak_omega, "peak_V": peak_V,
            "E_cos": E_cos, "E_k4": E_k4, "lr": lr_now,
        }

    if track_every > 0:
        snap = _snapshot(0, S11_prev, lr)
        trajectory.append(snap)
        if verbose:
            print(f"  step {0:5d}  S11={snap['S11']:.6e}  c={snap['c_cos']}  "
                  f"|ω|={snap['peak_omega']:.3f}  |V|={snap['peak_V']:.4f}  "
                  f"E_k4={snap['E_k4']:.3e}  lr={snap['lr']:.2e}")

    for step in range(max_iter):
        u_save = engine.cos.u.copy()
        w_save = engine.cos.omega.copy()
        V_save = engine.k4.V_inc.copy()

        dS_du, dS_dw, dS_dV = s11_gradient_coupled(engine)
        engine.cos.u = engine.cos.u - lr * dS_du
        engine.cos.omega = engine.cos.omega - lr * dS_dw
        engine.k4.V_inc = engine.k4.V_inc - lr * dS_dV
        engine.cos._zero_outside_alive()
        engine.k4.V_inc = np.where(
            engine.k4.mask_active[..., None], engine.k4.V_inc, 0.0
        )

        S11_new = total_s11_coupled(engine)

        if S11_new <= S11_prev + noise_floor:
            rel_change = abs(S11_new - S11_prev) / max(abs(S11_prev), 1e-12)
            history.append(S11_new)

            if track_every > 0 and ((step + 1) % track_every == 0):
                snap = _snapshot(step + 1, S11_new, lr)
                trajectory.append(snap)
                if verbose:
                    print(f"  step {step+1:5d}  S11={snap['S11']:.6e}  c={snap['c_cos']}  "
                          f"|ω|={snap['peak_omega']:.3f}  |V|={snap['peak_V']:.4f}  "
                          f"E_k4={snap['E_k4']:.3e}  lr={snap['lr']:.2e}")

            if step > 10 and rel_change < tol:
                return {
                    "iterations": step + 1, "final_s11": S11_new,
                    "converged": True, "history": history,
                    "trajectory": trajectory, "lr_final": lr,
                }
            lr = min(lr * 1.1, 1.0)
            S11_prev = S11_new
            noise_floor = 1e-12 * max(abs(S11_prev), 1.0)
        else:
            engine.cos.u = u_save
            engine.cos.omega = w_save
            engine.k4.V_inc = V_save
            lr *= 0.5
            if lr < 1e-14:
                return {
                    "iterations": step + 1, "final_s11": S11_prev,
                    "converged": False, "history": history,
                    "trajectory": trajectory, "lr_final": lr,
                    "note": "lr collapsed",
                }

    return {
        "iterations": max_iter, "final_s11": S11_prev,
        "converged": False, "history": history,
        "trajectory": trajectory, "lr_final": lr,
    }


# ─── Phase 5c driver ──────────────────────────────────────────────────────────

def run_phase5c_validation(
    N: int = 80, R: float = 20.0,
    V_amp: float = 0.05, chirality: float = 1.0,
    max_iter: int = 500, initial_lr: float = 1e-3,
) -> dict:
    """Full Phase 5c validation: phase-quadrature seed → coupled S11 relax."""
    PHI_SQ = ((1 + np.sqrt(5)) / 2) ** 2
    r = R / PHI_SQ
    cos_amp = 0.3 / (np.sqrt(3.0) / 2.0)

    print("=" * 78)
    print(f"  F17-K Phase 5c: coupled S₁₁ relaxation at N={N}")
    print("=" * 78)
    print(f"  Engine: A28+self-terms")
    print(f"  Seed: phase-quadrature (V_amp={V_amp}, chirality={chirality}) + Cosserat ω")
    print(f"  R={R}, r={r:.4f}, max_iter={max_iter}, initial_lr={initial_lr}")
    print()

    engine = VacuumEngine3D.from_args(
        N=N, pml=4, temperature=0.0,
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )

    from tlm_electron_soliton_eigenmode import initialize_quadrature_2_3_eigenmode
    initialize_quadrature_2_3_eigenmode(
        engine.k4, R=R, r=r, amplitude=V_amp, chirality=chirality,
    )
    engine.cos.initialize_electron_2_3_sector(
        R_target=R, r_target=r, use_hedgehog=True, amplitude_scale=cos_amp,
    )

    print("  --- Initial state ---")
    S0 = total_s11_coupled(engine)
    c0 = int(engine.cos.extract_crossing_count())
    print(f"  S11_initial = {S0:.4e}")
    print(f"  c_cos = {c0}")
    print(f"  |ω|peak = {float(np.max(np.linalg.norm(engine.cos.omega, axis=-1))):.4f}")
    print(f"  |V|peak = {float(np.max(np.abs(engine.k4.V_inc))):.4f}")
    print()

    print("  --- relax_s11_coupled ---")
    import time
    t0 = time.time()
    result = relax_s11_coupled(
        engine, max_iter=max_iter, tol=1e-7,
        initial_lr=initial_lr, verbose=True, track_every=25,
    )
    elapsed = time.time() - t0

    print()
    print("  --- Final state ---")
    print(f"  iterations:  {result['iterations']}/{max_iter}")
    print(f"  converged:   {result['converged']}")
    print(f"  S11_final:   {result['final_s11']:.4e}  (S11/S0 = {result['final_s11']/S0:.4f})")
    print(f"  c_cos:       {int(engine.cos.extract_crossing_count())}  (target 3)")
    print(f"  |ω|peak:     {float(np.max(np.linalg.norm(engine.cos.omega, axis=-1))):.4f}")
    print(f"  |V|peak:     {float(np.max(np.abs(engine.k4.V_inc))):.4f}")
    print(f"  E_cos:       {float(engine.cos.total_energy()):.3e}")
    print(f"  E_k4:        {float(np.sum(engine.k4.V_inc ** 2)):.3e}")
    print(f"  elapsed:     {elapsed:.1f}s ({elapsed/60:.1f} min)")

    return result


if __name__ == "__main__":
    run_phase5c_validation(N=80, max_iter=500)


# ─── Phase 5c-v2: dual descent with tanh reparameterization ───────────────────
# Per [doc 67_ §23](../../research/L3_electron_soliton/67_lc_coupling_reciprocity_audit.md#L23):
# v1's spurious convergence was Cosserat over-saturation (|ω| 0.94 → 2.19). v2
# fixes this via HARD reparameterization (tanh-bounded amplitude in parameter
# space) instead of soft Lagrange penalties. Per doc 03_ §4.1-4.3, the Ch 8
# Golden Torus constraints are NATURAL EQUILIBRIA, not constraints to impose —
# so v2 has NO geometric or topology penalties. Just amplitude reparameterization.
#
# Dual descent runs both objectives from the same seed:
#   - Cosserat-energy: minimize E_Cos[u, ω] (per doc 03_ §1)
#   - |S₁₁|² coupled: minimize total_s11_coupled (per doc 34_ X4b template)
# Corpus claim per Vol 1 Ch 8: they co-locate at Golden Torus.

from ave.topological.cosserat_field_3d import _total_energy_saturated


@jax.jit
def _reparam_omega(omega_param: jnp.ndarray, omega_yield: float) -> jnp.ndarray:
    """ω_actual = ω_yield · tanh(ω_param / ω_yield). |ω| < ω_yield by construction."""
    return omega_yield * jnp.tanh(omega_param / omega_yield)


@jax.jit
def _reparam_V(V_param: jnp.ndarray, V_max: float) -> jnp.ndarray:
    """V_actual = V_max · tanh(V_param / V_max). |V| < V_max by construction."""
    return V_max * jnp.tanh(V_param / V_max)


def _inverse_reparam(actual: np.ndarray, scale: float, eps: float = 1e-3) -> np.ndarray:
    """Convert engine-space amplitude to param-space (clipped to avoid arctanh(±1)=∞)."""
    safe = np.clip(actual / scale, -(1.0 - eps), 1.0 - eps)
    return scale * np.arctanh(safe)


@jax.jit
def _s11_coupled_reparam_objective(
    u: jnp.ndarray, omega_p: jnp.ndarray, V_p: jnp.ndarray,
    mask_alive: jnp.ndarray, dx: float,
    omega_yield: float, epsilon_yield: float, V_SNAP: float,
) -> jnp.ndarray:
    """|S₁₁|² coupled with ω, V tanh-reparameterized; u unconstrained."""
    omega = _reparam_omega(omega_p, omega_yield)
    V_inc = _reparam_V(V_p, V_SNAP)
    rho = _s11_density_coupled(u, omega, V_inc, dx, omega_yield, epsilon_yield, V_SNAP)
    return jnp.sum(rho * mask_alive.astype(rho.dtype))


@jax.jit
def _cosserat_energy_reparam_objective(
    u: jnp.ndarray, omega_p: jnp.ndarray,
    mask_alive: jnp.ndarray, dx: float,
    G: float, G_c: float, gamma: float,
    omega_yield: float, epsilon_yield: float,
    k_op10: float, k_refl: float, k_hopf: float,
) -> jnp.ndarray:
    """Cosserat energy with ω tanh-reparameterized; u unconstrained."""
    omega = _reparam_omega(omega_p, omega_yield)
    return _total_energy_saturated(
        u, omega, mask_alive, dx, G, G_c, gamma,
        omega_yield, epsilon_yield, k_op10, k_refl, k_hopf,
    )


_val_and_grad_s11_reparam = jax.jit(
    jax.value_and_grad(_s11_coupled_reparam_objective, argnums=(0, 1, 2))
)
_val_and_grad_energy_reparam = jax.jit(
    jax.value_and_grad(_cosserat_energy_reparam_objective, argnums=(0, 1))
)


def _gather_reparam_state(engine: VacuumEngine3D) -> tuple:
    """Convert engine state (u, ω, V_inc) → (u_arr, ω_param, V_param)."""
    u = np.asarray(engine.cos.u).copy()
    omega = np.asarray(engine.cos.omega).copy()
    V_inc = np.asarray(engine.k4.V_inc).copy()
    omega_param = _inverse_reparam(omega, float(engine.cos.omega_yield))
    V_param = _inverse_reparam(V_inc, float(engine.V_SNAP))
    return u, omega_param, V_param


def _scatter_reparam_state(
    engine: VacuumEngine3D, u: np.ndarray, omega_param: np.ndarray, V_param: np.ndarray,
) -> None:
    """Push (u_arr, ω_param, V_param) back to engine state via tanh forward."""
    engine.cos.u = u
    omega_actual = float(engine.cos.omega_yield) * np.tanh(omega_param / float(engine.cos.omega_yield))
    V_actual = float(engine.V_SNAP) * np.tanh(V_param / float(engine.V_SNAP))
    engine.cos.omega = omega_actual
    engine.k4.V_inc = V_actual
    engine.cos._zero_outside_alive()
    engine.k4.V_inc = np.where(engine.k4.mask_active[..., None], engine.k4.V_inc, 0.0)


def relax_with_reparam(
    engine: VacuumEngine3D,
    objective: str = "s11",
    max_iter: int = 500,
    tol: float = 1e-9,
    initial_lr: float = 1e-3,
    verbose: bool = False,
    track_every: int = 25,
) -> dict:
    """Phase 5c-v2 descent on (u, ω_param, V_param) with tanh reparameterization.

    objective ∈ {"s11", "energy"}:
      "s11"    — minimize total_s11_coupled (per doc 34_ X4b precedent)
      "energy" — minimize Cosserat saturated energy (per doc 03_ §1)

    Both bound ω and V via tanh reparameterization (eliminates v1 over-saturation).
    No Lagrange penalties; topology preserved by ansatz, geometry emerges naturally.
    """
    u, omega_p, V_p = _gather_reparam_state(engine)

    cos_mask = engine.cos._mask_alive_jax
    k4_mask = jnp.asarray(engine.k4.mask_active)

    omega_yield = float(engine.cos.omega_yield)
    epsilon_yield = float(engine.cos.epsilon_yield)
    V_SNAP = float(engine.V_SNAP)
    dx = engine.cos.dx

    def _eval(u_, omp_, vp_) -> float:
        if objective == "s11":
            return float(_s11_coupled_reparam_objective(
                jnp.asarray(u_), jnp.asarray(omp_), jnp.asarray(vp_),
                cos_mask, dx, omega_yield, epsilon_yield, V_SNAP,
            ))
        else:
            return float(_cosserat_energy_reparam_objective(
                jnp.asarray(u_), jnp.asarray(omp_),
                cos_mask, dx, engine.cos.G, engine.cos.G_c, engine.cos.gamma,
                omega_yield, epsilon_yield,
                engine.cos.k_op10, engine.cos.k_refl, engine.cos.k_hopf,
            ))

    def _grad(u_, omp_, vp_) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        if objective == "s11":
            _, (gu, gom, gv) = _val_and_grad_s11_reparam(
                jnp.asarray(u_), jnp.asarray(omp_), jnp.asarray(vp_),
                cos_mask, dx, omega_yield, epsilon_yield, V_SNAP,
            )
            cos_m = cos_mask[..., None].astype(gu.dtype)
            k4_m = k4_mask[..., None].astype(gv.dtype)
            return np.asarray(gu * cos_m), np.asarray(gom * cos_m), np.asarray(gv * k4_m)
        else:
            _, (gu, gom) = _val_and_grad_energy_reparam(
                jnp.asarray(u_), jnp.asarray(omp_),
                cos_mask, dx, engine.cos.G, engine.cos.G_c, engine.cos.gamma,
                omega_yield, epsilon_yield,
                engine.cos.k_op10, engine.cos.k_refl, engine.cos.k_hopf,
            )
            cos_m = cos_mask[..., None].astype(gu.dtype)
            return np.asarray(gu * cos_m), np.asarray(gom * cos_m), np.zeros_like(vp_)

    lr = initial_lr
    history = []
    trajectory = []

    obj_prev = _eval(u, omega_p, V_p)
    history.append(obj_prev)
    noise_floor = 1e-12 * max(abs(obj_prev), 1.0)

    def _snapshot(step: int, obj: float, lr_now: float) -> dict:
        _scatter_reparam_state(engine, u, omega_p, V_p)
        c_cos = int(engine.cos.extract_crossing_count())
        peak_omega = float(np.max(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1)))
        peak_V = float(np.max(np.abs(np.asarray(engine.k4.V_inc))))
        E_cos = float(engine.cos.total_energy())
        E_k4 = float(np.sum(np.asarray(engine.k4.V_inc) ** 2))
        return {
            "step": step, "obj": obj, "c_cos": c_cos,
            "peak_omega": peak_omega, "peak_V": peak_V,
            "E_cos": E_cos, "E_k4": E_k4, "lr": lr_now,
        }

    if track_every > 0:
        snap = _snapshot(0, obj_prev, lr)
        trajectory.append(snap)
        if verbose:
            print(f"  [{objective}] step {0:5d}  obj={snap['obj']:.6e}  "
                  f"c={snap['c_cos']}  |ω|={snap['peak_omega']:.3f}  "
                  f"|V|={snap['peak_V']:.4f}  lr={snap['lr']:.2e}")

    for step in range(max_iter):
        u_save = u.copy()
        omp_save = omega_p.copy()
        vp_save = V_p.copy()

        gu, gom, gv = _grad(u, omega_p, V_p)
        u = u - lr * gu
        omega_p = omega_p - lr * gom
        if objective == "s11":
            V_p = V_p - lr * gv

        obj_new = _eval(u, omega_p, V_p)

        if obj_new <= obj_prev + noise_floor:
            rel_change = abs(obj_new - obj_prev) / max(abs(obj_prev), 1e-12)
            history.append(obj_new)

            if track_every > 0 and ((step + 1) % track_every == 0):
                snap = _snapshot(step + 1, obj_new, lr)
                trajectory.append(snap)
                if verbose:
                    print(f"  [{objective}] step {step+1:5d}  obj={snap['obj']:.6e}  "
                          f"c={snap['c_cos']}  |ω|={snap['peak_omega']:.3f}  "
                          f"|V|={snap['peak_V']:.4f}  lr={snap['lr']:.2e}")

            if step > 10 and rel_change < tol:
                _scatter_reparam_state(engine, u, omega_p, V_p)
                return {
                    "iterations": step + 1, "final_obj": obj_new,
                    "converged": True, "history": history,
                    "trajectory": trajectory, "lr_final": lr,
                    "objective": objective,
                }
            lr = min(lr * 1.1, 1.0)
            obj_prev = obj_new
            noise_floor = 1e-12 * max(abs(obj_prev), 1.0)
        else:
            u = u_save
            omega_p = omp_save
            V_p = vp_save
            lr *= 0.5
            if lr < 1e-14:
                _scatter_reparam_state(engine, u, omega_p, V_p)
                return {
                    "iterations": step + 1, "final_obj": obj_prev,
                    "converged": False, "history": history,
                    "trajectory": trajectory, "lr_final": lr,
                    "objective": objective, "note": "lr collapsed",
                }

    _scatter_reparam_state(engine, u, omega_p, V_p)
    return {
        "iterations": max_iter, "final_obj": obj_prev,
        "converged": False, "history": history,
        "trajectory": trajectory, "lr_final": lr,
        "objective": objective,
    }


def run_phase5c_v2_dual_descent(
    N: int = 80, R: float = 20.0,
    V_amp: float = 0.05, chirality: float = 1.0,
    max_iter: int = 500, initial_lr: float = 1e-3,
) -> dict:
    """Phase 5c-v2 — dual descent (Cosserat-energy + S₁₁) from same seed.

    Per doc 67_ §23.3: corpus claim is they co-locate at Golden Torus. This
    driver runs both from the same phase-quadrature seed and compares
    convergent (R, r, c, |ω|, |V|, E_cos, E_k4). Result is a
    corpus-duality test irrespective of which converges where.
    """
    PHI_SQ = ((1 + np.sqrt(5)) / 2) ** 2
    r = R / PHI_SQ
    cos_amp = 0.3 / (np.sqrt(3.0) / 2.0)

    print("=" * 78)
    print(f"  F17-K Phase 5c-v2: dual descent at N={N}")
    print(f"  Cosserat-energy AND |S₁₁|² from same seed (doc 67_ §23 corpus-duality)")
    print("=" * 78)
    print(f"  Seed: phase-quadrature K4 (V_amp={V_amp}, chirality={chirality}) + Cos ω")
    print(f"  R={R}, r={r:.4f}, max_iter={max_iter}, initial_lr={initial_lr}")
    print(f"  ω, V tanh-reparameterized → bounded |ω|<ω_yield, |V|<V_SNAP")
    print()

    from tlm_electron_soliton_eigenmode import initialize_quadrature_2_3_eigenmode

    def build_engine() -> VacuumEngine3D:
        eng = VacuumEngine3D.from_args(
            N=N, pml=4, temperature=0.0,
            disable_cosserat_lc_force=True,
            enable_cosserat_self_terms=True,
        )
        initialize_quadrature_2_3_eigenmode(
            eng.k4, R=R, r=r, amplitude=V_amp, chirality=chirality,
        )
        eng.cos.initialize_electron_2_3_sector(
            R_target=R, r_target=r, use_hedgehog=True, amplitude_scale=cos_amp,
        )
        return eng

    import time
    results = {}
    for objective in ["energy", "s11"]:
        print(f"\n  --- Run: objective={objective!r} ---")
        engine = build_engine()
        t0 = time.time()
        result = relax_with_reparam(
            engine, objective=objective,
            max_iter=max_iter, tol=1e-9,
            initial_lr=initial_lr, verbose=True, track_every=50,
        )
        elapsed = time.time() - t0
        # Final state diagnostics
        c_cos = int(engine.cos.extract_crossing_count())
        peak_omega = float(np.max(np.linalg.norm(engine.cos.omega, axis=-1)))
        peak_V = float(np.max(np.abs(engine.k4.V_inc)))
        E_cos = float(engine.cos.total_energy())
        E_k4 = float(np.sum(engine.k4.V_inc ** 2))
        R_found, r_found = engine.cos.extract_shell_radii()
        results[objective] = {
            **result,
            "elapsed": elapsed,
            "final_c": c_cos, "final_peak_omega": peak_omega,
            "final_peak_V": peak_V, "final_E_cos": E_cos, "final_E_k4": E_k4,
            "final_R": float(R_found), "final_r": float(r_found),
        }
        print(f"\n  --- {objective!r} final ---")
        print(f"  iters: {result['iterations']}/{max_iter}  converged={result['converged']}")
        print(f"  obj:   {result['final_obj']:.4e}")
        print(f"  c_cos: {c_cos}, peak|ω|={peak_omega:.4f}, peak|V|={peak_V:.4f}")
        print(f"  R/r:   ({R_found:.3f}, {r_found:.3f})  →  {R_found/max(r_found,1e-9):.3f}")
        print(f"  E_cos: {E_cos:.3e}, E_k4: {E_k4:.3e}")
        print(f"  elapsed: {elapsed:.1f}s")

    print(f"\n{'=' * 78}")
    print(f"  CORPUS-DUALITY COMPARISON")
    print(f"{'=' * 78}")
    print(f"  {'metric':<14}{'energy':<14}{'s11':<14}{'Δ':<14}")
    for k in ["final_c", "final_peak_omega", "final_peak_V", "final_R", "final_r", "final_E_cos", "final_E_k4"]:
        e = results["energy"][k]
        s = results["s11"][k]
        try:
            delta = float(s) - float(e)
            print(f"  {k:<14}{float(e):<14.4f}{float(s):<14.4f}{delta:<+14.4f}")
        except (TypeError, ValueError):
            print(f"  {k:<14}{e!s:<14}{s!s:<14}n/a")

    return results


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "v2":
    run_phase5c_v2_dual_descent(N=80, max_iter=500)
