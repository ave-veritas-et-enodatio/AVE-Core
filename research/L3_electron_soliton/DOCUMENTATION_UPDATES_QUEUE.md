# Documentation Updates Queue — L3 Research

**Purpose:** Running log of all documentation edits (LaTeX manuscript chapters, markdown KBs, state-of-work trackers, YAML manifests, etc.) surfaced during Level-3 research. Not executed during the research program; reviewed and applied as a batch after the research concludes, so the physics work stays focused and the documentation receives a coherent, reviewed update.

**Flag-don't-fix discipline:** Items are queued here and adjudicated/applied only after the user reviews. Phase-1+ research findings that contradict or require amending current documentation are added promptly so nothing is forgotten.

**Format per entry:**
```
### [N] <short title>
- **File:** <path>
- **Kind:** <latex / markdown / config / yaml / other>
- **Location:** <section / line / label reference>
- **Change:** <what needs to change>
- **Why:** <research finding that surfaced the issue>
- **Surfaced:** <date / phase>
- **Status:** queued / in-review / applied
```

---

## Active queue

### [1] Vol 1 Ch 8 — trefoil-vs-unknot convention footnote
- **File:** [manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex)
- **Kind:** latex
- **Location:** §sec:electron_trefoil, around line 18 ("Trefoil Knot (3₁)") and §sec:golden_torus throughout
- **Change:** Add a clarifying footnote (or short paragraph) distinguishing *spatial flux-tube topology* (unknot $0_1$ — an unknotted ring) from *phase-winding structure on the toroidal shell* ($(2,3)$ torus knot traced by the preimage of a constant phase on the Clifford torus). The chapter currently conflates the two by describing the electron as "a minimum-crossing Trefoil Knot ($3_1$)" without the spatial-vs-phase-space distinction. This is consistent with Ch 8's math (which is entirely on the Clifford torus $\mathbb{T}^2 \subset S^3$) but the prose can mislead a first-time reader into imagining a knotted flux-tube curve in real space.
- **Why:** [src/ave/topological/faddeev_skyrme.py:17](../../src/ave/topological/faddeev_skyrme.py) states: *"The electron's topology is an unknot ($0_1$), but its phase winding number follows the (2,3) pattern with $c_3 = 3$ crossings."* Grant adjudicated (2026-04-19): the electron is an unknot spatially with $(2,3)$ phase winding. Ch 8 needs to reflect this to prevent cross-doc contradiction and to align with the Cosserat-unification framing canonized in `research/L3_electron_soliton/00_scoping.md` §2.
- **Surfaced:** Phase 0, 2026-04-19
- **Status:** queued

### [2] LIVING_REFERENCE.md + CURRENT_STATE.md — canonical Cosserat cross-link
- **File (primary):** [LIVING_REFERENCE.md](../../LIVING_REFERENCE.md)
- **File (secondary):** [.agents/handoffs/CURRENT_STATE.md](../../.agents/handoffs/CURRENT_STATE.md)
- **Kind:** markdown
- **Location:** wherever each doc discusses axioms, formalism, or architectural commitments
- **Change:** Add a canonical pointer to `research/L3_electron_soliton/00_scoping.md` §2 (the Cosserat canonization declaration) and §4 (the $\hat{\mathbf{n}} \leftrightarrow \boldsymbol{\omega}$ identity gap). Wording suggestion: *"Canonical formalism: Cosserat micropolar field theory on K4 substrate with Axiom 4 gradient-saturation. See `research/L3_electron_soliton/00_scoping.md` §2 for the declaration and §4 for the open identity gap."*
- **Why:** Without a cross-link from the top-level reference docs, future sessions will not know to treat the Cosserat commitment as canonical when touching field-theory topics. Discoverability is the entire mechanism; the canonization itself is already declared in the scoping doc.
- **Surfaced:** Phase 0, 2026-04-19
- **Status:** queued (held per user direction, 2026-04-19)

### [3] research/L3_electron_soliton/02_lagrangian_derivation.md — correct §8.3 overclaim
- **File:** [research/L3_electron_soliton/02_lagrangian_derivation.md](02_lagrangian_derivation.md)
- **Kind:** markdown (internal research doc)
- **Location:** §8.3 (screening constraint derivation sketch)
- **Change:** Re-word §8.3 to reflect the corrected understanding established in [`03_existence_proof.md`](03_existence_proof.md) §0 + §4.3. Specifically, the current §8.3 sketch frames $R\cdot r = 1/4$ as emerging from "Cosserat bending-energy extremization" — which overclaims. Replace with: the condition is a *topological quantization* forced by SU(2) half-cover + Clifford-torus area match, not a dynamical energy extremum. Retain the Cosserat framing as consistency check, not as derivation mechanism.
- **Why:** Writing out §4.3 of `03_` at publication rigor revealed that the naive "uniform-winding kinetic energy on the Clifford torus" gives $R/r = 3/2$ (or $2/3$ depending on winding assignment), not the Golden $R/r = \varphi^2 \approx 2.618$. The Cosserat Lagrangian alone does not dynamically select $R\cdot r = 1/4$; the condition is topological. Keeping §8.3 as-written would mis-state where the derivation's weight lies.
- **Surfaced:** Phase 1, 2026-04-19
- **Status:** **APPLIED 2026-04-20.** `02_` §8.3 rewritten with "topological quantization, not a dynamical extremum" framing.

### [5] research/L3_electron_soliton/02_lagrangian_derivation.md — correct §9 Pinning-2 factor-of-3 and rationale
- **File:** [research/L3_electron_soliton/02_lagrangian_derivation.md](02_lagrangian_derivation.md)
- **Kind:** markdown (internal research doc)
- **Location:** §9 (Cosserat moduli pinning), Pinning 2 specifically
- **Change:** Replace $\ell_{\text{Cos}} = \sqrt{3\gamma/G_c}$ with $\ell_{\text{Cos}} = \sqrt{\gamma/G_c}$; replace $G_c = 3\gamma$ with $G_c = \gamma$; replace the "pinned by $\nu_{\text{vac}} = 2/7$ operating point" rationale with "pinned by $\ell_{\text{Cos}} = \ell_{\text{node}}$ (Axiom 1 Nyquist match)." See [`04_moduli_pinning_check.md`](04_moduli_pinning_check.md) §3 for the corrected derivation.
- **Why:** The factor of 3 came from naively summing three bending moduli that happen to all equal $\gamma$ in the isotropic ansatz; the dimensionally-natural characteristic length uses the coefficient of $|\nabla\boldsymbol{\omega}|^2$ in the isotropic energy functional, which is $\gamma$, not $3\gamma$. The $\nu_{\text{vac}}$ attribution was a confusion with the translational Poisson ratio (which pertains to $K/G$, not to $G_c$). After correction, all three pinnings self-consistently close and all three §9.1 checks pass.
- **Surfaced:** Phase 1 moduli-pinning check, 2026-04-20
- **Status:** **APPLIED 2026-04-20.** `02_` §9 Pinning-2 rewritten; factor-of-3 removed, rationale corrected to $\ell_\text{Cos}=\ell_\text{node}$ Nyquist match, final pinning updated to $G_c = \gamma$.

### [6] research/L3_electron_soliton/01_ §10 + 02_ §7.2 + 03_ §4.3 — remove Reading-(a)↔(b) equivalence implications
- **File:** [research/L3_electron_soliton/01_identity_adjudication.md](01_identity_adjudication.md), [02_lagrangian_derivation.md](02_lagrangian_derivation.md), [03_existence_proof.md](03_existence_proof.md)
- **Kind:** markdown (internal research docs)
- **Location:** `01_` §10.1 Reading-(a) language; `02_` §7.2 "a $(2,3)$ dual winding realizes $Q_H = 6$ via $Q_H = w_1 \cdot w_2$" (end of §7.2); `03_` §4.3 "torus-knot preimages" phrasing anywhere
- **Change:** Remove or qualify any phrasing that equates Reading (b)'s factorized SU(2) sector with a Sutcliffe Hopfion (Reading a). Specifically, the end of `02_` §7.2 claims "$Q_H = w_1 \cdot w_2 = 6$" for Reading (b); this is false, $Q_H(\hat{\mathbf{n}}) = 0$ for Reading (b) as written. See [`05_reading_equivalence_check.md`](05_reading_equivalence_check.md) §4 for the calculation. Readings (b) and (c) in `01_` §10 may also be unified into a single "factorized SU(2) with joint $(w_1, w_2)$ invariant" reading, per `05_` §8.2 — pending user adjudication.
- **Why:** The equivalence check revealed that (a) and (b) describe genuinely different topological sectors. Keeping equivalence-implying language would mislead future readers and introduce an error into the load-bearing topology-invariants claim.
- **Surfaced:** Phase 1 equivalence check, 2026-04-20
- **Status:** **APPLIED 2026-04-20** via universal-operator reframing supersession. `01_` §10.1 amended (two-step: (b)/(c) merge, then full supersession); `02_` §7.2 rewritten with $c = 3$ scalar invariant; `03_` §4.1 references updated. False "Q_H = w_1 × w_2 = 6" claim removed.

### [7] Resolve Williamson-van der Mark (2,1) vs AVE (2,3) winding tension via Cosserat→EM projection map
- **File (new):** suggested path `research/L3_electron_soliton/06_winding_index_projection.md`
- **Kind:** markdown (new research doc) + possible touch of `02_lagrangian_derivation.md` §7.2 to annotate the projection relationship
- **Location:** new Phase-1 wrap-up doc
- **Change:** Derive the explicit projection from AVE's SU(2)-Cosserat winding pair $(2, 3)$ to the semi-classical EM-phase winding of a Williamson-van der Mark-type toroidal photon model. Under user adjudication (2026-04-20) that the two indices count different observables, show which Cosserat invariant produces a semi-classical EM-phase count matching Williamson-van der Mark's preferred 2:1 — and verify the other Cosserat invariant (the $(2,3)$ second number) has a consistent interpretation in the semi-classical limit (e.g., as a fibre-phase count invisible to a pure-EM observer).
- **Why:** Williamson-van der Mark (B25) is the most directly comparable prior art for AVE's electron-as-torus claim. AVE uses $(2,3)$ winding; Williamson-van der Mark uses 2:1. User adjudicated this as option (1): different invariants being counted. But the adjudication is not written down formally anywhere yet; until it is, "why $(2,3)$ not $(2,1)$?" is an open question any reviewer will ask. The projection map is the rigorous answer.
- **Surfaced:** Phase 1 bibliography expansion, 2026-04-20
- **Status:** queued (Phase-1 wrap-up task)

### [8] Resolve AVE major-minor convention for "(2,3)" assignment on Clifford torus
- **File:** [research/L3_electron_soliton/02_lagrangian_derivation.md](02_lagrangian_derivation.md) §7.2 + [03_existence_proof.md](03_existence_proof.md) §4.3 (anywhere that assigns windings to major/minor cycles)
- **Kind:** markdown (internal research docs) + potentially manuscript Ch 8 annotation
- **Location:** §7.2 of `02_` and wherever $(w_1, w_2) = (2, 3)$ is tied to $(\theta_1, \theta_2)$
- **Change:** Explicitly state and justify whether $w_1 = 2$ lives on the major cycle ($\theta_1$, radius $R = \varphi/2$) or the minor cycle ($\theta_2$, radius $r = (\varphi-1)/2$). Currently the assignment is implicit. Given Williamson-van der Mark (B25) puts their "2" on the major cycle, and the natural matching under the Cosserat → EM projection ([`06_winding_index_projection.md`](06_winding_index_projection.md) §3) is "major = 2," the canonical AVE convention should be: $w_1 = 2$ on $\theta_1$ (major), $w_2 = 3$ on $\theta_2$ (minor). If the AVE corpus's physical intuition disagrees, the opposite convention must be made explicit and §3 of `06_` revised accordingly.
- **Why:** `06_` §6 flagged this as an unresolved convention. The (2,3) vs (2,1) resolution depends on the major-minor assignment. Leaving it implicit risks a silent sign/convention error in later Phase-3 numerics.
- **Surfaced:** Phase 1 winding-index projection, 2026-04-20
- **Status:** queued (Phase-1 wrap-up task)

### [9] Revise 02_ §7.2 topological boundary condition from (w_1,w_2) pair to scalar c=3
- **File:** [research/L3_electron_soliton/02_lagrangian_derivation.md](02_lagrangian_derivation.md) §7.2
- **Kind:** markdown (internal research doc)
- **Location:** §7.2 of `02_` (topological boundary condition on Clifford shell)
- **Change:** Replace the Hopfion-literature-style dual-winding specification (winding 2 on $\theta_1$, winding 3 on $\theta_2$) with an AVE-native crossing-count specification: the electron ground state is characterized by $c = 3$ (Op10 scalar topological invariant). Retain the SU(2) field formulation from C3 canonization. Drop the factorized "base + fibre" phase specification — it was imported from Hopfion literature and does not match AVE's own universal-operator invariant basis.
- **Why:** Survey of [`src/ave/core/universal_operators.py`](../../src/ave/core/universal_operators.py) in [`07_universal_operator_invariants.md`](07_universal_operator_invariants.md) establishes that AVE's native topological invariant is the scalar crossing count $c$ (used by Op10 = Junction Projection Loss), not a winding pair. The $(w_1, w_2)$ framing was a category error.
- **Surfaced:** Phase 1 universal-operator reframing, 2026-04-20
- **Status:** **APPLIED 2026-04-20.** `02_` §7.2 rewritten with scalar $c = 3$ framing; §7.3 updated accordingly.

### [10] Revise 06_ §3, §5, §8 projection map to AVE-native c-based framing
- **File:** [research/L3_electron_soliton/06_winding_index_projection.md](06_winding_index_projection.md) §3 (major-cycle direct agreement), §5 (consistency prediction), §8 (open questions)
- **Kind:** markdown (internal research doc)
- **Location:** §§3, 5, 8 of `06_`
- **Change:** Simplify the projection map under the `07_` finding. AVE and WvdM both speak $(p, q)$ torus-knot language but on different tori (phase-space Clifford for AVE; physical-space for WvdM), giving $c = 3$ for AVE and $c = 0$ (unknot; $(2,1)$ is an unknotted curve) for WvdM. The Cosserat → EM projection chain is still structurally correct but the "major vs minor" reasoning in §3 should be replaced with the two-different-tori framing.
- **Why:** The `07_` reframing shows that AVE-native invariant is scalar $c$, not a pair. The `06_` §3 "major cycle agreement" reasoning was based on Hopfion-literature conventions that don't apply natively. Cleaner story: both pictures use $(p,q)$ notation but for different tori.
- **Surfaced:** Phase 1 universal-operator reframing, 2026-04-20
- **Status:** **APPLIED 2026-04-20** (amendment box). Added ⚠ amendment at top of `06_` pointing to `07_` as cleaner resolution; preserved §§1–8 as traceable reasoning history. §§1–2 (two-tori distinction) and §5 (3:1 tube-wrap consistency check for Phase 3) retained as still-valuable; §§3–4 $(w_1, w_2)$ reasoning superseded by $c$-based framing.

### [11] Revise 05_ §8 three-readings framework — superseded by universal-operator reframing
- **File:** [research/L3_electron_soliton/05_reading_equivalence_check.md](05_reading_equivalence_check.md) §8 adjudication questions, §7 "Where the Cosserat canonization points"
- **Kind:** markdown (internal research doc)
- **Location:** `05_` §§6, 7, 8
- **Change:** Add an amendment note: under the `07_` universal-operator reframing, the Reading (a) / Reading (b) distinction is superseded. Both are external-literature conventions that don't match AVE's own Op10 invariant basis. What remains is: (i) the field-formulation choice is C3 SU(2) embedding (from `01_` §10, still valid), and (ii) the topological invariant is $c = 3$ (from `07_`, supersedes all readings).
- **Why:** The reading-equivalence check in `05_` was a valuable process that surfaced the category error. But now that the error is identified and resolved via `07_`, the three-readings framing is itself superseded.
- **Surfaced:** Phase 1 universal-operator reframing, 2026-04-20
- **Status:** **APPLIED 2026-04-20** (amendment box). Added ⚠ amendment at top of `05_` pointing to `07_`. §§1–6 retained as traceable reasoning; §§7–8 recommendations marked as overridden.

### [8] Resolve AVE major-minor convention for "(2,3)" assignment on Clifford torus — RESOLVED via 07_
- **Resolution:** No assignment needed. The scalar crossing count $c = 3$ is the AVE-native topological invariant (Op10, universal-operator basis), not a winding pair. The major-vs-minor assignment was a Hopfion-literature category error. See [`07_universal_operator_invariants.md`](07_universal_operator_invariants.md) §4.1.
- **Status:** **RESOLVED** 2026-04-20 via `07_`. Keeping entry in queue as a resolved-item marker. Requeue only if Phase-3 numerics reveals an axis-dependent observable not captured by the universal operators.

### [12] research/L3_electron_soliton/08_discretization_design.md — correct §3.2 consistency claim
- **File:** [research/L3_electron_soliton/08_discretization_design.md](08_discretization_design.md) §3.2 (discrete kinematic tensors)
- **Kind:** markdown (internal research doc)
- **Location:** §3.2 — where "second-order consistency" is stated for the nearest-neighbor tetrahedral gradient
- **Change:** Replace the "second-order consistency" wording with an honest statement: the naive nearest-neighbor tetrahedral-gradient estimator is **first-order consistent**, with leading error proportional to mixed second partials $\partial_k\partial_l V$ (for distinct $k, l \neq j$). Second-order consistency requires the A+B symmetrized estimator derived in [`09_phase2_wrapup.md`](09_phase2_wrapup.md) §1.4.
- **Why:** `08_` overclaimed. Honest analysis in `09_` §1 showed the triple-sum $\sum_\ell p_\ell^j p_\ell^k p_\ell^l$ is non-zero for distinct indices ($= 4$), producing an $O(\Delta x)$ error. Phase-3 implementation efforts need accurate expected convergence rates.
- **Surfaced:** Phase 2 wrap-up, 2026-04-20
- **Status:** queued

### [13] src/ave/topological/cosserat_field_3d.py — fix saturation-gradient bug
- **File:** [src/ave/topological/cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) `_stress_and_couple_stress()`
- **Kind:** code bug
- **Change:** The analytical derivative of the saturated energy `W_sat = W_bare · S²(|X|)` with respect to tensor component `X_mn` disagrees with finite-difference by factor ~10 and often wrong sign at sites with moderately saturated field.
- **Why:** Phase-3 validation revealed that without saturation, the Cosserat quadratic Lagrangian's unique minimum is the trivial vacuum — the soliton decays. Saturation is LOAD-BEARING for soliton stability.
- **Surfaced:** Phase 3 first-pass validation, 2026-04-20
- **Status:** **APPLIED 2026-04-20** — full JAX refactor. Module now uses `jax.value_and_grad` on the energy functional; hand-derived stress tensors removed entirely. New strict test `test_saturated_gradient_matches_finite_difference_under_activation` verifies FD agreement at 1e-5 rtol in the saturation-active regime (previously would fail at ~10× at same sites). x64 mode enabled via `jax.config.update`. JIT-compiled energy and gradient functions give ~5–10× speedup; Metal GPU backend will apply when `jax-metal` is installed.

### [14] Phase-3: preserve (2,3) topology through gradient descent
- **File:** [src/ave/topological/cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py)
- **Kind:** numerical-physics enhancement
- **Change:** Phase-3 validation with correct saturation gradient (per [13] APPLIED) now shows that (2,3) topology is NOT preserved during gradient descent at 32³ resolution — `c` drops from 3 to 0, R/r ratio does not converge to $\varphi^2$. Field unwinds through the discrete lattice faster than the saturation barrier can prevent. Needs one or more of:
  - Higher grid resolution ($64^3$, $96^3$) — reduces discrete topological-slip rate.
  - Finer lattice spacing (dx < 1) with rescaled (R, r) — increases tube resolution.
  - Topology-preserving solver variant: constrained gradient, projected descent, or Landau–Lifshitz-style precession-plus-damping that naturally conserves winding.
  - More robust c-extraction diagnostic (cross-check via Op11 topological-curl integral over full shell, not just a single minor-circle sample).
- **Why:** Fix [13] removed the saturation-gradient bug, but revealed that the solver as-is still doesn't complete Phase-3 end-to-end validation because topology isn't preserved. This is the next concrete blocker to demonstrating "electron emerges from Cosserat Lagrangian at Golden Torus."
- **Surfaced:** Phase 3 second-pass validation (JAX), 2026-04-20
- **Status:** queued — blocks Phase-3 completion.

### [4] research/L3_electron_soliton/03_existence_proof.md — complete formal proofs in §3 and §5
- **File:** [research/L3_electron_soliton/03_existence_proof.md](03_existence_proof.md)
- **Kind:** markdown (internal research doc)
- **Location:** §3 (existence, currently sketched via Faddeev-Skyrme-literature adaptation); §5 (uniqueness, currently sketched via modulus-space argument)
- **Change:** Replace the sketch-level existence and uniqueness arguments with formal proofs, including: (a) explicit coercivity bound for the Cosserat sector energy, (b) regularity argument for the weak-limit minimizer, (c) Palais-Smale or concentration-compactness for mass escape, (d) modulus-space uniqueness argument specific to the $(2,3)$ Cosserat sector.
- **Why:** Publication rigor target (`00_scoping.md` §0). Current sketches invoke "standard Hopfion-literature adaptations" which are technically correct but not publication-ready.
- **Surfaced:** Phase 1, 2026-04-19
- **Status:** **TABLED 2026-04-20** per user direction. Phase-1 theoretical spine is complete as a research artifact; formal rigor upgrade of §3 and §5 is deferred. If/when the research targets publication, this becomes a prerequisite deliverable. Retained in the active queue as a known outstanding item.

---

## Applied

*(none yet)*
