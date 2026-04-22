import os
import pathlib
import sys

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from periodic_table.simulations.simulate_element import get_nucleon_coordinates

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()


def calculate_vacuum_density(nodes, X, Y, z_slice):
    density_field = np.zeros_like(X)
    amplitude, epsilon = 100.0, 0.5
    for cx, cy, cz in nodes:
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
        density_field += amplitude / (dist_sq + epsilon)
    return density_field


Z, A = 13, 27
bound, grid_res = 180.0, 80
title = "Aluminum-27 ($^{27}Al$): X-Z Plane Structural Sweep"

nodes = get_nucleon_coordinates(Z, A)
if not nodes:
    sys.exit(1)

z_min = min(n[1] for n in nodes) - 1.0
z_max = max(n[1] for n in nodes) + 1.0

# Render X-Z plane and sweep the Y-axis (depth)
x = np.linspace(-bound, bound, grid_res)
z = np.linspace(-bound, bound, grid_res)
X, Z = np.meshgrid(x, z)

fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor("#0f0f0f")
ax.set_facecolor("#0f0f0f")

density = calculate_vacuum_density([(n[0], n[2], n[1]) for n in nodes], X, Z, 0.0)
im = ax.imshow(density, extent=[-bound, bound, -bound, bound], origin="lower", cmap="hot", alpha=0.9, vmin=0.0)

stream_lines = ax.streamplot(
    x,
    z,
    np.gradient(density)[1],
    np.gradient(density)[0],
    color="#aaaaaa",
    linewidth=1.2,
    density=1.5,
    arrowstyle="->",
    arrowsize=1.5,
)
scat = ax.scatter([n[0] for n in nodes], [n[2] for n in nodes], color="#00ffcc", s=80)

ax.set_title(title, color="white", fontsize=14, pad=20)
ax.tick_params(colors="white")

frames = 30
y_slices = np.linspace(z_min, z_max, frames)
y_slices = np.concatenate([y_slices, y_slices[::-1]])


def update(frame):
    y_slice = y_slices[frame]
    density = calculate_vacuum_density([(n[0], n[2], n[1]) for n in nodes], X, Z, y_slice)
    im.set_array(density)
    return [im]


anim = animation.FuncAnimation(fig, update, frames=len(y_slices), interval=100, blit=True)

outdir = "periodic_table/figures"
os.makedirs(outdir, exist_ok=True)
target = os.path.join(outdir, "aluminum_27_dynamic_flux.gif")
anim.save(target, writer="pillow", fps=15)
print(f"[*] Animation generated: {target}")
