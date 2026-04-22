"""
AVE Gravitational Wave Propagation
====================================

Gravitational waves in the AVE framework are transverse inductive
shear waves propagating through the structured LC vacuum. They are
governed by the SAME impedance, saturation, and reflection operators
used across all other scales.

Physical picture (from Ch. 19):
  - Mass = localized topological energy deficit in the LC lattice
  - Gravity = dielectric refraction: n(r) varies radially around mass
  - GW = transverse shear (μ-sector) perturbation radiating outward
  - At h ~ 10⁻²¹, the strain is 10¹⁹× below V_SNAP → no saturation
  - Therefore: perfectly linear, lossless, c-speed propagation

Key identities (SYMMETRIC GRAVITY):
  Refractive index: n(r) = 1 / (1 − r_s/r)
  ε_eff(r) = ε₀ · n(r)
  μ_eff(r) = μ₀ · n(r)
  Z(r) = √(μ_eff/ε_eff) = √(μ₀·n / ε₀·n) ≡ Z₀ (CONSTANT!)

  Symmetric Gravity enforces Z ≡ Z₀ everywhere.
  Γ = 0 everywhere — no reflection, perfect impedance matching.
  The local speed of light slows: c_local = c/n(r).
  Light bending and time dilation are REFRACTIVE effects.

  There are NO black hole echoes. The event horizon is a refractive
  singularity (n → ∞, c_local → 0), not an impedance boundary.
"""

from __future__ import annotations


import numpy as np
from typing import Optional

from ave.core.constants import (
    C_0,
    EPSILON_0,
    MU_0,
    Z_0,
    V_SNAP,
    B_SNAP,
    G,
    HBAR,
    L_NODE,
    M_SUN,
)
from ave.axioms.scale_invariant import (
    saturation_factor,
    impedance,
    reflection_coefficient,
)


# ═══════════════════════════════════════════════════════════════
# Schwarzschild refractive profile — gravity as symmetric refraction
# ═══════════════════════════════════════════════════════════════


def schwarzschild_radius(M: float) -> float:
    r"""
    Schwarzschild radius of a mass M.

    .. math::
        r_s = \frac{2 G M}{c^2}

    Args:
        M: Mass [kg].

    Returns:
        Schwarzschild radius [m].
    """
    return 2 * G * M / C_0**2


def refractive_index(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    Effective refractive index around a Schwarzschild mass.

    Symmetric Gravity requires both ε and μ to scale by the same
    factor n(r), preserving Z ≡ Z₀. The simplest mapping from
    the Schwarzschild metric gives:

    .. math::
        n(r) = \frac{1}{1 - r_s / r}

    As r → r_s: n → ∞ (light stops — refractive singularity).
    Far from mass: n → 1 (flat vacuum).

    This produces gravitational lensing identically to a graded-index
    optical medium, and time dilation via c_local = c/n.

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Refractive index (≥ 1).
    """
    from ave.core.universal_operators import universal_refractive_index
    from ave.core.constants import NU_VAC

    r = np.asarray(r, dtype=float)
    ratio = np.minimum(r_s / r, 0.9999)
    # n(r) = 1 / (1 - r_s/r)
    # n(r) = 1 + NU_VAC * eps_11
    # => eps_11 = (1 / (1 - ratio) - 1.0) / NU_VAC = (ratio / (1 - ratio)) / NU_VAC
    eps_11 = (ratio / (1.0 - ratio)) / NU_VAC
    return universal_refractive_index(eps_11, nu_vac=NU_VAC)


def epsilon_eff_schwarzschild(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    Effective permittivity in a Schwarzschild gravity well.

    Symmetric Gravity: ε and μ scale identically by n(r).

    .. math::
        \varepsilon_{eff}(r) = \varepsilon_0 \cdot n(r)

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Effective permittivity [F/m].
    """
    n = refractive_index(r, r_s)
    return EPSILON_0 * n


def mu_eff_schwarzschild(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    Effective permeability in a Schwarzschild gravity well.

    Symmetric Gravity: ε and μ scale identically by n(r).

    .. math::
        \mu_{eff}(r) = \mu_0 \cdot n(r)

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Effective permeability [H/m].
    """
    n = refractive_index(r, r_s)
    return MU_0 * n


def gravitational_impedance(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    Characteristic impedance at radius r in a Schwarzschild field.

    Under Symmetric Gravity, Z is strictly invariant:

    .. math::
        Z(r) = \sqrt{\mu_{eff} / \varepsilon_{eff}}
             = \sqrt{\mu_0 \cdot n / (\varepsilon_0 \cdot n)}
             = Z_0

    The impedance is CONSTANT everywhere. There is no impedance
    mismatch, no reflection boundary, and no black hole echoes.

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Impedance [Ω] (always Z₀).
    """
    # Impedance is strictly Z₀ under symmetric gravity.
    # We compute it explicitly to verify numerical consistency.
    mu = mu_eff_schwarzschild(r, r_s)
    eps = epsilon_eff_schwarzschild(r, r_s)
    return impedance(mu, eps)


def horizon_reflection(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    Reflection coefficient at radius r in a Schwarzschild field.

    Under Symmetric Gravity, Γ = 0 everywhere (perfect matching):

    .. math::
        \Gamma(r) = \frac{Z(r) - Z_0}{Z(r) + Z_0} = 0

    There is NO reflection at the event horizon. GW energy propagates
    inward without scattering.

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Reflection coefficient (always ~0).
    """
    Z_r = gravitational_impedance(r, r_s)
    return reflection_coefficient(Z_0, Z_r)


# ═══════════════════════════════════════════════════════════════
# GW strain and propagation properties
# ═══════════════════════════════════════════════════════════════


def gw_strain_to_voltage(h: float, freq_hz: float = 100.0) -> float:
    r"""
    Convert GW strain to equivalent voltage across one lattice cell.

    .. math::
        V_{GW} = h \cdot c \cdot \ell_{node} \cdot 2\pi f

    Args:
        h: Gravitational wave strain amplitude (dimensionless).
        freq_hz: GW frequency [Hz] (default 100 Hz for LIGO band).

    Returns:
        Equivalent voltage per lattice cell [V].
    """
    return h * C_0 * L_NODE * 2 * np.pi * freq_hz


def is_linear_propagation(h: float, freq_hz: float = 100.0) -> bool:
    r"""
    Check whether a GW propagates in the linear regime.

    Linear propagation requires V_GW << V_SNAP (no saturation).
    For LIGO-detected GW (h ~ 10⁻²¹), V_GW / V_SNAP ~ 10⁻¹⁹.

    Args:
        h: Strain amplitude.
        freq_hz: Frequency [Hz].

    Returns:
        True if propagation is linear (no saturation losses).
    """
    V_gw = gw_strain_to_voltage(h, freq_hz)
    return float(V_gw / V_SNAP) < 0.01


def gw_local_speed(r: float, r_s: float) -> float:
    r"""
    Local GW propagation speed in a Schwarzschild field.

    Under Symmetric Gravity, the local speed of light is reduced:

    .. math::
        c_{local}(r) = c_0 / n(r) = c_0 \cdot (1 - r_s/r)

    Near the horizon, c_local → 0 (light effectively stops).
    Far from mass, c_local → c₀.

    Returns:
        Local wave speed [m/s].
    """
    n = refractive_index(r, r_s)
    return float(C_0 / n)


# ═══════════════════════════════════════════════════════════════
# Summary dataclass
# ═══════════════════════════════════════════════════════════════


def gw_propagation_summary(M_solar: float = 30.0, h: float = 1e-21, r_multiples: list = None) -> dict:
    """
    Generate a summary of GW propagation properties.

    Args:
        M_solar: Source mass [solar masses].
        h: GW strain amplitude.
        r_multiples: List of r/r_s ratios to evaluate.

    Returns:
        Dict with all computed properties.
    """
    M = M_solar * M_SUN
    r_s = schwarzschild_radius(M)

    if r_multiples is None:
        r_multiples = [1.01, 1.1, 2, 5, 10, 100, 1000]

    results = {
        "M_kg": M,
        "r_s_m": r_s,
        "linear_propagation": is_linear_propagation(h),
        "V_gw_over_V_snap": gw_strain_to_voltage(h) / V_SNAP,
        "profiles": [],
    }

    for mult in r_multiples:
        r = mult * r_s
        results["profiles"].append(
            {
                "r_over_rs": mult,
                "r_m": r,
                "n_refract": float(refractive_index(r, r_s)),
                "epsilon_eff": float(epsilon_eff_schwarzschild(r, r_s)),
                "mu_eff": float(mu_eff_schwarzschild(r, r_s)),
                "Z_ohm": float(gravitational_impedance(r, r_s)),
                "gamma": float(horizon_reflection(r, r_s)),
                "c_local": gw_local_speed(r, r_s),
            }
        )

    return results
