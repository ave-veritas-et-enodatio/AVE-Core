[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "PROCESS leaf, PILOT status — the Standard Vacuum Analysis ten-declaration engineering procedure (Grant GO 2026-08-04). Integrates the banked hard learnings into one prereg-header fire-point; every physics statement is a pointer to its canonical home; zero clm-/def- minted, no solidity moved, adjudicates nothing. Canonization gated on two pilot passes + Grant ratification (pilot 1 = the axial RHO-B lane return)."
path-stable: "routing home for the SVA prereg header enforced by ave-prereg >= v1.8 during the pilot"
-->

# Standard Vacuum Analysis (SVA) — the engineering process for substrate problems

**Status: PILOT (v0.1, 2026-08-04) — NOT canonical.** Grant GO 2026-08-04 (core session, following
the sign-relativity ruling). Pilot case 1 = the axial RHO-B lane return; canonize only after ≥2
pilot passes and Grant ratification. This leaf is PROCESS, not physics: it mints no `clm-`/`def-`,
adjudicates nothing, and every physics statement in it is a POINTER to its canonical home.

**Why this exists.** The EE toolkit applies to the vacuum-as-material almost wholesale — its bedrock
constants (ε₀, μ₀, Z₀, c) ARE vacuum constants — but with a systematic modification set, and every
element of that set was learned here the hard way as a separate failure. This leaf integrates them
into one front-to-back procedure. The parts already exist:
[`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md) (component
library), [`wall-taxonomy.md`](wall-taxonomy.md) (boundary-condition catalog),
[`operators.md`](operators.md) (identities), the certified cold-Q instruments (worked examples:
`research/2026-08-03_coldq-pole-v2.4-root_prereg-FROZEN.md` + `_result.md`). What was missing is
the integrated sequence and a structural fire-point.

**Fire-point.** Discipline that lives only in skills does not fire (2026-06 ensemble audit). The SVA
fires where execution already always passes: **every frozen pre-registration opens with the §0
header below** (enforced by `ave-prereg` ≥ v1.8 during the pilot). A prereg that cannot fill a row
is not ready to freeze.

---

## §0 — The SVA header (copy into every prereg, fill every row)

```markdown
## §0 — Standard Vacuum Analysis header (SVA v0.1-pilot)
 1. SECTOR / OWNERSHIP:      <which channel owns each observable; cross-wiring check done>
 2. REGIME / PHASE-STATE:    <MODE + REGIME + PHASE-STATE; small- vs large-signal; DC bias point>
 3. CIRCUIT STATEMENT:       <the observable in circuit terms BEFORE any framework word; total-vs-slot>
 4. PLANE & PROJECTION:      <reference plane + series/shunt projection for every Γ or Z claim>
 5. CONSTITUTIVE PROVENANCE: <each grading law: DERIVED | IMPORTED | FORKED(fork-id) | ENG-CHOICE>
 6. ENERGY LEDGER:           <rim (within-system reactive) vs port (boundary-crossing); no loss word without a port>
 7. CALIBRATABILITY:         <is the target a dimensionless ratio or a port phase difference?>
 8. DISCRIMINATION CLASS:    <pure-AC | DC→AC coupling | DC-internal; tautology filter run; SM counterfactual>
 9. CERTIFICATION PLAN:      <gates frozen before numbers; unrun ≠ passed; negative controls named>
10. ADJUDICATION ROUTING:    <which run settles which fork; what propagates on which outcome>
```

---

## §1 — The ten declarations

**1. Sector / ownership.** Name the channel that owns each observable (A1 dilatation / T2 electric /
Cosserat rotation-winding) before reasoning about it. Mass, charge, and spin have DIFFERENT owners;
"A confines B" claims across owners are the recurring defect. Failure closed: sector cross-wiring.
Home: [`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md).

**2. Regime / phase-state.** Declare MODE + REGIME + PHASE-STATE, which selects the toolkit:
small-signal analysis is exact only at cold amplitude; near yield the large-signal toolkit
(bias-point, load-pull class) governs. The DC bias point is the gravitational grading. A null
where the effect cannot exist is an ARTIFACT, not a falsification. Failure closed: wrong-regime
verdicts. Home: the PHASE-STATE sector headers of [`wall-taxonomy.md`](wall-taxonomy.md).

**3. Circuit statement first.** State the observable in circuit terms before using any framework
word — imported words import their framework's THEOREMS ("memory," "dissipated," "internal field"
each carried a wrong theorem in 2026-08 alone). Declare total-vs-slot: the bench measures total
observables, not series slots. Failure closed: vocabulary-cage misconstruals.
Home: [`vocabulary-register.md`](vocabulary-register.md).

**4. Plane & projection.** Every signed Γ or Z claim declares its reference plane (a quarter-wave
of graded skin inverts short↔open) and its projection (series-graded ⇒ Z→∞, shunt-graded ⇒ Z→0
at the same cutoff). The sign is computed from the branch-derived wall row, never chosen. In a
medium with no outside, the plane declaration is a theorem, not a convention. Failure closed: the
FLAG-W class of phantom contradictions. Home: [`wall-taxonomy.md`](wall-taxonomy.md) §10.

**5. Constitutive provenance.** Tag every grading law and constant as DERIVED (substrate-forced),
IMPORTED (GR/SM/engineering value), FORKED (open, with fork-id), or ENG-CHOICE. The corpus-wide
meta-finding is that AVE forces FORMS and imports VALUES (PRs #262–264); an untagged import is a
future walk-back. Failure closed: silent value-laundering (the V_BR 3.631-vs-3.594 class).

**6. Energy ledger.** Within-system reactive exchange is free however many channels it crosses; an
arrow exists iff energy crosses the system boundary into a continuum-counted port (far-field
radiation, matter detector, topology change). On the vacuum Smith chart, all passive medium states
live ON the rim (Axiom 3); the interior is reachable only through ports. No "loss," "dissipated,"
or "Joule" without naming the port. Failure closed: delivery-vs-dissipation conflations. Home:
[`transfer-cost-theorem.md`](transfer-cost-theorem.md) — **canonized 2026-08-04** (`clm-xfrcst`,
mechanical-rulings batch), which carries the three delivery modes, $R_{rad}$-as-delivery, and the
Op3 negative control. *(This row's wording is the ruled statement; the leaf quotes it, not the
reverse.)*

**7. Calibratability.** From inside the medium there is no external calibration standard: the only
self-calibratable observables are dimensionless ratios and phase differences at your own ports (the
α-echo resolution is the type case — the VALUE is a calibration identity). If the target is not a
ratio or a port phase, say what the readout normalizes against. Failure closed: α-circular and
unit-bridge pseudo-targets.

**8. Discrimination class.** Classify per the AC/DC carve (`clm-acdc07`): pure-AC (shared with the
competitor — dead on arrival as a discriminator), DC→AC coupling (the only live chord class), or
DC-internal (a bet needing a transducer). Run the tautology filter (does the discriminator reduce
to a known identity restated?) and the SM counterfactual BEFORE surfacing, including in chat.
Home: the `ave-discrimination-check` discipline (v1.9).

**9. Certification plan.** Gates and bins frozen before any number exists; the prereg lands as its
own pushed commit; UNRUN ≠ PASSED; negative controls named in advance (reproduce the certified
predecessor before the new configuration). Exemplar: the cold-Q v2.4 root instrument and the
polar-family lane (`research/2026-08-03_coldq-polar-family_prereg-FROZEN.md`).

**10. Adjudication routing.** The substrate adjudicates physics forks, not fiat: state in advance
which run settles which fork and what propagates on each outcome — including the fence on your own
result (what this instrument does NOT license). Exemplar: v2.4's self-fence (its result doc
propagates nothing without an adjudication ruling) and FORK-3(b)'s routed axial run.

---

## §2 — Provenance of the modification set (why these ten and not others)

The ten rows are the delta between bench EE and vacuum EE, each purchased by a logged failure:
sector cross-wiring (rows 1), wrong-regime artifacts read as physics (2), the 2026-08-03
vocabulary-cage exercise — memory/medium, internal-field — (3), the FLAG-W phantom contradiction
and its 2026-08-04 sign-relativity dissolution (4), the FORM/VALUE meta-finding (5), the GW-memory
latch-vs-flux and R_rad delivery lessons (6), the α-keystone echo resolution (7), the AC/DC carve
and the 0-for-7 hopeful-forms ledger (8), four solver generations of the cold-Q arc with every
defect caught pre-number by frozen gates (9), and the standing substrate-adjudicates-forks rule
(10). The bench constants did not change; the engineer's checklist did — because the DUT contains
the engineer.

## §3 — Pilot protocol

Apply the §0 header retroactively to the axial RHO-B lane's frozen prereg at its return (pilot
case 1): score each row FILLED / FILLABLE-BUT-MISSING / NOT-APPLICABLE, and log gaps here as dated
amendments. Second pilot on the next fresh dispatch. Canonization decision (Grant) only after both
pilots; until then this leaf binds only lanes the core orchestrator dispatches.
