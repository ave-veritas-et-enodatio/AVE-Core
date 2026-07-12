# Genesis node-birth discriminators D1–D4 — RESULT

**Date:** 2026-07-12 · **Branch:** `analysis/genesis-node-birth-d14`
**Prereg (FROZEN by push on #654):** `research/2026-07-12_genesis-node-birth-discriminator_prereg_FROZEN.md`
**Driver:** `src/scripts/vol_1_foundations/genesis_node_birth_discriminator.py`
**Class:** architecture discrimination. **No chord. No `genesis_v{N}`. No graph-growth.**

α-CLEAN. Rule-14: reuses `CrystalEngine` / `MasterEquationFDTD` / `loop_gap_harness.run_loop_gap_probe`.

---

## Frozen-bin verdict

| bin | outcome |
|---|---|
| **(ii) A-WEAKENED** | **LANDED** |

| gate | result | claim class |
|---|---|---|
| **D1** DOF conservation | **PASS** — `N³` invariant on crystal_engine, master_equation_fdtd, loop_gap_harness config | `certification_entailed` |
| **D2** Fixed-N persistence | **FAIL** on declared harness battery (`N=10`, `fast=True`, photon_lock + bulk density) | `C_consistency` |
| **D3** Necessity of (B) | **PASS** — (B) not entailed; cite table below | `C_consistency` |
| **D4** Cosmology OOM | **SKIPPED-WITH-REASON** — fence only after (B) ruled | n/a |

**Meaning (frozen):** Fixed-N pattern is insufficient for lasting localization on the declared battery. This does **not** auto-select fork (B). R10 remanence remains open under (A). KEEP-BOTH continues until Grant rules.

**Refuse:** never bank D1 PASS as `ClaimClass.EMERGENCE` / node genesis (#653).

---

## D1 — numbers

| path | N | sites t0 | sites tend | invariant |
|---|---:|---:|---:|---|
| crystal_engine | 16 | 4096 | 4096 | yes |
| master_equation_fdtd | 16 | 4096 | 4096 | yes |
| loop_gap_harness | 10 | 1000 | 1000 | yes (config `N`; mesh cannot grow on this platform) |

Entailed-branch note: invariance on today’s engines is partly install-tautology (fixed mesh). Fireable content is the **labeling discipline** + surfacing any future cardinality mutation.

---

## D2 — numbers (smoke battery)

`run_loop_gap_probe(..., N=10, rank_target=4, seed_mode="photon_lock", bulk_density_on=True, front_target=A_YIELD, fast=True)`:

| quantity | value | floor |
|---|---:|---:|
| `E_persist_ratio` | 0.820 | ≥ 0.85 (`P11_E_PERSIST_MIN`) |
| `phi_persist_ratio` | 0.0 | ≥ 0.80 (`P11_A_PERSIST_MIN`) |
| `rank4_pass` | false | — |
| `v_inc_peak` | 0.0 | — |
| `persistence_pass` | **false** | — |

Honest FAIL → bin (ii). Matches corpus expectation that remanence / lasting localization often fails on anhysteretic paths; does not prove node mint.

---

## D3 — cite table (not entailed)

| leaf | point |
|---|---|
| `manuscript/ave-kb/common/historical-precedents.md` | Kelvin lacked confinement + scale; AVE names both on fixed N — does not derive N→N+1 necessity |
| `manuscript/ave-kb/common/engine-capability-map.md` | node-creation empty on every engine; after remanence+boost in build-order |
| `research/2026-06-24_engine-stage2-native-cage_result.md` | Mode-III DISPERSE; Γ=−1 cavity on fixed mesh |
| `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` | ranks 1–4 fixed platforms; R10 constitutive, not graph-growth |

No load-bearing leaf found that **derives** Compton-scale N→N+1 as necessary for charged-soliton existence.

---

## D4

**SKIPPED-WITH-REASON.** Numeric OOM fence is post-(B)-ruling only. Phase-0 remains KEEP-BOTH.

---

## Gates checklist (prereg §Gates)

1. D1 cardinality — done (3 paths).
2. D2 drive-off persistence — done (FAIL).
3. D3 cite table — done.
4. D4 SKIPPED-WITH-REASON — done.
5. `ClaimClass` tags — done (refuse EMERGENCE-as-genesis).
6. Fast pytest keepers green; D2 in `engine_sim` partition.

---

## Out of scope (still forbidden)

- Graph-growth / fourth engine / `genesis_v{N}` / srs v18+.
- Merging #652 X44 as reconciled.
- Ruling (A) or (B) from this result alone — **(ii) weakens (A)-as-sufficient for lasting localization; does not select (B).**

## Next (orchestration)

Grant: keep KEEP-BOTH, or escalate (A)-weakened → graph-growth charter discussion, or deepen D2 battery (non-fast / cavity Γ=−1 paths) before any (B) ruling.
