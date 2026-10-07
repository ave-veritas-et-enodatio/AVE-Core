# Shell-flux F1 harness — reference doc

**Date:** 2026-10-06 (fix pass 2026-10-07)
**Branch:** `fix/shell-flux-harness-gaps`
**Status:** G1–G12 gap fixes applied (fix pass FIX-BRIEF-PR1064-2026-10-07.md); NO Mac run (ruling INCONCLUSIVE + F1 FREEZE SUPERSEDED)
**Original FREEZE authority:** `~/AVE-staging/runs/shell-flux-ladder.md` (Math ACK 2026-10-06)
**Ruling:** `~/AVE-staging/runs/RULING-shell-flux-F1-run-02fc9794-2026-10-06.md`

---

## What was built

`src/scripts/verify/shell_flux_f1_harness.py` — measurement harness implementing the
FROZEN protocol from the proof ladder, with G1–G12 gap fixes from the ruling §5 and the
FIX-BRIEF-PR1064-2026-10-07.md corrections.

`src/tests/test_shell_flux_f1_harness.py` — unit tests (tol math, Q/A fit,
4-class partition (B0), empty-grid + identity sanity, force-stop classification,
RECEIPT_ONLY / IDENTITY_VIOLATION / INCONCLUSIVE / OUT_OF_SCOPE / MONOPOLE_DETECTED /
NO_MONOPOLE / CONTROL_FAIL verdict logic, vacuum-PASS trap, vacuum-box explicit check,
injected-force control, u-only convergence, untie tau tracking, fence boundary, platform line).

**4-class / 12-zero-mode property (c7):** the cf tetrahedral stencil has 4 independently
translatable classes (A sublattice all-even × FCC parity, B sublattice all-odd × FCC parity),
each with N_alive/4 sites. Per-class Σ∂E/∂u ≈ 1e-15 at a random state; shifting one class
rigidly leaves E exactly unchanged (dE < 1e-12·max(E,1), c7). This gives 12 translational
zero modes. The alive fraction is 1/4 (N_alive = N^3/4). Per-class projection eliminates
all 12 zero modes and allows the control to reach F_STOP = 1e-8.

---

## Gap fixes (G1–G12) — ruling §5

| Gap | Fix | File:line |
|-----|-----|-----------|
| G1 | Replaced private GD loop with `run_injected_force_control(engine, f0)` using `relax_u_only` with per-class projection. lr = 1/λ_max (λ_max(u) ≈ 3.318 at ω=0, measured c4). Reaches F_STOP = 1e-8 in ~327 steps on 32³ (9 s, c7). Expected value: exact closed form Φ(r) = −f0·(1−n_c(r)/N_c) (per-class equilibrium, c7). Verdict: MONOPOLE_DETECTED / NO_MONOPOLE / CONTROL_FAIL via pure `control_verdict()`. The "acoustic stall near 8e-7" was wrong: the floor was 3·f0/N_alive from 3 unprojected class-translation zero modes (c6); per-class projection reaches 1e-8. f0 = 1e-2 (not 1e-3). | `shell_flux_f1_harness.py: run_injected_force_control(), relax_u_only(), control_verdict(), alive_classes(), project_class_means(), _ball_mask()` |
| G2 | `_energy_slope_pct()` returns `Optional[float]` — `None` when history < window+1 or \|E_start\| < 1e-12; `compute_verdict` None → INCONCLUSIVE; `force_stop_relax` appends to energy_history on accepted steps only | `shell_flux_f1_harness.py: _energy_slope_pct(), compute_verdict(), force_stop_relax()` |
| G3 | `import jax; jax.config.update("jax_enable_x64", True)` at module top; `_build_platform_line(engine)` stored in `RunResult.platform_line` | `shell_flux_f1_harness.py:34-35, _build_platform_line()` |
| G4 | `RunResult` gains `energy_history`, `f_max_history`, `f_rms_history`, `crossing_history`, `lr_history`, `accepted` (booleans); `energy` = `total_energy()` at the final state (not E_history[-1]) | `shell_flux_f1_harness.py: RunResult dataclass, force_stop_relax()` |
| G5 | `run_empty_grid_sanity(radii=DEFAULT_RADII)` checks all three frozen radii {12,18,24} at 64³ periodic sat=True; returns per_radius list + passes_sanity; `run_identity_sanity()` tests random (u,ω) → global Σ(∂E/∂u) = 0 to ≤1e-12 | `shell_flux_f1_harness.py: run_empty_grid_sanity(), run_identity_sanity()` |
| G6 | `_measure_strain_metrics(engine)` computes measured max \|eps\|/eps_y, peak x, max A²; `measure_shell_flux` refuses if peak ≥ 0.41; `COLD_AMPLITUDE_SCALE=0.05` (measured 0.181 on 32³/64³, R=6/r=2, c5); `RunResult.seed_eps_ratio` = measured value; logs seed + stop metrics | `shell_flux_f1_harness.py: _measure_strain_metrics(), measure_shell_flux(), COLD_AMPLITUDE_SCALE` |
| G7 | `MAX_ITER = 20000` frozen constant; used as default in `force_stop_relax()` and `measure_shell_flux()`; stored in `RunResult.max_iter_used` | `shell_flux_f1_harness.py: MAX_ITER constant` |
| G8 | Untie exit requires `UNTIE_CONSEC_REQUIRED = 3` consecutive checks below c_init; logs iteration and τ at **every** crossing check (regardless of whether c < c_init) when verbose; appends `tau_history` and `check_iter_history` at every check; returns `tau_at_stop`, `iter_at_stop`, `tau_history`; RunResult gains these fields | `shell_flux_f1_harness.py: force_stop_relax() untie block` |
| G9 | Vacuum-PASS trap: force-stop passes require E ≥ 0.5·E_seed AND peak\|ω\| ≥ 0.5·peak_seed; otherwise INCONCLUSIVE('drained to vacuum'); explicit vacuum-box check: if E_seed ≤ 1e-12 → INCONCLUSIVE('no knot seeded (vacuum box)') | `shell_flux_f1_harness.py: compute_verdict() G9 block` |
| G10 | Retired PASS_F1/KILL_F1 for self-bound knot. `compute_verdict` returns RECEIPT_ONLY (all Φ<tol) or IDENTITY_VIOLATION (Φ≥tol — code/engine bug). Control returns MONOPOLE_DETECTED / NO_MONOPOLE / CONTROL_FAIL. Verdicts available: RECEIPT_ONLY / IDENTITY_VIOLATION / INCONCLUSIVE / OUT_OF_SCOPE / MONOPOLE_DETECTED / NO_MONOPOLE / CONTROL_FAIL | `shell_flux_f1_harness.py: Verdict enum, compute_verdict(), control_verdict()` |
| G11 | `force_stop_relax(u_only=True)` delegates entirely to `relax_u_only(engine, f_stop, max_iter)`. lr = 1/λ_max (λ_max(u) ≈ 3.318 at ω=0, 3.300 at A=0.05 seed, c4/c8). No energy line search, no lr growth. Safeguard: lr halved if F > 2×F_min for 3 consecutive iterations. Prior code's `lr → 1.0` switch diverged (F ≈ 0.95, c4); fixed lr converges monotonically in 465 steps on A=0.05 32³ seed (c8). | `shell_flux_f1_harness.py: relax_u_only(), force_stop_relax() u_only delegation` |
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
| Early-exit | untying: ≥3 consecutive checks below c_init; τ logged at every check | `force_stop_relax()` |
| Q/A fit | Φ_c(r) = Q_c + A_c·r³ per component; report always | `fit_qa()` |
| Verdict | RECEIPT_ONLY / IDENTITY_VIOLATION / INCONCLUSIVE / OUT_OF_SCOPE | `compute_verdict()` |
| Control verdict | MONOPOLE_DETECTED / NO_MONOPOLE / CONTROL_FAIL | `control_verdict()` |
| Φ receipt | \|Φ\|<tol all radii → RECEIPT_ONLY (code-identity, not physical test) | `compute_verdict()` |
| Φ violation | \|Φ\|≥tol at force-stop → IDENTITY_VIOLATION (code/engine bug) | `compute_verdict()` |
| Vacuum trap | E_stop < 0.5·E_seed or peak_ω < 0.5·peak_seed → INCONCLUSIVE | `compute_verdict()` G9 |
| Vacuum box | E_seed ≤ 1e-12 → INCONCLUSIVE 'no knot seeded' | `compute_verdict()` G9 |
| Seed fence | measured peak \|eps\|/eps_y < 0.41; REFUSE if ≥0.41 | `_measure_strain_metrics(), measure_shell_flux()` |
| Default grid | 64³ periodic, even edges | `make_engine_64_periodic()` |
| Knot | R=6, r=2 cold seed, A=0.05 | `seed_cold_knot()` |
| Radii | {12, 18, 24} | `DEFAULT_RADII` |
| Wrap control | 96³ / 128³ large-pad periodic | `make_engine_96_periodic()`, `make_engine_128_periodic()` |
| Empty-grid sanity | 64³ periodic, sat=True, Φ~0 at all DEFAULT_RADII | `run_empty_grid_sanity()` |
| Identity sanity | random (u,ω) → Σ(∂E/∂u) = 0 to ≤1e-12 | `run_identity_sanity()` |
| Injected-force control | per-class projection; f0 at center; Φ=−f0(1−n_c/N_c) | `run_injected_force_control()`, `relax_u_only()` |
| Platform banner | platform + backend + jax + x64 + dtypes | `_build_platform_line(), RunResult.platform_line` |

**Not implemented in this ticket (out of scope):**
- Independent σ·n surface-quadrature comparison (TODO marked in code; pending Math B2 — later PR)
- Free/open exterior non-wrap stencil
- u-only path in measure_shell_flux (parked pending Math B2)

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
ctrl = h.run_injected_force_control(eng, f0=(0, 0, 1e-2))
print(ctrl["verdict"], ctrl["Q_norm"])  # MONOPOLE_DETECTED, ~1e-2

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
| FIX-BRIEF-PR1064-2026-10-07 | `runs/gate-pr1064/FIX-BRIEF-PR1064-2026-10-07.md` | Fix pass: B0–B7 corrections (4-class zero modes, relax_u_only, IDENTITY_VIOLATION, NO_MONOPOLE, CONTROL_FAIL) |
| AVE-Core tip | `02fc9794` | Engine baseline at time of ruling |
