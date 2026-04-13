import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
import os

def create_comparison():
    fig = plt.figure(figsize=(22, 10), facecolor='#050510')
    
    # ---------------------------------------------------------
    # Panel 1: Standard Model (Probability Amplitude)
    # ---------------------------------------------------------
    ax1 = fig.add_subplot(121)
    ax1.set_facecolor('#050510')
    ax1.set_title("Standard Model Interpretation\n(Point Particle as Probability Cloud)", color='white', pad=25, fontsize=20, fontweight='bold')
    
    y, x = np.mgrid[-10:10:400j, 0:20:400j]
    
    # Slit positions
    slit1_y, slit2_y = 3, -3
    
    # SM: Particle is "everywhere" - spherical probability wave from both slits
    # \psi = e^{ikr_1}/r_1 + e^{ikr_2}/r_2
    k = 4.0
    r1 = np.sqrt(x**2 + (y - slit1_y)**2) + 0.1
    r2 = np.sqrt(x**2 + (y - slit2_y)**2) + 0.1
    
    # Amplitude
    psi = np.exp(1j * k * r1) / np.sqrt(r1) + np.exp(1j * k * r2) / np.sqrt(r2)
    prob_density = np.abs(psi)**2
    
    # Add a smooth fade-in from the slits to represent the "cloud"
    fade = np.clip(x / 5.0, 0, 1)
    prob_density *= fade
    
    # Visualize as a blurry quantum cloud (blues/purples)
    im1 = ax1.imshow(prob_density, extent=[0, 20, -10, 10], origin='lower', cmap='Purples_r', alpha=0.9, vmax=np.percentile(prob_density, 98))
    
    # Draw wall and slits
    wall_x = 0
    ax1.plot([wall_x, wall_x], [-10, slit2_y - 1], 'w-', lw=4)
    ax1.plot([wall_x, wall_x], [slit2_y + 1, slit1_y - 1], 'w-', lw=4)
    ax1.plot([wall_x, wall_x], [slit1_y + 1, 10], 'w-', lw=4)
    
    # Point particle icon as a blurry "superposition"
    ax1.text(wall_x - 3, 0, r'$|\Psi\rangle$', color='#d8b4e2', fontsize=24, ha='center', va='center')
    ax1.plot([-5, -1], [0, slit1_y], color='#d8b4e2', ls='--', alpha=0.5)
    ax1.plot([-5, -1], [0, slit2_y], color='#d8b4e2', ls='--', alpha=0.5)
    
    ax1.text(5, 8, "Particle passes through\nBOTH slits simultaneously", color='white', fontsize=12, ha='left',
            bbox=dict(facecolor='#111122', alpha=0.8, edgecolor='none'))
    
    ax1.set_axis_off()

    # ---------------------------------------------------------
    # Panel 2: AVE Interpretation (Physical Wake)
    # ---------------------------------------------------------
    ax2 = fig.add_subplot(122)
    ax2.set_facecolor('#050510')
    ax2.set_title("Applied Vacuum Engineering\n(Localized Defect + Physical Wake)", color='white', pad=25, fontsize=20, fontweight='bold')
    
    # AVE: Particle is localized, goes through ONE slit. It generates a wake that goes through both.
    source_x, source_y = -4, 0
    
    # Create the physical wave field (instantaneous pressure)
    r_source = np.sqrt((x + 4)**2 + y**2) + 0.1
    wake_primary = np.sin(k * r_source) / np.sqrt(r_source)
    
    # Secondary wavelets from slits (Huygens-Fresnel, but mechanical)
    wake_slit1 = np.sin(k * r1 - k*np.sqrt((-4)**2 + slit1_y**2)) / np.sqrt(r1)
    wake_slit2 = np.sin(k * r2 - k*np.sqrt((-4)**2 + slit2_y**2)) / np.sqrt(r2)
    
    # Combine (just a visual representation of classical interference)
    total_wake = wake_slit1 + wake_slit2
    
    # Use inferno heatmap on energy density |wake|² — makes fringes glow against dark bg
    wake_energy = total_wake**2
    ax2.imshow(wake_energy, extent=[0, 20, -10, 10], origin='lower', cmap='hot', alpha=0.95, vmin=0, vmax=np.percentile(wake_energy, 97))
    
    # Draw wall and slits (Thicker for clarity)
    ax2.plot([wall_x, wall_x], [-10, slit2_y - 1], 'w-', lw=5)
    ax2.plot([wall_x, wall_x], [slit2_y + 1, slit1_y - 1], 'w-', lw=5)
    ax2.plot([wall_x, wall_x], [slit1_y + 1, 10], 'w-', lw=5)
    
    # Draw the particle objectively going through Slit 1
    ax2.plot([-5, -1], [0, slit1_y], color='#00ff00', ls='-', lw=3)
    ax2.plot(-1, slit1_y, 'o', color='#00ff00', markersize=12, markeredgecolor='w', markeredgewidth=2)
    ax2.text(-1, slit1_y + 1.8, "Topological\nDefect", color='#00ff00', fontsize=12, ha='center', fontweight='bold')
    
    # Draw the wake going through Slit 2
    ax2.plot([-5, -1], [0, slit2_y], color='#00ffff', ls=':', lw=3)
    ax2.text(-1, slit2_y - 2.5, "Dark Wake\n(Vacuum Strain)", color='#00ffff', fontsize=12, ha='center', fontweight='bold')
    
    ax2.text(5, 8, "Particle passes through ONE slit.\nIts physical wake passes through BOTH.", color='white', fontsize=14, ha='left',
            bbox=dict(facecolor='#111122', alpha=0.9, edgecolor='#00aaff', lw=2))
    
    ax2.set_axis_off()
    
    plt.tight_layout()
    
    out_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'sim_outputs')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'double_slit_sm_vs_ave.png')
    plt.savefig(out_path, dpi=400, bbox_inches='tight', facecolor=fig.get_facecolor())
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    create_comparison()
