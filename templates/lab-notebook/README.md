# AVE Engineering Notebook — LaTeX template

A lab-notebook / experimental walk-through template in the AVE visual
identity: a dotted **coordinate-node** writing grid and a logo that is the
real **diamond-cubic substrate lattice**, not a generic graph.

The mark is built from the engine's canonical bond vectors
(`src/ave/topological/cosserat_field_3d.py:129`, `TETRA_OFFSETS`):

```
(+1,+1,+1) (+1,-1,-1) (-1,+1,-1) (-1,-1,+1)
```

— coordination-4, four ⟨111⟩ bonds at 109.47° (sp³), viewed down a 2-fold
axis so all four bonds stay visible. Centre node = A-site; neighbours =
B-sublattice (bipartite). Palette is taken from the canonical substrate
render `assets/sim_outputs/lattice_structure_3d.png` and the manuscript
preamble: core-pink flux lines `#FF3366`, cyan nodes, near-black `#0F0F0F`.

## Files

| File | Purpose |
|---|---|
| `avenotebook.sty` | The package — all styling, logo, grid, macros |
| `notebook-demo.tex` / `.pdf` | Typeset walk-through (letter) — exercises every feature |
| `master-notebook.tex` / `.pdf` | Blank **A4+ master notebook** (Leuchtturm-style: numbered dotted pages, fill-in Contents, ownership page) |

There are two use modes: the **walk-through** (you typeset an experiment write-up,
`notebook-demo`) and the **blank master** (you print it and write by hand,
`master-notebook`). Both share `avenotebook.sty`.

## Requirements

A full TeX Live (MacTeX). Compiles with **pdflatex / xelatex / lualatex**
— no `fontspec`, so plain pdflatex is fine. Uses XCharter (body), Helvetica
(chrome), Inconsolata (data); all standard in TeX Live.

## Build

```bash
latexmk -pdf notebook-demo.tex      # or: pdflatex notebook-demo (×2, for page refs)
latexmk -pdf master-notebook.tex    # the blank A4+ master book
```

For the master book, set the page count at the top of `master-notebook.tex`
(`\def\NBPAGES{120}` — the real Leuchtturm Master is 233). Print double-sided,
long-edge bind.

## Options

```latex
\usepackage[<options>]{avenotebook}
```

| Option | Effect |
|---|---|
| *(none)* | Light "100 g paper" + 5 mm **square** dot grid |
| `dark` | Neon-on-black variant (the substrate-render look) |
| `iso` | Triangular / ⟨111⟩-projection dot grid |
| `a4plus` | Leuchtturm Master trim (225 × 315 mm), two-sided, outer page numbers |
| `border` | Thin lattice border box around the writing area |
| `nodots` | Suppress the dot grid |
| `plain` | No per-page header/footer chrome |

## Metadata

```latex
\notebookproject{...}  \notebookauthor{...}  \notebookid{...}  \notebookdate{...}
\experimentid{...}     % also set per-entry by \aveentry
```

## Macros

**Structure**
- `\avecover` — title page (uses the metadata above)
- `\aveentry{date}{exp-id}{title}` — dated entry banner
- Section heads: `\objective \hypothesis \apparatus \materials \procedure
  \observations \dataheading \analysis \conclusion` (or `\avehead{Custom}`)
- `\witnessblock` — end-of-entry recorded/witnessed sign-off

**Callouts** (environments)
- `averesult` (core-pink) · `avenote` (teal) · `avecaution` (orange)

**Data**
- `\meas{value}{unit}` · `\uncert{x}{dx}{unit}` — mono, math-safe
- `avedata` environment: `\begin{avedata}{<tabular colspec>} … \end{avedata}`
  with auto core-pink top/bottom rules; `\avedatahead{...}` for header cells
- `\plotframe[height]{caption}` — dashed placeholder to affix a print or
  `\includegraphics` a figure later

**Master notebook mode** (with `[a4plus]`, see `master-notebook.tex`)
- `\aveownership` — "this notebook belongs to / if found" page
- `\aveindex[pages]{rows-per-column}` — fill-in Contents (two columns of ruled lines)
- `\avedottedpages{n}` — `n` numbered blank dotted pages, `DATE`/`TOPIC` header + outer page number

**Logo (vector, recolourable, any size)**
- `\avebondstar[unit-pt]` — the coordination-4 bond-star (inline-safe)
- `\avelatticemark[unit-pt]` — larger diamond-lattice cell (cover hero)
- `\avelogo[unit-pt]` — bond-star + wordmark lockup
- `\avewordmark` — "AVE · APPLIED VACUUM ENGINEERING"

## Notes

- Light is the default because it's the surface you write/print on; `dark`
  is for covers and figure pages.
- The grid dots are the "Discrete Coordinate Nodes" — write over them.
- v0.1. Not yet wired into the Makefile; standalone for now.
