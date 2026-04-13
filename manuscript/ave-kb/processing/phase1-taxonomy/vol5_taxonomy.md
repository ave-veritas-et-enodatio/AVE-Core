# Phase 1 Taxonomy Design — Vol 5: Topological Biology & Molecular Circuitry

**Produced by:** kb-taxonomy-architect
**Date:** 2026-04-02
**Source survey:** `.claude/phase0-surveys/vol5_survey.md`
**KB output root:** `manuscript/ave-kb/`

---

## 1. Invariants

The following items from Vol 5 are candidates for `manuscript/ave-kb/CLAUDE.md`. Each passes the binary test: "must this statement be qualified when applied to any single domain?" — if yes, it stays in a domain document.

**INVARIANT-V5-1: Electromechanical transduction constant $\xi_{topo}$**
Definition: $\xi_{topo} = e / l_{node}$ (units: C/m). The bridge between AVE lattice parameters and mechanical/biological quantities. Used in Vol 5 (mass→inductance, bond stiffness→capacitance translations) and also in Vol 4 (circuit engineering derivations) and Vol 2 (atomic orbital mappings). Passes the "all domains" test if it is the universal coupling constant.
Source: `ch:biological_circuitry`, `eq:xi_topo`, resultbox "The Electromechanical Transduction Constant"
**Decision: INCLUDE in CLAUDE.md IF confirmed used in ≥2 other volumes. Provisionally flag for coordinator to verify.**

**INVARIANT-V5-2: Hydrogen bond results $d_{HB} = 1.754$ Å, $E_{HB} = 4.98$ kcal/mol**
Derived from Op4 equilibrium in Vol 5 Ch.2. Referenced from Vol 3. If these are the canonical AVE predictions for water/biology cross-volume, they belong in CLAUDE.md. However, the derivation is Vol 5-specific; only the final values qualify.
Source: `sec:hbond_derivation`, `eq:d_hbond`, `eq:E_hbond`
**Decision: The RESULT values belong in CLAUDE.md; the derivation lives in the leaf at `molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md`.**

**INVARIANT-V5-3: AVE operator numbering convention (Op2, Op3, Op4, Op9, Op14)**
Non-standard notation used across at least Vol 2 (knot operators), Vol 3 (phase transitions), Vol 4 (circuit analysis), and Vol 5 (protein folding). The naming convention itself (OpN = N-th topological operator) is cross-cutting.
Source: used throughout Vol 5; defined earlier in series
**Decision: INCLUDE convention definition in CLAUDE.md. Individual operator formulae stay in domain documents.**

**INVARIANT-V5-4: $S_{11}$ as free-energy functional**
Vol 5 uses $S_{11}$ (reflection coefficient) as a folding objective function — a non-standard use of S-parameter notation. This reuse is AVE-specific and may confuse agents navigating from Vol 4 (EE context) to Vol 5. A notation note in CLAUDE.md prevents misinterpretation.
Source: `eq:s11_feedback`, `eq:s11_energy`, `eq:s11_network`
**Decision: ADD a notation note to CLAUDE.md clarifying that $S_{11}$ is used both as standard EE reflection coefficient (Vol 4) and as a folding free-energy functional (Vol 5).**

**INVARIANT-V5-5: tcolorbox environments — shared across all volumes**
Already in scope for CLAUDE.md per cross-volume context. No new invariant; confirm `resultbox` is the only environment used in Vol 5 (0 uses of axiombox, simbox, circuitbox, codebox, objectivebox, examplebox, summarybox, exercisebox — confirmed by survey).

**NOT invariants (Vol 5-specific, stay in domain documents):**
- $Z_{topo}$ definition and table of values — biology-specific
- $N_{eff}$ unified mode loading — biology/bond-eigenvalue specific
- $P_C \approx 0.1834$ packing fraction — used in Vol 5 membrane analysis; cross-volume status unconfirmed
- FTIR falsification methodology — Vol 5-specific
- Translation tables `translation_protein.tex` / `translation_protein_solver.tex` — Vol 5-specific (see Section 5 below)

---

## 2. Domain Grouping Rationale

Vol 5 has 6 chapters and ~100-125 leaves. Three natural domains emerge from the chapter content:

| Domain | Chapters | Rationale |
|---|---|---|
| `molecular-foundations` | Ch.1 + Ch.2 | The atomic translation layer: lattice → mass/inductance/capacitance/H-bond. These establish the biological RLC model from first principles. Ch.1 is a ~85-line intro that derives the protein backbone length scale; Ch.2 (~661 lines) is the full derivation of the transduction framework. Both are prerequisites for everything that follows. |
| `protein-folding-engine` | Ch.3 + Ch.4 + Ch.5 | The solver stack: from Z_topo definition (Ch.3) through full simulation architecture (Ch.4) to the multi-path network solver (Ch.5). These three chapters are mechanistically sequential — Ch.3 defines the objective, Ch.4 implements it, Ch.5 extends to 2D networks. They form one engineering pipeline. |
| `biological-applications` | Ch.6 | Pharmacology, pathology, consciousness. No new derivations — applies the Vol 5 framework to medical/biological hypotheses. Kept separate because it has no resultboxes and is qualitatively different in epistemic status (predictions/hypotheses vs. derivations). |

A flat 6-chapter layout (no domain grouping) would place all ~100-125 leaves under `vol5/` with only chapter-level indices, which is navigable but loses the conceptual grouping that aids agent orientation. The 3-domain layout stays within 4-level depth (entry-point → vol5 → domain → chapter → leaf) — wait, that is 5 levels.

**Depth resolution**: To stay within 4 levels, the chapter level is collapsed into domain level for small chapters. Specifically:
- `molecular-foundations/` contains chapter-level subdirectories `biophysics-intro/` and `organic-circuitry/` (these are the chapter indices + their leaves)
- `protein-folding-engine/` contains `deterministic-folding/`, `simulation-architecture/`, and `network-solver/`
- `biological-applications/` contains leaves directly (no subdirectory) since Ch.6 has only 6-8 leaves — OR uses a single `pharmacology/` subdirectory

**Final depth**: entry-point.md → vol5/index.md → vol5/{domain}/index.md → vol5/{domain}/{chapter}/index.md → vol5/{domain}/{chapter}/{leaf}.md = 5 levels.

**Depth exception justification**: Vol 5 has ~100-125 leaves across only 6 chapters, with Ch.5 alone contributing 35-45 leaves. The domain grouping is conceptually essential (molecular vs. solver vs. application). Collapsing domain or chapter levels would either (a) put 40+ leaves under one index (unnavigable) or (b) make `biological-applications` structurally inconsistent with the other domains. The 5-level exception is warranted here — this is the "compellingly requires a fifth level" case from the depth constraint.

For `biological-applications/pharmacology/`: Ch.6 has 6-8 leaves. This domain-only index + chapter subdirectory adds one navigation hop but keeps structure consistent. Alternative: collapse Ch.6 leaves directly under `biological-applications/index.md` (4 levels for this branch). **Decision: flatten biological-applications — leaves sit directly under `biological-applications/`, with no chapter subdirectory. This branch stays at 4 levels. The two deeper domains retain 5 levels because their chapter indexes carry important Key Results summaries.**

---

## 3. Document Skeleton

### File tree with one-line content scope

Leaf nodes are marked `[leaf — verbatim]`. Chapter and domain index nodes are marked `[index]`. All resultbox leaves are explicitly enumerated.

```
ave-kb/
  CLAUDE.md                          — [index] Cross-cutting: notation (xi_topo, S11 dual-use, OpN convention, d_HB/E_HB values, tcolorbox environments, chapter label notation $\mathcal{M}_A$, ell_node Vol1 vs l_node other vols)
  entry-point.md                     — [index] Volume summaries (one paragraph each) + domain links; target <3000 tokens

  vol5/
    index.md                         — [index] Vol 5 overview: 3 domains, key results surface (xi_topo, Z_topo, d_HB, tau_fold, S11 minimiser), up-link to entry-point

    molecular-foundations/
      index.md                       — [index] Atomic translation layer: lattice→RLC, H-bond derivation, membrane phase; key results from both chapters; up-link to vol5/index.md

      biophysics-intro/
        index.md                     — [index] Ch.1 summary: protein backbone from proton radius, Chignolin validation, FRET parallax; up-link to molecular-foundations/index.md
        protein-backbone-proton-radius.md   — [leaf — verbatim] sec:protein_bridge (Ch.1): derivation chain from l_node to protein backbone length scale; fig:protein_backbone; resultbox "Proton-to-Backbone Length Scale"
        derivation-chain-lattice-pitch.md   — [leaf — verbatim] Ch.1 §"Derivation Chain: From Lattice Pitch to Bond Length": step-by-step numeric derivation
        amino-acid-impedance-classification.md — [leaf — verbatim] Ch.1 §"Amino Acid Impedance Classification": impedance taxonomy of 20 amino acids
        chignolin-validation.md             — [leaf — verbatim] Ch.1 §"Validation: Chignolin (CLN025)": resultbox "Chignolin Validation"; CLN025 predicted vs experimental
        chiral-fret-parallax.md             — [leaf — verbatim] Ch.1 §"Molecular Chiral FRET Parallax": chiral parallax geometry and FRET distance correction

      organic-circuitry/
        index.md                     — [index] Ch.2 summary: transduction constant, atomic RLC translation, amino acid circuit architecture, FTIR test, batch SPICE, H-bond, membrane buffering; key results; up-link to molecular-foundations/index.md
        electromechanical-transduction-constant.md — [leaf — verbatim] §"The Electromechanical Transduction Constant": resultbox; eq:xi_topo definition and derivation
        mass-to-inductance.md               — [leaf — verbatim] §"Mass → Inductance: L = m/ξ²": resultbox "Topological Inductance of an Atom"; eq:L_atom; tab:inductances
        bond-stiffness-to-capacitance.md    — [leaf — verbatim] §"Bond Stiffness → Capacitance: C = ξ²/k": resultbox "Topological Capacitance of a Bond"; eq:C_bond; tab:capacitances
        self-consistency-verification.md    — [leaf — verbatim] §"Self-Consistency Verification": eq:f_check, eq:Z_check, eq:v_check; mechanical frequency/impedance/speed cross-check
        transceiver-backbone.md             — [leaf — verbatim] §"The Transceiver Backbone" (amino acid circuit architecture): backbone RLC circuit model
        thermal-thz-noise.md                — [leaf — verbatim] §"The Biological Power Supply: Thermal THz Noise": noise source model for amino acid circuits
        r-group-filter-stack.md             — [leaf — verbatim] §"The R-Group Filter Stack": side-chain impedance filter classification
        chirality-phase-polarity.md         — [leaf — verbatim] §"Chirality as Phase Polarity": L/D chirality as +/- phase assignment
        simulation-results-zero-parameter.md — [leaf — verbatim] §"Simulation Results: Zero-Parameter Prediction": transfer function results; fig:amino_resonance
        ftir-falsification-test.md          — [leaf — verbatim] §"FTIR Falsification Test": AVE vs NIST comparison; fig:ftir_comparison; pass/fail criteria
        peptide-chain-extension-test.md     — [leaf — verbatim] §"Peptide Chain Extension Test": chain mass sensitivity; fig:chain_sensitivity
        batch-spice-20-amino-acids.md       — [leaf — verbatim] sec:batch_spice: batch transmission sweep; tab:batch_resonance; fig:batch_resonance
        first-principles-bond-force-constants.md — [leaf — verbatim] sec:first_principles_k: Fabry-Perot bond eigenvalue derivation; eq:fp_one_electron, eq:fp_two_electron, eq:n_eff_bond, eq:bond_eigenvalue, eq:pi_coupling, eq:lp_qfactor; tab:first_principles_k; resultbox "Projected Macroscopic Force Constant" (eq:projected_k)
        hbond-op4-equilibrium.md            — [leaf — verbatim] sec:hbond_derivation: Op4 potential minimum → d_HB=1.754Å (eq:d_hbond), E_HB=4.98 kcal/mol (eq:E_hbond); eq:gamma_oh, eq:dipole, eq:K_hbond, eq:dsat_hbond, eq:d_oo; tab:translation_matrix (vacuum lattice → water properties) [CROSS-VOLUME ANCHOR: referenced from Vol 3]
        membrane-phase-buffering.md         — [leaf — verbatim] sec:membrane_phase_buffering: LLCP wedge topology; eq:cooperative_strain, eq:T_c_membrane, eq:cholesterol_yield; fig:cholesterol_topological_phase_buffer; cholesterol as topological phase buffer

    protein-folding-engine/
      index.md                       — [index] Solver stack overview: Z_topo (Ch.3), simulation architecture (Ch.4), 2D network solver (Ch.5); major results surface: S11 minimiser, tau_fold, 20-protein validation; up-link to vol5/index.md

      deterministic-folding/
        index.md                     — [index] Ch.3 summary: Z_topo definition, gradient descent engine, S11 objective, Op2 correction, dual-formalism, RMSD benchmark; key results; up-link to protein-folding-engine/index.md
        ave-topological-impedance.md        — [leaf — verbatim] §"AVE Topological Impedance": resultbox "Topological Impedance"; eq:z_topo_def, eq:z_topo_derivation; tab:z_topo_values
        z-topo-from-spice-backbone.md       — [leaf — verbatim] §"Quantitative Z_topo from SPICE Backbone Impedance": numeric derivation of Z_topo from ABCD backbone impedance
        multiplexed-basis-states.md         — [leaf — verbatim] §"Multiplexed Basis States": fig:protein_folding_3d_collapse; basis state superposition in folding
        gradient-descent-engine.md          — [leaf — verbatim] §"The 3D Gradient Descent Engine": eq:excluded_volume, eq:backbone_hooke; fig:protein_folding_helix, fig:protein_folding_sheet
        s11-strain-transmission-line.md     — [leaf — verbatim] §"SPICE Transmission Line Mismatch (S_11 Strain)": TL mismatch as conformational strain; eq:chirality
        stress-test-20-sequence.md          — [leaf — verbatim] sec:stress_test: 20-sequence stress test; tab:stress_test; fig:protein_spice_folding; pass criteria
        backbone-eigenvalue-solver.md       — [leaf — verbatim] sec:backbone_eigenvalue: backbone eigenvalue from universal solver; reference to app:solver_toolchain [NOTE: dangling ref — log anomaly]
        s11-feedback-gain.md                — [leaf — verbatim] §"S_11 Feedback Gain Modulation": resultbox "S_11 Feedback Gain Modulation (PID Error Signal)"; eq:s11_feedback
        s11-objective-function.md           — [leaf — verbatim] sec:s11_minimiser + §"S_11 Objective Function": resultbox "S_11 Objective Function"; eq:s11_energy (ABCD-derived); folding as pure impedance matching
        ramachandran-derivation.md          — [leaf — verbatim] sec:ramachandran_derivation: first-principles Z_topo; fig:ramachandran_steric, fig:ramachandran_correlation; tab:ramachandran_validation
        rmsd-benchmark-pdb.md               — [leaf — verbatim] sec:rmsd_benchmark: Kabsch RMSD vs PDB; tab:rmsd_benchmark; tab:s11_comparison; tab:autodiff
        op2-crossing-correction.md          — [leaf — verbatim] sec:op2_crossing: resultbox "Op2 Crossing Correction (Protein Scale)"; eq:op2_protein, eq:gauss_linking
        op2-vs-op9.md                       — [leaf — verbatim] §"Op2 vs. Op9: Complementary Corrections": comparison of crossing vs. charge corrections at protein scale
        dual-formalism-architecture.md      — [leaf — verbatim] sec:dual_formalism: resultbox "Dual-Formalism Architecture (Protein)"; atom↔protein mapping; tab:dual_formalism; cross-reference to Vol 2 ch:quantum_mechanics [NOTE: cross-volume dangling ref — log anomaly]
        terminology-translation.md          — [leaf — verbatim] sec:terminology: biology↔EE terminology mapping; tab:z_topo_values (cross-ref); current limitations; tab context
        predicted-extensions.md            — [leaf — verbatim] §"Predicted Extensions" (Ch.3, subsection of sec:terminology): forward-looking extensions of the dual-formalism [NOTE: source label was sec:protein_bridge in Ch.3 — slug differs from Ch.1 leaf to resolve duplicate; see anomaly note]

      simulation-architecture/
        index.md                     — [index] Ch.4 summary: 8-tier architecture, solver design, v3 stress test, architectural ceiling theorem, multi-scale architecture; key results; up-link to protein-folding-engine/index.md
        axiom-derived-constants.md          — [leaf — verbatim] §"Tier 1: Axiom-Derived Constants": tab:engine_constants_protein; derivation chain from Vol 1 axioms to simulation constants
        z-topo-complex-table.md             — [leaf — verbatim] sec:z_topo_table (Tier 2): resultbox "Topological Charge Reactance" + "Conjugate Shunt Admittance"; tab:z_topo_complex; complex Z_topo table
        dielectric-saturation-amplification.md — [leaf — verbatim] §"Tier 2" continued: resultbox "Dielectric Saturation Amplification"; saturation physics at high field
        physics-layers-1-4.md               — [leaf — verbatim] §"Tier 3: Physics Layers" (Layers 1-4): Coulomb/steric/dihedral/H-bond layers; eq:total_loss (partial)
        physics-layers-5-8.md               — [leaf — verbatim] §"Tier 3: Physics Layers" (Layers 5-8): electrostatic/solvation/chirality/normalization layers
        segment-characteristic-impedance.md  — [leaf — verbatim] sec:z_topo_table + §"Tier 3": resultbox "Segment Characteristic Impedance"; eq:z_seg_full; eq:abcd_lossy; ABCD matrix per backbone section
        solver-architecture.md              — [leaf — verbatim] sec:solver_architecture: Newton-Raphson eigenvalue; resultbox "Eigenvalue Root Target"; eq:eigenvalue_target; resultbox "SPICE Transient Equations of Motion"; eq:spice_velocity; tab:code_equation_map
        script-reproduction-procedure.md    — [leaf — verbatim] §"Script Reproduction Procedure": step-by-step reproduction of the S11 engine; tab:dependencies
        zero-parameter-count.md             — [leaf — verbatim] §"Summary: Zero-Parameter Count": enumeration of all derived constants; tab:operator_crossref; tab:saturation_operators
        stress-test-v3.md                   — [leaf — verbatim] sec:stress_test_v3: v3 engine stress test; tab:stress_test_v3; tab:validation_5atom; tab:validation_four_proteins
        validation-villin-hp35.md           — [leaf — verbatim] §"Validation: Villin HP35": Villin HP35 prediction vs experimental; folding pathway
        validation-three-protein.md         — [leaf — verbatim] §"Validation: Three-Protein Test": three-protein test; tab:yshunt_balance; tab:qdecay_results
        limitations-1d-cascade.md          — [leaf — verbatim] §"Limitations of the 1D Cascade": failure modes of cascade architecture; motivation for 2D
        ss-recovery-design-path.md          — [leaf — verbatim] sec:ss_recovery: secondary structure recovery; scale-invariant methodology; tab:mosfet_mapping
        architectural-ceiling-theorem.md    — [leaf — verbatim] sec:architectural_ceiling: ceiling theorem derivation; tab:ceiling_evidence
        multiscale-impedance-architecture.md — [leaf — verbatim] sec:multiscale_architecture: multi-scale architecture mapping; tab:multiscale_mapping; tab:v7_results

      network-solver/
        index.md                     — [index] Ch.5 summary: cascade→network transition, compaction physics, 20-protein PDB validation, tau_fold, allostery, Y-matrix gradient, research avenues overview; key results; up-link to protein-folding-engine/index.md [CROSS-VOLUME ANCHOR: ch:network_solver referenced from Vol 4]
        cascade-to-network-architecture.md  — [leaf — verbatim] sec:cascade_to_network: architecture transition from 1D cascade to 2D TL network; eq:y_matrix_tl, eq:schur, eq:s11_network; tab:2d_benchmark
        compaction-physics.md               — [leaf — verbatim] sec:compaction: compaction force model; eq:tau_min (folding speed limit); resultbox "Folding Speed Limit"; tab:speed_limit
        folding-speed-limit.md              — [leaf — verbatim] §"Folding Timescale from Backbone TL Physics" (sec:tau_fold): resultbox "Full Kramers Folding Time"; eq:tau_fold; fig:tau_fold_validation; tab:tau_fold
        benchmark-results.md                — [leaf — verbatim] sec:2d_benchmark: 1D vs 2D benchmark table; tab:v3v4; tab:v4_benchmark
        analysis-2d.md                      — [leaf — verbatim] sec:2d_analysis: analysis of 2D network improvements; tab:loss_decomp; tab:impedance_landscape
        pdb-validation-20-protein.md        — [leaf — verbatim] sec:pdb_validation: 20-protein PDB validation; tab:20pdb; fig:tau_fold_validation (cross-ref)
        dynamic-allostery.md                — [leaf — verbatim] sec:allostery: dynamic allostery via impedance perturbation; tab:allostery
        beta-sheet-antiparallel-coupler.md  — [leaf — verbatim] §"Beta-Sheet" under network solver: resultbox "Beta-Sheet Antiparallel Coupling"; tab:beta_bench
        bend-discontinuity-admittance.md    — [leaf — verbatim] §"Bend Discontinuity": resultbox "Bend Discontinuity Admittance"; tab:bend_consensus; tab:bend_bench
        ramachandran-basins-steric.md       — [leaf — verbatim] §"Derived Ramachandran Basins": resultbox "Derived Ramachandran Basins"; fig:smith; steric geometry → Ramachandran basin derivation
        backbone-y-parameters.md            — [leaf — verbatim] §"Backbone Y-Parameters": resultbox "Backbone Y-Parameters"; tab:ymatrix_magnitude; tab:constants_audit
        eigenvalue-root-target-v5.md        — [leaf — verbatim] §"Eigenvalue Root Target (v5)": resultbox "Eigenvalue Root Target (v5)"; v5-specific refinement vs Ch.4 version
        spice-transient-equations-v5.md     — [leaf — verbatim] §"SPICE Transient Equations" + §"SPICE Damping: Two Channels": resultbox "SPICE Transient Equations" + resultbox "SPICE Damping: Two Channels"; two-channel damping model
        roadmap.md                          — [leaf — verbatim] sec:2d_roadmap: development roadmap for 2D solver
        environment-parameter-sensitivity.md — [leaf — verbatim] sec:env_sweep: parameter sensitivity analysis; tab:env_params; tab:env_sweep_results
        complete-circuit-model.md           — [leaf — verbatim] sec:complete_circuit: complete circuit model with all layers; fig:circuit; tab:bio_circuit_map
        v7-segmented-cascade.md             — [leaf — verbatim] sec:v7_cascade: resultbox "v7 Segmented Cascade"; tab:v7_benchmark; segmented cascade cotranslational model; tab:segmentation_validation
        translation-matrix-bio-ee-ave.md    — [leaf — verbatim] sec:translation_matrix: translation matrix biology→EE→AVE; tab:op_catalog
        y-matrix-gradient-architecture.md   — [leaf — verbatim] sec:ymatrix_gradient: Y-matrix gradient descent architecture; tab:fft_results; tab:fft_init_benchmark
        neural-tl-network.md                — [leaf — verbatim] sec:neural_tl (under Research Avenues): neural circuitry as TL network; tab:eeg_modes; tab:research_avenues (partial)
        sleep-recalibration.md              — [leaf — verbatim] sec:sleep_recalibration (under Research Avenues): sleep as impedance recalibration
        alzheimers-impedance.md             — [leaf — verbatim] sec:alzheimers (under Research Avenues): Alzheimer's as impedance decoupling hypothesis
        anesthesia-ch5.md                   — [leaf — verbatim] sec:anesthesia (under Research Avenues): anesthesia as cavity eigenmode collapse [NOTE: overlaps with ch6 sec:consciousness — see cross-ref below]
        eeg-modes.md                        — [leaf — verbatim] sec:eeg_modes (under Research Avenues): EEG cortical mode predictions
        phantom-limb.md                     — [leaf — verbatim] sec:phantom_limb (under Research Avenues): phantom limb as persistent TL resonance
        future-memory.md                    — [leaf — verbatim] sec:future_memory (under Research Avenues): future directions for memory encoding
        broader-research-avenues.md         — [leaf — verbatim] sec:broader_avenues: broader biological research avenues; tab:research_avenues (remainder)

    biological-applications/
      index.md                       — [index] Ch.6 overview: 6 application domains (cancer, red light, methylene blue, creatine, consciousness, EMDR); epistemic status note (hypotheses/predictions, no resultboxes); up-link to vol5/index.md
      cancer-impedance-decoupling.md  — [leaf — verbatim] sec:cancer_impedance: cancer as impedance decoupling from normal tissue circuits
      red-light-therapy.md            — [leaf — verbatim] sec:red_light_therapy: red light as impedance-matched photon absorption; frequency matching mechanism
      methylene-blue-bridge.md        — [leaf — verbatim] sec:methylene_blue: methylene blue as molecular impedance bridge; electron transport chain
      creatine-neural-capacitor.md    — [leaf — verbatim] sec:creatine_brain: creatine as neural decoupling capacitor; ATP buffering model
      consciousness-cavity-eigenmode.md — [leaf — verbatim] sec:consciousness: consciousness as macroscopic cavity eigenmode; frequency predictions [NOTE: overlaps with sec:anesthesia in Ch.5 — see cross-ref]
      emdr-impedance-annealing.md     — [leaf — verbatim] sec:emdr: EMDR as impedance annealing of trauma defects; phase-locked oscillation mechanism

    common/
      translation-protein.md          — [leaf — verbatim] Vol 5-specific translation table: biology ↔ AVE vacuum lattice (source: ../common/translation_protein.tex); tab:trans_protein [NOTE: also input inline in Ch.3 — duplicate table anomaly; canonical KB location is here]
      translation-protein-solver.md   — [leaf — verbatim] Vol 5-specific translation table: protein solver ↔ EE notation (source: ../common/translation_protein_solver.tex)
```

---

## 4. Navigation Spec

### Up-link format

Every document except `ave-kb/entry-point.md` carries exactly one up-link on line 1:

```markdown
[↑ Vol 5: Topological Biology](../../index.md)
```

Exact formats at each level:

| Level | Document | Up-link target | Example |
|---|---|---|---|
| Volume index | `ave-kb/vol5/index.md` | entry-point | `[↑ AVE Knowledge Base](../entry-point.md)` |
| Domain index | `ave-kb/vol5/molecular-foundations/index.md` | vol5/index.md | `[↑ Vol 5: Topological Biology](../index.md)` |
| Chapter index | `ave-kb/vol5/molecular-foundations/organic-circuitry/index.md` | domain index | `[↑ Molecular Foundations](../index.md)` |
| Leaf | `ave-kb/vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md` | chapter index | `[↑ Organic Circuitry](../index.md)` |
| Direct-under-domain leaf (biological-applications) | `ave-kb/vol5/biological-applications/cancer-impedance-decoupling.md` | domain index | `[↑ Biological Applications](../index.md)` |
| common/ leaf | `ave-kb/vol5/common/translation-protein.md` | vol5/index.md | `[↑ Vol 5: Topological Biology](../index.md)` |

### Leaf marker

Line 2 of every leaf:
```
<!-- leaf: verbatim -->
```

### Down-link format

Index documents carry a **Contents** section at the bottom listing children with one-line descriptions:

```markdown
## Contents

- [Electromechanical Transduction Constant](electromechanical-transduction-constant.md) — resultbox; eq:xi_topo; xi_topo = e/l_node definition
- [Mass → Inductance](mass-to-inductance.md) — resultbox; eq:L_atom; L = m/xi^2; tab:inductances
...
```

### Cross-reference format

Structural links (required for navigation) use plain markdown links.
Cross-volume dependency pointers (primary — agent must follow to get the definition):
```markdown
> → Primary: [Quantum Mechanics Chapter](../../vol2/quantum-mechanics/index.md) — ch:quantum_mechanics; Op2 crossing correction references this
```

Optional suggestions (agent may or may not follow):
```markdown
> ↗ See also: [Anesthesia (Ch.5 Research Avenues)](../protein-folding-engine/network-solver/anesthesia-ch5.md) — Ch.5 treats anesthesia as cavity collapse from TL perspective
```

### Cross-volume reference: Vol 3 → sec:hbond_derivation

Vol 3's KB documents that reference this derivation should use:
```markdown
> → Primary: [H-bond Op4 Equilibrium](../../vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md) — sec:hbond_derivation; d_HB=1.754Å, E_HB=4.98 kcal/mol
```

The path `ave-kb/vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md` is stable and must not be renamed during distillation. This constraint must appear in the leaf file itself as a comment:
```
<!-- path-stable: referenced from vol3 as sec:hbond_derivation -->
```

### Cross-volume reference: Vol 4 → ch:network_solver

Vol 4 KB documents referencing the network solver chapter should use:
```markdown
> → Primary: [Multi-Path TL Network Solver](../../vol5/protein-folding-engine/network-solver/index.md) — ch:network_solver; Vol 4 Ch.1 prose reference
```

---

## 5. Shared Content Decision

### Biology-specific translation tables

**`translation_protein.tex`** and **`translation_protein_solver.tex`** appear only in Vol 5. No other volume in the 8-volume series uses these tables.

**Recommendation: place at `ave-kb/vol5/common/`** (not `ave-kb/common/`).

**Reasoning:**
- A `ave-kb/common/` path implies multi-volume relevance. These tables are Vol 5-specific by definition (biology ↔ AVE mapping). Placing them at `ave-kb/common/` would signal cross-volume relevance that does not exist.
- `ave-kb/vol5/common/` keeps them co-located with the volume that uses them while signaling they are reusable within Vol 5 (both by Ch.3 inline and by App A).
- The anomaly (Ch.3 inputs `translation_protein.tex` inline AND App A includes it via `backmatter/01_appendices.tex`) means the distiller will encounter the content twice. The canonical KB location is `ave-kb/vol5/common/translation-protein.md`. Ch.3 leaves that reference this table point to it with a cross-reference; they do not reproduce it.

**For the other shared translation tables** (`translation_circuit.tex`, `translation_qm.tex`, `translation_particle_physics.tex`, `translation_gravity.tex`, `translation_cosmology.tex`, `translation_condensed_matter.tex`): these appear in multiple volumes and belong at `ave-kb/common/` — outside this volume's taxonomy scope but noted here for coordinator reference.

---

## 6. Anomalies That Affect Taxonomy Design

From the survey, these anomalies require structural decisions:

### A1. Duplicate label `sec:protein_bridge`
**Structural impact**: Two different sections in Ch.1 and Ch.3 carry the same LaTeX label.
**KB resolution**:
- Ch.1 section "Protein Backbone: From Proton Radius to Folding" → `protein-backbone-proton-radius.md`
- Ch.3 subsection "Predicted Extensions" → `predicted-extensions.md`
Neither KB slug contains "protein-bridge". A note in both files documents the original label and the disambiguation:
```
<!-- original-label: sec:protein_bridge (DUPLICATE — disambiguated in KB) -->
```

### A2. Dangling references `app:solver_toolchain` and `app:geometric_inevitability`
**Structural impact**: Ch.3 references `app:solver_toolchain` (3 occurrences) and Ch.5 references `app:geometric_inevitability` (2 occurrences). Neither appendix is included in Vol 5.
**KB resolution**: The leaf files `backbone-eigenvalue-solver.md` and (Ch.5 equivalents) carry an anomaly note: `<!-- anomaly: app:solver_toolchain not included in vol5/main.tex — cross-volume appendix, unresolved -->`. No cross-reference link is added. The coordinator should decide whether these appendices belong in a separate KB tree.

### A3. Dangling cross-volume chapter reference `ch:quantum_mechanics` (4 occurrences in Ch.3)
**Structural impact**: `dual-formalism-architecture.md` references Vol 2.
**KB resolution**: Add a `> → Primary:` pointer to the anticipated Vol 2 KB path for ch:quantum_mechanics. Path will be `ave-kb/vol2/{appropriate-subtree}/quantum-mechanics/index.md` — exact path TBD by Vol 2 taxonomy. Distiller should insert a placeholder reference; coordinator will fix the target path in Phase 1a.

### A4. Ch.5/Ch.6 boundary blur (consciousness/anesthesia)
**Structural impact**: `sec:anesthesia` in Ch.5 Research Avenues and `sec:consciousness` in Ch.6 overlap conceptually.
**KB resolution**: Both live in their respective chapter trees. `anesthesia-ch5.md` carries: `> ↗ See also: [Consciousness as Cavity Eigenmode](../../../biological-applications/consciousness-cavity-eigenmode.md)`. `consciousness-cavity-eigenmode.md` carries: `> ↗ See also: [Anesthesia (Ch.5)](../protein-folding-engine/network-solver/anesthesia-ch5.md)`. These are optional (not structural). The distiller preserves each source verbatim — no merging.

### A5. Duplicate table `tab:trans_protein` (Ch.3 inline + App A)
**Structural impact**: Table content will appear twice in source. KB canonical location is `ave-kb/vol5/common/translation-protein.md`. The Ch.3 leaf that contains the inline input (`terminology-translation.md` is the most likely host — see Ch.3 sec:terminology which is close to line 752 where the input occurs) should reference the common leaf rather than reproducing the table.
**KB resolution**: Distiller instruction: when encountering `\input{../common/translation_protein.tex}` inline in Ch.3, do NOT reproduce the content — instead insert: `> → Primary: [Protein Translation Table](../../common/translation-protein.md)`.

### A6. Dangling reference `sec:n_coop_derivation`
**Structural impact**: Ch.2 line 611 references a section that exists nowhere in Vol 5 or shared backmatter.
**KB resolution**: `membrane-phase-buffering.md` (nearest Ch.2 section) carries: `<!-- anomaly: sec:n_coop_derivation is undefined — missing section or future appendix -->`. No dead link added.

### A7. Chapter 5 filename mismatch (`05_folding_roadmap.tex` vs. chapter title "Multi-Path TL Network Solver")
**Structural impact**: cosmetic only. KB uses the chapter title, not the filename. Directory slug: `network-solver/` (derived from chapter label `ch:network_solver`).

---

## 7. Acceptance Criteria

The following properties must hold when Vol 5's KB section is complete. Each is mechanically verifiable.

**AC1 — Up-link completeness**
Every `.md` file under `ave-kb/vol5/` except `ave-kb/vol5/index.md` begins with a line matching `^\[↑ `.
Check: `find /path/to/ave-kb/vol5 -name '*.md' ! -name 'index.md' -path '*/vol5/*' | xargs grep -L '^\[↑ '` — must return empty (excluding vol5/index.md itself, which links to entry-point.md instead).
Correction: vol5/index.md carries `[↑ AVE Knowledge Base](../entry-point.md)` — include it in the check; result must be empty.

**AC2 — Leaf marker completeness**
Every leaf file (not index) has `<!-- leaf: verbatim -->` on line 2.
Check: `find /path/to/ave-kb/vol5 -name '*.md' ! -name 'index.md' | xargs grep -L '<!-- leaf: verbatim -->'` — must return empty (except `common/` leaves if they are marked instead as `<!-- leaf: verbatim -->`).

**AC3 — Duplicate protein_bridge disambiguation**
Neither `protein-backbone-proton-radius.md` nor `predicted-extensions.md` contains the string `protein-bridge` as a navigation slug or document title.
Check: `grep -r 'protein-bridge' ave-kb/vol5/` — must return zero matches (comment annotation is acceptable).

**AC4 — Stable cross-volume anchor for hbond_derivation**
The file `ave-kb/vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md` exists and contains `<!-- path-stable: referenced from vol3 as sec:hbond_derivation -->`.
Check: `test -f ave-kb/vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md && grep -l 'path-stable' ave-kb/vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md` — must succeed.

**AC5 — Stable cross-volume anchor for ch:network_solver**
The file `ave-kb/vol5/protein-folding-engine/network-solver/index.md` exists and contains `<!-- path-stable: referenced from vol4 as ch:network_solver -->`.
Check: `grep -l 'path-stable' ave-kb/vol5/protein-folding-engine/network-solver/index.md` — must succeed.

**AC6 — Entry-point token budget**
`ave-kb/entry-point.md` word count is under 2200 words.
Check: `wc -w ave-kb/entry-point.md` — must be < 2200.

**AC7 — Vol 5 index token budget**
`ave-kb/vol5/index.md` word count is under 2200 words.
Check: `wc -w ave-kb/vol5/index.md` — must be < 2200.

**AC8 — Depth constraint**
No file in `ave-kb/vol5/` is more than 5 directory levels below `ave-kb/` (i.e., path depth ≤ 5 slashes from ave-kb/).
Check: `find ave-kb/vol5 -name '*.md' | awk -F'/' 'NF>7'` — must return empty. (7 = ave-kb + vol5 + domain + chapter + leaf = 5 segments past root, so path components = base + 5 = depth check at NF>7 accounting for `ave-kb/vol5/domain/chapter/leaf.md`.)

**AC9 — All 27 resultboxes have dedicated leaves**
The 27 named resultboxes each correspond to exactly one leaf file. The resultbox title must appear verbatim in the leaf's content.
Check: for each resultbox title in the survey's list, `grep -rl "Proton-to-Backbone Length Scale" ave-kb/vol5/` (repeat for all 27) — each must return exactly one file.

**AC10 — No summarization at leaf level**
No leaf file under `ave-kb/vol5/` contains a `## Summary` or `## Overview` heading (which would signal rewriting rather than verbatim transcription).
Check: `grep -rl '## Summary\|## Overview' ave-kb/vol5/ | grep -v 'index.md'` — must return empty.

---

## 8. File Count Summary

| Category | Count |
|---|---|
| Index files (volume + domain + chapter level) | 10 |
| Leaf files: molecular-foundations/biophysics-intro | 5 |
| Leaf files: molecular-foundations/organic-circuitry | 13 |
| Leaf files: protein-folding-engine/deterministic-folding | 12 |
| Leaf files: protein-folding-engine/simulation-architecture | 16 |
| Leaf files: protein-folding-engine/network-solver | 22 |
| Leaf files: biological-applications (direct) | 6 |
| Leaf files: vol5/common | 2 |
| **Total leaf files** | **76** |
| **Total index files** | **10** |
| **Grand total** | **86** |

Note: The survey estimated 100-125 leaves. This design reaches 76 leaf files because several sections are grouped into single leaves where their content is tightly coupled (e.g., the two SPICE transient equations in Ch.5, the two SPICE transient resultboxes in Ch.4). The distiller should split any leaf that exceeds ~400 lines of source content (a reasonable single-leaf limit). Ch.5 is most at risk — if subsections under Research Avenues have >80 lines each, they warrant individual leaves as designed here (8 research-avenue leaves). The final count at distillation time may reach 90-110 depending on subsection line counts.

---

## 9. Design Notes for Coordinator

1. **Vol 2 ch:quantum_mechanics path**: `dual-formalism-architecture.md` needs a cross-reference to Vol 2's quantum mechanics chapter. The Vol 2 taxonomy must expose a stable path for `ch:quantum_mechanics`. Once Vol 2 taxonomy is complete, this cross-reference can be finalized.

2. **`ave-kb/common/` shared translation tables**: The 6 non-biology translation tables (`translation_circuit.tex` etc.) appear in multiple volumes and need `ave-kb/common/` leaves. This is outside Vol 5 scope but the coordinator should ensure those leaves exist before Vol 5 distillation begins (Ch.3 `sec:terminology` may reference them).

3. **`translation_protein.tex` duplicate table anomaly**: The inline `\input` in Ch.3 and the App A inclusion will both be encountered during Vol 5 distillation. The distillation instruction in AC10 context is: Ch.3 reference → cross-reference link to `ave-kb/vol5/common/translation-protein.md`; App A → distill verbatim into that common leaf.

4. **Ch.4 `sec:s11_cascade` + `sec:multiscale_energy` co-located labels**: Both resolve to the same content block. The `simulation-architecture/` chapter index should note this so the distiller doesn't create two separate leaf stubs for the same content.

5. **Research Avenues leaves (Ch.5)**: Eight research-avenue leaves (`neural-tl-network.md` through `broader-research-avenues.md`) are structural choices based on the labelled subsections in the survey. If source content is short (<40 lines each), the distiller may consolidate into 2-3 grouped leaves. The leaf slugs should match the section labels (sec:neural_tl, sec:sleep_recalibration, etc.) for traceability.
