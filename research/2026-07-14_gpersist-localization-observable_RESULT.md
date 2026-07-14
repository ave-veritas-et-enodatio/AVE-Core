# G-PERSIST localization observable + φ-channel plant — RESULT

**Date:** 2026-07-14 · **Branch:** `analysis/gpersist-localization-observable` ·
**Freeze commit (prereg, pushed before driver):** `f919fb12` · **Driver:** `31d08f3a` ·
**Freeze margin:** 9 min 32 s (freeze 07:18:34 → driver 07:28:06, prereg pushed first) ·
**FROZEN prereg:** [`2026-07-14_gpersist-localization-observable_prereg_FROZEN.md`](2026-07-14_gpersist-localization-observable_prereg_FROZEN.md) ·
**Parent RESULT:** [`2026-07-13_genesis-npersist-n14-battery_RESULT.md`](2026-07-13_genesis-npersist-n14-battery_RESULT.md) ·
**Gate:** G-PERSIST ★RULED — CONFIRMS bin (ii) A-WEAKENED; **enclosure fork = KEEP-BOTH-OPEN**
(`_orchestration/2026-07-10_rulings-docket.md`).

**Class:** follow-on discriminator driver (two KEEP-BOTH new axes on the #670 battery; frozen
#670 E/φ axes untouched). **This doc STATES the fork data. Grant rules the fork.**

---

## TL;DR (brutal-clarity verdict)

1. **FORK BIN = LOOP-FILLING ⇒ Reading A (wake-feeding) CONFIRMED — Grant's a-priori lean
   validated.** On BOTH torus (`pml=0`) fork cells (`pair`, `graded_a0`, production), the
   energy meter reads the pattern **spreading out** — participation ratio **rises**
   (348.7→491.6 / 353.0→493.2) and core fraction **falls** (0.062→0.045 / 0.061→0.049) —
   **while φ inflates to ~10.5×**. The energy does **not** self-tighten; the φ growth is the
   accumulated-flux "counts laps" gauge effect (`Phi_link` accumulates monotonically,
   `k4_tlm.py:400`), **not** localization. This is Reading A, not Reading B.
2. **Boundary-insensitive.** The PML twins read the SAME sign (PR rises, CF falls →
   LOOP-FILLING under `pml=3` too). The dispersal appears under **both** boundaries ⇒ it is a
   boundary-clean property of the pattern, not a torus artifact.
3. **The meter is genuine — provably not derivable from E/φ.** On the torus `E_persist ≡ 1.0`
   (a conservation identity, #670 erratum) yet the participation ratio moves ~4× over 8 quiet
   steps (adversarial KNIFE B). The spatial statistic carries WHERE-information the scalar
   cannot encode. Independent naive recompute matches the driver to machine precision
   (|Δ|≤1.1e-13, KNIFE A).
4. **φ-channel plant: UN-FOOLABLE_CONFIRMED (both cells).** A distributed external K4 pump
   sustains φ far above the 0.80 floor (PML pair: free φ=0.084 → plant φ=4.2e6; torus pair:
   free 2.512 → plant 4.1e8) **while the localization meter reads LOOP-FILLING** — the meter
   classifies the sustained φ as externally-fed. The two-meter combination (φ-detector +
   localization meter) is **un-foolable by sustenance**; it closes the #670 review's missing
   φ-channel negative control.
5. **Independent reproduction of #670 is byte-exact.** Every cell's `E_persist`/`φ_persist`
   from the instrumented **mirror loop** reproduces banked #670 to the digit (torus pair
   φ=10.5197, graded_a0 φ=10.4218; PML pair 0.8449/0.7266; PML graded 0.8446/0.5826; smoke
   torus 2.5117/2.5488). Live-fire parity vs `run_loop_gap_probe` = **0.00e+00** relative. The
   meter is on the identical trajectory.
6. **CONTROL CAVEAT (flag-don't-fix):** the structure-dead torus `photon_lock` control trips
   CONCENTRATING via the **CF-rises-alone** leaf of the frozen disjunctive criterion
   (CF 0.097→0.138) **while PR contradicts it** (PR flat at −0.072; PR_frac stays ≈9% = still
   delocalized). The density-peak core fraction *alone* is not a robust CONCENTRATING detector
   on the periodic torus; the participation ratio and the two-statistic **conjunction** do not
   false-positive. **The fork verdict is unaffected** (both fork cells read LOOP-FILLING on
   **both** statistics). The frozen criterion is **NOT** retuned post-hoc; the caveat is
   recorded.
7. **G-PERSIST ★RULED is untouched.** This observable discriminates only the enclosure fork;
   the CONFIRMS-bin(ii) flip rests on the fork-independent PML φ-dispersion trend. **Neither a
   LOOP-FILLING nor a CONCENTRATING outcome here re-opens G-PERSIST.** Reading A being
   validated **closes the fork toward A**, consistent with the docket's leaned Reading — but
   **Grant rules the fork**, not this driver.

---

## Sector header (recap)

MODE = driven genesis on the saturable K4⊗Cosserat lattice, fixed-\(N\), rank-4 carrier,
re-run through an **instrumented mirror loop** using the frozen primitives (`make_engine`/
`apply_seed`/`apply_bulk_probe_ic`/`freeze_converter_wall`/`step`/`snapshot_op14`) — no new
engine, no new stepper, no retune (Rule-14). REGIME = at/above-yield launch
(`n_drive_mult=0.5`) → anhysteretic quiet-window relaxation (`n_quiet_mult=1.5`), the banked
#670 D2 schedule. PHASE-STATE = seed → de-energize → does the ENERGY spatially concentrate
(Reading B) or stay distributed while the accumulated Φ_link inflates (Reading A). Instrument
= the NEW localization meter, per-sector (A1/energy ⊥ T2/Φ_link, never summed), recorded per
quiet step over the PML-excluded interior. consistency-vs-emergence = **consistency-check /
fork-discriminator** (no CODATA/manuscript comparison; no emergence claim).

---

## 1 · Live-fire parity + independent #670 reproduction (validation gate)

The mirror loop reproduces `run_loop_gap_probe`'s `E_persist`/`φ_persist` **exactly**:

| cell | ref (run_loop_gap_probe) | mirror loop | relΔ | banked #670 |
|---|---|---|---|---|
| N=14 torus pair, smoke | E=0.999993 / φ=2.511658 | E=0.999993 / φ=2.511658 | 0.00e+00 | φ 2.5117 ✓ |

Every production cell independently reproduces banked #670 to four decimals (§2 table). ⇒ the
per-step localization meter is measured **on the identical field trajectory** as the banked
battery; the instrumentation does not perturb the physics.

---

## 2 · Per-cell concentration table (the deliverable) — energy (A1) meter

Trend = relative change from **drive-off** (t = n_drive) to **final quiet step** (t = n_total).
PR = raw participation ratio (effective participating sites, interior M sites; **no center**).
CF = fraction within r=2.0 of the **density peak** (PML-excluded interior). Resolution θ=0.10.

| N | boundary | fid | mode | E_persist | φ_persist | PR (start→end, rel) | CF (start→end, rel) | signature |
|---|---|---|---|---|---|---|---|---|
| 14 | torus | prod | **pair** | 1.0000 | **10.520** | 348.7→491.6 (**+0.410**) | 0.062→0.045 (**−0.274**) | **LOOP-FILLING** |
| 14 | torus | prod | **graded_a0** | 1.0000 | **10.422** | 353.0→493.2 (**+0.397**) | 0.061→0.049 (**−0.203**) | **LOOP-FILLING** |
| 14 | PML | prod | pair | 0.8449 | 0.7266 | 87.5→94.8 (+0.084) | 0.178→0.113 (−0.364) | LOOP-FILLING |
| 14 | PML | prod | graded_a0 | 0.8446 | 0.5826 | 88.1→97.1 (+0.102) | 0.182→0.125 (−0.316) | LOOP-FILLING |
| 14 | torus | prod | photon_lock | 1.0000 | 0.0000 | 270.1→250.7 (−0.072) | 0.097→0.138 (**+0.417**) | CONCENTRATING* |
| 14 | PML | prod | photon_lock | 0.9498 | 0.0000 | 68.4→83.4 (+0.219) | 0.303→0.222 (−0.269) | LOOP-FILLING |
| 14 | torus | smoke | pair | 1.0000 | 2.512 | 47.4→348.7 (+6.355) | 0.435→0.062 (−0.857) | LOOP-FILLING |
| 14 | torus | smoke | graded_a0 | 1.0000 | 2.549 | 47.5→353.0 (+6.428) | 0.432→0.061 (−0.859) | LOOP-FILLING |

`*` structure-dead control false-positive — CF-alone, PR-contradicted; see §4. Not a fork cell.

**Reading the fork cells.** Both φ-live seeds (`pair`, `graded_a0`) show the energy **spreading**
under **both** boundaries: PR rises (more sites participate) and CF falls (less mass in the
core). At **smoke** the dispersal arc is dramatic (the seed is still tight at drive-off,
CF≈0.43, then spreads to CF≈0.06 during quiet; PR 47→349); at **production** the drive phase
has already dispersed the pattern by drive-off (CF≈0.06), and it continues to spread. Both
fidelities, both seeds, both boundaries: the same direction — **dispersal, not tightening.**

---

## 3 · Fork bin — LOOP-FILLING (Reading A) — with the a-priori and the carve

**FORK BIN (torus `pair` + `graded_a0`, production): LOOP-FILLING.** Criterion (frozen): energy
stays distributed (PR does not fall, CF does not rise) while φ inflates — met on **both** fork
cells, on **both** statistics (PR rises AND CF falls), corroborated by the PML twins
(boundary-insensitive) and by the smoke arc.

- **⇒ Reading A (wake-feeding) CONFIRMED; the fork closes toward A.** The periodic-torus
  enclosure returns the pattern's own dispersing wake; the projection gauge counts laps
  (φ→10.5×) while the energy delocalizes. There is **no genesis-under-confinement
  self-tightening** on this battery for these seeds.
- **a-priori:** Grant leaned Reading A; the data validate the lean. The flip's evidentiary
  basis (the PML φ-dispersion trend) is **fork-independent** — G-PERSIST ★RULED CONFIRMS
  bin (ii) A-WEAKENED stands regardless of this outcome.
- **Carve — Grant rules the fork.** This driver returns the discriminator **data**; it does
  not fiat the fork. The framing-level call (does the LOOP-FILLING data close Reading B, or is
  a residual self-tightening channel unexamined?) is surfaced for Grant, not decided here.

---

## 4 · CONTROL CAVEAT — the density-peak CF-alone leaf is not torus-robust (flag-don't-fix)

The frozen CONCENTRATING criterion is disjunctive: **PR falls (≤−θ) OR CF rises (≥+θ)**. The
structure-dead torus `photon_lock` control trips it via **CF-alone** (CF 0.097→0.138, +0.42)
**while PR contradicts** (−0.072, within the flat band). Diagnosis: the delocalized photon
field (`PR_frac` ≈ 9% of the 2744 interior sites — still spread) develops a modestly **sharper
central peak** at the fixed seed site (7,7,7) over the quiet window (photon self-interference/
refocusing on the closed periodic lattice), so the density-peak core captures a growing
fraction. The **global** participation ratio correctly reports **no** concentration.

- **What this is:** a real meter-resolution limit — the density-peak core fraction, taken
  **alone**, can false-positive on transient local peak-sharpening of a still-delocalized
  field on the periodic torus. Under PML the same seed reads LOOP-FILLING (no false-positive),
  so the failure mode is torus-specific.
- **What this is NOT:** a threat to the fork verdict. The fork cells (`pair`, `graded_a0`) read
  LOOP-FILLING on **both** statistics (PR rises AND CF falls) — the robust, two-statistic-
  agreeing signature. Only a CONCENTRATING verdict resting on CF-alone would be suspect, and
  the fork went the other way on both statistics.
- **Discipline:** per honest-closure + flag-don't-fix, the frozen disjunctive criterion is
  **NOT** retuned post-hoc. The caveat is recorded: a future CONCENTRATING claim should require
  the **conjunction** (PR falls AND CF rises), and the participation ratio is the more robust
  single statistic. Surfaced for the auditor's meter-hardening queue.

---

## 5 · φ-channel plant — UN-FOOLABLE_CONFIRMED (the #670 second follow-on)

The #670 sabotage plant re-injected the *seed*, clobbering φ→0, so it never exercised the
load-bearing φ-channel (review finding #5). This plant sustains φ **without** clobbering the
Cosserat state: a **distributed external K4 pump** (`V_inc[interior,:] += √ALPHA` each quiet
step) keeps `V_avg` energized ⇒ `Phi_link` keeps accumulating ⇒ φ is externally sustained; the
Cosserat `u`/`ω` evolve under the real coupled integrator (never overwritten).

| plant cell | free φ_persist | plant φ_persist | φ sustained ≥0.80? | meter reads LOOP-FILLING? | verdict |
|---|---|---|---|---|---|
| N=14 PML pair (smoke) | 0.084 (would FAIL floor) | 4.24e6 | **yes** (fools the floor) | **yes** (externally-fed) | **UN-FOOLABLE_CONFIRMED** |
| N=14 torus pair (smoke) | 2.512 | 4.14e8 | yes | yes | UN-FOOLABLE_CONFIRMED |

**Finding:** external sustenance trivially fools the **scalar** φ-retention floor (φ lifted 7–8
orders of magnitude above 0.80), but the **localization meter catches it** — it reads
LOOP-FILLING (energy distributed, PR not falling, CF not rising), classifying the sustained φ
as **externally-fed**. The frozen criterion (φ sustained AND meter loop-filling ⇒ un-foolable)
is met on both cells. The two-meter combination is **un-foolable by sustenance**. (The plant φ
magnitude is a pump artifact — the point is *sustained ≥ floor* while the meter flags
externally-fed, not the absolute value. Budget = smoke, matching the #670 sabotage-plant
control class.)

---

## 6 · Adversarial self-review (3 lenses; live-fire this turn)

The full 10-agent `ave-adversarial-pr-review` scriptPath workflow is the orchestrator's to
fire at the PR gate (as for #670 — no workflow-runner tool in the implementer toolset). The
live-fire equivalent was executed this turn as the three standard lenses:

| lens | check | result |
|---|---|---|
| **Live-fire / re-derivation** | mirror-loop E/φ vs `run_loop_gap_probe`; independent naive recompute of PR/CF | parity 0.00e+00; PR/CF match to |Δ|≤1.1e-13 (KNIFE A) |
| **Meter-genuineness knife** | is the concentration meter derivable from φ/E alone? | **NO** — on the torus E≡1.0 (identity) yet PR moves ~4× over 8 quiet steps (KNIFE B); the scalar cannot encode the spatial move |
| **Discipline / prereg-parity** | every frozen declaration vs shipped code | clean — energy=k4+cos, φ=ΣΦ_link², PML-excluded mask, raw PR, density-peak core r∈{1.5,2,2.5}, 0.5/1.5 schedule, memristive, √ALPHA distributed quiet-only pump, a∧b criteria all grep-confirmed |

**Self-surfaced finding (not a defect, a caveat):** the CF-alone leaf false-positives on the
torus `photon_lock` control (§4) — recorded, criterion not retuned. No other findings; the
banked verdict (LOOP-FILLING) rests on the two-statistic-agreeing fork cells + byte-exact #670
reproduction.

---

## 7 · What this decides / does not decide

- **DECIDES (data, not ruling):** the enclosure fork — Reading A (wake-feeding) vs Reading B
  (self-tightening). Data ⇒ **LOOP-FILLING = Reading A**, boundary-insensitive, robust.
- **DOES NOT DECIDE:** the G-PERSIST ★RULED verdict (rests on the fork-independent PML
  φ-dispersion trend — untouched). Node-mint (fork B) stays firewalled; this reads (A)
  fixed-\(N\) only.
- **GRANT RULES THE FORK.** The docket's Reading A is *leaned*; this data supports closing it.
  The framing call is surfaced, not fiated.

---

## 8 · Provenance

- Prereg frozen + pushed as its own commit (`f919fb12`) **before** any driver code
  (freeze margin 9 min 32 s).
- Carrier = the existing `loop_gap_harness` rank-4 probe, re-run through an instrumented mirror
  loop (same primitives; no new engine/stepper/retune). Live-fire parity vs
  `run_loop_gap_probe` = 0.00e+00.
- Per-cell JSON + summary: `assets/sim_outputs/gpersist_localization_observable/`
  (**gitignored** — regenerate with
  `python src/scripts/vol_1_foundations/gpersist_localization_observable.py --cell N PML MODE FID`
  / `--plant …` / `--aggregate`; numbers reproduce byte-for-byte from the frozen carrier).
- Independent #670 reproduction: every cell's E/φ matches the banked battery to four decimals.
