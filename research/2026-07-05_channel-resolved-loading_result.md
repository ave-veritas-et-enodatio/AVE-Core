# RESULT — Channel-resolved loading: both wave types move ρ' via the hum INDISTINGUISHABLY; the #526 T/ℓ remap moves ρ' for the matched traveling wave, CONFLICTING with canon's #518 §7 radiation null. [ASYMMETRIC-BOTH]

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/channel-discriminator`
**Prereg (FROZEN):** `research/2026-07-05_channel-resolved-loading_prereg_FROZEN.md` (committed BEFORE the driver; commit order is the freeze proof).
**Driver:** `src/scripts/vol_1_foundations/channel_resolved_loading.py`
**Tests:** `src/tests/test_channel_resolved_loading.py` (25 pass)
**Output:** `src/scripts/vol_1_foundations/_output/channel_resolved_loading.json` (driver-regenerable)
**Successor to:** the merged NEGATIVE PR #529 (`research/2026-07-04_resonant-tension-law_result.md`, [RADIATION-CONTAMINATED]).

---

## VERDICT BOX

> **PRIMARY BIN: [ASYMMETRIC-BOTH].**
>
> Channel-resolved on the srs bond tensor (the minimal host that carries the axial/shear split),
> per Grant's 2026-07-05 Q-point ruling (S keyed on DEFORMATION not stress; no-double-count), the
> time-averaged bias of a transverse wave decomposes as:
> - **AXIAL numerator S_axial:** UNTOUCHED by a ⟨A⟩=0 traveling wave (axial deformation oscillation
>   is 4th-order in the bow — sympy-proven), = cold 1. For the CONFINED mode it is the electron's
>   DC bias **S(√α)=0.996345**, y₀-independent — the hum does NOT move it.
> - **SHEAR-adjacent denominator = k_s·S_shear + T/ℓ:** carries TWO competing 2nd-order terms — the
>   saturation SOFTENING (−¼y₀²/A_y², ⟨A²⟩-keyed) and the geometric STIFFENING (+T/ℓ = +y₀²/ℓ²,
>   the #529 Part-1 law). **They do NOT cancel at the canonical yield A_y=1: dD/k₀ = +¾y₀²**
>   (stiffening wins 4:1). Cancellation would require **A_y=1/2** — a knife tell (imported yield in
>   a costume, NOT a theorem).
>
> **RESULT:** BOTH the matched traveling wave AND the confined mode MOVE ρ' (by 1.5% at the tent-edge
> bow, up to 11.4% at the elastica edge), and — the load-bearing finding — the **y₀-dependent HUM
> RESPONSE is BIT-IDENTICAL between the two (hum-factor difference ≤ 1.1×10⁻¹⁶, machine ε).** The
> auto-resonance hum moves ρ' the SAME way for radiation and matter. The ONLY travel-vs-confined
> difference is the CONSTANT numerator DC-bias factor S(√α) — which is the **pre-existing #518 matter
> operating point**, NOT anything the hum contributes. **The hum is not a channel-resolved
> discriminator.**
>
> **THE CONFLICT (surfaced verbatim, flag-don't-fix — §CONFLICT below):** the #526 remap coordinate
> ρ' = S_axial/(S_shear + T/ℓ) moves ρ' for the matched CW traveling wave (⟨A⟩=0). Canon's #518 §7 /
> matter-stiffening §4 radiation null asserts ρ_eff = ρ_cold **identically** for the pure-AC traveling
> wave. The two disagree. The #526 T/ℓ term is 2nd-order-GEOMETRIC and survives ⟨A⟩=0; canon's null
> was derived at the PRE-#526 ρ_eff = S_axial/S_shear level (WITHOUT the T/ℓ term). I do NOT resolve
> which coordinate is the correct one for the radiation null — this may implicate the #526 T-slot
> scope; Grant adjudicates.

**Consistency-vs-emergence classification:** CONSISTENCY / DC-internal (per the frozen prereg
stakes-table). This is a re-band of a DC-bias operating-point ratio; no AC readout; NOT a
framework-level result. No VALUE is derived or claimed (the /7, ρ*=9.77, 2/7 stay GR-imported).

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** translational-u elastic sector of the ratified chiral srs-z3. RANK-2 bond tensor
  `Φ_b = k_a·S_axial·P + (k_s·S_shear + T/ℓ)·(I−P)`, P=d̂⊗d̂. BOTH k_a and k_s are translational-u /
  **capacitive** springs of the SAME bond (PR#516) — NOT the ε/μ photon pair.
- **MODE:** ANALYTIC (sympy 2nd-order backbone) + direct-kernel evaluation through the MERGED #526
  Born-Huang tensor (`extract_prestress_Cij`). No new solver.
- **REGIME:** the traveling case is on an Ax3-MATCHED line (Γ_internal=0, ρ_bond=1); the confined
  case is the electron's Γ=−1 TIR-wall self-trap. Timescale-separation assumption DECLARED: the
  hum period ≪ the DC-bias relaxation time, so the S-factor Q-point is set by the DC deformation and
  the hum enters only as a 2nd-order time-averaged small-signal shift (node-up:144).
- **PHASE-STATE:** traveling = radiation (⟨A⟩=0, no DC bias); confined = the electron matter operating
  point (A_dc=√α axial bias). Both sub-yield.
- **T2 HOMONYM GUARD (#527, respected):** the transverse bow is the MECHANICAL T2-response bend of
  the bond (arm-(a) geometry), NOT the Cosserat (2,3) charge winding. "Shear channel" = the (I−P)
  block of the translational-u spring, NOT the μ-inductive photon and NOT the charge-winding. The
  two "3"s stay orthogonal (mass=A1, charge=Cosserat-winding).

---

## GRANT'S RULING (recorded verbatim, attributed Grant 2026-07-05 — the Q-point framing)

> READING A — the saturation operating point is the QUIESCENT DEFORMATION STATE RELATIVE TO REST.
> The keying variable of S(A) is the deformation ratio (A = V/V_snap ↔ bond deformation toward snap),
> NOT stress. [Consequences 1–3 recorded verbatim in the FROZEN prereg §"GRANT'S RULING".]

The **no-double-count principle** (T is a STRESS → denominator +T/ℓ only, NEVER an S-factor) is the
load-bearing constraint and is honored throughout: `channel_loading()` feeds `saturation_factor` the
DEFORMATION amplitudes only (A_dc for the numerator, the transverse RMS for the shear soft term) and
feeds the tension T only into the pre-stress `T_per_bond` slot.

---

## THE PER-CHANNEL LOADING TABLE (both cases, both channels — at the tent-edge in-regime bow y₀≈0.14)

| Channel / term | (i) TRAVELING (radiation, A_dc=0) | (ii) CONFINED (matter, A_dc=√α) |
|---|---|---|
| **AXIAL numerator** S_axial | **1.0000** (cold — hum 4th-order, untouched) | **0.99617** = S(√α) (DC bias; hum-independent) |
| **SHEAR soft** k_s·S_shear (⟨A²⟩ softening) | **0.99490** | **0.99490** (SAME) |
| **SHEAR stiff** +T/ℓ (geometric stiffening) | **+0.02039** | **+0.02039** (SAME — #529 uniform ⟨T⟩) |
| **Denominator** k_shear_eff = soft+stiff | **1.01529** | **1.01529** (SAME) |
| **ρ' = numerator/denominator** | **0.98495** | **0.98131** |
| **ρ'-move vs own cold ref** | **−0.01505** (vs ρ_cold=1) | **−0.01505** (vs S(√α)=0.99617) |
| **hum factor** (numerator divided out) | **0.98495** | **0.98495** (BIT-IDENTICAL, Δ≤1.1e-16) |

(Full log-spaced y₀ band, both arc* edges [0.70, 0.96], both dictionaries, in the output JSON.
Magnitudes reported as bands; six digits are internal-precision, not claims.)

**Reading the table:** the denominator is IDENTICAL for both wave types (both carry the same shear
softening AND the same geometric T). The numerator is the ONLY thing that differs, and it differs by
a CONSTANT (S(√α), the DC bias) that is y₀-independent — the pre-existing #518 matter operating point.
The hum-driven move (−0.01505) is the SAME for both. **The hum does not discriminate.**

---

## THE ρ'-SHIFT PER CASE, WITH BANDS

| Case | arc* edge | interior ρ' band | max |move| vs cold ref |
|---|---|---|---|
| (i) traveling | hi_tent (0.96) | [0.985, 1.000) | 1.5×10⁻² |
| (i) traveling | lo_elastica (0.70) | [0.886, 1.000) | 1.14×10⁻¹ |
| (ii) confined | hi_tent (0.96) | [0.981, 0.996) | 1.5×10⁻² |
| (ii) confined | lo_elastica (0.70) | [0.882, 0.996) | 1.14×10⁻¹ |

The y₀→0 identity endpoints (ρ'→ρ_cold for travel, ρ'→S(√α) for confined) are LABELED and EXCLUDED
from the moved band (symmetric identity treatment). The bands sit in (0.88, 1.0) — **no interior edge
lands on any armed knife target** (2, 9.7734, 7.10, 11.68 all outside the band; the move is a small
stiffening, not a chord-shaped landing).

---

## WHY NO CANCELLATION (the knife clause — derived, not steered)

The prereg armed the knife: any ratio-preserving cancellation must be a derived theorem or reported
as unexplained-numerical (weaker grade). **There is no cancellation to explain — the honest result is
NON-cancellation.** Sympy-derived (9 exact-zero residuals, `symbolic_backbone`):

```
denominator 2nd-order change:  dD/k₀ = (soft) + (stiff)
                                     = −y₀²/(4 A_y²)  +  y₀²      [at k_a=k_s=k₀, ℓ=1]
                                     = +¾ y₀²                     [at the canonical yield A_y=1]
```

The geometric stiffening (+y₀²) DOMINATES the saturation softening (−¼y₀²) by 4:1. **Cancellation
(dD=0) requires A_y=1/2** — which is NOT the canonical yield (def-vyvsn1: A_y=1). Per the frozen knife
clause, an A_y=1/2 cancellation would be the imported yield re-expressed as a factor, NOT a theorem.
So the substrate says: the traveling wave's denominator moves, and it moves because the geometric
chord tension outweighs the saturation softening at the physical yield point. **This is the honest
NON-cancellation, derived from the S-kernel Taylor series + the #529 Part-1 law, no factor un-declared.**

---

## THE PUMP-NULL CONSISTENCY CHECK (Requirement 3 — reproduced before going channel-resolved)

My channel-resolved stiff term T reconciles with the imported #529 Γ-free ABCD traveling-wave field
(`field_from_abcd_propagation`, a DIFFERENT code path) to **max_rel = 2.2×10⁻¹⁵** (`PC_consistency_529`,
can-fire proven on this real pair). The framework reproduces #529's finding — the per-bond scalar ⟨T⟩
is uniform (= (k_a/ℓ)y₀²) and identical for both wave types — BEFORE the channel split. The pump-null
is respected in the S-factors: the numerator S_axial does NOT shift for the ⟨A⟩=0 wave (no DC
rectification); only the geometric T (a stress, not an S-shift) and the 2nd-order shear small-signal
average move. **The S-factor DC operating point carries no bias for radiation — correct per canon.**

---

## CONFLICT (surfaced verbatim, flag-don't-fix — Grant adjudicates; I do NOT resolve)

The [ASYMMETRIC-BOTH] verdict turns on a disagreement between two MERGED pieces of canon. Both quoted
verbatim, both file paths given:

**Claim A — canon's radiation null** (`research/2026-07-04_matter-stiffening-rho_result.md`:146-150):
> "A pure-AC traveling wave A(t)=A₀·sin(ωt) has zero time-averaged bias ⟨A⟩=0. **ρ_eff = ρ_cold
> identically** for every A₀ … Symmetric-internal (R1 …): a pure AC field drives BOTH grades with the
> same ⟨A²⟩, so S_axial=S_shear ⟹ ρ_eff=ρ_cold, regardless of amplitude."

and its canonized sibling (`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md`:155):
> "$S_{axial}=S_{shear}\Rightarrow\rho_{eff}=\rho_{cold}$ … a symmetrically-loaded … drive — the
> radiation / pure-AC $\langle A\rangle=0$ case — is transparent to the bond-stiffness ratio … for
> every amplitude."

**Claim B — the #526 remap coordinate** (`src/scripts/vol_1_foundations/prestress_elastic_tensor.py`:449-450):
> `k_shear_eff = S_shear + T / ell    # the shifted shear spring (corrected mechanism)`
> `rho_prime = (S_axial / k_shear_eff) …    # TRUE family coordinate`

**The disagreement:** Claim A's null is stated at the coordinate ρ_eff = S_axial/S_shear (no T/ℓ
term). Claim B's "TRUE family coordinate" is ρ' = S_axial/(S_shear + T/ℓ). For the ⟨A⟩=0 traveling
wave, S_axial=S_shear=1 (Claim A's ⟨A²⟩ argument, both channels symmetric) BUT the geometric T/ℓ =
+y₀²/ℓ² is nonzero (2nd-order-geometric, survives ⟨A⟩=0, = the #529 uniform ⟨T⟩). So:
- **At Claim A's coordinate:** ρ_eff = 1/1 = ρ_cold → radiation transparent. ✅ (canon's null holds)
- **At Claim B's coordinate:** ρ' = 1/(1 + y₀²/ℓ²) < ρ_cold → radiation MOVES ρ'. ❌ (canon's null fails)

The two coordinates give OPPOSITE radiation-transparency verdicts. **This is not a bug in my driver —
both claims are computed correctly; the driver reproduces each.** The open question (which I do NOT
answer): **is the geometric T/ℓ term a legitimate part of the radiation null's coordinate, or is the
#526 T-slot a MATTER-only correction that should not be applied to the pure-AC traveling wave?**
- If T/ℓ belongs (Claim B is the true coordinate everywhere): canon's radiation null (Claim A) is
  INCOMPLETE — it omits a geometric term that DOES stiffen radiation, and the #518/§7 "radiation
  transparent" statement needs a scope caveat. The auto-resonance carrier still dies (the hum does
  not discriminate), but the radiation-transparency claim itself is at issue.
- If T/ℓ is matter-only (Claim A is the radiation coordinate, Claim B is the matter coordinate): the
  #526 remap's T/ℓ term is being MISAPPLIED to the traveling wave, and the conflict is a scope
  artifact — my driver applied the matter-coordinate to radiation. The fix is a coordinate-scope rule
  canon does not currently state.

**I cannot tell which from inside the substrate** — both are internally consistent; the resolution is
a framing call about what the #526 T/ℓ term physically MEANS for a ⟨A⟩=0 wave. Flag-don't-fix.

---

## WHAT THIS DOES / DOES NOT CLAIM

**Does claim:**
- Under Grant's Reading-A (deformation-keyed S, no-double-count), the traveling-wave denominator does
  NOT cancel at the canonical yield (dD/k₀=+¾y₀², sympy-derived) — the traveling wave MOVES ρ'.
- The hum-driven ρ'-move is BIT-IDENTICAL between radiation and matter (Δ≤1.1e-16) — **the
  auto-resonance hum is NOT a channel-resolved discriminator.** The matter/radiation difference is the
  constant numerator DC-bias (the pre-existing #518 operating point), which the hum does not touch.
- A real CONFLICT exists between the #526 T/ℓ remap coordinate and canon's #518 §7 radiation null,
  surfaced verbatim (both file:line + quote), for Grant to adjudicate.

**Does NOT claim:**
- **NOT [CHANNEL-DISCRIMINATOR-DERIVED].** The hum does not discriminate; the carrier does not survive
  channel-resolved via the hum.
- **NOT that the carrier "dies entirely" ([SYMMETRIC-BOTH]).** Both move (not both-preserve), so the
  scalar/ratio question is not a clean symmetric null either — it is the ASYMMETRIC-BOTH conflict.
- **NOT a resolution of the T/ℓ-coordinate conflict.** Flag-don't-fix; Grant adjudicates.
- **NOT any VALUE claim.** The /7, ρ*=9.77, 2/7 stay GR-imported (PR#506/#261). CONSISTENCY /
  DC-internal only.
- **NOT a claim that the #518 S-ratio mechanism is wrong.** The #518 matter-stiffening direction
  (asymmetric shear loading, S_axial/S_shear) is untouched by this arc — it lives in the NUMERATOR's
  DC bias, which this arc CONFIRMS is the only channel-resolved matter/radiation distinguisher. The
  /7-mechanism thread's fallback to #518's S-ratio mechanism alone is INTACT.
- `mass=A1` untouched (PR#260/#311). The two "3"s stay orthogonal.

---

## LEDGER — canon-forced vs engineering-choice (all magnitudes banded)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel S(A)=√(1−(A/A_y)²) | CANON-FORCED | Axiom 4 |
| 2 | Remap ρ'=S_axial/(S_shear+T/ℓ) | CANON-FORCED (MERGED) | #526 (`_prestress_tensor_at`) |
| 3 | Part-1 T=(k_a/ℓ)y₀² | DERIVED (IMPORTED) | #529 (⟨sin²⟩=½ sympy) |
| 4 | S keyed on DEFORMATION not stress; no-double-count | GRANT-RULED | 2026-07-05 (verbatim, prereg) |
| 5 | S_axial untouched by ⟨A⟩=0 wave (axial deform 4th-order) | DERIVED (sympy) | consequence 1 |
| 6 | soft term −¼y₀²/A_y² | DERIVED | S-Taylor + node-up:144 |
| 7 | dD/k₀=+¾y₀² (NO cancellation at A_y=1) | DERIVED (sympy) | the central finding |
| 8 | A_y=1/2 cancellation condition | KNIFE TELL (NOT canon) | derived — import-in-costume |
| 9 | A_dc=√α (confined axial bias) | CANON-FORCED (α-echo) | def-vyvsn1 |
| 10 | y₀↔A_shear dictionary | UNDERDETERMINED (both run; coincide at ℓ=1) | KEEP-BOTH |

**Tally: 5 canon-forced + 3 derived + 1 Grant-ruled + 1 underdetermined. 0 free parameters tuned.**

---

## CONTROL STATUS

All 5 positive controls pass, each via the #528 reconcile-gate helper with the can-fire self-test
proven on its OWN real data path:
- **PC-consistency (#529 reproduction):** max_rel = 2.2×10⁻¹⁵. ✅
- **PC-cold:** y₀→0 recovers ρ_cold=1 exactly (vs a direct T=0 tensor call). ✅
- **PC-numerator:** confined S_axial=0.996345 genuinely shifted off cold. ✅
- **PC-denominator:** analytic 2nd-order ρ'=0.984936 vs full-kernel 0.984949, within the y₀⁴
  truncation band (NOT the defining identity — the #527-defect guard). ✅
- **PC-null-liveness (Step 3.8a):** the confined pipeline reads the biased ratio S(√α)=0.996345 ≠
  ρ_cold through the IDENTICAL remap — the preservation-null's known-nonzero positive control. ✅

Synthetic HALT triggers (tests): DiscrepantHalt fires on a hand-mismatched pair; ValueError refuses a
vacuous (infinite-tolerance) gate; DeadGateError path exercised on an exact-equality gate. The gate
plumbing is proven LIVE on this arc's real data paths.

---

## FALLOUT / AUDITOR-QUEUE (surfaced; implementer does NOT land manuals)

| Site | Proposed disposition |
|---|---|
| **The #518 §7 / node-up:155 radiation null** (S_axial=S_shear ⟹ ρ_eff=ρ_cold) | **CONFLICT (candidate) — DO NOT LAND until Grant adjudicates the T/ℓ-coordinate question.** The null holds at the ρ_eff=S_axial/S_shear coordinate but FAILS at the #526 ρ'=S_axial/(S_shear+T/ℓ) coordinate for the ⟨A⟩=0 traveling wave (the geometric T/ℓ term stiffens radiation). Whether the null needs a coordinate-scope caveat, or the #526 T/ℓ is matter-only, is the open framing call. |
| **The auto-resonance carrier** (Grant's standing ruling: "the hum is the bias") | **REFINE (candidate):** the hum survives at the SCALAR ⟨T⟩ level (it biases the denominator) but is NOT a channel-resolved matter/radiation DISCRIMINATOR — it moves ρ' identically for both wave types. The matter/radiation split lives entirely in the NUMERATOR DC-bias (the #518 S-ratio mechanism), which this arc confirms is the sole channel-resolved distinguisher. |
| **The /7-mechanism thread** | **NO CHANGE:** falls back to #518's S-ratio (asymmetric shear-loading) mechanism alone, exactly as the [SYMMETRIC-BOTH] contingency in the prereg anticipated. The tension carrier adds nothing channel-resolved. /7 stays GR-imported. |
| **#526 prestress_elastic_tensor T-slot scope** | **SCOPE FLAG (candidate):** the T/ℓ term's applicability to a pure-AC ⟨A⟩=0 wave is the crux of the conflict above — canon does not currently state whether the T-slot is a matter-only correction or a universal geometric term. |

**HONEST FLAG for Grant (flag-don't-fix):** the channel-resolved test does NOT rescue the carrier —
the hum is not a discriminator. It DOES surface a real conflict between the #526 T/ℓ remap and canon's
radiation null, which turns on what the geometric tension term means for a ⟨A⟩=0 wave. That is a
framing call I leave to you, not a bug I resolve.
