# R62 — Grid-fix Option A: seven calls of 2026-10-29 adopt an approach and a test list (2026-10-29)

### ENTRY 2026-10-29-ruling-gridfix-option-a

*(Number provisional: the number in the title is the next free ruling number at `origin/main` `cbc668e7`. The Orchestrator confirms the number at merge.)*

**Grant, verbatim (the rulings of 2026-10-29, listed in §1 with their times). This fragment is their docket record. No primary artifact by Grant exists in the repo at the time of writing; a comment by Grant on the PR that lands this file, quoting the rulings, would make this record self-verifying.**

**Relay chain.** The 6:32 PM, 8:21 PM and 9:02 PM calls went Grant → the Orchestrator (relay) → the Physics Call Briefing bot (written to the pages below). The 8:20 PM call went Grant → the Physics Call Briefing bot directly. The pages sit in the program tracker on PR #7's head `a8e6386`; PR #7 is unmerged, so tracker `main` has none of them. This entry copies from those pages. It is orchestration-authored: Grant launched the session that wrote it, on 2026-11-01.

**Gloss.** PCB here is the Physics Call Briefing bot in the program tracker, not a printed circuit board.

**Scope.** Records the seven calls on the decision page and RULING-ADDENDUM-1. Not recorded here: `grant-rulings-2026-10-29-30-compute.md` (sha1 9a61edcbf3f0), including the 10-29 11:07 PM compute ruling and the 10-30 hold "Hold the memory engine change until the small-case results are in" (verified against `physics-walks/grid-fix-2026-10-29/grant-rulings-2026-10-29-30-compute.md`@a8e6386 (sha1 9a61edcbf3f0)).

**Later Math addenda, not rulings:** ADD-4 (readout form); ADD-5 §5 (supersedes parts of the bar table; sponge face clamp D = 1). ADD-5's row reads "ADD-3 FROZEN:70–79 (q-unit bar table and r_abs used on H̃)" (verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-must-emerge-list_ADDENDUM-5-math_2026-10-29.md`@a8e6386 (sha1 160f9da58f8b)).

**Why this entry exists:** a ruling relayed through the orchestrator session gets a docket receipt (the R59 precedent), and these calls had no in-repo record.

## §1 — THE CALLS, in time order

**1. Option A, 2026-10-29, 6:32 PM PT.** Grant, verbatim, as relayed by the Orchestrator:

> "Go with Option A plus the sliding-mode and op10 checks"

Verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-decision_2026-10-29.md`@a8e6386 (sha1 e9a51ec0f61a).

The page records what it adopts as: "an approach (Option A: both fixes) and a test list. Items 1–9 below, plus two added checks". Item 10 is the 9 zero-cost sub-lattice sliding modes; item 11 is the op10 static Hessian check; the page's old item 10 (constant impedance) "becomes non-graded **item H**". Gloss from the page: op10 is the quartic twist term, 'not the corpus "Op 10" junction loss'. The page's Option A line reads: "We'd hold the floor as a declared numerical patch with a width-shrinking check." Whether the ruling accepted this is decision-page question 3; see §4. T-STAB1 per bond was not settled here; see call 2. Each quote in this paragraph: verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-decision_2026-10-29.md`@a8e6386 (sha1 e9a51ec0f61a). DECISION, not a physics result; nothing FINAL.

**2. T-STAB1 per bond, 2026-10-29, 8:20 PM PT.** Grant, verbatim, in his own chat with PCB (the Physics Call Briefing bot in the program tracker, not a printed circuit board):

> "yes, include it"

Verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-decision_2026-10-29.md`@a8e6386 (sha1 e9a51ec0f61a).

Gloss: it answers whether Option A also writes T-STAB1 (the quartic twist term) bond by bond. The page adds: "the stability cure stays OPEN (A8:114 −160.1)" (verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-decision_2026-10-29.md`@a8e6386 (sha1 e9a51ec0f61a)). DECISION, not a physics result; nothing FINAL.

**3. Team-shift, 2026-10-29, 8:21 PM PT.** Grant, verbatim, as relayed by the Orchestrator:

> "Keep Option A and test the team-shift modes as harmless"

Verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-decision_2026-10-29.md`@a8e6386 (sha1 e9a51ec0f61a).

The page records κ_u as: "Math's κ_u term (own-site penalty on u, ADDENDUM 2 §2) stays an unadopted CANDIDATE, held in reserve." and goes on: "Item 10 (team-shift modes, labelled "sliding modes" on the list) is graded HARMLESS through H1–H4 per 80f5cf77 as scoped in ADDENDUM 2. H1/H2 pass on paper (DERIVED); H3/H4 need a run (OPEN)." Both quotes verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-decision_2026-10-29.md`@a8e6386 (sha1 e9a51ec0f61a). Outside the quotes: 80f5cf77 is `2026-10-29-sliding-mode-criterion_CANDIDATE.md`; it is on the Mac under `runs/gridfix/spec/`, not on tracker PR #7. DECISION, not a physics result; nothing FINAL.

**4 to 7. RULING-ADDENDUM-1, 2026-10-29, 9:02 PM PT.** "Grant's own words, relayed verbatim by the Orchestrator" on the four ADD-3 §8 calls:

| # | ADD-3 §8 call | Grant, verbatim | Recorded as (the page's cell, verbatim) |
|---|---|---|---|
| 4 | B2, item-11 bar | "Bar A: the physics bar" | Item 11 grades on bar A: λ_min ≥ −4/T², with r_abs ≤ bar/3 (ADD-3 §2). Bar B (tol₁₁ = 0.03) is not the grade. Math's lean was bar A. |
| 5 | Floor placement | "Floor (iii): both sides plus the impedance readout" | Softplus at k4q:257 **and** k4q:258, **plus** the readout clips at cf:733–738. This is **not** Math's lean, which was (ii). |
| 6 | R2 boxes | "R2 boxes 328/616" | R2 uses the 328/616 boxes, not A8 288/576. |
| 7 | PML | "Adopt the dt-invariant sponge" | Adopt the dt-invariant sponge spec (ADD-3 §8 item 4). |

Each quote and cell in this table, and the source line above it: verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-RULING-ADDENDUM-1_2026-10-29.md`@a8e6386 (sha1 6d05bd698258).

Gloss on the cells: the only AVE-Core line cites in this entry sit inside them. k4q = `src/ave/topological/k4_quaternion.py`, cf = `src/ave/topological/cosserat_field_3d.py`, both at `cbc668e7`, where the cited lines hold. They are pinned to that SHA and are not updated here.

Gloss on ADD-3: the version ruled on is sha1 099f68e46311 (`physics-walks/grid-fix-2026-10-29/pcb-grid-fix-must-emerge-list_ADDENDUM-3-math_2026-10-29_FROZEN-099f68e4.md`). The later REV-1, sha1 dd40aa31ed7e, is the file without the suffix.

Gloss on the floor call: the saturation direction itself stays OPEN per Grant's earlier ruling. The frozen list, line 115, reads "OPEN by Grant's decision" (verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-must-emerge-list_2026-10-29.md`@a8e6386 (sha1 7ec611196360)). Call 5 does not settle it.

## §2 — What this ruling does NOT rule

- The R2 charged-knot run STOP is the Gate's, not Grant's. §3 carries it beside the calls; this entry does not file it as a Grant ruling.
- No run GO is given.
- No claim or band moves. The calls are DECISIONS, not physics results; nothing is FINAL and no solidity tag rises.
- The saturation direction (the floor gloss in §1), whether e3 is physical and the ADD-4 cosmetic call stay unruled (§4).
- Decision-page question 3 has no explicit recorded answer (§4).
- Whether Option A discharges the Gate's T-STAB condition: not established (§3).

## §3 — The R2 charged-knot run STOP, carried beside the calls

**Not a Grant ruling.** Gloss: here R2 is the charged-knot run, not docket ruling R2 (SHA-pinned cites). PCB where it appears in a path is the Physics Call Briefing bot, not a printed circuit board.

- Math lead, SETUP-SHEET rev 2026-10-09, line 3, verbatim: "**A8 STOP FLAG: C-STAB (K-R23) FAILS for R2, R2-PF and P-ii.**" Verified against `math-corpus-map/2026-10-08-charged-seed-SETUP-SHEET_CANDIDATE.md`@a8e6386 (sha1 4eebf809f2c7). Gloss: Math raised the flag; the Gate concurred and stamped it.
- Engine Rigor Gate, 2026-10-09 ~11:30 PT, verbatim: "Verdict: CONCUR that R2 should not launch." Verified against `physics-walks/engine-rigor/2026-10-09/A8-VERIFY-and-R2-STOP-2026-10-09.md`@a8e6386 (sha1 57e758a26d0f).
- Gate, 2026-10-10, verbatim: "Merging #1067 does NOT lift the R2 STOP." and "R2, R2-PF and P-ii stay STOPPED pending Grant's T-STAB trade and D1." Both verified against `physics-walks/engine-rigor/2026-10-10/AUDIT-PR1067-v71-03bd7955-2026-10-10.md`@a8e6386 (sha1 5e0bfaf1577f).
- Carried forward on 10-29 in the briefing bot's words, not Grant's: decision page line 10, "**R2 stays stopped.**" Verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-decision_2026-10-29.md`@a8e6386 (sha1 e9a51ec0f61a).
- Current exit, verbatim from the frozen list, line 98: "**R2 stays stopped.** Option A does not restart R2. Item 11 needs its own pre-registered static check first, and R2 restarts only on Grant's word after that." Verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-must-emerge-list_2026-10-29.md`@a8e6386 (sha1 7ec611196360).
- Gate restart order: see `physics-walks/engine-rigor/2026-10-08/LADDER-charged-seed-K4-2026-10-08.md` (sha1 8b015a4be51e), lines 511 and 513. Not restated here.
- Status of the 10-10 conditions. T-STAB trade: Option A names T-STAB2′ and T-STAB1, and no page found says this discharges "Grant's T-STAB trade" (verified against `physics-walks/engine-rigor/2026-10-10/AUDIT-PR1067-v71-03bd7955-2026-10-10.md`@a8e6386 (sha1 5e0bfaf1577f)), so not established. The nearest text is decision page line 47, "R2 stays stopped until you pick a fix." (verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-decision_2026-10-29.md`@a8e6386 (sha1 e9a51ec0f61a)). Gloss: it does not name the Gate's condition, and decision page line 10 and RULING-ADDENDUM-1 keep the run stopped. D1 (Grant's O1 call, audit of #1067, 2026-10-10): no ruling found. Gloss: this D1 is Grant's call on the O1 strain convention, not any sense listed in `open-items/2026-08-13-key-namespace-collision.md`.
- Sources differ on R2-PF and P-ii. The 2026-10-10 audit above keeps them STOPPED. SETUP-SHEET line 3 reads "R2-PF and P-ii may run as cheap confirmations of the pre-registered FAIL" (verified against `math-corpus-map/2026-10-08-charged-seed-SETUP-SHEET_CANDIDATE.md`@a8e6386 (sha1 4eebf809f2c7)), and ladder line 22 reads "Allowed compute: R2-PF, R2-PF-C, P-ii and P-ii-C as **pre-registered confirmations**" (verified against `physics-walks/engine-rigor/2026-10-08/LADDER-charged-seed-K4-2026-10-08.md`@a8e6386 (sha1 8b015a4be51e)). This record follows the later audit and does not resolve the difference.
- Grid-fix Gate ladder v2 is box-only: not checked from the Mac.

## §4 — Still open (not rulings)

The HASH-REGISTER `Pending` block (Physics Call Briefing bot, 2026-10-29, updated 9:16 PM PT), verbatim:

> - Grant's cosmetic call from ADD-4: max(·,δ_R) or smooth δ_R+S_w. The Orchestrator relays it.
> - Item 6 (whether e3 is physical) is OPEN.
> - κ_u stays in reserve.
> - Tier 2 hardware is for the Orchestrator to schedule.

Gloss: Item 6 here is ADD-3 §8 item 6, not must-emerge item 6.

Verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-HASH-REGISTER_2026-10-29.md`@a8e6386 (sha1 9ad1c27d1d8f).

- From RULING-ADDENDUM-1 (Physics Call Briefing bot, 2026-10-29), verbatim: "No run GO is recorded here. R2 restart conditions are unchanged." Verified against `physics-walks/grid-fix-2026-10-29/pcb-grid-fix-RULING-ADDENDUM-1_2026-10-29.md`@a8e6386 (sha1 6d05bd698258).
- D1 (Grant's O1 call, audit of #1067, 2026-10-10), the O1 strain convention: "pending Grant D1" (Math lead, SETUP-SHEET rev 2026-10-09, line 20). Verified against `math-corpus-map/2026-10-08-charged-seed-SETUP-SHEET_CANDIDATE.md`@a8e6386 (sha1 4eebf809f2c7). No ruling found. Searched: the word D1 in the tracker at a8e6386 across `00-PROGRAM-STATE.md`, `physics-walks/engine-rigor/` and `physics-walks/grid-fix-2026-10-29/`, plus `runs/gridfix/spec/` on the Mac. The latest mention of this D1 found is the Sync 2026-10-29 entry, `00-PROGRAM-STATE.md` line 185, "conditional on D1" (verified against `00-PROGRAM-STATE.md`@a8e6386 (sha1 31c7bbb6504f)), which restates the 2026-10-12 audit of #1067 (`physics-walks/engine-rigor/2026-10-12/AUDIT-PR1067-68bbd204-2026-10-12.md`, sha1 7972638174b8). Gloss: the `d60fb506 D1` in ADD-3 is a different label.
- Decision-page question 3 (the floor as a declared numerical patch) has no explicit recorded answer.

**Class:** ruling receipt (grid-fix approach and test list; DECISION, not a physics result). Mints no `clm-`/`def-`; engine `src/ave` byte-untouched; this entry itself edits no KB or manuscript leaf.
