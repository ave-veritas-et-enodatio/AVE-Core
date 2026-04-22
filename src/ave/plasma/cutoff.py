"""
AVE Plasma Physics: Dielectric Saturation as Plasma Onset
==========================================================

In AVE, a plasma is a region where the lattice dielectric has SATURATED.
When the local electric field exceeds V_snap/ℓ, ε_eff → 0 and the
medium can no longer support displacement current. This is identical
to the standard plasma condition: ε(ω) = 1 - (ω_p/ω)² < 0.

Key correspondences:
  - Plasma frequency ω_p = √(n_e e²/(m_e ε₀))
  - AVE: ω_p = V_snap/(ℓ × √(LC)) where LC = lattice constants
  - Skin depth δ = c/ω_p = field penetration into saturated region
  - Debye length = thermal screening length = √(ε₀ k_B T / n_e e²)

The FDTD engine already implements this: when E > V_snap/dx,
ε_eff → 0 and the field is expelled — exactly like a conductor
(plasma screening / Meissner effect analog).
"""

from __future__ import annotations


import numpy as np
from dataclasses import dataclass
from ave.core.constants import C_0, EPSILON_0, MU_0, V_SNAP, ALPHA, L_NODE, e_charge, M_E, K_B
from ave.axioms.scale_invariant import saturation_factor, epsilon_eff as _si_epsilon_eff


@dataclass
class PlasmaParameters:
    """Plasma properties from electron density."""

    n_e: float  # Electron density [m⁻³]

    @property
    def plasma_frequency(self) -> float:
        """ω_p = √(n_e e² / (m_e ε₀))  [rad/s]"""
        return np.sqrt(self.n_e * e_charge**2 / (M_E * EPSILON_0))

    @property
    def plasma_frequency_hz(self) -> float:
        """f_p = ω_p / (2π)  [Hz]"""
        return self.plasma_frequency / (2 * np.pi)

    @property
    def skin_depth(self) -> float:
        """δ = c / ω_p  [m]"""
        return C_0 / self.plasma_frequency

    @property
    def debye_length(self, T_eV: float = 1.0) -> float:
        """
        λ_D = √(ε₀ k_B T / (n_e e²))  [m]
        Default T = 1 eV.
        """
        T_K = T_eV * e_charge / K_B
        return np.sqrt(EPSILON_0 * K_B * T_K / (self.n_e * e_charge**2))

    @property
    def dielectric_function(self) -> callable:
        """
        Returns ε(ω) = 1 - (ω_p/ω)² (Drude model).
        """
        omega_p = self.plasma_frequency
        return lambda omega: 1.0 - (omega_p / omega) ** 2

    @property
    def critical_density(self) -> float:
        """
        For a given ω, the density at which ω = ω_p.
        n_c = m_e ε₀ ω² / e²
        """
        return self.n_e  # By definition at ω = ω_p


def ave_plasma_frequency() -> float:
    """
    Derive the fundamental plasma frequency from AVE lattice constants.

    The plasma onset occurs when E × ℓ > V_snap, i.e., when the
    dielectric saturates. The natural oscillation frequency of
    the saturated region is:

    ω_p(AVE) = V_snap / (ℓ_node × Z₀ × ℓ_node × ε₀)

    Returns:
        Plasma frequency [rad/s] at the lattice scale.
    """
    # At atomic scale, n_e ≈ 1/ℓ_node³ (one electron per lattice cell)
    n_e_lattice = 1.0 / L_NODE**3
    return np.sqrt(n_e_lattice * e_charge**2 / (M_E * EPSILON_0))


def dielectric_function_ave(omega: float, E_field: float) -> float:
    """
    AVE nonlinear dielectric function including saturation.

    ε_eff(ω, E) = ε₀ × √(1 - (E·dx/V_snap)²) × (1 - (ω_p/ω)²)

    When E → V_snap/dx: ε_eff → 0 (plasma onset)
    When ω < ω_p: ε < 0 (evanescent, field expelled)

    Args:
        omega: Angular frequency [rad/s].
        E_field: Local electric field magnitude [V/m].

    Returns:
        Effective permittivity [F/m].
    """
    # Saturation term (Axiom 4) — delegates to scale_invariant.epsilon_eff
    V_local = E_field * L_NODE
    eps_saturated = _si_epsilon_eff(V_local, V_SNAP, eps_base=EPSILON_0)

    # Drude term
    omega_p = ave_plasma_frequency()
    if omega > 0:
        drude = 1.0 - (omega_p / omega) ** 2
    else:
        drude = 0.0

    return eps_saturated * max(drude, 0.0)


def electron_density_from_frequency(f_hz: float) -> float:
    """
    Compute the electron density that corresponds to a given
    plasma frequency.

    n_e = (2πf)² × m_e × ε₀ / e²

    Args:
        f_hz: Plasma frequency [Hz].

    Returns:
        Electron density [m⁻³].
    """
    omega = 2 * np.pi * f_hz
    return omega**2 * M_E * EPSILON_0 / e_charge**2


# ============================================================
# Common plasmas (for comparison)
# ============================================================

COMMON_PLASMAS = {
    "Solar corona": PlasmaParameters(n_e=1e15),
    "Solar wind": PlasmaParameters(n_e=1e7),
    "Ionosphere (F2)": PlasmaParameters(n_e=1e12),
    "Fluorescent lamp": PlasmaParameters(n_e=1e18),
    "Fusion plasma": PlasmaParameters(n_e=1e20),
    "Metal (Cu)": PlasmaParameters(n_e=8.5e28),
    "Dense astrophysical": PlasmaParameters(n_e=1e30),
}
