# C14-DAMA Q-Factor: Matched-LC-Coupling Derivation Result

**Status:** PARTIAL CLOSURE 2026-05-17 night via 9th-cycle reactive-power resolution + structural-candidate evaluation. Striking numerical match to DAMA at $\epsilon_{det} = 4\pi / N_{single}^2$ within 0.6% — but the prefactor 4π is post-hoc selected from canonical AVE candidates {4π, 2π, π}, so the result is structurally-suggestive NOT first-principles-derived. Cross-detector test (DAMA vs COSINE-100 vs ANAIS-112) is the load-bearing falsifier.

**Date:** 2026-05-17 night
**Matrix row:** C14-DAMA-MATERIAL (rate magnitude)
**Driver:** [`src/scripts/vol_3_macroscopic/derive_dama_matched_lc_coupling.py`](../src/scripts/vol_3_macroscopic/derive_dama_matched_lc_coupling.py)
**Prior chain:** [`research/2026-05-17_C14-DAMA_amplitude_prereg.md`](2026-05-17_C14-DAMA_amplitude_prereg.md) → [`amplitude_result.md`](2026-05-17_C14-DAMA_amplitude_result.md) → [`audit_walk-back.md`](2026-05-17_C14-DAMA_audit_walk-back.md) (8th cycle) + 9th cycle resolution at source leaf §12 → [`Q-factor_prereg_and_derivation.md`](2026-05-17_C14-DAMA_Q-factor_prereg_and_derivation.md) → THIS RESULT

## §1 — Headline numerical match

| Quantity | Value |
|---|---|
| Required per-cycle matched-coupling efficiency $\epsilon_{det}^{required}$ | $2.0568 \times 10^{-51}$ |
| Structural candidate $4\pi / N_{single}^2$ | $2.0685 \times 10^{-51}$ |
| **Ratio (candidate / required)** | **1.0057 = 0.6% match** |

Where:
- $N_{single} = 9.7\,\text{kg} \times (N_A / M_{NaI}) \times 2 = 7.79 \times 10^{25}$ atoms in a single coherent DAMA/LIBRA Phase-2 crystal (Bernabei et al. published 9.7 kg per crystal × 25 crystals total)
- $4\pi = 12.566$ is the canonical AVE spinor double-cover / solid-angle factor (appears in Theorem 3.1' as $Z_{\text{radiation}} = Z_0 / (4\pi)$ per spinor cycle)

## §2 — Physical picture

**Per-cycle matched-coupling efficiency** between the electron's reactive LC tank (per Theorem 3.1' canonical $Q = \alpha^{-1}$ at the TIR boundary, with per-cycle reactive leak $\alpha m_e c^2 = 3.728$ keV at 90° phase) and an external coherent NaI crystal LC mode at the α-slew operating point:

$$\epsilon_{det} = \frac{4\pi}{N_{single}^2}$$

Physical interpretation:
- $1 / N_{single}^2$: probability that all $N_{single}$ atomic phase-elements simultaneously align with the electron's α-slew phase + reflected-phase pair (two-tank coupled-phase alignment, squared)
- $4\pi$: spinor double-cover solid-angle factor per spinor cycle (SU(2) double-cover of SO(3), per Vol 1 Ch 8 §3.2; same 4π that appears in Theorem 3.1' as the per-cycle impedance reference)

**Rate per kg** (assembled from canonical AVE factors):

$$R_{DAMA-predicted} = N_e^{(kg)} \times \nu_{slew} \times \frac{4\pi}{N_{single}^2}$$

where:
- $N_e^{(kg)} = (Z_{Na} + Z_I) \times N_A / M_{NaI} = 64 \times 4.01 \times 10^{24} = 2.57 \times 10^{26}$ electrons/kg
- $\nu_{slew} = \alpha c / (2\pi \ell_{node}) = 9.02 \times 10^{17}$ Hz (canonical α-slew rate)

Numerical evaluation:
$$R_{DAMA-predicted} = 2.57 \times 10^{26} \times 9.02 \times 10^{17} \times 2.07 \times 10^{-51} = 4.80 \times 10^{-7}\,\text{events/s/kg}$$

DAMA observed: $4.77 \times 10^{-7}$ events/s/kg (Phase-2, 2-6 keV window integrated). **Ratio: 1.006 = 0.6% match.**

## §3 — Honest discrimination-check (per ave-discrimination-check skill)

The 0.6% match is striking but requires the following honest caveats:

### §3.1 — Post-hoc prefactor selection

The 4π prefactor was selected AFTER seeing that $N_{single}^{-2}$ alone landed factor 12.6 low. Three canonical AVE O(10) prefactors all appear in Theorem 3.1' α-decomposition:
- $\Lambda_{vol} = 4\pi^3 \approx 124$ (3D volume integral)
- $4\pi \approx 12.57$ (spinor double-cover full cycle)
- $\Lambda_{surf} = \pi^2 \approx 9.87$ (2D surface integral)
- $2\pi \approx 6.28$ (Hoop Stress geometric factor / orbital period)
- $\Lambda_{line} = \pi \approx 3.14$ (1D line integral)

Of these, **4π is the one that lands within 1% of required**. The others land within OOM:

| Prefactor | $\epsilon_{candidate}$ | Ratio to required |
|---|---|---|
| $4\pi / N^2$ | $2.07 \times 10^{-51}$ | **1.006** |
| $2\pi / N^2$ | $1.03 \times 10^{-51}$ | 0.503 |
| $\pi^2 / N^2$ | $1.62 \times 10^{-51}$ | 0.790 |
| $\pi / N^2$ | $5.17 \times 10^{-52}$ | 0.251 |
| $4\pi^3 / N^2$ | $2.04 \times 10^{-50}$ | 9.93 |

The 4π match could be:
- (a) **Genuinely structurally correct**: spinor double-cover is the right physical mechanism (electron coupling to external receiver requires full 4π solid-angle phase coverage per cycle)
- (b) **Coincidental**: of the 5 canonical candidates, one landed within 1% by chance (probability ~20% if all are physically valid)

Without independent derivation of why 4π specifically (not 2π or π²), the match is structurally-suggestive NOT first-principles-derived.

### §3.2 — Cross-detector test (the load-bearing falsifier)

If $\epsilon_{det} = 4\pi / N_{single}^2$ is structurally correct, then **rate per kg scales as** $1/M_{single}^2$ where $M_{single}$ is the **per-crystal mass** (NOT per-detector total mass).

Predicted relative rates per kg, normalized to DAMA:

| Detector | $M_{single}$ (kg) | Predicted rate/kg ratio to DAMA |
|---|---|---|
| **DAMA/LIBRA Phase-2** | 9.7 | 1.000 (baseline) |
| **COSINE-100** | ~10 | $(9.7/10)^2 = 0.940$ |
| **ANAIS-112** | ~12.5 | $(9.7/12.5)^2 = 0.602$ |

**Empirical reality**:
- COSINE-100 and ANAIS-112 both DO NOT observe DAMA's annual modulation signal at the predicted ratios
- COSINE-100 limit: $\sim 0.1 \times$ DAMA modulation amplitude (much lower than predicted 0.94×)
- ANAIS-112 limit: similar exclusion (much lower than predicted 0.60×)
- This is a long-standing dark-matter detection puzzle

**The cross-detector tension means** the simple $4\pi / N_{single}^2$ formula is NOT a complete derivation. Either:
- (a) The 4π/N² match is coincidental (cross-detector falsifies it)
- (b) The formula is correct in form but requires a crystal-quality factor $\kappa_{quality} \ll 1$ for COSINE/ANAIS (these batches have lower true coherence volume than the DAMA Beam International high-quality crystals)
- (c) Some other detector-specific factor (purity, growth-process, thermal annealing) dominates

The DAMA prereg framework already invokes (b) — the binary $\Theta(\text{coherent shear support})$ gate with continuous modulation by crystal-quality factors (defect density, mosaicity, grain boundaries). The 4π/N² match would then represent a **theoretical ceiling** that only highest-quality DAMA-batch crystals approach.

### §3.3 — Mass-scaling test (cleaner discriminator)

If $\epsilon_{det} \propto 1/M_{single}^2$ at fixed $\kappa_{quality}$, then within a single detector campaign using **same-batch crystals of different masses**, the per-kg rate should track $1/M_{single}^2$. This is testable and would isolate the mass-scaling claim from the crystal-quality confound.

Specifically: DAMA's 25 crystals are NOT all exactly 9.7 kg (manufacturing variation). If the per-crystal masses are published with their per-crystal rates, the within-DAMA cross-crystal scaling test could discriminate.

### §3.4 — Z-independence claim consistency check

The §11 walk-back claim "Z-INDEPENDENCE: substrate-rate predicts same line in NaI, Sapphire, Ge" remains consistent with $\epsilon_{det} = 4\pi / N_{single}^2$:
- For any crystal at same $M_{single}$ but different Z-composition, $N_{single}$ scales as $1/M_{NaI-equivalent-molar-mass}$
- Sapphire $\text{Al}_2\text{O}_3$ at 9.7 kg: M_mol = 0.102 kg/mol, N_single = 9.7 × 6.02e23 / 0.102 × 5 = 2.87e26 atoms (5 atoms/molecule)
- Predicted: $\epsilon = 4\pi / (2.87 \times 10^{26})^2 = 1.52 \times 10^{-52}$
- Predicted Sapphire rate/kg ratio to DAMA at same $\kappa_{quality}$: $(7.79 \times 10^{25} / 2.87 \times 10^{26})^2 = 0.074$ — Sapphire detection rate per kg would be ~13× LOWER than DAMA per kg

Wait — this contradicts the §11 Z-independence claim. Let me think again.

Actually: the §11 Z-independence claim was about the LINE POSITION (3.728 keV regardless of Z), NOT the line AMPLITUDE. The line AMPLITUDE per kg depends on N_atoms per kg via the matched-coupling formula. Sapphire has 5 atoms per molecule vs NaI's 2, so N_atoms per kg is different.

Reframing: **AVE predicts (line at 3.728 keV) AND (amplitude scaling as 4π / N_atoms²)** for any solid coherent crystal. Both predictions are AVE-distinct from Moseley (which predicts different line positions for different Z) and from WIMP-class fits (which predict per-detector fitted cross-sections).

Cross-crystal test: Sapphire and Ge at same $M_{single}$ should give same 3.728 keV LINE POSITION but different per-kg AMPLITUDES governed by their atomic count per kg.

This sharpens the AVE-distinct claim. The line-position invariance is universal; the amplitude scaling is structural.

## §4 — Status and lifecycle

| Component | Status | Notes |
|---|---|---|
| Reactive-power categorical reframe (9th cycle) | **CONFIRMED** | Three canonical Vol 4 Ch 1 leaves explicit + §12 of DAMA leaf documents the picture |
| Structural form $\epsilon_{det} = C/N_{single}^2$ where $C = O(10)$ canonical prefactor | **STRUCTURALLY SUGGESTIVE** | Within factor 13 of required for $C = 1$; within factor 5-1 for canonical AVE prefactors {π, 2π, π², 4π} |
| Specific prefactor $C = 4\pi$ | **POST-HOC SELECTED; 0.6% MATCH** | One of 5 canonical candidates; lands closest but selected after seeing target |
| Cross-detector mass-scaling prediction $R/M \propto 1/M_{single}^2$ | **TESTABLE (currently DISFAVORED by COSINE/ANAIS nulls)** | Requires $\kappa_{quality} < 1$ for COSINE/ANAIS to recover null |
| Cross-crystal Z-independence (line position) | **TESTABLE, UNTESTED** | Same 3.728 keV line in NaI, Sapphire, Ge at $4\pi \kappa / N_{atoms}^2$ amplitude |
| CMB-velocity phase-lock | **CONFIRMED by DAMA** | June peak day-of-year ~152 |
| Solid-vs-liquid binary gate | **CONFIRMED** | DAMA NaI+ + XENONnT- |

## §5 — Honest scope statement

The session work has achieved:

1. **Categorical reframe (9th cycle)**: α m_e c² is reactive power, not photoabsorption quantum. The 22-α-power "out of reach" framing from 8th cycle was wrong category.

2. **Structural form identification**: $\epsilon_{det} \propto 1/N_{single}^2$ is the load-bearing scaling for matched-LC-coupling between electron LC tank and external coherent crystal. Within factor 13 of required without any prefactor.

3. **Striking numerical coincidence**: With $C = 4\pi$ (one of 5 canonical AVE O(10) prefactors), the formula matches DAMA observed within 0.6%. This is consistent with first-principles derivation but NOT yet derived from first principles.

The session work has NOT achieved:

1. **First-principles derivation of the 4π prefactor**. The 4π is post-hoc selected from canonical candidates; no canonical derivation chain forces it over 2π or π².

2. **Cross-detector consistency check**. The simple 4π/N² formula predicts rates for COSINE/ANAIS that exceed their published nulls — requires either κ_quality reductions or formula modification.

3. **First-principles N_single derivation**. The "single coherent crystal" is defined by experimental detector geometry (9.7 kg per crystal) rather than derived from AVE substrate physics. A natural AVE coherence length would derive N_coh from substrate parameters; this hasn't been done.

## §6 — Next-session work

To upgrade this from "structurally suggestive" to "forward-prediction CONFIRMED":

1. **Derive the 4π prefactor from independent physics** — show why 4π specifically appears in matched-LC-coupling at the electron α-slew TIR boundary (vs 2π Hoop Stress or π² surface integral). Canonical candidate: spinor double-cover of SO(3) per Vol 1 Ch 8 §3.2 + Theorem 3.1' Z_0/(4π) per-cycle impedance reference.

2. **Derive N_single from substrate physics** — show what determines the coherent-crystal mass scale that enters the formula. Candidate: AVE coherence length × κ_quality limits to single-crystal grain size.

3. **Cross-detector mass-scaling fit** — if DAMA crystals have varying masses (manufacturing variation), fit the within-DAMA per-crystal rate against per-crystal mass. Confirms or refutes the 1/M² scaling cleanly.

4. **Cross-crystal swap design** — propose Sapphire or Ge detector experiment with appropriate per-crystal mass to test Z-independence (line position) + N⁻² scaling (amplitude).

5. **Crystal-quality factor κ_quality derivation** — corpus has the binary-gate framework from prereg; need quantitative model for κ < 1 in lower-quality batches.

## §7 — Matrix row status update (proposed)

C14-DAMA-MATERIAL rate magnitude:
- Pre-9th-cycle: U-D-PAUSED (8th cycle "out of reach")
- Post-9th-cycle: **U-D-structurally-suggestive-pending-prefactor-derivation-and-cross-detector-consistency**

NOT promoted to U-C because:
- 4π prefactor is post-hoc selected
- Cross-detector tension (COSINE/ANAIS) unresolved
- N_single is empirically defined, not substrate-derived

The 0.6% match is the strongest quantitative result of the α-slew thread to date, but per `ave-discrimination-check` discipline cannot be claimed as closure without independent prefactor derivation.

## §8 — Cross-references

- **Derivation script**: [`src/scripts/vol_3_macroscopic/derive_dama_matched_lc_coupling.py`](../src/scripts/vol_3_macroscopic/derive_dama_matched_lc_coupling.py)
- **Source leaf §12 reactive-power physical picture**: [`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) §12
- **Canonical electron-tank Q-factor (4π origin)**: [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md)
- **Canonical reactive-power table**: [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) line 31
- **8th cycle walk-back**: [`research/2026-05-17_C14-DAMA_audit_walk-back.md`](2026-05-17_C14-DAMA_audit_walk-back.md)
- **9th cycle reactive-power resolution skill**: [`~/.claude/skills/ave-power-category-check/SKILL.md`](~/.claude/skills/ave-power-category-check/SKILL.md)
- **Matrix row**: [`manuscript/ave-kb/common/divergence-test-substrate-map.md` C14-DAMA-MATERIAL](../manuscript/ave-kb/common/divergence-test-substrate-map.md)

## §9 — Lane attribution

Derivation work landed on `analysis/divergence-test-substrate-map` branch. Driver script computes 14 structural candidates spanning {α^N, (α/2π)^N, N^(-2), geom-overlap, mean-free-path, Bragg-detuning, canonical-prefactor × N⁻²}. Best-fit candidate ($4\pi / N_{single}^2$, 0.6% match) is reported with full discrimination-check caveats per `ave-discrimination-check` skill. 9th audit cycle on α-slew thread continues.
