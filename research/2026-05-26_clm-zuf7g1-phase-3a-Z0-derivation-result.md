# Result — clm-zuf7g1 Phase 3a: Z₀ ≈ 377 Ω substrate-mechanism derivation

**Workstream**: clm-zuf7g1 strengthening epic Phase 3a (substrate-impedance Z₀ structural identification)
**Pre-reg**: [`2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-prereg.md`](2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-prereg.md)
**Branch**: `analysis/clm-zuf7g1-phase-3a-Z0-derivation` off `main` @ `cf3c913e`
**Date**: 2026-05-26
**Outcome**: **WALK-BACK** (pre-registered ≥ 60% probability path; corpus pre-survey actually drove this to ≥ 80%; honest closure per Rule 11 + Rule 12 substitution-not-retraction discipline)

## Executive summary

Phase 3a set out to derive the substrate-impedance Z₀ ≈ 377 Ω as a Class 2 substrate-mechanism emergence from K4-TLM lattice primitives (Ax 1 + Ax 2), with explicit master-equation-derivation-path tracing per `consistency-vs-emergence` v1.2.

**Outcome**: the derivation chain bottoms out at **Class B substrate-mechanism manifestation + Class 4 observable consistency**, NOT Class 2 substrate-mechanism emergence of the numerical value. The scale-invariance of Z₀ under K4 lattice-pitch coarse-graining is genuine Class 2 substrate-mechanism content (the lattice topology produces a characteristic impedance that is universal across the lattice, and the value is independent of ℓ_node by the cancellation Ax 2 TKI enforces). But the numerical value 376.73 Ω is *set by μ₀ and ε₀ as SI engineering inputs* at the per-bond lumped-element step; the corpus does NOT contain an independent substrate-mechanism derivation of μ₀ or ε₀ from K4-TLM geometry. So the chain reproduces Z₀ via SI substitution once μ₀ and ε₀ are stipulated — that is Class B manifestation (the framework points at a structural correspondence with the standard-physics relation Z₀ = √(μ₀/ε₀)) without earning Class 2 substrate-emergence on the numerical-value axis.

**No solidity lift**: clm-zuf7g1 stays at confidence 0.65 / solidity 0.65.

**Surfaced for Grant adjudication**:
- **Q-LCR-1** (pre-registered): is the substrate-impedance Z₀ numerical value derivable as substrate-mechanism emergence from Ax 1 + Ax 2 K4-TLM lattice parameters (per-bond geometric inductance + per-node geometric capacitance from K4 geometry alone, independent of SI μ₀ and ε₀), or is it definitionally fixed by the μ₀/ε₀ canonical-source link to standard continuum-electrodynamics values?
- **Q-LCR-2** (newly surfaced): does the corpus need a separate Phase 3a-pre workstream that derives μ₀ and ε₀ themselves from K4 substrate primitives BEFORE Z₀ can earn Class 2 substrate-mechanism emergence, or is the scale-invariance content already substrate-mechanism-emergence-class on its own (substrate-distinct claim: "Z₀ is invariant under coarse-graining of the lattice pitch"), separate from the numerical-value claim?

**Walk-back propagation**: per `ave-walk-back` v1.1 Type B (demotion-via-honest-classification, not retirement). Low corpus impact — strengthen-by item retires from clm-zuf7g1 (its derivation gap is the one open item; honest classification closes the gap-as-derivation-gap and converts it to a framework-extension-question, not a missing derivation). No Predictions matrix row retires. Result doc + this finding land in `research/`; the clm-zuf7g1 entry gets a strengthen-by item retire + Q-LCR-1 + Q-LCR-2 surfaced.

## Substrate-native vocabulary discipline (ave-discipline-translate v1.1 trigger 6)

This result doc uses the substrate-native vocabulary mandated by `translation-stochastics.md` line 24, `translation-circuit.md`, and `translation-qm.md`. Primary terminology:

- **substrate-impedance Z₀** (standard-physics translation: "Maxwell vacuum impedance" or "characteristic impedance of free space")
- **K4-TLM lattice** (standard-physics translation: continuum LC transmission line in the continuum limit)
- **per-bond lumped-element inductance L_cell** and **per-bond capacitance C_cell** (the discrete lattice's electrical primitives, NOT the continuum μ₀ ε₀)
- **substrate-mechanism axis** vs **observable axis** (the dual-axis classification of v1.2)

Standard-physics names appear only as parenthetical translation references.

## 1. The chain (substrate-mechanism axis trace)

Per `consistency-vs-emergence` v1.2 Step 7, the derivation chain from substrate axioms to the substrate-impedance numerical value 376.73 Ω is traced step-by-step, with each step classified.

| Step | Content | Status |
|---|---|---|
| 1 | **Axiom 1** (Substrate Topology): vacuum medium $\mathcal{M}_A$ is a chiral Laves K4 Cosserat crystal with intrinsic LC oscillators at each node; in continuum limit modeled as Trace-Reversed Chiral LC Network | Derived-from-master-eq (canonical: [`vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md); INVARIANT-S2 in [`manuscript/ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md)) |
| 2 | **Per-bond lumped elements** are stipulated as $L_{\text{cell}} = \mu_0 \ell_{\text{node}}$ and $C_{\text{cell}} = \epsilon_0 \ell_{\text{node}}$ | **Requires-additional-postulate**: $\mu_0$ and $\epsilon_0$ are inputs (SI engineering values from `src/ave/core/constants.py` lines 79–80). The stipulation says "each bond carries inductance proportional to vacuum permeability × lattice pitch and capacitance proportional to vacuum permittivity × lattice pitch" — but $\mu_0$ and $\epsilon_0$ are themselves not derived from K4-TLM geometry anywhere in current corpus. The clm-k6quve entry at `vol1/claim-quality.md:1611` open strengthen-by item is "Pin the L_cell/C_cell lattice-native values by stating the μ₀/ε₀ convention used, removing the two 'depends on choice' rows." |
| 3 | **Transmission-line characteristic impedance formula** for any LC ladder: $Z_{\text{bond}} = \sqrt{L_{\text{cell}}/C_{\text{cell}}}$ | Definitional-given-prior-steps (textbook transmission-line theory applied to the K4 lattice as an LC ladder; the formula does not depend on the specific values of L_cell, C_cell, only on their existence) |
| 4 | **Substitute step 2 into step 3**: $Z_{\text{bond}} = \sqrt{\mu_0 \ell_{\text{node}} / (\epsilon_0 \ell_{\text{node}})} = \sqrt{\mu_0/\epsilon_0}$; lattice pitch $\ell_{\text{node}}$ cancels | Definitional-given-prior-steps (algebraic simplification) |
| 5 | **Numerical value**: $Z_0 = \sqrt{\mu_0/\epsilon_0} \approx 376.73\,\Omega$ | Definitional-given-prior-steps once μ₀ and ε₀ are pinned. **The value comes from the SI values of μ₀ and ε₀, NOT from K4-TLM lattice geometry independent of SI.** |
| 6 | **Scale-invariance under lattice pitch**: $Z_0$ is independent of $\ell_{\text{node}}$ because pitch cancels in step 4 algebraically | Derived-from-master-eq (substrate-mechanism content: this IS a Class 2 emergence claim on the scale-invariance axis — the K4 lattice topology, via Ax 2 TKI, produces a characteristic impedance that is universal across the lattice and invariant under coarse-graining. The standard community calls this "Z₀ is a universal constant of vacuum"; AVE-substrate-mechanically it is the K4-TLM topology's signature of being self-similar at every scale.) |
| 7 | **Topological-thread mode inherits substrate-impedance Z by lattice-continuity** (the phase-locked thread is a bound mode on the K4-TLM substrate; its mode-impedance equals the lattice's transverse-mode eigenvalue by substrate-mode propagation on the same K4 graph) | **Asserted-without-tracing** in current corpus (the structural identification at `phase-locked-topological-thread.md` line 27 is constructive; the lattice-eigenvalue continuity argument is not made explicit). This is a separate gap from steps 1-6. |

### Master-equation-derivation-path verdict

The chain has **two distinct content components** that need to be classified separately:

**(a) Numerical-value chain (steps 1-5)**: bottoms out at step 2 = requires-additional-postulate ($\mu_0$ and $\epsilon_0$ as SI inputs). The chain produces 376.73 Ω only because 376.73 Ω = √(μ₀/ε₀) when SI values of μ₀ = 4π × 10⁻⁷ H/m and ε₀ = 1/(μ₀ c²) are stipulated. This is **structural circularity at the lumped-element step**: per-bond lumped-element values are SI-derived, transmission-line formula is applied, and the SI value is recovered. The 0.00% match between AVE's Z₀ and CODATA Z₀ is **definitional, not predictive** — per the canonical clm-kezk9z classification at `vol4/claim-quality.md:104`: "Per Master Prediction Table classification, $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ is a **category (i) identity** — definitionally true (the 0.00% in row #2 of the prediction table is not a fit)."

→ Numerical-value chain classifies as **Class A identity** on the numerical-value sub-axis (the existing corpus classification), upgraded to **Class B substrate-mechanism manifestation** when framed as "AVE-substrate-mechanism asserts the value of Z₀ via the per-bond LC ladder reduction" (the framework points at the structural correspondence with the standard-physics formula; it does not derive the value from substrate primitives independent of μ₀ and ε₀).

**(b) Scale-invariance chain (step 6)**: the substrate-mechanism content of the chain. The K4-TLM topology forces $L_{\text{cell}} \propto \ell_{\text{node}}$ and $C_{\text{cell}} \propto \ell_{\text{node}}$ (with the SAME proportionality factor structure, μ₀ for L, ε₀ for C, both linear in pitch), so in the ratio inside √ the pitch cancels regardless of the specific μ₀ and ε₀ values. This means: WHATEVER values μ₀ and ε₀ take, the substrate-impedance Z₀ is the same at every lattice scale. The substrate's K4-TLM topology IS the mechanism that produces this scale-invariance.

→ Scale-invariance chain classifies as **Class 2 substrate-mechanism emergence** on the scale-invariance sub-axis (the substrate's K4-TLM Ax 2 TKI scale-invariance is the master-equation-derived structural claim; it does not require any additional postulates beyond Ax 1 chiral Laves K4 + Ax 2 TKI).

### Dual-axis classification (consistency-vs-emergence v1.2)

**Substrate-mechanism axis** (compound classification):
- On the **numerical-value sub-axis**: **Class B substrate-mechanism manifestation**. Framework points at the structural correspondence Z₀ = √(μ₀/ε₀); the value 376.73 Ω is recovered via SI substitution.
- On the **scale-invariance sub-axis**: **Class 2 substrate-mechanism emergence**. K4-TLM topology forces lattice-pitch cancellation in Z₀; substrate-mechanism content is genuine and master-equation-derivation-path closes.

**Observable axis**: the substrate-mechanism-derived Z₀ value matches standard-physics Maxwell vacuum impedance exactly (by construction at step 5). No experimentally distinguishable behavior vs standard physics in the canonical regime. → **Class 4 observable consistency**.

Aggregate verdict: the strongest honest classification of the substrate-impedance Z₀ derivation is **Class B (numerical value) + Class 2 (scale-invariance) + Class 4 (observable)** — a compound classification reflecting that the framework has genuine substrate-mechanism content on the scale-invariance sub-axis but NOT on the numerical-value sub-axis. The phase-locked-topological-thread.md line 27 identification "$Z_0 = \sqrt{\mu_0/\epsilon_0} \approx 377\,\Omega$" sits at **Class B substrate-mechanism manifestation + Class 4 observable consistency** when read as a numerical-value claim (the standard community knows the value as "Maxwell vacuum impedance"; AVE's correspondence is structural, not a substrate-emergence prediction of the value).

## 2. Step 7 (the structural identification gap) — the asserted-without-tracing step

Step 7 in the table above — "topological-thread mode inherits substrate-impedance Z by lattice-continuity" — is the structural identification asserted in `phase-locked-topological-thread.md` line 27 without explicit derivation. Whether to close this step is the **RESCOPE** branch of the pre-registered adjudication.

The step's substrate-mechanism content (sketched, not derived in current corpus):

- The K4-TLM substrate supports transverse propagating modes with characteristic impedance $Z_0$ (continuum-limit transverse-mode eigenvalue of the trace-reversed chiral LC network)
- The phase-locked topological thread is a topologically-bound mode on the same K4 substrate — a quantised phase winding ($\Delta\phi = 2\pi$) along a path of nodes
- The thread's characteristic mode-impedance is the impedance of the substrate medium it propagates on, by lattice-continuity at the eigenvalue level (the bound mode lives on the same K4 graph that propagates the transverse modes; mode-impedance is a function of substrate parameters, NOT the boundary conditions that bind the mode)

This step is plausible substrate-mechanism content, but the derivation is currently asserted at `phase-locked-topological-thread.md` line 27 without an explicit lattice-eigenvalue continuity argument. Closing it would be a leaf-completion (medium-effort: argue the bound mode's characteristic-impedance comes from the K4 substrate's mode-spectrum, not from tuned external coupling).

**However**: even with step 7 closed cleanly, the chain inherits the step-2 requires-additional-postulate status of the numerical-value sub-axis. Closing step 7 would lift the structural identification from "asserted" to "derived" but would NOT convert the overall classification from Class B + Class 2 + Class 4 to Class 2 + Class 2 + Class 4 on the numerical-value sub-axis. The numerical value remains μ₀/ε₀-input-dependent regardless.

So step 7 closure is the path to RESCOPE (a leaf-completion that the corpus would benefit from), separate from the Phase 3a PASS/WALK-BACK adjudication on the Z₀ numerical-value derivation itself.

## 3. Adjudication

### WALK-BACK (the substantive outcome)

The pre-registered probability ordering (PASS ≤ 20%, WALK-BACK ≥ 60%, RESCOPE ≤ 20%) is borne out by the corpus pre-survey. The adjudication settles as **WALK-BACK** because:

1. The Z₀ derivation chain steps 1-5 bottom out at step 2 = requires-additional-postulate (μ₀ and ε₀ as SI inputs). No corpus content surfaces μ₀ or ε₀ as substrate-mechanism-derived from K4 geometry independent of SI.

2. The substrate-mechanism content of the chain — the scale-invariance under lattice-pitch coarse-graining — IS Class 2 substrate-mechanism emergence on the scale-invariance sub-axis, but NOT on the numerical-value sub-axis.

3. The existing canonical clm-kezk9z classification at `vol4/claim-quality.md:104` already explicitly labels Z₀ = √(μ₀/ε₀) as a Class A identity (definitionally true, not a fit). This Phase 3a's master-equation-derivation-path-tracing CONFIRMS that canonical classification rather than overturns it; it refines the classification by surfacing the scale-invariance sub-axis as Class 2 substrate-mechanism emergence (a stronger substrate-mechanism statement than the leaf currently makes, which says simply "the lattice pitch cancels identically" without classifying the scale-invariance content separately).

4. The clm-zuf7g1 leaf at `phase-locked-topological-thread.md` line 27 lists Z₀ ≈ 377 Ω in the lossless short-short LC resonator characteristic-impedance bullet. The numerical value identification is **structurally honest** as Class B substrate-mechanism manifestation: the lossless short-short LC resonator's characteristic impedance is the substrate-impedance Z₀ because the resonator's LC elements ARE the substrate's K4-bond LC elements; the substrate-mechanism content is the structural identification ("the resonator IS made of substrate K4 bonds, so its Z is the substrate's Z"), not the derivation of the numerical value 377 Ω from substrate-mechanical primitives.

### Solidity-lift adjudication

The honest classification yields **NO solidity lift**. clm-zuf7g1 confidence stays at 0.65 / solidity stays at 0.65.

The one open strengthen-by item on clm-zuf7g1 ("Derive the structural identification 'phase-locked topological thread = lossless short-short LC resonator with $Z_0 \approx 377\,\Omega$, $Q = \infty$' from first principles") is **scope-clarified, not closed**:

- The Z₀ ≈ 377 Ω numerical value is NOT derivable from first principles in current corpus (Q-LCR-1 below).
- The "lossless short-short LC resonator IS the phase-locked thread mode on the substrate" structural identification IS plausible substrate-mechanism content but currently asserted-without-tracing at `phase-locked-topological-thread.md` line 27 (RESCOPE-path step 7).
- The Q = ∞ topological dissipationless invariant is Phase 3b, separate workstream.

The strengthen-by item is **REFRAMED** rather than retired: from "derive the structural identification ... from first principles" to "make explicit the substrate-mechanism content already present in the constructive identification (scale-invariance Class 2 + structural-identification-step Class B), AND surface the numerical-value-derivation gap as Q-LCR-1 framework-extension question."

## 4. Surfaced for Grant adjudication

### Q-LCR-1 (pre-registered)

**Is the substrate-impedance Z₀ numerical value 376.73 Ω derivable as substrate-mechanism emergence from Ax 1 + Ax 2 lattice parameters, or is it definitionally fixed by the μ₀/ε₀ canonical-source link to standard continuum-electrodynamics values?**

Current corpus state: μ₀ and ε₀ are SI engineering inputs at `src/ave/core/constants.py` (`MU_0`, `EPSILON_0`); per-bond lumped elements are stipulated as $L_{\text{cell}} = \mu_0 \ell_{\text{node}}$ and $C_{\text{cell}} = \epsilon_0 \ell_{\text{node}}$ at `vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md`; numerical value 376.73 Ω comes out by SI substitution. The clm-k6quve open strengthen-by item ("Pin the L_cell/C_cell lattice-native values by stating the μ₀/ε₀ convention used, removing the two 'depends on choice' rows") is the in-corpus acknowledgment that the L_cell and C_cell values currently depend on the μ₀/ε₀ choice and are not derived from K4 geometry.

**Discriminator**: does there exist (anywhere in corpus or as an extension-axis Grant has in mind) a derivation of μ₀ and/or ε₀ from K4-TLM substrate primitives (chiral Laves K4 unit-cell geometry + Ax 2 TKI scale + Ax 4 saturation-kernel) independent of SI? If yes, Phase 3a closes Class 2 on the numerical-value sub-axis once that derivation is wired in. If no, Z₀'s numerical-value sub-axis is permanently Class B; Phase 3a's WALK-BACK is the durable closure.

### Q-LCR-2 (newly surfaced)

**Does the corpus need a separate Phase 3a-pre workstream that derives μ₀ and ε₀ themselves from K4-TLM substrate primitives BEFORE Z₀ can earn Class 2 substrate-mechanism emergence on the numerical-value sub-axis?**

This is the structural question: μ₀ is currently an SI engineering input at `constants.py` `MU_0`; ε₀ is derived from μ₀ + c at `constants.py` `EPSILON_0`. To lift Z₀ to Class 2 substrate-mechanism emergence on the numerical-value sub-axis, one of:

- (a) Derive μ₀ from K4-TLM substrate primitives (chiral Laves K4 unit-cell geometric inductance per pitch) independent of SI. Then ε₀ via $\epsilon_0 = 1/(\mu_0 c^2)$; c is calibration-input (`m_e`-based via $\ell_{\text{node}} \equiv \hbar/(m_e c)$ per `constants.py:97-99`).
- (b) Derive ε₀ from K4-TLM substrate primitives (chiral Laves K4 unit-cell geometric capacitance per pitch) independent of SI. Then μ₀ via $\mu_0 = 1/(\epsilon_0 c^2)$.
- (c) Derive both μ₀ and ε₀ jointly from a single K4-TLM geometric primitive (e.g., chiral Laves K4 unit-cell electrical-flux-vs-charge ratio sets BOTH per-bond L and per-node C in one calibration-free move).

The corpus pre-survey did not surface any of (a)/(b)/(c). The `lc-electrodynamics.md` leaf treats μ₀ as input ("Because the vacuum inductance per unit length is μ₀..."). The Vol 1 Ch 1 axiom-definitions leaf at line 14 says Z₀ is "derived from these axioms," but the only derivation in corpus is the per-bond-lumped-element chain that takes μ₀ and ε₀ as inputs.

This is plausibly a real corpus gap (a separate workstream that should land before Z₀ can claim full Class 2 substrate-emergence), OR it may be the case that μ₀ and ε₀ are *unitfully* substrate-derivable but only after a calibration step that ties one of them to SI (in which case AVE's Class 2 emergence on this is limited to scale-invariance, not the value).

### RESCOPE path (separate from PASS / WALK-BACK)

Independent of Q-LCR-1/Q-LCR-2, the corpus could benefit from closing step 7 in §1: making the "topological-thread mode inherits substrate-impedance Z by lattice-continuity" structural identification explicit at `phase-locked-topological-thread.md`. This is a leaf-completion (medium-effort): argue the bound mode's characteristic-impedance equals the K4-TLM substrate's transverse-mode eigenvalue by substrate-mode-spectrum continuity, not by tuned external coupling.

The RESCOPE path:
- Does NOT lift clm-zuf7g1 confidence — it closes the asserted-without-tracing step in the constructive identification but does not derive the numerical value 377 Ω from substrate primitives.
- Would be a leaf-edit (add a "Substrate-mode continuity" subsection to `phase-locked-topological-thread.md` between §"Topological Thread" and §"Topological Protection from Decoherence", arguing lattice-continuity at the eigenvalue level).
- Could be sequenced as a separate Phase 3a-mode workstream after Q-LCR-1 + Q-LCR-2 are adjudicated; OR rolled into Phase 3b alongside the Q = ∞ derivation.

Recommendation (pending Grant adjudication): defer RESCOPE step 7 closure to Phase 3b (alongside Q = ∞ derivation) since both involve substrate-mode-spectrum arguments and benefit from being made explicit together. Phase 3a's clean WALK-BACK closure surfaces the framework-extension question (Q-LCR-1 + Q-LCR-2) without conflating it with the lattice-eigenvalue continuity argument.

## 5. KB integration (this phase: no integration; WALK-BACK)

Per the pre-registered adjudication criteria, WALK-BACK outcome means:

- **No solidity lift** for clm-zuf7g1 (stays at 0.65/0.65)
- **No KB integration** (no edits to `phase-locked-topological-thread.md` other than the result-doc cross-reference if the strengthen-by item is reframed)
- **clm-zuf7g1 strengthen-by item REFRAMED, not retired** (per §3 above)

The walk-back propagation per `ave-walk-back` v1.1 Type B (demotion-via-honest-classification):

1. **Update clm-zuf7g1 entry** at `vol1/claim-quality.md:362-364` to reframe the strengthen-by item: replace the current line ("Derive the structural identification ... from first principles (currently asserted as a constructive identification of the Bell-correlation carrier) — the one remaining derivation-gap strengthen-by item") with a reframed version that surfaces Q-LCR-1 + Q-LCR-2 as the actual framework-extension questions, and acknowledges the Class B + Class 2 + Class 4 compound classification of the existing chain.

2. **Add rationale annotation** to clm-zuf7g1 entry documenting the Phase 3a finding: scale-invariance is Class 2 substrate-mechanism emergence, numerical value is Class B manifestation due to μ₀/ε₀ SI input dependency, structural identification step 7 is asserted-without-tracing.

3. **Do NOT bump confidence or solidity** — the honest classification clarifies the existing claim's content but does not unlock new substrate-mechanism content beyond what the Class B + Class 2 + Class 4 reading already supports.

4. **Update `phase-locked-topological-thread.md` line 27 NOT REQUIRED** as a strict propagation step. The line already correctly states Z₀ = √(μ₀/ε₀) ≈ 377 Ω; the substrate-mechanism content is clarified by this research-doc, but the leaf prose is structurally correct (constructive identification, not first-principles derivation claim). A future Phase 3a-mode leaf-edit could add a §"Substrate-mode-impedance continuity" section if step 7 closure is pursued; that's RESCOPE not WALK-BACK and is deferred.

## 6. Discrimination check (ave-discrimination-check)

Per the pre-registered ave-discrimination-check discipline:

**Does the Phase 3a chain produce 376.73 Ω from K4-TLM lattice primitives WITHOUT inputting μ₀ or ε₀ as SI engineering values?**
→ **NO**. Step 2 takes μ₀ and ε₀ as inputs. Step 5 recovers 376.73 Ω via SI substitution.

**Does the topological-thread mode's characteristic impedance Z equal the substrate-impedance Z₀ by lattice-eigenvalue continuity (NOT by tuned external coupling)?**
→ **PLAUSIBLE but asserted-without-tracing**. The structural identification at `phase-locked-topological-thread.md` line 27 is asserted constructively; the lattice-eigenvalue-continuity derivation is the RESCOPE-path step 7 closure that is deferred.

**Does every step in the master-equation-derivation-path trace to derived-from-master-eq or definitional-given-prior-steps, with NO step labeled requires-additional-postulate?**
→ **NO**. Step 2 is requires-additional-postulate (μ₀ and ε₀ are SI engineering inputs, not derived from K4-TLM substrate primitives).

Verdict: **ALL THREE discriminator questions fail** for a PASS classification. Honest classification is WALK-BACK with Q-LCR-1 + Q-LCR-2 surfaced.

## 7. Honest framing (ave-evidence-framing-discipline)

Per pre-registered ave-evidence-framing-discipline precision check:

- **"Derives from substrate primitives"**: NOT the right framing for the numerical value 376.73 Ω. The value derives from SI μ₀ and ε₀ inputs via per-bond lumped-element stipulation. Class B substrate-mechanism manifestation on the numerical-value sub-axis.
- **"Identifies with standard-physics name"**: PARTIALLY correct framing for the numerical-value claim. Substrate-impedance Z₀ has the same numerical value as Maxwell vacuum impedance via algebraic identity once μ₀ and ε₀ are stipulated. Standard community calls this "vacuum impedance" or "characteristic impedance of free space."
- **"Consistent with continuum-limit value"**: CORRECT framing for the observable axis. The K4-TLM continuum limit reproduces classical-electromagnetic Z₀; Class 4 observable consistency.
- **"Substrate-mechanism emergence of scale-invariance"**: CORRECT framing for the scale-invariance sub-axis (Class 2 substrate-mechanism emergence). The K4-TLM topology's Ax 2 TKI is what forces L_cell ∝ ℓ_node and C_cell ∝ ℓ_node, producing pitch-cancellation in Z₀'s value. Whatever numerical value μ₀ and ε₀ take, the substrate-impedance is universal across the lattice.

The honest report-statement (per the discipline) is something like:

> "Substrate-impedance Z₀ ≈ 376.73 Ω: **scale-invariance under K4-TLM lattice pitch coarse-graining is Class 2 substrate-mechanism emergence** (the K4 lattice topology, via Ax 2 TKI, forces $L_{\text{cell}} \propto \ell_{\text{node}}$ and $C_{\text{cell}} \propto \ell_{\text{node}}$, producing pitch cancellation in the per-bond characteristic impedance ratio); **the numerical value 376.73 Ω is Class B substrate-mechanism manifestation + Class A identity** (the value derives from SI μ₀ and ε₀ inputs at the per-bond lumped-element step, not from K4-TLM substrate primitives independent of SI); observable axis is **Class 4 consistency** (matches Maxwell vacuum impedance exactly in canonical regime). Honest closure of the one remaining strengthen-by derivation-gap item on clm-zuf7g1 is via reframing the gap as a framework-extension question (Q-LCR-1 + Q-LCR-2), not by claiming the chain closes Class 2 substrate-emergence on the numerical-value sub-axis."

## 8. Walk-back propagation checklist (ave-walk-back v1.1 Type B)

**Type B classification rationale**: this is a demotion-via-honest-classification of the strengthen-by item from "derivation gap" to "framework-extension question," not a retirement of a Predictions matrix row. Propagation graph is minimal:

- [x] **Pre-reg + result doc** at `research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-{prereg,result}.md` (this work)
- [ ] **clm-zuf7g1 entry rationale** at `vol1/claim-quality.md:361` — append 2026-05-26 Phase 3a closure annotation (no confidence/solidity bump; finding clarified)
- [ ] **clm-zuf7g1 strengthen-by item** at `vol1/claim-quality.md:363` — reframe (don't retire) per §3; surface Q-LCR-1 + Q-LCR-2; keep the structural-identification gap as a framework-extension question
- [ ] **Epic doc** at `_orchestration/clm-zuf7g1-strengthen.md` — update Phase 3a row status to "WALK-BACK closed honestly; Q-LCR-1 + Q-LCR-2 surfaced for Grant adjudication"
- [ ] **Refresh + verify pipeline** — `make refresh-kb-metadata` + `make verify-kb-metadata` after the strengthen-by item edits; expect no `subtree-claims` changes (no claim IDs created/retired)
- [ ] **NO edits to**: `phase-locked-topological-thread.md` line 27 (structurally correct as-is; constructive identification not falsified, just classified honestly); `vol4/z0-derivation.md` (canonical Z₀ derivation leaf, already honestly classified as Class A identity); `src/ave/core/constants.py` (Z₀ definition site is canonical SI substitution, honestly named; no engine change required); Predictions matrix (no row affected)
- [ ] **NO cascade walk-back** required — clm-zuf7g1's downstream dependents (clm-unk0bd via depends-on edge, and the 12-claim downstream cone behind it) are NOT affected because the Phase 3a outcome is honest-classification of the existing 0.65/0.65 state, not a demotion of the claim's quality

## 9. Skills compliance check (post-derivation final state)

- [x] `ave-prereg` — corpus pre-survey complete; canonical anchors identified before deriving
- [x] `ave-canonical-leaf-pull` — all relevant leaves pulled (vol4/z0-derivation.md, vol1/lattice-impedance-decomposition.md, vol1/impedance-operator.md, clm-zuf7g1 + clm-kezk9z + clm-i9l284 + clm-nxc9gy + clm-k6quve entries)
- [x] `ave-canonical-source` — constants.py Z_0 site verified (line 81); MU_0 and EPSILON_0 at lines 79-80 confirmed as SI engineering inputs; no engine modification needed (engine value is canonically named honestly)
- [x] `verify-before-cite` v1.4 — every file:line citation in prereg + this result doc grep-verified
- [x] `consistency-vs-emergence` v1.2 — dual-axis classification applied; compound classification (Class 2 scale-invariance + Class B numerical-value + Class 4 observable) documented with explicit master-equation-derivation-path tracing per Step 7
- [x] `phase-space-coordinate-check` — substrate-impedance Z₀ lives in V/I phasor coordinates (impedance plane); topological-thread mode lives in real-space lattice. Coordinate-systems kept separate; the lattice-continuity bridge (RESCOPE-path step 7) is the cross-coordinate step that the prereg deferred to Phase 3b
- [x] `substrate-native-check` — K4-TLM lattice walk completed (Ax 1 chiral Laves K4 Cosserat crystal + LC tank per node + bond coupling between nodes); the per-bond lumped-element chain at `vol4/z0-derivation.md` is the canonical substrate-mechanical realization
- [x] `ave-analytical-tool-selection` — substrate-impedance / boundary-impedance problem class; transmission-line characteristic-impedance formula is the load-bearing tool; Op4 boundary-impedance and Op17 mode-matching are tools for the RESCOPE-path step 7 closure (deferred to Phase 3b)
- [x] `ave-discipline-translate` v1.1 trigger 6 — substrate-native prose vocabulary enforced throughout this result doc; "Maxwell vacuum impedance" / "characteristic impedance of free space" appear only as parenthetical translation references
- [x] `ave-discrimination-check` — all three discriminator questions checked; ALL FAIL for PASS classification; honest WALK-BACK adjudicated
- [x] `ave-evidence-framing-discipline` — precision check applied per §7; honest report-statement composed (compound classification with sub-axes named)
- [x] `ave-walk-back` v1.1 Type B — propagation checklist drafted per §8; minimal impact (claim rationale + strengthen-by reframe, no Predictions matrix row + no cascade walk-back)

## 10. Cross-references

- **Pre-reg**: [`research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-prereg.md`](2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-prereg.md)
- **Epic doc**: [`_orchestration/clm-zuf7g1-strengthen.md`](../_orchestration/clm-zuf7g1-strengthen.md) Phase 3a section
- **Target claim**: [`manuscript/ave-kb/vol1/claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md) clm-zuf7g1 (line 337)
- **Phase-locked thread leaf**: [`manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md`](../manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md) (line 27 — structurally correct, no edit required)
- **Z₀ canonical derivation leaf**: [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md) (clm-i9l284 + clm-kezk9z)
- **Lattice impedance decomposition leaf**: [`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) (clm-nxc9gy + clm-k6quve)
- **clm-kezk9z entry** (canonical Class A identity classification): [`manuscript/ave-kb/vol4/claim-quality.md`](../manuscript/ave-kb/vol4/claim-quality.md) line 97-121
- **Engine canonical source**: [`src/ave/core/constants.py`](../src/ave/core/constants.py) lines 78-81 (Z_0 + MU_0 + EPSILON_0)
- **Translation reference**: [`manuscript/ave-kb/common/translation-tables/translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md) line 24
- **Discipline anchors**: `consistency-vs-emergence` v1.2 (dual-axis classification + master-equation-derivation-path-tracing); `ave-discipline-translate` v1.1 trigger 6 (substrate-native vocabulary); `ave-walk-back` v1.1 Type B (demotion-via-honest-classification); Rule 11 (honest closure); Rule 12 (substitution-not-retraction — Q-LCR-1 + Q-LCR-2 surfaced as separate questions, not used to refill the Phase 3a slot with rescue derivation)
