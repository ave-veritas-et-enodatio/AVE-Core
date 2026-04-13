import numpy as np
import matplotlib.pyplot as plt
import os

# --- Standard AVE output directory ---
def _find_repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, "pyproject.toml")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(_find_repo_root(), "assets", "sim_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
# --- End standard output directory ---, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def simulate_orbital_ac_power():
    t = np.linspace(0, 2 * np.pi, 1000)
    I_x, I_y = -np.sin(t), np.cos(t)
    V_x, V_y = -np.cos(t), -np.sin(t)
    
    Real_Power = (V_x * I_x) + (V_y * I_y)
    Reactive_Power = np.abs((V_x * I_y) - (V_y * I_x))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=150)
    fig.patch.set_facecolor('#0a0a12'); ax1.set_facecolor('#0a0a12'); ax2.set_facecolor('#0a0a12')
    
    ax1.plot(t, I_y, color='#00ffcc', lw=3, label=r'Tangential Current ($I_{condensate} \propto v$)')
    ax1.plot(t, V_y, color='#ff3366', lw=3, linestyle='--', label=r'Radial Voltage ($V_{condensate} \propto F_g$)')
    ax1.set_title(r'Orbital AC Phase Shift ($\theta = 90^\circ$)', color='white', fontsize=14, weight='bold')
    ax1.set_xlabel('Orbital Phase (Radians)', color='white')
    ax1.set_ylabel('Amplitude (Normalized)', color='white')
    ax1.legend(loc='lower right', facecolor='#111111', edgecolor='white', labelcolor='white')
    
    ax2.plot(t, Real_Power, color='#ffcc00', lw=4, label='Real Power $P$ (Dissipated Watts)')
    ax2.plot(t, Reactive_Power, color='#4FC3F7', lw=3, linestyle='--', label='Reactive Power $Q$ (Conserved VARs)')
    ax2.fill_between(t, 0, Reactive_Power, color='#4FC3F7', alpha=0.15)
    ax2.set_title('Analog Condensate Power Dissipation', color='white', fontsize=14, weight='bold')
    ax2.set_xlabel('Orbital Phase (Radians)', color='white')
    ax2.set_ylabel('Power Amplitude', color='white')
    ax2.legend(loc='center', facecolor='#111111', edgecolor='white', labelcolor='white')
    ax2.set_ylim(-0.5, 1.5)
    
    textstr = (
        r"$\mathbf{The~Friction~Paradox~Resolved:}$" + "\n" +
        r"$P_{real} = V_{rms} I_{rms} \cos(90^\circ) \equiv \mathbf{0}$" + "\n" +
        r"Because force and velocity are mathematically orthogonal, the planetary body dissipates" + "\n" +
        r"exactly zero Real Power into the spatial condensate. The orbit is a lossless" + "\n" +
        r"reactive LC tank circuit maintaining constant energy."
    )
    ax2.text(0.3, -0.3, textstr, color='white', fontsize=11, bbox=dict(facecolor='#111111', edgecolor='white', alpha=0.8, pad=8))

    for ax in [ax1, ax2]:
        ax.grid(True, ls=':', color='#333333'); ax.tick_params(colors='lightgray')
        for spine in ax.spines.values(): spine.set_color('#333333')

    plt.tight_layout(); plt.savefig(os.path.join(OUTPUT_DIR, "orbital_reactive_power.png"), facecolor=fig.get_facecolor(), bbox_inches='tight')

if __name__ == "__main__": simulate_orbital_ac_power()