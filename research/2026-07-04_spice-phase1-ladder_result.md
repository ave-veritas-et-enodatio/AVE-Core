# SPICE PHASE-1 — the validation ladder, live for the first time

**Date:** 2026-07-04
**Branch:** `analysis/spice-phase1` (off `origin/main`, HEAD `2a7d01dc`)
**Commissioned:** Grant, 2026-07-04 — SPICE PHASE-1. ngspice is now installed
(`/opt/homebrew/bin/ngspice`, **ngspice-46**); the SPICE-lane charter's named
limitation ("ngspice itself did NOT run") is lifted.
**Charter:** [`_orchestration/2026-07-03_spice-lane-charter.md`](../_orchestration/2026-07-03_spice-lane-charter.md)
STEP 4 (the five-rung validation ladder).
**Engine hook:** [`src/ave/bench/spice_runner.py`](../src/ave/bench/spice_runner.py)
— the thin `ngspice -b` subprocess wrapper this ladder introduced (the lane
was emit-only before today).
**Committed artifacts:** `src/scripts/vol_4_engineering/spice_ladder_artifacts/`
(one `.cir` + JSON per rung); transient `.dat` scratch in the gitignored
`_output/spice_ladder/`.

---

## What this is

The SPICE lane was chartered emit-only: a netlist compiler + a canonical
`.lib` that **had never been parsed by a SPICE engine** (charter §1). This note
records the first live runs — the five-rung *validate-on-known* ladder that
qualifies the lane before it may cross-check anything. Each rung states an
**analytic target**, the **ngspice-measured** value, and the **recovery
error**. The ladder has a **HALT-gate**: a rung failing its analytic target
stops the ladder (report, don't paper over).

**ngspice version used:** `ngspice-46` (Compiled with KLU Direct Linear Solver).

**ngspice-46 batch-mode contract (established empirically this session).**
`.AC` / `.TRAN` analyses under `-b` produce *no output* and error
"no simulations run" unless the netlist carries an explicit
`.control … run … .endc` block with a `wrdata` / `print` directive. Bare `.OP`
+ `.END` prints the operating point automatically. All rung drivers emit a
`.control` block and export data via `wrdata`. This is a real ngspice-46
invocation fact the emit-only lane never had to satisfy.

---

## Ladder result table

| Rung | Test | Analytic target | ngspice measured | Rel. error | Tol | Class | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | RC transient (τ=RC) | τ = 1.000000e-3 s | 1.000000e-3 s | 1.21e-7 | 2e-2 | consistency | ✅ PASS |
| 1 | LC transient (f_res) | f_res = 5032.92 Hz | 5039.67 Hz | 1.34e-3 | 2e-2 | consistency | ✅ PASS |
| 2 | AVE_VACUUM_CELL Ax4 C(V) vs kernel | _pending_ | | | | manifestation | ⏳ |
| 3 | Poisson `.OP` vs numpy MNA / Laplacian (real ngspice) | _pending_ | | | | consistency | ⏳ |
| 4 | 1D LC-chain dispersion ω(k) | _pending_ | | | | manifestation | ⏳ |
| 5 | Biased-chain small-signal shift vs S(A) | _pending_ | | | | consistency (DC→AC) | ⏳ |

---

## Rung 1 — RC/LC analytic transients

**Driver:** [`src/scripts/vol_4_engineering/spice_ladder_rung1_rc_lc_transient.py`](../src/scripts/vol_4_engineering/spice_ladder_rung1_rc_lc_transient.py)
· **Artifacts:** `spice_ladder_rung1_{rc,lc}.cir`, `spice_ladder_rung1_result.json`

**Purpose.** The engine floor: does ngspice parse + integrate our netlists
correctly, before any AVE constitutive law is exercised? Class **consistency**
(engine-integrates-a-known-analytic-circuit). No substrate DOF is claimed; the
RC / LC cells are standard lumped elements whose scalar treatment is exactly
correct (a known-analytic calibration, not a substrate measurement — the
substrate-native-check checkpoint is deliberately a no-op here, and that is the
honest answer for a linear-QA rung).

**(a) RC charging.** 1 V step into series R = 1 kΩ, C = 1 µF; the cap voltage
follows `V_C(t) = V0(1 − e^{−t/RC})`. τ recovered from the 63.2% (1 − 1/e)
crossing (linearly interpolated).
- Target τ = RC = **1.000000e-3 s**; measured **1.000000e-3 s**;
  rel-error **1.21e-7** (tol 2e-2). **PASS.**

**(b) LC oscillation.** Undamped LC tank (L = 1 mH, C = 1 µF, cap pre-charged
to 1 V via `IC`) rings at `f_res = 1/(2π√(LC))`. f_res recovered from the
Hann-windowed FFT peak with parabolic sub-bin interpolation.
- Target f_res = **5032.92 Hz**; measured **5039.67 Hz**; rel-error
  **1.34e-3** (tol 2e-2). **PASS.**

**Rung-1 verdict: PASS.** ngspice-46 parses and time-integrates the netlists
to well within the discretization tolerance. The lane's engine floor holds.

---

## Empirical-driver-discipline finding (Rule 10) — surfaced at first live parse

The instant ngspice actually parsed the canonical `.lib`
(`src/ave/solvers/spice_models/ave_vacuum_cell.lib`), a real syntax bug that
skip-gating + static analysis had masked fired: the `AVE_MEMRISTOR_S_STATE`
subcircuit had its capacitor initial condition on a **standalone line**:

```
C_S N_S 0 1
IC=1
```

ngspice-46 parses the bare `IC=1` as a *new element* named `IC` → fatal
`"Not enough parameters for i source"`. Fixed to the inline
initial-condition form `C_S N_S 0 1 IC=1` (mechanical ngspice-syntax fix,
in-lane, not a physics adjudication). This is the exact Rule-10 case: a bug
that only manifests at integrator time, invisible while the tests were
ngspice-gated to skip. Recorded here so the fix's lineage is auditable.

**Pre-existing SPICE test-harness gap (flagged, not silently fixed).** Beyond
the `IC=1` bug, several pre-existing tests in `src/tests/test_spice_vacuum_cell.py`
build `.AC` / `.TRAN` netlists that terminate in a bare `.END` with no
`.control`/`.print` — which ngspice-46 batch mode rejects with "no simulations
run". These are pre-existing test-harness netlists (not part of the five-rung
deliverable); the harness fix is folded into the rung-2 commit (which is the
`.lib` validation rung and the natural home for the test-harness repair).
