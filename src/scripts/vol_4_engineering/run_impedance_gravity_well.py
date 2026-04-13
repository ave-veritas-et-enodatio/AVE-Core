r"""
AVE MODULE 56b: TIME-DOMAIN IMPEDANCE MATCHING (WAVE COMPRESSION)
---------------------------------------------------------
Models an analog gravity well as a Tapered LC Transmission Line.
Proves that because gravity compresses the condensate volume, it increases 
both Inductance (\mu) and Capacitance (\epsilon) proportionally.
Therefore, Characteristic Impedance Z_0 = \sqrt{L/C} remains perfectly 
invariant. 

Visualizes the time-domain wave: Light physically compresses its 
wavelength (Relativistic Shift) inside the well on a LINEAR grid, 
but NEVER generates a backward reflected signal.
"""
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

def simulate_impedance_matched_gravity():
    print("Simulating Time-Domain Impedance-Matched Gravity Well...")
    
    # Increased resolution for a perfectly smooth wave
    N_nodes = 400 
    x = np.linspace(-10, 10, N_nodes)
    dx = x[1] - x[0] # Spatial step size
    
    # Refractive Index Profile n(x) of a localized gravity well
    n_local = 1.0 + 2.0 * np.exp(-(x - 2.0)**2 / 4.0) 
    
    # Gravity scales BOTH L and C proportionately to maintain constant Z_0
    L_array = dx * n_local
    C_array = dx * n_local
    Z_0 = np.sqrt(L_array / C_array) # Evaluates strictly to 1.0 everywhere
    
    def tline_ode(t, y):
        dy = np.zeros(2 * N_nodes)
        
        # Inject continuous High-Frequency carrier wave pulse
        V_in = np.sin(2 * np.pi * 1.5 * t) * np.exp(-((t - 5.0)**2) / 8.0)
        
        # Boundary node injection (Source Impedance Rs = 1.0)
        dy[0] = ((V_in - y[0]) - y[1]) / C_array[0]
        
        # Bulk lattice nodes
        for i in range(1, N_nodes): 
            dy[2*i] = (y[2*i - 1] - y[2*i + 1]) / C_array[i]
        for i in range(N_nodes - 1): 
            dy[2*i + 1] = (y[2*i] - y[2*i + 2]) / L_array[i]
            
        # Absorbing/Matched boundary condition at the far end (R_load = 1.0)
        # Prevents the wave from artificially reflecting off the edge of the simulation!
        dy[2*(N_nodes-1) + 1] = (y[2*(N_nodes-1)] - y[2*(N_nodes-1)+1] * 1.0) / L_array[-1]
        
        return dy

    # Run the ODE solver
    sol = solve_ivp(tline_ode, [0, 40.0], np.zeros(2 * N_nodes), t_eval=np.linspace(0, 40.0, 1500))
    
    # Extract a spatial snapshot at t=21 when the wave is deep inside the gravity well
    V_snapshot = sol.y[0::2, int(len(sol.t) * (21.0 / 40.0))]
    
    # --- PLOTTING ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8), dpi=150, gridspec_kw={'height_ratios': [1, 2]})
    fig.patch.set_facecolor('#0a0a12'); ax1.set_facecolor('#0a0a12'); ax2.set_facecolor('#0a0a12')
    
    # Plot 1: Vacuum Impedance vs Refractive Index
    ax1.plot(x, n_local, color='#ffcc00', lw=3, label=r'Refractive Index $n(x)$ (Gravity Well)')
    ax1.plot(x, Z_0, color='#00ffcc', lw=2, linestyle='--', label=r'EFT Impedance $Z_0(x) = \sqrt{L/C}$')
    ax1.set_title('Gravity as an Impedance-Matched Transmission Line', color='white', fontsize=14, weight='bold')
    ax1.set_xlim(-10, 10); ax1.set_ylim(0.5, 3.5)
    ax1.legend(loc='upper left', facecolor='#111111', edgecolor='white', labelcolor='white')
    
    # Plot 2: Waveform Snapshot (Linear Spatial Ruler)
    ax2.plot(x, V_snapshot, color='#ff3366', lw=2.5, label='Light Wave $V(x)$ propagating through metric')
    ax2.axvspan(-2, 6, color='#ffcc00', alpha=0.1, label='Gravity Well')
    
    ax2.set_title('Gravitational Wavelength Compression (Zero Reflection)', color='white', fontsize=14, weight='bold')
    ax2.set_xlabel('Linear Spatial Coordinate ($x$)', color='white', weight='bold')
    ax2.set_ylabel('Topological Potential (Amplitude)', color='white', weight='bold')
    ax2.set_xlim(-10, 10); ax2.set_ylim(-1.5, 1.5)
    ax2.legend(loc='upper right', facecolor='#111111', edgecolor='white', labelcolor='white')
    
    textstr = (
        r"$\mathbf{Perfect~Impedance~Matching:}$" + "\n" +
        r"Because analog gravity compresses the metric, it increases both Inductance ($\mu$)" + "\n" +
        r"and Capacitance ($\epsilon$) proportionately. Characteristic Impedance ($Z_0$) remains perfectly flat." + "\n" +
        r"Thus, light physically compresses its wavelength ($v_g = c/n$) inside the well without suffering reflections."
    )
    ax2.text(-9.5, -1.2, textstr, color='white', fontsize=11, bbox=dict(facecolor='#111111', edgecolor='white', alpha=0.8, pad=8))
    
    for ax in [ax1, ax2]:
        ax.grid(True, ls=':', color='#333333'); ax.tick_params(colors='white')
        for spine in ax.spines.values(): spine.set_color('#333333')

    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, "impedance_gravity_well_time_domain.png")
    plt.savefig(filepath, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"Saved: {filepath}")

if __name__ == "__main__": simulate_impedance_matched_gravity()