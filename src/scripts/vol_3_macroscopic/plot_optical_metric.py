import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os
import sys

# Aesthetic configuration
plt.style.use('dark_background')
COLOR_NODE = '#00ffff'
COLOR_GRID = '#ff00ff'

def _find_repo_root():
    """Find the Git repository root directory."""
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != '/':
        if os.path.isdir(os.path.join(current_dir, '.git')):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return os.path.abspath(os.path.dirname(__file__))  # Fallback

def plot_optical_metric():
    fig, ax = plt.subplots(figsize=(10, 8), dpi=150)
    ax.set_aspect('equal')
    ax.axis('off')

    # Grid parameters
    grid_size = 30
    x = np.linspace(-10, 10, grid_size)
    y = np.linspace(-10, 10, grid_size)
    X, Y = np.meshgrid(x, y)
    
    # Calculate radius from origin
    R = np.sqrt(X**2 + Y**2)
    
    # Avoid div by zero
    R_safe = np.clip(R, 0.5, None)
    
    # Ponderomotive force / Refractive index gradient 
    # n(r) = 1 + GM/c^2r. We simulate the density visually.
    density = 1.0 + 8.0 / (R_safe**1.5)
    
    # Normalize density for colormapping
    norm_density = (density - np.min(density)) / (np.max(density) - np.min(density))
    
    # Custom colormap from black -> purple -> cyan
    colors = ['#000000', '#220022', '#660066', '#aa00aa', '#00cccc', '#00ffff']
    cmap = LinearSegmentedColormap.from_list("ave_gravity", colors, N=256)
    
    # Plot background refractive density field
    heatmap = ax.contourf(X, Y, density, levels=200, cmap=cmap, alpha=0.6, zorder=1)
    
    # Plot distorted LC grid lines
    # Radial displacement inward to simulate geometric densification
    displacement_factor = 1.5 / R_safe
    X_disp = X - (X / R_safe) * displacement_factor
    Y_disp = Y - (Y / R_safe) * displacement_factor
    
    for i in range(grid_size):
        # We fade the grid lines near the center to let the bright core pop
        alpha_mask = np.clip(1.0 - (5.0 / (R_safe[i,:]**2)), 0.1, 0.8)
        
        # Horizontal lines
        for j in range(grid_size - 1):
            ax.plot([X_disp[i,j], X_disp[i,j+1]], [Y_disp[i,j], Y_disp[i,j+1]], 
                    color=COLOR_GRID, lw=0.8, alpha=alpha_mask[j], zorder=2)
            
        # Vertical lines
        alpha_mask_v = np.clip(1.0 - (5.0 / (R_safe[:,i]**2)), 0.1, 0.8)
        for j in range(grid_size - 1):
            ax.plot([X_disp[j,i], X_disp[j+1,i]], [Y_disp[j,i], Y_disp[j+1,i]], 
                    color=COLOR_GRID, lw=0.8, alpha=alpha_mask_v[j], zorder=2)

    # Plot the massive topological defect in the center
    circle1 = plt.Circle((0, 0), 0.6, color=COLOR_NODE, alpha=1.0, zorder=5)
    circle2 = plt.Circle((0, 0), 1.2, color=COLOR_NODE, alpha=0.4, zorder=4)
    circle3 = plt.Circle((0, 0), 2.5, color=COLOR_NODE, alpha=0.1, zorder=3)
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)
    
    # Title
    ax.set_title("Optical Metric: Gravity as Dielectric Refraction", fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    # Save Figure
    OUTPUT_DIR = os.path.join(_find_repo_root(), "assets", "sim_outputs")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    filename = "optical_refractive_gradient.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(filepath, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    print(f"Saved figure to: {filepath}")

if __name__ == "__main__":
    plot_optical_metric()
