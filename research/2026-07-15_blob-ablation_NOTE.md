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
