"""AVE visualization layer — the shared house figure style.

The single source of truth for manuscript / Vol-9 datasheet figure appearance.
Import the style API and apply it once per driver::

    from ave.viz import style
    style.apply()                       # white-background print profile (default)
    ...
    style.save(fig, sim_output("vol9", "fig"))   # writes fig.pdf + fig.png

Public API (re-exported from ``ave.viz.style``):

    apply       — set rcParams from the house stylesheet ("print" | "screen")
    COLORS      — semantic Okabe-Ito colourblind-safe palette dict
    REGIME_COLORS — four-regime band palette (I/II/III/IV), colourblind-safe
    CMAP_SEQ    — sequential field colormap ("magma")
    CMAP_DIV    — diverging / signed field colormap ("RdBu_r")
    axis_label  — canonical "Quantity $symbol$ [unit]" label string
    save        — vector-preferred save (PDF + PNG, bbox tight, title-discipline)
    figsize     — standard column-size presets ("single"/"double"/"wide"/"square")
    legend      — place a legend OUTSIDE the axes (never overlaps the data)

This is a presentation-tier package: NO dependency on the engine (``ave.core``),
changes only how figures look — never what they show.
"""

from ave.viz.style import (
    CMAP_DIV,
    CMAP_SEQ,
    COLORS,
    REGIME_COLORS,
    apply,
    axis_label,
    figsize,
    legend,
    save,
)

__all__ = [
    "apply",
    "COLORS",
    "REGIME_COLORS",
    "CMAP_SEQ",
    "CMAP_DIV",
    "axis_label",
    "save",
    "figsize",
    "legend",
]
