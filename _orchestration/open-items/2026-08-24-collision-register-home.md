---
id: collision-register-home
title: "Symbol collisions have two competing homes (theorem-thesaurus §6 rows, ungated; vocabulary-register def-nodes, CI-gated) — pick one before the next batch lands"
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-24
source: manuscript/ave-kb/common/theorem-thesaurus.md
anchor: "## §6 — ★The homonym watch-list"
---

Methodology question surfaced by the 2026-08-24 symbol-collision sweep, which found the
corpus routing this class of finding two different ways with no rule:

- **`theorem-thesaurus.md` §6 homonym watch-list** — carries symbol rows (e.g. $Q$,
  $I_{max}$); prose, not machine-gated.
- **`vocabulary-register.md` `def-` nodes** — CI-gated via the metadata verifier
  (`open_ambiguity`, `conflicting_sites`), and therefore the home that cannot silently rot.
- **Ad-hoc inline warnings** — INVARIANT-N4 ($S_{11}$), the δ_CP caveat at clm-4vwsjc, the
  ELL_C block in `constants.py`. These are the ones that have gone stale (N4 still cites a
  volume tree that no longer exists).

**Why it needs deciding now:** one arc surfaced four-plus collisions in two days, and each
was filed wherever the finding happened to land. Without a standing home rule the register
fragments and the ungated copies drift.

**Orchestrator recommendation (not a ruling):** `def-` nodes as the single gated home, with
§6 keeping pointer rows only. **Grant's call.**

Dependent items awaiting this routing: `a0-glyph-collision`,
`gammac-gc-modulus-identity`, `axiom5-b-glyph`, `kernel-argument-normalization`.
