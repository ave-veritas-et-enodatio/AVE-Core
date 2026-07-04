# PREREG (FROZEN) — DOES THE DC-BIAS PRE-STRESS DEFORM THE ν(ρ_eff) MAP?

**[SAME-TENSOR-POINT] beyond-model test 1 of 2 — the initial/residual PRE-STRESS contribution**

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `prestress-tensor-test`
**Stacks on:** PR #521 (MERGED) `research/2026-07-04_saturated-elastic-tensor_result.md`;
PR #518 (MERGED) `research/2026-07-04_matter-stiffening-rho_result.md`;
cold family `research/2026-07-04_srs-elastic-tensor_result.md`.
**Driver (to be scaffolded AFTER this freeze):** `src/scripts/vol_1_foundations/prestress_elastic_tensor.py`
**Test:** `src/tests/test_prestress_elastic_tensor.py`
**Result:** `research/2026-07-04_prestress-tensor_result.md`

---

## 0. THE SEAM THIS OPENS — the #521 MODEL SCOPE block, verbatim

PR #521's VERDICT BOX names the closure as **model-bounded**. Its § MODEL SCOPE (verified verbatim,
`research/2026-07-04_saturated-elastic-tensor_result.md:28-34`):

> "A real DC-biased lattice can carry contributions this model OMITS: **(a) initial/residual stress**
> (the bias pre-loads the bonds → a nonzero reference stress that shifts the effective moduli beyond
> spring-softening), and **(b) bias-induced geometry change** (the operating point may relax the node
> positions / bond directions away from the cold geometry). Both are **OUT OF SCOPE here and remain
> OPEN.**"

**This arc computes contribution (a) ONLY** — the initial/residual PRE-STRESS. **Contribution (b)
(bias-induced geometry change) stays OUT OF SCOPE here** — geometry is held FIXED at the cold
reference; that is the follow-on arc (beyond-model test 2 of 2). This is stated so the auditor lane
can see the scope split.

The #521 closure was that the saturated small-signal tensor is the cold tensor at ρ_eff, because the
Born-Huang map `(k_a,k_s)↦C_ij` is homogeneous of degree 1 (the overall S factor cancels in every
dimensionless ratio; VS2 measured 4×10⁻⁸). **The pre-stress term is NOT a mere spring-softening**; it
adds a *new* force-constant structure (a transverse "string tension" `(T/ℓ)(I−d̂d̂ᵀ)` per bond) that
is NOT homogeneous-degree-1-compatible with the `k_axial·P + k_shear·(I−P)` swapped-springs form —
so the pre-stress term can, in principle, break the degree-1 homogeneity that made the #521 closure
hold. **That is exactly why this test is informative.**

---

## 1. SUBSTRATE-FIRST SECTOR HEADER (declared BEFORE any standard-physics term)

- **SECTOR:** translational-u (Cauchy) sector of the ratified chiral srs-z3, on the **PRE-STRESSED**
  bond tensor. BOTH `k_a` and `k_s` are translational-u / **CAPACITIVE** springs (axial STRETCH vs
  transverse SHEAR of the SAME bond; #518 verbatim) — NOT the ε-vs-μ photon pair. Cosserat
  couple-stress = Stage 2, NOT invoked.
- **MODE:** SMALL-SIGNAL long-wave about a **PRE-STRESSED DC Q-point**. The small-signal elastic
  response is read *about* an operating point that now carries a nonzero reference bond tension
  `T(A) = Φ'(A) ≠ 0` (the cold reference had `Φ'(0)=0`, zero tension — that is the separating axis
  from #521).
- **REGIME:** quasi-static about a **static DC bias**. Op14 saturation ON. **PHASE-STATE = saturated,
  S<1, WITH BIAS TENSION.** Sub-yield on the interior; A→1 is the yield-wall limit.
- **DC-vs-AC (resolves the time-average factor, see §3):** the operating point A is a **static DC
  bias** (R2 varactor picture, keyed on field amplitude V∼E), NOT the amplitude of an AC standing
  wave. Verified verbatim: `node-up-small-large-signal.md:118` — *"A DC bias is a real operating
  point"*; `:40` — *"the operating point 'analogous to DC bias on a semiconductor varactor'"*; the
  R2 row `:145` is the static-E route (`∂B/∂t=0`). **CONSEQUENCE: NO ⟨sin²⟩=½ time-average factor** —
  there is no oscillation to average over; the reference tension is `Φ'(A)` at the static bias A,
  factor = 1. This is derived from the corpus DC-bias convention, NOT hand-set (the factor question
  the task raised is answered by the substrate's own R2 varactor operating-point definition).
- **COORDS (A46):** operating-point knob `(A_axial, A_shear)` in **phase-space / reactance** (#518
  verbatim); tensor readout `ω(k)→C_ij→ν,Zener,K/G` in **real-space / spatial-Brillouin**. Each
  measured in its OWN matching coordinate. A46-clean on both axes.
- **CLASS (consistency-vs-emergence):** CONSISTENCY / MANIFESTATION. ν, Zener, K/G are α-clean
  dimensionless ratios (α enters only via the √α core amplitude, off the ratio verdict path).
  **EMERGENCE FORBIDDEN for any VALUE** — 2/7, 9.7734, 0.99479 are ALL visible targets; NO tuning
  toward any (the frozen bins + the anti-tune ledger are the guard). Whether pre-stress shifts the
  crossing ONTO a canon-distinguished amplitude is the maximally-armed knife (bin [MAP-DEFORMED]).

---

## 2. THE DERIVED BOND TENSION — from the kernel, no imports

**Given (Ax4 kernel as DIFFERENTIAL stiffness).** The bond potential has
`Φ''(a) = k0·S(a) = k0·√(1−a²)` — the Ax4 kernel `S(A)=√(1−A²)` is the DIFFERENTIAL (tangent) bond
stiffness (`scale_invariant.saturation_factor`; #521/#518 verbatim: "the saturated `k(A)=k0·S(A)` are
the differential (tangent) bond stiffnesses at the DC bias point"). This is the tangent-stiffness
reading of the same kernel #518/#521 used for the swapped springs `k_axial=S_axial`,
`k_shear=S_shear`.

**Derived tension (direct integration, `Φ'(0)=0`).** The bond TENSION at bias amplitude A is the
first integral of the differential stiffness:

    T(A) = Φ'(A) = ∫₀ᴬ k0·√(1−a²) da = k0·( A·√(1−A²) + arcsin A ) / 2.

**Symbolically verified** (sympy, this session): `∫₀ᴬ k0√(1−a²) da − k0(A√(1−A²)+arcsin A)/2 = 0`
exactly; numeric check `Φ'(0.5)=0.478306` on both forms. `Φ'(0)=0` (cold reference is un-tensioned);
`Φ'(A)→k0·π/4` as A→1 (finite tension at the yield wall — the differential stiffness → 0 but the
integrated tension stays finite). This is the KEY structural fact: **at the yield wall the bond has
ZERO tangent stiffness but MAXIMUM finite tension π/4·k0.**

**Per-channel (matching #518 channel assignments, both blind, KEEP-BOTH):**

- **SHEAR-LOADS** (def-vyvsn1-consistent, PRIMARY per #518): axial fixed sub-saturated at `A=√α`
  (`T_axial = Φ'(√α)`); shear swept to `A=A_wall` (`T_shear = Φ'(A_wall)`).
- **AXIAL-LOADS** (mirror control): shear fixed at `A=√α` (`T_shear = Φ'(√α)`); axial swept to
  `A=A_wall` (`T_axial = Φ'(A_wall)`).

Both channels' tensions are the SAME integrated kernel `Φ'` evaluated at each channel's own bias
amplitude. **No hand-set factor; no import.** The time-average factor is 1 by the DC-bias convention
(§1); if the driver-time analysis surfaces that the operating point is secretly an AC standing wave
(it is not, per §1), the ½ factor would enter — but the corpus R2 varactor definition freezes it at
static DC.

**Cite chain for the tension (verify-before-cite, all grep-confirmed this session):**
1. Kernel `Φ''(a)=k0·S(a)`, `S=√(1−a²)`: `src/ave/axioms/scale_invariant.py:107-156`
   (`saturation_factor`), docstring `:116-119`.
2. Kernel-as-differential-stiffness reading: #521 result `:71-72` ("the saturated `k(A)=k0·S(A)` are
   the **differential (tangent) bond stiffnesses at the DC bias point**"); Ax4 kernel
   `S(A)=√(1−A²)` is the DIFFERENTIAL stiffness factor (task CONTEXT, matches
   `scale_invariant.py` docstring).
3. Integration `Φ'(A)=k0(A√(1−A²)+arcsin A)/2`: derived here (§2), symbolically verified.
4. DC-bias (no ⟨sin²⟩ factor): `node-up-small-large-signal.md:118,:40,:145` (R2 varactor, static).

---

## 3. THE INITIAL-STRESS ACOUSTIC-TENSOR FORM — Wallace / Born-Huang for a pair-potential lattice

**The physics.** For a central-bond pair potential, the standard lattice-dynamics force-constant
matrix of a bond of natural length ℓ, direction `d̂`, carrying axial tension `T=Φ'` and axial
stiffness `Φ''`, is (Born & Huang, *Dynamical Theory of Crystal Lattices*, Ch. V; Wallace,
*Thermodynamics of Crystals* — the initial-stress acoustic tensor):

    Φ_bond = Φ''·(d̂⊗d̂)  +  (T/ℓ)·(I − d̂⊗d̂).

- The **first term** `Φ''·d̂d̂ᵀ` is the axial (longitudinal-stretch) stiffness — this is the `k_a·P`
  term the cold/#521 model already carries, with `Φ''=k0·S(A)` at the operating point (the
  swapped-spring softening).
- The **second term** `(T/ℓ)(I−d̂d̂ᵀ)` is the **transverse "string tension" / rotational-stiffness
  term** — the restoring force a taut bond exerts against TRANSVERSE (perpendicular) displacement,
  proportional to the axial tension T. **THIS IS THE PRE-STRESS PHYSICS at lattice level.** A bond at
  natural length (`T=0`, cold reference) has NO transverse restoring stiffness from this term; a
  pre-tensioned bond does (a guitar string resists transverse plucking in proportion to its tension).

**Mapping onto the #521 pipeline.** The #521/cold model already has a transverse block
`k_shear·(I−P)`. The pre-stress term ADDS to it:

    k_shear_effective = k_shear(A_shear)  +  (T_channel / ℓ),

i.e. the transverse block becomes `[k_shear·S(A_shear) + T/ℓ]·(I−P)`. **CRITICAL STRUCTURAL POINT:**
this term is ADDITIVE and does NOT scale with the same overall factor as the swapped springs — the
tension `T=Φ'(A)` is a DIFFERENT function of A than the stiffness `Φ''=k0·S(A)`. So the total
transverse stiffness is `k0·S(A_shear) + Φ'(A_channel)/ℓ`, which is NOT `λ·(k0·S)` for any single λ
— **the degree-1 homogeneity that gave #521's [SAME-TENSOR-POINT] is broken by the pre-stress
term unless T/ℓ happens to scale as S.** This is the deformation channel.

**The ℓ normalization (must be derived, not hand-set).** `T/ℓ` has stiffness units; `ℓ` is the srs
bond length in the SAME length units as `pos`/`bonds` in the pipeline (the minimum-image bond
displacement norm `|d|`, `srs_primitive` `:293`). The driver reads ℓ per-bond from the geometry
(`np.linalg.norm(d)`), NOT a hand-set number. `k0=1` in the pipeline's units (units absorbed into ρ,
#521 `:141`), so `T/ℓ = Φ'(A)/|d|` in the same units as `k_shear`.

**Which bond direction carries which tension.** In SHEAR-LOADS, the swept (shear-loaded) channel is
the one at `A_wall`; its tension `T_shear=Φ'(A_wall)` enters the transverse block of EVERY bond
(the pre-stress is isotropic across bonds at the operating point, matching the #518 uniform-loading
convention — each bond sees the same channel bias). The axial fixed channel carries
`T_axial=Φ'(√α)`. **DERIVATION CHOICE TO VALIDATE (§4 control b):** whether the pre-stress T entering
the transverse block is the channel-specific tension or the bond's own axial tension is a modeling
fork; the physically standard central-pair-potential form uses the bond's OWN axial tension
`T=Φ'(A_axial-of-this-bond)` in `(T/ℓ)(I−d̂d̂ᵀ)`. **The driver uses the standard form: each bond's
transverse-stiffness gain is its OWN axial tension `Φ'(A_axial)/ℓ`, where A_axial is that bond's
axial-channel bias.** This is stated so the auditor can check the form; the alternative (channel-
tension) is reported as a KEEP-BOTH sensitivity row, not silently chosen.

---

## 4. POSITIVE CONTROLS — MANDATORY, HALT-gated, run BEFORE any adjudicated number

Per the null-verdict-liveness discipline (a [MAP-UNDEFORMED] verdict is a "the pre-stress changed
nothing" NULL — it MUST be pushed through a pipeline PROVEN to detect a REAL deformation):

- **PC1 — zero-bias recovery (A=0 ⟹ T=0 ⟹ pre-stress term vanishes ⟹ #521/cold tensor to machine
  precision).** With `A_axial=A_shear=0`: `T=Φ'(0)=0`, the `(T/ℓ)(I−P)` term is exactly zero, and the
  tensor MUST equal the merged #521/cold tensor at ρ=1 to machine precision (gated 1×10⁻⁹, the same
  full-precision-reference-on-the-same-pipeline discipline #521 used — NOT the rounded literal). This
  is the identity control: the pre-stress driver with tension off IS the #521 driver.

- **PC2 — analytic stressed-lattice limit (a KNOWN acoustoelastic result the transverse-tension form
  MUST reproduce).** Build a uniformly-tensioned SIMPLE-CUBIC lattice (the `simple_cubic_ref`
  geometry, 6 axial bonds) where the transverse acoustic speed shift under a uniform bond tension T
  is ANALYTIC: a taut simple-cubic lattice's transverse (shear) branch gains `ρc_T² = k_shear + T/ℓ`
  (the string-tension term adds directly to the transverse force constant along a cubic axis, with
  no cross-coupling by symmetry). Gate: the driver's extracted `C44_stressed − C44_unstressed` MUST
  equal `T/ℓ` to the pipeline's numerical tolerance (the transverse-speed shift `√((k_shear+T/ℓ)/ρℓ)`
  vs `√(k_shear/ρℓ)`). **This validates the `(T/ℓ)(I−d̂d̂ᵀ)` form itself on a lattice where the answer
  is known in closed form — BEFORE it is trusted on srs.** HALT if PC2 fails: the pre-stress
  insertion is wrong and no srs verdict is bookable.

- **PC3 — homogeneity re-check (the #521 VS2, re-run WITH the pre-stress term OFF).** Confirms the
  pipeline still reproduces #521's degree-1 homogeneity when T=0 — so any homogeneity BREAK observed
  with T≠0 is attributable to the pre-stress term and not a pipeline change.

All three are HALT-gated (`ALL_PASS` required before the sweep runs). Tolerances: full-precision
references computed on the SAME pipeline (never rounded literals); PC1 gated 1×10⁻⁹, PC2 gated at the
analytic-limit numerical tolerance (stated in the result), PC3 gated at the #521 VS2 floor 1×10⁻⁷.

---

## 5. THE SWEEP — same grid as #521, both channels, full coverage, two-hand cross-validation

- **A_wall grid (same as #521):** `0, √α, 0.5, 0.9, 1−α, 0.99479, 0.999, 0.99999` + the log-approach
  `1−10⁻ᵏ, k=1..8`, plus a dense 5000-point grid for the crossing search.
- **BOTH channel assignments** (SHEAR-LOADS, AXIAL-LOADS), run blind, KEEP-BOTH.
- **Full direction/branch coverage:** the same `extract_cubic_Cij` full-direction least-squares
  ([100]/[110]/[111]/off-axis), inherited unmodified from the cold pipeline.
- **Two-hand cross-validation:** full-direction least-squares long-wave C_ij vs independent [100]
  direct eigensolve, at ≥3 operating points INCLUDING the ν=2/7 crossing — the SAME cross-check
  #521/cold used, now on the pre-stressed bonds.
- **Enantiomorph parity control:** both hands must give the same C_ij at a prescribed operating
  point (pre-stress is prescribed, not chiral-kernel-evolved).

**Readouts per operating point:** `C_ij`, `K`, `G_Hill`, `ν_Hill` (+Voigt/Reuss), `Zener A`,
`sign(K)`, PLUS the **NEW pre-stress-specific readout**: the **fractional map shift**
`Δν(ρ_eff) = ν_prestress(ρ_eff) − ν_#521(ρ_eff)` vs the #521 no-prestress map at matched ρ_eff, and
`Δν/ν`, at every swept point. The #521 map is regenerated on the SAME pipeline (full-precision
reference), not read from a table.

---

## 6. FROZEN BINS (verbatim — NO fall-through else; any criterion-fails path is a loud DISCREPANT-HALT)

- **[MAP-UNDEFORMED]** — with pre-stress included, `ν(ρ_eff)` matches the #521 map within a stated
  tolerance everywhere swept ⟹ **SAME-TENSOR-POINT survives beyond-model test 1 of 2.** (Tolerance:
  `|Δν/ν| < 1×10⁻⁴` at every ρ_eff where ν is pole-free, on the same-pipeline full-precision #521
  reference; the pole-region exclusion is keyed on `|ν_#521|>1` exactly as #521 VS3.)

- **[MAP-DEFORMED]** — the map shifts (`|Δν/ν|` exceeds the [MAP-UNDEFORMED] tolerance at ≥1 swept
  point); report the NEW ν=2/7 locus (ρ_eff AND A_wall) and the shift magnitude vs A. **KNIFE
  MAXIMALLY ARMED:** if the shifted crossing lands ON a canon-distinguished amplitude
  (√α, 1−α, ½, ¼, yield A→1), that is a WOULD-BE-CHORD claim requiring from-scratch re-derivation and
  skeptical framing — do NOT celebrate; 2/7, 9.7734, 0.99479 are visible targets. Report the
  ½/¼-over-determination check; a clean landing is a smuggled-tuning red flag first, a discovery
  second (only after independent re-derivation).

- **[DESTABILIZED]** — pre-stress flips `sign(K)` or an eigenvalue (acoustic Christoffel Γ loses
  positive-definiteness) at the matter locus (ρ_eff near 9.77, or anywhere the #521 map was stable);
  report the NEW stability boundary (the ρ_eff and A_wall where `K` or an acoustic eigenvalue crosses
  zero) vs the #521 scale-invariant ρ_eff=2 floor.

- **[GEOMETRY-COUPLED]** — the pre-stress term CANNOT be honestly evaluated at fixed geometry (e.g.,
  the tension term's equilibrium requires node relaxation — the net force on a node from the bias
  tensions is nonzero at the cold geometry, so the "pre-stressed at fixed geometry" state is not a
  mechanical equilibrium and the small-signal tensor about it is ill-defined). Document EXACTLY where
  the coupling enters (which node, which residual force) and defer to the geometry arc (test 2 of 2).
  **This is an HONEST bin, not a failure** — it would mean tests 1 and 2 are inseparable, which is
  itself a load-bearing finding.

**NO fall-through else.** The bin selector is: (i) if PC1/PC2/PC3 fail → HALT (no verdict). (ii) if
the residual-force self-consistency check fails (nonzero net node force at cold geometry from the
bias tensions, above a stated floor) → [GEOMETRY-COUPLED]. (iii) else if `sign(K)` or an acoustic
eigenvalue flips at a previously-stable locus → [DESTABILIZED] (compound-recordable with iv). (iv)
else if `|Δν/ν|` exceeds tolerance anywhere → [MAP-DEFORMED]. (v) else if `|Δν/ν|` within tolerance
everywhere → [MAP-UNDEFORMED]. Any state that satisfies NONE of (ii)-(v) cleanly — e.g. VS-style
internal contradiction (map-undeformed-by-Δν but crossing-readout-inconsistent) — is a **loud
DISCREPANT-HALT with the conflicting numbers printed**, never a silent default to the benign bin.

---

## 7. ANTI-TUNE LEDGER (canon-forced vs read-off vs free)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel `Φ''(a)=k0·√(1−a²)` | CANON-FORCED | Ax4, `scale_invariant.saturation_factor` |
| 2 | Tension `Φ'(A)=k0(A√(1−A²)+arcsin A)/2` | DERIVED (from 1) | direct integration, sympy-verified §2 |
| 3 | Time-average factor = 1 (no ⟨sin²⟩) | CANON-FORCED | DC-bias R2 varactor, `node-up:118,:40,:145` |
| 4 | Initial-stress form `(T/ℓ)(I−d̂d̂ᵀ)` | STANDARD (validated PC2) | Born-Huang/Wallace pair-potential acoustic tensor |
| 5 | ℓ = per-bond `|d|` from geometry | READ-OFF (geometry) | `srs_primitive`, `np.linalg.norm(d)` — not hand-set |
| 6 | `k0=1` (units absorbed into ρ) | CANON-FORCED | #521 `:141` units convention |
| 7 | Axial core amplitude `A=√α` | CANON-FORCED (α-echo) | def-vyvsn1 |
| 8 | Which channel loads near-yield | CANON-LEANED (both run blind) | def-vyvsn1 → SHEAR; KEEP-BOTH |
| 9 | `A_wall` sweep variable | FREE (swept, not fit) | reported as a profile |
| 10 | ρ*=9.7734, ν=2/7, A_wall=0.99479 | GR-IMPORTED / READ-OFF | never inputs (anti-tune guard, locked by test) |

**0 free parameters tuned toward 2/7 / 9.7734 / 0.99479.** The ONE free thing (A_wall) is swept and
reported as a profile.

---

## 8. THE OPEN PLUMBER-PHYSICAL QUESTION (surfaced to Grant; see §9)

Per pre-test-physics-check: one plumber-physical question is genuinely open and bears on the whole
arc — whether the pre-stress is even well-defined at fixed geometry, or is inseparable from the
geometry relaxation (which would route [GEOMETRY-COUPLED] a priori and collapse test 1 into test 2).
This is surfaced to Grant BEFORE the driver runs (§9). The driver's residual-force self-consistency
check (§6 branch ii) is the COMPUTABLE discriminator that answers it either way — so per
pre-test-physics-check Trigger 9 (fork-to-computable), the arc does NOT wait on a fiat ruling: the
[GEOMETRY-COUPLED] bin + the residual-force check let the engine decide. Grant's answer refines the
FRAMING (is a nonzero residual force expected physics or a bug), not the bin logic.

---

## 9. FRAMING QUESTION FOR GRANT (recorded here; answer to be appended, Rule-12 banner)

> **Before the driver runs, one physics question:** on the srs cold reference the bonds are at
> natural length (zero tension); a DC bias raises each bond to operating amplitude A, giving a real
> bond tension `T=Φ'(A)≠0`. **Is that bias tension a genuine pre-stress the lattice holds at FIXED
> geometry (the nodes stay put, the bond tensions self-balance by the srs site symmetry) — or does a
> nonzero net force appear at each node that only a geometry relaxation can cancel (which would mean
> pre-stress and geometry-change are inseparable, i.e. [GEOMETRY-COUPLED] a priori)?**

Two readings, each with a computable signature the driver already checks (§6 branch ii):
- **(reading A) self-balancing pre-stress:** the srs site symmetry makes the vector sum of bond
  tensions at each node zero at the cold geometry ⟹ fixed-geometry pre-stress is well-defined ⟹ the
  ν(ρ_eff) map shift is the honest test-1 answer ([MAP-UNDEFORMED]/[MAP-DEFORMED]/[DESTABILIZED]).
- **(reading B) unbalanced pre-stress:** a nonzero residual node force appears ⟹ [GEOMETRY-COUPLED]
  ⟹ tests 1 and 2 are inseparable, deferred to the geometry arc.

The driver computes the residual node force either way; Grant's answer tells us whether a nonzero
residual is EXPECTED PHYSICS (reading B is the real answer) or a BUG to chase (reading A is expected
and a residual means the tension insertion is wrong). **This is the framing input; the bin is
engine-decided.**

> **↗ ENGINE-DECIDED (2026-07-04, per Trigger-9 fork-to-computable; this appends the disposition —
> prereg body above is a frozen record, banner-append only).** The residual-force discriminator ran
> and returned **reading A: self-balancing.** Max residual node force = **3.6×10⁻¹⁷** (relative
> 4.2×10⁻¹⁶ — machine zero) under uniform bias bond tension at the cold srs geometry. The srs z=3
> site symmetry (each node's three bond directions sum to zero) cancels the bias tensions at fixed
> geometry, so the "pre-stressed at fixed geometry" state IS a mechanical equilibrium and the
> small-signal tensor about it is well-defined. **[GEOMETRY-COUPLED] is NOT triggered; test 1 is
> well-posed and NOT collapsed into test 2.** The framing question is STILL surfaced to Grant (does
> a machine-zero residual match his intuition for the srs site symmetry?) — but the bin logic did
> not wait on it. Provenance: `research/2026-07-04_prestress-tensor_result.md` (VERDICT BOX + §7);
> driver §(1) geometry_coupled_discriminator.

---

## 10. FREEZE

This prereg is FROZEN at this commit. The driver `prestress_elastic_tensor.py`, the test, and the
result doc are scaffolded AFTER this commit (commit order proves the freeze). Bins, tolerances, and
the anti-tune ledger above are the adjudication contract; no gate looser than frozen here; no
post-data bin edits (Rule 11). Any amendment is a Rule-12 dated banner preserving this body.
