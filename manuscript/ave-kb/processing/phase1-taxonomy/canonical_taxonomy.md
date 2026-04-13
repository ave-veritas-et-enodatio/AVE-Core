# AVE Knowledge Base — Canonical Phase 1 Taxonomy

**Produced by:** KB Coordinator (synthesized from 8 kb-taxonomy-architect outputs)
**Date:** 2026-04-02
**Revised:** 2026-04-02 (Phase 1a revision — 3 Critical findings resolved; 6 Warning findings addressed as §8 distiller guidance)
**Source inputs:** `.claude/phase1-taxonomy/vol{1-8}_taxonomy.md`
**KB output root:** `manuscript/ave-kb/`

---

## 1. CLAUDE.md Invariants

The following items are confirmed genuinely cross-cutting: each appears in ≥2 volumes and requires no qualification when applied to any single volume. These belong in `ave-kb/CLAUDE.md` and must NOT be duplicated in domain documents.

### 1.1 Notation and Rendering

**INVARIANT-N1: Vacuum medium notation**
$\mathcal{M}_A$ denotes the vacuum medium. Written directly in body text; do NOT use `\vacuum` macro (macro exists but is not used in chapter bodies across any volume). KB distillers must render as `$\mathcal{M}_A$` throughout.
*Confirmed by: vol1, vol2, vol3, vol4, vol5, vol6, vol7, vol8 (unanimous)*

**INVARIANT-N2: Lattice node spacing notation (vol-split)**
All volumes **except Vol 1** write `$l_{node}$` (roman ell). Vol 1 writes `$\ell_{node}$` (script ell). Distillers must preserve the source notation within each volume; do not normalize across volumes.
*Confirmed by: vol1 (script ell); vol6 (roman ell); coordinator context*

**INVARIANT-N3: AVE Operator numbering convention**
Topological operators are named OpN where N is the operator number. Known operators: Op2 (knot crossing correction), Op3 (small-signal impedance correction), Op4 (potential well / H-bond), Op8 (large-signal confirmation), Op9 (charge correction), Op14 (long-range coupling). The naming convention is cross-volume; individual operator formulae live in domain documents.
*Confirmed by: vol2, vol3, vol4, vol5 (explicit); vol7 (Op3, Op8 in Ch.4)*

**INVARIANT-N4: $S_{11}$ dual-use notation**
$S_{11}$ is used as the standard EE reflection coefficient in Vol 4 and Vol 7, AND as a folding free-energy functional / objective function in Vol 5. An agent navigating from Vol 4 to Vol 5 must not assume the same physical meaning. Both uses are intentional and AVE-specific.
*Confirmed by: vol4 (EE context), vol5 (biology context)*

**[RETRACTED — N5 was incorrectly placed here]**
Vol 8 raw-form notation policy ($Z_0$, $\mu_0$ instead of shorthand macros) is volume-local and does NOT belong in CLAUDE.md. It belongs in `vol8/NOTES.md` only. See Vol 8 distiller dispatch for the substitution rule.

### 1.2 Structural Conventions

**INVARIANT-S1: tcolorbox environments**
All volumes share these named environments: `resultbox`, `axiombox`, `simbox`, `examplebox`, `summarybox`, `exercisebox`, `circuitbox`, `codebox`, `objectivebox`. In KB markdown, each renders as a named blockquote with a bold environment-type prefix:
```markdown
> **[Resultbox]** *Title of the Result*
> Body content...
```
Individual volumes may use only a subset; resultbox is the most common. Vol 5 uses only resultbox. Vol 8 uses none.
*Confirmed by: vol1, vol2, vol3, vol4, vol5, vol6, vol7 (confirmed in surveys); vol8 (zero instances)*

**INVARIANT-S2: AVE Axiom numbering**
The four AVE axioms carry stable meanings across all volumes:
- Axiom 1: ABCD cascade / coupled amplitude
- Axiom 2: Topological phase dislocation
- Axiom 3: Least reflected action
- Axiom 4: SiLU / saturation gate (dielectric saturation)
*Confirmed by: vol1 (originating), vol8 (re-instantiated in virtual media domain)*

**INVARIANT-S3: Shared experimental appendix**
`common/appendix_experiments.tex` (Unified Index of Experimental Falsifications) is not owned by any volume. Its canonical KB location is `ave-kb/common/appendix-experiments.md`. Each volume that includes this file points to the canonical location; it is never duplicated in a volume tree.
*Confirmed by: vol7, vol8 (explicit); implied by vol1, vol3, vol4 context*

**INVARIANT-S4: Up-link format**
Every KB document except `ave-kb/entry-point.md` begins with exactly one up-link on line 1:
```markdown
[↑ Parent Name](../index.md)
```
The `↑` character (U+2191) is the machine-checkable marker. Pattern: `^\[↑ `.
*Confirmed by: all 8 volumes (unanimous)*

**INVARIANT-S5: Leaf marker**
Line 2 of every leaf document (non-index):
```markdown
<!-- leaf: verbatim -->
```
*Confirmed by: all 8 volumes (unanimous)*

### 1.3 Cross-Volume Physical Constants

**INVARIANT-C1: Dielectric yield limit**
$V_{\text{yield}} \approx 43.65\,\text{kV}$ is defined in Vol 4 Ch.1. When this value appears in any KB document outside Vol 4, it must carry a cross-reference primary pointer to its Vol 4 definition.
*Confirmed by: vol4 (definition), vol3, vol6, vol7 (references without qualification)*

**INVARIANT-C2: Electromechanical transduction constant**
$\xi_{topo} = e / l_{node}$ (units: C/m). The bridge between AVE lattice parameters and mechanical/biological quantities. Used in Vol 2 (atomic orbital mappings), Vol 4 (circuit engineering derivations), and Vol 5 (mass→inductance, bond stiffness→capacitance translations). Canonical definition: Vol 5 `organic-circuitry/electromechanical-transduction-constant.md`.
*Confirmed by: vol5 (proposes as CLAUDE.md invariant, ≥3 volumes)*

**INVARIANT-C3: H-bond canonical values**
$d_{HB} = 1.754\,\text{Å}$ and $E_{HB} = 4.98\,\text{kcal/mol}$ are the canonical AVE predictions for the hydrogen bond equilibrium distance and energy, derived from Op4 potential minimum in Vol 5. Referenced from Vol 3. The result values belong here; the derivation lives in `vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md`.
*Confirmed by: vol5 (derivation), vol3 (cross-volume reference)*

**INVARIANT-C4: Z-proportionality regimes**
Two distinct impedance scaling regimes in the AVE framework:
- Physical/biological media: $Z \propto 1/A$
- Virtual media (LLM / information topology): $Z \propto A$
This inversion defines the hardware/software isomorphism. Cross-referenced from Vols 1, 2, 5, and 8.
*Confirmed by: vol8 (explicit); vol1 (foundation); vol2, vol5 (biological context)*

### 1.4 Cross-Reference Formats

**INVARIANT-F1: Primary cross-volume dependency**
When a KB document requires the reader to navigate to another location to get a definition, use:
```markdown
> → Primary: [Document Name](relative/path/to/target.md) — brief rationale (source label if known)
```

**INVARIANT-F2: Optional cross-volume suggestion**
When a KB document suggests (but does not require) navigation to a related location:
```markdown
> ↗ See also: [Document Name](relative/path/to/target.md) — brief rationale
```

Cross-volume references appear in index documents and in leaf documents where the source text explicitly references another section. They must never paraphrase or summarize the target content.

---

## 2. Hierarchy Specification

### 2.1 Depth Rules

- **Standard maximum depth**: 4 levels below `ave-kb/` (entry-point → vol → domain → chapter → leaf)
- **Approved exception**: Vol 5 uses 5 levels for `molecular-foundations/` and `protein-folding-engine/` branches due to Ch.5 alone contributing 22+ leaves. Biological-applications branch stays at 4 levels.
- **Vol 6**: 4 levels (entry-point → vol6 → period or framework → element or subtopic → leaf)
- **Vol 8**: 4 levels (entry-point → vol8 → domain → chapter → leaf); no chapter-level subdirectories

### 2.2 Naming Conventions

- Directory slugs: `kebab-case`, derived from chapter label keys where available, otherwise from chapter titles
- Chapter directories: `ch{N}-{slug}` (e.g., `ch4-phase-transitions`)
- Section leaves: `s{NN}-{slug}.md` (e.g., `s03-melting-eigenmode.md`)
- Named-result leaves: `{concept-slug}.md` (e.g., `hbond-op4-equilibrium.md`)
- Index files: always named `index.md`
- Vol 6 element standard leaves use template names: `structure-isotope-stability.md`, `vacuum-density-flux.md`, `ee-equivalent.md`, `topological-area.md`, `orbital-knot-topology.md`, `semiconductor-regime.md`

### 2.3 What Belongs at Each Level

| Level | File | Content |
|---|---|---|
| Root | `entry-point.md` | One paragraph per volume (≤2200 words total); links to all 8 vol indexes + common |
| Root | `CLAUDE.md` | All invariants from §1 above; nothing domain-specific |
| Common | `common/` | Shared translation tables, unified experiments appendix |
| Volume | `vol{N}/index.md` | Volume summary; 3–6 domain links; key results surface (≤2200 words) |
| Domain | `{domain}/index.md` | Domain overview; chapter links; Key Results section (verbatim from children); Derivations section (down-link index) |
| Chapter | `{chapter}/index.md` | Chapter summary; leaf links; Key Results; Derivations |
| Leaf | `{slug}.md` | Verbatim LaTeX→Markdown translation; up-link + leaf marker |

---

## 3. Complete Document Skeleton

Leaf counts are taken from individual volume taxonomy designs. Index counts include vol, domain, and chapter levels. Cross-volume anchor paths are marked `[PATH-STABLE]`.

### 3.1 Root and Common

**CANONICAL AUTHORITY NOTE**: This `common/` skeleton supersedes all per-volume taxonomy proposals for `common/` content. Vol 1's per-volume taxonomy proposed additional backmatter files (`full-derivation-chain.md`, `geometric-inevitability.md`, `mathematical-closure.md`, `solver-toolchain.md`, `appendices-overview.md`) and different translation table slugs. The definitive file list is below.

**Translation table slug resolution**: The exact filenames in `manuscript/common/translation_*.tex` must be confirmed by the Phase 2 `kb-latex-specialist` for Vol 1. The provisional slugs below are derived from vol5 survey which listed actual filenames. If Phase 2 finds different filenames, Phase 3 distillers must use the confirmed names.

**Geometric-inevitability placement**: `backmatter/03_geometric_inevitability.tex` content is owned by Vol 6 (it is the Vol 6 backmatter). It lives at `vol6/appendix/geometric-inevitability/` (10 detailed leaves). Cross-references from other volumes point there. It does NOT appear in `common/`.

```
ave-kb/
  CLAUDE.md                                    [index] — all §1 invariants (excluding retracted N5)
  entry-point.md                               [index] — one paragraph per volume; max 200 words/vol; total <2200 words

  common/
    index.md                                   [index] — common content directory; up-link to entry-point.md
    appendix-experiments.md  [PATH-STABLE]     [leaf — verbatim] — Unified Index of Experimental Falsifications (source: common/appendix_experiments.tex; label: app:unified_experiments); NOTE: vol1 taxonomy used slug experiments-appendix.md — SUPERSEDED by this canonical slug
    full-derivation-chain.md                   [leaf — verbatim] — Complete AVE derivation chain (source: backmatter/02_full_derivation_chain.tex; label: app:full_derivation_chain); referenced from Vol 1 and others
    solver-toolchain.md                        [leaf — verbatim] — Universal solver toolchain (source: backmatter/05_universal_solver_toolchain.tex; label: app:solver_toolchain); contains eq:ave_qnm_eigenvalue; referenced from Vol 5 (dangling ref)
    mathematical-closure.md                    [leaf — verbatim] — System verification trace (source: backmatter/12_mathematical_closure.tex; label: app:verification); referenced from Vol 1
    appendices-overview.md                     [leaf — verbatim] — App A–E overview and translation matrix index (source: backmatter/01_appendices.tex preamble; label: app:translation_matrix); referenced from Vol 1
    translation-tables/
      index.md                                 [index] — translation table directory; up-link to common/index.md
      translation-circuit.md                   [leaf — verbatim] — EE/circuit ↔ AVE notation (source: common/translation_circuit.tex or equivalent; CONFIRM filename at Phase 2)
      translation-qm.md                        [leaf — verbatim] — Quantum mechanics ↔ AVE notation (source: common/translation_qm.tex or equivalent; CONFIRM filename at Phase 2)
      translation-particle-physics.md          [leaf — verbatim] — Particle physics/nuclear ↔ AVE notation (source: common/translation_particle_physics.tex or equivalent; CONFIRM filename at Phase 2)
      translation-gravity.md                   [leaf — verbatim] — Gravity/galactic ↔ AVE notation (source: common/translation_gravity.tex; CONFIRM filename at Phase 2)
      translation-cosmology.md                 [leaf — verbatim] — Cosmology ↔ AVE notation (source: common/translation_cosmology.tex or equivalent; CONFIRM filename at Phase 2)
      translation-condensed-matter.md          [leaf — verbatim] — Condensed matter/BCS/thermo ↔ AVE notation (source: common/translation_condensed_matter.tex or equivalent; CONFIRM filename at Phase 2)
```

**Up-link rule for common/ root leaves**: `appendix-experiments.md`, `full-derivation-chain.md`, `solver-toolchain.md`, `mathematical-closure.md`, `appendices-overview.md` all up-link to `common/index.md` (not to entry-point.md directly). This is design decision (A) per Phase 1a cycle-2 finding N3. `common/index.md` in turn up-links to `entry-point.md`. Maximum hop count from any common/ root leaf to entry-point = 2 hops (leaf → common/index → entry-point).

**Phase 2 instruction for common/ translation tables**: The `kb-latex-specialist` assigned to Vol 1 must enumerate all files matching `manuscript/common/translation_*.tex` and report exact filenames. If additional translation domains exist beyond the 6 listed, new leaves must be added. If some provisional slugs above do not match actual files, slug corrections must be reported to the coordinator before Phase 3 distillation begins.

Common totals: 13 files in common/ subtree (2 index + 5 root leaves + 6 table leaves). The 2 index files are common/index.md and common/translation-tables/index.md — there is no separate "table-index" term; that index is already in the count. For the "Root + common" row in §6, add CLAUDE.md + entry-point.md to get 15 total.

### 3.2 Vol 1 — Foundations

Source: `vol_1_foundations/`; 3 domains, 7 chapters (+Ch.0 intro), ~58 leaves

**Ch.0 placement**: Per vol1 taxonomy architect's explicit design, Ch.0 (no resultboxes, no labels, ~55 lines) is a **standalone leaf at the volume root** (`vol1/ch0-intro.md`), not inside a domain. The `vol1/index.md` Contents section must link to it directly alongside the 3 domain links. This supersedes the canonical synthesis's earlier placement at `axioms-and-lattice/`.

**Ch.4 directory slug**: The correct slug (per vol1 taxonomy) is `ch4-continuum-electrodynamics`, not `ch4-field-regimes`. This is the path used for Vol 1 → Vol 6 cross-reference targets.

**Vol 1 invariant disposition**: The vol1 per-volume taxonomy proposed 11 CLAUDE.md invariants. The coordinator accepted: Four-Axiom Set (as INVARIANT-S2), Vacuum Manifold Symbol (as INVARIANT-N1), Node Length (as INVARIANT-N2), Dielectric Yield Voltage (as INVARIANT-C1), and partially the Universal Operators Symbol Convention (as INVARIANT-N3). Rejected from CLAUDE.md and belonging in Vol 1 domain indexes: `eq:master_wave` (→ `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`), Vacuum Impedance $Z_0$ (→ `vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`), Four Universal Regimes (→ `vol1/operators-and-regimes/ch7-regime-map/four-regimes.md`), Topo-Kinematic Isomorphism (→ `vol1/axioms-and-lattice/ch2-macroscopic-moduli/topo-kinematic-isomorphism.md`), Vacuum Porosity Ratio $\alpha$ (→ `vol1/axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md`).

```
vol1/
  index.md                                     [index] — Vol 1 overview: K4 lattice, AVE axioms, TLM dynamics; links to 3 domains AND to ch0-intro.md
  ch0-intro.md                                 [leaf — verbatim] — Ch.0 intro; no resultboxes, no labels; up-link to vol1/index.md; source: 00_intro.tex

  axioms-and-lattice/
    index.md                                   [index] — Ch.1-Ch.2 domain; axiom definitions, lattice constants, macroscopic moduli
    ch1-fundamental-axioms/
      index.md                                 [index]
      axiom-definitions.md                     [leaf — verbatim] — 4 axioms; eq:axiom1_impedance through eq:axiom4_saturation
      calibration-cutoff-scales.md             [leaf — verbatim]
      lc-condensate-vacuum.md                  [leaf — verbatim] — porosity ratio α
      zero-parameter-universe.md               [leaf — verbatim]
      kirchhoff-network-method.md              [leaf — verbatim]
      lattice-structure.md                     [leaf — verbatim] — xi_topo = e/ell_node definition
    ch2-macroscopic-moduli/
      index.md                                 [index]
      implosion-paradox.md                     [leaf — verbatim]
      constitutive-moduli.md                   [leaf — verbatim]
      topo-kinematic-isomorphism.md            [leaf — verbatim] — dimensional isomorphism table
      dielectric-rupture.md                    [leaf — verbatim]
      dielectric-snap-limit.md                 [leaf — verbatim] — V_snap = 511.0 kV

  dynamics/
    index.md                                   [index] — Ch.3-Ch.4 domain
    ch3-quantum-signal-dynamics/
      index.md                                 [index] — 9 leaves
      dielectric-lagrangian.md                 [leaf — verbatim]
      paley-wiener-hilbert.md                  [leaf — verbatim]
      gup-derivation.md                        [leaf — verbatim]
      schrodinger-from-circuit.md              [leaf — verbatim]
      zero-impedance-boundary.md               [leaf — verbatim]
      quantum-foam-virtual.md                  [leaf — verbatim]
      ohmic-decoherence-born.md                [leaf — verbatim]
      nonlinear-telegrapher.md                 [leaf — verbatim]
      entanglement-mechanism.md                [leaf — verbatim]
    ch4-continuum-electrodynamics/             ← CORRECT SLUG (not ch4-field-regimes)
      index.md                                 [index] — key results: eq:master_wave, eq:H_infinity, a_genesis
      master-equation.md                       [leaf — verbatim] — eq:master_wave
      lc-electrodynamics.md                    [leaf — verbatim] — rho_bulk, nu_kin
      operating-regimes-table.md               [leaf — verbatim]
      magnetic-saturation.md                   [leaf — verbatim]
      mond-hoop-stress.md  [PATH-STABLE]       [leaf — verbatim] — sec:galactic_saturation; a_genesis=cH_inf/2pi; eq:H_infinity; <!-- path-stable: referenced from vol6 as eq:H_infinity and sec:galactic_saturation -->
      dark-sector.md                           [leaf — verbatim]
      bullet-cluster.md                        [leaf — verbatim]

  operators-and-regimes/
    index.md                                   [index] — Ch.5-Ch.7 domain
    ch5-universal-spatial-tension/
      index.md                                 [index] — 4 leaves
      mass-unification.md                      [leaf — verbatim]
      scale-invariance.md                      [leaf — verbatim]
      scale-invariant-predictions.md           [leaf — verbatim]
      fdtd-yee-proof.md                        [leaf — verbatim]
    ch6-universal-operators/
      index.md                                 [index] — 8 leaves; all 8 universal operators
      impedance-operator.md                    [leaf — verbatim] — sec:universal_impedance
      saturation-operator.md                   [leaf — verbatim] — sec:universal_saturation
      reflection-coefficient.md                [leaf — verbatim] — sec:universal_gamma
      pairwise-potential.md                    [leaf — verbatim] — sec:universal_pairwise
      y-to-s-conversion.md                     [leaf — verbatim] — sec:universal_y_to_s
      eigenvalue-target.md                     [leaf — verbatim] — sec:universal_eigenvalue
      spectral-analyser.md                     [leaf — verbatim] — sec:universal_spectral
      packing-reflection.md                    [leaf — verbatim] — sec:universal_packing
    ch7-regime-map/
      index.md                                 [index] — 5 leaves; regime map for ch:regime_map
      four-regimes.md                          [leaf — verbatim] — Regimes I-IV (r=A/A_c)
      domain-catalog.md                        [leaf — verbatim] — sec:domain_catalog; 8-domain table
      regime-equation-sets.md                  [leaf — verbatim] — eq:S_taylor
      dimensional-analysis.md                  [leaf — verbatim] — sec:dimensional_analysis
      experimental-design-space.md             [leaf — verbatim]
```

Vol 1 totals: defer to `.claude/phase1-taxonomy/vol1_taxonomy.md` §3 for definitive count (~11 index + ~58 leaves ≈ 69 files including ch0-intro.md; canonical skeleton above shows partial enumeration — full leaf list in per-volume taxonomy).

### 3.3 Vol 2 — Subatomic Physics

Source: `vol_2_subatomic/`; 5 domains, 12 chapters + 6 appendices, ~110 leaves

```
vol2/
  index.md                                     [index] — Vol 2 overview: particle-physics through backmatter

  particle-physics/
    index.md                                   [index] — Ch.1-Ch.6
    ch1-.../
      index.md  + leaves
    ...ch6-.../
      index.md  + leaves

  quantum-orbitals/  [PATH-STABLE: ch:quantum_mechanics anchor]
    index.md  [PATH-STABLE]                    [index] — Ch.7 quantum mechanics chapter; referenced from Vol 5 sec:dual_formalism_architecture
    ch7-quantum-mechanics/
      index.md                                 [index]
      [~8 leaves per vol2 taxonomy — LARGE CHAPTER ~3600 lines, may split further]

  foundations-validation/
    index.md                                   [index] — Ch.8-Ch.9
    ch8-.../
      index.md  + leaves
    ch9-.../
      index.md  + leaves

  open-problems/
    index.md                                   [index] — Ch.10-Ch.12
    ch10-.../  ch11-.../  ch12-.../
      index.md + leaves each

  backmatter/
    index.md                                   [index] — Appendices A-F
    appendix-a/ through appendix-f/
      index.md + leaves each
```

Vol 2 totals (per vol2 taxonomy): ~25 index + ~110 leaves ≈ 135 files
*Full leaf enumeration: see `.claude/phase1-taxonomy/vol2_taxonomy.md` §3*

### 3.4 Vol 3 — Macroscopic Physics

Source: `vol_3_macroscopic/`; 4 domains, 15 chapters, ~120 leaves
Outbound cross-volume refs: → Vol 4 `sec:k4_tlm`, → Vol 5 `sec:hbond_derivation`, → Vol 7 `sec:melting_eigenmode`

```
vol3/
  index.md                                     [index] — Vol 3 overview: gravity, cosmology, condensed-matter, applied-physics

  gravity/
    index.md                                   [index] — Ch.1-3, Ch.8
    ch1-.../  ch2-.../  ch3-.../  ch8-.../
      index.md + leaves each

  cosmology/
    index.md                                   [index] — Ch.4-6, Ch.14, Ch.15
    ch4-.../
      index.md + leaves
    ch05-dark-sector/                           ← NOTE: slug is ch05-dark-sector, NOT cosmology_v7
      index.md + leaves
    ch6-.../  ch14-.../  ch15-.../
      index.md + leaves each

  condensed-matter/
    index.md                                   [index] — Ch.9-11 (Ch.11 thermodynamics: 16 leaves)
    ch9-.../  ch10-.../
      index.md + leaves each
    ch11-thermodynamics/
      index.md                                 [index] — 16 individual leaves (subsection granularity)
      [16 subsection-level leaves per vol3 taxonomy]

  applied-physics/
    index.md                                   [index] — Ch.7, Ch.12, Ch.13
    ch7-.../  ch12-.../  ch13-.../
      index.md + leaves each
```

Vol 3 totals (per vol3 taxonomy): 22 index + ~120 leaves ≈ 142 files
*Full leaf enumeration: see `.claude/phase1-taxonomy/vol3_taxonomy.md` §3*

### 3.5 Vol 4 — Engineering

Source: `vol_4_engineering/`; 6 domains, 18 chapters, ~96 leaves
Outbound cross-volume refs: none confirmed in source
Note (Phase 2 correction): `ch:network_solver` was initially attributed to Vol 4 but is NOT present in vol_4_engineering/ source. The chapter lives in vol_5_biology/chapters/05_folding_roadmap.tex (Vol 5 Ch.5).

```
vol4/
  index.md                                     [index] — Vol 4 overview: circuit-theory through simulation

  circuit-theory/
    index.md                                   [index] — Ch.1-2
    ch1-.../  ch2-.../
      index.md + leaves each

  hardware-programs/
    index.md                                   [index] — Ch.3-6
    ch3-.../  ch4-.../  ch5-.../  ch6-.../
      index.md + leaves each

  advanced-applications/
    index.md                                   [index] — Ch.7-10, Ch.18
    ch7-.../  ch8-.../  ch9-.../  ch10-.../  ch18-.../
      index.md + leaves each

  falsification/
    index.md                                   [index] — Ch.11-12 (Ch.11: 21 leaves, 1 per protocol)
    ch11-falsification-protocols/
      index.md                                 [index]
      [21 leaves — 1 per falsification protocol]
    ch12-.../
      index.md + leaves

  future-geometries/
    index.md                                   [index] — Ch.13
    ch13-future-geometries/
      index.md                                 [index]
      k4-tlm-simulator.md  [PATH-STABLE]       [leaf — verbatim] — K4-TLM simulator; referenced from Vol 3 as sec:k4_tlm
      [other ch13 leaves per vol4 taxonomy]

  simulation/
    index.md                                   [index] — Ch.14-17 (SPICE chapters: 2 leaves each)
    ch14-.../  ch15-.../  ch16-.../  ch17-.../
      index.md + leaves each (2 leaves per SPICE chapter: theory + netlist)
```

Vol 4 totals (per vol4 taxonomy): 26 index + ~96 leaves ≈ 122 files
*Full leaf enumeration: see `.claude/phase1-taxonomy/vol4_taxonomy.md` §3*

### 3.6 Vol 5 — Topological Biology

Source: `vol_5_biology/`; 3 domains, 6 chapters, 76 leaves (may reach 90-110 at distillation time)
Outbound cross-volume refs: → Vol 2 `ch:quantum_mechanics`
Inbound cross-volume refs: ← Vol 3 `sec:hbond_derivation`
Note (Phase 2 correction): `ch:network_solver` (Vol 5 Ch.5, 05_folding_roadmap.tex) is Vol 5-internal; Vol 4 was erroneously listed as referencing it.

```
vol5/
  index.md                                     [index] — Vol 5 overview: molecular-foundations, protein-folding-engine, biological-applications

  common/
    index.md                                   [index] — Vol 5 local translation tables; up-link to vol5/index.md; NOTE: vol5/index.md Contents must list this directory explicitly
    translation-protein.md                     [leaf — verbatim] — biology ↔ AVE translation table (vol5-specific; source: common/translation_protein.tex); up-link to vol5/common/index.md
    translation-protein-solver.md              [leaf — verbatim] — protein solver ↔ EE notation (vol5-specific; source: common/translation_protein_solver.tex); up-link to vol5/common/index.md

  molecular-foundations/
    index.md                                   [index — DECLARED] — domain index for Ch.1-2; up-link to vol5/index.md; Contents links to biophysics-intro/ and organic-circuitry/; Key Results surfaces xi_topo, d_HB, E_HB values
    biophysics-intro/
      index.md                                 [index] — Ch.1 (5 leaves)
      protein-backbone-proton-radius.md        [leaf — verbatim] — sec:protein_bridge (Ch.1); <!-- original-label: sec:protein_bridge DUPLICATE -->
      derivation-chain-lattice-pitch.md        [leaf — verbatim]
      amino-acid-impedance-classification.md   [leaf — verbatim]
      chignolin-validation.md                  [leaf — verbatim]
      chiral-fret-parallax.md                  [leaf — verbatim]
    organic-circuitry/
      index.md                                 [index] — Ch.2 (13 leaves)
      electromechanical-transduction-constant.md  [leaf — verbatim] — xi_topo = e/l_node definition
      mass-to-inductance.md                    [leaf — verbatim]
      bond-stiffness-to-capacitance.md         [leaf — verbatim]
      self-consistency-verification.md         [leaf — verbatim]
      transceiver-backbone.md                  [leaf — verbatim]
      thermal-thz-noise.md                     [leaf — verbatim]
      r-group-filter-stack.md                  [leaf — verbatim]
      chirality-phase-polarity.md              [leaf — verbatim]
      simulation-results-zero-parameter.md     [leaf — verbatim]
      ftir-falsification-test.md               [leaf — verbatim]
      peptide-chain-extension-test.md          [leaf — verbatim]
      batch-spice-20-amino-acids.md            [leaf — verbatim]
      first-principles-bond-force-constants.md [leaf — verbatim]
      hbond-op4-equilibrium.md  [PATH-STABLE]  [leaf — verbatim] — sec:hbond_derivation; d_HB=1.754Å, E_HB=4.98 kcal/mol; <!-- path-stable: referenced from vol3 as sec:hbond_derivation -->
      membrane-phase-buffering.md              [leaf — verbatim]

  protein-folding-engine/
    index.md                                   [index] — Ch.3-5: Z_topo, simulation, 2D network solver
    deterministic-folding/
      index.md                                 [index] — Ch.3 (15 leaves)
      [15 leaves per vol5 taxonomy §3]
    simulation-architecture/
      index.md                                 [index] — Ch.4 (16 leaves)
      [16 leaves per vol5 taxonomy §3]
    network-solver/
      index.md                                 [index] — Ch.5 (05_folding_roadmap.tex); <!-- vol5-internal: ch:network_solver; no cross-volume path-stable requirement -->
      [22 leaves per vol5 taxonomy §3]

  biological-applications/
    index.md                                   [index] — Ch.6 (6 leaves; no chapter subdirectory)
    cancer-impedance-decoupling.md             [leaf — verbatim]
    red-light-therapy.md                       [leaf — verbatim]
    methylene-blue-bridge.md                   [leaf — verbatim]
    creatine-neural-capacitor.md               [leaf — verbatim]
    consciousness-cavity-eigenmode.md          [leaf — verbatim]
    emdr-impedance-annealing.md               [leaf — verbatim]
```

Vol 5 totals (per vol5 taxonomy): 10 index + 76 leaves + 2 common leaves = 88 files (includes vol5/common/index.md)
*Full leaf enumeration: see `.claude/phase1-taxonomy/vol5_taxonomy.md` §3*

### 3.7 Vol 6 — Periodic Table of Knots (Z=1–14)

Source: `vol_6_periodic_table/`; period-based grouping + framework + appendix, 119 leaves

```
vol6/
  index.md                                     [index] — Vol 6 overview

  framework/
    index.md                                   [index]
    mass-defect-summary.md                     [leaf — verbatim] — empirical vs topological mass H-Si
    executive-abstract.md                      [leaf — verbatim] — mathematical closure Z=1–28
    computational-mass-defect/
      index.md                                 [index] — 11 leaves; all 8 labelled equations
      mass-as-reactive-load.md                 [leaf — verbatim]
      topological-circuit-conventions.md       [leaf — verbatim]
      python-simulator.md                      [leaf — verbatim] — verbatim block → fenced code
      network-analytics.md                     [leaf — verbatim]
      nucleon-spacing-derivation.md            [leaf — verbatim] — eq:d_proton, eq:d_intra
      mutual-coupling-constant.md              [leaf — verbatim] — eq:k_mutual
      pn-junction-coupling.md                  [leaf — verbatim] — resultbox "Topologic Yield Mass Defect"
      abcd-transfer-matrix.md                  [leaf — verbatim]
      operating-regimes.md                     [leaf — verbatim]
      semiconductor-nuclear-analysis.md        [leaf — verbatim] — eq:semiconductor_mass, Miller avalanche
      radioactive-decay-impedance.md           [leaf — verbatim]
    chemistry-translation/
      index.md                                 [index] — 3 leaves; no \label in source chapter
      quantum-vs-topological-shells.md         [leaf — verbatim]
      lewis-dots-vsepr.md                      [leaf — verbatim]
      semiconductor-regime-chemistry.md        [leaf — verbatim]

  period-1/
    index.md                                   [index] — H, He
    hydrogen/
      index.md                                 [index] — Z=1; knot: trefoil 3_1; 6 standard leaves
      structure-isotope-stability.md           [leaf — verbatim]
      vacuum-density-flux.md                   [leaf — verbatim]
      ee-equivalent.md                         [leaf — verbatim]
      topological-area.md                      [leaf — verbatim]
      orbital-knot-topology.md                 [leaf — verbatim]
      semiconductor-regime.md                  [leaf — verbatim]
    helium/
      index.md                                 [index] — Z=2; 6 standard leaves
      [6 standard leaves]

  period-2/
    index.md                                   [index] — Li through Ne (8 elements)
    lithium/    index.md + 6 leaves            ← ANOMALY: duplicate fig:li7_density_equator — use 2nd
    beryllium/  index.md + 6 leaves
    boron/      index.md + 6 leaves            ← NOTE: no ch:boron label in source
    carbon/     index.md + 6 leaves            ← NOTE: no ch:carbon label in source
    nitrogen/   index.md + 6 leaves            ← NOTE: no ch:nitrogen label in source
    oxygen/     index.md + 6 leaves            ← NOTE: orbital section has no named subsection
    fluorine/   index.md + 6 leaves            ← §2 titled "Macroscopic Halo Offset" — preserve
    neon/       index.md + 7 leaves            ← EXTRA: curve-fitting-fallacy.md

  period-3/
    index.md                                   [index] — Na through Si (4 elements)
    sodium/     index.md + 7 leaves            ← EXTRA: core-proximity-effect.md
    magnesium/  index.md + 7 leaves            ← EXTRA: symmetric-shell-collapse.md; NOTE: topological-area source is 14_magnesium.tex not 13_magnesium.tex
    aluminum/   index.md + 7 leaves            ← EXTRA: gradual-halo-separation.md
    silicon/    index.md + 6 leaves            ← §2 titled "Symmetric Core Collapse" — preserve

  appendix/
    index.md                                   [index]
    heavy-element-catalog/
      index.md                                 [index] — Z=15-119
      mass-prediction-accuracy.md              [leaf — verbatim]
      full-element-table.md                    [leaf — verbatim] — longtable → Markdown table
      selected-heavy-orbital-topology.md       [leaf — verbatim]
      selected-heavy-strain-fields.md          [leaf — verbatim]
      selected-heavy-circuit-models.md         [leaf — verbatim]
    geometric-inevitability/
      index.md                                 [index] — dangling refs → Vol1+Vol5 cross-refs
      golden-ratio-min-impedance.md            [leaf — verbatim]
      fibonacci-packing-proxy.md               [leaf — verbatim]
      pi-topological-horizon.md                [leaf — verbatim]
      magic-numbers-shell-closure.md           [leaf — verbatim]
      platonic-progression.md                  [leaf — verbatim]
      derived-numerical-constants.md           [leaf — verbatim]
      g-star-derivation.md                     [leaf — verbatim]
      alpha-s-derivation.md                    [leaf — verbatim]
      lambda-higgs-derivation.md               [leaf — verbatim] — \cite{pdg2022} present
      conclusion-death-of-numerology.md        [leaf — verbatim]
```

Vol 6 totals (per vol6 taxonomy): 24 index + 119 leaves = 143 files

### 3.8 Vol 7 — Hardware & Future Work

Source: `vol_7_hardware/`; 3 domains, 6 chapters, 43 leaves
Inbound cross-volume refs: ← Vol 3 `sec:melting_eigenmode`

```
vol7/
  index.md                                     [index] — Vol 7 overview: propulsion, condensed-matter, astrophysical-predictions

  propulsion/
    index.md                                   [index] — Ch.1-2 domain
    ch1-metric-streamlining/
      index.md                                 [index] — flat structure (no Part I/II split); 10 leaves
      s01-metric-streamlining-electrodynamics.md  [leaf — verbatim]
      s02-active-inertial-cancellation.md      [leaf — verbatim]
      s03-impedance-rectification.md           [leaf — verbatim]
      s04-chiral-impedance-matching.md         [leaf — verbatim]
      s05-autoresonant-dielectric-rupture.md   [leaf — verbatim]
      s06-local-refractive-control.md          [leaf — verbatim]
      s07-inductive-origin-special-relativity.md  [leaf — verbatim]
      s08-active-impedance-control.md          [leaf — verbatim]
      s09-superluminal-transit.md              [leaf — verbatim]
      s10-hts-detector.md                      [leaf — verbatim]
    ch2-ave-resolutions/
      index.md                                 [index] — 10 leaves
      s01-lsi-nano-warp-bubble.md              [leaf — verbatim]
      s02-solar-flares-macroscopic-photons.md  [leaf — verbatim]
      s03-jwst-early-galaxies.md               [leaf — verbatim]
      s04-dama-libra-xenonnt.md                [leaf — verbatim]
      s05-quasiparticle-poisoning.md           [leaf — verbatim]
      s06-particle-accelerator-matrix.md       [leaf — verbatim]
      s07-lorentz-invariance-lattice-drag.md   [leaf — verbatim]
      s08-spin-half-fermions.md                [leaf — verbatim]
      s09-quantum-entanglement-bell.md         [leaf — verbatim]
      s10-ponder-01.md                         [leaf — verbatim]

  condensed-matter/
    index.md                                   [index] — Ch.3-4 domain
    ch3-superconductivity/
      index.md                                 [index] — 2 leaves
      s01-introduction.md                      [leaf — verbatim]
      s02-phase-locked-gear-train.md           [leaf — verbatim]
    ch4-phase-transitions/
      index.md                                 [index] — 5 leaves (from 3 source files; 03_melting_eigenmode.tex split into s03+s04+s05)
      s01-water-condensation.md                [leaf — verbatim]
      s02-turbulence-onset.md                  [leaf — verbatim]
      s03-melting-eigenmode.md  [PATH-STABLE]  [leaf — verbatim] — sec:melting_eigenmode; <!-- path-stable: referenced from vol3 as sec:melting_eigenmode -->
      s04-hoh-bond-angle.md                    [leaf — verbatim] — resultbox "H-O-H Bond Angle (Op3 Small-Signal)"
      s05-topological-cell-collapse.md         [leaf — verbatim] — resultbox "Topological Cell Collapse"

  astrophysical-predictions/
    index.md                                   [index] — Ch.5-6 domain
    ch5-white-dwarf-predictions/
      index.md                                 [index] — 8 leaves
      s01-motivation.md  through  s08-conclusions.md  [8 leaves — verbatim]
    ch6-bh-interior/
      index.md                                 [index] — 8 leaves
      s01-motivation.md  through  s08-conclusions.md  [8 leaves — verbatim]
```

Vol 7 totals (per vol7 taxonomy): 10 index + 43 leaves = 53 files
*Note: Ch.5 and Ch.6 heading-inside-file anomaly — distillers must not double-render the `\chapter{}` heading.*

### 3.9 Vol 8 — Virtual Media & Informational Topology

Source: `vol_8_virtual_media/`; 4 domains, 12 chapters, 43 leaves
No tcolorbox environments; leaf boundaries drawn at section level.

```
vol8/
  index.md                                     [index] — Vol 8 overview
  NOTES.md                                     [vol8-local] — raw notation policy; Z∝A inversion scope; pending-result conventions

  foundations/
    index.md                                   [index] — Ch.1-3 domain
    ch1-llm-topology/
      index.md                                 [index] — 3 leaves
      swiglu-twoport.md                        [leaf — verbatim]
      ac-thermodynamic.md                      [leaf — verbatim]
      axiom3-pruning.md                        [leaf — verbatim]
    ch2-hw-sw-inversion/
      index.md                                 [index] — 2 leaves
      inversion-split.md                       [leaf — verbatim]
      breakdown-paradox.md                     [leaf — verbatim]
    ch3-universal-operator/
      index.md                                 [index] — 4 leaves
      axiomatic-correspondences.md             [leaf — verbatim]
      axiom2-attention.md                      [leaf — verbatim]
      regime-map.md                            [leaf — verbatim]
      ffn-twoport.md                           [leaf — verbatim]

  saturation-pruning/
    index.md                                   [index] — Ch.4-6 domain
    ch4-experimental-audit/
      index.md                                 [index] — 5 leaves
      saturation-operator.md                   [leaf — verbatim]
      quantitative-results.md                  [leaf — verbatim] <!-- status: pending-autotune -->
      swiglu-density.md                        [leaf — verbatim]
      head-pruning-audit.md                    [leaf — verbatim]
      current-limitations.md                   [leaf — verbatim]
    ch5-global-ac-scope/
      index.md                                 [index] — 4 leaves
      per-layer-paradox.md                     [leaf — verbatim]
      global-ac-correction.md                  [leaf — verbatim] <!-- status: pending-autotune -->
      runtime-shift.md                         [leaf — verbatim]
      gamma-per-layer.md                       [leaf — verbatim]
    ch6-continuous-smoothing/
      index.md                                 [index] — 2 leaves
      gamma-prune-metric.md                    [leaf — verbatim]
      saturation-sr.md                         [leaf — verbatim]

  architecture-analysis/
    index.md                                   [index] — Ch.7-11 domain
    ch7-operator-unification/
      index.md                                 [index] — 3 leaves
      phase-tension.md                         [leaf — verbatim]
      operator-bindings.md                     [leaf — verbatim]
      hamiltonian-cusp.md                      [leaf — verbatim]
    ch8-discrete-masking/
      index.md                                 [index] — 6 leaves
      masking-protocol.md                      [leaf — verbatim]
      zeff-telemetry.md                        [leaf — verbatim]
      masking-failures.md                      [leaf — verbatim] — groups two starred subsections (continuous + binary failure)
      static-baking.md                         [leaf — verbatim]
      gamma-excision.md                        [leaf — verbatim]
      neuroplasticity.md                       [leaf — verbatim] — groups starred subsections
    ch9-gamma-scaling/
      index.md                                 [index] — 5 leaves
      gamma-thresholds.md                      [leaf — verbatim]
      autotune-results.md                      [leaf — verbatim] <!-- status: pending-autotune -->
      cascade-transfer.md                      [leaf — verbatim] — eq:gamma_scaling: T=(1-γ)^N
      transmission-budget.md                   [leaf — verbatim]
      density-constraint.md                    [leaf — verbatim]
    ch10-attention-impedance/
      index.md                                 [index] — 5 leaves
      qkv-impedance.md                         [leaf — verbatim]
      gqa-constraint.md                        [leaf — verbatim]
      impedance-distribution.md                [leaf — verbatim]
      intersection-constraint.md               [leaf — verbatim]
      axiom2-interpretation.md                 [leaf — verbatim]
    ch11-moe-impedance/
      index.md                                 [index] — 4 leaves
      dynamic-impedance.md                     [leaf — verbatim]
      router-axiom3.md                         [leaf — verbatim]
      moe-vs-static.md                         [leaf — verbatim]
      moe-prediction.md                        [leaf — verbatim] — groups testable prediction + hardware limitations

  activation-geometry/
    index.md                                   [index] — Ch.12 domain
    ch12-sigmoid-saturation/
      index.md                                 [index] — 6 leaves
      unit-circle-identity.md                  [leaf — verbatim] — σ²+r²=1 derivation; starred subsections sub-included
      zero-bias-prediction.md                  [leaf — verbatim]
      yield-limit-virtual.md                   [leaf — verbatim]
      regime-boundaries.md                     [leaf — verbatim]
      density-derivation.md                    [leaf — verbatim] — 97% density via error function
      implications.md                          [leaf — verbatim]

  appendix/
    index.md                                   [index] — pointer only
    unified-experiments-ref.md                 [leaf — cross-ref] — Vol 8 contributes no experiments; pointer to ave-kb/common/appendix-experiments.md
```

Vol 8 totals (per vol8 taxonomy): 22 index + 43 leaves + 1 NOTES.md = 66 files

---

## 4. Cross-Volume Reference Resolution

All cross-volume references have stable, unambiguous paths. These paths must not change after taxonomy is frozen.

| Source | Label | Stable KB Path | Type |
|---|---|---|---|
| Vol 3 → Vol 4 | `sec:k4_tlm` | `ave-kb/vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md` | primary |
| Vol 3 → Vol 5 | `sec:hbond_derivation` | `ave-kb/vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md` | primary |
| Vol 3 → Vol 7 | `sec:melting_eigenmode` | `ave-kb/vol7/condensed-matter/ch4-phase-transitions/s03-melting-eigenmode.md` | primary |
| Vol 5 → Vol 2 | `ch:quantum_mechanics` | `ave-kb/vol2/quantum-orbitals/ch7-quantum-mechanics/index.md` | primary |
| Vol 5 internal | `ch:network_solver` | `ave-kb/vol5/protein-folding-engine/network-solver/index.md` | Vol 5 Ch.5 (05_folding_roadmap.tex); no cross-volume reference confirmed |
| Vol 6 → Vol 1 | `eq:H_infinity` | `ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` | primary |
| Vol 6 → Vol 1 | `sec:galactic_saturation` | `ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` | primary |
| Vol 6 → Vol 5 | `sec:membrane_phase_buffering` | `ave-kb/vol5/molecular-foundations/organic-circuitry/membrane-phase-buffering.md` | primary |
| All vols | `appendix_experiments` | `ave-kb/common/appendix-experiments.md` | structural |
| All vols | `translation_circuit.tex` etc. | `ave-kb/common/translation-tables/{slug}.md` | structural |

**Path-stable comments**: Each path-stable leaf or index must contain a comment on line 3:
```
<!-- path-stable: referenced from {vol} as {label} -->
```

---

## 5. Navigation Specification

### 5.1 Up-Link Format by Level

| Document | Up-link target | Example |
|---|---|---|
| `entry-point.md` | (none — is root) | n/a |
| `vol{N}/index.md` | entry-point | `[↑ AVE Knowledge Base](../entry-point.md)` |
| `vol{N}/{domain}/index.md` | vol index | `[↑ Vol 4: Engineering](../index.md)` |
| `vol{N}/{domain}/{chapter}/index.md` | domain index | `[↑ Circuit Theory](../index.md)` |
| `vol{N}/{domain}/{chapter}/{leaf}.md` | chapter index | `[↑ Ch.1 Circuit Analysis](../index.md)` |
| `vol5/biological-applications/{leaf}.md` | domain index | `[↑ Biological Applications](../index.md)` |
| `vol5/{domain}/{chapter}/{leaf}.md` (5-level) | chapter index | `[↑ Organic Circuitry](../index.md)` |
| `vol5/common/{leaf}.md` | vol5/common/index.md | `[↑ Vol 5 Translation Tables](../index.md)` |
| `vol6/{period}/{element}/{leaf}.md` | element index | `[↑ Hydrogen](../index.md)` |
| `vol6/{period}/{element}/index.md` | period index | `[↑ Period 1](../index.md)` |
| `vol6/{period}/index.md` | vol6 index | `[↑ Vol 6: Periodic Table of Knots](../index.md)` |
| `common/index.md` | entry-point | `[↑ AVE Knowledge Base](../entry-point.md)` |
| `common/{leaf}.md` (root leaves: appendix-experiments, full-derivation-chain, solver-toolchain, mathematical-closure, appendices-overview) | common/index.md | `[↑ Common Resources](../index.md)` |
| `common/translation-tables/{leaf}.md` | common index | `[↑ Common: Translation Tables](../index.md)` |
| `vol8/NOTES.md` | vol8 index | `[↑ Vol 8: Virtual Media](../index.md)` |

### 5.2 Down-Link Format

Every index document ends with a `## Contents` section:

```markdown
## Contents

- [Child Name](child-slug/index.md) — one-line description of content scope
- [Leaf Name](leaf-slug.md) — resultbox "Title"; key equations; brief scope
```

### 5.3 Index Document Structure (Domain and Above)

```markdown
[↑ Parent Name](../index.md)

# {Domain/Chapter Name}

## Key Results

| Result | Location |
|---|---|
| Verbatim result statement (formula or claim) from source | [Source leaf](path) |

## Derivations and Detail

- [Child Name](path) — one-line scope description

## Contents

- [Child 1](path) — description
- [Child 2](path) — description
```

**Key Results rule**: populated verbatim from source content, drawn from all children below. No paraphrasing. The coordinator-level description: "conclusions and formulae tabulated first."

### 5.4 Leaf Document Structure

```markdown
[↑ Parent Name](../index.md)
<!-- leaf: verbatim -->
<!-- path-stable: ... -->           (only for path-stable anchors)
<!-- original-label: ... -->        (only for disambiguation notes)
<!-- status: pending-autotune -->   (only for Vol 8 pending leaves)

# {Section Title as in source}

{Verbatim LaTeX→Markdown content}

> → Primary: [Reference](path) — rationale    (cross-volume deps from source text only)
> ↗ See also: [Reference](path) — rationale   (optional suggestions)
```

**Verbatim rule**: `$$...$$` for display math, `$...$` for inline math. No paraphrasing, no summarization. No analogies not present in source text. No accessibility simplifications. The KB audience is the same as the original material's audience.

---

## 6. File Count Summary

| Volume / Section | Index files | Leaf files | Total |
|---|---|---|---|
| Root + common | 4 | 11 | 15 |
| Vol 1 | ~11 | ~58 | ~69 |
| Vol 2 | ~25 | ~110 | ~135 |
| Vol 3 | 22 | ~120 | ~142 |
| Vol 4 | 26 | ~96 | ~122 |
| Vol 5 | 10 | 78 | 88 |
| Vol 6 | 24 | 119 | 143 |
| Vol 7 | 10 | 43 | 53 |
| Vol 8 | 22 | 43+1 | 66 |
| **Total** | **~157** | **~679** | **~836** |

Estimates: Vol 1, Vol 2, Vol 3 leaf counts are approximate (per-volume taxonomy architects gave ranges). Vol 5 may reach 90–110 depending on line-count splitting at distillation time. Total range: ~700–875 files.

---

## 7. Unified Acceptance Criteria

These must all pass before Phase 4 review loop exits.

### Navigation

**AC-NAV-1**: Every `.md` file except `ave-kb/entry-point.md` contains a line matching `^\[↑ ` on line 1.
```bash
find manuscript/ave-kb -name "*.md" ! -wholename "*/entry-point.md" | xargs grep -L '^\[↑ '
# Must return empty
```

**AC-NAV-2**: Every non-index `.md` file contains `<!-- leaf: verbatim -->` on line 2 (cross-ref leaves may use `<!-- leaf: cross-ref -->` instead).
```bash
find manuscript/ave-kb -name "*.md" | grep -v index.md | grep -v NOTES.md | grep -v CLAUDE.md | xargs grep -L '<!-- leaf:'
# Must return empty
```

**AC-NAV-3**: `ave-kb/entry-point.md` exists and links to all 8 volume indexes.

**AC-NAV-4**: No unreachable documents (every file is linked from exactly one parent). Automated check: link graph must be connected.

### Depth

**AC-DEPTH-1**: No Vol 1, 2, 3, 4, 6, 7, or 8 file exceeds 4 levels below `ave-kb/`.
```bash
find manuscript/ave-kb -name "*.md" ! -path "*/vol5/*" | awk -F/ 'NF>7 {print}'
# Must return empty
```

**AC-DEPTH-2**: No Vol 5 file exceeds 5 levels below `ave-kb/`.
```bash
find manuscript/ave-kb/vol5 -name "*.md" | awk -F/ 'NF>8 {print}'
# Must return empty (path = ave-kb/vol5/domain/chapter/leaf = 5 levels = 8 components)
```

### Path-Stable Anchors

**AC-ANCHOR-1**: `ave-kb/vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md` exists and contains `<!-- path-stable: referenced from vol3 as sec:k4_tlm -->`.

**AC-ANCHOR-2**: `ave-kb/vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md` exists and contains `<!-- path-stable: referenced from vol3 as sec:hbond_derivation -->`.

**AC-ANCHOR-3**: `ave-kb/vol7/condensed-matter/ch4-phase-transitions/s03-melting-eigenmode.md` exists and contains `<!-- path-stable: referenced from vol3 as sec:melting_eigenmode -->`.

**AC-ANCHOR-4**: `ave-kb/vol5/protein-folding-engine/network-solver/index.md` exists (Vol 5 Ch.5, 05_folding_roadmap.tex). Note: PATH-STABLE designation removed — no cross-volume reference confirmed in Phase 2 extraction.

**AC-ANCHOR-5**: `ave-kb/vol2/quantum-orbitals/ch7-quantum-mechanics/index.md` exists (path-stable for Vol 5 cross-ref to ch:quantum_mechanics).

**AC-ANCHOR-6**: `ave-kb/common/appendix-experiments.md` exists and is not duplicated inside any volume tree.
```bash
find manuscript/ave-kb/vol* -name "appendix-experiments.md"
# Must return empty (canonical copy lives only in common/)
```

**AC-ANCHOR-7**: `ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` exists and contains `<!-- path-stable: referenced from vol6 as eq:H_infinity and sec:galactic_saturation -->`.
```bash
grep -l 'path-stable' manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md
# Must succeed
```

**AC-ANCHOR-8**: `ave-kb/vol1/ch0-intro.md` exists (standalone leaf at vol1 root per vol1 taxonomy architect design) and `ave-kb/vol1/index.md` Contents section links to it.
```bash
test -f manuscript/ave-kb/vol1/ch0-intro.md
grep -l 'ch0-intro.md' manuscript/ave-kb/vol1/index.md
# Both must succeed
```

### Content Fidelity

**AC-FIDELITY-1**: No leaf file contains a `## Summary` or `## Overview` heading.
```bash
grep -rl '^## Summary\|^## Overview' manuscript/ave-kb/ | grep -v index.md | grep -v NOTES.md | grep -v CLAUDE.md
# Must return empty
```

**AC-FIDELITY-2**: All 3 Vol 8 pending-autotune leaves contain `<!-- status: pending-autotune -->` on line 3.
```bash
grep -l 'pending-autotune' manuscript/ave-kb/vol8/
# Must return at least: quantitative-results.md, global-ac-correction.md, autotune-results.md
```

### Token Budget

**AC-TOKEN-1**: `wc -w manuscript/ave-kb/entry-point.md` reports ≤ 2200 words.

**AC-TOKEN-2**: Each volume index `wc -w` reports ≤ 2200 words.

### Structure

**AC-STRUCT-1**: Exactly 14 element directories exist under Vol 6 period-1/, period-2/, period-3/ combined.
```bash
find manuscript/ave-kb/vol6/period-* -maxdepth 1 -type d | grep -v '/period-[0-9]*$' | wc -l
# Must equal 14
```

**AC-STRUCT-2**: Vol 6 elements neon, sodium, magnesium, aluminum each contain exactly 7 leaf files; all other elements contain exactly 6 leaf files. Verify by per-element file count.

**AC-STRUCT-3**: Vol 7 Ch.4 `ch4-phase-transitions/` contains exactly 5 leaf files (s01–s05); confirming `03_melting_eigenmode.tex` was split into s03, s04, s05.
```bash
find manuscript/ave-kb/vol7/condensed-matter/ch4-phase-transitions -maxdepth 1 -name "*.md" ! -name "index.md" | wc -l
# Must equal 5
```

**AC-STRUCT-4**: No `Part-I/` or `Part-II/` directory exists under Vol 7 Ch.1.
```bash
find manuscript/ave-kb/vol7/propulsion/ch1-metric-streamlining -maxdepth 1 -type d
# Must return only ch1-metric-streamlining itself
```

**AC-STRUCT-5**: Vol 5 `protein-backbone-proton-radius.md` and `predicted-extensions.md` do not contain the string `protein-bridge` as a navigation slug or title (comment annotation is acceptable).
```bash
grep -r 'protein-bridge' manuscript/ave-kb/vol5/ | grep -v '<!--'
# Must return empty
```

---

## 8. Distiller Dispatch Guidance

These items are not structural (no skeleton change needed), but must be included in distiller dispatch instructions to prevent Phase 4 review failures.

### 8a. Vol 8 Key Results strategy (no resultboxes)

Vol 8 has zero resultbox environments. The canonical §5.3 Key Results rule requires verbatim content from source. For Vol 8 domain and chapter indexes, distillers must use the following substitution:

> **Key Results (Vol 8 chapters)**: Use verbatim section-level claims and the two labelled equations as Key Results anchors:
> - `eq:gamma_scaling`: $T = (1-\gamma)^N$ cascade transfer function
> - `eq:unit_circle`: $\sigma^2 + r^2 = 1$ sigmoid-saturation identity
>
> For chapters without labelled equations, use the verbatim opening claim of the chapter's first section as the Key Result. Do NOT paraphrase or abstract. If no claim is identifiable, write: `Key Results: See leaves for detailed results.`

This constitutes a formal exemption from the resultbox-sourced Key Results requirement for Vol 8 only.

### 8b. Vol 8 NOTES.md structural type

`vol8/NOTES.md` is a **vol8-local notes file** — not a leaf, not an index. It carries:
- Up-link on line 1: `[↑ Vol 8: Virtual Media](../index.md)`
- Content marker on line 2: `<!-- notes: vol8-local -->`
- Content: Vol 8 raw-form notation policy, Z∝A inversion scope clarification, pending-result marker conventions

`vol8/index.md` Contents section must include an explicit entry:
```markdown
- [Vol 8 Notation Notes](NOTES.md) — raw-form notation policy; Z∝A inversion scope; pending-result conventions
```

### 8c. Entry-point paragraph budget

The entry-point word limit of 2200 must be distributed as:
- **Per-volume paragraphs**: maximum 200 words each × 8 volumes = 1600 words
- **Structural text** (header, `common/` link, navigation instructions, orientation sentence): 400 words budget
- **Total**: 2000 words target, 2200 ceiling

Each per-volume paragraph must include: (1) the volume's core claim in one sentence, (2) the domain grouping names, (3) the most important 2-3 Key Results, (4) a link to the volume index.

### 8d. Vol 3 translation table cross-references

Vol 3 taxonomy AC9 assumes a single `common/translation-tables.md`. The canonical structure uses per-domain leaves under `common/translation-tables/`. Vol 3 distillers must use these paths for `> → Primary:` references:
- Gravity translation: `../../common/translation-tables/translation-gravity.md`
- Condensed matter translation: `../../common/translation-tables/translation-condensed-matter.md`
- Cosmology translation: `../../common/translation-tables/translation-cosmology.md`

### 8e. Vol 1 invariant disposition

Vol 1 distillers must NOT place these items in CLAUDE.md (they were considered but rejected by coordinator):
- `eq:master_wave` → belongs in `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`
- Vacuum Impedance $Z_0$ → belongs in `vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`
- Four Universal Regimes → belongs in `vol1/operators-and-regimes/ch7-regime-map/four-regimes.md`
- Topo-Kinematic Isomorphism table → belongs in `vol1/axioms-and-lattice/ch2-macroscopic-moduli/topo-kinematic-isomorphism.md`
- Vacuum Porosity Ratio $\alpha$ → belongs in `vol1/axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md`

### 8f. Vol 2 quantum-orbitals word-count constraint

`vol2/quantum-orbitals/index.md` doubles as domain and chapter index for a ~3600-line source. Word-count budget: maximum 2200 words. The distiller must abbreviate leaf one-line descriptions in the Contents section if needed to stay within budget.

### 8g. Vol 5 common/ down-link requirement

`vol5/index.md` Contents section must include an explicit entry linking to `vol5/common/index.md`:
```markdown
- [Vol 5 Translation Tables](common/index.md) — biology ↔ AVE and protein solver ↔ EE notation tables
```

### 8h. Cross-ref leaf minimum content

`<!-- leaf: cross-ref -->` type leaves (currently only `vol8/appendix/unified-experiments-ref.md`) must contain:
1. Up-link on line 1
2. `<!-- leaf: cross-ref -->` on line 2
3. A `> → Primary:` pointer to the canonical location
4. A one-sentence description of what the target contains
5. No other content

---

## 9. Coordinator Notes

The following open questions were provided to `kb-structure-reviewer` and have been resolved or deferred:

1. **Vol 2 Ch.7 anomaly (~3600 lines)**: Single chapter forms its own domain (`quantum-orbitals/`). Reviewer should assess whether the chapter index + leaves adequately surfaces major results within the 2200-word budget. This is the single largest source chapter in the series.

2. **Vol 5 fifth-level exception**: Biological-applications branch stays at 4 levels; molecular-foundations and protein-folding-engine branches use 5 levels. Reviewer should verify the exception is self-consistent (leaf ancestors in 5-level branches can still navigate up in 5 hops to entry-point).

3. **Vol 6 framework depth**: The `computational-mass-defect/` subtopic is 3 levels below vol6 (vol6 → framework → computational-mass-defect → leaf = 3 = within 4-level limit). Confirm this is correct.

4. **`ave-kb/common/` up-links**: `common/appendix-experiments.md` and `common/translation-tables/{leaf}.md` up-link to entry-point and common/index.md respectively. The common/index.md up-links to entry-point. Reviewer should confirm this chain is unambiguous.

5. **Vol 1 Ch.0 placement**: **RESOLVED** — canonical placement is `vol1/ch0-intro.md` (root level, not inside any domain). See §3.2. AC-ANCHOR-8 verifies this. The old path `vol1/axioms-and-lattice/ch0-preface-foundations.md` must NOT be used.

6. **Vol 8 `NOTES.md` file**: This is not a leaf and not an index — it is a volume-local notes file. It needs an up-link (→ vol8/index.md) and must not have a leaf marker. Reviewer should flag if this creates any link-validation issues.

7. **Vol 6 `geometric-inevitability/` dangling refs**: **RESOLVED** — all three refs have confirmed targets. See §4 PATH-STABLE table and AC-ANCHOR-7:
   - `eq:H_infinity` → `ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md`
   - `sec:galactic_saturation` → same file
   - `sec:membrane_phase_buffering` → `ave-kb/vol5/molecular-foundations/organic-circuitry/membrane-phase-buffering.md`

8. **Vol 7 Ch.1 Part I/II comment structure**: The LaTeX source has Part I/Part II in comments only; KB flattens to a single chapter directory. Reviewer should confirm no structural links in the source text will create navigation confusion.

---

## 10. Distiller Standing Directive

The following instruction must be included verbatim in every `kb-content-distiller` dispatch:

> **Standing directive for all distiller dispatches**: the KB audience is the same as the original material's audience. Distillers must not introduce analogies not present in the source text, simplify for a different audience, or reframe content for accessibility. Contextual explanation is the docent's responsibility, delivered interactively. The KB's responsibility is accurate navigation structure for readers already at the level of the source material.

---

## 11. Phase Readiness

**Phase 1 (Taxonomy Design)**: COMPLETE
- All 8 per-volume taxonomy designs produced and read by coordinator
- Canonical synthesis complete (this document)

**Next step**: Phase 1a — dispatch `kb-structure-reviewer` with this canonical taxonomy and the 8 per-volume taxonomy files. Reviewer should assess navigability, cross-volume dependency representativeness, invariant correctness, and entry-point feasibility.

**After Phase 1a**: Phase 1b — present to human for approval.
