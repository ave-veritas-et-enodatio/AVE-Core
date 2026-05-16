# AVE-KB Derived Index — Schema Specification

**Status:** Live — built and hardened (clm- IDs, framework nodes, derived solidity, NaN-propagation). Last revised 2026-05-16.
**Scope:** specifies the canonical JSONL files that live under this directory, the record shapes within each, the build invariants, and the query semantics the runtime module (`src/ave/kb/index.py`) is expected to provide over them.

This directory is **derived** from canonical sources:
- Leaf frontmatter (`claims:`, `subtree-claims:`, `kind:`, `path-stable`, `no-claim`) in every KB `.md` file outside `session/`.
- Tier 2 inline markers (`<!-- claim-quality: <id> ... -->`) in multi-claim leaves.
- Claim-quality entries in every `claim-quality.md` register (root, per-volume, common).

Every file here is regeneratable from those canonical sources via `make refresh-kb-metadata`. If any file here disagrees with what regeneration would produce, the canonical sources win and the file is rebuilt. The freshness verifier (`make verify-kb-metadata`) runs the build in dry-run and diffs against on-disk; non-empty diff = stale index = hard failure.

---

## File inventory

| File | Records | Sort key | Purpose |
|---|---|---|---|
| `claims.jsonl` | one per graph node (claim / invariant / axiom) | `(node_type, id)` | Canonical graph nodes — claims plus framework nodes |
| `depends-on.jsonl` | one per forward dependency edge | `(source, target, context)` | "What does X depend on?" / "What depends on Y?" |
| `strengthen-by.jsonl` | one per open work item | `(claim_id, item_idx)` | "What gates this claim?" / "Where is this strengthen-by item being worked on?" |
| `cites.jsonl` | one per (claim, leaf) citation edge | `(claim_id, leaf_path)` | "Which leaves cite claim X?" (inverse of leaf frontmatter) |
| `subtree-aggregates.jsonl` | one per index / entry-point node | `node_path` | Precomputed subtree-claims aggregation |

All files are JSONL — one JSON object per line, no trailing whitespace, single trailing newline at EOF. Keys appear in fixed order per record type (specified below) so byte-identical regeneration is guaranteed.

---

## Build invariants

These hold across every regeneration. They are checked by `personant verify`-style operations (`make verify-kb-metadata` extended):

1. **Determinism.** Running `make refresh-kb-metadata` against the same canonical state yields byte-identical files. No timestamps, no random IDs, no environment-dependent paths embedded in records.
2. **Sort stability.** Each file's records are sorted by the file's sort key. A new claim or edge appears as one inserted line in `git diff`, never reorders surrounding lines.
3. **Schema closure.** Every record matches the schema in this document. Unknown fields are a hard verifier failure (catches drift between schema and emitter).
4. **Referential integrity.** Every ID referenced in `depends-on.jsonl`, `strengthen-by.jsonl`, `cites.jsonl`, or `subtree-aggregates.jsonl` resolves to a record in `claims.jsonl` — which holds claim **and** framework nodes. A `depends-on` edge's `target` may resolve to any node type, and its `target_kind` must equal the resolved record's `node_type` (kind-match). `strengthen-by` / `cites` `claim_id` and `subtree-aggregates` `subtree_claims` reference claim ids only. (Orphan or kind-mismatch is a verifier failure.)
5. **Single newline EOF.** Every file ends with exactly one `\n`. (Catches editor mishaps and trailing-whitespace creep.)
6. **JSON valid.** Every line parses as a JSON object. (Catches partial writes and merge corruption.)

---

## Record schemas

All field types are JSON types: `string`, `number` (float), `integer`, `boolean`, `null`, `array`, `object`. Solidity / confidence values are floats in [0, 1]. Paths are POSIX-style (forward slashes), relative to `manuscript/ave-kb/`.

### `claims.jsonl`

Despite the name, `claims.jsonl` holds **three node types** — a type-tagged union discriminated by the `node_type` field (`claim` | `invariant` | `axiom`). Claim nodes are one per `<!-- id: clm-xxxxxx -->` canonical entry across all `claim-quality.md` files; framework nodes (invariants + axioms) are parsed from `manuscript/ave-kb/CLAUDE.md`. The file is **not** split — all node types share one file so a single referential-integrity pass spans the whole graph.

**Claim record** (`node_type: "claim"`) — `node_type` is the new FIRST field; the 12 pre-existing fields are unchanged. 13 fields total.

```typescript
{
  node_type: "claim",            // discriminator — always "claim" here
  id: string,                    // clm-[a-z0-9]{6}; primary key
  title: string,                 // text from the ## heading containing this id
  canonical_path: string,        // e.g. "vol1/claim-quality.md"
  canonical_anchor: string,      // GitHub-style anchor for the heading
  confidence: number,            // 0.0 .. 1.0; hand-authored, from Quality section
  solidity: number,              // 0.0 .. 1.0; DERIVED by compute_solidity (null if confidence unset)
  build_status: string,          // DERIVED phrase from solidity band, e.g. "ok to build on" (null if solidity null)
  build_band: string,            // DERIVED from solidity: ok-to-build, ok-with-caveats, input-only, do-not-build, refuted
  rationale: string,             // text after "rationale:" — preserved as single line (LF → ' ')
  depends_on_count: integer,     // count of edges in depends-on.jsonl with source == this id
  strengthen_by_count: integer,  // count of items in strengthen-by.jsonl with claim_id == this id
  citation_count: integer        // count of edges in cites.jsonl with claim_id == this id
}
```

Claim field order: `node_type`, `id`, `title`, `canonical_path`, `canonical_anchor`, `confidence`, `solidity`, `build_status`, `build_band`, `rationale`, `depends_on_count`, `strengthen_by_count`, `citation_count`.

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

**Sort key.** Records are sorted by `(node_type, id)` — explicit grouping by ASCII order of the discriminator: axioms, then claims, then invariants.

**`build_band` derivation** (mechanical, from solidity):

| Solidity range | `build_band` value |
|---|---|
| 0.85 ≤ s ≤ 1.00 | `ok-to-build` |
| 0.65 ≤ s < 0.85 | `ok-with-caveats` |
| 0.45 ≤ s < 0.65 | `input-only` |
| 0.20 ≤ s < 0.45 | `do-not-build` |
| 0.00 ≤ s < 0.20 | `refuted` |

This mirrors the build-status legend in the root `claim-quality.md` and provides a machine-stable enum for filtering even if the human-readable `build_status` phrasing drifts.

**Solidity is derived, not parsed.** `solidity`, `build_status`, and `build_band` are NOT read from the claim-quality.md `solidity` line — they are computed by `kb_index_lib.compute_solidity` from the hand-authored `confidence` values and the depends-on DAG (`solidity = round-half-up-2dp(confidence × min(dependency solidities))`; framework-target dependencies contribute 1.0). The claim-quality.md `solidity` line is itself a write-back of the same computation (`make refresh-kb-metadata`). The freshness verifier hard-fails if the on-disk claim-quality.md solidity content or these JSONL fields disagree with the recomputed values.

**HARD RULE — `*pending*` propagates transitively (NaN semantics).** A claim's solidity is `*pending*` (uncomputable) if its `confidence` is `*pending*` (not yet quality-assessed) **OR** any of its dependencies' solidity is `*pending*` — **regardless of the claim's own local `confidence`**. A claim with `confidence: 1.0` that depends on one pending claim still has solidity `*pending*`. Pending-ness propagates through the depends-on DAG exactly like NaN through arithmetic. Framework-node dependencies (invariant / axiom targets) are **never** pending — they are solidity-1.0 bedrock by definition, so a claim depending only on framework nodes is not pending (its solidity equals its confidence). A claim with a pending solidity carries `null` for `solidity`, `build_status`, and `build_band` in `claims.jsonl`, the bare `- solidity: *pending*` line in claim-quality.md, and `(solidity *pending*)` wherever it is a depends-on target. Every consumer treats "absent from `compute_solidity`'s result" identically to "pending".

**Rationale-text normalization:** preserve text verbatim except for collapsing internal line breaks to single spaces (so rationale is one-line JSON-safe). Inline markdown (backticks, asterisks) is preserved.

### `depends-on.jsonl`

One record per forward dependency edge. A `source` is always a claim id. A `target` may be a claim id **or** a framework node id (invariant / axiom) — `target_kind` discriminates.

```typescript
{
  source: string,                          // claim id (depender)
  target: string,                          // dependee node id (claim / invariant / axiom)
  target_kind: "claim" | "invariant" | "axiom",  // node type of the target
  target_solidity_recorded: number | null, // solidity as written in the line; null for framework targets
  context: string | null                   // optional context note from the depends-on line
}
```

Field order: `source`, `target`, `target_kind`, `target_solidity_recorded`, `context`.

**Bullet-head extraction.** A depends-on bullet's dependency target(s) live in its *head*, not its title/context. The head is the bullet text after the leading `- `, truncated at the EARLIER of: the first ` — ` (em-dash title separator) or the first ` (` (paren). The head is scanned for ALL recognized target tokens, emitting **one edge per token**:

- `\bclm-[a-z0-9]{6}\b` → `target_kind: "claim"`; `target_solidity_recorded` parsed from a `(solidity <num>)` group; `context` from a trailing `[...]` group (an `[= ...]` arithmetic annotation is skipped).
- `\bINVARIANT-[A-Z]+[0-9]+\b` → `target_kind: "invariant"`, `target` the label verbatim, `target_solidity_recorded: null`; `context` from the bullet's first `(...)` paren content.
- `\bAxiom [1-4]\b` → `target_kind: "axiom"`, `target` normalized to `axiom-N` lowercase, `target_solidity_recorded: null`; `context` from the first `(...)` paren content.

A normal claim bullet `- clm-unk0bd — Title (solidity 0.4)` has head `clm-unk0bd` → one claim edge. A framework bullet `- INVARIANT-S2 / Axiom 4 (saturation kernel — ...)` has head `INVARIANT-S2 / Axiom 4` → two edges (invariant + axiom), both carrying the paren content as context.

**Non-edges:** Quality sections may contain a placeholder line like `- *(none entry-local — ...)*`. These are recognized by the leading asterisk + italic marker and produce zero edges. A bullet whose head contains no recognized token also produces zero edges — e.g. `- none entry-local — Axiom 4 is framework input...` has head `none entry-local`; the `Axiom 4` after the em-dash is explanatory text, not a target, and is not scanned.

**Sort key.** `(source, target, context)` — a null context sorts as the empty string. The context component keeps two edges from the same source to the same target (e.g. an `INVARIANT-S2` dependency declared in two separate bullets with different context notes) deterministically ordered.

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
  subtree_claims: string[]      // sorted unique list of all claim ids under this node's subtree
}
```

Field order: `node_path`, `node_kind`, `subtree_claims`.

This file persists what `refresh-kb-metadata` already computes transiently for the frontmatter `subtree-claims:` field. Having it materialized as JSONL means cross-volume aggregation queries don't require re-walking the tree.

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
- Runs all existing checks (Tier 1, Tier 2, ID uniqueness, orphans, frontmatter presence, subtree consistency, bidirectional coverage, claim/no-claim exclusivity).
- runs the index build in-memory; diffs against `.index/*.jsonl` on disk; any difference is a `refresh-fixable` failure with `make refresh-kb-metadata` as the remediation hint.
- validates each JSONL file is well-formed JSON line-by-line; reports parse failures as hard failures.
- validates referential integrity (every id referenced in any non-claims file appears in claims.jsonl).
- **NEW (Push 3):** checks the claim depends-on graph is acyclic (a cycle makes solidity undefined — hard failure, not refresh-fixable).
- **NEW (Push 3):** checks solidity freshness — every claim-quality.md `solidity` line, its build-status phrase, the depends-on `(solidity X)` annotations, and the `claims.jsonl` solidity fields must equal `compute_solidity`'s output (`refresh-fixable`).

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
- ~~**Solidity recomputation.**~~ *Done (Push 3).* `solidity` is now a derived field: `compute_solidity` computes `solidity = round-half-up-2dp(confidence × min(dep_solidity))` over the depends-on DAG, `refresh-kb-metadata` writes it back to claim-quality.md and the JSONL, and `check-claim-quality` carries a standing freshness check (plus a depends-on graph acyclicity check).
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
