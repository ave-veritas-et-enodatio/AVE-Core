# simulate_yee_cell_update.py
# Renders a rigorous mathematical 3D diagram of the standard FDTD Yee Cell,
# explicitly mapping the staggered spatial gradients (\nabla_d \times) that 
# govern the fundamental discrete limits of causality in the universe.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

def generate_yee_cell():
    """
    Renders the discrete spatial offsets of the E-field and H-field nodes.
    This explicit staggering prevents division-by-zero errors when calculating
    spatial curl operations across discrete distances (delta_x).
    """
    print("Constructing 3D Spatially-Staggered Yee Hardware Cell...")
    fig = plt.figure(figsize=(10, 10), facecolor='#050510')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#050510')

    # Base grid lines for spatial reference (Structural Edges)
    x = [0, 1, 1, 0, 0]
    y = [0, 0, 1, 1, 0]
    z_bottom = [0, 0, 0, 0, 0]
    z_top = [1, 1, 1, 1, 1]
    
    # Plot the wireframe cube (The physical node volume)
    ax.plot(x, y, z_bottom, color='#555555', linestyle='solid', alpha=0.4)
    ax.plot(x, y, z_top, color='#555555', linestyle='solid', alpha=0.4)
    for i in range(4):
        ax.plot([x[i], x[i]], [y[i], y[i]], [0, 1], color='#555555', linestyle='solid', alpha=0.4)
        
    # --- E-Field Components (Placed explicitly on the edges of the cell) ---
    e_color = '#00ffff'  # Cyan for Electric/Strain field
    # E_x (bottom-front edge)
    ax.quiver(0.2, 0, 0, 0.6, 0, 0, color=e_color, arrow_length_ratio=0.2, lw=4, label=r'Electric Field ($\mathbf{E}$)')
    # E_y (left-bottom edge)
    ax.quiver(0, 0.2, 0, 0, 0.6, 0, color=e_color, arrow_length_ratio=0.2, lw=4)
    # E_z (front-left edge)
    ax.quiver(0, 0, 0.2, 0, 0, 0.6, color=e_color, arrow_length_ratio=0.2, lw=4)

    # --- H-Field Components (Placed explicitly on the faces of the cell) ---
    # Shifted by exactly +0.5 delta_x/y/z
    h_color = '#ff00aa'  # Magenta for Magnetic/Kinematic field
    # H_x (center of left face)
    ax.quiver(0, 0.5, 0.5, 0.6, 0, 0, color=h_color, arrow_length_ratio=0.2, lw=4, label=r'Magnetic Field ($\mathbf{H}$)')
    # H_y (center of front face)
    ax.quiver(0.5, 0, 0.5, 0, 0.6, 0, color=h_color, arrow_length_ratio=0.2, lw=4)
    # H_z (center of bottom face)
    ax.quiver(0.5, 0.5, 0, 0, 0, 0.6, color=h_color, arrow_length_ratio=0.2, lw=4)

    # --- Labeling the specific mathematical node coordinates ---
    ax.text(0.5, 0, -0.1, r'$E_x[i+1/2, j, k]$', color=e_color, fontsize=12)
    ax.text(0, 0.5, -0.1, r'$E_y[i, j+1/2, k]$', color=e_color, fontsize=12)
    ax.text(-0.1, 0, 0.5, r'$E_z[i, j, k+1/2]$', color=e_color, fontsize=12)

    ax.text(0.6, 0.5, 0.5, r'$H_x[i, j+1/2, k+1/2]$', color=h_color, fontsize=12)
    ax.text(0.5, 0.6, 0.5, r'$H_y[i+1/2, j, k+1/2]$', color=h_color, fontsize=12)
    ax.text(0.5, 0.5, 0.6, r'$H_z[i+1/2, j+1/2, k]$', color=h_color, fontsize=12)

    # --- Formatting the plot ---
    ax.set_title("The Hardware Primitive: Spatially Staggered FDTD Matrix", color='white', pad=20, fontsize=16)
    
    # Hide axis ticks but keep the grid reference volume
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    
    # Adjust view angle for ideal 3D visibility
    ax.view_init(elev=25, azim=30)
    ax.axis('off')
    
    # Add Equation Proofs
    text_box = (r"$\mathbf{Discrete\ Spatial\ Curl\ (\nabla_d \times \mathbf{E})}$" + "\n\n" +
                r"$\partial E_z/\partial y \approx \frac{E_z[i, j+1, k] - E_z[i, j, k]}{\Delta y}$" + "\n" +
                r"$\partial E_y/\partial z \approx \frac{E_y[i, j, k+1] - E_y[i, j, k]}{\Delta z}$")
                
    props = dict(boxstyle='round,pad=1', facecolor='#111122', alpha=0.8, edgecolor=h_color)
    ax.text2D(0.05, 0.85, text_box, transform=ax.transAxes, fontsize=12, color='white', bbox=props)
    
    ax.legend(loc='upper right', facecolor='#000000', edgecolor='white', labelcolor='white')

    output_path = os.path.join(OUTPUT_DIR, 'fdtd_continuous_yee_mesh.pdf')
    plt.tight_layout()
    plt.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
    print(f"Saved mathematically staggered Yee Cell plot to: {output_path}")

if __name__ == "__main__":
    generate_yee_cell()
