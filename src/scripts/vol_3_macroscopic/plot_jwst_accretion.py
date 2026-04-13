import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Aesthetic configuration
plt.style.use('dark_background')
COLOR_AVE = '#00ffff'      # Cyan for AVE
COLOR_LCDM = '#ff00ff'     # Magenta for Lambda-CDM
COLOR_DATA = '#ffff00'     # Yellow for JWST data points

def _find_repo_root():
    """Find the Git repository root directory."""
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != '/':
        if os.path.isdir(os.path.join(current_dir, '.git')):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return os.path.abspath(os.path.dirname(__file__))  # Fallback

def plot_jwst_accretion():
    # Time vector in Million Years (Myr) from Big Bang
    t = np.linspace(0, 800, 500)
    
    # ---------------------------------------------------------
    # 1. Models
    # ---------------------------------------------------------
    # Seed mass (Arbitrary, say 10^6 solar masses for a primordial halo)
    M_seed = 1e6
    
    # AVE Exponential Model (Mutual Inductance)
    # tau = 65.1 Myr (Derived in Chapter 10)
    tau_ind = 65.1
    M_AVE = M_seed * np.exp(t / tau_ind)
    
    # Lambda-CDM Hierarchical Merging Model (Collisionless)
    # Slow power-law growth, M ~ t^(5/2)
    # Normalize so it starts at M_seed at t=10 (to avoid zero div/funny scaling)
    t_safe = np.clip(t, 10, None)
    k_lcdm = M_seed / (10**2.5) 
    M_LCDM = k_lcdm * (t_safe**2.5)
    
    # ---------------------------------------------------------
    # 2. JWST Empirical Data Points
    # ---------------------------------------------------------
    # Empirical constraints:
    # ~10^10 M_sun by 350 Myr
    # ~10^11 M_sun by 500 Myr
    data_t = [350, 500]
    data_M = [1e10, 1e11]
    
    # ---------------------------------------------------------
    # 3. Plotting
    # ---------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    
    # Plot Models
    ax.plot(t, M_AVE, color=COLOR_AVE, lw=3, label=r'AVE Mutual Inductance ($M_{seed} \cdot e^{t / 65.1}$)')
    ax.plot(t, M_LCDM, color=COLOR_LCDM, lw=3, linestyle='--', label=r'Standard $\Lambda$CDM ($M \propto t^{2.5}$)')
    
    # Plot Data
    ax.scatter(data_t, data_M, color=COLOR_DATA, s=150, zorder=5, 
               edgecolors='white', linewidth=1.5, marker='*', label="JWST Empirical Data ($z > 10$)")
    
    # Formatting
    ax.set_yscale('log')
    ax.set_ylim(1e5, 1e12)
    ax.set_xlim(0, 800)
    
    ax.set_title("Early Galaxy Accretion: AVE vs $\Lambda$CDM", fontsize=16, fontweight='bold', pad=15)
    ax.set_xlabel("Time since Big Bang (Million Years)", fontsize=14)
    ax.set_ylabel("Stellar Mass ($M_{\odot}$)", fontsize=14)
    
    # Grid and Legend
    ax.grid(True, which="both", axis='both', color='white', alpha=0.1, linestyle='--')
    ax.legend(loc='lower right', fontsize=12, framealpha=0.8, edgecolor='white')
    
    # Annotate the paradox region
    ax.axvspan(300, 600, color='white', alpha=0.05)
    ax.text(450, 5e6, "JWST High-z\nObservation Window", 
            color='white', alpha=0.6, fontsize=11, 
            horizontalalignment='center', verticalalignment='center')
    
    plt.tight_layout()
    
    # Save Figure
    OUTPUT_DIR = os.path.join(_find_repo_root(), "assets", "sim_outputs")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    filename = "jwst_exponential_accretion.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(filepath, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    print(f"Saved figure to: {filepath}")

if __name__ == "__main__":
    plot_jwst_accretion()
