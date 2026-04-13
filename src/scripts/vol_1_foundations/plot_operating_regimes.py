import numpy as np
import matplotlib.pyplot as plt
import os

def create_phase_diagram():
    fig, ax = plt.subplots(figsize=(14, 8), facecolor='#050510')
    ax.set_facecolor('#050510')
    
    # Generate data for the stress-strain curve
    strain = np.linspace(0, 1.2, 500)
    
    # Linear regime 
    stress_linear = strain
    
    # Non-linear (strain-stiffening) then snap
    # We use a phenomenological curve: linear -> cubic stiffening -> horizontal cutoff (snap)
    stress_actual = strain + 0.5 * strain**3
    
    rupture_strain = 0.85
    rupture_stress = rupture_strain + 0.5 * rupture_strain**3
    
    stress_actual[strain > rupture_strain] = np.nan
    
    # Plot curves
    ax.plot(strain, stress_linear, '--', color='#555555', lw=2, label='Ideal Hookean (Classical Physics)')
    ax.plot(strain, stress_actual, '-', color='#00ffcc', lw=4, label='AVE Vacuum Response')
    
    # Fill regimes
    ax.axvspan(0, 0.4, alpha=0.2, color='#0044ff')
    ax.text(0.2, 0.1, "I. Linear Regime\n(Acoustic Modes)", color='white', ha='center', fontweight='bold', fontsize=14)
    
    ax.axvspan(0.4, rupture_strain, alpha=0.2, color='#ff00aa')
    ax.text(0.625, 0.1, "II. Tensor Regime\n(Non-linear Stiffening)", color='white', ha='center', fontweight='bold', fontsize=14)
    
    ax.axvspan(rupture_strain, 1.2, alpha=0.5, color='#440000', hatch='//')
    ax.text(1.025, 0.5, "III. Rupture Limit\n(Topological Defect Formation)", color='#ff5555', ha='center', fontweight='bold', fontsize=14, rotation=90, va='center')
    
    # Boundaries and Annotations
    ax.axvline(0.4, color='#777777', ls=':')
    ax.axvline(rupture_strain, color='#ff0000', ls='-', lw=2)
    
    # Physical examples
    bbox_props = dict(boxstyle="round,pad=0.5", fc="#111122", ec="gray", lw=2)
    
    ax.annotate("Electromagnetism\nWeak Gravity (Newtonian)", 
                xy=(0.15, 0.15 + 0.5*0.15**3), xytext=(0.05, 0.8),
                arrowprops=dict(facecolor='white', shrink=0.05, width=1, headwidth=6, edgecolor='white'),
                color='white', fontsize=11, bbox=bbox_props)
                
    ax.annotate("MOND Acceleration Scale ($a_0$)\nStrong Force Confinement", 
                xy=(0.6, 0.6 + 0.5*0.6**3), xytext=(0.4, 1.1),
                arrowprops=dict(facecolor='white', shrink=0.05, width=1, headwidth=6, edgecolor='white'),
                color='white', fontsize=11, bbox=dict(boxstyle="round,pad=0.5", fc="#221133", ec="#ffaa00", lw=2))

    ax.annotate(r"Absolute Snap Limit ($V_{snap} = 511$ kV)" + "\nPair Production / Event Horizon", 
                xy=(rupture_strain, rupture_stress), xytext=(0.55, 1.4),
                arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=8, edgecolor='red'),
                color='#ffaaaa', fontsize=11, bbox=dict(boxstyle="round,pad=0.5", fc="#330000", ec="red", lw=2))

    # Formatting
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 1.6)
    
    ax.set_xlabel("Local Vacuum Strain / Distortion Magnitude ($|\\nabla \Psi|$)", color='white', fontsize=14, labelpad=15)
    ax.set_ylabel("Restoring Tension / Topological Resistance ($T$)", color='white', fontsize=14, labelpad=15)
    ax.set_title("The Three Operating Regimes of the Universal LC Lattice", color='white', fontsize=18, fontweight='bold', pad=20)
    
    # Customize ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.legend(loc='upper left', facecolor='#111122', edgecolor='none', labelcolor='white')
    
    plt.tight_layout()
    
    out_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'figures')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'operating_regimes_phase_diagram.png')
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    create_phase_diagram()
