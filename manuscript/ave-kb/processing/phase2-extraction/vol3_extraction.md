# Vol 3 — Phase 2 Extraction

**Volume:** Applied Vacuum Engineering, Volume III — The Macroscopic Continuum
**Source root:** `manuscript/vol_3_macroscopic/`
**Taxonomy reference:** `.claude/phase1-taxonomy/vol3_taxonomy.md`
**Extraction date:** 2026-04-02
**Status:** Complete — all skeleton positions mapped

---

## Source Directory Listing

```
vol_3_macroscopic/
  main.tex
  frontmatter/
    00_title.tex
  chapters/
    _manifest.tex
    01_gravity_and_yield.tex           (196 lines)
    02_general_relativity_and_gravity.tex (167 lines)
    03_macroscopic_relativity.tex      (196 lines)
    04_generative_cosmology.tex        (149 lines)
    05_cosmology_dark_sector.tex       (156 lines)
    06_solar_system.tex                (190 lines)
    07_stellar_interiors.tex           (147 lines)
    08_gravitational_waves.tex         (123 lines)
    09_condensed_matter_superconductivity.tex (262 lines)
    10_macroscopic_material_properties.tex (194 lines)
    11_thermodynamics_and_entropy.tex  (341 lines)
    12_ideal_gas_law_and_fluid_pressure.tex (99 lines)
    13_geophysics.tex                  (102 lines)
    14_macroscopic_orbital_mechanics.tex (171 lines)
    15_black_hole_orbital_resonance.tex (339 lines)
```

Note: `06_condensed_matter.tex` is absent; its content was merged into `09_condensed_matter_superconductivity.tex` (confirmed in `_manifest.tex` comment).

---

## Domain Structure (from source)

| Domain (KB slug) | Source chapters | Chapter labels |
|---|---|---|
| `gravity` | Ch.1, 2, 3, 8 | `ch:gravity_and_yield`, `ch:general_relativity`, `ch:relativity`, `ch:gravitational_waves` |
| `cosmology` | Ch.4, 5, 6, 14, 15 | `ch:cosmology`, `ch:cosmology_v7`, `ch:solar_system`, `ch:orbital_mechanics`, `ch:bh_orbitals` |
| `condensed-matter` | Ch.9, 10, 11 | `ch:condensed_matter`, `ch:derived_properties`, `ch:thermodynamics` |
| `applied-physics` | Ch.7, 12, 13 | `ch:stellar`, `ch:ideal_gas_law`, `ch:geophysics` |

---

## Skeleton-to-Source Mapping

### Domain: gravity

**Ch.1 Gravity and Yield:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/gravity/ch01-gravity-yield/index.md` | `01_gravity_and_yield.tex` | `\chapter{}`, `\label{ch:gravity_and_yield}` | 1–3 | Index node |
| `vol3/gravity/ch01-gravity-yield/topological-packing-fraction.md` | `01_gravity_and_yield.tex` | `\resultbox{Topological Packing Fraction}` | 9–13 | `p^* = 8\pi\alpha \approx 0.1834` |
| `vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md` | `01_gravity_and_yield.tex` | `\resultbox{Vacuum Poisson Ratio}` | 17–21 | `\nu_{vac} = 2/7`; INVARIANT |
| `vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md` | `01_gravity_and_yield.tex` | `\resultbox{The 1/7 Isotropic Impedance Projection}` | 70–74 | INVARIANT |
| `vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md` | `01_gravity_and_yield.tex` | `\resultbox{The Asymptotic Hubble Constant}` | 94–98 | INVARIANT `H_\infty = 28\pi m_e^3 c G / \hbar^2 \alpha^2` |
| `vol3/gravity/ch01-gravity-yield/gravitational-coupling-constant.md` | `01_gravity_and_yield.tex` | `\resultbox{Gravitational Coupling Constant}` | 104–108 | `G = \hbar c / 7\xi m_e^2` |
| `vol3/gravity/ch01-gravity-yield/planck-mass.md` | `01_gravity_and_yield.tex` | `\resultbox{The Planck Mass}` | 122–126 | `m_P = m_e\sqrt{7\xi}` |
| `vol3/gravity/ch01-gravity-yield/kinetic-yield-threshold.md` | `01_gravity_and_yield.tex` | `\resultbox{The Kinetic Yield Threshold}` | 156–160 | `E_k = \sqrt{\alpha} m_e c^2 \approx 43.65` keV |
| `vol3/gravity/ch01-gravity-yield/static-nodal-tension.md` | `01_gravity_and_yield.tex` | `\resultbox{Static Nodal Tension}` | 168–172 | `T_{static} = m_e c^2 / (2\pi \ell_{node})` |
| `vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md` | `01_gravity_and_yield.tex` | `\subsection{The Mechanism of Trace-Reversal}` + `\subsection{EMT Verification}` | 23–38 | Under `\section{Chiral LC Trace-Reversal}` |
| `vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md` | `01_gravity_and_yield.tex` | `\section{Macroscopic Gravity as Optical Refraction}` | 40–147 | Contains 6 intermediate resultboxes (Volumetric Impedance Trace, Trace-Reversed Volume Fraction, Machian Hierarchy Coupling, Scale of the Universe, Dimensionless Scale, Physical Causal Horizon) — see Ambiguities §1 |
| `vol3/gravity/ch01-gravity-yield/leaky-cavity-decay.md` | `01_gravity_and_yield.tex` | `\section{Microscopic Point-Yield}` (l.148) + `\subsection{The "Leaky Cavity" Mechanism}` (l.176) | 148–181 | |
| `vol3/gravity/ch01-gravity-yield/remaining-ch01-results.md` | `01_gravity_and_yield.tex` | 6 intermediate resultboxes embedded in `optical-refraction-gravity.md` | 54–144 | **REDUNDANT** — see Ambiguities §1 |

**Ch.2 General Relativity:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/gravity/ch02-general-relativity/index.md` | `02_general_relativity_and_gravity.tex` | `\label{ch:general_relativity}` | 1–4 | Index node |
| `vol3/gravity/ch02-general-relativity/einstein-field-equation.md` | `02_general_relativity_and_gravity.tex` | `\resultbox{Einstein Field Equation}` | 13–17 | |
| `vol3/gravity/ch02-general-relativity/stress-energy-lc-density.md` | `02_general_relativity_and_gravity.tex` | `\resultbox{Stress-Energy as LC Energy Density}` | 20–24 | `T_{\mu\nu} \equiv U_{\mu\nu}` |
| `vol3/gravity/ch02-general-relativity/gravitational-refractive-index-gradient.md` | `02_general_relativity_and_gravity.tex` | `\resultbox{Gravitational Refractive Index Gradient}` | 80–84 | `n(r) = (1 + r_s/2r)^3 / (1 - r_s/2r)` |
| `vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md` | `02_general_relativity_and_gravity.tex` | `\resultbox{Frame-Dragging Impedance Convolution}` | 88–92 | `\omega(r) = 2Mar/(r^2+a^2)^2` |
| `vol3/gravity/ch02-general-relativity/k4-tlm-lensing-validation.md` | `02_general_relativity_and_gravity.tex` | `\section{K4-TLM Gravitational Lensing Cross-Validation}`, `\label{sec:k4_tlm_lensing}` | 112–140 | OUTBOUND ref to `sec:k4_tlm` Vol.4 confirmed at **line 115** |
| `vol3/gravity/ch02-general-relativity/gr-ave-translation-dictionary.md` | `02_general_relativity_and_gravity.tex` | `\section{GR $\leftrightarrow$ AVE Translation Dictionary}`, `\label{sec:gr_ave_translation}` | 142–149 | Inputs `../common/translation_gravity.tex` and `../common/translation_cosmology.tex` |
| *(gap)* | `02_general_relativity_and_gravity.tex` | `\resultbox{Symmetric Gravity Impedance}` (l.27-33), GW Regime table (l.55-68) | 27–68 | **GAP** — unassigned; see Gaps § |

**Ch.3 Macroscopic Relativity:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/gravity/ch03-macroscopic-relativity/index.md` | `03_macroscopic_relativity.tex` | `\label{ch:relativity}` | 1–5 | Index node |
| `vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md` | `03_macroscopic_relativity.tex` | `\resultbox{Gordon Optical Metric}` | 18–22 | `g_{\mu\nu}^{AVE} = \eta_{\mu\nu} + (1 - 1/n^2) u_\mu u_\nu` |
| `vol3/gravity/ch03-macroscopic-relativity/newtonian-gravity-optical-gradient.md` | `03_macroscopic_relativity.tex` | `\resultbox{Newtonian Gravity from Optical Gradient}` | 54–58 | |
| `vol3/gravity/ch03-macroscopic-relativity/transverse-refractive-index.md` | `03_macroscopic_relativity.tex` | `\resultbox{Transverse Refractive Index}` | 77–81 | |
| `vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md` | `03_macroscopic_relativity.tex` | `\resultbox{The Refractive Index of Gravity}` | 85–89 | `n(r) = 1 + 2GM/c^2 r`; INVARIANT |
| `vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md` | `03_macroscopic_relativity.tex` | `\subsection{Achromatic Impedance Matching}`, `\label{sec:achromatic_matching}` | 114–132 | |
| `vol3/gravity/ch03-macroscopic-relativity/einstein-lensing-deflection.md` | `03_macroscopic_relativity.tex` | `\resultbox{Einstein Lensing Deflection}` | 137–141 | `\delta = 4GM / b c^2` |
| `vol3/gravity/ch03-macroscopic-relativity/dielectric-rupture-event-horizon.md` | `03_macroscopic_relativity.tex` | `\section{The Event Horizon as Dielectric Rupture}`, `\label{sec:dielectric_rupture}` | 156–165 | |
| `vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md` | `03_macroscopic_relativity.tex` | `\section{The Ponderomotive Equivalence Principle}` | 40–60 | Boundary note: 2 resultboxes at l.26-38 appear in the preceding section — see Ambiguities §4 |
| `vol3/gravity/ch03-macroscopic-relativity/cauchy-implosion-resolution.md` | `03_macroscopic_relativity.tex` | `\section{Resolving the Cauchy Implosion Paradox}` | 144–154 | Short prose section |
| `vol3/gravity/ch03-macroscopic-relativity/gravitomagnetism-frame-dragging.md` | `03_macroscopic_relativity.tex` | `\section{Gravitomagnetism: Frame Dragging as Mutual Inductance}`, `\label{sec:gravitomagnetism_viscosity}` | 167–180 | |

**Ch.8 Gravitational Waves:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/gravity/ch08-gravitational-waves/index.md` | `08_gravitational_waves.tex` | `\label{ch:gravitational_waves}` | 1–5 | Index node |
| `vol3/gravity/ch08-gravitational-waves/invariant-gravitational-impedance.md` | `08_gravitational_waves.tex` | `\resultbox{Invariant Gravitational Impedance}`, `\label{eq:Z_grav}` | 17–22 | `Z(r) = Z_0` (invariant) |
| `vol3/gravity/ch08-gravitational-waves/gw-impedance-perturbation.md` | `08_gravitational_waves.tex` | `\resultbox{GW-Induced Impedance Perturbation}` | 62–64 | `\delta Z = Z_0 \cdot h` |
| `vol3/gravity/ch08-gravitational-waves/ligo-gw-saturation-ratio.md` | `08_gravitational_waves.tex` | `\resultbox{LIGO GW Saturation Ratio}` | 100–103 | `V_{GW}/V_{snap} \approx 1.4 \times 10^{-28}` |
| `vol3/gravity/ch08-gravitational-waves/standard-quantum-limit.md` | `08_gravitational_waves.tex` | `\resultbox{Standard Quantum Limit (Strain)}` | 80–83 | |
| `vol3/gravity/ch08-gravitational-waves/fabry-perot-phase-shift.md` | `08_gravitational_waves.tex` | `\resultbox{Fabry-Pérot Accumulated Phase Shift}` | 68–72 | |
| `vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md` | `08_gravitational_waves.tex` | `\section{GW Propagation as Impedance Modulation}`, `\label{sec:gw_propagation}` | 7–52 | Note: GW regime table is in Ch.2 source (l.54-68), NOT Ch.8 — see Anomalies § |
| `vol3/gravity/ch08-gravitational-waves/gw-detection-antenna.md` | `08_gravitational_waves.tex` | `\section{GW Detection: The Impedance Antenna}`, `\label{sec:gw_detection}` | 55–107 | Full detection section |

---

### Domain: cosmology

**Ch.4 Generative Cosmology:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/cosmology/ch04-generative-cosmology/index.md` | `04_generative_cosmology.tex` | `\label{ch:cosmology}` | 1–4 | Index node |
| `vol3/cosmology/ch04-generative-cosmology/asymptotic-expansion-limit.md` | `04_generative_cosmology.tex` | `\resultbox{Asymptotic Expansion Limit}` | 11–15 | |
| `vol3/cosmology/ch04-generative-cosmology/phantom-energy-equation-of-state.md` | `04_generative_cosmology.tex` | `\resultbox{Phantom Energy Equation of State}` | 52–56 | |
| `vol3/cosmology/ch04-generative-cosmology/jwst-constraint-equation.md` | `04_generative_cosmology.tex` | `\resultbox{JWST Constraint Equation}` | 96–100 | |
| `vol3/cosmology/ch04-generative-cosmology/mutual-inductive-accretion-time-constant.md` | `04_generative_cosmology.tex` | `\resultbox{Mutual Inductive Accretion Time Constant}` | 101–104 | `\tau_{ind} \approx 65.1` Myr |
| `vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md` | `04_generative_cosmology.tex` | `\section{Lattice Genesis}` + `\subsection{Verification: Resolving the Hubble Tension}` | 5–41 | |
| `vol3/cosmology/ch04-generative-cosmology/cmb-thermal-attractor.md` | `04_generative_cosmology.tex` | `\section{The CMB as an Asymptotic Thermal Attractor}` | 63–81 | |
| `vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md` | `04_generative_cosmology.tex` | `\section{Black Holes and The Absolute Impedance Mismatch}` | 116–133 | |
| `vol3/cosmology/ch04-generative-cosmology/remaining-ch04-results.md` | `04_generative_cosmology.tex` | Placeholder | Various | Taxonomy says survey count 8; source has 6. Placeholder will be empty — see Anomalies § |

**Ch.5 Dark Sector (`\label{ch:cosmology_v7}`):**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/cosmology/ch05-dark-sector/index.md` | `05_cosmology_dark_sector.tex` | `\label{ch:cosmology_v7}` | 1–6 | Source label is `ch:cosmology_v7` |
| `vol3/cosmology/ch05-dark-sector/derived-mond-acceleration-scale.md` | `05_cosmology_dark_sector.tex` | `\resultbox{Derived MOND Acceleration Scale ($a_0$)}`, `\label{eq:a0_derived}` | 10–16 | `a_0 = c H_\infty / 2\pi`; INVARIANT |
| `vol3/cosmology/ch05-dark-sector/saturated-lattice-mutual-inductance.md` | `05_cosmology_dark_sector.tex` | `\resultbox{Saturated Lattice Mutual Inductance}`, `\label{eq:galactic_inductance}` | 22–28 | |
| `vol3/cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md` | `05_cosmology_dark_sector.tex` | `\resultbox{Effective Galactic Acceleration (Axiom 4 MOND)}`, `\label{eq:saturation_mond}` | 32–38 | |
| `vol3/cosmology/ch05-dark-sector/mcgaugh-empirical-rar.md` | `05_cosmology_dark_sector.tex` | `\resultbox{McGaugh Empirical RAR}`, `\label{eq:rar_mcgaugh}` | 83–88 | |
| `vol3/cosmology/ch05-dark-sector/asymptotic-limits.md` | `05_cosmology_dark_sector.tex` | `\section{Asymptotic Limits}` + `\section{Regime Identification}`, `\label{sec:galactic_regimes}` | 40–66 | |
| `vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md` | `05_cosmology_dark_sector.tex` | `\section{Multi-Galaxy Validation}`, `\label{sec:multi_galaxy}` | 96–130 | |

**Ch.6 Solar System:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/cosmology/ch06-solar-system/index.md` | `06_solar_system.tex` | `\label{ch:solar_system}` | 1–6 | Index node |
| `vol3/cosmology/ch06-solar-system/heliospheric-impedance-profile.md` | `06_solar_system.tex` | `\resultbox{Heliospheric Impedance Profile}`, `\label{sec:solar_impedance}` | 7–20 | |
| `vol3/cosmology/ch06-solar-system/oumuamua-acceleration.md` | `06_solar_system.tex` | `\resultbox{'Oumuamua Non-Gravitational Acceleration}`, `\label{sec:oumuamua}` | 22–37 | |
| `vol3/cosmology/ch06-solar-system/oort-cloud-saturation-boundary.md` | `06_solar_system.tex` | `\resultbox{Oort Cloud Saturation Boundary}`, `\label{sec:oort_cloud}` | 39–54 | |
| `vol3/cosmology/ch06-solar-system/planetary-magnetopause-standoff.md` | `06_solar_system.tex` | `\resultbox{Planetary Magnetopause Standoff}`, `\label{sec:planetary_magnetosphere}` | 79–95 | |
| `vol3/cosmology/ch06-solar-system/chapman-ferraro-enhancement.md` | `06_solar_system.tex` | `\resultbox{Chapman-Ferraro Boundary Enhancement}` | 101–105 | |
| `vol3/cosmology/ch06-solar-system/dipole-loss-cone-fraction.md` | `06_solar_system.tex` | `\resultbox{Dipole Loss Cone Trapped Fraction}` | 114–118 | |
| `vol3/cosmology/ch06-solar-system/kirkwood-gaps-cavity-modes.md` | `06_solar_system.tex` | `\section{Kirkwood Gaps as Cavity Modes}`, `\label{sec:kirkwood}` | 56–77 | |
| `vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md` | `06_solar_system.tex` | `\subsection{Standing Wave Enhancement}` through Results | 97–155 | |

**Ch.14 Orbital Mechanics:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/cosmology/ch14-orbital-mechanics/index.md` | `14_macroscopic_orbital_mechanics.tex` | `\label{ch:orbital_mechanics}` | 1–5 | Index node |
| `vol3/cosmology/ch14-orbital-mechanics/anomalous-perihelion-advance.md` | `14_macroscopic_orbital_mechanics.tex` | `\resultbox{Anomalous Perihelion Advance}` | 62–66 | |
| `vol3/cosmology/ch14-orbital-mechanics/macroscopic-avalanche-transconductance.md` | `14_macroscopic_orbital_mechanics.tex` | `\resultbox{Macroscopic Avalanche Transconductance}` | 122–126 | Boundary overlap with solar-flares leaf — see Ambiguities §3 |
| `vol3/cosmology/ch14-orbital-mechanics/saturn-ring-integrator.md` | `14_macroscopic_orbital_mechanics.tex` | `\section{The Saturn Ring Integrator}`, `\label{sec:saturn_rings}` | 22–49 | |
| `vol3/cosmology/ch14-orbital-mechanics/solar-flares-led-avalanche.md` | `14_macroscopic_orbital_mechanics.tex` | `\section{Stellar Magnetic Topology and Solar Flares}` + subsections | 77–152 | |
| `vol3/cosmology/ch14-orbital-mechanics/orbital-regime-table.md` | `14_macroscopic_orbital_mechanics.tex` | `\subsection*{Regime Classification of Orbital Domains}` | 6–20 | Unnumbered; **no `\label`** |

**Ch.15 Black Hole Orbitals:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/cosmology/ch15-black-hole-orbitals/index.md` | `15_black_hole_orbital_resonance.tex` | `\label{ch:bh_orbitals}` | 1–4 | Index node |
| `vol3/cosmology/ch15-black-hole-orbitals/qpo-frequency-impedance-resonance.md` | `15_black_hole_orbital_resonance.tex` | `\resultbox{QPO Frequency from Impedance Resonance}` | 73–77 | |
| `vol3/cosmology/ch15-black-hole-orbitals/hawking-temperature-nyquist-noise.md` | `15_black_hole_orbital_resonance.tex` | `\resultbox{Hawking Temperature as Impedance Noise}`, `\label{sec:hawking_emission}` | 112–116 | |
| `vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md` | `15_black_hole_orbital_resonance.tex` | `\resultbox{AVE Merger Ringdown Eigenvalue}` | 156–161 | `\omega_R M_g = 18/49 = 0.3673`; INVARIANT |
| `vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md` | `15_black_hole_orbital_resonance.tex` | `\resultbox{QNM Quality Factor from Lattice Phase Transition}` | 268–272 | `Q = \ell`; INVARIANT |
| `vol3/cosmology/ch15-black-hole-orbitals/ave-compactness-limit.md` | `15_black_hole_orbital_resonance.tex` | `\resultbox{AVE Compactness Limit}`, `\label{sec:compactness_limit}` | 302–306 | `2GM/c^2 R < 2/7`; INVARIANT |
| `vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md` | `15_black_hole_orbital_resonance.tex` | `\section{The Electron--Black Hole Isomorphism}` + subsections | 6–47 | |
| `vol3/cosmology/ch15-black-hole-orbitals/accretion-disk-resonance.md` | `15_black_hole_orbital_resonance.tex` | `\section{Quantised Accretion Disk Resonance}` + subsections | 49–86 | |
| `vol3/cosmology/ch15-black-hole-orbitals/constructive-destructive-paradox.md` | `15_black_hole_orbital_resonance.tex` | `\section{The Constructive vs. Destructive Paradox}` | 88–97 | |
| `vol3/cosmology/ch15-black-hole-orbitals/cross-scale-emission.md` | `15_black_hole_orbital_resonance.tex` | `\section{Cross-Scale Emission}`, `\label{sec:cross_scale_emission}` | 123–142 | |
| `vol3/cosmology/ch15-black-hole-orbitals/first-principles-predictions.md` | `15_black_hole_orbital_resonance.tex` | `\section{Untapped First-Principles Predictions}` | 144–243 | Large composite leaf: Kerr QF, Iron Kα, Jet, GW Memory, EHT Shadow |
| `vol3/cosmology/ch15-black-hole-orbitals/axiom-coverage-audit.md` | `15_black_hole_orbital_resonance.tex` | `\section{Axiom Coverage Audit}` | 245–291 | |
| `vol3/cosmology/ch15-black-hole-orbitals/remaining-ch15-results.md` | `15_black_hole_orbital_resonance.tex` | 4 unassigned resultboxes | Various | |

---

### Domain: condensed-matter

**Ch.9 Condensed Matter and Superconductivity:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/condensed-matter/ch09-condensed-matter-superconductivity/index.md` | `09_condensed_matter_superconductivity.tex` | `\label{ch:condensed_matter}` | 1–4 | Index node |
| `vol3/condensed-matter/ch09-condensed-matter-superconductivity/kuramoto-phase-locking.md` | `09_condensed_matter_superconductivity.tex` | `\resultbox{The Kuramoto Phase-Locking Condition}` | 24–28 | |
| `vol3/condensed-matter/ch09-condensed-matter-superconductivity/inertial-london-penetration-depth.md` | `09_condensed_matter_superconductivity.tex` | `\resultbox{The Inertial London Penetration Depth}` | 73–77 | |
| `vol3/condensed-matter/ch09-condensed-matter-superconductivity/superconductor-type-classification.md` | `09_condensed_matter_superconductivity.tex` | `\resultbox{Superconductor Type Classification}`, `\label{sec:type_classification}` | 153–158 | |
| `vol3/condensed-matter/ch09-condensed-matter-superconductivity/critical-field-validation.md` | `09_condensed_matter_superconductivity.tex` | `\resultbox{Critical Field Validation}`, `\label{sec:superconductor_validation}` | 179–193 | 4-material validation table |
| `vol3/condensed-matter/ch09-condensed-matter-superconductivity/superconductor-catalog-predictions.md` | `09_condensed_matter_superconductivity.tex` | `\section{Superconductor Catalog: AVE Engine Predictions}` | 81–116 | |
| `vol3/condensed-matter/ch09-condensed-matter-superconductivity/meissner-gear-train.md` | `09_condensed_matter_superconductivity.tex` | `\section{The Meissner Effect: A Phase-Locked Gear Train}` | 48–79 | |
| `vol3/condensed-matter/ch09-condensed-matter-superconductivity/bcs-alternative-framework.md` | `09_condensed_matter_superconductivity.tex` | `\section{Alternative to the BCS Framework}` + `\section{Superconductivity as Kinematic Phase-Lock}` | 4–46 | |
| `vol3/condensed-matter/ch09-condensed-matter-superconductivity/universal-saturation-operator.md` | `09_condensed_matter_superconductivity.tex` | `\section{The Universal Saturation Operator}`, `\label{sec:superconductivity_duality}` | 118–147 | |
| `vol3/condensed-matter/ch09-condensed-matter-superconductivity/cm-ave-translation.md` | `09_condensed_matter_superconductivity.tex` | `\section{Condensed Matter $\leftrightarrow$ AVE Translation Dictionary}`, `\label{sec:cm_ave_translation}` | 240–245 | Pointer to `ave-kb/common/translation-tables.md` |

**Ch.10 Material Properties:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/condensed-matter/ch10-material-properties/index.md` | `10_macroscopic_material_properties.tex` | `\label{ch:derived_properties}` | 1–4 | Index node |
| `vol3/condensed-matter/ch10-material-properties/nuclear-hessian.md` | `10_macroscopic_material_properties.tex` | `\resultbox{Nuclear Hessian}`, `\label{eq:hessian}` | 97–102 | |
| `vol3/condensed-matter/ch10-material-properties/inter-element-reflection-coefficient.md` | `10_macroscopic_material_properties.tex` | `\resultbox{Inter-Element Reflection Coefficient}`, `\label{eq:gamma_inter}` | 167–172 | |
| `vol3/condensed-matter/ch10-material-properties/helium-metamaterial-paradox.md` | `10_macroscopic_material_properties.tex` | `\subsection*{The Helium Metamaterial Paradox}` | 14–19 | No `\label` |
| `vol3/condensed-matter/ch10-material-properties/diamond-hardness-alpha-clusters.md` | `10_macroscopic_material_properties.tex` | `\section{Quantitative Hardness: Diamond from Alpha Clusters}` | 53–72 | |
| `vol3/condensed-matter/ch10-material-properties/metallicity-magnetic-asymmetry.md` | `10_macroscopic_material_properties.tex` | `\section{Metallicity from Magnetic Asymmetry}` | 74–83 | |
| `vol3/condensed-matter/ch10-material-properties/per-element-impedance-table.md` | `10_macroscopic_material_properties.tex` | `\section{Single-Element Impedance Under Stress}`, `\label{sec:element_impedance}` | 85–194 | |

**Ch.11 Thermodynamics:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/condensed-matter/ch11-thermodynamics/index.md` | `11_thermodynamics_and_entropy.tex` | `\label{ch:thermodynamics}` | 1–3 | Index node; surfaces Vol5 and Vol7 outbound refs |
| `vol3/condensed-matter/ch11-thermodynamics/macroscopic-temperature-lc-noise.md` | `11_thermodynamics_and_entropy.tex` | `\resultbox{Macroscopic Temperature as LC Noise}` | 13–17 | |
| `vol3/condensed-matter/ch11-thermodynamics/vacuum-nyquist-baseline.md` | `11_thermodynamics_and_entropy.tex` | `\resultbox{The Vacuum Nyquist Baseline}`, `\label{eq:vacuum_nyquist}` | 57–62 | |
| `vol3/condensed-matter/ch11-thermodynamics/effective-dof-g-star.md` | `11_thermodynamics_and_entropy.tex` | `\resultbox{The Effective Degrees of Freedom ($g_*$)}`, `\label{eq:g_star}` | 127–132 | `g_* = 7^3/4 = 85.75`; INVARIANT |
| `vol3/condensed-matter/ch11-thermodynamics/vacuum-heat-capacity.md` | `11_thermodynamics_and_entropy.tex` | `\resultbox{Vacuum Volumetric Heat Capacity}`, `\label{eq:heat_capacity}` | 147–152 | |
| `vol3/condensed-matter/ch11-thermodynamics/baryon-asymmetry.md` | `11_thermodynamics_and_entropy.tex` | `\resultbox{The Baryon Asymmetry}`, `\label{eq:baryon_asymmetry}` | 159–164 | `\eta = 6.08 \times 10^{-10}`; INVARIANT |
| `vol3/condensed-matter/ch11-thermodynamics/thermal-softening-correction.md` | `11_thermodynamics_and_entropy.tex` | `\resultbox{Thermal Softening Correction}`, `\label{eq:thermal_kappa}` + `\resultbox{Residual Thermal RMS Correction}`, `\label{eq:delta_th}` | 177–211 | Two resultboxes; split from thermal-softening-skyrme — see Ambiguities §5 |
| `vol3/condensed-matter/ch11-thermodynamics/casimir-effective-temperature.md` | `11_thermodynamics_and_entropy.tex` | `\resultbox{Casimir Effective Temperature}`, `\label{eq:casimir_temperature}` | 250–255 | |
| `vol3/condensed-matter/ch11-thermodynamics/entropy-redefinition.md` | `11_thermodynamics_and_entropy.tex` | `\section{The Redefinition of Entropy}` + `\section{Geometric Scattering and Thermal Jitter}` | 4–32 | |
| `vol3/condensed-matter/ch11-thermodynamics/arrow-of-time.md` | `11_thermodynamics_and_entropy.tex` | `\section{The Arrow of Time}` | 33–38 | Short prose |
| `vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md` | `11_thermodynamics_and_entropy.tex` | `\section{The Fluctuation-Dissipation Theorem}`, `\label{sec:fluctuation_dissipation}` | 40–83 | |
| `vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md` | `11_thermodynamics_and_entropy.tex` | `\subsection{Application: Transmon Qubit Decoherence}` + `\subsection{Ohmic Damping}` | 85–108 | `\ref{ch:quantum_computing}` dangling |
| `vol3/condensed-matter/ch11-thermodynamics/mode-counting-heat-capacity.md` | `11_thermodynamics_and_entropy.tex` | `\section{Mode Counting and Heat Capacity}`, `\label{sec:mode_counting}` | 110–154 | |
| `vol3/condensed-matter/ch11-thermodynamics/baryon-asymmetry-derivation.md` | `11_thermodynamics_and_entropy.tex` | `\subsection{Verification: Baryon Asymmetry}` | 156–165 | |
| `vol3/condensed-matter/ch11-thermodynamics/thermal-softening-skyrme.md` | `11_thermodynamics_and_entropy.tex` | `\section{Thermal Softening of Topological Structures}`, `\label{sec:thermal_softening_thermo}` | 167–224 | Full section prose; see split ambiguity §5 |
| `vol3/condensed-matter/ch11-thermodynamics/phase-transitions-impedance.md` | `11_thermodynamics_and_entropy.tex` | `\section{Phase Transitions as Impedance Matching Events}`, `\label{sec:phase_transitions}` | 226–256 | |
| `vol3/condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md` | `11_thermodynamics_and_entropy.tex` | `\subsection{Fluid Anomalies: The Two-State LC Partition Framework}`, `\label{sec:water_partition}` | 258–288 | **OUTBOUND** `sec:hbond_derivation` at **line 267**, `sec:melting_eigenmode` at **line 278** — CONFIRMED |
| `vol3/condensed-matter/ch11-thermodynamics/phase-transition-classification.md` | `11_thermodynamics_and_entropy.tex` | `\subsection{General Classification}` | 290–309 | |
| `vol3/condensed-matter/ch11-thermodynamics/ch11-remaining-resultboxes.md` | `11_thermodynamics_and_entropy.tex` | 8 unassigned resultboxes | Various | Placeholder |

---

### Domain: applied-physics

**Ch.7 Stellar Interiors:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/applied-physics/ch07-stellar-interiors/index.md` | `07_stellar_interiors.tex` | `\label{ch:stellar}` | 1–4 | Index node; `\ref{ch:regime_map}` dangling |
| `vol3/applied-physics/ch07-stellar-interiors/neutrino-msw-matter-potential.md` | `07_stellar_interiors.tex` | `\resultbox{Neutrino MSW Matter Potential}`, `\label{sec:neutrino_msw}` | 88–92 | |
| `vol3/applied-physics/ch07-stellar-interiors/msw-resonance-critical-density.md` | `07_stellar_interiors.tex` | `\resultbox{MSW Resonance Critical Density}` | 94–97 | |
| `vol3/applied-physics/ch07-stellar-interiors/stellar-regime-classification.md` | `07_stellar_interiors.tex` | `\section{Stellar Regime Classification}`, `\label{sec:stellar_regimes}` | 7–29 | |
| `vol3/applied-physics/ch07-stellar-interiors/stellar-interior-impedance-profiles.md` | `07_stellar_interiors.tex` | `\section{Stellar Interiors as Impedance Profiles}`, `\label{sec:stellar_interior}` | 31–73 | |
| `vol3/applied-physics/ch07-stellar-interiors/neutrino-flavor-mixing.md` | `07_stellar_interiors.tex` | `\section{Neutrino MSW: Flavor Mixing as Impedance Mode Coupling}` | 75–131 | |

**Ch.12 Ideal Gas Law:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/applied-physics/ch12-ideal-gas-law/index.md` | `12_ideal_gas_law_and_fluid_pressure.tex` | `\label{ch:ideal_gas_law}` | 1–4 | Index node |
| `vol3/applied-physics/ch12-ideal-gas-law/ideal-gas-law.md` | `12_ideal_gas_law_and_fluid_pressure.tex` | `\resultbox{The Ideal Gas Law}` | 6–10 | `PV = nRT` |
| `vol3/applied-physics/ch12-ideal-gas-law/lc-energy-balance-equation.md` | `12_ideal_gas_law_and_fluid_pressure.tex` | `\resultbox{The LC Energy Balance Equation}` | 31–35 | |
| `vol3/applied-physics/ch12-ideal-gas-law/gas-dynamics-foundations.md` | `12_ideal_gas_law_and_fluid_pressure.tex` | `\section{Ontological Foundations}` + `\section{Mapping the Equation of State}` | 4–26 | |
| `vol3/applied-physics/ch12-ideal-gas-law/recovering-r-at-stp.md` | `12_ideal_gas_law_and_fluid_pressure.tex` | `\section{Quantitative Verification: Recovering $R$ at STP}` | 48–83 | |

**Ch.13 Geophysics:**

| Skeleton path | Source file | Section/label | Lines | Notes |
|---|---|---|---|---|
| `vol3/applied-physics/ch13-geophysics/index.md` | `13_geophysics.tex` | `\label{ch:geophysics}` | 1–6 | Index node |
| `vol3/applied-physics/ch13-geophysics/seismic-reflection-coefficient-moho.md` | `13_geophysics.tex` | `\resultbox{Seismic Reflection Coefficient (Moho)}`, `\label{sec:seismic_fdtd_bridge}` | 25–30 | |
| `vol3/applied-physics/ch13-geophysics/seismic-fdtd-engine.md` | `13_geophysics.tex` | `\section{Seismic Wave Propagation on the FDTD Engine}` | 7–46 | |
| `vol3/applied-physics/ch13-geophysics/prem-layers-waveguide.md` | `13_geophysics.tex` | `\section{PREM Layer Data}` + `\section{Waveguide Trapping in the Low-Velocity Zone}` | 48–85 | |

---

## Outbound Cross-Reference Confirmation

- **`sec:k4_tlm`**: CONFIRMED at `02_general_relativity_and_gravity.tex`, **line 115**. Text: `"cross-validate the same physics with the K4-TLM native lattice dynamics simulator (Section~\ref{sec:k4_tlm}, Vol.~4)"`. Explicit `Vol.~4` annotation.

- **`sec:hbond_derivation`**: CONFIRMED at `11_thermodynamics_and_entropy.tex`, **line 267**. Text: `"(Vol.~V, Ch.~2, \S\ref{sec:hbond_derivation}: $d_{OO} = 2.727$~\AA)"`. Explicit Vol.5, Ch.2 annotation.

- **`sec:melting_eigenmode`**: CONFIRMED at `11_thermodynamics_and_entropy.tex`, **line 278**. Text: `"see Vol.~VII, Ch.~11, \S\ref{sec:melting_eigenmode}"`. Explicit Vol.7, Ch.11 annotation.

**All three primary outbound references confirmed** with explicit volume annotations in the source.

---

## Ch.11 Thermodynamics — Subsection Count

Ch.11 (341 lines) contains **7 top-level sections + 15 subsections = 22 structural content units** (excluding Summary/exercisebox). The taxonomy's 16-leaf skeleton is a valid decomposition grouping related subsections together.

---

## Empty Skeleton Positions

None confirmed. All skeleton positions have identified source locations.

---

## Gaps

1. **Ch.2 extra resultboxes**: `\resultbox{Symmetric Gravity Impedance}` (l.27-33) and GW Regime Classification table (l.54-68) are unassigned. No `remaining-ch02-results.md` placeholder exists. Recommendation: distiller bundles into `einstein-field-equation.md`.

2. **Ch.4 resultbox count**: Taxonomy says survey count 8; source has 6. `remaining-ch04-results.md` will be empty.

3. **Ch.8 GW Regime table**: The GW regime table (l.54-68) is in `02_general_relativity_and_gravity.tex`, not Ch.8 as implied. Distiller alert needed.

---

## Notation and Macro Notes

| Macro | Markdown translation |
|---|---|
| `\Zvac` | `Z_{vac}` or `Z_0` |
| `\vacuum` | `\mathcal{M}_A` (confirmed INVARIANT) |
| `\planck` | `\hbar` |
| `\permeability` | `\mu_0` |
| `\permittivity` | `\varepsilon_0` |
| `\impedance` | `Z_0` |

Chapter bodies use `\mathcal{M}_A` directly (confirmed at Ch.3 l.150, Ch.11 l.263). No chapter body uses `\vacuum` macro.

---

## Ambiguities

1. **Ch.1 remaining-ch01-results.md scope**: All 6 "remaining" Ch.1 resultboxes are embedded in `optical-refraction-gravity.md`. Placeholder is redundant. Recommend: bundle all 6 into the derivation-chain leaf; mark `remaining-ch01-results.md` empty with `<!-- leaf: placeholder -->`.

2. **Ch.4 empty placeholder**: `remaining-ch04-results.md` will have no content. Mark as placeholder.

3. **`solar-flares-led-avalanche.md` / `macroscopic-avalanche-transconductance.md` overlap (Ch.14)**: The transconductance resultbox is embedded inside the solar-flares section. Resolution: `macroscopic-avalanche-transconductance.md` holds only the resultbox (l.122-126); `solar-flares-led-avalanche.md` holds surrounding prose.

4. **Ch.3 `ponderomotive-equivalence.md` boundary**: Two resultboxes at l.26-38 appear in the preceding section (l.7), before the section title at l.40. Distiller should either extend the leaf boundary to l.7 or reassign to `remaining-ch03-results.md`.

5. **`thermal-softening-correction.md` vs `thermal-softening-skyrme.md`**: Both derive from `\section{Thermal Softening...}` (l.167-224). Clean split: `thermal-softening-correction.md` holds only the two resultbox environments (l.177-211); `thermal-softening-skyrme.md` holds the full section prose. `Axiom 4 Gradient Saturation Kernel` resultbox (l.194-199) belongs to `thermal-softening-skyrme.md`.
