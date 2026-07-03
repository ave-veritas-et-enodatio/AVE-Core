# FROZEN PREREG — is the Axiom-4 saturation kernel FORCED or genuinely POSTULATED?

**Date:** 2026-07-02
**Lane:** implementer (foundational / potential axiom-reduction; analysis + derivation pass, NO simulation)
**Branch:** `analysis/axiom4-saturation-forced` (off `origin/main` @ `f556dcdc`)
**Disciplines fired:** `ave-prereg`, `substrate-native-check`, `consistency-vs-emergence`
**Status at freeze:** the discriminator, the two candidate paths, and the axiom-count
consequence are locked BEFORE the verdict is written.

> **SHA-PIN.** Frozen at commit time. Any change to the discriminator, the PASS/FAIL
> criterion, or the class-tag after the verdict is known is a Rule-16 violation and must
> be a NEW prereg with its own version, not an edit here.

---

## 0. The object under test

Axiom 4 (Scheme A canonical, `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md:48-58`, label `eq:axiom4_saturation`, source `common_equations/eq_axiom_4.tex:6-9`):

$$ S(A) = \sqrt{1 - (A/A_{yield})^2}, \qquad A \in [0, A_{yield}] $$

posited as an axiom (NO claim ID; `common/claim-quality.md:805` states verbatim "the kernel
is the **postulated** Axiom 4 form"). It is the "quarter-arc / Born-Infeld form"
(`session/axiom-homologation.md:46`), the single most cross-cited operator in the corpus
(A-034 catalog, 26 instances / 21 orders of magnitude).

## 1. Grant's incisive question (the frame)

"What defines forced? **If it is forced, should it actually be an axiom?**" If the *shape*
`√(1−A²)` is derivable from more primitive structure (Axioms 1–2 + a bounded-amplitude
identification), then Axiom-4's FORM is a **theorem**, and the residual axiomatic content is
only the IDENTIFICATION that the vacuum modulus saturates (not the specific curve). The axiom
count would drop 4 → 3 + a saturation identification.

## 2. The discriminator (locked)

**A primitive constraint FORCES the kernel form iff it UNIQUELY picks `√(1−A²)` — not merely
PERMITS it among a family.** The sharp test:

- **FORCED** requires: a substrate-native primitive (norm-preservation on a genuine rotation
  DOF, OR a maximal-amplitude / Born-Infeld constraint) from which `S = √(1−A²)` follows with
  **no free exponent, no free functional choice**, and where the competing forms
  (`1−A`, `1−A²`, `(1−A²)^p` for `p ≠ ½`, `cos(πA/2)`, `e^{-A²}`, …) are **excluded** by the
  same primitive.
- **POSTULATED** verdict if: the primitive fixes only *that S is a decreasing bounded
  complement of A vanishing at A=1 with the right small-A limit* — a class the quarter-arc
  belongs to but does not uniquely occupy — OR if the "derivation" silently inserts a
  Pythagorean/quadratic norm that is itself an independent posit.

**Key sub-question (the load-bearing hinge):** the quadratic norm
`A² = ε² + κ² + V²` (`trampoline-framework.md:247,380`) already MAKES `S = √(1−A²)` a
Pythagorean complement — so the whole question reduces to: **is the quadrature (the
`Σ mode²` sum-of-squares, i.e. an L2 / energy norm) FORCED by substrate structure, or is it
itself the postulate wearing a different hat?**

## 3. What I expect (pre-registered)

Given the corpus already contains (and has already adjudicated) a Pythagorean route:

- `trampoline-analogy-primer.md:188-192`: the buckled-bond Pythagorean picture is a
  **"pedagogical correspondence, not a first-principles derivation"**; "**Axiom 4 remains
  postulated**"; the residual gate is named as Q-G47 (network-level elastic calc).
- `common/claim-quality.md:805,816`: "Does NOT derive Axiom 4 itself"; the load-bearing
  unstated step is that A is genuinely the same dimensionless object across manifestations.
- Q-G47 (`q-g47-substrate-scale-cosserat-closure.md:11-13`) closed what fixes the *operating
  point* `u_0*` where `S(A*)=0` — it uses `S(A)` as INPUT (`A*=1` boundary), it does NOT
  derive the *shape*.

**My prediction:** the verdict is **CONDITIONALLY-FORCED / GENUINELY-POSTULATED-AT-THE-NORM**.
Specifically: IF one grants (i) that A is an L2 (energy / RMS) amplitude — `A² = Σ reactive
mode²` normalized to a maximum, and (ii) that the total stored reactive amplitude is conserved
against a fixed ceiling `A_yield` (a Nyquist/bandwidth bound, Grant's own name "Nyquist yield",
`axiom-homologation.md:711`), THEN `S = √(1−A²)` is FORCED as the complementary amplitude of a
2-vector of fixed length (Pythagoras), with the exponent `½` and the power `2` both fixed by
the L2 norm — the Born-Infeld `n=2` squared limit is then a theorem, not a choice. BUT premises
(i)+(ii) are themselves the axiomatic content: the choice of an **L2 (quadratic/energy) norm**
plus a **fixed ceiling** is what does the forcing. So the reduction is real but PARTIAL — it
relocates the axiom from "the curve `√(1−A²)`" to "the amplitude is an energy-norm bounded by a
fixed ceiling." Whether that relocation counts as 4→3 is a framing call for Grant.

**Falsifier of my own expectation:** if I find a substrate-native primitive that forces the L2
norm ITSELF (e.g. energy-conservation on the bond LC tank genuinely FORCES `V_inc² + Φ² = const`
as the only admissible invariant, with no competing norm), then the reduction is FULL (4→3, form
is a theorem, only the saturation-identification stays axiomatic) — a stronger result than I
expect. Conversely, if the L2 norm is only ONE consistent choice and other norms (L1, L4) are
equally substrate-admissible, the kernel is GENUINELY POSTULATED and my "conditionally-forced"
softens to "postulated with a natural but non-unique motivation."

## 4. Two candidate paths (both to be tested)

**(A) NORM-PRESERVATION / rotational projection.** Is there a substrate quantity that IS
sin θ of a rotation/phase angle, with S its cos θ, so that `|A|² + |S|² = A_yield²` is forced
by unitary norm preservation? CHECK: the bond LC tank C-state `V_inc` ↔ L-state `Φ_link`
conjugacy (`substrate-perspective-electron.md:36-39`); the Clifford-torus `(2,3)` phase winding;
`A²_local = Σ_ports V_inc² / V_SNAP²` (`substrate-perspective-electron.md:56`). Is A_yield a
Nyquist/bandwidth ceiling making A a bounded projection?

**(B) BORN-INFELD / maximal-field geometry.** `√(1−A²)` is the unique NLED with a bounded field
strength / minimal-area (determinant) structure. CHECK: does the `ℓ_node` bandwidth limit
`A_yield` as a maximal amplitude, plus the LC-network constitutive structure, force the
Born-Infeld quarter-arc via a maximal-amplitude constraint? Is there a variational route
(Axiom 3 = min |Γ|² / S11-min action) that yields it?

## 5. Classification commitment (consistency-vs-emergence)

This is a META-classification of an AXIOM's status, not a numerical-prediction test. The
outcome will be tagged on the axis: **{FORCED-THEOREM (form demotes; count 4→3) /
CONDITIONALLY-FORCED (form is a theorem GIVEN a named sub-posit; count stays 4 but the axiom's
CONTENT is relocated/shrunk) / GENUINELY-POSTULATED (independent axiom; forms the primitives
equally permit are named)}**. Per `consistency-vs-emergence`: I must name explicitly what NEW
substrate primitive (if any) does the forcing, and NOT inflate a norm-choice into an emergence.

## 6. Lane / output discipline

- Analysis only. No solver, no engine run. Substrate-native-check applies to the PROSE
  derivation (Checkpoint 6): the norm, the ceiling, and the projection must be K4/Cosserat/LC
  native, not a Cartesian gradient-descent or continuum-Helmholtz posit.
- Flag-don't-fix: if the verdict conflicts with any canonical leaf (e.g. a leaf that IMPLIES
  the form is derived), surface both paths verbatim; do NOT reframe.
- Output: this prereg + `2026-07-02_axiom4-forced_result.md`. Surface the framing fork to Grant.
