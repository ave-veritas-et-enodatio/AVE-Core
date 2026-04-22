"""
AVE Stellar Engineering: Topological Solar Weather Calculator
======================================================
Building on the scale-invariant proof that a Star is a Macroscopic 
Light Emitting Diode (LED), we can apply rigorous semiconductor
transconductance equations to predict Solar Weather.

In a standard solid-state diode, the Current-Voltage (I-V) relationship 
is governed by the Shockley Diode Equation, modified by an Avalanche 
Multiplication Factor M(V) as the voltage approaches the breakdown threshold (Bandgap).

For a Star:
- VOLTAGE (V): The accumulated topological $1/r$ magnetic shear stress (Dynamo wind-up).
- CURRENT (I): The macroscopic photon (flare) emission rate.
- V_bd: The macroscopic yield stress of the LC vacuum metric (Bandgap).

This script:
1. Derives the Macroscopic I-V curve for a stellar diode.
2. Maps predicted flare classifications (C, M, X-class) directly to the I-V thresholds.
3. Computes the Full-Width at Half-Maximum (FWHM) of the Solar Maximum topological saturation zone.
"""

import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np

# AVE Engine — for context on the macroscopic yield limit
from ave.core.constants import AVALANCHE_N_3D


project_root = pathlib.Path(__file__).parent.parent.absolute()
# ── PHENOMENOLOGICAL PARAMETERS ──────────────────────────────────────────
# These are phenomenological fits to the Shockley diode + avalanche model.
# V_BD, I_S, V_T are macroscopic analogy parameters (NOT derived from AVE axioms).
# AVALANCHE_N is derived from pure Axiom 4 + 3D Poisson scaling.
V_BD = 100.0  # Macroscopic Bandgap Voltage (Yield Stress of Vacuum)
I_S = 1e-3  # Saturation leakage current (Ambient Corona Emission)
V_T = 15.0  # Thermal Equivalent Voltage (Ambient kinetic baseline)
AVALANCHE_N = AVALANCHE_N_3D  # Axiom 4: 38/21 ≈ 1.8095


def macroscopic_shockley_avalanche(v):
    """
    Computes the Macroscopic Photon Emission Rate (Current I)
    based on the topological shear strain (Voltage V).
    """
    # 1. Shockley Baseline (Forward Bias)
    i_diode = I_S * (np.exp(v / V_T) - 1.0)

    # 2. Avalanche Multiplication Factor M(V)
    # As V approaches V_BD, M -> infinity (structural breakdown)
    # We clip it slightly below 1.0 to prevent divide-by-zero infinite asymptotic blowup in code
    v_ratio = np.clip(v / V_BD, 0, 0.999)
    m_factor = 1.0 / (1.0 - (v_ratio) ** AVALANCHE_N)

    # Base Current is zero for V < 0 (reverse bias)
    i_total = np.where(v > 0, i_diode * m_factor, 0.0)
    return i_total


def generate_weather_calculator():
    print("[*] Initializing AVE Topological Solar Weather Calculator...")

    # -------------------------------------------------------------
    # PLOT 1: The Macroscopic I-V Curve (Transconductance)
    # -------------------------------------------------------------
    print("[*] Deriving Stellar Diode I-V Curve...")
    voltages = np.linspace(0, 105, 500)
    currents = macroscopic_shockley_avalanche(voltages)

    # Define empirical Solar Flare Classes as distinct "Current" thresholds
    # C-Class: Minor bubbling, M-Class: Moderate localized snap, X-Class: Massive regional cascade
    C_CLASS_THRESHOLD = 0.5
    M_CLASS_THRESHOLD = 5.0
    X_CLASS_THRESHOLD = 50.0

    # -------------------------------------------------------------
    # PLOT 2: The 11-Year Dynamo FWHM (Solar Maximum Saturation Zone)
    # -------------------------------------------------------------
    print("[*] Simulating 11-Year Dynamo Voltage cycle...")
    years = np.linspace(0, 22, 1000)  # Two full 11-year cycles

    # Model the Sun's dynamo topological voltage winding up and relaxing
    # Base voltage + AC dynamo sine wave
    dynamo_voltage = 50.0 + 49.5 * np.sin((2 * np.pi * years) / 11.0 - np.pi / 2)

    # Calculate the resulting Current (Flare Emission Probability)
    flare_probability = macroscopic_shockley_avalanche(dynamo_voltage)

    # Calculate FWHM
    print("[*] Calculating FWHM of Solar Maximum Saturation Zone...")
    # Find peaks in the emission curve
    peaks, _ = scipy_find_peaks(flare_probability)  # Custom inline to avoid extra imports if possible

    # We will compute FWHM manually for the highest peak
    max_prob = np.max(flare_probability)
    half_max = max_prob / 2.0

    # Find indices where it crosses half_max
    # Just looking at the first cycle (years 0 to 11)
    cycle1_mask = years <= 11.0
    cycle1_prob = flare_probability[cycle1_mask]
    cycle1_years = years[cycle1_mask]

    above_half = np.where(cycle1_prob >= half_max)[0]
    if len(above_half) > 0:
        fwhm_start_idx = above_half[0]
        fwhm_end_idx = above_half[-1]
        fwhm_start_yr = cycle1_years[fwhm_start_idx]
        fwhm_end_yr = cycle1_years[fwhm_end_idx]
        fwhm_duration = fwhm_end_yr - fwhm_start_yr
    else:
        fwhm_start_yr = 0
        fwhm_end_yr = 0
        fwhm_duration = 0

    # -------------------------------------------------------------
    # RENDER PANELS
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    fig.patch.set_facecolor("#0f0f0f")

    for ax in [ax1, ax2]:
        ax.set_facecolor("#0f0f0f")
        ax.grid(color="#333333", linestyle="--", alpha=0.5)
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("white")
        for spine in ax.spines.values():
            spine.set_edgecolor("#555555")

    # Panel 1: Macroscopic I-V Curve
    ax1.plot(voltages, currents, color="#00ffcc", lw=3, label=r"Macroscopic $I-V$ (Shockley+Avalanche)")
    ax1.axvline(V_BD, color="#ff3333", linestyle="--", lw=2, label=r"Topological Yield Limit ($V_{bd}$)")

    # Highlight Flare Classes as current regimes
    ax1.fill_between(
        voltages,
        C_CLASS_THRESHOLD,
        M_CLASS_THRESHOLD,
        color="#ffff99",
        alpha=0.2,
        label="C-Class Regime",
    )
    ax1.fill_between(
        voltages,
        M_CLASS_THRESHOLD,
        X_CLASS_THRESHOLD,
        color="#ff9933",
        alpha=0.3,
        label="M-Class Regime",
    )
    ax1.fill_between(
        voltages,
        X_CLASS_THRESHOLD,
        max(currents),
        color="#ff3333",
        alpha=0.4,
        label="X-Class Avalanche Region",
    )

    ax1.set_yscale("log")
    ax1.set_ylim([1e-3, 1e4])
    ax1.set_xlim([0, 105])
    ax1.set_title("Stellar Diode: Macroscopic I-V Transconductance")
    ax1.set_xlabel("Topological Strain / Dynamo Winding (Macroscopic Volts V)")
    ax1.set_ylabel("Photon Emission Rate (Macroscopic Amperes I)")
    ax1.legend(loc="upper left", fontsize=9)

    # Panel 2: Predictive Solar Weather & FWHM
    ax2.plot(years, flare_probability, color="#ffcc00", lw=2, label="Flare Probability (I)")
    ax2.plot(years, dynamo_voltage, color="#66ccff", linestyle="-.", lw=1.5, label="Dynamo Voltage (V)")

    # Plot the FWHM
    ax2.hlines(
        half_max,
        fwhm_start_yr,
        fwhm_end_yr,
        color="#ff33ff",
        lw=3,
        label=f"Solar Max FWHM: {fwhm_duration:.2f} Years",
    )
    ax2.scatter([fwhm_start_yr, fwhm_end_yr], [half_max, half_max], color="white", zorder=5)

    # Mark Flare Thresholds on the dynamic timeline
    ax2.axhline(M_CLASS_THRESHOLD, color="#ff9933", linestyle="--", alpha=0.5, label="M-Class Threshold")
    ax2.axhline(X_CLASS_THRESHOLD, color="#ff3333", linestyle="--", alpha=0.5, label="X-Class Threshold")

    ax2.set_yscale("log")
    ax2.set_xlim([0, 22])
    ax2.set_ylim([1e-2, 1e4])
    ax2.set_title("11-Year Cycle Tracking & FWHM (Solar Weather Forecast)")
    ax2.set_xlabel("Time (Years)")
    ax2.set_ylabel("Emission Probability / Voltage")
    ax2.legend(loc="lower right", fontsize=9)

    plt.tight_layout()

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "solar_weather_iv_calculator.png"
    plt.savefig(target, dpi=300)
    print(f"[*] Visualized Solar Weather Calculator & I-V Curves: {target}")
    print(f"[*] Calculated Solar Maximum FWHM: {fwhm_duration:.2f} Years.")


# Quick inline helper to avoid importing scipy.signal just for one basic peak find if not needed
def scipy_find_peaks(arr):
    # Dummy implementation for simple smooth curves
    return [np.argmax(arr)], None


if __name__ == "__main__":
    generate_weather_calculator()
