# G-PERSIST localization observable + φ-channel plant — FROZEN prereg

**Date:** 2026-07-14 · **Branch:** `analysis/gpersist-localization-observable` ·
**Freeze discipline:** frozen **by push** as its own commit **BEFORE** the driver runs
(freeze commit precedes the first driver commit in git history; model
`research/2026-07-13_genesis-npersist-n14-battery_prereg_FROZEN.md`, freeze-first).
**Frozen bins enforce; flags don't.**

**Parent RESULT / gate.** This is the queued follow-on discriminator named in
`research/2026-07-13_genesis-npersist-n14-battery_RESULT.md` §8 and in the G-PERSIST
docket row (`_orchestration/2026-07-10_rulings-docket.md`, ★RULED — CONFIRMS bin (ii)
A-WEAKENED; **enclosure fork = KEEP-BOTH-OPEN, Reading A wake-feeding LEANED by Grant
2026-07-13**). Grant GO 2026-07-14 to fire the two follow-ons (localization observable +
φ-channel plant).

**KEEP-BOTH (binding).** These are **NEW axes added alongside** the frozen #670 E/φ
detector — per the #670 prereg §Detector-substitution rule, **never a swap**. The frozen
#670 axes (`E_persist ≥ 0.85 ∧ φ_persist ≥ 0.80`, bins (i)/(ii), the boundary-artifact
axis) are **untouched**. This prereg adds (1) a boundary-insensitive spatial-concentration
meter and (2) a φ-channel negative-control plant.

---

## What this observable does and does NOT decide

- **DECIDES:** the enclosure **fork** only — *Reading A (wake-feeding: the periodic-torus
  enclosure returns the pattern's own wake; the projection gauge counts laps)* vs *Reading B
  (genesis-under-confinement: genuine self-tightening)*. Output = fork adjudication **data**;
  **Grant rules the fork** (state, don't rule).
- **DOES NOT DECIDE:** the G-PERSIST ★RULED verdict. That flip (CONFIRMS bin (ii)
  A-WEAKENED) rests on the **boundary-insensitive PML φ-dispersion trend** (φ 0.87→0.73→0.51
  as N grows), which is **fork-independent**. Neither a CONCENTRATING nor a LOOP-FILLING
  outcome here re-opens G-PERSIST. **A-priori: Grant leans Reading A.**

---

## Sector header (mandatory)

- **MODE** = driven genesis on the saturable K4⊗Cosserat lattice, **fixed-\(N\)** (no node
  birth; fork (B) firewalled). Carrier = `run_loop_gap_probe` rank-4 config, re-run through
  an **instrumented mirror loop** that uses the SAME primitives
  (`make_engine`/`apply_seed`/`apply_bulk_probe_ic`/`freeze_converter_wall`/`step`/
  `snapshot_op14`) — **no new engine, no new stepper, no retune** (Rule-14). The mirror loop
  is validated byte-parity against `run_loop_gap_probe` on a live cell (§Live-fire parity).
- **REGIME** = at/above-yield launch (`n_drive_mult=0.5`) → anhysteretic quiet-window
  relaxation (`n_quiet_mult=1.5`), the banked #670 D2 schedule.
- **PHASE-STATE** = seed → de-energize → does the ENERGY **spatially concentrate**
  (self-tighten, Reading B) or **stay distributed while the accumulated Φ_link inflates**
  (wake-feeding, Reading A). A spatial-shape read, **not** a mint probe.
- **Instrument** = the NEW localization meter (below) recorded **per quiet step** over the
  recording window, **per sector, never summed** (A1/energy ⊥ T2/Φ_link). The frozen #670
  E_persist / φ_persist scalars are recorded alongside (parity + context), unchanged.
- **consistency-vs-emergence** = **consistency-check / fork-discriminator**. This meter
  discriminates two readings of an existing engine result; it makes **no** CODATA/manuscript
  comparison and **no** emergence claim. A CONCENTRATING outcome supports Reading B *for this
  seed on this battery*; it is **not** electron genesis (EMERGENCE-as-electron refused).
- **phase-space-coordinate-check** = the corpus claim under test (self-tightening vs
  wake-spreading) is a **real-space spatial-localization** claim ⇒ the meter is measured in
  **real-space lattice coordinates** (matched). The φ_persist scalar is the phase-space/gauge
  quantity; the localization meter is deliberately real-space to complement it. Coordinate
  match holds.

---

## Corpus sweep (STEP-0, grep-verified 2026-07-14)

| Prior | Finding |
|---|---|
| `research/2026-07-13_genesis-npersist-n14-battery_RESULT.md:268-280` (§8) | spec verbatim: "a **boundary-insensitive localization observable** — e.g. the fraction of interior energy / Φ_link² inside a central core … + the participation ratio"; second follow-on = φ-channel negative control (sustain φ WITHOUT clobbering the Cosserat state) |
| `research/2026-07-13_..._RESULT.md:14-34` (torus erratum) | `pml=0` = **PERIODIC torus** (`np.roll` wraparound, `k4_tlm.py:393`), **not** a reflecting box; Φ_link² runaway to ~10× = wake re-absorption; conclusions unchanged |
| `_orchestration/2026-07-10_rulings-docket.md:435,477,502` | G-PERSIST ★RULED — CONFIRMS bin (ii); **enclosure fork KEEP-BOTH-OPEN, Reading A LEANED**; discriminator = "spatial-concentration / participation-ratio localization observable (follow-on driver queued); the φ-channel-plant control is the second follow-on" |
| `src/ave/core/k4_tlm.py:400` | `Phi_link[...] += V_avg·dt` — Φ_link **accumulates monotonically** (never reset during the run) ⇒ φ_persist ratio grows with quiet-step count ("counts laps") — the mechanistic root of the ~10× runaway; the meter reads the **shape** of the accumulated flux, not its magnitude |
| `src/ave/topological/k4_cosserat_coupling.py:469` | `_interior_mask()` = PML-excluded interior (pml>0) / full grid (pml=0) — the meter's domain (A-Rule 10 PML-exclusion satisfied) |
| `src/ave/core/k4_tlm.py:528` | `get_energy_density()` = Σ_k(V_inc²+V_ref²), per-site (N,N,N) — K4/V-sector energy density |
| `src/ave/topological/cosserat_field_3d.py:1427` | `cos.energy_density()` — per-site (N,N,N) Cosserat energy density |

---

## The localization meter (FROZEN definition)

Two **per-sector** density fields over the PML-excluded interior mask
(`_coupled._interior_mask()`, M interior sites) — **never summed** (A1 ⊥ T2):

- **A1 / energy density** `E_dens[i]` = `k4.get_energy_density()[i] + cos.energy_density()[i]`
  (the spatial parallel of the frozen `E_persist` channel; K4 V-sector + Cosserat per-site
  energy). Diagnostic sub-field reported alongside: `E_k4_dens[i] = k4.get_energy_density()[i]`.
- **T2 / Φ_link density** `Phi_dens[i]` = Σ_port `k4.Phi_link[i,port]²`
  (the spatial parallel of the frozen `φ_persist` channel; the accumulated flux, T2/Cosserat
  winding channel).

On each nonnegative density field `d` over the interior (M sites), two concentration
statistics:

1. **Participation ratio (raw)** — `PR(d) = (Σ d_i)² / Σ d_i²` ∈ [1, M].
   Effective number of participating sites. **PR = 1** ⇒ all mass on one site (maximally
   localized); **PR = M** ⇒ uniform (maximally distributed). Reported raw (boundary-comparable:
   a k-site structure reads ≈ k in both boundaries) and as `PR_frac = PR/M`.
   **No center choice** ⇒ immune to drift/shell structure.
2. **Core fraction (density-peak-centered)** — `CF_r(d) = (Σ_{|i−i*| ≤ r} d_i) / (Σ_i d_i)`,
   where `i*` = argmax `d` over the **interior mask** (peak, **not** centroid — per the
   density-peak-vs-centroid discipline; a shell's centroid is the empty middle). Radii
   `r ∈ {1.5, 2.0, 2.5}` lattice units (Euclidean ball); **primary r = 2.0**. A fixed
   physical core radius ⇒ boundary-comparable. Also reported: `CF_r^geom` (same, centered at
   the geometric interior center = the seed site) as a secondary drift-sensitive read.

**Recording window (reactance-pair discipline).** The meter is recorded at **drive-off**
(t = n_drive) and at **every quiet step** (t = n_drive+1 … n_total) — a full time series of
length n_quiet+1, **both sectors at every step** (not a single snapshot). `E_persist` /
`φ_persist` are recorded alongside for parity and context.

**Trend summary (per sector, per statistic).** With `start` = value at drive-off and `end`
= value at final step: `rel_trend = (end − start)/|start|`. Also reported: min/max over the
window and the least-squares slope normalized by window mean (non-monotone guard).

**Meter-genuineness (binding self-check).** A concentration statistic is admissible only if
it is **NOT derivable from the scalar `E_persist` / `φ_persist` alone** — it must read the
**spatial distribution** (WHERE), not the total (HOW MUCH). PR and CF are shape statistics of
the per-site field and are **scale-invariant** (invariant under global rescaling of `d`), so
they carry information orthogonal to the scalar magnitude ratios. The live-fire review
(§Adversarial) verifies this by confirming PR/CF are **not** monotone functions of
`E_persist`/`φ_persist` across the cells.

---

## Cells (FROZEN grid — the discriminating subset of #670)

The fork lives in the **N=14 periodic-torus** (`pml=0`) cells (φ→~10×) with `pair` and
`graded_a0` (the φ-live seeds). Their **PML twins** (`pml=3`) give the boundary-insensitivity
corroboration; `photon_lock` (φ≡0, structure-dead) is the meter's **negative control**.

| # | N | pml (boundary) | mode | fidelity | role |
|---|---|---|---|---|---|
| 1 | 14 | 0 (torus) | pair | production | **primary fork cell** |
| 2 | 14 | 0 (torus) | graded_a0 | production | **primary fork cell** |
| 3 | 14 | 3 (PML) | pair | production | boundary-insensitivity twin |
| 4 | 14 | 3 (PML) | graded_a0 | production | boundary-insensitivity twin |
| 5 | 14 | 0 (torus) | photon_lock | production | structure-dead control (must NOT read CONCENTRATING) |
| 6 | 14 | 3 (PML) | photon_lock | production | structure-dead control |
| S1 | 14 | 0 (torus) | pair | smoke | fast preview + parity gate |
| S2 | 14 | 0 (torus) | graded_a0 | smoke | fast preview |

Carrier config per cell is **byte-identical** to the banked #670 D2:
`rank_target=4, seed_mode, N=14, pml∈{0,3}, bulk_density_on=True, bulk_seed="probe"
(amp 0.08), front_target=A_YIELD, n_drive_mult=0.5, n_quiet_mult=1.5, use_memristive_
saturation=True`. **Only the instrumentation is added** (per-step meter readout); the field
trajectory is unchanged (verified by §Live-fire parity).

---

## Live-fire parity gate (validation, mandatory before banking)

The instrumented mirror loop must reproduce `run_loop_gap_probe`'s `E_persist` /
`φ_persist` **to ≤ 1e-6 relative** on a live cell (the engine is deterministic — identical
config ⇒ identical trajectory). If parity fails the meter is measured on a *different*
trajectory and the run is **void**. Parity is checked on cell S1 (torus pair, smoke) and on
one production cell.

---

## FROZEN BINS (the fork adjudication — scored on the TORUS pair + graded_a0 cells)

Resolution floor **θ = 0.10** (10 % relative change). Evaluated on the **A1/energy** meter
(primary), with the T2/Φ_link meter and the PML twins as corroboration.

- **CONCENTRATING** ⇒ *Reading B genesis-under-confinement REVIVES; the fork re-opens
  toward B.* Criterion: on **BOTH** torus `pair` AND `graded_a0`, the energy meter shows
  concentration through the quiet window — `PR_energy` **falls** (`rel_trend ≤ −θ`) **OR**
  `CF_energy(r=2)` **rises** (`rel_trend ≥ +θ`).
- **LOOP-FILLING** ⇒ *Reading A wake-feeding CONFIRMED; the fork closes toward A; Grant's
  lean validated.* Criterion: on **BOTH** torus `pair` AND `graded_a0`, the energy stays
  distributed — `PR_energy` does **not** fall (`rel_trend ≥ −θ`) **AND** `CF_energy(r=2)`
  does **not** rise (`rel_trend ≤ +θ`) — **while** `φ_persist` inflates (≫ 1, the banked
  ~10×). I.e. the accumulated flux grows but the energy does not tighten.
- **MIXED** ⇒ enumerate. Triggered when `pair` and `graded_a0` disagree, OR the energy meter
  and the Φ_link meter disagree within a cell, OR a torus cell concentrates while its PML twin
  does not (trend is boundary-coupled, not boundary-clean).
- **INCONCLUSIVE** ⇒ meter resolution. Triggered when `|rel_trend| < θ` on **both**
  `PR_energy` **and** `CF_energy(r=2)` for the torus cells (no resolvable trend at 10 %).

**Corroboration (reported, not bin-determining):** (a) PML-twin agreement = boundary-clean
localization; disagreement folds into MIXED. (b) `photon_lock` must **not** read
CONCENTRATING (meter false-positive guard). (c) the T2/Φ_link meter shape trend
(concentrated accumulated flux = B-leaning; spread-around-the-loop = A-leaning).

---

## The φ-channel plant (FROZEN negative control — the #670 second follow-on)

**Gap (from #670 §6 / review finding #5).** The #670 sabotage plant re-injected the *seed*,
which **clobbers the Cosserat state and zeroes φ** — so it exercised only the E-channel and
never the load-bearing φ-channel. Needed: a plant that **sustains φ WITHOUT destroying the
Cosserat state**, i.e. external sustenance the φ-detector SHOULD flag.

**Plant (frozen).** Run the mirror loop on a cell where φ would otherwise **decay** (the
**PML** N=14 `pair` cell — banked `φ_persist` 0.73/0.51 < the 0.80 floor at N=14/16). During
**every quiet step**, add a small **spatially DISTRIBUTED external K4-sector pump** —
`k4.V_inc[interior, :] += amp_pump` on **all four ports at all interior sites** — with
`amp_pump = √ALPHA` (matched to the `pair` seed amplitude; principled, not tuned). This keeps
`V_avg` energized ⇒ `Phi_link` keeps accumulating ⇒ `φ_persist` is externally sustained,
**without** calling `apply_seed` (the Cosserat `u`/`ω` state is **not** clobbered). Both the
free (unpumped) mirror run and the plant run are recorded on the **real integrator**.
Corroboration leg: the same plant on the **torus** N=14 `pair` cell. Budget = smoke
(control-class, matching the #670 sabotage plant budget).

**Frozen criterion (PASS = the two-meter combo is un-foolable by sustenance):**
- **(a)** `plant_φ_persist ≥ 0.80` — the plant **fools the φ-retention floor** (sustains φ),
  AND
- **(b)** the localization meter reads **LOOP-FILLING** on the plant's evolved field
  (`PR_energy` does not fall AND `CF_energy(r=2)` does not rise — the distributed external
  pump signature) — the meter **classifies the sustained φ as externally-fed**.

- **(a) ∧ (b) ⇒ UN-FOOLABLE CONFIRMED:** φ-sustenance that beats the scalar floor is caught
  by the localization meter.
- **(a) ∧ ¬(b) ⇒ FOOLABLE (surface it):** the pump sustains φ AND drives the meter to read
  CONCENTRATING ⇒ the two-meter combo is foolable — a genuine negative finding to report
  (flag-don't-fix), not a rescue.
- **¬(a) ⇒ INCONCLUSIVE:** the pump could not sustain φ ≥ 0.80 without clobbering the state ⇒
  the φ-channel fooling scenario could not be constructed at this amplitude (follow-on).

---

## Out of scope

- Any (B) node-birth / graph-growth / `genesis_v{N}` / srs v18+ code. Fork (B) firewalled.
- Retuning thresholds, seed amplitudes, drive/quiet multipliers, the #670 detector, or the
  carrier config. Only the per-step meter readout + the frozen plant pump are added.
- Re-opening the G-PERSIST ★RULED verdict (rests on the fork-independent PML φ-trend).
- Claiming electron genesis / mass / self-tightening-as-electron from any outcome.
- Ruling the fork. This driver returns **data**; **Grant rules** Reading A vs B.

---

## Deliverables after this freeze push

1. This FROZEN prereg (this commit, pushed first).
2. Driver `src/scripts/vol_1_foundations/gpersist_localization_observable.py` (instrumented
   mirror loop + meter + φ-plant + aggregate), reusing the frozen primitives (Rule-14).
3. Battery run → per-cell JSON under `assets/sim_outputs/` (gitignored per repo convention).
4. RESULT doc `research/2026-07-14_gpersist-localization-observable_RESULT.md` (per-cell
   concentration table + bin + φ-plant outcome; **state, don't rule**).
5. Adversarial PR review (scriptPath wrapper) + PR
   `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.

---

## Amendments (dated — appended below the frozen body per freeze discipline)

> The frozen body above (lines 1–242) is **byte-untouched**. The dated amendments below record
> corrections surfaced by the independent adversarial review (2026-07-14; **15/15** confirmed,
> **0 refuted**, all **EVIDENCE-VOID**). **None alters the fork verdict** (LOOP-FILLING ⇒
> Reading A) or G-PERSIST ★RULED; they reconcile frozen-vs-shipped parity and citation provenance.
> Citations below were re-verified two-method on 2026-07-14.

### 2026-07-14 · Amendment (review finding #4) — LOOP-FILLING bin: φ-conjunct superseded by gauge quarantine

The frozen **LOOP-FILLING** criterion (lines 169–173) reads as a **three**-conjunct rule:
`PR_energy` not falling **AND** `CF_energy(r=2)` not rising **— while `φ_persist` inflates
(≫ 1, the banked ~10×)**. The shipped classifier (`_classify_cell`) implements only the
**two**-conjunct PR∧CF signature and does **not** gate on `φ_persist`.

**This omission is intentional and quarantine-STRONGER, not a weakening.** The ~10.5× φ
inflation is the **lap-counting gauge artifact** — `Phi_link` accumulates **monotonically**
(`k4_tlm.py:400`: `self.Phi_link[self.mask_A, port] += V_avg[self.mask_A] * self.dt`, never
reset during the run). Gating the fork verdict on that quantity would inject the **quarantined
gauge artifact** into the bin, violating the standing gauge-artifact quarantine.

**Correction:** the frozen bin's φ conjunct is **superseded** — the operative classifier is the
**2-conjunct PR∧CF** signature, with **φ ≫ 1 retained as human-verified corroboration**
(byte-exact vs banked #670: torus `pair` φ=10.5197, `graded_a0` φ=10.4218 — both ≫ 1, so the
full frozen conjunction **is** satisfied where it is scored; it is simply **not machine-gated**).
Per the review, **φ is NOT added back to the classifier** (that would re-import the artifact).
Future **CONCENTRATING** claims adopt the **two-statistic conjunction** rule (PR falls **AND**
CF rises, on the torus-native CF) — see RESULT §4 meter-reuse note.

### 2026-07-14 · Amendment (review finding #5) — MIXED-trigger reconciliation + slope guard shipped

Two frozen-vs-shipped gaps in the aggregate gate and the trend summary:

**(i) MIXED triggers — internal contradiction reconciled.** The frozen §FROZEN BINS (lines
174–176) lists **three** bin-determining MIXED triggers — `pair`/`graded_a0` disagree, **OR** the
energy meter and the Φ_link meter disagree within a cell, **OR** a torus cell concentrates while
its PML twin does not — while §Corroboration (lines 180–183) labels the Φ_link meter and PML twin
"reported, **not** bin-determining". This is an **internal contradiction** in the frozen body, and
the shipped `cmd_aggregate` implemented only trigger (1). **Reconciliation:** all **three** MIXED
routes are **bin-determining** and are now machine-evaluated in `cmd_aggregate`; the Φ_link-meter
and PML-twin *agreement* remains corroboration, but their *disagreement* (resp. a
torus-concentrates-while-twin-does-not condition) fires MIXED. All three are **moot on this run** —
the Φ_link meter agrees in sign with the energy meter on both fork cells (PR +0.996/+0.963,
CF −0.753/−0.731 = LOOP-FILLING) and no torus fork cell concentrates — so the banked
**LOOP-FILLING** bin is **unchanged**; the completeness is a robustness fix for meter reuse.

**(ii) Non-monotone slope guard — declared but unshipped, now shipped.** The frozen §Trend
summary (line 113) declares "the least-squares slope normalized by window mean (non-monotone
guard)"; it was **not** implemented. `_trend` now returns `slope_norm` alongside the already-
shipped min/max, completing the frozen declaration. (The endpoint-only `rel_trend` can hide
strongly non-monotone series — e.g. under the finding-#3 composed meter the PML `pair` PR swings
min 71.7 → max 99.1 yet returns near-flat at the endpoints.)
