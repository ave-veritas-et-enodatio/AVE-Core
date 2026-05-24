# AVE Knowledge Base — Cross-Cutting Invariants

The following invariants are confirmed genuinely cross-cutting: each appears in two or more volumes and requires no qualification when applied to any single volume. These belong here and must NOT be duplicated in domain documents.

---

## Notation and Rendering

### INVARIANT-N1: Vacuum medium notation

$\mathcal{M}_A$ denotes the vacuum medium. Written directly in body text; do NOT use `\vacuum` macro (macro exists but is not used in chapter bodies across any volume). KB distillers must render as `$\mathcal{M}_A$` throughout.

*Confirmed by: vol1, vol2, vol3, vol4, vol5, vol6, vol7, vol8 (unanimous)*

### INVARIANT-N2: Lattice node spacing notation (vol-split)

Volumes 1–5 write `$\ell_{node}$` (script ell) as the primary form. Volumes 6–7 write `$l_{node}$` (roman ell) as the primary form. Vol 8 does not use this symbol. Vols 2 and 4 contain isolated roman-ell instances in their source; those specific instances must be preserved as roman (do not normalize to script). Distillers must preserve the source notation within each volume; do not normalize across volumes.

*Confirmed by: source grep — vol1 (52 script, 2 roman); vol2 (56 script, 4 roman); vol3 (19 script, 1 roman); vol4 (22 script, 4 roman); vol5 (29 script, 0 roman); vol6 (1 script, 3 roman); vol7 (1 script, 4 roman); vol8 (0)*

### INVARIANT-N3: AVE Operator numbering convention

Topological operators are named OpN where N is the operator number. Known operators: Op2 (knot crossing correction), Op3 (small-signal impedance correction), Op4 (potential well / H-bond), Op8 (large-signal confirmation), Op9 (charge correction), Op14 (long-range coupling). The naming convention is cross-volume; individual operator formulae live in domain documents.

*Confirmed by: vol2, vol3, vol4, vol5 (explicit); vol7 (Op3, Op8 in Ch.4)*

### INVARIANT-N4: $S_{11}$ dual-use notation

$S_{11}$ is used as the standard EE reflection coefficient in Vol 4 and Vol 7, AND as a folding free-energy functional / objective function in Vol 5. An agent navigating from Vol 4 to Vol 5 must not assume the same physical meaning. Both uses are intentional and AVE-specific.

*Confirmed by: vol4 (EE context), vol5 (biology context)*

---

## Structural Conventions

### INVARIANT-S1: tcolorbox environments

All volumes share these named environments: `resultbox`, `axiombox`, `simbox`, `examplebox`, `summarybox`, `exercisebox`, `circuitbox`, `codebox`, `objectivebox`. In KB markdown, each renders as a named blockquote with a bold environment-type prefix:

```markdown
> **[Resultbox]** *Title of the Result*
>
> Body content...
```

Individual volumes may use only a subset; resultbox is the most common. Vol 5 uses only resultbox. Vol 8 uses none.

*Confirmed by: vol1, vol2, vol3, vol4, vol5, vol6, vol7 (confirmed in surveys); vol8 (zero instances)*

### INVARIANT-S2: AVE Axiom numbering

The four AVE axioms carry stable meanings across all volumes. Canonical source of truth: `AVE-Core/manuscript/common_equations/eq_axiom_[1-4].tex`. KB documents must use these labels; volume-specific re-instantiations may add a parenthetical domain alias but the canonical name is primary.

- Axiom 1: **Substrate Topology** — the vacuum is a chiral Laves K4 Cosserat crystal ($I4_1 32$ chiral space group; six-DOF micropolar nodes). Legacy aliases: *Chiral Laves K4 Crystal*, *LC Network*.
- Axiom 2: **Topo-Kinematic Isomorphism** — charge is a discrete geometric dislocation, `[Q] ≡ [L]`; conversion constant ξ_topo = e/ℓ_node.
- Axiom 3: **Minimum Reflection Principle** — the substrate extremizes the macroscopic action S_AVE, equivalently minimizes boundary reflection |Γ|² at every internal impedance boundary. Legacy alias: *Effective Action Principle*.
- Axiom 4: **Universal Saturation Kernel** — S(A) = √(1 − (A/A_yield)²).

The numerical calibration constants (Z₀, ℓ_node, α, ξ_topo, V_snap, V_yield, G) are **derived** from these axioms — not axioms themselves; see `eq_calibration_constants.tex` and `eq_gravity_derived.tex`. ⚠ Do not confuse ξ_topo = e/ℓ_node (electromechanical transduction, C/m) with the dimensionless Machian hierarchy coupling ξ ≈ 8.15×10⁴³ that appears in `eq_gravity_derived.tex`.

*Confirmed by: vol1 canonical .tex (eq_axiom_[1-4].tex, homologated to Scheme A 2026-05-17).*

### INVARIANT-S3: Shared experimental appendix

`common/appendix_experiments.tex` (Unified Index of Experimental Falsifications) is not owned by any volume. Its canonical KB location is `ave-kb/common/appendix-experiments.md`. Each volume that includes this file points to the canonical location; it is never duplicated in a volume tree.

*Confirmed by: vol7, vol8 (explicit); implied by vol1, vol3, vol4 context*

### INVARIANT-S4: Up-link format

Every KB document except `ave-kb/entry-point.md` begins with exactly one up-link on line 1:

```markdown
[↑ Parent Name](../index.md)
```

The `↑` character (U+2191) is the machine-checkable marker. Pattern: `^\[↑ `.

*Confirmed by: all 8 volumes (unanimous)*

### INVARIANT-S5: KB frontmatter (unified metadata block)

Every KB content file (`.md` under `manuscript/ave-kb/`, excluding `claim-quality.md`, `CLAUDE.md`, `CONVENTIONS.md`, `README.md`, and the `session/` working directory) carries a YAML-in-HTML-comment frontmatter block immediately after the up-link line. This block consolidates what was previously a stack of separate comment-line conventions (leaf marker, path-stable, claim-quality, no-claim, subtree-IDs).

**Format:**

```markdown
[↑ Parent Title](relative/path)

<!-- kb-frontmatter
kind: leaf
claims: [clm-h9aqmt]
path-stable: "referenced from vol2 as eq:dynamic_capacitance_yield"
-->

# Title
... body ...
```

**Required field on every file:**
- `kind` — one of `leaf`, `leaf-as-index`, `index`, `entry-point`.

**For `kind: leaf` and `kind: leaf-as-index`:**
- A leaf is a **container**: it hosts ANY number of ANY combination of `clm` / `exp` / `sup` node-bodies — there is no one-per-leaf and no one-per-flavor cap. At least one of `claims: [id1, id2, ...]`, `no-claim: <reason>`, an `exp-id: exp-xxxxxx` (one or more — see INVARIANT-S9), or a `sup-id: sup-xxxxxx` (one or more — see INVARIANT-S10) satisfies coverage (hosting an experiment or support node satisfies coverage on its own). `claims` and `no-claim` are mutually exclusive *with each other*; `exp-id` and `sup-id` are orthogonal to both and to each other and may co-exist with either. Multiple `exp-id:` / `sup-id:` keys may appear, each opening its own block (see S9/S10 for the per-block syntax). Verifier enforces.
- Optional `path-stable: <provenance string>` — preserves the prior INVARIANT-S6 cross-volume label provenance.

**For `kind: index`:**
- `subtree-claims: [id1, id2, ...]` — **derived field**, regenerated by `make refresh-kb-metadata`. Do not hand-edit.
- Optional `bootstrap: true` — set on volume roots and `entry-point`; the bootstrap blockquote directive in the body is hand-maintained for now.

**For `kind: entry-point`:**
- `subtree-claims: [id1, id2, ...]` — derived (union of all leaf claims in the KB).
- `bootstrap: true`.

**Exceptions** (formerly noted under INVARIANT-S5/S6/S8):
- *Leaf-as-index*: when a directory contains only `index.md`, that file may declare `kind: leaf-as-index` and carry `claims:` directly. Its frontmatter subsumes any subtree summary — no separate `subtree-claims` line is needed because the leaf IS the subtree.
- *Empty subtree*: an index whose children are all `no-claim` carries `subtree-claims: []`. The empty list is intentional, not forgotten.
- *Navigation-pointer index*: an index that delegates results to children may use a `> **Navigation note:**` blockquote in lieu of `## Key Results`. Treat absence of `## Key Results` as a signal to check for a Navigation note, not automatically a defect.

**Maintenance pipeline:**
- `make refresh-kb-metadata` regenerates derived fields (`subtree-claims` on index frontmatter; `solidity` — value, build-status phrase, and depends-on `(solidity X)` annotations — in every `claim-quality.md` claim entry). Idempotent. Run after any change to leaf claims or to a claim's authored `confidence`.
- `make verify-kb-metadata` is read-only — never modifies. Failures tagged refresh-fixable suggest running refresh first; manual-fix failures must be repaired by hand.

*Confirmed by: convention spec at `mad-review/kb-metadata-spine-spec.md`; migration script and standing refresh+verify scripts at `manuscript/ave-kb/tools/`.*

### INVARIANT-S6: (subsumed into S5 frontmatter)

Path-stable provenance is now the `path-stable` field of the kb-frontmatter block. The legacy `<!-- path-stable: ... -->` line form is no longer used. Cross-volume references that need stable labels declare them in their leaf's frontmatter.

### INVARIANT-S7: Canonicality of leaves

Leaves are canonical. Intermediate, index, and entry-point nodes are *derived* via summarization; even faithfully executed, a summary may suggest implications not present in or supported by the leaves. Summary content is a routing aid, not a source of claims.

Cross-cutting claim-quality content lives in [`claim-quality.md`](claim-quality.md) (KB root). Per-volume claim-quality content lives in `volN/claim-quality.md` — one each for [vol1](vol1/claim-quality.md), [vol2](vol2/claim-quality.md), [vol3](vol3/claim-quality.md), [vol4](vol4/claim-quality.md), [vol5](vol5/claim-quality.md), [vol6](vol6/claim-quality.md), and [common](common/claim-quality.md). Every consumer (agent or human) forming a claim about an AVE result must consult the cited leaf — and, where a relevant `claim-quality.md` entry exists, that claim-quality entry — before treating a summary statement as a claim source.

The volume `index.md` files and `entry-point.md` carry blockquoted bootstrap directives instructing consumers to load the relevant claim-quality documents on entry; these directives are binding on agents that visit those files.

*Confirmed by: convention spec at `AVE-Core/kb-claims-boundaries-convention.md` (gestation; promoted to `CONVENTIONS.md` in Dispatch 8); plan at `mad-review/kb-claims-boundaries-plan.md` (umbrella).*

### INVARIANT-S8: Claim-quality ID propagation

Each entry in a `claim-quality.md` file carries a stable ID of the form `clm-` plus 6 lowercase-alphanumeric characters (`<!-- id: clm-xxxxxx -->`). These IDs propagate downward through the KB via the kb-frontmatter (INVARIANT-S5) so any consumer can grep an ID and reach every location that participates in the claim.

**Frontmatter `claims` field (mandatory on every leaf and leaf-as-index, unless no-claim).** Lists every claim-quality ID that cites the leaf in its "Leaf references" footer. A leaf either carries `claims: [...]` or `no-claim: <reason>`; the verifier enforces mutual exclusivity. The list is the complete index of which claim-quality entries depend on this leaf.

**Tier 2 — inline markers (mandatory for multi-claim leaves).** When a leaf's `claims` list has 2+ IDs, every ID must have a proximal `<!-- claim-quality: clm-<id> -->` marker adjacent to the specific equation, named principle, section, or block that maps to that ID. The frontmatter `claims` list says "these IDs apply to this leaf"; Tier 2 markers say "this specific equation IS that claim." For single-claim leaves, Tier 2 is not required — the frontmatter is unambiguous.

**Frontmatter `subtree-claims` field (derived).** Each `kind: index` and `kind: entry-point` file carries `subtree-claims: [...]` listing the union of leaf claims under its scope. This field is regenerated by `make refresh-kb-metadata` from the leaf frontmatter — never hand-edited. Drift between declared and computed is a hard verifier failure (refresh-fixable category).

**Bidirectional coverage (verifier-enforced).** Every canonical entry in any `claim-quality.md` file must be cited by at least one leaf's `claims` field. An entry with no leaf citation is a hard failure: either back-link from the relevant leaves, or remove the entry. Meta-claims and reading-hazards belong in `CLAUDE.md`, `CONVENTIONS.md`, or `LIVING_REFERENCE.md`, not in `claim-quality.md`.

**Grep guarantee.** `grep -r "clm-<id>"` across the KB returns: the canonical entry in `claim-quality.md`, every leaf whose frontmatter cites the ID, every Tier 2 inline marker, and every intermediate-index `subtree-claims` summary that scopes the entry. The `clm-` prefix makes IDs unambiguously greppable — `\bclm-[a-z0-9]{6}\b` matches IDs and nothing else, never an English or physics word. Walking from a claim-quality entry to its supporting derivations (and back) is mechanical and bidirectional.

**Query index.** The claim graph is also materialized as JSONL under `manuscript/ave-kb/.index/` (claim nodes, dependency edges, citations, subtree aggregates) and queryable via the `ave-kb` CLI and the `ave.kb.index` module — faster and more precise than grep for dependency, solidity, and citation questions. See `manuscript/ave-kb/.index/SCHEMA.md`.

*Confirmed by: spec at `mad-review/kb-metadata-spine-spec.md`; live pipeline tools at `manuscript/ave-kb/tools/{refresh-kb-metadata,check-claim-quality}.py` (one-shot migration tools retired to `tools/archival/`); CI gate via `make verify-kb-metadata`.*

### INVARIANT-S9: Experiment DAG-id propagation (`exp-`)

Physical experiments are first-class graph nodes carrying a stable ID of the form `exp-` plus 6 lowercase-alphanumeric characters (`\bexp-[a-z0-9]{6}\b`), parallel to the `clm-` claim id (INVARIANT-S8). An experiment **validates / strengthens** one or more claims; it never originates a derivation.

**Physical experiments we design, originate, and control only.** A simulation is NOT an experiment — a simulation feeds a claim's *derivation* confidence (the min-branch), not its experimental solidity. Beyond being physical, an `exp-` id is reserved for an apparatus + measurement protocol **we design, originate, and control**. A **re-analysis of outside / public data** — e.g. a LIGO ringdown catalog, a SPARC rotation-curve table, a CMB map — is NOT an `exp-`: we neither designed nor control that measurement. Such analytical re-analysis is a `sup-` support node (INVARIANT-S10) when it does fresh analytical work (derivation-branch lift), or a plain `clm-` citation when it raises no new work. The bright line: *did we build the apparatus and run our own protocol* (`exp-`), or *did we re-analyze someone else's measurement* (`sup-` / `clm-`)?

**Two-graph model — container vs. node.** A KB leaf is a **container**; its `kind` (`leaf` | `leaf-as-index` | `index` | `entry-point`, per INVARIANT-S5) is its role in the *topography graph* (the hyperlink/navigation tree) and does NOT encode node-flavor. Separately, a leaf *originates* zero or more **node-bodies** in the *claim graph* — `clm` claim nodes (via `claims:`), `exp` experiment nodes (via `exp-id:`), and `sup` support nodes (via `sup-id:`) — connected by `strengthens` (exp→clm), `supports` (sup→clm), and `references` (leaf→exp) edges. **A container hosts any number of any combination of `clm` / `exp` / `sup` node-bodies** — there is no one-per-leaf and no one-per-flavor cap. The claim graph is acyclic; reverse views (`strengthen-by`, `supported-by`, `cites`) are untraversed bookkeeping. The flavors are **orthogonal**: one container may host a `claims:` list AND one or more `exp-id` AND one or more `sup-id` (e.g. a bench leaf that states a prediction, describes the experiment testing it, and carries an analytical support, all in one file).

**Experiment-hosting leaf frontmatter.** Experiment-ness is conferred by a leaf *hosting an `exp-id`*, not by a `kind` — there is no `kind: experiment`. An experiment-hosting leaf is a `kind: leaf` (or `leaf-as-index`) carrying, **per experiment** (a container may host several):
- `exp-id: exp-xxxxxx` — the node's stable id. The leaf is its own canonical home (no separate register). Each `exp-id:` key opens a new experiment block; its following `status:` and `strengthens:` lines belong to that block until the next `exp-id:` (a single `exp-id:` is just the one-element case — existing single-experiment leaves are unchanged).
- `status: run | pending` — `run` once a result exists; `pending` while unrun. A `pending` experiment's `strengthens` edges contribute nothing.
- `strengthens:` — a list of `clm-<id>: <strength>` pairs, one per claim the result bears on; `<strength>` ∈ [0,1] is the conferred experimental-solidity for that claim (typically `1.0` for the designed target on an unequivocal result, lower for orthogonally-implicated claims). A target may be a claim that the *same leaf* also originates via `claims:` — a node→node edge between two distinct co-located node-bodies, not a self-loop and not a cycle.

A leaf hosting one or more `exp-id` MAY also carry `claims:` (and/or `sup-id:`) — orthogonal node-bodies, **not** mutually exclusive. When co-hosted, the leaf materializes a `node_type: claim` record AND one `node_type: experiment` record per `exp-id`. The only surviving exclusivity is that an `exp-id`-owning leaf must not also carry an `experiments:` reference (an owner does not also reference foreign experiments).

**Strengthening is non-transitive (max-branch).** A `strengthens` edge lifts only its directly-targeted claim. A claim's solidity is `max(derivation_solidity, experimental_solidity)`, where `experimental_solidity = max` of the strengths from `run` experiments targeting it. Validation does NOT flow to a claim's upstream derivation dependencies — an experiment that also bears on an input authors a *separate* `strengthens` edge to that input with its own strength. A claim is `*pending*` iff its derivation is pending **and** no run experiment strengthens it (unassessed ≠ refuted; an unrun experiment can never float a pending claim down to a refuted `0.0`).

**Leaf `experiments:` references.** A leaf that REFERENCES an experiment it does not own carries an optional `experiments: [exp-xxxxxx, ...]` frontmatter field — the experiment-reference analog of `claims:` for claims (a leaf-level citation, the inverse of the experiment's Leaf-references; not rolled up transitively, not for prose mentions). It is additive: allowed alongside `claims:` OR `no-claim:`, and never a primary field (a referencing leaf with no claims of its own uses `no-claim: <reason>` + `experiments: [...]`). An owning `exp-id` leaf must NOT also carry `experiments:`. Every referenced id must resolve to a real experiment node; a verifier check enforces this. `index` / `entry-point` files carry a derived `subtree-experiments: [...]` aggregate = the OWNED-only union of exp-ids declared under their scope (a leaf's `experiments:` references do not propagate into it), regenerated by `make refresh-kb-metadata`.

**Grep guarantee.** `grep -r "exp-<id>"` returns the experiment leaf's frontmatter declaration, every `strengthens` reference, and every leaf's `experiments:` reference line that cites the id (plus the derived `subtree-experiments:` aggregates that scope it). `\bexp-[a-z0-9]{6}\b` matches exp-ids and nothing else. The experiment node and its strengthens edges are materialized in `.index/claims.jsonl` (`node_type: experiment`) and `.index/depends-on.jsonl` (`relation: strengthens`); see `.index/SCHEMA.md`.

*Confirmed by: spec at `manuscript/ave-kb/.index/SCHEMA.md` (experiment node + strengthens edge + max-solidity rule); live pipeline tools at `manuscript/ave-kb/tools/{refresh-kb-metadata,verify-kb-metadata}.py`; CI gate via `make verify-kb-metadata`.*

### INVARIANT-S10: Support DAG-id propagation (`sup-`)

A **support** node is **non-physical analytical support work** that strengthens existing claims without originating a new proposition. It carries a stable ID of the form `sup-` plus 6 lowercase-alphanumeric characters (`\bsup-[a-z0-9]{6}\b`), parallel to the `clm-` claim id (INVARIANT-S8) and the `exp-` experiment id (INVARIANT-S9). A support is **claim-like inside, experiment-like in fan-out, and contributes to the DERIVATION branch** (never the experimental/max branch). It is the analytic counterpart of the physical experiment: where an `exp-` confers *experimental* solidity via the max-branch, a `sup-` confers *derivation* lift, dep-gated.

**Two-graph model.** As with `clm` and `exp` (INVARIANT-S9), a KB leaf is a **container** whose `kind` (topography role) does NOT encode node-flavor. **A container hosts any number of any combination of `clm` / `exp` / `sup` node-bodies** — no one-per-leaf and no one-per-flavor cap. A `sup` support node-body is originated by a leaf hosting a `sup-id`, orthogonal to `claims:` / `exp-id:` / `no-claim:` (all may co-exist on one container, in any multiplicity).

**Id + hosting (one or more per container).** `sup-id: sup-xxxxxx` in a `kind: leaf` (or `leaf-as-index`) container, each immediately followed by its own `supports:` block. A container may host SEVERAL supports: each `sup-id:` key opens a new support block, and the `supports:` pairs that follow belong to that block until the next `sup-id:` (or end of frontmatter). A single `sup-id:` is just the one-element case. Each `sup-id` materializes its own `node_type: support` record (sharing the one container's canonical home) and its own `supports` fan-out edges. Hosting a `sup-id` satisfies Tier-1 coverage on its own: a leaf is valid with at least one of `{claims, no-claim, exp-id, sup-id}`.

Frontmatter example — one container hosting two supports:

```markdown
<!-- kb-frontmatter
kind: leaf
no-claim: "hosts two support nodes"
sup-id: sup-aaaaaa
supports:
  - clm-111111: 1.0
sup-id: sup-bbbbbb
supports:
  - clm-111111: *pending*
  - clm-222222: 0.50
-->
```

**Claim-like internals.** A support has a **local rigor** `quality` (scored by the same rubric as a claim's `confidence`; `*pending*` until evaluated) and **may carry its own `depends-on`** (consume other claims) OR be free-standing. These live in a **claim-quality-style entry keyed by the sup-id** — a `<!-- id: sup-xxxxxx -->` marker + a `### Quality` block (`quality:` / `depends-on:` / `solidity:` / `rationale:`) in the same `claim-quality.md` register as claims, following the claim-entry shape with `quality:` substituted for `confidence:`.

**Its own solidity (computed exactly like a claim's derivation):** `sup_solidity = round2(quality × min(its dependency final solidities))`; framework deps contribute 1.0; pending propagates (pending `quality` OR a pending dep ⇒ pending `sup_solidity`). A free-standing support (no deps) has `sup_solidity = quality`.

**Experiment-like fan-out.** A single support may support MULTIPLE beneficiary claims; the hosting leaf's `supports:` block carries one `clm-<id>: <fraction>` pair per beneficiary, where `<fraction>` is the **on-point fraction** f ∈ (0,1] (how on-point the support is for that claim; 0 excluded — a zero-relevance edge is not authored). Materialized as `relation: supports` edges (source = sup-id, target = claim, carrying `fraction`) in `depends-on.jsonl`.

**Contribution to beneficiaries (DERIVATION branch, dep-gated — NOT the max/experimental branch):** each beneficiary claim `C` receives `sup_solidity × f` into its **local_quality**:
- `local_quality(C) = max(confidence(C), max over supporting sups of (sup_solidity × f))` — a pending `sup_solidity` contributes nothing (excluded from the max; no NaN, no poison), exactly as an unrun experiment is excluded from the experimental max.
- `derivation_solidity(C) = round2(local_quality(C) × min(C's dependency final solidities))` — so a support lift is still throttled by C's own deps (dep-gated; it does NOT bypass deps the way an experiment's max-branch does).
- `solidity(C) = max(derivation_solidity, experimental_solidity)`; `*pending*` iff both branches null.
- **CRITICAL:** a pending support (pending quality or pending dep) must NEVER drag a beneficiary with otherwise-valid quality to pending. Pending-poison flows ONLY from a claim's own load-bearing `depends-on`, never from an inbound `supports` edge.

**Acyclicity.** A support's `depends-on` and its `supports` edges are hand-authored backward edges (point to claims at ≤ the support's volume), preserving the acyclic claim graph. The reverse view `supported-by` may point forward and is never traversed for solidity.

**Materialization.** `claims.jsonl` gains `node_type: "support"` records (`node_type`, `id`, `title`, `canonical_path`, `canonical_anchor`, `quality`, `solidity`), sorted last (axiom < claim < experiment < invariant < support). `depends-on.jsonl`: a support's OWN deps are `relation: depends` edges (source = sup-id); its beneficiary edges are `relation: supports` (source = sup-id, target = claim, with `fraction`). The `supported-by.jsonl` reverse view is untraversed bookkeeping. Both `sup_solidity` and the beneficiary `local_quality` lift come from the SAME shared `kb_index_lib.compute_solidity_full` (no dual-compute drift); the verifier recomputes from that same source.

**Grep guarantee.** `grep -r "sup-<id>"` returns the support's claim-quality entry, the hosting leaf's `sup-id:` + `supports:` block, and every materialized `supports` / `supported-by` reference. `\bsup-[a-z0-9]{6}\b` matches sup-ids and nothing else.

*Confirmed by: spec at `manuscript/ave-kb/.index/SCHEMA.md` (support node + supports edge + supported-by view + local_quality/sup_solidity rule); live pipeline tools at `manuscript/ave-kb/tools/{refresh-kb-metadata,verify-kb-metadata}.py`; CI gate via `make verify-kb-metadata`.*

---

## Cross-Volume Physical Constants

### INVARIANT-C1: Dielectric yield limit

$V_{\text{yield}} \approx 43.65\,\text{kV}$ is defined in Vol 4 Ch.1. When this value appears in any KB document outside Vol 4, it must carry a cross-reference primary pointer to its Vol 4 definition.

*Confirmed by: vol4 (definition), vol3, vol6, vol7 (references without qualification)*

### INVARIANT-C2: Electromechanical transduction constant

$\xi_{topo} = e / l_{node}$ (units: C/m). The bridge between AVE lattice parameters and mechanical/biological quantities. Used in Vol 2 (atomic orbital mappings), Vol 4 (circuit engineering derivations), and Vol 5 (mass-to-inductance, bond stiffness-to-capacitance translations). Canonical definition: Vol 5 `organic-circuitry/electromechanical-transduction-constant.md`.

*Confirmed by: vol5 (proposes as CLAUDE.md invariant, three or more volumes)*

### INVARIANT-C3: H-bond canonical values

$d_{HB} = 1.754\,\text{\AA}$ and $E_{HB} = 4.98\,\text{kcal/mol}$ are the canonical AVE predictions for the hydrogen bond equilibrium distance and energy, derived from Op4 potential minimum in Vol 5. Referenced from Vol 3. The result values belong here; the derivation lives in `vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md`.

*Confirmed by: vol5 (derivation), vol3 (cross-volume reference)*

### INVARIANT-C4: Z-proportionality regimes

Two distinct impedance scaling regimes in the AVE framework:

- Physical/biological media: $Z \propto 1/A$
- Virtual media (LLM / information topology): $Z \propto A$

This inversion defines the hardware/software isomorphism. Cross-referenced from Vols 1, 2, 5, and 8.

*Confirmed by: vol8 (explicit); vol1 (foundation); vol2, vol5 (biological context)*

---

## Cross-Reference Formats

### INVARIANT-F1: Primary cross-volume dependency

When a KB document requires the reader to navigate to another location to get a definition, use:

```markdown
> → Primary: [Document Name](relative/path/to/target.md) — brief rationale (source label if known)
```

### INVARIANT-F2: Optional cross-volume suggestion

When a KB document suggests (but does not require) navigation to a related location:

```markdown
> ↗ See also: [Document Name](relative/path/to/target.md) — brief rationale
```

Cross-volume references appear in index documents and in leaf documents where the source text explicitly references another section. They must never paraphrase or summarize the target content.
