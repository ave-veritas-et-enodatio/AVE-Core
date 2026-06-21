"""
Topological Solar Flare Simulator
=================================
Demonstrates how a massive stellar node's differential rotation
twists the surrounding 1/d topological flux lines (impedance lattice).
When the sheer stress exceeds a critical threshold, the lattice
violently "snaps" back to a lower energy state, ejecting a massive
directional density wave (Coronal Mass Ejection / Solar Flare).

The simulation physics/data are unchanged from the original driver; this
version restyles the embedded static frame through the shared AVE house figure
style (``ave.viz.style``, print profile) instead of the previous hand-rolled
``dark_background`` aesthetic. White print background, Okabe-Ito colourblind-safe
palette (the previous neon hexes and the ``hot`` colormap are retired), and the
baked figure title is dropped into the LaTeX ``\\caption{}`` of Ch~14
(ave-figure-discipline Axis 4). The radial-coordinate axes carry quantity +
symbol + unit via ``style.axis_label`` (the lattice radial coordinate ``r`` is a
dimensionless model coordinate).

The manuscript (Vol 3 Ch~14, Fig~``solar_flare``) embeds the single static
frame ``solar_flare_topology_frame.png`` — a post-snap snapshot showing both the
wound 1/d flux lattice (the Parker spiral) and the directional CME ejecta (the
white scatter nodes the caption names). This driver renders that one frame; the
underlying ``simulate_solar_topology`` evolution is byte-for-byte the original.

Run::

    PYTHONPATH=src ./.venv/bin/python \\
        src/scripts/vol_3_macroscopic/simulate_solar_flare.py

Writes ``assets/sim_outputs/solar_flare_topology_frame.png``.
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless render-to-file driver

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Resolve the repo's src/ (for `ave` + `ave_path_util`) so the imports below
# work whether the driver is run directly or via PYTHONPATH=src.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ave.viz import style  # noqa: E402
from ave_path_util import sim_output  # noqa: E402

# Simulation Parameters
N_RADIAL = 30  # Number of shells
N_ANGULAR = 60  # Points per shell
FRAMES = 120
R_SUN = 5.0
R_MAX = 25.0

# Critical stress threshold for a flare
SNAP_FRAME = 75

# The single static frame embedded in the manuscript: a post-snap snapshot where
# the directional CME ejecta wave is mid-propagation through the still-wound 1/d
# flux lattice. The post-snap wave reaches radial shell index
# ``2*(frame - SNAP_FRAME)`` and is only drawn while that is ``< N_RADIAL`` (30),
# so the embedded frame is chosen inside that window (idx 20 at frame 85) — both
# the wound spiral and the ejecta scatter are visible together, matching the
# Ch~14 caption.
EMBED_FRAME = 85

# Pin the post-snap ejecta scatter (the only stochastic element) so the embedded
# frame is a reproducible artifact. This pins the cosmetic plasma jitter only; it
# does not change the simulation's physics model.
_RNG_SEED = 0


def initialize_grid() -> tuple[np.ndarray, np.ndarray]:
    r = np.linspace(R_SUN, R_MAX, N_RADIAL)
    theta = np.linspace(0, 2 * np.pi, N_ANGULAR)

    R, THETA = np.meshgrid(r, theta)
    return R, THETA


def differential_omega(r: np.ndarray, theta: np.ndarray) -> np.ndarray:
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


def simulate_solar_topology() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
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


def render_frame(
    R: np.ndarray, history_theta: np.ndarray, flare_wave: np.ndarray, frame: int
) -> "matplotlib.figure.Figure":
    """Render one static topological-flare frame through the AVE house style.

    The previous driver rendered an animated GIF on a hand-rolled dark canvas
    (``#050010`` background, neon ``#ffcc00`` sun, ``#ff4400`` flux lines, a
    ``hot`` ejecta colormap, baked Axes title). This renders the single frame the
    manuscript actually embeds, on the shared print profile: white background,
    Okabe-Ito palette, no baked title (it lives in the LaTeX caption).
    """
    style.apply()  # white print profile FIRST

    np.random.seed(_RNG_SEED)

    current_theta = history_theta[frame]
    X = R * np.cos(current_theta)
    Y = R * np.sin(current_theta)

    lim = R_MAX + 5
    fig, ax = plt.subplots(figsize=style.figsize("square"))
    # Give constrained_layout extra outer padding so the rotated y-label is not
    # cropped flush to the canvas edge by the save-time bbox_inches="tight".
    try:
        fig.get_layout_engine().set(w_pad=0.10, h_pad=0.12)
    except AttributeError:
        pass
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_aspect("equal")

    # Stellar core: paired colour + a clear filled disk (the macroscopic node).
    sun = plt.Circle((0, 0), R_SUN, color=style.COLORS["accent"], zorder=10,
                     label="Stellar node (macroscopic core)")
    ax.add_patch(sun)
    glow = plt.Circle((0, 0), R_SUN * 1.3, color=style.COLORS["accent"],
                      alpha=0.18, zorder=9)
    ax.add_patch(glow)

    # The wound 1/d flux lattice (the Parker spiral): radial "spokes" of constant
    # initial angular index across the radial shells. Vermillion = the "red
    # lines" the Ch~14 caption names (Okabe-Ito comparison hue, print-safe).
    flux_label_done = False
    for i in range(N_ANGULAR):
        lbl = None
        if not flux_label_done:
            lbl = "Wound 1/d flux lattice (Parker spiral)"
            flux_label_done = True
        ax.plot(X[i, :], Y[i, :], color=style.COLORS["comparison"],
                alpha=0.45, linewidth=1.0, zorder=5, label=lbl)

    # Lattice nodes (the topological resonator sites along each flux line). Kept
    # faint so they read as a texture on the flux lines, not as the dominant
    # series — the vermillion spiral and the CME ejecta are the figure's subject.
    ax.scatter(X.flatten(), Y.flatten(), s=2, color=style.COLORS["muted"],
               alpha=0.18, zorder=6, label="Lattice nodes")

    # Directional CME ejecta — the post-snap reconnection wave (the "white
    # scatter nodes" of the caption). Rendered as black data points on the white
    # page (the print-profile analogue of the original white-on-black ejecta),
    # sized by the local burst intensity.
    wave_mask = flare_wave[frame] > 0
    if np.any(wave_mask):
        eX = X[wave_mask]
        eY = Y[wave_mask]
        # Size by local burst intensity (the wave amplitude), but capped so the
        # ejecta reads as a directional cloud of scatter nodes on the print page
        # rather than one saturated black blob (the original *50 scale was tuned
        # for an animated GIF, not a static raster). Physics/data unchanged — this
        # is the marker size only.
        eV = np.clip(flare_wave[frame][wave_mask] * 8.0, 6.0, 36.0)

        # Cosmetic plasma jitter (seeded above for reproducibility).
        noise_x = np.random.normal(0, 0.6, size=len(eX))
        noise_y = np.random.normal(0, 0.6, size=len(eY))

        ax.scatter(eX + noise_x, eY + noise_y, s=eV, color=style.COLORS["data"],
                   alpha=0.85, zorder=8, edgecolor="none",
                   label="CME ejecta (reconnection wave)")

    ax.set_xlabel(style.axis_label("Lattice", "x", ""))
    ax.set_ylabel(style.axis_label("Lattice", "y", ""))

    # Legend OUTSIDE the (square) data box so it never lands on the spiral
    # (ave-figure-discipline Axis 3). Placed to the RIGHT of the square plot; the
    # constrained_layout w_pad above keeps the rotated y-label off the canvas
    # edge. Caption lives in the LaTeX \\caption{}, not the raster.
    style.legend(ax, where="right")

    return fig


def render_static_frame() -> None:
    """Render + save the single manuscript-embedded static frame."""
    R, history_theta, flare_wave = simulate_solar_topology()

    print(f"[*] Rendering static topological-flare frame (frame {EMBED_FRAME})...")
    fig = render_frame(R, history_theta, flare_wave, EMBED_FRAME)

    target = sim_output("solar_flare_topology_frame.png")
    written = style.save(fig, target)
    plt.close(fig)

    # assets/sim_outputs tracks this figure PNG-only; drop the stray companion
    # .pdf so the regen leaves exactly the one tracked raster changed.
    for p in written:
        if p.suffix == ".pdf":
            p.unlink(missing_ok=True)
            print(f"[*] removed stray {p}")
        else:
            print(f"[*] Topological Solar Flare frame saved: {p}")


if __name__ == "__main__":
    render_static_frame()
