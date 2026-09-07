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

## 3 — A cross-branch wording divergence, twice repaired, recorded so it is not re-opened

The clip-domain statements on PR #1020 and PR #1022 were **both** falsified by
`A_max = 0.986728 < A_cap = 0.99` (F8, RESULT §3) — the sites saying the solvers
failed *at*, *reached*, or *crossed* the clip, each repaired to
approach-not-arrival with the receipt attached.

> ⚑ **RE-OPENED AND RE-REPAIRED 2026-09-06 (`0dc6f611`).** This section
> previously called the divergence *"now closed"*. It was not: the
> approach-not-arrival wording those repairs installed asserted a **universal
> over the round** — see §3c entry 4 — which the RESULT's own §2.5 falsifies.
> The header is corrected rather than the record deleted, and the accurate
> statement is that the divergence has now been repaired **twice**, on different
> axes: first arrival→approach, then universal→enumeration.

> ⚑ **CORRECTED 2026-08-27, second time. This section carried a running total —
> first "five", then "seven" — and both were wrong.** A bare total is replaced
> here by the **inventory**, keyed to the commit that made each repair, because
> the totals kept failing in the same way: each one counted the *defect lists*
> the rounds worked from, not the *repairs the branch contains*, and so it
> silently dropped every repair made between two lists. The two commits it
> dropped are `db3831a1` and `277557fa`, three sites between them.

### 3a — PR #1022: the ten repaired sites, keyed by commit

Line numbers are as at this branch's HEAD; the wording column is the text **as
it now stands**, not the falsified text it replaced (that is in each commit's
diff).

> ⚑ **RE-DERIVED 2026-09-06.** A later round (commit `0dc6f611`) corrected the
> *completeness* defect these repairs introduced — **six of the ten sites
> (rows 1, 3, 7, 8, 9, 10)** stated the clip result as a universal over the
> round rather than as the runs measured — and its edits moved the line column.
> **Every line below was re-derived against HEAD after that commit** by grepping
> each row's own wording, one row at a time. Rows **1, 3, 8 and 9** also carry
> re-stated wording, because the fragment they quoted no longer exists; rows 7
> and 10 were edited but the fragment they quote survived verbatim, and rows 2,
> 4, 5 and 6 were not edited at all. The `repaired by` column is unchanged and
> still names the commit that made the *approach-not-arrival* repair, not the
> later completeness repair.

| # | file | line | now reads, in part | repaired by |
|---|------|------|--------------------|-------------|
| 1 | `research/2026-08-25_autonomous-hb-lens-audit_RESULT.md` — §0 sector declaration | `:55` | *"is **approached, and entry is NOT ESTABLISHED** — of the clip-directed runs this doc reports, the three carrying an `A_max` give …"* | `d28e76fc`, re-scoped `0dc6f611` |
| 2 | `…_RESULT.md` — §2.5, the F5 TRIM bullet | `:409` | *"Picard stops converging on the APPROACH to the kernel's … clip"* | `d28e76fc` |
| 3 | `…_RESULT.md` — §7, FLAG 5 | `:1095` | *"which **no clip-directed run in this doc is reported reaching**"* | `d28e76fc`, re-scoped `0dc6f611` |
| 4 | `…_RESULT.md` — §3/F8, the "not a fold" headline sentence | `:531` | *"it is the solver dying on the approach to the kernel's own declared clip domain"* | `277557fa` |
| 5 | `…_RESULT.md` — §3/F8, the convergence-death receipt | `:536` | *"**convergence dies on the approach to `A_cap`**, with `A_max` still just short of the clip"* | `db3831a1` |
| 6 | `…_RESULT.md` — §3/F8, the branch-loss clause | `:538` | *"branch is lost approaching the clip, not turned around by a fold"* | `277557fa` |
| 7 | `…_RESULT.md` — §3/F8, the A5 answer sentence | `:543` | *"a numerical failure on the approach to the clip, not a result"* | `1a9afc85` |
| 8 | `…_RESULT.md` — §5, the A5 charter-disposition row | `:708` | *"break on the approach to the kernel's clip domain (`A_max = 0.986728` against `A_cap = 0.99` — **that run** stopped short …)"* | `1a9afc85`, re-scoped `0dc6f611` |
| 9 | `_orchestration/open-items/2026-08-25-autonomous-hb-lens-audit.md` — open question 2 | `:42` | *"all stopped on the **approach to** the saturation kernel's *declared* clip domain"* | `74b04ec9`, re-scoped `0dc6f611` |
| 10 | `research/2026-08-25_autonomous-harmonic-balance-lens_RECORD.md` — the dated status note | `:210` | *"a numerical failure on the **approach to** the saturation kernel's declared clip domain"* | `74b04ec9` |

**A new site, not on the ten.** `0dc6f611` also added a scope box in §3/F8
carrying the enumeration, the method and four blind spots. It is the one place
the clip result is stated in full. **Rows 1, 3, 8, 9 and 10 now point at it
instead of restating it**, which is why none of them re-mints a universal; row 7
sits immediately above the box and needs no pointer, and rows 2, 4, 5 and 6 were
already scoped to the run they describe.

Eight of the ten are in the audit RESULT doc; four of those eight are inside the
single §3/F8 block, which is why a search that had already "done F8" kept
missing the rest of it.

**Method, stated so a later reader can re-run it and can see what it would
miss.** Walk every commit on this branch — `git rev-list --reverse
origin/main..HEAD` — and for each, `git show --format= -U0 <sha>` filtered to
added/removed lines matching `clip|A_cap|0\.986728|approach`, case-insensitive;
then read each surviving hunk and decide by hand whether it is a clip-domain
wording repair or something else. **Blind spots this method has:** (a) it is
token-based, so a repair phrased without any of those four tokens is invisible
to it; (b) it reads diff lines, so a repair split across a line-rewrap would be
attributed to whichever commit re-flowed it — `37c0abc8` was inspected on this
run and is a pure rewrap, no wording change, which is why it carries no row;
(c) it counts repairs **made**, and says nothing about whether an eleventh site
exists that was never repaired at all.

For (c) a separate check was run, and it answers a different question:
`grep -rnE` across `research/` and `_orchestration/` for arrival-shaped
phrasings — the verbs *at / reached / reaches / crosses / crossed / into*
applied to the clip or to `A_cap` — with lines containing "approach" excluded.
Re-run against this file's final state, it returns **one hit on this branch**:
`research/2026-06-10_cavitation-core-probe_result.md:148`, an unrelated arc
whose clip is `−0.95`, not `A_cap`. **That is a statement about that regex, not
about the corpus** — it is one verb list, and a site that says the same thing
in different words is outside it. It was deliberately re-run after the last
edit to this item, because an earlier draft of this very paragraph cited a hit
on its own line number, which the edit that shipped it then moved.

### 3b — PR #1020's figure is NOT re-derived here

The earlier text of this section put **three** sites on PR #1020 (record §4.2a,
§7.2's amendment blockquote, §10's Q1 bullet). **That number is carried over
from the round that wrote it and has not been re-derived by §3a's method.** PR
#1020 is CLEAR and was deliberately untouched by this round, so nothing was
checked on it beyond confirming it was left alone. A reader who needs the
#1020 inventory should re-derive it the same way rather than trusting the
carried-over count — the failure mode §3a documents (counting defect lists
instead of repairs) applied to both branches' bookkeeping equally.

### 3c — the false completeness claims found so far, named

**This is a list of the ones that have been caught, not a claim that the list is
closed** — entry 4 was added after this heading first read *"the false
completeness claims, named"*, which is the same definite-article error the
entries below describe.

1. This section's original *"All were repaired"* — corrected in the round that
   raised the total to seven.
2. Commit **`74b04ec9`**'s message, *"After this commit every clip-domain
   statement on the branch agrees with §3/F8's `A_max = 0.986728 < A_cap =
   0.99`"* — **not** true when written. That message stays as written (git is
   the audit trail); this is its correction.
3. The **"seven"** that replaced them. It carried a hedge — *"a count of
   repairs made, not a claim that no eighth site exists"* — and the hedge was
   pointed at the wrong risk. The number was not merely optimistic about
   unrepaired sites; it was **wrong about repairs already in the branch**, by
   three.

4. **The wording §3a's repairs installed** — *"the clip domain is never entered
   — every solver failed on the approach, the furthest reaching
   `A_max = 0.986728`"* and its three siblings. Corrected 2026-09-06 in
   `0dc6f611`. The round that made the approach-not-arrival repairs replaced an
   arrival claim with a **universal over the round**, and the audit RESULT's own
   §2.5 falsifies it: the second converged continuum at `||v|| = 10.25 → 10.5`
   is recorded with **no `A_max`**, so *"the furthest reaching"* was never
   established. **This is the same failure one turn later — a repair round
   introducing the defect the next round finds — which is the arithmetic this
   whole item was opened to record.**

All four are the same class: a completeness claim is a claim about a search,
and each search was narrower than the sentence reporting it. §3a's response is
not a better number, it is an enumeration plus the method that produced it.

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
