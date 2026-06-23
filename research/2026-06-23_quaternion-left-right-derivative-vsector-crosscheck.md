# Quaternion left/right-derivative ↔ V-sector cross-check

**Date:** 2026-06-23 · **Type:** research inspection (refute-by-default cross-check; **NOT** a code change, **NOT** a new chord). **Lane:** engine-consolidation (D5).
**Status:** for review — orchestrator adversarial audit + Grant merge pending.

> **TL;DR (the honest verdict up front).** The non-commutative left/right quaternion (Fueter)
> derivative is algebraically real, and keeping **both** orderings retains a seventh, grade-0 scalar
> **T = ∇·A + (1/c²)∂φ/∂t** — exactly the Lorenz-gauge quantity textbook EM sets to zero, and
> structurally the **same algebraic slot** as AVE's longitudinal **V-sector / "the 3."** But this is a
> **cross-check, not a derivation**: the algebra makes the scalar grade **visible**; it does **not** make
> it **physical**. The physical reality of AVE's V-sector rides the substrate posit + the saturable
> Master Equation, **not** the operator algebra. This **confirms and modestly tightens** the prior
> result [`research/2026-06-06_biquaternion-node-algebra-result.md`](2026-06-06_biquaternion-node-algebra-result.md)
> (which already reached "identifies, does not derive" and **G3-FAIL: no new testable prediction**).
> **No new chord. No optical-activity bankability rescue** (the Phase-1 buried-g₀ verdict stands,
> formalism-independent). The deliverable is a cleaner formal home (Clifford geometric calculus /
> Fueter / biquaternion=SL(2,C) / Riemann-Silberstein) + a bidirectional crank-check of the
> Jack→Kennedy lineage.

---

## 1. Why this is a cross-check, not a discovery (prior art)

Per the corpus-grep discipline, this is **the second** pass at the quaternion↔V-sector question, not the
first. [`research/2026-06-06_biquaternion-node-algebra-result.md`](2026-06-06_biquaternion-node-algebra-result.md)
already:

- Applied the quaternion differential operator to the potential (φ + **A**) and recovered the scalar
  part **(1/c)∂ₜφ + ∇·A** = the Lorenz term (§4.2:218–224).
- Landed the honest framing (§4.3:228–242): "the biquaternion scalar **slot** is the common algebraic
  **home** for (i) Maxwell's gauge scalar and (ii) AVE's physical acoustic mode" — it **identifies, does
  not derive**; AVE's longitudinal mode is a real medium DOF *because of the medium*, not the algebra.
- Recorded the explicit verdict **G3 (longitudinal discriminator) = FAIL** (:21, :439–445): "the algebra
  re-expresses *why* (Heaviside's deleted scalar) but adds **no new number/dispersion/coupling**."

**What D5 adds over the 2026-06-06 pass** (the genuine, bounded increment):
1. The explicit **left vs right (Fueter)** ordering lens — 2026-06-06 used "the quaternion differential
   operator" as a single object; Jack's specific contribution is that **left ≠ right**, and that picking
   one ordering *is* what imposes the Lorenz condition T = 0. This names the *mechanism* of the deletion.
2. The **formal-home placement** (§4) — Fueter regularity, biquaternion = SL(2,C), Clifford geometric
   calculus (STA), Riemann-Silberstein — the theorem-backed containers the corpus had not yet named.
3. A **bidirectional crank-check** (§5) of the Jack → Dunning-Davies/Norman → Kennedy lineage.
4. The **D5(ii) chiral-operator** assessment against the Phase-1 writhe-blind stencil.

None of these changes the G3-FAIL classification; they sharpen the *form* and the *external citations*.

---

## 2. The operator and the seventh scalar (the sound core)

P.M. Jack, *Physical Space as a Quaternion Structure, I* ([arXiv:math-ph/0307038](https://arxiv.org/abs/math-ph/0307038), 2003):
with d/dr = (1/c)∂ₜ + i∂ₓ + j∂_y + k∂_z and potential **A** = U + A₁i + A₂j + A₃k, the non-commutative
product means d/dr can act to the **right** (a→b) or **left** (b←a); the two differ **only in the sign of
the cross/wedge term**. Forming the symmetric and antisymmetric combinations and defining
**E** = −{d/dr, A}, **B** = +[d/dr, A], the symmetric (electric) derivative carries a non-vanishing
**scalar/time grade**:

  **T = −(1/c)∂U/∂t + ∇·A**  (Gaussian)  ≡  **∇·A + (1/c²)∂φ/∂t**  (SI).

The Maxwell set becomes the usual four equations **plus T-source terms** (e.g. ∇×B = (1/c)∂ₜE + ∇T + …;
∇·E = (1/c)∂ₜT + …). **T is exactly the Lorenz-gauge scalar** ∂_μA^μ that standard EM sets to zero.

**This much is sound and uncontroversial** — it is just the grade decomposition ∇A = ⟨∇A⟩₀ + ⟨∇A⟩₁ +
⟨∇A⟩₂, with ⟨∇A⟩₀ = T the grade-0 part the transverse-vector projection discards.

**The load-bearing distinction** (and the seam where soundness ends): the algebra makes T **visible**; it
does **not** make T **physical**. In standard EM, T = ∂_μA^μ is **pure gauge** — removable by a gauge
transformation, not an independent DOF. To promote T to an observable propagating field you must **add
structure beyond Maxwell** (break U(1): a Proca/Stueckelberg mass term, a non-conserved current, or a
**medium**). The quaternion algebra supplies none of that. *Keeping both orderings* is a choice of
**notation that retains the grade**, not a derivation that the grade is excited.

---

## 3. D5(i) — Does the operator FORCE the V-sector? **No — it CONFIRMS the algebraic home; AVE's physics supplies the reality.**

Two facts decide this, and they point the same way:

**(a) AVE genuinely carries the longitudinal scalar in code** (operative-code reading, not narrative):
- [`master_equation_fdtd.py:97`](../src/ave/core/master_equation_fdtd.py) — `self.V` is a first-class
  scalar state field, time-integrated by the **saturable** Master Equation
  ∇²V − μ₀ε₀ √(1−(V/V_yield)²) ∂ₜ²V = 0, with the A1 stiffening kernel c_eff² = c₀²/S, S = √(1−A²)
  (:148–151) that self-traps the wave into rest mass (the A1 cage). **Carried, not projected out.**
- [`fdtd_3d.py:80-86`](../src/ave/core/fdtd_3d.py) — the textbook Yee solver carries E/H vectors **only**,
  no φ/A/∇·A. This is the transverse-vector projection — but it is **acknowledged by design**
  ([`engine-capability-map.md`](../manuscript/ave-kb/common/engine-capability-map.md):41,57), *not* a
  smuggled Gauss-deletion: the scalar Master-Equation engine exists precisely because the cubic Yee/K4-TLM
  grids implement Z(V) but not c_eff(V).

So AVE's substrate **does** have a real longitudinal DOF, governed by the Master Equation and the medium —
matching [`master-equation.md:18,20`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)
("the longitudinal re-engages at saturation = the electron"; A1 dilatation-MASS scalar) and the MYTH-GUARD
in [`common/the-abandoned-interior.md:22`](../manuscript/ave-kb/common/the-abandoned-interior.md)
("'Heaviside deleted a physical mode' is **false** for standard EM; AVE **adds** a medium with a genuine
longitudinal DOF").

**(b) The quaternion left/right derivative identifies that DOF's algebraic grade — and stops there.**
The grade-0 part of ∇A *is* T *is* the slot AVE's V-sector occupies. The left/right lens additionally
explains **why** textbook EM loses it (picking one ordering ≡ imposing T = 0). But the step from "the
scalar grade exists in the algebra" to "the scalar grade is a propagating, physical mode" is **AVE's
substrate posit + the Master Equation dynamics**, *not* the algebra. This is the same boundary the
2026-06-06 result drew ("identifies, does not derive") and the same boundary the **mass = A1 grade
assignment** sits behind ([`master-equation.md:25`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):
"ratified-consistency, **not** driver-validated — no driver discriminates A1-mass from T2-mass").

**Verdict on D5(i):** the operator route is a **derivation-tightening of the V-sector's FORM** — it gives
an external, theorem-backed (Fueter/STA, §4) statement that the V-sector = exactly the grade-0 part of ∇A
that the transverse projection deletes, and names the ordering-choice mechanism of that deletion. It is
**not** a derivation of the V-sector's physical reality, and it adds **no** new number, dispersion, or
coupling. **G3-FAIL stands** (corroborated, not overturned).

---

## 4. D5(ii) — Is left≠right the natural chirality operator? **Yes as a cleaner LANGUAGE; NO as a bankability fix.**

Non-commutativity **is** a handedness: the left and right products differ by the sign of the cross/wedge
term, and at the field level the **Riemann-Silberstein** split **F⁺ = E + icB** vs **F⁻ = E − icB** is
literally a parity/chirality selector (the duality rotation F → e^{iθ}F is the continuous chiral
symmetry). This is a **cleaner, coordinate-free, intrinsically-handed** chiral operator than the
local-bond Bloch stencil.

**Why this is a genuine cross-check on the Phase-1 failure mode.** The Phase-1 FAIL-1 stencil was
**writhe-blind** because operators built from local bond directions {d̂, k·d} cannot see handedness — the
left and right srs bond-direction multisets are **identical** (spec_R − spec_L ≈ 4.4×10⁻¹⁵,
[`research/2026-06-23_chiral-vector-tlm-phase1_result.md:32`](2026-06-23_chiral-vector-tlm-phase1_result.md)).
A left/right-derivative / RS-chirality operator is handed **by construction** (F⁺ ≠ F⁻ algebraically), so
it cannot exhibit that specific blindness — a useful structural confirmation that the handedness is
intrinsic to the operator, not an artifact of stencil choice.

**HONEST GUARD (load-bearing — do NOT over-claim).** This does **not** move the Phase-1 buried-g₀ verdict.
The writhe-**aware** vector-TLM operator *already* converged a signed bulk g₀ = ∓2.21589 rad/lattice-z-unit
([`…chiral-vector-tlm-phase1_result.md:23-25`](2026-06-23_chiral-vector-tlm-phase1_result.md), PR #374) —
i.e. the chirality is already seen cleanly. The unsolved problem is the **magnitude** (g₀/a_cell ≈ 2×10¹²
rad/m ≈ ~40 OOM above the cosmic bound; the continuum k→0 gyration not extracted) and that is
**formalism-independent**. A left/right / RS chiral operator is **better notation + a cross-check**, **not**
a fix for the optical-activity bankability (def-0pt1ac stays demoted, PRs #373/#374/#376).

---

## 5. D5(iii) — The formal home (rigorous containers)

| Container | What it is | Map to AVE | Honest caveat |
|---|---|---|---|
| **Fueter regularity** (Sudbery 1979) | Quaternionic analogue of complex analyticity: D = ∂ₜ + i∂ₓ + j∂_y + k∂_z; **left-regular** Df=0 ≠ **right-regular** fD=0 (genuinely different — non-commutative). Theorem-backed (Cauchy-Fueter integral formulas). | The rigorous home of Jack's left/right derivative — elevates "ordering matters" from notation to a theorem. The regularity conditions are where the scalar (Lorenz/T) part is constrained. | A statement about **function theory** (source-free analyticity), not a dynamical law. Supplies FORM, not which grades are excited. |
| **Biquaternion = SL(2,C)** | Complex quaternions ≅ M₂(C) ≅ Pauli algebra; even part = Spin⁺(1,3) ≅ **SL(2,C)**, the Lorentz double cover carrying Weyl/Dirac spinors. Conway (1911)/Silberstein (1912) biquaternion-Maxwell. | The citable external home for AVE's **carrier/spin-½ sector** (charge/spin on the Cosserat (2,3) grade; FR-braid spin-statistics). | **Peer with — in fact *is* — the SM's spinor machinery** in different notation. Formalizes the carrier; does **not** produce an AVE-distinct chord. |
| **Clifford geometric calculus (Hestenes STA)** | The geometric derivative ∇A = ∇·A + ∇∧A; all of Maxwell collapses to **∇F = J**. ⟨∇A⟩₀ = T (scalar/V-sector grade), ⟨∇A⟩₂ = transverse EM; pseudoscalar-I multiplication = the **E+iB duality = native chiral operator**. | **The recommended home** — the rigorous superset of Jack's trick. Unifies AVE's longitudinal-scalar + transverse-EM + rotational grades in **one** derivative, matching the **Z_EM / Z_shear / Z_bulk** channel picture. Using Clifford-the-*algebra* (relabeling) is cosmetic; using the grade-*calculus* is what forces the scalar grade into view. | Same boundary: STA gives which grades exist and how they couple; it does not assert which carry observable excitation — that is substrate physics. |
| **Riemann-Silberstein** F = E + icB | Source-free Maxwell as one complex equation i∂ₜF = c∇×F, ∇·F = 0; F is a symmetric SL(2,C) spinor (Bialynicki-Birula photon wavefunction). | The concrete biquaternion-Maxwell object and natural seat of the chiral operator (F⁺/F⁻). | **Purely transverse** (∇·F = 0) = the **photon sector**; it does **not** contain T. Jack/STA restore the scalar grade RS omits — RS and the full geometric derivative are complementary halves. |

**Net:** Clifford **STA** is the cleanest rigorous home (it contains the others as projections: RS = the
transverse bivector half; biquaternion=SL(2,C) = the even/spinor part; Fueter = the left/right-regularity
of the geometric derivative). It maps 1:1 onto AVE's existing multi-grade impedance-channel picture.

---

## 6. Crank-check (bidirectional — take the operator, reject the conclusions)

The lineage's **math hygiene degrades monotonically** while its **physical claims inflate** — a textbook
over-claim cascade: Maxwell (quaternions, legit) → Conway 1911 / Silberstein 1912 (legit biquaternion-Maxwell,
RS) → **Jack 2003** (sound operator; speculative *thermoelectric* interpretation of T) → **Dunning-Davies &
Norman 2020** (SCIRP journal; cites Bearden; Thunder Energies affiliation; high crank density) → **Kennedy
2023 viXra / 2025 JHEPGC** (SCIRP; gravity-EM unification + "photo-graviton"/"negative-mass graviton" +
UFO-propulsion).

**SOUND — import as FORM (keep):** the non-commutative left/right derivative; the grade-0 scalar
T = the Lorenz quantity made visible; Maxwell's original quaternion formulation; Conway/Silberstein/RS as
mainstream; T = ∂_μA^μ normally gauge-fixed to zero.

**CRANK — reject the conclusions:**
- **"T is a physical, observable, propagating field"** — *not* established by the algebra; needs broken U(1)
  (mass term / non-conserved source). The whole edifice rests on this un-derived leap.
- **Superluminal c√3 scalar wave** (Dunning-Davies/Norman) — artifact of ad hoc assumptions (integration
  constant = 0, T = 2∇²S).
- **Over-unity / "clean vacuum energy"** (Bearden-tier, 5×10⁴–10⁶ power gains) — energy-conservation
  violation, no replication.
- **Reactionless / antigravity propulsion; "graviton gas"** (Kennedy) — invented entities, no evidence.
- **Gravity-EM unification by setting the integration constant k = −κmM/r** (Kennedy) — curve-fitting a
  gauge term to Newton's potential by fiat, not a derivation.

**AVE's structural immunity (why AVE can import the operator safely).** AVE *cannot* make the lineage's
category errors **if** it imports the operator as FORM only, because its substrate posits already forbid each
crank conclusion:
- **Lossless-reactive (Axiom 3)** → no energy extraction ⇒ rejects over-unity by construction.
- The longitudinal mode is a **medium-stiffness phase property** (c_eff(V) self-trapping), **not** an FTL
  *signal* ⇒ rejects superluminal-signaling.
- EM and gravity are **separate impedance channels** (Z_EM / Z_shear / Z_bulk) ⇒ rejects Kennedy's
  one-unified-quaternion-field ansatz.

So the safe posture is the EE-import posture: **take the scalar-grade operator, quarantine the
conclusions**, and be explicit that the algebra→observable leap is supplied by AVE's substrate physics, not
borrowed from the lineage.

---

## 7. Verdict + classification

- **D5(i):** the left/right-derivative route **confirms** the V-sector's algebraic identity (grade-0 of ∇A
  = the Lorenz scalar = AVE's "the 3") and names the ordering-choice deletion mechanism. It is a
  **FORM / derivation-tightening + cross-check**, corroborating the 2026-06-06 **G3-FAIL**. It does **not**
  derive the V-sector's physical reality and adds **no** new testable number. **Class: consistency /
  structural-illumination** (same band as the 2026-06-06 result; this does not lift it).
- **D5(ii):** left≠right / RS F⁺-F⁻ is a **cleaner, intrinsically-handed chiral operator** and a useful
  cross-check that handedness is operator-intrinsic (not stencil-dependent) — but it **does not move** the
  Phase-1 buried-g₀ verdict. No bankability change.
- **D5(iii):** the rigorous home is **Clifford STA** (with biquaternion=SL(2,C), Fueter, RS as its
  even-part / regularity / transverse-projection facets). It maps onto AVE's existing Z_EM/Z_shear/Z_bulk
  multi-grade picture.
- **No new chord. No optical-activity bankability rescue.** The honest expected outcome (a cross-check /
  notation-tightening of the V-sector, not new content) holds.

---

## 8. Grant-calls — RESOLVED (orchestrator audit, 2026-06-23)

1. **Clifford STA notation layer: RESOLVED → do NOT adopt corpus-wide.** STA is pure notation here (D5
   added no new content), so it does **not** get adopted as a framework-wide layer. Use it **only as a
   LOCAL expository aid inside the V-sector docs** where it clarifies "the Heaviside-deleted grade is
   physical" — never as an engine rewrite (the FDTD/Cosserat engines already realize the physics). This
   doc records that decision.
2. **External corroboration vs FORM-solidity: RESOLVED → corroboration ONLY, band unchanged.** The
   Fueter/STA theorem-backing is recorded as **FORM-level corroboration only**; it does **NOT** lift the
   V-sector's FORM-solidity band. The **physical** "mass = A1" grade-assignment stays
   **ratified-consistency, not driver-validated** ([`master-equation.md:25`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)).
   Lifting any band on the strength of an algebraic identification would repeat the lineage's category error.
3. **Citation hygiene: RESOLVED → apply.** Cite **Jack (arXiv:math-ph/0307038)** for the operator and the
   **upstream** mathematics (Sudbery/Fueter, Hestenes/STA, Conway/Silberstein/RS) for the formal home; cite
   Dunning-Davies/Norman and Kennedy **only** as the over-claim cascade to avoid (SCIRP/viXra,
   fringe-adjacent), **never** for a physical conclusion. (Applied in §9.)

---

## 9. Provenance + corrections

- Built from a 3-lane read-only gathering (corpus grounding + operative-code reading + formal-home/lineage
  web research) and the prior result
  [`research/2026-06-06_biquaternion-node-algebra-result.md`](2026-06-06_biquaternion-node-algebra-result.md).
- **Correction to the D5 brief's algebra counts.** The brief states "Clifford 111 / Pauli 94 / quaternion 19
  / biquaternion 7," which is **not reproducible** at HEAD by any method tried. Counts are method-sensitive,
  so the exact figures are **not load-bearing** here — only the qualitative claim is. As **file** counts
  (`grep -rliE <term> manuscript src --include='*.md' --include='*.py' | wc -l`): Clifford 90 / Pauli 70 /
  quaternion 16 / biquaternion 6 (manuscript + src), or 220/109/42/24 full-corpus; **line/occurrence** counts
  run several times higher. The **load-bearing, method-independent** facts: the quaternion/biquaternion/Clifford
  **algebra** is heavily present at every scope, while the non-commutative **left/right (Fueter) derivative
  operator** has **0 genuine uses** (confirmed across `left.*derivative` / `right.*derivative` / `Fueter` /
  `left-regular` / `right-regular`; the only hits are this brief and an incidental archive use of
  "right"=correct, "derivative"=ordinary time-derivative).
- **Sources** (formal home): Jack [arXiv:math-ph/0307038](https://arxiv.org/abs/math-ph/0307038); Sudbery,
  *Quaternionic Analysis*, Math. Proc. Camb. Phil. Soc. 85 (1979) 199; Hestenes, *Space-Time Algebra* (2nd
  ed. Springer 2015) + Am. J. Phys. 71 (2003) 691; Bialynicki-Birula, *Photon wave function*, Prog. Optics
  36 (1996); biquaternion ≅ SL(2,C) is the standard Spin⁺(1,3) double-cover identity (textbook; no
  preprint pin needed). Crank cascade (cite as avoid-list only):
  Dunning-Davies & Norman, J. Mod. Phys. 11 (2020) 1361 (SCIRP); Kennedy, viXra:2312.0075 / JHEPGC 11 (2025)
  (SCIRP).
