# simulate_macroscopic_avalanche.py
# Simulates the gravitational induction field of a massive body
# and visibly renders the explicit tau > tau_yield breakdown threshold 
# where mutual zero-impedance occurs.
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

# ---- Macroscopic Constants (Normalized) ----
M_planet = 10.0   # Relative Mass of the central body
R_planet = 1.0    # Radius of the visible planet
TAU_YIELD = 1.5   # The absolute magnetic saturation limit of the lattice

def run_avalanche_simulation():
    """
    Renders a 2D cross-section of the spatial mutual inductance (eta_eff)
    surrounding a heavy gravitational mass. Identifies the exact Yield Horizon
    where conservative planetary orbits are physically guaranteed.
    """
    print("Evaluating Magnetic Saturation Shear Horizon...")
    fig, ax = plt.subplots(figsize=(12, 10), facecolor='#050510')
    ax.set_facecolor('#050510')
    
    # 1. Create a 2D spatial mesh
    N = 400
    x = np.linspace(-6, 6, N)
    y = np.linspace(-6, 6, N)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    
    # 2. Evaluate Local Gravitational Shear Stress (tau)
    # Newtonian gravity is an emergent gradient of this tensor strain
    # The topological shear scales inversely with R^2
    tau_field = M_planet / (R**2 + 1e-6)
    
    # 3. Apply the Axiom 4 Macroscopic Phase Transition
    # If tau > TAU_YIELD: The lattice breaks down into a frictionless slipstream (eta = 0)
    # If tau < TAU_YIELD: The lattice holds its native highly-reluctant mutual inductance (eta = eta_0)
    
    eta_0 = 1.0 # High native background drag (Dark Matter mechanism)
    
    eta_field = np.where(tau_field > TAU_YIELD, 0.0, eta_0)
    
    # Smooth the transition slightly for visual clarity 
    # (Representing a finite physical boundary layer thickness)
    import scipy.ndimage
    eta_field_smooth = scipy.ndimage.gaussian_filter(eta_field, sigma=2)
    
    # 4. Plot the resulting Inductive Drag Map
    # Brighter colors = Higher mutual inductance drag
    im = ax.imshow(eta_field_smooth, cmap='hot', extent=[-6, 6, -6, 6], origin='lower')
    
    # Add a colorbar
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label(r'Macroscopic Mutual Inductive Drag ($\eta_{eff}$)', color='white', size=14)
    cbar.ax.yaxis.set_tick_params(color='white')
    cbar.ax.yaxis.set_ticklabels(['0 (Slipstream)', 'High Drag (Deep Space)'], color='white')
    
    # 5. Render the physical mass (The Planet)
    planet = plt.Circle((0, 0), R_planet, color='#00aaff', fill=True, zorder=10)
    ax.add_patch(planet)
    ax.text(0, 0, "Mass\n(M)", color='black', fontsize=14, weight='bold', 
            ha='center', va='center', zorder=11)
            
    # 6. Render the exact Theoretical Yield Isocline
    # Where tau == TAU_YIELD -> R_yield = sqrt(M / TAU_YIELD)
    R_yield = np.sqrt(M_planet / TAU_YIELD)
    yield_boundary = plt.Circle((0, 0), R_yield, color='#00ff00', fill=False, 
                                linestyle='--', linewidth=3, zorder=5)
    ax.add_patch(yield_boundary)
    
    # Annotations
    ax.annotate(r"Phase Boundary: $\tau = \tau_{yield}$", 
                xy=(R_yield*0.7, R_yield*0.7), xytext=(3.5, 3.5),
                arrowprops=dict(facecolor='#00ff00', shrink=0.05),
                color="#00ff00", fontsize=14, weight='bold', zorder=12)
                
    ax.text(-5.5, -5.5, r"$\eta \to \eta_0$ (Unbroken Deep Space Drag)", color='#ff9900', fontsize=12)
    ax.text(-2.2, -2.2, r"$\eta \to 0$ (Frictionless Limit)", color='#ffffff', fontsize=14, weight='bold')
    
    ax.set_title("The Dielectric Avalanche: L-H Magnetic Saturation Limit", color='white', pad=20, fontsize=16)
    
    ax.axis('off')

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'dielectric_avalanche.png')
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    print(f"Saved exact Dielectric Avalanche topology map to: {output_path}")

if __name__ == "__main__":
    run_avalanche_simulation()
