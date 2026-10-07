# Shell-flux F1 harness — reference doc

**Date:** 2026-10-06  
**Branch:** `fix/shell-flux-harness-gaps`  
**Status:** G1–G12 gap fixes applied; NO Mac run (ruling INCONCLUSIVE + F1 FREEZE SUPERSEDED)  
**Original FREEZE authority:** `~/AVE-staging/runs/shell-flux-ladder.md` (Math ACK 2026-10-06)  
**Ruling:** `~/AVE-staging/runs/RULING-shell-flux-F1-run-02fc9794-2026-10-06.md`

---

## What was built

`src/scripts/verify/shell_flux_f1_harness.py` — measurement harness implementing the
FROZEN protocol from the proof ladder, with G1–G12 gap fixes from the ruling §5.

`src/tests/test_shell_flux_f1_harness.py` — unit tests (tol math, Q/A fit,
empty-grid + identity sanity, force-stop classification, RECEIPT_ONLY / KILL / INCONCLUSIVE /
OUT_OF_SCOPE / MONOPOLE_DETECTED verdict logic, vacuum-PASS trap, injected-force control).

---

## Gap fixes (G1–G12) — ruling §5

| Gap | Fix | File:line |
|-----|-----|-----------|
| G1 | Replaced fixed-wall negative control with `run_injected_force_control(engine, f0)` — a live positive control that can fail; mean-subtraction fixes translation zero mode on periodic grid; `make_engine_32_periodic()` added for unit tests (64³ exceeds 300s test timeout); uses `F_STOP_CONTROL=1e-6` (not F_STOP=1e-8) because the K4 periodic alive mask has an acoustic long-wavelength mode that stalls gradient descent near 8e-7 — reachable in ~500 steps (~11s), sufficient for Q_norm within 1% of f0_norm | `shell_flux_f1_harness.py: run_injected_force_control(), make_engine_32_periodic(), F_STOP_CONTROL` |
| G2 | `_energy_slope_pct()` returns `Optional[float]` — `None` when history < window+1 or \|E_start\| < 1e-12; `compute_verdict` None → INCONCLUSIVE; `force_stop_relax` appends to energy_history on accepted steps only | `shell_flux_f1_harness.py: _energy_slope_pct(), compute_verdict(), force_stop_relax()` |
| G3 | `import jax; jax.config.update("jax_enable_x64", True)` at module top; `_build_platform_line(engine)` stored in `RunResult.platform_line` | `shell_flux_f1_harness.py:23-24, _build_platform_line()` |
| G4 | `RunResult` gains `energy_history`, `f_max_history`, `f_rms_history`, `crossing_history`, `lr_history`, `accepted` (booleans) | `shell_flux_f1_harness.py: RunResult dataclass, force_stop_relax()` |
| G5 | `run_empty_grid_sanity()` uses 64³ periodic + sat=True (matching knot-run factory); `run_identity_sanity()` tests random (u,ω) → global Σ(∂E/∂u) = 0 to ≤1e-12 | `shell_flux_f1_harness.py: run_empty_grid_sanity(), run_identity_sanity()` |
| G6 | `_measure_strain_metrics(engine)` computes measured max \|eps\|/eps_y, peak x, max A²; `measure_shell_flux` refuses if peak ≥ 0.41; logs seed + stop metrics in `RunResult` | `shell_flux_f1_harness.py: _measure_strain_metrics(), measure_shell_flux()` |
| G7 | `MAX_ITER = 20000` frozen constant; used as default in `force_stop_relax()` and `measure_shell_flux()`; stored in `RunResult.max_iter_used` | `shell_flux_f1_harness.py: MAX_ITER constant` |
| G8 | Untie exit requires `UNTIE_CONSEC_REQUIRED = 3` consecutive checks below c_init; logs iteration and τ at every check | `shell_flux_f1_harness.py: force_stop_relax() untie block` |
| G9 | Vacuum-PASS trap: force-stop passes require E ≥ 0.5·E_seed AND peak\|ω\| ≥ 0.5·peak_seed; otherwise INCONCLUSIVE('drained to vacuum'); floors `VACUUM_E_FLOOR_FRAC`, `VACUUM_OMEGA_FLOOR_FRAC` | `shell_flux_f1_harness.py: compute_verdict() G9 block` |
| G10 | Retired PASS_F1/KILL_F1 for self-bound knot; `compute_verdict(receipt_only=True)` returns `RECEIPT_ONLY`; TODO for σ·n surface quadrature marked in code | `shell_flux_f1_harness.py: Verdict.RECEIPT_ONLY, compute_verdict()` |
| G11 | `force_stop_relax(u_only=True)`: switches to grad-norm acceptance once F < `GRAD_NORM_SWITCH_F = 1e-6` | `shell_flux_f1_harness.py: force_stop_relax() G11 block` |
| G12 | Logs max \|∂E/∂ω\| at stop state; stored in `RunResult.max_dE_domega` | `shell_flux_f1_harness.py: force_stop_relax() G12 block` |

---

## FROZEN protocol implemented (updated)

| Item | Value | Implemented in |
|------|-------|----------------|
| Estimator | ball-sum Σ(−∂E/∂u) as 3-vector | `ball_sum_phi()` |
| Tol formula | k(N·F_max + C·ε·√N), k=3, C=6e³, ε=2⁻⁵² | `frozen_tol()` |
| F_max in tol | MEASURED after stop, not F_STOP | `measure_shell_flux()` |
| Force-stop | F_max < 1e-8 on ≥3 consecutive checks | `force_stop_relax()` |
| Energy-slope gate | >1%/100 ACCEPTED steps; None → INCONCLUSIVE | `compute_verdict(), _energy_slope_pct()` |
| MAX_ITER | 20000 (frozen, all grids) | `MAX_ITER`, `force_stop_relax()` |
| Early-exit | untying: ≥3 consecutive checks below c_init | `force_stop_relax()` |
| Q/A fit | Φ_c(r) = Q_c + A_c·r³ per component; report always | `fit_qa()` |
| Verdict | RECEIPT_ONLY / KILL_F1 / INCONCLUSIVE / OUT_OF_SCOPE / MONOPOLE_DETECTED | `compute_verdict()` |
| Φ receipt | \|Φ\|<tol all radii → RECEIPT_ONLY (code-identity, not physical test) | `compute_verdict(receipt_only=True)` |
| Vacuum trap | E_stop < 0.5·E_seed or peak_ω < 0.5·peak_seed → INCONCLUSIVE | `compute_verdict()` G9 |
| Seed fence | measured peak \|eps\|/eps_y < 0.41; REFUSE if ≥0.41 | `_measure_strain_metrics(), measure_shell_flux()` |
| Default grid | 64³ periodic, even edges | `make_engine_64_periodic()` |
| Knot | R=6, r=2 cold seed | `seed_cold_knot()` |
| Radii | {12, 18, 24} | `DEFAULT_RADII` |
| Wrap control | 96³ / 128³ large-pad periodic | `make_engine_96_periodic()`, `make_engine_128_periodic()` |
| Empty-grid sanity | 64³ periodic, sat=True, Φ~0 | `run_empty_grid_sanity()` |
| Identity sanity | random (u,ω) → Σ(∂E/∂u) = 0 to ≤1e-12 | `run_identity_sanity()` |
| Injected-force control | f0 at center site, u-only relax, Q≈f0_norm | `run_injected_force_control()` |
| Platform banner | platform + backend + jax + x64 + dtypes | `_build_platform_line(), RunResult.platform_line` |

**Not implemented in this ticket (out of scope):**
- Independent σ·n surface-quadrature comparison (TODO marked in code; pending Math B2 — later PR)
- Free/open exterior non-wrap stencil

---

## Main-path discipline

`force_stop_relax()` and `run_injected_force_control()` are harness-side loops that call
`energy_gradient()` and `total_energy()` but do NOT modify `relax_to_ground_state()`
defaults or any engine parameter.  The harness runs entirely outside the main physics path.

---

## Usage

```python
# Fast sanity (no run, zero state)
import shell_flux_f1_harness as h
assert h.run_empty_grid_sanity()["passes_sanity"]
assert h.run_identity_sanity()["passes"]

# Injected-force positive control (live control that can fail)
eng = h.make_engine_64_periodic()
ctrl = h.run_injected_force_control(eng, f0=(0, 0, 1e-3), radii=(3, 4, 5))
print(ctrl["verdict"], ctrl["Q_norm"])  # MONOPOLE_DETECTED, ~1e-3

# Full measurement (BLOCKED — F1 FREEZE SUPERSEDED per ruling)
eng = h.make_engine_64_periodic()
h.seed_cold_knot(eng, R=6.0, r=2.0)
run = h.measure_shell_flux(eng, grid_desc="64³ periodic")
print(run.verdict, run.platform_line, run.notes)
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
| PROOF-LADDER-shell-flux-zero | `runs/shell-flux-ladder.md` | Original FREEZE authority (SUPERSEDED by ruling) |
| RULING-shell-flux-F1-run-02fc9794 | `runs/RULING-shell-flux-F1-run-02fc9794-2026-10-06.md` | Gate ruling; G1–G12 gap specs; overall stamp INCONCLUSIVE + F1 FREEZE SUPERSEDED |
| AVE-Core tip | `02fc9794` | Engine baseline at time of ruling |
