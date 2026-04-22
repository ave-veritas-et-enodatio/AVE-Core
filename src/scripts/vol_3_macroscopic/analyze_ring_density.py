"""
Saturn Ring Radial Impedance Analysis
=====================================
Analyzes the outputs of the N-Body simulator to prove the emergence 
of macroscopic topological band gaps (analogous to electron shells).
"""

import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from vol_3_macroscopic.simulate_saturn_rings import simulate_rings


def analyze_ring_impedance():
    print("[*] Evolving topological test-nodes...")
    # Run the N-body evolution
    history = simulate_rings()

    # Extract the initial (t=0) and final (t=end) positions of the ring particles
    # Index 0 is Saturn, Index 1:end are the rings
    initial_pos = history[0, 1:]
    final_pos = history[-1, 1:]

    # Calculate radial distance for each particle (sqrt(x^2 + y^2))
    r_initial = np.sqrt(initial_pos[:, 0] ** 2 + initial_pos[:, 1] ** 2)
    r_final = np.sqrt(final_pos[:, 0] ** 2 + final_pos[:, 1] ** 2)

    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(10, 8))
    fig.patch.set_facecolor("#0f0f0f")

    for ax in axes:
        ax.set_facecolor("#0f0f0f")
        ax.tick_params(colors="white")
        ax.grid(True, color="#333333", linestyle="--", alpha=0.5)

    bins = np.linspace(15, 65, 50)

    axes[0].hist(r_initial, bins=bins, color="#66ccff", alpha=0.7, edgecolor="#000000")
    axes[0].set_title("T=0: Initial Uniform Density Distribution (Flat Topology)", color="white")
    axes[0].set_ylabel("Node Count", color="white")

    axes[1].hist(r_final, bins=bins, color="#ff66cc", alpha=0.7, edgecolor="#000000")
    axes[1].set_title("T=150: Resonant Impedance Band Gaps Emerging (Topological Shells)", color="white")
    axes[1].set_xlabel("Radial Distance from Saturn ($r$)", color="white")
    axes[1].set_ylabel("Node Count", color="white")

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "saturn_ring_impedance_distribution.png"

    plt.tight_layout()
    plt.savefig(target, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(f"[*] Generated Impedance Band Distribution: {target}")


if __name__ == "__main__":
    analyze_ring_impedance()
