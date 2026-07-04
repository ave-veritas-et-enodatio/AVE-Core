# RESULT — THE DC-BIAS PRE-STRESS DEFORMS THE ν(ρ_eff) MAP: [SAME-TENSOR-POINT] does NOT survive its first beyond-model test. [MAP-DEFORMED] on BOTH assignments

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `prestress-tensor-test`
**Driver:** `src/scripts/vol_1_foundations/prestress_elastic_tensor.py`
**Output:** `src/scripts/vol_1_foundations/_output/prestress_elastic_tensor.json` (driver-regenerable; gitignored)
**Test:** `src/tests/test_prestress_elastic_tensor.py` (13 pass)
**Prereg (FROZEN):** `research/2026-07-04_prestress-tensor_prereg_FROZEN.md` (committed BEFORE the driver)
**Stacks on:** PR #521 (MERGED) `research/2026-07-04_saturated-elastic-tensor_result.md`;
PR #518 (MERGED) `research/2026-07-04_matter-stiffening-rho_result.md`; cold family
`research/2026-07-04_srs-elastic-tensor_result.md`.

## VERDICT BOX

> **PRIMARY BIN: [MAP-DEFORMED]** on BOTH channel assignments (SHEAR-LOADS and AXIAL-LOADS).
>
> The DC-bias PRE-STRESS — the transverse "string-tension" force-constant `(T/ℓ)(I−d̂d̂ᵀ)` with
> `T=Φ'(A)` the integrated bond tension — **DEFORMS the ν(ρ_eff) map.** Under SHEAR-LOADS, at the
> ρ_eff=9.7734 matter crossing the Poisson ratio drops from **ν=2/7=0.285714 (the #521 no-prestress
> value) to ν=0.089407** (pole-free `|Δν/ν|=0.687` at the crossing; up to **1.045** elsewhere; the
> pole-free tensor SHAPE deviates by up to **0.999**). **[SAME-TENSOR-POINT] does NOT survive its
> first beyond-model test:** the saturated small-signal tensor is NOT the cold tensor at ρ_eff once
> the pre-stress the bias necessarily creates is included.
>
> **THE MECHANISM (proven, not asserted).** #521's [SAME-TENSOR-POINT] held because the Born-Huang
> map `(k_a,k_s)↦C_ij` is homogeneous of degree 1, so the dimensionless ratios are degree 0 and the
> overall S factor cancels. **The pre-stress term breaks that homogeneity.** `T=Φ'(A)` is a
> *different* function of A than the stiffness `Φ''=k0·S(A)`, so the total transverse force constant
> `k0·S(A_shear) + Φ'(A_axial)/ℓ` is not `λ·(k0·S)` for any single λ. The degree-1 homogeneity that
> made #521 hold is gone; the ratios no longer depend on ρ_eff alone — they pick up the pre-stress.
> (PC3 confirms: with T=0 the pipeline still reproduces #521's degree-1 homogeneity to 4×10⁻⁸, so the
> break is attributable to the pre-stress term, not a pipeline change.)
>
> **THE KNIFE HOLDS — no would-be-chord.** The ρ_eff=9.77 crossing amplitude stays at the free-knob
> `A_wall=0.99479` (pre-stress does not move ρ_eff, only the tensor at it), which is NOT
> canon-distinguished. The ν=2/7 crossing (K>0-gated, stable branch) MOVES from ρ_eff=9.7734 to
> **ρ_eff≈66.6** under pre-stress — *further* from any distinguished value, still a free knob.
> **KNIFE=False:** no shifted crossing lands on √α, 1−α, ½, ¼, or the yield wall. The deformation
> does NOT manufacture a chord; it destroys the #521 consistency finding.
>
> **CLASS unchanged:** this is a CONSISTENCY-class NEGATIVE (the #521 consistency finding is
> falsified beyond its model, not a value derivation lost). 9.7734 / 2/7 / K=2G stay GR-imported;
> the GR-import grade (PR#261) is UNTOUCHED. This result REMOVES a consistency finding, it does not
> add or subtract an emergence claim.
>
> **GEOMETRY-COUPLED NOT triggered — test 1 is well-posed at fixed geometry.** The srs z=3 site
> symmetry makes the bias bond tensions **self-balance at the cold geometry** (max residual node
> force 3.6×10⁻¹⁷, relative 4.2×10⁻¹⁶ — machine zero): the "pre-stressed at fixed geometry" state IS
> a mechanical equilibrium, so the small-signal tensor about it is well-defined. **Reading A**
> (prereg §9). Tests 1 and 2 are separable — the bias-geometry-change contribution (test 2 of 2)
> remains genuinely OPEN and is NOT collapsed into this test.

**All positive controls PASSED (HALT-gated).** PC1 zero-bias recovery: `A=0 ⟹ T=Φ'(0)=0 ⟹` the
pre-stress tensor = the cold/#521 tensor at ρ=9.7734 to **rel 0.0** (bit-exact, full-precision cold
reference on the SAME pipeline, gated 1×10⁻⁹). PC2 analytic stressed-lattice: uniformly-tensioned
simple-cubic `C44_stressed − C44_unstressed = T/ℓ` to **≤1.7×10⁻⁹** (validates the `(T/ℓ)(I−d̂d̂ᵀ)`
form on a closed-form case). PC3 homogeneity re-check: #521 degree-1 homogeneity recovered at T=0 to
**4.2×10⁻⁸**. Two-hand cross-validation ALL_AGREE (long-wave vs [100] direct eigensolve, ≤3×10⁻⁸).
Enantiomorph parity 3×10⁻¹⁶.

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** translational-u (Cauchy) sector of the ratified chiral srs-z3, on the **PRE-STRESSED**
  bond tensor. BOTH `k_a`, `k_s` are translational-u / **CAPACITIVE** springs (#518 verbatim).
  Cosserat = Stage 2, NOT invoked.
- **MODE:** SMALL-SIGNAL long-wave about a **PRE-STRESSED DC Q-point** — the reference bond tension
  `T=Φ'(A)≠0` (cold had `Φ'(0)=0`, the separating axis from #521).
- **REGIME:** quasi-static about a static DC bias. Op14 ON. **PHASE-STATE = saturated S<1 WITH bias
  tension.** Sub-yield interior; A→1 is the yield-wall limit.
- **DC-vs-AC:** A is a **static DC bias** (R2 varactor, `node-up-small-large-signal.md:118,:40,:145`)
  ⟹ **NO ⟨sin²⟩=½ time-average factor** — the reference tension is `Φ'(A)` at the static bias,
  factor 1 (derived from the corpus DC-bias convention, not hand-set).
- **COORDS (A46):** knob `(A_axial, A_shear)` in phase-space/reactance; tensor readout in
  real-space/spatial-Brillouin. Each in its own coordinate. A46-clean.
- **CLASS:** CONSISTENCY / MANIFESTATION. This is a consistency-class NEGATIVE (the #521 consistency
  finding is falsified beyond its model). EMERGENCE FORBIDDEN for any value; 2/7, 9.7734, 0.99479 are
  visible targets, none tuned toward (anti-tune ledger + frozen bins are the guard).

---

## 1. THE DERIVED BOND TENSION (the load-bearing input, no imports)

`Φ''(a) = k0·S(a) = k0·√(1−a²)` (Ax4 kernel AS DIFFERENTIAL STIFFNESS,
`src/ave/axioms/scale_invariant.py:107-156`; the tangent-stiffness reading #521/#518 already used
for the swapped springs). Direct integration with `Φ'(0)=0`:

> **T(A) = Φ'(A) = ∫₀ᴬ k0·√(1−a²) da = k0·( A·√(1−A²) + arcsin A ) / 2.**

**Symbolically verified this session** (sympy): the integral minus the closed form is exactly 0.
Key structural facts: `Φ'(0)=0` (cold reference un-tensioned); **`Φ'(1)=k0·π/4` — FINITE tension at
the yield wall** (the tangent stiffness `Φ''→0` there, but the integrated tension does not). The
time-average factor is **1** (DC bias, no oscillation to average — R2 varactor, not a standing wave).

**Cite chain (all grep-confirmed this session):** kernel `scale_invariant.py:107-156` +
docstring `:116-119`; kernel-as-differential-stiffness `saturated_elastic_tensor_result.md:71-72`;
DC-bias convention `node-up-small-large-signal.md:118,:40,:145`; integration derived + sympy-checked
(prereg §2, this doc §1).

---

## 2. THE INITIAL-STRESS ACOUSTIC TENSOR (Wallace / Born-Huang) — the pre-stress physics at lattice level

For a central-bond pair potential (Born & Huang Ch. V; Wallace initial-stress acoustic tensor), a
bond of natural length ℓ, direction `d̂`, tension `T=Φ'`, axial stiffness `Φ''`, carries:

> **Φ_bond = Φ''·(d̂⊗d̂) + (T/ℓ)·(I − d̂⊗d̂).**

The first term is the axial (swapped-spring softened) stiffness #521 already had. The **second term
`(T/ℓ)(I−d̂d̂ᵀ)` is the transverse "string-tension" rotational-stiffness term — THE PRE-STRESS
PHYSICS.** A bond at natural length (`T=0`) has no transverse restoring stiffness from it; a
pre-tensioned bond does (a taut string resists transverse plucking ∝ its tension). In the pipeline
the transverse block becomes `[k0·S(A_shear) + T/ℓ]·(I−P)`, with `ℓ = |d|` read per-bond from
geometry (`np.linalg.norm(d)`, `srs_primitive:293`) and `k0=1` (units into ρ, #521 convention). This
term is ADDITIVE and does NOT scale with the overall S — **that is what breaks the degree-1
homogeneity.**

**VALIDATED on a known case (PC2).** Uniformly-tensioned simple-cubic: the transverse acoustic speed
shift is analytic, `C44_stressed − C44_unstressed = T/ℓ` exactly. Measured to ≤1.7×10⁻⁹. The
`(T/ℓ)(I−d̂d̂ᵀ)` form is trusted BEFORE it is used on srs.

---

## 3. THE ν(ρ_eff) MAP SHIFT — both assignments (KEEP-BOTH, run blind)

The #521 no-prestress reference map is regenerated on the SAME pipeline (full-precision, T=0) at the
MATCHED ρ_eff; `Δν = ν_prestress − ν_#521` and the pole-free SHAPE deviation (`C11/C44, C12/C44,
Zener` — the #521 VS3 metric, valid even where ν diverges) are reported at every swept point.

**SHEAR-LOADS** (axial fixed sub-saturated at √α, S_axial=√(1−α)=0.996345; shear swept to A_wall).
The pre-stress T=Φ'(√α)=0.08532 is carried by the fixed axial channel (standard central-pair form:
each bond's OWN axial tension enters `(T/ℓ)(I−P)`):

| A_wall | ρ_eff | ν_prestress | ν_#521 | \|Δν/ν\| (pole-free) | SHAPE-dev | Zener_pre | sign(K) |
|---|---|---|---|---|---|---|---|
| 0 (loaded-cold) | 0.9963 | +15.363 | +342.09 | (ν pole) | 0.040 | 0.9894 | − |
| 0.5 | 1.1505 | −26.288 | −8.151 | (ν pole) | 0.052 | 1.0058 | − |
| 0.9 | 2.2858 | −1.1285 | −0.7012 | 0.610 | 0.224 | 1.0832 | − |
| 0.99 | 7.0629 | −0.00893 | +0.19831 | **1.045** | 0.939 | 1.1743 | + |
| **0.99479** (crossing) | **9.7733** | **+0.089407** | **+0.285714 = 2/7** | 0.687 | 0.796 | 1.1902 | + |
| 0.99999 | 222.79 | +0.31214 | +0.49086 | 0.364 | 0.967 | 1.2354 | + |

**AXIAL-LOADS** (mirror control: shear fixed at √α, axial swept to A_wall) — ρ_eff→0 (SOFTENING),
so ν is in its pole region at EVERY rung (`|ν_#521|>1` everywhere). The pole-free SHAPE metric is
what gives the honest verdict: **max SHAPE-dev = 0.441 ⟹ [MAP-DEFORMED].** (Reported the pole-free
metric explicitly because the ν-ratio metric alone would spuriously read null here — see §5 Rule-10.)

**Both assignments: [MAP-DEFORMED].** The map is not the cold map at ρ_eff once pre-stress enters.

---

## 4. THE KNIFE — the shifted crossing is NOT canon-distinguished ([MAP-DEFORMED] armed maximally)

| Test | Value | Canon-distinguished? |
|---|---|---|
| Crossing A_wall (ρ_eff=9.77, unchanged by pre-stress) | 0.99479 | — (free knob, = #518's) |
| Shifted ν=2/7 locus (K>0-gated, stable branch) | ρ_eff ≈ **66.6** | ✗ (further from 9.77) |
| Shifted locus = √α / 1−α / ½ / ¼ / yield? | no | ✗ |
| any clean ½/¼ over-determination? | none | ✗ |

**KNIFE=False.** The pre-stress does NOT move the ν=2/7 crossing ONTO any canon-distinguished
amplitude — it pushes it *away* (9.7734→66.6 in the stable branch), and 66.6 is a free knob. No
would-be-chord. The deformation is a clean falsification of the #521 consistency finding beyond its
model, NOT a chord discovery. (Skeptical framing applied per the frozen bin: had the shifted crossing
landed on a distinguished value, it would have required from-scratch re-derivation before any claim —
it did not land there.)

---

## 5. RULE-10 — running the imperfect driver early caught TWO readout defects (test bugs, not physics)

Per empirical-driver discipline, the driver ran before it was perfect and surfaced two ADJUDICATION-
metric defects; the physics (PC1/PC2/PC3, the homogeneity break) was right from the first run. Both
fixes were to the READOUT, never the tensor:

- **(i) AXIAL-LOADS spurious null.** The first cut reported `max|Δν/ν|=0.0` for AXIAL-LOADS — because
  ρ_eff<1 there keeps ν in its pole region (`|ν_#521|>1`) at every rung, and the ν-ratio tolerance
  test EXCLUDES the pole region, so the metric never updated. This is exactly the pole-region trap
  the prereg flagged. Fixed by adding the **pole-free SHAPE metric** (C11/C44, C12/C44, Zener — the
  #521 VS3 metric) as the deformation discriminator, valid everywhere. AXIAL-LOADS then reads
  SHAPE-dev 0.441 ⟹ [MAP-DEFORMED] honestly.
- **(ii) Two-hand crossval mislabel at near-iso-bond.** The [100] direct eigensolve read the acoustic
  eigenvalues by ascending-sort assuming `[C44, C44, C11]` (C11>C44), but at the near-iso-bond point
  the pre-stress pushes C44>C11, so the ascending order is `[C11, C44, C44]` — a 2% "disagreement"
  that was a branch-LABELING artifact, not a tensor error (lsq residual 5.9×10⁻⁸). Fixed with
  nearest-value branch matching (the duplicated transverse pair are the two closest eigenvalues; C11
  is the odd one out). Crossval then reads ALL_AGREE to ~10⁻⁸.
- **(iii) K>0-gated new-locus finder.** The raw ladder-crossing of ν=2/7 initially caught a K=0-pole
  sign-flip (ν:+∞→−∞) and reported a spurious locus at ρ_eff≈1.06 (where ν=39.7, K<0, NOT 2/7). The
  cold arc's discipline: ν diverges through the K=0 pole, so the crossing search MUST be K>0-gated
  (stable branch only). Fixed; the real stable-branch shifted locus is ρ_eff≈66.6.

---

## 6. KEEP-BOTH tension-form sensitivity (prereg §3) — the verdict is robust to the modeling fork

The standard central-pair-potential form uses each bond's OWN **axial** tension in `(T/ℓ)(I−P)`. The
KEEP-BOTH alternative uses the **channel** (near-yield swept) tension. At the SHEAR-LOADS crossing
(ρ_eff=9.7734):

| Tension form | T | ν | K | sign(K) | Zener | verdict |
|---|---|---|---|---|---|---|
| #521 no-prestress | 0 | +0.285714 = 2/7 | +0.458 | + | 1.2293 | (baseline) |
| standard (axial T) | 0.08532 | +0.089407 | +0.0366 | + | 1.1902 | DEFORMED |
| alt (channel/shear T) | 0.78504 | −9.987 | −0.0458 | **−** | 1.0147 | DEFORMED + DESTABILIZED |

**Both forms deform** (ν far off 2/7). The larger channel tension additionally flips K<0
(compound-recordable [DESTABILIZED]). The [MAP-DEFORMED] verdict is robust to the standard-vs-channel
fork; recorded, not silently picked.

---

## 7. BINS — per-assignment verdicts (frozen bins, NO fall-through else)

| Assignment | Primary bin | Basis |
|---|---|---|
| **SHEAR-LOADS** | **[MAP-DEFORMED]** | pole-free \|Δν/ν\| up to 1.045; SHAPE-dev up to 0.999; ν at ρ_eff=9.77 crossing = 0.0894 ≠ 2/7. KNIFE=False (shifted locus ρ_eff≈66.6, not canon-distinguished). |
| **AXIAL-LOADS** | **[MAP-DEFORMED]** | SHAPE-dev up to 0.441 (ν always in the pole region here; the pole-free metric is the honest discriminator). Mirror control confirms the deformation is assignment-independent in KIND. |

- **[GEOMETRY-COUPLED] NOT triggered:** residual node force 3.6×10⁻¹⁷ (relative 4.2×10⁻¹⁶) ⟹ reading
  A (self-balancing) ⟹ fixed-geometry pre-stress is well-posed; test 1 not collapsed into test 2.
- **[DESTABILIZED]** is a compound sub-finding under the channel-tension form (K<0 at the crossing),
  and K<0 persists below ρ_eff=2 as in #521 — reported, not the primary bin under the standard form.
- **[MAP-UNDEFORMED] is EMPTY.** The map IS deformed; [SAME-TENSOR-POINT] does not survive.

---

## 8. HONEST CLOSURE (Rule 11) — the pre-registered prediction failed decisively; one mechanism explains it

The #521 [SAME-TENSOR-POINT] rested on Born-Huang degree-1 homogeneity. The pre-stress term
`(T/ℓ)(I−d̂d̂ᵀ)`, with `T=Φ'(A)` a different function of A than the stiffness `k0·S(A)`, breaks that
homogeneity — a **single mechanism** that explains the deformation on BOTH assignments and under BOTH
tension forms. This is the discipline working: a clean CONSISTENCY-class negative, mechanism named,
branch closed. **No rescue attempted.** The #521 closure is correct *within its model* (swapped
springs at fixed geometry, pre-stress omitted); this test shows the model's first omitted
contribution (a) undoes the closure. [SAME-TENSOR-POINT] is now KNOWN to be model-bounded in the
strong sense: it fails the moment the DC bias's own pre-stress is included.

**Substitution-not-retraction note (Rule 12):** this does NOT refill the #521 slot with a new
hypothesis. It records that the #521 consistency finding does not extend past its model scope. Any
new claim (e.g., "the pre-stressed tensor has its own distinguished operating point") would be a new
version with its own verification chain — none is asserted here.

---

## 9. FALLOUT / AUDITOR-QUEUE (surfaced; implementer does NOT land manuals)

| Site | Proposed disposition |
|---|---|
| **#521 VERDICT BOX + § MODEL SCOPE** (`saturated-elastic-tensor_result.md:11-53`: "[SAME-TENSOR-POINT]... closes at the tensor level of this model") | **STRENGTHEN-THE-SCOPE (candidate):** the model bound is now SHARP. Contribution (a) initial/residual pre-stress is TESTED and it **DEFORMS** the map (ν 2/7→0.089 at the matter crossing). Add: "[SAME-TENSOR-POINT] does NOT survive beyond-model test 1 of 2 — the DC-bias pre-stress breaks the degree-1 homogeneity; provenance `prestress-tensor_result.md`." Contribution (b) geometry-change remains test 2, OPEN. |
| **#521 §7 SHEAR-LOADS [SAME-TENSOR-POINT] row** | **REFINE (candidate):** valid ONLY in the swapped-springs-at-fixed-geometry model; adding the bias pre-stress the same DC bias creates gives [MAP-DEFORMED]. |
| **The K=2G "GR-imported" grade** (PR#261, `k2g-crystalline-provenance_result.md`) | **UNTOUCHED / re-confirmed:** the pre-stress moves the ν=2/7 crossing to ρ_eff≈66.6, still a free knob; K=2G's GR-import grade stands, unaffected (this result removes a consistency finding, adds no value derivation). |
| **The floppy-near-yield picture** (`electron-bh-isomorphism.md:32`) | **CONSISTENT:** the pre-stress does not rescue the ratios — under the channel-tension form K flips negative (DESTABILIZED) near yield, consistent with topology-melts. No new claim. |
| **`node-up-small-large-signal.md` R2 varactor DC-bias convention** | **CROSS-LINK (candidate):** the DC-bias (not standing-wave) convention was the load-bearing input that set the time-average factor to 1; this arc uses it verbatim. |

**No rewrites performed.** Strengthen / refine / cross-link ROWS only; the auditor lane lands the
manual entries.

---

## 10. flag-don't-fix — surfaced, not resolved

1. **The tension-form modeling fork (SURFACED for Grant/auditor).** The standard central-pair-
   potential form puts each bond's OWN axial tension in the transverse `(T/ℓ)(I−P)` term; a channel-
   tension alternative puts the near-yield swept-channel tension there. **Both deform the map**
   (verdict robust), but they differ in magnitude and in whether K flips negative. Which is the
   physically correct pre-stress carrier on the srs bond is a Grant/auditor framing question — the
   verdict does not depend on it, but the *quantitative* deformation and the DESTABILIZED sub-finding
   do. Surfaced, not resolved. (KEEP-BOTH recorded, §6.)

2. **The Grant framing question (§9 of the prereg) — answered by the engine (Trigger-9 fork-to-
   computable).** "Is the bias tension a genuine fixed-geometry pre-stress, or does an unbalanced
   node force require geometry relaxation ([GEOMETRY-COUPLED])?" The residual-force discriminator
   answered **reading A** (self-balancing, residual 4×10⁻¹⁶) — the srs z=3 site symmetry cancels the
   uniform bias tensions at fixed geometry. **Still surfaced to Grant** for the framing gut-check:
   whether a machine-zero residual is EXPECTED PHYSICS (srs site symmetry) or worth a second look —
   the bin is engine-decided either way, but Grant's intuition on the site-symmetry cancellation is
   the framing input.

---

## Cross-references (verified at branch HEAD, grep-checked this session)

- Driver: `src/scripts/vol_1_foundations/prestress_elastic_tensor.py`
- Test: `src/tests/test_prestress_elastic_tensor.py` (13 pass)
- Prereg (FROZEN): `research/2026-07-04_prestress-tensor_prereg_FROZEN.md`
- #521 (MERGED): `research/2026-07-04_saturated-elastic-tensor_result.md` (VERDICT BOX + § MODEL
  SCOPE, the seam this test opens); driver `src/scripts/vol_1_foundations/saturated_elastic_tensor.py`
- #518 (MERGED): `research/2026-07-04_matter-stiffening-rho_result.md` (channel assignments)
- Cold family: `research/2026-07-04_srs-elastic-tensor_result.md` (ρ*=9.7734, K<0 for ρ<2)
- Kernel S(A) / differential stiffness: `src/ave/axioms/scale_invariant.py:107-156`
- DC-bias R2 varactor (time-average factor = 1): `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md:118,:40,:145`
- Parent condition ρ_bond=1 (clm-mfb2ax): `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parent-condition-match-forces-balance.md`
- Cold Born-Huang extraction (imported unmodified): `src/scripts/vol_1_foundations/srs_elastic_tensor.py`
- Carrier: `src/ave/core/chiral_lattice.py` `build_srs_net`
