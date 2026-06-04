#!/usr/bin/env python3
r"""
Double-Slit Dark-Wake on the K4-TLM Substrate (Option (i): imposed trajectory).
================================================================================

A moving localized transverse source traces an electron-defect trajectory toward
a two-slit wall. Its REAL K4-TLM transverse wake (the radiated V-sector field)
spreads and passes through BOTH slits, producing real-space interference on a
downstream screen plane. Two animated panels, side by side:

  Panel A -- no observer:   coherent wake through both slits -> |E|^2 fringes.
  Panel B -- observer:      a local Ohmic / Gamma-mismatch impedance load (Z_det)
                            at slit 2 thermalizes the wake throughput there, so
                            the screen pattern collapses toward the single-slit
                            diffraction envelope -> fringe visibility drops
                            CONTINUOUSLY (dark-wake / Born, not Copenhagen-binary).

HONEST FRAMING (load-bearing; printed on the figure and in the result doc)
--------------------------------------------------------------------------
Dark-wake mechanism on the K4-TLM substrate; the defect TRAJECTORY is imposed;
the transverse wake, the interference fringes, and the Gamma-mismatch which-path
decoherence are real engine physics. This is NOT a from-scratch emergent or
free-propagating electron (that is the separate option-(ii) probe), and the
moving object is NOT a "helical photon" (that dual-sector framing is retracted at
manuscript/ave-kb/.../ch4-continuum-electrodynamics/photon-identification.md).
CP5: the trajectory is imposed BECAUSE a Gamma=-1 self-trapped core has
c_local -> 0 and cannot free-propagate -- that is the option-(ii) question.

Canonical mechanism leaf:
  manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md
  (defect through one slit; transverse wake through both; Ohmic detector at slit 2
   thermalizes phase energy -> decoherence; Born rule
   P(click|x) = |dt A(x)|^2 / integral |dt A|^2).
Consolidated EE leaves double-slit-ee-mapping.md + photon-ee-mapping.md are on
PR #85 (NOT yet on main) -- cited by canonical path, pending-merge.

SUBSTRATE-NATIVE compliance (substrate-native-check)
----------------------------------------------------
- K4-TLM scatter+connect (engine.step() IS the computation), V-sector.
- amp = 0.05*V_SNAP < V_YIELD  -> Axiom 4 saturation dormant (linear vacuum).
- Slit wall = deactivated cells (perfect reflector), not a continuum boundary.
- PML cells EXCLUDED from screen/intensity sampling (CP7).
- Screen observable = real-space |E|^2 = sum_ports (V_inc + V_ref)^2 (CP4); the
  phase-space (2,3) ansatz stays OUT.
- E ~ (V_inc + V_ref), B ~ (V_inc - V_ref)/Z; |dt A|^2 ~ |E|^2 per the canonical
  Lagrangian L = 1/2 eps0 |dt A|^2 - 1/(2 mu0) |curl A|^2.

ave-canonical-source: Z_0, ALPHA, V_YIELD, V_SNAP, C_0, L_NODE all imported from
ave.core.constants; carrier omega tied to the lattice cell pitch (NOT a hardcoded
freq); a verify_constants() cross-check runs before any plotting.

ave-driver-script-honesty: the fringe spacing is FORWARD-PREDICTED from the wake
wavelength + slit geometry (Fraunhofer Delta_y = lambda*L/d) and reported against
the observed value; no fit-to-target, no print-vs-compute mismatch.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.animation import FFMpegWriter, FuncAnimation, PillowWriter  # noqa: E402

from ave.core.constants import ALPHA, C_0, L_NODE, V_SNAP, V_YIELD, Z_0  # noqa: E402
from ave.core.k4_tlm import K4Lattice3D  # noqa: E402

try:
    from ave_path_util import SIM_OUTPUTS
except ImportError:  # pragma: no cover - path fallback when run outside src/
    from pathlib import Path

    SIM_OUTPUTS = Path(__file__).resolve().parents[3] / "assets" / "sim_outputs"


# ─────────────────────────────────────────────────────────────────────────────
# Locked configuration (see _orchestration/double-slit-ave-sim.md STEP-0)
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class DSConfig:
    NX: int = 200
    NY: int = 140
    NZ: int = 24  # >= 2*PML + interior band (isotropic PML constraint)
    PML: int = 8
    wall_x: int = 80
    wall_thick: int = 3
    slit_sep: int = 30
    slit_w: int = 3
    x_src: int = 16
    lambda_cells: float = 8.0  # wake cell-pitch carrier wavelength
    amp_frac_vsnap: float = 0.05  # 0.05*V_SNAP = 25.55 kV < V_YIELD = 43.65 kV
    n_steps: int = 600
    record_from_frac: float = 0.5  # time-average over the second half
    z_band: int = 3  # sample/inject over zc-z_band .. zc+z_band
    Z_det: float = 0.9  # observer Ohmic-load strength (Panel B)
    screen_offset: int = 12  # screen at NX - PML - screen_offset

    @property
    def zc(self) -> int:
        return self.NZ // 2

    @property
    def s1(self) -> int:
        return self.NY // 2 - self.slit_sep // 2

    @property
    def s2(self) -> int:
        return self.NY // 2 + self.slit_sep // 2

    @property
    def src_y(self) -> int:
        return self.NY // 2

    @property
    def screen_x(self) -> int:
        return self.NX - self.PML - self.screen_offset

    @property
    def amp(self) -> float:
        return self.amp_frac_vsnap * float(V_SNAP)

    @property
    def L(self) -> int:
        """Slit-plane-to-screen distance in cells (for Fraunhofer prediction)."""
        return self.screen_x - self.wall_x

    def predicted_fringe_spacing(self) -> float:
        """Fraunhofer (small-angle) two-slit spacing Delta_y = lambda * L / d."""
        return self.lambda_cells * self.L / self.slit_sep


def verify_constants(cfg: DSConfig) -> dict:
    """ave-canonical-source / ave-driver-script-honesty cross-check.

    Runs BEFORE any simulation or plotting. Confirms the canonical constants are
    self-consistent and that the drive amplitude keeps Axiom 4 dormant
    (linear vacuum), so the wake is a genuine small-signal transverse field.
    """
    assert 376.0 < Z_0 < 377.0, f"Z_0 out of range: {Z_0}"
    assert V_YIELD < V_SNAP, f"V_YIELD ({V_YIELD}) must be < V_SNAP ({V_SNAP})"
    assert abs(V_YIELD - np.sqrt(ALPHA) * V_SNAP) < 1.0, "V_YIELD != sqrt(alpha)*V_SNAP"
    assert cfg.amp < V_YIELD, (
        f"drive amp {cfg.amp:.0f} V must be < V_YIELD {V_YIELD:.0f} V "
        f"(Axiom 4 must stay dormant -> linear vacuum)"
    )
    return {
        "Z_0_ohm": float(Z_0),
        "ALPHA": float(ALPHA),
        "V_YIELD_V": float(V_YIELD),
        "V_SNAP_V": float(V_SNAP),
        "L_NODE_m": float(L_NODE),
        "C_0_mps": float(C_0),
        "drive_amp_V": float(cfg.amp),
        "drive_amp_over_V_YIELD": float(cfg.amp / V_YIELD),
        "axiom4_dormant": bool(cfg.amp < V_YIELD),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Port geometry (A->B vectors); used only for diagnostics / optional T2 launch.
# ─────────────────────────────────────────────────────────────────────────────
PORT_VECS = np.array(
    [[+1, +1, +1], [+1, -1, -1], [-1, +1, -1], [-1, -1, +1]], dtype=float
)
PORT_HAT = PORT_VECS / np.sqrt(3.0)


@dataclass
class RunResult:
    """Container for one engine run's recorded fields."""

    energy_map: np.ndarray  # (NX, NY) time-averaged |E|^2 over z-band
    frames: list = field(default_factory=list)  # per-frame (NX, NY) |E|^2 maps
    frame_steps: list = field(default_factory=list)
    visibility: float = float("nan")
    screen_profile: np.ndarray = None  # coarse-grained y-profile at screen
    screen_y: np.ndarray = None
    peak_ys: np.ndarray = None
    observed_spacing: float = float("nan")
    marker_xy: list = field(default_factory=list)  # imposed-trajectory marker (x,y) per frame


def imposed_trajectory(cfg: DSConfig, frac: float) -> tuple[float, float]:
    """Imposed (DEPICTED, not dynamical) defect trajectory through slit 1.

    The marker travels along the central axis toward the wall, bends into slit 1,
    and continues downstream -- the deterministic-navigation picture of the
    canonical leaf (the particle "navigates the transverse ponderomotive gradients
    into the quantized standing-wave troughs"). This is an animation OVERLAY only;
    it does NOT drive the engine (the wake field is emitted from a stable upstream
    point so both slits stay symmetrically illuminated -> clean Young fringes).
    """
    x_enter = cfg.wall_x + cfg.wall_thick / 2.0
    x_end = cfg.screen_x
    if frac <= 0.5:
        # approach: x_src -> slit-1 x, y on axis -> slit 1
        f = frac / 0.5
        x = cfg.x_src + f * (x_enter - cfg.x_src)
        y = cfg.src_y + f * (cfg.s1 - cfg.src_y)
    else:
        # downstream: continue from slit 1 toward the screen, drifting into a trough
        f = (frac - 0.5) / 0.5
        x = x_enter + f * (x_end - x_enter)
        y = cfg.s1 + f * (cfg.s1 - cfg.src_y) * 0.4  # mild deterministic drift
    return x, y


# ─────────────────────────────────────────────────────────────────────────────
# Engine builder + run
# ─────────────────────────────────────────────────────────────────────────────
def build_lattice(cfg: DSConfig, two_slit: bool) -> tuple[K4Lattice3D, np.ndarray]:
    """Build a thin-slab K4 lattice with a two- (or one-) slit reflecting wall.

    The wall is realized by DEACTIVATING cells (mask_active / mask_A / mask_B set
    False): a deactivated cell forces V_ref=0 in _scatter_all and receives no
    incident pulse in _connect_all -> a perfect non-absorbing reflector. The slit
    apertures are the un-deactivated y-gaps.
    """
    lat = K4Lattice3D(cfg.NX, cfg.NY, cfg.NZ, dx=1.0, nonlinear=False, pml_thickness=cfg.PML)
    wall = np.zeros((cfg.NX, cfg.NY, cfg.NZ), dtype=bool)
    wall[cfg.wall_x : cfg.wall_x + cfg.wall_thick, :, :] = True
    # slit 1 aperture
    wall[cfg.wall_x : cfg.wall_x + cfg.wall_thick, cfg.s1 - cfg.slit_w // 2 : cfg.s1 + (cfg.slit_w + 1) // 2, :] = False
    if two_slit:
        wall[cfg.wall_x : cfg.wall_x + cfg.wall_thick, cfg.s2 - cfg.slit_w // 2 : cfg.s2 + (cfg.slit_w + 1) // 2, :] = (
            False
        )
    lat.mask_active[wall] = False
    lat.mask_A[wall] = False
    lat.mask_B[wall] = False
    return lat, wall


def observer_mask(cfg: DSConfig) -> np.ndarray:
    """Ohmic / Gamma-mismatch impedance load (Z_det) over the slit-2 aperture and
    its immediate downstream throughput cells -- the substrate which-path detector.
    Returns a per-cell load fraction in [0, Z_det]; 0 elsewhere."""
    obs = np.zeros((cfg.NX, cfg.NY, cfg.NZ), dtype=float)
    for dxx in range(-1, cfg.wall_thick + 5):
        for dyy in range(-cfg.slit_w - 2, cfg.slit_w + 3):
            xi, yi = cfg.wall_x + dxx, cfg.s2 + dyy
            if 0 <= xi < cfg.NX and 0 <= yi < cfg.NY:
                obs[xi, yi, :] = cfg.Z_det
    return obs


def _e_intensity_slab(lat: K4Lattice3D, cfg: DSConfig) -> np.ndarray:
    """Real-space transverse |E|^2 ~ |dt A|^2, z-band-summed -> (NX, NY).

    E ~ (V_inc + V_ref) per the canonical Lagrangian; squaring removes the A/B
    sublattice sign flip, so the map is parity-clean.
    """
    E = lat.V_inc + lat.V_ref  # (NX, NY, NZ, 4)
    fld = np.sum(E**2, axis=-1)  # (NX, NY, NZ)
    return fld[:, :, cfg.zc - cfg.z_band : cfg.zc + cfg.z_band + 1].sum(axis=2)


def run_engine(cfg: DSConfig, two_slit: bool, observer: bool, n_frames: int = 60) -> RunResult:
    """Run the K4-TLM dark-wake simulation and record |E|^2 frames + time-average.

    The defect's WAKE is emitted from a stable point on the central axis upstream
    of the wall (isotropic inject_point_source). Its transverse wake spreads and,
    by the time it reaches the wall, covers BOTH slit apertures symmetrically ->
    real-space Young interference downstream.

    Engine-physics rationale for a STABLE emission point (Rule 10 integrator-time
    finding, see _orchestration STEP-0): the canonical wake "passes through both
    slits", which requires a broad, phase-stable wavefront at the wall. The K4
    group velocity is finite, so a MOVING emission point makes the wake from
    successive source positions arrive at the screen with different phase, blurring
    the time-averaged fringes (verified: moving-source two-slit V ~ 0.62 / spacing
    ~12 cells vs stable-source V ~ 0.93 / spacing ~34 cells). A pure-T_2 forward
    beam is too collimated to light two separated slits at all. The DEFECT
    TRAJECTORY through slit 1 is therefore depicted as an imposed marker overlay
    (imposed_trajectory()), faithful to the canonical "particle navigates the
    transverse ponderomotive gradients into the troughs" picture, while the
    measured wake/fringe/decoherence physics is the real engine output.
    """
    lat, _ = build_lattice(cfg, two_slit)
    obs = observer_mask(cfg) if observer else None
    omega = 2.0 * np.pi * lat.c / (cfg.lambda_cells * lat.dx)
    # Stable emission point on the central axis (both slits symmetrically lit).
    sx, sy = cfg.x_src, cfg.src_y
    zz = cfg.zc if lat.mask_active[sx, sy, cfg.zc] else cfg.zc + 1

    rec_start = int(cfg.record_from_frac * cfg.n_steps)
    acc = np.zeros((cfg.NX, cfg.NY), dtype=float)
    rec = 0
    frames: list = []
    frame_steps: list = []
    marker_xy: list = []
    frame_every = max(1, cfg.n_steps // n_frames)

    for step in range(1, cfg.n_steps + 1):
        t = step * lat.dt
        osc = np.sin(omega * t)
        if lat.mask_active[sx, sy, zz]:
            lat.inject_point_source(sx, sy, zz, cfg.amp * osc)
        lat.step()
        if observer:
            # Joule thermalization at the detector: W ~ |dt A|^2 / Z_det.
            # Realized as a per-cell power-loss factor on both wave sectors.
            lat.V_inc *= 1.0 - obs[..., None]
            lat.V_ref *= 1.0 - obs[..., None]
        if step % frame_every == 0:
            frames.append(_e_intensity_slab(lat, cfg).copy())
            frame_steps.append(step)
            marker_xy.append(imposed_trajectory(cfg, step / cfg.n_steps))
        if step > rec_start:
            acc += _e_intensity_slab(lat, cfg)
            rec += 1

    acc /= max(rec, 1)
    prof, ycg, vis, peaks, spacing = screen_profile(acc, cfg)
    return RunResult(
        energy_map=acc,
        frames=frames,
        frame_steps=frame_steps,
        marker_xy=marker_xy,
        visibility=vis,
        screen_profile=prof,
        screen_y=ycg,
        peak_ys=peaks,
        observed_spacing=spacing,
    )


def screen_profile(energy_map: np.ndarray, cfg: DSConfig, block: int = 4):
    """Coarse-grained screen-plane y-profile, interior-only (PML excluded), plus
    visibility and detected fringe peaks/spacing.

    Block-averaging by `block` in y removes the diamond unit-cell comb (unit cell
    = 2 cells); PML exclusion per A-Rule 10 / CP7.
    """
    sx = cfg.screen_x
    raw = energy_map[sx - 3 : sx + 4, :].mean(axis=0)  # average a thin x-strip at the screen
    ny = cfg.NY
    n = (ny // block) * block
    pc = raw[:n].reshape(-1, block).mean(axis=1)
    ycg = (np.arange(len(pc)) + 0.5) * block
    interior = (ycg >= cfg.PML + 8) & (ycg < ny - cfg.PML - 8)
    seg = pc[interior]
    ys = ycg[interior]
    denom = seg.max() + seg.min()
    vis = float((seg.max() - seg.min()) / denom) if denom > 0 else float("nan")
    thr = 0.5 * seg.max()
    pk = [
        i
        for i in range(1, len(seg) - 1)
        if seg[i] >= seg[i - 1] and seg[i] >= seg[i + 1] and seg[i] > thr
    ]
    peak_ys = ys[pk]
    spacing = float(np.median(np.diff(peak_ys))) if len(peak_ys) >= 2 else float("nan")
    return pc, ycg, vis, peak_ys, spacing


HONEST_CAPTION = (
    "Dark-wake mechanism on the K4-TLM substrate. The defect TRAJECTORY is imposed; "
    "the transverse wake, the interference fringes, and the Gamma-mismatch which-path "
    "decoherence are real engine physics. Not a free-propagating electron; not a helical photon."
)


# ─────────────────────────────────────────────────────────────────────────────
# Render: side-by-side animated panels (A: no observer, B: observer at slit 2)
# ─────────────────────────────────────────────────────────────────────────────
def render_panels(cfg: DSConfig, resA: RunResult, resB: RunResult, out_stem: str) -> dict:
    """Render the two-panel animation (mp4 + gif) and a static still.

    Each panel shows the per-column-normalized |E|^2 (reveals the dark-wake fringe
    structure despite geometric falloff); the cyan dashed line marks the slit wall.
    """
    nframes = min(len(resA.frames), len(resB.frames))

    def norm_cols(m: np.ndarray) -> np.ndarray:
        return m / (m.max(axis=1, keepdims=True) + 1e-30)

    framesA = [norm_cols(f) for f in resA.frames[:nframes]]
    framesB = [norm_cols(f) for f in resB.frames[:nframes]]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6.4), facecolor="#0a0a2e")
    fig.suptitle(
        "AVE Double-Slit Dark-Wake on the K4-TLM Substrate (imposed trajectory)",
        color="white",
        fontsize=15,
        fontweight="bold",
        y=0.985,
    )
    ims = []
    markers = []
    for ax, fr0, ttl, vis, res in [
        (ax1, framesA[0], "A  no observer  (coherent wake -> fringes)", resA.visibility, resA),
        (ax2, framesB[0], "B  observer at slit 2  (Z_det Ohmic load -> washout)", resB.visibility, resB),
    ]:
        ax.set_facecolor("#0a0a2e")
        im = ax.imshow(fr0.T, origin="lower", cmap="inferno", aspect="auto", vmin=0, vmax=1)
        ax.axvline(cfg.wall_x, color="cyan", lw=0.8, ls="--", alpha=0.7)
        ax.axhline(cfg.s1, color="#39ff88", lw=0.4, alpha=0.5)
        ax.axhline(cfg.s2, color="#39ff88", lw=0.4, alpha=0.5)
        ax.set_title(f"{ttl}\nscreen visibility V = {vis:.2f}", color="white", fontsize=11)
        ax.set_xlabel("x  [lattice cells]", color="white")
        ax.set_ylabel("y  [lattice cells]", color="white")
        ax.tick_params(colors="white", labelsize=8)
        for s in ax.spines.values():
            s.set_color("#334")
        ims.append(im)
        # imposed-trajectory marker (depicted defect navigating through slit 1)
        mx0, my0 = res.marker_xy[0] if res.marker_xy else (cfg.x_src, cfg.src_y)
        (mk,) = ax.plot(
            [mx0], [my0], marker="o", color="#ff3b3b", markersize=7,
            markeredgecolor="white", markeredgewidth=1.0, zorder=12,
        )
        markers.append(mk)
        ax.set_xlim(0, cfg.NX)
        ax.set_ylim(0, cfg.NY)
    # observer marker on panel B
    ax2.plot(
        cfg.wall_x, cfg.s2, "o", color="#39ff88", markersize=9,
        markeredgecolor="white", markeredgewidth=1.5, zorder=10,
    )
    ax2.annotate("OBSERVER (Z_det)", xy=(cfg.wall_x, cfg.s2), xytext=(cfg.wall_x - 55, cfg.s2 + 22),
                 fontsize=8, color="#39ff88", fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color="#39ff88", lw=1.2))
    # imposed-trajectory legend (honesty: marker is depicted, not dynamical)
    ax1.annotate(
        "imposed defect trajectory (depicted)", xy=(cfg.x_src, cfg.src_y),
        xytext=(cfg.x_src + 8, cfg.src_y + 16), fontsize=7.5, color="#ff8b8b",
        arrowprops=dict(arrowstyle="->", color="#ff8b8b", lw=1.0),
    )
    fig.text(0.5, 0.012, HONEST_CAPTION, color="#cccccc", fontsize=7.5, ha="center", style="italic", wrap=True)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    def update(k: int):
        ims[0].set_data(framesA[k].T)
        ims[1].set_data(framesB[k].T)
        mxA, myA = resA.marker_xy[k] if k < len(resA.marker_xy) else resA.marker_xy[-1]
        mxB, myB = resB.marker_xy[k] if k < len(resB.marker_xy) else resB.marker_xy[-1]
        markers[0].set_data([mxA], [myA])
        markers[1].set_data([mxB], [myB])
        return ims + markers

    anim = FuncAnimation(fig, update, frames=nframes, blit=True)

    SIM_OUTPUTS.mkdir(parents=True, exist_ok=True)
    out_mp4 = str(SIM_OUTPUTS / f"{out_stem}.mp4")
    out_gif = str(SIM_OUTPUTS / f"{out_stem}.gif")
    out_png = str(SIM_OUTPUTS / f"{out_stem}_still.png")

    rendered = {}
    try:
        anim.save(out_mp4, writer=FFMpegWriter(fps=18, bitrate=2400))
        rendered["mp4"] = out_mp4
    except Exception as exc:  # ffmpeg may be absent in some envs
        rendered["mp4_error"] = str(exc)
    anim.save(out_gif, writer=PillowWriter(fps=15))
    rendered["gif"] = out_gif

    # static still = last frame
    update(nframes - 1)
    fig.savefig(out_png, dpi=110, bbox_inches="tight", facecolor="#0a0a2e")
    rendered["still"] = out_png
    plt.close(fig)
    return rendered


def visibility_vs_z_det(cfg: DSConfig, z_values: list, out_stem: str) -> dict:
    """Optional: screen fringe visibility vs detector load Z_det.

    Demonstrates that the which-path transition is CONTINUOUS (dark-wake / Born),
    not the binary all-or-nothing collapse of the Copenhagen reading. A separate
    light render (no frames recorded -> fast).
    """
    vis_pts = []
    for zd in z_values:
        c = DSConfig(**{**cfg.__dict__})
        c.Z_det = zd
        res = run_engine(c, two_slit=True, observer=(zd > 0.0), n_frames=2)
        vis_pts.append(res.visibility)
    # single-slit floor (full which-path) for reference
    floor = run_engine(cfg, two_slit=False, observer=False, n_frames=2).visibility

    fig, ax = plt.subplots(figsize=(7.5, 5), facecolor="#0a0a2e")
    ax.set_facecolor("#0a0a2e")
    ax.plot(z_values, vis_pts, "o-", color="#ff8b3b", lw=2, markersize=7, label="K4-TLM dark-wake (continuous)")
    ax.axhline(floor, color="#39ff88", ls="--", lw=1.2, label=f"single-slit floor (V={floor:.2f})")
    # Copenhagen-binary caricature: V stays maximal until "measurement", then 0.
    ax.step(
        [z_values[0], 0.5, 0.5, z_values[-1]],
        [vis_pts[0], vis_pts[0], floor, floor],
        where="post", color="#5b9bff", ls=":", lw=1.5, label="Copenhagen-binary (caricature)",
    )
    ax.set_xlabel("detector load strength  Z_det", color="white")
    ax.set_ylabel("screen fringe visibility  V", color="white")
    ax.set_title("Which-path decoherence is CONTINUOUS on the K4-TLM substrate", color="white", fontsize=11)
    ax.tick_params(colors="white")
    for s in ax.spines.values():
        s.set_color("#334")
    leg = ax.legend(loc="lower left", fontsize=8, facecolor="#111122", edgecolor="#334")
    for txt in leg.get_texts():
        txt.set_color("white")
    fig.text(0.5, 0.01, HONEST_CAPTION, color="#cccccc", fontsize=7, ha="center", style="italic", wrap=True)
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    SIM_OUTPUTS.mkdir(parents=True, exist_ok=True)
    out_png = str(SIM_OUTPUTS / f"{out_stem}_visibility_vs_Zdet.png")
    fig.savefig(out_png, dpi=110, bbox_inches="tight", facecolor="#0a0a2e")
    plt.close(fig)
    return {
        "z_values": list(z_values),
        "visibility": [float(v) for v in vis_pts],
        "floor": float(floor),
        "png": out_png,
    }


def main() -> dict:
    parser = argparse.ArgumentParser(description="K4-TLM double-slit dark-wake animation")
    parser.add_argument("--steps", type=int, default=None, help="override n_steps")
    parser.add_argument("--frames", type=int, default=60, help="recorded animation frames")
    parser.add_argument("--stem", type=str, default="k4tlm_double_slit_dark_wake")
    parser.add_argument("--visibility-sweep", action="store_true", help="also render visibility-vs-Z_det")
    args = parser.parse_args()

    cfg = DSConfig()
    if args.steps:
        cfg.n_steps = args.steps

    print("=" * 78)
    print("  K4-TLM Double-Slit Dark-Wake (Option (i): imposed trajectory)")
    print("  Brief: _orchestration/double-slit-ave-sim.md")
    print("=" * 78)
    const_info = verify_constants(cfg)
    print(json.dumps(const_info, indent=2))
    pred = cfg.predicted_fringe_spacing()
    print(f"\n  FORWARD-PREDICTED fringe spacing Delta_y = lambda*L/d = "
          f"{cfg.lambda_cells:.0f}*{cfg.L}/{cfg.slit_sep} = {pred:.1f} cells\n")

    print("  Running Panel A (no observer, two slits)...", flush=True)
    resA = run_engine(cfg, two_slit=True, observer=False, n_frames=args.frames)
    print("  Running Panel B (observer at slit 2, two slits)...", flush=True)
    resB = run_engine(cfg, two_slit=True, observer=True, n_frames=args.frames)
    print("  Running reference (single slit, no observer)...", flush=True)
    res1 = run_engine(cfg, two_slit=False, observer=False, n_frames=2)

    print(f"\n  OBSERVED two-slit fringe spacing  = {resA.observed_spacing:.1f} cells "
          f"(predicted {pred:.1f})")
    print(f"  Panel A (two-slit, no obs) visibility = {resA.visibility:.3f}")
    print(f"  Panel B (two-slit, observer) visibility = {resB.visibility:.3f}")
    print(f"  Single-slit reference visibility        = {res1.visibility:.3f}")
    print(f"  which-path washout (A -> B)             = {resA.visibility - resB.visibility:+.3f}")

    rendered = render_panels(cfg, resA, resB, args.stem)
    print("\n  Rendered:")
    for k, v in rendered.items():
        print(f"    {k}: {v}")

    sweep = None
    if args.visibility_sweep:
        print("\n  Running visibility-vs-Z_det sweep...", flush=True)
        sweep = visibility_vs_z_det(cfg, [0.0, 0.2, 0.4, 0.6, 0.8, 0.95], args.stem)
        print(f"    visibility(Z_det): {list(zip(sweep['z_values'], [round(v, 3) for v in sweep['visibility']]))}")
        print(f"    single-slit floor: {sweep['floor']:.3f}")
        print(f"    png: {sweep['png']}")

    summary = {
        "constants": const_info,
        "predicted_fringe_spacing_cells": float(pred),
        "observed_fringe_spacing_cells": float(resA.observed_spacing),
        "visibility_two_slit_no_obs": float(resA.visibility),
        "visibility_two_slit_observer": float(resB.visibility),
        "visibility_single_slit": float(res1.visibility),
        "whichpath_washout": float(resA.visibility - resB.visibility),
        "peak_ys_two_slit": [float(y) for y in (resA.peak_ys if resA.peak_ys is not None else [])],
        "honest_caption": HONEST_CAPTION,
        "rendered": rendered,
        "visibility_sweep": sweep,
    }
    print("\n" + json.dumps({k: v for k, v in summary.items() if k != "constants"}, indent=2))
    return summary


if __name__ == "__main__":
    main()
