# Vol 6 — Phase 2 Extraction

**Source volume:** `manuscript/vol_6_periodic_table/`
**Taxonomy reference:** `.claude/phase1-taxonomy/vol6_taxonomy.md`
**Extraction date:** 2026-04-02
**Status:** Complete — all skeleton positions mapped; 3 critical structural anomalies found

---

## Source Directory Listing

Chapter files (confirmed present):

| File | Lines (approx) | Content |
|---|---|---|
| `chapters/00_summary_table.tex` | ~10 | Unnumbered chapter; mass defect table |
| `chapters/00_introduction.tex` | ~50 | Executive Abstract chapter |
| `chapters/01_computational.tex` | ~420 | Computational mass defect; 8 labelled equations |
| `chapters/02_chemistry.tex` | ~50 | Chemistry Translation Guide |
| `chapters/03_hydrogen.tex` | ~90 | Z=1 Hydrogen |
| `chapters/04_helium.tex` | ~90 | Z=2 Helium |
| `chapters/05_lithium.tex` | ~90 | Z=3 Lithium |
| `chapters/06_beryllium.tex` | ~85 | Z=4 Beryllium |
| `chapters/07_boron.tex` | ~75 | Z=5 Boron |
| `chapters/08_carbon.tex` | ~75 | Z=6 Carbon |
| `chapters/09_nitrogen.tex` | ~75 | Z=7 Nitrogen |
| `chapters/10_oxygen.tex` | ~70 | Z=8 Oxygen |
| `chapters/11_fluorine.tex` | ~57 | Z=9 Fluorine — NON-STANDARD STRUCTURE |
| `chapters/12_neon.tex` | ~61 | Z=10 Neon — NON-STANDARD STRUCTURE |
| `chapters/13_sodium.tex` | ~61 | Z=11 Sodium |
| `chapters/14_magnesium.tex` | ~58 | Z=12 Magnesium |
| `chapters/15_aluminum.tex` | ~60 | Z=13 Aluminum |
| `chapters/16_silicon.tex` | ~57 | Z=14 Silicon — NON-STANDARD STRUCTURE |
| `chapters/A_heavy_element_catalog.tex` | ~350+ | Appendix: Z=15–119 |
| `../backmatter/03_geometric_inevitability.tex` | ~487 | Shared backmatter; included by `main.tex` |

Chapter listing confirmed from `main.tex` (hardcoded `\input{}` calls; no `_manifest.tex`).

---

## Element-to-Source File Mapping

| Element | Source file | Notes |
|---|---|---|
| hydrogen | `chapters/03_hydrogen.tex` | Standard 6-section structure |
| helium | `chapters/04_helium.tex` | Standard |
| lithium | `chapters/05_lithium.tex` | Duplicate `fig:li7_density_equator` label |
| beryllium | `chapters/06_beryllium.tex` | Standard |
| boron | `chapters/07_boron.tex` | No `\label{ch:boron}` |
| carbon | `chapters/08_carbon.tex` | No `\label{ch:carbon}` |
| nitrogen | `chapters/09_nitrogen.tex` | No `\label{ch:nitrogen}` |
| oxygen | `chapters/10_oxygen.tex` | Has `\label{ch:oxygen}`; no orbital-knot section (see Anomaly 4) |
| fluorine | `chapters/11_fluorine.tex` | Has `\label{ch:fluorine}`; non-standard 5-section structure — **CRITICAL** |
| neon | `chapters/12_neon.tex` | Has `\label{ch:neon}`; severely non-standard 4-section structure — **CRITICAL** |
| sodium | `chapters/13_sodium.tex` | Has `\label{ch:sodium}`; extra section at §3 position |
| magnesium | `chapters/14_magnesium.tex` | Has `\label{ch:magnesium}`; extra section at §3 position |
| aluminum | `chapters/15_aluminum.tex` | Has `\label{ch:aluminum}`; extra section at §3 position |
| silicon | `chapters/16_silicon.tex` | Has `\label{ch:silicon}`; non-standard structure — **CRITICAL** |

---

## Standard Leaf Section Titles (confirmed from source)

The 6 standard leaves map to the following `\section{}` titles. Confirmed from hydrogen, helium, lithium, beryllium, boron, carbon, nitrogen:

| Leaf slug | Section title in source |
|---|---|
| structure-isotope-stability | `Topological Structure and Isotope Stability` |
| vacuum-density-flux | `Continuous Vacuum Density Flux` |
| ee-equivalent | `Electrical Engineering Equivalent: [element-specific subtitle]` |
| topological-area | `Topological Area of Interest: [element-specific subtitle]` |
| orbital-knot-topology | `Orbital Knot Topology` (section + one `\subsection`) |
| semiconductor-regime | `Semiconductor Regime Classification` |

---

## Anomalous Extra Leaves

| Element | Extra leaf slug | Source section title | Source location (line) |
|---|---|---|---|
| sodium | core-proximity-effect | `The Core Proximity Effect ($351d$ vs $50d$)` | `13_sodium.tex` line 16 |
| magnesium | symmetric-shell-collapse | `The Symmetric Shell Collapse` | `14_magnesium.tex` line 16 |
| aluminum | gradual-halo-separation | `The Gradual Halo Separation Effect` | `15_aluminum.tex` line 16 |

In all three cases the extra section appears at position §3 (after §1 structure and §2 vacuum-density-flux), shifting the standard §3 EE-equivalent to §4, §4 topological-area to §5, and §6 semiconductor remains at the end.

---

## Framework + Appendix Skeleton-to-Source Mapping

| Skeleton path | Source file | Section/label | Notes |
|---|---|---|---|
| `framework/mass-defect-summary.md` | `chapters/00_summary_table.tex` | `\chapter*{Macroscopic Mass Defect Summary}` | Unnumbered chapter |
| `framework/executive-abstract.md` | `chapters/00_introduction.tex` | `\chapter{Executive Abstract: The Topological Nucleus}` | 4 sections; no `\label{}` on chapter |
| `framework/computational-mass-defect/index.md` | `chapters/01_computational.tex` | `\label{ch:computational_mass_defect}` | |
| `framework/computational-mass-defect/mass-as-reactive-load.md` | `01_computational.tex` | `\section{Mass as a Localized Reactive Load}` line 9 | |
| `framework/computational-mass-defect/topological-circuit-conventions.md` | `01_computational.tex` | `\section{Topological Circuit Conventions}` line 23 | |
| `framework/computational-mass-defect/python-simulator.md` | `01_computational.tex` | `\section{The Python Simulator: EE-Based Thermodynamic Integration}` line 33 | Source uses `\verbatim`, not `codebox` |
| `framework/computational-mass-defect/network-analytics.md` | `01_computational.tex` | `\section{Network Analytics: Q-Factor and S-Parameters}` line 60 | Includes 2 subsections |
| `framework/computational-mass-defect/nucleon-spacing-derivation.md` | `01_computational.tex` | `\section{...Nucleon Spacing ($d$)...}` line 82; `\label{sec:d_derivation}` | Includes subsection `Intra-Alpha Distance` line 97 |
| `framework/computational-mass-defect/mutual-coupling-constant.md` | `01_computational.tex` | `\section{Derivation of the Mutual Coupling Constant ($K$)}` line 110; `\label{sec:K_derivation}` | |
| `framework/computational-mass-defect/pn-junction-coupling.md` | `01_computational.tex` | `\section{Proton--Neutron Junction Coupling}` line 152; `\label{sec:pn_junction}` | 3 subsections |
| `framework/computational-mass-defect/abcd-transfer-matrix.md` | `01_computational.tex` | `\section{Transfer Matrix Cascade (ABCD Framework)}` line 196; `\label{sec:abcd_cascade}` | 2 subsections |
| `framework/computational-mass-defect/operating-regimes.md` | `01_computational.tex` | `\section{Linear vs Non-Linear Operating Regimes}` line 212; `\label{sec:operating_regimes}` | 1 subsection |
| `framework/computational-mass-defect/semiconductor-nuclear-analysis.md` | `01_computational.tex` | `\section{Semiconductor Circuit Analysis of Nuclear Binding}` line 227; `\label{sec:semiconductor_nuclear}` | 8 subsections; all 8 labelled equations in scope |
| `framework/computational-mass-defect/radioactive-decay-impedance.md` | `01_computational.tex` | `\section{Radioactive Decay as Impedance Mismatch}` line 404 | 2 subsections |
| `framework/chemistry-translation/index.md` | `chapters/02_chemistry.tex` | `\chapter{Chemistry Translation Guide}` line 1 | No `\label{}` on chapter |
| `framework/chemistry-translation/quantum-vs-topological-shells.md` | `02_chemistry.tex` | `\section{Quantum Orbitals vs. Topological Shells}` line 7 | |
| `framework/chemistry-translation/lewis-dots-vsepr.md` | `02_chemistry.tex` | `\section{Lewis Dots and Unbound Valency}` line 18 + `\section{VSEPR Theory and Inductive Minimization}` line 27 | Two sections combined into one leaf per taxonomy |
| `framework/chemistry-translation/semiconductor-regime-chemistry.md` | `02_chemistry.tex` | `\section{Semiconductor Regime Classification and Chemical Behavior}` line 39 | |
| `appendix/heavy-element-catalog/mass-prediction-accuracy.md` | `chapters/A_heavy_element_catalog.tex` | `\section{Mass Prediction Accuracy}` line 10 | Figure `fig:mass_error_vs_Z` |
| `appendix/heavy-element-catalog/full-element-table.md` | `A_heavy_element_catalog.tex` | `\section{Full Element Table}` line 21 | Contains longtable `tab:heavy_catalog`; Z=15–119 |
| `appendix/heavy-element-catalog/selected-heavy-orbital-topology.md` | `A_heavy_element_catalog.tex` | `\section{Orbital Topology of Selected Heavy Elements}` line 157 | |
| `appendix/heavy-element-catalog/selected-heavy-strain-fields.md` | `A_heavy_element_catalog.tex` | `\section{Nuclear Strain Fields of Selected Heavy Elements}` line 212 | |
| `appendix/heavy-element-catalog/selected-heavy-circuit-models.md` | `A_heavy_element_catalog.tex` | `\section{Equivalent Circuit Models of Selected Heavy Elements}` line 306 | |
| `appendix/geometric-inevitability/golden-ratio-min-impedance.md` | `../backmatter/03_geometric_inevitability.tex` | `\section{The Golden Ratio: Minimum Impedance at 12 Nodes}` line 12; `\label{sec:golden_ratio_emergence}` | 2 subsections |
| `appendix/geometric-inevitability/fibonacci-packing-proxy.md` | `03_geometric_inevitability.tex` | `\section{The Fibonacci Sequence: Convergent Ratio as Packing Proxy}` line 39; `\label{sec:fibonacci_packing}` | |
| `appendix/geometric-inevitability/pi-topological-horizon.md` | `03_geometric_inevitability.tex` | `\section{Pi and the Topological Horizon}` line 51; `\label{sec:pi_horizon}` | |
| `appendix/geometric-inevitability/magic-numbers-shell-closure.md` | `03_geometric_inevitability.tex` | `\section{Nuclear Magic Numbers: Shell Closure as Impedance Matching}` line 68; `\label{sec:magic_numbers}` | |
| `appendix/geometric-inevitability/platonic-progression.md` | `03_geometric_inevitability.tex` | `\section{The Platonic Progression}` line 90 | NO `\label{}` on this section — see Ambiguity 4 |
| `appendix/geometric-inevitability/derived-numerical-constants.md` | `03_geometric_inevitability.tex` | `\section{Derived Numerical Constants}` line 117; `\label{sec:derived_numerology}` | 9 subsections; all 3 cross-volume refs fall within this leaf scope |
| `appendix/geometric-inevitability/g-star-derivation.md` | `03_geometric_inevitability.tex` | `\section{$g_* = 7^3/4 = 85.75$: Lattice Mode Count}` line 376; `\label{sec:g_star_derivation}` | 2 subsections |
| `appendix/geometric-inevitability/alpha-s-derivation.md` | `03_geometric_inevitability.tex` | `\section{$\alpha_s = \alpha^{3/7} \approx 0.121$: Strong Coupling}` line 412; `\label{sec:alpha_s_derivation}` | 2 subsections |
| `appendix/geometric-inevitability/lambda-higgs-derivation.md` | `03_geometric_inevitability.tex` | `\section{$\lambda_H = 1/8$: Higgs Quartic Coupling}` line 446; `\label{sec:lambda_higgs_derivation}` | 2 subsections; `\cite{pdg2022}` present |
| `appendix/geometric-inevitability/conclusion-death-of-numerology.md` | `03_geometric_inevitability.tex` | `\section{Conclusion: The Death of Numerology}` line 480 | Final section |

---

## geometric-inevitability Cross-Reference Confirmation

- **`eq:H_infinity`**: PRESENT. File: `../backmatter/03_geometric_inevitability.tex` **line 257**. Text: `$H_\infty = 28\pi m_e^3 c G / (\hbar^2 \alpha^2)$ (see Eq.~\ref{eq:H_infinity})`. This is a forward/cross-volume `\ref{}` — `eq:H_infinity` is not defined anywhere in vol_6. Renders as `??` in Vol 6 PDF.

- **`sec:galactic_saturation`**: PRESENT. File: `../backmatter/03_geometric_inevitability.tex` **line 261**. Text: `(see \S\ref{sec:galactic_saturation})`. Not defined in vol_6. Renders as `??` in Vol 6 PDF.

- **`sec:membrane_phase_buffering`**: PRESENT. File: `../backmatter/03_geometric_inevitability.tex` **line 374**. Text: `(Volume V, Chapter 2, $\S$\ref{sec:membrane_phase_buffering})`. Explicitly cites Volume V, Chapter 2. Not defined in vol_6.

All three dangling refs fall within the `derived-numerical-constants.md` leaf scope (`\section{Derived Numerical Constants}`, line 117+). The cross-volume pointer `> → Primary:` must appear in both `geometric-inevitability/index.md` and in `derived-numerical-constants.md` itself.

---

## Magnesium Anomaly

All 7 magnesium leaves map to `14_magnesium.tex`. There is no `13_magnesium.tex`. The taxonomy typo at line 459 (which says `Source: 13_magnesium.tex §4`) is incorrect; the footnote correction at line 700 is correct. All magnesium content is in `14_magnesium.tex`.

---

## Structural Anomalies Requiring Skeleton Refinement

### Anomaly 1: Fluorine — Non-standard 5-section structure

Source `11_fluorine.tex` has these sections:

```
§1  Topological Structure and Isotope Stability  (line 10)
§2  Continuous Vacuum Density Flux               (line 15)
§3  The Macroscopic Halo Offset                  (line 18)  ← taxonomy incorrectly calls this §2
§4  Topological Area of Interest: ...            (line 32)  ← contains EE circuit figure fig:circuit_f19
§5  Semiconductor Regime Classification          (line 52)
```

There is NO `\section{Electrical Engineering Equivalent}` and NO `\section{Orbital Knot Topology}` in `11_fluorine.tex`.

**Corrected leaf mapping:**

| Leaf slug | Correct mapping |
|---|---|
| `structure-isotope-stability.md` | §1 "Topological Structure and Isotope Stability" |
| `vacuum-density-flux.md` | §2 "Continuous Vacuum Density Flux" |
| `ee-equivalent.md` | **NO SOURCE SECTION** — EE circuit figure embedded in §4 |
| `topological-area.md` | §3 "The Macroscopic Halo Offset" (NOT §4 as taxonomy implies) |
| `orbital-knot-topology.md` | §4 "Topological Area of Interest: Electronegativity as Asymmetric Inductance" (contains `fig:fluorine_19_topo`) |
| `semiconductor-regime.md` | §5 "Semiconductor Regime Classification" |

**Taxonomy error confirmed**: The taxonomy note (line 406) states `vacuum-density-flux.md` is "titled 'The Macroscopic Halo Offset' in source." This is wrong. §2 IS "Continuous Vacuum Density Flux." §3 is "The Macroscopic Halo Offset" — a distinct section. The taxonomy conflates §2 and §3 for fluorine.

**Coordinator action required**: Reduce fluorine to 5 leaves (remove `ee-equivalent.md`) or map `ee-equivalent.md` to the circuit figure content within §4 (very thin leaf — 1–2 sentences + figure).

### Anomaly 2: Neon — Non-standard 4-section structure; 3 of 7 skeleton leaves have no source

Source `12_neon.tex` has these sections:

```
§1  Addressing the Curve-Fitting Fallacy         (line 10)  ← extra section is FIRST
§2  Electrical Engineering Equivalent: ...       (line 26)
§3  Topological Area of Interest: ...            (line 29)  ← contains density fig + orbital fig
§4  Semiconductor Regime Classification          (line 56)
```

There is NO `\section{Topological Structure and Isotope Stability}`, NO `\section{Continuous Vacuum Density Flux}`, and NO `\section{Orbital Knot Topology}`.

**Corrected leaf mapping:**

| Leaf slug | Correct mapping |
|---|---|
| `structure-isotope-stability.md` | **NO SOURCE SECTION** — content exists only in unnumbered intro paragraphs (lines 1–9) |
| `vacuum-density-flux.md` | **NO SOURCE SECTION** — density figure `fig:neon_20_density` embedded in §3 |
| `ee-equivalent.md` | §2 "Electrical Engineering Equivalent: The 5-Phase Ring Oscillator" |
| `topological-area.md` | §3 "Topological Area of Interest: Noble Gas Inertness & Spectral Emission" |
| `orbital-knot-topology.md` | **NO SOURCE SECTION** — orbital topology figure `fig:neon_20_topo` embedded in §3 |
| `curve-fitting-fallacy.md` | §1 "Addressing the Curve-Fitting Fallacy" — CONFIRMED PRESENT |
| `semiconductor-regime.md` | §4 "Semiconductor Regime Classification" |

**Coordinator action required**: Reduce neon to 4 leaves (`curve-fitting-fallacy` + `ee-equivalent` + `topological-area` + `semiconductor-regime`). Option: extract the 9-line intro paragraphs (lines 1–9) as a thin 5th leaf for `structure-isotope-stability`. The density and orbital figures embedded in §3 do not constitute separate source sections.

### Anomaly 3: Silicon — Non-standard 5-section structure; 2 of 6 skeleton leaves have no source

Source `16_silicon.tex` has these sections:

```
§1  Topological Structure and Isotope Stability  (line 8)
§2  Continuous Vacuum Density Flux               (line 13)
§3  Symmetric Core Collapse                      (line 16)  ← separate extra section
§4  Electrical Engineering Equivalent: ...       (line 23)
§5  Topological Area of Interest: ...            (line 26)  ← semiconductor content merged here
```

There is NO `\section{Orbital Knot Topology}` and NO `\section{Semiconductor Regime Classification}`.

**Corrected leaf mapping:**

| Leaf slug | Correct mapping |
|---|---|
| `structure-isotope-stability.md` | §1 "Topological Structure and Isotope Stability" |
| `vacuum-density-flux.md` | §2 "Continuous Vacuum Density Flux" |
| `ee-equivalent.md` | §4 "Electrical Engineering Equivalent: The 7-Phase Pentagonal Bipyramid Network" |
| `topological-area.md` | §5 "Topological Area of Interest: The Foundation of Semiconductor Microelectronics" (semiconductor regime content embedded here) |
| `orbital-knot-topology.md` | **NO SOURCE SECTION** — topology figure `fig:silicon_28_topo` embedded in §5 |
| `semiconductor-regime.md` | **NO SOURCE SECTION** — semiconductor content merged into §5 |

**Taxonomy error confirmed**: The taxonomy note (line 487) states `vacuum-density-flux.md` is "titled 'Symmetric Core Collapse' in source." This is wrong. §2 is "Continuous Vacuum Density Flux" and §3 is "Symmetric Core Collapse" — a distinct section. The taxonomy conflates §2 and §3 for silicon.

**Coordinator action required**: Either (a) reduce silicon to 5 leaves (remove `orbital-knot-topology` and `semiconductor-regime`, merge their content into `topological-area.md`), or (b) add a `symmetric-core-collapse.md` extra leaf for §3 (analogous to the sodium/magnesium/aluminum pattern) and keep 5 standard leaves with 2 empty positions.

### Anomaly 4: Oxygen — `\section{Orbital Knot Topology}` absent; figure embedded in §4

Source `10_oxygen.tex` sections:
```
§1  Topological Structure and Isotope Stability  (line 4)
§2  Continuous Vacuum Density Flux               (line 15)
§3  Electrical Engineering Equivalent: ...       (line 25)
§4  Topological Area of Interest: ...            (line 39)  ← contains orbital figure fig:oxygen_16_topo
§5  Semiconductor Regime Classification          (line 56)
```

No `\section{Orbital Knot Topology}` exists. The orbital figure `fig:oxygen_16_topo` and its caption appear within §4. The taxonomy (line 397) already notes "no named subsection in source."

**Corrected mapping for `orbital-knot-topology.md`**: Carve from within §4 content — the paragraph beginning "While Carbon-12..." through `\label{fig:oxygen_16_topo}` (approximately lines 41–54 of `10_oxygen.tex`). This is a sub-section extraction, not a full-section extraction.

---

## Empty Skeleton Positions

| Skeleton leaf | Source file | Status |
|---|---|---|
| `fluorine/ee-equivalent.md` | `11_fluorine.tex` | NO SOURCE SECTION — EE content embedded in §4 |
| `neon/structure-isotope-stability.md` | `12_neon.tex` | NO SOURCE SECTION — content only in unnumbered intro paragraphs (lines 1–9) |
| `neon/vacuum-density-flux.md` | `12_neon.tex` | NO SOURCE SECTION — density figure embedded in §3 |
| `neon/orbital-knot-topology.md` | `12_neon.tex` | NO SOURCE SECTION — topology figure embedded in §3 |
| `silicon/orbital-knot-topology.md` | `16_silicon.tex` | NO SOURCE SECTION — topology figure embedded in §5 |
| `silicon/semiconductor-regime.md` | `16_silicon.tex` | NO SOURCE SECTION — semiconductor content merged into §5 |

---

## Leaf Boundary Notes

### Neon intro paragraphs (lines 1–9)
If the distiller extracts `neon/structure-isotope-stability.md` from the intro, the boundary is: from `\chapter{...}` through the line ending "...to $R_{bipyramid} = 81.181d$ from the origin." This is 9 lines of unnumbered prose.

### Oxygen orbital-knot-topology
Recommended boundary within §4: from the paragraph "While Carbon-12..." (~line 41) through `\label{fig:oxygen_16_topo}` (~line 53). Excludes the opening combustion paragraphs of §4. Distiller must verify exact line numbers.

### Fluorine ee-equivalent
Circuit figure `fig:circuit_f19` and its caption appear in §4 "Topological Area of Interest" (lines ~37–42). No separate EE circuit section exists. Distiller options: (a) fold circuit figure into `topological-area.md`; (b) extract circuit figure + surrounding sentence as a very thin `ee-equivalent.md`. Option (a) is cleaner.

### Chemistry translation combined leaf
`lewis-dots-vsepr.md` spans two adjacent sections: `\section{Lewis Dots and Unbound Valency}` (line 18) through the end of `\section{VSEPR Theory and Inductive Minimization}` (line 27 to ~line 38).

### Sodium section title with inline math
Source title: `The Core Proximity Effect ($351d$ vs $50d$)`. The `$...$` math expressions are part of the section title. Taxonomy slug is `core-proximity-effect.md`. Distiller must render the math in the leaf heading: "The Core Proximity Effect ($351d$ vs $50d$)".

---

## Notation and Macro Notes

Custom macros from `../structure/commands.tex` (shared across all volumes):

| Macro | Definition | Affected leaves |
|---|---|---|
| `\Lvac` | vacuum inductance per node | `01_computational.tex` throughout |
| `\Cvac` | vacuum capacitance per node | `01_computational.tex` throughout |
| `\Zvac` | vacuum characteristic impedance | `01_computational.tex` throughout |
| `\Wcut` | cutoff angular frequency | `01_computational.tex` throughout |
| `\vacuum` | `\mathcal{M}_A` | prose |
| `\planck` | Planck constant | equations |
| `\permeability` | `\mu_0` | equations |
| `\permittivity` | `\varepsilon_0` | equations |
| `\impedance` | impedance notation | equations |

All defined with `\providecommand` — safe for re-input.

**Project-specific notation (not macros) used inline in Vol 6:**
- `$d$` — nucleon spacing constant ($d = 4\hbar/(m_p c) \approx 0.841$ fm); defined in `eq:d_proton` in `01_computational.tex`
- `$K$` — mutual coupling constant ($K \approx 11.337$ MeV·fm); defined in `eq:k_mutual` in `01_computational.tex`
- `$M_{ij}$` — mutual impedance matrix element (throughout element chapters)
- `$V_R/V_{BR}$` — operating ratio (Small Signal analysis; throughout element chapters)
- `$R_{\text{bipyramid}}$`, `$R_{\text{oct}}$`, `$R_{\text{tet}}$` etc — geometry-specific radii
- CODATA masses in MeV inline (e.g., `$18617.730$ MeV`) — standard LaTeX math, no macro

---

## Ambiguities

1. **Fluorine leaf count (6 vs 5)**: Taxonomy allocates 6 leaves; source has 5 sections. `ee-equivalent.md` has no source section. Recommend: reduce to 5 leaves, treating §3 "Macroscopic Halo Offset" as a non-standard named leaf (analogous to sodium/magnesium/aluminum pattern). The taxonomy architect must decide before distillation.

2. **Neon leaf count (7 vs 4)**: Taxonomy allocates 7 leaves; source has 4 sections. Three skeleton positions have no named source section. Recommend: reduce neon to 4 leaves + optional 5th from intro prose. The taxonomy architect must decide.

3. **Silicon leaf count (6 vs 5)**: Taxonomy allocates 6 leaves; source has 5 sections. `orbital-knot-topology.md` and `semiconductor-regime.md` have no source sections; content merged into §5. Recommend: reduce to 5 leaves, or add `symmetric-core-collapse.md` extra leaf for §3. The taxonomy architect must decide.

4. **Platonic Progression section has no label**: `\section{The Platonic Progression}` at line 90 of `03_geometric_inevitability.tex` has no `\label{}`. Taxonomy's `platonic-progression.md` leaf navigates by section title only.

5. **Fluorine taxonomy note error**: The taxonomy (line 406) states `vacuum-density-flux.md` is "titled 'The Macroscopic Halo Offset' in source." This is wrong — §2 IS "Continuous Vacuum Density Flux" and §3 is "The Macroscopic Halo Offset." Must be corrected before distillation.

6. **Silicon taxonomy note error**: The taxonomy (line 487) states `vacuum-density-flux.md` is "titled 'Symmetric Core Collapse' in source." This is wrong — §2 is "Continuous Vacuum Density Flux" and §3 is "Symmetric Core Collapse." Must be corrected before distillation.
