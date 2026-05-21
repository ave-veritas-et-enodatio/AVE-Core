# Plumber-Physical Audit: Matched-LC-Coupling Framework Structural Gap

**Status:** Audit research doc 2026-05-17 night. Step-back self-audit as an applied vacuum engineer / electron plumber per Grant directive ("step back and audit like an applied vacuum engineer, map the physical picture of what you are attempting to derive"). Triggered by attempted next-session work on κ_quality bounded-scope derivation. **Headline finding**: the matched-LC-coupling formula $\epsilon_{det} = 4\pi/N_{single}^2$ is **structurally inconsistent** with the canonical AVE κ_entrain template from Sagnac-RLVE — including the canonical $\kappa_{entrain} = \rho_{matter}/\rho_{bulk}$ factor underpredicts DAMA observed rate by **factor ~2000×**. The 0.6% "match" at κ=1 (κ_entrain dropped) is therefore a NUMERICAL COINCIDENCE in formula-space, NOT a derived AVE prediction. The κ_quality bounded-scope derivation should be PAUSED pending plumber-physical adjudication of the actual energy-transfer mechanism.

**Date:** 2026-05-17 night
**Lane:** Research audit doc (research/ scope; not corpus-canonical)
**Triggered by:** Grant directive to audit-as-plumber before κ_quality derivation

## §1 — The matched-LC-coupling formula as currently written

From [`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md):

$$\epsilon_{det} = \frac{4\pi}{N_{single}^2}$$

Predicted rate:
$$R = N_e^{(kg)} \times \nu_{slew} \times \epsilon_{det} = 4.80 \times 10^{-7}\,\text{events/s/kg}$$

vs DAMA observed $4.77 \times 10^{-7}$ events/s/kg — 0.6% match at $\kappa_{quality} = 1$.

## §2 — The canonical κ_entrain template (what was missing)

From [`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) line 14-18 verbatim:

> "A macroscopic physical rotor is composed of fundamental nucleons (topological inductive loops). The degree to which these loops physically pack and magnetically couple to the vacuum impedance is strictly proportional to the object's physical mass density ratio ($\rho_{rotor} / \rho_{bulk}$).
>
> For a solid Tungsten rotor ($\rho_W = 19{,}300\,\text{kg/m}^3$):
> $$\kappa_{entrain} = \frac{19{,}300}{7.916 \times 10^6} \approx 0.00244$$"

**This is the canonical AVE matched-coupling template for matter-substrate interaction.** It governs how much external coupling is achievable between a physical mass and the substrate. For any matter with density $\rho$:

$$\kappa_{entrain}^{matter} = \frac{\rho_{matter}}{\rho_{bulk}}$$

For NaI ($\rho = 3670\,\text{kg/m}^3$):
$$\kappa_{entrain}^{NaI} = \frac{3670}{7.916 \times 10^6} = 4.63 \times 10^{-4}$$

For HPGe ($\rho = 5323\,\text{kg/m}^3$):
$$\kappa_{entrain}^{HPGe} = \frac{5323}{7.916 \times 10^6} = 6.72 \times 10^{-4}$$

**Per the canonical template, HPGe should couple MORE strongly than NaI by factor ~1.45 (density ratio).** This is exactly OPPOSITE the empirical observation (DAMA NaI detects; MAJORANA HPGe null).

## §3 — Structural inconsistency

If the matched-LC-coupling formula includes the canonical κ_entrain template:
$$\epsilon_{det}^{canonical} = \kappa_{entrain} \times \frac{4\pi}{N_{single}^2} = 4.63 \times 10^{-4} \times 2.07 \times 10^{-51} = 9.6 \times 10^{-55}$$

Predicted DAMA rate WITH canonical κ_entrain:
$$R_{canonical} = 2.57 \times 10^{26} \times 9.02 \times 10^{17} \times 9.6 \times 10^{-55} = 2.2 \times 10^{-10}\,\text{events/s/kg}$$

vs DAMA observed $4.77 \times 10^{-7}$ events/s/kg.

**Including κ_entrain underpredicts DAMA by factor 2000×.**

Two diagnoses:

**(a) The 0.6% match was a numerical coincidence in formula-space.** The 4π/N² formula at κ=1 happens to land near DAMA's rate by chance because:
- Formula-space at the required magnitude (~$10^{-51}$) is dense with candidates: $\alpha^{24}$, $(\alpha/2\pi)^{17}$, $1/N_{atoms}^2$, $4\pi/N^2$, $2\pi/N^2$, $\pi^2/N^2$, etc.
- Of these, $4\pi/N_{single}^2$ landed within 1% of required
- The 4π was post-hoc selected from 5 canonical AVE prefactors (per §3.1 of dama-matched-lc-coupling.md)
- Adding the canonical κ_entrain breaks the match by 2000×

**(b) DAMA's signal involves a NON-CANONICAL enhancement mechanism beyond κ_entrain.** Some additional factor boosts coupling 2000× above the canonical mass-density-ratio template:
- Resonance enhancement near atomic L-edges?
- Bragg-like coherent enhancement at the lattice scale?
- Tl-dopant-specific atomic transition?
- Some other unmodeled mechanism?

**Both diagnoses are consistent with the data; the framework cannot currently discriminate them.**

## §4 — Plumber-physical mechanism mapping

As an electron plumber, what does the actual physical picture of energy transfer from electron α-slew tank to external matter look like?

### §4.1 — Setup recap (canonical Vol 4 Ch 1)

The electron is an LC tank with:
- Resonant frequency: $\omega_C = c/\ell_{node}$ (Compton)
- Q-factor at TIR boundary: $Q = \alpha^{-1} \approx 137$
- Peak voltage: $V_{peak} \approx 3.73$ kV (safe below $V_{yield} = 43.65$ kV)
- Per-cycle reactive leak energy: $\alpha m_e c^2 = 3.728$ keV
- Per-cycle dissipation (when receiver available): $Z_0/(4\pi) \approx 30\,\Omega$ at impedance match
- Spatial localization: bound at TIR boundary, evanescent tail ~ $\ell_{node}/(2\pi) \approx 0.06$ Å

### §4.2 — What does an "external matched receiver" actually look like at $\omega_{slew}$?

For the electron's reactive leak to do work on something external, the external receiver must be:

1. **Resonant at $\omega_{slew}$ = $5.66 \times 10^{18}$ rad/s** ($\nu = 9.02 \times 10^{17}$ Hz, E = 3.728 keV)
2. **Impedance-matched to $Z_0/(4\pi) \approx 30\,\Omega$**
3. **Geometrically accessible** within evanescent reach (~Å scale)
4. **Coherent over many cycles** to avoid back-reflection cancellation

What natural physical degrees of freedom in matter satisfy these?

| Candidate receiver | Resonant frequency | Impedance | Geometric reach | Notes |
|---|---|---|---|---|
| Phonons | GHz-THz | varies | Lattice-scale | **6 OOM too slow**; ruled out |
| Plasmons | THz-PHz | varies | nm | **3 OOM too slow**; ruled out |
| Optical electronic transitions | $10^{14}$-$10^{15}$ Hz | varies | atomic | **3 OOM too slow**; ruled out |
| **Atomic K-shell transitions** | $10^{18}$ Hz at heavy atoms | Z-dependent | atomic | **MATCHES freq for atoms with K-edges near 3.728 keV** |
| Atomic L-shell transitions | $10^{17}$-$10^{18}$ Hz | Z-dependent | atomic | Matches freq for atoms with L-edges near 3.728 keV |
| Nuclear γ-transitions | keV-MeV | very narrow lines | nuclear | Possible for specific isotopes with γ-lines near 3.728 keV |
| Bulk crystal LC resonance | depends on lattice | depends on lattice | crystal-scale | **Speculative**; the matched-LC formula's implied receiver |

**The natural receivers at 3.728 keV are ATOMIC INNER-SHELL TRANSITIONS, not bulk crystal LC modes.** This is a Z-DEPENDENT mechanism, not Z-independent.

### §4.3 — Atomic inner-shell energies in DAMA NaI vs MAJORANA HPGe

| Material | Element | K-edge (keV) | L-edges (keV) | Relevance to 3.728 keV |
|---|---|---|---|---|
| **DAMA NaI** | Na | 1.07 | 0.06/0.03 | All below 3.728 (no near-resonance) |
| | I | 33.17 | 5.19/4.85/4.56 | **L-edges within 22% of 3.728** (near-resonant) |
| | Tl (dopant) | 85.5 | 14.7/13.4/12.7 | All far from 3.728 |
| **MAJORANA HPGe** | Ge | 11.10 | 1.41/1.25/1.22 | **SPECTROSCOPIC GAP** at 3.728 (between L and K) |
| **Sapphire Al₂O₃** | Al | 1.56 | 0.07 | All below 3.728 (no near-resonance) |
| | O | 0.54 | <0.05 | All below 3.728 |
| **Ca-containing** | Ca | 4.04 | 0.44/0.35/0.35 | **K-edge within 8% of 3.728** (very near-resonant) |

**Pattern**: materials with atomic K- or L-edges within $\sim 1$ keV of 3.728 keV (NaI Iodine L; Ca K) show possible near-resonant coupling. Materials with spectroscopic gaps (HPGe, Sapphire) don't.

**This atomic-physics picture naturally explains the cross-detector pattern**:
- DAMA NaI: I L-edge at 4.56 keV → near-resonant coupling (detuning factor 1/(4.56-3.728)² = 1.45 keV⁻²)
- MAJORANA HPGe: no edge nearby → no resonant coupling (matrix element suppressed)
- Sapphire: no edge nearby → would also be null (matching MAJORANA prediction)

### §4.4 — But: this is an ATOMIC-PHYSICS mechanism, NOT a substrate-physics mechanism

If the actual energy-transfer mechanism is via atomic-inner-shell resonant coupling, then:

- **Z-INDEPENDENCE claim (foreword bullet) is WRONG**: coupling is inherently Z-dependent via L-edge detuning
- **The 4π/N_single² formula is WRONG** (or at best, structurally incomplete): the correct formula would involve atomic-resonance matrix elements, not crystal-lattice atom count
- **The 0.6% DAMA match is NUMERICAL COINCIDENCE**: not a physical derivation
- **Cross-detector predictions for Sapphire/HPGe (1.03×, 1.15× DAMA) are WRONG**: should predict near-zero from absence of L-edge resonance

This would be a **substantial walk-back** of the matched-LC-coupling work landed earlier this session.

### §4.5 — Alternative: matched-LC-coupling really IS bulk-crystal physics

If the canonical κ_entrain template applies (which it should per Sagnac-RLVE):
- $\kappa_{entrain}^{NaI} = 4.63 \times 10^{-4}$
- Predicted DAMA rate (4π/N² × κ_entrain): $2.2 \times 10^{-10}$ events/s/kg
- vs observed $4.77 \times 10^{-7}$ events/s/kg: framework UNDERPREDICTS by 2000×

For the matched-LC-coupling framework to be consistent with both DAMA observation AND canonical κ_entrain template, there must be an ADDITIONAL ENHANCEMENT factor ~2000× beyond what 4π/N² × κ_entrain provides:

$$\epsilon_{det}^{required} = \kappa_{entrain} \times \frac{4\pi}{N_{single}^2} \times \text{Enhancement}_{2000}$$

What physical mechanism provides 2000× enhancement? Candidates:
- Bragg-like coherent enhancement at NaI lattice spacing matching λ_slew (the second-order Bragg condition gives factor ~$N_{Bragg}^2$ enhancement where $N_{Bragg}$ is the coherent baseline)
- Atomic resonance enhancement near L-edges (as in §4.3)
- Crystal-quality coherent-Q enhancement
- Some combination

**None of these are derived from first-principles AVE canonical physics.** The 2000× factor would be a phenomenological adjustment.

## §5 — Empirical constraints summary

| Observation | Required $\epsilon_{det}$ per electron-cycle | Interpretation |
|---|---|---|
| DAMA NaI(Tl) observed rate $4.77 \times 10^{-7}$ events/s/kg | $2.06 \times 10^{-51}$ | $4\pi/N_{single}^2$ at κ=1 matches by coincidence |
| MAJORANA HPGe implicit null at 3.728 keV | $\lesssim 10^{-52}$ | HPGe has factor ~20+ lower coupling than NaI |
| COSINE-100 NaI null | $\lesssim 10^{-52}$ | Lower-quality NaI batches don't reproduce DAMA |
| ANAIS-112 NaI null | $\lesssim 10^{-52}$ | Same as COSINE |

**Cross-detector tension is real.** Whatever mechanism mediates the DAMA signal varies by factor 20-100 across detector classes. The matched-LC-coupling formula doesn't constrain this variation without specifying the physical mechanism.

## §6 — Plumber questions to surface to Grant

Per the `pre-test-physics-check` skill discipline (mandatory single plumber-physical question before next-session test design), surface these to Grant before continuing:

### Question 1 (load-bearing): What is the canonical AVE energy-transfer mechanism from substrate-mode at frequency ν to matter at temperature T?

The corpus has:
- κ_entrain = ρ_matter / ρ_bulk for momentum/velocity transfer (Sagnac-RLVE)
- Op17 T² = 1 - Γ² for matched-impedance power transmission
- κ_crystal G > 0 binary gate for solid-vs-liquid

But **NO canonical formula for energy absorption rate at a specific substrate-mode frequency.** This is the foundational gap.

Without this, the matched-LC-coupling formula is hand-waving the actual physics.

**Sub-question 1a**: Is the energy transfer mediated by:
- (i) Bulk crystal LC modes (the matched-LC formula's implicit assumption)?
- (ii) Atomic inner-shell resonances (the atomic-physics picture from §4.3)?
- (iii) Phonon-electron coupling at the substrate refresh rate (the original refresh-rate prereg framing from before the α-slew reframing)?
- (iv) Something else entirely?

### Question 2: Does the canonical κ_entrain template (ρ_matter / ρ_bulk) apply to DAMA-class matched-coupling, or is DAMA-class coupling structurally different from Sagnac-RLVE class?

If κ_entrain applies, the formula must include it and DAMA observed rate requires factor 2000× enhancement somewhere. If κ_entrain doesn't apply, what's the canonical alternative coupling template for energy-frequency-resonance coupling?

### Question 3 (audit-honest): Was the 0.6% match a numerical coincidence?

Given:
- Required ε_det $\sim 10^{-51}$
- 5 canonical AVE prefactors (π, 2π, π², 4π, 4π³) all within factor 10 of required when paired with 1/N²
- α^N candidates at N=22-26 also within factor 10
- (α/2π)^N candidates at N=15-19 also within factor 10
- Formula-space DENSITY is high at the required magnitude

**Probability that one candidate lands within 1% of required by pure coincidence: rough estimate ~30-50% (5 prefactors × 0.01 each + α-power candidates).**

The 0.6% match looks impressive but might be a SELECTION-EFFECT artifact of trying many formulas until one fits. **Per `ave-discrimination-check` skill, this is exactly the failure mode the skill is supposed to catch.**

## §7 — What this means for the κ_quality bounded-scope derivation

**RECOMMENDATION: PAUSE κ_quality bounded-scope derivation pending plumber-physical adjudication of Questions 1-3.**

The κ_quality framework derivation assumes:
- The matched-LC formula's $1/N_{single}^2$ scaling is correct
- κ_quality is a multiplicative factor on this scaling
- Cross-detector variation can be explained by κ_quality alone

If §4-§6 above reveal that the matched-LC formula is structurally wrong (Question 1 returns "atomic physics, not bulk LC"), then κ_quality is not the right framework — element-specific resonance matrix elements would be.

If Question 1 returns "canonical AVE κ_entrain × (4π/N²)" but the factor 2000× enhancement isn't identified, then κ_quality framework is incomplete — needs the enhancement-factor mechanism specified first.

**Bounded-scope κ_quality work as currently planned is therefore PREMATURE.** The audit findings need adjudication before it can proceed productively.

## §8 — Implications for the HPGe + Sapphire experimental proposals

Both experimental proposals' predicted rates are derived from the matched-LC-coupling formula. If the formula is structurally wrong, the predicted rates are wrong.

**Honest scope for the HPGe proposal**: the experiment STILL TESTS the AVE matched-LC framework, because either:
- A 3.728 keV peak IS observed at predicted rate → matched-LC formula correct (validates 4π/N² and κ assumption)
- A 3.728 keV peak NOT observed → matched-LC formula wrong OR κ_HPGe is much smaller than 1

Either outcome is informative. The proposal itself remains valid as a falsifier specification.

**But**: the proposal's HEADLINE predicted rate (1.03× DAMA at 3.728 keV) is conditioned on κ_HPGe = 1 in the 4π/N² formula. If the actual physics is atomic-resonance-mediated, HPGe predicted rate is much smaller (near-zero), and MAJORANA's null is consistent with the framework after all.

The proposals should add an HONEST-SCOPING note: "predicted rate is from the matched-LC-coupling formula which has a structural gap (not yet derived from canonical AVE physics); a null result at predicted rate could mean either κ_HPGe << 1 OR the formula is wrong."

## §9 — Discipline meta-observation

**I created the `ave-canonical-leaf-pull` skill specifically to catch the failure mode "the corpus had the answer for N audit cycles before pulling it in." Then I IMMEDIATELY violated the skill by deriving the matched-LC-coupling formula WITHOUT pulling in the canonical κ_entrain template from Sagnac-RLVE.**

The skill exists; I had it; I didn't use it.

This is the canonical "physician, heal thyself" failure mode. The skill ensemble is structurally complete only if I actually invoke the skills on my own work.

**Add to ave-canonical-leaf-pull SKILL.md**: explicit reminder that the skill applies to AGENT'S OWN NEW DERIVATIONS, not just to literature reviews. Self-application of the discipline is the failure mode pattern.

## §10 — Recommended next-session sequencing (REVISED post-audit)

**Before any κ_quality work**:

1. **Adjudicate plumber questions §6** with Grant — this is the gating-step
2. **Read the canonical Vol 4 Ch 1 leaves more carefully** — specifically check whether the corpus has any formula for energy-transfer-rate-per-frequency that I haven't pulled in
3. **Walk back the dama-matched-lc-coupling KB leaf** if Question 3 returns "yes, numerical coincidence" — demote from "candidate formula" to "candidate formula with structural gap"
4. **Update HPGe + Sapphire proposals** with the honest-scoping note from §8
5. THEN if a derived formula exists, the κ_quality bounded-scope derivation can proceed

Per `ave-discrimination-check` discipline applied to my own work: the matched-LC-coupling 0.6% match landed earlier this session was probably overclaimed. The honest-scoping correction needs to extend to "we have a numerical coincidence with structural gaps" framing rather than "candidate formula with cross-detector forward predictions."

## §11 — Cross-references

- **Framework under audit**: [`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md) — matched-LC-coupling derivation
- **Canonical κ_entrain template**: [`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) line 14-26
- **Canonical Op17 power transmission**: [`manuscript/ave-kb/common/operators.md`](../manuscript/ave-kb/common/operators.md) Op17 (line 47)
- **Reactive-power physical picture**: [`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) §12
- **MAJORANA discovery pass**: [`research/2026-05-17_MAJORANA-legacy-discovery-pass.md`](2026-05-17_MAJORANA-legacy-discovery-pass.md)
- **HPGe + Sapphire proposal**: [`research/2026-05-17_HPGe-9.39kg-experimental-proposal.md`](2026-05-17_HPGe-9.39kg-experimental-proposal.md)
- **Discipline skill that I should have applied**: `ave-canonical-leaf-pull` (`~/.claude/skills/ave-canonical-leaf-pull/SKILL.md`)
- **Discipline skill that flags this pattern**: `ave-discrimination-check` Class B (post-hoc structural-form-fitting)

## §12 — Lane attribution

Audit research doc landed on `analysis/divergence-test-substrate-map` branch as step-back-as-plumber per Grant directive. **Identifies structural gap in matched-LC-coupling formula**: missing canonical κ_entrain template + 2000× unexplained enhancement OR atomic-resonance physical mechanism not specified. **Surfaces three plumber questions to Grant** for adjudication before κ_quality bounded-scope derivation proceeds. **Honest meta-observation**: failed to invoke own newly-created `ave-canonical-leaf-pull` skill on my own derivation; skill ensemble works only if self-applied.

The matched-LC-coupling work landed earlier this session was probably overclaimed in its "0.6% post-hoc consistency check" framing. The proper framing per this audit is "0.6% numerical coincidence with structural gaps requiring plumber-physical adjudication of the energy-transfer mechanism."
