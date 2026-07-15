# NOTE — Two-Tank Decoherence Check (thermal-phase-registers walk, registered check)

**Date:** 2026-07-15 · **Lane:** TWO-TANK DECOHERENCE CHECK (registered check from Grant's
2026-07-15 thermal/phase-register walk — "let's do them" / "fire the test")
· **Driver:** [`src/scripts/vol_1_foundations/two_tank_decoherence_check.py`](../src/scripts/vol_1_foundations/two_tank_decoherence_check.py)
· **Test:** [`src/tests/test_two_tank_decoherence_check.py`](../src/tests/test_two_tank_decoherence_check.py)
· **Engine imported UNMODIFIED:** `src/ave/core/k4_tlm.py` `K4Lattice3D` (native V-sector TLM lattice)
· **The leaf this check gates:** `manuscript/ave-kb/common/thermal-phase-registers.md` §2/§4
  (branch **`docs/2026-07-15-walk-batch`**, commit `c29e61ed`; **not yet merged to main** — cited by
  branch per verify-before-cite).

> **Ordering discipline (no answer-shaping).** This note is committed **hypothesis-first**:
> §1 (hypothesis) + §2 (verdict classes) + §3 (method) were frozen and committed BEFORE the
> production sweep was run; §4 (results), §5 (implications), §6 (leaf consequence) were appended in
> a SEPARATE, later commit. The verdict-class thresholds live in the driver's module constants +
> `classify()` (declared in code before the run) and are unit-tested at their frozen boundaries.
> Git history carries the split.

> **TL;DR (verdict §4.6): `ADDITIVE-ARTIFACT`.** The two clocks' relative phase **does** diffuse
> (MSD `∝ τ`, slope `~1.1`) with variance monotone in `u_bath` — so the leaf's literal "monotone
> variance-growth-vs-bath-energy" criterion is met. **But the substrate-native mechanism control kills
> it:** the pure-**linear** lattice (Op14 kernel OFF) reproduces the same diffusion (kernel-excess
> `0.19 → −0.001` when the bath is densified), so the diffusion is **additive wave-interference**, not the
> proposed `bath → A² → S → clock-rate` mechanism. When the additive bath is spectrally rejected, the
> **isolated Op14 differential phase is BOUNDED** (`MSD` slope `~0.10`) — reversible dephasing, forced by
> Ax3-losslessness (`energy_drift ~ 10⁻¹³`). Control machine-clean (`Δφ ~ 10⁻¹³` rad). The proposed
> "temperature = clock phase-**diffusion (rate)**" definition is **NOT demonstrated**; the leaf's §1 Ax3
> "reversible phase-scramble" framing is confirmed, and a genuine diffusion-rate thermometer is gated on
> the **unbuilt F6 irreversibility channel** (§5 item 4, flag).

---

## Sector / regime header (declared before any number)

- **SECTOR** — thermal / **incoherent-propagating V-sector register**: the "3" longitudinal scalar
  K4 voltage field on the bond capacitance (the Heaviside-excised scalar; **NOT** a transverse
  photon). This is the third phase-register of `thermal-phase-registers.md` §3
  (coherent-bound / coherent-propagating / **incoherent-propagating**).
- **MODE** — closed (undriven), **lossless** two-body phase-statistics measurement. Two identical
  localized V-oscillators ("clocks") immersed in a common incoherent traveling-wave bath.
- **REGIME** — **sub-yield.** Clock operating point `A_clk ≈ 0.08` (≈ `V_YIELD/V_SNAP = √α ≈ 0.0854`,
  the regime-I/II boundary); bath **deep-linear** (`A_bath ≪ R_I = √(2α) ≈ 0.121` everywhere); total
  field sub-rupture (`A < R_III = 1`), predominantly regime-I. Max realized strain is reported per run
  and gated against `R_I`.
- **PHASE-STATE** — cold substrate + incoherent V-bath perturbation.
- **KERNEL** — measured **BOTH ways** (substrate-native regime discipline): **ON** (`nonlinear=True` +
  `op3_bond_reflection=True`; the Op14 saturation `S = √(1−A²)` active = the proposed thermal-clock
  mechanism) and **OFF** (pure linear lattice; mechanism disabled = additive-interference control).
- **CLASS (consistency-vs-emergence)** — **CONSISTENCY.** This check adjudicates whether a proposed
  DEFINITIONAL operationalization is internally consistent with the engine. No CODATA input, no value
  minted, no emergence headlined.
- **PHASE-SPACE-COORDINATE DISCIPLINE (A46)** — the clock phase is read in the native
  `(V_inc, V_ref)` / `(V, Φ_link)` phasor plane (a phase-space coordinate), **not** a real-space
  Cartesian projection of `φ²`. `Δφ(t)` is a phase-plane angle difference. Both reactance-pair states
  (C-state node voltage `V`, L-state flux linkage `Φ_link`) are recorded every step
  (reactance-pair-tracking discipline).

---

## 1. Hypothesis (stated FIRST, before any number)

**The registered claim under test** (`thermal-phase-registers.md` §2, PROPOSED-DEFINITIONAL):

> **"temperature = the width of the clock-detuning distribution."** Operationalized (§4): *seed two
> identical soliton tanks + a random traveling bath; measure relative-phase variance growth vs bath
> energy density. A monotone variance-growth-vs-bath-energy relation confirms it at consistency-class.*

The **mechanism** the walk names (per the task framing + leaf §1) is the substrate's own Op14
clock-rate modulation: **bath energy raises the time-averaged local strain `A²` → the saturation
kernel `S = √(1−A²)` drops → the local clock rate `ω_local(r) = ω₀·√(1−A²(r))` slows.** The observable
splits into two halves (leaf §1):

- **(a) the MEAN shift (the TCC / operating-point half).** Both clocks detune *together* (common-mode).
  Kernel prediction: `⟨A²_total⟩ = A_clk² + ⟨A²_bath⟩` (the clock–bath cross-term time-averages to zero
  for an incoherent bath), so `⟨ω_local⟩ = ω₀·⟨√(1−A²)⟩ < ω₀` — the clocks **slow**, by an amount
  `∝ −u_bath` at leading order. Sign predicted (negative), magnitude definitional.
- **(b) the VARIANCE (the heat-content half).** `Var[Δφ](t)` — the *differential* phase random-walk.
  Kernel expectation: the fluctuating detuning is dominated by the clock–bath cross-term
  `δω(t) ∝ −ω₀·A_clk·A_bath(t)/√(1−A_clk²)` (first order in the bath amplitude, `∝ √u_bath`), so
  `Var[δω] ∝ u_bath`; if the bath decorrelates with a `u`-independent correlation time `τ_c`, the phase
  random-walks with diffusion constant `D = Var[δω]·τ_c ∝ u_bath`.

**Two identical, well-separated tanks** (translation-related on the periodic lattice) give a **provably
clean control**: with the bath OFF, `Δφ(t) ≡ 0` to machine precision, so the bath is the *only*
symmetry-breaking source. Separation `≥ N/2` decorrelates the two sites' bath realizations so the
differential phase can random-walk.

> **⚑ Sharper-than-the-leaf discriminator (flag-don't-fix, built into the frozen method).** The leaf's
> §1 narrative attributes the variance to *"Johnson-Nyquist strain-noise jittering every tank"* while
> its §1 Ax3 line frames heat as *"phase disorganization of reactive energy, NOT loss"* — i.e. a
> **reversible** scramble. But a bath field also **additively superposes** at each clock site, and
> reading the local phasor angle of the *total* (clock + bath) field will show a differential phase
> wander **even in a purely LINEAR lattice with no Op14 mechanism at all** — a trivial
> which-patch-of-bath wave-interference effect, not the proposed clock-rate decoherence. Per the
> regime discipline (*a signal that survives disabling its claimed mechanism is an artifact*), this
> check therefore measures the phase statistics with the **kernel ON and OFF** and attributes the
> variance to the Op14 mechanism only via the **kernel-excess** `(Var_ON − Var_OFF)/Var_ON`. This is
> stricter than the leaf's literal "monotone variance-growth-vs-bath-energy" criterion, which an
> additive-interference artifact would satisfy by itself.

---

## 2. Verdict classes (DECLARED before the computation; frozen in the driver)

Frozen thresholds live in the driver as module constants (`CTRL_FLOOR`, `DIFF_LO/HI`, `BALLISTIC_LO`,
`BOUNDED_HI`, `P_LIN_LO/HI`, `EXCESS_MIN`) and in `classify(Summary)`; unit-tested at their boundaries.
Reduced sweep observables → class:

| Class | Criterion (frozen) | Reading |
|---|---|---|
| **CONTROL-FAIL** | u=0 control `Δφ` span `> CTRL_FLOOR (1e-3 rad)`, either kernel | instrument artifact — **STOP** before any physics verdict |
| **NON-DIFFUSIVE** | kernel-ON MSD log-log slope `≤ BOUNDED_HI (0.30)` (bounded) **or** `≥ BALLISTIC_LO (1.70)` (ballistic `t²`) | the proposed **diffusion** definition **FAILS as posed** |
| **ADDITIVE-ARTIFACT** | diffusive-shaped (slope in `(0.30, 1.70)`) **but** kernel-excess `(Var_ON−Var_OFF)/Var_ON < EXCESS_MIN (0.50)` | `Δφ` diffuses, but **kernel-independent** → the variance is additive wave-interference, **NOT** the Op14 thermal-clock mechanism; the substrate-thermal definition is **NOT demonstrated** |
| **DIFFUSIVE-LINEAR** | diffusive-shaped, kernel-driven (excess `≥ 0.50`), and `D(u)` log-log exponent `p ∈ [0.80, 1.30]` | `Var[Δφ] ∝ t`, `D ∝ u_bath`, from the mechanism → the definition is **MEASURED** (report `D(u)` thermometer calibration) |
| **DIFFUSIVE-NONLINEAR** | as DIFFUSIVE-LINEAR but `p ∉ [0.80, 1.30]` | survives with a **nonlinear** calibration; report `p` |

Primary shape statistic: the MSD log-log slope of `Δφ(t)` (anomalous-diffusion exponent; 1 = diffusive,
2 = ballistic, ~0 = bounded). Mechanism attribution: the kernel-excess. `u`-scaling: `p = ` log-log
slope of `D_ON(u)`. The isolated-Op14 readout (lock-in demod at `ω₀`, rejecting additive bath spectrally)
is reported as a cross-check on the mechanism's own shape.

---

## 3. Method

1. **Engine.** Native `K4Lattice3D`, `N = 16` periodic (torus, `pml_thickness=0`), `V_SNAP=1.0`
   (native units, strain `A = |V|`; avoids the Flag-5e-A dormant-saturation trap). Cheapest native
   harness that carries the load-bearing DOF: the V-sector phasor `(V_inc, V_ref)` is the phase-space
   coordinate; the Op14 saturation kernel is the bath-coupling mechanism; **no Cosserat `(u,ω)` DOF is
   load-bearing** for clock-phase diffusion, so the coupled cage is not needed.
2. **Clocks.** Two identical Gaussian-windowed standing V-oscillations (`amp = 0.08`, `σ = 1.5`,
   carrier `k = π/2`) seeded at `(N/4, N/2, N/2)` and `(3N/4, N/2, N/2)` → separation `N/2 = 8`
   (`≥ half the lattice`, non-overlapping envelopes). Their single-site node-voltage `V = Σ_ports
   (V_inc + V_ref)` oscillates at a well-defined `ω₀` and persists at stable amplitude over the window
   (validated: lossless recirculation keeps the local antinode populated).
3. **Bath.** `M = 40` random plane waves (random `k`-direction on the lattice, random phase, random
   per-port weight), scaled to a target mean active-site energy density `u_bath` — an incoherent,
   microcanonical (fixed initial-condition) traveling-wave bath. `u_bath ∈ {0, 1e-4, 3e-4, 9e-4,
   2.7e-3}` (control + 4 log-spaced, ratio 3), all sub-yield; **3 seeds** per non-zero value.
4. **Kernel ON / OFF.** Every `(u, seed)` is run with the Op14 kernel **ON** (`nonlinear` +
   `op3_bond_reflection`) and **OFF** (pure linear). The **u=0 controls run first** (mandatory).
5. **Readout.** PRIMARY = the analytic-signal (Hilbert) phase of the single-site node voltage `V(t)`
   at each clock — the literal "phase of the local oscillation," which includes any additive bath at
   the site (that is what the kernel-OFF control disentangles). `Δφ(t) = φ₁ − φ₂` (edge-trimmed).
   ISOLATED-Op14 cross-check = lock-in demod at `ω₀` (spectral bath rejection). Both reactance-pair
   states `(V, Φ_link)` recorded every step.
6. **Estimators.** Time-averaged MSD `M(τ) = ⟨(Δφ(t+τ)−Δφ(t))²⟩_t`; shape = log-log slope; `D` from
   `M ≈ 2Dτ`; common-mode mean-shift = long-window slope of `½(φ₁+φ₂)` minus `ω₀`; kernel-excess =
   `(Var_ON − Var_OFF)/Var_ON` at window end; `p =` log-log slope of `D_ON(u)`.
7. **Verdict** = `classify(Summary)` on the reduced medians. **One disclosed rescue allowance**
   (honesty rail): if kernel-ON is NON-DIFFUSIVE-bounded, a single mode-density increase
   (`N=24, M=150`, `--mode-density-up`) is run to test whether the bounded-ness is a finite-bath
   (Poincaré-recurrence) artifact. No other tuning.
8. **Discretization caveat.** Modest lattice (`N=16`, `N=24` for the rescue); this is a
   phase-statistics measurement, not a convergence study. A closed lossless lattice is quasi-periodic
   (finite recurrence), so any "diffusion" is only asymptotic *within* the window; the recurrence
   caveat is load-bearing for the verdict and is reported.

---

## 4. Results

**Driver as-run:** `N = 16` periodic, `V_SNAP = 1`, `N_STEPS = 3000`, clock `amp = 0.08` / `σ = 1.5`
/ `k = π/2`, sites `(4,8,8)` & `(12,8,8)` (**sep = 8 = N/2**), bath `M = 40`, `u_bath ∈ {0, 1e-4,
3e-4, 9e-4, 2.7e-3}`, **3 seeds** per non-zero `u`, kernel **ON + OFF**. Constants imported
(`R_I`, `R_II`, `R_III`, `V_YIELD`, `V_SNAP`, `ALPHA`); `make verify` green at HEAD. Output
`assets/sim_outputs/two_tank_decoherence_check_{production,mode_density_up}.{json,png}` (gitignored,
regenerable). Wall 126 s (production).

### 4.0 Control (mandatory, run FIRST) — PASSES

`u_bath = 0`: the two clocks are translation-related, so `Δφ(t) ≡ 0` to machine precision — for BOTH
kernels. `ctrl_span_on = 6.8×10⁻¹³` rad, `ctrl_span_off = 9.1×10⁻¹³` rad (both `≪ CTRL_FLOOR = 1e-3`).
`Δφ` rms over the whole window: `1.0×10⁻¹⁴` (ON) / `2.8×10⁻¹⁴` (OFF). **No CONTROL-FAIL** — the
instrument is clean; the bath is the only symmetry-breaking source.

### 4.1 The differential-phase statistics (raw single-site readout) — DIFFUSIVE-SHAPED, `D(u)` table

The raw `Δφ(t)` (analytic-signal phase of the total local field) **does** grow like a random walk
(MSD `∝ τ`, slope `~1.1`) and its variance **is** monotone in `u_bath` — so by the leaf's *literal*
§4 criterion ("monotone variance-growth-vs-bath-energy") the naive measurement looks **confirmed**. The
`D(u_bath)` "thermometer" table, kernel ON vs OFF (median over 3 seeds, rad²/step):

| `u_bath` | `D_ON` | `D_OFF` | MSD slope (ON) | kernel-excess `(V_on−V_off)/V_on` | max strain |
|---:|---:|---:|---:|---:|---:|
| 1×10⁻⁴ | 0.550 | 0.667 | +1.12 | **+0.059** | 0.0848 |
| 3×10⁻⁴ | 0.560 | 0.469 | +0.99 | **+0.329** | 0.0886 |
| 9×10⁻⁴ | 1.494 | 1.058 | +1.19 | **+0.316** | 0.0957 |
| 2.7×10⁻³ | 1.603 | 1.731 | +1.07 | **−0.112** | 0.1289 |

`D_ON(u)` log-log exponent `p = 0.38` — **sub-linear**, already off the predicted `D ∝ u¹`.

### 4.2 Mechanism attribution (kernel ON vs OFF) — the diffusion is ADDITIVE, not Op14

**`D_OFF ≈ D_ON` at every `u`.** The pure-**linear** lattice (Op14 kernel entirely disabled) reproduces
the same diffusion: median kernel-excess `= 0.187` (`< EXCESS_MIN = 0.50`); at the top `u` it is
*negative*. So the phase-diffusion is **additive wave-interference** — two separated points embedded in
independent patches of a random bath have independently-winding *total-field* phasors whose difference
random-walks — **present in full with no Op14 mechanism at all.** Confirming this from the other side:
the **isolated-Op14 readout** (lock-in demod at `ω₀`, which rejects the additive bath spectrally) is
**BOUNDED** — MSD slope `shape_iso ≈ 0.10` at all three sub-`R_I` values (the top-`u` `0.98` is the
regime-II / bath-swamps-clock point, §4.5). **The Op14 clock-rate mechanism, isolated, does NOT produce
a phase random-walk; it produces bounded, reversible dephasing.**

### 4.3 The MEAN-shift half (TCC / operating point) — below the additive floor

Common-mode shift (bath-on minus control, to cancel the fixed `ω₀`-reference offset): `+1.7×10⁻²`,
`+3.7×10⁻²`, `+4.1×10⁻²`, `+2.1×10⁻²` rad/step for the four `u`. These are small, non-monotone, and
**positive** — the *wrong* sign for the kernel's predicted slowing. The kernel prediction is
`Δω_mean ≈ −½ω₀·u_bath ≈ −0.6·u ≈ −1.6×10⁻³` rad/step at the top `u` — **an order of magnitude below the
additive-contamination floor** (`~2–4×10⁻²`) at the single-site total-field readout. So the TCC/operating-
point half is *also* additive-limited: the Op14 slowing is real in the kernel but too small to resolve
above the additive bath pull at these sub-yield `u`. (Honest closure, not a rescue: the mean-shift is a
secondary cross-check; the primary variance half is decisive.)

### 4.4 The one disclosed mode-density increase (`N=24`, `M=150`) — verdict UNCHANGED

Per the single allowed rescue (honesty rail), the bath mode density was raised (`N=16/M=40 →
N=24/M=150`). Result: **verdict still ADDITIVE-ARTIFACT.** Raw MSD slope `1.11` (still diffusive-shaped),
but the **kernel-excess collapses to `−0.001`** (median; per-`u` `{+0.02, −0.02, +0.02, −0.42}`) — with
a denser bath the Op14 contribution to the diffusion is **exactly zero**. The isolated-Op14 slope rises
to `1.09` — i.e. at higher mode density the additive bath leaks into the lock-in band too, so *even the
spectrally-isolated readout* is now additive-dominated. **The mode-density increase does not rescue the
Op14 mechanism — it only adds more additive interference.** The bounded Op14 signature (`shape_iso ≈
0.10` at `N=16`) plus the zero excess at both densities together settle it: the mechanism does not drive
diffusion.

### 4.5 Regime witnesses

- **Lossless (Ax3):** `energy_drift_max = 1.6×10⁻¹³` (production) — energy conserved to machine
  precision; the system is a closed reactive lattice, no dissipation anywhere. (Load-bearing for §5.)
- **Sub-yield:** max realized strain is `0.085 → 0.096` (`< R_I = √(2α) = 0.1208`) for the three lower
  `u`; only the top `u = 2.7×10⁻³` reaches `0.1289`, a brief **regime-II** (`R_I < A < R_II = √3/2`)
  core excursion at the clock antinode where clock + bath add constructively — still **sub-rupture**
  (`≪ R_III = 1`). The verdict is robust on the three strictly-sub-`R_I` points (the top-`u` point is
  the noisiest anyway: negative excess, contaminated `shape_iso`).

### 4.6 Verdict

**`ADDITIVE-ARTIFACT`** (`classify()` at frozen thresholds; `make verify` green). The differential clock
phase *does* diffuse (MSD `∝ τ`, variance monotone in `u_bath`) — so the leaf's literal criterion is
satisfied — **but the substrate-native mechanism control proves the diffusion is additive wave-
interference, not the proposed Op14 thermal-clock mechanism** (kernel-excess `0.19 → −0.001`; isolated-
Op14 differential phase bounded). **The proposed "temperature = clock phase-diffusion (rate)" definition
is NOT demonstrated as a substrate-thermal statement.**

---

## 5. Implications

**The naive measurement passes; the mechanism control fails it. That gap IS the finding.**

1. **A false positive, caught by the substrate-native mechanism control.** The leaf's registered
   criterion (§4: "a monotone variance-growth-vs-bath-energy relation confirms it") is **satisfied by the
   raw readout** — `Δφ` diffuses (`MSD ∝ τ`) with variance rising in `u_bath`. Had this check stopped at
   the leaf's bar, it would have reported "confirmed." The **kernel ON-vs-OFF control** (added to the
   frozen method precisely because *the total-field phasor at a point in a random bath winds even in a
   linear medium*) shows the diffusion is **kernel-independent** (excess `0.19 → −0.001`) — it is
   additive wave-interference, a which-patch-of-bath kinematic effect, **not** the proposed
   `bath → A² → S = √(1−A²) → clock-rate` decoherence. This is the regime discipline working: *a signal
   that survives disabling its claimed mechanism is an artifact.*

2. **The isolated Op14 mechanism gives BOUNDED, reversible dephasing — consistent with Ax3.** When the
   additive bath is rejected (lock-in), the Op14 clock-rate modulation's differential phase is **bounded**
   (`MSD` slope `~0.10`), not a random walk. This is not a numerical accident — it is **forced by
   losslessness**: `energy_drift ~ 10⁻¹³` confirms the lattice is a **closed reactive system (Ax3)**, and
   a closed reactive system is **time-reversible** ⇒ its phase relationships are **quasi-periodic / bounded
   on the Poincaré-recurrence timescale**, not monotonically diffusing. *You cannot get irreversible phase
   diffusion (true decoherence, an entropy-increasing arrow) out of a lossless closed lattice.* The
   mode-density increase does not change this — a denser closed bath is still closed.

3. **This is exactly the leaf's own Ax3 line — and it re-frames "diffusion" as "reversible scramble."**
   The leaf's §1 states *"heat = phase disorganization of reactive energy, NOT loss ... it scrambles the
   phase relationship between clocks; the reactive energy is conserved."* The check **confirms that
   framing** — the phase IS scrambled reversibly — while showing the scramble the two tanks actually see
   is dominated by **additive interference** (a reversible, `√u_bath`-amplitude, *bounded* wander), not a
   diffusion *rate* from the clock-rate mechanism. The width of the wander does rise with `u_bath` (so the
   *width-scaling* half of "temperature = width" has support), but **"phase-DIFFUSION (a rate `D ∝
   u_bath`)" is a misnomer for a bounded reversible process**, and the *mechanism* is misattributed.

4. **⚑ FLAG (flag-don't-fix) — where a genuine thermometer would have to come from.** An irreversible,
   unbounded phase-diffusion (a real decoherence *rate*) requires a **dissipative channel** — the
   substrate must actually *lose* coherent phase to an incoherent sink, not just reversibly redistribute
   it. In the AVE engine that is precisely the **unbuilt F6 irreversible `ε → T2` depletion** primitive
   (`engine-capability-map` / memory `project_engine_architecture_qed_gr_replacement`). This check
   therefore reads as **corroborating evidence that the thermal/heat register cannot be closed on the
   lossless kernel alone** — the "temperature = phase-diffusion rate" definition needs the irreversibility
   channel that AVE has not yet built. Surfaced for Grant/auditor adjudication, not resolved here.

5. **Consistency-vs-emergence tag: CONSISTENCY.** No value minted, no CODATA input, no emergence
   headlined. The earnable content is a **mechanism attribution** (the diffusion is additive, not Op14)
   and a **regime characterization** (bounded/reversible under Ax3), not a number.

---

## 6. Leaf-status consequence

**The verdict `ADDITIVE-ARTIFACT` is a NEGATIVE for the registered check → DEMOTE.** Per the frozen
gate (§2/§6 preamble): a positive verdict would have upgraded `thermal-phase-registers.md` §2's
PROPOSED-DEFINITIONAL *"temperature = clock phase-diffusion width"* to measured-consistency; this negative
**keeps it gated and demotes the diffusion (rate) reading.** Precisely, for the leaf on branch
`docs/2026-07-15-walk-batch` (commit `c29e61ed`):

- **§2 "temperature = clock phase-diffusion width" — DEMOTED as a diffusion-*rate* claim.** The two-tank
  check does **not** demonstrate an Op14-mechanism phase-diffusion: the only diffusion present is
  additive wave-interference (kernel-independent), and the isolated Op14 differential phase is bounded.
  The `D ∝ u_bath` calibration the leaf implied is unsupported (`p = 0.38`, and additive-sourced).
- **§1 Ax3 line "heat = reversible phase-scramble, not loss" — CONFIRMED / STRENGTHENED.** The check
  directly exhibits reversible, lossless, bounded phase-scrambling whose width rises with `u_bath`.
- **The refinement the leaf needs:** replace "phase-**diffusion** (rate)" with "**bounded reversible
  phase-scramble** (width `∝ √u_bath`)", and record that a genuine diffusion-*rate* thermometer is gated
  on the **unbuilt F6 irreversibility channel** — not obtainable from the lossless kernel.

> **Lane note (implementer → auditor).** This is the empirical finding + verbatim numbers. The
> **auditor lane lands** the demotion/refinement into `thermal-phase-registers.md` and any
> `COLLABORATION_NOTES` / manuscript queue entry (I surface, I do not edit the tracked leaf). The leaf is
> on `docs/2026-07-15-walk-batch`, not on this branch, so no cross-branch edit is attempted here.
