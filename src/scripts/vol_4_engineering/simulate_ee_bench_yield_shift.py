"""
AVE Falsifiable Predictions: The EE Bench (Dielectric Yield Shift)
======================================================
This script models the most accessible, definitive benchtop falsification
of the AVE framework: The Macroscopic Dielectric Plateau.

Standard electromagnetism assumes the vacuum permittivity (epsilon_0) is a
constant, linear baseline. AVE dictates that the vacuum is a non-linear
structural lattice governed by a strict squared saturation operator limit
(Axiom 4), bounded fundamentally by the Fine Structure Constant (alpha).

The saturation kernel S(A) = sqrt(1 - (A/A_yield)^2) drives TWO observables:
  1. Constitutive permittivity epsilon_eff = epsilon_0 * S -> 0 (collapse)
  2. Observable capacitance C_eff = C_0 / S -> infinity (divergence)

The Experiment:
  - LCR meter: Sees C_eff SPIKE upward (anomalous capacitance increase)
  - Interferometer: Sees n ~ sqrt(S) DROP (loss of optical phase delay)
  Both are signatures of the same saturation phenomenon.
"""

import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()


def simulate_ee_bench_plateau():
    print("[*] Generating the EE Bench Dielectric Yield predictions...")

    # -------------------------------------------------------------
    # Experimental Parameters (Zero-Parameter Foundation)
    # -------------------------------------------------------------
    from ave.core.constants import ALPHA, C_0, L_NODE, M_E, e_charge

    # Absolute Localized Node Voltage Limit (derived dynamically)
    # V_node = (m_e * c^2) / e * sqrt(alpha) -> 43,653 Volts
    V_NODE_LIMIT = (M_E * C_0**2 / e_charge) * np.sqrt(ALPHA)

    # Macroscopic E-Field Saturation Limit (V/m)
    E_BREAKDOWN = V_NODE_LIMIT / L_NODE  # Approx 1.13e17 V/m

    # Sweep E-field from 0 to just past the yield limit
    e_fields = np.linspace(0, E_BREAKDOWN, 1000)

    # -------------------------------------------------------------
    # Theoretical Models
    # -------------------------------------------------------------
    # Standard Physics: Both C and n are dead flat (linear)
    standard_flat = np.ones_like(e_fields)

    # AVE: Universal Saturation Factor
    safe_e = np.clip(e_fields, 0, E_BREAKDOWN * 0.999)
    S = np.sqrt(1.0 - (safe_e / E_BREAKDOWN) ** 2)
    S[e_fields >= E_BREAKDOWN] = 0.01  # Clip at structural failure

    # Observable 1: Capacitance ratio C_eff/C_0 = 1/S -> SPIKES upward
    C_ratio = 1.0 / S
    C_ratio[e_fields >= E_BREAKDOWN] = 50.0  # Clip for visualization

    # Observable 2: Refractive index n ~ sqrt(epsilon_eff) = sqrt(eps_0*S) -> DROPS
    # Normalized: n/n_0 = S^(1/2)
    n_ratio = np.sqrt(S)

    # -------------------------------------------------------------
    # Rendering the Experimental Blueprints
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
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

    # Convert x-axis to 10^17 for readable plotting
    plot_e_fields = e_fields / 1e17
    plot_breakdown = E_BREAKDOWN / 1e17

    # Panel 1: LCR Meter — Observable Capacitance SPIKES
    ax1.plot(
        plot_e_fields,
        standard_flat,
        color="#ff3333",
        linestyle="--",
        lw=2,
        label="Standard EM (Linear)",
    )
    ax1.plot(
        plot_e_fields,
        C_ratio,
        color="#00ffcc",
        lw=3,
        label=r"AVE: $C_{eff}/C_0 = 1/\sqrt{1-(E/E_{yield})^2}$",
    )

    ax1.axvline(
        plot_breakdown,
        color="white",
        linestyle=":",
        lw=2,
        label=r"$E_{yield} \approx 1.13 \times 10^{17}$ V/m",
    )
    ax1.axvspan(
        plot_breakdown * 0.85,
        plot_breakdown,
        color="#ffff99",
        alpha=0.2,
        label="LCR Detectable Anomaly Window",
    )

    ax1.set_xlim([0, plot_breakdown * 1.05])
    ax1.set_ylim([0, 10])
    ax1.set_title("Benchtop LCR Sensor: Capacitance Spike vs E-Field")
    ax1.set_xlabel(r"Applied Macroscopic E-Field ($\times 10^{17}$ V/m)")
    ax1.set_ylabel(r"Observable Capacitance Ratio ($C_{meas} / C_0$)")
    ax1.legend(loc="upper left")

    # Panel 2: Interferometer — Refractive Index DROPS
    ax2.plot(
        plot_e_fields,
        standard_flat,
        color="#ff3333",
        linestyle="--",
        lw=2,
        label="Standard GR (Flat Optical Metric)",
    )
    ax2.plot(
        plot_e_fields,
        n_ratio,
        color="#ffcc00",
        lw=3,
        label=r"AVE: $n_{eff}/n_0 = (1-(E/E_{yield})^2)^{1/4}$",
    )

    ax2.axvline(plot_breakdown, color="white", linestyle=":", lw=2, label="Absolute Yield Limit")
    ax2.axvspan(
        plot_breakdown * 0.85,
        plot_breakdown,
        color="#ff99ff",
        alpha=0.2,
        label="Laser Phase Shift Window",
    )

    ax2.set_xlim([0, plot_breakdown * 1.05])
    ax2.set_ylim([0, 1.1])
    ax2.set_title("Interferometer Bench: Refractive Index Loss vs E-Field")
    ax2.set_xlabel(r"Applied Macroscopic E-Field ($\times 10^{17}$ V/m)")
    ax2.set_ylabel(r"Optical Phase Ratio ($n_{eff} / n_0$)")
    ax2.legend(loc="lower left")

    plt.tight_layout()

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "ee_bench_saturation_prediction.png"
    plt.savefig(target, dpi=300)
    print(f"[*] Visualized EE Bench Falsification Limits: {target}")


if __name__ == "__main__":
    simulate_ee_bench_plateau()
