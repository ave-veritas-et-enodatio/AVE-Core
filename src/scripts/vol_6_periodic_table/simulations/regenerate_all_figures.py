#!/usr/bin/env python3
"""
AVE UNIFIED DENSITY FIGURE GENERATOR
=====================================
Regenerates ALL density/flux heatmap figures for the periodic table chapters.
All coordinates sourced from simulate_element.py (which uses ave.core.constants).
Outputs directly to periodic_table/figures/ for LaTeX inclusion.
"""
import os
import sys
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import pathlib

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from periodic_table.simulations.simulate_element import get_nucleon_coordinates

REPO_ROOT = pathlib.Path(__file__).parent.parent.parent.parent.absolute()
OUTDIR = os.path.join(REPO_ROOT, "periodic_table", "figures")
os.makedirs(OUTDIR, exist_ok=True)


def density_field_inv_r(nodes, X, Y, z_slice=0.0):
    density = np.zeros_like(X)
    Z = np.full_like(X, z_slice)
    for nx, ny, nz in nodes:
        r = np.sqrt((X - nx) ** 2 + (Y - ny) ** 2 + (Z - nz) ** 2)
        r = np.clip(r, 0.4, None)
        density += 1.0 / r
    return density


def density_field_inv_r2(nodes, X, Y, z_slice=0.0):
    density = np.zeros_like(X)
    for cx, cy, cz in nodes:
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
        density += 100.0 / (dist_sq + 0.5)
    return density


def plot_density_hot(nodes, bounds, z_slice, title, filename):
    grid_size = 400
    xs = np.linspace(-bounds, bounds, grid_size)
    ys = np.linspace(-bounds, bounds, grid_size)
    X, Y = np.meshgrid(xs, ys)
    density = density_field_inv_r(nodes, X, Y, z_slice)

    fig, ax = plt.subplots(figsize=(10, 8), facecolor="black")
    ax.set_facecolor("black")
    vmax_val = 14 if len(nodes) > 10 else 12
    im = ax.imshow(
        density,
        extent=[X.min(), X.max(), Y.min(), Y.max()],
        origin="lower",
        cmap="hot",
        alpha=0.9,
        vmin=0,
        vmax=vmax_val,
    )
    DY, DX = np.gradient(density)
    ax.streamplot(X, Y, DX, DY, color="white", linewidth=0.5, density=1.5, arrowsize=0.8)
    for nx, ny, nz in nodes:
        if abs(nz - z_slice) < 5.0:
            ax.plot(nx, ny, "wo", markersize=3, alpha=0.8)
            ax.plot(nx, ny, "co", markersize=6, alpha=0.4)
    ax.set_title(title, color="white", pad=20)
    ax.set_xlabel(r"Spatial Radius ($d$)  [$d \approx 0.841$ fm]", color="white")
    ax.set_ylabel(r"Spatial Radius ($d$)  [fm]", color="white")
    ax.tick_params(colors="white")
    cbar = plt.colorbar(im, ax=ax, label="Vacuum Strain Density ($1/d$)")
    cbar.ax.yaxis.label.set_color("white")
    plt.gcf().axes[-1].tick_params(colors="white")
    plt.savefig(filename, dpi=300, bbox_inches="tight", facecolor="black")
    plt.close()
    print(f"  [ok] {os.path.basename(filename)}")


def plot_flux_inferno(nodes, bounds, z_slice, title, filename, grid_res=120):
    x = np.linspace(-bounds, bounds, grid_res)
    y = np.linspace(-bounds, bounds, grid_res)
    X, Y = np.meshgrid(x, y)
    density = density_field_inv_r2(nodes, X, Y, z_slice)

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#0f0f0f")
    ax.set_facecolor("#0f0f0f")
    cmap = plt.cm.inferno.copy()
    cmap.set_bad(color="#0f0f0f")
    ax.imshow(
        density,
        extent=[-bounds, bounds, -bounds, bounds],
        origin="lower",
        cmap=cmap,
        alpha=0.9,
        vmin=0.0,
    )
    grad_y, grad_x = np.gradient(density)
    ax.streamplot(
        x,
        y,
        grad_x,
        grad_y,
        color="#aaaaaa",
        linewidth=1.2,
        density=1.5,
        arrowstyle="->",
        arrowsize=1.5,
    )
    for cx, cy, cz in nodes:
        depth_scale = np.exp(-np.abs(cz / (bounds / 3.0)))
        ax.scatter(cx, cy, color="#00ffcc", s=300 * depth_scale, marker="+", linewidth=2, alpha=0.8)
        ax.scatter(
            cx,
            cy,
            color="#00ffcc",
            s=100 * depth_scale,
            edgecolor="#00ffcc",
            facecolor="none",
            linewidth=1.5,
            alpha=0.9,
        )
    ax.set_title(title, color="white", fontsize=16, pad=20)
    ax.set_xlabel(r"Spatial Radius ($d$)  [$d \approx 0.841$ fm]", color="white", fontsize=11)
    ax.set_ylabel(r"Spatial Radius ($d$)  [fm]", color="white", fontsize=11)
    ax.tick_params(colors="white")
    plt.savefig(filename, facecolor=fig.get_facecolor(), dpi=300, bbox_inches="tight")
    plt.close()
    print(f"  [ok] {os.path.basename(filename)}")


elements = [
    ("hydrogen_1", 1, 1, 10.0, [0], 10.0, "Hydrogen-1: Protium Vacuum Flux"),
    ("helium_4", 2, 4, 10.0, [0, 0.81], 10.0, "Helium-4: Alpha Particle Strain"),
    ("lithium_7", 3, 7, 15.0, [0, 9.72], 15.0, "Lithium-7: Core + Halo Strain"),
    ("beryllium_9", 4, 9, 15.0, [0, 5.0], 15.0, "Beryllium-9: 2a + Neutron Strain"),
    ("boron_11", 5, 11, 15.0, [0], 20.0, "Boron-11: 2a + Tritium Strain"),
    ("carbon_12", 6, 12, 65.0, [0], 65.0, "Carbon-12: 3a Ring Strain"),
    ("nitrogen_14", 7, 14, 30.0, [0, 5.0], 30.0, "Nitrogen-14: 3a + Deuteron Strain"),
    ("oxygen_16", 8, 16, 75.0, [0], 75.0, "Oxygen-16: 4a Tetrahedron Strain"),
    ("fluorine_19", 9, 19, 420.0, [0], 420.0, "Fluorine-19: 4a + Tritium Halo"),
    ("neon_20", 10, 20, 100.0, [0], 100.0, "Neon-20: 5a Bipyramid Strain"),
    ("sodium_23", 11, 23, 100.0, [0], 100.0, "Sodium-23: 5a + Tritium Halo"),
    ("magnesium_24", 12, 24, 100.0, [0], 100.0, "Magnesium-24: 6a Octahedron Strain"),
    ("aluminum_27", 13, 27, 110.0, [0], 110.0, "Aluminum-27: 6a + Tritium Halo"),
    ("silicon_28", 14, 28, 110.0, [0], 110.0, "Silicon-28: 7a Pentagonal Bipyramid"),
    ("sulfur_32", 16, 32, 120.0, [0], 120.0, "Sulfur-32: Large Signal Avalanche"),
    ("argon_40", 18, 40, 140.0, [0], 140.0, "Argon-40: Bicapped Antiprism"),
    ("calcium_40", 20, 40, 140.0, [0], 140.0, "Calcium-40: Large Signal Alkaline Earth"),
    ("titanium_48", 22, 48, 160.0, [0], 160.0, "Titanium-48: Cuboctahedral Packing"),
    ("chromium_52", 24, 52, 170.0, [0], 170.0, "Chromium-52: Icosahedron+1 Packing"),
    ("iron_56", 26, 56, 180.0, [0], 180.0, "Iron-56: FCC-14 Peak Stability"),
]


if __name__ == "__main__":
    print("=" * 70)
    print("AVE UNIFIED DENSITY FIGURE GENERATOR")
    print(f"Output: {OUTDIR}")
    print("=" * 70)

    for name, Z, A, d_bounds, d_slices, f_bounds, f_title in elements:
        print(f"\n--- {name.replace('_', ' ').title()} (Z={Z}, A={A}) ---")
        nodes = get_nucleon_coordinates(Z, A)
        if not nodes:
            print(f"  [!] No coordinates found")
            continue

        for z_slice in d_slices:
            label = "equator" if z_slice == 0 else "z_pos"
            fn = os.path.join(OUTDIR, f"{name}_density_{label}.png")
            title = f"{name.replace('_', ' ').title()}\nVacuum Strain Density ($Z={z_slice}d$)"
            plot_density_hot(nodes, d_bounds, z_slice, title, fn)

        fn_flux = os.path.join(OUTDIR, f"{name}_dynamic_flux.png")
        plot_flux_inferno(nodes, f_bounds, 0.0, f_title, fn_flux)

    print(f"\n{'=' * 70}")
    print("ALL FIGURES REGENERATED")
    print("=" * 70)
