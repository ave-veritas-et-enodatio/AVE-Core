# RESULT — THE DC-BIAS PRE-STRESS DEFORMS THE ν(ρ_eff) MAP: [SAME-TENSOR-POINT] does NOT survive its first beyond-model test. [MAP-DEFORMED] on BOTH assignments

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `prestress-tensor-test`
**Driver:** `src/scripts/vol_1_foundations/prestress_elastic_tensor.py`
**Output:** `src/scripts/vol_1_foundations/_output/prestress_elastic_tensor.json` (driver-regenerable; gitignored)
**Test:** `src/tests/test_prestress_elastic_tensor.py` (17 pass)
**Prereg (FROZEN):** `research/2026-07-04_prestress-tensor_prereg_FROZEN.md` (committed BEFORE the driver)
**Stacks on:** PR #521 (MERGED) `research/2026-07-04_saturated-elastic-tensor_result.md`;
PR #518 (MERGED) `research/2026-07-04_matter-stiffening-rho_result.md`; cold family
`research/2026-07-04_srs-elastic-tensor_result.md`.

> **⚠ INTERPRETATION REWRITE (2026-07-04, orchestrator 16-agent adversarial review, PR #526 fix
> round — 12 of 13 confirmations).** The BIN VERDICT [MAP-DEFORMED] is EARNED and reproduced by all
> three review lenses. But the review proved the FIRST mechanism narrative FALSE, the headline
> magnitudes calibration-dependent, and the sign of T un-adjudicated. The verdict letter STAYS; the
> interpretation below is the corrected one. Summary of what changed: (1) the tensor NEVER leaves the
> cold family — the pre-stress is a SHIFTED SHEAR SPRING (family survives, DICTIONARY breaks,
> coordinate CAPPED); (2) all magnitudes are now BANDS over the canon arc\* range (a δ_y
> normalization choice); (3) the sign of T is an OPEN Grant-fork (stretched-pair vs buckling-strut).

## VERDICT BOX

> **PRIMARY BIN: [MAP-DEFORMED]** on BOTH channel assignments (SHEAR-LOADS and AXIAL-LOADS). EARNED:
> the #521 map ties ν to the dictionary coordinate ρ_eff=S_ax/S_shear, and that TIE breaks under
> pre-stress. [SAME-TENSOR-POINT], as #521 defined it (ν=2/7 at ρ_eff=9.7734), does NOT survive its
> first beyond-model test.
>
> **THE CORRECTED MECHANISM (verifier-proved bit-exact).** The transverse string-tension term
> `(T/ℓ)(I−d̂d̂ᵀ)` has the **SAME PROJECTOR STRUCTURE** as the shear spring `k_s(I−P)`, so the
> pre-stressed force-constant matrix is **EXACTLY the cold matrix with a shifted shear spring**
> `k_s → k_s + T/ℓ`. On srs (uniform bond length ℓ=1) a single scalar shift works. Verified:
> `extract_prestress_Cij(k_a,k_s,T) == extract_cubic_Cij(k_a, k_s+T/ℓ)` to **≤8×10⁻¹⁶** at every
> probe point, both assignments (new **VS4 exact-collapse gate**). **The Born-Huang degree-1
> homogeneity is INTACT; the tensor NEVER leaves the cold one-parameter family.** (The first framing
> — "homogeneity broken, tensor leaves the family" — was FALSE; retracted.) **What breaks is ONLY
> #521's DICTIONARY** ρ_eff=S_ax/S_shear. The **true family coordinate** is
>
>     ρ' = S_ax / (S_shear + T/ℓ),
>
> monotone in the swept channel and **CAPPED**: as A_wall→1 (S_shear→0), ρ' → ρ'_max = S_ax·ℓ/T,
> **FINITE** — the yield wall no longer sends the coordinate to infinity. **FAMILY SURVIVES,
> DICTIONARY BREAKS, COORDINATE CAPPED.**
>
> **MAGNITUDES ARE BANDS (δ_y normalization, item 2).** `T=Φ'(A)` integrates over dimensionless
> amplitude; turning it into a force sets the yield-displacement δ_y=1 bond length — an
> **ENGINEERING/NORMALIZATION choice** (now a ledgered row, §7), not canon-forced. Over canon's Ax4
> arc\* band (`axiom-register.md:189`: 0.89–0.96 tent / ×0.79 elastica ⟹ δ_y∈[0.70, 0.96]):
> **ν at the crossing spans ≈0.098–0.151** (not the six-digit 0.089407); the **cap ρ'_max spans
> ≈12.2–16.7**. The **BINARY verdict is robust:** the map deforms past tolerance for any
> δ_y > ~1.5×10⁻⁴ — a **~4700× margin** below the physical δ_y. Six-digit headline numbers without
> the band are false precision.
>
> **THE SIGN IS AN OPEN GRANT-FORK (item 3).** This arm assumed the **stretched-pair** reading
> (T>0, taut string). Canon's Ax4 residual-content (`axiom-register.md:189`) reads the same kernel as
> a fixed-arc-length **BOWED STRUT (Euler buckling)**, whose end-to-end axial force is plausibly
> **COMPRESSIVE (T<0)**. T→−T gives **ν=+0.466 at the crossing** (RISES toward ½, not drops), and in
> the remap language T<0 **UNCAPS** the coordinate (k_s+T/ℓ→0 ⟹ ρ'→∞ at finite amplitude — the
> divergence direction). **The bin verdict survives either sign; the entire physical narrative
> inverts.** Both arms reported (§6.5); fork-resolution deferred to a buckling-microfoundation
> derivation. Flagged for Grant (§10).
>
> **THE KNIFE (re-aimed, item 5d) — no would-be-chord.** The crossing AMPLITUDE is analytically
> INVARIANT (pre-stress does not move ρ_eff), so testing it was testing a fixed quantity. Re-aimed at
> the MOVABLE quantities: (a) the cap ρ'_max = **11.68** (δ_y=1) / band 12.2–16.7, and (b) the ν=2/7
> locus in the OLD coordinate, **ρ_eff=59.93 by bisection** (the earlier 66.6 was a linear-
> interpolation artifact, item 4). **KNIFE=False:** neither lands on a canon-distinguished value.
> Soberly: **ρ'_max ≈ 1/√α to 0.24%** — but this is the **trivial small-A expansion** T≈k₀A at
> A=√α (§4), giving cap ≈ √(1−α)/√α, **NOT a new coincidence**; and 9.7734/cap = 0.8369 near 5/6 is a
> reported near-miss (noise, no chain produces it).
>
> **CLASS unchanged:** CONSISTENCY-class NEGATIVE (the #521 consistency finding falsified beyond its
> model; no value derivation lost). 9.7734 / 2/7 / K=2G stay GR-imported; the GR-import grade
> (PR#261) is UNTOUCHED.
>
> **GEOMETRY-COUPLED NOT triggered (internal DOFs) — test 1 well-posed.** The srs z=3 site symmetry
> self-balances the bias bond tensions at the cold geometry (residual node force 3.6×10⁻¹⁷, relative
> 4.2×10⁻¹⁶). **Reading A.** SCOPE (item 5g): this covers **INTERNAL node DOFs only**; the CELL virial
> under uniform tension is NONZERO (2.05, §6.6), clamped by the fixed cell — the A1-owned uniform
> dilation is exactly test 2's leading mode. Tests 1 and 2 are separable at the internal-DOF level;
> the cell-scale relaxation is deferred to test 2, honestly. The bias-geometry-change contribution
> (test 2 of 2) remains OPEN.

**All positive controls PASSED (HALT-gated), 17 tests pass.** PC1 zero-bias recovery: `A=0 ⟹ T=0 ⟹`
pre-stress tensor = cold/#521 tensor at ρ=9.7734 to **rel 0.0** (bit-exact, full-precision cold ref on
the SAME pipeline, gated 1×10⁻⁹). PC2 analytic stressed-lattice: `C44_stressed − C44_unstressed = T/ℓ`
to **≤1.7×10⁻⁹** (validates the `(T/ℓ)(I−d̂d̂ᵀ)` form; ℓ=1 disclosure, §2). PC3: #521 degree-1
homogeneity recovered at T=0 to **4.2×10⁻⁸**. **VS4 exact-collapse (NEW):** `prestress(k_a,k_s,T) ==
cold(k_a, k_s+T/ℓ)` to **≤8×10⁻¹⁶** — the corrected-mechanism gate. Two-hand cross-validation
ALL_AGREE (≤3×10⁻⁸); enantiomorph parity 3×10⁻¹⁶.

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
pre-tensioned bond does. In the pipeline the transverse block becomes `[k0·S(A_shear) + T/ℓ]·(I−P)`,
with `ℓ = |d|` read per-bond from geometry (`np.linalg.norm(d)`, `srs_primitive:293`) and `k0=1`
(units into ρ, `saturated_elastic_tensor.py:139` units convention).

> **CORRECTED MECHANISM (orchestrator review, retracting the first framing).** The first draft said
> this term "does NOT scale with S, so it BREAKS the degree-1 homogeneity and the ratios no longer
> depend on ρ_eff alone." **That is FALSE (verifier-proved bit-exact) and is retracted.** The
> `(T/ℓ)(I−d̂d̂ᵀ)` term has the **SAME PROJECTOR STRUCTURE** as the shear spring `k_s(I−P)`, so it
> does not add a new tensor structure — it just **adds a scalar to the shear spring:**
> `[k0·S(A_shear) + T/ℓ]·(I−P) = k_shear_eff·(I−P)`. On srs (uniform bond length ℓ=1) the whole
> pre-stressed matrix is therefore **EXACTLY the cold matrix with `k_s → k_s + T/ℓ`.** Verified
> (**VS4 gate**): `extract_prestress_Cij(k_a,k_s,T) == extract_cubic_Cij(k_a, k_s+T/ℓ)` to
> **≤8×10⁻¹⁶** at every probe point, both assignments. So the **Born-Huang degree-1 homogeneity is
> INTACT and the tensor NEVER leaves the cold one-parameter family.** What breaks is ONLY #521's
> DICTIONARY ρ_eff=S_ax/S_shear; the true family coordinate is **ρ' = S_ax/(S_shear + T/ℓ)**, capped
> at ρ'_max = S_ax·ℓ/T. (PC3 confirms the pipeline still gives #521's degree-1 homogeneity at T=0 to
> 4.2×10⁻⁸ — as it must, since T=0 is literally the cold pipeline.)

**VALIDATED on a known case (PC2).** Uniformly-tensioned simple-cubic: the transverse acoustic speed
shift is analytic, `C44_stressed − C44_unstressed = T/ℓ` exactly. Measured to ≤1.7×10⁻⁹. The
`(T/ℓ)(I−d̂d̂ᵀ)` form is trusted BEFORE it is used on srs. **Disclosure (item 5b):** PC2 runs only at
ℓ=1, where all powers of ℓ degenerate — so PC2 validates the `T/ℓ` FORM but does not independently
pin the ℓ-POWER; the ℓ¹ (string-tension) power is the standard Born-Huang/Wallace form. srs is also
ℓ=1, so no result number is affected.

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
so ν is in its pole region at EVERY rung (`|ν_#521|>1` everywhere). **Prereg-fidelity (item 5c):** the
FROZEN bin criterion is the ν-ratio match, and here it is **UNDEFINED** (0 pole-free points) — the
frozen metric alone yields NO verdict. The pole-free SHAPE metric (added post-freeze, explicitly
**POST-HOC supplementary**) is what gives the honest verdict: **max SHAPE-dev = 0.441 ⟹
[MAP-DEFORMED].** SHEAR-LOADS, by contrast, is [MAP-DEFORMED] on the **frozen ν-ratio metric itself**
(10 pole-free points, `|Δν/ν|` up to 1.045).

**Both assignments: [MAP-DEFORMED]** (SHEAR-LOADS on the frozen metric; AXIAL-LOADS on the post-hoc
SHAPE metric, frozen metric undefined). The #521 dictionary tie ν↔ρ_eff breaks once pre-stress enters.
**All magnitudes above are at δ_y=1; over the arc\* band δ_y∈[0.70,0.96] the crossing ν spans
≈0.098–0.151 (§7).**

---

## 4. THE KNIFE (re-aimed, item 5d) — the MOVABLE quantities land on NO canon-distinguished value

The crossing AMPLITUDE (A_wall=0.99479) is **analytically INVARIANT** — pre-stress does not move
ρ_eff, only the tensor at it — so testing it was testing a fixed quantity. The knife is re-aimed at
the quantities that DO move under pre-stress: the cap and the OLD-coordinate ν=2/7 locus.

| Test | Value (δ_y=1) | Canon-distinguished? |
|---|---|---|
| ν=2/7 locus, OLD coord, **bisected** (K>0-gated) | ρ_eff = **59.93** | ✗ (66.6 was a linear-interp artifact, item 4) |
| Cap ρ'_max = S_ax·ℓ/T | **11.68** (band 12.2–16.7) | ✗ (free knob; see below) |
| ρ'_max = √α / 1−α / ½ / ¼? | no | ✗ |
| 9.7734 / cap | 0.8369 vs 5/6=0.8333 | near-miss (0.4% off) — reported as NOISE |

**KNIFE=False** (`lands_on_canon_distinguished_value` = False). No movable quantity lands on a
canon-distinguished value. **Sober note on ρ'_max ≈ 1/√α (0.24%):** this is NOT a new coincidence —
it is the **trivial small-A expansion**. `T = Φ'(A) = (A√(1−A²)+arcsin A)/2 → A` as A→0, and at
A=√α the ratio T/A = 0.9988, so `cap = S_ax·ℓ/T ≈ √(1−α)/√α = 1/√α · √(1−α)` — the 1/√α is
mechanical, the ×√(1−α)≈0.9976 is the only content. Reported for completeness, weighted as noise
(no chain produces 9.7734/ρ'_max). The deformation is a clean falsification of the #521 **dictionary**
beyond its model, NOT a chord discovery.

---

## 5. RULE-10 — running the imperfect driver early caught TWO readout defects (test bugs, not physics)

Per empirical-driver discipline, the driver ran before it was perfect and surfaced ADJUDICATION-
metric defects; the physics (PC1/PC2/PC3/VS4, the shifted-shear-spring collapse) was right from the
first run. The fixes were to the READOUT, never the tensor:

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
- **(iii) K>0-gated new-locus finder + BISECTION (item 4).** The raw ladder-crossing of ν=2/7 first
  caught a K=0-pole sign-flip (ν:+∞→−∞) and reported a spurious locus at ρ_eff≈1.06 (ν=39.7, K<0). ν
  diverges through the K=0 pole, so the search MUST be K>0-gated. And linear interpolation on the
  sparse ladder gave 66.6; the correct **bisected** stable-branch locus is **ρ_eff=59.93** (item 4).
- **(iv) MECHANISM (the orchestrator's central finding).** The first run's PHYSICS narrative
  ("homogeneity broken, tensor leaves the cold family") was wrong — see §2. VS4 (exact-collapse)
  now gates the corrected mechanism (shifted shear spring, family intact) at ≤8×10⁻¹⁶.

---

## 6. KEEP-BOTH tension-form sensitivity (prereg §3) — the verdict is robust to the modeling fork

The standard central-pair-potential form uses each bond's OWN **axial** tension in `(T/ℓ)(I−P)`. The
KEEP-BOTH alternative uses the **channel** (near-yield swept) tension. At the SHEAR-LOADS crossing
(ρ_eff=9.7734, δ_y=1):

| Tension form | T | ν | K | sign(K) | Zener | ρ' remap |
|---|---|---|---|---|---|---|
| #521 no-prestress | 0 | +0.285714 = 2/7 | +0.458 | + | 1.2293 | ρ'=ρ_eff=9.77 |
| standard (axial T) | 0.08532 | +0.089407 | +0.0366 | + | 1.1902 | ρ'=5.32 (capped) |
| alt (channel/shear T) | 0.78504 | −9.987 | −0.0458 | **−** | 1.0147 | ρ'=1.123 |

**Both forms deform the #521 dictionary.** The alt/channel form's K<0 (ν=−9.987) is **NOT new
instability** — it is the **pre-existing cold K<0-for-ρ<2 region reached via the remap** (ρ'=1.123 is
inside the cold unstable band; cold ν at ρ'=1.1233 = −9.9872 vs the pre-stressed −9.9874, agreeing).

**KEEP-BOTH does NOT bracket a different carrier (item 5a).** Both forms feed the SAME transverse
`(I−P)` string slot — they differ only in the SCALAR T magnitude, not in the force-constant STRUCTURE.
A genuinely different pre-stress carrier would need an **off-`(I−P)` projector** — e.g. an
axial-stretch-stiffening contribution to the `d̂d̂ᵀ` block, or a Cosserat couple-stress bending term
(Stage 2). Such a carrier could leave the cold family (break VS4); untested here (Cauchy-only,
fixed-geometry scope).

### 6.5 THE SIGN FORK — an OPEN Grant-fork (item 3), both arms reported, NOT resolved

This arm assumed the **stretched-pair** reading (T>0, taut string, pair-potential `Φ'(A)` analogy).
Canon's Ax4 residual-content (`axiom-register.md:189`) reads the same kernel as a fixed-arc-length
**BOWED STRUT (Euler buckling)** — whose end-to-end axial force is plausibly **COMPRESSIVE (T<0)**.
At the crossing (δ_y=1):

| Sign arm | T | ν at crossing | sign(K) | remap reading |
|---|---|---|---|---|
| T>0 (stretched pair, my assumed arm) | +0.08532 | **+0.0894** (DROPS below 2/7) | + | ρ'=5.32, cap FINITE at S_ax·ℓ/T |
| T<0 (compressive buckling strut, canon) | −0.08532 | **+0.4659** (RISES toward ½) | + | ρ'=59.93, coordinate **UNCAPPED** (k_s+T/ℓ→0 ⟹ ρ'→∞ at finite amplitude) |

**The bin verdict [MAP-DEFORMED] survives either sign; the entire physical narrative INVERTS.** With
T>0 the crossing ν drops and the coordinate is capped; with T<0 the crossing ν rises toward ½ and the
coordinate diverges. **Fork-resolution condition:** derive the **end-to-end axial force** of the
biased bond from the **buckling microfoundation** (fixed arc-length, `A²+S²=arc*²`, Euler-strut), NOT
the pair-potential analogy — the sign of that force decides the arm. Flagged for Grant (§10).

### 6.6 CELL-STRESS honesty (item 5g) — the residual check covers INTERNAL DOFs only

The GEOMETRY-COUPLED residual-force check (§1) covers **INTERNAL node DOFs**. The **cell virial** under
uniform bond tension is **NONZERO** (2.05, computed) — a uniform dilational stress **clamped by the
fixed cell geometry**. That uniform dilation/compression is **A1-owned and is exactly test 2's
(bias-geometry-change) leading mode** (central-pair form → pure dilation; channel form → + deviatoric).
So [GEOMETRY-COUPLED]=NOT-triggered is scoped to the internal DOFs; the cell-scale relaxation is
honestly **deferred to test 2**. This does not change test 1's fixed-geometry small-signal tensor (the
acoustic modes ride on the internal DOFs), but it makes the scope boundary exact.

---

## 7. BINS — per-assignment verdicts (frozen bins; FROZEN metric verbatim FIRST, item 5c)

| Assignment | Primary bin | FROZEN ν-ratio metric (verbatim) | SHAPE metric (post-hoc supp.) |
|---|---|---|---|
| **SHEAR-LOADS** | **[MAP-DEFORMED]** | **MAP-DEFORMED** on the frozen metric (10 pole-free points, \|Δν/ν\| up to 1.045; ν at crossing 0.089≠2/7) | SHAPE-dev up to 0.999 (corroborates) |
| **AXIAL-LOADS** | **[MAP-DEFORMED]** | **UNDEFINED** — 0 pole-free points (ν in the pole region at every rung); no verdict from the frozen metric alone | SHAPE-dev 0.441 ⟹ deformed (the ONLY basis here — explicitly post-hoc) |

- **KNIFE=False** (re-aimed at movable quantities): cap 11.68 / OLD-coord locus 59.93, neither
  canon-distinguished (§4). All numbers at δ_y=1; over the arc\* band the crossing ν spans 0.098–0.151.
- **[GEOMETRY-COUPLED] NOT triggered (internal DOFs):** residual node force 3.6×10⁻¹⁷ ⟹ reading A;
  cell-scale relaxation deferred to test 2 (§6.6).
- **[DESTABILIZED]** under the channel-tension / T<0 arm is the **pre-existing cold K<0-for-ρ<2 region
  via the remap** (§6), not new instability — reported, not the primary bin under the standard T>0 arm.
- **[MAP-UNDEFORMED] is EMPTY.** The #521 dictionary tie ν↔ρ_eff breaks.
- **NO fall-through else + reachable DISCREPANT-HALT (item 5e):** the bin selector fires a loud
  DISCREPANT-HALT if the map reads deformed yet VS4 exact-collapse FAILS (the tensor left the cold
  family) — the contradiction is caught, not silently binned (the #521-review dead-else defect fixed).

---

## 8. HONEST CLOSURE (Rule 11) — the pre-registered prediction failed decisively; one mechanism explains it

The #521 [SAME-TENSOR-POINT] tied ν=2/7 to the dictionary coordinate ρ_eff=S_ax/S_shear at 9.7734.
The pre-stress is a **shifted shear spring** `k_s → k_s + T/ℓ` (VS4, bit-exact) — the tensor stays in
the cold family, but the #521 **dictionary** breaks: the true coordinate is ρ'=S_ax/(S_shear+T/ℓ),
capped. This **single mechanism** — a coordinate remap, not a homogeneity break — explains the
deformation on BOTH assignments and BOTH tension forms. This is the discipline working: a clean
CONSISTENCY-class negative, mechanism named (and CORRECTED under adversarial review), branch closed.
**No rescue attempted.** The #521 closure is correct *within its model* (swapped springs at fixed
geometry, pre-stress omitted); this test shows the model's first omitted contribution (a) undoes the
**dictionary** — [SAME-TENSOR-POINT], as the ν=2/7-at-ρ_eff=9.7734 map, fails the moment the DC bias's
own pre-stress is included.

**Substitution-not-retraction note (Rule 12):** this does NOT refill the #521 slot with a new
hypothesis. It records that the #521 consistency finding does not extend past its model scope. Any
new claim (e.g., "the pre-stressed tensor has its own distinguished operating point") would be a new
version with its own verification chain — none is asserted here.

---

## 9. FALLOUT / AUDITOR-QUEUE (surfaced; implementer does NOT land manuals)

| Site | Proposed disposition |
|---|---|
| **#521 VERDICT BOX + § MODEL SCOPE** (`saturated-elastic-tensor_result.md:11-53`: "[SAME-TENSOR-POINT]... closes at the tensor level of this model") | **STRENGTHEN-THE-SCOPE (candidate):** the model bound is now SHARP. Contribution (a) initial/residual pre-stress is TESTED and it **DEFORMS the #521 dictionary** (ν 2/7→≈0.09–0.15 band at the matter crossing). Add: "[SAME-TENSOR-POINT] does NOT survive beyond-model test 1 of 2 — the DC-bias pre-stress is a shifted shear spring that remaps the coordinate (ρ'=S_ax/(S_shear+T/ℓ), capped); the tensor stays in the cold family but the ν=2/7-at-ρ_eff=9.7734 dictionary breaks; provenance `prestress-tensor_result.md`." Contribution (b) geometry-change remains test 2, OPEN. |
| **#521 §7 SHEAR-LOADS [SAME-TENSOR-POINT] row** | **REFINE (candidate):** valid ONLY in the swapped-springs-at-fixed-geometry model; adding the bias pre-stress the same DC bias creates remaps the coordinate ⟹ [MAP-DEFORMED]. |
| **The K=2G "GR-imported" grade** (PR#261, `k2g-crystalline-provenance_result.md`) | **UNTOUCHED / re-confirmed:** the ν=2/7 locus moves to the OLD-coord ρ_eff≈59.93 (still a free knob); the true-coordinate ν=2/7 point is ρ'=9.7734 at a shifted, still-free-knob amplitude. K=2G's GR-import grade stands (this result removes a consistency finding, adds no value derivation). |
| **The floppy-near-yield picture** (`electron-bh-isomorphism.md:32`) | **CONSISTENT:** the T<0 / channel arm's K<0 is the pre-existing cold K<0-for-ρ<2 region reached via the remap, not new instability — consistent with topology-melts. No new claim. |
| **`node-up-small-large-signal.md` R2 varactor DC-bias convention** | **CROSS-LINK (candidate):** the DC-bias (not standing-wave) convention was the load-bearing input that set the time-average factor to 1; this arc uses it verbatim. |

**No rewrites performed.** Strengthen / refine / cross-link ROWS only; the auditor lane lands the
manual entries.

---

## 10. flag-don't-fix — surfaced, not resolved

1. **THE SIGN FORK (item 3, the load-bearing Grant-fork).** This arm assumed T>0 (stretched pair).
   Canon's Ax4 residual-content (`axiom-register.md:189`) reads the kernel as a bowed-strut (Euler
   buckling), whose end-to-end axial force is plausibly **COMPRESSIVE (T<0)**. **The bin verdict
   survives either sign; the physical narrative inverts** (T>0: ν drops to ≈0.09, coordinate capped;
   T<0: ν rises to ≈0.47 toward ½, coordinate uncapped/diverges — §6.5). **Resolution condition:**
   derive the end-to-end axial force from the buckling microfoundation (fixed arc-length A²+S²=arc*²),
   not the pair-potential analogy. Surfaced, NOT resolved.

2. **THE δ_y NORMALIZATION (item 2, ledgered).** `T=Φ'(A)` integrates over dimensionless amplitude;
   making it a force sets the yield-displacement δ_y=1 bond length — an ENGINEERING/NORMALIZATION
   choice (now a ledger row, §11), not canon-forced. Every magnitude is a BAND over the arc\* range
   (ν crossing ≈0.098–0.151, cap ≈12.2–16.7); the BINARY verdict is robust for any δ_y>~1.5×10⁻⁴
   (~4700× margin). Which δ_y the srs bond actually carries is a Grant/auditor question (couples to
   the arc\* anchor); the verdict does not depend on it.

3. **The tension-form modeling fork.** Standard (bond's own axial tension) vs channel (swept-channel
   tension); both deform the #521 dictionary, both are the same `(I−P)` carrier (KEEP-BOTH does not
   bracket a different carrier — §6, item 5a). Which is physically correct is a Grant/auditor framing
   question; the verdict does not depend on it.

4. **The Grant framing question (prereg §9) — answered by the engine (reading A, internal DOFs).** The
   residual-force discriminator returned self-balancing (residual 4×10⁻¹⁶) for INTERNAL node DOFs; the
   CELL virial is nonzero and deferred to test 2 (§6.6). Surfaced to Grant: whether a machine-zero
   internal residual matches intuition for the srs z=3 site symmetry.

---

## 11. ANTI-TUNE / NORMALIZATION LEDGER (item 2 row added)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel `Φ''(a)=k0·√(1−a²)` | CANON-FORCED | Ax4, `scale_invariant.py:107-156` |
| 2 | Tension `Φ'(A)=k0(A√(1−A²)+arcsin A)/2` | DERIVED | direct integration, sympy-verified §1 |
| 3 | Time-average factor = 1 (no ⟨sin²⟩) | CANON-FORCED | DC-bias R2 varactor, `node-up:118,:40,:145` |
| 4 | Initial-stress form `(T/ℓ)(I−d̂d̂ᵀ)` | STANDARD (VS4/PC2) | Born-Huang/Wallace; = shifted shear spring on srs |
| **5** | **δ_y (yield displacement) = 1 bond length** | **ENGINEERING/NORMALIZATION-CHOICE (NEW ROW)** | **NOT canon-forced; canon arc\* band ⟹ δ_y∈[0.70,0.96] (`axiom-register.md:189`); all magnitudes reported as bands** |
| 6 | ℓ = per-bond `|d|` from geometry (=1 on srs) | READ-OFF (geometry) | `srs_primitive`; not hand-set |
| 7 | `k0=1` (units into ρ) | CANON-FORCED | `saturated_elastic_tensor.py:139` (cite fixed, item 5f) |
| 8 | Sign of T (stretched vs buckling) | **OPEN GRANT-FORK** | verdict survives either; narrative inverts (§6.5, §10.1) |
| 9 | ρ*=9.7734, ν=2/7, A_wall=0.99479 | GR-IMPORTED / READ-OFF | never inputs (anti-tune guard, test-locked) |

**0 free parameters tuned toward 2/7 / 9.7734 / 0.99479.** The δ_y normalization and the T-sign are
now explicit (a ledgered engineering choice and an open fork), not silent defaults.

---

## Cross-references (verified at branch HEAD, grep-checked this session)

- Driver: `src/scripts/vol_1_foundations/prestress_elastic_tensor.py`
- Test: `src/tests/test_prestress_elastic_tensor.py` (17 pass)
- Prereg (FROZEN): `research/2026-07-04_prestress-tensor_prereg_FROZEN.md`
- Ax4 residual-content (arc\* band + buckling-strut microfoundation): `manuscript/ave-kb/common/axiom-register.md:189`
- Units-into-ρ convention (cite fixed, item 5f): `src/scripts/vol_1_foundations/saturated_elastic_tensor.py:139`
- #521 (MERGED): `research/2026-07-04_saturated-elastic-tensor_result.md` (VERDICT BOX + § MODEL
  SCOPE, the seam this test opens); driver `src/scripts/vol_1_foundations/saturated_elastic_tensor.py`
- #518 (MERGED): `research/2026-07-04_matter-stiffening-rho_result.md` (channel assignments)
- Cold family: `research/2026-07-04_srs-elastic-tensor_result.md` (ρ*=9.7734, K<0 for ρ<2)
- Kernel S(A) / differential stiffness: `src/ave/axioms/scale_invariant.py:107-156`
- DC-bias R2 varactor (time-average factor = 1): `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md:118,:40,:145`
- Parent condition ρ_bond=1 (clm-mfb2ax): `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parent-condition-match-forces-balance.md`
- Cold Born-Huang extraction (imported unmodified): `src/scripts/vol_1_foundations/srs_elastic_tensor.py`
- Carrier: `src/ave/core/chiral_lattice.py` `build_srs_net`
