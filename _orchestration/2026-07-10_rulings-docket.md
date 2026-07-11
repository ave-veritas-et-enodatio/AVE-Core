# Rulings docket + working model — core planning session (2026-07-10)

**Purpose:** the durable record of the core-session **working model** and the **rulings docket** — the queue of framework-level decisions the core session owns, their walk-materials, and their adjudicators. Track-in-repo, not memory/context. Every PR#, claim-id, and file cite below was grep-confirmed against the corpus this session (verify-before-cite). Companion to the orchestration board (`_orchestration/2026-07-10_orchestration-board.md`, session-close findings/PR register) and the R-B framing note (`research/2026-07-10_rb-fossil-walk_framing.md`).

---

## THE WORKING MODEL

Two kinds of session, cleanly separated:

- **This session = core planning / rigor.** It runs the **walks, the rulings, and the board**. It does not execute simulations or drivers itself; it produces framing notes, adjudications, and handoff briefs. Its output is decisions and the materials a decision needs.
- **Execution = satellite orchestration sessions.** Grant launches and directs these **himself**, from handoff briefs written into `_orchestration/`. He chooses the **model and effort per session**, and the core session **chips in only on request**. The satellites are where drivers run, prereg-freezes land, and PRs get cut.

Consequence for this docket: the core session's job is to get each ruling **walk-ready** (materials assembled, adjudicator named, fork-record clean) and then either rule or hand the number-generating piece to a satellite. Testing over fiat: where a measurement can decide, the ruling is **deferred to the number**, not decreed.

---

## SATELLITES RUNNING (Grant-launched 2026-07-10)

| Satellite | What | Carries |
|---|---|---|
| **#33** | collapse-target sweep | next collapse-target sweep item (post-vertex-arc) |
| **#38 / X40** | ring transient | **the cut/cycle-split addendum** — the R-B deciding measurement (report cut-space vs cycle-space components of the trapped fraction + trapped-flux sign vs `ring-normal · Ω̂`); a cycle-fraction ≈ 0 banks R-B branch (i), finite banks the T-odd family |
| **#11 / X42** | eigencavity | the atom-as-port / eigencavity spectrum thread |

---

## HELD HANDOFFS (write on request, post-rulings)

These briefs are **not yet written** — each is gated on a ruling that must land first, so the meter and the source stay in matched coordinates:

- **#34 — physics batch.** Needs the **A1↔T2 bridge ruling first** (sector ownership: resolve A1 vs T2 before the capture spec, so the meter and the source are in matched coordinates — A46 phase-space discipline). See the board slate `#34` row for the D-IV nucleation-capture framing.
- **#37 — full-vertex.** Inherits the **R-B four-branch fork** (the circulator / T-breaking escape; the vertex non-reciprocity question). Grant picture-walk before any prereg (walk input is a circuit, not a formalism).
- **#40 — CVR bench spec.** **Walk-first on measurement topology** — the CVR held-DC-E bench is the empirical adjudicator for R-A (K1 vs K2); the bench spec is Requirements-derived + trade-study-open per the bench-doc pattern, and the measurement-topology walk precedes the spec.

---

## THE DOCKET

### R-A — K1-vs-STANDING-CANON  ·  **NEXT UP** (walked in the core session post-compaction)

**The question:** does a held longitudinal static **E** load the **T2** saturation kernel? A ruling **for K1** is a **NEW axiom-level decision against the current canonical reading — NOT a contradiction-resolution.** The X41 / #627 record governs (the canon is internally consistent; the fork is a *reinterpretation* choice, not a bug fix — `manuscript/ave-kb/common/program-arc-map.md:313`, OF10 row).

**Walk-materials (assembled, ready):**
- the confirmed **#547 config-fact** — the muon loads the **full `|E|` into the `V_yield` / T2 key, with no Helmholtz split** (`research/2026-07-10_x41-radiative-scoping-why_RESULT.md:154`; merged #547, `[DERIVED: CHARGE-KEYED]`) — this is what K1 must overturn;
- **M1's computed topology mechanism** which K1 must beat (the two-topology time-domain DC-response derivation of the #547 arc);
- **K2's impedance reading** (the off-line reactive-static dress; the mode-basis / impedance candidate, `research/2026-07-10_impedance-register-walks_framing.md`);
- **the CVR held-DC-E bench = the empirical vote** (K1 vs K2 split only on the transverse-reactive near-zone — an unbuilt probe; the bench is the adjudicator, board §5 / §6).

**Status:** UNDERDETERMINED — frozen tie [K1 ∧ K2] (PR #627, MERGED); K1 = axiom-level reinterpretation, PENDING-GRANT; K3 DEAD-on-arrival. Core-session walk NEXT UP post-compaction.

### R-B — the circulator / T-breaking question  ·  **WALKED · RULING DEFERRED**

WALKED this session — see the framing note `research/2026-07-10_rb-fossil-walk_framing.md` (T-even twist vs T-odd frozen circulation; the field-cooled-ferrite / Barnett analogy; the cut⊥cycle Helmholtz split + u₀* homonym flag; the four-branch fork-record; the u₀*-as-loaded-4₁-screw geometric identity). **RULING DEFERRED to X40's cut/cycle number** per Grant ("testing is better than ruling"). #38/X40 carries the deciding addendum.

### R-C — branch-(i) on the (2,3) f_touch = 1/(2π) degenerate locus  ·  **PENDING**

At swept cell `(s_L, s_C) = (2,3)`, `f_touch = 1/(2π)` EXACTLY, INSIDE `f_crit` — an exact obj-1 co-minimum ON the unknot tube-radius (branch-i) mark in the self-consistent regime (`research/2026-07-10_x38-s11-bore-selection_result.md:25,37,80`). A **formula locus**, not asserted as branch (i), not dismissed — **UNADJUDICATED PENDING-GRANT**. Colored by R-B's outcome (whether the vertex carries a T-odd bias bears on how the degenerate locus reads).

### R-D — the Op6-audit W1 question  ·  **PENDING**

The uniform-far-field match question (from the Op6-scope / S₁₁ honesty-lag audit, #621 site 2): does the "match into the uniform `Z_0` far-field bath" framing **escape** doc-34's exterior-`Γ²=0` flatness, or is it the **closed exterior match renamed**? Flagged PENDING-GRANT, not silently resolved (`_orchestration/2026-07-10_orchestration-board.md:76`).

### D-V — the submission decision  ·  **PENDING (weekend)**

The Letter submission decision — **Grant + Keith + Benn, weekend.** Task **#41 (comment-strip)** is **gated on it** (no comment-strip until the submission call lands).

---

## Docket status board

| Ruling | What | Status | Adjudicator |
|---|---|---|---|
| **R-A** | K1-vs-STANDING-CANON (held-E loads T2?) | **NEXT UP** — frozen tie, PENDING-GRANT | Grant (axiom-level) + CVR held-DC-E bench |
| **R-B** | circulator / T-breaking | **WALKED · DEFERRED** | X40 cut/cycle number (testing over fiat) |
| **R-C** | branch-(i) on (2,3) f_touch=1/(2π) locus | **PENDING** (colored by R-B) | Grant, on the degenerate locus |
| **R-D** | Op6-audit W1 uniform-far-field match | **PENDING** | Grant |
| **D-V** | Letter submission decision | **PENDING** (weekend) | Grant + Keith + Benn |

---

*Cross-refs: the R-B framing note (`research/2026-07-10_rb-fossil-walk_framing.md`); the orchestration board (`_orchestration/2026-07-10_orchestration-board.md`, session-close findings + PR register + fresh-session slate); the impedance-register framings note (`research/2026-07-10_impedance-register-walks_framing.md`, the K1/K2 off-line-register walk). Discipline: verify-before-cite run on every PR# / claim-id / file cite above; pure-corpus; nothing here canonizes — the docket records queue-state, not adjudicated physics.*

---

## Continuation — 2026-07-11 (post-X40/X42/registry)

Docket state after the X40 (#632/#638), X42 (#634/#639), and collapse-registry (#631/#636/#637) landings. **KEEP-BOTH:** the original docket + status board above are **not edited**; this continuation carries the new state. Every PR#/cite below was git/gh-confirmed this session (verify-before-cite).

### R-B — the circulator / T-breaking question · **DECIDER REPORTED**

X40's cut/cycle split landed: **9/10 T-even strain : 1/10 T-odd cycle flux**, **machine-exact** — a **THEOREM** of the ratified matched-bath model (`trapped = 1/girth`; N=10 girth → 1/10; the split was independently reproduced as `N=7→1/7, N=13→1/13`, `research/2026-07-10_x40-ring-closure-transient_result.md:104`). Consequences:
- **The T-odd family stays ALIVE** — but **model-conditional**: *"It does NOT prove the bias is real"* per the P10 statement (`research/2026-07-10_x40-ring-closure-transient_result.md:294`). A finite cycle-fraction banks the T-odd family only *within* the matched-bath model.
- **Orientation-bias UNMEASURED.** The **"BALANCED (net ~0)"** leg is **retired as a DFS-sign-convention artifact** (#638; `:200,:206`). What survives is **plane-isotropy** — the **sign-free Q tensor** (`|Σn̂|/N = 0.047`, orientation tensor ⅓·I, `:196`) — which is real and **BOUNDS branch (ii)** (a uniform T-odd swirl), it does not measure one.
- **Branch (iii)** (staggered / Haldane) needs the **srs staggerability graph check** (bipartiteness / cycle-parity, R-B framing §6a). **Branch (iv)** (orientation-keyed) needs **circulation-keyed formation statistics** (task **#34 / D-IV**).
- **The `u₀*` homonym-split trigger fired CONDITIONALLY** — both projections (strain-`u₀*` cut-space, flux-`u₀*` cycle-space) nonzero *within the model*. The **register split stays gated on Grant + the model-conditionality** (the split is owed only if the finite cycle-fraction is model-independent).

### R-A — K1-vs-STANDING-CANON · **WALKED · HOLD-THE-TIE**

Walked 2026-07-10/11. Posture = **HOLD-THE-TIE** (Grant: testing over ruling; the frozen [K1 ∧ K2] tie, #627, stands). The **X42 `saturate` finding** first read as a **spectral vote for transparency** (K2-leaning), then was **WEAKENED by the Nyquist licensing caveat** (§2 of the new framing note `research/2026-07-11_ringdown-nyquist-pi-register_framing.md`): the muonic wreckage is produced where the continuum kernel has no license, so it votes against an **unlicensed calculation**, not cleanly against loading physics. The **licensed R-A discriminators** are the **CVR held-DC-E bench** (task **#40**, walk-first) and a **discrete-lattice muonic eigencavity solve** (candidate arc, gated on Grant's *which-two-liquids* + *barrier-vs-crossover* answers).

**★ NEW STRUCTURAL OBSERVATION — one axis behind three rulings.** **R-A ∧ registry-T4 ∧ Route-C are the same question:** *what variable does `S(A)` key on?*
- **R-A:** `E_T` (K1) vs full `|E|` (standing canon);
- **T4 (MOND EFE):** the internal source's `g_N` only (→ no EFE) vs the **total local** field (→ EFE);
- **Route-C (birefringence μ-grade):** **circulation** vs **flux**.
One keying principle should answer all three. **Recommendation: walk R-A and T4 TOGETHER** — the sector-ownership answer is shared, and splitting them risks a per-ruling convention drift.

### NEW ROWS from the registry (cross-ref board §5, merged #636)

Grant-gated adjudications surfaced by the collapse-target registry (flag-don't-fix; Grant's to rule):
- **T3** — Γ=−1 **short-vs-fuse** loss-character (walk-shaped; a possible sign/loss issue riding in the thrust + decay benches — lossless short vs blown fuse).
- **T4** — **MOND external-field-effect keying** (forward-prediction opener; **fold with R-A** per the axis observation above).
- **T6** — **mass→inductance sector** contradiction (TKI dictionary-image vs a genuine A1↔T2 cross-wire).
- **T13** — **N13 protein-folding scope** (full falsification vs narrower channel; **cross-repo** — receipt in the AVE-Protein lane).
- **T15** — **S₁₁ INVARIANT-N4 touch** (needs the **out-of-repo `eq:s11_energy` receipt** before any edit; touches a solidity-1.00 invariant).

### FIRE-READY COLLAPSE BATCH · **UNBLOCKED** (post-#637)

The registry's fire-ready CLEAN tier is now unblocked (the #637 registry-receipt repairs landed): **T1 / T2 / T5 / T7 / T8** (X41-gated on bin-3) **/ T10 / T12 / T14 / T16 / T19** + the **δ_strain precision rider** (board Continuation-2 §5). The **handoff brief is written on Grant's go** (handoff-briefs-not-chips — the brief is Grant-launched, not chipped inline).

### Unchanged rows

**R-C** (branch-(i) on the (2,3) `f_touch=1/(2π)` locus), **R-D** (Op6-audit W1 uniform-far-field match), **D-V** (Letter submission, weekend) — **unchanged**. Note **R-C is now colored by the live T-odd family**: whether the degenerate locus reads as branch (i) bears on R-B's still-open T-odd branches.

### Docket status board — continuation state (KEEP-BOTH; original table above unedited)

| Ruling | What | Status (2026-07-11) | Adjudicator |
|---|---|---|---|
| **R-A** | K1-vs-STANDING-CANON (held-E loads T2?) | **WALKED · HOLD-THE-TIE** — X42 spectral vote weakened by the Nyquist licensing caveat; walk with T4 (shared keying axis) | Grant (axiom-level) + CVR bench (#40) + discrete-lattice muonic solve (gated) |
| **R-B** | circulator / T-breaking | **DECIDER REPORTED** — 9/10 : 1/10 cut/cycle (theorem of the matched-bath model); T-odd family ALIVE but model-conditional; orientation-bias UNMEASURED (BALANCED retired #638); branches (iii)/(iv) open | X40 number (reported) → Grant on the `u₀*` register split |
| **R-C** | branch-(i) on (2,3) f_touch=1/(2π) locus | **PENDING** (now colored by the live T-odd family) | Grant, on the degenerate locus |
| **R-D** | Op6-audit W1 uniform-far-field match | **PENDING** (unchanged) | Grant |
| **D-V** | Letter submission decision | **PENDING** (weekend, unchanged) | Grant + Keith + Benn |
| **T3** | Γ=−1 short-vs-fuse loss-character | **NEW · Grant-gated** (walk-shaped) | Grant |
| **T4** | MOND EFE keying (forward-prediction opener) | **NEW · Grant-gated** — fold with R-A (shared `S(A)`-keying axis) | Grant |
| **T6** | mass→inductance sector contradiction | **NEW · Grant-gated** | Grant |
| **T13** | N13 protein-folding scope (cross-repo) | **NEW · Grant-gated** (receipt in AVE-Protein lane) | Grant |
| **T15** | S₁₁ INVARIANT-N4 touch | **NEW · Grant-gated** (needs out-of-repo `eq:s11_energy`) | Grant |

---

## Continuation — 2026-07-11 (Grant input round, 16 items)

Sixteen items Grant surfaced in the 2026-07-11 input round, recorded as short rows (RULED / WALK-CONTINUES /
PARKED / GO). **KEEP-BOTH:** the two continuations above (post-X40/X42/registry + the original docket) are
**not edited**; this section carries only the new input round. Nothing here canonizes; substrate claims below
are records of Grant's rulings, not new assertions. Cross-refs verify-before-cite'd this session.

1. **R-A Kerr-cell gut-check — WALK-CONTINUES.** Grant asked for the DC/AC circuit analysis; delivered in-chat.
   **SECTOR:** the canon cell is a lumped LC tank with ONE scalar `V`. Analysis: DC bias reaches the shunt node
   through the DC-short series-L (#547-M1, computed); AC small-signal reads the tangent `C` at the operating
   point (#547-M3). Because the lumped cell has a single scalar `V`, **K1's polarization split** and **K2's
   `R_rad` relocation** are **not expressible in the canon cell** — they are **MODIFIED-CIRCUIT proposals**, not
   readings of the canon circuit. Circuit analysis of the canon circuit = **loads**; the K1/K2 tie persists only
   as a dispute about **which circuit the vacuum IS**. Grant response pending.
2. **Free-fall gut-check — WALK-CONTINUES.** Restated in-chat (elevator form). Grant response pending.
3. **Discrete-solve framing — RULED.** Grant: **drop the media-taxonomy framing**; work the **BOUNDARY
   CONDITIONS at the interfaces directly** (continuum↔discrete crossover, soliton surface). The discrete muonic
   arc is to be framed **BC-first**.
4. **R-C — RULED-TO-TEST.** Grant reframe: is the (2,3) `1/(2π)` degenerate locus **REMEMBER** (stored/frozen
   preference persisting when de-energized) or **RELAX** (dynamic equilibrium under drive)? Discriminator = a
   **vertex transient** with desaturation / back-EMF observables (kick the vertex, de-energize, watch whether
   the locus preference persists). **Arc candidate, not yet dispatched.** (Refines R-C above, which stays
   PENDING on the degenerate locus.)
5. **R-D / W1 — CANDIDATE RESOLUTION (Grant-walked, pending verification).** The "match into the uniform `Z₀`
   far-field bath" **IS** the boundary condition that every point of the soliton surface sees uniform 377 Ω;
   the E-strain dress = the soliton's projected shape onto that uniform background. Under this reading the
   "match" language and doc-34's exterior flatness (`Γ²=0`) are the **SAME statement**, not a renamed closed
   match. **Owed:** a verification pass against doc-34's exact wording, then a register relabel. **NOT yet
   closed** (R-D above stays PENDING until the doc-34 wording pass lands).
6. **T3 — RULED-IN-SHAPE.** Grant's question "are electrons and nodes the same?" answers the homonym: **NO**.
   The **electron-cage `Γ=−1`** (stable sub-yield lossless TIR confinement of a bound mode) and the
   **past-yield node-rupture** boundary are **DIFFERENT objects in different regimes** and must not share the
   glyph. Resolution = **KEEP-BOTH SPLIT** (confinement-`Γ=−1` stays lossless; the rupture boundary is
   **fuse-class**, consistent with the ringdown-absorption lean). Final wording + the thrust/decay bench relabels
   **await the sweep's A4 verdict**.
7. **T6 — RULED.** Follow the most robust claim: the Grant-ratified **A1-dilatation mass ownership governs**;
   the M-row demotes to **TKI translation-image**. Executed in the collapse batch (D1,
   `_orchestration/2026-07-11_collapse-batch-handoff.md`).
8. **u₀* split — RULED.** **WAIT on the split** (model-conditional trigger — X40 returned both cut/cycle
   components nonzero only within the matched-bath model). The homonym **FLAG rides the T12 def-node mint** (D1
   rider, flag-not-split).
9. **T13 protein scope — PARKED.** Grant: "worry later."
10. **T15 S₁₁ invariant — NOT OPENED.** Tidiness alone does not justify touching a solidity-1.00 invariant;
    parked behind T13.
11. **Astro sweep — GO.** Brief in canon: `_orchestration/2026-07-11_astro-adjudicator-sweep-handoff.md`. Grant
    launches, his model / effort.
12. **Collapse batch — GO.** Brief = D1 of this PR: `_orchestration/2026-07-11_collapse-batch-handoff.md`.
13. **#40 CVR bench walk — WAITS (Grant-confirmed).** The two-config requirement stays recorded; walk **after
    the keying adjudicators report**.
14. **C13b — GO.** Run the frozen prereg; brief = D2 of this PR:
    `_orchestration/2026-07-11_c13b-bullet-cluster-run-handoff.md`. (Run-time flag: the prereg's α/β/γ
    adjudication gate is stale — Grant already adjudicated (γ), `dm-mechanism-unification.md:54`; the brief
    surfaces this for confirmation.)
15. **Precision house rule — ★RATIFIED (Grant 2026-07-11).** Landed via the **D1 batch** (the five clauses (a)–(e);
    board Continuation-2 §6 `_orchestration/2026-07-10_orchestration-board.md:199-209` is the PROPOSED origin).
    The δ_strain prose reconcile rides the same batch.
16. **D-V — HELD for the weekend (Grant).** Letter **v6 confirmed in good state** (round-4 closed, #625; second
    validation all-PASS; OTS chain intact); task **#41 (comment-strip) stays gated** on the submission call.

### Docket status board — Grant-input-round state (KEEP-BOTH; tables above unedited)

| Item | What | Status (2026-07-11 input round) | Owner / next |
|---|---|---|---|
| R-A Kerr-cell | DC/AC canon-cell circuit analysis | **WALK-CONTINUES** — K1/K2 = MODIFIED-CIRCUIT proposals, canon cell has one scalar V | Grant response pending |
| Free-fall | elevator-form gut-check | **WALK-CONTINUES** | Grant response pending |
| Discrete-solve | framing | **RULED** — drop media-taxonomy, BC-first | implementer (BC-first arc) |
| R-C | (2,3) 1/(2π) locus | **RULED-TO-TEST** — REMEMBER vs RELAX, vertex-transient discriminator | arc candidate, undispatched |
| R-D / W1 | uniform-Z₀ far-field match | **CANDIDATE RESOLUTION** — same statement as doc-34 Γ²=0; not yet closed | doc-34 wording pass owed |
| T3 | electron-cage vs node-rupture Γ=−1 | **RULED-IN-SHAPE** — KEEP-BOTH SPLIT (lossless vs fuse-class) | final wording awaits A4 verdict |
| T6 | mass→inductance M-row | **RULED** — A1 ownership; M-row = TKI image | executed in D1 batch |
| u₀* split | cut/cycle homonym | **RULED** — WAIT (model-conditional); flag rides T12 | D1 rider (flag-not-split) |
| T13 | protein scope | **PARKED** — worry later | — |
| T15 | S₁₁ invariant | **NOT OPENED** — parked behind T13 | — |
| Astro sweep | adjudicator sweep | **GO** | Grant launches |
| Collapse batch | fire-ready subset | **GO** — D1 brief | Grant launches |
| #40 CVR bench | held-DC-E bench walk | **WAITS** — after keying adjudicators | Grant-confirmed |
| C13b | bullet-cluster run | **GO** — D2 brief (γ-adjudication stale-gate flagged) | Grant launches |
| Precision house rule | reporting hygiene | **★RATIFIED** — landed via D1 | done via batch |
| D-V | Letter submission | **HELD (weekend)** — v6 good; #41 gated | Grant + Keith + Benn |

---

*Cross-refs: D1 collapse batch `_orchestration/2026-07-11_collapse-batch-handoff.md`; D2 C13b run
`_orchestration/2026-07-11_c13b-bullet-cluster-run-handoff.md`; the astro sweep
`_orchestration/2026-07-11_astro-adjudicator-sweep-handoff.md`; the orchestration board Continuation-2 §6
(precision house rule PROPOSED origin); the R-B framing note `research/2026-07-10_rb-fossil-walk_framing.md` §3
(u₀* homonym flag); the X40 result `research/2026-07-10_x40-ring-closure-transient_result.md` (both cut/cycle
nonzero within the model). Every cross-ref verify-before-cite'd; this continuation records queue-state, not
adjudicated physics.*

---

## Continuation — 2026-07-11 (X43 ringdown-port GO)

**X43 ringdown-port arc: GO (Grant 2026-07-11)** — brief at `_orchestration/2026-07-11_x43-ringdown-port-handoff.md`; frozen bins ω⁵/ω³/ω¹/no-law; A0 dimensional-`L` pre-gate severable; the program's first forward-form derivation attempt of the testing pivot.
