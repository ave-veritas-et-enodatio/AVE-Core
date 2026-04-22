"""
P2: Borromean Flux-Tube FEM — V_halo Convergence Study (JAX GPU)
================================================================

GPU-accelerated port of fem_borromean_convergence.py.
All physics is IDENTICAL — only the compute backend changes.

Borromean 6³₂ linkage geometry and saturation threshold are
axiom-derived (Axiom 1: FWHM = ℓ_node, mutual inductance at crossing).

Three orthogonal Gaussian flux tubes (the Borromean core) are evaluated
on a 3D grid. The GPU parallelises the volumetric integration that
dominates wall time (especially at N=512: 134M voxels).

Output: assets/sim_outputs/borromean_fem_convergence.png
"""

import sys
import os


import numpy as np
import jax
import jax.numpy as jnp
from jax import jit
from functools import partial
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


@partial(jit, static_argnums=(1,))
def _compute_v_halo_jax(threshold, N, L=6.0):
    """
    Compute the saturated overlap volume on an N³ grid spanning [-L, L]³.

    All geometry is axiom-derived:
      - Three flux tubes along X, Y, Z axes
      - Gaussian profile: ρ(r) = exp(-r²/2σ²)
      - σ = FWHM/(2√(2ln2)), FWHM = ℓ_node = 1.0
      - Tube offset = ℓ_node/2 = 0.5

    Returns (V_sat, V_overlap, peak_density).
    """
    offset = 0.5
    sigma = 1.0 / (2.0 * jnp.sqrt(2.0 * jnp.log(2.0)))
    s2 = sigma**2

    x = jnp.linspace(-L, L, N)
    dx = x[1] - x[0]
    dV = dx**3

    # 3D meshgrid (fully vectorised on GPU)
    X, Y, Z = jnp.meshgrid(x, x, x, indexing="ij")

    # Three orthogonal flux tubes with skew offsets
    # X-tube: runs along x, centered at (y, z) = (0, offset)
    rho_x = jnp.exp(-(Y**2 + (Z - offset) ** 2) / (2.0 * s2))
    # Y-tube: runs along y, centered at (x, z) = (offset, 0)
    rho_y = jnp.exp(-((X - offset) ** 2 + Z**2) / (2.0 * s2))
    # Z-tube: runs along z, centered at (x, y) = (0, -offset)
    rho_z = jnp.exp(-(X**2 + (Y + offset) ** 2) / (2.0 * s2))

    rho_total = rho_x + rho_y + rho_z

    # Saturated volume: where total density exceeds threshold
    sat_mask = rho_total > threshold
    V_sat = jnp.sum(sat_mask.astype(jnp.float32)) * dV

    # Overlap volume: where ≥2 tubes both exceed half-threshold
    half_t = threshold / 2.0
    n_above = (
        (rho_x > half_t).astype(jnp.int32) + (rho_y > half_t).astype(jnp.int32) + (rho_z > half_t).astype(jnp.int32)
    )
    V_overlap = jnp.sum((n_above >= 2).astype(jnp.float32)) * dV

    peak = jnp.max(rho_total)

    return V_sat, V_overlap, peak


def compute_v_halo_jax(N, L=6.0, threshold=0.5):
    """Wrapper that handles the static N argument for JIT."""
    V_sat, V_ov, peak = _compute_v_halo_jax(threshold, N, L)
    return float(V_sat), float(V_ov), float(peak)


def run_convergence_study():
    """Run mesh refinement study and Richardson extrapolation."""
    import time

    print("=" * 60)
    print("  P2: BORROMEAN FLUX-TUBE FEM — V_halo CONVERGENCE (JAX GPU)")
    print("=" * 60)

    # --- Phase 1: Derived Saturation Threshold ---
    # AXIOM-DERIVED: σ = FWHM/(2√(2ln2)), threshold = 1 + σ/4
    # M/L = exp(-d²/(4σ²)) = 1/√2 (exact at crossing)
    sigma_tube = 1.0 / (2.0 * np.sqrt(2.0 * np.log(2.0)))
    t_derived = 1.0 + sigma_tube / 4.0

    d_offset = 0.5
    M_over_L = np.exp(-(d_offset**2) / (4.0 * sigma_tube**2))

    print(f"\n--- Phase 1: Derived Saturation Threshold ---")
    print(f"  σ_tube = FWHM/(2√(2ln2)) = {sigma_tube:.6f} ℓ_node")
    print(f"  M/L at crossing = exp(-d²/(4σ²)) = {M_over_L:.6f} = 1/√2")
    print(f"  Derived threshold: t = 1 + σ/4 = {t_derived:.6f}")
    t_target = t_derived

    # --- Phase 2: Mesh Convergence at optimal threshold ---
    print(f"\n--- Phase 2: Mesh Convergence (threshold = {t_target:.4f}) ---")
    Ns = [64, 96, 128, 192, 256]
    results = []

    for N in Ns:
        t0 = time.time()
        V_sat, V_ov, peak = compute_v_halo_jax(N, threshold=t_target)
        dt_s = time.time() - t0
        dx = 12.0 / N
        results.append((N, dx, V_sat, V_ov, peak))
        print(
            f"  N = {N:4d}: dx = {dx:.4f}, V_sat = {V_sat:.6f}, V_overlap = {V_ov:.6f}, "
            f"peak = {peak:.4f}  ({dt_s:.1f}s)"
        )

    # Richardson extrapolation (order p=2)
    N1, _, V1, _, _ = results[-2]
    N2, _, V2, _, _ = results[-1]
    h1 = 12.0 / N1
    h2 = 12.0 / N2
    p = 2
    V_richardson = (h1**p * V2 - h2**p * V1) / (h1**p - h2**p)
    print(f"\n  Richardson extrapolation (N→∞): V_sat = {V_richardson:.6f}")
    print(f"  Error from 2.0: {abs(V_richardson - 2.0):.6f} ({abs(V_richardson - 2.0)/2.0*100:.3f}%)")

    # --- Phase 3: Soliton Confinement Radius ---
    print("\n--- Phase 3: Soliton Confinement Radius ---")
    sigma = 1.0 / (2.0 * np.sqrt(2.0 * np.log(2.0)))
    r_vals = np.linspace(0, 5, 500)
    rho_crossing = 2.0 * np.exp(-(r_vals**2) / (2.0 * sigma**2))
    cage_idx = np.argmax(rho_crossing < t_target)
    r_cage = r_vals[cage_idx]
    print(f"  σ_tube = {sigma:.4f} ℓ_node")
    print(f"  Cage radius (where ρ < {t_target:.3f}): r_cage = {r_cage:.4f} ℓ_node")
    print(f"  Confinement diameter: 2·r_cage = {2*r_cage:.4f} ℓ_node")

    # --- Plotting (identical to numpy version) ---
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))
    fig.patch.set_facecolor("#0d1117")

    for ax in axes:
        ax.set_facecolor("#0d1117")
        ax.tick_params(colors="white")
        for spine in ax.spines.values():
            spine.set_color("#30363d")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    # Panel 1: V_sat vs threshold
    thresholds = np.linspace(0.5, 1.5, 40)
    V_sat_vs_t = np.array([compute_v_halo_jax(128, threshold=t)[0] for t in thresholds])
    axes[0].plot(thresholds, V_sat_vs_t, color="#58a6ff", linewidth=2.5)
    axes[0].axhline(
        2.0,
        color="#f0883e",
        linestyle="--",
        alpha=0.8,
        label=r"$\mathcal{V}_{total} = 2.0$ (topological bound)",
    )
    axes[0].axvline(
        t_target,
        color="#da3633",
        linestyle=":",
        alpha=0.8,
        label=f"Derived $t = 1+\\sigma/4 = {t_target:.3f}$",
    )
    axes[0].set_xlabel("Density Threshold", fontsize=12, color="white")
    axes[0].set_ylabel(r"Saturated Volume $\mathcal{V}_{sat}$", fontsize=12, color="white")
    axes[0].set_title("Threshold Sensitivity", fontsize=13, color="white")
    axes[0].legend(fontsize=9, facecolor="#161b22", edgecolor="#30363d", labelcolor="white")
    axes[0].grid(True, alpha=0.15, color="#30363d")

    # Panel 2: Mesh convergence
    Ns_arr = np.array([r[0] for r in results])
    Vs_arr = np.array([r[2] for r in results])
    axes[1].plot(Ns_arr, Vs_arr, "o-", color="#58a6ff", linewidth=2, markersize=8)
    axes[1].axhline(
        V_richardson,
        color="#f0883e",
        linestyle="--",
        alpha=0.8,
        label=f"Richardson: {V_richardson:.4f}",
    )
    axes[1].axhline(2.0, color="#238636", linestyle=":", alpha=0.5, label="Topological bound = 2.0")
    axes[1].set_xlabel("Grid Points per Axis (N)", fontsize=12, color="white")
    axes[1].set_ylabel(r"$\mathcal{V}_{sat}$", fontsize=12, color="white")
    axes[1].set_title("Mesh Convergence", fontsize=13, color="white")
    axes[1].legend(fontsize=9, facecolor="#161b22", edgecolor="#30363d", labelcolor="white")
    axes[1].grid(True, alpha=0.15, color="#30363d")

    # Panel 3: Crossing profile and cage radius
    axes[2].plot(r_vals, rho_crossing, color="#58a6ff", linewidth=2.5, label="Combined density at crossing")
    axes[2].axhline(t_target, color="#f0883e", linestyle="--", alpha=0.8, label=f"Threshold = {t_target:.3f}")
    axes[2].axvline(r_cage, color="#da3633", linewidth=2, alpha=0.8, label=f"Cage radius = {r_cage:.2f} ℓ_node")
    axes[2].fill_between(r_vals[: cage_idx + 1], 0, rho_crossing[: cage_idx + 1], alpha=0.15, color="#238636")
    axes[2].set_xlabel(r"Distance from crossing center ($\ell_{node}$)", fontsize=12, color="white")
    axes[2].set_ylabel(r"Density $\rho$", fontsize=12, color="white")
    axes[2].set_title("Flux-Tube Confinement", fontsize=13, color="white")
    axes[2].legend(fontsize=9, facecolor="#161b22", edgecolor="#30363d", labelcolor="white")
    axes[2].grid(True, alpha=0.15, color="#30363d")

    fig.suptitle(
        r"P2: Borromean $6^3_2$ FEM — $\mathcal{V}_{halo}$ Convergence (JAX GPU)",
        fontsize=16,
        color="white",
        y=1.02,
    )
    plt.tight_layout()

    output_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "assets",
        "sim_outputs",
        "borromean_fem_convergence.png",
    )
    plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(f"\nSaved: {output_path}")

    return V_richardson, r_cage


if __name__ == "__main__":
    V_inf, r_cage = run_convergence_study()
    print(f"\n{'='*60}")
    print(f"  FINAL: V_halo (N→∞) = {V_inf:.6f}")
    print(f"  Cage confinement radius = {r_cage:.4f} ℓ_node")
    print(f"{'='*60}")
