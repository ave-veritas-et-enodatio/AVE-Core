# PREREG — CI engine-sim partition: route the slow tier-1/2 engine tests out of the default keeper gate

**Status:** FROZEN prereg (no code moved yet — partition list for review)
**Opened:** 2026-06-13
**Branch:** `analysis/2026-06-13-ci-engine-sim-partition` (off `main` @ `efb15e3f`)
**Parent ledger:** [`_orchestration/2026-06-13_loop-gap-corpus-engine-coverage.md`](../_orchestration/2026-06-13_loop-gap-corpus-engine-coverage.md) (the T0–T4 tier taxonomy + §0 declared CI scope this prereg *implements*)
**Sibling infra:** PR #218 (worktree-aware local gates, merged `efb15e3f`); the capability matrix (`engine_capability_matrix.yaml`, PR #216) — used here as **justification context only**.

---

## §1 — Problem & prior art

`make test` is **26 min in CI** (green-main baseline `27473550560`: 17:16:07→17:42:22), ~8.5 min local; the 30-min CI timeout leaves only ~4 min of margin. `make verify` is 41 s — the entire cost is the pytest suite. A `--durations` run (local, 2026-06-13; CI ≈ 3.1× local) shows the cost is concentrated in a handful of **engine-simulation** tests added in the last 1–3 days (`loop_gap_harness*` 06-11/12, `unified_*` 06-10), vs. settled keepers from 04-13.

**This is an already-declared scope the conftest under-enforces, not a new policy.** The parent ledger §0 states:
- `make test` (~1480) = **"Bedrock rows only"**
- harness = a **separate** suite (`pytest src/tests/test_loop_gap_harness*.py`)
- genesis = **opt-in** (`make test-genesis`)

…and §7 names the exact failure: *"Anti-pattern: claiming KEEPER because `make test` is green — default suite does not assert CVG-R1-003 or CVG-R4-001."* But `src/tests/conftest.py` only excludes `chiral_lattice_v*` / `test_genesis_*` (the latter glob matches **zero** files), so the T1 harness wiring + slow batteries leak into the keeper gate. Precedent for the fix: conftest commit `78605bb8` *"Exclude genesis drivers from default CI."*

## §2 — The rule (oracle = test-role tier + cost; NOT physics-confirmation)

A test gates the default `make test` suite **iff** it is a **T0 KEEPER** (asserts an outcome / definitional identity) **and** is **fast + deterministic**. Everything else routes to an opt-in lane.

- **Trigger axis = test-engineering only:** (a) cost (local call/setup ≥ ~2 s ⇒ route-or-shrink candidate); (b) role-tier (T1 WIRING / T2 DRIVER ⇒ out by nature — they assert nothing / are drivers). Stability is **not** a discriminator here: the heavy files are seeded/RNG-free (zero unseeded draws), i.e. deterministic-but-expensive.
- **The engine capability matrix is NOT in the selection path.** It appears only as a per-row *justification column* ("…and per the matrix this verifies a `partial`/`absent` cell [anchor]"). **Invariant:** re-grading a capability cell tomorrow must flip **zero** markers and change **zero** CI coverage.
- **Why tier-coupling is safe but matrix-coupling corrupts:** couple CI to the physics matrix and the incentive is to misgrade *physics* (mark `have` to win coverage) — corrupting the honesty artifact. Couple CI to the *tier* and the only promotion path is the ledger's own rule — *"WIRING→KEEPER: add a pytest that asserts the floor/ceiling"* — so the incentive is to **write a real assertion**. One bends physics; the other improves the test.

## §2a — Rulings (Grant + auditor, 2026-06-13) — FROZEN

1. **Tier beats blanket §0 — *after* confirming the tag.** "Harness = separate suite" was §0 shorthand from when the harness was all-wiring; real T0 keepers there stay gating. But the tier oracle is only as good as the tag, so each disputed tag was re-read against its assertions (below). Keep genuine T0; opt-in wiring-mistagged.
2. **`transition_metals`: shrink-to-FIXED-sample.** Stable canon (not actively developed) + the `IE<100 eV` bound is resolution-independent ⇒ sampling elements (not coarsening) is safe. Fixed, range-covering subset gates; full sweep in the engine lane.
3. **`electron_tlm` golden-torus: OPT-IN at full resolution, never shrink.** A convergence/eigensolve assertion is resolution-DEPENDENT — coarsening tests a different regime and could pass a margin check by luck.

**Verified CVG-R1B tags (re-read 2026-06-13, `test_loop_gap_harness_bulk_channel.py`):**
- **002 `test_f0`** — `rho_bar_min_end==0.0` & `c_bulk2_min_end==0.0` (bulk-OFF ⇒ exact zero) + `v_inc_peak>=0`: genuine **T0**, step-independent → **SHRINK**, keep gating.
- **003 `test_f1`** — `on.rho_bar_min_end < off.rho_bar_min_end` + channel-primary membership: borderline-wiring "sector is live," 2× cost, **redundant** with the fast direct rarefaction keepers (`test_bulk_sector_rk2_evolve`, `test_bulk_circulation_ic_rarefies`, which stay gating) → **OPT-IN**.
- **004 `test_f2`** — only `"EM"/"bulk"/"proxy" in channel_tags` + `rank1b_pass` flag: the literal **T1** definition (flag/tag presence) → mistagged-T0 → **OPT-IN** (blanket-§0 and tier agree).

## §2b — Shrink-safety rule (PRIMARY gate on any SHRINK)

**Shrink only tests whose assertion is resolution-INDEPENDENT** — a floor/ceiling/sign/physical bound that does not move with grid N (`IE<100eV`, `bulk-OFF==0`, a sign). **OPT-IN (never shrink) any test whose assertion is resolution-DEPENDENT** — convergence, eigensolve, `rel<0.05`, or a count gated by grid-scale physics (e.g. `≥3 Q before boundary reflection` — reflection timing moves with N). The **≥2× margin check (§6) is the SECONDARY guard, not the primary** — a resolution-dependent assertion can pass a margin check while testing a different regime.

## §3 — Partition (the slow tests; cost = local s, CI ≈ 3.1×)

Remedy legend: **SHRINK** = stays gating, cut grid/steps (resolution-independent only, per §2b); **OPT-IN** = `@pytest.mark.engine_sim` → `make test-engine`; **KEEP** = unchanged; **SMOKE** = add a sub-second guard to keep active-engine coverage in the gate.

| Test | s | Asserts? (tier) | Resolution | Remedy |
|:---|--:|:---|:---|:---|
| `loop_gap_harness_rank1_regime::test_dlite_battery_smoke` | 131.7 | smoke "runs" (T2 driver) | — | **OPT-IN** + **SMOKE** (tiny rank-1 guard added) |
| `cosserat_engine_q_preservation::test_q_preservation_cavity_radius_sweep` | 37.8 | `≥3 Q` count (T0) | **DEP** (decay-before-reflection ∝ N) | **OPT-IN** (was SHRINK — §2b override) |
| `loop_gap_harness_bulk_channel::test_f1_bulk_on_differs_from_off` | 33.8 | sector-live diff (borderline-wiring) | — | **OPT-IN** (redundant w/ fast keepers) |
| `loop_gap_harness::test_loop_gap_probe_runs` | 19.7 | "runs" (T1) | — | **OPT-IN** |
| `electron_tlm_eigenmode::golden_torus convergence` (setup) | 19.6+16.2 | `converged`,`rel<0.02` (T0) | **DEP** (eigensolve) | **OPT-IN** full-res (Ruling 3) |
| `loop_gap_harness_rank1_regime::test_dlite_probe_fields` | 19.0 | instrument (T1) | — | **OPT-IN** |
| `loop_gap_harness::test_graded_a0_seed_runs` | 18.9 | "runs" (T1) | — | **OPT-IN** |
| `loop_gap_harness_bulk_channel::test_f2_channel_tags_on_bulk_probe` | 16.9 | tag/flag presence (**T1**, mistagged) | — | **OPT-IN** |
| `loop_gap_harness_bulk_channel::test_f0_harness_bulk_off_matches_legacy_metrics` | 16.7 | bulk-OFF `==0` (T0) | **INDEP** | **SHRINK** (fewer steps) |
| `unified_threaded_v8::test_d17_cascade_bounded_each_rendering` | 15.4 | bounded (T0-ish) genesis-v8 | — | **OPT-IN** (genesis program) |
| `test_periodic_table::test_transition_metals_stability` | 14.9 | `IE<100 eV` (T0, canonical) | **INDEP** | **SHRINK** (fixed sample) |
| `unified_{quadrature_v7,transducer_v6,genesis_engine,snap_machine}::*` | 2–3 ea | genesis-v8 family | — | **OPT-IN** |
| `engine_saturation_invariants::*` | 3–4 ea | `S_min<0.95`,`z>1.05` (T0) | — | **KEEP** |
| `fdtd3d_*::*` | 1–3.6 ea | comparisons; some xfail | — | **KEEP** |

**Bulk physics stays gated** by the fast direct keepers (`test_bulk_sector_rk2_evolve`, `test_bulk_circulation_ic_rarefies`, `test_vacuum_engine_bulk_on_steps`) — opting in f1/f2 loses no physics coverage.

**Net:** OPT-IN removes ~290 s; the two safe SHRINKs reclaim ~30 s. Projected default `make test`: ~505 s → **~120–140 s local (~6–7 min CI)**, with **zero coverage loss** — the shrunk keepers still assert resolution-independent bounds, the opt-in lane runs in its own CI job, and a tiny rank-1 smoke keeps the active engine guarded.

## §4 — Mechanism

1. `pyproject.toml`: register `markers = ["engine_sim: slow/wiring engine-simulation test, opt-in (see CI partition prereg)"]`.
2. Mark the **OPT-IN** rows `@pytest.mark.engine_sim` (per-test, **not** whole-file — heavy files hold fast keepers too).
3. `Makefile`: default `test` runs `-m "not engine_sim"`; add `test-engine` (`-m engine_sim`).
4. `.github/workflows/verify.yml`: split into a fast PR-blocking `make test` job + a separate `make test-engine` job (longer timeout, or main-only) — coverage de-latencied, not dropped.
5. SHRINK rows: reduce grid/steps **only after** confirming the assertion verdict is unchanged (§6).
6. Sync the conftest comment + ledger §0 to the implemented reality.

## §5 — What I expect / what would discriminate (prereg honesty)

- **Expect:** the marked-out set is exactly the cost-heavy tier-1/2 tests; default-gate verdict set is unchanged for everything that stays; CI `make test` < ~10 min.
- **Falsifier — SHRINK must not change physics:** §2b is the PRIMARY gate (shrink only resolution-independent assertions). SECONDARY guard: for each SHRINK, run full-res vs shrunk, confirm identical pass/fail **and** the asserted quantity stays the same side of its threshold with ≥2× margin. If a shrink flips or narrows margin < 2×, it does **not** shrink — OPT-IN at full res instead.
- **Falsifier — SMOKE must guard:** the tiny rank-1 smoke must still fail on a known-broken rank-1 mutation (e.g., `converter_OFF`). If it can't catch a regression the battery would, keep the battery on a path-filtered trigger.
- **Coupling check:** grep the final diff — if any selection logic (`conftest`, marker assignment, Makefile `-m`) references the capability matrix or a `clm-`/cell grade, that's the hole; remove it (matrix → comments only).

## §6 — Validation plan

1. `make test` (marked) green + timed < target; `make test-engine` green (full set still runs).
2. Per SHRINK: full-res vs shrunk verdict identical + margin ≥ 2× (script the comparison, attach to result doc).
3. Smoke catches a seeded rank-1 regression mutation.
4. Two-worktree check (post-#218 hygiene): markers resolve identically from main checkout + a worktree.
5. CI: the split workflow — fast job blocks PRs; engine job runs and reports.

## §7 — Invariant (the one-line soundness test)

*If someone re-grades a capability-matrix cell tomorrow, does CI coverage change?* **Must be NO.** Enforced structurally: the matrix is referenced only in comments/justification, never in `conftest`/marker/Makefile selection. CI tracks fast+stable+asserting (test-role); the matrix tracks physically-confirmed; the two are never wired.
