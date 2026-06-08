"""Theorem 3.1′ per-cycle radiation leak on a localized lattice shell.

Applies fraction α of stored energy per Compton cycle (1/Q = α) by scaling
phasor and Cosserat fields on a shell — forward test of the TUNE channel.
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

import numpy as np

from ave.core.constants import ALPHA_COLD, Z_RADIATION, Z_0

if TYPE_CHECKING:
    from ave.topological.vacuum_engine import VacuumEngine3D


def shell_mask(
    shape: tuple[int, int, int],
    center: tuple[int, int, int],
    radius: int,
    active: np.ndarray,
) -> np.ndarray:
    cx, cy, cz = center
    i, j, k = np.indices(shape)
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    return (r <= radius) & active


def leak_per_step(
    dt_outer: float,
    omega_yield: float,
    *,
    leak_fraction_per_cycle: float = float(ALPHA_COLD),
) -> float:
    """Discrete per-step leak fraction for target leak per Compton cycle."""
    if omega_yield <= 0 or dt_outer <= 0:
        return 0.0
    steps_per_cycle = (2.0 * math.pi / omega_yield) / dt_outer
    if steps_per_cycle <= 0:
        return 0.0
    return 1.0 - (1.0 - leak_fraction_per_cycle) ** (1.0 / steps_per_cycle)


def apply_radiation_leak_shell(
    engine: VacuumEngine3D,
    center: tuple[int, int, int],
    shell_radius: int,
    *,
    leak_fraction_per_cycle: float = float(ALPHA_COLD),
) -> dict[str, float]:
    """Drain shell energy at Theorem 3.1′ rate (α per Compton cycle).

    Returns diagnostics; does not alter engine dynamics elsewhere.
    """
    dt = float(engine._coupled.outer_dt)
    omega_y = float(engine.cos.omega_yield)
    lps = leak_per_step(dt, omega_y, leak_fraction_per_cycle=leak_fraction_per_cycle)
    scale = math.sqrt(max(1.0 - lps, 0.0))

    mask3 = shell_mask(
        engine.k4.V_inc.shape[:3],
        center,
        shell_radius,
        engine.k4.mask_active,
    )

    e_before = float(
        np.sum(engine.k4.V_inc[mask3] ** 2 + engine.k4.V_ref[mask3] ** 2)
    )

    engine.k4.V_inc[mask3] *= scale
    engine.k4.V_ref[mask3] *= scale

    cos_mask = mask3 & engine.cos.mask_alive
    engine.cos.omega[cos_mask] *= scale
    engine.cos.u[cos_mask] *= scale

    e_after = float(
        np.sum(engine.k4.V_inc[mask3] ** 2 + engine.k4.V_ref[mask3] ** 2)
    )
    fractional = 1.0 - (e_after / e_before) if e_before > 1e-30 else 0.0

    return {
        "leak_per_step": lps,
        "leak_fraction_per_cycle_target": leak_fraction_per_cycle,
        "steps_per_compton_cycle": (2.0 * math.pi / omega_y) / dt if omega_y > 0 else None,
        "shell_fractional_energy_loss": fractional,
        "scale_applied": scale,
        "Z_radiation_SI": float(Z_RADIATION),
        "Z_radiation_over_Z0": float(Z_RADIATION / Z_0),
    }
