# Scripts Architecture

## Overview

The `src/scripts/` directory contains 317 Python files organized into 7 volume directories, each corresponding to a manuscript volume of the AVE (Applied Vacuum Electrodynamics) framework. Scripts are standalone programs — each typically has its own `main()` or `if __name__ == "__main__"` block — used for derivations, simulations, visualizations, and validation of the physics model described in the manuscript.

---

## Volume Directories

### `vol_1_foundations/` (28 files)

Manuscript relationship: Volume 1 covers the foundational axioms of the AVE framework — the LC lattice structure, double-slit reinterpretation, vacuum phonon propagation, operating regimes, and fundamental constant derivations.

| Script | Description |
|--------|-------------|
| `animate_double_slit_dark_wake.py` | GIF animation of double-slit experiment with/without observer side-by-side |
| `animate_vacuum_phonon_3d.py` | Animates a Gaussian wave packet (photon) on a 2D lattice slice |
| `demo_engine.py` | Demonstrates VacuumGrid and TopologicalNode from `ave.core` |
| `derive_alpha_m4_pro.py` | Computes fine-structure constant via 3D rigidity percolation on large lattice |
| `double_slit_design_space.py` | Sweeps double-slit parameters: frequency, spacing, N-slit, observer impedance |
| `generate_alpha_workunits.py` | Generates BOINC-style workunits for distributed alpha computation |
| `plot_calibration_flow.py` | Flowchart of calibration inputs to derived constants |
| `plot_double_slit_comparison.py` | Side-by-side Standard Model vs AVE double-slit interpretation |
| `plot_emt_packing_landscape.py` | K/G ratio vs packing fraction with p*=8piAlpha operating point |
| `plot_epsilon_eff.py` | Axiom 4 saturation: epsilon_eff(A) and C_eff(A) curves |
| `plot_neon20_geometry.py` | 3D trigonal bipyramid geometry of Ne-20 alpha clusters |
| `plot_operating_regimes.py` | Stress-strain phase diagram showing 3 AVE operating regimes |
| `simulate_3d_lattice.py` | Constructs and visualizes the SRS (K4) chiral lattice |
| `simulate_cosmological_equilibrium.py` | Derives Hubble constant from latent heat equilibrium |
| `simulate_double_slit_observer_jax.py` | JAX-accelerated FDTD double-slit simulation |
| `simulate_double_slit_observer.py` | NumPy FDTD double-slit with/without observer |
| `simulate_double_slit_wake.py` | FDTD ponderomotive wake simulation of double slit |
| `simulate_gup_resolution.py` | Generalized Uncertainty Principle from Brillouin zone cutoff |
| `simulate_helical_confinement.py` | Wave confinement into helical spin-1 topology under increasing impedance |
| `simulate_lepton_asymmetry.py` | Derives CP-violating chirality and matter-antimatter asymmetry from alpha |
| `simulate_macroscopic_avalanche.py` | Gravitational induction field and yield horizon visualization |
| `simulate_vacuum_energy.py` | Derives dark energy density from zero-point LC network energy |
| `simulate_weak_boson_modes.py` | W/Z bosons as torsional vs transverse impedance modes |
| `simulate_yee_cell_update.py` | 3D diagram of FDTD Yee cell staggered field layout |
| `verify_universe.py` | AST scanner verifying no smuggled Standard Model constants in `src/ave/` |
| `visualize_dark_wake.py` | Instantaneous pressure field of double-slit with dark wake visible |
| `visualize_photon_helicity.py` | 3D FDTD helical photon propagation through chiral lattice |
| `visualize_topological_bounds.py` | Borromean linkage bounds and Witten fractionalization |

### `vol_2_subatomic/` (40 files + 5 in subdirectories)

Manuscript relationship: Volume 2 covers subatomic physics — atomic orbitals, electroweak unification, baryon structure, particle masses, neutrino oscillation, and the Higgs mechanism.

| Script | Description |
|--------|-------------|
| `analyze_c12_emitter.py` | Analyzes C-12 nuclear emitter topology |
| `assemble_uranium.py` | Optimizes 235-nucleon cloud into U-235 crystal structure |
| `electron_interferometry_parallax.py` | Electron de Broglie interferometry calculation |
| `fem_borromean_convergence.py` | FEM convergence test for Borromean link integrals |
| `fem_borromean_convergence_jax.py` | JAX-accelerated version of FEM Borromean convergence |
| `generate_particle_stl.py` | Generates 3D-printable STL meshes of topological particles |
| `generate_particle_topology_suite.py` | Batch generates topology visualizations for particle zoo |
| `generate_verification_trace.py` | Produces a verification trace of all derived constants |
| `higgs_impedance_mapping.py` | Maps Higgs VEV to characteristic impedance Z_0 |
| `merge_orbitals.py` | Merges orbital visualization outputs into composite image |
| `plot_chiral_dispersion.py` | Plots chiral dispersion relation of the K4 lattice |
| `plot_hydrogen_orbitals.py` | Visualizes hydrogen orbital shapes |
| `plot_mass_oscillator_flow.py` | Mass-oscillator flow diagram |
| `plot_photon_helical_spin.py` | Photon helical spin visualization |
| `plot_thermal_skyrmion.py` | Thermal Skyrmion profile visualization |
| `simulate_atomic_orbitals.py` | Spherical harmonic orbital computation |
| `simulate_atomic_spectra.py` | Derives Rydberg spectrum from AVE constants |
| `simulate_bh_orbital_resonance.py` | Black hole orbital resonance frequencies |
| `simulate_bh_untapped_predictions.py` | Novel black hole predictions from orbital resonance |
| `simulate_borromean_baryon.py` | Borromean baryon (proton) 3-loop linkage visualization |
| `simulate_chiral_network.py` | Chiral LC network mode simulation |
| `simulate_cross_scale_triptych.py` | Cross-scale verification: atomic, planetary, galactic |
| `simulate_dynamic_orbitals.py` | Dynamic orbital eigenmode solver with impedance matching |
| `simulate_electron_topology.py` | Electron unknot topology visualization |
| `simulate_electroweak_unification.py` | Full electroweak derivation: W, Z, Higgs from axioms |
| `simulate_g2.py` | Electron g-2 anomalous magnetic moment from Cosserat |
| `simulate_higgs_rupture.py` | Higgs mechanism as dielectric rupture of LC lattice |
| `simulate_hoop_stress.py` | Hoop stress of soliton confinement |
| `simulate_longitudinal_entanglement.py` | Longitudinal entanglement wave simulation |
| `simulate_neutrino_oscillation.py` | Neutrino flavor oscillation as lattice dispersion |
| `simulate_string_theory_mapping.py` | Maps string theory concepts to LC network |
| `simulate_uranium_fission.py` | U-235 fission via topological shear failure |
| `solve_helium_ground_state.py` | He ground state from impedance cavity eigenmodes |
| `solve_orbital_eigenmodes.py` | General orbital eigenmode solver for multi-electron atoms |
| `string_tension_mapping.py` | Maps string tension to inductive energy density |
| `torus_knot_spectrum.py` | Baryon resonance spectrum from (2,q) torus knots |
| `visualize_isotope_stability.py` | U-235 vs U-238 structural stability comparison |
| `visualize_self_trapping.py` | Self-trapping of soliton in impedance well |
| **standard_model_animations/** | |
| `animate_lepton_decay.py` | Animated lepton decay via RC discharge |
| `simulate_beta_decay_spark.py` | Beta decay spark animation |
| `simulate_nambu_goto_lc.py` | Nambu-Goto string action mapped to LC inductance |
| **standard_model_simulations/** | |
| `fractional_charge_solver.py` | Quark fractional charges from Borromean flux projections |


### `vol_3_macroscopic/` (33 files)

Manuscript relationship: Volume 3 covers macroscopic phenomena — gravity, cosmology, dark matter, Saturn rings, solar physics, black holes, and gravitational lensing.

| Script | Description |
|--------|-------------|
| `analyze_ring_density.py` | Saturn ring radial impedance analysis |
| `animate_k4_tlm_lensing.py` | Animated K4 TLM gravitational lensing |
| `animate_k4_tlm_lensing_ultra.py` | High-resolution K4 TLM lensing animation |
| `animate_kerr_lensing.py` | Animated Kerr metric gravitational lensing |
| `demo_black_hole_capture.py` | Black hole particle capture demonstration |
| `fetch_and_plot_noaa_goes_flares.py` | Fetches NOAA solar flare data and plots it |
| `k4_tlm_gravitational_lensing.py` | Static K4 TLM gravitational lensing computation |
| `plot_cross_scale_verification.py` | Cross-scale verification summary plot |
| `plot_hubble_tension.py` | AVE H-infinity vs Planck vs SH0ES Hubble tension |
| `plot_jwst_accretion.py` | JWST accretion anomaly analysis |
| `plot_lense_thirring_inductive_drag.py` | Lense-Thirring frame dragging as inductive drag |
| `plot_meissner_gear_train.py` | Meissner effect gear train analogy |
| `plot_optical_metric.py` | Optical metric visualization |
| `simulate_black_hole_core.py` | Black hole interior regime mapping |
| `simulate_bullet_cluster_fdtd.py` | Bullet cluster dark matter via FDTD |
| `simulate_cosmology_bao.py` | BAO scale from AVE cosmological parameters |
| `simulate_dark_matter_detectors.py` | Dark matter detector sensitivity predictions |
| `simulate_entropy_noise_scattering.py` | Entropy-noise scattering on vacuum grid |
| `simulate_gargantua_acoustic_vortex.py` | Black hole acoustic vortex (Gargantua-style) |
| `simulate_gravitational_waves_lc.py` | Gravitational waves as LC lattice shear modes |
| `simulate_ideal_gas_law_lc.py` | Ideal gas law emergent from LC lattice |
| `simulate_jwst_accretion.py` | JWST early galaxy accretion simulation |
| `simulate_oort_cloud_trap.py` | Oort cloud as gravitational impedance trap |
| `simulate_orbital_standing_waves.py` | Planetary orbital standing waves |
| `simulate_phase_locked_superconductivity.py` | Phase-locked superconductivity simulation |
| `simulate_sagnac_impedance_drag.py` | Sagnac effect with impedance drag |
| `simulate_saturn_rings.py` | N-body Saturn ring formation from impedance gaps |
| `simulate_solar_flare.py` | Solar flare energy release simulation |
| `simulate_solar_weather_calculator.py` | Solar weather calculator with yield thresholds |
| `visualize_regime_map.py` | Regime map visualization (Linear/Nonlinear/Saturated/Rupture) |
| `vlbi_impedance_parallax.py` | VLBI impedance parallax calculation |
| `water_lattice_proof.py` | Water anomalies from LC lattice properties |
| `wrap_boxes.py` | LaTeX chapter box-wrapping utility |

### `vol_4_engineering/` (107 files)

Manuscript relationship: Volume 4 covers engineering applications — antenna design, ponderomotive devices, FDTD simulations, material properties, fusion reactors, Sagnac gyroscopes, and experimental falsification protocols. This is the largest volume.

Scripts span these categories:
- **Antenna/RF design**: `antenna_design_water.py`, `antenna_water_dark_wake.py`, `chiral_antenna_q_analysis.py`, `beltrami_hopf_coil.py`
- **Hopf-01 antenna characterization**: 9 scripts (`hopf_01_*.py`, `hopf_02_*.py`) analyzing torus-knot antenna S-parameters, impedance models, substrate comparisons, and sensitivity analyses
- **K4 TLM validation**: 3 phases of K4 Transmission Line Matrix validation (`k4_tlm_phase*.py`)
- **Ponder-01 device**: ~25 scripts (`ponder_01_*.py`, `simulate_ponder_01_*.py`) covering FDTD near-field, far-field, thrust modeling, dark-wake animation, thermal analysis, impedance matching, discrete LC mesh, and 3D volumetric animations
- **Ponder-05 device**: `ponder_05_characterization.py`, `ponder_05_gravity_parallax.py`, `plot_ponder05_saturation.py`
- **Sagnac RLVG**: `simulate_sagnac_*.py`, `sagnac_geo_parallax.py`, `plot_sagnac_entrainment.py`
- **Fusion/energy**: `simulate_metric_catalyzed_fusion.py`, `simulate_solar_vs_tokamak.py`, `plot_fusion_crisis_audit.py`, `simulate_tokamak_dielectric_leakage.py`
- **Materials**: `derive_material_properties.py`, `calculate_conductivity.py`, `simulate_llcp_dopant_sweep.py`
- **SPICE/circuit modeling**: `generate_ponder_01_spice_netlist.py`, `simulate_hardware_netlists.py`, `run_log_imp_s_params.py`
- **White dwarf/astrophysics**: `wd_shear_eigenfrequency.py`, `white_dwarf_saturation_redshift.py`
- **Other**: `simulate_casimir_cavity.py`, `simulate_vacuum_birefringence_E4.py`, `simulate_vacuum_mirror.py`, `simulate_kinetic_armor_yield.py`, `simulate_neuromorphic_memristor.py`, `simulate_smes_battery.py`, `simulate_solar_led.py`, `simulate_topological_qubit_3d.py`, `born_huang_percolation.py`, `simulate_rigidity_percolation.py`

### `vol_5_biology/` (26 files)

Manuscript relationship: Volume 5 covers biological applications — protein folding via transmission line S-parameters, amino acid impedance mapping, membrane physics, and FRET parallax.

| Script | Description |
|--------|-------------|
| `amino_chain_pipeline.py` | End-to-end amino acid chain → S-parameter → folding pipeline |
| `analyze_loss_components.py` | Decomposes S11 loss into individual component contributions |
| `batch_amino_spice_solver.py` | Batch SPICE solver for amino acid transmission line models |
| `derive_z_topo_first_principles.py` | Derives Z_topo (topological impedance) from first principles |
| `fret_chiral_parallax.py` | FRET chiral parallax prediction |
| `generate_amino_spice.py` | Generates SPICE netlists for amino acid residues |
| `ramachandran_steric.py` | Ramachandran plot from steric impedance constraints |
| `ramachandran_steric_jax.py` | JAX-accelerated version of Ramachandran steric |
| `rmsd_benchmark.py` | RMSD benchmark against known protein structures |
| `s_param_network_engine.py` | S-parameter network cascade engine for protein chains |
| `s11_fold_engine_v3_jax.py` | JAX S11 reflection fold engine v3 |
| `s11_fold_engine_v4_ymatrix.py` | Y-matrix S11 fold engine v4 |
| `s12_pdb_validation.py` | PDB structure validation against S-parameter predictions |
| `s13_oligomer_assembly.py` | Oligomer assembly simulation |
| `s14_folding_kinetics.py` | Protein folding kinetics via RC discharge |
| `s15_allosteric_yield.py` | Allosteric yield from impedance matching |
| `s16_allosteric_pathway_map.py` | Allosteric pathway mapping |
| `s17_sub5_rmsd_benchmark.py` | Sub-5 Angstrom RMSD benchmark |
| `simulate_ftir_comparison.py` | FTIR spectrum comparison with impedance model |
| `simulate_membrane_llcp.py` | Membrane LLCP (cholesterol phase buffer) simulation |
| `simulate_protein_spice_transmission_line.py` | Protein as SPICE transmission line model |
| `spice_organic_mapper.py` | Maps organic molecules to SPICE circuit parameters |
| `stress_test_20_sequences.py` | Stress test of fold engine on 20 sequences |
| `test_membrane_llcp.py` | Unit tests for membrane LLCP simulation |
| `test_vswr_fold.py` | Tests VSWR-based protein fold predictions |
| `validate_tau_fold.py` | Validates tau protein fold predictions |

### `vol_6_periodic_table/` (37 files across 5 subdirectories)

Manuscript relationship: Volume 6 covers the periodic table — nuclear binding energies, element-by-element solvers, orbital topology, 3D mesh generation, SPICE circuit equivalents, and per-element animations.

| Subdirectory | Contents |
|---|---|
| `simulations/` | `simulate_element.py` (master element solver), `binding_engine_jax.py`, `binding_scf_solver.py`, `semiconductor_binding_engine.py`, `alpha_cascade_engine.py`, per-element solvers (`solve_aluminum.py`, `solve_fluorine.py`, `solve_magnesium.py`, `solve_neon.py`, `solve_oxygen.py`, `solve_silicon.py`, `solve_sodium.py`), `solve_topology.py`, `generate_3d_meshes.py`, `generate_orbital_strain.py`, `generate_topology_figures.py`, `regenerate_all_figures.py`, `simulate_dt_fusion.py`, `spice_exporter.py` |
| `animations/` | Per-element animations (`animate_hydrogen.py` through `animate_silicon.py`), `build_animators.py`, `generate_dynamic_flux.py` |
| `circuits/` | `make_circuits.py`, `make_heavy_circuits.py`, `generate_all_semiconductor_circuits.py` |
| `figures/` | (output directory for generated figures) |
| Root | `generate_periodic_table.py` |

### `vol_7_hardware/` (40 files)

Manuscript relationship: Volume 7 covers hardware predictions, experimental falsification, and advanced topics — warp metrics, pair production, galaxy rotation, muon lifetime, BCS superconductivity, seismic analysis, and master prediction tables.

| Script | Description |
|--------|-------------|
| `master_predictions.py` | Comprehensive prediction table: 30+ quantities vs PDG values |
| `approach29_op6_op7_atomic.py` | Atomic solver approach 29 using dimensionless natural units |
| `bcs_superconductor_validation.py` | BCS superconductor gap validation against AVE plasma module |
| `bh_interior_regime_iv.py` | Black hole interior regime IV analysis |
| `batch_generate_remaining_figures.py` | Batch figure generation for remaining manuscript items |
| `plot_birefringence_killswitch.py` | Vacuum birefringence falsification threshold |
| `plot_sagnac_rlve_prediction.py` | Sagnac RLVE prediction plot |
| `plot_tabletop_falsification_thresholds.py` | Tabletop experiment falsification thresholds |
| `plot_topological_pfc.py` | Topological PFC (plasma facing component) analysis |
| `plot_vacuum_aerodynamics.py` | Vacuum aerodynamics prediction |
| `plot_vacuum_tesla_coil.py` | Vacuum Tesla coil prediction |
| `simulate_casimir_superconductor.py` | Casimir force with superconductor geometry |
| `simulate_galaxy_rotation.py` | Galaxy rotation curve from impedance saturation |
| `simulate_muon_lifetime.py` | Muon lifetime from RC discharge of topological cavity |
| `simulate_nested_sleep_pods.py` | Nested time-dilation sleep pod simulation |
| `simulate_pair_production_3d.py` | 3D pair production FDTD simulation |
| `simulate_pair_production_transient.py` | Pair production transient analysis |
| `simulate_quantum_measurement_cfd.py` | Quantum measurement as CFD wave solver |
| `simulate_quantum_measurement_cfd_jax.py` | JAX version of quantum measurement CFD |
| `simulate_seismic_ave.py` | AVE seismic wave propagation |
| `simulate_warp_metric_cfd.py` | Warp metric CFD simulation |
| `simulate_warp_metric_oam_drill.py` | Warp metric with OAM drill topology |
| `simulate_warp_metric_tensors.py` | Warp metric tensor field computation |
| `simulate_warp_metric_time_evolution_3d.py` | 3D warp metric time evolution |
| `simulate_water_anomaly.py` | Water anomalies from fluids factory module |
| `test_be_natural.py` | Beryllium solver in natural units |
| `test_boron_natural.py` | Boron solver in natural units |
| `test_mode_sum.py` | Mode sum convergence test |
| `test_scale_invariance.py` | Scale invariance test across regimes |
| `test_weighted_lc.py` | Weighted LC network test |
| `append_*.py` (8 files) | Jupyter notebook cell-append utilities for approach history |
| `documentation_plan.py` | Documentation plan notebook cell generator |

---

## Import Patterns

### Scripts that import from `src/ave/`

Approximately 130 of the 317 scripts import from the `ave` library. The most commonly used modules:

- `ave.core.constants` — the primary import target, used by ~100 scripts for physical constants (ALPHA, C_0, M_E, HBAR, Z_0, V_YIELD, V_SNAP, P_C, etc.)
- `ave.core.fdtd_3d` / `ave.core.fdtd_3d_jax` — 3D FDTD engines, typically with JAX-first fallback pattern
- `ave.core.k4_tlm` — K4 Transmission Line Matrix lattice
- `ave.core.regime_map` — regime classification functions
- `ave.core.universal_operators` — universal saturation, impedance, reflection operators
- `ave.core.grid` / `ave.core.node` — VacuumGrid and TopologicalNode
- `ave.topological.*` — Borromean topology, Faddeev-Skyrme, Cosserat, soliton solvers
- `ave.solvers.*` — orbital resonance, coupled resonator, protein bond constants, transmission line
- `ave.gravity.*` — stellar interior, gravitational wave propagation, neutrino MSW
- `ave.axioms.*` — scale invariant, saturation factor, spectral gap
- `ave.regime_*` — regime-specific modules (fluids_factory, protein_fold, galactic rotation)
- `ave.plasma.*` — superconductor, cutoff modules

### Self-contained scripts (~125 files)

The remaining scripts do not import from `ave` at all. These fall into two categories:
1. **Pure visualization/animation scripts** that use only numpy/matplotlib for conceptual illustrations
2. **Early scripts** written before the ave library existed, which hard-code their own constants

### Cross-volume imports

Several scripts import from other scripts rather than the ave library:
- Many `vol_6_periodic_table/` scripts import from `periodic_table.simulations.simulate_element`
- `vol_4_engineering/` has 4 scripts importing from `periodic_table.simulations.*`
- `vol_3_macroscopic/analyze_ring_density.py` imports from `vol_3_macroscopic.simulate_saturn_rings`
- `vol_5_biology/` has intra-volume relative imports (`.s11_fold_engine_v3_jax`, `ramachandran_steric`, `spice_organic_mapper`)

---

## Common Patterns

### Plotting

Nearly all scripts (363 matplotlib imports) generate plots. The dominant aesthetic is dark-background (`#050510`, `#0d0d14`, `#0d1117`, `#111111`). Most scripts save PNG figures.

### Output location

Scripts save output primarily to `assets/sim_outputs/` relative to the repository root. Several patterns exist for resolving this path:
- `os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'sim_outputs')`
- Finding repo root by walking up to `pyproject.toml` or `.git`
- `pathlib.Path(__file__).parent.parent.parent.absolute()`
- A few scripts save to `standard_model/figures/` (relative, likely broken)

### JAX fallback pattern

Scripts using the 3D FDTD engine follow a standard pattern:
```python
try:
    from ave.core.fdtd_3d_jax import FDTD3DEngineJAX as FDTD3DEngine
except ImportError:
    from ave.core.fdtd_3d import FDTD3DEngine
```

### Script entry points

264 scripts have `if __name__ == "__main__"` guards. 52 scripts execute at module level (no guard), including several plot-generation scripts, test files, and notebook-append utilities.

---

## External Dependencies

| Package | Usage |
|---------|-------|
| `numpy` | Universal — numerical computation |
| `matplotlib` | Universal — plotting and animation |
| `jax` / `jax.numpy` | ~32 files — GPU-accelerated computation, optional with numpy fallback |
| `scipy` | ~38 files — `scipy.sparse`, `scipy.spatial`, `scipy.special`, `scipy.optimize`, `scipy.ndimage` |
| `PIL` / `Pillow` | 6 files — image composition for vol_6 animations |
| `networkx` | 1 file — `vol_4_engineering/simulate_rigidity_percolation.py` |
| `python-control` | 2 files — `vol_5_biology/amino_chain_pipeline.py`, `simulate_protein_spice_transmission_line.py` |
| `numpy-stl` | 1 file — `vol_2_subatomic/generate_particle_stl.py` |
| `imageio` | 1 file — `vol_3_macroscopic/animate_k4_tlm_lensing.py` |
| `nbformat` | 1 file — `vol_7_hardware/append_notebook.py` |

---

## Shared Utilities

There are no formal shared utility modules within the scripts directories. The closest equivalents are:

- `vol_6_periodic_table/simulations/simulate_element.py` — acts as a de facto shared module, with `get_nucleon_coordinates()` imported by ~20 scripts across volumes 2, 4, and 6
- `vol_6_periodic_table/simulations/spice_exporter.py` — SPICE netlist generation, imported by 3 scripts
- `vol_5_biology/spice_organic_mapper.py` — organic molecule SPICE mapping, imported by 3 scripts within vol_5
- `vol_5_biology/ramachandran_steric.py` — steric calculation, imported by 2 scripts within vol_5
- `vol_5_biology/s11_fold_engine_v3_jax.py` — fold engine, imported by `analyze_loss_components.py`

The `__init__.py` at the scripts root is empty (0 bytes). No subdirectories have `__init__.py` files.
