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
   (348.7→491.6 / 353.0→493.2) and core fraction **falls** (0.062→0.052 / 0.061→0.055,
   torus-native minimum-image ball — repair finding #1; the seam-clipped Euclidean ball had
   read 0.045/0.049) — **while φ inflates to ~10.5×**. The energy does **not** self-tighten; the φ growth is the
   accumulated-flux "counts laps" gauge effect (`Phi_link` accumulates monotonically,
   `k4_tlm.py:400`), **not** localization. This is Reading A, not Reading B.
2. **Boundary-insensitive.** The PML twins read the SAME sign (PR rises, CF falls →
   LOOP-FILLING under `pml=3` too). The dispersal appears under **both** boundaries ⇒ it is a
   boundary-clean property of the pattern, not a torus artifact.
   > **🔴 CORROBORATION WITHDRAWN (2026-07-15, falsifying-evidence pointer — Rule 12).** This
   > PML-twin **boundary-insensitivity corroboration is withdrawn**. It holds only on the frozen
   > **potential-only endpoint** meter; on the mandatory full-register instrument the PML twins do
   > **not** corroborate — they read INCONCLUSIVE (this doc's **Finding #3 — ESCALATED §1**, below)
   > / CONCENTRATING† under the sponge-guard read
   > ([`2026-07-14_gpersist-meter-circuit-ontology.md`](2026-07-14_gpersist-meter-circuit-ontology.md)
   > §5/§7) — a register/guard-dependent candidate PML kinetic-drain artifact, **not admissible as
   > boundary corroboration**. **The fork rests entirely on the torus cells** (`pair`+`graded_a0`),
   > which read LOOP-FILLING robustly under every read (`guard_sensitive=False`). **RULED Reading A
   > and G-PERSIST ★RULED are untouched** — they rest on the torus cells and the fork-independent
   > PML **φ-dispersion** trend (a different, still-valid boundary-insensitive signal — the #670
   > T2/Φ_link channel, never summed into this A1 meter), respectively.
3. **The meter is genuine — provably not derivable from E/φ.** On the torus `E_persist ≡ 1.0`
   (a conservation identity, #670 erratum) yet the participation ratio moves ~4× over 8 quiet
   steps (adversarial KNIFE B). The spatial statistic carries WHERE-information the scalar
   cannot encode. Independent naive recompute matches the driver to machine precision
   (|Δ|≤1.1e-13, KNIFE A).
4. **φ-channel plant: UN-FOOLABLE_CONFIRMED (both cells).** A distributed external K4 pump
   sustains φ far above the 0.80 floor (PML pair: free φ=0.084 → plant φ=4.2e6; torus pair:
   free 2.512 → plant 4.1e8) **while the localization meter reads LOOP-FILLING** — the meter
   classifies the sustained φ as externally-fed. The two-meter combination (φ-detector +
   localization meter) is **un-foolable by DISTRIBUTED sustenance** (repair finding #2 — the
   only pump tested is the frozen spatially-distributed one, for which the meter leg is
   near-vacuous; the core-LOCALIZED adversarial pump is the required, untested follow-on); it
   closes the #670 review's missing φ-channel negative control.
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
| N=14 torus pair, **prod** | E=0.999996 / φ=10.519699 | E=0.999996 / φ=10.519699 | **0.00e+00** | φ 10.5197 ✓ |

The frozen parity protocol requires cell S1 (torus pair, smoke) **and one production cell** at
≤1e-6 relative (prereg §Live-fire parity gate). Both legs are now documented at the frozen
tolerance (review finding #6b — the production leg had been documented only as a 4-decimal
banked-value match). Production parity JSON (`--parity 14 0 pair prod`):
`ref_E = mirror_E = 0.9999960995736088`, `ref_phi = mirror_phi = 10.51969852461048`,
`rel_dE = rel_dphi = 0.0`, `parity_pass = true` — byte-identical trajectory, meter non-perturbing.

Every production cell independently reproduces banked #670 to four decimals (§2 table). ⇒ the
per-step localization meter is measured **on the identical field trajectory** as the banked
battery; the instrumentation does not perturb the physics.

---

## 2 · Per-cell concentration table (the deliverable) — energy (A1) meter

Trend = relative change from **drive-off** (t = n_drive) to **final quiet step** (t = n_total).
PR = raw participation ratio (effective participating sites, interior M sites; **no center**).
CF = fraction within r=2.0 of the **density peak** (PML-excluded interior; **torus-native
minimum-image ball** on `pml=0`, plain-Euclidean on the PML box — repair finding #1).
Resolution θ=0.10.

| N | boundary | fid | mode | E_persist | φ_persist | PR (start→end, rel) | CF (start→end, rel) | signature |
|---|---|---|---|---|---|---|---|---|
| 14 | torus | prod | **pair** | 1.0000 | **10.520** | 348.7→491.6 (**+0.410**) | 0.062→0.052 (**−0.158**) | **LOOP-FILLING** |
| 14 | torus | prod | **graded_a0** | 1.0000 | **10.422** | 353.0→493.2 (**+0.397**) | 0.061→0.055 (**−0.101**) | **LOOP-FILLING** |
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
(**2026-07-15:** the "both boundaries" PML-twin leg is a **potential-only-endpoint** read; its
role as *boundary corroboration* is **withdrawn** on the full register — see TL;DR item 2 note +
Finding #3 ESCALATED §1. The **torus** fork verdict is unaffected.)

**Stencil caveat (repair finding #1 — torus-native CF).** The original banked torus CF values
(pair **−0.274**, graded_a0 **−0.203**) were computed with a **non-periodic Euclidean** core-ball
on the `pml=0` **periodic** lattice (`np.roll` wraparound, `k4_tlm.py:393`). The final-step
energy peak on **both** fork cells sits at the array **seam**, `(6,6,6)→(7,1,1)`, so the
Euclidean r=2.0 ball was **clipped**, excluding the wrapped part and inflating the CF-fall
~2× (pair 1.73×, graded_a0 2.00×) — a bias that can **only** lower CF, i.e. only toward the
LOOP-FILLING verdict (structural-null stencil class). The **minimum-image** distance
`min(|d|, N−|d|)` per axis is the substrate-native torus metric; the corrected values are
pair **−0.158**, graded_a0 **−0.101** (banked above). **Fork-cell peak coordinates** (energy,
drive-off→end): pair `(6,6,6)→(7,1,1)`, graded_a0 `(6,6,6)→(7,1,1)` (both seam-adjacent at
end); the PML twins peak interior (`(9,7,9)→(7,7,3)`, no seam) so their Euclidean balls are
unaffected; `photon_lock` peaks at the center `(7,7,7)→(7,7,7)` so clipped ≡ periodic (its
`+0.417` is genuine peak-sharpening, **not** a clip artifact — §4). The **PR** statistic is
center-free/mask-only and stencil-clean, and rises strongly on both fork cells (`+0.410 /
+0.397`), so the LOOP-FILLING bin is carried independently of the CF stencil.

**graded_a0 sits at the θ resolution floor.** Its torus-native CF-fall (**−0.101**) is
essentially **at** the θ=0.10 floor — half of the previously-quoted dispersal magnitude on CF
was seam-clip artifact. LOOP-FILLING for `graded_a0` therefore rests on the **stencil-clean,
center-free PR** (rises `+0.397`), with CF-not-rising corroborating at the floor. (`pair`
retains a resolved CF-fall of −0.158.) **Any future CF-based CONCENTRATING claim on the torus
must use the torus-native (minimum-image) CF ball** — see the meter-reuse note in §4.

---

## 3 · Fork bin — LOOP-FILLING (Reading A) — with the a-priori and the carve

**FORK BIN (torus `pair` + `graded_a0`, production): LOOP-FILLING.** Criterion (frozen): energy
stays distributed (PR does not fall, CF does not rise) while φ inflates — met on **both** fork
cells, on **both** statistics (PR rises AND CF falls), corroborated by the PML twins
(boundary-insensitive) and by the smoke arc. *(**2026-07-15:** the PML-twin boundary-insensitivity
corroboration is **withdrawn** — it holds only on the potential-only endpoint meter; on the full
register the PML twins do not corroborate. See TL;DR item 2 note + Finding #3 ESCALATED §1 +
[`2026-07-14_gpersist-meter-circuit-ontology.md`](2026-07-14_gpersist-meter-circuit-ontology.md)
§5/§7. The torus fork verdict — and the smoke corroboration — stand.)*

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
- **It is an endpoint read of an oscillating series (frozen non-monotone guard, now shipped —
  finding #5).** Over the quiet window the `photon_lock` CF swings **min 0.050 → max 0.303**
  (endpoint read +0.417) with a least-squares **`slope_norm ≈ +0.002`** (essentially flat), and
  the energy peak **wanders across 11 distinct sites**. The +0.417 `rel_trend` is the endpoint of
  a strongly non-monotone series — exactly what the frozen least-squares-slope guard was declared
  to catch (it had been declared-but-unshipped; now `_trend` reports `slope_norm` alongside
  min/max). A CONCENTRATING claim gated on the conjunction + slope would not fire here.
- **What this is NOT:** a threat to the fork verdict. The fork cells (`pair`, `graded_a0`) read
  LOOP-FILLING on **both** statistics (PR rises AND CF falls) — the robust, two-statistic-
  agreeing signature. Only a CONCENTRATING verdict resting on CF-alone would be suspect, and
  the fork went the other way on both statistics.
- **Discipline:** per honest-closure + flag-don't-fix, the frozen disjunctive criterion is
  **NOT** retuned post-hoc. The caveat is recorded: a future CONCENTRATING claim should require
  the **conjunction** (PR falls AND CF rises), and the participation ratio is the more robust
  single statistic. Surfaced for the auditor's meter-hardening queue.
- **Meter-reuse note (repair finding #1):** any future **CF-based CONCENTRATING** claim on the
  **torus** (`pml=0`) **must** use the torus-native **minimum-image** CF ball (now shipped). A
  non-periodic Euclidean ball clips seam-adjacent peaks and biases CF **low**, which on a
  concentration claim would **conservatively mask** a real tightening — the same structural-null
  stencil failure, in the opposite direction. The `photon_lock` false positive here is **not**
  the clip artifact (peak at center, clipped ≡ periodic); it is genuine peak-sharpening the CF
  leaf cannot distinguish alone.
- **Two-statistic-conjunction rule (adopted; review finding #4):** the operative CONCENTRATING
  rule for meter reuse is the **conjunction PR falls AND CF rises** (torus-native CF), **not**
  the frozen CF-OR-PR disjunction and **not** any φ-conjunct. φ is deliberately **excluded** from
  the verdict logic — the ~10.5× inflation is the lap-counting gauge artifact
  (`Phi_link` monotone accumulation, `k4_tlm.py:400`) and is quarantined (finding #4); it is
  carried as human-verified corroboration only. The endpoint-only `rel_trend` is additionally
  guarded by the least-squares slope (finding #5) against non-monotone series.

---

## 5 · φ-channel plant — UN-FOOLABLE_CONFIRMED (**distributed** sustenance; the #670 second follow-on)

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
is met on both cells. The two-meter combination is **un-foolable by DISTRIBUTED sustenance**.
(The plant φ magnitude is a pump artifact — the point is *sustained ≥ floor* while the meter
flags externally-fed, not the absolute value. Budget = smoke, matching the #670 sabotage-plant
control class.)

**Scope of the un-foolable claim (repair finding #2 — MAJOR, identity-audit hit).** The only
pump exercised is the frozen **spatially-DISTRIBUTED** external K4 pump (prereg §The φ-channel
plant: `k4.V_inc[interior,:] += √ALPHA` on all four ports at **all** interior sites). For that
geometry the **meter leg (b)** of the gate is **near-vacuous**: a uniform additive injection
maximally **delocalizes** the field, forcing PR up and CF down, so `loop_filling=True` is close
to true-by-construction — the tested geometry is the one **least** able to trip the CONCENTRATING
(fooling) leg. The free (unpumped) PML run **already** reads LOOP-FILLING (PR +0.084, CF −0.364)
and the pump pushes the same direction, so `UN-FOOLABLE_CONFIRMED` was close to pre-ordained once
φ sustained. What the run **genuinely** establishes (and banks): a distributed external pump that
fools the **scalar** φ floor by 7–8 orders is correctly classified **externally-fed** — closing
the #670 missing-φ-channel control. What it does **NOT** establish is the general "cannot be
fooled by sustenance" safety property.

- **Untested adversary (the natural remaining fooling route):** a **core-LOCALIZED** external
  pump that sustains φ above the 0.80 floor **while sharpening the density peak** — driving the
  meter toward CONCENTRATING, i.e. the FOOLABLE branch `(a) ∧ ¬(b)` the frozen prereg names as a
  live outcome class (prereg §The φ-channel plant). This route was **not** run. The branch's own
  torus `photon_lock` control (§4) already shows the meter's **CF-alone** leaf false-positives to
  CONCENTRATING under **mere peak-sharpening** (CF 0.097→0.138) — so a peak-sharpening localized
  pump is a plausible, non-exotic fooler, not a strawman.
- **REQUIRED FOLLOW-ON (do NOT cite the combo as a general sustenance-proof detector until run):**
  a **core-localized adversarial-pump plant** — sustain φ ≥ 0.80 with a pump footprint
  concentrated at the seed core, and test whether the recommended **two-statistic conjunction**
  hardening (PR falls AND CF rises, torus-native CF) also defeats it. See §7 follow-ons.

---

## 6 · Adversarial self-review (3 lenses; live-fire this turn)

The full 10-agent `ave-adversarial-pr-review` scriptPath workflow is the orchestrator's to
fire at the PR gate (as for #670 — no workflow-runner tool in the implementer toolset). The
live-fire equivalent was executed this turn as the three standard lenses:

| lens | check | result |
|---|---|---|
| **Live-fire / re-derivation** | mirror-loop E/φ vs `run_loop_gap_probe`; independent naive recompute of PR/CF | parity 0.00e+00; PR/CF match to |Δ|≤1.1e-13 (KNIFE A) |
| **Meter-genuineness knife** | is the concentration meter derivable from φ/E alone? | **NO** — on the torus E≡1.0 (identity) yet PR moves ~4× over 8 quiet steps (KNIFE B); the scalar cannot encode the spatial move |
| **Discipline / prereg-parity** | every frozen declaration vs shipped code | **corrected** (the original "clean" was overstated — review findings #4/#5) — matches on energy=k4+cos, φ=ΣΦ_link², PML-excluded mask, raw PR, density-peak core r∈{1.5,2,2.5}, 0.5/1.5 schedule, memristive, √ALPHA distributed quiet-only pump. **Disclosed deviations** (EVIDENCE-VOID, verdict-robust, reconciled by dated prereg amendments): (i) the LOOP-FILLING classifier omits the frozen **φ≫1 conjunct** — *intentional gauge quarantine*, φ carried as human-verified corroboration (finding #4); (ii) the aggregate gate implemented only **1 of 3** frozen MIXED triggers — now **all 3** machine-evaluated, all moot on this data (finding #5); (iii) the frozen **least-squares slope** non-monotone guard was declared but unshipped — now shipped (finding #5). |

**Self-surfaced finding (not a defect, a caveat):** the CF-alone leaf false-positives on the
torus `photon_lock` control (§4) — recorded, criterion not retuned. No other findings; the
banked verdict (LOOP-FILLING) rests on the two-statistic-agreeing fork cells + byte-exact #670
reproduction.

---

## 7 · What this decides / does not decide

- **DECIDES (data, not ruling):** the enclosure fork — Reading A (wake-feeding) vs Reading B
  (self-tightening). Data ⇒ **LOOP-FILLING = Reading A**, ~~boundary-insensitive~~, robust.
  (**2026-07-15:** "boundary-insensitive" here was the PML-twin corroboration, now **withdrawn** on
  the full register — the verdict rests on the **torus** cells, robust under every read. See TL;DR
  item 2 note + Finding #3 ESCALATED §1.)
- **DOES NOT DECIDE:** the G-PERSIST ★RULED verdict (rests on the fork-independent PML
  φ-dispersion trend — untouched). Node-mint (fork B) stays firewalled; this reads (A)
  fixed-\(N\) only.
- **GRANT RULES THE FORK.** The docket's Reading A is *leaned*; this data supports closing it.
  The framing call is surfaced, not fiated.

**Required follow-ons (before the named claims are cited beyond this driver):**

1. **Core-localized adversarial-pump plant** (repair finding #2) — the un-foolable claim is
   scoped to **distributed** sustenance; the general anti-fooling guarantee is **untested**
   against a **peak-sharpening core-localized** pump (the FOOLABLE branch the frozen prereg
   names). Run a plant whose pump footprint is concentrated at the seed core, sustaining
   φ ≥ 0.80, and check whether the **two-statistic conjunction** (PR falls AND CF rises, on the
   torus-native CF) also defeats it. Until run, do **not** cite the two-meter combo as a general
   sustenance-proof detector. *(Registered, not run in this repair.)*
2. **Torus-native CF for any forward CONCENTRATING adjudication** (repair finding #1) — shipped;
   required before the CF leaf is used to claim concentration on the torus.

---

## Review findings + repairs (2026-07-14)

Independent adversarial review (`ave-adversarial-pr-review`, 3 lenses × 18 agents) confirmed
**15 of 15** findings, **0 refuted** — all **EVIDENCE-VOID** (broken/absent demonstration
machinery around a conclusion that is independently true). The **LOOP-FILLING ⇒ Reading A**
fork verdict **survives every finding** (carried by the stencil-clean, center-free PR statistic
and the byte-exact #670 φ-trend); the repairs **harden the meter and honesty-scope the claims**,
they do **not** soften the data.

**Finding→commit map** (branch `analysis/gpersist-localization-observable`): #1 → `44afb78b`
(torus-native CF stencil) · #2 → `31b85424` (scope to DISTRIBUTED sustenance) · **#3 →
`9c588bbe` ESCALATED** (kinetic register moves bins — STOP+report, not banked) · #4 → `bbd57a69`
(φ-conjunct quarantine) · #5 → `abaad0a6` (3 MIXED routes + slope guard) · #6a/#6b → `f558d258`
(quote-attribution + production parity). Finding→fix map:

| # | severity | finding | repair |
|---|---|---|---|
| 1 | MAJOR | CF core-ball used non-periodic Euclidean distance on the `pml=0` periodic torus; seam-adjacent peak clipped the ball, inflating the banked torus CF-fall ~2× toward LOOP-FILLING | driver `_meter_snapshot` now uses **minimum-image** distance on `pml=0` (Euclidean on the PML box); §2 table re-banked (pair −0.274→**−0.158**, graded_a0 −0.203→**−0.101**), stencil caveat + fork-cell peak coords added (§2), meter-reuse note added (§4). Verdict-robust: PR (center-free) rises `+0.410/+0.397`; both cells stay LOOP-FILLING. `graded_a0` CF now sits at the θ floor — LOOP-FILLING rests on PR. |
| 2 | MAJOR ×2 | "un-foolable by sustenance" overgeneralizes: only the frozen **distributed** pump was tested, for which the meter leg (b) is near-vacuous (identity-audit hit) | headline (TL;DR item 4 + §5 + §5 header) retitled "un-foolable by **DISTRIBUTED** sustenance"; untested **core-localized** adversary stated (§5), `photon_lock` peak-sharpening false-positive cited as the plausible fooling route; **required follow-on** (core-localized adversarial-pump plant + two-statistic conjunction test) registered in §7 — **not run** in this repair. Fork verdict + G-PERSIST ★RULED untouched. |
| 3 | MAJOR | energy-meter density is **potential-only** — omits the Cosserat KINETIC register (~44% of H on the fork cells); the frozen prereg (line 85) sells `E_dens` as the "spatial parallel of `E_persist`", but `E_persist` is a kinetic-inclusive H-ratio | **ESCALATED — STOP+report, NOT re-banked** (see the ESCALATED subsection below). Implemented the composed (min-image + kinetic) meter and re-ran the full production battery: **fork cells stay LOOP-FILLING** (disperse *harder* on CF, −0.420/−0.409) so the verdict is robust — **but four non-fork cells' bins MOVE** (torus `photon_lock` CONCENTRATING*→LOOP-FILLING; all three PML cells LOOP-FILLING→INCONCLUSIVE). Per the cluster-3 STOP rule, the kinetic term is **not committed to the driver** and the composed numbers are **not banked** into §2; surfaced for orchestrator/Grant adjudication (register choice = framing-level). |
| 4 | MINOR ×3 | shipped LOOP-FILLING classifier drops the frozen **φ≫1 conjunct** (quarantine-stronger); RESULT §6 self-review overclaimed prereg-parity "clean" | φ **not** re-added to the classifier (would re-import the quarantined gauge artifact); dated **prereg amendment (finding #4)** reconciles the frozen bin as *superseded-by-quarantine* (2-conjunct PR∧CF + φ≫1 human-verified corroboration, byte-exact vs #670: φ=10.5197/10.4218); RESULT §6 "clean" cell corrected to disclose the intentional omission; §4 adopts the **two-statistic-conjunction** rule for future CONCENTRATING claims. Verdict-robust (fork cells meet the full conjunction where scored). |
| 5 | MINOR ×3 | aggregate gate implemented only **1 of 3** frozen MIXED triggers; the frozen least-squares-slope non-monotone guard was never built; prereg 174-176 vs 180-183 internally contradictory | driver: `cmd_aggregate` now machine-evaluates **all 3** MIXED routes (pair-vs-graded, energy-vs-Φ_link, torus-concentrates-vs-PML-twin) and `_trend` now returns `slope_norm`; all three MIXED routes **moot on this data** (Φ_link agrees LOOP-FILLING PR +0.996/+0.963, no torus concentration) so **FORK BIN = LOOP-FILLING unchanged**; dated **prereg amendment (finding #5)** reconciles the 174-176-vs-180-183 contradiction; RESULT §4 surfaces the min/max non-monotone read; §6 row corrected. |
| 6a | MINOR | frozen prereg STEP-0 splices "+ the participation ratio" into a quote cited as `spec verbatim` from parent RESULT §8, where it does not occur | verified two-method (`grep -c` = 0, `git grep` = 0 hits on the parent file); dated **prereg amendment (finding #6a)** re-attributes the participation-ratio spec to `_orchestration/2026-07-10_rulings-docket.md:435` (also :477/:502). Meter stays fully authorized; citation-only. |
| 6b | MINOR | frozen parity protocol promised smoke S1 **and** one production cell at ≤1e-6; RESULT documented only the smoke leg at tolerance | RESULT §1 now includes the **production** parity row + JSON (`--parity 14 0 pair prod`: ref==mirror E=0.9999961, φ=10.5196985, relΔE=relΔφ=**0.0**, PASS) — both frozen legs documented at ≤1e-6. |

### Finding #3 — ESCALATED (kinetic register moves corroboration/control bins; STOP + report)

Review finding #3 (MAJOR): the meter density `e_dens = k4.get_energy_density() +
cos.energy_density()` is **potential-only** — `cos.energy_density()` is the Cosserat strain +
curvature density (`cosserat_field_3d.py:1427`), while the engine Hamiltonian
(`k4_cosserat_coupling.py:946`) also carries `cosserat_kinetic_energy()` →
`cos.kinetic_energy()` = ½ρ|u̇|² + ½I_ω|ω̇|² (`cosserat_field_3d.py:1789`), **~44 % of H** on the
fork cells. The frozen prereg (line 85) calls `E_dens` "the spatial parallel of the frozen
`E_persist` channel" — but `E_persist` is a **kinetic-inclusive** H-ratio, so the shipped meter
is measuring a different register than the scalar it claims to parallel.

**What was done (Rule-10 empirical check):** the per-site kinetic density (½ρ Σ_c u̇² + ½I_ω Σ_c ω̇²,
`mask_alive` applied — verified to sum to `cos.kinetic_energy()` at rel-diff 0.00e+00) was added
to `e_dens`, composed with the finding-#1 minimum-image ball, and the **full production battery
was re-run**. Composed vs shipped (potential-only + min-image) signatures:

| cell | shipped (potential-only) | composed (+ kinetic) | bin move |
|---|---|---|---|
| torus pair prod | PR +0.410 / CF −0.158 → **LOOP-FILLING** | PR +0.376 / CF −0.420 → **LOOP-FILLING** | none (verdict cell) |
| torus graded_a0 prod | PR +0.397 / CF −0.101 → **LOOP-FILLING** | PR +0.354 / CF −0.409 → **LOOP-FILLING** | none (verdict cell) |
| torus photon_lock prod | PR −0.072 / CF +0.417 → CONCENTRATING\* | PR +1.426 / CF −0.471 → LOOP-FILLING | **CONCENTRATING\*→LOOP-FILLING** |
| PML pair prod | PR +0.084 / CF −0.364 → LOOP-FILLING | PR −0.010 / CF +0.061 → INCONCLUSIVE | **LOOP-FILLING→INCONCLUSIVE** |
| PML graded_a0 prod | PR +0.102 / CF −0.316 → LOOP-FILLING | PR +0.006 / CF −0.083 → INCONCLUSIVE | **LOOP-FILLING→INCONCLUSIVE** |
| PML photon_lock prod | PR +0.219 / CF −0.269 → LOOP-FILLING | PR −0.002 / CF +0.025 → INCONCLUSIVE | **LOOP-FILLING→INCONCLUSIVE** |
| torus pair/graded_a0 smoke | LOOP-FILLING | LOOP-FILLING (PR +11.8/+11.5, CF −0.867/−0.864) | none |

Aggregate **FORK BIN = LOOP-FILLING** (torus `pair`+`graded_a0` prod) is **unchanged**; both
φ-plants remain **UN-FOOLABLE_CONFIRMED**.

**Why this is ESCALATED, not banked.** The cluster-3 repair carried an explicit stop rule: *if
the composed re-run moves any cell's bin, STOP and report to the orchestrator instead of
re-banking.* It moved **four** non-fork bins. The **headline fork verdict (LOOP-FILLING ⇒
Reading A) is robust** under both registers (and the composed CF-fall is *sharper*, matching the
review's kinetic-only smoke counterfactual), and **G-PERSIST ★RULED is untouched**. But two
supporting structures are **register-dependent**, which is a framing-level call:

1. **Boundary-insensitivity corroboration (TL;DR item 2, §3) weakens under the full register.**
   Under the composed meter the PML twins read **INCONCLUSIVE** (endpoint trends collapse below
   θ=0.10; e.g. PML pair PR swings min 71.7→max 99.1 but returns near-flat, a strongly
   non-monotone series the endpoint `rel_trend` hides — cf. the finding-#5 slope guard). So
   "the PML twins read the SAME sign" holds on the potential-only meter but **not** on the
   full-register meter — a candidate boundary-artifact in the Cosserat **kinetic** register the
   PML absorbs. This does not touch the *torus* fork verdict, but it does change the corroboration
   story.
2. **The §4 `photon_lock` CF-alone false positive is a potential-only artifact.** Under the full
   register `photon_lock` reads **LOOP-FILLING** (the photon mode's energy is dominantly kinetic;
   once included, the field is correctly seen as delocalized). The disclosed CF-alone
   false-positive **vanishes** — i.e. the §4 caveat is specific to the incomplete register.

**Disposition (flag-don't-fix).** The kinetic term is **not committed** to the driver and the
composed numbers are **not banked** into §2 (the banked meter remains the shipped potential-only +
min-image meter). The register choice (potential-only-as-shipped vs full-kinetic-inclusive) and
the boundary-insensitivity restatement are surfaced for **orchestrator / Grant** adjudication. The
exact code change is a one-block addition to `_meter_snapshot` (per-site kinetic density added to
`e_dens`); the composed battery log is preserved in the run scratch. **Fork verdict and
G-PERSIST ★RULED stand regardless of the register call.**

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
