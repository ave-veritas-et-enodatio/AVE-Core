"""
Macroscopic impedance calculations, replacing older Navier-Stokes mechanical rheology.
Calculates localized refractive index and mutual inductance transitions.

The mutual inductance saturation uses the SAME ``saturation_factor()`` that
governs particle confinement, FDTD field updates, and plasma cutoff:
when rotational shear exceeds the lattice saturation threshold, the
drag vanishes smoothly — not as a step function.
"""

from __future__ import annotations


import numpy as np
from ave.core.constants import G, C_0, ISOTROPIC_PROJECTION
from ave.axioms.scale_invariant import saturation_factor

# Re-export from gravity module (single source of truth)
from ave.gravity import refractive_index as calculate_refractive_strain  # noqa: F401
from ave.gravity import is_dielectric_rupture  # noqa: F401

# NOTE: calculate_refractive_strain and is_dielectric_rupture are
# re-exported from ave.gravity above. No local implementation needed.


def get_mutual_inductance(shear_rate: float, background_inductance: float, saturation_threshold: float) -> float:
    """
    Effective macroscopic mutual inductance under rotational shear.

    Uses the universal Axiom 4 saturation operator — the SAME function
    that confines particles, drives FDTD, and causes plasma cutoff:

        η_eff = η₀ · √(1 − (γ̇/γ̇_yield)²)

    When shear is LOW (outer galaxy): η_eff ≈ η₀ → full drag
        → the unbroken LC lattice drags on orbiting mass
        → manifests as "dark matter"

    When shear is HIGH (inner galaxy): η_eff → 0 → no drag
        → saturated lattice cannot support transverse inductive coupling
        → conservative Keplerian orbits

    The transition is smooth, governed by the same √(1−r²) kernel that
    operates at every other scale in the framework.

    Args:
        shear_rate: Local rate of topological shear (from orbital velocity gradients).
        background_inductance: Base undisturbed inductance of deep space.
        saturation_threshold: Critical shear threshold for LC loop saturation.

    Returns:
        Effective macroscopic mutual inductance at that specific shear rate.
    """
    S = float(saturation_factor(shear_rate, saturation_threshold))
    return background_inductance * S
