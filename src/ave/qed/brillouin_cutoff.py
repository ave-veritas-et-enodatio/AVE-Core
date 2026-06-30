r"""
The Brillouin-cutoff propagator — a FORM-DERIVED 1-loop regulator
=================================================================

Substrate-native first (the substrate-walk, before the numerics):

  * **Substrate dynamics.** This is k-space *mode-counting over the first
    Brillouin zone*, NOT a continuum-Helmholtz / Lagrangian-minimization
    construct. The lattice carries wave propagation; the discrete dispersion
    relation is the K4/cubic-bond sum

        ω²/c² = (2/ℓ²) · Σ_b (1 − cos(k·b̂·ℓ))                     (the denominator)

    and the loop integral is a sum over the FINITE set of BZ modes
    (N = V/ℓ³). Finiteness is by mode-count, NOT by a counterterm.

  * **The FORM is derived (Axiom 1).** The momentum cutoff is not imposed by
    hand; it falls out of the EXACT discrete-Hilbert commutator (DCVE App-E,
    `manuscript/ave-kb/vol2/appendices/app-e-dcve/dcve-specification.md`:36-42):

        p_disc = (ℏ / i ℓ) · sin(k ℓ)
        [x, p_disc] = iℏ · cos(k ℓ) = iℏ · √(1 − (ℓ p / ℏ)²)

    As p → ℏ/ℓ the commutator → 0; the lattice cannot represent momenta beyond
    the Brillouin edge |k| = k_max = π/ℓ_node. This is the more-principled-than-
    dim-reg half: the regulator is a PHYSICAL lattice fact, not a subtraction.

  * **Distinct-cutoff discipline** (constants.py:286-294): there are TWO distinct
    k-space ceilings and they must NOT be conflated:

        SPATIAL  k_max = π / ℓ_node   ≈ 8.135e12  /m   — the LOOP-INTEGRAL bound
        TEMPORAL ω_C   = c / ℓ_node   ≈ 7.763e20 rad/s — the μ-grade (circulation) bound

    with the exact ratio  k_max / (ω_C / c) = π. **This module's loop integral is
    bounded by the SPATIAL k_max = π/ℓ_node.** ω_C is the μ-saturation ceiling
    and does NOT enter the loop quadrature here.

FORM/VALUE: the cutoff FORM is FORM-DERIVED (Axiom 1). No α is used in this
module — the regulator is purely geometric (ℓ_node). (α enters the *birefringence*
magnitude, a separate module; this one is α-clean.)
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import L_NODE

# =============================================================================
# The SPATIAL Brillouin loop bound (DECLARED — not the temporal ω_C bound).
# =============================================================================
#   k_max = π / ℓ_node  — the spatial Brillouin zone-edge; the LOOP-INTEGRAL
#   ceiling. (constants.OMEGA_C = c/ℓ_node is the TEMPORAL μ-grade bound; the
#   exact ratio k_max·ℓ_node / (ω_C·ℓ_node/c) = π. Do NOT conflate them.)
K_MAX_SPATIAL: float = np.pi / L_NODE  # ≈ 8.135e12 /m


def lattice_dispersion_denominator(
    k: np.ndarray,
    *,
    ell: float = L_NODE,
    omega_over_c: float = 0.0,
) -> np.ndarray:
    r"""
    The lattice propagator denominator (the K4/cubic-bond dispersion):

    .. math::
        D_{lat}(\mathbf k) = \frac{2}{\ell^2}\sum_{b}\bigl(1-\cos(k_b\,\ell)\bigr)
                             \;-\;\frac{\omega^2}{c^2}

    The bond sum runs over the three cubic axes b ∈ {x, y, z} (the simplest
    Brillouin zone; the K4 diamond stencil shares the same small-k limit). At
    ``omega_over_c = 0`` this is the static (Euclidean) propagator denominator
    used for the loop quadrature.

    **Recover-QED:** at ``|k|ℓ ≪ 1``, ``cos(kℓ) → 1 − ½(kℓ)²`` so
    ``D_lat → |k|² − ω²/c²`` — the continuum (QED) propagator denominator. The
    relative error is the Taylor remainder ``(kℓ)²/12``.

    **Activate-at-cutoff:** at the BZ edge ``k_b = π/ℓ`` the per-axis term
    saturates at ``4/ℓ²`` (12/ℓ² at the (π,π,π) corner) — the dispersion is
    band-limited, which is *why* the loop integral is finite.

    Args:
        k: momentum vector(s); last axis is the 3 Cartesian components [1/m].
           Shape ``(..., 3)``.
        ell: lattice pitch (default ℓ_node). The cutoff scale.
        omega_over_c: ω/c [1/m] (default 0 → static/Euclidean denominator).

    Returns:
        The denominator ``D_lat(k)`` [1/m²], shape ``k.shape[:-1]``.
    """
    k = np.asarray(k, dtype=float)
    # bond sum over the three cubic axes (last axis = components)
    bond_sum = np.sum(1.0 - np.cos(k * ell), axis=-1)
    return (2.0 / ell**2) * bond_sum - omega_over_c**2


def continuum_loop_integral(
    cutoff_lambda: float,
    *,
    m_sq: float,
    n_radial: int = 40000,
) -> float:
    r"""
    The **continuum** 1-loop integrand evaluated to a hard sphere ``|k| < Λ``.

    .. math::
        \Pi_{cont}(\Lambda) = \int_{|k|<\Lambda}\!\! d^3k\;\frac{1}{k^2+m^2}
            = 4\pi\!\int_0^{\Lambda}\!\frac{k^2}{k^2+m^2}\,dk

    This is the prototypical UV-divergent vacuum-polarization / self-energy
    integrand: it **grows without bound** (~Λ, linear) as Λ → ∞. In standard QED this
    is the divergence that *needs* a regulator (dim-reg + a counterterm). It is
    provided here ONLY to exhibit the divergence the BZ cutoff removes — there is
    no AVE claim in the continuum branch.

    Args:
        cutoff_lambda: the hard UV cutoff Λ [1/m].
        m_sq: the regulator mass² (IR scale) [1/m²].
        n_radial: radial quadrature points.

    Returns:
        The continuum loop integral truncated at Λ (grows with Λ — divergent).
    """
    kk = np.linspace(0.0, cutoff_lambda, n_radial)
    integrand = kk**2 / (kk**2 + m_sq)
    return float(4.0 * np.pi * np.trapezoid(integrand, kk))


def loop_integral_brillouin_zone(
    *,
    m_sq: float,
    ell: float = L_NODE,
    n_grid: int = 48,
) -> float:
    r"""
    The **lattice** 1-loop integral over the FIRST Brillouin zone — FINITE by
    construction (no counterterm).

    .. math::
        \Pi_{lat} = \int_{BZ}\!\! d^3k\;\frac{1}{D_{lat}(\mathbf k)+m^2},
        \qquad \mathbf k \in \Bigl[-\tfrac{\pi}{\ell},\tfrac{\pi}{\ell}\Bigr]^3

    The integration domain is bounded by the SPATIAL cutoff ``k_max = π/ℓ`` on
    every axis (the declared loop bound — NOT ω_C). Because the band-limited
    dispersion ``D_lat`` never exceeds ``12/ℓ²`` and the domain is the compact BZ
    (a finite mode count N ∝ (n_grid)³), the integral is finite for any
    ``m_sq ≥ 0`` — there is nothing to subtract.

    **Recover-QED:** as ``ℓ → 0`` the BZ opens to all of k-space and the
    integrand → the continuum form, recovering the (divergent-without-cutoff)
    continuum result; at FIXED physical ℓ_node the integral is the lattice-
    regulated, finite value.

    Args:
        m_sq: the regulator mass² (IR scale) [1/m²].
        ell: lattice pitch (default ℓ_node). Sets the BZ size π/ℓ.
        n_grid: modes per axis (the discrete BZ sampling; convergence ≥ 48).

    Returns:
        The finite BZ-regulated loop integral [m].
    """
    # uniform BZ grid k ∈ [-π/ℓ, π/ℓ)^3 — midpoint-free periodic sampling
    axis = np.linspace(-np.pi / ell, np.pi / ell, n_grid, endpoint=False)
    dk = (2.0 * np.pi / ell) / n_grid
    kx, ky, kz = np.meshgrid(axis, axis, axis, indexing="ij")
    k = np.stack([kx, ky, kz], axis=-1)
    denom = lattice_dispersion_denominator(k, ell=ell) + m_sq
    return float(np.sum(1.0 / denom) * dk**3)
