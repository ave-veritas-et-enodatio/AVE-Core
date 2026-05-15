"""
R10 v14 Visualization v3 — Watchable pace, zoomed-in, side-by-side

Per Grant directive 2026-05-14 late evening (2nd revision):
  "still too fast and zoomed in for a human to make out the animations"

v2 issues fixed:
  - 15 fps too fast → 5 fps (each frame visible 200ms)
  - 360° camera rotation disorienting → static camera angle
  - Full 32-cell lattice view dwarfs the 6-cell soliton → zoom to central
    16×16×16 region around soliton
  - Single-view animation → side-by-side 2D slice + 3D isosurface so the
    viewer can correlate slice dynamics with volume dynamics
  - Annotations too small → bigger labels, V_peak readout overlay
  - 5000 step run sampled every 25 steps → 200 frames is too many to
    watch carefully. Instead: capture 500-1000 timesteps densely (every
    5-10 steps), play slowly. Shows ~5-10 breathing cycles clearly.

Outputs:
  STILL: v14_zoomed_hierarchy.png — annotated single-view zoom-in
  ANIM: v14_breathing_dual_view.gif (5 fps, side-by-side 2D + 3D)
  ANIM: v14_breathing_2d_zoomed.gif (5 fps, just the 2D slice zoomed)
"""
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Rectangle, Circle
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from ave.core.master_equation_fdtd import MasterEquationFDTD
from skimage import measure


print("=" * 78)
print("R10 v14 Visualization v3 — Watchable pace, zoomed-in")
print("=" * 78)
print()


# =============================================================================
# Configuration: focus on showing breathing clearly
# =============================================================================
N = 32
DX = 1.0
V_YIELD = 1.0
C0 = 1.0
PML = 4
A_CAP = 0.99
S_MIN = 0.05

CENTER = (N // 2, N // 2, N // 2)
SEED_PROFILE = "sech"
SEED_AMP = 0.85
SEED_R = 2.5

# Animation parameters tuned for watchability:
# - Snapshot every 6 timesteps (denser than v1/v2)
# - Run for 720 timesteps total
# - 120 frames captured
# - Play at 5 fps → 24 second animation
# - Each frame visible 200ms → viewer can track each "breath" frame
N_STEPS = 720
SNAPSHOT_CADENCE = 6
GIF_FPS = 5

# Zoom window: 14 cells around center (vs 32-cell lattice)
# This makes the 6-cell-radius soliton fill ~85% of the frame
ZOOM_HALF = 7
ZOOM_LO = N // 2 - ZOOM_HALF
ZOOM_HI = N // 2 + ZOOM_HALF

OUT = REPO_ROOT / "assets" / "sim_outputs"
OUT.mkdir(parents=True, exist_ok=True)

print(f"Run: {N_STEPS} steps, snapshot every {SNAPSHOT_CADENCE} → "
      f"{N_STEPS // SNAPSHOT_CADENCE} frames")
print(f"Playback: {GIF_FPS} fps → {(N_STEPS // SNAPSHOT_CADENCE) / GIF_FPS:.0f}s animation")
print(f"Zoom window: cells [{ZOOM_LO}, {ZOOM_HI}] in each axis "
      f"(14 cells centered on soliton)")
print()


# =============================================================================
# Run engine + capture snapshots
# =============================================================================
print(f"Running {N_STEPS} steps with dense snapshot capture...")
engine = MasterEquationFDTD(
    N=N, dx=DX, V_yield=V_YIELD, c0=C0,
    pml_thickness=PML, A_cap=A_CAP, S_min=S_MIN,
)
engine.inject_localized_blob(
    center=CENTER, radius=SEED_R,
    amplitude=SEED_AMP * V_YIELD, profile=SEED_PROFILE,
)

V_initial = engine.V.copy()
V_peak_init = float(np.max(np.abs(V_initial)))

snapshots_V = [engine.V.copy()]
snapshots_t = [0.0]
snapshots_v_peak = [V_peak_init]

t_start = time.time()
for step in range(1, N_STEPS + 1):
    engine.step()
    if step % SNAPSHOT_CADENCE == 0:
        snapshots_V.append(engine.V.copy())
        snapshots_t.append(step * engine.dt)
        snapshots_v_peak.append(float(np.max(np.abs(engine.V))))

print(f"  {len(snapshots_V)} snapshots captured in {time.time()-t_start:.1f}s")
print(f"  V_peak min/max/mean across run: "
      f"{min(snapshots_v_peak):.3f} / {max(snapshots_v_peak):.3f} / "
      f"{np.mean(snapshots_v_peak):.3f}")
print()


# =============================================================================
# Helpers
# =============================================================================
def isosurface(V, level, color, alpha=0.6):
    V_abs = np.abs(V)
    if V_abs.max() < level:
        return None
    try:
        verts, faces, _, _ = measure.marching_cubes(V_abs, level=level)
        return Poly3DCollection(verts[faces], alpha=alpha,
                                  facecolor=color, edgecolor="none")
    except Exception:
        return None


def lattice_wireframe_zoomed(ax, lo, hi, color="#888888", lw=1.2, alpha=0.4):
    """Draw the central zoom region's box as wireframe."""
    edges = [
        ([lo, hi], [lo, lo], [lo, lo]), ([hi, hi], [lo, hi], [lo, lo]),
        ([hi, lo], [hi, hi], [lo, lo]), ([lo, lo], [hi, lo], [lo, lo]),
        ([lo, hi], [lo, lo], [hi, hi]), ([hi, hi], [lo, hi], [hi, hi]),
        ([hi, lo], [hi, hi], [hi, hi]), ([lo, lo], [hi, lo], [hi, hi]),
        ([lo, lo], [lo, lo], [lo, hi]), ([hi, hi], [lo, lo], [lo, hi]),
        ([hi, hi], [hi, hi], [lo, hi]), ([lo, lo], [hi, hi], [lo, hi]),
    ]
    for x, y, z in edges:
        ax.plot(x, y, z, color=color, lw=lw, alpha=alpha)


# Find high/low phase snapshots for the still
v_peak_array = np.array(snapshots_v_peak)
post_transient = len(v_peak_array) // 4
high_idx = post_transient + int(np.argmax(v_peak_array[post_transient:]))
low_idx = post_transient + int(np.argmin(v_peak_array[post_transient:]))
print(f"Phases: high @ snap {high_idx} (V_peak={v_peak_array[high_idx]:.3f}), "
      f"low @ snap {low_idx} (V_peak={v_peak_array[low_idx]:.3f})")


# =============================================================================
# STILL: zoomed-in single-view annotated hero
# =============================================================================
print("Generating STILL: zoomed-in annotated hero...")

fig = plt.figure(figsize=(12, 10), facecolor="#0a0a0a")
ax = fig.add_subplot(111, projection="3d")

V_high = snapshots_V[high_idx]
V_max_high = np.abs(V_high).max()

# Zoom box wireframe
lattice_wireframe_zoomed(ax, ZOOM_LO, ZOOM_HI, color="#888888", lw=1.5, alpha=0.5)

# Soliton envelope (translucent outer)
mesh_env = isosurface(V_high, level=0.12 * V_max_high,
                        color="#ffcc40", alpha=0.22)
if mesh_env is not None:
    ax.add_collection3d(mesh_env)
# Soliton core (opaque inner)
mesh_core = isosurface(V_high, level=0.35 * V_max_high,
                         color="#ff3030", alpha=0.85)
if mesh_core is not None:
    ax.add_collection3d(mesh_core)

ax.scatter([CENTER[0]], [CENTER[1]], [CENTER[2]],
            color="cyan", s=250, marker="*",
            edgecolors="white", linewidth=3, zorder=20)

# Annotations
ax.text(ZOOM_HI - 0.5, ZOOM_LO + 0.5, ZOOM_HI + 1.5,
         "← Zoom window (14×14×14 cells around soliton)\nFull lattice is 32×32×32",
         color="#bbbbbb", fontsize=11, ha="right")
ax.text(CENTER[0] + 6.5, CENTER[1] + 6.5, CENTER[2],
         "Soliton envelope\nΓ→−1 boundary\n(physical, has 𝓜, 𝓠, 𝓙)",
         color="#ffcc40", fontsize=12, ha="left",
         bbox=dict(boxstyle="round,pad=0.3", facecolor="#0a0a0a",
                    edgecolor="#ffcc40", alpha=0.8))
ax.text(CENTER[0] - 4, CENTER[1] - 4, CENTER[2] - 4,
         "Soliton core\n(A→1 saturated)",
         color="#ff5050", fontsize=12, ha="right",
         bbox=dict(boxstyle="round,pad=0.3", facecolor="#0a0a0a",
                    edgecolor="#ff5050", alpha=0.8))

ax.set_xlim(ZOOM_LO, ZOOM_HI)
ax.set_ylim(ZOOM_LO, ZOOM_HI)
ax.set_zlim(ZOOM_LO, ZOOM_HI)
ax.set_xlabel("x (cells)", color="white", fontsize=11)
ax.set_ylabel("y (cells)", color="white", fontsize=11)
ax.set_zlabel("z (cells)", color="white", fontsize=11)
ax.set_title(f"The AVE breathing soliton — high-amplitude phase\n"
             f"t = {snapshots_t[high_idx]:.1f}, V_peak = {V_max_high:.3f}",
             color="white", fontsize=13, pad=18)
ax.set_facecolor("#0a0a0a")
for axn in (ax.xaxis, ax.yaxis, ax.zaxis):
    axn.pane.set_facecolor("#050505")
    axn.pane.set_edgecolor("#222222")
ax.tick_params(colors="white", labelsize=9)
# Pick a good static view angle
ax.view_init(elev=22, azim=35)

still_path = OUT / "v14_zoomed_hero.png"
plt.savefig(still_path, dpi=160, facecolor="#0a0a0a", bbox_inches="tight")
print(f"  {still_path}")
plt.close(fig)


# =============================================================================
# ANIMATION 1: Dual-view side-by-side (2D slice + 3D isosurface)
# =============================================================================
print(f"Generating ANIMATION 1: dual-view 2D + 3D, {len(snapshots_V)} frames at {GIF_FPS} fps...")

fig = plt.figure(figsize=(16, 9), facecolor="#0a0a0a")
gs = GridSpec(1, 2, figure=fig, wspace=0.15)

ax2d = fig.add_subplot(gs[0, 0])
ax3d = fig.add_subplot(gs[0, 1], projection="3d")

# Set up 2D axes (static elements)
vmax_2d = V_peak_init * 0.6
ax2d.set_facecolor("#0f0f0f")
ax2d.set_xlim(ZOOM_LO, ZOOM_HI)
ax2d.set_ylim(ZOOM_LO, ZOOM_HI)
ax2d.set_aspect("equal")
ax2d.set_xlabel("x (cells)", color="white", fontsize=11)
ax2d.set_ylabel("y (cells)", color="white", fontsize=11)
ax2d.tick_params(colors="white", labelsize=9)
for spine in ax2d.spines.values():
    spine.set_color("#444444")

im2d = ax2d.imshow(snapshots_V[0][ZOOM_LO:ZOOM_HI, ZOOM_LO:ZOOM_HI, CENTER[2]].T,
                    origin="lower", cmap="RdBu_r",
                    extent=[ZOOM_LO, ZOOM_HI, ZOOM_LO, ZOOM_HI],
                    aspect="equal", vmin=-vmax_2d, vmax=vmax_2d)
center_marker = ax2d.plot(CENTER[0] + 0.5, CENTER[1] + 0.5, "*",
                            color="cyan", markersize=22,
                            markeredgecolor="white", markeredgewidth=1.5,
                            zorder=10)[0]

title2d = ax2d.set_title("V(x,y), z=center — equatorial slice",
                          color="white", fontsize=13)

# Colorbar
cbar = plt.colorbar(im2d, ax=ax2d, fraction=0.04, pad=0.04)
cbar.ax.tick_params(colors="white")
cbar.set_label("V", color="white")

# 3D axes (will redraw each frame)
contour_storage = {"contour": None}


def update_dual(frame_idx):
    V_state = snapshots_V[frame_idx]
    V_max_state = np.abs(V_state).max()
    t_val = snapshots_t[frame_idx]

    # 2D update
    im2d.set_array(V_state[ZOOM_LO:ZOOM_HI, ZOOM_LO:ZOOM_HI, CENTER[2]].T)

    # Redraw 2D contour
    if contour_storage["contour"] is not None:
        try:
            contour_storage["contour"].remove()
        except (AttributeError, ValueError):
            pass
    if V_max_state > 0.05:
        A_zoom = np.abs(V_state[ZOOM_LO:ZOOM_HI, ZOOM_LO:ZOOM_HI, CENTER[2]]) / V_YIELD
        contour_storage["contour"] = ax2d.contour(
            A_zoom.T,
            levels=[0.12 * V_max_state, 0.35 * V_max_state],
            colors=["#ffcc40", "#ff3030"],
            linewidths=[2, 2.5],
            extent=[ZOOM_LO, ZOOM_HI, ZOOM_LO, ZOOM_HI],
        )

    title2d.set_text(f"V(x,y), z=center, t={t_val:.1f}, V_peak={V_max_state:.3f}")

    # 3D update
    ax3d.clear()
    lattice_wireframe_zoomed(ax3d, ZOOM_LO, ZOOM_HI,
                              color="#888888", lw=1.2, alpha=0.4)

    if V_max_state > 0.05:
        mesh_env = isosurface(V_state, level=0.12 * V_max_state,
                                color="#ffcc40", alpha=0.22)
        if mesh_env is not None:
            ax3d.add_collection3d(mesh_env)
        mesh_core = isosurface(V_state, level=0.35 * V_max_state,
                                 color="#ff3030", alpha=0.8)
        if mesh_core is not None:
            ax3d.add_collection3d(mesh_core)

    ax3d.scatter([CENTER[0]], [CENTER[1]], [CENTER[2]],
                  color="cyan", s=150, marker="*",
                  edgecolors="white", linewidth=2, zorder=20)
    ax3d.set_xlim(ZOOM_LO, ZOOM_HI)
    ax3d.set_ylim(ZOOM_LO, ZOOM_HI)
    ax3d.set_zlim(ZOOM_LO, ZOOM_HI)
    ax3d.view_init(elev=22, azim=35)  # STATIC camera angle
    ax3d.set_title(f"3D isosurface |V|>0.12 (env) and 0.35 (core)",
                    color="white", fontsize=13)
    ax3d.set_facecolor("#0a0a0a")
    for axn in (ax3d.xaxis, ax3d.yaxis, ax3d.zaxis):
        axn.pane.set_facecolor("#050505")
        axn.pane.set_edgecolor("#222222")
    ax3d.tick_params(colors="white", labelsize=8)
    ax3d.set_xlabel("x", color="white", fontsize=10)
    ax3d.set_ylabel("y", color="white", fontsize=10)
    ax3d.set_zlabel("z", color="white", fontsize=10)

    return [im2d, title2d, ax3d]


anim_dual = FuncAnimation(fig, update_dual, frames=len(snapshots_V),
                            interval=1000 // GIF_FPS, blit=False)
anim_dual_path = OUT / "v14_breathing_dual_view.gif"

print(f"  Saving {anim_dual_path} (this takes ~30-60s)...")
fig.suptitle("AVE breathing soliton — 2D equatorial slice + 3D isosurface",
              color="white", fontsize=14, y=0.96)
anim_dual.save(str(anim_dual_path), writer=PillowWriter(fps=GIF_FPS))
print(f"  {anim_dual_path}")
plt.close(fig)


# =============================================================================
# ANIMATION 2: zoomed 2D-only slice (slower, very legible)
# =============================================================================
print(f"Generating ANIMATION 2: zoomed 2D-only at {GIF_FPS} fps...")

fig, ax = plt.subplots(figsize=(11, 10), facecolor="#0a0a0a")
ax.set_facecolor("#0f0f0f")
ax.set_xlim(ZOOM_LO, ZOOM_HI)
ax.set_ylim(ZOOM_LO, ZOOM_HI)
ax.set_aspect("equal")

vmax_2d = V_peak_init * 0.6
im = ax.imshow(snapshots_V[0][ZOOM_LO:ZOOM_HI, ZOOM_LO:ZOOM_HI, CENTER[2]].T,
               origin="lower", cmap="RdBu_r",
               extent=[ZOOM_LO, ZOOM_HI, ZOOM_LO, ZOOM_HI],
               aspect="equal", vmin=-vmax_2d, vmax=vmax_2d)

ax.plot(CENTER[0] + 0.5, CENTER[1] + 0.5, "*",
        color="cyan", markersize=24, markeredgecolor="white",
        markeredgewidth=1.5, zorder=10)
ax.set_xlabel("x (cells)", color="white", fontsize=12)
ax.set_ylabel("y (cells)", color="white", fontsize=12)
ax.tick_params(colors="white", labelsize=10)
for spine in ax.spines.values():
    spine.set_color("#444444")
cbar = plt.colorbar(im, ax=ax, fraction=0.04, pad=0.04)
cbar.ax.tick_params(colors="white")
cbar.set_label("V (substrate potential)", color="white", fontsize=11)

# V_peak readout text (will update each frame)
readout_text = ax.text(0.02, 0.96, "", transform=ax.transAxes,
                        fontsize=12, family="monospace",
                        verticalalignment="top", color="white",
                        bbox=dict(boxstyle="round,pad=0.4",
                                    facecolor="#0a0a0a", edgecolor="#666666",
                                    alpha=0.9))

contour_storage2 = {"contour": None}
title = ax.set_title("V(x,y) at z=center, zoomed to soliton region",
                       color="white", fontsize=14, pad=12)


def update_2d_zoom(frame_idx):
    V_state = snapshots_V[frame_idx]
    V_max_state = np.abs(V_state).max()
    t_val = snapshots_t[frame_idx]

    im.set_array(V_state[ZOOM_LO:ZOOM_HI, ZOOM_LO:ZOOM_HI, CENTER[2]].T)

    if contour_storage2["contour"] is not None:
        try:
            contour_storage2["contour"].remove()
        except (AttributeError, ValueError):
            pass
    if V_max_state > 0.05:
        A_zoom = np.abs(V_state[ZOOM_LO:ZOOM_HI, ZOOM_LO:ZOOM_HI, CENTER[2]]) / V_YIELD
        contour_storage2["contour"] = ax.contour(
            A_zoom.T,
            levels=[0.12 * V_max_state, 0.35 * V_max_state],
            colors=["#ffcc40", "#ff3030"],
            linewidths=[2.5, 3],
            extent=[ZOOM_LO, ZOOM_HI, ZOOM_LO, ZOOM_HI],
        )

    # Determine breathing phase
    if V_max_state > 0.4:
        phase_str = "HIGH PHASE (inhale)"
        phase_color = "#ff5050"
    elif V_max_state < 0.15:
        phase_str = "LOW PHASE (exhale)"
        phase_color = "#5080ff"
    else:
        phase_str = "transition"
        phase_color = "#cccccc"

    readout = (
        f"t      = {t_val:>6.2f}\n"
        f"step   = {frame_idx * SNAPSHOT_CADENCE:>6d}\n"
        f"V_peak = {V_max_state:>6.3f}\n"
        f"phase  = {phase_str}"
    )
    readout_text.set_text(readout)
    readout_text.set_color(phase_color)

    return [im, readout_text, title]


anim_zoom = FuncAnimation(fig, update_2d_zoom, frames=len(snapshots_V),
                            interval=1000 // GIF_FPS, blit=False)
anim_zoom_path = OUT / "v14_breathing_2d_zoomed.gif"
print(f"  Saving {anim_zoom_path}...")
anim_zoom.save(str(anim_zoom_path), writer=PillowWriter(fps=GIF_FPS))
print(f"  {anim_zoom_path}")
plt.close(fig)


# =============================================================================
# Summary
# =============================================================================
print()
print("=" * 78)
print("VISUALIZATION v3 COMPLETE — watchable pace, zoomed-in")
print("=" * 78)
print(f"  Still:")
print(f"    {still_path}")
print(f"  Animations ({GIF_FPS} fps, ~{len(snapshots_V) / GIF_FPS:.0f} seconds each):")
print(f"    {anim_dual_path}    ← side-by-side 2D + 3D")
print(f"    {anim_zoom_path}    ← 2D-only zoomed with phase readout")
print()
print(f"  Animation duration: {len(snapshots_V)} frames at {GIF_FPS} fps = "
      f"{len(snapshots_V) / GIF_FPS:.0f} seconds")
print(f"  Zoom region: 14×14×14 cells (vs full lattice 32×32×32)")
print(f"  Camera angle: STATIC elev=22 azim=35 (no rotation)")
print(f"  V_peak range in shown window: "
      f"{min(snapshots_v_peak):.3f} - {max(snapshots_v_peak):.3f}")
print("=" * 78)
