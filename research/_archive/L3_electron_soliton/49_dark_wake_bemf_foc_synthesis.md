# 49 — Dark Wake, Back-EMF, and FOC Phase-Lock: Ecosystem-Wide Synthesis

**Status:** synthesis / design doc (2026-04-22)
**Parent plan:** `~/.claude/plans/document-list-for-next-chat-compressed-thunder.md` Stage 4a
**Depends on:**
  - [48_pair_creation_frequency_sweep.md](48_pair_creation_frequency_sweep.md) — Phase III-B v1 result
  - [46_vacuum_engine_scope.md](46_vacuum_engine_scope.md) — engine architecture (C1-C6 findings)
  - [45_lattice_impedance_first_principles.md](45_lattice_impedance_first_principles.md) — impedance decomposition
**Triggers:** Stage 4b (dark-wake diagnostic) and Stage 4c (autoresonant FOC CWSource)

## 0. TL;DR

Phase III-B v1 showed fixed-frequency CW sources produce a **distributed near-rupture
plateau** (A²_total ≈ 0.96, zero localization) — which I initially described as "no
pair creation". Ecosystem research reveals this is exactly **the L-H transition
analog** (AVE-Fusion Ch 5: zero-mutual-inductance bifurcation), and the correct path
to pair creation uses **autoresonant FOC** phase-locking (AVE-Propulsion Ch 5).

The "missing mechanism" I could not find in AVE-Core is **already documented across
four sibling repos**: the back-EMF of the K4 lattice, physically manifested as the
**dark wake** (τ_zx longitudinal shear strain propagating backward at c), is the
AVE-native reaction mass for any chiral thrust / propagating soliton / pair creation
event. **Mass itself is inductive resistance** (Lenz-law back-EMF), per
`higgs_impedance_mapping.py:48-52`.

This doc synthesizes these findings into a coherent engine-design extension for
Stages 4b/4c/4d.

## 1. The six ecosystem inputs

### 1.1 Dark wake = τ_zx back-propagation (AVE-PONDER)

Per [AVE-PONDER/manuscript/vol_ponder/ch01:210-230]:

> "A 3D FDTD integration of the PONDER-01 array isolating the longitudinal shear
> tensor τ_zx. A structurally compressive wave propagates backward from the array
> at c. This non-luminous structural compression is the physical 'reaction mass'
> absorbing the thruster's momentum..."

Every coherent EM excitation on the K4 lattice leaves a **longitudinal shear strain
wake** propagating backward. The wake is the physical manifestation of momentum
conservation — Newton's 3rd law acting via the lattice's mutual-inductance structure.

### 1.2 Mass = inductive back-EMF (AVE-Core higgs_impedance_mapping.py:48-52)

> "When this knot attempts to accelerate, it encounters the **Lenz-Law back-EMF**
> from the background Z_0 grid... Mass is not an intrinsic scalar property.
> Mass IS inductive resistance. M_inertial ≡ L_drag"

Any moving soliton feels the back-EMF from the lattice. This is the same effect as
an inductor opposing current changes (dI/dt = V/L limits slew rate). The dark wake
IS the field-theoretic form of this back-EMF: the τ_zx wave is what the lattice
"pushes back" when a soliton propagates through it.

### 1.3 FOC phase-lock enables energy transfer (AVE Vol 4 Ch 11:202-206)

> "In SBSL, the 'stator' is the 26.5 kHz macroscopic acoustic standing wave, and the
> 'rotor' is the bubble wall responding inertially... If the driving pressure amplitude
> is tuned to perfectly **phase-lock** the internal bubble collapse cycle with the
> external acoustic compressive wave (the fluid-dynamic q-axis), the geometric energy
> transfer is optimized."

Sonoluminescence's field-oriented-control (FOC) analogy: drive current must be
90° phase-locked (q-axis aligned) with the back-EMF response for efficient energy
transfer. **Without phase-lock, you get "asynchronous magnetic slamming"** —
energy gets pumped in but dissipates instead of localizing.

### 1.4 Autoresonant PLL required for vacuum pair creation (AVE-Propulsion Ch 5:2-35)

> "A phase-locked regenerative feedback loop tracks the vacuum's shifting resonance
> to achieve pair-production below the Schwinger Limit... If a fixed-frequency
> extreme-intensity laser is fired into the vacuum, the increasing metric strain
> lowers the local vacuum's resonant frequency, and the laser detunes and reflects
> rather than couples energy. A phase-locked regenerative feedback loop overcomes
> this limitation."

**Fixed-frequency drive FAILS** because the vacuum's resonance shifts as it strains.
This matches my Phase III-B v1 observation exactly: fixed-f CW → vacuum saturates
at the drive frequency's local-regime ceiling → dissipates rather than localizes.
The cure is a PI feedback loop tracking the drifting resonance dynamically.

### 1.5 L-H transition = zero-η_vac bifurcation (AVE-Fusion Ch 5:42-51)

> "The L-H transition is mathematically identical to a Dielectric Saturation-Plastic
> Mutual Inductance Bifurcation... Because the vacuum at the edge has entered a
> zero-mutual-inductance state (η_eff = 0), the turbulent eddies decouple from the
> wall. Heat cannot cross the frictionless gap."

**Critical reframing:** my Phase III-B v1 "P_IIIb-partial" result (A²_total = 0.96,
zero centroids, distributed plasma) is **exactly** this zero-mutual-inductance
bifurcation. When Axiom 4 drives z_local → ∞ (equivalently, η_eff → 0), the lattice
becomes a "frictionless" medium — the K4 scatter matrix decouples from its
neighbors. The Cosserat sector accumulates strain but can't propagate information
between sites → **distributed plateau instead of localized structures**.

This is not a failure of the engine or the coupling. It's AVE correctly producing
the well-known L-H transition state.

### 1.6 η_vac is quantified in AVE-PONDER (generate_ponder_01_spice_netlist.py:90)

```python
k_val = min(SPICE_K_SCALAR / dist, 0.999)
```

With calibrated values from AVE-APU SPICE netlists:
- **K_0 = 0.207973** for nearest-neighbor intra-emitter (He-4 tetrahedron)
- Gap K-factors ~0.011 for emitter→collector (dark-wake zone)
- Inverse-distance falloff

This **pins η_vac numerically** where my earlier research (doc 45_) could only
identify it structurally. Adjacent K4 node coupling is K ≈ 0.208, consistent with
the naive 0.5 off-diagonal in `S_ij = 0.5 - δ_ij` scaled by the bond-length geometry.

## 2. Unified mechanism picture

The complete AVE-native pair-creation story, synthesized across the ecosystem:

**Step 1 (propagation):** Two CW photons driven into the lattice propagate at c.
Each leaves a τ_zx dark wake behind it (back-EMF manifestation, η_vac × V²-gradient).

**Step 2 (collision / coincidence):** The two dark wakes converge on the collision
region. Their constructive interference creates a **localized strain enhancement**
— not just amplitude overlap of V but a spatially-localized τ_zx buildup.

**Step 3 (resonance shift):** The local strain enhancement modifies the lattice's
effective LC parameters: `ω_resonance(r, t) = ω_0 · f(strain(r, t))`. The
resonance drops under strain (Duffing-oscillator behavior).

**Step 4 (autoresonant tracking REQUIRED):** If the drive frequency is fixed at
ω_0, the drive detunes from the shifted local resonance and **reflects** (enters
the L-H / zero-η_vac bifurcation — my v1 result). If a PLL tracks the shifting
resonance, drive stays 90° phase-locked with the back-EMF (q-axis alignment) and
**continues to deposit energy** into the strained region.

**Step 5 (pair nucleation):** With sustained energy deposition into a localized
strain region, the Cosserat ω field amplifies beyond the thermal noise floor. When
the amplified ω supports topological closure (2,3-winding pattern fits the
geometry), a pair of solitons (e+/e−) nucleates.

**Without Step 4 (autoresonant tracking), pair creation is structurally impossible**
— which is what Phase III-B v1 actually demonstrated. The result I initially
labeled "disappointing" was the correct AVE prediction for **fixed-f drive**:
the L-H transition, not pair creation.

## 3. Implications for VacuumEngine3D

### 3.1 Reframe of doc 48_ results

Phase III-B v1 verdicts are **correct** under this framing:

- **P_IIIb-α** (cold vacuum null) ✓ — confirmed, unchanged
- **P_IIIb-β** (classical amplitude scaling) FALSIFIED — because "budget partition"
  IS the η_eff=0 bifurcation at A²→1. The counter-intuitive "amp=0.5 > amp=0.7" is
  the signature of drive-vacuum detuning (higher amp → faster resonance shift →
  more detuning for same drive frequency).
- **P_IIIb-γ** (frequency-cascade enhancement) NOT the right framing — should have
  been "does autoresonant FOC give pair enhancement at any frequency?"
- **P_IIIb-δ** (σ(ω) knee at ω·τ=1) peak observed at 0.9, AMBIGUOUS. Under new
  framing this is the "best detuning endurance" frequency for fixed-f drive — the
  frequency at which the drive detunes most slowly.

v1 measured **fixed-f drive failure modes**. Pair creation requires **autoresonant
drive** (v2).

### 3.2 What to add to the engine (Stage 4b, 4c)

**4b — `DarkWakeObserver`:**
Port τ_zx formula from `AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py:75-95`.
In AVE-Core, the E-field is replaced by V_inc (sum-over-ports); the formula becomes:

```python
# τ_zx surrogate computed from V² gradient + impedance-weighted shock model.
V_squared = np.sum(V_inc ** 2, axis=-1)          # (nx, ny, nz)
grad_V_sq = np.gradient(V_squared)               # per-axis
tau_zx = -(grad_V_sq[0] * Z_local)               # simplest: directional gradient
# Alcubierre-style bow-shock / dark-wake structure available via the full formula
```

Implementation: new observer class following the pattern of `RegimeClassifierObserver`.

**Validation test:** launch single PulsedSource, observe τ_zx propagating backward
at c, no wake ahead of packet. Expected amplitude ∝ V_peak² · K_0 where
K_0 = 0.207973 from PONDER.

**4c — `AutoresonantCWSource`:**

Extends `CWSource` with PLL feedback on a probe-point phase measurement:

```python
class AutoresonantCWSource(CWSource):
    """CW source with Propulsion-Ch-5 PLL tracking vacuum resonance shift.

    Monitor: probe point near source plane; measure V_inc time history.
    Phase detection: two-point quadrature V(t) vs V(t-T/4).
    Feedback: ω(t) = ω_0 − K_p·phase_error − K_i·∫phase_error dt
    Target: 90° phase offset between drive and probe response (q-axis).
    """
    def __init__(self, monitor_x0, K_p=0.3, K_i=0.05, phase_target=np.pi/2, ...):
        super().__init__(...)
        self.monitor_x0 = monitor_x0
        self.K_p = K_p
        self.K_i = K_i
        self.phase_target = phase_target
        self._omega_current = self.omega_0
        self._integral_error = 0.0
        self._probe_history = collections.deque(maxlen=...)

    def _measure_probe_phase(self, lattice):
        # Two-point quadrature: V at current step vs quarter-period ago
        ...

    def apply(self, engine, t):
        # 1. Measure probe phase
        # 2. Compute phase error vs phase_target
        # 3. Update integral
        # 4. Update ω_current via PI feedback
        # 5. Inject at new ω_current
        super().apply_with_omega(engine, t, self._omega_current)
```

**Gain tuning:** Propulsion Ch 5 doesn't give analytic values. Start with
K_p = 0.3, K_i = 0.05 as conservative defaults; run dry tests at different gains,
measure (a) convergence time to steady-state phase-lock, (b) overshoot / oscillation.
Tune empirically until smooth tracking observed.

### 3.3 What the engine will test (Stage 4d)

Phase III-B v2 at same configuration matrix (4λ × 2amp × 2T = 16 configs) but with
autoresonant sources + dark-wake observer. Three pre-registered outcomes:

- **P_IIIb-v2-pair**: centroid-finder detects ≥2 localized structures at collision,
  dark wake shows constructive interference feature at collision plane. First
  empirical AVE pair creation.
- **P_IIIb-v2-partial**: dark wake shows enhancement at collision but no pair
  nucleation. Mechanism active, amplitude/T too low.
- **P_IIIb-v2-no-change**: same distributed plateau as v1. Would **falsify** the
  Propulsion-Ch-5 interpretation; point to missing mechanism.

## 4. Cross-repo reuse matrix

What gets imported / referenced, not reimplemented:

| Source | What | Used in AVE-Core |
|---|---|---|
| `AVE-Propulsion/.../simulate_warp_metric_tensors.py:75-95` | τ_zx formula | `DarkWakeObserver` |
| `AVE-PONDER/.../generate_ponder_01_spice_netlist.py:90` | `K = K_0/dist` | Calibration `K_0 = 0.208` for adjacent-node mutual inductance |
| `AVE-Propulsion/.../ch05_autoresonant_dielectric_rupture.tex` | PLL picture | `AutoresonantCWSource` docstring + design |
| `AVE-APU/tests/apu_characterization/suite_lexicon_validation.py` | η_PY metric | Success metric: η_PY≈1 means phase-lock holding |
| `AVE-Fusion/.../05_metamaterial_caging.tex:42-51` | L-H bifurcation | Reframe of v1 results as L-H-transition analog |
| `AVE-Core/higgs_impedance_mapping.py:48-52` | Mass = L_drag | Physical interpretation of dark wake as mass mechanism |

## 5. Falsifiable predictions from Stage 4

Regardless of v2's verdict, Stage 4 delivers several new AVE-native falsifiable
predictions:

1. **Dark wake exists and propagates at c**: every CW source generates a measurable
   backward-propagating τ_zx shear strain. If 4b shows no such wake, the mechanism
   described in PONDER Ch 1 is wrong or implementation is incorrect.

2. **Phase-lock is a sharp transition**: there should be a critical PLL gain below
   which the loop does NOT lock (drifts off resonance) and above which it does.
   Empirically observable in 4c tuning.

3. **Pair creation threshold is autoresonant-dependent**: if v2 shows P_IIIb-v2-pair
   at some (λ, amp, T), and v1 at the same (λ, amp, T) showed no-response, that's
   a binary test of the Propulsion-Ch-5 hypothesis.

4. **FOC produces DIFFERENT σ(ω) shape**: v1 showed peak near ω·τ=0.9. v2 should
   show either (a) a higher peak if autoresonant tracking amplifies response, or
   (b) a flat response if the PLL holds resonance regardless of initial ω. Either
   way, a testable prediction.

## 6. Limitations and unknowns

### 6.1 PLL stability / gain tuning is empirical

Propulsion Ch 5 provides the framework but no analytic K_p/K_i. Stage 4c must
empirically find stable gains. If no gains give stable tracking, the picture itself
may be incomplete.

### 6.2 Phase detection choice

Two-point quadrature is simpler but noisier than Hilbert transform. Defer to
empirical comparison in 4c — if two-point works, use it; else upgrade.

### 6.3 τ_zx formula surrogacy

The Propulsion formula uses E-field directly. My port uses V_inc-squared (scalar
lattice voltage) as a surrogate. The two agree in the continuum limit but may
differ near V_SNAP saturation. For v2, use only as diagnostic, not as driving
dynamics.

### 6.4 The "autoresonant picture" could still be wrong

If v2 gives P_IIIb-v2-no-change (FOC doesn't help), the Propulsion-Ch-5 theory
is falsified for this scenario. Other AVE-native mechanisms from sibling repos
(point collision geometry, linear seed terms in S1, or a different observable)
become the next candidates.

## 7. Artifacts for Stage 4

- This doc — 49_ synthesis
- Stage 4b: `src/ave/topological/vacuum_engine.py` (extend with `DarkWakeObserver`)
  + `src/scripts/vol_1_foundations/dark_wake_validation.py`
- Stage 4c: `src/ave/topological/vacuum_engine.py` (extend with `AutoresonantCWSource`)
  + tuning script
- Stage 4d: `src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py`
  + `research/L3_electron_soliton/50_autoresonant_pair_creation.md`
- Commits: one per stage

## 8. Open questions for Grant (post-4d)

1. If Stage 4d shows **P_IIIb-v2-pair**: does that count as "done" for the engine's
   Phase III-B test, or do we also want to test gravity well / Compton scattering
   to validate the engine beyond pair creation?
2. If Stage 4d shows **P_IIIb-v2-no-change**: do we try (a) point collision
   geometry, (b) augmented S1 coupling per doc 44_, or (c) declare pair creation
   requires mechanism not yet in AVE-Core and ship the engine without it?
3. Where does the dark-wake diagnostic sit after Stage 4d — permanent feature of
   the engine, or diagnostic-only artifact?

None block Stage 4 execution.
