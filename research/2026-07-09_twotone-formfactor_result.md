# RESULT — Two-tone four-photon form factor (FORK A, task #31-A): **BRANCH (i) DRIVE-TRACKING** (1D mechanism probe)

**Date:** 2026-07-09 · **Branch:** `analysis/x31a-twotone-formfactor` (off main @ post-#604/#605)
**Prereg (FROZEN):** [`research/2026-07-09_twotone-formfactor_prereg_FROZEN.md`](2026-07-09_twotone-formfactor_prereg_FROZEN.md)
**Driver:** [`src/scripts/vol_1_foundations/twotone_formfactor.py`](../src/scripts/vol_1_foundations/twotone_formfactor.py) (extends the x29 base driver, Rule 14)
**Data:** [`research/2026-07-09_twotone-formfactor_result.json`](2026-07-09_twotone-formfactor_result.json)
**Figure:** [`src/scripts/vol_1_foundations/twotone_formfactor_figs/twotone_formfactor.png`](../src/scripts/vol_1_foundations/twotone_formfactor_figs/twotone_formfactor.png)
**Class (consistency-vs-emergence):** **EMERGENCE (Class D)** — the frequency form factor is computed
from the substrate's own nonlinear dynamics with no CODATA/target input, **on the 1D MODEL substrate**
(mechanism probe). The A⁶ amplitude law + parity null are **MANIFESTATION (Class B)**.

> **★ FIRST measurement of the substrate's four-photon coupling law above the band edge.** The object
> the ATLAS comparison needs. This is the 1D **mechanism** probe (the 3D srs run is the follow-on).
> **NO Letter/KB edits from this run** (research-tier; propagation is a follow-on after adversarial review).

---

## 0. TL;DR

Drive two tones ω_lo, ω_hi both **above the 1D chain band top (2.0 ω_C)** — evanescent, non-propagating,
but establishing real skin-region amplitudes. The saturable varactor's **χ³ (four-photon) vertex mixes
them into a propagating in-band product** at `ω_out = 2ω_lo − ω_hi`. Sweeping the tone pair UP while
holding ω_out fixed at 1.0 measures the **form factor** — how the four-photon coupling depends on how
far above the band the tones sit.

> **VERDICT: BRANCH (i) DRIVE-TRACKING.** Once the (drive-bond) participation is divided out, the
> four-photon beat power is **flat in tone frequency (q = 0.30, R² = 0.96)** across a sweep over which
> the tones' skin AMPLITUDE fell by **370×**. **The four-photon vertex is frequency-blind above the band
> — the χ³ enhancement survives; the ATLAS-tension-is-real reading (branch i) holds on the 1D mechanism
> substrate.** Casting-independent (r/√S: q = 0.23), amplitude law confirmed to the χ³ prediction
> (**exponent 6.16, predict 6, R² = 0.9997**), parity null holds, all gates pass.

Three findings, each independently checked:

1. **★ Parity theorem (pre-run, numerically confirmed).** The reversible sub-yield kernel is inversion-
   symmetric (`U(r)=1−√(1−r²)` even ⇒ `F=r+½r³+…` odd), so a two-tone line at `m·ω_lo+n·ω_hi` exists
   **only when `m+n` is ODD**. **The literal difference frequency ω_hi−ω_lo (m+n=0) is STRUCTURALLY
   FORBIDDEN below yield** — measured 10⁻³·⁴ × below the allowed product, i.e. at the floor. The four-
   photon channel that carries the form factor is the FWM sideband `2ω_lo−ω_hi` (m+n=1). *This sharpens
   the FORK-A framing: the vacuum below yield is a symmetric varactor; the "difference tone" needs a
   biased/asymmetric junction, which only appears above yield (pair production).*

2. **★ Form factor is FLAT (branch i).** The four-photon vertex does not weaken as the tones move deeper
   above the band. Raw beat power falls only 2.9× (∝ ω̄^−2.9) over a 370× skin-amplitude change; once the
   drive-bond participation is removed, the residual is flat (q = 0.30). Confirmed casting-independent.

3. **★ A⁶ amplitude law (χ³ signature).** Equal-amplitude two-tone beat power ∝ A⁶ (field ∝ A³): measured
   exponent **6.16 (R² = 0.9997)** over a 2.6×10⁵ dynamic range, down to a kernel-OFF floor at 5×10⁻²³.

**FLAG-DON'T-FIX (§4):** the prereg's *frozen* skin-amplitude participation `O_skin=e^(−(2κ_lo+κ_hi))`
**over-corrects** (it assumed the mixing scales with the skin AMPLITUDE product; the run found the mixing
is **drive-bond-localized** — birth depth = 1 node at every pair — where the strain is O(A), not skin-
suppressed). Branch (i) is read from the **KEEP-BOTH** mechanism-derived drive-bond participation
`O_bond=(1+e^(−κ_lo))²(1+e^(−κ_hi))`, **not** the frozen O_skin (which gives an unphysical q_frozen=−13.6,
power RISING). **The participation-normalization choice is surfaced for orchestrator/Grant adjudication.**

---

## 1. Gate ledger (all PASS — measurement VALID)

| Gate | Condition (prereg §8) | Result | Pass |
|---|---|---|---|
| **(a) M7 per-tone injection** | each tone establishes a nonzero skin amplitude ∝ A (NOT a no-op) | node-1 amp @A=0.10: lo **0.0223** (analytic 0.0220), hi **0.0062** (analytic 0.0064); halves with A (ratio **2.03 / 2.03**) | ✅ |
| **(b) Validate-on-known (reader)** | a planted linear ω_out tone is recovered with directional flux ∝ amp² | power-vs-amp slope **2.00**; J_right>0, J_left<0 (directional) | ✅ |
| **(c) Ramp-independence (MANDATORY)** | steady-window beat stable under ramp doubling (<5%) | rel change **1.7×10⁻³** (R vs 2R) — the x29 transient-artifact killer passes | ✅ |
| **(d) Linear control (A→0)** | beat → 0 as A⁶, not to a floor | all 5 amplitudes on the A⁶ line down to floor 5×10⁻²³; slope **6.16** | ✅ |
| **(e) Energy + dt** | free-evo \|ΔH\|/H ≤1e-5 (converging); driven beat dt-invariant <5% | dH/H **4.4×10⁻⁶** → **1.1×10⁻⁶** at dt/2 (O(dt²) converges); beat dt-halving **9.8×10⁻⁴** | ✅ |

**Decision rule applied (prereg §9.1):** gates (a,c,e) pass; ≥2 pairs clear FLOOR_SNR×floor (all 5, max
SNR 6.7×10⁶); `q = 0.30` on the drive-bond-corrected axis; `|q| < Q_FLAT = 1.0` ⇒ **BRANCH (i)
DRIVE-TRACKING** (machine-emitted in the JSON `verdict` block).

---

## 2. The parity theorem — pre-run finding, numerically confirmed (prereg §5)

`U(r)=1−√(1−r²)` is **even** ⇒ `F(r)=r+½r³+⅜r⁵+…` is **odd** (pure χ³ leading, no χ²). Under `V→−V` the
whole scheme (EOM + damping) is odd, so the response is an **odd functional of the drive**: only frequency
lines with an ODD number of ±ω factors appear. **A line at `m·ω_lo+n·ω_hi` exists iff `m+n` is ODD.**

| product | (m,n) | m+n | allowed | measured @ (2.6, 4.2) |
|---|---|---|---|---|
| ω_hi − ω_lo (difference) | (−1,+1) | 0 | **FORBIDDEN** | P_null / P_beat ≈ **3×10⁻¹¹** (floor) |
| DC / rectification | (0,0) | 0 | **FORBIDDEN** | at floor |
| **2ω_lo − ω_hi (FWM)** | **(+2,−1)** | **1** | **ALLOWED** | **the measured beat** (SNR 6.7×10⁶) |

The parity-null holds at **every** sweep pair (`P(ω_hi−ω_lo) < 10⁻³·P_beat`). **Consequence:** the FORK-A
"difference-frequency" naming is loose — the reversible vacuum is a symmetric varactor, so the true
difference tone is forbidden; the four-photon form factor lives on the odd-allowed `2ω_lo−ω_hi` sideband.
The difference channel is a **witness of inversion symmetry**: a nonzero reading there would flag an
even-order leak or that yield/rectification (pair production) had been touched — it never does here.

---

## 3. The form factor — BRANCH (i) DRIVE-TRACKING (prereg §6, §9)

Fixed in-band product `ω_out = 2ω_lo − ω_hi = 1.0` (v_g = 0.866 c); sweep the carrier ω̄ up (both tones
> 2.0 throughout). `P_beat = |Ṽ_{n_read}(ω_out)|²` (drive-bond r/S casting, A = 0.15):

| ω̄ | (ω_lo, ω_hi) | κ_lo | κ_hi | O_skin² (frozen) | O_bond² (drive-bond) | **P_beat** | P_beat/O_bond² | birth |
|---|---|---|---|---|---|---|---|---|
| 2.8 | (2.2, 3.4) | 0.887 | 2.247 | 3.22e-4 | 4.86 | 7.23e-6 | 1.49e-6 | 1 |
| 3.1 | (2.4, 3.8) | 1.245 | 2.514 | 4.51e-5 | 3.22 | 4.55e-6 | 1.41e-6 | 1 |
| 3.4 | (2.6, 4.2) | 1.513 | 2.746 | 9.71e-6 | 2.51 | 3.46e-6 | 1.38e-6 | 1 |
| 3.7 | (2.8, 4.6) | 1.734 | 2.950 | 2.66e-6 | 2.12 | 2.88e-6 | 1.36e-6 | 1 |
| 4.0 | (3.0, 5.0) | 1.925 | 3.134 | 8.60e-7 | 1.88 | 2.50e-6 | 1.33e-6 | 1 |

- **Skin amplitude fell 370×** (O_skin² column) across the sweep; **raw P_beat fell only 2.9×** (q_raw =
  2.93, R² = 0.96). The beat does NOT track the skin amplitude — it barely depends on it (raw-tracks-O_skin²
  slope = **0.18**, not 1.0).
- **Drive-bond-corrected P_beat/O_bond² is FLAT: 1.49 → 1.33 (×10⁻⁶), q = 0.30, R² = 0.96** ⇒ **|q| < 1 ⇒
  BRANCH (i) DRIVE-TRACKING.** The four-photon vertex is frequency-blind above the band.
- **Corroboration:** the r/√S casting gives the same flat form factor (q = 0.23, R² = 0.97). The
  empirically-measured drive-bond participation also corroborates branch (i) (`|q_meas| = 0.95 < 1`) but is
  noisier (R² = 0.15, one high-tone outlier at ω_hi = 5.0) — the smooth analytic drive-bond model is the
  primary; the measured is the empirical check.

**Physical reading:** the mixing happens at the **drive bond**, where the field steps from full amplitude
A down to A·e^(−κ), so the **strain** the varactor sees is `|r_0| ∝ A(1+e^(−κ)) = O(A)` for any above-band
tone — NOT skin-amplitude-suppressed. Evanescence kills the amplitude deep in the bulk, but the drive-bond
strain (hence the χ³ source) stays O(A). Confirmed by **birth depth = 1 node at every pair** (the beat is
born at the drive bond, then propagates flat — figure panel 3). This is why the vertex is frequency-blind.

---

## 4. FLAG-DON'T-FIX — the frozen participation factor over-corrects (KEEP-BOTH)

The prereg §6.2 *froze* `O_skin = e^(−(2κ_lo+κ_hi))`, modeling the FWM source by the **skin AMPLITUDE
product at node 1**. The run falsified that model: the mixing is **drive-bond-localized** (birth depth = 1;
raw P_beat barely tracks O_skin²). On the frozen axis, `P_beat/O_skin²` **RISES** steeply (q_frozen = **−13.6**,
R² = 0.999) — an unphysical negative exponent that is the signature of an over-correcting participation
factor, not a physical enhancement.

Per **KEEP-BOTH** (add a new axis, preserve the frozen one) + **flag-don't-fix**:
- **Frozen axis reported faithfully:** O_skin over-corrects; q_frozen = −13.6 (does not fit branches i/ii/iii
  as frozen, which assumed q ≥ 0). The frozen adjudication is **mis-specified** on this axis.
- **KEEP-BOTH corrected axis:** the mechanism-derived drive-bond participation
  `O_bond = (1+e^(−κ_lo))²(1+e^(−κ_hi))` (the strain the varactor actually sees). This is **not outcome-tuned**
  — it is forced by the drive-bond birth-depth finding and is independently evidenced by the near-perfect
  flatness of `P_beat/O_bond²` (1.12× over a 370× skin range).

**The branch (i) verdict rests on the drive-bond participation, NOT the frozen O_skin.** The correct
participation normalization for the eventual 3D form-factor run is **surfaced for orchestrator/Grant
adjudication** — this is a prereg-metric-misspecification, flagged not silently swapped.

---

## 5. Amplitude scaling — the A⁶ / χ³ law (prereg §5.3, Gate d)

At the fixed pair (2.6, 4.2), sweeping equal drive amplitude A over {0.015 … 0.24} (all sub-yield):

| A | max bond r | P_beat | above floor? |
|---|---|---|---|
| 0.015 | 0.034 | 2.9e-12 | ✅ |
| 0.03 | 0.069 | 1.9e-10 | ✅ |
| 0.06 | 0.137 | 1.2e-08 | ✅ |
| 0.12 | 0.275 | 8.5e-07 | ✅ |
| 0.24 | 0.551 | 8.0e-05 | ✅ |

**Measured exponent 6.16 (predict 6.0, R² = 0.9997)** — field ∝ A³, power ∝ A⁶, the four-wave-mixing (χ³)
signature. The kernel-OFF floor is **5.1×10⁻²³** (no χ³ ⇒ the ω_out bin holds only numerical leakage); all
5 points are ≥10× above it, so the beat follows the A⁶ law **down to the floor, not to a plateau** (Gate d
passes — no spurious floor). The r/√S casting reproduces the same frequency shape with a prefactor **0.24×**
the r/S run (predict ¼, from the vertex coefficient ratio ¼:½) — a clean casting cross-check.

---

## 6. Platform scoping + numerical honesty

- **1D MECHANISM PROBE.** Band top ω_top = 2.0 ω_C (1D chain dispersion), NOT the 3D srs top. The 3D srs
  top is π√3 ≈ 5.441 ω_C (#604); the **3D follow-on tones (18.51 / 17.51 ω_C, Δ=1.0, #607)** are recorded
  in the JSON, **NOT run here** and no 3D claim is made. Whether the 3D srs geometry preserves or kills
  this flat form factor is the follow-on burden.
- **Physical vs numerical:** the evanescent skin is PHYSICAL (Axiom-1 discreteness); the integrator is
  continuous-time. Free-evolution energy conserves to 4.4×10⁻⁶ at the measurement dt and **converges O(dt²)**
  (1.1×10⁻⁶ at dt/2) — controlled symplectic drift, not instability. The measured beat is dt-invariant to
  9.8×10⁻⁴ and ramp-invariant to 1.7×10⁻³. Sponge (PML) cells excluded from all reads (Rule-10).
- **Both directions:** interior drive; the beat radiates symmetrically (P_right = P_left; J_right = −J_left,
  equal magnitude) — confirming isotropic emission and reflection symmetry.

---

## 7. consistency-vs-emergence + corpus-state consequence

- **Frequency form factor → EMERGENCE (Class D)** on the 1D model substrate — computed from the substrate's
  own nonlinear dynamics, no CODATA/target input; the actual open measurement.
- **A⁶ law + parity null → MANIFESTATION (Class B)** — direct consequences of the odd (χ³) Axiom-4 kernel.
- **Band scale ω_C, ω_out=1.0, ω_top=2.0 → IDENTITY (Class A)** (native units).

**Corpus-state consequence (for the auditor to land, not this lane):** the Letter v5 named-open-item —
"the constitutive channel's closure above ω₀" (clm-gg4wmx) — now has its **first empirical form-factor
measurement on the 1D mechanism substrate: DRIVE-TRACKING (flat, branch i)** — the four-photon vertex does
NOT close above the band; the χ³ enhancement survives. **This is NOT a Letter edit or leaf correction** —
it is a research-tier fork-record surfaced to the auditor's queue, with two caveats that gate promotion:
(1) it is the **1D mechanism** probe (3D srs follow-on required before any ATLAS-facing claim); (2) the
branch rests on the **drive-bond participation normalization**, which is flagged for adjudication (§4).
Propagation to the manuscript/KB is a follow-on **after adversarial review** (research-tier discipline).

---

## 8. Caveats (load-bearing — do not over-read)

1. **1D, not 3D.** Mechanism probe only. The 3D srs run (tones 18.51/17.51, #607) is the follow-on; the 1D
   flat form factor does not by itself establish the 3D result.
2. **Participation-normalization dependence (§4).** The branch is read from the drive-bond participation
   O_bond, after the frozen O_skin was found to over-correct. The correct normalization is surfaced for
   adjudication; a different defensible participation model could shift q (though the RAW falloff, q_raw=2.9,
   is already 5× below the skin-suppression exponent ~16 — branch (i) vs (ii) is robust to the choice).
3. **Reversible (sub-yield) medium only.** The parity-forbidden difference channel ω_hi−ω_lo and the even-
   order rectification (pair production) are out of scope; runs stay sub-yield (max r ≤ 0.55).
4. **The absolute vertex normalization is a measurement output, not a first-principles prediction** (prereg
   §6.4) — only the exponents (form-factor q, amplitude 6) and the casting ratio (¼) were frozen.

---

## 9. What a follow-on / adversarial reviewer should check first

- **Re-derive the participation factor from first principles** (drive-bond strain Green's function) and
  confirm q on that normalization; adjudicate O_skin-vs-O_bond (§4).
- **The measured drive-bond outlier** at ω_hi = 5.0 (why the empirical strain dips): a longer window / finer
  spectral resolution at the highest, most evanescent tone.
- **3D srs run** at the #607 tones — the platform on which any ATLAS-facing statement must rest.
- **Widen the sweep** (more carriers, second ω_out value) to tighten q and test the flatness further above band.
