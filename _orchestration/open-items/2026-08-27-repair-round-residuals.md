---
id: repair-round-residuals
title: "Known-imperfect and deliberately-untouched — the closing inventory for the three 2026-08-26 walk/audit records"
status: OPEN
owner: lane
opened: 2026-08-27
source: research/2026-08-25_autonomous-hb-lens-audit_RESULT.md
anchor: "the dispatch targets exist only in the uncommitted run journal"
---

**This item exists instead of a fourth repair round, and the reason is
arithmetic rather than fatigue.** Three directed-repair rounds ran against
PR #1020 (`research/2026-08-26-overbraced-crystal-walk`), PR #1021
(`research/2026-08-26-wall-first-walk`) and PR #1022
(`research/2026-08-26-hb-lens-audit-result`). Each round's defect list included items the
PREVIOUS round had introduced — the round-3 list opened by naming four of them —
and round 3's own largest finds were regressions it caught in its own edits
before pushing. The judgement recorded at closure was that the expected
marginal defect of another editing pass now exceeds its expected marginal find,
so **the remaining known imperfections are inventoried here rather than
edited.** The rounds are in the branch histories if the judgement needs
re-testing.

**Read this as an inventory, not a work queue.** Nothing below is claimed to be
worth fixing on its own; several items are judgement calls recorded so a later
reader does not mistake them for oversights. **None of them is load-bearing on
any physics claim.**

## 1 — Deliberately NOT asserted, pending PR #1022 landing

**`research/2026-08-26_wall-first-and-trefoil-propagation-walk_RECORD.md` §0
does not say whether the autonomous-HB lens's flagged step (A3) actually
failed.** §0 now states the process finding — that A3 was named as *"the lens's
most load-bearing unverified step"* (`2026-08-25_autonomous-harmonic-balance-lens_RECORD.md`:131,
:157) and the arc advanced past it anyway — but stops short of characterizing
the audit's verdict. Three reasons, all still live:

- §0's own `[MEASURED-ELSEWHERE]` fence forbids it in as many words: *"this
  record does not characterize its verdict. Nothing here may be read as
  reporting one."*
- The audit RESULT doc is **not on PR #1021's branch**. Citing its disposition
  from there would be a cross-branch cite to an unmerged document.
- The process finding does not depend on the disposition. "It was flagged and
  we proceeded" is a process failure whether or not the flag turned out right.

**Decision needed once PR #1022 merges:** should §0 (and the routing item
`2026-08-26-wall-first-reframe-audit.md`) be updated to carry the A1–A7
disposition of A3, and if so does §9's *"forthcoming inputs not folded in"*
fence come down with it? **Do not do this before #1022 is on `origin/main`.**

## 2 — Quote-fidelity defect surfaced and left alone (different file, out of scope)

**`_orchestration/open-items/2026-08-26-electron-rest-energy-channel.md`:30–32**
renders the `cosserat-mass-gap.md`:151 driver-validation rider as a single
whole-block bold, and inside the quote marks it merges *"**No** driver
discriminates A1-mass from T2-mass."* — a separate sentence in the source, with
a capital N — into an em-dash clause reading *"— no driver discriminates
A1-mass from T2-mass."*

Same class as the added-emphasis defects repaired on PR #1021 at §5.2(1),
§5.2(2) and the §4.5 flag block, but one file over and not on that round's
defect list. **Surfaced under flag-don't-fix rather than fixed.** The physics is
unaffected: the rider's content (mass = A1 is RATIFIED-CONSISTENCY, an
adjudicated grade-assignment, not driver-validated) is quoted correctly.

## 3 — A cross-branch wording divergence that is now closed, recorded so it is not re-opened

The clip-domain statements on PR #1020 and PR #1022 were **both** falsified by
`A_max = 0.986728 < A_cap = 0.99` (F8, RESULT §3) — the sites saying the
solvers failed *at*, *reached*, or *crossed* the clip. **Three on PR #1020**
(record §4.2a, §7.2's amendment blockquote, §10's Q1 bullet) and, on PR #1022,
five in the round that produced this item (RESULT §0's sector declaration,
§2.5's F5 TRIM bullet, §7's FLAG 5, the routing item
`2026-08-25-autonomous-hb-lens-audit.md`, and the status note appended to
`2026-08-25_autonomous-harmonic-balance-lens_RECORD.md`) — each repaired to
approach-not-arrival with the receipt attached.

> ⚑ **CORRECTED 2026-08-27 — that sweep was INCOMPLETE, and two claims that it
> was complete were therefore false.** A later audit found **two more** sites on
> PR #1022 carrying arrival-shaped wording: **RESULT §3/F8's own A5 sentence**
> (*"the stall is a numerical failure **at the clip**, not a result"* — three
> lines below the same block's *"still just short of the clip"*), and **RESULT
> §5's charter-disposition row for A5** (*"break **at** the kernel's declared
> clip"*). Both are now repaired to approach-not-arrival with the receipt
> attached, bringing the number of sites repaired on PR #1022 to **seven** —
> which is a count of repairs made, not a claim that no eighth site exists.
>
> **The two false completeness claims, named:** (i) this paragraph's own *"All
> were repaired"*, corrected above; and (ii) commit **`74b04ec9`**'s message,
> *"After this commit every clip-domain statement on the branch agrees with
> §3/F8's `A_max = 0.986728 < A_cap = 0.99`"* — which was **not** true when it
> was written. That commit message stays as written (git is the audit trail);
> **this note is its correction.** Both are the stranded-pointer class: a
> completeness claim is a claim about a search, and neither search had covered
> §3/F8's own prose or §5's disposition table.

**Recorded because an earlier review note said PR #1020's twin passage had
already been repaired and the branches therefore disagreed in precision. They
did not disagree — they agreed, and both were wrong.** If a later reader finds
that note, this is the correction.

## 4 — Judgement calls a later reader may want to revisit

- **PR #1020's `hyperstatic` enumeration (§6.0) carries no total count**,
  deliberately: the count changes when the paragraph stating it is edited, which
  is the self-referential-fixture failure mode. It is stated as a partition
  (three gloss sites named, all outside §6.0; every remaining occurrence inside
  §6.0) so a grep can check it. If a stable total is ever wanted, it has to
  live outside the file it counts.
- **PR #1022's FL-12 records the twelve-vs-nineteen overlap as NOT
  ESTABLISHED.** The dispatch targets exist only in an uncommitted run journal.
  This is a permanent unknown unless the journal is committed; it is **not** a
  question a later lane can answer by re-reading the repo.
- **PR #1021's W4-6 charter row lost a sentence rather than gaining a
  rewrite.** Both parses of *"the one that loses is the one quoting ratified
  canon"* pre-judged a fork the record declines to adjudicate, so there was no
  correct version to restore. The row carries a one-clause ledger entry saying
  so.

## Blocking relationship

**None of this blocks anything.** All three source PRs remain
`[DO-NOT-MERGE][REVIEW: pending-orchestrator]` on their own terms. Item 1 is the
only one with a trigger, and its trigger is PR #1022 reaching `origin/main`.
