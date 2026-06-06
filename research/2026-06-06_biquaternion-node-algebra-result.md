# Is the AVE substrate node-algebra a biquaternion? (RESULT)

**Date:** 2026-06-06
**Branch:** `analysis/2026-06-06-biquaternion-node-algebra` (worktree `AVE-Core-quaternion-wt`)
**Prereg:** [`2026-06-06_biquaternion-node-algebra-prereg.md`](2026-06-06_biquaternion-node-algebra-prereg.md) (FROZEN)
**Status:** COMPLETE — analytical derivation + symbolic/numeric consistency checks.
**Verification script:** [`src/scripts/vol_1_foundations/verify_biquaternion_node_algebra.py`](../src/scripts/vol_1_foundations/verify_biquaternion_node_algebra.py) (forward-only; constants imported per `ave-canonical-source`; no fitting to 137.036).

---

## §0 Verdict up front + scope-fence (`ave-evidence-framing`)

**Open-goal verdict (prove-or-disprove): the biquaternion is a CONSISTENCY-CLASS
re-expression, NOT the substrate's newly-discovered number system.** All three
`(e)-genuinely-new` gates (§3 of the prereg) **FAIL**:

| Gate | Question | Verdict |
|---|---|---|
| **G1** structural unification | does ONE algebra *force* closure + longitudinal + Möbius to co-occur as necessity? | **FAIL** — they co-occur in the algebra (SU(2)⊂SL(2,ℂ); scalar grade; null cone), but this is standard math over already-canonical, independently-substrate-derived facts; no new substrate primitive (`consistency-vs-emergence` Step 8b). |
| **G2** α-decomposition | does the algebra forward-derive `α⁻¹ = 4π³+π²+π`? | **FAIL** — the grades give the *dimensional skeleton* {3D,2D,1D} but generate none of the π-powers; those are Golden-Torus geometry + K4 bipartite, not algebra. |
| **G3** longitudinal discriminator | does the algebra force a NEW testable longitudinal prediction? | **FAIL** — the longitudinal/breathing 7th mode is already canonical; the algebra re-expresses *why* (Heaviside's deleted scalar) but adds no new number/dispersion/coupling. |

**Therefore: the biquaternion is canonized to nothing. It is a notation/pedagogy
aid** — an elegant unifying *language* that re-expresses the already-canonical
SU(2)/Cosserat/Hopf/4π-spinor/Γ structure in one algebra. This is the
pre-registered "most likely partial → land consistency-class" outcome (prereg §4
"Honest expected outcome"). It is a **valid, expected result**, recorded honestly
per Rule 11 (honest closure). We do **NOT** claim "we found the substrate's number
system."

**Strongest *accurate* framing (not inflated):** the single genuinely-illuminating
observation is **why *bi*quaternion and not real quaternion** — the substrate has a
reflection/saturation boundary (`|Γ|=1`, Z→∞, the `Γ=-1` TIR wall where mass forms),
and that boundary is the biquaternion **null cone** (zero divisors), which the real
(division-algebra) quaternion does not possess. This is a clean structural
*re-expression* of the canonical `Γ=-1` boundary — consistency-class, pedagogically
valuable — not new physics.

**Scope-fence:** analytical derivation only; does not touch the open/short primer
sign relabel (separate item; the sign is a Möbius convention, adjudication-pending
per `observable-battery-infrastructure-prereg.md:44`, flag-don't-fix).

---

## §1 Canonical-leaf cross-links (verified file:line)

Every piece the biquaternion re-expresses is already canonical, at its own
classification ceiling. Verified this session:

| Piece | Canonical home (verified) | Already-canonical content | Ceiling |
|---|---|---|---|
| SU(2)→SO(3) double cover = spin-½ | `finkelstein-misner-spin-half-derivation.md` §2–§5 | unit quaternions ARE SU(2); the 720°/4π closure via FM kink on the extended unknot; **§5 explicitly decomposes K4-native physics vs imported SU(2)/Pauli math** | clm-salw2h |
| (2,3) Clifford-torus winding | `torus-knot-uniqueness.md` §5–§6 | (2,3) = smallest coprime torus knot (gcd=1, both ≥2); **phase-space** Clifford-torus winding, NOT real-space | clm-8c3yhs |
| Cosserat E/B = translational/microrotational | `CLAUDE.md` INVARIANT-S2 (Axiom 1) | 3 translational→E (capacitive), 3 microrotational→B (inductive); Cosserat rotational DOF IS spin-origin | Axiom 1 |
| Volumetric / longitudinal 7th mode | `trampoline-framework.md:235–249`; `master-equation.md:16–21`; `solver-toolchain.md:395` | the breathing mode = "only mode with no rotational character"; Maxwell-Heaviside acoustic eqn; electron = trapped longitudinal wave (Γ=-1) | clm-efo113 / clm-lv3uw1 |
| 4π spinor-cycle / `α⁻¹=4π³+π²+π` | `theorem-3-1-q-factor.md:15,48,78` | THE load-bearing number; **the 4π's substrate content is "K4 bipartite lobe-count (2 sublattices)×2π"; "SU(2) double-cover" is demoted to a *standard-physics translation reference*** | clm-rtdmsn |
| Γ reflection coefficient (Möbius) | `operators.md:43` **Op3** `Γ=(Z₂−Z₁)/(Z₂+Z₁)` | universal reflection coefficient (sub-nuclear Pauli / antenna S₁₁ / Moho) | — |

> **Precision catch (flag-don't-fix):** prereg §1 labels the reflection coefficient
> "Op17." The canonical reflection-coefficient operator is **Op3** (`operators.md:43`);
> **Op17** is the *downstream* power-transmission `T²=1−Γ²` (`operators.md:57`). The
> Möbius structure lives in Op3's Γ; Op17 is built on it. Corrected throughout this doc.

---

## §2 Construction of the biquaternion node-algebra (Task 1)

### §2.1 The algebra

A **biquaternion** is `ℍ⊗ℂ` — a quaternion with complex coefficients:

$$q = w + x\,\mathbf{i} + y\,\mathbf{j} + z\,\mathbf{k}, \qquad w,x,y,z \in \mathbb{C} = \{a + b\,\iota\}.$$

Two imaginaries that must be kept distinct:
- `i, j, k` — the **quaternion** units (the rotation/spin sector): `i²=j²=k²=ijk=−1`, non-commutative (`ij=k`, `ji=−k`).
- `ι` — the **complex** unit (`ι²=−1`), **central** (commutes with `i,j,k`).

Eight real components: a **complex scalar** `w` (2) + a **complex 3-vector** `(x,y,z)` (6).

**Multiplication** is Hamilton's product on `{i,j,k}` with complex coefficients; verified to close (C1):
`i²=j²=k²=−1`, `ij=k`, `jk=i`, `ki=j`, `ji=−k`, and `ij≠ji` (non-abelian).

**Three conjugations** (each an involution):

| Conjugation | Action | Fixes | Negates |
|---|---|---|---|
| quaternion `q*` | `w − xi − yj − zk` | scalar `w` | vector `(x,y,z)` |
| complex `q̄` | `ι → −ι` in all coeffs | `i,j,k` | the `ι` part of each coeff |
| total (biconj) `q̄*` | both | — | — |

**Complex norm** `N(q) = q q* = w²+x²+y²+z² ∈ ℂ` — multiplicative (`N(pq)=N(p)N(q)`, verified C1) but
**NOT positive-definite** (it is complex-valued). This is the load-bearing structural
difference from the real quaternion: `N(q)=0` has nonzero solutions (the **null cone** /
zero divisors, C5) — e.g. `N(1+ι\,i)=1+ι²=0`. The real quaternion `ℍ` is a division
algebra (no zero divisors); the biquaternion `ℍ⊗ℂ` is not.

**Isomorphisms** (all standard math): `ℍ⊗ℂ ≅ M₂(ℂ)` (2×2 complex matrices) `≅ Cl(3,0)`
(the Pauli/geometric algebra of 3-space). The verification script uses the `M₂(ℂ)`
representation `1↦I, i↦[[ι,0],[0,−ι]], j↦[[0,1],[−1,0]], k↦[[0,ι],[ι,0]]`, under which
`N(q)=det`.

### §2.2 The proposed substrate map (prereg §2) — and which 8-decomposition

The node carries **7 DOF + charge = 8** (`trampoline-framework.md:235–249`): 3 translational
`u` + 3 microrotational `ω` + 1 volumetric breathing + charge. The prereg §2 map:

| biquaternion slot | substrate DOF | sector |
|---|---|---|
| complex 3-vector `F = E + ι B` (6) | translational `u` (E, capacitive) + Cosserat `ω` (B, inductive) | the (E,B) reactive pair |
| real scalar `Re(w)` (1) | volumetric breathing (longitudinal 7th mode) | the scalar/acoustic mode |
| imaginary scalar `Im(w)` (1) | charge = topological winding (Axiom 2, `[Q]≡[L]`) | the spare slot |

Two **distinct** natural 8-decompositions of the same algebra — worth separating cleanly:

- **(a) Coefficient framing (prereg §2):** complex-scalar `w` ⊕ complex-vector `(x,y,z)`.
  `F = E + ιB` is the complex 3-vector; `E = Re`, `B = Im` of the `{i,j,k}` part.
- **(b) Geometric-algebra grading `Cl(3)`:** scalar(1) ⊕ vector(3) ⊕ bivector(3) ⊕ pseudoscalar(1).
  Here the pseudoscalar `ι = e₁e₂e₃` **is** the central complex unit, so `F=E+ιB`
  automatically gives `B` its axial/bivector character (`ι·vector = bivector`). This is the
  geometrically-honest statement of the canonical Cosserat split (INVARIANT-S2): the
  **translational(E, polar/vector) vs microrotational(B, axial/bivector)** distinction =
  the **vector-vs-bivector grade** split, with `ι` (pseudoscalar) the operator relating them.

### §2.3 substrate-native-check (honesty gate on the construction)

The construction is a prose-derivation of an algebra mapped onto the substrate — `substrate-native-check`
trigger 6 fires. The checkpoints, walked:

- **The substrate's 7 modes are NOT generated by the algebra.** They come from K4 + Cosserat
  **micropolar DOF counting** (Axiom 1: 3 translational + 3 microrotational; + the volumetric
  bubble compliance; + charge as winding, Axiom 2). The biquaternion's 8 real components can
  *host* `7+charge`, but the **match is a consistency** (the algebra has room for the modes),
  **not a derivation** of why the substrate has them. Imposing `Cl(3)` top-down and declaring
  "therefore 7 modes" would be exactly the SM/QED-style algebra-first leak the discipline guards.
- **Sector identification is honest:** `F=E+ιB` lives in the (V,Cos) field sectors (real-space /
  field-space), NOT in `(V_inc,V_ref)` phase-space — see the coordinate caveat carried into §3.
- **`ave-ee-first-mapping` (prereg §5, already fired):** EE (Z, Γ, windings) is the measurement
  language; the biquaternion is the rotation-group/longitudinal language **under** it —
  complementary, not a replacement.

**All algebraic claims in this section verified** (C1, C4, C5) in
`verify_biquaternion_node_algebra.py`. The construction is sound; the question of whether it is
*more than notation* is the G-gate (§7).

---

## §3 T1 — closure: does unit-quaternion/SU(2) recover 720°/(2,3)/spin-½?

**Result: YES for the 720°/spin-½ double cover (consistency-class); the (2,3) is a
SEPARATE phase-space fact that unit-closure does NOT force.**

### §3.1 The 720° double cover — recovered (consistency)

The **real** unit quaternions are exactly `SU(2)`. A rotation by `θ` about `x̂` is
`U = cos(θ/2) + sin(θ/2)\,i`; verified (C2):
- `U†U = I` (unitary — it IS SU(2)),
- `θ=2π → U = −I` (sign flip — the spin-½ signature),
- `θ=4π → U = +I` (the 720° closure),
- `det U = 1` (places it in `SL(2,ℂ)`; `SU(2)` is the real, unitary subgroup).

This **reproduces** the canonical Finkelstein–Misner result exactly. Per
`finkelstein-misner-spin-half-derivation.md` §2–§5, the 4π/720° double cover is
K4-native (FM kink on the extended `0₁` unknot; group chain `K₄→A₄→2T⊂SU(2)`), and
**§5 already decomposes** "K4-native physics vs imported SU(2)/Pauli math." The
biquaternion's unit-closure is the **same SU(2)**, in quaternion notation.

### §3.2 The (2,3) is phase-space — NOT forced by unit-closure (`phase-space-coordinate-check`)

> **Flag-don't-fix — coordinate-discipline catch.** Prereg §2 writes "unit-quaternion
> closure = SU(2) = the spin-½ / **(2,3)** / 720° double cover," bundling three things as
> one. The canonical leaves keep them in **different coordinate systems**:
>
> - The **720°/spin-½** double cover lives in **real space** — the FM kink on the unknot
>   defect embedded in the 3D K4 substrate (`finkelstein-misner` §9: *"this derivation
>   lives in real-space coordinates"*).
> - The **(2,3)** lives in **phase space** — the Clifford-torus winding `T²⊂S³⊂ℂ²` of the
>   bond-pair LC tank (`torus-knot-uniqueness` §"Note on real-space vs phase-space";
>   `finkelstein-misner` §9: *"the (2,3) winding … lives in phase-space coordinates"*).
>
> Unit-quaternion closure recovers the real-space `SU(2)` double cover (720°) **and**
> provides the `S³` stage on which phase-space torus knots live (the quaternionic Hopf map
> `S³→S²`). But it does **not select (2,3)**: that selection is the coprimality +
> minimality argument of `torus-knot-uniqueness.md` (gcd=1, both windings ≥2, smallest
> `p+q`), a knot-theoretic fact about curves on the torus, **not** a consequence of the
> quaternion algebra. **Conflating the real-space 720° with the phase-space (2,3) under
> "SU(2) closure" is a coordinate-category error.** The honest statement: unit-closure ⟹
> 720° (real-space); (2,3) is a separate phase-space minimality result the algebra hosts
> but does not derive.

### §3.3 Classification (`consistency-vs-emergence`)

**T1 = Class C / consistency-class re-expression.** `consistency-vs-emergence` Step 8:
the canonical source (`finkelstein-misner`, clm-salw2h) already carries the SU(2)
double cover, and **§5 explicitly tags SU(2)/Pauli as imported math language** over
K4-native physics. The biquaternion adds **no new substrate primitive** — no new axiom
invocation, no new substrate-derivation of the double cover, no new discriminator. Per
Step 8c, classification **stays at the canonical ceiling (clm-salw2h)**; the quaternion
is a re-notation. **T1 does NOT pass any G-gate.**

---

## §4 T2 — longitudinal: is the scalar part = Maxwell's deleted scalar = the 7th mode?

PENDING.

---

## §5 T3 — Möbius: is Γ the SL(2,ℂ)/biquaternion action on the reflection sphere?

PENDING.

---

## §6 T4 — α-structure (G2 test): vol/surf/line + 4π-spinor, forward only

PENDING.

---

## §7 Classification + the explicit G1/G2/G3 verdict

PENDING.

---

## §8 Discrimination-check on T2 (`ave-discrimination-check`)

PENDING.

---

## §9 Discipline-fired log + honest closure

PENDING.
