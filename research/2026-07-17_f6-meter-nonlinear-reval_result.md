# F6 bath meter — NONLINEAR-REGIME REVALIDATION (W-battery) — RESULT

**Date:** 2026-07-17 · **Class:** revalidation result (banks the frozen §B battery) · **Lane:** METER (instrumentation; NO F6 arm fired). · **Charter:** `research/2026-07-16_f6-bath-meter_CHARTER.md` Amendment §B (frozen this date, pre-registered before this code). · **Instrument:** `src/ave/thermal/f6_bath_meter.py`. · **Driver:** `src/scripts/vol_1_foundations/f6_bath_meter_validate.py --w-battery`. · **Data:** `research/2026-07-17_f6-meter-nonlinear-reval_result.json`.

---

## VERDICT: **METER-VALID-NONLINEAR-ENVELOPE** (scoped — see caveat)

All six legs W1–W6 pass at all three operating points (mild A_max≈0.10 / moderate ≈0.30 / near-knee ≈0.50). The verdict **STANDS** per the frozen §B3 (all W1–W6 pass at all three points; the battery reproduces bit-for-bit). The secular pump does not resurrect in the nonlinear regime — but the honest mechanism is stronger and narrower than the §B1 pre-reg framed: **conservation is IDENTITY-ENFORCED on this plant class, not empirically survived** (see "The central physics result" and the §B-post-review addendum R-1). The tare-with-envelope certificate (§B0) extends to the driven-nonlinear regime (A_max ≤ ~0.50); an irreversibility-keyed F6 arm may integrate the meter **with the §B0 tare applied**, within that band — in a different lane, after the §9 rebase-before-integration onto the F1 fix.

> **★SCOPE CAVEAT (R-1, PR #721 review — load-bearing).** This certificate is scoped to **STANDALONE-K4 plants**. On this plant class energy conservation is an **algebraic identity** (z-independent equal-admittance 4-port scatter `S=0.5−δ` orthogonal; bond connect `[[γ,T],[T,−γ]]` orthogonal at any γ; global rescale arithmetic-exact on the quadratic energy), so pump-immunity was **structurally guaranteed, not empirically discovered** — and the S(A)-kernel-in-scatter pump path the §B1 risk feared is **INEXPRESSIBLE on this junction**. A **CoupledK4Cosserat arm** (a Cosserat-owned z front, Cosserat↔V exchange outside the meter's `E_lat` ledger) or **ANY genuine irreversible ε→T2 depletion primitive** BREAKS the identity ⇒ the **W-battery must be RE-VALIDATED** before such an arm integrates the meter (not merely the §9 V1–V6 re-run). **Alignment note:** the door charter's **CHANNEL-BOUNDED** bin is *defined* energy-conserving, so identity-enforced conservation is **consistent with** (not a blocker for) the arm's counting-arrow design — the caveat is about which plant the certificate covers, not about the arm's target.

**NO F6 arm/door fired. Engine files untouched.** The meter module (`f6_bath_meter.py`) was NOT modified for this lane — the W-battery reads it through the same clean interface as the A-battery, adding only two behavior-preserving default parameters (`nonlinear`, `scale`) to the driver's `_build`/`_seed_lattice`.

---

## The central physics result (why the pump could not resurrect — identity, not luck)

The §B1 pre-registered risk: with the amplitude-dependent kernel active, the §A1 "a scalar multiple of an on-shell TLM state stays on-shell" conservation argument is LINEAR and may break, re-introducing a secular pump. **It did not — and, post-review, we can say why more sharply than the pre-reg's "co-decisive substrate adjudication" framing (R-1 supersedes that reading):**

1. **The on-shell violation IS real and grows with amplitude** (§B1 FACT-4). The global rescale does not commute with the step: `‖step(s·x) − s·step(x)‖/‖step(x)‖` (s=0.9) grows ~28× across the operating band. **⚠ The §B1 charter triple `1.8e-4 / 1.76e-3 / 5.4e-3` was scratch-provenance — not reproducible from shipped code (all natural readings are ~3–4× smaller).** The banked reproduction (opt-in `--fact4`; method = the on-shell `(V_inc,V_ref)` state the rescale actually acts on) is **`4.74e-5 (mild) → 4.52e-4 (moderate) → 1.32e-3 (near-knee)`, 27.8× growth** — same order and trend as the reviewer's independent `4.3e-5 → 1.2e-3` (~28×). The charter §B body is NOT edited (frozen); both are stated in the §B-post-review addendum R-3, and the reproduced triple is banked in the result JSON addendum. The qualitative claim (the §A1 linearity premise is genuinely violated, more so with amplitude) survives; the specific numbers are the reproduced ones.
2. **Yet total energy conserves as an ALGEBRAIC IDENTITY — not because the pump was empirically survived.** On this STANDALONE-K4 plant every operation in the loop is orthogonal or arithmetic-exact on the quadratic energy: the z-independent equal-admittance 4-port scatter `S=0.5−δ` is orthogonal, the bond connect `[[γ,T],[T,−γ]]` is orthogonal at any γ, and `_global_rescale(Δe_bath)` removes exactly the bath's gain (`scale=√((E_lat−Δe_bath)/E_lat)` ⇒ `E_lat·scale²=E_lat−Δe_bath`, arithmetic-exact). So `E_lat+E_bath` conserves to round-off **independent of amplitude** — the S(A)-kernel-in-scatter pump path is **inexpressible on this junction** (verified: the global rescale is arithmetic-exact even as the step non-commutation grows). **Pump-immunity was structurally guaranteed, not a substrate adjudication that could have gone either way** — see the §B-post-review addendum R-1 and the ★SCOPE CAVEAT above.

Because conservation is an identity here, **W2 is not the "decisive kill leg" the §B1 pre-reg framed** (relabelled: *ledger-regression + transfer-health leg* — see W2 below). The genuinely informative content of this lane is **W5's spatial-residual trend** (0.025 → 0.046 → 0.053): the "amount-not-phase" limitation (§A1/§A8) worsens with amplitude, and that residual is the arm's spatial-discriminant budget. The nonlinear-regime cost is **fidelity, not conservation** — fidelity degrades gracefully; conservation was never at risk on this plant.

### Substrate-native finding (banked; §B1 FACT-1/2/3)

`nonlinear=True` is a **NO-OP UNCONDITIONALLY in `K4Lattice3D`** (R-2 strengthening, PR #721 review). The W1 receipt (`flag_no_op_ok=True`; max‖ΔV_inc‖ ~1e-15 over the run) shows the no-op *given* `op3_bond_reflection=True`; the reviewer's independent op3-**OFF** twin was bit-identical too (`7.8e-16`; our reproduction `2.8e-16`) — **z-independence kills the branch everywhere, not just under op3.** The K4 4-port scattering matrix `build_scattering_matrix(z)=2y/(4y)−δ=0.5−δ` is **z-independent**, so the nonlinear branch reproduces the linear scatter exactly regardless of op3. The amplitude-dependent kernel `S(A)=√(1−A²) → z_local=(1−A²)^(−1/4)` flows through op3's **bond Γ**, which is ON in every plant here. **The nonlinearity knob is AMPLITUDE (seed scale), not the flag.** The W-battery sets `nonlinear=True` faithfully AND sweeps A_max across the three operating points.

> **⚠ LATENT DOUBLE-INTEGRATION HAZARD (R-2; flagged for the engine lane — NOT triggered here).** If `op3_bond_reflection` **and** `nonlinear` **and** `use_memristive_saturation` are ever ALL on simultaneously, `_scatter_all` advances `S_field` **twice per step**: once in the op3 branch (`_update_z_local_field → _integrate_s_field_from_v`, backward-Euler substep) and again in the `nonlinear` branch (a second backward-Euler substep). This lane is safe because `use_memristive_saturation=False` (out of scope, §B1); but any lane that turns memristive saturation on with both other flags will double-integrate the Op14 relaxation. Owed to the engine lane (see Routed flags).

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

### W2 — kernel-ON coupled drift (LEDGER-REGRESSION + TRANSFER-HEALTH leg) · **PASS**
> **★RELABEL (R-1, PR #721 review — supersedes the "decisive KILL leg" heading).** On this STANDALONE-K4 plant class, conservation is **identity-enforced** (orthogonal scatter/connect + arithmetic-exact rescale), so pump-immunity was **structurally guaranteed**, not empirically survived — W2 is **not** a decisive kill leg. Its remaining, genuine content is: **(a)** a **regression guard** against #717-class ledger bugs; **(b)** **transfer health** (E_bath stays healthy — no off-comb collapse); **(c)** the **dormant `max(·,0)` clamp path** stays dormant.

Signed total-E drift; the frozen KILL gate `|proj slope·N|/transfer ≥ R_BATH_MAX=0.2` is retained as the regression tripwire. All ~13 orders **below** the ceiling — no kill at any point:

| point | A_peak | transfer (E_bath/E0) | signed drift end | \|slope·N\|/transfer | ceil | KILL |
|-------|--------|----------------------|------------------|----------------------|------|------|
| mild | 0.130 | 2.57e-01 | −3.65e-14 | 1.36e-13 | 0.2 | **False** |
| moderate | 0.397 | 1.13e-01 | +2.21e-15 | 2.53e-14 | 0.2 | **False** |
| near-knee | 0.581 | 1.39e-01 | +1.70e-15 | 2.73e-15 | 0.2 | **False** |

Drift is a tiny round-off walk (both signs, not a monotone one-sign pump). **(a) Ledger-regression content (verified):** the *global* (both-field) rescale is arithmetic-exact (realized ΔE = target to machine precision); a **single-field** (V_inc-only) rescale — a #717-class ledger bug — **breaks the conservation identity** (the reviewer measured a **10.5%** energy jump; an independent reproduction at these operating points measured a smaller ~0.2% per-step discontinuity — *direction confirmed, magnitude regime/measurement-dependent; flagged, not silently adopted*). **(b) Transfer health:** E_bath/E0 ∈ [0.11, 0.26] at all points — healthy, well above `E_BATH_MIN`. **(c) Clamp margin:** `max(Δe_bath/e_lat)` over 3000 steps ≈ **5.1e-3** (reviewer ~3.9e-3; same order), far below the `1.0` where the `max(·,0)` clamp would truncate the ledger — the clamp is never triggered. **The pump could not resurrect (identity), and the ledger regressions are all clean.**

### W3 — detuning soul-check (nonlinear plant, harmonic-controlled) · **PASS**
At moderate: resonant E_bath=2.177 (N_occ=10) vs detuned E_bath=6.75e-3 (N_occ=0) → **collapse ×323 ≥ 100** (≥2 orders, frozen). The transfer is resonance-gated on the nonlinear plant, not amount-matched.

> **★DISCLOSED §B DEVIATION (Rule 11: a finding, not a silent fix).** The literal §B W3 placement rule ("detuned band ≥2Δω from every harmonic n·ω_d, n=1…6") is **UNSATISFIABLE** here: the plant is broadband-seeded, so its measured ω_d=0.524 harmonics `[0.524, 1.048, 1.571, 2.095, 2.619, 3.141]` **tile (0,π) at ~0.52 spacing**, leaving no 32-mode (width 0.93) Nyquist-valid gap; and those high folded harmonics carry negligible power anyway. **Replacement (physically honest):** place the detuned comb off all significant MEASURED q-power — scan ω_min from the 99%-cumulative-power cutoff (ω_99=1.123) + guard for the lowest 32-mode Nyquist band with q-power fraction `< 1e-2` (DERIVED from the ≥2-order collapse requirement). Chosen band **[1.18, 2.11]**, q-power fraction **1.1e-3** (≪ ceiling). The collapse (×323, N_occ→0) is unchanged by the deviation; the PASS criterion (≥2 orders + N_occ 10→0) was frozen and is met.
>
> **★PLAIN STATEMENT (R-6, PR #721 review — say it, don't make the reader infer it).** The chosen detuned band **[1.18, 2.11] CONTAINS two harmonics the frozen rule ordered avoided: n=3 (1.571) and n=4 (2.095).** This is stated plainly so the reader sees the containment directly. The placement is honest **on the power budget**: those contained harmonics carry negligible *measured* power (band q-power fraction 1.1e-3 < the 1e-2 ceiling), so a harmonic that carries negligible measured power cannot re-excite the bath past the ≥2-order collapse budget — which is exactly what the ×323 collapse (N_occ 10→0) demonstrates. The **PASS criterion was untouched** (still ≥2 orders + N_occ 10→0); only the *placement* deviated from the literal harmonic-avoidance text, and the deviation is disclosed rather than hidden behind "off all significant measured q-power".

### W4 — N_occ honesty under self-generated harmonics · **PASS**
At moderate: 10 occupied bath modes, **5 of them at self-generated harmonics n·ω_d** (ω_d=0.524). All sit on real content (local q-power fraction `> 4× the median off-content sea`), q-power **coverage 0.995 ≥ 0.5**, N_occ M-invariant `[10, 10, 10]` for M∈{32,64,90} (NOT tracking M), off-resonant probe → 0.

Occupied ω: `[0.48, 0.51, 0.54, 0.57, 0.72, 0.75, 0.78, 1.05, 1.11, 1.14]`; local q-power fractions `[0.69, 0.69, 0.69, 0.69, 0.23, 0.23, 0.23, 1.8e-4, 0.078, 0.078]`; sea (median) 8.6e-6, floor 3.4e-5. The weakest mode ω=1.05 = **2·ω_d=1.048** (the 2nd harmonic) at local frac 1.8e-4 = 5× the floor — a legitimate self-generated-harmonic excitation.

> **★DISCLOSED IMPLEMENTATION DEVIATION (R-5, PR #721 review — a THIRD operationalization).** The **shipped** W4 honesty gate is **`local band-power > 4× median-sea`**, which is a *third* operationalization — neither the frozen §B W4 proximity text ("every occupied mode lies within `2Δω` of a peak/harmonic of the measured V-spectrum") nor the earlier peaks-only definition it corrected (§B W4 disclosure). **Mitigation banked (reviewer-verified + independently reproduced):** all **10** occupied modes ALSO pass the **strict frozen** criterion — every one is within `2Δω=0.06` of a measured peak OR a harmonic (reproduced: nearest-peak/harmonic Δ ∈ [0.002, 0.057]; the weakest, ω=1.05, matches **2·ω_d** at Δ=**0.0025**), and the off-resonant / white-noise probe fires honestly (detuned comb → N_occ=0). So the deviation does not change the verdict here. **⚠ Future-plant divergence risk:** on a *different* plant the two operationalizations (band-power-vs-sea vs. proximity-to-a-peak) **can disagree** — reconcile the two before reusing this gate on any new plant (flagged).

> **★DISCLOSED implementation correction (read-and-run catch; NOT a frozen-gate change).** A first implementation defined "a peak" as `psd > 1e-3·max` only, which — omitting the **"harmonic"** half of the frozen §B "peak/**harmonic**" criterion — falsely flagged the ω=1.05 = 2ω_d mode as unmatched (nearest strong peak 0.071 away), yielding a false METER-PARTIAL(W4). Diagnosis showed the mode sits on the real 2nd-harmonic content (local power 8× the sea). The corrected match ("on real content = a peak or a power-carrying harmonic, above the off-resonant sea") is faithful to the frozen "peak/harmonic" wording; the PASS criterion was not loosened (coverage, M-invariance, off-resonant→0 all hold independently).

### W5 — tare-rule check (the arm-spatiality budget) · **PASS**
Tare-usable gate `|c_fit − c|/c < 0.02` holds at all three points (the computable tare `c=√(1−E_bath/E0)` IS the fitted global attenuation `c_fit=⟨V_on·V_off⟩/⟨V_off·V_off⟩`):

| point | c = √(1−E_bath/E0) | c_fit (best-fit global) | \|c_fit−c\|/c | **spatial residual** |
|-------|--------------------|-------------------------|---------------|----------------------|
| mild | 0.8546 | 0.8543 | 4.44e-04 | **0.0255** |
| moderate | 0.8713 | 0.8701 | 1.38e-03 | **0.0457** |
| near-knee | 0.8897 | 0.8881 | 1.75e-03 | **0.0526** |

**★Spatial-residual trend (the arm-spatiality budget, the number that gates how spatial an arm discriminant can be): 0.025 → 0.046 → 0.053, growing ~2× from mild to near-knee.** This quantifies the fidelity degradation predicted in §B1: at near-knee, ~5.3% of the ON-vs-OFF trajectory divergence is genuine spatial restructuring the global tare does NOT capture. An F6 arm keying on a spatial discriminant near the knee must survive above this ~5% residual floor (and below the flag at 0.5, which is far off). The tare stays a computable, non-fitted scalar across the whole envelope.

> **★HONEST SCOPE (R-4, PR #721 review).** `|c_fit − c|/c` is **algebraically `1 − cosθ`**, where θ is the angle between the ON and OFF trajectories (`c_fit = ‖V_on‖cosθ/‖V_off‖`, `c ≈ ‖V_on‖/‖V_off‖`) — **verified EXACT numerically** at all three points (`|c_fit−c|/c` = `1−cosθ` to full precision, ratio 1.00). It is therefore the **SAME measurement as the spatial residual** (both read θ): the c-agreement is *enforced by the rescale arithmetic* and **could never fail independently** of the residual. So W5's informative content is the **RESIDUAL TREND** (the arm's spatial-discriminant budget), **not** an independent tare confirmation. To give this leg a genuinely independent liveness check, the tare-usable gate is **TIGHTENED** (Rule-11-legal — a strengthening, not a loosening; disclosed in the §B-post-review addendum R-4): E_bath at each point must exceed `E_BATH_MIN`, so the tare check cannot pass trivially on a **dead coupling** (where c→1, c_fit→1, θ→0 agree vacuously on a zero transfer). All three points pass the tightened gate (E_bath healthy — see W2 transfer).

### W6 — envelope restatement · **PASS**
Nyquist guard fires (build past the M≤95 cap raises: True). Friction discriminator on the nonlinear moderate plant: reactive **R=0.0 (<0.2, stored=4.64)** vs friction **R=0.953 (>0.8, dissipated=5.41)**, magnitude matched Δ=17% ≤ 20%. The reactive-vs-friction (stored-vs-gone) separation persists on the nonlinear plant.

---

## Deviations from §B (disclosed, Rule 11 — deviations are findings, not silent fixes)

1. **W3 placement rule** — the literal "avoid n·ω_d harmonics" rule is unsatisfiable for this broadband plant (harmonics tile (0,π)); replaced by "off all significant measured q-power" (band q-power fraction < 1e-2, above ω_99). **The chosen band [1.18, 2.11] CONTAINS harmonics n=3 (1.571) and n=4 (2.095)** — stated plainly (R-6); honest on the power budget (those harmonics carry q-power frac 1.1e-3 ≪ 1e-2). PASS criterion unchanged; collapse ×323. See W3 above.
2. **W4 honesty gate is a THIRD operationalization** (R-5) — the shipped gate is **band-power > 4×median-sea**, not the frozen "within `2Δω` of a peak/harmonic" proximity text (nor the earlier peaks-only definition). Mitigation banked: all 10 occupied modes ALSO pass the **strict frozen** criterion (reproduced; ω=1.05 matches 2ω_d at Δ=0.0025) and the white-noise/off-resonant probe fires honestly (→ N_occ=0). Future-plant divergence risk flagged (the two operationalizations can disagree on a different plant — reconcile before reuse). See W4 above.
3. **W2 relabel** (R-1) — heading demoted from "decisive KILL leg" to "ledger-regression + transfer-health leg"; conservation is identity-enforced on this plant class, not empirically survived. See W2 above + the §B-post-review addendum R-1.
4. **W5 tare-agreement is not independent of the residual** (R-4) — `|c_fit−c|/c` = `1−cosθ` (exact), the same measurement as the spatial residual; a genuinely independent E_bath-liveness sub-check was added to the tare-usable gate (Rule-11-legal tightening). See W5 above.
5. **FACT-4 charter triple was scratch-provenance** (R-3) — the §B1 `1.8e-4/1.76e-3/5.4e-3` triple is not reproducible from shipped code; the banked reproduction is `4.74e-5/4.52e-4/1.32e-3` (27.8×), same order/trend as the reviewer's independent `4.3e-5→1.2e-3`. Charter §B body NOT edited; both stated in the §B-post-review addendum R-3; reproduced triple banked in the result JSON addendum.

All frozen **PASS thresholds** (MACHINE_TOL, R_BATH_MAX, R_FRICTION_MIN, FRICTION_MATCH_TOL, N_OCC_M_TOL, W3 ≥2-orders collapse, W5 tare 0.02) were met as frozen; no gate was loosened (the W5 change is a tightening). The deviations above are **operationalization / provenance / framing** findings, not gate loosenings.

---

## Routed flags (owed to other lanes — NOT landed here; surfaced per flag-don't-fix)

- **[→ auditor lane] Mode-count arm prereg "Platform" lines (R-2).** Both prior F6 arm preregs pin *"Platform: nonlinear=True"* as the kernel. Given FACT-1 (the `nonlinear` flag is a no-op UNCONDITIONALLY — z-independent scatter), those labels are **costume to the same degree** as this lane's was pre-relabel: the platform line describes a flag with no dynamical consequence. An **auditor-lane correction-note is owed** on the mode-count arm preregs' platform lines. Those are **frozen docs** — this is a **flag only**, not an edit here.
- **[→ auditor lane] §A6 "pump independent of nonlinearity — verified" is now vacuous (R-7).** §A6 records that the cold-plant pump is *"independent of nonlinearity — verified"*. Given FACT-1, that comparison was between **bit-identical configurations** (nonlinear=True ≡ nonlinear=False), so the statement is **vacuously true, not an independent verification**. **§A stays byte-untouched**; the correction-note lands in the §B-post-review addendum (R-7) and is surfaced here for the auditor to land the manual entry.
- **[→ engine lane] Double-integration hazard (R-2).** If op3 + nonlinear + `use_memristive_saturation` are ever all ON, `_scatter_all` advances `S_field` twice per step. Dormant in this lane (`use_memristive_saturation=False`). See the Substrate-native finding above.

---

## Reproduce

```
python src/scripts/vol_1_foundations/f6_bath_meter_validate.py --w-battery          # text
python src/scripts/vol_1_foundations/f6_bath_meter_validate.py --w-battery --json    # machine
python src/scripts/vol_1_foundations/f6_bath_meter_validate.py --fact4               # FACT-4 non-commutation (opt-in provenance; R-3)
pytest src/tests/test_f6_bath_meter.py -m "not engine_sim"   # 16 fast (11 A + 5 W)
pytest src/tests/test_f6_bath_meter.py -m engine_sim         # 2 full batteries (A + W)
```

Deterministic (SEED=1). Runtime ~60 s (W-battery). The A-battery (V1–V6) is unchanged and still returns METER-VALID-WITHIN-ENVELOPE. The `--fact4` opt-in is NOT a gate — it reproduces the §B1 FACT-4 non-commutation triple for provenance (R-3).

---

## Scope guard

This lane returns a verdict on the **meter in the nonlinear regime**, never on F6. METER-VALID-NONLINEAR-ENVELOPE does NOT bank CHANNEL-BOUNDED, does NOT ungate the thermometer, and does NOT fire an arm. The R7 §7 receipt stays with the auditor lane; rebase-before-integration onto the F1 fix still stands (charter §9). The arm-integration ruling (whether the ~90% uniform + ≤5.3% spatial back-reaction satisfies the ratings-map §7 semantics) remains **Grant's call at integration time**, now with the nonlinear-regime tare budget quantified.
