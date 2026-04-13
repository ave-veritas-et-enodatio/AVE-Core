import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.signal.windows import blackmanharris
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

def simulate_condensate_imd_spectroscopy():
    f1, f2 = 1000.0, 1300.0  
    w1, w2 = 2 * np.pi * f1, 2 * np.pi * f2
    C0, V_crit, I_amp = 1.0, 10.0, 4.0   
    
    def varactor_ode(t, V):
        V_ratio = np.clip(V[0] / V_crit, -0.99, 0.99)
        C_eff = C0 / np.sqrt(1.0 - V_ratio**4)
        I_t = I_amp * (np.sin(w1 * t) + np.sin(w2 * t))
        return [I_t / C_eff]

    Fs = 20000.0; T_total = 2.0
    t_eval = np.linspace(0, T_total, int(Fs * T_total))
    
    sol = solve_ivp(varactor_ode, [0, T_total], [0.0], t_eval=t_eval, method='RK45', rtol=1e-8, atol=1e-10)
    
    window = blackmanharris(len(sol.y[0]))
    fft_vals = np.fft.rfft(sol.y[0] * window)
    fft_freqs = np.fft.rfftfreq(len(sol.y[0]), 1/Fs)
    fft_mag_db = 20 * np.log10(np.abs(fft_vals) / np.max(np.abs(fft_vals)) + 1e-12)
    
    fig, ax = plt.subplots(figsize=(11, 5), dpi=150)
    fig.patch.set_facecolor('#0a0a12'); ax.set_facecolor('#0a0a12')
    
    ax.plot(fft_freqs, fft_mag_db, color='#00ffcc', lw=1.5)
    ax.scatter([f1, f2], [0, 0], color='#FFD54F', s=50, zorder=5)
    ax.text(f1-100, 5, "f1", color='#FFD54F', weight='bold')
    ax.text(f2+50, 5, "f2", color='#FFD54F', weight='bold')
    
    imd1, imd2 = abs(3*f1 - 2*f2), abs(3*f2 - 2*f1)  
    ax.axvline(imd1, color='#E57373', linestyle=':', lw=1.5)
    ax.axvline(imd2, color='#E57373', linestyle=':', lw=1.5)
    ax.text(imd1-350, -40, "EFT Signature\n(3f1 - 2f2)", color='#E57373')
    ax.text(imd2+50, -40, "EFT Signature\n(3f2 - 2f1)", color='#E57373')
    
    ax.set_xlim(0, 3000); ax.set_ylim(-140, 10)
    ax.set_xlabel('Frequency (Hz)', color='white', weight='bold')
    ax.set_ylabel('Magnitude (dBc)', color='white', weight='bold')
    ax.set_title('Condensate IMD Spectroscopy: The EFT Harmonic Fingerprint', color='white', fontsize=14, weight='bold')
    
    textstr = (
        r"$\mathbf{The~Non{-}Linear~EFT~Fingerprint:}$" + "\n" +
        r"Because standard mechanical materials feature 2nd or 3rd-order elasticity," + "\n" +
        r"and the EFT mandates an exact 4th-order condensate saturation limit ($1 - V^4$)," + "\n" +
        r"the analog substrate acts as a unique RF mixer. It mathematically generates" + "\n" +
        r"distinct 5th-order sidebands, completely isolated from normal material noise."
    )
    ax.text(1400, -20, textstr, color='white', fontsize=11, bbox=dict(facecolor='#111111', edgecolor='#4FC3F7', alpha=0.9, pad=10))

    ax.grid(True, ls=':', color='#333333'); ax.tick_params(colors='lightgray')
    for spine in ax.spines.values(): spine.set_color('#333333')
    
    plt.tight_layout(); plt.savefig(os.path.join(OUTPUT_DIR, "condensate_imd_spectroscopy.png"), facecolor=fig.get_facecolor(), bbox_inches='tight')

if __name__ == "__main__": simulate_condensate_imd_spectroscopy()