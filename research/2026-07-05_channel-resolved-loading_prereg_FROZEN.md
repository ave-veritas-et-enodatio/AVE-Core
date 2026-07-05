# PREREG (FROZEN) — Channel-resolved loading: does ρ' preserve for the traveling wave and move for the confined mode?

> ## 🔴 ERRATA (2026-07-05, post-run, orchestrator review of PR #531 — Rule-12 banners; frozen body preserved)
> 1. **Numeric (item 5b):** `:134` states `S(√α) ≈ 0.99617` — WRONG. Correct: **S(√α) = 0.996345**
>    (`saturation_factor(√α, 1.0) = 0.9963446428975768`). The result doc uses the correct value.
> 2. **Verdict re-frame (item 1):** this prereg's bins assumed the #526 T-slot accepts the hum's AC
>    cycle-averaged ⟨T⟩. The review found the #526 FROZEN prereg scopes the slot to a STATIC DC bias
>    (`2026-07-04_prestress-tensor_prereg_FROZEN.md`:64-78). The verdict is therefore a T-SLOT SCOPE
>    FORK: **ARM DC_ONLY (canon keying) → [SYMMETRIC-BOTH]**, **ARM EXTENDED (this-arc re-keying) →
>    [ASYMMETRIC-BOTH]** — Grant's to resolve. The frozen bins map: DC_ONLY realizes [SYMMETRIC-BOTH]
>    (both preserve the ρ' HUM-move); EXTENDED realizes [ASYMMETRIC-BOTH]. No bin is orphaned; the
>    [CHANNEL-DISCRIMINATOR-DERIVED] bin is reached on neither arm (the hum is not a discriminator).
> 3. **Grade (item 5c):** `:134` and the ledger grade the numerator hum-independence as fully DERIVED;
>    the sympy covers the axial-oscillation term (4th-order) only — the FULL numerator invariance also
>    rests on Grant's no-double-count RULING. Graded honestly in the result as sympy + ruling.
> See `research/2026-07-05_channel-resolved-loading_result.md` for the full re-framed verdict.

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/channel-discriminator`
**Freeze order:** this doc is committed BEFORE the driver (`channel_resolved_loading.py`); commit
order is the freeze proof. Bins below are VERBATIM-FROZEN; no post-data edits (Rule 11) — the ERRATA
banner above is Rule-12 (post-run correction of a numeric typo + verdict re-frame; the frozen body
below is UNEDITED).

**Successor to:** the merged NEGATIVE PR #529 (`research/2026-07-04_resonant-tension-law_result.md`,
[RADIATION-CONTAMINATED]) — the scalar ⟨y²⟩-tension carrier died because a matched CW traveling wave
carries the SAME per-bond scalar ⟨T⟩ = (k_a/ℓ)y₀² as the confined hum. Scalar tension cannot
distinguish matter from radiation. #529's own die-note names the successor: *"The magnitude
discriminator, if any, is CHANNEL-RESOLVED … that is a NEW prereg for a future arc."* This is that arc.

---

## TARGET (Step 1)

Per bond, decompose the time-averaged bias effect of a transverse wave into the AXIAL channel
(numerator of ρ': S_axial and any axial-spring renormalization) and the SHEAR-adjacent slot
(denominator of ρ': k_s·S_shear + T/ℓ), for **(i)** a matched CW TRAVELING transverse wave and
**(ii)** a CONFINED standing mode between Γ=−1 terminations, and adjudicate whether the RATIO
ρ' = S_axial / (S_shear + T/ℓ) is preserved for (i) and moved for (ii).

The remap ρ' is the observable the /7-mechanism candidate CONSUMES (`prestress_elastic_tensor.py`
`_prestress_tensor_at`: `k_shear_eff = S_shear + T/ℓ`, `rho_prime = S_axial / k_shear_eff`). Per the
#529 CRITICAL lesson, every "preserved/moved" claim is gated on ρ' ITSELF (the consumed observable),
not a proxy (not the scalar T, not a gradient, not a reflection coefficient).

---

## PHYSICAL PICTURE (Step 1.5)

- **What saturates / where:** each srs bond is a rank-2 spring `Φ_b = k_a·S_axial·P + (k_s·S_shear +
  T/ℓ)·(I−P)` where `P = d̂⊗d̂` (axial projector). BOTH k_a and k_s are translational-u /
  **capacitive** springs of the SAME bond (PR #516) — NOT the ε/μ photon pair. S(A)=√(1−(A/A_y)²) is
  the Ax4 kernel; A is the DEFORMATION-toward-snap of that channel (Grant 2026-07-05, below).
- **Which Γ=−1 boundary:** the confined mode (ii) is the electron's own Γ=−1 TIR wall
  (`resonant-lc-solitons.md`:47); the traveling wave (i) is on an Ax3-matched line (Γ_internal=0 at
  ρ_bond=1, `clm-mfb2ax`) — no wall.
- **Soliton population/topology:** the confined mode is the electron unknot's transverse bond hum
  riding on the A1 mass-core DC operating point A_dc=√α (def-vyvsn1); the traveling wave carries no
  soliton, no DC bias (⟨A⟩=0 pure AC).
- **What scales how:** the geometric chord tension T = (k_a/ℓ)y₀² is 2nd-order in bow amplitude and
  survives ⟨A⟩=0 (it is quadratic-geometric, NOT ⟨A⟩-keyed). The shear-channel saturation shift is
  also 2nd-order (⟨A²⟩ keying). The axial-channel deformation is 4th-order (chord wobble) → S_axial
  Q-point unmoved at 2nd order.
- **Discrete onset vs smooth curve:** there is no knee — this is a smooth 2nd-order-in-y₀
  perturbation of ρ' off its cold value. The discriminator, if it exists, is the SIGN/EXISTENCE of a
  DIFFERENCE between how (i) and (ii) move ρ', not a threshold event.

---

## GRANT'S RULING — the Q-point framing (VERBATIM, attributed Grant 2026-07-05)

> READING A — the saturation operating point is the QUIESCENT DEFORMATION STATE RELATIVE TO REST.
> The keying variable of S(A) is the deformation ratio (A = V/V_snap ↔ bond deformation toward snap),
> NOT stress. Consequences:
>
> 1. The axial channel of a bond under a ⟨A⟩=0 purely-transverse wave: its DEFORMATION is 4th-order
>    in y₀ (the chord wobble), so its Q-point does not move at 2nd order — the numerator S_axial is
>    untouched. The axial STRESS (tension) is real but enters ONLY as the geometric (T/ℓ)(I−P) term —
>    exactly the merged #526 form Φ''(deformation)·P + (T/ℓ)(I−P), which already separates
>    constitutive-stiffness-at-the-Q-point from the stress term. Keying S on stress would
>    double-count into both terms and corrupt the PC2-validated form — state this no-double-count
>    principle explicitly.
> 2. The transverse/shear channel DOES have 2nd-order RMS deformation under both wave types — its S
>    shifts per the ⟨A²⟩ keying (node-up:144 δn≈+¼A²). So the traveling-wave denominator carries TWO
>    competing 2nd-order terms: the saturation shift of k_shear·S (softening) AND the geometric +T/ℓ
>    (stiffening). Whether they cancel in ρ' — and whether any cancellation is a THEOREM (e.g., keyed
>    to the Ax3 matched point k_a=k_s) or an unexplained numerical accident — is the arc's central
>    derivation. Do NOT steer toward the cancellation; derive what is.
> 3. The confined standing mode gets the same treatment: per-channel deformation Q-points + stress
>    terms, at the electron's asymmetric operating state. The discriminator, if it exists, must fall
>    out of the SAME bookkeeping applied to both.

**Binding consequences carried into this prereg:**
- **NO-DOUBLE-COUNT (load-bearing):** the axial tension T is a STRESS. It enters ρ' ONLY through the
  denominator `+T/ℓ` term (the #526 pre-stress transverse block). It must NOT also be fed into
  S_axial (the numerator) or into S_shear. S-factors are keyed on DEFORMATION-toward-snap; T is a
  stress and lives only in the (I−P) stress term. Feeding T into an S-factor corrupts the
  PC2-validated `_prestress_phi_of_k` form.
- **Numerator S_axial is UNTOUCHED by a ⟨A⟩=0 transverse wave** (axial deformation 4th-order). For
  the CONFINED mode the numerator IS shifted — by the electron's axial DC operating point A_dc=√α (a
  real DC deformation), NOT by the hum.
- **Denominator carries the two competing 2nd-order terms** (soft: k_s·S_shear shift; stiff: +T/ℓ).

---

## HOST MODEL (Requirement 1) — and what it cannot see

**Choice: the merged srs-tensor remap machinery, orientation-resolved, imported verbatim** — NOT a
new 2-DOF chain. Justification:
- A scalar 1D ladder cannot host a channel decomposition (the #529 host — that is WHY #529 could only
  see the scalar T). The srs bond tensor `Φ_b = k_a·P + (k_s + T/ℓ)·(I−P)` (P=d̂⊗d̂) natively carries
  the axial (P) vs shear (I−P) channel split per bond. The remap `_prestress_tensor_at` /
  `_remap_at_signed_T` already consumes S_axial (numerator) and S_shear + T/ℓ (denominator) as
  SEPARATE per-channel inputs. This is the minimal host that can host the decomposition, and it is
  already merged + PC2-validated — importing it (not reimplementing) respects the concurrency-safe
  import discipline and avoids a fresh un-validated host.
- The transverse-wave kinematics feed this host via the per-channel time-averaged loading derived
  below (the axial S, the shear S, the geometric T), all at consistent 2nd order in y₀.

**SCOPE CAVEAT (up front — the #529 review dinged the missing ladder-scope caveat):**
- **(a) The srs bond tensor is a LINEAR rank-2 spring pair per bond.** It carries the axial/shear
  channel split, but it does NOT carry a full nonlinear elastica or any inter-bond coupling of the
  transverse mode beyond the affine Born-Huang tensor. The 2nd-order loading terms are derived
  analytically (sympy) and FED to the tensor; the tensor is not itself solving a transverse wave
  equation. What this CANNOT see: any channel-mixing that appears only at 3rd+ order, any
  bond-to-bond phase structure of the transverse mode that is not captured by the per-bond ⟨A²⟩ and
  ⟨T⟩ (the per-bond scalars). The verdict is drawn at the per-bond 2nd-order level.
- **(b) The y₀↔A_shear dictionary (how a transverse mechanical bow y₀ maps to the shear-channel
  saturation deformation A_shear) is NOT pinned by canon for a purely-transverse mechanical bow.**
  Two readings (below) bracket it; the driver runs BOTH (KEEP-BOTH) and the verdict is reported per
  reading. What this CANNOT see: the physically-correct dictionary, if it is neither bracket.
- **(c) Homonym guard (#527, binding):** the transverse bow is a MECHANICAL T2-response bend of the
  bond (arm-(a) geometry), NOT the Cosserat (2,3) charge winding. "Transverse/shear channel" here =
  the mechanical (I−P) block of the translational-u spring, NOT the μ-inductive photon channel and
  NOT the charge-winding. The two "3"s stay orthogonal (mass=A1, charge=Cosserat-winding).

---

## THE PER-CHANNEL TIME-AVERAGED LOADING (Requirement 2 — all terms at consistent 2nd order, sympy-verified)

Let y₀ = transverse bow amplitude at midspan (ℓ_node units), ℓ = bond length (=1 on srs), A_y = 1
(canonical yield, def-vyvsn1). Every term below is sympy-verified in the driver's `symbolic_backbone`
with exact-zero residuals; no term is dropped without an order-proof.

### (N) AXIAL channel — the numerator S_axial
- **Traveling wave (⟨A⟩=0):** axial deformation is the chord-shortening wobble, 4th-order in y₀
  (Δℓ/ℓ ~ y₀²/2 is a STATIC 2nd-order shortening → its STRESS is T, the denominator term; the
  DEFORMATION *oscillation* about that shifted rest length that would move the S-factor Q-point is
  4th-order). Per Grant consequence 1 + no-double-count: **S_axial = S_axial(A_dc)**, y₀-independent
  at 2nd order. For radiation A_dc=0 → **S_axial = 1** (cold).
- **Confined mode:** the electron's axial core sits at DC deformation **A_dc = √α** (def-vyvsn1,
  α-echo) → **S_axial = S(√α) ≈ 0.99617**, y₀-independent. THE HUM DOES NOT MOVE THE NUMERATOR; the
  DC bias does. This is the asymmetry Grant consequence 3 names.

### (D) SHEAR-adjacent slot — the denominator k_s·S_shear + T/ℓ
Two competing 2nd-order terms:
- **(D-soft) saturation shift of the shear spring:** the transverse bow is a shear deformation of the
  bond. Its RMS ⟨A_shear²⟩ shifts S_shear per the ⟨A²⟩ keying (node-up:144). At 2nd order
  S_shear ≈ 1 − ⟨A_shear²⟩/2. **Direction: SOFTENING** (S_shear < 1). SAME for both wave types (both
  have ⟨y²⟩ = y₀²/2 per bond). The magnitude depends on the y₀↔A_shear dictionary (scope caveat b):
  - **Reading D1 (bond-angle):** A_shear = y₀/ℓ (transverse angle) → ⟨A_shear²⟩ = (y₀/ℓ)²/2 →
    soft term = −k_s·(y₀/ℓ)²/4.
  - **Reading D2 (displacement-direct):** A_shear = y₀ (displacement in yield units, matching the
    node-up A=V/V_snap convention where the transverse displacement IS the deformation) →
    ⟨A_shear²⟩ = y₀²/2 → soft term = −k_s·y₀²/4. On srs ℓ=1 the two readings COINCIDE; they diverge
    only if ℓ≠1 — reported as a dictionary flag, not a knife (KEEP-BOTH).
- **(D-stiff) geometric chord tension (the #529 Part-1 law, IMPORTED):** T = (k_a/ℓ)y₀²,
  ⟨sin²⟩=½ already folded in. **Direction: STIFFENING** (+T/ℓ = +k_a·y₀²/ℓ² > 0). SAME for both wave
  types (#529: scalar T identical). This is the term that killed the scalar carrier.

### The competition (the central derivation — sympy, PRE-freeze, reported HONESTLY)
At the Ax3 matched point k_a = k_s = k₀, cold S_shear reference, A_y=1, ℓ=1:
```
dD/k₀ = (D-soft) + (D-stiff) = −y₀²/(4A_y²) + y₀²  = +¾ y₀²   (at A_y=1)
```
**The denominator does NOT cancel at the canonical yield A_y=1.** Cancellation (dD=0) requires
**A_y = 1/2** (soft = −stiff ⟺ 1/(4A_y²)=1). A_y=1/2 is NOT the canonical yield — so there is NO
theorem-cancellation at the physical operating point. The geometric stiffening dominates the
saturation softening 4:1. **PRE-FREEZE EXPECTATION: the traveling wave MOVES ρ'** (ρ'_travel ≈
1 − ¾y₀² < 1), it is NOT ratio-preserving under the #526 remap. This is stated up front so the
result cannot be steered.

**Dimensional/anchor pre-check (Step 3.5):** all three terms are O(y₀²) dimensionless (y₀ in ℓ_node
units, ℓ=1); at the in-regime tent-edge bow y₀≈0.14 (#527), dD/k₀ ≈ ¾·0.02 ≈ 0.015 → ρ'_travel ≈
0.985, a ~1.5% move — small but nonzero, above the ~1e-9 reconcile floor. At the elastica edge
y₀≈0.42, dD/k₀ ≈ 0.13 → ρ'_travel ≈ 0.88 (matches #529's radiation-stiffening 9.77→0.90 order).

---

## THE PUMP-NULL CONSTRAINT (Requirement 3 — canon consistency BEFORE going channel-resolved)

Per canon (#518 §7 / matter-stiffening §4 + `clm-clvchn`): pure-AC has ⟨A⟩=0 so the SATURATION
factors carry no DC bias for radiation. My framework must respect this:
- **The S-factors' DC operating point does NOT shift for a ⟨A⟩=0 wave** (no rectification; the pump
  Chern C=0). CORRECT in my bookkeeping: S_axial=1 (cold) for radiation; S_shear's shift is 2nd-order
  ⟨A²⟩ (the small-signal δn, node-up:144), NOT a DC-bias operating-point move. The DC Q-point is
  unmoved; only the small-signal average stiffness shifts at 2nd order.
- **Consistency gate BEFORE channel-resolved (mandatory):** the framework MUST reproduce #529's
  finding — the scalar per-bond ⟨T⟩ is UNIFORM (= (k_a/ℓ)y₀²) and IDENTICAL for both wave types. This
  is a hard reconcile-gate against the imported `field_from_abcd_propagation` (the Γ-free #529 path):
  my per-bond ⟨T⟩ must equal #529's to reconcile tolerance. If it does not, the driver HALTs (I have
  a bookkeeping error, not a result).

**The crux tension I SURFACE, do not resolve (flag-don't-fix):** canon's radiation null
(matter-stiffening §4) was derived at the PRE-#526 level `ρ_eff = S_axial/S_shear` — WITHOUT the
geometric T/ℓ denominator term (that term arrived at #526). Canon's null: radiation drives both
grades with the same ⟨A²⟩ → S_axial=S_shear → ratio unchanged. But that null OMITS the +T/ℓ term,
which is geometric-2nd-order and DOES survive ⟨A⟩=0. Under the FULL #526 remap ρ'=S_axial/(S_shear+
T/ℓ), my derivation says the traveling wave's denominator picks up +¾y₀² that does NOT cancel. **This
is a potential CONFLICT between the #526 T-slot remap and canon's #518/§7 radiation null.** Whether it
is a real conflict or a scope artifact (canon's null is at the ρ_eff-ratio level, the #526 T-slot is
the corrected coordinate) is a bin outcome, NOT something I resolve here — see [ASYMMETRIC-BOTH] /
[UNDERDETERMINED].

---

## FROZEN BINS (verbatim; no post-data edits; no fall-through)

- **[CHANNEL-DISCRIMINATOR-DERIVED]** — (i) the traveling wave is ratio-preserving (ρ'_travel = ρ_cold
  to reconcile tolerance across the in-regime y₀ band, both dictionary readings) — the per-channel
  effects CANCEL in ρ' — AND (ii) the confined mode MOVES ρ' (ρ'_conf ≠ ρ_cold). ⟹ the auto-resonance
  carrier SURVIVES channel-resolved; report the corrected matter track. **KNIFE (armed): the (i)
  cancellation must be DERIVED as a symmetry/theorem** (e.g. the soft and stiff denominator terms
  cancel by an identity keyed to the Ax3 matched point k_a=k_s, or the confined-mode asymmetry is the
  sole ρ'-mover) **or reported as unexplained-numerical at WEAKER grade.** A ratio-preserving
  cancellation is a coincidence-shaped event.
- **[SYMMETRIC-BOTH]** — both (i) and (ii) preserve the ratio (ρ'_travel = ρ'_conf = ρ_cold) ⟹ no
  tension-based discriminator exists; the auto-resonance carrier family DIES entirely; the
  /7-mechanism thread falls back to #518's S-ratio mechanism alone (matter-stiffening §4). Honest
  negative.
- **[ASYMMETRIC-BOTH]** — both (i) and (ii) MOVE the ratio (ρ'_travel ≠ ρ_cold AND ρ'_conf ≠ ρ_cold,
  in a way that does not distinguish them) ⟹ the tension-slot remap AS FORMULATED (the #526 +T/ℓ
  denominator term) CONFLICTS with canon's radiation null (#518 §7: radiation must leave ρ
  invariant). **Do NOT resolve the conflict — surface it VERBATIM** (both file paths + both verbatim
  claims: the #526 remap's T/ℓ term and canon's S_axial=S_shear null). This may implicate the #526
  T-slot scope. Flag-don't-fix; Grant adjudicates.
- **[UNDERDETERMINED]** — the decomposition needs structure canon does NOT supply; name the missing
  piece precisely (candidate: the y₀↔A_shear dictionary that fixes whether the denominator cancels at
  A_y=1 vs A_y=1/2 — canon does not pin how a purely-transverse mechanical bow maps to the
  shear-channel saturation deformation; OR: whether the #526 T/ℓ term belongs in the radiation null's
  coordinate at all).

**Bin routing (no fall-through):**
```
travel_preserves  = |ρ'_travel/ρ_cold − 1| ≤ TOL  (both dictionary readings)
conf_moves        = |ρ'_conf/ρ_cold − 1|   >  TOL
travel_moves      = not travel_preserves
conf_preserves    = not conf_moves

if travel_preserves and conf_moves:                    -> CHANNEL-DISCRIMINATOR-DERIVED
elif travel_preserves and conf_preserves:              -> SYMMETRIC-BOTH
elif travel_moves and conf_moves and not distinguish:  -> ASYMMETRIC-BOTH
else (dictionary-split decides, or ill-defined):       -> UNDERDETERMINED
```
where `distinguish` = the two ρ'-moves differ by more than TOL in sign or magnitude (a real
discriminator hides inside ASYMMETRIC if the moves differ; that routes to DERIVED-with-caveat, tested
explicitly). Any un-routed outcome is UNDERDETERMINED by construction (the final else).

**Referential integrity (Step 3.6):** every falsifier below routes to a live bin; the [UNDERDETERMINED]
bin catches the dictionary-split and the T/ℓ-scope questions; no falsifier is orphaned.

---

## KNIFE (armed — full force per the brief)

Only DERIVED factors may enter, each declared. The ½ (⟨sin²⟩, ⟨y²⟩=y₀²/2) is sympy-DERIVED (the ONE
½). The ¼ in the soft term (S≈1−A²/2, ⟨A²⟩ gives the /4) is DERIVED from the S-kernel Taylor series
(sympy). The ¾ in dD is DERIVED (1 − ¼). NO other un-derived ½/¼ may enter. Visible targets under
full knife: 2/7, 9.7734, ρ'=2, the caps (11.68 / 7.10), arc* edges [0.70, 0.96], 1/√α. Any re-banded
edge landing ON these gets coincidence-discipline (not headlined). **Special clause: ANY cancellation
in bin 1 is itself a coincidence-shaped event — derive WHY (theorem) or report as unexplained-numerical
(weaker grade).** The A_y=1/2 cancellation condition is a KNIFE tell: if a reading requires A_y=1/2 to
cancel, that is the imported yield re-expressed, NOT a theorem.

---

## GATES (via the #528 reconcile-gate helper ONLY; can-fire proofs on REAL data paths)

Every discrepancy gate is a `ReconcileGate` (`ave.validation.reconcile_gate`), `enforce(prove_first=
True)` so the can-fire self-test runs on the SAME comparator+halt path before every live gate.
Hand-rolled gates are FORBIDDEN (the defect recurred 4× before #528).

- **PC-consistency (#529 reproduction, HARD reconcile):** my channel-resolved per-bond scalar ⟨T⟩
  vs the imported `field_from_abcd_propagation(θ)["T_bond_mean"]` (the #529 Γ-free path, a DIFFERENT
  code path — I do NOT reimplement it). Must reconcile to rtol=1e-9. Proves my bookkeeping reproduces
  #529's uniform-⟨T⟩ negative before I trust the channel split. **can-fire proven on this real pair.**
- **PC-cold (zero-amplitude recovers cold EXACTLY):** y₀→0 ⟹ ρ'_travel→ρ_cold AND ρ'_conf→S(A_dc)
  (the biased cold ratio). Reconcile the y₀=0 ρ' against a DIRECT `_prestress_tensor_at(A_axial,
  A_shear, T=0)` call (independent code path — the merged remap at T=0). rtol=1e-10.
- **PC-numerator (independent-reference positive control, no self-verifying identity):** S_axial(√α)
  computed in my bookkeeping vs `saturation_factor(√α)` from the axiom kernel (different code path).
  rtol=1e-12.
- **PC-denominator-independent-recompute:** my ρ'_travel(y₀) vs an INDEPENDENT assembly — build the
  denominator from `saturation_factor(A_shear)` (kernel) + `bond_tension(A_axial)`-derived T
  (prestress module), NOT from my analytic 2nd-order series. The analytic series and the
  full-kernel assembly must reconcile within the 2nd-order truncation band (rtol set by the y₀⁴
  residual, reported). This is the #527-defect guard: the reference is NOT the defining identity, it
  is the full-kernel recompute vs my truncated series.
- **DISCREPANT-HALT (synthetic-trigger):** a unit test injects a hand-mismatched (claimed,
  independent) pair through `ReconcileGate.prove_can_fire()` on EACH gate's real data path and asserts
  `DiscrepantHalt`/`DeadGateError` fires. No gate is trusted until its halt is proven live on its own
  data.

**Structural-degeneracy (Step 3.8b):** ρ' is a LOCAL per-bond ratio, not a global sum on a closed
graph — NOT bookkeeping-forced to any value. The cold recovery (y₀→0 → ρ_cold) is an EARNED identity,
gated by PC-numerator proving the kernel reads S(√α)≠1 (a known-nonzero shift).

**Positive control for the null direction (Step 3.8a):** the [SYMMETRIC-BOTH] / preservation verdict
is a NULL (ρ' unchanged). Its positive control = the CONFINED mode at A_dc=√α, which MUST read
ρ'_conf = S(√α) ≠ ρ_cold through the IDENTICAL pipeline — the known-nonzero case. No preservation
verdict is bookable until the confined-mode pipeline demonstrably reads the biased ratio.

---

## OBSERVABLE ROBUSTNESS LADDER (Step 3.7a — declared PRE-freeze)

PRIMARY (gating) observable = the SIGN/EXISTENCE of the ρ'-move for each wave type (preserved vs
moved), and the SIGN of the DIFFERENCE between (i) and (ii). The ρ'-shift MAGNITUDE is
supplementary/reported (banded over δ_y and the in-regime y₀ range, log-spaced grid). If the
magnitude proves y₀-dictionary-ridden (scope caveat b), the form-end result — which channel moves and
whether (i) and (ii) differ — still stands. Re-banded ρ'/ν edges reported as bands, six digits
forbidden.

**Gate-floor consistency (Step 3.7b):** the in-regime y₀ grid bottoms at y₀→0 (the cold identity,
LABELED and excluded from the moved-band) and tops at the #527 in-regime bow ceiling. No gate demands
a sign at y₀=0 (where the move is identically zero — the noise-floor cell); the identity endpoint is
excluded from the move-verdict, reported as the labeled identity it approaches.

---

## STAKES-TABLE SECTOR CLASSIFICATION (Step 3, AC/DC carve clm-acdc07)

- **ρ'_travel and ρ'_conf (the re-banded matter/radiation tracks):** **DC-internal** — a DC-bias
  operating-point ratio (the resonant hum + the A1-core DC bias set the #526 stiffness ratio). No AC
  readout yet ⟹ NOT a framework-level result; a consistency-class DC-internal re-band. A preservation
  null on the traveling wave is EXPECTED (radiation transparency is mandatory, #518 §7), so
  ρ'_travel-preserved is a REQUIRED consistency pass, NOT a falsifiable framework negative. The
  falsifiable content is the ASYMMETRY (i)-preserved while (ii)-moved, OR the CONFLICT (i)-moved
  contradicting the mandatory radiation transparency.

---

## LEDGER — canon-forced vs engineering-choice (the knife, tallied; all magnitudes banded)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel S(A)=√(1−(A/A_y)²) | CANON-FORCED | Axiom 4 (`saturation_factor`) |
| 2 | Remap ρ'=S_axial/(S_shear+T/ℓ) | CANON-FORCED (MERGED) | #526 (`_prestress_tensor_at`) |
| 3 | Part-1 geometric T=(k_a/ℓ)y₀² | DERIVED (IMPORTED) | #529 (`resonant_tension_law`, ⟨sin²⟩=½ sympy) |
| 4 | S keyed on DEFORMATION not stress; no-double-count | GRANT-RULED (2026-07-05) | this prereg, verbatim above |
| 5 | S_axial untouched by ⟨A⟩=0 wave (axial deform 4th-order) | DERIVED (from 4) | consequence 1 |
| 6 | Shear ⟨A²⟩ keying → soft term −¼y₀²/A_y² | DERIVED | S-Taylor (sympy), node-up:144 |
| 7 | y₀↔A_shear dictionary (angle vs displacement) | UNDERDETERMINED (both run) | scope caveat b — KEEP-BOTH |
| 8 | A_dc=√α (confined-mode axial bias) | CANON-FORCED (α-echo) | def-vyvsn1 |
| 9 | A_y=1 yield | CANON-FORCED | def-vyvsn1 |
| 10 | The A_y=1/2 cancellation condition | KNIFE TELL (NOT canon) | derived — would be import-in-costume |

**Tally: 6 canon-forced + 3 derived + 1 underdetermined (both-run). 0 free parameters tuned.**

---

## FALSIFIERS (each routes to a live bin)

- **F1:** ρ'_travel ≠ ρ_cold beyond TOL (both readings) AND ρ'_conf ≠ ρ_cold, moves indistinguishable
  → [ASYMMETRIC-BOTH] (the conflict). *(Pre-freeze expectation leans here for the traveling wave,
  from the +¾y₀² non-cancellation — but the confined-mode numerator asymmetry may still distinguish
  them, routing to DERIVED-with-caveat.)*
- **F2:** ρ'_travel = ρ_cold AND ρ'_conf = ρ_cold → [SYMMETRIC-BOTH] (carrier dies entirely).
- **F3:** ρ'_travel = ρ_cold (cancellation) AND ρ'_conf ≠ ρ_cold → [CHANNEL-DISCRIMINATOR-DERIVED] —
  BUT only if the cancellation is a derived theorem (else weaker grade / UNDERDETERMINED).
- **F4:** the verdict flips between dictionary reading D1 and D2 → [UNDERDETERMINED] (the dictionary
  is the missing structure; name it).
- **F5 (framing falsifier):** if S_axial turns out to be y₀-dependent at 2nd order (numerator moves
  with the hum), Grant's consequence-1 no-double-count reading is wrong — HALT and re-surface to
  Grant (do not re-bin).
