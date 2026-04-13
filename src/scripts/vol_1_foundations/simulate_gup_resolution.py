# simulate_gup_resolution.py
# Formally simulates the Generalized Uncertainty Principle (GUP) in the AVE framework.
# Plots the absolute minimum localization bounds created by the discrete Brillouin zone
# of the LC lattice, preventing the Ultraviolet (UV) Singularities inherent to continuum QM.

import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use('dark_background')
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
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def generate_gup_resolution():
    print("Executing Brillouin Zone Topological GUP Solver...")
    
    # Constants (Normalized for graphing clarity rather than SI units)
    hbar = 1.0           # Planck constant
    l_node = 0.5         # The discrete fundamental Planck-scale lattice node distance
    
    # The absolute momentum breaking point (Brillouin boundary)
    p_max = (np.pi * hbar) / l_node
    
    # Momentum sweep
    # We sweep from 0 up to slightly past p_max to show the physical cut-off
    p_array = np.linspace(0.01, p_max * 1.5, 1000)
    
    # -----------------------------------------------------------------
    # 1. Standard Model Continuum Limit (Heisenberg)
    # dx * dp >= hbar / 2
    # dx = hbar / (2 * dp)
    # -----------------------------------------------------------------
    dx_continuum = hbar / (2 * p_array)
    
    # -----------------------------------------------------------------
    # 2. AVE Discrete Matrix Limit (Generalized Uncertainty Principle)
    # The physical momentum operator acts on a discrete grid, modifying the expectation.
    # dx * dp_discrete >= (hbar / 2) * |cos(l_node * p / hbar)|
    # A true finite-difference structural lattice cannot support a waveform shorter than 2*l_node.
    # Therefore, we calculate the geometric saturation of dx.
    # -----------------------------------------------------------------
    # The fundamental structural limit: you cannot localize tighter than the node spacing
    min_localization = l_node / 2.0 
    
    # The AVE GUP formula forces a distinct lower bound plateau:
    dx_ave = np.sqrt( (hbar / (2*p_array))**2 + min_localization**2 )
    
    # Filtering arrays strictly at the Brillouin Limit for the discrete plot
    valid_p_idx = p_array <= p_max
    
    fig = plt.figure(figsize=(11, 8), facecolor='#050510')
    ax = fig.add_subplot(111)
    ax.set_facecolor('#050510')
    
    # Plot Standard Model (Continuum)
    y_max_bound = float(np.max(dx_continuum[100:]))
    dy_plot_limit = y_max_bound * 2.0
    ax.plot(p_array, np.clip(dx_continuum, 0, dy_plot_limit), color='#ff0055', linewidth=3, linestyle='--', 
            label="Standard Model Limit: Continuum Topology\n" + r"(Approaches UV Singularity $\Delta x \to 0$)")
            
    # Plot AVE Matrix (Discrete)
    ax.plot(p_array[valid_p_idx], np.clip(dx_ave[valid_p_idx], 0, dy_plot_limit), color='#00ffff', linewidth=4, 
            label=r"AVE Discrete Lattice Limit: $\Delta x \geq \ell_{node}/2$")
            
    # Highlight the absolute forbidden geometric zone
    ax.fill_between(p_array, 0, min_localization, color='#00ffff', alpha=0.15, hatch='///',
                    label="Forbidden Spatial Contraction\n(Sub-Lattice Resolutions)")
    ax.axhline(min_localization, color='white', linestyle=':', alpha=0.6)
    
    # Highlight the Brillouin Momentum boundary
    ax.axvline(p_max, color='#ffaa00', linestyle='-', linewidth=2, zorder=1)
    
    y_max_bound = float(np.max(dx_continuum[100:]))
    y_text_pos = y_max_bound * 0.8
    print(f"DEBUG bounds: y_max_bound={y_max_bound}, y_text_pos={y_text_pos}")
    ax.text(p_max + 0.1, y_text_pos, 
            "Brillouin Zone Boundary:\nAbsolute Lattice Saturation\n" + r"($\lambda_{min} \to 2\ell_{node}$)", 
            color='#ffaa00', fontsize=12, weight='bold')
    
    # Axes Formatting
    ax.set_ylim(0, y_max_bound * 1.5) # Zoom in to show the divergence clearly
    ax.set_xlim(0, p_max * 1.2)
    
    ax.set_title("Resolution of Ultraviolet Singularities\nvia the AVE Generalized Uncertainty Principle (GUP)", 
                 color='white', fontsize=18, pad=20, weight='bold')
                 
    ax.set_xlabel(r"Kinetic Momentum ($p_c$)", color='white', fontsize=14)
    ax.set_ylabel(r"Spatial Localization Variance ($\Delta x$)", color='white', fontsize=14)
    
    # Math Box overlay
    text_box = (r"$\mathbf{The\ AVE\ GUP\ Derivation}$" + "\n\n" +
                r"Continuum Limit (Heisenberg):" + "\n" +
                r"$\Delta x_{SM} = \frac{\hbar}{2 p_c}$" + "\n\n" +
                r"Discrete Matrix (Nyquist-Bounded GUP):" + "\n" +
                r"$\Delta x_{AVE} = \sqrt{(\Delta x_{SM})^2 + \left(\frac{\ell_{node}}{2}\right)^2}$" + "\n\n" +
                "As $p_c \to p_{max}$, the LC wavelength\n" +
                "approaches the discrete Nyquist limit.\n" +
                r"Instead of a UV singularity ($\Delta x \to 0$)," + "\n" +
                r"the localization structurally plateaus" + "\n" +
                r"at the $\ell_{node}/2$ grid resolution.")
                
    props = dict(boxstyle='round,pad=1', facecolor='#111122', alpha=0.9, edgecolor='#00ffff')
    ax.text(0.55, 0.45, text_box, transform=ax.transAxes, fontsize=13, color='white', bbox=props)
    
    ax.legend(loc='lower left', facecolor='black', edgecolor='white', labelcolor='white', fontsize=12)
    
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'ave_gup_resolution.png')
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    print(f"Saved formal GUP mathematical limit derivation to: {output_path}")

if __name__ == "__main__":
    generate_gup_resolution()
