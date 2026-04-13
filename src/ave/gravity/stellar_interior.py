"""
AVE Stellar Interior — Impedance Profile of Stars
====================================================

Models stellar interiors as radial impedance profiles using the
same operators (impedance, saturation, reflection) that govern
all other scales in the AVE framework.

Physical picture:
  - A star is a self-gravitating ball of plasma
  - The plasma density n_e(r) increases toward the core
  - Each radial shell has a local plasma frequency ω_p(r)
  - Below ω_p, EM waves cannot propagate → ε < 0 → Γ → −1
  - The stellar interior IS a giant spherical plasma waveguide

This bridges plasma.cutoff (which handles uniform plasma) to
the gravity module (which handles the Schwarzschild impedance).
A star combines BOTH: gravitational impedance gradient PLUS
plasma cutoff.

Key correspondences:
    Earth (seismic)     Star (plasma)       Black hole (gravity)
    ───────────────     ─────────────       ────────────────────
    PREM layers         SSM layers          Schwarzschild metric
    K, G moduli         n_e, T profiles     ε_eff, μ_eff
    Moho reflection     Tachocline Γ        Horizon Γ = −1
"""
from __future__ import annotations


import numpy as np
from dataclasses import dataclass
from typing import Optional

from ave.core.constants import (
    C_0, EPSILON_0, MU_0, Z_0, M_E, e_charge, HBAR, ALPHA, K_B,
    M_SUN, M_PROTON, EPS_NUMERICAL,
)
from ave.axioms.scale_invariant import (
    impedance,
    reflection_coefficient,
    saturation_factor,
)


def plasma_frequency(n_e):
    """ω_p = √(n_e e² / (m_e ε₀))  [rad/s]."""
    return np.sqrt(np.asarray(n_e, dtype=float) * e_charge**2 / (M_E * EPSILON_0))


# ═══════════════════════════════════════════════════════════════
# Standard Solar Model — simplified radial profile
# ═══════════════════════════════════════════════════════════════

R_SUN = 6.957e8  # Solar radius [m]
L_SUN = 3.828e26  # Solar luminosity [W]

@dataclass
class StellarLayer:
    """A radial shell in a stellar interior."""
    name: str
    r_inner: float     # Inner radius [units of R_star]
    r_outer: float     # Outer radius [units of R_star]
    n_e: float         # Electron density [m⁻³]
    T: float           # Temperature [K]
    composition: str   # Dominant species

    @property
    def omega_p(self) -> float:
        """Plasma frequency [rad/s]."""
        return plasma_frequency(self.n_e)

    @property
    def f_p_hz(self) -> float:
        """Plasma frequency [Hz]."""
        return self.omega_p / (2 * np.pi)

    @property
    def epsilon_r(self) -> float:
        """Relative permittivity at low frequency (ω << ω_p → ε < 0)."""
        # For radio waves trying to penetrate: ε_r = 1 - (ω_p/ω)²
        # At optical frequencies (ω >> ω_p): ε_r ≈ 1 (transparent)
        # For the impedance profile, we use the plasma contribution:
        return 1.0  # Optical regime; cutoff only matters below ω_p

    @property
    def impedance_ratio(self) -> float:
        """Z/Z₀ for this layer (from plasma density)."""
        # Higher n_e → lower Z (more conductive)
        n_ref: float = 1e6  # Reference: interplanetary space
        eps_r_analog = 1.0 + self.n_e / n_ref
        return impedance(1.0, eps_r_analog)


# Standard Solar Model layers (Bahcall & Pinsonneault, 2004)
SSM_LAYERS = [
    StellarLayer("Core",          0.00, 0.25, 1.5e32, 1.57e7, "H/He"),
    StellarLayer("Radiative",     0.25, 0.70, 1.0e30, 7.0e6,  "H/He"),
    StellarLayer("Tachocline",    0.70, 0.72, 2.0e29, 2.0e6,  "H/He"),
    StellarLayer("Convection",    0.72, 0.95, 1.0e28, 5.0e5,  "H/He"),
    StellarLayer("Photosphere",   0.95, 1.00, 1.0e23, 5.8e3,  "H/He"),
    StellarLayer("Chromosphere",  1.00, 1.003, 1.0e17, 1.0e4, "H"),
    StellarLayer("Corona",        1.003, 3.0, 1.0e15, 1.5e6,  "H"),
]


def build_radial_profile(layers: list = None,
                          n_points: int = 500,
                          r_star_m: float = R_SUN) -> dict:
    """
    Build a continuous radial impedance profile from stellar layers.

    Returns:
        Dict with arrays:
            'r_frac': Fractional radius r/R_star
            'r_m': Absolute radius [m]
            'n_e': Electron density [m⁻³]
            'T_K': Temperature [K]
            'omega_p': Plasma frequency [rad/s]
            'Z_ratio': Z/Z₀
            'layer_names': Layer name at each point
    """
    if layers is None:
        layers = SSM_LAYERS

    r_frac = np.linspace(0.001, layers[-1].r_outer, n_points)
    n_e = np.zeros(n_points)
    T = np.zeros(n_points)
    names = []

    for i, r in enumerate(r_frac):
        for layer in layers:
            if layer.r_inner <= r <= layer.r_outer:
                # Linear interpolation within layer
                frac = (r - layer.r_inner) / max(
                    layer.r_outer - layer.r_inner, EPS_NUMERICAL)
                n_e[i] = layer.n_e
                T[i] = layer.T
                names.append(layer.name)
                break
        else:
            n_e[i] = layers[-1].n_e
            T[i] = layers[-1].T
            names.append(layers[-1].name)

    omega_p = plasma_frequency(n_e)
    # Z ratio: impedance drops in high-density plasma
    n_ref = 1e6
    # Map plasma density to relative permittivity analog
    eps_r_analog = 1.0 + n_e / n_ref
    Z_ratio = impedance(1.0, eps_r_analog)

    return {
        'r_frac': r_frac,
        'r_m': r_frac * r_star_m,
        'n_e': n_e,
        'T_K': T,
        'omega_p': omega_p,
        'Z_ratio': Z_ratio,
        'layer_names': names,
    }


def tachocline_reflection() -> float:
    """
    Reflection coefficient at the tachocline boundary.

    The tachocline (r ≈ 0.70-0.72 R☉) separates the rigid
    radiative zone from the convective envelope. In AVE, this
    is an impedance discontinuity — the same physics as the
    Moho boundary in the Earth.

    Returns:
        Reflection coefficient at the tachocline.
    """
    # Radiative zone: n_e ≈ 10³⁰
    Z_rad = impedance(1.0, 1.0 + 1e30 / 1e6)
    # Convection zone: n_e ≈ 10²⁸
    Z_conv = impedance(1.0, 1.0 + 1e28 / 1e6)
    return reflection_coefficient(Z_rad, Z_conv)


def photosphere_reflection() -> float:
    """
    Reflection coefficient at the photosphere boundary.

    The photosphere (τ = 2/3 surface) is where photons escape.
    In AVE, this is the impedance-matching point where Z_plasma
    transitions to Z₀ (free space).

    Returns:
        Reflection coefficient at the photosphere.
    """
    # Photosphere: n_e ≈ 10²³
    Z_photo = impedance(1.0, 1.0 + 1e23 / 1e6)
    # Free space above: Z = Z₀ → ratio = 1
    Z_space = 1.0  # normalised
    return reflection_coefficient(Z_photo, Z_space)


def solar_opacity_from_impedance(r_frac: float,
                                   freq_hz: float = 5e14) -> float:
    """
    Photon opacity at radius r as impedance mismatch.

    At optical frequencies (f ~ 5×10¹⁴ Hz), the plasma is transparent
    if ω >> ω_p. The opacity comes from collisional broadening, which
    in AVE is Ohmic damping in the LC lattice.

    For radio frequencies (f < f_p), the plasma is opaque (Γ → −1).

    Args:
        r_frac: Fractional radius (0 = centre, 1 = surface).
        freq_hz: Photon frequency [Hz].

    Returns:
        |Γ|² — fraction of power reflected (opacity proxy).
    """
    # Find the layer
    for layer in SSM_LAYERS:
        if layer.r_inner <= r_frac <= layer.r_outer:
            n_e = layer.n_e
            break
    else:
        n_e = SSM_LAYERS[-1].n_e

    omega = 2 * np.pi * freq_hz
    omega_p = plasma_frequency(n_e)

    if omega > omega_p:
        # Transparent: ε_r > 0
        eps_r = 1 - (omega_p / omega)**2
        Z_local = impedance(1.0, eps_r)  # normalised
        gamma = reflection_coefficient(1.0, Z_local)
    else:
        # Opaque: total reflection
        gamma = -1.0

    return float(gamma**2)


def helioseismology_modes(n_max: int = 10,
                            l: int = 0) -> np.ndarray:
    """
    Predict solar p-mode frequencies from the impedance profile.

    p-modes are standing acoustic waves trapped between the
    surface and an inner turning point. In AVE, they are
    transmission line resonances — exactly like the protein
    S₁₁ cavity modes.

    The fundamental frequency depends on the sound travel time:

        f_n ≈ n / (2T)  where T = ∫ dr/c_s(r)

    For the Sun: fundamental ≈ 68 μHz (T ≈ ~2 hours).

    Args:
        n_max: Maximum radial order.
        l: Angular degree (0 = radial).

    Returns:
        Array of predicted frequencies [μHz].
    """
    # Solar sound speed profile (simplified)
    # c_s ≈ √(γ k_B T / m_p)  where γ = 5/3
    k_B_val = float(K_B)
    m_p = float(M_PROTON)
    gamma = 5.0 / 3.0

    # Acoustic travel time through the Sun
    profile = build_radial_profile(n_points=200)
    dr = np.diff(profile['r_m'])
    T_mid = 0.5 * (profile['T_K'][:-1] + profile['T_K'][1:])
    c_s = np.sqrt(gamma * k_B_val * T_mid / m_p)
    travel_time = np.sum(dr / c_s)  # one-way [s]

    # Resonant frequencies: f_n = n / (2T)
    # With angular correction: f_nl ≈ (n + l/2 + 1/4) × Δν
    delta_nu = 1.0 / (2 * travel_time)  # Large frequency separation

    modes = np.array([(n + l/2 + 0.25) * delta_nu for n in range(1, n_max + 1)])
    return modes * 1e6  # Convert Hz to μHz


def print_stellar_summary():
    """Print a summary of the Standard Solar Model impedance profile."""
    print("\n" + "=" * 70)
    print("  Standard Solar Model — AVE Impedance Profile")
    print("=" * 70)
    for layer in SSM_LAYERS:
        print(f"  {layer.name:15s}  r={layer.r_inner:.3f}-{layer.r_outer:.3f} R☉  "
              f"n_e={layer.n_e:.1e} m⁻³  T={layer.T:.1e} K  "
              f"f_p={layer.f_p_hz:.2e} Hz")
    print()
    print(f"  Tachocline Γ:   {tachocline_reflection():.6f}")
    print(f"  Photosphere Γ:  {photosphere_reflection():.6f}")
    print()
    p_modes = helioseismology_modes(5)
    print(f"  p-mode frequencies (n=1-5, l=0):")
    for n, f in enumerate(p_modes, 1):
        print(f"    n={n}: {f:.1f} μHz")
    print("=" * 70)
