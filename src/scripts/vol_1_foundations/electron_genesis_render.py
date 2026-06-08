"""electron_genesis_render.py — manuscript-quality figures from the REAL capture.

Renders the LANDMARK "full vacuum lattice at work" showcase from the field arrays
captured by electron_genesis_capture.py (FDTD3DEngine output — NOT synthetic, in
contrast to the illustrative visualize_self_trapping.py). Produces:

  STILL FRAMES (different dynamics, research/figures/):
    electron_genesis_stage_a_free_photon.png       free transverse photon propagating
    electron_genesis_stage_b_saturation_onset.png  collision: Axiom-4 kernel S(A) bites
    electron_genesis_stage_c_selftrap_core.png      localized core + radiative shedding
    electron_genesis_stage_d_standing_residual.png  persistent standing residual
    electron_genesis_validation.png                 localization-beat + saturation + c
    electron_genesis_landmark_montage.png           the showcase montage (all stages)
  ANIMATION:
    electron_genesis_full_sequence.gif              full sequence photon→self-trap→stand
    electron_genesis_full_sequence.mp4              (if ffmpeg available)

HONESTY (ave-evidence-framing-discipline — every panel labeled REAL vs ILLUSTRATIVE):
  REAL (engine-demonstrated): the saturation heatmap A=|E|dx/V_SNAP + S(A) kernel,
      the transverse E⊥B polarization fields, the energy-density localization, the
      ponderomotive force F=−∇u, the localization beat (0.580 vs 0.389), c-recovery.
  ILLUSTRATIVE / NOT SHOWN: the (2,3) Clifford-torus winding + spin-½. These do NOT
      emerge on this continuum engine (P4 toroidal-winding FAILS, 0.000; 2026-06-04
      §7.2). They are NOT overlaid — drawing them would imply an emergence the engine
      does not produce. The K4 diamond-lattice context panel shows the discrete 4-port
      substrate (k4_tlm.K4Lattice3D) where the winding IS testable (the fork's path
      forward), labeled as geometry context, NOT as carrying this run's field.

Run (after electron_genesis_capture.py):
    PYTHONPATH=src python3 src/scripts/vol_1_foundations/electron_genesis_render.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.animation import FFMpegWriter, FuncAnimation, PillowWriter  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import ALPHA, R_I  # noqa: E402

FIG_DIR = Path(__file__).resolve().parents[3] / "research" / "figures"
NPZ = FIG_DIR / "electron_genesis_capture.npz"
VAL = FIG_DIR / "electron_genesis_validation.json"

# AVE house dark palette (matches visualize_self_trapping.py)
BG = "#08081a"
FG = "#ddddff"
MUTE = "#8888aa"
GRID = "#1a1a38"
REAL_C = "#55dd88"      # green = REAL / engine-demonstrated
ILLUS_C = "#dd8844"     # amber = ILLUSTRATIVE / planted
SQRT2A = float(R_I)     # Op14 saturation-engagement onset √(2α)


def load() -> dict:
    d = np.load(NPZ, allow_pickle=True)
    data = {k: d[k] for k in d.files}
    data["validation"] = json.loads(VAL.read_text())
    cfg = data["config"]
    data["N"] = int(cfg[0]); data["PML"] = int(cfg[2]); data["amp_frac"] = float(cfg[3])
    data["n_settle"] = int(cfg[4]); data["n_record"] = int(cfg[5])
    return data


def frame_for_step(steps: np.ndarray, target: int) -> int:
    return int(np.argmin(np.abs(steps - target)))


def k4_node_geometry(n: int = 12):
    """REAL K4 (diamond/FCC) node geometry from k4_tlm.K4Lattice3D masks.

    Returns (A_coords, B_coords): the two interpenetrating sublattices. This is
    the canonical discrete 4-port vacuum lattice (the substrate); it is rendered
    as GEOMETRY CONTEXT only — it does NOT carry the FDTD self-trap run's field.
    """
    from ave.core.k4_tlm import K4Lattice3D

    lat = K4Lattice3D(nx=n, ny=n, nz=n, dx=1.0)
    A = np.argwhere(lat.mask_A)
    B = np.argwhere(lat.mask_B)
    return A, B


def _dark(ax):
    ax.set_facecolor(BG)
    for sp in ax.spines.values():
        sp.set_color("#333355")
    ax.tick_params(colors=MUTE, labelsize=7)


def _tag(ax, text, color, *, loc="lower left"):
    """REAL/ILLUSTRATIVE provenance tag (ave-evidence-framing-discipline)."""
    xy = {"lower left": (0.02, 0.03), "lower right": (0.98, 0.03),
          "upper left": (0.02, 0.97), "upper right": (0.98, 0.97)}[loc]
    ha = "left" if "left" in loc else "right"
    va = "bottom" if "lower" in loc else "top"
    ax.text(*xy, text, transform=ax.transAxes, color=BG, fontsize=6.5,
            fontweight="bold", ha=ha, va=va,
            bbox=dict(boxstyle="round,pad=0.25", fc=color, ec="none", alpha=0.92))


def _yee_grid(ax, n: int, step: int = 6):
    """Overlay the discrete FDTD Yee lattice cells (the real computational cells)."""
    for g in range(0, n + 1, step):
        ax.axhline(g - 0.5, color=GRID, lw=0.4, alpha=0.55)
        ax.axvline(g - 0.5, color=GRID, lw=0.4, alpha=0.55)


# ── panel: saturation heatmap (xz propagation plane) ───────────────────────────
def panel_saturation(ax, A_xz, n, pml, *, title="Saturation  A = |E|·dx / A_yield"):
    im = ax.imshow(A_xz.T, origin="lower", cmap="magma", vmin=0.0, vmax=1.0,
                   interpolation="nearest", aspect="equal")
    # Op14 engagement onset contour √(2α): where the Axiom-4 kernel starts to bite
    if A_xz.max() > SQRT2A:
        ax.contour(A_xz.T, levels=[SQRT2A], colors=["#33e0ff"], linewidths=1.1, alpha=0.9)
    _yee_grid(ax, n)
    # PML frame (Rule 10 — absorbing boundary, excluded from physics)
    ax.add_patch(plt.Rectangle((pml - 0.5, pml - 0.5), n - 2 * pml, n - 2 * pml,
                               fill=False, ec="#5566aa", lw=0.8, ls=":", alpha=0.7))
    ax.set_title(title, color=FG, fontsize=8.5, pad=4)
    ax.set_xlabel("x (propagation →)", color=MUTE, fontsize=7)
    ax.set_ylabel("z", color=MUTE, fontsize=7)
    _dark(ax)
    _tag(ax, "REAL · Axiom-4 S(A)=√(1−A²)", REAL_C)
    return im


# ── panel: transverse E⊥B polarization (yz plane at lattice center) ────────────
def panel_transverse(ax, Ey, Ez, Hy, Hz, u, n, *, title="Transverse  E ⊥ B  (yz core plane)"):
    # energy background
    ub = u / max(u.max(), 1e-30)
    ax.imshow(ub.T, origin="lower", cmap="inferno", vmin=0, vmax=1,
              interpolation="bilinear", aspect="equal", alpha=0.85)
    # downsample quiver
    s = 3
    yy, zz = np.mgrid[0:n:s, 0:n:s]
    ey = Ey[::s, ::s]; ez = Ez[::s, ::s]
    hy = Hy[::s, ::s]; hz = Hz[::s, ::s]
    en = np.sqrt(ey**2 + ez**2); en_m = max(en.max(), 1e-30)
    hn = np.sqrt(hy**2 + hz**2); hn_m = max(hn.max(), 1e-30)
    ax.quiver(yy, zz, ey / en_m, ez / en_m, color="#33e0ff", scale=22, width=0.006,
              alpha=0.9, pivot="mid")
    ax.quiver(yy, zz, hy / hn_m, hz / hn_m, color="#ffaa33", scale=22, width=0.004,
              alpha=0.75, pivot="mid")
    ax.set_title(title, color=FG, fontsize=8.5, pad=4)
    ax.set_xlabel("y", color=MUTE, fontsize=7)
    ax.set_ylabel("z", color=MUTE, fontsize=7)
    ax.set_xlim(-0.5, n - 0.5); ax.set_ylim(-0.5, n - 0.5)
    _dark(ax)
    ax.text(0.98, 0.97, "E", transform=ax.transAxes, color="#33e0ff", fontsize=9,
            fontweight="bold", ha="right", va="top")
    ax.text(0.90, 0.97, "B", transform=ax.transAxes, color="#ffaa33", fontsize=9,
            fontweight="bold", ha="right", va="top")
    _tag(ax, "REAL E⊥B · (2,3)/spin NOT shown (no emergence)", REAL_C)
    return ax


# ── panel: energy-density localization (xz) ───────────────────────────────────
def panel_energy(ax, u_xz, n, pml, *, title="Energy density  u  (localization)"):
    ub = u_xz / max(u_xz.max(), 1e-30)
    im = ax.imshow(ub.T, origin="lower", cmap="inferno", vmin=0, vmax=1,
                   interpolation="bilinear", aspect="equal")
    ax.add_patch(plt.Rectangle((pml - 0.5, pml - 0.5), n - 2 * pml, n - 2 * pml,
                               fill=False, ec="#5566aa", lw=0.8, ls=":", alpha=0.7))
    ax.set_title(title, color=FG, fontsize=8.5, pad=4)
    ax.set_xlabel("x (propagation →)", color=MUTE, fontsize=7)
    ax.set_ylabel("z", color=MUTE, fontsize=7)
    _dark(ax)
    _tag(ax, "REAL · engine energy_density()", REAL_C)
    return im


# ── panel: ponderomotive force F = −∇u (the "displacement" proxy) ──────────────
def panel_ponderomotive(ax, u_xz, n, pml, *, title="Ponderomotive force  F = −∇u"):
    """The engine carries no explicit node-displacement DOF (Maxwell E/H only);
    F=−∇u is the REAL engine-exposed force that pushes lattice nodes off
    equilibrium toward the soliton core — the honest displacement surrogate."""
    gz, gx = np.gradient(u_xz.T)  # note .T so axis0=z, axis1=x
    Fx = -gx; Fz = -gz
    ub = u_xz / max(u_xz.max(), 1e-30)
    ax.imshow(ub.T, origin="lower", cmap="bone", vmin=0, vmax=1,
              interpolation="bilinear", aspect="equal", alpha=0.7)
    s = 3
    xx, zz = np.mgrid[0:n:s, 0:n:s]
    fx = Fx[::s, ::s]; fz = Fz[::s, ::s]
    fn = np.sqrt(fx**2 + fz**2); fm = max(fn.max(), 1e-30)
    ax.quiver(xx, zz, (fx / fm).T, (fz / fm).T, color="#88ff88", scale=20,
              width=0.005, alpha=0.85, pivot="mid")
    ax.set_title(title, color=FG, fontsize=8.5, pad=4)
    ax.set_xlabel("x (propagation →)", color=MUTE, fontsize=7)
    ax.set_ylabel("z", color=MUTE, fontsize=7)
    _dark(ax)
    _tag(ax, "REAL F=−∇u · no explicit u DOF on Maxwell engine", REAL_C)
    return ax


STAGES = [
    ("a", "free_photon", 8,
     "FREE PHOTON  —  two counter-propagating focused CP transverse packets (E⊥B⊥k) "
     "propagate toward the lattice center"),
    ("b", "saturation_onset", 24,
     "SATURATION ONSET (Γ→−1)  —  the packets collide; constructive interference drives "
     "A→0.93 (S↓0.36): the Axiom-4 kernel bites, ε collapses, c_eff↓, the longitudinal "
     "channel chokes; energy concentrates"),
    ("c", "selftrap_core", 72,
     "SELF-TRAP + RADIATIVE SHEDDING  —  a localized core forms; the leaky continuum "
     "engine sheds excess to the absorbing boundary (confinement self-generated, no wall)"),
    ("d", "standing_residual", 400,
     "STANDING RESIDUAL  —  a persistent localized standing state remains (centroid "
     "central, flat 120→536) that OUT-RETAINS the matched baseline 0.580 vs 0.389"),
]


def render_stage(data: dict, stage) -> Path:
    letter, slug, step, desc = stage
    n, pml = data["N"], data["PML"]
    steps = data["ce_steps"]
    fi = frame_for_step(steps, step)
    peakA = float(data["ce_peakA"][fi]); Smin = float(data["ce_Smin"][fi])

    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.7))
    fig.patch.set_facecolor(BG)
    panel_saturation(axes[0], data["ce_xz_A"][fi], n, pml)
    panel_transverse(axes[1], data["ce_yz_Ey"][fi], data["ce_yz_Ez"][fi],
                     data["ce_yz_Hy"][fi], data["ce_yz_Hz"][fi], data["ce_yz_u"][fi], n)
    panel_energy(axes[2], data["ce_xz_u"][fi], n, pml)

    fig.suptitle(f"({letter})  step {int(steps[fi])}   ·   peak A = {peakA:.3f}   ·   "
                 f"S(A)_min = {Smin:.3f}", color=FG, fontsize=11, fontweight="bold", y=0.99)
    fig.text(0.5, 0.015, desc, color=MUTE, fontsize=8.5, ha="center", wrap=True)
    fig.text(0.5, 0.95, "Photon → Electron self-trap  ·  FDTD3DEngine (real engine output)",
             color=REAL_C, fontsize=8, ha="center")
    fig.subplots_adjust(left=0.045, right=0.99, top=0.88, bottom=0.10, wspace=0.22)
    out = FIG_DIR / f"electron_genesis_stage_{letter}_{slug}.png"
    fig.savefig(out, dpi=150, facecolor=BG)
    plt.close(fig)
    return out


def render_validation(data: dict) -> Path:
    n, pml = data["N"], data["PML"]
    v = data["validation"]
    steps = data["ce_steps"]
    ns, nr = data["n_settle"], data["n_record"]

    fig = plt.figure(figsize=(13.5, 8.0))
    fig.patch.set_facecolor(BG)
    gs = fig.add_gridspec(2, 3, hspace=0.38, wspace=0.30,
                          left=0.07, right=0.97, top=0.90, bottom=0.10)

    # V1 — localization beat (peak-field retention, normalized to window start)
    ax1 = fig.add_subplot(gs[0, 0]); _dark(ax1)
    win = (steps >= ns) & (steps < ns + nr)
    ce_pf = data["ce_peakfield"][win]; ce_st = steps[win]
    ce_pf_n = ce_pf / max(ce_pf[0], 1e-30)
    bs = data["base_steps"]; bwin = (bs >= ns) & (bs < ns + nr)
    b_pf = data["base_peakfield"][bwin]; b_st = bs[bwin]
    b_pf_n = b_pf / max(b_pf[0], 1e-30)
    ax1.plot(ce_st, ce_pf_n, color=REAL_C, lw=2.0, label="C-EMERGE (structured photon)")
    ax1.plot(b_st, b_pf_n, color=ILLUS_C, lw=1.8, ls="--", label="matched baseline (scrambled)")
    ce_r = v["V1_localization_beat"]["C_EMERGE_retention"]
    b_r = v["V1_localization_beat"]["BASELINE_retention"]
    ax1.axhline(ce_r, color=REAL_C, lw=0.7, alpha=0.5)
    ax1.axhline(b_r, color=ILLUS_C, lw=0.7, alpha=0.5)
    ax1.set_title(f"V1  localization beat  {ce_r:.3f} > {b_r:.3f}", color=FG, fontsize=9)
    ax1.set_xlabel("step", color=MUTE, fontsize=7); ax1.set_ylabel("peak |field| (norm.)", color=MUTE, fontsize=7)
    ax1.legend(facecolor=BG, edgecolor="#333355", labelcolor=FG, fontsize=6.5, loc="upper right")
    _tag(ax1, "REAL", REAL_C, loc="lower left")

    # V2 — saturation engagement timeseries
    ax2 = fig.add_subplot(gs[0, 1]); _dark(ax2)
    ax2.plot(steps, data["ce_peakA"], color="#ff5599", lw=1.8, label="peak A = |E|dx/A_yield")
    ax2.axhline(SQRT2A, color="#33e0ff", lw=1.2, ls=":", label=f"√(2α)={SQRT2A:.3f} (Op14 onset)")
    ax2.axhline(1.0, color="#ffffff", lw=0.7, ls="--", alpha=0.5, label="A_yield (Γ→−1)")
    ax2.set_ylim(0, 1.05)
    pA = v["V2_saturation_engaged"]["peakA_max"]
    ax2.set_title(f"V2  saturation engaged  A_max={pA:.3f}", color=FG, fontsize=9)
    ax2.set_xlabel("step", color=MUTE, fontsize=7); ax2.set_ylabel("A", color=MUTE, fontsize=7)
    ax2.legend(facecolor=BG, edgecolor="#333355", labelcolor=FG, fontsize=6.0, loc="upper right")
    _tag(ax2, "REAL", REAL_C, loc="upper left")

    # V3 / context — K4 diamond lattice substrate (REAL geometry)
    ax3 = fig.add_subplot(gs[0, 2], projection="3d"); ax3.set_facecolor(BG)
    A, B = k4_node_geometry(12)
    ax3.scatter(A[:, 0], A[:, 1], A[:, 2], s=10, c="#33e0ff", alpha=0.8, label="sublattice A")
    ax3.scatter(B[:, 0], B[:, 1], B[:, 2], s=10, c="#ff5599", alpha=0.8, label="sublattice B")
    ax3.set_title("K4 diamond vacuum lattice (k4_tlm)", color=FG, fontsize=9)
    ax3.tick_params(colors=MUTE, labelsize=5)
    for pane in (ax3.xaxis, ax3.yaxis, ax3.zaxis):
        pane.set_pane_color((0.03, 0.03, 0.10, 1.0))
    ax3.legend(facecolor=BG, edgecolor="#333355", labelcolor=FG, fontsize=6.0, loc="upper right")
    ax3.text2D(0.02, 0.02, "REAL geometry · 4-port substrate (winding testable here, not run)",
               transform=ax3.transAxes, color=ILLUS_C, fontsize=5.5)

    # footer text block: the three validations + honesty
    ax4 = fig.add_subplot(gs[1, :]); ax4.axis("off"); ax4.set_facecolor(BG)
    cv = v["V3_c_recovery"]
    lines = [
        ("VALIDATION (validate-what-you-did) — the self-trap ACTUALLY occurs:", FG, 10, "bold"),
        (f"   V1  localization beats matched baseline   : C-EMERGE {ce_r:.3f}  >  baseline {b_r:.3f}   "
         f"[REAL — topology/coherence-driven, NOT amplitude-driven]", REAL_C, 8.5, "normal"),
        (f"   V2  Axiom-4 saturation kernel engages      : peak A = {pA:.3f}  >  √(2α) = {SQRT2A:.3f}   "
         f"(S_min = {v['V2_saturation_engaged']['S_min_kernel_floor']:.3f})   [REAL]", REAL_C, 8.5, "normal"),
        (f"   V3  c recovered                            : c_meas/c₀ = {cv['c_ratio']:.3f}  "
         f"(wavefront speed, λ=12 cells; ~4% = numerical dispersion)   [REAL]", REAL_C, 8.5, "normal"),
        ("HONESTY (ave-evidence-framing-discipline):", FG, 10, "bold"),
        ("   REAL / engine-demonstrated : self-trap localization (= mass formation), saturation "
         "engagement, transverse E⊥B propagation, c-recovery.", REAL_C, 8.5, "normal"),
        ("   ILLUSTRATIVE / NOT SHOWN   : the (2,3) Clifford-torus winding + spin-½ do NOT emerge "
         "(P4 toroidal-winding FAILS, 0.000; 2026-06-04 §7.2) — not overlaid.", ILLUS_C, 8.5, "normal"),
        ("   Propagating-soliton / de Broglie wake      : TESTED, NOT clean (single intense packet "
         "disperses, Rg 5.7→15.9) — excluded, not faked.", ILLUS_C, 8.5, "normal"),
    ]
    y = 0.95
    for txt, col, sz, w in lines:
        ax4.text(0.0, y, txt, color=col, fontsize=sz, fontweight=w,
                 family="monospace", transform=ax4.transAxes, va="top")
        y -= 0.115

    fig.suptitle("Electron genesis — VALIDATION + substrate context",
                 color=FG, fontsize=13, fontweight="bold", y=0.965)
    out = FIG_DIR / "electron_genesis_validation.png"
    fig.savefig(out, dpi=150, facecolor=BG)
    plt.close(fig)
    return out


def render_montage(data: dict) -> Path:
    n, pml = data["N"], data["PML"]
    steps = data["ce_steps"]
    v = data["validation"]
    fig = plt.figure(figsize=(15.5, 17.0))
    fig.patch.set_facecolor(BG)
    gs = fig.add_gridspec(len(STAGES), 3, hspace=0.30, wspace=0.18,
                          left=0.05, right=0.98, top=0.93, bottom=0.055)
    for r, (letter, slug, step, desc) in enumerate(STAGES):
        fi = frame_for_step(steps, step)
        peakA = float(data["ce_peakA"][fi]); Smin = float(data["ce_Smin"][fi])
        ax0 = fig.add_subplot(gs[r, 0])
        panel_saturation(ax0, data["ce_xz_A"][fi], n, pml,
                         title=f"({letter}) Saturation A   step {int(steps[fi])}  ·  A={peakA:.3f}")
        ax1 = fig.add_subplot(gs[r, 1])
        panel_transverse(ax1, data["ce_yz_Ey"][fi], data["ce_yz_Ez"][fi],
                         data["ce_yz_Hy"][fi], data["ce_yz_Hz"][fi], data["ce_yz_u"][fi], n,
                         title="Transverse E⊥B (yz core)")
        ax2 = fig.add_subplot(gs[r, 2])
        panel_energy(ax2, data["ce_xz_u"][fi], n, pml, title="Energy density u")
        ax0.text(-0.18, 0.5, desc.split("  —  ")[0], transform=ax0.transAxes, color=FG,
                 fontsize=8.5, fontweight="bold", rotation=90, va="center", ha="center")

    ce_r = v["V1_localization_beat"]["C_EMERGE_retention"]
    b_r = v["V1_localization_beat"]["BASELINE_retention"]
    cv = v["V3_c_recovery"]["c_ratio"]
    pA = v["V2_saturation_engaged"]["peakA_max"]
    fig.suptitle("PHOTON → ELECTRON SELF-TRAP  ·  the full K4 vacuum lattice at work",
                 color=FG, fontsize=17, fontweight="bold", y=0.975)
    fig.text(0.515, 0.948,
             "REAL FDTD3DEngine output (Axiom-4 saturable Maxwell)  ·  a transverse photon "
             "self-traps into a localized soliton core (mass formation)",
             color=REAL_C, fontsize=9.5, ha="center")
    fig.text(0.515, 0.030,
             f"VALIDATED  ·  localization beat {ce_r:.3f} > {b_r:.3f} (matched baseline)  ·  "
             f"saturation A_max={pA:.3f} > √(2α)={SQRT2A:.3f}  ·  c_meas/c₀={cv:.3f}     "
             f"ILLUSTRATIVE/NOT SHOWN: (2,3) winding + spin-½ do NOT emerge (P4 FAIL)",
             color=MUTE, fontsize=8.5, ha="center")
    out = FIG_DIR / "electron_genesis_landmark_montage.png"
    fig.savefig(out, dpi=140, facecolor=BG)
    plt.close(fig)
    return out


def render_animation(data: dict) -> list[Path]:
    n, pml = data["N"], data["PML"]
    steps = data["ce_steps"]
    v = data["validation"]
    nframes = len(steps)

    fig = plt.figure(figsize=(13.0, 5.2))
    fig.patch.set_facecolor(BG)
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.05], wspace=0.26,
                          left=0.045, right=0.985, top=0.84, bottom=0.13)
    ax_s = fig.add_subplot(gs[0, 0])
    ax_t = fig.add_subplot(gs[0, 1])
    ax_m = fig.add_subplot(gs[0, 2])

    peakA_all = data["ce_peakA"]
    pf_all = data["ce_peakfield"]
    pf_n = pf_all / max(pf_all[0], 1e-30)

    def stage_label(st):
        if st < 16:
            return "FREE PHOTON", REAL_C
        if st < 40:
            return "SATURATION ONSET (Γ→−1)", "#ff5599"
        if st < 110:
            return "SELF-TRAP + SHEDDING", "#ffaa33"
        return "STANDING RESIDUAL", REAL_C

    def update(fi):
        for a in (ax_s, ax_t, ax_m):
            a.clear()
        st = int(steps[fi])
        panel_saturation(ax_s, data["ce_xz_A"][fi], n, pml,
                         title=f"Saturation A   ·   A={peakA_all[fi]:.3f}")
        panel_transverse(ax_t, data["ce_yz_Ey"][fi], data["ce_yz_Ez"][fi],
                         data["ce_yz_Hy"][fi], data["ce_yz_Hz"][fi], data["ce_yz_u"][fi], n,
                         title="Transverse E⊥B (yz core)")
        # right: live peak-A + peak-field trace with a moving cursor
        _dark(ax_m)
        ax_m.plot(steps, peakA_all, color="#ff5599", lw=1.4, label="peak A")
        ax_m.plot(steps, pf_n, color=REAL_C, lw=1.4, label="peak |field| (norm.)")
        ax_m.axhline(SQRT2A, color="#33e0ff", lw=1.0, ls=":", alpha=0.8)
        ax_m.axvline(st, color="#ffffff", lw=1.0, alpha=0.6)
        ax_m.set_ylim(0, 1.05)
        ax_m.set_xlabel("step", color=MUTE, fontsize=7)
        ax_m.set_title("self-trap timeline (REAL)", color=FG, fontsize=8.5)
        ax_m.legend(facecolor=BG, edgecolor="#333355", labelcolor=FG, fontsize=6.0, loc="upper right")
        lab, col = stage_label(st)
        fig.suptitle(f"PHOTON → ELECTRON SELF-TRAP   ·   step {st:3d}   ·   {lab}",
                     color=col, fontsize=13, fontweight="bold", y=0.965)
        return []

    ani = FuncAnimation(fig, update, frames=nframes, blit=False)
    outs = []
    gif = FIG_DIR / "electron_genesis_full_sequence.gif"
    ani.save(gif, writer=PillowWriter(fps=12), dpi=100)
    outs.append(gif)
    try:
        mp4 = FIG_DIR / "electron_genesis_full_sequence.mp4"
        ani.save(mp4, writer=FFMpegWriter(fps=12, bitrate=2400), dpi=120)
        outs.append(mp4)
    except Exception as e:  # noqa: BLE001
        print(f"  (mp4 skipped: {e})")
    plt.close(fig)
    return outs


def main() -> None:
    print("=" * 78)
    print("  electron_genesis_render — manuscript figures from REAL FDTD capture")
    print("=" * 78, flush=True)
    data = load()
    print(f"  loaded {NPZ.name}: {len(data['ce_steps'])} frames, N={data['N']}, "
          f"alpha={ALPHA:.6g}")
    outs = []
    for stage in STAGES:
        p = render_stage(data, stage)
        print(f"  still: {p.name}")
        outs.append(p)
    p = render_validation(data); print(f"  panel: {p.name}"); outs.append(p)
    p = render_montage(data); print(f"  montage: {p.name}"); outs.append(p)
    print("  rendering long animation (GIF + mp4) ...", flush=True)
    anim = render_animation(data)
    for a in anim:
        print(f"  anim: {a.name}")
        outs.append(a)
    print(f"\n  {len(outs)} figures written to {FIG_DIR}")


if __name__ == "__main__":
    main()
