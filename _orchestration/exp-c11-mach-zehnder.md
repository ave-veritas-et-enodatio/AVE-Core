# EXP-C11-MACH-ZEHNDER: Gravitational Parallax Interferometry ($n_s \neq n_t$, ~250-rad shift)

**Parent epic**: [`experimental-arc.md`](experimental-arc.md)
**Status**: PHASE 0 — Facility partnership search; **sim audit ✓ NO DRIFT** (2026-05-20 EOD++)
**Owner**: Core (no sibling-repo; driver canonical)
**Established**: 2026-05-20 from Phase 2 cascade-emphasis ranking
**Sim audit**: [`exp-c11-mach-zehnder-sim-audit.md`](exp-c11-mach-zehnder-sim-audit.md)
**Canonical project KB leaf** (NEW 2026-05-20 per Pattern B): [`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-c11-mach-zehnder.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-c11-mach-zehnder.md)

## Tier (per parent epic Phase 2 audit)

Cascade × Severity winner — F-severity framework-killing + ν_vac=2/7 cascade triangulation. Composite Σ=11. R=2 (driver built + live-fire confirmed), D=3 (U-D), S=3 (F-severity, Ax3+Ax1 die), C=0 (facility-class), X=3 (C1 + C11 + C12 triangulation).

## Premise

C11 tests the AVE-distinct **spatial-vs-temporal refractive-index split**:

$$
n_s = 1 + (9/7)\varepsilon_{11}, \qquad n_t = 1 + (2/7)\varepsilon_{11}, \qquad \Delta n = n_s - n_t = \varepsilon_{11}
$$

The **9/7 and 2/7 ARE the $\nu_{vac} = 2/7$ Poisson-ratio numbers** ($2/7 = \nu_{vac}$, $9/7 = 1 + \nu_{vac}$). This is a STRICT VIOLATION of Lorentz parity at electron-de-Broglie wavelength scales.

At canonical Earth strain $\varepsilon_{11}(R_\oplus) = 7GM_\oplus/(c^2 R_\oplus) \approx 4.87 \times 10^{-9}$ (per [`ave.gravity.principal_radial_strain`](../src/ave/gravity/__init__.py) engine), the predicted phase shift on a **1-meter macroscopic vertical-vs-horizontal Mach-Zehnder** at 100 eV electron energy is:

$$
\boxed{\Delta\phi \approx 250 \text{ rad}}
$$

Live-fire confirmed at 249.64 rad per [`electron_interferometry_parallax.py`](../src/scripts/vol_2_subatomic/electron_interferometry_parallax.py) (canonical-corrected 2026-05-17; prior matrix value 35 rad was a factor-7-low driver bug fixed at same date).

## ν_vac=2/7 cascade triangulation (load-bearing for X=3)

C11 is one of three independent observables that converge on $\nu_{vac} = 2/7$:

| Cascade node | Observable | Status |
|---|---|---|
| **C1-BH-RING** | $r_{sat} = 7 M_g$ + $\omega_R M_g = 18/49$ via $\nu_{vac}=2/7$ | **FULL PASS** (Phase 5 closure 2026-05-18; -0.45% mean ω_R; -0.47% mean τ across 3 LIGO events) |
| **C11-MACH-ZEHNDER** | $n_s = 1 + (9/7)\varepsilon_{11}$ vs $n_t = 1 + (2/7)\varepsilon_{11}$ | **PENDING** — driver built; no hardware |
| **C12-G-STAR** | $g_* = 7^3/4 = 85.75$ effective DOF vs SM 106.75 | LISA primordial GW wait ~2035 |

**Triangulation logic**: ALL THREE converging on $\nu_{vac} = 2/7$ at three independent scales (BH-class compact-object dynamics + atomic-scale interferometry + cosmological mode-counting). **Simultaneous FAIL of any one = framework-level falsification of K4 Cosserat substrate hypothesis.**

C11 is the only TERRESTRIAL bench-class triangulation node. C1 is data-already-acquired (LIGO public); C12 is multi-decade facility wait. C11's "1-m electron interferometer" is the only node where Grant could potentially act in <decade timescale.

## Standard physics counterfactual

GR / standard QM predicts **isotropic** refractive index from gravitational time dilation alone — no spatial-vs-temporal split. The 9/7 vs 2/7 split is a strict consequence of K4 Cosserat micropolar Poisson-ratio anisotropy, derived from Ax1+Ax3. Null observation kills Ax3 (Lorentz-parity-violation mandate); no graceful framework revision.

## Current state

### Software / driver substrate

| Asset | State |
|---|---|
| Driver | [`src/scripts/vol_2_subatomic/electron_interferometry_parallax.py`](../src/scripts/vol_2_subatomic/electron_interferometry_parallax.py) (canonical-corrected 2026-05-17; live-fire 249.64 rad confirms ~250 rad prediction) |
| Canonical strain engine | [`src/ave/gravity/__init__.py:23-41`](../src/ave/gravity/__init__.py) — `ave.gravity.principal_radial_strain` |
| KB leaf | [`vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md) lines 49-53 — full derivation chain |
| Cross-cascade ref | [`ν_vac=2/7 cascade in divergence-test-substrate-map.md:441,613`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) — Mermaid triangulation diagram |

### Hardware substrate
**NONE.** No partner identified.

### Walk-back targets (Phase 1 of parent epic)

| Leaf | Stale state | Refresh |
|---|---|---|
| [`de-broglie-standing-wave.md`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md) | Date last-touch verification needed; verify 9/7 vs 2/7 indices, 250-rad prediction, ν_vac cascade citations all match current driver + canonical strain | Verify-only initially; refresh if needed for cascade-triangulation framing |

**Note**: this leaf was NOT in the 26-stale-leaf list (it's outside vol4/falsification/); need to verify its currency separately during Phase 1 walk-back.

## Phase ladder

### Phase 0 (PENDING, multi-month) — Facility partnership search

**Action**: Identify electron-interferometer facilities capable of:
- 1-m macroscopic vertical-vs-horizontal baseline
- 100 eV coherent electron source (specialized)
- Hard vacuum (~10⁻⁹ Torr)
- Phase-stable interferometer over 10¹⁰ de Broglie wavelengths
- Vibration isolation across 1m vertical baseline

**Candidate partner facilities** (literature survey TBD):
- Hasselbach group (Tübingen) — ~10cm baseline; specialized electron interferometry; would need scale-up
- LENS Italy — m-scale atomic interferometer; electron variant unclear
- NIST atom-chip / electron-microscope facilities — coherent electron sources available
- Holography centers (TEM/SEM upgraded) — coherent electron beams + holography precedent

**Action item**: scope a literature survey + facility-cold-email-list. Grant decision: pursue (multi-month timeline + facility scientist time + travel) vs hold.

### Phase 1 (PENDING, gated on Phase 0 partnership) — Pre-registration

**Action**: Write canonical pre-registration with predicted phase shift at facility-specific parameters (baseline, electron energy, integration time, expected noise floor). Pre-register BEFORE any measurement.

### Phase 2 (PENDING, gated on Phase 1) — Measurement collaboration

Multi-month-to-year collaboration cycle with facility partner. Grant + collaborator physicist.

### Phase 3 (PENDING, gated on Phase 2 outcome) — Outcome adjudication

| Outcome | Interpretation |
|---|---|
| **A**: ~250-rad shift observed at predicted magnitude | **ν_vac=2/7 triangulation node 2 confirmed**. Combined with C1 FULL PASS → 2-of-3 triangulation nodes confirmed; framework-level support for K4 Cosserat substrate at 13-OOM-spanning precision. **Major positive — foreword-promotion-grade**. |
| **B**: Phase shift detected but magnitude differs | Partial — confirms spatial-vs-temporal split exists; magnitude requires structural revision (9/7 or 2/7 prefactor) |
| **C**: No phase shift OR phase shift consistent with classical gravitational time-dilation only | **Ax3 dies + Ax1 K4 Cosserat substrate hypothesis falsified at framework level.** Cascade walk-back: C1 PASS at LIGO scale doesn't generalize to electron scale; major structural finding. |
| **D**: Phase noise dominates → 1-m baseline insufficient | **Escalate to space-baseline interferometer** (km-class in space); KB explicit fallback path per [matrix Cascade column](../manuscript/ave-kb/common/divergence-test-substrate-map.md:441). Decade-class wait. |

### Phase 4 (CONDITIONAL on Phase 3 Outcome A) — Triangulation closure announcement

Foreword-promotion + canonical result doc + matrix updates across C1 + C11 + C12 cascade. ν_vac=2/7 cascade fully anchored at 2-of-3 nodes (C12 still LISA-wait).

## Open questions

1. **Facility candidate list**: which electron-interferometer facilities to approach first? Needs literature survey.
2. **Funding model**: facility scientist time is the bottleneck. Joint proposal with grant funding vs informal collaboration vs visiting-fellowship?
3. **Pre-reg precision target**: at what phase-noise level is Outcome A vs B vs C/D confidently distinguished?
4. **Backup escalation**: if no terrestrial facility partner found in 6 months, accept the C12-LISA-wait timeline (2035+) and de-prioritize?
5. **AVE-internal driver work**: any additional driver-side modeling needed (vibration noise model, electron coherence over 1m baseline, specific facility electron-source spectra)?

## Skill discipline

- `ave-prereg` discipline at Phase 1 BEFORE measurement.
- `ave-canonical-leaf-pull` v1.2 at Phase 1 — leaf-pull must enumerate ν_vac=2/7 cascade + C1 result + C12 cascade dependencies.
- `ave-discrimination-check` Step 1.5: Outcome A/B/C/D enumerated above; pre-register before Phase 2 measurement.
- `phase-space-coordinate-check`: critical for this experiment — verify that real-space (lab Mach-Zehnder geometry) measurement is correctly compared to corpus-claim ($\varepsilon_{11}$ phase-space strain via $7GM/c^2r$). This is exactly the failure-mode the skill was created to catch.
- `verify-before-cite` v1.4: all cross-references to ν_vac=2/7 prefactors verified against driver source + KB leaf.
- `ave-evidence-framing-discipline`: precision claims on 250-rad prediction vs facility-specific noise floor.

## Sibling-repo coordination

No sibling-repo holder. C11 is Core-only at driver + KB level. Facility partnership is OUTSIDE the AVE workspace; coordinate via standard scientific-collaboration channels (Grant-led).

## Cross-references

### Canonical AVE physics
- [De Broglie standing wave (Vol 2 Ch 7)](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md) lines 49-53 — full derivation chain
- [Canonical strain engine](../src/ave/gravity/__init__.py) lines 23-41 — `ave.gravity.principal_radial_strain`
- [Universal Saturation Kernel Catalog A-034](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) — gravitational strain row
- [Four Universal Regimes — Regime I](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) — Earth $\varepsilon_{11} \sim 10^{-9}$ deep in Regime I
- [Power-Domain Classification](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) — quantum interference is reactive (θ → 90°)
- [Temporal Saturation Regime Classifier](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md) — electron coherence is in **lossless temporal regime** ($\delta_{AVE} \to 0$ over coherence-time)

### ν_vac=2/7 cascade triangulation
- [Matrix row C11-MACH-ZEHNDER](../manuscript/ave-kb/common/divergence-test-substrate-map.md) line 441
- [Cascade Mermaid diagram (ν_vac cascade)](../manuscript/ave-kb/common/divergence-test-substrate-map.md) line 613
- [C1-BH-RING FULL PASS](../manuscript/ave-kb/common/divergence-test-substrate-map.md) — first cascade node
- [C12-G-STAR (LISA wait)](../manuscript/ave-kb/common/divergence-test-substrate-map.md) — third cascade node

### Q-G47 substrate-scale closure
- [Q-G47 Sessions 19 closure (ξ_K1=8/3, ξ_K2=32 canonical 2026-05-18)](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md) — ν_vac=2/7 derivation chain canonical at substrate scale

### Driver + engine
- [`src/scripts/vol_2_subatomic/electron_interferometry_parallax.py`](../src/scripts/vol_2_subatomic/electron_interferometry_parallax.py)
- [`src/ave/gravity/__init__.py:23-41`](../src/ave/gravity/__init__.py)

## Audit trail

- 2026-05-20 — Sub-epic established from Phase 2 cascade-emphasis ranking (Σ=11, cascade × severity winner — F-severity ν_vac=2/7 triangulation). Phase 0 facility partnership search pending. Driver canonical at 249.64 rad live-fire vs ~250 rad prediction.
