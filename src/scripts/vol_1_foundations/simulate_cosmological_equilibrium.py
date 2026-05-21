"""
AVE Framework: Cosmological Equilibrium Visualization (illustrative — NOT a derivation driver).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script visualizes the AVE narrative that H(t) settles to a steady-state
H_∞ ≈ 69.32 km/s/Mpc via thermodynamic equilibrium between latent-heat
generation and holographic boundary cooling. The H_∞ = 69.32 value is a
HARDCODED LITERAL (line 46) sourced from the canonical derivation in
`simulate_cosmology_bao.py` which computes H_0 = 28π × M_E^3 × C_0 × G /
(ℏ^2 α^2). This script does NOT re-derive that value — it plots a
phenomenological exponential approach `H(t) = H_∞ × (1 − exp(−t))` for
pedagogical illustration.

Specifically:
  - H_baseline = 69.32 is a literal (NOT computed here)
  - The exponential approach curve is phenomenological (NOT axiom-derived)
  - G_normalized(t) is a normalized illustration, not a G derivation

For the actual AVE derivation of H_0 and G, see:
  - simulate_cosmology_bao.py (zero-parameter derivation chain)
  - simulate_vacuum_mirror.py (G from K=2G operating point)

Title "Deriving Macroscopic Gravity (G)" was misleading; corrected to
"Cosmological Equilibrium Visualization" 2026-05-17. The narrative still
serves the manuscript's pedagogical purpose, with honest scope.
"""

import os

import matplotlib.pyplot as plt
import numpy as np


def simulate_cosmological_equilibrium() -> None:
    """
    Simulates the heat equation of the expanding lattice.
    Latent heat generation scales with Volume (R^3).
    Boundary radiation cooling scales with Surface Area (R^2) or Holographic bounds (R).
    The universe accelerates until these two curves intersect, determining the
    permanent cosmological horizon R_H, which in turn fixes G.
    """
    print("==========================================================")
    print("   AVE FRAMEWORK: COSMOLOGICAL EQUILIBRIUM VISUALIZATION   ")
    print("   (illustrative — H_∞ literal from simulate_cosmology_bao)")
    print("==========================================================")

    # 1. Theoretical Setup
    # Generative Cosmology defines expansion as state-change (crystallization).
    # Power generated P_gen = k_g * d(Volume)/dt
    # Power radiated P_cool = k_c * Surface_Area

    # Using arbitrary structural units to demonstrate the algebraic intersection
    # where the derivative of expansion becomes zero (Steady State limit)

    time_steps = np.linspace(0.1, 10.0, 500)

    # Phenomenological model of latent heat thermal back-pressure
    # Early universe: high temperature, slow crystallization
    # Late universe: cold, fast crystallization approaching equilibrium

    # Expansion Rate (Hubble Parameter H)
    # Starts low (CMB phase), accelerates, then asymptotes to H_infinity
    # H_baseline literal (NOT computed here) — sourced from canonical derivation in
    # simulate_cosmology_bao.py: H_0 = 28π × M_E^3 × C_0 × G / (ℏ^2 α^2) ≈ 69.32 km/s/Mpc.
    H_baseline = 69.32

    # Modeled acceleration curve based on thermodynamic cooling
    H_t = H_baseline * (1.0 - np.exp(-time_steps))

    # The effective measured G is inversely proportional to the expansion boundary
    # G_eff(t) = c^3 / (M_universe * H_t)
    # Here we plot the normalized stabilization of the geometric tensor
    G_normalized = 1.0 / (1.0 - 0.9 * np.exp(-time_steps))

    print("Plotting phenomenological approach to thermodynamic equilibrium...")
    print(f"H_∞ literal (from simulate_cosmology_bao.py): {H_baseline} km/s/Mpc")
    print("(Canonical AVE claim: equilibrium R_H fixes G via G = c^3/(M_universe·H_∞);")
    print("  G-derivation chain lives in simulate_cosmology_bao.py + simulate_vacuum_mirror.py)")

    # 2. Visualization
    plt.style.use("dark_background")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # ----- Plot 1: The Hubble Acceleration to Equilibrium -----
    ax1.plot(time_steps, H_t, color="magenta", linewidth=3, label="Topological Genesis Rate $H(t)$")
    ax1.axhline(
        H_baseline,
        color="white",
        linestyle="--",
        label="Thermodynamic Limit ($H_0 \\approx 69.32$)",
    )

    ax1.set_title("Cosmological Acceleration to Latent Heat Equilibrium", fontsize=14)
    ax1.set_xlabel("Cosmological Time (Arbitrary Units)")
    ax1.set_ylabel("Expansion Rate $H(t)$")
    ax1.legend()
    ax1.grid(True, alpha=0.2)

    # ----- Plot 2: The Stabilization of Macroscopic G -----
    ax2.plot(
        time_steps,
        G_normalized,
        color="gold",
        linewidth=3,
        label="Effective Macroscopic Tensor $G(t)$",
    )
    ax2.axhline(1.0, color="white", linestyle="--", label="Present Day Fundamental Constant ($G_0$)")

    ax2.set_title("Stabilization of the Gravitational Coupling Constant", fontsize=14)
    ax2.set_xlabel("Cosmological Time (Arbitrary Units)")
    ax2.set_ylabel("Normalized Gravitational Constant")
    ax2.legend()
    ax2.grid(True, alpha=0.2)

    plt.tight_layout()

    # Save the output
    output_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../assets/sim_outputs/simulate_cosmological_equilibrium.png")
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor())

    print(f"\nSaved cosmological equilibrium plot to {output_path}")
    print("\nNOTE: Plot is illustrative — H_∞ is a literal from simulate_cosmology_bao.py;")
    print("approach curve is phenomenological. G(t) is normalized for visual comparison,")
    print("not derived. The underlying AVE claim (G = c^3/(M_universe·H_∞), equilibrium")
    print("between latent-heat generation and holographic boundary cooling) is canonical.")


if __name__ == "__main__":
    simulate_cosmological_equilibrium()
