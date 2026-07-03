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

### Family 1 — localization / cage / genesis (the load-bearing pair)

**Two findings, both reproduced this lane (flag-don't-fix).**

**(1) CLASS-1 — the Stage-2 / S3 native operator is nullspace-heavy AND sublattice-decoupled.** Because all four `TETRA_OFFSETS` have odd coordinate-sum (`cosserat_field_3d.py:134-139`), `L_D = Div·diag(D)·Grad` connects only same-parity nodes: the periodic diamond box splits into two non-communicating sublattices, each with its own nullspace. A smooth centered seed projects almost entirely onto that frozen nullspace — the `L_D` neither self-focuses nor disperses it. **Independently reproduced this lane** by extracting `build_grad_div_periodic` + `assemble_L_D` verbatim from `origin/main:src/ave/solvers/native_cage_imex.py` and running them read-only:

| Probe (cold `D=1`) | N=8 | N=10 | N=12 |
|:--|:--|:--|:--|
| off-diagonal coupling: same-parity mass | 384.0 | 750.0 | 1296.0 |
| off-diagonal coupling: cross-parity mass | **0.0** | **0.0** | **0.0** |
| near-zero eigenvalues (`\|λ\|<1e-9`) | 16 | 8 | 16 |
| centered v14 sech energy-fraction in nullspace | **98.0%** | 96.1% | 93.5% |
| (v14 seed: `N`, `dx=0.5`, `amp=0.85`, `radius=2.5`) — null-projected peak | 0.653 | 0.574 | 0.499 |

The 100%-same-parity coupling confirms the two-sublattice decoupling; the checkerboard `(-1)^(i+j+k)` is in the `Grad`-nullspace (`‖Grad·checker‖=0`, Rayleigh=0) and persists under **any** diagonal `D` (verified saturated random `D∈[1,1000]` — Rayleigh still 0), because it is a `Grad`-kernel property. So the DISPERSE observable (interior peak) is governed by an operator artifact, not the bulk-self-focusing physics the make-or-break claims to test. The corpus already half-knows this: commit `78e7d403` records "engine is degree-4 ACHIRAL diamond, NOT canonical degree-3 chiral srs; corpus self-contradictory".

> **BOX-SIZE NUANCE (verify-before-cite catch, this lane):** the **98%** nullspace-energy fraction is the **N=8** probe number (the seed occupies most of the small box). At the **production N=24** box the same v14 sech projects **≈67%** of its energy onto the nullspace, not 98%. Both numbers say the majority of the seed energy sits in the frozen decoupled subspace; the 98% headline is specifically the small-box figure and is quoted as such. The `peak 0.653 of 0.850` pair is likewise the N=8 null-projected-peak vs seed-peak.

**(2) CLASS-2 — the one positive control runs on the wrong engine.** The only "the instrument can SEE a self-trap" control (`engine_stage2_native_cage_imex_makeorbreak.py:100` `run_cartesian_reference`; `s3_cavity_pinning_gate.py:200` `_cartesian_v14_self_traps`) runs on the **Cartesian `MasterEquationFDTD`** engine — its own docstring calls it "the known-good self-trap the native run is compared to" — NOT the native `TETRA_OFFSETS` pipeline that renders the DISPERSE verdict. On the native pipeline **every** seed disperses (sech 0.315, gaussian 0.236, linear 0.0074). There is no demonstration anywhere that the native pipeline can read "bound/persist" for **any** input. The energy-conservation and winding-integer gates are rigor guards, not liveness proofs that the readout can register a bound state.

**S3 inherits both** (same `L_D` on the A1 block, `coupled_cage_winding.py:105` import / `:345` apply — the apply-site comment even asserts "real SPD", the same doc-error), and its own **§5 "load-bearing build finding"** (`:70`) admits the native vector operator **unwinds** the (2,3) integer even uncoupled (3→0→−1) — a self-disclosed instrument artifact corroborating that the native diamond operator mishandles localized structure.

**The srs-z3 / diamond-z4 asymmetry (exploratory, NOT adjudicated).** The genesis v5–v15 chiral-lattice series (genesis-v13 "LOCALIZATION-LANDED" among them) runs on the **srs z=3 chiral** TLM lattice (`chiral_lattice_v13_genesis.py`), NOT the bipartite diamond production stencil. The DISPERSE falsifications (Stage-2 / S3) land on **diamond z=4**. So the one POSITIVE localization verdict lands on srs-z3 while the DISPERSE negatives land on diamond-z4 — a stencil-keyed asymmetry worth a dedicated srs-family pass. **Tagged exploratory-not-adjudicated:** this is a surfaced asymmetry, not a claim that srs would host a bulk trap.

**What Family 1 does and does NOT claim:** it is NOT claiming a real self-trap was masked and the electron localizes in the bulk after all — the sweep cannot resolve that. It IS claiming the two DISPERSE falsifications were rendered on a stencil whose operator has a large nullspace a smooth seed dominantly occupies, and that neither verdict has a same-pipeline positive control demonstrating the native readout can register a bound core. Per flag-don't-fix, this is a surfaced conflict for Grant's adjudication. **None of this touches mass = A1 (PR#260);** both docs' scope-locks ("only the localization MECHANISM changes") are unaffected — only the diamond-stencil DISPERSE *evidence* for that mechanism-switch is flagged. The doc-error `assemble_L_D` docstring "SPD" (`native_cage_imex.py:151`) should read positive-**semi**-definite (nullspace measured).

### Family 2 — winding / charge-sector (no HIGH; the good-news family)

The auditor reproduced the same diamond-`L_D` arithmetic (8–16-dim nullspace at N=4/6/8; checkerboard in `Grad`-nullspace under any `D`), confirming the CLASS-1 pathology in the **#415/#59** operator. **Mitigant that de-risks the A1 gates:** for `H = ω_b·I − c²·L_D` solved `which='SA'`, the nullspace maps to eigenvalue `ω_b=+1` at the **largest**-algebraic end — the opposite end from the most-bound state #415 reads (`w_H=−7.065`) — so #415's reported A1-confinement gates (a/b/c/e) are **not** directly nullspace-contaminated (why #415 is MEDIUM not HIGH). Every other LIVE winding/charge verdict either runs on the **cubic CrystalGraft** host (S1, clm-wcoul2, writhe-gate0 — no `TETRA_OFFSETS` in that chain), uses the diamond as a correctly-constructed **achiral null** with a nonzero chiral positive control on srs (chiral-vector-TLM, chiral-srs), or makes **no handedness/parity claim** so the achiral category-error does not bite. The CLASS-2 discipline is notably strong across the family (compositeness ran validate-on-known and correctly FAILED-to-ENGINE-BLOCKED; writhe-gate0 carries nonzero pos-control floors). No FAIL, no HIGH.

### Family 3 — cleave / Chern / phase-space

The two Cleave Chern verdicts (2-band + N-band) and `srs_bloch_dispersion` are **clean on srs z=3**. The two diamond-stencil verdicts (`k4_bloch_dispersion`, `cosserat_band_structure_two_sublattice`) use diamond **correctly** — dynamical eigensolves with the RANK-2 general-force-constant bond tensor (not a Cartesian Laplacian), so the statics `Div·Grad` nullspace bite does not fire; their exposures are CLASS-2, not CLASS-1. The one genuine CLASS-1 exposure is **#417 phase-space-winding** (a (2,3) chiral-winding BREAK verdict run on the achiral diamond `TETRA_OFFSETS`, with **zero** stencil acknowledgment in the doc) — graded MEDIUM because the carrier-detuning discriminator carries the negative independent of the stencil and the positive control plants+reads a (2,3) on the same diamond. The **k4_bloch "QUARTIC chord"** is a CLASS-2 structural restatement (photon slope-4 is the hardcoded form `1+κ·Ξ·(kℓ)⁴`, not an eigenvalue; the genuine eigensolve gives slope-2), but the corpus **already self-corrected** — `clm-k4d4ph` is demoted to conditional-on-open-gate `wejkhvnfb`, and `srs_bloch_dispersion.py` (on main) is the positive control that caught it.

### Family 4 — gravity / GW / network / misc

**PRIORITY TARGET CLEARED:** the Q~30.8 cold-cage "clean negative" (the load-bearing corpus negative, `Q=1/α` cited as identity) is **NOT** CLASS-1-exposed — its host is CrystalEngine's **Cartesian** 7-point Laplacian (`crystal_engine.py:154`, no TETRA/diamond import) and its readout is live (driven Hilbert-envelope ringdown with a nonzero positive control). The only CLASS-1-exposed Family-4 verdict is the α-echo→chord eigenframe leg, and its exposure is **contained** (nullspace documented and filtered; verdict is a HALT — no bankable chord rests on it). Three Family-4 docs had already caught their own CLASS-2-adjacent overclaims via Rule-12 before this sweep (node-scattering R3, two-body T0i R1, coupled-network GATE1). One discovery gap surfaced (Route-C loaded-μ `|dH/H|=1.4e-3` driver could not be located at main HEAD this turn — likely PR#80-adjacent / unmerged).

### Skip-lists (preserved)

Each lane skipped analytic-only drivers, figure generators, consistency scaffolds, already-retracted verdicts, and unmerged branch-only results. Notable skips: the genesis v5–v15 srs-chiral series (distinct D1 srs-vs-diamond sub-lane, mostly positive/exploratory); the already-HALTed charge-sector two-winding field-route (audit `w1ni1axfg`); the geometric SU(2) holonomy diagnostics (correct achiral null + chiral signal); and the em-readout Stage-0 analytic nulls (unmerged at the time of the F3 sweep — the "dynamic pumping time-averages to zero" null was flagged by the F3 auditor as a **prime future CLASS-2 candidate IF it lands as a global-sum time-domain simulation**). It has since landed (2026-07-03, `2026-07-03_em-readout-stage0_result.md`) — but as an **analytic** kill (VERDICT [STUCK]) that **grounds** the pump-null in Axiom 3: a lossless-reactive linear coupling of an oscillatory source time-averages to zero *by construction* (`:62`, `:75`). So it is a self-aware axiom-derived kill, not an uncontrolled blind readout; the F3 auditor's concern does not fire against the merged form. See §6.

## 5. Disposition and the caveats landed

**This is a STATUS-DEMOTION arc, not a retraction arc.** Conclusions stay; their evidentiary status demotes to under-re-adjudication. **25 LOW rows survive untouched.** The 2 HIGH + 4 MEDIUM rows receive dated caveats (this PR):

**HIGH — the load-bearing pair (dated ⚠ EVIDENTIARY-EXPOSURE blocks appended; original text preserved, git is the trail):**

- **Stage-2 native-cage** (`research/2026-06-24_engine-stage2-native-cage_result.md`) — CLASS-1 nullspace/decoupling (98% N=8 projection) + CLASS-2 mislocated Cartesian control. Status line: *DISPERSE verdict = EVIDENCE-EXPOSED, UNDER RE-ADJUDICATION (native positive control + `L_D` spectral decomposition + srs-z3 re-run pending); conclusion NOT retracted, NOT confirmed.*
- **S3 cavity-pinning** (`research/2026-06-24_engine-s3-cavity-pinning_result.md`) — inherits Stage-2's CLASS-1 (same `L_D` on the A1 block) + CLASS-2, plus its own §5 self-admitted instrument artifact (native vector operator unwinds the integer). Same status line.

**MEDIUM — one short dated note each:**

- **Genesis-24** (`research/2026-06-09_genesis-24-saturated-seed_result.md`, Case C) — grades the residual pump finding. **See §6: the sweep's "residual pump" framing is superseded by the doc's own 2026-06-21 Lenz-sign ADDENDUM.**
- **#415 coupled-eigensolve** (`research/2026-06-24_engine-coupled-eigensolve_result.md`) — stencil note: diamond `L_D` nullspace confirmed by sweep arithmetic; checkerboard in `Grad`-nullspace under any diagonal `D`.
- **#417 phase-space carrier-ratio** (`research/2026-06-24_engine-phase-space-winding_result.md`) — chiral-on-achiral category note (a (2,3) chirality verdict evolved on the achiral diamond host; srs re-run queued). **Also fixes the doc's zero-stencil-acknowledgment gap.**
- **K4-quartic** (`clm-k4d4ph` at `vol4/claim-quality.md`, leaf `k4-bloch-dispersion-quartic.md`) — **existing in-corpus demotion already covers the sweep's finding including the inserted-exponent point; NO register edit.** One stale leaf cite fixed (see §6).

**Claim-spine demotion (the one entry that rides the DISPERSE evidence):** `clm-sjjvhf` (interior-eigenmode Nyquist exemption, `common/claim-quality.md:679`) had its rationale caveat "partially discharged" by the Stage-2 DISPERSE evidence via the additive-corroboration banner at `boundary-observables-m-q-j.md:91`. With that evidence exposed, the discharge is itself under re-adjudication, so `clm-sjjvhf`'s authored confidence demotes (see the PR final message for old→new). **`clm-uatcql` (electron-identification) does NOT demote** — its confidence rests on the Axiom 1–4 per-property audit, not the DISPERSE readout; the electron-identification banner explicitly says the build-on claim STANDS. **mass = A1 (PR#260) untouched** across the entire spine.

## 6. What the claim-trail surfaced that the sweep missed

Two verify-before-cite catches where the corpus state at HEAD is ahead of the sweep's framing:

**(A) Genesis-24: the "residual pump" is already resolved as a sign-artifact.** The sweep row grades a "residual pump finding … plausibly a coupling-routing artifact per `k4_cosserat_coupling.py:242` docstring". But the genesis-24 result doc at HEAD carries a **2026-06-21 Lenz-sign ADDENDUM** (below the CORRECTING HEADER) that already resolved this: the runaway rested on a `+2` EMF sign-wiring bug; the method's own docstring and doc 67_ §13.6 derive `−2` (Lenz back-EMF). Under the corrected `−2` the source is **bounded** (E_V ~12→5, `v_secular<1`, verdict **C1**), NOT a runaway. So the pump is a **confirmed sign-artifact**, not a live residual pump — the sweep's "residual pump" framing is superseded. (The `:242` docstring the sweep cites is now a superseded NOTE at `:260`; the `:703` EMF cite has drifted to the `_compute_emf_per_port` symbol — both line-drifts are already self-flagged in the doc.) The MEDIUM note reflects the ADDENDUM, not the pre-ADDENDUM framing.

**(B) K4-quartic: the stale leaf cite.** The sweep flagged that the leaf `k4-bloch-dispersion-quartic.md:101` says `srs_bloch_dispersion.py` is "on branch `engine/p1b-modes-live` — cited by path, not yet on `main`". **Verified stale:** `srs_bloch_dispersion.py` IS on main (commit `19a31836`, "P1b.3: the band-edge dispersion gate — genuine srs eigensolve gives SLOPE-2"). This PR fixes that one-line stale cite (a factual on-main correction, not a conclusion change).

Neither catch breaks a conclusion; both are corpus-state-ahead-of-sweep corrections landed faithfully.

---

**Cross-references:** the two HIGH result docs (`2026-06-24_engine-stage2-native-cage_result.md`, `2026-06-24_engine-s3-cavity-pinning_result.md`) carry the dated ⚠ EVIDENTIARY-EXPOSURE blocks pointing back to this doc. The re-adjudication arc and the D1 srs-z3 production-carrier ratification are tracked in `_orchestration/index.md`.

## 6. What the claim-trail surfaced that the sweep missed

<!-- filled next commit -->
