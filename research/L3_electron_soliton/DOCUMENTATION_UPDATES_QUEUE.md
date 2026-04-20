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
- **Status:** queued

### [5] research/L3_electron_soliton/02_lagrangian_derivation.md — correct §9 Pinning-2 factor-of-3 and rationale
- **File:** [research/L3_electron_soliton/02_lagrangian_derivation.md](02_lagrangian_derivation.md)
- **Kind:** markdown (internal research doc)
- **Location:** §9 (Cosserat moduli pinning), Pinning 2 specifically
- **Change:** Replace $\ell_{\text{Cos}} = \sqrt{3\gamma/G_c}$ with $\ell_{\text{Cos}} = \sqrt{\gamma/G_c}$; replace $G_c = 3\gamma$ with $G_c = \gamma$; replace the "pinned by $\nu_{\text{vac}} = 2/7$ operating point" rationale with "pinned by $\ell_{\text{Cos}} = \ell_{\text{node}}$ (Axiom 1 Nyquist match)." See [`04_moduli_pinning_check.md`](04_moduli_pinning_check.md) §3 for the corrected derivation.
- **Why:** The factor of 3 came from naively summing three bending moduli that happen to all equal $\gamma$ in the isotropic ansatz; the dimensionally-natural characteristic length uses the coefficient of $|\nabla\boldsymbol{\omega}|^2$ in the isotropic energy functional, which is $\gamma$, not $3\gamma$. The $\nu_{\text{vac}}$ attribution was a confusion with the translational Poisson ratio (which pertains to $K/G$, not to $G_c$). After correction, all three pinnings self-consistently close and all three §9.1 checks pass.
- **Surfaced:** Phase 1 moduli-pinning check, 2026-04-20
- **Status:** queued

### [6] research/L3_electron_soliton/01_ §10 + 02_ §7.2 + 03_ §4.3 — remove Reading-(a)↔(b) equivalence implications
- **File:** [research/L3_electron_soliton/01_identity_adjudication.md](01_identity_adjudication.md), [02_lagrangian_derivation.md](02_lagrangian_derivation.md), [03_existence_proof.md](03_existence_proof.md)
- **Kind:** markdown (internal research docs)
- **Location:** `01_` §10.1 Reading-(a) language; `02_` §7.2 "a $(2,3)$ dual winding realizes $Q_H = 6$ via $Q_H = w_1 \cdot w_2$" (end of §7.2); `03_` §4.3 "torus-knot preimages" phrasing anywhere
- **Change:** Remove or qualify any phrasing that equates Reading (b)'s factorized SU(2) sector with a Sutcliffe Hopfion (Reading a). Specifically, the end of `02_` §7.2 claims "$Q_H = w_1 \cdot w_2 = 6$" for Reading (b); this is false, $Q_H(\hat{\mathbf{n}}) = 0$ for Reading (b) as written. See [`05_reading_equivalence_check.md`](05_reading_equivalence_check.md) §4 for the calculation. Readings (b) and (c) in `01_` §10 may also be unified into a single "factorized SU(2) with joint $(w_1, w_2)$ invariant" reading, per `05_` §8.2 — pending user adjudication.
- **Why:** The equivalence check revealed that (a) and (b) describe genuinely different topological sectors. Keeping equivalence-implying language would mislead future readers and introduce an error into the load-bearing topology-invariants claim.
- **Surfaced:** Phase 1 equivalence check, 2026-04-20
- **Status:** queued (pending §8 adjudication in `05_`)

### [4] research/L3_electron_soliton/03_existence_proof.md — complete formal proofs in §3 and §5
- **File:** [research/L3_electron_soliton/03_existence_proof.md](03_existence_proof.md)
- **Kind:** markdown (internal research doc)
- **Location:** §3 (existence, currently sketched via Faddeev-Skyrme-literature adaptation); §5 (uniqueness, currently sketched via modulus-space argument)
- **Change:** Replace the sketch-level existence and uniqueness arguments with formal proofs, including: (a) explicit coercivity bound for the Cosserat sector energy, (b) regularity argument for the weak-limit minimizer, (c) Palais-Smale or concentration-compactness for mass escape, (d) modulus-space uniqueness argument specific to the $(2,3)$ Cosserat sector.
- **Why:** Publication rigor target (`00_scoping.md` §0). Current sketches invoke "standard Hopfion-literature adaptations" which are technically correct but not publication-ready.
- **Surfaced:** Phase 1, 2026-04-19
- **Status:** queued (Phase-1 wrap-up task)

---

## Applied

*(none yet)*
