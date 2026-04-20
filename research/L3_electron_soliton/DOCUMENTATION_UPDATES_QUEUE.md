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

---

## Applied

*(none yet)*
