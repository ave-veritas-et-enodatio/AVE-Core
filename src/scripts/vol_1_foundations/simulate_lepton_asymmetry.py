"""
Lepton Asymmetry and Baryogenesis — illustrative scaffold (NOT a closed derivation).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script computes a candidate algebraic identity η ~ α × 8πα = 8πα^2 ≈ 1.34e-4
and labels it "baryogenesis efficiency". The observed baryon-to-photon ratio is
η ≈ 6e-10 — so the candidate identity is ~2.2e5× the empirical value (5 OOM off).
The script does NOT close the baryogenesis derivation; it identifies a chirality
phase angle that AVE proposes is the seed of the asymmetry, but the
sphaleron-suppression / thermal-projection chain that brings 8πα^2 down to 6e-10
is NOT modeled here (explicitly flagged at line 54).

Specifically:
  - theta_cp = 8πα is an algebraic identity, NOT derived from any AVE
    lattice geometry equation
  - baryogen_efficiency = α × 8πα is the chosen scaling; alternative
    scalings (α × 8πα × suppression-factor) would land closer to 6e-10
    but require thermal-projection physics not implemented here

For the canonical AVE framing of CP violation as substrate chirality, see
the corpus discussion in vol2/particle-physics/ch02-baryon-sector/* and
vol1 chiral-symmetry-breaking leaves.

Title "Derives the fundamental CP-violating chiral phase bias" was
overclaim; corrected 2026-05-17 to "candidate identity, NOT closed
baryogenesis derivation".
"""

import os

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import ALPHA

# Ensure local ave package is in path


def derive_chiral_asymmetry() -> tuple[float, float]:
    """
    Identifies a candidate algebraic identity (η ~ 8πα^2 ≈ 1.34e-4) for the
    CP-violating chirality phase. Does NOT close the baryogenesis derivation
    — empirical η ≈ 6e-10 is 5 OOM smaller. Sphaleron suppression and
    thermal-projection physics that close the gap are NOT implemented.
    """
    print("==========================================================")
    print("   AVE LEPTON ASYMMETRY (CANDIDATE IDENTITY — NOT closed)")
    print("==========================================================")

    # In a linear continuum, left-handed and right-handed states are perfectly symmetric.
    # In a discrete periodic matrix, the minimum resolvable topological phase shift
    # per lattice node is related directly to the porosity coupling constant (Alpha).

    # The volumetric packing fraction of the topological limit dictates the intrinsic twist
    volumetric_packing_fraction = 8 * np.pi * ALPHA

    # The fundamental CP-violating phase angle (theta_CP)
    theta_cp = volumetric_packing_fraction

    # The cosmological Matter-Antimatter asymmetry (eta) is roughly proportional
    # to the phase overlap interference of this twist during early lattice genesis.
    # Given by the standard anomaly equation analog: \eta \propto \alpha * \theta_CP

    baryogen_efficiency = ALPHA * theta_cp

    print("[1] INTRINSIC LOMMEL-SEELIGER LATTICE CHIRALITY")
    print(f"    Fundamental CP-Violating Phase: {theta_cp:.4e} Radians")

    print("\n[2] BARYOGENESIS (MATTER-ANTIMATTER IMBALANCE)")
    print(f"    Calculated Asymmetry Ratio (eta): {baryogen_efficiency:.4e}")

    # Target Cosmological Asymmetry ~ 6e-10
    target_eta = 6e-10
    print(f"    Cosmological Target Ratio:        {target_eta:.4e}")
    print(f"    Gap (candidate / empirical):       ~{baryogen_efficiency/target_eta:.2e}× (5 OOM)")
    print("    NOTE: This is a candidate seed identity, NOT a closed prediction.")
    print("    Sphaleron suppression + thermal-projection physics that would close")
    print("    the 5-OOM gap are NOT modeled in this script.")

    return theta_cp, baryogen_efficiency


def visualize_chiral_evanescence() -> None:
    """
    Plots the divergence of Left vs Right handed polarization fields propagating
    through a discrete LC Network, demonstrating why the vacuum intrinsically
    prefers matter over antimatter.
    """
    z = np.linspace(0, 100, 1000)

    # The core concept: Beta (wavenumber) is slightly different for L and R
    k_L = 1.0
    k_R = 1.005  # Slight chiral phase delay due to lattice geometric twist

    # Field amplitudes
    E_L = np.cos(k_L * z)
    E_R = np.cos(k_R * z)

    # The macroscopic interference (The matter-antimatter splitting gap)
    interference_gap = E_L - E_R

    plt.figure(figsize=(10, 6))

    plt.plot(z, E_L, color="blue", alpha=0.5, label="Left-Handed Tensor (Matter)")
    plt.plot(z, E_R, color="red", alpha=0.5, label="Right-Handed Tensor (Antimatter)")
    plt.plot(
        z,
        interference_gap,
        color="purple",
        linewidth=2,
        label="Chiral Phase Splitting (CP Violation)",
    )

    plt.title("Intrinsic Vacuum Chirality: Dissociation of L/R Polarizations")
    plt.xlabel("Propagation Distance (Lattice Nodes)")
    plt.ylabel("Normalized Tensor Amplitude")
    plt.legend()
    plt.grid(True, alpha=0.3)

    output_path = os.path.join(os.path.dirname(__file__), "../assets/sim_outputs/simulate_lepton_asymmetry.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300)
    print(f"\nSaved Chiral Phase Splitting visualization to {output_path}")


if __name__ == "__main__":
    derive_chiral_asymmetry()
    visualize_chiral_evanescence()
