# Standing-Decisions Audit/Challenge Lane — Charter

**Founded:** 2026-06-16
**Type:** Orchestration lane (audit/challenge — NOT implementor)
**Status:** ACTIVE — first-pass (`wxzjr5w6p`) + independent second-pass verification (`wdu86r1f4`, 2026-06-16, findings at bottom) complete. Second pass CORRECTED the first (two phantom escalations withdrawn: `gamma_c` bug + ACT-02 test). Awaiting Grant's rulings — prioritized brief delivered inline.

---

## Mandate

Adversarially audit/challenge the open **Grant-decisions** that accumulate awaiting ratification, so Grant rules with the strongest *counter-case* in hand rather than rubber-stamping a prior lean. This is a meta-lane: it audits decisions surfaced by the *other* lanes (engine, reconciliation, discipline-infra, field-definition, …) plus the orchestrator's own recommendations. Two of the three seed decisions are the *orchestrator's own* framings — they get attacked as hard as the rest.

Rationale: un-adjudicated decisions rotting silently is a documented failure mode in this workspace (the legacy `A-`/`E-`/`Q-G`/`L5` scheme churn; INVARIANT-S11). A standing lane whose job is to keep the open-decision set short, sharp, and surfaced closes that loop.

## Methodology (binding)

- **Adversarial + grep-grounded.** Every challenge cites actual corpus configs/claims by `file:line`, never assertion. Build the strongest case AGAINST the current lean — find the load-bearing weak premise / asserted-not-derived step / glossed alternative. Default skeptical (`feedback_challenge_canonical_negative`).
- **flag-don't-fix.** Surface the challenge + the single sharpest question; **Grant rules.** No self-ratify, no self-merge. Present decisions as inline prose with bulleted options — NOT `AskUserQuestion` multi-choice (`feedback_inline_questions`).
- **Pure-AVE-corpus rule.** `main` is PROTECTED; any tracked-doc / corpus edits go via branch + reviewed PR.
- **Track here** + a memory entry `project_standing_decisions_audit_lane.md`.

## First read (for any session picking up this lane)

1. Auto-loaded memory — esp. `project_wall_branch_fork`, `project_k2g_crystalline_provenance`, `project_form_value_meta_finding`, `project_reconciliation_handoff_lane`, `feedback_flag_dont_fix`, `feedback_inline_questions`, `feedback_challenge_canonical_negative`.
2. `AVE-Core/CLAUDE.md` + `manuscript/ave-kb/CLAUDE.md` (INVARIANT-S2 Q1=B is load-bearing here).
3. Open PRs: `gh pr list` (esp. #260, #265, #270, #271, #248).

---

## Decisions in scope (challenge each → verdict + the one question Grant must answer)

### D1 — Canonize the projective-ℂP¹ Smith-chart ontology? *(orchestrator's framing — attack it)*
**Lean:** canonize "the Smith chart = the projective boundary phase-space (Γ disk = ℂP¹ of the `(V,I)` phasor; a space of orbit-SHAPES, not states or real-space), one chart PER SECTOR (longitudinal-A1 `Z_tank=√(L/C)` ⊥ transverse-T2 `√(μ/ε)`)." **0 corpus precedent.**
**Attack:** (a) is the ℂP¹/orbit-moduli claim rigorous, or overclaimed (the chart *also* encodes real-space via angle, frequency via sweep)? (b) does "one chart per sector" add anything beyond INVARIANT-S2 Q1=B (already canonical)? (c) the practical content (the genesis-24 double-count guard) already landed as a flag in `cvr-reflection-smith.md` §7 + `boundary-observables-m-q-j.md` (PR #270) — is canonizing the *ontology* worth corpus weight, or should it stay an explanatory note?
**Anchors:** `cvr-reflection-smith.md`, `ave-kb/CLAUDE.md` INVARIANT-S2, `vocabulary-register.md`.

### D2 — Ratify the wall-sector H3 fork (PR #260)?
**State** (`project_wall_branch_fork`): the magnetic-vs-capacitive Γ=−1 wall is a chirality-set SIGN/spin selector NOT a branch (degenerate on `Z`, `|Γ|`; co-saturation locked by `K=2G`); **"magnetic PRIMARY" is ASSERTED-not-derived**; mass=A1 settled independently so the fork is MUTE on the mass sector; it refines the two-"3"s gauge claim to PARTIAL.
**Attack:** (a) is "magnetic primary" DERIVABLE from the substrate or genuinely asserted? (b) is the degeneracy complete — is there ANY physical observable (`Z`, `|Γ|`, energy) that distinguishes magnetic-short from capacitive-open, or is it truly Möbius-gauge (one wall, two frames)? (c) does PR #260 over/under-claim?
**Anchors:** `master-equation.md:78-79/84-85`, `trampoline-framework.md:641` (Möbius `Z↔1/Z`), `cvr-reflection-smith.md` §7 FLAG-2, `K=2G` (`project_k2g_crystalline_provenance`), PR #260 diff.

### D3 — Is the EE-toolkit build order right (jw-axis stability adjudicator FIRST)? *(orchestrator's framing — attack it)*
**Lean:** build the jw-axis stability adjudicator NOW (classify `|ω|` growth as physical-marginal / radiative / numerical-artifact), then dual-sector Smith + two-grid S-param + driven-Q at "Stage-1.5"; rigorous Link/Wind later.
**Attack:** (a) the pump question is ALREADY decided by the pump-exclusion triad (`research/2026-06-13_cage-stiffening-wall_prereg_FROZEN.md` A3.2: `converter_on=False` + bounded-at-V_yield + inverse-amplitude-scaling), and the adjudicator must fit `Re(s)` from the ENGINE's `ω(t)` (the `cvr_model` analytic pole is stable-by-construction with the baked `Q=1/α` at `cvr_model.py:72`) — so does it ADD anything over the triad + a growth-rate fit? (b) the build order was scoped before Stage-1.5 Layer-c came back emergence-NEGATIVE — **and that negative is now itself overturned as a Cartesian-vs-tetrahedral curl stencil artifact (2026-06-16), so the loop-closure question is untested, not negative** — is the toolkit analyzing a build whose physics is in flux? (c) the Stage-1.5/1.6 panel's recommended next move was the moving-Γ=−1-wall on Sector B (the genesis-named OPEN route, CP8-safe) — should THAT be the first build instead?
**Anchors:** `engine-capability-map.md` §4, the cage-stiffening prereg, the Stage-1.5/1.6 result branches.

---

## Also: enumerate other open decisions quietly rotting

Sweep `gh pr list`, `_orchestration/` trackers, recent `research/` result-docs for un-adjudicated forks + FLAG / Grant-rules / awaiting-ratify markers. Verify status (don't assume) of: DEC-01 photon ontology (regime vs primitive continuum; ACT-02 convergence test); the C′ scalar-helicity chord/echo bin (un-banked); the Heaviside-Gibbs corpus self-contradiction; the C4-SHARPEN `[Q]≡[L]` vocab ratify; the amorphous-D3 retirement / τ>τ_yield-vs-lossless fork; the Stage-1.5 Fork-1 (confined precursor, CP8-hazard) / Fork-2 (genesis-leg); the curl-stencil retraction follow-through (does the bug touch the broader genesis arc). For each: where it lives, current lean, staleness, recommended disposition.

## Deliverable

A prioritized brief to Grant: per-decision verdict (does the lean survive challenge?) + the single sharpest question, ordered by (blocks-a-merge / cheap-to-settle / physics-load-bearing), plus the rotting-decision inventory. Track it in this doc.

---

## First-pass audit findings (`wxzjr5w6p`, 2026-06-16)

5 agents; adversarial. **Both orchestrator self-framings (D1, D3) were grep-weakened — the lane-separation worked exactly as intended (a cross-lane grep caught stale-belief inflation the orchestrator carried).** Two recurring defect classes span the set: (i) status-inflation of an already-adjudicated echo; (ii) non-propagation of an already-rendered verdict into the canonical leaf body.

**Rule order (cheapest/most-blocking first):**

- **D2 (rule FIRST) — MOOT as posed; two live defects.** PR #260 is **already MERGED + RATIFIED** (`git log`: merge `04bda99b`, Grant-ratify `5089ca09`, demote-magnetic-PRIMARY `dcbc994f`) — the memory's "awaiting Grant ratify" is **stale**. Real open items: **(a)** the surviving "formation-order residue / not-FULLY-gauge" is elevated to "real, frame-invariant" at the *same* asserted-not-derived tier as the "magnetic PRIMARY" it demotes (engine `cvr_model.py:243-246` flags the residue magnitude as a non-derived placeholder the cubic FDTD averages out) → should it be tagged B3-leaning-B4, residue-pending-the-chiral-engine? **(b) NON-PROPAGATION:** `master-equation.md:85` STILL reads "confinement proceeds via the magnetic branch instead … B saturates μ_eff first" unhedged — only the claim-quality *rationale* was scoped. Needs a 🔴 demotion header (substitution-not-retraction half-live).
- **D3 (rule SECOND) — WEAK-SHOULD-RECONSIDER (0.72).** The jω-adjudicator is ceremony around an already-built in-driver classifier (`OMEGA_BLOWUP_FACTOR=1e3`), and it measures a build that doesn't emerge. **Alternative: build the moving-Γ=−1-wall-on-Sector-B confiner FIRST** (`use_impedance_boundary`, a LIVE engine capability) — confine the propagating ω before measuring it. (Aligns with the Stage-1.5/1.6 panel + the engine lane's current Stage-1.6 arc.)
- **D1 (rule THIRD) — SHOULD-FLIP (0.83).** The "0 corpus precedent" premise is grep-false: the Möbius=PSL(2,ℂ)-on-ℂP¹ / "Smith chart is the spinor geometry of impedance" framing is verbatim in `research/2026-06-06_biquaternion-node-algebra-result.md` §5.1 and was **already adjudicated consistency-class / "echo, not chord"** (propagated to `op21:252`, `historical-precedents.md:39`). "One chart per sector" is already INVARIANT-S2 Q1=B. So: do NOT canonize — at most add an INVARIANT-F2 cross-link from `cvr-reflection-smith.md` to the biquaternion result at its existing echo ceiling; the practical guard already lands with PR #270.

**Rotting-decision inventory (other open items found):**

| Item | Disposition |
|---|---|
| DEC-01 photon ontology (regime vs primitive) | HOLD #248 until ACT-02 returns |
| **DEC-03 + `gamma_c` numeric bug** (vol_2 neutrino handedness sign-inversion; `gamma_c` 3.67e-6 vs 2.12e16) | **ESCALATE — auditor-arithmetic-confirmable hard error** |
| Vocab def-node 7-term cluster | LET-DIE the "menu" framing / PARTIAL-RATIFY; C4 `[Q]≡[L]` already canon (clm-dfaiwj 0.8 — closed) |
| Crystalline-vs-amorphous axiom seam | ESCALATE to Grant as a one-sentence plumber-physical question |
| Stage-1.5 eigenmode keystone | CHALLENGE-FURTHER before greenlighting the build |
| k_max canonical value | RATIFY PR #271 (auditor-arithmetic-clean) |
| Engine build-order DAG | CHALLENGE-FURTHER then RATIFY-WITH-SCRUTINY (verify each DOF firewall is canon-derived) |
| ACT-01 coverage-completion sweep | RATIFY THE GO — blocking; "ratified ≠ propagated" thrice-confirmed |
| AVE-Skills mirror | LET-IT-WAIT (low priority; implementer's push) |

---

## Session-kickoff prompt (paste into a fresh session to pick up this lane)

```
You are the Standing-Decisions Audit/Challenge lane — an AVE orchestration session
(not an implementor). Mandate: adversarially audit/challenge the open Grant-decisions
awaiting ratification, so Grant rules with the strongest counter-case in hand. Two of the
three seed decisions are the orchestrator's own framings — attack them as hard as the rest.
Read this charter (_orchestration/2026-06-16_standing-decisions-audit-lane.md) in full, then
your auto-loaded memory + the open PRs. Run an independent adversarial challenge of D1/D2/D3
above (grep-grounded, flag-don't-fix), enumerate other rotting decisions, and bring Grant a
prioritized brief: per-decision verdict + the single sharpest question, ordered by
blocks-a-merge / cheap-to-settle / physics-load-bearing. Grant rules; you do not self-ratify
or self-merge. Inline prose, not multi-choice.
```

---

## Second-pass independent verification (`wdu86r1f4`, 2026-06-16)

8 grep-grounded agents (4 verifiers on the decisive pivots + 2 rotting-sweeps + 3 adversarial challengers fed the verified facts; one tracker sweep re-run after a 529). Discipline: treat every first-pass finding as a CLAIM to verify, not a fact. **The three verdicts (D1 flip, D2 moot, D3 reconsider) SURVIVE — but the first pass over-escalated TWO non-existent items and got three supporting sub-claims wrong.** All claims below carry verbatim file:line; the first-pass section above is preserved unedited (Rule-12 audit trail).

### Meta-finding — first-pass had two PHANTOM escalations
- **`gamma_c` "hard numeric error" — REFUTED (does not exist).** `git grep '3.67e-6'/'3.67e6'` returns ZERO hits for `gamma_c`; the nearest `3.67e3` is the unrelated **NaI crystal density** (kg/m³, `vol_3.../05_cosmology_dark_sector.tex:232`). There is exactly ONE dimensional `gamma_c` = `2.12e16 m/s²` (`vol_2.../03_neutrino_sector.tex:57/81/85`) — the value the escalation itself called "canonical" — and it is a *stipulated normalization* (`:88`), so there is no arithmetic to be wrong. Not a bug, not even a label collision. **Withdraw the escalation.**
- **"ACT-02 convergence test" (DEC-01 gate) — REFUTED (does not exist).** `git grep 'ACT-02'` is EMPTY repo-wide AND empty in the (untracked) photon-ontology handoff. The charter's own D1/rotting framing (this doc, line 51 / 73) propagated the phantom. The real DEC-01 gate is a causality/signal-front discriminator, recorded **OPEN** at `vocabulary-register.md:388`.
- **DEC-03 (the other half of the escalation) is REAL but already a disclosed Rule-12 flag**, not an undisclosed contradiction: tex prose + KB canon agree LEFT-propagates (`chiral-screening.md:22`, `weak-coupling.md:20`, `03_neutrino_sector.tex:59-61`) but two figure scripts (`simulate_chiral_network.py` K_R=1.0/K_L=0.05; `plot_chiral_dispersion.py:20`) encode the OPPOSITE hand — flagged verbatim at `03_neutrino_sector.tex:66` ("the generating scripts currently encode the OPPOSITE hand; flagged DEC-03", on main via PR #257). Untested path (no `gamma_c` in `src/tests/`). Fix = align the two scripts to LEFT-propagates; no Grant ruling beyond confirming the convention.

### D1 — projective-ℂP¹ Smith-chart ontology — verdict SHOULD-FLIP **CONFIRMED (cross-link-only, do NOT canonize)**, conf 0.82
- CONFIRMED: the Möbius=PSL(2,ℂ)-on-ℂP¹ / "Smith chart is the spinor geometry of impedance" framing is verbatim at `research/2026-06-06_biquaternion-node-algebra-result.md:270-278`, genuinely adjudicated **consistency-class / "echo, not chord"** (§5.3 "T3 = Class A/C"; `historical-precedents.md:39` verbatim "echo, not chord"), propagated to `op21:252`. "One chart per sector" (√(L/C) ⊥ √(μ/ε), A1⊥T2) is ALREADY canon as INVARIANT-S2 Q1=B + `master-equation.md:20`. **So the orchestrator's "0 corpus precedent" premise is grep-FALSE.**
- TWO first-pass sub-claims CORRECTED: (1) **"guard already landed via PR #270" is FALSE** — #270 is OPEN (`mergedAt:null`); the genesis-24 guard exists only on-branch and only in `cvr-reflection-smith.md §7`, NOT in `boundary-observables-m-q-j.md` (whose #270 change is an unrelated k_max relabel). (2) **"orbit-shapes NOT states" is corpus-CONTRADICTED** — the canonical leaf parametrizes the locus by the operating-point STATE `Γ(A_0)` (`cvr-reflection-smith.md:24`). The AVE Γ-locus IS a state sweep; the textbook electrical-distance reading is simply never invoked (not "excluded").
- NEW (first-pass missed): the SL(2,ℂ) substance D1 would "add" is ALREADY canon a *second* place — `trampoline-framework.md §4.1`. The genuinely-new layer (Γ-disk as ℂP¹ "orbit-moduli") is exactly the part that overclaims. **NEW FLAG for Grant:** a proven-vs-consistency-class tension — `trampoline §4.1` asserts "the Smith chart is the SL(2,ℂ) spinor action … proven" while biquaternion §5.3 adjudicates the identical fact "consistency-class, passes no G-gate."

### D2 — wall-sector H3 fork (PR #260) — verdict **MOOT-as-posed CONFIRMED** (already Grant-merged), conf 0.83
- Ratification real: merge `04bda99b` is a genuine GitHub Grant-L PR-merge. NUANCE: the substantive sign-off prose ("Lane 3 RATIFIED" / "Grant ratified B3 + demotion") lives only in orchestrator-drafted, Claude-co-authored commit bodies `5089ca09`/`dcbc994f` — the *identity* is Grant's (the PR-merge), the *wording* is orchestrator-paraphrased (referential-integrity residual, not a doc-merge masquerade).
- Defect-a (residue elevation) — REAL but first-pass OVER-stated: `result:22` says "real, frame-invariant" but the *same sentence* fences it `[verify=PARTIAL, auditor-assessed high]` + Amendment A5 ("'high' = auditor confidence, NOT a solidity"); the χ magnitude is "a STRUCTURAL placeholder … not a derived magnitude" (`cvr_model.py:243-246`, FLAG-4). So it is asserted-at-PARTIAL-explicitly-below-solidity, **not** elevated to the demoted clm-lv3uw1 tier. WARN-grade label hygiene, not FAIL.
- Defect-b (non-propagation) — REAL and **WIDER than posed**: `master-equation.md:85` still reads "*confinement proceeds via the magnetic branch* … B saturates μ_eff first … generating invariant rest mass" with only a bare `clm-lv3uw1` marker and NO demotion header — while the SAME file carries a 🔴 Rule-12 demotion at line 20 (so the pattern is established here; its absence at :85 is a genuine half-live contradiction). The demotion reached only the claim-quality scope-note + 3 vol4 leaves; **≥6 more body sites still read "magnetic branch" unhedged:** `regime-equation-sets.md:42`, `photon-ee-mapping.md:45`, `double-slit-ee-mapping.md:30/51/52`, `cvr-reflection-smith.md:28`, `index.md:32`, `dual-reactance-storage-taxonomy.md:175`. This is the exact parallel-site/salience-gradient lapse the discipline-infra gate exists to catch.
- Disposition: **no new Grant decision** — implementer-cleanup (ONE propagation PR; run the parallel-site gate as its completeness check). One physics sub-question for Grant remains (residue tag).

### D3 — EE-toolkit build order — verdict **WEAK-SHOULD-RECONSIDER → RECONSIDER-FRAMING** (neither option first), conf 0.78
- CONFIRMED: `OMEGA_BLOWUP_FACTOR=1e3` in-driver classifier exists (`stage15_layer_b_coupled_stability.py:58`, branch-only); `cvr_model.py:72 Q_TANK=1/ALPHA` and `poles():197-209` is LHP-stable for any Q>0 (so a jω adjudicator on the *analytic* model is circular). `use_impedance_boundary` is a live engine capability on main. The moving-Γ=−1-wall-on-Sector-B WAS the verify-panel-recommended next move (Phase 11.1, prereg `b2de04fc`).
- CORRECTIONS: (1) **Layer-c was NOT "overturned"** — the Cartesian-vs-tetrahedral curl-stencil mismatch (`coupling_work=0` integrated where `gXi_cartesian=0` by construction, vs `gXi_tetrahedral=2.92` un-integrated; `overlap_cells` 0 vs 1024) is a 🔴 LOAD-BEARING OPEN artifact-vs-structural fork marked **"DO NOT bank — verify panel w9q6nv9gm dispatched"** (`_orchestration/2026-06-15_passive-eigenmode-solve.md:970-977`); the panel has NOT returned. "UNTESTED, not negative" is the defensible phrasing. (2) `engine-capability-map.md §4` is the WRONG anchor (it is a labelled "this engine does not exist" DESIGN PROPOSAL); the recommendation lives in the orchestration doc + §5. (3) circularity is from passivity/the LC form, not "Q baked to 1/α."
- **Both** the orchestrator's "adjudicator first" AND the first-pass's "moving-wall confiner first" are downstream of a loop-closure result the data shows was mis-measured. Disposition: **build-X-first where X = settle loop-closure via the matched-grid re-run (panel w9q6nv9gm) BEFORE any toolkit-vs-confiner ranking.** Cross-cutting caveat: ALL Stage-1.5/1.6 evidence is branch-only (not on main).

### Rotting-decision inventory (verified this pass)

| Item | Status (verified) | Disposition |
|---|---|---|
| **#271** K4 zone-edge Nyquist k_max | CLEAN, arithmetic auditor-verified to full precision, prereg FROZEN, clm-sjjvhf relabel correctly deferred | **RATIFY/merge FIRST** — load-bearing settle the others depend on |
| **#270** toolkit audit (4 edits) | body says "flag-don't-fix" but DIFF already writes "✅ k_max RELABELED (Grant-approved)" citing unmerged #271 HEAD `b72045d4` — flag-vs-fix split | **SPLIT**: land items 1/3/4 now; demote item-2 to a real flag OR hold until #271 merges + Grant rules the relabel |
| **#269** engine-map Stage-1 + ledger walk-back | sound walk-back, anchors check; but "EMPIRICALLY VERIFIED" banner cites unmerged `be459b7` | SHA-pin `be459b7`; merge order = be459b7-result → #269 |
| **#248** Weak-C photon continuum | asserts "Grant confirmed weak-C 2026-06-14" but grep EMPTY + `vocabulary-register.md:388` still reads DEC-01 **OPEN**; the ACT-02 gate it presumes doesn't exist | **PROVENANCE CONFLICT — do NOT merge while register reads OPEN.** Grant: ratify weak-C in a tracked record (+flip :388) OR re-scope #248. Real Grant decision. |
| **#268** eigenmode handoff v2 | faithful handoff, _orchestration-only; but the test it designs has since RUN (be459b7 NEGATIVE-pending-panel) | annotate/retire as overtaken, or keep as live design doc — no ruling needed |
| DEC-01 photon ontology | genuinely OPEN; home handoff doc is **UNTRACKED** (not greppable on main) | PR the handoff into _orchestration so OPEN is greppable; surface §7(a) ruling to Grant; ties to #248 |
| C′ scalar-grade-restoration | RAN → swept DEAD as in-firewall move **in memory only**; chord/echo ledger has NO entry | add a `genesis-chord-falsification-ledger.md` entry (likely WRONG-CARRIER tag, NOT a chord/echo bin); recovery-pointer to `analysis/2026-06-13-loop-gap-scalar-grade @ 85f83cd4` |
| Heaviside-Gibbs longitudinal scalar | **NO open contradiction** — sense-disambiguated by `def-9a4f07` (sense-a A1 V-scalar = physical/not-Gauss-deleted ⊥ sense-c transverse photon = Gauss-transverse) | PASS; optional sense-(c) scoping note at `maxwell-quaternion-longitudinal-context.md:22` |
| C4 `[Q]≡[L]` + #265 | `[Q]≡[L]` (clm-dfaiwj 0.8) ALREADY CANON; two PROPOSED items await Grant: `def-tk1xfm` (TKI-transformer) + the charge-winding SHARPEN on `def-3638f2` | **Grant ratify** the two proposed def-items (proposed→SOLID); leave clm-dfaiwj untouched |
| amorphous-D3 / τ_yield fork | **NOT settled by #267** (cosmetic 1-line relabel); discipline rule landed (#266) but plastic/thixotropic load-bearing language survives at `appendices-overview.md:52`, `dark-wake-bemf-foc-synthesis.md:159`, `clm-ghs75o` | Grant rule the reversible-reactive lean ("phase slipstream" leans reversible); THEN per-sense relabel (NOT find-replace — re-breaks Peierls-Nabarro) |
| Stage-1.5 Fork-1/Fork-2 | **BOTH off the table** — superseded by Stage-1.6 moving-wall (Phase 12 "replaces both forks"); live object = un-returned panel `w9q6nv9gm` | no Grant action until panel returns |
| curl-stencil follow-through | **contained** to Stage-1.5 Layer-c + Stage-1.6; does NOT invalidate genesis-23 (source-deadness, `GAP-1`) or held-BC (apparatus-floor, `:585`) — different diagnostics | PASS; scope retraction to the Sector-B coupling integral only |

**Other awaiting-Grant markers found (not in the seed list):** INVARIANT-S2 residual yield-weld sub-question (`topological-kinematics.md:89`); platform Option-A "PENDING Grant ratification" (`_orchestration/index.md:78`, may be superseded by the C′-DEAD ruling); the 2/7-homonym chord-vs-circular gate ("Grant's physics call", `magic-angle-provenance-...:76`).
