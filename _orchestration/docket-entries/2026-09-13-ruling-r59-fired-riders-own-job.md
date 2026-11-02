# R59 — `verify-fired-riders` leaves the required `verify:` gate for its own non-required CI job (2026-09-13)

### ENTRY 2026-09-13-ruling-r59-fired-riders-own-job

**Grant, verbatim (the ruling, 2026-09-13, relayed through the orchestrator session — this fragment is its docket record; no primary artifact by Grant exists in the repo at the time of writing, and a comment by Grant on #1041 quoting the ruling would make this record self-verifying):**
- *"I do NOT rubber-stamp a forgotten 2026-09-07 quote."*
- *"I DO accept the tradeoff NOW as a fresh ruling: move verify-fired-riders out of the required `verify:` gate into its own non-required CI job (safety valve — a broken finder / hard FAIL must not hostage every PR). The check still runs; it is advisory for merge protection."*
- *"Please add a one-line docket receipt for this 2026-09-13 ruling when you touch orchestration (so the PR's "own job" claim has a home). Then MERGE #1041, then MERGE #1042 (rebase whichever is second on verify.yml)."*
- The ruling's `Still HOLD:` section: *"#1026 Rule-12 gate — do not merge (RED on today's main; would red every PR)."* and *"Residue / BLOCKED / research stack (#1021–#1025 etc.) — out of scope; no action."*

**Why this entry exists:** PR #1041 (`infra/2026-09-07-fired-riders-own-job`) carried its authority as `Grant ruling 2026-09-07, verbatim: "move it to its own job."` in its `.github/workflows/verify.yml` comment (wrapped across two comment lines, so a contiguous grep misses it) and, without the terminal period, as the heading of its PR body. The 2026-09-13 Lane-B review pass found that quote was never written to the docket: no docket entry; no occurrence on `main` (`git grep -F 'move it to its own job' origin/main` is empty); nothing in #1035's PR thread (`gh pr view 1035 --json body,comments,reviews`). Grant declined to ratify it and ruled the same trade-off fresh, above. This fragment is the docket record of that ruling. The PR's `verify.yml` comment now cites it; the PR body is re-headed to R59 before merge.

## §1 — THE RULING (R59), restated by the entry in one line

**`verify-fired-riders` is removed from the `verify:` target inside the single branch-protection-required check `make verify + make test` (R3, [`2026-08-06-rulings-decision-batch.md`](2026-08-06-rulings-decision-batch.md)) and runs as its own non-required CI job, `fired prereg riders (non-required)`; the check still runs and is advisory for merge protection.**

## §2 — Execution ordered by the same ruling (Grant's orders; the parenthetical is the entry's)

Merge #1041, then merge #1042 rebased on `verify.yml` (the merge commits on `main` are the execution receipts: `git log --merges --grep='#1041' --grep='#1042' origin/main`). HOLD #1026; residue / BLOCKED / research stack: out of scope, no action. No PR-by-PR disposition beyond Grant's words above is ruled here.

**Class:** ruling receipt + CI placement. Infrastructure only; mints no `clm-`/`def-`; engine `src/ave` byte-untouched.
