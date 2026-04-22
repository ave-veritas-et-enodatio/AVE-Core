import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

from ave.core.constants import V_YIELD

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

# Simulation Parameters for the Spacetime Vacuum Tank
L_0 = 1e-3  # Baseline Inductance (1 mH)
C_0_SIM = 1e-9  # Baseline Capacitance (1 nF)


# Resonant Frequency Formula
def w_res(C_val):
    return 1.0 / np.sqrt(L_0 * C_val)


w_0 = w_res(C_0_SIM)  # Baseline resonant frequency (rad/s)


# Non-linear Capacitance (Dielectric Yielding)
# C(V) increases as V approaches V_yield because e_eff drops (C = e*A/d goes down, causing frequency
# characteristic to detune).
# Wait, actually in Book 4 Eq 13.1, e_eff decreases. So C_eff decreases!
# w = 1 / sqrt(L*C_eff). If C_eff drops, the resonant frequency of the vacuum INCREASES as it is stressed.
def C_eff(V):
    # Cap stops dropping right before divide by zero to prevent solver crash
    v_norm = min(abs(V) / V_YIELD, 0.999)
    return C_0_SIM * np.sqrt(1.0 - v_norm**2)


# Source Drive (The laser)
DRIVE_AMPLITUDE = 8e-5  # Drive current amplitude


# --- 1. The Fixed-Frequency Petawatt Laser (No PLL) ---
def fixed_driver_model(y, t):
    """
    Simulates driving the vacuum with a massive fixed-frequency laser.
    y[0] = V_C (Voltage across the space)
    y[1] = I_L (Current)
    """
    V_c, I_l = y

    # The vacuum detunes itself!
    C_current = C_eff(V_c)

    # Fixed frequency laser drive (tuned to the resting vacuum w_0)
    I_drive = DRIVE_AMPLITUDE * np.cos(w_0 * t)

    dV_c_dt = (I_drive - I_l) / C_current
    dI_l_dt = V_c / L_0

    return [dV_c_dt, dI_l_dt]


# --- 2. The Autoresonant Phase-Locked Loop (PLL) ---
def pll_driver_model(y, t):
    """
    Simulates driving the vacuum with a smart PLL that tracks the detuning.
    y[0] = V_C
    y[1] = I_L
    y[2] = theta_drive (The active phase of the PLL)
    """
    V_c, I_l, theta = y

    C_current = C_eff(V_c)

    # Auto-resonance: The PLL measures the *current* resonant frequency of the gap
    # and strictly injects exactly at that detuned frequency to maximize power transfer.
    w_current = w_res(C_current)

    # Drive with the active phase
    I_drive = DRIVE_AMPLITUDE * np.cos(theta)

    dV_c_dt = (I_drive - I_l) / C_current
    dI_l_dt = V_c / L_0

    # The PLL updates its phase angle based on the shifting resonant frequency
    dtheta_dt = w_current

    return [dV_c_dt, dI_l_dt, dtheta_dt]


def run_autoresonance_sim():
    print("[*] Running Autoresonant PLL SPICE Model...")

    t_end = 200e-6
    t = np.linspace(0, t_end, 50000)

    # Initial Conditions (start at 0V)
    y0_fixed = [0.0, 0.0]
    y0_pll = [0.0, 0.0, 0.0]  # Starts with 0 phase

    sol_fixed = odeint(fixed_driver_model, y0_fixed, t)
    sol_pll = odeint(pll_driver_model, y0_pll, t)

    V_fixed = sol_fixed[:, 0]
    V_pll = sol_pll[:, 0]

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

    # Plot 1: Fixed Frequency (Schwinger Limit reflection)
    axes[0].plot(
        t * 1e6,
        V_fixed / 1000,
        color="#ffcc00",
        linewidth=1.5,
        label="Fixed Freq Laser ($w = w_0$)",
    )
    axes[0].axhline(
        V_YIELD / 1e3,
        color="#ff3333",
        linestyle="--",
        linewidth=2,
        label=f"Dielectric Yield Limit ({V_YIELD/1e3:.1f} kV)",
    )
    axes[0].axhline(-V_YIELD / 1e3, color="#ff3333", linestyle="--", linewidth=2)
    axes[0].set_ylim(-80, 80)
    axes[0].set_title("Standard Approach: The Vacuum Detunes and Reflects Power")
    axes[0].set_xlabel("Time ($\\mu$s)")
    axes[0].set_ylabel("Metric Voltage (kV)")
    leg1 = axes[0].legend(facecolor="#0f0f0f", edgecolor="none", loc="upper right")
    for text in leg1.get_texts():
        text.set_color("white")

    # Annotate plateau
    axes[0].annotate(
        "Laser Detunes\nPower is Reflected",
        xy=(100, 20),
        xytext=(50, 40),
        arrowprops=dict(facecolor="white", shrink=0.05),
        color="white",
        fontsize=10,
    )

    # Plot 2: PLL Autoresonance
    axes[1].plot(
        t * 1e6,
        V_pll / 1000,
        color="#00ffcc",
        linewidth=1.5,
        label="PLL Autoresonant Laser ($w = w_{eff}$)",
    )
    axes[1].axhline(
        V_YIELD / 1e3,
        color="#ff3333",
        linestyle="--",
        linewidth=2,
        label=f"Dielectric Yield Limit ({V_YIELD/1e3:.1f} kV)",
    )
    axes[1].axhline(-V_YIELD / 1e3, color="#ff3333", linestyle="--", linewidth=2)
    axes[1].set_ylim(-80, 80)
    axes[1].set_title("AVE Approach: PLL Tracks Detuning to Breach Limit")
    axes[1].set_xlabel("Time ($\\mu$s)")
    axes[1].set_ylabel("Metric Voltage (kV)")

    axes[1].annotate(
        "PLL Tracks Shift\nConstructive Interference Maintained",
        xy=(150, 50),
        xytext=(50, -40),
        arrowprops=dict(facecolor="white", shrink=0.05),
        color="white",
        fontsize=10,
    )

    leg2 = axes[1].legend(facecolor="#0f0f0f", edgecolor="none", loc="upper left")
    for text in leg2.get_texts():
        text.set_color("white")

    plt.tight_layout()

    # Save output
    project_root = pathlib.Path(str(pathlib.Path(__file__).parent.parent.parent.parent.absolute()))
    outdir = project_root / "spice_manual" / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "autoresonance_pll.png"

    plt.savefig(target, dpi=150, facecolor="#0f0f0f")
    print(f"[*] Visualized Autoresonant PLL: {target}")


if __name__ == "__main__":
    run_autoresonance_sim()
