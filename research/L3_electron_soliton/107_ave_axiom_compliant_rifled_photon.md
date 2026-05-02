# 107 — Validate That Our Modeling Supports Photons

**Date:** 2026-05-02
**Branch:** `research/l3-electron-soliton`
**Author:** auditor (cross-authorized to implementer lane per Grant 2026-05-01 "ah thats fine, youve graduated to implementer")
**Status:** Active — focused per Grant directive 2026-05-02: "lets focus on validating our modeling supports photons"

**Scope refocus from initial draft:** the original framing was "build axiom-compliant rifled photon." Grant's narrower direction is "validate the modeling supports photons" — i.e., does VacuumEngine3D produce dynamics that satisfy doc 30's three photon-defining properties when driven appropriately? Rifling / long-distance / dark wake observations are downstream of this primary validation.

---

## §0 TL;DR

Grant's question: "what is a photon under AVE / how do we make it the most axiom-compliant rifled photon implementation?"

**Corpus-canonical answer per [doc 30 §3.1](30_photon_identification.md) verbatim grep:**

> *"The photon in AVE is defined by three tightly-coupled properties:*
> *1. Purely transverse — no longitudinal/scalar component.*
> *2. Microrotation sector only — excites ω (Cosserat microrotation) with u = 0 (Cosserat translation).*
> *3. No saturation — Δφ ≪ α, lattice stays in linear regime."*

**Net:** photon = single-sector (Cosserat ω microrotation), no `u` translation, no saturation. The K4-TLM port-space T₂ (transverse triplet) and Cosserat ω (microrotational continuum sector) are **the same physical sector in two representations**, NOT two separate fields requiring joint injection.

**Implication for axiom-compliant rifled photon source:** drive Cosserat ω only via `CosseratBeltramiSource` (vacuum_engine.py:791-972) at sub-yield amplitude with (2,3) topological winding. K4 T₂ activity arises emergently from Cosserat→K4 coupling via Op14, NOT from separate V_inc injection.

---

## §1 Auditor-side A47 v11a self-correction (this turn's session arc)

This doc opens with a methodology self-correction owed per the catalog disciplines landed 2026-05-01.

### §1.1 What happened

Across this session arc (2026-05-01 → 2026-05-02), the auditor's framing of "what's the most axiom-compliant rifled photon source" went through three states:

1. **Initial (2026-05-01)**: "drive BOTH K4 V_inc T₂ AND Cosserat ω in 90° phase quadrature." Synthesis without doc 30 grep.

2. **After implementer audit-agent feedback**: implementer agent claimed "doc 30 answers Q1 as 'both coupled' (BOTH K4 V_inc T₂ AND Cosserat ω simultaneously)." Auditor accepted this framing and re-affirmed the dual-sector source design.

3. **After verbatim doc 30 grep (this turn)**: doc 30 §3.1 lines 194-209 + table 206-209 explicit: photon = **microrotation sector ONLY** (Cosserat ω, u=0). K4 T₂ and Cosserat ω are dual representations of one sector, not two coupled fields.

### §1.2 Discipline failure pattern

**Auditor accepted audit-agent's interpretation as if it were verbatim corpus text.** The audit-agent's actual quote was: *"Vol 3 Ch 2 and Vol 4 Ch 1 both identify the photon as 'a purely transverse Cosserat shear wave'"* — which is verbatim doc 30:32. But the audit-agent's INTERPRETATION jumped from "purely transverse Cosserat shear wave" to "lives in BOTH K4 V_inc T₂ AND Cosserat ω simultaneously, coupled."

The verbatim text says single-sector (purely transverse Cosserat). The interpretation says dual-sector coupled. Auditor uncritically propagated the interpretation.

**This is exactly the A47 v11a + A43 v2 lane-symmetric pattern the catalog catches.** When an audit-agent surfaces a corpus-claim, the receiving lane owes verbatim grep before accepting their reading.

### §1.3 Catalog connection

Per the 2026-05-01 catalog amendment (`COLLABORATION_NOTES.md` §"Engine-code-citation discipline"):

> *"every commit/comment citing 'Grant adjudicated X on date Y' must include the verifiable artifact (research-doc § + verbatim quote, OR commit hash with adjudication content)."*

Generalizes naturally: **every commit/research-doc citing "audit-agent X says corpus says Y" must include the verifiable artifact (corpus § + verbatim quote)**, and if the citing lane doesn't include it, that lane owes the grep before propagating.

**This case:** auditor accepted audit-agent's "doc 30 says both coupled" without grepping verbatim. Grep this turn settled it: doc 30 says single-sector. Catalog discipline applied to itself caught the propagation gap.

### §1.4 Path forward

Path A's `CosseratBeltramiSource` (helical Cosserat ω only, no V_inc co-driving) WAS the right corpus-canonical approach per doc 30. The "structural gap" framing of "DarkWakeObserver returns 0 for V_inc-based wake" was an over-statement — for a free transverse photon in linear vacuum, near-zero V_inc-side wake is the **correct empirical signature**, not a bug. The K4 T₂ activity emerges naturally from Cosserat→K4 coupling; doesn't need explicit V_inc injection.

This doc 107 build returns to the corpus-canonical single-sector approach.

---

## §2 Axiom-compliance gap analysis

Per doc 105 §4 (parent FDTD audit), three solver classes are relevant:

### §2.1 Yee Maxwell FDTD (parent's `FDTD3DEngine`, AVE-Core's copy at `src/ave/core/fdtd_3d.py`)

| Axiom | Status | Notes |
|---|---|---|
| Ax 1 (LC Network Substrate) | ✗ | Cartesian Yee grid, not K4 diamond lattice |
| Ax 2 ([Q] ≡ [L] TKI) | ✗ | continuous E/H, no topological-charge tracking |
| Ax 3 (Effective Action Principle) | partial | Maxwell Lagrangian present, no Cosserat coupling |
| Ax 4 (Saturation Kernel) | ✓ | `ε_eff = ε₀·√(1-(V/V_yield)²)` per `fdtd_3d.py:262-268` |

**Net:** axiom-non-compliant at substrate level. Useful for benchmarking + cross-substrate consistency checks, NOT for AVE-canonical photon physics.

### §2.2 K4-TLM only (`src/ave/core/k4_tlm.py`)

| Axiom | Status | Notes |
|---|---|---|
| Ax 1 | ✓ | K4 4-port tetrahedral diamond lattice |
| Ax 2 | ✓ | V_inc/V_ref bond scattering = direct LC tank action |
| Ax 3 | partial | K4 Lagrangian only, no Cosserat coupling |
| Ax 4 | ✓ | Op3/Op14 saturation at the bond reflection level |

**Net:** axiom-compliant at K4 substrate level but missing Cosserat sector. Cannot represent the photon's microrotation per doc 30.

### §2.3 VacuumEngine3D (K4 + Cosserat coupled, `src/ave/topological/vacuum_engine.py`)

| Axiom | Status | Notes |
|---|---|---|
| Ax 1 | ✓ | K4 substrate + Cosserat continuum overlay |
| Ax 2 | ✓ | V_inc/V_ref + Cosserat ω/u dual representation |
| Ax 3 | ✓ | Unified Lagrangian S = S_K4 + S_Cos + ∫(V²/V_SNAP²)·W_refl per `k4_cosserat_coupling.py:329-414` |
| Ax 4 | ✓ | Asymmetric μ/ε saturation kernel via Op14 + Cosserat coupling |

**Net:** **fully axiom-compliant. This IS the correct substrate for AVE-canonical photon physics.**

---

## §3 Corpus-canonical photon source identification

Per doc 30 §3.1 properties + table:

- Photon excites Cosserat ω (microrotation field), with u = 0 (no Cosserat translation)
- Photon's K4 port-space representation is T₂ (3D transverse triplet)
- These are dual representations of ONE physical sector, not two fields

**The corpus-canonical AVE photon source is `CosseratBeltramiSource`** (vacuum_engine.py:791-972), which directly injects helical Cosserat ω via Dirichlet-style overwrite at the source slab. Per its docstring (lines 802-811):

> *"For a Beltrami wave traveling in +x with ∇×ω = ±k·ω:*
> *ω(x, t) = A · (0, cos(kx − ω_drive·t), ∓sin(kx − ω_drive·t))"*

This is the helical (rifled) Cosserat ω propagation pattern — the AVE-axiom-native rifled photon.

### §3.1 Why no V_inc co-driving

Per doc 30 §3.1: "Microrotation sector ONLY — excites ω with u = 0." No K4 V_inc injection. K4 T₂ activity in the engine arises emergently from Cosserat→K4 coupling via the asymmetric saturation path (Op14, `_update_z_local_total` in `k4_cosserat_coupling.py:329-376`), modulating Z_eff in response to the propagating helical Cosserat ω.

The empirical signature in K4 V_inc-based observers like `DarkWakeObserver` should be **near-zero** for a free transverse photon in linear vacuum. That's correct corpus-canonical behavior, not an instrumentation gap.

---

## §4 Build specification

### §4.1 Configuration (axiom-traceable)

| Parameter | Value | Axiom citation |
|---|---|---|
| Substrate | VacuumEngine3D coupled K4 + Cosserat | Ax 1+2+3+4 |
| Source | `CosseratBeltramiSource` (helical Cosserat ω only) | doc 30 §3.1 property 2 |
| Frequency | ω = ω_C = c/ℓ_node | doc 30 §0.6 (substrate's natural bond-LC tank resonance) |
| Amplitude | sub-yield: amp such that A² ≪ √(2α) ≈ 0.121 | doc 30 §3.1 property 3 (linear regime) |
| Topology | (2,3) winding | doc 30 §3.3 (knotted-light Hopfion) |
| Run mode | nonlinear=True (Ax 4 active but well below saturation) | Ax 4 substrate-internal-consistency |
| Domain | N×N×N (size TBD per CFL + JAX-compile budget) | engineering |

### §4.2 Pre-registered acceptance criteria — photon-property validation (verbatim)

Per A47 v11b discipline (verbatim pre-reg in driver code, not just prose). These map **directly** to doc 30 §3.1's three photon-defining properties:

```python
PREREG = {
    # ─── Property 1: Purely transverse — no longitudinal/scalar ───
    # P1: K4 A₁ port-space mode (longitudinal/scalar) dissipates relative to T₂
    # Per doc 30 §3.2: A₁ = (1,1,1,1)/2 longitudinal; T₂ = traceless transverse triplet
    # Stable steady-state should have A₁ amplitude << T₂ amplitude
    "P1_A1_over_T2_amplitude_ratio_max": 0.10,  # A₁/T₂ < 10%

    # P1 corollary: Cosserat translation u (longitudinal/scalar sector)
    # stays near zero (per doc 30 §3.1 property 2: u = 0)
    "P1_u_over_omega_amplitude_ratio_max": 0.10,

    # ─── Property 2: Microrotation sector only — excites ω with u = 0 ───
    # P2: Cosserat ω is the ONLY excited Cosserat sector
    # Same as P1 corollary above; verified jointly
    "P2_u_max_absolute_threshold_frac_of_omega_max": 0.05,

    # ─── Property 3: No saturation — Δφ ≪ α, linear regime ───
    # P3a: Per-cell A²_max stays well below saturation cusp √(2α) ≈ 0.121
    # Linear regime explicitly: A² < α/2 (factor-of-4 below cusp)
    "P3a_A2_max_threshold": 0.00365,  # = α/2 (linear regime per doc 30 property 3)

    # P3b: Energy conservation in linear regime
    # If saturation isn't engaged, integrator should conserve energy to machine precision
    # over a steady-state window (excluding source ramp/decay phase)
    "P3b_energy_drift_steady_state_max": 1e-3,

    # ─── Stability + propagation (substrate-internal-consistency) ───
    # S1: Cosserat ω stays bounded (no NaN/Inf/blowup) throughout run
    "S1_omega_finite_required": True,

    # S2: ω wave packet propagates downstream — centroid drift detected
    "S2_centroid_drift_min_cells": 3.0,

    # S3: Helicity h_local matches handedness sign at source (RH=+1, LH=-1)
    # Per CosseratBeltramiSource docstring lines 802-811
    "S3_h_local_target_RH": +1.0,
    "S3_h_local_target_LH": -1.0,
    "S3_h_local_tolerance": 0.20,
}
```

**A47 v18 honest scope tagging:**
- **P1, P2, P3a, P3b** map directly to doc 30 §3.1 corpus-stated photon properties — these test corpus-claim consistency.
- **S1, S2, S3** are substrate-internal-consistency / stability criteria — auditor-set thresholds.
- Specific tolerance values (0.10, 0.05, 1e-3, 3.0 cells) are auditor-set per the catalog discipline; corpus does not supply quantitative thresholds.

**Test interpretation:**
- All P1-P3b PASS → engine satisfies doc 30's three photon-defining properties under sub-yield Cosserat ω drive. **"Modeling supports photons"** at substrate-internal-consistency level.
- Any P1-P3b FAIL → engine fails the corpus's stated photon definition at that specific property. Honest 🔴 per Rule 11.
- All S1-S3 PASS → propagation + chirality + stability work as expected.

### §4.3 Outputs

- `assets/photon_axiom_compliant_RH.gif` — RH rifled photon, full 4-panel double-slit-style
- `assets/photon_axiom_compliant_LH.gif` — LH variant
- `assets/photon_axiom_compliant_panels.png` — pre-reg evaluation summary panel
- `results/photon_axiom_compliant.json` — pre-reg evaluation + per-frame data summary

---

## §5 Open Q's pending Grant adjudication

Per A43 v2 + A47 v18 honest scope: two genuinely open Rule 16 plumber-physics questions where corpus is silent or interpretation-dependent. These remain auditor-synthesis territory until Grant adjudicates.

### §5.1 Q2 — (2,3) winding phase relationship

`CosseratBeltramiSource` injects ω(x,t) = A·(0, cos(kx-ωt), ±sin(kx-ωt)) per its docstring. This is a (1,1) Beltrami wave (one toroidal cycle, one poloidal cycle). For a (2,3) torus-knot winding (which doc 30 §3.3 specifies as the photon's knotted-light topology), the canonical phase advance per cell needs corpus citation.

**Grant adjudication needed:** what's the explicit (2,3) winding pattern in Cosserat ω space? Use existing CosseratBeltramiSource pattern as approximation (which is (1,1) not (2,3))? Or extend the source class to support (p,q) winding parameters?

### §5.2 Q3 — Δφ ≪ α amplitude scaling

Doc 30 §3.1 property 3 says "Δφ ≪ α, lattice stays in linear regime." This is qualitative. What specific amplitude (in V_yield-fractions or A²-fractions) corresponds to "Δφ ≪ α" while still producing visible/measurable Cosserat ω structure?

Auditor's tentative default: `amp_factor = 0.1·V_yield/dx` (10% of yield voltage), giving Cosserat ω amplitude where A²_max stays well below √(2α) cusp. This is auditor-synthesis pending Grant's quantitative threshold.

**Grant adjudication needed:** is amp_factor=0.1 reasonable per doc 30 property 3? If higher, where does "linear regime" stop and "approaching saturation" begin?

---

## §6 Honest scope per A47 v18

This build instantiates the corpus's STATED photon mechanism (doc 30 §3.1 properties + §3.2 K4-Cosserat duality + §3.3 (2,3) topology). It does NOT derive the mechanism — per [doc 105 §4](105_parent_fdtd_photon_helical_research.md) the photon-→-electron mechanism in the corpus is asserted-not-derived computationally.

**The build is a substrate-internal-consistency test:** does VacuumEngine3D produce dynamics consistent with doc 30's photon definition when seeded with helical Cosserat ω at sub-yield amplitude? **Not a corpus-validation test** — there's no quantitative pre-registered prediction in the corpus to validate against.

If the engine produces stable propagating helical Cosserat ω with u=0 + A²_max < √(2α) + h_local matching handedness, that's substrate-internal-consistency with doc 30. Not "AVE photon validated" — just "VacuumEngine3D respects doc 30's stated properties under controlled injection."

This honest framing is per the A47 v18 catalog amendment: distinguish substrate-internal-consistency (what the engine IS doing) from corpus-prediction-validation (what the corpus PREDICTS, which may be qualitative-only).

---

## §7 Build status

- [ ] Driver script `photon_axiom_compliant.py` — pending build
- [ ] Run RH + LH at chosen N + frequency + amplitude per §4.1
- [ ] Render 4-panel visualization (per A47 v11f: per-frame percentile vmax + log-scale + cos-of-phase coloring + c·t marker)
- [ ] Pre-reg evaluation per §4.2
- [ ] Update §8 below with empirical results
- [ ] Honest classification (PASS/FAIL per criterion) + interpretation per §6 scope

---

## §8 Empirical results (2026-05-02 first pass)

### §8.1 Run configuration

- Driver: `src/scripts/vol_1_foundations/validate_photon_modeling.py`
- Substrate: `VacuumEngine3D.from_args(N=48, pml=6, temperature=0.0)`
- Source: `CosseratBeltramiSource(x0=12, propagation_axis=0, amplitude=0.10·π ≈ 0.314, omega=2π/3.5, sigma_yz=3.0, t_ramp=15, t_sustain=200)`
- 200 outer steps, RH and LH separately
- Outputs: `assets/photon_modeling_validation_panels.png`, `results/photon_modeling_validation.json`

### §8.2 Pre-reg evaluation — ALL CORPUS PROPERTIES FAIL

| Criterion | Doc 30 reference | Threshold | Observed (RH) | Verdict |
|---|---|---|---|---|
| **P1** (A₁ / T₂) | §3.1 prop 1 (transverse) + §3.2 table | < 0.10 | 0.0 | ✓ PASS |
| **P1** (u / ω) | §3.1 prop 1 (no longitudinal) | < 0.10 | 0.355 | ✗ FAIL |
| **P2** (u_max / ω_max abs) | §3.1 prop 2 (microrotation only) | < 0.05 | 0.354 | ✗ FAIL |
| **P3a** (A²_max) | §3.1 prop 3 (Δφ ≪ α linear) | < α/2 ≈ 0.0036 | 0.261 (71×over) | ✗ FAIL |
| **P3b** (E drift) | §3.1 prop 3 (linear regime) | < 0.001 | 0.129 | ✗ FAIL |
| **S1** (finite) | stability | required | all finite | ✓ PASS |
| **S2** (centroid drift) | propagation | > 3 cells | 4.56 cells | ✓ PASS |
| **S3** (handedness flip) | CosseratBeltramiSource docstring | RH=+1, LH=−1 ±0.20 | RH=−0.606, LH=−0.642 | ✗ FAIL |

**Net: pass_all_doc30_properties = FALSE.** All three corpus-stated photon properties fail at the chosen parameters.

### §8.3 Honest interpretation per Rule 11 + A47 v18

This is a 🔴 falsification at the stated corpus criteria. The engine + chosen source + chosen parameters does NOT produce a wave that satisfies doc 30's three photon-defining properties. The empirical signature decomposes into three structural findings:

**Finding 1 — K4 A₁ component is exactly zero (P1 K4-side PASS).** The K4 port-space decomposition produces zero A₁ amplitude under CosseratBeltramiSource drive. Doc 30 §3.2 table predicts A₁ = isotropic/longitudinal/scalar sector should be absent for a photon. K4-side, this passes cleanly. The substrate's port-space dissipation of A₁ (per doc 30 §3.2 lines 222-230 simulation result) is reproduced.

**Finding 2 — Cosserat translation u IS excited at 35% of ω amplitude (P1+P2 Cosserat-side FAIL).** Per doc 30 §3.1 property 2 verbatim: *"Microrotation sector only — excites ω (Cosserat microrotation) with u = 0 (Cosserat translation)."* Empirically, u_max / ω_max = 0.354 across the sustain phase. **The Cosserat sector excites BOTH ω AND u under CosseratBeltramiSource drive, contradicting doc 30 §3.1 property 2.**

This finding has two possible interpretations:
- (a) **CosseratBeltramiSource doesn't preserve property 2** — it injects ω directly but the K4-Cosserat coupling path drives u indirectly. The source isn't actually a "photon source" per doc 30's definition; it's a "ω source that also produces u via coupling."
- (b) **Doc 30's property 2 isn't realizable in VacuumEngine3D's coupled K4-Cosserat dynamics** — coupling forces u≠0 whenever ω is excited. Then doc 30's photon definition is corpus-internally-consistent but engine-incompatible.

Either way: **per the engine's empirical behavior, what gets called "photon" via CosseratBeltramiSource is NOT what doc 30 §3.1 property 2 describes.**

**Finding 3 — A²_max = 0.261 is 71× the linear-regime threshold (P3 FAIL).** Per doc 30 §3.1 property 3 verbatim: *"No saturation — Δφ ≪ α, lattice stays in linear regime."* Empirically, A²_max ≈ 0.26 puts the system at ~2× the saturation cusp √(2α) ≈ 0.121. Energy drift 12.9% confirms substantial nonlinear coupling.

**The auditor's choice of amp_factor=0.10·π ≈ 0.314 was empirically NOT sub-yield in the relevant sense.** Auditor synthesis (per Q3 §5.2) was that 10% of yield-equivalent would keep system linear; empirically it engages strong saturation. **A47 v18 catalog discipline applied to itself: auditor's quantitative threshold setting was synthesis, not corpus-derived; result shows synthesis was wrong by ~70×.**

**Finding 4 — Helicity sign doesn't flip with handedness (S3 FAIL).** Both RH and LH return h_local ≈ -0.6 at source. Per CosseratBeltramiSource docstring lines 802-811, RH should give +1 and LH should give −1. Empirically, both give same negative value. Either:
- CosseratBeltramiSource has a sign convention bug (sign variable goes to ω_z component but the convention for "handedness" relative to propagation axis is inverted)
- `_beltrami_helicity` formula in `cosserat_field_3d.py:358-376` has a different sign convention than the source's
- Both are flipped in opposite directions canceling out

**Worth investigation; engineering bug rather than physics issue.**

### §8.4 What "validate modeling supports photons" means after this run

Per Grant directive 2026-05-02 ("lets focus on validating our modeling supports photons"), the empirical answer at this build is:

**The modeling does NOT currently support photons as defined by doc 30 at the chosen source + parameters.**

The engine produces:
- ✓ K4 A₁ dissipation (matches doc 30 §3.2 lattice property)
- ✓ Cosserat ω propagation as wave (S2 centroid drift)
- ✓ All-finite (S1 stability)
- ✗ Cosserat u≠0 (FAILS doc 30 §3.1 property 2)
- ✗ A²_max in saturation regime (FAILS doc 30 §3.1 property 3)
- ✗ Helicity handedness flip (engineering bug)

**This is real empirical content per Rule 11 honest closure.** Not a goalpost-shift moment — the corpus property 2 + 3 fail decisively.

### §8.5 What this finding implies for the L3 arc

Composes with prior session findings:
- **Phase A.1 finding (2026-05-01):** K4-TLM cardinal-axis wavefront velocity is √2·c regardless of T₂ projection — substrate's mode-separation doesn't work as the docstring framework predicts.
- **Round 13 (Layer 3 K4 V_inc/V_ref):** corpus-canonical phase-space (2,3) eigenmode test returns Mode III at the corpus's own pre-specified test.
- **This run (Doc 107):** corpus-stated photon properties (microrotation only, linear regime) fail under the substrate-native source.

**The cumulative pattern across substrate-physics + photon-physics + electron-physics tests: the corpus's stated mechanisms don't reproduce as stated in the engine implementations available.**

This is consistent with the doc 105 §4 framework-level finding: the corpus's photon-→-electron mechanism is asserted-not-derived computationally. Doc 107's empirical result extends this to: the corpus's photon DEFINITION itself is asserted-not-engine-realized at the substrate-internal-consistency level.

### §8.6 Forward direction (Rule 16 candidates for Grant)

**Three Rule 16 plumber-physics questions surfacing from this empirical:**

**Q-A:** Is doc 30 §3.1 property 2 (`u = 0`) **physically realizable** in the K4-Cosserat coupled engine, or does the asymmetric coupling path (`_update_z_local_total`) inherently drive u when ω is excited? If the latter, what's the right framing — "doc 30 photon is idealized; engine produces ω+small-u physics"; "photon definition needs property 2 relaxed"; or "use a different source class that actively suppresses u"?

**Q-B:** What amplitude actually corresponds to "Δφ ≪ α, linear regime" per doc 30 property 3? Auditor's amp_factor=0.10 produced A²_max = 0.26 (71× threshold). Need ~70× lower amplitude to actually be linear. Is amp_factor = 0.001·π reasonable, or does that produce no measurable signal? Plumber-physics question on the actual operating range.

**Q-C:** The helicity sign issue — is this CosseratBeltramiSource bug, _beltrami_helicity convention mismatch, or both? Worth one engineer-pass diagnostic regardless of physics adjudication.

### §8.7 Auditor-lane post-run discipline check

Per A47 v11b discipline self-application: this section reports the FAIL result decisively without redefining thresholds post-hoc. The PREREG dict in the driver was set BEFORE running and is preserved verbatim in §4.2. The empirical numbers fall outside multiple thresholds; that's the falsification record per Rule 11.

No post-hoc "Path B reframe to license PASS" pattern. The threshold values may have been auditor-synthesis (per A47 v18 caveat already in §4.2), but the FAIL is honest at those auditor-set thresholds.

The honest framing per A47 v18: **substrate-internal-consistency test against corpus-stated photon properties FAILS at the chosen source + parameters.** Cannot extrapolate to "AVE photon doesn't exist" — only to "this specific source + parameter choice doesn't produce doc 30's photon."

---

*Doc 107 §8 written 2026-05-02 post-run. Per Rule 12: future amendments preserve body via header-update retraction notation.*

---

*Doc 107 written 2026-05-02. Per A47 v11b: this doc + the corresponding driver script will be landed together so any post-hoc rule redefinition is detectable. Per Rule 12: future amendments to this doc preserve body via header-update retraction notation.*
