"""
SPICE Transient Integrator — Canonical Explicit Euler Step
=========================================================

Universal explicit Euler integrator for lumped L-C-R networks.
This is the Tier 3 solver implementing Newton's 2nd law as a
circuit equation:

    v(t + Δt) = v(t) + [ -∇f(θ) - R·v(t) ] / L  ·  Δt     (Newton's 2nd)
    θ(t + Δt) = θ(t) + v(t + Δt) · Δt                       (Euler forward)

where:
    L = inertial mass (inductance analogue)
    R = dissipative friction (resistance analogue)
    ∇f = gradient of the potential (eigenvalue target, S₁₁, etc.)

Canonical API:
    explicit_euler_step()     — single step, domain-agnostic
    explicit_euler_step_jax() — JAX-traceable variant

Deprecated (zero external callers):
    integrate_transient()     — use explicit_euler_step() in a loop
    integrate_transient_jax() — use explicit_euler_step_jax() with lax.fori_loop

Known inline copies:
    s11_fold_engine_v4_ymatrix.py fold_cascade_transient_v7() (L1274)
        — identical physics: acceleration = (-g - R_damp * vel_c) / L_mass
        — inline because it runs inside @jit lax.fori_loop closure
          with captured seg_mask/junc_mask; cannot call external functions
        — see KB entry: spice-transient-equations-v5.md

Used at:
    - Protein scale: torsion-angle ring-down into native fold
    - Nuclear scale: bond geometry relaxation
    - Antenna scale: current distribution equilibration
    - Hardware scale: APU transient verification (test_ato_compiler.py)

All constants are set by the caller — this module contains ZERO
domain-specific physics.

Reference: Backmatter App 5 (Universal Solver Toolchain)
           Backmatter App 6 (SPICE Verification Manual)
"""

from __future__ import annotations




def explicit_euler_step(theta, velocity, grad_f, L, R, dt, mask=None):
    """
    Single explicit Euler step for SPICE transient integration.

    Args:
        theta:    Current state vector (angles, positions, etc.)
        velocity: Current velocity vector
        grad_f:   Gradient of the target function at theta
        L:        Inertial mass per DOF (scalar or array)
        R:        Damping resistance per DOF (scalar or array)
        dt:       Timestep (physical, not a learning rate)
        mask:     Optional binary mask (1 = active, 0 = frozen DOF)

    Returns:
        new_theta, new_velocity: Updated state and velocity vectors
    """
    g = grad_f
    if mask is not None:
        g = g * mask

    # Physical SPICE Euler: a = (-∇V - R·v) / L
    acceleration = (-g - R * velocity) / L
    new_velocity = velocity + acceleration * dt
    new_theta = theta + new_velocity * dt

    return new_theta, new_velocity


# ── JAX backend (optional, for JIT-compiled loops) ──────────────

try:
    pass

    def explicit_euler_step_jax(theta, velocity, grad_f, L, R, dt, mask=None):
        """JAX-traceable single Euler step."""
        g = grad_f
        if mask is not None:
            g = g * mask
        acceleration = (-g - R * velocity) / L
        new_velocity = velocity + acceleration * dt
        new_theta = theta + new_velocity * dt
        return new_theta, new_velocity

    HAS_JAX = True

except ImportError:
    HAS_JAX = False
