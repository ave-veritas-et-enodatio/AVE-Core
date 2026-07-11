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
