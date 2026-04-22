"""
1D Finite-Difference Time-Domain (FDTD) solver for the AVE LC Network Metric.
Strictly replaces continuous structural CFD solvers with discrete Electrodynamic solvers.
"""

import numpy as np

from ave.axioms.scale_invariant import impedance
from ave.core.constants import C_0, EPSILON_0, MU_0
from ave.regime_3_saturated.orbital_impedance import calculate_refractive_strain


class FDTDLattice1D:
    def __init__(self, size: int, grid_resolution: float, mass_center_kg: float = 0.0):
        """
        Initializes a 1D discrete LC network transmission line representing the macroscopic vacuum.

        Args:
            size (int): Number of nodes in the simulated 1D lattice.
            grid_resolution (float): Physical spacing between discrete nodes (dz).
            mass_center_kg (float): Mass located at the center pulling the metric.
        """
        self.size = size
        self.dz = grid_resolution

        # Courant limit for stability (dt <= dz / c)
        self.dt = self.dz / (2.0 * C_0)

        # Grid allocations: Electric Field (E), Magnetic Field (H)
        self.E = np.zeros(size)
        self.H = np.zeros(size - 1)

        # Spatially varying macroscopic grid parameters L(z) and C(z)
        self.u_local = np.ones(size - 1) * MU_0
        self.e_local = np.ones(size) * EPSILON_0
        self.n_refractive = np.ones(size)

        self._apply_gravitational_metric(mass_center_kg)

        # Precompute update coefficients
        self.ce = self.dt / (self.dz * self.e_local)

        # H field is staggered, average the adjacent n(r) or define uniquely
        u_centers = self.u_local
        self.ch = self.dt / (self.dz * u_centers)

    def _apply_gravitational_metric(self, mass_kg: float) -> None:
        """
        Applies topological gravity (vectorized).
        Calculates localized optical strain n_r based on mass distance from center.
        Achromatic Impedance Matching explicitly scales BOTH u and e symmetrically!
        """
        if mass_kg <= 0.0:
            return

        center_idx = self.size // 2

        # Vectorized E-field nodes (integer positions)
        k_e = np.arange(self.size)
        radius_e = np.abs(k_e - center_idx) * self.dz
        valid_e = radius_e > 0.001  # Avoid singularity at center
        if np.any(valid_e):
            n_r_e = np.array([calculate_refractive_strain(mass_kg, r) for r in radius_e[valid_e]])
            self.e_local[valid_e] = EPSILON_0 * n_r_e
            self.n_refractive[valid_e] = n_r_e

        # Vectorized H-field nodes (half-integer positions)
        k_h = np.arange(self.size - 1)
        radius_h = np.abs((k_h + 0.5) - center_idx) * self.dz
        valid_h = radius_h > 0.001
        if np.any(valid_h):
            n_r_h = np.array([calculate_refractive_strain(mass_kg, r) for r in radius_h[valid_h]])
            self.u_local[valid_h] = MU_0 * n_r_h

    def get_local_impedance(self, k: int) -> float:
        """Returns the local transverse impedance at node k."""
        u_eff = self.u_local[min(k, self.size - 2)]
        e_eff = self.e_local[k]
        return impedance(u_eff / MU_0, e_eff / EPSILON_0)

    def step(self, source_node: int, t_steps: int) -> None:
        """
        Advances the FDTD simulation by injecting a continuous sine wave at the source node.
        """
        omega = 2.0 * np.pi * (C_0 / (50.0 * self.dz))

        for t in range(t_steps):
            # Update H field (Magnetic)
            self.H[:] += self.ch[:] * (self.E[1:] - self.E[:-1])

            # Simple absorbing boundary conditions (ABC) for E field edges
            self.E[0] = self.E[1]
            self.E[-1] = self.E[-2]

            # Update E field (Electric) internal nodes
            self.E[1:-1] += self.ce[1:-1] * (self.H[1:] - self.H[:-1])

            # Hard source injection
            self.E[source_node] = np.sin(omega * t * self.dt)
