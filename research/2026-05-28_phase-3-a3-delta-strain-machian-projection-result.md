[↑ Research](index.md)

# Phase 3-A3 Result — WALK-BACK: δ_strain Machian-G Projection Derivation Inconsistent With Canonical clm-3zz0f6 SYM-Class α-Invariance

**Branch**: `analysis/phase-3-a3-delta-strain-machian-projection`
**Prework brief**: [`_orchestration/2026-05-28_phase-3-a3-prework.md`](../_orchestration/2026-05-28_phase-3-a3-prework.md)
**Prereg**: [`2026-05-28_phase-3-a3-delta-strain-machian-projection-prereg.md`](./2026-05-28_phase-3-a3-delta-strain-machian-projection-prereg.md)
**Date**: 2026-05-27
**Outcome**: **WALK-BACK** per prereg adjudication criteria. Substrate-thermodynamic-mapping derivation of δ_strain via Machian-G operating-point cascade cannot close from canonical content. Q-DELTA-MAP-1 framework-extension question logged. Type B walk-back of SM-leaked language proceeds independently. clm-009nkt confidence STAYS at 0.45.

## §1 — Executive summary

Phase 3-A3 prework brief proposed deriving δ_strain ≈ 2.225×10⁻⁶ from a Machian-G operating-point cascade: cosmic-substrate operating point u_0* ≈ 0.187 → substrate amplitude loading A_0^cosmic/A_yield ≈ 1.72×10⁻³ → Ax 4 saturation kernel response S(A_0^cosmic) → INVARIANT-S2 SYM scaling → α_eff/α_cold = 1/S^(3/2) → δ_strain = (3/2)(1−S).

Step 3.5 substrate-thermodynamic-mapping audit identified that this derivation chain has a substantive substrate-physics inconsistency with canonical content `vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md` (clm-3zz0f6, confidence/solidity 0.85): **SYM-class scaling produces α exactly invariant, not modulated**. The prework-brief substitution `α_eff/α_cold = 1/S^(3/2)` uses c_shear (group/rest-mass velocity) where c_EM (phase velocity) belongs — exactly the misreading that LIVING_REFERENCE.md Pitfall #5 flags as the canonical framework-leakage error.

The canonical saturation-class taxonomy (SYM mass-energy loading + ASYM strong-EM loading per clm-8nkvwy) does not yet include a third class for low-amplitude electromagnetic thermal-bath loading (CMB at 2.725 K). Phase 3-A3 logs this as framework-extension question Q-DELTA-MAP-1 with three candidate substrate-physics paths P1/P2/P3. Closing Q-DELTA-MAP-1 requires substrate-physics derivation work absent from canonical content as of 2026-05-27 and requires Grant adjudication on substrate-mechanism direction.

The Type B walk-back of SM-leaked "G_vac + equipartition" + "thermal expansion" language proceeds independently. It substitutes SM-vocabulary open-derivation pointers with substrate-native open-derivation pointers (Q-DELTA-MAP-1) without asserting closure of the substrate-physics question. clm-009nkt confidence STAYS at 0.45 (vocabulary-cleanup-only walk-back does not lift derivation-class evidence).

## §2 — Step 3.5 audit findings (substantive substrate-physics)

### §2.1 — The prework brief's proposed derivation chain

Per `_orchestration/2026-05-28_phase-3-a3-prework.md:10-19`:

1. Cosmic-genesis substrate operating-point u_0* ≈ 0.187 (canonical at `common/omega-freeze-cosmic-grain-cascade.md:13-16`)
2. Substrate operating-point mapping u_0* → A_0^cosmic/A_yield ≈ 1.72×10⁻³ (OPEN substrate-thermodynamic step)
3. Ax 4 saturation-kernel response S(A_0^cosmic) ≈ 1 − 1.483×10⁻⁶
4. INVARIANT-S2 SYM scaling: ε_eff = ε_0 S, μ_eff = μ_0 S, c_eff = c_0√S
5. α modulation: α_eff/α_cold = 1/S^(3/2)
6. δ_strain identification: δ_strain ≡ −δα⁻¹/α⁻¹ = (3/2)(1−S) ≈ 2.225×10⁻⁶

### §2.2 — Canonical clm-3zz0f6 SYM-class α-invariance derivation

Per `vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md:15-22` (verbatim):

> "Under Symmetric Gravity, both constitutive parameters scale by the same factor n·S (including Axiom 4 saturation). The fine-structure constant is therefore *exactly invariant* under gravitational strain:
>
> α = e² / (4π ε_local ℏ c_local) = e² / (4π (ε_0 nS) ℏ (c_0/(nS))) = e² / (4π ε_0 ℏ c_0) = α_0
>
> Multi-species clock comparisons at different gravitational potentials predict a **null result** for Δα/α, consistent with all current experimental bounds."

This derivation gives α exactly invariant under SYM scaling: the n·S factor on ε is cancelled by the 1/(n·S) factor on c_EM. The leaf is cited from `common/claim-quality.md:134-165` (clm-3zz0f6, confidence/solidity 0.85, leaf at canonical KB cross-cutting register).

### §2.3 — The category error

The corpus distinguishes two velocities under SYM saturation (canonical at `common/claim-quality.md:111-113`, clm-8nkvwy):

- **SYM EM phase velocity**: c_EM,sym = c_0/S (the velocity at which electromagnetic phase travels through the saturated medium; appears in α = e²/(4π ε ℏ c_EM))
- **SYM shear velocity**: c_shear,sym = c_0·√S (the "wave-packet freezes / rest mass" group velocity; appears in mass-energy expressions, NOT in α)

The CLAUDE.md INVARIANT-S2 statement (line 60) reads:

> "Small-signal transverse propagation through a region at operating point A_0 sees modulated effective parameters ε_eff = ε_0 S(A_0), μ_eff = μ_0 S(A_0), C_eff = C_0/S(A_0), **c_eff = c_0√S(A_0)** — the same varactor-bias mechanism producing refractive-index gradients across all scales."

The CLAUDE.md "c_eff = c_0√S" reading without phase-vs-group disambiguation suggests substituting c_shear into α — which IS the prework brief's step 5 substitution. But per clm-3zz0f6 + clm-8nkvwy, the EM phase velocity that appears in α is c_EM = c_0/S, NOT c_shear = c_0√S. Substituting the correct c_EM gives α invariance, exactly per the canonical clm-3zz0f6 derivation.

LIVING_REFERENCE.md Pitfall #5 (cross-cutting `common/claim-quality.md:147`) explicitly warns: *"any framework summary suggesting 'AVE predicts multi-species Δα/α from gravity' is wrong."* The prework brief's `α_eff/α_cold = 1/S^(3/2)` derivation produces exactly such an α-modulation-from-substrate-SYM-scaling result, which IS the canonical framework-leakage error.

### §2.4 — Numerical check on the prework brief's claim

If we proceed with the prework brief's substitution (c_eff = c_0√S into α):

$$\alpha_{\text{eff}}^{\text{(brief)}} = \frac{e^2}{4\pi (\varepsilon_0 S) \hbar (c_0 \sqrt{S})} = \frac{\alpha_0}{S^{3/2}}$$

For δ_strain = (3/2)(1−S) ≈ 2.225×10⁻⁶: S ≈ 1 − 1.483×10⁻⁶; (A/A_yield)² ≈ 2(1−S) ≈ 2.967×10⁻⁶; A/A_yield ≈ 1.72×10⁻³. Brief's pre-frozen target matches.

If we proceed with the canonical clm-3zz0f6 SYM substitution (c_EM = c_0/S into α):

$$\alpha_{\text{SYM,canonical}} = \frac{e^2}{4\pi (\varepsilon_0 S) \hbar (c_0/S)} = \frac{e^2}{4\pi \varepsilon_0 \hbar c_0} = \alpha_0$$

**α is invariant.** No δ_strain emerges from SYM scaling at all. This is the canonical content's derivation result, and it contradicts the prework brief's existence of an α modulation.

If we proceed with the ASYM substitution (c_EM = c_0/√S into α, with only ε scaling):

$$\alpha_{\text{ASYM}} = \frac{e^2}{4\pi (\varepsilon_0 S) \hbar (c_0/\sqrt{S})} = \frac{\alpha_0}{\sqrt{S}}$$

For δ_strain = (1−S)/2 (single-power coefficient) ≈ 2.225×10⁻⁶: S ≈ 1 − 4.45×10⁻⁶; (A/A_yield)² ≈ 8.9×10⁻⁶; A/A_yield ≈ 2.98×10⁻³ — **factor √3 different from the prework brief's 1.72×10⁻³**. But ASYM applies to "strong EM field" loading per clm-8nkvwy:112, not low-amplitude thermal-photon-bath loading.

### §2.5 — The canonical narrative IS substrate-spatial-metric strain — but NOT SYM scaling

Per `vol1/ch8-alpha-golden-torus.md:161`:

> "Substrate-mechanism content: this is the thermal expansion of the substrate's spatial metric at the current cosmological epoch (T_CMB ≈ 2.725 K), bridging the substrate's T → 0 asymptote to the measured value at finite T."

The canonical narrative says δ_strain IS substrate spatial-metric strain — but the corpus does NOT yet derive this from any of the canonical saturation classes (SYM or ASYM). Per clm-3zz0f6:147 explicit non-claim: the δ_strain mechanism is "**CMB-induced spatial metric expansion, NOT a gravitational effect**" — distinct from the SYM-class gravitational scaling.

The corpus simultaneously asserts:
- (A) δ_strain ≈ 2.225×10⁻⁶ IS thermal expansion of the substrate spatial metric at T_CMB
- (B) SYM scaling produces α invariance (clm-3zz0f6)
- (C) The mechanism is NOT a gravitational effect (clm-3zz0f6:147)
- (D) The substrate-physics derivation of δ_strain magnitude is OPEN (clm-5xon03 strengthen-by; clm-009nkt confidence 0.45)

(A) + (B) + (C) + (D) together say: the substrate-physics mechanism is real, it's NOT SYM scaling, NOT a gravitational effect, and not yet derived. The open question is what substrate-mechanism class IT IS.

## §3 — Q-DELTA-MAP-1 framework-extension question

**Q-DELTA-MAP-1 (NEW 2026-05-28)**: What substrate saturation class does low-amplitude electromagnetic thermal-bath loading fall into?

Three candidate substrate-physics paths (requires Grant adjudication; documented for orchestration session):

- **(P1)** New saturation class **ELECTROMAGNETIC-THERMAL-BATH** (third class beyond SYM/ASYM). Substrate response to a thermal bath of low-amplitude photons distinct from both SYM (mass-energy loading) and ASYM (strong-EM loading). New scaling rule for ε, μ, c. Closing P1 requires axiom-grounded derivation of the third-class scaling from Ax 4 saturation kernel + Ax 1 substrate topology — substantive substrate-mechanism work.
- **(P2)** ASYM IS the right class but applies at the **time-averaged thermal-bath amplitude** rather than per-photon. Reanalyse ASYM with `A` interpreted as the equilibrium thermal-bath substrate amplitude `⟨A²_{thermal}⟩ ~ k_B T_CMB / (ε_0 ℓ_node³ E_yield)` or similar. Closing P2 requires deriving the cosmological-thermodynamic-equilibrium substrate amplitude from u_0* + cosmic-genesis-thermodynamics — substrate-thermodynamic derivation work. Numerical evaluation: for k_B T_CMB ≈ 3.76×10⁻²³ J, ε_0 ℓ_node³ ≈ 8.85×10⁻¹² × (3.86×10⁻¹³)³ ≈ 5.1×10⁻⁴⁹ J·m, gives `⟨A²⟩ / (E_yield/V)` ~ 7×10⁻²⁶ — orders of magnitude away from the required 8.9×10⁻⁶. The naive thermal-bath amplitude is way too small to produce the δ_strain magnitude via ASYM, suggesting P2 also fails by orders-of-magnitude unless the substrate-thermodynamic coupling is more efficient than naive equipartition.
- **(P3)** δ_strain is NOT a substrate-saturation-kernel modulation at all; it's a **cosmic-substrate-bond rest-length thermal contraction** independent of the Ax 4 saturation kernel. The substrate spatial metric (bond rest length L_spring) is itself a thermodynamic equilibrium parameter; T_CMB enters via the substrate's Cosserat bond-network thermal-equilibrium statistical mechanics, NOT via the saturation kernel S(A). Distinct substrate-mechanism class. Closes the canonical narrative literally (`vol1/ch8-alpha-golden-torus.md:161` says "thermal expansion of the substrate's spatial metric" — bond rest-length contraction at T_CMB IS a direct reading). But: requires substrate-statistical-mechanics derivation that produces δ_strain magnitude — not present in canonical content; substantive substrate-thermodynamic-mapping work.

**Naive numerical check on P3**: standard solid-thermal-expansion coefficient β at T_CMB scales as ~(k_B T / E_bind), where E_bind ~ V_yield × e ~ 43.65 keV × e ≈ 7×10⁻¹⁵ J per node bond. Then β ~ k_B T_CMB / E_bind ~ 3.76×10⁻²³ / 7×10⁻¹⁵ ~ 5×10⁻⁹ per unit-volume. Single-power thermal-strain gives δL/L ~ 5×10⁻⁹ — orders of magnitude smaller than δ_strain ≈ 2.225×10⁻⁶. So naive P3 also fails by orders of magnitude unless the substrate-thermodynamics coupling is more efficient than naive solid-thermal-expansion.

**All three candidate paths fail at order-of-magnitude before substrate-mechanism direction is set.** This strongly suggests the substrate-physics mechanism producing δ_strain magnitude is structurally different from any of the candidates — either a new substrate-mechanism class not enumerated in the current corpus, or one of the candidates with a substrate-specific amplification factor not captured by naive estimates.

**Adjudication recommendation**: Q-DELTA-MAP-1 is a framework-extension question with substrate-physics direction-setting required. NOT a closure-asserted answer; NOT a near-term tweak. Surface to Grant via orchestration session for substrate-mechanism direction.

## §4 — Decision: WALK-BACK

Per prereg adjudication criteria:

- **PASS** ruled out: substrate-thermodynamic mapping cannot close from canonical content; Q-DELTA-MAP-1 requires substrate-physics direction-setting
- **PARTIAL** ruled out: partial closure would still require canonical-leaf assertion of mechanism beyond canonical content; would conflict with Pitfall #5 + clm-3zz0f6 ruling
- **WALK-BACK** selected: clean negative result on substrate-thermodynamic-mapping derivation; Q-DELTA-MAP-1 logged; Type B walk-back of SM-leaked language proceeds (vocabulary cleanup, independent of substrate-mechanism question)

Per Rule 11 (honest closure): the pre-registered substrate-thermodynamic mapping failed decisively; a single canonical-content-inconsistency explanation (clm-3zz0f6 SYM α-invariance) closes the derivation chain at step 5 (α modulation step); the failure mechanism is named (category error: c_shear vs c_EM substitution); the branch can be cleanly closed without rescue. The discipline is working as designed.

Per Rule 12 (substitution-not-retraction): the prework brief's hypothesis (δ_strain via SYM-class Machian-G cascade) is falsified at the canonical-content-inconsistency step. The new substrate-physics path (Q-DELTA-MAP-1) is logged as framework-extension question without unverified hypothesis substitution; it gets its own future workstream with its own verification chain.

## §5 — Vocabulary cleanup (Type B walk-back) proceeds independently

The Type B walk-back of SM-leaked "G_vac + equipartition" + "thermal expansion" language is INDEPENDENT of the substrate-mechanism question — it substitutes SM-vocabulary open-derivation pointers with substrate-native open-derivation pointers (Q-DELTA-MAP-1). The walk-back does NOT assert closure of the substrate-physics question; it just relabels the open item from SM-vocabulary to substrate-vocabulary.

Walk-back file scope per prereg §3h-exhaustive-4:

1. `manuscript/ave-kb/entry-point.md:12`
2. `manuscript/ave-kb/common/full-derivation-chain.md:816`
3. `manuscript/ave-kb/common/mathematical-closure.md:105, 128, 134, 163`
4. `manuscript/ave-kb/common/claim-quality.md:21, 36`
5. `manuscript/ave-kb/common/divergence-test-substrate-map.md:720`
6. `manuscript/ave-kb/vol1/claim-quality.md:53, 66, 121, 123`
7. `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md:166, 169`
8. `manuscript/ave-kb/vol1/ch0-intro.md:55`

Replacement pattern: "G_vac + equipartition" → "substrate-thermodynamic mapping (Q-DELTA-MAP-1)" with cross-link to clm-009nkt + omega-freeze-cosmic-grain-cascade canonical anchor.

## §6 — Cascading clm-quality updates

**clm-009nkt** (Vacuum Strain Coefficient δ_strain): confidence STAYS at 0.45. Rationale extended with 2026-05-27 Phase 3-A3 WALK-BACK note + Q-DELTA-MAP-1 cross-link. Strengthen-by item updated from "Derive δ_strain magnitude from G_vac + equipartition" → "Adjudicate Q-DELTA-MAP-1 substrate-mechanism class (P1/P2/P3 candidates); derive δ_strain magnitude from chosen class".

**clm-5xon03** (Zero-Parameter Closure Status): confidence STAYS at 0.70. Rationale extended with 2026-05-27 Phase 3-A3 Q-DELTA-MAP-1 cross-link. Strengthen-by item 1 updated from "Derive δ_strain magnitude at T_CMB from G_vac + equipartition" → "Adjudicate Q-DELTA-MAP-1 substrate-mechanism class + derive δ_strain magnitude". Non-claim caveat "fitted scalar at T_CMB" preserved verbatim (this IS the honest Class A identity disclosure).

**No new canonical leaf**. Creating `delta-strain-cosmic-projection.md` would be premature absent Q-DELTA-MAP-1 closure. Deferred to a future workstream after Grant adjudication.

## §7 — Adjudication summary

**Phase 3-A3 outcome: WALK-BACK** (~10% probability per prereg adjudication criteria; per Honest Closure Rule 11).

**Substantive substrate-physics finding**: the prework brief's proposed δ_strain derivation chain contains a category error (c_shear vs c_EM substitution) that produces α modulation in violation of canonical clm-3zz0f6 SYM-class α-invariance ruling. The corpus does not yet have a canonical substrate-mechanism class for low-amplitude electromagnetic thermal-bath loading; closing the δ_strain magnitude derivation requires substrate-physics direction-setting (Q-DELTA-MAP-1).

**Type B walk-back proceeds independently**: SM-leaked language at 8 files walked back to substrate-native open-derivation pointers without asserting closure.

**clm-009nkt confidence STAYS at 0.45** (no derivation work; vocabulary cleanup does not lift derivation-class evidence). **clm-5xon03 confidence STAYS at 0.70**.

**Q-DELTA-MAP-1 logged as new framework-extension question** for Grant adjudication.

**Q-CLM-3ZZ0F6-DEPTH-1 logged as KB-hygiene followup**: recommend amending CLAUDE.md INVARIANT-S2 to disambiguate c_EM (= c_0/S in SYM) vs c_shear (= c_0√S in SYM) explicitly per canonical clm-8nkvwy. The current "c_eff = c_0√S" without phase-vs-group disambiguation is the upstream source of the category-error pattern this Phase 3-A3 work surfaced.

## §8 — Pure-AVE-corpus rule confirmed

NO external-context references in this result or any associated deliverable. Pure substrate physics throughout.
