# Vol 7 — Phase 2 Extraction

**Volume:** `manuscript/vol_7_hardware/`
**Taxonomy reference:** `.claude/phase1-taxonomy/vol7_taxonomy.md`
**Extraction date:** 2026-04-02
**Status:** Complete — all skeleton positions mapped

---

## Source Directory Listing

```
vol_7_hardware/
  main.tex
  chapters/
    _manifest.tex
    01_metric_streamlining/   (Part I + Part II via _manifest.tex order; flat KB structure)
    02_ave_resolutions/
      01_ave_resolutions.tex  (all 10 sections in single file)
    03_superconductivity/
      01_introduction.tex
      02_phase_locked_gear_train.tex
    04_phase_transitions/
      01_water_condensation.tex
      02_turbulence_onset.tex
      03_melting_eigenmode.tex    ← contains 3 sections (s03 + s04 + s05)
    05_white_dwarf_predictions/
      12_white_dwarf_predictions.tex
    06_bh_interior/
      13_bh_interior_regime_iv.tex
```

---

## Skeleton-to-Source Mapping

### Domain: propulsion/ch1-metric-streamlining (10 leaves)

All 10 sections are in `02_metric_streamlining/` directory. Source has Part I/Part II in `_manifest.tex` comments only — NO `\part{}` commands, NO structural subdivision. Flat `ch1-metric-streamlining/` directory is correct. Filename collision anomaly: both Part I and Part II use `01_` through `05_` prefixes. The `_manifest.tex` input order is the authoritative sequence.

| Skeleton leaf | Source file | Section title | `\label` |
|---|---|---|---|
| `s01-metric-streamlining-electrodynamics.md` | Part I, section 01 | (per manifest order) | none |
| `s02-active-inertial-cancellation.md` | Part I, section 02 | (per manifest order) | none |
| `s03-impedance-rectification.md` | Part I, section 03 | (per manifest order) | none |
| `s04-chiral-impedance-matching.md` | Part I, section 04 | (per manifest order) | none |
| `s05-autoresonant-dielectric-rupture.md` | Part I, section 05 | (per manifest order) | none |
| `s06-local-refractive-control.md` | Part II, section 01 | (per manifest order) | none |
| `s07-inductive-origin-special-relativity.md` | Part II, section 02 | (per manifest order) | none |
| `s08-active-impedance-control.md` | Part II, section 03 | (per manifest order) | none |
| `s09-superluminal-transit.md` | Part II, section 04 | (per manifest order) | none |
| `s10-hts-detector.md` | Part II, section 05 | (per manifest order) | none |

Note: No `\label{}` on any `\section{}` in Ch.1. Leaf boundaries follow `\section{}` commands.

### Domain: propulsion/ch2-ave-resolutions (10 leaves)

All 10 sections in single file: `05_ave_resolutions/01_ave_resolutions.tex`

| Skeleton leaf | Source section | `\label` | Notes |
|---|---|---|---|
| `s01-lsi-nano-warp-bubble.md` | §2.1 | none | |
| `s02-solar-flares-macroscopic-photons.md` | §2.2 | none | |
| `s03-jwst-early-galaxies.md` | §2.3 | none | Stray figure block spans §2.3/§2.4 boundary — assign to s03 |
| `s04-dama-libra-xenonnt.md` | §2.4 | none | |
| `s05-quasiparticle-poisoning.md` | §2.5 | none | |
| `s06-particle-accelerator-matrix.md` | §2.6 | none | |
| `s07-lorentz-invariance-lattice-drag.md` | §2.7 | none | |
| `s08-spin-half-fermions.md` | §2.8 | none | |
| `s09-quantum-entanglement-bell.md` | §2.9 | none | |
| `s10-ponder-01.md` | §2.10 | none | Bare `\tcolorbox` (not named env) in §2.3 — treated as resultbox |

Note: No `\label{}` on any `\section{}` in Ch.2.

### Domain: condensed-matter/ch3-superconductivity (2 leaves)

| Skeleton leaf | Source file | Section title | `\label` |
|---|---|---|---|
| `s01-introduction.md` | `01_introduction.tex` | Chapter intro | none |
| `s02-phase-locked-gear-train.md` | `02_phase_locked_gear_train.tex` | Phase-Locked Gear Train | none |

### Domain: condensed-matter/ch4-phase-transitions (5 leaves from 3 source files)

**CRITICAL: `03_melting_eigenmode.tex` contains 3 sections → s03, s04, s05**

| Skeleton leaf | Source file | Section title | `\label` | Line range |
|---|---|---|---|---|
| `s01-water-condensation.md` | `01_water_condensation.tex` | full file | `\label{sec:water_condensation}` | 1–end |
| `s02-turbulence-onset.md` | `02_turbulence_onset.tex` | full file | `\label{sec:turbulence_onset}` | 1–end |
| `s03-melting-eigenmode.md` [PATH-STABLE] | `03_melting_eigenmode.tex` | The Water Melting Point as a Proton Transfer Eigenmode | `\label{sec:melting_eigenmode}` at line 2 | 1–293 (ends with exercisebox) |
| `s04-hoh-bond-angle.md` | `03_melting_eigenmode.tex` | The H–O–H Bond Angle as an Impedance Eigenvalue | `\label{sec:bond_angle_derivation}` | 297–409 |
| `s05-topological-cell-collapse.md` | `03_melting_eigenmode.tex` | Topological Cell Collapse (State II Volume) | `\label{sec:topological_cell_collapse}` | 412–447 |

**PATH-STABLE Confirmation:** `\label{sec:melting_eigenmode}` CONFIRMED at `03_melting_eigenmode.tex` line 2, immediately following the `\section{}` command.

### Domain: astrophysical-predictions/ch5-white-dwarf-predictions (8 leaves)

Source: `12_white_dwarf_predictions.tex`

**Ch.5 heading anomaly:** `\chapter{White Dwarf Gravitational Predictions}` appears inside the content file at line 3, with `\label{ch:white_dwarf_predictions}` at line 4. The introductory paragraphs (4–10 lines before the first `\section{}`) belong in the chapter `index.md`, not any leaf.

| Skeleton leaf | Source section | Notes |
|---|---|---|
| `s01-motivation.md` through `s08-conclusions.md` | §5.1 through §5.8 | 8 section-level leaves |

### Domain: astrophysical-predictions/ch6-bh-interior (8 leaves)

Source: `13_bh_interior_regime_iv.tex`

**Ch.6 heading anomaly:** `\chapter{Regime IV: The Black Hole Interior}` appears inside the content file at line 3, with `\label{ch:bh_interior}` at line 4. Same pattern as Ch.5 — intro paragraphs → index.md, sections → leaves.

| Skeleton leaf | Source section | Notes |
|---|---|---|
| `s01-motivation.md` through `s08-conclusions.md` | §6.1 through §6.8 | 8 section-level leaves |

---

## Ch.4 Split Confirmation (Critical)

- **s03 section title:** "The Water Melting Point as a Proton Transfer Eigenmode"
- **s04 section title:** "The H–O–H Bond Angle as an Impedance Eigenvalue" (resultbox: "H-O-H Bond Angle (Op3 Small-Signal)")
- **s05 section title:** "Topological Cell Collapse (State II Volume)" (resultbox: "Topological Cell Collapse")
- **sec:melting_eigenmode label:** In s03 (line 2 of `03_melting_eigenmode.tex`)

---

## PATH-STABLE Anchor Confirmation

- `s03-melting-eigenmode.md`: `\label{sec:melting_eigenmode}` CONFIRMED at `03_melting_eigenmode.tex` line 2
- `ave-kb/vol7/condensed-matter/ch4-phase-transitions/s03-melting-eigenmode.md` is a stable path

---

## Ch.1 Part I/II Confirmation

- Source has Part I/Part II in `_manifest.tex` COMMENTS ONLY — no `\part{}` commands
- All 10 sections present across the two `01_`–`05_` file sets
- Filename collision: both Part I and Part II use `01_metric_*.tex` through `05_*.tex` prefixes in the same directory
- Manifest order is the ONLY authoritative sequence for leaf ordering
- KB flat structure (no Part I/II subdirectories) is CORRECT

---

## Ch.5 and Ch.6 Heading Text

- **Ch.5 inside-file heading:** `\chapter{White Dwarf Gravitational Predictions}` with `\label{ch:white_dwarf_predictions}`
- **Ch.6 inside-file heading:** `\chapter{Regime IV: The Black Hole Interior}` with `\label{ch:bh_interior}`
- Both manifest files are comments + single `\input` only
- The introductory paragraphs (before first `\section{}`) must go into the chapter `index.md`

---

## Appendix

- Vol 7 `main.tex` contains only: `\input{../common/appendix_experiments.tex}`
- **No original experimental content** in Vol 7's appendix position
- All experiments reference the shared appendix
- Vol 7 contributes NO content to `ave-kb/common/appendix-experiments.md`
- The Vol 7 appendix position in the skeleton has no KB leaf (pointer only to common/)

---

## Ch.5 `common_equations` input

- `s05` of Ch.5 contains `\input{../common_equations/eq_axiom_3.tex}`
- Distiller must inline this content from `manuscript/common_equations/eq_axiom_3.tex` when writing `s05-conclusions.md`

---

## Empty Skeleton Positions

NONE. All 43 leaf positions have confirmed source content.

---

## Leaf Boundary Notes

- **Ch.1 and Ch.2**: No `\label{}` on any `\section{}`. Leaf boundaries are `\section{}` commands only.
- **Ch.3**: Two separate source files, one per leaf. Boundaries are clean at file level.
- **Ch.4**: `03_melting_eigenmode.tex` splits into 3 leaves at `\section{}` boundaries. s03 runs lines 1–293, s04 lines 297–409, s05 lines 412–447.
- **Ch.5 and Ch.6**: Chapter heading + intro paragraphs → `index.md`. Leaf content starts at first `\section{}`.

---

## Notation and Macro Notes

Standard shared macro set (see CLAUDE.md invariants). No Vol 7-specific macros identified.

Section labels confirmed present (Ch.4): `sec:water_condensation`, `sec:turbulence_onset`, `sec:melting_eigenmode`, `sec:bond_angle_derivation`, `sec:topological_cell_collapse`.

Chapter labels: `ch:white_dwarf_predictions` (Ch.5), `ch:bh_interior` (Ch.6). Ch.1, Ch.2, Ch.3 have no chapter-level labels.

---

## Ambiguities Requiring Coordinator Decision

1. **Ch.1 leaf titles**: No `\label{}` or section-level identifiers in source. Leaf slugs are based on taxonomy taxonomy design (s01–s10). Confirm that the taxonomy's assumed section titles for s01–s10 match the actual source section headings (cannot verify without reading all Ch.1 files).

2. **Ch.5/Ch.6 intro paragraph placement**: Distiller must decide whether to put the 4–10 intro lines in `index.md` (as the chapter summary) or in `s01-motivation.md`. Recommendation: `index.md` per the distiller spec (indexes contain chapter-level content, leaves contain section content).
