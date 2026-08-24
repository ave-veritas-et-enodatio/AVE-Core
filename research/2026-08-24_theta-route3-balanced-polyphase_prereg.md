# PREREG — θ route 3: the balanced-N-phase reading of the 𝒥-dressing

> **Class:** research-tier pre-registration. **No canon edit.** Nothing is minted; no `clm-`/`def-`/
> `exp-`/`sup-`/`ilk-` node is authored; no solidity moves. This document freezes the question, the
> criteria under test, the outcome bins and the adjudication rules BEFORE the first-order pass,
> per `ave-prereg`.
>
> **Frozen:** 2026-08-24, before the driver ran and before any dimension count / arithmetic
> enumeration was computed. The companion result doc is
> [`2026-08-24_theta-route3-balanced-polyphase_result.md`](2026-08-24_theta-route3-balanced-polyphase_result.md).
>
> 🔴 **Dated surface-note 2026-08-24 (checker-audit Finding 6a) — THE FREEZE CLAIM DIRECTLY ABOVE
> IS WITHDRAWN TO "STATED, UNVERIFIABLE."** This prereg, the result doc, the driver and its JSON
> output all landed in **ONE commit, `bdf51221`**. Per the ratified P9 rule
> (`_orchestration/2026-07-09_breakthrough-patterns-methods-note.md` §P9: *"a freeze you cannot
> point to in the git log is a promise, not a freeze"*), a single-commit landing makes the
> ordering unverifiable: neither "before the driver ran" nor §1's five not-known-at-freeze claims
> can be shown from git. **Contrast route 1, which had genuine ordering** — its prereg commit
> `b50c0d86` (2026-08-23 20:56) precedes its result commit `4f963e29` (2026-08-23 21:07), so
> route 1's freeze is checkable and route 3's is not. The independent checker-audit re-derived
> every number in the result bit-exactly, so no *result* is impeached; what is withdrawn is the
> *freeze claim*, and with it the evidentiary weight of §1's honesty declaration and of any
> "pre-registered, therefore not post-hoc" defence of §5's bins.
>
> **Compounding disclosure (checker-audit Finding 6b), recorded because it is exactly what an
> unverifiable freeze cannot rule out:** bin **B3** in §5 was **added by this lane beyond the
> dispatch's three named bins** (the §5 B3 cell says so itself, under the KEEP-BOTH discriminator
> pattern) — **and B3 is the bin this lane's own positive finding landed in** (result §5, the
> N=3 rigidity result). A lane adding a bin and then landing its own positive in that added bin is
> the shape that pre-registration exists to exclude; with the freeze unverifiable, the ordering
> that would clear it cannot be shown. The B3 finding is already marked **not banked** in the
> result, and this note is the reason that marking must stay. No claim is made here that the bin
> was added post-hoc — only that the record cannot establish that it was not.
>
> **Program context:** open item `theta-dressing-open-questions`, route 3, on branch
> `kb/2026-08-23-theta-carve` (**not on `main`** at this branch's base — every quotation from it
> below is taken via `git show origin/kb/2026-08-23-theta-carve:<path>` and marked accordingly).
> Route 1 returned B4 (question ill-posed) at PR #999 and its re-banked minimum-N statement was
> subsequently REFUTED-AS-BANKED; route 2 was CLOSED-BY-CORPUS (answer NO). Route 3 is the
> third and, per the docket, the one that would "collapse *why thirds* + *what the dressing is*."

---

## §0 — SECTOR DECLARATION (mandatory header, stated before any standard-physics word)

| Axis | Declaration |
|---|---|
| **MODE** | **T2 / Cosserat charge-and-spin sector**, on the *boundary-observable algebra*, not the bulk. The object under test is the pair (𝒬, 𝒥) at a Γ=−1 saturation surface — 𝒬 = Link(∂Ω, **F**) the fundamental integer, 𝒥 = Wind(∂Ω) the dressing carrier. This is **NOT** an A1 dilatation/mass question (sector-ownership: MASS = A1 ⊥ CHARGE/spin = T2, `def-portmp`; the route-1 adversarial pass died partly on crossing exactly this fence). It is **NOT** a K4-TLM scatter/connect dynamics question and **NOT** an eigenproblem. |
| **REGIME** | **Split, declared as scope caveat.** The dressing's host — the proton's Borromean core — is canonically **Regime IV / Ax4-saturated** (`proton-identification.md` §1 property 4: *"the cinquefoil core operates in the saturated regime ($S \to 0$, $G_{shear} = 0$)"*). The phasor mathematics this lane performs is **regime-free** (it is configuration counting on a phase manifold), so no cold-vs-saturated claim is made or needed. Any step that would require an *energy* is therefore out of this lane's reach and is flagged where it arises rather than supplied. |
| **PHASE-STATE** | Not applicable to the phasor argument; the host is saturated-core (named-open per R45, not silently assumed crystalline). |
| **CHANNEL** | **PHASE-SPACE**, and specifically the **common-phase / fibre coordinate** — per the open item's banked route-3/4 input: *"the thirds live in the coordinate the chart deletes — the common-phase U(1)"*. **The spatial bond star is OUT OF CHANNEL for this lane** (see §0.1). |

### §0.1 — The channel fence that route 1's corpse installs (load-bearing, stated before anything else)

The route-1 adversarial verdict (docket `2026-08-23-route1-minimum-flip-ruling`, 🔴 block, lens 2,
verbatim) names as FATAL: *"the internal-phase-vs-spatial-star tie is route 3's unproven content,
imported silently."*

**This prereg therefore forbids, in advance, any step that ties the polyphase angles θ_i to the
z=3 node's three spatial bond directions.** A balanced polyphase set in power engineering is
*two* things at once — N temporal phases AND N spatially displaced windings — and it is precisely
the spatial half that route 1's corpse forbids importing. Any argument this lane makes must
survive with the phases living **only** on the fibre / common-phase coordinate, with no spatial
referent. Where the spatial half would be needed, the lane reports that need as a *finding*, not
as a supplied premise.

Corollary the same fence installs: the corpus's existing three-phase WYE reading of the srs node
(`first-principles-bond-force-constants.md`:110, *"each interior node … is a 3-connected WYE
junction — a three-phase node"*) is a **spatial-star** reading and may be cited as context but
**never as support** for this lane's phases.

---

## §1 — WHAT WAS ALREADY KNOWN AT FREEZE TIME (honesty declaration)

Prereg value depends on what the author did not yet know. Stated explicitly:

**Known at freeze (from the corpus-reading phase, which precedes the freeze):**
- The four canonical texts quoted in §3, read in full.
- The taxonomy of three candidate criteria in §4 (C-SUM / C-ORTH / C-CLOSURE) — these were
  *formulated* during corpus reading; that is design work, not result.
- That canon carries N-phase EE archetypes at N = 3,4,5,6,7 (`vol6/claim-quality.md`:625) and that
  `clm-sd04x4` is solidity 0.30 / build-status *"do not build on, rework needed"*.

**NOT known at freeze (computed only in the result doc):**
- Any dimension count of the equal-modulus zero-sum configuration variety at any N.
- The Jacobian-rank behaviour at N=2 vs N≥3.
- The compact-θ charge enumeration (which (n, θ) pairs reproduce ±1/3, ±2/3).
- The maximum N admitting pairwise time-averaged mode orthogonality.
- Whether any criterion in §4 turns out to be N-selective.

The bins in §5 are written to be decidable *either way* on each of these, and §5.4 lists the
criteria that may not be dropped post-hoc.

---

## §2 — SUBSTRATE-NATIVE WALK (`substrate-native-check`, trigger: prose-derivation construction)

Fired before any argument or code. Ten checkpoints.

| CP | Checkpoint | Walk result for this lane |
|---|---|---|
| 1 | Substrate dynamics for this problem? | **None — and that is the finding-shaped part.** The question is *configuration counting on a phase manifold*: given N phasors on a circle and a stated constraint, what is the solution set? No stepper, no stencil, no kernel. **The SM/continuum default this closes:** "the balanced set is the energy minimum." That answer is BARRED (see CP3) — the corpus carries **no θ-dynamics at all** (`2026-06-23_witten-angular-momentum-charge_result.md`:253-254, *"no body-angular-momentum coupling in any engine"*), so an energy answer would be imported, not derived. |
| 2 | Which sector? | T2 / Cosserat (charge + spin). Explicitly NOT A1. See §0. |
| 3 | AVE-native objective? | A **realisability + rigidity count** on the constraint variety. NOT an energy minimum, NOT an $S_{11}$ null, NOT a Hessian spectrum. Fixed in advance so the answer form cannot drift into energetics. |
| 4 | Phase-space vs real-space | **Phase-space, fibre coordinate.** Locked by §0/§0.1. This is the A46 checkpoint and it is the whole point of the route: the claim is a phase claim, so the test is in phase coordinates. |
| 5 | Saturation-modulated local clock | **N/A** (no eigensolve, no drive). The host's saturated regime is carried as the §0 scope caveat. |
| 6 | Reactance pair (C-state AND L-state) | **N/A** — no time-domain run. Flagged because a *future* dynamical version of this question (does the substrate phase-lock N constituents?) would require the pair; that requirement is recorded in the result doc's follow-on list, not discharged here. |
| 7 | Sampling discipline (PML exclusion / density-peak vs centroid) | **N/A** — no lattice field is extracted, no `argpartition`, no PML exists in this lane. |
| 8 | Generative precursor vs planted end-state | **Named, and it bounds the verdict.** This lane reasons about a *planted* N-constituent composite and asks what phase relation it may carry. It does not grow one. Therefore a positive ("N=3 forced") reading can **never** be banked from this lane alone — it would have to route to a hosting test. Written into bin B1's conditions. |
| 9 | Heuristic-vs-dynamical observable | The quantities computed are **analytic/combinatorial** (constraint-variety dimensions, Jacobian ranks, exact rational arithmetic). No engine observable is evolved. ⇒ **WALL-engine** for the dynamical form of the question; recorded as a capability finding, not a physics floor. |
| 10 | Boundary condition, not bulk force | Relevant and honoured: the dressing lives on ∂Ω (a boundary integral), not in a bulk term. No bulk energy/force term is introduced anywhere in this lane. |

**Exit:** ten checkpoints answered; CP1/CP3 bar the energetic answer, CP8 bars banking a positive,
CP9 records the engine wall. All three are written into §5.

---

## §3 — THE FOUR CANONICAL TEXTS THE ROUTE MUST SURVIVE (verbatim, `verify-before-cite` run)

Quoted here so that "contradicts a canon receipt" (bin B5) is decidable against frozen text rather
than against recollection. Paths on `origin/main` unless marked.

**T1 — the ratified 𝒥-dressing identification** (`manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/topological-fractionalization.md`:55):

> *"**Ontology A is the EFFECTIVE appearance.** The fractions $\pm 1/3, \pm 2/3$ are a *dressing*
> of the integer, carried by the soliton's body angular momentum $\mathcal{J} =
> \mathrm{Wind}(\partial\Omega)$ — a *separate* 2D surface boundary integral. The dressed effective
> charge is $q_{eff} = \mathcal{Q} + \theta/2\pi$ with $\mathcal{Q}$ the fundamental integer and
> $\theta/2\pi$ the effective $\mathcal{J}$-dressing."*

**T2 — the per-constituent share is 1/N by symmetry, for every N**
(`research/2026-06-23_witten-angular-momentum-charge_result.md`, PART C1):

> *"Grant's chord claim: the baryon's 3-fold body angular-momentum structure (3 constituents)
> FORCES `θ/(2π) = 𝒥_constituent / 𝒥_total = 1/3`. The arithmetic IS clean: for an `N`-fold-symmetric
> soliton, the per-constituent share of a symmetric body rotation is EXACTLY `1/N` by symmetry."*

and the same doc's table: *"The denominator equals `N` for every `N`; the substrate EXCLUDES none."*

**T3 — the θ set and the n_twist=0 convention** (`topological-fractionalization.md`, Examplebox):

> *"restricting the topological phase angles of the trapped vacuum to mathematical thirds
> ($\theta = \pm 2\pi/3, \pm 4\pi/3$) … Assuming an uncharged base node ($n_{twist} = 0$),
> substitute the allowed permutation angles."*

and the leaf's headline set: *"$\theta\in\{0,\pm2\pi/3,\pm4\pi/3\}$"*.

**T4 — the closure statement, already adjudicated as content-free**
(`neutron-identification.md`, dated note 2026-08-23; **branch `kb/2026-08-23-theta-carve` only**):

> *"the net Σθ ≡ 0 (mod 2π) across the nucleon's constituents is arithmetically EQUIVALENT to
> integer total charge — it is a restatement of charge integrality, not an independent
> EDM-cancellation argument."*

**T5 — the definitional gap that bounds every formalization below**
(`boundary-observables-m-q-j.md`:21 is the sole KB definitional site; the engine's
`src/ave/core/boundary_invariants.py`:220-231 carries only a proxy):

> table cell: *"$\mathcal{J}$ | Boundary winding number | $\mathrm{Wind}(\partial\Omega)$,
> half-integer per $SU(2)$ double-cover | **2D surface** | magnetic moment | rotation | spin $J$"*
>
> engine: *"Compute 𝓙 — boundary winding number (FIRST-PASS proxy implementation). … RIGOROUS
> implementation (deferred) requires: Hopf invariant computation on the full Cosserat rotational
> field ω; SU(2) → SO(3) double-cover factor giving half-integer quantization"*

**Frozen instruction on T5:** this lane **may not mint** the missing Wind(∂Ω) definition. Every
formalization it writes must name *which object carries the phase* and, where the missing
definition would be required, must state **what the definition leaf would need to supply** —
as an owed-prerequisite finding, never as a supplied one.

---

## §4 — THE THREE CANDIDATE CRITERIA (frozen; the pass tests exactly these, no substitutions)

The frozen route asks whether the balanced set is *forced by a stated criterion*. Three criteria
are on the table; each is stated as a mathematical condition on N phasors
$a_i = A_i e^{i\theta_i}$ living on the fibre coordinate (§0.1: no spatial referent).

| Tag | Criterion | Stated as | Provenance |
|---|---|---|---|
| **C-SUM** | **Net-null / Kirchhoff.** The composite carries no net excitation of the fibre coordinate. | $\sum_i a_i = 0$ with $|A_i| = A$ equal (equal moduli from constituent identity) | The polyphase reading's own natural condition (a balanced source has no neutral current). **NOT** corpus-derived — its route-1 *spatial* analogue was killed FATALLY; the fibre version has no corpus site. Tagged IMPORTED-PREMISE at freeze. |
| **C-ORTH** | **Pairwise mode orthogonality.** Two constituents coexist iff their modes do not interfere. | $\langle u_i, u_j\rangle = 0$ for all $i \neq j$, on co-located modes differing only by fibre phase ⇒ time-averaged cross-energy $\propto \cos(\theta_i - \theta_j) = 0$ | Grant 2026-08-24, banked as the open item's third Q3 reading, verbatim: *"threading = MODE ORTHOGONALITY … no constructive interference = no energy exchange = stable coexistence"*. |
| **C-CLOSURE** | **Winding closure.** The constituents' phases close on an integer number of turns. | $\sum_i \theta_i \equiv 0 \pmod{2\pi}$ | Canon-carried (T4) and already adjudicated there as *"a restatement of charge integrality"*. |

**Frozen adjudication of each criterion, on two axes:**
1. **Does it force the balanced set at fixed N?** (a rigidity question)
2. **Does it select N — i.e. is it satisfiable/rigid at some N and not others — without N being
   fed in?** (the chord question)

A criterion passes axis 2 **only** if the N-dependence comes out of the mathematics, not out of
being told the answer. Per the standing weld hazard (docket, verbatim): *"'N=3 because z=3' counts
only as a derived embedding obstruction, never as the numeral rhyme"* — and its route-3 analogue:
**"N=3 because three-phase" is the numeral rhyme unless the mathematics excludes N=4.**

---

## §5 — OUTCOME BINS (frozen; exactly one is primary)

| Bin | Fires when | Consequence |
|---|---|---|
| **B1 — POLYPHASE-FORCES-N (emergence-class)** | A criterion from §4 is (i) derived from canon or an axiom, (ii) forces the balanced set at fixed N, (iii) singles out N=3 against N=2 and N≥4, AND (iv) the realization $\theta_i/2\pi = \mathcal{J}_i/\mathcal{J}_{total}$ holds under it. | The thirds stop being imported. **Cannot be banked from this lane alone** (CP8 planted-end-state) — a B1 reading routes to a hosting test. |
| **B2 — CRITERION-N-GENERIC** | A criterion realizes the balanced set but is satisfiable at every N ≥ 2 (or does not even force the balanced set at fixed N). | **The thirds stay honestly imported.** This is route 1's lesson repeating and is the *expected* bin. |
| **B3 — CRITERION-N-SELECTIVE-BUT-PREMISE-UNDERIVED** | A criterion IS N-selective by the mathematics (it distinguishes N=3 from N=2 and N≥4 without being told), but ≥1 of its substrate premises is underived with current corpus/engine primitives. | **Not a chord and not a nothing.** The result must name each underived premise and what would discharge it. *(Bin added by this lane beyond the dispatch's named three, per the KEEP-BOTH discriminator pattern: the dispatch's "works-for-any-N" and "underivable-as-posed" do not cover the case where the mathematics selects but the physics premise is missing. Adding a bin ≠ dropping a criterion; B1's bar is unchanged.)* |
| **B4 — CRITERION-UNDERIVABLE-AS-POSED** | No criterion in §4 can even be *stated* against corpus primitives — e.g. because the object carrying the phase has no definition and the criterion cannot be written without minting one. | STOP-AND-ASK with the missing definition named (T5 discipline). |
| **B5 — KILL: CONTRADICTS A CANON RECEIPT** | The polyphase reading contradicts a quoted canonical statement (T1–T4) or fails on canon's own arithmetic. | Route 3 closes NEGATIVE. Per Rule 12 the slot is **not refilled**: any successor hypothesis gets its own number and its own freeze. |
| **B6 — QUESTION-ILL-POSED-AS-FROZEN** | The frozen question's own premise is internally inconsistent (e.g. it asks to realize an identity that its own canonical inputs forbid). | STOP-AND-ASK with the specific defect named; **do not repair the question unilaterally** — a repaired question is a new question and needs its own freeze. (Route 1's actual outcome; recorded here so the same shape is decidable in advance.) |

### §5.1 — Multi-bin precedence (frozen)

If several conditions are met, the **primary verdict** is the earliest of
**B6 → B5 → B4 → B3 → B2 → B1**. Rationale, frozen so it cannot be reordered post-hoc: a defect in
the question dominates a contradiction with canon; a contradiction with canon dominates a missing
criterion; a missing criterion dominates a partial (premise-gapped) selection; and any of those
dominates a generic criterion, which in turn dominates a positive that CP8 forbids banking.
All non-primary fired bins are reported as **secondary findings, explicitly not banked**.

### §5.2 — Symmetric-standard check (frozen, mandatory in the result)

Before any negative is headlined, the result doc must state what the Standard Model does with the
same object: SM does **not** derive $N_c = 3$ either (it is measured — R-ratio, $\pi^0\to\gamma\gamma$),
and SM's quark hypercharges are assigned, not derived. A B2/B3/B5 verdict is therefore an
**object-level verdict on this specific mechanism**, not a comedown relative to SM. Omitting this
check is a frozen adjudication failure, not a stylistic one.

### §5.3 — Consistency-vs-emergence pre-classification (`consistency-vs-emergence` fired at design time)

- **B1** would be **Class D (emergence)** *about the value 3* — the highest bar, which is why
  §5.4's criteria are non-negotiable.
- **The realization step alone** ($\theta_i/2\pi$ re-labelled as polyphase indices $i/N$) is
  **Class A (identity)** — a relabelling of the same arithmetic — and must be reported as such,
  never as evidence.
- **B2/B3/B5** are **NEGATIVE / PROCESS** verdicts and mint nothing.
- **No CODATA and no `ave.core.constants` value enters any verdict path.** The driver computes
  exact rational and integer arithmetic plus linear-algebra ranks; the only numbers that appear
  are configuration counts, ranks, and the small rationals $\{0, \pm 1/3, \pm 2/3\}$ that are
  the *target* of the enumeration, entered as targets and never as inputs to a fit.

### §5.4 — Adjudication criteria that may NOT be dropped post-hoc

1. **The spatial-star fence (§0.1) is absolute.** Any argument requiring N spatially displaced
   windings fails, regardless of how well the phase mathematics works.
2. **"The balanced set is the energy minimum" never satisfies any bin** (CP1/CP3): the corpus has
   no θ-dynamics, so that answer is imported.
3. **A criterion satisfied at N=2 and N≥4 does not select 3**, even if 3 is "nicest".
4. **Rigidity of a constraint variety is not stability.** Converting a dimension count into a
   stability statement requires an energy functional; if the lane wants that step it must name the
   functional or mark the step OWED. This is the specific way B3 could be inflated to B1 and is
   barred in advance.
5. **The θ compactness question must be settled explicitly, not assumed.** The polyphase reading
   requires θ to be a genuine phase (mod 2π). If canon's θ list is used non-compactly, the lane
   must say so and report the consequence rather than silently choosing a convention.
6. Every corpus tension found is **flagged with both sides quoted** (flag-don't-fix); no leaf is
   edited, demoted, or repaired by this lane.

---

## §6 — METHOD

1. **Corpus pass** (done pre-freeze; `verify-before-cite` on every quote in §3).
2. **Analytic pass** on the three §4 criteria, on the fibre coordinate only.
3. **Driver** — [`drivers/theta_route3_balanced_polyphase.py`](drivers/theta_route3_balanced_polyphase.py):
   a numerical *check* of every analytic claim (constraint-variety dimension via Jacobian rank +
   random-sampling of solution families; collinearity test; exact-rational charge enumeration under
   compact and non-compact θ; the pairwise-orthogonality search). The driver **decides nothing**;
   it exists so that no analytic assertion in the result is un-checked (Rule 10: run it, even small).
4. **Bin, per §5 precedence. Report stuck-points.** 2-attempt cap.

**Pre-registered null-liveness check.** The decision observables here can return "no selection",
so the positive control is built in: the driver must reproduce two facts that are *known* to be
non-trivial and would immediately expose a bug — (a) at N=3 the equal-modulus zero-sum solution set
must be a single point modulo global rotation and relabelling (the equilateral-triangle rigidity),
and (b) at N=4 an explicit one-parameter family must be constructible with residual ≈ 0. If the
driver cannot reproduce a *known* rigidity at N=3 and a *known* freedom at N=4, its "no selection"
answers are not trustworthy and the lane HALTS.

---

## §7 — WHAT THIS PREREG DOES NOT DO

- It does not define Wind(∂Ω) (T5) and does not mint any node.
- It does not touch the CP-parity debt (route 4) or the ropelength/Q3 fork.
- It does not re-open route 1 or route 2; both are closed and their premises are barred (§0.1).
- It does not adjudicate the θ symbol collision (`strong-cp.md` vs `topological-fractionalization.md`)
  — that was executed separately on `kb/2026-08-23-theta-carve`.
- It does not edit, demote, or repair any canonical leaf.

---

## §8 — PLUMBER-PHYSICAL QUESTION SURFACED TO GRANT (`pre-test-physics-check`, Step 1-3)

Corpus-searched first (§3; `polyphase|three-phase|balanced` across `manuscript/`, `research/`,
`src/`) — the corpus carries N-phase *archetype names* but no statement of what physically holds
N constituent phases apart, so the question is genuinely open:

> **On the real bench, what holds the three loops at 120° from each other — is there a restoring
> torque between them (a phase-lock, like paralleled alternators pulling into step), or is 120°
> just where they sit because nothing is pushing them anywhere?**

Why it is load-bearing rather than curiosity: a *restoring* answer means the balanced set is an
energy minimum and the whole question moves into a dynamics this lane cannot run (CP1/CP3 bar it,
and canon has no θ-dynamics). A *nothing-pushing* answer means the balanced set can only be
selected by a constraint — which is exactly what §4's C-SUM/C-ORTH/C-CLOSURE test, and the pass is
correctly posed. **The lane proceeds on the constraint reading and states that dependency
explicitly**, per the 2-attempt stop-and-ask cap; if Grant's answer is "restoring torque," §5's
verdict is scoped to the constraint reading only and the dynamics version is a new freeze.
