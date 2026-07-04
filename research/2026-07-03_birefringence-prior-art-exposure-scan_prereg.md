# FROZEN MINI-PRE-REG — Prior-art / commissioning exposure scan (GATES the prediction doc)

**Status:** FROZEN. Committed BEFORE the exposure-scan driver code (freeze-before-code discipline).
**Arc:** E-route vacuum-birefringence campaign — the decisive-paper arc (Grant-directed 2026-07-03).
**Scope cap:** the PRIOR-ART / COMMISSIONING scan ONLY. This is the Cleave G-B discipline at maximum
stakes: before ANY AVE birefringence prediction is registered, establish whether an existing measurement
already bounds an AVE-sized signal (flip-prob 5.4×10⁻³ at HIBEF-class fields — enormous by facility standards).
**Classification (`consistency-vs-emergence`):** **CONSISTENCY-class.** The scan drives the *already-canonical*
AVE δn (`clm-pp3qwf`) across a LITERATURE intensity plane and compares to LITERATURE polarimetric sensitivities.
No new emergence claim, no new `clm-`, no new constant. The magnitude rides the α-echo.

---

## 0. Sector + regime + coordinate (mandatory, inherited from GAP-1 prereg §0)

- **SECTOR.** ε-varactor grade keyed on V (quasi-static E made uniaxial by a linearly-polarized pump);
  ε-route `clm-pp3qwf`, NOT the μ-route.
- **REGIME.** Deep-cold across the whole scanned plane (A² ≤ 6×10⁻⁷ at HIBEF 10²¹, scaling as A²∝I down to
  ~6×10⁻¹¹ at 10¹⁷). Both AVE (−½A²) and QED (a_EH·α²·(E/E_crit)²) are leading-order valid; the AVE/QED ratio
  is field-independent, so the DISCRIMINATION does not weaken at lower field — only the absolute signal shrinks.
- **COORDINATE (`phase-space-coordinate-check`, A46).** The flip-prob / cross-section observables are read in
  their native coordinates: flip-prob = |retardance-phase amplitude|² (Poincaré), cross-section = photon-count.
  Both AVE and QED δn enter the IDENTICAL δn→Δφ→flip chain. PASS: no coordinate mismatch.

---

## 1. The scan question (the gate)

**Does ANY existing measurement already bound an AVE-sized flip-prob (5.4×10⁻³ at HIBEF-class fields, scaling as
A²∝I to lower fields) at any facility?** Four channels:
- (a) the LoI itself — commissioning / background / pilot data (X-ray polarimeter purity runs WITH the ReLaX pump
  on? head-on collision data at any sensitivity?).
- (b) published HIBEF/HED X-ray-polarimetry + ReLaX-collision results 2021-2026.
- (c) the broad class: any polarized X-ray probe through a PW-class optical focus with polarization analysis
  (SACLA, LCLS+laser, all-optical LbL).
- (d) non-polarimetric channels a 5.4×10⁻³ flip would contaminate (photon-count anomalies in strong-field scattering).

## 2. Frozen method

### 2.1 The A²-scaling exposure line (the NEW machinery this scan adds)
AVE's flip-prob at ANY pump intensity I, via the GAP-1 chain, reusing `src/ave/bench/birefringence.py`:
```
E(I)        = sqrt(2·I/(c·eps0))                 # peak field from intensity (LABELED std-EM)
δn_ave(E)   = -1/2·(E/E_yield)^2                  # canonical clm-pp3qwf (differential)
δn_qed(E)   = (3/45)·alpha^2·(E/E_crit)^2         # literature differenced Euler-Heisenberg
Δφ(E)       = (2π/λ)·|δn|·z                       # single-pass retardance
P_flip      = sin^2(Δφ/2)  ≈ (Δφ/2)^2 deep-cold  # flip-prob (perturbative == exact here, A²≪1)
```
Because P_flip ∝ δn² ∝ A⁴ ∝ I² at fixed (λ, z): **AVE's flip-prob scales as I² (field⁴)**, NOT I. (QED's
Eq-19 N'/N ∝ I_L² likewise — both ride δn², so the RATIO is I-independent. Verify this scaling live.)

### 2.2 The prior-experiment table (LITERATURE inputs, LABELED)
Each prior experiment plotted in the intensity × polarimetric-sensitivity plane, from the LoI + primary sources:
- LULI all-optical two-beam (σ<9.9×10⁻⁴⁰ cm² @ω*=1.7 eV) — all-optical, no X-ray probe.
- LULI all-optical three-beam (σ<1.5×10⁻⁴⁸ cm² @0.8 eV) — all-optical.
- SACLA XFEL+XFEL (σ<1.9×10⁻²³ cm² @6.5 keV) — X-ray+X-ray, no optical PW focus, cross-section not flip.
- HED-HIBEF X-ray polarimetry record purity 8×10⁻¹¹ (Fig.14) — pump OFF, no strong field in path.
- HED-HIBEF March-2024 priority-access dark-field proof-of-principle — X-ray ONLY (no ReLaX pump).
- PVLAS-FE static-B Δn/B²=(19±27)×10⁻²⁴ T⁻² — static-B route (AVE predicts EXACTLY zero, clm-pvlas1: consistent, not a test).
- STAR polarized-γγ→e⁺e⁻ modulation (indirect birefringence signature) — heavy-ion, not X-ray-through-optical-focus.

### 2.3 The classification test (frozen)
For each prior experiment, the pass/fail question: **does its geometry pass a polarized X-ray probe through a
strong (PW-class optical) field with polarization analysis, at a sensitivity finer than AVE's predicted flip-prob
at that experiment's field?** A "yes with a null" → ALREADY-BOUNDED. A "collision data exists but polarization
analysis not done/published" → PILOT-DATA-EXISTS-UNANALYZED. No prior experiment reaches the regime → CLEAN-FIELD.

## 3. Frozen output bins (the GATE verdict)

- **[ALREADY-BOUNDED]** — a measurement exists whose null constrains flip-prob < AVE's prediction at HIBEF-class
  (or scaled-down) fields → the falsifier is DEAD or wounded. **STOP before the prediction doc; surface to Grant
  with full evidence.** (The scan's most valuable possible outcome — book it honestly.)
- **[PILOT-DATA-EXISTS-UNANALYZED]** — collision data (X-ray through optical focus) exists but polarization
  analysis wasn't done/published → the reanalysis target is already sitting there. **Name the dataset.**
- **[CLEAN-FIELD]** — no prior measurement reaches the regime → the prediction document proceeds.

**Two-method rigor (Rule, mandatory):** any "no prior art / CLEAN-FIELD" conclusion must be cross-checked by a
second independent method (the driver's A²-scaling line AND a documented literature-geometry argument), not a
single grep or single fetch.

**Adjudication (Rule 11):** the bin is read off (i) the COMPUTED AVE flip-prob-vs-sensitivity per prior experiment
and (ii) the documented geometry of each. No post-hoc reclassification to keep the prediction doc alive. If a prior
null bounds AVE, that is the finding.

## 4. What is NOT claimed here
- No exp-/sup- node minted. No new `clm-`, constant, or coefficient re-derivation.
- The scan does not adjudicate the AVE physics; it establishes whether the empirical field is clean for a prediction.

**Provenance:** LoI = arXiv:2405.18063 (v1, 28 May 2024; published HPLSE Cambridge 2025); all AVE constants from
`ave.core.constants`. Frozen 2026-07-03 before the exposure-scan driver.
