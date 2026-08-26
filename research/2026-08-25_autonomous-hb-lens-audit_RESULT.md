# AUDIT RESULT — the AUTONOMOUS-HARMONIC-BALANCE lens (PR #1019): the existence criterion is DEAD as posed

**Date:** 2026-08-26 · **Branch:** `research/2026-08-26-hb-lens-audit-result` · **Base:** `origin/main` @ `a3f4fef7`
**Object under audit:** [`research/2026-08-25_autonomous-harmonic-balance-lens_RECORD.md`](2026-08-25_autonomous-harmonic-balance-lens_RECORD.md) (PR #1019, MERGED)
**Charter:** §6 of that record, `:151-167` — seven items **A1–A7** plus two required checks
**Routing item:** [`_orchestration/open-items/2026-08-25-autonomous-hb-lens-audit.md`](../_orchestration/open-items/2026-08-25-autonomous-hb-lens-audit.md)

---

## §0 — VERDICT

> # `THE EXISTENCE CRITERION IS DEAD AS POSED`
>
> ### The lens is repairable **only as a SELECTION test, never as an EXISTENCE test.**
>
> "Does a nontrivial source-free solution exist" cannot return NO. Existence is
> generic: continuous one-parameter families at machine-zero residual
> (`r_auto ~ 5e-15`), in **every** winding sector, **delocalized** across 45–85 %
> of the lattice, running continuously down to `A→0` where they **are** the cold
> empty lattice's own linear eigenmodes.

### ⚠ FIRST — THE AUDIT'S OWN INSTRUMENT WAS BROKEN, and it broke in the dangerous direction

The verify phase's roll-up computed each finding's status as
**`refuters >= ceil(total/2)`**. With two adversarial lenses per finding that
makes **one refuter equal REFUTED**. It stamped **all six findings REFUTED**
when **five were 1-of-2 SPLITS**, and in **four** of those five the *reproduce*
lane — the lane that ran code against the branch tip — voted `refuted=false`
with `confidence: high`.

**Had the orchestrator acted on the status column, four findings that survived
read-and-run would have been discarded.** This is a defect in the audit
*instrument*, not in the lens, and it is recorded here first because it is the
most transferable lesson of the round. Full treatment in §1.

### ⚠ WHAT THIS IS, AND WHAT IT IS NOT — read before quoting anything below

**Class: AUDIT DISPOSITION.** This doc records what the A1–A7 audit measured and
which charter items it discharged. It is **not** a physics result, **not** a
ruling, and **not** a decision. It mints nothing: no `clm-`/`def-`/`exp-`/`sup-`,
no KB leaf edited, no solidity moved, no register touched.

- **It does NOT rule on R58.** Decision 1 and the (2,3) carrier fork stay
  **LIVE and un-ruled**, exactly as the lens record's §7 (`:171-174`) states.
  Only Grant can rule that the lens replaces them, and this audit's verdict is
  that it does not currently qualify to.
- **It does NOT retract the lens record.** Per Rule 12 the merged record's body
  is untouched; a single dated status note is appended pointing here.
- **The findings are lane products, not this lane's measurements.** Every number
  below carries its measuring lane. The two exceptions — F9/F10 in §4 — were
  re-run against this branch's base before being quoted.

**Sector declaration.** MODE numerical-lens-audit · REGIME driven-to-saturated
(`A_bond` swept `0 → 0.95`, `S(A)` down to `0.31`; the kernel's clip domain
`A_cap=0.99 / S_min=0.05` is reached and is where every solver failed) ·
PHASE-STATE cold-through-saturated, no yield · CHANNEL **scalar / A1-adjacent
longitudinal ONLY** — the T2/Cosserat channel is not wired in
(`src/ave/solvers/harmonic_balance_srs.py:146-149`, verbatim: *"The T2/Cosserat
channel is NOT wired in (A1 perpendicular to T2, master-equation.md:20); no
winding observable exists here."*) · CARRIER **srs-z3**, `L=2` (N=64, degree 3,
96 bonds, **ndof = 192**), with unitarity spot-checked at `L=3` (648) and `L=4`
(1536). **Cross-wiring check performed:** nothing measured here couples the
scalar channel to charge, spin or mass — and §2.4 records that the *lens* does
cross that line, which is finding F4.

### Provenance of the evidence

Two phases, both agentic, neither previously landed in the repo:

| phase | shape | what it produced |
|---|---|---|
| **REVIEW** | 6 lanes, one per charter cluster | **28 findings**; 3 of them independently checked and all 3 **DOWNGRADED to MINOR** |
| **VERIFY** | **6** of those 28 findings × 2 adversarial refuter lenses (12 votes) + 1 completeness-critic synthesis | the verdict table, the two orphan findings, F9/F10, the reframe assessment |

**Selection bias, stated up front:** the verify phase re-tested only **6 of the
28** review findings, and all six came from **3 of the 6** review lanes. The A2
lane, the A4 lane and the A5/logic lane contributed **zero** findings to the
verify phase. Everything those three lanes found is **review-grade and
un-refuted-tested**. §5 and §8 say where that matters.

## §1 — THE INSTRUMENT BUG — read this before the verdict table

**The roll-up was wrong, and it was wrong in the dangerous direction.** The
synthesizer led with it, and it leads here for the same reason.

Each of the six findings was handed to **two** adversarial refuter lenses:

- a **reproduce** lane (build the object, run the code at the branch tip, try to
  break the measurement), and
- a **does-it-measure** / construct-validity lane (grant the number, attack the
  inference).

The roll-up then computed a per-finding status as `refuters >= ceil(total/2)`.
With `total = 2`, `ceil(2/2) = 1`: **a single dissenting lens sets the status to
REFUTED.** The synthesis states the same thing in its own words —
*"It is computed as `≥1 refuter → REFUTED`."*

### The actual votes

| # | finding | reproduce lane | does-it-measure lane | roll-up said | what it is |
|---|---|---|---|---|---|
| **F1** | unitary-generic | `refuted=true` | `refuted=true` | REFUTED | the **only** unanimous one |
| **F2** | seed-is-fork | **`refuted=false`** | `refuted=true` | REFUTED | **SPLIT** |
| **F3** | winding-is-seed | **`refuted=false`** | `refuted=true` | REFUTED | **SPLIT** |
| **F4** | no-wound-sector | **`refuted=false`** | `refuted=true` | REFUTED | **SPLIT** |
| **F5** | amplitude-free | **`refuted=false`** | `refuted=true` | REFUTED | **SPLIT** |
| **F6** | priorart-precondition | `refuted=true` | **`refuted=false`** | REFUTED | **SPLIT, the other way** |

All twelve votes carry `confidence: high`. **Five splits reported as six
unanimous refutations.** In four of the five, the lane that dissented from
REFUTED was the one that had actually built the operator and run it.

### Why it is the dangerous direction and not a wash

A false REFUTED is silently expensive in a way a false CONFIRMED is not. A false
CONFIRMED gets attacked again at the next gate — the corpus is built to do that.
A false REFUTED **removes the finding from the board**, and nothing downstream
ever re-opens it. Four of the discarded findings here are the ones that
established that the lens's core criterion cannot fail.

The failure has a second edge worth naming: in three cases the refuting lane was
arguing against receipts **produced in the same round that it could not see**.
F2's does-it-measure lane wrote that the wound-vs-trivial discriminating run
*"does not exist anywhere"*; F2's reproduce lane had run it, in the same round,
with a template-free integer readout (§2.2). Cross-lane invisibility plus a
one-vote refutation threshold is how a panel converts *"we disagree"* into
*"it is dead."*

### Two receipt-level cautions on this section

1. **The `status` column is not in the journal.** The twelve result records
   carry only `refuted`, `confidence`, `reasoning`, `corrected_claim`,
   `receipts`, `symmetric_standard_note`. The status field lives in the workflow
   roll-up, outside the journal. The formula quoted above is therefore recorded
   **as the synthesizer reported it**, cross-checked against the vote pattern
   (which is directly readable and is what the table above is built from), not
   read out of the roll-up source.
2. **"Three" vs "four".** The dispatch brief for this doc says the reproduce
   lane voted the other way *"in three of those"*. The journal says **four**
   (F2, F3, F4, F5). The synthesis's own bottom line agrees with four
   (*"it will discard four findings that survived read-and-run"*). Flagged, not
   silently harmonised.

### The repair, stated so it is reusable

A 2-lens adversarial panel has **no majority**. It should not report a scalar
status at all. The honest roll-up for an even panel is the vote vector plus the
disagreement axis — and where one lane ran code and the other did not, that
asymmetry is itself part of the report. `refuters >= ceil(total/2)` is a
majority rule applied to a set that cannot have one.

## §2 — THE VERDICT TABLE, F1–F6

*(section landed in a later commit)*

## §3 — THE ORPHAN FINDINGS — F7 and F8, filed by nobody

*(section landed in a later commit)*

## §4 — F9 / F10 — two new measurements, and a receipt-convention correction

*(section landed in a later commit)*

## §5 — CHARTER DISPOSITION — A1 through A7

*(section landed in a later commit)*

## §6 — THE BOTTOM LINE

*(section landed in a later commit)*

## §7 — THE OVER-BRACED CHIRAL CRYSTAL REFRAME — does it dodge these defects?

*(section landed in a later commit)*

## §8 — FLAGS SURFACED, NOT FIXED BY THIS LANE

*(section landed in a later commit)*

## §9 — WHAT THE AUDIT DID NOT COVER

*(section landed in a later commit)*

## §10 — Skill-selection retro-pass

*(section landed in a later commit)*
