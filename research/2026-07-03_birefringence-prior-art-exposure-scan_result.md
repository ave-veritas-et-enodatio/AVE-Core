# RESULT — Prior-art / commissioning exposure scan: CLEAN-FIELD (the prediction doc proceeds)

**Date:** 2026-07-03 · **Lane:** implementer · **Branch:** `analysis/birefringence-prediction-doc`
**Pre-reg:** [`2026-07-03_birefringence-prior-art-exposure-scan_prereg.md`](2026-07-03_birefringence-prior-art-exposure-scan_prereg.md) (FROZEN before this driver)
**Driver:** `src/scripts/vol_9_device/birefringence_prior_art_exposure_scan.py` · **Output:** `_output/birefringence_prior_art_exposure_scan.json`
**Class:** CONSISTENCY (canonical AVE δn `clm-pp3qwf` across a literature intensity plane vs literature polarimetric sensitivities; no new `clm-`/constant/emergence).
**Gate role:** this scan GATES the prediction document (Deliverable 3). A verdict of ALREADY-BOUNDED would have STOPPED the prediction doc and gone to Grant.

---

## 0. Headline

> **SCAN BIN: CLEAN-FIELD.** No prior or commissioning measurement bounds an AVE-sized E-route
> polarization-flip signal. Every prior experiment classifies **CANNOT-BOUND-E-ROUTE** on a single
> load-bearing geometry fact: **no published experiment simultaneously (i) puts a PW-class optical focus
> in the beam path, (ii) passes a polarized X-ray probe through it, and (iii) analyses the X-ray
> polarization flip.** The experiments with strong fields (SACLA X-ray+X-ray, LULI all-optical) have no
> X-ray-through-optical-focus geometry and measure cross-sections, not flip; the experiment with the
> sensitivity to see AVE (the record 8×10⁻¹¹ X-ray polarimeter) was run **pump OFF** (no strong field →
> A²=0 → no E-route signal to bound); the 2024 priority-access run was **X-ray ONLY** (dark-field
> beam-shaping proof-of-principle, ReLaX not fired).
>
> **The prediction document PROCEEDS** (Deliverable 3 gate CLEARED).

---

## 1. The two-method rigor (mandatory for any CLEAN-FIELD verdict)

**Method 1 — driver + documented geometry.** The exposure-scan driver classifies each prior experiment by
the arithmetic geometry test: an experiment can bound the E-route flip-prob only if it passes a polarized
X-ray probe through a strong optical field (else A²=0 and there is no AVE E-route signal to bound,
regardless of sensitivity). All 7 tabulated experiments return `CANNOT-BOUND-E-ROUTE`. The `verdict set`
across all prior experiments is the single element `{CANNOT-BOUND-E-ROUTE}`.

**Method 2 — independent literature search.** A Google-Scholar-level search on "X-ray polarization flip
through a high-intensity optical laser focus" returns **only proposals / feasibility studies / detection
schemes** (BIREF@HIBEF LoI arXiv:2405.18063; Karbstein et al. 2021 "Vacuum birefringence and diffraction
at an XFEL"; Ahmadiniaz et al. 2023 "Detection schemes for quantum vacuum diffraction and birefringence")
— **no executed measurement.** This independently confirms the driver's geometry conclusion: the
X-ray-through-optical-focus polarimetric-flip measurement has never been performed.

Both methods converge. The CLEAN-FIELD verdict is not resting on a single grep or single fetch.

---

## 2. The exposure plane — AVE's A²-scaling line vs prior-experiment sensitivities

**The scaling law (verified live):** AVE flip-prob `P = sin²(Δφ/2) ≈ (Δφ/2)²` deep-cold, and
`Δφ ∝ δn ∝ A² ∝ I`. So **P_flip ∝ I² (field⁴)** at fixed (λ, z) — `P(1e21)/P(1e20) = 99.82` (I² → ~100,
PASS). Crucially the **AVE/QED ratio is I-INDEPENDENT** (`3.72×10¹⁴` flat across the whole plane; both legs
ride δn²) — the DISCRIMINATION does not weaken at lower field, only the absolute signal shrinks.

| Pump I (W/cm²) | E-field (V/m) | A² | AVE P_flip | QED P_flip | AVE/QED | vs 8×10⁻¹¹ polarimeter floor |
|---|---|---|---|---|---|---|
| 1×10¹⁷ | 8.68×10¹¹ | 5.90×10⁻¹¹ | 5.40×10⁻¹¹ | 1.45×10⁻²⁵ | 3.73×10¹⁴ | below (≈ floor) |
| 1×10¹⁸ | 2.74×10¹² | 5.90×10⁻¹⁰ | 5.40×10⁻⁹ | 1.45×10⁻²³ | 3.73×10¹⁴ | **68× above** |
| 1×10¹⁹ | 8.68×10¹² | 5.90×10⁻⁹ | 5.40×10⁻⁷ | 1.45×10⁻²¹ | 3.73×10¹⁴ | **6.7×10³ above** |
| 1×10²⁰ | 2.74×10¹³ | 5.90×10⁻⁸ | 5.40×10⁻⁵ | 1.45×10⁻¹⁹ | 3.72×10¹⁴ | **6.7×10⁵ above** |
| 3×10²⁰ | 4.75×10¹³ | 1.77×10⁻⁷ | 4.86×10⁻⁴ | 1.30×10⁻¹⁸ | 3.72×10¹⁴ | **6.1×10⁶ above** |
| 1×10²¹ (HIBEF demo) | 8.68×10¹³ | 5.90×10⁻⁷ | 5.39×10⁻³ | 1.45×10⁻¹⁷ | 3.72×10¹⁴ | **6.7×10⁷ above** |
| 1×10²² | 2.74×10¹⁴ | 5.90×10⁻⁶ | 4.49×10⁻¹ | 1.45×10⁻¹⁵ | 3.10×10¹⁴ | above (saturation onset) |

**The brief's lower-field hypothesis is CONFIRMED and it strengthens the exposure story:** AVE's flip-prob
stays 1-8 OOM above the best X-ray polarimeter floor (8×10⁻¹¹) all the way down to ~10¹⁸ W/cm² — so *any*
pump-ON polarimetric run at ≥10¹⁸ W/cm² with a good X-ray polarimeter would see an AVE signal. **The reason
the field is clean is not that AVE's signal is small at lower fields — it is that no pump-ON polarimetric
run has ever been done at all.**

---

## 3. Per-experiment classification (the gate, verbatim from the driver)

| Prior experiment | Year | Verdict | Why it cannot bound the E-route flip-prob |
|---|---|---|---|
| LULI all-optical two-beam | 1996/2000 | CANNOT-BOUND | all-optical; no X-ray probe, no polarimetric flip channel |
| LULI all-optical three-beam | 2000 | CANNOT-BOUND | all-optical; no X-ray probe, no polarimetric flip channel |
| SACLA XFEL+XFEL | 2016 | CANNOT-BOUND | X-ray+X-ray; NO optical PW focus, cross-section not flip |
| HED-HIBEF record polarimetry (8×10⁻¹¹) | 2021 | CANNOT-BOUND | **pump OFF: no strong field in path → A²=0 → no AVE signal to bound** |
| HED-HIBEF March-2024 priority-access | 2024 | CANNOT-BOUND | **X-ray-ONLY dark-field PoP; ReLaX not fired → no collision, no flip** |
| PVLAS-FE static-B | 2016 | CANNOT-BOUND | static-B route; AVE predicts EXACTLY zero (clm-pvlas1) → consistent, not a test of the E-route |
| STAR polarized γγ→e⁺e⁻ | 2019/2021 | CANNOT-BOUND | heavy-ion virtual-photon; NOT X-ray-through-optical-focus |

**The two most-scrutinized (the commissioning data the brief flagged):**
- The **record 8×10⁻¹¹ purity** (LoI Sec 4.1, Fig.14: "in crossed-polarizer position not a single photon
  reaches the detector; to the level tested the polarizers are perfect") is a **pump-OFF** polarimeter
  characterization. It has the raw sensitivity to see AVE's flip by ~8 OOM at HIBEF field — but with no
  ReLaX pump firing there is no strong field in the beam path, so A²=0 and there is nothing to flip. It
  bounds the *instrument floor*, not an AVE signal.
- The **March-2024 priority-access beamtime** (LoI Sec 4: "the first x-ray-only beamtime was allocated for
  March 2024 ... devoted to carrying out a proof-of-principle experiment of the dark-field concept ...
  outcomes currently being analysed") was **X-ray only** — a dark-field beam-shaping / background-rate
  proof-of-principle, ReLaX not collided. It measures the shadow quality S, not a polarization flip.

---

## 4. Non-polarimetric channels (Deliverable 2d — a 5.4×10⁻³ flip contamination check)

The scan also considered whether a 5.4×10⁻³ flip would contaminate *photon-count* channels visibly:
- **LbL cross-section experiments (SACLA σ<1.9×10⁻²³ cm², LULI).** These count *scattered/flipped* photons
  as a cross-section, not a polarization-flip fraction, and none passes a polarized X-ray probe through a
  PW-class *optical* focus (they are X-ray+X-ray or all-optical). Their nulls constrain the QED LbL
  cross-section in *their* geometry — a different observable in a different field configuration. They do
  NOT translate to a bound on the E-route par−perp flip-prob (the LoI itself lists these as the historical
  bounds it aims to improve on, LoI Table 1). CANNOT-BOUND.
- **STAR γγ→e⁺e⁻ modulation** is an indirect virtual-photon birefringence signature in heavy-ion collisions
  — again not an X-ray-through-optical-focus flip.

No non-polarimetric channel bounds the E-route flip either.

---

## 5. What the scan settles vs holds

**Settles:** the empirical field is CLEAN — the prediction document may be registered as a genuine forward
(pre-data) prediction, not a post-diction against an existing null. The most valuable-possible outcome
(ALREADY-BOUNDED, which would have killed/wounded the falsifier) did NOT occur, and this was established
before any prediction was frozen.

**Holds (downstream, unchanged by this scan):**
- The INVARIANT-S9 exp-vs-sup classification (a reanalysis of HIBEF's eventual pump-on run is a sup-).
- Whether HIBEF's eventual pump-on collision (when performed) yields data a piggyback reanalysis can use —
  that is the reanalysis-target section of the prediction doc, contingent on data that does not yet exist.

---

## 6. Provenance + verify

- LoI: BIREF@HIBEF arXiv:2405.18063 (v1, 28 May 2024; published High Power Laser Science and Engineering,
  Cambridge 2025). Sections read: Exec Summary, §2.1-2.4 (History/Previous Experiments), Table 1 (prior
  bounds), Table 2 (EuXFEL + ReLaX parameters), §3.1-3.2 (conventional + dark-field scenarios), §4 (March
  2024 x-ray-only PoP), §4.1 (record 8×10⁻¹¹ purity, Fig.14).
- Independent literature cross-check: Google-Scholar-level search returns only proposals (Karbstein 2021,
  Ahmadiniaz 2023) for X-ray-through-optical-focus polarimetry — no executed measurement.
- AVE δn: `src/ave/bench/birefringence.py` (`delta_n_ave_differential_exact`, `delta_n_qed`), CANONICAL
  `clm-pp3qwf`. Constants: `ave.core.constants`, live-verified (substrate identity 137.036 = 1/α).
- `make verify` GREEN.
