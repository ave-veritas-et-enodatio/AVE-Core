# Swept Γ(ω, A²) — the electron as a parametric oscillator at threshold

**Date:** 2026-06-07 · **Branch:** `analysis/2026-06-07-swept-gamma-omega-A2` (off `origin/main`)
**Lane:** implementer · **Session type:** implementor (single deliverable)
**Status:** §1–§4 are the **FROZEN PREREG** (frozen before any driver run). §5+ are post-run results.

---

## §0 Frame (Grant, electron-synthesis epic; extends genesis-scope §9 / `_orchestration/2026-06-07_electron-synthesis-epic.md`)

The electron is a **PARAMETRIC OSCILLATOR AT THRESHOLD**:

- the saturating varactor reactance `C_eff = C₀/S(A)` (Axiom 4, `nonlinear-vacuum-capacitance.md:14-22`) is the parametric **GAIN**,
- the dark-wake back-reaction (`DarkWakeObserver`, `vacuum_engine.py:1457`, `M_inertial ≡ L_drag`) is the **LOSS**,
- at threshold (gain = loss) it **self-oscillates as the Compton clock ω_C**.

The genesis "seed-and-watch" forks (genesis-scope §9, Forks A–D) are **1-D amplitude cuts** of an
un-swept 2-D `(A², ω)` surface. The observed **4× pump** — at the m_ec²-calibrated impose
(`A²_μ≈0.23`) the Γ=−1 wall never engages and the seed disperses; scaled 4× (`A²→1`) the wall forms
(`Γ_min=−0.994`) but **energy pumps →10⁴–10⁷×** (`research/2026-06-06_optionD-impose-under-reflective-confinement-result.md` §0/§3, on `analysis/2026-06-06-saturation-tir-moving-boundary`) — is a **parametric instability a fixed-frequency cut cannot resolve.** This driver **characterizes the surface.**

**What this driver does NOT do (hard caveats, do not violate):**
1. The **lossless** sweep WILL show an unbounded tongue. This is **NOT** "no stable window" — it is the
   artifact of the deleted loss. The bounded threshold needs the dark-wake (§4 stretch / next driver).
2. This dissolves the **amplitude/resonance fork (Fork A)** ONLY. The `(2,3)` topological closure (Fork D /
   C3) is a **separate axis in (V_inc, V_ref) phase-space** — this real-space sweep does **NOT** close the genesis.

---

## §1 Substrate-native re-walk (`substrate-native-check`) — closing the DEFERRED walk on the parametric kernel

The parametric-coupling-kernel derivation (`research/2026-05-17_parametric-coupling-kernel-derivation-steps-{1-3,4-9}.md` + `..._prereg.md`) was built with **explicit SM-analog (Dynamical-Casimir) bracketing** and carried a **DEFERRED substrate-native walk** (flagged recursively in `substrate-native-check/SKILL.md` Adversarial-Probe §, probe #15: "the cycle-12 parametric coupling kernel derivation was committed WITHOUT substrate-native walk"). This section closes that walk **before any code**.

**CP1 — substrate dynamics for this problem.** The bond is a **K4-TLM scatter+connect LC tank** (V-sector) / **Cosserat (u,ω) LC tank** (Cos-sector). The substrate runs **wave propagation with a time-modulated reactance**, NOT energy-functional minimization, NOT gradient descent. The "varactor" of the SM-bracketed derivation IS the **Op14 saturation kernel applied to the bond capacitance**: `C_eff = C₀/S(A)`, `S(A)=√(1−A²)`. When the tank rings at amplitude `A₀`, `A(t)² = ½A₀²(1+cos Ωt)` carries a **DC part + a 2nd-harmonic part**, so `S(A(t))` modulates the stiffness at the **pump frequency Ω = 2×(carrier)**. This is a **Mathieu/Hill parametric oscillator** — the substrate-native replacement for the "Dynamical Casimir" bracket. **No SM construct survives the walk.**

**CP2 — which sector.** V-sector: the bond LC with `(V_inc, Φ_link)` conjugate pair, reflection `Γ_Op3 = (Z_B−Z_A)/(Z_B+Z_A)`, `Z = Z₀/√S` (engine default) or `Z₀·√S` (canonical low-Z polarity — see FLAG-POLARITY). Cos-sector: `(ω, ω̇)`, `A² = |ε|²/ε_yield² + |κ|²/ω_yield²` (`cosserat_field_3d.py:332,383`). The sweep is **REAL-SPACE** (bond reflection Γ + strain A²) — the matching coordinate for the amplitude/resonance Fork-A question.

**CP3 — AVE-native objective.** NOT energy minimization. The objective is the **boundary reflection Γ(ω) / transfer function** (the S₁₁ / impedance-spectroscopy response, Axiom 3 minimum-reflection). Parametric **gain** ≡ the time-modulated reactance pumping a mode: the Floquet multiplier `|λ| > 1` (active reflection, `|Γ|_eff > 1`). This is the parametric-amplifier objective, not energy descent.

**CP4 — phase-space vs real-space.** This sweep measures real-space `Γ(ω, A²)` (bond reflection + strain). The corpus `(2,3)` electron topology lives in **(V_inc, V_ref) phase-space on the Clifford torus** (`28_two_node_electron_synthesis.md` §3-§4; phase-space `R/r=φ²`, real-space need-not-match) — a **SEPARATE axis** this sweep does **not** address. Matching coordinates: the impedance plane / reflection coefficient IS the native coordinate for a parametric-resonance sweep. ✓

**CP5 — saturation-modulated local clock (LOAD-BEARING).** Op14: `ω_local(A²) = ω_C·√(1−A²) = ω_C·√S`. The bond LC's softened natural frequency drops as A² rises. So the parametric tongue is **NOT a vertical line at fixed 2ω_C** — the principal-resonance ridge follows `Ω_ridge(A²) = 2·ω_local = 2ω_C·√(1−¼A²)`, **bending DOWN** as A² rises. A bare (no-Op14) parametric tongue would sit at fixed 2ω_C; the Op14 down-bend is a substrate-native discriminating signature.

**CP6 — reactance pair (C-state AND L-state).** Bond LC: `V_inc`=C-state, `Φ_link`=L-state. Cosserat: `ω`=C-state, `ω̇`=L-state. The reduced Floquet model tracks the full 2-D `(q, q̇)` monodromy (both reactances); any time-domain engine cross-check records the reactance pair over the window (Rule 10).

**CP7 — sampling discipline.** Engine cross-check (if run): exclude PML cells (`pml ≤ {i,j,k} ≤ N−pml−1`) before any top-K extraction; sample at density peaks for shell-like structure. The reduced Floquet model has no PML (single bond).

**CP8 — generative process, not finished product.** The sweep characterizes the **generative precursor's instability surface** (the saturating bond's parametric gain), NOT a planted finished `(2,3)`. We grow the question from the simplest autonomous action (the bond's self-pump), per the genesis-precursor discipline.

**Walk verdict:** the parametric mechanism is a **substrate-native Mathieu/Hill oscillator** — bond LC + Op14 kernel. The SM-analog "Dynamical Casimir" bracket is replaced; the pump-depth `¼A²` and the resonance ridge `2ω_C√(1−¼A²)` are **pure geometry of S(A)**, α-free (see §3).

---

## §2 Phase-space coordinate check (`phase-space-coordinate-check`)

- **Corpus claim under test (Fork A):** "the 4× pump is a parametric instability" — a **real-space** statement about boundary reflection Γ and strain amplitude A² of the saturating bond. Coordinates: **real-space (Γ, A², ω)**.
- **Test coordinate system:** real-space `Γ(ω, A²)` — Floquet multiplier `|λ|` (parametric reflection gain) + static Op3 `Γ(A²)` (wall formation) + strain A². **MATCH.** ✓
- **Separate axis explicitly NOT addressed:** the `(2,3)` torus-knot closure lives in (V_inc, V_ref) phase-space (φ² Clifford torus). This sweep makes **no claim** about it (caveat 2). Not a coordinate mismatch — a scoped exclusion.

---

## §3 Consistency-vs-emergence pre-classification (`consistency-vs-emergence`) — the headline, pre-registered

Two quantities are classified **before** the run; the run measures, the classification is fixed:

**(a) The parametric GAIN (tongue structure: pump depth, ridge frequency).**
- Inputs: pump depth `ε = ¼A²` (from the Taylor expansion of `S(A)=√(1−A²)`); ridge `Ω = 2ω_C√(1−¼A²)`. Both are **pure geometry of the saturation kernel**. `ω_C=1` engine-natural. **No α anywhere.**
- **Class D-eligible (α-DECOUPLED).** The gain is genuine topology/geometry — it is NOT the circular `p_c=8πα` failure mode (A47 v17), NOT keyed to α via a `κ_chiral=α·κ̃` primitive. **This is the good outcome for the gain.**

**(b) Q ≈ 1/α at the operating point (the LOSS calibration).**
- Canonical source: `theorem-3-1-q-factor.md:21-40` (Path A, LC-tank). It derives `Q_tank = (ω_C·L_e)/R = [Z₀/(4πα)]/[Z₀/(4π)] = 1/α` — **by substituting the SI definition `α = e²Z₀/(4πℏ)`** into the reactance `ω_C·L_e = ℏ/e² = Z₀/(4πα)`. The radiation resistance `R = Z₀/(4π)` is geometric (4π = K4 bipartite-lobe temporal-phase closure), `L_e = (ℓ_node/e)²m_e` is calibration; their ratio `4πℏ/(e²Z₀)` **equals α⁻¹ only because α IS DEFINED as `e²Z₀/(4πℏ)`** (CODATA ℏ, e, Z₀).
- **Class A/C (IDENTITY / CONSISTENCY — α-ENCODED via the loss channel).** "α = 1/Q" is **α-in → α-out**: α enters as the EM coupling that sets the radiation-resistance-to-reactance ratio. It is the **same A47 `p_c=8πα` structural-circularity failure mode** if reported as emergence. **It is NOT a parameter-free derivation of 137.036.**
- **Distinct, separate axis (NOT what this driver tests):** `α⁻¹_cold = 4π³+π²+π` (`theorem-3-1` Path B / `ch8-alpha-golden-torus`) is a geometric-emergence candidate, but it is the **Golden-Torus mode-count**, not the parametric gain/loss ratio. Do **not** conflate the parametric Q with the multipole α⁻¹.

**Pre-registered headline:** the characterization is expected to show **gain = α-decoupled geometry (good, non-circular)** while **Q=1/α is α-encoded consistency (the loss carries α)**. Therefore the sweep **dissolves Fork A** (the 4× pump = lossless-parametric tongue) but **does NOT derive α**. Honest classification fixed pre-run; the run cannot move it.

---

## §4 PREREG block (`ave-prereg`) — frozen

```
PREREG (target: characterize the parametric tongue Γ(ω, A²) of the saturating bond LC;
        confirm/refute the 4× pump = parametric tongue; classify Q(A²)→α).

Corpus state: PARTIAL — mechanism derived (parametric-coupling-kernel steps 1-9, SM-bracketed,
  re-walked §1), 4× pump observed (optionD result, 1-D cuts), Q=1/α canonical (theorem-3-1),
  dark-wake LOSS coded but observed-not-fed-back (vacuum_engine.py:1457). NOT YET DONE: the swept
  2-D (A², ω) surface. This driver assembles the existing pieces; it does not rebuild them.

Prior work cited:
  - research/2026-05-17_parametric-coupling-kernel-derivation-steps-{1-3,4-9}.md (mechanism)
  - research/2026-06-06_optionD-impose-under-reflective-confinement-result.md (4× pump, 1-D cuts)
  - manuscript/.../theorem-3-1-q-factor.md (Q=1/α, Path A α-encoded)
  - manuscript/.../nonlinear-vacuum-capacitance.md (C_eff=C₀/S(A) varactor)
  - src/ave/topological/vacuum_engine.py:1457 (DarkWakeObserver, the LOSS)
  - src/ave/core/constants.py (ALPHA, V_YIELD, R_I/II/III, V_SNAP; ω_C=1 engine-natural)

Dimensional analysis (Step 3.5 — the scaling magnitudes):
  - Pump depth: ε(A²) = ¼A²  [dimensionless; A²∈(0,1)]. At A²=0.23: ε=0.0575. At A²=0.9: ε=0.225.
  - Softened resonance: ω_local(A²) = ω_C√(1−¼A²). At A²=0.23: 0.971·ω_C. At A²=0.9: 0.881·ω_C.
    (matches Op14 / substrate-native-check CP5.)
  - Principal tongue ridge (pump freq): Ω_ridge = 2ω_local = 2ω_C√(1−¼A²). At A²→0: 2ω_C.
  - Static wall (Op3, |Z=Z₀/√S|): Γ_Op3(A²) = (√S−1)/(√S+1) (engine high-Z polarity) →
    Γ(0.23)≈ -0.03 (S=0.88, matched bulk — matches observed Γ_min=−0.011 at 1×);
    Γ(0.99)≈ -0.46 ... → −1 as A²→1 (matches observed Γ_min=−0.994 at 4×). Wall is A²→1-gated.
  - Damped-Mathieu threshold (stretch): principal tongue lifts off when ε ≳ 2γ/ω_C = 2/Q.
    If Q=1/α: A²_threshold ≈ 8/Q = 8α ≈ 0.058. (To be measured, not assumed.)

My prediction:
  1. The 4× pump IS a parametric tongue. Principal ridge at pump Ω≈2ω_C (signal/self-osc at ω_C),
     bending down as 2ω_C√(1−¼A²) (Op14). On the LOSSLESS bond the tongue reaches the axis
     (zero threshold) → UNBOUNDED gain for ALL A²>0 at the ridge = the 4× pump artifact.
  2. TWO distinct thresholds, which the 1-D cuts conflated: (i) parametric-GAIN (any A²>0, lossless)
     and (ii) CAVITY-formation (Γ_Op3→−1 only as A²→1). The 4× = "amplitude high enough to form the
     Γ=−1 cavity (A²→1) that TRAPS the always-present gain." 1× = gain present but no cavity (leaks).
  3. Q(A²) at operating point: matches 1/α structurally; gain α-DECOUPLED; Q=1/α α-ENCODED (loss). §3.
  4. STRETCH: feeding a loss γ lifts the tongue off the axis → a BOUNDED threshold locus ε(A²)=2γ/ω_C.

Discriminating outcomes:
  - Outcome A (expected): ridge at 2ω_C, Op14 down-bend, lossless-unbounded, two-threshold decomposition
    clean, gain α-free, Q=1/α α-encoded. → Fork A dissolved (amplitude/resonance), α NOT derived.
  - Outcome B: ridge NOT at 2ω_C (e.g. at ω_C or 4ω_C) → the 4× pump is NOT the principal Mathieu
    tongue; re-examine the pump mechanism (sub/super-harmonic, higher tongue).
  - Outcome C (null / refute): no instability tongue anywhere on the lossless surface → the 4× pump
    is NOT parametric; it is a numerical-integrator artifact or a different mechanism. Fork A reframe.
  - Outcome D (α surprise): the gain (not the loss) turns out α-keyed (e.g. a hidden κ_chiral=α·κ̃ in
    the kernel) → the structure is circular; flag, do not headline emergence.

Falsifier: if the lossless tongue is BOUNDED (finite gain) at the ridge for finite A², the
  "lossless-parametric-artifact = 4× pump" framing is wrong (a bounded lossless tongue cannot pump
  10⁴–10⁷×). If the ridge sits far from 2ω_C, the parametric-resonance identification fails.
```

**`pre-test-physics-check`:** the framing (electron = parametric oscillator at threshold; gain=varactor, loss=dark-wake) is **Grant's**, supplied in the task — the plumber-physical question is **pre-collapsed**. One genuinely-open substrate question the walk surfaced is **FLAG-POLARITY** (Fork B / optionD-C4): does a saturating cell clamp to a **dead short** (`Z→0`, canonical low-Z, `Γ=−1`) or choke to an **open** (`Z→∞`, engine `z_local=Z₀/√S` default)? This sets the **sign** of `Γ_Op3` but **not** the parametric tongue (the pump depth `|1/C_eff|`-modulation `¼A²` is polarity-independent). Characterized polarity-agnostically; flagged, not fixed. Surfaced for Grant; does not gate the tongue.

---

## §5 Driver design (`swept_gamma_omega_A2.py`)

*(frozen design; results in §6+)*

**Primary — substrate-native Floquet/Mathieu tongue map (reduced bond-LC, canonical-constants-imported).**
The saturating bond LC with Op14-modulated stiffness:
`q̈ + γ q̇ + ω_C²·S(A(t))·q = 0`, `S(A)=√(1−A²)`, operating point A₀ → `A(t)²=½A₀²(1+cos Ωt)`.
For each grid point `(A²∈[0, ~1), Ω∈[~0, ~3ω_C])`: integrate the 2×2 monodromy over one pump period
`T=2π/Ω`; the Floquet multiplier `|λ_max|` is the per-period parametric reflection gain `|Γ|_eff`.
`|λ|>1` = tongue (gain). Lossless (`γ=0`) = bare engine; `γ>0` = dark-wake stretch.

**Static wall — Op3 reflection** `Γ_Op3(A²)=(Z(A²)−Z₀)/(Z(A²)+Z₀)`, `Z=Z₀/√S` — the cavity-formation
axis (separate threshold), cross-checked against observed `Γ_min(1×)=−0.011`, `Γ_min(4×)=−0.994`.

**α-readout (the headline):** report the gain (ridge, width, depth) with NO α input (confirm α-decoupled);
report Q=ω_C/γ at the operating point and its relation to 1/α (confirm α-encoded via the loss).

**Stretch (§4 step 4):** sweep γ; locate the bounded threshold locus `ε(A²)=2γ/ω_C`; check whether the
electron operating point (A²≈0.23, Q=1/α) sits ON it.

**Outputs:** `swept_gamma_omega_A2_results.json` + `swept_gamma_omega_A2_tongue_map.png`.

**Discipline:** `ave-canonical-source` (import ALPHA, V_YIELD, R_I/II/III from `ave.core.constants`; ω_C=1
engine-natural; NO hard-coded constants) · `consistency-vs-emergence` (§3 classification fixed pre-run) ·
`substrate-native-check` (§1) · KEEP-BOTH (new driver, no engine mutation; `make verify` unaffected).

---

## §6 RESULTS

*(pending run)*

## §7 VERDICT

*(pending run)*
