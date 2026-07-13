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

- **MISS-LEDGER candidates (Grant-gated increments; hopeful-interior-mechanism ledger).**
  - **X43 ringdown-port → 0-for-8** — the 6th convergence-shaped move of the register arc; paid to kill and failed (the port is real but forces `ω³`/no-law, not Sargent `ω⁵`) (`research/2026-07-11_x43-ringdown-port_result.md:87`).
  - **C13b cluster-halo source → candidate 0-for-9** — classification call is Grant's: **hopeful-interior-mechanism** (fits the 0-for-N ledger) **vs a separate class** (a source-fork MISS, not an interior-mechanism over-fit). Increment gated on the classification.

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
| **Miss-ledger** | X43 → 0-for-8; C13b → cand. 0-for-9 | **Grant-gated increments** (C13b classification his) | Grant |

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
| **X-LEDGER (X44 outcome)** | √S-weighted flux mass vs \(U_{\rm bind}\) ledger | **★PROPOSED-RULED X-LEDGER (text pending Grant confirmation — stamps become effective on his merge of #661)** — bank #652 bin (iii) UNRECONCILED; two substrate mass functionals named open; no silent √S retune; merge only as banked negative ([`2026-07-12_ave-native-rulings_g-persist_x-ledger.md`](2026-07-12_ave-native-rulings_g-persist_x-ledger.md)). *(Merge-resolution 2026-07-12: this X-LEDGER row is the SURVIVOR of the X44-firing event; the duplicate "X44 Komar-source" row that arrived via #652's merge was dropped per the pre-declared #652/#661 docket resolution — one event, one row.)* | Grant (PROPOSED-RULED) |
| **G-PERSIST (genesis D1–D4)** | Fixed-N lasting localization vs node birth | **★PROPOSED-RULED G-PERSIST (text pending Grant confirmation — stamps become effective on his merge of #661)** — bank #655 bin (ii) A-WEAKENED; remanence (R10-class) before node-mint; KEEP-BOTH; no `genesis_v{N}` ([same ruling leaf](2026-07-12_ave-native-rulings_g-persist_x-ledger.md)). **★FOUNDATION UNDER RE-ADJUDICATION** — consistent with main's merged #655 re-adjudication ([`2026-07-12_genesis-node-birth-fork.md`](2026-07-12_genesis-node-birth-fork.md)): the D2 battery-of-one was broadened to all 3 landed seed modes at BOTH fidelities ⇒ **per-fidelity SPLIT** — **SMOKE (n_quiet=12): 2/3 persist → bin (i) A-SUPPORTED** (`pair`/`graded_a0` pass; `photon_lock` φ-channel dead); **PRODUCTION (n_quiet=52): 0/3 → bin (ii) A-WEAKENED**. Both N=10 bins are **boundary-confounded** (PML leakage, interior only 4³ cells; E_persist recovers 0.69→0.80→0.84 as N 10→12→14 — ARTIFACT-LEANING). Ruling-grade banking **DEFERRED to Grant**; G-PERSIST confirmation MUST postdate the **#655 battery re-run (N≥14 / closed-box)** — if the fork re-adjudicates to (i) A-SUPPORTED, G-PERSIST as drafted is moot and the remanence-before-node-mint build-order directive loses its banked-fact basis (the R10 remanence question stays open on independent grounds — the anhysteretic-kernel zero-loop-area fact is corpus-standing regardless) | Grant (PROPOSED-RULED) |

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

**Convergence flags (this arc):** 10 (SYM/EP unification), 11 (one-door R-A/F6 — statics stable *because* release needs a topological event), 12 (cascade filter). Each carries a named kill-shape or investigation; none asserted as a win. Seduction ledger stands at **0-for-7** (`research/2026-07-10_collapse-target-registry.md:23,64,317`) — ⚠ the walk referenced "0-for-8"; discrepancy flagged for reconciliation (an 8th flagged negative may have landed post-2026-07-10, un-booked). **All rows above are PENDING-GRANT where his word is still owed; nothing is canonized.**