# RESULT — the RESONANT time-averaged tension law + the radiation control

> ## 🔴 SUPERSEDED VERDICT (2026-07-04, orchestrator re-run) — the carrier DIES
>
> **The live verdict is [RADIATION-CONTAMINATED], not [RESONANT-CARRIER-DERIVED].** The
> orchestrator review (1 CRITICAL, 4 MAJOR confirmed) found the Part-2 control gated the
> **gradient** of ⟨T⟩ (trivially zero for a uniform traveling wave), while the mechanism
> **consumes ⟨T⟩ itself** (`_remap_at_signed_T`: `k_shear_eff = S_shear + T/ℓ`). Re-gated on the
> consumed observable: a matched CW traveling wave carries a **persistent per-bond ⟨T⟩ = (k_a/ℓ)y0²**
> — identical in kind to the confined hum — and fed through the same remap it stiffens ρ' **9.773 →
> 0.904**. Radiation stiffens exactly as matter does; the resonant-tension carrier as formulated
> **cannot distinguish matter from radiation** and contradicts #518 §7. **Rule 11: the mechanism DIES
> as stated; no rescue.** The honest re-run + numbers are in **§HONEST RE-RUN** below; the original
> body is PRESERVED (Rule 12) as the falsified hypothesis's record, with 🔴 inline corrections on the
> load-bearing false claims. The magnitude discriminator, if any, is CHANNEL-RESOLVED (does the
> traveling wave tension both channels symmetrically while the hum tensions shear asymmetrically?) —
> that is a NEW prereg for a future arc, not a patch to this one.

---

## HONEST RE-RUN (the live result, 2026-07-04)

**Verdict: [RADIATION-CONTAMINATED].** Driver `src/scripts/vol_1_foundations/resonant_tension_law.py`;
tests `src/tests/test_resonant_tension_law.py` (26 passed); output
`src/scripts/vol_1_foundations/_output/resonant_tension_law.json`.

**Part 1 (STANDS — the law is derived):** `⟨T⟩ = (2k_a/ℓ)⟨y²⟩ = (k_a/ℓ)y0²`, `⟨sin²⟩=½` sympy-DERIVED
(5 exact-zero residuals). Exact tent cycle-average over-predicts +0.05% (small hum) → +4.5% (tent
edge) → +36% (elastica edge). The law is real; what fails is its use AS A MATTER/RADIATION
DISCRIMINATOR.

**Part 2 (the make-or-break — FAILS):**
- **(i) matched CW traveling wave, re-gated on the CONSUMED per-bond ⟨T⟩:** phasor path ⟨T⟩ =
  **1.000000**, genuinely Γ-free ABCD-propagation path ⟨T⟩ = **1.000000** (value-reconcile rel =
  2.2×10⁻¹⁵; the two paths are now genuinely independent — the Γ-free path takes NO Γ input). **⟨T⟩
  does NOT vanish.** Remap consequence: **ρ' 9.7733 → 0.9042** (radiation stiffens).
- **(ii) standing wave (Γ=−1):** antinode ⟨T⟩ = 4.0000 (grid 3.9999) recovers 4× the Part-1 unit law
  — but this is MOOT: the carrier already died at (i).

**Matter re-band (reported for completeness only — MOOT):** interior ρ' ∈ [4.36, 9.77) (exact),
ν ∈ [−0.015, 2/7); the y0→0 identity twins **ρ'→9.7734 AND ν→2/7 (BOTH the unstressed #518
crossing)** are labeled and excluded from the band (symmetric knife).

**Scope caveats (MAJOR-4b/c):**
- **(b) ladder scope:** the Part-2 control that killed the carrier is a **1D linear TL ladder**
  (#525 `cascade_gamma` / `abcd_lossless_line`); the full **srs-lattice generalization is UNTESTED.**
  The negative is drawn from the 1D linear ladder — a channel-resolved srs test could in principle
  behave differently (that is the future-arc prereg, not a rescue of this one).
- **(c) mode-shape feeding the remap:** the matter re-band feeds the **bond-level ⟨T⟩** (the tent-bow
  cycle-average `(k_a/ℓ)y0²`, a single per-bond scalar) into `_remap_at_signed_T` — NOT a per-mode
  antinode value. The standing-mode antinode (4×) and bond-average (`(k_a/ℓ)y0²(1+|Γ|²)`) are
  reported in `ii_standing` for the discriminator only; the remap band uses the per-bond ⟨T⟩ because
  that is the uniform static bias the #526 remap consumes (matching #527 arm (a)).

---

<details><summary>🔴 PRESERVED (Rule 12) — the original [RESONANT-CARRIER-DERIVED] body, FALSIFIED. Read as the record of the wrong hypothesis, with inline 🔴 corrections.</summary>

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/resonant-tension-law`
**Prereg (FROZEN):** `research/2026-07-04_resonant-tension-law_prereg_FROZEN.md` (committed BEFORE
the driver; commit order proves it).
**Driver:** `src/scripts/vol_1_foundations/resonant_tension_law.py`
**Tests:** `src/tests/test_resonant_tension_law.py`.
**Output:** `src/scripts/vol_1_foundations/_output/resonant_tension_law.json`.

## VERDICT: ~~**[RESONANT-CARRIER-DERIVED]**~~ 🔴 FALSIFIED → [RADIATION-CONTAMINATED] (see top)

🔴 The three sentences below are FALSE as implemented: (i) did NOT exert "no reaction" — it gated
the GRADIENT, not the consumed ⟨T⟩; "both independent paths" were one computation (the field path was
algebraically 1.4244·|Γ|). Preserved as the falsified claim.

Part 1 law derived (leading + exact, ½ sympy-verified) AND the make-or-break Part-2 radiation
control passes: (i) the traveling wave on the Ax3-matched line exerts NO time-averaged axial
reaction (both independent paths), and (ii) the standing wave between Γ=−1 reflecting terminations
is nonzero and recovers the Part-1 tent-law ⟨T⟩. **The plucking fork RESOLVES: the matter arm's
carrier is the CONFINED RESONANCE; the magnitude-law noun = the time-averaged resonant law; the
matter track is re-banded.**

---

## GRANT'S RULING (this arc's subject, ratified 2026-07-04 — the driver TESTS it, does not assume it)

> The bond is **not plucked — it AUTO-RESONATES.** The electron is a resonant LC tank at a self-set
> Q-point (`resonant-lc-solitons.md`:10); the standing transverse oscillation on its bonds has
> `⟨y⟩=0` but `⟨y²⟩>0`, and since the pluck law is QUADRATIC, the time-averaged tension survives:
> the tank's own hum IS the bias. The resonant time-averaged law is the candidate magnitude-law noun
> for the matter arm.

The ontology is Grant-ratified and corpus-anchored (electron = confined standing wave, Γ=−1 TIR
wall, `resonant-lc-solitons.md`:25-52,104). This arc COMPUTES the two things that were not yet
settled: the time-averaged law itself, and — the make-or-break — whether the same ⟨y²⟩ that biases
matter would also (wrongly) stiffen radiation.

---

## PART 1 — THE RESONANT TENSION LAW

### (a) Leading order (analytic, sympy-verified — 5 exact-zero residuals)

> **⟨T⟩ = (2k_a/ℓ)·⟨y²⟩ = (k_a/ℓ)·y₀²**,  with **⟨y²⟩ = y₀²·⟨sin²⟩ = y₀²/2** (⟨sin²⟩=½ **DERIVED**).

Sympy backbone (all residuals exactly 0):
- `⟨sin²⟩ − ½ = 0` — the ONE ½ of this arc, DERIVED not asserted.
- `⟨y²⟩ − y₀²/2 = 0`.
- `⟨T_lead⟩ − (k_a/ℓ)y₀² = 0` — the leading time-average.
- `⟨T_lead⟩ − (2k_a/ℓ)⟨y²⟩ = 0` — the substitution the noun rests on.
- `[exact-tent 2nd-order coeff] − 2k_a/ℓ = 0` — ties the resonant law to the **#527 exact tent law's
  own series** (not a fresh guess).

### (b) Exact tent law, cycle-averaged numerically — where the quadratic breaks

`⟨T_a⟩ = (1/2π)∮ k_a·ℓ·(1−ℓ/√(ℓ²+4y₀²sin²θ)) dθ` (the #527 exact tent law, IMPORTED). The exact
law is concave in y², so **the leading law is a strict UPPER BOUND**; it over-predicts the exact
cycle-average by:

| y₀ | leading/exact rel-dev | note |
|---|---|---|
| 0.01 | +0.02% | small-hum: quadratic trustworthy |
| 0.05 | +0.56% | |
| 0.1428 (tent edge) | **+4.5%** | in-regime tent-edge bow (arc*=0.96) |
| 0.4153 (elastica edge) | **+36.1%** | in-regime elastica-edge bow (arc*=0.70) |

**Where the quadratic breaks:** the approximation is good (~4%) at the tent edge and materially
over-predicts (~36%) at the elastica edge — reported as a band, NOT collapsed to one number.

### (c) Matter track re-banded through the #526 remap

Fed the RESONANT ⟨T⟩ (tension, +) through the merged #526 `_remap_at_signed_T` (imported) at the A1
op-point `A_axial=√α` (S≈0.996) and the #518 shear operating amplitude `A_shear=0.99479`, banded
over the in-regime hum amplitude `y₀ ∈ [0, in_regime_pluck_bow(arc*)]` for arc* ∈ [0.70, 0.96]:

| edge (arc*) | y₀ range | ρ' (exact) at y₀_max | ν at y₀_max |
|---|---|---|---|
| tent (0.96) | [0, 0.1428] | 8.20 | +0.243 |
| elastica (0.70) | [0, 0.4153] | 4.36 | −0.015 |

> **Re-banded matter track (exact law): ρ' ∈ [4.36, 9.65], ν ∈ [−0.015, +0.283].**
> (Leading-law band: ρ' ∈ [4.14, 9.65] — slightly lower because the leading ⟨T⟩ over-caps.)
>
> 🔴 MAJOR-4a correction: this band MISQUOTED the driver JSON (the 9.65/+0.283 top was a grid
> artifact of the arbitrary 0.25·y0_max first sample). Honest log-grid values (see §HONEST RE-RUN):
> exact ρ' ∈ [4.36, 9.77), ν ∈ [−0.015, 2/7), with the y0→0 identity twins ρ'→9.7734 AND ν→2/7
> excluded. And it is MOOT — the carrier died at Part 2.

The **⟨T⟩>0 (tension) CAPS ρ'** (grows `k_shear_eff = S_shear + T/ℓ`), matching the #527 arm-(a) sign
rule. At **y₀→0 the remap is unshifted ⟹ ρ'=9.7733** — the cold GR-imported ρ*≈9.7734 recovered as
the no-hum limit (a T→0 IDENTITY, see KNIFE).

**Mode-shape convention (declared):** bond-level tent bow (the #527 arm-(a) geometry). **y₀↔A
dictionary:** y₀ is the transverse bow amplitude in ℓ_node units; the inherited δ_y normalization is
#526's `arc*/0.96` displacement scale — NOT re-derived, inherited verbatim.

---

## PART 2 — THE RADIATION CONTROL (make-or-break; the mechanism was allowed to die)

**The threat (verbatim from the prereg):** a TRAVELING transverse wave also has `⟨y²⟩=y₀²/2` at a
fixed bond while the train passes. Naive ⟨y²⟩-tension would therefore stiffen radiation too —
CONTRADICTING #518 §7 (`ρ_eff=ρ_cold` for pure-AC traveling wave;
`research/2026-07-04_matter-stiffening-rho_result.md`:146-157) and `clm-clvchn` (displacement-pump
NULL-CONFIRMED-FINAL).

**Grant's candidate discriminator (TESTED, confirmed):** radiation pressure exists ONLY where there
is reflection.

### (i) Traveling wave on the Ax3-MATCHED line — the reaction VANISHES (two independent paths)

Computed on the #525 `cascade_gamma` / field machinery (imported):

| path | value | interpretation |
|---|---|---|
| Γ-read (`cascade_gamma`, matched Z_0 chain) | \|Γ\| = **4.6×10⁻¹⁸** | no internal reflection (clm-mfb2ax) |
| INDEPENDENT field momentum-flux RMS | **2.0×10⁻¹⁵** | ⟨T⟩(x) uniform ⟹ zero axial gradient |

Both vanish. **The traveling wave carries momentum THROUGH but deposits none (Ax3 lossless) ⟹ no
static bias ⟹ ρ_eff=ρ_cold respected.** This is the REQUIRED consistency pass with #518 §7 — a
null here is EXPECTED (Maxwell/radiation recovery is mandatory), not a framework negative.

### (ii) Standing wave between Γ=−1 reflecting terminations — recovers the Part-1 law

| quantity | value |
|---|---|
| \|Γ\| (short termination, the Γ=−1 self-trap wall) | 1.000000 |
| field momentum-flux reaction RMS | **1.439** (nonzero) |
| antinode ⟨T⟩ (analytic) | **4.0000** |
| 4× Part-1 unit law (constructive \|Γ\|=1 antinode) | 4.0000 |

The reflection turns the wave around; ⟨y²(x)⟩ varies (antinode = ½y₀²(1+\|Γ\|)² = 2y₀²), so the
tent-law tension varies with position and integrates to the confinement force at the Γ=−1 wall.
**The antinode ⟨T⟩ recovers exactly 4× the Part-1 unit law** — the standing mode recovers the Part-1
tent-law FORM through the SAME field integrand.

### The reconcile (independent recomputation; the DISCREPANT-HALT gate)

The two (i) paths — the Γ-read (a reflection functional) and the field momentum-flux gradient RMS (a
field-space integral) — are DIFFERENT assemblies. They **agree** that the matched-line reaction
vanishes. The `reconcile_matched_reaction` gate HALTs if they disagree; a **synthetic-trigger test**
(`test_discrepant_halt_fires_when_paths_disagree`) proves the gate fires on hand-mismatched inputs.
This closes the reconcile-gate defect that recurred at #521/#526/#527 (a real independent
recomputation, not a re-check of one identity).

---

## THE KNIFE (armed; coincidence discipline)

- **½** is the DECLARED-DERIVED time-average factor (⟨sin²⟩, sympy exact-zero). No OTHER un-derived
  ½/¼ enters this arc.
- **ρ'=9.7734 at y₀→0** — the re-banded track's endpoint sits ON the GR-imported 9.7734, but this is
  the **T→0 IDENTITY** (⟨T⟩=0 ⟹ the remap is trivially the cold value), the no-hum limit, NOT a
  re-banded landing. KNIFE=noise: it is definitional, not a coincidence.
- **Interior re-band (y₀>0): ρ' ∈ [4.36, 9.65]** does NOT reach the ρ'=2 canon crossing, does not
  land on 7.10, does not land on 2/7. **No interior edge lands on a canon-distinguished value.**
- ν band bottom −0.015 is near-zero but not on a canon target.

---

## LEDGER — canon-forced vs derived vs inherited

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | tent law `T_a(y)=k_a·ℓ(1−ℓ/√(ℓ²+4y²))` | **INHERITED** (#527) | imported, not reimplemented |
| 2 | ⟨sin²⟩ = ½ | **DERIVED** (sympy) | `symbolic_backbone`, exact-zero |
| 3 | ⟨T⟩ = (k_a/ℓ)y₀² | **DERIVED** (from 1,2) | leading time-average |
| 4 | exact cycle-average (numeric) | **DERIVED** | quadrature over the #527 exact tent law |
| 5 | in-regime bow `in_regime_pluck_bow(arc*)` | **INHERITED** (#527) | fixed-arc premise ceiling |
| 6 | remap `k_shear_eff=S_shear+T/ℓ`, ρ'=S_ax/k_shear_eff | **INHERITED** (#526) | imported |
| 7 | A1 op-point A=√α | **READ-OFF** (Class-C echo) | def-vyvsn1; never tuned |
| 8 | matched-line Γ=0 (clm-mfb2ax) | **INHERITED** (#525) | `cascade_gamma`, imported |
| 9 | radiation control (i)→0 / (ii)→law | **DERIVED** | the make-or-break discriminator |
| 10 | matter ρ'/ν VALUES | **GR-IMPORTED** (via #526) | EMERGENCE grade FORBIDDEN |

---

## SECTOR / CLASS (as run)

- **SECTOR:** the MECHANICAL transverse bow DOF (the #527 arm-(a) tent response). **T2 HOMONYM GUARD
  binding (cite #527):** the static Cosserat winding carries NO real power
  (`resonant-lc-solitons.md`:128) and is NOT the plucker; the resonance is the mechanical bow, never
  re-welded to the winding. mass=A1; charge=Cosserat-winding; bow=T2-mechanical-response.
- **MODE:** cycle-averaged quasi-static about the resonant Q-point; **timescale-separation assumed**
  (resonance period ≪ tensor-probe timescale), so the tensor sees ⟨T⟩ not T(t).
- **CLASS (consistency-vs-emergence):** **CONSISTENCY / MANIFESTATION.** The resonant-tension law is
  an Ax4-microfoundation manifestation (tent law is #527-canon; the ⟨·⟩ is a time-average). The
  matter-track VALUES inherit #526's GR-imported 9.7734 status — **EMERGENCE grade FORBIDDEN.** α
  enters only via A=√α (Class-C echo).
- **AC/DC carve (clm-acdc07):** Part-1 ⟨T⟩ + matter re-band = **DC-internal** (a DC-bias operating
  point; the hum sets a DC ⟨y²⟩ that biases the #526 ratio). Part-2 = the **DC→AC boundary**
  statement: a traveling AC wave deposits no DC bias; a confined AC standing mode does. The
  falsifiable content is the ASYMMETRY (i)=0 while (ii)≠0 — confirmed.

---

## FLAGS SURFACED (flag-don't-fix)

1. **The ρ'=9.7734 y₀→0 endpoint is a T→0 identity, not a landing** — flagged for the auditor lane
   so the coincidence-discipline reviewer does not mis-read the re-band as chording on 9.7734.
2. **Leading law over-predicts by up to +36% at the elastica edge** — the matter-track ρ' band edge
   (4.36) is on the leading law's over-cap side; the exact-law band (4.36 lower, since exact caps
   less) is the reportable one. The two-law spread IS the honest magnitude uncertainty; the ⟨T⟩
   MAGNITUDE is δ_y-knob-ridden (inherits #526's normalization fork) — per the prereg robustness
   ladder, the FORM-end result (the carrier resolution) is what stands, not the six-digit magnitude.
3. **The matched-line (i)→0 is canon-FORCED, not novel evidence** — it is the required #518 §7 /
   clm-clvchn consistency pass; the AVE-distinct content is the ASYMMETRY (matter stiffens, radiation
   does not), which is Grant's hypothesis, now discriminator-confirmed.

---

## COROLLARY FOR THE CORPUS (auditor lands the manual; implementer surfaces)

🔴 FALSIFIED corollary (preserved): "The plucking-mechanism fork left OPEN by #527 is RESOLVED…"
It is NOT resolved. The carrier DIED (§HONEST RE-RUN). The correct corollary is below.

The plucking-mechanism fork left OPEN by #527 is RESOLVED: the matter arm's carrier is the confined
resonance (the resonant LC tank's own hum), and the magnitude-law noun for the matter arm is the
time-averaged resonant law `⟨T⟩=(k_a/ℓ)y₀²` (leading), banded by the exact cycle-average. This is a
CONSISTENCY-class resolution — it should be recorded against `resonant-lc-solitons.md` (the LC-tank
canon) and the #527 result doc's OPEN-fork note. **The auditor lane lands the KB/manuscript entry; I
surface the finding here.**

</details>

---

## HONEST COROLLARY FOR THE CORPUS (the live one; auditor lands the manual)

The plucking-mechanism fork left OPEN by #527 is **NOT resolved by this arc** — the resonant-tension
carrier as formulated is **[RADIATION-CONTAMINATED]** and DIES (Rule 11). The Part-1 law
`⟨T⟩=(k_a/ℓ)y0²` is real and derived, but it stiffens a matched CW traveling wave identically to the
confined hum, so it cannot serve as the matter/radiation discriminator (contradicts #518 §7). What
should be recorded: the #527 OPEN plucking-fork remains OPEN; the "auto-resonance ⟨T⟩ IS the bias"
noun is falsified as a discriminator at the per-bond scalar-tension level. **Pointer only (no new
adjudication):** canon's #518 §7 null rests on CHANNEL SYMMETRY (S_axial=S_shear under the traveling
wave) + the pump null, NOT on zero tension — so the viable discriminator, if any, is
**channel-RESOLVED** (does the traveling wave tension both channels symmetrically while the confined
hum tensions shear asymmetrically?). That is a NEW prereg for a future arc. **The auditor lane lands
the KB/manuscript entry against `resonant-lc-solitons.md` + the #527 result-doc OPEN-fork note; I
surface the honest negative here.**
