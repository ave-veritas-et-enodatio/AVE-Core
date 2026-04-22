"""
Topological Solar Flare Simulator
=================================
Demonstrates how a massive stellar node's differential rotation 
twists the surrounding 1/d topological flux lines (impedance lattice).
When the sheer stress exceeds a critical threshold, the lattice 
violently "snaps" back to a lower energy state, ejecting a massive 
directional density wave (Coronal Mass Ejection / Solar Flare).
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pathlib

project_root = pathlib.Path(__file__).parent.parent.absolute()

# Simulation Parameters
N_RADIAL = 30  # Number of shells
N_ANGULAR = 60  # Points per shell
FRAMES = 120
R_SUN = 5.0
R_MAX = 25.0

# Critical stress threshold for a flare
SNAP_FRAME = 75


def initialize_grid():
    r = np.linspace(R_SUN, R_MAX, N_RADIAL)
    theta = np.linspace(0, 2 * np.pi, N_ANGULAR)

    R, THETA = np.meshgrid(r, theta)
    return R, THETA


def differential_omega(r, theta):
    """
    Equator (theta=0, pi) rotates much faster than the poles
    (theta = pi/2, 3pi/2).
    """
    base_omega = 0.05
    # The equator has maximum rotational drag on the topology
    equator_boost = 0.08 * np.abs(np.sin(theta + np.pi / 2)) ** 3

    # Drag drops off with distance
    decay = (R_SUN / r) ** 1.5

    return (base_omega + equator_boost) * decay


def simulate_solar_topology():
    print("[*] Initializing Stellar Topological Matrix...")
    R, THETA = initialize_grid()

    # We will track the evolution of THETA over time
    history_theta = np.zeros((FRAMES, N_ANGULAR, N_RADIAL))

    # The flare ejection wave (radial velocity burst)
    flare_wave = np.zeros((FRAMES, N_ANGULAR, N_RADIAL))

    current_theta = THETA.copy()

    print("[*] Winding the Macroscopic Magnetic Flux (Differential Rotation)...")
    for step in range(FRAMES):
        if step < SNAP_FRAME:
            # Continuously wind the flux lines
            delta_theta = differential_omega(R, current_theta)
            current_theta += delta_theta

        elif step == SNAP_FRAME:
            print("    -> [CRITICAL] Topological sheer limit reached. Snapping lattice (CME)!")
            # The tension snaps! The highly wound lines near the equator
            # violently dump their built up angular momentum.
            # We "straighten" the lines out slightly, converting the potential
            # energy into a massive outward kinetic wave.

            # Find the most heavily wound region (the equator, approx index 0 and 30)
            # We'll just trigger a massive flare at the right equator (theta=0)
            flare_center = 0
            flare_width = 8  # angular indices

            for a in range(N_ANGULAR):
                # How close is this angle to the flare center?
                dist = min(abs(a - flare_center), abs(a - (flare_center + N_ANGULAR)))
                if dist < flare_width:
                    # Release the twist!
                    intensity = 1.0 - (dist / flare_width)
                    # Unwind current_theta towards base THETA radially
                    current_theta[a, :] = current_theta[a, :] * (1.0 - 0.5 * intensity) + THETA[a, :] * (
                        0.5 * intensity
                    )

                    # Inject a massive radial velocity wave moving outwards
                    # It starts at the surface and propagates out
                    flare_wave[step, a, 0] = 5.0 * intensity
        else:
            # Post-snap evolution
            # The flare wave propagates outward radially at high speed
            time_since_snap = step - SNAP_FRAME
            wave_radius_idx = time_since_snap * 2  # Speed of CME

            flare_center = 0
            flare_width = 8

            # Keep generating normal rotation
            current_theta += differential_omega(R, current_theta) * 0.5  # Wind up slower after releasing tension

            # Propagate the wave
            for a in range(N_ANGULAR):
                dist = min(abs(a - flare_center), abs(a - (flare_center + N_ANGULAR)))
                if dist < flare_width and wave_radius_idx < N_RADIAL:
                    intensity = 1.0 - (dist / flare_width)
                    # Add thickness to the wave
                    for w in range(3):
                        if 0 <= wave_radius_idx - w < N_RADIAL:
                            flare_wave[step, a, wave_radius_idx - w] = 5.0 * intensity * (1.0 - w * 0.3)

        history_theta[step] = current_theta.copy()

    return R, history_theta, flare_wave


def animate_flare(R, history_theta, flare_wave):
    print("[*] Rendering Solar Flare Evolution GIF...")

    fig, ax = plt.subplots(figsize=(10, 10))
    fig.patch.set_facecolor("#050010")
    ax.set_facecolor("#050010")

    lim = R_MAX + 5
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_aspect("equal")
    ax.axis("off")

    # Sun Core
    sun = plt.Circle((0, 0), R_SUN, color="#ffcc00", zorder=10)
    ax.add_patch(sun)
    # Sun Glow
    glow = plt.Circle((0, 0), R_SUN * 1.3, color="#ffaa00", alpha=0.3, zorder=9)
    ax.add_patch(glow)

    # We will draw "flux lines" by connecting points at constant theta (the initial spoke)
    # across the radial shells.
    lines = []
    for _ in range(N_ANGULAR):
        (line,) = ax.plot([], [], color="#ff4400", alpha=0.4, linewidth=1.2, zorder=5)
        lines.append(line)

    # Scatter points for the lattice nodes
    nodes = ax.scatter([], [], s=5, color="#ffffff", alpha=0.2, zorder=6)

    # Flare ejecta overlay (a scatter of high-energy particles)
    ejecta = ax.scatter([], [], s=20, color="#ffffff", alpha=0.9, zorder=8, cmap="hot")

    title = ax.set_title(
        "Macroscopic Topological Flare (CME)\nDifferential Rotation vs. 1/d Lattice Tension",
        color="white",
        fontsize=16,
        pad=20,
    )

    def update(frame):
        current_theta = history_theta[frame]

        # Calculate X, Y coordinates
        X = R * np.cos(current_theta)
        Y = R * np.sin(current_theta)

        # Update lines (radial connections)
        for i in range(N_ANGULAR):
            lines[i].set_data(X[i, :], Y[i, :])
            # If the lines are highly twisted, make them brighter (tension)
            if frame < SNAP_FRAME:
                # Color intensity scales as we approach the snap
                intensity = 0.4 + 0.5 * (frame / SNAP_FRAME)
                lines[i].set_color((1.0, 0.3 * (1.0 - intensity), 0.0, intensity))
            else:
                lines[i].set_color("#ff4400")
                lines[i].set_alpha(0.4)

        # Update nodes
        nodes.set_offsets(np.column_stack([X.flatten(), Y.flatten()]))

        # Update ejecta (CME wave)
        wave_mask = flare_wave[frame] > 0
        if np.any(wave_mask):
            eX = X[wave_mask]
            eY = Y[wave_mask]
            eV = flare_wave[frame][wave_mask] * 50  # Size scale

            # Add some chaotic scatter to the plasma
            noise_x = np.random.normal(0, 0.5, size=len(eX))
            noise_y = np.random.normal(0, 0.5, size=len(eY))

            ejecta.set_offsets(np.column_stack([eX + noise_x, eY + noise_y]))
            ejecta.set_sizes(eV)

            # Bright flash at the snap frame
            if frame == SNAP_FRAME:
                ax.set_facecolor("#ffffff")
                title.set_color("black")
            else:
                # Fade back to black
                decay = min(1.0, (frame - SNAP_FRAME) / 10.0)
                color_val = int(255 * (1.0 - decay))
                hex_color = f"#{color_val:02x}{color_val:02x}{color_val:02x}"
                if decay >= 1.0:
                    hex_color = "#050010"
                ax.set_facecolor(hex_color)
                title.set_color("white")
        else:
            ejecta.set_offsets(np.empty((0, 2)))

        return lines + [nodes, ejecta, title]

    anim = animation.FuncAnimation(fig, update, frames=FRAMES, interval=40, blit=False)

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "solar_flare_topology.gif"

    anim.save(target, writer="pillow", fps=25)
    print(f"[*] Topological Solar Flare Animation Saved: {target}")


if __name__ == "__main__":
    R, h_theta, f_wave = simulate_solar_topology()
    animate_flare(R, h_theta, f_wave)
