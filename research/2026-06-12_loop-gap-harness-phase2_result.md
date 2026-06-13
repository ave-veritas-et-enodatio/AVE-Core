# LOOP GAP harness — Phase 2 seed + ∇A₀ protocols

**Date:** 2026-06-12  
**Status:** IMPLEMENTOR — pending production battery fill  
**Epic:** `_orchestration/2026-06-12_loop-gap-unified-harness.md`  
**DAG:** `_orchestration/2026-06-12_loop-gap-engine-dag.md`  
**Harness:** `src/ave/core/loop_gap_harness.py` + `loop_gap_seeds.py`  
**Driver:** `src/scripts/vol_1_foundations/loop_gap_harness_genesis.py`

---

## §1 — What changed (Phase 2)

| Item | Detail |
|:---|:---|
| Seed modes | `pair`, `photon_lock` (genesis-23 ω precursor), `graded_a0` (∇A₀ tanh ramp) |
| Primary default | `photon_lock` with `A_LOCK=3.0` |
| `phi_growth` fix | Baseline = $\|\Phi_{\mathrm{link}}\|^2$ after **first scatter step**, not IC |
| Impedance gradient | Spatial **∇A** via seed geometry — **not** node density |
| Biology lens | `graded_a0` uses buffered-yield analogue $A_{\mathrm{yield}}^{\mathrm{buf}} = 1 + \varphi_{\mathrm{pack}}$ (membrane LLCP wedge) |

---

## §2 — Classification (`consistency-vs-emergence`)

| Test | Class |
|:---|:---|
| Seed ablation (pair vs photon vs graded) | **consistency-check** — channel routing |
| Rank-1 Γ gate on primary seed | **emergence-test** — asymmetric wall engagement |
| v18 pair-seed production (prior) | **falsifier** — uniform sub-yield IC insufficient |

---

## §3 — Smoke results (N=10, 2026-06-12)

| Seed | $V_{\mathrm{inc,peak}}$ | $\Gamma_{\min}$ | $E_{\mathrm{persist}}$ | R1 | R3 |
|:---|---:|---:|---:|:---:|:---:|
| pair | $1.2\times 10^{-2}$ | $-4\times 10^{-4}$ | 0.873 | FAIL | PASS |
| photon_lock | 0 | **−0.069** | **0.893** | FAIL | FAIL |

**Read:** `photon_lock` moves $\Gamma$ toward engagement (7× vs pair) and raises $E_{\mathrm{persist}}$; $V_{\mathrm{inc}}$ nucleation still needs converter+pair path or longer production grid. **Verdict (smoke):** ENGINE-GAP — rank-1 wall still open.

Production (N=14) proxy-only run **cancelled** — ENGINE-GAP unchanged; rank-1b bulk work in Phase 2b.

```bash
./.venv/bin/python src/scripts/vol_1_foundations/loop_gap_harness_genesis.py --smoke
./.venv/bin/python src/scripts/vol_1_foundations/loop_gap_harness_genesis.py --smoke --bulk
```

**JSON:** `assets/sim_outputs/loop_gap_harness_battery.json`

---

## §6 — Phase 2b (GAP-A bulk channel, 2026-06-12)

| Item | Detail |
|:---|:---|
| Module | `src/ave/core/bulk_rarefaction_sector.py` |
| Engine hook | `VacuumEngine3D.bulk_density_on` (KEEP-BOTH default OFF) |
| Seeds | `probe` (sector-live IC) \| `circulation` (OP-3 motor column) |
| Channel tags | `EM` / `shear` / `bulk` / `proxy` in `LoopGapResult.channel_tags` |
| Rank 1b | `rank1b_pass` — bulk sector live (`ρ̄_min` or `c_bulk²` drop); **not** EM proxy Γ |

### §2b smoke table (N=10, `--smoke --bulk`, 2026-06-12)

| Arm | $\rho_{\mathrm{bar,min}}$ | $\Gamma_{\min}$ (proxy) | R1 | R1b | Channel |
|:---|---:|---:|:---:|:---:|:---|
| bulk_OFF | 0 | −0.069 | FAIL | — | EM+shear |
| bulk_ON (probe) | **−0.0075** | −0.069 | FAIL | **PASS** | bulk+EM+shear |
| bulk_circulation (motor) | **−0.3942** (drive) | — | — | **PASS** | bulk+EM+shear |

| Gate | Result |
|:---|:---|
| F0 bulk_OFF legacy path | PASS (pytest) |
| F1 bulk_ON ≠ bulk_OFF | **PASS** |
| F2 channel-tagged + rank1b | **PASS** |
| Rank-1 proxy Γ | **FAIL** ($\Gamma_{\min}=-0.069 > -0.25$) — expected; not bulk PASS |

**Bugfix (B0):** `BulkRarefactionConfig.c0` must be engine natural units (`1.0`), not SI `C_0` — SI caused CFL substep runaway (~8h pytest hang).

**Verdict (2b smoke):** **F1/F2 PASS**; rank-1 proxy still **ENGINE-GAP** (channel discipline honored).

---

## §4 — Skills fired

- `ave-loop-gap-harness-discipline` — no v19; harness phase advance only  
- `substrate-native-check` — ∇A₀ not buoyancy; asymmetric yield surface  
- `consistency-vs-emergence` — §2 classification  
- `ave-driver-script-honesty` — conservative stepping, no external Source  
- `ave-handoff-canonical-locale` — orchestration + research docs tracked  

---

## §5 — Read-through (pre-production)

v18 production (pair, uniform): $\Gamma_{\min} \approx -4\times 10^{-4}$, $E_{\mathrm{persist}} \approx 0.60 \to 0.47$ as Compton mult increases — **more drive hurts**. Phase 2 tests whether **graded impedance approach** (photon_lock / graded_a0) engages rank-1 wall without pump detonation.

---

## §7 — Phase D-lite (OP-2 instrument + smoke baseline, 2026-06-13)

**Prereg:** `research/2026-06-12_loop-gap-harness-rank1-regime_prereg_FROZEN.md`  
**Driver:** `./.venv/bin/python src/scripts/vol_1_foundations/loop_gap_harness_genesis.py --dlite`  
**JSON:** `assets/sim_outputs/loop_gap_harness_dlite_battery.json`

| Item | Detail |
|:---|:---|
| Instrument | `gamma_bulk_min` live Smith read on $Z_{\mathrm{bulk}}=\rho_{\mathrm{bulk}} c_{\mathrm{bulk}}$ (bulk sector snapshot) |
| Regime | `photon_lock` normalized to canon $A_{\mathrm{yield}}=\sqrt{\alpha}$ via `normalize_cosserat_amplitude` (not `a_lock` sweep) |
| Primary arm | B1 `photon_lock` + bulk probe IC |

### §7.1 Smoke table (N=10, `--dlite`)

| Arm | $V_{\mathrm{inc,peak}}$ | $\Gamma_{\mathrm{bulk,min}}$ | proxy $\Gamma_{\min}$ | $A_{\mathrm{seed}}$ | OP-2 bin |
|:---|---:|---:|---:|---:|:---|
| B0 heal bulk_OFF | 0 | — | 0 | 0 | ENGINE-GAP |
| B0 heal bulk_ON | 0 | −0.190 | 0 | 0 | ENGINE-GAP |
| **B1 photon_yield** | **0** | **−0.190** | ≈0 | **0.0854** | **ENGINE-GAP** |
| B2 pair $\sqrt{\alpha}$ | $1.22\times 10^{-2}$ | −0.190 | ≈0 | 0.866 | OP-2-PARTIAL |

### §7.2 Hypothesis read (`consistency-vs-emergence`)

| ID | Verdict |
|:---|:---|
| H1 | **CONFIRMED** — bulk $\bar\rho$ live ($\Gamma_{\mathrm{bulk}}\approx -0.19$); B1 $V_{\mathrm{inc}}=0$ on transverse-only engine |
| H2 | **CONFIRMED** — `gamma_bulk_min` tracks bulk port independently of proxy (proxy flat at ≈0 under yield-front seed) |
| H3 | **CONFIRMED** — ENGINE-GAP on primary B1 motivates **Phase C′** scalar restoration (not louder transverse sweep) |

**Composite verdict:** **ENGINE-GAP** on primary arm (expected by thesis). B2 pair path shows **OP-2-PARTIAL** ($V_{\mathrm{inc}}$ only) — consistency arm, not emergence on transverse $\omega$ packet.

**Next:** Phase C′ implementor — `research/2026-06-13_loop-gap-scalar-grade-restoration_prereg_FROZEN.md`

---

## §8 — Phase C′ scalar-grade restoration (2026-06-13)

**Prereg:** `research/2026-06-13_loop-gap-scalar-grade-restoration_prereg_FROZEN.md`  
**Driver:** `./.venv/bin/python src/scripts/vol_1_foundations/loop_gap_harness_genesis.py --smoke-scalar`  
**JSON:** `assets/sim_outputs/loop_gap_harness_scalar_battery.json`  
**Runtime:** ~15 min (N=10, S0–S4 + ablations)

| Item | Detail |
|:---|:---|
| C′1 | `scalar_grade_seed.py` — Lane-1 standing $V$, CP8 on S1 |
| C′2 | `scalar_grade_source.py` — B′ Beltrami bootstrap (relu(−Γ) rejected) |
| C′5 | GAP-C **not wired** — S4 ≡ S3 |

### §8.1 Primary arms (frac=0.85, $A_{\mathrm{yield}}$ front)

| Arm | $V_{\mathrm{inc,peak}}$ | $\Gamma_{\mathrm{bulk,min}}$ | $\|\omega\|_{\mathrm{end}}$ | $A^2_V$ | $H_{\mathrm{drift}}$ | OP-2 | SCALAR |
|:---|---:|---:|---:|---:|---:|:---|:---|
| S0 | 0 | −0.190 | 0.043 | 0 | 0.145 | ENGINE-GAP | BASELINE |
| S1 | 0.289 | −0.190 | 0 | 0.321 | 0.517 | OP-2-PARTIAL | SCALAR-IC-LANDED |
| S2 | 0.289 | −0.190 | 0.043 | 0.321 | 0.492 | OP-2-PARTIAL | REPRESENTATION-GAP |
| **S3** | **0.289** | **−0.190** | **0.043** | **0.321** | **0.492** | **OP-2-PARTIAL** | REPRESENTATION-GAP |
| S4 | 0.289 | −0.190 | 0.043 | 0.321 | 0.492 | OP-2-PARTIAL | REPRESENTATION-GAP |

### §8.2 Falsifiers (primary S3)

| ID | Result | Read |
|:---|:---:|:---|
| F1 scalar seed | **PASS** | S1: CP8 null, $A^2_V=0.32 > 0.25\,A_{\mathrm{yield}}^2$ |
| F2 $V\to\omega$ source | **FAIL** | S3 $\|\omega\|$ ≈ S2; $H_{\mathrm{drift}}\approx 0.49 \gg 10^{-6}$ |
| F3 OP-2 composite | **FAIL** | $\Gamma_{\mathrm{bulk}}=-0.19 > -0.25$; $V_{\mathrm{inc}}$ high but **IC-attributable** on S1 (not dynamic nucleation) |

### §8.3 Hypothesis read

| ID | Verdict |
|:---|:---|
| H1 | **CONFIRMED** — S0 $V_{\mathrm{inc}}=0$ (transverse-only baseline) |
| H2 | **CONFIRMED** — S1 scalar IC lands without source; $\omega=0$ at $t=0$ |
| H3 | **NOT SUPPORTED** — S3 does not deepen $\Gamma_{\mathrm{bulk}}$ or lift $\|\omega\|$ vs S2 at smoke budget |
| H4 | **DEFERRED** — GAP-C not wired |
| H5 | **INCONCLUSIVE** at battery scale — `bulk_force_ON` arm matches S3 $\|\omega\|$; keeper detonation test passes at reduced budget |

**Composite verdict:** **REPRESENTATION-GAP** (program bin). **Physics read:** **SCALAR-PARTIAL** — scalar IC restoration lands (F1); conservative source + OP-2 dynamic closure **not** demonstrated at √α smoke. Do **not** promote S1/S3 $V_{\mathrm{inc}}\approx 0.29$ as OP-2 LANDED (seed scatter into transverse readout).

**D-full gate:** SCALAR-PARTIAL documented — rational `a_lock` / saturation-front sweep may proceed; expect Grant adjudication on χ lock leg if source stays weak.

**Next:** PR `analysis/2026-06-13-loop-gap-scalar-grade`; optional C′5 GAP-C; D-full on restored engine.
