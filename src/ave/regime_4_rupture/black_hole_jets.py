"""
AVE MODULE: Regime IV — Black Hole Jets
=======================================
Implements the topological shear mechanics at the Event Horizon boundary.
At the boundary where r = 1.0 (Schwarzschild saturation radius), infalling
transverse wave energy cannot penetrate the ruptured interior. The energy
is geometrically redirected along the un-ruptured polar axes, resulting in
the emission of extreme relativistic jets.
"""

from __future__ import annotations

import numpy as np

from ave.gravity import principal_radial_strain
from ave.regime_4_rupture.rupture_solver import TopologicalRuptureSolver


def compute_jet_emission_power(M_kg: float, r_infall: np.ndarray, incident_power: np.ndarray) -> np.ndarray:
    """
    Computes the fraction of incident spherical infall power that is geometrically
    redirected into polar jets due to equatorial lattice rupture (Event Horizon).

    Args:
        M_kg: Mass of the central body.
        r_infall: Array of radial distances.
        incident_power: Incident energy flux at radius r.

    Returns:
        Array of emitted jet power.
    """
    # Calculate dimensional strain (Axiom 4 limit)
    strain = np.array([principal_radial_strain(M_kg, r) for r in r_infall])
    rupture_state = TopologicalRuptureSolver.evaluate_rupture_state(strain)

    # Power transmission into the interior is strictly bounded by lattice compliance S(r)
    S = rupture_state["S"]

    # Energy that CANNOT be transmitted (1 - S) is radially sheared outward along the poles
    jet_power = incident_power * (1.0 - S)
    return jet_power
