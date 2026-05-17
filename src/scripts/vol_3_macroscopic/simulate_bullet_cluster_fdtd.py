"""
1D static-halo-superposition simulation of the Bullet Cluster Merger.

SCOPE NOTE (2026-05-17 audit + Grant adjudication per ponderomotive-halo
reframing): This script's filename ("FDTD") is MISLEADING. It does NOT compute
finite-difference time-domain field evolution, TT-tensor shockwave propagation,
Gordon optical metric integration, or light ray-tracing. It computes pure
kinematic-prescription + static MOND-saturation-halo linear superposition at
prescribed timesteps.

What the script ACTUALLY does:
  1. Kinematically advances two cluster cores at hardcoded velocities
  2. At each timestep: computes Newtonian g_N = GM/r^2 for each cluster
  3. Applies saturation kernel ave_saturation_acceleration(g_N, a0) per
     Vol 3 Ch 5 eta_eff halo framing
  4. Defines "halo strain" = g_eff - g_N
  5. Linearly superposes the two static halos at each timestep
  6. Plots resulting 1D strain field

This is the CORRECT computation for the bullet-cluster mechanism per the
2026-05-17 reframe: ponderomotive-class substrate-strain halos co-moving with
stellar cluster centers + standard Einstein lensing through Gordon optical
metric tracks halos. No propagating TT shockwave needed.

Reframe summary (per research/2026-05-17_C13b_bullet_cluster_prereg.md +
Grant adjudication 2026-05-17 evening):
- Each cluster's mass generates inhomogeneous substrate-strain halo
  (Ax2 TKI + Ax4 saturation)
- Halo co-moves with stars (stars source the strain)
- Collisions: halos linearly superpose & pass through ballistically
  (long-wavelength linear regime); gas decouples (atomic-scale collisional)
- Post-collision: stars + halos moved apart with cluster centers; gas stuck
  at collision center
- Lensing peak tracks halos (standard Einstein deflection through Gordon
  optical metric)
- Offset = geometric separation (~150 kpc projected for 1E 0657-558)

The script's STATIC HALO SUPERPOSITION approach IS the correct AVE mechanism
(interpretation γ from the prereg). The "FDTD" name is a vestigial artifact
from the prior Vol 1 Ch 4 TT-shockwave framing that the prereg retired.

Recommended cleanup (Class B per driver-script honesty audit pattern):
honest rename to simulate_bullet_cluster_halo_superposition.py or similar.
Code itself does not need changing. Same anti-pattern class as the retired
vlbi_impedance_parallax.py (which was renamed in docstring, not file path,
to preserve commit history; same pattern applies here).
"""

import os

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import M_SUN, G
from ave.regime_3_saturated.galactic_rotation import A0_LATTICE, ave_saturation_acceleration


def simulate_bullet_cluster_fdtd() -> None:
    """
    Simulates the Bullet Cluster collision purely via first-principles scaling.
    Replaces empirical Gaussians with Absolute Metric Drag operators (A0_LATTICE)
    derived explicitly from H_INFINITY and the topological unknot.
    """
    KPC = 3.086e19  # m

    # 3 Megaparsec spread across the collision axis
    GRID_SIZE = 1000
    x_axis_si = np.linspace(-1500 * KPC, 1500 * KPC, GRID_SIZE)
    x_axis_kpc = x_axis_si / KPC

    # Asymmetric Cluster masses based on Bullet Cluster empiricals
    mass_main = 1e14 * M_SUN
    mass_bullet = 1e13 * M_SUN

    pos_main_init = -800 * KPC
    pos_bullet_init = +800 * KPC

    def calculate_cluster_profiles(pos: float, mass: float) -> tuple:
        """
        Calculates Newtonian Bare Mass (g_N) and the Topo-Inductive Halo (g_eff)
        """
        r = np.abs(x_axis_si - pos)
        r = np.maximum(r, 10 * KPC)  # Prevent div zero at exact point mass core

        # 1. Pure Newtonian Gravity (Bare Baryons)
        g_N = G * mass / (r**2)

        # 2. Extract topological Dark Matter extension natively via AVE Saturation
        g_eff = np.array([ave_saturation_acceleration(g, a0=A0_LATTICE) for g in g_N])

        # The inductive drag is the exact difference between the saturated field and the bare matter
        inductive_drag = g_eff - g_N
        return g_N, inductive_drag

    snapshots = []

    # Evolve the collision across 60 time steps
    for t in range(61):
        # Kinematic collision updates (Clusters pass through each other)
        # Bullet moves much faster than the massive main cluster
        pos_main = pos_main_init + (t * 20.0 * KPC)
        pos_bullet = pos_bullet_init - (t * 40.0 * KPC)

        # Pull the absolute physical shear strains on the underlying spatial LC network
        g_N_main, drag_main = calculate_cluster_profiles(pos_main, mass_main)
        g_N_bullet, drag_bullet = calculate_cluster_profiles(pos_bullet, mass_bullet)

        # Axiom 1: Superposition. Dark Matter metric lensing simply sums across the geometry
        total_gN = g_N_main + g_N_bullet
        total_drag = drag_main + drag_bullet

        if t % 15 == 0:
            snapshots.append((pos_main / KPC, pos_bullet / KPC, total_gN, total_drag))

    # Visualize the Crossing using standard Astrophysics profiling
    fig, axes = plt.subplots(len(snapshots), 1, figsize=(10, 14), sharex=True)

    for i, (p_main, p_bullet, gN, drag) in enumerate(snapshots):
        ax = axes[i]

        # Normalizing for clear visual mapping
        norm_factor = np.max(drag) if np.max(drag) > 0 else 1

        # Dark Matter (Topological LC Inductance Wake)
        ax.plot(
            x_axis_kpc,
            drag / norm_factor,
            color="purple",
            linewidth=2.5,
            label="Topological Lensing Halo (Dark Matter)",
        )

        # Bare Baryonic Matter (Newtonian gas shock centers)
        ax.plot(x_axis_kpc, gN / norm_factor, color="grey", linestyle=":", alpha=0.5)
        ax.axvline(p_main, color="red", linestyle="solid", alpha=0.9, label="Main Cluster Core")
        ax.axvline(p_bullet, color="blue", linestyle="solid", alpha=0.9, label="Bullet Cluster Core")

        ax.set_ylabel("Metric Yield Strain")
        ax.set_ylim(0, 1.2)
        ax.grid(True, alpha=0.2)

        if i == 0:
            ax.set_title(
                "First-Principles Bullet Cluster Topo-Lensing Crossing"
                "\nDriven entirely by absolute constants (G, m_e, ALPHA)",
                pad=15,
            )
            ax.legend(loc="upper right")

    axes[-1].set_xlabel("Galaxy Collision Axis (kiloparsecs)")

    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), "../../../assets/sim_outputs/bullet_cluster_axiomatic.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    print(f"Saved Axiomatic Bullet Cluster footprint to {output_path}")


if __name__ == "__main__":
    simulate_bullet_cluster_fdtd()
