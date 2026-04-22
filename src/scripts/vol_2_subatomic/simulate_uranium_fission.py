"""
AVE Topological Fission Simulator
======================================================
Models the MACROSCOPIC sheer-failure mechanism of U-235 nuclear fission.
Instead of relying on quantum probabilities, we compute the explicit
$1/d$ topological strain matrix of the U-235 nucleus. Upon impact
by a thermal neutron, the lattice experiences an impedance rupture,
shearing into two stable daughter lattices (Ba-141 + Kr-92) which
are then violently ejected by long-range Coulomb repulsion.
"""

import os
import pathlib

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from ave.solvers.topology_optimizer import TopologicalOptimizer

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()
# Simulation Parameters
Z = 92  # Protons in U-235
A = 235  # Total nucleons in U-235
N_neutrons = A - Z

M_P = 1.00727
M_N = 1.00866

# Force Constants
K_ATTR = 20.0
K_REP = 500.0
R_MIN = 1.0
K_COULOMB = 4.0  # Proton-proton long range repulsion

DT = 0.005
FRAMES = 150


def run_fission_simulation() -> None:
    print("[*] Initializing U-235 Core Topology...")
    masses = []
    is_proton = []
    colors = []

    for _ in range(Z):
        masses.append(M_P)
        is_proton.append(True)
        colors.append("#ff3333")  # Red

    for _ in range(N_neutrons):
        masses.append(M_N)
        is_proton.append(False)
        colors.append("#3333ff")  # Blue

    # Standard convergence to get a stable U-235 core
    np.random.seed(42)
    box_size = 5.0
    initial_coords = np.random.uniform(-box_size, box_size, size=(A, 3))

    optimizer = TopologicalOptimizer(node_masses=masses, interaction_scale="nuclear")
    print("[*] Annealing nucleus to lowest topological strain...")
    core_coords, _, _, _ = optimizer.optimize(
        initial_coords,
        method="L-BFGS-B",
        options={"maxiter": 200, "ftol": 1e-4, "disp": False},
        record_history=True,
    )

    # Add the thermal neutron
    masses.append(M_N)
    is_proton.append(False)
    colors.append("#00ffcc")  # Cyan thermal neutron

    # Position the neutron just outside the core, aimed directly at it
    neutron_pos = np.array([8.0, 0.5, 0.5])
    neutron_vel = np.array([-15.0, 0.0, 0.0])  # Fast velocity vector

    pos = np.vstack([core_coords, neutron_pos])
    vel = np.zeros_like(pos)
    vel[-1] = neutron_vel

    mass_arr = np.array(masses)
    proton_arr = np.array(is_proton)

    history = np.zeros((FRAMES, A + 1, 3))

    def compute_accelerations(p: np.ndarray) -> np.ndarray:
        N = len(mass_arr)
        acc = np.zeros((N, 3))

        for i in range(N):
            for j in range(i + 1, N):
                r_vec = p[i] - p[j]
                dist_sq = np.sum(r_vec**2) + 0.001
                dist = np.sqrt(dist_sq)

                m_prod = mass_arr[i] * mass_arr[j]
                force_mag = 0.0

                # Strong Nuclear Force (short range 1/d topology)
                if dist < R_MIN:
                    # Repulsion core
                    force_mag += 3.0 * m_prod * K_REP * (R_MIN**3 / (dist**4))
                else:
                    # Attraction (exponential decay to cut off strong force at long ranges)
                    # This is key for fission: strong force must drop off so Coulomb can push them apart
                    decay = np.exp(-(dist - R_MIN) / 1.5)
                    force_mag -= m_prod * K_ATTR * decay / dist_sq

                # Coulomb Repulsion (long range, only between protons)
                if proton_arr[i] and proton_arr[j]:
                    force_mag += K_COULOMB / dist_sq

                # Apply force
                # force_mag > 0 means pushing apart (r_vec points from j to i)
                f_vec = force_mag * (r_vec / dist)

                acc[i] += f_vec / mass_arr[i]
                acc[j] -= f_vec / mass_arr[j]

        return acc

    print("[*] Executing Topological Sheer-Fracture (Time Integration)...")
    acc = compute_accelerations(pos)

    for step in range(FRAMES):
        if step % 20 == 0:
            print(f"    -> Timestep {step}/{FRAMES}")

        pos = pos + vel * DT + 0.5 * acc * (DT**2)
        history[step] = pos.copy()

        new_acc = compute_accelerations(pos)
        vel = vel + 0.5 * (acc + new_acc) * DT
        acc = new_acc

    print("[*] Rendering 3D Fission Event GIF...")

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
        "Macroscopic Topological Fission (U-235 + n $\\rightarrow$ Ba-141 + Kr-92)"
        "\nStrain Rupture via Thermal Neutron Impact",
        color="white",
        fontsize=14,
        pad=20,
    )

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    x0, y0, z0 = history[0][:, 0], history[0][:, 1], history[0][:, 2]
    scat = ax.scatter(x0, y0, z0, c=colors, s=80, alpha=0.9, edgecolors="black")
    time_text = ax.text2D(0.05, 0.95, "", transform=ax.transAxes, color="#00ffcc", fontsize=14)

    def update(frame: int) -> tuple:
        coords = history[frame]
        scat._offsets3d = (coords[:, 0], coords[:, 1], coords[:, 2])
        time_text.set_text(f"Atto-second t={frame * DT * 1000:.1f}")
        return scat, time_text

    anim = animation.FuncAnimation(fig, update, frames=FRAMES, interval=40, blit=False)

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "topological_fission_dynamic.gif"

    anim.save(target, writer="pillow", fps=25)
    print(f"[*] Visualized Macroscopic Fission Dynamics: {target}")


if __name__ == "__main__":
    run_fission_simulation()
