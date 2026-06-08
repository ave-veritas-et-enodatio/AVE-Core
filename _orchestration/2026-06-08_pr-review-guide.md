# 2026-06-08 PR review guide — 21 open PRs (#117–#137)

**Purpose.** Grant reviews each PR himself. This is the per-PR fast-review
checklist, ordered by dependency + risk so the careful ones cluster and the fast
ones batch. Every PR was verified `OPEN` / non-draft / base `main` /
`mergeable:MERGEABLE` against `origin/main` HEAD `63e6671a` (`gh pr list
--state open`, 2026-06-08).

**DO NOT merge from this guide** — it is a review aid; Grant merges.

## How to use this guide

- **Risk tiers**: `low-additive` (new doc/prereg/figure, no corpus edit) ·
  `code` (new script/tooling, additive) · `tracker` (orchestration doc) ·
  `corpus-edit` (touches KB/manuscript/constants — careful) ·
  `corpus-edit[Rule-12]` (a walk-back; verify the 🔴 header + preserved body).
- **The only two direct textual conflicts** (whichever merges 2nd rebases):
  - `manuscript/ave-kb/.index/claims.jsonl` → **#130 ∩ #132**
  - `manuscript/ave-kb/common/full-derivation-chain.md` → **#133 ∩ #135**
- **The r_opt sibling chain `#132 → #133 → #137`** is a *semantic* ordering
  (no shared file path); merge in that order so #137 reads the post-#133
  canonical r_opt. `src/ave/core/constants.py` is touched ONLY by #133.
- **Suggested review order**: fast batch first (low-additive + code + tracker),
  then the careful corpus-edit cluster (baryon-sector + r_opt chain in order),
  then the two large 06-07 forward-instrumentation PRs (#126, #134).

## Quick-reference table (review order)

| grp | # | branch (short) | what-it-does | risk-tier | dep / conflict |
|-----|---|----------------|--------------|-----------|----------------|
| A | 127 | vacuum-piezoelectric-framing | vacuum-as-chiral-piezoelectric research doc + KB table addition | low-additive[doc] | none |
| A | 128 | qm-foundations-trio | superposition/collapse/entanglement trio doc + 2 KB pointer edits | low-additive[doc] | none |
| A | 131 | highE-aliasing-prereg | FROZEN high-E winding-aliasing prereg (testable→topological-selection) | low-additive[prereg] | none |
| B | 129 | photon-engine-run | real photon-propagation engine output (new 471-line script + figures) | code | none |
| B | 134 | electron-genesis-showcase | photon→electron self-trap figures; 2 new scripts (largest additive, +1028) | code | none |
| B | 136 | code-provenance-index | code-provenance index prototype (6-seed) + drift-gate verifier | code[tooling] | none |
| C | 120 | session-handoff | epic §9–§47 tracker catch-up (orphaned off main after #114) | tracker | none |
| D | 130 | physics-flag-resolutions | c_L=√(10/3)c + piezo z0-link flag-resolutions (13 files, deletions) | corpus-edit | **CONFLICT** claims.jsonl ↔ #132 |
| D | 132 | proton-leaf-walkbacks | 3 proton-leaf Rule-12 walk-backs (phase-space type, dim, magnitude) | corpus-edit[Rule-12] | **CONFLICT** claims.jsonl ↔ #130; **HEAD of r_opt chain** |
| D | 133 | ropt-dimensional-propagation | r_opt dim-provenance across 10 sites; edits constants.py + faddeev_skyrme.py | corpus-edit[Rule-12]+code | **CONFLICT** full-derivation-chain.md ↔ #135; **MID r_opt chain** |
| D | 137 | stl-scale-relabel | §43 relabel STL physical-scale claims + r_opt canonical-source drift fix | code+corpus-edit | **TAIL r_opt chain** (reads post-#133) |
| D | 135 | lepton-sector-corrections | lepton-sector KB corrections; flags √(3/7) label; edits backmatter .tex | corpus-edit[Rule-12] | **CONFLICT** full-derivation-chain.md ↔ #133 |
| E | 117 | cosmic-dilution-trajectory | cosmic-dilution scope → REFUTED (3 grounds); consistency-class | low-additive[doc] | none |
| E | 118 | swept-gamma-omega-A2 | swept Γ(A²,ω) parametric-oscillator characterization | low-med[driver] | **STACK-PARENT of #119** |
| E | 119 | darkwake-feedback-alpha | the non-circular α-test → CALIBRATION not emergence (clean negative) | med[driver] | **STACKED ON #118** |
| E | 121 | alpha-valley-fraction | real-space valley-fraction α test → near-miss (clean negative) | low-med[driver] | none |
| E | 122 | session-reframes-mapping | 6 §14 reframes → KB; **edits glossary + translation-circuit** | corpus-edit[canonical-leaf] | none (only PR on those leaves); carries Axiom-1 tension |
| E | 123 | alpha-twist-framing | α=cross-section-twist test → clean negative (Rule-11 closure) | low-med[driver] | none |
| E | 124 | vacuum-characterization-program | vacuum datasheet × dynamics-domains matrix; figures | low-med[research+fig] | none; carries un-completed-verify caveat in-body |
| E | 125 | phi-winding-stability | φ-winding-stability route → both conjuncts falsified (Rule-12) | low-med[driver] | LATENT epic-doc overlap w/ #126 |
| E | 126 | two-node-alpha-projection | forward electron-genesis instrumentation; **60 files, engine-namespace add** | **HIGH** | EPIC-DOC editor; **main checkout parked here** |

---

## GROUP A — low-risk additive (fast batch; mergeable any order)

New research docs / preregs. Additive-only; the corpus touch is minimal and
additive. Fast review: confirm the discipline-tag (consistency-class /
prereg-frozen) and that no value/matrix row silently changed.

**#127 — vacuum-piezoelectric-framing** (2 files, +219/−0)
- *What*: new research doc `research/2026-06-08_vacuum-as-chiral-piezoelectric.md`
  (Class-B consistency reframe: vacuum = chiral piezoelectric Cosserat solid;
  EM = its piezo response) + a 21-line additive block to KB
  `translation-circuit.md`.
- *Check*: the framing is tagged CONSISTENCY-class, not emergence (it is — §30/§32);
  the translation-circuit addition is additive only (no existing row rewritten);
  ave-discrimination-check PASS noted in-body.

**#128 — qm-foundations-trio** (3 files, +186/−0)
- *What*: new doc `research/2026-06-08_qm-foundations-trio.md` + 2 tiny KB pointer
  edits (`translation-qm.md`, `phase-locked-topological-thread.md`, +2 each).
- *Check*: the 3-leg confidence asymmetry is preserved (entanglement=CANONICAL ·
  collapse=DERIVED · superposition=aliasing=SYNTHESIS, NOT promoted canonical);
  the origin-mislabel fix (aliasing→superposition) is the Bell-surviving slot
  (§33); cite-drift already fixed (`62cec37f`).

**#131 — highE-aliasing-prereg** (1 file, +208/−0)
- *What*: FROZEN prereg `research/2026-06-08_highE-winding-aliasing-prereg.md`
  (§35/`wdot9oegf`). No driver/result.
- *Check*: it is FROZEN (prereg-only); the A46 axis-split is honest (phase-space
  ω=mc²/ℏ vs real-space q→π/ℓ_node — do NOT fuse); testable content RELOCATED to
  the topological-selection rule (stable (2,4) falsifies). Note the in-body
  adjudication conflict #10 (emergence-leaf vs consistency-prereg) → that is a
  Grant decision, not a merge blocker.

## GROUP B — code / tooling (additive; fast but eyeball the scripts)

New scripts/figures/tooling. Additive-only, no engine mutation. Fast review:
confirm `make verify` is unaffected and the run scripts are substrate-native
(K4-TLM / FDTD-Yee), not SM-default solvers.

**#129 — photon-engine-run** (4 files, +502/−0)
- *What*: real photon-propagation engine output (K4-TLM + FDTD Yee); new
  `src/scripts/vol_1_foundations/photon_engine_real_run.py` (471 lines) + gif/png/
  json figures.
- *Check*: new script only (no `src/ave/` engine edit); figures are artifacts;
  the v/c≈1.45 cardinal photon speed matches the √2 A1-port-mode (§37 √2-vs-√(10/3)).

**#134 — electron-genesis-showcase** (13 files, +1028/−0 — largest additive)
- *What*: photon→electron self-trap figures via `FDTD3DEngine`; 2 new scripts
  (capture +392, render +580) + figs + `.gitignore`.
- *Check*: additive-only (new scripts, no engine mutation); the figures are a
  SHOWCASE — confirm the captions do NOT over-claim emergent (2,3) formation
  (the §27/§28 finding: drivers reach a PLANTED wall, not emergent selection).
  Scale-claim tier on any baryon-scale figure is gated on the §43/§45 A-vs-B fork.

**#136 — code-provenance-index** (3 files, +387/−0)
- *What*: prototype `CODE_PROVENANCE.md` + `code_provenance.jsonl` (6-seed) +
  `verify_code_provenance.py` drift-gate.
- *Check*: the doc is honestly framed "6-seed PROTOTYPE, NOT all-code-tracked";
  the verifier exits 0 and mirrors `claims.jsonl` (8 clm-IDs resolve); 4
  robustness WARNs are queued in-body (not yet in `make verify`). It caught its
  own §41 seed-contradiction on first run (leptons LOOSELY-gated, not ungated) —
  recorded flag-don't-fix, good sign.

## GROUP C — tracker (orchestration doc)

**#120 — session-handoff** (1 file, +293/−0)
- *What*: appends epic §9–§47 to `2026-06-07_electron-synthesis-epic.md` — the
  catch-up that never reached main (#114's PR merged early, orphaning the later
  commits off main; process note in §15).
- *Check*: additive tracker-only; this is the detailed log the
  `2026-06-08_session-handoff.md` distills. Reviewing #120 = reviewing the
  session narrative. **Process note**: future tracker updates go on a fresh
  short-lived branch per push-batch (this consolidation branch follows that).

## GROUP D — corpus-edit walk-backs (CAREFUL; r_opt chain #132→#133→#137 IN ORDER)

<!-- group-d -->

## GROUP E — 06-07 α-route research + forward-instrumentation

<!-- group-e -->

## Cross-cutting flags

<!-- flags -->
