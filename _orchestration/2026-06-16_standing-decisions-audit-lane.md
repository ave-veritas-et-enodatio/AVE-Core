# Standing-Decisions Audit/Challenge Lane — Charter

**Founded:** 2026-06-16
**Type:** Orchestration lane (audit/challenge — NOT implementor)
**Status:** ACTIVE — first-pass adversarial audit complete (`wxzjr5w6p`, findings below); awaiting Grant's rulings on D1/D2/D3 + the escalated rotting-decision items.

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
