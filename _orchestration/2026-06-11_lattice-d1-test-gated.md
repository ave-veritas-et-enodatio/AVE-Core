# Epic — Lattice D1 test-gated (srs vs diamond)

**Opened:** 2026-06-11
**Branch:** `analysis/2026-06-11-lattice-d1-test-gated` (orchestration docs)
**Status:** ACTIVE — **test not pick**
**Supersedes:** prose D1 rulings; partial "srs it is" hypothesis stays **hypothesis** until bins land

---

## Principle

**D1 (lattice identity) is an empirical outcome, not a Grant call before sim.**

Writhe-on-srs (Phase-0) is **necessary-condition** evidence only. The symmetric three-arm battery (bare srs, bare diamond, decorated diamond) + Phase-1 P4/P6 ablations are **sufficient** to assign a D1 bin.

---

## Phase log

### Phase 0 — Scaffold + bare-net smokes (COMPLETE, main @ PR #195)

- `chiral_lattice.py` + Phase-0 smokes PASS
- Smoke A: achiral scalar physics preserved on srs
- Smoke B: writhe ±4.0867e-02 on srs enantiomorphs; diamond 0
- **Not decided:** substrate (A) vs decoration (B)

### Phase 1 — R3 decoration discriminator (COMPLETE — branch `analysis/2026-06-11-lattice-d1-test-gated`)

- **Pre-reg:** `research/2026-06-11_lattice-decoration-discriminator_prereg.md`
- **Result:** `research/2026-06-11_lattice-decoration-discriminator_result.md`
- **D1 PARTIAL BIN: D1-A** (R3-P5 FAIL — decoration ρ≈0.057% of srs Bishop; κ sign-flips)
- **Gate:** Phase-1 P4/P6 still required for full D1

### Phase 2 — v9 Phase-1 prereg freeze (COMPLETE — 2026-06-11)

- **FROZEN:** `research/2026-06-11_genesis-v9-phase1-prereg_FROZEN.md`
- **Scope:** P1–P4 + A1–A4 ratified; **P5/P6 deferred to Phase-2** (separate freeze)
- **Visual model:** `research/2026-06-11_helicity-visual-model.md`
- **T4 (parallel):** `research/2026-06-11_electron-mirror-vs-bh-helicity_prereg_DRAFT.md`
- §0 framing (A)/(B) **not** picked at freeze

### Phase 3 — v9 Phase-1 vector-TLM (COMPLETE — P1–P4 ALL PASS)

- **Module:** `src/ave/core/chiral_lattice_vector.py`
- **Tests:** `src/tests/test_chiral_lattice_vector_phase1.py` (5/5)
- **Driver:** `src/scripts/vol_1_foundations/chiral_lattice_phase1_vector_tlm.py`
- **Artifact:** `assets/sim_outputs/genesis_v9_phase1_vector_tlm.json`
- P1 drift ≤1e−8; isotropy ≤2% @ L=8; P2 signed enantiomorph flip; P3 writhe-concordant; P4 diamond null + κ=0 geometry channel
- **Gate for D1:** still need Phase-2 P5/P6 before full adjudication

### Phase 3b — v9 Phase-2 prereg freeze (COMPLETE — 2026-06-11)

- **FROZEN:** `research/2026-06-12_genesis-v9-phase2-prereg_FROZEN.md` (PR #202)
- **Op14:** $z_{\text{local}}(A^2)$ + **Op3 @ CONNECT**; instantaneous v1; ring_writhe charge proxy
- P5 hosting + P6 genesis-by-precursor (CVR-SET bins, A1–A4 inherited)
- §0 D1 framing still deferred

### Phase 3c — v9 Phase-2 implementor (COMPLETE — PR #203 merged @ `d753fc11`)

- **Module:** `src/ave/core/chiral_lattice_vector_sat.py` (Op14 + Op3 @ CONNECT)
- **Tests:** `src/tests/test_chiral_lattice_phase2.py` (6/6)
- **Driver:** `chiral_lattice_phase2_genesis.py` (`--smoke` for CI-scale)
- **CI:** workflow timeout raised to 30m (#203)

### Phase 3d — v9 Phase-2 production battery (COMPLETE — branch `analysis/2026-06-12-genesis-v9-phase2-production`)

- **Run:** L=10, P5 500 steps, P6 800 steps, amp `{0.25,0.5,1.0}`, diamond + Op3/Op14 ablations
- **Result:** `research/2026-06-12_genesis-v9-phase2_result.md` — **P5 FAIL**; P6 partial CVR-SET
  at amp=0.25 only; matched-baseline **FAIL**; no BIN-G genesis promotion
- **Gate:** production bins landed — **D1 memo unblocked**

### Phase 4 — D1 adjudication memo (COMPLETE — 2026-06-12)

- **Memo:** `research/2026-06-12_lattice-d1-adjudication-memo.md`
- **Ruling:** **D1-FINAL: B-primary / A-partial** — structural srs chirality confirmed (D1-A);
  hosting/genesis miss on discrete TLM+Op14; **diamond stays engine substrate**
- **Walk-back:** queue §5 in memo — **authorized, not executed** (Grant greenlight + `ave-walk-back`)

### Phase 4b — D1 corpus walk-back (COMPLETE — 2026-06-12)

- **Branch:** `analysis/2026-06-12-lattice-d1-walkback`
- **Sites:** `eq_axiom_1.tex`, `lattice-net-resolution.md` amendment, design doc §0 ADJUDICATED,
  fundamentality plan R3 ✅
- **Not in scope:** α/Lorentz srs re-derivation; full KB P2 grep-sweep (deferred batch)

### Phase 5 — v10 spine (UNBLOCKED — charter updated 2026-06-12)

- **Charter:** `research/2026-06-11_chiral-vacuum-reactor-framing.md` §5 — Decisions 1+3 ✅
- **Blocked on:** R2 prereg freeze + Decisions **2+4+5** (loop scope, `chi_shock`/`H_*`,
  Ω_freeze IC arm); R1 α forward check scheduled in parallel
- **Platform:** diamond engine + srs **instrument** controls; σ-equipped medium + loop kernel
  + **three-channel readout** + explicit Ω_freeze initial data (not ferrite remanence)
- **R2 draft:** `research/2026-06-12_constitutive-loop-r2-prereg_DRAFT.md` (§0b three-wave gaps)

---

## Skill matrix (reviewed 2026-06-11)

Skills apply at the lifecycle moment listed. **Implementor must read the full SKILL.md** before acting.

### Tier 1 — Mandatory before any new work on this epic

| Skill | Fires when | Load-bearing checkpoint |
|-------|------------|-------------------------|
| **ave-prereg** | R3 prereg, Phase-1 freeze edit, D1 memo | Corpus-grep before derive; Step 1.5 physical picture |
| **pre-test-physics-check** | Before freezing thresholds; before dispatching implementor | Plumber question: structural vs excited chirality? |
| **substrate-native-check** | R3 driver, Phase-1 vector-TLM, any genesis integrator | CP1 scatter+connect not Lagrangian; CP8 seed precursor not composite; CP9 dynamic not heuristic |
| **consistency-vs-emergence** | Every observable in prereg + result doc | Tag O1=replication; O2 Arm1@κ=0=emergence candidate; Arm3@κ≠0=consistency |
| **phase-space-coordinate-check** | O2/O3 Δθ/L, P2/P3 Phase-1 | Chirality coord ≠ lattice-Cartesian; no fake V_inc projection |
| **ave-canonical-source** | All new Python | `KAPPA_CHIRAL_ELECTRON`, `ALPHA`, `L_NODE`, `Z_0` from `constants.py` |

### Tier 2 — Mandatory at result write / promotion

| Skill | Fires when | Load-bearing checkpoint |
|-------|------------|-------------------------|
| **ave-discrimination-check** | Before "D1 resolved" / "substrate proven" language | SM-counterfactual per observable; no aggregate promotion |
| **ave-multi-falsifier-triangulation** | D1 bin assignment from R3+Phase-1 | Arm3 κ channel alone cannot confirm D1-A; pair with Arm1 κ=0 |
| **ave-evidence-framing-discipline** | Adjudication memo, index update | No "~PASS" without numbers; denominator = all arms |
| **ave-driver-script-honesty** | R3 driver + Phase-1 drivers | Four discriminators; no fit-as-prediction on Δθ/L |
| **verify-before-cite** | Any file:line / Phase-0 quote in memo | Re-grep baselines before cite |

### Tier 3 — Mandatory at Phase-1 genesis / v10 charter

| Skill | Fires when | Load-bearing checkpoint |
|-------|------------|-------------------------|
| **ave-fundamental-ground-up-implementation** | Locking ⟨thresholds⟩ | Prefer Phase-0 floors over engineering defaults |
| **ave-apparatus-floor-attribution** | If κ or grid knobs swept | Tag engineering choices vs substrate-derived |
| **regime-phase-state-check** | Op14 ON in P6 | Saturation regime matches prereg |
| **ave-regime-phase-state-check** | P6 precursor run | Linear vs saturated bins separated |

### Tier 4 — At D1 memo / corpus propagation only

| Skill | Fires when | Load-bearing checkpoint |
|-------|------------|-------------------------|
| **ave-walk-back** | After Grant greenlights D1 bin | `eq_axiom_1.tex`, lattice resolution, electron definitive model |
| **ave-handoff-canonical-locale** | All orchestration edits | `_orchestration/`, not `~/.claude/plans/` |
| **ave-ip-divide-discipline** | Before any push | Public corpus only |

### Tier 5 — Parallel tracks (not R3 blockers, same session awareness)

| Skill | When |
|-------|------|
| **ave-conserved-vs-pumped** | Phase-1 P6 if drive-off persistence tested |
| **ave-dimensional-provenance-check** | If λ_G redo on srs unit cell queued post-D1 |
| **ave-independence-check** | If multi-instance "three nets" listed as independent evidence |

### Explicitly NOT required for R3 Phase-0 extension

- `ave-audit` / `ave-sweep-audit` — unless result triggers walk-back
- `ave-prereg` corpus-grep for α/Lorentz chains — deferred to post-D1 re-derivation queue
- Bugbot / security-review — no merge without PR review per workflow

---

## Dependency graph

```
Phase-0 (main) ──► R3 prereg freeze ──► R3 implementor ──► D1 partial bins
                                                      │
Phase-1 prereg freeze (thresholds) ◄──────────────────┘
         │
         ▼
   Phase-1 P1-P6 ──► D1 full adjudication ──► v10 spine + corpus walk-back
```

**Parallel (non-blocking):** R2 constitutive-loop prereg, a3 α-reservoir resume.

---

## Open decisions (test-gated — not Grant picks)

| ID | Was | Now |
|----|-----|-----|
| D1 | Pick framing A or B | **Ruled: B-primary / A-partial** (`research/2026-06-12_lattice-d1-adjudication-memo.md`) |
| D3 | v9 freeze | Freeze **thresholds** after R3; genesis after |
| v10 spine | Pre-pick srs | **After** D1 memo |

---

## Implementor spawn brief (Phase 1 — R3)

**Read first:** this epic §Skill matrix Tier 1; `research/2026-06-11_lattice-decoration-discriminator_prereg.md`; `research/2026-06-11_genesis-v9-chiral-lattice_design.md` §3.

**Branch:** `analysis/2026-06-12-lattice-decoration-discriminator` off `main`.

**Deliverables:**
1. Driver + pytest keeper per prereg §9
2. Result doc `research/2026-06-11_lattice-decoration-discriminator_result.md` with D1 bin assignment
3. No index/orchestration edits on implementor branch (orchestration PR separate)

**Do not:** freeze Phase-1 prereg; write D1 ruling in axiom text; merge to main.

---

## Cross-refs

- v9 design: `research/2026-06-11_genesis-v9-chiral-lattice_design.md`
- v9 Phase-1 FROZEN: `research/2026-06-11_genesis-v9-phase1-prereg_FROZEN.md`
- v9 Phase-2 FROZEN: `research/2026-06-12_genesis-v9-phase2-prereg_FROZEN.md`
- CVR framing: `research/2026-06-11_chiral-vacuum-reactor-framing.md`
- Branch plan: `_orchestration/2026-06-11_orchestration-branch-plan.md` (R3 row — **update after this epic merges**)
