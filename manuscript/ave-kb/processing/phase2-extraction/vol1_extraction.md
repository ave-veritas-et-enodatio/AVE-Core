# Vol 1 — Phase 2 Extraction

**Produced by:** kb-latex-specialist
**Source volume:** `manuscript/vol_1_foundations/`
**Skeleton reference:** approved taxonomy skeleton (task prompt) + `phase1-taxonomy/vol1_taxonomy.md`
**Date:** 2026-04-02

---

## Source Directory Listing

All `.tex` files in `manuscript/vol_1_foundations/`:

```
vol_1_foundations/main.tex
vol_1_foundations/frontmatter/00_title.tex
vol_1_foundations/chapters/_manifest.tex
vol_1_foundations/chapters/00_intro.tex
vol_1_foundations/chapters/01_fundamental_axioms.tex
vol_1_foundations/chapters/02_macroscopic_moduli.tex
vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex
vol_1_foundations/chapters/04_continuum_electrodynamics.tex
vol_1_foundations/chapters/05_universal_spatial_tension.tex
vol_1_foundations/chapters/06_universal_operators.tex
vol_1_foundations/chapters/07_regime_map.tex
```

Chapter manifest order (from `_manifest.tex`): 00 → 01 → 02 → 03 → 04 → 05 → 06 → 07.
No gaps in the chapter file sequence. All 8 chapter files confirmed present.

Backmatter included in `main.tex` via `\input`: `01_appendices.tex`, `02_full_derivation_chain.tex`,
`12_mathematical_closure.tex`, `03_geometric_inevitability.tex`, `05_universal_solver_toolchain.tex`.
(All five backmatter appendices are included by Vol 1.)

---

## Skeleton-to-Source Mapping

| Skeleton leaf path | Source file | Section/label | Line range (approx.) | Notes |
|---|---|---|---|---|
| `vol1/ch0-intro.md` | `00_intro.tex` | full file | 1–55 | unnumbered chapter `\chapter*{Introduction}`; one `examplebox`, no resultboxes, no `\label` keys; ends with Chapter Summary + Exercises as `\section*` |
| `vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md` | `01_fundamental_axioms.tex` | `\section{The Four Fundamental Axioms}` | 32–59 | Contains 3 resultboxes: Topological Conversion Constant (`\xi_{topo}`), Macroscopic Hardware Action (`\mathcal{L}_{node}`), Non-Linear Dielectric Saturation (`C_{eff}`); no `\label` on these equations — the section itself is the atom |
| `vol1/axioms-and-lattice/ch1-fundamental-axioms/calibration-cutoff-scales.md` | `01_fundamental_axioms.tex` | `\section{The Calibration of the Effective Cutoff Scales}` | 14–31 | Prose enumeration of 3 cutoff scales ($\ell_{node}$, $\alpha$, $G$); one figure (`fig:calibration_flowchart`); no resultboxes in this section; calibration table appears later in §Methodology (see kirchhoff-network-method.md note) |
| `vol1/axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md` | `01_fundamental_axioms.tex` | `\section{The Vacuum as an LC Resonant Condensate}` (both subsections) | 61–139 | §1.3.1 "Planck Scale Artifact" (2 resultboxes: True Gravitational Coupling, True Planck Length) + §1.3.2 "Vacuum Porosity Ratio" (fig:lattice_3d); together these form one coherent atom on the condensate model |
| `vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md` | `01_fundamental_axioms.tex` | `\section{The Pathway to a Zero-Parameter Universe}` | 107–145 | 1 resultbox: Trace-Reversal Packing Fraction; 2 figures (fig:rigidity_alpha, fig:equilibrium_G); derives $\alpha$ via EMT and $G$ via Machian equilibrium |
| `vol1/axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md` | `01_fundamental_axioms.tex` | `\section{Methodology: Explicit Discrete Kirchhoff Execution}` + subsections | 146–196 | 2 resultboxes: Edge Strain Update, Node Displacement Update; also contains the Master Constants Derivation Pipeline table (the calibration table in the task prompt description); fig:calibration_flowchart is in §1.1 but referenced here |
| `vol1/axioms-and-lattice/ch1-fundamental-axioms/lattice-structure.md` | `01_fundamental_axioms.tex` | Subsections under §Kirchhoff: `\subsection{The Network Mapping}` + `\subsection{The Explicit Laplacian Integration}` | 151–178 | OVERLAP NOTE: `kirchhoff-network-method.md` and `lattice-structure.md` both map to §1.5 (Kirchhoff Execution) and its subsections. The skeleton separates them; the source does not have a distinct "Network Mapping" section independent of the Kirchhoff methodology section. See Ambiguities. |
| `vol1/axioms-and-lattice/ch2-macroscopic-moduli/implosion-paradox.md` | `02_macroscopic_moduli.tex` | `\section{The Implosion Paradox: Why The Vacuum Must Be Micropolar}` | 13–20 | Pure prose, no resultboxes; argument about MacCullagh's condition and negative bulk modulus forcing micropolar continuum |
| `vol1/axioms-and-lattice/ch2-macroscopic-moduli/constitutive-moduli.md` | `02_macroscopic_moduli.tex` | `\section{The Constitutive Moduli of the Void}` | 21–48 | 1 resultbox: Impedance Dimensional Isomorphism; two-item list defining $\mu_0$ and $\epsilon_0$ as mechanical analogs |
| `vol1/axioms-and-lattice/ch2-macroscopic-moduli/topo-kinematic-isomorphism.md` | `02_macroscopic_moduli.tex` | `\subsection*{Topo-Kinematic Dimensional Isomorphism}` (unnumbered, at end of chapter) | 120–137 | The verbatim 7-row table (Voltage→Force, Current→Velocity, Impedance→Kinematic impedance, Inductance→Mass, Capacitance→Compliance, $\mu_0$→linear density, $\epsilon_0$→inverse tension); this subsection is UNNUMBERED (`\subsection*`) and appears after the `dielectric-snap-limit` subsection |
| `vol1/axioms-and-lattice/ch2-macroscopic-moduli/dielectric-rupture.md` | `02_macroscopic_moduli.tex` | `\section{Dielectric Rupture and The Volumetric Energy Collapse}` | 49–80 | 3 resultboxes: Discrete Voronoi Cell Volume, Vacuum Packing Fraction ($p_c = 8\pi\alpha$), Inverse Fine-Structure Constant; fig:emt_landscape; reference to "Chapter 12" is unresolved stale cross-reference |
| `vol1/axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md` | `02_macroscopic_moduli.tex` | `\subsection{Computational Proof of Effective Over-Bracing}` + `\subsection{The Dielectric Snap Limit ($V_{snap} = 511.0$ kV)}` | 82–118 | 3 resultboxes: Over-Bracing Factor ($\mathcal{R}_{OB} \approx 1.673$), Secondary Link Reach, Dielectric Snap Limit ($V_{snap}$); examplebox for lab comparison |
| `vol1/dynamics/ch3-quantum-signal-dynamics/dielectric-lagrangian.md` | `03_quantum_and_signal_dynamics.tex` | `\section{The Dielectric Lagrangian: Hardware Mechanics}` | 16–52 | 4 resultboxes: Dielectric Lagrangian Density, Vector Potential Dimensions, Vector Potential as Mass Flow, Kinetic Energy Density Dimensions |
| `vol1/dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md` | `03_quantum_and_signal_dynamics.tex` | `\subsection{The Paley-Wiener Hilbert Space}` | 57–68 | 1 resultbox: Analytic Signal Extension; Nyquist / Whittaker-Shannon construction of quantum Hilbert space |
| `vol1/dynamics/ch3-quantum-signal-dynamics/gup-derivation.md` | `03_quantum_and_signal_dynamics.tex` | `\subsection{The Generalized Uncertainty Principle (GUP)}` | 70–114 | 3 resultboxes: Continuous Momentum Expectation, Discrete Graph Commutator, The GUP; fig:gup_resolution; examplebox |
| `vol1/dynamics/ch3-quantum-signal-dynamics/schrodinger-from-circuit.md` | `03_quantum_and_signal_dynamics.tex` | `\subsection{Deriving the Schrödinger Equation from Circuit Resonance}` | 116–132 | 2 resultboxes: Klein-Gordon Equation as Circuit Resonance, The Schrödinger Equation |
| `vol1/dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md` | `03_quantum_and_signal_dynamics.tex` | `\section{Wave-Particle Duality and The Zero-Impedance Boundary}` + subsections | 134–175 | 2 resultboxes: Transmission Line Reflection, Absolute Impedance Boundary ($\Gamma = -1$); fig:double_slit_comparison; subsections: $0\Omega$ Boundary, Internal Confinement, Scattering/Pauli Exclusion |
| `vol1/dynamics/ch3-quantum-signal-dynamics/quantum-foam-virtual.md` | `03_quantum_and_signal_dynamics.tex` | `\section{The Physical Origin of Quantum Foam and Virtual Particles}` | 176–191 | No resultboxes; two subsections: Quantum Foam as RMS Thermal Noise, Virtual Particles as Failed Topologies |
| `vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md` | `03_quantum_and_signal_dynamics.tex` | `\section{Deterministic Interference and The Measurement Effect}` | 193–217 | 2 resultboxes: Extracted Measurement Work, Deterministic Born Rule; fig:double_slit_wake |
| `vol1/dynamics/ch3-quantum-signal-dynamics/nonlinear-telegrapher.md` | `03_quantum_and_signal_dynamics.tex` | `\section{Non-Linear Dynamics and Topological Shockwaves}` | 219–252 | 4 resultboxes: Non-Linear Telegrapher Equation (`\label{eq:nonlinear_wave}`), Dielectric Saturation Taylor Expansion, Euler-Heisenberg $E^4$ Correction; fig:vacuum_dielectric_saturation; `eq:nonlinear_wave` is the only labelled equation in ch.3 |
| `vol1/dynamics/ch3-quantum-signal-dynamics/entanglement-mechanism.md` | `03_quantum_and_signal_dynamics.tex` | `\section{Classical Causality of Quantum Entanglement (Bell's Theorem)}` | 254–286 | No resultboxes; 2 subsections: Transverse vs. Longitudinal Wave Propagation (displays $v_{long} \approx 3.9c$), The Local Mechanism of Entanglement; both inline equations (unnumbered displays) |
| `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md` | `04_continuum_electrodynamics.tex` | `\section{The Unifying Master Equation}` | 32–70 | 5 resultboxes: Maxwell-Heaviside Acoustic Wave Equation, FDTD Yee Cell Update, D'Alembert Wave Operator, Non-Linear Permittivity Collapse, Field-Dependent Wave Speed, Unifying AVE Master Equation (`\label{eq:master_wave}`) |
| `vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md` | `04_continuum_electrodynamics.tex` | `\section{Continuum Electrodynamics of the LC Condensate}` | 72–117 | 5 resultboxes: Effective Inductive Node Mass, Longitudinal Tension Wave Velocity, Macroscopic Bulk Mass Density ($\rho_{bulk} \approx 7.92 \times 10^6$ kg/m³), Baseline Vacuum Shear Modulus ($G_{vac}$), Kinematic Network Mutual Inductance ($\nu_{kin}$) |
| `vol1/dynamics/ch4-continuum-electrodynamics/operating-regimes-table.md` | `04_continuum_electrodynamics.tex` | `\section{Analytical Operating Regimes of the Vacuum}` | 119–151 | No resultboxes; prose enumeration of 3 regimes + verbatim "Formal Operating Regime Classification" table (3-row: Linear/Non-Linear/Rupture); fig:operating_regimes — NOTE: ch.4 has only 3 regimes; ch.7 expands this to 4 regimes (I–IV). The taxonomy leaf `operating-regimes-table.md` maps to the ch.4 3-regime table. |
| `vol1/dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md` | `04_continuum_electrodynamics.tex` | `\section{The Macroscopic Yield Limit: The Magnetic Saturation Transition}` | 153–197 | 1 resultbox: Macroscopic Yield Stress Limit; subsections on Asteroid Belts/Oort Clouds and Sagnac-RLVE falsification; fig:dielectric_avalanche |
| `vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` | `04_continuum_electrodynamics.tex` | `\section{Deriving MOND from Unruh-Hawking Hoop Stress}` (`\label{sec:galactic_saturation}`) | 199–278 | 2 resultboxes: Asymptotic Hubble Constant (`\label{eq:H_infinity}`), Geometric Drift Acceleration, Superluminal Lattice Compression Velocity; examplebox (Hubble derivation); fig:unruh_hawking_hoop_stress; the Dark Sector Comparison table is included in this section |
| `vol1/dynamics/ch4-continuum-electrodynamics/dark-sector.md` | `04_continuum_electrodynamics.tex` | `\subsection*{Dark Sector Comparison: AVE vs. Observation}` (unnumbered table, embedded in §4.4) | 240–254 | The 4-row comparison table ($H_\infty$, $a_0$, Dark Matter, Dark Energy) is an unnumbered subsection within `sec:galactic_saturation`. It is NOT a separate section — it is inside `mond-hoop-stress.md`'s section. See Ambiguities. |
| `vol1/dynamics/ch4-continuum-electrodynamics/bullet-cluster.md` | `04_continuum_electrodynamics.tex` | `\section{The Bullet Cluster: Refractive Tensor Shockwaves}` | 281–297 | No resultboxes; Subsections: main Bullet Cluster argument + `\subsection{Resolving the DAMA/LIBRA vs XENONnT Paradox}` |
| `vol1/operators-and-regimes/ch5-universal-spatial-tension/mass-unification.md` | `05_universal_spatial_tension.tex` | `\section{The Unification of Mass}` | 13–31 | 2 resultboxes: Vacuum Compliance Scalar ($K \equiv \hbar/c$), Universal Spatial Tension ($M_{topo}$) |
| `vol1/operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md` | `05_universal_spatial_tension.tex` | `\section{Scale Invariance across the Framework}` | 33–64 | No resultboxes; 2 subsections: Lepton Tension Limit (3 generations from Cosserat sectors), Nuclear Tension Limit (Neon-20 bipyramid, 1 resultbox: Bipyramid Pairwise Binding Energy); examplebox; fig:neon20_geometry |
| `vol1/operators-and-regimes/ch5-universal-spatial-tension/scale-invariant-predictions.md` | `05_universal_spatial_tension.tex` | `\subsection*{Scale-Invariant Mass Predictions}` table | 87–104 | The 4-row prediction table (Electron, Muon, Tau, Neon-20 with AVE vs CODATA); this is an unnumbered subsection inside §3 (Continuous FDTD Yee Lattice Proof) |
| `vol1/operators-and-regimes/ch5-universal-spatial-tension/fdtd-yee-proof.md` | `05_universal_spatial_tension.tex` | `\section{Continuous FDTD Yee Lattice Proof}` (prose) | 73–86 | No resultboxes in the prose body; fig:fdtd_yee_lattice; argument for continuous FDTD over virtual particles. The prediction table (scale-invariant-predictions.md) is the trailing unnumbered subsection of this section. |
| `vol1/operators-and-regimes/ch6-universal-operators/impedance-operator.md` | `06_universal_operators.tex` | `\section{The Universal Impedance Operator}` (`\label{sec:universal_impedance}`) | 24–92 | NO resultbox — instead a raw `\framebox` theorem (Scale Invariance); followed by prose and `tab:cross_scale` (8-row cross-scale constitutive mapping table); fig:cross_scale is in §6.3 but is the figure for impedance operator + saturation operator + reflection coefficient together |
| `vol1/operators-and-regimes/ch6-universal-operators/saturation-operator.md` | `06_universal_operators.tex` | `\section{The Universal Saturation Operator}` (`\label{sec:universal_saturation}`) | 95–119 | 1 resultbox: Universal Saturation Factor `S(A, A_c) = sqrt(1-(A/A_c)^2)` (`\label{eq:saturation_sigma}`); 4 domain applications listed |
| `vol1/operators-and-regimes/ch6-universal-operators/reflection-coefficient.md` | `06_universal_operators.tex` | `\section{The Universal Reflection Coefficient}` (`\label{sec:universal_gamma}`) | 121–178 | 1 resultbox: Universal Reflection Coefficient (`\label{eq:universal_gamma}`); 3-row application table; examplebox; fig:cross_scale (shared with §6.1) |
| `vol1/operators-and-regimes/ch6-universal-operators/pairwise-potential.md` | `06_universal_operators.tex` | `\section{The Universal Pairwise Potential}` (`\label{sec:universal_pairwise}`) | 182–216 | 1 resultbox: Universal Pairwise Potential (`\label{eq:universal_pairwise}`); 3-regime table; code path note |
| `vol1/operators-and-regimes/ch6-universal-operators/y-to-s-conversion.md` | `06_universal_operators.tex` | `\section{The Universal Y-to-S Conversion}` (`\label{sec:universal_y_to_s}`) | 219–232 | 1 resultbox: Multiport S-Matrix (`\label{eq:y_to_s}`); minimal prose; code path note |
| `vol1/operators-and-regimes/ch6-universal-operators/eigenvalue-target.md` | `06_universal_operators.tex` | `\section{The Universal Eigenvalue Target}` (`\label{sec:universal_eigenvalue}`) | 235–249 | 1 resultbox: Eigenvalue Target (`\label{eq:eigenvalue_target}`); minimal prose |
| `vol1/operators-and-regimes/ch6-universal-operators/spectral-analyser.md` | `06_universal_operators.tex` | `\section{The Universal Spectral Analyser}` (`\label{sec:universal_spectral}`) | 251–264 | No resultbox; itemized description (Fourier peaks, Wiener-Khintchin autocorrelation, DSP complement); code path note |
| `vol1/operators-and-regimes/ch6-universal-operators/packing-reflection.md` | `06_universal_operators.tex` | `\section{The Universal Packing Reflection}` (`\label{sec:universal_packing}`) | 267–291 | 1 resultbox (align environment): Packing Reflection Coefficient with `\label{eq:rg_target}` and `\label{eq:gamma_pack}`; domain-agnostic description |
| `vol1/operators-and-regimes/ch7-regime-map/four-regimes.md` | `07_regime_map.tex` | `\section{The Four Universal Regimes}` + subsections | 16–88 | 1 resultbox: Universal Regime Classification ($S(r) = \sqrt{1-r^2}$, $r = A/A_c$); 4-column regime table; subsections: Semiconductor Device Analogy, Perturbative Expansion (Regime I) including `\label{eq:S_taylor}` |
| `vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md` | `07_regime_map.tex` | `\section{Domain Control Parameter Catalog}` (`\label{sec:domain_catalog}`) | 90–230 | 8 subsections (EM-Dielectric, EM-Field, Gravitational, BCS, Magnetic, Nuclear, GW, Galactic); each with a 2-row table defining $A$, $A_c$, control parameter; one examplebox (Black Hole regime) |
| `vol1/operators-and-regimes/ch7-regime-map/regime-equation-sets.md` | `07_regime_map.tex` | `\section{Regime-Specific Equation Sets}` | 232–249 | No resultbox; 6-column table ($\varepsilon_{eff}$, $\mu_{eff}$, $c_{eff}$, $Z_{eff}$, $C_{eff}$, $Q$ across 4 regimes); discusses symmetric vs. asymmetric saturation |
| `vol1/operators-and-regimes/ch7-regime-map/dimensional-analysis.md` | `07_regime_map.tex` | `\section{Cross-Domain Dimensional Analysis}` (`\label{sec:dimensional_analysis}`) | 251–260 | 1 resultbox: Universal Dimensionless Master Equation ($\partial_{tt}\phi = c_0^2(1-r^2)^{1/2}\nabla^2\phi$) |
| `vol1/operators-and-regimes/ch7-regime-map/experimental-design-space.md` | `07_regime_map.tex` | `\section{The Experimental Design Space}` | 262–299 | No resultbox; 4-section experiment/object table (18 rows across Regimes I–IV); fig:regime_design_space |

---

## Common/ Translation Table Filenames (CONFIRMED)

Exact filenames as found on disk in `manuscript/common/`:

```
translation_circuit.tex
translation_condensed_matter.tex
translation_cosmology.tex
translation_gravity.tex
translation_particle_physics.tex
translation_protein.tex
translation_protein_solver.tex
translation_qm.tex
```

**Total: 8 files.**

These do NOT match the taxonomy skeleton's assumed filenames (`translation-em.md`, `translation-gravity.md`, `translation-nuclear.md`, `translation-quantum.md`, `translation-thermo.md`, `translation-bcs.md`, `translation-galactic.md`, `translation-grav-waves.md`). See Ambiguities section for full reconciliation.

---

## Backmatter Files

Checked against `manuscript/backmatter/`:

| File | Status |
|---|---|
| `02_full_derivation_chain.tex` | FOUND |
| `05_universal_solver_toolchain.tex` | FOUND |
| `12_mathematical_closure.tex` | FOUND |
| `01_appendices.tex` | FOUND |
| `03_geometric_inevitability.tex` | FOUND (bonus — not in checklist) |
| `04_physics_engine_architecture.tex` | FOUND (bonus — not in checklist) |

All 4 checklist files confirmed present. `03_geometric_inevitability.tex` and `04_physics_engine_architecture.tex` also exist but were not on the checklist.

`manuscript/common/appendix_experiments.tex`: **FOUND**

---

## Empty Skeleton Positions

No skeleton position is entirely without source material. All 46 leaves in the task-prompt skeleton have a confirmed source location.

---

## Leaf Boundary Notes

### Ch1: `kirchhoff-network-method.md` vs. `lattice-structure.md`

The skeleton lists these as two distinct leaves:
- `kirchhoff-network-method.md` — described as "network mapping, Laplacian integration, master constants pipeline table"
- `lattice-structure.md` — described as "chiral SRS net geometry; topological conversion constant $\xi_{topo}=e/\ell_{node}$"

In the source, `01_fundamental_axioms.tex` §1.5 is one section (`\section{Methodology: Explicit Discrete Kirchhoff Execution}`) with three subsections:
- `\subsection{The Network Mapping}` — nodes as capacitors, struts as inductors
- `\subsection{The Explicit Laplacian Integration}` — 2 resultboxes (Edge Strain Update, Node Displacement Update)
- `\subsection*{Master Constants Derivation Pipeline}` — derivation table

The label `\xi_{topo}=e/\ell_{node}` (the "topological conversion constant" noted for `lattice-structure.md`) is actually defined in **§1.2 (The Four Fundamental Axioms)**, not in §1.5. The Master Constants table in §1.5 lists $\xi_{topo}$ as row 3 of the table, but doesn't derive it there. The Axiom 2 resultbox (in `axiom-definitions.md`) defines $\xi_{topo}$.

Figures `fig:lattice_3d`, `fig:rigidity_alpha`, and `fig:equilibrium_G` are all in different sections of ch.1:
- `fig:lattice_3d` is in §1.3.2 (Vacuum Porosity Ratio, inside `lc-condensate-vacuum.md`)
- `fig:rigidity_alpha` is in §1.4 (Zero-Parameter Universe, inside `zero-parameter-universe.md`)
- `fig:equilibrium_G` is in §1.4 (Zero-Parameter Universe, inside `zero-parameter-universe.md`)

**Recommendation:** The `lattice-structure.md` skeleton leaf as described does not correspond to a discrete source section. The Network Mapping subsection (~5 lines) is the closest match. Distiller should either: (a) combine `kirchhoff-network-method.md` and `lattice-structure.md` into one leaf covering all of §1.5, or (b) assign `lattice-structure.md` to the §1.3.2 Vacuum Porosity Ratio subsection (which contains `fig:lattice_3d`). Option (b) would require `lc-condensate-vacuum.md` to cover only §1.3.1.

### Ch2: `topo-kinematic-isomorphism.md`

The Topo-Kinematic Dimensional Isomorphism table appears as an **unnumbered subsection** (`\subsection*{...}`) at the very end of ch.2, after the `dielectric-snap-limit` content. In the source it is the last element before `\section*{Chapter Summary}`. The distiller should note this position: it is physically the trailing content of the chapter, not a standalone section.

### Ch4: `dark-sector.md` vs. `mond-hoop-stress.md`

The Dark Sector Comparison table (`\subsection*{Dark Sector Comparison: AVE vs.\ Observation}`) is an **unnumbered subsection** embedded within `\section{Deriving MOND from Unruh-Hawking Hoop Stress}` (`\label{sec:galactic_saturation}`). It is not a separate section. The 4-row table appears at lines ~240–254, between the MOND resultboxes and the examplebox. Both skeleton leaves (`mond-hoop-stress.md` and `dark-sector.md`) map to content within the single `sec:galactic_saturation` section. Distiller must split this section at a boundary they define; the natural split point is after the last MOND resultbox and before the table.

### Ch5: `scale-invariant-predictions.md` vs. `fdtd-yee-proof.md`

The Scale-Invariant Mass Predictions table is an **unnumbered subsection** (`\subsection*{Scale-Invariant Mass Predictions}`) inside `\section{Continuous FDTD Yee Lattice Proof}`. These are two skeleton leaves from one source section. The split is natural: prose argument = `fdtd-yee-proof.md`, prediction table = `scale-invariant-predictions.md`. However `fig:neon20_geometry` (listed under `scale-invariant-predictions.md`) actually belongs to §5.2.2 (Nuclear Tension Limit, which maps to `scale-invariance.md`). The FDTD section has `fig:fdtd_yee_lattice`. The prediction table has no dedicated figure.

### Ch6: `impedance-operator.md` — no resultbox, raw framebox

`sec:universal_impedance` contains a raw `\framebox[\textwidth]` theorem (not a `resultbox` tcolorbox) plus `tab:cross_scale`. There is no `\begin{resultbox}` in §6.1. The framebox content should be reproduced verbatim in the leaf. The `fig:cross_scale` figure appears in §6.3 (reflection coefficient) but visually summarizes §6.1–6.3 together.

### Ch4 vs Ch7 regime tables

Two different regime tables exist in the source:
- Ch.4 §4.3 (maps to `operating-regimes-table.md`): 3-regime table (Linear/Non-Linear/Rupture) with $\Delta\phi/\alpha$ as control parameter
- Ch.7 §7.1 (maps to `four-regimes.md`): 4-regime table (I–IV) with $r = A/A_c$ as control parameter, plus semiconductor analogy

These are genuinely distinct: ch.4 introduces the concept with 3 regimes; ch.7 formalizes to 4 with derived boundaries. No conflict.

---

## Notation and Macro Notes

All custom macros are defined in `manuscript/structure/commands.tex` (shared). Per MEMORY.md the macros `\Lvac`, `\Cvac`, `\Zvac`, `\Wcut`, `\lp`, `\vacuum`, `\slew`, `\planck`, `\permeability`, `\permittivity`, `\impedance` are defined with `\providecommand` and are available to all volumes.

**Confirmed from Vol 1 source reading:** None of the 11 custom macros appear to be called in any of the 8 chapter files. All physics notation is written directly (e.g., `Z_0`, `\mu_0`, `\epsilon_0`, `\mathcal{M}_A`). The macro `\vacuum` is defined but unused — `$\mathcal{M}_A$` is used directly everywhere.

**For distillers:** No macro substitution is required for Vol 1 leaves. Render all equations exactly as written in source. Custom tcolorbox environments (`resultbox`, `examplebox`, `objectivebox`, etc.) are structural wrappers — their content is the leaf content; the wrapper becomes Markdown formatting.

**Equation label inventory** (labelled equations that distillers must preserve as anchors):

| Label | Location | Leaf |
|---|---|---|
| `eq:nonlinear_wave` | ch.3 §Non-Linear Dynamics | `nonlinear-telegrapher.md` |
| `eq:master_wave` | ch.4 §Unifying Master Equation | `master-equation.md` |
| `eq:H_infinity` | ch.4 §MOND/Hoop Stress | `mond-hoop-stress.md` |
| `eq:saturation_sigma` | ch.6 §Universal Saturation | `saturation-operator.md` |
| `eq:universal_gamma` | ch.6 §Universal Reflection | `reflection-coefficient.md` |
| `eq:universal_pairwise` | ch.6 §Universal Pairwise | `pairwise-potential.md` |
| `eq:y_to_s` | ch.6 §Y-to-S Conversion | `y-to-s-conversion.md` |
| `eq:eigenvalue_target` | ch.6 §Eigenvalue Target | `eigenvalue-target.md` |
| `eq:rg_target` | ch.6 §Packing Reflection | `packing-reflection.md` |
| `eq:gamma_pack` | ch.6 §Packing Reflection | `packing-reflection.md` |
| `eq:S_taylor` | ch.7 §Four Regimes (Regime I subsection) | `four-regimes.md` |
| `sec:galactic_saturation` | ch.4 §MOND | `mond-hoop-stress.md` |
| `sec:universal_impedance` | ch.6 §1 | `impedance-operator.md` |
| `sec:universal_saturation` | ch.6 §2 | `saturation-operator.md` |
| `sec:universal_gamma` | ch.6 §3 | `reflection-coefficient.md` |
| `sec:universal_pairwise` | ch.6 §4 | `pairwise-potential.md` |
| `sec:universal_y_to_s` | ch.6 §5 | `y-to-s-conversion.md` |
| `sec:universal_eigenvalue` | ch.6 §6 | `eigenvalue-target.md` |
| `sec:universal_spectral` | ch.6 §7 | `spectral-analyser.md` |
| `sec:universal_packing` | ch.6 §8 | `packing-reflection.md` |
| `sec:domain_catalog` | ch.7 §2 | `domain-catalog.md` |
| `sec:dimensional_analysis` | ch.7 §4 | `dimensional-analysis.md` |
| `ch:fundamental_axioms` | ch.1 | chapter label |
| `ch:macroscopic_moduli` | ch.2 | chapter label |
| `ch:quantum_signal_dynamics` | ch.3 | chapter label |
| `ch:electrodynamics` | ch.4 | chapter label |
| `ch:universal_spatial_tension` | ch.5 | chapter label |
| `ch:universal_operators` | ch.6 | chapter label |
| `ch:regime_map` | ch.7 | chapter label |

**Labels NOT found** (mentioned in taxonomy §1 invariants but absent from source):
- `eq:axiom1_impedance`, `eq:axiom1_pitch`, `eq:axiom2_alpha`, `eq:axiom2_v_yield`, `eq:axiom3_gravity`, `eq:axiom3_refraction`, `eq:axiom4_saturation` — these label names appear in the taxonomy §1 but none exist in `01_fundamental_axioms.tex`. The Four Fundamental Axioms section has 3 resultboxes but none carry `\label{eq:...}`. **The axiom equations are unlabelled in source.** The `eq:axiom*` label names used throughout the taxonomy are architectural labels that the KB must assign, not source labels.
- `eq:universal_impedance` and `eq:universal_saturation` — listed in taxonomy §3 but not in source. `sec:universal_impedance` and `eq:saturation_sigma` are the actual source labels.
- `eq:universal_reflection` — listed in taxonomy; not in source. `eq:universal_gamma` is the actual label.

---

## Ambiguities Requiring Coordinator Decision

### Ambiguity 1: Translation table naming mismatch (CRITICAL)

The taxonomy skeleton (`vol1_taxonomy.md` §3, `common/` section) lists 8 translation leaf filenames:
`translation-em.md`, `translation-gravity.md`, `translation-nuclear.md`, `translation-quantum.md`,
`translation-thermo.md`, `translation-bcs.md`, `translation-galactic.md`, `translation-grav-waves.md`

The actual files on disk are:
`translation_circuit.tex`, `translation_condensed_matter.tex`, `translation_cosmology.tex`,
`translation_gravity.tex`, `translation_particle_physics.tex`, `translation_protein.tex`,
`translation_protein_solver.tex`, `translation_qm.tex`

**Mapping attempt** (8 taxonomy names → 8 disk files, where possible):

| Taxonomy skeleton name | Probable disk source | Confidence |
|---|---|---|
| `translation-gravity.md` | `translation_gravity.tex` | HIGH |
| `translation-quantum.md` | `translation_qm.tex` | HIGH |
| `translation-em.md` | `translation_circuit.tex` | MEDIUM (circuit = EM/LC analog) |
| `translation-bcs.md` | `translation_condensed_matter.tex` | MEDIUM (condensed matter includes BCS) |
| `translation-galactic.md` | `translation_cosmology.tex` | MEDIUM (cosmology ≈ galactic) |
| `translation-nuclear.md` | `translation_particle_physics.tex` | MEDIUM (particle physics includes nuclear) |
| `translation-grav-waves.md` | ??? | LOW — no obvious match |
| `translation-thermo.md` | ??? | LOW — no obvious match |
| ??? | `translation_protein.tex` | No taxonomy slot |
| ??? | `translation_protein_solver.tex` | No taxonomy slot |

**The disk has 2 files with no taxonomy slot** (protein tables) and the taxonomy has 2 names with no disk match (thermo, grav-waves). The coordinator must reconcile the `common/` skeleton leaf names against the actual 8 disk files before distillation of `common/` leaves can proceed.

### Ambiguity 2: `lattice-structure.md` — skeleton leaf without a discrete source section

As detailed in Leaf Boundary Notes, the description in the taxonomy ("chiral SRS net geometry; xi_topo = e/ell_node") does not correspond to any single discrete section in ch.1. Options: (a) merge `kirchhoff-network-method.md` + `lattice-structure.md` into one leaf covering §1.5 in full; (b) split §1.3.2 (Vacuum Porosity Ratio + `fig:lattice_3d`) out of `lc-condensate-vacuum.md` and rename it `lattice-structure.md`. Coordinator decision required before distillation of ch.1 leaves.

### Ambiguity 3: `dark-sector.md` vs. `mond-hoop-stress.md` boundary

The Dark Sector Comparison table is an unnumbered subsection inside `sec:galactic_saturation`. Both skeleton leaves map to the same source section. The distiller must define the split boundary (natural: after the Superluminal Lattice Compression Velocity resultbox, before `\subsection*{Dark Sector Comparison}`). This is a distiller decision if the coordinator accepts the split, but it should be confirmed that `dark-sector.md` is intended to be a standalone leaf rather than merged into `mond-hoop-stress.md`.

### Ambiguity 4: Axiom equation labels — architectural vs. source

The taxonomy §1 invariants and §3 skeleton use label names `eq:axiom1_impedance`, `eq:axiom2_alpha`, etc. that do not exist in the LaTeX source. The Four Fundamental Axioms section has 3 unlabelled resultboxes. The distiller must either: (a) invent anchors (e.g., HTML `id` attributes in Markdown) using these architecture-defined names, or (b) use positional references (Axiom 1, Axiom 2, etc.). The coordinator should specify the anchor convention.

### Ambiguity 5: `04_physics_engine_architecture.tex` in backmatter — no skeleton slot

`manuscript/backmatter/04_physics_engine_architecture.tex` exists on disk but has no corresponding leaf in the `common/` skeleton. The taxonomy §3 lists 5 backmatter appendices; there are 6 backmatter files (01, 02, 03, 04, 05, 12). File 04 has no slot. The coordinator must decide whether to add `physics-engine-architecture.md` to `common/` or exclude this file.

### Ambiguity 6: Taxonomy §3 leaf count vs. skeleton in task prompt

The task prompt skeleton lists 46 vol1 leaves (counting index files separately). The taxonomy §3 table lists: 6 ch1 leaves + 5 ch2 leaves + 9 ch3 leaves + 7 ch4 leaves + 4 ch5 leaves + 8 ch6 leaves + 5 ch7 leaves + 1 ch0 leaf = **45 leaves**, matching the taxonomy §8 summary. The task-prompt skeleton is consistent with this count. No discrepancy requiring action.

### Ambiguity 7: `common/` leaf `translation_protein_solver.tex`

Vol 1 does not `\input` any translation tables in its chapter files (confirmed: no `\input{../common/translation_*}` in any vol_1 chapter). The protein and protein_solver tables are clearly Vol 5 domain content. The coordinator should confirm that `common/` is the right home for protein tables (vs. a Vol 5 subtree), and clarify which volumes' input chains include which translation files.
