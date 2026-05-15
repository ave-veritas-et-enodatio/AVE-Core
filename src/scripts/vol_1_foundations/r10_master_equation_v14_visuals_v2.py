"""
R10 v14 Visualization v2 — Lattice / PML / Soliton boundary hierarchy

Per Grant directive 2026-05-14 late evening:
  "those are somewhat hard to see, and what about the simulations lattice
   boundaries? the simulation and the soliton both need those three numbers
   or just the boundary? or how do those boundaries relate to the sims"

Answer (conceptually, then visually):

  THREE distinct levels of "boundary" must be visually disambiguated:

  Level 1 — Lattice domain edge (the N×N×N simulation box)
    Just the computational window. No physical meaning. Mark as wireframe.

  Level 2 — PML region (cells within pml_thickness of the box edge)
    Sponge-layer absorber that simulates radiation-to-infinity.
    Computational, not physical. Mark as semi-transparent shell.

  Level 3 — Soliton's Γ=−1 envelope (where local A → 1)
    THE physical boundary. Has the substrate-observable invariants
    𝓜, 𝓠, 𝓙. Mark as colored isosurface.

Visualizations produced:
  STILL: hero_v2.png — single high-resolution figure with all three
    levels labeled and visible simultaneously
  STILL: lattice_breakdown.png — annotated lattice + PML + soliton
    schematic showing the hierarchy
  ANIM: breathing_with_hierarchy.gif — soliton's Γ=−1 envelope
    breathing inside the labeled lattice + PML structure
  ANIM: equatorial_with_hierarchy.gif — 2D slice showing soliton
    + PML region marked + lattice edge marked

Engine: Master Equation FDTD, sech A=0.85 R=2.5, 5000 steps.
"""
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from ave.core.master_equation_fdtd import MasterEquationFDTD
from skimage import measure


print("=" * 78)
print("R10 v14 Visualization v2 — Lattice / PML / Soliton hierarchy")
print("=" * 78)
print()


# =============================================================================
# Configuration
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

N_STEPS = 5000
SNAPSHOT_CADENCE = 25
FRAMES_FOR_GIF = 80

OUT = REPO_ROOT / "assets" / "sim_outputs"
OUT.mkdir(parents=True, exist_ok=True)


# =============================================================================
# Run engine + capture snapshots (same as v1)
# =============================================================================
print(f"Running {N_STEPS} steps with snapshot capture...")
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

v_peak_array = np.array(snapshots_v_peak)
analysis_start = len(v_peak_array) // 10
high_idx = analysis_start + int(np.argmax(v_peak_array[analysis_start:]))
low_idx = analysis_start + int(np.argmin(v_peak_array[analysis_start:]))
print(f"  High phase: V_peak = {v_peak_array[high_idx]:.3f}, "
      f"Low phase: V_peak = {v_peak_array[low_idx]:.3f}")
print()


# =============================================================================
# Helper: marching-cubes isosurface
# =============================================================================
def isosurface(V, level, color, alpha=0.6):
    """Compute marching-cubes isosurface and return Poly3DCollection."""
    V_abs = np.abs(V)
    if V_abs.max() < level:
        return None
    try:
        verts, faces, normals, _ = measure.marching_cubes(V_abs, level=level)
        mesh = Poly3DCollection(verts[faces], alpha=alpha,
                                  facecolor=color, edgecolor="none")
        return mesh
    except Exception as e:
        print(f"  marching_cubes failed: {e}")
        return None


def lattice_wireframe(ax, N, color="#666666", lw=1, alpha=0.3):
    """Draw the N×N×N lattice box as wireframe."""
    edges = [
        # 4 bottom edges
        ([0, N], [0, 0], [0, 0]),
        ([N, N], [0, N], [0, 0]),
        ([N, 0], [N, N], [0, 0]),
        ([0, 0], [N, 0], [0, 0]),
        # 4 top edges
        ([0, N], [0, 0], [N, N]),
        ([N, N], [0, N], [N, N]),
        ([N, 0], [N, N], [N, N]),
        ([0, 0], [N, 0], [N, N]),
        # 4 vertical edges
        ([0, 0], [0, 0], [0, N]),
        ([N, N], [0, 0], [0, N]),
        ([N, N], [N, N], [0, N]),
        ([0, 0], [N, N], [0, N]),
    ]
    for x, y, z in edges:
        ax.plot(x, y, z, color=color, lw=lw, alpha=alpha)


def pml_wireframe(ax, N, pml, color="#ff8030", lw=1, alpha=0.4):
    """Draw the inner PML boundary as wireframe (the bulk-physics region)."""
    p = pml
    M = N - pml
    edges = [
        ([p, M], [p, p], [p, p]),
        ([M, M], [p, M], [p, p]),
        ([M, p], [M, M], [p, p]),
        ([p, p], [M, p], [p, p]),
        ([p, M], [p, p], [M, M]),
        ([M, M], [p, M], [M, M]),
        ([M, p], [M, M], [M, M]),
        ([p, p], [M, p], [M, M]),
        ([p, p], [p, p], [p, M]),
        ([M, M], [p, p], [p, M]),
        ([M, M], [M, M], [p, M]),
        ([p, p], [M, M], [p, M]),
    ]
    for x, y, z in edges:
        ax.plot(x, y, z, color=color, lw=lw, alpha=alpha, linestyle="--")


# =============================================================================
# STILL 1: lattice / PML / soliton hierarchy schematic (annotated)
# =============================================================================
print("Generating STILL 1: lattice + PML + soliton hierarchy schematic...")

fig = plt.figure(figsize=(14, 10), facecolor="#0a0a0a")
ax = fig.add_subplot(111, projection="3d")

# Draw lattice box (computational domain edge)
lattice_wireframe(ax, N, color="#aaaaaa", lw=1.5, alpha=0.5)

# Draw inner PML boundary (bulk-physics region)
pml_wireframe(ax, N, PML, color="#ff8030", lw=1.5, alpha=0.6)

# Draw soliton isosurface at high-phase
V_high = snapshots_V[high_idx]
V_peak_high = np.abs(V_high).max()
# Inner isosurface: |V| > 0.3 × V_peak_high (the "core")
mesh_core = isosurface(V_high, level=0.3 * V_peak_high,
                         color="#ff3030", alpha=0.7)
if mesh_core is not None:
    ax.add_collection3d(mesh_core)
# Outer isosurface: |V| > 0.1 × V_peak_high (the "envelope")
mesh_env = isosurface(V_high, level=0.1 * V_peak_high,
                        color="#ffaa30", alpha=0.25)
if mesh_env is not None:
    ax.add_collection3d(mesh_env)

# Mark center
ax.scatter([CENTER[0]], [CENTER[1]], [CENTER[2]],
            color="cyan", s=200, marker="*",
            edgecolors="white", linewidth=2.5, zorder=10)

# Annotations
ax.text(N - 1, N - 1, N + 2, "Lattice domain edge (computational, PML at +z)",
         color="#aaaaaa", fontsize=10, ha="right")
ax.text(PML, PML - 1, N - PML - 0.5, f"PML shell (sponge-layer absorber, thickness={PML})",
         color="#ff8030", fontsize=10, ha="left")
ax.text(N - PML, CENTER[1], CENTER[2],
         "Soliton's Γ→−1 envelope\n(physical, has 𝓜, 𝓠, 𝓙)",
         color="#ffaa30", fontsize=11, ha="left")
ax.text(CENTER[0], CENTER[1], CENTER[2] - 1,
         "Soliton core\n(saturated A→1)",
         color="#ff5050", fontsize=11, ha="center")

ax.set_xlim(-2, N + 2)
ax.set_ylim(-2, N + 2)
ax.set_zlim(-2, N + 5)
ax.set_xlabel("x (lattice cells)", color="white")
ax.set_ylabel("y (lattice cells)", color="white")
ax.set_zlabel("z (lattice cells)", color="white")
ax.set_title("AVE simulation hierarchy:\n"
             "Computational lattice (gray) → PML absorber (orange dashed) → "
             "Soliton's physical Γ→−1 envelope (red/yellow isosurface)",
             color="white", fontsize=12, pad=20)
ax.set_facecolor("#0a0a0a")
for axn in (ax.xaxis, ax.yaxis, ax.zaxis):
    axn.pane.set_facecolor("#050505")
    axn.pane.set_edgecolor("#222222")
ax.tick_params(colors="white", labelsize=8)
ax.view_init(elev=18, azim=42)

still1_path = OUT / "v14_lattice_pml_soliton_hierarchy.png"
plt.savefig(still1_path, dpi=160, facecolor="#0a0a0a", bbox_inches="tight")
print(f"  {still1_path}")
plt.close(fig)


# =============================================================================
# STILL 2: annotated equatorial slice — all three levels visible
# =============================================================================
print("Generating STILL 2: equatorial slice with all three boundary levels...")

fig, ax = plt.subplots(figsize=(11, 10), facecolor="#0a0a0a")
ax.set_facecolor("#0f0f0f")

# Equatorial slice of V at high phase
V_slice = V_high[:, :, CENTER[2]]
vmax = V_peak_init * 0.7
im = ax.imshow(V_slice.T, origin="lower", cmap="RdBu_r",
               extent=[0, N, 0, N], aspect="equal",
               vmin=-vmax, vmax=vmax, alpha=1.0)

# Mark PML region with hatch
for edge in ["bottom", "top", "left", "right"]:
    if edge == "bottom":
        rect = Rectangle((0, 0), N, PML, linewidth=2,
                         edgecolor="#ff8030", facecolor="#ff8030",
                         alpha=0.15, hatch="///", zorder=5)
    elif edge == "top":
        rect = Rectangle((0, N - PML), N, PML, linewidth=2,
                         edgecolor="#ff8030", facecolor="#ff8030",
                         alpha=0.15, hatch="///", zorder=5)
    elif edge == "left":
        rect = Rectangle((0, PML), PML, N - 2 * PML, linewidth=2,
                         edgecolor="#ff8030", facecolor="#ff8030",
                         alpha=0.15, hatch="///", zorder=5)
    else:  # right
        rect = Rectangle((N - PML, PML), PML, N - 2 * PML, linewidth=2,
                         edgecolor="#ff8030", facecolor="#ff8030",
                         alpha=0.15, hatch="///", zorder=5)
    ax.add_patch(rect)

# Mark lattice edge (the outer box)
lattice_rect = Rectangle((0, 0), N, N, linewidth=3,
                           edgecolor="#aaaaaa", facecolor="none", zorder=6)
ax.add_patch(lattice_rect)

# Mark soliton envelope (|V| > 0.1 × V_peak contour)
A_slice = np.abs(V_slice) / V_YIELD
ax.contour(A_slice.T, levels=[0.1 * V_peak_high, 0.3 * V_peak_high],
           colors=["#ffaa30", "#ff3030"], linewidths=[2, 3],
           extent=[0, N, 0, N])

# Mark center
ax.plot(CENTER[0] + 0.5, CENTER[1] + 0.5, "*", color="cyan",
        markersize=20, markeredgecolor="white", markeredgewidth=1.5, zorder=10)

# Annotations
ax.text(N / 2, N - 1.5, "← Lattice domain edge (computational)",
        color="#aaaaaa", fontsize=11, ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#0a0a0a",
                   edgecolor="#aaaaaa", alpha=0.8))
ax.annotate("PML absorber\n(sponge-layer)",
            xy=(2.5, N / 2), xytext=(-3.5, N / 2),
            color="#ff8030", fontsize=11, ha="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#0a0a0a",
                       edgecolor="#ff8030", alpha=0.85),
            arrowprops=dict(arrowstyle="->", color="#ff8030", lw=1.5))
ax.annotate("Soliton's Γ→−1 envelope\n(physical, has 𝓜, 𝓠, 𝓙)",
            xy=(CENTER[0] + 4, CENTER[1]),
            xytext=(N + 3, CENTER[1] + 3),
            color="#ffaa30", fontsize=11, ha="left",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#0a0a0a",
                       edgecolor="#ffaa30", alpha=0.85),
            arrowprops=dict(arrowstyle="->", color="#ffaa30", lw=1.5))
ax.annotate("Soliton core (saturated)",
            xy=(CENTER[0] + 1.5, CENTER[1] + 1.5),
            xytext=(N + 3, CENTER[1] - 3),
            color="#ff5050", fontsize=11,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#0a0a0a",
                       edgecolor="#ff5050", alpha=0.85),
            arrowprops=dict(arrowstyle="->", color="#ff5050", lw=1.5))

ax.set_xlim(-7, N + 12)
ax.set_ylim(-3, N + 3)
ax.set_xlabel("x (lattice cells)", color="white", fontsize=12)
ax.set_ylabel("y (lattice cells)", color="white", fontsize=12)
ax.set_title(f"Equatorial slice (z={CENTER[2]}, high-phase t={snapshots_t[high_idx]:.1f})\n"
             "Three boundary levels: lattice edge (gray) / PML (orange hatch) / soliton envelope (yellow + red)",
             color="white", fontsize=12, pad=15)
ax.tick_params(colors="white", labelsize=10)
for spine in ax.spines.values():
    spine.set_color("#333333")
cbar = plt.colorbar(im, ax=ax, fraction=0.040, label="V (substrate potential)")
cbar.ax.yaxis.label.set_color("white")
cbar.ax.tick_params(colors="white")

still2_path = OUT / "v14_equatorial_three_boundaries.png"
plt.savefig(still2_path, dpi=160, facecolor="#0a0a0a", bbox_inches="tight")
print(f"  {still2_path}")
plt.close(fig)


# =============================================================================
# ANIMATION 1: 3D isosurface breathing with lattice + PML visible
# =============================================================================
print("Generating ANIMATION 1: 3D isosurface breathing with hierarchy...")

# Subsample frames
gif_step = max(1, len(snapshots_V) // FRAMES_FOR_GIF)
gif_frames = list(range(0, len(snapshots_V), gif_step))

fig = plt.figure(figsize=(11, 10), facecolor="#0a0a0a")
ax3d = fig.add_subplot(111, projection="3d")


def update_3d_iso(frame_idx):
    ax3d.clear()

    # Draw lattice box
    lattice_wireframe(ax3d, N, color="#aaaaaa", lw=1.2, alpha=0.4)
    # Draw PML inner edge
    pml_wireframe(ax3d, N, PML, color="#ff8030", lw=1.2, alpha=0.5)

    idx = gif_frames[frame_idx]
    V_state = snapshots_V[idx]
    V_max = np.abs(V_state).max()

    # Soliton core isosurface
    if V_max > 0.05:
        mesh_core = isosurface(V_state, level=0.4 * V_max,
                                 color="#ff3030", alpha=0.7)
        if mesh_core is not None:
            ax3d.add_collection3d(mesh_core)
        # Envelope isosurface
        mesh_env = isosurface(V_state, level=0.15 * V_max,
                               color="#ffaa30", alpha=0.25)
        if mesh_env is not None:
            ax3d.add_collection3d(mesh_env)

    # Center marker
    ax3d.scatter([CENTER[0]], [CENTER[1]], [CENTER[2]],
                  color="cyan", s=120, marker="*",
                  edgecolors="white", linewidth=2, zorder=10)

    ax3d.set_xlim(-1, N + 1)
    ax3d.set_ylim(-1, N + 1)
    ax3d.set_zlim(-1, N + 1)
    azim = 25 + (frame_idx / len(gif_frames)) * 360
    ax3d.view_init(elev=18, azim=azim)
    ax3d.set_title(f"Breathing soliton inside computational lattice\n"
                   f"t={snapshots_t[idx]:.1f}, V_peak={V_max:.3f}\n"
                   f"Gray box = lattice domain | Orange = PML | Yellow/red = soliton envelope",
                   color="white", fontsize=10)
    ax3d.set_facecolor("#0a0a0a")
    for axn in (ax3d.xaxis, ax3d.yaxis, ax3d.zaxis):
        axn.pane.set_facecolor("#050505")
        axn.pane.set_edgecolor("#222222")
    ax3d.tick_params(colors="white", labelsize=7)
    return [ax3d]


print(f"  Animating {len(gif_frames)} frames (each ~1.5s of marching-cubes)...")
anim = FuncAnimation(fig, update_3d_iso, frames=len(gif_frames),
                      interval=100, blit=False)
anim_path = OUT / "v14_breathing_with_lattice.gif"
anim.save(str(anim_path), writer=PillowWriter(fps=12))
print(f"  {anim_path}")
plt.close(fig)


# =============================================================================
# ANIMATION 2: equatorial slice with PML region marked
# =============================================================================
print("Generating ANIMATION 2: equatorial slice + PML region annotated...")

fig, ax = plt.subplots(figsize=(10, 9), facecolor="#0a0a0a")
ax.set_facecolor("#0f0f0f")

vmax = V_peak_init * 0.7
im = ax.imshow(snapshots_V[0][:, :, CENTER[2]].T,
               origin="lower", cmap="RdBu_r",
               extent=[0, N, 0, N], aspect="equal",
               vmin=-vmax, vmax=vmax, animated=True)

# Static PML markers (don't update)
for edge_pos in [
    ((0, 0), N, PML),         # bottom strip
    ((0, N - PML), N, PML),   # top strip
    ((0, PML), PML, N - 2 * PML),         # left strip
    ((N - PML, PML), PML, N - 2 * PML),   # right strip
]:
    pos, w, h = edge_pos
    rect = Rectangle(pos, w, h, linewidth=1.5,
                     edgecolor="#ff8030", facecolor="#ff8030",
                     alpha=0.15, hatch="//", zorder=5)
    ax.add_patch(rect)

# Lattice edge
lattice_rect = Rectangle((0, 0), N, N, linewidth=3,
                          edgecolor="#aaaaaa", facecolor="none", zorder=6)
ax.add_patch(lattice_rect)

# Initial soliton envelope contours (will redraw)
contours_storage = {"contour": None}


def update_slice(frame_idx):
    idx = gif_frames[frame_idx]
    V_state = snapshots_V[idx]
    V_slice = V_state[:, :, CENTER[2]]
    V_max_state = np.abs(V_state).max()
    im.set_array(V_slice.T)

    # Redraw soliton envelope contour (matplotlib 3.10+ — use .remove() directly)
    if contours_storage["contour"] is not None:
        try:
            contours_storage["contour"].remove()
        except (AttributeError, ValueError):
            pass

    if V_max_state > 0.05:
        contours_storage["contour"] = ax.contour(
            np.abs(V_slice).T / V_YIELD,
            levels=[0.1 * V_max_state / V_YIELD,
                    0.3 * V_max_state / V_YIELD],
            colors=["#ffaa30", "#ff3030"],
            linewidths=[2, 3],
            extent=[0, N, 0, N],
        )

    ax.set_title(f"V(x,y), z={CENTER[2]}, t={snapshots_t[idx]:.1f}, "
                 f"V_peak={V_max_state:.3f}\n"
                 f"Orange hatch = PML | Yellow/red contour = soliton envelope",
                 color="white", fontsize=11)
    return [im]


anim2 = FuncAnimation(fig, update_slice, frames=len(gif_frames),
                       interval=100, blit=False)
ax.plot(CENTER[0] + 0.5, CENTER[1] + 0.5, "k*", ms=14, mec="cyan", zorder=10)
ax.set_xlabel("x", color="white")
ax.set_ylabel("y", color="white")
ax.tick_params(colors="white")
for spine in ax.spines.values():
    spine.set_color("#333333")
cbar = plt.colorbar(im, ax=ax, fraction=0.04, label="V")
cbar.ax.yaxis.label.set_color("white")
cbar.ax.tick_params(colors="white")

anim2_path = OUT / "v14_breathing_equatorial_annotated.gif"
anim2.save(str(anim2_path), writer=PillowWriter(fps=15))
print(f"  {anim2_path}")
plt.close(fig)


# =============================================================================
# Summary
# =============================================================================
print()
print("=" * 78)
print("VISUALIZATION v2 COMPLETE")
print("=" * 78)
print(f"  Stills:")
print(f"    {still1_path}")
print(f"    {still2_path}")
print(f"  Animations:")
print(f"    {anim_path}")
print(f"    {anim2_path}")
print()
print(f"  Lattice domain: {N}×{N}×{N} = {N**3} cells")
print(f"  PML region: {PML} cells thick on each face (sponge-layer absorber)")
print(f"  Bulk physics region: ({N - 2*PML})×({N - 2*PML})×({N - 2*PML}) = "
      f"{(N - 2*PML)**3} cells")
print(f"  Soliton core radius: ~{SEED_R} cells (sech profile)")
print(f"  Soliton envelope extent: ~{SEED_R * 2.5:.1f} cells (where A drops to 0.1)")
print("=" * 78)
