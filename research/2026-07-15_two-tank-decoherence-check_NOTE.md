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

*PENDING — appended in a separate commit after the frozen production run (hypothesis-first ordering).*

---

## 5. Implications

*PENDING — appended in a separate commit.*

---

## 6. Leaf-status consequence

*PENDING — appended in a separate commit. A **positive** verdict (DIFFUSIVE-LINEAR / -NONLINEAR)
upgrades `thermal-phase-registers.md` §2's PROPOSED-DEFINITIONAL "temperature = clock phase-diffusion
width" to **measured-consistency**; a **negative** (NON-DIFFUSIVE / ADDITIVE-ARTIFACT / CONTROL-FAIL)
**demotes** it (stays gated / walk-level). The consequence sentence is landed by the auditor lane into
the leaf on branch `docs/2026-07-15-walk-batch`.*
