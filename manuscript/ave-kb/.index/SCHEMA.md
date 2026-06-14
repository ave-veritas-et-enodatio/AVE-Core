# AVE-KB Derived Index — Schema Specification

**Status:** Live — built and hardened (clm- IDs, framework nodes, derived solidity, NaN-propagation, exp- experiment nodes + `experiments:` references, sup- support nodes; experiment-/support-ness conferred by hosting an `exp-id` / `sup-id`. A leaf is a **container** hosting ANY number of ANY combination of `clm` / `exp` / `sup` node-bodies — no one-per-leaf and no one-per-flavor cap). Last revised 2026-05-23.

> **`def-` definition node-type — Stage 1 SPECIFIED + Stage 2 MATERIALIZED (LIVE as of 2026-06-08).** A sixth node-type, `def-` (vocabulary / adjudicated-term), is **specified** below (see "Definition record"), **seeded** in the canonical vocabulary register [`common/vocabulary-register.md`](../common/vocabulary-register.md), and — as of Stage 2 — **materialized + drift-gated** into the pipeline, extending the single identification spine per INVARIANT-S11/S12 ("extend, don't reinvent"). Its record shape, `\bdef-[a-z0-9]{6}\b` id format, and sort position are frozen here. The **emit + drift-gate wiring** is now active: `build_claims_records` emits one `node_type: "definition"` record per register entry into `claims.jsonl`; `verify-kb-metadata` enforces `clm_cross_links` referential integrity (each resolves to a `claim` / `experiment` / `support` node — orphan = hard failure), the `\bdef-[a-z0-9]{6}\b` id format, and the freshness count; `ANY_NODE_ID_RE` and `verify-md-links`'s id-validity check span the `def-` prefix, with the illustrative `def-xxxxxx` field-legend token in the `_ID_PLACEHOLDERS` exemption set. `claims.jsonl` now holds **SEVEN** materialized node types (`claim` / `definition` / `experiment` / `interlock-mechanism` / `support` / `invariant` / `axiom`). A perturbed or malformed `def-` entry fails `make verify-kb-metadata` — the loud-on-drift gate that keeps the spine single (INVARIANT-S12).

> **`interlock-mechanism` node-type + `interlocks` relation — SPECIFIED + MATERIALIZED (LIVE 2026-06-14, INVARIANT-S13).** A seventh node-type, `interlock-mechanism` (`\bilk-[a-z0-9]{6}\b`), and a fourth edge class, `interlocks` (a SYMMETRIC mutual-constraint relation distinct from 1-directional `depends`), are **specified** below (see "Interlock-mechanism record" + `depends-on.jsonl`), **seeded** in the canonical interlock register [`common/interlock-register.md`](../common/interlock-register.md), and **materialized + drift-gated** into the pipeline — extending the single identification spine per INVARIANT-S11/S13 ("extend, don't reinvent"). It makes the calibration-parameter INTERLOCK (mutual constraint) first-class and machine-enforced: each mechanism carries a `real_or_fitted` chord/echo tag, the LIVE independent-parameter count is a verifier-checked DERIVED number that moves when a tag flips, and a falsification-net check propagates a `refuted` interlocked channel to the operating-point root. `refresh-kb-metadata` emits one `node_type: "interlock-mechanism"` record per register entry plus one `interlocks` edge per interlocked constant; `verify-kb-metadata` enforces the `\bilk-[a-z0-9]{6}\b` id format, the `interlocks`-edge referential integrity, the derived count, and the falsification-net wiring.
**Scope:** specifies the canonical JSONL files that live under this directory, the record shapes within each, the build invariants, and the query semantics the runtime module (`src/ave/kb/index.py`) is expected to provide over them.

This directory is **derived** from canonical sources:
- Leaf frontmatter (`claims:`, `experiments:`, `subtree-claims:`, `subtree-experiments:`, `kind:`, `path-stable`, `no-claim`) in every KB `.md` file outside `session/`.
- Experiment-hosting frontmatter (`exp-id:`, `status:`, `strengthens:`) in every leaf that hosts an experiment node — experiment-ness is conferred by HOSTING an `exp-id`, not by a `kind` (the container `kind` stays `leaf` / `leaf-as-index`). A container may host SEVERAL `exp-id:` (each opening its own `status:`/`strengthens:` block) and may co-host `claims:` and `sup-id:` (orthogonal node-bodies) (INVARIANT-S9).
- Support-hosting frontmatter (`sup-id:` + `supports:`) in every leaf that hosts a support node — support-ness is conferred by HOSTING a `sup-id`. A container may host SEVERAL `sup-id:` (each opening its own `supports:` block) and may co-host `claims:` / `exp-id:` / `no-claim:` (INVARIANT-S10).
- Tier 2 inline markers (`<!-- claim-quality: <id> ... -->`) in multi-claim leaves.
- Claim-quality entries in every `claim-quality.md` register (root, per-volume, common).

Every file here is regeneratable from those canonical sources via `make refresh-kb-metadata`. If any file here disagrees with what regeneration would produce, the canonical sources win and the file is rebuilt. The freshness verifier (`make verify-kb-metadata`) runs the build in dry-run and diffs against on-disk; non-empty diff = stale index = hard failure.

**Two-graph model.** A KB `.md` leaf is a **container**, and two orthogonal graphs run through it. (1) The **topography graph** — the hyperlink/navigation tree — in which a container's `kind` (`leaf` | `leaf-as-index` | `index` | `entry-point`) is its structural-position label; `kind` does NOT encode node-flavor. (2) The **claim graph** — an acyclic graph of `clm` (claim), `exp` (experiment), and `sup` (support) node-bodies a leaf *originates*, connected by `strengthens` (exp→clm), `supports` (sup→clm), and `references` (leaf→exp) edges. **A container hosts ANY number of ANY combination of `clm` / `exp` / `sup` node-bodies** — there is no one-per-leaf and no one-per-flavor cap (one file may originate a `claims:` list, several `exp-id:`, and several `sup-id:`). These are declared additively in frontmatter and are independent of the container's `kind`. The reverse views materialized here (`strengthen-by`, `supported-by`, `cites`) are untraversed bookkeeping — convenience indexes, not part of the forward acyclic graph.

---

## File inventory

| File | Records | Sort key | Purpose |
|---|---|---|---|
| `claims.jsonl` | one per graph node (claim / definition / experiment / interlock-mechanism / support / invariant / axiom) | `(node_type, id)` | Canonical graph nodes — claims, framework nodes, experiments, support nodes, definitions, interlock-mechanism nodes |
| `depends-on.jsonl` | one per forward graph edge (`depends` / `strengthens` / `supports` / `interlocks`) | `(source, target, context)` | "What does X depend on / strengthen / support / interlock with?" |
| `strengthen-by.jsonl` | one per open work item | `(claim_id, item_idx)` | "What gates this claim?" / "Where is this strengthen-by item being worked on?" |
| `supported-by.jsonl` | one per (claim, supporting support) edge | `(claim_id, sup_id)` | "Which support nodes lift claim X, and by how much?" (reverse view of `supports` edges; untraversed bookkeeping) |
| `cites.jsonl` | one per (claim, leaf) citation edge | `(claim_id, leaf_path)` | "Which leaves cite claim X?" (inverse of leaf frontmatter) |
| `subtree-aggregates.jsonl` | one per index / entry-point node | `node_path` | Precomputed subtree-claims aggregation |

All files are JSONL — one JSON object per line, no trailing whitespace, single trailing newline at EOF. Keys appear in fixed order per record type (specified below) so byte-identical regeneration is guaranteed.

---

## Build invariants

These hold across every regeneration. They are checked by `personant verify`-style operations (`make verify-kb-metadata` extended):

1. **Determinism.** Running `make refresh-kb-metadata` against the same canonical state yields byte-identical files. No timestamps, no random IDs, no environment-dependent paths embedded in records.
2. **Sort stability.** Each file's records are sorted by the file's sort key. A new claim or edge appears as one inserted line in `git diff`, never reorders surrounding lines.
3. **Schema closure.** Every record matches the schema in this document. Unknown fields are a hard verifier failure (catches drift between schema and emitter).
4. **Referential integrity.** Every ID referenced in `depends-on.jsonl`, `strengthen-by.jsonl`, `cites.jsonl`, or `subtree-aggregates.jsonl` resolves to a record in `claims.jsonl` — which holds claim, framework, **and experiment** nodes. For a `relation:"depends"` edge: `source` resolves to a claim, `target` may resolve to any node type, and `target_kind` must equal the resolved target's `node_type` (kind-match). For a `relation:"strengthens"` edge: `source` resolves to an **experiment** node, `target` resolves to a **claim** (and `target_kind == "claim"`); experiment nodes are never edge `target`s and never appear in `cites`. For a `relation:"supports"` edge (INVARIANT-S10): `source` resolves to a **support** node, `target` resolves to a **claim** (and `target_kind == "claim"`), `strength` is null, and `fraction` is in (0,1] OR the literal `"*pending*"` (distinct on disk from a depends edge's null fraction). For a `relation:"interlocks"` edge (INVARIANT-S13): `source` resolves to a **claim** node, `target` resolves to an **interlock-mechanism** node (and `target_kind == "interlock-mechanism"`), and `strength` / `fraction` / `target_solidity_recorded` are all null; the resolved mechanism node carries a valid `real_or_fitted` tag (tag-present), a `derived_endpoint` that (when non-null) resolves to a claim that is itself an `interlocks`-edge source into that mechanism, and a `cited_leaf` whose file part resolves to an existing KB leaf. The `\bilk-[a-z0-9]{6}\b` id format is enforced for interlock-mechanism nodes; an interlock-mechanism node is never an edge `source` and never appears in `cites`. The `\bsup-[a-z0-9]{6}\b` id format is enforced for support nodes; `supported-by` `claim_id`/`sup_id` must resolve to a claim/support node respectively. `strengthen-by` / `cites` `claim_id` and `subtree-aggregates` `subtree_claims` reference **claim** ids only; `subtree-aggregates` `subtree_experiments` references **experiment** ids only (a claim id there is a kind mismatch). The `\bexp-[a-z0-9]{6}\b` id format is enforced for experiment nodes. (Orphan, kind-mismatch, or relation/source-type mismatch is a verifier failure.)
   - **Leaf `experiments:` references.** A leaf may carry an optional `experiments: [exp-xxxxxx, ...]` frontmatter field — the experiment-reference analog of `claims:` (a leaf-level citation, the inverse of an experiment's Leaf-references; NOT rolled up transitively, NOT for mere prose mentions). Every id in any leaf's `experiments:` must be a well-formed exp-id AND resolve to an actual experiment node (an `exp-id`-declaring leaf). An id that resolves to a claim (`clm-`) instead of an experiment, or resolves to nothing, is a hard verifier failure (not refresh-fixable). The field is **additive**: it is allowed alongside `claims:` OR `no-claim:` and is **not** a primary field — a referencing leaf still satisfies Tier 1 coverage via `claims:`/`no-claim:`. An owning (`exp-id`) experiment-hosting leaf must **not** also carry `experiments:` (an owner does not also reference foreign experiments). Note this is the ONLY exclusivity that survives: `claims:` and `exp-id:` are **not** mutually exclusive — they are orthogonal node-bodies and may co-exist on one leaf.
5. **Single newline EOF.** Every file ends with exactly one `\n`. (Catches editor mishaps and trailing-whitespace creep.)
6. **JSON valid.** Every line parses as a JSON object. (Catches partial writes and merge corruption.)

---

## Record schemas

All field types are JSON types: `string`, `number` (float), `integer`, `boolean`, `null`, `array`, `object`. Solidity / confidence values are floats in [0, 1]. Paths are POSIX-style (forward slashes), relative to `manuscript/ave-kb/`.

### `claims.jsonl`

Despite the name, `claims.jsonl` holds **seven node types** — a type-tagged union discriminated by the `node_type` field (`claim` | `definition` | `experiment` | `interlock-mechanism` | `support` | `invariant` | `axiom`). Claim nodes are one per `<!-- id: clm-xxxxxx -->` canonical entry across all `claim-quality.md` files; framework nodes (invariants + axioms) are parsed from `manuscript/ave-kb/CLAUDE.md`; **experiment nodes** are one per `exp-id: exp-xxxxxx` declaration in a leaf that hosts an experiment (a container may host several) — regardless of whether that same leaf also originates `claims:` / `sup-id:` (INVARIANT-S9); **support nodes** are one per `sup-id: sup-xxxxxx` declaration (a container may likewise host several) (INVARIANT-S10); **definition nodes** are one per `def-xxxxxx` entry in the vocabulary register (INVARIANT-S12); **interlock-mechanism nodes** are one per `ilk-xxxxxx` entry in the interlock register (INVARIANT-S13). The file is **not** split — all node types share one file so a single referential-integrity pass spans the whole graph. (The `definition` group was added by the Stage-2 `def-` materialization 2026-06-08; the `interlock-mechanism` group by INVARIANT-S13 2026-06-14 — the historical "five node types" wording predates both.)

**Claim record** (`node_type: "claim"`) — `node_type` is the FIRST field. `derivation_solidity` (min-branch) and `experimental_solidity` (max-branch) are the two solidity sources; `solidity` is their `max`. 15 fields total.

```typescript
{
  node_type: "claim",            // discriminator — always "claim" here
  id: string,                    // clm-[a-z0-9]{6}; primary key
  title: string,                 // text from the ## heading containing this id
  canonical_path: string,        // e.g. "vol1/claim-quality.md"
  canonical_anchor: string,      // GitHub-style anchor for the heading
  confidence: number,            // 0.0 .. 1.0; hand-authored, from Quality section
  derivation_solidity: number,   // 0.0..1.0; DERIVED gating branch: min(local_quality, dep final solidities) — weakest link; null if pending (NaN-propagating)
  experimental_solidity: number, // 0.0..1.0; DERIVED max-branch: max over RUN-experiment strengthens-edge strengths; null if no run experiment strengthens this claim
  solidity: number,              // 0.0 .. 1.0; DERIVED = max of the non-null branch(es); null (*pending*) iff derivation_solidity null AND experimental_solidity null
  build_status: string,          // DERIVED phrase from solidity band, e.g. "ok to build on" (null if solidity null)
  build_band: string,            // DERIVED from solidity: ok-to-build, ok-with-caveats, input-only, do-not-build, refuted
  rationale: string,             // text after "rationale:" — preserved as single line (LF → ' ')
  depends_on_count: integer,     // count of relation:"depends" edges with source == this id
  strengthen_by_count: integer,  // count of items in strengthen-by.jsonl with claim_id == this id
  citation_count: integer        // count of edges in cites.jsonl with claim_id == this id
}
```

Claim field order: `node_type`, `id`, `title`, `canonical_path`, `canonical_anchor`, `confidence`, `derivation_solidity`, `experimental_solidity`, `solidity`, `build_status`, `build_band`, `rationale`, `depends_on_count`, `strengthen_by_count`, `citation_count`.

**Solidity branches (definitive rule).**
- `derivation_solidity` = the gating branch: `round2(min(local_quality, *dependency final solidities))` — the **weakest link** in the dependency cone, framework deps contributing 1.0 (they never lower the min); **pending propagates NaN-style** through this branch (a pending dependency → pending `derivation_solidity`). Each dependency contributes its own **`solidity`** (the `max`), so building on an experimentally-validated claim correctly un-blocks the dependent. **Why `min`, not a product down the chain?** Solidity must be *refactor-invariant*: splitting one derivation step into two same-quality steps must not lower the result, and a deep clean chain must not decay toward 0 as a pure bookkeeping artifact of how finely the derivation was subdivided. A product `confidence × dep₁ × dep₂ × …` violates both (it is granularity-dependent). The confidence grades are ordinal quality bands, not independent probabilities, so multiplying them is not meaningful; the weakest link in the cone is the honest summary of "how solid is this, end to end". (The change from product → `min` was deliberate; confidence/quality remain hand-assessed and unchanged.)
  - `local_quality(C)` = `max(confidence(C), max over supporting support-nodes S of sup_solidity(S) × f)`, where `f` ∈ (0,1] is the support's on-point fraction for C and a **pending** `sup_solidity` is EXCLUDED from the max (no NaN, no poison) — INVARIANT-S10. With no supports, `local_quality == confidence`. The support on-point fraction `f` is a single edge-weight relevance discount (`sup_solidity × f`) — a lone edge, NOT a chain — so it stays **multiplicative** and is not subject to the granularity argument above. A support lift is still **dep-gated** (throttled by C's own `min(dep finals)`), unlike an experiment's max-branch which bypasses deps. CRITICAL: a pending support never drags a beneficiary with otherwise-valid quality to pending — pending-poison flows ONLY from a claim's own load-bearing `depends-on`, never from an inbound `supports` edge.
  - `sup_solidity(S)` = `round2(min(quality(S), *S's dependency final solidities))` — weakest link, same as a claim's derivation; framework deps 1.0; pending if `quality` pending OR any dep pending; free-standing (no deps) → `quality`. Computed by the SAME shared function as claim solidity (`compute_solidity_full`), so refresh and verify never dual-compute it.
- `experimental_solidity` = `max` of the `strength` on every `relation:"strengthens"` edge into this claim whose source experiment has `status:"run"`. Unrun experiments contribute nothing (excluded from the max — **no NaN, no 0.0 floor**). `null` if no run experiment strengthens this claim.
- `solidity` = `max(derivation_solidity, experimental_solidity)` over the non-null branches; **`*pending*` (null) iff BOTH are null** — i.e. derivation pending AND no run experiment. (`*pending*` = unassessed ≠ `0.0` = refuted; an unrun experiment can never float a pending claim down to a refuted 0.0.)
- **Non-transitive:** a `strengthens` edge lifts only its directly-targeted claim. An experiment that also bears on an upstream input authors a *separate* `strengthens` edge to that input with its own `strength`.

**Experiment record** (`node_type: "experiment"`) — a *physical* experiment node. Experiments are terminal strength-sources: they have **no `relation:"depends"` edges** and never gate; they only emit `relation:"strengthens"` edges to the claims their result bears on. 6 fields.

```typescript
{
  node_type: "experiment",       // discriminator
  id: string,                    // exp-[a-z0-9]{6}; primary key
  title: string,                 // experiment / project leaf title
  canonical_path: string,        // POSIX path of the experiment leaf, relative to ave-kb/
  canonical_anchor: string,      // GitHub-style anchor for the heading carrying the exp-id
  status: "run" | "pending"      // "run" = result exists (its strengthens edges count); "pending" = unrun (its edges contribute nothing)
}
```

Experiment field order: `node_type`, `id`, `title`, `canonical_path`, `canonical_anchor`, `status`. A **physical** experiment **we design, originate, and control** only — simulations are NOT experiments (a simulation feeds derivation confidence, not experimental solidity), and a re-analysis of outside/public data (LIGO, SPARC, CMB, …) is a `sup-` support node (INVARIANT-S10) or a `clm-` citation, never an `exp-` (see INVARIANT-S9). A container may host SEVERAL `exp-id:` (each `exp-id:` key opens its own `status:`/`strengthens:` block; a single `exp-id:` is the one-element case, so existing single-experiment leaves are unchanged) and may also originate its own `claims:` and/or `sup-id:` — orthogonal node-bodies in one container, not mutually exclusive. When co-hosted, the leaf emits a `node_type: claim` record AND one `node_type: experiment` record per `exp-id` (all sharing the container's canonical home), and an experiment's `strengthens` edge may target that same leaf's own claim (a node→node edge between two distinct co-located nodes — not a self-loop).

**Support record** (`node_type: "support"`) — a non-physical analytical SUPPORT node (INVARIANT-S10). A support is claim-like inside (carries a local-rigor `quality` and may consume its own `depends-on` claims), experiment-like in fan-out (one support may help many claims via `relation:"supports"` edges), and contributes to the DERIVATION branch of each beneficiary (never the experimental/max branch). 7 fields.

```typescript
{
  node_type: "support",          // discriminator
  id: string,                    // sup-[a-z0-9]{6}; primary key
  title: string,                 // support / analysis leaf title (its `##`/`#` heading)
  canonical_path: string,        // POSIX path of the support-hosting leaf, relative to ave-kb/
  canonical_anchor: string,      // GitHub-style anchor for the heading
  quality: number | null,        // 0.0..1.0; hand-authored local rigor (claim-`confidence` analog); null if *pending*
  solidity: number | null        // 0.0..1.0; DERIVED sup_solidity = round2(min(quality, dep final solidities)) — weakest link; null if pending
}
```

Support field order: `node_type`, `id`, `title`, `canonical_path`, `canonical_anchor`, `quality`, `solidity`.

A support node's `quality` / `depends-on` / `solidity` write-back live in a **claim-quality-style entry keyed by the sup-id** (a `<!-- id: sup-xxxxxx -->` marker + a `### Quality` block with `quality:` / `depends-on:` / `solidity:` / `rationale:`, parallel to a claim entry — `quality:` in place of `confidence:`). The beneficiary fan-out is authored in the **hosting leaf's** `supports:` frontmatter block (parallel to an experiment's `strengthens:`), one `clm-<id>: <fraction>` pair per beneficiary. A container may host SEVERAL `sup-id:` — each `sup-id:` key opens its own `supports:` block (the pairs that follow belong to that block until the next `sup-id:`); a single `sup-id:` is the one-element case. Each `sup-id` materializes its own support record (sharing the container's canonical home) and its own `supports` edges. A leaf may co-host `sup-id:` with `claims:` / `exp-id:` / `no-claim:` — orthogonal node-bodies. `sup_solidity` is dep-gated and pending-propagating exactly like a claim's derivation; a free-standing support (no deps) has `sup_solidity == quality`.

**Definition record** (`node_type: "definition"`) — SPECIFIED (Stage 1) + **MATERIALIZED (Stage 2, LIVE — emitted into `claims.jsonl` as of 2026-06-08)**. A `def-` node is an **adjudicated vocabulary term** — the third tracked index after the claim graph (`clm`/`exp`/`sup`) and the code-provenance index. It records the *locked meaning* of a load-bearing term, the substrate **axis** it lives on, its **dimension/type**, an adjudication **status**, the `clm`/`exp`/`sup` ids it is load-bearing for, and — for an overloaded term — an **open-ambiguity flag** plus the verified file:line **conflicting sites**. A definition is a **terminal metadata node**: like a framework node it carries NO scoring fields (no `confidence`/`solidity`/`quality`), and like a framework node it emits NO graph edges — it never participates in `depends` / `strengthens` / `supports`. Its `clm_cross_links` are reverse-citation bookkeeping (which claims a term is load-bearing for), never traversed for solidity. Definitions are register-hosted (the way `clm-`/`sup-` entries are hosted in a `claim-quality.md` register): one per `<!-- id: def-xxxxxx -->` marker in the canonical vocabulary register `common/vocabulary-register.md`. 11 fields.

```typescript
{
  node_type: "definition",       // discriminator
  id: string,                    // def-[a-z0-9]{6}; primary key (greppable \bdef-[a-z0-9]{6}\b)
  term: string,                  // the vocabulary term (surface form, e.g. "node", "r_opt", "κ_share")
  adjudicated_meaning: string,   // the locked meaning — single-line normalized (LF → ' ')
  axis: string,                  // "spatial-Brillouin" | "phase-carrier" | "dimensionless" | "notation" | "other"
  dimension: string,             // dimension / type, e.g. "length (L)", "frequency (T⁻¹)", "dimensionless", "n/a (notation)"
  status: string,                // "SOLID" | "ambiguous" | "proposed" | "retired"
  canonical_path: string,        // POSIX path of the register leaf (the term's home) — relative to ave-kb/
  canonical_anchor: string,      // GitHub-style anchor for the term's heading in the register
  clm_cross_links: string[],     // sorted unique clm-/exp-/sup- ids this term is load-bearing for (reverse bookkeeping; may be empty)
  open_ambiguity: boolean,       // true iff the term is overloaded (≥2 conflicting corpus meanings to disambiguate)
  conflicting_sites: string[]    // when open_ambiguity: verified "path:line" sites carrying the conflicting meanings (sorted; [] when open_ambiguity false)
}
```

Definition field order: `node_type`, `id`, `term`, `adjudicated_meaning`, `axis`, `dimension`, `status`, `canonical_path`, `canonical_anchor`, `clm_cross_links`, `open_ambiguity`, `conflicting_sites`.

**Status semantics (definitive rule).**
- `SOLID` — the meaning is locked AND the cite confirms it (e.g. `node` = spatial-Nyquist / Brillouin cell per `vol1/dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md:10`). A `SOLID` term MAY still carry `open_ambiguity: true` (the canonical sense is locked, but the same word is used loosely elsewhere and must be qualified) — the two fields are orthogonal (status = "is the canonical sense adjudicated?"; open_ambiguity = "is the surface form overloaded?").
- `ambiguous` — the term has ≥2 corpus meanings and NO single locked sense yet; canonization is gated on adjudication. Always carries `open_ambiguity: true` + the `conflicting_sites`.
- `proposed` — a coined term gated on review, verified to have **0 prior corpus hits** (e.g. `κ_share`, `r_env`, `node-Nyquist-size-boundary`). NEVER seed a coinage `SOLID` — a coinage with prior hits is a collision, not a coinage.
- `retired` — a superseded / walked-back term, preserved (Rule 12 substitution-not-retraction) so a grep for it resolves to its replacement.

**Stage-2 materialization rule (LIVE).** `refresh-kb-metadata` parses each `<!-- id: def-xxxxxx -->` entry in the vocabulary register, emits one `node_type: "definition"` record into `claims.jsonl`, and the sort key `(node_type, id)` places the `definition` group **between `claim` and `experiment`** (ASCII: axiom < claim < **definition** < experiment < invariant < support). `verify-kb-metadata` extends the referential-integrity pass so every id in `clm_cross_links` resolves to a `claim` / `experiment` / `support` node (orphan = hard failure), enforces the `\bdef-[a-z0-9]{6}\b` id format, and adds the def-count to the freshness check. No new edge file is touched (definitions emit no edges). `ANY_NODE_ID_RE` (and `verify-md-links`'s `_ID_RE` / id-validity check) span the `def` prefix, and the illustrative `def-xxxxxx` token is in the `_ID_PLACEHOLDERS` exemption set (alongside `clm-xxxxxx` / `exp-xxxxxx` / `sup-xxxxxx`) so the register's field-legend placeholder is not flagged as an orphan id. The parser (`kb_index_lib.parse_definition_entries`) raises `DefinitionEntryError` on a malformed `def-` id, an unknown `status`, a missing required field, or an `ambiguous` term whose mandatory open-ambiguity flag is dropped — the parser-level half of the drift-gate.

**Interlock-mechanism record** (`node_type: "interlock-mechanism"`) — SPECIFIED + MATERIALIZED (LIVE 2026-06-14, INVARIANT-S13). An `ilk-` node is a **joint-constraint mechanism** — the named substrate relation that mutually constrains two (or more) calibration constants (e.g. R·r=1/4 linking the operating point u₀* and α). It is the seventh tracked node type, a deliberate spine extension per INVARIANT-S11 (extend, don't reinvent). Like a definition / framework node it carries **NO scoring fields** (no `confidence` / `solidity` / `quality`) and **originates no `depends` / `strengthens` / `supports` edges**; unlike them it IS a valid edge **target** — the hub of the symmetric `interlocks` relation (see `depends-on.jsonl` below): each interlocked constant emits one `interlocks` edge whose `target` is this mechanism node, so the joint-constraint's two endpoints are the two `interlocks`-edge **sources** sharing this hub. Interlock-mechanism nodes are **register-hosted** — one per `<!-- id: ilk-xxxxxx -->` marker in the canonical interlock register `common/interlock-register.md` (the `ilk-` analog of how `def-` entries are hosted in the vocabulary register and `clm-`/`sup-` entries in a `claim-quality.md` register). 10 fields.

```typescript
{
  node_type: "interlock-mechanism", // discriminator
  id: string,                    // ilk-[a-z0-9]{6}; primary key (greppable \bilk-[a-z0-9]{6}\b)
  title: string,                 // mechanism name, from the ## <title> heading
  mechanism: string,             // the constraint statement — single-line normalized (LF → ' ')
  real_or_fitted: string,        // "real-geometric-constraint" | "mixed" | "fitted-identification" — the chord/echo classification (3 values)
  status: string,                // "SOLID" | "proposed" | "retired"
  derived_endpoint: string | null, // the constant-claim id made DEPENDENT iff real_or_fitted == real-geometric-constraint (the DOF this chord removes); null if none designated
  canonical_path: string,        // POSIX path of the register leaf (the mechanism's home) — relative to ave-kb/
  canonical_anchor: string,      // GitHub-style anchor for the mechanism's ## heading in the register
  cited_leaf: string             // the EXISTING corpus leaf grounding the mechanism, "path:line[,line-range]" (ave-canonical-leaf-pull anchor; the file part is verifier-resolved)
}
```

Interlock-mechanism field order: `node_type`, `id`, `title`, `mechanism`, `real_or_fitted`, `status`, `derived_endpoint`, `canonical_path`, `canonical_anchor`, `cited_leaf`.

**`real_or_fitted` is the chord/echo axis (definitive rule, INVARIANT-S13; THREE values as of the 2026-06-14 G-ruling).** `real-geometric-constraint` = a **chord**: the substrate independently forces the relation, so it removes one degree of freedom from the calibration-parameter count (its `derived_endpoint` becomes dependent). `fitted-identification` = an **echo**: a named identification the substrate does NOT independently select (a consistency match), so it buys **NO** parameter reduction — the count is unchanged. `mixed` = **form-derived / value-fitted** (added 2026-06-14 for G — gravity's FORM is derived from Ax 1 + Ax 4 SYM scaling (the Achromatic-Lens: ε·μ co-scale → Z=Z₀, Γ=0; the /7 PPN couplings), but G's VALUE is a calibration input (the Machian-boundary-impedance termination ξ is back-solved from CODATA G via `ξ=ℏc/(7Gm_e²)` — circular, not forward). **COUNT SEMANTICS (load-bearing): `mixed` and `fitted-identification` BOTH do NOT reduce the count; ONLY `real-geometric-constraint` reduces.** A `mixed` mechanism still carries a `derived_endpoint` (the constant that WOULD become dependent if the mechanism's value-fitted half were ever closed form-first — e.g. G via Chain B′ flips `mixed→real`), but until then it buys no reduction, exactly like a fitted echo. This is `consistency-vs-emergence` made machine-enforced per mechanism rather than narrated. A `derived_endpoint` reduces the count ONLY on a `real-geometric-constraint`; on `fitted-identification` or `mixed` it is informational.

**Status semantics.** `SOLID` (the mechanism + its real/fitted classification are adjudicated and the cite confirms), `proposed` (gated on review — the default for a newly minted mechanism), `retired` (superseded / walked-back, preserved per Rule 12). A newly minted mechanism is seeded `proposed`, never `SOLID`.

**Materialization + drift-gate (INVARIANT-S13).** `refresh-kb-metadata` parses each `<!-- id: ilk-xxxxxx -->` register entry and emits one `node_type: "interlock-mechanism"` record into `claims.jsonl` PLUS one `relation: "interlocks"` edge per interlocked constant into `depends-on.jsonl` (the register entry's `interlocks:` list authors the edges — single source of truth, no drift). The sort key `(node_type, id)` slots the `interlock-mechanism` group **between `experiment` and `invariant`** (axiom < claim < definition < experiment < **interlock-mechanism** < invariant < support), so no existing record's relative order changes. `verify-kb-metadata` enforces the `\bilk-[a-z0-9]{6}\b` id format, that `real_or_fitted` / `status` are in their enums, that `derived_endpoint` (when non-null) resolves to a claim that is one of the mechanism's interlocked sources, that `cited_leaf`'s file part resolves to an existing KB leaf, and the `interlocks`-edge referential integrity (below). A perturbed register entry fails `make verify-kb-metadata` — the loud-on-drift gate that keeps the spine single (INVARIANT-S11/S13).

**Framework record** (`node_type: "invariant"` or `"axiom"`) — exactly 5 fields. Framework nodes carry no scoring fields: they are **solidity-1.0 by definition** (framework bedrock). This is a documented rule, not a stored field.

```typescript
{
  node_type: "invariant" | "axiom",
  id: string,                    // "INVARIANT-XX" verbatim, or "axiom-N" lowercase (N in 1..4)
  title: string,                 // invariant heading title, or axiom bold-text title
  canonical_path: "CLAUDE.md",   // always — framework nodes live in CLAUDE.md
  canonical_anchor: string       // GitHub-style slug (see provenance below)
}
```

Framework field order: `node_type`, `id`, `title`, `canonical_path`, `canonical_anchor`.

**Framework-node provenance** (from `manuscript/ave-kb/CLAUDE.md`):

- **Invariants** (18) — parsed from `### INVARIANT-XX: <title>` headings (regex `^### (INVARIANT-[A-Z]+[0-9]+):\s*(.+)$`). `id` is the label verbatim; `canonical_anchor` is the slug of the node's own heading. `INVARIANT-S6` (the subsumed-into-S5 tombstone) is a real heading and is included so a reference to it resolves.
- **Axioms** (4) — parsed from the `- Axiom N: **<title>** — ...` bullets in the INVARIANT-S2 section (regex `^- Axiom ([1-4]): \*\*(.+?)\*\*`). `id` is `axiom-N` lowercase; `title` is the bold text. All four axioms point at the slug of the `### INVARIANT-S2: AVE Axiom numbering` heading — the KB's axiom-numbering authority.

**Sort key.** Records are sorted by `(node_type, id)` — explicit grouping by ASCII order of the discriminator: axioms, then claims, then **definitions**, then experiments, then **interlock-mechanisms**, then invariants, then **support** (alphabetical: axiom < claim < **definition** < experiment < **interlock-mechanism** < invariant < support). The Stage-2 `def-` materialization (LIVE 2026-06-08) inserted the `definition` group between `claim` and `experiment`; the INVARIANT-S13 `interlock-mechanism` materialization (LIVE 2026-06-14) inserts that group between `experiment` and `invariant` (`experiment` < `interlock-mechanism` because `'e'(101) < 'i'(105)`; `interlock-mechanism` < `invariant` because at index 2 `'t'(116) < 'v'(118)`). Each is a NEW group inserted at its ASCII position, so no pre-existing record's relative order changed — the existing nodes stay byte-identical.

**`build_band` derivation** (mechanical, from solidity):

| Solidity range | `build_band` value |
|---|---|
| 0.85 ≤ s ≤ 1.00 | `ok-to-build` |
| 0.65 ≤ s < 0.85 | `ok-with-caveats` |
| 0.45 ≤ s < 0.65 | `input-only` |
| 0.20 ≤ s < 0.45 | `do-not-build` |
| 0.00 ≤ s < 0.20 | `refuted` |

This mirrors the build-status legend in the root `claim-quality.md` and provides a machine-stable enum for filtering even if the human-readable `build_status` phrasing drifts.

**Solidity is derived, not parsed.** `solidity`, `build_status`, and `build_band` are NOT read from the claim-quality.md `solidity` line — they are computed by `kb_index_lib.compute_solidity` from the hand-authored `confidence` values and the depends-on DAG (`solidity = round-half-up-2dp(min(confidence, *dependency solidities))` — the weakest link; framework-target dependencies contribute 1.0 and never lower the min). The claim-quality.md `solidity` line is itself a write-back of the same computation (`make refresh-kb-metadata`). The freshness verifier hard-fails if the on-disk claim-quality.md solidity content or these JSONL fields disagree with the recomputed values.

**HARD RULE — `*pending*` propagates transitively (NaN semantics).** A claim's solidity is `*pending*` (uncomputable) if its `confidence` is `*pending*` (not yet quality-assessed) **OR** any of its dependencies' solidity is `*pending*` — **regardless of the claim's own local `confidence`**. A claim with `confidence: 1.0` that depends on one pending claim still has solidity `*pending*`. Pending-ness propagates through the depends-on DAG exactly like NaN through arithmetic. Framework-node dependencies (invariant / axiom targets) are **never** pending — they are solidity-1.0 bedrock by definition, so a claim depending only on framework nodes is not pending (its solidity equals its confidence). A claim with a pending solidity carries `null` for `solidity`, `build_status`, and `build_band` in `claims.jsonl`, the bare `- solidity: *pending*` line in claim-quality.md, and `(solidity *pending*)` wherever it is a depends-on target. Every consumer treats "absent from `compute_solidity`'s result" identically to "pending".

**Rationale-text normalization:** preserve text verbatim except for collapsing internal line breaks to single spaces (so rationale is one-line JSON-safe). Inline markdown (backticks, asterisks) is preserved.

### `depends-on.jsonl`

One record per directed claim-graph edge. The file holds **four edge classes** discriminated by `relation`:

- **`depends`** (gating, min-branch): `source` is a **claim** OR a **support** id (a support's own deps are `depends` edges sourced at the sup-id); `target` is a claim / invariant / axiom id. `strength` and `fraction` are null.
- **`strengthens`** (max-branch): `source` is an **experiment** id; `target` is a **claim** id; carries a `strength`. `fraction` null. Authored from the experiment leaf's `strengthens:` block.
- **`supports`** (DERIVATION-branch lift, INVARIANT-S10): `source` is a **support** id; `target` is a **claim** id; `target_kind` is `"claim"`; carries an on-point `fraction` ∈ (0,1] **OR** the literal string `"*pending*"` (an intended-but-unassessed edge); `strength` null. The `"*pending*"` fraction is DISTINCT on disk from a `depends` edge's `null` fraction: null means "no fraction applies to this edge class", `"*pending*"` means "a fraction applies but is unassessed". A pending fraction contributes nothing to the beneficiary's `local_quality` (excluded from the max, like a pending `sup_solidity`) and never poisons it. Authored from the support leaf's `supports:` block and emitted by `refresh`. The derivation-branch analog of a `strengthens` edge.
- **`interlocks`** (SYMMETRIC mutual-constraint, INVARIANT-S13 — **NOT traversed for solidity**): `source` is a **claim** id (a calibration constant); `target` is an **interlock-mechanism** id (`target_kind: "interlock-mechanism"`); `strength`, `fraction`, and `target_solidity_recorded` are all null; `context` carries the mechanism's `real_or_fitted` tag as an at-a-glance human note (authoritative tag lives on the mechanism node). **Symmetric-encoding convention (hub-node, NOT mirrored directed pairs):** a joint-constraint among N constants is encoded as N `interlocks` edges, one from each constant to a SHARED interlock-mechanism node — the symmetry is represented by the shared `target` (the hub), so the edges stay directed and the existing loader's directed-edge assumption is unchanged (no mirrored A→B + B→A rows, no symmetric-sort convention needed). The joint-constraint's two endpoints are the two `interlocks`-edge sources sharing one mechanism hub; the mechanism-node id is the shared target; the `real_or_fitted` tag is on the mechanism node. `interlocks` edges are **never** consumed by `compute_solidity` (which follows only `depends`) — they drive the LIVE independent-parameter count and the falsification-net checks instead. Authored from the interlock register's `interlocks:` list and emitted by `refresh`.

```typescript
{
  source: string,                          // claim/support id (depends) | experiment id (strengthens) | support id (supports) | claim id (interlocks)
  target: string,                          // claim/invariant/axiom (depends); claim (strengthens / supports); interlock-mechanism id (interlocks)
  relation: "depends" | "strengthens" | "supports" | "interlocks",  // edge class
  target_kind: "claim" | "invariant" | "axiom" | "interlock-mechanism",  // node type of the target
  target_solidity_recorded: number | null, // depends: dep solidity as written; null for framework / strengthens / supports / interlocks
  strength: number | null,                 // strengthens: conferred experimental-solidity in [0,1]; null otherwise
  context: string | null,                  // optional context note (interlocks: the mechanism's real_or_fitted tag, human-facing)
  fraction: number | "*pending*" | null    // supports: on-point fraction f ∈ (0,1] or "*pending*" (unassessed); null otherwise
}
```

Field order: `source`, `target`, `relation`, `target_kind`, `target_solidity_recorded`, `strength`, `context`, `fraction`. Every record carries all eight keys (schema closure); only the relevant ones are non-null per edge class.

`relation` is recoverable from `source`-node type (claim ⇒ depends, experiment ⇒ strengthens), but is stored explicitly so a human reviewer sees each edge's *role* at a glance and `compute_solidity` need not cross-reference node types. A `strengthens` edge's `strength` is the per-(experiment, claim) conferred experimental-solidity — typically `1.0` for the experiment's designed target on an unequivocal result, lower for orthogonally-implicated claims; it counts only when the source experiment has `status: "run"`.

**Bullet-head extraction.** A depends-on bullet's dependency target(s) live in its *head*, not its title/context. The head is the bullet text after the leading `- `, truncated at the EARLIER of: the first ` — ` (em-dash title separator) or the first ` (` (paren). The head is scanned for ALL recognized target tokens, emitting **one edge per token**:

- `\bclm-[a-z0-9]{6}\b` → `target_kind: "claim"`; `target_solidity_recorded` parsed from a `(solidity <num>)` group; `context` from a trailing `[...]` group (an `[= ...]` arithmetic annotation is skipped).
- `\bINVARIANT-[A-Z]+[0-9]+\b` → `target_kind: "invariant"`, `target` the label verbatim, `target_solidity_recorded: null`; `context` from the bullet's first `(...)` paren content.
- `\bAxiom [1-4]\b` → `target_kind: "axiom"`, `target` normalized to `axiom-N` lowercase, `target_solidity_recorded: null`; `context` from the first `(...)` paren content.

A normal claim bullet `- clm-unk0bd — Title (solidity 0.4)` has head `clm-unk0bd` → one claim edge. A framework bullet `- INVARIANT-S2 / Axiom 4 (saturation kernel — ...)` has head `INVARIANT-S2 / Axiom 4` → two edges (invariant + axiom), both carrying the paren content as context.

**Non-edges:** Quality sections may contain a placeholder line like `- *(none entry-local — ...)*`. These are recognized by the leading asterisk + italic marker and produce zero edges. A bullet whose head contains no recognized token also produces zero edges — e.g. `- none entry-local — Axiom 4 is framework input...` has head `none entry-local`; the `Axiom 4` after the em-dash is explanatory text, not a target, and is not scanned.

**Sort key.** `(source, target, context)` — a null context sorts as the empty string. The context component keeps two edges from the same source to the same target (e.g. an `INVARIANT-S2` dependency declared in two separate bullets with different context notes) deterministically ordered.

### Interlock structure: independent-parameter count + falsification net (INVARIANT-S13)

Two DERIVED, verifier-checked quantities ride on the `interlocks` relation. Neither is materialized as a JSONL record file; both are recomputed by `verify-kb-metadata` from `claims.jsonl` + the `interlocks` edges and the assertions in the interlock register's meta header.

**LIVE independent-parameter count (replaces the prose-stated count).** The framework's calibration-parameter count was previously stated only in prose (`clm-5xon03`: 26 SM parameters → `{m_e, α, G}` + 4 axioms). It is now ALSO a DERIVED number the verifier recomputes and CI-asserts. **As of the 2026-06-14 G-ruling the node set is the explicitly-marked CALIBRATION set, not the build-readiness band:**

```
independent_count = (# claim nodes in the marked calibration set)
                    − |{ derived_endpoint(m) : m is a REAL-tagged interlock-mechanism
                                               that is WIRED (has interlocks edges),
                                               derived_endpoint(m) resolves to a claim,
                                               and that claim is in the calibration set }|
```

The calibration set is declared in the interlock register's meta header as a `calibration-params:` list (machine-identifiable, swappable — the same convention as `operating-point-root:` / `expected-independent-count:`); each id must resolve to a `claim` node (referential integrity). At the G-ruling it is `{clm-0ktpcn (α), clm-5xon03 (m_e mass-scale), clm-dsb560 (G — its Route-2)}` = **3**. (When no `calibration-params:` is declared the count falls back to the legacy `build_band == "input-only"` set — the pre-G-ruling default, retained for KB states without the marker.)

A `real-geometric-constraint` mechanism is a **chord**: it removes one DOF (its `derived_endpoint` becomes dependent) and lowers the count. A `fitted-identification` **echo** and a `mixed` (form-derived/value-fitted) mechanism BOTH remove NONE, so the count is unchanged ("an echo buys no parameter reduction; only a chord does" — and a mixed mechanism's value-fitted half is, for counting, an echo until its flip-test closes). The interlock register declares an `expected-independent-count:` in its meta header; `verify-kb-metadata` recomputes and **hard-fails on mismatch**. So a tag flip (`fitted`/`mixed`→`real`) visibly moves the count and breaks the assertion until the author deliberately updates it — the loud-on-drift gate applied to the framework's headline parameter-economy claim. (Concretely: α's `ilk-rr14gt` flipping `fitted→real`, or G's `ilk-gravmb` flipping `mixed→real` via Chain B′, each drops the count 3→2.)

> **Semantics caveat — RESOLVED by the 2026-06-14 G-ruling.** The earlier draft counted the literal `build_band == "input-only"` set (143 at materialization), a BUILD-READINESS band, NOT the calibration-parameter enumeration `{m_e, α, G}` (3) of `clm-5xon03` ("input" had two meanings). Grant's G-ruling adjudicated the canonical denominator to be the calibration set: the count function (written swappable) is now repointed to the `calibration-params:`-marked set, so the live count is **3** (all three fitted/mixed-value, none `real`-reduced). The build-band path remains only as the unmarked fallback.

**Falsification net (the model's strongest claim, CI-enforced).** Per `omega-freeze-cosmic-grain-cascade.md:11`: the substrate has ONE degree of freedom (the operating point u₀*); the N observables project onto N joint-constrained channels; **falsification of any one kills the operating point and the entire model**. Encoded as: the interlock register declares an `operating-point-root:` (the single-DOF node, `clm-iouqn9` = K4 Magic-Angle u₀*≈0.187); the **channels** are the distinct `interlocks`-edge source constants EXCLUDING the root. `verify-kb-metadata` hard-fails if ANY channel claim's `build_band == "refuted"` (solidity < 0.20), naming the operating-point root in the failure — the refutation of one interlocked channel propagates a visible failure to the root, exactly as the corpus claims. (Root assignment rationale: the operating-point u₀* node `clm-iouqn9` is the single DOF the channels project from and that "dies" if a channel is refuted; the net-statement claim `clm-dsb560` hosts the prose + the Ω_freeze IC but is not itself the operating point.)

### `strengthen-by.jsonl`

One record per `strengthen-by` bullet in a claim's Quality section.

```typescript
{
  claim_id: string,        // the claim whose Quality section contains this strengthen-by item
  item_idx: integer,       // 0-indexed position within the strengthen-by list (preserves order)
  text: string,            // bullet text, single-line normalized
  mentioned_ids: string[]  // claim ids mentioned in `text` (lowercase, deduplicated, sorted)
}
```

Field order: `claim_id`, `item_idx`, `text`, `mentioned_ids`.

**Multi-line bullets** are collapsed to single lines (LF → ' '), preserving inline markdown.

**`mentioned_ids` extraction:** match the `\bclm-[a-z0-9]{6}\b` pattern in `text`. The `clm-` prefix makes the pattern exact — it cannot match incidental English or physics words. A `clm-`-shaped token that doesn't match any record in `claims.jsonl` is still emitted, and signals a typo or stale reference (the verifier flags orphan-style consistency issues globally).

### `supported-by.jsonl`

One record per (claim, supporting support-node) edge — the reverse view of the `supports` edges in `depends-on.jsonl` (INVARIANT-S10). It answers "which support nodes lift claim X, and by how much?". It is **untraversed bookkeeping** — solidity flows forward through the `supports` edges; this file is a convenience reverse index analogous to `strengthen-by`, never consulted in the solidity computation.

```typescript
{
  claim_id: string,          // the beneficiary claim
  sup_id: string,            // the supporting support node (sup-[a-z0-9]{6})
  fraction: number | "*pending*", // the on-point fraction f ∈ (0,1] of this support for this claim, or "*pending*" if unassessed
  sup_solidity: number | null // the support's computed sup_solidity (same shared computation); null if pending
}
```

Field order: `claim_id`, `sup_id`, `fraction`, `sup_solidity`. Sort key `(claim_id, sup_id)`. Referential integrity: every `claim_id` resolves to a `claim` node and every `sup_id` to a `support` node in `claims.jsonl`.

**Leaf-references footer (derived).** Each `clm-` / `exp-` / `sup-` entry in a `claim-quality.md` register carries a `> **Leaf references:**` blockquote footer — the reverse-citation map of which leaves host the entry's id. It is a **derived field** regenerated by `make refresh-kb-metadata` (`kb_index_lib.build_leaf_references` → `render_leaf_references`) and drift-gated by `make verify-kb-metadata`, exactly like `subtree-claims` and the derived `solidity` line; **do not hand-edit it.** The map is fully derivable from leaf frontmatter: a `clm-` lists every leaf whose `claims:` declares it (the same leaf→claim edges in `cites.jsonl`); an `exp-` lists its canonical home (the `exp-id:`-hosting leaf) plus any leaf referencing it via `experiments:`; a `sup-` lists its canonical home (the `sup-id:`-hosting leaf). Each footer is a single blockquote line of stable-sorted relative Markdown links (`[<name>](./<rel>)`, where `<rel>` is the leaf path relative to the register's directory and `<name>` is the leaf filename stem — real link text, no backticks, so the footer links are checked by `verify-md-links` and a dead path *gates* instead of rotting silently), comma-joined, with **all free-text editorial annotations dropped** (the rot the derived footer eliminates). The footer is found-and-replaced as one stable region between the entry's `<!-- id: … -->` marker and its `### Quality` heading (inserted there if absent). A hand-edited or stale footer is a `refresh-fixable` verifier failure. The bidirectional-coverage check guarantees every canonical entry is cited by ≥ 1 leaf, so an empty footer is abnormal; an id with no citing leaf regenerates to an explicit `*(none …)*` marker rather than a bare prefix.

### `cites.jsonl`

One record per (claim, leaf) citation edge. A leaf's frontmatter `claims: [a, b, c]` produces three edges.

```typescript
{
  claim_id: string,         // clm-[a-z0-9]{6} id
  leaf_path: string,        // POSIX path relative to manuscript/ave-kb/
  leaf_kind: string,        // "leaf" or "leaf-as-index"
  tier2_marked: boolean     // true iff leaf body has a proximal <!-- claim-quality: <id> ... --> marker for this id
}
```

Field order: `claim_id`, `leaf_path`, `leaf_kind`, `tier2_marked`.

**`tier2_marked` semantics:** matches the existing Tier 2 verifier rule (INVARIANT-S8). For single-claim leaves, Tier 2 is not required by the verifier; in those cases `tier2_marked` is `false` unless the leaf chose to also include a marker. The flag captures observed state, not requiredness; downstream consumers can filter by it.

### `subtree-aggregates.jsonl`

One record per index file (`kind: index`) plus the single entry-point node.

```typescript
{
  node_path: string,            // POSIX path relative to manuscript/ave-kb/
  node_kind: string,            // "index" or "entry-point"
  subtree_claims: string[],     // sorted unique list of all claim ids OWNED under this node's subtree
  subtree_experiments: string[] // sorted unique list of all exp-ids OWNED under this node's subtree
}
```

Field order: `node_path`, `node_kind`, `subtree_claims`, `subtree_experiments`.

This file persists what `refresh-kb-metadata` already computes transiently for the frontmatter `subtree-claims:` and `subtree-experiments:` fields. Having it materialized as JSONL means cross-volume aggregation queries don't require re-walking the tree.

**`subtree_experiments` (owned-only).** The union of exp-ids OWNED (declared via `exp-id:`) by experiment leaves under this node's directory (`kind: index`) or the whole KB (`kind: entry-point`). It is the experiment analog of `subtree_claims`, and OWNED-ONLY in the same sense: just as a leaf's foreign depends-on references never enter `subtree_claims` (only its owned `claims:` support rolls up), a leaf's `experiments:` REFERENCES never propagate into `subtree_experiments` — only an experiment leaf's own `exp-id:` declaration does. Sorted with the same ordering convention as `subtree_claims`. Both this JSONL key and the frontmatter `subtree-experiments:` field are derived from the single shared `kb_index_lib.compute_subtree_aggregates`, so the materialized aggregate, the refresh write-back, and the verify consistency check cannot drift; declared `subtree-experiments` ≠ the computed owned union is a refresh-fixable verifier failure.

---

## Query semantics (`src/ave/kb/index.py`)

The runtime module loads these JSONL files once per process and exposes the canonical question shapes as Python functions. Stdlib only (no pip deps).

```python
from ave.kb import index

idx = index.load()                    # default: $REPO/manuscript/ave-kb/.index/
idx = index.load(path="...")          # explicit path override

# Forward dependency edges (work for any node id, including framework ids)
idx.depends_on("clm-0ktpcn")              # → list[str] of target node ids
idx.dependents_of("clm-unk0bd")           # → list[str] of source claim ids (inverse)
idx.dependents_of("INVARIANT-S2")         # → claims that break if this invariant changes

# Open work
idx.strengthen_by("clm-trf3bd")           # → list[StrengthenByItem]
idx.gated_on("clm-unk0bd")                # → list[str] of claim_ids whose strengthen-by mentions "clm-unk0bd"

# Citation / leaf membership
idx.cited_by("clm-0ktpcn")                # → list[CitationEdge] (leaves citing this claim)
idx.claims_in_leaf("vol1/ch8-...")    # → list[str] of claim ids cited by that leaf

# Subtree aggregation
idx.subtree_claims("vol1")            # → list[str] of all claim ids under vol1/
idx.subtree_claims("")                # → list[str] (whole tree; same as entry-point's aggregate)

# Filters
idx.solidity_below(0.7)               # → list[Claim] with solidity < threshold
idx.in_band("do-not-build")           # → list[Claim] in given build_band

# Lookup
idx.claim("clm-trf3bd")                   # → Claim | None (None for framework ids)
idx.node("INVARIANT-S2")                  # → Claim | FrameworkNode | None (any node type)
```

`claim()` resolves claim ids only — it returns `None` for an invariant or axiom id. `node()` resolves any node type. The filter queries `solidity_below`, `in_band`, and `all_claims` operate on claim nodes only (framework nodes have no scoring fields); `framework_nodes` and `all_nodes` expose the framework subset and the full node set respectively.

Record types (`Claim`, `FrameworkNode`, `CitationEdge`, `StrengthenByItem`, etc.) are simple dataclasses constructed from the JSONL records on load. `claims.jsonl` is loaded as a type-tagged union: each record is dispatched on its `node_type` to a `Claim` or a `FrameworkNode`. The module favors plain Python types over heavy abstractions.

**Performance budget:** at current KB scale (~200 claim entries, ~400 leaves), full load + every-query is well under 10 ms cold; subsequent queries against the loaded in-memory structures are microseconds. No need for caching/lazy-loading at this scale.

---

## CLI surface

A thin CLI wrapper exposes the most common queries for shell use. Backed by the same `ave.kb.index` module:

```sh
ave-kb deps <claim_id>              # ids X depends on
ave-kb deps -i <claim_id>           # inverse: ids that depend on X
ave-kb gated-on <claim_id>          # claims whose strengthen-by mentions X
ave-kb cited-by <claim_id>          # leaves citing X
ave-kb solidity-below <threshold>   # claims with solidity < N
ave-kb weak-points                  # shaky AND load-bearing claims (rework targets)
ave-kb subtree <path>               # ids in subtree
ave-kb show <claim_id>              # full record for one node (claim, invariant, axiom)
ave-kb stats                        # counts summary
```

JSON output via `--json` flag for piping to `jq`.

---

## Build pipeline

```
canonical state  ──▶  refresh-kb-metadata.py  ──▶  derived state
─────────────────                            ──────────────────
frontmatter on              parse leaves                 frontmatter
indexes /                   parse claim-quality          subtree-claims
entry-point                 build index records          REWRITTEN
                                                         (existing behavior)
claim-quality.md                                         .index/*.jsonl
files                                                    WRITTEN (new)
                                                         (sorted, deterministic)
```

`refresh-kb-metadata.py` is idempotent: same canonical state → same outputs, byte-identical.

`check-claim-quality.py` (extended):
- Runs all existing checks (Tier 1 coverage — a leaf declares its content via at least one of `{claims, no-claim, exp-id}`; Tier 2, ID uniqueness, orphans, frontmatter presence, subtree consistency, bidirectional coverage, claim/no-claim exclusivity — `claims` and `no-claim` stay mutually exclusive with each other, but `exp-id` is orthogonal to both).
- runs the index build in-memory; diffs against `.index/*.jsonl` on disk; any difference is a `refresh-fixable` failure with `make refresh-kb-metadata` as the remediation hint.
- validates each JSONL file is well-formed JSON line-by-line; reports parse failures as hard failures.
- validates referential integrity (every id referenced in any non-claims file appears in claims.jsonl).
- validates leaf `experiments:` references resolve to experiment nodes (orphan / claim-id-mismatch is a hard failure, not refresh-fixable) and that declared `subtree-experiments` equals the computed owned union (refresh-fixable).
- **NEW (Push 3):** checks the claim depends-on graph is acyclic (a cycle makes solidity undefined — hard failure, not refresh-fixable).
- **NEW (Push 3):** checks solidity freshness — every claim-quality.md `solidity` line, its build-status phrase, the depends-on `(solidity X)` annotations, and the `claims.jsonl` solidity fields must equal `compute_solidity`'s output (`refresh-fixable`).
- **NEW (INVARIANT-S13):** interlock referential integrity — every `interlocks` edge's source resolves to a claim and target to an interlock-mechanism node; the `\bilk-[a-z0-9]{6}\b` id format, the `real_or_fitted` / `status` enums, the `derived_endpoint` resolution (a claim that is one of the mechanism's interlocked sources), and the `cited_leaf` file-part resolution are all enforced (hard failure; symptom of a perturbed interlock register).
- **NEW (INVARIANT-S13):** independent-parameter count freshness — the live derived count must equal the interlock register's asserted `expected-independent-count:` (hard failure on mismatch, so a chord/echo tag flip is loud).
- **NEW (INVARIANT-S13):** falsification net — no interlocked channel (a non-root `interlocks` source) may be `refuted`; if one is, the failure names the `operating-point-root:` (the model's strongest claim, CI-enforced).

---

## Design decisions (settled)

- **Where in the tree?** Settled: `.index/` under `manuscript/ave-kb/`. Grep-discoverable, tracked in git.
- **One file or several?** Settled: five files split by edge type (claims, depends-on, strengthen-by, cites, subtree-aggregates).
- **Deterministic ordering?** Settled: per-file sort key documented above.
- **Incremental or full-rebuild?** Settled v0: always full-rebuild. Revisit if rebuild time crosses a few seconds (~400 leaves currently rebuilds in well under 1 s).
- **Pre-commit vs CI freshness check?** v0: only the verifier (`make verify-kb-metadata`) checks. Pre-commit hook can be added separately when the user installs one.

---

## v0 → v0.1 candidate refinements (NOT in v0)

These were considered and deferred to keep v0 small and reviewable:

- **Embeddings / full-text search.** Out of scope for the derived index — a separate concern; layer on top if ever needed.
- **Synonym resolution.** Whether two surface forms refer to the same claim is currently encoded by id only; no aliasing.
- **History queries.** `git log .index/claims.jsonl` already provides this for free; no separate module needed.
- ~~**Solidity recomputation.**~~ *Done (Push 3).* `solidity` is now a derived field: `compute_solidity` computes `solidity = round-half-up-2dp(min(confidence, *dep_solidity))` (weakest link) over the depends-on DAG, `refresh-kb-metadata` writes it back to claim-quality.md and the JSONL, and `check-claim-quality` carries a standing freshness check (plus a depends-on graph acyclicity check).
- **Cross-claim consistency** (e.g., mutual-exclusion checks like `clm-trf3bd`/`clm-unk0bd`). Encoded informally in prose now; could become a structured `excludes` edge in v0.1.

---

## Test coverage definition of done

The verifier reports counts at every run. The numbers that define success for v0:

- `claims.jsonl` line count == code-fence-scrubbed count of `<!-- id: clm-xxxxxx -->` across all `claim-quality.md` files (i.e. excluding example placeholders inside fenced code blocks). Naive `grep -c` over-counts by the number of fenced examples; the existing verifier already strips fences. On the current KB state this number is **199**.
- `cites.jsonl` line count == sum of `len(claims)` across all leaves with `claims:` frontmatter.
- `subtree-aggregates.jsonl` line count == number of `kind: index` files + 1 (entry-point).
- Every id referenced in any non-claims `.jsonl` file appears in `claims.jsonl`.
- `make verify-kb-metadata` exits 0 after `make refresh-kb-metadata` on the current canonical state.

If those five numbers match, v0 is mechanically complete.
