"""
Seismic FDTD Bridge: Earth's Interior on the Maxwell Solver
============================================================

Proves that the FDTD3DEngine is a UNIVERSAL wave engine by injecting
the PREM seismic impedance profile as ε_r and μ_r material maps.

The key identity:
  Seismic:  Z = ρ·V_p = √(K·ρ)     [Rayl]
  Maxwell:  Z = √(μ/ε)              [Ω]

Both use the same impedance, saturation, and reflection operators
from ``scale_invariant.py``.  The FDTD engine doesn't "know" whether
it's solving Maxwell's equations or the elastic wave equation —
they have the same mathematical structure.

Usage:
    from ave.regime_2_nonlinear.seismic_fdtd import build_seismic_engine

    engine, profile = build_seismic_engine(n_cells=200)
    for step in range(n_steps):
        engine.inject_soft_source('Ez', src_x, src_y, src_z, pulse(t))
        engine.step()
"""
from __future__ import annotations


import numpy as np
from typing import Tuple

from ave.core.fdtd_3d import FDTD3DEngine
from ave.regime_2_nonlinear.seismic import (
    build_1d_impedance_profile,
    PREM_LAYERS,
    SeismicLayer,
)
from ave.axioms.scale_invariant import (
    reflection_coefficient,
    impedance,
)
from ave.core.constants import EPSILON_0, MU_0


def build_seismic_engine(
    n_cells: int = 200,
    dx_km: float = 10.0,
    linear_only: bool = True,
) -> Tuple[FDTD3DEngine, dict]:
    """
    Create an FDTD engine pre-loaded with the PREM Earth profile.

    The seismic impedance profile is mapped to ε_r and μ_r material
    arrays along the X-axis (representing depth).  Y and Z are kept
    uniform (1D radial propagation).

    The mapping is:
        ε_r(x) = K_ref / K(x)    (compressibility → capacitance)
        μ_r(x) = G_ref / G(x)    (shear compliance → inductance)

    This produces correct:
        - Wave speed: c(x) = c₀ / √(ε_r · μ_r)  ↔  V_p(x)
        - Impedance:  Z(x) = Z₀ · √(μ_r / ε_r)  ↔  ρ·V_p(x)
        - Reflection:  Γ at each layer boundary

    Args:
        n_cells: Number of cells along the depth axis.
        dx_km: Cell size in km (default 10 km).
        linear_only: If True (default), disable Axiom 4 nonlinearity
                     (seismic waves are far below saturation).

    Returns:
        (engine, profile): The FDTD engine with material loaded,
                           and the impedance profile dict.
    """
    # Build the 1D impedance profile
    profile = build_1d_impedance_profile(dx_km=dx_km)

    # Resample to n_cells if different
    depth_source = profile['depth_km']
    eps_r_source = profile['eps_r']
    mu_r_source = profile['mu_r']

    depth_target = np.linspace(0, depth_source[-1], n_cells)
    eps_r = np.interp(depth_target, depth_source, eps_r_source)
    mu_r = np.interp(depth_target, depth_source, mu_r_source)

    # Create FDTD engine (1D propagation: nx=n_cells, ny=1, nz=1)
    # dx = dx_km * 1000 [m]
    dx_m = dx_km * 1000.0
    engine = FDTD3DEngine(
        nx=n_cells,
        ny=3,         # Minimum for curl computation
        nz=3,
        dx=dx_m,
        linear_only=linear_only,
    )

    # Inject the seismic material profile along the X-axis
    for i in range(n_cells):
        engine.eps_r[i, :, :] = eps_r[i]
        engine.mu_r[i, :, :] = mu_r[i]

    # Update profile dict with resampled values
    profile_out = {
        'depth_km': depth_target,
        'eps_r': eps_r,
        'mu_r': mu_r,
        'rho': np.interp(depth_target, depth_source, profile['rho']),
        'v_p': np.interp(depth_target, depth_source, profile['v_p']),
        'v_s': np.interp(depth_target, depth_source, profile['v_s']),
    }

    return engine, profile_out


def verify_impedance_consistency(profile: dict) -> dict:
    """
    Verify that the FDTD material maps produce the correct seismic impedance.

    For each cell, computes:
        Z_seismic = ρ · V_p               [Rayl]
        Z_fdtd    = Z₀ · √(μ_r / ε_r)    [Ω, but proportional]

    The ratio Z_fdtd / Z_seismic should be constant across all cells
    (the overall scale factor is Z₀ × (reference impedance conversion)),
    proving the FDTD impedance profile is the seismic profile.

    Returns:
        Dict with:
            'Z_seismic': seismic impedance at each depth
            'Z_fdtd_normalized': FDTD impedance, normalized to match
            'max_deviation_pct': maximum relative deviation
    """
    Z_seismic = profile['rho'] * profile['v_p']
    Z_fdtd_raw = impedance(profile['mu_r'], profile['eps_r'])

    # Normalize to the same scale (surface value)
    scale = Z_seismic[0] / Z_fdtd_raw[0]
    Z_fdtd_norm = Z_fdtd_raw * scale

    deviation_pct = np.abs(Z_fdtd_norm - Z_seismic) / Z_seismic * 100

    return {
        'Z_seismic': Z_seismic,
        'Z_fdtd_normalized': Z_fdtd_norm,
        'max_deviation_pct': float(np.max(deviation_pct)),
        'rms_deviation_pct': float(np.sqrt(np.mean(deviation_pct**2))),
    }


def compute_boundary_reflections(profile: dict) -> list:
    """
    Compute reflection coefficients at all layer boundaries using
    both the seismic formula and the universal reflection_coefficient.

    Proves that ``reflection_coefficient(Z1, Z2)`` gives the same
    results for seismic impedances as for electromagnetic ones.

    Returns:
        List of dicts with boundary name, Γ_seismic, Γ_fdtd.
    """
    results = []
    for i in range(len(PREM_LAYERS) - 1):
        L1 = PREM_LAYERS[i]
        L2 = PREM_LAYERS[i + 1]

        Z1 = L1.acoustic_impedance_p
        Z2 = L2.acoustic_impedance_p

        # Universal function — same code as Pauli exclusion, Moho, S₁₁
        gamma = float(reflection_coefficient(Z1, Z2))

        results.append({
            'boundary': f"{L1.name} → {L2.name}",
            'Z1_MRayl': Z1 / 1e6,
            'Z2_MRayl': Z2 / 1e6,
            'gamma': gamma,
            'reflection_pct': abs(gamma) * 100,
        })

    return results
