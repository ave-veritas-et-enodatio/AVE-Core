# AVE-Core Orchestration Index

**Audit trail (2026-05-23 Benn → 2026-05-25 merge):** This directory was ported from `analysis/integration` (D7 curation, KB claim-DAG integration) on 2026-05-23, and completed-work snapshots were moved to [`_archive/index-stale.md`](_archive/index-stale.md). Merged with integration live state on 2026-05-25 — treat this doc as the current live tracker; consult git log for recent updates.
**EDIT** - 2026-05-23 Benn - document deprecated. Do not do any sweeping work from this document without evaluating current repo state. KB claim DAG has received many improvements and the KB has had many fixups in the process. This directory was ported over from `analysis/integration` branch, which has now been superseded. Work that was clearly already done has been extracted and moved to _archive/. What remains may still be relevant, but again, *check first*.

> **Staleness notice (2026-05-28 EOD)**: Sections below (active epics, adjudication queue, priority ladder, open decisions) reflect 2026-05-20 EOD state. The reconciliation section directly below catalogs what has demonstrably changed between 2026-05-20 and 2026-05-28; items not addressed in the reconciliation should be re-verified against current corpus before relying on details below. Verify-before-cite v1.4 applies.

## 2026-05-20 → 2026-05-28 reconciliation

Eight-day delta between the live 2026-05-20 baseline in this doc and the current 2026-05-28 EOD state. Items here are verified against git log / file existence / PR merge state.

### PRs landed (10 between 2026-05-20 and 2026-05-28)

| PR | Title (short) | Landed | Notes |
|---|---|---|---|
| #43 | Path B-prime closure | 2026-05-26 | empirical Outcome C FALSIFIED; epic archived to `_archive/path-b-prime-k4-dispersion-pq.md` |
| #47 | Phase 3-A4 Op21 multi-mode mode-counting canonical leaf | 2026-05-27 | clm-0ktpcn 0.60 → 0.65 |
| #48 | Phase 3-A4 AMENDMENT (auditor findings) | 2026-05-27 | Class 2 → Class B; 0.65 → 0.63 PARTIAL |
| #49 | Fix kb_cmd tool path in agent-facing docs | 2026-05-28 | hygiene |
| #50 | Phase 3-A4 walk-back propagation cleanup P1-P4 | 2026-05-28 | LOAD-BEARING cascade arithmetic + 14 stale-prose + Rule 12 prereg header |
| #51 | translation-circuit META framework expansion | 2026-05-28 | clm-eemap1 (EE-as-substrate-native at minimal-DOF) |
| #52 | Phase 3-A3 WALK-BACK + Type B SM-leakage cleanup | 2026-05-28 | δ_strain Machian-G framing FALSIFIED; 12-file scrub |
| #53 | INVARIANT-S2 c_EM/c_shear disambiguation | 2026-05-28 | Q-CLM-3ZZ0F6-DEPTH-1 closed; 2 PR #51 observation cleanups |
| #54 | §9 + clm-hp7nlm Cosserat-Curie δ_strain canonical leaf | 2026-05-28 | closes Q-DELTA-MAP-1 at mechanism-class identification |
| #55 | Vol 9 foundation (skeleton + Ch 1) + 7-vol PDF build infra | 2026-05-28 | broke + fixed all volume builds via foreword + preamble + table-wrap edits |
| #56 | Vol 9 Ch 2-16 buildout (15 sessions in 5 waves) | 2026-05-28 | full Vol 9; 165-page PDF builds clean; 16 new audit tags |
| #57 | orch(post-vol9-handoff-updates) | 2026-05-28 | this doc + Vol 9 plan/handoff doc completion |

### Workstreams CLOSED since 2026-05-20

- **Path B-prime — K4 (p,q) band-splitting** — CLOSED via PR #43; empirical Outcome C FALSIFIED; substrate-physical (p,q) reframe via canonical corpus. Epic doc moved to `_orchestration/_archive/path-b-prime-k4-dispersion-pq.md`. Was open-decision #2 in queued epics; now removed.
- **Q-PBP-1** adjudication — RESOLVED GO via canonical corpus survey (commit `c29e3595`, 2026-05-26).
- **clm-0ktpcn Phase 3-A2 / A3 / A4** — multiple closures (Phase 3-A2 WALK-BACK closure structural reframe; Phase 3-A4 Op21 + AMENDMENT to Class B 0.63 + walk-back propagation). clm-0ktpcn lifted via Op21 multi-mode formalization to 0.65 confidence then walked back to 0.63 PARTIAL.
- **clm-zuf7g1 Phase 1 + Phase 2 + Phase 3a** — Phase 1 FM chain-promotion CLOSED via PR #37; Phase 2 master-equation derivation 5-session arc CLOSED; Phase 3a Z₀ derivation WALK-BACK CLOSURE (Class 2 not achieved on numerical-value sub-axis; Q-LCR-1/2 surfaced for Grant).
- **Q-DELTA-MAP-1** — CLOSED at mechanism-class identification via PR #54 (Cosserat-Curie thermal-asymmetry; clm-hp7nlm canonical). NEW open follow-up: **Q-DELTA-MAP-1-quant** (quantitative η_ε derivation; Class 2 lift path).
- **Q-AX4-NA-1 + Q-AX4-NA-2** — BOTH ADJUDICATED GO 2026-05-26 (κ_3 = 0 substrate-mechanical refinement; varactor canonical reframe). Q-AX4-NA-3 deferred to Phase 0c implementor. **Phase 0c CLOSED** with 2 Type E walk-backs (commits `f20335e6` + `380ce9fb`). **Phase 2-NA row CLOSED** (commit `9bbb13a2`). **Phase 2-A close-out** (commit `8415e0b1`).
- **Vol 9 "The Vacuum Datasheet" initiative** — kicked off + CLOSED in single session 2026-05-28 via PR #55 + PR #56. See `2026-05-28_vol-9-vacuum-datasheet-plan-and-handoff.md` Completion Summary.
- **Lossless-dynamics framing** (adjudication item #3 in queue below) — RESOLVED 2026-05-19 EOD+++ via `temporal-saturation-regime-classifier.md` companion KB leaf (option c selected). Already marked RESOLVED in adjudication queue below.

### NEW canonical content since 2026-05-20

- **`clm-eemap1`** — EE-as-substrate-native META framework at minimal-DOF (canonical at `manuscript/ave-kb/common/translation-tables/translation-circuit.md`); 23-row mapping + 20-case means-test corpus; PR #51.
- **`clm-hp7nlm`** — Cosserat-Curie δ_strain at T_CMB canonical leaf (canonical at `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`); δ_strain ≈ 2.225×10⁻⁶ → η_ε ≈ 4.45×10⁻⁶; Class B 0.55 PARTIAL band; PR #54.
- **`clm-rtdmsn`** (or near) — Op21 multi-mode mode-counting canonical leaf (`op21-multi-mode-mode-counting.md`); PR #47.
- **`temporal-saturation-regime-classifier.md`** — 14-discipline temporal-regime trichotomy companion leaf; landed earlier in May.
- **INVARIANT-S2 c_EM vs c_shear** disambiguation in `manuscript/ave-kb/CLAUDE.md` (PR #53) — load-bearing for α-invariance discipline; Pitfall #5 framework-leakage caught via ave-prereg v1.1 Step 3.5.
- **Vol 9 "The Vacuum Datasheet"** at `manuscript/vol_9_vacuum_datasheet/` (16 chapters + KB mirror at `manuscript/ave-kb/vol9/`) — PRs #55 + #56.

### Skills updated since 2026-05-20 (see Skill ecosystem state section below for canonical versions)

- **NEW**: `ave-ee-first-mapping` v1.0 (2026-05-28; PR #51 companion)
- `ave-walk-back` v1.1 → v1.2 (2026-05-27; Step 3h-exhaustive)
- `consistency-vs-emergence` v1.2 → v1.3 (2026-05-27; Trigger 8 + Step 8 classification-promotion)
- `ave-worktree-paths` NEW v1.0 (2026-05-27; first-call canary)
- `ave-prereg` amended 2026-05-26 (v1.1 Step 3.5 substrate-thermodynamic-mapping audit)
- `ave-canonical-leaf-pull` amended 2026-05-26 (Trigger 17 / framework-extension proposals)
- `ave-discipline-translate` amended 2026-05-26 (v1.1 Trigger 6 cross-disciplinary translation)
- Plus prior amendments: ave-multi-falsifier-triangulation-discipline (2026-05-23), ave-directory-enumeration-discipline (2026-05-23), ave-cavity-class-identification (2026-05-23), ave-fundamental-ground-up-implementation (2026-05-23), ave-module-library-discipline (2026-05-20)

### Open follow-ups created by 2026-05-28 work

- **Q-DELTA-MAP-1-quant** (NEW): quantitative substrate-statistical-mechanics derivation of η_ε ≈ 4.45×10⁻⁶ from substrate E-mode dispersion + thermal occupation + dielectric coupling. Class 2 closure path; would lift clm-hp7nlm + clm-009nkt above 0.60.
- **Q-OP21-BARDEEN-1** (earlier session, carried forward): explicit reduction Q = ℓ → 1/ln(Z₁/Z₀) via substrate-impedance integration at Cooper-pair Γ-boundary.
- **Q-LCR-1 + Q-LCR-2** (NEW from clm-zuf7g1 Phase 3a walk-back): substrate-mechanism questions for Grant adjudication.
- **Per-overrun `\texttt{path}` cleanup** + margin gate tightening (350pt → 15-30pt) — publication polish queued.
- **Means-test corpus extensions** to muon/tau, neutrino, QCD, cosmological inflation, substrate-microbiology (clm-eemap1 framework extension).

### Audit tag delta

- 2026-05-20 baseline: 35 tags
- 2026-05-28 current: 65 tags
- +30 across 8 days; +16 are Vol 9 chapter-buildout tags landed 2026-05-28; the other +14 cover Path B-prime, Phase 3-A2 through 3-A4, clm-zuf7g1 Phase 1/2/3a, ax4-saturation Phase 0c + 2-NA + 2-A, and related.

### What this reconciliation does NOT cover (deferred)

- Section E cascade row in active-epics table — last activity in epic doc was 2026-05-19 EOD; the cascade items (methodology-systematic adjudication, Neptune sub-class adjudication, β cosmic-ε Session 3) have NOT verifiably progressed. Still as-of-2026-05-19 below.
- A1-HOPF Phase 0b — per `exp-a1-hopf.md`: "Phase 0b ready for Grant fab submission". Memory entry `project_hopf_01_status.md` says "boards in hand 2026-05-02; partial knot stitching underway; AVE-HOPF docs lag actual lab state" — so Phase 0b has likely progressed in the lab but AVE-HOPF docs lag. Not updated here; trust the memory entry over the epic doc on lab state.
- C11-MACH-ZEHNDER Phase 0 facility partnership search — NOT verified.
- C15-CLEAVE-01 Phase 1a-rev1 — last activity 2026-05-20; no further progress visible in git log. Likely still gated on Phase 1b/1c Grant manual KiCad work per index header below.
- Adjudication queue items #1 (methodology-systematic), #2 (Neptune), #4 (C5 threshold-policy), #5 (4th-category) — no verifiable progress in 8 days.
- Sibling-repo hygiene items (open decisions #7-10) — UNVERIFIED.
- Pre-commit hook + worktree-spawn-leak discipline fixes — STILL OPEN (worktree-leak recurred during Vol 9 Wave 1 sessions).

---

**Last updated**: 2026-05-20 EOD++++++++++++++ (most sections); 2026-05-28 EOD (audit tag count + staleness notice + HEAD ref)
**Current focus**: Vol 9 "The Vacuum Datasheet" ✅ COMPLETE 2026-05-28 (PR #55 + #56 both merged). Earlier 2026-05-20 focus: C15-CLEAVE-01 Phase 1a-rev1 ✓ COMPLETE — atopile walk-back delivered clean module-level imports; all Q-C15-10/11/12 + Q1.2 + Q-HWMOD-04 CLOSED. Next: A1-HOPF Phase 0b (Grant fab submission, [EXEC]) + C11 Phase 0 outreach ([PREP]) — both still queued.
**Current HEAD on `main`**: `c6d2dcaf` — PR #56 merge (Vol 9 Ch 2-16). Last live integration head on `analysis/integration` (2026-05-20 EOD reference): `5977f4d`.
**Audit tag count (AVE-Core)**: 65 (`git tag -l "audit/*" \| wc -l`) — 16 NEW Vol 9 audit tags landed 2026-05-28: `audit/2026-05-28_vol9-ch{02-16}-*` (15 chapter implementor branches) + `audit/2026-05-28_vol9-chapter-buildout` (integration branch). Was 35 at 2026-05-20 EOD; +30 across 8 days.
**Audit tags pushed (sibling repos this session)**: `audit/2026-05-20_phase-1a-kicad-design` + `audit/2026-05-20_phase-1a-rev1-atopile-walkback` at `AVE-Bench-FemtoElectrometer`; `audit/2026-05-20_q-c15-12-stage-a-fix` at `AVE-Hardware-Modules`
**Active branches (local AVE-Core)**: 5 — `analysis/integration`, `benn/long-running`, `golden-torus-update`, `main`, `research/l3-electron-soliton`. Vol 9 chapter-buildout branches (16 total) deleted 2026-05-28 post-merge; preserved as audit tags.
**Cross-repo state**: `AVE-Bench-FemtoElectrometer` main @ `7f9c721` (Phase 1a-rev1 ✓ MERGED with clean atopile module imports); `AVE-Hardware-Modules` main @ `8b0626b` (Q-C15-12 Stage A fix ✓ MERGED); AVE-Skills main @ `4f504c0`.

**Grant adjudication queue (needs your yes before agents proceed)**:
1. **A1-HOPF Phase 0b** [EXEC] — upload `AVE-HOPF/hardware/Gerbers_hopf_02a/` ZIP to JLCPCB + order 3D-print mandrels per BOM (your only low-friction high-signal exec item now).
2. **C11 Phase 0** [PREP→EXEC trigger] — facility partnership outreach (literature survey + cold-emails to Hasselbach / LENS / NIST / TEM holography centers). Agent-prep complete; outreach needs your decision.
3. **C15 Phase 1b** [PREP] — KiCad GUI work (schematic ERC clean + PCB layout + guard-ring polygon + DRC) per DESIGN_LOG §5.1-5.2; sub-agent tooling limitation makes this Grant manual. No spend; just time commitment when ready.

**Session narrative** (collapsed from prior 609-word inline header): see `_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md` audit trail for Phase 1a-rev1 detail; `experimental/experimental-arc.md` for top-3 sub-epic state; per-epic docs for phase-by-phase. This file is the snapshot; per-epic docs hold the narrative.

This is the cross-cutting carry-forward for AVE-Core orchestration. Per-epic state lives in adjacent `<epic-slug>.md` files; this doc carries the priority ladder, open decisions, skill-ecosystem state, and active-epic table. **For canonical full handoff content, this file is authoritative**; per-epic docs hold phase plans.

> **Completed-work snapshots extracted 2026-05-23** (D7 curation): the 2026-05-19 session summary and the "recently closed epics" table were moved to [`_archive/index-stale.md`](_archive/index-stale.md). What remains below is the forward-looking carry-forward (active epics, adjudication queue, priority ladder, open decisions).

## Active epics

> **Status note (2026-05-28)**: each epic's row marked with verified-status if I checked the epic doc / git log against 2026-05-28 state. UNVERIFIED items reflect 2026-05-20 baseline.

| Epic | Doc | Status (2026-05-28 annotated) | Last phase landed | Next |
|---|---|---|---|---|
| Section E cascade | [`theoretical/section-e-cascade.md`](theoretical/section-e-cascade.md) | **STILL ACTIVE — no verifiable progress 2026-05-20 → 2026-05-28**. Methodology-systematic adjudication still PROVISIONAL. Epic doc internal state still 2026-05-19 EOD. | E1b-prime merged via `c587573` audit `audit/2026-05-19_c5-pantheon-tightening` | (a) Methodology-systematic adjudication (Ganalyzer vs Longo cos-γ); (b) Observable 5/6/7 execution; (c) Joint Pantheon+ + SDSS + Shamir-DESI constraint |
| Soliton-lattice coupling operator | [`theoretical/soliton-lattice-coupling-operator.md`](theoretical/soliton-lattice-coupling-operator.md) | **STILL ACTIVE — no verifiable progress 2026-05-20 → 2026-05-28**. Sessions 3-5 still queued; Neptune sub-class adjudication still pending. | Session 2 merged via `78b9770` audit `audit/2026-05-19_soliton-lattice-coupling-operator-session2` | Session 3 (planetary finalization + Neptune sub-class adjudication) OR Session 4 (galactic-scale extension to SDSS DR17 via Row 11-a) |
| Cosmic-ε / DE projection | [`theoretical/cosmic-epsilon-de-projection-scoping.md`](theoretical/cosmic-epsilon-de-projection-scoping.md) | **STILL ACTIVE — no verifiable progress 2026-05-20 → 2026-05-28**. Sessions 3-4 still conditional. | Session 2 merged via `8e09046` (+ conflict fixup `4e99d77`); audit `audit/2026-05-19_cosmic-epsilon-de-projection-session2` | Session 3 (downstream walk-back: `cosmological-constant-closure.md` framing reconciliation per A2) OR Session 4 conditional (4th-category "thermodynamic latent-heat flow" if load-bearing) |
| **Experimental Arc** (parent) | [`experimental/experimental-arc.md`](experimental/experimental-arc.md) | ACTIVE — Phase 2 audit complete 2026-05-20; 3 sub-epics spawned per cascade-emphasis ranking. Adjudication queue items EXP-1 / EXP-3 / EXP-4 promoted to sub-epics. EXP-2 (walk-back scope) RESOLVED to surgical (4-5 leaves). EXP-6 (B4-PROTEIN) + EXP-7 (C2-T-PAIR) DEFERRED outside cascade-emphasis top-3. | Phase 1 walk-back bundled with sub-epic-establishment commit | Phase 3 driver readiness audit (after sub-epic Phase 1 measurements land); Phase 4 cross-repo coordination on-demand; Phase 5 continuous canonical tie-back |
| ↳ EXP-A1-HOPF (cascade × executability) | [`experimental/a1-hopf/exp-a1-hopf.md`](experimental/a1-hopf/exp-a1-hopf.md) + [Phase A audit](experimental/a1-hopf/exp-a1-hopf-repo-audit.md) + [Sim audit](experimental/a1-hopf/exp-a1-hopf-sim-audit.md) | **PHASE 0a ✓ COMPLETE (per epic doc, 2026-05-20 state)** + Sim audit ✓ NO DRIFT. Epic doc says "Phase 0b ready for Grant fab submission". **HOWEVER**: per memory entry `project_hopf_01_status.md`, boards in hand 2026-05-02; partial knot stitching underway; AVE-HOPF docs lag actual lab state. Phase 0b has likely progressed in the lab beyond what epic doc reflects. **Trust memory entry over epic doc for current lab state**. | Phase A audit + Sim audit + Phase B walk-back all landed 2026-05-20 | Grant uploads `Gerbers_hopf_02a/` to JLCPCB per `hopf_02a_ORDERING.md`; orders mandrels per `hopf_02a_BOM.md`; **OR** verify current AVE-HOPF lab state and update epic doc accordingly |
| ↳ EXP-C15-CLEAVE-01 (cascade SIZE — largest) | [`experimental/c15-cleave-01/exp-c15-cleave-01.md`](experimental/c15-cleave-01/exp-c15-cleave-01.md) | **PHASE 1a-rev1 ✓ FULLY MERGED both repos** per top-of-doc note (Q-C15-12 ✓ CLOSED via Path 1 at commit `c7996256` 2026-05-20). **Still STILL ACTIVE at Phase 1b/1c (Grant manual KiCad GUI work) — no further verifiable progress in 8 days.** | Q-C15-12 Path 1 brief landed at `5977f4d` 2026-05-20 | Phase 1b/1c KiCad GUI work (schematic ERC clean + PCB layout + guard-ring polygon + DRC) per DESIGN_LOG §5.1-5.2; sub-agent tooling limitation makes this Grant manual |
| ↳ EXP-C11-MACH-ZEHNDER (cascade × severity F) | [`experimental/c11-mach-zehnder/exp-c11-mach-zehnder.md`](experimental/c11-mach-zehnder/exp-c11-mach-zehnder.md) + [Sim audit](experimental/c11-mach-zehnder/exp-c11-mach-zehnder-sim-audit.md) + [project-c11-mach-zehnder.md canonical KB leaf](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-c11-mach-zehnder.md) | **STILL ACTIVE at Phase 0 facility partnership search — no verifiable progress in 8 days.** Sim audit ✓ NO DRIFT (2026-05-20 EOD+). | Sim audit + project KB leaf landed 2026-05-20 EOD+++ | Phase 0 facility partnership search: literature survey of electron-interferometer SOTA (Hasselbach Tübingen / LENS Italy / NIST / TEM holography centers) → candidate verification → cold-email outreach |

## Queued epics (not yet kicked off) — annotated with 2026-05-28 status

| Epic | Doc | Trigger | Status (2026-05-28) | Notes |
|---|---|---|---|---|
| DM META closure | (no doc yet) | Grant greenlight | STILL QUEUED | Independent of Section E. Closes C13c META row. ~1-2 sessions. |
| Phase 2 mass-spectrum activation | (no doc yet) | Grant greenlight | STILL QUEUED | W/Z/Higgs eigenvalue solver; ~1 week scope. Pre-greenlit 2026-04-30. |
| Lossless-dynamics framing extension | (no doc yet) | Grant adjudication on Option (a) vs (b) | ✅ RESOLVED via Option (c) | Resolved via `temporal-saturation-regime-classifier.md` companion KB leaf 2026-05-19 EOD+++. |
| Soliton-coupling Session 3 | [`theoretical/soliton-lattice-coupling-operator.md`](theoretical/soliton-lattice-coupling-operator.md) | Grant Neptune adjudication | STILL QUEUED | Planetary finalization. Estimated 1-2 hr. |
| Soliton-coupling Session 4 | same | Session 3 verdict | STILL QUEUED | Galactic-scale extension. Estimated 1-2 hr. |
| β cosmic-ε Session 3 | [`theoretical/cosmic-epsilon-de-projection-scoping.md`](theoretical/cosmic-epsilon-de-projection-scoping.md) | Anomaly A2 trigger | STILL QUEUED | Downstream walk-back. Estimated 1-2 hr. |
| **clm-zuf7g1 strengthen** | [`clm-zuf7g1-strengthen.md`](clm-zuf7g1-strengthen.md) | Grant greenlight | **PARTIALLY EXECUTED 2026-05-26** — Phase 1 + Phase 2 (5-session master-eq arc) CLOSED; Phase 3a Z₀ derivation CLOSED WALK-BACK (no solidity lift; Q-LCR-1/2 surfaced); Phase 3b deferred. clm-zuf7g1 confidence 0.60 → 0.65 (Phase 2); solidity remains 0.55. | Subsequent phases gated on Grant Q-LCR-1/2 adjudication. |
| ~~Path B-prime~~ | ~~[`path-b-prime-k4-dispersion-pq.md`](_archive/path-b-prime-k4-dispersion-pq.md)~~ | Q-PBP-1 adjudication | **✅ CLOSED 2026-05-26 via PR #43** — empirical Outcome C FALSIFIED; substrate-physical (p,q) reframing. Epic doc archived. | No further action. |
| **KB Q2 stale narrative-tail cleanup** | (no doc; tracked here) | Anytime — batchable | UNVERIFIED at 2026-05-28 | The mentioned solidity values may have changed in Phase 3-A4 + walk-back propagation work; verify against current state before action. |
| **ax4-saturation narrow-aperture amplitude-shape** (NEW 2026-05-26) | [`ax4-saturation-narrow-aperture-amplitude-shape.md`](ax4-saturation-narrow-aperture-amplitude-shape.md) | Phase 0c implementor | **PARTIALLY EXECUTED 2026-05-26 to 2026-05-27** — Q-AX4-NA-1 + Q-AX4-NA-2 ADJUDICATED GO; Phase 0c CLOSED with 2 Type E walk-backs; Phase 2-NA + Phase 2-A close-outs landed. | Phase 0c implementor verifies Q-AX4-NA-3 (substrate correlation length) when ready. |
| **clm-0ktpcn Golden Torus α strengthen** (NEW 2026-05-25) | [`clm-0ktpcn-golden-torus-alpha-strengthen.md`](clm-0ktpcn-golden-torus-alpha-strengthen.md) | — | **PARTIALLY EXECUTED 2026-05-25 to 2026-05-28** — Phase 1 (FM chain-promotion 8 claims 0.45 → 0.50) + Phase 2 (4/4 strengthen-by items on clm-unk0bd closed) + Phase 3-A2 (WALK-BACK closure structural reframe) + Phase 3-A3 (WALK-BACK δ_strain Machian-G framing FALSIFIED via PR #52) + Phase 3-A4 (Op21 multi-mode → AMENDMENT Class B → walk-back propagation P1-P4 via PRs #47/#48/#50). clm-0ktpcn at 0.55 solidity / 0.63 confidence PARTIAL. | Future: Q-DELTA-MAP-1-quant (Class 2 closure path for clm-hp7nlm → clm-0ktpcn cascade). |

## Adjudication queue for next orchestrator (5 substantive items + 4 hygiene)

Grant has 5 substantive items + 4 hygiene items pending. Prioritized roughly by urgency / impact. **Status column (2026-05-28 EOD) added; verified against current state.**

### Substantive (physics / framework)

| # | Item | Origin | Status (2026-05-28) | Recommendation |
|---|---|---|---|---|
| 1 | **Methodology-systematic adjudication**: Ganalyzer (Shamir 2022) vs Longo cos-γ (AVE SDSS DR17) — same SDSS-class input galaxies, 74° axis separation = 2.99σ_combined. AVE-Longo gets 5.33σ EXCLUSION of CMB-LSS alignment; Shamir's DESI Legacy gets 3.77° AGREEMENT. | Shamir 2022 epic | **STILL OPEN PROVISIONAL** — no verifiable progress in 8 days. McAdam & Shamir 2023 cross-comparison discriminating test not run. | Run McAdam & Shamir 2023 cross-comparison. 4 interpretive alternatives enumerated in leaf §Methodology-systematic. |
| 2 | **Neptune spin-axis class-mismatch** (Soliton Session 2 sub-anomaly) | Soliton Session 2 | **STILL OPEN** — gated on Grant Path A vs B adjudication. No verifiable progress in 8 days. | Path A (lossless-vs-lossy sub-class refinement) recommended. |
| 3 | **Lossless-dynamics framing** | Grant observation | **✅ RESOLVED 2026-05-19 EOD+++** via [temporal-saturation-regime-classifier.md](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md). Option (c) selected. | Closed; no further action. |
| 4 | **C5 threshold-policy adjudication** | Earlier session | **STILL OPEN PROVISIONAL** — no verifiable progress. | Surface for Grant call. |
| 5 | **4th-category "thermodynamic latent-heat flow"** framing | β Session 1 Q3 | **STILL OPEN — HOLD** | Pending downstream signals; not load-bearing unless Session 3 walk-back reveals tension. |

### NEW substantive items surfaced 2026-05-28

| # | Item | Origin | Status | Recommendation |
|---|---|---|---|---|
| 1a | **Q-DELTA-MAP-1-quant** — quantitative substrate-statistical-mechanics derivation of η_ε ≈ 4.45×10⁻⁶ from substrate E-mode dispersion + thermal occupation + dielectric coupling | PR #54 (clm-hp7nlm) | NEW OPEN | Class 2 closure path; would lift clm-hp7nlm + clm-009nkt above 0.60. Substantial workstream (substrate-statistical-mechanics setup). |
| 2a | **Q-LCR-1 + Q-LCR-2** — substrate-mechanism questions from clm-zuf7g1 Phase 3a walk-back | clm-zuf7g1 Phase 3a | NEW OPEN | Surfaced for Grant adjudication; pre-condition for Phase 3b. |
| 3a | **Q-OP21-BARDEEN-1** — explicit reduction Q = ℓ → 1/ln(Z₁/Z₀) via substrate-impedance integration at Cooper-pair Γ-boundary | earlier session, carried forward | STILL OPEN | Future workstream. |

### Process / discipline

| # | Item | Recurrence | Status (2026-05-28) | Recommendation |
|---|---|---|---|---|
| 6 | **Worktree-spawn branch-state leak** | Originally 3rd recurrence at 2026-05-19; **observed +3 more times during Vol 9 Wave 1 implementor sessions 2026-05-28** (Ch 2, Ch 7, Ch 9 implementors leaked to main repo path; recovered) | **STILL OPEN — RECURRENT** | Pattern not yet structurally fixed. `ave-worktree-paths` v1.0 added 2026-05-27 (first-call canary) but did not prevent the leak — implementors still wrote to main-repo path before canary check in some cases. **Stronger fix needed**: either pre-Write tool guard, or structural change to spawn-default behavior. |
| 7 | **Merge-conflict-marker commit-slip** | 1 instance 2026-05-19 | **STILL OPEN** — no verifiable progress on recommended pre-commit hook | Recommend installation of `<<<<<<<` pre-commit hook. |
| 8 | **Closed-epic archive move** | Done | **✅ RESOLVED 2026-05-19** + **Path B-prime added to archive 2026-05-26** | Closed; archive currently holds 8 docs at `_orchestration/_archive/`. |
| 9 | **Sibling-repo hygiene** | Long-standing | **STILL OPEN — UNVERIFIED** for 2026-05-28 state | Items 6-9 from open-decisions table below; verify state before batching. |

## Next-move priority ladder

### Immediate (can spawn in parallel via `isolation: "worktree"`)

1. **Soliton-coupling Session 3** — planetary finalization + Neptune sub-class adjudication. Triggered by adjudication item 2 (Neptune class-mismatch path A); Neptune-on-lossy-branch substantive structural explanation now available via [temporal-saturation-regime-classifier.md](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md) (item 3 RESOLVED). ~1-2 hr. Depends on Grant Path A vs B call.
2. **McAdam & Shamir 2023 cross-comparison** — discriminating test for Item 1 PROVISIONAL adjudication. Tests whether Shamir Ganalyzer applied to AVE's GZ1 catalog reproduces Shamir DESI axis (methodology-systematic) OR AVE Longo axis (catalog-systematic). Catalog redistribution required first. ~1 session if catalog accessible.
3. **DM META closure** — independent of all above. ~1-2 sessions. Depends on Grant greenlight.

### Medium-term (multi-session)

4. **β cosmic-ε Session 3** — downstream walk-back of `cosmological-constant-closure.md` per Anomaly A2. Triggered by β Session 2 framing reconciliation.
5. **Soliton-coupling Session 4** — galactic-scale extension to SDSS DR17 via Row 11-a (Ax 2 TKI scaling from Row 9-a planetary form). Depends on Session 3 outcome.
6. **Phase 2 mass-spectrum activation** (W/Z/Higgs eigenvalue solver) per doc 98 §3.2. Grant pre-greenlit 2026-04-30. Not gated. ~1 week scope.
7. **Observable 5/6/7 execution** (E/B polarization, orbital alignments, G P_2 anisotropy) — each multi-session, deferred until C5 settles or methodology-systematic adjudication (item 1) resolves.
8. **Joint Pantheon+ + SDSS + Shamir-DESI Option B constraint** — if methodology-systematic adjudication (item 1) supports it.

### Hygiene tier

9. Items 6-9 from "Open decisions" below. Each ≤30 min; batchable into single hygiene-pass session.
10. Process-discipline fixes (items 6-7 from adjudication queue): pre-commit hook + skill amendments.

## Open decisions (carry-forward + new) — annotated with 2026-05-28 status

| # | Item | Status (2026-05-28) | Detail |
|---|---|---|---|
| 1 | **Methodology-systematic adjudication** | STILL OPEN PROVISIONAL | Ganalyzer vs Longo cos-γ; 2.99σ separation on same SDSS data. Load-bearing for C5 cascade interpretation. |
| 2 | **Neptune spin-axis class-mismatch** | STILL OPEN | Path A (sub-class refinement, lossless-vs-lossy axis) vs Path B (granularity limitation). Recommend A. |
| 3 | **Lossless-dynamics framing** | ✅ RESOLVED 2026-05-19 EOD+++ | Closed via `temporal-saturation-regime-classifier.md`. |
| 4 | **C5 threshold-policy adjudication** | STILL OPEN PROVISIONAL | 20° + 3σ_combined vs σ_combined-only vs cascade-loose. |
| 5 | **4th-category "thermodynamic latent-heat flow"** | STILL OPEN — HOLD | Pending downstream signals. |
| 6 | **C3-MUON-DELTA Run-4/5 update** | STILL OPEN — TIMING | Fermilab Run-4/5 expected 2026-2027 at ±10 ppm. |
| 7 | **AVE-Protein 51 uncommitted files** | UNVERIFIED at 2026-05-28 | State 8 days old; verify before action. Grant decides commit / stash / restore. |
| 8 | **AVE-Metamaterials SOLAR_PANEL_INITIATIVE WIP** (8 uncommitted) | UNVERIFIED at 2026-05-28 | State 8 days old; verify. |
| 9 | **AVE-QED PDF gitignore + .tex commit** (2 uncommitted) | UNVERIFIED at 2026-05-28 | State 8 days old; verify. |
| 10 | **`analysis/c8-baryon-ladder-pdg-anchor` branch fate** | UNVERIFIED at 2026-05-28 | Branch still alive on local + origin per 2026-05-20 baseline. Audit-tag-and-delete option remains. |
| 11 | **Pre-commit hook for conflict markers** | STILL OPEN | No verifiable progress in 8 days. Recommend installation. |
| 12 | **Worktree-spawn branch-state-leak discipline** | STILL OPEN — RECURRENT | `ave-worktree-paths` v1.0 added 2026-05-27 but did not fully prevent the leak (recurred 3× during Vol 9 Wave 1 sessions 2026-05-28). Stronger fix needed. |
| 13 | **Soliton-coupling Session 3 kickoff** | STILL OPEN — gated on #2 | No progress. |
| 14 | **β cosmic-ε Session 3 kickoff** | STILL OPEN — gated on Anomaly A2 | No progress. |

### NEW open decisions surfaced 2026-05-28

| # | Item | Status | Detail |
|---|---|---|---|
| 15 | **Q-DELTA-MAP-1-quant Class 2 closure path** | NEW OPEN | Quantitative η_ε derivation; would lift clm-hp7nlm + clm-009nkt above 0.60. Substantial workstream. |
| 16 | **Q-LCR-1 + Q-LCR-2** (from clm-zuf7g1 Phase 3a walk-back) | NEW OPEN | Substrate-mechanism questions for Grant adjudication; pre-condition for Phase 3b. |
| 17 | **Q-OP21-BARDEEN-1** (carry-forward from earlier) | STILL OPEN | Explicit reduction Q = ℓ → 1/ln(Z₁/Z₀). |
| 18 | **Means-test corpus extensions** (from clm-eemap1 META framework) | NEW OPEN | Extend 20-case means-test corpus to muon/tau, neutrino, QCD, cosmological inflation, substrate-microbiology. Per-domain workstreams. |
| 19 | **Per-overrun `\texttt{path}` cleanup** | NEW OPEN | Foreword + Vol 9 chapter narratives; convert to `\path{}` / `\seqsplit{}`; then tighten margin gate back from 350pt → 15-30pt for publication polish. |
| 20 | **Vol 9 followup PRs** | QUEUED | Means-test corpus extensions, per-overrun cleanup, Q-DELTA-MAP-1-quant — all queued post-Vol-9-merge. |

## Skill ecosystem state (current versions — refreshed 2026-05-28 EOD)

Below table refreshed to 2026-05-28 EOD by filesystem mtime on `~/.claude/skills/`. The previous skill table (2026-05-19 EOD baseline) is superseded; this table is canonical.

| Skill | Version | Location | Last amended | Purpose |
|---|---|---|---|---|
| `ave-ee-first-mapping` | **v1.0 (NEW 2026-05-28)** | `~/.claude/skills/ave-ee-first-mapping/SKILL.md` | 2026-05-28 (PR #51 companion) | EE-as-substrate-native at minimal-DOF primary methodology. Forces EE vocabulary primary, classical-other-discipline secondary. Closes "reach for QFT / GR / chemistry analogue first when EE is closer-to-canonical" failure mode. 6th skill in "before deriving" cluster. |
| `ave-walk-back` | **v1.2** (was v1.1 pre-2026-05-27) | `~/.claude/skills/ave-walk-back/SKILL.md` | 2026-05-27 | Step 3h-exhaustive added. Closes "incomplete walk-back propagation" surfaced 2026-05-27 Phase 3-A4 amendment. |
| `consistency-vs-emergence` | **v1.3** (was v1.1 at 2026-05-19) | `~/.claude/skills/consistency-vs-emergence/SKILL.md` | 2026-05-27 | Trigger 8 + Step 8 classification-promotion checks. Closes Class 2 ↔ Class B promotion-discipline failure mode (Phase 3-A4 AMENDMENT PR #48). |
| `ave-worktree-paths` | **v1.0 (NEW 2026-05-27)** | `~/.claude/skills/ave-worktree-paths/SKILL.md` | 2026-05-27 | First-call canary discipline. Forces `git rev-parse --show-toplevel` BEFORE first Write tool call; subsequent paths must start with canary output. Closes worktree-vs-main-repo path-leak failure mode (observed 3rd time during Vol 9 Wave 1 implementor sessions 2026-05-28; pattern not yet structurally fixed — see open decisions #11/#12 below). |
| `ave-prereg` | **v1.1** | `~/.claude/skills/ave-prereg/SKILL.md` | 2026-05-26 | Step 3.5 substrate-thermodynamic-mapping audit added. Caught Phase 3-A3 framework-leakage error (c_shear-vs-c_EM substitution in α formula) per CLAUDE.md INVARIANT-S2; returned WALK-BACK rather than committing broken derivation. |
| `ave-canonical-leaf-pull` | **v1.3** (was v1.2 at 2026-05-19) | `~/.claude/skills/ave-canonical-leaf-pull/SKILL.md` | 2026-05-26 | Trigger 17 added (framework-extension classifier — when to invoke per-class survey). |
| `ave-discipline-translate` | **v1.1** (was v1.0 at 2026-05-19) | `~/.claude/skills/ave-discipline-translate/SKILL.md` | 2026-05-26 | Trigger 6 added (prose-vocabulary-substitution check). Forces substrate-native vocabulary when prose drifts to standard-physics analogue. |
| `ave-multi-falsifier-triangulation-discipline` | v1.0 | `~/.claude/skills/ave-multi-falsifier-triangulation-discipline/SKILL.md` | 2026-05-23 | 2-of-3 triangulation rule for orthogonal-physics multi-anchor validation. |
| `ave-directory-enumeration-discipline` | v1.0 | `~/.claude/skills/ave-directory-enumeration-discipline/SKILL.md` | 2026-05-23 | Forces `ls` survey of relevant directory before claiming "X doesn't exist". |
| `ave-cavity-class-identification` | v1.0 | `~/.claude/skills/ave-cavity-class-identification/SKILL.md` | 2026-05-23 | Substrate-cavity classification: open / closed / matched / mismatched. |
| `ave-fundamental-ground-up-implementation` | v1.0 | `~/.claude/skills/ave-fundamental-ground-up-implementation/SKILL.md` | 2026-05-23 | Implementation discipline: derive substrate observables before fitting. |
| `ave-module-library-discipline` | v1.0 | `~/.claude/skills/ave-module-library-discipline/SKILL.md` | 2026-05-20 | Module-level imports for atopile + hardware modules. Surfaced 2026-05-20 Q-C15-12 atopile walk-back. |
| `verify-before-cite` | **v1.4** | `~/.claude/skills/verify-before-cite/SKILL.md` | 2026-05-19 EOD+ | Trigger 9 added (merge-conflict-shape claims — empirical `git merge --no-commit` before adjudication). |
| `ave-handoff-canonical-locale` | v1.0 | `~/.claude/skills/ave-handoff-canonical-locale/SKILL.md` | 2026-05-19 EOD | This directory's write-time discipline. |
| AVE-Core directives | n/a (corpus) | [`CLAUDE.md`](../CLAUDE.md) + [`_orchestration/README.md`](README.md) | 2026-05-19 EOD | Pre-commit branch-check + worktree-isolation default. |

**Skill ecosystem delta (2026-05-20 → 2026-05-28)**: +2 NEW skills (`ave-ee-first-mapping` + `ave-worktree-paths`) + 5 amendments (`ave-walk-back` v1.2, `consistency-vs-emergence` v1.3, `ave-prereg` v1.1, `ave-canonical-leaf-pull` v1.3, `ave-discipline-translate` v1.1) + 5 other skills with last-touched dates from 2026-05-23. The 25 active-skills total from 2026-05-19 baseline may have grown; canonical count is `ls ~/.claude/skills/ | wc -l` (not refreshed here — verify before citing).

## Data caching state

- **Pantheon+SH0ES canonical cache** at `data/pantheon_plus/` — `.dat` (579 KB, regular git) + `.cov` (33 MB, git-LFS) + `README.md` with re-download instructions and MD5 checksums. Required by `c5_pantheon_bulk_flow_tightening.py`. LFS filter at `.gitattributes` + gitignore allowlist override of `data/*` pattern.
- **SDSS DR17 Galaxy Zoo 1 cache** at `data/sdss_dr17/` — `.csv.gz` (19.4 MB, regular git via gitignore allowlist; not LFS) + `README.md`. Required by `c5_sdss_spin_orientation.py`. Galaxy Zoo 1 Table 2 (Lintott+2011, ~668k SDSS DR7 galaxies, crowdsourced visual classification).
- **Shamir 2022 cache** at `data/shamir_2022/` — README only (no catalog data; per-galaxy classifications not publicly redistributed per Phase 0 verification; E2 sub-finding). Driver uses paper-quoted Table 3 axis (RA, Dec) → galactic 68%-containment radius via 200×200 uniform sampling.

## Catalog state (A-034 universal-saturation-kernel-catalog) — 2026-05-19 EOD baseline

**Baseline at 2026-05-19**: 26 instances at `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md` (was 21 at session start). 5 new rows added (9-a, 9-b, 11-a, 14-a, 14b).

**2026-05-28 status**: per Vol 9 Ch 7 implementor surfacing (`vol-9-ch07(saturation-characteristics)`), the catalog currently reports **26 canonical cross-scale instances (17 physical + 2 biological + 5 engineered + 2 scoped)** per the catalog body, with the canonical kernel governing **19 cross-scale topological-reorganization events** (physical-substrate subset) per `eq_axiom_4.tex` / Vol 0 backmatter, **21 orders of magnitude span uniformly**. Both counts presented honestly with scope distinction. UNVERIFIED whether any rows added 2026-05-20 → 2026-05-28 beyond the 26 baseline; reconfirm via current file head if relying on instance count.

**ε/μ axis classification** + **gap-cells table** + **companion-row links** all from 2026-05-19 baseline — UNVERIFIED for further changes.

**Internal inconsistency carried forward**: Row 11 MOND classified SYM at line 38 of catalog vs. canonical leaf `saturated-lattice-mutual-inductance.md:4` ASYM-N(μ). UNVERIFIED whether resolved.

## Reference paths (canonical, tracked)

| Path | Purpose |
|---|---|
| [`_orchestration/theoretical/section-e-cascade.md`](theoretical/section-e-cascade.md) | Section E cascade (ACTIVE — E1b-prime CLOSED Marginal-D; SDSS DR17 + Shamir CLOSED) |
| [`_orchestration/theoretical/soliton-lattice-coupling-operator.md`](theoretical/soliton-lattice-coupling-operator.md) | Soliton-coupling epic (ACTIVE — Sessions 1+2 CLOSED; Sessions 3-5 queued) |
| [`_orchestration/theoretical/cosmic-epsilon-de-projection-scoping.md`](theoretical/cosmic-epsilon-de-projection-scoping.md) | β cosmic-ε / DE projection epic (ACTIVE — Sessions 1+2 CLOSED; Sessions 3-4 conditional) |
| [`_orchestration/experimental/experimental-arc.md`](experimental/experimental-arc.md) | Experimental Arc parent epic + 3 sub-epics (a1-hopf + c11-mach-zehnder + c15-cleave-01) at `experimental/<slug>/` |
| [`_orchestration/_archive/`](_archive/) | 7 top-level closed-epic docs (cosmic-axis-glossary + h-infinity 3 + c5-sdss-dr17 + c5-shamir-2022); pre-Phase-B archive |
| [`_orchestration/README.md`](README.md) | Convention doc; spawn discipline; lifecycle pattern; Phase B reorg structure |
| [`CLAUDE.md`](../CLAUDE.md) | AVE-Core agent orientation; pre-commit branch-check; merge pattern |
| [`manuscript/ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md) | Cross-cutting KB invariants |
| [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) | A-034 catalog (26 instances, 4-axis classification) |
| [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) | 33-row experimental-claim landscape; C5 row Marginal-D + cross-catalog sub-findings |
| [`manuscript/ave-kb/claim-quality-closure-roadmap.md`](../manuscript/ave-kb/claim-quality-closure-roadmap.md) | Closure roadmap (relocated to KB root; now clm-id-annotated → points into the claim DAG) |
| [`manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md`](../manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md) | K4 rest frame ↔ Ω_freeze definitional leaf (NEW earlier in session) |
| [`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md) | Op14 cosmic-horizon profile leaf (NEW β Session 2) |
| `data/pantheon_plus/README.md` + `data/sdss_dr17/README.md` + `data/shamir_2022/README.md` | Canonical data caches with re-download instructions |
| `git tag -l "audit/*" \| wc -l` | 34 immutable audit tags (13 new this session, including c8-baryon-ladder post-session) |
| [`.agents/handoffs/`](../.agents/handoffs/) | Ephemeral scratch (gitignored; NOT canonical) |

## Playbook for the next orchestration session

1. **First read**: this file (`index.md`) + the relevant active epic doc(s) — particularly `soliton-lattice-coupling-operator.md` and `cosmic-epsilon-de-projection-scoping.md` (both multi-session, Sessions 3+ queued).
2. **Phase 0 state verification**:
   - `git log analysis/integration -1 --oneline` should match HEAD `f9b2e55` (or have advanced).
   - `git tag -l "audit/*" | wc -l` should match 33 (or higher).
   - `git branch --show-current` should report `analysis/integration` — if not, `git checkout analysis/integration` BEFORE any commit per CLAUDE.md "Pre-commit discipline" section.
   - Verify no leftover worktrees at `.claude/worktrees/` (none expected at handoff).
3. **Don't trust corpus-state claims here without re-verifying** (per `verify-before-cite` v1.4 triggers 7c + 8 + 9): facts here are accurate as of 2026-05-19 EOD+; re-verify if days/weeks later. For any merge decision, fire trigger 9 — attempt `git merge --no-commit --no-ff` with audit-tag safety BEFORE generating adjudication options.
4. **Ask Grant**: which adjudication item to action first. Default if not specified: priority ladder item 1 (Soliton-coupling Session 3 with Neptune sub-class refinement). The methodology-systematic adjudication (item 1) is the most physically interesting but has multi-session downstream cascade.
5. **For implementor-session kickoff**: append a `## Phase X (PENDING)` section to the relevant epic doc with assumptions A1-AN, scope boundary, phase plan, adjudication criteria, verification — that's the implementor briefing. Spawn `ave-implementer` agent with `isolation: "worktree"`. **Immediately after spawn, run `git checkout analysis/integration` to defensively avoid the worktree-spawn branch-state leak failure (3rd recurrence this session — pattern, not instance)**.
6. **At session close**: update this file (`index.md`) — bump HEAD ref, audit count, active-epic statuses, closed-epic table, adjudication queue. Per `ave-handoff-canonical-locale` v1.0 discipline.

## Pure-AVE-corpus rule

All content in this directory is pure physics. No external context (no investor / fund / interview references). Tracked files MUST be scrubbed before commit.
