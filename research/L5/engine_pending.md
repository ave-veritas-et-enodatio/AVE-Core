# Engine Pending Changes

Mirrors `src/ave/` and includes `manuscript/predictions.yaml` (the structured prediction manifest is engine-side data). Each pending change for a module sits under its file heading; if multiple research docs converge on the same file or symbol, their entries cluster together. Empty headings are placeholders — the file IS the index of the engine.

**Entry schema:**

```
- **[E-NNN] <short concept title>**
  - **Sources:** doc_NN §X.Y (`<sha>`, YYYY-MM-DD); doc_MM §A.B (`<sha>`, YYYY-MM-DD)
  - **Action:** <what specifically changes — function signature, new helper, refactor, test, etc.>
  - **Status:** queued | in-review | applied (`<sha>`)
  - **Cross-refs:** E-NNN, E-MMM
```

`E-NNN` IDs are monotonic and shared with `manuscript_pending.md`. Next free ID is recorded in `manuscript_pending.md`.

For engine entries, the **Action** field should specify the symbol (class, function, or constant) being touched when the change is more localized than a whole file.

---

## src/ave/core/

### `constants.py`

- **[E-035] `TAU_RELAX_SI` / `TAU_RELAX_NATIVE` constant — APPLIED**
  - **Sources:** [doc 59_ §10.1:L580-L588](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md#L580) (`03cb9d5`, 2026-04-23)
  - **Action:** add `TAU_RELAX_SI = L_NODE / C_0` (≈ 1.288e-21 s) and `TAU_RELAX_NATIVE = 1.0` to `constants.py`. Required precondition for E-036 memristive Op14 work.
  - **Status:** applied (`03cb9d5`) — verified at [`constants.py:231-232`](../../src/ave/core/constants.py#L231)
  - **Cross-refs:** E-036, E-029
### `grid.py`
### `node.py`
### `regime_map.py`
### `universal_operators.py`

- **[E-044] Cascade-saturation operator candidate — Op_cascade_saturation OR doc-only justification**
  - **Sources:** [doc 45_ §4.2:L183-L204](../L3_electron_soliton/45_lattice_impedance_first_principles.md#L183) (`fa89466`, 2026-04-22)
  - **Action:** doc 45_ §4.2 identifies that no current AVE operator captures **cascade saturation** — the wave's progressive degradation through Regimes II → III → IV as it propagates through saturated lattice regions. Op14 Z_eff captures local instantaneous response; cascade is the path-integrated effect. Either: (a) introduce a new universal operator `Op_cascade_saturation` capturing this (potential Op23 in the canonical 22 + N catalog), OR (b) document why composition of Op2 + Op3 + Op14 already covers cascade (likely the right answer — cascade may be an emergent observable, not a primitive operator). Decision affects how cosmological-scale (BH approach, gravitational lensing, etc.) calculations should be structured.
  - **Status:** queued
  - **Cross-refs:** E-031

- **[E-069] Strain-regime energy-conservation invariants — universal operator + engine assertion + unit tests — EMPIRICALLY VINDICATED, REQUIRED PRE-MOVE-9**
  - **Sources:** Synthesizer/Grant dialogue 2026-04-27 — slowing-vs-damping disambiguation (A-010); doc 54_ §6 Phase 4 asymmetric saturation (E-002); Vol 3 Ch 11 Ŝ entropy operator (E-022); Vol 3 Ch 21 BH interior Regime IV rupture
  - **Action:** corpus distinguishes three strain-regime energy-conservation behaviors but engine doesn't enforce the distinction at the invariant-checking level. Three pieces of work:
    - **(a) Universal operator:** new `universal_strain_regime_classifier(A²_total, S_μ, S_ε, chirality)` returning a regime tag from {I/II/III-symmetric, III-asymmetric, IV-rupture}. Wraps E-031 four-regime classifier with the additional asymmetric-vs-symmetric + rupture-vs-non-rupture axes. ~80 LOC, in `src/ave/core/universal_operators.py`.
    - **(b) Engine assertion:** add a per-step optional diagnostic `engine.check_energy_conservation(tol=1e-6)` that verifies H = T + V is constant when no rupture cells are present (Regime I/II/III). Returns warning if dH/dt > tol AND no Regime IV cell active — flags hidden numerical dissipation that would confound the static-fixed-point reading. ~30 LOC.
    - **(c) Unit tests:** new `test_strain_regime_energy_conservation.py` covering:
      - `test_op14_uniform_slowing_conserves_energy` — uniform A² ∈ {0.1, 0.5, 0.95} across lattice, no rupture, run engine 100 steps, assert H constant within machine precision (modulo PML losses if PML active)
      - `test_asymmetric_saturation_conserves_energy` — chiral RH seed (h_local > 0) with S_μ ≠ S_ε, no rupture, H constant
      - `test_rupture_regime_dissipates_energy` — A² → 1 forced at one site, verify H decreases over 100 steps; verify Vol 3 Ch 11 Ŝ entropy operator returns positive Ŝ at the rupture cells
      - `test_strain_regime_classifier_boundaries` — seed configurations at each regime boundary, classifier returns correct regime tag
      - `test_static_fixed_point_is_not_damped` — re-run E-060 Move 5 setup at A²_core ≈ 0.95, confirm H constant across t ∈ [50P, 200P] plateau (validates A-009 reading that "static fixed point" is slowing-frozen, not damped)
    - ~200 LOC tests + integration with `test_engine_saturation_invariants.py` (existing).
  - **Tests needed:** the test suite IS the deliverable for (c).
  - **Status:** **rationale partially weakened 2026-04-27 by Move 11b resolution.** Original rationale: 5.5% H_cos drift was unexplained, suggesting hidden numerical dissipation. Move 11b's Pearson matrix RESOLVED the drift as Op14 cross-sector trading (real physics, ρ(H_cos, Σ|Φ_link|²) = -0.990, H_total ≈ conserved). E-069 still valuable for general engine-invariant checks (rupture vs non-rupture energy conservation distinction, three-regime classifier, and detecting future numerical-dissipation cases) but the SPECIFIC load-bearing rationale (Move 11 H drift) no longer applies. **Reduce priority from "required-before-Move-9" to "Tier 2 cleanliness work."** Companion to E-038 (test_memristive_op14.py) and E-039 (Cosserat PML verification).
  - **Cross-refs:** A-010 (canonical methodology entry — A-010 articulates the three regimes; E-069 makes the distinction enforceable), A-009 (static-fixed-point reading — REVISED to hybrid pending Move 11b + E-069), A-011 (reactance gap — E-069 catches the engine-side cause), A-012 (Cosserat NOT in LC reactance — needs E-069 to distinguish numerical from physical), E-002 (asymmetric saturation, engine-side foundation), E-022 (Vol 3 Ch 11 Ŝ operator), E-031 (universal regime classifier), E-038, E-039, E-068 (Move 11 — empirical demonstration the 5.5% H drift exists), E-070 (Move 11b — clarifies whether interior cells confirm)

- **[E-031] New `universal_regime_classifier` operator (v4 refactor item)**
  - **Sources:** [doc 57_ §3.3:L175-L200](../L3_electron_soliton/57_universal_lattice_units_v4_refactor.md#L175) (`224cad0`, 2026-04-23); Vol 1 Ch 7:30-54 boundaries
  - **Action:** add new universal operator routing the four-regime classification (I_LINEAR/II_NONLINEAR/III_YIELD/IV_RUPTURED) at boundaries `r² < 2α`, `2α ≤ r² < 0.75`, `0.75 ≤ r² < 1`, `r² ≥ 1`. Currently these boundaries are hardcoded in [`vacuum_engine.py:151-153`](../../src/ave/topological/vacuum_engine.py#L151) as `_REGIME_I_BOUND_A2 = 2*ALPHA` etc. Routing through a canonical operator preserves the scale-invariance claim (the operator IS the canonical implementation; engine consumes it). Part of the v4 refactor (FUTURE_WORK G-10) — full refactor scope in doc 57_.
  - **Tests needed:** add to `test_universal_operators.py` — boundary classifications at exactly `2α`, `0.75`, `1.0` (boundary-inclusive semantics); cross-domain test using same operator on macroscopic V_yield (= √α·V_SNAP) AND subatomic V_SNAP — both should produce identical regime classifications when given the appropriate `r²`. Per doc 57_ §5.3 cross-scale regression suite.
  - **Status:** queued
  - **Cross-refs:** E-032, E-033
### `k4_tlm.py`

- **[E-021] Global `τ_relax` — flag for spatial-n(r) modulation in cosmological/strong-gravity work**
  - **Sources:** [doc 66_ §17.1:L507-L517](../L3_electron_soliton/66_single_electron_first_pivot.md#L507) (`a53ce1c`, 2026-04-25)
  - **Action:** engine currently uses τ_relax = ℓ_node/c as a global constant per Ax 1 + Ax 3. Per doc 66_ §17.1, time itself is a local clock rate from lattice strain (τ_local = n(r) · τ_unstrained). For weak-gravity / lab-scale work the global τ_relax is fine. For cosmological / strong-gravity work, τ_relax needs spatial n(r) modulation. Add a docstring note where τ_relax is defined, and flag the modulation as a future engine extension (not blocking). Consider exposing as `τ_relax_field(r)` interface in a future refactor.
  - **Status:** queued
  - **Cross-refs:** E-015

- **[E-033] Replace hand-rolled inline saturation/impedance/reflection with universal-operator calls (v4 refactor item)**
  - **Sources:** [doc 57_ §2.1:L80-L91](../L3_electron_soliton/57_universal_lattice_units_v4_refactor.md#L80) (`224cad0`, 2026-04-23)
  - **Action:** route the following inline implementations through canonical operators:
    - [`k4_tlm.py:227-232`](../../src/ave/core/k4_tlm.py#L227): `S_factor = np.sqrt(...)` → `universal_saturation`
    - [`k4_tlm.py:232`](../../src/ave/core/k4_tlm.py#L232): `z_strained = 1.0 / max(sqrt(S), 1e-6)` → `universal_dynamic_impedance`
    - [`k4_tlm.py:256-259`](../../src/ave/core/k4_tlm.py#L256): duplicate of above pattern
    - [`k4_tlm.py:333-346`](../../src/ave/core/k4_tlm.py#L333): `gamma = (z_B - z_A)/(z_B + z_A + eps); T = sqrt(1-gamma²)` → `universal_reflection` + `universal_power_transmission`
  - Hand-rolled inline implementations are a code smell; canonical operators are the only allowed code path for these physics. Part of v4 refactor (FUTURE_WORK G-10).
  - **Tests needed:** existing `test_axiom_4_vacuum_varactor.py` + `test_cross_domain_operators.py` + `test_cross_scale.py` must all pass unchanged (these pin the operator behavior; this entry just routes call sites through them). Add a regression-check test asserting K4-TLM scatter+connect output is bit-identical pre- and post-refactor at a fixed seed for at least one canonical config (Phase II validation seed).
  - **Status:** queued
  - **Cross-refs:** E-031, E-032

- **[E-012] Module docstring / comment — bare K4 single-bond ≠ LC tank**
  - **Sources:** [doc 69_ §2.1, §2.2](../L3_electron_soliton/69_bootstrap_chain_calibration.md) (`c830f07`, 2026-04-25)
  - **Action:** add a module-level docstring or top-of-class comment in `K4Lattice3D` (or wherever the LC-tank framing might be misread) noting: bare K4-TLM at the single-bond level produces grid dispersion (2-step alternation as the wave shuttles between A and B nodes at the discrete-time scatter+connect timescale). It does NOT manifest LC-tank Compton resonance — kinetic inductance lives in the Cosserat sector. The "simplest unknot $O_1$" is the smallest COUPLED (K4 + Cosserat) oscillator, not a bare K4 lattice bond. Prevents future agents from running single-bond tests expecting Compton resonance and concluding the engine is broken.
  - **Status:** queued
  - **Cross-refs:** E-002
### `fdtd_3d.py`
### `fdtd_3d_jax.py`
### `lbm_3d.py`

## src/ave/topological/

### `borromean.py`
### `combiner.py`
### `cosserat.py`
### `cosserat_field_3d.py`

- **[E-007] Coupled `total_s11_coupled` + `relax_s11_coupled` extending Cosserat-only `relax_s11`**
  - **Sources:** [doc 68_ §7.2, §11, §12.3](../L3_electron_soliton/68_phase_quadrature_methodology.md) (`3f6d544`, 2026-04-25); [doc 70_ §1 A31](../L3_electron_soliton/70_phase5_resume_methodology.md) (`e1f6eac`, 2026-04-25)
  - **Action:** existing [`cosserat_field_3d.py:974 relax_s11`](../../src/ave/topological/cosserat_field_3d.py#L974) operates on Cosserat-only state. Extend to a coupled-engine objective `total_s11_coupled(V_inc, V_ref, u, ω)` and a `relax_s11_coupled` driver. Two methodology branches surfaced:
    - **§11 plan:** AVE-Protein-style Lagrange-penalty enforcement of Ch 8 geometric constraints (d=1, R−r=1/2, R·r=1/4), per template at `AVE-Protein/protein_fold.py:97-177`.
    - **§12.3 corrected plan (preferred):** hard saturation reparameterization via `tanh` (bounds A² < 1 by construction), plus dual descent (Cosserat-energy AND $|S_{11}|^2$ in parallel) for falsifiability. NO Lagrange penalties on geometry/topology — Ch 8 constraints are natural equilibria per doc 03_ §4, not hard constraints.
  - **Tests needed:** new `test_coupled_s11_relax.py` covering: (i) reduces to Cosserat-only `relax_s11` when V_inc/V_ref = 0; (ii) tanh reparameterization keeps A² < 1 by construction (no escape to A² > 1); (iii) dual-descent path produces convergent (R, r) trajectories; (iv) Golden Torus seed remains UNSTABLE at coupled-engine scale (per A30/A32 — confirms E-001 falsification). Regression: `test_cosserat_field_3d.py` Cosserat-only `relax_s11` tests must still pass.
  - **Status:** queued
  - **Cross-refs:** E-009, E-011, A-004

- **[E-009] Phase-coherence diagnostic — `θ_pq(x)` and `coherence(x)` helpers**
  - **Sources:** [doc 68_ §7.3](../L3_electron_soliton/68_phase_quadrature_methodology.md) (`3f6d544`, 2026-04-25)
  - **Action:** add diagnostic helpers (location TBD — likely `cosserat_field_3d.py` or a new `diagnostics.py`). Per doc 68_ §7.3:
    - `θ_pq(x) = arg(V_inc^complex(x)) - arg(V_ref^complex(x))`
    - `coherence(x) = |cos(θ_pq(x) - π/2)|` — returns 0 at perfect 90° quadrature, 1 at 0°/180° (in-phase / anti-phase, dissipative). Aggregate to global mean + shell mean.
    - Phase-space winding number: sample $(V_{inc}(t), V_{ref}(t))$ at one bond over a Compton-period window, project onto 2D phase plane, count winding number — should equal 3 for the (2,3) electron eigenmode.
  - **Tests needed:** new `test_phase_coherence_diagnostic.py` covering: (i) coherence = 0 at exact 90° quadrature seed; (ii) coherence = 1 at in-phase / anti-phase seed; (iii) phase-space winding-number extractor returns 3 for an analytically-seeded (2,3) ansatz; (iv) returns 0 for a constant V_inc/V_ref pair.
  - **Status:** queued
  - **Cross-refs:** E-007

- **[E-034] Cosserat moduli audit — G, γ, ρ, I_ω, ε_yield, ω_yield require axiom derivations or explicit calibration markers**
  - **Sources:** [doc 57_ §1.2:L31-L46, §2.1:L89-L90, §3.5:L250-L262](../L3_electron_soliton/57_universal_lattice_units_v4_refactor.md#L31) (`224cad0`, 2026-04-23); [`cosserat_field_3d.py:520-531`](../../src/ave/topological/cosserat_field_3d.py#L520) (`G = G_c = γ = ρ = I_ω = 1.0, ε_yield = 1.0, ω_yield = π`)
  - **Action:** each Cosserat modulus needs either (a) axiom derivation citation (Vol 1 Ch 7:96 is emphatic: "A_c is derived from the four axioms — never fitted or empirical") OR (b) explicit code comment marking it as "engineering placeholder pending calibration" with a pointer to [`S_GATES_OPEN.md S4`](../L3_electron_soliton/S_GATES_OPEN.md). `ε_yield = 1` defensible under Vol 1 Ch 7:138 gravity-row unitary-strain convention; `ω_yield = π` is currently empirical. Per doc 02_ §9 Pinning-2 (queue [5] PARTIALLY-applied), Cosserat modulus pinning has algebraic chain `G = G_c = γ = ρ_vac = 1` from Axiom 1 Nyquist match — that derivation should be cited inline in the Cosserat code.
  - **Tests needed:** add `test_constants_derivation.py` (or extend existing) coverage: each modulus value asserted against its derivation chain + flagged with the corresponding `S_GATES_OPEN.md` reference if not derived. No behavior change; this is a discoverability/audit test.
  - **Status:** queued
  - **Cross-refs:** E-031, E-032

- **[E-036] Memristive Op14 — promote Φ_link from diagnostic to dynamical state; replace Op14 with full memristive form**
  - **Sources:** [doc 59_ §9 + §10.2:L543-L598](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md#L543) (`03cb9d5`, 2026-04-23)
  - **Action:** currently [`k4_tlm.py:122-132`](../../src/ave/core/k4_tlm.py#L122) accumulates Φ_link but it's unused in dynamics. To implement memristive behavior: (i) add per-bond or per-cell S(t) state variable initialized at S_eq(r_initial); (ii) replace Op14 in [`k4_tlm.py:229-260`](../../src/ave/core/k4_tlm.py#L229) with doc 59_ Eq. 9.2 using integrated S(t); (iii) integrate doc 59_ Eq. 9.1 via stable ODE integrator (implicit Euler or BDF, since τ_relax ≪ dt for some sims). ~50 LOC for K4. Similar extension to [`cosserat_field_3d.py:459-499`](../../src/ave/topological/cosserat_field_3d.py#L459) for Cosserat saturation kernels (S_μ, S_ε). ~70 LOC. Total ~120 LOC. Companion: E-038 test file. **Why deferred:** per doc 59_ §10.6 — derive before simulate, separate commit after derivation approved.
  - **Tests needed:** see E-038 (the new `test_memristive_op14.py` is a co-required deliverable — entry E-036 lands this code, entry E-038 lands its tests). Plus regression on `test_axiom_4_vacuum_varactor.py` — full memristive Op14 must converge to current Op14 in ω·τ ≪ 1 limit.
  - **Status:** queued
  - **Cross-refs:** E-035 (TAU_RELAX applied), E-037, E-038

- **[E-038] New test file `test_memristive_op14.py` (~200 LOC)**
  - **Sources:** [doc 59_ §10.4:L606-L615](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md#L606) (`03cb9d5`, 2026-04-23)
  - **Action:** when E-036 lands, add tests for: τ_relax constant value; full memristive Op14 → current Op14 in ω·τ ≪ 1 limit; Debye amplitude `|χ(ω)| = 1/√(1+(ωτ)²)`; peak shift to 0.9 under nonlinear drive (doc 59_ Eq. 6.3); energy conservation in closed loop (no spurious heating/cooling in interior). ~200 LOC.
  - **Status:** queued (follows E-036)
  - **Cross-refs:** E-036

- **[E-039] Cosserat-sector PML implementation (already partially landed; verify scope)**
  - **Sources:** [doc 58_ §4:L92-L150](../L3_electron_soliton/58_cosserat_pml_derivation.md#L92) (`8272583`, 2026-04-23); engine commit [`03cb9d5`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/03cb9d5) (Phase 5.5 Cosserat-sector PML); engine reference at [`cosserat_field_3d.py:719`](../../src/ave/topological/cosserat_field_3d.py#L719)
  - **Action:** verify Cosserat PML implementation is complete per doc 58_ §4. Specifically: (a) which fields get damped (§4.1) — confirm match; (b) attenuation profile (§4.2); (c) match K4 `pml_thickness` parameter (§4.3); (d) energy conservation in interior (§5); (e) exponential dissipation in PML region (§6); (f) composition with Ax4 saturation Op14 boundary (§7). If any sub-item is missing, file as separate sub-entry. Engine reference at line 719 is stub-citation; verify substance.
  - **Tests needed:** existing `test_cosserat_pml.py` should already cover (d) interior energy conservation and (e) exponential dissipation — confirm both. If composition with Op14 saturation (§7) not tested, add coverage.
  - **Status:** in-review (commit `03cb9d5` lands the work; need substance verification against doc 58_)
  - **Cross-refs:** E-036

- **[E-016] `initialize_electron_2_3_sector` — docstring warning that default `amplitude_scale=1.0` produces wrong empirical amplitude**
  - **Sources:** [doc 66_ §14.3:L347-L370](../L3_electron_soliton/66_single_electron_first_pivot.md#L347) (`a53ce1c`, 2026-04-25); [doc 34_ §9.4](../L3_electron_soliton/34_x4_constrained_s11.md) (`a9853d9`, 2026-04-22); engine commit `bcedb18` introduced the parameter
  - **Action:** [`cosserat_field_3d.py:783-829`](../../src/ave/topological/cosserat_field_3d.py#L783) currently defaults `amplitude_scale=1.0` which preserves the original `√3/2·π` peak. Per doc 34_ §9.4, the empirical bound-state amplitude is peak |ω| = 0.3π (= `amplitude_scale ≈ 0.3464`). Default-amplitude callers get a Regime III uniform-saturation blob, NOT the TIR-bounded electron. Add explicit prominent docstring warning at top of function (currently the warning is embedded mid-docstring at line 808-811). Consider also: changing default to 0.3464 with a `legacy_canonical_amplitude=False` opt-in, after auditing test-suite callers.
  - **Status:** queued
  - **Cross-refs:** E-006

- **[E-010] Phase-quadrature seeder — `initialize_quadrature_2_3_eigenmode`**
  - **Sources:** [doc 68_ §7.1](../L3_electron_soliton/68_phase_quadrature_methodology.md) (`3f6d544`, 2026-04-25)
  - **Action:** new seeder (likely in `cosserat_field_3d.py` or new `tlm_electron_soliton_eigenmode.py`) producing phase-coherent (V_inc, V_ref) at 90° quadrature with phase-space phasor tracing the (2,3) torus knot at $R_{phase} = \varphi/2$, $r_{phase} = (\varphi-1)/2$:
    - $V_{inc}(x, t_0) = A \cdot E(\rho_{tube}/r_{opt}) \cdot \cos(2\phi + 3\psi)$
    - $V_{ref}(x, t_0) = A \cdot E(\rho_{tube}/r_{opt}) \cdot \sin(2\phi + 3\psi)$
    - where $E$ is the hedgehog envelope, $\phi$ is toroidal angle, $\psi$ is poloidal angle. Cosserat (u, ω) seeded as conjugate of the K4 phasor pair, not as independent amplitudes.
  - **Tests needed:** add to `test_electron_tlm_eigenmode.py` (or new file): (i) seeder produces 90° phase relationship at every site; (ii) phase-space winding-number = 3 immediately post-seed (hooks into E-009 diagnostic); (iii) hedgehog envelope peaks at $r_{opt}$; (iv) Cosserat (u, ω) conjugate seeding consistency check.
  - **Status:** queued
  - **Cross-refs:** E-006, E-007
### `entanglement_thread.py`
### `faddeev_skyrme.py`
### `k4_cosserat_coupling.py`

- **[E-020] Module-level annotation that A28 (no `_compute_coupling_force_on_cosserat`) is the canonical configuration**
  - **Sources:** [doc 67_ §15:L707-L763](../L3_electron_soliton/67_lc_coupling_reciprocity_audit.md#L707) (`3fede52`, 2026-04-25); [doc 67_ §17:L845-L909](../L3_electron_soliton/67_lc_coupling_reciprocity_audit.md#L845)
  - **Action:** A28 inline comments exist at [`k4_cosserat_coupling.py:217, :220, :275-296, :378, :386`](../../src/ave/topological/k4_cosserat_coupling.py#L217). Add a top-of-class or top-of-module canonical statement: under the unified-Lagrangian framing, the K4↔Cosserat cross-sector coupling is carried by Op14 z_local impedance modulation (single channel). The legacy `_compute_coupling_force_on_cosserat` route (additive Cosserat force from `δL_c/δω` at every step) was double-counting and is disabled by default (`disable_cosserat_lc_force=True`). Similarly, Cosserat self-term `k_refl` carries the same redundant-force pattern and is suppressed (`k_refl=0.0`) when A28 is active. Prevents future agents from re-enabling the legacy path "for symmetry."
  - **Status:** queued
  - **Cross-refs:** E-007
### `mixing_derivation.py`
### `soliton_bond_solver.py`
### `tensors.py`
### `vacuum_engine.py`

- **[E-032] Single-source-of-truth methods `r_squared_K4()` / `r_squared_cosserat()` / `r_squared_total()` / `regime_at_each_site()` (v4 refactor item)**
  - **Sources:** [doc 57_ §3.3:L133-L173](../L3_electron_soliton/57_universal_lattice_units_v4_refactor.md#L133) (`224cad0`, 2026-04-23); [vacuum_engine.py:151-153](../../src/ave/topological/vacuum_engine.py#L151) (hardcoded constants); [vacuum_engine.py:370-388](../../src/ave/topological/vacuum_engine.py#L370) (RegimeClassifierObserver)
  - **Action:** add SOT methods on `VacuumEngine3D`. `r_squared_total()` returns Pythagorean dimensionless r² across active sectors (per AVE-APU Vol 1 Ch 5 strain theorem). All observers, regime classifications, impedance updates, and nucleation gates call this — none reinvent the sum. Replaces the three-observer divergent A²_total computations (R4 patched the immediate bugs in commit `6e355d1`; v4 prevents recurrence by removing the parallel-implementation surface). Enforces the per-call A_c specification pattern (no global `scale` parameter — see doc 57_ §1.5). Companion to E-031.
  - **Tests needed:** extend `test_normalization_subatomic_override.py` with: (i) `r_squared_K4()` matches `RegimeClassifierObserver` direct sum; (ii) `r_squared_cosserat()` matches existing `_cosserat_A_squared` helper; (iii) `r_squared_total()` matches Pythagorean sum within numerical tolerance; (iv) `regime_at_each_site()` matches the inline regime classification that observers currently do. Hard regression: all 23 existing `test_normalization_subatomic_override.py` tests must pass unchanged.
  - **Status:** queued
  - **Cross-refs:** E-031, C-002

- **[E-037] `PairNucleationGate` optional hysteresis (fire ≥ 0.95, heal ≤ 0.85)**
  - **Sources:** [doc 59_ §10.3:L600-L604](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md#L600) (`03cb9d5`, 2026-04-23)
  - **Action:** [`PairNucleationGate`](../../src/ave/topological/vacuum_engine.py#L1133) currently has instantaneous C1 threshold (A² ≥ 0.95). Memristive behavior (per doc 59_) suggests adding hysteresis: fire upward at A² ≥ 0.95, heal threshold at A² ≤ 0.85. Models that a once-saturated bond doesn't immediately un-saturate when driven below threshold (frozen topology, BEMF-blocked unwinding). ~20 LOC. Optional — cleaner physics, but `_nucleated_bonds` set already prevents re-fire so the practical effect is small. Defer until empirically motivated.
  - **Status:** queued
  - **Cross-refs:** E-006, E-036

- **[E-006] `PairNucleationGate._inject_pair` — upgrade injection profile from point-rotation Beltrami to topologically-protected ((2,3) torus-knot or Hopf fibration)**
  - **Sources:** [doc 70_ §7.3, §7.4, §7.6](../L3_electron_soliton/70_phase5_resume_methodology.md) (`e1f6eac`, 2026-04-25); [VACUUM_ENGINE_MANUAL §9 G-13](../L3_electron_soliton/VACUUM_ENGINE_MANUAL.md) (`0b45687`, 2026-04-25)
  - **Action:** the gate's current `_inject_pair` profile (single ω vector at A,B + Φ_link) is fundamentally unstable in Cosserat self-dynamics — it dissolves 93% in ONE Velocity-Verlet step regardless of drive presence. The G-13 contingency has been activated empirically. Replace the point-rotation Beltrami injection with a topologically-richer ansatz: (2,3) torus-knot OR Hopf fibration at each endpoint (chirality-matched: LH at A, RH at B). Reuse `cosserat_field_3d.py:initialize_electron_2_3_sector` (hedgehog seeder), `tlm_electron_soliton_eigenmode.py:initialize_quadrature_2_3_eigenmode` (V_inc/V_ref phase-coherent seed, see E-010), and `coupled_s11_eigenmode.py:_project_omega_to_saturation` (saturation pin, peak |ω|=0.3π).
  - **Tests needed:** update `test_phase5_pair_nucleation_gate.py` injection-profile tests (LH/RH sign, |ω|=√2 → topologically-protected envelope shape, ω̇=0, Φ magnitude+sign). Add new test asserting post-drive persistence ≥ 10 Compton periods (the empirical G-13 falsification threshold). Regression: existing 32-test suite must still pass with the new profile.
  - **Status:** queued
  - **Cross-refs:** E-008, E-010

- **[E-008] New driver script `phase5_topological_pair_injection.py` (Round 7 Stage 2) — APPLIED**
  - **Sources:** [doc 70_ §7.6](../L3_electron_soliton/70_phase5_resume_methodology.md) (`e1f6eac`, 2026-04-25); [doc 74_ §9.2 R7.2 result](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L342) (`d3adcc2`, 2026-04-26)
  - **Action:** [original action retained] ~200 LOC new driver at `src/scripts/vol_1_foundations/phase5_topological_pair_injection.py`. Tests whether topologically-richer ansatz (per E-006) survives Cosserat self-dynamics.
  - **Tests needed:** pre-reg `P_phase5_topological_injection` IS the integration test. Outcome registered.
  - **Status:** applied (`d3adcc2`). Result: **Mode III** — (2,3) torus-knot ansatz dissolves at the same Cosserat self-dynamics timescale as the Beltrami point-rotation profile per §9.2. Coupling-depth issue, NOT injection-profile issue (G-13 contingency falsified at deeper layer per A41).
  - **Cross-refs:** E-006 (original injection-profile-upgrade entry — NOT closed by E-008's null result; still pending Round 8 work); A-006, A-007 (A41)

- **[E-058] Cos-block N=64 dual-criterion driver — APPLIED at σ=1; σ=4 retarget SUBSUMED by L3 closure (A-014) — DEFERRED to Round 10+ Direction 1 (N=128 escalation)**

  **DEFERRED 2026-04-28** per A-014 L3 closure: σ=4 retarget no longer the load-bearing follow-up. The 10-test Mode III closure across V_inc/V_ref AND Φ_link sectors (path α v1/v2/v3) supersedes the σ=4 individual sub-test in importance; if R/r=φ² doesn't manifest in either sector at any sampler view, the σ=4 eigsolve question becomes secondary. Round 10+ Direction 1 (N=128+ continuum-limit escalation) is the canonical follow-up; if (α) continuum-limit-only branch is correct, σ=4 retarget at N=128 may show different behavior. Until then: original σ=1 result preserved as historical Mode III; σ=4 retarget queued behind Round 10+ Direction 1.
  - **Sources:** [doc 74_ §9.1](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L330) (`d3adcc2`, 2026-04-26); A-008 resolution; **doc 74 §15.3 PASS criteria revision** (`89ba147`, 2026-04-26)
  - **Action:** [original] driver at `src/scripts/vol_1_foundations/r7_cos_block_n64_topology.py`. Per A-008, re-run at σ = m_Cosserat² = 4. **PER MOVE 10 (E-066): the relaxed natural state is spherically symmetric (Y_{0,0}-dominant), NOT shell-shaped.** §14.4's PASS criteria assumed shell localization; that assumption is empirically falsified for the relaxed background. Revised PASS framing (from doc 74 §15.3): (i) freq |λ - 4| / 4 < α; (ii) c via Op10 = 3 — **but caveated by A-013 non-standard c=3 carrier**; (iii') shell_frac on a *fitted* shell IF the eigvec localizes (not assumed); (iv') per-cell A² at eigvec load-bearing sites — informational, expected near-vacuum (A²≈0) given Move 10's relaxed state.
  - **Tests needed:** revised pre-reg with A-013-aware topology criterion (Op10 c=3 + topology-type identification) before re-run.
  - **Status:** applied at σ=1 (`d3adcc2`); σ=4 re-run pending revised PASS criteria. **The σ=4 test now asks: does engine's K_cos Hessian admit eigenmode at λ=4 with c=3 winding against the relaxed (near-vacuum-locally) background?** Cleaner question than original saturated-background framing.
  - **Cross-refs:** E-053, E-054, E-061, E-066 (Move 10 — informs revised criteria), A-006, A-008 (Reconciliation B), A-009 (relaxed-state spherical attractor), A-010, A-013 (c=3 carrier interpretation)

- **[E-059] Cos-block N=64 c-via-Op10 driver `r7_cos_block_n64_c_eigvec.py` — APPLIED at σ=1; RE-RUN NEEDED at σ=4 per A-008 Reconciliation B**
  - **Sources:** [doc 74_ §10.1 Test A](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L420) (`39f656a`, 2026-04-26); A-008 resolution 2026-04-27
  - **Action:** driver re-runs Cos-block N=64 GT_corpus dual-criterion with corpus-canonical c via Op10 + shell-fraction topology.
  - **Tests needed:** pre-reg IS the integration test.
  - **Status:** applied at σ=1 (`39f656a`); result Mode III-both at WRONG TARGET. Per A-008 Reconciliation B, re-run at σ = 4 (m_Cosserat²). Original result preserved; A42 (corpus-canonical c via Op10) finding still valid as methodology lesson independent of σ choice. **Re-run instrumented per A-010** to report eigvec local-saturation distribution.
  - **Cross-refs:** E-058, E-061, A-007 (A42), A-008, A-010

- **[E-060] Round 8 Move 5 self-consistent orbit hunt driver `r8_self_consistent_orbit_hunt.py` — APPLIED (FIRST POSITIVE EMPIRICAL RESULT)**
  - **Sources:** [doc 74_ §11](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L501) (`c772211`, 2026-04-26)
  - **Action:** new driver at `src/scripts/vol_1_foundations/r8_self_consistent_orbit_hunt.py` — time-domain test at corpus GT (R=10, r=R/φ²=3.82), joint seed (Cosserat ω hedgehog at peak |ω|=0.3π + V_inc chiral-phasor at amp=0.14), no external drive, 200 Compton periods. Per pre-reg `P_phase6_self_consistent_orbit_hunt` frozen at `b11996d`.
  - **Tests needed:** pre-reg IS the integration test.
  - **Status:** applied (`c772211`). Result: **Mode III-orbit per pre-reg** (persistence 0.329 < 0.50 threshold; topology criterion failed mid-transient at c=0 t=10P/25P). **BUT empirical positive plateau:** corpus seed unwound over 50 Compton periods, then peak |ω| stabilized at **0.3044 to 4 decimals across 150 consecutive Compton periods (t ∈ [50P, 200P])**, c=3 preserved continuously, shell fraction migrated 0.787 → 0.136 (orbit moved AWAY from corpus shell). **First positive empirical signal in Round 7-8 arc: engine hosts self-stable (2,3) orbit at SUB-CORPUS parameters.** See A-006 + E-057 + E-062.
  - **Cross-refs:** E-061, E-062 (Move 6 follow-up), A-006, A-007 (A45/A46/A47)

- **[E-055] Round 8 V≠0 hybrid-bound-state research direction — SUPERSEDED by Move 5/6 sequence**
  - **Sources:** [doc 74_ §7.2 + §1 Mode III interpretation](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L276) (`b8d97d9`, 2026-04-26)
  - **Action:** [original action retained] investigate whether bound state is genuinely hybrid V≠0 ∧ ω≠0 requiring V≠0 seed (Round 8 architectural rework restored).
  - **Status:** superseded by Move 5/6 sequence. Per doc 74_ §11.5 + §11.7: "Move 6 is now the load-bearing Round 8 next test, ahead of Move 3" — the V≠0 hybrid eigsolve (was Move 3) is deferred until Move 6 maps the settled-orbit (R', r') so the eigsolve seed can use the engine's actual self-consistent geometry, not corpus (10, 3.82). Hybrid V≠0 ∧ ω≠0 framing remains valid; sequencing changed.
  - **Cross-refs:** E-060, E-062 (replacement sequencing), A-006

## src/ave/axioms/

### `isomorphism.py`
### `millennium.py`
### `navier_stokes.py`
### `open_problems.py`
### `saturation.py`
### `scale_invariant.py`
### `spectral_gap.py`
### `yang_mills.py`

## src/ave/solvers/

### `bond_energy_solver.py`
### `coupled_resonator.py`
### `eigenvalue_root_finder.py`
### `fdtd_lc_network.py`
### `fdtd_yee_lattice.py`
### `g_minus_2_lattice.py`
### `orbital_resonance.py`
### `radial_eigenvalue.py`

- **[E-091] `radial_eigenvalue.py` post-`0401388` drift — APPLIED 2026-04-30: FULL RESTORATION ARC COMPLETE, 14/14 elements at manuscript precision at HEAD via Q1+Q3+Q4+Q5+Q6 surgical commits**
  - **Sources:** [doc 100 §10.4-§10.5](../L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md#L332) (`7cf8243`, 2026-04-30, per-element drift trajectory across 11 commits); [doc 100 §10.9-§10.13](../L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md#L472) (`6856b28`, 2026-04-30, surgical-fix prescription via diff reads); [doc 100 §10.14-§10.17](../L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md) (`ac7b0f5`, 2026-04-30, Q2 empirical sweep + closure + adjudication state finalized)
  - **Action:** Three plumber-physics questions (Q1/Q2/Q3) bisected from 11 post-`0401388` commits. Q2 closed empirically; Q1 + Q3 remain pending Grant authorization for engine-code modification.
    - **Q1 — `_z_net` form (commit `7fa60b7` Change A) — PENDING Grant adjudication:** screening of outer electrons by inner shells. Old form (pre-`7fa60b7`): σ_n(r) = enclosed-charge fraction from |ψ|² CDF (continuum-limit Helmholtz solution of K4-LC network — Ax-1 + Ax-2 chain explicit in old docstring). New form (HEAD): step function at Bohr radius r_n = n²a₀/Z (Ax-3 claim but no operational chain in docstring). Empirical: old form reproduces `0401388` exactly; new form drifts 6/8 affected elements *away* from CODATA. **Action map: Q1=(i, Helmholtz revert) → revert `_z_net` change in `7fa60b7`; Q1=(ii, step-tuned) → tune discrete formula transition zone or alternate boundary.** Per A-021 caveat: before recommending Q1 revert, grep `git log -p` for prior corpus-author intent on `_z_net` to confirm which axiom-chain reading the corpus is committed to.
    - **Q2 — angular reactance — RESOLVED 2026-04-30 via `ac7b0f5`:** HEAD is mixed. `f23ec7b` had partially reverted `7fa60b7`, restoring ℓ(ℓ+1) at eigenvalue-determining sites (`_sir_mode_weighted_base:546` + `_direct_ODE_eigenvalue:1486`) but leaving ℓ² at integration-only sites (`_radial_ode:637` + `_abcd_section:715`). Test 1 (flip integration sites ℓ²→ℓ(ℓ+1)): zero IE change, sites not load-bearing. Test 2 (flip eigenvalue sites ℓ(ℓ+1)→ℓ²): Z=1-12 unchanged, Al +37.8%, Si +36.6% catastrophic. **f23ec7b commit comment (line 543-545) explicitly frames ℓ(ℓ+1) as AVE-native** via "3D Spherical Helmholtz Harmonic Eigenvalue mapping" of acoustic-LC-resonance volumes. Q2=ℓ(ℓ+1) at eigenvalue path stands at HEAD; no surgical commit needed for Q2. **Optional Commit C (Q2 hygiene)** would flip integration-only sites 637+715 ℓ²→ℓ(ℓ+1) for codebase consistency; zero IE effect, low priority.
    - **Q3 — full-shell TIR gate (commit `87b4114` Change C) — PENDING Grant adjudication:** new gate `(is_full_shell and gamma<0) → Y_loss = 0` (perfect mirror) fires for any element with a full inner shell, not just Z≥31 heavy elements. For Si: gamma = -0.5, Op3 |Γ|² = 0.25 (partial reflection per Op3) — perfect-mirror claim contradicts Op3 reflection physics at Period 3. **Action map: Q3=perfect → keep `87b4114` broadly, accept Period 3 drift; Q3=Z≥31-only → narrow gate to mirrored_away clause** (one-line change per §10.17 Commit B). Per A-021 caveat: before recommending Q3 narrowing, grep `git log -p` on `87b4114` for prior corpus-author intent on the gate scope to confirm if a full-shell→perfect-mirror axiom-chain reading exists in commit history that the substrate-physics-recommendation alone doesn't surface.
  - **Other commits in the 11-commit drift window classified per §10.6-§10.7:** `046a233` (Op10 promoted to global scope from inside SIR — load-bearing for Al/Si but axiom-clean per Rule 12, broadening direction is right); `3c4870c` (Correction D Hopf back-EMF — clean Ax-2 PHYSICS-IMPROVEMENT for paired electrons in p-block; manuscript O/F values can either pin to `0401388` or update to HEAD, small effect either way); remaining 7 commits are EXTENSION (Period 4+ targeted, e.g., `c70054d` Lanthanide Prelude, `b78f157` Period 4 parity shift, `fa3a58e` Period 4 stabilize) or NEUTRAL-REFACTOR with negligible Period 1-3 spillover.
  - **Surgical-fix prescription per §10.17:** **Commit A (Q1 revert)** — non-trivial code restoration; pre-`7fa60b7`'s `_z_net` used `_enclosed_charge_fraction_1s` + `_enclosed_charge_fraction_n2` helper functions which `7fa60b7` may have also removed; needs verification of which auxiliary functions to restore. Source state available at any pre-`7fa60b7` commit (e.g., `0401388` worktree). **Commit B (Q3 narrowing)** — one-line change; drop the `or (is_full_shell and gamma < 0)` clause from the mirror gate. **Optional Commit C (Q2 hygiene)** — flip 637+715 for codebase consistency; zero IE effect.
  - **Status:** **APPLIED 2026-04-30 — FULL RESTORATION ARC COMPLETE.** Surgical-fix arc expanded beyond original Q1/Q3 to include Q4 (Phase A½ restoration) and Q5 (Correction B restoration) at [`6783711`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/6783711), then Q6 (Op10 inline-co-resonant restoration) at [`01f4f90`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/01f4f90). Q1+Q3 surgical commits at [`4c5035d`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/4c5035d) per Grant 2026-04-30 authorization. **14 of 14 elements now at manuscript precision at HEAD.** A-021 grep precondition was honored at each step (per agent commit messages). Optional Commit C (Q2 hygiene flip at integration-only sites 637+715) — status unconfirmed; Grant did not explicitly authorize and agent did not flag landing it; cosmetic-only, zero IE impact. CI gate (E-093) at [`d4f097b`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/d4f097b) prevents future regression at ±0.5% tolerance.
  - **Cross-refs:** A-018 (closed — full surgical lane γ executed), A-019 (commit-SHA anchoring discipline — operationalized via `b41063e` SHA-anchoring manifest), A-021 (prior-corpus-author-intent grep — operationalized via `b41063e` PR template axiom-chain checkbox), A-022 (closed — E-093 CI gate landed), C-003 (RESOLVED via full restoration), E-090 (manuscript-side SHA-anchor footnote — unblocked under γ since table values reproduce at HEAD post-surgical-fix), E-093 (APPLIED — CI gate at ±0.5% tolerance gates post-surgical state)

### `resonator.py`
### `spice_netlist_compiler.py`
### `spice_transient.py`
### `topology_optimizer.py`
### `transmission_line.py`
### `spice_models/`

## src/ave/condensed/

### `bjt_mechanics.py`
### `gaas_doping.py`
### `germanium_doping.py`
### `silicon_crystal.py`
### `silicon_doping.py`

## src/ave/gravity/

### `galactic_mond_drag.py`
### `gw_detector.py`
### `gw_propagation.py`
### `hyperbolic_kinematics.py`
### `lense_thirring.py`
### `neutrino_msw.py`
### `orbital_lc_damping.py`
### `planetary_magnetosphere.py`
### `solar_impedance.py`
### `stellar_interior.py`

## src/ave/nuclear/

### `arsenic_atom.py`
### `boron_atom.py`
### `carbon_atom.py`
### `gallium_atom.py`
### `germanium_atom.py`
### `phosphorus_atom.py`
### `silicon_atom.py`
### `silicon_nucleus.py`

## src/ave/plasma/

### `cutoff.py`
### `superconductor.py`

## src/ave/regime_1_linear/

### `fluids_factory.py`
### `hexagonal_lattice.py`

## src/ave/regime_2_nonlinear/

### `seismic.py`
### `seismic_fdtd.py`

## src/ave/regime_3_saturated/

### `black_hole_core.py`
### `cavitation_collapse.py`
### `condensed_matter.py`
### `electrostatic_core.py`
### `galactic_rotation.py`
### `kolmogorov_cutoff.py`
### `orbital_impedance.py`

## src/ave/regime_4_rupture/

### `black_hole_jets.py`
### `caustic_solver.py`
### `rupture_solver.py`

## Engine-side data manifests

### `manuscript/predictions.yaml`

- **[E-052] Retract `P_phase6_eigensolver_multiseed`; register `P_phase6_helmholtz_eigenmode_sweep` (Helmholtz reframe)**
  - **Sources:** [doc 72_ §6:L218-L235](../L3_electron_soliton/72_vacuum_impedance_design_space.md#L218) (uncommitted, 2026-04-25)
  - **Action:** the frozen `P_phase6_eigensolver_multiseed` (E-050, doc 71_ §13) used "linearize coupled K4+Cosserat dynamics around each seed ansatz, build sparse generalized-eigenvalue Jacobian" — Hessian-of-W framing. Doc 72_ §1.1 + §6 reframes: build discretized Helmholtz operator `H(R, r) = ∇·(z(x; R, r)·∇·) + k²` with Op14-modulated impedance, eigsh at sigma=ω_Compton². Pred field changes per doc 72_ §6 (1)-(6): methodology field, seed treatment, PASS criteria (`(ω, Q, c_eigvec)` instead of shape correlation), three-mode resolution, lattice geometry retained, optional Layer 2. **Replace** `P_phase6_eigensolver_multiseed` in `manuscript/predictions.yaml` with `P_phase6_helmholtz_eigenmode_sweep`. Mark old entry RETRACTED with reference to commit (TBD when doc 72_ commits) and doc 72_ §6.
  - **Status:** queued
  - **Cross-refs:** E-050 (the now-retracted predecessor), E-051 (driver implementation), A-004 (methodology framework)

- **[E-050] Retract `P_basin_audit_GT_stationarity`; register `P_phase6_eigensolver_multiseed` (multi-seed R7.1 sparse eigensolver)**
  - **Sources:** [doc 71_ §13-§14](../L3_electron_soliton/71_multi_seed_eigenmode_sweep.md) (`c69e79c`, 2026-04-25); original pre-registration commit `1bc1652` (2026-04-25)
  - **Action:** doc 71_ was renamed + reframed. Original pre-registration `P_basin_audit_GT_stationarity` (commit `1bc1652`, 2026-04-25, basin-audit framing) is **retracted-superseded** because the basin-audit framing was a Rule 6/8/10 corpus-bypass violation. Replace in `manuscript/predictions.yaml` with `P_phase6_eigensolver_multiseed` per doc 71_ §13.4: multi-seed R7.1 sparse eigensolver sweep with three-mode falsification structure (Helmholtz / acoustic-cavity formulation per [doc 67_ §23.4](../L3_electron_soliton/67_lc_coupling_reciprocity_audit.md#L23) — corpus-canonical for bound-state finding, NOT gradient-descent on Cosserat W). Keep `P_basin_audit_GT_stationarity` entry in `predictions.yaml` as historical record marked `RETRACTED` with reference to commit `c69e79c` and doc 71_ self-supersession.
  - **Status:** queued
  - **Cross-refs:** E-011 (F17-K Phase 6 sparse eigensolver — this IS that work, now formally pre-registered)

- **[E-061] Register R7+R8 prediction outcomes (5 new pre-regs, all Mode III with one empirical positive caveat)**
  - **Sources:** [doc 74_ §9 + §10 + §11](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L322) (commits `1c89fa1`, `53c2ce9`, `b932a45`, `b11996d`, `c772211`)
  - **Action:** register or update outcome status in `manuscript/predictions.yaml` for:
    - `P_phase6_cos_block_n64_dual_criterion` (frozen `1c89fa1`) → outcome **Mode III** per E-058
    - `P_phase5_topological_injection` (frozen `1c89fa1`) → outcome **Mode III** per E-008 status update
    - `P_phase6_cos_block_n64_c_eigvec_recheck` (frozen `53c2ce9`) → outcome **Mode III-both** per E-059
    - `P_phase6_test_b_bond_phasor_v2` (frozen `b932a45`) → outcome **Mode III-spatial** per doc 74_ §10.3
    - `P_phase6_test_b_bond_phasor_v3` (frozen `7fea8f7`) → outcome **Mode III-spatial** at saturation regime per doc 74_ §10.3
    - `P_phase6_self_consistent_orbit_hunt` (frozen `b11996d`) → outcome **Mode III-orbit per pre-reg** + **empirical positive plateau** per E-060 (mixed-outcome — schema may need outcome-narrative field). See A-007 (A47) on pre-reg-vs-narrative discipline.
  - **Tests needed:** none beyond the integration tests already executed.
  - **Status:** queued — predictions need actual `predictions.yaml` outcome-field updates; per A-007 (A47), some outcomes are mixed (strict pre-reg verdict + nuanced narrative reading) which the current schema may not support cleanly. Coordinate with E-040 + E-028 batched `predictions.yaml` update.
  - **Cross-refs:** E-008, E-058, E-059, E-060, A-007

- **[E-072] Per-cell local clock rate observer — PARTIAL ADVANCEMENT via universal-operator catalog (E-082 APPLIED); per-cell observer code still queued**

  **Update 2026-04-28:** universal-operator catalog at `manuscript/ave-kb/common/operators.md` (E-082 APPLIED via `35cc818`) lands the methodology layer of E-072. The per-cell engine observer code (`compute_local_clock_rate(engine, cell)` returning `(omega_substrate, omega_local, S_local, n_local)`) is still queued. Per Round 10+ plan, this is **Phase 0.2 cleanup work** — Phase 0.1 (save/load API) APPLIED via E-081; Phase 0.2 catalog APPLIED via E-082; the per-cell observer becomes a Phase 1 instrumentation deliverable companion to Direction 3 multi-operator signature observer (~50-100 LOC). Reduce priority from "load-bearing for Move 9" to "Phase 1 instrumentation" — Move 9 itself superseded per E-065 status.
  - **Sources:** [doc 76 §4.2 + §6.2](../L3_electron_soliton/76_lattice_to_axiom3_bridge.md#L160) (`05f8ac3`, 2026-04-27); A-010 (saturation as local clock modulation)
  - **Action:** add per-cell observer reporting `(omega_substrate, omega_local(x), S_local(x), n_local(x), c_local(x))` exposing Ax 4 saturation kernel + local clock rate at each lattice cell. Implementation sketch in doc 76 §4.2: `compute_local_clock_rate(engine, cell)` returns dict with `S_local = sqrt(1 - A²_local)`, `n_local = 1/S_local`, `omega_local = omega_substrate · S_local`, `c_local = c_substrate · S_local`. Lands in `cosserat_field_3d.py` or `vacuum_engine.py` alongside existing energy-density observers.
  - **Tests needed:** new test in `test_strain_regime_energy_conservation.py` (E-069 family) — verify observer returns correct values for known A² distributions: uniform, saturated-core, gradient. Add to `test_engine_saturation_invariants.py` for regression.
  - **Status:** queued — Tier 2 cleanliness work. Makes future tests Ax-4-canonical: instead of "frequency at single node" (which conflates local clock with global frequency), reports `(omega_substrate, omega_local_at_each_cell)`. Distinguishes lattice-level Ax 4 effects from physics-level frequency. **Caveat:** doc 76 framed this in Scheme-B Ax 3 = Gravity language; under canonical Scheme A, this observer is the substrate-native realization of **Ax 4** (saturation), with gravity n(r) as a derived consequence at continuum scale. The observer code is unchanged; the documentation framing changes.
  - **Cross-refs:** A-010 (canonical methodology entry), A-008 (Reconciliation B + spin-½), E-069 (engine-invariant family — observer adds the per-cell local-clock axis)

- **[E-073] Cosserat T_kinetic saturation fix — V·S/T·1 asymmetry — CANCELED 2026-04-28 per doc 79 §8.3 Direction 4 + doc 75 line 140 verbatim**

  **CANCELED 2026-04-28** per closure synthesis v4.4 (commit `c2115ea`) + doc 79 §8.3 Direction 4. Original framing (T_kinetic saturation fix as load-bearing for Mode III adjudication) was the fifth A43 instance — a lane-symmetric implementer-side miscall pattern. Per doc 75 line 140 verbatim: *"the reason is NOT V·S, T·1 wave-speed drift."* Engine V·S/T·1 fix is empirically negligible at relevant amplitudes (Diag A Mode I) and is corpus-acknowledged-as-NOT-load-bearing for Mode III closure. Per doc 79 §8.3 Direction 4: *"~30-45 min implementation + ~10 min Diag A verification. Per doc 75 line 140 verbatim: NOT load-bearing for Mode III closure (already empirically verified across V_inc/V_ref + Φ_link/ω sectors in path α v1+v2). Queued as cleanliness, not critical."* Reduce from "Tier 2 cleanliness work" to "deprioritized housekeeping" — only revisit if Round 10+ Phase 4.1 reaches its slot in the plan.
  - **Sources:** [doc 75 §2 + §7](../L3_electron_soliton/75_cosserat_energy_conservation_violation.md#L21) (`1b48f4d`, 2026-04-27); pre-reg `P_ax5_cosserat_wave_speed_amplitude_dependence` frozen `36d6e0d`
  - **Action:** [`cosserat_field_3d.py:545-587`](../../src/ave/topological/cosserat_field_3d.py#L545) saturates V_potential (W·S) but [`cosserat_field_3d.py:1204-1209`](../../src/ave/topological/cosserat_field_3d.py#L1204) does NOT saturate T_kinetic (`rho`, `I_omega` are constants 1.0). Per doc 75 §1 Ax 3 / unitarity argument, this is an in-principle violation of energy conservation. Fix: `T = ½·(ρ·S)·|u̇|² + ½·(I_ω·S)·|ω̇|²` with corresponding velocity-Verlet integrator update for time-varying effective inertia. Reframed motivation per doc 76 §6.3: not just energy-conservation cleanliness; makes engine's c_eff actually equal Ax 4's `c_0·√S` prediction (currently engine under-saturates c by leaving T unmodulated).
  - **Tests needed:** Diag A re-run at supplementary high-amp (A ∈ [3, 5]) post-fix should show stronger amplitude dependence (Mode II per pre-reg ~ 5%+ drift at A=2). Energy-conservation test in E-069 family. Integrator stability re-validation against `test_cosserat_field_3d.py` Velocity-Verlet test suite.
  - **Status:** **queued, NOT urgent** per Diag A Mode I result (asymmetry empirically negligible at corpus operating amplitudes A ≤ 2; only ~3% drift at A = 5; integrator-cliff at A = 6 separate phenomenon). Engine cleanliness work; not blocking Round 8. If R7.1 / Move 5 / R7.2 reruns are eventually motivated by other physics findings, the engine fix becomes a precondition.
  - **Cross-refs:** A-008 (resolved); A54 in A-007 (pre-reg falsified analytical prediction); E-069 (energy-conservation family — companion); E-072 (local clock observer makes Ax 4 c_eff = c_0·√S explicit per cell)

- **[E-074] Photon-tail branch CLOSED Mode III at engine-representable corpus aspect (paths a + b near-identical) — SUBSUMED 2026-04-28 into A-014 L3 closure**

  **Update 2026-04-28:** subsumed into A-014 L3 closure (doc 79 v5.1 §6.3) as one of the 10 pre-reg tests. Original Mode III finding stands.
  - **Sources:** [doc 75 §10 + §11](../L3_electron_soliton/75_cosserat_energy_conservation_violation.md#L172) (`1b48f4d`, 2026-04-27); pre-regs `P_phase6_photon_tail_dual_seed` frozen `fb2e4f1` + `P_phase6_photon_tail_propagating_ic` frozen `bd15bb0`
  - **Action:** photon-tail framework tested at engine-representable scale (N=64, R=4, r=1.5, corpus aspect R/r=φ²). Two paths:
    - **Path (a) standing-wave dual-seed** (`r8_photon_tail_dual_seed.py`): both K4 V_inc + Cosserat ω seeded with corpus (2,3) IC. Result: **Mode III, 0/4** — C1 ellipse aspect 25.74 (target 2.618 ± 5%), C2 winding NaN (12/30 nodes finite), C3 LC reactance ρ = -0.463 (target -1 ± 0.2), C4 c via Op10 = 1 (target 3, with A57 sub-Nyquist caveat). Sector asymmetry surfaced: Cosserat ω 4.3% retention vs K4 V_inc 66%.
    - **Path (b) propagating IC** (`r8_photon_tail_propagating_ic.py`): identical seeder + ω̇ enforces loop-tangent rotation (ω̇_x = +Ω_loop·ω_y, ω̇_y = −Ω_loop·ω_x). Adjudication 3/3 load-bearing per A57 (C4 demoted to informational). Result: **Mode III, 0/3** — near-identical fingerprint to path (a); C1=25.74, C3 ρ=-0.463 match to 3 sig figs. c(t) flickered between 0/1/2/3 (transient c=3 every ~50P with decaying ω, then settles to c=0 by t=200P).
  - **Net:** dissolution is NOT IC-driven (paths a + b near-identical); it's structural at this scale. **A58 NEW:** path-(a)/path-(b) empirical equivalence at engine-representable corpus aspect — IC velocity-tuning ruled out as the route to corpus-electron formation at engine-representable scales.
  - **Tests needed:** pre-regs ARE the integration tests; both registered + executed.
  - **Status:** **applied, branch closed at this scale.** Open follow-ups: (a) N=128+ with larger (R, r) to escape Nyquist constraint on c=3 seed (~5 hr per run, expensive); (b) non-corpus aspect ratio with c=3 cleanly seedable (relax R/r=φ²); (c) reframed corpus prediction at integrated-loop scale per doc 76. **Doc 76's path-integrated framing is the cleanest open extension.**
  - **Cross-refs:** A-006, A-007 (A57 + A58), E-061 (predictions.yaml lifecycle), E-072 (local clock observer enables path-integrated framing)

- **[E-077] Round 9 entry driver `r9_canonical_phase_space_phasor.py` — APPLIED methodology-conditional Mode III**
  - **Sources:** [doc 78](../L3_electron_soliton/78_canonical_phase_space_phasor.md) (`f3886d1`, 2026-04-27); pre-reg `P_phase8_canonical_phase_space_phasor` frozen `a535090`
  - **Action:** doc 28 §5.1 single-bond (V_inc, V_ref) phasor test in canonical phase-space framing on Move 5 attractor. Dual-criterion R/r=φ² + chirality. Setup IDENTICAL to Move 5. 200 Compton periods.
  - **Status:** applied (`f3886d1`). Result: **Mode III nominal per dual-criterion** (C1 R/r=φ² ± 5% FAIL, C2 chirality ≥75% consensus FAIL). BUT persistence guard violated (Move 5 attractor at 33% of initial peak |ω| at end of recording window, below 40% threshold) AND chirality cross-product noise-dominated (std/|mean| = 600-1200×). **Methodology-conditional negative** — surfaced methodology gaps (A59) addressed in path α v1/v2/v3 redesign.
  - **Cross-refs:** A-014 (L3 closure includes this test); A-015 (chirality finding here was noise-dominated; path α v3 view (c) gave the clean 100% CCW signal); E-078/E-079/E-080 (path α v1/v2/v3 successors with methodology fixes)

- **[E-078] Round 9 path α v1 driver `r9_path_alpha_bond_pair_phasor.py` — APPLIED Mode III at unfixed engine**
  - **Sources:** [doc 79 v4 §7.1-§7.5](../L3_electron_soliton/79_l3_branch_closure_synthesis.md#L451) (`661d6ff`, 2026-04-28); pre-reg `P_phase9_path_alpha` frozen `9b4fdcb`
  - **Action:** bond-pair (V_inc/V_ref) phasor on Move 5 fresh attractor with four methodology fixes from r9: Hilbert-transform chirality, persistence guard, per-cluster adjudication, recording window [15, 50] P. Tests doc 28 §5.1 + doc 37 §1 bond-pair object class.
  - **Status:** applied (`661d6ff`). Result: **Mode III** at unfixed engine — methodology-clean negative. Doc 79 v4 lands provisional closure pending v2/v3 Φ_link sector tests. **A-016 caveat:** tested bond-cluster scale, NOT corpus-canonical bond-pair (per doc 83).
  - **Cross-refs:** A-014, A-015, A-016 (wrong object class per doc 83), E-077, E-079, E-080

- **[E-079] Round 9 path α v2 driver `r9_path_alpha_v2_phi_link_sector.py` — APPLIED Mode III in Φ_link sector → doc 75 line 140 prediction empirically falsified**
  - **Sources:** [doc 79 v5 §7.6](../L3_electron_soliton/79_l3_branch_closure_synthesis.md#L248) (`baadc33`, 2026-04-28); pre-reg `P_phase9_path_alpha_v2` frozen `8b80c85`
  - **Action:** (Φ_link, ω_axial) bond-pair phasor on Op14 trading channel — the unprobed inductive trading channel doc 75 line 140 named as the load-bearing alternative. Recording window [15, 200] P (multiple trading periods at 0.020 rad/unit ≈ 50 P each).
  - **Status:** applied (`baadc33`). Result: **Mode III** in Φ_link sector. **Doc 75 line 140 prediction empirically falsified.** Doc 79 v5 lands FINAL Mode III canonical (negative) closure across 9 pre-reg tests (v1+v2 jointly close the canonical empirical question). **A-016 caveat:** bond-cluster scale tested, not bond-pair.
  - **Cross-refs:** A-014, A-015, A-016, E-073 CANCELED downstream of this result, E-078, E-080

- **[E-080] Round 9 path α v3 driver `r9_path_alpha_v3_3d_aligned.py` — APPLIED Mode III + ONE STRUCTURAL PARTIAL POSITIVE (100% CCW chirality view (c))**
  - **Sources:** [doc 79 v5.1 §7.6.4 + §8.2](../L3_electron_soliton/79_l3_branch_closure_synthesis.md#L306) (`6d27e58`, 2026-04-28)
  - **Action:** 3D-aligned ω-vector test, 5 sampler views: (a) 3D ω-PCA, (b) Φ_link/ω_x, Φ_link/ω_y, Φ_link/ω_z per-axis, (c) (Φ_link, |ω|) magnitude pairing. Tests auditor (δ) interpretation that c=3 maps to 3 spatial Cosserat ω-axes.
  - **Status:** applied (`6d27e58`). Results: **Mode III canonical across all 5 views on R/r=φ²** + **(δ) 3D-axis-mapping branch CLOSED** (view (a) decisive: ω-orbit volumetric NOT planar; principal-axis ratios near-unity NOT golden). **NEW partial positive: view (c) (Φ_link, |ω|) magnitude pairing yields 100% CCW chirality across both clusters (8 of 8 bonds; baseline ~50/50 random)** — substrate K4 right-handed bipartite chirality empirically anchored. R/r is wrong in this view too (median 4.55-5.74), so partial signature isolates chirality (anchored) from R/r (open). **A-016 caveat:** bond-cluster scale.
  - **Cross-refs:** **A-015 canonical entry**, A-014, A-016, E-077-E-079

- **[E-081] Round 10+ Phase 0.1 — VacuumEngine3D save/load API + Move 5 cached-state driver — APPLIED**
  - **Sources:** [round_10_plan.md §0.1](../L3_electron_soliton/round_10_plan.md) (`d8ca5b9`, 2026-04-28); commit `999d2ac`
  - **Action:** `r10_save_move5_state.py` driver verified roundtrip + deterministic evolution preservation. Engine-side: VacuumEngine3D save/load API for serializing simulation state. Required for Move 5 cached-state reuse across Round 10+ Phase 1+ work (Move 5 takes ~5-10 min wall; subsequent path α reruns shouldn't need to re-evolve from t=0 each time).
  - **Tests needed:** roundtrip determinism test added per `999d2ac`; should land in `test_vacuum_engine.py` regression suite.
  - **Status:** applied (`999d2ac`).
  - **Cross-refs:** Round 10+ Phase 0 complete

- **[E-082] Round 10+ Phase 0.2 — Universal-operator catalog at `manuscript/ave-kb/common/operators.md` — APPLIED**
  - **Sources:** [round_10_plan.md §0.2](../L3_electron_soliton/round_10_plan.md) (`d8ca5b9`, 2026-04-28); commit `35cc818`
  - **Action:** light source-consolidation of universal-operator catalog at canonical manuscript-tree location. Documents the 22+ universal operators with explicit citations to engine code + corpus chapters. Direction 3.4/3.5 in-flight corrections per A43 v10/v11 catches landed in same commit.
  - **Tests needed:** none directly (documentation work). Companion to E-031/E-072 universal-operator + per-cell observer work — when those land they should cite this catalog.
  - **Status:** applied (`35cc818`). Doc 81 §2.2 Op20+Op22 misattribution flagged via Rule 12 footnote at `a0a2c7e` (synthesis-as-corpus catches per A43 v10/v11).
  - **Cross-refs:** E-031, E-072, E-076

- **[E-083] Round 10+ Phase 1 supplementary — path α v4 + v4b drivers — APPLIED with chirality-pairing-dynamic-asymmetry hypothesis EMPIRICALLY BURIED**
  - **Sources:** commits `2a684a4` (v4) + `d4b0495` (v4b)
  - **Action:** `r10_path_alpha_v4_port_mixed.py` (port-mixed test on cached Move 5 state) + `r10_path_alpha_v4b_n2_per_port.py` (n=2-per-port test). Tests chirality-pairing-dynamic-asymmetry hypothesis on cached Move 5 state.
  - **Tests needed:** pre-regs ARE the integration tests.
  - **Status:** applied. Results: v4 DECISIVE on chirality-pairing-breaks-C_3 falsification + open on LH-internal inconsistency + subsidiary chirality-port-0-dependence finding. v4b n=2-per-port — v4 RH-tight/LH-spread was n=1 sampling coincidence; **both pairs spread comparably at n=2 (Mode I-both-spread)**; chirality-pairing-dynamic-asymmetry hypothesis further empirically buried. **A-016 caveat:** bond-cluster scale (per doc 83 reframe).
  - **Cross-refs:** A-016 (wrong-object-class reframe motivated by these results), E-094 (bond-pair scale rerun is the active L3 next step closing A-016)

- **[E-094] Round 10+ Phase 1 — path α bond-pair-scale rerun — ACTIVE L3 NEXT STEP (lane (2) per Grant 2026-04-30 adjudication)**
  - **Sources:** [doc 83](../L3_electron_soliton/83_phase1_bond_pair_vs_bond_cluster_scale.md) (`9e8b1e2`, 2026-04-28, bond-pair-vs-bond-cluster reframe); [round_10_plan.md](../L3_electron_soliton/round_10_plan.md) (`d8ca5b9`, 2026-04-28, Round 10+ Phase 1 critical path); auditor agent dialogue 2026-04-30 (Lepton Mass Spectrum (1) deferred per A-017 framing-correction + extension-vs-closure bias toward closing A-016 first)
  - **Action:** Re-run path α at corpus-canonical **bond-PAIR scale** (NOT the bond-cluster scale that v1-v4(b) tested per A-016). Per doc 83 reframe, the bond-pair LC tank is the corpus electron's substrate-canonical site (Vol 4 Ch 1:175-184 Virial sum at saturation onset, structural per A-017). New driver candidate: `r10_path_alpha_v5_bond_pair.py` rerun of path α v3 (Φ_link, |ω|) magnitude pairing at bond-pair scale instead of bond-cluster. Per A-023 dual soliton+wake framing surfaced 2026-04-30, IC seeder must engage BOTH soliton (V_inc) AND lattice-wake (V_ref / Φ_link) sides — A47 v7 catch (corpus-canonical IC is `initialize_quadrature_2_3_eigenmode` with V_inc + V_ref at 90° quadrature, NOT V_inc-only `initialize_2_3_voltage_ansatz`). Pre-reg dual-criterion: (1) Φ_link sector engagement at bond-pair scale + (2) chirality pairing carries to bond-pair regime per A-015 100% CCW partial positive at bond-cluster.
  - **Predicted outcomes per agent's reframe:** if Mode I at bond-pair scale → A-014 closure conditional revises (bond-cluster Mode III + bond-pair Mode I would mean engine HOSTS the electron at the right scale, with 10-test corpus-GT closure being a wrong-scale negative). If Mode III at bond-pair scale → A-014 closure strengthens (electron-as-K4-eigenmode falsified at the corpus-canonical scale, not just at the wrong scale Round 9 tested). Either result sharpens whether Track B Phase 3 lepton-mass-spectrum work has substrate-level grounding to build on.
  - **A-021 precondition:** before kicking off the rerun driver, grep `git log -p src/scripts/vol_1_foundations/` for prior corpus-author intent on bond-pair scale IC seeders to confirm no existing infrastructure handles this case. If `initialize_quadrature_2_3_eigenmode` already exists and is bond-pair-scale-correct, use it; if not, scope new driver per A-021 caveat (don't silently override prior corpus-author choices).
  - **Status:** **APPLIED 2026-04-30 via [`34b7fe1`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/34b7fe1) — bond-pair Mode III at corpus-canonical scale + IC; A-016 caveat closure NEGATIVE.** Track A empirical record complete at three scales (single-bond from doc 28; bond-cluster from path α v1-v4(b); bond-pair from E-094). All three: Mode III. The "wrong scale + wrong side" gap from A-016+A-023 is now closed: the corpus-canonical IC seeder (V_inc + V_ref quadrature, addressing A47 v7) was used at corpus-canonical bond-pair scale, and the result is still Mode III decisive. **A-014 L3 closure stands at corpus-canonical configuration**, no longer asterisked by A-016. Round 13 (`4452539`) further reaffirmed: 8 cumulative Mode III tests across configurations × ICs.
  - **Cross-refs:** A-014 (REAFFIRMED — L3 closure stands at corpus-canonical scale + IC; previous bond-cluster-only asterisk now closed), A-015 (chirality partial positive does NOT carry to bond-pair scale; bond-cluster-only finding), A-016 (closed NEGATIVE — bond-pair Mode III), A-017 (rest energy structural at bond-pair LC tank — bond-pair scale tested per A-017 framing, Mode III result), A-021 (grep precondition honored), A-023 (reassessed — wake-side IC was used and Mode III result decisively falsifies "wake-side untested" implication of dual-view framing), A-024 (NEW — bracket-Golden-Torus reframe is the Grant adjudication consequence of E-094's negative outcome), E-083 (bond-cluster precursor — same Mode III result at adjacent scale), E-095 (lepton mass spectrum — A-016 closure NEGATIVE means substrate-eigenmode question for corpus electron is empirically closed; Track B Phase 3 lepton-ladder work now stands or falls on its own substrate-level grounding, not on Track A's substrate validation)

- **[E-095] Lepton mass spectrum prediction (Track B Phase 3 candidate) — DEFERRED pending A-016 closure via E-094**
  - **Sources:** auditor agent dialogue 2026-04-30 (Lepton Mass Spectrum (1) lean considered + flagged as wrong framing on m_e per A-017, extension-vs-closure bias toward (2) bond-pair instead); [round_10_plan.md](../L3_electron_soliton/round_10_plan.md) Phase 3 (topology + mass spectrum)
  - **Action (when unblocked):** Pre-register lepton mass ratio predictions: do m_μ / m_τ emerge from (2,q) torus-knot ladder ratios at <1% (analogous to baryon J=(c-4)/2 pattern with 7/8 PDG matches at c=15-19)? **Critical framing per A-017:** m_e is STRUCTURAL (boundary condition that defines LC tank saturation onset), NOT predicted. Pre-reg targets are m_μ/m_τ as ratio predictions, not m_e as standalone prediction. **A-021 precondition:** torus-knot ladder for leptons (electron at c=3 trefoil-class, muon and tau at higher (2,q)) is a DIFFERENT mass formula from baryon J=(c-4)/2 — verify whether shared Faddeev-Skyrme + BARYON_LADDER infrastructure extends, or whether lepton-specific framework is needed. The "same lane" categorization (Track B analytical eigenvalue solvers) does not imply "shared infrastructure"; ABCD cascade (atomic IE) and Faddeev-Skyrme + ladder (baryons) are related-lane-not-shared-infrastructure per agent self-correction 2026-04-30.
  - **Why deferred:** A-016 caveat from L3 closure means Mode III closure on K4-TLM electron-existence has explicit asterisk until bond-pair scale tested. E-094 outcome sharpens whether Phase 3 lepton-ladder work has substrate-level grounding to build on or not. Closing what's open before opening what's closed is the cleaner empirical posture.
  - **Status:** deferred (queued behind E-094)
  - **Cross-refs:** A-014, A-015, A-016, A-017, A-021, E-094 (gating), [round_10_plan.md](../L3_electron_soliton/round_10_plan.md) Phase 3

- **[E-084] Round 10+ research plan tracked at `research/L3_electron_soliton/round_10_plan.md` — APPLIED**
  - **Sources:** [round_10_plan.md](../L3_electron_soliton/round_10_plan.md) (`48ee43d` original; `d8ca5b9` auditor-refinements amendment)
  - **Action:** version-control the Round 10+ research arc plan in repo for auditor review. Six-direction comprehensive sequencing across 4 phases (~20-33 fresh sessions). Phase 0 (infrastructure) APPLIED; Phase 1 (highest info-per-cost) in flight; Phase 2-4 queued. Phase 1 reassessment gate per auditor refinements.
  - **Tests needed:** none directly (planning doc).
  - **Status:** applied (`d8ca5b9`); serves as forward research-arc index for L5 tracker downstream.
  - **Cross-refs:** All Round 10+ E-NN entries should reference this plan; Phase 1 reassessment gate is the formal mid-arc adjudication point.

- **[E-068] Round 8 Move 11 — reactance tracking — APPLIED with PML-cell methodology bug; HYBRID FINDING (V-static + Cosserat-non-conserving)**
  - **Sources:** Synthesizer/agent dialogue 2026-04-27 surfacing A-011; engine code at [`k4_tlm.py:384-391`](../../src/ave/core/k4_tlm.py#L384) (Φ_link accumulator); doc 74 §13 static-fixed-point verdict
  - **Action:** [original action retained] driver `r8_reactance_tracking.py` reads time-resolved K4 reactance pair (Φ_link, V_avg) + Cosserat reactance pair (|ω̇|, |ω|) + H(t) = T(t) + V(t) traces over t ∈ [150P, 200P] window of E-060 Move 5 simulation state.
  - **Tests needed:** pre-reg `P_phase6_reactance_tracking` IS the integration test.
  - **Status:** **applied (Move 11) + Move 11b (E-070) APPLIED — final reading: co-stable trading state, NOT LC-oscillating, NOT strict static.** Three findings + Move 11b resolution:
    1. **K4 V-sector confirmed near-static** — Σ|V_inc|² mean=24.92, std=9.4e-4 → variation < 0.004%. V_inc-near-constant reading holds for K4.
    2. **Cosserat H_cos drift 5.5% RESOLVED via Move 11b Pearson matrix**: ρ(H_cos, Σ|Φ_link|²) = -0.990. **Op14 cross-sector trading IS the mechanism** — Cosserat loses energy ⟺ K4-inductive (Φ_link) gains it. H_total = H_cos + H_K4-inductive ≈ conserved. The +0.366 ρ(T_cos, V_cos) reflects T+V both driven by external Φ_link forcing, NOT internal LC reactance. See A-012 (RESOLVED) and doc 75 §6.2.
    3. **PML-cell methodology bug** caught (top-5 |ω|² at PML boundary) → Move 11b re-ran with PML-region exclusion (E-070 APPLIED).
  - **Cross-refs:** A-009 (REVISED to co-stable-trading verdict per Move 11+11b), A-011 (RESOLVED), A-012 (RESOLVED — Op14 trading mechanism), E-060 (Move 5), E-065 (Move 9 — gated on σ=4 Cos-block re-run), E-066 (Move 10), E-069 (rationale partially weakened — 5.5% drift was real Op14 trading not numerical), E-070 (Move 11b — APPLIED)

- **[E-070] Round 8 Move 11b — reactance tracking with PML-region exclusion — APPLIED**
  - **Sources:** Move 11 PML-cell methodology bug; Move 11b execution per `r8_phase1_reactance_tracking_v2_results.json` (uncommitted in working tree); doc 75 §6.2 + doc 74 §15.5 reactance closure
  - **Action:** [original] re-run E-068 driver with cell selection filter `4 ≤ i,j,k ≤ 27` (interior of PML thickness=4 active region at N=32).
  - **Status:** **applied** (results json present in working tree). Pearson matrix produced: ρ(H_cos, Σ|Φ_link|²) = -0.990 (Op14 trading); ρ(Σ|V_inc|², Σ|Φ_link|²) = -0.990; ρ(H_cos, Σ|V_inc|²) = +1.000; ρ(T_cos, V_cos) = +0.366. **Resolves A-012** — Op14 cross-sector trading is the mechanism for the Cosserat H_cos drift. H_total ≈ conserved.
  - **Cross-refs:** E-068 (predecessor + Move 11), A-011 (RESOLVED), A-012 (RESOLVED — Op14 trading)

- **[E-066] Round 8 Move 10 — fixed-point spatial-winding characterization — APPLIED**
  - **Sources:** [doc 74 §15](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L846) (`89ba147`, 2026-04-26); pre-reg `P_phase1_attractor_winding_characterization` frozen at `d4fda36`; scipy 1.15+ `sph_harm` rename fix at `c9e38c4`
  - **Action:** [original] characterize static fixed point's spatial winding pattern. Four extractions: (1) torus winding (p, q) per shell; (2) Hopf linking proxy; (3) Y_{l,m} decomposition of |ω|²; (4) per-cell A² at top-50 |ω|² cells.
  - **Tests needed:** pre-reg IS the integration test.
  - **Status:** **applied (`89ba147`).** Result: relaxed attractor's c=3 carrier is **NOT torus knot** (extraction 1 zero (p,q)), **NOT Hopf-linked** (extraction 2 ≈ noise), **|ω|² spherically symmetric Y_{0,0}-dominant** (extraction 3), **sectors spatially decoupled** (extraction 4: V_inc ≈ 0 where ω is highest, A² ∈ [0.0, 0.015]). **The c=3 carrier is non-standard direction-field winding** — see A-013 NEW. Op10 reads c=3 from a configuration that's none of {torus, Hopf, multipole, two-twists}. §14.4's σ=4 PASS criteria need revision per §15.3 (relaxed state isn't shell-shaped; criteria framed for shell localization don't apply).
  - **Cross-refs:** E-064, E-065 (gated), A-009 (REVISED — Move 10 informs spherical-attractor reading), A-006, **A-013 (NEW — non-standard c=3 carrier)**, E-058/E-059 (PASS criteria need revision)

- **[E-065] Round 8 Move 9 — autoresonant CW drive at ω = 2 — SUPERSEDED by Round 9 path α arc + L3 closure (A-014)**

  **SUPERSEDED 2026-04-28** per A-014 L3 closure: path α v1/v2/v3 took the empirical place that Move 9 would have occupied (test corpus electron at corpus GT under different sampling regimes). Result: Mode III canonical across all sampler views. Move 9 autoresonant drive at ω=2 specifically would test whether sustained drive engages a (2,3) mode; given the bond-cluster tests all returned Mode III + the closure framework now reads chirality (not R/r) as the empirically-anchored signal, Move 9 in its original framing is no longer the canonical test. Queued behind Round 10+ Direction 1 (N=128 escalation) — if continuum-limit hypothesis holds, Move 9 at N=128 may matter.
  - **Sources:** [doc 74 §13.5](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L736) (`51463c2`, 2026-04-26); A-008 resolution 2026-04-27
  - **Action:** autoresonant CW drive at **ω_drive = m_Cosserat = 2** (medium's full-cover SO(3) twist mode per A-008 Reconciliation B), NOT ω_C = 1 (which is the spinor projection — driving it engages only the half-cover observable, not the underlying field). Corpus (2,3) seed. Run engine 200 Compton periods. **Falsification test for interpretation (A) vs (B) of A-009:** if a sustained standing-wave at ω = 2 emerges that maintains c=3 + spatial localization, that's the corpus electron sustained by drive at the medium's twist mode (B confirmed); spinor projection observable at ω_C = 1 emerges as expected. If engine relaxes back to static fixed point regardless of drive at ω = 2, strong evidence for interpretation (A) (engine doesn't host the corpus oscillating electron at any frequency).
  - **Tests needed:** pre-register `P_phase6_autoresonant_drive_at_medium_twist` (or similar) before driver run. **Per A-010, instrument to report local-saturation distribution at the seed's load-bearing sites** so we can disambiguate "no global mode" from "local saturation pattern frustrates global drive at correct ω."
  - **Status:** queued — **load-bearing.** A-008 dimensional-contingency now resolved (Reconciliation B canonical, drive at ω = 2). Sequencing: Move 10 (E-066, dimensionally + saturation-locally neutral) first → Cos-block re-run at σ=4 (E-058/E-059 retarget) → THEN Move 9 at ω=2.
  - **Cross-refs:** E-064, E-066, A-006, A-008 (now resolved — drive at ω = 2), A-009 (interpretation A vs B falsification), A-010 (local saturation diagnostic instrumentation)

- **[E-064] Round 8 Move 7+7b — `r8_phase1_attractor_characterization*.py` drivers — APPLIED (FFT-corrected per §13.2)**
  - **Sources:** [doc 74 §13](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L664) (`51463c2`, 2026-04-26); pre-regs `P_phase1_attractor_characterization` (frozen `39444d0`) + `P_phase1_attractor_characterization_v2_fft_fix` (frozen `dd63116`)
  - **Action:** Phase 1 characterization in two parts: Move 7 initial extraction (centroid-displaced FFT samples corrupted by zero-V_inc artifact at all 5 cells) + Move 7b corrected (top-5 |V_inc|² cells per A49 sampling fix). Five extractions: spatial moments, FFT at top-|V_inc|² cells, Q-factor from log-decay, (V_inc, V_ref) phasor, energy partition.
  - **Tests needed:** pre-regs ARE the integration tests; both registered + executed.
  - **Status:** applied (`48d7cc9` + `51463c2` §13 correction). Result: **branch (b)′ — STATIC (2,3)-topological fixed point**, NOT corpus oscillating electron. Initial FFT reading "lattice cutoff oscillation" was misread of spectral leakage from sub-percent residual ripple around near-DC signal (3 adjacent FFT bins at 4.43/4.41/4.39 are leakage signature, not clean tone). Per §13.2 dimensional-analysis check: 4.44 IS in same natural units as ω_C = 1 (lattice Nyquist π·√2 ≈ 4.44), but the FFT signal interpretation was wrong. Attractor properties: c=3 preserved, V_inc ≈ -V_ref ≈ ±0.264 frozen, |ω| ≈ 0.30 constant, 85:15 V:T potential-dominant, all three Cosserat sectors balanced (Σ|ω|² ≈ Σ|u|² ≈ Σ|V_inc|² ≈ 21-25). **17-cell extent** (3× corpus shell minor radius) — diffuse, NOT bond-scale. τ = 83.6 Compton periods is relaxation timescale toward fixed point, NOT oscillation period.
  - **Cross-refs:** E-060, E-063, E-065, E-066, A-006, A-007 (A49 sampling, A50 FFT-leakage caveat, A51 static-fixed-point physics-substantive), A-009

- **[E-063] Round 8 Move 6 result — Mode III-natural (delocalized at search-grid boundary, spectrum non-physical) → meta-methodology pivot to characterize attractor as itself**
  - **Sources:** [doc 74 §12](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L607) (`880165b`, 2026-04-26)
  - **Action:** Move 6 (E-062) executed; **Mode III-natural** verdict per pre-reg adjudication: shell_frac_opt < 0.4 + (R_opt, r_opt) at search-grid boundary indicating no well-defined shell + spectrum non-physical (zero-V_inc-cells artifact). Triggered meta-methodological pivot: stop asking "is corpus electron at config X?" and instead characterize Move 5 attractor as itself. Spawned Move 7 + 7b (E-064) + reframed Move 9/10 priorities (E-065/E-066).
  - **Tests needed:** pre-reg `P_phase6_natural_attractor_characterization` IS the integration test.
  - **Status:** applied (`880165b`). Outcome: Mode III-natural per pre-reg, but the spectrum-non-physical caveat motivated the Move 7+7b sampling-fix re-run (E-064).
  - **Cross-refs:** E-062 (predecessor pre-reg + driver), E-064 (Move 7+7b downstream), A-007 (A48 NEW: meta-methodology pivot lesson), A-009

- **[E-062] Round 8 Move 6 natural-attractor characterization — APPLIED (`880165b`); outcome Mode III-natural per pre-reg, triggered E-063 meta-pivot**
  - **Sources:** [doc 74_ §11.5 + §11.6 + §11.7](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L561) (`c772211`, 2026-04-26); pre-reg + driver frozen at `97178c6` (2026-04-26); result + meta-pivot at `880165b`
  - **Action:** [`r8_natural_attractor_characterization.py`](../../src/scripts/vol_1_foundations/r8_natural_attractor_characterization.py) (448 LOC, ~5 min wall) implements three integrated extractions on Move 5's settled (2,3) attractor:
    - **(a) Geometry (PRIMARY CRITERION):** re-run Move 5 deterministically; snapshot full ω + V_inc at t = {100, 150, 200} Compton periods; sweep candidate (R, r) ∈ [2, 14] × [0.5, 6] torus shells centered on lattice center; fit (R_opt, r_opt) maximizing shell-localized ω-energy fraction on t=200P snapshot; report R_opt/r_opt vs corpus φ² = 2.618.
    - **(b) Phasor (DIAGNOSTIC):** select 8 highest-|ω|² cells on relaxed shell; compute per-cell time-averaged V_inc magnitude across 3 snapshots → spatial envelope; R_spatial/r_spatial vs corpus φ². This is doc 28_ §5.1's actual test on the engine's natural attractor (NOT corpus seed).
    - **(c) Spectrum (DIAGNOSTIC):** FFT of peak |ω|(t) and peak |V_inc|(t) over t ∈ [100P, 200P]; confirm dominant frequency at ω_C = 1.0; look for (2,3)-signature 3:2 harmonic ratio.
  - **Adjudication (3-mode primary on geometry):**
    - **Mode I-natural** (CORPUS ASPECT-RATIO VINDICATED): shell_frac_opt ≥ 0.4 AND R_opt/r_opt = φ² ± 0.10 → corpus R/r=φ² claim empirically validated at non-corpus absolute scale; only R_anchor calibration was wrong. **Substantive Round 7+8 narrative inversion.**
    - **Mode II-natural** (corpus ratio FALSIFIED): shell_frac_opt ≥ 0.4 AND R_opt/r_opt ≠ φ² ± 0.10 → engine prefers different aspect ratio.
    - **Mode III-natural** (delocalized): shell_frac_opt < 0.4 → (2,3) topology stable but energy density doesn't shell-localize.
  - **Tests needed:** pre-reg `P_phase6_natural_attractor_characterization` IS the integration test.
  - **Status:** applied (`880165b`). **Outcome: Mode III-natural per pre-reg** — shell_frac_opt < 0.4; (R_opt, r_opt) at search-grid boundary indicating no well-defined shell; spectrum non-physical (zero-V_inc-cells artifact). Triggered Move 7+7b (E-063→E-064): meta-methodology pivot from "is corpus electron at config X?" to "characterize attractor as itself."
  - **Cross-refs:** E-055 (superseded), E-057 (Vol 1 Ch 8 reframe — adjudication-open shifts: corpus φ² ratio test now subsumed under E-064 static-fixed-point reading), E-060 (Move 5), E-061, E-063 (meta-pivot), E-064 (Phase 1 characterization downstream), A-006

- **[E-040] Register memristive-cycle predictions from doc 59_ §11**
  - **Sources:** [doc 59_ §11:L627-L671](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md#L627) (`03cb9d5`, 2026-04-23)
  - **Action:** add to `manuscript/predictions.yaml`:
    - `P_phase5_memristor_loop_area` — hysteresis loop area `A(ω) = ℓ_node²·m_e c²·f(ω·τ_relax)` per doc 59_ Eq. 6.3, peak at ω·τ ∈ [0.88, 0.92] for Δr ≈ 0.3·V_SNAP around r_0 ≈ 0.7
    - `P_phase5_yield_heal_residue` — down-crossing through V_yield leaves topologically non-trivial ω residues persisting ≥ N Compton periods (N ≥ 100 estimate) in post-heal solid regime
    - `P_phase5_cooling_rate_density` — defect density from cool-from-above scales LINEARLY with volumetric yield-crossing rate (NOT KZ power-law `τ_Q^{-ν/(νz+1)}`, since Ax4 is first-order, not second-order)
    - `P_phase5_chirality_horizon` — see doc 59_ §11
  - All four require E-036 (memristive Op14) to be testable empirically. Each entry needs `derivation_label`, `axioms_used`, `falsification_protocol` per the manifest schema.
  - **Status:** queued
  - **Cross-refs:** E-036

- **[E-028] Register BH-horizon predictions; retract `P_er_epr_chirality_correlation`**
  - **Sources:** [doc 61_ §11](../L3_electron_soliton/61_cosmic_bipartite_k4_bh_interface_proposal.md) (`740b1a3`, 2026-04-24); [doc 62_ §10.9 + §11](../L3_electron_soliton/62_ruptured_plasma_bh_entropy_derivation.md) (`2671a54`, 2026-04-23); [doc 63_ §6.2-§6.3](../L3_electron_soliton/63_info_loss_stance_reaudit.md#L142) (`740b1a3`, 2026-04-24); [doc 64_ Flag 64-A:L64](../L3_electron_soliton/64_first_law_derivation_attempt.md#L64) (`b74ac19`, 2026-04-24)
  - **Action:** update `manuscript/predictions.yaml`:
    - Add `P_interface_eigenmode_entropy` — the surface-vs-volume info-destruction discriminator (per Flag 63-A). Reframed in doc 62_ §10.9.
    - Add `P_hawking_polarization_asymmetry` — Hawking radiation handedness-asymmetry under A-B interface framing.
    - Add `P_horizon_radius_357` — AVE's r_sat = 7GM/c² = 3.5·r_s prediction (Flag 64-A).
    - **Mark `P_er_epr_chirality_correlation` as RETRACTED** (commit `740b1a3`, retracting source: doc 63_ §3.3 + §6.2). Keep entry as historical record per scientific archive discipline.
    - Each new entry needs `derivation_label`, `axioms_used`, and `falsification_protocol` per the manifest schema. Validator at `src/scripts/claim_graph_validator.py` will check structural consistency.
  - **Status:** queued
  - **Cross-refs:** E-022, E-023, E-024, E-026, C-001
### `src/scripts/vol_*/` driver scripts

- **[E-096] Round 13 Layer 3 K4 V_inc/V_ref test driver — APPLIED via `4452539` (Mode III decisive at lattice-resolved chair-ring with corpus-canonical (V_inc, V_ref) quadrature IC)**
  - **Sources:** [doc 104 §8](../L3_electron_soliton/104_round_13_layer_3_entry.md) (`4452539`, 2026-05-01, Round 13 (α) executed); [doc 104 §8.10](../L3_electron_soliton/104_round_13_layer_3_entry.md) (`35bf51a`, 2026-05-01, self-audit corrections per Grant: 🔴 promotion premature + Rule 9 v2 trigger over-stated + A47 v11b near-miss caught + Rule 14 substrate-walk done); driver `r10_v8_o1f_quadrature_eigenmode.py` (launched 2026-04-30, committed via `4452539`)
  - **Action:** Layer 3 K4 V_inc/V_ref test at lattice-resolved chair-ring (N=48³) using corpus-canonical `initialize_quadrature_2_3_eigenmode(R=8, r=4, amp=0.05, chir=1.0)` — V_inc + V_ref at 90° quadrature, A²_max(t=0) = 0.032, Cosserat ON but unsourced (pure K4 V_inc/V_ref test), 50 Compton periods at DT=1/√2.
  - **Empirical result:** Median peak ω = 0.0000 → DC-dominated quasi-static residual. Same failure mode as V_inc-only IC; canonical quadrature seeder did NOT differentiate. 4/5 cells DC-dominated; 1 cell at lattice Nyquist artifact ω=4.43. **Mode III decisive.** Independently corroborates E-094 bond-pair Mode III at adjacent test configuration.
  - **Self-audit per `35bf51a` (Grant 2026-05-01):** initial framing claimed "Rule 9 v2 trigger fires (8 cumulative Mode III tests)" was over-stated; the cumulative count framing was promotion-premature. A47 v11b near-miss caught (substitution-not-retraction tendency in framing the cumulative interpretation). Rule 14 substrate-walk performed.
  - **Status:** APPLIED. Substantively contributes to A-016 closed NEGATIVE + A-014 reaffirmation by independently confirming Mode III at corpus-canonical IC across an adjacent configuration. A43 v2 grep finding (doc 104 entry) further surfaced the corpus-canonical seeder was actually USED in 3 prior drivers (NOT unused per the original A47 v7 framing) — A47 v7 status flip pending COLLABORATION_NOTES amendment.
  - **Cross-refs:** A-014 (REAFFIRMED), A-016 (closed NEGATIVE), A-023 (wake-side IC tested — dual-view "wake-side untested" implication falsified), E-094 (sibling bond-pair test — same Mode III result at adjacent configuration); A47 v7 (status flip pending — corpus-canonical IC was USED, NOT unused; doc 104 A43 v2 grep finding); A47 v11b near-miss (caught in §8.10 self-audit, not landed as a new failure-mode catalog entry but worth flagging for next COLLABORATION_NOTES touch)

- **[E-051] R7.1 Helmholtz multi-seed eigensolver driver — SUPERSEDED by E-053**
  - **Sources:** [doc 72_ §3 + §5:L110-L214](../L3_electron_soliton/72_vacuum_impedance_design_space.md#L110) (`b0e0431`, 2026-04-25)
  - **Action:** [original action retained for audit trail] new script in `src/scripts/vol_1_foundations/` implementing the Helmholtz multi-seed eigensolver per doc 72_ §3 + §5.
  - **Status:** superseded (E-053). Per doc 73_ §1.2 §6.1 catastrophic-error carve-out: continuum graph-Laplacian approximation for V-block does not lift to discrete K4-TLM scatter+connect at finite N. Approximation error ~10% vs PASS tolerance ~0.5% → 14× outside noise floor. Methodology error invalidates any result. **First on-record §6.1 invocation.** A37 finding documents the lineage.
  - **Cross-refs:** E-053 (replacement), A-004 (revised methodology), A-005 (sectoral-operator-structure principle)

- **[E-053] R7.1 K4-TLM scatter+connect + Cosserat Hessian + Op14 cross-coupling driver — APPLIED (`c69e79c`)**
  - **Sources:** [doc 73_ §2-§5:L57-L346](../L3_electron_soliton/73_discrete_k4_tlm_lctank_operator.md#L57) (`ce5af9f`, 2026-04-25); [doc 74_ §1-§3 run result](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md) (`b8d97d9`, 2026-04-26)
  - **Action:** [`r7_k4tlm_scattering_lctank.py`](../../src/scripts/vol_1_foundations/r7_k4tlm_scattering_lctank.py) implements R4 frame: V-block via K4-TLM scatter+connect transmission eigenvalue problem (sparse complex non-Hermitian, dim 32768 at N=32, 262144 nonzeros, eigsh shift-invert at sigma=exp(i·ω_C·dt)); Cos-block via Cosserat (u, ω) LC-tank Hessian-of-W (sparse real-symmetric, dim 196608 at N=32, FD HVP on engine.cos.energy_gradient(), Lanczos SA-mode k=100); Op14 cross-coupling at the seed handles inter-sector channel. Two implementation bugs caught + fixed via empirical run per Rule 10: (i) `build_scattering_matrix(z_local)` returned z-invariant matrix; (ii) Cos-block SA-mode found rigid-body null space (k bumped 20→100, NULL_SKIP_THRESH=1e-6).
  - **Tests needed:** driver script (research-grade); pre-registration `P_phase6_k4tlm_scattering_lctank` is the integration test (E-054). Two `test_*` validators considered for the new helpers if any get promoted to `src/ave/` proper: scatter+connect transmission-matrix construction; Cos-block FD HVP correctness vs analytical Cosserat Hessian on a smooth ansatz.
  - **Status:** applied (driver + pred committed `c69e79c`; run executed and reported in doc 74_)
  - **Cross-refs:** E-051 (predecessor — superseded), E-054 (companion pred), E-055 (Round 8 follow-up), A-004, A-005

- **[E-052] `P_phase6_helmholtz_eigenmode_sweep` retraction — SUPERSEDED by E-054**
  - **Sources:** [doc 73_ §1.2 §6.1 carve-out](../L3_electron_soliton/73_discrete_k4_tlm_lctank_operator.md#L26) (`ce5af9f`, 2026-04-25)
  - **Action:** [original action retained for audit trail] register `P_phase6_helmholtz_eigenmode_sweep` replacing `P_phase6_eigensolver_multiseed`.
  - **Status:** superseded (E-054). Pred was registered in commit `675141e` and retracted in `ce5af9f` per the §6.1 catastrophic-error carve-out.
  - **Cross-refs:** E-054 (replacement)

- **[E-054] `P_phase6_k4tlm_scattering_lctank` registration — APPLIED (`c69e79c`); run yielded Mode III at all 4 seeds**
  - **Sources:** [doc 73_ §8 + doc 74_ §4 falsification adjudication](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L98) (`b8d97d9`, 2026-04-26)
  - **Action:** registered `P_phase6_k4tlm_scattering_lctank` in `manuscript/predictions.yaml` with V-block PASS criterion `phase rel_diff < α/√2 ≈ 0.516%` and Cos-block PASS criterion `√λ rel_diff < α·ω_C ≈ 0.731%`. Frozen seeds: GT_corpus, F17K_cos_endpoint, F17K_s11_endpoint, vacuum_control. Run result: **Mode III at all four seeds.** V-block comprehensive (closest mode 1.22% off, 2.4× outside tolerance). Cos-block bottom-100-coverage Mode III (84× outside tolerance for vacuum_control smallest non-null mode). Three within-doc-74 headline flips: Mode III → Mode I CANDIDATE at N=64 → Mode I FALSIFIED via topology check (shell fraction 1.13%, BULK not (2,3)). Doc 74_'s headline result is preserved as-flipped per rule 12; net Round 7 didn't close.
  - **Tests needed:** none (this IS a test entry — the prediction is the integration test for E-053). Mark prediction `Status: tested → falsified Mode III` once `manuscript/predictions.yaml` schema supports outcome fields, OR add an outcome row in a comment.
  - **Status:** applied (pred registered + run executed + outcome reported); however, **Round 8 RESTORED per doc 74_ §7.2** — architectural rework is the next layer of investigation, see E-055
  - **Cross-refs:** E-052 (superseded predecessor), E-053 (driver), E-055 (Round 8 hybrid-bound-state research direction), E-056 (methodology lesson)

- **[E-055] Round 8 V≠0 hybrid-bound-state research direction — flagged from doc 74_ §7.2**
  - **Sources:** [doc 74_ §7.2 + §1 Mode III interpretation](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L276) (`b8d97d9`, 2026-04-26)
  - **Action:** Mode III interpretation per pred: "(2,3) representation needs structural rework, OR bound state is genuinely hybrid (V≠0 ∧ ω≠0) requiring V≠0 seed (Round 8)." All four R7.1 seeds were V=0 at the seed configuration. Round 8 architectural rework restored: investigate whether the bound state is genuinely hybrid V≠0 ∧ ω≠0, requiring V≠0 seeded eigenmode finding. Likely involves: (i) initialization of (V_inc, V_ref) at A26-corrected amplitude alongside Cosserat (u, ω) hedgehog; (ii) Op14 cross-block becomes nonzero at V≠0 seed (per doc 73_ §4.4 deferred); (iii) operator construction needs full block-structured form including V↔ω cross-block.
  - **Tests needed:** TBD (pre-registration drafting follows methodology articulation, per the post-72_ pattern)
  - **Status:** queued (Round 8 work — fresh research)
  - **Cross-refs:** E-053, E-054, A-004, A-005

- **[E-056] Methodology lesson — "frequency-PASS alone is band-density-vulnerable at high N"**
  - **Sources:** [doc 74_ §7 + Methodological lesson:L255](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L255) (`b8d97d9`, 2026-04-26)
  - **Action:** future bound-state predicates and `predictions.yaml` PASS criteria for any (2,3) localized bound-state finding must include frequency + topology jointly (NOT frequency alone). Topology check at minimum: shell fraction (sum of |ψ|² in shell vs bulk) + c_eigvec (crossing count from `extract_crossing_count`). Doc 74_ §7 third-flip: N=64 V-block GT_corpus passed frequency PASS at gap 0.45% < α/√2 tolerance, then topology check FALSIFIED it as BULK mode (shell fraction 1.13%). Update terminology table (already done in this sweep) and propagate to any new pre-registration.
  - **Tests needed:** when next bound-state pred is registered, add topology-check field to PASS criteria. No standalone test work; methodology constraint applied at pred-drafting time.
  - **Status:** queued (methodology constraint applied to all subsequent bound-state predicates)
  - **Cross-refs:** E-054, E-055, A-004

- **[E-011] F17-K Phase 6 sparse eigensolver methodology (Round 7 Stage 1)**
  - **Sources:** [doc 68_ §12.4](../L3_electron_soliton/68_phase_quadrature_methodology.md) (`3f6d544`, 2026-04-25); [doc 70_ §1 A31, §6](../L3_electron_soliton/70_phase5_resume_methodology.md) (`e1f6eac`, 2026-04-25)
  - **Action:** ~300 LOC new helper. If E-007's coupled-S₁₁ relaxation hits limits at coupled-engine scale, the Helmholtz acoustic-cavity framing motivates a genuine eigenvalue-problem solver (`scipy.sparse.linalg.eigsh` / Lanczos / Arnoldi) at fixed cavity geometry. AVE-Core does NOT currently use sparse eigensolvers for the (2,3) electron — would be new methodology. Pre-register `P_phase6_eigensolver`. Defer to fresh Round 7 Stage 1 session.
  - **Status:** queued
  - **Cross-refs:** E-007

## Test suite

### `src/tests/`
*Test additions/updates that follow from engine changes are tracked under the changed file's entry, not separately, unless they're large enough to warrant their own entry.*

- **[E-093] Manuscript IE table CI gate — `verify_ionization_energy_table.py` + `make verify` hook + test-suite extension**
  - **Sources:** [doc 100 §9.1-§9.10](../L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md#L147) (`8a3dd82`, 2026-04-30, provenance bisection); [Makefile:49-70](../../Makefile#L49-L70) (current `make verify` script list); [test_radial_eigenvalue.py:19-53](../../src/tests/test_radial_eigenvalue.py#L19-L53) (current pytest coverage gap)
  - **Action:** Three-part fix to close the structural CI-gate blind spot that let the +11.6% Na / +11.9% Al / +8.3% Si drift survive across 11 commits undetected.
    - **(1) New verify script `src/scripts/vol_2_subatomic/verify_ionization_energy_table.py`:** runs `ionization_energy_e2k(Z)` for Z=1-14, diffs against the manuscript table values verbatim from [`manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md), exits non-zero if any element exceeds tolerance (Grant adjudicates target tolerance — recommend ±0.5% as the "machine precision modulo 4-sig-fig rounding" floor, since the table reproduces to ±0.008% at `0401388`). Pattern: parse the markdown table once, hold the published values as the assertion target, regenerate via solver, table-print + fail-loud on any over-tolerance row.
    - **(2) Wire into `make verify` ([Makefile:49-70](../../Makefile#L49-L70)):** add a new line e.g. `$(PYTHON) $(SCRIPT_DIR)/vol_2_subatomic/verify_ionization_energy_table.py` between the existing volume-1 / volume-4 verify entries. Ordering: after `derive_alpha_from_golden_torus.py` (Vol 1 Ch 8) since IE table validation depends on the same constants chain.
    - **(3) Extend [`test_radial_eigenvalue.py`](../../src/tests/test_radial_eigenvalue.py):** parameterize a single test over all Z=1-14 elements at ±2.8% tolerance (matching the manuscript's stated precision claim). Current state covers 4 of 14 elements at tolerances LOOSER than the manuscript claim (Z=1 ±0.07%, Z=2 ±5%, Z=6 ±5%, Z=32 ±8%) — extend to all elements quoted in the manuscript table at tolerance ≤ manuscript claim. Pattern: `@pytest.mark.parametrize("Z, expected_eV", MANUSCRIPT_IE_TABLE.items())` with assertion `abs(ie - expected_eV) / expected_eV < 0.028`.
  - **Coupling to E-091 surgical-fix outcome:** E-093 lands AFTER E-091's Q1+Q3 surgical commits (so the verify gate measures the post-fix state, not the current drift). If Grant picks lane (β) "pin manuscript to `0401388`," E-093 lands directly. If Grant picks (α) "re-run at HEAD + update manuscript table," E-090's table edit + E-093's verify gate land together. If (γ) "surgical forward-fix," E-091 lands first, then E-090 + E-093 close the loop.
  - **Generalization (post-A-022):** once E-093 establishes the pattern, sweep across all `manuscript/ave-kb/**/*-validation.md` files + `manuscript/predictions.yaml` numerical-claim tables — each should have a paired `verify_*.py` script + `make verify` hook + test-suite coverage at the claimed precision. Editorial process discipline candidate; precondition for landing any future numerical-claim manuscript edit. See E-092 for the manuscript-side editorial sweep companion.
  - **Status:** **APPLIED 2026-04-30 via [`d4f097b`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/d4f097b)** — IE manuscript-table CI gate at ±0.5% tolerance + cross-repo erosion-pattern audit landed. Gates the post-surgical-fix state (E-091 full restoration arc). γ lane chosen by Grant 2026-04-30; verify script regenerates table from `ionization_energy_e2k(Z)` and diffs against published manuscript values; fails non-zero on any element exceeding ±0.5%. Wired into `make verify`. Cross-repo erosion-pattern audit added the discipline-rule check that catches similar drift patterns elsewhere in the repo.
  - **Cross-refs:** A-019 (write-time SHA-anchor companion — operationalized via `b41063e`), A-022 (closed — discipline rule operationalized via E-093 implementation), C-003 (RESOLVED via E-091+E-093 combination), E-090 (manuscript-side SHA-anchor convention — companion editorial work), E-091 (APPLIED — surgical-fix state E-093 gates), E-092 (systemic manuscript-side editorial sweep — companion)
