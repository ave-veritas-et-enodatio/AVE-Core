# P6-LV — which SECTOR sources the nonlinear-sector Lorentz violation, and does it map to a bounded SME coefficient? (FROZEN PRE-REG)

**Status:** **FROZEN PRE-REG.** Freezes the two-hypothesis sector fork, the discriminators, and the
SME-classification criteria BEFORE the derivation/compute commit (timestamp-ordered: this commit
precedes the driver + result). Does NOT state the answer.
**Date:** 2026-07-08 · **Lane:** implementer.
**Part:** P6 make-or-break, **Part 1** (sector-trace + SME classification). Feeds Part 2 (external
bounds-retrieval) with a one-line LV-framework classification.
**Class (consistency-vs-emergence):** **CONSISTENCY.** Determines the SECTOR OWNERSHIP (A1 vs T2) of
an EXISTING non-covariant kernel and its CLASSIFICATION against an external LV framework (SME). No new
claim-id / constant / axiom. Q=137 stays empty. The 4.9e-3 magnitude rides the external ratio
β = v_CMB/c (settled upstream, PR #574 / p6-frame-boost); it is NOT re-derived or re-claimed here.
**Builds on (does NOT re-open):** `research/2026-07-08_p6-frame-boost-dependence_result.md`
(origin/analysis/p6-frame-boost, PR #579) — established that the kernel argument A = |E|/E_YIELD is a
frame-dependent MAGNITUDE (not the invariant F = B²−E²), the response references the substrate/CMB rest
frame (BULK corner), and the sidereal first-harmonic P_flip amplitude is 4β ≈ 4.94×10⁻³. This pre-reg
takes that result as GIVEN and asks the UPSTREAM sector question it deferred: **in which substrate
sector does the non-covariance actually live, and is that sector one the standard SME photon sector
carries a bounded coefficient for?**
**Driver (to be written AFTER this freeze):** `src/scripts/vol_9_device/p6_lv_sector_classification.py`
**Result (AFTER compute):** `research/2026-07-08_p6-lv-sector-classification_result.md`
**Loci GROUNDED (read-only; NOT edited — auditor/orchestrator integrates):**
`src/ave/bench/birefringence.py:158-224`, `src/ave/core/constants.py:476-506`,
`manuscript/ave-kb/common/substrate-native-terminology.md:52-65`,
`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:18-20`,
`manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md:189,221`,
`papers/2026_birefringence_letter/main.tex:402-432,850-865`.

---

## §0 SUBSTRATE-FIRST SECTOR HEADER (declared before any physics word)

- **SECTOR under analysis:** the object is the Axiom-4 saturation kernel S(A)=√(1−A²) as it drives the
  vacuum birefringence, A = |E|/E_YIELD. Candidate owning sectors (canon, do NOT cross-wire):
  - **A1** = longitudinal dilatation / mass / compression scalar (the Heaviside-excised "3";
    `mₑc²` = trapped acoustic compression energy; `master-equation.md:20`). Its saturation observables
    are the **local clock** ω_local = ω·(1−A²)^¼ (Op14) and the **compliance** C₀/S (↑).
  - **T2** = transverse Cosserat photon (E,B). "The photon **is** transverse … no longitudinal
    component" (`substrate-native-terminology.md:54`). Its saturation observable is the **permittivity**
    ε_eff = ε₀·S (↓) — the birefringence readout.
  - A1 ⊥ T2 (grade-orthogonal); wiring the A1 scalar into the transverse-photon sector is the
    **two-"3"s double-count** (`master-equation.md:20`, `terminology.md:54`). The analysis must respect
    this and NOT cross-wire.
- **REGIME:** deep-cold, WEAK-field, sub-yield (A² ≈ 6×10⁻⁷); the kernel is in its perturbative tail,
  tank NOT ruptured. NOTE the regime discipline: the canonical statement "the longitudinal re-engages at
  saturation = the electron" (`historical-precedents`, `master-equation.md:18`) is a **FULL-saturation**
  (A→1) statement; it does NOT license importing A1-re-engagement into this WEAK-field regime unless the
  discriminators independently place the response there.
- **PHASE-STATE:** the saturating medium (nodes) at rest in substrate/CMB frame; apparatus boosted at β.
- **COORDS (A46):** observable = dimensionless P_flip / δn (matching coordinate); boost acts on the real
  (E,B) 4-tensor. MATCH.

## §1 THE TWO HYPOTHESES (frozen — each with a distinct sector prediction)

- **H_A1 (Grant's mechanism — CONFIRM candidate):** the non-covariance is SOURCED in the A1 /
  longitudinal-dilatation (compression) sector. The transverse |E| is only the DRIVE and the transverse
  birefringence only the READOUT; the response that references a preferred frame (saturation = the
  vacuum compressing toward its yield) is the A1 mode. **Prediction if true:** standard SME photon-sector
  (transverse) LV tests are STRUCTURALLY BLIND to it — it is a scalar/longitudinal object the SME does
  not carry a photon-sector coefficient for.
- **H_T2 (anti-bias — REFUTE candidate, held honestly):** the non-covariance lives ENTIRELY in the
  transverse EM (T2 photon) response — the kernel keys on the transverse magnitude |E| and modulates the
  transverse permittivity ε₀·S; a boosted observer sees an ordinary transverse-sector effect.
  **Prediction if true:** it IS a transverse photon-sector object and is (in principle) constrained by
  the transverse LV framework — potentially SME-bounded.

**Anti-bias directive (frozen):** H_A1 is attractive because it saves the flagship. This pre-reg does
NOT steer to H_A1. The discriminators below are read off the ENGINE + CANON, and whichever way they
land is reported plainly — including the honest bad outcome that the effect is transverse and bounded.

## §2 THE DISCRIMINATORS (frozen — read off engine + canon, sympy where useful)

- **D1 — kernel-argument invariance class.** Is A built from an invariant (F=B²−E², E·B) or a MAGNITUDE
  (|E|)? Read `birefringence.py`. (Settled upstream as MAGNITUDE; re-confirmed here as the sector entry
  point.) Sympy: for a radiation pump both invariants vanish (B=E/c) — so an invariant-keyed kernel is
  zero; the live kernel is a magnitude. This fixes the ENTRY of non-covariance but NOT its sector.
- **D2 — response-channel sector ownership (the load-bearing discriminator).** WHICH reactance does the
  birefringence kernel modulate: the transverse-T2 permittivity ε₀·S (↓), or the longitudinal-A1
  compliance C₀/S (↑)? Read `birefringence.py` (`n=√(ε_eff/ε₀)=√S`, "eps strained, mu=mu0") against the
  canon split `terminology.md:65` / `dual-reactance-storage-taxonomy.md`. Also: the letter's uniaxial
  eigen-permittivities `main.tex:857` (ε₀S "transverse", ε₀(S+2S'E²) "longitudinal") — verify whether
  that "longitudinal" is the **optic-axis orientation** (both T2-photon permittivities) or the **A1
  grade** (do NOT conflate the two senses of "longitudinal").
- **D3 — frame-anchor provenance.** WHAT makes a preferred frame exist at all? Trace E_YIELD in
  `constants.py`: does it chain to `M_E` (the A1 dilatation rest-mass, "rest energy per cell") or to a
  transverse-sector quantity? A massless T2 photon has no rest frame; the rest frame must be anchored by
  something. Report whether the frame-anchor is A1 (rest-mass) or T2.
- **D4 — boost-order projection sense.** β-expand D^p(|E|) for a radiation pump (sympy). Show which
  projection of the boost yields the O(β) first-harmonic (β·k̂, the component ALONG propagation) vs which
  yields O(β²). NOTE: "longitudinal" here = propagation-direction projection — a THIRD, kinematic sense
  of "longitudinal", NOT the A1 grade. Keep the three senses of "longitudinal" separate:
  (i) A1 grade-scalar, (ii) optic-axis-parallel eigen-permittivity, (iii) propagation-parallel boost.
- **D5 — SME field-dependence test.** The minimal SME photon coefficients k_F (CPT-even, d=4) and k_AF
  (CPT-odd, d=3) are CONSTANT background tensors coupling to the LINEAR field strength F² — they are
  field-AMPLITUDE-INDEPENDENT (present at zero field, ∂(coeff)/∂E = 0). Compute the AVE LV coefficient's
  field-dependence: is it ∝ A² (vanishes at E=0, ∂/∂E ≠ 0 — NONLINEAR)? If so it is NOT k_F and NOT
  k_AF, regardless of sector.

## §3 THE ADJUDICATION CRITERION (frozen)

**★ SECTOR VERDICT (D2 ⊕ D3):**
- If the birefringence kernel modulates ε₀·S = **transverse-T2 permittivity** (D2) AND the transverse
  readout is a genuine T2-photon permittivity (not the A1 grade), then the **RESPONSE CHANNEL is T2** →
  Grant's H_A1 is **REFUTED at the response-channel level**. A1 may still enter as the frame-anchor (D3).
- If D2 shows the modulated reactance is the A1 compliance C₀/S, or the response is the A1 clock/
  dilatation, then the **RESPONSE is A1** → H_A1 **CONFIRMED**.
- Report the D3 frame-anchor separately: even under a T2 response, if the preferred frame is anchored by
  the A1 rest-mass (E_YIELD ∝ mₑc²), state that the LV EXISTS-BECAUSE-OF A1 (frame-selector) while the
  RESPONSE lives in T2 — a split verdict, reported as such (flag-don't-fix; do not collapse to one horn
  to protect or to kill the chord).

**SME CLASSIFICATION (D5 ⊕ sector):**
- If D5 shows field-DEPENDENCE (∝ A²): the effect is **NOT** minimal-SME k_F or k_AF (those are linear /
  field-independent). State it as a **NONLINEAR / higher-dimension** photon-sector object.
- Then combine with the sector verdict: (a) if T2-response + nonlinear → a **transverse-photon NONLINEAR**
  object, NOT bounded by existing LINEAR cavity/Michelson/astrophysical-birefringence limits on k_F/k_AF,
  but IN-PRINCIPLE a transverse-sector object a dedicated nonlinear/higher-dimension photon-sector LV
  experiment could bound (hand to Part 2, honest — the escape is nonlinear-vs-linear, not
  longitudinal-invisibility). (b) if A1-response → a **scalar/longitudinal** object the standard SME
  photon sector carries no coefficient for (structurally unconstrained by the photon sector).

## §4 ANTI-TAUTOLOGY / LIVENESS (frozen)

The driver must be able to return EITHER sector. The D2 test reads the ACTUAL modulated reactance from
`birefringence.py` and compares to BOTH canon reactances (ε₀·S and C₀/S); it is rigged if it can only
name one. The D5 field-dependence test must be able to return "field-independent" (which would map to
k_F/k_AF) — planted control: feed a constant (field-independent) coefficient and confirm the test flags
it as k_F-class; feed ∝A² and confirm it flags NONLINEAR. If the discriminators cannot reach both
verdicts the run is void.

## §5 DISCIPLINE CHECKLIST (frozen)

- **ave-canonical-source:** C_0, E_YIELD, V_SNAP, M_E, ALPHA, L_NODE, E_CRIT imported from
  `ave.core.constants`; never hardcoded. `verify_constants()` asserts C_0 CODATA-exact and reproduces
  the E_YIELD→M_E chain and β. v_CMB = 370 km/s tagged EXTERNAL.
- **substrate-native + sector-ownership:** respect A1 ⊥ T2; the two-"3"s double-count is the failure
  mode explicitly guarded. No Lagrangian / gradient-descent / continuum-Helmholtz / energy-basin.
- **phase-space-coordinate-check (A46):** observable in P_flip/δn; boost on real (E,B). MATCH.
- **consistency-vs-emergence:** tagged CONSISTENCY (sector ownership + external-framework classification
  of an existing object; no emergence headline; magnitude rides external β).
- **pure-AVE-corpus:** own re-derivation; the SME is referenced as an established physics FRAMEWORK
  (structural: k_F linear/field-independent, k_AF CPT-odd/dimensionful) — NO external citations, authors,
  or specific experimental bounds (those are Part 2's retrieval). NO business/funding context anywhere.
- **do NOT edit paper / ledger / canon.** Result doc + a clearly-marked PROPOSED INTEGRATION NOTE only.
  NO self-merge — push branch, open PR marked `[REVIEW: pending-orchestrator] … (DO-NOT-MERGE)`.
