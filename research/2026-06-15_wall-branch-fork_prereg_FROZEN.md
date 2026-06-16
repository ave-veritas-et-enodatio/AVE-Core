# PREREG (FROZEN) — Wall-Branch Fork (H3): magnetic vs capacitive Γ=−1 wall

**Status:** FROZEN 2026-06-15 (Rule 11). Lane: `analysis/2026-06-15-wall-branch-fork`. Orchestration: [`_orchestration/2026-06-15_wall-branch-fork.md`](../_orchestration/2026-06-15_wall-branch-fork.md). **This is an ADJUDICATION of an already-open corpus flag (FLAG-2), not a green-field experiment.**

---

## 1. Question

Which saturation branch forms the electron's Γ=−1 confining wall — **MAGNETIC** (B saturates μ_eff→0 → Z=√(μ_eff/ε₀)→0; `master-equation.md`:85, clm-lv3uw1) or **CAPACITIVE** (the topological twist drives C_eff→∞ → Z_core=√(μ₀/C_eff)→0; `resonant-lc-solitons.md`:29-46, clm-kezk9z)? Distinguish from the reserved third config (ε-rupture → Z→∞, `master-equation.md`:84, the anti-confinement/photon branch). If degenerate/co-saturating → report it.

## 2. Pre-registered expectation (committed `945acb66` BEFORE the Phase-1 corpus-map workflow)

> Working thesis (charter §2, verbatim from the pre-workflow commit): "the magnetic-vs-capacitive *impedance* fork is not an independent physical branch — degenerate on equilibrium observables, the Z-sign is gauge, and the genuine physical content is the A1-vs-T2 sector question. INVARIANT-S2's static-field loading rule leans **A1/capacitive**; clm-lv3uw1 asserts **magnetic/T2 PRIMARY**."

**Pre-registered discriminator axes** (charter §4): (1) formation-order — which reactance kernel hits argument=1 first as a soliton forms; (2) energy-sector / static-loading analytical argument; (3) gauge-vs-physical test of the Z↔1/Z, Γ-sign pair.

**Honest scoring of the pre-thesis against the frozen evidence (Phase 1):**
- ✅ CONFIRMED: degeneracy on equilibrium observables; relocation to the A1-vs-T2 axis as the genuine content.
- ❌ REFUTED: the "static-loading leans capacitive/A1" prediction. The ε-only static-asymmetric state is the Z→∞ **rupture** branch (`master-equation.md`:84), NOT confinement; the soliton is a *ringing* LC tank (∂B/∂t present, `resonant-lc-solitons.md`:23), so the "no ∂B/∂t" static premise fails. (verify:static-loading-rule, refuted-reconciled, high.)
- ◑ REFINED: the "Z-sign is gauge" leg is PARTIAL. The Möbius Z↔1/Z map is rigorous but applies to the INSIDE(Z→0,Γ−1)/OUTSIDE(Z→∞,Γ+1) axis — which is ORTHOGONAL to the μ-vs-C route axis (both μ→0 and C→∞ give the SAME inside Z→0). The gauge argument does NOT dissolve the formation-order residue.

## 3. Discriminator — bins (frozen)

The equilibrium-Z discriminator is dead (degenerate, both → Z₀√S; corpus + code confirmed). The live discriminator is **formation-order at the symmetric substrate level + chirality dependence**, adjudicated as:

| Bin | Condition | Verdict on the fork |
|---|---|---|
| **B1 MAGNETIC** | μ-sector kernel reaches argument=1 first, substrate-forced (not chirality-set), independent of sign convention | magnetic branch is the wall; T2/charge-winding builds it |
| **B2 CAPACITIVE** | ε-sector kernel reaches argument=1 first, substrate-forced | capacitive branch is the wall; A1/dilatation builds it |
| **B3 DEGENERATE (symmetric co-saturation)** | at K=2G trace-free, ε and μ saturate at the SAME A; asymmetry needs a chirality bias; which-sector = chirality-set SIGN (spin), not a substrate-forced branch | fork is not an independent branch; report degeneracy + chirality-sign |
| **B4 GAUGE-ONLY** | the μ↔C distinction is fully the Möbius inside/outside frame of one wall, no physical residue | fork dissolves entirely into gauge |

## 4. Pre-registered falsifiers (what would move the verdict OFF B3)

- **F1 (→B1/B2):** a from-first-principles derivation showing the substrate FORCES one sector to saturate first *independent of an imposed chirality-sign convention* (i.e. not baked into a (1±κh) sign). Corpus status: ABSENT — clm-lv3uw1 is "asserted-not-derived" (0.50/0.32); clm-5fu303 "which sector saturates preferentially" is asserted-not-derived (0.45).
- **F2 (→B1/B2):** an engine observer that records the temporal first-cross of S_μ vs S_ε on a forming soliton WITHOUT the answer being an input. Corpus status: ABSENT — `crystal_engine` is single-kernel (degenerate); `k4_cosserat_coupling` bakes μ-first into the sign; no first-cross observer exists.
- **F3 (→B4):** a proof the trace-free lock makes ε,μ identical at ALL A (not just the symmetric point) so no formation-order residue exists. Corpus status: the residue survives (mutually-exclusive self-terminating branches, `dual-reactance-storage-taxonomy.md`:171-173; preferential-saturation axis, clm-5fu303).

## 5. Expected verdict (pre-committed, pending auditor-gate)

**B3 DEGENERATE** — co-saturation at the symmetric substrate level (trace-free K=2G lock), the magnetic-vs-capacitive label a chirality-set SIGN/spin selector, "magnetic PRIMARY" an asserted labeling convention not a derivation. Knock-on: mass=A1 settled by ontology; wall co-built; the fork does NOT independently decide which "3" carries the mass.

## 6. Method (the "driver" is the corpus-map + adversarial-verification workflow, already run)

This is an adjudication of existing corpus, so the discriminating evidence is the Phase-1 corpus-map workflow (`wf_c8a6cb2d-a99`): 6 corpus-grep readers + 1 engine-reality reader + 3 adversarial auditors, all verbatim-grounded. **No fresh engine driver is run** — justified: an engine instrumentation would reconstruct an already-degenerate (crystal_engine single-kernel) or assumption-baked (Cosserat (1±κh) sign) path (substrate-native-check CP9; pre-test-physics-check Trigger 7/8). That non-instrumentability is itself a reported finding.

## 7. MODE / REGIME / PHASE-STATE (ave-regime-phase-state-check)

MODE: longitudinal-bulk dielectric (ε/A1/X_C) + microrotational inductive (μ/T2/X_L) saturation at the soliton wall; observable = boundary impedance (Op17-bounded BC, not a bulk term). REGIME: near-yield/saturating (S→0), formation-transient + formed-operating-point sub-regimes distinct. PHASE-STATE: forming→formed bound resonator (Q_e=1/α at the operating point).

---

**FREEZE.** No edits below this line after the freeze commit; amendments per Rule 12 in a dated addendum.

---

## Rule-12 amendment addendum (2026-06-15, post-auditor-gate)

Auditor-gate (ave-auditor, independent): **PASS-WITH-AMENDMENTS** — verdict **B3 DEGENERATE confirmed**; falsifiers F1/F2/F3 ABSENT/surviving as predicted. Precision fixes (do NOT alter the frozen body; recorded here):
- **A3:** wherever §2/§4 write clm-lv3uw1 as "0.50/0.32," read it as **confidence 0.65 / solidity 0.50 / rest-mass-mechanism 0.32**.
- **A4:** the K=2G co-saturation lock (§3 B3) is **operating-point-true, not axiom-forced** (K=2G is a downstream consistency the lattice sits at given α; `dual-reactance-storage-taxonomy.md`:62-67).
- **A6:** the `cvr_model.py:144` quote ("SAME trajectory…") is at **:146**.
Full result + flag-don't-fix to Grant: [`2026-06-15_wall-branch-fork_result.md`](2026-06-15_wall-branch-fork_result.md).
