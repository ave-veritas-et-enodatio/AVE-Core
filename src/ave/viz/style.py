"""AVE house figure style — the single source of truth for figure appearance.

This module turns "follow the house style" from a per-driver checklist into a
mechanical call. A driver does::

    from ave.viz import style

    style.apply()                      # print profile (white bg) by default
    fig, ax = plt.subplots()
    ax.plot(x, y, color=style.COLORS["ave"], label="AVE")
    ax.set_xlabel(style.axis_label("Frequency", "f", "Hz"))
    style.save(fig, sim_output("vol9", "my_figure"))   # writes .pdf + .png

It is a pure presentation-layer helper: it has NO dependency on the engine
(`ave.core`) and changes only how figures *look*, never what they show
(ave-module-library-discipline — presentation tier, not physics tier). The
matplotlib rcParams live in the sibling ``ave.mplstyle`` stylesheet; the
semantic colour palette and the column-size presets live here as Python data so
the maintainer re-tunes the whole corpus in exactly one place.

Two profiles, one palette:
  * ``profile="print"`` (default) — white background, black text/axes, for the
    LaTeX-embedded manuscript / Vol-9 datasheet figures. This is the house
    default because the corpus had drifted to 30x ``dark_background`` rasters
    shipping into a print manuscript (ave-figure-discipline Axis 4).
  * ``profile="screen"`` — dark background for interactive / field-viz work, so
    the existing dark engine-output aesthetic is preserved — just no longer the
    silent default for print figures.

Both profiles share ``COLORS`` (the Okabe-Ito colourblind-safe palette) and the
same colormaps, so an AVE-prediction curve is the same blue whether it is drawn
on a white page or a dark screen.

See ``~/.claude/skills/ave-figure-discipline/SKILL.md`` for the five-axis figure
gate this module mechanizes (Axis 2 units, Axis 3 rendering, Axis 4 house style).
"""

from __future__ import annotations

import warnings
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Semantic palette — Okabe-Ito colourblind-safe (ONE place; Grant-ratifiable)
# ---------------------------------------------------------------------------
# Every colour the corpus uses by name lives here. To re-tune the house palette,
# edit THIS dict — do not hard-code hex in a driver. The values below are the
# PROPOSED defaults (Okabe-Ito 8-colour set, the standard colourblind-safe
# palette); Grant ratifies or re-tunes. Pair colour with linestyle/marker in the
# driver — never rely on colour alone (ave-figure-discipline Axis 4).
COLORS: dict[str, str] = {
    "ave": "#0072B2",        # blue        — the AVE prediction / engine result
    "comparison": "#D55E00", # vermillion  — SM / QED / standard-physics overlay
    "data": "#000000",       # black       — empirical data points
    "accent": "#009E73",     # bluish-green — secondary AVE series / highlight
    "muted": "#7F7F7F",      # gray        — reference lines, annotations, guides
}

# ---------------------------------------------------------------------------
# Regime palette — the four universal saturation regimes (ONE place)
# ---------------------------------------------------------------------------
# The four-regime map (ave-kb/.../ch7-regime-map/four-regimes.md) partitions all
# of physics by the single control parameter r = A/A_c through the Axiom-4 kernel
# S(r) = sqrt(1 - r^2). Every regime-banded figure in the corpus shades these four
# bands; they previously used an ad-hoc green/amber/red "traffic-light" fill that
# is NOT colourblind-safe (the amber/red pair collides under deuteranopia) and
# drifted in hex per-driver. This dict single-sources them to the colourblind-safe
# Okabe-Ito family so a regime band is the same colour in every figure.
#
# Semantics (a stoplight that IS colourblind-safe):
#   I   green       — Linear: standard equations hold, propagate / proceed.
#   II  yellow      — Nonlinear: caution. Axiom-4 curvature switches on; metric
#                     lensing begins (the permittivity softens as eps = S while
#                     the Maxwell speed stiffens as c_EM = 1/S).
#   III orange      — Avalanche / Yield: deep lensing, energy-trapping dominates
#                     (Q = 1/S >= 2); a phase transition is underway.
#   IV  vermillion  — Ruptured: S = 0, K4 topology destroyed, propagation is NOT
#                     allowed.
#
# Boundaries (single-sourced to four-regimes.md; DERIVED, not chosen):
#   r1 = sqrt(2*alpha) ~ 0.1208  (Regime I/II : Delta-S = alpha, sub-alpha limit)
#   r2 = sqrt(3)/2     ~ 0.8660  (Regime II/III: spin-2 avalanche onset Q = 2)
#   r3 = 1.0                     (Regime III/IV: Axiom-4 rupture, S -> 0)
# A driver pairs the band fill with its boundary lines; it does NOT re-derive the
# hex. Keep colour paired with the I/II/III/IV text label — never rely on the band
# colour alone (ave-figure-discipline Axis 4).
REGIME_COLORS: dict[str, str] = {
    "I": "#009E73",    # bluish-green — Linear      (proceed)
    "II": "#F0E442",   # yellow       — Nonlinear   (caution: lensing onset)
    "III": "#E69F00",  # orange       — Avalanche   (deep lensing / yield)
    "IV": "#D55E00",   # vermillion   — Ruptured    (no propagation)
}

# Semantic names for the four regimes (the traffic-light reading: proceed /
# caution-metric-lensing / rupture). Paired with REGIME_COLORS so the band
# colour is never the only carrier of meaning (ave-figure-discipline Axis 4).
REGIME_LABELS: dict[str, str] = {
    "I": "I — Linear (proceed)",
    "II": "II — Nonlinear (caution: lensing)",
    "III": "III — Avalanche (deep lensing)",
    "IV": "IV — Ruptured (no propagation)",
}


def shade_regimes(ax, bounds, *, axis: str = "x", labels: bool = True, alpha: float = 0.15):
    """Shade the four canonical operating regimes on ``ax`` — the single mechanic.

    Every regime-banded figure calls this, so they read identically (same
    colours, labels, ordering). Presentation tier: the regime BOUNDARIES are
    physics and stay in ``ave.core`` — the caller passes them in, keeping this
    module's no-``ave.core``-dependency invariant intact.

    Parameters
    ----------
    ax:
        Axes to shade (data already plotted, so the limits are set).
    bounds:
        ``(r1, r2, r3)`` — the I/II, II/III, III/IV boundaries on the plotted
        axis, imported by the caller from the canonical source (e.g.
        ``ave.core.constants.R_I`` = √(2α); ``four-regimes.md``). Bands run
        ``[lo, r1)=I``, ``[r1, r2)=II``, ``[r2, r3)=III``, ``[r3, hi]=IV``.
    axis:
        ``"x"`` (default) → vertical bands (``axvspan``); ``"y"`` → horizontal
        (``axhspan``).
    labels:
        If True, attach REGIME_LABELS to the legend (one proxy per band).
    alpha:
        Band fill transparency.

    Returns
    -------
    list
        The band artists, in I→IV order.
    """
    r1, r2, r3 = bounds
    if axis == "x":
        lo, hi = ax.get_xlim()
        span = ax.axvspan
    elif axis == "y":
        lo, hi = ax.get_ylim()
        span = ax.axhspan
    else:
        raise ValueError(f"axis must be 'x' or 'y', got {axis!r}")
    arts = []
    for a, b, key in ((lo, r1, "I"), (r1, r2, "II"), (r2, r3, "III"), (r3, hi, "IV")):
        if b > a:
            arts.append(span(a, b, color=REGIME_COLORS[key], alpha=alpha, zorder=0,
                             label=(REGIME_LABELS[key] if labels else "_nolegend_")))
    return arts


# The ordered colour cycle for unlabelled multi-series plots. Kept distinct from
# the semantic names above but drawn from the same colourblind-safe family so an
# auto-cycled plot still reads on-style. Order chosen for max adjacent contrast.
_PROP_CYCLE: tuple[str, ...] = (
    COLORS["ave"],         # blue
    COLORS["comparison"],  # vermillion
    COLORS["accent"],      # bluish-green
    "#CC79A7",             # reddish-purple (Okabe-Ito)
    "#E69F00",             # orange         (Okabe-Ito)
    "#56B4E9",             # sky blue       (Okabe-Ito)
    "#F0E442",             # yellow         (Okabe-Ito)
    COLORS["muted"],       # gray
)

# ---------------------------------------------------------------------------
# Colormaps — perceptually-uniform + print-safe (retires `hot`)
# ---------------------------------------------------------------------------
# CMAP_SEQ: sequential / one-sided fields (|E|, energy density, magnitude).
#   `magma` is perceptually uniform and prints to a sane greyscale, unlike `hot`
#   (which the corpus used 55x and which clips to white in print).
# CMAP_DIV: signed / diverging fields (anything with a meaningful zero: charge
#   density, V_ref sign, residuals). `RdBu_r` is the colourblind-safe diverging
#   choice already in partial use (retires `seismic`/`hsv` for signed data).
CMAP_SEQ: str = "magma"
CMAP_DIV: str = "RdBu_r"

# ---------------------------------------------------------------------------
# Column-size presets — so figsizes stop drifting (10x8 / 8x8 / 10x6 / 13x9 ...)
# ---------------------------------------------------------------------------
# Sizes in inches, tuned for a single-column / double-column / full-width slot in
# the manuscript. A driver asks for a *kind*, not a magic tuple.
_FIGSIZES: dict[str, tuple[float, float]] = {
    "single": (6.5, 4.0),   # one text-column figure (the default)
    "double": (3.3, 2.6),   # half-column / side-by-side pair member
    "wide": (9.5, 4.0),     # full-text-width banner / multi-panel row
    "square": (5.2, 5.2),   # field imshow / phase-space plot
}

# Path to the bundled print-profile stylesheet (sibling of this module).
_STYLE_FILE: Path = Path(__file__).resolve().parent / "ave.mplstyle"

# Screen-profile overrides applied ON TOP of the print stylesheet. Only the
# background/text colours flip; everything else (fonts, layout, palette, grid)
# is shared so the two profiles stay visually consistent.
_SCREEN_OVERRIDES: dict[str, object] = {
    "figure.facecolor": "#0a0a0a",
    "axes.facecolor": "#0a0a0a",
    "savefig.facecolor": "#0a0a0a",
    "text.color": "white",
    "axes.edgecolor": "white",
    "axes.labelcolor": "white",
    "axes.titlecolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "#666666",
}


def apply(profile: str = "print") -> None:
    """Apply the AVE house style to the global matplotlib rcParams.

    Call once near the top of a driver, before creating any figure.

    Parameters
    ----------
    profile:
        ``"print"`` (default) — white background, black text/axes, for
        manuscript / datasheet figures embedded in LaTeX. ``"screen"`` — dark
        background for interactive / field-viz, layered on the same base so the
        palette and layout match the print profile.

    Raises
    ------
    ValueError
        If ``profile`` is not ``"print"`` or ``"screen"``.
    """
    if profile not in ("print", "screen"):
        raise ValueError(
            f"unknown profile {profile!r}; expected 'print' (white, default) "
            f"or 'screen' (dark field-viz)"
        )

    # Base: the print stylesheet (white). Loaded for BOTH profiles so screen is
    # a thin override, not a parallel source of truth.
    plt.style.use(str(_STYLE_FILE))

    # The colour cycle is set from the COLORS palette so the cycle lives in the
    # same one place as the semantic names (kept out of the .mplstyle on purpose).
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=list(_PROP_CYCLE))

    if profile == "screen":
        mpl.rcParams.update(_SCREEN_OVERRIDES)


def axis_label(quantity: str, symbol: str, unit: str) -> str:
    """Return the canonical "Quantity $symbol$ [unit]" axis-label string.

    Enforces ave-figure-discipline Axis 2 (every axis/colorbar carries quantity
    + symbol + unit, in mathtext). A dimensionless quantity is labelled
    ``[dimensionless]`` rather than left bare.

    Examples
    --------
    >>> axis_label("Frequency", "f", "Hz")
    'Frequency $f$ [Hz]'
    >>> axis_label("Strain", "\\\\delta n", "")
    'Strain $\\\\delta n$ [dimensionless]'

    Parameters
    ----------
    quantity:
        Human-readable quantity name, e.g. ``"Frequency"``. May be empty to emit
        a symbol-only label (``"$f$ [Hz]"``).
    symbol:
        Math symbol, wrapped in ``$...$`` for mathtext. Pass the bare symbol
        (``"f"``, ``"\\delta n"``) — do not pre-wrap in ``$``.
    unit:
        Physical unit, e.g. ``"Hz"``, ``"V/m"``, ``"m"``. Empty / ``None`` →
        ``[dimensionless]``.
    """
    sym = f"${symbol}$" if symbol else ""
    unit_token = unit.strip() if unit else ""
    bracket = f"[{unit_token}]" if unit_token else "[dimensionless]"
    parts = [p for p in (quantity.strip() if quantity else "", sym, bracket) if p]
    return " ".join(parts)


def figsize(kind: str = "single") -> tuple[float, float]:
    """Return a standard column-size preset (inches).

    Parameters
    ----------
    kind:
        One of ``"single"`` (one text column, the default), ``"double"``
        (half-column / side-by-side member), ``"wide"`` (full-text-width banner /
        multi-panel row), or ``"square"`` (field imshow / phase-space).

    Raises
    ------
    ValueError
        If ``kind`` is not a known preset.
    """
    try:
        return _FIGSIZES[kind]
    except KeyError:
        raise ValueError(
            f"unknown figsize kind {kind!r}; expected one of {sorted(_FIGSIZES)}"
        ) from None


def legend(ax, *args, where: str = "right", **kwargs):
    """Place a legend OUTSIDE the axes so it never overlaps the data.

    ave-figure-discipline Axis 3: ``loc="best"`` / auto-placement is NOT a
    guarantee — when the data fills the axes (e.g. an oscillation spanning the
    full vertical range), matplotlib still drops the legend onto the curve. This
    helper reserves space outside the plot box instead; ``save``'s
    ``bbox_inches="tight"`` ensures the outside legend is captured in the output.

    Parameters
    ----------
    ax:
        The Axes to attach the legend to.
    *args, **kwargs:
        Forwarded to ``ax.legend`` (handles/labels, ``ncol``, ``title``, ...).
        An explicit ``loc`` or ``bbox_to_anchor`` in ``kwargs`` overrides the
        ``where`` placement — the escape hatch for a legend the caller has
        verified sits in genuine in-axes whitespace.
    where:
        ``"right"`` (default) — to the right of the axes; good for a single-panel
        figure. Do NOT use on the left/middle panel of a multi-panel row, where
        it lands on the neighbouring panel — use ``"below"`` there. ``"below"`` —
        beneath the axes; good for multi-panel rows and many entries (pass
        ``ncol`` to spread them).

    Returns
    -------
    matplotlib.legend.Legend

    Raises
    ------
    ValueError
        If ``where`` is not ``"right"`` or ``"below"``.
    """
    placements = {
        "right": dict(loc="upper left", bbox_to_anchor=(1.02, 1.0)),
        "below": dict(loc="upper center", bbox_to_anchor=(0.5, -0.18)),
    }
    if where not in placements:
        raise ValueError(
            f"unknown legend placement {where!r}; expected 'right' or 'below'"
        )
    # An explicit caller loc/bbox wins (verified-whitespace escape hatch).
    opts = {} if ("loc" in kwargs or "bbox_to_anchor" in kwargs) else placements[where]
    return ax.legend(*args, **{**opts, **kwargs})


def _baked_titles(fig: "mpl.figure.Figure") -> list[str]:
    """Return any non-empty suptitle / Axes title baked into ``fig``.

    Captions belong in LaTeX ``\\caption{}``, not in the raster
    (ave-figure-discipline Axis 4). This finds the offenders.
    """
    offenders: list[str] = []
    sup = getattr(fig, "_suptitle", None)
    if sup is not None and sup.get_text().strip():
        offenders.append(f"suptitle: {sup.get_text().strip()!r}")
    for i, ax in enumerate(fig.axes):
        # A colorbar Axes legitimately carries a label via set_label, not a
        # title, so checking ax.get_title() is the right test here.
        title = ax.get_title().strip()
        if title:
            offenders.append(f"axes[{i}].title: {title!r}")
    return offenders


def save(
    fig: "mpl.figure.Figure",
    path,
    *,
    dpi: int = 200,
    formats: tuple[str, ...] = ("pdf", "png"),
    strict: bool = False,
) -> list[Path]:
    """Save ``fig`` to ``path`` in each requested format, on house defaults.

    Writes vector-preferred (PDF first) plus a raster PNG, with
    ``bbox_inches="tight"`` so nothing clips. If ``path`` carries a suffix it is
    stripped and replaced per-format (so ``save(fig, "x.png")`` still emits
    ``x.pdf`` + ``x.png``).

    Caption discipline (ave-figure-discipline Axis 4): a figure carrying a baked
    ``suptitle`` or Axes ``title`` is flagged — captions belong in the LaTeX
    ``\\caption{}``, not the raster. In default mode this is a ``warnings.warn``;
    with ``strict=True`` it raises ``AssertionError`` so a CI/driver gate can
    block the bad figure.

    Parameters
    ----------
    fig:
        The figure to save.
    path:
        Output path (``str`` or ``pathlib.Path``); any suffix is replaced
        per-format. Parent directory must exist (use ``ave_path_util.sim_output``
        / ``manuscript_path`` to resolve it).
    dpi:
        Raster DPI (default 200). PDF is vector and ignores this.
    formats:
        Iterable of extensions to write, default ``("pdf", "png")``.
    strict:
        If ``True``, raise on a baked title instead of warning.

    Returns
    -------
    list[pathlib.Path]
        The paths written, in ``formats`` order.
    """
    baked = _baked_titles(fig)
    if baked:
        msg = (
            "figure carries a baked title/suptitle — captions belong in the "
            "LaTeX \\caption{}, not the raster (ave-figure-discipline Axis 4): "
            + "; ".join(baked)
        )
        if strict:
            raise AssertionError(msg)
        warnings.warn(msg, stacklevel=2)

    base = Path(path)
    if base.suffix:
        base = base.with_suffix("")

    written: list[Path] = []
    for ext in formats:
        out = base.with_suffix(f".{ext.lstrip('.')}")
        # bbox_inches="tight" is belt-and-suspenders on top of constrained_layout
        # — guarantees no clip even if a driver disabled the layout engine.
        fig.savefig(out, dpi=dpi, bbox_inches="tight")
        written.append(out)
    return written
