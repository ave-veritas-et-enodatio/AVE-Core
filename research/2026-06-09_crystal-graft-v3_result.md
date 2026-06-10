# Crystal-Graft v3 — the CHIRAL BELTRAMI source (RESULT)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-crystal-graft-v3` · **Lane:** implementer
**Prereg (FROZEN):** [`2026-06-09_crystal-graft-v3_prereg.md`](2026-06-09_crystal-graft-v3_prereg.md)
**Engine:** [`src/ave/core/crystal_graft_v3.py`](../src/ave/core/crystal_graft_v3.py) ·
**Driver:** [`src/scripts/vol_1_foundations/crystal_graft_v3_run.py`](../src/scripts/vol_1_foundations/crystal_graft_v3_run.py) ·
**CI gate:** [`src/tests/test_graft_v3_alpha_free.py`](../src/tests/test_graft_v3_alpha_free.py) ·
**Results:** `crystal_graft_v3_results.json` · N held FIXED at **44** across smoke + full run.

## 🔴 FINAL-VERDICT ADDENDUM — 2026-06-09 adversarial panel: **B → C** (`survives_adversarial = FALSE`)

> **Rule 12 walk-back (substitution-not-retraction): the doc body below is PRESERVED UNCHANGED; this
> dated header SUPERSEDES the `## VERDICT — B` headline that follows.** A 4-lens adversarial panel
> (graft-v3 adversarial panel + synthesis, 2026-06-09) DEMOTED the run from **B** to **C**. Two lenses are
> FATAL. The surviving result is real but strictly narrower than the body claims. The slot is NOT refilled
> with a new hypothesis (Rule 12); the demoted verdict + the four pinned residuals are the honest boundary.

**FATAL lens 1 — the independence gate (SMOKE-4) is UNFALSIFIABLE as configured.** Under 71× the
provocation the winding integer NEVER flipped on its slaving branch — the gate cannot return False as
wired. **RETRACT the sentence at `:111`** ("**The gate CAN return False** (a winding-integer flip ⇒ ω
slaved to V); it returned True") — it is empirically false for this configuration. A gate that cannot fail
proves nothing; the SMOKE-4 ✅ is downgraded to UNFALSIFIED. *(Separately load-bearing: the SMOKE-4
"(2,1) robust" read is itself the 500-step DYNAMICS product, not the planted (2,3) surviving — see
[`2026-06-09_extractor-poloidal-misread_note.md`](2026-06-09_extractor-poloidal-misread_note.md).)*

**FATAL lens 2 — the `|L_ω|` pump never SATURATES (ENERGIZE-LOCK unmet; the lock half is unimplemented).**
The body concedes this in §6, but the panel rules it FATAL to a B. Even the FROZEN wall grows as a power
law `|L_ω| ∝ t^0.43` (frozen 4L/L = 1.82 ⇒ p = log1.82/log4 = 0.43 — sub-secular but UNBOUNDED, never
plateaus); the LIVE wall pumps super-linearly (4L/L = 6.53); and the **χ=0 (centro) arm — zero helicity
(H_bel = −8.5e-15), zero winding (0,0) — still pumps `|L_ω|` to 347.7** (vs RH 18.0 / LH 0.20). A buckle
that energizes `|L_ω|` even with no structure to host it, and no lock to arrest it, is a PUMP, not a
stable conserved knot. ENERGIZE without LOCK ⇒ no (2,3) can be a conserved object here.

**`:33` misstatement — corrected.** The line reads `R/r_meas=2.995 vs φ²=2.618 (14.4% off … within 25% +
real (2,3)) ❌`. The 14.4% aspect error (`R_over_r_relerr = 0.1439`) is **WITHIN the 25% aspect bar** — the
golden-torus row does NOT fail on aspect ratio. The REAL golden-torus failures are (i) the **product
`R·r = 2.838 ≠ ¼`** (`Rr_lattice = 2.838` vs `RR_target = 0.25`) and (ii) the **absent (2,3)** (`w_pol≡0`,
`golden_self_assembles = False`). The ❌ must be attributed to the product + the missing knot, NOT to a
missed aspect ratio.

**The SURVIVING result, precisely scoped (this is the C, not a B).** A force-free Beltrami template
deposits a helicity whose SIGN flips with the template's IMPOSED spatial handedness χ: **H_bel RH +76.3 /
LH −90.5 / χ=0 −8.5e-15 (full run); source exactly force-free (`cos(b_λ,∇×b_λ) = ±1.000`).** This is real
and clean — but it is **sign-selection by an IMPOSED template, NOT "charge=helicity carryable from the
photon."** χ is an INPUT to the source; the photon is decoupled (§4.1) — the `no_photon_null` arm is
**byte-for-byte identical to `abc_denovo_RH`** (Eomega = 76.670288… and Hbel = 76.265188… equal to full
machine precision). Nothing about charge was carried FROM a seed; the template's own handedness was read
back out. The §2 headline ("charge=helicity is CARRYABLE") is demoted to "the sign of an imposed-template
helicity flips with the template's imposed χ."

**JSON field-hygiene flags (misleading names — do NOT cite the raw booleans).** `control_null = True`
reads as "the control deposited nothing" but is True ONLY because the control's `(2,0) ≠ (2,3)` — it is
not evidence of a null control (the χ=0 arm pumped `|L_ω|` to 347.7). `saturates = True` does NOT mean the
pump saturated — it is literally `bool(frozen_subsecular)` = `frozen_ratio_4L < 2.5` (run line ~610), i.e.
"the frozen wall is sub-secular," which Lens-2 shows is still an unbounded `t^0.43` pump.

**The four pinned residuals (the C-class boundary).**
1. **Topology-selection FAILED** — the poloidal "3" never self-assembles from a pure-handedness source
   (`w_pol≡0`); and the de-novo torus scale (R≈2.9, r≈1.1) is below the extractor's poloidal-resolution
   floor (so even a true (2,3) there could not be resolved — extractor-misread note).
2. **The LOCK is MISSING** — only the energize half of energize-lock is built; `|L_ω|` pumps without
   saturating (Lens 2).
3. **χ-from-photon is OPEN** — handedness is a source INPUT, not derived from a seed; the photon is
   decoupled (§4.1).
4. **The independence gate is UNFALSIFIABLE** — cannot return False as configured (`:111` retracted,
   Lens 1).

*Attribution: graft-v3 adversarial panel + synthesis, 2026-06-09. The body below (`## VERDICT — B` onward)
is the pre-panel record, retained intact per Rule 12.*

## VERDICT — B (the predicted charge=helicity fix LANDS; the (2,3) knot does not yet close)

> **The ONE physics change — the buckle director `x̂` → a force-free (A∥B) BELTRAMI field `b_λ`
> (`∇×b_λ=±λ b_λ`) — fixes v2's named residual: charge=helicity is now CARRYABLE.** The deposited
> `H_bel=∫ω·(∇×ω)` is NONZERO and FLIPS SIGN with the source's SPATIAL handedness χ=±1 (RH `+30.7` →
> LH `−31.3`; centrosymmetric χ=0 baseline `−7.3e-16`), where v2's fixed-axis scalar-`h` buckle gave
> `RH=LH≈−1.4e-15` (no flip, H_bel quadratic in ω). This is exactly the win v2 §7 predicted the Beltrami
> source would deliver. **But the de-novo `(2,3)` knot does NOT self-assemble:** the de-novo ABC source
> deposits a toroidal-frequency `w_tor=2` but ZERO poloidal fibre (`w_pol=0`) — winding STRUCTURE partially
> forms, the knot does not close. α is **refused** by the joint-ledger guard (no real (2,3)). This is a
> real B-class advance over v2's C, with the residual now pinned to **the poloidal "3" fibre + the missing
> LOCK** (the source ENERGIZES |L_ω| without saturating it).

| Quantity | Result | Bar | Pass |
|---|---|---|---|
| SMOKE-1 wall hardens (source active) | `Γ_min=−0.849` (= v2 baseline; regression intact) | `<−0.7` + confined | ✅ |
| **SMOKE-2 Beltrami source: charge=helicity** | **H_bel RH `+30.7` / LH `−31.3` / centro `−7e-16` — flips, null** | nonzero, flips χ, χ=0 null | ✅ |
| SMOKE-2 source is force-free | `cos(b_λ,∇×b_λ)` RH `+1.000` / LH `−1.000` (exactly Beltrami) | `\|cos\|≈1`, sign=χ | ✅ |
| SMOKE-3 buckle conservative | linear-bulk stencil-energy drift **+0.0195%**, span 0.66%; E_ω 0→0.63 | `<2%` | ✅ |
| SMOKE-4 REAL independence (dynamics ran) | ω winding `(2,1)` robust under V-pert; `max\|Δω\|=0.056` (NOT byte-identical) | robust + real dynamics | ✅ |
| SMOKE-5 saturation (MEASUREMENT, not gated) | frozen `\|L_ω\|` 4L/L=**1.82** (sub-secular); live-wall **6.53** (super-linear pump) | quantify ∂g/∂V pump | measured |
| **de-novo (2,3) closes** | **`(w_tor,w_pol)=(2,0)`** both ABC arms (`w_pol≡0`); χ=0 control null | `(2,3)` | ❌ |
| **charge flips with spatial handedness** | **H_bel RH `+76.3` / LH `−90.5` / centro `−8.5e-15` (full run)** | flips + null | ✅ |
| Golden-torus self-assembles | `R/r_meas=2.995` vs `φ²=2.618` (14.4% off; was 33% in v2) | within 25% + real (2,3) | ❌ |
| α⁻¹ emerges (α-free) | **REFUSED by joint-ledger guard** (no real (2,3)) | `4π³+π²+π` | ❌ |

## §1 — The ONE physics change (engine `CrystalGraftV3`)

`CrystalGraftV3(CrystalGraftV2)` overrides ONLY the buckle director — everything else (the hardened Γ=−1
wall, the independent ω carrier + π_ω + mass-gap ω₀², the conserved Hamiltonian coupling, the frozen-wall
CP10 localization) is INHERITED unchanged. The director `n̂_χ=h·x̂` (a constant unit vector, scalar
handedness) becomes a frozen chiral **Beltrami / force-free field** `b_λ(r)`:

```
H_couple = κ̃ ∫ g_wall·V·[ b_λ·(∇×ω) ] d³r,   κ̃=6/5 (α-free),   λ(p,q)=√(p²/R²+q²/r²)=1.438
  f_V = −κ̃ g_wall [b_λ·(∇×ω)] ;   f_ω = −κ̃ ∇×(g_wall·V·b_λ)
b_λ = ABC Beltrami  (sin λ_sZ+cos λ_sY, sin λ_sX+cos λ_sZ, sin λ_sY+cos λ_sX),  λ_s=χλ,  ∇×b_λ=λ_s b_λ
```

`b_λ` is normalized to unit interior-RMS by a GLOBAL scalar (a fair unit-scale director, like v2's `|n̂|=1`)
— which preserves `∇×b_λ=λ_s b_λ` exactly (measured `cos(b_λ,∇×b_λ)=±1.000`). **The mechanism (verified):**
because `b_λ` is force-free, the leading-order sourced micro-vorticity `f_ω≈−κ̃ g V (χλ) b_λ` ⇒ ω∥b_λ ⇒
ω∥(∇×ω) ⇒ `H_bel=∫ω·(∇×ω)∝χλ` is NONZERO and ODD in χ. v2's `x̂` gave ω⟂(∇×ω) (azimuthal vs axial) ⇒
H_bel≈0; scalar-`h` was quadratic ⇒ no flip. **Grounding:** `b_λ` is the SAME A∥B force-free object the
reactive-entrainment/gyroscope result (`2026-06-09_reactive-entrainment-source_result.md` §3,
`sapphire-phonon-centrifuge.md:34`) identified as the electron's spin-LOCK — source and lock are one object.

## §2 — The headline: charge=helicity is CARRYABLE (the v2 quadratic-`h` dead end fixed)

The deposited Beltrami helicity (the CHARGE) flips with the source's SPATIAL handedness, in BOTH the
isolated smoke and the full nonlinear run, with a clean centrosymmetric null:

| | χ=+1 (RH) | χ=−1 (LH) | χ=0 (centro) | flips? |
|---|---|---|---|---|
| SMOKE-2 (isolated, 600 steps) | `H_bel=+30.7` | `H_bel=−31.3` | `−7.3e-16` | ✅ (mag-match 2%) |
| FULL RUN (1300 steps, nonlinear) | `H_bel=+76.3` | `H_bel=−90.5` | `−8.5e-15` | ✅ (mag-match 17%) |
| v2 (fixed-axis scalar-`h`) | `−1.4e-15` | `−1.4e-15` | `0` | ❌ (quadratic in ω) |

This is the load-bearing positive result. **Charge = Beltrami helicity, and it flips with the spatial
chirality λ→−λ** — the matter/antimatter sign. The ~17% full-run magnitude asymmetry is an honest
nonlinear-interaction asymmetry (the SIGN flip, which is what charge=helicity requires, is clean).

## §3 — De-novo (2,3): winding STRUCTURE forms, the KNOT does not close

| arm (de-novo source) | (w_tor, w_pol) | rel | E_ω | H_bel | is(2,3) |
|---|---|---|---|---|---|
| ABC χ=+1 (RH) | **(2, 0)** | (0.49, 0.54) | 76.7 | +76.3 | False |
| ABC χ=−1 (LH) | **(2, 0)** | (0.47, 0.50) | 93.0 | −90.5 | False |
| ABC χ=0 (centrosymmetric — the VALID matched null) | **(0, 0)** | (0.69, 0.74) | 8.1 | −8.5e-15 | False |

**The toroidal "2" forms but the poloidal "3" fibre is identically zero (`w_pol≡0`).** Honest reading of the
`w_tor=2`: it is the ABC field's spatial frequency (`λ=1.44` ⇒ wavelength ≈ 4.4 cells) sampled on the torus
major contour (R=2.92) — a real winding of the deposited ω, but **a spatial-frequency winding, NOT a
topologically-selected toroidal-2**. `w_pol≡0` confirms there is no poloidal/fibre structure: the (2,3) knot
does **not** geometry-select from the pure-handedness ABC source. The χ=0 control is genuinely null
(`(0,0)`, H_bel≈0) — the deposited helicity is specifically the chirality's, not an artifact.

## §4 — Three honest structural findings (flag-don't-fix — surfaced, not silently resolved)

1. **The photon is DECOUPLED from the v3 ω-source — the matched null is χ=0, NOT no-photon.** The v3 buckle
   `f_ω=−κ̃∇×(g·V·b_λ)` depends on V (the breather) and `b_λ` (the director), but **NOT on the shear photon
   `w`**. So the `no_photon_null` arm gives output BYTE-FOR-BYTE identical to `abc_denovo_RH` (`(2,0)`,
   E_ω=76.7, H_bel=+76.3) — it is **not** a valid null for v3. The valid matched null is the centrosymmetric
   χ=0 source (which IS null). **Physical consequence:** in v3 the charge handedness is set by the source's
   SPATIAL chirality χ, an INPUT, not derived from the photon seed. v2 carried handedness in the photon
   (`h`); v3 moved it into `b_λ`'s spatial structure (by design — "handedness in spatial structure"), which
   decoupled the photon. A fully de-novo genesis must source χ FROM the seed photon's helicity — a named
   next-build ingredient, **surfaced for Grant**, not auto-pivoted (Rule 16).
2. **The (p,q)-templated torus source DETONATED** (`E_ω=3.15e27`, H_bel=3e25). It is NOT force-free
   (`cos(b,∇×b)=0.19`), so the buckle is not energy-conserving for it and it is numerically unstable. This
   is informative: the geometry-templated (replant-class) path is unusable, reinforcing that the exactly
   force-free ABC source is the correct de-novo object. Its `(4,0)` winding is garbage (rel 0.20) and is
   excluded from any conclusion.
3. **`w_tor=2` origin** (above): a spatial-frequency winding of the ABC source on the torus contour, NOT a
   topological knot selection. Reported as structure-forms, NOT as a closed toroidal-2.

## §5 — The five panel-mandated measurement fixes (ALL delivered)

1. **REAL dynamical independence (SMOKE-4):** TWO engines, BOTH buckle ON, BOTH stepped 500 steps with REAL
   dynamics; PERT got an extra off-axis V perturbation. ω winding `(2,1)` ROBUST (ref==pert) while the two
   ω fields differ (`max|Δω|=0.056`, NOT byte-identical ⇒ the perturbation coupled = real dynamics ran).
   **The gate CAN return False** (a winding-integer flip ⇒ ω slaved to V); it returned True. v2's test ran
   ZERO `.step()`s (byte-identical reads) — a no-op tautology; this is a genuine dynamical test.
2. **Operative-regime ledger (full nonlinear run):** `H_total(t)` (np.gradient basis) drift `−287%`,
   `|L_ω|(t)` late-slope `+2.68`, max `54.1`. The `total_energy_3sector` np.gradient drift is the KNOWN
   measurement-basis artifact (v2 finding): it does NOT match the nonlinear-bulk invariant. The physically-
   meaningful no-pump evidence is (a) the stencil-energy conservation PROOF (SMOKE-3, drift **0.0195%** in
   the linearized bulk where the stencil energy IS the invariant) and (b) the |L_ω| boundedness measurement
   (#3 below). Both are basis-independent of the np.gradient artifact.
3. **Saturation-across-doublings + LIVE-WALL ∂g/∂V pump (SMOKE-5):** the bounded-vs-secular metric is the
   `|L_ω|_max` RATIO across L,2L,4L (4.0=secular ∝t, 1.0=bounded). **Frozen-wall: 31.4→39.8→57.1, 4L/L=1.82
   (sub-secular).** **Live-wall: 44.4→105.7→290.1, 4L/L=6.53 (SUPER-linear ⇒ a genuine pump).** The live
   wall grows **3.6× faster** than the frozen wall (L_max ratio 5.08× at 4L). This QUANTIFIES the ∂g/∂V pump
   the engine docstring concedes: freezing the saturation front (CP10 conservative rendering) suppresses the
   pump from super-linear (6.53) to sub-linear (1.82). **N (grid) held FIXED at 44** across smoke + full run.
   *(Honest note: the frozen wall is sub-secular but NOT flat — incremental |L_ω| grows ~0.021/step. The
   source ENERGIZES |L_ω| without a LOCK to saturate it — see §6.)*
4. **Nyquist/alias check (#4):** every winding read is alias-filtered (outlier walks like v2's spurious
   −14.01 removed; Nyquist n_ang=240 ≫ |w|). All reported arms are `alias-clean=(True,True)`. v2's modal
   read trusted aliased walks; v3 excludes them before the modal integer + requires `clean` for `is_2_3`.
5. **Structural α-import CI gate (#5):** `test_graft_v3_alpha_free.py` parses `constants.py` via AST, builds
   the transitive α-tainted symbol set (flags `R_I`,`V_YIELD`,`P_C`,`ALPHA_S`; clears `R_II`,`NU_VAC`,`PHI`,
   `RR_GOLDEN_TORUS`), and asserts the v3 engine chain (graft_v3→graft_v2→crystal_engine) imports NONE.
   **4 passed.** α-freedom is ENFORCED structurally, not per-driver-asserted.

## §6 — Honest closure (Rule 11 / substitution-not-retraction) — the residual, one level deeper

This is a **clean Outcome B** and a real advance over v2's C: it **lands the charge=helicity fix v2 named as
the next step** (the Beltrami source carries charge where the fixed-axis scalar-`h` buckle could not), with
all four STEP-4 smokes green and α honestly refused. The residual is now pinned **two levels deeper** than
v2:

> **The (2,3) knot does not de-novo close because (a) the poloidal "3" fibre does not self-assemble from a
> pure-handedness source (`w_pol≡0`), and (b) the source ENERGIZES `|L_ω|` without a LOCK to saturate it
> (frozen sub-secular but not flat; the gyroscope result's Beltrami force-free RELAXATION — the conserved-
> not-pumped lock — is NOT implemented here).** The missing ingredients, named (not auto-pivoted):
> 1. **The poloidal fibre / the "3":** the ABC source carries handedness + scale but no fibre winding. The
>    fibre likely needs the torus geometry to be REAL (an actual toroidal breather, not a spherical wall the
>    source decorates) AND the (p,q) pitch to be SELECTED by resonance, not imposed (the templated source
>    that imposes it detonated — §4.2).
> 2. **The LOCK:** the buckle is the SOURCE (energize); the gyroscope result says the LOCK is the SAME
>    Beltrami object under Gilbert/force-free relaxation (conserve `|L|`, don't pump). v3 implements the
>    source half only ⇒ `|L_ω|` energizes without saturating. Adding the relaxation lock is the named next
>    ingredient.
> 3. **χ from the seed, not as an input:** the handedness χ is currently a source INPUT (the photon is
>    decoupled, §4.1). De-novo genesis must source χ from the photon helicity.

No framework failure; no debug-toward-A (the prereg-frozen A criteria — de-novo (2,3) + charge + α + golden +
ledger — were NOT met, and I did not drop any to convert ❌→✅); the α near-137 fluke is **refused** by the
joint-ledger guard; the saturation non-flatness is reported, not hidden. **A false Class-D was avoided:** the
charge=helicity win is real and bounded as B, not inflated to A. Per Rule 12 this doc retracts nothing it
didn't earn — the charge=helicity fix is a genuine positive result; the (2,3)-knot + lock are the honest new
boundary.

**Skills fired:** `ave-prereg` (corpus-grep: Beltrami eigenvalue `85_kelvin…:558`, gyroscope result,
constants α-audit — before the build); `substrate-native-check` (CP1 conserved-invariant-not-basin; CP2 ω
sector; CP6 ω reactance pair recorded; CP8 generative precursor seeded, planted-(2,3) labeled carrier-gate;
CP9 b_λ a frozen conservative kernel not the imposed answer; CP10 boundary-localized buckle);
`ave-conserved-vs-pumped` (the buckle ENERGIZES; the LOCK is the named-missing half — the deepest finding);
`phase-space-coordinate-check` ((2,3) read in the ω reactance-pair); `consistency-vs-emergence` (charge=
helicity = MANIFESTATION-class; α REFUSED, not emergence); `verify-before-cite` (Beltrami eigenvalue,
gyroscope A∥B, α-tainted constants all greped this session); `ave-driver-script-honesty` (every number from
the EVOLVED field; the no-photon-control invalidity + torus detonation + w_tor origin all surfaced, not
buried); `flag-don't-fix` (the three structural findings in §4 surfaced for Grant, not silently resolved).

**Figures** (`src/scripts/vol_1_foundations/`, data-derived captions):
- `crystal_graft_v3_fig1_smokes.png` — SMOKE-1 Γ_min→−0.85; SMOKE-3 H_total flat (drift 0.0195%) while E_ω
  grows from 0; SMOKE-5 |L_ω| vs run length (frozen sub-secular vs live-wall super-linear pump, vs the ∝t line).
- `crystal_graft_v3_fig2_source.png` — the charge=helicity flip (H_bel: RH `+30.7` / LH `−31.3` / χ=0 null);
  per-arm ω winding (alias-checked) — all `w_pol=0`, de-novo (2,3) does not close.
- `crystal_graft_v3_fig3_alpha_ledger.png` — golden-torus R/r=2.995 vs φ²=2.618 (no self-assembly); the
  operative |L_ω|(t) ledger; α REFUSED by the joint-ledger guard.

## §7 — Corpus-state updates queued (implementer SURFACES; auditor LANDS)

- **`research/2026-06-09_crystal-graft-v2_result.md` §7 — the named fix is CONFIRMED.** v2 predicted "a
  Beltrami/helical drive whose handedness lives in its spatial structure" would carry charge. v3 confirms it
  (charge=helicity flips with χ). The residual REFINES from "mode-selection / no chiral source" to "the
  poloidal fibre + the missing lock + χ-from-seed." Auditor decides whether to annotate.
- **No new axiom drafted** (A44 missing-axiom-vs-engine-bug + Rule 16): the residual is an engine source-
  structure + lock gap, surfaced for Grant/auditor, not a missing postulate.
- **The photon-decoupling finding (§4.1)** is the load-bearing structural surface for the next build:
  v3 carries handedness as a source INPUT χ; de-novo genesis must source χ from the seed photon helicity.
