"""Stabilized back-EMF feedback and local avalanche damping for Cosserat fields.

Implements self-limiting gain on the τ_zx back-reaction and local viscosity
scaling with the avalanche multiplier M = 1 / (1 - (V/V_snap)^n) to prevent
unbound energy growth while retaining topological confinement.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from ave.topological.cosserat_field_3d import tetrahedral_gradient

if TYPE_CHECKING:
    from ave.topological.vacuum_engine import VacuumEngine3D


def apply_dark_wake_back_emf_v3(
    engine: VacuumEngine3D,
    *,
    propagation_axis: int = 0,
    gain: float = 0.12,
    damping_rate: float = 0.0,
    n: float = 1.8095,  # AVALANCHE_N_3D ≈ 1.8095
) -> dict[str, float]:
    """Apply stabilized τ_zx back-reaction and local avalanche damping."""
    v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
    v_norm = np.clip(np.sqrt(v_sq) / engine.V_SNAP, 0.0, 1.0)
    
    # 1. Self-limiting gain factor: 1/M = (1 - (V/V_snap)^n)
    # At V -> V_SNAP, gain drops to 0.
    limiting_factor = 1.0 - v_norm ** n
    
    # 2. Local avalanche multiplier M (with safe clip)
    v_norm_safe = np.clip(v_norm, 0.0, 1.0 - 1e-10)
    M = 1.0 / (1.0 - v_norm_safe ** n)
    
    # Compute the tau_zx back-reaction force
    a_sq = v_sq / (engine.V_SNAP**2)
    grad_a = tetrahedral_gradient(a_sq) / engine.k4.dx
    z_local = np.asarray(engine.k4.z_local_field)
    tau = z_local * grad_a[..., propagation_axis]

    dt = float(engine._coupled.outer_dt)
    alive = engine.cos.mask_alive
    u = np.asarray(engine.cos.u)
    u_before = float(np.linalg.norm(u[alive])) if np.any(alive) else 0.0

    # Apply self-limiting back-EMF impulse
    impulse_axis = gain * tau * dt * limiting_factor
    u[alive, propagation_axis] -= impulse_axis[alive]
    engine.cos.u = u

    # 3. Apply local avalanche viscosity (decay velocities)
    if damping_rate > 0.0:
        # Viscous decay factor: exp(-damping_rate * dt * M)
        decay = np.exp(-damping_rate * dt * M)
        
        u_dot = np.asarray(engine.cos.u_dot)
        omega_dot = np.asarray(engine.cos.omega_dot)
        
        u_dot[alive] *= decay[alive, None]
        omega_dot[alive] *= decay[alive, None]
        
        engine.cos.u_dot = u_dot
        engine.cos.omega_dot = omega_dot

    u_after = float(np.linalg.norm(u[alive])) if np.any(alive) else 0.0
    tau_peak = float(np.abs(tau[alive]).max()) if np.any(alive) else 0.0

    return {
        "gain": gain,
        "damping_rate": damping_rate,
        "n": n,
        "max_tau_zx": tau_peak,
        "u_norm_before": u_before,
        "u_norm_after": u_after,
        "dt": dt,
        "max_M": float(M[alive].max()) if np.any(alive) else 1.0,
    }
