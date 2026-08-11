# LC-1 frozen-cell RE-ADJUDICATION under the ratified set (R43, 2026-08-10)

### ENTRY 2026-08-10-lc1-readjudication-under-r43

**Class:** receipted re-adjudication record. Executes item **(f)** of the R43
execution batch ([`2026-08-10-ruling-r43-ratification.md`](2026-08-10-ruling-r43-ratification.md):45-49
— *"(f) the LC-1 re-adjudication record"*), fired by the same record's
what-fires-mechanically clause at `:30-35`: *"the four-tuple becomes
DERIVED-under-the-ratified-set → **LC-1's frozen cell re-adjudicates**"*.

**Mints nothing. Edits no LC-1 lane document.** The LC-1 result docs and the arc
brief are left byte-untouched; this record adjudicates *against* their frozen
text and is the artifact that carries the new disposition.

---

## §1 — THE FROZEN CELL, QUOTED VERBATIM (adjudicate against THIS, not a gloss)

The arc brief's own kill cell —
[`_orchestration/2026-08-04_lorentz-compliance-arc-brief.md`](../2026-08-04_lorentz-compliance-arc-brief.md):44,
the fifth column of the **LC-1** row, verbatim `[sic]`:

> **"An energy-carrying inter-event channel at ≠ c ⇒ arc-level kill"**

and the same file at `:59`, verbatim `[sic]`:

> **"LC-1 runs first and its kill condition is arc-terminating."**

The same row's *derivation-task* cell, `:44` column four, verbatim `[sic]` — a
**separate** cell that is NOT the kill condition and is adjudicated separately in
§4 below:

> **"(a) provenance of cold c_shear = c (is G_vac = ρc² derived or a matching condition?); (b) bulk √(10/3)c P-wave observability — gapped, confined, or sourceless?"**

**Anti-paraphrase interlock (this lane's own documented failure mode).** LC-1's
result doc records that its adjudicated kill condition — *"an energy-carrying
inter-event channel at speed $\neq c$ that a GW170817-class event **sources and a
detector reads**"* — *"came from the **orchestrator dispatch**, not from the
tracked arc brief"*, and that *"**There is no sources-and-reads clause**"* in the
brief ([`research/2026-08-06_lc1-one-speed_result.md`](../../research/2026-08-06_lc1-one-speed_result.md):495-504).
This record therefore adjudicates the **brief's** comparator-agnostic wording and
nothing else: the question is only whether an energy-carrying inter-event channel
at ≠ c **exists**. No detectability qualifier, no comparator scoping, no
"sources-and-reads" clause is imported. All three quoted cells above are
byte-verified at HEAD by the lane's committed two-engine quote gate
(`research/drivers/bound_constitutive_quotes_number_check.py`, rows 1–3), which
runs inside `make verify`. **Coverage correction (2026-08-10, review finding):** an earlier
cut of this record claimed all three cells were gated by "rows 1–2" — two rows
cannot byte-verify three cells, and the uncovered one was the DERIVATION-TASK
cell that §4 adjudicates tasks (a) and (b) against. That cell is now a third gate
row, and the gate's mutation receipt is per-row, so every expectation is proven
live rather than assumed.

## §1.5 — THE ARMING GATE, QUOTED AND DISCHARGED (do not skip: this record should not exist unless both halves are discharged)

The source lane put an explicit brake on this very record, and it sits on the SAME
LINE this record quotes its derived-partials fragment from —
[`research/2026-08-10_bound-constitutive_result.md`](../../research/2026-08-10_bound-constitutive_result.md):25,
verbatim `[sic]`:

> **"LC-1's cell re-adjudication is NOT ARMED:** it is gated on Grant's ratification of BC-SRC (and an orchestrator ruling on whether `DERIVED-VIA-NEW-AXIOM` counts as "DERIVED-class" under the brief's frozen sentence) — not arithmetic, per C2's confirmed repair."

The brake exists because the frozen trigger is grade-conditional —
[`_orchestration/2026-08-10_bound-sector-constitutive-brief.md`](../2026-08-10_bound-sector-constitutive-brief.md):37,
verbatim `[sic]`: *"LC-1's cell re-adjudicates only on (i)+(ii) both DERIVED-class."*
— while the lane in fact landed the SECOND of the brief's three grades for all four
items (`:23`: *"**THE FOUR-TUPLE (final): (i) `DERIVED-VIA-NEW-AXIOM(BC-SRC)`"*).

**Both halves are now discharged, and by whom is stated so Grant can see the call
being made:**

- **Gate (a) — ratification of the axiom: DISCHARGED BY GRANT.**
  [`2026-08-10-ruling-r44-r43-reconciliation.md`](2026-08-10-ruling-r44-r43-reconciliation.md),
  Grant verbatim: *"The first session I accidentally reset the chat to before it on
  R43, the one we scoped is final, so the dc operation point/quiescent point is
  ok."* R44's own ruling text, verbatim `[sic]`: *"The **full-scope record is
  FINAL**: `2026-08-10-ruling-r43-ratification.md` (via #941) — **Tier A + BC-SRC
  clauses S, G, AND Q all RATIFIED**, with the DC operating point / quiescent point
  (Q-point) naming."*
- **Gate (b) — whether `DERIVED-VIA-NEW-AXIOM` counts as DERIVED-class:
  DISCHARGED BY ORCHESTRATOR RULING, MADE IN R44 — not "standing".** R44's
  consequences clause, verbatim `[sic]`: *"Consequences now unambiguous: the axiom
  count is **5**; the doc-lane execution batch runs items (a)-(g) IN FULL (the Tier-A
  repair and the Q/def-node promotion are no longer held); **LC-1's cell
  re-adjudication FIRES** (all clauses ratified, per the standing orchestrator
  ruling)."* Read plainly: with the candidate ratified as an
  axiom, the `(candidate)` qualifier in the brief's second grade evaporates and the
  four-tuple is DERIVED-under-the-ratified-set.

**⚑ Disclosed defect in the citation chain, surfaced not smoothed.** R43 `:30`
attributes gate (b) to *"the standing orchestrator ruling (#939 record)"* — but the
#939 record is the very document whose `:25` and `:257` say the ruling has **not**
been made. That is a circular arming citation. It is upstream of this record (the
R43 file landed on main separately, not in this PR), it is **not repaired here**,
and R44's later `FIRES` is what this record actually stands on. Routed to the
orchestrator as a correction-PR candidate against R43 `:30`.

### §1.6 — BASIS OF THIS RE-ADJUDICATION, SCOPED (read before §3)

**This record rests on ONE theorem and says so: the $(u,\pi)$-sector ENERGY-TRANSPORT
theorem.** T1 (one finite characteristic speed $c$, zero longitudinal characteristic
speed) + T2 (constraint conserved step-by-step by local operations) + T3 (the
shrinking-cone/Grönwall energy estimate, with the longitudinal sector contributing
ZERO flux). That is what the receipts measure and that is the whole of the basis.

**What the basis explicitly does NOT include, stated up front rather than discovered
later:** it does **not** cover the **bias read**. The no-signalling theorem is proven
on the $(u,\pi)$ sector; the bias $\varepsilon_{11}$ is a **declared distinct
object**, and clause G's elliptic law is the *static abstraction of underived
finite-speed bias dynamics*. **THE BIAS PROPAGATION THEOREM is Axiom 5's standing
debt and is NOT discharged here.** The kill cell asks about an energy-carrying
inter-event channel, which is an energy-transport question and therefore inside this
basis — but a reader must not carry this record as authority for the bias sector's
propagation speed. It is not.

## §2 — WHAT FIRED THE KILL, AND WHAT ITS REFERENT WAS

Under the brief's operative wording the kill was adjudicated **FIRED**. The
standing record states it without softening
([`research/2026-08-06_lc1-one-speed_result.md`](../../research/2026-08-06_lc1-one-speed_result.md):526,
verbatim `[sic]`):

> **"Row 3b of §5 is one: it is energy-carrying, it is inter-event, and it runs at $\sqrt{10/3}\,c$. On its face, under the brief's wording, row 3b satisfies the kill"**

and the dated disposition note at
[`research/2026-08-07_lc1-one-speed_result.md`](../../research/2026-08-07_lc1-one-speed_result.md):4-7,
verbatim `[sic]`:

> **"The frozen kill condition subsequently FIRED via the screening lane's residue (PR #930, merged — `SEAL-DERIVED + RESIDUE-EXCEEDS`), and the constitutive PREMISE the chain consumed (a propagating bulk channel) is now under R38 adjudication (the bound-response lane)."**

**So the kill's referent is a single, named object: row 3b — the A1 bulk
RADIATIVE column, a freely propagating longitudinal P-wave at $\sqrt{10/3}\,c$.**
The whole kill stands or falls on whether that mode exists. The standing record
itself already flagged the premise as under adjudication; that adjudication is
the bound-constitutive lane, and it has now returned.

## §3 — THE ADJUDICATION: THE PREMISE HAS NO REFERENT AMONG THE DERIVED ROWS

**Verdict: the kill condition does NOT fire under the ratified set — because it has
no referent among the DERIVED rows, not because a bound was met.**

The ratified axiom set writes **no longitudinal restoring term**. The receipted
dynamics is curl-only, so on the longitudinal line the spatial operator is
identically zero ($\nabla\times\nabla\times(\nabla\varphi)\equiv0$): **zero
characteristic speed**, not a small one. There is no finite-$\omega$ longitudinal
eigenmode to carry a $1/r$ term at any drive frequency, so there is no radiative
pole, no radiated power, and nothing that is "energy-carrying" and "inter-event"
on that line at any speed. The $\sqrt{10/3}\,c$ branch is a theorem of the
**imported** elastic OPERATOR, not of the axioms —
[`research/2026-08-10_bound-constitutive_result.md`](../../research/2026-08-10_bound-constitutive_result.md)
§5.4 (`:213`), verbatim `[sic]`:

> **"there is no such mode and no such passband in the receipted dynamics — the `√(10/3)c` branch is a theorem of the imported W (the driver's control arm, where the instrument duly detects it at `1.8182c`), not of the axioms. The corpus owed a mechanism for a phantom's silence; the actual structure has nothing to silence."**

**⚑ THE GROUND IS STENCIL-ABSENCE, NOT MODULUS PROVENANCE — stated explicitly,
because LC-1 pre-closed the modulus route and this record must not appear to
reconstruct it.** LC-1 froze an anti-escape clause aimed at exactly this kind of
argument —
[`research/2026-08-06_lc1-one-speed_result.md`](../../research/2026-08-06_lc1-one-speed_result.md):661,
verbatim `[sic]`: *"**Q1's exclusion cannot be escaped through the $K=2G$ import.**
§2.2: $v_L > c$ for every $K \geq 0$. Any future re-derivation, dispute, or
replacement of $K$ leaves a superluminal branch."* — with the $K=0$ floor at
`:185`, verbatim `[sic]`: *"**$v_L > c$ for every $K \geq 0$.** The floor at $K=0$
is $\sqrt{4/3}\,c$"*. **That clause is scoped to the MODULUS (re-derive, dispute,
or replace $K$), and this record does not take that route.** The defeater is the
absent STENCIL, carried verbatim from the source lane —
[`…_bound-constitutive_result.md`](../../research/2026-08-10_bound-constitutive_result.md):139,
verbatim `[sic]`:

> **"The LC-1 K=0 trap is answered structurally, not by tuning:** the imported W's longitudinal floor `v_L ≥ √(4/3)c` at K=0 comes from its deviatoric-restoring stencil acting on longitudinal patterns; the receipted potential HAS no such term — its potential is curl-keyed only."

and `:35`, verbatim `[sic]`: *"and NOT by the K→0 route the LC-1 receipt closes: the
receipted potential lacks the deviatoric-restoring stencil entirely, which is why
there is no `√(4/3)c` floor"*. So the $4G/3$ term that produces the floor is not
present to be tuned to zero: LC-1's clause forbids escaping through $K$'s VALUE,
and this record escapes through the OPERATOR the axioms wrote instead. Reconciled
in the open rather than left for a third document.

**Receipts (all machine-checked; the lane's number gate `BOUND-CONSTITUTIVE
NUMBER CHECK: PASS — 27 checks green` runs inside `make verify` and byte-checks
these numerals against the shipped driver JSON):**

| # | Receipt | Value | What it establishes |
|---|---|---|---|
| R1 | longitudinal dispersion on the receipted operator | $\omega^2 \equiv 0$ | no longitudinal eigenmode at any $\omega$ |
| R3 | curl-free pulse, receipted operator, full run | $\max\|\Delta u\| = $ `1.6e-19` | the longitudinal sector transports **nothing** (machine zero); no detector triggers |
| R3 | transverse front | `0.9959c` | the one finite characteristic speed is $c$ |
| R3 | **K-loaded CONTROL** longitudinal front | `1.8182c` vs frozen $\sqrt{10/3}c=$ `1.8257` | the instrument **provably sees the phantom where it exists** — 0.41% low = one detector-timestep of half-max latching (241 vs 240 steps), inside the frozen 3% gate |
| R5 | driven receipted radial sector | machine zero, while the control radiates | same liveness pair under a *driven* source |
| R7 | retarded-fields control | front `1.004c`; energy outside the c-cone $\le$ `1.1e-14` | domain-of-dependence holds on the receipted flow |
| R8 | two-$\omega$ near-zone | tracks the instantaneous elliptic solve to `3.0%`, quadratic-class $\omega$-scaling | the near-zone response is reactive tracking, not propagation |
| T3 | energy flux vector | $\mathbf{S} = -\rho c^2\,\dot{\mathbf u}\times(\nabla\times\mathbf u)$, $\|\mathbf S\|\le c\,e$ | purely longitudinal content contributes **ZERO** flux — its energy does not move at all |

**The liveness pair is the load-bearing anti-artifact control.** A null from an
instrument that cannot see the effect is worthless. Here the *same* instrument,
in the *same* run configuration, detects the $\sqrt{10/3}\,c$ P-wave at `1.8182c`
in the K-loaded control arm and machine-zero in the receipted arm. The absence is
a measurement, not a silence.

**The no-signalling theorem** ([`…_bound-constitutive_result.md`](../../research/2026-08-10_bound-constitutive_result.md)
§3, item (ii)) supplies the positive statement the kill cell's negation needs:
T1 locality + one finite characteristic speed $c$ + **zero** longitudinal
characteristic speed; T2 the constraint is conserved step-by-step by local
operations only (`∂_t(∇·π) = −∇·j_m`), with (`:143`) *"No global re-solve happens anywhere
in the dynamics — the elliptic language of the STATICS is a solution method, not a
propagation mechanism"*; T3 the shrinking-cone/Grönwall estimate ⇒ **no energy,
hence no information, crosses any surface faster than $c$, at any frequency**.
The **constraint structure** is what makes this a theorem rather than a
coincidence: BC-LAW is **initial-data class** (temporal-gauge/Gauss class), NOT
multiplier/holonomic class. That distinction is load-bearing and was derived, not
chosen — a holonomic multiplier constraint is the *incompressible-medium*
structure, i.e. the textbook infinite-signal-speed idealization, and had item (i)
landed there, item (ii) would be FALSE.

**BC-SRC does not reintroduce a channel.** The ratified axiom's own consequence
audit forbids it — §2.6 item 5 (`:130`), verbatim `[sic]`: *"any new longitudinal stiffness
or wave (BC-SRC adds no kinetic/potential term on the flat direction — the
pole-absence results survive it untouched)"*. Landed at
[`eq_axiom_5.tex`](../../manuscript/common_equations/eq_axiom_5.tex)
("What BC-SRC forbids").

### §3.2 — THE OTHER CHANNELS IN LC-1'S OWN TABLE, NAMED AND DISPOSED (no bare universal)

The §3 argument above — *"on the longitudinal line the spatial operator is
identically zero"* — reaches rows **3a/3b** and nothing else. LC-1's frozen channel
table has two further rows that run at $\neq c$, and an unqualified "no referent"
would silently sweep them in. They are named and disposed here instead:

- **Row 4 — the Cosserat micro-rotation / wryness carrier** (`clm-2bkp7v`;
  [`…_lc1-one-speed_result.md`](../../research/2026-08-06_lc1-one-speed_result.md):339,
  *"both $\neq c$"*). **EXCLUDED, on its own lane's terms, by citation not
  re-derivation.** Its source lane forbids exactly this use —
  [`research/2026-08-05_two-band-kinematics_result.md`](../../research/2026-08-05_two-band-kinematics_result.md):304-306,
  verbatim `[sic]`: *"**This lane does NOT license:** … and any firing of LC-1's
  arc-level kill."* — and the merged docket record restates it comparator-agnostically,
  [`2026-08-05-two-band-kinematics.md`](2026-08-05-two-band-kinematics.md):28,
  verbatim `[sic]`: *"**LC-1's arc-level kill is NOT fired** (that needs an"* energy-carrying
  inter-event channel at $\neq c$; this lane does not establish one). Substantively:
  its $\neq c$ is the **low-energy effective theory's invariant speed, not a
  transport speed** — same record `:22`, verbatim `[sic]`: *"**★MATERIAL QUALIFIER
  — do NOT read this as superluminal transport.**"* An invariant speed in an
  effective theory whose validity window closes before its relativistic regime
  opens is not an energy-carrying inter-event channel.
- **Row 5 — matter messengers (neutrinos, cosmic rays).** **NOT disposed, and NOT
  claimed as de-fired.** LC-1 leaves its speed **UNDERIVED** (`:340`) and refused
  to fold it into a verdict — `:352`, verbatim `[sic]`: *"**One row the corpus
  cannot fill.** It is left open and visible rather than assumed compliant."* That
  refusal is **carried forward here unchanged**. A kill fires only on a positive
  referent and an UNDERIVED row establishes none, so row 5 does not resurrect the
  kill — but neither does this record get to call it absent. It is a **named-open**.

**Therefore: the premise "an energy-carrying inter-event channel at ≠ c" has NO
REFERENT AMONG THE DERIVED ROWS under the ratified set.** (That phrasing is the
honest one and is deliberate: rows 3a/3b are removed by the absent stencil, row 4 is
excluded on its own lane's terms, and **row 5 is UNDERIVED — a NAMED-OPEN, not a
de-firing**. The claim is scoped to the rows the corpus has actually derived, and it
is not an unqualified universal over all possible channels.) Row 3b is the only object that ever
satisfied the kill cell (corpus-wide: *"satisfies the kill"* resolves to row 3b and
nothing else), and row 3b is a mode of an imported operator the axioms never wrote;
row 4 is excluded on its own lane's terms; row 5 is UNDERIVED and stays a
named-open. The kill **de-fires** — on the absence of an established referent, not
on a claim that no referent could ever exist.

*(Wording note: the first cut of this record asserted the bare universal "has NO
REFERENT" and named none of these rows. That over-reached against LC-1's own frozen
table and is corrected here.)*

### §3.3 — Dependency structure of this de-firing (stated so it can be attacked)

The de-firing rides the **pole-absence half** of the lane's item (iv), which
stands **DERIVED from the receipted action alone** — the source doc's own
enumeration of the derived partials includes *"the pole-absence half of item
(iv)"* among *"What stands DERIVED inside the candidate-conditional package"*
([`…_result.md`](../../research/2026-08-10_bound-constitutive_result.md):25, HEADLINE),
and item (iv)'s final-bin note lists *"the pole-absence derivation … stand[s]"*
with only *"the static-stiffness home"* re-homed to clause G. **So the kill's
de-firing does NOT depend on BC-SRC.** It depends on the receipted dynamics
having no longitudinal wave operator, which is prior to the new axiom. BC-SRC is
required for a *different* leg — the observable-**bias** causality (§3.4 of the
source doc), which is candidate-conditional and whose condition R43 has now
discharged by ratifying clause G.

This is stated explicitly because it is the strongest available form of the
result *and* the most attackable: if the orchestrator disagrees that the
pole-absence half is BC-SRC-independent, the de-firing still holds under the
ratified set (R43 :30-35) — it would simply be `DE-FIRED-UNDER-THE-RATIFIED-SET`
rather than `DE-FIRED-ON-THE-RECEIPTED-ACTION`. Both readings de-fire the kill;
they differ only in how much they lean on the new axiom. **This record claims the
weaker, ratified-set reading as its verdict and offers the stronger one as a
finding.**

## §4 — WHAT DOES *NOT* CLOSE (no post-hoc criterion-dropping)

**LC-1 the LANE does not close. Only its kill CELL re-adjudicates.** The frozen
row carries two derivation tasks and they land differently:

- **(b) "bulk √(10/3)c P-wave observability — gapped, confined, or sourceless?"** —
  **DISCHARGED, negatively, and outside the frozen trichotomy.** The answer is
  none of the three: the mode is **non-existent** in the receipted dynamics. The
  frozen cell *presupposed* the trichotomy — LC-1's own result says so at
  `:728`, verbatim `[sic]`: *"uses neither phrase; it **presupposes the
  trichotomy**"*. Recording "non-existent" as a fourth outcome is a **finding
  against the frozen cell's framing**, surfaced here rather than quietly bin-fitted
  into "sourceless".
- **(a) "provenance of cold c_shear = c (is G_vac = ρc² derived or a matching
  condition?)"** — **NOT DISCHARGED.** The bound-constitutive lane explicitly
  leaves the value chain imported: §5.3 (`:209`), verbatim `[sic]`: *"The static stiffness
  `κ = c⁴/7G` and `ν_vac = 2/7` remain VALUE-imports exactly as #261/#506 left
  them; this lane derives the FORM of the static response … and the ABSENCE of
  the radiative channel — neither touches the imported values"*. LC-1 task (a) is
  a VALUE-provenance question and this lane answered a FORM question. It stays
  open.

**Live phantom-consumer rows remain in the corpus, and repairing them is NOT part
of this record.** The corpus still asserts the mode whose non-existence de-fires
the kill:
- [`manuscript/ave-kb/common/port-register.md`](../../manuscript/ave-kb/common/port-register.md):91,
  verbatim `[sic]`: *"the corpus then **owes a mechanism** for why a mode that
  propagates freely at $\sqrt{10/3}\,c$ in its linear passband does not radiate
  from a strong quadrupolar source."* The debt is discharged by *"there is no such
  mode"*, but the row's own live state is Reading-A LIVE and the discharge is
  routed to the R40 demotion sweep's re-derivation queue, not edited here.
- [`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md`](../../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md):146,
  verbatim `[sic]`: *"$\nu=2/7$ is **GR-imported**"* — the seam where the static
  import generates the P-branch. Mechanism sentence (source doc §5.3): *"a static
  ratio was fed to a wave operator the axioms never wrote."* Routed, not edited.

Until those rows are re-derived or demoted, a reader can still find the phantom
asserted in the corpus. That is an honesty-lag to burn down, not a hole in this
adjudication — but it is named rather than left for someone to trip over.

## §5 — DISPOSITION

| Object | Frozen text | Disposition under the ratified set |
|---|---|---|
| LC-1 **kill cell** (`brief:44` col 5) | *"An energy-carrying inter-event channel at ≠ c ⇒ arc-level kill"* | **DOES NOT FIRE — premise has no referent AMONG THE DERIVED ROWS** (rows 3a/3b removed by the absent stencil; row 4 excluded on its own lane's terms; row 5 UNDERIVED = named-open, carried forward not swept in). The prior FIRED disposition (via row 3b / PR #930's residue) is **VACATED**: it rested on a mode of an imported operator, not of the axioms. |
| LC-1 **arc-termination** (`brief:59`) | *"LC-1 runs first and its kill condition is arc-terminating."* | **NOT TRIGGERED.** The arc is not terminated; LC-2…LC-5 stand unaffected. |
| LC-1 task **(b)** (`brief:44` col 4) | *"bulk √(10/3)c P-wave observability — gapped, confined, or sourceless?"* | **DISCHARGED NEGATIVELY, outside the frozen trichotomy** — the mode is non-existent. Framing finding recorded. |
| LC-1 task **(a)** (`brief:44` col 4) | *"provenance of cold c_shear = c (is G_vac = ρc² derived or a matching condition?)"* | **OPEN — not discharged.** VALUE-provenance; #261/#506 imports untouched. |
| LC-1 **lane** | — | **NOT CLOSED.** Only the kill cell re-adjudicates. |

**Class:** the de-firing is **CONSISTENCY-class, not a chord.** Its content is
that the substrate has *one* propagation speed on the sectors that carry energy —
which is what the incumbent already says. The source doc books it the same way
(§6 `:225`, verbatim `[sic]`): *"Maxwell/GR-CLASS on this axis (peer, **no chord**)"*.
Nothing here is an AVE-distinct prediction; what changed is that a self-inflicted
kill from an imported operator has been removed.

**Standing:** `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`. Tier-2 applies to
this item per R43 `:35` (*"Tier-2 applies."*) — this record is the receipted
object the Tier-2 reviews, not a cleared verdict.

**Companions:** [R43 ratification](2026-08-10-ruling-r43-ratification.md) ·
[R43 S+G](2026-08-10-ruling-r43-sg-ratified.md) ·
[the source lane result](../../research/2026-08-10_bound-constitutive_result.md) ·
[its committed sweep record](../../research/2026-08-10_bound-constitutive_sweep-record.md) ·
[the arc brief](../2026-08-04_lorentz-compliance-arc-brief.md) ·
[LC-1's result](../../research/2026-08-06_lc1-one-speed_result.md) +
[its dated disposition note](../../research/2026-08-07_lc1-one-speed_result.md) ·
[BC-SRC's equation file](../../manuscript/common_equations/eq_axiom_5.tex).
