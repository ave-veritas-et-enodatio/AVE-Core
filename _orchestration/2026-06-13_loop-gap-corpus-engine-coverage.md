# LOOP GAP — corpus ↔ engine ↔ test coverage ledger

**Status:** LIVE — orchestrator-maintained belief map  
**Opened:** 2026-06-13  
**Parent plan:** [`2026-06-12_loop-gap-orchestration-plan.md`](2026-06-12_loop-gap-orchestration-plan.md)  
**Harness DAG:** [`2026-06-12_loop-gap-engine-dag.md`](2026-06-12_loop-gap-engine-dag.md)  
**Doctrine:** [`manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md`](../manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md)

**Last verified branch HEAD:** `analysis/2026-06-13-loop-gap-scalar-grade` @ C′1+C′2 commit (orchestrator: refresh each session via `git rev-parse --short HEAD`)

---

## §0 — How orchestrators use this doc

### Belief tiers (do not conflate)

| Tier | Label | Meaning | Orchestrator rule |
|:---:|:---|:---|:---|
| **T0** | `KEEPER` | Unit test asserts the claim outcome (or definitional identity) | Safe to cite as **verified** |
| **T1** | `WIRING` | Code runs; test checks flags/shapes/non-crash only | **Machinery exists** — not physics PASS |
| **T2** | `DRIVER` | Production JSON / driver script only; excluded from default CI | Cite result doc + JSON path; not keeper |
| **T3** | `NARRATIVE` | Corpus leaf with no engine observable on active path | Routing / intuition only |
| **T4** | `FALSIFIED` | Ablation or prereg closed the lever | Do not re-scope without new prereg |

### Row ID convention

`CVG-{rank|BED}-{NNN}` — e.g. `CVG-R1-003`, `CVG-BED-012`, `CVG-NAR-001`, `CVG-FAL-002`.

### Promotion rules (implementor → orchestrator)

1. **WIRING → KEEPER:** add pytest that asserts the gate floor/ceiling from doctrine or prereg; update row `Keeper` + `Tier`; cite `test_*.py` path in PR body.
2. **DRIVER → KEEPER:** port the production assertion into `src/tests/` (smoke tier OK if prereg says so); demote driver to supplementary.
3. **NARRATIVE:** stays T3 until engine DAG lists an observable — then open a phase task; do not promote from KB prose alone.
4. Every orchestration session that touches harness ranks: grep this file for rows in scope; update `Production` / `Phase` / `Last verified` columns.

### Default CI scope (sanity)

| Suite | Command | LOOP GAP relevance |
|:---|:---|:---|
| Substrate keepers | `make test` (~1480 tests) | Bedrock rows only |
| Harness | `pytest src/tests/test_loop_gap_harness*.py` (11 tests) | Ranks 1–4 wiring |
| Genesis archive | `make test-genesis` (opt-in) | srs falsifiers — **not** active path |

---

## §1 — Rollup (update counts when rows change)

| Tier | Count | LOOP GAP ranks 1–4 |
|:---:|:---:|:---|
| T0 KEEPER | 22 | Bedrock + C′ scalar seed/source keepers |
| T1 WIRING | 12 | Harness + bulk port |
| T2 DRIVER | 9 | v15b–v18 + smoke battery |
| T3 NARRATIVE | 8 | Identification / cosmology |
| T4 FALSIFIED | 6 | Retired levers |

**Rank closure (belief, 2026-06-13):** Rank **1** partial · Rank **1b** channel live · **C′** scalar IC + source **WIRING→KEEPER** (C′1–C′2) · OP-2 composite **open** · Ranks **2–4** **open** · LOOP GAP **not closed**.

---

## §2 — Bedrock (Tier T0 — trust these)

| ID | Claim | Corpus / constant | Engine | Keeper test | Notes |
|:---|:---|:---|:---|:---|:---|
| CVG-BED-001 | $\alpha$ canonical | `constants.py` | `ave.core.constants.ALPHA` | `test_constants_derivation.py` | Definitional import chain |
| CVG-BED-002 | $\ell_{\mathrm{node}}=\hbar/(m_e c)$ | KB natural units | `L_NODE` | `test_engine_constants_alignment.py` | Instance alignment |
| CVG-BED-003 | $A^2_{\mathrm{yield}}=2\alpha$ knee | doctrine §4 | yield surfaces | `test_v_snap_v_yield_consistency.py` | Regime gate reference |
| CVG-BED-004 | $S_{\mathrm{eq}}(A)=\sqrt{1-A^2}$ | Ax4 | `k4_tlm` saturation | `test_axiom_4_vacuum_varactor.py` | Level-1 anhysteretic |
| CVG-BED-005 | $K/G=2$, $V_{\mathrm{LONG}}=\sqrt{2}\,c$ | vol9 three-channel | `constants` + rupture | `test_vacuum_moduli_and_channels.py` | Channel algebra |
| CVG-BED-006 | $\tau_{\mathrm{relax}}=\ell_{\mathrm{node}}/c$ native | doc 59 | `TAU_RELAX_NATIVE` | `test_memristive_op14.py` | Rank 4 dynamics substrate |
| CVG-BED-007 | K4 CFL + port scatter | doc 30 | `K4Lattice3D` | `test_engine_constants_alignment.py` | z=4 diamond bedrock |
| CVG-BED-008 | Memristive Op14 stable at $\mathrm{d}t/\tau\sim O(1)$ | doc 59 | `k4_tlm` branch | `test_memristive_op14.py` | **Dynamics only** — not P11 outcome |
| CVG-BED-009 | Trilinear $f_V\neq 0$ with $\omega$, $w$ | A44 / GAP-1 | `cross_sector_coupling` | `test_cross_sector_coupling.py` | Converter primitive |
| CVG-BED-010 | Converter ON raises $V_{\mathrm{inc}}$ vs OFF | GAP-1 | `CoupledK4Cosserat` | `test_cross_sector_coupling.py` | Rank-1 partial mechanism |
| CVG-BED-011 | $c_{\mathrm{bulk2}}(\bar\rho)$ EOS clip | bulk leaf | `bulk_rarefaction_sector` | `test_c_bulk2_eos_at_probe` | Rank 1b EOS |
| CVG-BED-012 | Bulk sector RK2 evolves $\bar\rho$ | GAP-A | `BulkRarefactionSector` | `test_bulk_sector_rk2_evolve` | Sector unit |
| CVG-BED-013 | $\tilde\kappa=6/5$ α-free | cross-sector prereg | `KAPPA_TILDE` | `test_cross_sector_coupling.py` | Trilinear scale |
| CVG-BED-014 | Pump / `add_drive` falsified | genesis-24 | harness DAG ✗ | `test_unified_drive.py` (legacy) | Rank 3 negative |
| CVG-BED-015 | Predictions manifest schema | `predictions.yaml` | validator | `test_predictions_manifest_validator.py` | Metadata — not physics PASS |
| CVG-BED-016 | Engine instances use `constants` | Grant 2026-05-02 | `VacuumEngine3D` | `test_engine_constants_alignment.py` | Alignment gate |
| CVG-BED-017 | Cosserat field shapes / yields | topological sector | `CosseratField3D` | `test_cosserat_field_3d.py` | Coupling substrate |
| CVG-BED-018 | Rank profile flags cumulative | harness DAG | `engine_config_for_rank` | `test_rank_profiles_cumulative` | Config wiring only |

---

## §3 — LOOP GAP ranks 1–4 (active path — `VacuumEngine3D` + harness)

### Rank 1 — OP-2 container ($V_{\mathrm{inc}}$, $\Gamma$ wall)

| ID | Claim | Ch | Corpus | Engine | Keeper | Tier | Production | Phase |
|:---|:---|:---:|:---|:---|:---|:---:|:---|:---:|
| CVG-R1-001 | $V_{\mathrm{inc,peak}}>P18$ floor | EM+conv | v15b charter | `loop_gap_harness` | — | **T2** | v15b **LANDED** (`genesis_v15b_k4_nucleation.json`) | D |
| CVG-R1-002 | Proxy `gamma_min ≤ -0.25` (Op14 μ-short) | proxy | harness Phase 2 | `use_impedance_boundary` | — | **T1** | smoke **ENGINE-GAP** | D |
| CVG-R1-003 | $\Gamma_{\mathrm{bulk}}$ from live $\bar\rho$, $c_{\mathrm{bulk}}$ | bulk | vol9 §3, bulk leaf | `loop_gap_harness.gamma_bulk_min` | `test_loop_gap_harness_rank1_regime.py` | **T0** | D-lite smoke **PARTIAL** ($\approx -0.19$) | D-lite ✅ |
| CVG-R1-004 | `rank1_pass` composite gate | multi | harness | `_rank_gates` | — | **T1** | not asserted in CI | D |
| CVG-R1-005 | Seed `pair` conservative IC | — | genesis pair | `loop_gap_seeds.pair` | `test_loop_gap_probe_runs` (partial) | **T1** | smoke only | D |
| CVG-R1-006 | Seed `photon_lock` @ $A_{\mathrm{LOCK}}$ | — | genesis-23 | `loop_gap_seeds.photon_lock` | `test_loop_gap_probe_runs` | **T1** | 7× proxy Γ vs pair (result §2) | D |
| CVG-R1-007 | Seed `graded_a0` ∇$A_0$ ramp | — | graded yield | `loop_gap_seeds.graded_a0` | `test_graded_a0_seed_runs` | **T1** | smoke only | D |
| CVG-R1-008 | Regime gate $A^2\in[0.5,2]\cdot 2\alpha$ | — | plan §3 | harness logs `max_a_sq_k4_end` | — | **T1** | not enforced in CI | D |
| CVG-R1-009 | `impedance_OFF` ablation kills Γ proxy | proxy | DAG ablation | harness battery | — | **T2** | driver JSON only | D |
| CVG-R1-010 | `converter_OFF` ablation kills $V_{\mathrm{inc}}$ | conv | DAG ablation | harness battery | — | **T2** | driver JSON only | D |

**Phase D-lite closes:** CVG-R1-003 (instrument), CVG-R1-002/004 (keeper or ENGINE-GAP), CVG-R1-008 (regime gate in test). — **D-lite LANDED** `05fa9e4f`.

**Phase C′ closes:** standing longitudinal $V$ seed; $V\to\omega$ Option-D source; S3 vs S0 $V_{\mathrm{inc}}$ nucleation — rows below.

| ID | Claim | Ch | Corpus | Engine | Keeper | Tier | Production | Phase |
|:---|:---|:---:|:---|:---|:---|:---:|:---|:---:|
| CVG-C′-001 | Standing $V$ seed (Lane-1) on K4 $V_{\mathrm{inc}}$ | scalar | genesis-24 / abandoned-interior | `scalar_grade_seed.py` | `test_loop_gap_harness_scalar_grade.py` | **T0** | keeper only | C′1 ✅ |
| CVG-C′-002 | CP8 topology-null certificate at $t=0$ | scalar | prereg F1 | `scalar_seed_certificate` | `test_scalar_seed_cp8_topology_null` | **T0** | keeper only | C′1 ✅ |
| CVG-C′-003 | $V\to\omega$ Option-D source (B′ bootstrap) | conv | tracereversal + reactive-entrainment | `scalar_grade_source.py` | `test_loop_gap_harness_scalar_grade.py` | **T0** | weak at smoke; not F3 PASS | C′2 ✅ |
| CVG-C′-004 | `bulk_force_v_to_omega` detonation control | conv | prereg ablation | harness + engine | `test_bulk_force_detonates` | **T0** | detonates ~9× | C′2 ✅ |
| CVG-C′-005 | S0–S4 smoke + SCALAR verdict bin | multi | prereg §3 | driver `--smoke-scalar` | — | **T2** | **not run** | **C′3 — NEXT** |
| CVG-C′-006 | Result §8 ablation + $H_{\mathrm{drift}}$ ledger | — | phase2 result | — | — | **T2** | **not written** | **C′4 — NEXT** |
| CVG-C′-007 | GAP-C `gap_c_coupling_on` ablation (S4) | bulk | 2b prereg Inc C | harness | — | **T1** | not wired | **C′5 — PENDING** |

### Rank 1b — bulk channel (GAP-A containment)

| ID | Claim | Ch | Corpus | Engine | Keeper | Tier | Production | Phase |
|:---|:---|:---:|:---|:---|:---|:---:|:---|:---:|
| CVG-R1B-001 | `bulk_density_on` attaches sector | bulk | Phase 2b prereg | `VacuumEngine3D.bulk` | `test_vacuum_engine_bulk_on_steps` | **T0** | Phase 2b **LANDED** | ✅ |
| CVG-R1B-002 | `bulk_OFF` leaves EM/shear unchanged | bulk | KEEP-BOTH | harness F0 | `test_f0_harness_bulk_off_matches_legacy_metrics` | **T0** | F0 PASS | ✅ |
| CVG-R1B-003 | `bulk_ON` ≠ `bulk_OFF` on $\bar\rho_{\min}$ | bulk | GAP-A | harness | `test_f1_bulk_on_differs_from_off` | **T0** | F1 PASS | ✅ |
| CVG-R1B-004 | Channel tags include `bulk` + `proxy` | multi | I2 invariant | harness | `test_f2_channel_tags_on_bulk_probe` | **T0** | F2 PASS | ✅ |
| CVG-R1B-005 | Circulation IC rarefies $\bar\rho$ | bulk | scale ladder | `BulkRarefactionSector` | `test_bulk_circulation_ic_rarefies` | **T0** | Phase 2b | ✅ |
| CVG-R1B-006 | `rank1b_pass` = containment read | bulk | doctrine | harness | — (asserted in F2 indirectly) | **T1** | smoke PASS | D |
| CVG-R1B-007 | Bulk rarefaction **≠** rank-4 remanence | bulk | fool mode | — | — | **T4** | thixotropy OUTCOME B | — |

### Rank 2 — Compton ring-up

| ID | Claim | Ch | Corpus | Engine | Keeper | Tier | Production | Phase |
|:---|:---|:---:|:---|:---|:---|:---:|:---|:---:|
| CVG-R2-001 | Drive length $\propto \tau_{\mathrm{relax}}$ | — | v16 charter | `n_drive_mult` | — | **T1** | v16 **CAVITY-SET-ONLY** | F |
| CVG-R2-002 | Cavity holds under ring-up | — | v16 | srs v16 / harness | `test_p16_cavity_cell_runs` (genesis opt-in) | **T1** | $E_{\mathrm{persist}}\approx 0.71$ | F |
| CVG-R2-003 | `phi_growth` or `ρ_cross` rank-2 gate | multi | DAG | `_rank_gates` rank2 | — | **T2** | harness driver | F |
| CVG-R2-004 | Matched-baseline 2× structure doubling | — | doctrine §6 | — | — | **T3** | not implemented | F |

### Rank 3 — energize-lock (conservative)

| ID | Claim | Ch | Corpus | Engine | Keeper | Tier | Production | Phase |
|:---|:---|:---:|:---|:---|:---|:---:|:---|:---:|
| CVG-R3-001 | `freeze_converter_wall()` post-seed | conv | genesis-23 | `CoupledK4Cosserat` | used in `test_cross_sector_coupling` | **T0** | GAP-1 replay PASS | F |
| CVG-R3-002 | No external pump / CW source | — | genesis-24 | harness DAG ✗ | CVG-BED-014 | **T4** | pump falsified | — |
| CVG-R3-003 | `rank3_pass` ($\Phi$ growth / $\rho_{\mathrm{cross}}$) | multi | DAG | harness | — | **T2** | driver | F |
| CVG-R3-004 | GAP-1 parity with `cross_sector_gap1_closure.py` | conv | FROZEN prereg | script | — | **T2** | production PASS | F |

### Rank 4 — constitutive remanence (LOOP GAP crux)

| ID | Claim | Ch | Corpus | Engine | Keeper | Tier | Production | Phase |
|:---|:---|:---:|:---|:---|:---|:---:|:---|:---:|
| CVG-R4-001 | $E_{\mathrm{persist}}\geq 0.85$ after quiescence | — | P11 | harness rank 4 | — | **T2** | best **0.71** FAIL | G |
| CVG-R4-002 | $\phi_{\mathrm{persist}}\geq 0.80$ | — | P11 | harness | — | **T2** | sub-floor | G |
| CVG-R4-003 | `use_memristive_saturation` on rank 4 profile | — | doc 59 | `k4_tlm` + engine | `test_memristive_op14` (K4 only) | **T1** | dynamics pinned; outcome not | G |
| CVG-R4-004 | `memristive_OFF` ablation changes $S_\Delta$ | — | DAG | harness | — | **T2** | driver | G |
| CVG-R4-005 | Pinned quiescence (no comoving bleed) | — | v17 lesson | harness protocol | — | **T2** | v17 falsified comoving | G |
| CVG-R4-006 | R2 ferrite B–H enclosed loop area | bench | R2 prereg FROZEN | **bench** not lattice | — | **T3** | not run | G2 |
| CVG-R4-007 | CVR-SET under drive = mass | — | fool mode #1 | — | — | **T4** | v10 falsifier | — |
| CVG-R4-008 | `REMANENCE-LANDED` harness verdict | multi | doctrine | harness battery | — | **T2** | never landed | G |

---

## §4 — Narrative corpus (Tier T3 — do not treat as engine-verified)

| ID | Narrative | Corpus home | Why T3 | Unblock path |
|:---|:---|:---|:---|
| CVG-NAR-001 | $(2,3)$ Clifford-torus winding | `l3-electron-soliton-synthesis.md` | No winding DOF in harness | Identification layer post-rank-4 |
| CVG-NAR-002 | Spin-½ / $0_1$ unknot body | `photon-identification.md` | Not measured | Downstream |
| CVG-NAR-003 | Cosmic crystallization stream | `op14-cosmic-horizon-profile.md` | Finite box; v15a cosmic IC FAIL | Cosmology drivers — not LOOP GAP |
| CVG-NAR-004 | Lane A cosmic deposit nucleation | v15a provenance | $10^{-72}$/cell | Not rank closure |
| CVG-NAR-005 | $\Omega_{\mathrm{freeze}}$ as remanence motor | omega-freeze leaf | IC only | CVG-FAL-003 |
| CVG-NAR-006 | EM $S_{11}$ at $Z_0$ = confinement | vol9 fool mode | Wrong channel | Use CVG-R1-003 |
| CVG-NAR-007 | srs substrate migration (framing) | D1 memo | P5/P6 post-rupture | Valid-regime hosting TBD |
| CVG-NAR-008 | `CrystalEngine.gamma_bulk` ⇒ harness PASS | apparatus scripts | **Wrong platform** | Port to harness (Phase D) |

---

## §5 — Falsified / retired (Tier T4)

| ID | Mechanism | Evidence | Harness rule |
|:---|:---|:---|:---|
| CVG-FAL-001 | `add_drive` / CW pump lock | genesis-24 | ✗ ranks 3–4 |
| CVG-FAL-002 | Snap bin-isolating remanence | v10 ablation | optional; not default |
| CVG-FAL-003 | $\Omega_{\mathrm{freeze}}$ IC = remanence | v10 ablation | ablation arm only |
| CVG-FAL-004 | Comoving quiescence | v17 | pinned quiet only |
| CVG-FAL-005 | Proxy `gamma_min` as bulk PASS | smoke + doctrine | require CVG-R1-003 |
| CVG-FAL-006 | Post-rupture bins for framing | v9/v10 quarantine | `_POST_RUPTURE` suffix |

---

## §6 — Keeper backlog (orchestrator priority queue)

Ordered work that **promotes rows** from T1/T2 → T0. Implementor PR must cite row IDs.

| Priority | Row ID(s) | Deliverable | Owner phase | Acceptance |
|:---:|:---|:---|:---:|:---|
| **P0** | CVG-C′-005, CVG-C′-006 | `--smoke-scalar` S0–S4 + result §8 | **C′3–C′4** | SCALAR bin + ablation matrix |
| **P0** | CVG-C′-007 | GAP-C ablation arm S4 | **C′5** | `gap_c_coupling_on` OFF default |
| **P1** | CVG-R1-002, CVG-R1-004, CVG-R1-008 | Proxy Γ + composite + regime gate keepers | **D-full** | on restored engine |
| **P1** | CVG-R1-009, CVG-R1-010 | Ablation keepers in harness CI | **D-full** | `impedance_OFF` / `converter_OFF` flip gates |
| **P2** | CVG-R2-003 | Rank-2 keeper at valid regime | **F** | Compton sweep smoke |
| **P3** | CVG-R4-001, CVG-R4-008 | P11 keeper (PASS or honest FAIL) | **G** | assert floor or `OPERATOR-SET-ONLY` |
| **P4** | CVG-R4-006 | R2 bench execution | **G2** | bench result doc |

---

## §7 — Session update checklist (orchestrator agent)

Run at **start** of each LOOP GAP orchestration session:

```bash
git rev-parse --short HEAD                    # → update § header Last verified
pytest src/tests/test_loop_gap_harness*.py -q # → harness wiring still green
# After implementor PR merge:
# 1. Grep row IDs cited in PR body
# 2. Promote Tier column if new keeper landed
# 3. Update §1 rollup counts
# 4. Point index.md carry-forward to open P0 rows
```

Run at **implementor handoff**:

1. Assign row IDs from §6 backlog — not vague "close rank 1."
2. Prereg must list row IDs under test.
3. Result doc table columns: `Row ID | Tier before | Tier after | Verdict`.

**Anti-pattern:** Claiming KEEPER because `make test` is green — default suite does not assert CVG-R1-003 or CVG-R4-001.

---

## §8 — Cross-references

| Doc | Role |
|:---|:---|
| [`2026-06-12_loop-gap-orchestration-plan.md`](2026-06-12_loop-gap-orchestration-plan.md) | Phase D–G execution |
| [`2026-06-12_loop-gap-unified-harness.md`](2026-06-12_loop-gap-unified-harness.md) | Harness epic log |
| [`research/2026-06-12_genesis-program-status.md`](../research/2026-06-12_genesis-program-status.md) | Production verdict ledger |
| [`research/2026-06-12_loop-gap-harness-phase2_result.md`](../research/2026-06-12_loop-gap-harness-phase2_result.md) | Phase 2 smoke reads |
