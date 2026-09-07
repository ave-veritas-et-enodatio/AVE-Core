---
id: eps11-four-objects
title: "eps_11 is four objects across canon, and Op19 contracts a non-strain with a Poisson ratio"
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-27
source: manuscript/common_equations/eq_axiom_5.tex
anchor: "DISTINCT object from mechanical strain"
---

**ROUTED-TO-GRANT. This item supersedes nothing and rules nothing. Only Grant rules.**

Basis: [`research/2026-08-27_ppn-tensor-derivation_result.md`](../../research/2026-08-27_ppn-tensor-derivation_result.md) §3–§5.
Surfaced while working the PPN chain; **independent of the PPN verdict**, which is blind to which object `eps_11` is (result doc §4, last paragraph).

**⚑ Attribution corrected 2026-09-06.** Consequence 2 below, and its heading, previously credited **R55** with declaring `eps_11` not-an-elastic-strain. R55 does not say that: R55 §3, ratified consequence 2, verbatim (`_orchestration/docket-entries/2026-08-24-ruling-r55-axiom5-source-law.md`:125-126) is *"No renaming of the object, only re-grading of its container."* The naming is R43+R50, the distinctness is R48's un-adjudicated walk note, and **the finding itself is unchanged** — only the authority credited for it.

## The question

**What kind of object is `eps_11`?** Canon carries four incompatible answers at HEAD, all live, each load-bearing for something.

| object | what it is | sites (verified on `a3f4fef7`) |
|---|---|---|
| **A** | a principal **component** of a rank-2 strain tensor | `gordon-optical-metric.md`:20 *"1D principal radial polarisation strain"* · `transverse-refractive-index.md`:14 *"principal radial tensile strain"* · `temporal-spatial-lattice-decomposition.md`:14 *"The principal radial strain"* · `eq_gravity_derived.tex`:50 (same sentence) |
| **B** | a **volumetric trace** | `double-deflection.md`:22, :28, :42 (`chi_vol`, with `chi_vol(r) = 7GM/c^2r`) · `vol3/claim-quality.md`:1141 |
| **C** | a **scalar** solving a scalar Poisson equation | `gordon-optical-metric.md`:25 · `eq_axiom_5.tex`:76 (clause G) |
| **D** | a **potential**, explicitly NOT mechanical strain | `eq_axiom_5.tex`:45 *"eps_11's canonical name is THE BIAS"* · `:73` *"the bound sector's potential"* · `:146` *"non-circular only if the bias eps_11 is a DISTINCT object from mechanical strain (grad u)"* |

**METHOD, and its limit.** These are the sites this lane opened and read (result doc §10 lists the twenty files read end to end and the patterns searched, cross-run under two grep binaries). **A statement about that search, not about the corpus.**

## Three consequences, each verified

### 1. A and B disagree by exactly 3/7

Canon's own trace formula, `one-seventh-impedance-projection.md`:13:

> `Isotropic Projection = (1/3) theta = (1/3)(3/7 eps_11) = (1/7) eps_11`

i.e. **`theta = (3/7) eps_11`**. So the volumetric trace is `3/7` of the principal component — yet `double-deflection.md`:42 sets `chi_vol(r) = 7GM/c^2r`, the same value canon gives `eps_11`. Every coupling written against `chi_vol` is a factor `7/3 ≈ 2.33` from the same coupling written against `eps_11`. Canon writes both spellings and equates the numbers. `double-deflection.md`:24 shows the collision inside one sentence: *"the projection a 1D uniaxial stress makes onto the isotropic spherical bulk tensor (1/3) theta delta_ij"* — the argument is **named** volumetric and **used** as the uniaxial component.

### 2. Op19 applies an elastic Poisson contraction to an object canon's own walk note records as possibly not an elastic strain

`operators.md`:59, status **CANONICAL**: `n(r) = 1 + nu_vac * eps_11`. `nu_vac` is literally the ratio of transverse to axial **strain** (`vacuum-poisson-ratio.md`:13), and `transverse-refractive-index.md`:16 uses it as exactly that: `h_perp = -nu_vac * eps_11`. Under object **D** — the R43+R50 vocabulary block (`eq_axiom_5.tex`:40, :45) plus R48's non-circularity walk note (`:145-149`), all three anchor lines last written 2026-08-10 in commit `a00eda3c`; **not R55**, whose 2026-08-24 name clause reads *"No renaming of the object, only re-grading of its container"* (`_orchestration/docket-entries/2026-08-24-ruling-r55-axiom5-source-law.md`:125-126) and whose consequence 4 reads *"Content untouched"* (`:131`) — `eps_11` is a *potential whose gradient is the displacement*, so applying a strain-to-strain relation to it is a category error. **Grade, stated plainly: the walk note is conditional (*"non-circular **only if** …"*) and self-marked *"recorded not adjudicated."* Nothing in canon RULES that `eps_11` is not a strain — which is part of why this item is routed rather than resolved.** The same applies to the `1/7` isotropic projection at `one-seventh-impedance-projection.md`:13.

### 3. If `eps_11` WERE a mechanical strain, there would be no gravity on matter at all

Verified symbolically (result doc §3). `sympy.dsolve` on the spherically symmetric Navier equation returns the complete exterior solution space `u(r) = C2*r + C1/r^2`, giving `eps_rr = C2 - 2*C1/r^3`, `eps_tt = C2 + C1/r^3`. Three consequences:

- **`1/r` is not in that space.** A `1/r` strain is not a static-elastic solution around a point source at any moduli.
- **`lambda` and `mu` drop out entirely** — the free symbols of the strain solution intersected with `{lambda, mu}` is empty — so the exterior anisotropy ratio is `eps_tt/eps_rr = -1/2` **independent of nu**, and no `nu`-dependent `/7` projection can arise from exterior elasticity at any coefficient.
- **The decaying branch is exactly trace-free**: `theta = -2B/r^3 + 2B/r^3 = 0`. An exterior static elastic field around a point source is volume-preserving. So the `1/7` isotropic projection of a genuine elastic field is **identically zero**, `n_scalar` would be `1` exactly, and matter would not fall.

Clause G's own bound response `u_0 = -A_g grad(eps_11) = 7 A_g GM/(c^2 r^2)` **is** an exact solution of that Navier equation (residual identically `0`, checked) — it is the `B/r^2` branch. Its strain is a genuine anisotropic tensor with ratio exactly `-1/2`. But it falls as `1/r^3`, tidal order, and **cannot source a `1/r` metric coefficient at any coupling** — a scaling statement, so no choice of `A_g` rescues it.

## Why this is not just bookkeeping

`eq_axiom_5.tex`:145-149 already records the non-circularity observation, *"as an observation with its routing, not as a finding"*, and R48's `A_g = c*l_node^2` 57-order miss is cited there as **evidence for** the distinctness. **Consequence 3 above is an independent second piece of evidence for the same distinctness, from a different direction: not "one object would have made `A_g ~ l_node^2` work", but "one object would have made gravity on matter vanish."** That strengthens D — and D is precisely the reading under which Op19 and the `1/7` projection are ill-formed.

## What a ruling would have to settle

- Are **A** and **B** the same object? If yes, which value is right and which sites carry the `3/7`? If no, `chi_vol` and `eps_11` need distinct symbols.
- Under **D**, what licenses `nu_vac * eps_11` and `theta/3` from `eps_11`? A potential has no Poisson ratio. Either a bridge is owed, or the contractions are relabelled as phenomenological couplings that merely *happen* to be numerically `2/7` and `1/7`.
- Is **C** the definition and A/B/D descriptions of it? That reading is self-consistent — `eps_11` is *defined* by its elliptic equation and the Poisson-ratio language is analogy — but it means the `/7` family's elastic provenance is decorative, and `nu_vac = 2/7` would then be a fitted coupling rather than a material constant.

**This lane takes no position.** No canonical file was edited.

## Open, adjacent, not merged into this item

`eq_axiom_5.tex`:98 names **the bias propagation theorem** as this law's STANDING DEBT — clause G's elliptic solve is instantaneous by construction and *"the `(u,pi)` no-signalling theorem does NOT cover the bias read"*. That debt and this item are both about `eps_11`'s ontology and may be one question; recorded rather than assumed.
