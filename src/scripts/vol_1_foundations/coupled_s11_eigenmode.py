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
