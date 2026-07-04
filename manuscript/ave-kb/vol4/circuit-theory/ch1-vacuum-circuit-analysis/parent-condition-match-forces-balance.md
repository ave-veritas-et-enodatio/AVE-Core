[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-mfb2ax]
-->

## The Parent Condition: Axiom 3 Forces the Isotropic-Bond Point $k_s=k_a$

The photon's emergent-Lorentz operating point — the isotropic-bond ratio $k_s=k_a$ on the chiral
**srs-z3** net at which the transverse light-cone is isotropic — is **not a hand-chosen locus**. It is
a **consequence of Axiom 3** (the Minimum Reflection Principle, boundary form:
[`../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md):48).
Minimising the srs net's **internal-boundary acoustic reflection** $\Gamma_{internal}(\rho_{bond})$
over the bond-stiffness ratio $\rho_{bond}=k_a/k_s$ lands on $\rho_{bond}=1$ ($k_s=k_a$) knob-free,
so the three "transparencies" the corpus tracked separately — the **MATCH** (achromatic
$\varepsilon\mu$), the **BALANCE** (axial↔shear elastic isotropy), and the **HEAVISIDE**
(distortionless-line) condition — are **one parent condition co-locating at $\rho_{bond}=1$**.

> **Classification (do NOT lift).** **[MECHANISM-DERIVED / axiom-manifestation class — FORM not
> VALUE].** This leaf derives the **FORM / pinning** of the operating point (that $k_s=k_a$ is an
> Axiom-3 consequence, not an engineering choice); it derives **no VALUE**. It mints **no** new
> dimensionful constant and makes **no** emergence claim about $Z_0$'s or $\alpha$'s value (both
> enter only by symbol). The ½/¼ knife PASSES: no tuned $\rho_{bond}^\ast$ is supplied — the ratio
> 1 falls out of an unseeded golden-section minimiser.

> **Derivation provenance.** The full derivation — the knob-free minimiser, the MATCH/BALANCE/HEAVISIDE
> co-location, the instrument's genuine-reflection control, and the independence control — is recorded
> in [`research/2026-07-04_parent-condition-match-forces-balance_result.md`](../../../../../research/2026-07-04_parent-condition-match-forces-balance_result.md)
> ([MECHANISM-DERIVED]); driver `src/scripts/vol_4_engineering/parent_condition_match_forces_balance.py`;
> test `src/tests/test_parent_condition_match_forces_balance.py` (9 pass). The photon-at-$k_s=k_a$
> arc this derivation upgrades is [`research/2026-07-04_lorentz-on-srs_result.md`](../../../../../research/2026-07-04_lorentz-on-srs_result.md).

## §1 — The theorem: $|\Gamma|^2$-min at the internal acoustic boundary forces $k_s=k_a$

Axiom 3's boundary form states that the substrate minimises the reflection coefficient $|\Gamma|^2$
at **every** internal impedance boundary $\partial\Omega$. Applied to the srs net's **internal
acoustic (elastic) boundary**, the minimand is $\Gamma_{internal}(\rho_{bond})$ as a function of the
stiffness ratio $\rho_{bond}=k_a/k_s$ (axial stiffness $k_a$, transverse/shear stiffness $k_s$ of the
RANK-2 bond tensor $\Phi_b = k_a\,\hat d\otimes\hat d + k_s\,(\mathbf I - \hat d\otimes\hat d)$).

> **[Resultbox]** *The isotropic-bond point is the Ax3 $|\Gamma|^2$-minimum.*
>
> An unseeded golden-section minimiser over $\rho_{bond}$ lands on $\rho_{bond}=1$ ($k_s=k_a$) **to
> machine precision** ($\rho^\ast = 0.99999999$, $\Gamma_{min}=1.5\times10^{-8}$), **KNOB-FREE**.
> The functional genuinely measures reflection (V1 reads $\Gamma_{internal}=1.5\times10^{-8}$ on the
> isotropic control $k_s=k_a$, and $9.3\times10^{-2}$ on the anisotropic control $k_a=2k_s$ — it SEES
> anisotropy), so the ratio-1 landing is physics, not a blind functional.

This is the substrate reason the photon's emergent-Lorentz light-cone sits where it does: $k_s=k_a$
is the **unique point where the substrate's internal-boundary acoustic reflection vanishes**. Cold
birefringence, dispersion, and anisotropy are forbidden at the SAME point by the SAME axiom.

## §2 — MATCH / BALANCE / HEAVISIDE are one parent condition

The three "transparencies" the corpus tracked as separate conditions all minimise at $\rho_{bond}=1$
to a spread of $4.75\times10^{-8}$ (all four loci — the achromatic $\varepsilon\mu$ **MATCH**, the
photon-branch isotropy **BALANCE**, the distortionless **HEAVISIDE** line, and the Zener-$A=1$ point
— co-locate at $\rho=1$ to 7 digits). They are **one parent condition**, not a coincidence of three:

| Child condition | Sector | Statement at $\rho_{bond}=1$ |
|---|---|---|
| **MATCH** (achromatic) | transverse-EM | $\varepsilon=\mu$ symmetric scaling / $Z_0$-invariance, $\Gamma_{EM}=0$ |
| **BALANCE** (bond-isotropy) | translational-elastic | axial↔shear stiffness equal ($k_s=k_a$), the isotropic light-cone |
| **HEAVISIDE** (distortionless) | line | the distortionless-transmission condition of the graded LC line |

The EM **MATCH** and the elastic **BALANCE** are the **transverse-EM** and **translational-elastic**
faces of the same Axiom-3 minimum — different sectors, one principle: each is the operating point
where the internal-boundary reflection vanishes. (Sibling links: §5.)

## §3 — Honest flag: the photon point is lossless-reactive (K<0), not a static solid

The match point $\rho_{bond}=1$ is mechanically **UNSTABLE** (bulk modulus $K<0$, per the
`srs-elastic-tensor` result $K<0$ for $\rho<2$). The photon's zero-reflection point is a
**lossless-reactive operating point** for the transverse photon, **NOT** a stable static elastic
solid. This is consistent and expected (the substrate is a reactive LC medium, not a load-bearing
crystal at the photon point) — but it means the **PHOTON point and the MATTER point are genuinely
DIFFERENT loci**:

| Locus | $\rho_{bond}$ | mechanical $K$ | physical role |
|---|---|---|---|
| **PHOTON** (Ax3 match) | $1.0$ | $K<0$ (unstable) | the transverse photon's zero-reflection light-cone |
| **MATTER** ($\nu=2/7$ / $K=2G$) | $\approx 9.77$ | $K>0$ (stable) | the GR-imported matter Poisson operating point |

The photon rides the transparent point (Ax3 forces it there); the matter sector sits at a different,
mechanically-stable $\rho^\ast$ where the substrate can store static strain (and where it internally
reflects, per the $\Gamma=-1$ particle-core canon).

## §4 — Post-#521 state: the matter locus is reached model-scoped, value still imported

A follow-on arc ([SAME-TENSOR-POINT], PR #521) tested whether the two loci above connect under
saturation. The canon-forced composition $\rho_{eff}=\rho_{cold}\cdot(S_{axial}/S_{shear})$ (with
$\rho_{cold}=1$, this leaf's Ax3-forced point) stiffens $\rho_{eff}$ off the photon point under
asymmetric shear-channel loading, and the **saturated small-signal Born-Huang tensor is the cold
tensor with $\rho\to\rho_{eff}$** (homogeneous degree-1 map ⇒ dimensionless ratios degree-0), so
driving $\rho_{eff}$ to $9.7734$ DOES land the same cold $\nu=2/7$ / $K=2G$ tensor.

- **The cold-vs-saturated tensor gap CLOSES — MODEL-SCOPED** to the small-signal swapped-springs model
  (cold tensor with each bond spring softened by its per-channel $S(A)$ at FIXED geometry).
- **RESIDUAL STAYS OPEN:** initial/residual (pre-)stress from bias pre-loading and bias-induced
  geometry change are OMITTED and remain OPEN (§ MODEL SCOPE of the saturated result).
- **VALUE GRADE UNCHANGED:** [SAME-TENSOR-POINT] is a CONSISTENCY finding, **NOT** a value derivation —
  the matter value $\rho^\ast\approx9.77$ / $K=2G$ stays **GR-imported** (PR #506 / PR#261), reached at
  the canon-undistinguished free-knob crossing $A_{wall}=0.99479$ (not $\sqrt\alpha$, not $1-\alpha$,
  not the $A\to1$ yield wall).

Provenance: [`research/2026-07-04_saturated-elastic-tensor_result.md`](../../../../../research/2026-07-04_saturated-elastic-tensor_result.md)
(VERDICT BOX + § MODEL SCOPE).

## §5 — Sibling conditions (same Ax3 parent, different sectors)

- [`../../../vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md`](../../../vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md)
  (clm-rd9cjm) — the transverse-EM **MATCH** face ($\varepsilon=\mu$ / $Z_0$-invariance, $\Gamma_{EM}=0$).
- [`z0-derivation.md`](z0-derivation.md) — the $Z_0$ / $\Gamma=0$ EM face at the circuit layer.
- [`../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md):48
  — the parent Axiom 3 (Minimum Reflection Principle, boundary form).

## §6 — Falsification scope

- **FALSIFIES this leaf:** a demonstration that the srs internal-boundary $|\Gamma|^2$-minimum lands
  at a $\rho_{bond}\ne1$ (i.e. that the isotropic-bond point is NOT the Ax3 reflection minimum), or
  that a tuned $\rho_{bond}^\ast$ had to be supplied for the ratio-1 landing (the ½/¼ knife).
- **DOES NOT bear on** the matter VALUE $\rho^\ast\approx9.77$ (GR-imported; a separate locus) nor on
  the weak-C no-zone-edge $(q\ell)^4$ dispersion theorem (gate `wejkhvnfb`, OPEN) — this leaf derives
  the isotropy/MATCH pinning, not the zone-edge decoupling.

---

> **Quality, depends-on, and solidity for `clm-mfb2ax` live in the volume claim register**
> ([`../../claim-quality.md`](../../claim-quality.md)).
