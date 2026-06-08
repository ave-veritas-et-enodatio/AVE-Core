"""Reactance-boundary radiation leak — drain reflected flux only (TUNE v2).

WS2 naive shell drain scaled V_inc+V_ref and destroyed TIR. This channel
drains only the **outward/reflected** bond component (V_ref) on the trap
shell at Theorem 3.1′ α/cycle — forward, α as corpus target rate only.
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

import numpy as np

from ave.core.constants import ALPHA_COLD, Z_RADIATION, Z_0

from radiation_leak_shell import leak_per_step, shell_mask

if TYPE_CHECKING:
    from ave.topological.vacuum_engine import VacuumEngine3D


def apply_radiation_leak_boundary(
    engine: VacuumEngine3D,
    center: tuple[int, int, int],
    shell_radius: int,
    *,
    leak_fraction_per_cycle: float = float(ALPHA_COLD),
    leak_omega_fraction: float = 0.25,
) -> dict[str, float]:
    """Leak radiative V_ref (and partial ω) on shell — preserve V_inc trap."""
    dt = float(engine._coupled.outer_dt)
    omega_y = float(engine.cos.omega_yield)
    lps = leak_per_step(dt, omega_y, leak_fraction_per_cycle=leak_fraction_per_cycle)
    scale = math.sqrt(max(1.0 - lps, 0.0))
    omega_scale = math.sqrt(max(1.0 - leak_omega_fraction * lps, 0.0))

    mask3 = shell_mask(
        engine.k4.V_inc.shape[:3],
        center,
        shell_radius,
        engine.k4.mask_active,
    )

    e_ref_before = float(np.sum(engine.k4.V_ref[mask3] ** 2))
    engine.k4.V_ref[mask3] *= scale
    e_ref_after = float(np.sum(engine.k4.V_ref[mask3] ** 2))

    cos_mask = mask3 & engine.cos.mask_alive
    omega_before = float(np.sum(engine.cos.omega[cos_mask] ** 2))
    engine.cos.omega[cos_mask] *= omega_scale
    omega_after = float(np.sum(engine.cos.omega[cos_mask] ** 2))

    return {
        "leak_per_step": lps,
        "leak_fraction_per_cycle_target": leak_fraction_per_cycle,
        "v_ref_scale": scale,
        "omega_scale": omega_scale,
        "v_ref_fractional_loss": 1.0 - (e_ref_after / e_ref_before) if e_ref_before > 1e-30 else 0.0,
        "omega_fractional_loss": 1.0 - (omega_after / omega_before) if omega_before > 1e-30 else 0.0,
        "Z_radiation_SI": float(Z_RADIATION),
        "Z_radiation_over_Z0": float(Z_RADIATION / Z_0),
        "channel": "V_ref_only_boundary",
    }
