# RESULT — Channel-resolved loading: the "conflict" DISSOLVES into an OPEN T-slot SCOPE FORK. Two arms, opposite verdicts, Grant's to resolve. [FORK: DC_ONLY→SYMMETRIC-BOTH / EXTENDED→ASYMMETRIC-BOTH]

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/channel-discriminator`
**Prereg (FROZEN):** `research/2026-07-05_channel-resolved-loading_prereg_FROZEN.md` (committed BEFORE the driver; commit order is the freeze proof — see the ERRATUM banner below for the one frozen-doc numeric correction).
**Driver:** `src/scripts/vol_1_foundations/channel_resolved_loading.py`
**Tests:** `src/tests/test_channel_resolved_loading.py` (35 pass)
**Output:** `src/scripts/vol_1_foundations/_output/channel_resolved_loading.json` (driver-regenerable)
**Successor to:** the merged NEGATIVE PR #529 (`research/2026-07-04_resonant-tension-law_result.md`, [RADIATION-CONTAMINATED]).

> ## RE-FRAME (2026-07-05, orchestrator review of PR #531 — 13 items, 3 MAJOR)
> The first draft of this result headlined a canon-vs-canon CONFLICT and a single [ASYMMETRIC-BOTH]
> verdict. **The review verified that the conflict DISSOLVES: the #526 T-slot is scoped to a STATIC
> DC bias (verbatim, below), and radiation moving ρ' REQUIRED this arc's re-keying of the slot to
> #529's AC cycle-averaged ⟨T⟩ — an extrapolation the arc made, not canon.** The result is therefore
> re-framed as TWO ARMS conditional on an OPEN T-slot SCOPE FORK, which is Grant's to resolve. Both
> arms are reported in full; this arc does NOT pick. (Items 2/3 fixed the control integrity; items 4/5
> corrected specific cells; all folded in below.)

---

## VERDICT BOX

> **PRIMARY: [FORK] — the verdict is CONDITIONAL on the T-slot scope, which is Grant's to resolve.**
>
> The observable the /7-mechanism candidate consumes is ρ' = S_axial / (k_s·S_shear + T/ℓ). Channel-
> resolved per Grant's 2026-07-05 Q-point ruling (S keyed on DEFORMATION-toward-rest, not stress;
> no-double-count), the decomposition is unambiguous EXCEPT for one open scope question: **does the
> #526 pre-stress T-slot accept an AC cycle-averaged ⟨T⟩, or only a static DC-bias tension?** Canon
> scopes it to the latter; this arc's radiation-moves-ρ' result needed the former. Two arms:
>
> **ARM DC_ONLY (canon's keying) → [SYMMETRIC-BOTH] at the hum level.** The #526 FROZEN prereg
> (`2026-07-04_prestress-tensor_prereg_FROZEN.md`:64-78) scopes the T-slot to a static DC bias with
> `T = bond_tension(A_axial) = Φ'(A_DC)`, which is 0 at ⟨A⟩=0, and "NO ⟨sin²⟩=½ time-average factor."
> Under this keying a pure-AC ⟨A⟩=0 traveling wave loads NOTHING (ρ'=ρ_cold exactly, every amplitude),
> AND — symmetrically — the confined mode's cycle-averaged hum ⟨T⟩ cannot enter either; only its true
> static DC bias A_dc=√α loads (numerator + the legitimate static Φ'(√α) in-slot). **The
> auto-resonance tension HUM moves NEITHER wave type → no tension discriminator → the carrier family
> is DEAD at the hum level.** The matter/radiation split is then #518's DC S-ratio asymmetry ALONE;
> #526/#527's static results are UNTOUCHED (those ARE static DC biases, legitimately in-slot).
>
> **ARM EXTENDED (this arc's re-keying) → [ASYMMETRIC-BOTH].** If the slot accepts AC cycle-averaged
> tensions (and S_shear is RMS-keyed by the R1 δn≈+¼A² small-signal shift), both wave types move ρ'
> by an INDISTINGUISHABLE hum response (hum factor bit-identical — a by-construction shared-denominator
> identity, §"THE HUM IDENTITY"). The traveling wave is then NOT ratio-preserving, and #518's radiation
> null would need revision. Even here the hum is NOT a discriminator (both move identically); the only
> travel/confined difference is the constant numerator DC-bias S(√α) — the pre-existing #518 point.
>
> **EITHER WAY, the auto-resonance TENSION HUM is not a channel-resolved matter/radiation
> discriminator.** DC_ONLY: it enters nothing. EXTENDED: it moves both identically. The carrier does
> not survive as a discriminator on either arm. The two arms differ only on whether radiation's ρ' is
> preserved (DC_ONLY) or moved (EXTENDED) — a #518-null question that turns on the T-slot scope.
>
> **Grant's Reading-A ruling BEARS on the fork** (his to apply, not ours): the Q-point is the quiescent
> DEFORMATION state relative to rest — and a passing wave's cycle-averaged stress is arguably not a
> quiescent bias, which would favor DC_ONLY. But that reading is Grant's to make.

**Consistency-vs-emergence:** CONSISTENCY / DC-internal. No VALUE derived or claimed (/7, ρ*=9.77,
2/7 stay GR-imported, PR#506/#261). This re-bands a DC-bias operating-point ratio; no AC readout.

---

## ERRATUM (2026-07-05, review item 5b) — one numeric correction to the FROZEN prereg

The FROZEN prereg (`research/2026-07-05_channel-resolved-loading_prereg_FROZEN.md`:134) states
`S(√α) ≈ 0.99617`. **That value is WRONG.** The correct value is **S(√α) = 0.996345** (verified:
`saturation_factor(√α, 1.0) = 0.9963446428975768`). The frozen-prereg body is preserved (Rule 12);
this erratum banner records the correction. All numbers in THIS result doc use the correct 0.996345.

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** translational-u elastic sector of the ratified chiral srs-z3. RANK-2 bond tensor
  `Φ_b = k_a·S_axial·P + (k_s·S_shear + T/ℓ)·(I−P)`, P=d̂⊗d̂. BOTH k_a, k_s are translational-u /
  **capacitive** springs of the SAME bond (PR#516) — NOT the ε/μ photon pair.
- **MODE:** ANALYTIC (sympy 2nd-order backbone) + direct-kernel evaluation through the MERGED #526
  Born-Huang tensor (`extract_prestress_Cij`). No new solver.
- **REGIME:** traveling = Ax3-MATCHED line (Γ_internal=0); confined = electron Γ=−1 TIR-wall.
  Timescale-separation DECLARED: hum period ≪ DC-bias relaxation time. **The T-slot scope fork is
  precisely the question of whether the hum's cycle-average is a legitimate slot input at this
  separation — the open item.**
- **PHASE-STATE:** traveling = radiation (⟨A⟩=0, no DC bias); confined = electron matter point
  (A_dc=√α). Both sub-yield.
- **T2 HOMONYM GUARD (#527):** the transverse bow is the MECHANICAL T2-response bend, NOT the Cosserat
  (2,3) charge winding. "Shear channel" = the (I−P) block of the translational-u spring. Two "3"s
  orthogonal (mass=A1, charge=Cosserat-winding).

---

## GRANT'S RULING (recorded verbatim, attributed Grant 2026-07-05 — the Q-point framing)

> READING A — the saturation operating point is the QUIESCENT DEFORMATION STATE RELATIVE TO REST.
> The keying variable of S(A) is the deformation ratio (A = V/V_snap ↔ bond deformation toward snap),
> NOT stress. [Consequences 1–3 recorded verbatim in the FROZEN prereg §"GRANT'S RULING".]

The **no-double-count principle** (T is a STRESS → denominator +T/ℓ only, NEVER an S-factor) is
honored on both arms. Reading-A's "quiescent deformation relative to rest" is what BEARS on the fork:
whether a passing wave's cycle-averaged stress counts as a quiescent bias is the crux — Grant's call.

---

## THE T-SLOT SCOPE FORK (the load-bearing open item — VERBATIM sources; Grant's to resolve)

**Canon's keying (ARM DC_ONLY) — the #526 FROZEN prereg**
(`research/2026-07-04_prestress-tensor_prereg_FROZEN.md`:64-78, verified verbatim this session):
> "the operating point A is a **static DC bias** (R2 varactor picture, keyed on field amplitude V∼E),
> NOT the amplitude of an AC standing wave. … **CONSEQUENCE: NO ⟨sin²⟩=½ time-average factor** — there
> is no oscillation to average over; the reference tension is `Φ'(A)` at the static bias A, factor = 1."

and its keying (`:100-120`): `T(A) = Φ'(A) = bond_tension(A_axial)`, with `Φ'(0)=0` (cold reference
un-tensioned). So for a pure-AC ⟨A⟩=0 wave, **T = Φ'(0) = 0** — the slot is empty; radiation preserves
ρ' exactly. This is canon's own keying, not a choice this arc made.

**This arc's re-keying (ARM EXTENDED)** fed the slot the #529 CYCLE-AVERAGED ⟨T⟩ = (k_a/ℓ)y₀²
(nonzero at ⟨A⟩=0) and RMS-keyed S_shear via the R1 δn≈+¼A² small-signal shift (node-up:144). Under
this reading the traveling wave moves ρ'. **This is an EXTRAPOLATION of the #526 slot beyond its
frozen static-DC scope — legitimate to explore, but NOT canon.**

**The fork:** does the pre-stress T-slot (and the S-shift keying) accept AC cycle-averaged quantities,
or only static DC biases? Canon says static-DC. Grant's Reading-A (quiescent deformation) leans the
same way. But the extension is physically arguable (a real hum does carry a persistent 2nd-order mean
stress), so this arc reports both and does NOT pick. **A one-line Grant ruling closes it.**

---

## THE PER-CHANNEL LOADING TABLE (both cases, both channels, BOTH ARMS — at tent-edge bow y₀≈0.1428)

**ARM DC_ONLY (canon keying):**

| Channel / term | (i) TRAVELING (radiation, A_dc=0) | (ii) CONFINED (matter, A_dc=√α) |
|---|---|---|
| AXIAL numerator `S_axial` | **1.000000** (cold) | **0.996345** = S(√α) (DC bias) |
| SHEAR soft `k_s·S_shear` | **1.000000** (no AC RMS enters) | **1.000000** (no AC RMS enters) |
| SHEAR stiff `+T/ℓ` = Φ'(A_dc)/ℓ | **0.000000** (Φ'(0)=0) | **0.085321** = Φ'(√α)/ℓ (static DC tension) |
| Denominator `k_shear_eff` | **1.000000** | **1.085321** |
| **ρ'** | **1.000000** (radiation transparent) | **0.918019** (DC-bias move, NOT a hum move) |
| **HUM move** (ρ' variation over y₀) | **0** | **0** (ρ' is y₀-independent) |

**ARM EXTENDED (this-arc re-keying):**

| Channel / term | (i) TRAVELING (A_dc=0) | (ii) CONFINED (A_dc=√α) |
|---|---|---|
| AXIAL numerator `S_axial` | **1.000000** (cold; hum 4th-order) | **0.996345** = S(√α) (DC bias) |
| SHEAR soft `k_s·S_shear` | **0.994887** (RMS-keyed) | **0.994887** (SAME) |
| SHEAR stiff `+T/ℓ` (cycle-avg ⟨T⟩) | **0.020400** | **0.020400** (SAME — #529 uniform ⟨T⟩) |
| Denominator `k_shear_eff` | **1.015287** | **1.015287** (SAME) |
| **ρ'** | **0.984943** | **0.981343** |
| **HUM move** (ρ' variation over y₀) | **−0.0151** (moves) | **−0.0151** (moves, SAME) |

(Full log-spaced y₀ band, both arc* edges [0.70, 0.96], both dictionaries, both arms, in the JSON.
Magnitudes are BANDS; six digits are internal precision, not claims.)

---

## THE HUM IDENTITY (item 5a — labeled as the by-construction identity it is)

On the EXTENDED arm the "hum factor" (ρ' with the constant numerator divided out) is IDENTICAL between
travel and confined. **This is an ALGEBRAIC identity, NOT a measured null.** ρ' = S_axial · [1/(k_s·
S_shear + T/ℓ)]; S_axial is a constant (the DC bias) that divides out, and the bracket (the shared
denominator) is the SAME for both wave types under this arm (same S_shear, same ⟨T⟩). So
hum_factor_travel ≡ hum_factor_confined by construction; the ≤1.1×10⁻¹⁶ is machine round-off on an
algebraic identity, not a physical coincidence. (The prior draft's "bit-identical, machine ε" framing
over-dressed a bookkeeping identity as a measured result.)

---

## WHY NO CANCELLATION (the knife clause — derived, not steered)

On the EXTENDED arm the denominator does NOT cancel: sympy-derived (11 exact-zero residuals),
`dD/k₀ = −¼y₀²/A_y² + y₀² = +¾y₀²` at the canonical yield A_y=1. The geometric stiffening dominates
the saturation softening 4:1. Cancellation (dD=0) would require **A_y=1/2** — a knife tell (imported
yield in a costume), NOT a theorem. So on the EXTENDED arm the honest result is NON-cancellation. On
the DC_ONLY arm the question is moot: neither term enters for radiation (both are zero at ⟨A⟩=0), so
ρ' is preserved trivially — the correct kind of "cancellation" (no loading at all), not a coincidence.

---

## THE PUMP-NULL CONSISTENCY CHECK (Requirement 3 — reproduced before going channel-resolved)

My channel-resolved cycle-averaged ⟨T⟩ (the EXTENDED-arm stiff term) reconciles with the imported
#529 Γ-free ABCD traveling-wave field (`field_from_abcd_propagation`, a different code path) to
**max_rel = 2.2×10⁻¹⁵** (`PC_consistency_529`, can-fire proven on this real pair). The framework
reproduces #529's uniform scalar ⟨T⟩. Crucially, this reproduction is EXACTLY the extrapolation the
fork is about: #529's ⟨T⟩ is the cycle-averaged AC quantity; whether it belongs in the #526 static-DC
slot is the open question. The consistency check confirms my bookkeeping of the AC ⟨T⟩ is correct; it
does not license feeding it into the DC-scoped slot (that is the EXTENDED arm's premise, flagged).

---

## CORRECTED CONFLICT CELL (item 4 — the false "✅" fixed)

The prior draft's CONFLICT table claimed: "At Claim A's coordinate ρ_eff = S_axial/S_shear = 1/1 = 1
✅ (canon's null holds)." **That cell is FALSE under this arc's own EXTENDED bookkeeping:** the
RMS-keyed S_shear shifts (0.994887 at tent edge) even at the OLD coordinate, so ρ_eff = S_axial/S_shear
= 1/0.994887 = **1.00514 ≠ 1** — it MOVES (+0.5%) even without the T/ℓ term. The implication carried
honestly into both arms: **the S_shear RMS-shift is itself part of the EXTENDED re-keying** — under
canon's DC keying (ARM DC_ONLY) S_shear does NOT shift for ⟨A⟩=0 either (S is keyed on the DC
deformation, which is zero). So the OLD-coordinate move is not evidence against canon; it is another
face of the same EXTENDED extrapolation. On the DC_ONLY arm both the T/ℓ term AND the S_shear shift
vanish for radiation, and ρ_eff = ρ' = 1 exactly. The fork is clean; the false ✅ is retracted.

---

## WHAT THIS DOES / DOES NOT CLAIM

**Does claim:**
- The auto-resonance TENSION HUM is NOT a channel-resolved matter/radiation discriminator on EITHER
  arm (DC_ONLY: enters nothing; EXTENDED: moves both identically, a by-construction identity).
- The verdict is a FORK conditional on the #526 T-slot scope (DC_ONLY→[SYMMETRIC-BOTH],
  EXTENDED→[ASYMMETRIC-BOTH]), surfaced with verbatim canon sources, Grant's to resolve.
- Under canon's own keying (DC_ONLY), radiation preserves ρ' exactly and the carrier family is dead —
  the matter/radiation split is #518's DC S-ratio asymmetry alone (the /7-thread fallback the prereg
  anticipated).

**Does NOT claim:**
- **NOT a canon-vs-canon CONFLICT** (the prior draft's headline; the review dissolved it — the #526
  slot is DC-scoped, so radiation-moves-ρ' is this arc's extrapolation, not canon disagreeing with
  itself).
- **NOT [CHANNEL-DISCRIMINATOR-DERIVED].** The hum does not discriminate on either arm.
- **NOT a resolution of the T-slot scope fork.** Grant's to resolve; both arms reported.
- **NOT any VALUE claim.** CONSISTENCY / DC-internal only.
- **NOT that Grant's Reading-A ruling failed.** Reading-A was APPLIED and STANDS on both arms
  (no-double-count honored). It is the CARRIER hypothesis that failed to yield a hum discriminator —
  the ruling is the tool, not the casualty (item 5d).

---

## LEDGER — canon-forced vs engineering-choice (all magnitudes banded)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel S(A)=√(1−(A/A_y)²) | CANON-FORCED | Axiom 4 |
| 2 | Remap ρ'=S_axial/(S_shear+T/ℓ) | CANON-FORCED (MERGED) | #526 |
| 3 | Part-1 cycle-avg ⟨T⟩=(k_a/ℓ)y₀² | DERIVED (IMPORTED) | #529 |
| 4 | S keyed on DEFORMATION not stress; no-double-count | GRANT-RULED | 2026-07-05 (verbatim) |
| 5 | S_axial hum-independence | PARTLY DERIVED (item 5c) | sympy covers the axial-osc term (4th-order); the FULL numerator invariance also rests on Grant's no-double-count ruling (the stress does not re-enter S). Graded honestly: sympy + ruling, not pure-sympy. |
| 6 | soft term −¼y₀²/A_y² (EXTENDED) | DERIVED | S-Taylor + node-up:144 |
| 7 | dD/k₀=+¾y₀² (NO cancellation, EXTENDED) | DERIVED (sympy) | central finding |
| 8 | A_y=1/2 cancellation condition | KNIFE TELL (NOT canon) | derived |
| 9 | A_dc=√α (confined bias) | CANON-FORCED (α-echo) | def-vyvsn1 |
| 10 | T-slot scope (DC-only vs AC-extended) | OPEN FORK (Grant's) | #526 prereg:64-78 vs this arc |
| 11 | PC-denominator residual y0⁴/32 | DERIVED (sympy) | honest gate band (item 2) |

**Tally: 5 canon-forced + 4 derived + 1 partly-derived + 1 open-fork. 0 free parameters tuned.**

---

## CONTROL STATUS (items 2+3 fixed)

All 5 positive controls pass via the #528 `ReconcileGate`, can-fire proven on OWN real data paths:
- **PC-consistency (#529):** max_rel 2.2×10⁻¹⁵. ✅
- **PC-cold (item 3 fixed):** ρ'=1 vs the algebraic cold identity AND ν(ρ*=9.7734) vs the merged
  NU_VAC=2/7 (independent provenance; ν is pole-divergent at cold ρ=1 so checked at ρ* where
  well-defined). ✅
- **PC-numerator (item 3 fixed):** S_axial(√α)=0.996345 vs the RAW √(1−A²) formula evaluated directly
  (a different code path than `saturation_factor`). ✅
- **PC-denominator (item 2 fixed):** honest rtol = 3× the sympy-DERIVED y0⁴/32 residual (~4×10⁻⁵),
  NOT the old vacuous 5·y0²≈0.10; the dropped-soft-term AND sign-flipped-soft-term mutations are both
  REJECTED (proven live). ✅
- **PC-null-liveness (Step 3.8a):** the confined pipeline reads the biased ratio S(√α)=0.996345 ≠
  ρ_cold. ✅

Synthetic HALT triggers: DiscrepantHalt on mismatch; ValueError on vacuous (infinite) tolerance;
DeadGate path exercised; plus the item-2 dropped/flipped-term rejections. Gate plumbing proven live on
this arc's real data.

---

## FALLOUT / AUDITOR-QUEUE (surfaced; implementer does NOT land manuals)

| Site | Proposed disposition |
|---|---|
| **#526 prestress T-slot scope** (`2026-07-04_prestress-tensor_prereg_FROZEN.md`:64-78) | **SCOPE-FORK candidate, DO NOT LAND until Grant rules.** Does the pre-stress T-slot accept an AC cycle-averaged ⟨T⟩ (EXTENDED) or only a static DC-bias Φ'(A_DC) (DC_ONLY, the frozen scope)? The channel-resolved verdict is conditional on this. Grant's Reading-A leans DC_ONLY. |
| **#518 §7 / node-up:155 radiation null** | **CONDITIONAL:** holds unchanged on ARM DC_ONLY (canon keying → radiation preserves ρ'). Would need a revision ONLY on ARM EXTENDED. NOT a confirmed conflict — conditional on the fork above. |
| **The auto-resonance carrier** (Grant's standing ruling: "the hum is the bias") | **REFINE:** Grant's Reading-A ruling was APPLIED and STANDS. The CARRIER hypothesis (that the tension hum is a channel-resolved matter/radiation discriminator) FAILED: on DC_ONLY the hum enters nothing; on EXTENDED it moves both identically. The ruling is the tool; the carrier is the casualty (NOT the ruling). The matter/radiation split lives in the numerator DC-bias (#518 S-ratio) on both arms. |
| **The /7-mechanism thread** | **NO CHANGE:** falls back to #518's S-ratio (asymmetric shear-loading) mechanism alone, exactly as the [SYMMETRIC-BOTH] contingency anticipated. /7 stays GR-imported. |

**HONEST FLAG for Grant (flag-don't-fix):** the channel-resolved test does not rescue the carrier as
a discriminator on either arm. The one open item is the T-slot scope fork — a one-line ruling
(does the slot take AC cycle-averaged tension, yes/no?) closes it and selects the arm.
