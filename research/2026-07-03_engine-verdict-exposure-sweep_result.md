# Engine verdict-exposure sweep — RESULT (the canonized instrument-audit disposition)

**Date:** 2026-07-03 · **Lane:** verdict-exposure audit (4 auditor lanes → implementer canonization) · **Status:** CANONIZED INSTRUMENT-AUDIT — source-of-truth for the exposure grades.

**Class (consistency-vs-emergence):** this is an **INSTRUMENT-AUDIT**, NOT a physics result. It makes **NO** chord / echo / emergence / consistency claim about the vacuum. It grades the *evidentiary standing* of already-merged engine verdicts against two apparatus-pathology classes. Nothing here is booked as a physics finding; every disposition is an evidence-status tag.

**What this sweep does NOT claim (read first — the seduction-trap, named and rejected):**

- **No verdict is proven wrong.** Not one merged conclusion is retracted by this sweep.
- **Bulk localization is NOT claimed real.** The exposure of the Stage-2 / S3 DISPERSE *evidence* does **not** mean "the electron localizes in the bulk after all." That inversion — *"a real self-trap was masked, so the electron localizes after all"* — is the seduction-trap. It is **named and rejected** here, pending the re-adjudication arc. The sweep resolves neither direction.
- **mass = A1 (PR#260) is UNTOUCHED.** Both HIGH result docs' own scope-locks say only the localization *mechanism* was ever at stake, not the mass=A1 identity. That scope-lock is preserved intact.

**Provenance:** the sweep was triggered by the 2026-07-03 Stage-1 blind-readout panel catch (PR #477) — a merged null read on a structurally-degenerate observable without a same-pipeline positive control. That catch motivated an exhaustive sweep of the merged engine-based verdicts for the same two apparatus pathologies.

**Source triage (read-only auditor output, re-verified this lane):** the 4-lane sweep's full 31-row triage. Every file:line cite carried into this doc was **re-verified at `origin/main` HEAD `a0508e50` by the implementer lane** (verify-before-cite; the sweep was read-only auditor output — this lane lands it). The load-bearing nullspace arithmetic was **independently reproduced** (see §4).

---

## 1. Methodology

**Four auditor lanes, one implementer landing.** Four read-only auditor lanes each swept one family of merged engine-based verdicts (localization/cage/genesis; winding/charge-sector; cleave/Chern/phase-space; gravity/GW/network/misc). Each lane READ the driver — not just its result doc — to confirm the *actual* stencil and the *literal* decision observable, and each returned a triage row per verdict plus family notes and an explicit skip-list. This implementer lane then re-verified every carried file:line cite at `origin/main` HEAD `a0508e50`, reproduced the load-bearing nullspace arithmetic independently (§4), and landed the dated exposure caveats.

**Scope.** Only **merged, engine-based, time-domain (or eigensolve) verdicts** were triaged. Analytic-only drivers (closed-form impedance/reflection formulas, forward-computed birefringence coefficients, figure generators, and consistency scaffolds) were skipped by scope, as were unmerged branch-only results. The full skip-list per family is preserved in §4.

**Discipline applied.** verify-before-cite on every carried cite; flag-don't-fix (two conflicts surfaced in §6 rather than silently resolved); consistency-vs-emergence tag (this doc is an INSTRUMENT-AUDIT); INVARIANT-N1 prose nouns for the substrate.

## 2. The two exposure classes

The sweep grades each verdict against two apparatus-pathology classes. A verdict is *exposed* when its rendering apparatus could return the observed reading for a reason unrelated to the physics the verdict claims to test.

**CLASS-1 — stencil pathology.** The operator carrying the dynamics has a structural defect on the lattice it is built on. The load-bearing instance is the **diamond `TETRA_OFFSETS` stencil** (z=4, bipartite, achiral) used by the native-cage / coupled-winding pipeline, as against the canonical **chiral srs z=3** net the electron's (2,3) winding lives on. The four `TETRA_OFFSETS` offsets `(+1,+1,+1)/(+1,-1,-1)/(-1,+1,-1)/(-1,-1,+1)` (`src/ave/topological/cosserat_field_3d.py:134-139`) all have **odd coordinate-sum**, so `Grad` maps a node to its opposite-parity neighbours and `L_D = Div·diag(D)·Grad` connects **only same-parity** nodes. The periodic box therefore **decouples into two interpenetrating sublattices**, each carrying its own nullspace — the operator is nullspace-bearing (positive-**semi**-definite, not SPD) and cannot represent lattice chirality on an achiral host. A verdict is CLASS-1-exposed when its dynamics run through this operator on structure the operator cannot faithfully carry.

**CLASS-2 — blind readout.** The verdict is a null (or a "does-not-exist" / "disperses" / "breaks") read on an observable the apparatus was **never shown to be able to read the opposite of**, in the same pipeline. Two sub-patterns: (a) a **null without a same-pipeline positive control** — the only "the instrument can SEE the effect" demonstration runs on a *different* engine; and (b) a **structurally-degenerate observable** — a global-sum or hardcoded form that is zero (or fixed) by an antisymmetry / an inserted exponent, so the readout cannot register the alternative. An energy-conservation gate is a rigor guard against dissipation-bought results, **not** a positive control that the readout can register the effect.

## 3. The 31-row triage table

Condensed from the 4-lane triage JSON. **Grade counts: 2 HIGH · 4 MEDIUM · 25 LOW = 31.** Stencil / positive-control / observable columns are the auditor's classification; key file:line cites re-verified this lane. Full per-row `reason` text lives in the source triage; the load-bearing rows are expanded in §4–§5.

| # | Fam | Grade | Verdict (short) | Stencil | Pos. control | Observable / exposure note |
|:-:|:-:|:-:|:--|:--|:--|:--|
| 1 | F1 | **HIGH** | Stage-2 native-cage MODE-III DISPERSE (bulk self-trap falsified) | diamond TETRA z4 (bipartite) | PARTIAL / mislocated (Cartesian) | interior-peak time-series; CLASS-1 nullspace-heavy operator + CLASS-2 mislocated control |
| 2 | F1 | **HIGH** | Stage-3 cavity-pinning DISPERSE-FALSIFIED (winding+H_couple+cavity does not pin) | diamond TETRA z4 (reuses S2 `L_D`) | PARTIAL / mislocated (Cartesian) | A1-centroid spread DELTA; inherits S2 CLASS-1 + CLASS-2; §5 self-admitted instrument artifact |
| 3 | F1 | LOW | Keystone energize-LOCK NEGATIVE | Cartesian 7-pt | NO (n/a here) | already-canonical negative; not diamond-stencil |
| 4 | F1 | **MED** | Genesis-24 keystone-pump NOT-RESOLVED (Case C) | diamond-K4 class | PARTIAL | energy-budget delta (runs away, nonzero); pump plausibly a coupling-routing artifact; doc self-retracts lock |
| 5 | F1 | LOW | Cage-stiffening-wall | Cartesian 7-pt | YES | live positive control present |
| 6 | F1 | LOW | Cavitation-core-probe | 2D rarefaction bulk-flow | n/a to diamond/srs | out of diamond/srs scope |
| 7 | F2 | LOW | S1 winding-DOF conservation = PASS-WITH-FLAGS | cubic chain (not diamond) | YES | live; gate-(c) local-continuity near-structural WARN, non-load-bearing |
| 8 | F2 | **MED** | #415 coupled A1+winding eigensolve = DOES-NOT-EXIST (gate-d FAIL) | diamond TETRA z4 | PARTIAL | eigenvalue + linking-integer; CLASS-1 `L_D` nullspace confirmed; A1 gates de-risked (opposite spectral end) |
| 9 | F2 | LOW | #59/#417 phase-space coupling-winding = BREAK | diamond TETRA z4 | YES | live planted-(2,3) readback; carrier-detuning discriminator stencil-independent |
| 10 | F2 | LOW | clm-wcoul2 writhe linear-channel = COULOMB-RECOVERY | regular-cubic CrystalGraft | YES | not diamond; achiral-hedgehog degeneracy declared in driver |
| 11 | F2 | LOW | writhe Gate-0 pair feasibility = STABLE-IN-A-WINDOW | regular-cubic (S1 host) | YES | T-symmetry-zeroed carries nonzero floors |
| 12 | F2 | LOW | compositeness engine-leg = ENGINE-BLOCKED | cubic host / n/a | YES | validate-on-known correctly FAILED to ENGINE-BLOCKED |
| 13 | F2 | LOW | chiral-vector-TLM phase-1 = OUTCOME A | srs z3 (chiral signal) | YES | diamond used as correct achiral null; chiral pos-control on srs |
| 14 | F2 | LOW | charge-quantization-gate = Q=Link(∂Ω,F) recovered | diamond/tetrahedral curl | YES | decision observable is field-phase loop, lattice-faithful |
| 15 | F2 | LOW | winding-charge-quant: lattice does NOT force p=2 (FIT/ECHO) | parametric (integers) | PARTIAL | value-echo immunity; consistency-class |
| 16 | F3 | LOW | Cleave registry-pump Chern (2-band) | analytic 2-band toy | YES | planted-nonzero control |
| 17 | F3 | LOW | N-band Cleave registry-pump Chern (8-band srs) | srs z3 (genuine 8-site) | YES | two-sided VOK; strongest liveness in F3 |
| 18 | F3 | **MED** | K4 Bloch dispersion (q·ℓ)⁴ QUARTIC chord | diamond TETRA z4 (rank-2 tensor) | PARTIAL | MIXED; headline slope-4 is hardcoded form (CLASS-2); corpus ALREADY demoted (clm-k4d4ph) |
| 19 | F3 | LOW | srs Bloch dispersion band-edge slope-2 | srs z3 (genuine chiral) | YES | this IS the positive control that caught #18 |
| 20 | F3 | LOW | two-sublattice K4⊗Cosserat band structure | diamond TETRA z4 (rank-2) | YES | dynamical eigensolve, gapped, no statics nullspace bite |
| 21 | F3 | **MED** | Phase-space coupling-winding #417 = BREAK ((2,3) not a conserved orbit) | diamond TETRA z4 | YES | CLASS-1 chiral-on-achiral category zone; ZERO stencil ack in doc; carrier-detuning carries the negative |
| 22 | F3 | LOW | Winding charge-quantization (p=2, quark thirds) | parametric (p,q) | YES | not a lattice sim |
| 23 | F3 | LOW | Vacuum-impedance-probe Phase-A feasibility | analytic derivation | n/a (no pipeline) | analytic feasibility, no readout |
| 24 | F4 | LOW | Q~30.8 cold-cage α-free ringdown NEGATIVE (the "clean negative") | Cartesian 7-pt (CrystalEngine) | YES | PRIORITY TARGET CLEARED — Cartesian, not diamond; readout live |
| 25 | F4 | LOW | Electron α echo→chord eigenframe leg: GATE1 FAIL → HALT | diamond TETRA z4 | PARTIAL | exposure CONTAINED: nullspace filtered, verdict is a HALT |
| 26 | F4 | LOW | Node-scattering multiplicity Fork-A REFUTE-R3 | srs/diamond connect-map | YES | self-caught its own R3 overclaim (Rule 12) |
| 27 | F4 | LOW | Stage-3 two-way gravitational back-reaction (#86) | diamond TETRA z4 (binding-E leg) | YES | binding-deficit loop; live |
| 28 | F4 | LOW | Node-circulator lossless bulk↔shear coupling | 2-mode/port generator | YES | Gate-B 100%-sloshing control defeats vacuous-conservation |
| 29 | F4 | LOW | FT-1 E-mode Bose-Einstein occupation NEGATIVE | k-space Debye spectrum | YES | live |
| 30 | F4 | LOW | Two-body mass-sector scattering (T0i) force-sign | Cartesian 7-pt (Master-Eq) | YES | self-caught R1 clean-NULL→MIXED (Rule 12) |
| 31 | F4 | LOW | Vacuum-varactor scatter operator S(A) per-bond | srs/diamond connect-map | YES | recovers bedrock at S=1 |

## 4. Family notes (verified)

<!-- filled next commit -->

## 5. Disposition and the caveats landed

<!-- filled next commit -->

## 6. What the claim-trail surfaced that the sweep missed

<!-- filled next commit -->
