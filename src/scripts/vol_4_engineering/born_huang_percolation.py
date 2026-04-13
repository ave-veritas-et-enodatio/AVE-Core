"""
P1: Rigidity Percolation — K/G = 2 at the Vacuum Operating Point

Derives the K/G = 2 trace-reversal identity using Effective Medium Theory
(EMT) for diluted 3D central-force spring networks.

Key result: The EMT K/G ratio equals 2 at a specific packing fraction
  p* = (10z₀ - 12) / [z₀(z₀+2)] ≈ 10/z₀  (for large z₀)

Setting p* = 8πα (the AVE ansatz) uniquely determines:
  z₀ = 10/(8πα) ≈ 54.5  (the effective coordination number)
  p_K = 2/z₀ ≈ 0.037   (connectivity percolation)
  p_G = 6/z₀ ≈ 0.110   (rigidity percolation)
  p* = 8πα ≈ 0.183      (vacuum operating point, K/G = 2)

The vacuum is a rigid solid operating 56.7% above the fluid-solid
transition, at the unique point where ν = 2/7.
"""
import sys
import os


import numpy as np
import matplotlib.pyplot as plt


def emt_moduli(p, z0):
    """
    EMT bulk and shear moduli for a diluted 3D central-force network.

    K_eff = (p - p_K)/(1 - p_K)  for p > p_K, else 0
    G_eff = (p - p_G)/(1 - p_G)  for p > p_G, else 0

    where p_K = 2/z0 (connectivity), p_G = 2d/z0 = 6/z0 (rigidity).
    """
    p_K = 2.0 / z0
    p_G = 6.0 / z0

    K = np.where(p > p_K, (p - p_K) / (1 - p_K), 0.0)
    G = np.where(p > p_G, (p - p_G) / (1 - p_G), 0.0)

    return K, G


def p_star_kg2(z0):
    """Packing fraction where K/G = 2 in the EMT."""
    return (10.0 * z0 - 12.0) / (z0 * (z0 + 2.0))


def run_analysis():
    """Full EMT analysis with derived z₀ = 10/(8πα)."""
    print("=" * 60)
    print("  P1: RIGIDITY PERCOLATION — K/G = 2 AT VACUUM OPERATING POINT")
    print("=" * 60)

    from ave.core.constants import ALPHA as alpha, P_C as p_c

    # Solve for z₀ from the exact EMT formula:
    # p* = (10z₀ - 12) / [z₀(z₀+2)] = 8πα
    # → p_c·z₀² + (2p_c - 10)·z₀ + 12 = 0
    a_coeff = p_c
    b_coeff = 2 * p_c - 10.0
    c_coeff = 12.0
    disc = b_coeff**2 - 4 * a_coeff * c_coeff
    z0_vac = (-b_coeff + np.sqrt(disc)) / (2 * a_coeff)  # positive root
    p_K_vac = 2.0 / z0_vac
    p_G_vac = 6.0 / z0_vac
    p_star_vac = p_star_kg2(z0_vac)

    print(f"\n  α = 1/{1/alpha:.3f}")
    print(f"  p* = 8πα = {p_c:.6f}")
    print(f"  z₀ = 10/(8πα) = {z0_vac:.2f}")
    print(f"  p_K = 2/z₀ = {p_K_vac:.6f} (connectivity threshold)")
    print(f"  p_G = 6/z₀ = {p_G_vac:.6f} (rigidity threshold)")
    print(f"  p*(K/G=2) = {p_star_vac:.6f}")
    print(f"  Structural margin: {(p_c - p_G_vac)/p_G_vac*100:.1f}% above rigidity")

    # Verify K/G = 2 at p*
    p_check = np.array([p_star_vac])
    K_check, G_check = emt_moduli(p_check, z0_vac)
    print(f"  Verification: K/G = {K_check[0]/G_check[0]:.6f}")

    # --- EMT curves for z₀_vac ---
    p_fine = np.linspace(0.001, 0.5, 1000)
    K_vac, G_vac = emt_moduli(p_fine, z0_vac)

    # K/G ratio (suppress benign divide-by-zero warnings)
    with np.errstate(divide='ignore', invalid='ignore'):
        KG_vac = np.where(G_vac > 1e-10, K_vac / G_vac, np.nan)
        # Poisson ratio
        nu_vac = np.where((K_vac > 1e-10) & (G_vac > 1e-10),
                          (3*K_vac - 2*G_vac) / (6*K_vac + 2*G_vac), np.nan)

    # --- Comparison across z₀ values ---
    z0_range = np.linspace(8, 80, 200)
    p_star_range = np.array([p_star_kg2(z) for z in z0_range])

    # --- Plotting ---
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))
    fig.patch.set_facecolor('#0d1117')

    for ax in axes:
        ax.set_facecolor('#0d1117')
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('#30363d')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    # Panel 1: K, G, K/G vs p for the vacuum z₀
    ax = axes[0]
    ax.plot(p_fine, K_vac, '-', color='#58a6ff', linewidth=2.5, label='$K$')
    ax.plot(p_fine, G_vac, '--', color='#f0883e', linewidth=2.5, label='$G$')

    # Shade fluid window
    ax.axvspan(p_K_vac, p_G_vac, alpha=0.1, color='#f0883e',
               label=f'Fluid window ($K>0, G=0$)')
    ax.axvline(p_K_vac, color='#7c3aed', linestyle=':', alpha=0.5,
               label=f'$p_K = {p_K_vac:.3f}$')
    ax.axvline(p_G_vac, color='#da3633', linestyle=':', alpha=0.7,
               label=f'$p_G = {p_G_vac:.3f}$')
    ax.axvline(p_c, color='#238636', linewidth=2.5, linestyle='--',
               alpha=0.9, label=f'$p^* = 8\\pi\\alpha = {p_c:.3f}$')

    ax.set_xlabel('Bond occupation $p$', fontsize=12, color='white')
    ax.set_ylabel('Effective modulus', fontsize=12, color='white')
    ax.set_title(f'EMT ($z_0 = {z0_vac:.1f}$)', fontsize=13, color='white')
    ax.legend(fontsize=7, facecolor='#161b22', edgecolor='#30363d',
              labelcolor='white', loc='upper left')
    ax.grid(True, alpha=0.15, color='#30363d')
    ax.set_xlim(0, 0.35)

    # Panel 2: K/G vs p
    ax = axes[1]
    valid = np.isfinite(KG_vac) & (KG_vac < 15) & (p_fine > p_G_vac + 0.002)
    ax.plot(p_fine[valid], KG_vac[valid], '-', color='#58a6ff', linewidth=2.5,
            label=f'$K/G$ (EMT, $z_0={z0_vac:.0f}$)')
    ax.axhline(2.0, color='#da3633', linestyle='--', linewidth=2,
               alpha=0.8, label='$K/G = 2$ ($\\nu = 2/7$)')
    ax.axvline(p_c, color='#238636', linewidth=2.5, linestyle='--',
               alpha=0.9, label=f'$p^* = 8\\pi\\alpha$')

    # Mark the K/G = 2 point
    ax.scatter([p_c], [2.0], s=100, color='#238636', zorder=5, edgecolors='white')

    ax.set_xlabel('Bond occupation $p$', fontsize=12, color='white')
    ax.set_ylabel('$K / G$', fontsize=12, color='white')
    ax.set_title(r'$K/G = 2$ at $p = 8\pi\alpha$', fontsize=13, color='white')
    ax.set_ylim(0, 8)
    ax.set_xlim(0.08, 0.35)
    ax.legend(fontsize=9, facecolor='#161b22', edgecolor='#30363d', labelcolor='white')
    ax.grid(True, alpha=0.15, color='#30363d')

    # Panel 3: Poisson ratio
    ax = axes[2]
    valid_nu = np.isfinite(nu_vac) & (p_fine > p_G_vac + 0.002)
    ax.plot(p_fine[valid_nu], nu_vac[valid_nu], '-', color='#58a6ff',
            linewidth=2.5, label='EMT')
    ax.axhline(2/7, color='#da3633', linestyle='--', linewidth=2,
               alpha=0.8, label=r'$\nu = 2/7$')
    ax.axhline(0.5, color='#7c3aed', linestyle=':', alpha=0.4,
               label=r'$\nu = 1/2$ (fluid)')
    ax.axvline(p_c, color='#238636', linewidth=2.5, linestyle='--',
               alpha=0.9, label=f'$p^* = 8\\pi\\alpha$')

    ax.scatter([p_c], [2/7], s=100, color='#238636', zorder=5, edgecolors='white')

    ax.set_xlabel('Bond occupation $p$', fontsize=12, color='white')
    ax.set_ylabel(r"$\nu$", fontsize=12, color='white')
    ax.set_title(r"$\nu = 2/7$ at Operating Point", fontsize=13, color='white')
    ax.set_ylim(0.2, 0.52)
    ax.set_xlim(0.08, 0.35)
    ax.legend(fontsize=9, facecolor='#161b22', edgecolor='#30363d', labelcolor='white')
    ax.grid(True, alpha=0.15, color='#30363d')

    fig.suptitle(r'P1: Vacuum Operating Point — $K = 2G$ at $p = 8\pi\alpha$',
                 fontsize=16, color='white', y=1.02)
    plt.tight_layout()

    output_path = os.path.join(
        os.path.dirname(__file__), '..', 'assets', 'sim_outputs',
        'rigidity_percolation_kg_convergence.png')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"\nSaved: {output_path}")


if __name__ == "__main__":
    run_analysis()
