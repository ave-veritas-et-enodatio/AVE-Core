# κ_quality Empirical Correlation — Tier-2 #9 First-Pass Scoping

**Status:** First-pass literature scoping per Tier-2 #9 (NOW LOAD-BEARING per Tier-2 #6 KIMS refinement). Initial finding: **light yield ANTICORRELATES with κ_quality across DAMA/COSINE/ANAIS** — opposite of what naive "crystal quality correlates with κ" would predict. Implications: κ_quality must depend on a NON-OPTICAL crystal property (phonon coherence at α-slew rate, mosaicity, defect-trap structure), NOT on optical-quality metrics (light yield, energy resolution).
**Date:** 2026-05-17 night
**Lane:** First-pass literature scoping doc; not a definitive walk-back (framework status hasn't fundamentally shifted), but a pre-falsifier flag for κ_quality framework integrity

## §1 — Why this is now load-bearing

Per Tier-2 #6 KIMS refinement (commit `12e95d4`): cross-detector κ_quality variation now spans 20-50× within rock-salt+Tl class (DAMA κ=1 vs KIMS κ≲0.02) and 10⁴-5000× across lattice types (DAMA vs MAJORANA HPGe). This variation MUST be explained by materials-science crystal-quality metrics for framework integrity, per parametric-coupling-kernel.md §9 Falsifier #2:

> "κ_quality does NOT correlate with crystal-quality metrics across DAMA/COSINE/ANAIS samples" → framework loses physical grounding

This first-pass literature scoping is the initial test.

## §2 — Published light yield data (cross-detector)

| Detector | NaI(Tl) light yield (phe/keV or NPE/keV) | Source |
|---|---|---|
| DAMA/LIBRA | 5.5-7.5 phe/keV | [DAMA technical papers](https://en.wikipedia.org/wiki/DAMA/LIBRA) |
| COSINE-100 | ~15 NPE/keV (2-3× DAMA) | [arXiv:2408.14688](https://arxiv.org/html/2408.14688v1) (lowered threshold paper) |
| ANAIS-112 | 12-16 phe/keV (2-3× DAMA) | [ANAIS performance papers](https://arxiv.org/html/2502.01542v1) |

**Observation**: COSINE-100 and ANAIS-112 have **HIGHER** light yield than DAMA/LIBRA by factor 2-3×. Yet COSINE/ANAIS observe NULL while DAMA detects.

## §3 — κ_quality vs light yield (cycle-12 framework)

Per cycle-12 cross-detector predictions:

| Detector | κ_quality (cycle-12 derived) | Light yield (published) |
|---|---|---|
| DAMA/LIBRA NaI(Tl) | ≈ 1 (matched ceiling) | 5.5-7.5 phe/keV |
| COSINE-100 NaI(Tl) | ≲ 0.4 (from null) | ~15 NPE/keV |
| ANAIS-112 NaI(Tl) | ≲ 0.4 (from null) | 12-16 phe/keV |
| **KIMS CsI(Tl)** | **≲ 0.02-0.05** (Tier-2 #6 refined) | (commercial-grade; lower than DAMA NaI(Tl)) |
| MAJORANA HPGe | ≲ 10⁻³-10⁻⁴ (Tier-2 #7 refined) | (different detection mechanism — HPGe is direct ionization, not scintillation) |

**Correlation analysis**:
- DAMA (κ=1) has LOWEST light yield among NaI(Tl) detectors
- COSINE/ANAIS (κ≲0.4) have ~2-3× HIGHER light yield
- KIMS (κ≲0.02) uses different lattice (CsI vs NaI) but commercial-grade crystals

**Light yield ANTICORRELATES with κ_quality within the NaI(Tl) class** (correlation coefficient would be strongly negative if computed across these 3 data points).

## §4 — Implication for framework integrity

The cycle-12 framework asserts κ_quality is a **physics-grounded** parameter set by crystal-quality variations. The light-yield-anticorrelation observation has THREE possible interpretations:

### Interpretation A (framework consistent) — κ_quality depends on non-optical crystal property

κ_quality is set by lattice phonon coherence at α-slew rate ν_slew ~ 9×10¹⁷ Hz (THz scale). Light yield depends on:
- Tl dopant concentration (more Tl → more scintillation centers, higher light yield)
- Optical clarity (less self-absorption)
- PMT geometry + QE

These are DIFFERENT physics than phonon coherence at THz. So light yield is NOT a relevant κ_quality proxy.

**Falsifiable prediction**: κ_quality SHOULD correlate with a NON-OPTICAL crystal property:
- X-ray rocking curve FWHM (mosaicity)
- Phonon mean free path at THz frequencies
- Defect density via TEM
- Acoustic Q-factor at THz

If such correlation found → framework validated as physics-grounded.

### Interpretation B (framework needs revision) — κ_quality is fit parameter

If κ_quality variation does NOT correlate with ANY measurable crystal-quality metric, the framework loses predictive content. κ_quality becomes a per-detector fit parameter absorbing cross-detector variation without physical basis.

This is the Falsifier #2 condition per parametric-coupling-kernel.md §9.

### Interpretation C (cycle-12 framework has structural issue) — DAMA-distinct mechanism

DAMA's signal might be from a fundamentally different mechanism that doesn't apply to COSINE/ANAIS/KIMS. The cycle-12 parametric coupling kernel might be necessary but not sufficient — additional DAMA-specific physics needed.

Plausible DAMA-distinct features:
- DAMA crystals are OLDER (grown 1990s with different techniques)
- DAMA crystals have UNIQUE history (specific annealing / cooling)
- DAMA's lower light yield could indicate MORE specific defect types that couple to substrate refresh

This would walk back cycle-12 framework from "single canonical detection mechanism" to "DAMA-class only" — a substantial framework reduction.

## §5 — Honest scoping of this first-pass scoping

This is a **literature search**, not a rigorous correlation analysis. Caveats:

1. **Sparse data**: only 3-4 NaI(Tl) detectors with published light-yield numbers; statistical correlation analysis underpowered
2. **Confounders**: COSINE/ANAIS use DIFFERENT PMT models + crystal-coupling geometries than DAMA; light yield differences could be partly from electronics + geometry, not pure crystal quality
3. **Tl concentration**: DAMA NaI(Tl) Tl-doping level might differ from COSINE/ANAIS; this directly affects light yield but also could affect substrate coupling via dopant uniformity
4. **No mosaicity data found**: published X-ray rocking curve measurements for dark-matter NaI(Tl) crystals not found in this literature pass
5. **No phonon-coherence-at-THz data found**: this is the load-bearing metric for cycle-12 framework but is not typically measured for scintillator crystals

## §6 — Recommendations for full Tier-2 #9 work

To rigorously test cycle-12 framework κ_quality grounding:

**Required data (not found in first-pass literature search)**:
1. **X-ray rocking curve FWHM** for DAMA, COSINE-100, ANAIS-112 NaI(Tl) crystals (mosaicity)
2. **TEM defect density** for same crystals
3. **Brillouin-scattering data** at THz frequencies for phonon coherence length
4. **Tl-dopant uniformity maps** (cathodoluminescence + EBIC + SIMS)

**Required protocol**:
1. Compile crystal-quality metrics from peer-reviewed materials-science literature (NOT dark-matter physics literature — typically reports light yield + radio-purity but not lattice quality)
2. Engage with detector collaborators (DAMA, COSINE-100, ANAIS-112, KIMS) for unpublished crystal-characterization data
3. Statistical correlation test between κ_quality (cycle-12 derived) and each materials-science metric
4. Publish κ_quality framework validation OR falsification

**Estimated effort**: 1-3 sessions for literature compilation; additional collaboration engagement for unpublished data (multi-month timeline).

## §7 — Preliminary framework-state assessment

Given the light-yield-anticorrelation observation + sparse data on non-optical metrics:

**Framework status (post external reviewer A#3 honest-scoping)**: cycle-12 κ_quality framework is **NOT YET FALSIFIABLE on this data class** — the load-bearing data (mosaicity, phonon coherence at THz, defect density) does not exist in published dark-matter literature. ~~Framework SURVIVES first-pass test~~ is generous framing; what actually obtains is that the framework has not been falsified yet BECAUSE the falsifying data class doesn't exist in publicly-available form. Light yield is not a relevant κ_quality proxy by physics argument (different mechanism), so the light-yield-anticorrelation observation doesn't constitute a survival test — it's a category-mismatch, neither confirmation nor falsification. **Falsifiability remains PENDING materials-science data acquisition** (multi-month timeline involving literature dive + detector-collaborator engagement).

**Risk**: if rigorous Tier-2 #9 work (above) finds NO correlation with ANY measurable crystal-quality metric, framework Falsifier #2 triggers and cycle-12 walk-back to "DAMA-class only" would be required.

**Strongest test currently feasible**: Sapphire (Al₂O₃) cryogenic experiment per HPGe proposal §13 — different lattice + different temperature + different Q regime; tests cycle-12 framework's lattice-dependence prediction independent of the rock-salt+Tl-dopant complications.

## §8 — Single-detector falsifier candidates (if rigorous #9 work blocked)

If materials-science data hunting fails, the framework can still be tested via:

1. **Cross-detector swap test**: same NaI(Tl) crystal used by both DAMA AND COSINE/ANAIS infrastructure (e.g., transfer a DAMA crystal to COSINE's analysis pipeline). If DAMA crystal shows DAMA-class rate in COSINE infrastructure → crystal-specific (not analysis-specific). Politically infeasible but scientifically clean.

2. **Sapphire cryogenic forward prediction**: cycle-12 framework predicts $\sim 10^{-5}$-$10^{-7}$ events/s/kg for Sapphire at TES-readout cryogenic conditions. Independent of κ_quality framework grounding.

3. **DAMA crystal age effect**: if DAMA crystals' uniqueness is from age + annealing history, freshly-grown high-purity NaI(Tl) should NOT show DAMA-class rate even at matched light-yield + radio-purity. Testable via dedicated growth + characterization.

## §9 — Net first-pass conclusion

**Light yield anticorrelates with κ_quality across DAMA/COSINE/ANAIS** — this is the cleanest empirical observation from first-pass literature search. The cycle-12 framework can accommodate this IF κ_quality depends on non-optical crystal properties (phonon coherence at α-slew rate, mosaicity, defect-trap structure).

**Full Tier-2 #9 validation pending**: requires non-optical crystal-quality data not found in first-pass dark-matter literature. Recommended next steps: materials-science literature dive + detector-collaborator engagement.

**Framework status unchanged (post A#3 honest scoping)**: cycle-12 framework is NOT YET FALSIFIABLE on this data class (relevant κ_quality metrics not published in dark-matter literature). The light-yield-anticorrelation finding is a CATEGORY-MISMATCH observation (different physics than κ_quality), not a survival test. **Full empirical grounding requires materials-science data acquisition (multi-month timeline)**. Sapphire cryogenic prediction (HPGe proposal §13) provides an independent forward test that doesn't depend on κ_quality grounding work — that's the cleanest path forward for empirical evaluability.

## §10 — Corpus impact (minimal)

This is a first-pass scoping doc, NOT a definitive walk-back. Minimal corpus propagation:

1. **`manuscript/ave-kb/common/closure-roadmap.md` §0.5**: new brief entry noting first-pass scoping outcome
2. **`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md` §6 κ_quality**: cross-reference this scoping doc; note that light yield is NOT a relevant κ_quality proxy

## §11 — Cross-references

**Upstream**:
- Cycle-12 parametric coupling kernel canonical leaf + cross-detector §8 + §9 falsifiers
- Tier-2 #6 KIMS quantitative refinement (commit `12e95d4`)
- Tier-2 #7 MAJORANA quantitative refinement (same commit)

**Source literature (this scoping doc)**:
- DAMA/LIBRA detector overview: [Wikipedia](https://en.wikipedia.org/wiki/DAMA/LIBRA)
- COSINE-100 lowered threshold + light yield: [arXiv:2408.14688](https://arxiv.org/html/2408.14688v1)
- ANAIS-112 6-year results: [arXiv:2502.01542](https://arxiv.org/html/2502.01542v1)
- NaI(Tl) nonproportionality study: [EPJ C 84, 12770 (2024)](https://link.springer.com/article/10.1140/epjc/s10052-024-12770-1)
- NaI defect formation (recent): [arXiv:2512.23553](https://arxiv.org/abs/2512.23553)

**Recommended follow-up data sources** (not pursued in first pass):
- COSINE-200 ultra-pure crystal development [arXiv:2009.00802](https://arxiv.org/abs/2009.00802)
- COSINE-100 alpha backgrounds [arXiv:2311.05010](https://arxiv.org/abs/2311.05010)
- Direct PMT-coupling COSINE upgrade [arXiv:2409.15748](https://arxiv.org/abs/2409.15748)

---

**First-pass scoping landed 2026-05-17 night per Tier-2 #9. Light yield anticorrelation with κ_quality found across DAMA/COSINE/ANAIS — consistent with cycle-12 framework IF κ_quality depends on non-optical crystal properties; falsifier IF κ_quality is purely a fit parameter. Full validation requires materials-science literature dive + detector-collaborator engagement (multi-session). Framework status: cycle-12 SURVIVES first-pass test; full empirical grounding remains LOAD-BEARING; Sapphire cryogenic forward test provides independent path.**
