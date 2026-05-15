# AVE-KB Improvements

Running list of improvements scoped specifically to the AVE-KB (canonical markdown tree at `AVE-Core/manuscript/ave-kb/`). Broader design questions about future agentic systems live elsewhere; items here are about making the existing KB better as it stands.

---

## 1. KB Leaves Are Canonical; LaTeX Is Derived

**Status as of 2026-05-07.** The relationship between the KB markdown tree (`AVE-Core/manuscript/ave-kb/`) and the LaTeX manuscript (`AVE-Core/manuscript/vol_*/`) has inverted from the original project intake.

### The shift

When the KB system was first built, the LaTeX manuscript was the canonical, pre-existing artifact inherited from the original author, and the KB was a hierarchical projection of it built for navigability and agent context. That framing made sense at the time and is the reason the build pipeline is structured as `LaTeX → extraction → KB`.

The author is now working primarily *in* the KB. The LaTeX manuscript is updated periodically to reflect KB state, not the other way around. This makes the KB the working surface and the LaTeX a derived publication artifact.

### What this means for agents

- **Treat KB leaves as canonical.** When KB and LaTeX disagree, the KB is right and the LaTeX is stale (modulo unverified-but-load-bearing claim-quality entries, which still gate on dependency analysis regardless of representation).
- **Edits flow KB → LaTeX, not LaTeX → KB.** When updating a result or correcting a derivation, write the KB leaf first, propagate to the relevant indexes (frontmatter `claims:`, Tier 2 inline markers, subtree-claims aggregation), then update the LaTeX as a downstream sync step if the LaTeX is currently in scope.
- **Do not treat LaTeX silence as authority.** If a KB leaf documents a result that the LaTeX does not yet reflect, the result still stands. Conversely, a LaTeX section that contradicts a current KB leaf should be read as obsolete prose pending sync.
- **Corrigenda live in the KB.** When superseding prior framing (e.g., the 2026-05-06 neutrino screw-dislocation corrigendum), the canonical record is the KB index/leaf. The LaTeX should mirror it, but the KB is the source of truth.

### What this does *not* change

- Source-document fidelity for *historical* extraction work — i.e., when distilling a not-yet-touched LaTeX section into a new KB leaf for the first time, the LaTeX is still the input. The inversion applies once a region of the KB has been authored or revised in-place.
- The verifier-driven discipline around claim-quality propagation, INVARIANT-S5/S8, and subtree aggregation. Those structural rules apply to the KB regardless of where canonicity sits.
- The need to keep LaTeX in sync for publication. It is derived, but it is not optional.

### Open follow-ups

- Update `CLAUDE.md` and any `kb-*` agent definitions that currently describe the LaTeX as canonical.
- Decide whether to add a verifier step that flags KB-vs-LaTeX divergence as a derivation-staleness signal rather than a KB-error signal.

---

## 2. First-Class Derived Index for Graph Queries

**Status as of 2026-05-07. Proposed.**

### The friction

Several common navigation patterns currently fall back to `grep` or full-tree scans:

- "What depends on claim `0ktpcn`?"
- "Which leaves in this subtree have solidity below 0.7?"
- "Where is this claim's strengthen-by item being worked on?"
- "What cites the Cosserat sector definition?"
- "Which claims are gated on this leaf's strengthen-by completing?"

These are graph traversals, not filesystem operations. Each invocation linearly scans + parses N markdown files; for an agent, the cost is paid out of the working context budget every time. That, not disk latency, is the actual navigation-velocity ceiling for the KB.

### The pattern

Canonical source on the left, derived index on the right:

| Canonical (human-editable) | Derived (machine-queryable, text + git) |
|---|---|
| markdown leaves with `kb-frontmatter` | claim graph, dependency edges, solidity scores, inverse edges, materialized as JSONL files in `.index/` and committed to git |

The same pattern works for git itself (loose objects → packfiles), Lean (`.lean` → `.olean`), search engines (documents → inverted index), WAL databases (log → B-trees), and lockfiles (manifest → `package-lock.json` / `Cargo.lock` / `poetry.lock`). The KB already has the seedling: `make refresh-kb-metadata` and the verifier transiently parse frontmatter and reason about the claim graph; that work just isn't persisted as a queryable artifact.

The frontmatter discipline this requires is already in place. The fields the index would consume — `claims`, `subtree-claims`, claim-quality entries with `depends-on` and `strengthen-by`, supersedes / superseded-by edges from corrigenda, the Tier 2 inline marker positions — are exactly what INVARIANT-S5 and INVARIANT-S8 already require.

### What the index should hold

At minimum:

- **Claim records**: `claim_id`, `leaf_path`, claim-quality tier, current solidity bound, rationale source, supersedes / superseded-by status.
- **Dependency edges**: `depends-on`, `strengthen-by`, `supersedes` / `superseded-by`. Forward edges from each claim-quality entry, materialized.
- **Subtree-claim aggregation**: precomputed per index-node, kept in sync at index-build time rather than recomputed on every traversal. (Currently the verifier already computes this; the index would persist it.)
- **Inverse edges**: "leaves that cite claim X", "claims gated on this leaf's strengthen-by completing", "leaves whose solidity bound depends on this claim". These are the queries the markdown can't answer cheaply today.
- **Position metadata**: file path, line number of inline Tier 2 markers, frontmatter field locations — so the index can answer "where exactly does this assertion live" without a re-scan.

### Implementation sketch

- **Storage**: JSONL files under `ave-kb/.index/` — one record per line, sorted deterministically (e.g. by `claim_id`) so git diffs stay legible. Concrete starting set: `claims.jsonl` (claim records), `depends-on.jsonl` (forward dependency edges), `strengthen-by.jsonl` (open work edges), `subtree-aggregates.jsonl` (precomputed per-index aggregations), `cites.jsonl` (inverse edges, leaves → claim IDs). All committed to git. Text + line-oriented = `grep`, `git grep`, `jq`, `cut`, `awk`, `git diff` all work natively. Inspectability and recoverability are inherited from the substrate, not added on top.
- **History via git**: because the index is committed text, `git log .index/claims.jsonl` is the history of the claim graph; `git diff` between two commits shows exactly which claims and edges changed; `git blame` answers "when did this claim's solidity bound change and why" by pointing to the commit + message; `git checkout <commit> -- .index/` restores any prior graph state. Branching gives what-if exploration of claim-graph restructuring for free.
- **Build**: extend `make refresh-kb-metadata` to also (re)build the index files. Build must be deterministic — same inputs produce byte-identical outputs — so freshness can be checked by re-running the build and diffing.
- **Freshness enforcement**: pre-commit hook (or CI step) regenerates the index and fails if the working tree diverges from the regenerated state. Same pattern lockfiles use; structurally prevents drift between leaves and index. If the index is committed and clean, it is authoritative for the commit.
- **Query surface**: a thin Python module (e.g. `ave.kb.index`), **stdlib only — no pip dependencies**, loads the JSONL files into memory once per process and exposes functions for the canonical question shapes — `depends_on(claim_id)`, `dependents_of(claim_id)`, `subtree_claims(path)`, `solidity_below(threshold)`, `cited_by(claim_id)`, `gated_on(claim_id)`. Agents call these instead of grepping; the load + dict-lookup is microseconds at current scale. For ad-hoc shell work, `jq` over the JSONL files is the second query path. CLI wrappers (`ave-kb deps 0ktpcn`, `ave-kb gated-on 0ktpcn`, `ave-kb solidity-below 0.7`) keep parity with the shell-tool inspection model the rest of the KB lives in. Stdlib coverage (`json`, `re`, `pathlib`, `argparse`) is sufficient for everything this module needs; avoiding pip dependencies keeps the KB tooling blast-radius-free and long-lived.
- **Schema enforcement**: the index builder doubles as a structural verifier. Frontmatter that doesn't match the schema fails the build, surfacing drift at edit-time rather than letting it accumulate. Strict superset of what the current verifier catches.
- **Reversibility**: the storage choice is reversible. If scale ever forces a move to SQLite (or anything else), the `ave.kb.index` API can be reimplemented behind the same function signatures without changing callers. Storage substrate is an implementation detail; the query API is the contract.

### Non-goals

- **Replacing markdown as the canonical store.** The index is rebuilt-from-source at all times. If the index disagrees with the markdown, the markdown wins and the index is rebuilt. Inspectability and recoverability with shell tools are preserved by construction.
- **Full-text search.** Separate concern. If needed, layer on top.
- **Multi-author conflict resolution.** With single-author + agents, the index is always derivable from the current markdown state. Multi-author would add "stale index" as a real concern; price that in if/when it happens.

### Why this is worth doing regardless of any future agentic system

The AVE-KB's current navigation friction is a real cost paid daily. The index layer is small, additive, and removable — worst case it's wasted effort, best case it raises the working-velocity ceiling of every future session by a meaningful factor. The frontmatter discipline it requires is already in place; this is harvest, not new planting.

It also surfaces a class of staleness the current verifier doesn't catch — e.g., a strengthen-by item whose dependency just got resolved, or a subtree-claims aggregation that should have included a newly-added claim. Those become standing queries against the index rather than ad-hoc audit passes.

### Open questions

- **Where in the tree?** `.index/` under `ave-kb/` keeps it adjacent to canonical content and grep-discoverable. *Tracked* in git, not gitignored — the whole point is to get free history and diffs.
- **One file or several?** Probably several JSONL files split by edge type (`claims`, `depends-on`, `strengthen-by`, `cites`, `subtree-aggregates`). Cleaner diffs, smaller diff blast radius per change, easier `jq` pipelines. Single combined file is simpler but loses the line-grain.
- **Deterministic ordering policy?** Sort by `claim_id` alphabetically. Makes diffs stable: a new claim shows up as one inserted line, never reorders the rest. Document this as a build invariant; verifier can check it.
- **Do we go incremental or always full-rebuild?** Full-rebuild is simpler and almost certainly fast enough at current KB size (~400 leaves). Revisit if rebuild time crosses a few seconds.
- **Pre-commit vs. CI for freshness check?** Pre-commit gives immediate feedback but can be skipped (`--no-verify`). CI is harder to skip but lags. Probably both — pre-commit warns, CI enforces.
