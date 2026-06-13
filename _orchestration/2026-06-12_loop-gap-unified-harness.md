# Epic — LOOP GAP unified harness (K4 platform pivot)

**Status:** ACTIVE  
**Opened:** 2026-06-12  
**Harness land:** PR **#207** merged → `main` @ `98ec9270` (2026-06-12)  
**Next work:** D-lite (`analysis/2026-06-12-loop-gap-phase-d`) → C′ scalar restoration (`analysis/2026-06-13-loop-gap-scalar-grade`)  
**DAG:** [`2026-06-12_loop-gap-engine-dag.md`](2026-06-12_loop-gap-engine-dag.md)  
**Ledger:** [`research/2026-06-12_genesis-program-status.md`](../research/2026-06-12_genesis-program-status.md)  
**Execution plan (authoritative order):** [`2026-06-12_loop-gap-orchestration-plan.md`](2026-06-12_loop-gap-orchestration-plan.md)  
**Session handoff (spawn other agent):** [`2026-06-12_loop-gap-orchestration-session-handoff.md`](2026-06-12_loop-gap-orchestration-session-handoff.md)  
**Full plan + implementor brief:** [`2026-06-12_loop-gap-first-principles-implementor-brief.md`](2026-06-12_loop-gap-first-principles-implementor-brief.md) (Part I = orchestrator; Part II = implementor)  
**Coverage ledger:** [`2026-06-13_loop-gap-corpus-engine-coverage.md`](2026-06-13_loop-gap-corpus-engine-coverage.md) — belief tiers T0–T4; keeper backlog §6

---

## Session log (2026-06-12 — updated post-#207)

| Item | Read |
|:---|:---|
| Harness + Phase 2b | **LANDED** — PR #207 → `main` @ `98ec9270` |
| Audit tag | ✅ `audit/2026-06-12_loop-gap-harness-phase2b` on `98ec9270` → origin |
| Smoke `--bulk` | **ENGINE-GAP** on $V_{\mathrm{inc}}$ — motivates **Phase C′** scalar restoration |
| Uncommitted | ~70 paths on old branch — **PR2** handoff / **PR1** vol9 / **Phase C** / **PR4** archive |
| Blocker B1 | `common/index.md:59` — fixed in PR2 orchestration pass |
| P11 constants | `genesis_v18_coupled.py` on main (`chiral_lattice_v11` removed at merge) |

---

## Plan map (phases A→G — detail in orchestration plan)

| Phase | Scope | Harness epic slice |
|:---|:---|:---|
| **A** | Orchestration ledger | This doc + index reconciliation |
| **B** | Phase 2b GAP-A land | §Phase 2b below |
| **C** | D1 reframe + regime quarantine | Corpus only — **LANDED** #210 |
| **D-lite** | OP-2 instrument + smoke baseline | §Phase 2 — `gamma_bulk_min` |
| **C′** | Scalar-grade restoration | Standing $V$ + $V\to\omega$ source |
| **D-full** | Rational seed sweep (post-C′) | §Phase 2 completion |
| **E** | ±k seed fix | `loop_gap_seeds.py` / vector launch |
| **F** | Ranks 2–3 Compton + GAP-1 | Post–D-full |
| **G** | Rank 4 P11 + R2 bench | §Phase 3 |

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

## Phase 2b — Bulk channel port (Rank 1b, LANDED 2026-06-12)

**Goal:** Three-channel fidelity on the active harness — dynamical $\bar\rho$ sector (GAP-A) without conflating EM / shear / bulk reads.

**Prereg (DRAFT):** [`research/2026-06-12_loop-gap-harness-bulk-channel_prereg_DRAFT.md`](../research/2026-06-12_loop-gap-harness-bulk-channel_prereg_DRAFT.md)

**Corpus rule:** Port `UnifiedGenesisEngine.bulk_density_on` into `VacuumEngine3D` (KEEP-BOTH default OFF). **Do not** open snap/GAP-C in this phase. Motor seed = `energize_rotation_column` (OP-3), not `dω/dt` injection.

**Increments:**
| Inc | Deliverable | Status |
|:---|:---|:---|
| A | GAP-A port + F0 byte-identical regression | [x] |
| B | Channel-tagged `LoopGapResult` + `rank1b_pass` + bulk ablation arms | [x] |
| B+ | `bulk_circulation` motor arm (GAP-D seed) | [x] |
| C | GAP-C / snap — **out of scope** (separate prereg) | — |

**Tasks:**
- [x] `EngineConfig.bulk_density_on` on `VacuumEngine3D`
- [x] `bulk_rarefaction_sector.py` + circulation IC
- [x] Harness `--bulk` flag; bulk fields in battery JSON
- [x] `test_loop_gap_harness_bulk_channel.py` (F0/F1/F2)
- [x] `--smoke --bulk` battery + result doc §2b table
- [x] B0 `c0` natural-units fix + `bulk_f1` dict bugfix
- [x] pytest F0–F2 green (9 tests)
- [x] PR #207 merged (2026-06-12)
- [ ] Audit tag `audit/2026-06-12_loop-gap-harness-phase2b` on `98ec9270` + push origin

**Phase A (ledger):** [x] orchestration plan doc; [x] index §2026-06-12; [x] program status §10

**Acceptance:** F0 PASS; F1 bulk_ON ≠ bulk_OFF; F2 channel-tagged — **LANDED on main**. Rank-1 $\Gamma$ gate remains **open** (Phase 2 / Phase D).

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

---

## 2026-06-13 addendum — engine capability map + the C′ platform decision

**The C′ scalar-grade diagnosis closed a deeper question than the seed bug.** This harness (`VacuumEngine3D`) **cannot host the A1 stiffening cage** — its scalar is a `v_scalar_from_v_inc(V_inc)` projection (softening-bulk only; `k4_cosserat_coupling.py:503`), so the cage's engine-confirmed home is the longitudinal-bulk engine (`crystal_engine.py` / `master_equation_fdtd.py`). The full engine×DOF picture — the 7 DOF, the three canon-derived firewalls, and the substrate-complete-engine **design proposal** — is now a tracked KB artifact: [`engine-capability-map.md`](../manuscript/ave-kb/common/engine-capability-map.md) + a living-tracker figure.

**Platform decision (Option A — PENDING Grant ratification; block in [`index.md`](index.md) §2026-06-13 addendum).** The C′ cage test runs on `crystal_engine` / `master_equation_fdtd`, **not** this harness; `ave-loop-gap-harness-discipline` needs amending to *"one platform per firewalled branch"* (out-of-band, user-level skill). Until ratified, Phase C′-on-the-harness is **HELD**. The harness continues to own the doctrine §2 ranks (softening-bulk + Cosserat + transport); the stiffening cage is a separate firewalled branch.
