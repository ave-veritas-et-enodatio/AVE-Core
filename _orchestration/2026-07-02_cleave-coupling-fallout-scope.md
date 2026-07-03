# Cleave-01 coupling adjudication — fallout inventory + scope

**Date:** 2026-07-02
**Branch:** `analysis/cleave-coupling-chern-adjudication`
**Upstream:** receipts `research/2026-07-02_cleave-coupling-derivation_adjudication.md`;
FROZEN prereg `research/2026-07-02_cleave-registry-pump-chern_prereg.md`;
RESULT `research/2026-07-02_cleave-registry-pump-chern_result.md`.

**What happened.** The Cleave-01 plate-displacement → topological-charge coupling `Q = ξ_topo·x`
(labelled "analytically derived") was found ASSERTED (a def-tk1xfm unit-bridge), not derived. A
three-angle adversarial derivation + cross-examination returned **UNDECIDABLE-AT-PAPER**; the sole
surviving mechanism class = an adiabatic Thouless registry pump over the 4₁ screw. Grant ruled (b):
the engine adjudicates via OA-anchor reproduction. The dual-reading Chern driver **ran** and returned
**NULL-DERIVED** (C_slide = 0, C_lock = 0, gapped + converged, toy gate PASS) for the operator-derived
construction — bounded by an honest scope caveat (a full N-band `Link(∂Ω, F)` srs solve is the gated
upgrade path).

Each fallout item is tagged **[IMMEDIATE]** (this session, minimal KEEP-BOTH cross-ref) or
**[GATED-ON-RESULT]** (queued; the result now exists, so several GATED items are unblocked for a
*follow-on* session — the full rewrites are still NOT this session's scope). The auditor lands the
manual/manuscript entries; this doc surfaces them.

---

## Item 1 — vol4 ch11 `project-cleave-01.md` coupling-status  **[IMMEDIATE cross-ref; full rewrite GATED]**

- **Site:** `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md:32`
  — "The induced topological charge is **analytically derived** as: `Q = ξ_topo·x`".
- **Change (immediate, KEEP-BOTH):** one status line pointing "analytically derived" → "unit-bridge
  + mechanism-gated: registry-pump candidate, Chern-gated → NULL-DERIVED for the operator-derived
  construction (2026-07-02)." Preserve the legacy prose; add the cross-ref to the receipts + result.
- **Full rewrite (GATED):** reframing the bench as an **Axiom-2 null-test** (nonzero floor →
  falsifies AVE) rather than a confirmation of a derived pump. Follow-on session.

## Item 2 — `cleave-01-requirements-boundary-conditions.md` slope + new corners  **[IMMEDIATE cross-ref; full after]**

- **Site:** `:19` (slope = "consistency-class echo"), `:27` (`CLV-REQ-FLOOR = 414.9 fC/µm`).
- **Change (immediate):** cross-ref line noting the slope conditioning result — the exact 414.9 is
  NOT integer-C-reachable (needs C = 2√2); if a pump existed it would give `C × {146.7 | 586.8}` fC/µm.
  The datasheet already demotes the slope to non-gating (`:19`), so this reinforces, not overturns.
- **New corners as NEW axes alongside legacy (KEEP-BOTH):** (a) sidereal/orientation
  period-modulation (screw-axis fingerprint, NOT (qℓ)⁴-suppressed); (b) moving-dielectric-slab-at-
  fixed-gap exact-null control; (c) STAIRCASE phase-native readout (quantized charge per closed
  2-axis cycle, V-independent, present at V=0; `slope-without-staircase = dictionary echo`). Full
  datasheet landing GATED (follow-on) — minimal cross-ref now.

## Item 3 — AVE-Bench-FemtoElectrometer sibling repo stale sites  **[SEPARATE SESSION — cross-repo discipline]**

Per cross-repo-session-scope: these are Femto-repo edits, NOT performed here. Enumerated exact sites
(`analytically derived` + exact-slope framing that predates this adjudication):
- `README.md` — carries the exact slope / "analytically derived" bench framing.
- `docs/glossary.md` — ξ_topo / slope definitions.
- `hardware/TEST_PROCEDURE.md` — round-1 "standard EE predicts Q→0" + slope discriminator framing
  (already flagged stale by `project-cleave-01.md:100`, F-R2-3).
- `docs/open_questions.md` — round-1 framing.
- `hardware/cad/reference_design.md`, `hardware/RE-SPEC.md`, `hardware/DESIGN_LOG.md`,
  `hardware/ORDERING.md`, `AGENTS.md`, `CLAUDE.md` — exact-slope (414.9 / 0.415 pC / 41.5 mV) sites.
- **Note:** the round-2 analysis docs (`docs/analysis/2026-06-04_*`, `2026-06-03_*`) are already
  CURED (4-corner / gap-independence / positive-control) per `project-cleave-01.md:98-100` — do NOT
  re-touch those; the stale sites are the round-1 default-checkout artifacts.
- **Action:** SEPARATE Femto-repo session; add the "coupling = unit-bridge + registry-pump
  NULL-DERIVED" reframe alongside the (already-landed) 4-corner reframe.

## Item 4 — `ivim-RA-adjudication.md` doc-109 dependency  **[IMMEDIATE one-liner]**

- **Site:** `research/2026-06-03_ivim-RA-adjudication.md:108-117` (the sliding-vs-locked / doc-109
  "RULED OUT, not gated" note — scoped to the piezo E-field channel).
- **Change (immediate):** one-liner adding Cleave as a DEPENDENT of the sliding-vs-locked fork and
  recording the (b) engine-adjudication path: doc-109's piezo-channel closure is distinct from the
  Cleave registry-pump reading; Grant (b) reopened the fork for the registry-pump channel, now
  settled by the engine as NULL-DERIVED for the operator-derived construction. (Flag-don't-fix: do
  NOT reconcile the two — they are different transducers; see receipts §f scope note.)

## Item 5 — forward-prediction register Cleave/Ax2 row  **[GATED-ON-RESULT]**

- **Site:** the Ax2 / Cleave forward-prediction row (in the vol4 claim-quality / closure-roadmap
  family — exact leaf to be confirmed by the auditor at landing).
- **Change (gated):** CONDITIONAL flag on the Cleave/Ax2 row — the bench tests an Axiom-2 null (a
  nonzero gap-independent floor falsifies AVE), NOT a derived-pump confirmation. The derived-pump
  reading is NULL-DERIVED. Follow-on.

## Item 6 — ξ_topo cascade dependents (B4-PROTEIN, C9-LEVITATION, C16-TORSION, B5/B6/B7-PONDER)  **[scope now, action GATED]**

- **Scope question (each dependent):** does it assume the displacement COUPLING `Q = ξ_topo·x` (a
  *mechanism* — now NULL-DERIVED), or merely the ξ_topo UNIT-BRIDGE (a units identity — untouched)?
- **Sites to audit (follow-on):** `metric-levitation-limit.md` (C9),
  `electromechanical-transduction-constant.md` (vol5, B4/B-family), the C16-torsion + B5/B6/B7-ponder
  leaves. Most cascade uses are expected to ride the UNIT-BRIDGE (ξ_topo as a C/m constant), which
  this result does NOT disturb — only a use that assumes a *pumped* displacement charge is affected.
- **Action:** scope each now (this doc); the actual per-leaf audit + any walk-back is GATED and
  follow-on. Preliminary read: the cascade is likely SAFE (unit-bridge, not coupling-dependent), but
  each must be checked before that is asserted.

## Item 7 — `def-tk1xfm` / `translation-circuit`  **[GATED-ON-RESULT]**

- **Sites:** `common/vocabulary-register.md:348-357` (def-tk1xfm, the "identity-by-translation, NOT
  a derivation" ceiling), `vol4/circuit-theory/ch1-vacuum-circuit-analysis/translation-circuit.md:17-26,41,660`.
- **Reading of this result:** the NULL-DERIVED verdict **REAFFIRMS the def-tk1xfm ceiling** — no
  derived-mechanism instance emerged; `Q = ξ_topo·x` stays a unit-bridge, not a pump. (Had C≠0, that
  would have been the FIRST derived-mechanism instance and an upgrade path for the ceiling.) The
  gated upgrade path (§5 of the result, full N-band Link solve) is the only route that could still
  lift the ceiling; until then the ceiling holds.
- **Action:** GATED. A one-line note that the ceiling is reaffirmed can land with the auditor.

## Item 8 — OA cross-links: k→0 OPEN + the 2√2 ambiguity  **[IMMEDIATE check]**

- **k→0 coupling (immediate cross-ref):** the Cleave slope magnitude is coupled to the OA
  k→0 continuum-extraction OPEN (`chiral-vector-tlm-phase1_result.md:142`) — add to the Cleave
  datasheet open-items (done via the receipts §f; a one-line cross-ref at the OA leaf is the
  reciprocal link).
- **2√2 ambiguity (immediate check, one hour):** `chiral-vector-tlm-phase1_result.md:105` converts
  by dividing by `a_cell_physical`; Angle A alleged a ×2√2 slip. **Checked this session:** the driver's
  anchor cross-check surfaced the same z-unit ↔ physical-length / sign-convention split (result §3) —
  the bare-pitch formula reproduces srs-R's magnitude but not the enantiomorph sign (which lives in
  the writhe operator). **The one-hour check did NOT settle it** (it is a real convention ambiguity,
  not an arithmetic bug — the auditor's earlier regrade stands: OPEN, not confirmed). Documented as
  still-OPEN; the null result does not depend on it.

## Item 9 — staircase readout → Cleave trade-study knob D4  **[GATED-ON-RESULT]**

- **Site:** `cleave-01-trade-study-decision-register.md` (D4 drift-scheme knob).
- **Change (gated):** the STAIRCASE phase-native readout (quantized charge per closed 2-axis drive
  cycle, V-independent) is the chord-grade discriminator; it evolves the D4 readout-scheme trade
  (step-differencing / DC-restore) toward a phase-native / cyclic-drive option. Follow-on.

## Item 10 — claim-quality / solidity entries  **[IMMEDIATE]**

- **Minted (in the receipts):** `clm-cleave-coupling-adjudication` — adjudication/consistency-class,
  solidity CANDIDATE → now downgraded by the run to **NULL-DERIVED for the operator-derived
  construction** (result §5 scope caveat bounds it). The auditor lands the formal claim-quality row.
- **Action:** surface the entry (done, receipts §claim-quality); the auditor adds the row to
  `vol4/claim-quality.md` with the NULL-DERIVED status + the scope caveat + the gated upgrade path.

---

## Summary of what THIS session landed vs surfaced

- **Landed (this branch):** receipts, FROZEN prereg, driver + tests (engine_sim-partitioned), result
  doc, this fallout scope, and the [IMMEDIATE] minimal KEEP-BOTH cross-refs (items 1, 4, 8, 10).
- **Surfaced for the auditor / follow-on:** items 2 (full datasheet), 3 (SEPARATE Femto session),
  5, 6, 7, 9 — plus the formal claim-quality row.
- **Unresolved flags (surfaced, not fixed):** the 2√2 / sign-convention ambiguity (item 8, OPEN);
  the OA k→0 coupling (item 8); the full N-band `Link(∂Ω, F)` srs upgrade path (result §5).

---

## ★ MISSION-2 EXECUTION STATUS (2026-07-02, branch `analysis/cleave-nband-chern`)

The N-band upgrade RAN (the gated §5 path): `research/2026-07-02_cleave-registry-pump-chern-nband_result.md`
— **NULL-CONFIRMED-FINAL** ($C_N=0$ both readings, both enantiomorphs, gapped + converged, VOK PASS).
The coupling question is now **CLOSED** per Grant's frozen last-roll pre-commitment. With the FINAL
verdict in hand, the previously-[GATED-ON-RESULT] AVE-Core items are EXECUTED this branch:

- **Item 1 (project-cleave-01.md coupling-status) — EXECUTED.** Full rewrite: NULL-CONFIRMED-FINAL
  header + **Outcome-C rescope** (Outcome C is now the AVE-consistent expectation, NOT a falsification;
  the bench is a one-sided corroborative-null discriminator; legacy chord-gating prose preserved as
  historical per Rule 12, no in-doc banner). Back-linked to `clm-clvchn` (frontmatter + Tier-2 marker).
- **Item 2 (requirements leaf) — EXECUTED.** Final disposition: the three new corners are **moot for
  THIS bench** (fingerprints of the now-null mechanism), retained as diagnostics for any future
  REOPENS; legacy `CLV-REQ-*` specs kept for the one-sided-falsifier reading. Supersedes the #454
  "add-as-axes" note.
- **Item 5 (forward-prediction register) — EXECUTED.** New §2.9: Cleave/Ax2 = **RETIRED-AS-DISCRIMINATOR**
  (corroborative-null class).
- **Item 7 (def-tk1xfm) — EXECUTED.** Ceiling **REAFFIRMED by a computed null** (KEEP-BOTH one-liner in
  the vocabulary-register entry).
- **Item 10 (claim-quality) — EXECUTED.** `clm-clvchn` row minted in `vol4/claim-quality.md`
  (solidity 0.85, NULL-CONFIRMED-FINAL, scope history 2-band → N-band).
- **STILL REMAINING:** Item 3 (AVE-Bench-FemtoElectrometer stale sites) stays **[SEPARATE SESSION]**
  per cross-repo discipline — the sibling repo is NOT touched this branch. Item 6 (ξ_topo cascade
  coupling-vs-unit-bridge per-leaf audit) remains a follow-on scope item (preliminary read: SAFE =
  unit-bridge, the null does not disturb unit-bridge uses). Item 9 (D4 trade-study staircase knob) is
  moot given the retirement (folded into item 2's disposition).
- **Unresolved flags carried:** the 2√2 / sign-convention ambiguity (still OPEN; the null does not
  depend on it); the OA k→0 coupling (OPEN). The N-band `Link(∂Ω,F)` upgrade path (result §5.2 / the
  claim-quality strengthen-by) is the only remaining route and is a *strengthen-by*, not a reopen.
