import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pathlib

# Ensure the core framework is in PATH
project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from periodic_table.simulations.simulate_element import get_nucleon_coordinates

def rotate_cluster_y(nodes, angle):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    return [np.dot(R, n) for n in nodes]

def calculate_vacuum_density(nodes, X, Y, z_slice=0.0):
    density_field = np.zeros_like(X)
    amplitude, epsilon = 100.0, 0.5
    for cx, cy, cz in nodes:
        dist_sq = (X - cx)**2 + (Y - cy)**2 + (z_slice - cz)**2
        density_field += amplitude / (dist_sq + epsilon)
    return density_field

if __name__ == "__main__":
    Z, A = 2, 4
    bound, grid_res, frames = 3.0, 80, 60
    name = "helium_4"
    title = "Helium-4 ($^4He$): Dynamic Transverse Vacuum Strain"
    
    nodes = get_nucleon_coordinates(Z, A)
    if not nodes:
        print(f"Error: No coordinates for Z={2}, A={4}")
        sys.exit(1)

    x = np.linspace(-bound, bound, grid_res)
    y = np.linspace(-bound, bound, grid_res)
    X, Y = np.meshgrid(x, y)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor('#0f0f0f')
    
    def update(frame):
        ax.clear()
        ax.set_facecolor('#0f0f0f')
        angle = frame * (2 * np.pi / frames)
        rotated_nodes = rotate_cluster_y(nodes, angle)
        
        density = calculate_vacuum_density(rotated_nodes, X, Y)
        cmap = plt.cm.inferno
        cmap.set_bad(color='#0f0f0f')
        ax.imshow(density, extent=[-bound, bound, -bound, bound], origin='lower', cmap=cmap, alpha=0.9, vmin=0.0)
        
        grad_y, grad_x = np.gradient(density)
        ax.streamplot(x, y, grad_x, grad_y, color='#aaaaaa', linewidth=1.2, density=1.5, arrowstyle='->', arrowsize=1.5)
        
        for cx, cy, cz in rotated_nodes:
            depth_scale = np.exp(-np.abs(cz / (bound/3.0)))
            ax.scatter(cx, cy, color='#00ffcc', s=300 * depth_scale, marker='+', linewidth=2, alpha=0.8)
            ax.scatter(cx, cy, color='#00ffcc', s=100 * depth_scale, edgecolor='#00ffcc', facecolor='none', linewidth=1.5, alpha=0.9)
            
        ax.set_title(title, color='white', fontsize=16, pad=20)
        ax.tick_params(colors='white')
        
    print(f"[*] Rendering {name} GIF...")
    anim = FuncAnimation(fig, update, frames=frames, interval=80, blit=False)
    outdir = "../figures"
    os.makedirs(outdir, exist_ok=True)
    anim.save(os.path.join(outdir, "helium_4_dynamic_flux.gif"), writer='pillow', fps=15, savefig_kwargs={'facecolor': fig.get_facecolor()})
    print("[*] Done.")
