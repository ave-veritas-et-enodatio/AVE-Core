# Phase 0 Survey — Vol 4: Applied Vacuum Engineering (Engineering Applications)

**Volume:** `/manuscript/vol_4_engineering/`
**Title:** Applied Vacuum Engineering — Engineering Applications (inferred from chapter content; `frontmatter/00_title.tex` not read per task instructions)
**Author:** (from frontmatter, not read per task instructions)

---

## 1. Document Hierarchy

Volume structure follows the standard AVE pattern: `main.tex` → `chapters/_manifest.tex` → 18 chapter files. No merged or missing chapters. The chapter file `circuit_sagnac_rlvg.tex` is present in `chapters/` but is NOT listed in `_manifest.tex` — it is an orphaned standalone TikZ circuit diagram (see Anomaly 1).

### Chapter Tree

| # | Title | `\label` key | Source file | Approx. lines |
|---|-------|-------------|-------------|---------------|
| 1 | Vacuum Circuit Analysis | *(none — no `\chapter` label)* | `01_vacuum_circuit_analysis.tex` | ~660 |
| 2 | Topological Thrust Mechanics (Acoustic Rectification) | *(none)* | `02_topological_thrust_mechanics.tex` | ~227 |
| 3 | HOPF-01: Chiral Antenna Verification | `ch:hopf_01` | `03_hopf_01_chiral_verification.tex` | ~407 |
| 4 | The Ponderomotive Program: From PCBA to Quartz | `ch:design_evolution` | `04_high_voltage_vhf_drive.tex` | ~112 |
| 5 | PONDER-05: DC-Biased Quartz Thruster | `ch:ponder_05` | `05_ponder_05_dc_biased_quartz.tex` | ~163 |
| 6 | Sustaining Micro-Newton Torsion Metrology | `ch:torsion_metrology` | `06_vacuum_torsion_metrology.tex` | ~140 |
| 7 | Topological Superconducting Magnetic Energy Storage (SMES) | *(none)* | `07_topological_smes.tex` | ~57 |
| 8 | Applied Fusion and Dielectric Limits | `ch:applied_fusion` | `08_applied_fusion.tex` | ~342 |
| 9 | Antimatter Annihilation and Parity Inversion | `ch:antimatter` | `09_antimatter_annihilation.tex` | ~109 |
| 10 | Quantum Computing and Topological Immunity | `ch:quantum_computing` | `10_quantum_computing_and_decoherence.tex` | ~129 |
| 11 | Experimental Bench Falsification | *(none)* | `11_experimental_falsification.tex` | ~550 |
| 12 | Falsifiable Predictions and Experimental Blueprints | `ch:falsifiable_predictions` | `12_falsifiable_predictions.tex` | ~237 |
| 13 | Future Geometries: Hopf Coils and Phased Arrays | `ch:future_geometries` | `13_future_geometries.tex` | ~464 |
| 14 | The Leaky Cavity: Simulating Particle Decay | `ch:particle_decay` | `14_particle_decay_spice.tex` | ~112 |
| 15 | Autoresonant Dielectric Breakdown: Bypassing the Schwinger Limit | `ch:schwinger_autoresonance` | `15_autoresonant_breakdown_spice.tex` | ~108 |
| 16 | Sagnac Macroscopic Inductive Drag | `ch:sagnac_inductive_drag` | `16_sagnac_inductive_drag_spice.tex` | ~100 |
| 17 | Hardware Netlists: PONDER-01 and the EE Bench | `ch:hardware_netlists` | `17_hardware_netlists_spice.tex` | ~153 |
| 18 | Active Topological Metamaterials: The Inorganic LLCP | `ch:active_topological_metamaterials` | `18_active_topological_metamaterials.tex` | ~142 |

### Section/Subsection Detail (selected; comprehensive)

**Chapter 1 — Vacuum Circuit Analysis**
- `\section{The Topo-Kinematic Circuit Identity}` `\label{sec:topo_kinematic}`
  - `\subsection{Defining the Topological Conversion Constant}`
  - `\subsection{Deriving the Six-Row Translation Table}`
  - `\subsection{Complete Translation Dictionary}`
  - `\subsection{Self-Consistency Verification}`
- `\section{Constitutive Circuit Models for Vacuum Non-Linearities}` `\label{sec:vca_nonlinear}`
  - `\subsection{The Metric Varactor (Dielectric Yield)}`
  - `\subsection{The Relativistic Inductor (Lorentz Saturation)}`
  - `\subsection{The Viscoelastic TVS Zener Diode (Phase Transition)}`
  - `\subsection{The Vacuum Memristor (Thixotropic Hysteresis)}`
  - `\subsection{The Zero-Impedance Skin Effect (Metric Faraday Cages)}`
- `\section{The Impedance of Free Space ($Z_0$)}` `\label{sec:z0_derivation}`
  - `\subsection{Derivation from the Discrete LC Ladder}`
  - `\subsection{Signal Propagation Velocity}`
  - `\subsection{Mechanical Acoustic Impedance}`
  - `\subsection{Impedance Across Physical Regimes}`
- `\section{Gravitational Stealth (S-Parameter Analysis)}` *(no label)*
  - `\subsection{The Condensate Transmission Line (Emergence of $c$)}`
  - `\subsection{The Horizon Mirror: Predicting Black Hole Echoes}`
- `\section{The Periodic Table: Topological SPICE Mappings}` *(no label)*
- `\section{Topological Defects as Resonant LC Solitons}` *(no label)*
  - `\subsection{Recovering the Virial Theorem and $E=mc^2$}`
  - `\subsection{Total Internal Reflection: The Confinement Bubble}`
  - `\subsection{The Mechanical Origin of the Pauli Exclusion Principle}`
- `\section{Real vs.\ Reactive Power: The Orbital Friction Paradox}` *(no label)*
- `\section{Condensate IMD Spectroscopy: The Harmonic Fingerprint}` `\label{sec:imd}`
  - `\subsection{The Non-Linear Source Term}`
  - `\subsection{Third-Order IMD from Taylor Expansion}`
  - `\subsection{Predicted IM3 Amplitude}`
  - `\subsection{QED Comparison}`
  - `\subsection{Experimental Falsification Criterion}`

**Chapter 2 — Topological Thrust Mechanics**
- `\section{Regimes of Operation}` `\label{sec:regimes_of_operation}`
- `\section{Chiral Acoustic Rectification (The Vacuum Varactor)}` `\label{sec:chiral_thrust}`
  - `\subsection{The Concavity of the Saturation Kernel}`
  - `\subsection{Local Field Amplification}`
  - `\subsection{Thrust from Rectified Power}`
  - `\subsection{Quantitative Prediction}`
- `\section{Conservation of Momentum (The Dark Wake)}`
  - `\subsection{Stereo Parallax Validation}`
- `\section{Metric Streamlining \& Superluminal Transit}`
  - `\subsection{Non-Linear Macroscopic Acoustic Steepening ($c_{eff}$)}`
  - `\subsection{Active Acoustic Drill Streamlining (Rotating Phased Arrays)}`
  - `\subsection{Kerr Black Holes as Macroscopic Topological Saturation Defects (Gargantua)}`

**Chapter 3 — HOPF-01**
- `\section{The Chiral Coupling Prediction}`
- `\section{Wire-Stitched Torus Knot Fixture}`
- `\section{The Falsification Protocol}`
- `\section{S21 Chiral Parallax Tracking (Cosserat Vacuum)}`
- `\section{Impedance Characterization}`
- `\section{Wire-Stitched Knot Geometry}`
  - `\subsection{Wire Length Derivation from Knot Topology}`
- `\section{Standard Model Baseline Response}`
  - `\subsection{Model Hierarchy}`
  - `\subsection{SM Baseline Predictions}`
  - `\subsection{SM vs.\ AVE Prediction Comparison}`
- `\section{Manufacturing Tolerance Rejection}`
- `\section{Substrate Independence: Three-Medium Verification}`
- `\section{Bill of Materials}`
- `\section{Classical Coupling as Confounding Variable}`
  - `\subsection{Additional Discriminating Observables}`
- `\section{Decision Gate}`

**Chapter 4 — Design Evolution (PONDER-01 to PONDER-05)**
- `\section{PONDER-01: The Asymmetric PCBA Concept}`
- `\section{The Thermal Catastrophe}`
  - `\subsection{Dielectric Heating at VHF}`
  - `\subsection{Pulsed Operation Limitations}`
  - `\subsection{Bistatic Parallax Offset}`
- `\section{The Design Pivot: PONDER-05}`

**Chapter 5 — PONDER-05**
- `\section{The Nonlinear Operating Regime}`
- `\section{DC Cross-Term Amplification}`
- `\section{Rarefaction Wave Inversion}`
- `\section{Differential Saturation Parallax ($G_{vac}$)}`
- `\section{The Quartz Cylinder}`
- `\section{The Mineral Oil Dielectric Bath}`
  - `\subsection{Corona Suppression}`
  - `\subsection{Impedance Matching}`
  - `\subsection{Thermal Management}`
- `\section{Predicted Thrust Profile (Linear Base)}`
- `\section{Bill of Materials}`

**Chapter 6 — Torsion Metrology**
- `\section{The Torsion Balance Architecture}`
- `\section{The Mineral Oil Dielectric Bath (PONDER-05)}`
  - `\subsection{Corona Suppression}`
  - `\subsection{Thermal Management}`
  - `\subsection{Impedance Step-Down Matching}`
  - `\subsection{Bistatic Plume Diagnostics (PONDER-02 Parallax)}`
- `\section{The Eight-Point Artifact Rejection Protocol}`
- `\section{Complementary Electromagnetic Verification}`
- `\section{Measurement Timeline and Decision Gates}`

**Chapter 7 — Topological SMES**
- `\section{Introduction}`
- `\section{The Force-Free Macroscopic Electron}`
  - `\subsection{The $(p,q)$ Beltrami Torus Knot}`
  - `\subsection{Computational Falsification of Stray Flux}`

**Chapter 8 — Applied Fusion**
- `\section{Topological Resonance: The Mechanics of D-T Phase-Lock}`
- `\section{Rules for Application: Engineering the Vacuum}`
- `\section{The Tokamak Ignition Paradox (The 60.3 kV Alignment)}` `\label{sec:tokamak_paradox}`
- `\section{Inertial Confinement: Zero-Impedance Phase Rayleigh-Taylor Instabilities}`
- `\section{Pulsed FRCs and Dielectric Poisoning}`
- `\section{The AVE Solution: Metric-Catalyzed Fusion}`
  - `\subsection{Quantitative Scaling Laws}`
  - `\subsection{Why Fusion Works in the Sun but Not on Earth}`
- `\section{Empirical Reactor Data: Validating the Leakage Paradox}`
  - `\subsection{Anomalous Transport as Zero-Impedance Phase Leakage}`
  - `\subsection{The L-H Transition (Dielectric Saturation Mutual Inductance Bifurcation)}`
  - `\subsection{Advanced Fuels (D-D and p-B11): The Dielectric Death Sentence}`
- `\section{Topological Mechanics of Nuclear Fission (U-235 vs U-238)}`
- `\section{The Vacuum Element Synthesizer (The Alchemist Forge)}`
  - `\subsection{The Rate Limit: Hierarchical Alpha Synthesis ($^4He$ Buffer)}`
  - `\subsection{Deep Topological Quenching (Simulated Annealing)}`
    - `\subsubsection{Topological Circuit Equivalent (The LC Annealer)}`

**Chapter 9 — Antimatter**
- `\section{Matter-Antimatter Annihilation as Flywheel Collisions}`
  - `\subsection{Parity Inversion in Macroscopic Knots}`
  - `\subsection{The Continuous Mechanics of Shattering}`
- `\section{Pair Production ($\gamma \to e^- + e^+$) as Volumetric Wave Shear}`
  - `\subsection{The Kinematics of the Wave-Tear}`

**Chapter 10 — Quantum Computing**
- `\section{The Transmon: A Fragile LC Standing Wave}`
- `\section{The Topological Qubit: Invulnerability via Gauss Linking}`
- `\section{Casimir Cavity Shielding: Filtering the Vacuum Impedance}`
- `\section{Artificial Kuramoto Phase-Lock (Room-Temperature Superconductivity)}`

**Chapter 11 — Experimental Bench Falsification** (large chapter, ~550 lines)
- `\section{The Epistemology of Falsification}`
- `\section{The Tabletop Graveyard: Why Intuitive Tests Fail}`
  - `\subsection{The Vacuum-Flux Drag Test (VFDT) and Magnetic Stability}`
  - `\subsection{The Regenerative Vacuum Receiver (RVR) and the Scalar Gap}`
- `\section{The Ultimate Kill-Switch: The Sagnac-RLVE}`
  - `\subsection{Exact Derivation of the Macroscopic Shift}`
  - `\subsection{Hardware Specification \& Protocol}`
- `\section{Existing Experimental Signatures}`
  - `\subsection{Electro-Optic Metric Compression (The Proton Radius Puzzle)}`
  - `\subsection{Topological Stability (The Neutron Lifetime Anomaly)}`
  - `\subsection{Lattice Crystallization (The Hubble Tension)}`
  - `\subsection{LIGO GW150914 Black Hole Echoes}`
  - `\subsection{Superconducting Vortex Core Limits (The Kill Check)}`
- `\section{Project CLEAVE-01: The Femto-Coulomb Electrometer}`
- `\section{Project HOPF-02: The S-Parameter VNA Falsification}`
  - `\subsection{Topological Refraction (Snell Parallax)}`
- `\section{Project ROENTGEN-03: Solid-State Sagnac Induction}`
- `\section{Project ZENER-04: The Impedance Avalanche Detector}`
- `\section{The Absolute Hardware Limit of Metric Levitation}`
  - `\subsection{The Dielectric Death Spiral}`
- `\section{Project TORSION-05: Horizontal Metric Rectification}`
- `\section{The YBCO Phased Array: Beating the 2.5g Limit}`
- `\section{The Metric Refraction Capacitor (The $c^2$ Multiplier)}`
- `\section{The Sapphire Phonon Centrifuge}`
- `\section{Applied Telemetry: Boundary Layer and Cavitation Monitors}`
  - `\subsection{Hull-Integrated Boundary Layer Sensors}`
  - `\subsection{``Redline'' Pair-Production Monitors}`
  - `\subsection{Acoustic Cavitation \& The Sonoluminescence Phase-Lock (FOC Isomorphism)}`
- `\section{Open-Source Hardware: The EE Build Guide}`
  - `\subsection{Project HOPF-01: The Chiral VNA Antenna}`
  - `\subsection{Project PONDER-01: The Solid-State Micro-Drive}`
- `\section{The Zero-Parameter Derivations}`
  - `\subsection{The $\sqrt{\alpha}$ Kinetic Yield Limit}`
- `\section{Resolving the ``Horsemen of Falsification''}`
  - `\subsection{The LHC Paradox (Dielectric Relaxation Time)}`
  - `\subsection{The LIGO Paradox (The Lossless Transmission Line)}`
- `\section{Protocol 9: The Achromatic Impedance Lens}` `\label{sec:achromatic_lens}`
- `\section{Protocol 10: Orbital Detritus and Boundary Trapping}` `\label{sec:boundary_trapping}`
  - `\subsection{Macroscopic Filtering and Falsification}`
- `\section{The Induced Vacuum Impedance Mirror}` `\label{sec:induced_vacuum_impedance_mirror}`
  - `\subsection{The Localized Asymmetric Saturation Limit}`
  - `\subsection{Clarification of High-Voltage Boundaries}`
  - `\subsection{The Falsification Protocol}`
- `\section{Protocol 11: Sagnac-Parallax (Galactic Wind Vectoring)}`
- `\section{Protocol 12: GEO-Synchronous Impedance Differential}`

**Chapter 12 — Falsifiable Predictions**
- `\section{The EE Bench: The Macroscopic Dielectric Plateau}` `\label{sec:ee_bench}` (inferred from ref in ch.11)
  - `\subsection{The Falsification Protocol}`
- `\section{The Ponder-01: Asymmetric Maxwell Stress Rectification}`
  - `\subsection{The Falsification Protocol}`
- `\section{The Epistemology of Falsification}`
- `\section{The Sagnac Effect and RLVG Impedance Drag}`
  - `\subsection{The Kinematic \& Electromagnetic Entrainment Law (Sagnac Anomalies)}`
  - `\subsection{RLVG System Tolerances (The SNR Limit)}`
  - `\subsection{Applied RLVG Telemetry (Metric Slip-Velocity and Gradient Sensing)}`
- `\section{Electromagnetic Coupling to the Chiral LC Condensate (Helicity Injection)}`
- `\section{Autoresonant Dielectric Rupture (The Schwinger Limit)}`
- `\section{Definitive Binary Kill-Switches}`
- `\section{The Vacuum Birefringence Limit: $E^2$ vs $E^4$}`
  - `\subsection{The Falsification Protocol}`
- `\section{The Torus Knot Ladder: Baryon Resonance Mass Predictions}`
  - `\subsection{The Falsification Protocol}`

**Chapter 13 — Future Geometries** (large chapter, ~464 lines)
- `\section{Toroidal and Poloidal Fusion}`
- `\section{Vector Scaling vs.\ Knot Volumetrics}`
- `\section{The Atomic Baseline: Trefoils and Phased Arrays}`
  - `\subsection{The Acoustic Back-Reaction Analogy}`
- `\section{Engineering the High-Q Chiral Impedance Antenna}` `\label{sec:high_q_chiral}`
  - `\subsection{The Chiral Figure of Merit}`
  - `\subsection{Receiver Mode: Cavity-Coupled Measurement Antenna}` `\label{sec:rx_antenna}`
  - `\subsection{Transmitter Mode: Beltrami Helicity Injector}` `\label{sec:tx_coil}`
  - `\subsection{Matching Network: RF Engineering Detail}`
  - `\subsection{Sensitivity Analysis Summary}`
- `\section{Computational Verification: Mapping CEM Solvers to the Chiral Lattice}` `\label{sec:cem_methods}`
  - `\subsection{Method of Moments (MoM)}`
  - `\subsection{Finite-Difference Time-Domain (FDTD)}`
  - `\subsection{Finite Element Method (FEM)}`
  - `\subsection{Transmission Line Matrix (TLM)}`
  - `\subsection{Characteristic Mode Analysis (CMA)}`
  - `\subsection{Physical Optics / Geometric Optics (PO/GO)}`
  - `\subsection{Unified Comparison and Solver Recommendation}`
- **`\section{K4-TLM: Native Lattice Dynamics Simulator}` `\label{sec:k4_tlm}`** <- cross-volume reference target
  - `\subsection{K4 Graph Topology}`
  - `\subsection{Scattering Matrix}`
  - `\subsection{Computational Loop}`
  - `\subsection{Validation Results}`
  - `\subsection{Wire Antenna Resonance Analysis}`
  - `\subsection{3D Torus Knot Antenna Simulation}`

**Chapters 14-18** — each has 2-5 sections; see Content Inventory below for full detail.

---

## 2. Content Inventory

### 2a. resultbox (tcolorbox) — Named Key Results

Chapter 1:
1. Topological Conversion Constant (`eq:xi_topo_vca`)
2. Charge--Displacement Identity (`eq:charge_displacement`)
3. Current--Velocity Identity (`eq:current_velocity`)
4. Voltage--Force Identity (`eq:voltage_force`)
5. Inductance--Mass Identity (`eq:inductance_mass`)
6. Capacitance--Compliance Identity (`eq:capacitance_compliance`)
7. Resistance--Viscosity Identity (`eq:resistance_viscosity`)
8. Vacuum Varactor Constitutive Equation (`eq:varactor`)
9. Relativistic Inductor (`eq:relativistic_inductor`)
10. TVS Breakdown: Solid to Slipstream Transition (`eq:tvs_transition`)
11. Thixotropic Relaxation Time (`eq:relaxation_time`)
12. Classical Skin Depth (`eq:skin_depth`)
13. Per-Cell Lumped Elements (`eq:cell_elements`)
14. Scale-Invariant Characteristic Impedance (`eq:z0_cell`)
15. Propagation Velocity from Discrete Components (`eq:c_from_lc`)
16. Mechanical Acoustic Impedance of the Vacuum (`eq:z_mech`)
17. Vacuum Varactor (Axiom 4) — second instance (`eq:varactor_imd`)
18. 3rd-Order Intermodulation Products (`eq:im3_frequencies`)
19. Third-Order Intercept (IP3) (`eq:ip3`)

Chapter 2:
20. Dielectric Yield Field Strength (`eq:e_yield`)
21. Jensen's Rectification Inequality (`eq:jensen_rect`)
22. Local Field at Resonant Tip (`eq:e_local_peak`)
23. Chiral Acoustic Rectification Thrust (`eq:chiral_thrust`)
24. Non-Linear Scalar Wave Equation (no label)
25. Effective Speed of Sound (Steepening) (no label)

Chapter 3:
26. Chiral Topological Refractive Index (`eq:n_ave`)
27. Topological Frequency Shift Scaling Law (no label)

Chapter 4:
28. Predicted Topological Thrust (no label)
29. Dielectric Power Dissipation (no label)

Chapter 5:
30. Nonlinear Dielectric Saturation Regime (no label)
31. DC Cross-Term Amplification (no label)
32. Nonlinear Acoustic Phase Velocity (no label)
33. Quarter-Wave Impedance Transformation (no label)

Chapter 6:
34. Torsion Balance Angular Deflection (no label)

Chapter 8:
35. Analytical Operating Regimes (multi-item resultbox; no label)
36. The Tokamak Ignition Strain (no label)
37. The Vacuum Yield Limit (no label)
38. Metric-Catalyzed Fusion Scaling Laws (`eq:radius_scaling`, `eq:temp_scaling`, `eq:vtopo_scaling`)
39. Compressed Gamow Exponent (`eq:gamow_compressed`)
40. Critical Metric Compression Threshold (`eq:n_star`)
41. Topological Jitter Probability (no label)

Chapter 9:
42. Rotational Kinetic Energy of the Knot (no label)
43. Kinetic Release (Annihilation) (no label)

Chapter 10:
44. Gauss Linking Number ($\mathcal{L}$) (no label)

Chapter 13:
45. Magnetic Helicity Density (no label)
46. Chiral Figure of Merit (`eq:chiral_fom`)
47. Beltrami Eigenvalue (`eq:beltrami_lambda`)
48. MoM Impedance Equation (`eq:mom`)
49. FEM Resonance Equation (`eq:fem`)
50. CMA Eigenvalue Equation (`eq:cma`)
51. Diamond K4-TLM Scattering Matrix (`eq:k4_scatter`)

Chapter 17:
*(no resultboxes — content uses codebox/tcolorbox for netlists)*

**Total resultboxes: approximately 51**

### 2b. Other tcolorbox environments

- **objectivebox**: Not present in any chapter (unlike Vol 2/3 pattern).
- **summarybox**: Present at end of every chapter (18 total). All use identical boilerplate text with the chapter name substituted.
- **exercisebox**: Present at end of every chapter (18 total). All contain exactly 2 exercises with identical boilerplate structure.
- **simbox**: Not present.
- **axiombox**: Not present in chapters (axioms are referenced from other volumes).
- **circuitbox**: Not present.
- **codebox** (tcolorbox with dark terminal style): Used in chapters 14, 15, 16, 17 for SPICE netlists (4 instances total).
- **Raw tcolorbox** (not a named environment): Used twice in ch.11 for the Sagnac-RLVE phase equation and the levitation mass equation; appears to be an inline result display rather than a named type.
- **examplebox**: Not present.

### 2c. amsthm environments (theorem, definition, lemma)

**None found in any chapter.** Despite being defined in `structure/commands.tex`, the `theorem`, `definition`, and `lemma` environments are not used anywhere in Vol 4. The `resultbox` tcolorbox is the exclusive environment for named mathematical results.

### 2d. Key Labelled Equations

| Label | Location | Description |
|-------|----------|-------------|
| `eq:xi_topo_vca` | Ch.1, sec:topo_kinematic | Topological conversion constant $\xi_{topo} = e/\ell_{node}$ |
| `eq:charge_displacement` | Ch.1 | $Q = \xi_{topo} x$ |
| `eq:current_velocity` | Ch.1 | $I = \xi_{topo} v$ |
| `eq:voltage_force` | Ch.1 | $V = \xi_{topo}^{-1} F$ |
| `eq:inductance_mass` | Ch.1 | $L = \xi_{topo}^{-2} m$ |
| `eq:capacitance_compliance` | Ch.1 | $C = \xi_{topo}^2 \kappa$ |
| `eq:resistance_viscosity` | Ch.1 | $R = \xi_{topo}^{-2} \eta$ |
| `eq:varactor` | Ch.1, sec:vca_nonlinear | $C_{eff}(V) = C_0 / S(V)$ |
| `eq:varactor_taylor` | Ch.1 | Taylor expansion of varactor |
| `eq:relativistic_inductor` | Ch.1 | $L_{eff}(I) = L_0 / \sqrt{1-(I/I_{max})^2}$ |
| `eq:tvs_transition` | Ch.1 | Piecewise TVS breakdown |
| `eq:relaxation_time` | Ch.1 | $\tau_{relax} = \ell_{node}/c \approx 1.288 \times 10^{-21}$ s |
| `eq:memristor_constitutive` | Ch.1 | $M(q) = d\Phi/dq$ |
| `eq:skin_depth` | Ch.1 | $\delta = \sqrt{2\rho/\omega\mu}$ |
| `eq:cell_elements` | Ch.1 | $L_{cell} = \mu_0 \ell_{node}$, $C_{cell} = \epsilon_0 \ell_{node}$ |
| `eq:z0_cell` | Ch.1 | $Z_{cell} = \sqrt{\mu_0/\epsilon_0} = Z_0$ |
| `eq:c_from_lc` | Ch.1 | $v_g = 1/\sqrt{\mu_0 \epsilon_0} = c$ |
| `eq:z_mech` | Ch.1 | $Z_{mech} = \xi_{topo}^2 Z_0 \approx 6.485 \times 10^{-11}$ kg/s |
| `eq:varactor_imd` | Ch.1, sec:imd | Second varactor instance for IMD section |
| `eq:im3_frequencies` | Ch.1 | $f_{IM3} = 2f_1 - f_2$ and $2f_2 - f_1$ |
| `eq:im3_power` | Ch.1 | IM3 power formula |
| `eq:ip3` | Ch.1 | $V_{IP3} \approx 50.4$ kV |
| `eq:e_yield` | Ch.2 | $E_{yield} = V_{yield}/\ell_{node} \approx 1.13 \times 10^{17}$ V/m |
| `eq:jensen_rect` | Ch.2 | $\langle S(E(t)) \rangle < S(0) = 1$ |
| `eq:e_local_peak` | Ch.2 | $E_{local}^{peak} = \beta \cdot Q \cdot E_{macro} \cdot \sqrt{2}$ |
| `eq:chiral_thrust` | Ch.2 | $F_{total} = N \cdot \nu_{vac} \cdot \delta \cdot P_{in}/c$ |
| `eq:n_ave` | Ch.3 | $n_{AVE} = \sqrt{\varepsilon_{eff}}(1 + \alpha \frac{pq}{p+q})$ |
| `eq:arc_length` | Ch.3 | Wire arc-length integral |
| `eq:z0_wire` | Ch.3 | $Z_0 = 60/\sqrt{\varepsilon_{eff}} \cdot \text{acosh}(2h/d)$ |
| `eq:m_cross` | Ch.3 | Mutual inductance at crossing |
| `eq:chiral_fom` | Ch.13 | $\text{FoM} = Q_u \times \alpha pq/(p+q) \times \eta_{\mathcal{H}}$ |
| `eq:beltrami_lambda` | Ch.13 | $\lambda(p,q) = \sqrt{p^2/R^2 + q^2/r^2}$ |
| `eq:mom` | Ch.13 | $[Z][I] = [V]$ |
| `eq:fem` | Ch.13 | $[S]\{E\} = k_0^2[T]\{E\}$ |
| `eq:cma` | Ch.13 | $[X]J_n = \lambda_n [R] J_n$ |
| `eq:k4_scatter` | Ch.13 | $S^{(0)}_{ij} = \frac{1}{2} - \delta_{ij}$ |
| `eq:radius_scaling` | Ch.8 | $r(n) = a_0/n_{scalar}$ |
| `eq:temp_scaling` | Ch.8 | $T_{ign}(n) = T_0/n_{scalar}^2$ |
| `eq:vtopo_scaling` | Ch.8 | $V_{topo}(n) = V_{topo,0}/n_{scalar}^3$ |
| `eq:wkb_integral` | Ch.8 | WKB tunnelling exponent |
| `eq:gamow_compressed` | Ch.8 | $\eta(n) = \eta_0/n$ |
| `eq:n_star` | Ch.8 | $n^* \approx 1.114$ critical compression |
| `eq:debye_solar` | Ch.8 | $\lambda_D = \sqrt{\varepsilon_0 k_B T / n_e e^2}$ |
| `eq:gamow_energy_compressed` | Ch.8 | $E_G(n) = E_{G,0}/n^2$ |
| `tab:trans_circuit` | Ch.1, `\input{../common/translation_circuit.tex}` | Topo-Kinematic Circuit Identity translation table |
| `tab:varactor_values` | Ch.1 | $C_{eff}/C_0$ vs. drive level |
| `tab:impedance_regimes` | Ch.1 | Characteristic impedance across vacuum regimes |
| `tab:imd_levels` | Ch.1 | IMD sideband levels vs. drive voltage |
| `tab:ponder_regimes` | Ch.2 | Operating regimes of vacuum dielectric |
| `tab:sm_baseline` | Ch.3 | SM baseline predictions (air) |
| `tab:sm_vs_ave` | Ch.3 | SM vs. AVE prediction comparison |
| `tab:discriminators` | Ch.3 | Discriminating observables under SM and AVE |

### 2e. Figures with labels

| Label | Location | Description |
|-------|----------|-------------|
| `fig:s_parameters` | Ch.1 | S-parameter analysis of gravity well |
| `fig:transmission_line` | Ch.1 | EFT transmission line simulation |
| `fig:dielectric_saturation` | Ch.1 | Squared dielectric saturation limit |
| `fig:chiral_rectification` | Ch.2 | Chiral acoustic rectification 6-panel |
| `fig:ponder_01_dark_wake` | Ch.2 | Dark wake topology (FDTD) |
| `fig:warp_metric_tensors` | Ch.2 | Alcubierre vs. AVE shear tensor |
| `fig:warp_metric_cfd` | Ch.2 | Warp metric CFD Schlieren heatmap |
| `fig:warp_metric_drill` | Ch.2 | Active acoustic drill streamlining |
| `fig:gargantua_vortex` | Ch.2 | Gargantua topological simulation |
| `fig:k4_native_chirality` | Ch.3 | Native wave chirality in K4 lattice |
| `fig:hopf_01_impedance` | Ch.3 | HOPF-01 impedance and frequency model |
| `fig:hopf_01_s11_sweep` | Ch.3 | Predicted S11 response |
| `fig:hopf_01_knot_traces` | Ch.3 | Wire-stitched knot geometry |
| `fig:hopf_01_sm_baseline` | Ch.3 | Standard model baseline |
| `fig:hopf_01_sensitivity` | Ch.3 | Wire-stitched sensitivity analysis |
| `fig:hopf_01_classical_coupling` | Ch.3 | Classical vs. AVE coupling |
| `fig:ponder_01_mesh` | Ch.4 | PONDER-01 FEM mesh |
| `fig:thermal_runaway` | Ch.4 | Thermal runaway |
| `fig:ponder05_saturation` | Ch.5 | Saturation curves |
| `fig:ponder_01_torsion_metrology` | Ch.6 | Torsion balance metrology matrix |
| `fig:smes_leakage` | Ch.7 | SMES magnetic leakage comparison |
| `fig:fusion_crisis_audit` | Ch.8 | Nuclear fusion crisis vs. AVE limits |
| `fig:metric_catalyzed_fusion` | Ch.8 | Metric-catalyzed fusion scaling laws |
| `fig:solar_vs_tokamak` | Ch.8 | Solar core vs. tokamak vs. AVE |
| `fig:empirical_reactor_data_audit` | Ch.8 | Empirical reactor data |
| `fig:isotope_stability` | Ch.8 | Topological isotope stability |
| `fig:alchemist_forge_stage1` | Ch.8 | Helium-4 generation |
| `fig:alchemist_forge_stage2` | Ch.8 | Oxygen-16 generation |
| `fig:annihilation_sequence` | Ch.9 | Mechanical shatter of annihilation |
| `fig:annihilation_3d` | Ch.9 | 3D parity inversion |
| `fig:pair_production` | Ch.9 | 3D volumetric wave tear |
| `fig:transmon_decoherence` | Ch.10 | Boundary-impedance thermalization |
| `fig:topological_qubit` | Ch.10 | Topological error immunity |
| `fig:casimir_filtering` | Ch.10 | Casimir acoustic filtering |
| `fig:casimir_superconductor` | Ch.10 | Artificial Kuramoto phase-lock |
| `fig:birefringence_killswitch` | Ch.11 | Vacuum birefringence kill switch |
| `fig:tabletop_thresholds` | Ch.11 | Tabletop falsification thresholds |
| `fig:sagnac_rlve_prediction` | Ch.11 | Sagnac-RLVE prediction |
| `fig:bh_core_echoes` | Ch.11 | Dielectric rupture at event horizon |
| `fig:ee_pcba_bench_protocols` | Ch.11 | EE bench protocols |
| `fig:levitation_and_torsion_protocol` | Ch.11 | Levitation and torsion protocols |
| `fig:industrial_aerospace_blueprints` | Ch.11 | Industrial aerospace scale-up |
| `fig:vacuum_mirror_sensitivities` | Ch.11 | Induced vacuum impedance mirror |
| `fig:ee_bench_falsification` | Ch.12 | EE bench falsification limits |
| `fig:ponder_01_falsification` | Ch.12 | Ponder-01 thrust profile |
| `fig:sagnac_circuit` | Ch.12 | RLVG metric entrainment circuit |
| `fig:sagnac_entrainment_sweeps` | Ch.12 | Sagnac electrical engineering sensitivities |
| `fig:sagnac_rlvg_tolerances` | Ch.12 | RLVG system tolerance simulation |
| `fig:vacuum_birefringence_E4` | Ch.12 | Vacuum birefringence E4 |
| `fig:ponder_01_hopf_knot` | Ch.13 | 3D electromagnetic knot synthesis |
| `fig:ponder_c0g_phased_array` | Ch.13 | Optimal synthesis |
| `fig:chiral_parametric` | Ch.13 | Chiral impedance antenna parametric |
| `fig:topological_lensing` | Ch.13 | Axiom 4 topological lensing |
| `fig:k4_tlm_phase1` | Ch.13 | K4-TLM phase 1 validation |
| `fig:k4_tlm_phase2` | Ch.13 | K4-TLM phase 2 wire antenna |
| `fig:k4_tlm_phase3_4` | Ch.13 | K4-TLM phase 3+4 3D antenna |
| `fig:leaky_cavity_decay` | Ch.14 | Quantum decay as RLC discharge |
| `fig:autoresonance_pll` | Ch.15 | Autoresonance PLL |
| `fig:sagnac_inductive_drag` | Ch.16 | Sagnac inductive drag |
| `fig:hardware_netlist_overview` | Ch.17 | Hardware netlist engineering overview |
| `fig:superconducting_lock` | Ch.18 | Superconducting metamaterial lock |
| `fig:kinetic_armor_yield` | Ch.18 | Kinetic armor reflection |
| `fig:memristor_hysteresis` | Ch.18 | Neuromorphic memristor hysteresis |

---

## 3. Notation and Custom Macros

### Shared macros from `structure/commands.tex` (all used in this volume)

| Macro | Definition | Usage in Vol 4 |
|-------|-----------|----------------|
| `\Lvac` | `\ensuremath{L_{node}}` | Lattice inductance |
| `\Cvac` | `\ensuremath{C_{node}}` | Lattice capacitance |
| `\Zvac` | `\ensuremath{Z_0}` | Characteristic impedance |
| `\Wcut` | `\ensuremath{\omega_{sat}}` | Saturation frequency |
| `\lp` | `\ensuremath{l_{node}}` | Lattice pitch |
| `\vacuum` | `\ensuremath{M_A}` | The vacuum condensate ($\mathcal{M}_A$ used directly more often) |
| `\slew` | `\ensuremath{c}` | Speed of light |
| `\planck` | `\ensuremath{\hbar}` | Reduced Planck constant |
| `\permeability` | `\ensuremath{\mu_0}` | Vacuum permeability |
| `\permittivity` | `\ensuremath{\epsilon_0}` | Vacuum permittivity |
| `\impedance` | `\ensuremath{Z_0}` | Characteristic impedance |

Note: In practice, Vol 4 chapters overwhelmingly use raw LaTeX notation (`$\mu_0$`, `$\varepsilon_0$`, `$Z_0$`, `$c$`, `$\mathcal{M}_A$`) rather than the shorthand macros. The macros are defined but not prominently employed.

### Volume-specific macros

None defined. No `\newcommand` or `\renewcommand` calls in any chapter file.

### Key project-specific notation (used extensively, not standard)

| Symbol | Meaning | Defined in |
|--------|---------|-----------|
| `$\xi_{topo}$` | Topological conversion constant $e/\ell_{node}$ | Ch.1 |
| `$V_{yield}$` | 43.65 kV dielectric saturation limit | Ch.1, 2, 5, 8, 11... |
| `$V_{snap}$` | 511 kV absolute nodal snap limit | Ch.1, 8, 11... |
| `$S(V)$` / `$S(E)$` | Saturation kernel $\sqrt{1-(V/V_{yield})^2}$ | Ch.1, 2, 5... |
| `$\ell_{node}$` | Lattice pitch $\hbar/(m_e c)$ | Throughout |
| `$\rho_{bulk}$` | Vacuum bulk density $\approx 7.91 \times 10^6$ kg/m^3 | Ch.11, backmatter |
| `$n_{scalar}$` | Local effective refractive index | Ch.8, 11 |
| `$\nu_{vac}$` | Vacuum Poisson's ratio $2/7$ | Ch.2 |
| `$\eta_{chiral}$` | Chiral coupling efficiency $= \nu_{vac}$ | Ch.2 |
| `$\kappa_{FS}$` | Faddeev-Skyrme coupling $= 8\pi$ | backmatter |
| `$p_c$` | Geometric packing fraction $\approx 0.1834$ | backmatter |
| `$pq/(p+q)$` | Harmonic mean of torus knot winding numbers | Ch.3, 12, 13 |

### Translation table imported via `\input`

- `\input{../common/translation_circuit.tex}` — used in Ch.1 (`\label{tab:trans_circuit}`). This table is also re-used in `backmatter/01_appendices.tex`. It is SHARED CROSS-VOLUME.

---

## 4. Cross-References to Other Volumes

### Labels defined in this volume and referenced externally (confirmed)

| Label | Section | Referenced by other volumes |
|-------|---------|----------------------------|
| `\label{sec:k4_tlm}` | Ch.13, section "K4-TLM: Native Lattice Dynamics Simulator" | Yes — Vol 3 memory notes reference Vol 4 K4-TLM simulator |
| `$V_{yield} \approx 43.65$ kV | Ch.1, `eq:varactor`, `sec:vca_nonlinear` | Yes — referenced as "43.65 kV Absolute Dielectric Yield Limit" across the project |

Both labels the task instructions asked to verify are confirmed present in this volume.

### Prose cross-volume references (outbound from Vol 4)

| Reference | Location | Target |
|-----------|----------|--------|
| "as derived in Volume I" / "established in Volume I" | Ch.1, sec:z0_derivation | Vol 1 (physics axioms) |
| "as derived in Volume II" | Ch.2, sec:regimes_of_operation | Vol 2 particle physics |
| "As derived in Book 2, the most stable structure..." | Ch.13 | Vol 2 |
| "As documented in Volume 5 (Organic Circuitry)" | Ch.18 | Vol 5 |
| "As established in Volume 6, the entirety of the Periodic Table..." | Ch.8 | Vol 6 |
| "the supplementary *Periodic Table of Knots*" | Ch.1 | Vol 6 (Periodic Table of Knots) |
| "Chapter 5" / "Chapter 9" cross-references within ch.1 | Ch.1 | Intra-volume; self-referential |
| `\cite{misner1973}` | Ch.1 | Bibliography |
| `\cite{codata2018}` | Ch.1, backmatter | Bibliography |
| `\cite{einstein1916}` | Ch.1 | Bibliography |
| `\cite{flyby2008}` | Ch.1 | Bibliography |
| `\cite{pdg2022}` | Ch.12 | Bibliography |

### Inbound label references to other volumes (unresolvable within Vol 4)

- `\ref{sec:topological_defects_lc}` — referenced in Ch.11 (`sec:induced_vacuum_impedance_mirror`). No such label defined in Vol 4; likely defined in another volume or is a forward reference.
- `\ref{sec:point_yield}` — referenced in Ch.11. Not defined in Vol 4.
- `\ref{eq:dielectric_saturation}` — referenced in Ch.11. Not defined in Vol 4 (similar equations appear but are not labelled `eq:dielectric_saturation`).
- "Chapter 5" references in Ch.1 are intra-volume (forward to ch.10, Quantum Computing — likely a numbering error in the prose).
- "Chapter 7" referenced in Ch.8 as source of metric compression derivation — this is intra-volume (Ch.7 = SMES); the specific derivation is not actually present in Ch.7.
- "Chapter 8" referenced in Ch.11 for vacuum bulk density — this is intra-volume and the derivation is not present in Ch.8.
- "Chapter 13" referenced in Ch.11 for charge-displacement identity — this is intra-volume Ch.1 content referenced as "Chapter 13" — likely a numbering inconsistency from an earlier manuscript version.
- `app:full_derivation_chain` referenced in backmatter — not defined in this volume's backmatter (same anomaly as Vol 2).

---

## 5. Key Concept List

**Section-level concepts:**
Topo-Kinematic Circuit Identity, Topological Conversion Constant ($\xi_{topo}$), Charge-Displacement Identity, Current-Velocity Identity, Voltage-Force Identity, Inductance-Mass Identity, Capacitance-Compliance Identity, Resistance-Viscosity Identity, Metric Varactor, Relativistic Inductor, TVS Zener Diode (Phase Transition), Vacuum Memristor, Thixotropic Relaxation, Zero-Impedance Skin Effect, Impedance of Free Space ($Z_0$), Gravitational Stealth, S-Parameter Analysis, Topological Defects as Resonant LC Solitons, Confinement Bubble (Total Internal Reflection), Pauli Exclusion from Impedance, Orbital Friction Paradox, IMD Spectroscopy, Jensen's Rectification Inequality, Chiral Acoustic Rectification, Dark Wake, Metric Streamlining, Superluminal Transit, Active Acoustic Drill, HOPF-01 Chiral Antenna, Torus Knot Resonant Frequency Shift, Three-Medium Verification, Chiral Figure of Merit, PONDER-01, PONDER-05, DC Cross-Term Amplification, Rarefaction Wave Inversion, Differential Saturation Parallax, Torsion Balance Metrology, Eight-Point Artifact Rejection, Mineral Oil Bath, Beltrami Torus Knot SMES, Force-Free Field, D-T Phase-Lock, Tokamak Ignition Paradox (60.3 kV), Metric-Catalyzed Fusion, WKB Barrier Narrowing, L-H Transition, Anomalous Transport, Alchemist Forge, Hierarchical Alpha Synthesis, Antimatter as Parity-Inverted Topology, Pair Production as Vortex Shedding, Transmon Decoherence, Topological Qubit (Gauss Linking Number), Casimir Cavity Shielding, Kuramoto Phase-Lock, Sagnac-RLVE, Proton Radius Puzzle, Neutron Lifetime Anomaly, Hubble Tension, Black Hole Echoes, CLEAVE-01 Electrometer, HOPF-02 VNA, ROENTGEN-03 Sagnac Induction, ZENER-04 Avalanche Detector, TORSION-05, YBCO Phased Array, Metric Refraction Capacitor ($c^2$ Multiplier), Sapphire Phonon Centrifuge, Induced Vacuum Impedance Mirror, Sagnac-Parallax Galactic Wind, GEO-Synchronous Impedance Differential, EE Bench Dielectric Plateau, Maxwell Stress Tensor Rectification, RLVG Kinematic Entrainment Law, Autoresonant PLL (Schwinger Limit Bypass), Torus Knot Ladder (Baryon Masses), MoM/FDTD/FEM/TLM/CMA mapping to AVE, K4-TLM Simulator, K4 Diamond Lattice, Beltrami Eigenvalue, Chiral FoM, Leaky Cavity (Particle Decay), SPICE Netlists, Sagnac Inductive Drag, Hardware Netlists, Active Topological Metamaterials, Inorganic LLCP, Self-Healing Kinetic Armor, Neuromorphic Memristor

---

## 6. Estimated Leaf Document Count

Each chapter would produce multiple leaf documents. The primary named results (resultboxes) are 51. Adding the SPICE-model sections (4 dedicated chapters: 14, 15, 16, 17), the experimental protocol sections (chapters 11 and 12 each contain 6-12 distinct protocols), and the CEM survey (6 methods x 1 subsection each in ch.13), the K4-TLM multi-phase simulation section, and the distinct application sections in ch.18:

- Chapters 1-2 (circuit theory + thrust mechanics): ~25 leaves (one per named result or major subsection)
- Chapter 3 (HOPF-01): ~10 leaves (falsification protocol, 5 knot predictions, SM baseline, discriminating observables, etc.)
- Chapters 4-6 (PONDER evolution + metrology): ~15 leaves
- Chapter 7 (SMES): ~3 leaves
- Chapter 8 (Fusion): ~15 leaves (tokamak paradox, metric-catalyzed fusion, isotope fission, alchemist forge)
- Chapter 9 (Antimatter): ~4 leaves
- Chapter 10 (Quantum computing): ~5 leaves
- Chapter 11 (Experimental falsification): ~20 leaves (multiple distinct projects and protocols)
- Chapter 12 (Falsifiable predictions): ~8 leaves
- Chapter 13 (Future geometries + K4-TLM): ~15 leaves
- Chapters 14-17 (SPICE chapters): ~4 leaves each = 16 leaves
- Chapter 18 (Metamaterials): ~5 leaves

**Estimated total: 140-160 leaf documents**

---

## 7. Anomalies

1. **Orphaned file `circuit_sagnac_rlvg.tex`**: Present in `chapters/` directory but NOT listed in `_manifest.tex`. The file begins with `\documentclass[border=10pt]{standalone}` — it is a standalone TikZ/CircuiTikZ circuit diagram, not a chapter. It contains a trailing `\begin{summarybox}` and `\begin{exercisebox}` block after the `\end{document}` command, making those blocks unreachable. This file appears to be a circuit illustration source that was accidentally placed in the chapters directory. It will not be compiled by `main.tex`.

2. **Missing `\label` keys on many chapters**: Chapters 1, 2, 7, and 11 have no `\label` on their `\chapter` command. This means they cannot be cross-referenced by label from other chapters or volumes. This is inconsistent with chapters 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18 which all have `\label{ch:...}`.

3. **Dangling internal cross-references**: Three labels referenced in Ch.11 (`\ref{sec:topological_defects_lc}`, `\ref{sec:point_yield}`, `\ref{eq:dielectric_saturation}`) are not defined anywhere in this volume. These may resolve in another volume or may be authoring errors.

4. **Prose chapter numbering inconsistency**: In Ch.11, the text refers to "Chapter 13" for the charge-displacement identity ($Q \equiv \xi_{topo} x$), but this result is in Chapter 1 of Vol 4. This suggests earlier draft had a different chapter ordering, and prose was not updated when chapter numbers changed.

5. **All summarybox and exercisebox content is boilerplate**: Every chapter ends with an identical summarybox (three bullet points with "[chapter name]" substituted) and an exercisebox with two exercises that follow an identical template. None of the summary or exercise content is chapter-specific. This is a structural anomaly — these boxes exist but contain no unique distillable content.

6. **Chapter 7 (Topological SMES) is unusually short (~57 lines)**: Has only an introduction and two subsections with minimal derivation. It is approximately 10x shorter than average chapters and reads more like an outline than a complete chapter.

7. **Ch.11 is unusually large (~550 lines)**: Contains approximately 15 distinct experimental protocols, making it the longest chapter by a wide margin. It may need subdivision into multiple KB entries.

8. **`sec:ee_bench` label not found in Ch.12**: Ch.11 contains `\ref{sec:ee_bench}` referencing a label that should be in Ch.12. Inspection of Ch.12 confirms the section exists ("The EE Bench: The Macroscopic Dielectric Plateau") but has no `\label` command on it. This is a dangling reference within the volume.

9. **Ch.18 figures use path `../../assets/sim_outputs/`**: Unlike all other chapters which use figure names without paths (resolved via `\graphicspath`), Ch.18 uses explicit relative paths (`\includegraphics[width=\textwidth]{../../assets/sim_outputs/superconducting_metamaterial_lock.png}`). This is inconsistent with the rest of the volume and may cause compilation errors depending on the current working directory during compilation.

10. **`app:full_derivation_chain` reference in backmatter**: The shared `backmatter/01_appendices.tex` references `app:full_derivation_chain` and `tab:sm_params`. Neither label is defined in the backmatter text that was read, and this is the same dangling reference reported in the Vol 2 survey. This is a pre-existing cross-volume anomaly.

---

*Survey completed. All 18 chapter files read in full. Shared files read: `structure/commands.tex`, `common/translation_circuit.tex`, `backmatter/01_appendices.tex`. File `circuit_sagnac_rlvg.tex` read (orphaned). Frontmatter not read per instructions.*
