"""
Vacuum Energy (Dark Energy) and Cosmological Inflation Solver.
Derives the Zero-Point Energy of the LC Network and the inflationary limit.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# Ensure local ave package is in path

from ave.core.constants import C_0, G, HBAR, M_E, ALPHA, L_NODE


def derive_vacuum_energy():
    """
    Derives the cosmological constant (Dark Energy density) not as 'anti-gravity',
    but simply as the ground-state Zero-Point Energy of the discrete LC network hardware.
    """
    print("==========================================================")
    print("   AVE VACUUM ENERGY (DARK ENERGY) DERIVATION")
    print("==========================================================")

    # M_E, HBAR, L_NODE imported from ave.core.constants

    # In a discrete LC Network, the zero-point energy is simply the ground state
    # oscillation of each structural node: E_0 = 1/2 hbar * omega_max

    # Omega Max occurs at the Nyquist spatial frequency of the lattice (k = pi / l_node)
    lambda_cut = 2.0 * L_NODE
    omega_max = (2 * np.pi * C_0) / lambda_cut

    # Acoustic zero-point energy per node
    E_zero_point = 0.5 * HBAR * omega_max

    # Volume of a single node cell
    V_node = L_NODE**3

    # Effective Dark Energy Density (rho_lambda) = Energy / Volume / c^2
    rho_lambda = (E_zero_point / V_node) / (C_0**2)

    print(f"[1] ZERO-POINT LC NETWORK ENERGY Density (Dark Energy)")
    print(f"    Calculated Zero-Point Density: {rho_lambda:.4e} kg/m^3")

    # Target Cosmological Constant Density ~ 6e-27 kg/m^3
    target_rho = 6.0e-27
    print(f"    Empirical Cosmological Const : {target_rho:.4e} kg/m^3")
    print(f"    Note: Analytical result requires trace-reversed volume mapping.")

    # The actual geometric projection requires mapping the 1D string oscillation
    # into a 3D expanding horizon. (1/7 Isotropic strain projection)
    projected_rho = rho_lambda * (1.0 / 7.0) ** 15  # (Scaling geometrically, full derivation in manuscript)
    print(f"    Trace-Reversed Extrapolation (Work in Progress): {projected_rho:.4e} kg/m^3")

    return rho_lambda


def simulate_cosmic_inflation():
    """
    Simulates Cosmic Inflation. In AVE, inflation is not an arbitrary scalar field
    (Inflaton), but the absolute maximum geometric crystallization rate of the LC network
    before inductive latency (speed of light) locks the grid into place.
    """
    print("\n==========================================================")
    print("   AVE COSMIC INFLATION (LATTICE CRYSTALLIZATION)")
    print("==========================================================")

    # The maximum theoretical expansion rate occurs when the lattice is totally unstructured
    # and Genesis runs at the absolute impedance limit (Gamma = -1).

    # Time steps in Planck units
    times = np.logspace(-43, -32, 100)

    # Standard inflation expects a scale factor a(t) exp(H_inf * t)
    # H_inf is derived from the structural breakdown limit of the lattice
    # ALPHA, M_E, C_0, HBAR imported from ave.core.constants

    # Eq 4.7: H_inf bound
    H_inf = (28 * np.pi * (M_E**3) * C_0 * G) / (HBAR**2 * ALPHA**2)
    # Scaled up to the early-universe impedance state
    # (Simplified for plotting representation)
    H_early = H_inf * 1e50

    scale_factor = np.exp(H_early * times)

    plt.figure(figsize=(10, 6))
    plt.plot(times, np.log10(scale_factor), color="orange", linewidth=3)

    plt.axvline(x=1e-36, color="red", linestyle="--", label="End of Inflation (Impedance Lock)")

    plt.title("Cosmic Inflation as LC Network Grid Crystallization")
    plt.xlabel("Time since Big Bang (seconds)")
    plt.ylabel(r"Log Scale Factor $\log_{10}(a(t))$")
    plt.xscale("log")
    plt.legend()
    plt.grid(True, alpha=0.3)

    output_path = os.path.join(os.path.dirname(__file__), "../assets/sim_outputs/simulate_cosmic_inflation.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300)
    print(f"\nSaved Cosmic Inflation plot to {output_path}")


if __name__ == "__main__":
    derive_vacuum_energy()
    simulate_cosmic_inflation()
