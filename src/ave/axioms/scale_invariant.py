"""
Scale-Invariant Impedance Operations
=====================================
Every function in this module is domain-agnostic.  The SAME function computes
the reflection coefficient at a Pauli exclusion boundary, a PONDER-01 antenna
port, a seismic discontinuity, or a galactic halo edge.

This is not an analogy.  It is a structural identity:

    Z = √(μ/ε)

The saturation operator ``ε_eff(A) = ε_base · √(1 − (A/A_yield)²)`` is the
single non-linear kernel of the AVE framework, applied identically from
particle confinement (A = E·ℓ_node, A_yield = V_snap) to plasma cutoff
(A = V_local, A_yield = V_snap) to macroscopic dielectric yield.

NOTE ON DEFAULT YIELD LIMITS:
  This module defaults to V_SNAP (= m_e c²/e ≈ 511 kV) — the absolute
  topological node destruction limit.  This is correct for the fundamental
  scale-invariant primitives.  Higher-level wrappers (saturation.py,
  fdtd_3d.py, k4_tlm.py) default to V_YIELD (= √α × V_SNAP ≈ 43.65 kV),
  which is the macroscopic onset of Axiom 4 nonlinearity.  Callers should
  always pass the appropriate yield_limit for their domain:

Functions
---------
impedance(mu, eps)
    Z = √(μ/ε) — the universal operator.
saturation_factor(amplitude, yield_limit)
    √(1 − (A/A_yield)²) — Axiom 4 at any scale.
epsilon_eff(amplitude, yield_limit, eps_base)
    ε_eff = ε_base · saturation_factor()
mu_eff(amplitude, yield_limit, mu_base)
    μ_eff = μ_base · saturation_factor()
reflection_coefficient(Z1, Z2)
    Γ = (Z₂ − Z₁) / (Z₂ + Z₁) — at every boundary, every scale.
transmission_coefficient(Z1, Z2)
    T = 1 + Γ
local_wave_speed(amplitude, yield_limit, c_base)
    c_eff = c_base · (1 − (A/A_yield)²)^(1/4)
impedance_at_strain(amplitude, yield_limit, Z_base)
    Z_eff = Z_base / (1 − (A/A_yield)²)^(1/4)
regime_boundary_eigenvalue(r_sat, nu_vac, ell, c_wave)
    ω = ℓ·c/r_eff — eigenfrequency at any saturation boundary.
phase_transition_Q(ell)
    Q = ℓ — quality factor from shear-reflector geometry.
shear_modulus_ratio(strain, yield_strain)
    G_shear/G₀ = S(ε) — alias for saturation_factor.
co_rotating_decay_rate(omega_R, omega_rotation, ell, m)
    ω_I = (ω_R − m·Ω)/(2ℓ) — FOC/Park co-rotating frame decomposition.
avalanche_factor(V_applied, V_breakdown, n_topology)
    M = 1/(1 − (V/V_BR)^n) — Miller multiplication (inverse of saturation).
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import C_0, EPSILON_0, MU_0, V_SNAP, Z_0

# ────────────────────────────────────────────────────────────────────
# The universal impedance operator
# ────────────────────────────────────────────────────────────────────


def impedance(mu, eps):
    r"""
    Compute the characteristic impedance of any medium.

    .. math::
        Z = \sqrt{\frac{\mu}{\varepsilon}}

    This single formula is valid at every scale:

    ========================  ==========  ==========  ==============
    Domain                    μ-analog    ε-analog    Z expression
    ========================  ==========  ==========  ==============
    Vacuum lattice (fm)       μ₀          ε₀          Z₀ = 376.73 Ω
    Seismic (km)              1/G         1/K         ρ·Vₚ (Rayl)
    Protein (nm)              backbone τ  dipole C    S₁₁ impedance
    ========================  ==========  ==========  ==============

    Args:
        mu: Permeability (or inductive analog) — scalar or array.
        eps: Permittivity (or capacitive analog) — scalar or array.

    Returns:
        Impedance (same shape as inputs).
    """
    from ave.core.universal_operators import universal_impedance

    return universal_impedance(mu, eps)


# ────────────────────────────────────────────────────────────────────
# The Axiom 4 saturation kernel
# ────────────────────────────────────────────────────────────────────


def saturation_factor(
    amplitude,
    yield_limit: float = V_SNAP,
    *,
    clip: bool = True,
) -> np.ndarray:
    r"""
    The universal non-linear saturation factor (Axiom 4).

    .. math::
        S(A) = \sqrt{1 - \left(\frac{A}{A_{yield}}\right)^{\!2}}

    At A = 0: S = 1 (linear Maxwell recovered).
    At A → A_yield: S → 0 (full dielectric collapse / mass confinement).

    This kernel is the ONLY non-linearity in the AVE framework.
    It appears identically in:
      - Particle rest-mass confinement (faddeev_skyrme)
      - FDTD E- and H-field updates (fdtd_3d)
      - Nuclear bond energy (bond_energy_solver)
      - Plasma cutoff (cutoff)
      - Macroscopic dielectric yield (saturation)

    Delegates to ``ave.core.universal_operators.universal_saturation()``
    for the core kernel.  This wrapper adds the ``clip=False`` error path.

    Args:
        amplitude: Local field amplitude, voltage, or strain (scalar/array).
        yield_limit: Absolute saturation limit (default V_snap = m_e c²/e).
        clip: If True (default), clip ratio² to [0, 1-ε] for numerical
              stability.  If False, raise ValueError on rupture.

    Returns:
        Saturation factor S ∈ (0, 1] — same shape as ``amplitude``.

    Raises:
        ValueError: If ``clip=False`` and |amplitude| > yield_limit.
    """
    if not clip:
        ratio_sq = np.asarray(amplitude, dtype=float) ** 2 / yield_limit**2
        if np.any(ratio_sq > 1.0):
            raise ValueError(
                f"Dielectric rupture: |A/A_yield| > 1.0. "
                f"Max ratio² = {np.max(ratio_sq):.6f}. "
                f"The lattice has structurally failed at this strain."
            )
    # Core kernel: single source of truth in universal_operators
    from ave.core.universal_operators import universal_saturation

    return universal_saturation(amplitude, yield_limit)


# ────────────────────────────────────────────────────────────────────
# Effective material parameters under saturation
# ────────────────────────────────────────────────────────────────────


def epsilon_eff(amplitude, yield_limit: float = V_SNAP, eps_base=EPSILON_0, *, clip: bool = True):
    r"""
    Non-linear effective permittivity under dielectric saturation.

    .. math::
        \varepsilon_{eff}(A) = \varepsilon_{base}
            \cdot \sqrt{1 - (A / A_{yield})^2}

    At A = 0: ε_eff → ε_base (linear Maxwell recovered).
    At A → A_yield: ε_eff → 0 (dielectric collapse / impedance divergence).

    NOTE: This is the CONSTITUTIVE permittivity (material property of the
    lattice node). This DECREASES under strain. The OBSERVABLE capacitance
    C_eff = 1/S → ∞ (diverges), which matches Euler-Heisenberg QED.
    These are different quantities: ε is a property, C is a response.

    Args:
        amplitude: Local strain (scalar or array).
        yield_limit: Saturation voltage / strain limit.
        eps_base: Baseline permittivity — ε₀ (or ε₀·ε_r for materials).
        clip: Clip vs. raise on rupture (see ``saturation_factor``).

    Returns:
        Effective permittivity (same shape as amplitude).
    """
    return eps_base * saturation_factor(amplitude, yield_limit, clip=clip)


def mu_eff(amplitude, yield_limit: float = V_SNAP, mu_base=MU_0, *, clip: bool = True):
    r"""
    Non-linear effective permeability under magnetic saturation.

    .. math::
        \mu_{eff}(B) = \mu_{base}
            \cdot \sqrt{1 - (B / B_{yield})^2}

    Args:
        amplitude: Local B-field magnitude (scalar or array).
        yield_limit: Magnetic saturation limit (B_snap).
        mu_base: Baseline permeability — μ₀ (or μ₀·μ_r for materials).
        clip: Clip vs. raise on rupture (see ``saturation_factor``).

    Returns:
        Effective permeability (same shape as amplitude).
    """
    return mu_base * saturation_factor(amplitude, yield_limit, clip=clip)


# ────────────────────────────────────────────────────────────────────
# The universal reflection and transmission coefficients
# ────────────────────────────────────────────────────────────────────


def reflection_coefficient(Z1, Z2=None):
    r"""
    Amplitude reflection coefficient at any impedance boundary.

    .. math::
        \Gamma = \frac{Z_2 - Z_1}{Z_2 + Z_1}

    This is the same operator at EVERY scale:

    ===========================  ==============================
    Scale                        Physical manifestation
    ===========================  ==============================
    Particle (Z_knot → 0)        Γ → −1  (Pauli exclusion)
    Antenna S₁₁                  Γ = (Z_L − Z₀)/(Z_L + Z₀)
    Seismic Moho                 Γ ≈ 0.17  (partial reflection)
    ===========================  ==============================

    Args:
        Z1: Impedance of the incident medium (scalar or array).
        Z2: Impedance of the transmitted medium (scalar or array).
            If None, defaults to Z₀ (vacuum).

    Returns:
        Reflection coefficient Γ ∈ [−1, +1].
    """
    from ave.core.universal_operators import universal_reflection

    if Z2 is None:
        Z2 = Z_0
    return universal_reflection(Z1, Z2)


def transmission_coefficient(Z1, Z2=None):
    r"""
    Amplitude transmission coefficient at any impedance boundary.

    .. math::
        T = 1 + \Gamma = \frac{2 Z_1}{Z_1 + Z_2}

    Args:
        Z1: Impedance of incident medium.
        Z2: Impedance of transmitted medium (default: Z₀).

    Returns:
        Transmission coefficient T.
    """
    return 1.0 + reflection_coefficient(Z1, Z2)


# ────────────────────────────────────────────────────────────────────
# Derived wave-speed and impedance under saturation
# ────────────────────────────────────────────────────────────────────


def local_wave_speed(amplitude, yield_limit: float = V_SNAP, c_base: float = C_0, *, clip: bool = True):
    r"""
    Effective local **shear / GW wave speed** under dielectric saturation.

    .. math::
        c_{shear}(A) = c_{base} \cdot (1 - (A/A_{yield})^2)^{1/4}
                     = c_{base} \cdot \sqrt{S(A)}

    **Derivation — shear wave route (correct):**

    The shear modulus of the vacuum lattice scales with the saturation factor:
        :math:`G_{shear} = G_0 \cdot S(A)`

    The shear wave speed follows from :math:`v = \sqrt{G/\rho}`:
        :math:`c_{shear} = c_0 \cdot \sqrt{S} = c_0 \cdot (1 - (A/A_y)^2)^{1/4}`

    At :math:`A \to A_{yield}`: :math:`S \to 0`, :math:`c_{shear} \to 0`
    (GWs freeze, phonons stop, soliton group velocity → 0 → rest mass).

    **Clarification — EM phase velocity route (different formula):**

    For asymmetric saturation (:math:`\varepsilon_{eff} = \varepsilon_0 S`, :math:`\mu` unchanged):
        :math:`c_{EM} = 1/\sqrt{\mu_0 \varepsilon_0 S} = c_0 / \sqrt{S}  \to \infty`
        (EM phase velocity *rises* in a collapsing dielectric — evanescent modes)

    For symmetric saturation (both :math:`\mu` and :math:`\varepsilon` scale by S):
        :math:`Z = Z_0` (invariant),  :math:`c_{EM} = c_0 / S \to \infty`
        (as expected: the BH interior is an absorbing, not reflecting, medium)

    This function computes the **shear speed** (the ``c_eff`` entry in the
    LIVING_REFERENCE Axiom 4 table labeled "Wave packet freezes (mass)").
    Call ``impedance_at_strain`` if you need the EM impedance :math:`Z_0/\sqrt{S}`.

    Args:
        amplitude: Local strain amplitude.
        yield_limit: Saturation limit.
        c_base: Base wave speed (default c₀).
        clip: See ``saturation_factor``.

    Returns:
        Local shear/GW wave speed [m/s]. Equals ``c_base * sqrt(S)``.
    """
    from ave.core.universal_operators import universal_wave_speed

    if clip:
        from ave.core.constants import EPS_CLIP

        amplitude_ratio_sq = np.asarray(amplitude, dtype=float) ** 2 / yield_limit**2
        # Use a clipped amplitude to pass to universal_wave_speed so it evaluates within bounds
        safe_amplitude = np.sqrt(np.clip(amplitude_ratio_sq, 0.0, 1.0 - EPS_CLIP)) * yield_limit
        return universal_wave_speed(safe_amplitude, yield_limit, c_base)

    return universal_wave_speed(amplitude, yield_limit, c_base)


def impedance_at_strain(amplitude, yield_limit: float = V_SNAP, Z_base: float = Z_0, *, clip: bool = True):
    r"""
    Local characteristic impedance under dielectric saturation.

    .. math::
        Z_{eff}(A) = \frac{Z_{base}}{(1 - (A/A_{yield})^2)^{1/4}}

    As strain increases, impedance rises (the medium becomes opaque
    to transverse waves).  At exact saturation the impedance formally
    diverges — but physically the lattice ruptures first.

    Args:
        amplitude: Local strain amplitude.
        yield_limit: Saturation limit.
        Z_base: Base impedance (default Z₀).
        clip: See ``saturation_factor``.

    Returns:
        Local impedance [Ω].
    """
    from ave.core.universal_operators import universal_dynamic_impedance

    S = saturation_factor(amplitude, yield_limit, clip=clip)
    return universal_dynamic_impedance(Z_base, S)


# ────────────────────────────────────────────────────────────────────
# Universal regime-boundary eigenvalue operators
# ────────────────────────────────────────────────────────────────────


def regime_boundary_eigenvalue(r_sat, nu_vac, ell, c_wave=C_0):
    r"""
    Universal eigenfrequency at any saturation boundary (the 5-step method).

    .. math::
        \omega = \frac{\ell \cdot c}{r_{eff}}, \qquad
        r_{eff} = \frac{r_{sat}}{1 + \nu_{vac}}

    This is the SAME formula at every scale:

    ===========  ============  ======  ========  ===================
    Domain       r_sat         ν       ℓ         Result
    ===========  ============  ======  ========  ===================
    BH QNM       7 M_g         2/7     2         ω·M = 18/49
    Electron     a₀            2/7     n         Bohr levels
    Protein      bond length   2/7     amide     Amide-I eigenmode
    Antenna      stub length   2/7     λ/4       Design frequency
    Tokamak      wall radius   2/7     Alfvén    MHD eigenmode
    ===========  ============  ======  ========  ===================

    Args:
        r_sat: Regime boundary radius (where saturation_factor = 0).
        nu_vac: Poisson ratio of the medium (ν_vac = 2/7 for vacuum).
        ell: Angular mode number (integer).
        c_wave: Wave speed in the medium (default c₀).

    Returns:
        Angular eigenfrequency ω [rad/s].
    """
    from ave.core.universal_operators import universal_regime_eigenvalue

    return universal_regime_eigenvalue(r_sat, nu_vac, ell, c_wave)


def phase_transition_Q(ell):
    r"""
    Universal quality factor from lattice phase transition: Q = ℓ.

    At the saturation boundary (S = 0), the shear modulus vanishes.
    Transverse (shear) waves cannot propagate in the ruptured interior,
    making it a perfect reflector.  The mode has ℓ wavelengths around
    the circumference, each releasing ~1/ℓ of energy per cycle.

    .. math::
        Q = \ell

    This is the gravitational-scale manifestation of the knot crossing
    number → mass stability relationship at the particle scale.

    ===========  ======  ======  ==============================
    Domain       ℓ       Q       Physical meaning
    ===========  ======  ======  ==============================
    BH QNM       2       2       Fundamental GW ringdown
    Overtone 1   3       3       First GW overtone
    Electron     n       n       Atomic orbital Q
    ===========  ======  ======  ==============================

    Args:
        ell: Angular mode number (integer ≥ 1).

    Returns:
        Quality factor Q (dimensionless).
    """
    from ave.core.universal_operators import universal_quality_factor

    return universal_quality_factor(ell)


def shear_modulus_ratio(strain, yield_strain=1.0):
    r"""
    Shear modulus relative to baseline: G_shear / G_shear₀ = S(ε).

    At saturation (ε = yield_strain): G_shear → 0 (topology melts).
    Transverse (shear) waves cannot propagate.
    Identical to ``saturation_factor`` but named for physical clarity.

    Args:
        strain: Local strain amplitude (scalar or array).
        yield_strain: Strain at which topology ruptures (default 1.0).

    Returns:
        Shear modulus ratio S ∈ [0, 1].
    """
    return saturation_factor(strain, yield_limit=yield_strain, clip=True)


def co_rotating_decay_rate(omega_R, omega_rotation, ell, m=None):
    r"""
    Co-rotating frame decomposition: the FOC/Park transform operator.

    Decomposes the mode frequency into co-rotating (reactive) and
    differential (radiating) components:

    .. math::
        \omega_I = \frac{\omega_R - m \cdot \Omega}{2\,\ell}

    This is structurally identical to Field-Oriented Control (FOC)
    of a BLDC motor:

    ==================  =========================  ====================
    FOC Motor           BH QNM                     Universal
    ==================  =========================  ====================
    d-axis (flux)       m·Ω (co-rotating)          Reactive component
    q-axis (torque)     (ω_R − m·Ω) (differential) Radiating component
    Back-EMF            Curvature radiation ω_I     Decay rate
    Stall = 0 torque    Superradiance (ω_R = m·Ω)  Q → ∞
    ==================  =========================  ====================

    At the **superradiance threshold** (ω_R = m·Ω): ω_I → 0, Q → ∞.
    The mode gains energy from the rotation — no net radiation.

    Applicable domains:
      - BH ringdown: Ω = lattice frame-dragging at photon sphere
      - Nuclear: Ω = shell rotation → magic number corrections
      - BLDC motor: Ω = rotor angular velocity, ω_R = stator field
      - Tokamak: Ω = plasma toroidal rotation

    Args:
        omega_R: Mode angular frequency [rad/s or dimensionless].
        omega_rotation: Co-rotating angular velocity Ω [same units].
        ell: Angular mode number (integer ≥ 1).
        m: Azimuthal mode number (default: m = ell for co-rotating).

    Returns:
        Decay rate ω_I [same units as omega_R].
        Returns 0 if at or beyond superradiance (ω_R ≤ m·Ω).
    """
    if m is None:
        m = ell
    omega_eff = omega_R - m * omega_rotation
    omega_I = omega_eff / (2.0 * ell)
    return max(omega_I, 0.0)


def avalanche_factor(V_applied, V_breakdown, n_topology):
    r"""
    Miller avalanche multiplication: the INVERSE of saturation.

    .. math::
        M = \frac{1}{1 - (V / V_{BR})^n}

    At V → 0:     M = 1  (linear, no avalanche).
    At V → V_BR:  M → ∞  (breakdown, divergence).

    This is the topological dual of the saturation factor:

    ====================  ===================================
    Saturation            Avalanche
    ====================  ===================================
    S = √(1 − (A/A_y)²)  M = 1/(1 − (V/V_BR)^n)
    S → 0 at boundary     M → ∞ at boundary
    Continuous (n=2)       Discrete (n = crossing number)
    Kills propagation      Amplifies coupling
    ====================  ===================================

    The exponent n is set by the **topology**: for nuclear binding,
    n = 5 (cinquefoil crossing number).  For a simple junction,
    n could be 3 (trefoil) or 7 (septafoil).

    Applied domains:
      - Nuclear binding: V = Coulomb/alpha, V_BR = 6·αℏc/D, n = 5
      - Semiconductor: V = reverse bias, V_BR = junction breakdown, n varies
      - LED: V = current density, V_BR = droop onset, n = recombination order

    Args:
        V_applied: Applied stress (voltage, Coulomb, current density).
        V_breakdown: Breakdown threshold.
        n_topology: Exponent = crossing number or recombination order.

    Returns:
        Multiplication factor M ≥ 1.
    """
    from ave.core.universal_operators import universal_avalanche_factor

    return universal_avalanche_factor(V_applied, V_breakdown, n_topology)
