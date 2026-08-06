### ENTRY 2026-08-05-reconciler-authorization (2026-08-05): authorization record — Grant's go for the `calibration_role` reconciler (#873), and the standing rule it establishes: a go or ruling lands as a tracked record in the SAME session it is issued

> **★ WHY THIS RECORD EXISTS — read this before the content.** This fragment is not
> bookkeeping about a merge that already happened. It exists because an authorization
> that lives only in a chat transcript is, from any other lane's point of view,
> indistinguishable from an executor's own judgement. Four properties are what a
> tracked record buys, and none of them survive an untracked go:
>
> 1. **Discoverable.** A lane that greps `_orchestration/` for the authority behind a
>    gate finds it, instead of finding nothing and having to either stop or invent.
> 2. **Timestamped.** The go is fixed to a date, so a later reader can tell whether it
>    predates or postdates the object it authorizes — and can spot a post-hoc
>    reconstruction for what it is.
> 3. **Authority separated from executor.** The record says *Grant ruled X*; the commit
>    says *the lane executed X*. When those are the same sentence in the same head,
>    there is no gate. Splitting them is the gate.
> 4. **Ratified by merge.** Landing the record through a reviewed PR means the
>    authority claim itself passes a review, exactly like the physics it authorizes.
>    Merging this fragment ratifies the record.

---

## 1 — The authorization

- **Object:** the `calibration_role` reconciler — check #6 in
  `src/scripts/predictions_manifest_validator.py`, which reconciles each manifest
  row's self-declared `calibration_role` against CORPUS-DERIVED provenance
  statements in the bridged claim's `claim-quality.md` card.
- **Go issued:** Grant, **2026-08-05**, authorizing the reconciler to stand as a
  registered check.
- **Vehicle:** **PR #873** — `[REVIEW: CLEARED] infra: calibration_role reconciler —
  check the declared provenance axis against corpus-derived truth`. MERGED
  2026-08-05T13:36:07Z at `450dd7e0`.
- **Authority chain, in order, none of it self-cleared:**
  1. built and opened **DO-NOT-MERGE**, self-declared as needing an independent
     verify — the PR body's own opening: *"Tier-2 object (a new gate); needs an
     independent verify, not a self-clear."*
  2. Tier-2 independent audit returned **CLEARED-eligible NO** with three blocking
     findings; all three repaired, the repair pass landed on the same PR.
  3. re-reviewed to `[REVIEW: CLEARED]`.
  4. **Grant's go (2026-08-05)** — this record.
  5. merged; the merge ratifies.

**What the go covers and what it does not.** The go authorizes the reconciler as a
**report-only** check. It does **not** flip it to gating. The check's own flip
condition is named in `check_calibration_role`'s docstring and is keyed to two
specific rows, not to a class of rows; the posture stays `severity="warn"` until both
have not merely been ruled but **landed**. See §3 item 4.

---

## 2 — The parallel Grant named: the core session hit the identical gap the same week

This is the second instance of the same failure in one week, in two different
sessions, and Grant named the pair explicitly. Recording the parallel is the point —
one instance is an incident, two is a process defect.

- **The core-session instance.** A mechanical-rulings lane was dispatched with a Rule
  Zero of *"every ruling's operational content lives in the docket records — read them
  there … trust NOTHING transcribed in this brief."* Executed as instructed, **that
  check FAILED for six of the eight items**: no committed `_orchestration/` record
  carried the ruling text for R3, R4, R5, R7, R8, R12 or R13. What the dockets carried
  was the routed *question*, usually explicitly marked OPEN or *"Grant's call"*. Only
  R10 had a full ruling chain in committed corpus.
- **The lane did the right thing** — it stopped and flagged with verbatim evidence
  rather than inventing content, executing only where the docket already recorded the
  **consequence** of the ruled arm. That discipline is why the gap surfaced as a
  finding instead of as silently-fabricated canon. Record:
  [`2026-08-04-mechanical-rulings-batch-executed.md`](2026-08-04-mechanical-rulings-batch-executed.md),
  landed via PR #878 (MERGED 2026-08-05).
- **The repair was POST-HOC.** The missing ruling record landed afterwards as
  **PR #879** — `[REVIEW: CLEARED] orchestration: the 2026-08-03 thirteen-ruling
  record — provenance gap closed` (MERGED 2026-08-05T13:37:41Z), whose own body says
  it *"Lands the ruling record PR #878's headline finding showed was missing"*.
  Post-hoc works, but it costs a refused batch, a re-dispatch, and a reader who
  cannot tell reconstruction from contemporaneous record.

**The two instances share one shape:** the physics was fine, the review was fine, the
*provenance of the authority* was untracked — so the next lane downstream had to
either stop or trust a transcription.

---

## 3 — Standing rule (stated here, and to be stated identically in the core session)

> **A go or a ruling lands as a tracked record in the SAME session it is issued.**

Not at the end of the arc, not when the executing PR opens, not when a downstream lane
discovers it is missing. Same session. The record may be a one-paragraph docket
fragment; brevity is fine, latency is not. A ruling with no same-session record is
treated by downstream lanes exactly as PR #878 treated its six items — as a routed
question, not a ruling.

Corollary, from the #878 experience: where a ruling's *consequence* is already written
into canon, a lane may execute on the ruled arm and cite the canon for the content.
Where it is not, the lane stops and flags. That corollary is a mitigation, not a
substitute for the record.

---

## 4 — The four 2026-08-05 rulings this PR executes (the authority chain, recorded)

All four were issued by Grant on **2026-08-05**. Listed so the corpus carries the
authority for each, not just its execution.

| # | Ruling | Disposition in this PR |
|---|---|---|
| 1 | **P04 relabel** — `calibration_role` `chord` → `mixed` on the sin²θ_W row (`clm-5zuo7g`, `public_in_readme: true`), with two mandatory execution riders: (a) name the `K = 2G` dependency AND its standing upgrade path; (b) declare the comparison scheme explicitly or make no scheme claim at all | **LANDED.** Row relabelled; both riders written onto the row's `notes`. Verdict flips CONTRADICTED → RECONCILED. |
| 2 | **P42 re-role** off `forward-prediction` (`clm-3zz0f6`) — **APPROVED, CONDITIONAL** on an independent Tier-1 language-and-logic read of the replacement wording BEFORE it lands | **NOT LANDED — by instruction.** The manifest row is byte-untouched. Proposed role + proposed `notes` wording are carried in the PR body under an explicit *PROPOSED — NOT COMMITTED* heading, for the independent read. |
| 3 | **`P_A034_bh_ringdown` notes — WHOLE-BLOCK repair**, not label-only: swap the retracted 10–18%-frequency-error validation figure for Ruling B1's corrected framing, **preserving the row's empirical-comparison anchor** (repair by replacement, not deletion) | **LANDED.** Retracted figure replaced by the B1 framing; the three named merger events survive as the stated comparison anchor; the per-event ladder is pointed at, not duplicated. |
| 4 | **This authorization record** — land the reconciler go as a tracked docket fragment, carrying its own rationale, the #879 parallel, and the standing rule | **LANDED.** This fragment. |

**Also in this PR, as a consequence of ruling 1 rather than a ruling of its own:** the
`check_calibration_role` docstring's flip condition is updated to record that P04 is
DONE and only P42 remains, and sharpened from *ruled* to *ruled AND landed*. The gate
does **not** flip — `severity` stays `"warn"`, byte-unchanged.

---

## 5 — Verification

- PR states read live at write time via `gh pr view` (not transcribed): #873 MERGED
  2026-08-05T13:36:07Z (`450dd7e0`); #878 MERGED 2026-08-05T13:37:12Z; #879 MERGED
  2026-08-05T13:37:41Z.
- The six-of-eight finding read at its source in PR #878's body and mirrored in the
  committed fragment `2026-08-04-mechanical-rulings-batch-executed.md:3`, whose
  headline reads `that check FAILS for six of the eight items`.
- Reconciler census re-measured before and after on the live manifest (36 rows), not
  inherited from the docstring: before — UNDECLARED 12 / RECONCILED 12 /
  UNRECONCILED 10 / CONTRADICTED 2 (P04, P42); after — UNDECLARED 12 / RECONCILED 13 /
  UNRECONCILED 10 / CONTRADICTED 1 (P42).
- Adjudicates no physics. Mints no `clm-` / `def-` / `exp-` / `sup-` / `ilk-` id.
  Moves no `confidence` / `solidity` / `build_status` / `real_or_fitted` field.
