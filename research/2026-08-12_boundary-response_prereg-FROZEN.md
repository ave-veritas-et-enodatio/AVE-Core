# THE BOUNDARY-RESPONSE DERIVATION (R51 §4) — FROZEN PREREG

**Date:** 2026-08-12 · **Branch:** `lane/2026-08-12-r51-boundary-response` · **Base:** `origin/main` @ `ecf91aec`
**Premise (cited, NOT re-derived):** `_orchestration/docket-entries/2026-08-12-ruling-r51-a1-two-objects-carve.md`
— the ratified A1 two-objects carve. This lane executes R51 §4, which is also #261's one open item
(eigenmode existence).

**FREEZE DISCIPLINE.** This document is committed **ALONE** and **PUSHED** before any derivation
content, algebra, driver, or lane-produced number exists in the tree (freeze-by-push, ave-prereg
Step 3.11). The verdict grammar in §2 is frozen **before** the derivation runs. Rule 11: no bin may
be edited, widened, or re-labelled after any derivation content lands.

**Class:** DERIVATION (analytic) + ADJUDICATION BRIEF. **Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`;
edits no KB leaf, register, ledger, axiom, or ruling; changes no solidity; propagates nothing.**
Engine `src/ave` byte-untouched, and **no engine run may corroborate anything in this lane** (the
#935 stencil fence, inherited: `crystal_engine.py` codes a bulk scalar V, so an engine energy
functional carries exactly the import under test).

---

## §0 — Standard Vacuum Analysis header (SVA v0.2-pilot)

1. **SECTOR / OWNERSHIP.** The driven coordinate is **A1 dilatation** (the defect's size / common
   mode, the `(1,1,1,1)/2` port vector — `k4-port-irrep-decomposition.md:47`). The defect's fixed
   content is **T2 Cosserat winding** (charge/spin, `master-equation.md:20`). **Cross-wiring check
   performed and the carve declared up front:** this lane writes `E(R; n)` — a scalar potential on
   the **A1 coordinate** `R`, parameterised by a **fixed integer T2 label** `n`. That is NOT a
   phasor wire: `n` never becomes a dynamical DOF inside the A1 `(V_inc, V_ref)` pair, and no
   `V_ref` is treated as independent. The `master-equation.md:20` fence and R51 §7 (two distinct
   quaternionic structures) are held. **If the derivation cannot keep `n` a parameter — if the
   restoring force requires `n` to respond dynamically — that is a STUCK-POINT, reported, not
   worked around.**
2. **REGIME / PHASE-STATE.** MODE = constitutive existence question (does a stationary point with
   positive curvature exist?). REGIME = **cold, sub-yield, crystalline, lossless-reactive**
   (Regime-I). PHASE-STATE = cold-reactive; **past-wall and de-bonded states OUT OF SCOPE**
   (Axiom 5 phase map clauses c3/c4 are unwritten). DC bias point = the Axiom-5 clause-Q quiescent
   point away from the defect; the defect is the clause-S deposit.
3. **CIRCUIT STATEMENT (before any framework word).** A fixed charge sits on a tank. Drive the
   tank's single common-mode coordinate. **Question: is there a nonzero shunt susceptance
   returning energy to that coordinate, or is the coordinate a through-line to ground?** In
   mechanical dress: does `E(R)` have `E''(R*) > 0` at a finite `R* > 0`. **Total-vs-slot
   declared:** the question is about the TOTAL response at the defect boundary, not any one series
   slot; a slot-level zero does not settle it, and a total-level zero is the verdict.
4. **PLANE & PROJECTION.** Reference plane = **the defect boundary at `r = R`** (the surface where
   the fixed-content interior meets the vacuum exterior). Projection: the medium's A1 compliance
   and the defect's own self-stiffness are two stiffnesses **at one common coordinate `R`**, so
   they compose in **PARALLEL** (energies add at fixed `R`) — *unless* the medium sits in the load
   path, in which case SERIES. **This is FORK-SP, frozen open with both branches (§3).** Under
   PARALLEL a zero medium stiffness is transparent; under SERIES a zero medium stiffness is a
   short and kills the tank outright. The fork is decided by derivation, never by convenience.
5. **CONSTITUTIVE PROVENANCE.** Allowed ingredients and their tags:
   - `G_vac = ρ_bulk c²` — **DERIVED** (cross-check `v_T = √(G/ρ) = c` exact;
     `derived-numerology.md:56`; the 13-OOM `G_string`/`G_vac` conflation is corrected canon,
     `lc-electrodynamics.md:76`).
   - Geometry: K4 tetrahedral stencil, the `A₁ ⊕ T₂` port split, the `1/r²` exterior falloff free
     from the clause-G elliptic solve — **DERIVED**.
   - Axiom 3 curl-only potential (`eq_axiom_3.tex:22`), Axiom 4 saturation kernel, Axiom 5 clauses
     S/G/Q — **AXIOM (receipted)**.
   - **`K` (bulk modulus) and anything bottoming out in `K = 2G` — FORBIDDEN IN THIS CHAIN**
     (#261: GR-imported, not crystalline, not constitutively forced). Every step is provenance-
     tagged; a step that silently re-imports `K` is a lane failure, not a result.
   - `ℓ_node`, `m_e`, `α` — **IMPORTED** (calibration). Admissible as a *floor location*, but a
     result whose EXISTENCE depends on them is `CANNOT-CLOSE-WITHOUT-IC`, not
     `RESPONSE-EXISTS`. This distinction is the whole point of bin 3.
   - The Faddeev–Skyrme / Op10 quartic — **PROVENANCE UNVERIFIED AT FREEZE.** It is the corpus's
     Derrick bypass #2 (`relativistic-inductor-newtonian-limit.md:62`) and `vol4/claim-quality.md:1587`
     records it as *"imported from Vol 2 / Axiom 1 rather than re-derived."* Its tag is
     **BRACKETED(pending-verification)** and verifying it is a derivation step, not an assumption.
6. **ENERGY LEDGER.** Everything here is **rim** — within-system reactive exchange, no port, no
   arrow, no loss word. The A1 near-field is banked REACTIVE added-mass, explicitly **NOT-A-PORT**
   (`port-register.md:77`, P9: *"a port drains; this stores-and-returns"*). No step may introduce
   radiation, damping, or `Q` without naming a port — and this lane names none.
7. **CALIBRATABILITY.** The primary target is a **FORM** (existence + exponents + the symbolic
   frequency), explicitly **not a value**. Per the brief: symbols, not numbers. A numerical tank
   frequency is out of scope and its absence is not a gap.
8. **DISCRIMINATION CLASS.** **DC-internal** (a cold-medium constitutive property with no AC
   readout in this lane). Consequences frozen now: **(a)** a NO-RESPONSE verdict here is a
   *framework-internal* result — it fires R51's own §5(ii) kill-check on item 2 — and is
   explicitly **NOT** an empirical falsification of anything; **(b)** per the AC/DC carve a
   DC-internal null cannot be framework-level without a liveness-proven readout, and this lane has
   none. **SM counterfactual:** ordinary elasticity gives a defect's breathing mode a restoring
   force trivially, *from K*. So a positive result is **not** phenomenologically AVE-distinct; the
   only distinct content would be its **provenance** (obtained without K). Symmetric standard
   applied: standard elasticity also measures its moduli rather than deriving them, so "K is
   imported" is not by itself an AVE-specific defect — the question is whether AVE's *own* chain
   needs it. **Tautology filter (armed):** see §4.
9. **CERTIFICATION PLAN.** Gates frozen in §3–§5 before any algebra. UNRUN ≠ PASSED. Negative and
   positive controls named in §5.
10. **ADJUDICATION ROUTING.** This lane settles FORK-SP (§4 P4) and R51 §5(ii). It **routes, does
    not settle**, the K-identity question (§6 deliverable = an options brief with evidence, no
    recommendation unless the math forces one). The §9-pass / #955 clock-chain connection is
    **FLAGGED, NOT BANKED** (R51 §5(iii) requires quantitative reproduction, which this lane does
    not attempt).
11. **NUMERICAL CONDITIONING.** No floating-point arm; the lane is symbolic power-counting and
    exact algebra. Named hazard: **scaling-ansatz Derrick counting is exponent-only** and cannot
    see a prefactor that vanishes. Any exponent-level "stiffness exists" claim must be checked for
    a zero prefactor before it is booked.

---

## §1 — The target, stated in one sentence

From `G_vac` + geometry alone, with **no imported `K` anywhere in the chain**, does a pure
common-mode (A1, all-ports-in-phase) boundary drive on a defect of **fixed topological content**
meet a **restoring** response — i.e. does the defect's energy `E(R)` at fixed content have a
stationary point at finite `R* > 0` with `E''(R*) > 0`?

### §1.5 — The physical picture, before equations

- A knot of fixed winding sits in the cold lattice. Its size `R` is the one coordinate being
  driven. Squeeze it uniformly and let go: does anything push back, and does the push-back come
  from the medium or from the knot?
- The bond network has already answered for the **bulk**: it does not push back. Axiom 3's
  potential is curl-only, so a purely longitudinal configuration stores **zero** potential energy
  (#935's flat direction). The exterior `u_r = B/r²` at fixed clause-S flux `B` is *independent of
  `R`* — breathing at fixed `B` moves no far field.
- So if a restoring force exists at all, it is **the knot's own self-energy curvature**, not the
  vacuum's A1 compliance. The medium's A1 channel may be transparent (parallel) or a short
  (series) — FORK-SP.
- The knot's self-energy has a term the bulk lacks: its winding lives on the **shear** sector,
  which has a real modulus `G_vac`. A fixed winding squeezed into size `R` costs shear gradient
  energy. Classic Derrick counting in 3D makes that term grow **linearly in `R`** — so it wants
  the knot to *shrink*, monotonically. Alone, it gives collapse, not a tank.
- Therefore the whole question reduces to: **is there an allowed term that grows as `R` shrinks,
  and is it a smooth curvature (a tank) or a hard wall (a constraint)?** A smooth counter-term
  gives `RESPONSE-EXISTS`. A hard lattice floor gives a defect resting against a wall — which
  rattles but is not a harmonic tank, and whose scale is a frozen-in initial condition.

---

## §2 — THE VERDICT GRAMMAR (frozen before any derivation)

Exactly one of three verdicts is returned. The wording of each is frozen here verbatim.

- **`RESPONSE-EXISTS(form)`** — a stationary point at finite `R* > 0` with `E''(R*) > 0`, derived
  from `G_vac` + geometry + receipted axioms, with **every step provenance-tagged and no `K` in
  the chain**. Deliverable: the FORM of `R*` and of `ω_tank` in symbols. The `(form)` slot is
  filled with the derived functional form, e.g. `RESPONSE-EXISTS(E = aR + bR⁻¹)`.
- **`NO-RESPONSE`** — no stationary point with positive curvature is reachable from the allowed
  ingredients: `E(R)` is monotone, or every stationary point is a maximum, or every candidate
  restoring term re-imports `K`. **Consequence, stated in advance:** the common-mode tank does not
  exist; compression is **marginal** (neither rings nor sits — a conserved density); **R51 item 2
  dies by its own §5(ii) kill-check.** This is a banked result, not a failure of the lane.
- **`CANNOT-CLOSE-WITHOUT-IC`** — a restoring response exists **but** its existence or its scale is
  fixed by a frozen-in quantity (the lattice floor `ℓ_node`, the freeze-in pre-tension `u₀`, or any
  genesis-deposited datum) rather than derived from `G_vac` + geometry. The verdict must name
  **which** initial-condition datum, and state whether the datum sets only the SCALE (response
  exists, value imported) or the EXISTENCE itself (no response without the datum).

**Bin-integrity check (ave-prereg Step 3.6), run now:** every falsifier in §5 routes to one of
these three; no falsifier points at a bin absent from this set; the dangerous direction — a
`NO-RESPONSE` masquerading as `RESPONSE-EXISTS` via a loosened criterion — is closed by requiring
`E''(R*) > 0` **at finite `R* > 0` with a non-vanishing prefactor**, not merely "a term with the
right exponent exists" (§0 row 11).

---

## §3 — Analytic expectations: the walked picture's predicted forms, frozen (Step 3.9)

Let `R` be the defect size coordinate, `n` the fixed integer winding, `B` the fixed clause-S flux,
`Λ` the fixed winding amplitude set by `n`. Under a 3D scaling ansatz `u(x) = f(x/R)`:

| Term | Predicted form | Exponent | Sign of effect | Provenance at freeze |
|---|---|---|---|---|
| `E_shear` — fixed winding's shear gradient energy | `∝ G_vac · Λ²(n) · R` | **+1** | wants to SHRINK | DERIVED (`G_vac`) |
| `E_A1,pot` — longitudinal potential energy | **identically 0** | n/a | none | ENTAILED by Ax3 curl-only |
| `E_stab` — the counter-term (if any) | `∝ R⁻¹` (Skyrme-like) *or* hard wall at `ℓ_node` | **−1** or non-analytic | wants to EXPAND | BRACKETED / IMPORTED |

**Predicted stationary point (branch A, smooth `R⁻¹` counter-term):**
`E(R) = aR + b/R` ⇒ `R* = √(b/a)`, `E''(R*) = 2b/R*³ > 0` — a genuine tank, exactly one crossing.

**Predicted stationary point (branch B, hard floor only):** `E(R) = aR` monotone ⇒ the defect rests
**on** the floor at `R = ℓ_node`. One-sided constraint, not a harmonic tank.

**Tank frequency, IF a response exists (FORM only, symbols not values):**
`ω_tank = √( E''(R*) / M_eff )`, with `M_eff` frozen as a two-branch fork:
`M_eff^(i) = 4π ρ_bulk R*³` (medium added-mass, the P9 reactive near-field) **or**
`M_eff^(ii) =` the defect's own dilatation inertia. **Both branches are frozen; the cheapest
separator is run and reported.** The lane does **not** pick one by fiat.

**Cross-check against corpus prior (`research/2026-07-01_electron-unifier-cocompress_result.md`):**
that lane's analytic Part 1 measured `E_grad_A1 ∝ R⁻²` and `E_tank_w ∝ R⁺¹` with "exactly one
crossing" and `p<3` forced in 3D. My `+1` shear exponent should **agree** with its `R⁺¹`. Its
`R⁻²` A1-gradient term is the one I predict to be **absent** under the curl-only potential — if it
survives my provenance audit, my picture is wrong and I say so. Its Part-2 numerical leg is
**downgraded to near-tautology by its own verdict** and is therefore **not** evidence for anything
here; I cite its Part-1 analytic leg only.

---

## §4 — Entailed-vs-fireable audit (Step 3.10), run BEFORE the derivation

Honesty requires separating what this lane can genuinely adjudicate from what it merely re-exhibits.

- **P1 — "the bulk A1 channel has no restoring force." ENTAILED.** This is #935's finding restated;
  Axiom 3's curl-only potential forces it. When it fires the honest verb is **DEMONSTRATED, not
  ADJUDICATED.** It is background, not this lane's result, and will be reported as such.
- **P2 — "the defect self-energy `E(R)` has a stationary point with `E''>0` from allowed
  ingredients." FIREABLE.** It can genuinely come out either way: a monotone `E(R)` (collapse), or
  a minimum. Nothing installed forces the answer.
- **P3 — "the counter-term's provenance is K-free." FIREABLE.** The audit can find `K` in the
  chain; if it does, the verdict is `NO-RESPONSE` on the stated scope.
- **P4 — FORK-SP: does the medium's A1 compliance sit in PARALLEL (transparent) or SERIES (a
  short)? FIREABLE, and load-bearing** — SERIES kills the tank even if `E''>0`. Both branches
  frozen; neither presumed.
- **Structural-degeneracy self-check (Step 3.8).** Is `NO-RESPONSE` forced by bookkeeping? **Partly
  — and the trap is named now:** if I admit *only* the curl-only potential and then ask about a
  purely longitudinal coordinate, the answer is zero **by construction**, and reporting that as a
  physics null would be circular. This is precisely why the question is posed at the **defect
  boundary** with **fixed T2 content**, where the shear modulus legitimately enters the A1
  coordinate's potential. **Any NO-RESPONSE verdict must state explicitly whether it survives
  outside the curl-only-by-construction zero** — if it does not, the honest verdict is
  `NO-RESPONSE` scoped to the bulk with the boundary question left open, and I say that instead.

---

## §5 — Controls and falsifiers (frozen; UNRUN ≠ PASSED)

**POSITIVE CONTROL (mandatory before any null is bookable).** Run the *identical* energy-ledger
machinery on a case that **must** return a restoring response: a standard elastic medium **with `K`
restored**, where the breathing defect is the textbook acoustic monopole with a known nonzero
stiffness. If the machinery returns "no response" there, the machinery is broken and **no null from
this lane is bookable.** A second control: the T2 transverse sector, which must return the known
`c = √(G/ρ)` restoring structure.

**NEGATIVE CONTROL.** Apply the machinery to a genuinely portless flat direction with no fixed
content (a free longitudinal displacement of the empty lattice). It **must** return no restoring
force. If it manufactures stiffness there, the machinery is over-fitting and every positive is void.

| # | Falsifier | Fires → verdict |
|---|---|---|
| F1 | `E(R)` is monotone on `0 < R < ∞` with all allowed terms admitted | `NO-RESPONSE` |
| F2 | Every candidate counter-term's provenance chain contains `K` or `K = 2G` | `NO-RESPONSE` |
| F3 | A counter-term is K-free but its coefficient is a genesis/freeze-in datum or `ℓ_node` | `CANNOT-CLOSE-WITHOUT-IC` (naming the datum) |
| F4 | FORK-SP resolves SERIES and the medium's A1 stiffness is zero | `NO-RESPONSE` (the short dominates) |
| F5 | The stationary point exists but has `E'' < 0` (a maximum) | `NO-RESPONSE` (unstable; not a tank) |
| F6 | The exponent-level stiffness has an identically vanishing prefactor | `NO-RESPONSE` (§0 row 11) |
| F7 | The restoring force requires `n` to become dynamical inside the A1 phasor | **STUCK-POINT**, reported; fence held, no verdict forced |
| F8 | The positive control fails | **NO VERDICT BOOKABLE**; lane reports machinery failure |

**Observable robustness ladder (Step 3.7), declared now.** PRIMARY (gating) rung = **EXISTENCE**
(is there a restoring response, yes/no). SECONDARY = **FORM/exponents**. Explicitly
**supplementary, never gating** = any magnitude or numerical frequency. If the exponents prove
ansatz-dependent, **existence + the K-provenance verdict still stand** and are what the lane books.

---

## §6 — Deliverables (fixed order, per the lane brief)

1. This frozen prereg (committed alone + pushed).
2. The form derivation, with every step provenance-tagged.
3. **IF** a response exists: `ω_tank` as a FORM prediction (symbols), and what it implies for the
   clock chain — **FLAGGED, NOT BANKED**; the §9-pass / #955 connection is named as a routed
   follow-on, and R51 §5(iii)'s quantitative bar is explicitly *not* claimed.
4. The **K-identity adjudication brief** for Grant: which of R51 §3's three readings the result
   supports — (i) **constitutive**, (ii) **quench initial condition** (Grant's lean; ties to the
   `trampoline-framework.md:95-125` freeze-in, where `u₀ = ρΩ²_freeze r²_node / 2K₀` and `G` itself
   is anchored to `u₀`), or (iii) **boundary-response echo** (the defect-boundary stiffness is the
   real object; `K = 2G` is its far-field shadow). **Options with evidence; NO recommendation
   unless the math forces one.** This lane does **not** derive `K`'s value and must not appear to.

**Anti-rescue guard.** Real odds this returns `NO-RESPONSE` are held to be substantial. A derivation
that reaches a tank only by admitting an untagged term, a `K`-descended coefficient, or a
dynamical `n` has **failed**, and the honest output is `NO-RESPONSE` or a STUCK-POINT report — not
a rescued positive. **2-attempt cap on every fork; this is exactly the terrain where compute
spirals manufacture stiffness that isn't there.**
