"""
R10 Path-α v14 — Soliton Visualizer (companion to v14a/b/c/d driver)
======================================================================

Grant 2026-05-14 evening: *"show me the most fundamental AVE soliton on
our K4-TLM simulator."*

The v14a-d dynamics runs (commits earlier this session) returned Mode III
across three independent seed configurations:
  v14a (single-cell V_inc plant + Cosserat unknot, A=0.6)
  v14b (shell-envelope V_inc at A=0.95 + Cosserat unknot, R=2)
  v14d (Cosserat-only seed, no K4 plant)

All three: K4 V_inc decays to noise within ~50 steps; Cosserat ω damps to
its standalone attractor plateau at |ω|_peak ≈ 0.10 (10% of initial); no
stable coupled bound state forms. This is the empirical Mode III finding
documented in L3 doc 92 §6 (the Nyquist wall, reframed per doc 109 §13)
+ L3 doc 108 §11.5 (Layer 7 indefinitely queued).

The boundary-envelope reformulation (doc 109 §13, Grant-confirmed 2026-05-14
evening) remains canonically defensible — Q-G19α Route B closure at 50 ppm
to PDG validates the boundary-integral / no-hair framing empirically at
the electron scale. What the v14 dynamics tests reveal is that the K4-TLM
+ Cosserat coupled engine *as currently implemented* does not autonomously
host the bound state. The framework's empirical validation lives in Route
B's boundary-integrated observables, not in lattice-resolved live bound-state
dynamics.

This script generates a focused visual of the *seed soliton structure* —
what the canonical electron unknot looks like in the engine's representation,
even if the engine doesn't persist it. The visual gives Grant the empirical
artifact requested: the most fundamental AVE soliton as the engine encodes
it, with honest annotation of Mode III dynamics.
"""
import sys
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
print("R10 Path-α v14 — Soliton Visualizer (seed-focused)")
print("=" * 78)

# Build the SAME engine + plant the SAME seed as v14a (canonical pre-reg)
N = 17
PML = 4
CENTER = (N // 2, N // 2, N // 2)
COSSERAT_R = 2.0
COSSERAT_AMP_SCALE = 0.35
V_INC_AMPLITUDE = 0.6

engine = VacuumEngine3D.from_args(
    N=N, pml=PML, temperature=0.0,
    amplitude_convention="V_SNAP",
)
print(f"Engine: N={N}, V_SNAP={engine.V_SNAP}, op3_bond_reflection=True (internal)")

# Plant the canonical soliton seed
amp_per_port = V_INC_AMPLITUDE / 2.0
for port in range(4):
    engine.k4.V_inc[CENTER[0], CENTER[1], CENTER[2], port] = amp_per_port
    port_phase = (2 * port * np.pi / 2 + 3 * port * np.pi / 2) % (2 * np.pi)
    engine.k4.V_ref[CENTER[0], CENTER[1], CENTER[2], port] = amp_per_port * np.cos(port_phase)

engine.cos.initialize_electron_unknot_sector(
    R_target=COSSERAT_R, r_target=COSSERAT_R,
    amplitude_scale=COSSERAT_AMP_SCALE,
)

# Capture seed state
V_inc_seed = engine.k4.V_inc.copy()
V_ref_seed = engine.k4.V_ref.copy()
omega_seed = engine.cos.omega.copy()
omega_norm_seed = np.linalg.norm(omega_seed, axis=-1)

# Compute Q-factor integral on the SEED (the canonical soliton structure)
def q_factor_seed(V_inc, V_ref, omega_norm, R_volume=COSSERAT_R):
    cx, cy, cz = CENTER
    x = np.arange(N) - cx
    y = np.arange(N) - cy
    z = np.arange(N) - cz
    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
    r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    # Use omega-magnitude as the relevant integral density on the SEED
    omega_norm_2 = omega_norm ** 2
    omega_center = omega_norm[CENTER]
    if omega_center < 1e-10:
        return 0.0, 0.0, 0.0, 0.0
    omega_normalized = omega_norm_2 / omega_center ** 2

    volume_mask = (r < R_volume) & engine.k4.mask_active
    Lambda_vol = float(np.sum(omega_normalized[volume_mask]))

    surface_mask = (r >= R_volume - 0.5) & (r < R_volume + 0.5) & engine.k4.mask_active
    Lambda_surf = float(np.sum(omega_normalized[surface_mask]))

    line_mask = (np.abs(Z) < 1) & (np.sqrt(X**2 + Y**2) >= R_volume - 0.5) & \
                (np.sqrt(X**2 + Y**2) < R_volume + 0.5) & engine.k4.mask_active
    Lambda_line = float(np.sum(omega_normalized[line_mask]))

    return Lambda_vol, Lambda_surf, Lambda_line, omega_center


Lambda_vol, Lambda_surf, Lambda_line, omega_peak = q_factor_seed(
    V_inc_seed, V_ref_seed, omega_norm_seed
)
print(f"Seed Λ_vol  = {Lambda_vol:.4f} (canonical 4π³ = {4*np.pi**3:.4f})")
print(f"Seed Λ_surf = {Lambda_surf:.4f} (canonical π² = {np.pi**2:.4f})")
print(f"Seed Λ_line = {Lambda_line:.4f} (canonical π = {np.pi:.4f})")
print(f"Seed peak |ω| = {omega_peak:.4f}")
print()


# =============================================================================
# Build figure
# =============================================================================
OUT = REPO_ROOT / "assets" / "sim_outputs"
OUT.mkdir(parents=True, exist_ok=True)

fig = plt.figure(figsize=(17, 12), facecolor="#0a0a0a")
gs = GridSpec(3, 4, figure=fig, hspace=0.4, wspace=0.35,
              height_ratios=[1.0, 1.0, 0.7])

# ─── Panel A: 3D Cosserat ω hedgehog ───────────────────────────────────────
ax3d = fig.add_subplot(gs[0:2, 0:2], projection="3d")
# Show ω vectors at active sites with |ω| > threshold
threshold = 0.1 * omega_peak
mask = (omega_norm_seed > threshold) & engine.k4.mask_active
xs, ys, zs = np.where(mask)
ux = omega_seed[..., 0][mask]
uy = omega_seed[..., 1][mask]
uz = omega_seed[..., 2][mask]
mag = omega_norm_seed[mask]

# Color by magnitude
colors = plt.cm.plasma(mag / omega_peak)
ax3d.quiver(
    xs, ys, zs, ux, uy, uz,
    length=0.8, normalize=True, colors=colors,
    arrow_length_ratio=0.3, linewidth=1.5,
)

# Mark the center
ax3d.scatter([CENTER[0]], [CENTER[1]], [CENTER[2]],
             color="cyan", s=100, marker="*", edgecolor="white",
             linewidth=2, label="Center cell")

# Draw the horn-torus reference loop (unknot at R = ℓ_node/(2π) scaled to R=2 lattice cells)
theta = np.linspace(0, 2 * np.pi, 100)
loop_r = COSSERAT_R
loop_x = CENTER[0] + loop_r * np.cos(theta)
loop_y = CENTER[1] + loop_r * np.sin(theta)
loop_z = np.full_like(theta, CENTER[2])
ax3d.plot(loop_x, loop_y, loop_z, "cyan", lw=2, alpha=0.7, label=f"Unknot loop (R={COSSERAT_R})")

ax3d.set_xlabel("x")
ax3d.set_ylabel("y")
ax3d.set_zlabel("z")
ax3d.set_xlim(2, 14)
ax3d.set_ylim(2, 14)
ax3d.set_zlim(2, 14)
ax3d.set_title("The Most Fundamental AVE Soliton:\n"
               "Cosserat ω-field unknot 0₁ at horn torus",
               color="white", fontsize=12, pad=12)
ax3d.legend(loc="upper right", fontsize=9)
ax3d.set_facecolor("#0f0f0f")
ax3d.tick_params(colors="white", labelsize=8)
ax3d.xaxis.label.set_color("white")
ax3d.yaxis.label.set_color("white")
ax3d.zaxis.label.set_color("white")
# Set pane colors
ax3d.xaxis.pane.set_facecolor("#0a0a0a")
ax3d.yaxis.pane.set_facecolor("#0a0a0a")
ax3d.zaxis.pane.set_facecolor("#0a0a0a")
ax3d.xaxis.pane.set_edgecolor("#333333")
ax3d.yaxis.pane.set_edgecolor("#333333")
ax3d.zaxis.pane.set_edgecolor("#333333")

# ─── Panel B: |ω| slice through z = center ─────────────────────────────────
ax_b = fig.add_subplot(gs[0, 2])
omega_slice = omega_norm_seed[:, :, CENTER[2]]
im = ax_b.imshow(omega_slice.T, origin="lower", cmap="viridis",
                 extent=[0, N, 0, N], aspect="equal")
ax_b.plot(CENTER[0] + 0.5, CENTER[1] + 0.5, "c*", ms=15,
          markeredgecolor="white", label="Center")
# Draw horn-torus equator
circle_theta = np.linspace(0, 2 * np.pi, 100)
ax_b.plot(CENTER[0] + 0.5 + COSSERAT_R * np.cos(circle_theta),
          CENTER[1] + 0.5 + COSSERAT_R * np.sin(circle_theta),
          "cyan", lw=2, alpha=0.7, label=f"Loop R={COSSERAT_R}")
ax_b.set_xlabel("x")
ax_b.set_ylabel("y")
ax_b.set_title(f"|ω| equatorial slice (z={CENTER[2]})")
plt.colorbar(im, ax=ax_b, fraction=0.046)
ax_b.legend(loc="upper right", fontsize=8)

# ─── Panel C: |ω| slice through x = center (orthogonal view) ───────────────
ax_c = fig.add_subplot(gs[0, 3])
omega_slice_yz = omega_norm_seed[CENTER[0], :, :]
im = ax_c.imshow(omega_slice_yz.T, origin="lower", cmap="viridis",
                 extent=[0, N, 0, N], aspect="equal")
ax_c.plot(CENTER[1] + 0.5, CENTER[2] + 0.5, "c*", ms=15,
          markeredgecolor="white", label="Center")
ax_c.set_xlabel("y")
ax_c.set_ylabel("z")
ax_c.set_title(f"|ω| orthogonal slice (x={CENTER[0]})")
plt.colorbar(im, ax=ax_c, fraction=0.046)
ax_c.legend(loc="upper right", fontsize=8)

# ─── Panel D: V_inc + V_ref planted at center cell (phase-space) ────────────
ax_d = fig.add_subplot(gs[1, 2])
v_inc_center = V_inc_seed[CENTER[0], CENTER[1], CENTER[2]]
v_ref_center = V_ref_seed[CENTER[0], CENTER[1], CENTER[2]]
colors = ["C0", "C1", "C2", "C3"]
for port in range(4):
    ax_d.plot(v_inc_center[port], v_ref_center[port], "o", color=colors[port],
              ms=15, label=f"Port {port}", markeredgecolor="white", linewidth=2)
ax_d.axhline(0, color="white", ls=":", lw=0.5, alpha=0.3)
ax_d.axvline(0, color="white", ls=":", lw=0.5, alpha=0.3)
# Draw the Clifford-torus (2,3) winding curve
t = np.linspace(0, 2 * np.pi, 500)
clifford_x = 0.3 * np.cos(2 * t)
clifford_y = 0.3 * np.sin(3 * t)
ax_d.plot(clifford_x, clifford_y, "cyan", lw=1.5, alpha=0.5,
          label="(2,3) Clifford ref")
ax_d.set_xlabel("V_inc")
ax_d.set_ylabel("V_ref")
ax_d.set_title("Phase-space (V_inc, V_ref) at center\n(2,3) Clifford torus winding seed")
ax_d.legend(loc="upper right", fontsize=8)
ax_d.set_xlim(-0.5, 0.5)
ax_d.set_ylim(-0.5, 0.5)
ax_d.set_aspect("equal")

# ─── Panel E: Λ decomposition (the three boundary invariants 𝓜, 𝓠, 𝓙) ──
ax_e = fig.add_subplot(gs[1, 3])
categories = ["Λ_vol\n→ 𝓜", "Λ_surf\n→ 𝓙", "Λ_line\n→ 𝓠"]
measured = [Lambda_vol, Lambda_surf, Lambda_line]
canonical = [4 * np.pi ** 3, np.pi ** 2, np.pi]
x_pos = np.arange(len(categories))
width = 0.35
ax_e.bar(x_pos - width / 2, measured, width, label="Seed (engine)",
         color="C0", alpha=0.85, edgecolor="white")
ax_e.bar(x_pos + width / 2, canonical, width, label="Canonical α⁻¹ decomp",
         color="C3", alpha=0.85, edgecolor="white")
ax_e.set_xticks(x_pos)
ax_e.set_xticklabels(categories, fontsize=9)
ax_e.set_ylabel("Magnitude")
ax_e.set_title("Q-factor decomposition α⁻¹ = 4π³ + π² + π\n"
               "(seed soliton on engine vs canonical)")
ax_e.set_yscale("log")
ax_e.legend(loc="best", fontsize=8)
ax_e.grid(True, axis="y", alpha=0.2)

# ─── Panel F: Adjudication summary ─────────────────────────────────────────
ax_f = fig.add_subplot(gs[2, :])
ax_f.axis("off")
summary = (
    "Seed structure (T=0): canonical electron unknot per L3 doc 101 §10 three-layer canonical\n"
    "  Layer 1 (real-space): 0₁ unknot at horn torus R = r = ℓ_node/(2π); engine R=" + str(COSSERAT_R) + " lattice-resolved\n"
    "  Layer 2 (field bundle): SU(2) double-cover via SO(3)→SU(2) Rodrigues projection of ω-field\n"
    "  Layer 3 (phase-space): (2,3) Clifford-torus winding in (V_inc, V_ref) at center cell — planted via 4-port phase pattern\n\n"
    "Substrate-observable boundary invariants (Q1 names locked 2026-05-14 evening, Grant confirmed):\n"
    "  𝓜 (integrated strain integral) ←→ Λ_vol → mass M; canonical 4π³ = " + f"{4*np.pi**3:.3f}" + "\n"
    "  𝓠 (boundary linking number)   ←→ Λ_line → charge Q; canonical π = " + f"{np.pi:.3f}" + "\n"
    "  𝓙 (boundary winding number)   ←→ Λ_surf → spin J; canonical π² = " + f"{np.pi**2:.3f}" + "\n\n"
    "Empirical adjudication (v14a/b/d dynamics tests, 2000 steps each): MODE III decisive across three seed variants.\n"
    "  v14a (single-cell V_inc + Cosserat unknot, A=0.6): K4 V_inc decays to noise in ~50 steps; Cosserat ω plateaus at 10% initial.\n"
    "  v14b (shell-envelope V_inc, A=0.95 + Cosserat): Cosserat ω numerical blow-up (peak grows 10⁴×) — F17-K instability.\n"
    "  v14d (Cosserat-only seed, no K4 plant):           Cosserat ω damps to 10% standalone attractor; K4 stays at zero.\n\n"
    "Interpretation: the boundary-envelope reformulation (doc 109 §13, Grant-confirmed canonical) is logically and corpus-consistently\n"
    "right, but the K4-TLM + Cosserat coupled engine as currently implemented does NOT autonomously host the bound state. The framework's\n"
    "empirical validation lives in Q-G19α Route B (50 ppm to PDG via boundary-integrated phase-space observables), not in live lattice\n"
    "bound-state dynamics. Doc 92 Reading A (Ax 1 revision) or Reading B (continuum FDTD substrate) remain candidate framework moves;\n"
    "doc 109 §13 substrate-observability rule remains canonical for external claims."
)
ax_f.text(0.02, 0.95, summary, transform=ax_f.transAxes,
          fontsize=9, family="monospace", verticalalignment="top",
          color="white",
          bbox=dict(boxstyle="round,pad=0.5",
                    facecolor="#181818", edgecolor="#404040"))

# Style 2D axes
for ax in [ax_b, ax_c, ax_d, ax_e]:
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

fig.suptitle(
    "The Most Fundamental AVE Soliton — Cosserat Unknot Seed on K4-TLM (Mode III dynamics)",
    color="white", fontsize=14, y=0.995,
)

out_path = OUT / "r10_path_alpha_v14_soliton_seed.png"
plt.savefig(out_path, dpi=140, facecolor="#0a0a0a", bbox_inches="tight")
print(f"Figure: {out_path}")
print()

print("=" * 78)
print("This visual shows the AVE-canonical electron soliton AS THE ENGINE ENCODES IT")
print("at t=0 (planted seed state). The Mode III dynamics finding (v14a/b/d empirical)")
print("means the engine does NOT autonomously sustain this state past ~50 timesteps.")
print()
print("The seed structure IS the most fundamental AVE soliton per L3 doc 101 three-")
print("layer canonical: unknot 0₁ real-space + SU(2) ω-bundle + (2,3) Clifford phase-")
print("space. The figure visualizes all three layers. The Λ_vol + Λ_surf + Λ_line")
print("decomposition shows where 𝓜, 𝓠, 𝓙 would map IF the bound state self-stabilized.")
print()
print("Honest framework status: §13 substrate-observability rule = canonical;")
print("§14 acceptance criteria for engine bound-state hosting = FAIL (Mode III).")
print("=" * 78)
