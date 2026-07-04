# RESULT — The SATURATED srs Elastic-Tensor: the saturated small-signal tensor is the COLD tensor at rho_eff — [SAME-TENSOR-POINT] on BOTH assignments

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/saturated-elastic-tensor`
**Driver:** `src/scripts/vol_1_foundations/saturated_elastic_tensor.py`
**Output:** `_output/saturated_elastic_tensor.json` (driver-regenerable; gitignored)
**Test:** `src/tests/test_saturated_elastic_tensor.py` (12 pass)
**Prereg (FROZEN):** `research/2026-07-04_saturated-elastic-tensor_prereg_FROZEN.md`
**Stacks on:** COLD arc (merged) `srs-elastic-tensor_result.md`; #518 (MERGED 6d2ecdf4)
`matter-stiffening-rho_result.md` — resolves its §6 scope flag.

## VERDICT BOX

> **PRIMARY BIN: [SAME-TENSOR-POINT]** on BOTH channel assignments.
>
> The saturated **small-signal** Cauchy elastic tensor — computed by the Born-Huang method of
> long waves on the **SATURATED** bond tensor `Φ_b(A) = k_{a,0}·S(A_axial)·d̂⊗d̂ +
> k_{s,0}·S(A_shear)·(I−d̂⊗d̂)`, i.e. the differential stiffnesses at the DC bias point — is the
> **COLD tensor with ρ → ρ_eff = ρ_cold·(S_axial/S_shear)**, exactly. The regime gap flagged in
> #518 §6 **CLOSES**: driving the saturated ρ_eff to 9.7734 (SHEAR-LOADS, A_wall=0.99479) DOES
> land the same tensor — **ν_Hill = 0.285714 = 2/7, K/G_Hill = 2.0000, Zener A = 1.2293** — that
> the cold arc found at cold ρ*=9.7734. Saturated ρ_eff is **tensor-equivalent** to cold ρ.
>
> **THE REASON (proven, not asserted):** the Born-Huang map `(k_a, k_s) ↦ C_ij` is **homogeneous
> of degree 1**, so the dimensionless RATIOS (ν, Zener, K/G) are homogeneous **degree 0** — an
> overall stiffness scale drops out (verified to 4×10⁻⁸, VS2). The saturated ν(ρ_eff) map is the
> cold ν(ρ) map with ρ→ρ_eff, bit-for-bit (VS3, ≤1×10⁻⁶ at every operating point). The
> **[DEFORMED-FAMILY]** bin is empty (the map is not deformed).
>
> **THE KNIFE HOLDS — [NEW-DISTINGUISHED-POINT] is EMPTY.** ν=2/7 is reached at the free-knob
> crossing A_wall=0.99479, which is **NOT** √α, **NOT** 1−α, **NOT** the A→1 yield wall — the
> #518 [DRIVES-STIFF-QUALITATIVE] finding stands: **the direction (STIFFENING) is earned, the
> value 9.7734 stays GR-imported.** [SAME-TENSOR-POINT] is a CONSISTENCY finding (the saturated
> map is the cold map, undeformed) — it is **NOT a value derivation**. It does NOT make 9.77
> emergent; it makes the saturated small-signal tensor a **scaled cold tensor**.
>
> **THE NEW PHYSICS (the axis the cold arc could not see):** while the RATIOS freeze at ρ_eff, the
> **ABSOLUTE moduli scale by the overall S factor** — the lattice goes **floppy** near the yield
> wall (C44_abs: 0.1766 cold → 4×10⁻⁵ as A→1; the corpus "topology melts"). And **sign(K) is
> scale-invariant**: the K<0 instability boundary sits at ρ_eff=2 (the cold ρ=2 floor, mapped
> through ρ_eff to A_wall≈0.9 for shear-loads), **unshifted** by saturation magnitude.

**Cold positive control PASSED.** A_wall=0 (both channels de-energized, S_axial=S_shear=1) →
ρ_eff=1 → the saturated tensor is bit-identical to the merged cold tensor at ρ=1 (C11=C12↔=C44=
±0.17678, K=−0.05893 UNSTABLE, Zener=1.0000). Enantiomorph parity 2×10⁻¹⁶. Two-hand
cross-validation ALL_AGREE (long-wave vs [100] direct eigensolve, ≤3×10⁻⁸) at cold ρ=1, stable
ρ=3, and the ν=2/7 crossing.

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** translational-u (Cauchy) sector of the RATIFIED chiral srs-z3, on the **SATURATED**
  bond tensor. BOTH `k_a` and `k_s` are translational-u / **CAPACITIVE** springs (axial STRETCH vs
  transverse SHEAR of the *same* bond) — NOT the ε-vs-μ photon pair (#518 verbatim). Cosserat
  couple-stress = Stage 2, NOT invoked (the Cauchy family is clean).
- **MODE:** SMALL-SIGNAL long-wave. The saturated `k(A) = k_0·S(A)` are the **differential
  (tangent) bond stiffnesses at the DC bias point** — the small-signal elastic response *about*
  the operating point (varactor-bias picture, INVARIANT-S2).
- **REGIME:** quasi-static about a DC bias. Op14 saturation **ON**. **PHASE-STATE = saturated,
  S<1** (the cold arc was S=1, saturation OFF — this is the separating axis). Sub-yield on the
  interior; A→1 is the yield-wall limit.
- **COORDS (A46):** operating-point knob `(A_axial, A_shear)` in **phase-space / reactance**
  (#518 verbatim); tensor readout `ω(k)→C_ij→ν,Zener,K/G` in **real-space / spatial-Brillouin**;
  each measured in its OWN matching coordinate. No φ²/winding comparison. A46-clean on both axes.
- **CLASS:** CONSISTENCY / MANIFESTATION. ν, Zener, K/G are α-CLEAN dimensionless ratios (α enters
  only via the √α core amplitude, off the ratio verdict path). **EMERGENCE FORBIDDEN** for any
  VALUE — 2/7, 9.7734, 0.99479 are all visible targets; NO tuning toward any (the frozen bins +
  the anti-tune ledger are the guard).

---

## 1. THE LOAD-BEARING PHYSICS — homogeneity, verified (VS2)

The single fact that drives every bin, **verified directly**:

The Born-Huang long-wave map `(k_a, k_s) ↦ C_ij` is **homogeneous of degree 1** — each C_ij is a
sum of terms linear in one bond stiffness (the long-wave `Γ = Φ2_aa − Φ1_ao·Φ0_oo⁻¹·Φ1_oa` is
degree-1 because the degree-(−1) `Φ0_oo⁻¹` cancels one of the two degree-1 `Φ1` factors). VS2
confirms, for an arbitrary overall scale λ=0.41:

| Property | measured | meaning |
|---|---|---|
| `C_ij(λk)/λ − C_ij(k)` rel-err | **4×10⁻⁸** | C_ij is homogeneous degree-1 (scales by λ) |
| `ν, Zener, K/G` under λ-scaling | **identical to 4×10⁻⁸** | ratios are homogeneous degree-0 (λ drops out) |
| `K(λk)/K(k)` | **= λ to 1×10⁻⁸** | absolute bulk modulus scales by exactly λ |

**Consequence:** the dimensionless ratios depend **ONLY** on `ρ_eff = k_a·S_axial/(k_s·S_shear) =
ρ_cold·(S_axial/S_shear)`. The overall S factor cancels in every ratio. So the saturated ν(ρ_eff)
map **IS** the cold ν(ρ) map under ρ→ρ_eff. This was **pre-registered as the expected outcome**
(prereg §0.6) — the result confirms it.

---

## 2. VALIDATE-ON-KNOWN — all PASS (HALT-gated)

The saturated driver imports the cold arc's PROVEN `extract_cubic_Cij` / `acoustic_christoffel`
**unmodified** (identical pipeline — the load-bearing point) and prepends only the per-channel
S(A) stiffness maps. On top of the inherited cold V1/V2/V3 (simple-cubic, diamond-Born-vs-symbolic,
isotropy — all GREEN, `srs-elastic-tensor_result.md` §1), THREE saturated-specific checks:

| # | Check | Result | Verdict |
|---|---|---|---|
| **VS1** | cold-recovery: both channels off (S=1) → tensor = cold at ρ=1 | ρ_eff=1.0, C11=C44=+0.17678, C12=−0.17678, K=−0.05893, Zener=1.0000 | **PASS** |
| **VS2** | homogeneity: C_ij deg-1, ratios deg-0, K scales by λ | ratio-inv 4×10⁻⁸; K-scale err 1×10⁻⁸ | **PASS** |
| **VS3** | saturated == cold-at-matched-ρ_eff (SHAPE + Zener, pole-free) | ≤1×10⁻⁶ at every operating point, both sides of the K=0 pole | **PASS** |

**Rule-10 note (empirical-driver discipline caught two TEST-construction defects early, not
physics):** the first run HALTed on VS1/VS3. Both were adjudication-metric bugs, surfaced by
running the imperfect driver early: (i) VS1 initially wired the #518 fixed-channel-at-√α point as
"cold", but that is a *loaded* cold vacuum (ρ_eff=0.9963), not the fully-de-energized control — the
true cold control is BOTH channels off (S=1); (ii) VS3 initially compared ν *through* its
divergence poles (ρ_eff=1 iso-bond, ρ_eff=2 K=0), where a relative error on a diverging quantity is
meaningless **even when the two values agree bit-for-bit** (shape_err was ~1×10⁻¹⁶ there). Fixed by
comparing the pole-free tensor SHAPE (C11/C44, C12/C44) + Zener, excluding ν in its divergent
regime. The underlying physics was correct on the first run (VS2 passed immediately); the fixes were
to the *test*, not the tensor.

---

## 3. THE nu(rho_eff) MAP — both assignments (KEEP-BOTH, run blind, both recorded)

Per #518's exact loading definitions (`matter_stiffening_rho.py`), run BOTH blind:

**SHEAR-LOADS** (axial fixed sub-saturated at √α, S_axial=0.99270; shear swept to A_wall,
S_shear=S(A_wall)): ρ_eff = S_axial/S_shear **RISES** → **STIFFENING**.

| A_wall | S_shear | ρ_eff | ν_Hill | Zener A | K (abs) | sign(K) | C44 (abs) |
|---|---|---|---|---|---|---|---|
| 0 (loaded-cold) | 1.0000 | 0.9963 | (pole) | 0.9995 | −0.05914 | − | 0.17661 |
| 0.5 | 0.8660 | 1.1505 | −8.151 | 1.0178 | −0.04335 | − | 0.15845 |
| 0.9 | 0.4359 | 2.2858 | −0.7012 | 1.1052 | +0.00734 | **+** | 0.09213 |
| 0.99 | 0.1411 | 7.0629 | +0.1983 | 1.2106 | +0.04209 | + | 0.03431 |
| **0.99479** (crossing) | 0.10194 | **9.7733** | **+0.285714 = 2/7** | **1.2293** | +0.04670 | + | 0.02536 |
| 0.999 | 0.04471 | 22.28 | +0.4078 | 1.2595 | +0.05344 | + | 0.01152 |
| 0.99999 | 0.004472 | 222.8 | +0.4909 | 1.2830 | +0.05818 | + | 0.00118 |
| →1 (yield wall) | →0 | →∞ | →0.5 | →1.286 | +0.0587 | + | →0 |

**AXIAL-LOADS** (mirror control: shear fixed at √α, axial swept to A_wall): ρ_eff **FALLS** →
**SOFTENING**; ρ_eff→0.00449 at the yield limit; **never crosses 9.77.**

| A_wall | ρ_eff | ν_Hill | sign(K) |
|---|---|---|---|
| 0.5 | 0.8692 | +9.663 | − |
| 0.9 | 0.4375 | +2.214 | − |
| 0.99 | 0.1416 | +1.312 | − |
| →1 | →0.0045 | (low-ρ branch) | − |

- **The direction is ASSIGNMENT-SET** (as #518 found): shear-loads stiffens, axial-loads softens.
  The substrate distinguishes them.
- **At the ν=2/7 crossing (SHEAR-LOADS, A_wall=0.99479): ν_Hill=0.285714=2/7, K/G_Hill=2.0000,
  Zener=1.2293** — the cold ν=2/7/K=2G tensor, reached from the saturated bonds. The regime gap
  closes at the tensor level.
- **Note the ρ_eff=1 / iso-bond rows show a ν "pole" (huge magnitude)** — this is the K→0
  divergence of ν, NOT a physics anomaly; the tensor SHAPE there is clean (Zener=1.000). Reported
  honestly rather than suppressed.

## 4. THE ABSOLUTE-SCALE STORY — the floppy-near-yield axis (NEW; the cold arc could not see it)

The cold arc worked with a fixed overall stiffness scale, so it saw only the ratio-family. Under
saturation the **absolute** moduli scale by the overall S factor (homogeneity degree-1), giving a
picture the cold arc structurally could not produce:

- **The lattice goes FLOPPY near the yield wall.** SHEAR-LOADS C44 (absolute shear stiffness):
  0.17661 (loaded-cold) → 0.09213 (A_wall=0.9) → **0.02536** (the ν=2/7 crossing) → **4×10⁻⁵**
  (A_wall→1). The absolute shear stiffness collapses toward zero as the shear channel yields — the
  corpus "**topology melts**" / G_shear→0 picture (`electron-bh-isomorphism.md:32`), now
  quantified on the srs Cauchy tensor. The RATIOS freeze (ν→0.5, Zener→1.286) while the absolute
  scale → 0. **This is the physical content of "matter stiffening" that ρ_eff alone hides:** the
  bond-stiffness RATIO stiffens, but the bulk lattice softens in absolute terms as it approaches
  rupture.
- **sign(K) stability boundary is scale-invariant** (predicted §0.6, confirmed): K<0 (unstable)
  below ρ_eff=2, K>0 (stable) above — the same cold ρ=2 floor, **unshifted by saturation
  magnitude**, mapped through ρ_eff to A_wall≈0.9 (shear-loads) / never-reached (axial-loads, which
  stays sub-2 throughout, K<0 across the whole matter regime). The *magnitude* of K is softened by
  S; the *sign* is set by ρ_eff alone.
- **Worst-case internal acoustic Γ** (the softest-vs-stiffest [100] acoustic-branch mismatch) rises
  from ~0.0002 (cold) toward **0.95** at the yield wall — as the absolute shear channel collapses
  while the bulk stays comparatively stiffer, the internal acoustic impedance step grows. (Reported
  as a mechanical-matching diagnostic; the substrate minimizes |Γ|² per Ax3, so a large internal Γ
  near yield is the mechanical signature of the impending rupture, consistent with the
  saturation-boundary picture.)

---

## 5. TWO-HAND CROSS-VALIDATION (the cold arc's cross-check, on the saturated bonds)

The full-direction least-squares long-wave C_ij vs an **independent [100] direct eigensolve** of the
saturated acoustic branches, at ≥3 operating points **including the ν=2/7 crossing** (the SAME
cross-check the cold arc used):

| Operating point | ρ_eff | C11 long-wave / [100]-direct | rel-err | AGREE |
|---|---|---|---|---|
| cold ρ=1 | 1.0000 | 0.17613 / 0.17613 | 5.6×10⁻⁹ | ✅ |
| stable ρ=3 | 3.0000 | 0.10568 / 0.10568 | 2.1×10⁻⁸ | ✅ |
| **ν=2/7 crossing** | 9.7734 | 0.07420 / 0.07420 | 2.0×10⁻⁸ | ✅ |

**ALL_AGREE.** The two independent extractions of the saturated tensor agree to ~10⁻⁸ — the
saturated number is trustworthy on the same footing as the cold one.

---

## 6. THE KNIFE — the crossing is NOT canon-distinguished ([NEW-DISTINGUISHED-POINT] EMPTY)

Maximum-scrutiny check per the frozen bin (2/7, 9.7734, and 0.99479 are ALL visible targets):

| Test | Value | Canon-distinguished? |
|---|---|---|
| Crossing A_wall (SHEAR-LOADS) | 0.99479 | — |
| = √α (0.085425)? | no (off by ~12×) | ✗ |
| = 1−α (0.992703)? | no | ✗ |
| = the def-vyvsn1 A→1 yield wall? | no (that gives ρ_eff→∞, overshoots) | ✗ |
| any clean ½/¼ over-determination? | none | ✗ |

**[NEW-DISTINGUISHED-POINT] is EMPTY.** No canon-forced A lands ON ν=2/7 — exactly the a-priori
expectation (a firing of this bin would have been a red flag for smuggled tuning, not a discovery).
**The knife holds:** ν=2/7 is reached only at the free-knob amplitude 0.99479, which is the
GR-imported value 9.7734 in an amplitude costume. **NO parameter was tuned toward 2/7, 9.7734, or
0.99479** — RHO_STAR_IMPORTED and A_WALL_518_CROSSING are read-off comparison constants the sweep
never fits to (locked by `test_anti_tune_constants_are_readoff_only`). The #518
[DRIVES-STIFF-QUALITATIVE] verdict stands: **the direction is earned, the value stays imported.**

---

## 7. PER-ASSIGNMENT BIN VERDICTS (bins are per-assignment)

| Assignment | Primary bin | Basis |
|---|---|---|
| **SHEAR-LOADS** | **[SAME-TENSOR-POINT]** | STIFFENING; at ρ_eff=9.7734 the saturated tensor gives ν=2/7, K/G=2, Zener=1.229 to cold precision; VS3 confirms the map is undeformed. [NEW-DISTINGUISHED-POINT] empty (crossing not canon-forced). |
| **AXIAL-LOADS** | **[SAME-TENSOR-POINT]** (mirror) | SOFTENING; ρ_eff→0, no 9.77 crossing; the map is still the undeformed cold map (VS3 passes at ρ_eff<1 too). The mirror control confirms the direction is assignment-set. |

Neither assignment fires [DEFORMED-FAMILY] (VS3 passes everywhere) or [NEW-DISTINGUISHED-POINT]
(crossing not canon-forced). [UNSTABLE] is a REPORTED sub-finding, not a primary bin: K<0 below
ρ_eff=2 on both assignments (shear-loads is unstable for A_wall<~0.9; axial-loads is unstable across
the whole matter regime) — the saturated stability boundary is the cold ρ=2 floor, scale-invariant.

---

## 8. KEEP-BOTH — the saturated axis lives ALONGSIDE the cold axis (cold NOT superseded)

Per the KEEP-BOTH discipline, the saturated ρ_eff axis is a NEW axis recorded alongside the cold-ρ
axis — the cold result is **NOT restated as superseded**:

- **COLD axis (merged, unchanged):** the srs cold Cauchy tensor is a one-parameter family in
  ρ=k_a/k_s; ν=2/7 ⟺ K=2G only at cold ρ*=9.7734 (GR-imported); Zener=1.229 there; K<0 for ρ<2;
  [ANISOTROPIC-BREAKDOWN]+[DIFFERENT-ν]. **This stands.**
- **SATURATED axis (this arc, NEW):** the saturated *small-signal* tensor at operating point
  (S_axial, S_shear) is that SAME cold family evaluated at ρ_eff=ρ_cold·(S_axial/S_shear), with the
  absolute scale softened by S. The two axes are **consistent** (the saturated map IS the cold map
  under ρ→ρ_eff) — the saturated axis EXTENDS the cold one into the operating-point regime; it does
  not replace it.

The channel-assignment fork (SHEAR-LOADS vs AXIAL-LOADS) is a formal recorded axis (both run blind),
not a pre-picked branch — KEEP-BOTH on the assignment fork too.

---

## 9. FALLOUT / AUDITOR-QUEUE (surfaced; implementer does NOT land manuals)

Auditor-lane manual landings (implementer surfaces, auditor lands):

| Site | Proposed disposition |
|---|---|
| **#518 §6 scope flag** (`matter-stiffening-rho_result.md`: "recompute the saturated C_ij(ρ_eff)… I do NOT claim it") | **RESOLVE (candidate):** the saturated C_ij IS recomputed here; driving ρ_eff to 9.77 DOES land the same cold ν=2/7/K=2G tensor. The regime gap closes at the tensor level. **Scope caveat (the knife):** this is a CONSISTENCY finding (undeformed map), NOT a value derivation — 9.77 stays GR-imported (crossing at the free-knob A_wall=0.99479). |
| **#518 cross-link to `srs-elastic-tensor_result.md`** ("reaching the same ν=2/7 tensor from the saturated bonds is UNTESTED") | **STRENGTHEN (candidate):** now TESTED and CONFIRMED. Add forward evidence `saturated_elastic_tensor.py`. |
| **`node-up-small-large-signal.md`** (R1 symmetric-internal null: S_ε=S_μ ⟹ Z=Z_0) | **STRENGTHEN (candidate):** the elastic-sector sibling now has its own tensor form — S_axial=S_shear ⟹ ρ_eff=ρ_cold ⟹ the FULL saturated tensor = the cold tensor (not just the ratio): symmetric loading is elastically transparent at the tensor level, not merely the ρ level. |
| **The K=2G "GR-imported" grade** (PR#261, `k2g-crystalline-provenance_result.md`) | **UNTOUCHED / re-confirmed:** the saturated tensor reaches K=2G only at the imported ρ_eff=9.77 point; saturation does NOT force K=2G at any canon-distinguished operating point. The GR-import grade stands. |
| **The floppy-near-yield / topology-melts picture** (`electron-bh-isomorphism.md:32`) | **NEW quantitative support (candidate):** G_shear→0 near yield is now quantified on the srs Cauchy C44 (0.177→4×10⁻⁵ as A→1); the RATIOS freeze while the absolute scale collapses. |

**No rewrites performed.** Status-demotion / strengthen / cross-link / resolve ROWS only; the
auditor lane lands the manual entries.

---

## 10. flag-don't-fix — surfaced, not resolved

1. **The "matter stiffening" noun vs the absolute-softening reality (SURFACED for Grant).** #518's
   picture is "matter = local STIFFENING (ρ_eff rises)". At the tensor level this arc shows a
   two-faced behavior the ρ_eff scalar hides: the bond-stiffness RATIO stiffens (ρ_eff rises, ν
   moves toward 2/7 and beyond), but the **absolute** bulk lattice SOFTENS (K, G, C_ij → 0 in
   magnitude as A→1, floppy near rupture). Both are true and consistent (ratio vs scale), but
   "stiffening" is only half the story — the absolute lattice is going floppy toward yield. This is
   a physics-framing observation for Grant, not a contradiction I resolve; the #518 direction result
   (ρ_eff RATIO rises) is unaffected.

2. **The Born-vs-Keating-vs-clm-bjceop bond-model discrepancy (INHERITED, still open).** The cold
   arc surfaced (§8) that the engine-native BORN 2-body model, the Keating angle-bend model, and the
   corpus `clm-bjceop` form give three different C_ij on the same lattice. This arc uses the SAME
   engine-native Born model (the honest carrier choice), so the discrepancy is INHERITED, not
   introduced. The [SAME-TENSOR-POINT] verdict is model-independent: on ANY of the three, the
   saturated tensor's dimensionless ratios are homogeneous degree-0 (depend on ρ_eff only), so the
   saturated map is the cold map under ρ→ρ_eff regardless of which bond model sets the family shape.
   Which bond model is canonical remains a Grant/auditor framing question — unchanged by this arc.

---

## Cross-references (verified at branch HEAD)

- Driver: `src/scripts/vol_1_foundations/saturated_elastic_tensor.py`
- Test: `src/tests/test_saturated_elastic_tensor.py` (12 pass)
- Prereg (FROZEN): `research/2026-07-04_saturated-elastic-tensor_prereg_FROZEN.md`
- COLD arc (merged): `research/2026-07-04_srs-elastic-tensor_result.md`;
  driver `src/scripts/vol_1_foundations/srs_elastic_tensor.py` (imported unmodified)
- #518 (MERGED 6d2ecdf4): `research/2026-07-04_matter-stiffening-rho_result.md` §6 (the scope flag);
  driver `src/scripts/vol_4_engineering/matter_stiffening_rho.py` (exact loading defs)
- Kernel S(A): `src/ave/axioms/scale_invariant.py` `saturation_factor`, `shear_modulus_ratio`
- Varactor-bias / operating-point (INVARIANT-S2): `manuscript/ave-kb/CLAUDE.md`
- Symmetric-loading Z=Z_0 sibling: `node-up-small-large-signal.md`;
  `research/2026-06-22_c4-symmetric-loading-reconciliation.md:42`
- Floppy / topology melts: `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md:32`
- K/G one-param family in ρ: `research/2026-06-15_form-deriving-value-importing_meta-finding.md:161`
- K=2G GR-imported (PR#261): `research/2026-06-15_k2g-crystalline-provenance_result.md`
- Carrier: `src/ave/core/chiral_lattice.py` `build_srs_net`
