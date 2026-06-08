# 2026-06-08 PR review guide — 21 open PRs (#117–#137)

**Purpose.** Grant reviews each PR himself. This is the per-PR fast-review
checklist, ordered by dependency + risk so the careful ones cluster and the fast
ones batch. Every PR was verified `OPEN` / non-draft / base `main` /
`mergeable:MERGEABLE` against `origin/main` HEAD `63e6671a` (`gh pr list
--state open`, 2026-06-08).

**DO NOT merge from this guide** — it is a review aid; Grant merges.

## How to use this guide

- **Risk tiers**: `low-additive` (new doc/prereg/figure, no corpus edit) ·
  `code` (new script/tooling, additive) · `tracker` (orchestration doc) ·
  `corpus-edit` (touches KB/manuscript/constants — careful) ·
  `corpus-edit[Rule-12]` (a walk-back; verify the 🔴 header + preserved body).
- **The only two direct textual conflicts** (whichever merges 2nd rebases):
  - `manuscript/ave-kb/.index/claims.jsonl` → **#130 ∩ #132**
  - `manuscript/ave-kb/common/full-derivation-chain.md` → **#133 ∩ #135**
- **The r_opt sibling chain `#132 → #133 → #137`** is a *semantic* ordering
  (no shared file path); merge in that order so #137 reads the post-#133
  canonical r_opt. `src/ave/core/constants.py` is touched ONLY by #133.
- **Suggested review order**: fast batch first (low-additive + code + tracker),
  then the careful corpus-edit cluster (baryon-sector + r_opt chain in order),
  then the two large 06-07 forward-instrumentation PRs (#126, #134).

## Quick-reference table (review order)

<!-- quickref -->

---

## GROUP A — low-risk additive (fast batch; mergeable any order)

<!-- group-a -->

## GROUP B — code / tooling (additive; fast but eyeball the scripts)

<!-- group-b -->

## GROUP C — tracker (orchestration doc)

<!-- group-c -->

## GROUP D — corpus-edit walk-backs (CAREFUL; r_opt chain #132→#133→#137 IN ORDER)

<!-- group-d -->

## GROUP E — 06-07 α-route research + forward-instrumentation

<!-- group-e -->

## Cross-cutting flags

<!-- flags -->
