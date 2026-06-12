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

Production (N=14) pending — full seed ablation + `A_LOCK` sweep.

```bash
./.venv/bin/python src/scripts/vol_1_foundations/loop_gap_harness_genesis.py
./.venv/bin/python src/scripts/vol_1_foundations/loop_gap_harness_genesis.py --smoke
```

**JSON:** `assets/sim_outputs/loop_gap_harness_battery.json`

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
