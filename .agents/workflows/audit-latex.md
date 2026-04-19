---
description: Audit all LaTeX files for formatting, structure, and hygiene
---

# LaTeX Audit Workflow

Audit all `.tex` files in `manuscript/`, `future_work/`, `spice_manual/`, and `periodic_table/` for formatting, structural consistency, document architecture, prose style, and figure quality.

> **Before starting:** Read `LIVING_REFERENCE.md` to load the canonical axioms, constants, and project conventions.

## Scope

Search for all `.tex` files across:
- `manuscript/` (7 books, backmatter, frontmatter, common_equations, structure)
- `future_work/`
- `spice_manual/`
- `periodic_table/`

---

## Checks

### 1. Document Architecture (Single Source of Truth)

Each book's `main.tex` must reference shared infrastructure — the **only** per-book items are `\documentclass`, `\graphicspath`, and document structure (`\begin{document}` ... `\end{document}` with `\input{}` calls to frontmatter/chapters/backmatter).

#### Canonical `main.tex` structure
```latex
\documentclass[11pt, letterpaper, openright]{book}
\input{../structure/preamble.tex}       % All \usepackage declarations
\graphicspath{{../../assets/}{...}}      % Book-specific paths
\input{../structure/commands.tex}        % All custom commands + box styles
\begin{document}
  ...
\end{document}
```

For standalone builds outside `manuscript/` (e.g., `spice_manual/`, `future_work/`):
```latex
\input{../manuscript/structure/preamble.tex}
\input{../manuscript/structure/commands.tex}
```

#### Checklist
- [ ] **Preamble**: All builds use `\input{../structure/preamble.tex}` (or `../manuscript/structure/preamble.tex` for standalone builds). Flag any `\usepackage` lines in `main.tex`.
- [ ] **Custom commands**: All commands (`\vacuum`, `\impedance`, `\slew`, `\planck`, `\permeability`, `\permittivity`, `\Lvac`, `\Cvac`, `\Zvac`, `\Wcut`, `\lp`) must be defined ONLY in `commands.tex` using `\providecommand`. Flag any `\newcommand` in `main.tex`.
- [ ] **tcolorbox styles**: 5 canonical styles are defined in `commands.tex`:
  - `axiombox` / `axiom` — Blue, for Vacuum Engineering postulates
  - `simbox` — Green, for computational module results
  - `resultbox` — Black frame on white, for key derived results
  - `circuitbox` — Light grey, for circuit diagrams
  - `codebox` — Dark terminal, for SPICE netlists / code listings
  Flag any inline `\begin{tcolorbox}[...]` that duplicates these styles instead of using the named environments.
- [ ] **Foreword**: All books should `\input{../frontmatter/00_foreword.tex}` — the same shared foreword. Check for books with a local foreword copy.
- [ ] **Backmatter**: All books should reference `../backmatter/*.tex` files — never contain local copies of appendices.
- [ ] **Common equations**: The 4 axioms and key shared equations must come from `common_equations/eq_axiom_*.tex` via `\input{}`. Flag any book that types axioms inline.
- [ ] **`\graphicspath`**: The only per-book element. Verify paths point to `../../assets/` and its subdirectories. Flag missing or broken paths.
- [ ] **No `variables.tex`**: This file has been deleted (was dead/stale). Flag any `\input{variables.tex}`.

### 2. Prose Style (Engineering Textbook Tone)

The manuscript must read like a professional engineering textbook: neutral, precise, third-person, present-tense for established results.

- [ ] **No first person**: Flag any use of "I", "we", "our", "my" (except in quoted material or acknowledgments). Use "the framework", "this analysis", "the solver" instead.
- [ ] **No casual language**: Flag colloquialisms, exclamation marks (!), rhetorical questions, hyperbole ("amazingly", "incredibly", "shockingly"), or editorializing ("beautiful", "elegant").
- [ ] **No marketing language**: Flag promotional phrases ("revolutionary", "groundbreaking", "paradigm-shifting", "unprecedented").
- [ ] **Neutral declarative tone**: Statements should be factual declarations. Instead of "This stunningly shows that...", use "This demonstrates that...".
- [ ] **Consistent tense**: Present tense for established theory ("The saturation kernel bounds..."), past tense for experimental results ("The simulation produced...").
- [ ] **No acronym on first use without definition**: Every acronym must be defined on first use in each book (e.g., "Applied Vacuum Engineering (AVE)").
- [ ] **Precise language**: Physical claims should include quantitative precision (e.g., "within 0.3% of the PDG value" not "very close to the measured value").

### 3. Label and Reference Integrity

- [ ] Every `\label{...}` is referenced by at least one `\ref{...}`, `\eqref{...}`, or `\autoref{...}`
- [ ] Every `\ref{...}`, `\eqref{...}`, and `\autoref{...}` has a corresponding `\label{...}`
- [ ] No duplicate labels across files
- [ ] Labels follow a consistent naming convention (`eq:`, `fig:`, `tab:`, `ch:`, `sec:`)

### 4. Figure and Table Environments

- [ ] Every `\begin{figure}` has a `\caption{...}` with non-empty content
- [ ] Every `\begin{table}` has a `\caption{...}` with non-empty content
- [ ] Every figure/table has a `\label{...}` inside the environment
- [ ] Figures use `[H]`, `[h]`, `[h!]`, or `[htbp]` placement — no bare `\begin{figure}` without placement spec
- [ ] Captions are descriptive and engineering-grade (state what the figure shows, the key result, and the generating script if applicable)

### 5. Figure Output Verification

For each figure referenced in the manuscript, verify the output is publication-quality:

- [ ] **Locate the source**: For each `\includegraphics{filename}` or figure environment, find the generating script in `src/scripts/` (search by filename or caption keywords)
- [ ] **Run the script**: Execute the generating script with `python <script>` to regenerate the figure
- [ ] **Inspect the output**: View the generated figure and check:
  - All axes have labels with units (e.g., "Frequency [GHz]", "Voltage [kV]")
  - All axes have tick marks with legible numbers
  - No clipping or cropping issues (data not cut off at plot boundaries)
  - Legend is present and readable (if multiple traces)
  - Title is present (or caption is sufficient)
  - Color scheme is colorblind-accessible (avoid red-green only)
  - Font sizes are legible at print scale
  - No matplotlib default styling that looks unprofessional (use clean, publication-ready styles)
- [ ] **Value verification**: Check that key numeric values displayed in the figure match `constants.py`:
  - Axis limits make physical sense
  - Annotated values (threshold lines, markers) use canonical constants
  - No stale values from old theory versions
- [ ] **Caption-figure agreement**: Verify the caption accurately describes what the figure actually shows (not a stale caption from a previous version of the figure)

### 6. Heading Hierarchy

- [ ] No heading level skips: `\chapter` → `\section` → `\subsection` → `\subsubsection`
- [ ] Each book's `main.tex` has a clear chapter structure
- [ ] `_manifest.tex` files include all chapter files in correct order
- [ ] Chapter numbering across books is consistent (no duplicate chapter numbers)

### 7. Shared Equation Usage

- [ ] The 4 axioms are stated via `\input{...common_equations/eq_axiom_*.tex}` — never re-typed inline
- [ ] `eq_saturation_observables.tex` and `eq_universal_operators.tex` used where relevant
- [ ] Any chapter that formally states an axiom does so by `\input{}`-ing the canonical file

### 8. Typography and Formatting

- [ ] No Markdown artifacts in LaTeX (`**bold**` instead of `\textbf{}`)
- [ ] Code/module names use `\texttt{...}` consistently
- [ ] Math symbols in `$...$` or appropriate environments
- [ ] Units formatted consistently (`\SI{43.65}{kV}` or `$43.65\,\text{kV}$` — no bare numbers)
- [ ] Greek letters use proper commands (`$\alpha$`, not "alpha")
- [ ] Equation environments properly terminated

### 9. Bibliography

- [ ] Every `\cite{...}` key exists in `manuscript/bibliography.bib`
- [ ] No broken citation references
- [ ] Custom `\citestart`/`\citeend` macros used consistently (if present)

### 10. Input Path Validation

- [ ] Every `\input{...}` path resolves to an existing file
- [ ] Every `\includegraphics{...}` resolves against the book's `\graphicspath`
- [ ] No hardcoded absolute paths in any `.tex` file

### 11. Engine Architecture Appendix Sync

- [ ] `manuscript/backmatter/04_physics_engine_architecture.tex` accurately lists all current modules in `src/ave/`
- [ ] Module names match actual filenames
- [ ] Function signatures in API tables match actual code
- [ ] Delegation flow examples are accurate

### 11a. Cross-Volume Reference Hygiene (xr-hyper)

Cross-volume `\ref{}` calls only resolve in standalone PDF builds if the target volume's `.aux` file is pulled in via `xr-hyper`. Volumes that cite another volume's labels MUST declare the dependency in their `main.tex`.

**Setup pattern (in `main.tex`, after `commands.tex` include, before `\begin{document}`):**
```latex
\usepackage{xr-hyper}
\IfFileExists{../../build/aux/vol_1_foundations.aux}{%
    \externaldocument{../../build/aux/vol_1_foundations}%
}{%
    \typeout{[xr-hyper] vol_1_foundations.aux not found — run `make vol1` first.}%
}
```

**Makefile dependency**: `vol0`, `vol2`, etc. that rely on Vol 1 labels must depend on `vol1` so the aux file is present at build time.

#### Checklist
- [ ] **Scan every standalone-built `main.tex`** for `\ref{}` calls to labels defined in *another* volume (grep the label name in the project and check which volumes define/consume it).
- [ ] **Any downstream volume citing Vol 1 labels** (e.g. `ch:alpha_golden_torus`, `sec:pi_squared_rigor`) must load `xr-hyper` and declare `\externaldocument{../../build/aux/vol_1_foundations}`. If it doesn't, the build will silently produce `??` in the PDF.
- [ ] **Shared backmatter files** (`manuscript/backmatter/*.tex`) that contain `\ref{}` to Vol 1 labels must be paired with xr-hyper setup in *every* volume's `main.tex` that `\input`s them. Currently: Vol 0 and Vol 2.
- [ ] **Verify resolution** by grepping the final-pass log for undefined references: `grep -E "undefined on input" build/aux/<vol>.log` must return zero lines after the last pdflatex pass (initial-pass warnings are fine).
- [ ] **Prose citations are a fallback, not the target state.** If a cross-volume cite is in prose form (`"see Vol.~1, Ch.~8 \textit{Zero-Parameter Closure}"` rather than `\ref{}`), treat it as a historical artifact from before xr-hyper was wired up and convert to `\ref{}`. The point of xr is that chapter numbers, page numbers, and hyperref links all stay accurate under chapter renumbering.

### 12. Chapter Content Completeness (Engineering Textbook Standard)

Every chapter should contain the elements expected in a professional engineering textbook:

- [ ] **Chapter objectives**: Opening paragraph clearly states what the chapter derives, proves, or demonstrates. No chapter should start without context.
- [ ] **Derivation completeness**: Flag any derivation gap — phrases like "it can be shown that", "it follows trivially", "the reader can verify", or jumps from axiom to result without intermediate algebra. Per project rules, **100% of each step must be shown**.
- [ ] **Dimensional analysis**: At key derivation steps, verify that units are tracked and balance. Flag any equation where a dimensional check would catch an error (e.g., adding quantities of different dimensions).
- [ ] **Theory vs. experiment comparison**: Every quantitative prediction should be accompanied by a comparison table or inline statement showing the predicted value, the measured/PDG value, and the percentage error (Δ%). Flag chapters with predictions that lack this.
- [ ] **End-of-chapter summary**: Each chapter should close with a brief summary of key results derived in that chapter. Flag chapters that end abruptly.
- [ ] **Cross-references**: Chapters that depend on results from other chapters should cite them explicitly (e.g., "As derived in §3.2..."). Flag isolated chapters that use results from elsewhere without citing the source chapter.
- [ ] **Boxed key results (`tcolorbox`)**: Major derived results (axioms, key equations, important theorems) should be highlighted in `tcolorbox` environments consistently across all chapters. Check:
  - Consistent styling: same `colframe`, `colback`, `title` formatting across all books
  - **No white title text**: Flag any `tcolorbox` using `coltitle=white` or white-on-dark title styling — titles must be legible in print
  - All 4 axiom boxes use the canonical `common_equations/eq_axiom_*.tex` source
  - Key derived results (sin²θ_W, proton mass, V_YIELD, etc.) are boxed when first derived
- [ ] **Notation consistency**: Variables introduced in a chapter are defined before or at first use. No undefined symbols appear in equations.

---

## Output

Produce a structured report with:
1. **ARCHITECTURE** — Duplicated preambles, divergent shared infrastructure
2. **STYLE** — Tone violations, casual language, first-person usage
3. **CONTENT** — Missing chapter bookends, derivation gaps, missing comparison tables, tcolorbox issues
4. **FIGURE** — Output quality issues, stale figures, caption mismatches
5. **CRITICAL** — Broken references, missing files, incorrect content
6. **WARNING** — Inconsistencies, style violations, stale references
7. **INFO** — Suggestions for improvement

For each finding, cite the specific file and line number.
