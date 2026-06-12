# LOOP GAP — Orchestration plan (pedantic, 2026-06-12)

**Status:** ACTIVE — authoritative execution sequence for the K4 harness pivot  
**Supersedes for execution order:** `_orchestration/index.md` §2026-06-11 Grant decision stack (D1/D2 rows — see §2 below)  
**Physics anchor:** `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md`  
**Program ledger:** `research/2026-06-12_genesis-program-status.md`  
**Harness epic:** `_orchestration/2026-06-12_loop-gap-unified-harness.md`  
**Capability DAG:** `_orchestration/2026-06-12_loop-gap-engine-dag.md`

**Working branch (implementor):** `analysis/2026-06-12-genesis-v10-cvr-implementor`  
**Integration target:** `main` via reviewed PR only (2026-06-05 workflow)

---

## §0 — One-sentence objective

Close the **LOOP GAP** by advancing **ranks 1→4** on the unified K4 harness (`VacuumEngine3D` + `loop_gap_harness.py`), with **channel-tagged** observables at **valid regime** (`A²` near yield cusp), while **R2 ferrite B–H bench** runs in parallel for rank-4 ground truth — **not** by adding srs genesis versions or agent-adjudicated framing closures.

---

## §1 — First-principles invariants (every phase)

| ID | Invariant | Violation = stop |
|:---|:---|:---|
| I1 | **Mass = zero-drive persistence** (`P11`, `t ≫ τ_relax`, drive OFF) | Promoting CVR-SET, `e_driveoff`, or snap ledger as mass |
| I2 | **Three channels** — tag every read: `EM` / `shear` / `bulk` / `proxy` | `gamma_min` (Op14 μ-short) promoted as `Γ_bulk` |
| I3 | **Regime** — production bins at yield cusp: `A²_yield = 2α` target band; quarantine `A² ≫ 1` | Using post-rupture P5/P6/v10 bins for substrate/framing adjudication |
| I4 | **Coordinate** — `(2,3)` phase-space; launch = ±**k** along screw axis | Global field sign-flip as "reversed direction" |
| I5 | **Engine substrate** — production on **z=4 diamond K4**; srs = **instrument** | srs migration on regime-invalid genesis alone |
| I6 | **Grant-reserved** — framing, snap scope, IC canon: **strike-and-date** if changed; no silent delete | Walk-back removing "Grant picks" language without dated strike |
| I7 | **PR gate** — orchestration + corpus land on branch + reviewed PR | Direct push to `main` |

---

## §2 — Decision stack reconciliation (2026-06-12 audit + first principles)

Session-record vs physics-truth. **Do not block harness work on D1 re-litigation**; **do** quarantine over-closed rows.

| ID | 2026-06-11 index row | 2026-06-12 physics read | Plan action |
|:---|:---|:---|:---|
| **D1 structural** | (buried in R3) | **LANDED** — R3 D1-A: decoration ρ ≈ 0.057% of srs Bishop | Keep; cite `research/2026-06-11_lattice-decoration-discriminator_result.md` |
| **D1 framing** | ✅ B-primary / A-partial | **OVER-CLOSED** — structural srs real; migration not demonstrated; P5/P6 at invalid regime | **REOPEN** — relabel memo §2.3; strike "FINAL" → "SESSION-RECORD pending Grant confirm" |
| **D2 snap** | ✅ σ + rate-gated snap | **TESTED, NOT LOAD-BEARING** — v10: snap-OFF still CVR-SET; ablations match ON | **DOWNGRADE** to optional dissipator; σ-only default for harness rank ≤3 |
| **D3 freeze** | ✅ FROZEN | Keep v9/v10 preregs frozen | No re-freeze |
| **D4 χ** | ✅ equal χ + H_* ON | Keep for srs archive; **not** on K4 harness until prereg | Out of harness Phase 2b |
| **D5 Ω_freeze** | ✅ IC ON | **NOT remanence** — v10 ablation falsifies | IC = ablation arm only on harness |
| **Pivot** | (not in index) | **LANDED** — freeze srs v17; one harness | Index §2026-06-12 reconciliation |

**Grant confirm queue (non-blocking for Phases A–C):** Did you voice D1-B framing, D2 snap, D5 IC? Record yes/no in orchestration PR body; physics plan proceeds regardless.

---

## §3 — Regime-invalid bin quarantine

These artifacts **remain in corpus** (Rule 12); they **must not** adjudicate framing or migration.

| Artifact | Regime fault | Quarantine rule |
|:---|:---|:---|
| `research/2026-06-12_genesis-v9-phase2_result.md` | `max(A²) ≈ 13–14` srs, `≈ 38` diamond | P5/P6 bins → **ENGINE-CLASS / POST-RUPTURE** only |
| `research/2026-06-12_genesis-v10-cvr-convergence_result.md` | `max(A²) ≈ 15–22` | CVR-SET → **reactive under drive** only; snap → **not bin-isolating** |
| `research/2026-06-12_lattice-d1-adjudication-memo.md` §2.3 | Used P5-fail from quarantined runs | Reframe §2.3; add quarantine header |

**Regime gate for all future production:**

```text
PRE-RUN:  assert amp / A_LOCK maps to A²_target ∈ [0.5·2α, 2·2α] at drive peak (log actual max_A²)
POST-RUN: if max_A² > 10 · A²_yield → bin suffix _POST_RUPTURE; exclude from D1/framing tables
```

---

## §4 — Execution phases (strict order)

### Phase A — Orchestration ledger (THIS PHASE)

| Step | Task | Acceptance | Owner |
|:---|:---|:---|:---|
| A1 | This plan doc on branch | File exists; index points here | orchestration |
| A2 | Index §2026-06-12 reconciliation | Supersedes stale decision closure for execution | orchestration |
| A3 | Harness epic cross-link | `_orchestration/2026-06-12_loop-gap-unified-harness.md` §Plan | orchestration |
| A4 | Program status §10 pointer | `research/2026-06-12_genesis-program-status.md` | orchestration |

**PR:** orchestration-only; Grant reviews before merge.

---

### Phase B — Phase 2b land (GAP-A bulk channel)

**Prereg:** `research/2026-06-12_loop-gap-harness-bulk-channel_prereg_DRAFT.md`  
**Out of scope:** GAP-C snap, `dω/dt → ρ̄` injection, proxy-only rank-1 PASS

| Step | Task | Acceptance |
|:---|:---|:---|
| B0 | **c0 natural units** | `BulkRarefactionConfig.c0 = ENGINE_C0 (1.0)` — not SI `C_0` (CFL substep runaway) |
| B1 | Fast unit tests | `pytest` on: `test_bulk_sector_rk2_evolve`, `test_vacuum_engine_bulk_*`, `test_c_bulk2_eos_at_probe`, `test_bulk_circulation_ic_rarefies`, `test_rank_profiles_cumulative` — all green |
| B2 | Coupled probe tests (bounded) | `test_f0_*`, `test_f1_*`, `test_f2_*` with `fast=True`, `N=10` — green or documented ENGINE-GAP with timeout cap 120s per test |
| B3 | Smoke battery | `./.venv/bin/python src/scripts/vol_1_foundations/loop_gap_harness_genesis.py --smoke --bulk` → JSON + stdout `bulk_F1`, `bulk_F2` |
| B4 | Result doc §2b | `research/2026-06-12_loop-gap-harness-phase2_result.md` §Phase 2b table filled |
| B5 | Epic Phase 2b checkboxes | Harness epic tasks complete except PR |
| B6 | Commit split | **Commit 1:** Phase 2b harness only (`bulk_rarefaction_sector.py`, `vacuum_engine.py` bulk hook, `loop_gap_harness.py`, driver, tests, prereg if amended, result §2b, epic). **Not** genesis v11–v17 / vol9 KB sprawl in same commit |
| B7 | `make verify` | Green before PR |
| B8 | PR + audit tag | `audit/2026-06-12_loop-gap-harness-phase2b` on branch tip before delete |

**Rank 1b acceptance:** `rank1b_pass` from `ρ̄_min` or `c_bulk²` drop; **`rank1_pass` proxy FAIL is not bulk PASS**.

---

### Phase C — Corpus discipline pass (D1 reframe + quarantine)

| Step | Task | Acceptance |
|:---|:---|:---|
| C1 | D1 adjudication memo header | Add quarantine + "SESSION-RECORD" framing; §2.3 not "FINAL" without Grant confirm |
| C2 | `2026-06-11_lattice-d1-test-gated.md` | Open decisions table: D1 → **STRUCTURAL-LANDED / FRAMING-OPEN** |
| C3 | Quarantine banners on v9/v10 result docs | `_POST_RUPTURE` / regime fault explicit at §P6 |
| C4 | Bulk leaf channel note | `bulk-impedance-at-saturation-boundary.md` — FLAG: tensile cavitation vs compressive melt; electron constructive interior ≠ BH melt (no equation change; discipline block only) |
| C5 | Restore struck decision-trail | If git history shows deleted "Grant picks" lines → Rule 12 strike-and-date block in plan or handoff |

**PR:** corpus/orchestration; separate from B if B is already in flight.

---

### Phase D — Regime-gated rank-1 charter (harness Phase 2 completion)

**Goal:** Rank 1 proxy `gamma_min ≤ -0.25` **or** honest ENGINE-GAP with ablation attribution — at **valid regime**.

| Step | Task | Acceptance |
|:---|:---|:---|
| D1 | Prereg amend / charter | `research/2026-06-12_loop-gap-harness-rank1-regime_prereg_DRAFT.md` — `A_LOCK` sweep bounded to yield band; log `max_A_sq` every run |
| D2 | Seed ablation battery | `photon_lock` vs `graded_a0` vs `pair` — production or `--smoke` with regime gate |
| D3 | `gamma_bulk_min` observable (new) | `Γ_bulk = (Z_bulk - Z_ref)/(Z_bulk + Z_ref)` from live `ρ̄`, `c_bulk`; channel tag `bulk` not `proxy` |
| D4 | Rank-1 bin | `rank1_pass` OR `ENGINE-GAP` doc with which ablation isolates |
| D5 | Phase 2 epic close | Harness epic Phase 2 tasks checked |

**Do not:** N=14 full production without regime gate and `--bulk` channel tags.

---

### Phase E — Seed geometry fix (srs + harness seeds)

| Step | Task | Acceptance |
|:---|:---|:---|
| E1 | True ±k launch | Replace `packet *= -1` proxy with propagation-axis reversal in `launch_linear_packet` / harness seeds |
| E2 | Keeper test | Reversed k flips acquired rotation sign; global sign-flip does not |
| E3 | Re-run R3 Phase-1 P4 cell if magnitudes shift | Document delta; do not auto-reopen D1 |

**Gated on:** Phase D charter merged or parallel if seed module owned separately.

---

### Phase F — Rank 2–3 harness (Compton + lock)

| Rank | Work | Gate |
|:---|:---|:---|
| **2** | `n_drive_mult` sweep in units of `τ_relax`; Compton carrier | `phi_growth` or `ρ_cross` per DAG; matched-baseline 2× |
| **3** | GAP-1 trilinear on harness; genesis-23 replay metrics | `v_inc_peak > floor`; no pump; `cross_sector_gap1_closure.py` parity |

**Prereq:** Phase D rank-1 ENGINE-GAP or PARTIAL documented.

---

### Phase G — Rank 4 + R2 bench (remanence crux)

| Track | Work | Gate |
|:---|:---|:---|
| **G1 Harness** | Phase 3: pinned quiescence (`n_quiet` no translate); memristive ablation changes `S_persist_delta` | P11 or `OPERATOR-SET-ONLY` honest |
| **G2 R2 bench** | Execute `research/2026-06-12_constitutive-loop-r2-prereg_FROZEN.md` ferrite B–H protocol | Enclosed loop area measured |
| **G3 GAP-C** | Separate prereg — ω↔ρ̄ coupling, snap on bulk branch | **Not** until G1+G2 read |

---

## §5 — Deferred (explicit do-not-do)

| Item | Reason |
|:---|:---|
| New `chiral_lattice_v18+` / `genesis_v19+` | srs FROZEN; harness ranks replace version treadmill |
| srs substrate migration | No valid-regime hosting/genesis; α/Lorentz on diamond |
| Proxy-only N=14 production harness | ENGINE-GAP known; waste without bulk + regime gate |
| D1 re-adjudication from quarantined bins | Regime-invalid |
| GAP-C / snap on harness Phase 2b | Prereg scope exclusion |
| R5 boost-covariant transport | Expensive; blocks v12/v14 class only; parallel fund plan |
| Proton body scale | Epic §45–47; does not unblock electron ranks |

---

## §6 — Active epic table (2026-06-12)

| Epic | Doc | Status | Next step |
|:---|:---|:---|:---|
| **LOOP GAP harness** | `2026-06-12_loop-gap-unified-harness.md` | ACTIVE Phase 2/2b | **Phase B** after A |
| Electron synthesis | `2026-06-07_electron-synthesis-epic.md` | ACTIVE — record landed | Rank closure via harness, not new genesis |
| Lattice D1 | `2026-06-11_lattice-d1-test-gated.md` | STRUCTURAL done; framing open | Phase C |
| Constitutive loop R2 | `research/2026-06-12_constitutive-loop-r2-prereg_FROZEN.md` | FROZEN | Phase G2 parallel |
| Experimental arc | `experimental/experimental-arc.md` | ACTIVE survivors | Unchanged |

---

## §7 — Skill matrix (mandatory per phase)

| Phase | Skills |
|:---|:---|
| A, C | `ave-handoff-canonical-locale`, `verify-before-cite`, `ave-walk-back` (Rule 12) |
| B, D, F, G1 | `substrate-native-check`, `phase-space-coordinate-check`, `consistency-vs-emergence`, `ave-driver-script-honesty`, `ave-regime-phase-state-check` |
| B, D | `ave-multi-falsifier-triangulation-discipline` (channel tags) |
| D, G1 | `pre-test-physics-check`, `ave-dimensional-provenance-check` (Γ_bulk) |
| G2 | `ave-engineering-program-rigor` |
| All commits | `ave-ip-divide-discipline` (public repo) |

---

## §8 — Branch / commit discipline

```bash
# Before every orchestration commit:
git branch --show-current   # must match intended branch

# Implementor isolation: prefer worktree for subagents (see _orchestration/README.md)
```

| Commit slice | Paths (typical) |
|:---|:---|
| **2b-harness** | `src/ave/core/bulk_rarefaction_sector.py`, `vacuum_engine.py`, `loop_gap_harness.py`, `loop_gap_seeds.py`, driver, `test_loop_gap_harness_bulk_channel.py`, harness epic, result §2b |
| **orch-plan** | `_orchestration/2026-06-12_loop-gap-orchestration-plan.md`, `index.md` reconciliation, D1/quarantine docs |
| **rank1-charter** | prereg DRAFT, `gamma_bulk` read, harness Phase 2 close |

---

## §9 — Verification commands (copy-paste)

```bash
# Phase B — fast
./.venv/bin/pytest \
  src/tests/test_loop_gap_harness_bulk_channel.py::test_bulk_sector_rk2_evolve \
  src/tests/test_loop_gap_harness_bulk_channel.py::test_vacuum_engine_bulk_off_no_sector \
  src/tests/test_loop_gap_harness_bulk_channel.py::test_vacuum_engine_bulk_on_steps \
  src/tests/test_loop_gap_harness_bulk_channel.py::test_c_bulk2_eos_at_probe \
  src/tests/test_loop_gap_harness_bulk_channel.py::test_bulk_circulation_ic_rarefies \
  src/tests/test_loop_gap_harness.py::test_rank_profiles_cumulative \
  -q

# Phase B — coupled (may be slow; cap wall clock)
./.venv/bin/pytest src/tests/test_loop_gap_harness_bulk_channel.py -q -k "f0 or f1 or f2"

# Phase B — smoke
./.venv/bin/python src/scripts/vol_1_foundations/loop_gap_harness_genesis.py --smoke --bulk

# Pre-PR
make verify
```

---

## §10 — Success criteria (program level)

| Milestone | Criterion |
|:---|:---|
| **M1** | Phase 2b merged; F0/F1/F2 documented |
| **M2** | D1 framing reopened; quarantine banners live |
| **M3** | Rank-1 charter at valid regime; `gamma_bulk` instrumented |
| **M4** | ±k seed fix landed |
| **M5** | P11 attempted on harness rank 4 + R2 bench executed |
| **M6** | `REMANENCE-LANDED` or honest `OPERATOR-SET-ONLY` with R2 cross-ref |

---

## §11 — Change log

| Date | Change |
|:---|:---|
| 2026-06-12 | Initial pedantic plan — post audit synthesis + harness pivot |
