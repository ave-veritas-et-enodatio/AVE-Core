# Corpus Map + Rule-12 Narrowing — DEFERRED (Grant 2026-06-18: table for a later session)

**Status: DEFERRED.** Captured here so the effort is recoverable; not chartered/run yet. Full framing in the 2026-06-18 conversation.

**Problem:** too much "removed"/superseded content preserved INLINE in KB + manuscript (over-applied Rule-12) + a growing pile of open `_orchestration/` and `research/` docs. The live working theory is cluttered with the graveyard of past efforts.

**Direction (Grant):** git history IS the audit trail — use it. Keep the live corpus = current theory, clean. Have ONE thin "map" to find any past effort by its location in history, instead of carrying it inline.

**Proposed model:**
- Live corpus = current state, no graveyard.
- Git = the complete record (every version/diff/date/author/message).
- ONE thin, git-native map: lean on tags (e.g. `effort/<name>`) + PR titles + commit messages as the machine-readable index; a thin curated top-layer points at SHAs. CONSOLIDATE the existing partial registries (`claim-quality-closure-roadmap.md §0.5`, `divergence-test-substrate-map.md`, `LIVING_REFERENCE.md`, the promotions-tracker) — do NOT add a 5th.
- Rule-12 NARROWS to its real job.

**Constraints (the challenge — do not skip):**
1. Load-bearing inline preservation that CANNOT move to git: demotion banners on *falsified claims still cited* (a reader following a `\kbleaf` won't check git history) + amendments to *frozen / SHA-pinned preregs*. Migration is surgical; sort key = "would a reader be misled," NOT "is it old."
2. PRECONDITION: git only preserves what's COMMITTED. The untracked `_orchestration/` scratch + `reconciliation-handoffs/` (26 files incl. the DEC-01 adjudication that def-nodes cite) must be committed FIRST, or they vanish with no map entry.
3. The map must be low-maintenance (git-native, thin) or it rots into new clutter.

**Open policy decision (Grant ratify — amends Rule-12):** narrow inline-preservation to {cited-falsified claims, frozen-prereg amendments}; everything else (our own superseded editorial framing, closed exploratory arcs, done orchestration/research docs) → git history + the one map. Per [[feedback_dont_ceremonialize_revising_own_output]] this is the corpus-scale extension of that lesson.

**Session shape (when un-tabled):** challenge/ratify-policy → map design (consolidate registries + adopt tags) → surgical migration (commit untracked first → sweep inline-clutter → archive closed orch/research docs).
