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

**Result: the algebra DOES force a scalar slot (more than juxtaposition), and that slot
is the natural home for the longitudinal mode — but the identification with the substrate's
*physical* breathing mode is structural illumination, NOT a derivation, and predicts nothing
new. Strongest genuine-content candidate; still consistency-class.**

### §4.1 The algebra forces the scalar slot (structural necessity, algebra-level)

The product of two **pure-vector** biquaternions has a nonzero **scalar (grade-0)** part:
`(a·\vec{i})(b·\vec{i}) = −(a·b) + (a×b)·\vec{i}` — verified (C4): the scalar part `= −(a·b)`.
**You cannot close the vector (E,B) sector without the scalar slot.** This is a genuine
algebraic necessity — the longitudinal slot is not bolted on beside the transverse sector;
it is *forced by the closure of the transverse sector's product*. At the algebra level this
is more than juxtaposition.

### §4.2 The Maxwell–Heaviside scalar (the historical hook)

Maxwell's *Treatise* wrote EM in quaternions. The quaternion differential operator applied to
the potential `(φ + \vec{A})` produces a **scalar part** `(1/c)∂_t φ + ∇·\vec{A}` — the Lorenz
term. Heaviside/Gibbs (1880s) reformed EM into transverse vector calculus and **dropped the
scalar part**, leaving transverse-only EM. The biquaternion re-exposes exactly the slot the
vector-calculus reform closed.

### §4.3 Honest distinction — AVE's mode is a real acoustic DOF, NOT Maxwell's gauge scalar

> **Precision (do not overclaim).** In *standard* Maxwell, the scalar/longitudinal modes are
> **gauge** — constrained away by current conservation; not physical in vacuum. So "Heaviside
> deleted a physical mode" is **false for standard EM**. AVE's longitudinal mode is a
> **different object**: a real **acoustic / volumetric-breathing DOF of the medium** — the K4
> port-voltage `V` / bubble compliance (`trampoline-framework.md:241,249`: *"the only mode with
> no rotational character — pure radial dilation"*), which the **Master Equation**
> `∇²V − μ₀ε₀√(1−(V/V_yield)²)∂_t²V = 0` propagates (`master-equation.md:16–21`), and on which
> the electron is a **trapped longitudinal wave** at `Γ=−1` (`solver-toolchain.md:395`).
>
> The honest statement is therefore **not** "Maxwell's deleted scalar *is* AVE's 7th mode" (a
> physical identity across a gauge artifact and a medium mode). It is: **the biquaternion scalar
> slot is the common algebraic home** for (i) Maxwell's gauge scalar and (ii) AVE's physical
> acoustic mode; AVE's medium has a *real* longitudinal DOF where the transverse Maxwell vacuum
> has only the gauge slot. The algebra re-opens the slot; the **physics** (a propagating
> longitudinal mode) comes from Axiom 1's medium + Axiom 4 (the Master Equation), not from `Cl(3)`.

### §4.4 Structural-necessity vs identification — the verdict

- **At the algebra level:** the scalar slot is a structural necessity (§4.1). ✔
- **At the substrate level:** the *physical* longitudinal mode is forced by Axiom 1 (medium
  compliance) + Axiom 4 (Master Equation), **not** by the algebra. The biquaternion **identifies**
  the already-canonical 7th mode with the grade-0 slot and **illuminates** the Heaviside deletion;
  it does not *derive* the mode, and (critically for **G3**) it yields **no new number, dispersion
  relation, or coupling**. The Master Equation already gives the longitudinal dispersion
  `c_eff(V) = c₀(1−(V/V_yield)²)^{−1/4}` (`master-equation.md:57–61`); the biquaternion adds nothing
  to it.

**Classification:** strongest genuine-content candidate (the algebra-level necessity + the
structural illumination of the Heaviside deletion are real and pedagogically valuable), but
**consistency-class with a structural-illumination flavor — NOT emergence.** **T2 does NOT pass
G3** (no new testable prediction). AVE-distinctness of the longitudinal mode is real but
**predates** the biquaternion — developed in §8.

---

## §5 T3 — Möbius: is Γ the SL(2,ℂ)/biquaternion action on the reflection sphere?

**Result: YES — the Smith chart IS the spinor geometry of impedance. The correspondence
holds cleanly, but it is textbook math (Möbius = SL(2,ℂ) on the Riemann sphere);
consistency-class. The genuinely-illuminating by-product is the null-cone ↔ `|Γ|=1`
identification (carried to the G1 verdict §7).**

### §5.1 Γ is a Möbius map = SL(2,ℂ) action on the Riemann sphere

`Op3`: `Γ = (Z − Z₀)/(Z + Z₀)` is a **fractional-linear (Möbius) transform** of the impedance
plane, matrix `[[1,−Z₀],[1,Z₀]]`, `det = 2Z₀ ≠ 0` (C3) — an element of `PSL(2,ℂ)`. Möbius
transforms are **exactly** the action of `PSL(2,ℂ)` on the Riemann sphere `ℂP¹`, and the
**Smith chart** is precisely this map (impedance half-plane → reflection unit disk). Since the
**unit biquaternions are `SL(2,ℂ)`** (the complexification of the `SU(2)` of §3), the impedance
reflection geometry is the **biquaternion (spinor) action on the reflection sphere**. The Smith
chart is the spinor geometry of impedance — the correspondence **holds**.

Verified images (C3): open `Z→∞ → Γ=+1`; short `Z=0 → Γ=−1`; matched `Z=Z₀ → Γ=0`. And
`|Γ|=1 ⟺ Z = ιX` purely reactive (`|Γ|²=1`, C3) — the lossless boundary is the unit circle.

### §5.2 The open/short SIGN is a Möbius convention (ties to the session measurement)

The 1-port duality `Z ↔ 1/Z` sends `Γ → −Γ` (C3) — it **swaps the open and short fixed
points** on the Smith/Riemann sphere. So **which boundary one calls `+1` is a Möbius
convention** (which antipode is "north"). This is exactly the open/short seam from this
session's measurement: `sign(Γ_at_max_A2)` distinguishes `+1` = antinode/OPEN (Z→∞,
mass-closure) from `−1` = node/SHORT (primer), and per
`observable-battery-infrastructure-prereg.md:44` *"which boundary condition the substrate truly
imposes is the corpus seam, Grant's adjudication (flag-don't-fix)."* The biquaternion/SL(2,ℂ)
view **names the sign-ambiguity precisely** (it is the choice of which fixed point is the base
point of the Möbius action) but **does not resolve which the substrate imposes** — that remains
the empirical/adjudication question. The algebra clarifies the *structure* of the convention;
it is not evidence for either boundary condition.

### §5.3 Classification (`consistency-vs-emergence`)

**T3 = Class A/C consistency-class.** "Möbius = SL(2,ℂ) on the Riemann sphere" and "the Smith
chart is a Möbius transform of impedance" are **standard mathematics + textbook EE**. The
biquaternion re-expresses the canonical `Op3` reflection coefficient in spinor language —
elegant, and it unifies cleanly with T1's `SU(2)` (the real/complex faces of one group, §7) —
but it adds **no new substrate primitive** (Step 8b). **T3 passes no G-gate** on its own.

### §5.4 The one genuinely-illuminating by-product — the null cone IS the reflection wall

The lossless boundary `|Γ|=1` (`Z` purely reactive; the open/short wall where `Z→∞`/`Z=0`)
coincides with the biquaternion **null cone** (`N(q)=0`, the zero divisors, C5). Real quaternions
`ℍ` have **no** null cone (division algebra); only the **complex** (bi)quaternion does. So the
substrate's having a **reflection/saturation boundary** (the `Γ=−1` TIR wall where mass forms,
Axiom 3/4) is what "selects" the **bi**quaternion over the real quaternion: the wall is the null
cone, and only `ℍ⊗ℂ` carries one. This is the strongest *structural* observation in the analysis
— but it is a **re-expression** of the canonical `Γ=−1` boundary (Axiom 3 minimum-reflection +
Axiom 4 saturation), not new physics. Consistency-class; pedagogically valuable. Carried into the
G1 verdict (§7).

---

## §6 T4 — α-structure (G2 test): vol/surf/line + 4π-spinor, forward only

**Result: G2 FAILS. The grade structure parallels the vol/surf/line dimensional hierarchy
(a real, consistency-class observation) but generates NONE of the π-powers. There is no
forward path from the algebra to `137` without importing the Golden-Torus geometry.**

`ave-canonical-source` / forward-only: `ALPHA_COLD_INV = 4π³+π²+π` is **imported**, not fit
(`constants.py:204` → `137.0363038`). No target-fitting to `137.036` anywhere below.

### §6.1 The clean structural parallel (consistency-class)

The canonical decomposition `α⁻¹ = Q_vol + Q_surf + Q_line = 4π³ + π² + π` is a **3D/2D/1D**
dimensional hierarchy (`theorem-3-1-q-factor.md:15`; `Λ_vol↔ℳ` 3D, `Λ_surf↔𝒥` 2D, `Λ_line↔𝒬`
1D — the `ℳ,𝒬,𝒥` boundary-observable structure). The biquaternion / `Cl(3)` grades are a
dimensional hierarchy too:

| `Cl(3)` grade | dim | components | α-term |
|---|---|---|---|
| pseudoscalar (grade 3) | 3D | 1 | `Λ_vol = 4π³` |
| bivector (grade 2) | 2D | 3 | `Λ_surf = π²` |
| vector (grade 1) | 1D | 3 | `Λ_line = π` |
| scalar (grade 0) | 0D | 1 | — (the breathing/longitudinal mode, T2) |

This is genuinely tidy: the α-sum uses exactly the **three spatial grades** `{3D,2D,1D}`, and
the **grade-0 scalar** (the longitudinal mode of T2) sits *apart* from the reactance sum —
which is precisely why the 7th mode is separate from `α`. The algebra gives a clean reason for
**why three additive terms** and **why they are 3D/2D/1D graded**.

### §6.2 But it generates none of the π-powers (the G2 failure)

The grade structure supplies the **dimensional skeleton** only. The **magnitudes** `4π³, π², π`
come from the **Golden-Torus geometry**, NOT the algebra (`theorem-3-1-q-factor.md:46–61`):
`Λ_vol = (2πR)(2πr)(2π·2) = 16π³(R·r) = 4π³` at `R·r = 1/4`; `Λ_surf = 4π²(R·r) = π²`;
`Λ_line = π·d` at `d=1`. These are **angular measures** (`2π` per winding) × the
substrate-derived `R·r = 1/4` (Nyquist cell cross-section at saturation onset, Q-EMBED-SEL-1)
× the **K4 bipartite lobe-count factor 2**. The biquaternion algebra produces **no `2π` angular
measures**, no `R·r=1/4`, no Golden-Torus — so **there is no forward path `algebra → 137`**.
The verification script states this limit explicitly (C6).

> **Sharper still (`theorem-3-1-q-factor.md:48,78`):** the canonical substrate content of the
> `4π` is *"K4 bipartite lobe-count (2 sublattices) × 2π phasor rotation per lobe,"* and
> **"SU(2) double-cover" is explicitly demoted to a *standard-physics translation reference.***
> So even the one factor a spinor account would claim — the `4π` — is, in canon, **K4 bipartite,
> not a spinor postulate.** The biquaternion's spinor-`4π` is the *translation label*, not the
> mechanism. This **further** undercuts any G2 claim: the algebra cannot even claim the `4π` as
> its own forward-derived content.

### §6.3 Classification (`consistency-vs-emergence` Step 8)

**T4 = Class C / consistency-class.** The 3D/2D/1D structure is **already canonical**
(`theorem-3-1-q-factor.md` + `boundary-observables-m-q-j.md`, clm-rtdmsn). The grade-dimension
parallel **re-expresses** it; it adds **no new substrate primitive**, derives **no value**, and
the `4π` it would lean on is canonically K4-bipartite, not spinor. Per Step 8c, classification
stays at the canonical ceiling. **G2 FAILS** — the biquaternion does not derive or
structurally-explain `α⁻¹` independently of the Golden-Torus geometry. The grade-parallel is a
pedagogically-nice *consistency* observation, recorded as such, not inflated.

---

## §7 Classification + the explicit G1/G2/G3 verdict

### §7.1 Per-result classification (`consistency-vs-emergence`)

| Result | Class | New substrate primitive? | G-gate |
|---|---|---|---|
| §2 construction (algebra closes, maps to 7+charge) | definitional / consistency | No — hosts the canonical mode-count; does not generate it | — |
| §3 T1 closure (720°/SU(2)) | **C consistency** | No — same SU(2) as FM (already tagged imported math, FM §5) | none |
| §4 T2 longitudinal scalar | **C consistency** (structural-illumination flavor) | No — mode forced by Ax 1+4, not algebra | none (G3 fail) |
| §5 T3 Möbius/Γ | **A/C consistency** | No — textbook Möbius=SL(2,ℂ)=Smith chart | none |
| §6 T4 α grade-parallel | **C consistency** | No — 3D/2D/1D already canonical (clm-rtdmsn) | none (G2 fail) |

No result reaches Class D (emergence) or Class E (operating-point projection). Every result
is a re-expression of content already canonical at its source's ceiling; per
`consistency-vs-emergence` Step 8c, none promotes.

### §7.2 G1 — structural unification: **FAIL** (the load-bearing determination)

**Steelman (the strongest case FOR G1).** One algebra makes four canonical facts co-occur as
facets of `ℍ⊗ℂ`, and *with algebra-internal necessity*:
- T1 spin double cover = real unit quaternions `SU(2)`;
- T3 impedance-Möbius/reflection = unit biquaternions `SL(2,ℂ)` (**forced** as the
  complexification of that same `SU(2)`);
- T2 longitudinal scalar = the grade-0 part **forced** by closure of the (E,B) vector product;
- the `Γ=−1` reflection wall = the **null cone**, **forced** to exist by the complexification
  (it is exactly what makes `N` non-definite).

You cannot have the complexified spin group (needed for the boost/Möbius reflection structure)
without *also* getting the scalar grade and the null cone. At the **algebra level** this is
necessity, not juxtaposition — the strongest result in the analysis.

**Why it still FAILS the gate.** The necessity is **algebra-internal, not substrate-physical**,
and per `consistency-vs-emergence` Step 8b the unification adds **no new substrate content**:

1. **No new axiom / primitive.** It uses Axioms 1–4 and standard math (`SU(2)⊂SL(2,ℂ)`,
   `Cl(3)` grading, Möbius geometry, the null cone) unchanged.
2. **The "bridge" is notational, not derivational.** The substrate has all four facts for
   **independent physical reasons** — the FM kink (spin), medium compliance (longitudinal),
   EE boundary reflection (Γ), the saturation wall (null cone) — **none derived from the
   others via the algebra.** The biquaternion does not derive any facet from another; it is a
   post-hoc container that fits *because* the substrate independently has all four.
3. **Algebra-necessity ≠ substrate-necessity.** That `ℍ⊗ℂ` forces `SL(2,ℂ)` to contain `SU(2)`
   is a fact about the *algebra*. It does **not** demonstrate that a substrate with spin **must**
   have a propagating longitudinal mode, or that reflection **must** co-occur with spin — a
   counterfactual incompressible or spinless medium would simply be described by a *different*
   algebra. The biquaternion is the right *language* for *this* substrate; it does not *force*
   the substrate's feature-set.

The gate requires unification that is **new structural content** (Step 8b) and **necessity**
at the substrate level. What we have is genuine **algebra-internal** necessity re-expressing
four **independently-canonical, independently-substrate-derived** facts in one elegant
notation. **That is consistency-class unification-of-description — not new physics. G1 FAILS.**

### §7.3 G2 — α-decomposition: **FAIL**

Per §6: the `Cl(3)` grades parallel the `{3D,2D,1D}` vol/surf/line hierarchy (a clean
consistency observation), but the algebra generates **none** of the π-powers — those are
Golden-Torus angular geometry + `R·r=1/4` + the K4-bipartite factor 2. No forward path
`algebra → 137`. And canon already makes the `4π` **K4-bipartite**, demoting "SU(2)
double-cover" to a translation reference (`theorem-3-1-q-factor.md:48,78`). **G2 FAILS.**

### §7.4 G3 — longitudinal discriminator: **FAIL**

Per §4: the scalar slot is algebra-forced and the longitudinal mode is AVE-distinct
(§8), but the mode is **already canonical** (the breathing/acoustic 7th mode; the Master
Equation already supplies its dispersion `c_eff(V)`). The biquaternion re-expresses *why* the
mode exists (the Heaviside-deleted scalar slot) but yields **no new number, dispersion
relation, or coupling**. **G3 FAILS.**

### §7.5 Overall verdict

**All three gates fail → the biquaternion is a CONSISTENCY-CLASS notation / pedagogy aid.**
Canonize nothing. The strongest accurate framing is the **null-cone ↔ reflection-wall**
identification (§5.4): the substrate's `Γ=−1` boundary is *why* the number system is the
**complex** quaternion (which has a null cone) rather than the real one (which does not) — a
clean re-expression of the canonical Axiom-3/4 boundary, valuable as a teaching lens, not new
physics. This is the pre-registered "most likely partial → land consistency-class" outcome
(prereg §4), recorded honestly per Rule 11.

---

## §8 Discrimination-check on T2 (`ave-discrimination-check`)

The prereg §4.7 question: is the longitudinal mode AVE-distinct (transverse-EM-forbidden),
and does it predict anything new?

**Step 1 — enumerate the claims:**
- (a) the substrate has a *propagating longitudinal/acoustic* vacuum mode;
- (b) that mode is *transverse-EM-forbidden* (the Heaviside vacuum has no propagating
  longitudinal EM mode);
- (c) the biquaternion grade-0 scalar is its algebraic home;
- (d) the biquaternion *adds a new testable prediction* about it (the G3 claim).

**Step 2 — SM-counterfactual table:**

| Claim | SM / Heaviside-Maxwell predicts same? | AVE-distinct? |
|---|---|---|
| (a) propagating longitudinal *vacuum* mode | NO — Maxwell vacuum is transverse; longitudinal/scalar modes are gauge, non-propagating. (SM *does* have longitudinal modes in **media** — sound, Langmuir, phonons.) | **YES** — but as a *framework claim* (vacuum is a medium), already canonical via the Master Equation, **not** new to the biquaternion |
| (b) transverse-EM-forbidden | YES forbidden in transverse EM — that is the point | YES, **already canonical** (the deleted scalar) |
| (c) biquaternion is its algebraic home | N/A — a math statement, no physical counterfactual | notation, consistency-class |
| (d) **new** prediction from the algebra | — | **NO** — the biquaternion adds no number/dispersion/coupling |

**Step 2.5 — discriminator axis:** the T2 claim is an **existence** claim (does a propagating
longitudinal vacuum mode exist?), not magnitude or ratio. The discriminator is existence-of-mode:
SM-vacuum NO, AVE YES. But that discriminator is **already supplied** by the Master Equation
(it propagates `V`; gives `c_eff(V)`), and **predates** the biquaternion. A *new* discriminator
would be a measured longitudinal dispersion/speed — which is the Master Equation's content, not
the algebra's.

**Step 3 — promote only on AVE-distinct content:** the longitudinal mode **IS** AVE-distinct
(claims a/b) — answering the first half of §4.7 **YES**. But the AVE-distinctness is a property
of the **already-canonical** breathing/acoustic mode; the biquaternion contributes the
structural **narrative** (Heaviside's deleted scalar = the grade-0 slot), which is
consistency-class. Answering the second half of §4.7 — does the biquaternion predict anything
new — **NO**.

**Discrimination verdict:** *"Maxwell's deleted scalar = AVE's 7th mode"* is best read as a
**structural identification with illumination value**, **not** a structural necessity of the
substrate and **not** a new AVE-distinct prediction. The longitudinal mode's AVE-distinctness is
real and canonical; the biquaternion re-expresses it without adding empirical content. (This is
the §4.4 verdict, confirmed by the counterfactual.)

---

## §9 Discipline-fired log + honest closure

### §9.1 Disciplines fired (and what each caught)

| Discipline | What it caught / enforced here |
|---|---|
| `substrate-native-check` (trigger 6, prose-derivation of an algebra) | §2.3: the substrate's 7 modes come from K4+Cosserat micropolar DOF (Ax 1), **not** the algebra; the 8-component match is consistency, not derivation — guarded the algebra-first SM/QED leak |
| `phase-space-coordinate-check` | §3.2: prereg §2 bundles **real-space** 720° with **phase-space** (2,3) under "SU(2) closure"; surfaced as a coordinate-category caveat (consistent with FM §9 + torus-knot-uniqueness) |
| `consistency-vs-emergence` (Step 8 classification-promotion) | §7.1 + the whole G-gate: every result classified; none promotes past its canonical-source ceiling; named the algebra-necessity-vs-substrate-necessity distinction that sinks G1 |
| `ave-discrimination-check` | §8: T2 longitudinal mode IS AVE-distinct but the biquaternion adds no new discriminator |
| `ave-evidence-framing-discipline` | §0 verdict-up-front; no "found the number system"; strongest *accurate* framing (null cone ↔ reflection wall), neither inflated nor under-claimed |
| `ave-canonical-source` | §6 + verify script: `ALPHA_COLD_INV` imported, forward-only, no fitting; canonical-source assertion in the script |
| `ave-ee-first-mapping` (prereg §5, pre-fired) | EE (Z, Γ, windings) is the measurement language; the biquaternion is the rotation/longitudinal language under it — complementary |

### §9.2 Flag-don't-fix items surfaced (not silently reconciled)

1. **Op3 vs Op17** (§1): the prereg labels the reflection coefficient "Op17"; canonically the
   reflection coefficient is **Op3** (`operators.md:43`), Op17 is the downstream `T²=1−Γ²`. A
   prereg-internal label slip; no corpus change — noted for the auditor.
2. **Real-space 720° vs phase-space (2,3)** (§3.2): the prereg §2 bundling is loose; the
   canonical leaves already separate the two coordinate systems. Consistent with canon; a
   clarification, not a correction.
3. **Open/short sign = Möbius convention** (§5.2): the SL(2,ℂ) view names the sign-ambiguity
   precisely but does **not** resolve which boundary the substrate imposes — that remains the
   open corpus seam / Grant's adjudication (`observable-battery-infrastructure-prereg.md:44`).
   The algebra is not evidence for either boundary condition.

### §9.3 Honest closure (Rule 11)

The pre-registered prediction — *"most likely partial; T1/T3 consistency-class, T2 the strongest
genuine-content candidate, T4 high-risk; pre-commit to landing consistency-class if G1–G3 fail"*
— is **borne out**. A **single mechanism explains all three G-gate failures**: every piece is
**standard mathematics** (`SU(2)⊂SL(2,ℂ)`, `Cl(3)` grading, Möbius geometry, the null cone) over
**already-canonical, independently-substrate-derived** facts, and **algebra-internal necessity is
not substrate-physical necessity**. That is the discipline working at full strength, not a
failure. **Branch closed**; no rescue toward a forced G-gate pass attempted.

**Substitution-not-retraction (Rule 12):** N/A — this was an open prove-or-disprove, not a
falsified prior hypothesis. It lands **disprove-the-strong-claim** (the biquaternion is *not* a
newly-discovered substrate number system) / **affirm-the-weak-claim** (it is an elegant
consistency-class re-expression). No slot is refilled with an unverified hypothesis.

### §9.4 Corpus-state (for the auditor — surface, do not land)

This result is **consistency-class**: it adds/retires **no** matrix row, **no** claim-quality
entry, and requires **no** manuscript edit. It cross-links the §1 canonical leaves without
modifying them. If anything is worth landing, it is a one-line teaching cross-reference (the
null-cone ↔ `Γ=−1`-wall lens) and the Op3/Op17 prereg-label note — both the auditor's call, not
the implementer's. The verification script
[`verify_biquaternion_node_algebra.py`](../src/scripts/vol_1_foundations/verify_biquaternion_node_algebra.py)
is forward-only and passes `make verify`.
