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

Driver `src/scripts/vol_1_foundations/swept_gamma_omega_A2.py`; outputs
`swept_gamma_omega_A2_results.json` + `..._tongue_map.png`. Grid: A²∈[0.01,0.97]×49,
ω_drive∈[0.20,3.00]×141 ω_C; Floquet monodromy, 4000 RK4 steps/pump-period.

### §6.1 GAIN — the 4× pump IS a parametric tongue (Outcome A confirmed)

The lossless `(A², ω_drive)` Floquet surface shows a single **principal instability tongue**.
Its ridge (the ω_drive of max gain per A²) tracks the **Op14-softened** prediction
`ω_drive = 2ω_C√(1−¼A²)`:

| A² | ridge measured (ω_C) | Op14 predict `2ω_C√(1−¼A²)` |
|---|---|---|
| 0.19 | 1.940 | 1.952 |
| 0.49 | 1.860 | 1.873 |
| 0.79 | 1.720 | 1.792 |

mean `|ridge − Op14pred| = 0.042 ω_C` over the resolved tongue. **The tongue peaks near `2ω_C`
(at A²→0) and bends DOWN as A² rises** — the Op14 local-clock signature (CP5); a bare no-Op14
tongue would be a vertical line at fixed `2ω_C`. The amplified signal / self-oscillation is at the
**sub-harmonic `ω_drive/2 ≈ ω_C` — the Compton clock.** So the pump is at `2ω_C`, the clock is `ω_C`.

`max|λ| = 1.575 > 1` on the ridge ⟹ **positive Floquet exponent ⟹ exponential growth.** On the
**lossless** engine the principal tongue reaches the ω-axis (**zero threshold**): gain is unbounded
for **all A² > 0** on the ridge. **This IS the lossless-parametric artifact = the 4× pump** (the
engine's observed `10⁴–10⁷×` energy blow-up = `1.575×/period` compounded over the run). ✓ Outcome A.

*(Honest caveat: at A²=0.79 the measured ridge 1.720 sits BELOW the leading-order 1.792 — the exact
non-Taylor `⟨S(A(t))⟩` softens faster than `1−¼A²`, so the real down-bend is even stronger than
leading order. The discriminating fact — tongue at `2ω_C`, bending down — is robust.)*

### §6.2 CAVITY — the SECOND threshold the 1-D cuts conflated

Static Op3 reflection `|Γ_Op3(A²)| → 1 only as A²→1` (S→0). low-Z (canonical short) `Γ(0.23) = −0.033`
**matches optionD 1× (`Γ_min = −0.011`, "matched bulk, no wall")**; the wall (`|Γ|>0.9`) forms only at
**A² ≳ 0.999**. So there are **TWO distinct thresholds**, which the genesis 1-D amplitude cuts saw only
in combination:
- **(i) parametric-GAIN** threshold: any A² > 0 (lossless tongue).
- **(ii) CAVITY-formation** threshold: A² → 1 (the Γ=−1 wall that traps the gain).

The genesis "amplitude-gating" verdict IS this decomposition: **1× (A²=0.23) = gain present but no
cavity** → the mode leaks/disperses before the gain compounds; **4× (amplitude ×4 = A²×16 → A²→1,
rupture R_III) = gain AND cavity** → the Γ=−1 wall traps the always-present gain → runaway pump.
Neither fixed-amplitude cut could resolve that gain and cavity are **separate axes**.

**FLAG-POLARITY (for Grant):** observed Γ is **negative** (low-Z / short, canonical Meissner μ-branch),
matching the optionD asymmetric kernel. The engine's 4× `Γ=−0.994` is **steeper** than the symmetric
low-Z toy at A²=0.97 (`−0.41`) — the asymmetric μ-wall (`Z_μ→0`) shorts faster than the symmetric
`Z=Z₀√S`. Sign + steepness flagged; **does not change the gain** (pump depth is the `|1/C_eff|`
modulation, polarity-independent).

### §6.3 α-READOUT — the headline (consistency-vs-emergence, as pre-registered §3)

- **GAIN is α-DECOUPLED.** The pump depth (`¼A²`), the ridge (`2ω_C√(1−¼A²)`), and the entire Floquet
  surface were computed with **ZERO α input** — pure geometry of `S(A)=√(1−A²)`. This is **NOT** the
  circular `p_c=8πα` failure mode (A47 v17) and **NOT** keyed to α via a `κ_chiral=α·κ̃` primitive.
  The gain is genuine topology/geometry. **Class D-eligible structure.** ✓
- **Q=1/α is α-ENCODED.** To land `Q=ω_C/γ=1/α` the loss must be **set to `γ=α·ω_C` by hand**.
  Theorem-3-1 Path A (`:21-40`) derives `Q=1/α` by **substituting the SI definition `α=e²Z₀/(4πℏ)`**
  into the reactance (`ω_C·L_e=ℏ/e²=Z₀/(4πα)`; `Q=4πℏ/(e²Z₀) ≡ α⁻¹` by CODATA ℏ,e,Z₀). So **"α=1/Q"
  is α-in → α-out** — **Class A/C identity/consistency, NOT an emergence of 137.036.** Reporting it as
  emergence would be the exact A47 `p_c=8πα` failure mode.
- **The honest split:** parametric **STRUCTURE** (gain) = α-free geometry; parametric **SCALE** (where the
  threshold sits → Q → operating amplitude) = α-encoded via the loss. The separate geometric
  `α⁻¹=4π³+π²+π` (Golden-Torus mode-count, theorem-3-1 Path B) is a **DIFFERENT axis** — not the
  parametric Q; do not conflate.

### §6.4 LOSS (STRETCH) — a BOUNDED threshold appears with the dark-wake

Adding a loss γ lifts the principal tongue off the ω-axis: a **BOUNDED threshold locus `γ*(A²)`**
appears (the gain=loss curve), rising with A² (more gain needs more loss to bound). **YES — Fork A's
stable window exists once the loss is restored.** At `Q=1/α` (`γ=α·ω_C`), the self-selected gain=loss
amplitude is **`A²_self ≈ 0.057 ≈ 8α`** (within 2%; scaling `A²_self ∝ α`, **α-encoded via the loss**,
NOT an α-free prediction).

**Does the electron operating point sit ON it?** The m_ec²-calibrated impose is at `A²≈0.23` — **above**
`A²_self≈0.057` (ratio `0.23/0.057 ≈ 4.0`). This is **suggestive** of Fork A's "~4× apart" calibration
crux, but **flagged as an observation for Grant, NOT a closed claim** (the rest-energy-to-threshold
ratio and the amplitude-scale-to-cavity "4×" are different ratios; over-reading a 4≈4 coincidence is
exactly the coincidence-magnet tell). **Caveat:** this stretch uses a TOY damping γ — it demonstrates a
bounded locus EXISTS for any loss; it does **not** show the *real* dark-wake `τ_zx` produces `Q=1/α`.
That is the genuine emergence test and the immediate next driver (§7).

## §7 VERDICT

**The four return questions:**

1. **Is the 4× pump a parametric tongue (peaks at ω≈2ω_C)? — YES.** A single principal Floquet tongue,
   ridge at `2ω_C` (A²→0) bending down as `2ω_C√(1−¼A²)` (Op14); signal/self-osc at the sub-harmonic
   `ω_C` (Compton clock). Lossless `max|λ|=1.575>1` → unbounded ridge = the 4× pump. The 1-D genesis
   cuts couldn't resolve it because they sampled fixed (A², ω) points on a 2-D surface.

2. **Q(A²) at the operating point — is it 1/α? α-decoupled or α-encoded? — Q≈1/α STRUCTURALLY, but the
   GAIN is α-DECOUPLED (geometry) while Q=1/α is α-ENCODED (the loss carries α).** The honest headline:
   the parametric gain is genuine α-free topology/geometry (good — not the circular `p_c=8πα` mode), but
   "α=1/Q" is α-in→α-out (theorem-3-1 inserts the SI α definition into the loss). **The characterization
   does NOT derive α; it does not let an α-encoded primitive masquerade as deriving α.**

3. **Does a bounded threshold locus appear with the dark-wake loss? Electron on it? — A bounded locus
   appears with a TOY loss (YES, Fork A's window exists); at Q=1/α the self-osc amplitude is A²≈8α≈0.057.
   "Electron on it" is UNRESOLVED** — pending feeding the *real* dark-wake `τ_zx` (α-free geometry) into
   the EOM. The operating point A²≈0.23 sits ~4× above the toy-loss threshold (suggestive of Fork A's
   calibration crux; flagged, not closed).

4. **Verdict — does the characterization dissolve Fork A? — YES, the amplitude/resonance Fork A is
   dissolved.** The "4× pump" is not a pathology to debug away: it is the **lossless-parametric tongue**,
   the necessary artifact of running genesis with the dark-wake back-reaction switched off
   (`DarkWakeObserver` observed-not-fed-back, `vacuum_engine.py:1457`). The genesis fork structure
   collapses into: *(i)* an always-present α-free parametric gain, *(ii)* a cavity that forms only at
   A²→1, and *(iii)* a missing loss. **Caveat held:** this dissolves Fork A (amplitude/resonance) ONLY —
   the `(2,3)` topological closure (Fork D / C3) is a **separate (V_inc,V_ref) phase-space axis** this
   real-space sweep does **not** touch. The genesis is **not** closed.

**Immediate next driver (the genuine emergence test):** feed the real `DarkWakeObserver` `τ_zx`
back-EMF (the α-free, geometry-set loss; `M_inertial≡L_drag`) into the bond-LC / Cosserat EOM and
re-measure Q at the gain=loss threshold. **If the α-free dark-wake produces Q=1/α**, that is a genuine
α emergence (α-free loss → α-encoded Q out) — the first non-circular route. **If the dark-wake magnitude
is a free knob**, Q=1/α is calibration. This is the test the §6.3 split makes well-posed; it does NOT
solve α (deriving 137 has eluded everyone — do not overclaim). Pair with the **FLAG-POLARITY** (Fork B)
and **calibration-crux** (Fork A rest-energy-vs-threshold) adjudications for Grant.

---

**Status: §1–§4 frozen pre-run; §6–§7 post-run. Outcome A (parametric tongue) confirmed. Fork A
dissolved (amplitude/resonance axis). α NOT derived (gain α-decoupled / Q=1/α α-encoded — honest
consistency, not emergence). `(2,3)` phase-space closure untouched (caveat held). Next: dark-wake
back-EMF into the EOM.**
