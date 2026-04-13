import numpy as np
import matplotlib.pyplot as plt
import os

def create_orbital_plot():
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='#050510')
    ax.set_facecolor('#050510')
    
    # Bohr radius mapped to lattice units (x = r / a_0)
    x = np.linspace(0, 25, 1000)
    
    # Radial wavefunctions R_nl(x)
    # n=1, l=0
    R_10 = 2.0 * np.exp(-x)
    # n=2, l=0
    R_20 = (1/np.sqrt(2)) * (1 - 0.5*x) * np.exp(-x/2)
    # n=3, l=0
    R_30 = (2/(3*np.sqrt(3))) * (1 - (2/3)*x + (2/27)*x**2) * np.exp(-x/3)
    
    # Radial probability / Acoustic intensity : P(r) = r^2 * |R(r)|^2
    P_10 = x**2 * R_10**2
    P_20 = x**2 * R_20**2
    P_30 = x**2 * R_30**2
    
    # Plot configurations
    ax.plot(x, P_10, color='#ff00aa', lw=3, label='n=1 (Ground State)')
    ax.fill_between(x, 0, P_10, color='#ff00aa', alpha=0.1)
    
    ax.plot(x, P_20, color='#00ffff', lw=3, label='n=2 (1st Overtone)')
    ax.fill_between(x, 0, P_20, color='#00ffff', alpha=0.1)
    
    ax.plot(x, P_30, color='#00ff00', lw=3, label='n=3 (2nd Overtone)')
    ax.fill_between(x, 0, P_30, color='#00ff00', alpha=0.1)
    
    # Top tech box explaining the isomorphism
    tech_text = (
        "Mathematical Isomorphism:\n"
        "Standard Model     : Schrödinger Eq. $\\rightarrow$ Radial Probability $|\\Psi|^2$\n"
        "AVE Framework      : Helmholtz Eq. $\\rightarrow$ Acoustic Pressure Mode $P(r)$"
    )
    
    ax.text(0.5, 0.95, tech_text, transform=ax.transAxes, color='white', fontsize=12,
            ha='center', va='top', bbox=dict(facecolor='#111122', edgecolor='white', boxstyle='round,pad=0.5'))
            
    # Highlight that the curves are IDENTICAL
    ax.text(7, 0.4, "Prediction is 100% mathematically identical.\nOnly interpretation differs.", 
            color='#aaaaaa', fontsize=13, style='italic',
            bbox=dict(facecolor='#050510', edgecolor='none'))
            
    # Formatting
    ax.set_xlabel(r"Distance from Nucleus ($r / a_0$)", color='white', fontsize=14, labelpad=10)
    ax.set_ylabel(r"Energy Density / Probability ($r^2 |R_{n0}|^2$)", color='white', fontsize=14, labelpad=10)
    ax.set_title("Atom as an Acoustic Resonant Cavity\n(Hydrogen s-orbitals)", color='white', fontsize=16, fontweight='bold', pad=20)
    
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 0.6)
    
    ax.tick_params(colors='white')
    for s in ax.spines.values():
        s.set_color('#333')
        
    ax.legend(loc='center right', facecolor='#111122', edgecolor='none', labelcolor='white', fontsize=12)
    
    plt.tight_layout()
    
    out_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'figures')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'hydrogen_orbital_comparison.png')
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    create_orbital_plot()
