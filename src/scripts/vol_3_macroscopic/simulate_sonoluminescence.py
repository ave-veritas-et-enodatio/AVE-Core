#!/usr/bin/env python3
"""
Simulate Sonoluminescence Event: Pure Topological Yield
======================================================
This script drives an 18-kHz acoustic standing wave across a water microbubble,
simulating extreme cavitational collapse.

Outputs:
1. Bubble radius over time R(t).
2. The peak topological blackbody temperature resulting from macroscopic
   fluid momentum halting against the LC metric topological yield point.
"""


import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import K_B
from ave.regime_1_linear.fluids_factory import WaterMolecule
from ave.regime_3_saturated.cavitation_collapse import AxiomaticRayleighPlesset, PayloadConfig
from ave.viz import style
from ave_path_util import manuscript_path


def compute_flash_temperature(R_min: float, P_max: float, R_0: float, payload: PayloadConfig) -> float:
    """
    Derives the topological flash temperature at maximum collapse.

    Using the VCA scaling framework, the mechanical work locally stresses the
    bubble cavity volume. If a payload species is present, atomic ionization
    consumes a discrete band of that structural heat.
    """
    # Mechanical work stored in compressed volume
    # Ideal gas approximation mapping from the topological boundary limits:
    # W = P_max * V_min
    V_min = (4.0 / 3.0) * np.pi * R_min**3
    V_0 = (4.0 / 3.0) * np.pi * R_0**3

    # Approx moles using standard PV=nRT at the start (n_0)
    # n_0 = P_g0 * V_0 / (K_B * 293.15 * N_A) ... Wait, using direct K_B per molecule:
    # N_molecules = P_g0 * V_0 / (K_B * T_amb)
    P_amb = 101325.0
    N_molecules = P_amb * V_0 / (K_B * 293.15) if payload.gas_type != "vapor" else 1.0

    # Pure topological kinetic strain temperature: 3/2 N k_B T = E
    # Taking into account that the actual energy is dictated by the
    # fluid wall's yielding momentum hitting Z_eff -> infinity.
    # T_flash = P_max / (number_density * k_b)
    n_density = N_molecules / V_min
    if n_density > 0:
        T_flash = P_max / (n_density * K_B)
    else:
        T_flash = 0.0

    # Payload ionization limitation
    # If the temperature drives sufficient thermal energy to strip electrons,
    # it clamps. 1 eV ~ 11604 K.
    if payload.gas_type in ["argon", "xenon"]:
        T_ionization = payload.ionization_potential_ev * 11604.5
        if T_flash > T_ionization:
            T_flash = T_ionization  # Thermal reservoir yields to plasma strip

    # If it's a pure vapor bubble containing no true non-condensable noble gas,
    # it completely collapses or hits the pure topological water wall.
    # We allow the pure vapor to reach arbitrary strain limits since water
    # condensation is assumed instantaneously bypassed by acoustic matching.
    return T_flash


def run_simulation(payload_type: str = "argon") -> tuple:
    print(f"--- Simulating Sonoluminescence for payload: {payload_type} ---")

    if payload_type == "argon":
        payload = PayloadConfig(gas_type="argon", ionization_potential_ev=15.76)
    elif payload_type == "xenon":
        payload = PayloadConfig(gas_type="xenon", ionization_potential_ev=12.13)
    else:
        payload = PayloadConfig(gas_type="vapor")

    # Water at 20°C
    water = WaterMolecule()

    # Typical single-bubble sonoluminescence experimental params
    R0 = 4.0e-6  # 4 microns
    f_ac = 26.5e3  # 26.5 kHz
    P_amp = 1.35 * 101325  # 1.35 atm acoustic drive amplitude

    # Create the solver
    solver = AxiomaticRayleighPlesset(
        fluid=water,
        R0_m=R0,
        acoustic_freq_hz=f_ac,
        acoustic_amp_pa=P_amp,
        payload=payload,
        T_celsius=20.0,
    )

    T_cycle = 1.0 / f_ac
    t_span = (0, T_cycle)

    print("Integrating Topological Ode (Halts via Saturation Yield)...")
    sol = solver.solve_collapse(t_span, max_step=1e-8)

    R_array = sol.y[0]
    R_min = np.min(R_array)
    U_min = np.min(sol.y[1])

    print(f"Simulation completed in {len(sol.t)} steps.")
    print(f"Collapse R_min: {R_min*1e9:.2f} nm (compression ratio: {R0/R_min:.1f})")
    print(f"Max wall velocity: {abs(U_min):.2f} m/s (Mach: {abs(U_min)/solver.c_sound:.3f})")

    # Internal state at collapse
    P_max = solver._internal_pressure(R_min)
    print(f"Peak internal pressure: {P_max/101325.0:.2e} atm")

    T_flash = compute_flash_temperature(R_min, P_max, R0, payload)
    print(f"Predicted Topological Flash Temp: {T_flash:.1f} K")
    print("----------------------------------------------------------\n")
    return sol, solver


def generate_manuscript_figures() -> None:
    """Generates the Vol 3 publication figures demonstrating Tabletop Relativity.

    Figure bodies are restyled through ``ave.viz.style`` (house print profile);
    the descriptive titles live in the LaTeX ``\\caption{}`` of the Vol-3
    chapter, not baked into the raster (ave-figure-discipline Axis 4). The
    underlying physics/data are unchanged.
    """
    print("Generating Manuscript Figures...")

    # House print profile (white background, house grid/palette) FIRST.
    style.apply()

    # Run the Argon payload for the baseline experimental comparison
    sol, solver = run_simulation("argon")

    t = sol.t * 1e6  # milliseconds to microseconds
    R = sol.y[0] * 1e6  # meters to microns
    U = sol.y[1]

    # Calculate the topological Lorentz factor (gamma^3 for longitudinal inertia)
    M = np.clip(U / solver.c_sound, -0.999999999, 0.999999999)
    S = np.sqrt(1.0 - M**2)
    gamma_equiv = 1.0 / (S**3)

    # Highlight the final 1 microsecond of the collapse
    idx_collapse = np.argmin(R)
    t_collapse = t[idx_collapse]

    # ---- FIGURE 1: Sonoluminescence R(t) Phase ----
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    ax.plot(t, R, color=style.COLORS["ave"], linestyle="-")
    ax.set_xlabel(style.axis_label("Time", "t", r"$\mu$s"))
    ax.set_ylabel(style.axis_label("Bubble radius", "R", r"$\mu$m"))
    style.save(fig, manuscript_path("vol_3_macroscopic", "figures", "vol3_sonoluminescence_collapse"))
    plt.close(fig)

    # ---- FIGURE 2: Tabletop Relativity (Effective Mass Divergence) ----
    # Focus only on the collapse spike (last ~0.1 us before collapse)
    spike_mask = (t > t_collapse - 0.2) & (t < t_collapse + 0.05)
    t_spike = t[spike_mask]
    gamma_spike = gamma_equiv[spike_mask]

    fig, ax = plt.subplots(figsize=style.figsize("single"))
    ax.plot(t_spike, gamma_spike, color=style.COLORS["ave"], linestyle="-")
    ax.set_xlabel(style.axis_label("Time", "t", r"$\mu$s"))
    ax.set_ylabel(style.axis_label("Relative fluid inertia", r"\rho_{\mathrm{eff}}/\rho_0", "dimensionless"))
    ax.set_yscale("log")
    ax.annotate(
        r"$\rho_{\mathrm{eff}} \rightarrow \infty$ as $U \rightarrow c_0$",
        xy=(t_collapse, np.max(gamma_spike)),
        xytext=(t_collapse - 0.1, np.max(gamma_spike) * 0.1),
        arrowprops=dict(color=style.COLORS["muted"], shrink=0.05, width=1.0, headwidth=5),
        color=style.COLORS["muted"],
    )
    style.save(fig, manuscript_path("vol_3_macroscopic", "figures", "vol3_tabletop_relativity_lorentz"))
    plt.close(fig)

    print("Figures saved: vol3_sonoluminescence_collapse.pdf, vol3_tabletop_relativity_lorentz.pdf")


if __name__ == "__main__":
    print("=== AVE Sonoluminescence Simulation Suite ===")
    print("Zero-Parameter Tabletop Relativity Boundary Prediction\n")

    generate_manuscript_figures()

    # Also run Xenon and Vapor for console metrics
    run_simulation("xenon")
    run_simulation("vapor")
