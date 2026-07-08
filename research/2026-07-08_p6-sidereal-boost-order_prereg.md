# P6 — sidereal boost-order re-derivation: radiation-Doppler O(β) vs static-motional O(β²)

**Status:** **FROZEN PRE-REG.** Freezes the FORK and the ADJUDICATION CRITERION before the
derivation/result commit. Does NOT state the answer — states the two candidate orders and the
one physical test that selects between them (timestamp-ordered: this commit precedes the result).
**Date:** 2026-07-08
**Class:** CONSISTENCY. This audits an order-of-magnitude *registration* against a first-principles
re-derivation. It mints NO new claim-id, NO new constant, touches NO axiom. Q=137 stays empty.
**Contention:** P6 in the paper-hardening ledger.
**Driver:** `src/scripts/vol_9_device/p6_sidereal_boost_order.py` · **Result:** `research/2026-07-08_p6-sidereal-boost-order_result.md`
**Paper loci under audit (do NOT edit here — orchestrator integrates):**
`papers/2026_birefringence_letter/main.tex:420-432`, `papers/2026_birefringence_letter/provenance.md:40-43`.

---

## §0 WHAT THE PAPER CURRENTLY REGISTERS (verbatim, for the SHA-pin)

- `main.tex:424-427`: *"modulating the birefringence coefficient at the fractional level `(v/c)²≃1.5e-6`
  with sidereal and annual periods. Operationally, a pump-on flip probability measured across many
  sidereal days would carry `∼1.5e-6` fractional sidebands at the sidereal frequency (and its harmonics),
  phased to the known CMB dipole direction."*
- `provenance.md:42-43`: *"sidereal modulation sidebands at `(v/c)² = (370e3/c)² = 1.523×10⁻⁶`."*

**Provenance of the `(v/c)²`:** it is the order of the STATIC motional-field paragraph immediately above
(`main.tex:408-411`): a lab magnet of `2.5 T` whose *only* frame-induced field is the motional
`E ∼ vB`, giving `A² ∼ 7e-23`. That paragraph is about a STATIC field. The sidereal paragraph then
applies the SAME `(v/c)²` order to the pump/probe modulation.

## §1 THE LOAD-BEARING PREMISE (stated, not hidden)

The sidereal prediction exists ONLY IF **the model's dynamical response frame is the CMB rest frame**
(v ≈ 370 km/s). This is the paper's own conditional at `main.tex:420-421` ("If the model's response
frame coincides with the CMB rest frame …"). Note the *internal tension* we are NOT resolving here:
`main.tex:404-406` states the prediction is "stated in the lab frame of the optical focus, where the
pump field magnitude is defined" — i.e. lab frame. If the response frame is the lab frame, there is
**no sidereal signal at all**. This prereg audits the ORDER *given the CMB-frame premise*; it does not
adjudicate the frame. Flag-don't-fix: the frame choice is surfaced for Grant, not silently picked.

## §2 THE FORK (frozen)

Which transform does the **signal-carrying field** obey in the response frame?

- **Branch (a) — RADIATION field.** The birefringence is driven by the PUMP: a propagating EM plane
  wave. A plane wave's E-amplitude transforms by the relativistic Doppler factor
  `D(θ) = 1 / [γ(1 − β cosθ)] = γ(1 + β cosθ')`. **Expected order: O(β)** (linear-in-β term present).
- **Branch (b) — STATIC field.** If the signal-carrying field is a static reactive field (like the
  lab magnet's), its magnitude transforms by the tensor factor `γ ≈ 1 + β²/2` (transverse) or is
  unchanged (longitudinal). **Expected order: O(β²)** (NO linear-in-β term). This is what the paper
  registered.

## §3 THE DISCRIMINATING PHYSICS (the one test)

**Does the signal-carrying field's amplitude transform have a nonzero linear-in-β coefficient?**

- A propagating vacuum EM mode (E and B locked as `B = E/c`) carries a `v×B` cross-term ⇒ the boosted
  amplitude has a `+β cosθ` term ⇒ **linear coeff ≠ 0 ⇒ branch (a), O(β)**.
- A static field (no locked companion, or `v×B = 0` in its own analysis) has amplitude factor `γ` whose
  β-expansion starts at `β²` ⇒ **linear coeff = 0 ⇒ branch (b), O(β²)**.

**Adjudication rule (frozen):** compute the β-expansion (sympy, to O(β²)) of (i) the plane-wave Doppler
factor `D` and (ii) the static magnitude factor `γ`. Read the linear-in-β coefficient of each.
- `D`'s linear coeff `≠ 0` **and** `γ`'s linear coeff `= 0` ⇒ the pump is branch (a) ⇒ **verdict O(β)**.
- Both linear coeffs `= 0` ⇒ **verdict O(β²)**, registration stands.

## §4 PROPAGATION TO THE OBSERVABLE (frozen mapping)

The repo observable chain (`ave.bench.birefringence`): `δn_bir = −½A²`, `A = E/E_YIELD` ⇒ `δn ∝ E²`;
the flip probability `P_flip = sin²(Δφ/2) ≈ (Δφ/2)²` with `Δφ ∝ δn·L` ⇒ **`P_flip ∝ E⁴`**. So under a
field-amplitude factor `F`:
- `δn_bir ∝ F²` → fractional modulation `F² − 1`.
- `P_flip ∝ F⁴` → fractional modulation `F⁴ − 1`.

For branch (a), `F = D`: leading modulations `2β cosθ` (coefficient) and `4β cosθ` (flip probability).
For branch (b), `F = γ`: leading modulations `O(β²)`.

## §5 ANGULAR / TEMPORAL SIGNATURE (pre-registered)

`cosθ(t) = n̂(t)·d̂`, lab optical axis `n̂` rotating with Earth, CMB dipole `d̂` fixed inertial,
decomposes as `cosθ(t) = c₀ + c₁ cos(Ω_sid t − φ)`.
- **Branch (a) prediction:** the linear `β cosθ` term ⇒ a **FIRST (fundamental) sidereal harmonic**
  is the dominant modulation; the `β²cos²θ` piece contributes a SECOND harmonic (2×sidereal) suppressed
  by β. Annual sideband from Earth's orbital velocity vector-adding to the CMB boost (`v_orb/v_CMB`).
- **Branch (b) prediction:** no linear term ⇒ the dominant modulation is `cos²θ` ⇒ a **SECOND harmonic**
  (2×sidereal) plus a DC shift; NO first-harmonic sidereal signal at leading order.

**The harmonic content is itself a discriminator:** first-harmonic-dominant ⇒ (a); second-harmonic-only
⇒ (b). This is pre-registered so the result cannot retro-fit the harmonic to the order.

## §6 DISCIPLINE GATES (frozen)

- **ave-canonical-source:** `c` imported from `ave.core.constants.C_0`; NEVER hardcoded. `v_CMB` and
  `v_orb` are EXTERNAL astrophysical inputs, labeled, NOT AVE constants. `verify_constants()` asserts
  `C_0` CODATA-exact and that `β²` reproduces the registered `1.523e-6` (confirming same quantity audited).
- **consistency-vs-emergence:** CONSISTENCY. The corrected number rides on the external ratio `β = v_CMB/c`.
  NOT an AVE emergence. No headline emergence claim.
- **pure-AVE-corpus:** our own re-derivation. No external attribution in any tracked file/commit.
- **do-NOT-edit-paper/ledger:** this branch produces prereg + result + driver ONLY. Orchestrator integrates.
- **NO self-merge:** PR opened DO-NOT-MERGE for orchestrator review.
