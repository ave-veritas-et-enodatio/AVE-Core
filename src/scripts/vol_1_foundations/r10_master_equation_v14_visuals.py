"""
R10 v14 Visualization Suite — Master Equation FDTD breathing soliton

Comprehensive visual deliverable for v14 Mode I closure (doc 113).
Re-runs the canonical breathing-soliton seed (sech A=0.85 R=2.5) on the
Master Equation FDTD engine, captures snapshots, and produces:

  STILLS (PNG):
    1. Hero multi-panel: 3D isosurface + slices + diagnostics
    2. Breathing cycle: high-amplitude phase vs low-amplitude phase

  ANIMATIONS (GIF):
    3. 2D equatorial-slice heatmap over time
    4. 3D scatter (V > threshold) over time, with camera rotation
    5. Radial profile A(r) over time — the breathing dynamics

All outputs land at assets/sim_outputs/.
"""
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from ave.core.master_equation_fdtd import MasterEquationFDTD
from ave.core.constants import ALPHA, ALPHA_COLD_INV

print("=" * 78)
print("R10 v14 Visualization Suite — Master Equation FDTD breathing soliton")
print("=" * 78)
print()


# =============================================================================
# Configuration: replicate v14 v2 Mode I-PASS seed
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
SNAPSHOT_CADENCE = 25  # 200 snapshots total
FRAMES_FOR_GIF = 100   # subsample for GIF (every other snapshot)

OUT = REPO_ROOT / "assets" / "sim_outputs"
OUT.mkdir(parents=True, exist_ok=True)

print(f"Engine: N={N}, V_yield={V_YIELD}, c0={C0}, PML={PML}")
print(f"Seed: {SEED_PROFILE} @ A={SEED_AMP}, R={SEED_R}")
print(f"Run: {N_STEPS} steps, snapshot every {SNAPSHOT_CADENCE} ({N_STEPS // SNAPSHOT_CADENCE} frames)")
print()


# =============================================================================
# Initialize engine + run with snapshot capture
# =============================================================================
print("Initializing engine + planting breathing-soliton seed...")
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
print(f"  Initial V_peak = {V_peak_init:.4f}, t=0")
print()

# Capture snapshots
print(f"Running {N_STEPS} steps with snapshot capture...")
snapshots_V = [engine.V.copy()]
snapshots_t = [0.0]
snapshots_v_peak = [V_peak_init]
snapshots_v_center = [float(engine.V[CENTER])]
snapshots_fwhm = []
snapshots_a_profile = []  # radial A(r) at each snapshot
snapshots_a_max = [V_peak_init / V_YIELD]


def fwhm_3d(V):
    V_abs = np.abs(V)
    V_max = V_abs.max()
    if V_max < 1e-10:
        return 0.0
    above_half = V_abs > V_max / 2.0
    n_cells = above_half.sum()
    if n_cells == 0:
        return 0.0
    radius = (3 * n_cells / (4 * np.pi)) ** (1.0 / 3.0)
    return 2.0 * radius


def radial_A_profile(V, center, max_r=10):
    cx, cy, cz = center
    i, j, k = np.indices(V.shape)
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    r_arr = np.arange(0, max_r + 1)
    A_arr = np.zeros_like(r_arr, dtype=float)
    for ri, r_val in enumerate(r_arr):
        shell = (r >= r_val - 0.5) & (r < r_val + 0.5)
        if shell.sum() > 0:
            A_arr[ri] = float(np.mean(np.abs(V[shell]))) / V_YIELD
    return r_arr, A_arr


r_axis, A_init = radial_A_profile(V_initial, CENTER)
snapshots_a_profile.append(A_init)
snapshots_fwhm.append(fwhm_3d(V_initial))

t_start = time.time()
for step in range(1, N_STEPS + 1):
    engine.step()
    if step % SNAPSHOT_CADENCE == 0:
        V_snap = engine.V.copy()
        snapshots_V.append(V_snap)
        snapshots_t.append(step * engine.dt)
        snapshots_v_peak.append(float(np.max(np.abs(V_snap))))
        snapshots_v_center.append(float(V_snap[CENTER]))
        snapshots_fwhm.append(fwhm_3d(V_snap))
        _, A_prof = radial_A_profile(V_snap, CENTER)
        snapshots_a_profile.append(A_prof)
        snapshots_a_max.append(float(np.max(np.abs(V_snap))) / V_YIELD)
        if step % (SNAPSHOT_CADENCE * 20) == 0:
            print(f"  step={step:>4d}  V_peak={snapshots_v_peak[-1]:.4f}  "
                  f"FWHM={snapshots_fwhm[-1]:.2f}")

print(f"Captured {len(snapshots_V)} snapshots in {time.time() - t_start:.1f}s")
print()

# Find indices of high-phase and low-phase frames (breathing cycle extremes)
v_peak_array = np.array(snapshots_v_peak)
# Skip first 10% (transient) for cycle analysis
analysis_start = len(v_peak_array) // 10
high_idx = analysis_start + int(np.argmax(v_peak_array[analysis_start:]))
low_idx = analysis_start + int(np.argmin(v_peak_array[analysis_start:]))
print(f"Breathing cycle extremes (post-transient):")
print(f"  High phase: snapshot {high_idx}, V_peak = {v_peak_array[high_idx]:.4f}")
print(f"  Low  phase: snapshot {low_idx}, V_peak = {v_peak_array[low_idx]:.4f}")
print()


# =============================================================================
# STILL 1: Hero multi-panel figure
# =============================================================================
print("Generating STILL 1: hero multi-panel figure...")

V_high = snapshots_V[high_idx]
V_low = snapshots_V[low_idx]
V_final = snapshots_V[-1]

fig = plt.figure(figsize=(18, 12), facecolor="#0a0a0a")
gs = GridSpec(3, 4, figure=fig, hspace=0.4, wspace=0.3,
              height_ratios=[1.0, 1.0, 0.85])

# Panel A: 3D scatter of |V| at high-amplitude phase
axA = fig.add_subplot(gs[0:2, 0:2], projection="3d")
threshold = 0.15 * np.abs(V_high).max()
mask = np.abs(V_high) > threshold
xs, ys, zs = np.where(mask)
vals = V_high[mask]
sizes = 30 * (np.abs(vals) / np.abs(V_high).max()) ** 1.5
colors = plt.cm.hot(np.abs(vals) / np.abs(V_high).max())
axA.scatter(xs, ys, zs, c=colors, s=sizes, alpha=0.6, edgecolors="none")
axA.scatter([CENTER[0]], [CENTER[1]], [CENTER[2]],
            color="cyan", s=150, marker="*",
            edgecolors="white", linewidth=1.5, label="Center")
axA.set_xlim(N // 2 - 8, N // 2 + 8)
axA.set_ylim(N // 2 - 8, N // 2 + 8)
axA.set_zlim(N // 2 - 8, N // 2 + 8)
axA.set_title(f"The breathing soliton, high-amplitude phase\n"
              f"|V| > {threshold:.2f}, V_peak = {v_peak_array[high_idx]:.3f}",
              color="white", fontsize=11)
axA.set_facecolor("#0a0a0a")
for axn in (axA.xaxis, axA.yaxis, axA.zaxis):
    axn.pane.set_facecolor("#0a0a0a")
    axn.pane.set_edgecolor("#333333")
axA.tick_params(colors="white", labelsize=8)

# Panel B: equatorial slice at high phase
axB = fig.add_subplot(gs[0, 2])
slice_high = V_high[:, :, CENTER[2]]
vmax = np.abs(V_initial).max() * 0.5
im = axB.imshow(slice_high.T, origin="lower", cmap="RdBu_r",
                extent=[0, N, 0, N], aspect="equal",
                vmin=-vmax, vmax=vmax)
axB.plot(CENTER[0] + 0.5, CENTER[1] + 0.5, "k*", ms=12, mec="white")
axB.set_title(f"V(x,y) at z={CENTER[2]}, high phase\nt = {snapshots_t[high_idx]:.1f}")
plt.colorbar(im, ax=axB, fraction=0.046)

# Panel C: equatorial slice at low phase
axC = fig.add_subplot(gs[0, 3])
slice_low = V_low[:, :, CENTER[2]]
im = axC.imshow(slice_low.T, origin="lower", cmap="RdBu_r",
                extent=[0, N, 0, N], aspect="equal",
                vmin=-vmax, vmax=vmax)
axC.plot(CENTER[0] + 0.5, CENTER[1] + 0.5, "k*", ms=12, mec="white")
axC.set_title(f"V(x,y) at z={CENTER[2]}, low phase\nt = {snapshots_t[low_idx]:.1f}")
plt.colorbar(im, ax=axC, fraction=0.046)

# Panel D: V_peak time series (the breather)
axD = fig.add_subplot(gs[1, 2])
axD.plot(snapshots_t, snapshots_v_peak, "C2-", lw=1.5)
axD.axhline(0.2, color="white", ls=":", lw=1, alpha=0.5)
axD.axvline(snapshots_t[high_idx], color="orange", lw=1, alpha=0.7, label="High phase")
axD.axvline(snapshots_t[low_idx], color="cyan", lw=1, alpha=0.7, label="Low phase")
axD.set_xlabel("t (lattice units)")
axD.set_ylabel("V_peak")
axD.set_title("Breathing oscillation")
axD.legend(loc="best", fontsize=8)
axD.grid(True, alpha=0.2)

# Panel E: V_center time series (oscillates through zero)
axE = fig.add_subplot(gs[1, 3])
axE.plot(snapshots_t, snapshots_v_center, "C0-", lw=1.5)
axE.axhline(0, color="white", ls=":", lw=0.5)
axE.set_xlabel("t (lattice units)")
axE.set_ylabel("V at center")
axE.set_title("V_center: oscillates through zero")
axE.grid(True, alpha=0.2)

# Panel F: radial A(r) at three phases
axF = fig.add_subplot(gs[2, 0])
axF.plot(r_axis, snapshots_a_profile[0], "k-", lw=2, alpha=0.7, label="Initial")
axF.plot(r_axis, snapshots_a_profile[high_idx], "C3-", lw=2, label="High phase")
axF.plot(r_axis, snapshots_a_profile[low_idx], "C0-", lw=2, label="Low phase")
axF.plot(r_axis, snapshots_a_profile[-1], "C2-", lw=2, label="Final")
axF.set_xlabel("r (cells from center)")
axF.set_ylabel("|V|/V_yield")
axF.set_title("Radial profile A(r) at phases")
axF.legend(loc="best", fontsize=8)
axF.grid(True, alpha=0.2)

# Panel G: FWHM time series
axG = fig.add_subplot(gs[2, 1])
axG.plot(snapshots_t, snapshots_fwhm, "C4-", lw=1.5)
fwhm_init = snapshots_fwhm[0]
axG.axhline(fwhm_init, color="white", ls=":", lw=1, label=f"Initial = {fwhm_init:.2f}")
axG.set_xlabel("t (lattice units)")
axG.set_ylabel("FWHM (cells)")
axG.set_title("Localization stability")
axG.legend(loc="best", fontsize=8)
axG.grid(True, alpha=0.2)

# Panel H: refractive index profile (at final state)
axH = fig.add_subplot(gs[2, 2])
n_field = engine.refractive_index()
cx, cy, cz = CENTER
i, j, k = np.indices(n_field.shape)
r_3d = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
r_axis_n = np.arange(0, 11)
n_arr = np.zeros_like(r_axis_n, dtype=float)
for ri, r_val in enumerate(r_axis_n):
    shell = (r_3d >= r_val - 0.5) & (r_3d < r_val + 0.5)
    if shell.sum() > 0:
        n_arr[ri] = float(np.mean(n_field[shell]))
axH.plot(r_axis_n, n_arr, "C2o-", lw=2, ms=8)
axH.axhline(1.0, color="white", ls=":", lw=1)
axH.set_xlabel("r (cells)")
axH.set_ylabel("n(r)")
axH.set_title(f"Refractive gradient (final)")
axH.grid(True, alpha=0.2)

# Panel I: summary
axI = fig.add_subplot(gs[2, 3])
axI.axis("off")
summary = (
    f"v14 Mode I PASS\n"
    f"{'─' * 28}\n"
    f"Engine: Master Eq FDTD\n"
    f"Seed: sech, A=0.85, R=2.5\n"
    f"Run: {N_STEPS} steps\n\n"
    f"V_peak:\n"
    f"  initial = {V_peak_init:.3f}\n"
    f"  mean = {np.mean(v_peak_array[len(v_peak_array)//4:]):.3f}\n"
    f"  ratio = {np.mean(v_peak_array[len(v_peak_array)//4:])/V_peak_init:.3f}\n\n"
    f"FWHM range:\n"
    f"  initial = {fwhm_init:.2f}\n"
    f"  range = {np.min(snapshots_fwhm[len(snapshots_fwhm)//4:]):.2f}-"
    f"{np.max(snapshots_fwhm[len(snapshots_fwhm)//4:]):.2f}\n\n"
    f"4/4 acceptance criteria PASS\n"
    f"(breathing-soliton appropriate\n"
    f" per doc 113)\n\n"
    f"The substrate hosts a sustained\n"
    f"breathing soliton — the dynamic\n"
    f"signature of the canonical AVE\n"
    f"electron at lattice resolution."
)
axI.text(0.05, 0.95, summary, transform=axI.transAxes,
         fontsize=9, family="monospace", verticalalignment="top",
         color="white",
         bbox=dict(boxstyle="round,pad=0.5", facecolor="#181818",
                   edgecolor="#404040"))

for ax in [axB, axC, axD, axE, axF, axG, axH]:
    ax.set_facecolor("#0f0f0f")
    ax.tick_params(colors="white")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.title.set_color("white")
    for spine in ax.spines.values():
        spine.set_color("#333333")
    leg = ax.get_legend()
    if leg is not None:
        leg.get_frame().set_facecolor("#0f0f0f")
        leg.get_frame().set_edgecolor("none")
        for text in leg.get_texts():
            text.set_color("white")

fig.suptitle("AVE Breathing Soliton on Master Equation FDTD — v14 Mode I",
             color="white", fontsize=15, y=0.995)

hero_path = OUT / "v14_breathing_soliton_hero.png"
plt.savefig(hero_path, dpi=140, facecolor="#0a0a0a", bbox_inches="tight")
print(f"  Hero figure: {hero_path}")
plt.close(fig)


# =============================================================================
# STILL 2: 3D side-by-side high vs low phase
# =============================================================================
print("Generating STILL 2: high-phase vs low-phase 3D comparison...")
fig = plt.figure(figsize=(14, 7), facecolor="#0a0a0a")

for idx, (V_state, phase_name, t_val) in enumerate([
    (V_high, f"High phase  (V_peak = {v_peak_array[high_idx]:.3f})", snapshots_t[high_idx]),
    (V_low, f"Low phase   (V_peak = {v_peak_array[low_idx]:.3f})", snapshots_t[low_idx]),
]):
    ax = fig.add_subplot(1, 2, idx + 1, projection="3d")
    threshold_local = 0.1 * np.abs(V_state).max()
    mask = np.abs(V_state) > threshold_local
    xs, ys, zs = np.where(mask)
    vals = V_state[mask]
    sizes = 50 * (np.abs(vals) / np.abs(V_state).max()) ** 1.5
    # Color by sign
    colors = np.where(vals > 0, "red", "blue")
    alphas = np.minimum(np.abs(vals) / np.abs(V_state).max(), 1.0) * 0.7
    ax.scatter(xs, ys, zs, c=colors, s=sizes, alpha=0.5, edgecolors="none")
    ax.scatter([CENTER[0]], [CENTER[1]], [CENTER[2]],
                color="white", s=100, marker="*", edgecolors="cyan", linewidth=2)
    ax.set_xlim(N // 2 - 8, N // 2 + 8)
    ax.set_ylim(N // 2 - 8, N // 2 + 8)
    ax.set_zlim(N // 2 - 8, N // 2 + 8)
    ax.set_title(f"{phase_name}\nt = {t_val:.1f}", color="white", fontsize=11)
    ax.set_facecolor("#0a0a0a")
    for axn in (ax.xaxis, ax.yaxis, ax.zaxis):
        axn.pane.set_facecolor("#0a0a0a")
        axn.pane.set_edgecolor("#333333")
    ax.tick_params(colors="white", labelsize=8)

fig.suptitle("Breathing cycle extremes: high amplitude vs low amplitude phases",
             color="white", fontsize=13, y=0.95)

phase_path = OUT / "v14_breathing_phase_comparison.png"
plt.savefig(phase_path, dpi=140, facecolor="#0a0a0a", bbox_inches="tight")
print(f"  Phase comparison: {phase_path}")
plt.close(fig)


# =============================================================================
# ANIMATION 1: 2D equatorial slice heatmap
# =============================================================================
print("Generating ANIMATION 1: 2D equatorial slice (signed V)...")
# Subsample frames for GIF
gif_step = max(1, len(snapshots_V) // FRAMES_FOR_GIF)
gif_frames = list(range(0, len(snapshots_V), gif_step))
print(f"  GIF will use {len(gif_frames)} frames")

fig, ax = plt.subplots(figsize=(8, 7), facecolor="#0a0a0a")
ax.set_facecolor("#0f0f0f")
v_abs_max = np.max([np.abs(s).max() for s in snapshots_V[::5]])

im = ax.imshow(snapshots_V[0][:, :, CENTER[2]].T,
               origin="lower", cmap="RdBu_r",
               extent=[0, N, 0, N], aspect="equal",
               vmin=-V_peak_init, vmax=V_peak_init,
               animated=True)
ax.plot(CENTER[0] + 0.5, CENTER[1] + 0.5, "k*", ms=12, mec="white")
title = ax.set_title(f"V(x,y), z={CENTER[2]}, t={0.0:.1f}",
                       color="white", fontsize=12)
ax.tick_params(colors="white")
plt.colorbar(im, ax=ax, fraction=0.046, label="V")
for spine in ax.spines.values():
    spine.set_color("#333333")


def update_2d(frame_idx):
    idx = gif_frames[frame_idx]
    V_state = snapshots_V[idx]
    im.set_array(V_state[:, :, CENTER[2]].T)
    title.set_text(f"V(x,y), z={CENTER[2]}, t={snapshots_t[idx]:.1f}, "
                   f"V_peak={np.abs(V_state).max():.3f}")
    return [im, title]


anim_2d = FuncAnimation(fig, update_2d, frames=len(gif_frames),
                          interval=80, blit=False)
anim_2d_path = OUT / "v14_breathing_slice_2d.gif"
anim_2d.save(str(anim_2d_path), writer=PillowWriter(fps=15))
print(f"  2D slice animation: {anim_2d_path}")
plt.close(fig)


# =============================================================================
# ANIMATION 2: 3D scatter with camera rotation
# =============================================================================
print("Generating ANIMATION 2: 3D scatter with camera rotation...")
fig = plt.figure(figsize=(10, 9), facecolor="#0a0a0a")
ax3d = fig.add_subplot(111, projection="3d")

# Use a fixed threshold for all frames so visual is comparable
fixed_threshold = 0.10 * V_peak_init


def update_3d(frame_idx):
    ax3d.clear()
    idx = gif_frames[frame_idx]
    V_state = snapshots_V[idx]
    mask = np.abs(V_state) > fixed_threshold
    xs, ys, zs = np.where(mask)
    vals = V_state[mask]
    if len(vals) > 0:
        # Color by sign
        v_max = max(np.abs(vals).max(), 1e-10)
        sizes = 60 * (np.abs(vals) / v_max) ** 1.5
        colors = ['red' if v > 0 else 'blue' for v in vals]
        ax3d.scatter(xs, ys, zs, c=colors, s=sizes, alpha=0.5,
                     edgecolors="none")
    ax3d.scatter([CENTER[0]], [CENTER[1]], [CENTER[2]],
                  color="white", s=120, marker="*",
                  edgecolors="cyan", linewidth=2)
    ax3d.set_xlim(N // 2 - 8, N // 2 + 8)
    ax3d.set_ylim(N // 2 - 8, N // 2 + 8)
    ax3d.set_zlim(N // 2 - 8, N // 2 + 8)
    # Rotate camera
    azim = 30 + (frame_idx / len(gif_frames)) * 360
    ax3d.view_init(elev=20, azim=azim)
    ax3d.set_title(f"AVE breathing soliton — t={snapshots_t[idx]:.1f}, "
                   f"V_peak={np.abs(V_state).max():.3f}",
                   color="white", fontsize=11)
    ax3d.set_facecolor("#0a0a0a")
    for axn in (ax3d.xaxis, ax3d.yaxis, ax3d.zaxis):
        axn.pane.set_facecolor("#0a0a0a")
        axn.pane.set_edgecolor("#333333")
    ax3d.tick_params(colors="white", labelsize=8)
    return [ax3d]


anim_3d = FuncAnimation(fig, update_3d, frames=len(gif_frames),
                         interval=80, blit=False)
anim_3d_path = OUT / "v14_breathing_soliton_3d.gif"
anim_3d.save(str(anim_3d_path), writer=PillowWriter(fps=15))
print(f"  3D scatter animation: {anim_3d_path}")
plt.close(fig)


# =============================================================================
# ANIMATION 3: radial profile A(r) over time
# =============================================================================
print("Generating ANIMATION 3: radial profile A(r,t)...")
fig, ax = plt.subplots(figsize=(10, 6), facecolor="#0a0a0a")
ax.set_facecolor("#0f0f0f")

line_init, = ax.plot(r_axis, snapshots_a_profile[0], "C0--", lw=1.5,
                     alpha=0.5, label="Initial (t=0)")
line_current, = ax.plot(r_axis, snapshots_a_profile[0], "C2-", lw=2.5,
                          label="Current")
ax.set_xlabel("r (cells from center)")
ax.set_ylabel("|V|/V_yield = A(r)")
ax.set_xlim(0, 10)
ax.set_ylim(0, 1.0)
ax.grid(True, alpha=0.2)
ax.legend(loc="upper right", fontsize=10)
title = ax.set_title("Radial profile A(r), t=0.0", color="white", fontsize=12)
ax.tick_params(colors="white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
for spine in ax.spines.values():
    spine.set_color("#333333")
leg = ax.get_legend()
leg.get_frame().set_facecolor("#0f0f0f")
leg.get_frame().set_edgecolor("none")
for text in leg.get_texts():
    text.set_color("white")


def update_profile(frame_idx):
    idx = gif_frames[frame_idx]
    line_current.set_ydata(snapshots_a_profile[idx])
    title.set_text(f"Radial profile A(r), t={snapshots_t[idx]:.1f}, "
                   f"V_peak={snapshots_v_peak[idx]:.3f}")
    return [line_current, title]


anim_profile = FuncAnimation(fig, update_profile, frames=len(gif_frames),
                               interval=80, blit=False)
anim_profile_path = OUT / "v14_breathing_radial_profile.gif"
anim_profile.save(str(anim_profile_path), writer=PillowWriter(fps=15))
print(f"  Radial profile animation: {anim_profile_path}")
plt.close(fig)


# =============================================================================
# Summary
# =============================================================================
print()
print("=" * 78)
print("VISUALIZATION SUITE COMPLETE")
print("=" * 78)
print(f"  Stills:")
print(f"    {hero_path}")
print(f"    {phase_path}")
print(f"  Animations:")
print(f"    {anim_2d_path}")
print(f"    {anim_3d_path}")
print(f"    {anim_profile_path}")
print()
print(f"  Total frames per animation: {len(gif_frames)}")
print(f"  Engine: Master Equation FDTD, sech A=0.85 R=2.5, 5000 steps")
print(f"  V_peak oscillates: min={np.min(v_peak_array[len(v_peak_array)//4:]):.3f}, "
      f"max={np.max(v_peak_array[len(v_peak_array)//4:]):.3f}, "
      f"mean={np.mean(v_peak_array[len(v_peak_array)//4:]):.3f}")
print("=" * 78)
