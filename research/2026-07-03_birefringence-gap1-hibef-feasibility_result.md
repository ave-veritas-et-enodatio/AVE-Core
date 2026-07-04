# RESULT — GAP-1: AVE's realized birefringence observable at HIBEF (the campaign-sizing arithmetic)

> 🔴 **QED-NORMALIZATION CORRECTION (2026-07-03; Rule-12).** The QED P_flip `~10⁻¹⁷` and ratio `7.5/α³ ≈ 1.93×10⁷`
> here use an understated QED denominator (`(3/45)α²` too small by `1/(2πα) ≈ 21.8`). Corrected: QED P_flip
> `~2.8×10⁻¹⁴` single-pass, ratio `7.5π/α² ≈ 4.42×10⁵` (propagating). The AVE realized flip-prob `5.4×10⁻³` and the
> CLEARS-FLOOR verdict are UNAFFECTED. See
> [`2026-07-03_birefringence-qed-normalization-correction.md`](2026-07-03_birefringence-qed-normalization-correction.md).

**Date:** 2026-07-03 · **Lane:** implementer · **Branch:** `analysis/birefringence-campaign-opening`
**Pre-reg:** [`2026-07-03_birefringence-gap1-hibef-feasibility_prereg.md`](2026-07-03_birefringence-gap1-hibef-feasibility_prereg.md) (FROZEN before this driver)
**Driver:** `src/scripts/vol_9_device/birefringence_gap1_hibef_feasibility.py` · **Output:** `_output/birefringence_gap1_hibef_feasibility.json`
**Class:** CONSISTENCY (canonical AVE δn `clm-pp3qwf` through a literature HIBEF X-ray-polarimeter readout; no new `clm-`/constant/emergence).
**HEAD:** origin/main 93c7424d (constants live-verified: `E_yield=1.1304×10¹⁷ V/m`, `(E_crit/E_yield)²=137.036=1/α`).

---

## 0. Headline

> **BIN: CLEARS-FLOOR.** At HIBEF's actual demonstrated parameters (E ~ 8.7×10¹³ V/m, single-pass z ~ 10 µm, X-ray probe 9835 eV), AVE's honest **saturated** polarization-flip probability is
> $$P_{AVE} = \sin^2(\Delta\phi/2) = 5.44\times10^{-3}$$
> which clears the **demonstrated** X-ray purity floor (2.4×10⁻¹⁰, Marx-Schulze PRL 110 254801) by a margin of **~2.3×10⁷**, and the **required** floor (1.4×10⁻¹⁰, NJP 2021) by **~3.9×10⁷**. The margin is robust across the three probe-energy scenarios (1.8×10⁷ @8766 eV, 2.3×10⁷ @9835 eV, 3.9×10⁷ @12914 eV).
>
> **The piggyback prize is real.** The SAME readout chain puts the QED signal (1.5×10⁻¹⁷) far below the floor — consistent with the survey's "QED unmeasurable" (:74). So **HIBEF's own planned QED-birefringence run adjudicates AVE by REANALYSIS**: an AVE-sized coefficient would produce a ~7-OOM-above-floor flip signal where QED produces none. Per INVARIANT-S9 that reanalysis is a **sup-**, not an **exp-** (it does not float `experimental_solidity` off None) — the S9 classification is HELD for the charter, flagged here.

---

## 1. Step-3.8 liveness — QED-leg pipeline validation (PASS, gated before the AVE read)

The pre-reg froze the rule: **validate the QED leg through the new readout chain FIRST.**

| Gate | Result |
|---|---|
| Substrate identity `(E_crit/E_yield)²=1/α`, `c·B_crit=E_crit` | PASS |
| `A_e` recovers PVLAS 1.32×10⁻²⁴ T⁻² | PASS (relerr 3.5×10⁻³) |
| QED exact `sin²` reduces to perturbative `(Δφ/2)²` (Δφ_qed≪1) | PASS (Δφ_qed ~ 7.6×10⁻⁹ rad) |
| QED design-field flip-prob in literature order band | PASS (1.4×10⁻¹⁵ @1e22 W/cm², 1.4×10⁻¹³ @1e23 W/cm²) |

**Honest booking of the flat-geometry gap.** My single-pass flat-z QED flip-prob at the *demonstrated* pump (I_L=10²¹) is 1.5×10⁻¹⁷, whereas the survey/NJP characterize the QED signal as "~10⁻¹²" and 0.86 flipped-photons/hr. The gap is the **focus-integration weighting** the LoI applies (the on-axis peak field over a Gaussian-focus interaction volume) that a flat single-pass z does not carry, plus the LoI's petawatt-upgrade *design* intensity (~10²²-10²³, above the demonstrated 10²¹). **This does NOT affect the GAP-1 verdict:** the AVE/QED ratio is field-independent and geometry-independent (both legs ride the identical chain), and AVE clears the floor by 7 OOM even at the *conservative* demonstrated-pump flat-z field. If anything, the LoI's focus-integration would raise BOTH legs, widening the absolute AVE margin.

---

## 2. The GAP-1 arithmetic (the CLEARS-FLOOR bin, ledgered)

At E=8.7×10¹³ V/m, A²=5.92×10⁻⁷ (deep-cold, far below yield):

| Probe | λ (pm) | δn_AVE (differential) | Δφ_AVE (rad) | P_AVE perturbative | **P_AVE saturated** | margin vs 2.4e-10 |
|---|---|---|---|---|---|---|
| 8766 eV | 141.4 | −2.96×10⁻⁷ | 0.1316 | 4.33×10⁻³ | **4.32×10⁻³** | 1.80×10⁷ |
| 9835 eV | 126.1 | −2.96×10⁻⁷ | 0.1476 | 5.45×10⁻³ | **5.44×10⁻³** | 2.27×10⁷ |
| 12914 eV | 96.0 | −2.96×10⁻⁷ | 0.1938 | 9.39×10⁻³ | **9.36×10⁻³** | 3.90×10⁷ |

Every term ledgered:
- `δn_AVE = −½A²` — the **par-perp differential** (the polarimeter observable), CANONICAL `clm-pp3qwf` (`birefringence.py:193` `delta_n_ave_differential_exact`). MANIFESTATION of Axiom 4.
- `Δφ = (2π/λ)·|δn|·z` — accumulated single-pass retardance phase (real-space-EM bench relation, LABELED).
- `P_saturated = sin²(Δφ/2)` — the HONEST bounded flip-prob (the exact non-perturbative form). The DERIVED saturation that resolves the form-break.
- Floors: 2.4×10⁻¹⁰ demonstrated, 1.4×10⁻¹⁰ required — LITERATURE facility inputs (Marx-Schulze / NJP 2021).
- Ratio `7.5/α³ = 1.93×10⁷` — the field-independent matched-differential coefficient (α-ECHO at value level; the FORM is the chord).

---

## 3. FLAG (flag-don't-fix, surfaced to Grant) — the survey's "flip-prob >1" is a ratio-vs-absolute conflation

The scout's mission and the facility survey (:77-79) carried the premise that **"the naive perturbative AVE form drives flip-prob >1 (the form BREAKS)"** at HIBEF, and asked me to derive the honest saturated prediction for that broken regime.

**My computation at HIBEF's ACTUAL demonstrated parameters shows the premise does not hold there:**

- The naive perturbative AVE flip-prob is **5.4×10⁻³** at (E=8.7×10¹³, z=10 µm, 9835 eV) — it does **NOT** exceed unity.
- The saturated `sin²(Δφ/2)` = 5.44×10⁻³ and the perturbative `(Δφ/2)²` = 5.45×10⁻³ **agree to 0.2%** — because Δφ/2 = 0.074 rad is safely small-angle. **No saturation is active at HIBEF; the form does not break there.**
- The absolute AVE flip-prob only exceeds unity at **~3.7× higher field** (E~3.2×10¹⁴ V/m, ELI-class ~1.4×10²² W/cm²) OR a **~14× longer path** (z~0.14 mm at HIBEF field).

**Diagnosis.** The survey :77-79 statement — "on flip-PROBABILITY it squares to ~9×10¹³× QED, driving the predicted flip-prob >1" — conflates two distinct quantities:
- The flip-prob **RATIO** P_AVE/P_QED = (δn_AVE/δn_QED)² = (1.93×10⁷)² = **3.7×10¹⁴** — CORRECT (matches survey ~9×10¹³ to a factor, ratio convention aside).
- The flip-prob **ABSOLUTE** P_AVE — the survey reads it as ">1", but at HIBEF's real field/path it is 5.4×10⁻³.

The ratio being 3.7×10¹⁴ does NOT make the absolute >1; it makes AVE sit 14 OOM above QED, and since QED is ~10⁻¹⁷ that puts AVE at ~10⁻³, not >1.

**This STRENGTHENS the campaign, it does not weaken it.** The GAP-1 verdict is CLEANER than the "form-breaks" premise: AVE's realized signal at HIBEF is a **well-behaved, small-angle, un-saturated 5.4×10⁻³** — no non-perturbative rescue needed, no derivation gap, sitting ~7 OOM above the demonstrated floor. The FORM-BREAKS-UNRESOLVABLE bin is NOT triggered. **Recommendation:** correct the survey :77-79 wording to distinguish the ratio (3.7×10¹⁴×) from the absolute flip-prob (5.4×10⁻³, un-saturated) — the auditor lands the leaf/survey edit; I surface it here per flag-don't-fix.

---

## 4. E-vs-B asymmetry discriminator at HIBEF geometry (NOT clean at HIBEF)

**Verdict: the zero-vs-nonzero E-vs-B asymmetry is NOT a clean discriminator in HIBEF's geometry.**

- AVE predicts `δn_μ = 0` **exactly** for a static B (`clm-pvlas1`, μ-grade is a relativistic inductor keyed on circulation; static B has ∂B/∂t=0 → no circulation → unloaded).
- HIBEF's ReLaX pump is a **PROPAGATING optical wave** (B = E/c = 2.9×10⁵ T, ∂B/∂t ≠ 0). A propagating wave's E and B co-move; AVE's μ-grade IS loaded by the circulation, and the ε-route birefringence `clm-pp3qwf` already captures the full wave response. So there is no static-B leg at HIBEF to run the clean asymmetry against.
- The clean E-vs-B asymmetry lives at the **PVLAS/BMV magnetic-route facilities** (a genuine static B, ∂B/∂t=0), where AVE predicts EXACTLY zero and QED predicts 3 A_e B² — and where the existing static-B nulls are CONSISTENT-with-AVE (they don't test it, they confirm the side-prediction).

**So at HIBEF the discriminator is the E-route COEFFICIENT gap (`clm-pp3qwf`), not the E-vs-B asymmetry.** The asymmetry is a separate (magnetic-route) discriminator. flag-don't-fix: do not book the E-vs-B asymmetry as a HIBEF-testable observable.

---

## 5. What GAP-1 does and does not settle

**Settles:** AVE's realized flip-prob at HIBEF is measurable — ~7 OOM above the demonstrated purity floor — so a reanalysis of HIBEF's planned QED run adjudicates AVE (the piggyback prize). The feasibility gate is CLEARED at the demonstrated field; the campaign is NOT facility-generation-gated.

**Does NOT settle (HELD downstream):**
- The **INVARIANT-S9 exp-vs-sup classification** (piggyback reanalysis = sup-, dedicated run = exp-). Charter deliverable.
- The **R-3 polarimetry-floor validate-on-known** against the published Marx-Schulze cavity — closed separately in this arc (see the debt-reconciliation result).
- The **absolute SNR / integration-time** numbers (need the facility-matched co-model; the flip-prob-vs-purity comparison here does not depend on them).
- **FLAG-A** (which coefficient ratio pairs with which observable) — comparison page written for Grant's ruling (this arc).

---

## 6. Provenance + verify

- Constants: `ave.core.constants`, live-verified at HEAD 93c7424d.
- Facility numbers: BIREF@HIBEF LoI arXiv:2405.18063; NJP 2021 doi:10.1088/1367-2630/ac1df4; Marx-Schulze PRL 110 254801 (2013); survey `research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md`.
- AVE δn: `src/ave/bench/birefringence.py` (`delta_n_ave_differential_exact`, `delta_n_qed`), CANONICAL leaf `vacuum-birefringence-e4.md` (`clm-pp3qwf`).
- `make verify` GREEN.
