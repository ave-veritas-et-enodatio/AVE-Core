# Boundary-Strain Amplitude — DERIVATION (Leg A analytic; the exact spherical-elasticity kinematics + the spatial-separation mechanism)

**Date:** 2026-07-21
**Class:** DERIVATION (analytic Leg A of the frozen prereg `research/2026-07-21_boundary-strain-amplitude_prereg-FROZEN.md`). Forms `[derived]` (exact geometric identities); values `[canon]`/`[import]`-tagged. Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched.
**Provenance:** Grant standing derivation-class authorization (the #773 §4(a) owed follow-on). COMMIT 2 (analytic Leg A + driver), after the prereg was frozen + pushed ALONE (`c35c612e`). Every `[canon]` cite content-verified two-method at base HEAD `3d07ceeb`.

> **Scope note.** This doc lands the Leg-A ANALYTIC kinematics + the physical mechanism (why the answer is what it is). The FINAL frozen-bin verdict — citing only the frozen criteria's outputs (Legs A/B/C) — lands in the result doc.

---

## §1 — the exact spherical-elasticity kinematics of a radial breather `[derived]`

For a spherically-symmetric radial displacement `u = f(r) r̂` (the localized A1 breather form #773 §2 Step 2 uses), the strain tensor in the orthonormal spherical frame is **diagonal**:

$$\varepsilon_{rr} = f'(r), \qquad \varepsilon_{\theta\theta} = \varepsilon_{\phi\phi} = \frac{f(r)}{r},$$

with dilatation `θ = ∇·u = f′ + 2f/r` and deviatoric shape `D(r) ≡ ε_rr − ε_θθ = f′ − f/r` (the #773 "deviatoric ∝ (f′−f/r)" object). The **per-bond** decomposition the saturation kernel keys on (#773 §2 Step 3): a bond at angle `ψ` to `r̂` has

- **axial swing** (keys `k_a`): `d̂·ε·d̂ = cos²ψ·ε_rr + sin²ψ·ε_θθ` (radial bond `ψ=0` ⇒ `ε_rr`);
- **transverse swing** (keys `k_s`): `|(I−d̂d̂)·ε·d̂| = ½|sin 2ψ|·|ε_rr − ε_θθ| = ½|sin 2ψ|·|D|` (max at `ψ=45°`, `= ½|D|`).

**★The factor of ½ is derivation-grade, not a convention:** the transverse *bond swing* the `k_s` kernel keys on is the shear `½|D|` (maximal over orientation), NOT the raw principal-strain difference `|D|`. On the lattice the RMS over the discrete bond orientations further reduces it. So the physically-correct `k_s`-argument (MEASURE-1) is systematically ≈½ the raw `|D|` (MEASURE-2). This is the load-bearing factor near the 0.5 margin (§4).

---

## §2 — the two admissible bracket-limits are exact `[derived]`

- **uniform (affine) dilatation** `f ∝ r` (the #773 UNIFORM limit): `ε_rr = ε_θθ = const`, `D = 0` ⇒ `ρ_dev ≡ |D|/|ε_rr| = 0`. Mode-orthogonality holds; `k_a` rails alone. This is the limit #773 correctly derived.
- **divergence-free exterior tail** `f ∝ 1/r²` (the only decaying div-free radial harmonic; `master-equation.md:20` mass=interior-dilatation ⇒ exterior is source-free; `gravitomagnetism-frame-dragging.md:15` `A_g∝1/r²` is the same harmonic order): `ε_rr = −2A/r³`, `ε_θθ = A/r³`, `D = −3A/r³`, `θ = 0` ⇒ **`ρ_dev = |−3A/r³| / |−2A/r³| = 3/2`** — the deviatoric strain strictly DOMINATES the axial (by 50%) everywhere in the tail.

**★The fence (both ways).** Every localized breather that carries net mass MUST transition from a dilatational interior (`θ≠0`) to a div-free `ρ_dev=3/2` exterior. So no admissible profile makes the boundary deviatoric strictly negligible — a bare "`k_s` stays cold" is excluded at the tail by geometry. The only live question is **whether the axial swing has already fallen below yield by the radius where the deviatoric reaches yield-scale** — i.e. whether the axial-saturation shell and the deviatoric build-up are SPATIALLY SEPARATED. §3 shows they are.

---

## §3 — ★the spatial-separation mechanism (why `ρ_dev(r_sat) ≈ 0` but the tail is deviatoric-dominated) `[derived]`

For any smooth peaked localized profile the **axial swing `|ε_rr| = |f′|` peaks at the core CENTER** (the dilatational core), where `ε_rr ≈ ε_θθ` (isotropic dilatation) so `D ≈ 0`. The **deviatoric `|D|` peaks at an OUTER shell**, where the profile bends from dilatational to div-free — and there the axial swing has already decayed. Worked exactly for the primary member `f = A·s/(s²+1)^{3/2}` (`s=r/r_c`, affine core → div-free tail):

$$\varepsilon_{rr}=f'=\frac{1-2s^2}{(s^2+1)^{5/2}},\quad \varepsilon_{\theta\theta}=\frac{f}{r}=\frac{1}{(s^2+1)^{3/2}},\quad D=\frac{-3s^2}{(s^2+1)^{5/2}},\quad \theta=\frac{3}{(s^2+1)^{5/2}}.$$

- `|f′|` is maximal at `s=0` (`=1`, the saturation shell `r_sat`), where `D(0)=0` ⇒ **`ρ_dev(r_sat)=0`**.
- `|D|` is maximal at `s=√(2/3)=0.816`, value `|D|=2(5/3)^{-5/2}=0.558` — there `|f′| = 0.093` (only 9% of yield).
- ⇒ **peak deviatoric `|D| = 0.558·A_yield`** (MEASURE-2 shape) / **bond-shear `½|D| = 0.279·A_yield`** (MEASURE-1 partner), **when the peak axial = `A_yield`**.

So the kernel arguments are **spatially disjoint**: `k_a` rails at the core center (where `k_s` is cold, `ρ_dev≈0`), and `k_s`'s argument peaks at an outer shell (where `k_a` has already relaxed). The closed-form family (all normalized so peak axial = `A_yield`):

| profile | `ρ_dev(r_sat)` | peak `½|D|` (MEASURE-2 bond-shear) | peak `|D|` (MEASURE-2 shape) | class |
|---|---|---|---|---|
| **smooth-eshelby** (PRIMARY) | `0` | `0.279` | `0.558` | smooth |
| **gaussian-curlfree** (seed) | `0` | `0.368` | `0.736` | seed |
| **lorentzian** | `0` | `0.250` | `0.500` | smooth |
| **sharp-eshelby** (LIMIT) | `0`* | `0.750` | `1.500` | sharp (strain-discontinuous) |

*(`sharp-eshelby` has an interior affine plateau where `D=0`; its deviatoric jumps at the discontinuity — the continuum peak `½|D|=0.75`, `|D|=1.5` sits just outside `r_c`.)*

**★The result is bracketed but profile-conditional.** The smooth members sit at `½|D| ≈ 0.25–0.37` (**sub-half-yield** — bin-1 direction on the bond-shear measure), the sharp-core LIMIT at `0.75` (yield-scale direction), and the raw `|D|` upper-bound at `0.5–1.5`. The verdict hinges on (a) core-boundary **sharpness** (canon under-determines it, §2 of the prereg) and (b) which **deviatoric measure** — the physically-correct per-bond bond-shear (MEASURE-1) or the loose principal-strain-difference (MEASURE-2).

---

## §4 — ★the pre-stress remap DOMINATES `k_s` at the yield-scale boundary (Leg C analytic; the #773-flagged countervailing mechanism) `[canon-read + derived]`

The `[canon]` pre-stress remap (`axiom-register.md:193` `[SIGN-RULE-DERIVED]`): `k_{shear,eff} = k_s + T/ℓ_node`, with `T` the bond axial tension and the sign rule *"an axial end-load buckles the strut ⟹ COMPRESSION (`T<0`) ⟹ `k_{shear,eff}` SHRINKS ⟹ UNCAPPED."* Per bond, `T = k_a·(axial stretch) = k_a·ε_axial·ℓ_node`, so

$$\frac{T}{\ell_{node}} = k_a\,\varepsilon_{axial}, \qquad \frac{k_{shear,eff}}{k_s} = 1 + \frac{k_a}{k_s}\,\varepsilon_{axial}.$$

At the saturation shell `ε_axial → A_yield`. In the AVE fixed-arc-length buckling picture the **yield strain is `O(1)`** (the bond bows when its stretch approaches `arc* ≈ 0.89–0.96 ℓ_node`, `axiom-register.md:189`), and `k_a/k_s = ρ*/1 = 9.77` (`RHO_STAR`, DERIVED from `ν_Hill=2/7`, GR-imported). Therefore

$$\left.\frac{T}{\ell_{node}}\right|_{shell} \sim k_a\cdot O(1) \approx 10\,k_s \;\gg\; k_s.$$

**★The remap term SWAMPS the bare `k_s` by ~an order of magnitude at a yield-scale axial boundary.** So the shell shear stiffness is controlled by the axial tension, NOT by the intrinsic `k_s`. Two consequences:
- **SIGN (robust, `ε_yield`-independent):** set by the breather's DC dilatation sign. An **expanding** core (`θ>0`, outward) puts the shell bonds in net tension ⇒ `T>0` ⇒ `k_{shear,eff}` **STIFFENS**. A **contracted / compressed** core (`θ<0` — the `master-equation.md:20` mass = *"trapped acoustic compression"* reading) puts them in compression ⇒ `T<0` ⇒ `k_{shear,eff}` **SOFTENS** (drives it toward zero and negative — a shear-buckling instability). This is precisely the `axiom-register.md:193` countervailing mechanism the #773 review flagged, and at yield scale it is not a small correction — it is dominant.
- **MAGNITUDE (`ε_yield`-scaled, disclosed):** `|T/ℓ|/k_s ≈ (k_a/k_s)·ε_yield`. For the AVE `O(1)` yield strain this is `~10`; if `ε_yield` were small the remap would be a small correction — so the magnitude rides the (canon `O(1)`) yield-strain, while the SIGN and the "dominates" conclusion hold for any `ε_yield ≳ k_s/k_a ≈ 0.1`.

**⇒ Even where the DIRECT transverse swing is sub-yield (smooth cores, §3), the bulk-only wall is NOT clean:** the shell shear stiffness `k_{shear,eff}` is not the cold `k_s` — it is dominated by the axial pre-stress, and for a compressed core it is softened/buckled. The "`k_s` stays cold, shear channel alive" premise the bulk-only `Γ_bulk=−1` wall needs (#773 §2 Step 3, §5 Refinement 1) is undercut by the pre-stress remap independently of the direct-swing result.

---

## §5 — Leg-A synthesis (analytic bin-lean; final verdict in the result doc after Legs B/C)

| axis | analytic finding | bin-lean |
|---|---|---|
| direct swing, smooth cores (MEASURE-1 bond-shear) | peak deviatoric `½|D| ≈ 0.25–0.37·A_yield` (sub-half); `ρ_dev(r_sat) ≈ 0` (spatially separated) | → bin-1 direction (K_A-ONLY) for smooth cores |
| direct swing, sharp-core LIMIT / raw `|D|` measure | `0.75` (bond-shear) / `0.5–1.5` (shape) — reaches/exceeds the margin | → the fork (measure + sharpness dependent) |
| pre-stress remap (Leg C) | `T/ℓ ~ 10 k_s` DOMINATES `k_s` at yield-scale; sign = DC-dilatation-sign-dependent (SOFTENS for compressed core) | → the bulk-only wall is NOT clean regardless of the direct swing |

**Analytic lean: PROFILE-DEPENDENT (bin 3), NOT a clean bin-1.** The direct deviatoric swing is sub-half-yield for smooth physical cores (spatially separated from the axial-saturation shell) — which would support `k_a`-alone — BUT the answer flips across (a) the admissible family (smooth `0.28` vs sharp `0.75`) and (b) the deviatoric measure (bond-shear `0.28` vs shape `0.56`), AND the pre-stress remap (§4) independently DOMINATES `k_s` at the yield-scale boundary with a DC-dilatation-sign-dependent (softening-for-compression) sign. So the #773 §4(b) NOT-YET-RATIFIABLE clause (*"a pure A1 dilatation breather rails `k_a` ALONE"*) is **NOT ratifiable as stated** for the localized core — it is profile-conditional and remap-undercut. **The result doc (Legs A/B/C integrated) lands the frozen bin.**

---

> **Derivation provenance.** Grant standing derivation-class authorization (#773 §4(a)). COMMIT 2 after the prereg froze + pushed ALONE (`c35c612e`). Forms `[derived]` by exact spherical-elasticity kinematics; the load-bearing constitutive facts are `[canon]` (`master-equation.md:20`, `axiom-register.md:186/189/193`, `gravitomagnetism-frame-dragging.md:15`, `q-g22-strain-convention.md` `clm-4r4jiy`) content-verified two-method at base `3d07ceeb`; `RHO_STAR` from `constituent_cage_ensemble.py`/`ave.core.*` read-only. Mints no `clm-`/`def-`; propagates to no leaf; engine `src/ave` byte-untouched; port-register untouched. The frozen-bin verdict lands in `research/2026-07-21_boundary-strain-amplitude_result.md` after the numeric Leg B + remap Leg C. Companion: the frozen prereg, the driver `research/drivers/boundary_strain_amplitude.py`, the docket continuation `### ENTRY 2026-07-21-boundary-strain-amplitude`.
