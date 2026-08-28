---
id: bias-to-index-photoelastic-map
title: "Op19 converts strain to index with a strain-per-strain ratio -- the rank-4 photoelastic tensor that would do the job is unnamed in the corpus"
status: OPEN
owner: unassigned
opened: 2026-08-27
source: manuscript/ave-kb/common/operators.md
anchor: "(settled A1 strain = index)"
---

Surfaced by the `L3-constitutive-map` lane; the sign arithmetic below was
re-derived independently by the `two-knob-gravity-repair` lane. **This is the
runner-up to `2026-08-27-two-knob-constitutive-forcing` and is the bigger of the
two.** Every `O(m)` gravity number in the corpus runs through this step.

**The step.** `operators.md`:59 carries Op19, `n(r) = 1 + ν_vac·ε₁₁`, status
**CANONICAL**, classified at `:123` as *"BC (settled A1 strain = index)"*. The
2026-08-11 gravity-linearity audit licenses it verbatim as *"Poisson-ratio
kinematics … a **kinematic ratio** (transverse strain per longitudinal strain),
**not a modulus**. Kinematic ratios are linear by construction; the kernel grades
moduli, not kinematics."*

**A strain-per-strain ratio lives entirely in the mechanical sector and carries
no information about how strain grades ε or μ.** The object that performs that
conversion in every real solid is the rank-4 photoelastic tensor,
`δ(ε⁻¹)_ij = p_ijkl·e_kl`, with three independent constants `(p11, p12, p44)` on
a cubic lattice. **The corpus has never named, derived, measured or bounded it**
— F-B4 at `research/2026-07-31_anisotropy-observable_scoping.md`:657, verified
three ways by its own author including `git log -S` over all of `origin/main`;
independently reproduced by two later lanes (4 files, all research/orchestration
scoping docs; **none in `manuscript/` or `src/`**).

**L3's sharpest sentence:** *"the audit asked whether the LINEARITY is licensed
and correctly answered yes; it did not ask whether the strain-to-INDEX conversion
is licensed, and that conversion is the missing object."*

**Three structural results that constrain any future map.**

1. **Ax3's boundary form FORCES `Z(x) = Z₀`**, hence `ε_ij ∝ μ_ij` as tensors.
   L3 then computed the Fresnel determinant of exactly that medium from Maxwell
   and it factors as a **perfect square** ⇒ **no gravitational birefringence at
   any order**, and the optical metric **emerges** as the inverse principal
   symbol of the wave operator. *Credit where due: this is a real derivation
   from a non-GR premise and it is machine-checkable; GR gets the same fact from
   the equivalence principle, which is not.* Caveat carried: Ax3's boundary form
   is canon-flagged *"ASSERTED — an underived dynamics leg"*.
2. **Cubic symmetry does not make the deflection isotropic for free.** A cubic
   point group protects rank-2 exactly and rank-4 not at all. The missing
   `p_ijkl` gives an isotropic `O(m)` deflection **iff `p11 − p12 = 2p44`**;
   otherwise light bending carries a **quadrupole relative to the substrate
   crystal axes** — a clean sidereal falsifier nobody has written down.
3. **A mechanical strain can never be the answer.** A static spherically
   symmetric displacement has `e_rr = u'`, `e_tt = u/r`; hydrostatic iff
   `u ∝ r`, which a localised source cannot produce. GR's `γ_PPN = 1` spatial
   sector in isotropic coordinates **is** exactly hydrostatic. And Ax5 clause G's
   bound response is `u ∝ 1/r²` (canon's own words), giving `1/r³` strain — **two
   powers too fast to source a Newtonian potential.** So no improved strain field
   will fix it; the fix **has** to be a constitutive grading.

**Aggravating: the axioms alone give O(A²), not O(A).** Ax4's kernel `√(1−A²)` is
**even**, so any `X = X₀S^p` is quadratic-leading and contributes nothing at
`O(GM/c²r)`. Solar-limb deflection from Ax4 alone: `3.58e-5″` (A = ε₁₁) or
`2.92e-6″` (A = r_s/r) against `1.75″`. And the 2026-08-11 audit already ruled
`graded-network-response.md`:147 *"UNLICENSED as a gravity index"* — **so the
gravity sector has formally disowned its only axiom-connected constitutive law
and put nothing in its place.** That consequence has not previously been stated.

**A flag, recorded one notch weaker than L3 stated it.** `double-deflection.md`
uses **opposite** strain→index sign conventions in two rows of one derivation:
`:22`-`:24` matter row is `n − 1 = +θ/3 = +(1/7)χ_vol` (verified in sympy:
`e_rr = 7m/r`, `e_tt = −2m/r`, `θ/3 = m/r` exactly), while `:28` light row is
`n − 1 = ν_vac·χ_vol = −e_tt`. L3 calls this a contradiction. **It is weaker than
that:** a genuine rank-4 `p_ijkl` *can* carry opposite signs on `p11` and `p12`,
so this is not automatically fatal — it is evidence that a single scalar Poisson
projection cannot be the map, which is L3's own conclusion reached from the other
side. Flag-don't-fix: no leaf touched.

**Fitting rather than deriving gives `p11 = −1/9`, `p12 = −4/9`** — two
parameters fitted to two data points, zero predictive content at `O(m)`. L3
flagged that itself.

**Suggested next step (unassigned, un-scoped).** Write `p_ijkl` explicitly with
the cubic symmetry of the ratified `z=3` srs carrier, count how many of its three
constants survive the Ax3 `Z = Z₀` constraint, and check that count against the
available observables. Result (2) already supplies one hard condition and one
falsifier for free.
