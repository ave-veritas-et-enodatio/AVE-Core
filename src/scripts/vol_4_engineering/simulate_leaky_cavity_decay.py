import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

from ave.core.constants import V_YIELD

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

# Simulation Parameters
L = 1e-3  # Inductance (1 mH)
C = 1e-9  # Capacitance (1 nF)

# We use a non-linear parallel resistance to model the vacuum breaking.
# In a perfect vacuum (V < V_YIELD), R is near infinite (perfect LC resonance).
# When the vacuum breaks (V > V_YIELD), R drops drastically to bleed energy.
R_IDEAL = 1e9  # 1 GigaOhm (Stable knot)
R_LEAK = 50.0  # 50 Ohms (Avalanche breakdown)


def leaky_rc_model(y: list[float], t: float) -> list[float]:
    """
    Simulates a non-linear RLC circuit.
    y[0] = V_C (Voltage across the capacitor)
    y[1] = I_L (Current through the inductor)
    """
    V_c, I_l = y

    # Non-linear Vacuum Breakdown
    if abs(V_c) > V_YIELD:
        R_eff = R_LEAK
    else:
        R_eff = R_IDEAL

    # The ODE system for parallel RLC
    # dV_c/dt = - V_c / (R_eff * C) - I_l / C
    # dI_l/dt = V_c / L
    dV_c_dt = -V_c / (R_eff * C) - I_l / C
    dI_l_dt = V_c / L

    return [dV_c_dt, dI_l_dt]


def run_leaky_cavity_sim() -> None:
    print("[*] Running Leaky Cavity (Particle Decay) SPICE Model...")

    # Time vector (we want to see the rapid cycles and the envelope decay)
    # Resonant frequency f = 1 / (2*pi*sqrt(L*C)) ~ 159 kHz
    t_end = 200e-6  # 200 microseconds
    t = np.linspace(0, t_end, 50000)

    # Initial Conditions:
    # 1. Standard Electron (Stable topological ground state)
    # Energy is well below structural yield limit.
    V_electron = 25000.0  # 25 kV
    y0_e = [V_electron, 0.0]

    # 2. Heavy Fermion / Muon (Unstable forced resonance)
    # Energy vastly exceeds the topological capacity.
    V_muon = 150000.0  # 150 kV
    y0_u = [V_muon, 0.0]

    sol_e = odeint(leaky_rc_model, y0_e, t)
    sol_u = odeint(leaky_rc_model, y0_u, t)

    V_e = sol_e[:, 0]
    V_u = sol_u[:, 0]

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.patch.set_facecolor("#0f0f0f")

    for ax in axes:
        ax.set_facecolor("#0f0f0f")
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("white")
        ax.grid(True, alpha=0.2)
        for spine in ax.spines.values():
            spine.set_color("#333333")

    # Plot 1: The Stable Electron
    axes[0].plot(
        t * 1e6,
        V_e / 1000,
        color="#00ffcc",
        linewidth=1.5,
        label="Electron LC Knot ($V < V_{yield}$)",
    )
    axes[0].axhline(
        V_YIELD / 1e3,
        color="#ff3333",
        linestyle="--",
        linewidth=2,
        label=f"Dielectric Yield Limit ({V_YIELD/1e3:.1f} kV)",
    )
    axes[0].axhline(-V_YIELD / 1e3, color="#ff3333", linestyle="--", linewidth=2)
    axes[0].set_ylim(-160, 160)
    axes[0].set_title("The Ground State (Stable Topological Knot)")
    axes[0].set_xlabel("Time ($\\mu$s)")
    axes[0].set_ylabel("Topological Metric Voltage (kV)")
    leg1 = axes[0].legend(facecolor="#0f0f0f", edgecolor="none", loc="upper right")
    for text in leg1.get_texts():
        text.set_color("white")

    # Plot 2: The Leaky Cavity (Muon Decay)
    axes[1].plot(
        t * 1e6,
        V_u / 1000,
        color="#ff00ff",
        linewidth=1.5,
        label="Heavy Fermion LC Knot ($V > V_{yield}$)",
    )
    axes[1].axhline(
        V_YIELD / 1e3,
        color="#ff3333",
        linestyle="--",
        linewidth=2,
        label=f"Dielectric Yield Limit ({V_YIELD/1e3:.1f} kV)",
    )
    axes[1].axhline(-V_YIELD / 1e3, color="#ff3333", linestyle="--", linewidth=2)
    axes[1].set_ylim(-160, 160)
    axes[1].set_title("The Leaky Cavity (Particle Decay to Ground State)")
    axes[1].set_xlabel("Time ($\\mu$s)")
    axes[1].set_ylabel("Topological Metric Voltage (kV)")

    # Overlay the envelope decay explanation
    axes[1].annotate(
        "Metric Ruptures\nEnergy bleeds into vacuum",
        xy=(10, 100),
        xytext=(40, 120),
        arrowprops=dict(facecolor="white", shrink=0.05),
        color="white",
        fontsize=10,
    )
    axes[1].annotate(
        "Decay Halts\nStable ground state reached",
        xy=(150, 60),
        xytext=(120, 100),
        arrowprops=dict(facecolor="white", shrink=0.05),
        color="white",
        fontsize=10,
    )

    leg2 = axes[1].legend(facecolor="#0f0f0f", edgecolor="none", loc="upper right")
    for text in leg2.get_texts():
        text.set_color("white")

    plt.tight_layout()

    # Save output
    project_root = pathlib.Path(str(pathlib.Path(__file__).parent.parent.parent.parent.absolute()))
    outdir = project_root / "spice_manual" / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "leaky_cavity_decay.png"

    plt.savefig(target, dpi=150, facecolor="#0f0f0f")
    print(f"[*] Visualized Leaky Cavity Decay: {target}")


if __name__ == "__main__":
    run_leaky_cavity_sim()
