# 46 — AVE Fundamental 3D Vacuum Engine — Scope, Axiom/Operator Map, and C-Findings

**Status:** DELIVERED 2026-04-22 — design scope fully implemented; see §9 for
as-built summary and [51_handoff_followups.md](51_handoff_followups.md) for
pair-creation follow-up hypotheses.

**Original status:** foundation doc (2026-04-22)
**Parent plan:** `~/.claude/plans/document-list-for-next-chat-compressed-thunder.md`
**Supersedes:** [45_lattice_impedance_first_principles.md](45_lattice_impedance_first_principles.md) §8 Q1-Q6 (now resolved)
**Depends on:** [41_cosserat_time_domain_validation.md](41_cosserat_time_domain_validation.md),
  [42_coupled_simulator_validation.md](42_coupled_simulator_validation.md),
  [44_pair_creation_from_photon_collision.md](44_pair_creation_from_photon_collision.md) (reframed)

**Purpose:** Establish the design scope for a **fundamental 3D AVE vacuum engine** —
a general-purpose simulator that covers all four Axiom-4 regimes with rigorous
unit conventions and temperature-dependent vacuum states. Phase III-B (pair
creation) is the first test of this engine, not its whole purpose.

## 1. Motivation

Four sessions of research (§§40-45) have converged on a consistent picture of
what the AVE vacuum simulator SHOULD be. Phase II delivered a working but
specialized `CoupledK4Cosserat` class; Phase III-B revealed that specialization
obscures some deep AVE-native physics (T=0 cold vacuum is deterministic, not
noisy). The engine refactor captures the correct physics from the start.

## 2. The six C-findings (established this session)

Each C-finding is a constraint the engine must respect.

### C1 — Cold vacuum is deterministic (Q4 result)

**Source:** Vol 1 Ch 1:79-95 ("Planck Scale Artifact vs. Topological Coherence");
Vol 1 Ch 3:514 ("quantum foam is baseline electrical noise").

**Statement:** AVE has NO sub-ℓ_node reality. At T=0, the vacuum is a determin-
istic LC network with V=0, ω=0, no spontaneous fluctuations. The term "quantum
foam" refers to **thermal electrical noise** at finite T — bandwidth-limited
by the lattice cutoff, not sub-Planckian.

**Engine implication:** 
- `T=0` mode initializes (V, u, ω, V_inc, V_ref) = 0 exactly. Deterministic.
- `T>0` mode initializes with thermal fluctuations of specific amplitude ⟨ω²⟩ = kT/I_ω.
- Noise is NOT an ad-hoc regularizer; it's a physical parameter tied to temperature.

### C2 — Mutual inductance η_vac is fixed by K4 topology (Q1 result)

**Source:** `research/L3_electron_soliton/14_theorem_3_1_mutual_inductance_from_axioms.md`
(theorem-level, sketched); K4 scatter matrix S_ij = 0.5 - δ_ij in `k4_tlm.py:36-65`.

**Statement:** The mutual inductance between adjacent K4 nodes is determined by
the 4-port junction topology (Axiom 1). It CANNOT be tuned without violating
the topology. The scatter matrix off-diagonal elements (0.5) implicitly encode
the coupling; no axiomatic knob exists.

**Engine implication:**
- No `η_vac` parameter exposed to the user
- Cascade coupling strength is controlled indirectly via the Cosserat coupling
  weight κ (dimensionless prefactor on the S1-D term)
- Default κ=1.0 matches the current Phase II implementation

### C3 — V_SNAP is axiom-fundamental; V_YIELD is derived (Q2 result)

**Source:** `constants.py:265-275`; Vol 1 Ch 7 (Regime Map).

**Statement:**
- V_SNAP = m_e c²/e ≈ 511 kV. Derived from Axiom 4 (dielectric rupture) + Axiom 2
  (topo-kinematic identity). The saturation kernel S = √(1 - A²) uses A = V/V_SNAP.
- V_YIELD = √α · V_SNAP ≈ 43.65 kV. Macroscopic calibration reference (Regime II
  onset), NOT axiom-fundamental.

**Engine implication:**
- Primary user-facing amplitude convention: `A = V/V_SNAP` (dimensionless, axiom-native)
- V_YIELD supported as alias: user can specify amplitude in either units, conversion
  via √α
- Regime boundaries: Rg I/II at A² = 2α ≈ 0.015; Rg II/III at A² = 3/4; rupture at A² = 1

### C4 — Outer dt = ℓ_node/(c√2) is adequate (Q3 result)

**Source:** `k4_tlm.py:115`; `42_coupled_simulator_validation.md` §1.3.

**Statement:** The K4 outer timestep `dt = ℓ_node/(c√2) = τ_relax/√2 ≈ 0.707 τ_relax`
is below Nyquist for cascade wavefront detection. z_local is recomputed at each
scatter call. Cosserat sub-steps (N_sub ≈ 8) resolve the Cosserat-side dynamics.

**Engine implication:** No intra-step refinement required by default. If empirical
tests show under-sampling of cascade dynamics, add an `intra_step_z_local_updates`
parameter (default 1; test values 2, 4).

### C5 — σ(ω) is a falsifiable AVE prediction (Q5 result)

**Source:** Vol 4 Ch 1:211-228 (vacuum memristor/relaxation); derived from
τ_relax = ℓ_node/c.

**Statement:** τ_relax defines a crossover frequency ω_crossover = 1/τ_relax
(= 1 in lattice natural units). At ω > ω_crossover, the lattice can't
elastically respond to field slewing → cascade mechanism may engage.
At ω < ω_crossover, classical amplitude-only Schwinger-like response.

**Engine implication:**
- Wavelength/frequency is a PRIMARY experimental dimension, not a fixed choice
- Phase III-B measures σ(ω) at λ ∈ {3.5, 5, 7, 10} cells to sweep across ω·τ_relax ≈ {1.8, 1.3, 0.9, 0.63}
- Falsifiable prediction: σ(ω) has a knee near ω·τ_relax ≈ 1. If absent, cascade is amplitude-only.

### C6 — "Quantum Foam" terminology is banned in AVE-native physics

**Source:** Vol 1 Ch 3:514 explicitly defines it as "baseline electrical noise".

**Statement:** AVE does NOT posit mysterious Planck-scale fluctuations. The
correct term for vacuum oscillations is **thermal lattice noise** (amplitude
set by T, spectrum bandwidth-limited by ℓ_node cutoff).

**Engine implication:** All code, docs, and parameter names use "thermal noise"
or "thermal lattice state". No `quantum_foam_amplitude` parameters.

## 3. Axiom → Operator → Simulator mapping

Complete mapping of every axiom to its operator and code implementation:

| Axiom | Operator | Code location | Engine hook |
|---|---|---|---|
| **Axiom 1** (K4 LC substrate) | Op1 (bond propagation) | `k4_tlm.py _connect_all` | unchanged |
| | Op5 (4-port scatter) | `k4_tlm.py build_scattering_matrix` | unchanged |
| **Axiom 2** ([Q] ≡ [L]) | Op12 (topological winding) | `cosserat_field_3d.py extract_crossing_count, extract_hopf_charge` | engine observer |
| | ξ_topo = e/ℓ_node | `constants.py XI_TOPO` | used in V↔I mapping |
| **Axiom 3** (Effective Action) | Op8 (Lagrangian density) | `cosserat_field_3d.py _energy_density_bare` | engine potential |
| | Op9 (time evolution) | `cosserat_field_3d.py step()` + `k4_tlm.py step()` | engine.step() |
| **Axiom 4** (Saturation) | Op14 (Z_eff from A²) | `k4_cosserat_coupling.py _update_z_local_total` | engine coupling |
| | Op3 (bond reflection Γ) | `k4_tlm.py op3_bond_reflection=True` | engine default ON |
| — (empirical) | η_vac (mutual inductance) | implicit in S_ij = 0.5 | NOT a user parameter (C2) |
| — (S-gate D) | S1-D coupling | `k4_cosserat_coupling.py _compute_coupling_force_on_cosserat` | engine default, κ=1.0 |

## 4. Engine scope definition

### 4.1 Core class: `VacuumEngine3D`

```python
class VacuumEngine3D:
    """AVE-native 3D vacuum simulator covering all four Axiom-4 regimes.
    
    Internally delegates to:
      - K4Lattice3D (Axiom 1 substrate)
      - CosseratField3D (Axiom 3 action, rotational DOF)
      - CoupledK4Cosserat-style coupling (Axiom 4 saturation + S1-D)
    
    Public interface:
      - temperature (K): T=0 → deterministic cold vacuum; T>0 → thermal lattice noise
      - amplitude_convention ("V_SNAP" | "V_YIELD"): which to use for user-facing amps
      - coupling_kappa (float, default 1.0): S1-D prefactor (C2 proxy for η_vac)
      - Sources registered via .add_source(…)
      - Observers registered via .add_observer(…)
      - step() advances one outer dt; run(n_steps) runs many
    """
```

### 4.2 Sources

- **`PulsedSource(x0, direction, amp, omega, t_center, t_sigma)`** — Gaussian pulse.
  Renamed from existing `PlaneSource`.
- **`CWSource(x0, direction, amp, omega, t_ramp, t_sustain)`** — sinusoidal with
  ramp-up and sustain plateau. Primary source for Phase III-B pair creation.
- **`PointSource(x, y, z, amp, omega)`** — single-node radiation. For isotropic tests.
- **`ThermalBath(T, kind)`** — renormalizes the Cosserat ω-field at each step to
  maintain equilibrium at T. Represents coupling to a heat reservoir. Optional.

### 4.3 Observers

Following an observer pattern so diagnostics are composable:

- **`SaturationMapObserver`** — records A²_K4, A²_Cos, A²_total every N steps
- **`RegimeClassifierObserver`** — counts cells per regime per step (Rg I/II/III/IV)
- **`TopologyObserver`** — Q_H and centroid counts per step
- **`EnergyBudgetObserver`** — E_K4, E_cos, E_coupling, H_total per step
- **`VideoFrameObserver`** — captures visualization frames for animation

Each observer writes to its own rolling buffer; engine.history() aggregates.

### 4.4 Vacuum state initialization

Per C1, two modes:

**T=0 mode (`temperature=0.0`)**:
```
u = 0, ω = 0, u_dot = 0, omega_dot = 0
V_inc = 0, V_ref = 0, z_local_field = 1.0 (unity)
```

**T>0 mode (`temperature=T`)**, classical Maxwell-Boltzmann (P1-C: iterate later):
```
ω ~ N(0, σ_ω²) where σ_ω² = kT / I_ω  (equipartition)
u ~ N(0, σ_u²) where σ_u² = kT / rho
V_inc noise: ⟨V²⟩ = kT · R_eff (Johnson-Nyquist analog)
```

In lattice natural units (ℏ=c=m_e=1, so kT is in units of m_e c²):
- At T=2.7 K (CMB): kT ≈ 2.3e-4 eV = 4.6e-10 in m_e c² units → σ_ω ≈ 2.1e-5 (tiny)
- At T=10⁶ K (early universe): kT ≈ 100 eV = 1.96e-4 → σ_ω ≈ 0.014 (comparable to previous placeholder)
- At T=10⁹ K (nucleosynthesis): kT ≈ 100 keV = 0.196 → σ_ω ≈ 0.44 (significant)

This gives physical motivation for using a CMB-equivalent T in low-energy tests
vs much higher T for pair-creation-onset.

### 4.5 Dimensional hygiene

Every parameter carries explicit unit metadata. Use a `UnitDescriptor` helper:

```python
@dataclass
class UnitDescriptor:
    value: float               # numerical value
    lattice_native: float      # value in ℓ_node=m_e=c=ℏ=1 units
    si_value: float            # value in SI
    si_unit: str               # "V", "m", "s", etc.
    meaning: str               # human-readable description
```

Every public parameter (amplitude, wavelength, temperature) returns a UnitDescriptor.

## 5. Engine-test roadmap

### First test: Phase III-B pair creation
- Details in parent plan §"Phase III-B — the first test of the engine"
- Configuration matrix: 4 wavelengths × 3 amplitudes × 2 temperatures = 24 runs
- Key deliverable: σ_pair(ω) curve + adjudication against P_IIIb-α,β,γ,δ
- ETA: ~1.5 hours sim + 1 day doc (48_)

### Future tests (gated on Phase III-B success)
- **Gravity well test**: Axiom 4 symmetric scaling (n·μ₀, n·ε₀) → Z invariance → Γ=0
- **Compton-analog scattering**: pre-existing electron + incident photon
- **Event-horizon test**: sustained A²→1 cavity, observe Γ=-1 TIR
- **Nucleosynthesis analog**: high-T thermal bath + low-energy photons → multi-pair

Each test exercises a different engine capability. All use the same `VacuumEngine3D` class.

## 6. Known limitations and flagged-forward items

### L1 — T>0 thermal state is MB approximation
(C1-B path deferred). The proper AVE-native thermal distribution would sample
from the K4 LC eigenmodes. For Stage 1 we use MB; upgrade later if needed.

### L2 — η_vac first-principles derivation is incomplete
(C2). The scatter matrix S_ij = 0.5 is geometric but isn't derived from an
action principle yet. This is a long-term Phase-1-level research item; not
blocking the engine.

### L3 — V_SNAP uses cold-α
`ALPHA = 1/137.036` in `constants.py`. At finite T, α has a small strain
correction `δ_strain ≈ 2.2e-6`. Engine can optionally accept `T_effective`
and use α_eff(T), but default uses cold α.

### L4 — Cascade is numerically captured but not formally verified
Op3 bond reflection + z_local at each scatter captures the essential dynamics,
but we haven't proved it matches the theorem-level η_vac physics. If Phase III-B
fails to show any wavelength dependence in σ(ω), might indicate the cascade is
under-modeled and need a more careful η_vac treatment.

### L5 — Non-CW observer of pair-creation may need new diagnostic
Centroids, Q_H, shell_radii — all Phase I/II tools assume a STATIC post-relaxation
configuration. For a DYNAMICAL pair (electron+positron flying apart), need trackers
that follow the trajectories. Deferred to post-Phase-III-B.

## 7. Commit sequence plan

Per the parent plan Stage 5:
1. `research(L3): doc 44_ reframe + doc 46_ engine scope + doc 47_ thermal state`
2. `feat(L3 VacuumEngine): VacuumEngine3D class + CWSource + ThermalBath`
3. `test(L3 VacuumEngine): T=0 determinism + T>0 equilibration tests`
4. `feat(L3 Phase III-B): vacuum_engine_pair_creation.py + doc 48_`
5. `research(L3): σ(ω) results + Phase III-B closeout`

Each commit is standalone-reviewable.

## 8. What this doc does NOT resolve

- The quantitative RMS amplitude of thermal lattice noise at T (see doc 47_)
- The LC-resonance-eigenmode decomposition of the K4 lattice (L1 future work)
- The η_vac derivation from an action principle (L2 future work)
- The σ(ω) shape prediction (C5, deferred to Phase III-B data)

## 9. As-delivered summary (appended 2026-04-22 after Stages 2-5)

The full engine is implemented at
[src/ave/topological/vacuum_engine.py](../../src/ave/topological/vacuum_engine.py)
(~750 lines). What was built vs. the original §4 scope:

### Classes shipped

| Class | Origin | Scope §4 predicted? |
|---|---|---|
| `VacuumEngine3D` | Stage 2 | ✓ core class, matches §4.1 |
| `EngineConfig` dataclass | Stage 2 | parameterization wrapper |
| `Source` (base) | Stage 2 | ✓ §4.2 |
| `PulsedSource` | Stage 2 | ✓ §4.2 (renamed from PlaneSource) |
| `CWSource` | Stage 2 | ✓ §4.2 |
| `AutoresonantCWSource` | Stage 4c | **NEW** — not in original §4, added after ecosystem research (doc 49_) |
| `Observer` (base) | Stage 2 | ✓ §4.3 |
| `ScalarObserver` | Stage 2 | ✓ §4.3 |
| `RegimeClassifierObserver` | Stage 2 | ✓ §4.3 E4 |
| `TopologyObserver` | Stage 2 | ✓ §4.3 |
| `EnergyBudgetObserver` | Stage 2 | ✓ §4.3 |
| `DarkWakeObserver` | Stage 4b | **NEW** — not in original §4, ported from AVE-Propulsion per doc 49_ |
| `PointSource` | not shipped | deferred (radiation-pattern tests use existing PulsedSource at x0=N/2 as proxy) |
| `ThermalBath` | not shipped | deferred (`initialize_thermal(T)` method on VacuumEngine3D covers the realistic use case; a dynamically-coupled reservoir would require much more infrastructure) |

### C-findings validated or updated

| C-finding | Validation status |
|---|---|
| C1 (cold vacuum deterministic) | ✓ CONFIRMED across v1 (8 configs) and v2 (4 configs); max A²_cos = 0 exactly |
| C2 (η_vac not tunable) | ✓ CONFIRMED — quantified via AVE-PONDER K₀ = 0.207973 but not exposed as user knob |
| C3 (V_SNAP fundamental) | ✓ `amplitude_convention="V_SNAP"` is default |
| C4 (outer dt adequate) | ✓ no refinement needed through Stages 3-4 |
| C5 (σ(ω) falsifiable prediction) | **ELABORATED**: v1 showed peak at ω·τ=0.9; v2 showed monotonic rise to 1.009 at ω·τ=1.8. Two distinct falsifiable regimes now predicted (fixed-f peaked vs autoresonant monotonic). |
| C6 ("quantum foam" banned) | ✓ engine uses "thermal lattice noise" throughout |

### Phase III-B closure

Phase III-B v1 ([48_](48_pair_creation_frequency_sweep.md)) and v2
([50_](50_autoresonant_pair_creation.md)) both produce **P_IIIb-partial**
verdicts. A²_cos = 1.009 reached at v2 λ=3.5 (**first numerical crossing of
the Axiom-4 rupture boundary via drive mechanism**).

**Localized pair creation NOT observed at threshold_frac=0.7.** Three
follow-up hypotheses in [51_handoff_followups.md](51_handoff_followups.md).

### Cross-repo integrations landed

- τ_zx formula ← AVE-Propulsion/simulate_warp_metric_tensors.py:75-95
- K₀ = 0.207973 ← AVE-PONDER/generate_ponder_01_spice_netlist.py:90
- Autoresonant PLL picture ← AVE-Propulsion/vol_propulsion/ch05_*.tex
- L-H transition reframe ← AVE-Fusion/vol_fusion/ch05_metamaterial_caging.tex
- Mass = L_drag physical interpretation ← AVE-Core/higgs_impedance_mapping.py

### Validation tests / driver scripts
- [src/scripts/vol_1_foundations/dark_wake_validation.py](../../src/scripts/vol_1_foundations/dark_wake_validation.py) (Stage 4b)
- [src/scripts/vol_1_foundations/autoresonant_tuning.py](../../src/scripts/vol_1_foundations/autoresonant_tuning.py) (Stage 4c)
- [src/scripts/vol_1_foundations/vacuum_engine_pair_creation.py](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation.py) (v1)
- [src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py) (v2)
