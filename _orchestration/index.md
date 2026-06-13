# AVE-Core Orchestration Index

**Audit trail (2026-05-23 Benn → 2026-05-25 merge):** This directory was ported from `analysis/integration` (D7 curation, KB claim-DAG integration) on 2026-05-23, and completed-work snapshots were moved to [`_archive/index-stale.md`](_archive/index-stale.md). Merged with integration live state on 2026-05-25 — treat this doc as the current live tracker; consult git log for recent updates.
**EDIT** - 2026-05-23 Benn - document deprecated. Do not do any sweeping work from this document without evaluating current repo state. KB claim DAG has received many improvements and the KB has had many fixups in the process. This directory was ported over from `analysis/integration` branch, which has now been superseded. Work that was clearly already done has been extracted and moved to _archive/. What remains may still be relevant, but again, *check first*.

> **Staleness notice (2026-06-12)**: The **2026-06-12 reconciliation** below is authoritative for **execution order**, active epics, decision-stack physics read, and harness phases. The **2026-06-11** block below remains valid for PR-merge history only; its Grant decision stack (D1/D2 **CLOSED** rows) is **superseded for execution** by §2026-06-12. Older sections (2026-05-28 priority ladder, open decisions #1–#20) remain historical unless touched by §2026-06-12. Verify-before-cite v1.4 applies.

## 2026-06-12 reconciliation (LOOP GAP harness pivot + audit discipline — ACTIVE)

**Authoritative execution plan:** [`2026-06-12_loop-gap-orchestration-plan.md`](2026-06-12_loop-gap-orchestration-plan.md) (pedantic phases A→G).

### Theory SOTA (one paragraph)

Electron = **Class A/B consistency structure** on **z=4 diamond K4** (`research/2026-06-08_ave-electron-definitive.md`). **LOOP GAP** = anhysteretic Level-1 kernel cannot retain mass at zero drive — ranks 1–4 closure on **one harness** (`loop_gap_harness.py`), not new srs genesis versions. **α** = Class B calibration (R1 forward check DIFFERENT-RATIO). **srs** = discrete **chirality instrument** (R3 structural D1-A landed); **not** demonstrated substrate migration (P5/P6 at post-rupture regime — **quarantined**). **Channel discipline:** `Γ_EM`, `Γ_shear`, Op14 `proxy` `gamma_min`, and `Γ_bulk` are distinct Smith charts. **Rank 4 crux:** R2 ferrite B–H bench + memristive harness P11.

### Active epics (execution order)

| Priority | Epic | Doc | Phase | Next step |
|:---:|:---|:---|:---|:---|
| **P0** | LOOP GAP orchestration plan | [`2026-06-12_loop-gap-orchestration-plan.md`](2026-06-12_loop-gap-orchestration-plan.md) | **A** ✅ | Merged #207 |
| **P1** | Unified K4 harness | [`2026-06-12_loop-gap-unified-harness.md`](2026-06-12_loop-gap-unified-harness.md) | **B** (2b) ✅ | **LANDED** #207 + #208 handoff |
| **P1b** | Vol 9 three-channel KB | [`2026-06-12_vol9-kb-discipline-pass.md`](2026-06-12_vol9-kb-discipline-pass.md) | ✅ | **LANDED** #209 |
| **P1c** | srs genesis archive | Plan §PR4 | ✅ | **LANDED** #211 @ `7cf5cdd6`; audit `audit/2026-06-13_loop-gap-genesis-archive` |
| **P2** | Corpus discipline | Plan §Phase C | **C** ✅ | **LANDED** #210 — D1 reframe + regime quarantine |
| **P3** | Rank-1 regime charter | Plan §Phase D | **D** | **NEXT** — `gamma_bulk` + seed/`A_LOCK` sweep; branch `analysis/2026-06-12-loop-gap-phase-d` |
| **P4** | Electron synthesis (record) | [`2026-06-07_electron-synthesis-epic.md`](2026-06-07_electron-synthesis-epic.md) | — | Ranks via harness only |
| **P5** | R2 constitutive loop | `research/2026-06-12_constitutive-loop-r2-prereg_FROZEN.md` | **G2** (parallel) | Ferrite bench when Grant schedules |
| — | Experimental arc | [`experimental/experimental-arc.md`](experimental/experimental-arc.md) | — | Unchanged |

**Session handoff:** [`2026-06-12_loop-gap-orchestration-session-handoff.md`](2026-06-12_loop-gap-orchestration-session-handoff.md) · **`main` HEAD:** `31c4235c` (PR #211 merged). **Next:** Phase D implementor (`gamma_bulk` + seed/`A_LOCK` ablation).

### Decision stack (2026-06-12 physics read — supersedes 2026-06-11 CLOSED rows for execution)

| ID | Session record (2026-06-11) | Physics read (2026-06-12) | Plan action |
|:---|:---|:---|:---|
| D1 structural | (via R3) | **LANDED** — decoration ρ ≈ 0.057% | Keep |
| D1 framing | B-primary / A-partial | **REOPEN** — SESSION-RECORD; quarantined P5/P6 bins | **LANDED** #210 (Phase C) |
| D2 snap | σ + rate-gated snap | **DOWNGRADE** — v10: not load-bearing | σ-only harness default |
| D3 | Phase-1/2 freeze | Keep | — |
| D4/D5 | χ equal; Ω_freeze IC | Ω_freeze ≠ remanence (ablation falsified) | Ablation arms only |
| Pivot | — | srs v17 **FROZEN**; harness **ACTIVE** | Plan §5 do-not-do |

**Grant confirm queue (non-blocking):** voice on D1-B / D2 / D5 — record in PR body.

### Fundamentality plan (re-ranked for harness world)

| Rank | Item | Status | Notes |
|:---|:---|:---|:---|
| R1 | Impedance + α forward | ✅ | Three-impedance law normative |
| **R2** | Constitutive-loop ferrite bench | FROZEN | **Parallel Phase G2** — rank-4 ground truth |
| R3 | srs structural test | ✅ D1-A | Framing open; not blocking harness |
| R5 | Boost-covariant transport | OPEN | Deferred — v12/v14 transport class |
| **Harness** | LOOP GAP ranks 1–4 | **ACTIVE** | Replaces R8 "v9 Phase-1 genesis" as primary sim path |

### Anti-patterns (2026-06-12)

- New `chiral_lattice_v{N}` / `genesis_v{N}` without DAG rank advance
- Proxy-only N=14 harness production without `--bulk` + regime gate
- Promoting `gamma_min` as `Γ_bulk` or rank-1 PASS as bulk PASS
- Adjudicating D1 migration from `max(A²) ≫ 1` bins

### Carry-forward

- **Phase D** implementor off `main` — rank-1 regime charter (`research/2026-06-12_loop-gap-harness-rank1-regime_prereg_DRAFT.md` → FROZEN)
- Phases E–G per orchestration plan (seed ±k fix, ranks 2–3, rank-4 + R2 bench)
- Audit tags on origin: `audit/2026-06-12_loop-gap-harness-phase2b` (`98ec9270`), `audit/2026-06-13_loop-gap-genesis-archive` (`7cf5cdd6`)
- Merged LOOP GAP branches deleted (local + origin)

---

## 2026-06-11 reconciliation (genesis mega-session merge close-out — COMPLETE)

Orchestration merge session. **`origin/main` HEAD `0b4b9d5c`** (Merge PR #184). **0 open PRs.** 20 PRs merged (#180–#199 except #143 closed, #175 absorbed via #180); 20 audit tags pushed (`audit/2026-06-11_*`); implementor branches deleted. Capstone docs on main: [`2026-06-11_session-handoff.md`](2026-06-11_session-handoff.md), [`2026-06-10_genesis-session-workflow-ledger.md`](2026-06-10_genesis-session-workflow-ledger.md), [`research/2026-06-11_next-step-fundamentality-plan.md`](../research/2026-06-11_next-step-fundamentality-plan.md).

### Theory SOTA (post-merge, one paragraph)
Electron = **Class A/B consistency structure** (`research/2026-06-08_ave-electron-definitive.md`): (2,3) phase-space topology + cubic T_d envelope on **z=4 diamond**; genesis **planted not emergent**. **α = Class B / calibration** — R1 forward check **DIFFERENT-RATIO** (α/13.9 at partition (a); PR #198); turns-ratio route dead at (a); a3 successor resumable on `origin/analysis/2026-06-11-alpha-a3-reservoir`. **Genesis:** 9 architectures tested (#180–#195); **no mass retention without lock**; central diagnosis = **LOOP GAP** (anhysteretic kernel, no B-H remanence). **Engine gap:** no boost-covariant transport (4× confirmed). **Lattice:** z=4 diamond on main; srs-vs-diamond **reopened** — blocks v9 Phase-1. **Experimental round-2 survivors unchanged:** Cleave-01 GO, Q-G42 V²-sign, birefringence coefficient, HOPF reciprocity.

### CLOSED this session
- **PR queue #180–#199** — all merged or closed (#143 superseded).
- **#184 conflict** — `unified_genesis_engine.py`: retained v7 quadrature + v8 polyphase init paths (additive layers).
- **Audit + branch hygiene** — +20 tags (133 total on origin); 20 implementor branches deleted.

### Active epic (updated)
| Epic | Doc | Status | Next |
|---|---|---|---|
| Electron-structure / genesis | [`2026-06-07_electron-synthesis-epic.md`](2026-06-07_electron-synthesis-epic.md) + [`2026-06-11_session-handoff.md`](2026-06-11_session-handoff.md) | **ACTIVE — genesis v6–v9 record landed; v10 chartered (CVR)** | Grant decision stack (below); then fundamentality plan R2→R8 |
| Experimental Arc | [`experimental/experimental-arc.md`](experimental/experimental-arc.md) | **ACTIVE — round-2 survivors** | Cleave Phase 1b (Grant manual); HOPF reciprocity; cRIO prereg (#181 landed) |

### Grant decision stack (v10 — **CLOSED 2026-06-11**)
| # | Call | Ruling |
|---|---|---|
| D1 | srs-vs-diamond | ✅ B-primary / A-partial (D1 memo) |
| D2 | Loop scope | ✅ **σ + rate-gated snap** (amended 2026-06-11) |
| D3 | Phase-1/2 freeze | ✅ FROZEN + executed |
| D4 | `chi_shock` / `H_*` | ✅ **Per-channel χ equal** + `H_*` ON |
| D5 | Ω_freeze IC | ✅ Canonical IC ON + ablation |
| — | Proton body scale | Still open — epic §45–§47 |

### Fundamentality plan (ranked — Grant-greenlit, on main)
| Rank | Item | Gate |
|---|---|---|
| R1 ✅ | Impedance repair + α forward check (#198) | Ratify three-impedance law |
| **R2** ✅ | Constitutive-loop prereg + cRIO ferrite B-H bench | **FROZEN 2026-06-11** — bench execution next |
| **R3** | srs-vs-diamond adjudication | Blocks R8 |
| R4 | Layer-8 mₑ-free smallest-stable-soliton | — |
| R5 | Boost-covariant transport (master-unblocker) | Expensive |
| R6 | σ-equipped shell formation | — |
| R7 | V↔ρ̄ death channel | Gated on R5 |
| R8 | v9 Phase-1 genesis | **Gated on R3** |

**Branch plan:** [`2026-06-11_orchestration-branch-plan.md`](2026-06-11_orchestration-branch-plan.md).

### Resumable branches (kept on origin)
| Branch | Workstream |
|---|---|
| `analysis/2026-06-11-alpha-a3-reservoir` | a3 α-successor (reservoir partition) |
| `analysis/2026-06-11-chiral-angle-of-attack` | chiral AoA scouts |
| `analysis/2026-06-11-fbd-v2-bubble` | FBD-v2 (column not bubble re-scope) |
| `analysis/2026-06-11-screened-winding-probe` | Panel-demoted; Grant decides |

### Carry-forward
- Soliton-size vocab disambiguation (14 terms, epic §47) — canon gated on Grant review.
- r_opt → κ_share propagation (14 sites still surfaced; #132 open).
- Orchestration index body (active-epics table §, adjudication queue) — still 2026-05-28; re-verify before relying.
- Untracked locally: `experimental/c15-cleave-01/exp-c15-cleave-01-state-audit-2026-06-06.md` — triage on orch branch or separate.
- **Audit tag count:** **133** (`git tag -l "audit/*" | wc -l`).

---

## 2026-06-08 reconciliation (electron-synthesis + α-route + soliton-size arc) — SUPERSEDED for PR queue

> **Superseded 2026-06-11:** the "21 open PRs (#117–#137)" state below is stale. PRs #117–#199 merged through the 2026-06-11 orchestration session. Retained for arc history (α-route sweep, soliton-size §46–§47, proton mass §39–§41).

## 2026-06-08 reconciliation (electron-synthesis + α-route + soliton-size arc)

Multi-session delta. **`origin/main` HEAD `63e6671a`** (Merge PR #116). Adds the
2026-06-07/08 electron-structure synthesis arc. Full handoff:
[`2026-06-08_session-handoff.md`](2026-06-08_session-handoff.md); detailed phase
log §0–§47 in [`2026-06-07_electron-synthesis-epic.md`](2026-06-07_electron-synthesis-epic.md)
(PR #120); per-PR review checklist: [`2026-06-08_pr-review-guide.md`](2026-06-08_pr-review-guide.md).

### State of the board
- **21 open PRs (#117–#137)**, all `MERGEABLE` against `main` (verified
  `gh pr list --state open`, 2026-06-08). Grant reviews each himself — see the
  review guide. **DO NOT auto-merge.**
- **46 worktrees**: 21 KEEP (1 per open PR) / 22 prune-safe / 3 HOLD
  (uncommitted work). Prune-list = §9 of the handoff doc. **List-only; nothing
  pruned this session.** Main checkout is parked on `analysis/2026-06-07-two-node-
  alpha-projection` (PR #126); carries 1 untracked stray flagged in the handoff.

### CLOSED / resolved
- **α-value derivation = NEGATIVE on every closed route** (incl. the z₀=52
  "1.5%" WALK-BACK, §31 — unforced path-multiplicity, physical z≈16→1/α≈49). AVE
  constrains α's SCALE + FUNCTIONAL FORM (substrate geometry) but does NOT derive
  its VALUE; α stays **Class-B**. The framing (α = a vacuum loss-tangent, not a
  constant) is the chord; the value is a calibration entry. [§18/§22/§25/§31.]
- **Fork A (genesis amplitude crux)**: electron = parametric oscillator at
  threshold = marginal Hopf limit cycle at ω_C. [§9/§12/§13/§19.]
- **Lattice = z=4 achiral diamond** (water-confirmed); spin/chirality on the
  Cosserat microrotation, not the net. [§8.1/§16/§28.]
- **proton = PHASE-space (2,5)** (walk-back, PR #132); **proton-mass I_scalar=1162
  forward-DERIVED not fitted** (+0.74% topology-only; −0.002% rides 1 thermal
  correction, proton-specific coincidence). [§36/§39/§40.]
- **QM trio** (PR #128); **piezoelectric framing** (PR #127); **force-projection
  grounding** (→ #130/#137). All consistency-class.

### Active epic (add to the Active-epics table)
| Epic | Doc | Status | Next |
|---|---|---|---|
| Electron-structure synthesis | [`2026-06-07_electron-synthesis-epic.md`](2026-06-07_electron-synthesis-epic.md) | **ACTIVE — §0–§47 logged; α-derivation closed-negative; soliton-size GAP scoped** | Soliton-size adoption (gated on vocab-lock + greenlight); then the operating-point coefficients (the falsifiable, AVE-distinct datasheet column) |

### Priority ladder delta (supersedes the 2026-05-28 ladder for the immediate tier)
1. **21-PR review backlog** (#117–#137) — Grant reviews each; the review guide
   orders them (fast batch → r_opt walk-back chain in order → HIGH-risk #126).
2. **Soliton-size adoption** (the recommended next workstream) — COHERENT-BUT-
   SYNTHESIS (§46); gated on the `w1pc27h3k` vocab-disambiguation lock (§47, 14
   clarity-risk terms) + Grant greenlight. Plan = §7 of the handoff.
3. **Operating-point coefficients** (dc/dA, dα/dT, dε/dE) — the falsifiable,
   AVE-distinct test surface (§26/§40 suggested next-effort), now that α's value
   is honestly bounded.

### Open decisions surfaced 2026-06-08 (carry forward)
| # | Item | Detail |
|---|---|---|
| 21 | **Soliton-size adoption mode** | adopt node-Nyquist two-size framing? gated on vocab-lock + greenlight (§46/§47). |
| 22 | **Multi-node-vs-single-node proton** | `02_baryon_sector.tex:40` (multi) vs `semiconductor_binding_engine.py:68` (single); decides the §43/§45 fork. |
| 23 | **§43/§45 A-vs-B canonical fork** | proton body sub-node (A; r_opt-as-length = bug) vs supra-node (B; STLs correct-scale). Do NOT collapse. |
| 24 | **√(3/7) dilatational-vs-torsion** | √(1−2ν) bulk signature vs the muon leaf's "torsion-shear" label; identity exact, label at-issue (§40/§41). Flag-don't-fix. |
| 25 | **cold-vs-thermal κ_FS** | proton leaf COLD 8π/5=5.03 vs ladder THERMAL κ_eff/5=4.990; single convention = Grant's call (§42). |
| 26 | **Manuscript-figure reference** | which figures #129/#134 feed, at what scale-claim tier (gated on #23). |
| 27 | **Emergence-vs-consistency m_p/m_e** | prereg (consistency) vs leaf Class-4 (emergence) self-classification (§38). |

### New infrastructure
- 2 new skills (drafted + live-validated §40): `ave-dimensional-provenance-check`
  (coupling/count-as-length guard), `ave-live-fire-derivation-provenance`
  (dead-input + forward-vs-fit residual guard).
- Code-provenance index prototype (PR #136, §44).
- **SKILL-CANDIDATE (watch)**: `lock-vocab-before-canonizing` (§46) — 5-way term
  cross-check before locking a canonical term.

### Discipline note
The session repeatedly inflated good intuitions into "mechanisms" + reasoned from
a partial archive slice (multiple Grant-pointer corrections: φ-premise inverted,
z₀ effort missed, chiral-matching ungrounded, cog→belt-trick, spherical-vs-cubic).
Next effort: GROUND intuitions + SWEEP the archive BEFORE framing a result.

---

## 2026-06-04 reconciliation (experimental round-2 hardening arc — COMPLETE)

Multi-session delta. **HEAD `d6f636f8`+** (verify vs `git log origin/main`). Directly **EXECUTES** the 2026-06-02 carry-forward item #1 (the experimental falsification pivot) — and reshapes it.

### The arc
2026-06-03 protocol revamp ([`2026-06-03_experimental-protocol-revamp-orchestration.md`](2026-06-03_experimental-protocol-revamp-orchestration.md)) surveyed + ranked the board → round-1 + round-2 adversarial hardening → **7 adjudications** (each EE-mapped + skill-disciplined) in the ledger [`experimental/2026-06-04_round2-adjudications.md`](experimental/2026-06-04_round2-adjudications.md) → merges → corrections → closure. Capstone narrative: [`research/2026-06-04_experimental-round2-synthesis.md`](../research/2026-06-04_experimental-round2-synthesis.md). Changelog: `claim-quality-closure-roadmap.md` §0.5 (round-2-arc row).

### Survivor board (SUPERSEDES the 2026-06-02 ranked pivot list)
- **Cleave-01** — SURVIVES + upgraded (gap-independent 4-corner symmetry; round-1 "SM=0.0" was FALSE — CPD). Flagship near-term bench (~$7.7k).
- **Birefringence-E4** — SURVIVES, reframed (coefficient discriminator ~10⁶× QED; the shipped "E² slope falsifies AVE" false-falsifier KILLED). Facility-class.
- **Q-G42 V²-sign** — forward, feasibility-gated. **HOPF** — C3/C4 retired (consistency-class); surviving leg = 2-port reciprocity sweep ($123).
- **Sagnac → RETIRED** · **IVIM → interferometric** (bench-undetectable) · **PONDER-05 → MATERIAL** (per-node conflation; reclassified across INVARIANT-S2 + corpus + EE-skill) · **NA-aperture → keep-derivation/deflate-anchor**.
- **Throughline (end-to-end):** SYMMETRY / SIGN / zero-free-param discriminators survive; MAGNITUDE / per-node-conflation-anchored ones deflate.

### Landed
All 4 round-2 + 3 corrections branches merged (AVE-Core + AVE-HOPF), audit-tagged, deleted. Public **README sweep** (`7b2ff096`): kill-switch table reframed to the survivors + honest-α propagated to the headlines/badge + stale rows fixed (g-2 demoted, δ_strain walked-back); `run_kill_switches.py` rewritten to the survivors (`d6f636f8`). 109 audit tags on origin.

### Carry-forward / follow-ons
- The broader `.tex` per-node-conflation echo sweep (13 files; KB `.md` corrected; flagged in §0.5).
- Per-row prediction-table classification + A-034 19-vs-26 corpus inconsistency (hygiene).
- Facility-class tests (birefringence, Q-G42) await a partner facility; near-term bench = Cleave + HOPF reciprocity sweep.
- **z₀-from-K4** — the one still-open α-route (see the 2026-06-02 section below).

## 2026-06-02 reconciliation (α Class-2 lift investigation + honest-α relabel)

Single-session delta from 2026-05-31 EOD. Verified against `git log origin/main` + `git tag -l`. **HEAD `b409b169`.** Directly addresses carry-forward item #1 (Class-2 lift candidate) in the 2026-05-31 section below.

### CLOSED — α Class-2 lift: the substrate does NOT independently select the identification

Question: does the K4 + Cosserat substrate **dynamically select** the (2,3) + R·r=¼ identification (the one posit under α's closed form) from a generic seed? **Outcome: NO** — closed across four engine×dynamics tests + the doc-34 static wall + the z₀ α-circularity:
- 4 dynamic engine tests — FDTD nonlinear-saturation → dispersed; static Cosserat S11-relax → flat; dressed-eigenmode → flat; chiral-Meissner (κ_chiral) → flat/small. Immutable negative record (driver source + findings on origin): `audit/2026-06-02_alpha-lift-{cell-count,cosserat-binding,dressed-eigenmode,chiral-dressing}`.
- doc-34 (`research/_archive/L3_electron_soliton/34_x4_constrained_s11.md`): "S11 landscape is flat within the hedgehog family … not uniquely selected without additional constraints."
- z₀ α-circularity: rigidity-route z₀≈51.25 ← C_ratio=1.187 ← p_c=8πα (imposes α, doesn't read it out).

**Genuine gain (survives the null):** α's **scale (~1/137) IS forced** — Compton-resonance trapping (cavity ≈ one Compton wavelength ≈ 4π³ Nyquist cells → Q≈137). Only the **exact** value (4π³+π²+π) rests on the one identification per route. Stronger + more precise than the prior "α rests entirely on R·r=¼."

### Honest-α relabel landed (merged `7e763b1f`, `--no-ff`)

Type-D framing narrowing (`ave-walk-back`): "derives / Zero-Parameter Closure" → "closed-form-at-one-identification, Class B." 20 files + straggler-fix, framing-only, `make verify` PASS, **NO value / prediction / matrix changed** (constants.py untouched). ch8 title → "Closed-Form α from the Golden Torus"; foreword honest-α scope para; trace-reversal + foreword two-engine → z₀ α-circular caveat. Tag `audit/2026-06-02_honest-alpha-relabel`.

### NEW content 2026-06-02

- **Epic**: `_orchestration/2026-06-02_alpha-class2-lift-radiation-resistance.md` (§1–§10 investigation + §11 close-state + §12 experimental pivot).
- **EE-native α framing capture**: `research/2026-06-02_alpha-ee-native-framing.md` — loss-tangent=1/Q, saturable-reactor cavity, Q=cell-count (scale-forced), dual-reactance=Cosserat-6DOF, geosync universality, photon-emission=mirror-leak, two α-routes; provenance-tagged (canonical/synthesis/Class-B). Promotion to `translation-circuit.md` (clm-eemap1) flagged, NOT done.

### Carry-forward to next session (2026-06-02)

1. **Experimental falsification pivot** (epic §12) — **✓ EXECUTED 2026-06-04** (see the 2026-06-04 reconciliation section above; the ranked list below was reshaped by round-2 — Sagnac RETIRED, vacuum-birefringence reframed E⁴-vs-E²→coefficient, √α impedance-mirror = per-node conflation). *Original carry-forward:* point verify-to-source at the NOVEL predictions, not more α-postdiction; **Phase-0 magnitude-gate first**. Ranked: Sagnac-RLVE (Δφ≈2.07 rad) / vacuum-birefringence E⁴-vs-E² / √α impedance-mirror (43.65 kV) / DAMA Z-independence. Pure-physics "near-term falsification priorities" doc scoped, NOT written.
2. **Two open first-principles threads** (either lifts a route to independent α): (a) **L3 dynamic trapping** — full nonlinear + chiral self-lock to R·r=¼ (the unsolved L3 bound-state problem; **supersedes the 2026-05-31 carry-forward #1** phasor↔real-space bijection step); (b) **z₀ from K4 amorphous coordination** (first-pass crystalline counting failed; currently α-circular).
3. **EE-mapping promotion** — clean rows from the EE-framing capture → `translation-circuit.md` (clm-eemap1) per `ave-ee-first-mapping` Step 6 (+ mirror vol2-appendix + vol4).

### Audit tags 2026-06-02

+5 this session (all on origin): `audit/2026-06-02_honest-alpha-relabel` + `audit/2026-06-02_alpha-lift-{cell-count,cosserat-binding,dressed-eigenmode,chiral-dressing}` (the 4 lift tags preserve driver source; findings in the epic). Separately, 4 earlier-2026-06-02 tags from other work also on origin (`baryon-r2-crossing-coupling`, `parameter-ledger-v2-reframe`, `tau-yield-reactance-count`, `zero-parameter-headline-reframe`). Baseline was 70 at 2026-05-31 EOD.

## 2026-05-31 reconciliation (Q-EMBED-SEL-1 substrate-mechanism arc)

Single-day delta from 2026-05-28 EOD++ baseline. All items verified against `git log origin/main` + `git tag -l "audit/*"` + PR merge state.

### PRs landed 2026-05-31 (3 PRs)

| PR | Title (short) | Landed | Notes |
|---|---|---|---|
| #59 | Q-EMBED-SEL-1 substrate-mechanism (Phase 1+2+3) | 2026-05-31 | Merge `7e814523..7529f7ce`. Class B closure for $\sqrt{R \cdot r} = d/2$ via Ax 4 self-saturation + Op14 + named phasor-area-equals-Nyquist-cell-area identification; cross-particle universal (electron/proton/Δ); cross-domain (NASA Glenn cold fusion + FP stochastic-irreproducibility framing); ponderomotive-equivalence cross-scale. |
| #60 | Q-EMBED-SEL-1 Phase 4 corpus walk-back | 2026-05-31 | Merge `7529f7ce..06161da6`. 46 files; spinor-half-cover provenance retired across corpus; new substrate-mechanism stamped canonical. Main sweep `a581d9f4` (33 files) + fixup `34a163f2` (13 files; sweep-audit findings). |
| #61 | orch(Q-EMBED-SEL-1 epic CLOSED markers) | 2026-05-31 | This-session orch state update + this reconciliation section + carry-forward consolidation. |

### Workstreams CLOSED 2026-05-31

- **Q-EMBED-SEL-1 evaluation epic** (4 phases, parent at `_orchestration/2026-05-31_q-embed-sel-1-evaluation.md`) — Phase 1+2+3 Outcome A (Class B substrate-mechanism); Phase 4 corpus walk-back propagated. The framework's α-derivation now anchored in **Class B substrate-mechanism manifestation** with the QED-imported spinor half-cover argument (doc 29 F5 + doc 39 §3.4 critique) RETIRED corpus-wide.
- **Parameter-count framing walkback epic Phase 3** (`_orchestration/2026-05-28_parameter-count-framing-walkback.md` §3.6) — RESOLVED by Q-EMBED-SEL-1 closure. The 2026-05-28 Phase 1+2 gating clause ("contingent on one open formal step: ropelength-minimality...") is SUPERSEDED. Framework upgrade: from "zero-parameter, gated on unproven embedding-selection" to "Class B substrate-mechanism manifestation, cross-particle universal + cross-domain validated + corpus-walkback propagated."

### NEW canonical content 2026-05-31

- **Phase 1+2+3 result docs** at `research/2026-05-31_Q-EMBED-SEL-1_step_c_*.md` (4 docs: prereg + result + Phase 2 prereg + Phase 2 result + Phase 3 prereg + Phase 3 result + Phase 4 prereg + Phase 4 result = effectively 8 docs across the 4 phases; canonical for the new substrate-mechanism).
- **Substrate-mechanism replacement of ch8 step 4** (`manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md`): retired spinor half-cover; new provenance via Ax 4 self-saturation + Op14 Meissner-asymmetric + named phasor-area-equals-Nyquist-cell-area identification. K4 → A4 → 2T ⊂ SU(2) chain preserved canonical for spin-½ structure (steps 1–3); only the downstream surface-area halving (step 4) retired. The $4\pi$ factor in $\Lambda_{\text{vol}}$ now substrate-derived from bipartite K4 lobe-count.
- **Cross-domain anchor**: same Ax 4 self-saturation + Op14 mechanism extends to Pd-D cold-fusion via $n_{\text{scalar}} = 1/S(A_0)$ identification (same form as ponderomotive equivalence at gravitational scale). Quantitatively predicts NASA Glenn lattice-confinement (~keV, ~10² reduction) AND quantitatively explains Fleischmann-Pons stochastic-irreproducibility as 2.9% operational tolerance sliver at metallurgical shatter limit.

### Audit tags 2026-05-31

- 2026-05-28 EOD++ baseline: 68 tags.
- 2026-05-31 EOD: **70 tags** (+2 this session).
- New this session: `audit/2026-05-31_q-embed-sel-1-substrate-mechanism` → `118a33a3` (Phase 1+2+3); `audit/2026-05-31_q-embed-sel-1-phase-4-corpus-walkback` → `34a163f2` (Phase 4).

### Memory + skill amendments 2026-05-31

- **Memory v2** of `feedback_branch_discipline_colleagues.md` — widened the pre-action check to cover push-to-main + merge-to-main + force-push, not just commit-on-main. Triggered by integration→main FF-push routing-convention slip (issue #58); landed during this session arc.
- No new skills landed; existing skills exercised heavily: `ave-prereg`, `pre-test-physics-check`, `phase-space-coordinate-check`, `ave-walk-back` v1.2, `ave-sweep-audit`, `consistency-vs-emergence` v1.3, `verify-before-cite` v1.4, `ave-evidence-framing-discipline`, `ave-discipline-translate` v1.1, `ave-canonical-leaf-pull`, `ave-canonical-source`, `ave-worktree-paths`, `ave-handoff-canonical-locale`.

### Carry-forward to next session (3 items)

**1. Class-2 lift candidate workstream** — derive the phasor↔real-space area bijection at the bond LC tank from K4 + Cosserat substrate primitives alone. Would lift the Q-EMBED-SEL-1 substrate-mechanism from Class B to Class 2. **Canonical anchor**: `research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md` §7.3. Out of scope for the closed epic; standalone future workstream.

**2. AVE-HOPF cross-repo reconciliation** — `AVE-HOPF/docs/glossary.md:32` (Grant 2026-04-30 bracketing of Golden Torus as "post-IP-separation patch-attempt") needs un-bracketing per the now-validated Class B substrate-mechanism on AVE-Core main. Cross-repo PR in AVE-HOPF; gated on Grant call (or auto-spawnable per the now-validated provenance). **Canonical anchor**: `_orchestration/2026-05-31_q-embed-sel-1-evaluation.md` §11 (final bullet) + the Phase 1+2+3 result docs on AVE-Core main.

**3. Class C deferred sites from sweep-audit (3 minor descriptors)** — captured here for persistence (auditor transcript doesn't persist):
- `_orchestration/_archive/path-b-prime-k4-dispersion-pq.md:158` — "Ax 3 Min-reflection spinor half-cover" (archived doc; preservation territory; arguably skip)
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot-cosserat-seeder.md:112` — minor cross-reference text "α derivation at Golden Torus + half-cover canonical"
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md:11` — bridging-role descriptor "regime (c) half-cover both presuppose"

**Plus inline-comment Class B-4 sites** (operational, not corpus-load-bearing — auditor flagged but explicitly deferred):
- `src/scripts/vol_1_foundations/verify_lambda_line.py`
- `src/scripts/vol_1_foundations/validate_cosserat_alpha_via_ch8_ratios.py`
- `src/scripts/vol_1_foundations/op21_multimode_derivation.py`
- `src/scripts/vol_1_foundations/phasor_trajectory_test.py`

All Class C + B-4 items: docstring/comment-only; would not break verify-* or tests. Single-pass `ave-walk-back` mini-sweep when convenient.

---

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
- **Per-overrun `\texttt{path}` cleanup** + margin gate tightening (350pt → 15-30pt) — **DONE 2026-05-28** via merge `a9ab377f` (gate now 45pt; see `2026-05-28_vol9-corpus-latex-formatting.md`).
- **Parameter-count framing walk-back (Option 2 — zero-parameter, gated)** — **EPIC CLOSED 2026-05-28 EOD++**: Phase 1 merge `f6b22757` (audit tag `audit/2026-05-28_parameter-count-gating-phase1` → `9b4ae922`); Phase 2 merge `7e814523` (audit tag `audit/2026-05-28_parameter-count-gating-phase2` → `2c0ce429`); sweep-audit cycle resolved D1+B1+B2+C1 via amendment `2c0ce429`. Deferred: C2 (`src/ave/ARCHITECTURE_REVIEW.md` staleness flag); Grant decisions carried forward: title-retitle-vs-gate-under-title + integration→main timing. Doc: [`2026-05-28_parameter-count-framing-walkback.md`](2026-05-28_parameter-count-framing-walkback.md) §CLOSED.
- **Means-test corpus extensions** to muon/tau, neutrino, QCD, cosmological inflation, substrate-microbiology (clm-eemap1 framework extension).

### Audit tag delta

- 2026-05-20 baseline: 35 tags
- 2026-05-28 EOD baseline (per stale upstream count): 65 tags
- 2026-05-28 EOD++ current (verified via `git tag -l "audit/*" | wc -l`): **68 tags** (+33 net across 8 days). The +3 delta from the stated 65→68 is param-gating Phase 1 + Vol 9 formatting + param-gating Phase 2 — the 65 stated above was a pre-EOD snapshot; Phase 1 and Vol 9 formatting tags landed within the same EOD window and the count wasn't refreshed.
- Sweep breakdown: +16 Vol 9 chapter-buildout (incl. rollup), +1 Vol 9 formatting, +1 Phase 3-A4 walkback-cleanup, +2 param-gating Phase 1+2, + earlier-day landings (Path B-prime, 3-A2/3-A3, clm-zuf7g1, ax4-sat 0c/2-NA/2-A).

### What this reconciliation does NOT cover (deferred)

- Section E cascade row in active-epics table — last activity in epic doc was 2026-05-19 EOD; the cascade items (methodology-systematic adjudication, Neptune sub-class adjudication, β cosmic-ε Session 3) have NOT verifiably progressed. Still as-of-2026-05-19 below.
- A1-HOPF Phase 0b — per `exp-a1-hopf.md`: "Phase 0b ready for Grant fab submission". Memory entry `project_hopf_01_status.md` says "boards in hand 2026-05-02; partial knot stitching underway; AVE-HOPF docs lag actual lab state" — so Phase 0b has likely progressed in the lab but AVE-HOPF docs lag. Not updated here; trust the memory entry over the epic doc on lab state.
- C11-MACH-ZEHNDER Phase 0 facility partnership search — NOT verified.
- C15-CLEAVE-01 Phase 1a-rev1 — last activity 2026-05-20; no further progress visible in git log. Likely still gated on Phase 1b/1c Grant manual KiCad work per index header below.
- Adjudication queue items #1 (methodology-systematic), #2 (Neptune), #4 (C5 threshold-policy), #5 (4th-category) — no verifiable progress in 8 days.
- Sibling-repo hygiene items (open decisions #7-10) — UNVERIFIED.
- Pre-commit hook + worktree-spawn-leak discipline fixes — STILL OPEN (worktree-leak recurred during Vol 9 Wave 1 sessions).

---

**Last updated**: 2026-05-20 EOD++++++++++++++ (most sections); 2026-05-28 EOD (audit tag count + staleness notice + HEAD ref); **2026-06-02** (α Class-2 lift close + honest-α relabel — see reconciliation block at top; HEAD `b409b169`)
**Current focus**: Vol 9 "The Vacuum Datasheet" ✅ COMPLETE 2026-05-28 (PR #55 + #56 both merged). Earlier 2026-05-20 focus: C15-CLEAVE-01 Phase 1a-rev1 ✓ COMPLETE — atopile walk-back delivered clean module-level imports; all Q-C15-10/11/12 + Q1.2 + Q-HWMOD-04 CLOSED. Next: A1-HOPF Phase 0b (Grant fab submission, [EXEC]) + C11 Phase 0 outreach ([PREP]) — both still queued.
**Current HEAD on `main`**: `c6d2dcaf` — PR #56 merge (Vol 9 Ch 2-16). Last live integration head on `analysis/integration` (2026-05-20 EOD reference): `5977f4d`.
**Audit tag count (AVE-Core)**: 65 (`git tag -l "audit/*" \| wc -l`) — 16 NEW Vol 9 audit tags landed 2026-05-28: `audit/2026-05-28_vol9-ch{02-16}-*` (15 chapter implementor branches) + `audit/2026-05-28_vol9-chapter-buildout` (integration branch). Was 35 at 2026-05-20 EOD; +30 across 8 days. **(This line is a 2026-05-28 snapshot — for current tags + HEAD see the 2026-06-02 reconciliation at top: +5 this session, 70 baseline at 2026-05-31.)**
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

1. **First read**: this file (`index.md`) — **2026-06-11 reconciliation** at top + [`2026-06-11_orchestration-branch-plan.md`](2026-06-11_orchestration-branch-plan.md) + [`2026-06-11_session-handoff.md`](2026-06-11_session-handoff.md) + [`research/2026-06-11_next-step-fundamentality-plan.md`](../research/2026-06-11_next-step-fundamentality-plan.md).
2. **Phase 0 state verification**:
   - `git log origin/main -1 --oneline` → **`0b4b9d5c`** (or advanced).
   - `git tag -l "audit/*" | wc -l` → **133** (or higher).
   - `gh pr list --state open` → **0** (or new branches only).
   - `git branch --show-current` → work on **`analysis/<date>-<topic>`** branches; merge via reviewed PR only.
3. **Grant calls first** (before spawning implementors): srs-vs-diamond (D1) + constitutive-loop scope (D2) + three-impedance ratification (D7).
4. **Spawn implementors** per branch plan with `isolation: "worktree"`; audit-tag before branch delete.
5. **At session close**: update this reconciliation block + branch plan; never commit orchestration directly to `main`.

## Pure-AVE-corpus rule

All content in this directory is pure physics. No external context (no investor / fund / interview references). Tracked files MUST be scrubbed before commit.
