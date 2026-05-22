# AVE Architecture Review — Findings

Review of all 60 Python files in `src/ave/`. Every file, import, and numeric
literal has been examined. Findings are organized by severity.

---

## Critical Issues

### C1. Zero Free Parameters Violations — Hard-Coded Empirical Constants

The framework claims three calibration inputs (M_E, ALPHA, G). The following
constants are hard-coded with no derivation chain, violating this claim.
Each entry lists file, line, constant, and whether it flows into computation
(INPUT) or is used only for comparison/display (TARGET).

**`src/ave/core/constants.py`**:
- Line 34: `R_I_JAX = jnp.sqrt(2.0 * 7.2973525693e-3)` — ALPHA as raw float
  literal in JAX pre-computation. Should reference ALPHA.
  Classification: INPUT. Severity: violation of single-source-of-truth.
- Line 51: `K_B = 1.380649e-23` — Boltzmann constant. Not derived. Used as
  computation input throughout (decoherence probability, melting temperature,
  thermal softening). Classification: INPUT.
- Line 52: `N_A = 6.02214076e23` — Avogadro constant. Not derived. Not used
  anywhere in the codebase as of current state. Classification: UNUSED.
- Line 53: `M_PROTON = 1.67262192369e-27` — Proton mass in kg. Not derived.
  Appears unused (the derived PROTON_ELECTRON_RATIO * M_E is used instead).
  Classification: POTENTIALLY UNUSED but its presence invites accidental use.
- Line 54: `M_SUN = 1.989e30` — Solar mass. Not derived. Used in
  gravity modules. Classification: INPUT.
- Lines 601-602: `M_P_MEV_TARGET = 938.272088`, `M_N_MEV_TARGET = 939.565420` — Proton
  and neutron masses in MeV. Labeled as "CODATA 2018 empirical — used as
  binding energy targets." However, M_P_MEV_TARGET flows into D_PROTON computation
  (line 611) which feeds into D_NN_EIGENVALUE, B_DEUTERON_PREDICTED, and
  all nuclear constants. Classification: **INPUT masquerading as TARGET.**
  This is the single most damaging violation — the entire nuclear sector
  depends on an empirical proton mass while the proton mass derivation
  (PROTON_ELECTRON_RATIO) exists in the same file but is not used for
  D_PROTON.

**`src/ave/gravity/neutrino_msw.py`**:
- Line 47: `G_FERMI = 1.1663788e-5` — Fermi constant in GeV^-2. Hard-coded
  empirical value. `constants.py` already derives G_F at line 277 from
  ALPHA and M_W_MEV. This is a redundant, non-derived copy.
  Classification: INPUT (used in MSW resonance calculations).
- Lines 52-53: `DELTA_M21_SQ = 7.53e-5`, `DELTA_M32_SQ = 2.453e-3` —
  Neutrino mass-squared splittings. Hard-coded PDG values. No derivation
  exists anywhere in the codebase.
  Classification: INPUT (used in MSW energy calculations).
- Line 63: `HBAR_EV_S = 6.582119569e-16` — Duplicate of HBAR in different
  units, hard-coded instead of derived from HBAR/e_charge.
  Classification: INPUT (dimensional duplicate).

**`src/ave/axioms/open_problems.py`**:
- Lines 270-271: `H0_PLANCK = 67.4`, `H0_SHOES = 73.04` — Hubble constant
  measurements. Used as computation inputs for impedance correction.
  H_INFINITY is derived in constants.py but these empirical values are
  used alongside it. Classification: INPUT.
- Line 275: `MPC = 3.0857e22` — Megaparsec in meters. Unit conversion,
  not a physics constant, but not derived.
  Classification: INPUT (unit conversion).

**`src/ave/axioms/navier_stokes.py`**:
- Line 253: `nu_water = 1.004e-6` — Kinematic viscosity of water. Empirical.
  Classification: INPUT (used in Lipschitz bound calculation).

**`src/ave/regime_3_saturated/galactic_rotation.py`**:
- Line 215: `KPC = 3.0857e19` — Kiloparsec in meters. Unit conversion.
  Classification: INPUT (unit conversion).

**`src/ave/regime_1_linear/fluids_factory.py`**:
- Lines 122-123: `m_center = 15.999 * 1.66054e-27`, `m_ligand = 1.008 * 1.66054e-27`
  — Oxygen and hydrogen nuclear masses with hard-coded AMU. The AMU value
  (1.66054e-27) is hard-coded with no derivation. The atomic weights (15.999,
  1.008) are integer-adjacent values that could in principle be derived from
  the nuclear binding engine but are not.
  Classification: INPUT.

**`src/ave/regime_3_saturated/condensed_matter.py`**:
- Line 59: `_M_U = 1.66053906660e-27` — Atomic mass unit. Hard-coded.
  Duplicate of the AMU in fluids_factory.py and bond_energy_solver.py.
  Classification: INPUT.

**`src/ave/solvers/bond_energy_solver.py`**:
- Line 298: `_DA = 1.66053906660e-27` — Dalton. Same value as _M_U above.
  Third independent copy.
  Classification: INPUT.
- Lines 300-306: `NUCLEAR_MASSES = {'H': 1.00794*_DA, 'C': 12.0107*_DA, ...}`
  — Empirical atomic weights for H, C, N, O, S. No derivation.
  Classification: INPUT (used in bond energy calculations).

**`src/ave/topological/soliton_bond_solver.py`**:
- Line 32: `z_eff = {1: 1.00, 6: 3.25, 7: 3.90, 8: 4.55, 16: 5.45}` —
  Slater effective nuclear charges. Empirical screening constants.
  Classification: INPUT (used in orbital radius calculation).
- Line 50: `chi = {1: 2.20, 6: 2.55, 7: 3.04, 8: 3.44, 16: 2.58}` —
  Pauling electronegativities. Empirical values.
  Classification: INPUT (used in bond polarity correction).

**`src/ave/solvers/protein_bond_constants.py`**:
- Lines 70-72: `'Ca-C': {'length_A': 1.520, ...}` etc. — Backbone bond
  lengths from Engh & Huber 1991 crystallography for Ca-C, C-N, N-Ca.
  The C=O and N-H entries are noted as "solver-derived."
  Classification: INPUT (Ca-C, C-N, N-Ca are empirical; C=O, N-H are derived).

**Total: 17 distinct violations across 9 files.** Of these, M_P_MEV_TARGET flowing
into D_PROTON is the most structurally damaging because it contaminates the
nuclear derivation chain while a first-principles proton mass
(PROTON_ELECTRON_RATIO * M_E) exists in the same file.

### C2. Circular Import Chain with Import-Time Side Effects

**Files**: `constants.py` (line 458), `faddeev_skyrme.py`, `universal_operators.py`

`constants.py` calls `_compute_i_scalar_dynamic()` at module scope (line 465),
which imports `faddeev_skyrme.py`, which imports `universal_operators.py`, which
imports from `constants.py`. The cycle resolves only because the EPS_* guards are
defined before line 458. This is:

1. **Fragile**: any reordering of `constants.py` definitions will break it.
2. **Slow**: scipy minimization runs at import time. Every `import ave` triggers
   numerical optimization for 5 crossing numbers (proton + 4 resonances).
3. **Non-parallelizable**: the import lock prevents concurrent first-import.
4. **Silent failure risk**: if the scipy solver fails or returns a different
   minimum, every downstream constant silently changes.

Recommendation: Extract the baryon ladder computation into a lazy-evaluated
cache (compute on first access, not on import). Alternatively, pre-compute
and store the results as validated constants with a regeneration script.

### C3. M_P_MEV_TARGET Used as Computation Input Despite Being Labeled as Target

**File**: `src/ave/core/constants.py`, lines 601 and 611

```python
M_P_MEV_TARGET: float = 938.272088   # "used as binding energy targets"
D_PROTON: float = 4.0 * HBAR / (M_P_MEV_TARGET * 1e6 * e_charge / C_0**2 * C_0) * 1e15
```

D_PROTON depends on the empirical M_P_MEV_TARGET, not on the derived
PROTON_ELECTRON_RATIO. D_PROTON then feeds into D_NN_EIGENVALUE (line 639),
B_DEUTERON_PREDICTED (lines 645-646), OMEGA_0_NUCLEAR (line 663),
E_0_NUCLEAR (line 666), and K_COUPLING (line 669).

The entire nuclear sector below line 605 is calibrated to the empirical proton
mass rather than the first-principles derivation that exists 110 lines earlier.
This contradicts the zero-free-parameters claim for all nuclear predictions.

Recommendation: Replace `M_P_MEV_TARGET` in the D_PROTON calculation with
`PROTON_ELECTRON_RATIO * M_E * C_0**2 / (e_charge * 1e6)`. Keep M_P_MEV_TARGET only
as a comparison target with a percentage-error annotation.

---

## Warnings

### W1. JAX Backend Detection Is Fragile (9 occurrences)

**File**: `src/ave/core/universal_operators.py`, lines 67, 132, 256, 297, 425,
498, 619, 726, 756

```python
is_jax = hasattr(A, 'device_buffer') or 'jax' in str(type(A))
```

`device_buffer` was removed from JAX arrays in version 0.4+. The string
inspection `'jax' in str(type(A))` works but is slow and brittle across JAX
internal reorganizations. This pattern appears 9 times.

Recommendation: Define a single `_is_jax_array(x)` helper at module scope that
uses `isinstance` with a try/except import, then call it from all 9 locations.

### W2. Duplicate FDTD Implementations (NumPy vs JAX)

**Files**: `src/ave/core/fdtd_3d.py` and `src/ave/core/fdtd_3d_jax.py`

These files implement the same 3D FDTD solver — one in NumPy, one in JAX.
Any physics fix must be applied to both files independently. This is a
maintenance liability that will diverge over time.

Recommendation: Single implementation with a backend selector, or a shared
physics module with backend-specific array operations factored out.

### W3. Duplicate Bond Solver Approaches

**Files**: `src/ave/topological/soliton_bond_solver.py` and
`src/ave/solvers/bond_energy_solver.py`

Both solve for molecular bond energies and distances but use different
approaches (Slater orbital vs FDTD nuclear defect). Both contain independent
copies of the atomic mass unit (_M_U / _DA). The relationship between these
solvers and which should be preferred is undocumented.

### W4. NU_VAC Shadow in orbital_resonance.py

**File**: `src/ave/solvers/orbital_resonance.py`, line 404

```python
NU_VAC = 2.0 / 7.0
```

This is a local redefinition of `NU_VAC` which already exists in `constants.py`
at line 249. If the canonical value ever changes (or gains a correction term),
this shadow will silently retain the old value.

Recommendation: Import from constants.py.

### W5. Missing `__init__.py` in Two Packages

**Directories**: `src/ave/topological/`, `src/ave/solvers/`

These directories contain Python modules but no `__init__.py`. They function
as implicit namespace packages (PEP 420) but this is unusual and may confuse
some tooling (pytest discovery, IDE auto-import, type checkers).

### W6. No Dependency Management

No `requirements.txt`, `pyproject.toml`, `setup.py`, or `setup.cfg` exists.
The codebase has hard dependencies on numpy, jax, scipy, and optionally
matplotlib. Without pinned versions, the JAX backend detection (W1) and JAX
API usage may break on version updates.

### W7. AMU/Dalton Defined Three Times

**Files**:
- `condensed_matter.py:59` — `_M_U = 1.66053906660e-27`
- `bond_energy_solver.py:298` — `_DA = 1.66053906660e-27`
- `fluids_factory.py:122` — `1.66054e-27` (lower precision, inline)

The same physical constant is independently hard-coded in three files with
different names and different precisions. This is a DRY violation layered on
top of a constant violation (C1).

### W8. No Test Infrastructure

There are zero test files in the repository. For a framework claiming to derive
fundamental constants from first principles, the absence of automated
verification is a significant risk. A single constant redefinition or
operator sign error can silently invalidate all downstream predictions.

### W9. millennium.py Claims to Solve Millennium Prize Problems

**File**: `src/ave/axioms/millennium.py`

This module maps AVE concepts to P vs NP, the Riemann Hypothesis, the Hodge
Conjecture, and other Millennium Prize problems. These claims are extraordinary
and, presented without rigorous mathematical proof, risk undermining the
credibility of the legitimate derivation work elsewhere in the codebase.

### W10. Commented-Out Code and QUARANTINE Sections

**Files**: `src/ave/core/k4_tlm.py` (30+ lines of commented reasoning),
`src/ave/solvers/coupled_resonator.py` (documents ~1555 lines of removed code
in QUARANTINE comments)

Dead code and extensive removal documentation add noise. The git history
preserves what was removed; inline QUARANTINE comments do not need to remain.

### W11. Import of `jax.numpy` at Module Level in constants.py

**File**: `src/ave/core/constants.py`, line 27

```python
import jax.numpy as jnp
```

This makes JAX a hard dependency for the entire framework. Any module that
imports anything from `constants.py` requires JAX to be installed, even if
the module only uses NumPy constants. The sole use of `jnp` is for three
pre-computed phase boundary constants (R_I_JAX, R_II_JAX, R_III_JAX) at
lines 34-40.

Recommendation: Compute these three constants using plain Python math or
numpy, and convert to JAX arrays at point of use. This would make JAX an
optional dependency.

### W12. faddeev_skyrme.py Duplicates EPS_NUMERICAL

**File**: `src/ave/topological/faddeev_skyrme.py`, line 52

```python
_EPS_NUMERICAL = 1e-12
```

This local copy exists because of the circular import (C2). If the canonical
EPS_NUMERICAL in constants.py changes, this copy will diverge.

---

## Notes

### N1. Empirical Observational Data (Not Violations)

The following empirical data catalogs serve as boundary conditions or
validation targets. They are NOT constant violations because they represent
observational inputs to specific physical scenarios (galaxy masses, earthquake
profiles, gravitational wave events), not fundamental constants:

- `galactic_rotation.py`: GALAXY_CATALOG — galaxy masses, distances,
  scale lengths (these are specific system measurements)
- `orbital_resonance.py`: LIGO_EVENTS — black hole merger parameters
- `seismic.py`: PREM_LAYERS — Earth interior density/velocity profile
- `protein_bond_constants.py`: Z_TOPO — amino acid classification
  (topological, not empirical in the constant-violation sense)

### N2. Unit Conversion Constants

Several files define unit conversion factors (KPC, MPC, eV_TO_JOULE). These
are definitional (meter-to-kiloparsec is a human convention, not physics)
and are lower-priority violations. However, they should be consolidated into
a single location rather than scattered across files.

### N3. K_B Status Is Ambiguous

Boltzmann's constant K_B (constants.py:51) occupies an ambiguous position.
In the 2019 SI redefinition, K_B is exact by definition (like c and hbar).
If the framework treats the 2019 SI definitions as part of its base layer
(alongside C_0, HBAR, e_charge), then K_B is not a violation. If the
framework's base layer is strictly {M_E, ALPHA, G, C_0, HBAR, e_charge,
MU_0, EPSILON_0}, then K_B is an additional input. The docstring at the
top of constants.py does not list K_B among the SI definitions. This
ambiguity should be resolved explicitly.

### N4. `constants.py` Line Ordering Creates Implicit Contracts

The file has an implicit contract: definitions must appear in dependency
order because Python executes module-level statements sequentially. The
EPS_* definitions (lines 235-237) must precede the deferred import (line 458),
which must precede the baryon ladder (line 537), which must precede the
nuclear constants (line 597+). This ordering is documented only in a comment
at lines 230-233. A future editor who reorders for readability could break
the import chain.

### N5. Protein Bond Constants Mix Empirical and Derived Values

**File**: `src/ave/solvers/protein_bond_constants.py`

BACKBONE_BONDS contains both empirical values (Ca-C = 1.520 A from
crystallography) and derived values (C=O = 1.121 A, N-H = 0.817 A from
the soliton solver). The file documents this clearly (lines 61-66),
but the derived values show significant deviation from experiment
(C=O: 1.121 vs 1.23 A = -8.9%, N-H: 0.817 vs 1.01 A = -19.1%).
These deviations are acknowledged as "1D solver underestimates" but
suggest the solver needs multi-body corrections.

### N6. `_compute_baryon_ladder()` Performance

The baryon ladder computation runs scipy.optimize.minimize (L-BFGS-B) five
times at import. Each invocation minimizes a 1D energy functional with
numerical quadrature. On a modern machine this takes 1-3 seconds total.
This is acceptable for a one-time startup cost but will be noticeable in
rapid iteration workflows (e.g., test loops that import fresh).

---

## Strengths

**S1. Operator reuse architecture.** The design principle of routing all physics
through `universal_operators.py` and `scale_invariant.py` is sound. When
followed, it guarantees axiom compliance across all domains.

**S2. Comprehensive electroweak derivation chain.** The path from NU_VAC = 2/7
through sin^2(theta_W), CKM, PMNS, W/Z/Higgs masses is internally consistent
and well-documented with inline derivation steps and PDG comparison values.

**S3. Scale-invariant solver design.** The ABCD cascade, Y-matrix, and
coupled resonator solvers are genuinely domain-agnostic. The same
transmission line mathematics handles atomic ionization, molecular bonds,
and nuclear binding without modification.

**S4. Clear axiom traceability.** Most modules document which axioms they
invoke. The regime classification (linear/nonlinear/saturated/rupture) is
consistently applied. Functions typically cite their axiom basis in docstrings.

**S5. PMNS mixing angles.** The derivation in `mixing_derivation.py` achieves
remarkable agreement with NuFIT data: theta_12 (0.6% error), theta_23
(0.3% error), theta_13 (1.0% error). If these are genuine first-principles
results, they are the framework's strongest predictions.

**S6. Separation of validation from computation.** In most modules, empirical
comparison values appear only in comments, not in computation. The exceptions
(identified in C1) are the minority.

**S7. Thorough inline documentation.** constants.py in particular provides
detailed derivation narratives for every constant, making the physics
traceable without external documentation.

---

## Substrate-Scale Closure Update (post 2026-05-15 evening)

The 2026-05-15 evening session landed substantial framework refinement
that the engine now reflects through docstring updates (no code logic
changes):

### A-034: Universal Saturation-Kernel Strain-Snap Mechanism

**Canonical** L5 entry (`research/_archive/L5/axiom_derivation_status.md` A-034)
identifies $S(A) = \sqrt{1 - A^2}$ as the universal mechanism governing
every topological-reorganization event at every scale. **19 canonical
instances span 21 orders of magnitude.** The engine's Op2 (`universal_saturation`
in `core/universal_operators.py`) is the implementation; `scale_invariant.py`
and `master_equation_fdtd.py` both reference A-034 in their docstrings.

Notable empirical anchors:
- BCS B_c(T): **0.00% error** across all measured superconductors
  (`regime_3_saturated/condensed_matter.py`)
- BH merger ring-down: 1.7% from GR exact (`regime_3_saturated/black_hole_core.py`)
- Solar flares: NOAA GOES 40-yr validated (Vol 3 Ch 14)
- Schwarzschild radius: exact (`regime_3_saturated/black_hole_core.py`)

### Q-G47 Sessions 9-18: substrate-scale closure

Magic-angle equation $K(u_0^*) = 2 G(u_0^*)$ IS the substrate-scale
expression of $S(A^*) = 0$. The K4 lattice + its operating point IS the
substrate's "frozen at the saturation boundary" configuration. Axiom-level
Cosserat moduli relations (per Q-G47 Session 17):
- $\mu + \kappa = \xi_{K1} \cdot T_{EM}$
- $\beta + \gamma = \xi_{K2} \cdot T_{EM} \cdot \ell_{node}^2$
- $\xi_{K2} / \xi_{K1} = 12$ (K4-symmetry-forced via $|T| = 12$ universality)

Engine modules `k4_tlm.py`, `cosserat_field_3d.py`, `k4_cosserat_coupling.py`,
`vacuum_engine.py` all reference Q-G47 Sessions 9-18 closure in their
docstrings.

### Namespace caveat: ξ (Vol 3 Ch 1) vs ξ_K1, ξ_K2 (substrate)

The "ξ" symbol used in `gravity/` modules for the Vol 3 Ch 1 Machian
impedance integral ($\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$, magnitude
~10⁴³, cosmological scope) is DISTINCT from Q-G47 Sessions 9-18 substrate
prefactors $\xi_{K1}, \xi_{K2}$ (O(1) dimensionless). Different scopes,
same letter. Disambiguated in
`manuscript/ave-kb/common/xi-topo-traceability.md`.

### Continuous-springs framing (per Grant 2026-05-15)

The discrete K4 lattice (implemented by `k4_tlm.py`) is a discretization
of the underlying continuous Cosserat micropolar field (Axiom 1). Discrete
bond stiffnesses are samplings of the continuous constitutive tensor.
Sessions 12-15 discrete-bond scaffolds (`scripts/verify/q_g47_session{12,14,15}_*.py`)
are sanity-check discretizations, not the load-bearing physics.

### Measurement-hierarchy framing (engineered-substrate)

`AutoresonantCWSource` (in `vacuum_engine.py`) is explicitly the
phased-array PLL autoresonant mode of the A-034 measurement hierarchy
(per Grant 2026-05-15: single-emitter highest-SNR / multi-emitter bulk /
phased-array PLL autoresonant). Same mechanism as Propulsion Ch 5
autoresonant rupture, applied to coherent kernel amplification rather than
energy delivery.

### Cross-references

- L5 A-034: `research/_archive/L5/axiom_derivation_status.md`
- Backmatter Ch 7 catalog: `manuscript/backmatter/07_universal_saturation_kernel.tex`
- Vol 3 Ch 4 §TKI Strain-Snap: `manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex`
- Trampoline §7.5: `manuscript/ave-kb/common/trampoline-framework.md`
- AVE-QED Sessions 9-18: `../../AVE-QED/docs/analysis/2026-05-15_Q-G47_session*.md`
