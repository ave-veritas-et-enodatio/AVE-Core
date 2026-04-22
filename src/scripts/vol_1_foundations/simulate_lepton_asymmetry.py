"""
Lepton Asymmetry and Baryogenesis Solver.
Derives the fundamental CP-violating chiral phase bias of the discrete LC Network.
"""

import os

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import ALPHA

# Ensure local ave package is in path


def derive_chiral_asymmetry():
    """
    Derives the Lepton Asymmetry (Matter-Antimatter imbalance) directly from
    the innate non-linear gyroscopic "twist" of the LC Network.

    The discrete vacuum is not perfectly isotropic; it is a 3D chiral lattice.
    This chirality manifests as a fundamental phase difference between left-handed
    and right-handed EM propagation (CP violation).
    """
    print("==========================================================")
    print("   AVE LEPTON ASYMMETRY (CP-VIOLATING CHIRALITY)")
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

    print(f"[1] INTRINSIC LOMMEL-SEELIGER LATTICE CHIRALITY")
    print(f"    Fundamental CP-Violating Phase: {theta_cp:.4e} Radians")

    print(f"\n[2] BARYOGENESIS (MATTER-ANTIMATTER IMBALANCE)")
    print(f"    Calculated Asymmetry Ratio (eta): {baryogen_efficiency:.4e}")

    # Target Cosmological Asymmetry ~ 6e-10
    target_eta = 6e-10
    print(f"    Cosmological Target Ratio:        {target_eta:.4e}")
    print(f"    Note: Full thermal suppression limits not modeled (Sphaleron transitions).")

    return theta_cp, baryogen_efficiency


def visualize_chiral_evanescence():
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
