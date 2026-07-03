# FROZEN MINI-PRE-REG — GAP-1: AVE realized observable at HIBEF's actual parameters

**Status:** FROZEN. Committed BEFORE the GAP-1 driver code (freeze-before-code discipline).
**Arc:** E-route vacuum-birefringence campaign opening (RANK-1, cold-eyes-audit-ratified 2026-07-03).
**Scope cap:** GAP-1 ONLY — the feasibility arithmetic that sizes the campaign. Bins frozen here; the campaign charter, the exp-vs-sup S9 classification, and any facility partnership are HELD downstream.
**Classification (`consistency-vs-emergence`):** **CONSISTENCY-class.** GAP-1 drives the *already-canonical* AVE δn coefficient (`clm-pp3qwf`, deriv_solidity 0.80) through a *literature* HIBEF readout chain (X-ray dark-field polarimeter; NJP 2021 / BIREF@HIBEF LoI). **No new emergence claim, no new `clm-`, no new constant.** The magnitude rides the α-echo (`7.5/α³`); the readout floor (`P=1.4×10⁻¹⁰` required, `2.4×10⁻¹⁰` demonstrated) is a facility engineering input. The output is a *feasibility book*, not a physics chord.

---

## 0. Sector header + regime declaration (mandatory)

- **SECTOR.** The birefringence observable is on the **ε-varactor grade of the vacuum LC tank — keyed on V (a static/quasi-static E)**. This is the A1-scalar dilatation kernel `S = √(1−(E/E_yield)²)` made uniaxial by a linearly-polarized pump (probe tensor `ε_ij = ε δ_ij + 2ε' E₀ᵢE₀ⱼ`, optic axis ∥ pump). It is the **ε-route** (`clm-pp3qwf`), NOT the μ-route. The μ-grade (relativistic inductor keyed on circulation I) is a DIFFERENT sector; a static B leaves it unloaded (`δn_μ = 0` exactly, `clm-pvlas1`) — that is the E-vs-B asymmetry discriminator, computed separately in §3.
- **REGIME.** **Deep-cold.** At HIBEF's field `E ~ 8.7×10¹³ V/m`, `A = E/E_yield ~ 7.70×10⁻⁴`, `A² ~ 5.92×10⁻⁷` — far below the yield knee (A=1). Both AVE (−½A² differential) and QED (a_EH·α²·(E/E_crit)²) are leading-order-in-A² expansions valid here. **Reaching E_yield is NOT the gate** — the AVE/QED ratio is field-independent (survey :47-48). The gate is the detector purity floor.
- **PHASE-STATE.** Quasi-static pumped vacuum: the optical pump provides the DC operating point (ε near V_yield); the X-ray probe reads the AC differential index. This is the **DC→AC coupling class** (the confirming instance of the AC/DC-carve selection rule iv, `form-deriving-value-importing.md`).

### 0.1 Coordinate declaration (`phase-space-coordinate-check`, A46)

- The **flip-probability / ellipticity observable is a POLARIZATION-PHASE (Jones / Poincaré-sphere) quantity** — accumulated retardance `Δφ = (2π/λ)·δn·z` maps to a polarization-flip amplitude, and the X-ray polarimeter reads `|flip amplitude|²`. This is a phase-space observable read in its native (retardance-phase) coordinates.
- **Both AVE and QED δn** (real-space index shifts) enter through the *identical* `δn → Δφ → flip-prob` chain (no-strawman R1). The AVE δn prediction and the QED δn prediction are compared in matched phase-space (flip-prob) coordinates — NOT a real-space-Cartesian δn against a phase-space φ². **PASS:** no coordinate mismatch.
- **The form-break is a phase-space wrapping problem:** the perturbative `P_flip ≈ (Δφ/2)²` is a small-angle truncation of the exact `P_flip = sin²(Δφ/2)`, which is bounded in [0,1]. When the linear formula exceeds unity the honest observable is the exact `sin²` (§2.3).

---

## 1. The GAP-1 question

**At HIBEF's ACTUAL parameters (E ~ 8.7×10¹³ V/m, I_L = 10²¹ W/cm², single-pass z ~ 10 µm, X-ray probe ~9-13 keV, X-ray dark-field polarimeter), what is AVE's REALIZED polarization-flip observable — and does it clear (a) the demonstrated 2.4×10⁻¹⁰ purity floor, (b) the required 1.4×10⁻¹⁰ floor, or (c) neither?**

The naive perturbative AVE flip-prob drives `P > 1` (survey :77-79: on flip-probability the field-independent amplitude ratio squares to ~9×10¹³× QED — the perturbative form BREAKS). GAP-1 must derive the **honest saturated** prediction (the exact `sin²(Δφ/2)`, bounded) and compare THAT to the floors.

---

## 2. Frozen method

### 2.1 Facility parameters (LITERATURE inputs, LABELED, from the survey + primary sources)

| Symbol | Value | Source |
|---|---|---|
| `E_HIBEF` | 8.7×10¹³ V/m | BIREF@HIBEF LoI arXiv:2405.18063 (I_L=10²¹ W/cm²), survey :71 |
| `z` (interaction length) | 10 µm | single-pass, survey :67 |
| `E_probe` | 9835 eV (NJP), 8766 / 12914 eV (LoI scenarios) | NJP 2021 doi:10.1088/1367-2630/ac1df4; survey :71 |
| `P_required` | 1.4×10⁻¹⁰ | NJP 2021 (diamond quasi-channel-cut @9835 eV) |
| `P_demonstrated` | 2.4(±0.9)×10⁻¹⁰ @6.457 keV; 5.7×10⁻¹⁰ @12.914 keV | Marx-Schulze PRL 110, 254801 (2013) |
| QED signal | ~0.86 flipped photons/hr vs ~5.6×10⁶ bkg/hr | NJP 2021 |

### 2.2 The δn legs (CANONICAL AVE, LITERATURE QED — reuse `src/ave/bench/birefringence.py`)

- **AVE differential:** `δn_bir = n_par − n_perp = −½A²` leading (exact: `delta_n_ave_differential_exact`), `A = E/E_yield`. **CANONICAL** (`clm-pp3qwf`, `birefringence.py:193`).
- **QED differential:** `δn_QED = (3/45)·α²·(E/E_crit)²` (differenced Euler-Heisenberg 7/45 ∥, 4/45 ⊥). **LITERATURE** (`delta_n_qed(E, 3/45)`).
- Matched ratio `δn_AVE/δn_QED = 7.5/α³ ≈ 1.93×10⁷`, field-independent (verified live: substrate identity `(E_crit/E_yield)² = 1/α`).

### 2.3 The readout chain (the NEW machinery GAP-1 adds — the HIBEF X-ray-polarimeter flip-prob)

Single-pass (no Fabry-Perot; HIBEF has none, survey :67,:155):
```
Δφ(E)       = (2π/λ_probe) · δn(E) · z          # accumulated retardance phase
P_flip_pert = (Δφ/2)²                            # perturbative (small-angle) flip-prob — BREAKS when > 1
P_flip_exact= sin²(Δφ/2)                          # HONEST bounded flip-prob (the saturated observable)
```
Both legs ride the IDENTICAL chain (no-strawman R1); only δn differs. `λ_probe = 2πℏc/E_probe`.

### 2.4 Step 3.8 liveness — VALIDATE THE PIPELINE ON THE QED LEG FIRST (freeze this gate)

**The QED leg through this chain must reproduce the literature QED order at the matching field before the AVE leg is read.** Frozen validation criteria:
1. `substrate_identity_holds()` True; `A_e` recovers 1.32×10⁻²⁴ T⁻² to <1% (existing validate-on-known).
2. **QED-leg order check:** at the LoI *design* field, the QED flip-prob computed through §2.3 must land in the literature order-of-magnitude band `[10⁻²¹, 10⁻¹²]` set by the published 0.86 flipped-photons/hr against 10¹²-10²⁰ probe-photons/hr (order-of-magnitude, per the survey's own ~10⁻¹² characterization). **The demonstrated-pump (I_L=10²¹) single-pass QED flip-prob is expected ~10⁻¹⁷** (my flat single-pass geometry, no focus-integration weighting) — this is BOOKED as the honest gap between a flat-z model and the LoI's focus-integrated design prediction, and the AVE/QED RATIO (field-independent) is unaffected by it.
3. `P_flip_exact == P_flip_pert` to machine precision on the QED leg (QED Δφ ≪ 1, so no saturation) — confirms the exact form reduces to perturbative where it should.

**If the QED leg does not reduce to the perturbative form (criterion 3 fails), HALT** — the readout chain is wrong.

---

## 3. Frozen output bins (the decision that sizes the campaign)

Compute AVE's `P_flip_exact` at HIBEF's demonstrated parameters (E=8.7×10¹³, z=10 µm, λ from the probe energy) and classify:

- **[CLEARS-FLOOR]** — AVE's realized flip-prob (or the equivalent single-shot detectable signal) ≥ demonstrated `2.4×10⁻¹⁰` purity floor → HIBEF's own planned QED run adjudicates AVE by REANALYSIS (the piggyback prize). **Quantify the margin** (AVE signal / demonstrated floor).
- **[BETWEEN]** — clears the required `1.4×10⁻¹⁰` but not the demonstrated `2.4×10⁻¹⁰` → dedicated precision push needed. **Quantify.**
- **[BELOW-FLOOR]** — AVE's realized flip-prob < required `1.4×10⁻¹⁰` at HIBEF → falsifier is facility-generation-gated; honest booking of what field/purity WOULD clear it.
- **[FORM-BREAKS-UNRESOLVABLE]** — the saturated `sin²` prediction cannot be derived at grade (e.g. the single-pass mapping is not credible because Δφ leaves the regime where `sin²(Δφ/2)` is the right observable, or the many-radian wrap makes the polarimetric readout ambiguous) → named derivation gap, route to a derivation arc.

**Adjudication note (Rule 11 discipline):** the bin is read off the COMPUTED `P_flip_exact` vs the two frozen floors. No post-hoc floor adjustment to move the bin. If the saturated signal is many radians (Δφ/2 ≫ 1), that is itself a finding (the vacuum is *opaque to the polarimeter* at this field in the AVE picture) and routes to FORM-BREAKS-UNRESOLVABLE with the mechanism named, NOT to a rescue.

### 3.1 E-vs-B asymmetry discriminator (frozen, computed alongside)

Compute at HIBEF geometry: AVE predicts `δn_μ = 0` exactly for the static/quasi-static B leg (`clm-pvlas1`); QED predicts B active (3 A_e B²). **Frozen question:** what B-field leg does BIREF@HIBEF's pump actually have (is the ReLaX optical pump's B a static/DC bias or a propagating-wave B), and is the zero-vs-nonzero asymmetry testable in their geometry? Book the answer; do not force a testable verdict if the pump B is propagating-wave (in which case AVE's μ-grade is loaded by circulation and the asymmetry is not clean — flag-don't-fix).

---

## 4. What is NOT claimed here

- No exp- node is minted (per INVARIANT-S9, a reanalysis of HIBEF's own run is a sup-, never an exp-; a dedicated run we design/control is the only exp- path — that classification is HELD downstream).
- No new `clm-`, no new constant, no coefficient re-derivation.
- The `a_EH ≈ 1.45` PVLAS back-solve artifact does NOT anchor anything (scout kill-lane flag; it is a `1/(2πα)` units artifact, excluded from the physical band).
- The absolute integration-time / SNR numbers are NOT hardened (R-3 detector-floor validate-on-known is a separate deliverable; GAP-1 books the flip-prob-vs-purity-floor comparison, which does not depend on the SNR chain).

---

**Provenance:** all facility numbers carry inline `[source]`; all AVE constants from `ave.core.constants` (verified live at HEAD 93c7424d: `E_yield=1.1304×10¹⁷ V/m`, `(E_crit/E_yield)²=137.036=1/α`). Frozen 2026-07-03 before the GAP-1 driver.
