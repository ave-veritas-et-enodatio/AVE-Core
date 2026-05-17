# AVE Agent Guide

What an AI coding agent must know before modifying this codebase.

---

## 1. The Zero Free Parameters Constraint

**This is the single most important rule.**

The model claims to derive ALL physical constants from three calibration inputs
(M_E, ALPHA, G) plus SI definitions (C_0, HBAR, e_charge, MU_0, EPSILON_0).
Introduction of any Standard Model constant — either hard-coded or via external
import — that is not derived from these inputs is a **framework violation**.

Before adding any numeric literal or constant import, ask:
- Is this derivable from M_E, ALPHA, G, and SI electromagnetic definitions?
- If yes: derive it. If no: it must be flagged as a boundary condition or
  validation target, never used as a computation input.

Constants labeled as "CODATA 2018" or "empirical" in existing code may be
intentional validation targets, or may be violations. Check whether the value
flows into any computation or is used only for comparison/reporting.

## 2. Import-Time Computation

`constants.py` runs scipy optimization at import time (lines 452-465, 518-537).
This means:

- **`import ave.core.constants` triggers numerical computation.** First import
  takes measurable time (seconds). This is not a bug — it is the baryon mass
  derivation running.
- The import chain `constants.py -> faddeev_skyrme.py -> universal_operators.py
  -> constants.py` is circular. It works because EPS_NUMERICAL/EPS_CLIP/EPS_DIVZERO
  are defined before the deferred import, and the import is inside a function body.
- **Do not move** the EPS_* definitions below line 458. Do not move the
  `_compute_i_scalar_dynamic` function or its call above the EPS_* definitions.
  Doing so will break the circular import resolution.
- Adding new imports from `constants.py` in files that `constants.py` imports
  (currently: `faddeev_skyrme.py`, `universal_operators.py`) risks import deadlock.

## 3. NU_VAC = 2/7 Is Central

The vacuum Poisson ratio `NU_VAC = 2/7` (defined at `constants.py:249`) is
the most-connected single constant in the framework. It appears in or flows into:

- Weak mixing angle: sin^2(theta_W) = 2/9
- CKM matrix: Wolfenstein lambda = 2/9, A = sqrt(7/9)
- PMNS matrix: sin^2(theta_12) = 2/7 + 1/45
- Strong coupling: alpha_s = alpha^(3/7)
- W/Z boson masses (via cosserat.py)
- Lepton mass spectrum (via cosserat.py)
- Nuclear eigenvalue distance: D_NN = pi * D_PROTON * 7/9
- Isotropic projection: 1/7
- Equilibrium packing: ETA_EQ = P_C * 5/7
- Galactic rotation: saturation acceleration
- Orbital resonance: QNM eigenvalue

Modifying NU_VAC or its downstream constants will cascade through essentially
the entire framework.

## 4. Operator Reuse Rule

`universal_operators.py` defines 15 operators that encode the four axioms.
The intended architecture is that ALL physics in downstream modules flows
through these operators. Local reimplementation of impedance, saturation, or
reflection logic is an architectural violation.

In practice, `scale_invariant.py` in the axioms package also defines versions
of impedance, saturation, and reflection that are used by many modules.
When modifying operator logic, check both files.

**A-034 framework state (canonical 2026-05-15 evening):** Op2 (universal
saturation kernel, `universal_operators.py:saturation_factor`) is the
**single S(A) = √(1-A²) function** that the engine evaluates across 19
distinct cross-scale phenomena (atomic dielectric breakdown → BCS
superconductivity at 0.00% error → NOAA solar flares → BH ring-down
at 1.7% from GR → cosmic K4 crystallization). This is the operator-level
universality claim — when adding new physics, do NOT introduce a per-scale
saturation function; reuse Op2. The 19-instance catalog is at
`manuscript/backmatter/07_universal_saturation_kernel.tex`; canonical
synthesis at `manuscript/ave-kb/common/trampoline-framework.md` §7.5;
L5 authority at `research/_archive/L5/axiom_derivation_status.md` A-034.

## 5. Regime Classification

Every physical phenomenon maps to one of four regimes based on the local
strain ratio r:

| Regime | Strain   | Phase Boundaries (JAX) | Application Domain |
|--------|----------|------------------------|--------------------|
| 1      | r << 1   | r < R_I_JAX            | Molecular, fluid   |
| 2      | r ~ O(1) | R_I < r < R_II         | Protein, seismic   |
| 3      | r -> 1   | R_II < r < R_III       | Nuclear, atomic    |
| 4      | r >= 1   | r >= R_III             | Black holes, sparks|

R_I_JAX = sqrt(2*alpha), R_II_JAX = sqrt(3)/2, R_III_JAX = 1.0.

Modules are organized by regime. A solver placed in the wrong regime directory
implies incorrect strain assumptions.

## 6. Dual Backend Pattern

NumPy is always available. JAX is used for GPU paths. The current detection
pattern (9 occurrences in `universal_operators.py`) is:

```python
is_jax = hasattr(x, 'device_buffer') or 'jax' in str(type(x))
```

This is fragile — JAX array types have changed across versions (`device_buffer`
was removed in JAX 0.4+). When writing new operators, prefer
`isinstance(x, jnp.ndarray)` with a try/except fallback, or use the existing
pattern for consistency while noting it needs refactoring.

## 7. File Dependency Map

Critical dependency ordering (imports flow downward):

```
constants.py
├── universal_operators.py (imports EPS_*)
├── faddeev_skyrme.py (imported at line 458, deferred)
│   └── universal_operators.py
├── scale_invariant.py (imports constants)
│   └── constants.py
├── coupled_resonator.py
│   ├── constants.py
│   └── scale_invariant.py
├── radial_eigenvalue.py
│   ├── constants.py
│   ├── coupled_resonator.py
│   └── transmission_line.py
└── All regime_*/gravity/plasma modules
    ├── constants.py
    └── scale_invariant.py or universal_operators.py
```

**Safe to modify independently**: Files in regime_1 through regime_4, gravity/,
plasma/ generally only import from core/ and axioms/ and do not export to them.

**Dangerous to modify**: constants.py, universal_operators.py, faddeev_skyrme.py,
scale_invariant.py — these form the foundation and are imported by everything.

## 8. Missing Infrastructure

- No `__init__.py` in `topological/` or `solvers/`. These packages rely on
  direct file imports (e.g., `from ave.topological.cosserat import ...`).
  Adding `__init__.py` files would not break anything but would enable
  package-level imports.
- No `requirements.txt`, `pyproject.toml`, or `setup.py`.
- No test files anywhere in the repository.
- No Makefile or build system.
- No logging infrastructure — all diagnostic output uses print or is absent.

## 9. Naming Conventions

- SI constants: ALL_CAPS (C_0, MU_0, EPSILON_0, HBAR)
- Native lattice units: N_ prefix (N_ALPHA, N_NU, N_A0, N_RY)
- Derived constants: ALL_CAPS descriptive (SIN2_THETA_W, PROTON_ELECTRON_RATIO)
- Private computation: _ prefix (_compute_baryon_ladder, _KG_TO_MEV)
- Operators: universal_ prefix in universal_operators.py, bare names in
  scale_invariant.py (impedance, saturation, reflection_coefficient)
- Empirical data catalogs: ALL_CAPS dicts or lists (GALAXY_CATALOG, LIGO_EVENTS,
  PREM_LAYERS, NUCLEAR_MASSES)

## 10. Validation Approach

The codebase uses comparison against known experimental values to validate
derivations. These appear as:
- Comments with PDG/CODATA/NuFIT values and percentage errors
- Assertion-style cross-checks (e.g., D_PROTON ~ 0.8412 fm)
- Galaxy/LIGO/PREM catalogs for astrophysical validation

When modifying a derivation, verify that the output value and its percentage
error against the documented experimental target have not regressed.

## 11. Files by Modification Risk

**Extreme risk** (cascading impact, circular imports):
- `src/ave/core/constants.py`

**High risk** (imported by many modules):
- `src/ave/core/universal_operators.py`
- `src/ave/axioms/scale_invariant.py`
- `src/ave/topological/faddeev_skyrme.py`

**Medium risk** (significant solver logic):
- `src/ave/solvers/coupled_resonator.py`
- `src/ave/solvers/radial_eigenvalue.py`
- `src/ave/solvers/transmission_line.py`

**Low risk** (leaf modules, regime-specific):
- Everything in regime_1/ through regime_4/
- Everything in gravity/, plasma/
- `src/ave/topological/borromean.py`, `combiner.py`, `entanglement_thread.py`
- `src/ave/solvers/fdtd_yee_lattice.py`, `resonator.py`
