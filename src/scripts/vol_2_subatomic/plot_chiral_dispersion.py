import numpy as np
import matplotlib.pyplot as plt
import os

def create_dispersion_plot():
    fig, ax = plt.subplots(figsize=(10, 7), facecolor='#050510')
    ax.set_facecolor('#050510')
    
    # Parameters (normalized)
    c = 1.0
    gamma_c = 0.8
    
    k = np.linspace(0, 3.0, 500)
    
    # Standard linear dispersion (omega = ck)
    omega_std = c * k
    
    # Right-handed (positive helicity): omega^2 = c^2 k^2 + gamma_c k
    omega_R_sq = c**2 * k**2 + gamma_c * k
    omega_R = np.sqrt(np.maximum(0, omega_R_sq))
    
    # Left-handed (negative helicity): omega^2 = c^2 k^2 - gamma_c k
    omega_L_sq = c**2 * k**2 - gamma_c * k
    
    # Handle imaginary part for L-branch
    omega_L_real = np.sqrt(np.maximum(0, omega_L_sq))
    omega_L_imag = np.sqrt(np.maximum(0, -omega_L_sq))
    
    # Evanescent gap bound
    k_gap = gamma_c / c**2
    
    # Plotting
    ax.plot(k, omega_std, '--', color='#777777', lw=2, label=r'Standard Vacuum ($\omega = ck$)')
    ax.plot(k, omega_R, '-', color='#00ffff', lw=3, label=r'Right-Handed Branch ($\omega^2 = c^2k^2 + \gamma_c k$)')
    
    # Plot L-branch real part
    mask_propagating = k >= k_gap
    ax.plot(k[mask_propagating], omega_L_real[mask_propagating], '-', color='#ff00aa', lw=3, label='Left-Handed Branch (Propagating)')
    
    # Plot L-branch imaginary part (evanescent)
    mask_evanescent = k < k_gap
    ax.plot(k[mask_evanescent], omega_L_imag[mask_evanescent], ':', color='#ff88cc', lw=3, label='Left-Handed Branch (Evanescent/Imaginary)')
    
    # Shade the parity violation gap
    ax.axvspan(0, k_gap, alpha=0.15, color='#ff00aa')
    ax.text(k_gap / 2, 1.5, "Evanescent Gap\n(Parity Violation Zone)", color='#ff88cc', ha='center', fontweight='bold')
    
    # Formatting
    ax.axvline(k_gap, color='#ff00aa', ls='--')
    ax.annotate(r'$k_{gap} = \frac{\gamma_c}{c^2}$', xy=(k_gap, -0.1), xytext=(k_gap, -0.4),
                color='#ff00aa', fontsize=14, ha='center',
                arrowprops=dict(arrowstyle="-", color='#ff00aa'))
                
    ax.set_xlabel("Wavenumber ($k$)", color='white', fontsize=14, labelpad=10)
    ax.set_ylabel(r"Frequency / Energy ($\omega$)", color='white', fontsize=14, labelpad=10)
    ax.set_title("Chiral Dispersion Relation (Cosserat Vacuum)", color='white', fontsize=16, fontweight='bold', pad=20)
    
    ax.set_xlim(0, 3)
    ax.set_ylim(-0.2, 4)
    
    ax.axhline(0, color='gray', lw=1)
    
    ax.tick_params(colors='white')
    for s in ax.spines.values():
        s.set_color('#333')
        
    ax.legend(loc='upper left', facecolor='#111122', edgecolor='none', labelcolor='white')
    
    plt.tight_layout()
    
    out_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'figures')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'chiral_dispersion_relation.png')
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    create_dispersion_plot()
