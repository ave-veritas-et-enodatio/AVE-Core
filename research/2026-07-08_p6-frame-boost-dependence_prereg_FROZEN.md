# P6-FRAME — does the birefringence response reference a preferred frame? (three-corner boost-dependence test)

**Status:** **FROZEN PRE-REG.** Freezes the three corners, the adjudication criterion, and the
anti-tautology liveness controls BEFORE the derivation/compute commit (timestamp-ordered: this commit
precedes the driver + result). Does NOT state the answer.
**Date:** 2026-07-08
**Lane:** implementer.
**Class (consistency-vs-emergence):** **CONSISTENCY.** This determines the Lorentz-transformation
property of an EXISTING kernel argument and the boost-order of an EXISTING observable. It mints NO new
claim-id, NO new constant, touches NO axiom. Q=137 stays empty. The corrected number (if any) rides the
external ratio β = v_CMB/c — NOT an AVE emergence.
**Contention:** P6-frame of the paper-hardening epic (`research/2026-07-08_paper-hardening-ledger.md`,
P6 section, "NEW FORK surfaced — the response frame"). Grant ruling: **"test it"** (autonomous physics test).
**Builds on (does NOT re-open):** PR #574 `analysis/p6-sidereal-boost` settled the ORDER *given the
CMB-frame premise* (radiation Doppler ⇒ O(β), P_flip first-harmonic 4.94e-3, NOT the registered
(v/c)²=1.5e-6). This prereg is the UPSTREAM question that #574 explicitly deferred to Grant: **which
frame does the response reference** — which selects the corner and hence whether the sidereal falsifier
exists at all.
**Driver (to be written AFTER this freeze):** `src/scripts/vol_9_device/p6_frame_boost_dependence.py`
**Result (AFTER compute):** `research/2026-07-08_p6-frame-boost-dependence_result.md`
**Figure (house-WHITE, driver-regenerable):** `src/scripts/vol_9_device/_output/p6_frame_boost_dependence.png`
**Paper loci under audit (do NOT edit here — orchestrator/auditor integrates):**
`papers/2026_birefringence_letter/main.tex:402-432` (the "Frame" subsection),
`papers/2026_birefringence_letter/provenance.md:40-43`.

---

## §0 SUBSTRATE-FIRST SECTOR HEADER (declared before any physics word)

- **SECTOR:** radiative EM (pump–probe) sector — the propagating vacuum EM mode. The pump is a
  transverse propagating plane wave (E ⟂ B, |B| = |E|/c); the observable is the probe's par–perp
  birefringence / flip probability.
- **REGIME:** deep-cold, weak-field (A² ≈ 6e-7), saturation ON but perturbative. The kernel
  S = √(1−A²) is evaluated in its linearized tail; the sub-yield tank is NOT ruptured.
- **PHASE-STATE:** the medium (vacuum nodes) is at rest in the substrate frame; the apparatus (pump
  source, probe, detector) moves through it at β = v/c. The frame-reference of the RESPONSE is exactly
  the unknown under test.
- **COORDS (A46 phase-space-coordinate-check):** the corpus claim is stated in the OBSERVABLE
  (dimensionless flip probability P_flip / index shift Δn). The test measures in the SAME coordinates
  (P_flip, Δn_bir). The boost acts on the EM field 4-tensor (E,B) via the exact Lorentz transform —
  the physically-correct operation, not a lattice-Cartesian proxy. Coordinates MATCH; A46-clean.

## §1 THE LOAD-BEARING ANALYTIC SUB-QUESTION (settle FIRST, before numerics)

Determine how the **kernel argument** A = |E|/E_YIELD transforms under a Lorentz boost β. The kernel is
S(A) = √(1−A²) (Axiom 4; `src/ave/axioms/saturation.py`, `src/ave/axioms/scale_invariant.py:107`,
`src/ave/bench/birefringence.py`). Three possible transformation classes route to three corners:

- **(a) Lorentz INVARIANT** — A built from √|F|, F ≡ B²−E² (Heaviside–Lorentz; the Letter's declared
  convention, `main.tex:306-307,319`) or √(E²−B²c⁻²): A boost-INDEPENDENT ⇒ response covariant ⇒
  **LOCAL corner ⇒ sidereal 0.** ANTI-TEST: for a radiation pump both EM invariants vanish (B=E/c ⇒
  F=0), so an invariant-keyed kernel gives A=0 ⇒ **zero pump birefringence** — which contradicts the
  Letter's central prediction. If this branch is where the kernel lives, the whole pump falsifier is
  self-inconsistent; report that plainly.
- **(b) lab-frame field MAGNITUDE |E|** — frame-DEPENDENT (the Letter states this: "S depends on the
  single quantity |E|², which is not a Lorentz invariant," `main.tex:404-405`). Sub-fork on WHICH
  frame's |E|:
  - (b1) **LAB frame:** the pump is lab-produced with fixed E_lab; boost-independent ⇒ **LOCAL corner
    ⇒ sidereal 0** (`main.tex:404-406`, the Letter's operational statement).
  - (b2) **SUBSTRATE / CMB rest frame:** the saturating nodes are at rest in the substrate frame; they
    respond to the substrate-frame field E_sub = Λ(β)[E_lab], which Doppler-modulates at O(β) ⇒
    **BULK corner ⇒ sidereal O(β)** (`main.tex:420-421`).
- **(c) LATTICE / substrate rest frame via DISCRETENESS** — boost-dependence enters only through the
  discrete node stencil at O((q·ℓ_node)ⁿ) ⇒ **LATTICE corner ⇒ sidereal ∝ (q·ℓ_node)ⁿ·β** (suppressed).

**Adjudication of the sub-question (frozen):** classify the ACTUAL kernel argument by reading the
corpus, NOT by assumption. Report: (i) is A an invariant or a magnitude? (ii) if a magnitude, in which
frame does the saturating medium evaluate it — and what corpus statement fixes that frame? Sympy the
boost of |E|² for a radiation pump to expose the leading β-order.

## §2 THE THREE CORNERS (frozen — each with a distinct sidereal prediction)

| Corner | Kernel reference | Boost-order of P_flip modulation | Sidereal signal |
|---|---|---|---|
| **LOCAL** | covariant invariant, OR lab-frame magnitude | FLAT in β (order → ∞ / null) | **≈ 0** (registered falsifier spurious) |
| **LATTICE** | substrate frame, discreteness-gated | ∝ (q·ℓ_node)ⁿ·β | **suppressed** (report magnitude) |
| **BULK** | substrate/CMB-frame magnitude, continuum | ∝ β at O(1) | **≈ 4.9e-3** (P_flip 1st-harmonic, CMB-phased) |

## §3 THE ADJUDICATION CRITERION (frozen, quantitative)

Boost the birefringence response relative to the lattice by β; sweep |β| (log grid) and direction; fit
the **order** n of the response's boost-dependence via the log-log slope of
|P_flip(β) − P_flip(0)| vs |β| at fixed geometry:

- **n → 0 / flat (slope ≈ 0, amplitude at the float floor):** LOCAL → sidereal ≈ 0 → **[SIDEREAL-NULL]**.
- **slope ≈ 1 but amplitude scaled by (q·ℓ_node)ⁿ:** LATTICE → **[SIDEREAL-SUPPRESSED]** (report the
  suppression factor and absolute magnitude).
- **slope ≈ 1 at O(1) amplitude (few×10⁻³):** BULK → **[SIDEREAL-REAL]** → note the strong-LV caveat.

Numeric bands (frozen, from the β = v_CMB/c = 1.234e-3 external ratio): BULK ⇒ P_flip 1st-harmonic
amplitude 4β ≈ 4.94e-3, δn_bir 1st-harmonic 2β ≈ 2.47e-3, 2nd-harmonic 5β² ≈ 7.6e-6 (these MUST
reproduce PR #574's numbers under the CMB-frame config, as a cross-check, not a new claim).

## §4 ANTI-TAUTOLOGY / LIVENESS CONTROLS (frozen — the harness MUST reach ALL THREE bins)

The harness implements the kernel's frame-reference as a CONFIGURABLE `response_frame` and boosts the
REAL EM field 4-tensor. It is rigged if it can only produce one bin. Required liveness:

1. **`response_frame="invariant"` (covariant control):** key the kernel on √|F|. MUST return a
   FLAT-in-β response → LOCAL bin. For the radiation pump this ALSO returns zero birefringence
   (the anti-test of §1a).
2. **`response_frame="lab"` (LOCAL control):** key on E_lab (boost-independent). MUST return FLAT in β
   → LOCAL bin, nonzero birefringence.
3. **`response_frame="substrate"` (BULK control):** key on |Λ(β)E_lab| (substrate-boosted). MUST return
   slope ≈ 1, amplitude ≈ 4β for P_flip → BULK bin.
4. **`response_frame="lattice"` (LATTICE control):** substrate-boost gated by (q·ℓ_node)ⁿ. MUST return
   slope ≈ 1 with amplitude scaled by (q·ℓ_node)ⁿ → LATTICE bin.

A planted-order guard (feed a known n, recover n) confirms the slope-reader is not floored. If any bin
is unreachable the harness is rigged and the run is void.

## §5 THE PHYSICAL DETERMINATION (what selects the corner — frozen method, not answer)

The corner AVE actually sits in is fixed by the corpus, not by the harness (the harness only proves the
corners are distinguishable + reachable). The determination reads:
- the kernel-argument class (§1: invariant vs magnitude — from `saturation.py` / `bench/birefringence.py`
  / `main.tex:404-405`);
- whether the saturating medium has a rest frame the response references (corpus:
  `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md`
  — the substrate has a CMB rest frame, and it is DETECTABLE in principle, §1 there);
- whether the emergent-Lorentz (q·ℓ_node)⁴ suppression (same leaf, §2) is the RIGHT channel for the
  pump boost-Doppler (it protects LINEAR-dispersion rotational anisotropy; the boost-Doppler of a
  nonlinear pump amplitude is a distinct, continuum, O(1)-in-(q·ℓ) channel — check whether it applies).

## §6 HONEST PRIORS (declared before the run, per the task brief)

- **LOCAL is a strong prior** from AVE's EE-native structure (Z₀, c, ε₀, μ₀ are the vacuum constants ⇒
  Maxwell ⇒ Lorentz-covariant at leading order). If the kernel is manifestly covariant, the honest
  verdict is sidereal 0 and the third falsifier is spurious. This prereg does NOT steer away from LOCAL.
- **BUT** the LOCAL-via-covariance route (1a) is in tension with the pump prediction itself (invariant
  vanishes for radiation ⇒ zero pump birefringence). If the kernel keys on |E|² (as the Letter states),
  covariance is already broken in the nonlinear sector, and the live fork is LOCAL-via-lab-lock (b1, 0)
  vs BULK-via-substrate (b2, O(β)). That fork is a substrate-physics question, adjudicated in §5.
- Flag-don't-fix: the Letter internally contradicts itself (`main.tex:404` lab → 0 vs `main.tex:420`
  CMB → O(β)). This is surfaced, both loci quoted verbatim; not silently reframed.

## §7 DISCIPLINE CHECKLIST (frozen)

- ave-canonical-source: C_0, E_YIELD, E_CRIT, L_NODE imported from `ave.core.constants`; never
  hardcoded. v_CMB = 370 km/s is an EXTERNAL astrophysical input, tagged. `verify_constants()` asserts
  C_0 CODATA-exact and reproduces β and β².
- substrate-native: the boost is a real Lorentz transform of the EM field (E,B) of the substrate mode;
  the kernel is the Axiom-4 saturation kernel. No Lagrangian, no gradient-descent, no continuum-Helmholtz.
- phase-space-coordinate-check (A46): observable measured in P_flip/Δn coordinates; boost on (E,B). MATCH.
- pure-AVE-corpus: our own re-derivation; NO external attribution anywhere.
- do NOT edit paper / ledger / canon. Result doc + proposed integration note only. NO self-merge.
