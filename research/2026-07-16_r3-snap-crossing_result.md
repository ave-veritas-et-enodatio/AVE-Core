# R3 — the destructive test: RESULT — NUMERICAL (frozen) + CLIPS-ONLY/null where stable

**Date:** 2026-07-16 · **Prereg (FROZEN, pushed before any driver):** [`2026-07-16_r3-snap-crossing_prereg_FROZEN.md`](2026-07-16_r3-snap-crossing_prereg_FROZEN.md) · **Driver:** [`src/scripts/vol_9_vacuum_datasheet/r3_snap_crossing.py`](../src/scripts/vol_9_vacuum_datasheet/r3_snap_crossing.py) · **Data:** [`2026-07-16_r3-snap-crossing_results.json`](2026-07-16_r3-snap-crossing_results.json) · **Charter cell:** hardware-ratings-map §2 **R3** (was UNRUN).

> **Verdict (frozen classes §2): NUMERICAL** at the frozen configuration; and where the integrator is stable, **CLIPS-ONLY / null — RECTIFIES is NOT supported.** The corpus "pair-production-as-AC→DC-rectification past snap" signature does NOT appear at engine scale on the shared_flux Cosserat harness: it is (a) instrument-blocked for the AC drive and (b) absent where readable. Mechanism named (below). Rule-11 honest closure.

---

## Sector header + coordinate/class discipline (as frozen)

- **DRIVE = E-sector** (longitudinal scalar `V`). **PREDICTED PRODUCT = T2 Cosserat winding** (`ω`; rectified DC winding = persistent net `Φ_ω`). The observable IS the cross-sector transfer E→T2 (coupling `α(V)=α₀(1−S(V))`, engages only as `A→1`).
- **Coordinate (A46):** measured in the engine-native `A=V/V_yield` and the T2 registers (`ω`, `Φ_ω`, `Φ_link`), NOT an SI 511 kV target. The kernel rupture root `A=1` sits at `V=V_yield` in this engine's macroscopic normalization; `V_snap=511 kV=V_yield/√α` and `V_yield=43.65 kV` are the two SI anchors of the same dimensionless `r=1.0` boundary.
- **Class (A47):** CONSISTENCY (does the frozen engine MANIFEST the asserted rectification at the rupture root?). No CODATA target; no value derived. **BENCH-∅** — model absolute-maximum behavior only; the real vacuum's snap is Schwinger-scale.

---

## §1 The frozen-matrix verdict: NUMERICAL

The frozen 5-run matrix + convergence pair (cfl 0.4 primary vs 0.2) at `N=48`, `pml=6`, `V_yield=1`:

| run | A_src_max | S_ker_min | note |
|---|---|---|---|
| shapeB_past_hard (controlled) | **1.20** | 0.141 | field crosses A=1 cleanly |
| shapeA_past_soft | 10.4 | 0.141 | soft current-drive OVERSHOOTS (no wall to reflect it) |
| shapeB_sub_soft ("control") | 6.7 | 0.141 | soft "sub-snap" also overshoots → invalid as a soft control |

**Convergence FAILS** (frozen NUMERICAL trigger, `CONV_TOL=0.20`): base(cfl0.4) vs dt/2(cfl0.2) — `R_rect` frac-change **15.2**, `A_src_max` frac-change **0.79**; base vs grid-refine — `R_rect` frac-change **11.8**. Both drive shapes ⇒ **NUMERICAL**.

**Two instrument facts this exposes:**
1. **The kernel is regularized: there is no true `S→0` wall.** The effective kernel-feedback floor is `S=0.141` — set by the `A_cap=0.99` clamp (`√(1−0.99²)=0.1411`), **not** `S_min=0.05`. The **field** `A` crosses 1 (to ~1.29) because leapfrog `V` is unclamped, while the **kernel feedback** `S` is floored at 0.141. So `c_eff` stays finite — there is no dynamical stiffening wall to reflect a drive.
2. **Consequently the STALLS hypothesis is falsified in the opposite direction:** a soft (current-injection) drive does NOT ceiling at `A=1` (the wall does not reflect it) — it **overshoots freely** (`A→10`, post-off energy growth order 10²–10³×). Amplitude is not a usable knob in soft mode; the amplitude-controlled probe is the **hard (Dirichlet)** source.

## §2 Numerical-health statement (the mechanism + convergence study, prereg §4)

**Mechanism isolated** (Shape B hard, A_peak=1.3, cfl0.4; metric `e_growth = max(E after source-off)/E(at source-off) − 1`, i.e. energy CREATED with no source = the clean instability signature; `stable ⇔ e_growth < 0.5`):

| configuration | e_growth | stable? |
|---|---|---|
| shared_flux, PAST (crosses A=1) | **8.38** | **UNSTABLE** |
| shared_flux, SUB (A=0.8, same coupling) | 0.031 | stable |
| DECOUPLED (α₀=0), PAST | 0.073 | stable |
| forward-coupling, PAST | 0.073 | stable |

⇒ The instability requires **BOTH** the shared_flux bidirectional velocity coupling `α(V)·{V̇,ω̇}` **AND** the crossing. Since `α(V)=α₀(1−S(V))` engages (→~0.86) precisely as `A→1`, **the same E→T2 channel that would carry rectification is what destabilizes the integrator at the crossing.**

**dt-scaling (the convergence study):**
- **Shape B (DC push) — CFL-fixable:** `e_growth = 8.38 (cfl0.4) → 0.46 (0.2) → 0.031 (0.1) → 0.042 (0.05)`. Stable at `cfl≤0.2`.
- **Shape A (AC carrier) — UNCONDITIONAL:** `e_growth = 90 (cfl0.1) → 65 (0.05) → 72 (0.025)` and `R_rect = 2.10 → 0.47 → 0.002` does NOT converge across `dt 0.013→0.003`. This is anti-damping of the `(V−V_prev)/dt` velocity-coupling discretization under sustained AC drive (large `|V̇|`) — a non-CFL instability that dt-refinement cannot cure.

**A blow-up is INSTRUMENT, not physics** (charter rail): the post-source-off energy growth is energy created with no source — a numerical artifact, reported as NUMERICAL, never as a physical rupture.

## §3 Substantive physics reading — where the integrator IS stable: no rectification

Amplitude-controlled hard source at the stable dt (`cfl=0.1`):

- **Shape B (DC push), stable crossing:** `A=1.29`, `S_ker_min=0.141`, `R_rect(past)=0.998`, `persist=0.85`. A persistent DC winding DOES appear — **but this is a DC-in→DC-out linear transfer** (a unipolar push has non-zero `∮α(V)V̇` over the one-signed ramp), **not the AC→DC rectification claim**, and it is **not crossing-specific**: the sub-snap twin gives `R_rect=0.296` (a DC push at A=0.8 also drives DC ω), `past/sub = 3.4 < RECT_RATIO(10)`.
- **Shape A (the AC rectification-proper test), stable corners** (at cfl0.1): `period 60` → past `R_rect=0.156`, sub `0.154`, **ratio 1.01**; `period 200` → past `0.474`, sub `0.519`, **ratio 0.91** (sub HIGHER). The sub-snap control shows EQUAL/MORE DC — so the small DC is **generic drive-transient, not a rectification product of the crossing**. RECTIFIES fails the frozen bar (`R_rect≥0.10 AND ratio≥10 AND persist≥0.5`) at every stable corner.

**⇒ Reading: CLIPS-ONLY / null. RECTIFIES is NOT supported.**

## §4 Why — the pre-test physics question, corroborated (Rule 11 / Rule 12)

The frozen pre-reg surfaced (pre-test-physics-check): *is "pair-production-as-rectification" a REMANENCE claim gated on the R10 loop, rather than a clipping claim the anhysteretic engine can carry?* The result corroborates the direction: rectification = a **latched (remanent)** DC winding; the canonical Ax-4 kernel `S(A)=√(1−A²)` is **anhysteretic** (zero enclosed loop area ⇒ no remanence — the R10 loop gap, `engine-capability-map.md §3.3`), and the `ω`-equation is **linear in ω**. A closed `V`-path has `∮α(V)dV=0`; a linear oscillator fed a zero-net-impulse source relaxes to `ω=0`. So the engine **structurally cannot latch a crossing-specific DC winding** — CLIPS-ONLY/null is the expected, and observed, physics where the integrator survives.

**Retraction discipline (Rule 12 / A47 v11b):** the corpus RECTIFIES prediction is **retracted for this harness, not refilled**. The slot "R3 = rectification confirmed at engine scale" stays EMPTY. The R3 cell closes as **DRIVEN → NUMERICAL-at-default / CLIPS-ONLY-where-stable**; RECTIFIES not supported.

## §5 What a real R3 test needs (spec, not a retune)

1. **A stable instrument:** implicit / symplectic integration of the velocity coupling `α(V)·{V̇,ω̇}` (the explicit leapfrog is unconditionally unstable under AC drive). No amount of dt-refinement fixes the AC case.
2. **A remanence primitive:** RECTIFIES appears **gated on R10-loop** — a harness with a genuine loop/hysteresis (the anhysteretic canonical kernel deliberately lacks it). R3-positive likely requires R10 first.

## §6 Flags for adjudication (surfaced, NOT resolved here — flag-don't-fix)

1. **Engine limitation (datasheet caveat):** `CosseratMasterEquationFDTD.step()` (shared_flux) is numerically unstable through the `A→1` crossing (default CFL) and unconditionally under AC drive. I did **not** modify the engine. Auditor/Grant to decide whether this is an engine-fix task or a documented limit.
2. **Cross-rating dependency:** R3-RECTIFIES appears **gated on R10-loop**. This is a ratings-map dependency edit — surfaced for the auditor to land, not drafted here.
3. **Pre-test physics question (Grant):** corroborated in direction — rectification IS a remanence claim on this engine. Standing for Grant's framing call.

---

*Figures (house-style WHITE; generated by the driver into `assets/sim_outputs/`, gitignored — reproducible, not committed binaries): `r3_snap_S_and_winding` (controlled crossing + post-off winding growth = the NUMERICAL signature); `r3_snap_reactance_pair` (C-state ΣV² / L-state ΣΦ_link²); `r3_snap_harmonics` (Shape-A odd-harmonic clipping spectrum); `r3_snap_dt_stability` (Shape-B CFL-fixable vs Shape-A unconditional — the numerical-health money figure).*

*Honest closure (Rule 11): a clean NUMERICAL-plus-null with the anhysteretic + velocity-coupling-instability mechanism named is the discipline at full strength — not a failure to debug around. No adjudication criterion was dropped post-hoc; no retune-to-rescue.*
