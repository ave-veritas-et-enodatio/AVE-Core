# PREREG (FROZEN) — the end-to-end bond force PER LOADING PATH from the fixed-arc-length K4 microfoundation

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/bond-force-sign-rule`
**Target:** derive the sign AND magnitude of the per-bond end-to-end axial force for TWO loading
paths (transverse pluck vs axial end-load) from the canonical fixed-arc-length constraint
`A²+S²=arc*²`, then feed both through the merged #526 remap machinery (consumed, not reimplemented).
**This prereg is FROZEN before the driver** (commit order proves it). Bins verbatim below; no post-data
edits (Rule 11).

**Resolves the OPEN FORK left by PR #526** (`research/2026-07-04_prestress-tensor_result.md:53-60,278-294,365-371`):
the SIGN of the end-to-end bond force, un-adjudicated there (stretched-pair T>0 assumed vs canonical
bowed-strut compression T<0).

**Stacks on (all MERGED, grep-verified this session at branch HEAD 8e21c72a):**
- PR #526 `research/2026-07-04_prestress-tensor_result.md` + `src/scripts/vol_1_foundations/prestress_elastic_tensor.py`
  (the remap: `ρ' = S_ax/(S_shear + T/ℓ)`, cap `ρ'_max = S_ax·ℓ/T`; δ_y ledger row = ENGINEERING/NORMALIZATION-CHOICE).
- Ax4 microfoundation `manuscript/ave-kb/common/axiom-register.md:189` (fixed-arc-length K4 bond bowing,
  `A²+S²=arc*²` single fixed-length constraint, arc* banded 0.89–0.96 ℓ_node tent / ~0.70–0.76 elastica).

---

## SUBSTRATE-FIRST SECTOR HEADER

- **SECTOR:** the K4/srs bond microfoundation (Ax4 quarter-arc kernel as a fixed-arc-length strut).
  Arm (a) = **T2-delivered** transverse bias (the self-trap bow response). Arm (b) = **A1-delivered**
  axial bias (the gravitational/dilatational end-load). **Do NOT cross-wire** (mass=A1, the load;
  transverse bow=T2, the response — corpus grammar, `axiom-register.md:189`
  "axial A1 dilatation load → transverse T2 bow response").
- **MODE:** quasi-static loading-path analysis on the bond microfoundation + small-signal tensor
  readout (via the #526 remap). Symbolic (sympy) force derivation FIRST; numeric bands second.
- **REGIME:** quasi-static about a static DC bias. Op14 ON. **PHASE-STATE = saturated** (S<1, sub-yield
  interior; A→arc* is the yield wall). A→0 is the Maxwell/no-load limit (the positive-control anchor).
- **DC-vs-AC:** the bias is a **static DC** amplitude (R2 varactor, `node-up-small-large-signal.md:118,:40,:145`)
  ⟹ time-average factor 1 (inherited from #526; NOT re-derived, NOT hand-set).
- **COORDS (A46):** the force is derived in the bond's own **arc-length/phase-space** coordinate
  (A_axial projection, S_transverse bow); the tensor readout is in real-space/spatial-Brillouin via
  the #526 pipeline. Each in its own coordinate — A46-clean, matching #526.
- **CLASS:** CONSISTENCY (this resolves the SIGN of a #526 consistency-class object; no new value
  derivation, no emergence claim). 2/7, 9.7734, ρ'_max≈11.68, 1/√α, ½, ¼, the arc* band edges are
  VISIBLE knife targets — none tuned toward (anti-tune ledger + frozen bins are the guard).

---

## ORCHESTRATOR RULING (2026-07-04, recorded verbatim — Reading (b), run both magnitude laws banded)

Surfaced the magnitude-law plumber question (the sign is clean and channel-keyed, but the two arms
have DIFFERENT magnitude laws — arm (a) 2nd-order geometric `~y²`, arm (b) 1st-order `|Φ'(A)|`).
**Orchestrator ruling: READING (b), run both magnitude laws banded per arm, with conditions.**
Rationale: the bin verdict is sign-keyed (cap-vs-uncap depends on `sign(T)` alone), so the
magnitude noun is a **bands question**, and Grant's standing preference for exactly this shape is
run-both-blind/engine-decides (documented ruling pattern; Grant can override at review). Conditions
(binding on this arc):

1. **Prereg (this doc) declares the magnitude-law noun an OPEN GRANT-FORK resolved-by-banding for
   this arc.** Arm (a) banded over {its own derived 2nd-order pluck law, the #526 `|Φ'(A)|` law};
   arm (b) banded over {`|Φ'(A)|` compressive, the 2nd-order geometric law}. **Neither is baked as
   "the" law.**
2. **The result doc reports the per-law ρ'/ν tracks SEPARATELY per arm (FOUR tracks)**, not just the
   envelope — Grant rules on the noun at review with the data in hand. The envelope is a summary
   view, not the finding.
3. **The sign-keying corpus-grounding goes in the result doc §corpus-grounding with verbatim grep
   quotes** (`axiom-register.md:189` "axial A1 dilatation load → transverse T2 bow response";
   `vocabulary-register.md:664` V_yield=T2-wall) — that the fork resolution was already in canon's
   grammar is itself a reportable finding.
4. **The plateau P_c = k_b·ℓ/4 (arm b post-buckling) — knife-check the ¼ explicitly.** Derived
   pre-freeze: the ¼ = (½ bend-energy prefactor) × (½ tent half-chord chain), a MECHANICAL
   tent-geometry factor (a pinned-pinned Euler elastica gives π² instead), a force in kernel units
   (dimensionally distinct from a charge-fraction ¼). **KNIFE=noise**, reported under coincidence
   discipline in the result doc, not in passing.
5. **Everything else unchanged:** bins as frozen, controls HALT-gated, the DISCREPANT-HALT synthetic
   unit test, bands over arc*, no self-merge.

---

## THE PHYSICAL PICTURE (mechanical, before equations)

- The bond is a **fixed-arc-length strut** (arc*, `axiom-register.md:189`). Two collective
  coordinates: `A` = axial projection (end-to-end chord), `S` = transverse bow, tied by
  `A²+S²=arc*²`. Inextensibility does NOT strictly hold — ρ=k_a/k_b ∈ [2,5.3] — so the strut has a
  finite axial stretch stiffness `k_a` AND a finite transverse bend stiffness `k_b`.
- **The LOADING PATH fixes the force**, not the constraint alone. Which coordinate is clamped and
  which is driven picks the force.
- **Arm (a) transverse pluck (T2 self-trap):** endpoints HELD at node spacing (chord A clamped ≈ ℓ),
  bow S DRIVEN. To bow a clamped-ends strut the arc must lengthen → axial stretch → the end force is
  the **string TENSION** the stretched arc exerts, pulling the ends together. Guitar-string picture.
- **Arm (b) axial end-load (A1/gravity bias):** end displacement IMPOSED (chord A driven below
  natural ℓ), bow S FREE to equilibrate on the fixed-arc constraint → the strut **BUCKLES**; the end
  force approaches the buckling load as the bow develops. Euler-strut picture.

---

## THE DERIVATION (done pre-freeze, sympy-verified — the prereg records the derived law, the driver reproduces + bands it)

Energy convention (stated per condition 1 of #526's δ_y ledger discipline): the kernel
`Φ''(a)=k0·√(1−a²)` is the AXIAL tangent stiffness (`scale_invariant.py:107-156`,
`saturated_elastic_tensor_result.md:71-72`); its double integral with `Φ(0)=Φ'(0)=0` is the axial
constitutive energy `Φ(A)`, with `Φ'(0)=0`, `Φ''(0)=k0` (Maxwell recovered). Sympy-verified this
session: `Φ'(A) = k0·(A√(1−A²)+arcsin A)/2` (matches #526 `bond_tension`, integral−closed-form = 0).

**Arm (a) — TRANSVERSE PLUCK (chord clamped at ℓ, bow y driven):**
> `T_a(y) = k_a·ℓ·(1 − ℓ/√(ℓ²+4y²))`, leading order `T_a ≈ (2 k_a/ℓ)·y²`.
> **Sign = +TENSION.** `T_a(0)=0` (vanishes quadratically — POSITIVE CONTROL, guitar-string slack
> limit). Second-order geometric law.

**Arm (b) — AXIAL END-LOAD (chord driven below ℓ, bow S free):**
> post-buckling end force = `−|Φ'(A)|` magnitude with the axial constitutive law (the SAME law #526
> used), sign **COMPRESSIVE (T<0)**; the tent post-buckling plateau is `P_c = k_b·ℓ/4` (buckling-load
> analog, FINITE as bow→0⁺ — POSITIVE CONTROL, Euler-strut phenomenology). Pre-buckling branch:
> Hooke `k_a·u`, compressive, → 0 as u→0.

**Reconciliation (sympy + numeric, this session):** the axial arm (b) magnitude = `|Φ'(A)|` (the
exact #526 law, first-order, →A at small A), sign compressive; #526 used `|Φ'(A)|` with tensile
sign. **The sign is the ONLY difference between arm (b) and #526.** Arm (a) pluck has a DIFFERENT
(2nd-order, weaker) magnitude law. So the two arms give **opposite-sign** end forces; the magnitude
laws differ; the cap-vs-uncap remap structure depends on `sign(T)` ALONE.

---

## Step 3.5 — dimensional / magnitude analysis at canonical primitives (mandatory)

- **Kernel units** k0 = 1 (`saturated_elastic_tensor.py:139`, units-into-ρ convention, inherited).
  ℓ = per-bond `|d|` = 1 on srs (`srs_primitive:293`, read-off geometry, inherited).
- **k_a, k_b** are the axial/bend stiffnesses; ρ=k_a/k_b ∈ [2,5.3] (`axiom-register.md:189`). At the
  swapped-spring operating point `k_a=S(A_axial)`, `k_b=S(A_shear)` (#521/#518 convention, inherited).
- **arc\* band** ⟹ δ_y ∈ [0.70, 0.96] (`axiom-register.md:189`, the #526 ledger row). Every FORCE
  magnitude and every ρ'/ν track is reported as a BAND over this range, never six-digit.
- **cap magnitude** `ρ'_max = S_ax·ℓ/T`: at δ_y=1, T=Φ'(√α)=0.08532 ⟹ cap ≈ 11.68 (#526); over the
  arc* band ≈ 12.2–16.7 (#526 §7). ρ'_max ≈ 1/√α to 0.24% is the TRIVIAL small-A expansion T≈k₀A at
  A=√α (#526 §4), NOT a new coincidence — inherited, re-stated as noise under the knife.
- **plateau** `P_c = k_b·ℓ/4` ⟹ 0.25 at k_b=ℓ=1; ¼ is tent-geometry (condition 4), KNIFE=noise.

---

## DISCRIMINATING OUTCOMES — BINS (FROZEN VERBATIM; no fall-through else; DISCREPANT-HALT reachable + unit-tested)

- **[SIGN-RULE-DERIVED]** — the two loading paths give OPPOSITE-sign end forces from the same
  constraint, each canon-forced ⟹ the fork resolves into a channel-keyed rule: **pluck→tension→capped
  track; end-load→compression→uncapped track.** Report the rule and BOTH tracks (four sub-tracks per
  condition 2). *Predicted most-likely (from the pre-freeze derivation): this bin.*

- **[SAME-SIGN]** — both paths give the same sign ⟹ the both-ways hypothesis FAILS; report which sign
  wins, why, and what that does to the #526 fork.

- **[PATH-INDETERMINATE]** — the constraint + kernel energy underdetermine the end force without
  additional structure the canon does not supply (e.g. a bending-stiffness PROFILE beyond the single
  k_b) ⟹ honest bin: report exactly what is missing and what canon would need to supply.

**Sector classification (v1.5, stakes-table):** the decision observable (sign of the per-bond axial
force, and the cap-vs-uncap remap it induces) is **DC-internal** (a DC medium-state quantity; the
tensor readout is a same-pipeline DC consistency check, not an AC channel). No pure-AC null is at
stake; no framework-level-negative is claimed (this is a CONSISTENCY-class sign adjudication).

**BIN SELECTOR — NO fall-through else.** The selector maps `(sign(T_pluck), sign(T_endload))` →
{both-opposite → SIGN-RULE-DERIVED; both-same → SAME-SIGN; either force analytically undefined /
requiring un-supplied structure → PATH-INDETERMINATE}. A **loud DISCREPANT-HALT** fires (raises, does
NOT bin) if the derived sign contradicts the remap it feeds — specifically if a force tagged TENSION
(T>0) yields an UNCAPPED `k_shear_eff ≤ 0` remap, or a force tagged COMPRESSION (T<0) yields a
strictly-capped `k_shear_eff > S_shear` remap (sign↔structure contradiction). **This branch has a
synthetic-input unit test that TRIGGERS it** (closes the #521/#526 dead-else gap: a fabricated
`(T>0, k_shear_eff<0)` pair must raise DISCREPANT-HALT, asserted by the test).

## FALSIFIER

If the from-scratch fixed-arc-length derivation gives the SAME sign for both loading paths (e.g. both
tensile, or both compressive), the channel-keyed hypothesis is FALSIFIED and the verdict is
[SAME-SIGN] — the #526 fork would collapse to a single global sign and Grant's "it does both
depending on interaction" would be wrong. Equally: if arm (a)'s pluck tension does NOT vanish as
y→0 (a finite force at zero pluck), the setup is wrong and must be found before any bin is booked
(this is a HALT-gated positive control, not a bin).

---

## POSITIVE CONTROLS (mandatory, HALT-gated — run BEFORE any adjudicated number)

- **PC-a1** arm (a) `T_a(y→0) → 0` (tension vanishes at zero pluck; guitar-string slack limit).
  Sympy + numeric.
- **PC-a2** arm (a) small-y limit matches the elementary fixed-ends string result derived
  independently (the `2k_a y²/ℓ` leading term), sympy series match.
- **PC-b1** arm (b) recovers Euler-strut phenomenology: finite compressive force `P_c=k_b·ℓ/4` as
  bow→0⁺ (the buckling-load analog in kernel units, stated).
- **PC-b2** arm (b) pre-buckling Hooke branch `k_a·u → 0` as u→0 (compressive).
- **PC-recon** the axial-arm magnitude equals `|Φ'(A)|` (the #526 `bond_tension`) to full precision on
  the SAME pipeline (bit-exact tie to the inherited machinery).
- **PC-dim** dimensional consistency of every force with the δ_y ledger row (`axiom-register.md:189`);
  sympy symbolic checks for EVERY derivative / chain-rule step.

Any PC failure HALTs before any bin is booked.

---

## TOLERANCES (disclosed)

- Symbolic checks: exact-zero (`sympy.simplify(...) == 0`).
- Same-pipeline full-precision references: PC-recon (arm-b vs #526 `bond_tension`) gated at 1×10⁻¹².
- Remap collapse consistency (VS4 inherited from #526): ≤8×10⁻¹⁶ (the #526 exact-collapse gate,
  re-run, not re-derived).
- Sign gate: exact sign comparison (no tolerance; a sign is discrete).
- All physics-magnitude numbers are BANDS over arc* ∈ [0.70, 0.96]; single-δ_y values are labeled
  δ_y=1 reference points, never headline.

## SCOPE BOUNDARY (stated per brief)

- This arc derives the **per-channel sign+magnitude of the per-bond axial load** ONLY. It does **NOT**
  do the cell-dilation relaxation (#526 test 2) — that test's INPUT is exactly this arc's per-channel
  sign output; stated as an explicit scope boundary in the result doc.
- Cauchy-only, fixed-geometry small-signal tensor readout (inherited #526 scope). Cosserat couple-
  stress bending carrier = Stage 2, not invoked.

## ANTI-TUNE LEDGER (inherited + this-arc rows)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel `Φ''=k0√(1−A²)` | CANON-FORCED | Ax4, `scale_invariant.py:107-156` (inherited #526) |
| 2 | Axial constitutive energy `Φ(A)` = ∫∫ kernel, `Φ(0)=Φ'(0)=0` | DERIVED | sympy this session |
| 3 | Arm (a) pluck tension `T_a=k_a ℓ(1−ℓ/√(ℓ²+4y²))` | DERIVED | sympy this session; PC-a1/a2 |
| 4 | Arm (b) end-load compression, plateau `P_c=k_b ℓ/4` | DERIVED | sympy this session; PC-b1 |
| 5 | δ_y (yield displacement) = 1 bond length | ENGINEERING/NORMALIZATION-CHOICE | inherited #526 ledger row 5; all magnitudes banded |
| 6 | ℓ = per-bond `|d|` = 1 on srs | READ-OFF (geometry) | `srs_primitive` (inherited) |
| 7 | k0=1 (units into ρ) | CANON-FORCED | `saturated_elastic_tensor.py:139` (inherited) |
| 8 | **Sign of T per channel** | **DERIVED THIS ARC** (was OPEN GRANT-FORK in #526) | fixed-arc-length loading-path derivation |
| 9 | **Magnitude LAW per channel** | **OPEN GRANT-FORK, resolved-by-banding** (orchestrator ruling cond. 1) | both laws banded per arm, four tracks |
| 10 | ρ*=9.7734, 2/7, ρ'_max, 1/√α, ½, ¼, arc* edges | GR-IMPORTED / READ-OFF / knife targets | never inputs; anti-tune guard |

**0 free parameters tuned toward any canon-distinguished value.**

---

## CROSS-REFERENCES (grep-verified at branch HEAD 8e21c72a this session)

- Remap machinery consumed: `src/scripts/vol_1_foundations/prestress_elastic_tensor.py`
  (`bond_tension`, `extract_prestress_Cij`, `_prestress_tensor_at`, `k_shear_eff`, `rho_prime`).
- #526 open fork: `research/2026-07-04_prestress-tensor_result.md:53-60,278-294,365-371`.
- Ax4 microfoundation + arc* band + A1-load/T2-response grammar: `manuscript/ave-kb/common/axiom-register.md:188-192`.
- V_yield = T2 self-trap wall (sign-keying corpus-grounding): `manuscript/ave-kb/common/vocabulary-register.md:664`.
- Kernel S(A) / differential stiffness: `src/ave/axioms/scale_invariant.py:107-156`.
- δ_y ledger discipline: `research/2026-07-04_prestress-tensor_result.md:392-407` (ledger table).
