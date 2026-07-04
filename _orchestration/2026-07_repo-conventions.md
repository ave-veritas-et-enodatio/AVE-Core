# Repo Formatting & Cleanup Conventions — PROPOSED (P0 deliverable)

**Status:** PROPOSED — awaiting Grant ratification (owner: P0 implementor, drafted 2026-07-04). Last-verified HEAD: `43d53e06`.
**Scope class:** ORGANIZATION AND FORMATTING ONLY — this document proposes conventions; it executes no move, rename, archive, or fix. Every execution phase is gated on Grant ratifying the relevant **RATIFY:** block below.
**Merge discipline:** lands via a reviewed PR (`[REVIEW: pending-orchestrator]`), no self-merge, per CLAUDE.md branching pattern.

> **What this doc is NOT.** It is not a physics adjudication, not a claim-id-spine change, not a KB-frontmatter change. The claim-id spine (`clm-`/`exp-`/`sup-`/`def-`/`ilk-`, INVARIANT-S8..S13) and solidity machinery are healthy + CI-enforced and OUT OF SCOPE. Nothing here touches content — only where files live, how they are named, and how their status is marked.

## How to read the RATIFY blocks

Each section (a)–(f) ends in a **RATIFY:** block written as inline prose. Where a real choice exists, options are bulleted and a recommended default is marked **[RECOMMENDED]**. Grant adjudicates in prose (no multi-choice UI). Until a block is ratified, the section is a proposal with no executable force.

## Cross-cutting invariants (apply to every section)

1. **Organization/formatting only — never content deletion.** No section may propose deleting or gutting a doc's content.
2. **Honesty-trail docs are UNTOUCHABLE.** RETRACTED / walk-back / correction records and frozen preregs of live claims are never archived away from a live claim, never rewritten, never banner-stamped. (Restated in full in section (b).)
3. **Git history is the audit trail.** No convention may introduce in-doc preservation banners. Corrections land append-only (the pattern codified in section (c)).
4. **Every move is link-coupled.** Any file move executes as move + citation update in the SAME commit, with `make verify-md-links` + `make verify-kb-metadata` green in that commit. (HEAD numbers in section (b).)
5. **Pure-AVE-corpus rule.** Every tracked file, commit message, and branch name stays pure physics/process — no external/non-physics context.

---

## (a) Figure placement

_(section body lands in commit 2)_

---

## (b) `research/` naming + organization grammar

_(section body lands in commit 3)_

---

## (c) `_orchestration/` lifecycle + currency rule

_(section body lands in commit 4)_

---

## (d) Branch lifecycle SLA

_(section body lands in commit 5)_

---

## (e) Status-marker grammar (lintable)

_(section body lands in commit 6)_

---

## (f) Badge / manifest accounting rule

_(section body lands in commit 7)_

---

## RATIFY decision list (rollup)

_(populated as sections land; each entry links to its section's RATIFY block)_

---

## Appendix — verified-input ledger (HEAD `43d53e06`, 2026-07-04)

_(populated as sections land; every `file:line` here is grep-verified at this doc's HEAD)_
