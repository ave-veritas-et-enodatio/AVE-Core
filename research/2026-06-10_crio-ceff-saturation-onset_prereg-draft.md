# Prereg (DRAFT): cRIO C_eff(V) Saturation-Onset Discriminator — the program's first real-hardware bench

**Status:** `DRAFT-FOR-GRANT-REVIEW` (2026-06-10). **NOT FROZEN.** This document freezes
only when Grant schedules bench time. DOC-ONLY: no hardware acquired, no execution. The
genesis-v7 simulation run closes the sim arc; this is the staged first-hardware prereg that
becomes live when Grant says "build it."
**Lane:** implementer (per Grant 2026-05-01 cross-authorization where applicable). Real-hardware
falsification-instrument design — the program's first one.
**Origin:** the deferred cRIO benchtop bench (memory: `project_crio_benchtop_falsification_bench.md`).
Grant owns NI cRIO-9014 controller + NI-9263 (4ch AO, ±10 V, 100 kS/s) + NI-9215 (4ch AI, ±10 V,
100 kS/s) = a DC–40 kHz 4×4 phase-coherent lock-in bench. First experiment = the C_eff(V)
saturation-onset discriminator, with the validation-ladder discipline FIRST (this bench's plan is
where `ave-apparatus-floor-attribution` was encoded from).

**Skills fired at draft time:** `pre-test-physics-check` (T6 draft-moment — one plumber question to
Grant, §0), `ave-prereg` (corpus-grep + Step-3.5 dimensional, §3), `ave-canonical-source` (every
number imported/verified from `src/ave/core/constants.py`, §3), `substrate-native-check` (the C_eff
form is derived from the Ax-4 kernel, not an SM nonlinear-optics analogy, §1), `ave-discrimination-check`
(SM/standard-phenomenology counterfactual, §2), `phase-space-coordinate-check` (§9 — the kernel's
amplitude `A` is a per-node operating-point coordinate, not the lab voltage), `consistency-vs-emergence`
(§9 class tags), `ave-regime-phase-state-check` (§9 mode/regime/phase declaration), `verify-before-cite`
(file:line citations grepped this session).

---

## §0 — Pre-test physics check: the ONE plumber question to Grant (BEFORE freeze)

Per Rule 16 strengthening, surfaced at DRAFT time, not after 30+ commits.

**The question (sign-of-slope — load-bearing for the discrimination bin, §2):**

> Grant — does the AVE bench prediction say a DC-biased capacitor's measured **small-signal
> capacitance** should **RISE toward a divergence** as bias climbs, or **FALL / soften**? The corpus
> gives me two canonical leaves with **opposite signs of slope**, and which one is right decides
> whether a Class-2 derating MLCC (which *falls*) **supports** or **contradicts** the AVE form — i.e.
> it sets the entire AVE-FORM / STANDARD-FORM bin boundary.

This is also logged below as a **flagged corpus tension** (flag-don't-fix, Operating-principle 6).
I did NOT pick a branch; both are quoted verbatim with file:line, and the discrimination section (§2)
is written to carry BOTH until Grant adjudicates.

### Flagged corpus tension — C_eff(V) sign of slope (DO NOT silently resolve)

- **Branch R (rising / diverging):** [`nonlinear-vacuum-capacitance.md:21`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md)
  — verbatim:
  > `C_eff(V) = C_0 / sqrt(1 - (V/V_yield)^2) = C_0/S(V)`
  with the table at `:32-39` showing `C_eff/C_0 = 1.005 / 1.155 / 2.294 / 7.089 / ∞` at
  `V/V_yield = 0.10 / 0.50 / 0.90 / 0.99 / 1.000`. Capacitance **rises and diverges** at V_yield. The
  leaf's own claim-quality marker `clm-8nkvwy` (`:17`) states: *"Asymmetric saturation case: only ε
  scales by S → C_eff → ∞, Z_asym = Z_0/√S → ∞."*

- **Branch F (falling / softening):** `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 — verbatim:
  *"Dielectric specialization … `C_eff = C_0/S, ε_eff = ε_0 S, μ_eff = μ_0 S`."* and the predecessor
  prereg [`2026-06-03_yield-knee-map-prereg.md:8,44`](2026-06-03_yield-knee-map-prereg.md):
  *"ε_eff(V) = ε₀√(1−(V/V_yield)²)"* and *"AVE: δε/ε₀ = −A²/2 — the vacuum dielectric **softens**
  (negative V² coefficient)."* The small-signal **permittivity falls** with bias.

**Why this is a genuine tension, not my confusion:** `C ∝ ε` for a fixed-geometry capacitor, so
`ε_eff = ε_0·S` (falling) and `C_eff = C_0/S` (rising → ∞) cannot both describe the same measured
parallel-plate capacitance. Physically they look like two *different observables* sharing the name
"capacitance": (a) the small-signal **differential permittivity** `ε_diff = dD/dE`, which a saturating
polarization drives toward `ε_0` (falls — the ferroelectric-derating picture), versus (b) a bulk
**compliance / displacement-per-force** that *diverges* at rupture (the medium flows). The bench
measures (a) — the quadrature-current small-signal C (§5). **Grant's call:** which sign should the
bench see, and is Branch R describing a rupture-compliance observable the bench does NOT measure?
The auditor lane should NOT land a manual entry on this until Grant adjudicates; I surface it only.

---

## §1 — The frozen forward prediction (derived from the canonical Ax-4 kernel)

**Class tag (per `consistency-vs-emergence`, full classification in §9): the FORM is a Class-B axiom
manifestation; any bench match on a real material is Class-C consistency.** Not an emergence test.

### §1.1 Substrate-native derivation chain (not an SM analogy)

The prediction is NOT "capacitors are varactors, fit a varactor curve." It descends from the Axiom-4
universal saturation kernel:

1. **Kernel (Axiom 4, canonical):** `S(A) = sqrt(1 - A^2)` where `A = A/A_yield` is the **per-node
   saturation operating-point amplitude** (`manuscript/ave-kb/CLAUDE.md` INVARIANT-S2; dielectric
   specialization `A = Δφ/α`). This is a **phase-space / operating-point** coordinate, NOT the lab
   voltage — see §9 phase-space note. The dielectric specialization sets `A = V/V_yield` **per node**.
2. **Op14 wave-speed modulation (canonical):** [`op14-local-clock-modulation.md:29`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md)
   `c_eff = c_0·sqrt(S)`; and the Maxwell phase velocity `c_EM = c_0/S` (`manuscript/ave-kb/CLAUDE.md`
   INVARIANT-S2, clm-8nkvwy:111).
3. **Lumped constitutive form (canonical):** holding the inductive (μ / Cosserat-B) sector fixed — the
   correct choice for a **static-E-only DC bias**, which is the **ASYMMETRIC** load per INVARIANT-S2
   (`S_ε < 1, S_μ = 1`) — the capacitance follows the kernel. **The two canonical branches (§0):**
   - Branch R: `C_eff(V)/C_0 = 1 / sqrt(1 - (V/V_yield)^2)` (`nonlinear-vacuum-capacitance.md:21`)
   - Branch F: `ε_eff(V)/ε_0 = sqrt(1 - (V/V_yield)^2)` → `C_eff(V)/C_0 = sqrt(1 - (V/V_yield)^2)`
     (INVARIANT-S2 + yield-knee prereg)

### §1.2 The frozen-form summary (both branches, small-A Taylor)

Let `x ≡ V/V_yield` (the per-node operating-point ratio). The canonical Taylor expansions:

| Branch | Closed form | Small-x Taylor | Sign of leading V² coeff |
|---|---|---|---|
| **R** (rising) | `C/C_0 = (1 − x²)^(−1/2)` | `1 + ½x² + ⅜x⁴ + …` (`nonlinear-vacuum-capacitance.md:27`) | **+½** (stiffens) |
| **F** (falling) | `C/C_0 = (1 − x²)^(+1/2)` | `1 − ½x² − ⅛x⁴ − …` (yield-knee prereg:44) | **−½** (softens) |

**The frozen forward prediction the bench would test:** the small-signal `C_eff(V)/C_0` follows a
**quarter-arc kernel** with leading **V² coefficient of magnitude ½** (in per-node units `x = V/V_yield`),
**sign per Grant's §0 adjudication.** The second-harmonic (2ω) generation coefficient is the canonical
companion observable: `δC/C = ¼ x²` at 2ω (yield-knee prereg:48, `parametric-coupling-kernel.md:70-80`).

**The AVE-distinct fingerprint vs standard phenomenology (§2):** (i) the specific `(1−x²)^(±1/2)`
**quarter-arc shape** (a √-form, with a vertical-tangent **knee** at `x→1`), not a power-law or
tanh/Devonshire form; (ii) the **single yield field V_yield** sets the knee location at zero free
parameters *for the vacuum* (but is a FIT parameter for any real material — §6 honest scope); (iii)
the 2ω even-harmonic with the canonical ¼ coefficient.

---

## §2 — Discrimination (`ave-discrimination-check`): does the AVE form separate from standard physics?

**Step 2.5 axis classification first:** the AVE kernel and the standard saturating phenomenologies
**share the SCALE** (both saturate at O(0.1–1) of the material's own field) but **differ in SHAPE**
(`(1−x²)^(±1/2)` vs power-law vs tanh). Therefore the discriminator is the **functional FORM / shape**,
NOT the magnitude. A magnitude claim here would carry the absolute V_yield calibration, which is a fit
parameter for any real material (§6).

### §2.1 What the competing (standard) phenomenologies predict for the same DC-bias C-V sweep

| Phenomenology | C(V) form | Sign of slope | Knee character |
|---|---|---|---|
| **Linear dielectric** (C0G/NP0) | `C = C_0` (flat) | none | none |
| **Reverse-biased junction varactor** | `C = C_j0·(1 + V_R/V_bi)^(−m)`, m≈0.3–0.5 | **falls** | smooth power-law roll-off, no finite-field divergence |
| **Class-2 ferroelectric MLCC** (X7R/X5R, DC-bias derating) | Landau–Devonshire / empirical; `ε_diff` falls (polarization saturates, `dP/dE→0`) | **falls** (50–80% by rated V) | smooth saturation, no √-knee |
| **AVE Branch F** (softening) | `C/C_0 = (1−x²)^(+1/2)` | **falls** | √-form, vertical-tangent knee at x→1 |
| **AVE Branch R** (rising) | `C/C_0 = (1−x²)^(−1/2)` | **rises** | √-form, **divergence** at x→1 |

**Sign-of-slope reading (load-bearing, ties to §0):**
- If Grant adjudicates **Branch R (rising)**: the AVE form is **sign-distinct from ALL three standard
  falling phenomenologies** — a real cap that *rises* toward a divergence would be a clean AVE-distinct
  signature. But no common dielectric rises (would need a relaxor near its Curie point from above);
  so a rising read is *unlikely on a stock cap* and Branch R may be describing the bulk
  rupture-compliance observable the small-signal bench does **not** measure (§0 physical note).
- If Grant adjudicates **Branch F (softening)**: the AVE form has the **same sign** as both varactor
  and Class-2 MLCC. Discrimination then lives **only in the SHAPE** — `(1−x²)^(1/2)` vs `(1+V/V_bi)^(−m)`
  vs Devonshire-tanh — which requires high-precision C(V) over a wide x-range AND a parameter-free knee
  location. With V_local a fit parameter, the shapes are **nearly degenerate** at modest x.

### §2.2 Where (and whether) the curves separate at bench precision — the DISCRIMINATION VERDICT

Two regimes, two verdicts:

1. **The VACUUM Axiom-4 kernel: NOT separable — unreachable by ~18–24 OOM.** Per §3, at ±10 V the
   per-node operating-point is `x = A_0 ~ 10^(−11)`, so the *vacuum* contribution to `δC/C` is
   `~½·A_0² ~ 10^(−21)` (10 V across 1 µm) down to `~10^(−27)` (10 V across 1 mm). No bench floor —
   not a 10⁻⁹ capacitance bridge, not a 10⁻¹² cryo-lock-in — comes within ~10 OOM. **The cRIO bench
   CANNOT measure the vacuum saturation kernel. This is a prereg verdict, not a failure** (the task's
   "if they do NOT separate measurably at bench precision, SAY SO"). It is consistent with the
   predecessor Q-G42 / yield-knee finding (`2026-06-03_yield-knee-map-prereg.md:41`).

2. **The MATERIAL-analog (consistency-class): separable in PRINCIPLE, but the read is Class-C.** A real
   Class-2 MLCC or varactor reaches `x = V/V_local ~ 0.1–1` of **its own** material nonlinearity at
   ±10 V (that's *why* Class-2 caps derate 50–80% by rated voltage). So the bench CAN acquire a strong,
   high-SNR C(V) arc and CAN ask whether the arc shape is the `(1−x²)^(±1/2)` kernel form vs the
   standard forms — **but with V_local a fit parameter, even a good form-match is consistency-class**
   (§6). This is the `op14:106` / INVARIANT-S2 PONDER-05 reading: the material's own
   voltage-coefficient-of-capacitance reproduces the **kernel SHAPE**, it is NOT a vacuum-kernel read.

**Bottom-line discrimination verdict (state plainly):** *For the vacuum claim — NOT separable
(unreachable by ~20 OOM). For the material analog — separable in shape only, and only to
consistency-class (Class C), contingent on the §0 sign adjudication and on the FORM being distinguished
from standard saturating arcs over a wide bias range.* The cRIO's first experiment is therefore
**honestly a validation-ladder + material-analog consistency bench — the calibration rung for any
future high-field AVE bench — NOT a vacuum-kernel discriminator.**

---

## §3 — Step-3.5 dimensional subsection (canonical numbers): is the bench even in regime?

All values imported/verified from `src/ave/core/constants.py` this session (`ave-canonical-source`):
`V_YIELD = 43651.9 V`, `V_SNAP = 510999 V`, `E_YIELD = 1.13041×10¹⁷ V/m`, `L_NODE = 3.86159×10⁻¹³ m`,
`ALPHA = 7.29735×10⁻³`. Regime boundaries (per-node `A = V/V_yield`): `R_I = √(2α) = 0.1208`
(linear→nonlinear), `R_II = √3/2 = 0.8660` (nonlinear→saturated), `R_III = 1.0` (rupture).

### §3.1 The per-node operating-point at bench fields (the load-bearing reachability calc)

The kernel amplitude is a **per-node** ratio: `A_0 = E_local · ℓ_node / V_yield` where `E_local = V/d`
is the field across the dielectric thickness `d` (per INVARIANT-S2 + `op14:106` per-node-vs-apparatus
discipline). At the bench maximum ±10 V:

| Geometry (10 V across d) | E_local (V/m) | per-node A_0 | vacuum δε/ε₀ = −½A_0² |
|---|---|---|---|
| 10 V / 1 µm | 1.0×10⁷ | 8.85×10⁻¹¹ | −3.9×10⁻²¹ |
| 10 V / 100 µm | 1.0×10⁵ | 8.85×10⁻¹³ | −3.9×10⁻²⁵ |
| 10 V / 1 mm | 1.0×10⁴ | 8.85×10⁻¹⁴ | −3.9×10⁻²⁷ |

**The bench sits ~9 OOM below even the linear→nonlinear knee `R_I = 0.12`** — DEEP Regime I (linear
vacuum). To reach `A_0 = 0.1` (a measurable `δε/ε₀ = −0.5%`) needs `E_local = 1.13×10¹⁶ V/m` —
~10⁹× beyond the bench's 10⁷ V/m, and ~10⁶× beyond even the 30 kV/1 mm = 3×10⁷ V/m of a high-voltage
C-V bench. **The vacuum kernel is unreachable on a ±10 V instrument. Confirmed dead by regime.**

### §3.2 The accessible ANALOG regime (honest identification)

The bench IS in regime — by ~20 OOM more — for the **material's own** saturation. A Class-2 ferroelectric
reaches substantial polarization saturation at its rated voltage (a few V to tens of V), i.e. its
effective `V_local ~ O(1–100 V)`, so at ±10 V `x = V/V_local ~ 0.1–1`: a **strong, measurable** C(V)
arc. **This is the only AVE-relevant regime the cRIO accesses, and it is consistency-class** (the
material is not the vacuum; `V_local` is a fit parameter, not `V_yield`).

### §3.3 Frequency / phase-state regime

The bench band (DC–40 kHz) is **~16 OOM below** the canonical thixotropic crossover
`1/τ_relax = 7.76×10²⁰ Hz` (`nonlinear-vacuum-capacitance.md:61`; `τ_relax = ℓ_node/c = 1.29×10⁻²¹ s`).
The vacuum is therefore **fully relaxed / quasi-static** at bench frequencies — **no vacuum memristive
hysteresis** is possible (that needs `f ≫ 10²⁰ Hz`). Any hysteresis the bench sees is the **material's**
(dielectric absorption / ferroelectric domain loss) — a systematic to characterize, not a vacuum signal.

---

## §4 — THE VALIDATION LADDER FIRST (`ave-apparatus-floor-attribution`)

This bench is where the apparatus-floor discipline was *encoded from*. The ladder runs **before any
discriminating read** — characterize the chain on knowns at the run's own scale/config. No DUT-of-interest
C(V) is interpreted as physics until A, B, and C have passed.

| Stage | Device | Role | Pass criterion | What a fail means |
|---|---|---|---|---|
| **A — known-null** | Known **LINEAR** cap: C0G/NP0 ceramic or PP film, ~1–10 nF | Must read **flat** C(V) across ±10 V | `\|ΔC/C\|` across full bias ≤ stated floor (target: ≤ 0.1%, set by stage C) | A bias-dependent systematic exists (AO bias-tee leakage, AI input-bias current, sense-R thermal drift, dielectric absorption) — that slope IS the C(V) false-positive floor; subtract or fix before B |
| **B — known-positive** | Known **NONLINEAR** cap with a **datasheet C-V curve**: a Class-2 X7R/X5R MLCC (DC-bias derating curve) OR a varactor diode (C-V table) | Must **recover the datasheet** C(V) within tolerance | Recovered C(V) matches datasheet within stated datasheet tol (typ. ±10–20% MLCC; ±5% varactor) over the bias range | The extraction is biased (wrong sense-R, lock-in phase error, probe-amp out of small-signal) — the chain mis-reads a *known* nonlinearity, so it cannot be trusted on an unknown |
| **C — instrument floor** | Open-channel / stable-reference: shorted, open, and a stable known cap, recorded over the full integration window | **Free-drift noise floor**, stated BEFORE any discriminating read | Report `σ_C` (C-extraction drift) and its allan-variance vs integration time | This IS the bench's resolution floor; any C(V) feature within ~3× of it is UNRESOLVED, never a result (apparatus-floor A-bis: floor gate adjudicates FIRST) |

**A-ter probe-capability note:** the known-positive (Stage B) must exercise the *discrimination axis* the
bench claims to measure — i.e. it must have a **shape** the extraction can resolve, not just a magnitude
offset. A datasheet MLCC derating curve (a real falling arc) is the right known-positive; a second linear
cap is not (it can't confirm the chain reads *shape*).

---

## §5 — Measurement design (lock-in quadrature C extraction)

**Principle.** At each DC bias `V_DC`, superpose a small AC probe `v_ac·sin(ωt)` and measure the DUT
current. The **quadrature** (90°, leading V) component is capacitive: `I_Q = ω·C_eff(V_DC)·v_ac`, so
`C_eff(V_DC) = I_Q / (ω·v_ac)`. The **in-phase** component gives the loss `G = I_I/v_ac`. Sweep `V_DC`.
This reads the **small-signal differential capacitance** `dQ/dV` — the §0 observable (a), NOT the bulk
rupture-compliance (b).

**4×4 phase-coherent channel plan (NI-9263 AO ×4, NI-9215 AI ×4, common 100 kS/s clock):**

| Ch | Signal | Purpose |
|---|---|---|
| AO0 | `V_DC + v_ac·sin(ωt)` → DUT | bias + probe drive (summed in software, single AO) |
| AO1 | `v_ac·sin(ωt)` → reference cap | ratiometric reference drive (phase-locked to AO0) |
| AO2 | guard / cancellation drive (optional) | common-mode / cable-capacitance null |
| AO3 | spare | reserved (e.g. temperature-cell drive) |
| AI0 | DUT current sense (across sense-R or TIA) | the measured `I(V_DC, t)` |
| AI1 | reference-cap current sense | ratiometric denominator (cancels lock-in gain + clock drift) |
| AI2 | DUT voltage monitor | true applied V (closes the bias loop; corrects AO loading) |
| AI3 | spare / temperature monitor | drift attribution |

**Ratiometric extraction** (DUT vs reference cap) cancels common-mode gain/clock/thermal drift — the
single most important systematic reducer; report `C_DUT/C_ref`, not raw `C_DUT`.

**Expected SNR (canonical bench params, computed this session):** with `v_ac = 0.1 V`, `C ~ 1–100 nF`,
`ω/2π = 1–40 kHz`: `I_Q = ω·C·v_ac` spans **6.3 µA → 2.5 mA** — comfortably inside NI-9215 ±10 V with a
sense resistor (e.g. `I_Q·R_sense` set to ~1 V full-scale). 16-bit AI over ±10 V → ~0.3 mV LSB; with
lock-in integration (`N` samples) the C-extraction SNR improves as `√N`, putting sub-0.1% `ΔC/C`
within reach at multi-second integration (to be confirmed empirically as Stage C, not assumed).

**Probe-amplitude linearity (the S11 lesson, A-Rule small-signal corollary):** sweep `v_ac` (§7) and
confirm extracted `C_eff` is **probe-amplitude-independent**. If `C` depends on `v_ac`, the probe is
NOT small-signal (it is itself driving the nonlinearity) and the "C(V)" is a large-signal average, not a
differential capacitance — a contamination that must be excluded before any FORM comparison.

---

## §6 — ORDERED BINS (floor gates FIRST, per apparatus-floor A-bis)

The floor gate adjudicates **before** any AVE-vs-standard form claim is evaluated. A sub-floor "match"
is UNRESOLVED, never a form verdict.

1. **APPARATUS (floor gate — evaluated FIRST).** Did Stage A read flat to floor, Stage B recover the
   datasheet, and is the candidate C(V) feature **> 3× the Stage-C drift floor**? If NO on any →
   **UNRESOLVED / APPARATUS.** Stop; the read is the bench, not physics. (No AVE/STANDARD verdict is
   even computed.)
2. **AVE-FORM.** Above floor AND the material C(V) arc matches the `(1−x²)^(±1/2)` kernel form (sign
   per §0, shape over the reachable x-range) **distinguishably better** than the standard forms, with a
   self-consistent fit `V_local` → **consistency-class support** for the kernel SHAPE (Class C, §8).
   NOT an emergence claim.
3. **STANDARD-FORM.** Above floor AND the C(V) arc matches a standard varactor / Devonshire-ferroelectric
   form **better** than the AVE kernel form → the AVE form is **not supported** for this material.
4. **INDISTINGUISHABLE-AT-PRECISION.** Above floor BUT both AVE and standard forms fit within bench
   precision over the reachable bias range → **cannot separate.** (This is the *expected* outcome for
   Branch F at modest x, and the *certain* outcome for the vacuum claim per §3.)

**Pre-registered expectation:** vacuum claim → bin 1/4 by construction (§3). Material analog → most
likely bin 4 (Branch F shape-degeneracy) unless the bench reaches `x ≳ 0.5` of `V_local` with
sub-0.1% precision, in which case bins 2/3 become decidable at consistency-class.

---

## §7 — Knob inventory + sweep plans (`ave-sweep-audit`)

Every knob that could *set* the number is inventoried; each is swept or bounded.

| Knob | Range / plan | What it controls / could masquerade as |
|---|---|---|
| **Probe amplitude `v_ac`** | sweep 10 mV → 1 V (≥1 decade) | small-signal linearity gate (§5); a `C(v_ac)` dependence = large-signal contamination |
| **DC bias `V_DC`** | 0 → ±10 V, bidirectional (hysteresis check), step ≤ 0.1 V near features | the C(V) sweep axis itself; bidirectional sweep separates material hysteresis from a static arc |
| **Frequency `ω/2π`** | 1, 3, 10, 30, 40 kHz | dielectric-relaxation dispersion (a `C(ω)` slope = material Debye relaxation, NOT a kernel feature); also separates series-R/ESL artifacts |
| **Integration time `τ_int`** | 0.1 → 10 s (Allan-variance) | the Stage-C noise floor vs speed tradeoff; sets the resolved `σ_C` |
| **Sense-R / TIA gain** | choose for ~1 V full-scale `I_Q` at nominal C | current SNR; a gain-dependent C = extraction-chain error |
| **Reference cap value** | match to DUT order | ratiometric common-mode cancellation quality |
| **Temperature** | record (AI3); bound drift | a `C(T)` drift mistaken for `C(V)` (thermal coupling to bias) — Class-2 caps are strongly `C(T)` |

---

## §8 — Honest scope: what a positive would and would NOT mean (emergence criterion)

**A positive (material C(V) matches the AVE kernel FORM) WOULD mean:** the material's
voltage-coefficient-of-capacitance is **consistent with the saturation-kernel quarter-arc SHAPE** — a
**Class-C consistency** result (an alternative-mechanism reproduction; the PONDER-05 reading at
`op14:106` / INVARIANT-S2). The novelty is that AVE *predicts the shape class* of nonlinear-dielectric
saturation; the bench would confirm a real material lands in that class.

**A positive WOULD NOT mean:** (i) the **vacuum** Axiom-4 kernel was measured — it is ~20 OOM out of
reach (§3); (ii) the kernel form is **parameter-free-validated** — `V_local` is a fit parameter for a
real material, so the match is degenerate with any one-parameter saturating arc unless the SHAPE is
distinguished at high precision over wide `x`; (iii) anything about the §0 sign tension is resolved by
the data alone — the bin boundary depends on Grant's adjudication, not the measurement.

**Emergence criterion (state explicitly, per `consistency-vs-emergence`):** the FORM result would rise
to **Class D / emergence** only if BOTH (a) `V_local` were **derived parameter-free** from the material's
own substrate properties (NOT fit to the C-V data) AND (b) the `(1−x²)^(±1/2)` form were **distinguished
from all competing saturating arcs** (power-law, Devonshire-tanh) at the bench's precision over
`x ∈ [0, ~0.9]`. Absent both, the headline is **consistency-class, full stop** — and saying so is the
discipline working, not a weakness.

---

## §9 — Classifications (consistency/emergence · phase-space · regime/phase-state)

**`consistency-vs-emergence` class tags (per observable):**

| Observable | Class | Rationale |
|---|---|---|
| Vacuum kernel `δε/ε₀(V)` on the cRIO | (untestable) | ~20 OOM below floor; no class — not a test (§3) |
| Material C(V) **shape**-match to kernel FORM | **C — consistency** | alternative-mechanism reproduction; `V_local` fit; PONDER-05 reading |
| Stage-A flatness, Stage-B datasheet recovery | **identity / calibration** | instrument qualification, not a physics claim |
| Kernel FORM itself (as a prediction *about* saturation media) | **B — axiom manifestation** | the quarter-arc is Axiom 4 expressed at material scale; not derived-from-scratch here |

No Class-D / emergence headline is available from this bench. Per A47 family: this test's inputs route
through the material's own (fit) `V_local`, so it cannot be emergence-class — flagged so it is never
promoted as "AVE derives capacitor C(V)."

**`phase-space-coordinate-check` note (A46):** the kernel coordinate `A = A/A_yield` is a **per-node
operating-point amplitude** (phase-space-like), not the lab voltage. The dielectric specialization
`A = V/V_yield` is a *per-node* identity, and the bench measures lab voltage across `~10³–10⁷` node
lengths. The prereg keeps these explicit (§3.1) — the lab-voltage C(V) is compared to the kernel form
**only after** the per-node `x` mapping is stated, never lab-V directly against an `A`-coordinate
prediction. (This is the same per-node-vs-apparatus conflation the corpus flags at
`op14-local-clock-modulation.md:106` + `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2, cross-referenced
to the `vol4/claim-quality.md:51` V_yield-vs-V_snap reading hazard.)

**`ave-regime-phase-state-check` declaration:** MODE = capacitive / ε-sector (static-E-only =
**ASYMMETRIC** load, INVARIANT-S2: `S_ε<1, S_μ=1`). REGIME (vacuum sector) = **deep Regime I (linear)**,
~9 OOM below `R_I` (§3.1). REGIME (material sector) = the material's own near-saturation, reachable.
PHASE-STATE = quasi-static / fully-relaxed (~16 OOM below thixotropic crossover, §3.3). A null on the
*vacuum* kernel here is an **artifact-of-regime** (the effect can't exist at this field), NOT a
falsification — exactly the dark-wake-Phases-1-5 lesson.

---

## §10 — Corpus citations (verify-before-cite, grepped this session)

- Frozen form Branch R: `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md:21,27,32-39` (clm-vjv4zf, clm-8nkvwy)
- Frozen form Branch F + per-node discipline: `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2; `2026-06-03_yield-knee-map-prereg.md:8,41,44,48`
- Kernel → wave-speed → clock: `op14-local-clock-modulation.md:29,31,61,106` (clm-1eg13f)
- 2ω even-harmonic companion: `parametric-coupling-kernel.md:70-80`
- V_yield vs V_snap + per-node-vs-apparatus reading hazard: `vol4/claim-quality.md:51` (clm-0vxzfu); LIVING_REFERENCE Critical Distinction #1
- Apparatus-floor / validate-on-known-cap-first: this bench is the encoding anchor of `ave-apparatus-floor-attribution` (SKILL.md:109)
- Constants: `src/ave/core/constants.py` — `V_YIELD, V_SNAP, E_YIELD, L_NODE, ALPHA, R_I, R_II, R_III`

## §11 — Open decisions for Grant (gate to freeze)

1. **§0 sign-of-slope adjudication** (Branch R rising vs Branch F falling) — sets the AVE-FORM/STANDARD-FORM
   bin boundary. **Blocking** for §6 bin pinning.
2. **Is Branch R a rupture-compliance observable the small-signal bench does not measure?** (§0 physical
   note) — if yes, the bench-relevant prediction is Branch F only, and the R/F tension is *scope*, not
   contradiction.
3. **Bench framing confirmation:** accept the honest scope that the cRIO first experiment is a
   **validation-ladder + material-analog consistency bench** (the calibration rung for a future
   high-field AVE C-V / autoresonant bench per Q-G42), NOT a vacuum-kernel discriminator.
4. **DUT selection for Stage B/material analog:** Class-2 MLCC (X7R/X5R) vs varactor diode — which
   datasheet anchors the known-positive.

**This document does not freeze until Grant schedules bench time.** Per substitution-not-retraction
(Rule 12): if the §0 tension resolves against the bench's observable, this prereg is amended (preserve
body, add header), not refilled with a new untested claim.
