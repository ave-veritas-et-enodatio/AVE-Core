import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import pathlib

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from periodic_table.simulations.simulate_element import get_nucleon_coordinates


def calculate_vacuum_density(nodes, X, Y, z_slice):
    density_field = np.zeros_like(X)
    amplitude, epsilon = 100.0, 0.5
    for cx, cy, cz in nodes:
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
        density_field += amplitude / (dist_sq + epsilon)
    return density_field


Z, A = 10, 20
bound, grid_res = 120.0, 80
title = "Neon-20 ($^{20}Ne$): Dynamic Bipyramid Flux"

nodes = get_nucleon_coordinates(Z, A)
if not nodes:
    print(f"Error executing Ne20 nodes")
    sys.exit(1)

z_min = min(n[2] for n in nodes) - 1.0
z_max = max(n[2] for n in nodes) + 1.0

x = np.linspace(-bound, bound, grid_res)
y = np.linspace(-bound, bound, grid_res)
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor("#0f0f0f")
ax.set_facecolor("#0f0f0f")

density = calculate_vacuum_density(nodes, X, Y, 0.0)
im = ax.imshow(density, extent=[-bound, bound, -bound, bound], origin="lower", cmap="hot", alpha=0.9, vmin=0.0)

stream_lines = ax.streamplot(
    x,
    y,
    np.gradient(density)[1],
    np.gradient(density)[0],
    color="#aaaaaa",
    linewidth=1.2,
    density=1.5,
    arrowstyle="->",
    arrowsize=1.5,
)
scat = ax.scatter([n[0] for n in nodes], [n[1] for n in nodes], color="#00ffcc", s=100)

ax.set_title(title, color="white", fontsize=14, pad=20)
ax.tick_params(colors="white")

frames = 30
z_slices = np.linspace(z_min, z_max, frames)
z_slices = np.concatenate([z_slices, z_slices[::-1]])  # Sweep and return


def update(frame):
    z_slice = z_slices[frame]
    density = calculate_vacuum_density(nodes, X, Y, z_slice)
    im.set_array(density)
    return [im]


anim = animation.FuncAnimation(fig, update, frames=len(z_slices), interval=100, blit=True)

outdir = "periodic_table/figures"
os.makedirs(outdir, exist_ok=True)
target = os.path.join(outdir, "neon_20_dynamic_flux.gif")
anim.save(target, writer="pillow", fps=15)
print(f"[*] Animation generated: {target}")
