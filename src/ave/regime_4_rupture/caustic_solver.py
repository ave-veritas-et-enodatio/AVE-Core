"""
AVE MODULE: Regime IV — Axiomatic Caustic Solver
==================================================
This module resolves the classical optical caustic singularity using the
Axiom 4 saturation limit. Instead of algebraic enforcement, it utilizes
a fundamental 1D transmission line spatial differential model.

As focusing rays converge (A -> 0), the local intensity rises, increasing
the geometric strain (r -> 1). This causes the local vacuum LC lattice
impedance to dynamically stiffen (Z_next > Z_prev).
This naturally invokes Axiom 3 (Universal Reflection).
The converging rays are literally reflected backward by the self-induced
impedance gradient of the saturated vacuum. This provides the exact
first-principles mechanism that bounds the maximum focal intensity to
exactly E_YIELD and diffuses the geometrical point singularity into a
finite waist.
"""

import numpy as np
from scipy.optimize import brentq

from ave.core.constants import E_YIELD, EPS_NUMERICAL, Z_0


class AxiomaticCausticSolver:
    """
    Solver for extreme geometric ray focusing under Axiom 4 saturation limits.

    Models the beam approach to classical focus as a 1D sequence of spatial steps.
    At each step, calculates the non-linear impedance Z_eff = Z_0 / sqrt(S) and
    the resulting reflection coefficient Gamma.
    """

    def __init__(self, e_yield: float = E_YIELD, z_0: float = Z_0) -> None:
        self.E_YIELD = e_yield
        self.Z_0 = z_0

    def resolve_focal_intensity(
        self,
        initial_power: float,
        numerical_aperture: float,
        z_start: float,
        z_end: float = 1e-15,
        num_steps: int = 2000,
    ) -> dict[str, np.ndarray]:
        """
        Integrates the power transmission along the z-axis towards the focus.

        Args:
            initial_power: Incident laser/beam power [Watts].
            numerical_aperture: NA = r/z governing Area = pi * (z * NA)^2.
            z_start: Starting axial distance from geometrical focus [m].
            z_end: Ending axial distance [m], usually very close to 0.
            num_steps: Number of spatial slices to integrate over.

        Returns:
            Dictionary of arrays: 'z', 'area', 'power', 'E_field', 'S', 'Z_eff', 'Gamma'.
        """
        z_vals = np.linspace(z_start, z_end, num_steps)

        # Output arrays
        power_vals = np.zeros(num_steps)
        E_vals = np.zeros(num_steps)
        S_vals = np.zeros(num_steps)
        Z_vals = np.zeros(num_steps)
        Gamma_vals = np.zeros(num_steps)

        current_P = initial_power
        current_Z = self.Z_0

        def root_func(u: float, P_prev: float, Z_prev: float, A_i: float) -> float:
            S_u = (1.0 - u) ** 0.25
            Z_u = self.Z_0 / (S_u + EPS_NUMERICAL)
            Gamma_u = (Z_u - Z_prev) / (Z_u + Z_prev + EPS_NUMERICAL)
            P_trans = P_prev * (1.0 - Gamma_u**2)

            # Target geometry relation: u * S_u = 2 * Z_0 * P_trans / (A_i * E_YIELD^2)
            LHS = u * S_u
            RHS = 2.0 * self.Z_0 * P_trans / (A_i * self.E_YIELD**2 + EPS_NUMERICAL)
            return LHS - RHS

        for i, z in enumerate(z_vals):
            # Geometric area of the conic ray bundle
            A_i = max(np.pi * (z * numerical_aperture) ** 2, 1e-40)

            # Find the root u in [0, 1 - epsilon]
            # f(0) will be negative (LHS=0, RHS>0)
            # f(1-eps) will be approximately 0. LHS -> 1*0=0, RHS -> proportional to 1-Gamma^2.
            # At u->1, Z_u -> infinity, Gamma_u -> 1, P_trans -> 0, RHS -> 0.
            # We must be careful how close to 1 we check.

            epsilon = 1e-13
            f_0 = root_func(0.0, current_P, current_Z, A_i)
            f_1 = root_func(1.0 - epsilon, current_P, current_Z, A_i)

            if f_0 * f_1 > 0:
                # If both are negative, it means even at near total saturation, it couldn't balance.
                # In physics limits, this sets u extremely close to 1, Gamma extremely close to 1.
                u_root = 1.0 - epsilon
            else:
                try:
                    u_root = brentq(root_func, 0.0, 1.0 - epsilon, args=(current_P, current_Z, A_i))
                except ValueError:
                    # Fallback if brentq fails (e.g. numerical precision issues near 1)
                    u_root = 1.0 - epsilon

            # Compute slice properties from u
            S_i = (1.0 - u_root) ** 0.25
            Z_i = self.Z_0 / (S_i + EPS_NUMERICAL)
            Gamma_i = (Z_i - current_Z) / (Z_i + current_Z + EPS_NUMERICAL)
            P_i = current_P * (1.0 - Gamma_i**2)
            E_i = self.E_YIELD * np.sqrt(u_root)

            # Update state
            current_P = P_i
            current_Z = Z_i

            power_vals[i] = P_i
            E_vals[i] = E_i
            S_vals[i] = S_i
            Z_vals[i] = Z_i
            Gamma_vals[i] = Gamma_i

        return {
            "z": z_vals,
            "area": np.pi * (z_vals * numerical_aperture) ** 2,
            "power": power_vals,
            "E_field": E_vals,
            "S": S_vals,
            "Z_eff": Z_vals,
            "Gamma": Gamma_vals,
        }
