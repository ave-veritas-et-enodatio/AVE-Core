"""
Macroscopic Orbital Simulator (Applied Vacuum Engineering)
========================================================
Demonstrates the scale-invariance of the 1/d topological framework.
Uses a simple N-body Verlet / Euler integrator to evolve a massive 
central node (Saturn) and N test-mass nodes (ice ring particles) 
over time in 3D space.

╔══════════════════════════════════════════════════════════════════╗
║  NOTE: This is a DIMENSIONLESS TOY MODEL.                       ║
║  G=1.0 and M_SATURN=10000 are computational parameters, NOT     ║
║  physical constants. No physics predictions are made here.       ║
║  For real Saturn ring gap physics, see:                          ║
║    src/ave/gravity/solar_impedance.py → saturn_ring_gap_model()  ║
╚══════════════════════════════════════════════════════════════════╝

Generates an animated GIF of the structural evolution.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pathlib

project_root = pathlib.Path(__file__).parent.parent.absolute()

# JAX GPU acceleration (graceful fallback to numpy)
try:
    import jax

    jax.config.update("jax_enable_x64", True)
    _HAS_JAX = True
except ImportError:
    _HAS_JAX = False

# ── DIMENSIONLESS TOY PARAMETERS (NOT physics constants) ──────────────────
# These are computational parameters for the N-body demo.
# For real Saturn physics, use ave.gravity.solar_impedance.saturn_ring_gap_model()
G = 1.0  # Dimensionless gravitational coupling
M_SATURN = 10000.0  # Dimensionless central mass

# Ring Particles
N_PARTICLES = 1000
M_PARTICLE = 0.01

# Simulation Parameters
DT = 0.05
FRAMES = 500


def initialize_rings():
    """
    Initializes N particles in a flat, uniformly dense Keplerian
    disk around the central mass.
    """
    # Central Mass (Saturn) at Origin
    positions = [np.array([0.0, 0.0, 0.0])]
    velocities = [np.array([0.0, 0.0, 0.0])]
    masses = [M_SATURN]

    # Ring Limits
    R_inner = 20.0
    R_outer = 60.0

    for _ in range(N_PARTICLES):
        # Random position in the disk (r, theta) -> (x, y)
        r = np.random.uniform(R_inner, R_outer)
        theta = np.random.uniform(0, 2 * np.pi)

        # Add slight Z-axis variance (ring thickness)
        z = np.random.normal(0, 0.5)

        pos = np.array([r * np.cos(theta), r * np.sin(theta), z])

        # Keplerian orbital velocity v = sqrt(G*M/r)
        v_mag = np.sqrt(G * M_SATURN / r)

        # Velocity vector is perpendicular to position vector in XY plane
        # Cross product of position and Z-axis unit vector
        v_dir = np.array([-pos[1], pos[0], 0.0]) / r
        vel = v_dir * v_mag

        positions.append(pos)
        velocities.append(vel)
        masses.append(M_PARTICLE)

    return np.array(positions), np.array(velocities), np.array(masses)


def compute_accelerations(pos, masses):
    """
    Calculates the N-body gravitational/topological acceleration matrix.
    a_i = SUM( G * m_j * r_ij / |r_ij|^3 )
    Fully vectorized — no Python loops.
    """
    epsilon = 0.5
    # r_vec[i, j] = pos[j] - pos[i]  shape: (N, N, 3)
    r_vec = pos[np.newaxis, :, :] - pos[:, np.newaxis, :]
    # dist_sq[i, j] = |r_ij|^2 + eps^2  shape: (N, N)
    dist_sq = np.sum(r_vec**2, axis=2) + epsilon**2
    dist = np.sqrt(dist_sq)
    # f_mag[i, j] = G / (dist_sq * dist)  shape: (N, N)
    f_mag = G / (dist_sq * dist)
    # Zero self-interaction
    np.fill_diagonal(f_mag, 0.0)
    # acc[i] = sum_j( f_mag[i,j] * m[j] * r_vec[i,j] )
    acc = np.sum(f_mag[:, :, np.newaxis] * masses[np.newaxis, :, np.newaxis] * r_vec, axis=1)
    return acc


def simulate_rings():
    print(f"[*] Initializing {N_PARTICLES} ring particles around Saturn...")
    pos, vel, masses = initialize_rings()

    # Store history for animation: shape (FRAMES, N_PARTICLES+1, 3)
    history = np.zeros((FRAMES, len(masses), 3))

    print("[*] Evolving macroscopic topological manifold...")

    # Initial acceleration
    acc = compute_accelerations(pos, masses)

    for step in range(FRAMES):
        if step % 20 == 0:
            print(f"    -> Timestep {step}/{FRAMES}")

        # Velocity Verlet Integration
        # 1. Update positions
        pos = pos + vel * DT + 0.5 * acc * (DT**2)
        history[step] = pos.copy()

        # 2. Update accelerations at new position
        new_acc = compute_accelerations(pos, masses)

        # 3. Update velocities
        vel = vel + 0.5 * (acc + new_acc) * DT
        acc = new_acc

    return history


def animate_simulation(history):
    print("[*] Rendering 3D Temporal Evolution GIF...")

    fig = plt.figure(figsize=(10, 10))
    # Dark modern background
    fig.patch.set_facecolor("#050510")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#050510")

    # Plot configuration
    lim = 80.0
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_zlim([-lim / 4, lim / 4])

    # Style axes
    ax.grid(False)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor("#050510")
    ax.yaxis.pane.set_edgecolor("#050510")
    ax.zaxis.pane.set_edgecolor("#050510")

    # Hide axis ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Initialize scatter plots
    # Index 0 is Saturn
    (saturn_scatter,) = ax.plot([], [], [], "o", color="#ffcc66", markersize=35, alpha=0.9)
    (rings_scatter,) = ax.plot([], [], [], ".", color="#a0d0ff", markersize=2, alpha=0.6)

    title = ax.set_title(
        "Macroscopic 1/d Topological Evolution\nSaturn Ring Network",
        color="white",
        fontsize=14,
        pad=20,
    )

    def update(frame):
        # Extract frame data
        frame_pos = history[frame]

        # Saturn
        saturn_pos = frame_pos[0]
        saturn_scatter.set_data(np.array([saturn_pos[0]]), np.array([saturn_pos[1]]))
        saturn_scatter.set_3d_properties(np.array([saturn_pos[2]]))

        # Rings
        ring_pos = frame_pos[1:]
        rings_scatter.set_data(ring_pos[:, 0], ring_pos[:, 1])
        rings_scatter.set_3d_properties(ring_pos[:, 2])

        # Slowly rotate the camera angle over time
        ax.view_init(elev=30 - frame * 0.1, azim=frame * 0.5)

        return saturn_scatter, rings_scatter, title

    anim = animation.FuncAnimation(fig, update, frames=FRAMES, interval=50, blit=False)

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "saturn_rings_evolution.gif"

    anim.save(target, writer="pillow", fps=20)
    print(f"[*] Scale-Invariant Topology Generated: {target}")


if __name__ == "__main__":
    hist = simulate_rings()
    animate_simulation(hist)
