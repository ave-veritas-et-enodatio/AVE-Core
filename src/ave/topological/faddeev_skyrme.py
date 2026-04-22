"""
Faddeev-Skyrme Hamiltonian Solver for the AVE Topological Network.
Solves for the 1D scalar rest-mass minimum of the structural metric defect.

NOTE: The energy functional used here is the 1D radial projection of the
full 3D hedgehog Hamiltonian. The angular σ-model terms (sin²f, sin⁴f/r²)
are deliberately excluded because the AVE architecture handles the 3D tensor
contribution separately via the Borromean eigenvalue equation in tensors.py.

CRITICAL: The 1D functional is scale-free — it has no natural energy
minimum at finite radius. Without a confinement bound, the soliton
spreads indefinitely (r_opt → ∞, I → 580). The physical confinement
is set by the topological crossing number of the soliton's winding.

THE TORUS KNOT LADDER (Phase Winding Classification):
  The electron's topology is an unknot (0₁), but its phase winding
  number follows the (2,3) pattern with c₃ = 3 crossings.
  The proton's phase winding is a (2,5) cinquefoil torus knot with
  c₅ = 5 crossings.  The (2,q) torus knots require odd q; there is
  no stable (2,4) configuration (the figure-eight is not a torus knot).

  The crossing number sets the confinement radius because each crossing
  constrains the phase gradient ∂ᵣφ by absorbing a fraction of the total
  coupling. The soliton's radial extent is therefore:

      r_opt = κ_FS / c₅ = κ_FS / 5

  This divides the total Faddeev-Skyrme coupling by the number of
  topological crossings through which the phase must wind.

  CROSS-SCALE CONNECTION (confinement ↔ atomic void floor):
    At nuclear scale (Regime I, S→0): the crossing number confines
    the soliton radius via r_opt = κ/c.  The SAME lattice packing
    fraction φ = π√2/6 (FCC, K=2G) bounds the saturated zone geometry.

    At atomic scale (Regime II, S≈1): the junction crossing count c
    drains phase space via Op10.  The void fraction (1-φ ≈ 0.26)
    bounds the drain: IE ≥ E_base × (1-φ).

    Both scales: crossing count partitions the available resource.
    The FCC packing fraction φ governs both.
"""

from __future__ import annotations


import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

# NOTE: Cannot import EPS_NUMERICAL from ave.core.constants here because
# constants.py calls _compute_i_scalar_dynamic() → TopologicalHamiltonian1D
# during module initialization, creating a circular import.  Use the
# canonical value directly (kept in sync with constants.EPS_NUMERICAL).
_EPS_NUMERICAL = 1e-12

# Crossing number of the (2,5) cinquefoil torus knot.
# This is the next entry in the phase winding ladder after the electron's c=3.
# The (2,q) torus knot progression uses only odd q: 3, 5, 7, ...
CROSSING_NUMBER_CINQUEFOIL: int = 5


class TopologicalHamiltonian1D:
    def __init__(self, node_pitch: float, scaling_coupling: float = 1.0):
        """
        Initializes the 1D solver for the localized non-linear phase defect.

        Args:
            node_pitch (float): Fundamental structural spacing (Axiom 1).
            scaling_coupling (float): The generalized Faddeev coupling constant.

                ⚠ PRECONDITION: If the caller passes KAPPA_FS from
                src/ave/core/constants.py (the canonical proton-baryon
                coupling), the value is ALREADY thermally softened at
                import time:

                    KAPPA_FS = KAPPA_FS_COLD * (1 - DELTA_THERMAL)
                           = 8π * (1 - 1/(14π²))
                           ≈ 24.951       (constants.py:563–566)

                The thermal softening δ_th = 1/(14π²) is the proton
                core's thermal correction at its native ~10¹³ K regime.
                This solver does NOT re-apply the softening — the input
                κ is expected to be already-softened. If you're passing
                a different coupling (e.g. KAPPA_FS_COLD for a
                sensitivity check or T→0 limit), pass the intended
                value explicitly.

                See also: src/ave/core/constants.py `KAPPA_FS` definition
                (~line 566), LIVING_REFERENCE.md Rule D2, and
                docs/framing_and_presentation.md §D2 for the
                "preconditions applied before solver entry" pattern.
        """
        self.l_node = node_pitch
        self.kappa = scaling_coupling

    def _phase_profile(self, r: float, r_opt: float, n: float) -> float:
        """
        Standard 1D topological profile interpolating smoothly between:
        phi(0) = pi (inverted core phase)
        phi(inf) = 0 (relaxed unbroken vacuum)
        """
        if r == 0:
            return np.pi

        scaled_r = r / r_opt

        # Power-law bounded profile matching standard topological ansatz
        return np.pi / (1.0 + (scaled_r) ** n)

    def _energy_density_integrand(self, r: float, r_opt: float, n: float) -> float:
        """
        Evaluates the local energy density of the Faddeev-Skyrme functional
        at a specific radius r, including Axiom 4 gradient saturation.

        The lattice has a maximum resolvable phase gradient of π/ℓ_node
        (one full half-rotation per cell).  When the solver's continuous
        profile produces gradients approaching this limit, the saturation
        factor S(|dφ/dr| / (π/ℓ_node)) smoothly reduces the effective
        gradient — the same operator that governs FDTD field updates,
        plasma cutoff, and galactic rotation drag.

        Note: The true 3D tensor trace uses external geometric bounding
        from `tensors.py`.  Here we evaluate the 1D radial scalar.
        """
        # Central-difference derivative for improved accuracy
        dr = 1e-6
        phi1 = self._phase_profile(r, r_opt, n)
        phi2 = self._phase_profile(r + dr, r_opt, n)
        dphi_dr = (phi2 - phi1) / dr

        # Axiom 4: gradient saturation at the lattice Nyquist limit
        # The solver operates in natural units where r is measured in
        # units of ℓ_node (i.e. ℓ_node = 1).  The maximum resolvable
        # phase gradient is therefore π per unit length (one half-
        # rotation per cell).
        gradient_yield = np.pi  # π / ℓ_node = π / 1 in natural units
        from ave.core.universal_operators import universal_saturation

        S = universal_saturation(dphi_dr, gradient_yield)
        dphi_dr_eff = dphi_dr * S

        # Quadratic stiffness term (Standard Dirichlet tension)
        kinetic_term = 0.5 * (dphi_dr_eff**2)

        # Quartic stabilization term (Skyrme/Faddeev Tensor repulsion)
        # Prevents the defect from collapsing to a singularity
        # In 1D radial projection, sin²(phi)/r² dominates
        skyrme_term = 0.5 * (np.sin(phi1) ** 2) / (r**2 + _EPS_NUMERICAL)

        # Total density scaled spherically
        density = 4 * np.pi * (r**2) * (kinetic_term + (self.kappa**2) * skyrme_term * dphi_dr_eff**2)

        return density

    def solve_scalar_trace(self, crossing_number: int = CROSSING_NUMBER_CINQUEFOIL) -> float:
        """
        Minimizes the 1D topological Hamiltonian to find the absolute lowest
        energy stable profile of the fundamental defect.

        The confinement bound r_opt ≤ κ/c divides the total Faddeev-Skyrme
        coupling by the crossing number, partitioning the coupling equally
        among the topological crossings through which the phase must wind.

        Preconditions applied to self.kappa BEFORE entry (see __init__ docstring):
          - Thermal softening δ_th = 1/(14π²) ≈ 7.21×10⁻³ is applied in
            src/ave/core/constants.py:563–566 (KAPPA_FS = KAPPA_FS_COLD × (1 − DELTA_THERMAL)).
            This solver receives the already-softened κ and does not re-apply.
            For T→0 / cold-limit behavior, instantiate with scaling_coupling=KAPPA_FS_COLD.

        Args:
            crossing_number: The number of topological crossings for the
                (2,q) torus knot.  Default is 5 (proton cinquefoil).
                The torus knot ladder uses odd q: 5, 7, 9, 11, 13, ...

        Returns:
            float: The integrated energy eigenvalue in dimensionless mass units.
        """
        # Confinement bound from crossing number
        r_opt_max = self.kappa / crossing_number

        def objective(params):
            """Integrate the Faddeev-Skyrme energy density for a trial (r_opt, n) profile."""
            r_opt, n = params
            # Integrate the energy density from core out to 10 * r_opt
            integral, _ = quad(self._energy_density_integrand, 0.0, 10.0 * r_opt, args=(r_opt, n), limit=100)
            return integral

        # Initial guesses: optimal radius roughly 1.0, power profile n=2
        initial_guess = [1.0, 2.0]

        # Bound the radius by the confinement, n > 0
        bounds = [(0.1, r_opt_max), (1.0, 4.0)]

        result = minimize(objective, initial_guess, bounds=bounds, method="L-BFGS-B")

        # Return the minimized dimensionless energy scalar
        return result.fun
