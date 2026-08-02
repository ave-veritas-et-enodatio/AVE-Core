# Manuscript-Reconciliation Epic — Orchestrator Handoff Brief

**Date:** 2026-08-01 · **Requested by:** Grant (verbatim [sic]: *"I'd also like to kick off a separate session/lane/epic/orchestrator on updating the manuscript from the KB"*) · **Author:** core-session orchestrator · **Status:** DRAFT — Grant launches the session himself and picks model/effort.

## Mission

Bring the printed manuscript (Vols 0–6, Vol 9, `manuscript/backmatter/`, and a check-only pass over `papers/`) into lockstep with the KB's current adjudicated state. **The KB is the truth source** (standing G-ruling; the reconciliation-handoff precedent): where they disagree, the manuscript moves, and where the KB itself is unsettled, the divergence is ROUTED back to the core session — never resolved in-lane.

## Why now

1. The compiled manuscript currently teaches retracted numbers in print. The strongest instance: Vol 3 ch 15 carries four printed sites asserting the retracted sub-2% Kerr-Q validation (interim chapter-head note landed 2026-07-31; per-occurrence rewrite owed — the #780 routing).
2. The 2026-07-01 honesty-lag audit cleared its 18-item backlog (batches A–G), but everything since — the B1 retraction propagation, the Q=ℓ scope tags, the ℓ-vs-overtone corrections, the v3 birefringence re-freeze, the superradiance provenance softening — reached the KB and *some* mirrors ad hoc. No systematic manuscript-vs-KB diff has run since.
3. The per-volume datasheet-cleanup program stopped after Vol 5 (merged #344/#347/#352). Vols 6 and 9 never ran; Vols 0–4 have accumulated new drift since their passes.

## Scope inputs (the routed backlog — verify each at launch, do not trust this list)

| # | Item | Provenance |
|---|---|---|
| 1 | Vol 3 ch 08 gravitational-waves warningbox: the LIVE bulk/shear double-count contradiction (Q1-revert, Reading-A) — physics prose rewrite owed | routed 2026-07-20 (q1-revert execution, arm d) |
| 2 | Vol 3 ch 08 item-3's shear-only rewording re-examined under Reading-A (ruled option (a)) | Grant ruling 2026-07-20 (#766 review F4) |
| 3 | Vol 3 ch 15: per-occurrence rewrite of the four printed sub-2%/spin-range sites | #780 routing; interim note via #810 |
| 4 | Datasheet cleanup: Vol 6 and Vol 9 (never run); drift re-sweep of Vols 0–4 | per-volume program precedent |
| 5 | Backmatter mirror-trio sweep: the KB-pair + `backmatter/*.tex` mirror pattern produced repeated divergence this window (sub-2%, superradiance, ℓ-vs-overtone all had a lagging tex mirror) — sweep the whole class | #809/#810/#816 receipts |
| 6 | Fresh full manuscript-vs-KB divergence sweep (the post-2026-07-01 delta) | this brief |
| 7 | `papers/` check-only pass (submission-gated; the birefringence letter already carries the v3 provenance — verify, do not churn) | #815 receipts |

## Method (per the validated per-volume pattern)

Per volume: **auditor sweep** (KB-state vs printed text, verbatim receipts, two-method greps) → **classified divergence list** (use the honesty-lag A–G taxonomy as the classification vocabulary: overclaim / stale value / missing retraction / scope-lag / mirror-drift) → **adjudication list to Grant** for anything ruling-shaped → **implementer worktree lanes** (skeleton-first incremental commits) → **one PR per volume**, `[DO-NOT-MERGE][REVIEW: pending-orchestrator]` → compact audit → repair → CLEARED → Grant merges.

## Sequencing note

The KB's ringdown sector is mid-churn (the cold-Q derivation arc is live in the core session). Sequence **Vol 3's ringdown chapters (ch 08 / ch 15) LAST**, or gate them on the derivation landing — otherwise they get reconciled twice.

## Discipline (binding)

- Rule 12 / KEEP-BOTH everywhere; frozen preregs byte-untouched; verify-before-cite two-method on every quote; pure-AVE-corpus.
- Every volume PR must pass `make verify`, `verify-md-links` gating 0, `refresh-kb-metadata` idempotent, and the volume's own `make volN` build (page-count and Overfull deltas disclosed, not hidden).
- Cite-shift sweeps after every insertion (the three-nested-undercounts lesson: filename-only patterns + bare "line NNN" forms; sweep runs AFTER content settles).
- Replacement-text discipline: a struck claim's slot is NOT refilled with new positive content unless that content is independently verified (three overreach instances this window).
- No physics re-adjudication in-lane. Divergences where the KB is unsettled → routed to the core session via `_orchestration/docket-entries/` fragments.
- Collision avoidance: check live branches before touching shared mirrors (`common/solver-toolchain.md`, `backmatter/05_universal_solver_toolchain.tex` are high-traffic).

## Interface with the core session

Cross-session items land as docket fragments; the core session's walk arcs (Q-law derivation, anisotropy fork) continue independently. This epic does not block on them except where the sequencing note says so.
