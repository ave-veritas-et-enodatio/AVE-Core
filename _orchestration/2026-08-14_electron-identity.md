# Epic: Electron identity — cleanup first, then horizons

**Status:** ACTIVE
**Opened:** 2026-08-14
**Goal:** Stop the corpus from offering killed electron mechanisms as current, then put the identification on a test that can fail — LC-5 form factor vs LEP, then the exterior Coulomb tail.
**Last updated:** 2026-08-15 (Phase A CLOSED — ledger on `main` via #970; Phase B is the next lane)

Filter for every phase: *does this stop a killed mechanism from being offered as current, or add one sentence to what an electron is?* If neither, stop.

The birefringence Letter is **not** in this epic (facility-class; submit tabled). Medium already has one banked kill (continuum static-E vs muonic hydrogen).

ELECTRON-IDENTITY-PROGRAM-ANCHOR: cleanup of killed mechanisms first, then LC-5 and Coulomb.

CHECKPOINT-1-KILL-LIST: signed with amends 2026-08-14 (Poincaré and cosmic injection held out).

---

## Current state at `origin/main` `ce55c881`

Phase 0 (#969) and Phase A (#970) are merged. The fence and the kill-list ledger are on `main`. Canon still offers K1/K3/K5 corpses as current; that is Phase B then C.

The catalog exists (`electron-identification.md`: \(0_1\) unknot, phase-space \((2,3)\), \(\Gamma=-1\) TIR *boundary* cavity, T₂ core). The object does not: no assembled electron, Coulomb \(1/r\) asserted, charge-channel form factor ill-defined.

Walk-level (un-audited, not dispatchable): `research/2026-08-04_electron-ontology-walk_framing-note.md` — *light that caught itself*. Checkpoint 1 pictures + smallest-wave question: `research/2026-08-14_electron-identity-checkpoint1-walk_RECORD.md`. Assertion-gate: walk-level never enters a lane's execution text — **except the §2 fence table of that RECORD** (the signed kills / amends).

## Checkpoint 1 — kill list (SIGNED WITH AMENDS 2026-08-14)

Grant in-session 2026-08-14 signed each row yes / amend. Durable fence:
`research/2026-08-14_electron-identity-checkpoint1-walk_RECORD.md` §2.
**Phase A (inventory) is CLOSED** (#970). The ledger inventories live-wrong hits of the
**signed kills**. It does **not** treat a held-out amend as killed.
**Phase B/C rewrite only the signed kills.** Held out of the kill: Poincaré-class
bulk cohesion (K1 amend; gated on FLAG-W + Coulomb); cosmic node-injection as a
*different* hypothesis (K3 amend, not in this epic unless Grant opens it).

| # | Ruled out (SIGNED YES) | Authority (pointer) | Proposed cleanup | Held out (AMEND) |
|---|---|---|---|---|
| K1 | Dynamical lock / remanence / reactive binding holds the electron | `research/2026-07-08_electron-lock-arc_CLOSE.md` CLOSED NEGATIVE | Type D banner; trackers SUPERSEDED | Poincaré-class bulk cohesion (FLAG-W + Coulomb) |
| K2 | Bulk self-trap as localizer | Stage-2 native-cage MODE-III DISPERSE; 2026-07-03 exposure sweep does **not** revive it | Confirm banners; grep unscope'd self-focus | — |
| K3 | Genesis from free precursor as manufacture path | Five self-assembly routes FAILED | Ledger SUPERSEDED, not deleted | Cosmic node-injection (not this epic) |
| K4 | \(Q=137\) as cage-emergent identity | T3.4b \(Q_\text{ringdown}\approx 30.8\), not \(\alpha^{-1}\) | Echo already in coverage matrix; grep identity-use | \(\ell_{\mathrm{node}}\) posit stands; Layer-8 is **not a program** (Grant 2026-08-14: do not derive \(\{m_e,\alpha,G\}\)) |
| K5 | LOOP GAP ranks as current manufacture path | Doctrine + lock-NEGATIVE | Epic/doctrine Status SUPERSEDED (historical ledger kept) | — |
| K6 | \((2,3)\) winding as dynamical mass-pin | S3 / #417; winding rides as static Link | Relabel banners exist; grep residue | Static Link + tank winding stand; `clm-satnec` OPEN |

**Do not delete** L3 archive, genesis result docs, or lock-arc negatives. Waste is *live pages that still sell a killed mechanism*.

**Flag-don't-fix (do not pick in any phase of this epic):**

- Two-node pair-production leaf vs \(0_1\) unknot identification (both ch01)
- Topology vs sub-yield stability accounts (plumbing primer 2026-08-02)
- Compositeness open-item text vs Gate-0 wall/charge split — Phase B may *update the item to match research*; that is honesty, not a ruling on F₁

## Focus rule (every PR)

End of every PR, three questions in this file (not a new dashboard):

1. Did we stop a killed mechanism from being offered as current?
2. Did we add a sentence about what an electron *is*, or an honest negative?
3. Did we open a new surface that is not 1 or 2?

Two consecutive PRs that fail 1 and 2 → stop and re-ask Grant.

## Phases

### Phase 0 (CLOSED 2026-08-14) — Front door

- Branch `analysis/electron-identity` off `origin/main` @ `91ca3db2`.
- This epic. Two `open-items/` files (program + kill-list). Docket kickoff fragment.
- `BOARD.md` regenerated on this branch (so the front door lists this program and is not the stale `e149080e` / 1-PR-open tree).
- **Out of scope for Phase 0:** 21 leftover worktrees (local chore), AVE-Skills README 19 vs 49 (wrong repo), the 34 other Grant-owned items, Letter submit, canon leaf edits.

### Phase A (CLOSED 2026-08-15, #970) — Inventory ledger

Read-only. No canon edits. No tracker Status flips. Do not banner a held-out amend as killed.

**Goal:** a kill-list ledger that classifies every HEAD hit of K1–K6 as Q1 historical / Q2 frozen journal / **live-wrong**.

**Kickoff:** read this Phase A section. After #969 merges, branch off `origin/main`. `isolation: worktree`. Do not checkout on the orchestrator tree.

**Assumptions**

- A1. Checkpoint 1 is signed with amends (2026-08-14 RECORD §2). Inventory live-wrong hits of the **signed kills**. Do **not** classify Poincaré cohesion or cosmic node-injection as killed.
- A2. Rule 12: the ledger quotes; it does not rewrite.
- A3. `verify-before-cite`: every live-wrong row has a file path + verbatim fragment + why it is offered as *current*.
- A4. Two-method grep (fixed-string + word-fragment). Report the commands.
- A5. Grant 2026-08-14: \(\{m_e,\alpha,G\}\) are calibration inputs and the **minimum set**. This epic does **not** derive them. Layer-8 is closed as a program target, not a signed kill. Do **not** inventory "Layer-8 OPEN" / "derive \(m_e\)" as a K4 corpse unless the page sells \(Q=137\) as the cage name. Do **not** walk back G's MIXED `/7` FORM in this lane.

**Scope boundary**

- IN: `manuscript/ave-kb/`, `_orchestration/` epics/trackers (status language), `research/2026-*` *titles/status lines that still say ACTIVE/IN PROGRESS for a closed arc*, AVE-Skills `ave-loop-gap-harness-discipline` as a **pointer** (do not edit that repo in this PR).
- OUT: L3 archive bodies (Q1 by default unless a KB leaf cites them as current). Engine code. New derivations. Picking flag-don't-fix tensions. `src/` except docstring status claims that present manufacture as live.

**Deliverable (one PR, this repo)**

- `_orchestration/2026-08-14_electron-identity-kill-list-ledger.md` — one row per live-wrong hit: path, verbatim fragment, K#, Q-class, proposed Phase B vs C.
- Counts: live-wrong / Q1 / Q2, with the listing command cited (directory-enumeration discipline).
- Phase A close-out paragraph in *this* epic (orchestrator lands that after merge, or the implementor appends a dated note if the brief is updated in the same PR — prefer a short "Phase A outcome" subsection at the bottom of the ledger, not a mid-file edit war on this epic).

**Adjudication:** none. Ledger is evidence. Checkpoint 1 is signed; the ledger still does not rewrite. Held-out amends are out of the kill, not out of the grep — quote them as Q1/live-wrong only if a page still sells the *signed* corpse (remanence, bulk self-trap, genesis-cook, Q=137-as-name, ranks-as-current-path, winding-as-pin).

**Verification:** `make verify` still green (no physics change expected). `generate_board.py --check` green if BOARD is untouched; if this phase does not edit BOARD, leave it.

**Closed by #970.** Deliverable: `_orchestration/2026-08-14_electron-identity-kill-list-ledger.md`. Outcome lives at the bottom of that file (not duplicated here). Orchestrator picks on ledger §5 (2026-08-15 review of #970): 5.1–5.3 are Q1; 5.4 is not a K-row. K2 is *not* fully retired — Phase C still owes C7/C8.

### Phase B (PENDING) — Tracker supersede

Read-only Status language on the Phase A ledger's 17 tracker rows (B1–B17). No physics-body rewrite. No Type D canon banners (that is Phase C).

LOOP GAP unified-harness epic SUPERSEDED; genesis-program-status SUPERSEDED; compositeness open-item text aligned to Gate-0 split (honesty, not a pick of F₁); coverage-matrix "do this ONE thing first" demoted as *priority*, not as a K4 kill. AVE-Skills loop-gap pointer in a **separate** repo PR. No canon identity rewrite.

**Kickoff:** branch off this close-out once it is on `origin/main`, or stack on the close-out branch. `isolation: worktree`. Do not checkout on the orchestrator tree. **Do not merge. Push + PR.** `[REVIEW: pending-orchestrator]`.

### Phase C (DEFERRED — gated on B + signed kill list) — Canon banners

Type D Rule-12 banners on signed live-wrong sites. Exhaustive walk-back grep. **Audit 1** (adversarial PR + `ave-audit`): no residue, no substitution-not-retraction, Rule 12 bodies intact.

**Checkpoint 2** after Audit 1: orchestrator paragraph — we cleaned waste; we did not mint a new electron.

### Phase D (DEFERRED — gated on Audit 1 green) — Horizons

1. LC-5 form factor vs LEP (existing-data; Lorentz-compliance arc). Frozen prereg, pointers-not-values, SVA header.
2. Exterior Coulomb tail — derive \(1/r\) or bank NOT-DERIVABLE. Name the terminal-charge fork; do not pick it in the dispatch.

**Checkpoint 3:** Grant muon/tau walk (ontology C3) before any lepton-ladder lane.

### Phase E (DEFERRED) — Modeling that needs Grant

S-exponent + engine-platform YES/NO only if an engine lane is still wanted. E1 \(|\Gamma|=1\) self-closure in circuit language after C3. No lock re-run. No \(Q=137\) closure. No derivation of \(\{m_e,\alpha,G\}\). No Letter submit. No genesis \(vN\).

## Open decisions

- Checkpoint 1: **signed with amends** (2026-08-14). Remaining Grant words on the *amends* are FLAG-W (already routed, not this item) and whether to open cosmic injection (default: no).
- **Calibration set (Grant 2026-08-14):** \(\{m_e,\alpha,G\}\) are the inputs and the minimum set. This epic does not derive them. Layer-8 is not a lane. Canon G MIXED form (`/7`) stands; Chain B′ (forward G) is not an electron-identity lane — whether to close that OPEN tag on the gravity register is a separate word, not this epic.
- Smallest-wave question (walk, RECORD §4): start from the linear photon, not a unique "smallest" wave. Not a phase until Grant says so. RECORD §4 unpaid (i) (which SI length replaces Compton if Layer-8 runs) is **moot**.
- Existing-physics manufacture (walk, RECORD §6): specify the medium, take projections (linear Maxwell → walls M/Q/J → saturation). Not a cook. Not a phase until Grant says so.
- Phase A: **CLOSED** (#970). Ledger is on `main`. Phase B is the next lane (17 Status flips + named tracker alignments). Phase C waits on B.
- Audit tags (close-out): `audit/2026-08-15_electron-identity-phase-0` @ `554c5ec0`; `audit/2026-08-15_electron-identity-phase-a` @ `869c11cf`.
- 21 leftover worktrees: local chore, not this epic.
- AVE-Skills README 19 vs 49: wrong repo; not this epic.

## References

- Identification: `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md`
- Coverage: `electron-bound-resonator-coverage.md` + `research/2026-06-17_electron-coverage-matrix.md`
- Lock close: `research/2026-07-08_electron-lock-arc_CLOSE.md`
- Ontology walk (2026-08-04): `research/2026-08-04_electron-ontology-walk_framing-note.md`
- Checkpoint 1 walk RECORD: `research/2026-08-14_electron-identity-checkpoint1-walk_RECORD.md`
- Lorentz arc / LC-5: `_orchestration/2026-08-04_lorentz-compliance-arc-brief.md`
- LOOP GAP doctrine: `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md`
- Compositeness: `research/2026-07-03_compositeness-defense-gate0_result.md` + engine-leg result
- Kill-list ledger: `_orchestration/2026-08-14_electron-identity-kill-list-ledger.md`
- Exterior field: `open-items/2026-07-03-exterior-field-profile-derivation.md`
