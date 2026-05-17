"""
AVE Cosmology: JWST Early Galaxy Accretion — illustrative N-body (hand-tuned coupling).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script runs side-by-side N-body simulations with HAND-TUNED force
constants (G_NEWTON = 0.5, AVE_INDUCTANCE = 2.5 — arbitrary units, chosen
for visual contrast). It does NOT compute:
  - Absolute galaxy mass-growth rates calibrated to JWST z>10 observations
  - The AVE-derived τ_ind = 65.1 Myr inductive herding timescale
    (that derivation lives in `manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex:112`,
    τ_ind = 150 / ln(10) ≈ 65.1 Myr; not used in this driver script)
  - Comparison against specific JWST objects (JADES, CEERS, etc.)

The script's visual contrast between exponential herding and power-law
collisionless growth IS the AVE interpretive narrative. The original
docstring's claim that the simulation "perfectly resolves the JWST paradox"
overclaims — the coupling ratio AVE_INDUCTANCE/G_NEWTON = 5 was chosen to
make the divergence visible, not derived from canonical AVE constants.

For the quantitative AVE-distinct JWST prediction (τ_ind = 65.1 Myr,
M(t) = M_seed × exp(t/τ_ind)), see `plot_jwst_accretion.py` which plots
the actual derived curve against JWST empirical data points.

Docstring corrected 2026-05-17.
"""

import os
import pathlib

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist

project_root = pathlib.Path(__file__).parent.parent.absolute()

# JAX GPU acceleration (graceful fallback to numpy)
try:
    import jax

    jax.config.update("jax_enable_x64", True)
    _HAS_JAX = True
except ImportError:
    _HAS_JAX = False

# Simulation Parameters
N_PARTICLES = 250
BOX_SIZE = 100.0
DT = 0.02
FRAMES = 250

# Force Constants
G_NEWTON = 0.5  # Standard inverse-square gravity
AVE_INDUCTANCE = 2.5  # Macroscopic inductive drag herding


def initialize_gas_cloud() -> tuple[np.ndarray, np.ndarray]:
    """Generates a uniform, diffuse primordial gas cloud footprint."""
    np.random.seed(int("137"))  # Fine structure seed for consistency
    pos = np.random.uniform(-BOX_SIZE / 2, BOX_SIZE / 2, size=(N_PARTICLES, 2))
    vel = np.random.normal(0, 0.5, size=(N_PARTICLES, 2))
    return pos, vel


def compute_newtonian_accelerations(pos: np.ndarray) -> np.ndarray:
    """Standard Lambda-CDM 1/r^2 collisionless gravity — fully vectorized."""
    epsilon = 2.0
    # r_vec[i,j] = pos[j] - pos[i]  shape: (N, N, 2)
    r_vec = pos[np.newaxis, :, :] - pos[:, np.newaxis, :]
    dist_sq = np.sum(r_vec**2, axis=2) + epsilon**2
    dist = np.sqrt(dist_sq)
    # F = G / r^2
    f_mag = G_NEWTON / (dist**2)
    np.fill_diagonal(f_mag, 0.0)
    # acc[i] = sum_j( f_mag[i,j] * (r_vec[i,j] / dist[i,j]) )
    acc = np.sum(f_mag[:, :, np.newaxis] * (r_vec / dist[:, :, np.newaxis]), axis=1)
    return acc


def compute_ave_accelerations(pos: np.ndarray, vel: np.ndarray) -> np.ndarray:
    """
    AVE Cosmology: Macroscopic Inductive Tracking.
    In addition to weak 1/r^2 gravity, the structured vacuum acts as a
    viscous LC network at large unbroken scales (Dark Matter effect).
    Dense clumps of matter locally lower the impedance, creating an attractive
    'slipstream' that exponentially herds nearby particles inward.
    """
    # 1. Base Newtonian Gravity (vectorized)
    acc = compute_newtonian_accelerations(pos)

    # 2. AVE Macroscopic Inductive 'Sweep'
    distances = cdist(pos, pos)
    density_radius = 15.0
    densities = np.sum(distances < density_radius, axis=1)

    core_idx = np.argmax(densities)
    core_pos = pos[core_idx]

    # Vectorized inductive pull
    vec_to_core = core_pos[np.newaxis, :] - pos
    dist_to_core = np.linalg.norm(vec_to_core, axis=1, keepdims=True)
    dist_to_core_safe = np.maximum(dist_to_core, 1.0)

    inductive_pull = AVE_INDUCTANCE * (vec_to_core / dist_to_core_safe) * np.log1p(dist_to_core_safe)
    # Mask particles too close to core
    mask = (dist_to_core > 1.0).astype(float)
    acc += inductive_pull * mask
    # Dielectric friction
    acc -= 0.1 * vel * mask

    return acc


def run_comparative_accretion() -> None:
    print("[*] Initializing Primordial Gas Clouds...")

    pos_newt, vel_newt = initialize_gas_cloud()
    pos_ave, vel_ave = initialize_gas_cloud()

    # Store history (FRAMES, N_PARTICLES, 2)
    hist_newt = np.zeros((FRAMES, N_PARTICLES, 2))
    hist_ave = np.zeros((FRAMES, N_PARTICLES, 2))

    # Accretion tracking metric
    accretion_rate_newt = np.zeros(FRAMES)
    accretion_rate_ave = np.zeros(FRAMES)

    print("[*] Running Time-Integration... (Standard vs AVE)")
    for step in range(FRAMES):
        if step % 25 == 0:
            print(f"    -> Timestep {step}/{FRAMES}")

        # 1. Update Lambda-CDM (Newtonian)
        acc_n = compute_newtonian_accelerations(pos_newt)
        vel_newt += acc_n * DT
        pos_newt += vel_newt * DT
        hist_newt[step] = pos_newt.copy()

        # Measure clustering (average distance to center of mass)
        cm_n = np.mean(pos_newt, axis=0)
        accretion_rate_newt[step] = BOX_SIZE / (np.mean(np.linalg.norm(pos_newt - cm_n, axis=1)) + 1.0)

        # 2. Update AVE (Macroscopic Inductance)
        acc_a = compute_ave_accelerations(pos_ave, vel_ave)
        vel_ave += acc_a * DT
        pos_ave += vel_ave * DT
        hist_ave[step] = pos_ave.copy()

        cm_a = np.mean(pos_ave, axis=0)
        accretion_rate_ave[step] = BOX_SIZE / (np.mean(np.linalg.norm(pos_ave - cm_a, axis=1)) + 1.0)

    print("[*] Rendering Comparative GIF...")

    # Setup Figure Side-by-Side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    fig.patch.set_facecolor("#0f0f0f")

    for ax in (ax1, ax2):
        ax.set_facecolor("#0f0f0f")
        ax.grid(color="#333333", linestyle="--", alpha=0.5)
        ax.set_xlim([-BOX_SIZE / 1.5, BOX_SIZE / 1.5])
        ax.set_ylim([-BOX_SIZE / 1.5, BOX_SIZE / 1.5])
        ax.set_xticks([])
        ax.set_yticks([])

    ax1.set_title(
        "Standard $\\Lambda$CDM (Collisionless $1/r^2$)\nSlow Hierarchical Merging",
        color="white",
        pad=15,
    )
    ax2.set_title(
        "AVE Cosmology (Macroscopic Inductive Net)\nExponential 'JWST' Accretion",
        color="#00ffcc",
        pad=15,
    )

    scat1 = ax1.scatter([], [], c="#ff6666", s=15, alpha=0.8)
    scat2 = ax2.scatter([], [], c="#66ccff", s=15, alpha=0.8)

    time_text_1 = ax1.text(0.05, 0.95, "", transform=ax1.transAxes, color="white", fontsize=12)
    time_text_2 = ax2.text(0.05, 0.95, "", transform=ax2.transAxes, color="white", fontsize=12)

    def update(frame: int) -> tuple:
        # Update Lambda-CDM
        scat1.set_offsets(hist_newt[frame])
        c_rate1 = accretion_rate_newt[frame]
        time_text_1.set_text(f"Time: {frame*5} Myrs\nClustering Index: {c_rate1:.1f}")

        # Update AVE
        scat2.set_offsets(hist_ave[frame])
        c_rate2 = accretion_rate_ave[frame]
        time_text_2.set_text(f"Time: {frame*5} Myrs\nClustering Index: {c_rate2:.1f}")

        return scat1, scat2, time_text_1, time_text_2

    anim = animation.FuncAnimation(fig, update, frames=FRAMES, interval=40, blit=True)

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "jwst_accretion_comparison.gif"

    anim.save(target, writer="pillow", fps=25)
    print(f"[*] Visualized Cosmological Accretion: {target}")


if __name__ == "__main__":
    run_comparative_accretion()
