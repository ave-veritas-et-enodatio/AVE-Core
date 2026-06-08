# Prereg: unified amplitude–Γ–retention sweep (calibration crux)

**Status:** FROZEN PREREG before driver run.
**Branch:** `analysis/2026-06-07-two-node-alpha-projection`.
**Driver:** `src/scripts/vol_1_foundations/unified_amplitude_gamma_sweep.py`.
**Parent:** `research/2026-06-07_electron-genesis-observer-bridge-prereg.md` §10.

---

## §0 Question

On the unified `MasterEquationFDTD + PhasorBridge` lane, does any alpha-free sech seed amplitude simultaneously:

1. form a short bond wall (`Γ` strongly negative), and
2. retain bounded trapped energy (no parametric pump / blow-up)?

This is the substrate-native test of **FORK A (calibration crux)**: rest-energy-sized seeds vs saturation-self-shorting seeds.

## §1 Corpus prior work

- `phase5_optionD_under_reflective_confinement` (coupled K4+Cosserat): at 1× rest-calibrated impose, `Γ≈−0.03` (matched bulk); at 4×, `Γ_min≈−0.994` but energy pumps to 10⁴–10⁷×. **No amplitude window with wall + bounded energy.**
- Unified projection bridge (2026-06-07): amplitude `0.85` gives `Γ_min≈−0.006`, `A_peak≈0.53`, L1 trapping passes.
- Orchestration `2026-06-06_genesis-next-steps-scope.md` §8–9: emergent wall exists in K4-TLM; blocker is amplitude/calibration, not wall absence.

## §2 Prediction before run

**Primary prediction:** No single amplitude in `[0.2, 4.0]` simultaneously satisfies `Γ_min ≤ −0.5` and `energy_growth_ratio ≤ 10` with L1 trapping. The wall and bounded confinement occupy disjoint amplitude bands — reproducing the option-D tension on the scalar unified lane.

**Secondary prediction:** A monotonic trend — `Γ_min` becomes more negative as seed amplitude increases, while `energy_growth_ratio` increases super-linearly past `A_peak ≈ 0.85`.

## §3 Inputs / forbidden inputs

Allowed:

- `MasterEquationFDTD` leapfrog dynamics (unchanged).
- `MasterFDTDPhasorBridge` read-only projection.
- Sech blob seeds at amplitudes `{0.20, 0.35, 0.48, 0.65, 0.85, 1.00, 1.25, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00}`.
- Reference amplitude `0.48` ≈ `√(0.23)` for rest-energy strain scale tag (comparison label only).

Forbidden:

- `alpha` as damping, Q target, threshold, or fitted normalization.
- Nelder-Mead / curve_fit against `137` or `4π`.

## §4 Measured observables (per amplitude)

| Observable | Definition |
|---|---|
| `A_peak_max` | max `|V|/V_yield` over full run |
| `gamma_min_shell` | min bond `Γ` on sites with `|V| ≥ 0.1·A_peak_max` |
| `gamma_min_center` | min `Γ` at center bond (port 0) post-transient |
| `energy_growth_ratio` | `max(E)/E_initial` |
| `energy_retained_fraction` | `E_final / max(E)` |
| `l1_trapping_pass` | same conservative criterion as observer bridge |
| `bounded_pass` | `energy_growth_ratio ≤ 10` and finite fields |
| `wall_pass` | `gamma_min_shell ≤ −0.5` |
| `window_pass` | `wall_pass ∧ bounded_pass ∧ l1_trapping_pass` |

Alpha (`137`, `4π`) imported for comparison labels only in JSON output.

## §5 Classification

| Outcome | Criterion |
|---|---|
| **A — window found** | ≥1 amplitude with `window_pass` |
| **B — disjoint bands** | some `wall_pass`, some `bounded_pass`, none `window_pass` |
| **C — no wall** | no amplitude reaches `wall_pass` |
| **D — no trap** | no amplitude passes `l1_trapping_pass` |

## §6 Discrimination

- Outcome A would falsify the primary prediction and reopen genesis at the impose amplitude.
- Outcome B confirms calibration crux on the unified lane (wall vs boundedness trade-off).
- Outcome C would indicate polarity/projection issue on scalar bridge (unexpected).
- Outcome D would indicate Master Equation cannot host localized states at tested amplitudes (unlikely).

---

## §7 Result

Executed with:

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/unified_amplitude_gamma_sweep.py
```

Output: `src/scripts/vol_1_foundations/_output/unified_amplitude_gamma_sweep_results.json`

## §8 Adjudication

**Verdict (capped observer — load-bearing): `CALIBRATION_CRUX_NO_CAPPED_WINDOW`.**

The engine-matching **capped-Γ observer (`A_cap = 0.99`)** reaches **Outcome C — no wall**: deepest `Γ_min ≈ −0.4253` at amplitudes ≥ 3.0, never crossing the `−0.5` wall threshold (`wall_pass = false`, `window_pass = false`). This is the load-bearing result and the headline. The uncapped-Γ observer's apparent window at `Γ_min ≈ −0.61` (amplitudes 3.0–4.0) is a **full-strain diagnostic artifact** that the engine never realizes — see below; do not headline the uncapped −0.61.

> Superseded headline label (for audit-trail continuity): `CALIBRATION_CRUX_WINDOW_UNCAPPED_OBSERVER`. It elevated the uncapped-observer window and is corrected here — the capped observer is the one that matches engine numerics.

### Capped-Γ observer (A_cap = 0.99, matches engine numerics)

- **Outcome C — no wall:** `Γ_min` saturates near **−0.43** at amplitudes ≥ 3.0; never reaches the `−0.5` wall threshold.
- All 13 amplitudes: `bounded_pass` (energy growth ≤ 1.02×), no NaNs.
- Rest-scale amplitude `0.48` (`A²_peak ≈ 0.23`): `Γ_min ≈ −0.005`, matched bulk.

### Uncapped-Γ observer (full strain for diagnostic z_local only)

- **Outcome A at high amplitude:** amplitudes **3.0, 3.5, 4.0** pass `window_pass_uncapped`:
  - `Γ_min` ∈ **[−0.61, −0.49]**
  - `energy_growth_ratio ≈ 1.0`
  - `l1_trapping_pass = True`
- No amplitude below **2.5** forms a short wall under uncapped observer.

### Interpretation (honest)

1. **Primary prediction falsified on the scalar unified lane** when Γ is computed from full strain. A bounded wall+trap window exists, but only at **~6–8× rest-energy amplitude** (`0.48` → `3.0+`), not at the calibrated rest scale.
2. **Secondary prediction confirmed:** `Γ_min` monotonically strengthens with amplitude; no parametric pump on `MasterEquationFDTD` (unlike coupled option-D at 4×).
3. **Observer-definition split:** the engine's `A_cap = 0.99` clipping homogenizes saturated-core `z_local`, capping observed `Γ` near −0.43. Wall detection is sensitive to whether the observer respects the engine cap.
4. **Not genesis closure:** planted sech seeds, scalar lane only, no `(2,3)` impose, no L5 Q measurement, no α claim.

### Next targets

1. Re-run the same sweep on **native K4-TLM + saturation** (not projection) to test whether pumping reappears in the window band.
2. ~~L5 alpha-free Q/leakage on unified lane~~ → **DONE** (`research/2026-06-07_unified-l5-q-leakage-prereg.md`, verdict `L5_NEGATIVE_BOTH`).
3. C3 phase-gate re-run on coupled impose harness (FORK D).
