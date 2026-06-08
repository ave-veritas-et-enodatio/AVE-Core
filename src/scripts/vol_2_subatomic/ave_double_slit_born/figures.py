"""
Figure builders for the AVE double-slit / Born-from-clicks capstone.

Stills (research/figures/2026-06-08-ave-double-slit/):
  (a) smooth_field      - the REAL FDTD interference field |E|^2 through the slits
  (b) clicks_first      - the first ~12 clicks (scattered, no pattern)
  (c) clicks_hundreds   - ~hundreds of clicks (the fringe pattern emerging)
  (d) born_recovered    - final click histogram vs the field |psi|^2 (Born back)
Plus a long animation of clicks landing one-by-one with the field underneath.

Honesty banner stamped on every figure: the field + clicks are REAL; the Born
rule EMERGES from threshold-crossing (no Born postulate in the detector); the
electron's (2,3) torus-knot winding is NOT shown (not hostable here).
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.animation import FFMpegWriter  # noqa: E402
from matplotlib.colors import PowerNorm  # noqa: E402

from .click_detector import ClickResult  # noqa: E402
from .config import fig_path  # noqa: E402
from .field_engine import FieldResult  # noqa: E402

_BG = "#05060d"
_FIELD_CMAP = "inferno"
_CLICK_C = "#39d7ff"
_PSI_C = "#ff5db1"
_HONESTY = (
    "REAL: FDTD field (canonical Maxwell engine) + threshold-crossing clicks   |   "
    "Born p∝|E|² EMERGES (no Born rule in the detector)   |   electron (2,3) winding not shown"
)


def _style(ax):
    ax.set_facecolor(_BG)
    ax.tick_params(colors="#8893b0", labelsize=8)
    for spine in ax.spines.values():
        spine.set_color("#2a3350")


def _field_extent(field: FieldResult) -> tuple[int, int]:
    """x-window for the cropped field image: just before the wall to past the detector."""
    x0 = max(0, field.cfg.wall_x - 12)
    x1 = min(field.cfg.nx, field.x_det + 14)
    return x0, x1


def _render_field(ax, field: FieldResult, *, gamma: float = 0.6, alpha: float = 1.0, column_norm: bool = True) -> None:
    """Draw the cropped |E|^2 interference field with the wall + slits + screen.

    The field decays cylindrically (~1/r) from the slits, so the detector-region
    fringes are ~10^3x fainter than near the slits. ``column_norm`` rescales each
    propagation column to its own peak so the interference fan is visible at
    every distance (a standard diffraction-display gain; the true |E|^2 fringe
    profile at the detector is shown quantitatively in the histogram figure).
    """
    x0, x1 = _field_extent(field)
    img = field.intensity2d[x0:x1, :].T.copy()  # (ny, x-window)
    if column_norm:
        col_max = img.max(axis=0, keepdims=True)
        img = np.where(col_max > 0, img / col_max, 0.0)
        vmax = 1.0
    else:
        vmax = np.percentile(img[img > 0], 99.6) if np.any(img > 0) else 1.0
    ax.imshow(
        img,
        origin="lower",
        aspect="auto",
        extent=[x0, x1, 0, field.cfg.ny],
        cmap=_FIELD_CMAP,
        norm=PowerNorm(gamma=gamma, vmin=0.0, vmax=vmax),
        alpha=alpha,
        interpolation="bilinear",
    )
    # Barrier (opaque, slits left open).
    wall = field.wall_mask2d[x0:x1, :].T.astype(float)
    wall_rgba = np.zeros((*wall.shape, 4))
    wall_rgba[..., :3] = 0.55
    wall_rgba[..., 3] = wall * 0.92
    ax.imshow(wall_rgba, origin="lower", aspect="auto", extent=[x0, x1, 0, field.cfg.ny])
    # Detector screen line.
    ax.axvline(field.x_det, color="#cfe9ff", lw=1.1, alpha=0.8, ls=(0, (4, 3)))
    ax.text(field.x_det + 0.6, field.cfg.ny * 0.02, "detector", color="#cfe9ff", fontsize=7, rotation=90, va="bottom")
    _style(ax)


def _screen_scatter(ax, field: FieldResult, clicks: ClickResult, n: int, heights: np.ndarray) -> None:
    """The iconic buildup: dots at (detector-cell, cosmetic screen-height)."""
    cells = clicks.click_cells[:n]
    ax.scatter(
        cells,
        heights[:n],
        s=7,
        c=_CLICK_C,
        alpha=0.85,
        linewidths=0,
    )
    ax.set_xlim(0, field.cfg.ny)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel("detector position  y  [cells]", color="#aab4d4", fontsize=9)
    _style(ax)


def _honesty_banner(fig) -> None:
    fig.text(0.5, 0.012, _HONESTY, color="#6f7da3", fontsize=7.0, ha="center", va="bottom")


# ----------------------------------------------------------------------------
# (a) smooth interference field
# ----------------------------------------------------------------------------
def still_smooth_field(field: FieldResult) -> str:
    fig, ax = plt.subplots(figsize=(11, 6.2), facecolor=_BG)
    _render_field(ax, field)
    for cy in field.slit_centres:
        ax.plot(field.cfg.wall_x + field.cfg.wall_thickness, cy, marker=">", color="#ffd479", ms=6)
    ax.set_title(
        "AVE double slit — REAL FDTD interference field $|E|^2$ (canonical Yee/Maxwell engine)",
        color="#eaf0ff",
        fontsize=13,
        pad=10,
    )
    ax.set_xlabel("propagation  x  [cells]", color="#aab4d4", fontsize=9)
    ax.set_ylabel("transverse  y  [cells]", color="#aab4d4", fontsize=9)
    ax.text(
        0.015,
        0.97,
        f"λ = {field.wavelength_measured:.0f} cells   d = {field.cfg.slit_sep} cells   "
        f"L = {field.cfg.L} cells\nfringe spacing (pred λL/d) = {field.fringe_spacing_pred:.0f} cells",
        transform=ax.transAxes,
        color="#cfe9ff",
        fontsize=8.5,
        va="top",
        bbox=dict(boxstyle="round", fc="#101426", ec="#2a3350", alpha=0.85),
    )
    _honesty_banner(fig)
    fig.subplots_adjust(bottom=0.11, top=0.93, left=0.06, right=0.985)
    out = fig_path("a_smooth_interference_field.png")
    fig.savefig(out, dpi=160, facecolor=_BG)
    plt.close(fig)
    return str(out)


# ----------------------------------------------------------------------------
# (b)/(c) click buildup stills
# ----------------------------------------------------------------------------
def still_clicks(field: FieldResult, clicks: ClickResult, n: int, heights: np.ndarray, tag: str, subtitle: str) -> str:
    fig, ax = plt.subplots(figsize=(11, 4.6), facecolor=_BG)
    # Faint field behind the screen, mapped onto the y axis as a thin reference band.
    _screen_scatter(ax, field, clicks, n, heights)
    ax.set_title(subtitle, color="#eaf0ff", fontsize=13, pad=10)
    ax.text(
        0.985,
        0.93,
        f"{n} clicks",
        transform=ax.transAxes,
        color=_CLICK_C,
        fontsize=12,
        ha="right",
        va="top",
        weight="bold",
    )
    _honesty_banner(fig)
    fig.subplots_adjust(bottom=0.18, top=0.9, left=0.05, right=0.985)
    out = fig_path(f"{tag}.png")
    fig.savefig(out, dpi=160, facecolor=_BG)
    plt.close(fig)
    return str(out)


# ----------------------------------------------------------------------------
# (d) Born recovered: histogram vs field |psi|^2
# ----------------------------------------------------------------------------
def still_born_recovered(field: FieldResult, clicks: ClickResult, heights: np.ndarray, stats: dict) -> str:
    fig, (axs, axh) = plt.subplots(
        2, 1, figsize=(11, 7.4), facecolor=_BG, gridspec_kw=dict(height_ratios=[1.0, 1.25], hspace=0.28)
    )
    n = clicks.click_cells.size
    _screen_scatter(axs, field, clicks, n, heights)
    axs.set_title(
        f"Born recovered — {n} threshold-crossing clicks rebuild the fringes",
        color="#eaf0ff",
        fontsize=13,
        pad=8,
    )
    axs.set_xlabel("")

    # Histogram (clicks) vs the REAL field |psi|^2.
    y = np.arange(field.cfg.ny)
    hist = clicks.histogram
    psi2 = field.intensity_y.copy()
    psi2 = psi2 / psi2.sum() * hist.sum()  # scale to the same click count (units, not Born)
    axh.bar(y, hist, width=1.0, color=_CLICK_C, alpha=0.62, label="clicks (threshold-crossing)")
    axh.plot(y, psi2, color=_PSI_C, lw=2.0, label=r"REAL FDTD field $|E|^2$ (= $|\psi|^2$)")
    axh.set_xlim(0, field.cfg.ny)
    axh.set_xlabel("detector position  y  [cells]", color="#aab4d4", fontsize=9)
    axh.set_ylabel("counts", color="#aab4d4", fontsize=9)
    leg = axh.legend(facecolor="#101426", edgecolor="#2a3350", fontsize=9, loc="upper right")
    for txt in leg.get_texts():
        txt.set_color("#dde6ff")
    _style(axh)
    axh.text(
        0.014,
        0.95,
        f"χ²/dof = {stats['chi2_dof']:.2f}    KS = {stats['ks']:.3f}    corr = {stats['corr']:.3f}\n"
        f"fringe spacing: clicks {stats['spacing_clicks']:.1f} vs de-Broglie λL/d "
        f"{field.fringe_spacing_pred:.1f} cells ({stats['spacing_err_pct']:.1f}%)\n"
        "Born EMERGES — no p=|ψ|² anywhere in the detector code",
        transform=axh.transAxes,
        color="#cfe9ff",
        fontsize=8.5,
        va="top",
        bbox=dict(boxstyle="round", fc="#101426", ec="#2a3350", alpha=0.9),
    )
    _honesty_banner(fig)
    fig.subplots_adjust(bottom=0.1, top=0.94, left=0.06, right=0.985)
    out = fig_path("d_born_recovered.png")
    fig.savefig(out, dpi=160, facecolor=_BG)
    plt.close(fig)
    return str(out)


# ----------------------------------------------------------------------------
# Long animation: clicks landing one-by-one over the field
# ----------------------------------------------------------------------------
def animation(field: FieldResult, clicks: ClickResult, heights: np.ndarray, stats: dict, *, fps: int = 24) -> str:
    n = clicks.click_cells.size
    # ~360 frames; each frame lands a batch of clicks (slow start, faster later).
    n_frames = 360
    schedule = np.unique(np.round(np.linspace(1, n, n_frames)).astype(int))

    fig = plt.figure(figsize=(11.5, 8.2), facecolor=_BG)
    gs = fig.add_gridspec(2, 1, height_ratios=[1.05, 1.0], hspace=0.32)
    ax_top = fig.add_subplot(gs[0])
    ax_bot = fig.add_subplot(gs[1])

    _render_field(ax_top, field, gamma=0.5, alpha=0.85)
    ax_top.set_title(
        "AVE double slit: REAL field underneath, clicks landing one-by-one",
        color="#eaf0ff",
        fontsize=12.5,
        pad=8,
    )
    ax_top.set_xlabel("propagation  x  [cells]", color="#aab4d4", fontsize=9)
    ax_top.set_ylabel("y  [cells]", color="#aab4d4", fontsize=9)
    # Clicks land on the detector line; cosmetic screen-height reused as marker offset.
    click_dots = ax_top.scatter([], [], s=10, c=_CLICK_C, alpha=0.9, linewidths=0)

    y = np.arange(field.cfg.ny)
    psi2 = field.intensity_y / field.intensity_y.sum() * n
    ax_bot.plot(y, psi2, color=_PSI_C, lw=1.8, alpha=0.9, label=r"field $|E|^2$ (= $|\psi|^2$)")
    bars = ax_bot.bar(y, np.zeros_like(y, dtype=float), width=1.0, color=_CLICK_C, alpha=0.6, label="clicks")
    ax_bot.set_xlim(0, field.cfg.ny)
    ax_bot.set_ylim(0, psi2.max() * 1.5)
    ax_bot.set_xlabel("detector position  y  [cells]", color="#aab4d4", fontsize=9)
    ax_bot.set_ylabel("counts", color="#aab4d4", fontsize=9)
    leg = ax_bot.legend(facecolor="#101426", edgecolor="#2a3350", fontsize=9, loc="upper right")
    for txt in leg.get_texts():
        txt.set_color("#dde6ff")
    _style(ax_top)
    _style(ax_bot)
    counter = ax_bot.text(
        0.014, 0.95, "", transform=ax_bot.transAxes, color="#cfe9ff", fontsize=10, va="top", weight="bold"
    )
    _honesty_banner(fig)
    fig.subplots_adjust(bottom=0.1, top=0.93, left=0.07, right=0.985)

    det_x = field.x_det
    out = fig_path("born_from_clicks_animation.mp4")
    writer = FFMpegWriter(fps=fps, bitrate=2600, metadata=dict(artist="AVE"))
    with writer.saving(fig, str(out), dpi=130):
        for k in schedule:
            cells = clicks.click_cells[:k]
            # top panel: dots on the detector line, jittered in x by cosmetic height
            xs = det_x + (heights[:k] - 0.5) * 6.0
            click_dots.set_offsets(np.column_stack([xs, cells]))
            # bottom panel: live histogram
            h = np.bincount(cells, minlength=field.cfg.ny).astype(float)
            for rect, hv in zip(bars, h):
                rect.set_height(hv)
            counter.set_text(f"{k} clicks   (χ²/dof→{stats['chi2_dof']:.2f}, Born recovered)")
            writer.grab_frame()
    plt.close(fig)
    return str(out)


def cosmetic_heights(n: int, seed: int = 7) -> np.ndarray:
    """Random screen-heights for the buildup visual (cosmetic only - the physics
    is the horizontal detector position; the screen's other dimension is not
    resolved by the 1D detector row)."""
    return np.random.default_rng(seed).random(n)
