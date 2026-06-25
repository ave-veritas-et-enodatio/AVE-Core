"""
AVE Heavy Nuclear Assembly Visualization (illustrative — NOT a Lattice QCD replacement).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script renders an animated 1/d topological optimization of 235 randomized
nucleons (with empirical proton/neutron masses M_P=1.00727, M_N=1.00866 amu
imported from PDG, NOT derived) using the AVE TopologicalOptimizer.

The original docstring claimed this script "replaces supercomputer-scale
Lattice QCD solvers" and "spontaneously assembles the precise crystalline
lattice of Uranium-235". Both claims overclaim what the code does:
  - The script does NOT compute U-235 binding energy (~7.59 MeV/nucleon NNDC)
  - The script does NOT compute U-235 cross-sections, decay rates, or shell
    structure that would falsify against PDG/NNDC data
  - The "lattice" produced is the optimizer's energy-minimum packing of
    point masses under the 1/d kernel — a geometric arrangement, not a
    benchmarked nuclear structure

The script DOES illustrate the AVE topological-assembly mechanism (1/d kernel
+ packing constraint as alternative to shell-model probabilistic framing).
That illustration is canonical to the framework's interpretive narrative.
Quantitative validation against NNDC nuclear-structure data is a separate
(open) work item.

Docstring corrected 2026-05-17.
"""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from ave.solvers.topology_optimizer import TopologicalOptimizer
from ave_path_util import sim_output

# Uranium-235 parameters
Z = 92  # Protons
A = 235  # Total Nucleons
N_neutrons = A - Z

# Base constants
M_P = 1.00727
M_N = 1.00866


def assemble_heavy_nucleus_dynamic() -> None:
    print("[*] Initializing Dynamic Topoloogical Synthesizer: 235 Nucleons (Uranium-235)")

    masses = []
    colors = []

    for _ in range(Z):
        masses.append(M_P)
        colors.append("#ff3333")  # Protons (Red)

    for _ in range(N_neutrons):
        masses.append(M_N)
        colors.append("#3333ff")  # Neutrons (Blue)

    # Start as a much larger, sparser unorganized gas clouds
    np.random.seed(42)
    box_size = 20.0
    initial_coords = np.random.uniform(-box_size, box_size, size=(A, 3))

    optimizer = TopologicalOptimizer(node_masses=masses, interaction_scale="nuclear")

    print("[*] Commencing Gradient Descent Assembly. Recording live state history...")

    # We don't need absolute strict convergence for the animation to look complete
    # (ftol 1e-3 is fine to get the main collapse sequence quickly)
    final_coords, total_energy, history, energy_history = optimizer.optimize(
        initial_coords,
        method="L-BFGS-B",
        options={"maxiter": 300, "ftol": 1e-4, "disp": False},
        record_history=True,
    )

    print(f"[+] Assembly Complete. Final Nuclear Impedance (Binding Energy proxy): {total_energy:.2f}")
    print(f"    -> Optimization Frames Recorded: {len(history)}")

    print("[*] Rendering Dynamic Assembly GIF...")
    fig = plt.figure(figsize=(10, 10))
    fig.patch.set_facecolor("#0f0f0f")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#0f0f0f")

    ax.grid(False)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    ax.set_title(
        "Nucleosynthesis Simulation: Uranium-235 Core Assembly\n(Dynamic $1/d$ Topological Gradient Descent)",
        color="white",
        fontsize=14,
        pad=20,
    )

    # Dynamic bounding
    all_coords_centered = history - np.mean(history[-1], axis=0)  # Centered on final origin
    c_max = min(box_size, np.max(np.abs(all_coords_centered[-1])) * 1.5)

    ax.set_xlim([-c_max, c_max])
    ax.set_ylim([-c_max, c_max])
    ax.set_zlim([-c_max, c_max])

    x0, y0, z0 = history[0][:, 0], history[0][:, 1], history[0][:, 2]
    # depthshade=False: matplotlib's 3D depth-shading desyncs the per-point
    # colour array against the z-order array for large scatters (a broadcast
    # ValueError at render time); disabling it keeps every nucleon coloured
    # correctly and is purely cosmetic.
    scat = ax.scatter(x0, y0, z0, c=colors, s=120, alpha=0.9, edgecolors="black", depthshade=False)
    energy_text = ax.text2D(0.05, 0.95, "", transform=ax.transAxes, color="#00ffcc", fontsize=14)

    # Pre-calculate centers to keep the camera focused
    centers = [np.mean(h, axis=0) for h in history]

    def update(frame: int) -> tuple:
        # Center the coordinates on the current center of mass so it doesn't drift
        coords = history[frame] - centers[frame]

        scat._offsets3d = (coords[:, 0], coords[:, 1], coords[:, 2])
        energy_text.set_text(f"Iter: {frame:03d} | Structural Impedance: {energy_history[frame]:.0f}")
        return scat, energy_text

    # Animate every frame
    anim = animation.FuncAnimation(fig, update, frames=len(history), interval=40, blit=False)

    # Render the final assembled state as the static PNG the manuscript embeds
    # (\includegraphics requires a raster/vector still, not the GIF). Build a
    # FRESH figure/scatter for the last frame: reusing the animation scatter via
    # _offsets3d leaves matplotlib's internal depth-order index stale, which
    # crashes the 3D renderer on large point counts.
    final_coords_centered = history[-1] - centers[-1]
    fig_s = plt.figure(figsize=(10, 10))
    fig_s.patch.set_facecolor("#0f0f0f")
    ax_s = fig_s.add_subplot(111, projection="3d")
    ax_s.set_facecolor("#0f0f0f")
    ax_s.grid(False)
    ax_s.xaxis.pane.fill = False
    ax_s.yaxis.pane.fill = False
    ax_s.zaxis.pane.fill = False
    ax_s.set_xticks([])
    ax_s.set_yticks([])
    ax_s.set_zticks([])
    ax_s.set_title(
        "Nucleosynthesis Simulation: Uranium-235 Core Assembly\n(Dynamic $1/d$ Topological Gradient Descent)",
        color="white",
        fontsize=14,
        pad=20,
    )
    ax_s.set_xlim([-c_max, c_max])
    ax_s.set_ylim([-c_max, c_max])
    ax_s.set_zlim([-c_max, c_max])
    ax_s.scatter(
        final_coords_centered[:, 0],
        final_coords_centered[:, 1],
        final_coords_centered[:, 2],
        c=colors,
        s=120,
        alpha=0.9,
        edgecolors="black",
        depthshade=False,
    )
    ax_s.text2D(
        0.05,
        0.95,
        f"Iter: {len(history) - 1:03d} | Structural Impedance: {energy_history[-1]:.0f}",
        transform=ax_s.transAxes,
        color="#00ffcc",
        fontsize=14,
    )
    png_target = sim_output("uranium_235_assembly_dynamic.png")
    fig_s.savefig(png_target, dpi=150, facecolor=fig_s.get_facecolor(), bbox_inches="tight")
    plt.close(fig_s)
    print(f"[*] Saved static U-235 assembly figure: {png_target}")

    target = sim_output("uranium_235_assembly_dynamic.gif")

    # The animated GIF reuses a single 3D scatter via _offsets3d, which can trip
    # a matplotlib depth-ordering bug on large point counts. The GIF is a bonus
    # artifact (the manuscript embeds the static PNG saved above), so a render
    # failure here must not fail the build-critical figure generation.
    try:
        anim.save(target, writer="pillow", fps=25)
        print(f"[*] Visualized Dynamic U-235 Assembly: {target}")
    except Exception as exc:  # noqa: BLE001 - GIF is non-critical, PNG already saved
        print(f"[!] Skipped GIF render (non-critical, static PNG already saved): {exc}")


if __name__ == "__main__":
    assemble_heavy_nucleus_dynamic()
