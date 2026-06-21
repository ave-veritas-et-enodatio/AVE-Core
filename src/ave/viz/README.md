# `ave.viz` — the shared AVE house figure style

The single source of truth for manuscript / Vol-9 datasheet figure appearance.
"Follow the house style" is now a mechanical `style.apply()` call, not a
per-driver checklist. This mechanizes the HOUSE-STYLE axis of
`~/.claude/skills/ave-figure-discipline/SKILL.md` (the OPEN INFRA GAP it flags).

## How a driver adopts it

```python
import matplotlib.pyplot as plt
from ave.viz import style
from ave_path_util import sim_output

style.apply()                 # white-background "print" profile (the default)

fig, ax = plt.subplots(figsize=style.figsize("single"))
ax.plot(x, y_ave, color=style.COLORS["ave"], linestyle="-",  label="AVE")
ax.plot(x, y_sm,  color=style.COLORS["comparison"], linestyle="--", label="Standard physics")
ax.plot(x, y_obs, color=style.COLORS["data"], linestyle="none", marker="o", label="Data")
ax.set_xlabel(style.axis_label("Frequency", "f", "Hz"))
ax.set_ylabel(style.axis_label("Reflection", r"|S_{11}|", "dimensionless"))
ax.legend()

style.save(fig, sim_output("vol9", "my_figure"))   # writes my_figure.pdf + .png
```

That is the whole contract. Do **not** hand-set `figsize`, `dpi`, facecolor,
font, or `plt.style.use("dark_background")` in the driver — those now live in
exactly one place.

## API

| Symbol | What it does |
|---|---|
| `apply(profile="print")` | Set rcParams from the house stylesheet. `"print"` = white bg / black text (manuscript default). `"screen"` = dark bg (interactive / field-viz). |
| `COLORS` | Semantic Okabe-Ito colourblind-safe palette: `ave` (blue), `comparison` (vermillion — SM/QED overlay), `data` (black points), `accent` (bluish-green), `muted` (gray). |
| `CMAP_SEQ` | Sequential / one-sided field colormap (`magma`). Retires `hot`. |
| `CMAP_DIV` | Diverging / signed field colormap (`RdBu_r`). Use zero-centred `vmin=-v, vmax=v`. |
| `axis_label(quantity, symbol, unit)` | Canonical `"Quantity $symbol$ [unit]"` string. Empty unit → `[dimensionless]`. A unit that is itself math (e.g. `ℓ_node`) must be passed pre-wrapped in `$...$` — plain-text units like `Hz` stay literal. |
| `figsize(kind="single")` | Column-size preset: `single` / `double` / `wide` / `square`. |
| `save(fig, path, *, dpi=200, formats=("pdf","png"), strict=False)` | Vector-preferred save (PDF + PNG, `bbox_inches="tight"`). **Warns** (or, with `strict=True`, asserts) if the figure carries a baked suptitle/Axes-title — captions belong in the LaTeX `\caption{}`, not the raster. |

## Two profiles, one palette

`apply("print")` is the default because the corpus had drifted to 30×
`dark_background` rasters shipping into a print manuscript. `apply("screen")`
preserves the dark field-viz aesthetic for interactive work — it layers
background/text overrides on the same base, so the palette, fonts, and layout
stay identical between the two.

## Palette is Grant-ratifiable

The colours in `COLORS` and the colormap choices are the **proposed** defaults
(the standard Okabe-Ito colourblind-safe set). They live in one Python dict in
`style.py` so re-tuning the whole corpus is a one-line edit. Grant ratifies or
adjusts.

## Where things live

- `style.py` — the API (palette, presets, profiles, save).
- `ave.mplstyle` — the matplotlib rcParams stylesheet (print profile base).
- `../../tests/test_viz_style.py` — the contract test.
- `../../scripts/viz/style_demo.py` — a 3-panel demo render that is the
  module's proof-of-correctness (run it, open the PNG, check the five axes).

This package is presentation-tier: **no** dependency on the engine (`ave.core`).
It changes how figures look, never what they show.
