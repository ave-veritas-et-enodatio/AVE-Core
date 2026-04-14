# Phase 0 Survey — Vol 5: Topological Biology & Molecular Circuitry

**Volume:** `/manuscript/vol_5_biology/`
**Title:** Applied Vacuum Engineering — Volume V: Topological Biology & Molecular Circuitry
**Author:** Grant Lindblom

---

## 1. Document Hierarchy

### Top-Level Include Chain
```
main.tex
  -> ../structure/preamble.tex          (packages/layout)
  -> ../structure/commands.tex          (shared macros and box environments)
  -> frontmatter/00_title.tex           (SKIPPED per instructions)
  -> ../frontmatter/00_foreword.tex     (SKIPPED per instructions)
  -> chapters/_manifest.tex
      -> chapters/01_biophysics_intro.tex
      -> chapters/02_organic_circuitry.tex
      -> chapters/03_deterministic_protein_folding.tex
      -> chapters/04_simulation_architecture.tex
      -> chapters/05_folding_roadmap.tex
      -> chapters/06_biophysics_pharmacology.tex
  -> ../backmatter/01_appendices.tex
      -> ../common/translation_circuit.tex
      -> ../common/translation_qm.tex
      -> ../common/translation_particle_physics.tex
      -> ../common/translation_gravity.tex
      -> ../common/translation_cosmology.tex
      -> ../common/translation_condensed_matter.tex
      -> ../common/translation_protein.tex
      -> ../common/translation_protein_solver.tex
      -> ../common/appendix_experiments.tex  (SHARED CROSS-VOLUME)
  -> ../bibliography
```

### Chapter Tree

**Chapter 1** — Biophysics: Protein Folding
- File: `chapters/01_biophysics_intro.tex`
- Label: `ch:biophysics`
- Approximate line count: ~85 lines
- Sections:
  - `\section{Protein Backbone: From Proton Radius to Folding}` — `\label{sec:protein_bridge}` **[DUPLICATE — see Anomalies]**
  - `\section{Derivation Chain: From Lattice Pitch to Bond Length}` — no label
  - `\section{Amino Acid Impedance Classification}` — no label
  - `\section{Validation: Chignolin (CLN025)}` — no label
  - `\section{Molecular Chiral FRET Parallax}` — no label

**Chapter 2** — Biological Circuitry: Amino Acids as SPICE Logic Gates
- File: `chapters/02_organic_circuitry.tex`
- Label: `ch:biological_circuitry`
- Approximate line count: ~661 lines
- Sections:
  - `\section{Introduction to Organic RLC Topology}` — no label
  - `\section{The Electromechanical Transduction Constant}` — no label
  - `\section{The Atomic Translation Layer}` — no label
    - `\subsection{Mass -> Inductance: L = m / xi^2}` — no label
    - `\subsection{Bond Stiffness -> Capacitance: C = xi^2 / k}` — no label
    - `\subsection{Self-Consistency Verification}` — no label
  - `\section{The Amino Acid Circuit Architecture}` — no label
    - `\subsection{The Transceiver Backbone}` — no label
    - `\subsection{The Biological Power Supply: Thermal THz Noise}` — no label
    - `\subsection{The R-Group Filter Stack}` — no label
    - `\subsection{Chirality as Phase Polarity}` — no label
  - `\section{Simulation Results: Zero-Parameter Prediction}` — no label
  - `\section{FTIR Falsification Test}` — no label
  - `\section{Peptide Chain Extension Test}` — no label
    - `\subsection{Batch SPICE Computation of 20 Standard Amino Acids}` — `\label{sec:batch_spice}`
  - `\section{First-Principles Bond Force Constants}` — `\label{sec:first_principles_k}`
    - `\subsection{Derivation}` — no label
    - `\subsection{Topological and Angular Projections}` — no label
    - `\subsection{Results}` — no label
  - `\section{Hydrogen Bond: Op4 Equilibrium}` — `\label{sec:hbond_derivation}`
    - `\subsection{The Macroscopic Translation Matrix: Liquid Water as the Vacuum Shadow}` — no label
  - `\section{Membrane Phase Buffering: The Topological LLCP Wedge}` — `\label{sec:membrane_phase_buffering}`
    - `\subsection{Discussion}` — no label

**Chapter 3** — Deterministic Protein Folding
- File: `chapters/03_deterministic_protein_folding.tex`
- Label: `ch:protein_folding`
- Approximate line count: ~792 lines
- Sections:
  - `\section{AVE Topological Impedance}` — no label
    - `\subsection{Quantitative Z_topo from SPICE Backbone Impedance}` — no label
  - `\section{Multiplexed Basis States}` — no label
    - `\subsection{The 3D Gradient Descent Engine}` — no label
  - `\section{SPICE Transmission Line Mismatch (S_11 Strain)}` — no label
  - `\section{Empirical Validation: 20-Sequence Stress Test}` — `\label{sec:stress_test}`
  - `\section{Backbone Eigenvalue from the Universal Solver}` — `\label{sec:backbone_eigenvalue}`
  - `\section{Discussion}` — no label
    - `\subsection{Comparison with Statistical Approaches}` — no label
    - `\subsection{First-Principles Derivation of Z_topo}` — `\label{sec:ramachandran_derivation}`
  - `\section{RMSD Benchmarking Against PDB}` — `\label{sec:rmsd_benchmark}`
    - `\subsection{S_11 Minimiser: Folding as Pure Impedance Matching}` — `\label{sec:s11_minimiser}`
  - `\section{Dual-Formalism Architecture and the Op2 Crossing Correction}` — `\label{sec:dual_formalism}`
    - `\subsection{Atom <-> Protein Mapping}` — no label
    - `\subsection{Op2 Topological Crossing Correction}` — `\label{sec:op2_crossing}`
    - `\subsection{Op2 vs. Op9: Complementary Corrections}` — no label
  - `\section{Translation of Terminology: Biology <-> Electrical Engineering}` — `\label{sec:terminology}`
    - `\subsection{Current Limitations}` — no label
    - `\subsection{Predicted Extensions}` — `\label{sec:protein_bridge}` **[DUPLICATE — see Anomalies]**

**Chapter 4** — Simulation Architecture: S11 Protein Folding Engine
- File: `chapters/04_simulation_architecture.tex`
- Label: `ch:protein_sim_architecture`
- Approximate line count: ~1,170 lines
- Sections (top-level only; full subsection tree is extensive — see labels file):
  - `\section{Tier 1: Axiom-Derived Constants}` — no label
  - `\section{Tier 2: Complex Topological Impedance Z_topo}` — `\label{sec:z_topo_table}`
  - `\section{Tier 3: Physics Layers}` — no label (8 subsections: Layers 1-8)
  - `\section{Solver Architecture}` — `\label{sec:solver_architecture}`
  - `\section{Script Reproduction Procedure}` — no label
  - `\section{Summary: Zero-Parameter Count}` — no label
  - `\section{Verification: 20-Sequence Stress Test}` — `\label{sec:stress_test_v3}`
  - `\section{Validation: Villin HP35}` — no label
  - `\section{Validation: Three-Protein Test}` — no label
  - `\section{Limitations of the 1D Cascade}` — no label
  - `\section{SS Recovery: Design Path and Scale-Invariant Methodology}` — `\label{sec:ss_recovery}`
  - `\section{Architectural Ceiling Theorem}` — `\label{sec:architectural_ceiling}`
  - `\section{Multi-Scale Impedance-Stratified Architecture}` — `\label{sec:multiscale_architecture}`

**Chapter 5** — Multi-Path TL Network Solver
- File: `chapters/05_folding_roadmap.tex`
- Label: `ch:network_solver`
- Approximate line count: ~2,500 lines (largest file in the 8-volume series)
- Sections (top-level only; subsection tree is very extensive):
  - `\section{Architecture: From Cascade to Network}` — `\label{sec:cascade_to_network}`
  - `\section{Compaction Physics}` — `\label{sec:compaction}`
  - `\section{Benchmark Results}` — `\label{sec:2d_benchmark}`
  - `\section{Analysis}` — `\label{sec:2d_analysis}`
  - `\section{Folding Timescale from Backbone Transmission Line Physics}` — `\label{sec:tau_fold}`
  - `\section{20-Protein PDB Validation}` — `\label{sec:pdb_validation}`
  - `\section{Dynamic Allostery via Impedance Perturbation}` — `\label{sec:allostery}`
  - `\section{Roadmap}` — `\label{sec:2d_roadmap}`
  - `\section{Environment Parameter Sensitivity}` — `\label{sec:env_sweep}`
  - `\section{Complete Circuit Model}` — `\label{sec:complete_circuit}`
  - `\section{Segmented Cascade Solver (v7)}` — `\label{sec:v7_cascade}`
  - `\section{Translation Matrix: Biology -> EE -> AVE}` — `\label{sec:translation_matrix}`
  - `\section{Y-Matrix Gradient Architecture}` — `\label{sec:ymatrix_gradient}`
  - `\section{Research Avenues Under the AVE Axioms}` — `\label{sec:research_avenues}`
- Notable subsections under Research Avenues:
  - `Neural Circuitry as a TL Network` — `\label{sec:neural_tl}`
  - `Future Memory` — `\label{sec:future_memory}`
  - `Sleep Recalibration` — `\label{sec:sleep_recalibration}`
  - `Alzheimer's` — `\label{sec:alzheimers}`
  - `Anesthesia` — `\label{sec:anesthesia}`
  - `EEG Modes` — `\label{sec:eeg_modes}`
  - `Phantom Limb` — `\label{sec:phantom_limb}`
  - `Broader Biological Research Avenues` — `\label{sec:broader_avenues}`

**Chapter 6** — Biophysics and Pharmacology Under AVE
- File: `chapters/06_biophysics_pharmacology.tex`
- Label: `ch:biophysics_pharmacology`
- Approximate line count: ~465 lines
- Sections:
  - `\section{Cancer as Impedance Decoupling}` — `\label{sec:cancer_impedance}`
  - `\section{Red Light Therapy as Impedance-Matched Photon Absorption}` — `\label{sec:red_light_therapy}`
  - `\section{Methylene Blue as a Molecular Impedance Bridge}` — `\label{sec:methylene_blue}`
  - `\section{Creatine as a Neural Decoupling Capacitor}` — `\label{sec:creatine_brain}`
  - `\section{Consciousness as a Macroscopic Cavity Eigenmode}` — `\label{sec:consciousness}`
  - `\section{EMDR as Impedance Annealing of Trauma Defects}` — `\label{sec:emdr}`

### Appendices (from shared `../backmatter/01_appendices.tex`)
- App A: The Interdisciplinary Translation Matrix — `\label{app:translation_matrix}`
- App B: Theoretical Stress Tests: Surviving Standard Disproofs — `\label{app:resolving_paradoxes}`
- App C: Summary of Exact Analytical Derivations — (no chapter label)
- App D: Computational Graph Architecture — `\label{app:computational_graph}`
- App E: Rigorous Foundations of DCVE — `\label{app:dcve}`
- App F: (from `../common/appendix_experiments.tex`) — SHARED CROSS-VOLUME

---

## 2. Content Inventory

### resultbox (tcolorbox) environments — 27 total

**Chapter 1 (01_biophysics_intro.tex) — 2 resultboxes:**
1. `{Proton-to-Backbone Length Scale}` — line ~13
2. `{Chignolin Validation}` — line ~71

**Chapter 2 (02_organic_circuitry.tex) — 4 resultboxes:**
3. `{The Electromechanical Transduction Constant}` — line ~13 (wraps eq:xi_topo)
4. `{Topological Inductance of an Atom}` — line ~28 (wraps eq:L_atom)
5. `{Topological Capacitance of a Bond}` — line ~57 (wraps eq:C_bond)
6. `{Projected Macroscopic Force Constant}` — line ~372 (wraps eq:projected_k)

**Chapter 3 (03_deterministic_protein_folding.tex) — 5 resultboxes:**
7. `{Topological Impedance}` — line ~16 (wraps eq:z_topo_def)
8. `{S_11 Feedback Gain Modulation (PID Error Signal)}` — line ~159 (wraps eq:s11_feedback)
9. `{S_11 Objective Function}` — line ~419 (wraps eq:s11_energy)
10. `{Op2 Crossing Correction (Protein Scale)}` — line ~631 (wraps eq:op2_protein)
11. `{Dual-Formalism Architecture (Protein)}` — line ~728

**Chapter 4 (04_simulation_architecture.tex) — 6 resultboxes:**
12. `{Topological Charge Reactance}` — line ~63
13. `{Conjugate Shunt Admittance}` — line ~119
14. `{Dielectric Saturation Amplification}` — line ~143
15. `{Segment Characteristic Impedance}` — line ~227 (wraps eq:z_seg_full)
16. `{Eigenvalue Root Target}` — line ~351 (wraps eq:eigenvalue_target)
17. `{SPICE Transient Equations of Motion}` — line ~373 (wraps eq:spice_velocity, eq:spice_position)

**Chapter 5 (05_folding_roadmap.tex) — 10 resultboxes:**
18. `{Folding Speed Limit}` — line ~225 (wraps eq:tau_min)
19. `{Full Kramers Folding Time}` — line ~321 (wraps eq:tau_fold)
20. `{Beta-Sheet Antiparallel Coupling}` — line ~740
21. `{Bend Discontinuity Admittance}` — line ~832
22. `{Derived Ramachandran Basins}` — line ~958
23. `{Backbone Y-Parameters}` — line ~1018
24. `{Eigenvalue Root Target (v5)}` — line ~1091
25. `{SPICE Transient Equations}` — line ~1148
26. `{SPICE Damping: Two Channels}` — line ~1167
27. `{v7 Segmented Cascade}` — line ~1710

**Chapter 6 (06_biophysics_pharmacology.tex) — 0 resultboxes**

### axiombox / simbox / examplebox / summarybox / exercisebox / circuitbox / codebox / objectivebox
None identified in any chapter file. The vol 5 chapters do not use these secondary tcolorbox environments.

### amsthm environments (theorem, definition, lemma)
None. The `theorem`, `definition`, and `lemma` environments are defined in `commands.tex` but are not used anywhere in vol 5.

### Key labelled equations

| Label | Location | Description |
|---|---|---|
| `eq:xi_topo` | ch2, line ~18 | Electromechanical transduction constant xi_topo = e/l_node |
| `eq:L_atom` | ch2, line ~30 | Topological inductance: L = m/xi^2 |
| `eq:C_bond` | ch2, line ~59 | Topological capacitance: C = xi^2/k |
| `eq:f_check` | ch2, line ~93 | Self-consistency: resonant frequency from L,C |
| `eq:Z_check` | ch2, line ~95 | Self-consistency: mechanical impedance |
| `eq:v_check` | ch2, line ~97 | Self-consistency: bond sound speed |
| `eq:fp_one_electron` | ch2, ~309 | Fabry-Perot one-electron eigenvalue |
| `eq:fp_two_electron` | ch2, ~323 | Two-electron MCL compression |
| `eq:n_eff_bond` | ch2, ~340 | Unified mode loading N_eff |
| `eq:bond_eigenvalue` | ch2, ~348 | d_eq from F-P with MCL loading |
| `eq:pi_coupling` | ch2, ~390 | pi-orbital axial coupling factor eta_pi = 4/9 |
| `eq:lp_qfactor` | ch2, ~399 | Lone-pair spatial Q-factor = 1/9 |
| `eq:projected_k` | ch2, ~374 | Projected macroscopic force constant |
| `eq:gamma_oh` | ch2, ~455 | Reflection coefficient Gamma for O-H |
| `eq:dipole` | ch2, ~460 | Water dipole moment 1.91 D |
| `eq:K_hbond` | ch2, ~468 | H-bond coupling constant K_HB |
| `eq:dsat_hbond` | ch2, ~475 | H-bond saturation distance = r_H + r_O |
| `eq:d_hbond` | ch2, ~487 | H-bond equilibrium distance d_HB = 1.754 Angstrom |
| `eq:E_hbond` | ch2, ~502 | H-bond energy E_HB = 4.98 kcal/mol |
| `eq:d_oo` | ch2, ~511 | O-O distance in ice: 2.727 Angstrom |
| `eq:cooperative_strain` | ch2, ~584 | Cooperative thermal strain A(T) |
| `eq:T_c_membrane` | ch2, ~607 | Yield temperature for pure membrane ~5.1 degrees C |
| `eq:cholesterol_yield` | ch2, ~621 | Cholesterol-buffered yield limit |
| `eq:z_topo_def` | ch3, ~18 | Z_topo = |Z_backbone|/|Z_R| |
| `eq:z_topo_derivation` | ch3, ~26 | First-principles Z_topo from R-group impedances |
| `eq:excluded_volume` | ch3, ~94 | Excluded volume repulsion force |
| `eq:backbone_hooke` | ch3, ~102 | Backbone Hooke spring |
| `eq:s11_feedback` | ch3, ~162 | S_11 feedback gain modulation |
| `eq:s11_energy` | ch3, ~421 | S_11 objective function (ABCD) |
| `eq:chirality` | ch3, ~440 | Non-reciprocal chiral phase beta_eff |
| `eq:op2_protein` | ch3, ~635 | Op2 knot crossing penalty |
| `eq:gauss_linking` | ch3, ~651 | Gauss linking integral for crossing number |
| `eq:total_loss` | ch4, ~12 | Full objective function L(phi,psi) |
| `eq:z_seg_full` | ch4, ~229 | Segment characteristic impedance Z_seg = sqrt(m/n_e) |
| `eq:abcd_lossy` | ch4, ~266 | Lossy ABCD matrix per backbone section |
| `eq:eigenvalue_target` | ch4, ~353 | Newton-Raphson eigenvalue root target |
| `eq:spice_velocity` | ch4, ~375 | SPICE transient velocity update |
| `eq:tau_min` | ch5, ~227 | Folding speed limit tau_min = QN/f_0 |
| `eq:tau_fold` | ch5, ~323 | Full Kramers folding time |
| `eq:y_matrix_tl` | ch5, ~47 | 2x2 Y-matrix for TL segment |
| `eq:schur` | ch5, ~62 | Schur complement for 1-port admittance |
| `eq:s11_network` | ch5, ~68 | S_11 from nodal admittance |

### Figures with labels

| Label | File | Description |
|---|---|---|
| `fig:protein_backbone` | ch1 | Protein backbone impedance from AVE axioms (3-panel) |
| `fig:amino_resonance` | ch2 | Transfer function of 6 amino acids |
| `fig:ftir_comparison` | ch2 | AVE vs NIST FTIR for Glycine/Alanine |
| `fig:chain_sensitivity` | ch2 | Peptide chain extension & mass sensitivity |
| `fig:batch_resonance` | ch2 | Batch transmission sweep of all 20 amino acids |
| `fig:cholesterol_topological_phase_buffer` | ch2 | Cholesterol phase buffer: A(T), S(T), Gamma(T) |
| `fig:protein_folding_helix` | ch3 | Topological gradient descent (alpha-helix) |
| `fig:protein_folding_sheet` | ch3 | Topological gradient descent (beta-sheet) |
| `fig:protein_folding_3d_collapse` | ch3 | Multiplexed basis state resolution |
| `fig:protein_spice_folding` | ch3 | Topological AC impedance means test |
| `fig:ramachandran_steric` | ch3 | Axiom-derived Ramachandran steric maps |
| `fig:ramachandran_correlation` | ch3 | Helix propensity vs Chou-Fasman P_alpha |
| `fig:tau_fold_validation` | ch5 | Predicted vs experimental folding rates (15 proteins) |
| `fig:smith` | ch5 | Smith chart (context: Ramachandran basin derivation) |
| `fig:circuit` | ch5 | Circuit representation (context: complete circuit model) |

### Tables with labels

| Label | File | Description |
|---|---|---|
| `tab:inductances` | ch2 | Atomic inductances L = m/xi^2 for 5 elements |
| `tab:capacitances` | ch2 | Bond capacitances C = xi^2/k |
| `tab:batch_resonance` | ch2 | Primary absorption notch for all 20 amino acids |
| `tab:first_principles_k` | ch2 | First-principles bond lengths and force constants |
| `tab:translation_matrix` | ch2 | Translation matrix: vacuum lattice -> water properties |
| `tab:z_topo_values` | ch3 | Complex Z_topo for all 20 amino acids |
| `tab:stress_test` | ch3 | 20-sequence stress test results |
| `tab:ramachandran_validation` | ch3 | First-principles vs Chou-Fasman P_alpha |
| `tab:rmsd_benchmark` | ch3 | Kabsch RMSD vs PDB (4 peptides) |
| `tab:s11_comparison` | ch3 | 8-force engine vs S_11 axiom minimiser |
| `tab:autodiff` | ch3 | Wall-clock speedup: finite-diff vs JAX+Adam |
| `tab:dual_formalism` | ch3 | Dual-formalism atom <-> protein mapping |
| `tab:engine_constants_protein` | ch4 | Engine constants and derivation chain |
| `tab:z_topo_complex` | ch4 | Complex Z_topo table (ch4 version) |
| `tab:code_equation_map` | ch4 | Code-equation mapping |
| `tab:operator_crossref` | ch4 | Universal operator cross-reference |
| `tab:dependencies` | ch4 | Module dependency table |
| `tab:stress_test_v3` | ch4 | 20-sequence stress test (v3 engine) |
| `tab:validation_5atom` | ch4 | 5-atom steric validation |
| `tab:validation_four_proteins` | ch4 | Three/four protein validation |
| `tab:yshunt_balance` | ch4 | Y-shunt balance diagnostic |
| `tab:qdecay_results` | ch4 | Q-decay weighting results |
| `tab:mosfet_mapping` | ch4 | MOSFET depletion-region analogy mapping |
| `tab:saturation_operators` | ch4 | Regime of operation / saturation operators |
| `tab:ceiling_evidence` | ch4 | Architectural ceiling evidence |
| `tab:multiscale_mapping` | ch4 | Multi-scale architecture mapping |
| `tab:v7_results` | ch4 | Multi-scale + S_11 v7 vs lumped versions |
| `tab:2d_benchmark` | ch5 | 1D cascade vs 2D S-parameter network |
| `tab:speed_limit` | ch5 | Folding speed limit per protein |
| `tab:tau_fold` | ch5 | Folding timescale: prediction vs experiment (15 proteins) |
| `tab:20pdb` | ch5 | 20-protein PDB validation |
| `tab:allostery` | ch5 | Allosteric angular displacement |
| `tab:beta_bench` | ch5 | Beta-sheet antiparallel coupler benchmark |
| `tab:bend_consensus` | ch5 | Bend admittance consensus values |
| `tab:bend_bench` | ch5 | Bend discontinuity benchmark |
| `tab:v3v4` | ch5 | v3 vs v4 engine comparison |
| `tab:env_params` | ch5 | Environment parameter sweep parameters |
| `tab:env_sweep_results` | ch5 | Environment sweep results |
| `tab:v4_benchmark` | ch5 | v4 benchmark |
| `tab:bio_circuit_map` | ch5 | Biology-circuit mapping table |
| `tab:v7_benchmark` | ch5 | v7 segmented cascade benchmark |
| `tab:constants_audit` | ch5 | Constants audit |
| `tab:ymatrix_magnitude` | ch5 | Y-matrix entry magnitude audit |
| `tab:loss_decomp` | ch5 | Loss decomposition table |
| `tab:impedance_landscape` | ch5 | Impedance landscape of solvent boundary |
| `tab:op_catalog` | ch5 | Universal operator catalog |
| `tab:eeg_modes` | ch5 | EEG cortical mode predictions |
| `tab:research_avenues` | ch5 | Summary of biological research avenues |
| `tab:fft_results` | ch5 | FFT frequency-domain analysis results |
| `tab:fft_init_benchmark` | ch5 | FFT-seeded initialisation benchmark |
| `tab:segmentation_validation` | ch5 | Segmentation validation |
| `tab:trans_protein` | common | Protein folding translation table (from `../common/translation_protein.tex`) |

---

## 3. Notation and Custom Macros

### Shared macros (from `../structure/commands.tex`)

All defined with `\providecommand` — safe to re-input:

| Macro | Renders as | Meaning |
|---|---|---|
| `\Lvac` | $L_{node}$ | Lattice inductance |
| `\Cvac` | $C_{node}$ | Lattice capacitance |
| `\Zvac` | $Z_0$ | Characteristic impedance |
| `\Wcut` | $\omega_{sat}$ | Saturation frequency |
| `\lp` | $l_{node}$ | Lattice pitch |
| `\vacuum` | $M_A$ | Vacuum mass/medium |
| `\slew` | $c$ | Speed of light |
| `\planck` | $\hbar$ | Reduced Planck constant |
| `\permeability` | $\mu_0$ | Vacuum permeability |
| `\permittivity` | $\varepsilon_0$ | Vacuum permittivity |
| `\impedance` | $Z_0$ | Vacuum impedance |

### Custom tcolorbox environments (from `../structure/commands.tex`)

| Environment | Usage | Notes |
|---|---|---|
| `resultbox{Title}` | Primary named-result container (27 uses in vol 5) | NOT cross-referenceable by label; no label on the box itself |
| `axiombox[Title]` | Vacuum Engineering Postulates | 0 uses in vol 5 |
| `simbox[Title]` | Computational Module results (auto-numbered) | 0 uses in vol 5 |
| `circuitbox{Title}` | Circuit schematics | 0 uses in vol 5 |
| `codebox{Title}` | SPICE netlists / code | 0 uses in vol 5 |
| `objectivebox[Title]` | Learning objectives | 0 uses in vol 5 |
| `examplebox[Title]` | Worked examples (auto-numbered) | 0 uses in vol 5 |
| `summarybox[Title]` | Chapter summaries | 0 uses in vol 5 |
| `exercisebox[Title]` | End-of-chapter exercises | 0 uses in vol 5 |

### amsthm environments
`theorem`, `definition`, `lemma` are defined in `commands.tex` but none are used in vol 5.

### Volume-specific macros
None found — vol 5 uses no `\newcommand` or `\renewcommand` beyond the shared set.

### Project-specific notation (not standard mathematical)
- `Z_topo`, `Z_{topo}` — topological impedance (not standard EE or biology notation)
- `xi_topo` / `\xi_\text{topo}` — electromechanical transduction constant (AVE-specific)
- `N_eff` — unified mode loading integer (AVE bond eigenvalue framework)
- `P_C` — packing fraction constant (~0.1834, Axiom 3; also written `p_c`)
- `E_HB`, `d_HB` — hydrogen bond energy and distance from Op4 equilibrium
- `Op2`, `Op3`, `Op4`, `Op9`, `Op14` — AVE "operator" numbering (not standard)
- `K=2G` — trace-reversed elastic condition (AVE-specific)
- `S_{11}` used as a free-energy functional (non-standard use of S-parameter notation)

---

## 4. Cross-References to Other Volumes

### References to labels defined outside vol 5

| Reference | Location in vol 5 | Probable source volume |
|---|---|---|
| `\ref{ch:quantum_mechanics}` | ch3, lines 508/529/537/608 | Vol 2 (quantum mechanics and orbitals chapter) |
| `\ref{app:solver_toolchain}` | ch3, lines 247/250/538 | `backmatter/05_universal_solver_toolchain.tex` — NOT included in vol 5's `main.tex` |
| `\ref{app:geometric_inevitability}` | ch5, lines 298/385 | `backmatter/03_geometric_inevitability.tex` — NOT included in vol 5's `main.tex` |
| `\ref{sec:n_coop_derivation}` | ch2, line 611 | Not defined anywhere in vol 5 — refers to a section that appears to be missing entirely |
| `\ref{eq:flory}` | ch3, line 250 (via app:solver_toolchain) | Would be in `backmatter/05_universal_solver_toolchain.tex` |

### Prose cross-volume references

| Reference | Location | Target volume |
|---|---|---|
| "Volume I" / "AVE axioms (Volume I)" | ch1 | Vol 1 (AVE foundations) |
| "Vol. II, Ch. 7" (Mutual Cavity Loading solver) | ch2, lines 304/364/534/535 | Vol 2, Chapter 7 (quantum mechanics/orbitals) |
| "Volume V" self-reference | ch1 line 70 | Self (vol 5) — not a cross-volume ref |
| "Chapter \ref{ch:quantum_mechanics}" | ch3 | Vol 2 (ch:quantum_mechanics is not in vol 5) |
| "Chapter \ref{ch:biological_circuitry}" | ch3 (multiple) | Vol 5 ch2 — internal, resolves correctly |
| "Chapter \ref{ch:protein_sim_architecture}" | ch5 line 4 | Vol 5 ch4 — internal, resolves correctly |

Note: `ch:quantum_mechanics` is referenced 4 times in ch3 (Dual-Formalism section) but is defined in Vol 2 (the quantum mechanics chapter), not in vol 5. This is a **dangling cross-volume reference** — the label does not exist in vol 5's compiled document.

### `\cite{}` calls

| Key | Location | Description |
|---|---|---|
| `codata2018` | ch2, line 35 | CODATA atomic masses (standard reference) |
| `jax2018` | ch3, line 478 | JAX automatic differentiation library |

---

## 5. Key Concept List

**Chapter/section titles:**
Biophysics: Protein Folding, Protein Backbone From Proton Radius, Derivation Chain Lattice Pitch to Bond Length, Amino Acid Impedance Classification, Chignolin Validation, Molecular Chiral FRET Parallax, Biological Circuitry Amino Acids as SPICE Logic Gates, Organic RLC Topology, Electromechanical Transduction Constant, Mass to Inductance, Bond Stiffness to Capacitance, Amino Acid Circuit Architecture, Chirality as Phase Polarity, FTIR Falsification Test, Batch SPICE 20 Amino Acids, First-Principles Bond Force Constants, Fabry-Perot Bond Eigenvalue, Hydrogen Bond Op4 Equilibrium, Liquid Water as Vacuum Shadow, Membrane Phase Buffering LLCP Wedge, Cholesterol as Topological Phase Buffer, Deterministic Protein Folding, AVE Topological Impedance, Multiplexed Basis States, 3D Gradient Descent Engine, SPICE Transmission Line Mismatch S11 Strain, 20-Sequence Stress Test, Backbone Eigenvalue Universal Solver, Ramachandran Derivation from Axioms, RMSD Benchmarking Against PDB, S11 Minimiser Folding as Pure Impedance Matching, Dual-Formalism Architecture, Op2 Topological Crossing Correction, Simulation Architecture S11 Engine, Axiom-Derived Constants, Complex Topological Impedance, Backbone ABCD Cascade, Newton-Raphson Eigenvalue Root-Finding, SPICE Transient Integration, Cotranslational Cascade v7, Architectural Ceiling Theorem, Multi-Scale Impedance Architecture, Multi-Path TL Network Solver, Network Topology, Y-Parameter Formulation, Schur Complement, Compaction Physics, Folding Timescale Transmission Line, Folding Speed Limit, Kramers Folding Time, 20-Protein PDB Validation, Dynamic Allostery Impedance Perturbation, Beta-Sheet Antiparallel TL Coupler, Ramachandran Basins from Steric Geometry, Frequency-Domain Analysis, Environment Parameter Sensitivity, Complete Circuit Model, Segmented Cascade v7, Research Avenues, Neural Circuitry TL Network, Sleep Recalibration, Alzheimers Impedance, Anesthesia Cavity Collapse, Phantom Limb, Biophysics Pharmacology, Cancer as Impedance Decoupling, Red Light Therapy, Methylene Blue Impedance Bridge, Creatine Neural Decoupling Capacitor, Consciousness Macroscopic Cavity Eigenmode, EMDR Impedance Annealing

**Named result titles (from resultboxes):**
Proton-to-Backbone Length Scale, Chignolin Validation, Electromechanical Transduction Constant, Topological Inductance of an Atom, Topological Capacitance of a Bond, Projected Macroscopic Force Constant, Topological Impedance, S11 Feedback Gain Modulation (PID Error Signal), S11 Objective Function, Op2 Crossing Correction (Protein Scale), Dual-Formalism Architecture (Protein), Topological Charge Reactance, Conjugate Shunt Admittance, Dielectric Saturation Amplification, Segment Characteristic Impedance, Eigenvalue Root Target, SPICE Transient Equations of Motion, Folding Speed Limit, Full Kramers Folding Time, Beta-Sheet Antiparallel Coupling, Bend Discontinuity Admittance, Derived Ramachandran Basins, Backbone Y-Parameters, Eigenvalue Root Target (v5), SPICE Transient Equations, SPICE Damping Two Channels, v7 Segmented Cascade

---

## 6. Estimated Leaf Document Count

**By content type:**

| Chapter | Resultboxes | Major equation derivations | Tables (substantial) | Subsection-level concepts | Estimated leaves |
|---|---|---|---|---|---|
| Ch 1 (Biophysics intro) | 2 | 3 | 0 | 5 sections | 6-8 |
| Ch 2 (Organic circuitry) | 4 | ~12 | 4 | ~12 subsections | 18-22 |
| Ch 3 (Deterministic folding) | 5 | ~8 | 5 | ~10 subsections | 16-20 |
| Ch 4 (Sim architecture) | 6 | ~10 | ~10 | ~20 subsections | 20-25 |
| Ch 5 (Network solver) | 10 | ~15 | ~15 | ~30 subsections | 35-45 |
| Ch 6 (Pharmacology) | 0 | 0 | 0 | 6 sections | 6-8 |
| **Total** | **27** | | | | **101-128** |

**Estimated range: 100-125 leaf documents.**

Reasoning: Vol 5 is dominated by ch5 (~2,500 lines with ~30 subsections and 10 resultboxes), ch4 (~1,170 lines), and ch3 (~792 lines). The pharmacology chapter (ch6) is primarily prose hypothesis + testable predictions with no derivations, so its leaves are coarser. Ch1 is short (~85 lines) but has a key complete derivation (H-bond from lattice pitch). The translation table from `common/translation_protein.tex` would map to one leaf.

---

## 7. Anomalies

1. **Duplicate label `sec:protein_bridge`** — Defined at two locations:
   - `chapters/01_biophysics_intro.tex`, line 8: section "Protein Backbone: From Proton Radius to Folding" in ch1
   - `chapters/03_deterministic_protein_folding.tex`, line 765: subsection "Predicted Extensions" in ch3
   This will cause a LaTeX duplicate-label warning. The ch3 occurrence is semantically a "predicted extensions" section, not a protein-bridge topic — the label appears to have been accidentally reused. Any `\ref{sec:protein_bridge}` will resolve to the ch3 location (second definition wins in LaTeX).

2. **Dangling appendix references** — Ch3 references `\ref{app:solver_toolchain}` (3 occurrences) and ch5 references `\ref{app:geometric_inevitability}` (2 occurrences). Neither appendix is included by vol 5's `main.tex`. The labels are defined in `backmatter/05_universal_solver_toolchain.tex` and `backmatter/03_geometric_inevitability.tex` respectively, but `01_appendices.tex` does not `\input` these files. These will compile as undefined references.

3. **Dangling cross-volume chapter reference** — Ch3 references `\ref{ch:quantum_mechanics}` four times (in the "Dual-Formalism Architecture" section, lines ~508-608). This label is defined in Vol 2 (the quantum mechanics chapter), not in vol 5. Will compile as an undefined reference within vol 5.

4. **Dangling section reference `sec:n_coop_derivation`** — Ch2 (line 611) refers to `\ref{sec:n_coop_derivation}` as the location of the "full dual derivation from Axioms 1 and 2" of the cooperative amplification constant n_coop = 9. This label is not defined anywhere in vol 5 or in any of the shared backmatter files included by vol 5. It may be intended for a future appendix or a different volume.

5. **Chapter naming mismatch** — The file `05_folding_roadmap.tex` has the chapter title "Multi-Path TL Network Solver" (not a "folding roadmap"). The filename reflects an older working title. This is purely cosmetic but may cause confusion when navigating by filename.

6. **No objectivebox / summarybox / exercisebox** — Every chapter in other volumes (notably vol 2 and vol 3) opens with an objectivebox and closes with a summarybox + exercisebox. Vol 5 uses none of these. The chapters begin directly with content. This is a structural inconsistency with the series pattern.

7. **Chapter 5 is the largest file in the series** (~2,500 lines, compared to ch4 at ~1,170 lines). It contains both the 2D network solver results and a very long "Research Avenues" section (subsections on neural circuitry, sleep, Alzheimer's, anesthesia, phantom limb, consciousness, EMDR — some of which duplicate content found in ch6). The boundary between ch5's "Research Avenues" and ch6's "Biophysics and Pharmacology" is blurry — there is conceptual overlap in the consciousness/anesthesia material.

8. **H-bond derivation confirmed as defined in vol 5** — `sec:hbond_derivation` is in ch2 of vol 5. The key results are: d_HB = 1.754 Angstrom (`eq:d_hbond`) and E_HB = 4.98 kcal/mol (`eq:E_hbond`). These are derived from the Op4 potential minimum plus the FCC void fraction projection (1 - phi ~= 0.2595). The reference in memory that vol 3 references vol 5 for this derivation is consistent — vol 5 is the source.

9. **Common translation table included inline** — Ch3 (line 752) inputs `../common/translation_protein.tex` directly within the chapter body (inside a section). The same table is also included by `../backmatter/01_appendices.tex` -> App A. This produces a **duplicate table** (`tab:trans_protein`) in the compiled document. LaTeX will warn about a duplicate label `tab:trans_protein`.

10. **Two separate `sec:s11_cascade` and `sec:multiscale_energy` labels at the same line** — In ch4, lines 1096-1097 define both `\label{sec:s11_cascade}` and `\label{sec:multiscale_energy}` on consecutive lines with no intervening section command. Both labels point to the same content block. This is unusual but not a LaTeX error (both will resolve to the same page).
