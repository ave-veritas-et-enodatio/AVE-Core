# RESULT — [SIGN-RULE-DERIVED]: the two loading paths give OPPOSITE-sign end forces from the same fixed-arc constraint. The #526 sign fork resolves into a CHANNEL-KEYED rule.

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/bond-force-sign-rule`
**Driver:** `src/scripts/vol_1_foundations/bond_force_sign_rule.py`
**Output:** `src/scripts/vol_1_foundations/_output/bond_force_sign_rule.json` (driver-regenerable; gitignored)
**Test:** `src/tests/test_bond_force_sign_rule.py` (24 pass)
**Prereg (FROZEN):** `research/2026-07-04_bond-force-sign-rule_prereg_FROZEN.md` (committed BEFORE the driver)
**Resolves:** the OPEN SIGN FORK left by PR #526 (`research/2026-07-04_prestress-tensor_result.md:53-60,278-294,365-371`).

## VERDICT BOX

> **PRIMARY BIN: [SIGN-RULE-DERIVED].** The two loading paths give **opposite-sign** end-to-end
> per-bond axial forces from the SAME fixed-arc-length constraint `A²+S²=arc*²`, each canon-forced.
> The #526 sign fork resolves into a **channel-keyed rule** — exactly Grant's ratified "it does both
> depending on interaction":
>
> | Loading path | Sector | End force | #526 remap | ν trajectory |
> |---|---|---|---|---|
> | **transverse pluck** | T2 mechanical BOW response (the strut coordinate; NOT the charge winding — §4 homonym guard) | **TENSION (T>0)** | k_shear_eff GROWS ⟹ **CAPPED** | ν → K<0 pole region (cold ρ<2 band, via remap) |
> | **axial end-load** | A1 dilatation load, at the A1 op-point amplitude (gravitational per-bond mapping PENDING — §1) | **COMPRESSION (T<0)** | k_shear_eff SHRINKS ⟹ **UNCAPPED** | ν RISES toward +½ |
>
> **The rule:** pluck→tension→capped track; end-load→compression→uncapped track. Both tracks reported
> (four sub-tracks per the orchestrator ruling below); the sign is the verdict, the magnitude is a band.
>
> **DERIVED, not assumed.** Both arms are derived from scratch from the fixed-arc-length microfoundation
> (`axiom-register.md:189`), NOT the pair-potential analogy #526 used. Both positive controls pass
> (HALT-gated): arm (a) tension vanishes at zero pluck (guitar-string slack limit); arm (b) recovers
> Euler-strut phenomenology (finite compressive buckling load as bow→0⁺). 12 sympy residuals exactly 0.
>
> **CLASS: CONSISTENCY.** This resolves the SIGN of a #526 consistency-class object; no new value
> derivation, no emergence claim. 2/7, 9.7734, ρ'_max, 1/√α, ½, ¼, arc* edges stay GR-imported /
> read-off; none tuned toward (anti-tune ledger + frozen bins are the guard).

**All positive controls PASSED (HALT-gated), 24 tests pass.** PC-a1 arm(a) `T_a(0)=0` exact;
PC-a2 small-y matches elementary `2k_a y²/ℓ` (rel dev <1e-4 at y=1e-3); PC-b1 plateau `P_c=−k_b·ℓ/4`
finite compressive; PC-b2 pre-buckle Hooke `−k_a·u→0`; **PC-recon arm(b) magnitude == #526
`bond_tension` BIT-EXACT (max_abs_dev = 0.0)**; PC-dim 12 sympy residuals all exactly 0.

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** the K4/srs bond microfoundation (Ax4 quarter-arc kernel as a fixed-arc-length strut).
  Arm (a) = the T2 **mechanical BOW** transverse bias (the strut coordinate — NOT the Cosserat charge
  winding; §4 homonym guard). Arm (b) = **A1-delivered** axial bias
  (dilatational/gravitational end-load). **NOT cross-wired** (mass=A1 load; transverse bow=T2 response).
- **MODE:** quasi-static loading-path analysis on the bond microfoundation + small-signal tensor
  readout via the MERGED #526 remap. Symbolic (sympy) force derivation FIRST; numeric bands second.
- **REGIME:** quasi-static about a static DC bias. Op14 ON. **PHASE-STATE = saturated** (S<1). A→0 =
  the Maxwell/no-load positive-control anchor.
- **DC-vs-AC:** static DC bias; time-average factor 1 (inherited from #526, `node-up:118,:40,:145`).
- **COORDS (A46):** force derived in the bond's own arc-length coordinate (A_axial, S_bow); tensor
  readout in real-space Brillouin via the #526 pipeline. Each in its own coordinate — A46-clean.
- **CLASS:** CONSISTENCY. EMERGENCE FORBIDDEN for any value.

---

## ORCHESTRATOR RULING (2026-07-04, verbatim in prereg §"ORCHESTRATOR RULING") — Reading (b)

I surfaced the magnitude-law plumber question (the sign is channel-keyed and clean, but the two arms
have DIFFERENT magnitude laws). Orchestrator ruling: **READING (b), run both magnitude laws banded per
arm** — the bin verdict is sign-keyed (cap-vs-uncap depends on `sign(T)` alone), so the magnitude noun
is a bands question; Grant's standing preference is run-both-blind/engine-decides (documented ruling
pattern; Grant can override at review). Five conditions recorded in the prereg; all discharged below
(cond.1 magnitude-fork banded not baked; cond.2 four tracks reported separately; cond.3
corpus-grounding with verbatim quotes; cond.4 the ¼ knife-checked; cond.5 bins/controls/HALT/bands
unchanged).

---

## 1. THE DERIVED FORCE LAW PER ARM (symbolic + banded numbers)

Energy convention (stated per the δ_y ledger discipline): the kernel `Φ''(a)=k0·√(1−a²)`
(`scale_invariant.py:107-156`) is the AXIAL tangent stiffness; its double integral with `Φ(0)=Φ'(0)=0`
is the axial constitutive energy `Φ(A)`, `Φ''(0)=k0` (Maxwell recovered — sympy exact). This is #526's
`Φ'(A)` reading; the fixed-arc-length picture attaches the geometry that fixes the SIGN.

### ARM (a) — TRANSVERSE PLUCK (T2 mechanical BOW response — NOT the charge winding, §4 guard) → TENSION

Chord held at ℓ; transverse bow driven to y. To bow the strut the arc lengthens from ℓ to
`2√((ℓ/2)²+y²)` (tent geometry), stretching the material line → axial tension whose chord-directed
component pulls the clamped ends together:

> **T_a(y) = k_a·ℓ·(1 − ℓ/√(ℓ²+4y²))** , leading order **T_a ≈ (2k_a/ℓ)·y²** . **SIGN = +TENSION.**

- `T_a(0) = 0` **exactly** (POSITIVE CONTROL PC-a1, guitar-string slack limit — no force at zero bow).
  *This is the setup-correctness check the prereg demanded: a finite force at A=0 would mean the setup
  is wrong; it is not — the tension vanishes quadratically.*
- **Second-order geometric law** (halving y quarters T_a — test-locked). This is WEAKER than #526's
  first-order `Φ'(A)`; the difference is why Reading (b) bands both laws.
- Cross-derived independently from the energy `U=½k_a(arc−ℓ)²+½k_b y²` (sympy `arm_a_from_energy=0`).

### ARM (b) — AXIAL END-LOAD (A1 dilatation/gravity load) → COMPRESSION

Chord driven below ℓ; bow free to equilibrate on the fixed-arc constraint → the strut BUCKLES and
resists compression:

> **F_b(A) = −|Φ'(A)| = −bond_tension(A)** . **SIGN = −COMPRESSION.** Post-buckling plateau
> **P_c = −k_b·ℓ/4** (buckling-load analog, FINITE as bow→0⁺). Pre-buckle branch: Hooke **−k_a·u→0**.

- **The magnitude is the SAME LAW as #526** (`|Φ'(A)|`); the SIGN is the ONLY difference. #526 used
  `+|Φ'(A)|` (tensile); the fixed-arc end-load derivation gives the same magnitude, compressive. This
  is the load-bearing reconciliation: **#526 already IS the axial arm — with the wrong sign for an
  end-load.** PC-recon gates the magnitude tie bit-exact (max_abs_dev = 0.0).
- **POSITIVE CONTROL PC-b1** (Euler phenomenology): finite compressive force as bow→0⁺, plateau
  `k_b·ℓ/4 = 0.25` in kernel units (k_b=ℓ=1). PC-b2: `−k_a·u→0` as u→0.

### The reconciliation

The two arms give **opposite-sign** end forces. Arm (b) shares #526's first-order magnitude law with a
flipped sign; arm (a) has a weaker second-order geometric law. The cap-vs-uncap remap structure depends
on **`sign(T)` ALONE**, so [SIGN-RULE-DERIVED] survives either magnitude reading — the magnitude is a
band, the sign is the verdict.

---

## 2. THE FOUR TRACKS (condition 2 — reported SEPARATELY, not just the envelope)

Through the MERGED #526 remap (`extract_prestress_Cij` + `k_shear_eff = S_shear + T/ℓ` +
`ρ' = S_ax/k_shear_eff`, consumed verbatim). Operating point: the #518 SHEAR-LOADS crossing
(A_axial=√α for the A1 end-load; A_shear=0.99479 sets k_shear at the crossing). **IN-REGIME (item 2,
orchestrator review 2026-07-04)** and **banded over arc* ∈ [0.70 elastica, 0.96 tent]**
(`axiom-register.md:189`).

> **REGIME BOUND (item 2 — disclosed).** Arm (a) is plucked at the **in-regime bow ceiling**
> `y = in_regime_pluck_bow(arc*)` — the fixed-arc premise's OWN maximum transverse displacement (the
> admissible pluck-arc excess equals the arc* deficit |1−arc*/ℓ|): `y ≈ 0.14` (tent) to `0.42`
> (elastica). This **REPLACES** the first draft's out-of-regime `y = 0.99479`, whose pluck-arc was
> `2.23 ℓ` — 2.3× beyond the arc*≤0.96 premise (undisclosed in the first draft). The band is over arc*
> itself (the displacement premise), applied **inside the geometry**, NOT δ_y multiplying the force.
> **The first draft's arm-(a) numbers (ρ'∈[1.17, 2.04]) are SUPERSEDED as out-of-regime.**

| Track (arm × law) | Sign | T (arc* 0.70→0.96) | k_shear_eff | ρ' (in-regime band) | ν | K | remap |
|---|---|---|---|---|---|---|---|
| **arm_a_geometric** | tension(+) | +0.231 → +0.038 | +0.33 → +0.14 | **2.99 → 7.10** | −0.32 → +0.20 | +0.020 → +0.042 | CAPPED |
| **arm_a_phi_prime** | tension(+) | +0.403 → +0.142 | +0.51 → +0.24 | **1.97 → 4.08** | −1.04 → −0.056 | −0.001 → +0.030 | CAPPED |
| **arm_b_phi_prime** | compression(−) | −0.062 → −0.085 | +0.040 → +0.017 | 25.1 → 59.9 | +0.418 → +0.466 | +0.054 → +0.057 | UNCAPPED |
| **arm_b_geometric** | compression(−) | −0.010 → −0.014 | +0.092 → +0.088 | 10.9 → 11.4 | +0.308 → +0.317 | +0.048 → +0.048 | UNCAPPED |

(At the tent edge arc*=0.96 the arm_b_phi_prime track = #526's T<0 arm verbatim: T=−0.08532, ρ'=59.93,
ν=+0.466 — `prestress-tensor_result.md:288`; test-locked.)

**Reading the tracks (Grant rules the noun at review):**
- **The SIGN split is law-invariant AND band-edge-invariant:** both arm-(a) laws are tension→capped at
  both edges; both arm-(b) laws are compression→uncapped. The verdict does not depend on the magnitude
  noun or the arc* edge. (`main()` adjudicates the bin at BOTH edges and requires agreement.)
- **The magnitude noun changes only HOW FAR (in-regime):** arm-(a) ρ' spans [1.97, 7.10] across
  {laws × band}; arm-(b) ρ' spans [10.9, 59.9]. The envelope is {arm a capped, arm b uncapped} — a
  summary view, NOT the finding. The four tracks are the finding.
- **Arm (a)'s ν<0 is the PRE-EXISTING cold K<0 band, not new instability** (matches #526 §6): cold ν at
  ρ=1.97 tracks the pre-stressed value; `min_acoustic_eig>0` everywhere (all four tracks), so ν<0 is
  the Poisson pole, NOT a lost sound mode ([DESTABILIZED] NOT triggered). **The K sign-flips inside the
  arm-(a) band** (K<0 at ρ'≈1.97 → K>0 at ρ'≈7.10) — knifed in §3 (item 3).

---

## 3. THE KNIFE (condition 4) — the plateau ¼ is tent geometry, KNIFE=noise

The visible knife targets (2/7, 9.7734, ρ'_max≈11.68, 1/√α, ½, **¼**, arc* edges) were armed. The one
arm-derived new value is the buckling plateau `P_c = −k_b·ℓ/4`. Knife-check of the ¼:

> The ¼ = (½ bend-energy prefactor) × (½ tent half-chord chain), a **MECHANICAL tent-geometry factor**
> (sympy `quarter_factor_trace = 0`). A pinned-pinned Euler elastica gives **π²** instead — the ¼ is
> tent-model-specific, model-dependent (arc* band discipline applies). It is a **FORCE in kernel
> units** (`k_b·ℓ`), dimensionally distinct from a charge-fraction ¼. A different bend stiffness gives
> a different plateau (`P_c(k_b=2)=−0.5`, test-locked), so the ¼ is not universal. **KNIFE=noise** —
> `lands_on_canon_distinguished_value = False`. Reported here under coincidence discipline, not in
> passing.

The inherited near-misses (ρ'_max≈1/√α to 0.24% = trivial small-A expansion; 9.7734/cap≈5/6) are
#526's, restated as noise (`prestress-tensor_result.md:66-69`); no new coincidence.

---

## 4. CORPUS-GROUNDING (condition 3) — the fork resolution was ALREADY in canon's grammar

That the channel-keyed sign rule is not a new posit but a re-reading of existing canonical grammar is
itself a reportable finding. Verbatim grep quotes (this session, at branch HEAD):

- **`axiom-register.md:189`** — the kernel IS a load-response bifurcation with the exact channel split:
  > "the kernel is a **load-response bifurcation** (axial A1 dilatation load → transverse T2 bow
  > response; $A^2+S^2=arc^{*2}$ is a *single fixed-length constraint*…)"

  This is the two arms in canon's own words: **A1 axial = the LOAD (arm b, end-load, compression); T2
  transverse bow = the RESPONSE (arm a, pluck, tension).** The sign-keying follows from which coordinate
  is the load and which is the response.

**Arm (a) is grounded on the axiom-register BOW ONLY.** The "transverse T2 bow response" in the line
above is the **mechanical bow COORDINATE** of the strut (the geometric transverse displacement in
`A²+S²=arc*²`). That is the whole grounding arm (a) needs and claims.

> **T2 HOMONYM GUARD (MAJOR fix, orchestrator review 2026-07-04).** The label "T2" names TWO
> categorically distinct canon objects, and this doc's first draft welded them. They must NOT be
> conflated:
> - **(i) the mechanical T2 BOW coordinate** — the strut's transverse displacement (axiom-register:189).
>   This is arm (a)'s legitimate geometric grounding.
> - **(ii) the Cosserat T2 MICRO-ROTATION charge winding** — `vocabulary-register.md:664`'s "transverse
>   Cosserat (T2) self-trap wall" is THIS object. Canon pins it as a **DISTINCT object**: a "static
>   reactive CHARGE BOUNDARY, a lossless-REACTIVE constraint **carrying no real power**," **STATIC
>   topology, not a dynamical/energetic mode** (both internal dynamical loci tested NEGATIVE, #415 +
>   #417) — `resonant-lc-solitons.md:95` ("a **DISTINCT object**… $A1 \perp T2$ per
>   master-equation.md:20 … Grant-ratified 2026-06-14"), `:128` ("static reactive CHARGE BOUNDARY …
>   lossless-REACTIVE … carrying no real power … STATIC topology, not a dynamical/energetic mode … both
>   internal dynamical loci … NEGATIVE (#415 + #417)"). **A mechanical midpoint pluck is NOT the charge
>   winding.**
>
> Therefore: the earlier "the two arms map onto the two canonical sectors 1:1" sentence is **WITHDRAWN**.
> Arm (a) is the **mechanical bow response** (object i), NOT the charge sector (object ii). The
> `vocabulary-register.md:664` cite is downgraded from grounding to this homonym guard: it shares the
> "T2" label but names a distinct object; do not cross-wire. The A1⊥T2 master-equation anchor forbids
> exactly the conflation the first draft made.

**Finding (corrected):** the fork's resolution is latent in the axiom-register's "A1 load → T2 *bow*
response" phrasing — read strictly as the mechanical load/response split (which coordinate is clamped
vs driven), NOT as the A1-mass / T2-charge sector map. Grant's ratified "it does both depending on
interaction" is that mechanical phrasing read as a force-sign rule.

> **OPEN QUESTION SURFACED (flagged for Grant, NOT resolved — item 1c).** If the electron's self-trap
> wall is the **STATIC T2 winding** (object ii, "carrying no real power," #415+#417 negative), then
> **what physically PLUCKS the bond in matter** to deliver arm (a)'s transverse mechanical bias? The
> mechanical bow (object i) needs a dynamical driver, but the charge winding (object ii) is static and
> does no work. Candidate distinction (Grant's fork to rule, recorded not resolved): the **dynamical
> standing shear wave** (a pre-trap / dynamic transverse excitation that CAN do work and pluck the
> bond) vs the **static winding** (the post-trap topological object). Whether arm (a)'s pluck is
> delivered by the dynamical shear wave — and how that relates to the static winding it may leave
> behind — is a substrate-ontology question I do not adjudicate. Surfaced for Grant.

---

## 5. HONEST CLOSURE (Rule 11) — the fork resolves; one mechanism, both tracks

The prereg predicted [SIGN-RULE-DERIVED] as most-likely; the from-scratch fixed-arc-length derivation
confirms it decisively. **One mechanism** — the loading path selecting which coordinate is clamped vs
driven — gives both arms their opposite signs, and the #526 remap's cap-vs-uncap structure follows from
`sign(T)` alone. This is the discipline working: the #526 fork does NOT collapse to a single global
sign ([SAME-SIGN] falsified — both bins reachability-tested); it resolves into the channel-keyed rule
Grant ratified. No rescue, no post-hoc bin edit.

**Substitution-not-retraction (Rule 12):** this does NOT refill any slot with an unverified hypothesis.
It resolves the SIGN axis #526 left explicitly open (`prestress-tensor_result.md:403` ledger row 8
"Sign of T … OPEN GRANT-FORK"). The magnitude LAW remains an OPEN GRANT-FORK resolved-by-banding
(this arc's ledger row 9) — Grant rules the noun at review with the four tracks in hand.

---

## 6. SCOPE BOUNDARY (stated per brief)

- This arc derives the **per-channel sign+magnitude of the per-bond axial load ONLY.** It does **NOT**
  do the cell-dilation relaxation (#526 test 2). **This arc's per-channel sign output is test 2's
  INPUT** — the #526 cell virial under uniform tension (2.05, `prestress-tensor_result.md:298`) is an
  A1-owned dilation whose SIGN this arc now supplies (compression for the A1 end-load). Test 2 remains
  OPEN and downstream.
- Cauchy-only, fixed-geometry small-signal readout (inherited #526 scope). Cosserat couple-stress
  bending carrier = Stage 2, not invoked.

---

## 7. BINS — verdict (frozen bins; no fall-through else; DISCREPANT-HALT reachable + unit-tested)

| Bin | Status | Basis |
|---|---|---|
| **[SIGN-RULE-DERIVED]** | **PRIMARY (earned)** | opposite-sign arms, each canon-forced; channel-keyed rule; both tracks reported |
| [SAME-SIGN] | NOT triggered (reachability-tested) | would need both arms same sign; falsified by the derivation |
| [PATH-INDETERMINATE] | NOT triggered (reachability-tested) | would need an undefined/non-sign-robust force; both arms sign-robust across laws |

- **NO fall-through else + reachable DISCREPANT-HALT (closes the #521/#526 dead-else gap PROPERLY this
  time):** the selector raises `DiscrepantHalt` if a force's sign contradicts its remap structure
  (tension that uncaps, or compression that caps). **TWO synthetic-input tests TRIGGER it**
  (`test_discrepant_halt_fires_on_tension_that_uncaps`, `…compression_that_caps`) + one no-false-fire
  test on the live tracks. Both non-primary bins also have reachability tests.
- Sector classification (v1.5): the decision observable is **DC-internal** (a DC medium-state sign; the
  tensor readout is a same-pipeline DC consistency check). No pure-AC null; no framework-level-negative
  claimed (CONSISTENCY-class sign adjudication).

---

## 8. FLAG-DON'T-FIX — surfaced, not resolved

1. **STALE DOCSTRING in the CONSUMED #526 driver** (`prestress_elastic_tensor.py:127-128`,
   `_prestress_phi_of_k`): the docstring still carries the RETRACTED first framing —
   > "The pre-stress term is ADDITIVE to the transverse block; it is NOT an overall scale, so it can
   > break the #521 degree-1 homogeneity."

   This was **retracted by #526 §2** (`prestress-tensor_result.md:147-159`: "That is FALSE
   (verifier-proved bit-exact) and is retracted" — VS4 proved the tensor NEVER leaves the cold family).
   The CODE is correct; only the docstring comment is stale. Per flag-don't-fix I do NOT edit another
   arc's committed file. **Surfaced for the auditor/#526-owner** to reconcile the docstring to §2's
   corrected mechanism. It is not load-bearing for this arc's arithmetic (I consume the function's
   behavior, not its comment).

2. **THE MAGNITUDE-LAW NOUN (OPEN GRANT-FORK, resolved-by-banding this arc).** Arm (a): 2nd-order
   geometric vs #526 `|Φ'(A)|`. Arm (b): `|Φ'(A)|` vs 2nd-order geometric. The sign (hence the verdict)
   is law-invariant; the magnitude band is not. Four tracks reported separately (§2) for Grant's noun
   ruling at review. Surfaced, NOT unilaterally resolved.

---

## 9. FALLOUT / AUDITOR-QUEUE (surfaced; implementer does NOT land manuals)

| Site | Proposed disposition |
|---|---|
| **#526 ledger row 8** (`prestress-tensor_result.md:403`: "Sign of T … OPEN GRANT-FORK") | **RESOLVE-THE-FORK (candidate):** the sign is now DERIVED and channel-keyed — pluck→T>0→capped, end-load→T<0→uncapped. #526's assumed T>0 (stretched-pair) is the PLUCK arm; the AXIAL bias #526 physically modeled (A1/gravity) is the END-LOAD arm ⟹ **T<0 compression** for the gravitational bias. Provenance `bond-force-sign-rule_result.md`. |
| **#526 §6.5 SIGN FORK table** (`prestress-tensor_result.md:285-288`) | **REFINE (candidate):** the "T<0 compressive buckling strut (canon)" row is now the DERIVED arm-(b) reading for the A1 end-load; the T>0 row is the arm-(a) pluck reading for the T2 transverse bias. Both are real, channel-keyed — not a single un-adjudicated fork. |
| **#526 driver docstring** (`prestress_elastic_tensor.py:127-128`) | **STALE-DOCSTRING (flag §8.1):** reconcile the `_prestress_phi_of_k` docstring to §2's corrected (VS4) mechanism. Code correct; comment stale. |
| **axiom-register.md:189** "A1 dilatation load → T2 bow response" | **CROSS-LINK (candidate):** this arc shows that phrasing IS the force-sign rule (A1 load→compression, T2 response→tension). No rewrite; a cross-link that the sign-keying follows from the load/response split. |
| **The K=2G GR-import grade** (PR#261) | **UNTOUCHED:** this arc adds no value derivation; it adjudicates a SIGN. 9.7734/2/7/K=2G stay GR-imported. |

**No rewrites performed.** Resolve / refine / cross-link / flag ROWS only; the auditor lane lands the
manual entries.

---

## Cross-references (grep-verified at branch HEAD this session)

- Driver: `src/scripts/vol_1_foundations/bond_force_sign_rule.py`
- Test: `src/tests/test_bond_force_sign_rule.py` (24 pass)
- Prereg (FROZEN): `research/2026-07-04_bond-force-sign-rule_prereg_FROZEN.md`
- Consumed #526 remap: `src/scripts/vol_1_foundations/prestress_elastic_tensor.py` (`bond_tension`,
  `extract_prestress_Cij`, `k_shear_eff`/`rho_prime` remap)
- #526 result + open sign fork: `research/2026-07-04_prestress-tensor_result.md:53-60,278-294,365-371,403`
- Ax4 microfoundation (fixed-arc-length, A1-load/T2-response grammar): `manuscript/ave-kb/common/axiom-register.md:188-192`
- T2 HOMONYM GUARD (mechanical bow vs charge winding — the two distinct T2 objects): `resonant-lc-solitons.md:95,:128` (A1⊥T2 per `master-equation.md:20`, Grant-ratified 2026-06-14; #415+#417 NEGATIVE); `vocabulary-register.md:664` (the charge-winding object, downgraded to homonym guard)
- Kernel S(A) / differential stiffness: `src/ave/axioms/scale_invariant.py:107-156`
