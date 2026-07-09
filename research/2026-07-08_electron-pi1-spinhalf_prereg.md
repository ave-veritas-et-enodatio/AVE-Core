# PRE-REGISTRATION — Electron π₁ / spin-½ SELECTION from the SO(3) Cosserat order parameter

**Date:** 2026-07-08 · **Lane:** implementer (carrier-sector / electron-interior) · **Status:** FROZEN
**Branch:** `analysis/electron-pi1-spinhalf` · **Tree-proof (origin/main):** `0341cababa92fadc8e680710bd3706b113268fa6`

**Discipline applied (this prereg):** `ave-prereg` (corpus-grep BEFORE design — §0) ·
`substrate-native-check` (order parameter = SO(3) Cosserat micro-rotation, NOT SU(2)/spinor — §1) ·
`phase-space-coordinate-check` (the (2,3) winding is a PHASE-SPACE object on the Clifford torus;
the computation is dimensionless homotopy, matched to the phase-space domain — §2) ·
`consistency-vs-emergence` (verdict tagged forced/admitted, no g=2 rescue-steering — §5) ·
`verify-before-cite` (every file:line grepped on this worktree — §0).

This is an **analytical topology** pre-reg, NOT a seeded-soliton FDTD. A seeded simulation would
re-import whatever representation seeds the ansatz; the question is settled by computing a
fundamental group from the target manifold + winding data, which cannot bake in the answer.

---

## 0 — VERIFY-BEFORE-CITE ANCHOR LEDGER (all grepped on this worktree @ `0341caba`)

| Claim used in this design | Anchor (file:line) | Status |
|---|---|---|
| Double-cover 2T⊂SU(2): structure derived, SELECTION asserted | `manuscript/ave-kb/vol1/claim-quality.md:992` (clm-rkisb8) + `:1011` rationale ("REPRESENTABILITY established … dynamical selection remains the FM argument, not derived") | ✅ verbatim |
| k4-rotation-group §6: "spin-½ DERIVED … fields must transform under 2T rather than T … provided by FM mechanism" | `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md:132-134` | ✅ verbatim |
| FR-braid: exchange −I is **generic-FR** (non-A4 control ALSO reaches −I); π₁(SO(3))=ℤ₂ shared by every double-cover framework; −I via **3-fold** C3³ encircle | `research/2026-06-20_fr-braid-spin-statistics_result.md:24-35` | ✅ verbatim |
| FM leaf: mechanism = belt-trick ℤ₂; §8 "Does NOT demonstrate dynamical stability … does NOT address the (2,3) winding selection mechanism here" | `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md` §2, §8 | ✅ verbatim |
| Competing reading: double branched cover of S³ along (2,3) trefoil = lens space **L(3,1), π₁=ℤ₃** | `research/_archive/L3_electron_soliton/36_pathB_trefoil_z2_investigation.md:49` | ✅ verbatim |
| Existence proof: "spin-1/2 structure is **derived from experimental observation** and fixed in AVE via the Clifford-torus representation" (IMPORT admission) | `research/_archive/L3_electron_soliton/03_existence_proof.md:168` | ✅ verbatim |
| Existence proof: energy functional does NOT select (⇒ selection must be TOPOLOGICAL, not variational) | `research/_archive/L3_electron_soliton/03_existence_proof.md:174` | ✅ verbatim |
| The POSITED half-angle lift to AVOID: `U(r)=exp(iσ·ω/2)` | `research/_archive/L3_electron_soliton/06_winding_index_projection.md:36` | ✅ verbatim |
| Existing substrate-native anti-tautology machinery: double-cover from LATTICE CONNECTIVITY, "NEVER calls the OP_B analytic axis-angle rotor … resolved by continuity along the path, never by cos(φ/2)" | `src/ave/topological/k4_lattice_holonomy.py:8-11,92,136` | ✅ verbatim |

---

## 1 — THE ORDER PARAMETER / CONFIGURATION SPACE (substrate-native)

The physical substrate DOF is the **SO(3)-valued Cosserat micro-rotation (director/frame) field**
`R(r) ∈ SO(3)` (Rodrigues image of ω; `cosserat_field_3d.py:91-119`). NOT SU(2), NOT a spinor.

The configuration space **Q** is the space of finite-energy SO(3)-valued field configurations on
the soliton domain, in the topological sector carrying the (2,3) winding. Spin/statistics of a
soliton is governed (Finkelstein–Rubinstein 1968) by **π₁(Q)** and the homotopy class in π₁(Q) of
the loop traced by a 2π rotation.

**★ Load-bearing modeling FORK (pre-registered, NOT resolved by fiat — substrate/Grant adjudicate):**
- **Domain-A (real-space):** X = ℝ³∪{∞} = S³ (finite-energy ⇒ constant at ∞). Real-space body = 0₁ unknot.
- **Domain-B (phase-space):** X = Clifford torus T² ⊂ S³ ⊂ ℂ², where the (2,3) winding physically lives.

Both will be computed. If the verdict differs between them, that fork IS where the physics is
decided and is surfaced to Grant (flag-don't-fix).

## 2 — THE FORK TO SETTLE: ℤ₂ vs ℤ₃

Two characterizations are in the corpus:
- **ℤ₂** = π₁(SO(3)) (the belt trick; RP³). Claimed source of spin-½.
- **ℤ₃** = π₁(L(3,1)), the double **branched** cover of S³ along the (2,3) trefoil (doc36:49).

Pre-registered question: **which space governs the SOLITON'S SPIN** — the SO(3)-field configuration
space (→ ℤ₂) or the branched cover of ambient space along the knot locus (→ ℤ₃)? They are different
spaces; the derivation must say which invariant answers the spin question and reconcile the other.

## 3 — THE COMPUTATION (method, frozen)

1. π₁(SO(3)) = ℤ₂ established INTRINSICALLY (SO(3)=RP³, universal cover S³) and demonstrated
   numerically by the **continuity-tracked Shepperd matrix→quaternion lift** of the SO(3) loop
   R_ẑ(θ), θ:0→2π (⇒ −I) and θ:0→4π (⇒ +I). The lift takes a rotation **matrix** (built from the
   FULL angle) and reads its quaternion; the −I arises by **continuity along the path**, never by
   evaluating cos(φ/2). (Reuse `k4_lattice_holonomy.rotation_matrix_to_quaternion`.)
2. π₁(Q) via the free-loop-space splitting for the topological group SO(3):
   Map(T²,SO(3)) ≃ iterated free loop space; π₁ computed from π₁,π₂,π₃(SO(3)). Identify the
   2π-rotation loop's factor.
3. Sector membership of the (2,3) field in [X, SO(3)] (obstruction theory / winding parities).
4. SELECTION: compute whether the 2π-rotation loop's π₁-class DEPENDS on the (2,3) winding parity
   (⇒ forcing) or is winding-independent (⇒ admits only). Compute the character set Hom(π₁(Q),U(1))
   to state forced-vs-admitted rigorously. Cross-check (2,3) vs (2,2) vs (1,1).
5. ℤ₃ reconciliation: L(3,1) via |H₁(double branched cover)| = |Δ_trefoil(−1)| (Alexander poly).
   Confirm it is a branched-cover-of-ambient invariant, a DIFFERENT space from Q.

## 4 — ★ THE HARD ANTI-TAUTOLOGY RULE (frozen)

- The half-angle lift `U=exp(iσ·ω/2)` is **FORBIDDEN on the π₁-computation path**. If any ℤ₂ is
  produced by inserting a half-angle spinor ansatz, the result is tautological → FAIL.
- Any ℤ₂ that appears MUST be traced to SO(3)'s **intrinsic** π₁ (belt trick / RP³ / π₄(SO(3))),
  demonstrably not to an inserted spinor. The code will carry an AST/grep self-check that
  `exp(iσ·φ/2)` and `cos(φ/2)`-as-input do not appear on the derivation path.
- No α, m_e, Q_TANK on the topology path (it is dimensionless homotopy anyway).

## 5 — VERDICT ROUTING (pre-registered; symmetric standard — NO steering to rescue g=2)

- **[SPIN-HALF-DERIVED]** — π₁(Q)=ℤ₂ AND the (2,3) winding **parity FORCES** the non-trivial
  (spin-½) class with no lift used. g=2 upgrades to a real AVE-internal derivation.
- **[SPIN-HALF-POSITED]** — π₁(Q)=ℤ₂ but **both sectors equally admitted** (selection un-forced,
  requires an action-level ℤ₂ input the corpus imports via the lift). Confirms the audit — say it plainly.
- **[WRONG-TOPOLOGY]** — π₁(Q)=ℤ₃ or trivial governs the spin ⇒ (2,3) soliton is not a spinor; g=2
  identification on wrong topology (foundational correction).
- **other** — report the actual group + implication.

A clean [SPIN-HALF-POSITED] or [WRONG-TOPOLOGY] is a **real, valuable result**, not a failure to be
debugged away. Honest closure (Rule 11): the verdict follows the computed group + character set,
never the desire to keep g=2.

## 6 — DELIVERABLE

Result doc `research/2026-07-08_electron-pi1-spinhalf_result.md` + analytical script
`src/scripts/vol_2_subatomic/electron_pi1_spinhalf_topology.py` + test
`src/tests/test_electron_pi1_spinhalf.py`. NO canon/paper edits — result doc carries a proposed
integration note for the auditor lane to land. NO self-merge.
