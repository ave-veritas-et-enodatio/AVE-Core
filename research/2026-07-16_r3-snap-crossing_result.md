# R3 — the destructive test: RESULT — NUMERICAL (frozen) + RECTIFIES-not-supported where stable (MIXED per the frozen scheme)

<!-- supersedes: "RESULT — NUMERICAL (frozen) + CLIPS-ONLY/null where stable" (2026-07-17 review repair, R-1: the frozen CLIPS-ONLY class requires R_rect<0.10, which every stable cell VIOLATES; the frozen fall-through is MIXED) -->

> **Post-review repair note (2026-07-17, PR#718):** the adversarial review confirmed 12 defect-class findings (all EVIDENCE-VOID / repair-and-bank; **no physics verdict flips**). This doc is repaired in place (Rule-12 supersession notes on every changed verdict-level sentence; the frozen prereg body is byte-untouched — see its appended POST-FREEZE AMENDMENTS). The RECTIFIES-not-supported physics and the named mechanism (anhysteretic kernel + velocity-coupling instability) bank unchanged; the repairs correct **class labels, verb scope, and the never-wired frozen drift bar**, not the substantive reading.

**Date:** 2026-07-16 · **Prereg (FROZEN, pushed before any driver):** [`2026-07-16_r3-snap-crossing_prereg_FROZEN.md`](2026-07-16_r3-snap-crossing_prereg_FROZEN.md) · **Driver:** [`src/scripts/vol_9_vacuum_datasheet/r3_snap_crossing.py`](../src/scripts/vol_9_vacuum_datasheet/r3_snap_crossing.py) · **Data:** [`2026-07-16_r3-snap-crossing_results.json`](2026-07-16_r3-snap-crossing_results.json) · **Charter cell:** hardware-ratings-map §2 **R3** (was UNRUN).

> **Verdict (frozen classes §2): NUMERICAL** at the frozen configuration; and where the integrator is stable, **RECTIFIES is NOT supported** — latched DC winding IS present but is **non-crossing-specific** (past/sub ratios **3.4** (Shape B) and **≈1.0** (Shape A) vs the frozen `RECT_RATIO=10`), so **no clean frozen class fires: MIXED per the frozen scheme.** The corpus "pair-production-as-AC→DC-rectification past snap" signature does NOT appear at engine scale on the shared_flux Cosserat harness: it is (a) instrument-blocked for the AC drive and (b) present-but-generic (not crossing-gated) where readable. Mechanism named (below). Rule-11 honest closure.
>
> <!-- supersedes: "where the integrator is stable, CLIPS-ONLY / null — RECTIFIES is NOT supported" (2026-07-17 review repair, R-1). The frozen CLIPS-ONLY class (prereg §2:66) fires only if R_rect(past) < RECT_FRAC=0.10 AND a measured clip-harmonic excess. Every stable cell VIOLATES R_rect<0.10 (Shape B 0.9985; Shape-A period-60 0.1564; period-200 0.4741) and clip_ratio was never measured at the stable corners (_probe() returns no clip_ratio). RECTIFIES also fails (ratio 3.4/≈1.0 < 10). The frozen fall-through that actually fires is MIXED. -->
> **Class-fire trace (frozen §2):** stable Shape-B crossing → `crossed✓, R_rect=0.998≥0.10✓, ratio=3.4<10✗` ⇒ RECTIFIES fails; `R_rect≥0.10` ⇒ CLIPS-ONLY fails ⇒ **MIXED**. Stable Shape-A corners → `ratio≈1.0<10` ⇒ RECTIFIES fails; `R_rect≥0.10` ⇒ CLIPS-ONLY fails ⇒ **MIXED**. No stable cell satisfies the frozen CLIPS-ONLY `R_rect<0.10` condition.

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
1. **The kernel is regularized: there is no true `S→0` wall in this harness.** The effective kernel-feedback floor is `S=0.141` — set by the `A_cap=0.99` clamp (`√(1−0.99²)=0.1411`), **not** `S_min=0.05`. The **field** `A` crosses 1 (to ~1.29) because leapfrog `V` is unclamped, while the **kernel feedback** `S` is floored at 0.141. So `c_eff` stays finite — **in this harness** there is no dynamical stiffening wall to reflect a drive; the `A_cap` clamp regularizes it, and an **unclamped kernel (true `S→0`) is untested** here.
2. **Consequently STALLS is UNADJUDICABLE in this harness:** with the kernel feedback floored at `S=0.141` by the `A_cap` clamp, the stiffening wall the STALLS class presumes never forms, and the soft source does not calibrate amplitude in any regime (the sub-snap soft control itself overshot to `A=6.7`, `e_growth≈145` = the blow-up bin). The soft drive overshoots freely (`A→10`, post-off energy growth order 10²–10³×); whether an unclamped `S→0` wall would stall a soft drive is **untested here**. (One empirical crumb survives: the hard-source field crossed to `A=1.29`, so the specific "engine enforces `A=1` as an asymptote" prediction is contradicted where readable — but that is a harness observation, not a falsification of the model's wall.) Amplitude is not a usable knob in soft mode; the amplitude-controlled probe is the **hard (Dirichlet)** source.

   <!-- supersedes: "Consequently the STALLS hypothesis is falsified in the opposite direction: a soft (current-injection) drive does NOT ceiling at A=1 (the wall does not reflect it) — it overshoots freely" (2026-07-17 review repair, R-2). Two scope breaks: (a) the no-wall is DERIVED from the A_cap=0.99 clamp, and the prereg's own frozen §0 rail says a null where the effect cannot exist is ARTIFACT not falsification; (b) the soft source failed calibration outright — the sub-snap soft control commanded A=0.8 but reached 6.728 (the doc itself calls it "invalid as a soft control"), and the A→10 overshoots carry e_growth 145–553, i.e. they ARE the NUMERICAL blow-up the charter calls INSTRUMENT. STALLS is therefore UNADJUDICABLE here, not falsified. -->


## §2 Numerical-health statement (the mechanism + convergence study, prereg §4)

**Mechanism isolated** (Shape B hard, A_peak=1.3, cfl0.4; metric `e_growth = max(E after source-off)/E(at source-off) − 1`, i.e. energy CREATED with no source = the clean instability signature; the `stable ⇔ e_growth < 0.5` label here is the **post-charter exploratory cut** — the frozen `5e-2` bar is re-adjudicated in §2b; the requires-BOTH conclusion holds at either bar):

The full 2×2 ablation (coupling {ON, OFF} × amplitude {past-crossing, sub-snap}):

| coupling | amplitude | e_growth | stable? |
|---|---|---|---|
| shared_flux ON | PAST (crosses A=1) | **8.38** | **UNSTABLE** |
| shared_flux ON | SUB (A=0.8) | 0.031 | stable |
| DECOUPLED (α₀=0) | PAST | 0.073 | stable |
| DECOUPLED (α₀=0) | SUB (A=0.8) | **0.0306** | stable |

**Ablation honesty (R-7 disclosure):** the earlier "forward-coupling PAST 0.073" row was **the same run as DECOUPLED PAST in disguise** — `ω` is zero-initialized AND unsourced in both the `α₀=0` and the `forward` modes, so both reduce to the identical uncoupled `V`-only run (`e_growth = 0.0734601027786197`, byte-identical to all digits). The strict fourth 2×2 cell (coupling-OFF × sub-snap: `α₀=0`, `A_peak=0.8`, Shape B hard, cfl0.4) was **unrun in the original matrix**; it was run + banked for this repair (`e_growth = 0.0306`, stable — reproduced independently). **The completed 2×2 confirms requires-BOTH:** only `coupling-ON × crossing` is unstable; all three off-diagonal/no-crossing cells are stable.

⇒ The instability requires **BOTH** the shared_flux bidirectional velocity coupling `α(V)·{V̇,ω̇}` **AND** the crossing. Since `α(V)=α₀(1−S(V))` engages (→~0.86) precisely as `A→1`, **the same E→T2 channel that would carry rectification is what destabilizes the integrator at the crossing.**

**dt-scaling (the convergence study):**
- **Shape B (DC push) — CFL-fixable:** `e_growth = 8.38 (cfl0.4) → 0.46 (0.2) → 0.031 (0.1) → 0.042 (0.05)`. Stable at `cfl≤0.2`.
- **Shape A (AC carrier) — dt-refinement does NOT cure it (at the frozen carrier):** `e_growth = 90 (cfl0.1) → 65 (0.05) → 72 (0.025)` and `R_rect = 2.10 → 0.47 → 0.002` does NOT converge across `dt 0.013→0.003`. This is a **non-CFL** instability of the explicit `(V−V_prev)/dt` velocity-coupling discretization under sustained AC drive (large `|V̇|`) — dt-refinement cannot cure it. It is **frequency-selective**, not literally unconditional: a fragile stable carrier corner exists (§3, `period 60`/`200`) — but even there no rectification appears.

**A blow-up is INSTRUMENT, not physics** (charter rail): the post-source-off energy growth is energy created with no source — a numerical artifact, reported as NUMERICAL, never as a physical rupture.

### §2b Frozen-tolerance re-adjudication (R-3 — the frozen drift bar the driver never wired)

The prereg froze `ENERGY_DRIFT_TOL = 5e-2` (§2 line 61) as the source-off NUMERICAL trigger. **The original driver never implemented it** — it minted `stable ⇔ e_growth < 0.5` (post-charter) + `BLOWUP_FACTOR=100` (post-charter) instead. Re-adjudicating every stable-labeled cell against the **frozen `5e-2` source-off drift bar**, using the ALREADY-BANKED `e_growth_frac` numbers (no re-runs), computed by `frozen_bar_readjudication()`:

| cell | banked e_growth | at frozen 5e-2 bar |
|---|---|---|
| `shared_flux_past` (crossing) | 8.378 | **NUMERICAL** |
| `decoupled_past` | 0.0735 | **NUMERICAL** at frozen bar |
| `forward_past` (= decoupled, see R-7) | 0.0735 | **NUMERICAL** at frozen bar |
| Shape B `cfl=0.2` | 0.4585 | **NUMERICAL** at frozen bar |
| **Shape B `cfl=0.1`** (past crossing) | **0.0310** | **SURVIVES** — the only frozen-stable crossing cell |
| Shape-A corners (period 60/200, past & sub) | 0.096 – 0.225 | **instrument-blocked** at frozen tolerance |

(The Shape-B `cfl=0.1` sub-twin 0.042 and the `cfl=0.05` refinement 0.042 also clear `5e-2`, so the Shape-B crossing regime is robustly the frozen-stable one; every Shape-A/AC corner fails it.)

**Consequence, stated plainly:** under the frozen bar the **AC (Shape-A) case is instrument-blocked everywhere — the AC null is unreadable at frozen tolerance.** The exploratory `0.5` cut (disclosed below) is retained as **EXPLORATION**, and **every §3 read from a cell that fails the frozen bar is downgraded to exploratory.** The one read that clears the frozen bar is the Shape-B (DC-push) crossing at `cfl≤0.1` — and its finding (RECTIFIES-not-supported: `R_rect` present but non-crossing-specific, past/sub 3.4 < 10) holds at the frozen bar. **The mechanism attribution survives either bar:** `shared_flux_past` 8.378 vs `decoupled_past` 0.073 is a **~114×** separation — the requires-BOTH conclusion is bar-independent.

**Deviations from the frozen method (post-charter instruments, R-3c disclosure):**
- `BLOWUP_FACTOR = 100` (`max|V| > 100·commanded ⇒ hard abort`) is a coarse NaN-precursor guard **minted after the freeze**; the frozen NUMERICAL trigger is `ENERGY_DRIFT_TOL`, not this.
- The `stable ⇔ e_growth < 0.5` cut (`STABLE_EXPLORATION_CUT`, driver `_probe()`) is **post-charter exploratory**, retained only for the dt-scaling narrative — NOT the frozen `5e-2` bar.
- **Drift-metric caveat (R-3d):** `E_int = ΣV² + Σω²` is a **field-norm proxy, not the Hamiltonian**, so kinetic↔potential sloshing can move it without energy creation — precisely in the `0.05–0.5` band where several corners sit. This is why the `5e-2`-failing / `0.5`-passing cells are read as *instrument-blocked* (unreadable), not as *physics-null*. Flagged as a spec item for the future implicit/symplectic instrument (§5).

## §3 Substantive physics reading — where the integrator IS stable: no crossing-specific rectification

Amplitude-controlled hard source at the stable dt (`cfl=0.1`):

- **Shape B (DC push), stable crossing:** `A=1.29`, `S_ker_min=0.141`, `R_rect(past)=0.998`, `persist=0.85`. A persistent DC winding DOES appear — **but this is a DC-in→DC-out linear transfer** (a unipolar push has non-zero `∮α(V)V̇` over the one-signed ramp), **not the AC→DC rectification claim**, and it is **not crossing-specific**: the sub-snap twin gives `R_rect=0.296` (a DC push at A=0.8 also drives DC ω), `past/sub = 3.4 < RECT_RATIO(10)`.
  - **Release-protocol scope (R-8 disclosure):** the shipped `_envelope` has **no ramp-down branch** — after the hold it steps the source hard OFF (`return 0.0`), so the crossing releases from `A≈1.29` as a **step**, not the prereg §3:83 "ramp down / source OFF over `N_relax`". So the `R_rect=0.998` / `persist=0.854` **Shape-B figures are release-protocol-specific** (step release); a **ramped** release is untested, and the doc's own `∮`-argument (§4) suggests a symmetric ramp would partially cancel the accumulated DC. The **past/sub RECTIFIES ratio (3.4) is release-robust** — both arms used the identical step release, so the ratio is not an artifact of the release shape.
  - **Clip-harmonic waiver (R-9 disclosure):** `_clip_ratio` is **undefined for the Shape-B DC push** (no fundamental → returns NaN), so the CLIPS-ONLY clip-harmonic evidence requirement is **waived for Shape B in code** (`or shape == "B"`, a reachability workaround). Consequently **no Shape-B verdict can be read as clip-harmonic-corroborated** — the Shape-B reading rests on `R_rect` + the past/sub ratio only.
- **Shape A (the AC rectification-proper test), stable corners** (at cfl0.1): `period 60` → past `R_rect=0.156`, sub `0.154`, **ratio 1.01**; `period 200` → past `0.474`, sub `0.519`, **ratio 0.91** (sub HIGHER). The sub-snap control shows EQUAL/MORE DC — so the small DC is **generic drive-transient, not a rectification product of the crossing**. RECTIFIES fails the frozen bar (`R_rect≥0.10 AND ratio≥10 AND persist≥0.5`) at every stable corner. **Frozen-bar caveat (§2b):** these Shape-A corners all FAIL the frozen `5e-2` drift bar (`e_growth 0.096–0.225`), so this AC read is **exploratory** — at frozen tolerance the AC null is unreadable, not a clean physics null.

**⇒ Reading: RECTIFIES is NOT supported — no clean frozen class fires, MIXED per the frozen scheme.** Latched DC is present at the stable Shape-B crossing but is **non-crossing-specific** (past/sub 3.4 < `RECT_RATIO=10`); the Shape-A corners show equal/more DC sub-snap (ratio ≈1). Neither satisfies the frozen CLIPS-ONLY condition (`R_rect < 0.10`), so the label is **MIXED**, not CLIPS-ONLY.

<!-- supersedes: "⇒ Reading: CLIPS-ONLY / null. RECTIFIES is NOT supported." (2026-07-17 review repair, R-1). Every stable cell has R_rect ≥ 0.10, which the frozen CLIPS-ONLY class forbids; the frozen fall-through is MIXED. -->
> **RECTIFIES-not-supported physics banks unchanged;** only the frozen class LABEL changes (CLIPS-ONLY → MIXED).

## §4 Why — the pre-test physics question, corroborated (Rule 11 / Rule 12)

The frozen pre-reg surfaced (pre-test-physics-check): *is "pair-production-as-rectification" a REMANENCE claim gated on the R10 loop, rather than a clipping claim the anhysteretic engine can carry?* The result corroborates the direction: rectification = a **latched (remanent)** DC winding; the canonical Ax-4 kernel `S(A)=√(1−A²)` is **anhysteretic** (zero enclosed loop area ⇒ no remanence — the R10 loop gap, `engine-capability-map.md §3.3`), and the `ω`-equation is **linear in ω**. A closed `V`-path has `∮α(V)dV=0`; a linear oscillator fed a zero-net-impulse source relaxes to `ω=0`. **So the analytic walk predicts the anhysteretic engine holds no ASYMPTOTIC remanence** — corroborated in direction by the runs: every observed DC is crossing-NONspecific (Shape-B past/sub = 3.4, Shape-A ratios ≈ 1), and the Shape-B window-persistent DC (`persist=0.85`) reads as a slow transient, not a latch (asymptotic relaxation untested; the walk also drops the `K_eff(V)` parametric term and the `α·ω̇` back-reaction). **Walk-level, not derived for the coupled system.**

<!-- supersedes: "So the engine structurally cannot latch a crossing-specific DC winding — CLIPS-ONLY/null is the expected, and observed, physics where the integrator survives." (2026-07-17 review repair, R-4). The pre-registered analytic prior was upgraded to a bolded structural theorem; it is a walk-level prediction (drops K_eff(V) and the α·ω̇ back-reaction; asymptotic relaxation untested), so it is reworded to walk-level. -->

**Register-liveness positive control (K2 knife):** the **Shape-B latch** (`R_rect=0.998`, `persist=0.85`) is the **positive control** for the ω-register — the register demonstrably HOLDS DC given a one-signed impulse, so the **Shape-A CLIPS-region null is not a dead-detector artifact.** The detector fires when there is DC to hold; the AC null is the register reporting no crossing-specific DC, not the register being unable to register.

**Retraction discipline (Rule 12 / A47 v11b):** the corpus RECTIFIES prediction is **retracted for this harness, not refilled**. The slot "R3 = rectification confirmed at engine scale" stays EMPTY. The R3 cell closes as **DRIVEN → NUMERICAL-at-default / RECTIFIES-not-supported-where-stable (MIXED per the frozen scheme)**; RECTIFIES not supported.

<!-- supersedes: "closes as DRIVEN → NUMERICAL-at-default / CLIPS-ONLY-where-stable" (2026-07-17 review repair, R-1). CLIPS-ONLY does not fire (R_rect ≥ 0.10 at every stable cell); the frozen fall-through is MIXED. -->


## §5 What a real R3 test needs (spec, not a retune)

1. **A stable instrument:** implicit / symplectic integration of the velocity coupling `α(V)·{V̇,ω̇}` (the explicit leapfrog is **unstable under sustained AC drive at the frozen carrier** — dt-refinement does not cure it; **frequency-selective**: fragile stable corners at period 60/200 exist but carry no rectification and fail the frozen drift bar). No amount of dt-refinement fixes the AC case at the frozen carrier.
2. **A remanence primitive:** RECTIFIES appears **gated on R10-loop** — a harness with a genuine loop/hysteresis (the anhysteretic canonical kernel deliberately lacks it). R3-positive likely requires R10 first.
3. **A conserving energy meter (R-3d spec item):** the current numerical-health metric `E_int = ΣV² + Σω²` is a **field-norm proxy, not the Hamiltonian** — kinetic↔potential sloshing can move it without energy creation, exactly in the `0.05–0.5` drift band that currently reads *instrument-blocked*. A real R3 instrument needs the **true conserved Hamiltonian** (or a symplectic invariant) as the drift meter so the frozen `5e-2` bar reads energy creation, not reactive sloshing — this would make the AC null readable at the frozen tolerance instead of instrument-blocked.

## §6 Flags for adjudication (surfaced, NOT resolved here — flag-don't-fix)

1. **Engine limitation (datasheet caveat):** `CosseratMasterEquationFDTD.step()` (shared_flux) is numerically unstable through the `A→1` crossing (default CFL) and under sustained AC drive at the frozen carrier (dt-refinement does not cure it). I did **not** modify the engine. Auditor/Grant to decide whether this is an engine-fix task or a documented limit. **Second datasheet caveat (R-5b):** `A_cap=0.99` clamps the kernel ARGUMENT only — the `V` field crosses `A=1` freely while the feedback saturates at `S=0.141`, so **this engine can never exhibit an amplitude barrier at `A=1`, only response-saturation**; wall-existence for an unclamped `S→0` is **out of this instrument's reach**.
2. **Cross-rating dependency:** R3-RECTIFIES appears **gated on R10-loop**. This is a ratings-map dependency edit — surfaced for the auditor to land, not drafted here.
3. **Pre-test physics question (Grant):** corroborated in direction — rectification IS a remanence claim on this engine. Standing for Grant's framing call.

---

*Figures (house-style WHITE; generated by the driver into `assets/sim_outputs/`, gitignored — reproducible, not committed binaries): `r3_snap_S_and_winding` (controlled crossing + post-off winding growth = the NUMERICAL signature); `r3_snap_reactance_pair` (C-state ΣV² / L-state ΣΦ_link²); `r3_snap_harmonics` (Shape-A odd-harmonic clipping spectrum); `r3_snap_dt_stability` (Shape-B CFL-fixable vs Shape-A non-CFL — dt-refinement does not cure — the numerical-health money figure).*

*Honest closure (Rule 11): a clean NUMERICAL-plus-null with the anhysteretic + velocity-coupling-instability mechanism named is the discipline at full strength — not a failure to debug around. No adjudication criterion was dropped post-hoc; no retune-to-rescue.*
