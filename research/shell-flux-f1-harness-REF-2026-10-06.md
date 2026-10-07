# Shell-flux F1 harness — reference doc

**Date:** 2026-10-06  
**Branch:** `feat/shell-flux-f1-harness`  
**Status:** harness shipped; NO Mac run (gate hold — see below)  
**FREEZE authority:** `~/AVE-staging/runs/shell-flux-ladder.md` (Math ACK 2026-10-06)  
**Plan:** `~/AVE-staging/runs/shell-flux-harness-plan.md`

---

## What was built

`src/scripts/verify/shell_flux_f1_harness.py` — measurement harness
implementing the FROZEN protocol from the proof ladder.

`src/tests/test_shell_flux_f1_harness.py` — unit tests (tol math, Q/A fit,
empty-grid sanity, force-stop classification, verdict logic with synthetic
Φ/Q/A).

---

## Gate hold

**No Mac run until:**
1. Engine Rigor Gate re-checks harness code vs FREEZE (ladder §Tolerance FROZEN, §Kill/pass/inconclusive FROZEN, §Force-stop criterion).
2. Orchestrator schedules run after #1062 green + merged.

Stricter-wins: if Gate or Math tightens constants, freeze updates supersede.

---

## FROZEN protocol implemented

| Item | Frozen value | Implemented in |
|------|-------------|----------------|
| Estimator | ball-sum Σ(−∂E/∂u) as 3-vector; IDW/surface = diagnostic only | `ball_sum_phi()` |
| Tol formula | k(N·F_max + C·ε·√N), k=3, C=6e³, ε=2⁻⁵² | `frozen_tol()` |
| F_max in tol | MEASURED after stop, not F_STOP | `measure_shell_flux()` |
| Force-stop | F_max < 1e-8 on ≥3 consecutive checks | `force_stop_relax()` |
| Energy-slope gate | >1%/100 steps at stop → INCONCLUSIVE | `compute_verdict()` |
| max_iter | ≥20k (caller can pass up to 50k) | `force_stop_relax()` default=20000 |
| Early-exit | untying (crossing count drop) | `force_stop_relax()` |
| Q/A fit | Φ_c(r) = Q_c + A_c·r³ per component; report always | `fit_qa()` |
| Verdict | PASS_F1 / KILL_F1 / INCONCLUSIVE / OUT_OF_SCOPE | `compute_verdict()` |
| PASS sufficient | \|Φ\|<tol all radii | `compute_verdict()` |
| Clean PASS | + \|Q\|<tol(r_min) + \|A\|r_max³<tol(r_max) | `compute_verdict()` notes |
| KILL | \|Q\|≫tol(r_min) (≥10× operationally) | `compute_verdict()`, `DEFAULT_KILL_RATIO=10` |
| Default grid | 64³ periodic, even edges | `make_engine_64_periodic()` |
| Knot | R=6, r=2 cold seed | `seed_cold_knot()` |
| Radii | {12, 18, 24} | `DEFAULT_RADII` |
| Seed fence | amplitude_scale=0.20 → peak \|ω\|/ω_yield ≈ 0.173 (<0.29) | `COLD_AMPLITUDE_SCALE` |
| Wrap control | 96³ / 128³ large-pad periodic | `make_engine_96_periodic()`, `make_engine_128_periodic()` |
| Empty-grid sanity | Φ~0 within float | `run_empty_grid_sanity()` |

**Not implemented in this ticket (out of scope):**
- Fixed far wall control (negative control only — not a pass path)
- Free/open exterior non-wrap stencil (requires engine-side flag; 96³/128³ large-pad is the available wrap-artifact discriminator per the FREEZE OR condition)
- IDW / surface quadrature verdict path

---

## Main-path discipline

`force_stop_relax()` is a harness-side loop that calls `energy_gradient()` and
`total_energy()` but does NOT modify `relax_to_ground_state()` defaults or any
engine parameter.  The harness runs entirely outside the main physics path — it
wraps, does not modify.

---

## Usage (Gate harness re-check)

```python
# Fast sanity (no run, zero state)
from src.scripts.verify.shell_flux_f1_harness import run_empty_grid_sanity
result = run_empty_grid_sanity()
assert result["passes_sanity"]

# Full measurement (BLOCKED until Gate ACK + Orchestrator schedule)
import src.scripts.verify.shell_flux_f1_harness as h
eng = h.make_engine_64_periodic()
h.seed_cold_knot(eng, R=6.0, r=2.0)
run = h.measure_shell_flux(eng, grid_desc="64³ periodic", max_iter=20000)
print(run.verdict, run.f_max, run.Q_norm, run.A_norm, run.notes)
```

```bash
# Unit tests only (no long sim)
PYTHONPATH=src /Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python \
    -m pytest src/tests/test_shell_flux_f1_harness.py -v
```

---

## Corpus pins

| Source | Ref | Role |
|--------|-----|------|
| PROOF-LADDER-shell-flux-zero | `runs/shell-flux-ladder.md` | FREEZE authority; tol formula, k=3, C=6e3, ε=2⁻⁵², force-stop criterion, verdict table, controls, seed fence |
| HARNESS-PLAN-shell-flux-F1 | `runs/shell-flux-harness-plan.md` | Build steps; logging requirements; explicit out-of-scope list |
| AVE-Core tip | `e78216ac` | Engine baseline: `relax_to_ground_state` (energy-stop, default max_iter=1000), `energy_gradient` (jax autodiff), stencil, defaults |
| Prior run (non-F1) | REPORT.md `charge-test-2026-10-03` | R26.100–102; leftover force ~27 at r=11 after energy-stop — NOT an F1 result |
