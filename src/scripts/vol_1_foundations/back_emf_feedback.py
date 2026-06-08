"""Dark-wake back-EMF feedback into Cosserat translational sector (driver-side).

Implements τ_zx ∝ z_local · ∂(A²)/∂x as a reactive back-reaction on u,
closing the read-only DarkWakeObserver gap for genesis experiments.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from ave.topological.cosserat_field_3d import tetrahedral_gradient

if TYPE_CHECKING:
    from ave.topological.vacuum_engine import VacuumEngine3D


def apply_dark_wake_back_emf(
    engine: VacuumEngine3D,
    *,
    propagation_axis: int = 0,
    gain: float = 0.15,
) -> dict[str, float]:
    """Apply τ_zx back-reaction as opposing impulse on Cosserat u."""
    v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
    a_sq = v_sq / (engine.V_SNAP**2)
    grad_a = tetrahedral_gradient(a_sq) / engine.k4.dx
    z_local = np.asarray(engine.k4.z_local_field)
    tau = z_local * grad_a[..., propagation_axis]

    dt = float(engine._coupled.outer_dt)
    alive = engine.cos.mask_alive
    u = np.asarray(engine.cos.u)
    u_before = float(np.linalg.norm(u[alive])) if np.any(alive) else 0.0

    impulse_axis = gain * tau * dt
    u[alive, propagation_axis] -= impulse_axis[alive]
    engine.cos.u = u

    u_after = float(np.linalg.norm(u[alive])) if np.any(alive) else 0.0
    tau_peak = float(np.abs(tau[alive]).max()) if np.any(alive) else 0.0

    return {
        "gain": gain,
        "propagation_axis": propagation_axis,
        "max_tau_zx": tau_peak,
        "u_norm_before": u_before,
        "u_norm_after": u_after,
        "dt": dt,
    }
