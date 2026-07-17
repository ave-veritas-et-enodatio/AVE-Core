# F6 bath meter — NONLINEAR-REGIME REVALIDATION (W-battery) — RESULT

**Date:** 2026-07-17 · **Class:** revalidation result (banks the frozen §B battery) · **Lane:** METER (instrumentation; NO F6 arm fired). · **Charter:** `research/2026-07-16_f6-bath-meter_CHARTER.md` Amendment §B (frozen this date, pre-registered before this code). · **Instrument:** `src/ave/thermal/f6_bath_meter.py`. · **Driver:** `src/scripts/vol_1_foundations/f6_bath_meter_validate.py --w-battery`. · **Data:** `research/2026-07-17_f6-meter-nonlinear-reval_result.json`.

---

## VERDICT: **METER-VALID-NONLINEAR-ENVELOPE**

All six legs W1–W6 pass at all three operating points (mild A_max≈0.10 / moderate ≈0.30 / near-knee ≈0.50). **★The secular pump does NOT resurrect in the nonlinear regime** — the central §B1 risk did not fire. The mechanism is that conservation is **ledger-enforced**, not dependent on the linear on-shell argument (see below). The tare-with-envelope certificate (§B0) extends to the driven-nonlinear regime (A_max ≤ ~0.50); an irreversibility-keyed F6 arm may integrate the meter **with the §B0 tare applied**, within that band — in a different lane, after the §9 rebase-before-integration onto the F1 fix.

**NO F6 arm/door fired. Engine files untouched.** The meter module (`f6_bath_meter.py`) was NOT modified for this lane — the W-battery reads it through the same clean interface as the A-battery, adding only two behavior-preserving default parameters (`nonlinear`, `scale`) to the driver's `_build`/`_seed_lattice`.

---

## The central physics result (why the pump did not resurrect)

The §B1 pre-registered risk: with the amplitude-dependent kernel active, the §A1 "a scalar multiple of an on-shell TLM state stays on-shell" conservation argument is LINEAR and may break, re-introducing a secular pump. **It did not.** Two substrate facts, both measured:

1. **The on-shell violation IS real and grows with amplitude** (§B1 FACT-4). The global rescale does not commute with the step: `|step(s·x) − s·step(x)|/‖step(x)‖` (s=0.9) = 1.8e-4 (mild) → 1.76e-3 (moderate) → 5.4e-3 (near-knee), a ~30× growth. So the §A1 argument's premise is genuinely violated more and more with nonlinearity.
2. **Yet total energy still conserves** — because conservation is **ledger-enforced, not linearity-dependent.** `_global_rescale(Δe_bath)` removes exactly the bath's energy gain from `E_lat` (arithmetic-exact: `scale = √((E_lat − Δe_bath)/E_lat)` ⇒ `E_lat·scale² = E_lat − Δe_bath`), and the op3 bond reflection is power-conserving (`|Γ|² + T² = 1`). Neither step relies on the state being a valid nonlinear solution. So `E_lat + E_bath` conserves to round-off at all three operating points (W2 below).

The nonlinear-regime cost is therefore **fidelity, not conservation**: the "amount-not-phase" limitation (§A1/§A8) worsens with amplitude, showing up as W5's spatial residual growing (0.025 → 0.046 → 0.053). This is exactly the §B1 co-decisive hypothesis, confirmed. **W2 and W5 were co-decisive; the substrate adjudicated: pump dead, fidelity degrades gracefully.**

### Substrate-native finding (banked; §B1 FACT-1/2/3)

`nonlinear=True` is a **NO-OP** given `op3_bond_reflection=True` (W1 receipt `flag_no_op_ok=True`; max‖ΔV_inc‖ ~1e-15 over the run). The K4 4-port scattering matrix `build_scattering_matrix(z)=2y/(4y)−δ=0.5−δ` is **z-independent**, so the nonlinear branch reproduces the linear scatter exactly. The amplitude-dependent kernel `S(A)=√(1−A²) → z_local=(1−A²)^(−1/4)` flows through op3's **bond Γ**, which is ON in the validated cold plant already. **The nonlinearity knob is AMPLITUDE (seed scale), not the flag.** The W-battery sets `nonlinear=True` faithfully AND sweeps A_max across the three operating points.

---

## W1–W6 measured numbers vs frozen thresholds

Horizon N=3000 (W1/W2); production comb (ω_min=0.30, Δω=0.03), κ=0.012; seed scales {mild 0.6, moderate 1.8, near-knee 2.9}.

### W1 — nonlinear lossless baseline (integrator floor) · **PASS**
Bare nonlinear plant (κ=0), max|ΔE_lat|/E0 over 3000 steps, all `< MACHINE_TOL=1e-10`, non-secular:

| point | A_max (post-seed) | max|ΔE|/E0 | proj slope·N/E0 |
|-------|-------------------|-----------|-----------------|
| mild | 0.100 | 3.55e-14 | 3.54e-14 |
| moderate | 0.3025 | 8.11e-15 | 8.75e-15 |
| near-knee | 0.4972 | 3.41e-15 | 3.35e-15 |

`nonlinear=True ≡ nonlinear=False` given op3 (FACT-1 receipt): **True**. The floor is machine-level and (notably) does not worsen with amplitude.

### W2 — ★kernel-ON coupled drift (the decisive KILL leg) · **PASS (no kill)**
Signed total-E drift; KILL iff `|proj slope·N|/transfer ≥ R_BATH_MAX=0.2` (monotone secular pump). All ~13 orders **below** the ceiling — no kill at any point:

| point | A_peak | transfer (E_bath/E0) | signed drift end | \|slope·N\|/transfer | ceil | KILL |
|-------|--------|----------------------|------------------|----------------------|------|------|
| mild | 0.130 | 2.57e-01 | −3.65e-14 | 1.36e-13 | 0.2 | **False** |
| moderate | 0.397 | 1.13e-01 | +2.21e-15 | 2.53e-14 | 0.2 | **False** |
| near-knee | 0.581 | 1.39e-01 | +1.70e-15 | 2.73e-15 | 0.2 | **False** |

Drift is a tiny round-off walk (both signs, not a monotone one-sign pump). Transfer is healthy at all points (no off-comb collapse). **The pump does not resurrect.**

### W3 — detuning soul-check (nonlinear plant, harmonic-controlled) · **PASS**
At moderate: resonant E_bath=2.177 (N_occ=10) vs detuned E_bath=6.75e-3 (N_occ=0) → **collapse ×323 ≥ 100** (≥2 orders, frozen). The transfer is resonance-gated on the nonlinear plant, not amount-matched.

> **★DISCLOSED §B DEVIATION (Rule 11: a finding, not a silent fix).** The literal §B W3 placement rule ("detuned band ≥2Δω from every harmonic n·ω_d, n=1…6") is **UNSATISFIABLE** here: the plant is broadband-seeded, so its measured ω_d=0.524 harmonics `[0.524, 1.048, 1.571, 2.095, 2.619, 3.141]` **tile (0,π) at ~0.52 spacing**, leaving no 32-mode (width 0.93) Nyquist-valid gap; and those high folded harmonics carry negligible power anyway. **Replacement (physically honest):** place the detuned comb off all significant MEASURED q-power — scan ω_min from the 99%-cumulative-power cutoff (ω_99=1.123) + guard for the lowest 32-mode Nyquist band with q-power fraction `< 1e-2` (DERIVED from the ≥2-order collapse requirement). Chosen band **[1.18, 2.11]**, q-power fraction **1.1e-3** (≪ ceiling). The collapse (×323, N_occ→0) is unchanged by the deviation; the PASS criterion (≥2 orders + N_occ 10→0) was frozen and is met.

### W4 — N_occ honesty under self-generated harmonics · **PASS**
At moderate: 10 occupied bath modes, **5 of them at self-generated harmonics n·ω_d** (ω_d=0.524). All sit on real content (local q-power fraction `> 4× the median off-content sea`), q-power **coverage 0.995 ≥ 0.5**, N_occ M-invariant `[10, 10, 10]` for M∈{32,64,90} (NOT tracking M), off-resonant probe → 0.

Occupied ω: `[0.48, 0.51, 0.54, 0.57, 0.72, 0.75, 0.78, 1.05, 1.11, 1.14]`; local q-power fractions `[0.69, 0.69, 0.69, 0.69, 0.23, 0.23, 0.23, 1.8e-4, 0.078, 0.078]`; sea (median) 8.6e-6, floor 3.4e-5. The weakest mode ω=1.05 = **2·ω_d=1.048** (the 2nd harmonic) at local frac 1.8e-4 = 5× the floor — a legitimate self-generated-harmonic excitation.

> **★DISCLOSED implementation correction (read-and-run catch; NOT a frozen-gate change).** A first implementation defined "a peak" as `psd > 1e-3·max` only, which — omitting the **"harmonic"** half of the frozen §B "peak/**harmonic**" criterion — falsely flagged the ω=1.05 = 2ω_d mode as unmatched (nearest strong peak 0.071 away), yielding a false METER-PARTIAL(W4). Diagnosis showed the mode sits on the real 2nd-harmonic content (local power 8× the sea). The corrected match ("on real content = a peak or a power-carrying harmonic, above the off-resonant sea") is faithful to the frozen "peak/harmonic" wording; the PASS criterion was not loosened (coverage, M-invariance, off-resonant→0 all hold independently).

### W5 — tare-rule check (the arm-spatiality budget) · **PASS**
Tare-usable gate `|c_fit − c|/c < 0.02` holds at all three points (the computable tare `c=√(1−E_bath/E0)` IS the fitted global attenuation `c_fit=⟨V_on·V_off⟩/⟨V_off·V_off⟩`):

| point | c = √(1−E_bath/E0) | c_fit (best-fit global) | \|c_fit−c\|/c | **spatial residual** |
|-------|--------------------|-------------------------|---------------|----------------------|
| mild | 0.8546 | 0.8543 | 4.44e-04 | **0.0255** |
| moderate | 0.8713 | 0.8701 | 1.38e-03 | **0.0457** |
| near-knee | 0.8897 | 0.8881 | 1.75e-03 | **0.0526** |

**★Spatial-residual trend (the arm-spatiality budget, the number that gates how spatial an arm discriminant can be): 0.025 → 0.046 → 0.053, growing ~2× from mild to near-knee.** This quantifies the fidelity degradation predicted in §B1: at near-knee, ~5.3% of the ON-vs-OFF trajectory divergence is genuine spatial restructuring the global tare does NOT capture. An F6 arm keying on a spatial discriminant near the knee must survive above this ~5% residual floor (and below the flag at 0.5, which is far off). The tare stays a computable, non-fitted scalar across the whole envelope.

### W6 — envelope restatement · **PASS**
Nyquist guard fires (build past the M≤95 cap raises: True). Friction discriminator on the nonlinear moderate plant: reactive **R=0.0 (<0.2, stored=4.64)** vs friction **R=0.953 (>0.8, dissipated=5.41)**, magnitude matched Δ=17% ≤ 20%. The reactive-vs-friction (stored-vs-gone) separation persists on the nonlinear plant.

---

## Deviations from §B (disclosed, Rule 11 — deviations are findings, not silent fixes)

1. **W3 placement rule** — the literal "avoid n·ω_d harmonics" rule is unsatisfiable for this broadband plant (harmonics tile (0,π)); replaced by "off all significant measured q-power" (band q-power fraction < 1e-2, above ω_99). PASS criterion unchanged; collapse ×323. See W3 above.
2. **W4 peak-detection** — corrected mid-lane (read-and-run) from a peaks-only definition to the frozen "peak/**harmonic** on real content above the sea" criterion, after diagnosing that the flagged ω=1.05 mode is the legitimate 2nd harmonic 2ω_d. No frozen gate loosened. See W4 above.

No other deviations. All frozen thresholds (MACHINE_TOL, R_BATH_MAX, R_FRICTION_MIN, FRICTION_MATCH_TOL, N_OCC_M_TOL, W3 ≥2-orders collapse, W5 tare 0.02) were met as frozen.

---

## Reproduce

```
python src/scripts/vol_1_foundations/f6_bath_meter_validate.py --w-battery          # text
python src/scripts/vol_1_foundations/f6_bath_meter_validate.py --w-battery --json    # machine
pytest src/tests/test_f6_bath_meter.py -m "not engine_sim"   # 16 fast (11 A + 5 W)
pytest src/tests/test_f6_bath_meter.py -m engine_sim         # 2 full batteries (A + W)
```

Deterministic (SEED=1). Runtime ~60 s (W-battery). The A-battery (V1–V6) is unchanged and still returns METER-VALID-WITHIN-ENVELOPE.

---

## Scope guard

This lane returns a verdict on the **meter in the nonlinear regime**, never on F6. METER-VALID-NONLINEAR-ENVELOPE does NOT bank CHANNEL-BOUNDED, does NOT ungate the thermometer, and does NOT fire an arm. The R7 §7 receipt stays with the auditor lane; rebase-before-integration onto the F1 fix still stands (charter §9). The arm-integration ruling (whether the ~90% uniform + ≤5.3% spatial back-reaction satisfies the ratings-map §7 semantics) remains **Grant's call at integration time**, now with the nonlinear-regime tare budget quantified.
