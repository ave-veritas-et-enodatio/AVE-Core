import os
from pathlib import Path

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import (
    N_PHI_PACK as PHI_LIMIT,  # Axiom 1: V_I Solid (Kepler Conjecture Rigid Hexagonal FCC/HCP packing limit)
)

# --- AVE First-Principles Constants ---
PHI_AMBIENT = 0.6402  # V_II Fluid (Random Close Packing for uncompressed macroscopic polymer LC)

# Acoustic limits
Z_FLUID = 1.0  # Base acoustic impedance (normalized)
Z_DIAMOND = 10000.0  # Rigid crystal lattice impedance upon V_I structural snap

# FDTD Environmental Constants
NX = 500  # Number of spatial discrete nodes
NT = 800  # Number of temporal time-steps
DX = 1.0  # Spatial step
DT = 0.5  # Time step (Courant condition stable)

# Compressibility scale (How easily external pressure pushes nodes together)
COMPRESSIBILITY = 0.05


def simulate_kinetic_armor_yield():
    """
    1D Finite-Difference Time-Domain (FDTD) Acoustic Wave Propagation.
    Strictly simulates the AVE topological volume compression phase state jump.
    """

    print("Initiating AVE FDTD Topological Shockwave Solver...")
    print(f"Tracking Axiom 1 Compression Limit: Phi_max = {PHI_LIMIT:.5f}\n")

    # Grid initialization
    p = np.zeros(NX)  # Kinetic Pressure Wave (Gigapascals)
    v = np.zeros(NX)  # Lattice particle velocity
    phi = np.ones(NX) * PHI_AMBIENT  # Local topological packing fraction
    Z_local = np.ones(NX) * Z_FLUID  # Local Acoustic Impedance
    state = np.zeros(NX)  # Boolean array: 0 = Fluid(V_II), 1 = Solid(V_I)

    # Store history for visualization
    history_p = []
    history_phi = []
    history_Z = []

    # The Ballistic Impact: Inject an extreme massive pressure pulse
    # (resembling an armor-piercing kinetic shock) on the left boundary
    def source(t):
        if t < 40:
            return 3.0 * np.sin(np.pi * t / 40.0)  # High-kinetic Gaussian-like hit
        return 0.0

    impact_crystallizations = 0

    # FDTD Main Loop
    for t in range(NT):
        # 1. Update Particle Velocity (accelerated by pressure gradient)
        # Using updated spatial impedance
        for x in range(1, NX):
            # Acoustic Impedance interface averaging
            Z_interface = 0.5 * (Z_local[x] + Z_local[x - 1])
            v[x] -= (DT / (DX * Z_interface)) * (p[x] - p[x - 1])

        # 2. Update Pressure (compressed by velocity gradient)
        for x in range(0, NX - 1):
            # Base fluid restores pressure based on standard fluid bulk modulus
            # Here normalized proportionally to Z_FLUID initially
            bulk_modulus = Z_local[x]
            p[x] -= (bulk_modulus * DT / DX) * (v[x + 1] - v[x])

        # Inject boundary shock source
        p[5] += source(t)

        # 3. AVE Topological Engine (The First-Principles Map)
        for x in range(NX):
            # Local density/packing fraction increases proportionally with absolute local pressure
            # (Pressure pushes physical matter into a tighter spatial sphere geometry)
            current_phi = PHI_AMBIENT + (p[x] * COMPRESSIBILITY)

            # The Trigger Condition (Axiom 1)
            # You CANNOT compress space past Phi = 0.7405 without crystalline deformation
            if current_phi >= PHI_LIMIT:
                phi[x] = PHI_LIMIT  # Hard topological lock
                state[x] = 1  # Phase shift: V_II Fluid -> V_I Crystalline Diamond
                Z_local[x] = Z_DIAMOND  # Massive impedance spike
                impact_crystallizations += 1
            else:
                phi[x] = current_phi
                state[x] = 0  # Relax back to fluid if pressure wave drops
                Z_local[x] = Z_FLUID

        # Save snapshots at specific temporal logic gates
        snap_times = [50, 150, 450]
        if t in snap_times:
            history_p.append(p.copy())
            history_phi.append(phi.copy())
            history_Z.append(state.copy())  # Track state rather than raw Z to viz easily

    print(f"Total simulated dynamic crystallizations: {impact_crystallizations}")
    print("FDTD Engine Complete. Commencing dynamic topological reflection breakdown plot...\n")
    return history_p, history_phi, history_Z


def plot_kinetic_armor_reaction(history_p, history_phi, history_Z):
    """Plot the 3 stages: Ingress, Phase-Lock Reflection, and Relaxation"""

    # fig = plt.figure(figsize=(12, 9))  # bulk lint fixup pass
    gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 1])

    titles = [
        "1. Ingress: Kinetic Wave Overloads Baseline Fluid LC",
        "2. Phase-Lock: Target Node Hits $\phi=0.7405$; Triggers Total Reflection (Armor)",
        "3. Relaxation: Sub-Limit Pressure Recedes & Wave Scatters Outward",
    ]

    colors = ["#FF4444", "#00FFF0", "#88FF44"]

    x_axis = np.arange(NX)

    for i in range(3):
        ax = plt.subplot(gs[i])
        ax.set_facecolor("black")

        # Plot Pressure Profile
        ax.plot(
            x_axis,
            history_p[i],
            color=colors[i],
            linewidth=2.5,
            label="Kinetic Pressure Wave ($\Delta P$)",
        )
        ax.fill_between(x_axis, history_p[i], 0, color=colors[i], alpha=0.2)

        # Overlay the nodes that turned into Diamond V_I
        crystallized_nodes = np.where(history_Z[i] == 1)[0]
        for node in crystallized_nodes:
            ax.axvline(x=node, color="white", linewidth=1.5, alpha=0.8)

        if len(crystallized_nodes) > 0:
            ax.plot(
                [],
                [],
                color="white",
                linewidth=1.5,
                label="V_I Structural Snap ($\phi \geq 0.7405$, $Z \to \infty$)",
            )

        ax.set_title(titles[i], color="white", fontsize=12, fontweight="bold", loc="left")
        ax.set_xlim(0, 300)
        ax.set_ylim(-3, 4)
        ax.tick_params(colors="white")
        ax.grid(True, color="#333333", linestyle=":")

        if i == 0:
            ax.legend(loc="upper right", facecolor="black", edgecolor="white", labelcolor="white")
        if i == 2:
            ax.set_xlabel("Spatial Lattice Distance (Nodes)", color="white")

        for spine in ax.spines.values():
            spine.set_color("white")

    plt.tight_layout()
    plt.gcf().patch.set_facecolor("black")

    # Save Output Asset
    out_dir = Path(os.path.dirname(__file__)) / ".." / ".." / ".." / "assets" / "sim_outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "kinetic_armor_reflection.png"
    plt.savefig(out_path, dpi=300, facecolor="black")
    print(f"Asset successfully rendered to: {out_path}")


if __name__ == "__main__":
    hp, hphi, hz = simulate_kinetic_armor_yield()
    plot_kinetic_armor_reaction(hp, hphi, hz)
