# Stage-3 — the Γ=−1 boundary cavity MUTUAL-PINNING test

**Status:** **FROZEN PRE-REG** (orchestrator-finalized; the three forks are RULED in §0). Frozen pre-run; SHA-pin before the run.
**Epic:** full-engine re-route, Stage 3 ("THE CONFINEMENT / MUTUAL-PINNING PAYOFF").
**Date:** 2026-06-24
**Class:** CONSISTENCY (proves the localization MECHANISM). NOT the α-free chord — that is S4. Q=137 stays EMPTY (anti-substitution, Rule 12). mass=A1 (PR#260) is UNTOUCHED by either outcome.
**Working checkout:** AVE-Core @ origin/main `a3a209d2` (S1 #407, S2 #409, docs #410 merged). All citations grep/read-confirmed @ a3a209d2.

## §0 SCOPE-LOCK (read first) — this is THE re-route payoff test; a FALSE result is a DEEPER negative

Stage-2 FALSIFIED the bulk self-trap: a seeded A1 precursor DISPERSES (Mode-III, energy-conservation-certified) on the native tetrahedral K4 stencil — the Cartesian self-trap was a GRID ARTIFACT (`research/2026-06-24_engine-stage2-native-cage_result.md:1-8,57-67`). A1-ALONE does NOT localize.

S3 tests the SANCTIONED successor hypothesis (the slot is NOT silently refilled — anti-substitution, Rule 12): **the now-conserved (2,3) Cosserat winding ω (S1, #407) + the conservative A1↔ω lock H_couple (S2, #409) PINS the dispersing A1 core** — a (2,3) twist cannot unwind and needs a saturated core to live on, so it HOLDS the core bare A1 sheds, with the `|Γ|→1` (μ-load short) boundary cavity at the operating point V_snap.

- **TRUE (pinned):** the electron's localization mechanism is demonstrated as boundary/topological, not bulk self-focus.
- **FALSE (disperses):** a DEEPER negative — the re-route fails at its load-bearing joint. RETRACT, do not refill (Rule 12: preserve body, add 🔴 header citing the falsifying run).

### Forks — RULED (Grant 2026-06-24)
- **FORK Γ-SIGN → sign-agnostic (|Γ|→1).** Substrate-decided/MUTE for the localization question (KB Axiom-4 `manuscript/ave-kb/CLAUDE.md:73` "both |Γ|=1, differing only in boundary phase"; B3 DEGENERATE `research/2026-06-15_wall-branch-fork_result.md:7`). The cavity gate is `|Γ|→1`; we do **NOT** write "reaches −1" as a derived result (the μ-first label is asserted-not-derived, clm-lv3uw1 solidity 0.50).
- **FORK FORMATION-SCOPE → POSITED-PERSISTENCE ONLY (Grant ruled (a)).** S3 seeds an *already-localized* eigen-precursor and asks whether winding + H_couple + cavity HOLDS it. **Formation is DEFERRED** to a separate question — the snap-overshoot / overshoot-rebound-lock / cast-vs-tune / "α-in-the-rupture-ratio" genesis hypothesis (Grant 2026-06-24) is being refute-grounded separately (workflow `wkp3xtzed`) and is explicitly **OUT of S3 scope**. Folding formation in would re-open the leaning-falsified keystone-pump under a new name (substitution-not-retraction) — barred from S3.
- **FORK PDE-HOST → extend `native_cage_imex` (orchestrator/implementer call).** Add the ω DOF + H_couple to the native+α-clean+energy-gated scalar cage (least re-validation; inherits the native stencil + the Stage-2 energy gate directly), rather than repairing the Cartesian/α-contaminated/pump-prone `cosserat_field_3d`.

## §1 MAKE-OR-BREAK (frozen pre-statement)

On a **real-space coupled A1↔ω PDE on the native tetrahedral TETRA_OFFSETS stencil**, seed an already-localized A1 eigen-precursor (POSITED persistence) carrying the S1-conserved (2,3) winding ω, with the S2 conservative skew-Hermitian H_couple A1↔ω lock ENGAGED and the `|Γ|→1` (μ-load short) cavity at V_snap (A²=1 saturation cap):

- **MAKE (pinned):** the A1-core centroid-spread / interior energy-localization holds BOUNDED over the full run — clears the Stage-2 Mode-I PERSIST bar that A1-alone FAILED — energy-conservation-certified on a CLOSED native-stencil box (|rel_drift| ≤ 1e-5, matching Stage-2's −8.77e-6; NO PML, NO damping_gamma), robust across sech AND gaussian seeds.
- **BREAK (disperses):** reproduces Stage-2 Mode-III (interior peak → seed level then sheds below the radiation floor) — winding+H_couple+cavity does NOT pin the core.

**The result is the DELTA** between (coupled, winding ON) and (winding OFF / ω=0 = A1-alone, which MUST reproduce Stage-2 Mode-III as the live negative control). A "pinned" verdict is trustworthy ONLY if (a) the A1-alone control still disperses in this harness, (b) the closed-box energy gate PASSES, (c) the verdict is seed-robust, (d) BOTH the A1-norm AND the ω-winding are separately certified conserved (no genesis-24 bleed). INCONCLUSIVE is a legit landing (Rule 11) if the coupled integrator can't carry a clean verdict — report, do not rescue.

## §2 VALIDATE-ON-KNOWN

- **Known NEGATIVE (the floor to beat):** Stage-2 Mode-III A1-alone dispersal — `FINAL.mode=MODE_III_DISPERSE_FALSIFICATION`, `sech.max_abs_over_run=0.849≈seed(0.85)`, `rel_drift_end=-8.77e-6`, `Q_numerical=2.26e7` (`research/2026-06-24_engine-stage2-native-cage_result.md:57-67`; `results/engine_stage2_native_cage_imex_makeorbreak_results.json`). This is the live in-harness negative control when winding is OFF.
- **Floor (inherited):** S1 winding-DOF conservation (#407); S2 H_couple norm-preserving lock (#409) — NOTE S2 is a C^{2M} on-node chain, NOT a real-space PDE (`src/ave/core/s2_hcouple_gate.py:131-132,164`), so it CANNOT carry this test; the floor is its independence + conservation result, not its machinery.
- **Energy hero + negative controls to port:** GX2 `energy_conservation_gate` (`src/tests/test_stage2_native_cage_imex.py:73-92`); GX3 backward-Euler-bleed-must-fire `assert bleed>0.05` (:96-128); GX5 passive-port `assert Hmax <= H0*(1.0+1e-6)` (:155-177); make-or-break HARD-HALT + gaussian-disperses + Cartesian-v14-self-traps controls (`src/scripts/engine_stage2_native_cage_imex_makeorbreak.py:14-22,180-210`).
- **DO NOT use "the wall reaches −1" as a gate.** The pathway's "≈−0.45 Cartesian clip" (`_orchestration/2026-06-24_engine-reroute-pathway.md:60`) is internally inconsistent — attributed to a Cartesian base-crack AND to the projection-vs-native lane (`research/2026-06-08_alpha-engine-input-adjudication.md:33`) — and a perfectly-reflecting Γ=−1 wall makes Q→∞ (`src/tests/test_graded_vacuum_network_isolation.py:9-26`), so "touching −1" is not a falsifiable pinning observable. The honest known is the Mode-III persistence DELTA, energy-certified.

## §3 TRAPS + GUARDS (the S3 immune system — Stage-2-style fakes)

1. **Damping-bought localization** (top risk; cosserat Γ-clamp pumped 10^4–10^5×, `cosserat_field_3d.py:990-994,2050-2066`). GUARD: closed-box energy gate (GX2) + GX3/GX5 negative controls as HARD-HALT; no PML, no damping_gamma; |rel_drift|≤1e-5 or HALT.
2. **Cartesian-stencil artifact** (the retired bulk self-trap). GUARD: native TETRA_OFFSETS only (`native_cage_imex.py:55-60,77`; Cartesian 7-pt FORBIDDEN, HR1); Cartesian-v14 kept only as a continuum cross-check that MUST self-trap.
3. **PML/boundary-injection** (142× Stage-2; existing L3 waives energy conservation on PML, `src/tests/engine_acceptance/test_l3_mass_cage.py:258-263`). GUARD: closed-box; passive-port monotonicity asserted; reproduce a 142×-class injection control.
4. **2-mode-model fakes localization** (structural — S2 has no real space). GUARD: real-space coupled PDE on the native 3-D stencil; observable in real-space 3-D (A1-core centroid/spread), A46.
5. **Seed-profile dependence** (Stage-2 FLAG-1). GUARD: BOTH sech and gaussian; gaussian disperses + Cartesian-v14 self-traps as live in-harness gates.
6. **HERO-CANARY: A1-alone-must-still-disperse in-harness.** GUARD: demonstrate winding-OFF Mode-III dispersal in the coupled harness, closed-box energy-certified, BEFORE claiming the pin; the result is the delta.
7. **α-contamination on the dynamics path** (cosserat `step()` consumes KAPPA_CHIRAL_ELECTRON=ALPHA·κ̃, `cosserat_field_3d.py:131,:56`). GUARD: extend the `_winding_host` forbidden-name guard (`s2_hcouple_gate.py:598-604`) into the coupled step; keep cosserat off the chord-deciding read unless α-stripped. (V_yield=√α·V_snap is √α-laden, `constants.py:456`; acceptable for CONSISTENCY-class but do not call the result α-clean-absolute.)
8. **Winding bled into the A1 scalar** (genesis-24 collapse fakes a pin). GUARD: §4.

## §4 GENESIS-24 GUARD

ω is its OWN conserved DOF — NEVER ω:=grad(V), NEVER wired into the A1 (V_inc,V_ref) phasor (`cosserat_field_3d.py:241-242` "NEVER wired into the A1 (V_inc, V_ref) phasor. Reads ONLY the holonomy SIGN"). The mechanism is winding-PINS-core (two distinct fields coupled by H_couple), NOT winding-IS-core. A1 (= MASS, the dispersing scalar) and ω (= CHARGE/helicity, the conserved winding) are separately initialized, separately conserved; H_couple (chirality phase χ·θ_χ from lattice handedness, STRUCTURAL, not read off V) is the ONLY coupling. The energy gate certifies BOTH the A1-norm AND the ω-winding — a "pin" cannot be bought by bleeding the winding into the scalar. Reuse the S1 reachable-False slaved-arm discriminator as the in-harness independence control.

## §5 BUILDABILITY

**NEEDS-NEW-COUPLED-PDE** (moderate cost; not from-scratch). The S2 2-mode model is INSUFFICIENT (no real space). Build on FORK-PDE-HOST = extend `native_cage_imex` (native + α-clean + energy-gated scalar A1 cage): (A) co-host the ω DOF + H_couple with the A1-scalar on the native TETRA_OFFSETS stencil; (B) α-strip the dynamics path (extend the `_winding_host` forbidden-name guard into the coupled step); (C) port the closed-box energy gate + GX3/GX5 negative controls onto the COUPLED object under a non-absorbing boundary; (D) real-space 3-D pinning observable with winding-OFF as the live Mode-III control. Do NOT build on the S2 model (vacuous) or on `cosserat_field_3d` unmodified (re-trips α-clean + Cartesian grid + energy pump).

## §6 CONSISTENCY-vs-EMERGENCE

S3 is CONSISTENCY-class: it proves the localization MECHANISM (does winding pin the core), NOT the α-free chord (S4). A green S3 must NOT be characterized as a chord; Q=137 stays EMPTY; mass=A1 (#260) is untouched. The result depends on `ave.core.constants` only through the operating point V_snap (√α-laden) — declared, not hidden.

## §7 REPRODUCE / GATE PLAN

1. **HALT GATE 1 — operator validity:** independent operator-equivalence check on the coupled native stencil. FAIL → HALT.
2. **HALT GATE 2 — energy conservation (the hero):** closed-box `energy_conservation_gate` on the COUPLED object at production N. |rel_drift| ≤ 1e-5. FAIL → HALT (broken instrument).
3. **HALT GATE 3 — negative controls fire:** GX3 backward-Euler bleed >0.05; GX5 passive-port Hmax/H0≤1; A1-alone (winding OFF) reproduces Mode-III dispersal in-harness; gaussian disperses; Cartesian-v14 self-traps. Any control that does NOT behave as pre-stated → HALT.
4. **PRIMARY:** coupled (winding ON) at V_snap, sech + gaussian seeds; real-space 3-D centroid-spread / energy-localization observable; verdict = PERSIST (clears Mode-I bar) vs DISPERSE (Mode-III) as the DELTA vs the winding-OFF control.
5. **ROBUSTNESS:** dt-refinement stability + multi-seed agreement (match Stage-2 `dt_verdict_stable`, `n_robust_agree`).
6. **OUTPUT:** a frozen result doc (`research/2026-06-24_engine-s3-cavity-pinning_result.md`) with the verdict, the energy-certification, both seed runs, the winding-OFF control, and BOTH-conserved (A1-norm + ω-winding) certification. Cite this pre-reg's SHA in the result. Branch-only; NEVER self-merge — Grant merges.
