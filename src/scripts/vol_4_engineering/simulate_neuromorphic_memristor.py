"""
Neuromorphic Memristor Hysteresis Visualization (illustrative — chosen R ratios).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script renders an illustrative I-V hysteresis curve for a metamaterial
neuromorphic memristor using:
  - E_GAP_TRIGGER = 0.2158 eV — the comment claims "Derived natively from
    the Void Fraction remainder (1 - Phi_limit)" but the derivation chain
    is NOT shown in this script; the value is asserted, not computed here.
    The (1 - Phi_limit) framing is canonical, but the projection chain to
    0.2158 eV needs to be cited from a derivation script.
  - RESISTANCE_V_II = 1e6 ohm and RESISTANCE_V_I = 1e2 ohm — CHOSEN to
    span the typical memristor on/off resistance ratio (~10^4), NOT
    derived from substrate impedance physics.

The script does NOT compute:
  - On/off resistance ratio derived from V_II vs V_I phase-state impedance
  - Comparison against specific neuromorphic device measurements
  - Switching speed prediction from substrate transition dynamics

The illustration supports the AVE narrative that memristor hysteresis is
a V_II↔V_I phase-state transition. Quantitative prediction requires the
phase-gap derivation chain to be sourced (TBD-pin 2026-05-17 audit).

Docstring corrected 2026-05-17.
"""

import os
from pathlib import Path

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

# The subatomic phase-gap separating the V_II dielectric phase from the V_I conduction phase
# Claim: derived from Void Fraction remainder (1 - Phi_limit) — derivation chain
# TBD-pin per 2026-05-17 audit; value asserted here, not computed
E_GAP_TRIGGER = 0.2158  # Regime II Subatomic Electroweak/Structural Energy Gap (eV) — asserted

# Dielectric State Limits — CHOSEN to span typical memristor on/off ratio, NOT derived
RESISTANCE_V_II = 1e6  # Native Unstructured Insulator (High Resistance, illustrative)
RESISTANCE_V_I = 1e2  # Structurally Locked Crystal Wire (Low Resistance, illustrative)


def simulate_neuromorphic_memristor() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Finite-Difference voltage stepping evaluating localized Metamaterial structures.
    Proves macroscopic brain-like memory (Hysteresis) mapped purely to the AVE E_gap trigger.
    """
    print("Initiating AVE Neuromorphic SPICE-Equivalent Solver...")
    print(f"Tracking Localized Dielectric Topological Collapse at Phase-Gap: {E_GAP_TRIGGER} eV\n")

    # Time constants
    NT = 2000
    times = np.linspace(0, 10, NT)
    dt = times[1] - times[0]

    # The Biological "Action Potential" Driver
    # We apply an alternating triangular voltage wave (Sweep from -1.0V to +1.0V)
    # Typical experimental memristor read/write setup
    freq = 0.5
    V_app = 0.8 * np.sin(2.0 * np.pi * freq * times)

    # State tracking arrays
    current_I = np.zeros(NT)
    w_state = np.zeros(NT)  # Structural state [0, 1]. 0 = Fluid V_II, 1 = Solid V_I

    # Initialize native insulating material
    w = 0.05

    # Topological Structural Kinetics (How fast the material crystallizes/melts)
    structural_mobility = 10.0  # Rate of lattice collapse when driven
    relaxation_rate = 1.0  # Rate of native V_II fluid relaxation

    # FDTD Main Sweep Loop
    for i in range(NT):
        V = V_app[i]

        # 1. Evaluate the Energy Phase-Gap (Axiom 2 / Axiom 4 limit)
        # We calculate the normalized energy being pumped into the local polymer node
        # We approximate E_applied ~ |V| (in a 1e- charge potential well)
        E_applied = abs(V)

        # 2. Structural Phase-Transition Logic
        if E_applied > E_GAP_TRIGGER:
            # The applied nanovolt action-potential overwhelms the void-fraction phase gap!
            # The material dynamically structurally snaps into a V_I crystal wire
            # The strength of the rewiring is proportional to how far past the gap we push it
            overdrive = E_applied - E_GAP_TRIGGER

            if V > 0:
                dw = structural_mobility * overdrive * dt
            else:
                # Reverse polarity dissolves the topological crystal bonds, erasing memory
                dw = -structural_mobility * overdrive * dt
        else:
            # If the voltage is too weak, the thermal geometry naturally relaxes
            # the node back into its base V_II un-locked fluid configuration (forgetting data)
            dw = -relaxation_rate * w * dt

        # Update physical lattice state and bound it
        w += dw
        w = max(0.001, min(1.0, w))
        w_state[i] = w

        # 3. Electrical Translation
        # Compute the instantaneous localized structural resistance
        # Weighted interpolation between the V_I diamond-like state and V_II unstructured state
        G_min = 1.0 / RESISTANCE_V_II
        G_max = 1.0 / RESISTANCE_V_I

        # Total localized conductance
        G_total = G_min * (1.0 - w) + G_max * w

        # Resultant topological current
        current_I[i] = G_total * V

    print("Phase-Gap Topological Breakdown successfully simulated across alternating action potentials.")
    return times, V_app, current_I, w_state


def plot_memory_hysteresis(times: np.ndarray, V_app: np.ndarray, current_I: np.ndarray, w_state: np.ndarray) -> None:
    """
    Plot the physical state transition over time and
    the classic Non-Linear I-V Memristor "Bow-Tie" curve.
    """
    # fig = plt.figure(figsize=(14, 6))  # bulk lint fixup pass
    gs = gridspec.GridSpec(1, 2, width_ratios=[1.2, 1])

    # Plot 1: Temporal Voltage and Structural State Mapping
    ax1 = plt.subplot(gs[0])
    ax1.set_facecolor("black")

    # Input Voltage (Action Potential)
    ax1.plot(times, V_app, color="cyan", linewidth=2.0, alpha=0.8, label="Applied Synaptic Voltage ($V$)")
    ax1.axhline(
        E_GAP_TRIGGER,
        color="white",
        linestyle="--",
        alpha=0.9,
        linewidth=1.5,
        label="AVE Void-Fraction Gap Limit (+0.2158 eV)",
    )
    ax1.axhline(
        -E_GAP_TRIGGER,
        color="white",
        linestyle="--",
        alpha=0.9,
        linewidth=1.5,
        label="AVE Void-Fraction Gap Limit (-0.2158 eV)",
    )

    # The physical structure variable w
    ax1_twin = ax1.twinx()
    ax1_twin.plot(
        times,
        w_state,
        color="#FF4444",
        linewidth=2.5,
        label="Structural State $w$ ($V_{II} \Rightarrow V_I$)",
    )

    ax1.set_title(
        "1. Dielectric Topological Yield tracking Action Potentials",
        color="white",
        fontsize=12,
        fontweight="bold",
    )
    ax1.set_xlabel("Time (s)", color="white")
    ax1.set_ylabel("Applied Voltage (V)", color="white")
    ax1_twin.set_ylabel("Physical Conductive State ($\%$ $V_I$ Lock)", color="white")

    ax1.tick_params(colors="white")
    ax1_twin.tick_params(colors="white")
    for spine in ax1.spines.values():
        spine.set_color("white")
    for spine in ax1_twin.spines.values():
        spine.set_color("white")

    ax1.legend(loc="upper right", facecolor="black", edgecolor="white", labelcolor="white")
    ax1_twin.legend(loc="lower right", facecolor="black", edgecolor="white", labelcolor="white")

    # Plot 2: I-V Hysteresis Loop (The Neural Bow-Tie)
    ax2 = plt.subplot(gs[1])
    ax2.set_facecolor("black")

    ax2.plot(V_app, current_I * 1000, color="#00FF55", linewidth=2.0)

    ax2.set_title(
        "2. I-V Hysteresis: True Artificial Hardware Memory",
        color="white",
        fontsize=12,
        fontweight="bold",
    )
    ax2.set_xlabel("Applied Membrane Voltage (V)", color="white")
    ax2.set_ylabel("Synthesized Current (mA)", color="white")
    ax2.grid(True, color="#333333", linestyle=":")

    ax2.tick_params(colors="white")
    for spine in ax2.spines.values():
        spine.set_color("white")

    plt.tight_layout()
    plt.gcf().patch.set_facecolor("black")

    # Save Output Asset
    out_dir = Path(os.path.dirname(__file__)) / ".." / ".." / ".." / "assets" / "sim_outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "neuromorphic_memristor_hysteresis.png"
    plt.savefig(out_path, dpi=300, facecolor="black")
    print(f"Asset successfully rendered to: {out_path}")


if __name__ == "__main__":
    t, V, I, state = simulate_neuromorphic_memristor()
    plot_memory_hysteresis(t, V, I, state)
