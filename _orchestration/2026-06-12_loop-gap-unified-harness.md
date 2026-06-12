# Epic — LOOP GAP unified harness (K4 platform pivot)

**Status:** ACTIVE  
**Opened:** 2026-06-12  
**Branch:** `analysis/2026-06-12-genesis-v10-cvr-implementor` (pending PR)  
**DAG:** [`2026-06-12_loop-gap-engine-dag.md`](2026-06-12_loop-gap-engine-dag.md)  
**Ledger:** [`research/2026-06-12_genesis-program-status.md`](../research/2026-06-12_genesis-program-status.md)

---

## Pivot summary (Grant-approved 2026-06-12)

1. **Freeze** discrete srs genesis at **v17** (falsifiers archived).  
2. **One harness** — `loop_gap_harness.py` on `VacuumEngine3D` + rank profiles.  
3. **Engine DAG** — capability prerequisites + observables per rank (orchestration doc above).  
4. **Stop version treadmill** — advance LOOP GAP **ranks**, not `v19`, `v20`, …

`genesis_v18_coupled.py` is **superseded** by the harness (kept as reference until Phase 2 migration complete).

---

## Phase 1 — Scaffold + DAG (COMPLETE 2026-06-12)

| Deliverable | Path | Status |
|:---|:---|:---|
| Engine capability DAG | `_orchestration/2026-06-12_loop-gap-engine-dag.md` | ✅ |
| Unified harness module | `src/ave/core/loop_gap_harness.py` | ✅ |
| Driver | `src/scripts/vol_1_foundations/loop_gap_harness_genesis.py` | ✅ |
| Smoke tests | `src/tests/test_loop_gap_harness.py` | ✅ |
| Meta skill | `~/.claude/skills/ave-loop-gap-harness-discipline/SKILL.md` | ✅ |
| Program ledger pivot § | `research/2026-06-12_genesis-program-status.md` §9 | ✅ |
| Doctrine srs freeze | `loop-gap-electron-resonator-closure-doctrine.md` §6 | ✅ |

---

## Phase 2 — Γ engagement + genesis-23 seed replay (IN PROGRESS 2026-06-12)

**Goal:** Rank 1 Γ gate PASS (`gamma_min ≤ -0.25`) on harness.

**Hypothesis:** Uniform pair seed at `√α` lacks ∇A₀; genesis-23 `photon_lock` + `graded_a0` engage asymmetric yield surface.

**Tasks:**
- [x] `loop_gap_seeds.py` — `pair` | `photon_lock` | `graded_a0`
- [x] `phi_growth` baseline = post-first-step `Φ_link` (not IC zero)
- [x] Battery: seed ablation + `A_LOCK ∈ {1.5, 3.0, 6.0}` sweep (production)
- [ ] Production smoke/production run + `loop_gap_harness_phase2_result.md`
- [ ] Rank-1 Γ PASS or ENGINE-GAP with ablation attribution

**Acceptance:** `rank1_pass` with `gamma_min ≤ -0.25` on primary arm OR documented ENGINE-GAP.

---

## Phase 2b — Bulk channel port (Rank 1b, PENDING)

**Goal:** Three-channel fidelity on the active harness — dynamical $\bar\rho$ sector (GAP-A) without conflating EM / shear / bulk reads.

**Prereg (DRAFT):** [`research/2026-06-12_loop-gap-harness-bulk-channel_prereg_DRAFT.md`](../research/2026-06-12_loop-gap-harness-bulk-channel_prereg_DRAFT.md)

**Corpus rule:** Port `UnifiedGenesisEngine.bulk_density_on` into `VacuumEngine3D` (KEEP-BOTH default OFF). **Do not** open snap/GAP-C in this phase.

**Increments:**
| Inc | Deliverable | Status |
|:---|:---|:---|
| A | GAP-A port + F0 byte-identical regression | [ ] |
| B | Channel-tagged `LoopGapResult` + bulk ablation arms | [ ] |
| C | GAP-C / snap — **out of scope** (separate prereg) | — |

**Tasks:**
- [ ] `EngineConfig.bulk_density_on` on `VacuumEngine3D`
- [ ] Harness `--bulk` flag; bulk fields in battery JSON
- [ ] `test_loop_gap_harness_bulk_channel.py` (F0 + F1 smoke)
- [ ] Result doc §production table

**Acceptance:** F0 PASS; F1 bulk_ON ≠ bulk_OFF at $t_{\mathrm{end}}$ without detonation; rank-1 JSON carries channel tags when bulk enabled.

---

## Phase 3 — P11 remanence at rank 4 (PENDING)

**Goal:** P11 PASS on pinned quiescence (lesson from v17: no comoving during quiet).

**Tasks:**
- [ ] `n_quiet` at fixed lattice origin (no translate during quiet)
- [ ] Memristive ablation must change `S_persist_delta` on production step budget
- [ ] Optional: wire `ObservableBattery` channels 3/4/6 on drive-off + end steps

**Acceptance:** `REMANENCE-LANDED` or honest `OPERATOR-SET-ONLY` with R2 bench cross-ref queued.

---

## Carry-forward from srs freeze

| srs finding | Harness implication |
|:---|:---|
| v10 CVR-SET | Not mass — do not reuse as P11 |
| v14b P12 gain fail | Transport gate deferred until R5 boost-covariant |
| v16/v17 P11 fail | Quiescence protocol + K4 observables |
| v15b V_INC-LANDED | Rank 1 partial — converter path validated |
| v18 smoke PARTIAL | Γ + metric fixes → Phase 2 |
