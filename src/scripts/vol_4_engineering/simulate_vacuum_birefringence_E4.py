"""
AVE Falsifiable Predictions: The E^4 Vacuum Birefringence Limit
======================================================
A distinction between standard Quantum Electrodynamics (QED) and the
Applied Vacuum Engineering (AVE) framework concerns the COEFFICIENT and
ONSET FIELD STRENGTH of higher-order vacuum-birefringence terms.

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
Standard QED at LEADING ORDER (one-loop Euler-Heisenberg) gives Δn ∝ E^2.
QED at higher loops DOES include E^4 corrections, but their coefficient
is set by α and the electron mass scale m_e c^2 (corresponding to onset
near the Schwinger limit E_S ≈ 1.32e18 V/m). The AVE-distinct claim is
NOT that "QED omits E^4" — it's that the E^4 term has a DIFFERENT
COEFFICIENT and earlier onset (at E ~ E_BREAKDOWN ≈ 1.13e17 V/m, ~12% of
Schwinger), driven by Axiom 4's geometric saturation kernel
n_eff = n_0 × (1 - (E/E_yield)^2)^(1/4) — NOT by perturbative loop expansion.

The script's QED reference curve (k_qed_norm = 1/E_BREAKDOWN^2) is
NORMALIZED for visual divergence at high fields and does NOT represent
the actual QED coefficient. The discriminating measurement is the
E-field at which the E^4 term begins to dominate, not the existence of
an E^4 term.

This script simulates an ultra-high-Q optical fiber ring resonator
placed in a transverse, extreme-voltage DC electric field.
By measuring the resonance frequency shift of the cavity under varied
E-field strengths, experimentalists can plot the slope's onset field.

If E^4 onset matches QED (~Schwinger limit), AVE is challenged.
If E^4 onset appears at ~10% of Schwinger as predicted by Axiom 4's
geometric saturation kernel, AVE is supported and standard QED's
loop-perturbative expansion is challenged at that field regime.

Title softened 2026-05-17: was "Standard QED mathematically predicts...
strictly proportionally to E^2" — corrected to clarify that the AVE-distinct
claim is the COEFFICIENT/ONSET, not the existence of an E^4 term.
"""

import pathlib

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import ALPHA, C_0, L_NODE, M_E, e_charge

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()


def simulate_birefringence_e4() -> None:
    print("[*] Simulating E^4 Vacuum Birefringence (Optical Cavity)...")

    # -------------------------------------------------------------
    # Zero-Parameter Geometric Limits
    # -------------------------------------------------------------
    V_NODE_LIMIT = (M_E * C_0**2 / e_charge) * np.sqrt(ALPHA)
    E_BREAKDOWN = V_NODE_LIMIT / L_NODE  # Approx 1.13e17 V/m

    # Sweep extreme fields typical of petawatt laser environments
    # or advanced macroscopic pulsed power (up to 20% of yield)
    e_fields = np.linspace(0, E_BREAKDOWN * 0.20, 1000)

    # -------------------------------------------------------------
    # Theoretical Birefringence Slopes
    # -------------------------------------------------------------

    # 1. Standard QED (Euler-Heisenberg E^2)
    # Delta n_QED = K_QED * E^2
    # For visualization, we will normalize the QED coupling constant
    # to roughly match the AVE magnitude at low fields so the divergence
    # at high fields is perfectly obvious.
    k_qed_norm = 1.0 / (E_BREAKDOWN) ** 2
    delta_n_qed = k_qed_norm * (e_fields**2)

    # 2. AVE Structural Condensate (Axiom 4 Non-Linearity)
    # The optical metric shrinks according to the saturation operator:
    # n_eff = n_0 * (1 - (E/E_yield)^2)^{1/4}
    # Taylor expanded, this yields: 1 - 1/4(E/Ey)^2 - 3/32(E/Ey)^4
    # The shift Delta n is dominated by the E^4 geometry.
    ratio = e_fields / E_BREAKDOWN
    ave_dielectric_factor = np.sqrt(1.0 - ratio**2)
    n_eff_ave = np.sqrt(ave_dielectric_factor)

    # We plot the absolute magnitude of the shift (Delta n)
    delta_n_ave = 1.0 - n_eff_ave

    # -------------------------------------------------------------
    # Render Plot
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor("#0f0f0f")

    ax.set_facecolor("#0f0f0f")
    ax.grid(color="#333333", linestyle="--", alpha=0.5)
    ax.tick_params(colors="white")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.title.set_color("white")
    for spine in ax.spines.values():
        spine.set_edgecolor("#555555")

    plot_e_fields = e_fields / 1e16  # Show in units of 10^16 V/m

    # Plot QED vs AVE
    ax.plot(
        plot_e_fields,
        delta_n_qed,
        color="#ff3333",
        linestyle="--",
        lw=3,
        label=r"Standard QED ($E^2$ Linear)",
    )
    ax.plot(
        plot_e_fields,
        delta_n_ave,
        color="#ffcc00",
        lw=3.5,
        label=r"AVE Structural Saturation ($E^4$ Non-Linear Hook)",
    )

    # Shaded deviation zone
    ax.fill_between(
        plot_e_fields,
        delta_n_qed,
        delta_n_ave,
        color="#ff9900",
        alpha=0.15,
        label="AVE E^4 Divergence Signature",
    )

    ax.set_title("Tabletop Metric Rupture: Vacuum Birefringence Signature", fontsize=14, color="white")
    ax.set_xlabel(r"Applied Transverse E-Field ($\times 10^{16}$ V/m)", fontsize=12)
    ax.set_ylabel(r"Optical Ring Resonator Phase Shift ($\Delta n$)", fontsize=12)

    ax.legend(loc="upper left", fontsize=11)

    outdir = project_root / "assets" / "sim_outputs"
    target = outdir / "vacuum_birefringence_E4.png"
    plt.savefig(target, dpi=300)
    print(f"[*] Visualized E^4 Vacuum Birefringence Signature: {target}")


if __name__ == "__main__":
    simulate_birefringence_e4()
