---
description: Audit the physics engine, scripts, and tests for code quality and constants compliance
---

# Code Audit Workflow

Audit the entire physics engine (`src/ave/`), all simulation scripts (`src/scripts/`, `future_work/`, `periodic_table/simulations/`), and test suite (`tests/`) for code quality, constants compliance, and architectural integrity.

> **Before starting:** Read `LIVING_REFERENCE.md` and `src/ave/core/constants.py` in full.
> Then read `manuscript/backmatter/04_physics_engine_architecture.tex` for the three-tier architecture spec.

## Scope

### Engine (Tier 1–3)
```
src/ave/
  core/           constants.py, fdtd_3d.py, fdtd_3d_jax.py, grid.py, lbm_3d.py, node.py
  axioms/         saturation.py, scale_invariant.py, yang_mills.py, navier_stokes.py,
                  spectral_gap.py, open_problems.py, isomorphism.py
  gravity/        __init__.py, galactic_rotation.py, gw_detector.py, gw_propagation.py,
                  neutrino_msw.py, planetary_magnetosphere.py, solar_impedance.py,
                  stellar_interior.py
  topological/    borromean.py, combiner.py, cosserat.py, faddeev_skyrme.py, soliton_bond_solver.py, tensors.py
  solvers/        bond_energy_solver.py, fdtd_lc_network.py, fdtd_yee_lattice.py,
                  protein_bond_constants.py, transmission_line.py
  mechanics/      impedance.py
  plasma/         cutoff.py, superconductor.py
  fluids/         water.py
  geophysics/     seismic.py, seismic_fdtd.py
```

### Scripts (95+ files importing from `ave`)
All `.py` files in `src/scripts/` and its subdirectories (book_1 through book_7, future_work, mechanics, infrastructure, periodic_table, standard_model, spice_manual).

### Tests (34 test files)
All `test_*.py` files in `tests/`.

---

## Checks

### 1. Constants Compliance (Highest Priority)

For every `.py` file in `src/ave/` and `src/scripts/`:

- [ ] **No hardcoded physics constants.** Every constant must be imported from `ave.core.constants`. Search for these literal patterns which indicate hardcoded values:
  - `376.73` or `377` (Z₀)
  - `511` followed by `kV` or `e3` or `000` (V_SNAP)
  - `43650` or `43.65` not imported (V_YIELD)
  - `3.86e-13` or `3.8616` (L_NODE)
  - `1.89e9` (B_SNAP)
  - `0.1834` (P_C)
  - `7.297e-3` or `1/137` (α)
  - `9.109e-31` (M_E) — except in `constants.py` itself
  - `0.2222` or `2/9` defined locally instead of importing `SIN2_THETA_W`
  - `25.13` or `8*pi` defined locally instead of importing `KAPPA_FS_COLD`
  - Any literal `scipy.constants` usage that duplicates an `ave.core.constants` value

- [ ] **Import chain correctness.** Constants imports should be:
  ```python
  from ave.core.constants import V_SNAP, V_YIELD, Z_0, ...
  ```
  Not: `from ave.core.constants import *` (wildcard imports obscure dependencies)

### 1b. Boltzmann Distribution Anti-Pattern (Critical)

The AVE framework uses **Axiom 4 saturation** (`S(r) = √(1 - r²)`) instead of Boltzmann `exp(-E/kT)` for all thermal/statistical physics. Any Boltzmann distribution in the codebase is a first-principles violation. Search for:

- [ ] **`exp(-` patterns**: `np.exp(-`, `math.exp(-` in engine modules. Each occurrence must be audited:
  - ❌ `exp(-E_hb / (K_B * T))` — Boltzmann occupancy (violates Axiom 4)
  - ❌ `exp(-T / T_char)` — exponential decay of structural fraction
  - ✅ `exp(-sigma * d)` — PML attenuation (electromagnetic, not thermal)
  - ✅ `exp(-r / r_screen)` — Yukawa screening (Op4 derived)
- [ ] **Boltzmann vocabulary**: Search for `boltzmann`, `partition function`, `canonical ensemble`, `fermi-dirac`, `bose-einstein` in `.py` docstrings. If found in derivation code (not just comparison text), flag as anti-pattern.
- [ ] **`kT` energy comparison**: Any expression comparing `kT` directly to a barrier energy via exponential is suspect. The correct AVE approach is `r = A/A_yield`, `S(r) = √(1-r²)`.

### 2. Three-Tier Architecture Compliance — No Equation Duplication (Engine Only)

The fundamental rule: **Scale-invariant equations live in Tier 1 ONLY. They are never re-derived, re-implemented, or duplicated in any lower tier.** All physics flows *upward* to `scale_invariant.py` and `constants.py`.

#### 2a. Universal Operators (must exist ONLY in `axioms/scale_invariant.py`)

The following functions are the single source of truth. Search every file in `src/ave/` **outside** `axioms/scale_invariant.py` for any reimplementation:

- [ ] **Impedance**: `Z = sqrt(mu/epsilon)` — only `scale_invariant.impedance()` computes this. Flag any `np.sqrt(mu / eps)`, `(mu/eps)**0.5`, or equivalent in domain adapters or solvers.
- [ ] **Saturation kernel**: `S = sqrt(1 - (A/Ac)²)` — only `scale_invariant.saturation_factor()`. Flag any inline saturation computation.
- [ ] **Effective permittivity**: `ε_eff = ε₀ · S` — only `scale_invariant.epsilon_eff()`. Flag any module computing `EPSILON_0 * sqrt(1 - ...)` directly.
- [ ] **Effective permeability**: `μ_eff = μ₀ · S` — only `scale_invariant.mu_eff()`. Flag any module computing `MU_0 * sqrt(1 - ...)` directly.
- [ ] **Reflection coefficient**: `Γ = (Z₂-Z₁)/(Z₂+Z₁)` — only `scale_invariant.reflection_coefficient()`. Flag any inline reflection computation.
- [ ] **Transmission coefficient**: `T = 1 + Γ` — only `scale_invariant.transmission_coefficient()`.
- [ ] **Local wave speed**: `c_eff = c₀ · S^(1/2)` — only `scale_invariant.local_wave_speed()`.
- [ ] **Impedance at strain**: `Z_eff = Z₀ / S^(1/2)` — only `scale_invariant.impedance_at_strain()`.

#### 2b. Systematic Equation Duplication Scan

For every function in Tier 2 (`gravity/`, `plasma/`, `geophysics/`, `fluids/`, `topological/`, `mechanics/`) and Tier 3 (`solvers/`, `core/fdtd_*.py`):

- [ ] **Read each function body.** If it computes any ratio, square root, or algebraic combination of `MU_0`, `EPSILON_0`, `Z_0`, `C_0`, or field amplitudes that produces an impedance, saturation factor, reflection coefficient, or wave speed — it MUST delegate to the corresponding `scale_invariant` function.
- [ ] **No local helper functions** that wrap the same physics. If a domain module defines a local `_compute_impedance()` or `_saturation()` helper, that's a duplication — it should call the Tier 1 function.
- [ ] **Tier 2 modules provide constitutive parameters only.** Domain adapters should return `(epsilon_analog, mu_analog)` pairs or domain-specific profiles — then pass them to Tier 1 operators. They should never close the loop themselves.

#### 2c. Import Direction (DAG Check)

- [ ] **Constants → Scale-invariant → Domain adapters → Solvers.** No reverse imports.
- [ ] **Tier 3 (Solvers) consume Tiers 1+2 only.** Solvers should not import from `scipy.constants` or define their own physical constants.
- [ ] **No circular imports.** Verify the import DAG has no cycles.

### 3. API Documentation

For every public function in `src/ave/`:
- [ ] Has a docstring
- [ ] Docstring includes parameter descriptions
- [ ] Docstring includes axiom traceability (which axiom(s) the computation derives from)
- [ ] Return type is documented

### 4. Script Quality

For every script in `src/scripts/`:
- [ ] Has a module-level docstring explaining purpose
- [ ] Saves outputs to `assets/` or `src/scripts/*/assets/` — not to repo root
- [ ] No PYTHONPATH or `sys.path` hacks — use proper structure to ensure module accessibility
- [ ] Matplotlib/plotting scripts: figures have titles, axis labels, and save to files
- [ ] Any derived "magic number" in a script annotated with derivation or flagged for numerology appendix

### 5. Test Coverage

- [ ] Map engine modules to test files:

  | Engine Module | Expected Test File | Status |
  |--------------|-------------------|--------|
  | `core/constants.py` | (verified at import time) | — |
  | `core/fdtd_3d.py` | `test_ave_engine.py`, `test_fdtd_nonlinear.py` | Check |
  | `axioms/saturation.py` | `test_saturation.py` | Check |
  | `axioms/scale_invariant.py` | `test_scale_invariant.py` | Check |
  | `axioms/yang_mills.py` | `test_yang_mills.py` | Check |
  | `axioms/navier_stokes.py` | `test_navier_stokes.py` | Check |
  | `axioms/spectral_gap.py` | `test_spectral_gap.py` | Check |
  | `axioms/open_problems.py` | `test_open_problems.py` | Check |
  | `gravity/galactic_rotation.py` | `test_galactic_saturation.py` | Check |
  | `gravity/gw_detector.py` | `test_gw_detector.py` | Check |
  | `gravity/gw_propagation.py` | `test_gw_propagation.py` | Check |
  | `gravity/neutrino_msw.py` | `test_neutrino_msw.py` | Check |
  | `gravity/planetary_magnetosphere.py` | `test_planetary_magnetosphere.py` | Check |
  | `gravity/solar_impedance.py` | `test_solar_impedance.py` | Check |
  | `gravity/stellar_interior.py` | `test_stellar_interior.py` | Check |
  | `topological/borromean.py` | `test_borromean.py` | Check |
  | `topological/faddeev_skyrme.py` | `test_faddeev_skyrme.py` | Check |
  | `topological/cosserat.py` | `test_cosserat.py` | Check |
  | `plasma/superconductor.py` | `test_superconductor.py` | Check |
  | `geophysics/seismic.py` | `test_seismic_fdtd.py` | Check |
  | `fluids/water.py` | (check if exists) | Check |
  | `mechanics/impedance.py` | (check if exists) | Check |
  | `solvers/bond_energy_solver.py` | (check if exists) | Check |
  | `solvers/transmission_line.py` | `test_q_factor_s_params.py` | Check |
  | `solvers/protein_bond_constants.py` | `test_protein_bond_constants.py` | Check |

- [ ] Flag any engine module without a corresponding test
- [ ] Verify `make test` passes: `./.venv/bin/pytest src/ -q`
- [ ] Verify `make verify` passes (the 4 physics protocol scripts)

### 6. Stale / Dead Code

- [ ] No unused imports in engine modules
- [ ] No commented-out code blocks longer than 5 lines (should be removed or documented)
- [ ] No `TODO` / `FIXME` / `HACK` comments without associated issue tracking
- [ ] Scripts in `src/scripts/` that no longer import from the current engine API are flagged as potentially stale

### 7. Engine ↔ LaTeX Sync

- [ ] Every function/module name referenced in `manuscript/backmatter/04_physics_engine_architecture.tex` exists in the actual codebase
- [ ] Any engine module added, renamed, or deleted since the last audit is reflected in the LaTeX appendix
- [ ] Rule 9 from `LIVING_REFERENCE.md`: "Engine architecture changes must propagate to LaTeX"

### 8. LIVING_REFERENCE.md Sync

`LIVING_REFERENCE.md` is the canonical onboarding document for all AI assistants. It must stay in sync with the actual engine:

- [ ] **Prediction count**: The "Master Prediction Table" entry count matches the actual output of `src/scripts/vol_7_hardware/master_predictions.py`
- [ ] **Prediction values**: Δ% values in the table match the script output
- [ ] **Key constants table**: All values (V_SNAP, V_YIELD, B_SNAP, L_NODE) match `constants.py`
- [ ] **Repository structure**: The file tree shown matches the actual directory layout
- [ ] **Development phases**: Status markers (✅, 🔄) reflect current reality (e.g., test count, active work areas)
- [ ] **Module paths**: All paths in "Content Sources (map to existing repo)" resolve to real files
- [ ] **Critical distinctions**: All numbered items are still accurate
- [ ] **Rules for AI Assistants**: All rules (1–9) are still applicable and complete

## Output

Produce a structured report:
1. **HARDCODED** — Physics constant not imported from `constants.py`
2. **TIER-VIOLATION** — Domain adapter re-deriving universal operators / equation duplication
3. **UNDOCUMENTED** — Public function missing docstring/axiom trace
4. **UNTESTED** — Engine module without test coverage
5. **STALE** — Dead code, unused import, or broken reference
6. **MAGIC** — Unexplained numeric literal needing derivation or numerology docs
7. **SYNC** — Engine/LaTeX mismatch
8. **LIVING-REF-DRIFT** — LIVING_REFERENCE.md out of sync with actual engine/repo

For each finding, cite the specific file, line number, and recommended fix.

Categories:
1. **HARDCODED** — Physics constant not imported from `constants.py`
2. **TIER-VIOLATION** — Domain adapter re-deriving universal operators / equation duplication
3. **UNDOCUMENTED** — Public function missing docstring/axiom trace
4. **UNTESTED** — Engine module without test coverage
5. **STALE** — Dead code, unused import, or broken reference
6. **MAGIC** — Unexplained numeric literal needing derivation or numerology docs
7. **SYNC** — Engine/LaTeX mismatch
8. **LIVING-REF-DRIFT** — LIVING_REFERENCE.md out of sync with actual engine/repo
9. **BOLTZMANN** — Scalar Boltzmann distribution `exp(-E/kT)` used instead of Axiom 4 saturation

### Verify Script Integration

For every **HARDCODED** or **TIER-VIOLATION** finding that gets fixed:

- [ ] **Add a corresponding check to the `make verify` pipeline** (e.g., `src/scripts/vol_1_foundations/verify_universe.py` or a new `verify_architecture.py`).
- [ ] The check should **grep or import-test** for the specific violation pattern so that regressions are caught automatically on every `make verify` run.
- [ ] Examples of verify checks:
  - `grep -rn "3.86e-13" src/` → should return 0 matches outside `constants.py`
  - `grep -rn "scipy.constants" src/ave/` → should return 0 matches
  - Import every engine module and assert no circular imports
  - Assert `scale_invariant.impedance` is the only function in `src/ave/` computing `sqrt(mu/eps)`
