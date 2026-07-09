# RESULT — Electron π₁ / spin-½ SELECTION from the SO(3) Cosserat order parameter

**Date:** 2026-07-08 · **Lane:** implementer (electron-interior) · **Status:** COMPLETE
**Prereg (frozen):** [`2026-07-08_electron-pi1-spinhalf_prereg.md`](2026-07-08_electron-pi1-spinhalf_prereg.md) (commit `4afcbd02`)
**Artifact:** [`src/scripts/vol_2_subatomic/electron_pi1_spinhalf_topology.py`](../src/scripts/vol_2_subatomic/electron_pi1_spinhalf_topology.py) ·
**Tests:** [`src/tests/test_electron_pi1_spinhalf.py`](../src/tests/test_electron_pi1_spinhalf.py) (6/6)
**Tree-proof (origin/main):** `0341cababa92fadc8e680710bd3706b113268fa6`

**Discipline applied:** `ave-prereg` (froze before derive) · `substrate-native-check` (order parameter = SO(3) Cosserat director, not SU(2)) · `phase-space-coordinate-check` (dimensionless homotopy; both phase-space T² and real-space S³ domains computed) · `consistency-vs-emergence` (verdict tagged, no g=2 rescue) · `verify-before-cite` (anchors grepped, prereg §0).

---

## ★ VERDICT

> **[SPIN-HALF-POSITED]** — π₁ of the electron's configuration space carries a genuine
> **ℤ₂** that traces to SO(3)'s **own** intrinsic π₁ (the belt trick), with **no half-angle
> lift used**. The 2π-rotation loop is the order-2 non-trivial element ⇒ spin-½ is **ADMITTED
> and representable**. But the class of that loop is **winding-INDEPENDENT** — the (2,3) parity
> does **not** force it — and the character set Hom(ℤ₂,U(1)) has **two** elements, so **both**
> boson and fermion quantizations are topologically admitted. **Selection into the spin-½
> (fermion) sector is NOT forced by the (2,3) winding parity; it is posited.** The corpus's
> half-angle lift `U=exp(iσ·ω/2)` is exactly the act of hand-choosing the −1 character.
>
> **This CONFIRMS the audit** (clm-rkisb8 rationale: "REPRESENTABILITY established … the
> dynamical selection remains the FM argument, not derived"). It is **NOT** [WRONG-TOPOLOGY]:
> the ℤ₃/L(3,1) reading measures a *different space* (the knot's ambient branched cover), not
> the field configuration space, so the spin-½ identification is on the *correct* topology — it
> is merely un-forced.

Symmetric-standard note: SM/QED also *posits* spin-½ (it is an input rep of the Lorentz group,
not derived); AVE here reaches the same ceiling as SM on selection, while deriving the *structure*
(double cover) that SM imposes. So "posited" is a peer result, not an AVE-specific deficiency —
but it does mean g=2 does **not** upgrade to a from-nothing derivation on this branch.

---

## 1 — THE ORDER PARAMETER AND CONFIGURATION SPACE (substrate-native, no spinor)

The physical DOF is the **SO(3)-valued Cosserat micro-rotation frame** `R(r) ∈ SO(3)` (Rodrigues
image of ω; `src/ave/topological/cosserat_field_3d.py:91-119`). NOT SU(2), NOT a spinor. The
configuration space **Q** is the finite-energy SO(3)-field configurations in the (2,3) winding
sector. Finkelstein–Rubinstein (1968): the soliton's spin/statistics is read from **π₁(Q)** and
the class in π₁(Q) of the loop traced by a **2π spatial rotation**.

## 2 — ★ π₁(Q), TRACED TO SO(3) (the derivation, no lift)

**Step 1 — π₁(SO(3)) = ℤ₂, intrinsic.** SO(3) ≅ ℝP³ = S³/{±1}; its universal cover is the simply
connected S³, a connected double cover, so π₁(SO(3)) = ℤ₂. The non-trivial generator is the loop
of rotations R_ẑ(θ), θ:0→2π (a diameter of the ℝP³ ball, endpoints antipodally identified); its
square (θ:0→4π) is contractible. **This is the belt trick — a fact about the substrate's target
manifold, not a spinor input.**

Demonstrated numerically (`pi1_so3_monodromy`) by the **continuity-tracked Shepperd matrix→quaternion
lift** — the SAME anti-tautology machinery as `src/ave/topological/k4_lattice_holonomy.py:8-11,136`.
Each SO(3) **matrix** is built from the **FULL** angle (cos θ, sin θ); the double-cover sign is read
off the matrix and resolved by **continuity along the path**, never by evaluating cos(φ/2):

| SO(3) loop | lift monodromy | meaning |
|---|---|---|
| R_ẑ(θ), θ:0→2π | **−1 (−I)** | non-contractible = π₁(SO(3)) generator |
| R_ẑ(θ), θ:0→4π | **+1 (+I)** | contractible |

**Step 2 — π₁(Q) via the free-loop-space splitting of the topological group SO(3).** For a
topological group G and finite CW complex X, Map(X,G) is a topological group and its homotopy
splits through iterated free-loop spaces (LG ≃ G × ΩG). With π₁(SO(3))=ℤ₂, π₂(SO(3))=0,
π₃(SO(3))=ℤ, π₄(SO(3))=ℤ₂:

- **Domain-A (real-space, X = S³):** Map(S³,SO(3)) ≃ SO(3) × Ω³SO(3), so
  **π₁(Q_A) = π₁(SO(3)) ⊕ π₄(SO(3)) = ℤ₂ ⊕ ℤ₂**. The winding sector is π₃(SO(3)) = ℤ (instanton/`c`).
- **Domain-B (phase-space, X = Clifford torus T²):** Map(T²,SO(3)) ≃ LG×ΩLG (twice), so
  **π₁(Q_B) = π₁(SO(3)) ⊕ π₃(SO(3)) = ℤ₂ ⊕ ℤ**. The winding sector is [T²,SO(3)] = ℤ₂⊕ℤ₂ (parities).

In **both** domains the **spin-relevant** factor — the class of the global 2π frame-rotation loop —
is the **π₁(SO(3)) = ℤ₂** summand. **The ℤ₂ that carries spin traces to SO(3)'s own π₁, with no
half-angle lift.** ✅ (This is the derived *structure*.)

## 3 — ℤ₂ vs ℤ₃: WHICH GOVERNS THE SPIN, AND WHY

**ℤ₂ governs the spin.** It is π₁ of the SO(3)-field configuration space Q — the object FR spin is
defined on.

**ℤ₃ is a DIFFERENT space.** L(3,1) is the double **branched** cover of the ambient S³ along the
(2,3) trefoil; `z3_branched_cover_order` computes |H₁| = |Δ_trefoil(−1)| = |(−1)²−(−1)+1| = **3**, so
π₁(L(3,1)) = ℤ₃ (matches `research/_archive/L3_electron_soliton/36_pathB_trefoil_z2_investigation.md:49`).
This is an invariant of the **knot's embedding in ambient space** (its monodromy / 3-colorability),
**not** of the field configuration space. It does **not** measure spin.

**Reconciliation (both are real, they measure different things):** the "3" of ℤ₃ reappears
physically in the carrier sector as the **3-fold encirclement** (C3³) required to build the −I — the
FR-braid result found a single partner-encircle rotates the frame by only 120° (`q_w=+0.5`), and −I is
reached only after **three** C3 steps (`research/2026-06-20_fr-braid-spin-statistics_result.md:31-35`).
So: **ℤ₃ = the winding/encirclement structure (how many C3 steps); ℤ₂ = the resulting spin sign (the
double-cover −I).** They coexist; neither is "wrong"; **spin is governed by ℤ₂**. Hence the
competing reading does **not** make the electron a non-spinor — ruling out [WRONG-TOPOLOGY].

## 4 — ★ SELECTION: FORCED BY WINDING PARITY, OR MERELY ADMITTED?

**The 2π-rotation (spin) loop class is winding-INDEPENDENT.** `spin_loop_monodromy(p,q)` applies a
global 2π rigid frame-rotation to the whole (p,q) field and continuity-tracks the lift:

| (p,q) | spin loop 2π | spin loop 4π |
|---|---|---|
| (2,3) electron | **−1 (−I)** | +1 |
| (2,2) | −1 | +1 |
| (1,1) | −1 | +1 |
| (3,5) | −1 | +1 |

The spin sign is **−I for every winding** — it is the generic π₁(SO(3)) belt-trick element, present
for *any* SO(3) field (consistent with the FR-braid finding that the **non-A4 control ALSO reaches
−I**, `…fr-braid…_result.md:24-27`). **The (2,3) parity does not change it.**

**Character set ⇒ ADMITTED, not FORCED.** π₁'s spin factor is ℤ₂ = {1, τ}, τ² = 1. The possible
quantizations are Hom(ℤ₂,U(1)) = {χ(τ)=+1 (boson/integer), χ(τ)=−1 (fermion/spin-½)} — **two**
elements. Topology **admits both**; it does not select. **General theorem realized here:** π₁-topology
alone can only *forbid* the fermion (if τ trivial) or *admit* it (if τ non-trivial, order 2) — it can
**never force** it. Forcing requires an **action-level ℤ₂ term** (a Wess-Zumino / θ / Hopf term) whose
sign is an *additional* physical input. The Skyrme precedent is identical: the B=1 Skyrmion is a
fermion only because the WZ coefficient N_c is odd — parity of an *imported* integer, not π₁ alone.

**The corpus imports exactly this missing sign** via the half-angle lift
`U(r)=exp(iσ·ω/2)` (`…/06_winding_index_projection.md:36`): writing the ½ IS the choice χ(τ)=−1.
The existence proof concedes the import at `…/03_existence_proof.md:168` ("the spin-1/2 structure is
**derived from experimental observation**"). Since energy does not select either
(`…/03_existence_proof.md:174`), and π₁ admits both, **selection is currently posited**.

## 5 — THE (2,3)-PARITY FEATURE THAT IS REAL (surface to Grant — candidate future forcing anchor)

The (2,3) winding **does** produce a genuine, winding-parity-dependent topological fact — just not
the spin one. `texture_class(2,3)`: the field's own cycle-monodromies are (−1)²=+1 (φ, p=2 even) and
(−1)³=−1 (ψ, q=3 **odd**), giving the [T²,SO(3)] component **(0,1)** — **non-zero**, so the (2,3)
SO(3)-field does **NOT** globally lift to SU(2) (the odd q=3 cycle is the obstruction). Contrast
(2,2)→(0,0), liftable.

This is the field's **internal ℤ₂ texture charge**, distinct from the spin-under-rotation loop. It is
the natural anchor for a *future* derivation of a substrate-native forcing term: if one could derive
(from the K4 constitutive action, NOT posit) a ℤ₂ term that **couples the spin quantization χ(τ) to
this odd-winding texture class**, then the (2,3) parity WOULD force χ(τ)=−1 and the verdict would
upgrade to [SPIN-HALF-DERIVED]. **That coupling is not in the corpus.** Deriving it is the concrete
open path — and it exists as an anchor **only in the phase-space (T²) domain**: on the real-space S³
domain H²(S³;ℤ₂)=0, so there is no such texture obstruction at all.

## 6 — ★ THE LOAD-BEARING MODELING CHOICE(S), NAMED

1. **Domain: real-space S³ vs phase-space T² for Q.** Both give ℤ₂ spin-factor and the same
   verdict (admits, not forced) — so the verdict is **robust to this fork**. The fork matters only
   for the *future forcing anchor* (§5), which exists only on T². **Named; surfaced.**
2. **The field model R(φ,ψ) = R_ẑ(2φ+3ψ) (SO(2)⊂SO(3), single-axis winding, per doc36's
   θ=pφ+qψ).** A genuinely 3-axis (non-abelian) director winding could in principle change the
   texture class, but **not** the spin-loop class (that is the π₁(SO(3)) constant summand regardless).
   If Grant reads the physical Cosserat director as non-abelian on the shell, the §5 anchor should be
   recomputed — flagged, not silently assumed.
3. **The relation between the real-space 2π rotation and the phase-space (2,3) winding.** The spin
   loop is a real-space operation; the winding is phase-space. Their coupling (whether a real-space
   2π rotation *drags* the phase-space winding in a way that changes χ) is the deepest open question
   and is the physically-decisive knob. Absent a derived drag term, they decouple ⇒ admits.

## 7 — ANTI-TAUTOLOGY / HONESTY GATES

| Gate | Status |
|---|---|
| **No half-angle lift on the π₁ path** | ✅ Confirmed. `exp(iσ·ω/2)` / cos(φ/2) never supplied as INPUT; `rot_z` uses the FULL angle; the SU(2) sign is read by the external Shepperd matrix→quaternion lift, resolved by continuity. Machine-checked: `test_anti_tautology_no_half_angle_lift_on_path` (strings/comments stripped; no `sigma`/`Pauli`/`np.exp`/`/ 2` in executable code). |
| **ℤ₂ traces to SO(3)'s intrinsic π₁** | ✅ Confirmed. The spin ℤ₂ is the π₁(SO(3))=π₁(ℝP³) summand (belt trick), demonstrated by the 2π→−I / 4π→+I monodromy. It is the generic double-cover element, not an inserted spinor. |
| **Firewall: no imported spinor structure** | ✅ π₁ from SO(3) target + (2,3) boundary only. No α/m_e/Q_TANK on the path (dimensionless homotopy). |
| **Symmetric standard, no g=2 steering** | ✅ Verdict follows the computed group + character set. A clean "posited" is reported plainly; NOT debugged toward [SPIN-HALF-DERIVED]. |

## 8 — WHAT THIS MEANS FOR g=2 (#583)

g=2 rides on the electron occupying the spin-½ sector. This result says that occupancy is:
- on the **correct topology** (ℤ₂, not the ℤ₃ red herring) — so g=2 is **not** built on a wrong-topology error; and
- **representable/admitted** (the −I double-cover element exists and is lift-free) — so g=2 is
  internally *consistent*; but
- **not forced** by the (2,3) winding parity — the selection into that sector is currently a **posit**
  (the half-angle lift), equivalent to SM's input choice.

**Net for #583:** g=2 should be tagged **consistency-class / peer-with-SM on the selection step**, NOT
emergence-class "spin-½ derived from AVE." The honest headline is "AVE derives the spin-½ *structure*
(double cover) and admits the sector; the *selection* is posited, at parity with SM." Do not headline
g=2 as an AVE-internal from-nothing derivation on this branch.

## 9 — PROPOSED INTEGRATION NOTE (for the auditor lane to land — I do NOT edit canon)

- **clm-rkisb8** (`manuscript/ave-kb/vol1/claim-quality.md:992`): the rationale already says
  "dynamical selection remains the FM argument, not derived." This result **strengthens and sharpens**
  it: selection is not merely *un-derived* but **cannot be forced by π₁ alone** (character-set theorem);
  forcing needs an action-level ℤ₂ term the corpus imports via the half-angle lift. Suggest adding a
  strengthen-by pointer to this result + the §5 odd-winding texture-class anchor as the concrete route.
- **FM leaf** (`…/finkelstein-misner-spin-half-derivation.md` §8): its own non-claim "does NOT address
  the (2,3) winding selection mechanism here" is now **positively answered**: the (2,3) parity does
  **not** force spin — it forces a distinct *texture* class. Suggest a forward-pointer.
- **doc 36** (`…/36_pathB_trefoil_z2_investigation.md`): its ℤ₂-vs-ℤ₃ instinct is confirmed and made
  rigorous (ℤ₂ = config-space/spin; ℤ₃ = ambient branched cover/knot). Suggest citing this result as
  the settled reconciliation.
- **No axiom action.** This is engine-consistent-with-Ax3 (SO(3) target); it is **not** a missing-axiom
  finding and does **not** call for an Ax5 candidate. It is a "selection un-forced / import named" finding.

## 10 — HONEST CAVEATS

- The ℤ₂ "admits-not-forces" ceiling is a theorem about π₁-topology + character sets; it is as strong
  as the modeling of Q. If a future substrate-native action term (a derived, not posited, ℤ₂/WZ/Hopf
  term keyed on the §5 odd-winding texture class) is produced, the verdict can move to
  [SPIN-HALF-DERIVED]. This result does not exclude that path — it names it and shows it is currently
  empty.
- The single-axis SO(2)⊂SO(3) field model (choice §6.2) is the corpus's own θ=pφ+qψ; a non-abelian
  director reading is a Grant-adjudicable refinement that could change the §5 texture computation (not
  the §4 spin verdict).
- "Posited at parity with SM" is a *peer* statement (symmetric standard), not a claim that AVE is
  worse than SM; SM does not derive spin-½ selection either. The AVE-distinct content, if any, lives in
  a *derived* forcing term — which would be a genuine chord — not yet in hand.
