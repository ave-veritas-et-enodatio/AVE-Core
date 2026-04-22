"""
AVE Gravitational Wave Detection
==================================

Models GW detectors (LIGO, LISA, etc.) as resonant impedance antennas
in the AVE framework. A detector arm is a Fabry-Pérot cavity embedded
in the LC vacuum — it converts tiny lattice strain (impedance
modulation) into measurable phase shift.

Physical picture:
  - GW propagates as inductive shear wave (from gw_propagation.py)
  - GW strain h modulates local impedance: Z(t) = Z₀(1 + h sin ωt)
  - Detector arm = resonant transmission line of length L
  - Phase accumulated: Δφ = (ω/c) × L × h × N_bounces
  - Strain sensitivity: h_min = 1/(ω × L × N_bounces × √(P/ℏω))

This is the SAME physics as:
  - Microwave cavity perturbation (electromagnetic)
  - Pulse-echo ultrasonics (seismic)
  - Impedance matching in protein folding (biological)

All use the universal operators from scale_invariant.py.

Key insight: LIGO is NOT "measuring spacetime curvature."
It is measuring the IMPEDANCE PERTURBATION of a lossless
transmission line caused by passing inductive shear waves.
"""

from __future__ import annotations


import numpy as np
from dataclasses import dataclass
from typing import Optional

from ave.core.constants import (
    C_0,
    EPSILON_0,
    MU_0,
    Z_0,
    V_SNAP,
    HBAR,
    L_NODE,
    ALPHA,
)
from ave.axioms.scale_invariant import (
    impedance,
    reflection_coefficient,
)


# ═══════════════════════════════════════════════════════════════
# Detector configurations
# ═══════════════════════════════════════════════════════════════


@dataclass
class GWDetector:
    """
    Gravitational wave detector modeled as a Fabry-Pérot impedance cavity.

    In the AVE framework, a GW detector is a resonant section of the
    LC vacuum where:
      - Arm length L defines the cavity length
      - N_bounces (finesse) determines the effective length L_eff = L × N
      - Laser power P provides the readout photon flux
      - The GW strain h modulates the cavity impedance
    """

    name: str
    arm_length_m: float  # Physical arm length [m]
    n_bounces: int  # Number of light bounces (finesse)
    laser_power_w: float  # Circulating laser power [W]
    laser_wavelength_m: float  # Laser wavelength [m]
    bandwidth_hz: float  # Detection bandwidth [Hz]

    @property
    def effective_length_m(self) -> float:
        """Effective cavity length = arm × bounces."""
        return self.arm_length_m * self.n_bounces

    @property
    def laser_frequency_hz(self) -> float:
        """Laser frequency [Hz]."""
        return C_0 / self.laser_wavelength_m

    @property
    def photon_energy_j(self) -> float:
        """Energy per photon [J]."""
        return HBAR * 2 * np.pi * self.laser_frequency_hz

    @property
    def photon_flux(self) -> float:
        """Photons per second entering the cavity."""
        return self.laser_power_w / self.photon_energy_j


# ═══════════════════════════════════════════════════════════════
# Detector catalog
# ═══════════════════════════════════════════════════════════════

DETECTOR_CATALOG = {
    "LIGO": GWDetector(
        name="LIGO",
        arm_length_m=4000,  # 4 km arms
        n_bounces=280,  # Finesse ≈ 450 → ~280 bounces
        laser_power_w=750e3,  # 750 kW circulating
        laser_wavelength_m=1064e-9,  # Nd:YAG
        bandwidth_hz=100,  # ~100 Hz optimal band
    ),
    "LISA": GWDetector(
        name="LISA",
        arm_length_m=2.5e9,  # 2.5 million km
        n_bounces=1,  # No cavity, single pass
        laser_power_w=2.0,  # 2 W
        laser_wavelength_m=1064e-9,
        bandwidth_hz=1e-3,  # mHz band
    ),
    "Einstein_Telescope": GWDetector(
        name="Einstein Telescope",
        arm_length_m=10000,  # 10 km arms
        n_bounces=560,  # Higher finesse
        laser_power_w=3e6,  # 3 MW circulating
        laser_wavelength_m=1064e-9,
        bandwidth_hz=10,  # Lower frequency target
    ),
}


# ═══════════════════════════════════════════════════════════════
# Detection physics
# ═══════════════════════════════════════════════════════════════


def impedance_modulation(h: float, Z0: float = Z_0) -> float:
    r"""
    Impedance perturbation caused by GW strain.

    A passing gravitational wave modulates the local vacuum impedance:

    .. math::
        \delta Z = Z_0 \cdot h

    This is the fundamental detection mechanism. The GW doesn't
    "stretch space" — it perturbs the LC lattice impedance, which
    changes the phase velocity of light in the detector arm.

    Args:
        h: GW strain amplitude (dimensionless).
        Z0: Background vacuum impedance [Ω].

    Returns:
        Impedance perturbation [Ω].
    """
    return Z0 * h


def phase_shift(h: float, detector: GWDetector, gw_freq_hz: float = 100.0) -> float:
    r"""
    Phase shift accumulated by laser in a Fabry-Pérot arm.

    .. math::
        \Delta\phi = \frac{2\pi f_{GW}}{c} \cdot L_{eff} \cdot h

    This is the measurable signal. LIGO detects phase shifts
    of ~10⁻¹² rad.

    Args:
        h: GW strain amplitude.
        detector: Detector model.
        gw_freq_hz: GW frequency [Hz].

    Returns:
        Phase shift [radians].
    """
    omega_gw = 2 * np.pi * gw_freq_hz
    L_eff = detector.effective_length_m
    return omega_gw * L_eff * h / C_0


def shot_noise_strain(detector: GWDetector, gw_freq_hz: float = 100.0) -> float:
    r"""
    Shot-noise-limited strain sensitivity.

    .. math::
        h_{shot} = \frac{1}{L_{eff}} \cdot
        \sqrt{\frac{\hbar c \lambda}{2\pi P}}
        \cdot \frac{1}{\sqrt{\Delta f}}

    This gives the minimum detectable strain per √Hz.
    For LIGO: h_shot ≈ 10⁻²³ /√Hz at 100 Hz.

    Args:
        detector: Detector model.
        gw_freq_hz: GW frequency [Hz].

    Returns:
        Strain sensitivity [1/√Hz].
    """
    L_eff = detector.effective_length_m
    lam = detector.laser_wavelength_m
    P = detector.laser_power_w

    # Phase noise from shot noise: δφ = 1/√N_photons
    # N_photons per measurement = P × τ / (ℏω)
    # τ = 1/(2π f_gw)
    h_shot = (1.0 / L_eff) * np.sqrt(HBAR * C_0 * lam / (2 * np.pi * P))
    return h_shot


def radiation_pressure_strain(detector: GWDetector, gw_freq_hz: float = 100.0, mirror_mass_kg: float = 40.0) -> float:
    r"""
    Radiation pressure noise strain.

    At low frequencies, photon momentum fluctuations push the
    mirrors, creating noise. The strain equivalent is:

    .. math::
        h_{RP} = \frac{1}{m L \omega^2} \cdot
        \sqrt{\frac{2 \hbar \omega_{laser} P}{c^2}}

    Args:
        detector: Detector model.
        gw_freq_hz: GW frequency [Hz].
        mirror_mass_kg: Test mass [kg].

    Returns:
        Radiation pressure strain [1/√Hz].
    """
    omega_gw = 2 * np.pi * gw_freq_hz
    omega_laser = 2 * np.pi * detector.laser_frequency_hz
    P = detector.laser_power_w
    L = detector.arm_length_m
    m = mirror_mass_kg

    h_rp = (1.0 / (m * L * omega_gw**2)) * np.sqrt(2 * HBAR * omega_laser * P / C_0**2)
    return h_rp


def total_strain_sensitivity(detector: GWDetector, freq_hz: np.ndarray, mirror_mass_kg: float = 40.0) -> np.ndarray:
    r"""
    Total strain sensitivity curve (shot + radiation pressure).

    The Standard Quantum Limit (SQL) is the geometric mean of
    shot noise and radiation pressure noise:

    .. math::
        h_{SQL} = \sqrt{h_{shot}^2 + h_{RP}^2}

    Args:
        detector: Detector model.
        freq_hz: Array of frequencies [Hz].
        mirror_mass_kg: Test mass [kg].

    Returns:
        Array of strain sensitivities [1/√Hz].
    """
    h_s = np.array([shot_noise_strain(detector, f) for f in freq_hz])
    h_r = np.array([radiation_pressure_strain(detector, f, mirror_mass_kg) for f in freq_hz])
    return np.sqrt(h_s**2 + h_r**2)


def gw_power_absorbed(h: float, gw_freq_hz: float, source_distance_m: float) -> float:
    r"""
    Power carried by a GW through a cross-section.

    .. math::
        P_{GW} = \frac{c^3}{16\pi G} \cdot h^2 \cdot \omega^2 \cdot A

    In AVE terms, this is the Poynting flux of the inductive shear wave.

    Args:
        h: Strain amplitude.
        gw_freq_hz: Frequency [Hz].
        source_distance_m: Distance to source [m].

    Returns:
        Power flux [W/m²].
    """
    from ave.core.constants import G

    omega = 2 * np.pi * gw_freq_hz
    return (C_0**3 / (16 * np.pi * G)) * h**2 * omega**2


def lattice_voltage_ratio(h: float, gw_freq_hz: float = 100.0) -> float:
    r"""
    Ratio V_GW / V_SNAP — measures how far below saturation the GW is.

    This is the key AVE prediction: GW detection operates in the
    PERFECTLY LINEAR regime. The ratio is astronomically small.

    Args:
        h: Strain amplitude.
        gw_freq_hz: Frequency [Hz].

    Returns:
        V_GW / V_SNAP (dimensionless, << 1 for all physical GW).
    """
    from ave.gravity.gw_propagation import gw_strain_to_voltage

    V_gw = gw_strain_to_voltage(h, gw_freq_hz)
    return V_gw / V_SNAP


def detector_summary(detector_name: str = "LIGO", h: float = 1e-21) -> dict:
    """
    Generate a summary of detector properties and sensitivity.

    Args:
        detector_name: Key from DETECTOR_CATALOG.
        h: Reference strain.

    Returns:
        Dict with computed properties.
    """
    det = DETECTOR_CATALOG[detector_name]
    freq = np.logspace(0.5, 3.5, 200)
    sens = total_strain_sensitivity(det, freq)

    return {
        "name": det.name,
        "arm_length_m": det.arm_length_m,
        "effective_length_m": det.effective_length_m,
        "n_bounces": det.n_bounces,
        "laser_power_w": det.laser_power_w,
        "photon_flux": det.photon_flux,
        "phase_shift_rad": phase_shift(h, det),
        "impedance_modulation_ohm": impedance_modulation(h),
        "lattice_voltage_ratio": lattice_voltage_ratio(h),
        "shot_noise_100hz": shot_noise_strain(det, 100.0),
        "freq_hz": freq,
        "sensitivity_curve": sens,
    }
