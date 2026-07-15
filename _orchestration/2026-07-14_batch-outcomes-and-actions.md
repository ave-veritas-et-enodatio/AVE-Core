# THE OUTCOMES-AND-ACTIONS BOARD — 2026-07-14 EIGHT-LANE BATCH (#686–#693)

**Class:** durable tracking doc (orchestration record). The CLOSING outcomes-and-actions
record for the 2026-07-14 eight-lane batch. All eight lanes have **settled** — nothing is
mid-flight — so this board is **not stale-on-arrival** (the standing meta-lesson from the
2026-07-13 reconciliation board's own "stale on arrival" amendment).
**Baseline:** written against `origin/main` HEAD `25b3b9116e9b80572ec2ac4e90f3852ffcec430c`
(the #691 merge). Five lanes MERGED (#686/#687/#688/#690/#691); three OPEN, fully repaired,
`[DO-NOT-MERGE]`, awaiting Grant items (#689/#692/#693). ⚠ **Review-tag nuance** (brief said
all three `[REVIEW: pending-orchestrator]`): #689/#693 title-tag `[REVIEW: pending-orchestrator]`;
**#692 title-tag is `[REVIEW: repaired]`** (its body reads `[REVIEW: repaired — pending-orchestrator]`)
— substantively all three await the orchestrator/Grant.
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

Eight items awaiting a Grant word. Each row names the **decision**, the **blocking
relationship** (what it gates), and the **authoritative in-repo site**. Verbatim anchors
(with file:line) follow the table. Sites on the three OPEN branches are quoted from those
branch refs; merged-lane sites are quoted from `origin/main`.

| # | Decision needed | Blocking relationship | Authoritative site |
|---|---|---|---|
| **1** | **F6 Komar-clock register ruling** — is `√S` the EM/wrong register (X44 §5b(i)) or the slope-1 Komar clock (W2 + RULED-(c) `komar_weight`)? | **BLOCKS the X44b prereg freeze** — the `η ≈ −1 → 0` ladder and the `\|η\| < 1e-3` PASS turn on exactly this factor-2 | `research/2026-07-14_tij-x44b_CHARTER.md:251` (Flag F6) + `:272` (auditor-queue cross-source contradiction) + `:106` |
| **2** | **#689 meter-register call** — bank **potential-only** vs **kinetic-inclusive** vs **KEEP-BOTH** energy-density meter (kinetic ≈ 44% of H); orchestrator recommends **KEEP-BOTH**, fork verdict is register-robust either way | Gates the localization-meter register; the composed (kinetic) numbers are NOT banked pending this call (four non-fork cells' bins move; the two fork cells stay LOOP-FILLING under both registers) | `research/2026-07-14_gpersist-localization-observable_RESULT.md:330` (cluster-3 escalation) + §"Finding #3 — ESCALATED" `:336-377` — branch `analysis/gpersist-localization-observable` |
| **3** | **#689 enclosure-fork ruling** — Reading A (wake-feeding) vs Reading B (bound resonance); the data **CONFIRM Reading A** (LOOP-FILLING on both statistics, ~~both boundaries~~) *(**2026-07-15:** the "both boundaries" PML-twin leg is **withdrawn** as boundary corroboration on the full register — #698 meter-ontology §5/§7 + RESULT Finding #3 ESCALATED §1; the verdict rests on the **torus** cells, LOOP-FILLING robust under every read. Reading A + G-PERSIST ★RULED unchanged.)* | Closes the #670 enclosure/closed-box fork toward A (**KEEP-BOTH-OPEN** until ruled); does NOT re-open G-PERSIST ★RULED | `research/2026-07-14_gpersist-localization-observable_RESULT.md:160,167-168` + header `:8` — branch `analysis/gpersist-localization-observable` |
| **4** | **#692 LA-target freeze-fidelity ratification** — ratify that reading the **LA fundamental** is freeze-fidelity to the frozen §4 bin-i "lowest interior mode" (vs. a post-hoc target move) | Closes the **D3 RULED-COEXIST stress-test loop** (verdict unchanged either way — non-(2,3) on both spectral ends); docket D3 rows then move via the auditor | `research/2026-07-14_cavity-census-stage1_RESULT.md:545-547` (§"Adjudication for Grant") + `:488-489` — branch `analysis/cavity-census-stage1` |
| **5** | **#693 "intervening cells" reading ratification** — ratify reading "intervening cells" (prereg §4:157) as the **mid-bridge medium** (RELABELED-PAIRWISE = primary; shipped-cylinder 50% = near-dress-slicing, KEEP-BOTH) | **Gates the `q-g20f` re-tag propagation** — Grant ratifies before the caveat-drop lands | `research/2026-07-14_screening-sum-gate_RESULT.md:50-53,237-239` (⚑ FLAGGED for Grant) — branch `analysis/qed-trace-screening-sum` |
| **6** | **#691 canonization** (optional) — canonize a `NEUTRON_ELECTRON_RATIO` / `M_N_MEV_AVE` into `ave.core.constants`? **Default = NO** (value-blind; the #676 n–p-gate detector stays clean by design) | Optional; default holds **C5-OPEN**, detector clean; canonization would flip the #676 corpus-state detector | `research/2026-07-14_route-a-composite-fs_RESULT.md:194-199` (§"Coordination") + `:110-111` (C5-OPEN) — on `origin/main` |
| **7** | **F5 conjecture-surface clarification** — did Grant's balance≡yield conjecture mean the ROLE-3 `A²=2α` **knee** or the ROLE-2 `S(A)→0` **wall**? (two same-day Grant inputs in tension; KEEP-BOTH) | **Adjudicated at the gate-(b) ENVELOPE-EIGENMODE freeze** — the charter defines `R_yield` as the ROLE-2 wall and pre-resolves nothing | `research/2026-07-14_tij-x44b_CHARTER.md:250` (Flag F5) — on `origin/main` |
| **8** | **Envelope-LENGTH canonical mint** — promote `r_env` (`def-088f0d`, `:367`) + node-Nyquist (`def-e0cd83`, `:382`) to SOLID | **Still gated on the §45 A-vs-B canonical FORK** (sub-node charge-core vs supra-node body envelope); `def-envl0p` (`:386` GATE marker) is the non-locking hygiene record only | `manuscript/ave-kb/common/vocabulary-register.md:367,382,386` (r_env def "GATED … NOT SOLID"; def-envl0p GATE) + `_orchestration/2026-07-10_rulings-docket.md:724,782` — on `origin/main` |

### Verbatim anchors (file:line — quoted this session)

1. **F6** — charter `:272`: *"**X44 §5b(i)** (`:126-138`) vs the **W2 walk-back** + **RULED (c)** live `komar_weight` is a *substantive* cross-source contradiction on whether `√S` is the EM/wrong register or the slope-1 Komar clock; the X44b prereg must resolve which register is the clock **before** freezing."* (charter `:106`: *"★ The X44b prereg MUST name WHICH temporal register is the clock (slope-1 `√g₀₀` vs slope-2 `n`) BEFORE freezing … (Flag F6)."*)
2. **#689 register** — RESULT `:330`: *"…the kinetic term is **not committed to the driver** and the composed numbers are **not banked** into §2; surfaced for orchestrator/Grant adjudication (register choice = framing-level)."* (fork-robustness at `:369`: *"fork cells stay LOOP-FILLING (disperse harder …) so the verdict is robust — but four non-fork cells' bins MOVE."*)
3. **#689 fork** — RESULT `:167-168`: *"Carve — Grant rules the fork. This driver returns the discriminator **data**; it does not fiat the fork."* (`:160`: *"⇒ Reading A (wake-feeding) CONFIRMED; the fork closes toward A."*; header `:8`: *"enclosure fork = KEEP-BOTH-OPEN."*)
4. **#692 LA** — RESULT `:545-547`: *"**Adjudication for Grant:** ratify that reading the LA fundamental is freeze-fidelity to 'lowest interior mode' (this repair's position), vs. treating it as a post-hoc target move. Either way the verdict is unchanged — non-(2,3) on both ends. D3 stays RULED-COEXIST stress-test."*
5. **#693 intervening cells** — RESULT `:53`: *"the corrected reading is primary; **Grant ratifies this interpretive step before the q-g20f re-tag propagates.**"* (`:237-239`: *"⚑ **FLAGGED for Grant ratification.** … Reading 'intervening cells' as the mid-bridge medium … is the crux interpretive step; Grant ratifies before propagation."*)
6. **#691 canon** — RESULT `:195-199`: *"canonization is a corpus-state change requiring Grant adjudication of this result … the **live detector remains clean by design** … canonization (which would flip the detector) awaits Grant's ruling."*
7. **F5** — charter `:250`: *"…whether Grant's conjecture meant the knee or the wall is his to adjudicate at the gate-(b) freeze. (Distinct from Flag F3 … F5 records the ROLE-2-vs-ROLE-3 *surface-role* contradiction between the two Grant inputs.)"*
8. **Envelope mint** — vocabulary-register `:367` (r_env `def-088f0d`): *"VERIFIED **0 prior exact-token `r_env` hits** … **GATED on Grant review — NOT SOLID.**"*; docket status-board `:782`: *"**Envelope def-node** … **QUEUED (OPEN, Grant-gated)** — PROPOSED, gated on §45 A-vs-B fork."*

---

## §3 — QUEUED FOLLOW-ON WORK (registered, NOT fired — per Grant's no-new-lanes directive)

All items below are **registered** in-repo; **none is dispatched**. Grant's word launches
each (or none). Cites point at where each is already booked.

1. **T_ij / σ_ij register build (gate-first).** The #688 charter is the gate; the build + the
   four per-consumer preregs land in a follow-on arc **after the charter's review**
   (`research/2026-07-14_tij-x44b_CHARTER.md:4`). **ONE build unblocks four arcs:**
   (a) X44b faithful Komar, (b) the ENVELOPE-EIGENMODE gate, (c) census **Stage-2**, and
   (d) electron `T_rr` (charter `:28`, §3 consumers). Registers-first plan of record RATIFIED
   (docket `:457`).
2. **Census Stage-2 (driven / walled)** — now the **load-bearing (2,3) test**. The cold-linear
   leg is **INSTRUMENT-INCONCLUSIVE by construction**: no engine-representable positive
   control can read (2,3) there (the seeded electron reads conclusive `(0,0)`), which is *why*
   Stage-2 driven is load-bearing (`research/2026-07-14_cavity-census-stage1_RESULT.md:311-313`,
   branch `analysis/cavity-census-stage1`). Rides the T_ij register as consumer (c).
3. **3D composite Faddeev-Skyrme build** — the **only C5-capable instrument**. The 1D radial
   proxy structurally excises the δ_th-carrying quartic linking channel (measure-cancellation);
   a faithful magnitude AND a faithful C5 test need a genuinely 3D composite FS solve — a
   separate, larger build (`research/2026-07-14_route-a-composite-fs_RESULT.md:51,250`, on main).
4. **Core-localized adversarial pump plant** (#689 follow-on) — registered **REQUIRED but NOT
   run**: the shipped φ-plant is spatially-DISTRIBUTED, so the un-foolable claim is scoped to
   distributed sustenance; a core-localized pump is the remaining negative control
   (`research/2026-07-14_gpersist-localization-observable_RESULT.md` repair cluster #2, commit
   `31b85424`, branch `analysis/gpersist-localization-observable`).
5. **Floor-augmented fit family for #693 (amendment A1.7)** — the naked whole-window `p≈0.60`
   is **HELD OUT of canon** pending a floor-augmented refit; the DECISIVE content is the slope
   collapse, not the global exponent (`research/2026-07-14_screening-sum-gate_prereg_FROZEN.md`
   AMENDMENT A2 / A1.7; RESULT `:359`, branch `analysis/qed-trace-screening-sum`).
6. **Auditor batch 3** (implementer surfaces; the auditor lands the manual/KB entries):
   - **q-g20f caveat-retire** — may drop the beta gate's one named "unprobed" caveat but stays
     **SCOPED** (static electric-dipole route only) and must NOT read as a full/complete
     import; **GATED on #693's Grant ratification** (§2 item 5) + the enumerated closure
     scoping bound into it (`research/2026-07-14_screening-sum-gate_RESULT.md:375-377`).
   - **X44 §7-option-5 + §5b(i) clock-register relabels** — the origin of the F6 mislabel +
     the substantive cross-source contradiction, flagged for the auditor queue, NOT edited in
     #688 (`research/2026-07-14_tij-x44b_CHARTER.md:270-272`).
   - **`vocabulary-register.md:173` pre-existing fabricated path** — the same fabricated
     `manuscript/vol_2_quantum/chapters/02_baryon_sector.tex:40` reference exists at
     `vocabulary-register.md:173` (pre-existing on main, not in #690's diff; routed to the
     auditor queue — #690 Flag 5).
   - **`r_e` strike at `trampoline-framework.md:687`** — still **OPEN / NOT landed** (verified
     NOT touched by #682); the "classical electron radius scale" parenthetical on the
     `ℓ_node/(2π) ≈ 61 fm` tube radius is a mislabel (`r_e ≈ 2.8 fm`) — #690 Flag 2.
   - **#691 RESULT `:177` attribution nit** — the 1D-radial-proxy / corpus-TBD-pin attribution
     note (`research/2026-07-14_route-a-composite-fs_RESULT.md:174-180`, on main).
   - **Docket-row moves post-rulings** — the D3 / q-g20f / envelope docket rows move only after
     the corresponding §2 rulings land (auditor executes the writes).
7. **CVR selection session (Grant + collaborator)** + its **3 receipt-debts**: the ~1e11 V/m
   field-evaporation ceiling pin; the fixture-*k* measurement; the blocking-element `C(V)`
   characterization (`research/2026-07-14_cvr-trade-study_v2_DECISIONS-OPEN.md` Part 3, on main).
   SELECT NOTHING until Grant + collaborator convene.
8. **Candidate process change — promote the structural-null stencil lens into the review
   workflow's STANDING DISCIPLINE block.** The lens was the **highest-yield knife of the day
   — 4 same-day kills**: #691 channel-blind δ_th ablation, #692 wrong spectral end +
   detector-blind floor, #689 seam-clipped CF, #693 near-cloud slicing. Candidate for
   `ave-adversarial-pr-review` / review-workflow standing discipline; **surfaced, not adopted**
   (process change is Grant's / the auditor's to ratify).

---

## §4 — META-LESSONS (register-honest)

1. **The structural-null stencil lens was the highest-yield knife of the day — 4 kills.** Every
   one of the four found a **disabled-flag / wrong-coordinate artifact masquerading as physics**:
   #691's δ_th ablation is **channel-blind** (the quartic linking channel is structurally
   excised by the 1D shift measure); #692 read the **wrong spectral end** (SA, band-inverted)
   AND had a **detector-blind floor** (a planted (2,3) reads the same refused `(0,0)`); #689's CF
   statistic was a **seam-clip artifact** on the periodic torus (fixed by minimum-image);
   #693's Knife-B was **near-cloud slicing** (the "many-body" signal was each probe's own
   dress, not the medium). The lens is the §3 item-8 standing-discipline candidate.
2. **Fabricated-quote / phantom-citation under a verify-claim surfaced ×2 — two-method grep
   every stamp.** (a) #690 finding #2: a **fabricated quote + false VERIFIED stamp** on the
   **fabricated non-path** *vol_2_quantum/chapters/02_baryon_sector.tex:40* ("multi-node body
   envelope") — that directory does **not** exist (real tree: `vol_2_subatomic/`) and the phrase
   has **0** genuine corpus hits (two-method `grep -F` + `git grep`, re-verified 2026-07-15);
   **struck, NOT repointed** in `0e7d4e11` (repointing to the real
   `vol_2_subatomic/chapters/02_baryon_sector.tex:41` "spans multiple fundamental nodes" would
   re-assert the supra-node reading the §45 A-vs-B fork holds open — same rationale as the
   def-envl0p / `vocabulary-register.md:174,414` strikes). (b) #692: a **phantom
   citation** — `"frozen §2 smallest-algebraic (most-bound)"` appears **nowhere** in the frozen
   body (the frozen §4 bin-i says only "the lowest interior mode"), caught by two-method grep
   and corrected. A **third, pre-existing twin** of the (a) fabrication survives at
   `vocabulary-register.md:173` (routed to the auditor queue — §3 item-6). Lesson: a VERIFIED
   stamp / frozen-body citation is not self-certifying — re-grep it two-method.
3. **Chat-relay ≠ repo receipt** — the `q-g20f` "screening-sum gate registered open, sibling
   lane" case. #690 finding #6: that parenthetical was **unreceipted coordinator-chat** (absent
   from #685 §7 and from the repo), stripped at 3 KB sites + `claims.jsonl` (`e309b61a`). A
   claim's home is the repo, not the relay; the KB carries only §7-supported boundaries.
4. **Session-limit resume worked** (process note; no repo receipt — harness mechanics). The
   batch spanned a session-limit boundary and resumed cleanly via transcripts +
   `resumeFromRunId`; no lane lost its freeze-by-push ordering or its finding→commit map across
   the resume.
5. **Every confirmed finding was EVIDENCE-VOID repair-and-bank; 0 verdicts flipped — the
   pipeline is functioning.** Across the batch's adversarial reviews, **no verdict flipped**:
   the numbers reproduced exactly and only the *promotion* of numbers to interpretive verdicts
   was ever refuted (#691's C5 retraction is the exemplar). That zero-flip rate is itself
   evidence the **freeze-by-push + wrapper-review** pipeline is working as designed. ⚠ See the
   §1 tally flag: the verified confirmed count across the 5 wrapper reviews is **61** (not the
   brief's "~50"); "0 verdicts flipped" verifies exactly.

---

## Cross-references + lane attribution

**The eight lanes (SHAs re-verified this session):**
- MERGED: **#686** `3b05771a` · **#687** `b05e6372` · **#688** `fd7f257c` · **#690** `a58ef1b6`
  · **#691** `25b3b911` (= `origin/main` HEAD).
- OPEN (`[DO-NOT-MERGE]`, fully repaired): **#689**
  `analysis/gpersist-localization-observable` @ `71b451ba` (title-tag `[REVIEW:
  pending-orchestrator]`) · **#692** `analysis/cavity-census-stage1` @ `1dd9485a` (title-tag
  `[REVIEW: repaired]`; body `repaired — pending-orchestrator`) · **#693**
  `analysis/qed-trace-screening-sum` @ `4d3355b0` (title-tag `[REVIEW: pending-orchestrator]`).

**Companion tracking docs:** the day-2 docket continuation
`_orchestration/2026-07-10_rulings-docket.md` ("Continuation — 2026-07-14 EOD", #686) — this
board adds a short append-only continuation row there pointing here; and the prior-day
`_orchestration/2026-07-13_eod-reconciliation-board.md` (whose "stale on arrival" amendment is
the standing meta-lesson this board is structured to avoid — all eight lanes are settled).

**Source docs (per PR):** `research/2026-07-14_tij-x44b_CHARTER.md` (#688) ·
`research/2026-07-14_cvr-trade-study_v2_DECISIONS-OPEN.md` (#687) ·
`research/2026-07-14_route-a-composite-fs_{prereg_FROZEN,RESULT}.md` (#691) · the #690
auditor-batch diff (KB/manuscript) · and on their branches the #689/#692/#693 `_prereg_FROZEN`
+ `_RESULT` docs.

**Lane attribution:** this board is authored in **implementer lane** (orchestration record).
It **surfaces** empirical outcomes + the Grant decision queue; it does **NOT** land any
manual / KB / manuscript entry — the **auditor lane** lands those (§3 item-6 batch), and
**Grant adjudicates** the §2 queue. Per flag-don't-fix, brief-vs-repo mismatches are surfaced
inline (the ~50/5 tally undercount, §1) rather than silently reconciled. Pure-corpus; nothing
here canonizes; records queue-state, not adjudicated physics.
