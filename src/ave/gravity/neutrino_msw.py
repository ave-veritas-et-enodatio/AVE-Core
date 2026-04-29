"""
AVE Neutrino MSW Effect — Flavor Mixing as Impedance Mode Coupling
====================================================================

The MSW (Mikheyev–Smirnov–Wolfenstein) effect describes neutrino
flavor oscillation in matter. In the standard model, the effective
mass squared of the electron neutrino changes with electron density
due to W-boson exchange.

In the AVE framework, this is impedance-dependent mode coupling:
  - Neutrino flavors are propagation modes in the LC lattice
  - In vacuum: modes have fixed mixing angle θ₁₂
  - In matter: the local electron density n_e modifies the
    effective impedance seen by the ν_e mode
  - When the matter potential V_CC matches Δm²/(2E), the
    modes undergo RESONANT CONVERSION (MSW resonance)

This is the SAME physics as:
  - Mode coupling in a tapered waveguide (electromagnetic)
  - Landau-Zener transition (atomic physics)
  - Impedance taper matching (transmission line engineering)

The module connects to stellar_interior.py: the solar n_e(r) profile
determines which radius produces MSW resonance.

Key equation:
    V_CC = √2 G_F n_e  (matter potential)
    θ_m = ½ arctan(sin2θ / (cos2θ - V_CC/(Δm²/2E)))

When V_CC = Δm²cos2θ/(2E): resonance → θ_m = π/4 → maximal mixing.
"""

from dataclasses import dataclass

import numpy as np

from ave.axioms.scale_invariant import reflection_coefficient
from ave.core.constants import C_0, EPS_CLIP, G_F, HBAR_EV_S, SIN2_THETA_12, SIN2_THETA_13, SIN2_THETA_23, e_charge

# ═══════════════════════════════════════════════════════════════
# Physical constants for neutrino physics
# ═══════════════════════════════════════════════════════════════

# @open_problem (Axiomatic Neutrino Sector)
# Neutrino mass splittings (PDG 2023). These are currently hard-coded as
# empirical TARGET bounds and constitute the final open problem in the electroweak
# derivation chain. They must eventually be derived from the topological loop
# eigenvalue gaps via PMNS mode coupling.
DELTA_M21_SQ_TARGET = 7.53e-5  # Δm²₂₁ [eV²] (solar)
DELTA_M32_SQ_TARGET = 2.453e-3  # |Δm²₃₂| [eV²] (atmospheric)

# Mixing angles — derived from AVE (regime-boundary eigenvalue method)
# See ave.topological.mixing_derivation for the full derivation chain.
THETA_12 = np.arcsin(np.sqrt(SIN2_THETA_12))  # Solar: ν_vac + 1/45
THETA_23 = np.arcsin(np.sqrt(SIN2_THETA_23))  # Atmospheric: 1/2 + 2/45
THETA_13 = np.arcsin(np.sqrt(SIN2_THETA_13))  # Reactor: 1/(c₁c₃) = 1/45

# Conversion factors
EV_TO_JOULE = float(e_charge)  # from constants.py
# HBAR_EV_S imported from ave.core.constants (single source of truth)
MEV_TO_JOULE = EV_TO_JOULE * 1e6


@dataclass
class NeutrinoFlavor:
    """A neutrino flavor state."""

    name: str
    energy_mev: float  # Neutrino energy [MeV]


# ═══════════════════════════════════════════════════════════════
# Matter potential — the impedance modification
# ═══════════════════════════════════════════════════════════════


def matter_potential(n_e: float) -> float:
    r"""
    Charged-current matter potential (Wolfenstein potential).

    .. math::
        V_{CC} = \sqrt{2} \, G_F \, n_e

    In AVE, this IS the impedance modification: the local
    electron density shifts the effective Z seen by the ν_e mode.

    Args:
        n_e: Electron density [m⁻³].

    Returns:
        Matter potential [eV].
    """
    # Convert n_e to natural units: n_e [m⁻³] → [(ℏc)⁻³ eV³]
    # V_CC = √2 G_F n_e [eV] (using G_F in appropriate units)
    # hbar_c_m = HBAR_EV_S * C_0  # ℏc [eV·m]
    # n_e_natural = n_e * hbar_c_m**3  # [eV³]  # bulk lint fixup pass
    # G_F is in GeV⁻² = 10⁻⁶ eV⁻²... but we need consistent units
    # Simpler: V_CC = √2 × 1.1664e-5 GeV⁻² × (ℏc)³ × n_e
    # In SI: V_CC [eV] = √2 × G_F [GeV⁻²] × (ℏc)³ [GeV³·m³] × n_e [m⁻³]
    hbar_c_gev_m = HBAR_EV_S * C_0 * 1e-9  # ℏc [GeV·m]
    V_cc = np.sqrt(2) * G_F * hbar_c_gev_m**3 * n_e * 1e9  # Convert GeV to eV
    return V_cc


def effective_mixing_angle(
    n_e: float, E_mev: float, theta_vac: float = THETA_12, delta_m_sq: float = DELTA_M21_SQ_TARGET
) -> float:
    r"""
    Effective mixing angle in matter (MSW formula).

    .. math::
        \tan 2\theta_m = \frac{\sin 2\theta_{vac}}
        {\cos 2\theta_{vac} - \frac{2E \cdot V_{CC}}{\Delta m^2}}

    Args:
        n_e: Electron density [m⁻³].
        E_mev: Neutrino energy [MeV].
        theta_vac: Vacuum mixing angle [rad].
        delta_m_sq: Mass-squared splitting [eV²].

    Returns:
        Effective mixing angle in matter [rad].
    """
    V = matter_potential(n_e)
    E_ev = E_mev * 1e6  # Convert MeV to eV

    # Ratio: A = 2E × V_CC / Δm²
    A = 2 * E_ev * V / delta_m_sq

    sin2 = np.sin(2 * theta_vac)
    cos2 = np.cos(2 * theta_vac)

    denominator = cos2 - A
    # MSW resonance occurs when cos(2θ_vac) = A; the denominator vanishes and
    # mixing becomes maximal. EPS_CLIP (1e-15, the float64 tight bound) is the
    # singularity threshold below which we short-circuit to the limit value.
    if abs(denominator) < EPS_CLIP:
        return np.pi / 4  # Resonance → maximal mixing

    # tan2theta_m = sin2 / denominator  # bulk lint fixup pass
    theta_m = 0.5 * np.arctan2(sin2, denominator)

    # Keep in [0, π/2]
    return abs(theta_m)


def msw_resonance_density(E_mev: float, theta_vac: float = THETA_12, delta_m_sq: float = DELTA_M21_SQ_TARGET) -> float:
    r"""
    Electron density at MSW resonance.

    .. math::
        n_e^{res} = \frac{\Delta m^2 \cos 2\theta}{2\sqrt{2} G_F E}

    At this density, the matter mixing angle θ_m = π/4 (maximal).

    Args:
        E_mev: Neutrino energy [MeV].
        theta_vac: Vacuum mixing angle [rad].
        delta_m_sq: Mass-squared splitting [eV²].

    Returns:
        Resonance electron density [m⁻³].
    """
    E_ev = E_mev * 1e6
    cos2theta = np.cos(2 * theta_vac)

    # V_CC(res) = Δm² cos2θ / (2E)
    V_res = delta_m_sq * cos2theta / (2 * E_ev)

    # Invert matter_potential: n_e = V_CC / (√2 × G_F × (ℏc)³)
    hbar_c_gev_m = HBAR_EV_S * C_0 * 1e-9
    n_e_res = V_res / (np.sqrt(2) * G_F * hbar_c_gev_m**3 * 1e9)
    return n_e_res


def survival_probability(
    n_e: float,
    E_mev: float,
    L_m: float = 1.0,
    theta_vac: float = THETA_12,
    delta_m_sq: float = DELTA_M21_SQ_TARGET,
) -> float:
    r"""
    Electron neutrino survival probability in matter.

    For adiabatic MSW conversion (valid in the Sun):

    .. math::
        P(\nu_e \to \nu_e) = \frac{1}{2} +
        \frac{1}{2}\cos 2\theta_m^{prod} \cdot \cos 2\theta_{vac}

    where θ_m^{prod} is the mixing angle at the production point.

    Args:
        n_e: Electron density at production [m⁻³].
        E_mev: Neutrino energy [MeV].
        L_m: Baseline (not used for adiabatic; kept for API).
        theta_vac: Vacuum mixing angle [rad].
        delta_m_sq: Mass-squared splitting [eV²].

    Returns:
        Survival probability (0 to 1).
    """
    theta_m = effective_mixing_angle(n_e, E_mev, theta_vac, delta_m_sq)
    cos2_m = np.cos(2 * theta_m)
    cos2_vac = np.cos(2 * theta_vac)
    P_ee = 0.5 + 0.5 * cos2_m * cos2_vac
    return float(np.clip(P_ee, 0, 1))


def impedance_analogy(n_e: float, E_mev: float) -> dict[str, float | bool]:
    """
    Express the MSW effect as an impedance problem.

    The neutrino propagation is mapped to a transmission line:
      - ν_e mode: Z_e = Z₀ × (1 + V_CC/V₀)  (modified by matter)
      - ν_μ mode: Z_μ = Z₀  (unchanged by charged current)
      - Mixing = impedance-mismatch-driven mode coupling
      - MSW resonance = critical coupling (Z_e = Z_μ)

    Args:
        n_e: Electron density [m⁻³].
        E_mev: Neutrino energy [MeV].

    Returns:
        Dict with impedance analogy quantities.
    """
    V = matter_potential(n_e)
    E_ev = E_mev * 1e6
    A = 2 * E_ev * V / DELTA_M21_SQ_TARGET  # Normalised potential

    # Z_e/Z_μ ratio (normalised)
    Z_ratio = 1 + A * np.cos(2 * THETA_12)

    # Reflection coefficient between modes
    Z_e = 1 + A
    Z_mu = 1.0
    gamma = reflection_coefficient(Z_e, Z_mu)

    theta_m = effective_mixing_angle(n_e, E_mev)
    P_ee = survival_probability(n_e, E_mev)

    return {
        "V_CC_eV": V,
        "A_ratio": A,
        "Z_e_over_Z_mu": Z_ratio,
        "gamma_mode": float(gamma),
        "theta_m_rad": theta_m,
        "theta_m_deg": np.degrees(theta_m),
        "P_ee": P_ee,
        "is_resonance": abs(A - np.cos(2 * THETA_12)) < 0.1,
    }


def solar_msw_profile(E_mev: float = 10.0, n_points: int = 200) -> dict[str, np.ndarray | float]:
    """
    Compute MSW mixing across the solar interior.

    Uses the SSM radial n_e profile (from stellar_interior.py)
    to compute how the mixing angle and survival probability
    evolve from core to surface.

    Args:
        E_mev: Neutrino energy [MeV].
        n_points: Number of radial points.

    Returns:
        Dict with arrays for the MSW profile.
    """
    from ave.gravity.stellar_interior import build_radial_profile

    profile = build_radial_profile(n_points=n_points)
    n_e = profile["n_e"]
    r_frac = profile["r_frac"]

    theta_m = np.array([effective_mixing_angle(ne, E_mev) for ne in n_e])
    P_ee = np.array([survival_probability(ne, E_mev) for ne in n_e])
    n_e_res = msw_resonance_density(E_mev)

    return {
        "r_frac": r_frac,
        "n_e": n_e,
        "theta_m_deg": np.degrees(theta_m),
        "P_ee": P_ee,
        "n_e_resonance": n_e_res,
        "E_mev": E_mev,
    }
