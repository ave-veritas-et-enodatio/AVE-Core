# Phase 0 Survey — Vol 2: The Subatomic Scale

**Volume path:** `/manuscript/vol_2_subatomic/`
**Main entry:** `main.tex`
**Survey date:** 2026-04-02

---

## 1. Document Hierarchy

```
VOLUME 2: The Subatomic Scale
├── [frontmatter — not surveyed]
│     00_title.tex
│     ../frontmatter/00_foreword.tex
│     ../frontmatter/00_nomenclature.tex
│
├── Chapter 1: Topological Matter: Fermion Generations          [ch:topological_matter, ~153 lines]
│   ├── 1.1  Mathematical Topology of Mass
│   ├── 1.2  Newtonian Inertia as Macroscopic Lenz's Law
│   ├── 1.3  The Electron: The Fundamental Unknot ($0_1$)
│   ├── 1.4  Regime Classification of Topological Matter
│   ├── 1.5  Torus Knot Phase Winding Ladder
│   └── 1.6  Chirality and Antimatter Disintegration
│
├── Chapter 2: The Baryon Sector: Confinement and Fractional Quarks  [ch:baryons, ~382 lines]
│   ├── 2.1  Borromean Confinement
│   ├── 2.2  Proton Mass (The Dynamic Tensor Deficit)
│   │   └── 2.2.1  The Topological Origin of Quark Flavors
│   ├── 2.3  Baryon Resonance Spectrum
│   │   ├── 2.3.1  The Self-Consistent Mass Oscillator (The Structural Eigenvalue)  [DUPLICATE — appears twice]
│   │   ├── 2.3.2  Thermal Softening and the Deconfinement Transition  [sec:thermal_softening]
│   │   └── 2.3.3  Hadronic Spectrum
│   ├── 2.4  Topological Fractionalization
│   ├── 2.5  Neutron Decay
│   ├── 2.6  Helium-4 Nucleus
│   └── 2.7  Hierarchy Bridge
│
├── Chapter 3: The Neutrino Sector: Chiral Unknots                   [ch:neutrino_sector, ~274 lines]
│   ├── 3.1  Mass Without Charge
│   ├── 3.2  Chiral Exclusion Principle                              [sec:chiral_screening]
│   ├── 3.3  Neutrino Mass Eigenvalue
│   ├── 3.4  Neutrino Oscillation
│   ├── 3.5  PMNS Mixing Angles                                      [sec:pmns_eigenvalues, sec:pmns_junction]
│   └── 3.6  Neutrino Mass Hierarchy                                 [sec:delta_cp]
│
├── Chapter 4: Quantum Spin as Classical Gyroscopic Precession       [ch:quantum_spin, ~82 lines]
│   ├── 4.1  Introduction
│   └── 4.2  Continuous Mechanics of the Spinor Transition
│       ├── 4.2.1  Larmor Derivation via Topological Gyroscopes
│       └── 4.2.2  Visual Equivalence
│
├── Chapter 5: Electroweak Mechanics and Gauge Symmetries            [ch:electroweak, ~161 lines]
│   ├── 5.1  Electrodynamics (The Gradient of Topological Phase)
│   ├── 5.2  The Weak Interaction
│   └── 5.3  The Gauge Layer
│
├── Chapter 6: The Subatomic Scale: Electroweak and Higgs Sectors    [ch:electroweak_higgs, ~313 lines]
│   ├── 6.1  Reinterpretation of Higgs Mechanism
│   ├── 6.2  Weak Mixing Angle
│   ├── 6.3  W and Z Boson Masses
│   ├── 6.4  W and Z Bosons as Dielectric Plasma Arcs
│   ├── 6.5  Three-Generation Lepton Spectrum
│   ├── 6.6  Neutrino Mass Spectrum
│   ├── 6.7  Schwinger's Anomalous Magnetic Moment
│   └── 6.8  Standard Model / AVE Translation Table                  [sec:sm_ave_translation]
│         [input: ../common/translation_particle_physics.tex]
│
├── Chapter 7: Quantum Mechanics and Atomic Orbitals                 [ch:quantum_orbitals, ~3600+ lines]
│   ├── 7.1  Deterministic Reinterpretation of the Wavefunction
│   ├── 7.2  Orbitals as Acoustic Resonant Cavities
│   ├── 7.3  Hydrogen Energy Levels
│   │   └── 7.3.1  ODE Orbital Verification                         [sec:ode_orbital_verification]
│   ├── 7.4  Helium: Symmetric Cavity Approach                       [sec:helium_symmetric_cavity]
│   ├── 7.5  Quantum Mechanics / AVE Translation Table               [sec:qm_ave_translation]
│   │         [input: ../common/translation_qm.tex]
│   ├── 7.6  Atom as an Analog Ladder Filter                         [sec:analog_ladder_filter]
│   ├── 7.7  Radial TL Eigenvalue                                    [sec:radial_tl_eigenvalue]
│   ├── 7.8  Macro-Cavity Saturation                                 [sec:macro_cavity_saturation]
│   ├── 7.9  p-Shell Isomorphism
│   ├── 7.10 Scale Separation: Knot Topology vs Orbital Geometry     [sec:scale_separation]
│   ├── 7.11 Phase 5: Sub-Shell Junction Scattering                  [sec:lattice_js2]
│   ├── 7.12 Helium Coupling from First Principles
│   └── 7.13 Geometry Pipeline                                       [sec:geometry_pipeline]
│
├── Chapter 8: The Planck Scale and String Theory                    [ch:string_theory, ~103 lines]
│   ├── 8.1  The Dimensionality Crisis
│   ├── 8.2  String Tension as Mutual Inductance
│   ├── 8.3  Why Extra Dimensions Are Unnecessary
│   └── 8.4  Topological Resonance vs Closed Strings
│
├── Chapter 9: Computational Proof and Anomaly Catalog               [ch:computational_proof, ~243 lines]
│   ├── 9.1  Computational Proof of Scale Invariance
│   ├── 9.2  Verification Summary
│   ├── 9.3  Anomaly Catalog                                         [sec:anomaly_catalog]
│   │   ├── 9.3.1  Tier 2 Anomalies
│   │   ├── 9.3.2  Tier 3 Anomalies
│   │   └── 9.3.3  Tier 4 Anomalies
│   ├── 9.4  Numerical Precision Policy                              [sec:precision_policy]
│   └── 9.5  Avoidance of Methodological Contamination              [sec:methodological_contamination]
│
├── Chapter 10: Three Open Problems from Lattice Topology            [ch:open_problems, ~393 lines]
│   ├── 10.1 Strong CP Problem                                       [sec:strong_cp]
│   ├── 10.2 Baryon Asymmetry                                        [sec:baryon_asymmetry]
│   ├── 10.3 Hubble Tension                                          [sec:hubble_tension]
│   ├── 10.4 Testable Prediction g*=85.75                            [sec:g_star_prediction]
│   ├── 10.5 Scale Invariance Principle                              [sec:scale_invariance]
│   └── 10.6 Quantitative Resolutions                                [sec:open_problems_resolutions]
│
├── Chapter 11: The Standard Model Overdrive                         [ch:overdrive, ~127 lines]
│   ├── 11.1 Universal Energy Functional                             [eq:universal_energy]
│   ├── 11.2 Overdriving Lattice QCD                                 [sec:overdrive_nuclear]
│   ├── 11.3 Overdriving AlphaFold                                   [sec:overdrive_protein]
│   └── 11.4 Computational Scaling Comparison                        [tab:overdrive_comparison]
│
├── Chapter 12: Mathematical Limits and the Millennium Prizes        [ch:millennium_prizes, ~679 lines]
│   ├── 12.1 Navier-Stokes Existence and Smoothness                  [sec:ns_millennium]
│   ├── 12.2 Yang-Mills and the Mass Gap                             [sec:ym_millennium]
│   ├── 12.3 The Riemann Hypothesis                                  [sec:rh_millennium]
│   ├── 12.4 The Hodge Conjecture                                    [sec:hc_millennium]
│   ├── 12.5 The BSD Conjecture                                      [sec:bsd_millennium]
│   ├── 12.6 P vs NP                                                 [sec:pnp_millennium]
│   ├── 12.7 The Poincaré Conjecture                                 [sec:poincare_millennium]
│   └── 12.8 Synthesis                                               [sec:millennium_synthesis]
│
└── [backmatter]
      Appendix A: Translation Matrix                                  [app:translation_matrix]
        [inputs 8 common translation tables]
      Appendix B: Resolving Physical Paradoxes                        [app:resolving_paradoxes]
      Appendix C: Summary of Exact Analytical Derivations             [no label]
      Appendix D: Computational Graph Architecture                    [app:computational_graph]
      Appendix E: Discrete Chiral LC Vacuum Electrodynamics           [app:dcve]
      [input: ../common/appendix_experiments.tex — SHARED CROSS-VOLUME]
      Appendix F: Universal Solver Toolchain                          [app:solver_toolchain]
        [from backmatter/05_universal_solver_toolchain.tex]
```

---

## 2. Content Inventory

### Environment counts (across all 12 chapters + backmatter)

| Environment | Count (approx) | Notes |
|---|---:|---|
| `resultbox` | 40+ | Primary named-result vehicle; no `\label` keys |
| `examplebox` | 14 | One per chapter on average; auto-numbered |
| `summarybox` | 12 | One per chapter (end-of-chapter) |
| `exercisebox` | 12 | One per chapter (end-of-chapter, 2 exercises each) |
| `objectivebox` | 12 | One per chapter (opening) |
| `axiombox/axiom` | 3–5 | Concentrated in early chapters and ch:overdrive |
| `simbox` | 2–4 | Computational module results; auto-numbered |
| `circuitbox` | 2–4 | Circuit schematic illustrations |
| `codebox` | 1–3 | SPICE netlists / code blocks |
| `theorem` | 0 | Defined but not used in body chapters |
| `definition` | 0 | Defined but not used in body chapters |
| `lemma` | 0 | Defined but not used in body chapters |

### Named equation labels (`\label{eq:...}`)

| Label | Location | Content |
|---|---|---|
| `eq:dynamic_capacitance_yield` | ch:topological_matter (ch.1) | Dynamic capacitance formula |
| `eq:torus_knot_ladder` | ch:baryons (ch.2) | Torus knot energy ladder |
| `eq:chiral_threshold` | ch:neutrino_sector (ch.3) | Chiral screening threshold |
| `eq:theta12_leading` | ch:neutrino_sector (ch.3) | PMNS theta_12 mixing angle |
| `eq:theta23_leading` | ch:neutrino_sector (ch.3) | PMNS theta_23 mixing angle |
| `eq:theta13` | ch:neutrino_sector (ch.3) | PMNS theta_13 mixing angle |
| `eq:pmns_13`, `eq:pmns_12`, `eq:pmns_23` | ch:neutrino_sector (ch.3) | PMNS matrix elements |
| `eq:delta_cp_pmns` | ch:neutrino_sector (ch.3) | CP-violation phase in PMNS |
| `eq:muon_twist_angle` | ch:electroweak_higgs (ch.6) | Muon topological twist angle |
| `eq:de_broglie_n` | ch:quantum_orbitals (ch.7) | de Broglie standing-wave condition |
| `eq:screening_rule` | ch:quantum_orbitals (ch.7) | Orbital screening rule |
| `eq:bonding_mode` | ch:quantum_orbitals (ch.7) | Bonding mode equation |
| `eq:omega_bond_derived` | ch:quantum_orbitals (ch.7) | Derived bonding frequency |
| `eq:universal_energy` | ch:overdrive (ch.11) | Universal Faddeev-Skyrme energy functional |
| `eq:eta_baryon` | ch:open_problems (ch.10) | Baryon asymmetry eta |
| `eq:g_star_ave` | ch:open_problems (ch.10) | g* prediction from AVE |
| `eq:delta_cp` | ch:open_problems (ch.10) | CP violation phase |
| `eq:lattice_ns` | ch:millennium_prizes (ch.12) | Lattice Navier-Stokes form |
| `eq:laplacian_norm` | ch:millennium_prizes (ch.12) | Laplacian norm bound |
| `eq:enstrophy_bound` | ch:millennium_prizes (ch.12) | Enstrophy saturation bound |
| `eq:lattice_dispersion` | ch:millennium_prizes (ch.12) | Lattice dispersion relation |
| `eq:bogomolnyi_bound` | ch:millennium_prizes (ch.12) | Bogomolny energy bound [DUPLICATE label] |
| `eq:gauge_rank` | ch:millennium_prizes (ch.12) | Gauge group rank |
| `eq:confinement_radius` | ch:millennium_prizes (ch.12) | Confinement radius |
| `eq:confinement_gamma` | ch:millennium_prizes (ch.12) | Confinement decay exponent |

### Named table labels

| Label | Location | Content |
|---|---|---|
| `tab:overdrive_comparison` | ch:overdrive (ch.11) | Computational scaling comparison |
| `tab:knot_vs_orbital` | ch:quantum_orbitals (ch.7) | Knot vs orbital mapping table |
| `tab:knot_vs_orbital` | ch:millennium_prizes (ch.12) | DUPLICATE — same label reused |
| `tab:scale_invariance` | ch:open_problems (ch.10) | Scale invariance summary table |
| `tab:operator_domain` | ch:quantum_orbitals (ch.7) | QM vs AVE operator domain table |

### Named figure labels (partial)

ch.1: `fig:electron_3d`, `fig:photon_spin_structure`
ch.2: `fig:borromean_proton_3d`, `fig:thermal_skyrmion`, `fig:mass_oscillator`, `fig:torus_knot_spectrum`, `fig:tensor_halo`
ch.3: `fig:chiral_dispersion`, `fig:chiral_parity_violation`
ch.4: `fig:spin_precession`
ch.5: `fig:electroweak_acoustic_modes`
ch.6: `fig:w_boson_spark`, `fig:topology_muon`, `fig:topology_tau`, `fig:topology_neutrino`, `fig:particle_zoo`
ch.7: `fig:hydrogen_orbitals`, `fig:orbital_standing_waves`, `fig:atomic_orbital_standing_waves`
ch.8: `fig:string_lc_mapping`
ch.9: `fig:cross_scale_verification`
ch.10: `fig:hubble_tension`
ch.11: `fig:u235_assembly`, `fig:protein_folding`
ch.12: `fig:navier_stokes`, `fig:lattice_dispersion`, `fig:confinement_gamma`

---

## 3. Notation and Custom Macros

All macros defined in `../structure/commands.tex` (shared across all volumes). All `\providecommand` — safe for re-input.

| Macro | Expansion | Meaning |
|---|---|---|
| `\Lvac` | `L_{node}` | Lattice inductance |
| `\Cvac` | `C_{node}` | Lattice capacitance |
| `\Zvac` | `Z_0` | Characteristic impedance |
| `\Wcut` | `\omega_{sat}` | Saturation frequency |
| `\lp` | `l_{node}` | Lattice pitch |
| `\vacuum` | `M_A` | Vacuum (aether mass matrix) |
| `\slew` | `c` | Speed of light |
| `\planck` | `\hbar` | Reduced Planck constant |
| `\permeability` | `\mu_0` | Permeability of free space |
| `\permittivity` | `\epsilon_0` | Permittivity of free space |
| `\impedance` | `Z_0` | Impedance of free space |

`\citestart{}` and `\citeend{}` are defined as empty (no-op placeholders). Distillers can ignore them.

`resultbox{Title}` does not support `\label` — 40+ key results are not cross-referenceable by label. Taxonomy architect must identify results by title string and source line range.

---

## 4. Cross-References to Other Volumes

### Dangling `\ref{}` targets

| Reference | Used in | Status |
|---|---|---|
| `ch:mass_gap` | ch:open_problems (ch.10) | Not defined in vol_2; stale ref — see Anomaly A6 |
| `ch:navier_stokes` | ch:open_problems, ch:computational_proof | Not defined in vol_2; ch.12 covers under `sec:ns_millennium` — see Anomaly A6 |
| `app:full_derivation_chain` | ch:neutrino_sector, backmatter/05 | Not in vol_2 backmatter — see Anomaly A5 |
| `ch:quantum_mechanics_and_orbitals` | ch:computational_proof (ch.9) | Internal typo; actual label is `ch:quantum_orbitals` — see Anomaly A7 |

### Cross-volume references (prose)

| Reference | Used in | Notes |
|---|---|---|
| `ch:network_solver` (Volume V) | ch:quantum_orbitals (ch.7) | Referenced as "Vol~V, Chapter on Network Solver" |
| **Volume V** | ch.11 (AlphaFold overdrive) | Protein biology / network solver |

### `\cite{}` calls

| Cite key | Used in |
|---|---|
| `codata2018` | ch:baryons (ch.2), ch:electroweak_higgs (ch.6) |
| `pdg2022` | ch:baryons (ch.2), ch:electroweak_higgs (ch.6) |

### Shared `\input{}` files

| File | In |
|---|---|
| `../common/translation_particle_physics.tex` | ch:electroweak_higgs (ch.6) |
| `../common/translation_qm.tex` | ch:quantum_orbitals (ch.7) |
| `../common/appendix_experiments.tex` | backmatter/01_appendices.tex |
| `../common/translation_circuit.tex` | App A |
| `../common/translation_gravity.tex` | App A |
| `../common/translation_cosmology.tex` | App A |
| `../common/translation_condensed_matter.tex` | App A |
| `../common/translation_protein.tex` | App A |
| `../common/translation_protein_solver.tex` | App A |

---

## 5. Key Concept List

**Particle physics / subatomic structure:** Topological matter / topological defects as particles, Fermion generations (torus knot ladder), Electron as fundamental unknot ($0_1$), Newtonian inertia as macroscopic Lenz's Law, Regime classification of topological matter, Chirality and antimatter disintegration, Borromean confinement (baryons), Proton mass (dynamic tensor deficit), Topological fractionalization (fractional quark charges), Thermal softening and deconfinement transition, Baryon resonance spectrum, Neutron decay, Helium-4 nucleus, Chiral unknot (neutrino topology), Neutrino mass without charge, Chiral exclusion principle, Neutrino mass eigenvalue, Neutrino oscillation, PMNS mixing angles, CP-violation phase, Quantum spin as gyroscopic precession, Larmor precession via topological gyroscopes, Electroweak mechanics as acoustic modes, Gauge symmetry as topological phase gradient, Higgs mechanism reinterpretation, Weak mixing angle derivation, W and Z boson masses as dielectric plasma arcs, Three-generation lepton spectrum, Schwinger anomalous magnetic moment

**Quantum mechanics / atomic structure:** Deterministic reinterpretation of wavefunction, Orbitals as acoustic resonant cavities, Hydrogen energy levels, Helium symmetric cavity approach, Atom as analog ladder filter, Radial transmission-line eigenvalue, Macro-cavity saturation, p-Shell isomorphism, Scale separation: knot topology vs orbital geometry, Sub-shell junction scattering, de Broglie standing-wave condition, Orbital screening rule

**Planck scale / string theory:** String tension as mutual inductance, Extra dimensions as unnecessary, Topological resonance vs closed strings

**Validation / computation:** Computational proof of scale invariance, Anomaly catalog (Tiers 2–4), Numerical precision policy, Methodological contamination avoidance

**Open problems / cosmology:** Strong CP problem resolution, Baryon asymmetry resolution, Hubble tension resolution, Testable prediction g*=85.75, Scale invariance principle

**Standard model overdrive:** Universal Faddeev-Skyrme energy functional, Overdriving Lattice QCD, Overdriving AlphaFold protein folding

**Millennium prize problems:** Navier-Stokes (lattice enstrophy bound), Yang-Mills mass gap (Bogomolny bound), Riemann Hypothesis (zeta zeros as dispersion poles), Hodge Conjecture, BSD Conjecture, P vs NP, Poincaré Conjecture

**Translation / cross-domain mapping:** SM / AVE, QM / AVE, Circuit / AVE, Gravity / AVE, Cosmology / AVE, Condensed matter / AVE, Protein / AVE translation tables

**Backmatter:** Resolving spin-1/2 paradox, Holographic information paradox, Peierls-Nabarro friction paradox, Discrete Chiral LC Vacuum Electrodynamics, Universal Solver Toolchain, Cross-scale isomorphism (BH QNM, electron, nuclear, protein, antenna, tokamak, BLDC motor)

---

## 6. Estimated Leaf Document Count: ~125–135

| Source region | Estimated leaves |
|---|---|
| Ch.1 Topological Matter | 6 |
| Ch.2 Baryon Sector | 10 |
| Ch.3 Neutrino Sector | 8 |
| Ch.4 Quantum Spin | 3 |
| Ch.5 Electroweak Mechanics | 5 |
| Ch.6 Electroweak + Higgs | 9 |
| Ch.7 Quantum Mechanics + Orbitals | 25–30 |
| Ch.8 Planck Scale / String Theory | 4 |
| Ch.9 Computational Proof | 6 |
| Ch.10 Open Problems | 8 |
| Ch.11 Standard Model Overdrive | 5 |
| Ch.12 Millennium Prizes | 14 |
| App A Translation Tables | 8 |
| App B Paradox Resolutions | 3 |
| App D Computational Graph | 2 |
| App E Discrete Chiral LC Vacuum | 3 |
| App F Universal Solver Toolchain | 6 |
| **Total** | **~125–135** |

Ch.7 dominates due to its ~3600-line size. Its 25–30 leaf estimate may need upward revision once the taxonomy skeleton is finalized.

---

## 7. Anomalies

**A1. Chapter 7 anomalously large (~3600 lines).** All other chapters range from ~82 to ~679 lines. Ch.7 is approximately 10× larger than the next-largest chapter. It contains ~80+ labelled equations, multiple simulation pipeline subsections, and internal `%%` comment blocks documenting "QM contamination audits." Likely needs to be split into multiple KB subtopics rather than mapped as a single chapter-level node.

**A2. Duplicate subsection title in Chapter 2.** `\subsection{The Self-Consistent Mass Oscillator (The Structural Eigenvalue)}` appears twice in `02_baryon_sector.tex` (~lines 114 and 166). Neither instance has a `\label`. Both instances have distinct content. Flag for author review.

**A3. Duplicate equation label `eq:bogomolnyi_bound`.** Appears twice in `12_the_millennium_prizes.tex` — once in Yang-Mills section, once in a later derivation. Second definition silently overrides first.

**A4. Duplicate table label `tab:knot_vs_orbital`.** Appears in both `07_quantum_mechanics_and_orbitals.tex` and `12_the_millennium_prizes.tex`. These are distinct tables. Cross-references to this label are ambiguous.

**A5. Dangling reference `app:full_derivation_chain`.** Referenced in ch:neutrino_sector and backmatter/05, but `main.tex` does not include any file defining this label. `backmatter/02_full_derivation_chain.tex` likely exists but is not `\input`-ted by vol_2. Reference is dangling within vol_2.

**A6. Dangling chapter references `ch:mass_gap` and `ch:navier_stokes`.** Both referenced in ch:open_problems (ch.10) as chapter-level peers. Neither label is defined in vol_2. The Navier-Stokes content appears in ch.12 under `sec:ns_millennium` (chapter label `ch:millennium_prizes`). These are likely stale references from an earlier organization where these were standalone chapters before being consolidated into ch.12.

**A7. Internal label mismatch in Chapter 9.** `ch:computational_proof` references `ch:quantum_mechanics_and_orbitals` but the actual chapter label is `ch:quantum_orbitals`. Internal typo.

**A8. `amsthm` environments defined but unused.** `theorem`, `definition`, `lemma` have zero instances in all 12 chapter files. Author uses `resultbox` exclusively for key results.

**A9. File internal numbering discrepancy.** `01_topological_matter.tex` has internal comment `% 05_topological_matter.tex`; `03_neutrino_sector.tex` has `% 07_neutrino_sector.tex`. Stale comments from earlier file naming. `_manifest.tex` ordering is authoritative.

**A10. resultboxes have no `\label` keys.** 40+ key results cannot be cross-referenced by label. Taxonomy architect and distillers must identify results by title string and source line range.
