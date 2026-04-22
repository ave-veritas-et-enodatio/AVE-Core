#!/usr/bin/env python3
"""
simulate_orbital_penetration.py
===============================

Proves that orbital penetration (e.g. 2s penetrating the 1s core, lowering its energy)
is not a probabilistic Quantum Mechanical phenomenon, but a deterministic
macroscopic LC spatial resonance constraint.

The 2s state (l=0) natively intersects the inner 1s shell geometry.
The Op3 impedance step (a 1/d boundary condition) perfectly breaks the l-degeneracy,
separating the 2s and 2p energies without any statistical Born-rule interpretation.
"""

from pathlib import Path

import matplotlib.pyplot as plt

from ave.solvers.radial_eigenvalue import radial_eigenvalue_abcd

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").is_dir())
OUT = PROJECT_ROOT / "assets/sim_outputs"
OUT.mkdir(exist_ok=True, parents=True)


def main() -> None:
    print("=========================================================================")
    print("  Deterministic Derivation of Orbital Penetration via Impedance Mismatch")
    print("=========================================================================")

    Z = 3  # Lithium
    n = 2  # Valence shell
    shells = [(1, 2)]  # 1s^2 inner core

    print("\nSimulating Lithium (Z=3) Valence Shell Eigenmodes [ABCD Cascade Solver]...")

    # Calculate 2s (l=0)
    # The ABCD solver internally computes the `_crossing_abcd` shunt admittance penalty
    # for the l=0 orbital piercing the l=0 inner shell.
    energy_2s_eV = radial_eigenvalue_abcd(Z, n, 0, shells)

    # Calculate 2p (l=1)
    # Since l=1 natively carries a centrifugal boundary barrier, it does not
    # pierce the inner core geometrically, bypassing the Op3 shunt admittance.
    energy_2p_eV = radial_eigenvalue_abcd(Z, n, 1, shells)

    print("\nResults:")
    print(f"  2s Binding Energy (l=0): {energy_2s_eV:.4f} eV")
    print(f"  2p Binding Energy (l=1): {energy_2p_eV:.4f} eV")

    delta_E = energy_2s_eV - energy_2p_eV
    print(f"\nTopological l-Degeneracy Splitting (1/d Penetration Penalty): {delta_E:.4f} eV")

    # Visualization
    fig, ax = plt.subplots(figsize=(8, 6), facecolor="#050510")
    ax.set_facecolor("#050510")

    states = ["2s (l=0)\n$p$-penetrating", "2p (l=1)\nCore-blocked"]
    energies = [energy_2s_eV, energy_2p_eV]

    bars = ax.bar(states, energies, color=["#00ffcc", "#ff6699"], width=0.5)

    ax.set_ylabel("Binding Energy (eV)", color="white", fontsize=12)
    ax.set_title("Deterministic Orbital Penetration (Lithium Z=3)", color="white", fontsize=14, pad=20)
    ax.tick_params(colors="white", labelsize=11)
    for s in ax.spines.values():
        s.set_color("#333333")

    for bar in bars:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 0.1,
            f"{yval:.2f} eV",
            ha="center",
            va="bottom",
            color="white",
            fontweight="bold",
            fontsize=12,
        )

    ax.text(
        0.5,
        max(energies) * 0.5,
        f"$\Delta E$ Splitting: {delta_E:.2f} eV\nDerived entirely from 1/d\nAcoustic Reflection Limits",
        ha="center",
        va="center",
        color="white",
        fontsize=11,
        bbox=dict(facecolor="#222233", edgecolor="#00ffcc", alpha=0.8, pad=10),
    )

    out_path = OUT / "lithium_penetration_splitting.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, facecolor=fig.get_facecolor())
    print(f"\nSaved visualization to: {out_path}")


if __name__ == "__main__":
    main()
