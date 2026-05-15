# AVE-KB Derived Index — Schema Specification

**Status:** v0 — initial design, 2026-05-15.
**Proposal source:** [`session/kb-improvements.md`](../session/kb-improvements.md) §2.
**Scope:** specifies the canonical JSONL files that live under this directory, the record shapes within each, the build invariants, and the query semantics the runtime module (`src/ave/kb/index.py`) is expected to provide over them.

This directory is **derived** from canonical sources:
- Leaf frontmatter (`claims:`, `subtree-claims:`, `kind:`, `path-stable`, `no-claim`) in every KB `.md` file outside `session/`.
- Tier 2 inline markers (`<!-- claim-quality: <id> ... -->`) in multi-claim leaves.
- Claim-quality entries in every `claim-quality.md` register (root, per-volume, common).

Every file here is regeneratable from those canonical sources via `make refresh-kb-metadata`. If any file here disagrees with what regeneration would produce, the canonical sources win and the file is rebuilt. The freshness verifier (`make verify-claim-quality`) runs the build in dry-run and diffs against on-disk; non-empty diff = stale index = hard failure.

---

## File inventory

| File | Records | Sort key | Purpose |
|---|---|---|---|
| `claims.jsonl` | one per claim-quality entry | `id` | Canonical claim graph nodes with metadata |
| `depends-on.jsonl` | one per forward dependency edge | `(source, target)` | "What does X depend on?" / "What depends on Y?" |
| `strengthen-by.jsonl` | one per open work item | `(claim_id, item_idx)` | "What gates this claim?" / "Where is this strengthen-by item being worked on?" |
| `cites.jsonl` | one per (claim, leaf) citation edge | `(claim_id, leaf_path)` | "Which leaves cite claim X?" (inverse of leaf frontmatter) |
| `subtree-aggregates.jsonl` | one per index / entry-point node | `node_path` | Precomputed subtree-claims aggregation |

All files are JSONL — one JSON object per line, no trailing whitespace, single trailing newline at EOF. Keys appear in fixed order per record type (specified below) so byte-identical regeneration is guaranteed.

---

## Build invariants

These hold across every regeneration. They are checked by `personant verify`-style operations (`make verify-claim-quality` extended):

1. **Determinism.** Running `make refresh-kb-metadata` against the same canonical state yields byte-identical files. No timestamps, no random IDs, no environment-dependent paths embedded in records.
2. **Sort stability.** Each file's records are sorted by the file's sort key. A new claim or edge appears as one inserted line in `git diff`, never reorders surrounding lines.
3. **Schema closure.** Every record matches the schema in this document. Unknown fields are a hard verifier failure (catches drift between schema and emitter).
4. **Referential integrity.** Every claim ID referenced in `depends-on.jsonl`, `strengthen-by.jsonl`, `cites.jsonl`, or `subtree-aggregates.jsonl` exists as a record in `claims.jsonl`. (Orphan check is a verifier failure.)
5. **Single newline EOF.** Every file ends with exactly one `\n`. (Catches editor mishaps and trailing-whitespace creep.)
6. **JSON valid.** Every line parses as a JSON object. (Catches partial writes and merge corruption.)

---

## Record schemas

All field types are JSON types: `string`, `number` (float), `integer`, `boolean`, `null`, `array`, `object`. Solidity / confidence values are floats in [0, 1]. Paths are POSIX-style (forward slashes), relative to `manuscript/ave-kb/`.

### `claims.jsonl`

One record per `<!-- id: xxxxxx -->` canonical entry across all `claim-quality.md` files.

```typescript
{
  id: string,                    // 6-char [a-z0-9]; primary key
  title: string,                 // text from the ## heading containing this id
  canonical_path: string,        // e.g. "vol1/claim-quality.md"
  canonical_anchor: string,      // GitHub-style anchor for the heading
  confidence: number,            // 0.0 .. 1.0; from Quality section
  solidity: number,              // 0.0 .. 1.0; from Quality section
  build_status: string,          // parenthetical phrase after solidity, e.g. "ok to build on"
  build_band: string,            // one of: ok-to-build, ok-with-caveats, input-only, do-not-build, refuted
  rationale: string,             // text after "rationale:" — preserved as single line (LF → ' ')
  depends_on_count: integer,     // count of edges in depends-on.jsonl with source == this id
  strengthen_by_count: integer,  // count of items in strengthen-by.jsonl with claim_id == this id
  citation_count: integer        // count of edges in cites.jsonl with claim_id == this id
}
```

Field order in emitted JSON: `id`, `title`, `canonical_path`, `canonical_anchor`, `confidence`, `solidity`, `build_status`, `build_band`, `rationale`, `depends_on_count`, `strengthen_by_count`, `citation_count`.

**`build_band` derivation** (mechanical, from solidity):

| Solidity range | `build_band` value |
|---|---|
| 0.85 ≤ s ≤ 1.00 | `ok-to-build` |
| 0.65 ≤ s < 0.85 | `ok-with-caveats` |
| 0.45 ≤ s < 0.65 | `input-only` |
| 0.20 ≤ s < 0.45 | `do-not-build` |
| 0.00 ≤ s < 0.20 | `refuted` |

This mirrors the build-status legend in the root `claim-quality.md` and provides a machine-stable enum for filtering even if the human-readable `build_status` phrasing drifts.

**Rationale-text normalization:** preserve text verbatim except for collapsing internal line breaks to single spaces (so rationale is one-line JSON-safe). Inline markdown (backticks, asterisks) is preserved.

### `depends-on.jsonl`

One record per forward dependency edge. An entry's Quality `depends-on:` list with non-placeholder entries produces one edge per listed claim ID.

```typescript
{
  source: string,                          // claim id (depender)
  target: string,                          // claim id (dependee)
  target_solidity_recorded: number | null, // solidity value as written in the depends-on line, or null
  context: string | null                   // optional bracketed/parenthesized context note from depends-on line
}
```

Field order: `source`, `target`, `target_solidity_recorded`, `context`.

**Non-edges:** Quality sections may contain a placeholder line like `- *(none entry-local — ...)*`. These are recognized by the leading asterisk + italic marker and produce zero edges (not a record with `target: null`).

**Context extraction:** the depends-on line format is roughly:
```
- <id> — <Title> (solidity <num>) [<optional context>]
```
The bracketed `[<context>]` (if present) is captured into `context`; the title text is for human readability and not separately captured (it's available in `claims.jsonl` via the target id).

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

**`mentioned_ids` extraction:** match the standard 6-char [a-z0-9] pattern in `text`, but exclude false positives by requiring word-boundary context. IDs that don't match any record in `claims.jsonl` are still emitted (the verifier flags orphan-style consistency issues globally).

### `cites.jsonl`

One record per (claim, leaf) citation edge. A leaf's frontmatter `claims: [a, b, c]` produces three edges.

```typescript
{
  claim_id: string,         // 6-char id
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

# Forward dependency edges
idx.depends_on("0ktpcn")              # → list[str] of target claim ids
idx.dependents_of("unk0bd")           # → list[str] of source claim ids (inverse)

# Open work
idx.strengthen_by("trf3bd")           # → list[StrengthenByItem]
idx.gated_on("unk0bd")                # → list[str] of claim_ids whose strengthen-by mentions "unk0bd"

# Citation / leaf membership
idx.cited_by("0ktpcn")                # → list[CitationEdge] (leaves citing this claim)
idx.claims_in_leaf("vol1/ch8-...")    # → list[str] of claim ids cited by that leaf

# Subtree aggregation
idx.subtree_claims("vol1")            # → list[str] of all claim ids under vol1/
idx.subtree_claims("")                # → list[str] (whole tree; same as entry-point's aggregate)

# Filters
idx.solidity_below(0.7)               # → list[Claim] with solidity < threshold
idx.in_band("do-not-build")           # → list[Claim] in given build_band

# Lookup
idx.claim("trf3bd")                   # → Claim | None
```

Record types (`Claim`, `CitationEdge`, `StrengthenByItem`, etc.) are simple dataclasses (or NamedTuples) constructed from the JSONL records on load. The module favors plain Python types over heavy abstractions.

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
ave-kb subtree <path>               # ids in subtree
ave-kb show <claim_id>              # full record for one claim
ave-kb verify                       # run freshness check (delegates to check-claim-quality)
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
- **NEW:** runs the index build in-memory; diffs against `.index/*.jsonl` on disk; any difference is a `refresh-fixable` failure with `make refresh-kb-metadata` as the remediation hint.
- **NEW:** validates each JSONL file is well-formed JSON line-by-line; reports parse failures as hard failures.
- **NEW:** validates referential integrity (every id referenced in any non-claims file appears in claims.jsonl).

---

## Open questions (carried from `session/kb-improvements.md` §2)

- **Where in the tree?** Settled: `.index/` under `manuscript/ave-kb/`. Grep-discoverable, tracked in git.
- **One file or several?** Settled: five files split by edge type (claims, depends-on, strengthen-by, cites, subtree-aggregates).
- **Deterministic ordering?** Settled: per-file sort key documented above.
- **Incremental or full-rebuild?** Settled v0: always full-rebuild. Revisit if rebuild time crosses a few seconds (~400 leaves currently rebuilds in well under 1 s).
- **Pre-commit vs CI freshness check?** v0: only the verifier (`make verify-claim-quality`) checks. Pre-commit hook can be added separately when the user installs one.

---

## v0 → v0.1 candidate refinements (NOT in v0)

These were considered and deferred to keep v0 small and reviewable:

- **Embeddings / full-text search.** Out of scope per kb-improvements.md §2 ("Separate concern. If needed, layer on top.").
- **Synonym resolution.** Whether two surface forms refer to the same claim is currently encoded by id only; no aliasing.
- **History queries.** `git log .index/claims.jsonl` already provides this for free; no separate module needed.
- **Solidity recomputation.** v0 records solidity as written in claim-quality.md. Recomputing `solidity = confidence × min(dep_solidity)` and flagging drift is a verifier extension for v0.1.
- **Cross-claim consistency** (e.g., mutual-exclusion checks like `trf3bd`/`unk0bd`). Encoded informally in prose now; could become a structured `excludes` edge in v0.1.

---

## Test coverage definition of done

The verifier reports counts at every run. The numbers that define success for v0:

- `claims.jsonl` line count == code-fence-scrubbed count of `<!-- id: xxxxxx -->` across all `claim-quality.md` files (i.e. excluding example placeholders inside fenced code blocks). Naive `grep -c` over-counts by the number of fenced examples; the existing verifier already strips fences. On the current KB state this number is **199**.
- `cites.jsonl` line count == sum of `len(claims)` across all leaves with `claims:` frontmatter.
- `subtree-aggregates.jsonl` line count == number of `kind: index` files + 1 (entry-point).
- Every id referenced in any non-claims `.jsonl` file appears in `claims.jsonl`.
- `make verify-claim-quality` exits 0 after `make refresh-kb-metadata` on the current canonical state.

If those five numbers match, v0 is mechanically complete.
