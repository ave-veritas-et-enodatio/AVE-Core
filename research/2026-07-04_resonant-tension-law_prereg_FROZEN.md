# PREREG (FROZEN) — the RESONANT TIME-AVERAGED TENSION LAW + the radiation control

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/resonant-tension-law`
**Target:** (Part 1) derive the time-averaged tension of a standing transverse oscillation
`y(t)=y₀·sin(ωt)` on the tent-geometry bond, feed it through the merged #526 remap, and re-band
the matter track; (Part 2, make-or-break) the radiation control — show that a TRAVELING transverse
wave on an Ax3-matched line exerts NO time-averaged axial reaction (so it does NOT stiffen), while
a BOUND standing wave between reflecting terminations DOES, recovering the Part-1 law.
**This prereg is FROZEN before the driver** (commit order proves it). Bins verbatim below; no
post-data edits (Rule 11).

**Resolves the OPEN plucking-mechanism fork** left by PR #527
(`research/2026-07-04_bond-force-sign-rule_result.md`): the arm-(a) tent law `T_a(y)=k_a·ℓ·(1−ℓ/√(ℓ²+4y²))
≈ (2k_a/ℓ)y²` needs a PLUCKER. GRANT'S RULING (this arc's subject, ratified 2026-07-04): the bond
is **not plucked — it AUTO-RESONATES**. The electron is a resonant LC tank at a self-set Q-point
(`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`:10);
its bonds carry a standing transverse oscillation with `⟨y⟩=0` but `⟨y²⟩>0`, and because the pluck
law is QUADRATIC, the time-averaged tension survives — **the tank's own hum IS the bias.**

**Stacks on (all MERGED, grep-verified this session at branch HEAD cffc9f85):**
- PR #527 `src/scripts/vol_1_foundations/bond_force_sign_rule.py` — the tent law `arm_a_pluck_tension`,
  the leading law `arm_a_pluck_tension_leading`, the in-regime bow bound `in_regime_pluck_bow`,
  the four-track remap `four_tracks`/`_remap_at_signed_T`. CONSUMED BY IMPORT (never edited).
- PR #526 `src/scripts/vol_1_foundations/prestress_elastic_tensor.py` — the remap `k_shear_eff =
  S_shear + T/ℓ`, `bond_tension`, `extract_prestress_Cij`, `moduli_from_Cij`. CONSUMED BY IMPORT.
- PR #525 `src/scripts/vol_4_engineering/bond_transmission_line.py` — `cascade_gamma`,
  `abcd_lossless_line`; the Ax3 matched-line theorem `clm-mfb2ax` (Γ_internal=0 at ρ_bond=1).
  CONSUMED BY IMPORT.
- #518 §7 radiation canon (`research/2026-07-04_matter-stiffening-rho_result.md`:37,146-157): a
  pure-AC traveling wave (⟨A⟩=0) ⟹ ρ_eff=ρ_cold IDENTICALLY (two reasons: symmetric-internal R1;
  displacement-pump null `clm-clvchn` NULL-CONFIRMED-FINAL). The control MUST respect this.

---

## SUBSTRATE-FIRST SECTOR HEADER

- **SECTOR:** the **MECHANICAL transverse bow DOF** on the K4/srs bond (the tent-geometry pluck
  response). This is the SAME transverse mechanical mode PR #527 arm (a) plucks — NOT the Cosserat
  `(2,3)` winding. **T2 HOMONYM GUARD (binding, cite #527):** the static Cosserat winding carries
  NO real power (lossless-reactive constraint, `resonant-lc-solitons.md`:128) and canNOT be the
  plucker; the resonance here is the mechanical bow, never re-welded to the winding. mass=A1;
  charge=Cosserat-winding; the bow=T2-mechanical-response — do NOT cross-wire.
- **MODE:** cycle-averaged **quasi-static about the resonant Q-point.** The bond hums at ω_resonant;
  the tensor probe reads the DC-biased small-signal network around that Q-point.
- **TIMESCALE-SEPARATION ASSUMPTION (declared):** resonance period `2π/ω_resonant` ≪ the
  tensor-probe timescale, so the tensor sees the CYCLE-AVERAGED tension `⟨T⟩`, not the instantaneous
  `T(t)`. This is the standing assumption that lets `⟨y²⟩` act as a static DC bias into the #526
  remap (matches #526/#527's "static DC bias ⟹ time-average factor 1" convention, but here the
  factor is `⟨sin²⟩=½`, DERIVED not asserted).
- **REGIME:** Op14 ON. **PHASE-STATE = the resonant Q-point** (a standing reactive mode, Ax3
  lossless; the closed-EM-port eigenframe has Im(ω)→0, Q→∞ per `resonant-lc-solitons.md`:104).
  A→0 / y₀→0 is the no-hum limit (positive-control anchor, ⟨T⟩→0).
- **COORDS (A46):** the tension is derived in the bond's own arc-length/phase-space coordinate
  (transverse bow y₀, projected to the axial chord pull); the tensor readout is real-space/spatial-
  Brillouin via the #526 pipeline. Each in its own coordinate — A46-clean, matching #526/#527.
- **CLASS (consistency-vs-emergence):** **CONSISTENCY / MANIFESTATION.** The resonant-tension law is
  an Ax4-microfoundation manifestation (the tent law is #527-canon; the ⟨·⟩ is a time-average). The
  matter-track ρ'/ν VALUES inherit #526's GR-imported 9.7734 status — **EMERGENCE grade FORBIDDEN.**
  α enters only through the A1 op-point `A=√α` (Class-C echo, def-vyvsn1). ½ is a DERIVED
  time-average factor (⟨sin²⟩); NO OTHER un-derived ½/¼ may enter.

---

## PART 1 — THE RESONANT TENSION LAW (derivation target)

**(a) Leading order (analytic, sympy-verified pre-freeze):**
For `y(t)=y₀·sin(ωt)` the leading tent law `T_lead(y)=(2k_a/ℓ)y²` time-averages to

> **⟨T⟩ = (2k_a/ℓ)·⟨y²⟩ = (k_a/ℓ)·y₀²**,  with **⟨y²⟩ = y₀²·⟨sin²⟩ = y₀²/2** (⟨sin²⟩=½ DERIVED).

Sympy pre-freeze (`sp.integrate(sin²(ωt),(t,0,2π/ω))/period = 1/2`; `⟨T_lead⟩ = k_a·y₀²/ℓ` exact).

**(b) Exact tent law, cycle-averaged numerically:** `⟨T_a⟩ = (1/2π)∮ k_a·ℓ·(1−ℓ/√(ℓ²+4y₀²sin²θ)) dθ`.
The quadratic approximation is an UPPER BOUND on the exact average (the exact law is concave in y²);
it breaks progressively vs the in-regime bow. **Dimensional/anchor pre-check (Step 3.5):** with
k_a=ℓ=1, ⟨T_lead⟩=y₀²; the exact average tracks it to +0.02% at y₀=0.01, +0.56% at y₀=0.05, +4.4% at
y₀≈0.14 (tent-edge in-regime bow), +37% at y₀≈0.42 (elastica-edge in-regime bow). So the leading law
is trustworthy at the tent edge (~4%) and materially over-predicts at the elastica edge (~37%) —
reported as a band, NOT collapsed to one number.

**(c) Feed ⟨T⟩ through the #526 remap** (`_remap_at_signed_T`, imported): re-band the matter track
over δ_y (the inherited #526 normalization) and the in-regime y₀ range `y₀ ∈ [0, in_regime_pluck_bow(arc*)]`
for arc* ∈ [0.70, 0.96]. **⟨T⟩>0 (tension) ⟹ caps ρ'** (grows k_shear_eff), matching #527 arm (a).

**Mode-shape convention (declared):** bond-level tent bow (the #527 arm-(a) geometry; the whole bond
bows as a single tent, amplitude y₀ at midspan). **y₀↔A dictionary:** y₀ is the transverse bow
amplitude in ℓ_node units; the inherited δ_y normalization is #526's `arc*/0.96` displacement scale
(the tent-edge-normalized in-regime displacement). NOT re-derived — inherited verbatim from #526.

---

## PART 2 — THE RADIATION CONTROL (make-or-break; the mechanism MUST be allowed to die)

**The threat:** a TRAVELING transverse wave also has `⟨y²⟩=y₀²/2` at a fixed bond while the train
passes. Naive ⟨y²⟩-tension would therefore stiffen radiation too — CONTRADICTING #518 §7
(`ρ_eff=ρ_cold` for pure-AC traveling wave; `clm-clvchn` displacement-pump null).

**Grant's candidate discriminator (TESTED, not assumed):** on an Ax3-MATCHED line (`clm-mfb2ax`,
Γ_internal=0 at ρ_bond=1) a traveling wave exchanges NO time-averaged momentum with the lattice —
no reflection ⟹ no static reaction force ⟹ no persistent tension. A BOUND standing mode is confined
by reflection (the Γ=−1 self-trap wall, `resonant-lc-solitons.md`:47) and its tension is the static
REACTION to confinement. **Radiation pressure exists ONLY where there is reflection.**

**COMPUTE (on the #525 TL machinery, imported):** the time-averaged NET axial force on an interior
bond, from the momentum-flux balance `⟨F_axial⟩ ∝ (|inc|² − |ref|²)` gradient:
- **(i) traveling wave on a MATCHED chain** (`cascade_gamma(full(N,Z_0), Z_0, θ)`): Γ→0, so incident
  and transmitted momentum flux are EQUAL at every interior bond ⟹ the flux is uniform ⟹
  `d⟨F_axial⟩/dx = 0` ⟹ NET interior reaction → 0. (Ax3 lossless: no absorption, nothing deposited.)
- **(ii) standing wave between REFLECTING terminations** (`cascade_gamma(full(N,Z_0), 0, θ)` short /
  `→∞` open, |Γ|=1): the wave is turned around at the wall; the momentum flux VARIES with position
  (antinode vs node) ⟹ the local axial reaction is nonzero and integrates to the confinement force
  at the Γ=−1 wall ⟹ recovers the Part-1 tent-law ⟨T⟩ evaluated at the local ⟨y²⟩.

**Independent reference path (no self-verifying control):** (i) is checked TWO ways — (1) the
`cascade_gamma` reflection read (|Γ|→0 on the matched chain), and (2) an INDEPENDENT momentum-flux
integral over an explicit `abcd_lossless_line` traveling-wave field (the axial-reaction integrand
computed from the field directly, NOT from Γ). The two must agree that the matched-line net axial
reaction vanishes. The standing-wave (ii) reaction is computed from the SAME momentum-flux integrand
on the reflected (|Γ|=1) field — a DIFFERENT boundary condition through the SAME code path, so (ii)
recovering the Part-1 law is a genuine cross-check, not a re-assertion.

---

## FROZEN BINS (verbatim; no post-data edits)

- **[RESONANT-CARRIER-DERIVED]** — Part 1 law derived (leading + exact, ½ sympy-verified) AND Part 2
  control passes: (i) matched-line net axial reaction vanishes (both reference paths, |Γ|<1e-9 and
  the independent flux integral → 0 within tol), AND (ii) the reflecting-termination reaction
  recovers the Part-1 tent-law ⟨T⟩. ⟹ the plucking fork RESOLVES: the matter arm's carrier is the
  CONFINED RESONANCE; the magnitude-law noun = the time-averaged resonant law; matter track re-banded.
- **[RADIATION-CONTAMINATED]** — the traveling-wave control (i) does NOT vanish (matched-line net
  axial reaction stays > tol) ⟹ the resonant-tension carrier contradicts #518 §7 / `clm-clvchn` ⟹
  the mechanism DIES as stated; report honestly, no rescue (Rule 11).
- **[DISCRIMINATOR-UNDERDETERMINED]** — the standing/traveling separation needs structure canon does
  NOT supply (name it precisely: e.g. the matched-line reaction is neither cleanly zero nor cleanly
  the Part-1 law, or the momentum-flux integrand requires a nonlinear term the #525 linear TL cannot
  host); defer.

**Bin routing / referential integrity:** (i)-vanishes AND (ii)-recovers → RESONANT-CARRIER-DERIVED;
(i)-nonzero → RADIATION-CONTAMINATED; separation-ill-defined → DISCRIMINATOR-UNDERDETERMINED. No
fall-through: any un-routed outcome is DISCRIMINATOR-UNDERDETERMINED by construction.

## KNIFE (armed)

½ is a DECLARED-DERIVED factor (⟨sin²⟩, sympy-verified) — but **no OTHER un-derived ½/¼ may enter.**
Visible targets under full knife treatment if a re-banded matter-track edge lands ON them: 2/7,
9.7734, the 7.10 cap, ρ'=2, arc* edges [0.70, 0.96], 1/√α. A re-banded edge landing on any of these
gets coincidence-discipline treatment in the result doc (not headlined as a chord).

## GATES (defect-history-aware; the reconcile recurred 3× at #521/#526/#527)

- **Positive controls (HALT-gated), each an INDEPENDENT reference path:**
  - PC-half: sympy ⟨sin²⟩=½ AND ⟨T_lead⟩=k_a·y₀²/ℓ, exact-zero residuals.
  - PC-lead-vs-exact: leading ⟨T⟩ matches exact-law cycle-average to declared band edges.
  - PC-noload: y₀→0 ⟹ ⟨T⟩→0 (no-hum anchor).
  - PC-matched: `cascade_gamma` on a Z_0-uniform chain returns |Γ|<1e-12 (the #525 matched-line
    positive control — a KNOWN-zero reflection through the imported callable).
  - PC-reflect: `cascade_gamma` on a shorted/open termination returns |Γ|=1 (the KNOWN-nonzero
    reflection — proves the discriminator instrument can read a reflecting wall, per liveness
    ave-prereg Step 3.8a).
- **DISCRIMINANT-HALT (a REAL reconcile, independent recomputation + synthetic-trigger tests):** the
  Part-2 verdict recomputes the matched-line net axial reaction TWO independent ways (Γ-read vs
  direct momentum-flux field integral); if they DISAGREE beyond tol the driver HALTs (does not bin).
  A synthetic-trigger unit test feeds a hand-mismatched pair to prove the HALT fires. This is NOT a
  re-check of a defining identity (the #521/#526/#527 checklist defect) — the two paths are
  different assemblies (a reflection functional vs a field-space momentum integral).
- **Structural-degeneracy (ave-prereg Step 3.8b):** the matched-line net-reaction is NOT a global
  sum on a closed graph (it is a local interior-bond reaction on an open cascade), so it is NOT
  bookkeeping-forced to zero; the reflecting-termination reaction is nonzero by construction —
  checked. The (i)→0 result is therefore an EARNED zero, gated by PC-reflect proving the instrument
  reads nonzero on the known reflecting case.

## OBSERVABLE ROBUSTNESS LADDER (ave-prereg Step 3.7a — declared PRE-freeze)

PRIMARY (gating) observable = the SIGN/EXISTENCE of the matched-line net axial reaction (zero vs
nonzero) — the Part-2 bin turns on this. The Part-1 ⟨T⟩ MAGNITUDE is supplementary/reported (banded,
not gating). If the ⟨T⟩ magnitude proves δ_y-knob-ridden (it inherits #526's normalization fork),
the form-end result — (i) vanishes, (ii) recovers the tent-law FORM — still stands as the carrier
resolution. The re-banded matter-track ρ'/ν edges are reported as bands, never as six-digit values.

## STAKES-TABLE SECTOR CLASSIFICATION (ave-prereg Step 3, AC/DC carve clm-acdc07)

- Part-1 ⟨T⟩ and the matter-track re-band: **DC-internal** (a DC-bias operating-point quantity; the
  resonant hum sets a DC ⟨y²⟩ that biases the #526 stiffness ratio). No AC readout yet ⟹ NOT a
  framework-level result, a consistency-class DC-internal re-band.
- Part-2 control: the matched-vs-reflecting separation is the **DC→AC boundary** statement (a
  traveling AC wave deposits no DC bias; a confined AC standing mode does). A null on (i) is
  EXPECTED (Maxwell/radiation recovery is mandatory, #518 §7), so (i)→0 is a REQUIRED consistency
  pass, NOT a falsifiable framework negative. The falsifiable content is the ASYMMETRY: (i)=0 while
  (ii)≠0. A failure of that asymmetry (RADIATION-CONTAMINATED) is the real negative.

---

<!-- FOOT-NOTE (2026-07-04, orchestrator re-run; appended at foot so it shifts NO body line
numbers — cites index this prereg by line). The BINS above stay FROZEN and are UNCHANGED. Only the
(i) OBSERVABLE they read was corrected, which is NOT a bin edit:

  🔴 OBSERVABLE CORRECTION (CRITICAL): this frozen prereg named the (i) observable as the "net axial
  reaction / momentum-flux GRADIENT (|inc|²−|ref|²)" (lines ~105,115-118,127,131,162,175). That was
  the WRONG observable — the gradient is trivially zero for a uniform traveling wave, but the
  mechanism CONSUMES the per-bond ⟨T⟩ itself (_remap_at_signed_T: k_shear_eff=S_shear+T/ℓ). The
  driver + result doc re-gate (i) on the CONSUMED per-bond ⟨T⟩. Re-gated, (i) does NOT vanish (the
  matched CW traveling wave carries a persistent ⟨T⟩), routing the SAME frozen bins to
  [RADIATION-CONTAMINATED]. See research/2026-07-04_resonant-tension-law_result.md §HONEST RE-RUN.

  🔴 INDEPENDENCE CORRECTION (MAJOR-1): the prereg promised a "Γ-free abcd_lossless_line" independent
  path (lines ~114-118); the original driver imported but never called it, and the field path it did
  use was algebraically 1.4244·|Γ| (the SAME Γ). The re-run builds the genuinely Γ-free
  ABCD-propagation path (field_from_abcd_propagation); the reconcile is now a real value-reconcile. -->

