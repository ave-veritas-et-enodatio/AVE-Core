# RESULT — S11 de-novo (v6 MADE object): gate PASS but the operating window is SUB-PERIOD at the made object's scale — both legs **UNRESOLVED** (apparatus-floor), demoted from the driver-emitted NO-RESPONSE; no mirror claim, no Q, no α

**Date:** 2026-06-11 · **Branch:** `analysis/2026-06-11-s11-de-novo`
**Prereg (FROZEN, committed ALONE first):** [`2026-06-11_s11-de-novo_prereg.md`](2026-06-11_s11-de-novo_prereg.md) (commit `bd218d13`, before any run artifact)
**Engine:** [`src/ave/core/s11_probe_unified.py`](../src/ave/core/s11_probe_unified.py) `S11ProbeUnified(UnifiedGenesisEngine)` — the FLAG-B re-layer on the ACTUAL v6 engine ·
**Driver:** [`src/scripts/vol_9_device/s11_de_novo_sweep.py`](../src/scripts/vol_9_device/s11_de_novo_sweep.py) (committed AS-RUN — see §4.2 KEEP-BOTH)
**Data:** `src/scripts/vol_9_device/_output/s11_denovo_results.json` · **Figures:** `s11_denovo_gate.png`, `s11_denovo_made.png`, `s11_denovo_planted.png`, `s11_denovo_paired.png` · run log archived from `/tmp/ave-s11denovo-run.log` (elapsed 3110 s)
**Governing discipline:** `ave-apparatus-floor-attribution` (probe-capability gate + ORDERED bins; "the floor-check gates the rest", prereg §6). Skills: substrate-native-check, ave-prereg, phase-space-coordinate-check, ave-representation-capability-check, ave-driver-script-honesty, consistency-vs-emergence, ave-regime-phase-state-check, verify-before-cite.
**Adversarial panel:** PROBE-ATTRIBUTION lens audited the finished artifacts — `refuted=true` on the driver-emitted bin; demotion executed here (§4.2). A second panel lens (rebuild-fidelity) was truncated in the orchestration handoff and is NOT incorporated (§7.6).

---

## 0. VERDICT (ordered: GATE first, then the legs)

> **KNOWN-NULL — PASS.** `S11ProbeUnified` with the probe off is **byte-identical** to `UnifiedGenesisEngine` over 200 full-v6 steps: max|diff| = 0.000e+00 on ALL five sectors (V, omega, w, rho_bar, u_adv). The re-layer probes the actual v6 made object with inherited physics unchanged.
>
> **GATE — PASS, with a SCOPE LIMIT that decides the verdict.** Re-run IN the unified engine (a V2 #166 gate PASS does not transfer): the lock-in recovers KNOWN ω mass-gap resonators (analytic f₀ = ω₀/2π = 0.1592 cyc/time) to **f₀ within 0.37%/0.31% and Q within 1.04%/0.99%** at Q=5 and Q=10 — inside the frozen ±5%/±20%. V-channel amplitude linearity ON the made object (×8 span, NET response): **R² = 1.0000000, intercept_rel = 8.4e-7** — closes #166 FLAG-5. **BUT** the gate certified the instrument at dt = 0.0387 with a 1100-step window = **6.8 periods** of the known f₀; the unknown was then measured at the made object's CFL dt = 1.732e-3 with an 800-step window = **0.067 periods** of its ring-down f₀ (planted leg: 0.033). The gate PASS does not extend to a sub-period window (prereg's own rule, §5: "a floor from a different config is invalid").
>
> **MADE leg — UNRESOLVED (apparatus-floor).** Driver-emitted raw bin was NO-RESPONSE (net never clears the median+3σ MAD floor: peak 1.57e-3 vs floor 2.60e-3, 0.60×). DEMOTED per panel + prereg §6: across the entire swept band the lock-in integrates only **0.022–0.20 periods of the drive** — a single-frequency lock-in cannot frequency-discriminate with a sub-period window, so "never clears the floor" attributes to the BENCH, not the object. The mirror reading ("does not couple a resolvable resonance") is **NOT licensed**.
>
> **PLANTED leg (same unified config, per-object floors) — UNRESOLVED.** Same sub-period floor (0.033 periods), AND the net argmax sits **at the band edge** (`at_band_edge=True`), which the prereg band rule (§7) independently routes to UNRESOLVED (the driver's NO-RESPONSE short-circuit bypassed that escalation — §4.2).
>
> **Consequences:** no f₀/Q is reported for the made object from the driven sweep; the BVD row stays EMPTY; the measured-Q row stays UNTESTED; the forward-registered α⁻¹ post-hoc line returns **NO ENTRY** (nothing measured to compare). The inherited **NOT-ELECTRON verdict is NOT reopened** — and is independently consistent: the made build forms **zero saturated-pocket cells** (`pocket_cells = 0`).

**Plumber-physical one-liner:** the network analyzer was certified on a fast tank with 7 swings on the clock, then pointed at a slow tank with the gate time cut to a fifteenth of one swing. A meter that never waits out one full swing cannot tell a perfect mirror from a resonator it never heard finish — so the datasheet line is "instrument window too short" (UNRESOLVED), not "perfect mirror" (NO-RESPONSE).

---

## 1. THE GATE (first; `ave-apparatus-floor-attribution`)

KNOWN resonator = ω mass-gap driven-damped oscillator IN `S11ProbeUnified` (c_omega=0 ⇒ each cell independent at ω₀; injected γ_probe; S_min=0.05 ⇒ dt=0.0387). Analytic f₀=ω₀/2π, Q=ω₀/γ_probe.

| known (f₀ cyc/time, Q) | recovered f₀ | f₀ err | recovered Q | Q err | gate |
|---|---|---|---|---|---|
| (0.1592, 5.0) | 0.1597 | **0.37%** | 4.948 | **1.04%** | PASS (≤5% / ≤20%) |
| (0.1592, 10.0) | 0.1597 | **0.31%** | 9.901 | **0.99%** | PASS |

**Known-null:** probe-off step ≡ parent v6 step, byte-identical (max|diff|=0.000e+00, all 5 sectors, 200 steps, N=16). Every probe term is additive behind the probe flag.

**V-channel linearity (closes #166 FLAG-5):** amplitudes 1.5e-4 / 3e-4 / 6e-4 / 1.2e-3 (×8 span, bracketing A_PROBE=6e-4) swept DIRECTLY on `drive_sector="V"` ON the made object, measured on the breather-subtracted NET response: **R²=1.0000000, intercept_rel=8.4e-7** ⇒ the residual net is a real, small, linear susceptibility — not subtraction round-off.

**1.1 GATE SCOPE LIMIT (the load-bearing finding).** The instrument spec that matters for frequency discrimination is the lock-in window measured in PERIODS, not steps:

| config | dt | window (steps × dt) | f₀ probed | window in periods |
|---|---|---|---|---|
| GATE (certified) | 0.0387 | 1100 × 0.0387 = 42.6 tu | 0.1592 | **6.8** |
| MADE sweep (operated) | 1.732e-3 | 800 × 1.732e-3 = 1.386 tu | f₀_rd = 0.0481 | **0.067** |
| PLANTED sweep (operated) | 1.732e-3 | 1.386 tu | f₀_rd = 0.0241 | **0.033** |

The window in steps (NW=800) was frozen, but dt is set by the engine's CFL (the made object inherits the V2 default S_min=1e-4 ⇒ dt=1.732e-3, ×22 smaller than the gate's), so the physical window collapsed ×~100 in periods between certification and operation. **A gate PASS at 6.8 periods/window does not license attribution at 0.067 periods/window** — this is the prereg's own different-config-invalid rule applied to the gate itself.

## 2. THE MADE BUILD (datasheet rows, all from the evolved field)

MAIN v6 recipe verbatim, N=48, N_BUILD=3200, then 2200-step drive-off settle (F-CLOSE/D11 convention):

| row | value | reading |
|---|---|---|
| T1 mass E_V convergence | late_drift = **0.86%** (floor 5%) | **CONVERGED** (E_V_cons 11.70 → 12.91) |
| T1 H_total convergence | late_drift = 0.83% | CONVERGED (H_cons 29203 → 24612) |
| saturated pocket cells | **0** | NO self-bound frozen core — the c_eff(V) Γ=−1 wall the bulk-V probe targets is never engaged; consistent with inherited NOT-ELECTRON |
| dt (CFL of the made object) | 1.7321e-3 | the apparatus-floor driver (§1.1) |
| max\|ρ̄\| at settle | 0.949 | at the EOS 1−ρ² edge |
| bulk sector, free evolution | **unstable** (FLAG-D) | ρ̄/u_adv overflow post-settle; **V decoupling proven**: V(bulk-live) − V(bulk-zeroed) = 0.0 over 8000 steps, V series finite throughout |

## 3. RING-DOWN SELF-SPECTRA (the new datasheet row class — BOUNDS, not measurements)

Free ring-down, 24000 steps = 41.6 tu of record, density-peak read point, PML-excluded:

| object | f_dom (cyc/time) | df_res | record in periods of f_dom | Q_rd | honest reading |
|---|---|---|---|---|---|
| MADE | **0.0481** | 0.0241 | **2.0** (FFT bin 2) | 0.5 | spectral weight near ~0.05 cyc/time (≈0.30× the ω-LC 0.1592; within ~7% of #166's planted f_est=0.0516) — but resolution is ±1 bin ≈ ±50%: a **BOUND**, not an f₀ measurement. Q unresolvable (0.5 = the 2-period resolution floor, not a physics Q) |
| PLANTED (unified config) | 0.0241 | 0.0241 | **1.0** (FFT bin 1) | 0.25 | no resolvable peak — f_dom sits in the first FFT bin of a 1-period record |

The band-setting self-spectrum (prereg §5a, the anti-retrofit device) is itself only 1–2 periods long at these objects' scales — under-resolved, which independently reinforces UNRESOLVED over NO-RESPONSE.

## 4. DRIVEN S11 SWEEP + BIN ADJUDICATION

### 4.1 Raw numbers (made leg; planted in §5)
Band = [0.33, 3]×w_est = [0.0998, 0.9069] rad/time (= 0.0159–0.1443 cyc/time), 20 pts, A=6e-4, NET = (driven I,Q) − (drive-off I,Q) with both legs deep-copied from the SAME settled object (breather + residual ring-down common-mode, cancelled to subtraction_ratio = **0.0055**). Floor = median+3σ MAD of the net across the band = 2.60e-3; peak net = 1.57e-3 (**0.60× floor**); `local_maxima_above_floor = 0`; `at_band_edge = False`; Lorentzian fit (w0_peak=0.142, resid 0.293) NOT promoted (bin is not RESONANCE-CHARACTERIZED).

### 4.2 KEEP-BOTH adjudication (driver-emitted bin preserved; final bin demoted)
- **Driver-emitted (AS-RUN, preserved in the JSON and here):** NO-RESPONSE — "net never exceeds its median+3σ floor across the band". The driver's `assign_bin` short-circuits on `not clears_floor` BEFORE any floor-attribution check; it computes `win_periods_of_f0rd` (made 0.0667, planted 0.0333) but never consults it, and it bypasses the prereg §7 band-edge escalation on the planted leg. The driver is committed exactly as run (provenance); its binning logic deviation is the finding, not hidden.
- **FINAL (panel-adjudicated, per prereg §6 UNRESOLVED definition "the response... does not clear the apparatus floor" + governing `ave-apparatus-floor-attribution`):** **UNRESOLVED, both legs.** The prereg's NO-RESPONSE bin is a POSITIVE datasheet claim (near-perfect mirror — "the made object does not couple a resolvable resonance"). That attribution requires an instrument capable of resolving the coupling had it existed. With 0.022–0.20 periods of drive integrated per point (§1.1), the instrument is structurally blind at the object's scale — a null where the effect cannot be resolved is an apparatus artifact, not a physics reading (`ave-regime-phase-state-check`; the dark-wake lesson applied to a bench).
- **Cross-config confirmation that the bin tracks the WINDOW, not the object:** #166's planted article (V2 config, S_min=0.0125 ⇒ dt≈0.0194 under the same √S CFL) had a 2200-step window ≈ 42.6 tu ≈ **2.2 periods** of its f_est=0.0516 and read MULTI-MODE (low-contrast); the same article class in THIS unified config at **0.033 periods** reads below-floor. Same instrument design, same object family — the bin moved with the window.

## 5. PLANTED vs MADE (the de-novo payoff column — first entry)

| | PLANTED (unified config) | MADE (de-novo) |
|---|---|---|
| ring-down f_dom | 0.0241 (FFT bin 1 — unresolved) | 0.0481 (FFT bin 2 — bound only) |
| net peak / floor | 0.62× (floor 1.10e-3) | 0.60× (floor 2.60e-3) |
| subtraction_ratio | 0.00058 | 0.0055 |
| local maxima above floor | 0 | 0 |
| at_band_edge | **True** | False |
| window in periods of f_dom | 0.033 | 0.067 |
| driver-emitted bin | NO-RESPONSE | NO-RESPONSE |
| **FINAL bin** | **UNRESOLVED** (floor + band-edge) | **UNRESOLVED** (floor) |

**Provenance discrimination achieved: NONE at this window.** Planted ≈ made at the UNRESOLVED-family level — exactly the prereg §1 design-level expectation, and attributable to the shared apparatus floor, not to object physics. The column is INSTALLED (same instrument, per-object recalibrated floors, paired protocol); its first entry is honest and empty of discrimination.

## 6. DATASHEET DELTA (what this measurement fills/changes)

**NEW ROW CLASS — "free ring-down self-spectrum"** (per object: f_dom bound, df_res, record-in-periods, Q_rd floor):
- MADE: f_dom ≈ 0.048 cyc/time ±1 bin (±50%); ≈0.30× the ω-LC anchor; Q unresolved. **First-ever spectral row for a de-novo MADE v6 object.**
- PLANTED-in-unified: f_dom ≤ ~0.024 (bin-1, no resolvable peak).

**NEW COLUMN — provenance ∈ {planted, made}** on every S11/self-spectrum row, measured same-config with per-object floors. First paired entry: UNRESOLVED / UNRESOLVED — no discrimination at this window (§5). The column also formally separates #166's V2-config planted rows (≈2.2-period window, MULTI-MODE) from unified-config rows (sub-period window) — bins are only comparable at like window-in-periods.

**CHANGED ROWS:**
- v6 MADE-object S11 coupling: **UNRESOLVED (apparatus-floor)** — the "near-perfect-mirror / does-not-couple" reading is NOT entered (it was the driver's raw bin; demoted, §4.2). Do not carry "mirror" into any downstream doc.
- Probe-gate row: PASS **with scope qualifier** — certified at f₀=0.159, dt=0.0387, ≥6.8 periods/window; NOT certified for sub-period windows. Gate needs a "window ≥ N periods of f₀_rd" sub-check (open for Grant, §7.1).
- V-channel small-signal linearity: **FILLED** (R²=1.0, ×8, NET-based) — #166 FLAG-5 closed.
- Build rows FILLED: T1 mass CONVERGED (0.86%), pocket_cells=0, dt=1.732e-3, max|ρ̄|=0.949 at settle, FLAG-D bulk free-evolution instability with V-decoupling proof.
- Measured-Q row: stays **UNTESTED**. BVD motional parameters: stays **EMPTY**. α⁻¹ forward-registered post-hoc line: **NO ENTRY** (nothing measured to compare; Rule 11 honored — no comparison performed).
- NOT-ELECTRON (inherited): **UNCHANGED**, independently consistent (pocket_cells=0).

## 7. FLAGS & OPEN ITEMS (surfaced, not auto-pivoted — Rule 16)

1. **GATE-TRANSFER GAP (for Grant, decision needed):** add a frozen gate sub-check "lock-in window ≥ N periods of the unknown's f₀_rd" (instrument spec in periods, not steps), OR re-run the made sweep with NW sized to periods. Feasibility arithmetic: matching the gate's ~6.8 periods at f₀_rd=0.048 and dt=1.732e-3 needs NW ≈ 8.2e4 steps/point × 20 pts × 2 legs (+settle) ≈ millions of steps — compute-prohibitive at the made object's CFL. If infeasible, **UNRESOLVED is the terminal honest bin at this dt** and apparatus redesign (e.g., multi-period chirp/broadband read, or probing at a coarser-S_min surrogate with a transfer argument) is a design question for Grant — not auto-pivoted (prereg §6 Rule-11 commitment).
2. **FLAG-C corrected arithmetic:** the driver docstring's "~0.6 of the ω-LC period" was computed for NW=2200; the run used NW=800 ⇒ 0.22 ω-LC periods (and 0.067 of f₀_rd). The docstring understates the actual floor ×2.7.
3. **NW window-independence spot-check NOT run:** the NS/NW 2200→800 concession claimed window-independence; no NW=2200 point exists in the JSON. Note even NW=2200 is 0.18 periods of f₀_rd — still sub-period; a spot-check can only reinforce UNRESOLVED, never rescue NO-RESPONSE.
4. **FLAG-D hardening (optional):** the V-decoupling proof is the driver's own self-test (V identical with bulk zeroed, 8000 steps); an independent check that the V series is unperturbed by the bulk runaway under the probe-ON path would harden it.
5. **#166 adjacency note (no walk-back here):** #166's MULTI-MODE was measured at ≈1.1–2.4 periods of its two reported maxima — above one period but marginal; its own doc already confines the load-bearing claim to the NULL. A win-periods column should be added to #166's rows if they are ever promoted.
6. **Panel coverage:** only the PROBE-ATTRIBUTION lens reached this doc in full; the second lens (rebuild-fidelity) was truncated in the orchestration handoff. Its findings, if any, are NOT incorporated; re-audit before any promotion.

## 8. CLOSURE

The de-novo S11 characterization CLOSES as: **instrument validated at its certified operating point; made object built and energy-settled with no saturated core; both driven legs UNRESOLVED — the apparatus window, not the object, sets the reading.** No seed/wall/band/settle/read tuning toward a peak was performed (Rule 11). Nothing here reopens NOT-ELECTRON, and no corpus-state promotion is licensed by an UNRESOLVED pair.
