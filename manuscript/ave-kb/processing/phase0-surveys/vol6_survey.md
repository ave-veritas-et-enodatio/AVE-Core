# Phase 0 Survey — Vol 6: The Periodic Table of Knots

**Volume:** `/Users/benn/projects/Applied-Vacuum-Engineering/manuscript/vol_6_periodic_table/`
**Title:** *Applied Vacuum Engineering, Volume VI: The Periodic Table of Knots*
**Author:** Grant Lindblom

---

## 1. Document Hierarchy

Entry point: `main.tex`. No `_manifest.tex` — chapter list hardcoded in `main.tex` lines 21–56. Backmatter uses `../backmatter/03_geometric_inevitability.tex` (NOT `01_appendices.tex`).

### Unnumbered front chapter — Macroscopic Mass Defect Summary
`chapters/00_summary_table.tex` — `\chapter*{Macroscopic Mass Defect Summary}` + `\addcontentsline` — `\label{ch:summary}` — ~31 lines

### Theoretical Framework

**Chapter: Executive Abstract: The Topological Nucleus** (`chapters/00_introduction.tex`, `\label{ch:intro}`, ~46 lines)
- Continuous Mathematical Closure ($Z=1\rightarrow28$)
  - §§ The Absolute Symmetric Cores ($\alpha$-Series)
  - §§ Asymmetric Valency and Reactivity
  - §§ Emergence of the Golden Ratio
- Deterministic Simulation

**Chapter: Computational Mass Defect via Mutual Impedance** (`chapters/01_computational.tex`, `\label{ch:computational_mass_defect}`, ~421 lines)
- Mass as a Localized Reactive Load
- Topological Circuit Conventions
- The Python Simulator: EE-Based Thermodynamic Integration
- Network Analytics: Q-Factor and S-Parameters
  - §§ Topological Quality Factor ($Q$) and Resonance
  - §§ Topological S-Parameters ($S_{11}$)
- Derivation of the Nucleon Spacing ($d$) from Axiom 1 `\label{sec:d_derivation}`
  - §§ Intra-Alpha Distance ($D_{\text{intra}}$) from Tetrahedral Packing
- Derivation of the Mutual Coupling Constant ($K$) `\label{sec:K_derivation}`
- Proton–Neutron Junction Coupling `\label{sec:pn_junction}`
  - §§ The Nuclear Diode Analogy
  - §§ Coulomb Correction for Heavy Nuclei
  - §§ The Absolute Mass Defect Topologic Limit
- Transfer Matrix Cascade (ABCD Framework) `\label{sec:abcd_cascade}`
  - §§ Nucleon Ports
  - §§ Network Topology for $Z \geq 15$
- Linear vs Non-Linear Operating Regimes `\label{sec:operating_regimes}`
  - §§ The Sulfur-32 Breakdown
- Semiconductor Circuit Analysis of Nuclear Binding `\label{sec:semiconductor_nuclear}`
  - §§ Two Binding Models: Bare vs Semiconductor `\label{sec:two_models}`
  - §§ Parameter Derivation Table
  - §§ Derivation of the Breakdown Voltage
  - §§ Miller Avalanche Multiplication
  - §§ Complete Binding Energy Formula
  - §§ Results: Small Signal to Large Signal Transition
  - §§ Topology as Semiconductor Device Type
  - §§ Inter-Alpha Distances as Coupled Cavity Resonators `\label{sub:R_coupled_cavity}`
- Radioactive Decay as Impedance Mismatch
  - §§ Tritium ($^3H$) Beta Decay
  - §§ Beryllium-8 ($^8Be$) Alpha Fission

**Chapter: Chemistry Translation Guide** (`chapters/02_chemistry.tex`, NO `\label`, ~49 lines)
- Quantum Orbitals vs. Topological Shells
- Lewis Dots and Unbound Valency
- VSEPR Theory and Inductive Minimization
- Semiconductor Regime Classification and Chemical Behavior

### Elemental Catalog (Z=1–14)

Standard 6-section template per element: (1) Topological Structure and Isotope Stability, (2) Continuous Vacuum Density Flux, (3) Electrical Engineering Equivalent, (4) Topological Area of Interest, (5) Orbital Knot Topology [+ subsection], (6) Semiconductor Regime Classification.

| File | Chapter Title | `\label` | Lines | Notable deviations |
|---|---|---|---|---|
| `03_hydrogen.tex` | Z=1: Hydrogen | `ch:hydrogen` | ~92 | Orbital section has 3 subsubsections (Bohr radius, Rydberg, de Broglie) |
| `04_helium.tex` | Z=2: Helium | `ch:helium` | ~94 | Standard template |
| `05_lithium.tex` | Z=3: Lithium | `ch:lithium` | ~93 | Duplicate label bug (see §7) |
| `06_beryllium.tex` | Z=4: Beryllium | `ch:beryllium` | ~88 | Standard template |
| `07_boron.tex` | Boron (Z=5): The Saturated Topological Horizon | **NONE** | ~77 | Missing `\label{ch:boron}` |
| `08_carbon.tex` | Carbon (Z=6): The Subcritical 3-Alpha Ring | **NONE** | ~74 | Missing `\label{ch:carbon}` |
| `09_nitrogen.tex` | Nitrogen (Z=7): Algorithmic Topologies | **NONE** | ~74 | Missing `\label{ch:nitrogen}` |
| `10_oxygen.tex` | Z=8: Oxygen | `ch:oxygen` | ~61 | No named subsection in orbital section |
| `11_fluorine.tex` | Fluorine-19: The Halogen Halo | `ch:fluorine` | ~57 | "The Macroscopic Halo Offset" replaces density section title |
| `12_neon.tex` | Neon-20: The Bipyramidal Noble Gas | `ch:neon` | ~60 | Extra section "Addressing the Curve-Fitting Fallacy" |
| `13_sodium.tex` | Sodium-23: The Alkali Halogen Paradox | `ch:sodium` | ~61 | "The Core Proximity Effect" section unique |
| `14_magnesium.tex` | Magnesium-24: The Six-Alpha Octahedron | `ch:magnesium` | ~58 | "The Symmetric Shell Collapse" section unique |
| `15_aluminum.tex` | Aluminum-27: The Octahedral Halo | `ch:aluminum` | ~60 | "The Gradual Halo Separation Effect" section unique |
| `16_silicon.tex` | Silicon-28: The Seven-Alpha Bipyramid | `ch:silicon` | ~57 | "Symmetric Core Collapse" replaces density section |

### Appendix

**Appendix Chapter: Catalog of Heavy Elements (Z=15 to Z=119)** (`chapters/A_heavy_element_catalog.tex`, `\label{ch:heavy_element_catalog}`, ~360 lines)
- Mass Prediction Accuracy
- Full Element Table `\label{tab:heavy_catalog}` — longtable Z=15–119
- Orbital Topology of Selected Heavy Elements (S-32, Ar-40, Ca-40, Ti-48, Cr-52, Fe-56)
- Nuclear Strain Fields of Selected Heavy Elements
- Equivalent Circuit Models of Selected Heavy Elements

**Shared Appendix: Geometric Inevitability** (`../backmatter/03_geometric_inevitability.tex`, `\label{app:geometric_inevitability}`, ~487 lines)
- The Golden Ratio: Minimum Impedance at 12 Nodes `\label{sec:golden_ratio_emergence}`
- The Fibonacci Sequence: Convergent Ratio as Packing Proxy `\label{sec:fibonacci_packing}`
- Pi and the Topological Horizon `\label{sec:pi_horizon}`
- Nuclear Magic Numbers: Shell Closure as Impedance Matching `\label{sec:magic_numbers}`
- The Platonic Progression
- Derived Numerical Constants `\label{sec:derived_numerology}` (9+ constants)
- $g_* = 7^3/4 = 85.75$: Lattice Mode Count `\label{sec:g_star_derivation}`
- $\alpha_s = \alpha^{3/7}$: Strong Coupling `\label{sec:alpha_s_derivation}`
- $\lambda_H = 1/8$: Higgs Quartic Coupling `\label{sec:lambda_higgs_derivation}`
- Conclusion: The Death of Numerology

---

## 2. Content Inventory

### Named tcolorbox environments
- **resultbox:** 1 total — `01_computational.tex` line 183, title "Topologic Yield Mass Defect (Binding Energy Ceiling)", $E_{\text{binding(max)}} = \alpha \cdot M_{\text{proton}} c^2$
- **axiombox, simbox, examplebox, summarybox, exercisebox, objectivebox, codebox:** 0 all
- **amsthm (theorem, definition, lemma):** 0

### Key labelled equations (all in `01_computational.tex`)

| Label | Description |
|---|---|
| `eq:d_proton` | $d = 4\hbar/(m_pc) \approx 0.841$ fm |
| `eq:d_intra` | $D_{\text{intra}} = d\sqrt{8} \approx 2.379$ fm |
| `eq:k_mutual_expanded` | K derivation (expanded form) |
| `eq:k_mutual` | $K = (5\pi/2) \cdot \alpha\hbar c/(1-\alpha/3) \approx 11.337$ MeV·fm (boxed) |
| `eq:coulomb_correction` | Coulomb repulsion correction |
| `eq:V_BR` | $V_{BR} = 6\alpha\hbar c / D_{\text{intra}} \approx 3.631$ MeV |
| `eq:miller` | Miller avalanche: $M = 1/(1-(V_R/V_{BR})^n)$ |
| `eq:V_R` | Reverse voltage per cluster |
| `eq:semiconductor_mass` | Complete nuclear mass formula (boxed master equation) |

No labelled equations in any element chapter (Z=1–14) or appendices.

### Key labelled tables

| Label | File | Description |
|---|---|---|
| `tab:mass_summary` | `00_summary_table.tex` | H through Si empirical vs. topological mass |
| `tab:model_comparison` | `01_computational.tex` | Bare K/r vs. semiconductor inter-alpha distances |
| `tab:engine_traceability` | `01_computational.tex` | Physics engine constant traceability |
| `tab:semi_nuclear_map` | `01_computational.tex` | Semiconductor–nuclear parameter mapping |
| `tab:avalanche_results` | `01_computational.tex` | Small/Large Signal transition |
| `tab:heavy_catalog` | `A_heavy_element_catalog.tex` | longtable Z=15–119 |

### Key labelled figures (per element: density/flux, circuit, topology)

`fig:ee_network_analytics`, `fig:isotope_decay` (computational chapter); per element H through Si: `fig:h1_density`, `fig:circuit_h1`, `fig:hydrogen_1_topo` … `fig:silicon_28_density`, `fig:circuit_si28`, `fig:silicon_28_topo`; heavy catalog: `fig:mass_error_vs_Z`, `fig:sulfur_topology` through `fig:circuit_fe56` (19 figures total in heavy catalog).

Note: `fig:li7_density_equator` defined TWICE in `05_lithium.tex` (see Anomaly 1).

---

## 3. Notation and Custom Macros

Shared macros from `structure/commands.tex` (all `\providecommand`): `\Lvac`, `\Cvac`, `\Zvac`, `\Wcut`, `\lp`, `\vacuum`, `\slew`, `\planck`, `\permeability`, `\permittivity`, `\impedance`, `\citestart`, `\citeend`.

**Critical observation:** None of these macros are used in any vol_6 chapter text. All math quantities typed inline as standard LaTeX. Vol_6 is completely decoupled from the macro shorthand system.

**Vol_6 inline notation (no macros defined):**
$d$ = proton spin radius; $K$ = mutual coupling constant; $D_{\text{intra}}$ = intra-alpha distance; $V_{BR}$ = breakdown voltage; $M$ = Miller avalanche factor; $V_R/V_{BR}$ = Small/Large Signal ratio; $6^3_2$ = Borromean link; $3_1$ = trefoil knot; $n\alpha$ = n-alpha cluster; $\mathcal{M}_A$ = vacuum medium; $K_{\text{MUTUAL}}$ = same as $K$ (code name used in prose)

Volume-specific `\definecolor` in circuit diagram files: `darkbg`, `neonblue`, `neongreen`, `neonorange`, `neonred`, `neonpurple`, `dimwhite`. These are local to standalone figure files; not loaded in chapter text. No Markdown translation needed.

---

## 4. Cross-References to Other Volumes

**Internal `\ref{}` calls** — all resolve within vol_6.

**Dangling `\ref{}` calls in shared backmatter** (`03_geometric_inevitability.tex`):
- `\ref{eq:H_infinity}` — defined in Vol 1 ch.4
- `\ref{sec:galactic_saturation}` — defined in Vol 1 ch.4 (or Vol 3 ch.5)
- `\ref{sec:membrane_phase_buffering}` — explicitly "Volume V, Chapter 2"

**Prose references to other volumes** (in `03_geometric_inevitability.tex`):
- "Volume V, Chapter 5" — protein folding timescale
- "Volume IV, Chapter 16" — FCC packing/void floor correction
- "Volume V, Chapter 2" — membrane phase buffering
- "Volume VI, Appendix A" — self-reference (valid)

**`\cite{pdg2022}`** in backmatter — requires shared `../bibliography`.

**Shared files NOT included by vol_6:** `../frontmatter/00_foreword.tex`, `../frontmatter/00_nomenclature.tex`, `../common/translation_*.tex`, `../common_equations/eq_axiom_[1-4].tex`, `../backmatter/01_appendices.tex`.

---

## 5. Key Concept List

**Framework vocabulary:** Topological Nucleus, Borromean Link ($6^3_2$), Trefoil Knot ($3_1$), Mass Defect via Mutual Impedance, Proton Spin Radius, Mutual Coupling Constant K, Nuclear Diode Analogy, Coulomb Correction, Miller Avalanche Multiplication, Breakdown Voltage, Small/Large Signal Regime, ABCD Transfer Matrix Cascade, Coupled Cavity Resonator, Radioactive Decay as Impedance Mismatch, Topological Q-Factor, S-Parameters, Alpha-Core Topology, Core-Plus-Halo Binding, Semiconductor Binding Engine

**Chemistry vocabulary:** Quantum Orbitals vs. Topological Shells, Lewis Dots as Unbound Valency, VSEPR as Inductive Minimization, Electronegativity as Asymmetric Inductance

**Named resultbox:** "Topologic Yield Mass Defect (Binding Energy Ceiling)"

**Element EE analogues (Z=1–14):** Hydrogen-1 (Isolated LC Tank), Helium-4 (Polyphase Resonant Transformer), Lithium-7 (Air-Core Transformer), Beryllium-9 (AC Wheatstone Bridge), Boron-11 (Massive Parasitic Array), Carbon-12 (3-Phase Delta-Wye Map), Nitrogen-14 (Irregular Scattering Matrix), Oxygen-16 (Tetraphase Network), Fluorine-19 (Halogen Halo / Asymmetric Inductance), Neon-20 (5-Phase Ring Oscillator), Sodium-23 (Dual-Band Coupled Filter), Magnesium-24 (6-Phase Balanced Bridge), Aluminum-27 (Asymmetrically Loaded Octahedral Network), Silicon-28 (7-Phase Pentagonal Bipyramid Network)

**Platonic geometry:** Triangle (C-12), Tetrahedron (O-16), Triangular Bipyramid (Ne-20), Octahedron (Mg-24), Pentagonal Bipyramid (Si-28), Cube (S-32), Bicapped Square Antiprism (Ar-40, Ca-40), Cuboctahedron (Ti-48), Centered Icosahedron (Cr-52), FCC-14 (Fe-56)

**Backmatter derived constants:** $g_* = 7^3/4$, $\alpha_s = \alpha^{3/7}$, $\lambda_H = 1/8$, $n_{\text{coop}} = 9$, $\beta_{\text{fold}} = \ln(3) \times 3/7$, $T_m$ water melting eigenmode, Golden Ratio as icosahedral packing, Magic Numbers as shell closure

---

## 6. Estimated Leaf Document Count: ~75–96

| Source | Rough leaf count |
|---|---|
| 00_summary_table | 1 |
| 00_introduction | 3–4 |
| 01_computational | 10–14 |
| 02_chemistry | 3–4 |
| 14 element chapters × ~4 atomic units | 56 |
| A_heavy_element_catalog | 4–5 |
| 03_geometric_inevitability | 10–12 |
| **Total** | **~87–96** |

Lower bound if element sections 1+2+3 merged per element: ~75.

---

## 7. Anomalies

1. **Duplicate label `fig:li7_density_equator` in `05_lithium.tex`.** Defined at both line 23 (minipage caption) and line 29 (actual equatorial slice). LaTeX uses second definition silently; first figure unreferenceable.

2. **Three element chapters missing `\label{ch:...}`.** Boron, Carbon, Nitrogen have no chapter label. No cross-references from within vol_6, so compiles without error.

3. **Chemistry chapter (`02_chemistry.tex`) missing `\label`.** Inconsistent with all other framework and element chapters.

4. **No `_manifest.tex`; chapter list hardcoded in `main.tex` lines 21–56.** Unlike other AVE volumes.

5. **Two `circuits/` directories with overlapping but non-identical content.** `vol_6_periodic_table/circuits/` contains 7 standalone files (H–N) NOT `\input`'d from any chapter. `figures/` contains 22 circuit `.tex` files that ARE used. `circuits/` appears to be an earlier working copy.

6. **`simulations/` directory is not LaTeX content.** `simulations/outputs/` has 13 orphaned PNGs; `simulations/spice_netlists/` has 100+ SPICE `.cir` files. Neither referenced from any `.tex` file.

7. **`elements.json` in volume root.** Standard periodic table data for Python physics engine only. Not referenced from any `.tex`.

8. **`\graphicspath` includes `assets/` which does not exist.** All figures are under `figures/`. Compiles because LaTeX also searches relative paths.

9. **Oxygen chapter lacks Orbital Knot Topology `\subsection`.** Every other element Z=1–14 has a named `\subsection` inside the orbital section; oxygen goes directly to prose.

10. **Python code in `01_computational.tex` uses `\verbatim` not `codebox`.** The `codebox` environment exists for this purpose.

11. **Three dangling `\ref{}` calls in shared backmatter.** `\ref{eq:H_infinity}`, `\ref{sec:galactic_saturation}`, `\ref{sec:membrane_phase_buffering}` render as `??` in the Vol_6 PDF.

12. **`\chapter*` for summary table with `\label` produces blank `\ref` output.** `ch:summary` is an unnumbered chapter — `\ref{ch:summary}` produces empty string.

13. **Local `bibliography.bib` in volume root alongside shared `../bibliography`.** Local file may be a development copy; only `../bibliography` used in the compiled document.
