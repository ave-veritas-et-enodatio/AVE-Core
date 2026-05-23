[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
exp-id: exp-7jekc6
status: pending
strengthens:
  - clm-rd9cjm: 1.0
path-stable: "referenced from vol2, vol3, vol4 + matrix C11-MACH-ZEHNDER as canonical project leaf"
-->

## Project C11-MACH-ZEHNDER: Gravitational Parallax Interferometry (electron Mach-Zehnder $n_s \neq n_t$)

> ↗ See also: [`_orchestration/experimental/c11-mach-zehnder/exp-c11-mach-zehnder.md`](../../../../../_orchestration/experimental/c11-mach-zehnder/exp-c11-mach-zehnder.md) — AVE-Core orchestration sub-epic for facility partnership search + measurement
>
> ↗ See also: [`_orchestration/experimental/c11-mach-zehnder/exp-c11-mach-zehnder-sim-audit.md`](../../../../../_orchestration/experimental/c11-mach-zehnder/exp-c11-mach-zehnder-sim-audit.md) — sim drift audit (NO DRIFT verdict on ν_vac + ε_11 + cascade axes)
>
> ↗ See also: [Vol 2 Ch 7 §Gravitational Parallax Interferometry](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md) — canonical physics derivation
>
> ↗ See also: [Q-G47 Substrate-Scale Cosserat Closure](../../../common/q-g47-substrate-scale-cosserat-closure.md) — ν_vac=2/7 upstream derivation

### The Hypothesis (Axiom 3 spatial-vs-temporal refractive-index split)

Per Axiom 3 (Minimum Reflection Principle on K4 Cosserat micropolar lattice) + Axiom 1 (K4 substrate with $\nu_{vac} = 2/7$ trace-reversed Poisson ratio), gravity polarizes the local refractive index of the LC vacuum **anisotropically** between spatial and temporal coordinate components. The split is canonical:

$$
n_s = 1 + (9/7)\varepsilon_{11}, \qquad n_t = 1 + (2/7)\varepsilon_{11}, \qquad \Delta n = n_s - n_t = \varepsilon_{11}
$$

where:
- $\nu_{vac} = 2/7$ (canonical K4 Poisson ratio; `ave.core.constants.NU_VAC`)
- $9/7 = 1 + \nu_{vac}$ (spatial coefficient with DC unit)
- $2/7 = \nu_{vac}$ (temporal coefficient)
- $\varepsilon_{11}(r) = 7GM/(c^2 r)$ (canonical Earth strain per `ave.gravity.principal_radial_strain` engine; factor 7 from K4 lattice's 7-mode compliance manifold)

The 9/7 and 2/7 **ARE the $\nu_{vac} = 2/7$ Poisson-ratio numbers** — making this experiment a direct test of the substrate's K4 Cosserat lattice structure.

### The Test Protocol

Split an electron matter-wave across a macroscopic Mach-Zehnder baseline (canonical: 1 m vertical-vs-horizontal). The two paths physically traverse different local densities of the Earth's gravitational VSWR. Per Δn = ε_11, the two paths experience deterministic differential phase velocity, inducing a measurable, macroscopic topological phase shift.

**Required apparatus**:
- 1 m macroscopic vertical-vs-horizontal Mach-Zehnder baseline (vibration-isolated)
- 100 eV coherent electron source (specialized — TEM-class or atom-chip-derived)
- Hard vacuum (~$10^{-9}$ Torr; electron de Broglie wavelength preservation over 1m baseline ≈ $10^{10}$ wavelengths)
- Phase-stable interferometer with sub-rad resolution
- Stray E/B field shielding across baseline

### The Falsification Metric

At canonical Earth strain $\varepsilon_{11}(R_\oplus) = 7GM_\oplus/(c^2 R_\oplus) \approx 4.873 \times 10^{-9}$ (factor-7 corrected 2026-05-17 per `principal_radial_strain` engine):

$$
\boxed{\Delta\Phi \approx 250\text{ rad on 1-m baseline at 100-eV electron energy}}
$$

Live-fire confirmed at **249.6394 rad** per [`electron_interferometry_parallax.py`](../../../../../src/scripts/vol_2_subatomic/electron_interferometry_parallax.py) (canonical-corrected 2026-05-17; prior matrix value 35 rad inherited a factor-7-low driver bug — script used naive Newtonian $\phi/c^2$ instead of canonical $7\phi/c^2$).

If the oscilloscope registers no phase difference between the two paths at this magnitude, the framework is falsified. If it reads ~250 rad, the K4 Cosserat substrate's anisotropic Poisson-ratio split is empirically validated at electron-de-Broglie-wavelength scale.

### Standard physics counterfactual

GR + standard QM predicts **isotropic** refractive index from gravitational time dilation alone — no spatial-vs-temporal split. The 9/7 vs 2/7 anisotropy is a STRICT consequence of K4 Cosserat micropolar Poisson-ratio anisotropy derived from Ax1 + Ax3. Null observation kills Ax3 (Lorentz-parity-violation mandate); no graceful framework revision possible.

### ν_vac=2/7 cascade triangulation (F-severity)

C11 is one of three independent observables that converge on $\nu_{vac} = 2/7$:

| Cascade node | Observable | Status |
|---|---|---|
| **C1-BH-RING** | $r_{sat} = 7 M_g$ + $\omega_R M_g = 18/49$ via $\nu_{vac}=2/7$ | **FULL PASS** (Phase 5 closure 2026-05-18; $-0.45\%$ mean $\omega_R$; $-0.47\%$ mean $\tau$ across 3 LIGO events) |
| **C11-MACH-ZEHNDER** (this leaf) | $n_s = 1 + (9/7)\varepsilon_{11}$ vs $n_t = 1 + (2/7)\varepsilon_{11}$ | **PENDING** — driver canonical; facility partnership search |
| **C12-G-STAR** | $g_* = 7^3/4 = 85.75$ effective DOF vs SM 106.75 | LISA primordial-GW wait (~2035) |

**Triangulation logic**: ALL THREE converging on $\nu_{vac} = 2/7$ at three independent scales (BH-class compact-object dynamics + atomic-scale interferometry + cosmological mode-counting). **Simultaneous FAIL of any one = framework-level falsification of K4 Cosserat substrate hypothesis.** C11 is the only TERRESTRIAL bench-class triangulation node (C1 is data-already-acquired; C12 multi-decade facility wait).

### Outcome adjudication (Phase 3 of sub-epic)

Pre-registered Outcome A/B/C/D criteria per `ave-discrimination-check`:

| Outcome | Interpretation |
|---|---|
| **A** (~250 rad observed at predicted magnitude) | **ν_vac=2/7 triangulation node 2 anchored.** Combined with C1 FULL PASS → 2-of-3 cascade nodes confirmed; framework-level support for K4 Cosserat substrate at 30+ OOM cross-scale evidence (BH-class km + atomic-scale m). **Foreword-promotion-grade**. |
| **B** (phase shift detected but magnitude differs) | Partial — spatial-vs-temporal split exists; coefficient requires structural revision (9/7 or 2/7 prefactor scale-dependent?) |
| **C** (no phase shift OR shift consistent with classical GR time-dilation only) | **Ax3 + Ax1 K4 Cosserat substrate hypothesis dies.** Cascade walk-back: C1 PASS at LIGO-scale doesn't generalize to electron-scale → major structural finding (framework-killing). |
| **D** (phase noise dominates → 1-m baseline insufficient) | **Escalate to space-baseline interferometer** (km-class in space; decade-class wait). Driver predicts ~250-rad SNR comfortable margin; if observed phase-noise floor dominates, suggests facility-specific upgrade path. |

### Engineering substrate status

| Asset | Location | State |
|---|---|---|
| Driver | [`src/scripts/vol_2_subatomic/electron_interferometry_parallax.py`](../../../../../src/scripts/vol_2_subatomic/electron_interferometry_parallax.py) | ✓ Canonical-corrected 2026-05-17; live-fire confirms 249.6394 rad |
| Canonical strain engine | [`src/ave/gravity/__init__.py`](../../../../../src/ave/gravity/__init__.py) `principal_radial_strain` | ✓ Canonical (factor-7 derivation per Vol 3 Ch 9) |
| Canonical Poisson ratio | [`src/ave/core/constants.py`](../../../../../src/ave/core/constants.py) `NU_VAC` | ✓ Exact 2/7 |
| Hardware | None — Core-only; **facility partnership required** | No PCBA design; no sibling repo (unlike A1-HOPF or PONDER family); C11 needs external collaborator with 1-m electron interferometer |
| Pre-registration | None yet | Phase 2 gate (deferred until facility partnership confirms apparatus parameters) |

### What's deferred

- **Phase 0 facility partnership search**: literature survey of electron-interferometer SOTA (candidate facilities: Hasselbach group Tübingen ~10cm electron interferometer; LENS Italy m-scale atomic interferometer; NIST atom-chip / electron-microscope facilities; TEM/SEM holography centers); facility candidate verification (which can actually do 1m baseline + 100 eV + hard vacuum)
- **Phase 1 pre-registration**: canonical pre-reg with predicted phase shift at facility-specific parameters (baseline, electron energy, integration time, expected noise floor); pre-register BEFORE any measurement per `ave-prereg` discipline
- **Phase 2 measurement collaboration**: multi-month-to-year cycle with facility partner
- **Phase 3 outcome paper-template** (IF Outcome A lands): per `ave-ip-divide-discipline` Step 3, draft public-theory-level result template (no application IP since C11 has no proprietary bench design)

### IP-divide status

C11 has **NO application IP** at current state. The experiment is:
- Public-theory prediction (Δφ ≈ 250 rad via K4 Cosserat Poisson-ratio anisotropy)
- Public-theory framing (ν_vac=2/7 cascade triangulation with C1 + C12)
- Generic experimental scope ("use your 1m electron interferometer to measure differential phase between vertical + horizontal baselines")

No proprietary bench design because Grant isn't designing the bench — facility scientists already have the apparatus. C11 is essentially: "you have the interferometer, here's our prediction, would you measure it?"

If C11 evolves to co-designed 1m interferometer + specific collaboration → application IP emerges → revisit per `ave-ip-divide-discipline` + [`promotion-workflow-template.md`](../../../../../_orchestration/experimental/promotion-workflow-template.md).

### Regime classification (per canonical regime taxonomy)

| Axis | C11 classification |
|---|---|
| **Spatial Regime I-IV** (per [`four-regimes.md`](../../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md)) | **Regime I** — Earth $\varepsilon_{11} \sim 5 \times 10^{-9}$ deep in Regime I (sub-yield linear) |
| **Power-Domain θ** (per [`orbital-friction-paradox.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md)) | **Reactive cycling** — quantum interference is reactive (θ → 90°); lossless within coherence-time |
| **Temporal regime** (per [`temporal-saturation-regime-classifier.md`](../../../common/temporal-saturation-regime-classifier.md)) | **Lossless** — $\delta_{\text{AVE}} \to 0$ (electron coherence over 1m baseline; no saturation events) |

### Cross-references

- [Vol 2 Ch 7 §Gravitational Parallax Interferometry](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md) lines 49-53 — canonical physics derivation
- [Matrix row C11-MACH-ZEHNDER](../../../common/divergence-test-substrate-map.md) — Predictions + Lifecycle + Execution rows + ν_vac=2/7 cascade Mermaid diagram
- [Q-G47 Substrate-Scale Cosserat Closure](../../../common/q-g47-substrate-scale-cosserat-closure.md) — ν_vac=2/7 upstream derivation (Sessions 19 closure 2026-05-18; ξ_K1=8/3, ξ_K2=32, ν_vac unchanged as algebraic Poisson identity at K=2G operating point)
- [C1-BH-RING canonical leaf](../../../vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md) — ν_vac=2/7 cascade node 1 (FULL PASS Phase 5 2026-05-18)
- [C12-G-STAR canonical leaf](../../../vol2/nuclear-field/ch10-open-problems/g-star-derivation.md) — ν_vac=2/7 cascade node 3 (LISA wait)
- Sub-epic [`exp-c11-mach-zehnder.md`](../../../../../_orchestration/experimental/c11-mach-zehnder/exp-c11-mach-zehnder.md) + Sim audit [`exp-c11-mach-zehnder-sim-audit.md`](../../../../../_orchestration/experimental/c11-mach-zehnder/exp-c11-mach-zehnder-sim-audit.md)

### Status (2026-05-20 EOD++)

**Driver canonical-ready; sim-audit ✓ NO DRIFT; Phase 0 facility partnership search initiating.** No blocking work on AVE-side. Bottleneck is external facility partnership establishment.

---
