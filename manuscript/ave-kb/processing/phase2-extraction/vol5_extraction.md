# Vol 5 — Phase 2 Extraction

**Volume:** `manuscript/vol_5_biology/`
**Taxonomy reference:** `.claude/phase1-taxonomy/vol5_taxonomy.md`
**Extraction date:** 2026-04-02
**Status:** Complete — all skeleton positions mapped

---

## Source Directory Listing

```
vol_5_biology/
  main.tex
  chapters/
    _manifest.tex
    01_biophysics_intro.tex
    02_organic_circuitry.tex           (661 lines)
    03_deterministic_protein_folding.tex
    04_simulation_architecture.tex
    05_folding_roadmap.tex             (~2534 lines)
    06_biophysics_pharmacology.tex
  (backmatter via main.tex):
    ../backmatter/01_appendices.tex
```

Chapter labels (all confirmed):
- `ch:biophysics` — `01_biophysics_intro.tex` line 5
- `ch:biological_circuitry` — `02_organic_circuitry.tex`
- `ch:protein_folding` — `03_deterministic_protein_folding.tex` line 2
- `ch:protein_sim_architecture` — `04_simulation_architecture.tex` line 2
- `ch:network_solver` — `05_folding_roadmap.tex` line 3 — **PATH-STABLE CONFIRMED**
- `ch:biophysics_pharmacology` — `06_biophysics_pharmacology.tex`

---

## Vol 5 Translation Files (CONFIRMED)

- **translation-protein**: `manuscript/common/translation_protein.tex`
  - Label: `\label{tab:trans_protein}`
  - Caption: "Protein folding terminology: structural biology ↔ transmission line / circuit theory ↔ AVE derivation."
  - 16 data rows. Header comment: `% Canonical location: manuscript/common/translation_protein.tex`
  - Maps to: `ave-kb/common/translation-protein.md`

- **translation-protein-solver**: `manuscript/common/translation_protein_solver.tex`
  - Label: `\label{tab:trans_protein_solver}`
  - Caption: "Protein solver domain translation." Maps biology → EE/RF → AVE Axiom → Script Reference.
  - Header comment: `% Canonical location: manuscript/common/translation_protein_solver.tex`
  - Maps to: `ave-kb/common/translation-protein-solver.md`

**Both files are in `manuscript/common/` (NOT in `manuscript/vol_5_biology/`).** The taxonomy reference to `ave-kb/vol5/common/` is incorrect; both translation tables go to the shared `ave-kb/common/` directory.

---

## PATH-STABLE Anchor Confirmation

### 1. hbond-op4-equilibrium.md — `sec:hbond_derivation`

**Source:** `02_organic_circuitry.tex`, **line 448**
**Status: CONFIRMED**

- `\label{sec:hbond_derivation}` at line 448
- `d_HB = 1.754~\text{\AA}` at line 487 (eq:d_hbond) — CONFIRMED
- `E_HB = 4.98~\textbf{kcal/mol}` at lines 505–506 (eq:E_hbond + prose, text: "exactly $\mathbf{4.98~\textbf{kcal/mol}}$") — CONFIRMED

### 2. membrane-phase-buffering.md — `sec:membrane_phase_buffering`

**Source:** `02_organic_circuitry.tex`, **line 571**
**Status: CONFIRMED**

- `\label{sec:membrane_phase_buffering}` at line 571
- Contains: `eq:cooperative_strain`, `eq:T_c_membrane`, `eq:cholesterol_yield`, `fig:cholesterol_topological_phase_buffer`

### 3. network-solver/index.md — `ch:network_solver`

**Source:** `05_folding_roadmap.tex`, **line 3**
**Status: CONFIRMED**

- `\label{ch:network_solver}` at line 3, immediately following `\chapter{...}` command

---

## Skeleton-to-Source Mapping

### Ch.1 — Biophysics Introduction (`vol5/biophysics-intro/`)

Source: `01_biophysics_intro.tex`

| Skeleton leaf | Source section | Key markers | Notes |
|---|---|---|---|
| `index.md` | ch01 chapter node | `ch:biophysics` | Summary position |
| `protein-backbone-proton-radius.md` | §1.1 `sec:protein_bridge` (line 8) | resultbox "Proton-to-Backbone Length Scale", `fig:protein_backbone` | NOTE: `sec:protein_bridge` label is duplicate — see Anomaly A1 |
| `derivation-chain-lattice-pitch.md` | §1.2 "Derivation Chain: From Lattice Pitch to Bond Length" | no label | Leaf |
| `amino-acid-impedance-classification.md` | §1.3 "Amino Acid Impedance Classification" | no label | Leaf |
| `chignolin-validation.md` | §1.4 "Validation: Chignolin (CLN025)" | resultbox "Chignolin Validation" | Leaf |
| `chiral-fret-parallax.md` | §1.5 "Molecular Chiral FRET Parallax" | no label | Leaf |

---

### Ch.2 — Organic Circuitry (`vol5/organic-circuitry/`)

Source: `02_organic_circuitry.tex` (661 lines)

| Skeleton leaf | Source section | Key markers | Notes |
|---|---|---|---|
| `index.md` | ch02 chapter node | `ch:biological_circuitry` | Summary position |
| `electromechanical-transduction-constant.md` | §2.1 "The Electromechanical Transduction Constant" | resultbox, `eq:xi_topo` | Leaf |
| `mass-to-inductance.md` | §2.2 "Mass → Inductance: L = m/ξ²" | resultbox "Topological Inductance of an Atom", `eq:L_atom`, `tab:inductances` | Leaf |
| `bond-stiffness-to-capacitance.md` | §2.3 "Bond Stiffness → Capacitance: C = ξ²/k" | resultbox "Topological Capacitance of a Bond", `eq:C_bond`, `tab:capacitances` | Leaf |
| `self-consistency-verification.md` | §2.4 "Self-Consistency Verification" | `eq:f_check`, `eq:Z_check`, `eq:v_check` | Leaf |
| `transceiver-backbone.md` | §2.5 "The Transceiver Backbone" | — | Leaf |
| `thermal-thz-noise.md` | §2.6 "The Biological Power Supply: Thermal THz Noise" | — | Leaf |
| `r-group-filter-stack.md` | §2.7 "The R-Group Filter Stack" | — | Leaf |
| `chirality-phase-polarity.md` | §2.8 "Chirality as Phase Polarity" | — | Leaf |
| `simulation-results-zero-parameter.md` | §2.9 "Simulation Results: Zero-Parameter Prediction" | `fig:amino_resonance` | Leaf |
| `ftir-falsification-test.md` | §2.10 "FTIR Falsification Test" | `fig:ftir_comparison` | Leaf |
| `peptide-chain-extension-test.md` | §2.11 "Peptide Chain Extension Test" | `fig:chain_sensitivity` | Leaf |
| `batch-spice-20-amino-acids.md` | `sec:batch_spice` | `tab:batch_resonance`, `fig:batch_resonance` | Leaf |
| `first-principles-bond-force-constants.md` | `sec:first_principles_k` | resultbox "Projected Macroscopic Force Constant", `eq:projected_k`, `tab:first_principles_k` | Leaf |
| `hbond-op4-equilibrium.md` | `sec:hbond_derivation` (line 448) | `d_HB=1.754Å`, `E_HB=4.98 kcal/mol`, `tab:translation_matrix` | **PATH-STABLE** |
| `membrane-phase-buffering.md` | `sec:membrane_phase_buffering` (line 571) | `eq:cooperative_strain`, `eq:T_c_membrane`, `eq:cholesterol_yield`, `fig:cholesterol_topological_phase_buffer` | **PATH-STABLE** |

---

### Ch.3 — Deterministic Protein Folding (`vol5/protein-folding/`)

Source: `03_deterministic_protein_folding.tex`

| Skeleton leaf | Source section | Key markers | Notes |
|---|---|---|---|
| `index.md` | ch03 chapter node | `ch:protein_folding` | Summary position |
| `ave-topological-impedance.md` | §3.1 "AVE Topological Impedance" + "Quantitative Z_topo" | resultbox "Topological Impedance", `eq:z_topo_def`, `eq:z_topo_derivation`, `tab:z_topo_values` | Leaf |
| `multiplexed-basis-states.md` | §3.2 "Multiplexed Basis States" | `fig:protein_folding_3d_collapse` | Leaf |
| `gradient-descent-engine.md` | §3.3 "The 3D Gradient Descent Engine" | `eq:excluded_volume`, `eq:backbone_hooke`, `fig:protein_folding_helix`, `fig:protein_folding_sheet` | Leaf |
| `s11-strain-transmission-line.md` | §3.4 "SPICE Transmission Line Mismatch (S11 Strain)" | `fig:protein_spice_folding`, `eq:chirality` | Leaf |
| `stress-test-20-sequence.md` | `sec:stress_test` | `tab:stress_test`, `fig:protein_spice_folding` | Leaf |
| `backbone-eigenvalue-solver.md` | `sec:backbone_eigenvalue` | — | Leaf — NOTE: `app:solver_toolchain` dangling ref (Anomaly A2) |
| `s11-feedback-gain.md` | §3.7 "S11 Feedback Gain Modulation" | resultbox, `eq:s11_feedback` | Leaf |
| `s11-objective-function.md` | `sec:s11_minimiser` | resultbox "S11 Objective Function", `eq:s11_energy` | Leaf |
| `ramachandran-derivation.md` | `sec:ramachandran_derivation` | `fig:ramachandran_steric`, `fig:ramachandran_correlation`, `tab:ramachandran_validation` | Leaf |
| `rmsd-benchmark-pdb.md` | `sec:rmsd_benchmark` | `tab:rmsd_benchmark`, `tab:s11_comparison`, `tab:autodiff` | Leaf |
| `op2-crossing-correction.md` | `sec:op2_crossing` | resultbox "Op2 Crossing Correction (Protein Scale)", `eq:op2_protein`, `eq:gauss_linking` | Leaf |
| `op2-vs-op9.md` | §3.12 "Op2 vs. Op9: Complementary Corrections" | — | Leaf |
| `dual-formalism-architecture.md` | `sec:dual_formalism` | resultbox "Dual-Formalism Architecture (Protein)", `tab:dual_formalism` | Leaf — NOTE: `ch:quantum_mechanics` dangling cross-vol ref (Anomaly A3) |
| `terminology-translation.md` | `sec:terminology` | `\input{../common/translation_protein.tex}` at line 752 | Leaf → cross-ref to `ave-kb/common/translation-protein.md` (Anomaly A5) |
| `predicted-extensions.md` | `sec:protein_bridge` (Ch.3 instance, line 765) | — | Leaf — NOTE: duplicate label (Anomaly A1) |

---

### Ch.4 — Simulation Architecture (`vol5/simulation-architecture/`)

Source: `04_simulation_architecture.tex`

| Skeleton leaf | Source section | Key markers | Notes |
|---|---|---|---|
| `index.md` | ch04 chapter node | `ch:protein_sim_architecture` | Summary position |
| `axiom-derived-constants.md` | §4.1 "Tier 1: Axiom-Derived Constants" | `tab:engine_constants_protein` | Leaf |
| `z-topo-complex-table.md` | `sec:z_topo_table` (Tier 2) | resultbox "Topological Charge Reactance", `tab:z_topo_complex` | Leaf |
| `dielectric-saturation-amplification.md` | within `sec:z_topo_table` | resultbox "Dielectric Saturation Amplification", `eq:c_sat` | Leaf — two leaves from one section |
| `physics-layers-1-4.md` | §4.? "Tier 3: Physics Layers" Layers 1–4 | — | Leaf |
| `physics-layers-5-8.md` | §4.? "Tier 3: Physics Layers" Layers 5–8 | — | Leaf |
| `segment-characteristic-impedance.md` | `sec:z_topo_table` + segment impedance | resultbox "Segment Characteristic Impedance", `eq:z_seg_full`, `eq:abcd_lossy` | Leaf |
| `solver-architecture.md` | `sec:solver_architecture` | resultbox "Eigenvalue Root Target", `eq:eigenvalue_target`; resultbox "SPICE Transient Equations of Motion", `eq:spice_velocity`; `tab:code_equation_map` | Leaf |
| `script-reproduction-procedure.md` | §4.? "Script Reproduction Procedure" | `tab:dependencies` | Leaf |
| `zero-parameter-count.md` | §4.? "Summary: Zero-Parameter Count" | `tab:operator_crossref`, `tab:saturation_operators` | Leaf |
| `stress-test-v3.md` | `sec:stress_test_v3` | `tab:stress_test_v3`, `tab:validation_5atom`, `tab:validation_four_proteins` | Leaf |
| `validation-villin-hp35.md` | `sec:validation_results` | — | Leaf |
| `validation-three-protein.md` | `sec:validation_three_protein` | `tab:yshunt_balance`, `tab:qdecay_results` | Leaf |
| `limitations-1d-cascade.md` | `sec:1d_limitations` | — | Leaf |
| `ss-recovery-design-path.md` | `sec:ss_recovery` | `tab:mosfet_mapping` | Leaf |
| `architectural-ceiling-theorem.md` | `sec:architectural_ceiling` | `tab:ceiling_evidence` | Leaf |
| `multiscale-impedance-architecture.md` | `sec:multiscale_architecture` | `tab:multiscale_mapping`, `tab:v7_results` | Leaf — NOTE: `sec:s11_cascade` / `sec:multiscale_energy` are co-located dual labels in same content block (Taxonomy Design Note 4) |

---

### Ch.5 — Folding Roadmap / Network Solver (`vol5/network-solver/`) — PATH-STABLE DOMAIN

Source: `05_folding_roadmap.tex` (~2534 lines)
Chapter label: `ch:network_solver` at line 3 — **PATH-STABLE CONFIRMED**
Contains: `\input{../common/translation_protein_solver.tex}` at line 1826 (within `sec:translation_matrix`)

| Skeleton leaf | Source section | Key markers | Notes |
|---|---|---|---|
| `index.md` | ch05 chapter node | `ch:network_solver` | Summary / **PATH-STABLE** anchor |
| `cascade-to-network-architecture.md` | `sec:cascade_to_network` | `eq:y_matrix_tl`, `eq:schur`, `eq:s11_network`, `tab:2d_benchmark` | Leaf |
| `compaction-physics.md` | `sec:compaction` | `eq:tau_min`, resultbox "Folding Speed Limit", `tab:speed_limit` | Leaf |
| `folding-speed-limit.md` | `sec:tau_fold` | resultbox "Full Kramers Folding Time", `eq:tau_fold`, `fig:tau_fold_validation`, `tab:tau_fold` | Leaf |
| `benchmark-results.md` | `sec:2d_benchmark` | `tab:v3v4`, `tab:v4_benchmark` | Leaf |
| `analysis-2d.md` | `sec:2d_analysis` | `tab:loss_decomp`, `tab:impedance_landscape` | Leaf |
| `pdb-validation-20-protein.md` | `sec:pdb_validation` | `tab:20pdb`, `fig:tau_fold_validation` | Leaf |
| `dynamic-allostery.md` | `sec:allostery` | `tab:allostery` | Leaf |
| `beta-sheet-antiparallel-coupler.md` | `sec:beta_sheet` | resultbox "Beta-Sheet Antiparallel Coupling", `tab:beta_bench` | Leaf |
| `bend-discontinuity-admittance.md` | `sec:bend_admittance` | resultbox "Bend Discontinuity Admittance", `tab:bend_consensus`, `tab:bend_bench` | Leaf |
| `ramachandran-basins-steric.md` | `sec:rama_derived` | resultbox "Derived Ramachandran Basins", `fig:smith` | Leaf |
| `backbone-y-parameters.md` | `sec:y_matrix` | resultbox "Backbone Y-Parameters", `tab:ymatrix_magnitude`, `tab:constants_audit` | Leaf |
| `eigenvalue-root-target-v5.md` | `sec:eigenvalue_v5` | resultbox "Eigenvalue Root Target (v5)", `eq:eigenvalue_target_v5` | Leaf |
| `spice-transient-equations-v5.md` | `sec:spice_v7` | resultbox "SPICE Transient Equations" + resultbox "SPICE Damping: Two Channels", `eq:R_damp_total` | Leaf |
| `roadmap.md` | `sec:2d_roadmap` | — | Leaf |
| `environment-parameter-sensitivity.md` | `sec:env_sweep` | `tab:env_params`, `tab:env_sweep_results` | Leaf |
| `complete-circuit-model.md` | `sec:complete_circuit` | `fig:circuit`, `tab:bio_circuit_map` | Leaf |
| `v7-segmented-cascade.md` | `sec:v7_cascade` | resultbox "v7 Segmented Cascade", `tab:v7_benchmark`, `tab:segmentation_validation` | Leaf |
| `translation-matrix-bio-ee-ave.md` | `sec:translation_matrix` | `tab:op_catalog`; `\input{../common/translation_protein_solver.tex}` at line 1826 | Leaf → cross-ref to `ave-kb/common/translation-protein-solver.md` |
| `y-matrix-gradient-architecture.md` | `sec:ymatrix_gradient` / `sec:freq_domain` | `tab:fft_results`, `tab:fft_init_benchmark` | Leaf |
| `neural-tl-network.md` | `sec:neural_tl` | `tab:eeg_modes`, `tab:research_avenues` (partial) | Leaf |
| `sleep-recalibration.md` | `sec:sleep_recalibration` | — | Leaf (Research Avenues subsection) |
| `alzheimers-impedance.md` | `sec:alzheimers` | — | Leaf (Research Avenues subsection) |
| `anesthesia-ch5.md` | `sec:anesthesia` | — | Leaf (Research Avenues subsection) — NOTE: overlaps with `sec:consciousness` in Ch.6 |
| `eeg-modes.md` | `sec:eeg_modes` | — | Leaf (Research Avenues subsection) |
| `phantom-limb.md` | `sec:phantom_limb` | — | Leaf (Research Avenues subsection) |
| `future-memory.md` | `sec:future_memory` | — | Leaf (Research Avenues subsection) |
| `broader-research-avenues.md` | `sec:broader_avenues` | `tab:research_avenues` (remainder) | Leaf |

Note: Research Avenues in Ch.5 are structured as `\section{Research Avenues}` → `\subsection{Neural Circuitry}` → nested `\subsubsection` labels (not top-level sections).

---

### Ch.6 — Biophysics and Pharmacology (`vol5/biological-applications/`)

Source: `06_biophysics_pharmacology.tex`

| Skeleton leaf | Source section | Key markers | Notes |
|---|---|---|---|
| `index.md` | ch06 chapter node | `ch:biophysics_pharmacology` | Summary position |
| `cancer-impedance-decoupling.md` | `sec:cancer_impedance` | — | Leaf |
| `red-light-therapy.md` | `sec:red_light_therapy` | — | Leaf |
| `methylene-blue-bridge.md` | `sec:methylene_blue` | — | Leaf |
| `creatine-neural-capacitor.md` | `sec:creatine_brain` | — | Leaf |
| `consciousness-cavity-eigenmode.md` | `sec:consciousness` | — | Leaf — NOTE: overlaps with `sec:anesthesia` in Ch.5 (Anomaly A7) |
| `emdr-impedance-annealing.md` | `sec:emdr` | — | Leaf |

---

## Empty Skeleton Positions

None confirmed. All 76 leaf positions have identified source content.

---

## Leaf Boundary Notes

1. **Ch.4 dual-label content block**: `sec:s11_cascade` and `sec:multiscale_energy` are co-located labels in Ch.4 at lines 1096–1097 (both label the same content block). The taxonomy places this content in `multiscale-impedance-architecture.md`. Distiller should note the dual label in the leaf metadata.

2. **Ch.3 `terminology-translation.md`**: The leaf maps to `sec:terminology` which contains `\input{../common/translation_protein.tex}` at line 752. The leaf should not reproduce the table verbatim; it should cross-reference `ave-kb/common/translation-protein.md`. The same translation table also appears in `../backmatter/01_appendices.tex` (Anomaly A5) — distiller should note this duplication in metadata.

3. **Ch.5 Research Avenues leaf granularity**: The Research Avenues block in Ch.5 is structured as a tree: `\section{Research Avenues}` → `\subsection{Neural Circuitry}` → `\subsubsection{Sleep Recalibration}`, etc. The taxonomy breaks these into 7 separate leaves (`sleep-recalibration.md` through `broader-research-avenues.md`). Each `\subsubsection` becomes one leaf. The `\subsection{Neural Circuitry}` content (before the first `\subsubsection`) goes into `neural-tl-network.md`.

4. **Ch.5 `translation-matrix-bio-ee-ave.md`**: The `\input{../common/translation_protein_solver.tex}` at line 1826 is inline within this leaf's section. The leaf should cross-reference `ave-kb/common/translation-protein-solver.md` rather than reproducing the table.

---

## Notation and Macro Notes

Standard shared macro set (see CLAUDE.md invariants). No Vol 5-specific macros identified.

Key Ch.2 / Ch.3 notation confirmed present in source:
- `\xi` — electromechanical transduction constant (defined inline, not a macro)
- `d_{OO}` — oxygen-oxygen distance (appears as raw LaTeX in Ch.2)
- `d_{HB}` — hydrogen bond length at equilibrium

Macro translation rules (from shared `commands.tex`):
- `\vacuum` → `\mathcal{M}_A`
- `\lp` → `\ell_{node}` (Vol 5 writes `\ell_{node}` directly; `\lp` macro not used in chapter bodies)
- All other shared macros apply per CLAUDE.md

---

## Ambiguities

### A1: Duplicate label `sec:protein_bridge`
**Locations:** Ch.1 line 8 AND Ch.3 line 765.
**Impact:** Both locations are PATH-STABLE candidates. The taxonomy uses `sec:protein_bridge` for the Ch.1 leaf (`protein-backbone-proton-radius.md`) and for the Ch.3 leaf (`predicted-extensions.md`). In LaTeX, the second occurrence overwrites the first. Cross-references to `sec:protein_bridge` resolve to Ch.3.
**Recommendation:** KB metadata for both leaves should document the duplicate; distiller should note which instance is the "intended" target of inbound refs.

### A2: Dangling `app:solver_toolchain` reference
**Location:** Ch.3 `sec:backbone_eigenvalue`.
**Status:** `app:solver_toolchain` is defined in `backmatter/05_universal_solver_toolchain.tex` (Vol 2 App F). Vol 5 references it without including that backmatter file.
**Recommendation:** KB leaf `backbone-eigenvalue-solver.md` should carry a cross-volume pointer to `ave-kb/vol2/appendices/app-f-solver-toolchain/`.

### A3: Dangling `ch:quantum_mechanics` cross-volume reference
**Location:** Ch.3 `sec:dual_formalism`.
**Status:** `ch:quantum_mechanics` does not exist in Vol 2 source — the actual label is `ch:quantum_orbitals` (see Vol 2 PATH-STABLE mismatch documented in vol2_extraction.md). This is a dangling reference regardless.
**Recommendation:** KB leaf `dual-formalism-architecture.md` should note the intended target as `vol2/quantum-orbitals/ch7-quantum-mechanics/index.md` with a note that the source label is actually `ch:quantum_orbitals`.

### A4: Ch.4 chapter label difference
**Issue:** Some Ch.5 source locations reference `ch:sim_architecture` (shorter form) while the confirmed label in `04_simulation_architecture.tex` is `ch:protein_sim_architecture`. This inconsistency is within Vol 5 source.
**Recommendation:** Distiller writing Ch.4 KB index should document the confirmed label `ch:protein_sim_architecture` and note the shorter-form references.

### A5: Translation table appears in both Ch.3 body and backmatter appendices
**Issue:** `\input{../common/translation_protein.tex}` appears at Ch.3 line 752 AND in `../backmatter/01_appendices.tex`. This means the translation table is rendered twice in the Vol 5 PDF.
**Recommendation:** Both KB leaf positions (`terminology-translation.md` and the appendix leaf) should carry the same cross-reference to `ave-kb/common/translation-protein.md` with a note about the duplication.

### A6: `app:geometric_inevitability` dangling reference
**Location:** Ch.5.
**Status:** `app:geometric_inevitability` is defined in `backmatter/03_geometric_inevitability.tex` (Vol 6). Vol 5 references it without including that backmatter.
**Recommendation:** KB leaf carrying this reference should carry a cross-volume pointer to `ave-kb/vol6/appendix/geometric-inevitability/`.

### A7: `sec:consciousness` (Ch.6) overlaps with `sec:anesthesia` (Ch.5)
**Issue:** Both sections address consciousness/anesthesia from the same AVE perspective. The Ch.5 `anesthesia-ch5.md` leaf and Ch.6 `consciousness-cavity-eigenmode.md` leaf likely cross-reference each other.
**Recommendation:** Both leaves should carry explicit cross-references to each other.
