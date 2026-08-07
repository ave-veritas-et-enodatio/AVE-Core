# Lane brief — Ax4 state-vector / residence adjudication (2026-08-06)

**Goal (prove-or-disprove level):** determine what state vector the Ax4 kernel-shape
theorem norms — i.e. whether the derivation FORCES the saturation-tank inventory, or the
inventory is an input the derivation is agnostic to. This is the combine-fork
(L2-vs-L∞-across-grades) recast as a residence question; the collapse rationale and ruled
context live in `_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-
rescope-v2.md` and `...2026-08-06-rulings-decision-batch.md` R6. **Substrate adjudicates,
not fiat** — deliver derivation + canon reconciliation, not a preference.

**SVA §0 header (leaf v0.2, 11 rows) MANDATORY on the prereg. Freeze-first. PR opens
`[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.**

## Questions, in order

1. **Reach of the dissolution.** Does the 2026-07-02 buckling result's dissolution (the
   (A,S) load-response pair) address DP-3's grade-into-A aggregation at all?
   `axiom-register.md:189` says dissolved; `:190`/`:232` + `trampoline-framework.md:255`
   say open (= FLAG-COMBINE-SPLIT). Read both source derivations; rule ONE-QUESTION or
   TWO-QUESTIONS with verbatim evidence. If TWO, draft the register reconciliation that
   scopes `:189` to load-response only.
2. **The state vector.** Re-derive the Ax4 kernel-shape theorem asking: an L2 norm OF
   WHAT? Does the derivation identify the normed object (per-element stored energy vs
   total cell energy), or is that an input? If forced, the fork closes here — say which
   member and show the forcing step.
3. **γ_c residence.** Where does twist-coupling energy live — in the bond, or through the
   material? Derive what each residence implies for cross-grade softening; state the
   discriminating consequence (both grades loaded simultaneously — note the κ=0 degeneracy
   makes single-grade configurations non-discriminating).
4. **Phase-level rider.** State explicitly at which phase level the answer holds
   (crystal-phase effective law vs substance-level law) — the monist walk (framing note
   `research/2026-08-06_rotation-substance-ontology_framing-note.md` §5, UN-AUDITED)
   admits a unified substance budget projecting as per-grade at crystal level. Do not
   adjudicate the ontology; scope the answer.
5. **F6 vacated cite.** The 2026-07-02 combine-rule result cites `cosserat_field_3d.py
   :411` as per-grade evidence; `:411` is the aggregated line, and its `:612-613` cite has
   drifted. Vacate and re-derive the engine-state paragraph fresh (vacated-cite pattern —
   dated surface-note on the frozen doc, never a rewrite).

## Fences

- **NOT an engine-run adjudication.** The engine codes the answer three ways
  (`:767-768` per-grade elastic; `:486-488`/`:409-413` aggregated at `k_refl=1.0`;
  `:619/:681` sym-only+V+chirality — FLAG-A2DEF is 3, not 2). A simulation would read back
  whatever was coded — the stencil-lens failure mode. Derivation + consistency only.
- `src/ave` stays byte-untouched; the three-definitions inconsistency is a physics-review
  item, not a code bug to silently close.
- Two-method receipts with named regex engines on every absence claim.
- Pointers-not-values: re-derive every number/quote you consume from the cited records.

---
**DATED SCOPE UPDATE 2026-08-06 PM (Tier-2 on #905, finding A2):** item 5's vacated-cite
characterization is corrected — the 2026-07-02 doc's real defect is a
**within-vs-across-grade misclassification** (it labels the `:411` aggregation "L∞ across
grades, L2-sum within a grade"; ε and κ are different grades, so `:411` IS the
across-grade aggregation), not a bare line miss. Scope addition: the SAME misread, with
the same `:411,600` cite (`:600` now drifted to a docstring line), sits in CANON at
`trampoline-framework.md:255` — vacate and re-derive that site too, same pattern. Also
consume the corrected residence map in
`2026-08-06-ruling-kernel-collapse-rescope-v2-correction.md` C2 (three definitions,
two live functionals + a separate S11 objective; definition 3 is the Phase-4 default via
`k4_cosserat_coupling`) as the authoritative engine-state statement.

---
**DATED SCOPE UPDATE 2026-08-06 late (ruling record
`2026-08-06-rulings-sourcing-go-pitch-walk.md`):** three converging questions now
formally in this lane's scope — all one object (which element owns which budget):
(a) **FLAG-FORK-RESIDENCE** (PR #914): the I_ω lane's ARM-0/ARM-1 fork (does the
strain grade load the rotational sector; which element is the gap's kinetic
coefficient) is this lane's question 3 seen from the kinetic side — read #914's
result §2 before deriving; (b) **SYM-class** (#914 Tier-2 Q2): the r_sat approach's
ε₁₁ = 7GM/(c²r) is a RADIAL PRINCIPAL strain — is that a realization of the SYM
(symmetric-gravity) voice at all, or does L-A resolve to the carve-out on
anisotropy grounds alone?; (c) **the pitch question** (R19, Grant LEAN recorded:
rotor moment is a node property, bond strain does not re-machine it — nodes stay,
waves shrink): derive whether j(ℓ) arises, i.e. whether canon's fixed-topology
primitive also fixes the per-element moment under strain. The lean is walk-level;
derive-don't-adopt.
