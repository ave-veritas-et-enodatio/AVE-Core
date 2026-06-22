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

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from ave.viz import style
from ave_path_util import sim_output

# House figure style (white "print" profile, Okabe-Ito palette, no baked titles).
# Presentation tier only — no ave.core dependency, so the dimensionless-toy
# isolation below is preserved (ave-figure-discipline / ave.viz README).
style.apply()

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


def initialize_rings() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
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


def compute_accelerations(pos: np.ndarray, masses: np.ndarray) -> np.ndarray:
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


def simulate_rings() -> np.ndarray:
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


# Saturn-disk axis extent: the ring is initialised in R_inner..R_outer = 20..60
# with N(0, 0.5) vertical thickness, so the data live in a flat disk of radius
# ~60 and half-thickness ~2. The previous render set xy-limits to +/-80 and a
# z-limit of +/-20 — the disk filled ~10% of a vast empty box and read as a thin
# band (ave-figure-discipline Axis 3 rendering defect). Frame the data instead.
_XY_LIM = 65.0   # snug around R_outer = 60
_Z_LIM = 8.0     # snug around the ~+/-2 ring thickness (slight headroom)


def _draw_frame(ax, frame_pos: np.ndarray, *, elev: float, azim: float) -> None:
    """Draw one N-body frame onto ``ax`` in the house palette (no clipping)."""
    ax.clear()
    ax.set_xlim([-_XY_LIM, _XY_LIM])
    ax.set_ylim([-_XY_LIM, _XY_LIM])
    ax.set_zlim([-_Z_LIM, _Z_LIM])
    ax.set_box_aspect((1, 1, 0.28))  # honour the flat-disk geometry, no z-stretch

    # Drop the 3D box/panes/axis-spines entirely: this is a spatial scatter of an
    # abstract Keplerian disk, the coordinate axes carry no quantity worth a tick,
    # and the leftover spine "wishbone" lines otherwise read as stray clipping
    # artifacts on the white print background (ave-figure-discipline Axis 3).
    ax.set_axis_off()
    ax.grid(False)

    saturn_pos = frame_pos[0]
    ring_pos = frame_pos[1:]
    # Saturn = central node; rings = test masses. Okabe-Ito palette: 'accent'
    # (bluish-green) marks the central node, 'ave' (blue) the ring nodes.
    ax.plot(
        [saturn_pos[0]], [saturn_pos[1]], [saturn_pos[2]],
        "o", color=style.COLORS["accent"], markersize=22, alpha=0.95,
        label="Central node (Saturn)",
    )
    ax.plot(
        ring_pos[:, 0], ring_pos[:, 1], ring_pos[:, 2],
        ".", color=style.COLORS["ave"], markersize=2.5, alpha=0.7,
        label="Ring nodes (ice shards)",
    )
    ax.view_init(elev=elev, azim=azim)


def render_static_frame(history: np.ndarray) -> None:
    """Render a single representative late-time frame to the manuscript PNG/PDF.

    The manuscript (Vol-3 Ch.14) embeds ``saturn_rings_evolution.png`` as "a
    single frame of the N-Body topological evolution". This emits that frame
    through the house style (white bg, framed data, no baked title — the caption
    lives in the LaTeX ``\\caption{}``). Physics is untouched: it samples one
    frame of the same Verlet integration.
    """
    print("[*] Rendering single representative frame (manuscript PNG)...")
    # A late, structured frame (~80% through) shows the clumped/sheared disk the
    # caption describes, not the initial uniform ring.
    frame_idx = int(0.8 * (history.shape[0] - 1))

    fig = plt.figure(figsize=style.figsize("square"))
    ax = fig.add_subplot(111, projection="3d")
    # A moderate elevation reads the disk + its gaps without flattening to a line.
    _draw_frame(ax, history[frame_idx], elev=32.0, azim=45.0)
    style.legend(ax, where="below", ncol=2)

    target = sim_output("saturn_rings_evolution.png")
    written = style.save(fig, target)
    plt.close(fig)
    print(f"[*] Static frame written: {', '.join(str(p) for p in written)}")


def animate_simulation(history: np.ndarray) -> None:
    print("[*] Rendering 3D Temporal Evolution GIF...")

    fig = plt.figure(figsize=style.figsize("square"))
    ax = fig.add_subplot(111, projection="3d")

    def update(frame: int) -> tuple:
        # Slowly orbit the camera over time while keeping the data framed.
        _draw_frame(
            ax, history[frame], elev=32.0 - frame * 0.04, azim=frame * 0.5
        )
        return (ax,)

    anim = animation.FuncAnimation(fig, update, frames=FRAMES, interval=50, blit=False)

    target = sim_output("saturn_rings_evolution.gif")

    anim.save(target, writer="pillow", fps=20)
    plt.close(fig)
    print(f"[*] Scale-Invariant Topology Generated: {target}")


if __name__ == "__main__":
    hist = simulate_rings()
    render_static_frame(hist)
    animate_simulation(hist)
