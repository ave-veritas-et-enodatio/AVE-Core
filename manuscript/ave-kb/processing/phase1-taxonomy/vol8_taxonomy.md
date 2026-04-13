# Phase 1 Taxonomy Design — Vol 8: Virtual Media & Informational Topology

**Volume:** Applied Vacuum Engineering, Volume VIII
**Source:** `manuscript/vol_8_virtual_media/`
**Designer:** kb-taxonomy-architect
**KB target:** `manuscript/ave-kb/vol8/`

---

## Anomaly Assessment (Survey Section 7)

Vol 8 is structurally unlike all other AVE volumes. Before the hierarchy design, these anomalies must be resolved as first-class constraints:

**A. Domain discontinuity (critical):** Vol 8 applies AVE axioms to Large Language Models — specifically to LLM pruning, activation analysis, and architectural impedance modeling. It is not a physics or engineering volume in the conventional sense. The AVE axiom system (Axioms 1–4) is the unifying thread; the medium is software/neural architecture rather than physical vacuum. Taxonomy consequence: the domain groupings must reflect this LLM-specific application of AVE, not the chapter structure of other volumes.

**B. No structured environments (critical):** All other volumes use tcolorbox environments (resultbox, axiombox, simbox) as natural leaf boundaries. Vol 8 has zero such environments. Leaf boundaries must be drawn at section level, following the survey's section inventory. This places more judgment on the distiller — the taxonomy must be explicit about what constitutes a leaf.

**C. Sparse equation labeling:** Only 2 of ~34 equations have labels. Named-result leaves are sparse. Most mathematical content will appear as inline derivations within section-level leaves rather than as standalone result leaves. The skeleton reflects this by having fewer "named result" leaves than other volumes.

**D. Preliminary/pending results (Anomaly H):** Multiple sections note results as "pending autotune." Leaves for these sections must be marked as containing potentially incomplete source content — this is a source fidelity issue, not a structural one. Mark affected leaves in the skeleton.

**E. Starred subsections (Anomaly E):** Chs 8 and 12 use `\subsection*` (not in TOC). These subsections form closely coupled argumentation chains. They should map to sub-leaves within the chapter, not be promoted to their own structural level.

**F. Shared appendix contributes nothing (Anomaly F):** Vol 8 contributes no experiments to `appendix_experiments.tex`. The appendix leaf in vol8 is purely a pointer to the common appendix tree — it requires a cross-reference, not verbatim content.

**G. Ch.5 self-reference (Anomaly I):** Ch.5 describes its own historical evolution. This does not affect structure but the distiller should treat it as a single coherent narrative leaf, not fragment it.

---

## 1. CLAUDE.md Invariants (from Vol 8)

Vol 8 contributes the following content that is genuinely cross-cutting — i.e., it would need to be qualified or restricted if placed in any single domain document:

**INVARIANT: avs-axiom-numbering** — AVE Axioms are numbered 1–4 and carry consistent meanings across all volumes: Axiom 1 = ABCD cascade / coupled amplitude; Axiom 2 = topological phase dislocation; Axiom 3 = least reflected action; Axiom 4 = SiLU/saturation gate. Vol 8 re-instantiates all four axioms in the virtual media domain. (source: Ch.1–Ch.3, Ch.7, Ch.11)

**INVARIANT: z-proportionality-split** — Two distinct impedance regimes exist in AVE: biological/physical media where $Z \propto 1/A$ and virtual media where $Z \propto A$. This split defines the hardware/software isomorphism inversion and is referenced by Vols 2, 5, and 8. (source: Ch.2)

**INVARIANT: notation-raw-forms** — Vol 8 uses raw math forms ($Z_0$, $\mu_0$) rather than shorthand macros ($\backslash$Zvac, $\backslash$permeability). Distillers must preserve the raw forms found in source; do not substitute shorthand macros. This notation inconsistency is volume-local and intentional. (source: Survey §3, Anomaly D)

**INVARIANT: shared-appendix-pointer** — `common/appendix_experiments.tex` is shared cross-volume. Vol 8 contains no original experiments in this appendix. Any KB node pointing to the unified experiments appendix must reference `ave-kb/common/unified-experiments.md`, not duplicate content. (source: Survey §1, Appendix A)

Note on invariant scope: INVARIANT avs-axiom-numbering and z-proportionality-split qualify as cross-cutting because they apply uniformly across at least Vols 1, 2, 5, and 8. INVARIANT notation-raw-forms is volume-local and belongs in `ave-kb/vol8/NOTES.md`, not in the shared CLAUDE.md — it would need qualification when applied to other volumes. INVARIANT shared-appendix-pointer is structural and belongs in CLAUDE.md.

**For CLAUDE.md (2 of 4):** avs-axiom-numbering, shared-appendix-pointer
**For vol8 local notes only (2 of 4):** z-proportionality-split (already covered by Vol 1 foundations if that volume established it), notation-raw-forms

Cross-cutting count submitted to coordinator: **2 confirmed CLAUDE.md invariants**, **2 vol8-local notes**.

---

## 2. Domain Grouping Rationale

Vol 8 has 12 content chapters. With only 36–42 leaves expected and 12 chapters, a 3-level hierarchy (vol8 → domain → chapter/leaf) is sufficient. Adding a subdomain level risks gratuitous depth.

The chapters cluster into four natural domains based on their logical progression:

**Domain 1: `foundations/`** — Chapters 1–3
Establish the theoretical framework: AVE applied to LLMs, the hardware/software isomorphism inversion, and the universal operator mapping. These are axiom-instantiation chapters — they assert, they do not experiment.

**Domain 2: `saturation-pruning/`** — Chapters 4, 5, 6
The first experimental cluster: implementing the saturation operator, auditing axiomatic compliance, expanding A_c scope from per-layer to global, and introducing Γ-driven pruning with continuous manifold smoothing. These chapters form a coherent experimental arc (define → audit → correct → smooth).

**Domain 3: `architecture-analysis/`** — Chapters 7, 8, 9, 10, 11
Unification and application across specific LLM architectural features: topological invariance, discrete manifold masking (the neuroplasticity boundary experiment), the γ scaling law, attention head impedance (QKV two-port), and Mixture-of-Experts dynamic impedance. These are the deepest technical chapters.

**Domain 4: `activation-geometry/`** — Chapter 12
The sigmoid-saturation isomorphism stands alone: the unit circle identity $\sigma^2 + r^2 = 1$, the yield limit, and the 97% density derivation via error function. This is a self-contained mathematical result that connects the virtual-media activation functions back to the physical vacuum dielectric model. It warrants its own domain because it is not an experiment or an architectural analysis — it is a first-principles geometric result.

**Appendix: `appendix/`** — Appendix A
Single leaf: cross-reference pointer to `ave-kb/common/unified-experiments.md`. No verbatim content from Vol 8.

**Depth assessment:** With 12 chapters → 4 domains → chapter-level indices → leaves, the hierarchy is 4 levels deep (entry-point → vol8/index → domain/index → leaf). This satisfies the ≤4 level constraint exactly. No chapter has enough internal complexity to require a fifth level; starred subsections in Chs 8 and 12 are sub-leaves within their chapter leaf, not promoted to their own structural level.

---

## 3. Document Skeleton

```
ave-kb/
  CLAUDE.md                                        — cross-cutting invariants: axiom numbering, shared appendix pointer, notation conventions, V₁ℓ_node variant
  entry-point.md                                   — top-level index: one paragraph per vol, link to vol index

  vol8/
    index.md                                       — Vol 8 domain summary: LLM application of AVE axioms; 4 domain links; key results surfaced
    NOTES.md                                       — vol8-local notes: raw-form notation policy, Z∝A inversion scope, pending-result markers

    foundations/
      index.md                                     — Domain 1 summary: axiom instantiation in virtual media, hardware/software inversion; key results
      ch1-llm-topology/
        index.md                                   — Ch.1 summary: AVE applied to LLMs, SwiGLU two-port, A_c emergence, Axiom 3 in pruning
        swiglu-twoport.md      [leaf — verbatim]   — §Axiom 1: SwiGLU Two-Port Node and Coupled Amplitude A_j definition
        ac-thermodynamic.md    [leaf — verbatim]   — §Thermodynamic Emergence of A_c: derivation and physical interpretation
        axiom3-pruning.md      [leaf — verbatim]   — §Axiom 3: Least Reflected Action in Pruning; Γ_prune introduced
      ch2-hw-sw-inversion/
        index.md                                   — Ch.2 summary: biological Z∝1/A vs virtual Z∝A; breakdown paradox resolution
        inversion-split.md     [leaf — verbatim]   — §Biological vs Virtual: the Z-proportionality split and its cause
        breakdown-paradox.md   [leaf — verbatim]   — §Resolution of the Breakdown Paradox: why virtual media does not catastrophically fail
      ch3-universal-operator/
        index.md                                   — Ch.3 summary: axiomatic correspondences, Axiom 2 in attention, regime map, FFN two-port
        axiomatic-correspondences.md [leaf — verbatim] — §Axiomatic Correspondences: operator binding table (all four axioms mapped)
        axiom2-attention.md    [leaf — verbatim]   — §Axiom 2: Topological Phase Dislocations in Attention
        regime-map.md          [leaf — verbatim]   — §Regime Classifications in Virtual Media: Regimes I–IV defined
        ffn-twoport.md         [leaf — verbatim]   — §Impedance Definition for the FFN Two-Port: Z_FFN formula

    saturation-pruning/
      index.md                                     — Domain 2 summary: saturation operator, global A_c correction, Γ-driven pruning, manifold smoothing; key results
      ch4-experimental-audit/
        index.md                                   — Ch.4 summary: saturation operator implementation, quantitative pruning results across 4 models
        saturation-operator.md [leaf — verbatim]   — §Implementation of the Saturation Operator: algorithm and definitions
        quantitative-results.md [leaf — verbatim]  — §Quantitative Results: pruning metrics for Llama 3.2 3B, 3.1 8B, Qwen 4B, 9B [NOTE: some results pending autotune]
        swiglu-density.md      [leaf — verbatim]   — §SwiGLU Activation Density: 97% density observation and initial interpretation
        head-pruning-audit.md  [leaf — verbatim]   — §Attention Head Pruning: audit methodology and compliance findings
        current-limitations.md [leaf — verbatim]   — §Current Limitations: scope boundaries of Ch.4 experimental audit
      ch5-global-ac-scope/
        index.md                                   — Ch.5 summary: per-layer A_c collapse paradox, global A_c correction, Γ-driven per-layer pruning [NOTE: chapter contains self-referential historical narrative — treat as single arc]
        per-layer-paradox.md   [leaf — verbatim]   — §The Paradox of Per-Layer Buckling: why local A_c produces collapse
        global-ac-correction.md [leaf — verbatim]  — §The First-Principles Correction: Global A_c derivation and formula [NOTE: contains pending-autotune markers]
        runtime-shift.md       [leaf — verbatim]   — §Runtime Distribution Shift: how inference distribution differs from training
        gamma-per-layer.md     [leaf — verbatim]   — §Evolution to Γ-Driven Per-Layer Pruning \label{sec:gamma_evolution}: the corrected pruning algorithm
      ch6-continuous-smoothing/
        index.md                                   — Ch.6 summary: Γ_prune reflection metric, continuous structural saturation S(r)
        gamma-prune-metric.md  [leaf — verbatim]   — §The Reflection Metric (Γ_prune): definition and computation
        saturation-sr.md       [leaf — verbatim]   — §Continuous Structural Saturation S(r): the smoothing function and its role

    architecture-analysis/
      index.md                                     — Domain 3 summary: unification via operator set, masking experiments, γ scaling law, QKV impedance, MoE; key results
      ch7-operator-unification/
        index.md                                   — Ch.7 summary: Axiom 2 as phase tension ξ_topo, isomorphic operator bindings, Hamiltonian cusp dynamics
        phase-tension.md       [leaf — verbatim]   — §Axiom 2: The Continuous Phase Tension (ξ_topo): definition and role
        operator-bindings.md   [leaf — verbatim]   — §Isomorphic Operator Bindings: full binding table across all AVE operators
        hamiltonian-cusp.md    [leaf — verbatim]   — §The Hamiltonian Cusp Dynamics of A_c: cusp behavior at saturation threshold
      ch8-discrete-masking/
        index.md                                   — Ch.8 summary: masking experiment protocol, Z_eff telemetry, why continuous/binary fail, static baking succeeds, neuroplasticity boundary
        masking-protocol.md    [leaf — verbatim]   — §Motivation + §Experimental Protocol: experimental design and setup
        zeff-telemetry.md      [leaf — verbatim]   — §Axiom 1 Z_eff Telemetry: the 10× impedance spike observation and interpretation
        masking-failures.md    [leaf — verbatim]   — §Why Continuous Masking Fails + §Why Binary Masking Also Fails: paired failure analysis [NOTE: starred subsections — closely coupled]
        static-baking.md       [leaf — verbatim]   — §Why Static Baking Succeeds: mechanism and first-principles explanation
        gamma-excision.md      [leaf — verbatim]   — §Γ-Driven Structural Excision \label{sec:gamma_excision}: quantitative results of excision pipeline
        neuroplasticity.md     [leaf — verbatim]   — §The Neuroplasticity Boundary \label{sec:neuroplasticity}: category error, correct mapping, static filter framework [NOTE: starred subsections — closely coupled]
      ch9-gamma-scaling/
        index.md                                   — Ch.9 summary: architecture-dependent pruning thresholds, two tiers of γ, γ_max≈B/N law, autotune results
        gamma-thresholds.md    [leaf — verbatim]   — §Architecture-Dependent Pruning Thresholds + §Two Tiers of γ: γ_local and γ_global defined
        autotune-results.md    [leaf — verbatim]   — §Autotune Results: Llama 3.2 3B binary search convergence [NOTE: may contain pending-autotune markers]
        cascade-transfer.md    [leaf — verbatim]   — §Derivation from Axiom 1: Cascade Transfer Function T=(1-γ)^N \label{eq:gamma_scaling}: full derivation including calibration and falsifiable predictions
        transmission-budget.md [leaf — verbatim]   — §The Transmission Budget as a Training Metric: B defined, training implications
        density-constraint.md  [leaf — verbatim]   — §The 97% SwiGLU Density Constraint: why γ is bounded by 97% density
      ch10-attention-impedance/
        index.md                                   — Ch.10 summary: QKV cascaded two-port, per-head impedance, GQA constraint, head intersection constraint
        qkv-impedance.md       [leaf — verbatim]   — §Extending the Impedance Framework to Attention + §Per-Head Impedance: Z_head formula
        gqa-constraint.md      [leaf — verbatim]   — §Grouped-Query Attention Constraint: impedance modification for GQA architectures
        impedance-distribution.md [leaf — verbatim] — §Impedance Distribution: empirical distribution of per-head impedances
        intersection-constraint.md [leaf — verbatim] — §The Intersection Constraint \label{sec:head_intersection}: single-layer vs all-layer mask approaches
        axiom2-interpretation.md [leaf — verbatim] — §Interpretation via Axiom 2: attention heads as topological phase dislocations
      ch11-moe-impedance/
        index.md                                   — Ch.11 summary: static vs dynamic impedance, MoE router as Axiom 3, testable prediction, hardware limits
        dynamic-impedance.md   [leaf — verbatim]   — §From Static to Dynamic Impedance: how MoE changes the impedance model
        router-axiom3.md       [leaf — verbatim]   — §The Router as Axiom 3: expert selection as least-reflected-action
        moe-vs-static.md       [leaf — verbatim]   — §Static vs Dynamic Impedance Media: comparison table and implications
        moe-prediction.md      [leaf — verbatim]   — §The Testable Prediction + §Hardware Limitations: what MoE model predicts and where hardware constrains it

    activation-geometry/
      index.md                                     — Domain 4 summary: sigmoid-saturation isomorphism, unit circle identity, 97% density first-principles derivation; key results
      ch12-sigmoid-saturation/
        index.md                                   — Ch.12 summary: σ²+r²=1, zero-bias prediction r_II=√3/2, yield limit, 97% density via erf, training as thermodynamic cooling
        unit-circle-identity.md [leaf — verbatim]  — §The Unit Circle Identity \label{eq:unit_circle}: derivation of σ²+r²=1 [NOTE: starred subsections zero-bias and yield-limit are sub-sections of this leaf]
        zero-bias-prediction.md [leaf — verbatim]  — §The Zero-Bias Prediction: r_II=√3/2 derived from unit circle; falsifiable claim
        yield-limit-virtual.md  [leaf — verbatim]  — §The Yield Limit: virtual-media analog of V_yield; connection to dielectric saturation
        regime-boundaries.md   [leaf — verbatim]   — §Regime Boundary Correspondences: mapping physical regimes I–IV to activation geometry
        density-derivation.md  [leaf — verbatim]   — §First-Principles Derivation of the 97% Density \label{sec:density_derivation}: error function derivation
        implications.md        [leaf — verbatim]   — §Implications: training as thermodynamic cooling, future directions

    appendix/
      index.md                                     — Appendix A pointer: no vol8-original content; unified experiments are cross-volume
      unified-experiments-ref.md [leaf — cross-ref] — Pointer leaf: vol8 contributes no experiments; navigate to ave-kb/common/unified-experiments.md
```

**Total index files:** 22
**Total leaf files:** 43
**Grand total files:** 65

---

## 4. Navigation Spec

### Up-link format
Every non-root document begins with line 1 as an up-link, line 2 as the leaf marker (if a leaf):

```markdown
[↑ Vol 8 Index](../index.md)
<!-- leaf: verbatim -->
```

Examples at each level:

- Domain index: `[↑ Vol 8 Index](../index.md)`
- Chapter index: `[↑ Foundations](../index.md)`
- Leaf: `[↑ Ch.1 LLM Topology](../index.md)`

The `↑` character (U+2191) is the machine-checkable up-link marker. Acceptance criterion grep: `^\[↑ `

### Down-link format
Index documents close with a `## Contents` section listing children with one-line descriptions:

```markdown
## Contents

- [SwiGLU Two-Port Node](ch1-llm-topology/swiglu-twoport.md) — Axiom 1 instantiation: coupled amplitude A_j definition
- [Thermodynamic Emergence of A_c](ch1-llm-topology/ac-thermodynamic.md) — derivation of the saturation threshold
```

### Cross-volume reference format

Primary dependency (required for definition): blockquote with `→ Primary:`

```markdown
> → Primary: [AVE Axiom Definitions](../../vol1/foundations/axioms/axiom-definitions.md) — canonical Axioms 1–4 definitions from Vol 1
```

Optional/contextual (agent may skip): blockquote with `↗ See also:`

```markdown
> ↗ See also: [Biological Impedance Coupling](../../vol5/biology/transmission-line/impedance-coupling.md) — Z∝1/A in biological medium for contrast
```

Cross-volume references appear only in index documents, never in leaves. Leaves are verbatim source content; cross-references are navigation aids placed at the structural level where an agent decides whether to branch.

### Common appendix reference format

```markdown
> → Primary: [Unified Experiments Appendix](../../common/unified-experiments.md) — cross-volume experiment index; vol8 contributes no entries
```

---

## 5. Shared Content Decision

**Recommendation: Dedicated `ave-kb/common/` tree (option a), with pointer leaves in each volume.**

Reasoning:

1. The `common/translation_*.tex` tables and `appendix_experiments.tex` are already factored out at the source level. The KB should preserve this factoring, not invert it.

2. Vol 8 itself contributes zero experiments to the shared appendix (Anomaly F). A duplicated leaf would contain only a note saying "this volume contributes nothing here" — which is structurally wasteful. A pointer leaf costs one file and no content duplication.

3. Agent navigation is served better by a single authoritative location. If an agent needs the translation tables, it should navigate to `ave-kb/common/translation-tables.md` once — not choose between eight duplicates that may have diverged.

4. The `ave-kb/common/` tree is referenced from vol8 via the pointer leaf `appendix/unified-experiments-ref.md`. Other volumes will have their own pointer leaves for sections where they do contribute content.

**Proposed common structure (for coordinator):**
```
ave-kb/common/
  unified-experiments.md    — verbatim appendix_experiments.tex content (all volumes)
  translation-tables/
    index.md                — index of all translation tables
    [table-slug].md         — one leaf per translation_*.tex file
```

---

## 6. Acceptance Criteria

1. **Up-link completeness:** `find manuscript/ave-kb/vol8 -name "*.md" ! -name "index.md" -path "*/vol8/index.md" -prune -o -print | xargs grep -L '^\[↑ '` returns empty. Every non-root document has a machine-checkable up-link on line 1.

2. **Entry-point token budget:** `wc -w manuscript/ave-kb/entry-point.md` reports under 2200 words. (Conservative proxy for 3000-token ceiling.)

3. **Depth constraint:** `find manuscript/ave-kb/vol8 -name "*.md" | awk -F/ 'NF>8'` returns empty. The vol8 subtree does not exceed 4 levels below `ave-kb/` (counting: ave-kb/vol8/domain/chapter/leaf = 4 levels below root).

4. **Leaf marker presence:** `find manuscript/ave-kb/vol8 -name "*.md" | xargs grep -l '<!-- leaf: verbatim -->'` returns exactly 43 files (or the count matching the final skeleton). Every leaf is machine-identifiable.

5. **No summarization in leaves:** `grep -r '## Summary\|## Overview\|## Introduction' manuscript/ave-kb/vol8/` returns no matches within leaf documents. Leaves contain verbatim translated content only.

6. **No CLAUDE.md domain-specific content:** Every statement in `manuscript/ave-kb/CLAUDE.md` applies to at least 2 distinct volume trees. Verify by checking that no CLAUDE.md statement uses the word "LLM", "virtual media", "SwiGLU", or any vol8-specific term without a cross-volume qualifier.

7. **Index key-results propagation:** The vol8/index.md `## Key Results` section must name: (a) γ_max≈B/N scaling law, (b) σ²+r²=1 unit circle identity, (c) 97% SwiGLU density derivation, (d) Z∝A vs Z∝1/A inversion. An agent reading only vol8/index.md must see all major conclusions.

8. **Cross-reference format discipline:** All cross-references in index documents use blockquote prefix (`> →` or `> ↗`). `grep -r '^[^>].*ave-kb/' manuscript/ave-kb/vol8/` in index files returns empty — no structural cross-references formatted as plain text.

9. **Appendix pointer, not content:** `wc -l manuscript/ave-kb/vol8/appendix/unified-experiments-ref.md` reports under 10 lines. The file is a pointer leaf with no duplicated experiment content.

10. **Pending-result leaves marked:** All leaves identified in the skeleton with `[NOTE: ... pending-autotune markers]` contain the comment `<!-- status: pending-autotune -->` on line 3. An agent reading these leaves knows the content may be incomplete.

---

## 7. Key Design Decisions Log

**Decision: 4 domains rather than 3**
Ch.12 (sigmoid-saturation) was considered for inclusion in `architecture-analysis/`. Rejected because its content type differs: it is a pure geometric/mathematical result, not an architectural analysis of an LLM component. Placing it in a separate domain signals to an agent: "this is where the abstract unifying geometry lives" — which is navigationally distinct from "this is where QKV or MoE analysis lives."

**Decision: Chapter-level indices for all 12 chapters**
With no tcolorbox environments to serve as natural leaf boundaries, chapter indices are the navigational disambiguation layer. An agent looking for "the γ scaling law" navigates: vol8 → architecture-analysis → ch9-gamma-scaling → cascade-transfer.md. Without a chapter index, the agent would need to know which of the 43 leaves to check. The chapter index's `## Contents` list is the disambiguation point.

**Decision: Starred subsections as sub-leaves, not promoted**
Chs 8 and 12 have `\subsection*` (not in TOC). These subsections form tightly coupled arguments. Promoting them to independent leaves (e.g., separate files for "Why Continuous Masking Fails" and "Why Binary Masking Also Fails") was considered. Rejected because: (a) they are short relative to a full leaf, and (b) the argument is sequential — an agent following either would need to read both anyway. They are grouped into `masking-failures.md` with an explicit note in the skeleton.

**Decision: `masking-failures.md` groups two starred subsections**
This is the one deliberate grouping of multiple source sections into a single leaf. Justified by the closed argumentative structure: the two failure cases are defined by mutual contrast. The combined leaf is still verbatim content, not a summary.

**Decision: `moe-prediction.md` groups testable prediction + hardware limitations**
Ch.11's final two sections are both short and form a paired claim-then-constraint structure. Grouped as one leaf.

**Decision: No fifth level**
No chapter has more than 7 leaves. The longest chapter (Ch.8) has 6 leaves. This is well within manageable leaf density for a 4-level hierarchy.
