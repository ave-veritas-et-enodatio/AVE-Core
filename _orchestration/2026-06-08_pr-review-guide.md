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

These touch KB / manuscript / `constants.py`. Highest review scrutiny. Two
direct conflicts live here (claims.jsonl, full-derivation-chain.md) — whichever
of each pair merges 2nd must rebase. The r_opt sibling chain has a SEMANTIC
order (no shared file path, but #137 must read the post-#133 canonical value).

**Suggested merge order within Group D:** #130 then #132 (claims.jsonl pair —
either order, 2nd rebases), then #133 → #137 (r_opt canonical-source order),
then #135 (full-derivation-chain pair with #133 — #135 rebases if #133 landed).
Review the three baryon-sector PRs (#130/#132/#133) together for narrative
coherence — they edit distinct files under `vol2/particle-physics/ch02-baryon-
sector/` (no textual conflict, but one cluster).

**#130 — physics-flag-resolutions** (13 files, +36/−21)
- *What*: two Grant-accepted flag-resolutions — c_L=√(10/3)c P-wave canon + the
  piezo force-dilution coordination-z0 link. Edits KB `.index/claims.jsonl`, 2
  manuscript `.tex`, claim-quality.
- *Check*: this PR has **deletions across canon** (−21) — verify each deletion is
  the OLD flag-state being resolved, not load-bearing content dropped. The
  √(10/3) split was landed here (§37 confirms √2 A1-port vs √(10/3) continuum
  P-wave are both real, different modes). **CONFLICT**: `claims.jsonl` ↔ #132 —
  if #132 lands first, #130 rebases its claims.jsonl hunk (or vice-versa).

**#132 — proton-leaf-walkbacks** (4 files, +20/−20) — **HEAD of r_opt chain**
- *What*: 3 proton-leaf Rule-12 walk-backs — (a) phase-space TYPE for (2,5)
  [§36], (b) dimensional provenance, (c) magnitude precision. Edits
  `proton-identification.md`, `torus-knot-ladder-baryons.md`,
  `vol2/claim-quality.md`, `claims.jsonl`.
- *Check*: each is a **Rule-12** walk-back — verify the 🔴 header is present and
  the original body is PRESERVED (not deleted, not refilled with a new unverified
  hypothesis). The (2,5)-as-phase-space relabel matches the electron (2,5)/(2,3)
  parallel (`electron-identification.md:23`). **NOTE: #132 is OPEN, not merged —
  until it lands, origin/main still carries the proton-leaf real-space error.**
  **CONFLICT**: `claims.jsonl` ↔ #130.

**#133 — ropt-dimensional-propagation** (10 files, +59/−34) — **MID r_opt chain**
- *What*: r_opt dimensional-provenance propagation across 10 sites (sibling of
  #132; zero file overlap). Edits `src/ave/core/constants.py` +
  `src/ave/topological/faddeev_skyrme.py` + 8 KB. The 26-site self-audit found
  the error; 10 fixed here, 2 in #132, 14 surfaced for adjudication (§42).
- *Check*: **`constants.py` is touched ONLY by #133** in this whole open-PR set —
  this is the canonical-source edit #137 depends on. Verify it is comment/
  docstring-level (the survey reports 86 tests pass, **values unchanged**) — i.e.
  the dimensional note added, NOT a numeric change. **CONFLICT**:
  `full-derivation-chain.md` ↔ #135.

**#137 — stl-scale-relabel** (5 files, +158/−20) — **TAIL of r_opt chain**
- *What*: §43 — RELABEL STL physical-scale claims + scope accurate-scaling + fix
  r_opt canonical-source drift. Edits `spectral_gap.py`, `cosserat_field_3d.py`,
  `entanglement_thread.py`, `generate_particle_stl.py`, `ACCURATE_SCALING.md`.
- *Check*: merge AFTER #133 so it reads the post-#133 canonical r_opt. **This PR
  is gated on the §43/§45 A-vs-B Grant fork** — it relabels STL scale-claims to
  rendering-only (the Resolution-A read). If Grant picks Resolution B (supra-node,
  STLs at correct body-envelope scale), the relabel is wrong-direction. Confirm
  the relabel is reconciled to the fork, or hold pending the Grant call.

**#135 — lepton-sector-corrections** (5 files, +38/−11)
- *What*: lepton-sector KB corrections; flags the √(3/7) label for Grant
  (`wdnhioko1` audit). Edits `lepton-spectrum.md`,
  `backmatter/02_full_derivation_chain.tex`.
- *Check*: the μ-α¹/τ-α² ladder is RETIRED (both leptons α⁻¹ — §41); honest-tier
  labels are matched-closed-form-no-solver (NOT "derived"). **The √(3/7) is
  FLAGGED, not relabeled** — confirm the PR surfaces it for Grant (decision #4),
  does NOT silently relabel dilatational↔torsion. **CONFLICT**:
  `full-derivation-chain.md` ↔ #133.

## GROUP E — 06-07 α-route research + forward-instrumentation

The 06-07 arc: one off-spine cosmic scope (#117), the swept-Γ→dark-wake α stack
(#118→#119), three α-route clean negatives (#121/#123/#125), the reframe→KB
mapping (#122), the datasheet scope (#124), and the large forward-genesis suite
(#126). **Net α-derivation status across all nine: OPEN** — every PR is
consistency-class or a clean negative; none claims an α readout. The fast ones
are the clean negatives (#117/#121/#123/#125); the careful ones are #122
(canonical leaves) and #126 (HIGH risk).

**#117 — cosmic-dilution-trajectory** (1 file, +256) — *fast*
- *What*: scopes Grant's "cosmic A slides down S(A) via dilution" → REFUTED on 3
  grounds (u₀* homeostatically pinned; strain intensive not dilutable;
  crystallization holds ∂_t ρ_n=0). Consistency-class, ends with a Rule-16 fork.
- *Check*: single research doc, no src/canonical edit; verdict is REFUTED (the
  doc records a negative, not a rescue). Off the genesis spine.

**#118 — swept-gamma-omega-A2** (4 files; bulk is JSON) — **STACK-PARENT of #119**
- *What*: swept 2-D Γ(A²,ω) parametric-oscillator characterization; 4× pump =
  parametric tongue (not pathology); gain α-DECOUPLED but Q=1/α α-ENCODED.
- *Check*: new vol_1 driver (`swept_gamma_omega_A2.py`, +376) + an 8731-line JSON
  artifact (the bulk of the diff — skim, don't line-read). No engine mutation;
  `make verify` unaffected. **Merge #118 before #119** (or accept #118 riding in
  via the stack — git-confirmed #118 head `5aef4a9` is an ancestor of #119).

**#119 — darkwake-feedback-alpha** (8 files; carries #118's 4) — **STACKED ON #118**
- *What*: THE genuine non-circular α test — feeds the real α-free dark-wake
  far-field loss, re-measures Q. Result: Q_self≈10–15≈O(4π), off 137 by ×9–14 →
  CALIBRATION not emergence; clean negative. 137 lives in the α-encoded
  near-field reactance/mass (§13).
- *Check*: clean negative, every input α-free (the precondition-for-emergence is
  MET, the magnitude misses); carries #118's swept-Γ files via the stack —
  merging #119 alone pulls #118's commits. The near/far split flag
  (`dark-back-reaction-taxonomy.md`) is for Grant.

**#121 — alpha-valley-fraction** (4 files) — *fast*
- *What*: Grant's real-space K4 rotor-envelope valley/shadow-fraction mechanism
  for the α-localization → α-free NEAR-MISS (≠1/137 in either frame); 137 only
  via the separate Clifford-torus mode-count.
- *Check*: vol_1 driver, negative result, `make verify` passes, ALPHA
  import comparison-only (α genuinely absent from the construction); rules out
  Grant's envelope as the 137-source (§17).

**#122 — session-reframes-mapping** (4 files) — **CAREFUL: edits canonical leaves**
- *What*: maps six §14 chat-only reframes into canonical structures (EE / vocab /
  fluids). All CONSISTENCY-class. **Edits `docs/glossary.md` (+15, §1.7 new) and
  `manuscript/ave-kb/common/translation-tables/translation-circuit.md` (+47, §10
  new)** + 2 research docs.
- *Check*: the ONLY PR in the 06-07 set editing canonical leaves (glossary +
  translation-circuit) — heaviest scrutiny in Group E. **It carries an
  unresolved Axiom-1 tension for Grant**: reframe-5 "z=4 ACHIRAL diamond" vs
  Axiom-1 "I4₁32 CHIRAL space group" (both quoted verbatim; NO edit to Axiom 1
  made). Confirm the additions are flagged consistency-class and the Axiom-1
  tension is surfaced-not-silently-resolved (it is — §8/§16 adjudicated z=4 with
  chirality on the Cosserat sector).

**#123 — alpha-twist-framing** (3 files) — *fast*
- *What*: α = per-revolution cross-section TWIST (Călugăreanu Tw) of the (2,3)
  flux tube → clean NEGATIVE (twist = q/p = 1.5 turns exact, ~1292× larger than
  α-rad). Rule-11 honest closure, branch closed, no rescue refilled.
- *Check*: vol_1 driver + research; negative; Călugăreanu cross-check (Wr+Tw=−6)
  holds. NOTE the result JSON lands under `research/` not `_output/`.

**#124 — vacuum-characterization-program** (13 files) — *low-med; carries a caveat*
- *What*: the vacuum datasheet × dynamics-domains matrix (each cell value +
  ✓/◐/○ status); real constants cited (T_EM=0.212 N, V_yield=43.65 kV,
  ℓ_node=3.862e-13 m). Consistency-class, no new derivations.
- *Check*: research + figures only, no src/engine. **In-body caveat: the
  FBD-workflow per-cell verify DID NOT COMPLETE** (spend limit) — flagged for a
  later pass. Confirm that caveat is preserved (it is an honest un-completed-
  verify note, not a silent gap). Most-recently-updated PR in the set.

**#125 — phi-winding-stability** (2 files) — *fast; LATENT epic-doc overlap*
- *What*: closes the last open α-route (§20/§21) — φ-as-most-stable-winding. Both
  conjuncts FALSIFIED α-free (KAM most-stable = irrational φ-torus, but (2,3) is
  the LEAST-stable convergent; (2,3) does NOT force R/r=φ²). §18 FIT no longer
  contingent. Rule-12 do-not-refill.
- *Check*: vol_1 driver + research; clean negative; AQ-4 explicitly says
  do-not-promote. **LATENT**: the body queues AQ-1/AQ-2 auditor edits to the epic
  doc §20/§21 + `ch8-alpha-golden-torus.md` (NOT in this PR's diff). If those
  land they overlap #126's epic-doc edit → sequencing flag, not a current git
  conflict.

**#126 — two-node-alpha-projection** (60 files, +15339) — **HIGH RISK**
- *What*: forward electron-genesis instrumentation (Theorem 3.1′ / calibration-
  crux). New engine module `src/ave/core/master_fdtd_phasor_bridge.py` (+193), 12
  vol_1 drivers, 11 frozen preregs/adjudications, ~20 `_output/*.json` artifacts;
  edits the shared epic doc + adds a native-bench handoff doc. Made with Cursor
  (outside the Claude-Code prereg flow).
- *Check*: **the largest PR by far + the only one adding to the `src/ave/core/`
  engine namespace + the parked main-checkout branch.** The §27 audit found CODE
  clean (`alpha_used_as_input:false` every row; honest negatives) but doc/
  description over-claims — **walk-backs B2/W1/W2/W3/N1/N2 were APPLIED + verified
  and FF-pushed onto #126 @ `891d0f36`**; B1 was a non-issue (orchestrator-map
  artifact only). One flag-don't-fix for Grant: W1 doc-headline (capped-leads)
  diverges from the machine-emitted JSON `classification.verdict`
  (`WINDOW_UNCAPPED_OBSERVER`) — Grant's call to leave-as-data-of-record or
  re-emit. Confirm the §28 framing: derives the CONDITIONS for a (2,3) electron,
  does NOT show dynamic SELECTION (drivers SEED a finished unknot ansatz, reach a
  PLANTED wall). EPIC-DOC editor — latent overlap with #125's queued §20/§21 edit.

## Cross-cutting flags

- **Stack**: #118 → #119 (git-confirmed ancestry). Merge #118 before #119, or
  recognize #119 carries #118's commits.
- **Two direct textual conflicts only**: `claims.jsonl` (#130 ∩ #132) and
  `full-derivation-chain.md` (#133 ∩ #135) — 2nd-to-merge rebases.
- **r_opt semantic chain**: #132 → #133 → #137 (no shared path; merge in order so
  #137 reads the post-#133 canonical r_opt). `constants.py` touched only by #133.
- **Canonical-leaf editors** (heaviest scrutiny): #122 (glossary +
  translation-circuit) and the Group-D KB edits.
- **Engine-namespace adds**: #126 (`master_fdtd_phasor_bridge.py`).
- **Epic-doc writers**: #120 (tracker), #126 (+12); #125 has queued (not-yet-
  applied) edits to the same doc — sequence if they land.
- **Gated on a Grant decision before/at merge**: #137 (§43/§45 A-vs-B fork);
  #135 (√(3/7) flag); #122 (Axiom-1 chirality tension — surfaced, not blocking).
- **In-body incomplete-verify caveat**: #124 (FBD per-cell verify did not finish).
- **Cursor-authored (outside the prereg flow)**: #126.
- **Main checkout is parked on #126's branch** — any worktree/clean-state op must
  account for HEAD there.
