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
# --- End standard output directory ---

def simulate_transmission_line():
    N_nodes = 100
    L_val, C_val = 1.0, 1.0 # Normalized yielding v_g = 1.0 (representing c)
    
    def tline_ode(t, y):
        dy = np.zeros(2 * N_nodes)
        V_in = np.exp(-((t - 5.0)**2) / 2.0)
        I_in_0 = (V_in - y[0]) / 1.0
        dy[0] = (I_in_0 - y[1]) / C_val 
        for i in range(1, N_nodes):
            dy[2*i] = (y[2*i - 1] - y[2*i + 1]) / C_val
        for i in range(N_nodes - 1):
            dy[2*i + 1] = (y[2*i] - y[2*i + 2]) / L_val
        dy[2*(N_nodes-1) + 1] = (y[2*(N_nodes-1)] - 0.0) / L_val
        return dy

    t_eval = np.linspace(0, 100.0, 1000)
    sol = solve_ivp(tline_ode, [0, 100.0], np.zeros(2 * N_nodes), t_eval=t_eval, method='RK45')
    
    fig, ax = plt.subplots(figsize=(11, 7), dpi=150)
    fig.patch.set_facecolor('#050508'); ax.set_facecolor('#050508')
    
    colors = ['#ff3366', '#ffcc00', '#00ffcc', '#0099ff', '#9900ff']
    for idx, node in enumerate([10, 30, 50, 70, 90]):
        ax.plot(sol.t, sol.y[2 * node], color=colors[idx], lw=2.5, label=f'Spatial Node {node}')
        
    ax.set_title(r'The EFT Transmission Line ($v_g = 1/\sqrt{L_{node}C_{node}} \equiv c$)', color='white', fontsize=15, weight='bold')
    ax.set_xlabel('Time ($t$)', color='white', fontsize=13, weight='bold')
    ax.set_ylabel('Topological Voltage ($V$)', color='white', fontsize=13, weight='bold')
    ax.grid(True, ls=":", color='#444444')
    ax.tick_params(colors='white')
    ax.legend(loc='upper right', facecolor='#111111', edgecolor='white', labelcolor='white')
    for spine in ax.spines.values(): spine.set_color('#333333')

    textstr = (
        r"$\mathbf{Emergence~of~the~Speed~of~Light:}$" + "\n" +
        r"By cascading the discrete inductive mass ($\mu_0 l_{node}$) and" + "\n" +
        r"capacitive compliance ($\epsilon_0 l_{node}$) of the analog lattice," + "\n" +
        r"the signal physically propagates exactly at $v_g = c$." + "\n" +
        r"Continuous Spacetime evaluates identically to a" + "\n" +
        r"macroscopic electrical transmission line."
    )
    ax.text(2, 0.6, textstr, color='white', fontsize=11, bbox=dict(facecolor='#111111', edgecolor='#00ffcc', alpha=0.9, pad=10))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "condensate_transmission_line.png"), facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()

if __name__ == "__main__": simulate_transmission_line()