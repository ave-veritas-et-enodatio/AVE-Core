# PRE-REGISTERED PREDICTION — AVE vacuum birefringence at BIREF@HIBEF (FROZEN, pre-data)

**Date:** 2026-07-03 · **Lane:** implementer · **Branch:** `analysis/birefringence-prediction-doc`
**Status:** FROZEN PRE-REGISTRATION. Every number below is computed from canonical AVE (`clm-pp3qwf`)
through the LoI's stated readout, BEFORE any BIREF@HIBEF pump-on collision data exists.
**Gate cleared:** the prior-art / commissioning exposure scan returned **CLEAN-FIELD**
([`2026-07-03_birefringence-prior-art-exposure-scan_result.md`](2026-07-03_birefringence-prior-art-exposure-scan_result.md)) —
no prior measurement bounds an AVE-sized E-route flip-prob, so this is a genuine forward prediction, not a
post-diction. (A verdict of ALREADY-BOUNDED would have blocked this document.)
**Driver:** `src/scripts/vol_9_device/birefringence_hibef_scenario_predictions.py` · **Output:** `_output/birefringence_hibef_scenario_predictions.json`
**Class:** CONSISTENCY (canonical `clm-pp3qwf` through the LoI's readout; no new `clm-`/constant/emergence).

---

## 0. Provenance requirement (the frozen-prereg discipline — read first)

**This document's predictions are complete and timestamped BEFORE any BIREF@HIBEF pump-on data is seen.** The
BIREF@HIBEF Letter of Intent (arXiv:2405.18063) is a plan; as of this document's date the only HIBEF data taken
is (i) the March-2024 x-ray-ONLY dark-field proof-of-principle (ReLaX not fired) and (ii) pump-OFF X-ray
polarimeter purity demonstrations (record 8×10⁻¹¹). Neither is a pump-on collision. The AVE prediction table in
§3 is therefore a pre-registration: if a future HIBEF pump-on run measures a flip-prob, this frozen table is the
pre-committed AVE and QED co-prediction against which it adjudicates. **No number here may be revised after HIBEF
data is public;** a revised prediction would be a new dated document with its own provenance chain.

## 1. Sector / regime / coordinate declaration (mandatory)

- **SECTOR (DC→AC coupling class).** The observable is the **ε-varactor grade** of the vacuum LC tank, keyed on
  **V (the quasi-static E of the optical pump's field envelope)** and made **uniaxial** by the linearly-polarized
  pump (probe tensor `ε_ij = ε δ_ij + 2ε' E₀ᵢE₀ⱼ`, optic axis ∥ pump). This is the **ε-route** (`clm-pp3qwf`),
  NOT the μ-route. The optical pump provides the DC operating point; the X-ray probe reads the AC differential
  index — the confirming instance of the DC→AC-carve selection rule. The μ-grade (relativistic inductor keyed on
  circulation I) is a DIFFERENT sector; §5 records why the E-vs-B asymmetry is not the HIBEF discriminator.
- **REGIME (deep-cold).** At the demonstrated pump (E ~ 8.7×10¹³ V/m), `A = E/E_yield ~ 7.7×10⁻⁴`,
  **A² ~ 5.9×10⁻⁷** — far below the yield knee (A=1). Both AVE (−½A²) and QED (differenced Euler-Heisenberg) are
  leading-order-in-A² expansions valid here. **Reaching E_yield is NOT the gate** — the AVE/QED ratio is
  field-independent; the gate is the X-ray polarimeter purity floor.
- **COORDINATE (`phase-space-coordinate-check`, A46; PASS).** The flip-prob observable is a POLARIZATION-PHASE
  (Poincaré / Jones) quantity: accumulated retardance `Δφ = (2π/λ)·|δn|·z` → flip amplitude → the polarimeter
  reads `|flip|²`. Both AVE and QED δn enter the IDENTICAL δn→Δφ→flip chain (no-strawman); the comparison is in
  matched phase-space (flip-prob) coordinates, NOT a real-space δn against a phase-space φ². No coordinate mismatch.

## 2. The prediction, in one line (with the α-echo ledgered honestly)

At the **matched par−perp differential observable** a birefringence polarimeter actually reads, AVE predicts a
polarization-flip probability a **field-independent `δn_AVE/δn_QED = 7.5/α³ ≈ 1.93×10⁷`** above QED's differenced
Euler-Heisenberg birefringence, present at ALL fields (live-verified: `coefficient_ratio_differential()` =
1.9300×10⁷, riding the exact substrate identity `(E_crit/E_yield)² = 137.036 = 1/α`).

**α-echo ledger (honest, symmetric standard).**
- **The FORM is the chord.** AVE predicts the vacuum saturates *at all* — a tree-level O(1) birefringence-bearing
  structure the QED vacuum lacks (QED's birefringence is an α²-loop effect). The *existence and form* of an O(1)
  saturation coefficient is the AVE-distinct content.
- **The MAGNITUDE (1.93×10⁷) is an α-echo at the value level.** AVE does not derive α, so the ratio rides α⁻³
  (α⁻² tree-vs-loop × α⁻¹ from the E_yield import `V_YIELD = √α·V_SNAP`, `constants.py:475/460`). Symmetric
  standard: QED's `a_EH·α²` is equally α-rooted — QED does not derive α either. **Do not headline the magnitude as
  a chord.** The chord is the existence/form; the magnitude is an echo that both frameworks share.

## 3. Per-scenario prediction table (FROZEN — the LoI's exact scenarios)

Computed through the GAP-1 readout chain (single-pass, z = 10 µm; the same chain validated in the GAP-1 result /
PR #496). AVE = canonical par−perp differential `δn_bir = −½A²` (`clm-pp3qwf`); QED = differenced Euler-Heisenberg
`(3/45)α²(E/E_crit)²` (LITERATURE), co-computed through the identical chain. LoI parameters (Table 2 / Sec 3-4):
probe X-ray 8766 / 9835 / 12914 eV; ReLaX λ=800 nm, W=4.8 J, τ=30 fs; near-head-on 45° geometry; record X-ray
polarimeter purity 8×10⁻¹¹, required-to-show ~10⁻¹².

| Scenario (LoI ref) | Pump I (W/cm²) | probe (eV) | E (V/m) | A² | **P_flip AVE** | P_flip QED | AVE/QED | margin vs 8×10⁻¹¹ | regime |
|---|---|---|---|---|---|---|---|---|---|
| conventional (Sec 3.1 Eq.27/28) | 1×10²¹ demo | 9835 | 8.68×10¹³ | 5.90×10⁻⁷ | **5.39×10⁻³** | 1.45×10⁻¹⁷ | 3.72×10¹⁴ | 6.7×10⁷ | un-saturated ✓ |
| dark-field (Sec 4.2, Ge-440) | 1×10²¹ demo | 8766 | 8.68×10¹³ | 5.90×10⁻⁷ | **4.28×10⁻³** | 1.15×10⁻¹⁷ | 3.72×10¹⁴ | 5.4×10⁷ | un-saturated ✓ |
| high-energy (Table 2, 12-13 keV) | 1×10²¹ demo | 12914 | 8.68×10¹³ | 5.90×10⁻⁷ | **9.28×10⁻³** | 2.50×10⁻¹⁷ | 3.71×10¹⁴ | 1.2×10⁸ | un-saturated ✓ |
| conventional design (Sec 2.2 PW-upgrade) | 1×10²² design | 9835 | 2.74×10¹⁴ | 5.90×10⁻⁶ | 4.49×10⁻¹ | 1.45×10⁻¹⁵ | 3.10×10¹⁴ | 5.6×10⁹ | **saturating** (Δφ=1.47 rad) |
| conventional design (Sec 2.2 upper) | 1×10²³ design | 9835 | 8.68×10¹⁴ | 5.90×10⁻⁵ | 7.65×10⁻¹ | 1.45×10⁻¹³ | 5.28×10¹² | 9.6×10⁹ | **FORM-BREAKS** (Δφ=14.7 rad) ⚠ |

**Reading the table (honest booking):**
- **The three DEMONSTRATED-pump scenarios are the bankable headline.** At HIBEF's already-demonstrated ReLaX
  field, AVE's flip-prob is a **well-behaved, small-angle, un-saturated 4–9×10⁻³** (Δφ/2 ≤ 0.10 rad; perturbative
  `(Δφ/2)²` and exact `sin²(Δφ/2)` agree to ~0.3%). It sits ~7 OOM above the record 8×10⁻¹¹ polarimeter floor.
  **No non-perturbative rescue is invoked; no derivation gap.** This is the prediction the campaign rests on.
- **The 1×10²² design scenario is saturating** (Δφ = 1.47 rad; the perturbative 0.54 and exact 0.449 diverge by
  ~17%). Book the exact `sin²` value (0.449), and note the small-angle approximation no longer holds here.
- ⚠ **The 1×10²³ design scenario is FORM-BREAKS-UNRESOLVABLE** (Δφ = 14.7 rad, Δφ/2 = 7.35 rad ≫ 1). The
  single-pass `sin²(Δφ/2)` is a many-radian-wrap oscillation and the crossed-polarimeter flip fraction is
  ambiguous (the vacuum is effectively opaque to the polarimeter at this field in the AVE picture). Per the GAP-1
  prereg §3 adjudication note (Rule 11), this is a **named derivation gap, NOT a clean prediction** — it is NOT
  part of the frozen falsifier. It is tabulated only to mark where the single-pass mapping stops being credible.
  **The falsifier lives at the demonstrated-pump scenarios, where the form does not break.**

## 4. The kill criteria (frozen, both ways — cite the pre-committed corpus language)

The pre-committed corpus falsifier statement (canonical leaf `vacuum-birefringence-e4.md:55`, verbatim):
> "At the **matched differential observable**, AVE sits a field-independent δn_AVE/δn_QED = 7.5/α³ ≈ 1.93×10⁷
> above QED's differenced Euler-Heisenberg (3/45) birefringence, present at **all** fields. A **QED-sized
> differential coefficient** (δn_bir ∼ (3/45)α²(E/E_crit)²) falsifies AVE; an AVE-sized coefficient falsifies QED
> at this observable. (An E² slope does **not** falsify AVE — QED is also E²-leading. The discriminator is the
> coefficient, not the exponent.)"

(Verbatim from the leaf; markdown emphasis preserved. `verify-before-cite`: grepped at HEAD this session — the
fragments "A **QED-sized differential coefficient**", "an AVE-sized coefficient falsifies QED at this observable",
and "does **not** falsify AVE — QED is also $E^2$-leading" all confirmed present in `vacuum-birefringence-e4.md`.)

Applied to a BIREF@HIBEF demonstrated-pump run:
- **NULL-ABOVE-FLOOR kills AVE (`clm-pp3qwf` + the E-route falsifier).** If a pump-on run at ≥10²¹ W/cm² with a
  polarimeter at or below the record 8×10⁻¹¹ purity measures a flip-prob **at or below the QED co-prediction**
  (≈10⁻¹⁷, i.e. no AVE-sized ~10⁻³ signal where the polarimeter can resolve it by ~7 OOM), that is a **QED-sized
  differential coefficient** → it **KILLS `clm-pp3qwf` and the E-route falsifier** by the leaf's own kill-language.
  This is a decisive, pre-committed falsification (Rule 11: record it, close the branch; no rescue).
- **SIGNAL-AT-AVE-LEVEL is the chord.** A measured flip-prob ~ P_AVE (4–9×10⁻³, ~7 OOM above QED and above floor)
  is an **AVE-sized coefficient** → it **falsifies QED at this observable** and is the AVE chord (the tree-level
  O(1) saturation QED lacks). Note per §2 the *magnitude* is an α-echo; the *chord* is the existence of an O(1)
  differential coefficient where QED has only an α²-loop.
- **An E² slope alone does NOT falsify AVE** (QED is also E²-leading). The discriminator is the COEFFICIENT.

## 5. Why the E-vs-B asymmetry is NOT the HIBEF discriminator (flag-don't-fix, carried from GAP-1)

AVE predicts `δn_μ = 0` EXACTLY for a static B (`clm-pvlas1`; the μ-grade is a relativistic inductor keyed on
circulation, and a static B has ∂B/∂t=0 → unloaded). But HIBEF's ReLaX pump is a **propagating** optical wave
(B = E/c, ∂B/∂t ≠ 0): its E and B co-move, AVE's μ-grade IS loaded by the circulation, and the ε-route
`clm-pp3qwf` already captures the full wave response. **So there is no static-B leg at HIBEF to run the clean
zero-vs-nonzero asymmetry against.** The clean E-vs-B asymmetry lives at the PVLAS/BMV magnetic-route facilities
(genuine static B), where AVE predicts EXACTLY zero and the existing static-B nulls are CONSISTENT-with-AVE (they
confirm the side-prediction, they do not test the E-route). **At HIBEF the discriminator is the E-route
coefficient gap (`clm-pp3qwf`), not the E-vs-B asymmetry.** Do not book the asymmetry as a HIBEF-testable observable.

## 6. Piggyback REANALYSIS vs a DEDICATED request (what each would need)

**What a piggyback REANALYSIS of HIBEF's eventual QED-birefringence run would need (the cheaper path):**
- The dataset: a pump-ON collision run (ReLaX firing, X-ray probe through the focus, crossed-polarimeter readout)
  — the conventional two-beam or dark-field scenario of the LoI. This does not yet exist (the field is CLEAN).
- The analysis chain: from their published crossed-polarimeter counts, extract the flip-prob (N⊥/N corrected for
  the LoI's non-ideal factors: diamond-reflection loss ~2%/reflection, lens transmission, analyser acceptance
  bandwidth Δω_diamond/Δω), then compare to (i) the QED co-prediction (~10⁻¹⁷ demonstrated-pump, ~10⁻¹² with the
  LoI's focus-integration) and (ii) THIS document's frozen AVE prediction (~10⁻³). The discrimination is ~14 OOM
  in flip-prob between the two hypotheses — a reanalysis needs only the flip-prob and its error bar, not new
  hardware.
- **S9 classification (HELD for the charter, flagged here):** per INVARIANT-S9 a reanalysis of HIBEF's own run is
  a **sup-**, not an **exp-** (it does not float `experimental_solidity` off None). A dedicated run we design and
  control would be the only **exp-** path. This document does not mint either node; the classification is HELD.

**What a DEDICATED request would add (the stronger path):**
- Control of the pump intensity (to place the run in the un-saturated demonstrated-pump regime, avoiding the
  1e23 form-break) and the probe energy (to hit the 8766 eV Ge-440 dark-field analyser sweet spot).
- The parity-odd optical-activity ROTATION channel (θ≠0, sign-flips, achiral-null; QED θ≡0 identically) as an
  orthogonal zero-vs-nonzero discriminator — strictly cleaner than the retardance coefficient, but not
  apparatus-spec'd here (flagged in the falsifier doc open-item #7).
- A two-color probe to exercise the `(qℓ_node)⁴` dispersion forward-prediction (open-item #8).

## 7. What is NOT claimed here
- No exp-/sup- node minted; no new `clm-`, constant, or coefficient re-derivation.
- The 1×10²³ design scenario is a named FORM-BREAKS derivation gap, NOT a frozen prediction (§3).
- The absolute SNR / integration-time numbers (shots-to-#σ) are the LoI's own (Eq.29: `#σ²×7.5×10⁴` shots for the
  QED signal); AVE's ~7-OOM-larger flip-prob would need proportionally fewer shots, but the shot-count model is
  not re-derived here — the flip-prob-vs-floor comparison this document freezes does not depend on it.

## 8. Provenance + verify
- LoI: BIREF@HIBEF arXiv:2405.18063 (v1, 28 May 2024; published HPLSE, Cambridge 2025). Scenario parameters:
  Table 2 (EuXFEL + ReLaX), Sec 3.1 (conventional Eq.27/28), Sec 4.2 (Ge-440 dark-field 8766 eV), Sec 4.1
  (record 8×10⁻¹¹ purity, required ~10⁻¹²), Eq.19 (N'/N ~ 10⁻¹² QED estimate at I_L=10²¹).
- AVE δn: `src/ave/bench/birefringence.py` (`delta_n_ave_differential_exact`, `delta_n_qed`), CANONICAL
  `clm-pp3qwf`. Chain: reuses the GAP-1 readout (`birefringence_gap1_hibef_feasibility.py`, PR #496).
- Kill-language: canonical leaf `vacuum-birefringence-e4.md:55` (quoted verbatim in §4).
- Constants: `ave.core.constants`, live-verified (substrate identity 137.036 = 1/α; ratio 1.9300×10⁷).
- `make verify` GREEN; drivers ruff-clean.
