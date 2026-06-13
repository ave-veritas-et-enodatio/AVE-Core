# LOOP GAP — v14 charter: cavity + comoving transport stack (2026-06-12)

**Epic:** genesis electron resonator closure  
**Status:** CHARTER COMPLETE — CAVITY-BREAK landed; v14b pocket-frame peak OPEN  
**Program ledger:** `research/2026-06-12_genesis-program-status.md`  
**Parent:** v13 charter `_orchestration/2026-06-12_loop-gap-v13-charter.md`  
**Prereg:** `research/2026-06-12_genesis-v14-cavity-transport_prereg_DRAFT.md`

---

## Phase 0 — Scope (2026-06-12)

v13 production **LOCALIZATION-LANDED** (P13). v12 production **ENGINE-GAP** on open srs (P12).

v14 is the **first dual-gate** integration:

> Stack v12 integer node-roll **on top of** v13 bulk-wall cavity; require **P13 + P12** on the same run.

**Unblocks:** voxel translation read under bounded resonator (LOOP GAP rank 1 + dynamical program R5).

**Deferred:** Compton ring-up (rank 2); P11 remanence (rank 4); CoupledK4Cosserat unified bulk.

---

## Phase 1 — Implementor (COMPLETE — 2026-06-12)

| Artifact | Path |
|:---|:---|
| Engine | `src/ave/core/chiral_lattice_v14.py` |
| Tests | `src/tests/test_chiral_lattice_v14.py` |
| Driver | `chiral_lattice_v14_genesis.py` |
| Figures | `chiral_lattice_v14_figures.py` → `assets/sim_outputs/genesis_v14_figures/` |

**Implementation sketch:**

1. `run_p14_stack_cell()` — `vector_tlm_step_v13` then `translate_field_along_axis` when `comoving=True`.
2. `v14_gates()` — 6-cell ablation matrix (prereg §4) + P14 composite verdict.
3. `run_op3_only_wall_cell()` — `exterior_leak=1.0` sensitivity arm.
4. Reuse P13/P12 thresholds from v13/v12 modules (single source).

```bash
pytest src/tests/test_chiral_lattice_v14.py -q
python src/scripts/vol_1_foundations/chiral_lattice_v14_genesis.py --smoke
python src/scripts/vol_1_foundations/chiral_lattice_v14_genesis.py
```

**Estimated wall time:** smoke ~1 min; production ~3–5 min (same order as v13).

---

## Phase 2 — Production result (DONE 2026-06-12)

- [x] Production run — **CAVITY-BREAK** (P13 peak metric on comoving arm)
- [x] Result doc — `research/2026-06-12_genesis-v14-cavity-transport_result.md`
- [ ] Ratify P14 composite thresholds / peak-metric revision (v14b)
- [ ] Rename prereg `_FROZEN`

**Production snapshot:** full stack disp=1.783, E_frac=0.828, width×=0.92; pinned disp=0.004; gain=1.778 (threshold 4.978); Op3-only width×=3.75.

---

## Phase 3 — Expected outcomes

| Outcome | Implication |
|:---|:---|
| **TRANSPORT-IN-CAVITY-LANDED** | Discrete srs can **localize and translate** — proceed to Compton ring-up (rank 2) |
| **PARTIAL** | Cavity holds; tune v_boost / pocket geometry |
| **CAVITY-BREAK** | Comoving incompatible with wall — revisit advection order or soft walls |
| **ENGINE-GAP** | Cavity OK, no gain — need multi-channel bulk or drive physics |

---

## Inputs (frozen context)

| Doc | Verdict |
|:---|:---|
| v13 result | LOCALIZATION-LANDED — `research/2026-06-12_genesis-v13-eigen-cavity_result.md` |
| v12 JSON | ENGINE-GAP — `assets/sim_outputs/genesis_v12_boost_transport.json` |
| v13 JSON | LOCALIZATION-LANDED — `assets/sim_outputs/genesis_v13_eigen_cavity.json` |

---

## Phase 4 — Successor forks

| Fork | Charter |
|:---|:---|
| v14b pocket-frame peak | This charter Phase 2 open item |
| v15 Lane A (HEAL-CONFIRMED) | `_orchestration/2026-06-12_loop-gap-v15-charter.md` |
| Program ledger | `research/2026-06-12_genesis-program-status.md` |

---

## Related

- LOOP GAP doctrine §6d, §7 (three lanes)
- Fundamentality plan **R5** — boost-covariant transport
- v12 charter v12b scope — now absorbed into v14
