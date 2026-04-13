"""
AVE Geophysics: Seismic Wave Propagation as Impedance Matching
==============================================================

The Earth's interior is a series of concentric impedance shells.  Seismic
waves are mechanical modes of the same LC lattice at macroscopic scale.

Key AVE reinterpretations:
  - P-waves: longitudinal compression (capacitive sector)
  - S-waves: transverse shear (inductive sector)
  - Moho discontinuity: impedance mismatch → partial reflection
  - Inner/outer core boundary: liquid = zero shear modulus = μ_r → 0
  - Shadow zone: total internal refraction at core-mantle impedance step

Material properties from PREM (Preliminary Reference Earth Model):
  Layer         ρ (kg/m³)   V_p (km/s)   V_s (km/s)   Z_p (MRayl)
  ─────────────────────────────────────────────────────────────────
  Upper crust    2600        5.8          3.2          15.1
  Lower crust    2900        6.5          3.6          18.9
  Upper mantle   3300        8.1          4.5          26.7
  Lower mantle   5500       13.7          7.3          75.4
  Outer core     9900        8.1          0.0          80.2
  Inner core    13000       11.3          3.6         146.9

In AVE terms:
  Z_acoustic = ρ · V = √(K · ρ)  where K = bulk modulus
  ε_r ∝ 1/K  (compressibility = capacitance)
  μ_r ∝ 1/G  (shear compliance = inductance)

The Moho produces a reflection coefficient:
  Γ = (Z₂ - Z₁) / (Z₂ + Z₁) = (26.7 - 18.9) / (26.7 + 18.9) ≈ 0.17
  → 17% amplitude reflection at crust-mantle boundary.
"""
from __future__ import annotations


import numpy as np
from dataclasses import dataclass, field
from typing import List

from ave.axioms.scale_invariant import (
    reflection_coefficient as _universal_gamma,
)


@dataclass
class SeismicLayer:
    """A single layer of the Earth's interior."""
    name: str
    depth_top_km: float    # Top of layer [km]
    depth_bot_km: float    # Bottom of layer [km]
    rho: float             # Density [kg/m³]
    v_p: float             # P-wave velocity [m/s]
    v_s: float             # S-wave velocity [m/s]

    @property
    def thickness_km(self) -> float:
        """Layer thickness in km (depth_bot - depth_top)."""
        return self.depth_bot_km - self.depth_top_km

    @property
    def bulk_modulus(self) -> float:
        """K = ρ(V_p² - 4/3 V_s²)  [Pa]"""
        return self.rho * (self.v_p**2 - (4.0 / 3.0) * self.v_s**2)

    @property
    def shear_modulus(self) -> float:
        """G = ρ V_s²  [Pa]"""
        return self.rho * self.v_s**2

    @property
    def acoustic_impedance_p(self) -> float:
        """Z_p = ρ · V_p  [Pa·s/m = Rayl]"""
        return self.rho * self.v_p

    @property
    def acoustic_impedance_s(self) -> float:
        """Z_s = ρ · V_s  [Pa·s/m = Rayl]"""
        return self.rho * self.v_s

    @property
    def eps_r_ave(self) -> float:
        """
        AVE-equivalent relative permittivity.
        ε_r = K_ref / K  (soft material → high ε_r → slow P-waves)
        Normalized to upper crust K as reference.
        """
        K_ref = 2600 * (5800**2 - (4/3) * 3200**2)  # Upper crust K
        K = self.bulk_modulus
        if K <= 0:
            return 1e6  # Liquid: infinite compressibility
        return K_ref / K

    @property
    def mu_r_ave(self) -> float:
        """
        AVE-equivalent relative permeability.
        μ_r = G_ref / G  (liquid = zero shear = μ_r → ∞)
        Normalized to upper crust G as reference.
        """
        G_ref = 2600 * 3200**2  # Upper crust G
        G = self.shear_modulus
        if G <= 0:
            return 1e6  # Liquid: no shear → infinite "inductance"
        return G_ref / G


# ============================================================
# Standard Earth Model (PREM-based)
# ============================================================

PREM_LAYERS: List[SeismicLayer] = [
    SeismicLayer("Upper Crust",   0,    15,  2600,  5800,  3200),
    SeismicLayer("Lower Crust",  15,    35,  2900,  6500,  3600),
    SeismicLayer("Upper Mantle",  35,   410,  3300,  8100,  4500),
    SeismicLayer("Transition Z", 410,   660,  3800, 10300,  5600),
    SeismicLayer("Lower Mantle", 660,  2891,  5500, 13700,  7300),
    SeismicLayer("Outer Core",  2891,  5150,  9900,  8100,     0),
    SeismicLayer("Inner Core",  5150,  6371, 13000, 11300,  3600),
]


def reflection_coefficient(layer1: SeismicLayer, layer2: SeismicLayer,
                           wave_type: str = 'p') -> float:
    """
    Compute the amplitude reflection coefficient at a boundary.

    Γ = (Z₂ - Z₁) / (Z₂ + Z₁)

    Delegates to ``ave.axioms.scale_invariant.reflection_coefficient`` —
    the same operator that computes Pauli exclusion, antenna S₁₁, and
    every other impedance boundary in the framework.

    Args:
        layer1: Incident layer.
        layer2: Transmitted layer.
        wave_type: 'p' for P-waves, 's' for S-waves.

    Returns:
        Reflection coefficient Γ ∈ [-1, 1].
    """
    if wave_type == 'p':
        Z1 = layer1.acoustic_impedance_p
        Z2 = layer2.acoustic_impedance_p
    else:
        Z1 = layer1.acoustic_impedance_s
        Z2 = layer2.acoustic_impedance_s

    return float(_universal_gamma(Z1, Z2))


def transmission_coefficient(layer1: SeismicLayer, layer2: SeismicLayer,
                             wave_type: str = 'p') -> float:
    """
    Compute the amplitude transmission coefficient at a boundary.

    T = 2Z₁ / (Z₁ + Z₂) = 1 + Γ

    Delegates to the universal reflection coefficient.

    Args:
        layer1: Incident layer.
        layer2: Transmitted layer.
        wave_type: 'p' for P-waves, 's' for S-waves.

    Returns:
        Transmission coefficient T.
    """
    gamma = reflection_coefficient(layer1, layer2, wave_type)
    return 1.0 + gamma


def travel_time(layers: List[SeismicLayer], wave_type: str = 'p') -> float:
    """
    Compute total vertical travel time through all layers.

    t = Σ (thickness / velocity) for each layer.

    Args:
        layers: List of SeismicLayer objects.
        wave_type: 'p' for P-waves, 's' for S-waves.

    Returns:
        Total travel time [seconds].
    """
    total = 0.0
    for layer in layers:
        thickness = layer.thickness_km * 1000.0  # km → m
        v = layer.v_p if wave_type == 'p' else layer.v_s
        if v > 0:
            total += thickness / v
    return total


def all_reflections(wave_type: str = 'p') -> dict:
    """
    Compute reflection coefficients at all PREM layer boundaries.

    Returns:
        Dict mapping boundary names to reflection coefficients.
    """
    results = {}
    for i in range(len(PREM_LAYERS) - 1):
        l1 = PREM_LAYERS[i]
        l2 = PREM_LAYERS[i + 1]
        name = f"{l1.name} → {l2.name}"
        gamma = reflection_coefficient(l1, l2, wave_type)
        results[name] = gamma
    return results


def build_1d_impedance_profile(dx_km: float = 10.0) -> dict:
    """
    Build a 1D radial impedance profile of the Earth for FDTD injection.

    Returns a dict with:
        'depth_km': array of depths
        'rho': density at each depth
        'v_p': P-wave velocity
        'v_s': S-wave velocity
        'eps_r': AVE equivalent relative permittivity
        'mu_r': AVE equivalent relative permeability
    """
    max_depth = 6371.0
    n_cells = int(max_depth / dx_km)
    depths = np.linspace(0, max_depth, n_cells)

    rho = np.zeros(n_cells)
    v_p = np.zeros(n_cells)
    v_s = np.zeros(n_cells)
    eps_r = np.ones(n_cells)
    mu_r = np.ones(n_cells)

    for i, d in enumerate(depths):
        for layer in PREM_LAYERS:
            if layer.depth_top_km <= d < layer.depth_bot_km:
                rho[i] = layer.rho
                v_p[i] = layer.v_p
                v_s[i] = layer.v_s
                eps_r[i] = layer.eps_r_ave
                mu_r[i] = layer.mu_r_ave
                break
        else:
            # Beyond deepest layer (inner core)
            last = PREM_LAYERS[-1]
            rho[i] = last.rho
            v_p[i] = last.v_p
            v_s[i] = last.v_s
            eps_r[i] = last.eps_r_ave
            mu_r[i] = last.mu_r_ave

    return {
        'depth_km': depths,
        'rho': rho,
        'v_p': v_p,
        'v_s': v_s,
        'eps_r': eps_r,
        'mu_r': mu_r,
    }
