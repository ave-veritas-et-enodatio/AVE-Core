# PREREG (FROZEN) — C_eff↑ vs ε_eff↓ inverse-monotonicity root (INVARIANT-S2)

**Date:** 2026-06-15 · **Lane:** [`_orchestration/2026-06-15_ceff-epsilon-monotonicity.md`](../_orchestration/2026-06-15_ceff-epsilon-monotonicity.md) · **Branch:** `analysis/2026-06-15-ceff-epsilon-monotonicity`
**Rule-11 FREEZE:** verdict bins + discriminator below are frozen at authoring. Post-freeze changes append a Rule-12 amendment; they do not edit the frozen text.

## Question

Is the Axiom-4 dielectric specialization `C_eff = C_0/S` (↑∞ as A→A_yield) vs `ε_eff = ε_0·S` (↓0) — **inverse monotonicity** — physically intended, or is one a sign error?

## Corpus inventory (ave-prereg grounding — all grep-verified 2026-06-15)

- INVARIANT-S2 carries the pair: `CLAUDE.md:58` + `:60` (small-signal modulation paragraph).
- `C_0/S` (diverging) home: `nonlinear-vacuum-capacitance.md:21` (clm-vjv4zf, clm-8nkvwy); echoed `resonant-lc-solitons.md:32`, `master-equation.md:69`, `entry-point.md:29`, `dm-mechanism-unification.md:98`.
- `C_0·S` (rolling off, **opposite sign**) home: `vol4/simulation/index.md:24`, `ch15-autoresonant-breakdown/index.md:17`, `ch17-hardware-netlists/index.md:19` (EE-bench / SPICE / autoresonant).
- Z-direction contradiction: `resonant-lc-solitons.md:35-39` (electric C↑ → Z→0 short, confinement) **vs** `master-equation.md:84-85` + `dual-reactance-storage-taxonomy.md:195-196` (electric ε↓ → Z→∞ open, rupture; confinement = magnetic μ↓ branch, clm-lv3uw1).
- Pre-existing flag: `cvr-dc-operating-point.md:55-57` (AUDITOR_STATE FLAG-2) — sector attribution open, "magnetic PRIMARY," C↑/ε↓ called a "convention" made moot by convention-independent Z₀√S. Deferred, not resolved.
- Engine: `src/ave/topological/cosserat_field_3d.py:402-540` implements asymmetric two-track `S_μ/S_ε`, `Z_eff=Z_0√(S_μ/S_ε)`, varactor `C_eff(V)=C_0/√(1−(V/V_yield)²)` (`:411`) + varinductor `L_eff(I)=L_0/√(1−(I/I_max)²)` in the docstring.

## What I expect, why, what discriminates

**Expectation (pre-adjudication):** the inverse pair is intended at the *symbol* level but rests on an unadjudicated synonym — "compliance (capacitance)" (`nonlinear-vacuum-capacitance.md:14`). The constitutive derivation will show small-signal C and ε of one fixed-geometry cell MUST co-move, so `C_0/S` and `ε_0·S` cannot both be the same cell's small-signal response. Survives only as (B) different objects or (A) sign error.

**Why:** `C = ε·A_area/d` binds C and ε by geometry; the kernel acts on the *constitutive law*, and both incremental responses inherit its sign. ε and μ both ×S (moduli soften); C_eff alone ÷S marks it as a reciprocal (compliance) quantity — which is either a genuinely distinct DOF (1/k) or a misplaced reciprocal.

**Discriminator (FROZEN):** does `C_eff` denote the **same** electric DOF as `ε_eff`, or a **different** DOF?
- **same-object** → C must co-move with ε → `C_0/S` is a **sign error** → fix to `C_0·S` (the bench form).
- **different-objects** (longitudinal bond compliance 1/k vs transverse permittivity) → both correct → the Z→0/Z→∞ split is a **name-collision** → document, don't fix.

## Verdict bins (FROZEN — every adjudication outcome resolves to exactly one)

- **BIN-SIGN-ERROR** — `C_eff` is the dielectric capacitance εA/d (same DOF as ε). `C_0/S` is wrong; canonical = `C_0·S`. Electric sector → Z→∞ rupture only; magnetic branch is the sole confiner; `resonant-lc-solitons` electric-confinement is deleted/rerouted.
- **BIN-NAME-COLLISION** — `C_eff`=`C_0/S` is the longitudinal bond compliance 1/k (distinct DOF); `ε_eff`=`ε_0·S` is the transverse permittivity. Both correct. Z→0 (tank √(L/C)) and Z→∞ (wave √(μ/ε)) are different reactances; both |Γ|=1. Action = rename C_eff "compliance" corpus-wide + document the collision; reconcile bench `C_0·S` as the *dielectric* C.
- **BIN-GEOMETRY-COMOVE** — `C_eff`=`C_0/S` is the same dielectric DOF but geometry (effective gap d) collapses faster than ε drops, so C=εA/d rises while ε falls. Both correct, same object, no name-collision; requires a derived d(S) law (currently absent).
- **BIN-ALREADY-RESOLVED** — auditor finds a canonical leaf that already adjudicates this (would retire the lane). [Pre-registered escape hatch; none found in author's grep.]

## Falsifiers (each must resolve to a bin)

- **F1:** a constitutive `Q(V)` law in the corpus from which `C_0/S` is *derived* (not asserted) as a small-signal capacitance co-existing with `ε_0·S` → would support BIN-GEOMETRY-COMOVE or refute the "co-move" derivation. (Author's grep: none found; `C_0/S` is asserted.)
- **F2:** a canonical statement that `C_eff` is the elastic-bond compliance 1/k *and not* εA/d → BIN-NAME-COLLISION. (Partial hits: `resonant-lc-solitons.md:12` C_e≡ξ²/k; the "compliance" naming is uniform but co-exists with "capacitance.")
- **F3:** the bench/sim `C_0·S` leaves being a *recompute-corrected* form that supersedes `C_0/S` → BIN-SIGN-ERROR with the corpus already half-fixed. (ch15 theory.md already carries an INVALIDATED banner — but for the V_yield=60kV error, not the sign.)
- **F4:** an existing adjudication leaf → BIN-ALREADY-RESOLVED.

## Method

Pure analytical/constitutive derivation + corpus consistency audit. No new sim required (engine forms already grep-verified). EE-native lens (varactor / compliance / permittivity). Auditor-gate before Grant adjudication.

## Out of scope (flag-don't-fix)

No corpus edit, no sign flip, no INVARIANT-S2 change in this lane. Ontology = Grant's call; propagation = separate gated implementor session.

---

## Rule-12 AMENDMENT (2026-06-15, post auditor-gate — bins/discriminator UNCHANGED)

The auditor-gate (read-only ave-auditor) verified all six load-bearing citations and the Lemma, confirmed flag-don't-fix clean, and surfaced three inventory enrichments that **reinforce the existing bins** (no bin/discriminator edit):
- **F-A:** the ÷S/×S sign discrepancy lives under ONE adjudicated claim — `clm-vjv4zf` rules `C_0/S` canonical yet its Leaf-references footer (`vol4/claim-quality.md:82`) cites both `ee-bench-netlist` (×S) and `spice-subcircuit` (÷S). Sharpens F1/F3 evidence; reinforces BIN-SIGN-ERROR / BIN-NAME-COLLISION contention.
- **F-B:** the ÷S/×S split is RAGGED across all layers (not theory-vs-bench): ÷S also in `spice-subcircuit.md:26`, `dielectric-plateau-prediction.md:27`, `ee-bench-plateau.md:18`, engine `cosserat_field_3d.py:411`; ×S in `ee-bench-netlist.md:15` + ch15/17/sim-index rollups. Corrects the inventory's clean-partition framing.
- **F-C (Q1 hinge):** `topological-kinematics.md:81-89` gives `C=ξ²/k` (⟶ BIN-NAME-COLLISION) and welds compliance-yield to dielectric-breakdown (⟶ BIN-SIGN-ERROR). New falsifier **F5:** if Grant rules the `topological-kinematics.md:89` weld binding, BIN-SIGN-ERROR (the two are one object); if he rules it a restated collision, BIN-NAME-COLLISION.
