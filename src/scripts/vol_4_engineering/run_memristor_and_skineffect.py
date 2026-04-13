import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
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

def simulate_memristor_and_skin_effect():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), dpi=150)
    fig.patch.set_facecolor('#0a0a12'); ax1.set_facecolor('#0a0a12'); ax2.set_facecolor('#0a0a12')
    
    R_solid = 50.0; R_ruptured = 1.0; V_yield = 2.0; tau_vac = 0.05
    freq = 2.0
    
    def memristor_ode(t, y):
        V_app = 5.0 * np.sin(2 * np.pi * freq * t)
        S_target = 0.5 * (1.0 + np.tanh(10.0 * (np.abs(V_app) - V_yield)))
        return [(S_target - y[0]) / tau_vac]
        
    t_eval = np.linspace(0, 2.0, 5000)
    sol = solve_ivp(memristor_ode, [0, 2.0], [0.0], t_eval=t_eval, method='RK45')
    
    V_history = 5.0 * np.sin(2 * np.pi * freq * t_eval)
    R_memristor = R_solid * (1 - sol.y[0]) + R_ruptured * sol.y[0]
    I_history = V_history / R_memristor
    
    mask = t_eval > 1.0 
    ax1.plot(V_history[mask], I_history[mask], color='#00ffcc', lw=3, label='Condensate $I-V$ Trace')
    ax1.plot(V_history[mask], V_history[mask]/R_solid, color='#E57373', lw=1.5, linestyle='--', label='Perfect Solid (Ohmic)')
    ax1.axvline(V_yield, color='white', lw=1, alpha=0.5, linestyle=':')
    ax1.axvline(-V_yield, color='white', lw=1, alpha=0.5, linestyle=':')
    
    ax1.set_title('The Condensate Memristor (Pinched Hysteresis)', color='white', fontsize=14, weight='bold')
    ax1.set_xlabel('Topological Potential / Shear Stress ($V$)', color='white', weight='bold')
    ax1.set_ylabel('Kinematic Flow Rate ($I$)', color='white', weight='bold')
    ax1.legend(loc='lower right', facecolor='#111111', edgecolor='white', labelcolor='white')
    
    V_sweep = np.linspace(0, 5, 1000)
    S_eq = 0.5 * (1.0 + np.tanh(10.0 * (np.abs(V_sweep) - V_yield)))
    skin_depth = np.sqrt((R_solid * (1 - S_eq) + R_ruptured * S_eq) / R_solid) * 100.0 
    
    ax2.plot(V_sweep, skin_depth, color='#FFD54F', lw=4, label=r'AC Metric Skin Depth ($\delta \propto \sqrt{R_{eff}}$)')
    ax2.axvline(V_yield, color='#ff3366', linestyle=':', lw=2, label='Dielectric Saturation Limit')
    ax2.fill_between(V_sweep, 0, skin_depth, color='#FFD54F', alpha=0.15)
    
    ax2.set_title('Metric Faraday Cage: The Zero-Impedance Skin Effect', color='white', fontsize=14, weight='bold')
    ax2.set_xlabel('Applied Stress Amplitude ($V$)', color='white', weight='bold')
    ax2.set_ylabel('Boundary Layer Penetration Depth (% of Max)', color='white', weight='bold')
    ax2.legend(loc='upper right', facecolor='#111111', edgecolor='white', labelcolor='white')
    
    textstr = (
        r"$\mathbf{Structural~Boundary~Layer~Mechanics:}$" + "\n" +
        r"Because AC skin depth scales with the square root of resistance," + "\n" +
        r"when the metric yields ($R_{eff} \to 0$), the penetration depth collapses." + "\n" +
        r"The destructive inductive shear is strictly confined to the exterior boundary." + "\n" +
        r"The interior metric is physically shielded from macroscopic turbulence."
    )
    ax2.text(0.1, 20, textstr, color='white', fontsize=11, bbox=dict(facecolor='#111111', edgecolor='#FFD54F', alpha=0.9, pad=10))

    for ax in [ax1, ax2]:
        ax.grid(True, ls=':', color='#333333'); ax.tick_params(colors='white')
        for spine in ax.spines.values(): spine.set_color('#333333')

    plt.tight_layout(); plt.savefig(os.path.join(OUTPUT_DIR, "memristor_and_skineffect.png"), facecolor=fig.get_facecolor(), bbox_inches='tight'); plt.close()

if __name__ == "__main__": simulate_memristor_and_skin_effect()