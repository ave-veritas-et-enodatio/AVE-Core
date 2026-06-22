# CLEAVE-01 / AVE-Bench-FemtoElectrometer — Session-Start Brief (SELF-CONTAINED)

**For:** a SEPARATE future agent/session working on the bench-hardware repo
`AVE-Bench-FemtoElectrometer`. That session will have **zero memory of the
session that wrote this brief.** This document therefore stands entirely on its
own — every fact, path, requirement ID, and stale-state item it needs is
in-line here. There is no "see the prior session."

**Authored:** 2026-06-22, from an AVE-Core worktree, read-only against the Femto
repo (per `cross-repo-session-scope`). Landed as a reviewed draft PR to AVE-Core.

**One-sentence charter for the separate session:** reconcile the Femto bench
repo onto the round-2 / chord-gated state, re-point its hardware docs to *cite*
(not duplicate) the canonical Vol-4 `CLV-REQ-*` requirements, fix the named
stale items, and stage the hardware re-spec mapped requirement-by-requirement —
**without making any of the OPEN design/make-vs-buy decisions** (those are
Grant + collaborator's call) and **without self-merging** (Grant merges).

---

## 0 — TABLE OF CONTENTS

1. CONTEXT — what Cleave-01 is and what it tests
2. ARCHITECTURE — the Vol-4-KB-is-truth / bench-repo-is-downstream split + the 21 CLV-REQ-* IDs
3. THE FEMTO REPO CURRENT STATE — the stale items, each as a concrete to-fix
4. THE TASKS for the separate session (a–e)
5. THE OPEN DECISIONS THAT GATE HARDWARE — D1–D6 + A1–A6 (STATUS:OPEN; do not decide)
6. DISCIPLINE for the separate session
7. REFERENCES — exact paths + inlined equipment-audit / spec-sheet findings

---

## 1 — CONTEXT: what Cleave-01 is

**Cleave-01 is the AVE-Bench-FemtoElectrometer** — a tabletop bench that tests
**AVE Axiom 2 (Topo-Kinematic Isomorphism: electric charge IS topological
spatial displacement, `[Q] ≡ [L]`)**. The canonical claim is
`clm-ydksh6`: `Q = ξ_topo · x`, where `ξ_topo = e / ℓ_node = 4.1490e-7 C/m`
is the electromechanical-transduction constant (charge-per-node-length).

**The physical experiment.** An isolated floating conductor (copper plate)
inside a hard-vacuum chamber is read by an ultra-low-bias electrometer
(ADA4530-1, 20 fA bias current) as `V = Q / C_in`. A facing grounded plate is
stepped away by a controlled displacement `x` via a piezo (PZT) actuator. Per
Axiom 2, one `e` per `ℓ_node` of relative displacement liberates a charge
`Q = ξ_topo · x` — `≈ 0.415 pC` per 1 µm of displacement.

**What it actually tests — the CHORD, not the slope (this is the load-bearing
reframe; the whole bench design follows from it):**

- The GO/NO-GO gates on a **gap-INDEPENDENT integer-charge floor** — the
  4-corner conjunction **{linear-in-x ∧ polarity-odd ∧ material-independent ∧
  gap-INDEPENDENT}** surviving a **≥4× geometric gap-sweep at fixed `C_in`**.
  This is a **resolution-gated BINARY falsifier for Axiom-2.** No single
  classical mechanism survives all four corners simultaneously.
- **The slope magnitude (0.415 pC/µm = 41.5 mV/µm at C_in=10 pF) is a NON-gating
  echo.** It is doubly over-determined (`ξ_topo = √α` in native units AND
  `ℓ_node` = the electron Compton wavelength), so a slope-match cannot by itself
  distinguish chord from α-chain, and a slope-deviation is NOT a falsification.
  The slope is a Level-2 secondary corroborator only.

**Why a gap-sweep (the round-2 cure).** The naive round-1 framing was
"SM predicts exactly 0.0 mV; any non-zero step confirms AVE." That is FALSE and
is the single biggest stale-framing error to purge. The dominant classical
background is **contact-potential-difference (CPD / moving-Kelvin-probe)**,
itself polarity-odd, at **~21.3% of the floor at the reference gap, scaling
∝1/g²**. So the standard-physics expectation is NOT zero — it is a
gap-DEPENDENT `∝1/g²` term. The discriminator is therefore not "0 vs non-zero
magnitude," it is a **SHAPE**: the `ξ_topo` floor is gap-INDEPENDENT (flat
across the sweep; `e/ℓ_node` is a pure constant), while CPD drops `∝1/g²`. The
≥4× gap-sweep is what separates them.

**The 4-corner faker-rejection table (each corner kills one mundane mechanism):**

| Mundane faker | Corner it fails | How separated |
|---|---|---|
| CPD / moving-Kelvin-probe (~21%-of-floor, itself polarity-odd) | gap-INDEPENDENT (CPD ∝ 1/g²) | ≥4× **gap-sweep**: CPD drops ∝1/g², floor stays flat |
| electrostriction / flexoelectric / secondary-piezo | polarity-ODD (these are even-in-V) | **displacement-direction reversal**: even fakers don't flip sign |
| triboelectric contact charging | static (tribo step **decays**) | **time-gating**: record relaxation profile |
| direct piezoelectric (d_ij) | material-INDEPENDENT (rides dielectric; zero in vacuum) | **dielectric-material swap** at fixed C_in |

**The C_in-held-fixed subtlety (load-bearing).** The measured *voltage* floor is
gap-independent only at **fixed readout capacitance `C_in`**. But the moving
plate-pair IS itself a `~1/g` capacitor, so a naive sweep changes `C_in` by ~4×
and contaminates the gap-independence corner. The gap-sweep MUST hold `C_in`
fixed (or explicitly account for it). A drifting `C_in` books as Outcome B
(re-run), not a false GO. This is the UNCLOSED design tension `CLV-REQ-CFIX`
(H3) — see §4(e) and §5 (knob D5).

**The false-null / resolution guard (anti-dead-instrument).** A null result
(no floor) counts as **Outcome C (Axiom-2 falsified)** ONLY IF a calibrated
positive-control injects a known ~0.415 pC charge that the chain resolves
in-session. Otherwise the null is a dead-instrument artifact = Outcome D, not a
falsification. This is `CLV-REQ-VALIDATE`.

**The outcome bins (GO/NO-GO gates on the CHORD; slope is non-gating):**

- **A — CHORD CONFIRMED (GO):** 4-corner conjunction survives the ≥4× gap-sweep
  at fixed `C_in`; positive-control passed in-session. Axiom-2 `[Q]≡[L]` confirmed
  at bench. Slope-match is a non-gating bonus; a slope-deviation books as
  A-with-α-chain-flag, it does NOT demote the GO.
- **B — partial (chord ambiguous):** floor detected but gap-sweep inconclusive
  (C_in drift / too few gaps / floor not separated from 1/g² CPD). NOT a GO; re-run.
- **C — null (CHORD FALSIFIED, NO-GO):** no gap-independent floor survives — charge
  absent within noise OR fully explained by 1/g² CPD — all corners checked AND
  positive-control passing. **Axiom-2 dies.** Largest single-row cascade in the
  matrix (B4-PROTEIN, C9-LEVITATION, C16-TORSION-05, B5/B6/B7-PONDER all fall);
  F-severity.
- **D — confound:** floor fails a corner OR positive-control did not register.
  Re-design guards; re-test. NOT adjudicated A or C.

---

## 2 — ARCHITECTURE (load-bearing): Vol-4 KB is the SINGLE SOURCE OF TRUTH; the bench repo is DOWNSTREAM

**The split is the central organizing principle of the whole effort. Internalize
it before touching a file:**

- **The Vol-4 KB leaf `cleave-01-requirements-boundary-conditions.md` (claim
  `clm-fuajdb`) is the SINGLE SOURCE OF TRUTH for every derived requirement.**
  Every number in it is either physics-set (forced by `{m_e, ℓ_node, e}` + the
  held-DC / multi-hour-sweep noise model) or written parametric in an OPEN design
  knob (`δ`, `C_in`). **The KB never holds part numbers and selects no design
  knob.**
- **The bench repo `AVE-Bench-FemtoElectrometer` is DOWNSTREAM.** It **CITES the
  Vol-4 `CLV-REQ-*` IDs and records only the IMPLEMENTATION** (chosen
  parts/board/chamber/SKUs). **The bench repo never re-derives physics.**
- The `CLV-REQ-*` IDs are **descriptive and reorder-proof** — each names the
  physics object it constrains (readout / gap / PZT / vacuum / thermal /
  vibration / EMI / calibration / a named master coupling), NOT a section number.
  A future §-reorder leaves every ID and every external citation intact.

**The exact Vol-4 files + claim-ids to cite** (paths relative to the AVE-Core
repo root; the bench repo references them as `../AVE-Core/...`):

| File | claim-id | Role |
|---|---|---|
| `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/cleave-01-requirements-boundary-conditions.md` | `clm-fuajdb` | **The derived-requirements truth-source** — the 21 `CLV-REQ-*` IDs + the REQ-ID INDEX |
| `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/cleave-01-trade-study-decision-register.md` | `no-claim` | The 6 make-vs-buy (A1–A6) + 6 design knobs (D1–D6), **STATUS:OPEN throughout, selects nothing** |
| `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md` | `clm-ydksh6` | The chord-gated falsification leaf (Axiom-2 hypothesis, 4-corner chord, outcome bins) |
| `_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01-phase-3-measurement-prereg.md` | (prereg, `exp-742kv5`) | The chord-gated measurement protocol (Level-1 chord = GO/NO-GO; Level-2 slope = non-gating) |
| `_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md` | (sub-epic) | The Q-C15 open-questions register (incl. Q-C15-13..18 ↔ the D1–D6 knobs) |

### THE 21 CANONICAL `CLV-REQ-*` IDs (the bench repo cites + builds to these)

These are the stable requirement identifiers. The bench repo's `TEST_PROCEDURE`,
`BOM`, and `reference_design` should be re-pointed to **reference these IDs**,
not to re-state the physics. (Source: the REQ-ID INDEX at the top of
`cleave-01-requirements-boundary-conditions.md`, `clm-fuajdb`.)

| # | REQ-ID | One-line requirement | OPEN knob(s) it depends on |
|---|---|---|---|
| 1 | `CLV-REQ-FLOOR` | The derived floor `dQ/dx = ξ_topo = e/ℓ_node = 414.9 fC/µm` the bench must detect (zero free params) | none (physics-set) |
| 2 | `CLV-REQ-CPL-A` | Master coupling A — position→charge: `dV/dx = ξ_topo/C_in = 41.49 nV/pm`; gap jitter rides the signal transfer function (non-averageable) | C_in (D2) |
| 3 | `CLV-REQ-CPL-B` | Master coupling B — 1/f + drift noise model (held-DC step over multi-hour sweep); binding spec = LEVEL STABILITY, not single-shot resolution | none (physics-set) |
| 4 | `CLV-REQ-CPL-C` | Master coupling C — CPD systematic ~21.3% of floor ∝1/g²; 19.97%-of-floor swing the chord-shape must beat across the sweep | none (physics-set) |
| 5 | `CLV-REQ-CPL-D` | Master coupling D — 20 fA bias-current ramp = 20.0 fC/s rails a passive node ⇒ step-differencing / DC-restore / reset-integration mandatory (a topology BC) | readout topology (D3) |
| 6 | `CLV-REQ-READOUT` | Charge-readout chain: in-band noise floor, charge-domain level resolution, ENOB, sub-Hz BW, C_in inheritance, validate-on-known | δ (D1), C_in (D2), topology (D3) |
| 7 | `CLV-REQ-DRIFT` | Readout LEVEL STABILITY (the GATING readout spec): drift-referred-to-charge ≤ δ×414.9 fC AND beat the 83 fC CPD swing; reached by ARCHITECTURE | δ (D1), drift scheme (D4) |
| 8 | `CLV-REQ-GAP` | Gap-actuation + metrology: closed-loop linear nanopositioner; travel ratio, resolution/repeatability/INL/hold, gap-knowledge, linear-DOF, thermal gap drift | δ (D1), g₀/stroke (D6), stage make-vs-buy (A6) |
| 9 | `CLV-REQ-CFIX` | `C_in`-FIXED across the ≥4× sweep (the moving plate IS a 1/g cap): `\|dC_in/C_in\| ≤ δ/k` (UNCLOSED tension) | C_in-fixed topology (D5) |
| 10 | `CLV-REQ-PZT` | PZT-drive (sub-yield, NOT a field-bias chain): drive-noise mechanical + electrostatic paths, synchronous-step confound, DC stability, range | C_in (D2), g₀/stroke (D6) |
| 11 | `CLV-REQ-VAC` | Vacuum ≤10⁻⁶ Torr (surface-leakage + patch-stationarity driver, NOT arc-breakdown); ion-gauge filament OFF during read | none (physics-set); A4/A5 make-vs-buy |
| 12 | `CLV-REQ-THERMAL` | Thermal `dT ≤ 1 K` over the sweep + 2× calibrated RTDs logged (derived; NOT the binding systematic) | none (physics-set); CTE fixturing (A3/A4) |
| 13 | `CLV-REQ-VIB` | Vibration/seismic (the BINDING environmental systematic): gap RMS jitter ≤ 14.6 pm in 1–50 Hz + turbo-decouple | C_in (D2); isolation/stage make-vs-buy (A6) |
| 14 | `CLV-REQ-EMI` | EMI/Faraday SE 64–84 dB + break the BNC-shield→chamber→gauge ground loop + guarded triax | none (physics-set); design/discipline |
| 15 | `CLV-REQ-CAL` | Calibration / in-situ-C / charge-reference: in-situ C_in split-by-level + one-instrument-three-jobs charge-injection reference | δ (D1); C_in method (D5), reference topology (A6) |
| 16 | `CLV-REQ-VALIDATE` | Validate-on-known (anti-false-null, gates Outcome C): inject ~0.415 pC, resolve to ≤0.1× floor in-session before trusting V=Q/C | none (physics-set); reference topology (A6) |
| 17 | `CLV-REQ-H1` | Hardest item H1 — readout level stability sub-µV over the multi-hour sweep (= `CLV-REQ-DRIFT`, NEAR EDGE) | δ (D1), drift scheme (D4) |
| 18 | `CLV-REQ-H2` | Hardest item H2 — gap HOLD pm-class + VIBRATION isolation together (= `CLV-REQ-VIB`+`CLV-REQ-GAP`, AT EDGE) | C_in (D2); stage+isolation (A6) |
| 19 | `CLV-REQ-H3` | Hardest item H3 — `C_in`-FIXED across the sweep (= `CLV-REQ-CFIX`, UNCLOSED) | C_in-fixed topology (D5) |
| 20 | `CLV-REQ-H4` | Hardest item H4 — absolute + relative gap-knowledge for the flat-vs-1/g² fit (= part of `CLV-REQ-GAP`; swap to closed-loop) | g₀/stroke (D6), stage make-vs-buy (A6) |
| 21 | `CLV-REQ-H5` | Hardest item H5 — travel/stroke ≥4× feasibility BLOCKER (15–30 µm actuators CANNOT execute the sweep; = part of `CLV-REQ-GAP`) | g₀/stroke (D6), stage make-vs-buy (A6) |

> `CLV-REQ-H1..H5` are **aliases-by-severity** onto the load-bearing primary IDs
> (`CLV-REQ-DRIFT`, `CLV-REQ-VIB`/`CLV-REQ-GAP`, `CLV-REQ-CFIX`), preserved as
> their own IDs so the §8 hardest-items register is independently citable. They
> name the same physics, not a new requirement.

---

## 3 — THE FEMTO REPO CURRENT STATE (the stale items found; each a concrete to-fix)

The Femto repo is at `/Users/grantlindblom/AVE-staging/AVE-Bench-FemtoElectrometer`
(GitHub: `https://github.com/ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer`,
private). State as of 2026-06-22, verified read-only by grep:

### 3.0 — Git state: HEAD is on a STALE pre-round-2 branch

- **HEAD branch = `ci/mirror-core-tooling`.** This is the on-disk default checkout.
- **`main` is NOT an ancestor of HEAD.** `git rev-list --left-right --count
  main...HEAD` returns `6  0` — i.e. **main is 6 commits AHEAD; HEAD is a stale
  checkout that PREDATES 6 commits already merged to main.** HEAD has zero
  commits main lacks.
- **The 6 commits HEAD is missing are the round-2 cure**, including:
  - `78a86f6` merge: Cleave-01 round-2 SM-counterfactual + gap-sweep upgrade
  - `76f66b9` Cleave-01 round-2: quantitative SM-counterfactual — VERDICT PARTIAL→SURVIVES (gap-sweep)
  - `e05012f` merge: Cleave-01 two-sided dielectric-invariance discriminator
- **The round-2 cure already lives on `main`** in:
  `docs/analysis/2026-06-03_cleave-two-sided-discriminator.md`,
  `docs/analysis/2026-06-04_cleave-round2-prereg.md`,
  `docs/analysis/2026-06-04_cleave-round2-smcounterfactual-result.md`,
  `scripts/round2_sm_counterfactual.py`, plus round-2 edits to
  `hardware/TEST_PROCEDURE.md`, `docs/glossary.md`, `docs/open_questions.md`,
  `manuscript/vol_cleave_01/chapters/04_falsification_metric.tex`.
  **But the cure did NOT propagate to every stale site** — that un-landed
  remainder is flagged in the round-2 doc as F-R2-3, and is what this brief's
  tasks address.

  **TO-FIX:** reconcile the working tree onto the round-2/main state (Task a).
  Do NOT just `git checkout main` and assume done — the round-2 cure is
  *incomplete* on main too (the stale sites below persist). The job is the
  reconciliation PLUS the propagation.

### 3.1 — Round-1 framing still present ("SM = exactly 0.0"; slope-gated, not chord-gated)

The naive round-1 discriminator framing survives in multiple sites and must be
purged in favor of the chord-gated round-2 framing:

- `docs/open_questions.md:51` — *"Vacuum-gap-only: ... standard EE predicts
  `Q → 0` ... The starkest contrast; the cleanest single-axis test."* **STALE.**
  Standard physics does NOT predict 0 — CPD gives a ~21%-of-floor `∝1/g²`
  background. The chord is gap-independence (a SHAPE), not a 0-vs-nonzero call.
- `docs/glossary.md:41` — the "Dielectric-independence discriminator" glossary
  entry frames the test as slope/dielectric-variance, not as the 4-corner chord.
- `docs/design/2026-05-20_initial_scoping.md:59` — preserves *"if 0.0 mV the
  framework is falsified"* verbatim as a round-1 orchestrator constraint. **STALE.**
- `hardware/TEST_PROCEDURE.md:93,97,100` — the §5 dielectric-independence section
  still says *"standard EE predicts `Q → 0`"* and frames Outcome A as a
  **slope-match** (`§6` decision tree: *"Compare measured slope vs 41.5 mV/μm"*),
  NOT the 4-corner gap-independence chord.
- `hardware/TEST_PROCEDURE.md` §4 "Measurement procedure" + §6 "Decision tree" —
  the whole adjudication is **slope-gated** (Outcome A = "slope matches 41.5
  mV/μm AND dielectric independence"). The round-2 cure makes the **chord** the
  GO/NO-GO and the **slope a non-gating echo**. This is the single largest
  framing fix.

  **TO-FIX:** re-point the discriminator/decision-tree/outcome framing to the
  chord (4-corner gap-independence) per the canonical
  `project-cleave-01.md` "The Falsification Metric" + "Outcome adjudication"
  sections and the Phase-3 prereg §4/§5/§6/§7 (Task c).

### 3.2 — PicoScope 2204A mislabelled "10-bit ENOB" (it is 8-bit)

- `hardware/TEST_PROCEDURE.md:29` — *"Oscilloscope | 10-bit ENOB at 1 kHz BW |
  Pico Tech PicoScope 2204A"*. **WRONG.** The PicoScope 2204A is an **8-bit**
  USB scope (Pico's 2000-series is 8-bit; only the 5000-series flexible-resolution
  models like the 5242D alt are 12–16 bit). An 8-bit scope on a ±50 mV range is
  ~390 µV/LSB — the Vol-4 leaf §3.3 explicitly states *"An 8-bit scope (390
  µV/LSB) is the wrong instrument class"* (it is ~400× short of the drift-corrected
  level-stability spec).
- Same mislabel propagates to `hardware/BOM.md:112` (*"2-channel, 10-bit ENOB"*),
  `docs/procurement_action_items.md:114-116` (*"10-bit-ENOB-class oscilloscope"*).

  **TO-FIX:** correct the bit label to **8-bit** everywhere AND record that an
  8-bit scope is the wrong instrument class per `CLV-REQ-READOUT` §3.3 (the
  binding readout is a drift-corrected sub-µV LEVEL on a 100 mV span, needing an
  18–24-bit ΔΣ front-end OR a 6.5–7.5-digit DMM in DC mode — the ΔΣ-vs-DMM
  choice is OPEN knob A6, do not pick it). The scope swap is a trivial COTS
  change; the point is the *instrument class*, not the SKU. (Task d.)

### 3.3 — ">5 K drift pause" operator rule (the derived requirement is ≤1 K)

- `hardware/TEST_PROCEDURE.md:167` — *"Lab-temperature drift `> 5 K` | Pause
  acquisition"*. **STALE / ~4× too loose.** The derived `CLV-REQ-THERMAL` spec
  (Vol-4 §6.2) is `dT ≤ 1 K` over the sweep (Vos drift referred to the floor
  needs `dT_sweep < 1.21 K` max-tempco) + 2× calibrated RTDs logged with the
  data. The Phase-3 prereg §5.9 already states the `≤1 K` rule SUPERSEDES the
  ">5 K pause." The ">5 K" string is verified ABSENT from every AVE-Core-side
  cleave file; it lives ONLY in the Femto-side `TEST_PROCEDURE.md`.

  **TO-FIX:** change ">5 K" → **"≤1 K"** per `CLV-REQ-THERMAL`, and add the
  2×-calibrated-RTD-logging requirement. (Task d.)

### 3.4 — Single-1µm-step framing (superseded by the ≥4× gap-sweep)

- `hardware/TEST_PROCEDURE.md` §4 "Measurement procedure" + the
  "Voltage-displacement sweep" table (steps at 0.5/1.0/1.5/2.0 µm) — this is a
  **single-baseline-gap displacement sweep**, NOT the **≥4× geometric
  gap-sweep** the chord requires. A displacement-amplitude sweep at one baseline
  gap cannot separate the flat `ξ_topo` floor from the `∝1/g²` CPD background.
- The canonical `project-cleave-01.md` "The PCBA Implementation" (line 28) is
  **already aligned on the AVE-Core side** to the ≥4× gap-sweep; the Femto-side
  `TEST_PROCEDURE.md` still carries the obsolete single-step framing. This is the
  ROOT CAUSE of the under-spec'd mechanical chain (it's specced to the wrong
  measurement).

  **TO-FIX:** replace the single-baseline displacement sweep with a **≥4 baseline
  gaps spanning a ≥4× geometric gap-sweep** (geometric spacing, ratio ~1.587/step
  over 4 points), at fixed `C_in`, per `CLV-REQ-GAP` §4.1 + the prereg §5.1. The
  per-point ~1 µm displacement modulation is retained (it liberates the 0.415 pC
  read), but the GATING axis is the across-baseline-gap flatness, not the
  single-step magnitude. (Task d.)

### 3.5 — 15–30 µm actuator (cannot execute the ≥4× gap-sweep; the H5 feasibility BLOCKER)

- `hardware/BOM.md:77` — PZT1 = PI `P-016.20H` (or `P-820.10`), a commodity
  **open-loop ~15–30 µm-class** piezo actuator (1 µm step, ~100 V drive, M3
  mount). `hardware/BOM.md:81` — mounts MNT1 = Thorlabs `KMS` / `POLARIS-K1`,
  which are mirror-**TILT** kinematic mounts (the WRONG degree of freedom — the
  plates must TRANSLATE along the gap normal staying parallel; tilt changes
  `C_in`).
- **This is `CLV-REQ-H5` / `CLV-REQ-GAP` §4.1 — a feasibility BLOCKER, not a
  tolerance.** A 15–30 µm-travel actuator **CANNOT execute a ≥4× gap-sweep at a
  ~100 µm baseline at all** (that needs ~300 µm of closed-loop travel for
  `g₀→4g₀`). Open-loop PZT additionally fails `CLV-REQ-GAP` §4.2 by ~100× on
  resolution/repeatability/creep, and cannot place `g` for the absolute/relative
  gap-knowledge `CLV-REQ-H4` needs.

  **TO-FIX (RE-SPEC, do not pick the SKU):** flag that the gap-actuation
  subsystem must become a **closed-loop, capacitive-sensor, flexure-guided LINEAR
  nanopositioner** with travel meeting the ≥4× ratio (≥300 µm at g₀≈100 µm, OR a
  de-spec'd g₀≈10–25 µm widening the vendor list to commodity closed-loop
  travel). The **absolute g₀/stroke is OPEN knob D6** — do not select it; set up
  the spec so it's ready once D6 + A6 are frozen. (Task e.)

### 3.6 — Other verified-stale cross-cites (fix in passing)

- `hardware/TEST_PROCEDURE.md:37` + the Femto `CLAUDE.md` cite
  `constants.py:205` for `ξ_topo`. **STALE LINE.** Verified 2026-06-22: the
  canonical lines are `XI_TOPO:291`, `L_NODE:257`, `e_charge:100` in
  `AVE-Core/src/ave/core/constants.py`. (Line 205 is unrelated commentary.) The
  *value* `4.149e-7 C/m` is correct; only the line number drifted. Per
  `ave-canonical-source`, never hard-code the value — import from
  `ave.core.constants`.
  **TO-FIX:** correct the line cite to `:291` (or, better, drop the line number
  and cite the symbol `XI_TOPO` — line numbers drift). (Task d, in passing.)
- `hardware/TEST_PROCEDURE.md:5` Header *"Status: SCAFFOLD STAGE. BENCH UNBUILT."*
  is accurate and should be PRESERVED (per `ave-evidence-framing-discipline` —
  never inflate scaffold to fab-ready).

---

## 4 — THE TASKS for the separate session

Execute in order. Each is a Femto-repo edit on a Femto-repo branch off `main`,
pushed but NOT merged (Grant merges; see §6).

### (a) Reconcile the repo onto the round-2 / main state

The on-disk HEAD is the stale `ci/mirror-core-tooling` branch (6 commits behind
`main`; main is NOT an ancestor — §3.0). Bring the working state to the round-2
baseline before doing anything else:

- Branch off **`main`** (which carries the round-2 cure), not off the stale
  `ci/mirror-core-tooling` HEAD. Confirm with `git branch --show-current` after
  any sub-agent invocation (the Femto repo's pre-commit discipline).
- Verify you can see the round-2 artifacts on disk (the
  `docs/analysis/2026-06-04_*` files, `scripts/round2_sm_counterfactual.py`).
- The reconciliation is NOT "done" at the checkout — the round-2 cure is itself
  incomplete (the §3.1–3.5 stale sites persist on main). Tasks (b)–(e) finish it.

### (b) RE-POINT TEST_PROCEDURE / BOM / reference_design to CITE the Vol-4 CLV-REQ-* requirements

This is the architectural fix (§2): the bench repo **references** the canonical
requirements; it does not duplicate or re-derive them.

- In `hardware/TEST_PROCEDURE.md`, `hardware/BOM.md`,
  `hardware/cad/reference_design.md`: wherever a physics requirement is currently
  stated inline (noise floor, `C_in`, gap-sweep, drift threshold, vacuum level,
  thermal, vibration), **replace the inline derivation with a citation to the
  matching `CLV-REQ-*` ID** in
  `../AVE-Core/manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/cleave-01-requirements-boundary-conditions.md`
  (`clm-fuajdb`). Keep the IMPLEMENTATION record (chosen SKU/board/chamber); strip
  the re-derived physics.
- Map each bench subsystem to its REQ-IDs (use the §2 table + the per-`CLV-REQ-*`
  derivations). Example mappings: the electrometer front-end → `CLV-REQ-READOUT`
  + `CLV-REQ-CPL-D` + `CLV-REQ-EMI`; the gap stage → `CLV-REQ-GAP` +
  `CLV-REQ-VIB` + `CLV-REQ-CFIX`; the PZT drive → `CLV-REQ-PZT`; the chamber →
  `CLV-REQ-VAC`; the thermal shroud → `CLV-REQ-THERMAL`; the charge-cal reference
  → `CLV-REQ-CAL` + `CLV-REQ-VALIDATE`.
- **Reference-don't-duplicate.** If you find yourself re-stating a derived number
  with its derivation, stop and cite the REQ-ID instead.

### (c) Sync the round-2 cure + chord-gating

Make the bench docs chord-gated, matching the canonical `project-cleave-01.md`
and the Phase-3 prereg:

- Replace the slope-match GO/NO-GO with the **4-corner gap-independence chord**
  as the GATING axis; demote the slope (41.5 mV/µm) to a **non-gating Level-2
  echo**. Rewrite the §6 decision tree in `TEST_PROCEDURE.md` to gate on the
  4-corner conjunction surviving the ≥4× gap-sweep at fixed `C_in` (Outcome A),
  with Outcomes B/C/D per the canonical bins (§1 of this brief).
- Land the **false-null / resolution guard** (`CLV-REQ-VALIDATE`): a null is
  Outcome C only if a calibrated ~0.415 pC positive-control registered
  in-session; otherwise it's Outcome D (dead-instrument).
- Land the **`C_in`-fixed subtlety**: the gap-sweep must hold `C_in` fixed (or
  account for it); a drifting `C_in` books as Outcome B, not a false GO
  (`CLV-REQ-CFIX`).
- Purge the round-1 "SM = exactly 0.0" framing from `docs/open_questions.md:51`,
  `docs/glossary.md:41`, `docs/design/2026-05-20_initial_scoping.md:59`, and the
  `TEST_PROCEDURE.md` §5 — replace with the CPD `∝1/g²` ~21%-of-floor background +
  gap-sweep-separates framing.

### (d) Fix the named stale items

Concrete, mechanical fixes (each maps to §3):

- **8-bit mislabel** (§3.2): PicoScope 2204A "10-bit ENOB" → **8-bit**, in
  `TEST_PROCEDURE.md:29`, `BOM.md:112`, `docs/procurement_action_items.md:114-116`;
  record that an 8-bit scope is the wrong instrument class per `CLV-REQ-READOUT`
  §3.3 (the binding readout is a drift-corrected sub-µV LEVEL needing 18–24-bit ΔΣ
  / 6.5–7.5-digit DMM — the choice is OPEN A6, do not pick).
- **Drift pause** (§3.3): `TEST_PROCEDURE.md:167` ">5 K" → **"≤1 K"** per
  `CLV-REQ-THERMAL`; add 2× calibrated RTDs logged with the data.
- **Single-1µm-step → ≥4× sweep** (§3.4): replace the single-baseline displacement
  sweep (`TEST_PROCEDURE.md` §4 table) with the **≥4 baseline gaps spanning ≥4×**
  geometric gap-sweep at fixed `C_in` per `CLV-REQ-GAP` §4.1 + prereg §5.1.
- **15–30 µm → ≥300 µm closed-loop** (§3.5): re-spec the gap-actuation subsystem to
  a closed-loop linear nanopositioner with ≥4×-ratio travel per `CLV-REQ-GAP` /
  `CLV-REQ-H5` (the absolute g₀/stroke is OPEN D6 — do not select).
- **Stale constant cite** (§3.6): `constants.py:205` → cite symbol `XI_TOPO`
  (canonical line `:291`); never hard-code `4.149e-7`.

### (e) The HARDWARE RE-SPEC, requirement-by-requirement (flag where current hardware FAILS each)

Produce a re-spec table in the Femto repo (e.g. a `hardware/RE-SPEC.md` or a
section in `TEST_PROCEDURE.md`/`BOM.md`) mapping each load-bearing `CLV-REQ-*` to
the current hardware and flagging the FAIL. **Set up the spec to be ready once
the OPEN knobs freeze; do NOT select the knob.** The four current FAILS:

| `CLV-REQ-*` | Requirement (the bench must meet) | Current Femto hardware | Verdict |
|---|---|---|---|
| `CLV-REQ-GAP` / `CLV-REQ-H5` / `CLV-REQ-H4` | closed-loop linear nanopositioner, ≥4× travel (≥300 µm @ g₀≈100 µm), ~nm repeatability, places g absolutely+relatively | PI `P-016.20H` open-loop ~15–30 µm PZT + Thorlabs `KMS`/`POLARIS-K1` TILT mounts | **FAIL** — travel ~10× short (feasibility blocker); open-loop fails resolution ~100×; tilt is the wrong DOF. Re-spec to closed-loop cap-sensor LINEAR stage (BUY, A6). g₀/stroke OPEN (D6). |
| `CLV-REQ-DRIFT` / `CLV-REQ-READOUT` / `CLV-REQ-H1` | drift-corrected sub-µV LEVEL stability on a 100 mV span (18–24-bit ΔΣ / 6.5–7.5-digit DMM) + a drift-rejection ARCHITECTURE | PicoScope 2204A 8-bit scope (~390 µV/LSB) | **FAIL** — ~400× short; wrong instrument class. The cure is ARCHITECTURE (auto-zero/chopper/CDS OR cRIO gap-dither lock-in), NOT a better scope. Digitizer + drift-scheme are OPEN (A6, D4). |
| `CLV-REQ-VIB` / `CLV-REQ-H2` | gap RMS jitter ≤ 14.6 pm in 1–50 Hz (`= V_floor / 41.49 nV/pm`) + turbo-decouple | no vibration-isolation subsystem specced; turbo `nEXT85D-T` mounted directly (a vibration SOURCE) | **FAIL/MISSING** — the BINDING environmental systematic is un-specced. Re-spec isolation (transmissibility T < 3e-4 to 1.5e-5 across 1–50 Hz) + decouple/valve-off the turbo during reads. Isolation/stage make-vs-buy OPEN (A6). |
| `CLV-REQ-CFIX` / `CLV-REQ-H3` | `\|dC_in/C_in\| ≤ δ/k` across the ≥4× sweep (the moving plate IS a ~1/g cap) | not addressed (`C_in` treated as a static board parasitic; Q-C15-04 ignores the 1/g motion-dependence) | **FAIL/UNCLOSED** — the moving plate-pair swings ~4× across the sweep; FATAL if it IS `C_in`. Resolution (fixed-ref-cap + weak-coupling sweep electrode VS in-situ-measure-and-divide) is OPEN knob D5 — flag, do not resolve. |

Also flag, but lower-severity: `CLV-REQ-CPL-D` (the bare-follower-into-passive-10pF-node
topology in `reference_design.md` §9 has NO DC bleed path — the 20 fA = 20.0
fC/s ramp RAILS it; the cure follower+differencing-vs-charge-reset-integrator is
OPEN knob D3); `CLV-REQ-CAL`/`CLV-REQ-VALIDATE` (the charge-injection reference
is un-specced — it's the one in-house MAKE-fragment, and it simultaneously closes
in-situ `C_in` + the anti-false-null gate; reference topology OPEN A6).

> **The discipline for (e):** name the FAIL against the requirement, name which
> OPEN knob gates the cure, and STOP. Do not pick the replacement SKU, the digitizer
> class, the drift scheme, the isolation table, or the `C_in`-fixed topology. The
> re-spec makes the gaps audit-able and the repo build-ready *once Grant +
> collaborator freeze the knobs* (§5).

---

## 5 — THE OPEN DECISIONS THAT GATE HARDWARE (D1–D6 + A1–A6: STATUS:OPEN — DO NOT DECIDE)

**These are Grant + collaborator's call, in a separate decision session. The
separate hardware session MUST NOT make them.** It sets the repo up to be ready
once they're frozen, and flags where each is needed. Source:
`cleave-01-trade-study-decision-register.md` (`no-claim`; STATUS:OPEN throughout;
selects nothing). Each design knob is also a Q-C15 register entry
(`exp-c15-cleave-01.md`): D1↔Q-C15-13, D2↔Q-C15-14, D3↔Q-C15-15, D4↔Q-C15-16,
D5↔Q-C15-17, D6↔Q-C15-18.

### Team-capability framing (carried into every build-vs-buy, NOT a selection)

- **Grant** — staff EE (Tesla Megapack thermal); can build the femto-amp PCB, the
  PZT-drive / HV-class board, and the thermal control; owns an NI cRIO-9014 +
  9263 (AO) + 9215 (AI) = a DC–40 kHz 4×4 phase-coherent lock-in bench.
- **Collaborator** — scrappy, high-quality vacuum chambers + fixturing.
- **Buy-side (the precision metrology the team does NOT self-build):** the
  closed-loop nanopositioner + capacitive gap sensor (≥300 µm, pm-class), the
  charge-cal reference, the pump/gauge, and the precision readout digitizer.

### The 6 DESIGN KNOBS (D1–D6) — each STATUS:OPEN

| Knob | Decision | REQ-IDs it touches | Q-C15 |
|---|---|---|---|
| **D1** | `δ`: freeze `δ_chord` (gating, ~10%) vs `δ_slope` (non-gating, ~5%) | `CLV-REQ-READOUT`, `CLV-REQ-DRIFT`, `CLV-REQ-GAP`, `CLV-REQ-CAL` | Q-C15-13 |
| **D2** | `C_in`: 10 pF vs 1 pF (THE single biggest lever; 1 pF raises the floor 10×) | `CLV-REQ-CPL-A`, `CLV-REQ-READOUT`, `CLV-REQ-DRIFT`, `CLV-REQ-VIB` | Q-C15-14 |
| **D3** | Readout front-end topology: follower+differencing vs charge-reset integrator | `CLV-REQ-CPL-D`, `CLV-REQ-READOUT` | Q-C15-15 |
| **D4** | Drift-rejection scheme: auto-zero/chopper/CDS vs cRIO gap-dither + lock-in (cRIO is an OPTION, not a decision) | `CLV-REQ-DRIFT` (=H1), `CLV-REQ-CPL-B` | Q-C15-16 |
| **D5** | `C_in`-fixed-vs-gap-motion topology: fixed-ref-cap + weak-coupling sweep electrode vs in-situ-measure-and-divide (the UNCLOSED H3 tension; resolve BEFORE freezing gap hardware) | `CLV-REQ-CFIX` (=H3), `CLV-REQ-CAL` | Q-C15-17 |
| **D6** | Baseline gap `g₀` + sweep range + N (≥4× RATIO is physics-set; absolute `g₀`/stroke is OPEN; 15–30 µm actuators CANNOT execute the sweep = H5 blocker) | `CLV-REQ-GAP` (=H5), `CLV-REQ-PZT`, `CLV-REQ-CPL-C` | Q-C15-18 |

### The 6 MAKE-vs-BUY (A1–A6) — each STATUS:OPEN

| ID | Subsystem | Builds to REQ-IDs | Recorded leaning (NOT a selection) |
|---|---|---|---|
| **A1** | Femto-amp PCB (ADA4530-1 + guard ring + Teflon standoffs) | `CLV-REQ-READOUT`, `CLV-REQ-CPL-D`, `CLV-REQ-EMI`, `CLV-REQ-CAL` | leaning MAKE (Grant; the one design-complete subsystem) |
| **A2** | PZT-drive / HV-class board (DAC + piezo amp + driven shield) | `CLV-REQ-PZT` (+ couples `CLV-REQ-VIB`, `CLV-REQ-GAP`) | OPEN; collapses into A6-BUY if D6 goes closed-loop-servo |
| **A3** | Thermal control (shroud + RTD logging, ≤1 K) | `CLV-REQ-THERMAL` | leaning MAKE (Grant; Tesla-thermal domain) |
| **A4** | Vacuum chamber + fixturing (≤10⁻⁶ Torr, oil-free, PARALLELISM) | `CLV-REQ-VAC`, `CLV-REQ-GAP` (§4.4 parallelism), `CLV-REQ-VIB` (turbo-decouple), couples `CLV-REQ-CFIX` | leaning MAKE (collaborator) |
| **A5** | Pump / gauge train (turbo + dry scroll + ion gauge) | `CLV-REQ-VAC`, couples `CLV-REQ-VIB` | BUY-or-REUSE, not MAKE |
| **A6** | Precision metrology (closed-loop nanopositioner + cap gap sensor + charge-cal reference + readout digitizer) | `CLV-REQ-GAP`, `CLV-REQ-VIB`, `CLV-REQ-READOUT`, `CLV-REQ-DRIFT`, `CLV-REQ-CAL`, `CLV-REQ-VALIDATE`, `CLV-REQ-CFIX` | BUY the metrology; the charge-cal reference is the one MAKE-fragment |

### Dependency map (which decisions must freeze TOGETHER — flag, do not resolve)

- **D2 (`C_in`)** with A6 (digitizer ENOB) + D4 (drift) — `C_in` sets the voltage
  floor ⇒ the ENOB + drift budgets.
- **D3 (topology)** with A1 (PCB) + A6 (digitizer) — integrator vs follower changes
  the feedback network + whether a high-ENOB ADC is needed.
- **D5 (`C_in`-fixed)** with A4 (fixturing) + A6 (stage) + D6 (`g₀`) — the unclosed
  H3 tension is mechanical OR metrological depending on D5; **resolve before
  freezing gap hardware.**
- **D6 (`g₀`/stroke)** with A6 (stage) + A2/A6 (drive) — the ≥4× stroke sets the
  stage travel + drive range; the 15–30 µm actuators can't do it (H5).
- **A2 (drive)** with A6/D6 (closed-loop stage) — drive + stage are ONE
  closed-loop problem; a servo controller subsumes the discrete drive.
- **D4 (drift)** with A6 (cRIO/digitizer) — the sub-µV LEVEL stability (H1) is an
  ARCHITECTURE choice, not an ADC choice.

> **Standing rule (from the trade-study leaf): SELECT NOTHING.** Every entry ends
> STATUS:OPEN. The separate hardware session makes the repo *ready* for these
> decisions and flags where each gates a spec; it does not adjudicate them.

---

## 6 — DISCIPLINE for the separate session

- **This IS the cross-repo session** (per `cross-repo-session-scope`). The
  AVE-Core-side propagation (the canonical leaves + the prereg) is already landed;
  the Femto-side propagation is the tracked follow-on, and it is YOUR job. The
  round-2 doc on Femto `main` flags this un-landed remainder as **F-R2-3**.
- **NEVER self-merge. Grant merges.** Branch off `main`, do the work, push the
  branch, open the PR, STOP. The Femto repo's own PRs go through review — do not
  `git merge` / `git push` to `main` / fast-forward `main`.
- **Reference-don't-duplicate.** The bench repo CITES the Vol-4 `CLV-REQ-*` IDs;
  it never re-derives physics or copies derived numbers with their derivation.
  When in doubt, cite the REQ-ID and the canonical leaf path.
- **`verify-before-cite`.** Before citing any AVE-Core file:line, verbatim quote,
  or `constants.py` value, Read it and grep it. Line numbers drift (the
  `constants.py:205` → `:291` case in §3.6 is exactly this failure). Prefer citing
  the symbol (`XI_TOPO`) over the line number. The REQ-IDs are descriptive and
  reorder-proof — cite the ID, not a section number.
- **`ave-canonical-source`.** Import `ξ_topo`, `ℓ_node`, `e` from
  `ave.core.constants`; never hard-code `4.149e-7`.
- **`ave-evidence-framing-discipline`.** Preserve the accurate "SCAFFOLD STAGE.
  BENCH UNBUILT." status; never inflate scaffold to fab-ready. The 4 hardware
  FAILS (§4e) are real and must be stated as FAILS, not softened.
- **Flag-don't-fix on physics.** If the engine/hardware reality conflicts with the
  corpus, surface the conflict with both file paths + verbatim content; do not
  reframe one to match the other. Surface the empirical finding and let the
  auditor / Grant adjudicate — do not draft the auditor's manual entry or make a
  framing-level call yourself.
- **Femto pre-commit discipline.** Run `git branch --show-current` after ANY
  sub-agent / Task invocation (sub-agents share the working tree and may leave it
  on their branch). The Femto repo has a `verify` workflow + ruff pre-commit hooks
  (mirrored from AVE-Core) — run them before committing.
- **Pure-AVE-corpus.** Every tracked file (docs, drivers, commit messages, branch
  descriptions) MUST be pure physics. No external-context refs.

---

## 7 — REFERENCES (exact paths + inlined findings so the separate session needs no /tmp access)

### Canonical AVE-Core paths (the truth-source the bench repo cites)

All paths relative to the AVE-Core repo root
(`/Users/grantlindblom/AVE-staging/AVE-Core/`); the bench repo references them as
`../AVE-Core/...`.

- **Requirements leaf (truth-source, `clm-fuajdb`):**
  `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/cleave-01-requirements-boundary-conditions.md`
  — the REQ-ID INDEX (21 `CLV-REQ-*`) + §1 floor/master-couplings + §2 chord/slope
  reframe + §3 readout + §4 gap + §5 PZT + §6 environment + §7 calibration + §8
  hardest-items register.
- **Trade-study / decision register (`no-claim`, STATUS:OPEN):**
  `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/cleave-01-trade-study-decision-register.md`
  — A1–A6 make-vs-buy + D1–D6 design knobs + the Part C dependency map.
- **Chord-gated falsification leaf (`clm-ydksh6`):**
  `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md`
  — Axiom-2 hypothesis, the 4-corner chord, the faker table, the C_in-fixed
  subtlety, the node-occupation-CLOSED derivation, outcome bins A/B/C/D.
- **Phase-3 measurement prereg:**
  `_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01-phase-3-measurement-prereg.md`
  — §4 discriminator (chord vs echo), §5 controls (the 4-corner machinery +
  positive-control), §6 outcome bins, §7 falsifier, §9 Femto-side propagation
  status, §10 spend-decision package.
- **Sub-epic + Q-C15 register (incl. Q-C15-13..18 ↔ D1–D6):**
  `_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md`
  — open-questions table; Q-C15-13..18 entries at lines 147–152.
- **Canonical constants (verified 2026-06-22):**
  `src/ave/core/constants.py` — `e_charge:100` (`1.602176634e-19 C`),
  `L_NODE:257` (`HBAR/(M_E*C_0) ≈ 3.8616e-13 m`), `XI_TOPO:291`
  (`e_charge/L_NODE ≈ 4.149e-7 C/m`). Import the symbols; never hard-code.

### Femto repo paths (the downstream repo to edit)

Root: `/Users/grantlindblom/AVE-staging/AVE-Bench-FemtoElectrometer`
(GitHub `ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer`, private).

- `hardware/TEST_PROCEDURE.md` — operator-facing procedure (the most stale file:
  8-bit mislabel :29, >5K :167, single-step §4, stale constant cite :37, round-1
  framing §5).
- `hardware/BOM.md` — bill of materials (PZT P-016.20H :77, KMS/POLARIS-K1 tilt
  mounts :81, PicoScope 2204A "10-bit" :112).
- `hardware/cad/reference_design.md` — ADA4530-1 reference-design notes (§9
  signal-chain topology = bare unity-gain follower into passive node, NO DC bleed
  path — the `CLV-REQ-CPL-D` topology decision).
- `hardware/ORDERING.md`, `docs/procurement_action_items.md` — procurement (also
  carry the "10-bit" mislabel).
- `docs/open_questions.md` (round-1 "Q→0" framing :51), `docs/glossary.md`
  (round-1 discriminator entry :41), `docs/design/2026-05-20_initial_scoping.md`
  ("if 0.0 mV the framework is falsified" :59).
- `docs/analysis/2026-06-03_cleave-two-sided-discriminator.md`,
  `docs/analysis/2026-06-04_cleave-round2-prereg.md`,
  `docs/analysis/2026-06-04_cleave-round2-smcounterfactual-result.md` — the
  round-2 cure (on `main`; the source for the chord-gated framing, incl. F-R2-3).
- `CLAUDE.md` / `AGENTS.md` — repo orientation + operating doctrine (CLAUDE.md
  also carries the stale `constants.py:205` cite to fix).

### Inlined equipment-audit + spec-sheet findings (so no /tmp access is needed)

The numbers below are reproduced from canonical primitives + the
requirements-leaf §1/§8 and corrected against the prior equipment-audit DRAFT.
They are the load-bearing arithmetic the re-spec rides on:

- **The floor (`CLV-REQ-FLOOR`):** `dQ/dx = ξ_topo = e/ℓ_node = 4.1490e-7 C/m =
  414.9 fC/µm = 0.4149 pC/µm` (zero free parameters). At `C_in=10 pF`:
  `dV/dx = ξ_topo/C_in = 41.49 mV/µm`. The CHARGE floor is `C_in`-independent;
  the VOLTAGE floor inherits `C_in`.
- **Position→charge coupling (`CLV-REQ-CPL-A`):** `dV/dx = 41.49 nV/pm` at 10 pF.
  A 1 nm gap excursion forges 41.5 µV — ~40× over the sub-µV floor. **Gap jitter
  is non-averageable** (it rides the signal transfer function). This is why
  vibration isolation + pm-class gap-hold are the hardest mechanical specs, and
  they are physics-set (movable only by raising `C_in` or loop stiffness).
- **Binding noise model (`CLV-REQ-CPL-B`):** the observable is a held-DC step over
  a multi-hour `N≥50` sweep ⇒ the band is sub-Hz (~1e-4 Hz). **White noise is
  irrelevant** (~10 nV over a 1 s hold, ~4e3 below one step). What binds is
  in-band 1/f (~0.61 µV rms) + sub-0.1-Hz drift ⇒ **the binding spec is LEVEL
  STABILITY, not single-shot resolution.** (The prior DRAFT's white-noise-×-√1Hz
  model overstated SNR by 1–2 OOM.)
- **CPD systematic (`CLV-REQ-CPL-C`):** ~21.3% of the floor at the reference gap,
  `∝1/g²`. Across a 1×→4× sweep the CPD contribution swings by
  `0.213×(1−1/16) = 19.97% of floor ≈ 8.3 mV ≈ 83 fC`, dropping to 1.33% at the
  4g₀ end. **The bench's level-stability must beat this ~20%-of-floor swing** to
  assert flat-vs-1/g².
- **Bias-current ramp (`CLV-REQ-CPL-D`):** 20 fA on a passive 10 pF node =
  `20.0 fC/s` continuously ⇒ a bare follower RAILS over the sweep. **Step-
  differencing / DC-restore / reset-integration is mandatory** (a topology BC).
  (Corrected from the prior DRAFT's 48 fC/s.)
- **No fundamental wall:** `kTC` on 10 pF at 300 K = 20.35 µV rms = **0.20 fC** —
  at/below the floor, reset-differenced away. No quantum/thermodynamic wall
  anywhere; every requirement is reachable in principle (corrected from the prior
  DRAFT's 50 fC).
- **ENOB (`CLV-REQ-READOUT` §3.3):** single-shot ENOB on a ±50 mV (100 mV span)
  range = `log2(100mV / (δ×41.49mV))` = **4.6 / 5.6 / 6.9 / 7.9 bits** at
  δ = 10 / 5 / 2 / 1%. (Corrected from the prior DRAFT's 7/8/9 — the DRAFT was
  ~2.3 bits high.) The drift-corrected LEVEL needs ~17.3 effective ENOB
  (18–24-bit ΔΣ OR 6.5–7.5-digit DMM; `√50 = 7.07×` averaging). **An 8-bit scope
  (390 µV/LSB) is the wrong instrument class — ~400× short** — but the swap is
  trivially COTS. (This is why the PicoScope 2204A 8-bit mislabel matters: the
  instrument CLASS is wrong, not just the SKU.)
- **Vibration (`CLV-REQ-VIB`):** gap RMS jitter ≤ **14.6 pm** in 1–50 Hz
  (`0.61 µV / 41.49 nV/pm`). Needs isolation transmissibility `T < 3e-4` (71 dB,
  quiet) to `T < 1.5e-5` (97 dB, noisy) across 1–50 Hz, PLUS turbo-decouple. The
  BINDING environmental systematic; near/at the COTS edge.
- **Thermal (`CLV-REQ-THERMAL`):** `dT ≤ 1 K` over the sweep (Vos drift referred to
  the floor: `dT_sweep < 1.21 K` max-tempco) + 2× calibrated RTDs logged. NOT the
  binding systematic, but the ">5 K" Femto rule is ~4× too loose.
- **`C_in`-fixed tension (`CLV-REQ-CFIX`, H3, UNCLOSED):** the moving plate-pair
  `C_plate = ε₀A/g` tracks ~1/g: at A=1 cm², 8.85 pF @100 µm → 35 pF @25 µm — a
  ~4× swing, FATAL if it IS `C_in`. Requirement: `|dC_in/C_in| ≤ δ/k` (≤3.3% at
  δ=10%), met by a fixed reference cap dominating `C_in` (moving-plate coupling
  `C_plate(g_min) < 0.44 pF`) OR by in-situ-measure-and-divide. **Resolution is
  OPEN knob D5.**
- **Phase-space-coordinate check (per A46):** this measurement is genuinely
  real-space (displacement in m, charge in C, voltage in V on a real cap); the
  corpus claim `[Q]≡[L]` is itself a real-space dimensional identity. Real-space
  coordinates are MATCHING — no phase-space discipline violation.
- **Consistency-vs-emergence tag:** the floor (`Q=ξ_topo·x`, gap-independent
  integer charge) is an **Axiom-2 MANIFESTATION (emergence-class)** prediction —
  zero free parameters. The slope magnitude (0.415 pC/µm) is a **consistency-class
  echo** (`ξ_topo=√α` in native units AND `ℓ_node`=Compton wavelength — doubly
  over-determined). The tight Level-2 specs protect the non-gating slope; they
  must NOT be read as gating the emergence claim.

### Spec-sheet facts on the named-stale hardware

- **PicoScope 2204A:** an **8-bit** USB scope (Pico 2000-series = 8-bit). NOT 10-bit.
  Only the 5000-series flexible-resolution models (e.g. the 5242D alt in the BOM)
  are 12–16 bit. The Femto BOM/TEST_PROCEDURE "10-bit ENOB" label is wrong.
- **PI P-016.20H (current PZT1):** a commodity ~15–30 µm-class open-loop piezo
  actuator (1 µm step framing in the BOM, ~100 V drive, M3 mount). Open-loop, NO
  capacitive position sensor — fails `CLV-REQ-GAP` on travel (≥4× blocker),
  resolution/repeatability (~100×), and gap-placement. The cure is a closed-loop
  cap-sensor LINEAR nanopositioner (≥300 µm @ g₀≈100 µm, or de-spec'd g₀) — a BUY
  (A6), with g₀/stroke OPEN (D6).
- **Thorlabs KMS / POLARIS-K1 (current MNT1):** mirror-TILT kinematic mounts — the
  WRONG degree of freedom. The plates must TRANSLATE along the gap normal staying
  parallel (`CLV-REQ-GAP` §4.4). Re-spec to a linear stage + parallelism fixture.

---

**End of brief.** The separate session's deliverable is a Femto-repo branch off
`main` (reconciled + re-pointed-to-CLV-REQ + chord-gated + stale-items-fixed +
hardware re-spec), pushed and opened as a DRAFT PR for Grant to review and merge.
It makes NO D1–D6 / A1–A6 decision.
