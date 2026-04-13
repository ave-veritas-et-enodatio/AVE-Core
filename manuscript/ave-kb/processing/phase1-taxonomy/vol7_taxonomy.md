# Phase 1 Taxonomy Design — Vol 7: Hardware & Future Work

**Designer:** kb-taxonomy-architect
**Source survey:** `.claude/phase0-surveys/vol7_survey.md`
**Output root:** `manuscript/ave-kb/`
**Volume root:** `manuscript/ave-kb/vol7/`

---

## 1. Invariants

These items are confirmed cross-cutting (apply uniformly across all volumes) and belong in
`manuscript/ave-kb/CLAUDE.md`. None are Vol 7-specific originations — all were either
established by other volumes or are shared-file content. Vol 7 introduces zero volume-specific
macros.

**INVARIANT: vacuum-macro-rendering** — Body text uses `$\mathcal{M}_A$` directly (not via
`\vacuum` macro); KB must render as `$\mathcal{M}_A$` throughout all volumes.
(Source: vol7 §3 Notation; confirmed in all 8 surveys)

**INVARIANT: dielectric-yield-limit** — $V_{\text{yield}} \approx 43.65\,\text{kV}$ defined in
Vol 4 Ch.1; referenced unqualified in Vol 7 Ch.1 and other volumes. When this value appears in
any KB document it must carry a cross-reference primary pointer to its Vol 4 definition.
(Source: vol7 §4 Cross-References)

**INVARIANT: chapter-number-refs-are-unqualified** — Vol 7 chapter-number cross-references
name no volume; distillers must resolve these to specific volume labels using the cross-volume
index before writing KB links.
(Source: vol7 §7 Anomaly 5)

**INVARIANT: shared-appendix** — `common/appendix_experiments.tex` (Unified Index of
Experimental Falsifications) is not owned by any single volume. Its KB representation lives at
`ave-kb/common/appendix-experiments.md`, referenced from each volume that includes it.
(Source: vol7 §1 Appendix A annotation)

**INVARIANT: tcolorbox-environments** — resultbox, axiombox, simbox, examplebox, summarybox,
exercisebox, circuitbox, codebox, objectivebox render as named Markdown blockquotes with bold
environment-type prefix. Convention applies across all volumes.
(Source: session-state coordinator note)

Note: Vol 7 does NOT introduce new invariants; it confirms existing ones. The invariant list
above is additive with what other volume taxonomists should be producing in parallel.

---

## 2. Structural Decisions

### 2a. Chapter count and anomaly resolutions

Vol 7 has **6 chapters** plus 1 shared appendix. The appendix is excluded from the vol7
hierarchy (it belongs in `ave-kb/common/`).

**Ch.1 dual-part anomaly**: The 10 sections (§1.1–§1.10) are flat peers in the LaTeX; the
Part I/Part II division exists only in comments. Do NOT create subtopic sub-directories for
Part I vs Part II — this would impose a false structural split. Keep all Ch.1 leaves in a
single `ch1-metric-streamlining/` directory.

**`03_melting_eigenmode.tex` multi-section anomaly**: This single source file contains three
distinct `\section{}` blocks (§4.3, §4.4, §4.5). The distiller must extract each section
independently and write them as separate leaf files. Do not treat the file as one leaf.

**Ch.5 and Ch.6 chapter-heading-inside-file anomaly**: Both chapters carry their own `\chapter{}`
heading inside the content file (not in a manifest wrapper). This has no effect on hierarchy
design but distillers must know the heading is present and must not double-render it.

### 2b. Domain grouping

Three natural content domains emerge from the chapter structure. The grouping is
thematic, not just sequential, because Ch.2 (precision crises) is logically an extension
of Ch.1's propulsion physics (same instruments and phenomena, different context).

| Domain slug | Chapters | Rationale |
|---|---|---|
| `propulsion` | Ch.1, Ch.2 | Metric streamlining, warp mechanics, experimental falsifications; both chapters concern active manipulation of the vacuum impedance for transit/propulsion and the precision experiments that test those predictions |
| `condensed-matter` | Ch.3, Ch.4 | Superconductivity, phase transitions, regime crossings; both chapters apply AVE to emergent many-body phenomena |
| `astrophysical-predictions` | Ch.5, Ch.6 | White dwarf and black hole interior predictions; both chapters structure the same derivation template (LC analogs → strain → operators → predictions → testability) |

**Depth**: 4 levels maximum (entry-point → volume → domain → chapter → leaf). With 6 chapters
and 43-49 estimated leaves, a 4-level structure is correct. No fifth level needed.

---

## 3. Document Skeleton

Leaf documents are marked `[leaf — verbatim]`. Index documents are marked `[index]`.
Source locations given as `[source: Ch.N §N.N label]`.

```
ave-kb/
  CLAUDE.md                                           [index] — cross-cutting notation, macro
                                                               rendering rules, environment
                                                               conventions; confirmed invariants
                                                               from all 8 volumes
  entry-point.md                                      [index] — top-level navigation anchor;
                                                               one-paragraph summary per volume,
                                                               link to each vol index; <3000 tokens

  common/
    appendix-experiments.md                           [leaf — verbatim] — shared Unified Index
                                                               of Experimental Falsifications
                                                               (source: common/appendix_experiments.tex)

  vol7/
    index.md                                          [index] — Vol 7 overview: 6 chapters,
                                                               3 domains; Key Results from all
                                                               chapters surfaced; links to 3
                                                               domain indexes

    propulsion/
      index.md                                        [index] — domain summary: metric
                                                               streamlining, warp mechanics,
                                                               precision-crisis resolutions;
                                                               Key Results from Ch.1 and Ch.2

      ch1-metric-streamlining/
        index.md                                      [index] — Ch.1 summary: 10 sections,
                                                               §1.1–§1.10; Key Results surfaced;
                                                               links to all leaves
                                                               [label: ch:metric_streamlining]

        s01-metric-streamlining-electrodynamics.md   [leaf — verbatim] — §1.1 + §1.1.1–§1.1.2:
                                                               Metric Streamlining and Vacuum
                                                               Electrodynamics, inductive
                                                               saturation, superluminal inductive
                                                               solitons
                                                               [source: Ch.1 §1.1,
                                                               01_metric_stream_lining.tex]

        s02-active-inertial-cancellation.md          [leaf — verbatim] — §1.2: Active Inertial
                                                               Cancellation; CEMF/vector potential
                                                               injection
                                                               [source: Ch.1 §1.2,
                                                               02_active_inertial_cancellation.tex]

        s03-impedance-rectification.md               [leaf — verbatim] — §1.3: Impedance
                                                               Rectification in Non-Linear
                                                               Dielectrics; asymmetric flyback
                                                               thrust
                                                               [source: Ch.1 §1.3,
                                                               03_acoustic_rectification.tex]

        s04-chiral-impedance-matching.md             [leaf — verbatim] — §1.4: Chiral Impedance
                                                               Matching, helicity injection,
                                                               Hopf coil design
                                                               [source: Ch.1 §1.4,
                                                               04_chiral_impedance_matching.tex]

        s05-autoresonant-dielectric-rupture.md       [leaf — verbatim] — §1.5: Autoresonant
                                                               Dielectric Rupture; PLL vacuum
                                                               rupture mechanism
                                                               [source: Ch.1 §1.5,
                                                               05_autoresonant_dielectric_rupture.tex]

        s06-local-refractive-control.md              [leaf — verbatim] — §1.6 + §1.6.1:
                                                               Principle of Local Refractive
                                                               Control; trace-reversed strain
                                                               tensors; modulating n
                                                               [source: Ch.1 §1.6,
                                                               01_local_refractive_control.tex]

        s07-inductive-origin-special-relativity.md  [leaf — verbatim] — §1.7 + §1.7.1:
                                                               Inductive Origin of Special
                                                               Relativity; dielectric saturation
                                                               singularity
                                                               [source: Ch.1 §1.7,
                                                               02_mechanical_origin.tex]

        s08-active-impedance-control.md              [leaf — verbatim] — §1.8 + §1.8.1–§1.8.2:
                                                               Metric Streamlining Active
                                                               Impedance Control; dimensionally
                                                               exact origin of inertia; evading
                                                               saturation singularity
                                                               [source: Ch.1 §1.8,
                                                               03_active_flow_control.tex]

        s09-superluminal-transit.md                  [leaf — verbatim] — §1.9 + §1.9.1–§1.9.3:
                                                               Superluminal Transit warp
                                                               mechanics; trace-reversed impedance
                                                               dipole; vacuum impedance boom;
                                                               nested subluminal sleep pods
                                                               [source: Ch.1 §1.9,
                                                               04_superluminal_transit.tex]

        s10-hts-detector.md                          [leaf — verbatim] — §1.10 + §1.10.1:
                                                               Laboratory Falsification HTS
                                                               Detector; kinetic inductance
                                                               prediction
                                                               [source: Ch.1 §1.10,
                                                               05_hts_detector.tex]

      ch2-ave-resolutions/
        index.md                                      [index] — Ch.2 summary: 10 precision-crisis
                                                               resolutions; Key Results surfaced;
                                                               links to all leaves
                                                               [label: ch:ave_resolutions]

        s01-lsi-nano-warp-bubble.md                  [leaf — verbatim] — §2.1: LSI "Nano-Warp
                                                               Bubble" (Dr. Sonny White, 2021);
                                                               falsification context
                                                               [source: Ch.2 §2.1]

        s02-solar-flares-macroscopic-photons.md      [leaf — verbatim] — §2.2 + §2.2.1: Solar
                                                               Flares as Macroscopic Photons;
                                                               scale invariance; macroscopic
                                                               avalanche diode prediction
                                                               [source: Ch.2 §2.2]

        s03-jwst-early-galaxies.md                   [leaf — verbatim] — §2.3: JWST "Impossible"
                                                               Early Galaxies; highly-reluctant
                                                               correction mechanism
                                                               [source: Ch.2 §2.3]

        s04-dama-libra-xenonnt.md                    [leaf — verbatim] — §2.4: DAMA/LIBRA vs
                                                               XENONnT Paradox resolution
                                                               [source: Ch.2 §2.4]

        s05-quasiparticle-poisoning.md               [leaf — verbatim] — §2.5: Quantum Computing
                                                               Quasiparticle Poisoning resolution
                                                               [source: Ch.2 §2.5]

        s06-particle-accelerator-matrix.md           [leaf — verbatim] — §2.6: Particle
                                                               Accelerator Matrix Paradox; LHC vs
                                                               Tokamak
                                                               [source: Ch.2 §2.6]

        s07-lorentz-invariance-lattice-drag.md       [leaf — verbatim] — §2.7: Lorentz Invariance
                                                               vs Discrete Lattice Drag resolution
                                                               [source: Ch.2 §2.7]

        s08-spin-half-fermions.md                    [leaf — verbatim] — §2.8: Deriving Quantum
                                                               Spin-1/2 Fermions from Classical
                                                               Nodes; Möbius topology
                                                               [source: Ch.2 §2.8]

        s09-quantum-entanglement-bell.md             [leaf — verbatim] — §2.9: Quantum
                                                               Entanglement and Bell's Theorem;
                                                               longitudinal wave interpretation
                                                               [source: Ch.2 §2.9]

        s10-ponder-01.md                             [leaf — verbatim] — §2.10: PONDER-01 and
                                                               Conservation of Momentum
                                                               [source: Ch.2 §2.10]

    condensed-matter/
      index.md                                        [index] — domain summary: superconductivity
                                                               as phase-lock, phase transitions as
                                                               regime crossings; Key Results from
                                                               Ch.3 and Ch.4 including melting
                                                               eigenmode and HOH bond angle results

      ch3-superconductivity/
        index.md                                      [index] — Ch.3 summary: phase-locked gear
                                                               train model; Meissner effect;
                                                               Casimir superconductivity; links to
                                                               leaves [label: ch:superconductivity]

        s01-introduction.md                          [leaf — verbatim] — §3.1: Introduction to
                                                               superconductivity chapter
                                                               [source: Ch.3 §3.1,
                                                               00_intro.tex]

        s02-phase-locked-gear-train.md               [leaf — verbatim] — §3.2 + §3.2.1–§3.2.3:
                                                               Superconductivity as Phase-Locked
                                                               Gear Train; topological flywheel
                                                               lattice; mechanical derivation of
                                                               Meissner effect; room-temperature
                                                               Casimir superconductivity;
                                                               Kuramoto phase-lock
                                                               [source: Ch.3 §3.2,
                                                               01_phase_locked_meissner.tex]

      ch4-phase-transitions/
        index.md                                      [index] — Ch.4 summary: 5 sections covering
                                                               water condensation, turbulence,
                                                               melting eigenmode, HOH bond angle,
                                                               topological cell collapse; all Key
                                                               Results and resultboxes surfaced;
                                                               links to all leaves
                                                               [label: ch:phase_transitions]

        s01-water-condensation.md                    [leaf — verbatim] — §4.1 + §4.1.1–§4.1.2:
                                                               Water Condensation as Macroscopic
                                                               Avalanche Breakdown; hypothesis and
                                                               testable prediction
                                                               [source: Ch.4 §4.1,
                                                               label: sec:water_condensation]

        s02-turbulence-onset.md                      [leaf — verbatim] — §4.2 + §4.2.1–§4.2.3:
                                                               Turbulence Onset as Regime I→II
                                                               Transition; mapping to fluid
                                                               variables; testable prediction
                                                               [source: Ch.4 §4.2,
                                                               label: sec:turbulence_onset]

        s03-melting-eigenmode.md                     [leaf — verbatim] — §4.3 §4.3.1–§4.3.9:
                                                               Water Melting Point as Proton
                                                               Transfer Eigenmode; 5-step
                                                               derivation; LC analogs, H-bond and
                                                               O-H spring constants, eigenfrequency,
                                                               numerical evaluation, lattice
                                                               loading, error analysis; summarybox;
                                                               exercisebox (5 exercises); key
                                                               equations eq:omega_m, eq:Tm_eigenmode
                                                               [source: Ch.4 §4.3,
                                                               03_melting_eigenmode.tex lines 1–N,
                                                               label: sec:melting_eigenmode]
                                                               *** PRIMARY CROSS-VOLUME TARGET:
                                                               Vol 3 references this label ***

        s04-hoh-bond-angle.md                        [leaf — verbatim] — §4.4 §4.4.1–§4.4.4:
                                                               H–O–H Bond Angle as Impedance
                                                               Eigenvalue; sp³ tetrahedral angle,
                                                               Op3 small-signal correction, Op8
                                                               large-signal confirmation;
                                                               resultbox "H–O–H Bond Angle (Op3
                                                               Small-Signal)"; equations
                                                               eq:theta_tet, eq:Gamma_OH,
                                                               eq:theta_HOH, eq:theta_HOH_large
                                                               [source: Ch.4 §4.4,
                                                               03_melting_eigenmode.tex,
                                                               label: sec:bond_angle_derivation]

        s05-topological-cell-collapse.md             [leaf — verbatim] — §4.5 §4.5.1–§4.5.3:
                                                               Topological Cell Collapse (State II
                                                               Volume); State I open lattice,
                                                               State II FCC maximal yield, water
                                                               density anomaly; resultbox
                                                               "Topological Cell Collapse (State II
                                                               Volume)"
                                                               [source: Ch.4 §4.5,
                                                               03_melting_eigenmode.tex,
                                                               label: sec:topological_cell_collapse]

    astrophysical-predictions/
      index.md                                        [index] — domain summary: white dwarf
                                                               gravitational predictions and black
                                                               hole interior regime; Key Results
                                                               from Ch.5 and Ch.6 surfaced

      ch5-white-dwarf-predictions/
        index.md                                      [index] — Ch.5 summary: Sirius B redshift,
                                                               WD shear eigenfrequencies; 6-step
                                                               derivation template; resultboxes
                                                               surfaced; links to leaves
                                                               [label: ch:white_dwarf_predictions]

        s01-motivation.md                            [leaf — verbatim] — §5.1: Motivation — Why
                                                               White Dwarfs?
                                                               [source: Ch.5 §5.1]

        s02-lc-analogs.md                            [leaf — verbatim] — §5.2: Step 1 — LC Analogs
                                                               for white dwarf interior
                                                               [source: Ch.5 §5.2]

        s03-strain-and-regime.md                     [leaf — verbatim] — §5.3: Step 2 — Strain
                                                               and Regime classification
                                                               [source: Ch.5 §5.3]

        s04-universal-operators-predictions.md       [leaf — verbatim] — §5.4 + §5.4.1–§5.4.2:
                                                               Step 3 — Universal Operators;
                                                               Prediction A (saturation correction
                                                               to gravitational redshift); Prediction
                                                               B (standing shear wave
                                                               eigenfrequencies); resultboxes
                                                               "Sirius B Redshift Comparison" and
                                                               "WD Shear Eigenfrequencies (l = 2)"
                                                               [source: Ch.5 §5.4]

        s05-symmetry-cancellations.md                [leaf — verbatim] — §5.5: Step 4 — Symmetry
                                                               Cancellations
                                                               [source: Ch.5 §5.5]

        s06-numerical-engine-validation.md           [leaf — verbatim] — §5.6: Step 5 — Numerical
                                                               Engine Validation
                                                               [source: Ch.5 §5.6]

        s07-testability.md                           [leaf — verbatim] — §5.7: Step 6 —
                                                               Testability
                                                               [source: Ch.5 §5.7]

        s08-conclusions.md                           [leaf — verbatim] — §5.8: Conclusions
                                                               [source: Ch.5 §5.8]

      ch6-bh-interior/
        index.md                                      [index] — Ch.6 summary: Regime IV BH
                                                               interior; 0·∞ LC limit; Regime IV
                                                               Isomorphism; resultboxes surfaced;
                                                               links to leaves
                                                               [label: ch:bh_interior]

        s01-motivation.md                            [leaf — verbatim] — §6.1: Motivation — The
                                                               Missing Regime
                                                               [source: Ch.6 §6.1]

        s02-lc-analogs.md                            [leaf — verbatim] — §6.2: Step 1 — LC Analogs
                                                               for BH interior; resultbox "The DC
                                                               Operating Point"
                                                               [source: Ch.6 §6.2]

        s03-strain-and-regime-profile.md             [leaf — verbatim] — §6.3: Step 2 — Strain
                                                               and Regime Profile
                                                               [source: Ch.6 §6.3]

        s04-zero-infinity-limit.md                   [leaf — verbatim] — §6.4: Step 3 — The 0·∞
                                                               Limit
                                                               [source: Ch.6 §6.4]

        s05-regime-iv-isomorphism.md                 [leaf — verbatim] — §6.5: Step 4 — Regime IV
                                                               Isomorphism; resultbox "Regime IV
                                                               Isomorphism Table"
                                                               [source: Ch.6 §6.5]

        s06-characteristic-scales.md                 [leaf — verbatim] — §6.6: Step 5 —
                                                               Characteristic Scales
                                                               [source: Ch.6 §6.6]

        s07-testability-predictions.md               [leaf — verbatim] — §6.7: Step 6 —
                                                               Testability and Predictions
                                                               [source: Ch.6 §6.7]

        s08-conclusions.md                           [leaf — verbatim] — §6.8: Conclusions
                                                               [source: Ch.6 §6.8]
```

---

## 4. File Count Summary

| Category | Count |
|---|---|
| Index files (vol7 scope) | 12 |
| Leaf files (vol7 scope) | 38 |
| Common scope files | 1 |
| **Vol 7 total (excl. common)** | **50** |

Index breakdown: vol7/index.md (1) + domain indexes (3) + chapter indexes (6) + chapter-level
subtopic indexes (0, not needed at this depth) = 10 structural indexes + entry-point.md (1) +
CLAUDE.md (1) = 12 total index files touching vol7 content.

Leaf breakdown by chapter:
- Ch.1: 10 leaves
- Ch.2: 10 leaves
- Ch.3: 2 leaves
- Ch.4: 5 leaves (from 3 source sections in one file + 2 others)
- Ch.5: 8 leaves
- Ch.6: 8 leaves
Total: 43 leaves (within the 43-49 estimated range)

---

## 5. Navigation Spec

### Up-link format
Every non-root document opens with exactly one up-link on line 1:

```
[↑ Vol 7: Hardware & Future Work](../index.md)           ← from domain index
[↑ Propulsion](../index.md)                               ← from chapter index
[↑ Ch.1: Metric Streamlining](../index.md)               ← from leaf
```

Pattern: `^\[↑ ` (grep-checkable; U+2191 Unicode arrow)

### Down-link format
Each index document ends with a `## Contents` section listing children with one-line
descriptions and relative links:

```markdown
## Contents

- [Ch.1: Metric Streamlining and Superluminal Transits](ch1-metric-streamlining/index.md) — 10
  sections covering active impedance control, warp mechanics, and the HTS falsification test
- [Ch.2: AVE Resolutions to Modern Precision Crises](ch2-ave-resolutions/index.md) — 10
  precision-crisis resolutions including JWST, DAMA/LIBRA, and quantum entanglement
```

### Leaf terminal marker
Line 2 of every leaf (after up-link):
```
<!-- leaf: verbatim -->
```

Placeholder variant (if source not yet extracted):
```
<!-- leaf: placeholder — source not yet extracted -->
```

### Cross-volume reference format

**Primary dependency pointer** (agent must follow to get the definition):
```markdown
> → Primary: [Dielectric Yield Limit $V_{\text{yield}}$](../../vol4/engineering/ch1-circuit-analysis/s01-yield-limit.md) — defined in Vol 4 Ch.1
```

**Optional suggestion** (agent may skip):
```markdown
> ↗ See also: [Condensed Matter Superconductivity](../../vol3/condensed-matter/ch9-condensed-matter/index.md) — Vol 3 treatment of same phenomenon
```

### Cross-volume reference: how Vol 3 points to `sec:melting_eigenmode`

Vol 3's KB document (wherever it references the water melting derivation) should carry:
```markdown
> → Primary: [Water Melting Point as Proton Transfer Eigenmode](../../vol7/condensed-matter/ch4-phase-transitions/s03-melting-eigenmode.md) — Vol 7 Ch.4 §4.3 [sec:melting_eigenmode]
```

The label `sec:melting_eigenmode` is stable at:
`ave-kb/vol7/condensed-matter/ch4-phase-transitions/s03-melting-eigenmode.md`

This path must not change after taxonomy is frozen — it is an external navigation dependency.

---

## 6. Shared Content Decision

**Recommendation: (a) Dedicated pages at `ave-kb/common/`**

`common/appendix_experiments.tex` (Unified Index of Experimental Falsifications) is explicitly
shared cross-volume — it is included via `\input{../common/appendix_experiments.tex}` in
multiple volumes and is not authored within any single volume's directory. Duplicating it in
each volume's KB section would:
- create multiple copies that can drift out of sync when the source is updated
- force any agent navigating to experimental falsifications to know which volume's copy to use
- make the acceptance criterion "each leaf has exactly one source" false

The correct structure is:
```
ave-kb/common/appendix-experiments.md    [leaf — verbatim]
```

Each volume's appendix section in its index carries a structural link (not a cross-reference
suggestion — it is a required link):
```markdown
## Appendix

- [Unified Index of Experimental Falsifications](../common/appendix-experiments.md) — shared
  across all volumes; sourced from common/appendix_experiments.tex
```

Same recommendation applies to `common_equations/eq_axiom_3.tex` and
`common/translation_*.tex` files: each gets one canonical leaf in `ave-kb/common/` and is
linked structurally from whatever volume indexes reference it.

---

## 7. Acceptance Criteria

1. **Navigation depth**: `find manuscript/ave-kb/vol7 -name "*.md" | awk -F/ 'NF>8'` returns
   empty — no file exceeds 4 levels below `ave-kb/` (entry-point → vol7 → domain → chapter →
   leaf = 5 path components below ave-kb/, but the depth constraint counts hierarchy levels, not
   filesystem depth). Correct check: no leaf is more than 4 up-link traversals from
   `entry-point.md`. From any Vol 7 leaf: leaf → chapter index (1) → domain index (2) → vol7
   index (3) → entry-point (4). Maximum traversal = 4. Pass.

2. **Up-link completeness**: `grep -rL '^\[↑ ' manuscript/ave-kb/vol7/` returns only files
   that are explicitly exempted (none in vol7 — `entry-point.md` is in `ave-kb/`, not
   `vol7/`). Every vol7 document must have an up-link on line 1.

3. **Leaf marker presence**: `grep -rL '^<!-- leaf: ' manuscript/ave-kb/vol7/ | grep -v
   index.md` returns empty — every non-index file in vol7 has a leaf marker on line 2.

4. **No summarization in leaves**: `grep -rl '^## Summary\|^## Overview' manifest/ave-kb/vol7/`
   returns only index files, never leaf files.

5. **Entry-point token budget**: `wc -w manuscript/ave-kb/entry-point.md` returns ≤ 2200 words
   (proxy for 3000 tokens).

6. **`sec:melting_eigenmode` stable path**: the file
   `manuscript/ave-kb/vol7/condensed-matter/ch4-phase-transitions/s03-melting-eigenmode.md`
   exists and contains `label: sec:melting_eigenmode` in its header metadata.

7. **Multi-section source extraction**: `manuscript/ave-kb/vol7/condensed-matter/ch4-phase-transitions/`
   contains exactly 5 leaf files (s01 through s05), not 3, confirming that
   `03_melting_eigenmode.tex` was split correctly across s03, s04, and s05.

8. **Shared appendix not duplicated**: `find manuscript/ave-kb/vol7 -name "appendix-experiments.md"`
   returns empty — the appendix leaf lives only in `ave-kb/common/`, not inside vol7.

9. **Ch.1 flat structure**: `find manuscript/ave-kb/vol7/propulsion/ch1-metric-streamlining -type d`
   returns only the single chapter directory — no subdirectories for Part I / Part II.

10. **Vol 7 resultbox coverage**: all 6 named resultboxes from the survey appear as content in
    their designated leaves — "H–O–H Bond Angle (Op3 Small-Signal)" in s04-hoh-bond-angle.md,
    "Topological Cell Collapse" in s05-topological-cell-collapse.md, "Sirius B Redshift
    Comparison" in s04-universal-operators-predictions.md (Ch.5), "WD Shear Eigenfrequencies" in
    s04-universal-operators-predictions.md (Ch.5), "The DC Operating Point" in s02-lc-analogs.md
    (Ch.6), "Regime IV Isomorphism Table" in s05-regime-iv-isomorphism.md (Ch.6). Verify by
    grepping for the resultbox title strings in the designated files.

---

## 8. Anomalies Affecting Taxonomy Design

| # | Anomaly | Taxonomy Impact |
|---|---|---|
| 1 | Legacy directory numbering (02_, 05_, 08_, 11_, 12_, 13_) | Use label keys only for KB slug generation; do not derive slugs from directory names |
| 2 | Ch.1 pseudo-Part I/II in comments only | Flatten: all 10 sections are leaves in one chapter directory; no Part subdirectory |
| 3 | Ch.5 and Ch.6 have `\chapter{}` heading inside content file | Distiller instruction: heading present in source — do not re-emit as a new heading; extract sections below it |
| 4 | `03_melting_eigenmode.tex` contains §4.3 + §4.4 + §4.5 (3 sections in 1 file) | Distiller must split one source file into 3 leaves (s03, s04, s05); acceptance criterion #7 verifies this |
| 5 | Unqualified chapter-number cross-references (no volume name) | Distillers must resolve these via cross-volume label index before writing links; this is a Phase 3 task, not a structural issue for taxonomy |
| 6 | No `\cite{}` commands anywhere | No bibliography leaf needed; no citation cross-references to handle |
| 7 | Appendix is shared cross-volume | Excluded from vol7 hierarchy; goes to `ave-kb/common/` |
