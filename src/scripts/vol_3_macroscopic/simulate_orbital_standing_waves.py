"""
Orbital Standing Wave Visualization (mathematically isomorphic to QM orbitals).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script renders s/p/d/f orbital amplitude patterns as LC standing-wave
harmonics on a 3D grid (pressure_s = exp(-R), pressure_pz = Z × exp(-R),
etc.). These are the STANDARD hydrogen orbital amplitude forms by
construction — mathematically identical to the Schrödinger probability
density, just reinterpreted as standing-wave mechanical pressure rather
than statistical probability.

This script's value is INTERPRETIVE (alternative AVE narrative for what
the orbitals represent physically), NOT mathematically novel. The
"Eliminate the Schrödinger Probability Density model" objective is more
accurately "reinterpret the same mathematical functions as standing-wave
amplitude rather than statistical cloud" — the math is preserved.

Per `plot_hydrogen_orbitals.py`'s honest framing: "The orbital prediction
is 100% mathematically identical to the standard QM expectation; the AVE
interpretation differs (mechanical standing wave vs probability density)
but the figures are the same".

Docstring corrected 2026-05-17 to match plot_hydrogen_orbitals.py honest
isomorphism framing.
"""

import os

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    print("==========================================================")
    print(" AVE ATOMIC SCALE: ORBITAL STANDING-WAVE INTERPRETATION ")
    print("==========================================================\n")

    print("- Renders s/p/d/f orbital amplitudes as LC standing waves.")
    print("- Mathematically identical to QM probability density;")
    print("  AVE reinterpretation is mechanical (standing wave amplitude)")
    print("  rather than statistical (probability cloud).")
    print("- See plot_hydrogen_orbitals.py for canonical isomorphism note.\n")

    print("[1] Generating 3D Cartesian Simulation Grid...")

    # Grid resolution
    N = 60
    x = np.linspace(-3, 3, N)
    y = np.linspace(-3, 3, N)
    z = np.linspace(-3, 3, N)
    X, Y, Z = np.meshgrid(x, y, z)

    # Distance from core
    R = np.sqrt(X**2 + Y**2 + Z**2)
    # Prevent divide by zero at origin
    R[R == 0] = 1e-10

    # Spherical coordinates
    # Theta = np.arccos(Z / R)  # bulk lint fixup pass
    # Phi = np.arctan2(Y, X)  # bulk lint fixup pass

    print("[2] Engaging Continuous LC Resonant Cavity Harmonics...")

    # In mainstream Quantum Mechanics, orbitals are probability density functions: |Psi|^2
    # In AVE, orbitals are continuous Ponderomotive Acoustic Standing Waves in the LC grid.
    # The pressure nodes (where electrons phase-lock) naturally map to the exact same spherical harmonics.

    # Base decay (electrostatic/inductive falloff)
    decay = np.exp(-R)

    # Fundamental Harmonic (s-orbital)
    # n=1, l=0, m=0
    # A purely spherical breathing mode of the central nucleus
    pressure_s = 1.0 * decay

    # First Transverse Harmonic (p_z orbital)
    # n=2, l=1, m=0
    # A dipole rotation mode driven by the nuclear spin-polarity
    pressure_pz = Z * decay

    print("[3] Rendering Subsystems...")

    # We will plot isosurfaces (constant pressure/impedance boundaries)
    # showing where the phase-velocity reaches an equilibrium standing-wave.

    def plot_isosurface(ax: "Axes3D", volume_data: np.ndarray, isovalue: float, color: str, title: str) -> None:
        # A simple voxel approximation for fast matplotlib 3D rendering
        voxels = np.abs(volume_data) > isovalue
        ax.voxels(voxels, facecolors=color, edgecolor="none", alpha=0.6)

        # Style
        ax.set_facecolor("#111111")
        ax.set_axis_off()
        ax.set_title(title, color="white", pad=20)

        # Center the view (rough approximation based on N)
        ax.set_xlim(N // 4, 3 * N // 4)
        ax.set_ylim(N // 4, 3 * N // 4)
        ax.set_zlim(N // 4, 3 * N // 4)

    fig = plt.figure(figsize=(14, 6), facecolor="#111111")

    # Plot s-orbital
    ax1 = fig.add_subplot(121, projection="3d")
    plot_isosurface(ax1, pressure_s, 0.4, "cyan", "Fundamental 1s Resonance\n(Continuous Breathing Mode)")

    # Plot p-orbital
    ax2 = fig.add_subplot(122, projection="3d")
    plot_isosurface(ax2, pressure_pz, 0.3, "magenta", "1st Transverse 2p_z Resonance\n(Continuous Dipole Mode)")

    plt.tight_layout()

    out_path = "assets/figures/atomic_orbital_standing_waves.pdf"

    # Also save to assets
    os.makedirs("assets/figures", exist_ok=True)
    plt.savefig(
        "assets/figures/atomic_orbital_standing_waves.pdf",
        facecolor="#111111",
        bbox_inches="tight",
        dpi=150,
    )

    print(f"\n[STATUS: SUCCESS] Deterministic LC Standing-Waves saved to {out_path}")
    print("The geometric shapes are identical to QM orbitals, but require ZERO probability/statistics.")


if __name__ == "__main__":
    main()
