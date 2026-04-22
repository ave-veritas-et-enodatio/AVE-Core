"""
Saturated Rayleigh-Plesset Cavitation Solver (Regime III/IV Transition)
========================================================================

Classical fluid dynamics relies on constant macroscopic properties (density,
compressibility). The AVE framework recognizes these as localized linearizations
of the underlying LC metric bounds (Regime I).

During sonoluminescence, a collapsing bubble cavity acts as a geometric
strain amplifier. As the shrinking boundary's velocity \\dot{R} approaches the
lattice metric speed c_0 (speed of sound), the mechanical strain r -> 1.0.

By Axiom 4, the topological yield operator S(A) = sqrt(1 - r^2) triggers a
divergence in the effective impedance: Z_eff = Z_0 / sqrt(S).

The fluid hits a "Topological Wall" identical to special relativistic
velocity bounds. The classical Rayleigh-Plesset equation is updated here
with the Axiomatic Topological mass/inertia divergence:
    rho_eff = rho_0 / sqrt(1 - (\\dot{R}/c_0)^2)

This guarantees the model halts without encountering physical singularities,
automatically predicting the sonoluminescent flash conditions.
"""

from dataclasses import dataclass
from typing import Any, Literal

import numpy as np
from scipy.integrate import solve_ivp

from ave.regime_1_linear.fluids_factory import FluidImpedanceFactory, MolecularFluid


@dataclass
class PayloadConfig:
    """Configures the gaseous interior of the cavitation topology."""

    gas_type: Literal["vapor", "argon", "xenon"]
    gamma_poly: float = 1.66  # Monatomic gas specific heat ratio
    ionization_potential_ev: float = 15.76  # Default Argon


class AxiomaticRayleighPlesset:
    """
    First-principles integrating environment for Regime III acoustic rupture.
    """

    def __init__(
        self,
        fluid: MolecularFluid,
        R0_m: float,
        acoustic_freq_hz: float,
        acoustic_amp_pa: float,
        payload: PayloadConfig,
        T_celsius: float = 20.0,
        P_ambient_pa: float = 101325.0,
    ):
        self.fluid = fluid
        self.factory = FluidImpedanceFactory(self.fluid)
        self.R0 = R0_m
        self.omega_ac = 2.0 * np.pi * acoustic_freq_hz
        self.P_amp = acoustic_amp_pa
        self.payload = payload

        self.T_c = T_celsius
        self.P_amb = P_ambient_pa

        # Derived axiomatic linear constraints (Phase 1 checks)
        self.rho_0 = self.factory.compute_density(self.T_c, self.P_amb)
        self.gamma_st = self.factory.compute_surface_tension(self.T_c)

        # VCA topological properties
        self.c_sound = 1480.0  # Approx baseline, could be derived from bulk modulus K
        self.P_vapor = 2339.0  # static water vapor pressure at 20C

        # Determine internal rest gas pressure:
        # P_g0 + P_vapor = P_ambient + 2*gamma/R0
        self.P_g0 = self.P_amb + (2.0 * self.gamma_st / self.R0) - self.P_vapor
        if self.payload.gas_type == "vapor":
            self.P_g0 = 0.0  # pure steam cavitation

    def _internal_pressure(self, R: float) -> float:
        """Pressure inside the cavity."""
        if self.payload.gas_type == "vapor":
            return self.P_vapor
        return self.P_g0 * (self.R0 / R) ** (3.0 * self.payload.gamma_poly) + self.P_vapor

    def _ode_system(self, t: float, y: np.ndarray) -> np.ndarray:
        """
        y = [R, U]
        Computes the saturated derivatives.
        """
        R, U = y

        # 1. Topological Strain tracking (Mach equivalent)
        M = U / self.c_sound
        # Prevent math overflow for runaway collapse
        M_safe = np.clip(M, -0.999999999, 0.999999999)

        # 2. Axiom 4: The topological yield bounding the mass inertia
        # S(r) = sqrt(1 - r^2)
        S = np.sqrt(1.0 - M_safe**2)
        # In relativistic dynamics, longitudinal inertia is gamma^3 * m0
        # Here, gamma = 1 / S. The fluid's resistance to acceleration diverges as S^3 -> 0.
        rho_eff = self.rho_0 / (S**3)

        # 3. Acoustic field
        P_ac = -self.P_amp * np.sin(self.omega_ac * t)

        # 4. Surface tension and radiation damping
        # dp_g/dt for acoustic radiation term
        if self.payload.gas_type == "vapor":
            dp_g_dt = 0.0
        else:
            poly_term = 3.0 * self.payload.gamma_poly * self.P_g0 * (self.R0 ** (3 * self.payload.gamma_poly))
            dp_g_dt = -poly_term * (R ** (-3.0 * self.payload.gamma_poly - 1.0)) * U

        # Acoustic radiation damping term: R/(rho * c) * dP/dt
        P_rad = (R / (self.rho_0 * self.c_sound)) * dp_g_dt

        P_in = self._internal_pressure(R)
        P_out = self.P_amb + P_ac

        # Effective driving pressure delta
        Delta_P = P_in - P_out - (2.0 * self.gamma_st / R) + P_rad

        # Keller-Miksis style modification using rho_eff
        # R * dU/dt + 1.5 * U^2 = Delta_P / rho_eff
        dU_dt = (Delta_P / rho_eff - 1.5 * U**2) / R

        return np.array([U, dU_dt])

    def solve_collapse(self, t_span: tuple[float, float], max_step: float = 1e-9) -> Any:
        """Integrates the topological bubble collapse over an acoustic cycle."""
        y0 = np.array([self.R0, 0.0])

        # Tracking minimum volume explicitly before topological bounce
        def bounce_event(t: float, y: np.ndarray) -> float:
            # Trigger when velocity flips from shrinking to expanding (bounce)
            return y[1]

        bounce_event.terminal = False
        bounce_event.direction = 1

        # Topological Wall: Stop the collapse exactly at the saturation metric limit
        def yield_event(t: float, y: np.ndarray) -> float:
            # M -> 1.0 (velocity approaches shear speed c_sound)
            return (self.c_sound * 0.995) - abs(y[1])

        yield_event.terminal = True

        sol = solve_ivp(
            self._ode_system,
            t_span,
            y0,
            method="Radau",
            max_step=max_step,
            events=[bounce_event, yield_event],
            rtol=1e-6,
            atol=1e-9,
        )
        return sol
