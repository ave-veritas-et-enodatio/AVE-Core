# Vacuum-Birefringence BENCH-MODEL — RESULT (the bankable-number gate)

> 🔴 **QED-NORMALIZATION CORRECTION (2026-07-03; Rule-12).** Any `7.5/α³ ≈ 1.93×10⁷` / `4.14×10⁶` ratio here uses
> an understated QED denominator (too small by `1/(2πα) ≈ 21.8`). Corrected differential ratio: `7.5π/α² ≈ 4.42×10⁵`
> (propagating). AVE leg unaffected. See
> [`2026-07-03_birefringence-qed-normalization-correction.md`](2026-07-03_birefringence-qed-normalization-correction.md).

> 🔵 **Current headline number.** This doc's bankable number and the per-row $4.14\times10^6$ in §0 / the table below were computed as
> the AVE **scalar single-arm** ($-\tfrac14 A^2$) over the QED **parallel single-mode** ($7/45$). A
> birefringence instrument measures the **par−minus−perp differential**, so the corrected falsifier
> headline is the **matched differential** $\delta n_{AVE}/\delta n_{QED}=7.5/\alpha^3\approx1.93\times10^7$
> (AVE differential $-\tfrac12 A^2$ vs QED **differenced** Euler-Heisenberg $3/45$). The single-arm
> $4.14\times10^6$ below is the isotropic common-mode (polarimeter-blind) comparison — traceability only.
> Canonical: [`2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`](2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md).
> Chord-vs-echo unchanged (CHORD = saturation exists; MAGNITUDE = $\alpha$-echo).

**Status:** RESULT (2026-06-20). First concrete step of the testing pivot (memory `project_state_of_ave_and_testing_pivot.md`): build the infra to fully model a bench + run a full sensitivity sweep -> produce THE bankable number that decides whether AVE's vacuum-birefringence prediction diverges from the SM at reachable fields.
**Driver:** `src/scripts/vol_9_device/vacuum_birefringence_bench.py`
**Physics module:** `src/ave/bench/birefringence.py` (extends the `ave.bench` shared package, #318)
**Artifacts:** `src/scripts/vol_9_device/_output/vacuum_birefringence_bench.{json,png}`
**Lane:** implementer.
**Class:** the FORMS (E²-leading retardance, parity-odd rotation) are AVE-distinct **chords** (manifestations of Axioms 4 / 1); the magnitudes ride the α-echo family — NOT headlined as forced numbers (`consistency-vs-emergence`, `ave-evidence-framing-discipline`).

---

## §0 — THE BANKABLE NUMBER (headline)

**Retardance:** at facility-class fields (E ~ 10¹³–10¹⁴ V/m, top-laser tier) AVE predicts a refractive-index retardance `δn_AVE ≈ 2×10⁻⁹ … 2×10⁻⁷`, against the QED Euler-Heisenberg baseline `δn_QED ≈ 5×10⁻¹⁶ … 5×10⁻¹⁴`. **Divergence factor `R = δn_AVE/δn_QED ≈ 4.1×10⁶` — field-INDEPENDENT** (single-mode a_EH=7/45; band `[4.4×10⁵, 9.7×10⁶]` across the EH prefactor convention spread). Both responses are **E²-leading**; the discriminator is the **COEFFICIENT**, present at every field.

**Parity-rotation (the cleanest discriminator):** AVE's chiral I4₁32 vacuum is parity-odd and rotates the polarization plane (±75.462°/lattice-unit, #195); **QED vacuum produces ZERO rotation**. A nonzero, enantiomorph-sign-flipping rotation that is zero on an achiral control has **no QED counterpart at all** — a zero-vs-nonzero discriminator. Magnitude is unpinned (rides a tagged engineering scale × apparatus chirality density); the FORM is the AVE-distinct content.

**Reachability verdict:** **FACILITY-class, not benchtop.** δn_AVE clears a high-finesse-cavity floor (~10⁻¹⁵) for E ≥ ~10¹¹ V/m (petawatt-laser tier); benchtop DC (FN-safe ceiling ~1.3×10⁹ V/m) leaves δn_AVE below floor. At the fields where δn_AVE is measurable, the accumulated cavity phase is enormous (many radians at finesse ≥ 10³), so measurability is NOT the binding constraint — reaching the field is. The binding question is whether the measured *coefficient* is AVE-sized (~10⁶× QED) or QED-sized.

---

## §1 — FLAG-DON'T-FIX: the task-brief framing conflicts with the corpus (surfaced, not silently reconciled)

The dispatch brief asked for the "**E⁴ deviatoric-split form**" as the AVE-distinct retardance and a "**~10⁶× coefficient**" headline. The canonical corpus **already adjudicated this and the E⁴ framing is RETRACTED.** Verbatim, both sides:

- **Brief:** "δn_AVE(E) — the E⁴ deviatoric-split form" and "AVE's ~10⁶× coefficient … quoted near the YIELD field".
- **Corpus** (`manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md:10,20`): *"**Both predict an E²-leading index shift; the discriminator is the COEFFICIENT.**"* … *"The historical formulation 'Δn_eff = 1 − √(1 − (E/E_yield)²), leading E⁴ term' was a √ε conflation … The corrected discriminator is the coefficient, not the exponent."*
- **Corpus driver header** (`src/scripts/vol_4_engineering/simulate_vacuum_birefringence_E4.py:1-28`): the E⁴ script is **🔴 SUPERSEDED (Rule 12 walk-back, 2026-06-20)** in favor of `birefringence_coefficient_discriminator.py`.

**Resolution applied (no silent fix):** this bench-model is built on the **corrected E²-leading COEFFICIENT** physics (the live corpus), NOT the retracted E⁴ form. The "deviatoric-split" idea from the brief is honored where it IS canonical — the deviatoric strain channel that splits per-DOF (L_i,C_i) is the *birefringence FORM origin* (`vacuum_node_circuit.py:162` `deviatoric()`), distinct from the *retardance magnitude* (the √S kernel). The "~10⁶× coefficient" is reported as a **band** with the E²-leading framing, not as a forced number near yield. This is a flag for Grant/auditor: **the brief carried the pre-2026-06-04 framing; the build follows the post-correction corpus.**

A second, SUBSTANTIVE addition the brief requested and the corpus supports: the **parity-odd optical-activity ROTATION** as a first-class discriminator. This is NOT in the existing coefficient driver — it is the genuinely new content of this bench-model, grounded in the validated #195 chiral-grid result (`engine-capability-map.md:44`, `def-0pt1ac`).

---

## §2 — VALIDATE-ON-KNOWN (the gate; HALT if any fail)

The driver HALTs before producing any AVE-vs-QED comparison unless all three recover a labeled known:

| Gate | Computed | Known target | Result |
|---|---|---|---|
| QED magnetic birefringence const `A_e = 2α²ℏ³/(45 μ₀ m_e⁴ c⁵)` | `1.3247×10⁻²⁴ T⁻²` | PVLAS/Rizzo `1.32×10⁻²⁴ T⁻²` | **PASS** (rel-err 0.35%) |
| substrate identity `(E_crit/E_yield)² == 1/α` | `137.0360` | `1/α = 137.0360` | **PASS** (exact) |
| field-energy equivalence `c·B_crit == E_crit` | `1.3233×10¹⁸ V/m` | `E_CRIT` | **PASS** (exact) |

The PVLAS `A_e` recovery is the load-bearing one: it proves the QED side reproduces the *actually-measured* vacuum magnetic birefringence constant. The QED differential shift `δn = 3A_e B²` gives `δn_QED(1 T) = 3.97×10⁻²⁴`, recovering the textbook `~4×10⁻²⁴`. All AVE constants import from `ave.core.constants`; the only non-AVE numbers are the EH prefactor band and the PVLAS `A_e` closed form (labeled literature).

> **Consistency-check finding (not a free pass).** The PVLAS-`A_e` differential convention and the single-mode `a_EH = 3/45` differential convention differ by **21.8×**: the PVLAS form corresponds to an effective `a_EH = 3 A_e B_crit²/α² ≈ 1.454`, exactly the "order-of-magnitude EH ~1.5" value flagged in `research/2026-06-04_birefringence-coefficient-prereg.md` §5.2. These are two standard conventions, not a contradiction — both are in the reported band. The PVLAS form is the authoritative validate-on-known anchor (it recovers `1.32×10⁻²⁴ T⁻²`).

---

## §3 — Channel 1: RETARDANCE δn_AVE(E) vs δn_QED(E)

| E (V/m) | A = E/E_yield | δn_AVE (full √S) | δn_QED (a=7/45) | \|AVE\|/QED | source tier |
|---|---|---|---|---|---|
| 1×10⁹ | 8.8×10⁻⁹ | −1.96×10⁻¹⁷ | 4.73×10⁻²⁴ | 4.14×10⁶ | benchtop DC (FN-safe) |
| 1×10¹¹ | 8.8×10⁻⁷ | −1.96×10⁻¹³ | 4.73×10⁻²⁰ | 4.14×10⁶ | petawatt laser ~10²² W/m² |
| 1×10¹³ | 8.8×10⁻⁵ | −1.96×10⁻⁹ | 4.73×10⁻¹⁶ | 4.14×10⁶ | top-facility ~10²⁶ W/m² |
| 1×10¹⁴ | 8.8×10⁻⁴ | −1.96×10⁻⁷ | 4.73×10⁻¹⁴ | 4.14×10⁶ | top-facility ~10²⁶ W/m² |
| 1×10¹⁶ | 8.8×10⁻² | −1.96×10⁻³ | 4.73×10⁻¹⁰ | 4.15×10⁶ | unreachable |

- **Field-INDEPENDENT ratio** verified (`True`): `1/(4 a_EH α³) = 4.14×10⁶` at a_EH=7/45; band `[4.42×10⁵, 9.65×10⁶]` across the four EH conventions.
- **Crossover:** the ratio is ~10⁶ and field-independent, so **AVE exceeds QED at ALL fields** — the "crossover field" is at zero; there is no field below which QED dominates. The discriminator is the COEFFICIENT, not an onset.
- **Numerical guard:** `δn_AVE` is evaluated via `expm1(¼·log1p(−A²))`, exact at small A (the naive `(1−A²)^¼ − 1` underflows to a spurious 0 for A ≲ 10⁻⁴ — the catastrophic-cancellation bug caught and fixed during this build; it would have zeroed every lab-magnet and weak-E entry).

**SM-counterfactual (`ave-discrimination-check`):** a measured retardance coefficient of QED size (α²-suppressed, ~10⁶× smaller) falsifies AVE; an AVE-sized coefficient falsifies QED at this observable. An E²-leading *slope* is NOT a discriminator (both are E²-leading).

---

## §4 — Channel 2: OPTICAL-ACTIVITY ROTATION (the clean QED-zero discriminator)

| Probe path (m) | θ_AVE (chir frac 1.0, bare ceiling) | θ_AVE (chir frac 10⁻¹²) | θ_QED |
|---|---|---|---|
| 1×10⁻³ (1 mm) | 1.95×10¹¹ deg | 1.95×10⁻¹ deg | **0** |
| 1×10⁻² | 1.95×10¹² deg | 1.95×10⁰ deg | **0** |
| 1×10⁻¹ | 1.95×10¹³ deg | 1.95×10¹ deg | **0** |
| 1×10⁰ (1 m) | 1.95×10¹⁴ deg | 1.95×10² deg | **0** |

- **Bare-lattice rate** ±1.954×10¹⁴ deg/m (= ±75.462°/node-span ÷ ℓ_node), sign-flipping between enantiomorphs; **achiral diamond control = 0**; **QED vacuum = 0 identically**.
- The bare rate is a **full-chirality CEILING**; a bench realizes a fraction `chirality_fraction` of it (apparatus-set, **unpinned**). At a 1 m path, a state-of-the-art polarimetry floor (~10⁻⁹ deg) is cleared down to `chirality_fraction ≈ 5.1×10⁻²⁴` — i.e. even a vanishingly small realized chirality density gives a detectable rotation over a metre, because the bare lattice rate is astronomically large.
- **This is the strongest discriminator:** QED has NO vacuum optical activity. A nonzero rotation that (i) flips sign with the lattice handedness and (ii) is zero on an achiral control has **no QED explanation at any magnitude** — a zero-vs-nonzero test, not a coefficient-comparison.

**Honest scope (`ave-evidence-framing-discipline`):** the rotation FORM (parity-odd, sign-flipping, achiral-null) is the AVE-distinct **chord** (Axiom-1 chiral I4₁32). The rotation MAGNITUDE rides a **tagged engineering scale** (`ETA_ROT_PER_WRITHE = 1.0`, `chiral_lattice_vector.py:27`) × the lattice writhe density — it is NOT a forced number and is NOT headlined as one. The open question for a real bench is how much of the bare-lattice chirality the vacuum actually presents to a probe (the `chirality_fraction`); the bare ceiling is almost certainly not realized, but even ~24 OOM of suppression leaves a metre-path rotation detectable.

---

## §5 — Channel 3: MAGNETIC (PVLAS/BMV-class)

QED `δn = 3 A_e B²` (the actually-measured PVLAS observable) vs the AVE magnetic-equivalent (energy-density mapping `A = cB/E_yield`, then the same √S retardance):

| B (T) | δn_QED = 3 A_e B² | cB (V/m) | δn_AVE(cB) | \|AVE\|/QED |
|---|---|---|---|---|
| 1.0 | 3.97×10⁻²⁴ | 3.0×10⁸ | −1.76×10⁻¹⁸ | 4.4×10⁵ |
| 5.0 | 9.94×10⁻²³ | 1.5×10⁹ | −4.40×10⁻¹⁷ | 4.4×10⁵ |
| 16.0 | 1.02×10⁻²¹ | 4.8×10⁹ | −4.50×10⁻¹⁶ | 4.4×10⁵ |
| 45.0 | 8.05×10⁻²¹ | 1.3×10¹⁰ | −3.56×10⁻¹⁵ | 4.4×10⁵ |

The coefficient gap persists (~4.4×10⁵ for the differential convention), but at lab/pulsed B the field-energy-equivalent E (cB ~ 10⁹–10¹⁰ V/m) is far below E_yield, so the **absolute** AVE signal (10⁻¹⁸–10⁻¹⁵) is at/below a cavity floor. **The magnetic channel alone does not reach measurability with lab magnets** — it needs E-field concentration or the rotation channel.

---

## §6 — Channel 4: MEASURABILITY MAP (peak field × cavity finesse)

A Fabry-Perot cavity (finesse F → 2F/π effective passes) accumulates phase `δφ = (2π/λ)·|δn|·L·(2F/π)` for an L=1 m, λ=1064 nm probe. Shot-noise 5σ phase floor (10¹⁵ Hz probe, 10³ s) ≈ **5×10⁻⁹ rad**.

| E (V/m) | F=10³ | F=10⁴ | F=10⁵ | F=10⁶ | (accumulated phase, rad) |
|---|---|---|---|---|---|
| 1×10¹³ | 7.4 | 73.5 | 735 | 7.4×10³ | |
| 1×10¹⁴ | 735 | 7.4×10³ | 7.4×10⁴ | 7.4×10⁵ | |
| 1×10¹⁶ | 7.4×10⁶ | 7.4×10⁷ | 7.4×10⁸ | 7.4×10⁹ | |

- **The AVE retardance, IF real at the ~10⁶× coefficient, is enormously above the cavity floor at facility fields:** at E=10¹³ V/m even F=10³ gives 7.4 rad = ~1.5×10⁹× the floor. Measurability is **not** the binding constraint at these fields — phase wraps many times.
- The binding constraint is **reaching the field.** δn_AVE clears the ~10⁻¹⁵ cavity floor at E ≥ ~10¹¹ V/m (petawatt-laser tier); benchtop DC (FN-safe ≤ 1.3×10⁹ V/m) leaves it below floor.

---

## §7 — Reachability verdict

| Tier | Field ceiling | δn_AVE there | Verdict |
|---|---|---|---|
| Benchtop DC (FN-safe) | ~1.3×10⁹ V/m | ~3×10⁻¹⁷ | below cavity floor — **not benchtop** |
| Petawatt laser (~10²² W/m²) | ~2.7×10¹¹ V/m | ~1.4×10⁻¹² | above floor — **facility-marginal** |
| ELI-class (~10²³ W/m²) | ~8.7×10¹² V/m | ~1.5×10⁻⁹ | comfortably measurable — **facility** |
| Top-facility (~10²⁶ W/m²) | ~2.7×10¹⁴ V/m | ~1.5×10⁻⁶ | **facility (sweet spot)** |

**Verdict: FACILITY-class, not benchtop, for the retardance channel.** The parity-rotation channel is the more bench-accessible discriminator IF any realized vacuum chirality presents to the probe (the bare-lattice rate is so large that even extreme suppression leaves a metre-path rotation detectable) — but its magnitude is unpinned, so it is a FORM-test (zero-vs-nonzero), not a magnitude-test.

---

## §8 — Bankable numbers + falsifiers (frozen, Rule 11)

1. **δn_AVE(10¹⁴ V/m) ≈ 1.96×10⁻⁷; δn_QED(10¹⁴ V/m) ≈ 4.73×10⁻¹⁴; divergence R ≈ 4.1×10⁶** (band [4.4×10⁵, 9.7×10⁶]), field-independent. Measurable at finesse ≥ 10³ (phase ≫ floor). Reachable at top-facility-laser fields.
2. **Parity rotation: θ_QED ≡ 0; θ_AVE ≠ 0, sign-flips with handedness, zero on achiral control.** The clean SM-divergence falsifier — a nonzero handedness-odd vacuum rotation falsifies QED; a measured zero (with realized chirality present) falsifies the AVE chiral-vacuum prediction.
3. **Falsifier (retardance, two-sided):** QED-sized coefficient (~10⁶× smaller) ⇒ AVE falsified; AVE-sized coefficient ⇒ QED falsified at this observable. NOT a falsifier: an E²-leading slope.

**Class discipline:** the E²-leading FORM and the parity-odd ROTATION FORM are AVE-distinct chords; the ~10⁶ coefficient rides α⁻³ (the α-echo family) and the rotation magnitude rides a tagged engineering scale — neither is headlined as a forced emergence-class number.

---

## §9 — Open items / flags for Grant + auditor

1. **FLAG (framing):** the dispatch brief carried the **pre-2026-06-04 E⁴ framing**, which the corpus RETRACTED (§1). The build follows the corrected E²-leading COEFFICIENT corpus. Grant/auditor to confirm the brief's E⁴ language was legacy, not a re-opening.
2. **OPEN (rotation magnitude):** the bench-realizable `chirality_fraction` (how much bare-lattice chirality a probe sees) is unpinned. The rotation channel is a robust FORM-test now; turning it into a magnitude-prediction needs a physical model of the realized vacuum chirality density — a follow-up.
3. **EH prefactor convention** (carried from prereg §5.2): the corpus headline coefficient should pin one a_EH convention; the band is reported so no re-run is needed. Physics verdict unchanged across the band.
4. **No new matrix cell flips, no claim retraction.** This bench-model is a forward calculator building on clm-pp3qwf (the coefficient discriminator) + the #195 optical-activity result; it adds the rotation channel as a new observable. The auditor lands any manifest/matrix entry; this result surfaces it.

