# THE OUTCOMES-AND-ACTIONS BOARD — 2026-07-14 EIGHT-LANE BATCH (#686–#693)

**Class:** durable tracking doc (orchestration record). The CLOSING outcomes-and-actions
record for the 2026-07-14 eight-lane batch. All eight lanes have **settled** — nothing is
mid-flight — so this board is **not stale-on-arrival** (the standing meta-lesson from the
2026-07-13 reconciliation board's own "stale on arrival" amendment).
**Baseline:** written against `origin/main` HEAD `25b3b9116e9b80572ec2ac4e90f3852ffcec430c`
(the #691 merge). Five lanes MERGED (#686/#687/#688/#690/#691); three OPEN, fully repaired,
`[DO-NOT-MERGE][REVIEW: pending-orchestrator]`, awaiting Grant items (#689/#692/#693).
**This PR:** `docs/2026-07-14-batch-outcomes` lands this board + a short append-only
continuation row on `_orchestration/2026-07-10_rulings-docket.md` pointing here. No corpus
physics touched; records queue-state, not adjudicated physics; nothing here canonizes.
**Companion doc:** the day-2 docket continuation
[`_orchestration/2026-07-10_rulings-docket.md`](2026-07-10_rulings-docket.md)
("Continuation — 2026-07-14 EOD", landed by #686) and the prior-day board
[`_orchestration/2026-07-13_eod-reconciliation-board.md`](2026-07-13_eod-reconciliation-board.md).

**Verification posture:** every PR#, merge SHA, branch head, verdict wording, review count,
and file:line below was re-verified this session against `gh` / `git` (two-method where a
count is load-bearing). Facts from the launching brief that did NOT verify are flagged
inline with ⚠ rather than papered over.

---

## §1 — THE BATCH LEDGER

Eight lanes. Five MERGED to main; three OPEN + fully repaired + `[DO-NOT-MERGE]` awaiting
Grant items. "Review outcome" = the independent `ave-adversarial-pr-review` result
(confirmed / refuted counts, EVIDENCE-VOID = repair-and-bank with no verdict flip); "repair
range" = the review-repair commit span on the branch. Merge SHAs and branch heads
`git`-verified ancestors of / reachable from their refs this session.

| PR | Title (short) | Final state | Landed verdict (one sentence) | Review outcome | Repair-commit range |
|---|---|---|---|---|---|
| **#686** | 2026-07-14 EOD docket continuation | **MERGED** `3b05771a` (head `68b72b3d`) | Day-2 chat-only docket items banked append-only: the g−2 plumbing fork REFRAMED **DEGENERATE-UNTIL-A-BREAK** (two registers of one kernel, #685 `register_flip`), the register rail, census stage-1 state, and the consolidated auditor-batch queue. | none (single-commit docs; `make verify` + `verify-md-links` green) | n/a (1 commit) |
| **#687** | CVR trade-study v2 | **MERGED** `b05e6372` (head `f154b9c7`) | CVR v2 **SELECTS NOTHING** (STATUS:OPEN throughout, Grant + collaborator) — 43 options / 7 open trades, tiered qualifiers, remains-to-target gap table; the **T-D PLATES** theory ruling **carried forward** from v1, not re-opened. | none (single-commit decision-record; `make verify` + `verify-md-links` green) | n/a (1 commit) |
| **#688** | T_ij stress-register + X44b CHARTER | **MERGED** `fd7f257c` (head `73b72ac3`) | **CHARTER only** (no solver): the ONE-BUILD-SERVES-FOUR σ_ij register; **`R_yield` = ROLE-2 `S(A)→0`/Γ=−1 wall**, **slope-1 `√g₀₀=√S` clock**, reconciliation-gate (adjoint ≡ autodiff); **Flags F3 / F5 / F6** surfaced for Grant. | **10/10 confirmed, 0 refuted**, all EVIDENCE-VOID; repairs landed **in-place** (charter is pre-freeze) | `44723fc8`..`73b72ac3` (5) |
| **#689** | G-PERSIST localization observable + φ-plant | **OPEN** head `71b451ba` | FORK BIN = **LOOP-FILLING ⇒ Reading A (wake-feeding) CONFIRMED**; the two-meter combo is **un-foolable by DISTRIBUTED sustenance**; G-PERSIST ★RULED untouched; **Grant rules the fork**. | **15/15 confirmed, 0 refuted**, all EVIDENCE-VOID (fork verdict survives every finding) | `44afb78b`..`71b451ba` (6 repairs + SHA-map backfill) |
| **#690** | auditor batch — q-g20f re-tag + hygiene 2 | **MERGED** `a58ef1b6` (head `268c4ebb`) | q-g20f RT-equivalence rows → **SCOPED IMPORT** (inherits the §7 UNPROBED-NOT-CLOSED boundary); envelope **`def-envl0p` gate-marked, mint still Grant-gated**; ~10³⁹ → **`3.456e38`**; **fabricated quote struck** (`02_baryon_sector.tex:40`); `r_e` strike verified **OPEN / NOT landed**. | **10/10 confirmed, 0 refuted**, all EVIDENCE-VOID / repair-and-bank | `0e7d4e11`..`268c4ebb` (4) |
| **#691** | Route A: composite Faddeev-Skyrme neutron | **MERGED** `25b3b911` (head `d072025f`) | Bin **(iii) RIGHT-SIGN(-by-construction)-WRONG-MAGNITUDE** (`+38.12 / +39.12 m_e` vs target `2.531`, ~15×); δ_th-loading `+0.042 m_e`; **C5 RE-OPENED** (the δ_th ablation is **channel-blind** — measure-cancellation, not adjudication); **sign canon-forced-by-construction**. | **12/12 confirmed, 0 refuted**, all EVIDENCE-VOID (only the *promotion* of numbers to verdicts was refuted; the numbers reproduce exactly) | `d3e34426`..`d072025f` (5) |
| **#692** | cavity-census stage-1 (cold-linear leg) | **OPEN** head `1dd9485a` | **NO (2,3) EMERGENCE** on the **freeze-faithful LA cavity fundamental** (never read before) AND the SA defect band; the detector is **validated per-rung** ({1.0, 1.6}, blind at 0.16, misreads at 0.5); **COEXIST stands unchanged, SELECTION stays imported** (not a falsification of the electron). | **14/15 confirmed, 1 refuted**, all EVIDENCE-VOID; verdict survives (band inversion was the pivotal repair) | `c74aff23`..`1dd9485a` (4) |
| **#693** | QED-TRACE screening-sum gate | **OPEN** head `4d3355b0` | **WRONG-FORM** — the static electric-dipole screening SUM gives a power law, not `ln` (per-decade log-slope collapses ~33×); genuineness **RELABELED-PAIRWISE** (mid-bridge medium is a ~0.02% relative spectator; near clouds carry ~100%); **closure ENUMERATED** — dynamical/retarded + circulation-keyed inductive routes unprobed. | **10 confirmed, 1 refuted**, all EVIDENCE-VOID; WRONG-FORM/no-log + QED-sign findings **strengthened** | `721edae1`..`4d3355b0` (5) |

**Finding→commit maps** live in each PR's RESULT/charter "Review findings + repairs (2026-07-14)"
section: `research/2026-07-14_tij-x44b_CHARTER.md:253-272` (#688, on main); the branch RESULT
docs for #689 (`research/2026-07-14_gpersist-localization-observable_RESULT.md`), #692
(`research/2026-07-14_cavity-census-stage1_RESULT.md`), #693
(`research/2026-07-14_screening-sum-gate_RESULT.md`); and on main for #691
(`research/2026-07-14_route-a-composite-fs_RESULT.md:227-244`) and #690 (its PR-body ledger +
per-cluster commits).

**Aggregate review tally (two-method — per-PR bodies + branch RESULT grep):** **6** adversarial
reviews ran across the batch (#688–#693); **71 findings confirmed, 2 refuted, 0 verdicts
flipped** — every confirmed finding EVIDENCE-VOID repair-and-bank. Of these, the **5 wrapper
reviews** on the freeze-by-push / analysis lanes (#689/#690/#691/#692/#693) account for **61
confirmed / 2 refuted**; the #688 charter adds **10 confirmed / 0 refuted** as in-place
pre-freeze repairs. ⚠ **Brief-number flag:** the launching brief's "~50 confirmed findings
across 5 wrapper reviews" **undercounts** — the verified confirmed total across the 5 wrapper
reviews is **61** (15+10+12+14+10), not ~50; "0 verdicts flipped" verifies exactly.

---

## §2 — GRANT DECISION QUEUE (the actions column)

<!-- SECTION-STUB: 8 decision rows, each with blocking relationship + authoritative in-repo site -->

---

## §3 — QUEUED FOLLOW-ON WORK (registered, NOT fired — per Grant's no-new-lanes directive)

<!-- SECTION-STUB -->

---

## §4 — META-LESSONS (register-honest)

<!-- SECTION-STUB -->

---

<!-- FOOTER-STUB: cross-refs + lane attribution -->
