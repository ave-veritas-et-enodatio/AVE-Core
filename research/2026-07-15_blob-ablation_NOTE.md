# BLOB-ABLATION — core-holding mechanism fork (kernel-OFF + amplitude sweep) — NOTE

**Date:** 2026-07-15 · **Branch:** `analysis/blob-ablation-kernel-off` ·
**Base:** origin/main `6f2030728` (the #698 corrected meter present:
`rel_qmean` + `_core_holding` verified at base — reached main via the #698
review-repair commits `8167a89c/16231ad7/850956b1/e45949fe` → merge `626a2bd5`
→ correction PR **#701** `fix/698-repair-commits-correction`; NB the launch
brief named "correction PR #703" — the actual landing PR is **#701**, cosmetic
number difference, **no merge gap**). ·
**Instrument reused (Rule-14 anti-rebuild):**
[`src/scripts/vol_1_foundations/gpersist_localization_observable.py`](../src/scripts/vol_1_foundations/gpersist_localization_observable.py)
(the corrected #698 meter — `_meter_snapshot` / `_core_holding` / `_classify_cell` /
`_trend` imported verbatim; NO re-implemented meter). ·
**Driver:**
[`src/scripts/vol_1_foundations/blob_ablation_kernel_off.py`](../src/scripts/vol_1_foundations/blob_ablation_kernel_off.py) ·
**Test:** `src/tests/test_blob_ablation_kernel_off.py`

**This NOTE is the FREEZE payload.** It carries the hypothesis, the frozen
verdict classes + decision rule, the battery grid, and the frozen consequence
routing. It is **committed and pushed BEFORE any battery result is computed**
(light freeze-by-push — the knee-check-plus precedent). Battery results land in
**later commits only**. Freeze commit/timestamp are recorded in the RESULT
addendum appended to this file after the run.

---

## Sector header (mandatory, substrate-first)

- **MODE:** driven ring-up → quiescence on the coupled K4⊗Cosserat lattice
  (`VacuumEngine3D`, rank-4 loop-gap probe), the #670/#698 schedule.
- **SECTOR under test:** the **A1 / energy** blob (two-register LC store =
  potential [K4 V-sector `Σ(V_inc²+V_ref²)` + Cosserat elastic] + kinetic
  [Cosserat inductor currents ½ρ|u̇|²+½I_ω|ω̇|²]). The **T2/Φ_link winding**
  channel is **NEVER summed** into this meter (A1 ⊥ T2) — it is the G-PERSIST
  channel and is untouched here (firewall below).
- **DOF the engine carries:** yes — the core-holding datum is read on the live
  A1 energy density the engine already integrates; the meter is the corrected
  #698 instrument on the identical trajectory (byte-parity asserted at run).
- **REGIME / PHASE-STATE:** **sub-yield throughout** (cold→moderately-saturated
  V-sector; A²_local < 1 everywhere). Any run whose `max_A²_local ≥ 1.0`
  crosses yield — it is **aborted and recorded INSTRUMENT-for-that-run** (a
  post-yield engine state is out of regime for this fork; see the sub-yield
  guard below). Baseline seed front `A = √α` (voltage/GW-strain yield register,
  `loop_gap_seeds.py:44`), i.e. seed-front `A² = α` — the whole excitation sits
  well below the `A²=1` rupture.

## Substrate-native-check (walked BEFORE scaffolding, per operating principle 1)

- **K4 (CP1):** the "3" V-sector U(1) fibre `(V_inc, Φ_link)`. The saturation
  kernel modulates the **bond impedance** `z_local = Z₀/√S`, `S = √(1−A²)`
  (Op14) — a TLM scatter/connect quantity, **not** a continuum-Helmholtz index.
  ✓ native.
- **Cosserat (CP-Cosserat):** the "2" ω-shear; the moving Γ=−1 ω-node-clamp
  wall keyed on the **same shared saturation front**. ✓ native (reactance-pair
  rotation, not gradient-descent).
- **Op14 (CP-Op14):** `S = √(1−A²)` IS the Axiom-4 saturation operator — the
  object this ablation toggles. ✓.
- **Phase-space vs real-space (A46):** the corpus datum (core-ball absolute
  energy 0.611→0.920) is intrinsically a **real-space energy-localization**
  claim ("where does the surviving structure sit"), and the meter measures
  **real-space A1 energy density** over a fixed geom-center ball — **matched
  coordinates**. The *mechanism* under test (the saturation index well) is an
  impedance-plane (phase-space) modulation of `z_local`; the discriminator
  toggles that phase-space kernel and reads its **real-space energy
  consequence**, which is the coordinate the "core-holding" claim lives in. No
  φ²-in-phase-space-vs-Cartesian mismatch here (A46 satisfied).

## Consistency-vs-emergence classification (operating principle 4)

This is a **mechanism-discrimination / consistency-internal** test. It compares
engine states to **each other** (kernel-ON vs kernel-OFF, amplitude-scaled), NOT
to CODATA or a manuscript-quoted target. The only canonical import is the seed
amplitude `√α` (`ave.core.constants.ALPHA`, via `loop_gap_seeds.A_YIELD`) — a
regime landmark, not a fitted target. **No emergence-class claim is made or
headlined.** Class tag: **manifestation/consistency** (does the engine's
saturation kernel produce the observed real-space energy signature).

---

## The datum under test (#698, the corrected `_core_holding`, MAJOR-2 block)

Source:
[`research/2026-07-14_gpersist-meter-circuit-ontology.md`](2026-07-14_gpersist-meter-circuit-ontology.md)
§5 (verbatim table), reproduced by the corrected `_core_holding` at production
`N=14, pml=3, pair, n_drive=18, n_quiet=52`, fixed geom-center ball `r≤2` = 33
sites, **phase-averaged quiet-window** (the corrected instrument's PRIMARY read):

| | PML `pair` | PML `graded_a0` | torus `pair` | torus `graded_a0` |
|---|---|---|---|---|
| core-ball E (drive-off → quiet-avg) | **0.611 → 0.920 (+50.6 %)** | 0.673 → 0.963 (+43.1 %) | 0.351 → 0.265 (−24.4 %) | 0.392 → 0.284 (−27.6 %) |
| rest-of-interior E | 4.355 → 3.594 (**−17.5 %**) | 4.517 → 3.744 (−17.1 %) | +1.6 % | +1.9 % |
| near-sponge kinetic shells | −26.6 % | −26.8 % | 0 | 0 |
| H | **−12.2 %** | −12.2 % | −0.0 % (conserved) | −0.0 % |

Named in #698 SURFACED-NOT-INTERPRETED: "the sponge removes the recirculating
wake, and the surviving central structure holds/gains absolute energy while the
interior drains and H falls."

## The fork (Grant-walked, fired in-chat 2026-07-15)

Is the PML-box core-holding (**+50.6 % pair**, phase-averaged, interior drains,
H falls) produced by:

- **(A) LINEAR MODE-SORTING** — the sponge sieves out the radiative
  (propagating) components; what remains is the bound, core-concentrated
  fraction. **No nonlinear kernel required** — pure linear dispersion + an
  absorbing boundary reproduce it. If (A), the hold survives with the saturation
  index disabled (S≡1), and the surviving fraction is ~amplitude-independent
  (the sieve keeps the same modal fraction regardless of drive strength).
- **(B) NONLINEAR SELF-TRAPPING** — the live saturation kernel makes the core a
  slow-wave region (a self-dug impedance/index well: high A → low S → high Z →
  slow wave) that **gathers the interior's residual energy once the wake stops
  stirring**. If (B), disabling the kernel kills the hold (core flat-or-decaying),
  and the hold-fraction grows **disproportionately** with seed amplitude, with a
  low-amplitude threshold below which the box disperses.

---

## Kernel-OFF — what "the kernel" is, and how it is disabled (DISCLOSURE)

The rank-4 production engine (`make_engine(4, …)`,
`loop_gap_harness.py:107-119`) runs **four** live saturation/coupling kernels:
`use_memristive_saturation=True`, `use_asymmetric_saturation=True`,
`use_impedance_boundary=True`, `use_trilinear_converter=True`. The
amplitude-dependent **index** — the object hypothesis (B) invokes — is the
saturation front `S = √(1−A²)` feeding **(i)** the V-sector bond short
`z_local = Z₀/√S` (`k4_cosserat_coupling.py:_update_z_local_total` +
`k4_tlm.py:_update_z_local_field`) and **(ii)** the Cosserat ω-clamp wall
`Ω₀ ∝ √relu(−Γ_shared)` (`_freeze_clamp_omega0_shared`), both derived from the
one shared front `_update_saturation_kernels(u,ω,V_sq)`.

**The engine's native toggle is NOT S≡1.** `use_memristive_saturation=False`
removes only the **memristive lag** (the backward-Euler `dS/dt=(S_eq−S)/τ_relax`
on the K4 V-sector, `k4_tlm.py:278-289`); it leaves the **instantaneous**
`S=√(1−A²)` index live — still a nonlinear (Kerr-like, memoryless) well. So per
the operating brief ("find the native toggle — a linearized S≡1 path; if none
exists, implement the minimal disabled-flag cleanly and DISCLOSE it") this NOTE
freezes **TWO kernel-OFF conditions (KEEP-BOTH)**:

- **OFF-mem (native toggle, no custom code):** `use_memristive_saturation=False`.
  Isolates the **stateful memory lag** — the literal "LIVE kernel" whose defining
  property is that the well *persists once the wake stops stirring*. τ_relax = 1
  step (native units), so a priori the lag may be short relative to the 52-step
  quiet window; the empirical read decides.
- **OFF-lin (disclosed minimal disabled-flag — S≡1):** pin the saturation index
  to the unsaturated limit. Concretely, the driver overrides three bound methods
  on the built engine instance (visible, local, no engine-source edit):
  1. `coupled._update_z_local_total` → pins `k4.z_local_field ≡ 1` (=Z₀, matched
     → bond Γ=0 → **linear TLM propagation**);
  2. `coupled.k4._update_z_local_field` → same pin (defeats the in-`k4.step`
     V_inc-keyed memristive/instantaneous recompute);
  3. `coupled._freeze_clamp_omega0_shared` → returns 0 (shared front Γ≡0 →
     Ω₀≡0 → the moving Γ=−1 ω-wall is inert).
  Everything else — the trilinear converter, the linear-elastic Cosserat bulk,
  geometry, seed, sponge, drive/quiet schedule — is **byte-identical to
  baseline**. This is a **single-variable** ablation: only the amplitude-dependent
  saturation index is removed. This is the clean (A)-vs-(B) discriminator.

**OFF-lin validation (mandatory, per brief):** an **energy-conservation sanity
on a torus twin**. With S≡1 (matched z_local, no wall) on the torus (pml=0, no
absorber), the engine is a **lossless reactive** system (linear TLM + linear-
elastic Cosserat + conservative converter) and must conserve H. Frozen gate:
`|H_rel|_torus,OFF-lin ≤ 2 %` over the quiet window. **A conservation failure
here means the S≡1 override is buggy → INSTRUMENT (stop, report)**, not a physics
result. (This is the EE lossless-reactive check: Re(Z)→0 ⇒ H conserved.)

## Amplitude sweep — the (B) signature (kernel-ON)

The whole excitation is scaled **self-similarly** by `amp_scale ∈ {0.5, 1.0,
1.5}`: the pair Cosserat seed `amp = amp_scale·√α` AND the bulk probe IC
`amp = amp_scale·0.08` (both scaled so the sweep isolates amplitude, not shape).
Per run the driver records `max_A²_local` (`coupled.max_A_squared()`) and reports
it against the marks **√α ≈ 0.0854 / √(2α) ≈ 0.1208 / 1** (the yield landmarks);
**sub-yield guard: abort + INSTRUMENT-for-that-run if `max_A²_local ≥ 1.0`.**

- **(B) SUPERLINEAR** signature: core-hold-rel monotone-increasing AND **convex**
  in amplitude — `rel(1.5×)−rel(1.0×) > rel(1.0×)−rel(0.5×)` — and/or a
  **low-amplitude dispersal threshold** (`rel(0.5×) ≤ 0` while `rel(1.0×) > 0`).
- **(A) FRACTION-PRESERVING/LINEAR** signature: core-hold-rel ~constant across
  amplitudes (all three within ±10 pp) — the sieve keeps the same modal fraction
  regardless of drive.

---

## THE BATTERY (frozen grid; production `N=14, pml=3, pair` unless noted)

| # | cell | kernel | amp_scale | boundary | purpose |
|---|---|---|---|---|---|
| 1 | baseline | ON (rank-4) | 1.0 | PML(3) | **reproduce the datum** (0.611→0.920, +50.6 %; interior −17.5 %; H −12.2 %). If it does not reproduce → **INSTRUMENT (stop)**. |
| 2 | kernel-OFF (native) | **OFF-mem** | 1.0 | PML(3) | discriminator — does the hold survive without the **memory lag**? |
| 3 | kernel-OFF (S≡1) | **OFF-lin** | 1.0 | PML(3) | **primary discriminator** — does the hold survive with the **whole saturation index** disabled? |
| 4 | sweep-lo | ON | 0.5 | PML(3) | amplitude sweep low |
| 5 | sweep-mid | ON | 1.0 | PML(3) | = run 1 (sweep mid) |
| 6 | sweep-hi | ON | 1.5 | PML(3) | amplitude sweep high |
| 7 | torus datum | ON | 1.0 | torus(0) | reproduce torus twin (core −24.4 %, H conserved) — wake-stirring reference |
| 8 | torus twin lo | ON | 0.5 | torus(0) | sweep-endpoint torus twin (wake-stirring contrast) |
| 9 | torus twin hi | ON | 1.5 | torus(0) | sweep-endpoint torus twin (wake-stirring contrast) |
| 10 | **conservation sanity** | **OFF-lin** | 1.0 | torus(0) | validate the S≡1 override: `|H_rel| ≤ 2 %`. Failure → INSTRUMENT. |
| 11 | OFF-mem torus | OFF-mem | 1.0 | torus(0) | cross-check (memory-off wake-stirring) |

Deterministic carrier (no RNG seed; the loop-gap probe is deterministic). Both
meter registers reported per cell (`energy_full` completed / `energy_pot`
banked). Compute cap: **≤3 concurrent runs**.

---

## FROZEN verdict classes + decision rule

Let `ON` = baseline core-hold-rel (`E_core_full_rel`, phase-avg, PML pair, amp
1.0×); `OFF_lin`, `OFF_mem` the same on runs 3 / 2. All gates on the corrected
instrument's PRIMARY read (quiet-window mean, both registers reported).

**Reproduction gate (run 1):** `ON ∈ [+40 %, +60 %]` AND `interior_rel ∈
[−22 %, −13 %]` AND `H_rel ∈ [−16 %, −8 %]`. Fail → **INSTRUMENT (stop)**.
**Conservation gate (run 10):** `|H_rel|_torus,OFF-lin ≤ 2 %`. Fail →
**INSTRUMENT (stop)**.

- **SELF-TRAPPING** — `OFF_lin ≤ +10 %` (rise killed: core flat-or-decaying)
  **AND** the amplitude sweep shows the (B) SUPERLINEAR signature (convex-in-amp
  and/or a low-amp dispersal threshold). [The clean (B): the index well is
  load-bearing.]
- **MODE-SORTING** — `OFF_lin ≥ +40 %` (rise preserved at ≈ the datum plateau)
  **AND** the sweep shows the (A) FRACTION-PRESERVING signature (~constant
  core-hold-rel across amplitudes). [The clean (A): the sponge sieve does it.]
- **MIXED** — `OFF_lin ∈ (+10 %, +40 %)` (partial kill) **OR** `OFF_lin` and the
  sweep signature disagree **OR** `OFF_lin` and `OFF_mem` fall in different
  classes. **Quantify the split** = `OFF_lin_plateau ÷ ON_plateau` (ratio of the
  phase-avg quiet core-hold rel's; also report the absolute-energy ratio
  `E_core_quietavg(OFF_lin) ÷ E_core_quietavg(ON)`). Report both OFF conditions.
- **INSTRUMENT** — reproduction-gate or conservation-gate failure, or a
  sub-yield-guard abort on a load-bearing run. **Stop, report.**

**Honest-closure commitment (Rule 11):** the decision rule above is frozen. It
is **not** re-tuned to the outcome; a partial kill is reported as MIXED with the
split quantified, not massaged toward either clean class. Interpretation beyond
the four classes is routed to Grant.

---

## FROZEN consequence routing (verbatim, statuses exact)

**If SELF-TRAPPING** —
- **(a)** the PUDDLE class is **`engine-confirmed`** (dynamical binding: coherent,
  bound, non-winding, kernel-dependent, metastable) as distinct from topological
  solitons; the wake-kills-puddles selection observation recorded as
  **WALK-LEVEL** (Grant-walked; not a ruling).
- **(b)** the BREATHER-CONNECTION flagged as **HYPOTHESIS for Grant** (a
  self-trapped non-winding kernel-dependent lump = the mobile-discrete-breather
  class at rest — candidate upgrade for the FPB carrier fork; **routed, NOT
  self-ratified**).
- **(c)** ★census Stage-2 **DESIGN REQUIREMENT** (record as **REQUIRED**): the
  Stage-2 prereg must carry a kernel-OFF twin as built-in control + a
  puddle-vs-knot discriminant column (winding detector ⊥ energy-settling
  criteria).

**If MODE-SORTING** — the requirement **demotes to RECOMMENDED-cheap-control**;
the puddle/breather items record as **not-supported-at-this-config**.

**Either way:** interpretation beyond the classes is routed to Grant.

**If MIXED / INSTRUMENT** — the SELF-TRAPPING consequence block is **NOT**
triggered as `engine-confirmed`; the split (MIXED) or the failure mode
(INSTRUMENT) is surfaced verbatim and routed to Grant; the census Stage-2
kernel-OFF-twin control is recorded as **REQUIRED** on a MIXED partial-kill
(any load-bearing kernel dependence warrants the built-in control) and
**RECOMMENDED** on a clean MODE-SORTING.

---

## Firewall — what this NOTE does NOT touch (explicit)

- **G-PERSIST ★RULED is UNTOUCHED.** The ★RULED flip rests on the fork-independent
  PML **φ-dispersion trend** — the **T2/Φ_link winding channel**, a different
  meter on a different sector, **never summed** with this A1 energy meter
  (A1 ⊥ T2). A core-holding signal in the A1 energy meter cannot structurally
  reach the ★RULED basis. This fork does not re-open it.
- **The Reading-A enclosure fork is UNTOUCHED.** That fork is scored on the
  **torus** cells (no sponge), which read LOOP-FILLING robustly; RULED Reading A
  stands. This NOTE asks a **different question** — the *mechanism* of the
  boundary-DEPENDENT PML core-holding signal, which #698 explicitly left
  SURFACED-NOT-INTERPRETED and routed to Grant. A SELF-TRAPPING or a MODE-SORTING
  verdict here does **not** move Reading A (the fork lives on the torus).
- The #698 **boundary-insensitivity corroboration withdrawal** (Ruling 10) is
  upstream and independent; this NOTE neither relies on it nor disturbs it.

---
---

# RESULT (post-freeze; 2026-07-15)

**Freeze receipt:** the hypothesis + verdict classes + battery grid above were
committed at `f5bce3f7` and **pushed to origin at 2026-07-15T05:54:19Z**; every
battery/parity/sweep run below was computed **after** that push (freeze
discipline intact). **Driver:**
`src/scripts/vol_1_foundations/blob_ablation_kernel_off.py`. Runs: production
`--parity` (datum + byte-parity), `--battery prod` (the 10 frozen cells),
`--sweep prod` (the disclosed working amplitude sweep — see §Instrument).

## VERDICT = **MODE-SORTING** (clean, both axes; the (B) self-trapping predictions FAIL decisively)

The #698 PML-box core-holding (+50.6 % `pair`) is **(A) LINEAR MODE-SORTING** —
the sponge sieves the radiative wake and the surviving bound core-concentrated
fraction holds a **fixed fraction** of energy, **independent of the saturation
kernel and independent of amplitude**. Both gates pass; both discriminator axes
agree.

### Gates
- **Reproduction gate — PASS.** Baseline ON reproduces the datum **exactly**:
  core `0.611 → 0.920 (+50.6 %)`, rest-interior `−17.5 %`, H `−12.2 %`; and the
  mirror loop matches the corrected #698 `run_instrumented` **byte-for-byte**
  (`--parity` core-holding maxΔ = `0.00e+00`, relΔE_persist = `0.00e+00`).
- **Conservation gate — PASS.** The S≡1 override (`off_lin`) on the torus
  conserves H to `−0.0 %` (`E_core_full` `0.351 → 0.265`, H `−0.0 %`): the
  disclosed disabled-flag is a genuine lossless-reactive linearization, not a
  buggy path.

### Kernel-OFF axis (the frozen grid) — the rise SURVIVES kernel-OFF at split = 1.000

| boundary | kernel | core drive→quiet (full reg) | rest-int | H | banked→full (qmean) |
|---|---|---|---|---|---|
| PML(3) | **ON** (baseline/datum) | 0.611 → 0.920 (**+50.6 %**) | −17.5 % | −12.2 % | CONCENTRATING→CONCENTRATING |
| PML(3) | **OFF-mem** (native toggle) | 0.611 → 0.920 (**+50.6 %**) | −17.5 % | −12.2 % | CONCENTRATING→CONCENTRATING |
| PML(3) | **OFF-lin** (S≡1, disclosed) | 0.611 → 0.920 (**+50.6 %**) | −17.5 % | −12.2 % | CONCENTRATING→CONCENTRATING |
| torus(0) | ON | 0.351 → 0.265 (−24.4 %) | +1.6 % | −0.0 % | LOOP-FILLING→LOOP-FILLING |
| torus(0) | OFF-lin (conservation sanity) | 0.351 → 0.265 (−24.4 %) | +1.6 % | **−0.0 %** | LOOP-FILLING→LOOP-FILLING |
| torus(0) | OFF-mem | 0.351 → 0.265 (−24.4 %) | +1.6 % | −0.0 % | LOOP-FILLING→LOOP-FILLING |

`split = OFF-lin plateau ÷ ON plateau = 1.000`. Both registers agree
(potential-only banked and full completed read identically). `OFF_lin = +50.6 %
≥ +40 %` ⇒ the frozen rule's **MODE-SORTING** leaf. The finer OFF-mem cross-check:
the memristive-lag removal changes the trajectory only at the ~13th significant
figure (τ_relax = 1 step ≪ the 52-step quiet window), and the full S≡1
linearization changes H only at the ~5th figure — the saturation kernel is
**dynamically inert on this trajectory**.

### Why the kernel is inert (structural-null / stencil-lens check — verified genuine, NOT a disabled-flag)

All four rank-4 kernels are **flag-ON**; the null is a real field-state property
(measured on the seeded ON engine):

- **V-sector saturation is dormant.** `A²_k4 max = 0` (the pair seed zeros the K4
  V-ports; the field is Cosserat-dominated, `‖u‖ ≈ 4.2` vs `‖V_inc‖ ≈ 0.024`), so
  the Op14 impedance short never engages: the z_local that actually gates bond
  reflection stays `z_local ≡ 1.000` (matched, Γ = 0). `A²_cos max = 0.75` = the
  R_II seed front (this is what `maxA2 = 0.7500` reports — the seed, not a
  dynamics signature).
- **The moving Γ=−1 ω-clamp wall never fires.** The shared-front reflection
  coefficient is `Γ_shared ∈ [0, 0.022]` — **≥ 0 everywhere** (the pair seed is on
  the ε-side / antinode); the wall clamps only the μ-side (`relu(−Γ)`), so
  `Ω₀ ≡ 0` on every site. Removing it (`off_lin`) is therefore a near-no-op.

Because the kernel is dynamically inert, it **cannot** be the trapping agent; the
only thing that differs between the holding PML box (+50.6 %) and the dispersing
torus (−24.4 %) is the **sponge**. The core-holding is the sponge removing the
recirculating wake — linear mode-sorting.

### Amplitude axis (the DISCLOSED working sweep) — FRACTION-PRESERVING (no (B) signature)

The frozen pair-seed amp knob is a **no-op** (§Instrument). The disclosed working
knob (`field_scale`, post-seed Cosserat scale ⇒ `A²_cos = 0.75·field_scale²`,
kernel-ON, PML) gives:

| field_scale | A²_cos front | core drive→quiet | hold-rel |
|---|---|---|---|
| 0.50 | 0.19 | 0.153 → 0.230 | +50.58 % |
| 0.75 | 0.42 | 0.344 → 0.518 | +50.57 % |
| 1.00 | 0.75 | 0.611 → 0.920 | +50.57 % |
| 1.10 | 0.91 | 0.740 → 1.114 | +50.57 % |

The **absolute** core energy scales `∝ field_scale²` (constant 0.612) — perfectly
linear — while the **hold-fraction is amplitude-invariant to 4 sig figs**
(spread = `0.0001`) across a ~5× energy range that pushes the front from mild
(A²_cos = 0.19, Regime II) toward rupture (A²_cos = 0.91, approaching R_III = 1).
**No superlinear growth. No low-amplitude dispersal threshold** (0.5× still holds
+50.6 %). The exact invariance over a 5× range is itself a signature of **linear**
dynamics. Torus twins disperse (−24.4 %) at both endpoints, H conserved. This is
the frozen (A) FRACTION-PRESERVING signature — **the (B) SUPERLINEAR predictions
are falsified.**

### Honest closure (Rule 11)

All three pre-registered **(B)** predictions fail decisively and a **single
mechanism** explains every failure: *the saturation kernel is dynamically inert
in the Cosserat-dominated loop-gap regime (V-sector dormant + ω-wall on the
ε-side), so the sponge does the sorting linearly.* (i) kernel-OFF does **not**
kill the rise (split = 1.000); (ii) the hold is **not** superlinear in amplitude
(fraction-preserving to 4 sig figs); (iii) there is **no** low-amplitude
dispersal threshold. Clean negative result for self-trapping **at this config**;
branch closed toward MODE-SORTING. The decision rule was **not** re-tuned to the
outcome.

**Scope (honest).** MODE-SORTING is the verdict **for the #698 config** (rank-4
loop-gap pair seed, N=14, PML=3). The reason is that the kernel is inert **here**;
a config that genuinely excites the V-sector (so the z_local short engages) or a
μ-side seed (so the Γ=−1 wall fires) is a **different** regime and is not
adjudicated by this run. The puddle/breather items are therefore recorded as
*not-supported-**at-this-config***, not as impossible-in-AVE.

## Consequence routing — MODE-SORTING branch (statuses exact)

- The census Stage-2 kernel-OFF-twin control **demotes to
  `RECOMMENDED-cheap-control`** (it remains cheap and worth carrying, but it is
  not a REQUIRED discriminator here — the kernel is inert at this config).
- The **PUDDLE class** and the **BREATHER-CONNECTION** items record as
  **`not-supported-at-this-config`** (no engine-level dynamical-binding signature
  at the #698 config: the core-holding is the sponge, not a self-dug well).
- **Interpretation beyond the classes is routed to Grant.**

## FLAG-DON'T-FIX — surfaced to Grant (NOT resolved here)

Two engine/config observations **explain** the kernel's inertness and are
surfaced verbatim for adjudication (they do **not** change the MODE-SORTING
verdict — the kernel is inert regardless — but they matter for other regimes):

1. **z_local overwrite (update-ordering).** In `CoupledK4Cosserat.step`, the
   coupling's `_update_z_local_total` computes a Cosserat-informed short
   (measured `z_local` up to **1.045** on 45 seeded sites), but `k4.step`'s
   `_update_z_local_field` (`op3_bond_reflection=True`) then **recomputes z_local
   from V_inc only and overwrites it** — flat `1.000`, because `A²_k4 = 0`. So the
   **Cosserat → V-sector bond-short channel is defeated by ordering** whenever the
   V-sector is quiet. Harmless here (V-sector carries ~0 energy); potentially
   load-bearing in a V-excited regime.
   [`src/ave/topological/k4_cosserat_coupling.py` `_update_z_local_total` /
   `src/ave/core/k4_tlm.py` `_update_z_local_field`]
2. **Γ=−1 ω-wall dormant on the ε-side.** For the pair seed the shared-front
   `Γ_shared ≥ 0` everywhere (ε-side / antinode), so `relu(−Γ) = 0` and the moving
   confinement wall (`Ω₀`) is **never engaged**. Whether the loop-gap pair seed
   *should* present a μ-side (node) front to this wall is a design question.
   [`src/ave/topological/k4_cosserat_coupling.py` `_freeze_clamp_omega0_shared`]

## §Instrument — the frozen amplitude sweep was a NO-OP (INSTRUMENT-defect, disclosed)

Rule-10 caught this at integrator time: the frozen amplitude knob (pair-seed
`amp = amp_scale·√α`) is a **no-op** because `pair_seed_cosserat`
(`src/ave/core/genesis_v18_coupled.py:129-131`) **front-normalizes the Cosserat
field to a fixed R_II** (`scale_cosserat_to_front target=R_II`) regardless of
`amp` — so amp 0.5×/1.0×/1.5× produce **byte-identical** cells (battery rows 4–5
== row 1; and the bulk probe at 0.08 is too small to move 3-decimal core
numbers). This defect affects **only the frozen amplitude-sweep axis**; the
kernel-OFF axis (runs 1/2/3/10) is unaffected. Per KEEP-BOTH, the frozen axis is
reported as INSTRUMENT-defective (the `FRACTION-PRESERVING` it mechanically
returns is **vacuous**), and a **disclosed working knob** (`field_scale`,
post-seed Cosserat scale, §Amplitude axis above) supplies the real sweep
evidence. The frozen decision rule is unchanged; the substitution is disclosed,
not silent.

## Firewall (reaffirmed) — untouched

- **G-PERSIST ★RULED — UNTOUCHED.** The A1 energy meter used here is `⊥` the
  T2/Φ_link winding channel the ★RULED flip rests on; a MODE-SORTING verdict on
  the A1 core-holding cannot reach the ★RULED basis.
- **Reading-A enclosure fork — UNTOUCHED.** That fork lives on the torus (no
  sponge); this verdict is about the *mechanism* of the boundary-**dependent**
  PML signal #698 left SURFACED-NOT-INTERPRETED. Reading A stands.

---
---

# AMENDMENTS (2026-07-15, post-review — adversarial review of PR #706)

Independent adversarial review of PR #706 (13 agents, 3 lenses — freeze-parity,
engine-flags, live-fire): **10 confirmed findings, 0 refuted, ALL MINOR** after
verification. **MODE-SORTING banks** with the scoping corrections below (the two
MAJOR-tabled findings were both DOWNGRADED to MINOR/EVIDENCE-VOID: the conclusion
is independently sound, only the demonstration language/gate wiring needed
repair). Per freeze discipline the frozen body **and** the RESULT section above
are left **byte-untouched**; each item below is a **dated amendment** that
supersedes the referenced text. Every review number quoted here was
**independently reproduced** by the now-shipped `--diag prod` diagnostic
(`run_inertness_probe` / `run_patched_ordering_diag`) — two-method (this driver's
per-step probe + the review's live-fire), matching to the quoted digits.

## A1 — Inertness: absolutes → BOUNDED TRANSIENTS (supersedes RESULT §"Why the kernel is inert" + the F2 flag)

The RESULT presents three inertness quantities as trajectory identities; they are
in fact **t=0 seed-state** values (the shipped run loop scanned only A²_cos). The
per-step scan over the full 70-step datum trajectory (`--diag prod`, N=14, pml=3,
pair, on, amp=1.0) corrects them:

| quantity | t=0 seed (as the RESULT states) | over the RUN (corrected, this driver) | review live-fire |
|---|---|---|---|
| A²_k4 max | 0 | **5.9e-4** (converter injects V after t=0) | 5.95e-4 |
| Γ_shared range | [0, +0.022] (≥0) | [**−2.3e-4**, +0.022] (dips negative) | −2.29946e-4 |
| Ω₀ (ω-wall) max | 0 on every site | **5.6e-2** transient @ t=2 | 5.648e-2 @ t=2 |

**Read every inertness absolute** ("`A²_k4 max = 0`", "`Γ_shared … ≥ 0
everywhere`", "`Ω₀ ≡ 0 on every site`", "the wall **never fires**") **as:
"dynamically negligible — bounded transients (A²_k4 ≲ 6e-4, Γ ≳ −2.3e-4, Ω₀ ≲
5.7e-2); removal changes nothing to 4 sig figs (the OFF/ON split = 1.000 is the
load-bearing discriminator)".** The transients are 3–4 orders below the front
(A²_cos = 0.75) and below the meter; `off_lin` (which sets Ω₀ ≡ 0 *exactly*)
reproduces ON to every reported figure. Verdict unchanged. The **F2 flag** wording
("relu(−Γ) = 0 … the wall is never engaged") is corrected to the same
bounded-transient phrasing.

## A2 — F1 flag REWRITTEN (supersedes RESULT §FLAG-DON'T-FIX item 1, verbatim below)

> **F1 (rewritten) — the Cosserat → V-sector bond-short channel is defeated
> UNCONDITIONALLY under `op3_bond_reflection=True` (every step, every regime), not
> "whenever the V-sector is quiet".** In `CoupledK4Cosserat.step`,
> `_update_z_local_total` writes the Cosserat-informed shared front
> `Z_eff = √(S_μ/S_ε)` to `k4.z_local_field` (step 1); then `k4.step` →
> `_scatter_all`'s first action — gated ONLY on `op3_bond_reflection` (hardwired
> `True` in the coupled engine, `k4_cosserat_coupling.py:306`) — **recomputes
> `z_local` from `V_inc` only** (`z = 1/√S_eq(V)`, memristive-lagged,
> `k4_tlm.py:272-294`) and **overwrites the coupling's write BEFORE `_connect_all`
> consumes it** for the bond Γ. The Cosserat A² contribution therefore **never
> reaches the bond Γ in any regime**. The visible symptom differs by regime:
> **flat `z ≡ 1.000` when V is quiet** (this config), and the **wrong V-only form
> `1/√S(V)` — not the intended asymmetric shared front — when V is excited** (the
> channel does NOT self-heal on V waking). Consequently the "one front, both
> sectors (CP2)" coupled-impedance **V-side** (`k4_cosserat_coupling.py:897`, "the
> V-sector short is applied via z_local in (1)") is **structurally dead
> engine-wide** in every `op3_bond_reflection=True` `CoupledK4Cosserat` instance;
> the shipped ordering contradicts the `:866` / `:373-375` / `:897` design
> comments and no corpus/comment supports the V-only recompute as the deliberate
> master ⇒ **DEFECT-CANDIDATE** (routed to Grant, NOT fixed here).
>
> - **Empirically immaterial at this config (measured, not asserted):** the
>   patched-ordering diagnostic (`--diag prod`; `k4._update_z_local_field` no-op'd
>   so the coupling short survives — `|z−1|` up to **4.53e-2** in-run, genuinely
>   live) reproduces the datum to **+0.0000%** (shipped core-rel +0.5057 = patched
>   +0.5057; core 0.6113 → 0.9205), because the defeated well gates only the
>   ~0-energy V-sector and the ω-wall computes Γ via `_impedance_gamma_shared`
>   independently of `k4.z_local_field` (so F1 cannot hide Cosserat-side
>   confinement).
> - **★REGISTERED follow-ons (routed to Grant / auditor lane; NOT fired here):**
>   (i) engine **ordering fix** (consume the coupled shared-front short before the
>   V-only recompute, or reconcile the two kernels) + regression; (ii) a
>   **CONSUMER AUDIT** of every **V-active** coupled simulation run under
>   `op3_bond_reflection=True` — those may have consumed the wrong `z_local` form
>   (V-only `1/√S(V)` instead of the asymmetric shared front); which banked results
>   are affected is un-surveyed; (iii) a cheap **re-run of this fork on the
>   ordering-fixed engine**, gated on Grant's F1 adjudication (expected
>   verdict-neutral per the diagnostic).
> - Line-ref correction: the "V-sector short is applied via z_local in (1)"
>   comment is at `k4_cosserat_coupling.py:897` (the RESULT cited :902).

## A3 — Regime declaration (supersedes the frozen sector-header "seed front A = √α, A² = α" line + the REGIME "cold→moderately-saturated" line)

The frozen header's "Baseline seed front `A = √α` … seed-front `A² = α` — the
whole excitation sits well below the `A²=1` rupture" is **wrong by ~100× in A²**:
`pair_seed_cosserat` front-normalizes the Cosserat field to **R_II = √3/2, i.e.
A²_cos = 0.75** (the nonlinear→saturated knee), regardless of the amp knob
(`genesis_v18_coupled.py:129-131`; the same stale √α belief that made the frozen
amp knob a no-op). `√α` is genuinely the V-*register* yield landmark
(`loop_gap_seeds.py:44`) but the un-scoped "whole excitation" clause
over-generalizes it onto the Cosserat-dominated excitation. **Operative regime
(corrected):** the trajectory sits **at the R_II front (A²_cos = 0.75, top of
Regime II)**, with V-sector zeroed at seed (A²_k4 = 0) and the sweep hi-point at
A²_cos = 0.91 (approaching R_III = 1); every cell stays sub-yield (abort guard
live, no cell crossed A²=1). Direction is **conservative** — kernel inertness at a
0.75 front is *more* surprising and **strengthens** MODE-SORTING. The head test
docstring echoing "well below A²=1" is fixed in the same commit.

## A4 — Verdict scope + the "cannot be the trapping agent" sentence (supersedes RESULT §Scope + §Kernel-OFF axis)

Read the scope as: **"MODE-SORTING at this configuration (#698 rank-4 loop-gap pair
seed, N=14, PML=3) AND with the shipped update-ordering (F1) — the kernel is
dynamically negligible here: bounded transients + the F1-defeated coupled
bond-short leg, whose restoration changes nothing at this config per the
patched-ordering diagnostic (+0.0000%)."** Qualification: "a config that genuinely
excites the V-sector (so the z_local short engages)" is imprecise — on the shipped
engine **only k4's legacy V-only short can ever reach `_connect_all`**; the
intended Cosserat-informed coupled short is overwritten in *any* config (A2). The
coupled-bond-short leg of the kernel-OFF ablation is thus **vacuous** (the channel
was dead-by-ordering in BOTH ON and OFF baselines) — but MODE-SORTING is
independently carried by the kernel-OFF split = 1.000, the ω-wall (F1-independent)
inertness, and the disclosed amplitude axis.

## A5 — Word fix (supersedes RESULT §Instrument "byte-identical cells")

"so amp 0.5×/1.0×/1.5× produce **byte-identical** cells" → **"observationally
identical at the reported precision"**: the bulk-probe IC channel is live and
scales with amp_scale (`apply_bulk_probe_ic(amp=amp_scale·0.08)` → 0.04/0.08/0.12),
so the cells differ at the input level (sub-3-decimal on the core observable); the
front-normalized Cosserat seed is the no-op, not the whole cell. The frozen-sweep
vacuousness verdict is unchanged.

## A6 — Machine-gate rewire (code, findings 2/8; no doc supersession)

`cmd_aggregate` previously computed the MODE-SORTING amplitude conjunct from the
**frozen** amp cells (structurally unfireable — byte-identical ⇒ always
FRACTION-PRESERVING) while the real `disc_sig` (field_scale) gated nothing. Rewired
so the amplitude conjunct **consumes `disc_sig`** (the disclosed working sweep),
emits **`…-PENDING-SWEEP` / SWEEP-INCOMPLETE** when only the vacuous axis exists,
and keeps the `[VACUOUS … does NOT gate]` label on the frozen axis. Re-run verdict
is **unchanged: MODE-SORTING** (disc_sig = FRACTION-PRESERVING, spread 0.0001;
OFF-lin split = 1.000).

## Two-method verification receipts (`--diag prod`, this driver vs the review)

- Inertness: A²_k4_max **5.945e-4** (review 5.95e-4); Γ_shared_min **−2.299e-4**
  (review −2.29946e-4); Ω₀_max **5.648e-2 @ t=2** (review 5.648e-2 @ t=2).
- F1 patched-ordering: coupling |z−1| in-run **4.531e-2** (review 4.53e-2); Δcore-rel
  **+0.0000%** (review +0.0000%). All match to the quoted digits.
- Verdict / gates after the amendments: `make verify` PASS; 5/5 unit tests PASS;
  re-run `--aggregate` VERDICT = **MODE-SORTING** (now gated on the real axis).
