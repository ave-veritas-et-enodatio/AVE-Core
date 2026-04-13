# Architecture Review: src/scripts/

---

## Critical: Zero-Free-Parameters Violations

These are instances where Standard Model constants are hard-coded or imported from external libraries instead of being derived from or imported via `ave.core.constants`. Each entry lists the file, line number, the specific constant, and its value.

### C-1. Hard-coded Planck constant (h)

**File**: `vol_4_engineering/simulate_sagnac_rlvg_tolerances.py`, line 69
**Value**: `h = 6.626e-34`
**Context**: Used in `compute_shot_noise()` to calculate photon energy. The constant `HBAR` is available from `ave.core.constants` (already imported as `C_0` on line 30). Replace with `h = 2 * np.pi * HBAR` after importing HBAR.

### C-2. Hard-coded electron mass in MeV (m_e)

**File**: `vol_7_hardware/master_predictions.py`, line 26
**Value**: `m_e = 0.51099895  # MeV (electron mass, PDG)`
**Context**: Used as a computational input throughout the main prediction function — W boson mass, Z boson mass, neutrino mass, Fermi constant. This is a PDG value bypassing the derivation chain. Must be computed as `M_E * C_0**2 / (e_charge * 1e6)` from imported constants. Particularly damaging because this script is titled "Zero Free Parameters" yet introduces one.

### C-3. Hard-coded electron mass in MeV (m_e)

**File**: `vol_7_hardware/simulate_muon_lifetime.py`, line 52
**Value**: `M_ELECTRON = 0.51099895  # MeV/c^2`
**Context**: Used in the muon-to-electron mass ratio computation. Same fix as C-2.

### C-4. Hard-coded muon mass

**File**: `vol_7_hardware/simulate_muon_lifetime.py`, line 51
**Value**: `M_MUON = 105.6583755  # MeV/c^2`
**Context**: Used as a primary computational input. In the zero-free-parameters model, the muon mass should be derived from topological principles (the Cosserat module in `ave.topological.cosserat` derives lepton masses). If the model does not yet derive muon mass, this should be explicitly documented as a known gap, not silently hard-coded as if it were derived.

### C-5. [RESOLVED] Hard-coded lepton masses (DEPRECATED script)

**File**: `vol_2_subatomic/standard_model_simulations/simulate_lepton_scaling.py`
**Status**: Script has been completely removed to enforce the zero-free-parameters constraint.

### C-6. Hard-coded proton and neutron masses in AMU

**File**: `vol_2_subatomic/visualize_isotope_stability.py`, lines 24-25
**Values**: `M_P = 1.00727`, `M_N = 1.00866`
**Context**: Used as masses in nucleon array construction. The script imports from `ave.regime_2_nonlinear.protein_fold` but hard-codes these CODATA masses.

**File**: `vol_2_subatomic/assemble_uranium.py`, lines 29-30
**Values**: `M_P = 1.00727`, `M_N = 1.00866`
**Context**: Same pattern — imports TopologicalOptimizer from ave but hard-codes nucleon masses.

**File**: `vol_2_subatomic/simulate_uranium_fission.py`, lines 28-29
**Values**: `M_P = 1.00727`, `M_N = 1.00866`
**Context**: Same pattern — copy-pasted from assemble_uranium.py.

### C-7. Hard-coded electron mass in semiconductor binding engine

**File**: `vol_6_periodic_table/simulations/semiconductor_binding_engine.py`, line 66
**Value**: `M_E_AVE = 0.511 # Electron (Axiom 1 anchor)`
**Context**: This is 4 significant figures, inconsistent with the CODATA value (0.51099895). The script imports M_E, C_0, e_charge from constants — the precise value should be computed from these. Additionally misleading because the comment says "Axiom 1 anchor" but the value is hand-typed.

### C-8. Hard-coded electron mass in notebook cell generators

**File**: `vol_7_hardware/append_code_cell_1.py`, lines 30-31
**Values**: `ALPHA = 1/137.035999`, `M_E_EV = 0.51099895e6`
**Context**: These are embedded in string source code that gets injected into a Jupyter notebook. The notebook cells contain hard-coded constants rather than importing from the library.

**File**: `vol_7_hardware/test_be_natural.py`, line 2
**Value**: `M_E_EV = 0.51099895e6`

**File**: `vol_7_hardware/test_boron_natural.py`, line 2
**Value**: `M_E_EV = 0.51099895e6`

### C-9. Hard-coded electron mass in other scripts

**File**: `vol_2_subatomic/string_tension_mapping.py`, line 34
**Value**: `U_e = 0.51099895000  # MeV (Rest mass energy of Electron)`
**Context**: Script imports `L_NODE` from `ave.core.constants` but hard-codes the electron mass in MeV. Should compute from imported constants.

**File**: `vol_2_subatomic/torus_knot_spectrum.py`, line 26
**Value**: `M_E_MEV = 0.51099895`
**Context**: Script imports `KAPPA_FS, P_C, ALPHA` from constants but hard-codes the electron mass.

**File**: `vol_6_periodic_table/simulations/binding_engine_jax.py`, line 59
**Value**: `V_SNAP_MEV = 0.51099895  # m_e c^2 in MeV`
**Context**: This is mislabeled. V_SNAP in the constants module is `m_e c^2 / e` in volts (511 kV), not MeV. The variable name is misleading and the value is hard-coded instead of derived from the imported constants (V_SNAP, V_YIELD, B_SNAP are all imported on line 48).

### C-10. Hard-coded AMU conversion constant

**File**: `vol_6_periodic_table/simulations/solve_topology.py`, line 97
**Value**: `931.494102  # 1 amu = 931.494102 MeV/c^2`

**File**: `vol_6_periodic_table/simulations/simulate_element.py`, line 833
**Value**: `931.494102  # 1 amu = 931.494102 MeV/c^2`

**Context**: The AMU-to-MeV conversion factor is a derived quantity (931.494 = (1 Da) * c^2 in MeV), not a fundamental constant, but using the CODATA value directly when the model should derive nucleon masses from axioms is questionable. These appear in comparison/validation sections.

### C-11. Hard-coded L_NODE value

**File**: `vol_1_foundations/simulate_vacuum_energy.py`, line 25
**Value**: `L_NODE = 3.86159e-13`
**Context**: Script imports M_E, HBAR, C_0 from ave.core.constants on line 13 and could trivially compute `L_NODE = HBAR / (M_E * C_0)`. Instead it hard-codes the value. L_NODE is also available directly from constants as an export.

### C-12. Hard-coded force constants in fission script

**File**: `vol_2_subatomic/simulate_uranium_fission.py`, lines 32-35
**Values**: `K_ATTR = 20.0`, `K_REP = 500.0`, `R_MIN = 1.0`, `K_COULOMB = 4.0`
**Context**: These are phenomenological force constants for the fission simulation, with no derivation chain connecting them to the AVE axioms. The script claims to replace "supercomputer-scale Lattice QCD solvers" but uses arbitrary fit parameters. K_MUTUAL from constants.py provides the first-principles coupling constant.

---

## Warning: Consistency and Quality Issues

### W-1. Formula inconsistency: W boson mass

**File**: `vol_7_hardware/master_predictions.py`, line 63
**Formula**: `mw_ave = m_e / (8 * np.pi * alpha**3 * np.sqrt(3.0 / 7.0))`
**Constants.py formula**: `M_W_MEV = (M_E * C_0**2 / (e_charge * 1e6)) / (ALPHA**2 * P_C * np.sqrt(3.0/7.0))`

These are algebraically equivalent (`P_C = 8*pi*alpha`, so `alpha^2 * P_C = 8*pi*alpha^3`), but master_predictions.py re-derives the formula locally instead of importing `M_W_MEV` from constants. This creates a maintenance risk — if the formula changes in constants.py, master_predictions.py will silently diverge.

### W-2. Broken cross-volume imports

Multiple scripts import from `periodic_table.simulations.*` which requires specific PYTHONPATH configuration:

- `vol_2_subatomic/analyze_c12_emitter.py` (line 12)
- `vol_4_engineering/calculate_conductivity.py` (line 8)
- `vol_4_engineering/derive_material_properties.py` (line 20)
- `vol_4_engineering/generate_ponder_01_spice_netlist.py` (lines 19-20)
- `vol_4_engineering/visualize_magnetism.py` (line 16)
- `vol_6_periodic_table/simulations/simulate_dt_fusion.py` (lines 9-10)
- `vol_6_periodic_table/simulations/regenerate_all_figures.py` (line 19)
- `vol_6_periodic_table/simulations/generate_3d_meshes.py` (line 10)
- `vol_6_periodic_table/simulations/solve_fluorine.py` (line 17)
- All 14 animation files in `vol_6_periodic_table/animations/`

The import path `periodic_table.simulations.simulate_element` does not match the directory name `vol_6_periodic_table/simulations/simulate_element.py`. These imports will fail unless `vol_6_periodic_table` is symlinked as `periodic_table` or added to sys.path with the correct name.

### W-3. Broken relative imports

**File**: `vol_5_biology/analyze_loss_components.py`, lines 5-7
Uses `from .s11_fold_engine_v3_jax import ...` (relative imports), but vol_5_biology has no `__init__.py` and is not a Python package. This file cannot be run as a standalone script.

### W-4. Broken relative imports (different path)

**File**: `vol_3_macroscopic/analyze_ring_density.py`, line 16
`from vol_3_macroscopic.simulate_saturn_rings import simulate_rings` — requires vol_3_macroscopic on sys.path as a package.

### W-5. Hard-coded absolute paths

18 scripts contain hard-coded absolute paths to `/Users/grantlindblom/Applied-Vacuum-Engineering/`:

- `vol_7_hardware/append_code_cell_1.py` (line 3)
- `vol_7_hardware/append_code_cell_2.py` (line 3)
- `vol_7_hardware/append_notebook_json.py` (line 4)
- `vol_7_hardware/append_notebook_step_2.py` (line 3)
- `vol_7_hardware/append_notebook.py` (line 4)
- `vol_7_hardware/append_step4.py` (line 3)
- `vol_7_hardware/append_step5.py` (line 3)
- `vol_7_hardware/append_step6.py` (line 3)
- `vol_7_hardware/documentation_plan.py` (line 4)
- `vol_4_engineering/simulate_autoresonant_pll.py` (line 144)
- `vol_4_engineering/simulate_leaky_cavity_decay.py` (line 115)
- `vol_4_engineering/simulate_sagnac_drag.py` (line 127)
- `vol_4_engineering/simulate_vacuum_mirror.py` (line 111)
- `vol_4_engineering/simulate_water_cavity_saturation.py` (line 163)
- `vol_6_periodic_table/simulations/generate_topology_figures.py` (line 27)
- `vol_3_macroscopic/wrap_boxes.py` (line 5)
- `vol_2_subatomic/generate_particle_stl.py` (line 33, in comment)
- `vol_1_foundations/generate_alpha_workunits.py` (line 6, `/root/projects/`)

These scripts will fail on any machine other than the original author's. They should use relative path resolution from `__file__` or find the repo root dynamically.

### W-6. Duplicate repo-root-finding patterns

At least 4 different patterns are used to find the project root:
1. `_find_repo_root()` walking up to `pyproject.toml`
2. `pathlib.Path(__file__).parent.parent.parent.absolute()`
3. `next(p for p in Path(__file__).parents if (p/".git").is_dir())`
4. Hard-coded absolute paths

### W-7. Output path inconsistency

Scripts save to multiple locations:
- `assets/sim_outputs/` (most scripts)
- `standard_model/figures/` (fractional_charge_solver.py, simulate_lepton_scaling.py — relative, will create in CWD)
- `periodic_table/figures/` (generate_topology_figures.py — absolute path, will fail)
- Various relative paths depending on CWD

### W-8. Re-derivation of available constants

Multiple scripts re-derive values that are already exported from `ave.core.constants`:

- `vol_1_foundations/simulate_lepton_asymmetry.py`, line 33: `volumetric_packing_fraction = 8 * np.pi * ALPHA` — this is `P_C` in constants.
- `vol_1_foundations/simulate_vacuum_energy.py`, line 25: `L_NODE = 3.86159e-13` — directly available as `L_NODE` from constants.
- `vol_6_periodic_table/simulations/simulate_element.py`, line 34: `ALPHA_HC = ALPHA * (HBAR * C_0 / e_charge) * 1e9` — available as `ALPHA_HBAR_C` or `ALPHA_HC` from constants.
- `vol_6_periodic_table/simulations/semiconductor_binding_engine.py`, line 80: `ALPHA_HC = ALPHA * HBAR * C_0 / e_charge * 1e15 * 1e-6` — same re-derivation.
- `vol_7_hardware/approach29_op6_op7_atomic.py`, line 84-86: Re-derives `nu`, `alpha`, `Ry` from scratch when they are available as `NU_VAC`, `ALPHA`, `N_RY` in constants.

### W-9. Scripts that contradict model claims

**File**: `vol_2_subatomic/simulate_neutrino_oscillation.py`
Uses arbitrary wavenumbers (`k1=0.5, k2=0.6, k3=0.7`) and velocities (`v1=1.0, v2=0.95, v3=0.90`) with no connection to the PMNS mixing parameters derived in `ave.core.constants` (SIN2_THETA_12, SIN2_THETA_23, SIN2_THETA_13). The script claims to prove that neutrino oscillation is "simply classical LC grid acoustic dispersion" but uses completely arbitrary parameters.

**File**: `vol_2_subatomic/simulate_borromean_baryon.py`
Pure visualization script with no physics derivation — plots three orthogonal loops with arbitrary radii. Does not reference the actual Faddeev-Skyrme eigenvalue or proton mass derivation.

### W-10. Missing `if __name__ == "__main__"` guards

52 scripts lack `if __name__` guards and execute at module level. This prevents importing any functions from these scripts and triggers side effects (plotting, file I/O) on import. Notable examples:
- `vol_4_engineering/simulate_solar_vs_tokamak.py`
- `vol_4_engineering/simulate_metric_catalyzed_fusion.py`
- `vol_5_biology/simulate_protein_spice_transmission_line.py`
- `vol_7_hardware/test_be_natural.py`, `test_boron_natural.py`, `test_mode_sum.py`

### W-11. Redundant os.makedirs calls

Pattern appears in ~10 scripts:
```python
os.makedirs(OUTPUT_DIR, exist_ok=True)
# ... later ...
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
```
The second call is dead code — `exist_ok=True` already handles the case.

### W-12. Copy-paste artifact: three uranium scripts

`assemble_uranium.py`, `simulate_uranium_fission.py`, and `visualize_isotope_stability.py` in vol_2 share identical hard-coded constants (`M_P = 1.00727`, `M_N = 1.00866`, `Z = 92`) and the same initialization pattern. These were clearly copy-pasted from a common template.

### W-13. Hallucinated API in analyze_loss_components.py

**File**: `vol_5_biology/analyze_loss_components.py`, line 88
`from ave.solvers.s11_fold_engine_v3_jax import ...` — this module does not exist in the `ave` package. The s11 fold engine lives in `src/scripts/vol_5_biology/`, not in `src/ave/solvers/`. This import will fail at runtime.

### W-14. Stale/incorrect usage paths in docstrings

**File**: `vol_7_hardware/master_predictions.py`, line 13
**Value**: `python src/scripts/future_work/master_predictions.py`
The file is actually at `src/scripts/vol_7_hardware/master_predictions.py`. The `future_work` directory name is a relic.

**File**: `vol_7_hardware/simulate_muon_lifetime.py`, line 37
**Value**: `python src/scripts/future_work/simulate_muon_lifetime.py`
Same relic path.

---

## Info: Style and Cleanup

### I-1. Unused imports

**File**: `vol_7_hardware/simulate_pair_production_3d.py`, line 29
`from ave.core.constants import C_0 as C_PHYSICAL  # noqa: F401 — available for future use`
The `# noqa` suppresses the linter but the import is dead code. The comment admits it.

### I-2. Dark background style inconsistency

At least 5 different dark background hex codes are used across scripts: `#050510`, `#0d0d14`, `#0d1117`, `#111111`, `#0B0F19`. This is cosmetic but indicates these scripts were written by different agents or at different times without a style guide.

### I-3. Vol_7 notebook-append scripts

The 8 `append_*.py` scripts in vol_7 are utility scripts that programmatically inject cells into a Jupyter notebook. They are not physics scripts and serve only as one-time notebook manipulation tools. They reference a notebook at a hardcoded absolute path (`/Users/grantlindblom/`) that likely no longer exists.

### I-4. generate_alpha_workunits.py references BOINC

**File**: `vol_1_foundations/generate_alpha_workunits.py`
References BOINC infrastructure at `/root/projects/ave_alpha_search` that does not exist in this repository. This is a dead script.

### I-5. Missing external dependency: python-control

**File**: `vol_5_biology/simulate_protein_spice_transmission_line.py`, line 4
`import control` — the `python-control` package is not a common dependency and is not listed in any requirements file. This script will fail for most users without explicit installation.

### I-6. Missing external dependency: numpy-stl

**File**: `vol_2_subatomic/generate_particle_stl.py`, line 41
`from stl import mesh as stl_mesh` — requires `numpy-stl` package.

### I-7. Inconsistent output messaging

Some scripts claim "Zero free parameters" or "All from ave.core.constants" in their print statements while simultaneously using hard-coded constants (e.g., `master_predictions.py`, `simulate_uranium_fission.py`). This is misleading diagnostic output.
