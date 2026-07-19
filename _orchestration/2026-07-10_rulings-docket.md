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

---

## Continuation — 2026-07-11 (four-lane returns + cross-lane reconciliations)

Docket state after the day's four Grant-launched satellite returns: **#643** astro-adjudicator sweep, **#646** collapse batch, **#647** X43 ringdown-port (all MERGED, HEAD `600db255`) + **#645** C13b bullet-cluster (OPEN at write time). **KEEP-BOTH:** the four continuations above + the original docket and status boards are **not edited**; this continuation carries the four-lane state and the cross-lane reconciliations. The **astro-sweep docket stub** (`_orchestration/2026-07-11_astro-adjudicator-sweep_docket-continuation-stub.md`) is **folded in** here (§A) and **marked superseded-by-this-section** (a pointer header lands on the stub; its body preserved per KEEP-BOTH). Every PR#/cite/SHA below was git/gh/grep-confirmed this session (verify-before-cite). Nothing here canonizes; substrate claims are records of the lanes' verdicts + the queue-state, not new assertions.

### §A — Astro-sweep rows folded in (from the #643 stub; suggested row-letters assigned canonical ids here)

The stub's five suggested rows (`T4`, `T3`, `G-WHEN`, `G-Ġ`, `CH-c`) fold in verbatim-in-substance below; source `research/2026-07-11_astro-adjudicator-sweep_result.md`, freeze `research/2026-07-11_astro-adjudicator-sweep_branch-signature-map_FROZEN.md` (`8bbb0ef1`, pushed pre-retrieval). Every row is `PENDING-GRANT` — the sweep recommends, Grant rules. **★ Note the T4 and G-WHEN rows are then modified by the §B cross-lane reconciliations** (X43-A0 retires T4's tide sub-branch; the WHEN posture is fixed).

| Ruling | What | Status (2026-07-11, astro sweep) | Adjudicator |
|---|---|---|---|
| **T4** | MOND EFE keying (internal / total / **tide**) | **NO CALL (contested)** — Chae 2020/2021 EFE 8–11σ (`:41`) vs Sargent-2025 confounding vs Desmond-2023 "weak"; strain symmetric with ΛCDM. Sweep froze **KEEP ALL THREE BRANCHES** (data-side; **★ superseded on the tide sub-branch by §B**). The `g_ext`-vs-`∇g_ext` discriminator T4 turns on **has never been run** (`:47`). | astro A1/A2 → Grant on the keying decision |
| **T3** | Γ=−1 short-vs-fuse loss-character (horizon) | **NO CALL (contested); OPEN** — echo axis disputed (Abedi/Afshordi vs Westerweck, method-driven). **★ Branch-(ii) is observationally GR-degenerate — no AVE-distinct chord at the horizon.** Do NOT demote branch-(i) on the wide-CI absorption bound. Revisit on O4/O5 echo searches. | astro A4 → Grant on loss-character |
| **WHEN** *(stub `G-WHEN`)* | `a₀` live-keyed (`∝H(z)`) vs attractor-keyed (redshift-constant) | **LEANS LIVE** (retrieval-limited) — Ciocan 2026 (`arXiv:2604.22613`) direct `a₀(z)` fit RISES (`2.38±0.1×10⁻¹⁰` at `z≈1`, ratio ≈1.98 vs `H(z=1)/H₀≈1.76`), single-group/unreplicated (`:108,:120,:121`). Attractor (`derived-mond-acceleration-scale.md:15`) = **DATA-STRAINED / demotion-candidate, NOT retired**; frozen in canon until an independent-group `a₀(z)` corroborates. (**★ posture fixed in §B**.) | astro A3 → Grant on the WHEN key |
| **G-Ġ** *(stub booking row)* | naive-live / flatness-live / fossil / attractor vs `Ġ` bounds | **BOOKED** — LLR (`≲1.5×10⁻¹³/yr`; verified brackets `3.8×10⁻¹³` 2010 / `9.6×10⁻¹⁵` 2021) + pulsar + BBN **demote naive-live G ~190–7600×** (`:208,:213`). Survivors: flatness-protected-live + attractor + fossil (fork **UNRESOLVED**). Flatness-`Ġ` self-cancellation derivation = out-of-scope theory item (owed). | astro A6 (books bounds) → Grant on the fork |
| **CH-c** *(stub booking row)* | shear + EM ride one substrate `c` | **BOOKED — passes.** GW170817 (`arXiv:1710.05834`) `(c_gw−c)/c ∈ [−3×10⁻¹⁵, +7×10⁻¹⁶]` verifies the external bound flagged at `research/2026-06-11_chiral-vacuum-reactor-framing.md:393` at `10⁻¹⁵` (`:170,:180`). **Brief-side correction: upper bound `+7×10⁻¹⁶`, not `+7×10⁻¹⁵`** (frozen map said `~10⁻¹⁵`, correct order). | astro A5 (books bound) → Grant |

### §B — Cross-lane reconciliations (the four-lane crossings)

- **T4 keying — the tide sub-branch is RETIRED (theory-side kill; KEEP-BOTH the two verdicts + the ordering).** X43's Appendix A0 (`research/2026-07-11_x43-A0-tide-dimensional-L_result.md`) ran the dimensional kill-test: **there is no canon-chain-forced galactic-scale length `L`** for a tide-keyed (`∇g_ext`) Axiom-4 kernel — the only forced macroscopic length is the de-Sitter horizon `R_H`, which places the MOND transition at cosmological scale, ~5 OOM too long (`:53,:59,:73`). **Verdict: the §4 tide `∇g_ext` third branch DIES AT BIRTH** (`:73`). **KEEP-BOTH — record both verdicts + the ordering:** the astro sweep froze **"NO CALL / KEEP ALL THREE BRANCHES / do NOT demote tide"** (data-side) in a **parallel lane, pre-A0** — it says the *data* cannot decide; A0's **theory-side dimensional kill** says there is *no tide branch to keep* regardless of the data, and **supersedes** the frozen data-side "don't demote" on the tide axis specifically. The two are not in conflict: data-can't-decide ∧ theory-forbids-the-branch ⇒ the branch retires on the theory side. **Consequence:** T4 collapses from a three-branch to a **TWO-branch map (internal-only `g_N` vs total local field)**, both still **data-contested** (A1/A2 NO-CALLs; A0 leaves the surviving pair *unaffected* — both are acceleration-keyed and need no length, `:73`). The **never-run `g_ext`-vs-`∇g_ext` separation test DEMOTES** from an AVE-distinct forward-prediction opener to a **generic MOND-EFE discriminator** — its AVE motivation died with the tide kernel. **PENDING-GRANT** on the surviving two-branch keying (fold with **R-A**, shared `S(A)`-keying axis).

- **WHEN axis — posture fixed: lean live tentatively, attractor derivation stays FROZEN.** The first real datum (Ciocan 2026, `arXiv:2604.22613`) **LEANS LIVE**. Posture per the sweep recommendation: **key the WHEN axis to LIVE tentatively**; the attractor derivation `a₀ = cH_∞/2π` (`derived-mond-acceleration-scale.md:15`) **stays FROZEN in canon until an independent-group `a₀(z)` replication corroborates the rise** (a single unreplicated paper does not book a canonical-axis demotion). Live confirmed in **direction only** — Ciocan fits `a₀(z)=a₀(0)+a₁z` (linear-in-`z`), NOT `∝H(z)`, so **do not upgrade to a strict functional-form confirmation** (`:120`). **Forward note:** a confirmed live-keying eventually requires **re-keying the `a₀` derivation to `H(t)`** (the attractor's redshift-constant form would then be the demoted branch). **PENDING-GRANT** on the WHEN key.

- **T3 — A4 gives no horizon chord; the electron≠node split proceeds on internal grounds.** A4 reported **no AVE-distinct chord at the horizon** (branch-(ii) GR-degenerate — echo data cannot adjudicate the Γ=−1 loss-character). Grant's **electron≠node KEEP-BOTH SPLIT** (docket item 6 above: electron-cage `Γ=−1` lossless TIR vs past-yield node-rupture fuse-class) therefore **proceeds on internal grounds** — A4 supplies no external constraint either way. The **thrust/decay bench relabels remain queued** on the split's final wording (which was gated on the A4 verdict; A4 has now reported, so the wording pass is unblocked, benches still queued). **PENDING-GRANT** on final wording.

- **X43 drain fork (NEW row).** The X43 result lands **CONTESTED between two negative bins** (`ω³` dipole-death vs no-law/wrong-sign above-band) separated by **ONE unadjudicated corpus question** (`research/2026-07-11_x43-ringdown-port_result.md:62,:67`): **is the neutrino V-sector drain a band-limited srs Cosserat channel** (band top `≤17 ω_C` → `ρ_drain(ω_μ)=0` → **no-law / wrong-sign**) **or a genuine non-lattice longitudinal-scalar continuum** (no cutoff → a **would-be `ω³`**, but with an uncomputed trans-Nyquist emitter-drain overlap form factor)? A **sector-ownership call** — surfaced, not fiat-resolved (substrate-adjudicates-forks). **PENDING-GRANT.**

- **WALK-BACK QUEUE (two new flags, both Grant-gated; flag-don't-fix — surfaced, not resolved in-lane):**
  1. **ch14 leaky-cavity decay leaf (`clm-c54kdd`)** — the canonical decay leaf `manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md` models the muon as **continuous above-yield RC-discharge breakdown** (`R_eff` `1 GΩ → 50 Ω`, half-life from standard RC time constants, `theory.md:46,49,53`). But a continuous 50 Ω breakdown gives **`Q ~ 1`**, whereas the observed lifetime is **`Q_μ ≈ 3.5×10¹⁷`** cycles — **~17.5 OOM** longer than a bare breakdown allows (`research/2026-07-11_x43-ringdown-port_result.md:80`). The high `Q` forces the nearly-closed-port reading; a reconciliation is available (the breakdown is the *rare terminal jump*; its low duty cycle IS the nearly-closed port / high `Q`), but the "continuous rupture → RC-discharge" model is **quantitatively wrong on the lifetime as written**. Flagged by X43; recommend a Q-consistency walk-back on `ch14` + the two `Γ=−1` shatter leaves.
  2. **`dm-mechanism-unification.md` cluster limb "qualitatively CONFIRMED"** (`:52-64`; §3 limb-(ii), `:64` / summary `:154`) — candidate re-scope to **"quantitatively misses under the derived source"**: C13b (#645) found the mechanism's own derived source (`η_eff` on `M_*+M_gas`) puts the lensing peak ON THE GAS (Δ = −145 kpc, −4.8σ) vs the observed 150–194 kpc; the stars-only HIT rests on the UNDERIVED source the ledger already grades **0.40 "matched-by-construction"** (`vol1/claim-quality.md:479-480`). **Rides Grant's Q1/Q2** (star-vs-gas source fork; re-scope wording) — do not land the header until Q1/Q2 rule.

- **MISS-LEDGER — BOOKED 🔴 *[Grant "classify and book" ruling 2026-07-13; increments no longer gated]*** (was: *Grant-gated candidates; hopeful-interior-mechanism ledger*).
  - **X43 ringdown-port → BOOKED as increment 8 (ledger → 0-for-8)** — the 6th convergence-shaped move of the register arc; paid to kill and failed (the port is real but forces `ω³`/no-law, not Sargent `ω⁵`). **Grant-ruled class: frozen-form miss** — the ringdown-port picture is retired (`research/2026-07-11_x43-ringdown-port_result.md:87`).
  - **C13b cluster-halo source → BOOKED as increment 9 (ledger → 0-for-9)** — ~~classification call is Grant's: **hopeful-interior-mechanism** vs **a separate class** (a source-fork MISS); increment gated on the classification~~ → **Grant-ruled 2026-07-13: forward-prediction miss, honest liability standing** (−4.8σ, **kernel-independent** — η_eff dormant in the core). Booked into the ledger as a distinct *forward-prediction* class (NOT an interior-mechanism over-fit) (`research/2026-07-11_C13b_bullet_cluster_result.md`).
  - **Ledger now reads 0-for-9 (BOOKED).** Supersedes the prior "stays 0-for-7 / increments pending" reconciliation flag (see the status-board + convergence-flags notes below; canonical home `manuscript/ave-kb/common/program-arc-map.md:404`, booked this session).

- **STANDING ITEMS — unchanged.** **R-A** Kerr-cell + free-fall gut-checks + the K1-vs-standing-canon walk (fold with T4 per the shared `S(A)`-keying axis); **R-C** (2,3) `1/(2π)` REMEMBER-vs-RELAX vertex-transient; **#40 CVR bench** (two-config requirement recorded, walk after the keying adjudicators report); the **discrete muonic eigencavity solve** (BC-first framing, gated on Grant's which-two-liquids + barrier-vs-crossover answers); **D-V** Letter submission (weekend, Grant + Keith + Benn). None edited by this continuation.

### Docket status board — four-lane-returns state (KEEP-BOTH; tables above unedited)

| Ruling | What | Status (2026-07-11 four-lane returns) | Adjudicator |
|---|---|---|---|
| **T4** | MOND EFE keying | **TIDE SUB-BRANCH RETIRED** (X43-A0 dimensional kill, theory-side; KEEP-BOTH the frozen data-side "don't demote"); now **TWO-branch map** (internal-`g_N` vs total-field), both data-contested; `g_ext`-vs-`∇g_ext` test demoted to generic MOND-EFE discriminator | Grant (fold with R-A) |
| **WHEN** | `a₀` live vs attractor | **LEANS LIVE** (Ciocan 2026); lean live tentatively, attractor derivation FROZEN until independent replication; live-keying eventually re-keys `a₀` to `H(t)` | Grant on the WHEN key |
| **T3** | Γ=−1 horizon loss-character | **A4 = no AVE-distinct chord at horizon** (branch-(ii) GR-degenerate); electron≠node split proceeds on internal grounds; bench relabels queued on final wording | Grant (final wording) |
| **X43 drain fork** | neutrino drain: Cosserat band vs longitudinal continuum | **NEW · PENDING-GRANT** — the single sector-ownership question separating the two negative bins (`ω³` vs no-law) | Grant (sector ownership) |
| **Walk-back: ch14** | `clm-c54kdd` RC-discharge `Q~1` vs `Q_μ≈3.5×10¹⁷` | **NEW FLAG · Grant-gated** (~17.5 OOM; X43-flagged) | Grant |
| **Walk-back: dm-unification** | cluster limb "qualitatively CONFIRMED" | **NEW FLAG · Grant-gated** (re-scope candidate; rides Q1/Q2) | Grant |
| **Miss-ledger** | ~~X43 → 0-for-8; C13b → cand. 0-for-9~~ **BOOKED 0-for-9** (X43 = incr. 8 frozen-form miss; C13b = incr. 9 forward-prediction miss) | **★ BOOKED (Grant "classify and book" 2026-07-13)** — increments no longer gated | Grant (ruled) |

---

*Cross-refs (verify-before-cite'd this session): the astro-sweep result + frozen map + folded stub; `research/2026-07-11_collapse-batch_result.md`; `research/2026-07-11_x43-ringdown-port_result.md` + `research/2026-07-11_x43-A0-tide-dimensional-L_result.md`; the C13b handoff `_orchestration/2026-07-11_c13b-bullet-cluster-run-handoff.md` (run result lands on #645 merge); the board Continuation 3 (four-lane day). KB cites: `vol1/claim-quality.md:479-480`, `dm-mechanism-unification.md:52-64/:154`, `derived-mond-acceleration-scale.md:15`, `ch14-leaky-cavity-particle-decay/theory.md:46,49,53`. Every cross-ref grep/Read-confirmed; this continuation records queue-state, not adjudicated physics.*

---

## Continuation — 2026-07-11 (A7 adjudicator + EP-CMRR instrument frame + gut-check status)

Three rows from the 2026-07-11 core-planning close, staged with the engine-refresh
handoff PR (`_orchestration/2026-07-11_engine-refresh-handoff.md`). **KEEP-BOTH:**
the four 2026-07-11 continuations above + the original docket and status boards are
**not edited**; this continuation is append-only. Nothing here canonizes; substrate
claims are records of Grant's rulings + the queue-state, not new assertions. The T4
two-branch state (internal-`g_N` vs total-field, tide sub-branch retired) is carried
forward from the four-lane continuation §B (verify-before-cite'd there).

- **A7 (NEW adjudicator row, Grant GO 2026-07-11 "both depending on strain").**
  Solar-system SEP / Nordtvedt vs **BOTH surviving T4 branches** (internal-only
  `g_N` AND total-local-field) — each branch's predicted SEP-violation computed
  **AT THE LOCAL OPERATING STRAIN** (dormancy-honest: the solar system sits
  ~1e8×`a₀`, deep-Newtonian, the Axiom-4 kernel ~dormant — the C13b core-dormancy
  lesson; the leading observable is therefore the **external-galactic-field-induced
  quadrupole class**, not an internal-source residual). Compared against
  **LLR-Nordtvedt (~1e-4 SEP-CMRR)** + planetary-ephemerides bounds. **Kill-tests
  both directions:** a branch predicting an above-bound residual **DIES**; both
  clearing = **honest no-discrimination** (record it, do not manufacture a
  chord). Mixed retrieval + derivation lane; **queued for the next sweep round.**
  Adjudicator: Grant (fold with **R-A** / **T4** per the shared `S(A)`-keying axis).

- **EP-CMRR instrument frame (Grant GO a+b).** The equivalence principle recast
  as coupling-level common-mode rejection. Two landings ride the engine-refresh
  PR: the **register row → engine-refresh U6** (`translation-circuit.md` §4:
  EP ↔ coupling-level CMRR; WEP-CMRR ~1e-15 Eötvös/MICROSCOPE, SEP-CMRR ~1e-4
  LLR-Nordtvedt; DISTINGUISHED from the ε-sector gauge rider = readout-level
  CMRR, `vol4/claim-quality.md:1856`); the **engine acceptance test →
  engine-refresh U5** (the differential-pair certify-and-expose test on the
  Master-Equation medium). **Framing = instrument language with named
  kill-tests, 10th convergence-flagged, NOT a physics claim** (it certifies the
  instrument + exposes the installed keying's EP-status per the X36
  install-tautology; it does not adjudicate T4). Adjudicator: Grant.

- **Gut-check status.**
  - **(a) junction** — Grant's small/large-signal reframe **confirmed the canon
    mapping is exact**: the SPICE `.OP → .AC` axis maps to **M1 / M3** (the
    DC-operating-point DC-short series-L = #547-M1; the AC small-signal tangent-`C`
    at the operating point = #547-M3; cross-ref the Grant-input-round item 1
    above). **Formal ruling still OPEN; the lean is recorded** (canon mapping
    exact, K1/K2 remain MODIFIED-CIRCUIT proposals not readings of the canon cell).
  - **(b) infinite-CMRR gravity — REFRAMED.** The "infinite by identity" holds at
    the **WEP level** (gravitational charge ≡ inertial mass = composition
    independence; nothing to mismatch). But **both surviving T4 branches require a
    FINITE SEP-CMRR** — a *measurable* self-energy / Nordtvedt violation (the two
    are not in tension: WEP-composition-CMRR infinite ∧ SEP-self-energy-CMRR
    finite). The open question is therefore **whether A7's strain-honest
    residuals clear the LLR-Nordtvedt + ephemerides bounds.** Formal ruling OPEN.

### Docket status board — A7 + EP-CMRR + gut-check state (KEEP-BOTH; tables above unedited)

| Ruling | What | Status (2026-07-11) | Adjudicator |
|---|---|---|---|
| **A7** | solar-system SEP/Nordtvedt vs BOTH T4 branches, at local operating strain | **NEW · queued for next sweep** — dormancy-honest (~1e8×a₀, quadrupole-class leading obs); kill-tests both directions; both-clear = honest no-discrimination | Grant (fold with R-A/T4) |
| **EP-CMRR frame** | EP ↔ coupling-level CMRR (register row U6 + acceptance test U5) | **GO (a+b)** — instrument language + named kill-tests, 10th convergence-flagged, NOT a physics claim | Grant |
| **Gut-check (a) junction** | small/large-signal canon mapping | **LEAN RECORDED** — .OP→.AC = M1/M3 exact; formal ruling OPEN | Grant |
| **Gut-check (b) infinite-CMRR gravity** | WEP-infinite vs SEP-finite | **REFRAMED** — WEP-CMRR ∞ by identity, SEP-CMRR finite/measurable; clears-bounds question = A7 | Grant |

---

*Cross-refs (verify-before-cite'd this session): the engine-refresh handoff
`_orchestration/2026-07-11_engine-refresh-handoff.md` (U5 test / U6 register row);
the four-lane continuation §B (T4 two-branch state, tide sub-branch retired) + §A
(T4 keying row); the Grant-input-round item 1 (junction small/large-signal walk);
the X36 install-tautology `research/2026-07-09_x36-node-bottleneck_result.md:54,89,215`;
the gauge-rider site `manuscript/ave-kb/vol4/claim-quality.md:1856`. This
continuation records queue-state, not adjudicated physics; nothing here canonizes.*

---

## Continuation — 2026-07-11 (THE ONE-EP CARVE + engine-derived η)

**THE ONE-EP CARVE (Grant-walked 2026-07-11, supersedes the two-principle WEP/SEP
presentation — KEEP-BOTH, the U6 register row stands as-is with a possible post-η
refinement as a gated follow-on):** the equivalence principle is ONE identity (one
energy ledger: gravitates = resists), probed per-REGISTER — knot-localized energy
(WEP: vary composition; infinite by identity) vs strain-field-distributed energy
(Nordtvedt: vary the field fraction f; η now ENGINE-DERIVABLE via the landed
backreaction solver — this arc) — plus the REGIME DIAL (ambient-strain operating
point: "environment-dependence" is bias-point physics of a nonlinear medium, NOT
principle-breaking — a lattice never promised local-position-invariance, it promised
one ledger). RAIL (binding): the reframe changes zero bounds — LLR/ephemerides bind
regardless of vocabulary; and η=0 is itself a RISKED prediction (η≠0 would be a real
two-ledger finding). CONSEQUENCE: A7's freeze waits on the η result; if η=0, A7 = the
EFE-quadrupole channel alone. Seduction note: the reframe ships with its own risked
test (this arc), 11th-convergence-flagged.

- **η RESULT (engine-derived, this arc — `analysis/nordtvedt-eta`).** The Nordtvedt
  register (register-2, strain-field self-energy) certified **η = +8.3×10⁻⁵**
  (< 1×10⁻³) across f ∈ [0.024, 0.060], driving the landed #86 backreaction solver
  as-is (Rule-14). **CERTIFICATION-class** — η=0 is ENTAILED by the single-`T₀₀^total`
  Gauss construction (P10 / X36 install-tautology); the value is converting **A7's
  Nordtvedt leg from a retrieval ASSUMPTION into an engine-CERTIFIED prediction.**
  **BANKING BASIS = the analytic entailment, NOT the numeric leg** (adversarial-review
  R1): the numeric instrument is RESOLUTION-LIMITED — clean N=32/40 slopes are −6.5×10⁻⁴
  / −4.7×10⁻⁴ (at/above the LLR bound 4.4×10⁻⁴; N=24 +8.3×10⁻⁵ is unresolved noise,
  se~8.9×10⁻⁴), so the numeric leg alone cannot certify the LLR null; it is consistent
  with the entailment (N=40 |η| < N=32 ⇒ slow convergence to 0). Detector teeth: the
  mixed-register leg is SOLVER-FED (η=2.28); the P11 ε=0.10→0.0999 arm is SYNTHETIC
  ledger-injection-recovery. Result doc `research/2026-07-11_nordtvedt-eta_result.md`
  (§4a convergence table + §9 deviation ledger); frozen prereg
  `research/2026-07-11_nordtvedt-eta_prereg_FROZEN.md`; test
  `src/tests/engine_acceptance/test_nordtvedt_eta.py`.
- **A7 ordering (per the CARVE consequence).** With η certified null, **A7's
  Nordtvedt leg = a derived-null consistency channel** and A7 reduces to the
  ephemerides / EFE-quadrupole channel alone; **A7's branch-signature freeze should
  POSTDATE this η result.**
- **FLAG — a LATENT #86 DEFECT EXPOSURE (flag-don't-fix; surfaced, Grant/auditor to
  adjudicate; adversarial-review R6/R8).** (1) The binding-deficit `M_eff = M − U_bind`
  is the engine's OWN-DESIGNATED inertial/ADM mass (`backreaction.py:33`), yet the far
  field provably reads M + U_bind (the +u_field source ADD, `backreaction.py:303-304`);
  so the as-built engine's far field disagrees with its OWN designated ADM mass at
  O(2f), and η_mixed=2.28 IS that statement. #86 never reconciled the two (sign-agnostic
  ratio/shape checks; result doc :339) — this arc is the FIRST reconciliation and it
  FAILS. NOT a free convention choice. Resolution **★RULED (c) — Grant 2026-07-12**,
  reading his own 2026-06-29 ruling ("positive strain energy … already accounted in the
  down-regulated frequency"): a THREE-WAY (KEEP-BOTH, all recorded) — {keep-ADD · bare
  −u_field (Picard source sign-indefinite) · **★RULED REDSHIFT/KOMAR-weighted
  `T₀₀^matter`** → far field reads the deficit mass, reconciling with `M_eff`}.
  **Follow-on engine arc NAMED + AUTHORIZED: X44 Komar-source reconciliation** —
  implement the ruled weighting in `backreaction.py`, re-run the #86 gate suite +
  GR-recovery checks + the η family + the mixed-register reconciliation (**η_mixed → 0
  expected but GENUINELY FIREABLE**: whether the ruled clock-weighting deficit equals
  `U_bind` at leading order is a real derivation risk, not bookkeeping) + an
  η_mixed-vs-N convergence gate (the R1 lesson); engine modification, own prereg, fires
  **AFTER #651 merges** (Rule-14 — NOT this PR). (2) The U6 register row
  (`translation-circuit.md:148`) "nonzero mismatch / both T4 branches REQUIRE a finite
  value" wording is in tension with the certified η=0 one-ledger prediction — **U6
  stands as-is (KEEP-BOTH), post-η refinement gated; the auditor lands any U6 edit.**

### Docket status board — ONE-EP carve + η (KEEP-BOTH; tables above unedited)

| Ruling | What | Status (2026-07-11) | Adjudicator |
|---|---|---|---|
| **ONE-EP carve** | one identity, two registers (knot/WEP · strain-field/Nordtvedt) + regime dial | **WALKED (Grant 2026-07-11)** — supersedes two-principle WEP/SEP; KEEP-BOTH U6; 11th-convergence-flagged | Grant |
| **η (Nordtvedt register)** | engine-derived η via #86 backreaction solver | **CERTIFIED η≈0 by ENTAILMENT** (`analysis/nordtvedt-eta`) — certification-class; numeric leg RESOLUTION-LIMITED (N=32/40 ~5–6.5×10⁻⁴, at LLR scale); banking = entailment | Grant (accept via PR) |
| **A7 ordering** | Nordtvedt leg vs EFE-quadrupole channel | **η=0 ⇒ A7 = EFE-quadrupole alone**; A7 branch-signature freeze POSTDATES η | Grant (fold with R-A/T4) |
| **M_eff-vs-far-field gap** | LATENT #86 DEFECT: far field (M+U) vs engine's OWN designated ADM mass M_eff (M−U), O(2f) | **★RULED (c) — Grant 2026-07-12** (Komar/redshift-weighted T₀₀ source; three-way KEEP-BOTH); follow-on arc **X44** implemented on `analysis/x44-komar-source` — **frozen bin (iii) UNRECONCILED** (η_mixed≈+1.05 at N=24/32/40; Δ_clock≪U_bind; no √S retune). Komar installed as default; ADD KEEP-BOTH. Escalation options in `research/2026-07-12_x44-komar-source_result.md` §7 | Grant (RULED; adjudicate bin-iii escalation) |
| **X-LEDGER (X44 outcome)** | √S-weighted flux mass vs \(U_{\rm bind}\) ledger | **★RULED X-LEDGER — Grant confirmed 2026-07-13** (effective condition met: #661 merged; KEEP-BOTH superseded phrasing: "★PROPOSED-RULED X-LEDGER (text pending Grant confirmation — stamps become effective on his merge of #661)") — bank #652 bin (iii) UNRECONCILED; two substrate mass functionals named open; no silent √S retune; merge only as banked negative ([`2026-07-12_ave-native-rulings_g-persist_x-ledger.md`](2026-07-12_ave-native-rulings_g-persist_x-ledger.md)). *(Merge-resolution 2026-07-12: this X-LEDGER row is the SURVIVOR of the X44-firing event; the duplicate "X44 Komar-source" row that arrived via #652's merge was dropped per the pre-declared #652/#661 docket resolution — one event, one row.)* | Grant (RULED — confirmed 2026-07-13) |
| **G-PERSIST (genesis D1–D4)** | Fixed-N lasting localization vs node birth | **★RULED — CONFIRMS bin (ii) A-WEAKENED (Grant confirmed 2026-07-13, in-chat)** — bank #655 bin (ii); remanence (R10-class) before node-mint; KEEP-BOTH; no `genesis_v{N}` ([ruling leaf](2026-07-12_ave-native-rulings_g-persist_x-ledger.md)). **Evidentiary basis:** the #670 N≥14 battery's **boundary-insensitive φ-dispersion** — φ collapses **0.87→0.73→0.51** as N grows (10→14→16, `pair`) under PML = boundary-clean non-persistence; the E-recovery (0.69→0.84→0.87) confirmed the old N=10 collapse was **absorber leakage**, not physics (`research/2026-07-13_genesis-npersist-n14-battery_RESULT.md`). **THE ENCLOSURE FORK — ~~KEEP-BOTH-OPEN~~ 🔴 RULED READING A (2026-07-14, Grant in-chat):** the fork is **CLOSED toward Reading A (wake-feeding)**; **Reading B retired**. Data-confirmed via the #689 localization observable — **LOOP-FILLING** on **both statistics, both boundaries, register-robust** (`research/2026-07-14_gpersist-localization-observable_RESULT.md:160`; "Reading A CONFIRMED; the fork closes toward A"). **G-PERSIST ★RULED stamp untouched.** *The 2026-07-13 "KEEP-BOTH-OPEN / Reading A LEANED / Reading B OPEN" read that follows is the superseded prior status, preserved verbatim:* *Reading A (wake-feeding: the periodic-torus enclosure returns the pattern's own wake; the projection gauge counts laps)* **LEANED by Grant 2026-07-13**; *Reading B (genesis-under-confinement: genuine self-tightening)* stays **OPEN**; discriminator = the **spatial-concentration / participation-ratio localization observable** (KEEP-BOTH new axis, follow-on driver queued); **the flip does NOT depend on this fork (the PML φ-trend carries it).** KEEP-BOTH — superseded stamp read: *"★PROPOSED-RULED G-PERSIST (text pending Grant confirmation — stamps become effective on his merge of #661)"*; the "confirmation MUST postdate the #655 battery re-run" gate is **met** (the #670 re-run returned the boundary-clean φ-trend). The remanence-before-node-mint build-order directive's banked-fact basis is **CONFIRMED**, not moot. | Grant (★RULED — CONFIRMS) |

---

*Cross-refs (verify-before-cite'd this session): the frozen prereg + result doc +
test named above; the landed backreaction solver
`src/ave/gravity/backreaction.py` + `research/2026-06-29_grqed-stage3-backreaction_result.md:343`
(the SUBTRACT ruling); the X36 install-tautology
`research/2026-07-09_x36-node-bottleneck_result.md:54,89,215`; the U6 register row
`manuscript/ave-kb/common/translation-tables/translation-circuit.md:148`; the A7 row
(this docket, 2026-07-11 continuation §A7). This continuation records queue-state +
one engine-derived result; the η certification is banked via the result doc, and A7 /
U6 adjudication remains Grant's. **Addendum 2026-07-12:** G-PERSIST + X-LEDGER **★PROPOSED-RULED** in AVE-native register (remanence-before-mint; bank mass-ledger unreconciliation) — text pending Grant confirmation; stamps become effective on his merge of #661 (repair R3). KEEP-BOTH: superseded prose read "ruled in AVE-native register".*

---

## Continuation — 2026-07-13 (the registers walk)

Core-session planning walk (post-compaction). Full framing record: `research/2026-07-13_registers-walk_framing.md` (FRAMING NOT DERIVATION; nothing canonized). The walk ratified the build order, answered Q1/Q2 in-walk, and Grant reframed Q3 into a **cascade-filter ontology**; Q4 stays open pending his go. Two Grant ontologies (transducer, cascade filter) are recorded as **ruling-grade inputs** to the X44b / F6 charters.

| Item | What | Status (2026-07-13) | Adjudicator |
|---|---|---|---|
| **PLAN OF RECORD** | build order **registers (T_ij + depletion) → X44b → F6** | **★ RATIFIED (Grant 2026-07-13)** — one materialization build discharges both registers' shared flux-object debt before the sector charters fire (`research/2026-07-13_registers-walk_framing.md` §1) | Grant (ratified) |
| **Q1 — does the register carry the twist?** | full Cosserat asymmetric `σ` vs symmetric reduction | **★ RULED-IN-WALK (Grant 2026-07-13): carry the twist.** The angular handover at the envelope IS spin (couple-stress `σ^A`); a symmetric-only `σ` deletes spin from the stress ledger (`…registers-walk_framing.md` §3; `manuscript/ave-kb/common/trampoline-framework.md:87`) | Grant (ruled) |
| **Q2 — brace: pressure or force?** | is `brace → +3∫p` the intended derivation? | **★ RULED-IN-WALK (Grant 2026-07-13): the brace = ⟨Maxwell stress⟩ of the (2,3) winding at its own envelope.** `T_rr` is manufactured by the general `σ_ij` build as a special case, which also retries the inconclusive bind-sim (`…registers-walk_framing.md` §2c,§3; `research/2026-06-30_electron-portmap-derivation_result.md:250-254`) | Grant (ruled) |
| **Q3 — what distinguishes the diode?** | the depletion-primitive taxonomy | **★ REFRAMED by Grant (2026-07-13) to the CASCADE-FILTER ontology** — mechanisms A/B are the two coupling classes of a multi-stage stability cascade; electron = terminal pole, universe envelope = top port; stress differentials draw the stage boundaries. **Locus / stage ruling PENDING the vol9 circuit-mapping investigation `ww0giq5he`** (its firmed cascade-map lands as a follow-on addendum) (`…registers-walk_framing.md` §5) | Grant (locus pending vol9) |
| **Q4 — where does the depleted energy live?** | F6 sink + build order | **OPEN — PENDING-GRANT.** 4-element map + two-tier build (global two-reservoir ODE ledger — no `a(t)` evolver today — then one X40-class click); `ρ_latent` parameterization is the **Grant-gated go** (`clm-s4n33u` 0.45, input-only); CC-honest scope (existence+form of DE-tracks-matter only) (`…registers-walk_framing.md` §4) | Grant (go owed) |
| **TRANSDUCER ontology** | envelope = transducer between transverse-EM stress and lattice mechanical stress | **RECORDED (Grant-walked, ruling-grade input).** Matter `T_ij` = two coupled halves at the envelope interface; cycle-averaging is a Jensen magnitude, geometry-directed (never "kernel rectifies") (`…registers-walk_framing.md` §3) | Grant (input to X44b/F6) |
| **SYM-gravity forward statement** | the standing empirical exposure | **RECORDED.** Symmetric-saturation matched-impedance loading ⇒ **ZERO gravitational reflection + ZERO lensing birefringence** (lensing polarization-blind); any confirmed lensing polarization-dependence or reflection component kills the carve (`…registers-walk_framing.md` §6) | Grant / bench (kill-shape live) |
| **X44b (enriched)** | the gravity-source ladder | **ENRICHED — theorem-target added.** Bound transverse content's radiation EOS `p=u/3` ⇒ Tolman `(ρ+3p)` doubling = the same factor-2 as the derived light-deflection (`4GM`); a SOURCE-side target on the `η ≈ −1 → 0` ladder (`…registers-walk_framing.md` §3; `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md:26,28`) | Grant (fold into X44b charter) |
| **F6 architecture** | the depletion charter's shape | **RECORDED.** 4-element map (source `ρ_latent` / dest T2 / transducer=mass-envelope / door=off-line↔on-line) + three release mechanisms (A entropic / B `3H·ρ_latent` frontier-minting / C envelope-port DE-tracks-matter) + constraints (bias≠release; electron-no-drain) (`…registers-walk_framing.md` §4) | Grant (F6 charter) |

---

## Continuation — 2026-07-13 EOD (cascade adjudication RATIFIED + satellite verdicts)

The registers-walk section above recorded **Q3 REFRAMED** to the cascade-filter ontology with locus PENDING the vol9 investigation `ww0giq5he`. That investigation landed, three satellite drivers fired and MERGED (#668 / #669 / #670), and **Grant RATIFIED the cascade-kill in-chat (2026-07-13).** Full EOD framing record: `research/2026-07-13_registers-walk_framing.md` (CONTINUATION section — walk rounds 2–3; FRAMING NOT DERIVATION). Headline: the cascade-filter framing **has no distinct content at the atom rung** — the homogeneous vacuum line relabeled — **RATIFIED-KILLED.** **Nothing is canonized by this continuation.**

| Item | What | Status (2026-07-13 EOD) | Adjudicator |
|---|---|---|---|
| **T1-KILL** | atom-rung Q cascade gate | **★ RATIFIED (Grant 2026-07-13) — #668 MERGED.** Pre-registered kill FIRED, **bin (ii) NO-DISTINCT-VALUE**: `Q_wall→∞` α-free (electron intrinsic endpoint) for H(1s)/H(2s)/He⁺/reduced-mass; observed `~10⁷ = Q_rad = 4α⁻³` exact = transverse `Z_EM` radiative port (different sector, α-echo, bin (iii) rider). **TRUE-KILL** per the false-kill probe; positive control fired bin (i). Cascade-filter = "the homogeneous vacuum line relabeled — a vocabulary echo." (`research/2026-07-13_t1-atom-q-cascade-gate_RESULT.md`) | **Grant (★RATIFIED)** |
| **K-SWEEP** | srs vertex k-sweep backscatter (docket **T4** fork) | **LANDED — #669 MERGED. bin (i) HOMOGENIZATION-SPLIT.** σ=0.123 suppression, ρ=3.14 band-edge rise, disorder 0.500, chirality-blind 2×10⁻¹⁶; the **srs-`1/9` per-vertex ontology fork (T4) adjudicated** = real reactive event, homogenized for in-band collective carriers, resolves near the band edge (long-λ = suppressed *plateau*; **band edge not independently located** — probe reaches k·ℓ≤0.83). CONSISTENCY / peer-with-SM. (`research/2026-07-13_srs-vertex-ksweep-backscatter_RESULT.md`) | landed (peer-class) |
| **G-PERSIST** | genesis N≥14 persistence battery | **★RULED — CONFIRMS bin (ii) A-WEAKENED (Grant confirmed 2026-07-13, in-chat).** #670 MERGED. E recovers with N (0.69→0.84→0.87 = absorber-leakage confirmed) / φ collapses with N (0.87→0.73→0.51 = boundary-clean non-persistence); the enclosure `pml=0` config = **energy-closed-periodic (a torus, `np.roll` wraparound)** artifact-leaning (E≡1.0 conservation-identity, φ→10× N-stable). **STAMP FLIP DONE** (does not require the fork — the PML φ-trend is boundary-clean on its own). **THE ENCLOSURE FORK — ~~KEEP-BOTH-OPEN~~ 🔴 RULED READING A (2026-07-14, Grant in-chat):** the fork is **CLOSED toward Reading A (wake-feeding)**; **Reading B retired**. Data-confirmed via the #689 localization observable — **LOOP-FILLING** on **both statistics, both boundaries, register-robust** (`research/2026-07-14_gpersist-localization-observable_RESULT.md:160`; "Reading A CONFIRMED; the fork closes toward A"). **G-PERSIST ★RULED stamp untouched.** *The 2026-07-13 "KEEP-BOTH-OPEN / Reading A LEANED / Reading B OPEN" read that follows is the superseded prior status, preserved verbatim:* *Reading A (wake-feeding: the periodic-torus enclosure returns the pattern's own wake; the projection gauge counts laps)* **LEANED by Grant 2026-07-13**; *Reading B (genesis-under-confinement)* stays **OPEN**; discriminator = the spatial-concentration / participation-ratio **localization observable** (follow-on driver queued); the φ-channel-plant control is the second follow-on. (`research/2026-07-13_genesis-npersist-n14-battery_RESULT.md`) | **Grant (★RULED — CONFIRMS; fork KEEP-BOTH-OPEN)** |
| **Q3 (cascade reframe)** | the depletion-primitive taxonomy | **RESOLVED-BY-KILL.** The cascade reframe is killed at the atom rung ⇒ Q3 **reverts to the 4-element depletion map** (§4) with **F6 tier-1 as the adjudicator.** Charter MERGED #666; **DRIVER IN FLIGHT** (sibling lane `analysis/f6-tier1-ledger-driver`, Grant-GO'd). A/B survive as **F6 ledger bookkeeping**, not cascade coupling-classes. | resolved-by-kill (F6 adjudicates) |
| **CVR** | dielectric-C-V bench doc set | **DOC SET MERGED #667.** Trades **T-A / T-B / T-C OPEN** (T-D theory-ruled PLATES); the **CVR-DC mis-key fix IN FLIGHT** (`clm-vjv4zf` V_yield divergence keying + stale-OPEN + F1/F2/F3 staleness; sibling lane `docs/cvr-miskey-qladder-relabel-killed-ledger`). (`research/2026-07-13_cvr-trade-study_DECISIONS-OPEN.md`, `…cvr-requirements_DERIVED.md`) | trades open / fix in flight |
| **Q-ladder relabel** | atom-rung Q-ladder annotation | **GO — IN FLIGHT** (sibling lane, auditor-landed). Annotate the atom rung "radiative `Z_EM` port, α⁻³ echo; the *wall* loss-Q is the intrinsic endpoint `Q→∞`" so no downstream cite reads it as an independent cascade cutoff; BH endpoint stays canon + distinct (`Q=ℓ`). | GO (in flight) |
| **killed-ledger booking (12+13)** | seduction-ledger bookings | **GO — IN FLIGHT** (sibling lane). Convergence **12** (cascade filter) + **13** (power-factor `S=P+jQ` ordering) → the killed ledger. ~~Seduction ledger stays **0-for-7** booked; X43 / C13b increments pending Grant's miss-ledger gating (the earlier "0-for-8" walk-count counted a pending X43).~~ 🔴 *[RESOLVED — Grant "classify and book" 2026-07-13]* Seduction ledger **BOOKED 0-for-9**: X43 = increment 8 (frozen-form miss), C13b = increment 9 (forward-prediction miss); the earlier "0-for-8" walk-count was the pending X43, now booked as #8. *(This killed-ledger row is a distinct instrument from the miss-ledger — the 12/13 killed-convergence bookings are unaffected.)* | GO (in flight) |
| **D3 COEXIST ruling (2026-07-09) — census stress-test** | the imposed-cavity mode-census arc REGISTERED (Grant 2026-07-13) as a **STRESS-TEST of the ruled-COEXIST's two legs** with new evidence (**IDENTITY** leg: windings = boundary data; **ENVELOPE** leg: near-field = real yield envelope) — **NOT a re-opening of a closed fork.** D3 was RULED **COEXIST-with-justification 2026-07-09** (`_orchestration/2026-07-09_electron-def-canon-authoring.md:11,21`) and canonized (`electron-identification.md:57-62` + 3 further leaves). Census imposes a `Γ=−1` TIR closed surface of electron scale as a boundary-condition object; **SUSPICION under test** = the (2,3)-phase-winding ⊥ `0₁`-unknot duality is EMERGENT as the closure class of the cavity's reflection map. **The precursor-vs-end-state sub-fork (`clm-uatcql`, `vol2/claim-quality.md:1159`) stays explicitly OPEN — not silently resolved.** | **REGISTERED (Grant 2026-07-13):** two-shape KEEP-BOTH battery (sphere null vs horn-torus canon-lean); STAGE 1 census grounding LANDED (parallel to F6 driver); STAGE 2 self-consistency/balance audit rides the `T_ij` register (task #45); walk-first — nothing frozen yet; the **only outcome class that genuinely re-opens D3 territory** = a STAGE-2 balance failure requiring interior structure the singularity forbids. 🔴 *[CLOSED — Grant in-chat 2026-07-14, Ruling 4]* **D3 stress-test loop CLOSED: COEXIST stands, stress-tested** (LA freeze-fidelity RATIFIED, Ruling 4 — reading the LA fundamental = freeze-fidelity to "lowest interior mode", not a post-hoc target move); the census stress-tested the ruled-COEXIST's two legs and **did not break them**; the (2,3) **SELECTION is formally a DRIVEN / NONLINEAR question** (the cold-linear Hermitian lattice has **no winding to give** — confirmed both spectral ends). The precursor-vs-end-state sub-fork (`clm-uatcql`) stays **OPEN** — untouched by this closure. (`research/2026-07-14_cavity-census-stage1_RESULT.md:545-547`.) | Grant (census walk card next; D3 stress-test loop CLOSED 2026-07-14) |

**RATIFIED vs PENDING-GRANT (this continuation canonizes nothing):**
- **★ RATIFIED:** the **T1-KILL / cascade-adjudication** (Grant in-chat, 2026-07-13).
- ~~**PENDING-GRANT (his word genuinely owed):** the **G-PERSIST closed-box fork** ruling + the two **follow-on candidates** (localization observable, φ-channel plant) + the **docket stamp flip**.~~ 🔴 *[RESOLVED — Grant in-chat 2026-07-13]* **G-PERSIST ★RULED — CONFIRMS bin (ii) A-WEAKENED; docket stamp FLIPPED.** The **enclosure fork** is **KEEP-BOTH-OPEN** with **Reading A (wake-feeding) LEANED**; the two follow-on candidates (spatial-concentration / participation-ratio **localization observable**, and the **φ-channel plant** control) remain **queued** (driver not yet fired). *(Ontology correction folded in: the `pml=0` enclosure is a **torus** — energy-closed-periodic — not a reflecting box; see the RESULT torus erratum.)*
- **Landed / in-flight (no Grant word owed to book them):** K-SWEEP, CVR doc set, Q-ladder relabel, killed-ledger booking, F6 tier-1 driver, and **Q4 (F6 sink) — GO'd by Grant in-chat 2026-07-13**: the `ρ_latent` parameterization is **unlocked** (input-only, CC-honest scope), the tier-1 **charter MERGED #666**, and the tier-1 **DRIVER is IN FLIGHT** (`analysis/f6-tier1-ledger-driver`) — all merged-or-Grant-GO'd work, tracked here for docket completeness. *(The earlier registers-walk Q4 row above predates the go and is left as historical.)*
- **Registered (Grant-ruled, walk-first):** the **imposed-cavity mode-census arc** as a **STRESS-TEST of the ruled-COEXIST D3** (2026-07-09, canonized) — **NOT** a re-opening of a closed fork; STAGE 1 census grounding landed, STAGE 2 rides the `T_ij` register; the precursor-vs-end-state sub-fork (`clm-uatcql`) stays OPEN; nothing frozen — the arc's own prereg carries the bins later. 🔴 *[CLOSED — Grant in-chat 2026-07-14, Ruling 4]* the **D3 stress-test loop is CLOSED: COEXIST stands, stress-tested** (#692 LA freeze-fidelity **RATIFIED**, Ruling 4); the (2,3) **SELECTION is formally a DRIVEN / NONLINEAR question** (cold-linear lattice has no winding to give — non-(2,3) on both spectral ends); the census did **not** break either COEXIST leg. The `clm-uatcql` precursor-vs-end-state sub-fork stays **OPEN** — untouched by this closure.

> **Correction (2026-07-13, dated — KEEP-BOTH audit).** An earlier draft of the D3 row in this continuation mis-framed D3 as an *open / parked* core-ontology fork. **D3 was RULED COEXIST-with-justification on 2026-07-09** (`_orchestration/2026-07-09_electron-def-canon-authoring.md:11,21`) and **canonized at four leaves** (`electron-identification.md:57-62`; `substrate-perspective-electron.md:93-103,135-145`; `the-abandoned-interior.md:84-97`; `hollow-vortex-binding.md:28-37`). The imposed-cavity mode-census arc is a **STRESS-TEST of that ruling's two legs**, not a re-opening; the row above carries the corrected framing. The "SUPERSEDE or COEXIST" verbatim belongs to a *different* fork (`clm-i4p11y` — photon-precursor vs electron-end-state), whose precursor-vs-end-state sub-fork (`clm-uatcql`, `vol2/claim-quality.md:1159`) remains **OPEN**. All cites re-verified at HEAD.

**Convergence flags (this arc):** 10 (SYM/EP unification), 11 (one-door R-A/F6 — statics stable *because* release needs a topological event), 12 (cascade filter). Each carries a named kill-shape or investigation; none asserted as a win. Seduction ledger ~~stands at **0-for-7**~~ **stands at 0-for-9 (BOOKED — Grant "classify and book" 2026-07-13)**; canonical home `manuscript/ave-kb/common/program-arc-map.md:404`. 🔴 *[RESOLVED]* the prior ⚠ "0-for-8 walk-count vs 0-for-7 booked" reconciliation flag is now closed: the walk's "0-for-8" anticipated the X43 booking (now increment **8**, frozen-form miss); C13b books as increment **9** (forward-prediction miss) → **0-for-9**. **Downstream lag (flag-don't-fix, not edited here — out of this session's named scope + sibling killed-ledger lane touches it):** `research/2026-07-10_collapse-target-registry.md:23,64,317` still reads **0-for-7** (the pre-ruling booked value) and needs propagating to **0-for-9**. **All rows above are PENDING-GRANT where his word is still owed; nothing is canonized.**

---

## Continuation — 2026-07-13 (two Grant rulings: G-PERSIST ★RULED-CONFIRMS + F6 §5.4 BOTH)

Two in-chat Grant rulings landed 2026-07-13, propagated on `docs/gpersist-f6-rulings-propagation` (DO-NOT-MERGE; only Grant merges). **Nothing is canonized by this continuation** beyond the two stamps below; the F6 leaf claims are **not upgraded** (KEEP-BOTH throughout).

| Ruling | What | Status (2026-07-13) | Adjudicator |
|---|---|---|---|
| **G-PERSIST** | fixed-\(N\) genesis persistence (bin from #655/#670) | **★RULED — CONFIRMS bin (ii) A-WEAKENED (Grant confirmed 2026-07-13, in-chat).** Evidentiary basis = the #670 N≥14 battery's **boundary-insensitive φ-dispersion** (φ 0.87→0.73→0.51 as N grows under PML = boundary-clean non-persistence; E-recovery 0.69→0.84→0.87 confirmed the old N=10 collapse was absorber leakage). **THE ENCLOSURE FORK — ~~KEEP-BOTH-OPEN~~ 🔴 RULED READING A (2026-07-14, Grant in-chat):** the fork is **CLOSED toward Reading A (wake-feeding)**; **Reading B retired**. Data-confirmed via the #689 localization observable — **LOOP-FILLING** on **both statistics, both boundaries, register-robust** (`research/2026-07-14_gpersist-localization-observable_RESULT.md:160`; "Reading A CONFIRMED; the fork closes toward A"). **G-PERSIST ★RULED stamp untouched.** *The 2026-07-13 "KEEP-BOTH-OPEN / Reading A LEANED / Reading B OPEN" read that follows is the superseded prior status, preserved verbatim:* *Reading A (wake-feeding: the periodic-torus enclosure returns the pattern's own wake; the projection gauge counts laps)* **LEANED**; *Reading B (genesis-under-confinement)* OPEN; discriminator = spatial-concentration / participation-ratio **localization observable** (follow-on queued); the flip does **NOT** depend on the fork. **Torus erratum** landed with this ruling: the `pml=0` enclosure is **energy-closed-periodic (a torus, `np.roll`, `k4_tlm.py:393`)**, not a reflecting box; physics conclusions unchanged. | **Grant (★RULED-CONFIRMS)** |
| **F6 §5.4** | tier-1 two-reservoir ODE ledger (#674) — disposition fork | **★RULED — BOTH (Grant confirmed 2026-07-13, in-chat).** (i) **FORM-EXISTENCE BANKED** — the occupancy-slaved chord is a real, distinct dynamical form (separable from FRONTIER **and** from Λ during the drain-active era; `D[ON,Λ]≈0.895` at frontier-best-mimic); **CONSISTENCY-class, κ free ⇒ no emergence**. (ii) **WRONG-INSTRUMENT CLOSURE BANKED** — the attribution is homogeneously invisible at late epochs (chord → Λ past window-start `τ₀≈300`; the two-limits map quantifies it); the chord's discriminating **home = the SPATIAL cross-correlation channel** (`dark-energy-latent-heat-definition.md:158-161` class). The charter a-priori ("bin (iii) FORM-DEGENERATE expected on physical") was **FALSIFIED by the driver** (Rule 11 — bins not dropped/retuned). | **Grant (★RULED — BOTH)** |

**Grant's walked refinement (ruling-grade walked input, ★QUARANTINE-tagged — "effectively off now, but not really").** The CHORD tap (matter-occupancy) is **effectively closed at late times** (matter dilution) — which is exactly why homogeneous averages read Λ. But the **FRONTIER mechanism** (expansion-boundary node-genesis drawing on `ρ_latent` at `3H` — reading-ii) **continues as long as expansion does**, asymptotically at the de Sitter rate `H∞`; in that limit its throughput also decays toward Λ-like. The surviving observational discriminant is therefore the **matter→DE TRANSITION ERA** (where the taps were closing — the **w(z)-evolution window** of the survey channel), reinforcing the spatial/survey-channel home. **Rail (do not conflate):** cosmic-frontier node-genesis (new CELLS) ≠ soliton genesis (patterns) — the #670 G-PERSIST negative does **not** touch the frontier mechanism.

**Propagation sites (this PR):** G-PERSIST — ruling leaf, this docket (3 rows + this entry), `_orchestration/index.md`, R10 remanence charter, RESULT torus erratum. F6 — `dark-energy-latent-heat-definition.md` (§4.2 :128 row + §5), `engine-capability-map.md` (F6 rows), `_orchestration/index.md` (RANK 3), F6 charter correction note, `identity-break-test-design.md` (lever 1), this entry.

---

## Continuation — 2026-07-14 (THE WALL-A RULING — floor + rail + deficit-knee re-tag)

Grant ruled Wall A (the electron's `Γ=−1` tube-wall surface) in-chat 2026-07-14 (**"accept!"**),
propagated on `docs/wall-a-ruling-propagation` (DO-NOT-MERGE; only Grant merges). **KEEP-BOTH:**
every continuation above + the original docket and status boards are **not edited**; this
continuation is append-only. Nothing here canonizes beyond recording Grant's ruling; the touched
KB leaves carry Rule-12 preserve-body annotations, not deletions. Every file cite below was
Read/grep-confirmed at HEAD `c12f2bdb` this session (verify-before-cite).

### THE RULING — Wall A is a THREE-ROLE structure (Grant 2026-07-14)

**(1) GEOMETRY = THE FLOOR.** The ropelength radius `ℓ_node/(2π)` (one-pitch closure `2πR = ℓ_node`,
horn-torus `R = r`) is **NOT the wall's definition** — it is the lattice's hard geometric MINIMUM
for closing a winding (the discrete loop-closure bound). The `(Bounding Limit 1 saturation)`
parenthetical reads: **the geometry is the BOUND; the ground state SATURATES the bound.** Grant's
discontinuity argument (recorded): the envelope is a zero-width discontinuity (no actions across it —
the same two-way-opaque termination class as the definability carve); **refined:** zero-width does
not alone force geometric location (shock fronts move); the ground state sits ON the floor because
it is **maximally tight**. ★**FALSIFIABLE RIDER (recorded explicitly):** any non-ground-state cavity
should **LIFT OFF the floor** — dynamically located ABOVE the ropelength minimum; the cavity-census
R-ladder is the instrument.

**(2) AMPLITUDE = THE MECHANISM + RESPONSE.** The wall **IS** the local `S(A)→0` discontinuity (the
engine's operative `Γ=−1` definition — amplitude-primary, dynamic); it carries the `M/Q/J`
observables (substrate-observability rule) and its loading **responds to external
pressure/saturation** (the envelope-transducer ontology, cross-ref the 2026-07-13 TRANSDUCER row).
**Location = max(dynamical S→0 locus, geometric floor);** for the electron ground state these
**coincide** (S→0 sits at the ropelength floor).

**(3) THE √(2α) CONTOUR IS NOT THE WALL — RE-TAGGED THE DEFICIT KNEE.** The contour where the local
amplitude reaches `A = √(2α)` (`A² = 2α` — the `ΔS = α` deficit condition, the regime-I boundary;
coordinate authority `src/ave/core/chiral_lattice_v10.py:29-30`, `A_YIELD_SQ = 2.0*ALPHA`) reflects
`Γ ≈ −0.002` (auditor arithmetic; even at the mislabeled `A² = √(2α)` reading, `Γ ≈ −0.016`) —
**never the TIR wall.** Its derivation = the deficit condition `ΔS ≈ A²/2 = α` (FORM derived; the
`α = Class-B` echo). The **FLUXOID-COLLIMATION hypothesis** for this contour (Grant-walked
2026-07-14 — the reading that the √(2α) contour collimates the winding's fluxoid) is **KILLED by
receipts** (KEEP-BOTH recorded):
- **(i) pieces absent** — no `A(r)` profile; harmonic `flux(r)` NOT BUILT; the London
  minimal-coupling leg = **"the missing leg"** (`research/2026-07-03_lanez-fluxoid-step0_note.md:100`);
- **(ii) W4's own anatomy** = collimation **DISTRIBUTED, no-wall** (frozen-flux in every lossless cell);
- **(iii) the D3 envelope⊥identity split** — mapping identity into the envelope = "a category error"
  (`substrate-perspective-electron.md:93-103`).
Grant **ACCEPTED the deficit reading** 2026-07-14 (**"accept!"**).

**PLUS the two-BC bookkeeping (walk-level, framing).** Wall A = the **QUANTIZING BC** (the mirror —
enforces `(p,q)` closure, reads `M/Q/J`); the deficit knee = the **LOADING BC** (the port — the
coupling/matching interface). No real-space surface "carries" the phase-space winding (the register
rule). **Two-Qs rider** (walk-level, one leg weakened post-fluxoid-kill): intrinsic `Q→∞` ↔ the
mirror; loaded `Q = α⁻¹` ↔ the port (candidate address, **unproven**).

### Propagation deliverables (this PR)

- **D2 — coordinate-slip fixes** (A²-convention: `A² = 2α ≈ 0.0146`, authority
  `chiral_lattice_v10.py:29-30`; KEEP-BOTH superseded quotes):
  `substrate-perspective-electron.md:85,109`, `op14-local-clock-modulation.md:22`.
- **D3 — contour re-tag** to "the deficit knee (`ΔS = α`; regime-I boundary)" at
  `substrate-perspective-electron.md`'s Regime-II-boundary rows (NOT the `Γ=−1` wall, `Γ≈−0.002`;
  NOT a fluxoid edge). Annotated, not deleted.
- **D4 — floor clarification** at `electron-unknot-cosserat-seeder.md:18` (Bounding-Limit-1 row) +
  `breathing-soliton-v14-mode-i.md:101` (`S(A)→0` sentence): geometry = floor/bound; mechanism =
  amplitude rail; ground-state = floor-saturating; location-derivation debt = the census/stage-2
  target; excited-state lift-off rider.
- **D5 — the fluxoid FORM/VALUE instance** (`form-deriving-value-importing.md`): the fourth+ instance
  **already lives as the charge-flux row** (:90 + §108-147); this PR adds the London-missing-leg
  detail + the Wall-A fluxoid-collimation-kill cross-ref **additively** (no duplicate row).
- **D6 — hygiene** `0.117 → 0.1208` (`√(2α) = 0.1208`, not `0.117`): `rectifier-stage1:18`,
  `full-electron-transverse-selftrap:142`, `field-symbol-registry:318` (the "three unrelated
  0.117s" coincidence note). *(`full-electron-transverse-selftrap:182` already reads `0.121` —
  no fix, flagged.)*

> **RESIDUAL A²-vs-√(2α) SLIP SWEEP (durable pointer; adversarial-review R2, 2026-07-14).** A
> repo-wide sweep found **FIVE** further sites carrying the same `A²`-vs-amplitude-`√(2α)` slip
> outside the D2/D6 scope; all verified at HEAD `39c1914f`. Disposition:
> - **Three FROZEN `_archive` docs — pointer-only, deliberately UNEDITED** (Rule-12 frozen-snapshot):
>   `research/_archive/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md:797`
>   ("`A² ≈ √(2α) ≈ 0.121` … ω_local ≈ 0.94" — also the **0.94 corroborator** for the op14 R1 flag);
>   `research/_archive/L5/axiom_derivation_status.md:195`
>   ("At saturation onset (`A² ≈ √(2α)`): ω_local ≈ 0.95" — the **sole source of the exact 0.95**,
>   a second drift); `research/_archive/L3_electron_soliton/S_GATES_OPEN.md:194`
>   ("`A²_c = √(2α) ≈ 0.121`").
> - **Two live CODE sites — FIXED this repair** (they are live instruments, not frozen):
>   `src/tests/test_engine_constants_alignment.py:338` was **LOAD-BEARING** — it fed the amplitude
>   value `√(2α) ≈ 0.1208` into the `A²`-slot of `saturation_factor` (which takes `A²`), asserting
>   the cusp `S ≈ 0.937` when the actual cusp `A² = 2α` gives `S ≈ 0.993`; corrected to
>   `cusp_a_sq = 2.0*ALPHA` with the assertion `0.99 < S < 1.0` (test re-run green).
>   `src/scripts/vol_1_foundations/r10_v8_foundation_audit_t3b_amplitude_scan.py:60` (+ the `:215`
>   twin) were **comment-only, NOT load-bearing** (executed gate = `A ≤ 0.003`; `A_sq = A*A`);
>   both comments corrected to amplitude-convention `A = √(2α) ≈ 0.1208` / `A² = 2α ≈ 0.0146`
>   (also clearing the `0.117` drift). The review's independent sweep named the count as **5, not
>   the 2 an earlier summary implied** — recorded here so no future reader's inventory is short.

### Docket status board — Wall-A ruling (KEEP-BOTH; tables above unedited)

| Ruling | What | Status (2026-07-14) | Adjudicator |
|---|---|---|---|
| **Wall-A ROLE-1 (floor)** | ropelength `ℓ_node/(2π)` = geometric BOUND, ground state SATURATES it | **★RULED (Grant 2026-07-14 "accept!")** — floor, not definition; excited states LIFT OFF (census R-ladder = instrument) | Grant (ruled); cavity-census (rider) |
| **Wall-A ROLE-2 (rail)** | `Γ=−1` wall = local `S(A)→0` discontinuity, carries `M/Q/J`, load-responsive | **★RULED** — amplitude-primary mechanism; location = max(S→0 locus, floor); coincide for ground state | Grant (ruled) |
| **Wall-A ROLE-3 (deficit knee)** | `A²=2α` `ΔS=α` regime-I contour re-tagged; NOT the wall (`Γ≈−0.002`) | **★RULED** — deficit-knee reading ACCEPTED; **fluxoid-collimation hypothesis KILLED** (3 receipts, KEEP-BOTH) | Grant (ruled) |
| **Two-BC bookkeeping** | mirror (quantizing BC) vs port (loading BC) | **WALK-LEVEL framing (recorded)** — no real-space surface carries the phase-space winding | Grant (framing) |
| **Two-Qs rider** | intrinsic `Q→∞` ↔ mirror; loaded `Q=α⁻¹` ↔ port | **WALK-LEVEL, one leg WEAKENED** (post-fluxoid-kill) — port address candidate, **unproven** | Grant (open) |

---

*Cross-refs (Read/grep-confirmed at HEAD `c12f2bdb` this session): coordinate authority
`src/ave/core/chiral_lattice_v10.py:29-30` (`A_YIELD_SQ = 2.0*ALPHA`); the fluxoid step-0 note
`research/2026-07-03_lanez-fluxoid-step0_note.md:14,16,100` ([DOORWAY-NO-PINNING]; the FORM/VALUE
split; the London "missing leg"); the FORM/VALUE umbrella `manuscript/ave-kb/common/form-deriving-value-importing.md:90`
(charge-flux row, `clm-ze4clw`); the touched leaves `substrate-perspective-electron.md:85,93-103,109`,
`op14-local-clock-modulation.md:22`, `electron-unknot-cosserat-seeder.md:18`,
`breathing-soliton-v14-mode-i.md:101`; the D3 COEXIST ruling (2026-07-13 continuation row) for the
envelope⊥identity split. This continuation records queue-state + Grant's Wall-A ruling; nothing here
canonizes beyond the ruling stamp. Verbatim note: Grant's in-chat acceptance ("accept!") is the
verbatim on record; the fluxoid-collimation hypothesis is recorded as his 2026-07-14 walked
reading (paraphrase faithful to the walk, no fabricated verbatim).*

---

## Continuation — 2026-07-14 EOD (register rail + g−2 fork reframe + census + auditor batch)

Day-2 docket items that lived only in chat, staged after the day's landings (**#677** hygiene
batch A1–A9, **#682** Wall-A propagation, **#683** Wall-A review-repairs, **#685** QED-TRACE beta
gate — all MERGED; HEAD `240d59d8`). **KEEP-BOTH / append-only:** every continuation above + the
original docket and status boards are **not edited**; this section carries only the new day-2 state.
Nothing here canonizes; substrate claims are records of walks + queue-state, not new assertions. Every
PR#/SHA/file cite below was git/gh/grep/Read-confirmed at HEAD `240d59d8` this session
(verify-before-cite).

### Q4 g−2 PLUMBING FORK — **REFRAMED** (core-session walk, PENDING-GRANT nod)

The Q4 fork (charter verbatim `research/2026-07-14_qed-trace-charter.md:92`: *"does the anomaly leak
out the **radiative port**, or is it an **on-site dielectric detuning** — same number, two different
pipes — i.e. should a port charter **supersede** `simulate_g2.py`'s on-site chain or **stand alongside
it as a declared-degenerate second view**?"*) is **reframed by the #685 register result**. The two
"pipes" are the **two registers** the beta gate demonstrated flip signs on:
- the **on-site Axiom-4 dielectric detuning** (`simulate_g2.py` chain: `a_e = α/(2π)` via `πα/2 ×
  1/π²`, materialized as `G_MINUS_2_TREE`, `src/scripts/vol_2_subatomic/simulate_g2.py:9-14,52,116`
  + `src/ave/topological/cosserat.py:641-655`) = the **REACTIVE** face (stored-energy / impedance
  dress);
- the **radiative-port leak** (loaded `Q = α⁻¹`, one power of α per cycle out the `Z_EM` port; charter
  §3, `:84`) = the **TRANSFER** face (through-coupling).

Same kernel, opposite-face — exactly the #685 `register_flip_observed = True`
(`research/2026-07-14_qed-trace-beta-gate_RESULT.md:106`; §2 both-registers table `:90-106`). **The
supersede-vs-alongside fork dissolves into DEGENERATE-UNTIL-A-BREAK** — the two views are the same
mechanism read on two registers, so neither supersedes the other absent an observable that separates
them. **The named break observable = an ENVIRONMENT-MODIFIED PORT (cavity-shift class):** a transfer
register that leaks through a real radiative port is modifiable by the electromagnetic environment
(real g−2 experiments already carry cavity-shift systematics), whereas a purely on-site reactive
detuning is not — so a cavity-dependent `a_e` shift is the discriminator that breaks the degeneracy.
**Class (consistency-vs-emergence): the VALUE `α/(2π)` is ECHO by construction (α imported — charter
row 5, `:36`); only the FORM/PORT mechanism is a walkable candidate** — no emergence headline. **Status:
PENDING-GRANT nod; any port prereg is gated on it** (charter go/no-go `:88`, CONDITIONAL-GO / HELD on
Q4).

### THE REGISTER RAIL — **STANDING** (from #685, cross-cutting)

A standing register-discipline finding, surfaced by #685 (RESULT flag 2, `:241-244`): **any
running / screening / coupling claim read off a REACTIVE observable** (stored-energy, impedance,
`√(L/C)` ratio) **inherits sign-by-register ambiguity vs the TRANSFER register** (through-coupling /
force / scattering amplitude). On the one kernel #685 probed, the SAME Op14 saturation dress reads
**opposite signs by register** (transfer weakens at short distance, `p≈4.25`; reactive grows,
`p≈2.10` — RESULT `:100-106`). **The TRANSFER register is the QED-faithful one** (RESULT §1 autopsy:
`simulate_running_alpha.py` is REACTIVE-CLASS, its wrong sign a register+mapping artifact, `:56-81`).
Demonstrated `register_flip = True` (`research/2026-07-14_qed-trace-beta-gate_RESULT.md:106`).
**Candidate for the identity-break leaf's knife list — auditor call** (implementer surfaces; the
auditor decides whether it lands as a knife on `identity-break-test-design.md`).

### THE RESIDUAL LOG ROUTE — **REGISTERED OPEN, NOT SPENT**

The one classical route to `ln(q)` the beta gate did **not** probe: the **many-body scale-integrated
screening SUM between two seeded windings** (not the two-body pointwise pairwise objects #685
computed). Per #685's own scope boundary (RESULT §7, `:208-217`, load-bearing / finding 0): *"The gate
computed the two-body saturation-dressed force (form-factor class); it never computed the lattice's
many-body screening SUM between the two probes. That many-body scale-integrated medium-response route
is UNPROBED, NOT CLOSED."* Logarithms **do** emerge from analytic kernels via scale-integration
(QED's own vac-pol `ln(q)` integrates algebraic integrands; a line-superposition of `1/r` gives
`ln r`) — so the WRONG-FORM verdict is scoped to the probed pointwise regime, **not** a universal-class
kill. **The `q-g20f` scoped-import re-tag (auditor lane, queued below) MUST inherit this boundary**
(RESULT §7 `:222-224`, flag 1 `:235-240`): the re-tag must not read as closing the log route in
general.

### CENSUS STAGE-1 STATE

- **Prereg FROZEN + PUSHED.** `research/2026-07-14_cavity-census-stage1_prereg_FROZEN.md` frozen at
  commit `1c362d1d` (*"freeze(cavity-census): stage-1 imposed-cavity mode-census prereg FROZEN"*) on
  branch `analysis/cavity-census-stage1` (remote ref = `1c362d1d`, freeze-by-push held through a
  process crash — the branch tip is the freeze commit). All frozen declarations stand. *(At main HEAD
  `240d59d8` only the DRAFT `..._prereg_DRAFT.md` exists; the FROZEN version lives on the census
  branch.)*
- **Instrument build IN-PROGRESS.** Two untracked files in the execution worktree —
  `src/ave/solvers/cavity_census.py` + `src/tests/test_cavity_census.py` (execution-lane report;
  confirmed **not tracked** on the frozen branch `1c362d1d`, consistent with in-progress/untracked).
- **Execution lane USER-STOPPED.** RELAUNCH = Grant's word. Nothing here re-opens the frozen prereg.
- Cross-ref the standing Decision-5 gate (2026-07-13 reconciliation board `:176-185`): the three
  chat-only census questions (which-skin / cold-vs-driven / which-dials) are still session-only
  (ledger C4) and should be written into the census walk card before any STAGE-2 freeze.

### AUDITOR-BATCH QUEUE (consolidated, from the day's flags) — **each verified at HEAD**

Implementer surfaces; the auditor lands. **Verify-before-cite state per item** (dropped items carry a
receipt):

1. **`q-g20f` re-tag — OPEN (queued).** The "Identical (RT-equivalence)" argued-not-computed rows are
   **live and unedited at HEAD**: `q-g20f-vacuum-polarization.md:28` (*"Identical (RT-equivalence)"*),
   `:29` (*"Identical functional form"*), `:30` (*"Identical at observable scales"*) — path
   `manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/`; solidity 0.60 per the RESULT.
   Routed to auditor (RESULT flag 1). **The re-tag wording MUST inherit the §7 many-body-scale-
   integrated-route-unprobed-not-closed boundary** (the Residual Log Route row above).
2. **Hygiene batch 2 — mixed state:**
   - **Six-scale ladder register tags — OPEN.** #677 A9 landed the node-count column KEEP-BOTH with
     *"open rows not settled"* (`trampoline-framework.md:707-716`); the §5 E⊗T₂ table still carries the
     un-split label at `:282` (*"Nucleus ((2, 5) Borromean cinquefoil …)"*), and the ladder rows beyond
     nucleus are not register-tagged. Remaining phase-space/real-space register-disambiguation debt.
   - **Envelope def-node — OPEN (Grant-gated).** The envelope-length def-node is PROPOSED / gated at
     `vocabulary-register.md:360` (envelope-length = r_opt Meaning B) + `:375,:382` (body-envelope vs
     charge-core node) — *"GATED on Grant review AND on the unresolved §45 A-vs-B canonical FORK …
     NOT SOLID."* Not minted.
   - **`r_e` strike — OPEN (verify: NOT landed via #682).** #682's 9-file set did **not** touch
     `trampoline-framework.md`, where the electron-envelope mislabel lives at `:687` (*"envelope ~
     ℓ_node/(2π) horn-torus tube radius (classical electron radius scale)"*). The parenthetical is a
     mislabel — `ℓ_node/(2π) ≈ 61 fm` (reduced-Compton/2π tube radius) is **not** the classical
     electron radius `r_e ≈ 2.8 fm`. Stays queued. *(Flag content session-sourced; site identified by
     grep.)*
   - **Magnetopause register/sign fix — OPEN.** Candidate homes: the boundary-observables ladder row
     `boundary-observables-m-q-j.md:50` (*"Planetary magnetopause | Magnetosphere boundary | …"*) and
     the vol3 ch06 solar-system leaves (`planetary-magnetopause-standoff.md`, `vol3/claim-quality.md:
     313-333`). No landing receipt at HEAD; part of the ladder register-tag sweep. *(Flag content
     session-sourced; auditor scopes the exact register/sign correction.)*
   - **~~Nucleus-cell relabel — DROPPED (LANDED via #677 A2/A3).~~** Receipt: the (2,5)-phase-winding
     vs `6₂³`-real-body register split landed on the nucleus row in **both** ladders —
     `boundary-observables-m-q-j.md` (commit `22948644`, register-split note + row edit) and the
     `trampoline-framework.md:708` six-scale table + `:717` KEEP-BOTH note (commit `463dc3e1`). Both
     grep-confirmed live at HEAD. **Do not re-queue.**
   - **~~`r_e` strike question resolved as NOT-landed~~** *(kept above, not dropped — the #682 check
     returned NOT-landed).*
3. **op14 stale-0.95 auditor call — OPEN (#683 flag).** #683 R1 (`5c31fbd2`) reworded the note to
   **provenance-unclear** but **left the `0.95` in place pending the auditor call**:
   `op14-local-clock-modulation.md:22` still reads *"ω_local ≈ 0.95"* and `:46` states *"The 0.95 is
   left in place pending"*; nearest reconstruction is **0.94** (`√(1−0.1208)=0.9377`, `:39`), exact
   `0.95` traces only to `_archive/L5/axiom_derivation_status.md:195` (`:41`). Also flagged: `:112`
   uses *"A² ≈ 0.95"* (a second candidate slip vs `A²≈2α`). Auditor decides strike-vs-recompute-vs-
   keep-flagged.
4. **Collapse-target-registry `0-for-7 → 0-for-9` propagation — OPEN.** The canonical home
   `program-arc-map.md:404` already reads **0-for-9** (booked via #675). The downstream research
   registry `research/2026-07-10_collapse-target-registry.md` still reads **0-for-7** at the 3 sites
   the docket flagged (`:23,:64,:317`, per this docket's 2026-07-11 continuation `:492`). ⚠
   **Grep-completeness flag (2-method cross-check):** at HEAD the same file carries **4 further**
   `0-for-7` occurrences (`:581,:769,:772,:802`) — these read as ledger-**name** references (*"the
   0-for-7 ledger / shape"*) rather than the booked-value; the auditor should decide whether the
   propagation is the 3 named sites or the full 7, so "(3 sites)" is not silently adopted as complete.
5. **Manuscript-side `~10^39` `.tex` sites — OPEN (KB-first lockstep debt from #677).** The KB leaves
   were normalized (`~10^39` annotated with the precise `R_H/ℓ_node = α²/(28πα_G) ≈ 3.455×10^38`, #677
   A6); the `.tex` sites are the matching manuscript-side debt, **DEFERRED** per #677 and still carrying
   bare `~10^39` at HEAD: `vol_1_foundations/chapters/01_fundamental_axioms.tex:34,237`,
   `vol_2_subatomic/chapters/10_open_problems.tex:261`,
   `vol_3_macroscopic/chapters/04_generative_cosmology.tex:53`,
   `vol_9_vacuum_datasheet/chapters/12_cosmological_characteristics.tex:7,16,24,27,52`. ⚠
   **Grep-completeness flag:** `12_cosmological_characteristics.tex` carries **additional** `~10^39`
   occurrences beyond the #677-enumerated set (`:116,:192,:204`) — the enumerated "5 sites" undercounts
   the full sweep; auditor scopes.

### Docket status board — 2026-07-14 EOD continuation (KEEP-BOTH; tables above unedited)

| Ruling / item | What | Status (2026-07-14 EOD) | Adjudicator |
|---|---|---|---|
| **Q4 g−2 plumbing fork** | radiative-port vs on-site-detuning: supersede vs alongside | **REFRAMED — DEGENERATE-UNTIL-A-BREAK** (two registers of one kernel, #685 register_flip); break = environment-modified port (cavity-shift class); VALUE=echo, FORM-only | Grant (PENDING nod; port prereg gated) |
| **The register rail** | reactive-observable running claims inherit sign-by-register | **STANDING (from #685)** — transfer register = QED-faithful; `register_flip=True`; knife-list candidate | auditor (identity-break knife-list call) |
| **Residual log route** | many-body scale-integrated screening SUM → `ln(q)` | **REGISTERED OPEN, NOT SPENT** — the one classical log route #685 did not probe; `q-g20f` re-tag inherits the boundary | (open route; re-tag inherits) |
| **Census stage-1** | imposed-cavity mode-census | **PREREG FROZEN+PUSHED (`1c362d1d`)** · instrument IN-PROGRESS (untracked) · execution USER-STOPPED | Grant (relaunch = his word) |
| **`q-g20f` re-tag** | "Identical (RT-equivalence)" → scoped-import | **QUEUED (OPEN)** — argued-match rows live `:28-30`; inherits §7 boundary | auditor |
| **Six-scale register tags** | ladder rows beyond nucleus | **QUEUED (OPEN)** — §5 table `:282` un-split | auditor |
| **Envelope def-node** | envelope-length canonical mint | **QUEUED (OPEN, Grant-gated)** — PROPOSED, gated on §45 A-vs-B fork | Grant / auditor |
| **`r_e` strike** | trampoline `:687` "classical electron radius scale" mislabel | **QUEUED (OPEN)** — verified NOT landed via #682 (trampoline untouched) | auditor |
| **Magnetopause register/sign** | ladder / vol3 ch06 magnetopause | **QUEUED (OPEN)** — candidate homes named; auditor scopes | auditor |
| **Nucleus-cell relabel** | (2,5)-phase vs `6₂³`-real split | **DROPPED — LANDED #677 (`22948644` + `463dc3e1`)** | — (done) |
| **op14 stale-0.95** | provenance-unclear `0.95` left in place | **QUEUED (OPEN, #683 flag)** — strike-vs-recompute call | auditor |
| **Collapse-registry 0-for-9** | downstream propagation | **QUEUED (OPEN)** — registry `:23,64,317` still 0-for-7 (⚠ +4 name-refs `:581,769,772,802`) | auditor |
| **`.tex` `~10^39` sites** | manuscript-side value normalization | **QUEUED (OPEN)** — KB-first lockstep debt (#677); 4 files bare `~10^39` (⚠ enumerated 5 undercounts) | auditor |

---

*Cross-refs (verify-before-cite'd at HEAD `240d59d8` this session): the #685 result
`research/2026-07-14_qed-trace-beta-gate_RESULT.md` (`:106` register_flip, `:90-106` both-registers
table, `:56-81` autopsy, `:208-224` §7 scope boundary, `:235-244` flags); the QED-TRACE charter
`research/2026-07-14_qed-trace-charter.md` (`:92` Q4 verbatim, `:36` row 5 echo-scoping, `:84-100`
§3 port reading, `:162` engine constant); the g−2 driver + engine constant
`src/scripts/vol_2_subatomic/simulate_g2.py:9-14,52,116` + `src/ave/topological/cosserat.py:641-655`;
the census freeze `analysis/cavity-census-stage1` @ `1c362d1d`; the 2026-07-13 reconciliation board
`_orchestration/2026-07-13_eod-reconciliation-board.md` (A6/A7/B4 ledger, Decision-5 census, the
`.tex` deferral); merged landings #677 (`cd2040d3`), #682 (`db06ba82`), #683 (`9ce726b1`), #685
(`240d59d8`), #675 (0-for-9 booking). KB/manuscript cites re-verified live at HEAD:
`q-g20f-vacuum-polarization.md:28-30`, `op14-local-clock-modulation.md:22,46,112`,
`trampoline-framework.md:282,687,708`, `boundary-observables-m-q-j.md:50`, `vocabulary-register.md:
360,375,382`, `program-arc-map.md:404`, `research/2026-07-10_collapse-target-registry.md:23,64,317`,
the four `.tex` bridge files. This continuation records queue-state, not adjudicated physics; nothing
here canonizes.*

---

## Continuation — 2026-07-14 (batch outcomes-and-actions board)

The 2026-07-14 eight-lane batch (**#686–#693**) has fully **SETTLED** — five MERGED
(#686/#687/#688/#690/#691), three OPEN + fully-repaired + `[DO-NOT-MERGE][REVIEW:
pending-orchestrator]` awaiting Grant items (#689/#692/#693); nothing mid-flight. The closing
**outcomes-and-actions board** lands at
[`_orchestration/2026-07-14_batch-outcomes-and-actions.md`](2026-07-14_batch-outcomes-and-actions.md):
§1 the batch ledger (per-PR verdict + review count + repair range), §2 the **8-item Grant
decision queue** (F6 Komar-clock register BLOCKS the X44b freeze; #689 meter-register +
enclosure-fork; #692 LA freeze-fidelity → closes the D3 stress-test loop; #693 intervening-cells
→ gates q-g20f; #691 canonization default-NO; F5 knee-vs-wall at gate-(b) freeze; envelope-LENGTH
mint still gated on §45 A-vs-B), §3 queued-not-fired follow-on, §4 register-honest meta-lessons.
**KEEP-BOTH:** every prior continuation + status board above is **byte-unedited**; this row is
append-only and points at the board. Baseline `origin/main` `25b3b911` (#691 merge); every
PR#/SHA/verdict/file:line on the board was gh/git-verified this session (verify-before-cite,
two-method where load-bearing — one brief-number flag surfaced: the "~50/5" finding tally
undercounts, verified 61 confirmed across the 5 wrapper reviews). Records queue-state, not
adjudicated physics; nothing here canonizes.*

---

## Continuation — 2026-07-14 (late): five in-chat rulings, walk-level context

Five rulings Grant made **in-chat** during the late 2026-07-14 session (after the eight-lane
batch board, PR #694). This continuation is **documentation-only**: for each ruling it records
(1) the ruling verbatim-faithful, (2) the physical walk that grounded it, (3) the consequence it
**registers**, and (4) the authoritative in-repo site it resolves. **Nothing here is executed.**
Every downstream consequence — KB edits, re-tag propagation, docket row-moves, the meter build,
prereg freezes, auditor items — is **REGISTERED-NOT-EXECUTED** and **HELD** pending Grant's
adjudication of the remaining opens and a full possibility-map review (see *Held state* below).
Nothing here canonizes. **DO-NOT-MERGE**; only the orchestrator/Grant merges.

**Cite-provenance (verify-before-cite, two-method, this session).** Every `file:line` below was
verified by two independent methods (line-range read + content grep). Base = `origin/main`
`25b3b911` (the #691 merge). **Three result docs, one frozen prereg, and the batch board are NOT
on `origin/main`** — they live on their in-flight **DO-NOT-MERGE** PR branches:
`analysis/gpersist-localization-observable` (#689 @ `71b451ba`),
`analysis/cavity-census-stage1` (#692 @ `1dd9485a`),
`analysis/qed-trace-screening-sum` (#693 @ `4d3355b0`),
`docs/2026-07-14-batch-outcomes` (#694 @ `c2df2c31`). Each branch's local tip equals its `origin/`
tip and the cited lines verify against those tips. Ruling 1's sites (the T_ij–X44b charter, the X44
result, `backreaction.py`) ARE on `origin/main` (charter merged via #688). Cites are given as
backtick `path:line` spans (not Markdown links) precisely because the in-flight files do not
resolve on this branch.

### Ruling 1 — F6 Komar-clock register: √S (slope-1) IS the clock — CONFIRMED

**Ruling (paraphrase, faithful).** On Flag F6, Grant confirmed that the **slope-1** quantity
`√g₀₀ = √S` **IS the local clock / Komar-redshift weight**. The engine's live `komar_weight`
(`src/ave/gravity/backreaction.py:235-252`, `return np.sqrt(S)`, docstring *"Redshift / Komar
weight √S(A) on the local clock (Grant RULED (c), X44)"*) is on the correct side; the slope-2
`n = 1 + (2/7)ε₁₁` deflection index (`ray_trace_deflection`) is a **propagation** index, not a
clock.

**The walk that grounded it (paraphrase).** The **local clock** = how quickly a mass region can
*compress-and-rebound in place* against the external strain state (the asymptotic reference). The
**propagation index** = how quickly the stress region *translates to new regions*. Refinement
Grant accepted: **transport pays both** the slowed local tick **and** the strained hand-off path
— the **slope-2 composition**; a **local oscillator pays only the first** (the tick). The
**Komar/Tolman ledger sums per-cell in-place readings** — it never rides a signal across the
strained region — so it weights by the **slope-1** in-place clock `√S`, not the slope-2
propagation index. Read from the source side, this is the `z = (n_temporal − 1)/2` bridge: a
propagating signal picks up 2× the local clock, but the source integral sees the 1× only.

**What it resolves.** The Flag F6 **cross-source contradiction**
(`research/2026-07-14_tij-x44b_CHARTER.md:251`, `:272`; charter ingredient-1 at `:106`). The
**prevailing side**: the **W2 walk-back** + Grant's **RULED (c)** + the live `komar_weight` (all:
`√S` IS the slope-1 clock/redshift). The **falsified side**: **X44 §5b(i)**
(`research/2026-07-12_x44-komar-source_result.md:126-138`), which called `√S` the "EM
operating-point / wrong register" and named the **linear** `n = 1 + (2/7)ε` the gravitational
clock. The charter surfaced this *flag-don't-fix* (`:272`, *"a real cross-source contradiction …
the X44b prereg must resolve which register is the clock before freezing"*); Grant has now
adjudicated it: **X44 §5b(i) is the wrong side; √S (slope-1) is the clock.**

**Registered — NOT executed.**
- The **X44 §5b(i) falsifying-evidence relabel** — mark `:126-138` as the falsified side (auditor
  queue). NOT fired.
- The **X44b prereg may now name the clock register** (slope-1 `√g₀₀`, not slope-2 `n`) **at
  freeze** — the charter required exactly this before freezing (`:106`, *"MUST name WHICH temporal
  register is the clock … BEFORE freezing"*). **UNBLOCKED by this ruling, but NOT fired** (the
  prereg is neither written nor frozen here).

**Site it resolves:** `research/2026-07-14_tij-x44b_CHARTER.md:251` (Flag F6), `:272` (auditor-queue
item), `:106` (ingredient-1); live engine `src/ave/gravity/backreaction.py:235-252`; falsified side
`research/2026-07-12_x44-komar-source_result.md:126-138` (§5b(i)).

### Ruling 2 — #689 meter register: KEEP-BOTH, GATED on the circuit-ontology mapping

**Ruling (in-chat verbatim).** Grant: *"let's do the work to complete the mapping for the circuit
ontology and make sure that accurately [captures] the dynamics we're after and that we fully label
everything — but if we do that, I'm OK with the KEEP-BOTH path being unblocked."* (The `[captures]`
bracket is an editorial insertion into the verbatim.) **KEEP-BOTH, GATED on completing the
circuit-ontology mapping.**

**What triggered it.** The #689 localization meter shipped **potential-only**: `e_dens` omits the
Cosserat **kinetic** register (~44% of H on the fork cells). The frozen prereg (line 85) sells
`E_dens` as the "spatial parallel of `E_persist`", but `E_persist` is a **kinetic-inclusive**
H-ratio — so the meter measures a *different register* than the scalar it claims to parallel.
Review finding #3 was **ESCALATED — STOP+report, NOT re-banked**
(`research/2026-07-14_gpersist-localization-observable_RESULT.md:330`; escalation autopsy
`:336-377`): the composed (min-image + kinetic) re-run kept the **fork verdict robust** (fork
cells disperse *harder*) but **moved four non-fork bins**, so per the cluster-3 STOP rule the
kinetic term was not committed and the composed numbers were not banked — register choice is
framing-level, surfaced to Grant.

**The mapping spec Grant registered (NOT fired).** Per his walk, the circuit-ontology mapping that
unblocks KEEP-BOTH must:
1. **Label both registers fully.** Potential = **node-capacitor charge** (strain / displacement);
   kinetic = **inductor currents** (velocities / rotation rates, **bond-resident**, ~44% of H at
   read).
2. **Pin the bond-energy attribution convention** — half-to-each-endpoint, or an alternative,
   *stated* (bond-resident energy has no a-priori node home).
3. **Pin sponge-region handling** — the PML termination cells are **likely excluded** from the read
   region: the resistive ladder holds **transit current that is not "the blob."**
4. **Check the labeled meter answers the fork's actual question** — localization of the **energy
   blob**, in **both** registers.

**Resolution shape.** **Bank the frozen potential-only run for this PR**; the kinetic column is a
**disclosed companion** (not the banked verdict); the **full register is mandatory forward**.
KEEP-BOTH is unblocked *only after* the mapping above is built and labeled — **the mapping is the
gate, not this ruling.**

**Registered — NOT executed.** The **meter circuit-ontology mapping build** (items 1–4). NOT fired
here.

**Site it resolves:** `research/2026-07-14_gpersist-localization-observable_RESULT.md:330`
(finding-#3 escalation row), `:336-377` (the ESCALATED autopsy / cluster-3 STOP + potential-only-vs-
composed table).

### Ruling 3 — #689 enclosure fork: READING A (wake-feeding) — CONFIRMED

**Ruling.** Grant **confirmed Reading A (wake-feeding)** as the source of the #689 LOOP-FILLING
signature; the fork closes toward A. His frame **(in-chat verbatim):** *"the wake is the source of
self/mutual induction."*

**The walk that grounded it (paraphrase of the precise form recorded).** The ring's **own
circulating current maintains the flux linkage**: on the lossless torus the traveling wave keeps
circulating, and **every lap re-threads the measurement loop** — so the projection gauge counts
laps (φ→10.5×) while the energy **delocalizes**. The meter confirms the energy is in the **ring
current (spread)**, **not** a self-tightened core; there is no genesis-under-confinement
self-tightening on this battery for these seeds
(`research/2026-07-14_gpersist-localization-observable_RESULT.md:160`).

**Scope fences (recorded).**
- **G-PERSIST ★RULED is untouched.** The stamp flip rests on the **fork-independent PML φ-trend**
  (boundary-clean φ-dispersion); that is exactly why the fork outcome does not move it — consistent
  with the RESULT's own carve (`:164-166`) and the standing G-PERSIST docket rows.
- **Formation-route scope only.** The result concerns the **N=14 genesis-persistence cells**
  (formation route), **not** the real electron's sustenance. The driver returns discriminator data;
  it does not fiat the fork — *"Carve — Grant rules the fork"* (`:167-168`).

**Registered — NOT executed.** The **docket enclosure-fork rows move to RULED-READING-A** (via the
auditor): the three G-PERSIST rows currently carrying *"Reading A … LEANED / KEEP-BOTH-OPEN"* at
`_orchestration/2026-07-10_rulings-docket.md:435`, `:477`, `:502`. **NOT moved here** — this
continuation is append-only and does not edit those rows.

**Site it resolves:** `research/2026-07-14_gpersist-localization-observable_RESULT.md:160` (Reading A
CONFIRMED / fork closes toward A), `:167-168` (the "Grant rules the fork" carve).

### Ruling 4 — #692 LA freeze-fidelity: RATIFIED

**Ruling (in-chat verbatim).** Grant: *"ratify"* — after the implications walk. He ratified that
reading the **LA (linear-algebra) fundamental** is **freeze-fidelity** to "lowest interior mode"
(**not** a post-hoc target move); the **SA defect-band read** was the actual deviation, kept
alongside (KEEP-BOTH). The verdict is unchanged: **non-(2,3) on both spectral ends.**

**Implications recorded (Grant's walk).**
- **(a) The D3 stress-test loop CLOSES.** COEXIST **stands**; the (2,3) **SELECTION stays
  imported** — now **tested-not-conceded** (the census stress-tested the ruled-COEXIST's two legs
  and did not break them).
- **(b) The scope theorem.** The **cold-linear lattice has no winding to give**: a Hermitian
  real-symmetric H ⇒ real eigenvectors ⇒ **no basis-invariant winding** — confirmed at **both**
  spectral ends, with the detector **validated by planted controls**. So selection, **if** it
  exists, is a **DRIVEN / NONLINEAR** phenomenon.
- **(c) Burden formally moves to census Stage-2 (driven).** The **cold leg is structurally
  incapable of hosting a positive control, permanently** — a cold-linear positive control cannot
  exist, so the question can only be answered in the driven regime.
- **(d) Untouched:** electron existence, the mass sector, the carrier results, and the Wall-A
  floor-test confirmation.

**Registered — NOT executed.** The **D3 docket-row move** (record the stress-test loop closed /
COEXIST tested-not-conceded) via the auditor. NOT moved here.

**Site it resolves:** `research/2026-07-14_cavity-census-stage1_RESULT.md:545-547` (the "ratify LA
fundamental = freeze-fidelity, not a post-hoc target move; verdict unchanged non-(2,3)"
adjudication), `:488-489` ("what remains for Grant" + the KEEP-BOTH SA read).

### Ruling 5 — #693 "intervening cells" = THE RUN reading — RATIFIED

**Ruling.** Grant ratified that **"intervening cells"** (prereg §4:157) means **the run between the
collars**, **NOT** the dress-slicing cylinder — so the frozen **RELABELED-PAIRWISE** re-tag
**FIRES**. (Verbatim term quoted: *"intervening cells"*; the rest below is the repaint that carried
the ruling.)

**The repaint that resolved Grant's objection.** Grant correctly insisted the medium between two
solitons **of course participates** — **the springs carry the force**. The resolution is the
**two-jobs carve**:
- **JOB ONE — the medium as TRANSMISSION LINE** carrying the **bare 1/R²**. Never in question,
  never tested; it is the **normalization baseline** (AVE is a **contact theory** — the medium *is*
  how the force gets across).
- **JOB TWO — the medium as ACTIVE DIELECTRIC** modifying the coupling: the **departure-from-bare**,
  `α_eff(R)`. This splits into **path physics** (per-decade accumulation — the QED-log shape) vs
  **endpoint physics** (each charge's **~10-cell saturated collar**; beyond it the induced
  polarization falls **~s⁻⁶**).

**Corrected decomposition.** Suppressing the **entire run's** polarization response changes the
correction by **~0.02%**; the **collars carry ~100%**
(`research/2026-07-14_screening-sum-gate_RESULT.md:233`). The **run is rigid** ⇒ **nothing
accumulates per decade** ⇒ the **no-log verdict is mechanistically explained** — it is a named
mechanism, not a null-of-ignorance.

**Plumber form on record.** Towers–pipes–manifolds: the **pipes carry the pressure** (job one); the
**correction lives in the two manifolds**, not the run; a **rigid run = no log**.

**What it means for the frozen rule.** The frozen genuineness knife
(`research/2026-07-14_screening-sum-gate_prereg_FROZEN.md:157`, §4: *"removing the intervening cells
does not change the result → RELABELED-PAIRWISE"*) is read with "intervening cells" = the **genuine
mid-bridge medium** (excluding each probe's own near dress). The two do-not-bury FLAGGED-for-Grant
blocks in the result (`research/2026-07-14_screening-sum-gate_RESULT.md:50-53`, `:237-239`) are the
crux interpretive step; Grant has now **ratified the mid-bridge reading**.

**Sector fence.** **E-sector static dielectric, transfer register** — this is about **charges, not
masses.**

**Registered — NOT executed.** The **`q-g20f` re-tag propagation** ("Identical (RT-equivalence)" →
scoped-import), **with the enumerated scope bound in**, via the auditor — **GATED until Grant's
full-picture session completes.** NOT fired here.

**Site it resolves:** `research/2026-07-14_screening-sum-gate_RESULT.md:50-53` (the do-not-bury FLAG
+ KEEP-BOTH shipped-cylinder-vs-corrected), `:237-239` (the frozen-rule reading); the frozen rule at
`research/2026-07-14_screening-sum-gate_prereg_FROZEN.md:157` (§4).

### Held state — Grant's standing directive + held executables

**Standing directive (verbatim-faithful).** **No further actions.** The remaining opens — **F5
(knee-vs-wall** on the yield surface), **#691 canonization (default-NO)**, and the **envelope-LENGTH
mint on §45** — are to be **adjudicated next**. **Then a full possibility-map review BEFORE any
execution.** Nothing on the held list below fires until that review completes.

| # | Held executable | Owner-lane when released | Gated by |
|---|---|---|---|
| 1 | **X44 §5b(i) falsifying-evidence relabel** (`research/2026-07-12_x44-komar-source_result.md:126-138` → mark as falsified side) | auditor | Ruling 1 (may fire once opens clear) |
| 2 | **Meter circuit-ontology mapping build** (Ruling 2 items 1–4: both registers labeled · bond-attribution pinned · sponge/PML handling pinned · fork-question check) | implementer | Ruling 2 (the mapping *is* the gate) |
| 3 | **Docket fork/D3 row moves** — G-PERSIST enclosure rows → RULED-READING-A (`_orchestration/2026-07-10_rulings-docket.md:435,:477,:502`); D3 row → stress-test-loop-closed | auditor | Rulings 3 + 4 |
| 4 | **`q-g20f` re-tag propagation** (scoped-import, enumerated scope bound in) | auditor | Ruling 5 **+ Grant's full-picture session** |
| 5 | **X44b prereg** (name the clock register — slope-1 `√g₀₀` — at freeze) — UNBLOCKED by Ruling 1, **not fired** | implementer | possibility-map review |
| 6 | **All board §3 queued work** (`_orchestration/2026-07-14_batch-outcomes-and-actions.md` §3 — QUEUED FOLLOW-ON WORK, registered NOT fired) | mixed | possibility-map review |

All six are **REGISTERED-NOT-EXECUTED**. This continuation records ruling-state and the held queue;
it **executes none of it** and **canonizes nothing.**

*Append-only continuation (2026-07-14 late) — all prior docket content byte-untouched. Cites
verified two-method at base `origin/main` `25b3b911`; in-flight files verified against their
PR-branch tips (#689 / #692 / #693 / #694, local == origin). DO-NOT-MERGE; only the
orchestrator/Grant merges. Nothing here canonizes; every consequence is HELD pending Grant's
possibility-map review.*

---

## Continuation — 2026-07-14 (night): three further in-chat rulings — F5, canonization, envelope mint

Three further rulings Grant made **in-chat** during the night 2026-07-14 session — after the
five-rulings continuation above and after the eight-lane batch board (#694). These adjudicate the
three items the batch board still flagged for Grant: decision-queue **#7 (F5 knee-vs-wall)**, **#6
(#691 canonization)**, **#8 (envelope-LENGTH mint)** — `_orchestration/2026-07-14_batch-outcomes-and-actions.md:80-82`.
For each ruling this continuation records (1) the ruling **verbatim** where one exists (marked), (2)
the physical walk that grounded it (**paraphrase-faithful**, marked), (3) the consequence — with its
execution-status tagged, and (4) the in-repo site it resolves. **Cites verified two-method**
(line-range read + content grep) at merged base `origin/main` `bb58727f`; the charter,
vocabulary-register, and #691 RESULT sites are on `origin/main`. **DO-NOT-MERGE**; only the
orchestrator/Grant merges. **Nothing here canonizes**; the FORM mint of Ruling 8 is landed by the KB
lane (this docket records the ruling and points at the leaves).

### Ruling 6 — F5: the conjecture meant THE WALL — RESOLVED

**Ruling (Grant verbatim).** *"yes, that's what I meant for F5"* — resolving Flag F5's KEEP-BOTH
(two same-day Grant inputs in tension on the yield surface). **The conjecture meant the WALL**
(ROLE-2), not the deficit knee (ROLE-3).

**The knee/wall carve (context walk, paraphrase-faithful).**
- **Knee** = the **proportional limit** — the **`A²=2α` contour** where the kernel deficit
  `1−S = 1−√(1−2α) ≈ α` (**ΔS = α**); the **onset-of-load-transfer**, `Γ ≈ −0.002`. (ROLE-3.)
- **Wall** = the **fully-yielded `S→0` surface** — polarization compliance **exhausted**, the
  **`|Γ|=1` mirror**; carries **M / Q / J**; ground state **pinned at the ropelength floor
  `ℓ_node/2π`**. (ROLE-2.)

These match the charter's F5 statement (`research/2026-07-14_tij-x44b_CHARTER.md:250`: knee = ROLE-3
`A²=2α`, `S≈0.993`, `Γ≈−0.002`, "never the TIR wall"; wall = ROLE-2 `S(A)→0` / `Γ=−1`, floor
`ℓ_node/2π ≈ 0.159`) and the Wall-A ruling's three ROLE rows
(`_orchestration/2026-07-10_rulings-docket.md:606-608`; floor `:522`, rail `:533`).

**Grant's walked physical picture (paraphrase-faithful, recorded).** An external **static field** =
a **DC bias across the dress**. A **uniform** field = **common-mode bias** — the ground state is
**floor-protected** (incompressibility: you cannot squeeze a closed loop below its ropelength). A
**gradient** field = **differential bias** → **asymmetric Maxwell stress** → **envelope
deformation**. **Excited states** (floor-lifted — the census-confirmed rider) are **genuinely
compressible**.

**Consequence — REGISTERED-NOT-EXECUTED-BEYOND-THIS-WAVE.** Gate-(b) pre-registration:
`R_balance ≡ R_yield`-**the-WALL** confirms the conjecture — with **F3's `1.6`-vs-`0.159`** (the
balance-radius vs floor-radius contradiction, charter Flag F3, `research/2026-07-14_tij-x44b_CHARTER.md:123,126`;
gate-(b) acceptance test `:132`) **riding the same measurement**. The gate-(b) envelope-eigenmode
freeze is **not written or fired here**; this ruling only fixes which surface it measures.

**Site it resolves:** `research/2026-07-14_tij-x44b_CHARTER.md:250` (Flag F5 KEEP-BOTH → WALL); the
ROLE-2/ROLE-3/floor split at `:121`, `:125`; the gate-(b) radius-discriminating acceptance test at
`:132`; the Wall-A ruling `_orchestration/2026-07-10_rulings-docket.md:606-608` (three ROLE rows),
`:522` (floor), `:533` (rail).

### Ruling 7 — #691 canonization: NO — RULED

**Ruling (Grant verbatim).** *"no, we need to be firm on our claims."* — on whether to canonize a
`NEUTRON_ELECTRON_RATIO` / `M_N_MEV_AVE` into `ave.core.constants`. **NO.**

**What it settles.** **C5 stays OPEN**; the **#676 n–p-gate detector stays clean** (canonization
would flip that corpus-state detector by design); **no NEUTRON value enters `constants.py`** — the
file keeps only the CODATA `M_N_MEV_TARGET` with its standing note that *"no framework derivation has
yet been adopted for the neutron mass"* (`src/ave/core/constants.py:1135,1138`), i.e. **no
derived/AVE neutron value**. **Revisit only if** the 3D composite (Faddeev-Skyrme) build lands a
**magnitude in-band** — the #691 1D-radial proxy is bin (iii) RIGHT-SIGN-WRONG-MAGNITUDE (~15×) and
its δ_th ablation is **channel-blind**, so C5 is **not adjudicated by the proxy**.

**Site it resolves:** batch board decision **#6** (`_orchestration/2026-07-14_batch-outcomes-and-actions.md:80`);
the #691 RESULT C5-OPEN + "detector clean by design"
(`research/2026-07-14_route-a-composite-fs_RESULT.md:110-111`, `:194-199`); `src/ave/core/constants.py:1135,1138`
(CODATA target + standing "no framework derivation adopted" note; no AVE neutron value).

### Ruling 8 — envelope mint: OPTION C — RULED

**Ruling (Grant verbatim).** *"I like C for that."* — on how to mint the envelope. **OPTION C: mint
the THREE-SURFACE ANATOMY as FORM; values stay gate-measured.**

**The three-surface anatomy (FORM minted; values gate-measured).**
- **(i) wall / floor** — the **mirror**; ground state at the ropelength floor `ℓ_node/2π ≈ 0.159
  ℓ_node`.
- **(ii) balance shell** — the corpus **soft number `~1.6 ℓ_node`**; status: **conjectured ≡ wall**
  per Ruling 6, **gate-(b) adjudicated**.
- **(iii) knee / dress-edge** — the **`ΔS = α` contour**; radius is a **REGISTERED CHECK** (is the
  #693 `~10-cell` collar edge the knee contour? — running as a Wave-0 sibling lane).

**Word-level sub-choice.** *"envelope" retires* vs *"envelope = the wall"* is **PROPOSED as
"envelope = the wall"** in the KB lane's mint, **pending Grant confirm at merge**.

**Canon-worthy walk findings — recorded BY POINTER (the KB lane lands the leaves).**
- the **knee/wall stress–strain mapping**;
- the **PATH-PARTICIPATION ASYMMETRY** — the EM correction is **endpoint physics** (collar-bound,
  `s⁻⁶`) while gravity is **ledger physics** (a clock-weighted Komar volume integral): **same kernel
  and stress register, inverted integration structure** — which is why gravity is **long-range
  unscreened** and the EM correction **short-range** out of one substrate;
- the **radial-ladder circuit table** — far-field **linear ladder** / **knee** = varactor-bias onset
  / **dress** / **wall** = compliance-exhausted `|Γ|=1` / **floor** = minimum closed loop.

**Consequence — FORM MINT LANDED BY THE KB LANE (not here).** This docket records the ruling and
points at the leaves; the values stay **gate-measured**, not asserted. The mint targets the gated
envelope def-nodes (`manuscript/ave-kb/common/vocabulary-register.md:367` `r_env` `def-088f0d`,
`:382` node-Nyquist `def-e0cd83`, `:386` `def-envl0p` GATE), still gated on the **§45 A-vs-B**
canonical fork (sub-node charge-core vs supra-node body envelope) until Grant's confirm.

**Site it resolves:** batch board decision **#8** (`_orchestration/2026-07-14_batch-outcomes-and-actions.md:82`);
the envelope def-nodes `manuscript/ave-kb/common/vocabulary-register.md:367,382,386`; the §45 fork +
docket status-board rows `_orchestration/2026-07-10_rulings-docket.md:724,782`.

*Append-only continuation (2026-07-14 night) — all prior docket content byte-untouched (origin/main
region, first 95658 bytes, sha256 `8df5b9f5…`). Cites verified two-method at merged base `origin/main`
`bb58727f`. DO-NOT-MERGE; only the orchestrator/Grant merges. Ruling 6's gate-(b) consequence is
REGISTERED-NOT-EXECUTED; Ruling 8's FORM mint is landed by the KB lane. Nothing here canonizes.*

## Continuation — 2026-07-15 (post-merge auditor batch 4): envelope=wall CONFIRMED + #698 corroboration-withdrawal landing

### Ruling 9 — envelope word-sense: "envelope = the wall" — CONFIRMED

**Ruling (Grant verbatim).** *"Yes"* — answering the explicit confirm-at-merge question (Ruling 8's
word-level sub-choice), in-chat 2026-07-15, after merging #697.

**What it settles.** Ruling 8's **word-level sub-choice** — *"envelope" retires* vs *"envelope = the
wall"*, left **PROPOSED as "envelope = the wall"** pending Grant confirm at merge (this docket
`:1150-1151`) — is now **CONFIRMED**. The token **"envelope" canonically denotes the wall** — surface
(i), the fully-yielded $S(A)\to 0$, $\lvert\Gamma\rvert=1$ mirror. The **balance shell** (ii) and the
**knee / dress edge** (iii) keep their own names. This is a **FORM-level word-sense ruling only** — it
promotes **no** numerical value. The value-side gates stay Grant-gated, **unchanged**: **(a)** the
r_env / node-Nyquist length mint (proposed → SOLID; board decision #8,
`_orchestration/2026-07-14_batch-outcomes-and-actions.md:82`) and **(b)** the §45
balance-shell-distinctness / radii (gate-(b), Ruling 6 CONJECTURED ≡ wall).

**Sites it resolves:** the KB markers flipped PROPOSED→CONFIRMED at
`manuscript/ave-kb/common/vocabulary-register.md:390` (def-anat3s) + `:401` (GATE item c),
`manuscript/ave-kb/common/claim-quality.md:1414` (clm-3surfa caveat), and the canonical-home status
block `manuscript/ave-kb/common/envelope-anatomy.md`. **Supersedes** Ruling 8's word-level sub-choice
(this docket `:1150-1151`, byte-untouched).

### Ruling 10 — #698 meter-ontology: #689 PML-twin boundary-insensitivity corroboration — WITHDRAWN (landing record + Rule-12 repair)

**What it records (a landing + Rule-12 staleness repair, not a new Grant ruling).** The **#698**
meter-circuit-ontology addendum (`research/2026-07-14_gpersist-meter-circuit-ontology.md` §5/§7,
merged; phase-robust restatement landed via correction PR #701) **withdrew** the #689 RESULT TL;DR
item 2 **PML-twin boundary-insensitivity corroboration**: it holds only on the frozen **endpoint**
read — a single LC-slosh **phase moment**; under the phase-robust **quiet-window mean**,
time-averaged, **NEITHER register is boundary-insensitive** (both the potential and full registers
CONCENTRATE on the PML box while reading LOOP-FILLING on the torus). Per §5(2) this is a
**boundary-DEPENDENT core-holding** signal (the fixed-center core ball absolutely GAINS energy on the
PML box, +50.6% `pair`), **not** a read-region / kinetic-drain artifact, and **not admissible as
boundary corroboration**. **The fork rests entirely on the torus cells** (`pair`+`graded_a0`),
LOOP-FILLING robust under every read (`guard_sensitive=False`).

**Untouched.** **Ruling 3** (enclosure fork = **Reading A**, wake-feeding) and **G-PERSIST ★RULED**
stand — they rest on the torus cells and the fork-independent PML **φ-dispersion** trend
respectively (the #670 T2/Φ_link channel — a *different*, still-valid boundary-insensitive signal,
never summed into the A1 localization meter).

**Fork-rows dated annotation (Item A of this batch).** The three G-PERSIST fork rows (this docket
`:435`, `:477`, `:502`) describe the #689 evidence as *"LOOP-FILLING on both statistics, **both
boundaries**, register-robust."* The **"both boundaries"** (PML-twin) leg leans on the now-**withdrawn**
corroboration and is **no longer load-bearing**; the RULED verdict stands on the **torus** cells
(register-robust there — LOOP-FILLING on both the potential and full registers, #698 §4). Rows
byte-untouched; this entry is the dated annotation.

**⚑ FLAG (flag-don't-fix — surfaced to orchestrator/Grant; resolution STAGED, not yet on main).** The
**#698 PR body** describes a *stronger* phase-robust withdrawal — *"phase-averaged, NEITHER register
is boundary-insensitive,"* a quiet-window-mean primary read, and a core-holding **+50%**
absolute-energy diagnostic — carried by review-repair commits `8167a89c` / `850956b1` / `16231ad7` /
`e45949fe`. **Those commits were NOT ancestors of `origin/main`** (`9bb760f9`): #698 merged the
addendum `000d9cf4` + `6d9a8b2b` only, dropping the four repairs. **Resolution STAGED — correction PR
#701** (`fix/698-repair-commits-correction`; pre-fix-merge pattern, precedents #679/#683) brings the
four repair commits onto a branch off `origin/main` (net diff = the four repairs, 3 files +469/−113;
8/8 tests + `make verify` green). Until #701 merges, `origin/main`'s §5/§7 still carries the *earlier*
framing (**potential** register boundary-clean; **kinetic** register PML-drain-contaminated); the
in-corpus annotations this batch landed (RESULT TL;DR/§2/§3/§7 + board `:77` + this Ruling 10) are now
written to the **phase-robust** framing #701 lands. Both framings agree the corroboration is withdrawn
and the fork rests on the torus cells; they differ only on whether the *potential* register is
boundary-insensitive on the PML box (phase-robust: it is **not** — time-averaged, both registers
CONCENTRATE). Orchestrator/Grant to merge #701 (sequence relative to #700 at their discretion).

**Sites it resolves / annotates:** `research/2026-07-14_gpersist-localization-observable_RESULT.md`
(TL;DR item 2 Rule-12 note + §2 `:126` / §3 `:157-158` / §7 `:290` pointers; internal Finding #3
ESCALATED §1); `research/2026-07-14_gpersist-meter-circuit-ontology.md` §5/§7;
`_orchestration/2026-07-14_batch-outcomes-and-actions.md:77` (decision-#3 "both boundaries"
annotation); this docket's fork rows `:435`, `:477`, `:502` (dated annotation, above).

*Append-only continuation (2026-07-15, post-merge auditor batch 4) — all prior docket content
byte-untouched (origin/main region, first 122775 bytes, sha256 `64879a3c…`). Cites verified two-method
at merged base `origin/main` `9bb760f9`. DO-NOT-MERGE; only the orchestrator/Grant merges. Ruling 9 is
a FORM-level word-sense ruling (no value promoted; gates (a)/(b) unchanged); Ruling 10 is a landing +
Rule-12 staleness repair carrying one FLAG now resolution-staged via correction PR #701 (the four
unmerged #698 phase-robust repair commits, DO-NOT-MERGE pending orchestrator). Nothing here canonizes
a value.*

---

## Continuation — 2026-07-15: the register walks

Core-session register walks (2026-07-15). **KEEP-BOTH:** all prior docket content above is byte-untouched;
this continuation is append-only. **Ruling-status precision is the prime rail** — each item below carries its
exact status (RULED / WALK-RECORD / PROPOSED), and the RULED items are **FORM-level ruled conventions, not
derivations** (a ruled convention organizes the corpus; it does not derive α or a knee value — values ride
CODATA imports). This content is now landed **KB-leaf-first**: the register carves live in the new leaf
[`manuscript/ave-kb/common/strain-registers.md`](../manuscript/ave-kb/common/strain-registers.md) (`clm-strreg`,
`clm-crit2a`); the saturation anatomy + Q2 in [`envelope-anatomy.md`](../manuscript/ave-kb/common/envelope-anatomy.md);
the thermal walk in [`thermal-phase-registers.md`](../manuscript/ave-kb/common/thermal-phase-registers.md)
(WALK-LEVEL, no-claim); the EE rows in `translation-circuit.md` §4. Every cite verified two-method; nothing
here canonizes a value.

### RULING 11 (RULED — Grant verbatim "Yes, I agree with where the walk is ending up"): THE STEP-REGISTER RULING

The constitutive kernel consumes **FIELD-strain** (the per-cell drop, $E\cdot\ell_{node}$ — the *gradient*
register), **NOT** **voltage-strain** (the potential, $d_{sat}/r$). Grounds walked: **(a)** a varactor biases
on the voltage across its own junction = one cell span; **(b)** every physical dielectric saturates against $E$
($P(E)$), never absolute potential; **(c)** locality / gauge — the mechanical twin of *potential* is total
displacement $u$; a kernel on $u$ violates lattice translation invariance; **strain is $\partial u$**, and the
electrical twin of strain is $E$ (not $\phi$).

**THE LADDER THEOREM (the reconciliation).** The potential IS the series sum of the per-cell drops — voltage
register $=$ line integral of the field register ($V=\int E\,d\ell=\sum_{\text{cells}}E\cdot\ell_{node}$).
**Cells feel steps; ports / interactions see sums.**

**CONSEQUENCES REGISTERED-NOT-EXECUTED.** Both knees are real: the **field knee** $(2\alpha)^{-1/4}=2.877\,\ell_{node}$
(the cell / dress knee, measured as the $r99$ outer edge in PR #696, **ratio 1.06–1.27** — frozen 1.06 / refined 1.27, resolution-stable, `research/2026-07-14_knee-contour-check_NOTE.md`:180,:224-225) and the
**voltage knee** $(2\alpha)^{-1/2}=8.278\,\ell_{node}$ (the interaction / port knee; the second is the square of
the first). Op4/Op14's $(d_{sat}/r)^2$ argument = a ~~**CANDIDATE integrated port expression of a field-biased
ladder** — ★ **REGISTERED CHECK (the Op4 ladder integral):** integrate the per-cell field-strain dress radially
and compare to the closed-form $Z_0(1-(d_{sat}/r)^2)^{-1/4}$ (a **match closes the fork completely**; a
**mismatch = a real defect in a canonical operator** — flag-don't-fix)~~. **🔴 UPDATE 2026-07-15 (Rule-12; PR #704 `analysis/op4-ladder-integral-check`, MERGED — the ★REGISTERED CHECK has now FIRED; strike-through above preserved, git is the trail):** the Op4 ladder integral **RETURNED NO-MATCH** — the field ladder integrates to $p=4$ under both signs, and (WKB) ports localize ($Z_{in}\to Z_{local}$). So Op4 is **NOT a constitutive-dress integration (candidate → REFUTED-as-integration)** but is **EXACTLY the local voltage-register dress — a legitimate pairwise / interaction-register operator under the ruled carve (RESOLVED-as-register-identity)**. The fork closes by register-identity, not by integration-match. **Routed to Grant:** the Op4 scope question (a pairwise-only / interaction-register label + its 4 consumer sites). The 1/4-map's Q#1 fork
(`research/2026-07-14_quarter-power-map.md`) **RESOLVES under this ruling** — both registers correct in their own
register — with the `r_knee` quarter-power retained, **fork-conditional no more** (still α-echo-classified).
`methodological-contamination.md:48`'s pairwise voltage-strain ($d_{sat}/r_{ij}$) is the **INTERACTION register
used correctly** — no correction owed; the knee-NOTE's ⚑ voltage-strain FLAG is resolved (port register), not
fixed. **gate-(b) prereg** should pre-register the **field knee** as the dress-edge candidate.

### RULING 12 (RULED — Grant verbatim "ratify", in-chat 2026-07-15; upgraded from the WALK-DELIVERED "factor-of-2 analysis"): THE TWO-CRITERIA RULING

The two α-thresholds are **two criteria on one nonlinear element**: the **STORAGE** criterion "stored fraction
$=\alpha$" $\Rightarrow A^2=\alpha$, $A=\sqrt\alpha\approx0.0854$ (the entire yield family: $V_{YIELD}=\sqrt\alpha\,V_{SNAP}$,
$E_{YIELD}=V_{YIELD}/\ell$, $h_{yield}=\sqrt\alpha$, genesis seeds); the **RESPONSE** criterion "deficit
$\Delta S=\alpha$" $\Rightarrow A^2=2\alpha$, $A=\sqrt{2\alpha}\approx0.1208$ (the knee family: `A_YIELD_SQ`,
`R_I`). **THE 2 IS THE TAYLOR-½ OF THE ROOT KERNEL** ($\Delta S=1-\sqrt{1-A^2}\approx A^2/2$) — unconditional.
**Equipartition** (the traveling-wave half-half quadrature split) is the **AC BRIDGE** that makes the deficit
numerically equal the per-sector share — **regime-dependent** (standing waves slosh; the #698 phase findings are
the live demo), so the ½ is the **kernel's**, not the wave's (the static dress using $\sqrt{2\alpha}$ and matching
$r99$ is the tell). The criteria carve is **ORTHOGONAL to the register carve** (a 2×2: register step/ladder ×
criterion storage/response; the corpus populates all four cells under names that never advertised the axis; $h_{yield}$ = a field-register quantity
carrying the storage criterion). The **near-collision** ($\sqrt{1-\alpha}=0.996345$ vs $(1-2\alpha)^{1/4}=0.996331$,
$\Delta=1.4\times10^{-5}$) = the two criteria's clock projections.

**RENAME NOTE (gentle, walk-record):** the $\sqrt\alpha$ family's "yield" name is soft — nothing yields there; it
is the **storage-α mark**; actual breakdown = the wall at $A=1$. (No rename executed; flagged for the vocabulary lane.)

★ **CRITERION-TAG MANDATE — RATIFIED (Grant "ratify", 2026-07-15):** every $\sqrt\alpha$/$\sqrt{2\alpha}$ site is
tagged **storage-α vs response-α**, folded into the contour-tag sweep (which moves from gated to **QUEUED** in the
next-steps register). A bookkeeping-discipline mandate, not a physics claim.

*(Grading note per the ratification: solidity reflects ruled-status, but the physics-content grading stays honest —
a ruled convention is a convention, not a derivation. The KB claims `clm-strreg` / `clm-crit2a` are graded
FORM-class at solidity 0.45, floored by CODATA-import deps.)*

### ENTRY 13 (WALK-RECORD — framework, not ruling): THE SATURATION ANATOMY

Landed in [`envelope-anatomy.md`](../manuscript/ave-kb/common/envelope-anatomy.md) §"saturation anatomy" +
`translation-circuit.md` §4. **Bench EE:** a saturated capacitor = polarization exhausted, $C_{diff}\to0$,
incremental **OPEN** ($\Gamma\to+1$), clips charge, voltage-stiff; a saturated inductor = magnetization exhausted,
$L_{diff}\to L_{air}$, incremental **SHORT** ($\Gamma\to-1$), clips flux, current-soft (the choke becomes a wire).
**Shared truth:** a saturated reactive element **leaves the storage business and joins the boundary business**;
$\lvert\Gamma\rvert\to1$ either way; **ideal saturation dissipates nothing** (lossless refusal — Ax3-compatible;
connects the amorphous/plastic retirement). **THE VACUUM NODE at $A\to1$, $S\to0$:** (1) its clock stops
($\omega_0\sqrt{S}\to0$ = the $g_{00}\to0$ signature, Ruling-1 register at its limit); (2) it becomes a mirror
($\lvert\Gamma\rvert\to1$) — **THE WALL = a closed curve of cells that have left the storage business**; TIR = a
ring of reactive refusal; phase-space: the orbit that can no longer turn; (3) open-vs-short = the ruled #260
sign/spin selector; (4) partial saturation = the varactor/mixing regime ($\chi^3$ four-wave; the deficit knee =
the first blush of refusal; the α-criteria = milestones on one road); (5) **past exhaustion THE VACUUM
RECTIFIES** — pair production = the vacuum's avalanche breakdown = out-of-band AC winding rectified to DC winding
(the corpus Miller-avalanche mapping + the FPB-corner walk); $V_{snap}=m_ec^2/e$ = one cell's rest energy = the
quantum of rupture (WHY the products are particles); (6) nothing dissipates — the frozen ring **HOLDS
$\mathcal{M}/\mathcal{Q}/\mathcal{J}$** as boundary observables. **THE ELECTRON IN ONE SENTENCE:** a
self-sustaining winding whose circulation keeps its own boundary ring of cells exactly at storage exhaustion; the
ropelength floor = the smallest closed ring of refusal the lattice geometry can form; excited states hold bigger
rings (census-confirmed lift-off).

### ENTRY 14 (WALK-RECORD + 2 PROPOSED-DEFINITIONAL items): THE THERMAL / PHASE-REGISTER WALK

Landed in [`thermal-phase-registers.md`](../manuscript/ave-kb/common/thermal-phase-registers.md) (WALK-LEVEL,
no-claim). Grant's three questions and the walked answers:

- **(Q1) heat as measured by bound structures = PHASE-DIFFUSION BETWEEN SOLITON CLOCKS**, split: **mean shift =
  the thermal operating point** (canon: $\delta_{strain}$/TCC at $T_{CMB}$, Q-DELTA-MAP-1) vs **variance = the
  heat content proper** (driver: Johnson-Nyquist $k_BT$-per-mode strain-noise jittering every tank). Under Ax3:
  heat = phase disorganization of reactive energy, **NOT loss**; entropy = lost phase information between clocks;
  temperature = the width of the clock-detuning distribution. ★ **PROPOSED-DEFINITIONAL #1** (walk-level, not
  solid until measured): **"temperature = clock phase-diffusion width"** — gated on the ★ **REGISTERED two-tank
  decoherence check** (seed two identical tanks + random traveling bath; measure relative-phase variance growth vs
  bath energy density). ★ **PROPOSED-DEFINITIONAL #2:** **"entropy = lost phase information between clocks"** —
  same gate. *(The one axiom-derived line: heat = decoherence, not dissipation, from Ax3.)*
- **(Q2) envelopes:** GROUND STATE never compresses geometrically (floor-pinned; incompressibility = the
  stability); the response is **DRESS RE-BIAS** (varactors walk their $C(V)$ curves, strain redistributes);
  EXCITED states genuinely compress (walls on the dynamical locus, census lift-off). Grant's "or" dissolves — the
  $E$-field IS the lattice strain read in the electrical grade (TKI; per Ruling 11 the field = the per-cell strain
  gradient the kernel eats). External Maxwell stress transmits through the dress and lands on the wall as a
  boundary condition (= the $T_{ij}$ object).
- **(Q3) the gravity well = the collective sum WITH TWO PRECISIONS:** (a) stored **ENERGY** both registers, not
  strain alone (kinetic register ~44% of $H$ in the measured driven cells — a strain-only ledger undercounts);
  (b) clock-weighted at $\sqrt{S}$ (Ruling 1; X44b tests incl. $+3\int p$).

**THE THREE-PHASE-REGISTER UNIFICATION (walk-record):** one substrate energy organized by phase — coherent-bound
(solitons; measured as wall observables $\mathcal{M}/\mathcal{Q}/\mathcal{J}$) / coherent-propagating (radiation;
measured as fields/dress) / incoherent-propagating (heat; measured as clock decoherence) — ALL in one
clock-weighted ledger, which is why hot things weigh more with no extra postulate; gravity = the phase-blind
interaction; EM correction = dress-bound endpoint physics; heat = the phase-noise floor. ★ **REGISTERED:**
thermal-ledger consistency note (incoherent energy enters Komar at the same $\sqrt{S}$ weight — consistency-class,
GR does likewise). **OPEN WALK (named, not walked):** the core-holding blob as candidate "phase-organization
without circulation — coherent but not winding" (see Entry 15).

> **🔴 UPDATE 2026-07-15 — the two-tank REGISTERED CHECK has FIRED (PR #707 `analysis/two-tank-decoherence-check`, `research/2026-07-15_two-tank-decoherence-check_NOTE.md`): verdict `ADDITIVE-ARTIFACT`.** The Op14 kernel ON/OFF mechanism control proved the observed relative-phase diffusion is **additive wave-interference**, not the `bath→A²→S→clock-rate` mechanism (kernel-excess median 0.187 < 0.50, collapsing to −0.001 on bath densification; `D_ON(u)` exponent p=0.38; isolated Op14 phase BOUNDED ~0.10, reversible; controls machine-clean ~7–9×10⁻¹³ rad; mean-shift additive-dominated, kernel-predicted −1.6×10⁻³ an order below the +1.7×10⁻² additive floor). **Consequences:** (1) ★#1 "temperature = phase-diffusion width/rate" **DEMOTES to NOT-DEMONSTRATED-AS-POSED / RE-GATED** — a lossless kernel yields only bounded reversible dephasing, so a genuine diffusion-**rate** thermometer needs **irreversibility** (the F6 channel below); NOT killed, re-gated. (2) ★#2 (entropy) stays PROPOSED (untested by this check). (3) **The Ax3 line "heat = reversible phase-scramble, not loss" is CORROBORATED** — the bounded reversible dephasing IS that statement measured (now axiom-derived + check-corroborated). (4) The leaf's registered "monotone variance-growth" bar was INSUFFICIENT (passed on the artifact) → criterion upgraded to mechanism-gated (kernel ON/OFF excess ≥ 0.50); orchestrator adjudication, Grant-vetoable. Landed in `thermal-phase-registers.md` §1/§2/§4/§6 + `translation-circuit.md` §4 heat row.
>
> ★ **THE F6 CONVERGENCE NOTE (prioritization datum for Wave 1+).** The thermal walk **independently rediscovered** that the **unbuilt F6 irreversible $\varepsilon\to T2$ depletion channel** is the missing primitive: it is now required by **BOTH** (a) the **DE-tracks-matter chord gate** (the engine-architecture make-or-break, `engine-capability-map`/F6) **AND** (b) the **lattice thermometer** (a genuine diffusion-rate temperature needs the irreversibility a lossless kernel cannot supply). Two independent load-bearing arcs now point at the same unbuilt primitive — a convergence that should **raise F6's build priority** in the Wave 1+ ordering.

### ENTRY 15 (WALK-RECORD — Grant verbatim "yes, this makes sense, fire the test"; the discriminating ablation FIRED as a sibling lane): THE CORE-HOLDING BLOB WALK

**The datum.** In the absorbing-box run the fixed core ball **+50.6%** absolute (phase-averaged) while the
interior drains **−17.5%** and $H$ **−12.2%** through the sponge; the torus twin core decays **−24.4% (`pair`) /
−27.6% (`graded_a0`)** — the banked quiet-avg absolute core-ball decays ($H$-conserved; `research/2026-07-14_gpersist-meter-circuit-ontology.md`:231,:284). The composed-register (kinetic-inclusive
CF) falls are **larger (~−41 to −47%)** but are **NOT BANKED** — the #689 meter-register call is open, and the
composed numbers were ESCALATED / held out under the cluster-3 STOP rule (`research/2026-07-14_gpersist-localization-observable_RESULT.md`:359; `_orchestration/2026-07-14_batch-outcomes-and-actions.md`:76). φ/winding **dead throughout** — energy flows inward, no circulation. *(🔴 Rule-12 provenance/irony note, 2026-07-15: the "−24 to −43%" this correction removes carried a −43% upper bound that was itself an **endpoint single-phase-moment read** (≈−42.9%, the #698 review's live-fire endpoint) — the exact endpoint-vs-quiet-window mirage class **Ruling 10** (this docket) and **Entry 14** document; the banked quiet-avg −24.4/−27.6% is the honest datum.)*

**The mechanism fork walked.** **(A) LINEAR MODE-SORTING** — the sponge as a sieve (radiative components leave,
bound near-field components cannot; predicts a plateau at the bound fraction, does **not** naturally predict an
absolute RISE). **(B) NONLINEAR SELF-TRAPPING** — the self-dug well (live kernel: elevated core amplitude loads
its varactors, $C_{eff}$ rises, local wave speed drops ⇒ the core is a **slow-wave lens** gathering interior
energy; the torus wake re-stirs the trap every lap so dispersion wins there; the box removes the wake so the well
is unopposed — Kerr self-focusing in the lattice's varactor form). **(C) boundary artifact** (control candidate;
weakened by the #698 guard / fixed-region tests). **The discriminator:** kernel-OFF ablation + amplitude sweep
(superlinear holding + a threshold = the (B) signature) — **FIRED**, branch `analysis/blob-ablation-kernel-off`.

**THE PUDDLE / SOLITON CARVE (walk-level).** Two binding classes — **soliton = topological binding** (winding
holds a ring of cells at refusal; quantized; floor-protected) vs **puddle = dynamical binding** (energy in its own
index well; unquantized; metastable, evaporates when stirred). The blob = **candidate first clean puddle sighting
= "phase-organization without circulation."** The **wake-kills-puddles selection observation** (walk-level):
recirculating radiation stirs dynamical traps apart — a selection-pressure argument for why persistent matter is
topological. **BREATHER HYPOTHESIS (flagged, routed to Grant, NOT ratified):** a self-trapped non-winding
kernel-dependent lump = the mobile-discrete-breather class *at rest* — a candidate upgrade for the FPB carrier
fork (`research/2026-07-09_highE-carrier-fpb-corner_walked-framing.md` branch (ii)) from posited to
engine-observed.

★ **CENSUS STAGE-2 DESIGN CONSEQUENCE (record as REQUIRED-if-B / RECOMMENDED-if-A, pending the ablation):** the
Stage-2 prereg carries a **kernel-OFF twin control** + a **puddle-vs-knot discriminant column**, since a driven
walled cavity grows puddles regardless of topology if (B) holds.

### NEXT-STEPS REGISTER (2026-07-15 update; the held queue)

- **WALKS REMAINING:** ~~core-holding blob~~ **WALKED (Entry 15)** — the ablation is IN FLIGHT; Re/Im carve; Op14 $Z$
  sign; r_knee consumer.
- **REGISTERED CHECKS (2026-07-15 status):** the **Op4 ladder integral** — **REPORTED** (PR #704, NO-MATCH → Ruling-11 register-identity; scope label routed to Grant) · the **two-tank decoherence check** — **REPORTED** (PR #707, `ADDITIVE-ARTIFACT` → ★#1 temperature-def demoted / RE-GATED on F6; Ax3 line corroborated) · the **blob ablation** (`analysis/blob-ablation-kernel-off`, kernel-OFF + amplitude sweep) — **IN FLIGHT**. Also registered: the **thermal-ledger note** (consistency-class); the **criterion-tag sweep** — **QUEUED** (Grant ratified Ruling 12's mandate 2026-07-15).
- **WAVE 1 parked:** $T_{ij}$ build gate-first + X44b / gate-(b) / census-S2 / QED-log charters — all fed by
  Rulings 6/11 (and now the Entry-15 Stage-2 kernel-OFF-control consequence). **★ F6 priority-raise datum (Entry 14 convergence note):** the unbuilt F6 irreversible $\varepsilon\to T2$ channel is now required by BOTH the DE-tracks-matter chord gate AND the lattice thermometer (PR #707) — a two-arc convergence on one primitive.
- **STANDING:** CVR session; 0.22/0.84; half-exponent clock Q4 OPEN.

### Docket status board — register-walks state (KEEP-BOTH; all tables above unedited)

| Ruling / Entry | What | Status (2026-07-15) | Adjudicator |
|---|---|---|---|
| **Ruling 11** | step-register: kernel eats field-strain, not voltage-strain; the ladder theorem | **RULED** (Grant "Yes, I agree with where the walk is ending up") — FORM-level ruled convention; Op4 ladder integral REGISTERED-not-run; `clm-strreg` | Grant (ruled) |
| **Ruling 12** | two α-criteria (storage-α vs response-α); the Taylor-½; criterion-tag mandate | **RULED** (Grant "ratify" 2026-07-15; upgraded from WALK-DELIVERED) — criterion-tag mandate **RATIFIED**→sweep QUEUED; `clm-crit2a` | Grant (ruled) |
| **Entry 13** | the saturation anatomy (C/L duality, node exhaustion, ring-of-refusal electron, rectification) | **WALK-RECORD** — framework, landed in `envelope-anatomy.md` + `translation-circuit.md` §4 | (framework; no ruling) |
| **Entry 14** | thermal/phase-register walk (Q1/Q2/Q3 + 3-register unification) | **WALK-RECORD; two-tank check FIRED (PR #707, `ADDITIVE-ARTIFACT`):** ★#1 temperature-def **DEMOTED / RE-GATED on F6**; ★#2 entropy stays PROPOSED; Ax3 line **corroborated**; criterion upgraded to mechanism-gated (Grant-vetoable); F6 convergence-priority datum | Grant (definitions re-gated; criterion + F6-priority to ratify) |
| **Entry 15** | core-holding blob walk (A linear-sort vs B self-trapping; puddle/soliton carve; breather) | **WALK-RECORD** — Grant "fire the test"; discriminating ablation IN FLIGHT (`analysis/blob-ablation-kernel-off`); breather hypothesis flagged-not-ratified | Grant (ablation adjudicates; breather routed) |

*Append-only continuation (2026-07-15, the register walks) — all prior docket content byte-untouched (origin/main
region, first 129045 bytes, sha256 `f524a695…`). Cites verified two-method at merged base `origin/main`
`6f203072` (post-#702). Landed KB-leaf-first: `strain-registers.md` (`clm-strreg`/`clm-crit2a`, FORM-class
solidity 0.45), the `envelope-anatomy.md` saturation-anatomy + Q2 additions, the `thermal-phase-registers.md`
WALK-LEVEL no-claim leaf, and the `translation-circuit.md` §4 rows. DO-NOT-MERGE; only the orchestrator/Grant
merges. Ruling-status precision is the prime rail — RULED items are FORM-level ruled conventions, not
derivations; nothing here canonizes a value.*

---

## Continuation — 2026-07-15 (anchor-sweep): Entry 15 + next-steps status flip

**Trigger:** PR #706 MERGED (`816054bf` ancestry; merge `d138818b`, 2026-07-15T13:32:10Z) while the Entry-15 / NEXT-STEPS REGISTER rows above still read "IN FLIGHT". Hardware-ratings-map anchor sweep (companion PR) caught the staleness; this append flips status only — prior prose KEEP-BOTH.

| Row | Prior status (above) | Current status (2026-07-15 sweep) |
|---|---|---|
| **Entry 15 ablation** | IN FLIGHT (`analysis/blob-ablation-kernel-off`) | **REPORTED / MERGED** — PR #706; verdict **MODE-SORTING** (`research/2026-07-15_blob-ablation_NOTE.md`); puddle/breather = not-supported-at-this-config; census-S2 kernel-OFF twin → **RECOMMENDED-cheap-control**; **F1 DEFECT-CANDIDATE** surfaced (Grant adjudication + consumer audit queued) |
| **NEXT-STEPS blob line** | "the ablation is IN FLIGHT" | ~~IN FLIGHT~~ → **REPORTED (#706)** |
| **REGISTERED CHECKS blob** | IN FLIGHT | **REPORTED (#706, MODE-SORTING)** |

**Not flipped here (still open / Grant-gated):** Op4 scope ruling; two-tank criterion (Grant-vetoable); ~~F1 adjudication~~; breather hypothesis (flagged-not-ratified); Wave-1 parked items; CVR session.

---

## Continuation — 2026-07-15 (Grant in-chat): F1 ★RULED DEFECT + F6 field channel GO

| Item | Ruling | Consequence |
|---|---|---|
| **F1** | **★RULED — DEFECT** (Grant: "1. fix it") | Cosserat load must reach bond Γ. Fix: `K4Lattice3D.external_z_local=True` under `CoupledK4Cosserat`; `_scatter_all` skips V-only overwrite. Regression `test_f1_shared_front_ordering.py`. Consumer-audit completion of HIGH V-active banked rows remains registered (not blocking). |
| **F6 field channel** | **★GO** (Grant: "2. proceed") | Charter accepted. Prereg frozen + first rung fired: **CHANNEL-BOUNDED** (`research/2026-07-15_f6-field-channel_prereg_FROZEN.md` §5) — occupancy-slaved parallel latent→bath ledger on live lattice; in-Hamiltonian ε depletion still queued as deeper rung. |

Package: `_orchestration/2026-07-15_f1-adjudication-package.md`. Charter: `research/2026-07-15_f6-field-channel_CHARTER.md`.

---

## Continuation — 2026-07-15 (keep-going): F1 consumer audit + F6 rung-2

| Item | Status |
|---|---|
| **F1 consumer audit** | Landed `_orchestration/2026-07-15_f1-consumer-audit.md` — scheduling only; top-3 cheap RE-RUNs queued; no verdict flips |
| **F6 rung-2** | Prereg frozen + fired: **BIAS-MOVED** (in-Hamiltonian V scale-down kills bias≠release / couples into core). Rule-11: do not retune. Next door class ≠ scale-down |
| **Thermometer re-fire** | `research/2026-07-15_thermometer-refire_prereg_GATED.md` — gated on a CHANNEL-BOUNDED in-Hamiltonian door |

---

## Continuation — 2026-07-15 (Grant in-chat): ℏ-as-FD unbanked + Re(Z) absorb forbidden as plan

| Item | Ruling | Consequence |
|---|---|---|
| **ℏ = lattice FD constant?** | **UNBANKED** (Grant: form not derived) | Canonical FDT remains classical Nyquist / ℏ-free (`clm-eaiqj1`). Not a FORM/VALUE 5th-instance workstream. Ratings-map §1 + parent F6 charter demoted. |
| **Next F6 door = “Re(Z) absorb”?** | **FORBIDDEN as the plan** (Grant: most honest path) | Discriminator charter: `research/2026-07-15_f6-mode-count-door_CHARTER.md` — mode-count irreversibility without sub-yield friction; fool-mode-3 / FRICTION-RENAMED first-class. Ax3 retirement knife preserved. |
| **#693 + #707** | Keep **separate** | Do not narrate as “one fact, two measurements.” |

---

## Continuation — 2026-07-16: F6 mode-count Arm A fired BIAS-MOVED

| Item | Status |
|---|---|
| **Prereg freeze** | `17662232` pushed **before** driver (Step 3.11) — `research/2026-07-16_f6-mode-count-event-gated_prereg_FROZEN.md` |
| **Arm A fire** | **BIAS-MOVED** — ΔN_occ=64 (mode-count LIVE); ΔS_core≫BIAS_TOL; soft ledger messy. Rule-11: do not retune. |
| **Sabotage** | `--sabotage-friction` → **FRICTION-RENAMED** (Discriminator 7 pass) |
| **Thermometer** | remains GATED |

### Post-#711-review corrections — 2026-07-16 (append-only; supersede the row above where cited)

Independent adversarial review of PR #711 (11 findings confirmed, 1 refuted): the **BIAS-MOVED verdict survives** (independent `S_core` knife), the **detector infrastructure is void**. Corrections (repairs landed on `analysis/2026-07-16-f6-mode-count-event-gated`):

- **"ΔN_occ=64 (mode-count LIVE)" RETRACTED** (findings 0/4/7): ΔN_occ = min(M_MODES, N_SPREAD × event-steps) — it reads the 64-slot accumulator dimension, **not** a physical mode-count. Bookkeeping liveness only. The twin-64 across #711/#713 is the shared array size, **not** independent corroboration — do not cite it as such.
- **FRICTION-RENAMED control = flag readback** (finding 5): production and `--sabotage-friction` are bit-identical except the `credit_modes` side-array increment (bath/field/core/events/soft_ledger/ΔS_core all identical; only N_occ differs 64 vs 0). The control verifies the credit path executes — it cannot fail on any energetic run; vacuous as a physical discriminator. **No-smuggle rail PASSED**: conservative bookkeeping, `_phase_scramble` preserves Σ_p V_p² sitewise, no Re(Z), no ℏ-FD — the void is the meter, not a hidden dissipator.
- **★ DETECTOR-REBUILD GATE (mandatory)**: before any future F6/R7 arm banks CHANNEL-BOUNDED or ungates the thermometer re-fire, the mode-count detector must be rebuilt as a real bath DOF (dynamics/frequencies + back-reaction) AND paired with a FRICTION-RENAMED control that varies a physical quantity (not the `credit_modes` flag). Tracked in ratings-map §7 / R7 next-drive.
- **"soft ledger messy" CORRECTED** (findings 1/6/9): it was an E0-capture accounting artifact — E0 was measured pre-step-1 on an off-shell seed whose energy doubles exactly at the first TLM connect, so soft_ledger ≡ E0 for any transfer and the lossless OFF control itself blew the criterion; **CHANNEL-BOUNDED (the only ungate bin) was structurally unreachable as shipped.** Harness repaired (E0 captured post-connect): corrected soft_ledger = 0.079 (field drop 7.634 vs bath credit 7.555 = 1.03% of on-shell E0); OFF control now passes; verdict BIAS-MOVED unchanged. Not "messy physics."
- **Multi-kill co-fire** (findings 3/8): the fired run also satisfies **ELECTRON-DRAIN** (87.3% protected-core drain vs DRAIN_TOL 5%). As shipped it also tripped the soft-DETONATE clause, but that was the cluster-3 artifact (fired on the OFF control too) and no longer fires post-repair. classify() precedence was never frozen → BIAS-MOVED was precedence-selected. Reporting rule frozen for future arms: report ALL satisfied bins; freeze precedence pre-fire. All bins co-directional → kill stands (run is more dead, not less).
- **BANKED (Rule 11)**: Arm A **BIAS-MOVED** stands on ΔS_core=1.421e-1 ≫ BIAS_TOL 5e-3 (**28×**) — event-gating does not evade the protected-core knife. The negative is real and banked; thermometer stays GATED; not CHANNEL-BOUNDED. No retune (the two driver changes are fidelity repairs leaving the verdict invariant). NOT banked: "mode-count LIVE" / the FRICTION-RENAMED control (await the detector-rebuild gate).

---

## Continuation — 2026-07-16: F6 mode-count Arm A BIAS-MOVED + frontier map charter

| Item | Status / ruling | Consequence |
|---|---|---|
| **Arm A (event-gated occupancy)** | **BIAS-MOVED** (PR #711 open at fire time; prereg `17662232` before driver) | Mode-count detector LIVE (ΔN_occ=64); bias knife still kills. Rule-11: do not retune. Sabotage → FRICTION-RENAMED. |
| **Freeze causal arrow** | **★WALKED (Grant 2026-07-16)** | Crystallization **releases** latent heat; drain does **not** drive formation. AM / `Ω_freeze` residue = frozen IC (`u0*`, chirality, `J`) — **not DE**. |
| **Orthogonal release geometry** | **CONJECTURE** (Grant challenge) | Not a proven derivation. Map forks G0–G3; Tier-0 default **G0**. Do not bake normal-to-surface into pass criteria. |
| **Frontier map charter** | Landed `research/2026-07-16_f6-frontier-map_CHARTER.md` | Full N→N+1 mint = **NO** (`node_creation` absent). Tier-0 Arm B exterior-leave = **gated on Grant GO**. F6 occupancy ≠ frontier (KEEP SEPARATE). |
| **SM/QED fence** | Reaffirmed | No ZPE/Λ-as-ontology/ℏ-FD/Re(Z) absorb as door. T2 primary; CMB/Kerr peer-check only. |
| **Thermometer** | remains GATED | Needs CHANNEL-BOUNDED + V-phase coupling the clocks see. |

---

## Continuation — 2026-07-16: F6 Arm B G0 exterior-leave fired BIAS-MOVED

| Item | Status |
|---|---|
| **Grant GO** | Tier-0 Arm B under frontier map — GO (in-chat "go") |
| **Prereg freeze** | `5bda8777` pushed **before** driver (Step 3.11) — `research/2026-07-16_f6-arm-b-exterior-leave_prereg_FROZEN.md` |
| **Arm B fire** | **BIAS-MOVED** — exterior ΔN_occ=64 (mode-count LIVE); \|ΔS_core\|≫BIAS_TOL; soft ledger messy. Rule-11: do not retune. |
| **Sabotage** | `--sabotage-friction` → **FRICTION-RENAMED** |
| **Sponge control** | PML-without-ports → NULL (not CHANNEL-BOUNDED) |
| **Geometry** | **G0** only — no orthogonal claim |
| **Thermometer** | remains GATED |
| **Full frontier mint** | remains NO (`node_creation` absent) |

---

## Continuation — 2026-07-16: F6 circuit-first repair (Arm B WRONG-OBJECT)

| Item | Status / ruling | Consequence |
|---|---|---|
| **Arm B object** | **WRONG-OBJECT / CATEGORY-WRONG** (bin **BIAS-MOVED** preserved) | Unsaturated face \(V\)-siphon ≠ native K4 port refusal at wall (\(\lvert\Gamma\rvert\to1\)). Siphon class **closed**. No retune; no Arm C siphon. |
| **Circuit-map gate** | Mode-count door **§5b** mandatory before any arm freezes | Filled port/regime/Γ/energy-fate table — not ban-list theater. |
| **Circuit-first door map** | Landed `research/2026-07-16_f6-circuit-first-door-map_CHARTER.md` | A1 wall vs frontier mint vs F6 KEEP SEPARATE; **reflection ≠ T2 leave**. |
| **Frontier map** | Arm B demoted from “necessary door” to killed costume; fool-mode 9 banked | Full mint still NO; thermometer GATED. |
| **Next field spend** | Frozen until §5b-passing prereg | Default: wall-native consistency probe (not DE door) or wait on node-mint epic — not chosen here. |

---

## Continuation — 2026-07-16: §5b rigorous fill PROTOCOL banked

| Item | Status |
|---|---|
| **Fill PROTOCOL** | Landed `research/2026-07-16_f6-circuit-map-fill-PROTOCOL.md` — binding for mode-count §5b |
| **Rule** | Each row = claim \| cite \| observable; entailment knife on energy fate; pre-freeze pass (1)–(6) |
| **Arm B** | Worked-fail example in PROTOCOL §3 (preserves BIAS-MOVED + WRONG-OBJECT) |
| **Next arm** | Probe-first for S/Γ; freeze only after PROTOCOL PASS — no door backfill |

---

## Continuation — 2026-07-16: F6 Arm A/B adversarial-review repair (mode-count DEMOTED; twin-64)

> Append-only Rule-12 supersession of the "mode-count detector LIVE (ΔN_occ=64)" banking at **Entry rows :1490 (Arm A)** and **:1505 (Arm B)** above. Verified two ways (production driver `--json` + independent monkeypatch probe) at branch `docs/2026-07-16-f6-circuit-first-repair`. Bins/verdicts unchanged.

| Item | Status / ruling | Consequence |
|---|---|---|
| **Mode-count "LIVE (ΔN_occ=64)"** | **DEMOTED** → "deposit path intact (`ΔN_occ≥1`; magnitude = the `M_MODES` knob) — code-flag self-test, NOT a physical mode-count measurement" | `ΔN_occ ≡ M_MODES` by construction; live-fire `M_MODES∈{16,48,64,128,256}→ΔN_occ={16,48,64,128,256}`, `E_bath=5.776694` invariant; `b[m]` write-only, zero back-reaction. Applies to **both** :1490 and :1505. |
| **Twin-64** | Arm A interior 64 = Arm B exterior 64 = **same `M_MODES=64` constant printed twice** | Not two geometries converging on a measurement. |
| **FRICTION-RENAMED** | Reachable **only** by the `--sabotage-friction` plant (`credit_modes=False`) | Unreachable by production physics; discriminates bookkeeping code-path, not a physical magnitude. |
| **BIAS-MOVED (survivor)** | **Preserved** — rests on `ΔS_core=−0.017146` (bookkeeping-independent) | The kill and WRONG-OBJECT closure stand; only the mode-count-LIVE leg is void. |
| **Detector rebuild** | **MANDATORY GATE** before any CHANNEL-BOUNDED bank / thermometer ungate | Real bath DOF + back-reaction + a physical control that can fail on physical inputs. Registered jointly with the **#711** (Arm A) repair — cross-cite. |

---

## Continuation — 2026-07-16: F6 Arm B E0 baseline bug fixed (soft ledger closes)

> Append-only Rule-12 supersession of the "soft ledger messy / ≈3.73" banking at **Entry row :1505** above. Driver fix (not a knob retune); lattice trajectory byte-identical (survivors unchanged). Two-method verified.

| Item | Status / ruling | Consequence |
|---|---|---|
| **Soft ledger "messy" (≈3.73)** | **ARTIFACT** — booked vs the raw V_inc-only seed `E0` | First step equilibrates; OFF energy doubles **exactly 2.000000×** (`3.839→7.678`). `soft=|(E0−E_f)−E_bath|≈E0` identically → the CHANNEL-BOUNDED **pass bin was structurally unreachable**. |
| **Fix** | Book vs equilibrated baseline `E_equil` (post-step-1; `RunOut.E_field_equil`) | Honest ledger **closes at 1.443 %** (`soft=0.110790` vs `E_equil=7.678`); PASSES `0.5·E_equil`; OFF ledger ≈ `5.3e-15`. |
| **Verdict** | **BIAS-MOVED unchanged** | Decided at bias step, upstream of soft-ledger DETONATE; WRONG-OBJECT closure independent. |
| **Propagation** | Same E0 convention flagged to **#711** (Arm A) | Same bug class — coordinate wording. |

---

## Continuation — 2026-07-17 (Grant in-chat): PRODUCT/TRANSITION split RATIFIED · retention row R13 · yield-fork ruling

> Append-only. Evidence base: the Regime-IV dissipation audit `research/2026-07-17_regime-iv-dissipation-audit.md` (workflow `wf_3f83fc66-6f5`; 126 items; final distribution **49 RETENTION-ONLY / 24 RADIATIVE-PORT / 19 LOSS-REQUIRED / 29 AMBIGUOUS / 5 RATE-CLAIM**; verify 8 OVERTURNED / 33 WEAKENED / 38 UPHELD / 47 NO-VERIFY). Three sub-entries continue the shared Ruling/Entry sequence (last = Entry 15).

### RULING 16 (RULED — Grant in-chat 2026-07-17): THE PRODUCT / TRANSITION SPLIT — RATIFIED as corpus discipline

**Ruling.** The loss/irreversibility vocabulary names **two physically distinct moments**, and load-bearing prose must declare which: **PRODUCT** — persistence of a latched state (winding integer / $\Gamma=-1$ cavity / retained order parameter), **LOSSLESS** per canon, no maintenance R; vs **TRANSITION** — the irreversibility of the crossing, an arrow **licensed only from counting** (mode-spread with reconvergence ≈ 0, or the energy-conserving click), **never a valve**.

| receipt | content |
|---|---|
| `master-equation.md:20` | the two orthogonal "3"s (A1 dilatation-mass ⊥ T2 winding) — two objects, two latches |
| `electron-identification.md:97` | "Two-reason trap: topological (the loop cannot untangle) + impedance — both independently prevent decay" |
| `resonant-lc-solitons.md:104-108` | $\Gamma=-1$ lossless persistence "partly follows from the lossless axiom itself" (consistency-class, not a chord) |
| tier-1 charter `research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md:256` | "the arrow comes from mode-count or a click, **never a valve**" |
| R10-fixed-n charter `research/2026-07-12_remanence-r10-fixed-n_CHARTER.md:108` | precedent: "the retained order parameter, not the crossing loss, is what must survive drive-off" |

Canonized as the discipline leaf `manuscript/ave-kb/common/retention-transition-split.md` (batch D4).

### DECISION 17 (Grant in-chat 2026-07-17): retention lands as a NEW ratings row R13 (KEEP-BOTH)

**Decision.** Retention (zero-drive persistence) is added as a **new** row **R13** on the hardware-ratings map (`_orchestration/2026-07-15_hardware-ratings-map.md`), **KEEP-BOTH** (a new axis alongside legacy; nothing redefined-in-place).

**R-number collision — disambiguated by cross-note, neither renumbered:** the engine-capability-map's internal "**R10**" (the remanence gap; `engine-capability-map.md:65,:80`, §3.3 *Anhysteretic ↮ loop*) is a **different namespace** from the ratings-map's **R10** (*Overclocking / driven selection*). Retention content lives in the ratings-map's **R13**; a footnote on the ratings-map records the two-namespace fact. Do **not** renumber either.

### RULING 18 (RULED — Grant in-chat 2026-07-17): THE YIELD-FORK RULING — lean recorded, fork OPEN

**Ruling.** On the near-yield crossing — **finite-area memristive loop ($\oint S\,dr \neq 0$, dissipative) vs zero-area saturating reactance (lossless refusal)** — Grant's **reversible-reactive lean is RECORDED AS A LEAN**; the **fork stays OPEN**; resolution is by the substrate via the **registered discriminators**, not by fiat:

1. the thixotropy amplitude-dependent-τ prereg `research/2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md` (FROZEN, un-run);
2. the pre-registered `P_phase5_memristor_loop_area` prediction (`tau-relax-derivation.md:109`, UNRUN).

Until one fires, the Vacuum Memristor Level-2 loop is LOSS-REQUIRED *by its own prose construction* but **not axiom-forced** (the resistor is asserted at the crossing, not derived; $\tau_{relax}=\ell_{node}/c$ derives from lossless causality). Substrate adjudicates; Grant leans reversible.

---

## Continuation — 2026-07-17: F6 bath-meter §7 ruling + NONLINEAR REVALIDATION lane opened

**Append-only, dated block.** Records the Grant §7 ruling on the F6 bath meter and opens the implementer lane that executes its mandatory prerequisite. Companion: charter `research/2026-07-16_f6-bath-meter_CHARTER.md` (Amendment §B, frozen this date, pre-registered before any battery code).

### RULING 19 (RULED — Grant in-chat 2026-07-17, "Proceed with 1"): F6 BATH-METER §7 MECHANISM — ACCEPTED-AS-METER-WITH-TARE, within the validated envelope

**Ruling.** On the §A8 V5-decomposition evidence (the shipped global-rescale back-reaction is ~90% uniform amplitude attenuation + ~10% genuine spatial restructuring; trajectory divergence D=0.154, best-fit global scalar c=0.8533 = √(1−E_bath/E0) to 4 sig figs, spatial residual 4.8%):

1. **§7 mechanism ACCEPTED-AS-METER-WITH-TARE (within the validated envelope).** The back-reaction is accepted as a **meter carrying a tare**, not an unqualified two-way coupling. The certificate stands only inside the envelope on which it was validated (cold plant, `nonlinear=False`, mild A_max≈0.16).
2. **The tare rule.** Any future F6 arm that keys on a **spatial** discriminant MUST first tare it by the computable global scalar **`c = sqrt(1 − E_bath/E0)`** (subtract the ~90% uniform-attenuation component; key only on the residual spatial shape `‖ON − c·OFF‖`). `c` is computable and non-fitted (= the §A8 best-fit c to 4 sig figs), so an arm applies it without a per-run calibration loop.
3. **Nonlinear-regime revalidation = MANDATORY PREREQUISITE.** No F6 arm may key on irreversibility until the meter is revalidated with the amplitude-dependent saturation kernel ON. The central risk: §A1's conservation argument is LINEAR ("a scalar multiple of an on-shell TLM state stays on-shell"), and with S(A)=√(1−A²) amplitude-dependent, a scalar multiple of a nonlinear on-shell state is NOT on-shell — the global energy-matched rescale may re-introduce a secular pump exactly in the regime the arms need.

### ENTRY 16 (2026-07-17): implementer lane opened — F6 meter nonlinear revalidation (W-battery)

**Lane.** Executes RULING-19 item 3. Charter §B (this date) pre-registers a nonlinear battery **W1–W6** with all thresholds + verdict classes frozen before code: W1 nonlinear lossless baseline (plant integrator floor), **W2 ★kernel-ON coupled drift (the decisive leg; KILL on a secular pump)**, W3 detuning soul-check (harmonic-controlled), W4 N_occ honesty under self-generated harmonics, W5 tare-rule check (fitted-c vs computed c; spatial-residual-vs-operating-point trend), W6 envelope restatement. Three operating points: mild (A_max≈0.10), moderate (≈0.30), near-knee (≈0.50). Verdict classes: METER-VALID-NONLINEAR-ENVELOPE / METER-PARTIAL-NONLINEAR / METER-INVALID-NONLINEAR. **NO F6 arm/door fires in this lane.**

**★Substrate-native finding surfaced at lane open (flag-don't-fix; folded into §B1).** `nonlinear=True` is a **no-op** given `op3_bond_reflection=True` (empirically identical dynamics to ~1e-15; the K4 4-port scatter matrix `build_scattering_matrix(z)=2y/(4y)−δ` is z-independent). The amplitude-dependent kernel flows through **`op3_bond_reflection`** (`z_local=(1−A²)^(−1/4)` at bond Γ), which is ON in the validated cold plant already — so the nonlinearity knob is **amplitude (seed scale)**, not the flag. The rescale-non-commutation `|step(s·x)−s·step(x)|` was measured to grow ~30× across the operating points (1.8e-4 → 5.4e-3), confirming the §A1 on-shell violation is real and amplitude-growing. Co-decisive hypothesis (tested, not asserted): conservation is ledger-enforced (rescale removes exactly Δe_bath; op3 is power-conserving), so the pump may NOT resurrect via the stated mechanism while fidelity degrades (W5 residual growth). W2 + W5 co-decisive; substrate adjudicates.

---

## Continuation — 2026-07-18: F6 COUNTING-ARROW ARM opened + Phase-1 fired (recurrence-sweep) → FALSIFIED

**Append-only, dated block.** Opens the F6 counting-arrow arm (the recurrence-sweep arm, consuming the RULING-19 meter as certified) and records its Phase-1 fire. Companion: prereg `research/2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md` (frozen-by-push **2026-07-18T00:36:15Z**, before any driver), result `research/2026-07-18_f6-counting-arrow-arm_result.md` + `.json`, driver `src/scripts/vol_1_foundations/f6_counting_arrow_arm.py`, §5b probe `src/scripts/vol_1_foundations/f6_counting_arrow_probe.py`.

### ENTRY 17 (2026-07-18): implementer lane — F6 counting-arrow arm (recurrence-sweep), Phase 1

**Lane.** Grant ratified in-chat 2026-07-17/18: Q1 = the ladder (Phase-1 sub-yield first; Phase-2 near-knee gated on Phase-1 banking, `A≤0.5` W-certified band); Q2 = the sparse-vs-dense recurrence sweep as the kill-shape; 377-Ω framing adjudicated **FORM-derived / VALUE-instrument-calibrated** + a secondary non-gating self-termination companion leg. The arm tests the **TRANSITION crossing-arrow license** (`retention-transition-split.md`: "licensed only from counting … never a valve"): energy leaving the E-sector ε-store fails to RETURN iff the recurrence horizon `T_rec=2π/Δω` exceeds the observation window. Observable `R_return(x)`, collapse variable `x=T_window·Δω/2π`. Instrument = `LatticeBathCoupler` (**byte-untouched**); plant = standalone-K4 (within the meter certificate; #721 R-1 SCOPE CAVEAT; CHANNEL-BOUNDED bin defined energy-conserving = consistent with the identity ledger). **NO Phase-2 fire in this lane.**

**★VERDICT (Phase 1): the frozen recurrence-collapse prediction is FALSIFIED — as a NULL-OF-REGIME.** Every declared grid value ran (6-comb density sweep `Δω∈{0.010…0.080}` + two-tank control + OFF + tared bias). The two headline criteria fail **decisively**: collapse `spread(x_50)=7.347` (vs frozen `<0.30`, 25× over) and transition `mean(x_50)=7.577` (vs frozen `[0.7,1.5]`). **Single mechanism (explains all failures):** the collar-drive from a settled K4 lattice is **narrowband** (`ω_d≈0.54`), filling only a narrow drive-linewidth **few-mode sub-band** (`N_occ≤3` at horizon, ≤~10 transiently, `≪ M`), and the **weak-κ transfer is SLOW — `τ_transfer≈5·T_rec ≫ T_rec`**, the *inverse* of the prereg's assumed Wigner–Weisskopf clean-separation. The return is coupling/detuning-controlled (peaks `x≈5`), NOT comb-recurrence-controlled (`x=1`); changing `Δω` moves `T_rec` but not `τ_transfer`, so `R_return` does not collapse in `x`. Conservation identity-audited green (`9.4e-14`); two-tank reversibility positive control reproduced (`R_cum[10]=0.987`) — the instrument is live, the null is regime.

**★FLAG (flag-don't-fix; ROUTED TO GRANT).** The frozen driver returns **`FRICTION-RENAMED`**, but this is a **semantic misfire**: prereg §4 mapped criterion-7 (`N_occ dense > sparse`) → FRICTION-RENAMED and the decision-tree checks it before the FOREIGN-EATER branch, so `N_occ dense (1) > sparse (1)`=False short-circuits. The door charter's FRICTION-RENAMED (§4 bin vi) requires `N_occ` **not** increasing from zero (Ax3-illegal dissipation) — but here `N_occ 1–3 > 0`, energy is **stored reversibly and returns** (conserved to `9e-14`): **no dissipation**. The mechanistically-correct frozen bin is **FOREIGN-EATER** ("return NOT tracking x → INSTRUMENT-first"). Per **Rule 11 the classifier is NOT retuned** post-fire; the label stands as-run and the FRICTION-RENAMED-vs-FOREIGN-EATER/NULL-OF-REGIME bin is **routed to Grant for adjudication**. The physical falsification is unambiguous regardless of the bin label.

**Disposition (Rule 12: retract, do not refill).** Branch **closed negative**. Follow-ons **SPEC only** (each earns a new prereg + verification chain if pursued): (1) a **broadband-sustained-drive** redesign that can populate a quasi-continuum (changes the frozen source-off protocol ⇒ new prereg); (2) route to the **click mechanism** (X40). Companion self-termination leg (secondary/non-gating): inconclusive (`Re(Z_in)/Z_char≈0`, port retains energy — consistent with no-quasi-continuum). Untouched: depletion-rate rung `Γ=3Hρ_latent`; meter certificate (standalone-K4 identity intact). **This is Rule-10 empirical-driver discipline working at full strength** — the prereg physics argument was sound for an idealised comb; the integrator revealed the drive never populates it.

---

## Continuation — 2026-07-18 (post-#722-review): ENTRY 17 disposition SCOPED (append-only; ENTRY 17 header untouched)

**Append-only, dated block.** Supersedes the **"FALSIFIED" adjacency** of the ENTRY 17 ★VERDICT above with the scoped wording below (the ENTRY 17 bytes are left untouched; this continuation is the current-status record). Repairs landed under PR #722 review R-1…R-10.

**★DISPOSITION (scoped).** **Banked:** the frozen recurrence-collapse **PREDICTION is FALSIFIED at the frozen `κ=0.012`** (collapse `spread(x_50)=7.35` vs `<0.30`; transition `mean(x_50)=7.58` vs `[0.7,1.5]`). **The counting-arrow QUESTION was NOT reached and REMAINS OPEN** — the regime (fast transfer + populated quasi-continuum) never existed in this run; FALSIFIED scopes to the `κ=0.012` prediction, **not** to the counting arrow (R-2).

**Verdict-structure re-bank (R-4).** `NULL-OF-REGIME` is **NOT a frozen §4 class** — it is **demoted from the banked headline to the lane's ROUTED regime-interpretation**, carried to Grant *with* the bin adjudication. Banked instead: frozen prediction FALSIFIED (κ=0.012); **shipped-classifier output = `FRICTION-RENAMED`** (fire-conditions frozen §4; tree + precedence = post-freeze implementation); **honest un-narrowed frozen reading = `FOREIGN-EATER`** (R-5: the shipped `sparse_ok` narrowed the frozen FOREIGN-EATER condition — "return NOT tracking `x`" — to a two-control check; a faithful reading fires FOREIGN-EATER on this data; code left un-retuned per Rule 11). **Bin adjudication (FOREIGN-EATER vs FRICTION-RENAMED) + `NULL-OF-REGIME` interpretation ROUTED to Grant.**

**Honesty-lag retraction (R-3, MAJOR).** The ENTRY 17 / result "Rule-10 empirical-driver discipline working at full strength … a bug static analysis could not surface" framing is **RETRACTED as FALSE**: this was a **PREREG-DESIGN MISS** — both mechanism halves were **derivable from the banked #721 meter data at freeze time** (production `N_occ`, W2 transfer rates; #721 banked `ω_d=0.52377` + per-point `transfer_frac` 0.11–0.26, and merged ~35 min before the freeze the prereg cites). The fire **confirmed**, not discovered, the mechanism.

**Provenance (R-7).** The regime-diagnosis numbers (`ω_d`, `n_pop`, `τ_transfer/T_rec`) were **prose-only** at push; a shipped `run_diagnostics` now computes them (banked `…_result.json["diagnostics"]`, NON-GATING). Re-measured `ω_d=0.524` (confirms the #721 bank; prose `0.54` was a transcription drift); `n_pop(>1%)` `{7,2,5,3,10,6}` (prose `{6,2,5,3,7,7}` — differs at 3 cells; load-bearing few-mode count is `N_occ 1–3`); `τ_transfer/T_rec` per-cell `2.3–10` (all ≫1, inversion holds).

**★Follow-on 3 (NEW, CHEAPEST — Grant-gated, NOT fired).** κ-sweep rerun of the same frozen grid (new prereg): review-probe evidence shows at `κ=0.03–0.06` the regime **IS** reached (fast transfer `x_63=0.19·T_rec`; `N_occ 15→33/47 of 71`; dense combs `R_cum=0.000`, sparse `0.793`, two-tank `0.996` controls pass) — the necessary counting shape appears; **NOT sufficient** (`x_50=nan` at dense; collapse-at-`x≈1` unshown). MANDATORY prerequisites: meter W-battery revalidation at the new κ (conservation drift `1e-14→6.8e-6@0.03→4.3e-4@0.06`), valid band bounded above by the `κ=0.12` two-tank-control break, dressed-comb/level-repulsion artifact check. **PR #722 stays DO-NOT-MERGE; owed to auditor lane: the FOREIGN-EATER-vs-FRICTION-RENAMED bin adjudication + the counting-arrow-negative closure manual entry (implementer surfaces; auditor lands).**

---

## Continuation — 2026-07-18 (Grant in-chat): F6 counting-arrow Phase-1 BIN RULED — FOREIGN-EATER (late, not eaten); FRICTION-RENAMED rejected; STORY 2 is the target

**Append-only, dated block.** Resolves the routed adjudication owed at the tail of the prior (post-#722-review) continuation — *"the FOREIGN-EATER-vs-FRICTION-RENAMED bin adjudication"* — with Grant's in-chat ruling. The **ENTRY 17** bytes and the post-#722 continuation bytes above are left **untouched**; this block is the current-status record. Companion: result `research/2026-07-18_f6-counting-arrow-arm_result.md` (§4 classifier + §7 deviations), prereg `research/2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md`, driver `src/scripts/vol_1_foundations/f6_counting_arrow_arm.py`.

### RULING 20 (RULED — Grant in-chat 2026-07-18): F6 counting-arrow Phase-1 bin = FOREIGN-EATER; FRICTION-RENAMED rejected; STORY 2 is the physics

**The read (Grant-ratified walk wording).** Grant in-chat, verbatim: *"story 2 seems important although i agree with story 3."* The three-story walk he ratified reads STORY 3 as — *"echo late, not eaten: transport-limited, governed by the port and coupling (`κ=0.012`), not the comb; nothing was lost; the counting question was never asked."* The deposit trickled in slowly (`τ_transfer ≈ 5·T_rec ≫ T_rec`, per-cell `2.3–10`) through a narrowband few-mode sub-band and returned late; it was not consumed.

**Bin RULED = FOREIGN-EATER** (of the frozen §4 taxonomy), on the **faithful frozen condition — not the shipped tree.** The frozen FOREIGN-EATER row fires here because the **return did not track the counting knob** (`x_50` spreads `3.6→11`, no collapse — the headline finding). Receipts: PR #722 review **R-5** — the shipped `sparse_ok` (`f6_counting_arrow_arm.py:247` defined / `:260` FOREIGN-EATER short-circuit; disclosed-narrowing note `:224–230`) narrowed the frozen FOREIGN-EATER condition ("return failure NOT tracking `x`") down to a two-control check, so a **faithful** reading of the frozen §4 row fires FOREIGN-EATER on this data — and the result-doc **deviations section** (`research/2026-07-18_f6-counting-arrow-arm_result.md` §7 item 2 + §4). Code left **un-retuned** per Rule 11; this RULING adjudicates the label, it does not touch the shipped output.

**FRICTION-RENAMED REJECTED.** Grant in-chat, verbatim: *"friction does seem wrong."* Grant-ratified walk wording: *"banking it would record a hidden resistor in a run that conserved to `1e-14`."* The run conserved total energy to `9.4e-14` (identity-audited, #721 R-1) and the deposited energy **returned** (`R_cum` up to `0.92`; two-tank `0.987`) — there is **no dissipation**, so the Ax3-illegal friction class (door charter `research/2026-07-15_f6-mode-count-door_CHARTER.md` §4 bin **(vi)** — "energy leaves the field but bath shows **no** mode-count / phase-space increase (Q-drop / damping alone)") does **not** fire. The shipped-classifier's `FRICTION-RENAMED` output stands recorded as a **semantic misfire** (Rule 11, un-retuned) — explicitly **NOT banked as the bin**. **NOT FRICTION-RENAMED** (ratified-walk wording): banking it would record a hidden resistor in a run that conserved to `1e-14`.

**Priority RULED — STORY 2 is the target physics.** **STORY 2 (scattered-beyond-recall = the counting arrow)** is the important physics; STORY 3 (this run's transport-limited late echo) is a `κ=0.012` regime artifact, not the arrow. The counting-arrow **QUESTION REMAINS OPEN** and is reached in the review-probe regime (`κ=0.03–0.06`; result §6 follow-on 3 — the necessary counting shape appears, **necessary-not-sufficient**). The **κ-sweep path PROCEEDS**, but the κ-sweep drive is **GATED** on meter **W-battery revalidation at the new `κ`** (conservation drift `1e-14 → 6.8e-6 @0.03 → 4.3e-4 @0.06` is the #721 scope-caveat trigger). **The κ-reval prerequisite lane fires separately** (in flight).

| Item | Status / ruling | Consequence |
|---|---|---|
| **Phase-1 bin** | **FOREIGN-EATER** (RULED — faithful frozen §4 condition: return NOT tracking `x`) | Resolves the routed adjudication. Shipped `FRICTION-RENAMED` = semantic misfire, un-retuned (Rule 11). |
| **FRICTION-RENAMED** | **REJECTED** — Grant: *"friction does seem wrong"*; ratified-walk wording: *"…a hidden resistor in a run that conserved to `1e-14`"* | No dissipation (cons `9.4e-14`; energy returns). NOT the Ax3-illegal friction class. |
| **STORY 3 (this run)** | ratified-walk wording: *"echo **late, not eaten** … transport-limited … the counting question was never asked"* | `κ=0.012` regime artifact (`τ_transfer ≈ 5·T_rec`), NOT a falsification of the counting arrow. |
| **STORY 2 (the target)** | **scattered-beyond-recall = the counting arrow** — the important physics | Counting-arrow QUESTION **OPEN**; κ-sweep path **PROCEEDS**. |
| **κ-sweep drive** | **GATED** on meter W-battery revalidation at the new `κ` (κ-reval prerequisite lane, in flight, fires separately) | Necessary counting shape appears at `κ=0.03–0.06` (necessary-not-sufficient); reval clears the conservation drift first. |

**Propagation.** Ratings-map **R7** status + next-drive receipt updated this batch (`_orchestration/2026-07-15_hardware-ratings-map.md`); the counting-arrow-negative **closure manual entry remains owed to the auditor lane** (implementer surfaces; auditor lands).

---

## Continuation — 2026-07-19: electron/proton shape-walk adjudicated — dead branches recorded, $r_p$ flag raised, opens tracked

**Append-only, dated block.** Records the 2026-07-18 electron/proton shape-walk (in-chat Grant + orchestrator walk, workflow `wf_e86a1fd8-a2e`) and its canon-adjudication. Walk-record: `research/2026-07-18_electron-proton-shape-walk_adjudicated.md`. **NOTHING new was canonized** — the walk was adjudicated *against* existing canon by a 3-lens corpus pull; all file:line receipts re-verified at HEAD.

**Adjudication outcome (the durable record):**
- **OWNED** (walk reconciles to canon): body asymmetry ($0_1$ vs $6^3_2$, phase-space-vs-real-space); "no two loops linked" load-bearing ($S_3\to SU(3)$ confinement); charge universality = the M/Q/J no-hair rule; neutron = $6^3_2\cup 0_1$ threaded composite.
- **CONTRADICTED — dead branches, stated so they stay dead:** (1) "proton mass = linkage/rigging strain" — canon = the self-consistent mass oscillator eigenvalue (1-residual; trapped $+1$ twist at $1.0\,m_e$ amplified by feedback); (2) "multi-cell spatial junction web / Y-junction" — canon = SUB-NODE proton ($\approx\ell_{node}/460$) with skew-line tubes offset $1.0\,\ell_{node}$ + orthogonal-crossing Transverse Polarization Strain, zero Y-junction content; (3) "fractions = shares" — canon = Witten-effect $\mathbb{Z}_3$ $\theta$-vacuum dressing + the two-ontology reconciliation.
- **NOT-IN-CANON** (demoted to candidate-framing): the form-factor flat-vs-structured correspondence; the $g_p\approx 5.586$-as-distributed-winding story (canon delegates the moment).

**Two tracked opens (surfaced, not fired):**
- **(a) $N=3$ minimality theorem = the named chord-decider** — already canonically tracked (`topological-fractionalization.md:59`, "NO 3-loop stability theorem"; strengthen-by at `vol2/claim-quality.md:324`). Cite, don't duplicate.
- **(b) ★ $r_p$ two-routes tension — FLAGGED, KEEP-BOTH, routed to the baryon lane.** Route A ($D_p=4\lambda_p$ Compton/Ax4, `proton-identification.md:46`, axiom-derived, matches muonic-H) vs Route B (linkage-strain-gradient RMS, `02_baryon_sector.tex:41`, asserted) — mechanisms not obviously compatible (sub-node vs multi-node framing under a shared $0.84$ fm target). Flag landed as a dated bottom-append on `proton-identification.md`; neither route edited.

**Also surfaced (auditor items, not landed here):** (c) mass=A1 sector-ownership never applied in the baryon chapter (propagation gap); (d) EDM=0 anchor (`research/2026-06-24_electron-vacuum-state-synthesis.md:46,:84`) canonization candidate, low priority.

**Plan-impact.** The sub-node scale fact ($D_p\approx\ell_{node}/460$) means current node-scale-DOF engines **cannot resolve baryon interior structure** — a future baryon-sector engine test needs a sub-node/internal-DOF instrument class (does not yet exist). **No change to the current F6 / counting-arrow priority.** The walk **reinforces R13 mechanism (a)** — the topological latch re-confirmed at the baryon scale via linking-invariance ("no two linked").

**Propagation.** The $r_p$-reconciliation and the mass=A1 propagation-gap items are **owed to the baryon / auditor lanes** (implementer surfaces; auditor lands).
