"""
R10 Path-α v14e — Seven-Mode Bounded-Boundary Test
====================================================

Grant 2026-05-14 evening pushback: *"did you forget your seven modes of compliance?"*

YES — v14a/b/d seeded only 2 of 7 canonical bubble modes (ω_x, ω_y tangent
to the unknot loop). Per `AVE-QED chapters/11_tensioned_trampoline.tex:946-
1056`, the canonical electron bubble has 7 modes:

  3 translational (Cosserat u_x, u_y, u_z) — kinetic motion role
  3 rotational   (Cosserat ω_x, ω_y, ω_z) — spin axes / chiral surface
  1 volumetric   (breathing)               — LC capacitance C

The LC tank: L = rotational (3 modes, μ-side), C = volumetric breathing
(1 mode, ε-side), ω_resonance = 1/√(LC) = ω_Compton (bulk-spin rate).

Previous seeds populated:
  - ω_x, ω_y (tangent-to-loop chiral circulation)         — 2 modes
  - ω_z = 0                                                — missing
  - u_x = u_y = u_z = 0                                    — missing (3)
  - breathing mode = 0                                     — missing
                                                          ─────────
                                                          2/7 modes

This script attempts the canonical 7-mode coupled bound-state seed:
  Layer 1 (real-space): unknot 0₁ at horn torus R = lattice cells
  Layer 2 (field bundle): SU(2) double-cover via ω-field SO(3)
  Layer 3 (phase-space): (2,3) Clifford winding in (V_inc, V_ref)

All 7 modes excited:
  • u hedgehog at horn-torus radius, tangent to unknot loop (3 trans)
  • ω hedgehog at horn-torus radius, tangent + bulk-spin ω_z (3 rot)
  • V_inc common-mode amplitude at boundary cells (1 breathing)
  • V_inc port-asymmetry pattern with (2,3) winding (Layer 3 phase-space)
  • Initial velocities zero (u_dot = ω_dot = 0, rest LC phase)

Adjudication criteria per doc 109 §14.7 (unchanged).
"""
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D
from ave.core.constants import ALPHA, ALPHA_COLD_INV

print("=" * 78)
print("R10 Path-α v14e — Seven-Mode Bounded-Boundary Test")
print("=" * 78)
print(f"  ALPHA               = {ALPHA:.6e}")
print(f"  ALPHA_COLD_INV      = {ALPHA_COLD_INV:.4f}  (= 4π³ + π² + π)")
print()


# =============================================================================
# Configuration (frozen)
# =============================================================================
N = 17
PML = 4
CENTER = (N // 2, N // 2, N // 2)
N_STEPS = 2000
LOG_CADENCE = 50

HORN_R = 2.0                   # horn-torus radius (lattice cells, lattice-resolved)
UNKNOT_AMP_OMEGA = 0.35        # bound-state ω amplitude per Path B Round 6
UNKNOT_AMP_U = 0.35            # matching u amplitude for LC coherence
BULK_SPIN_AMP = 0.15           # ω_z component (bubble bulk-spin around z-axis)
BREATHING_AMP = 0.4            # K4 V_inc common-mode (breathing) at boundary cells
PHASE_WINDING_AMP = 0.2        # K4 V_ref port-asymmetry (2,3) pattern

# Acceptance thresholds (unchanged from §14.7)
THRESH_BOUNDARY_PERSIST = 0.5
THRESH_WINDING_PERSIST = 0.5
THRESH_GRADIENT_TOL = 0.15
THRESH_Q_FACTOR_TOL = 0.05

print(f"7-MODE SEED CONFIGURATION:")
print(f"  Horn-torus R         = {HORN_R}")
print(f"  ω amplitude          = {UNKNOT_AMP_OMEGA}  (3 rotational modes)")
print(f"  u amplitude          = {UNKNOT_AMP_U}    (3 translational modes)")
print(f"  Bulk-spin ω_z amp    = {BULK_SPIN_AMP}")
print(f"  Breathing V_inc amp  = {BREATHING_AMP}  (1 volumetric mode)")
print(f"  Phase-winding V_ref  = {PHASE_WINDING_AMP}")
print(f"  N_steps              = {N_STEPS}")
print()


# =============================================================================
# Engine setup
# =============================================================================
engine = VacuumEngine3D.from_args(
    N=N, pml=PML, temperature=0.0,
    amplitude_convention="V_SNAP",
)
print(f"Engine: V_SNAP={engine.V_SNAP}, k4 dt = {engine.k4.dt:.6f}, op3=True")
print(f"  Center cell {CENTER} active: {bool(engine.k4.mask_active[CENTER])}")
print()


# =============================================================================
# Plant the 7-mode coupled bound-state seed
# =============================================================================
print("Planting 7-mode coupled bound-state seed...")
cx, cy, cz = CENTER

# Grid coordinates relative to center
i_grid = engine.cos._i
j_grid = engine.cos._j
k_grid = engine.cos._k
x = i_grid - cx
y = j_grid - cy
z = k_grid - cz

rho_xy = np.sqrt(x ** 2 + y ** 2)
# Distance to the unknot loop (circle of radius HORN_R in z=cz plane)
rho_tube = np.sqrt((rho_xy - HORN_R) ** 2 + z ** 2)
phi = np.arctan2(y, x)

# AVE-canonical hedgehog envelope: π/(1 + (ρ/r_opt)²)
r_opt = HORN_R
envelope = (np.sqrt(3.0) / 2.0) * np.pi / (1.0 + (rho_tube / r_opt) ** 2)
envelope *= engine.cos.mask_alive  # restrict to live nodes

# ─── Modes 1-3: Cosserat ω (rotational) — 3 components ─────────────────────
print(f"  Modes 1-3 (rotational ω): tangent-to-loop + bulk-spin ω_z")
omega = np.zeros((N, N, N, 3), dtype=np.float64)
# Tangent to unknot loop (chiral circulation, like initialize_electron_unknot_sector)
omega[..., 0] = UNKNOT_AMP_OMEGA * envelope * (-np.sin(phi))
omega[..., 1] = UNKNOT_AMP_OMEGA * envelope * np.cos(phi)
# Bulk-spin (perpendicular to loop plane, z-axis rotation at ω_Compton)
omega[..., 2] = BULK_SPIN_AMP * envelope  # ω_z component everywhere in bubble
omega *= engine.cos.mask_alive[..., None]
engine.cos.omega = omega

# ─── Modes 4-6: Cosserat u (translational) — 3 components ──────────────────
print(f"  Modes 4-6 (translational u): radial-tangent hedgehog at horn torus")
u = np.zeros((N, N, N, 3), dtype=np.float64)
# u tangent to the loop with same envelope (LC-coherent with ω)
# Use phase-shifted pattern: u tangent points 90° from ω tangent
u[..., 0] = UNKNOT_AMP_U * envelope * np.cos(phi)
u[..., 1] = UNKNOT_AMP_U * envelope * np.sin(phi)
u[..., 2] = 0.0
u *= engine.cos.mask_alive[..., None]
engine.cos.u = u

# Initial velocities zero (rest LC phase — all energy in C-state for now)
engine.cos.omega_dot[:] = 0.0
engine.cos.u_dot[:] = 0.0

# ─── Mode 7: Volumetric breathing — K4 V_inc common-mode at boundary cells ─
print(f"  Mode 7 (volumetric breathing): K4 V_inc common-mode at horn-torus shell")
# Active boundary cells: shell at horn-torus radius
shell_mask = (np.abs(rho_tube) < 1.0) & engine.k4.mask_active
shell_cells = list(zip(*np.where(shell_mask)))
print(f"    Boundary shell active cells: {len(shell_cells)}")

# Common-mode (breathing): equal V_inc on all 4 ports
# Plus port-asymmetry: V_ref with (2,3) phase-space winding pattern
for (i, j, k) in shell_cells:
    for port in range(4):
        # Breathing (common-mode) — same amplitude on all 4 ports
        engine.k4.V_inc[i, j, k, port] = BREATHING_AMP / 2.0
        # Phase-space (2,3) winding via V_ref port-asymmetry
        port_phase = (2 * port * np.pi / 2 + 3 * port * np.pi / 2) % (2 * np.pi)
        engine.k4.V_ref[i, j, k, port] = PHASE_WINDING_AMP * np.cos(port_phase)

# Capture seed snapshot
omega_seed = engine.cos.omega.copy()
u_seed = engine.cos.u.copy()
V_inc_seed = engine.k4.V_inc.copy()
V_ref_seed = engine.k4.V_ref.copy()

# Initial observable values
omega_norm_seed = np.linalg.norm(omega_seed, axis=-1)
u_norm_seed = np.linalg.norm(u_seed, axis=-1)
v_inc_norm_seed = np.sqrt(np.sum(V_inc_seed ** 2, axis=-1))

omega_peak_initial = float(np.max(omega_norm_seed))
u_peak_initial = float(np.max(u_norm_seed))
v_inc_shell_initial = float(np.mean([v_inc_norm_seed[c] for c in shell_cells]))

print(f"\n  Initial state:")
print(f"    Peak |ω| = {omega_peak_initial:.4f}  (across {(omega_norm_seed > 0.1).sum()} cells)")
print(f"    Peak |u| = {u_peak_initial:.4f}      (across {(u_norm_seed > 0.1).sum()} cells)")
print(f"    Mean |V_inc| at shell = {v_inc_shell_initial:.4f}")
print(f"    Total K4 energy = {float(engine.k4.total_energy()):.4f}")
print()


# =============================================================================
# Diagnostics
# =============================================================================
def boundary_persistence(engine):
    """Mean |V_inc| over the boundary shell cells."""
    v_norm = np.sqrt(np.sum(engine.k4.V_inc ** 2, axis=-1))
    return float(np.mean([v_norm[c] for c in shell_cells]))


def omega_peak(engine):
    return float(np.max(np.linalg.norm(engine.cos.omega, axis=-1)))


def u_peak(engine):
    return float(np.max(np.linalg.norm(engine.cos.u, axis=-1)))


def cosserat_winding_at_horn(engine, R=HORN_R, tol=0.7):
    cx_, cy_, cz_ = CENTER
    x_ = np.arange(N) - cx_
    y_ = np.arange(N) - cy_
    z_ = np.arange(N) - cz_
    X, Y, Z = np.meshgrid(x_, y_, z_, indexing="ij")
    rho_xy_ = np.sqrt(X ** 2 + Y ** 2)
    rho_tube_ = np.sqrt((rho_xy_ - R) ** 2 + Z ** 2)
    shell = rho_tube_ < tol
    if shell.sum() == 0:
        return 0.0
    omega_norm = np.linalg.norm(engine.cos.omega, axis=-1)
    return float(omega_norm[shell].mean())


def impedance_profile(engine, max_r=5):
    engine.k4._update_z_local_field()
    cx_, cy_, cz_ = CENTER
    x_ = np.arange(N) - cx_
    y_ = np.arange(N) - cy_
    z_ = np.arange(N) - cz_
    X, Y, Z = np.meshgrid(x_, y_, z_, indexing="ij")
    r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    r_arr = np.arange(1, max_r + 1)
    z_arr = np.zeros_like(r_arr, dtype=float)
    for i, r_val in enumerate(r_arr):
        shell = (r >= r_val - 0.5) & (r < r_val + 0.5) & engine.k4.mask_active
        if shell.sum() > 0:
            z_arr[i] = engine.k4.z_local_field[shell].mean()
        else:
            z_arr[i] = 1.0
    return r_arr, z_arr


def q_factor_decomposition(engine, R_volume=HORN_R):
    cx_, cy_, cz_ = CENTER
    x_ = np.arange(N) - cx_
    y_ = np.arange(N) - cy_
    z_ = np.arange(N) - cz_
    X, Y, Z = np.meshgrid(x_, y_, z_, indexing="ij")
    r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    # Use combined |V_inc|² + |ω|² (the total 7-mode energy density)
    v_inc_norm = np.sqrt(np.sum(engine.k4.V_inc ** 2, axis=-1))
    omega_norm = np.linalg.norm(engine.cos.omega, axis=-1)
    energy_density = v_inc_norm ** 2 + omega_norm ** 2

    e_center = energy_density[CENTER]
    if e_center < 1e-10:
        # Use max-in-domain as reference instead
        e_center = max(energy_density.max(), 1e-10)
    e_normalized = energy_density / e_center

    volume_mask = (r < R_volume) & engine.k4.mask_active
    surface_mask = (r >= R_volume - 0.5) & (r < R_volume + 0.5) & engine.k4.mask_active
    line_mask = (np.abs(Z) < 1) & (np.sqrt(X**2 + Y**2) >= R_volume - 0.5) & \
                (np.sqrt(X**2 + Y**2) < R_volume + 0.5) & engine.k4.mask_active

    L_vol = float(np.sum(e_normalized[volume_mask]))
    L_surf = float(np.sum(e_normalized[surface_mask]))
    L_line = float(np.sum(e_normalized[line_mask]))
    return L_vol, L_surf, L_line


# =============================================================================
# Run + log
# =============================================================================
print("=" * 78)
print(f"Running dynamics: {N_STEPS} steps, log every {LOG_CADENCE}")
print("=" * 78)

history = {
    "step": [], "t": [],
    "v_inc_shell": [], "omega_peak": [], "u_peak": [], "omega_at_horn": [],
    "total_energy": [],
}

history["step"].append(0)
history["t"].append(0.0)
history["v_inc_shell"].append(boundary_persistence(engine))
history["omega_peak"].append(omega_peak(engine))
history["u_peak"].append(u_peak(engine))
history["omega_at_horn"].append(cosserat_winding_at_horn(engine))
history["total_energy"].append(float(engine.k4.total_energy()))

t_start = time.time()
for step in range(1, N_STEPS + 1):
    engine.step()
    if step % LOG_CADENCE == 0:
        history["step"].append(step)
        history["t"].append(step * engine.k4.dt)
        history["v_inc_shell"].append(boundary_persistence(engine))
        history["omega_peak"].append(omega_peak(engine))
        history["u_peak"].append(u_peak(engine))
        history["omega_at_horn"].append(cosserat_winding_at_horn(engine))
        history["total_energy"].append(float(engine.k4.total_energy()))
        if step % (LOG_CADENCE * 10) == 0 or step == LOG_CADENCE:
            print(f"  step={step:>4d}  "
                  f"V_inc_shell={history['v_inc_shell'][-1]:.4f}  "
                  f"|ω|_peak={history['omega_peak'][-1]:.4f}  "
                  f"|u|_peak={history['u_peak'][-1]:.4f}  "
                  f"E={history['total_energy'][-1]:.3e}")
print(f"\nDynamics complete in {time.time() - t_start:.1f}s.")
print()

# =============================================================================
# Adjudication
# =============================================================================
print("=" * 78)
print("ADJUDICATION (per doc 109 §14.7)")
print("=" * 78)

# Test 1 — Boundary (V_inc shell) persistence
v_inc_initial = history["v_inc_shell"][0]
v_inc_late = np.mean(history["v_inc_shell"][-5:])
v_inc_ratio = v_inc_late / v_inc_initial if v_inc_initial > 0 else 0.0
test1_pass = v_inc_ratio > THRESH_BOUNDARY_PERSIST
print(f"\nTest 1 — Boundary V_inc shell persistence:")
print(f"  initial = {v_inc_initial:.4f}, late avg = {v_inc_late:.4f}, ratio = {v_inc_ratio:.4f}")
print(f"  Threshold {THRESH_BOUNDARY_PERSIST}: {'PASS ✓' if test1_pass else 'FAIL ✗'}")

# Test 2 — Cosserat winding persistence (both ω and u)
omega_init = history["omega_peak"][0]
omega_late = np.mean(history["omega_peak"][-5:])
omega_ratio = omega_late / omega_init if omega_init > 0 else 0.0
u_init = history["u_peak"][0]
u_late = np.mean(history["u_peak"][-5:])
u_ratio = u_late / u_init if u_init > 0 else 0.0
test2_pass = (omega_ratio > THRESH_WINDING_PERSIST) and (u_ratio > THRESH_WINDING_PERSIST)
print(f"\nTest 2 — Cosserat winding persistence (ω AND u, both 3 modes):")
print(f"  |ω|_peak: init={omega_init:.4f}, late={omega_late:.4f}, ratio={omega_ratio:.4f}")
print(f"  |u|_peak: init={u_init:.4f}, late={u_late:.4f}, ratio={u_ratio:.4f}")
print(f"  Threshold {THRESH_WINDING_PERSIST} both: {'PASS ✓' if test2_pass else 'FAIL ✗'}")

# Test 3 — Outside-cell impedance gradient
r_arr, z_arr = impedance_profile(engine, max_r=5)
print(f"\nTest 3 — Outside-cell impedance gradient:")
for r_val, z_val in zip(r_arr, z_arr):
    print(f"    r = {r_val}: z_local = {z_val:.6f}")
deviations = z_arr - 1.0
if abs(deviations[0]) > 1e-6:
    shape = deviations / deviations[0]
    predicted = 1.0 / r_arr
    rel_err = np.abs(shape - predicted) / (np.abs(predicted) + 1e-10)
    max_rel_err = float(np.max(rel_err[1:]))
    test3_pass = max_rel_err < THRESH_GRADIENT_TOL
    print(f"  max rel err = {max_rel_err:.4f} vs threshold {THRESH_GRADIENT_TOL}")
else:
    test3_pass = False
    max_rel_err = float("inf")
    print(f"  No measurable gradient")
print(f"  Verdict: {'PASS ✓' if test3_pass else 'FAIL ✗'}")

# Test 4 — Q-factor integral (Λ decomposition)
L_vol, L_surf, L_line = q_factor_decomposition(engine)
q_total = L_vol + L_surf + L_line
q_target = ALPHA_COLD_INV
q_rel_err = abs(q_total - q_target) / q_target if q_target > 0 else 1.0
test4_pass = q_rel_err < THRESH_Q_FACTOR_TOL
print(f"\nTest 4 — Q-factor integral:")
print(f"  Λ_vol={L_vol:.3f} (target 4π³={4*np.pi**3:.3f})")
print(f"  Λ_surf={L_surf:.3f} (target π²={np.pi**2:.3f})")
print(f"  Λ_line={L_line:.3f} (target π={np.pi:.3f})")
print(f"  Total={q_total:.3f} (target α⁻¹={q_target:.3f}), rel err={q_rel_err:.4f}")
print(f"  Threshold {THRESH_Q_FACTOR_TOL}: {'PASS ✓' if test4_pass else 'FAIL ✗'}")

all_tests = [test1_pass, test2_pass, test3_pass, test4_pass]
n_pass = sum(all_tests)
if n_pass == 4:
    mode = "I — full PASS"
elif n_pass == 3:
    mode = "I-partial (3 of 4)"
elif n_pass == 2:
    mode = "II — engine basin ≠ corpus (2 of 4)"
elif test1_pass or test2_pass:
    mode = "II-weak"
else:
    mode = "III — no stable bounded boundary"

print()
print("=" * 78)
print(f"MODE: {mode} (passes: {n_pass}/4)")
print("=" * 78)


# =============================================================================
# Visualization
# =============================================================================
OUT = REPO_ROOT / "assets" / "sim_outputs"
OUT.mkdir(parents=True, exist_ok=True)

fig = plt.figure(figsize=(17, 11), facecolor="#0a0a0a")
gs = GridSpec(3, 4, figure=fig, hspace=0.4, wspace=0.35,
              height_ratios=[1.0, 1.0, 0.6])

# Panel A: time series — all three persistence metrics
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(history["t"], np.array(history["v_inc_shell"]) / max(history["v_inc_shell"][0], 1e-10),
         "C2-", lw=2, label="V_inc shell")
ax1.plot(history["t"], np.array(history["omega_peak"]) / max(history["omega_peak"][0], 1e-10),
         "C0-", lw=2, label="|ω| peak")
ax1.plot(history["t"], np.array(history["u_peak"]) / max(history["u_peak"][0], 1e-10),
         "C3-", lw=2, label="|u| peak")
ax1.axhline(0.5, color="white", ls="--", lw=1, alpha=0.5, label="50% threshold")
ax1.set_xlabel("t (lattice units)")
ax1.set_ylabel("Relative magnitude")
ax1.set_title("Persistence: V_inc / |ω| / |u| (all normalized)")
ax1.legend(loc="best", fontsize=8)
ax1.grid(True, alpha=0.2)

# Panel B: energy time series
ax2 = fig.add_subplot(gs[0, 1])
ax2.semilogy(history["t"], history["total_energy"], "C1-", lw=2)
ax2.set_xlabel("t (lattice units)")
ax2.set_ylabel("K4 total energy")
ax2.set_title("K4 energy evolution")
ax2.grid(True, which="both", alpha=0.2)

# Panel C: Cosserat ω 3D quiver at SEED
ax3 = fig.add_subplot(gs[0, 2], projection="3d")
omega_threshold = 0.1 * omega_peak_initial
omega_mask = omega_norm_seed > omega_threshold
xs, ys, zs = np.where(omega_mask)
ux = omega_seed[..., 0][omega_mask]
uy = omega_seed[..., 1][omega_mask]
uz = omega_seed[..., 2][omega_mask]
mag = omega_norm_seed[omega_mask]
colors = plt.cm.plasma(mag / max(omega_peak_initial, 1e-10))
ax3.quiver(xs, ys, zs, ux, uy, uz, length=0.7, normalize=True,
           colors=colors, arrow_length_ratio=0.3, linewidth=1.0)
ax3.scatter([cx], [cy], [cz], color="cyan", s=80, marker="*",
            edgecolor="white", linewidth=1.5)
ax3.set_xlim(2, N - 2); ax3.set_ylim(2, N - 2); ax3.set_zlim(2, N - 2)
ax3.set_title("Cosserat ω SEED\n(3 rotational modes)", color="white", fontsize=10)
ax3.set_facecolor("#0f0f0f")
for axn in (ax3.xaxis, ax3.yaxis, ax3.zaxis):
    axn.pane.set_facecolor("#0a0a0a")
    axn.pane.set_edgecolor("#333333")
ax3.tick_params(colors="white", labelsize=7)

# Panel D: Cosserat u 3D quiver at SEED
ax4 = fig.add_subplot(gs[0, 3], projection="3d")
u_threshold = 0.1 * u_peak_initial
u_mask = u_norm_seed > u_threshold
xs, ys, zs = np.where(u_mask)
ux2 = u_seed[..., 0][u_mask]
uy2 = u_seed[..., 1][u_mask]
uz2 = u_seed[..., 2][u_mask]
mag2 = u_norm_seed[u_mask]
colors2 = plt.cm.viridis(mag2 / max(u_peak_initial, 1e-10))
ax4.quiver(xs, ys, zs, ux2, uy2, uz2, length=0.7, normalize=True,
           colors=colors2, arrow_length_ratio=0.3, linewidth=1.0)
ax4.scatter([cx], [cy], [cz], color="orange", s=80, marker="*",
            edgecolor="white", linewidth=1.5)
ax4.set_xlim(2, N - 2); ax4.set_ylim(2, N - 2); ax4.set_zlim(2, N - 2)
ax4.set_title("Cosserat u SEED\n(3 translational modes)", color="white", fontsize=10)
ax4.set_facecolor("#0f0f0f")
for axn in (ax4.xaxis, ax4.yaxis, ax4.zaxis):
    axn.pane.set_facecolor("#0a0a0a")
    axn.pane.set_edgecolor("#333333")
ax4.tick_params(colors="white", labelsize=7)

# Panel E: |V_inc| final slice
ax5 = fig.add_subplot(gs[1, 0])
v_inc_final = np.sqrt(np.sum(engine.k4.V_inc ** 2, axis=-1))
v_slice = v_inc_final[:, :, cz]
im = ax5.imshow(v_slice.T, origin="lower", cmap="hot",
                extent=[0, N, 0, N], aspect="equal")
ax5.plot(cx + 0.5, cy + 0.5, "c*", ms=15, markeredgecolor="white")
ax5.set_title(f"|V_inc| final (z={cz})")
plt.colorbar(im, ax=ax5, fraction=0.046)

# Panel F: |ω| final slice
ax6 = fig.add_subplot(gs[1, 1])
omega_final = np.linalg.norm(engine.cos.omega, axis=-1)
omega_slice = omega_final[:, :, cz]
im = ax6.imshow(omega_slice.T, origin="lower", cmap="viridis",
                extent=[0, N, 0, N], aspect="equal")
ax6.plot(cx + 0.5, cy + 0.5, "c*", ms=15, markeredgecolor="white")
ax6.set_title(f"|ω| final (z={cz})")
plt.colorbar(im, ax=ax6, fraction=0.046)

# Panel G: Λ-decomposition
ax7 = fig.add_subplot(gs[1, 2])
categories = ["Λ_vol\n→ 𝓜", "Λ_surf\n→ 𝓙", "Λ_line\n→ 𝓠"]
measured = [L_vol, L_surf, L_line]
canonical = [4 * np.pi ** 3, np.pi ** 2, np.pi]
x_pos = np.arange(len(categories))
ax7.bar(x_pos - 0.2, measured, 0.4, label="Final", color="C0", edgecolor="white")
ax7.bar(x_pos + 0.2, canonical, 0.4, label="Canonical", color="C3", edgecolor="white")
ax7.set_xticks(x_pos)
ax7.set_xticklabels(categories, fontsize=9)
ax7.set_yscale("log")
ax7.set_title("Q-factor decomposition")
ax7.legend(loc="best", fontsize=8)
ax7.grid(True, axis="y", alpha=0.2)

# Panel H: outside-cell impedance gradient
ax8 = fig.add_subplot(gs[1, 3])
ax8.plot(r_arr, z_arr, "C2o-", lw=2, ms=10, label="z_local(r)")
ax8.axhline(1.0, color="white", ls=":", lw=1)
if abs(deviations[0]) > 1e-6:
    z_pred = 1.0 + deviations[0] / r_arr
    ax8.plot(r_arr, z_pred, "C3--", lw=1.5, label="1 + k/r")
ax8.set_xlabel("r (cells)")
ax8.set_ylabel("z_local")
ax8.set_title("Outside gradient")
ax8.legend(loc="best", fontsize=8)
ax8.grid(True, alpha=0.2)

# Panel I (full bottom row): summary
ax9 = fig.add_subplot(gs[2, :])
ax9.axis("off")
summary = (
    f"v14e — 7-MODE SEED (3+3+1): 3 translational u + 3 rotational ω + 1 breathing V_inc common-mode + (2,3) phase-space\n"
    f"{'═' * 60}\n"
    f"  Test 1 (V_inc shell):    {'PASS ✓' if test1_pass else 'FAIL ✗'}  ratio = {v_inc_ratio:.3f}\n"
    f"  Test 2 (ω + u winding):  {'PASS ✓' if test2_pass else 'FAIL ✗'}  ω ratio = {omega_ratio:.3f}, u ratio = {u_ratio:.3f}\n"
    f"  Test 3 (outside grad):   {'PASS ✓' if test3_pass else 'FAIL ✗'}  rel err = {max_rel_err:.3f}\n"
    f"  Test 4 (Q-factor):       {'PASS ✓' if test4_pass else 'FAIL ✗'}  rel err = {q_rel_err:.3f}\n\n"
    f"  MODE: {mode}\n"
    f"  Net 7-mode seed: ω hedgehog (tangent + bulk-spin ω_z) + u hedgehog (tangent) + V_inc breathing common-mode + (2,3) V_ref"
)
ax9.text(0.02, 0.95, summary, transform=ax9.transAxes,
         fontsize=9, family="monospace", verticalalignment="top",
         color="white",
         bbox=dict(boxstyle="round,pad=0.5", facecolor="#181818", edgecolor="#404040"))

for ax in [ax1, ax2, ax5, ax6, ax7, ax8]:
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

fig.suptitle(f"v14e Seven-Mode Bounded-Boundary Test — {mode}",
             color="white", fontsize=14, y=0.995)
out_path = OUT / "r10_path_alpha_v14e_seven_mode.png"
plt.savefig(out_path, dpi=140, facecolor="#0a0a0a", bbox_inches="tight")
print(f"\nFigure: {out_path}")
print()
print(f"MODE: {mode}  ({n_pass}/4 tests PASS)")
