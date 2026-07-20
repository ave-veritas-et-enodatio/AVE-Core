# ℏ-as-FD — derived FD-ratio(ρ) on the certified F6 junction — DERIVATION (FROZEN)

**Date:** 2026-07-20 · **Class:** derivation (freeze-by-push; the FORM + frozen decision bins + tolerance are frozen by the push of THIS file, BEFORE the comparison driver code exists). · **Lane:** ℏ-as-FD (the fluctuation-dissipation frame on the F6 junction; the program's data-ahead-of-theory spearhead).
**Attribution:** lane fired by Grant 2026-07-20 (verbatim `[sic]`): *"lets launch the planks constant as FD"*. Everything below the ruling line is **execution wording** (tagged), not Grant's derivation.
**Consumes (banked, byte-untouched):** the FENCED FD leg of `research/2026-07-19_f6-thermal-floor-arm_result.md` §5 (`…_result.json` `fd_leg`), the STAGE-1 floor-battery config `research/2026-07-19_f6-floor-battery_result.md` §D, the seeding math `seed_floor` (`src/scripts/vol_1_foundations/f6_floor_battery.py:79`), the certified port `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler`, **BYTE-UNTOUCHED**).
**Certificate:** FLOOR-METER-VALID-BAND[0,5] (STAGE-1); the certified scalar-port junction at κ=0.030 MILD, standalone-K4.

---

## 0 · Sector / regime header (mandatory, first)

- **Sector:** R7 thermal / entropy-sink (F6 ε→T2 candidate). **NOT** A1 dilatation-mass, **NOT** Cosserat (2,3) winding/charge.
  - **The FLOOR (fluctuation side)** is carried by the **T2 sink DOF** — the modal oscillator bath (`OscillatorBath`, per-mode LC tanks), pre-occupied with frozen random phases.
  - **The RESPONSE (dissipation side)** is the **certified scalar collective-coordinate port** — `LatticeBathCoupler` couples the collar voltage `q` to the bath via `ṗ_m += κ g_m q` and returns AMOUNT via a global phase-blind amplitude rescale (`f6_bath_meter.py:292` `_global_rescale`).
- **Regime:** Regime I sub-yield, `A_max≈0.10` MILD, at the certified `κ=0.030`; driven-then-source-off; closed cavity (pml=0). **Cold plant** (the meter's lattice is linear; no Op14 saturation). The floor is a **classically-seeded** ensemble (see §1).
- **Instrument-class scope (phased-array ruling):** this derivation speaks for the **certified scalar-port FD junction** only. The port is a scalar collective coordinate + a global, spatially-uniform, phase-blind rescale (the B2 barrier, `f6_bath_meter.py:198` κ·g degeneracy, arm result §0 B2-SHARPENING). Results are **instrument-class-scoped**; they do not generalize to a phase-resolving or a multi-port junction.
- **Coordinate discipline (A46):** the fluctuation is read in the bath's own **scalar energy ledger** (the excess `ΔE_bath`, §D.D2) and its seed-ensemble spread — matching the FD-ratio's own coordinate. NOT a real-space φ² surrogate.
- **Classical-vs-quantum honesty (stated up front):** the certified engine is a **classical** lattice and the banked floor is a **classically-seeded** ensemble (equipartition-per-mode, §1). The **classical FD relation** is what this junction can express. The **quantum-FD `coth` form is DERIVED-FOR-COMPARISON only** (§4) — it is explicitly tagged imported-for-comparison, never asserted from a classical run. No ℏ is manufactured from a classical ensemble.

**★THE RULING / the lane (Grant verbatim, `[sic]`):** *"lets launch the planks constant as FD"* — read (execution wording, tagged): put the certified F6 junction into the fluctuation-dissipation frame and ask what, if anything, an action quantum can be on it. The DISSIPATION side is the certified meter transfer response (Op3 lossless transduction, RULING-21 — *"mode loss ≠ system loss, its transduction"* [sic]); the FLUCTUATION side is the pre-occupied noise floor (Grant's static-floor ruling; the Johnson-Nyquist canon row `manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md`).

---

## 1 · The floor's spectral density — first principles from `seed_floor` (the FLUCTUATION side)

`seed_floor` (`f6_floor_battery.py:79`, config-only, meter byte-untouched) seeds each bath mode `m`:

```
θ_m ~ Uniform(0, 2π)   (frozen per seed)
amp = √(2 · e_floor_per_mode),   e_floor_per_mode = ρ · e_sig
x_m = (amp / ω_m) · cos θ_m
p_m = amp · sin θ_m
```

- **Per-mode energy is EXACT (no energy variance):** `E_m = ½ p_m² + ½ ω_m² x_m² = ½ amp² = e_floor_per_mode = ρ·e_sig` for every mode, every seed. This is a **microcanonical-per-mode EQUIPARTITION floor** (every mode gets EXACTLY the same energy `ρ·e_sig`; only the phases are random) — the classical **Rayleigh-Jeans / Johnson-Nyquist** floor with a `k_B T`-analog `k_B T ≡ ρ·e_sig`.
- **Quadrature split (Johnson-Nyquist equipartition), DERIVED:** over the phase ensemble the C-state (capacitor, `½ω²x²`) and L-state (inductor, `½p²`) each carry HALF the floor energy:
  `⟨½ω_m² x_m²⟩_θ = e_floor·⟨cos²θ⟩ = ½ e_floor`; `⟨½p_m²⟩_θ = e_floor·⟨sin²θ⟩ = ½ e_floor`.
  Each quadrature = ½·(energy-per-mode) — the classical ½·k_B T per quadrature. **This is the Rule-10 reactance pair at the floor level.**
- **The injected fluctuation amplitude scales as √ρ (the amplitude law), DERIVED:** any linear functional of the seeded floor `L = Σ_m (a_m x_m + b_m p_m)` (e.g. the collar drive-back `q ~ Σ g x_m`) has, over the phase ensemble, `Var(L) = ½ amp² Σ(a_m²/ω_m² + b_m²) ∝ amp² = 2ρ·e_sig`, so `std(L) ∝ √(ρ·e_sig) = √ρ · √e_sig`. The **fluctuation AMPLITUDE ∝ √ρ** is FORCED — the exponent ½ is the equipartition-floor's √(energy) law, no free parameter.

**Consequence for the banked fluctuation proxy.** The banked FD numerator is `fluct = std_seed(R_rev)/√6` (`f6_thermal_floor_arm.py:338`). `R_rev` is a fractional excess-return; its seed-to-seed spread is a **floor×signal beat** — the random floor (amplitude √ρ) interfering with the coherent signal (amplitude √e_sig) in the coupled excess ledger. To leading order the beat inherits the floor amplitude: **`std(R_rev) ∝ √ρ`** (the amplitude law propagates linearly through the coupling). Sub-leading: `R_rev` is normalized by the excess plateau `ΔE_bath(t_fp)`, which itself grows mildly with ρ (excess-plateau 0.193→0.311 over the band, arm §2) — a normalization **droop** that makes `std(R_rev)` grow slightly SLOWER than √ρ at high ρ. The droop is a disclosed sub-leading correction, NOT a tuned parameter.

---

## 2 · The transductive response — the DISSIPATION side (engine-read, certified)

The FD denominator is `relax = t_fp / T_rec` (`f6_thermal_floor_arm.py:336`), `T_rec = 2π/Δω`: the first-plateau time (excess reaching 1−1/e of its plateau) in recurrence units. This is the **certified meter transfer response** — the port's transductive admittance turning collar drive into bath excess. It is set by the coupling `κ=0.030` and the comb (`Δω=0.050`), **floor-level-independent at leading order** (the coupling rate does not depend on how much the floor is pre-charged). It is an **ENGINE READ** of the certified junction (allowed; tagged engine-read, not fitted, not free).

- **Construction wrinkle (flag, do not fix — the driver is banked/frozen):** `relax` is read from **seed-0 only** (`c0 = primary[rho][0]`, `f6_thermal_floor_arm.py:334`), while the numerator uses the **full 6-seed** std. A single-seed denominator paired with an ensemble numerator is an asymmetry in the banked construction. It does not change the leading SHAPE conclusion (the plateau timing is nearly seed-independent), but it is disclosed.

---

## 3 · The DERIVED FD-ratio form + the FORCED dimensionless content (the freeze)

**The derived form (FROZEN, committed before overlay):**

> **FD-ratio(ρ) = k · √ρ / relax(ρ)**
>
> - **√ρ** — the FLUCTUATION side, **FORCED** by the equipartition-floor amplitude law (§1). Exponent ½, zero free parameters.
> - **relax(ρ)** — the DISSIPATION side, the certified transductive response, **engine-read** (§2), tagged.
> - **k** — a SINGLE calibration prefactor (VALUE), TAGGED calibration, anchored at the natural reference point **ρ=1 (floor=signal)**. It absorbs `√e_sig`, `κ`, the comb, and the `1/√6` ensemble factor — all ENGINEERING CHOICES.

**The FORCED dimensionless content (what "counts" per the α-circularity lesson):**

1. **The exponent ½** (the √ρ amplitude law) — forced, dimensionless.
2. **The quadrature split ½:½** (C-state:L-state at the floor) — forced, dimensionless.
3. **The ρ→0 intercept = 0** — forced by the classical (no-zero-point) seeding.

**★ FORM/VALUE + chord ruling (frozen, stated before overlay):** all three forced dimensionless items are the **universal classical-FD / Johnson-Nyquist equipartition signature** — SM stat-mech forces the identical √(k_BT) amplitude law and ½ equipartition. They are therefore **CONSISTENCY-class (peer-with-stat-mech), NOT an AVE-distinct chord.** The **absolute magnitude** (the 0.129 saturation value) is **NOT a forced dimensionless number**: the banked proxy is a **SEM** (`std/√6`), so the absolute FD-ratio scales as `1/√N_seeds` → it is calibration + ensemble-size-dependent, not physical FD-forced (a physical FD fluctuation amplitude uses `std`, not `std/√N`). **No chord candidate is expected in this leg.** (If the overlay nonetheless surfaces a retune-free forced dimensionless match, it is flagged loudly and routed to Grant — not self-promoted.)

---

## 4 · The zero-point (ℏ) discriminator — DERIVED (imported-for-comparison, tagged)

The current floor is **classical**: energy-per-mode `= ρ·e_sig`, **flat in ω**, and `→0` as `ρ→0`. A **quantum** floor would carry a surviving zero-point term. The quantum-FD occupation (imported-for-comparison, `manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md`; NOT asserted from this classical run):

> `E_m(T) = (ℏω_m/2) · coth(ℏω_m / 2k_B T)` — classical limit (`k_BT ≫ ℏω`) `→ k_BT` (flat, ∝ρ); zero-T limit `→ ℏω_m/2` (the zero-point, ∝ω).

**Two DERIVED dimensionless discriminators this instrument would use to detect ℏ:**

- **D1 — the ρ→0 INTERCEPT of the fluctuation amplitude.** Classical: `0` (no surviving floor). Quantum/zero-point: `√(E_zp/e_sig) > 0` (a finite intercept as the thermal part → 0). **The current classical seeding forces intercept = 0** (`seed_floor` is a NO-OP at ρ=0). A quantum-seeded run would seed `E_m = ½ℏω_m + ρe_sig` and the FD-ratio would extrapolate to a NONZERO intercept.
- **D2 — the ω-DEPENDENCE of energy-per-mode.** Classical equipartition: **flat in ω** (top/bottom-mode energy ratio `= 1`). Quantum zero-point: `∝ ω` (ratio `= ω_max/ω_min`). On the primary comb (`ω ∈ [0.30, 1.00]`, M=15) the quantum ratio would be **3.333** vs the classical **1.000** — a large, cleanly measurable dimensionless signature.

**Honest map of what THIS instrument's FD data can and cannot say about ℏ:** it can measure the **classical** FD relation (the √ρ amplitude law, §3) and it **DEFINES** the two dimensionless zero-point discriminators (D1 intercept, D2 ω-slope) — but it **CANNOT reach ℏ**: the classical seeding carries no zero-point term by construction (intercept ≡ 0, ω-slope ≡ 0). Reaching ℏ requires a **quantum-seeded floor** (a config change: `E_m = ½ℏω_m·coth(...)` instead of the flat `ρe_sig`) — a routed SPEC, not built here (and note the B2 phase-blind port may not even transduce the ω-structure; a separate open).

---

## 5 · Frozen decision bins + FROZEN tolerance (committed before overlay)

**Frozen tolerance (principled, not tuned-to-pass):** each banked FD point carries the intrinsic uncertainty of a standard-deviation estimated from N=6 seeds, `σ_point = fd_ratio · 1/√(2(N−1)) = fd_ratio · 0.316` (32% relative). The forced form uses a SINGLE calibration anchor (k at ρ=1); the other four nonzero ρ are genuine predictions.

- **FORM-MATCH (consistency-class):** the forced `FD = k·√ρ/relax` (k anchored at ρ=1) lands within **1.5·σ_point** (≈47% relative) of every banked FD point at ρ ∈ {0.3, 1, 2, 3, 5}, with the √ρ exponent NOT retuned. Params (k, and the engine-read relax) are calibration/engine-read-tagged. This is the expected verdict.
- **CHORD-CANDIDATE:** a dimensionless number FORCED by the derivation (not calibration, not N-dependent) matches the data with **no retune**. Pre-identified as **expected-EMPTY** (§3 — the forced content is universal classical-FD, not AVE-distinct; the absolute 0.129 is N-dependent). If surfaced anyway: flag LOUDLY, do NOT self-promote past consistency-class, route to Grant.
- **FORM-MISMATCH (bank the negative):** the shape is wrong — the √ρ exponent is excluded (a different exponent, or non-monotone) beyond 1.5·σ_point at ≥2 of the 5 points. The classical-FD framing fails on this instrument; close honestly.
- **UNDETERMINED (surface the fork, fail closed):** an **unforced modeling choice** controls the shape — e.g. if the single-seed `t_fp` denominator (§2 wrinkle) or the plateau-normalization droop (§1) dominates the ρ-dependence such that the forced √ρ numerator is NOT the load-bearing driver. Then the leg cannot adjudicate the FD form; surface both file paths, fail closed.

**Fireability check (frozen):** a linear-in-ρ numerator (exponent 1, not ½) would predict FD(ρ=5) ≈ √5× the ½-form ≈ 0.33 vs the banked 0.129 → +150%, far outside 1.5·σ_point at ρ∈{3,5}. A ρ-independent (flat) numerator fails the monotone rise. The bin is genuinely fireable.

---

## 6 · Scope fences + connections (pointer-class only)

- **NOT re-opened:** the arm's §4 verdict (the STRONG FLOOR-ARROW is excluded ~5σ + structurally inexpressible). This lane derives the FD FORM for the **fenced, non-gating** FD leg only; it mints nothing at the arrow rung and nothing at emergence-class.
- **Connections (pointers, not claims):** the Johnson-Nyquist canon row (`…/nyquist-noise-fdt.md`); RULING-21 lossless transduction (the certified dissipation-side meter, `…/photon-identification.md:47`); the entropy-definition equilibrium note and the dark-energy latent-heat T2-sink row (the floor's home sector) — pointer-class only.
- **Discipline:** engine + meter BYTE-UNTOUCHED (research driver only; banked configs reused, content-verified against §D). Every constant derived, engine-read, or calibration-TAGGED. Freeze-by-push: THIS derivation (form + bins + tolerance) is pushed BEFORE the comparison driver; the overlay + frozen-bin verdict land in the companion result (`2026-07-20_hbar-as-fd_result.md`) with the margin stated.
