# κ_quality Tl-Dopant First-Pass — Result: Outcome C (Cascade-Level Misdirection)

**Date:** 2026-05-17 night
**Status:** Outcome C — derivation NOT attempted; corpus-grep revealed cascade-level misdirection
**Prereg:** [`2026-05-17_kappa-quality-tl-dopant-first-pass-prereg.md`](2026-05-17_kappa-quality-tl-dopant-first-pass-prereg.md) (21:00 timestamp)
**Triggering audit recommendation:** "assemble CTG-1 + CTG-2 + CTG-4 into a first-attempt for Tl-dopant 6s² inert pair role in NaI(Tl)/CsI(Tl). That's a one-session attempt with existing framework"

## §1 — Headline finding: Foundation Item 11 pattern

**The auditor recommendation was made WITHOUT cross-referencing today's-date research docs from earlier in the same session.** Six load-bearing research docs landed between 13:06 and 16:18 on 2026-05-17 — all 4.5-8 hours BEFORE my prereg — that already addressed κ_quality at the load-bearing cascade level:

1. [`2026-05-17_C14-DAMA_Q-factor_matched-LC-coupling_result.md`](2026-05-17_C14-DAMA_Q-factor_matched-LC-coupling_result.md) — 13:17
2. [`2026-05-17_DAMA-bulk-transfer-function-reframe.md`](2026-05-17_DAMA-bulk-transfer-function-reframe.md) — 14:36
3. [`2026-05-17_KIMS-CsI-Tl-discovery-pass.md`](2026-05-17_KIMS-CsI-Tl-discovery-pass.md) — 14:36
4. [`2026-05-17_parametric-coupling-kernel-derivation-steps-1-3.md`](2026-05-17_parametric-coupling-kernel-derivation-steps-1-3.md) — 15:04
5. [`2026-05-17_parametric-coupling-kernel-derivation-steps-4-9.md`](2026-05-17_parametric-coupling-kernel-derivation-steps-4-9.md) — 15:19
6. [`2026-05-17_KIMS-MAJORANA-quantitative-bounds.md`](2026-05-17_KIMS-MAJORANA-quantitative-bounds.md) — 15:52
7. [`2026-05-17_kappa-quality-correlation-first-pass-scoping.md`](2026-05-17_kappa-quality-correlation-first-pass-scoping.md) — 16:18

These docs already DERIVED the parametric coupling kernel ε_det = 4π × κ_quality / N² from first principles, structurally defined the κ_quality envelope, refined cross-detector bounds, and did first-pass empirical correlation scoping. The Tl-dopant first-pass I was about to attempt would have been at the WRONG cascade level.

This is **Foundation Item 11 pattern**: same as FI-8 (cross-repo grep failure) and FI-6 (historical-research grep failure), but applied to **same-session research/ scope**. Corpus-grep MUST include `research/2026-05-17_*.md` glob when adjudicating κ_quality-related work BEFORE recommending any first-pass attempt.

## §2 — What the corpus actually says about κ_quality

### §2.1 — Cascade structure (derived 2026-05-17 day, NOT new)

The parametric coupling kernel decomposes detection rate into THREE cascade levels:

```
R_detect = J_substrate^bulk × σ_atomic(Z) × η_scintillation
            \________ε_det = 4π κ/N² _________/
                  (BULK + COUPLING level)
```

- **Bulk substrate-mode level** (Z-INDEPENDENT): ε_det = 4π × κ_quality / N²
  - 4π from spinor-cycle averaging (Theorem 3.1' Z_radiation = Z₀/(4π))
  - 1/N² from Dicke amplitude (1/N) × matched-cycle synchronization (1/N)
  - κ_quality structurally: = 1 for deep regenerative (Q·δ ≫ 2), = (Qδ/2)² for sub-regenerative
- **Atomic photoabsorption level** (Z-DEPENDENT): σ_atomic at 3.728 keV per detector chemistry
- **Scintillation/readout level**: η_scintillation = light output per absorbed photon (Tl-dopant role IS HERE)

**The Tl-dopant in NaI(Tl) and CsI(Tl) operates at level 3 (scintillation cascade), NOT at level 1 (κ_quality cascade).** Tl provides scintillation centers (recombination luminescence efficiency). It does NOT modify the parametric coupling efficiency.

### §2.2 — κ_quality regimes (derived from Q·δ regenerative threshold)

| Apparatus | Q | Q·δ_C (with δ_C = 0.0457) | κ_quality | Source |
|---|---|---|---|---|
| NaI(Tl) room-T | ~10³ | 45.7 | = 1 (deep regenerative, ceiling) | derivation steps-4-9 §6 |
| CsI(Tl) room-T | ~10³ | 45.7 | = 1 (deep regenerative, ceiling) | same |
| HPGe room-T | ~10⁴ | 457 | = 1 (deep regenerative, ceiling) | same |
| Sapphire cryo | ~10⁹ | 4.57×10⁷ | = 1 (extreme regenerative) | same |
| Xe(l) liquid | ~10⁰-10¹ | 0.046-0.46 | = (Q·δ/2)² ~ 10⁻⁴-10⁻² | same |

**Theoretical ceiling for all solid crystalline detectors: κ_quality = 1.** No Tl-dopant lone-pair Q-factor boost is needed for the structural derivation — the parametric framework already delivers κ_quality = 1 from the regenerative-regime calculation.

### §2.3 — Empirical κ_quality variation (the actual open question)

| Detector | κ_quality (empirical, refined 2026-05-17 night) | Source |
|---|---|---|
| DAMA NaI(Tl) Beam International | ≈ 1 (matches DAMA observed rate at 0.6% derived match) | derivation steps-4-9 §7.2 |
| COSINE-100 NaI(Tl) | ≲ 0.4 (from null at DAMA-equivalent sensitivity) | derivation steps-4-9 §9.2 |
| ANAIS-112 NaI(Tl) | ≲ 0.4 (from null) | same |
| KIMS CsI(Tl) | ≲ 0.02-0.05 (3σ rough, refined) | KIMS-MAJORANA bounds §1.4 |
| MAJORANA HPGe | ≲ 10⁻³ to 10⁻⁴ (3σ rough, refined) | KIMS-MAJORANA bounds §2 |
| XENONnT Xe(l) | (sub-regenerative; derived ~0) | derivation steps-4-9 §6.2 |

**Cross-detector variation spans 50× within rock-salt+Tl class (DAMA vs KIMS) and 5000× across lattice classes (DAMA vs HPGe).** This variation MUST be explained by materials-science crystal-quality metrics for framework integrity (parametric-coupling-kernel.md §9 Falsifier #2).

### §2.4 — First-pass empirical correlation scoping (16:18 timestamp)

The correlation-scoping doc found:
- **Light yield ANTICORRELATES with κ_quality** across DAMA/COSINE/ANAIS (DAMA has LOWEST light yield + κ=1; COSINE/ANAIS have 2-3× HIGHER light yield + κ<1)
- Light yield is therefore NOT a relevant κ_quality proxy (different physics)
- Need non-optical metrics: X-ray rocking curve FWHM (mosaicity), TEM defect density, Brillouin-scattering at THz (phonon coherence length), Tl-dopant uniformity maps
- **This data does NOT exist in published dark-matter literature** — typically reports light yield + radio-purity only, not lattice-quality metrics
- **Framework status: NOT YET FALSIFIABLE on this data class** (load-bearing data doesn't exist in publicly available form)
- Multi-session materials-science literature dive + detector-collaborator engagement needed for full empirical grounding

## §3 — Why the Tl-dopant first-pass would have been misdirected

### §3.1 — Wrong cascade level

My prereg pre-registered:
> "Tl 6s² inert pair acts as a lone-pair Q-factor analog. The lone-pair Q-factor multiplies the local coupling: each Tl site acts as a Q-amplifier for the cycle-12 substrate AC, raising the effective κ_quality at the dopant by ~Q_Tl/Q_baseline ~ 10³-10⁴."

The corpus says: **κ_quality is structurally = 1 for ALL solid crystalline detectors in deep regenerative regime** (Q·δ ≫ 2 satisfied for NaI(Tl), CsI(Tl), HPGe, Sapphire). No Tl-dopant multiplier is needed for the theoretical ceiling. The Tl role in NaI(Tl) operates at scintillation cascade (Q-amplification of light-output), not at κ_quality cascade (parametric coupling efficiency).

### §3.2 — Wrong falsifier target

My prereg's pre-registered outcomes:
- "Outcome A: framework SURVIVES if κ_NaI(Tl) end-to-end derivation matches ~10⁻² order needed for DAMA ε_det"
- "Outcome B: framework partially holds — Tl mechanism works but cross-element scaling fails"  
- "Outcome C: η_Tl does NOT cleanly derive from 6s² inert pair angular phase using existing CTG-1/2/4 pieces"

The corpus says: **κ_NaI(Tl) doesn't need to derive end-to-end** — the framework's ε_det = 4π / N² formula matches DAMA at 0.6% with κ_quality = 1 (structural ceiling). The actual open question is the CROSS-DETECTOR variation explanation via materials-science metrics, NOT a per-element Tl-dopant lone-pair derivation.

### §3.3 — CTG-4 (lone-pair Q-factor η_lp = 1/9) is sp³-specific, not transferable to 6s²

Even if I had attempted the derivation: η_lp = cos²(109.5°) = 1/9 derives from sp³ tetrahedral hybridization (Vol 5 organic-circuitry, [`first-principles-bond-force-constants.md:119-128`](../manuscript/ave-kb/vol5/molecular-foundations/organic-circuitry/first-principles-bond-force-constants.md)). The Tl 6s² inert pair is L=0 (spherically symmetric, no angle to take cos² of) — fundamentally different orbital topology. CTG-4 isn't transferable to Tl without separate derivation work (relativistic 6s contraction, lanthanide contraction analog, etc.), and that derivation work isn't in the corpus.

### §3.4 — CTG-1 (per-element Z_atom table) only extends to Z=14

Even if the cascade-level were correct: per-element Z_atom impedance values are only tabulated for Z=1-14 ([`per-element-impedance-table.md:39-54`](../manuscript/ave-kb/vol3/condensed-matter/ch10-material-properties/per-element-impedance-table.md)). Tl (Z=81), I (Z=53), Ge (Z=32) are NOT in the table. The heavy-element catalog at [`vol6/appendix/heavy-element-catalog/full-element-table.md`](../manuscript/ave-kb/vol6/appendix/heavy-element-catalog/full-element-table.md) has MASS DEFECT predictions for these elements but NOT Z_atom impedance values. Heavy-element Z_atom extension is genuine multi-session work.

### §3.5 — Compound issue: the auditor's recommendation was internally consistent BUT didn't cross-reference 7 today's-date research docs

The auditor's logic was: "CTG-1 + CTG-2 + CTG-4 pieces exist; assemble them for Tl-dopant first-pass." That logic is correct IF the κ_quality cascade level were the right target. But the corpus shows κ_quality is already structurally derived at = 1, and the Tl-dopant operates at a different cascade level. The auditor missed this because the corpus-grep at audit time didn't include same-session `research/2026-05-17_*.md` scope.

## §4 — Outcome C declaration

**This is Outcome C per the prereg's discriminating outcomes table — but for a SUBTLY DIFFERENT reason than the prereg anticipated.**

Prereg expected: "η_Tl cannot be derived from existing CTG pieces without invoking a parameter that doesn't itself derive from CTG."

Actual outcome: **Tl-dopant doesn't enter the κ_quality cascade level at all. The κ_quality framework is already structurally derived (κ = 1 for deep regenerative regime). The open question is cross-detector variation explanation via materials-science metrics, not a per-element Tl-dopant first-pass.**

### §4.1 — Net framework state (post-attempt)

The κ_quality framework is in the following state:
- **Leading-order derivation: CLOSED** (parametric-coupling-kernel-derivation-steps-1-9.md, Outcome A confirmed)
- **DAMA quantitative match: DERIVED** (0.6%, no longer post-hoc)
- **XENONnT null: DERIVED** (sub-regenerative regime Q·δ < 2)
- **Cross-detector empirical bounds: REFINED** (KIMS κ ≲ 0.02-0.05; MAJORANA κ ≲ 10⁻³-10⁻⁴)
- **κ_quality cross-detector variation explanation: GENUINELY OPEN** (multi-session materials-science literature dive + detector-collaborator engagement needed)
- **Framework status: SURVIVES first-pass tests; NOT YET FALSIFIABLE on κ_quality grounding** (load-bearing data class doesn't exist in publicly available form)

### §4.2 — What this attempt produced (positive output)

- **Foundation Item 11 finding**: corpus-grep failure mode — agent recommended derivation attempt without cross-referencing same-session research/ scope; same pattern as FI-6 (historical) and FI-8 (cross-repo)
- **Confirmation**: the κ_quality framework's structural derivation is robust (no derivation gap requires Tl-dopant lone-pair analog)
- **Identification**: the actual open work is materials-science correlation (Tier-2 #9 work pending), not per-element first-pass derivation
- **Sharpened scope**: the "1-session closure" candidate for κ_quality work is actually the next Foundation Item 12-class commit on correlation-scoping work or Sapphire cryogenic forward-prediction work, NOT a Tl-dopant first-pass

## §5 — Recommended next-direction options (for Grant adjudication)

### Option A — Land Foundation Item 11 (corpus-grep discipline) as immediate corpus commit
- Update `closure-roadmap.md` §0.5 with FI-11 entry
- Strengthen `ave-canonical-leaf-pull` skill (trigger 15?): same-session research/ scope corpus-grep
- Strengthen `ave-prereg` skill: explicit same-session research/ glob in Step 2 corpus-grep
- No physics work; pure discipline tightening
- ~1 session

### Option B — Sapphire cryogenic forward-prediction commit (independent of κ_quality grounding)
- Per correlation-scoping doc §3 and §8: Sapphire (Al₂O₃) cryogenic experiment is the cleanest path forward that doesn't depend on materials-science correlation data
- Per derivation-steps-4-9.md §9.4 Falsifier #1: "Sapphire cryogenic apparatus observes ZERO rate at 3.728 keV at sensitivity better than 10⁻⁸ events/s/kg" → framework FALSIFIED
- Land Sapphire experimental-proposal expansion / forward-prediction sharpening as next commit
- ~1-2 sessions

### Option C — Materials-science literature dive (multi-session)
- Tier-2 #9 work per correlation-scoping doc §6
- Compile mosaicity / TEM defect density / phonon-coherence-at-THz data for DAMA/COSINE/ANAIS/KIMS crystals
- Run statistical correlation test against κ_quality (cycle-12 derived)
- Publish framework validation OR Falsifier #2 walk-back
- 3-6 sessions; possibly multi-month with detector-collaborator engagement

### Option D — Bracket κ_quality work entirely; move to different ground-up physics
- κ_quality is in a "stable-pending" state — framework SURVIVES first-pass; full grounding awaits materials-science data
- Bracket and move to Q-G47 substrate-scale closure work (AVE-QED Sessions 1-18) or another open Foundation Item
- ~depends on next target

## §6 — Lane attribution + discipline reflection

This result doc landed on `analysis/divergence-test-substrate-map` branch as scoping output for the Tl-dopant first-pass attempt that the prereg pre-committed to. **The attempt itself did NOT execute — corpus-grep mid-attempt revealed the cascade-level misdirection and Outcome C terminated the derivation work.** Per ave-prereg discipline: this is the honest outcome; the prereg + result + Foundation Item 11 finding form the audit trail.

**Discipline lesson** (per `ave-newly-created-skill-self-audit` trigger 4 pattern): the auditor's "1-session attempt" recommendation was overconfident because it lacked same-session research/ corpus-grep. The corrective discipline is to encode same-session research/ scope into the corpus-grep step explicitly. Whether to encode this as `ave-canonical-leaf-pull` trigger 15 OR as `ave-prereg` Step 2 enhancement OR as a new `ave-audit-of-audit-cascade-level-check` skill depends on the pattern's recurrence — flagged for Grant adjudication.

## §7 — Cross-references

**Today's-date research docs that the audit recommendation missed**:
- [`2026-05-17_C14-DAMA_Q-factor_matched-LC-coupling_result.md`](2026-05-17_C14-DAMA_Q-factor_matched-LC-coupling_result.md)
- [`2026-05-17_DAMA-bulk-transfer-function-reframe.md`](2026-05-17_DAMA-bulk-transfer-function-reframe.md)
- [`2026-05-17_KIMS-CsI-Tl-discovery-pass.md`](2026-05-17_KIMS-CsI-Tl-discovery-pass.md)
- [`2026-05-17_parametric-coupling-kernel-derivation-steps-1-3.md`](2026-05-17_parametric-coupling-kernel-derivation-steps-1-3.md)
- [`2026-05-17_parametric-coupling-kernel-derivation-steps-4-9.md`](2026-05-17_parametric-coupling-kernel-derivation-steps-4-9.md)
- [`2026-05-17_KIMS-MAJORANA-quantitative-bounds.md`](2026-05-17_KIMS-MAJORANA-quantitative-bounds.md)
- [`2026-05-17_kappa-quality-correlation-first-pass-scoping.md`](2026-05-17_kappa-quality-correlation-first-pass-scoping.md)

**Canonical leaves consulted in mid-attempt corpus-grep**:
- [`parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) — cycle-12 canonical leaf
- [`per-element-impedance-table.md`](../manuscript/ave-kb/vol3/condensed-matter/ch10-material-properties/per-element-impedance-table.md) — CTG-1 (Z=1-14 only)
- [`inter-element-reflection-coefficient.md`](../manuscript/ave-kb/vol3/condensed-matter/ch10-material-properties/inter-element-reflection-coefficient.md) — CTG-2
- [`first-principles-bond-force-constants.md`](../manuscript/ave-kb/vol5/molecular-foundations/organic-circuitry/first-principles-bond-force-constants.md) — CTG-4 (sp³ η_lp = 1/9)
- [`analog-ladder-filter.md`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md) — CTG-supporting (Z_LC = 12.31Ω per atom)
- [`full-element-table.md`](../manuscript/ave-kb/vol6/appendix/heavy-element-catalog/full-element-table.md) — heavy-element catalog (mass-defect only, no Z_atom impedance)

**Prereg**: [`2026-05-17_kappa-quality-tl-dopant-first-pass-prereg.md`](2026-05-17_kappa-quality-tl-dopant-first-pass-prereg.md)

**Foundation Items context** (in `closure-roadmap.md §0.5`): FI-1 through FI-10 completed earlier this session; FI-11 candidate per this doc.

---

**Status: prereg COMMITTED, derivation NOT EXECUTED (corpus-grep terminated mid-attempt), Outcome C DECLARED with Foundation Item 11 finding. Next action: Grant adjudication of options A-D (Foundation Item 11 corpus commit vs Sapphire forward-prediction vs materials-science literature dive vs different physics target).**
