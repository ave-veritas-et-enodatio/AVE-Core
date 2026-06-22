"""
Phase-Locked Superconductivity Visualization (illustrative Kuramoto — no T_c prediction).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script runs an illustrative Kuramoto oscillator simulation with
chosen coupling K and temperature schedule to demonstrate the AVE
interpretation that superconductivity is a kinematic phase-lock of
adjacent electron inductors (NOT Cooper pairs + phonon exchange).

The script does NOT compute:
  - T_c (critical temperature) for any specific superconductor
  - Comparison against BCS prediction T_c = 1.13 Theta_D exp(-1/N(0)V)
  - Niobium, MgB2, YBCO, or any specific T_c numerical match
  - Meissner-effect penetration depth lambda_L

This is an illustrative Kuramoto demo of the AVE phase-lock interpretation,
NOT a T_c prediction. Quantitative superconductor benchmarks require a
dedicated AVE-engine workstream (would parallel the SPARC ingest pattern
for condensed-matter targets).

Docstring corrected 2026-05-17.

FIGURE STYLE (2026-06-21 Vol-3 figure-regen sweep):
Restyled through ``ave.viz.style`` (house print profile, white background,
Okabe-Ito palette, legend outside the data). The descriptive title lives in
the LaTeX ``\\caption{}`` of chapter 09, not baked into the raster. Only the
PRESENTATION changed; the Kuramoto simulation (coupling K, temperature
schedule, order-parameter / resistance traces) is byte-for-byte unchanged.
The figure is written through the canonical ``ave_path_util.sim_output``
resolver so it lands at ``assets/sim_outputs/superconductivity_phase_lock.pdf``
— the path the manuscript ``\\includegraphics`` resolves via ``graphicspath``.
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless render-to-file driver

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Resolve the repo's src/ so `ave_path_util` + `ave.viz` import when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ave.viz import style  # noqa: E402
from ave_path_util import sim_output  # noqa: E402


def main() -> None:
    print("==========================================================")
    print(" AVE CONDENSED MATTER: SUPERCONDUCTIVITY VISUALIZATION    ")
    print("                       (illustrative Kuramoto demo)        ")
    print("==========================================================\n")

    print("- Renders AVE narrative: superconductivity as kinematic phase-lock.")
    print("- No T_c prediction; no BCS comparison.")
    print("  Illustrative Kuramoto demo, not quantitative derivation.\n")

    print("[1] Initializing 2D cross-section of conducting electron gas...")

    # Simulation Parameters
    num_electrons = 100
    time_steps = 200
    dt = 0.1

    # We track the "Phase Angle" of each electron (its internal geometric rotation state)
    # Electrons are classical inductors (unknots).
    # Resistance = L * dI/dt (where dI/dt is driven by relative phase mismatches)

    # Random initial phases at high temperature (ambient jitter)
    phases = np.random.uniform(0, 2 * np.pi, num_electrons)

    # Natural rotation frequency of the free electrons
    omega_0 = 1.0

    # Coupling constant (How strongly the magnetic flux of one electron pulls on its neighbor)
    # In a lattice, as the lattice shrinks (T drops), coupling K increases relative to thermal noise.
    K = 1.5

    # Thermal Noise (Transverse acoustic jitter breaking the phase-locks)
    # We will simulate the system cooling down over time.
    initial_T = 2.0
    final_T = 0.05
    T_schedule = np.linspace(initial_T, final_T, time_steps)

    print("[2] Simulating Thermal Cooling (Kuramoto Oscillator Model)...")
    print("    - As Temperature (T) drops, thermal acoustic noise decreases.")
    print("    - When Coupling (K) > Noise (T), the electron inductors mechanically lock gears.")

    # Tracking Phase Coherence (Order Parameter r)
    # r = 0 : Total random chaos (High Resistance)
    # r = 1 : Total macroscopic phase-lock (Zero Resistance)
    coherence_history = []
    resistance_history = []

    for step in range(time_steps):
        T = T_schedule[step]

        # Calculate mean-field coupling (Kuramoto Phase-locking)
        # Every electron feels a torque proportional to sin(AvgPhase - MyPhase)
        avg_phase = np.angle(np.mean(np.exp(1j * phases)))

        # Add thermal noise
        noise = np.random.normal(0, T, num_electrons)

        # Update phases: d(theta)/dt = omega_0 + K * sin(avg_phase - theta) + noise
        d_theta = omega_0 + K * np.sin(avg_phase - phases) + noise
        phases = (phases + d_theta * dt) % (2 * np.pi)

        # Calculate Coherence
        r = np.abs(np.mean(np.exp(1j * phases)))
        coherence_history.append(r)

        # Calculate Resistance (Proportional to phase mismatches, i.e., 1 - Coherence)
        # When all electrons rotate perfectly in sync, there is no relative dB/dt between them.
        # No relative induction = No Resistance.
        resistance = 1.0 - r
        resistance_history.append(max(0, resistance))

    print("[3] Phase Transition Achieved.")

    # ------------------------------------------------------------------
    # Render the phase-transition graph (house print profile)
    # ------------------------------------------------------------------
    style.apply()  # white-background "print" profile, Okabe-Ito palette FIRST

    fig, ax = plt.subplots(figsize=style.figsize("single"))

    # X-axis is temperature, read right-to-left (cooling down). The arrays are
    # reversed exactly as before so the plotted data is unchanged.
    ax.plot(
        T_schedule[::-1],
        resistance_history[::-1],
        color=style.COLORS["ave"],
        linestyle="-",
        label="Macroscopic electrical resistance",
    )
    ax.plot(
        T_schedule[::-1],
        coherence_history[::-1],
        color=style.COLORS["comparison"],
        linestyle="--",
        label="Electron phase coherence (0 to 1)",
    )

    # Critical phase-lock threshold (illustrative T_c marker).
    ax.axvline(
        x=0.5,
        color=style.COLORS["muted"],
        linestyle=":",
        label=r"Critical phase-lock threshold ($T_c$)",
    )

    ax.set_xlabel(
        style.axis_label("Temperature (acoustic jitter)", "T", "dimensionless")
    )
    ax.set_ylabel(style.axis_label("Normalized state", "", ""))

    ax.invert_xaxis()  # plot cooling from left (warm) to right (cold)

    # Legend OUTSIDE the data (the old figure dropped it onto the curves).
    style.legend(ax, where="right")

    out_path = sim_output("superconductivity_phase_lock.pdf")
    written = style.save(fig, out_path)
    plt.close(fig)

    print("\n[STATUS: SUCCESS] Classical kinematic phase-lock figure rendered.")
    for p in written:
        print(f"wrote {p}")


if __name__ == "__main__":
    main()
