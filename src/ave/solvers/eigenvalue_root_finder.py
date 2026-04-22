"""
Eigenvalue Root-Finder
======================

Universal Newton-Raphson root-finder for eigenvalue ground states.

The fundamental problem solved:
    Find θ such that f(θ) = λ_min(S†S(θ)) · G(θ) = 0

where λ_min is the smallest eigenvalue of the Hermitian matrix S†S,
and G(θ) is an optional auxiliary penalty (sterics, saturation, etc.).

When f = 0, a mode of the S-matrix is perfectly matched to the
environment — the system has found an eigenstate.

Newton-Raphson step:
    Δθ = -f(θ) · ∇f / |∇f|²

Used at every scale:
    - Nuclear: K_MUTUAL eigenvalue → binding energy
    - Protein: λ_min(S†S) → native fold
    - Antenna: S₁₁ → impedance match

This module contains ZERO domain-specific physics.
"""

from __future__ import annotations


import numpy as np

from ave.core.constants import EPS_NUMERICAL


def newton_step(f_val, gradient, trust_radius=np.pi):
    """
    Single Newton-Raphson step for eigenvalue root-finding.

    Δθ = -f · g / |g|²

    Args:
        f_val:        Scalar function value (the root target)
        gradient:     Gradient vector ∇f (same shape as θ)
        trust_radius: Maximum step magnitude per component (default: π)

    Returns:
        delta_theta: The Newton update vector
    """
    g = np.where(np.isnan(gradient), 0.0, gradient)
    g_norm_sq = np.sum(g**2) + EPS_NUMERICAL
    direction = -f_val * g / g_norm_sq

    # Trust region: cap total step at trust_radius
    dir_norm = np.sqrt(np.sum(direction**2) + EPS_NUMERICAL)
    if dir_norm > trust_radius:
        direction = direction * trust_radius / dir_norm

    return direction


def find_eigenstate(theta_init, f_fn, grad_fn, n_iter=200, trust_radius=np.pi, converge_threshold=None, Q=None):
    """
    Newton-Raphson root-finder with backtracking line search.

    Args:
        theta_init:         Initial parameter vector
        f_fn:               Callable θ → scalar f(θ) (the root target)
        grad_fn:            Callable θ → ∇f(θ) (gradient)
        n_iter:             Maximum iterations
        trust_radius:       Per-step angular bound (default: π)
        converge_threshold: Stop when |f| < threshold (default: 1/Q²)
        Q:                  Quality factor (used to set threshold if not given)

    Returns:
        theta_final: Converged parameter vector
        f_final:     Final function value
        converged:   Boolean indicating convergence
        history:     List of f values per iteration
    """
    if converge_threshold is None and Q is not None:
        converge_threshold = 1.0 / (Q**2)
    elif converge_threshold is None:
        converge_threshold = 1e-4

    theta = np.array(theta_init, dtype=float)
    history = []

    for i in range(n_iter):
        f_val = float(f_fn(theta))
        history.append(f_val)

        if abs(f_val) < converge_threshold:
            return theta, f_val, True, history

        g = grad_fn(theta)
        delta = newton_step(f_val, g, trust_radius)

        # Backtracking line search: halve step until f decreases
        alpha = 1.0
        f_trial = float(f_fn(theta + alpha * delta))
        for _ in range(25):
            if f_trial < f_val:
                break
            alpha *= 0.5
            f_trial = float(f_fn(theta + alpha * delta))

        theta = theta + alpha * delta

    f_final = float(f_fn(theta))
    history.append(f_final)
    return theta, f_final, abs(f_final) < converge_threshold, history


# ── JAX backend (optional, for JIT-compiled loops) ──────────────

try:
    import jax
    import jax.numpy as jnp
    from jax import lax

    def newton_step_jax(f_val, gradient, trust_radius=jnp.pi):
        """JAX-traceable single Newton step."""
        g = jnp.where(jnp.isnan(gradient), 0.0, gradient)
        g_norm_sq = jnp.sum(g**2) + EPS_NUMERICAL
        direction = -f_val * g / g_norm_sq

        dir_norm = jnp.sqrt(jnp.sum(direction**2) + EPS_NUMERICAL)
        scale = jnp.where(dir_norm > trust_radius, trust_radius / dir_norm, 1.0)
        return direction * scale

    def find_eigenstate_jax(theta_init, f_fn, n_iter=200, trust_radius=jnp.pi):
        """
        JIT-compiled Newton-Raphson with backtracking line search.

        Args:
            theta_init: Initial JAX array
            f_fn:       JAX-traceable scalar function θ → f(θ)
            n_iter:     Maximum iterations
            trust_radius: Angular trust region bound

        Returns:
            theta_final: Converged parameter vector
        """
        grad_fn = jax.grad(f_fn)

        def step_fn(i, theta):
            f_val = f_fn(theta)
            g = grad_fn(theta)
            g = jnp.where(jnp.isnan(g), 0.0, g)

            direction = newton_step_jax(f_val, g, trust_radius)

            # Backtracking line search
            f_full = f_fn(theta + direction)

            def ls_cond(state):
                alpha, f_trial, count = state
                return (f_trial >= f_val) & (count < 25)

            def ls_body(state):
                alpha, _, count = state
                new_alpha = alpha * 0.5
                trial = theta + new_alpha * direction
                new_f = f_fn(trial)
                return (new_alpha, new_f, count + 1)

            alpha_final, _, _ = lax.while_loop(ls_cond, ls_body, (jnp.float64(1.0), f_full, jnp.int32(0)))

            return theta + alpha_final * direction

        return lax.fori_loop(0, n_iter, step_fn, theta_init)

    HAS_JAX = True

except ImportError:
    HAS_JAX = False
