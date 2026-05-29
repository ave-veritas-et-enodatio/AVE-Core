[↑ Research](index.md)

# Phase 3-A3 Prereg — δ_strain as 5th Class E Machian-G Projection

**Branch**: `analysis/phase-3-a3-delta-strain-machian-projection` off `main @ fb2fa923`
**Prework brief**: [`_orchestration/2026-05-28_phase-3-a3-prework.md`](../_orchestration/2026-05-28_phase-3-a3-prework.md)
**Companion result**: [`2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md`](./2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md)
**Date**: 2026-05-27

## Frame

`clm-009nkt` δ_strain ≈ 2.225×10⁻⁶ is the canonical CMB thermal-running residual of α below the cold-lattice asymptote α⁻¹_ideal = 4π³ + π² + π ≈ 137.0363038. Currently confidence 0.45; one back-subtracted scalar (`DELTA_STRAIN = 1 - (1/ALPHA)/ALPHA_COLD_INV` at `src/ave/core/constants.py:182`). Sign + existence substrate-derived (substrate thermal expansion of spatial metric at finite T); magnitude not derived from substrate primitives.

Phase 3-A3 prework brief reframed the work from the standing "G_vac + equipartition" SM-leaked open-derivation framing to a substrate-native Machian-G Class E operating-point projection at u_0* ≈ 0.187: δ_strain becomes the 5th joint-constrained observable in the cosmic-substrate family {G, H_∞, Ω̂_freeze, α, δ_strain}. Closure target: clm-009nkt 0.45 → 0.55–0.60 PARTIAL band via canonical-leaf formalization + Type B walk-back of SM-leaked language.

## Skills firing list (mandatory per prework brief)

ave-prereg v1.1 (Step 3.5 substrate-thermodynamic-mapping); ave-canonical-leaf-pull v1.3 (Trigger 17 vocabulary-broadened pre-survey); ave-canonical-source; ave-discipline-translate v1.1 Trigger 6 (LOAD-BEARING SM-leakage cleanup); substrate-native-check; consistency-vs-emergence v1.3 Step 8c (canonical fire-case — Class E stays at Class E); ave-walk-back v1.2 Step 3h-exhaustive (Type B walk-back); ave-worktree-paths v1.0 (first-call canary + worktree-absolute paths); verify-before-cite v1.4; ave-evidence-framing-discipline; ave-discrimination-check; ave-handoff-canonical-locale; phase-space-coordinate-check.

## Canonical-leaf pre-survey results (ave-canonical-leaf-pull v1.3 Trigger 17)

**Standard-physics wedge** (`δ_strain`, `delta_strain`, `DELTA_STRAIN`, `thermal expansion`, `G_vac + equipartition`):

| Source | Lines | Content |
|---|---|---|
| `vol1/claim-quality.md` | 43-68, 101-123 | clm-5xon03 Zero-Parameter Closure Status (confidence 0.70, solidity 0.65) + clm-009nkt δ_strain entry (confidence 0.45) |
| `vol1/ch8-alpha-golden-torus.md` | 155-186 | Canonical §"CMB thermal-bridge correction" + closure status discussion; line 161 "thermal expansion of the substrate's spatial metric"; line 165-166 Class 2/Class A predicted/fitted disclosure; line 169 G_vac + equipartition open item |
| `common/mathematical-closure.md` | 105, 128, 134, 163 | δ_strain closure-status table entry + G_vac + equipartition language repeated 4x |
| `common/claim-quality.md` | 21, 36, 134-165 | Cross-cutting Zero-Parameter Closure entry + clm-3zz0f6 α Invariance Under Symmetric Gravity (confidence 0.85) |
| `common/full-derivation-chain.md` | 816 | "Honest framing of zero free parameters" — G_vac + equipartition open item |
| `entry-point.md` | 12 | Top-level framework framing — G_vac + equipartition open item |
| `vol1/ch0-intro.md` | 55 | Foreword bullet — G_vac + equipartition open item |
| `common/divergence-test-substrate-map.md` | 720 | Open formal-rigor item — G_vac + equipartition language |

**Substrate-native wedge** (`SYM scaling`, `symmetric saturation`, `operating point`, `u_0`, `Ω_freeze`, `Class E`):

| Source | Lines | Content |
|---|---|---|
| `common/omega-freeze-cosmic-grain-cascade.md` | 11-34 | Three-route Class E framework: α, G, J_cosmic all derive from single u_0* ≈ 0.187; canonical-leaf for the Machian-G operating-point cascade |
| `common/boundary-observables-m-q-j.md` | 11-23, 52-68 | Three M, Q, J boundary observables at every Γ = -1 saturation surface; canonical Class E joint-constraint structure |
| `CLAUDE.md` (KB) | 60 | INVARIANT-S2 operating-point + small-signal modulation: ε_eff = ε_0 S, μ_eff = μ_0 S, c_eff = c_0√S; Gravity = SYM-class realization; Schwarzschild c√(1−r_s/r) in weak-field limit |
| `common/claim-quality.md` | 111-118 | clm-8nkvwy Symmetric vs Asymmetric Saturation canonical: SYM → Z = Z_0 invariant, c_EM = c_0/S, c_shear = c_0√S; ASYM → Z = Z_0/√S, c_EM = c_0/√S |
| `common/claim-quality.md` | 134-165 | clm-3zz0f6 α Invariance Under Symmetric Gravity: under SYM, α exactly invariant; Pitfall #5 — no Δα/α from gravity |
| `vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md` | 11-26 | Derived consequence: α = α_0 exactly invariant under SYM scaling (algebraic identity: ε_local·c_local cancels n·S factor) |
| `vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md` | 22-34 | Class E operating-point projection canonical companion for the new leaf |

## Step 3.5 substrate-thermodynamic-mapping (pre-frozen extension)

**Prework-brief pre-frozen target** (from prework brief lines 21-27):
- Canonical δ_strain ≈ 2.225×10⁻⁶
- Asserted S(A_0^cosmic) ≈ 1 − (2/3)·δ_strain = 1 − 1.483×10⁻⁶
- Asserted (A_0^cosmic/A_yield)² = 1 − S² ≈ 2.967×10⁻⁶
- Asserted A_0^cosmic/A_yield ≈ 1.722×10⁻³

**Implementor verification step (Step 3.5 extension per ave-prereg v1.1)**: walk the prework-brief derivation chain through canonical SYM-class definitions (clm-3zz0f6 + clm-8nkvwy + CLAUDE.md INVARIANT-S2) and dim-check the proposed α modulation step.

Walking the chain at canonical primitives:

1. Assume δ_strain mechanism is some saturation-kernel substrate loading (consistent with Ax 4)
2. Prework brief proposes INVARIANT-S2 SYM scaling: ε_eff = ε_0 S, μ_eff = μ_0 S, c_eff = c_0√S
3. Prework brief proposes α modulation: α_eff/α_cold = 1/S^(3/2) → δ_strain = (3/2)(1−S)

**Verification at the canonical α-invariance leaf** (`vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md:15-22`):
> "Under Symmetric Gravity, both constitutive parameters scale by the same factor n·S (including Axiom 4 saturation). The fine-structure constant is therefore *exactly invariant* under gravitational strain: α = e²/(4π·ε_local·ℏ·c_local) = e²/(4π·(ε_0 nS)·ℏ·(c_0/(nS))) = α_0"

The canonical SYM-class derivation says SYM scaling gives α invariance — the n·S factor on ε is cancelled by the 1/(n·S) factor on c. The prework brief's c_eff = c_0√S substitution corresponds to c_shear (the "wave-packet freezes / rest mass" group velocity, per common/claim-quality.md:113), NOT the EM phase velocity c_EM that enters α. The corpus canonical:

- SYM-class EM phase velocity: c_EM,sym = c_0/S (clm-8nkvwy line 111)
- SYM-class shear velocity: c_shear,sym = c_0√S (clm-8nkvwy line 113)

Substituting the **correct EM phase velocity** (the velocity that appears in α = e²/(4π ε ℏ c_EM)) gives:
$$\alpha_{\text{SYM}} = \frac{e^2}{4\pi (\varepsilon_0 S) \hbar (c_0/S)} = \frac{e^2}{4\pi \varepsilon_0 \hbar c_0} = \alpha_0$$

**α IS INVARIANT under SYM, per canonical clm-3zz0f6.** The prework brief's `α_eff/α_cold = 1/S^(3/2)` derivation contains a substrate-mechanism category error: it substitutes c_shear (group/rest-mass-freeze velocity) into the electromagnetic α expression where c_EM (phase velocity) belongs. The corpus' Pitfall #5 (LIVING_REFERENCE.md, cross-cutting clm-3zz0f6:147) explicitly warns this is the standing framework-leakage error: "any framework summary suggesting 'AVE predicts multi-species Δα/α from gravity' is wrong."

**ASYM alternative check** (per clm-8nkvwy line 112 ASYM-class scaling):
$$\alpha_{\text{ASYM}} = \frac{e^2}{4\pi (\varepsilon_0 S) \hbar (c_0/\sqrt{S})} = \frac{\alpha_0}{\sqrt{S}}$$

For small loading (S ≈ 1), this gives `δ_strain ≡ (1−S)/2` (single-power), NOT the prework brief's `(3/2)(1−S)`. Numerically: for δ_strain = 2.225×10⁻⁶, ASYM gives `(A/A_yield) ≈ 2.98×10⁻³` (factor √3 different from prework brief's 1.72×10⁻³).

But ASYM-class per clm-8nkvwy applies to **strong EM field loading only** (where ε scales but μ doesn't because the magnetic sector isn't being driven). CMB at 2.725 K is a low-amplitude thermal photon bath — not the "strong EM" regime ASYM is designed for. And the canonical clm-3zz0f6 explicitly notes (line 147) that the δ_strain mechanism is "**CMB-induced spatial metric expansion, NOT a gravitational effect**" — distinguishing it from the SYM-class gravitational scaling. So neither SYM nor ASYM cleanly maps.

**Conclusion of Step 3.5**: the prework brief's proposed derivation chain has a substantive substrate-physics inconsistency with canonical content (clm-3zz0f6 SYM α-invariance ruling), and the canonical saturation-class taxonomy (SYM vs ASYM per clm-8nkvwy) does not yet have a third class for the low-amplitude thermal-photon-bath loading that the δ_strain mechanism narrative requires.

## Substrate-thermodynamic-mapping framework-extension question Q-DELTA-MAP-1

**Q-DELTA-MAP-1 (NEW 2026-05-28)**: What substrate saturation class does low-amplitude electromagnetic thermal-bath loading fall into?

The corpus has two canonical saturation classes (clm-8nkvwy):
- **SYM** (mass-energy load: gravity, BH interior, particle confinement): both μ and ε scale by S; α invariant per clm-3zz0f6
- **ASYM** (strong EM field load): only ε scales by S; α scales as α_0/√S

CMB at 2.725 K is a low-amplitude electromagnetic load (thermal photon bath). Neither canonical class applies:
- Not SYM (no large mass-energy saturating the substrate)
- Not ASYM-as-defined (CMB photons individually are far below the "strong EM field" regime; total electromagnetic energy density is tiny)
- But the substrate is *thermally agitated* by the CMB photon bath — a coupling that lacks an SYM/ASYM canonical analog

**Three plausible substrate-physics paths** (paths require Grant adjudication; documented for the orchestration session):

- **(Q-DELTA-MAP-1 P1)** New saturation class **ELECTROMAGNETIC-THERMAL-BATH** (third class beyond SYM/ASYM). Distinct scaling rule. Class B substrate-mechanism manifestation rather than Class 2 axiom emergence; requires axiom-grounded justification that low-amplitude EM photon bath couples to substrate at a third-class scaling.
- **(Q-DELTA-MAP-1 P2)** ASYM is the right class but applies at the **time-averaged thermal-bath amplitude** rather than per-photon. Reanalyse ASYM with `A` interpreted as the equilibrium thermal-bath amplitude `⟨A²_{thermal}⟩ ~ k_B T_CMB / (ε_0 ℓ_node³ E_yield)` rather than per-photon. Derivation gives ASYM α-modulation with a specific cosmological-thermodynamic A_0 value.
- **(Q-DELTA-MAP-1 P3)** δ_strain is NOT a substrate-saturation-kernel modulation at all; it's a **cosmic-substrate-bond rest-length thermal contraction** independent of the Ax 4 saturation kernel. The substrate spatial metric (bond rest length L_spring) is itself a thermodynamic equilibrium parameter; T_CMB enters via the substrate's Cosserat bond-network thermal-equilibrium statistical mechanics, NOT via the saturation kernel S(A). This is closest to the canonical narrative at `vol1/ch8-alpha-golden-torus.md:161` ("thermal expansion of the substrate's spatial metric"). Distinct substrate-mechanism class — does NOT reduce to the SYM/ASYM scaling debate. Closing this requires a substrate-thermodynamics derivation that is currently absent from canonical content.

**The prework brief's "Machian-G operating-point cascade" framing presumes Path P1 or P2** (saturation-kernel substrate loading via cosmic operating-amplitude A_0^cosmic). Path P3 says the framing itself misidentifies the mechanism class — δ_strain isn't an operating-point projection at all, it's a substrate-thermodynamic-equilibrium projection. Distinguishing P1/P2/P3 requires substrate-physics derivation work that is NOT present in canonical content as of 2026-05-27.

**Adjudication recommendation**: Q-DELTA-MAP-1 is a framework-extension question, NOT a closure-asserted answer. Surface to Grant via orchestration session for direction-setting. The prework brief's Class E "5th Machian-G projection" framing remains potentially correct (if Path P1 or P2 closes from substrate primitives), but cannot be asserted as closed by Phase 3-A3 from canonical content alone.

## Per `consistency-vs-emergence` v1.3 Step 8c — Class E stays at Class E

Per Step 8b: what NEW substrate-mechanism content would Phase 3-A3 add beyond canonical Machian-G framework? Zero, if the substrate-thermodynamic mapping doesn't close. Phase 3-A3 attempts to add Class E "5th projection" identification, but per Q-DELTA-MAP-1 the substrate-mechanism path to this identification has not been derived from canonical content. The canonical Machian-G framework (`omega-freeze-cosmic-grain-cascade.md`) currently identifies four operating-point projections {α, G, J_cosmic} (and asserts H_∞ as a fourth consistency identity); promoting δ_strain to a fifth projection would require an additional substrate-mechanism step that this Phase 3-A3 work CANNOT supply absent Q-DELTA-MAP-1 adjudication.

**Step 8c result: classification stays at canonical Class E framework membership; Phase 3-A3 does NOT add new substrate-mechanism content beyond canonical Machian-G cascade.** The Type B walk-back of SM-leaked language proceeds independently and IS within scope of Phase 3-A3 (vocabulary cleanup, no substrate-mechanism work).

Confidence lift target on clm-009nkt: WALK-BACK if Q-DELTA-MAP-1 doesn't close from canonical content (most likely); PARTIAL 0.45 → 0.50 if pure vocabulary cleanup nudges the entry's classification rigor; NO lift to 0.55–0.60 absent substrate-mechanism derivation.

## Type B walk-back scope (ave-walk-back v1.2 Step 3h-exhaustive)

**3h-exhaustive-1 walk-back diff patterns** (extracted from canonical content, applied per prework brief Section "SM-leaked language patterns to walk back"):

| Pattern (OLD) | Target (NEW substrate-native) | Rationale |
|---|---|---|
| `"G_vac + equipartition"` (open-derivation framing) | `"substrate-thermodynamic mapping from u_0* operating point to substrate-amplitude loading (open framework-extension question Q-DELTA-MAP-1)"` | Reframes the open item from SM-language (G_vac + equipartition) to substrate-native open framework-extension question. Does NOT assert the substrate-physics closure exists. |
| `"thermal expansion"` (when describing δ_strain mechanism) | `"substrate spatial-metric strain at cosmic operating-point"` OR (for narrative passages) `"substrate spatial-metric thermal-bath response"` | Substrate-native vocabulary for the spatial-metric-loading mechanism. |
| `"first-principles derivation from G_vac + equipartition"` | `"substrate-thermodynamic derivation of cosmic-operating-point loading (Q-DELTA-MAP-1 open)"` | Same reframe with explicit framework-extension-question pointer. |
| `"fitted scalar at T_{CMB}"` | preserve (this IS the honest disclosure of the Class A identity) — but add cross-link to Q-DELTA-MAP-1 + Machian-G Class E framework membership | Disclosure is correct; cross-link improves Class E classification visibility. |

**Decision (per ave-discipline-translate v1.1 Trigger 6 LOAD-BEARING)**: walk-back substitutes the SM-leaked open-derivation pointer with a substrate-native open-derivation pointer. The walk-back does NOT assert closure of the substrate-thermodynamic mapping — it relabels the open item from SM-vocabulary to substrate-vocabulary while preserving the open status.

**3h-exhaustive-2 corpus-wide grep targets** (extended from prework brief):

```bash
grep -rn "G_vac + equipartition\|G_{vac} + equipartition\|G_vac.*equipartition" manuscript/ave-kb/ research/ _orchestration/
grep -rn "thermal expansion" manuscript/ave-kb/ | grep -iE "delta.strain|δ.strain|cmb|alpha|α"
grep -rn "spatial-metric thermal expansion\|spatial metric thermal expansion\|spatial.metric.thermal" manuscript/ave-kb/
grep -rn "fitted scalar.*T_CMB\|fitted scalar.*T_{CMB}\|one scalar at T_{CMB}\|one scalar at T_CMB" manuscript/ave-kb/
grep -rn "first-principles derivation from G_vac\|first-principles derivation from $G_{vac}$" manuscript/ave-kb/
```

**3h-exhaustive-3 Q1/Q2 hit classification**:

- **LOAD-BEARING** (will be walked back): canonical content asserting δ_strain awaits "G_vac + equipartition" derivation as SM-vocabulary open item
- **STALE-PROSE** (will be walked back): narrative passages describing δ_strain mechanism in undifferentiated "thermal expansion" language without cross-link to Q-DELTA-MAP-1 / Machian-G framework
- **PRESERVED-HISTORICAL** (Q1): walk-back-provenance notes documenting the 2026-05-28 reframing
- **FROZEN-SNAPSHOT** (Q2): pre-2026-05-28 research docs (e.g., `research/2026-05-19_*` predating this work) with SM-leaked language — exempt per Q2 (frozen-snapshot research docs are historical record)

**3h-exhaustive-4 gap inventory** (files in scope):

1. `manuscript/ave-kb/entry-point.md:12` — top-level framework framing; G_vac + equipartition language → substrate-native
2. `manuscript/ave-kb/common/full-derivation-chain.md:816` — Honest framing footer; G_vac + equipartition → substrate-thermodynamic-mapping pointer
3. `manuscript/ave-kb/common/mathematical-closure.md:105, 128, 134, 163` — Layer 0 inputs + back-edges discussion; G_vac + equipartition → substrate-thermodynamic-mapping (Q-DELTA-MAP-1)
4. `manuscript/ave-kb/common/claim-quality.md:21, 36` — Cross-cutting Zero-Parameter Closure entry; G_vac + equipartition → substrate-thermodynamic-mapping
5. `manuscript/ave-kb/common/divergence-test-substrate-map.md:720` — Open formal-rigor item footer; G_vac + equipartition → substrate-native
6. `manuscript/ave-kb/vol1/claim-quality.md:53, 66, 121, 123` — clm-5xon03 + clm-009nkt entries; G_vac + equipartition → substrate-thermodynamic-mapping; preserve fitted-scalar disclosure; add Q-DELTA-MAP-1 framework-extension-question cross-link
7. `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md:166, 169` — §"CMB thermal-bridge correction"; G_vac + equipartition → substrate-thermodynamic-mapping with Q-DELTA-MAP-1 cross-link
8. `manuscript/ave-kb/vol1/ch0-intro.md:55` — Foreword bullet; G_vac + equipartition → substrate-native
9. `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:30` (table row) — preserve canonical numerical value; add cross-link forward to new canonical leaf OR walk-back text in row if SM-leakage observed

Note: `vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md` mentions "thermal expansion" but in unrelated H-bond context; out of scope for δ_strain walk-back.

**3h-exhaustive-5 post-cleanup sweep verification before push**: grep for residual SM-leaked patterns; sweep-self-check confirms zero LOAD-BEARING + zero STALE-PROSE hits remaining.

## Per `consistency-vs-emergence` Class E framework membership

Phase 3-A3's intended deliverable was a substrate-native canonical leaf at `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-projection.md` formalizing δ_strain as the 5th Class E Machian-G projection. Per Step 3.5 + Q-DELTA-MAP-1 analysis above, this canonical leaf CANNOT be written without closure of the substrate-thermodynamic-mapping question, which itself requires Grant adjudication.

**Phase 3-A3 revised deliverable scope (post-Step 3.5 audit)**:

1. WALK-BACK on the substrate-thermodynamic-mapping derivation (this prereg + companion result document the WALK-BACK with the canonical-content-inconsistency finding)
2. Type B walk-back of SM-leaked "G_vac + equipartition" + "thermal expansion" patterns to substrate-native open-derivation pointers + Q-DELTA-MAP-1 cross-links (vocabulary cleanup; does NOT assert closure)
3. clm-009nkt rationale updated to reflect WALK-BACK + Q-DELTA-MAP-1 framework-extension-question framing; confidence STAYS at 0.45 (no derivation work; vocabulary-cleanup-only walk-back does NOT lift derivation-class evidence)
4. clm-5xon03 strengthen-by item updated to substrate-native language + Q-DELTA-MAP-1 cross-link; confidence STAYS at 0.70
5. NEW Q-DELTA-MAP-1 framework-extension-question logged in this prereg + cross-linked from clm-009nkt + clm-5xon03 + omega-freeze-cosmic-grain-cascade
6. NO new canonical leaf created (would be premature absent Q-DELTA-MAP-1 closure)

This is honest closure per Rule 11 (honest closure / wrong-reaction-debug-toward-rescue) + Rule 12 (substitution-not-retraction): the substrate-thermodynamic-mapping derivation is falsified at the canonical-content-inconsistency step; the vocabulary cleanup proceeds independently; no rescue-fork is attempted to convert ❌ to ✅; the framework-extension question is logged for future work.

## Adjudication criteria

- **PASS** (~0% — substrate-thermodynamic mapping closes from canonical content): would require Q-DELTA-MAP-1 closure absent from canonical content; ruled out at Step 3.5
- **PARTIAL** (~0% — mapping partially closes; canonical leaf created with explicit gap): would still require some substrate-mechanism content beyond what canonical Machian-G cascade provides; ruled out at Step 3.5
- **WALK-BACK** (selected outcome): mapping cannot close from canonical content; Q-DELTA-MAP-1 logged as framework-extension question; Type B walk-back of SM-leaked language proceeds (vocabulary cleanup independent of mechanism question); clm-009nkt confidence STAYS at 0.45; no new canonical leaf; clean negative result documented per Rule 11

## Open substrate-physics questions surfaced

- **Q-DELTA-MAP-1** (NEW 2026-05-28): What substrate saturation class does low-amplitude electromagnetic thermal-bath loading fall into? Three candidate paths P1/P2/P3 in §"Q-DELTA-MAP-1" above. Closure path requires substrate-physics work not present in canonical content as of 2026-05-27. Cross-link from clm-009nkt + clm-5xon03 + omega-freeze-cosmic-grain-cascade strengthen-by lists.
- **Q-CLM-3ZZ0F6-DEPTH-1** (NEW 2026-05-28): The canonical clm-3zz0f6 SYM-class α-invariance derivation uses the c_EM phase velocity (per the algebraic substitution form). The CLAUDE.md INVARIANT-S2 line 60 reads "c_eff = c_0√S" without phase-vs-group disambiguation, which could be read as endorsing the SYM-class derivation chain the prework brief proposed. Recommend amending CLAUDE.md INVARIANT-S2 to disambiguate c_EM (= c_0/S in SYM) vs c_shear (= c_0√S in SYM) explicitly, citing common/claim-quality.md:111-113 + vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md. Surface to orchestration session as KB-hygiene followup.

## Pure-AVE-corpus rule confirmed

NO external-context references in this prereg or downstream deliverables. Pure substrate physics throughout.
