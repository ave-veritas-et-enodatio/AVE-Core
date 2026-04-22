from __future__ import annotations

"""
Axiom 4: Dielectric Saturation
================================
The vacuum acts as a non-linear dielectric bounded by the fine-structure
limit α. The effective capacitance diverges as local strain approaches
saturation, while effective permittivity collapses — trapping energy into
topological knots (mass).

The saturation operator is strictly squared (n=2) to align with:
  - The E⁴ energy density of the Euler-Heisenberg QED Lagrangian
  - The χ⁽³⁾ displacement of the optical Kerr effect
  - Standard Born-Infeld non-linear electrodynamics

All core saturation operations are implemented in
``ave.axioms.scale_invariant`` — the SAME functions serve every scale.
This module re-exports them with Axiom-4-specific defaults and adds
the capacitance and energy-density formulas unique to this domain.

Key functions:
  epsilon_eff(V, V_yield)  — Non-linear permittivity
  capacitance_eff(dphi, alpha) — Non-linear capacitance
  reflection_coefficient(Z_knot, Z_vac) — Transmission line Γ
  local_wave_speed(V, V_yield) — c_eff under saturation
  energy_density_nonlinear(dphi, alpha, eps0) — Full non-linear U
  impedance_at_strain(V, V_yield) — Z_eff under saturation
"""

import numpy as np
from ave.core.constants import EPSILON_0, C_0, ALPHA, V_YIELD, Z_0

# ═══════════════════════════════════════════════════════════════
# Re-exports from scale_invariant.py (single source of truth)
# ═══════════════════════════════════════════════════════════════
#
# These are thin re-exports with Axiom-4-specific defaults baked in.
# The canonical implementations live in scale_invariant.py.
# Import from either location — they are the same function.


# Import the scale-invariant canonical implementations for wrapping
from ave.axioms.scale_invariant import (
    epsilon_eff as _si_epsilon_eff,
    reflection_coefficient as _si_reflection_coefficient,
    local_wave_speed as _si_local_wave_speed,
    impedance_at_strain as _si_impedance_at_strain,
)


# ═══════════════════════════════════════════════════════════════
# Thin wrappers with Axiom-4 defaults
# ═══════════════════════════════════════════════════════════════


def epsilon_eff(V, V_yield: float = V_YIELD):
    """
    Non-linear effective permittivity: ε_eff(V) = ε₀ · √(1 − (V/V_yield)²)

    Delegates to ``scale_invariant.epsilon_eff``.
    Raises ValueError if |V| > V_yield (physical rupture).
    """
    return _si_epsilon_eff(V, V_yield, EPSILON_0, clip=False)


def reflection_coefficient(Z_knot: float, Z_vac: float = Z_0) -> float:
    """
    Γ = (Z_knot − Z_vac) / (Z_knot + Z_vac)

    Delegates to ``scale_invariant.reflection_coefficient``.
    """
    return float(_si_reflection_coefficient(Z_vac, Z_knot))


def local_wave_speed(
    V: np.ndarray | float,
    V_yield: float = V_YIELD,
) -> np.ndarray | float:
    """
    c_eff(V) = c₀ · (1 − (V/V_yield)²)^(1/4)

    Delegates to ``scale_invariant.local_wave_speed``.
    """
    return _si_local_wave_speed(V, V_yield, C_0, clip=True)


def impedance_at_strain(V: np.ndarray, V_yield: float = V_YIELD) -> np.ndarray:
    """
    Z_eff(V) = Z₀ / (1 − (V/V_yield)²)^(1/4)

    Delegates to ``scale_invariant.impedance_at_strain``.
    """
    return _si_impedance_at_strain(V, V_yield, Z_0, clip=True)


# ═══════════════════════════════════════════════════════════════
# Unique domain-specific functions (NOT in scale_invariant)
# ═══════════════════════════════════════════════════════════════


def capacitance_eff(
    dphi: np.ndarray | float,
    alpha: float = ALPHA,
) -> np.ndarray | float:
    """
    Non-linear effective capacitance per Axiom 4:

    C_eff(Δφ) = C₀ / √(1 − (Δφ/α)²)

    This is the INVERSE of the saturation factor: as strain increases,
    capacitance DIVERGES (the node absorbs more displacement current).
    This matches the Euler-Heisenberg QED prediction of increased
    vacuum polarizability under extreme fields.

    Args:
        dphi: Normalized phase displacement (0 ≤ |Δφ| < α).
        alpha: Fine-structure saturation limit.

    Returns:
        Effective capacitance ratio (C_eff / C₀).
    """
    ratio_sq = np.asarray(dphi, dtype=float) ** 2 / alpha**2
    if np.any(ratio_sq >= 1.0):
        raise ValueError(f"Capacitance singularity: |Δφ/α| ≥ 1.0. " f"Max ratio² = {np.max(ratio_sq):.6f}.")
    return 1.0 / np.sqrt(1.0 - ratio_sq)


def energy_density_nonlinear(
    dphi: np.ndarray | float,
    alpha: float = ALPHA,
    eps0: float = EPSILON_0,
) -> np.ndarray | float:
    """
    Full non-linear energy density including the E⁴ correction term:

    U ≈ ½ε₀(Δφ)² + (3/8α²)ε₀(Δφ)⁴

    The first term is standard Maxwell. The second is the Euler-Heisenberg
    QED correction from Axiom 4's squared saturation operator.

    Args:
        dphi: Phase displacement (dimensionless or field amplitude).
        alpha: Fine-structure saturation limit.
        eps0: Baseline permittivity.

    Returns:
        Energy density [J/m³ equivalent units].
    """
    dphi = np.asarray(dphi, dtype=float)
    linear_term = 0.5 * eps0 * dphi**2
    nonlinear_correction = (3.0 / (8.0 * alpha**2)) * eps0 * dphi**4
    return linear_term + nonlinear_correction
