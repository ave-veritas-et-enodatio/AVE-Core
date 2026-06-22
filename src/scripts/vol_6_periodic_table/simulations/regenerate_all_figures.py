#!/usr/bin/env python3
"""
AVE UNIFIED DENSITY FIGURE GENERATOR
=====================================
Regenerates ALL density/flux heatmap figures for the periodic table chapters
(``manuscript/vol_6_periodic_table/figures/``, which the chapters
``\\includegraphics``).

HONESTY NOTE (ave-driver-script-honesty)
----------------------------------------
The scalar field is built by ``density_field_inv_*`` as a sum of analytic
``1/r`` / ``1/(r^2+c)`` kernels placed at the REAL solved nucleon coordinates
returned by ``get_nucleon_coordinates(Z, A)`` in ``simulate_element.py``. The
field's STRUCTURE (number of centres, multi-alpha lattice, halo offsets,
per-element stretch) is therefore the real solved geometry — this is NOT the
Z-cancelling single-centre topology glow that was dropped. What is NOT
engine-solved is the per-point MAGNITUDE: it is a geometric proximity envelope,
not the converged strain/permittivity field. So the layer is KEPT and rendered
honestly (white house style, CMAP_SEQ + colorbar with units), but the colorbar
is labelled as the geometric node-proximity field it actually is, not as an
"engine strain density". See the figure-pass flag list.

All coordinates sourced from simulate_element.py (which uses ave.core.constants).
"""
import os
import pathlib
import sys
import types

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

# Path bootstrap (FLAGGED provenance fix): the simulation package directory is
# named ``vol_6_periodic_table`` on disk, but these drivers import it under the
# alias ``periodic_table`` (per src/scripts/AGENTS.md). The directory has no
# __init__.py (namespace pkg), so register it under the ``periodic_table`` name
# here. Without this the driver raises ModuleNotFoundError and the manuscript
# density/flux PNGs cannot be regenerated. See the figure-pass flag list.
if "periodic_table" not in sys.modules:
    _pt_dir = pathlib.Path(__file__).resolve().parent.parent  # .../vol_6_periodic_table
    _pt = types.ModuleType("periodic_table")
    _pt.__path__ = [str(_pt_dir)]
    sys.modules["periodic_table"] = _pt

from ave.viz import style  # noqa: E402
from ave_path_util import manuscript_path  # noqa: E402
from periodic_table.simulations.simulate_element import get_nucleon_coordinates  # noqa: E402

style.apply()  # white print profile (house style); call once before any figure.

# The chapters \includegraphics{figures/<name>_density_*.png} from the manuscript
# tree, so write there (not a hand-rolled src/periodic_table path, which does not
# exist and silently dropped output away from the manuscript).
OUTDIR = str(manuscript_path("vol_6_periodic_table", "figures"))

# Honest colorbar label for the geometric node-proximity field (NOT an
# engine-solved strain density — see the module honesty note).
_CBAR_LABEL = style.axis_label("Node-proximity field", r"\rho_{\mathrm{geom}}", "1/d")


def density_field_inv_r(nodes: list, X: np.ndarray, Y: np.ndarray, z_slice: float = 0.0) -> np.ndarray:
    density = np.zeros_like(X)
    Z = np.full_like(X, z_slice)
    for nx, ny, nz in nodes:
        r = np.sqrt((X - nx) ** 2 + (Y - ny) ** 2 + (Z - nz) ** 2)
        r = np.clip(r, 0.4, None)
        density += 1.0 / r
    return density


def density_field_inv_r2(nodes: list, X: np.ndarray, Y: np.ndarray, z_slice: float = 0.0) -> np.ndarray:
    density = np.zeros_like(X)
    for cx, cy, cz in nodes:
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
        density += 100.0 / (dist_sq + 0.5)
    return density


def plot_density_hot(nodes: list, bounds: float, z_slice: float, filename: str) -> None:
    grid_size = 400
    xs = np.linspace(-bounds, bounds, grid_size)
    ys = np.linspace(-bounds, bounds, grid_size)
    X, Y = np.meshgrid(xs, ys)
    density = density_field_inv_r(nodes, X, Y, z_slice)

    fig, ax = plt.subplots(figsize=style.figsize("square"))
    vmax_val = 14 if len(nodes) > 10 else 12
    im = ax.imshow(
        density,
        extent=[X.min(), X.max(), Y.min(), Y.max()],
        origin="lower",
        cmap=style.CMAP_SEQ,
        vmin=0,
        vmax=vmax_val,
    )
    DY, DX = np.gradient(density)
    # Light-grey streamlines read against the dark (low-field) magma background
    # while staying subordinate to the colormap; nodes in house blue.
    ax.streamplot(X, Y, DX, DY, color="#cccccc", linewidth=0.5, density=1.5, arrowsize=0.8)
    for nx, ny, nz in nodes:
        if abs(nz - z_slice) < 5.0:
            ax.plot(nx, ny, "o", color="#56B4E9", markersize=5, alpha=0.95)
    ax.set_xlabel(style.axis_label("Spatial radius", "x", "d (0.841 fm)"))
    ax.set_ylabel(style.axis_label("Spatial radius", "y", "d (0.841 fm)"))
    cbar = plt.colorbar(im, ax=ax, label=_CBAR_LABEL)  # noqa: F841
    # No on-figure title: the chapter supplies the LaTeX \caption.
    style.save(fig, filename, formats=("png",))
    plt.close(fig)
    print(f"  [ok] {os.path.basename(filename)}")


def plot_flux_inferno(nodes: list, bounds: float, z_slice: float, filename: str, grid_res: int = 120) -> None:
    x = np.linspace(-bounds, bounds, grid_res)
    y = np.linspace(-bounds, bounds, grid_res)
    X, Y = np.meshgrid(x, y)
    density = density_field_inv_r2(nodes, X, Y, z_slice)

    fig, ax = plt.subplots(figsize=style.figsize("square"))
    im = ax.imshow(
        density,
        extent=[-bounds, bounds, -bounds, bounds],
        origin="lower",
        cmap=style.CMAP_SEQ,
        vmin=0.0,
    )
    grad_y, grad_x = np.gradient(density)
    # Light-grey flux arrows read against the dark (low-field) magma background;
    # nodes in house blue.
    ax.streamplot(
        x,
        y,
        grad_x,
        grad_y,
        color="#cccccc",
        linewidth=1.0,
        density=1.5,
        arrowstyle="->",
        arrowsize=1.2,
    )
    for cx, cy, cz in nodes:
        depth_scale = np.exp(-np.abs(cz / (bounds / 3.0)))
        ax.scatter(cx, cy, color="#56B4E9", s=120 * depth_scale, marker="+", linewidth=2, alpha=0.95)
    ax.set_xlabel(style.axis_label("Spatial radius", "x", "d (0.841 fm)"))
    ax.set_ylabel(style.axis_label("Spatial radius", "y", "d (0.841 fm)"))
    cbar = plt.colorbar(im, ax=ax, label=_CBAR_LABEL)  # noqa: F841
    # No on-figure title: the chapter supplies the LaTeX \caption.
    style.save(fig, filename, formats=("png",))
    plt.close(fig)
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

    for name, Z, A, d_bounds, d_slices, f_bounds, _f_title in elements:
        print(f"\n--- {name.replace('_', ' ').title()} (Z={Z}, A={A}) ---")
        nodes = get_nucleon_coordinates(Z, A)
        if not nodes:
            print("  [!] No coordinates found")
            continue

        for z_slice in d_slices:
            label = "equator" if z_slice == 0 else "z_pos"
            fn = os.path.join(OUTDIR, f"{name}_density_{label}.png")
            plot_density_hot(nodes, d_bounds, z_slice, fn)

        fn_flux = os.path.join(OUTDIR, f"{name}_dynamic_flux.png")
        plot_flux_inferno(nodes, f_bounds, 0.0, fn_flux)

    print(f"\n{'=' * 70}")
    print("ALL FIGURES REGENERATED")
    print("=" * 70)
