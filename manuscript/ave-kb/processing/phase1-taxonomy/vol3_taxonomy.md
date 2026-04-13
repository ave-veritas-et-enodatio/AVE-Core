# Phase 1 Taxonomy Design — Vol 3: The Macroscopic Continuum

**Volume:** Applied Vacuum Engineering, Volume III
**Chapters:** 15
**Estimated leaves:** 130–140
**Designed by:** kb-taxonomy-architect

---

## 1. CLAUDE.md Invariants

The following content from Vol 3 is genuinely cross-cutting — it appears as foundational constants or notation used across multiple volumes — and belongs in `manuscript/ave-kb/CLAUDE.md` rather than any volume-specific page.

```
INVARIANT: nu_vac — Vacuum Poisson ratio ν_vac = 2/7 (source: ch:gravity_and_yield, resultbox "Vacuum Poisson Ratio")
INVARIANT: impedance_projection — 1/7 isotropic impedance projection factor (source: ch:gravity_and_yield, resultbox "1/7 Isotropic Impedance Projection")
INVARIANT: hubble_asymptote — H_∞ ≈ 69.32 km/s/Mpc, asymptotic Hubble constant (source: ch:gravity_and_yield / ch:cosmology)
INVARIANT: mond_scale — a_0 = c H_∞ / 2π, MOND acceleration scale derived from AVE (source: ch:cosmology_v7 / eq:a0_derived)
INVARIANT: g_star — g* = 7³/4 = 85.75, effective relativistic DoF from lattice geometry (source: ch:thermodynamics, eq:g_star)
INVARIANT: baryon_asymmetry — η = 6.08×10⁻¹⁰, baryon-to-photon ratio (source: ch:thermodynamics, eq:baryon_asymmetry)
INVARIANT: buchdahl_ave — AVE Buchdahl bound: 2GM/c²R < 2/7 (source: ch:bh_orbitals, sec:compactness_limit)
INVARIANT: qnm_eigenvalue — ω_R M_g = 18/49, QNM eigenvalue for BH ringdown (source: ch:bh_orbitals)
INVARIANT: mathcal_M_A — Notation: write $\mathcal{M}_A$ directly; the \vacuum macro resolves to M_A but is NOT used in chapter bodies (source: vol3 survey §3, confirmed cross-volume)
```

**Boundary test applied:** each item above is referenced or depended upon in at least two distinct volume branches of the AVE series (e.g., H_∞ appears in Vol 1 regime map and Vol 3 cosmology; g* is used in Vol 3 thermodynamics and Vol 4 engineering calculations; the $\mathcal{M}_A$ notation rule is confirmed across all 8 volumes). Items that are purely internal to Vol 3 (e.g., the superconductor catalog, Saturn ring integrator) are NOT listed here.

**Not in CLAUDE.md:** The 1/7 projection's derivation, the full translation dictionaries, ch.11 thermodynamic formulae — these live in domain leaves, not CLAUDE.md.

---

## 2. Domain Grouping

Vol 3's 15 chapters divide into four natural domains based on the physical question an agent would pose:

| Domain | Chapters | Rationale |
|---|---|---|
| `gravity` | Ch.1, 2, 3, 8 | Gravity as optical refraction, GR mapping, gravitational waves — unified by the optical/dielectric model of gravity |
| `cosmology` | Ch.4, 5, 6, 14, 15 | Cosmological dynamics, dark sector, solar system, orbital mechanics, black holes — unified by large-scale structure and astrophysical observables |
| `condensed-matter` | Ch.9, 10, 11 | Superconductivity, material properties, thermodynamics — unified by condensed matter physics and the impedance phase-transition framework |
| `applied-physics` | Ch.7, 12, 13 | Stellar interiors, ideal gas law, geophysics — unified by being AVE applied to specific observational/experimental domains |

**Design justification:**

- Ch.6 (Solar System) and Ch.14 (Orbital Mechanics) join `cosmology` rather than forming a standalone `astrophysics` domain. Two chapters do not justify a domain-level split; the solar system and orbital mechanics content is deeply continuous with the cosmological impedance framework developed in Ch.4-5.
- Ch.8 (Gravitational Waves) joins `gravity` because its core content (GW as impedance modulation, LIGO as impedance antenna) is mechanistically the same model as Ch.3's dielectric gravity — an agent asking "how do gravitational waves work in AVE?" navigates to `gravity`, not `cosmology`.
- Ch.9 (Condensed Matter + Superconductivity) carries content merged from the former Ch.6. The KB slug and leaf names reflect the merged chapter as a single unit; the merge history is noted in the chapter index but does not affect hierarchy.
- Ch.11 (Thermodynamics, 341 lines) receives subsection-granularity leaf decomposition. Its cross-volume dependencies on Vol 5 and Vol 7 are surfaced at the chapter index level.

**Depth:** entry-point → vol3 index → domain index → chapter index → leaf. This is exactly 4 levels. No fifth level is introduced. Ch.11's additional leaves remain at level 4.

---

## 3. Document Skeleton

Legend: `[index]` = navigation node; `[leaf — verbatim]` = terminal content, source translated verbatim; `[leaf — placeholder]` = leaf position reserved, source not yet extracted.

```
ave-kb/
  CLAUDE.md                                           [index] — Cross-cutting notation, invariant constants, and conventions applying to ALL volumes; see §1 of this taxonomy for the boundary rule
  entry-point.md                                      [index] — One-paragraph summaries of all 8 volumes with links to each vol index; under 3000 tokens
  common/
    translation-tables.md                             [leaf — verbatim] — Verbatim content of all translation_*.tex files (gravity, cosmology, condensed matter); definitive single location; see §5 of this taxonomy for rationale
  vol3/
    index.md                                          [index] — Vol 3 summary: 15-chapter macroscopic volume; key results per domain; links to 4 domain indexes
    gravity/
      index.md                                        [index] — Domain: optical gravity, GR mapping, gravitational waves; key results from Ch.1-3,8; links to 4 chapter indexes
      ch01-gravity-yield/
        index.md                                      [index] — Ch.1 summary: chiral trace-reversal, 1/7 projection, yield threshold; links to leaves
        topological-packing-fraction.md               [leaf — verbatim] — Resultbox: Topological Packing Fraction derivation
        vacuum-poisson-ratio.md                       [leaf — verbatim] — Resultbox: Vacuum Poisson Ratio ν_vac = 2/7
        one-seventh-impedance-projection.md           [leaf — verbatim] — Resultbox: 1/7 Isotropic Impedance Projection
        asymptotic-hubble-constant.md                 [leaf — verbatim] — Resultbox: Asymptotic Hubble Constant H_∞ ≈ 69.32
        gravitational-coupling-constant.md            [leaf — verbatim] — Resultbox: Gravitational Coupling Constant G = ℏc/7ξm_e²
        planck-mass.md                                [leaf — verbatim] — Resultbox: The Planck Mass from lattice geometry
        kinetic-yield-threshold.md                    [leaf — verbatim] — Resultbox: Kinetic Yield Threshold
        static-nodal-tension.md                       [leaf — verbatim] — Resultbox: Static Nodal Tension
        trace-reversal-mechanism.md                   [leaf — verbatim] — §§ Mechanism of Trace-Reversal; §§ EMT Verification (source: Ch.1 §Chiral LC Trace-Reversal)
        optical-refraction-gravity.md                 [leaf — verbatim] — §§ Unity of Gravity and Expansion (source: Ch.1 §Macroscopic Gravity as Optical Refraction)
        leaky-cavity-decay.md                         [leaf — verbatim] — §§ Leaky Cavity Mechanism; point-yield and particle decay paradox (source: Ch.1 §Microscopic Point-Yield)
        remaining-ch01-results.md                     [leaf — placeholder] — Remaining Ch.1 resultboxes not individually listed above (survey count 14; distiller to enumerate)
      ch02-general-relativity/
        index.md                                      [index] — Ch.2 summary: spacetime curvature as LC, stress-energy tensor, Lense-Thirring, GR↔AVE translation; links to leaves
        einstein-field-equation.md                    [leaf — verbatim] — Resultbox: Einstein Field Equation mapped to AVE
        stress-energy-lc-density.md                   [leaf — verbatim] — Resultbox: Stress-Energy as LC Energy Density
        gravitational-refractive-index-gradient.md    [leaf — verbatim] — Resultbox: Gravitational Refractive Index Gradient
        frame-dragging-impedance-convolution.md       [leaf — verbatim] — Resultbox: Frame-Dragging Impedance Convolution
        k4-tlm-lensing-validation.md                  [leaf — verbatim] — §§ Method; §§ Results (source: Ch.2 §sec:k4_tlm_lensing); OUTBOUND ref to Vol 4 sec:k4_tlm flagged here
        gr-ave-translation-dictionary.md              [leaf — verbatim] — §§ GR↔AVE Translation Dictionary (sec:gr_ave_translation); inputs translation_gravity.tex and translation_cosmology.tex; see also ave-kb/common/translation-tables.md
      ch03-macroscopic-relativity/
        index.md                                      [index] — Ch.3 summary: ponderomotive equivalence, optical metric, event horizon, gravitomagnetism; links to leaves
        gordon-optical-metric.md                      [leaf — verbatim] — Resultbox: Gordon Optical Metric
        newtonian-gravity-optical-gradient.md         [leaf — verbatim] — Resultbox: Newtonian Gravity from Optical Gradient
        transverse-refractive-index.md                [leaf — verbatim] — Resultbox: Transverse Refractive Index
        refractive-index-of-gravity.md                [leaf — verbatim] — Resultbox: The Refractive Index of Gravity; n(r) = 1 + 2GM/c²r
        achromatic-impedance-matching.md              [leaf — verbatim] — Resultbox: Achromatic Impedance Matching (sec:achromatic_matching)
        einstein-lensing-deflection.md                [leaf — verbatim] — Resultbox: Einstein Lensing Deflection
        dielectric-rupture-event-horizon.md           [leaf — verbatim] — Resultbox: Dielectric Rupture (Event Horizon) (sec:dielectric_rupture)
        ponderomotive-equivalence.md                  [leaf — verbatim] — §§ Ponderomotive Equivalence Principle (source: Ch.3 §The Ponderomotive Equivalence Principle)
        cauchy-implosion-resolution.md                [leaf — verbatim] — §§ Resolving the Cauchy Implosion Paradox (source: Ch.3)
        gravitomagnetism-frame-dragging.md            [leaf — verbatim] — §§ Gravitomagnetism: Frame Dragging as Mutual Inductance (sec:gravitomagnetism_viscosity)
        remaining-ch03-results.md                     [leaf — placeholder] — Remaining Ch.3 resultboxes not individually listed (survey count 12; distiller to enumerate)
      ch08-gravitational-waves/
        index.md                                      [index] — Ch.8 summary: GW as impedance modulation, LIGO as impedance antenna; links to leaves
        invariant-gravitational-impedance.md          [leaf — verbatim] — Resultbox: Invariant Gravitational Impedance Z_grav (eq:Z_grav)
        gw-impedance-perturbation.md                  [leaf — verbatim] — Resultbox: GW-Induced Impedance Perturbation
        ligo-gw-saturation-ratio.md                   [leaf — verbatim] — Resultbox: LIGO GW Saturation Ratio
        standard-quantum-limit.md                     [leaf — verbatim] — Resultbox: Standard Quantum Limit
        fabry-perot-phase-shift.md                    [leaf — verbatim] — Resultbox: Fabry-Perot Phase Shift
        gw-propagation-lossless.md                    [leaf — verbatim] — §§ Lossless Propagation (sec:gw_propagation; source: Ch.8 §GW Propagation as Impedance Modulation)
        gw-detection-antenna.md                       [leaf — verbatim] — §§ The Impedance Antenna (sec:gw_detection; source: Ch.8 §GW Detection)
    cosmology/
      index.md                                        [index] — Domain: cosmological expansion, dark sector, solar system, orbital mechanics, black holes; key results from Ch.4-6,14,15; links to 5 chapter indexes
      ch04-generative-cosmology/
        index.md                                      [index] — Ch.4 summary: lattice genesis, dark energy, CMB attractor, JWST paradox, black holes; links to leaves
        asymptotic-expansion-limit.md                 [leaf — verbatim] — Resultbox: Asymptotic Expansion Limit
        phantom-energy-equation-of-state.md           [leaf — verbatim] — Resultbox: Phantom Energy Equation of State
        jwst-constraint-equation.md                   [leaf — verbatim] — Resultbox: JWST Constraint Equation
        mutual-inductive-accretion-time-constant.md   [leaf — verbatim] — Resultbox: Mutual Inductive Accretion Time Constant
        lattice-genesis-hubble-tension.md             [leaf — verbatim] — §§ Resolving the Hubble Tension (source: Ch.4 §Lattice Genesis)
        cmb-thermal-attractor.md                      [leaf — verbatim] — §§ CMB as Asymptotic Thermal Attractor (source: Ch.4)
        black-holes-impedance-mismatch.md             [leaf — verbatim] — §§ Black Holes and The Absolute Impedance Mismatch (source: Ch.4)
        remaining-ch04-results.md                     [leaf — placeholder] — Remaining Ch.4 resultboxes not individually listed (survey count 8; distiller to enumerate)
      ch05-dark-sector/
        index.md                                      [index] — Ch.5 summary (slug: dark-sector, NOT cosmology_v7): MOND from Axiom 4, RAR, multi-galaxy validation, VLBI parallax; links to leaves
        derived-mond-acceleration-scale.md            [leaf — verbatim] — Resultbox: Derived MOND Acceleration Scale a_0 (eq:a0_derived)
        saturated-lattice-mutual-inductance.md        [leaf — verbatim] — Resultbox: Saturated Lattice Mutual Inductance (eq:galactic_inductance)
        effective-galactic-acceleration-mond.md       [leaf — verbatim] — Resultbox: Effective Galactic Acceleration / Axiom 4 MOND (eq:saturation_mond)
        mcgaugh-empirical-rar.md                      [leaf — verbatim] — Resultbox: McGaugh Empirical RAR (eq:rar_mcgaugh; sec:rar)
        asymptotic-limits.md                          [leaf — verbatim] — §§ Asymptotic Limits; §§ Regime Identification (sec:galactic_regimes; source: Ch.5)
        multi-galaxy-validation.md                    [leaf — verbatim] — §§ Multi-Galaxy Validation (sec:multi_galaxy; source: Ch.5)
      ch06-solar-system/
        index.md                                      [index] — Ch.6 summary: heliospheric impedance, 'Oumuamua, Oort cloud, Kirkwood gaps, planetary magnetospheres; links to leaves
        heliospheric-impedance-profile.md             [leaf — verbatim] — Resultbox: Heliospheric Impedance Profile (sec:solar_impedance; eq:heliospheric_Z)
        oumuamua-acceleration.md                      [leaf — verbatim] — Resultbox: 'Oumuamua Non-Gravitational Acceleration (sec:oumuamua; eq:oumuamua_accel)
        oort-cloud-saturation-boundary.md             [leaf — verbatim] — Resultbox: Oort Cloud Saturation Boundary (sec:oort_cloud; eq:oort_saturation)
        planetary-magnetopause-standoff.md            [leaf — verbatim] — Resultbox: Planetary Magnetopause Standoff (sec:planetary_magnetosphere; eq:magnetopause)
        chapman-ferraro-enhancement.md                [leaf — verbatim] — Resultbox: Chapman-Ferraro Boundary Enhancement
        dipole-loss-cone-fraction.md                  [leaf — verbatim] — Resultbox: Dipole Loss Cone Trapped Fraction
        kirkwood-gaps-cavity-modes.md                 [leaf — verbatim] — §§ Kirkwood Gaps as Cavity Modes (sec:kirkwood; source: Ch.6)
        planetary-magnetospheres.md                   [leaf — verbatim] — §§ Standing Wave Enhancement; §§ Internal Plasma Pressure; §§ Jupiter/Io; §§ Uranus Anomaly; §§ Results (source: Ch.6 §Planetary Magnetospheres)
      ch14-orbital-mechanics/
        index.md                                      [index] — Ch.14 summary: regime table, Saturn rings, anomalous precession, solar flares as LED avalanche; links to leaves
        anomalous-perihelion-advance.md               [leaf — verbatim] — Resultbox: Anomalous Perihelion Advance (Mercury and Venus)
        macroscopic-avalanche-transconductance.md     [leaf — verbatim] — Resultbox: Macroscopic Avalanche Transconductance
        saturn-ring-integrator.md                     [leaf — verbatim] — §§ Gravity as Structural Tension; §§ Radial Impedance Bands / Cassini Gaps (sec:saturn_rings; source: Ch.14)
        solar-flares-led-avalanche.md                 [leaf — verbatim] — §§ Tension-Snap; §§ Exact Coronal Physics; §§ Sun as LED; §§ Topological Solar Weather; §§ NOAA GOES Validation (source: Ch.14 §Stellar Magnetic Topology)
        orbital-regime-table.md                       [leaf — verbatim] — Opening regime table (no label; source: Ch.14 before first section)
      ch15-black-hole-orbitals/
        index.md                                      [index] — Ch.15 summary: BH as macroscopic electron orbital, QPO quantisation, Hawking radiation, AVE Buchdahl bound; links to leaves; note OUTBOUND ref to sec:kerr_q_correction (dangling)
        qpo-frequency-impedance-resonance.md          [leaf — verbatim] — Resultbox: QPO Frequency from Impedance Resonance (eq:impedance_quantisation)
        hawking-temperature-nyquist-noise.md          [leaf — verbatim] — Resultbox: Hawking Temperature as Impedance Noise (sec:hawking_emission)
        ave-merger-ringdown-eigenvalue.md             [leaf — verbatim] — Resultbox: AVE Merger Ringdown Eigenvalue; ω_R M_g = 18/49
        qnm-quality-factor.md                        [leaf — verbatim] — Resultbox: QNM Quality Factor
        ave-compactness-limit.md                      [leaf — verbatim] — Resultbox: AVE Compactness Limit (sec:compactness_limit); 2GM/c²R < 2/7
        electron-bh-isomorphism.md                   [leaf — verbatim] — §§ Symmetric Gravity and Saturation; §§ Saturation Boundary as Phase Transition (source: Ch.15 §Electron–BH Isomorphism)
        accretion-disk-resonance.md                  [leaf — verbatim] — §§ Standing-Wave Condition; §§ QPO Frequency Predictions (source: Ch.15 §Quantised Accretion Disk Resonance)
        constructive-destructive-paradox.md          [leaf — verbatim] — §§ Constructive vs Destructive Paradox (source: Ch.15)
        cross-scale-emission.md                      [leaf — verbatim] — §§ Cross-Scale Emission (sec:cross_scale_emission; source: Ch.15)
        first-principles-predictions.md              [leaf — verbatim] — §§ Kerr Quality Factor; §§ Iron Kα Line; §§ Relativistic Jet; §§ GW Memory; §§ EHT Shadow Fine Structure (source: Ch.15 §Untapped First-Principles Predictions)
        axiom-coverage-audit.md                      [leaf — verbatim] — §§ Axiom 4 Saturation: Phase Transition and Q=ℓ (source: Ch.15 §Axiom Coverage Audit)
        remaining-ch15-results.md                    [leaf — placeholder] — Remaining Ch.15 resultboxes not individually listed (survey count 9; distiller to enumerate)
    condensed-matter/
      index.md                                        [index] — Domain: superconductivity, material properties, thermodynamics; key results from Ch.9-11; links to 3 chapter indexes
      ch09-condensed-matter-superconductivity/
        index.md                                      [index] — Ch.9 summary (merged from former ch6+ch9): Kuramoto phase-lock, Meissner effect, type I/II, numerical validation; links to leaves; note merge history
        kuramoto-phase-locking.md                    [leaf — verbatim] — Resultbox: Kuramoto Phase-Locking Condition
        inertial-london-penetration-depth.md         [leaf — verbatim] — Resultbox: Inertial London Penetration Depth
        superconductor-type-classification.md        [leaf — verbatim] — Resultbox: Superconductor Type Classification (sec:type_classification); κ = λ_L/ξ_0
        critical-field-validation.md                [leaf — verbatim] — Resultbox: Critical Field Validation (sec:superconductor_validation)
        superconductor-catalog-predictions.md        [leaf — verbatim] — §§ Superconductor Catalog: AVE Engine Predictions; §§ Regime Classification (source: Ch.9)
        meissner-gear-train.md                       [leaf — verbatim] — §§ The Meissner Effect: A Phase-Locked Gear Train (source: Ch.9)
        bcs-alternative-framework.md                 [leaf — verbatim] — §§ Alternative to BCS Framework; §§ Superconductivity as Kinematic Phase-Lock (source: Ch.9)
        universal-saturation-operator.md             [leaf — verbatim] — §§ Universal Saturation Operator: ε–μ Duality (sec:superconductivity_duality)
        cm-ave-translation.md                        [leaf — verbatim] — §§ Condensed Matter↔AVE Translation (sec:cm_ave_translation); inputs translation_condensed_matter.tex; see also ave-kb/common/translation-tables.md
        remaining-ch09-results.md                    [leaf — placeholder] — Remaining Ch.9 resultboxes not individually listed (survey count 7; distiller to enumerate)
      ch10-material-properties/
        index.md                                      [index] — Ch.10 summary: calculated absolute properties, diamond hardness, metallicity, per-element impedance table; links to leaves
        nuclear-hessian.md                           [leaf — verbatim] — Resultbox: Nuclear Hessian (eq:hessian)
        inter-element-reflection-coefficient.md     [leaf — verbatim] — Resultbox: Inter-Element Reflection Coefficient (eq:gamma_inter)
        helium-metamaterial-paradox.md               [leaf — verbatim] — §§ Helium Metamaterial Paradox (unnumbered section; source: Ch.10 §Calculated Absolute Properties)
        diamond-hardness-alpha-clusters.md           [leaf — verbatim] — §§ Quantitative Hardness: Diamond from Alpha Clusters (source: Ch.10)
        metallicity-magnetic-asymmetry.md            [leaf — verbatim] — §§ Metallicity from Magnetic Asymmetry (source: Ch.10)
        per-element-impedance-table.md               [leaf — verbatim] — §§ Single-Element Impedance Under Stress; §§ Hessian of 1/d Surface; §§ Normal Mode Classification; §§ Per-Element Impedance Table; §§ Two Impedance Families; §§ Implications (sec:element_impedance)
      ch11-thermodynamics/
        index.md                                      [index] — Ch.11 summary (longest chapter, 341 lines): entropy redefinition, FDT, g*, phase transitions, Casimir cooling, water anomaly; cross-volume deps on Vol5 (sec:hbond_derivation) and Vol7 (sec:melting_eigenmode) surfaced here; links to leaves
        macroscopic-temperature-lc-noise.md          [leaf — verbatim] — Resultbox: Macroscopic Temperature as LC Noise
        vacuum-nyquist-baseline.md                   [leaf — verbatim] — Resultbox: Vacuum Nyquist Baseline (eq:vacuum_nyquist)
        effective-dof-g-star.md                      [leaf — verbatim] — Resultbox: Effective DoF g* = 7³/4 = 85.75 (eq:g_star)
        vacuum-heat-capacity.md                      [leaf — verbatim] — Resultbox: Vacuum Heat Capacity (eq:heat_capacity)
        baryon-asymmetry.md                          [leaf — verbatim] — Resultbox: Baryon Asymmetry η = 6.08×10⁻¹⁰ (eq:baryon_asymmetry)
        thermal-softening-correction.md              [leaf — verbatim] — Resultbox: Thermal Softening Correction δ_th (eq:thermal_kappa, eq:delta_th; sec:thermal_softening_thermo)
        casimir-effective-temperature.md             [leaf — verbatim] — Resultbox: Casimir Effective Temperature (eq:casimir_temperature)
        entropy-redefinition.md                      [leaf — verbatim] — §§ Redefinition of Entropy; §§ Geometric Scattering and Thermal Jitter (source: Ch.11)
        arrow-of-time.md                             [leaf — verbatim] — §§ The Arrow of Time (source: Ch.11)
        nyquist-noise-fdt.md                         [leaf — verbatim] — §§ Nyquist Noise; §§ Boundary-Impedance Thermalization (sec:fluctuation_dissipation; eq:nyquist; source: Ch.11)
        transmon-decoherence.md                      [leaf — verbatim] — §§ Transmon Qubit Decoherence; §§ Ohmic Damping (sec:fluctuation_dissipation; source: Ch.11); OUTBOUND ref to fig:transmon_decoherence (dangling — another volume)
        mode-counting-heat-capacity.md               [leaf — verbatim] — §§ 7-Mode Compliance Manifold; §§ Effective DoF; §§ Equipartition and Heat Capacity (sec:mode_counting; source: Ch.11)
        baryon-asymmetry-derivation.md               [leaf — verbatim] — §§ Baryon Asymmetry (sec:mode_counting; source: Ch.11); OUTBOUND dangling refs to ch:fundamental_axioms (Vol1) and ch:baryons (Vol1 or Vol2) noted
        thermal-softening-skyrme.md                 [leaf — verbatim] — §§ Thermal Correction to Skyrme Coupling; §§ Gradient Saturation; §§ Physical Interpretation (sec:thermal_softening_thermo; source: Ch.11)
        phase-transitions-impedance.md               [leaf — verbatim] — §§ Phase Transitions as Impedance Matching Events; §§ Superconducting Transition; §§ Casimir Cooling (sec:phase_transitions; source: Ch.11)
        water-anomaly-lc-partition.md                [leaf — verbatim] — §§ Fluid Anomalies: Two-State LC Partition (sec:water_partition; source: Ch.11); OUTBOUND refs: Vol5 Ch2 sec:hbond_derivation and Vol7 Ch11 sec:melting_eigenmode — both flagged with > → Primary pointers
        phase-transition-classification.md           [leaf — verbatim] — §§ General Classification of Phase Transitions (sec:phase_transitions; source: Ch.11)
        ch11-remaining-resultboxes.md                [leaf — placeholder] — Remaining Ch.11 resultboxes not individually listed above (survey count 17; distiller to enumerate remaining after the 7 listed above)
    applied-physics/
      index.md                                        [index] — Domain: stellar interiors, ideal gas law, geophysics; key results from Ch.7,12,13; links to 3 chapter indexes
      ch07-stellar-interiors/
        index.md                                      [index] — Ch.7 summary: stellar regime classification, impedance profiles, tachocline, helioseismology, neutrino MSW; links to leaves; OUTBOUND dangling ref ch:regime_map (likely Vol1 ch7) noted
        neutrino-msw-matter-potential.md             [leaf — verbatim] — Resultbox: Neutrino MSW Matter Potential (sec:neutrino_msw)
        msw-resonance-critical-density.md            [leaf — verbatim] — Resultbox: MSW Resonance Critical Density
        stellar-regime-classification.md             [leaf — verbatim] — §§ Stellar Regime Classification (sec:stellar_regimes; source: Ch.7)
        stellar-interior-impedance-profiles.md       [leaf — verbatim] — §§ Stellar Interiors as Impedance Profiles; §§ Tachocline Γ Derivation; §§ Helioseismology as Cavity Resonance (sec:stellar_interior; source: Ch.7)
        neutrino-flavor-mixing.md                    [leaf — verbatim] — §§ Neutrino MSW: Flavor Mixing as Impedance Mode Coupling; §§ Energy-Dependent Validation (sec:neutrino_msw; source: Ch.7)
      ch12-ideal-gas-law/
        index.md                                      [index] — Ch.12 summary: ontological foundations, LC energy balance, recovering R at STP; links to leaves
        ideal-gas-law.md                             [leaf — verbatim] — Resultbox: The Ideal Gas Law as LC energy balance
        lc-energy-balance-equation.md                [leaf — verbatim] — Resultbox: LC Energy Balance Equation
        gas-dynamics-foundations.md                  [leaf — verbatim] — §§ Ontological Foundations of Gas Dynamics; §§ Mapping the Equation of State (source: Ch.12)
        recovering-r-at-stp.md                       [leaf — verbatim] — §§ Quantitative Verification: Recovering R at STP (source: Ch.12)
      ch13-geophysics/
        index.md                                      [index] — Ch.13 summary: seismic FDTD, constitutive mapping, PREM layers, waveguide trapping; links to leaves
        seismic-reflection-coefficient-moho.md       [leaf — verbatim] — Resultbox: Seismic Reflection Coefficient (Moho) (sec:seismic_fdtd_bridge)
        seismic-fdtd-engine.md                       [leaf — verbatim] — §§ Seismic Wave Propagation on the FDTD Engine (sec:seismic_fdtd_bridge; source: Ch.13)
        constitutive-mapping.md                      [leaf — verbatim] — §§ Constitutive Mapping (source: Ch.13)
        prem-layers-waveguide.md                     [leaf — verbatim] — §§ PREM Layer Data and Numerical Evaluation; §§ Waveguide Trapping in the Low-Velocity Zone (source: Ch.13)
```

**File counts:**
- Index files: 1 (CLAUDE.md) + 1 (entry-point) + 1 (vol3/index) + 4 (domain indexes) + 15 (chapter indexes) = **22 index/navigation files**
- Leaf files: See §6 for per-chapter tallies; **estimated 115–130 leaf files** (verbatim + placeholder combined)
- Common area: 1 translation-tables leaf
- **Grand total: ~138–153 files**

---

## 4. Navigation Spec

### Up-link format

Every non-root document opens with exactly one up-link on line 1:

```markdown
[↑ Vol 3: Macroscopic Continuum](../../index.md)
```

Format by level:
- **Leaf → chapter index:** `[↑ Ch.N: {Chapter Title}](../index.md)`
- **Chapter index → domain index:** `[↑ Domain: {Domain Name}](../../index.md)`
- **Domain index → vol3 index:** `[↑ Vol 3: Macroscopic Continuum](../index.md)`
- **Vol3 index → entry-point:** `[↑ AVE Knowledge Base](../entry-point.md)`

Up-link machine-checkability: the pattern `^\[↑ ` (caret, bracket, Unicode U+2191) must appear on line 1 of every file except `entry-point.md` and `CLAUDE.md`. This is grep-verifiable.

### Down-link format

Index pages end with a `## Contents` section listing children:

```markdown
## Contents

- [Ch.1: Gravity and Yield](ch01-gravity-yield/index.md) — Chiral trace-reversal, 1/7 impedance projection, yield threshold; 14 resultboxes
- [Ch.2: General Relativity](ch02-general-relativity/index.md) — GR↔AVE mapping, Lense-Thirring, K4-TLM validation
```

### Key Results propagation format

Domain and chapter indexes carry a `## Key Results` section that surfaces major conclusions upward:

```markdown
## Key Results

- **1/7 Isotropic Impedance Projection**: gravity is a 1/7 impedance projection of the LC lattice [Ch.1](ch01-gravity-yield/one-seventh-impedance-projection.md)
- **Refractive Index of Gravity**: n(r) = 1 + 2GM/c²r [Ch.3](ch03-macroscopic-relativity/refractive-index-of-gravity.md)
```

Results must propagate: a domain index's Key Results section must include at least one entry from every chapter index below it.

### Cross-volume reference format

**Confirmed outbound cross-volume references (3 primary + 8 dangling):**

Primary outbound references use `> → Primary:` blockquote at the relevant leaf or chapter index:

```markdown
> → Primary: [Vol 4 — K4-TLM Simulator](../../vol4/engineering/k4-tlm/index.md) — This section cross-validates against sec:k4_tlm in Vol 4. Navigate there for the simulator specification.
```

```markdown
> → Primary: [Vol 5 — Hydrogen Bond Derivation](../../vol5/biology/protein-folding/hbond-derivation.md) — sec:hbond_derivation is referenced here; that leaf contains the derivation.
```

```markdown
> → Primary: [Vol 7 — Melting Eigenmode](../../vol7/hardware/melting-eigenmode/index.md) — sec:melting_eigenmode is referenced here; that section contains the experimental validation.
```

**Placement of primary outbound references:**
- `ch02-general-relativity/k4-tlm-lensing-validation.md` — carries the Vol 4 pointer
- `ch11-thermodynamics/water-anomaly-lc-partition.md` — carries both the Vol 5 and Vol 7 pointers
- `ch11-thermodynamics/index.md` — also surfaces both outbound deps at chapter index level so an agent reading the chapter index is alerted before navigating to leaves

**Dangling refs (8 additional beyond the 3 confirmed):**

Dangling refs that cannot be resolved to a known KB path are marked with `> ↗ See also:` blockquote using an annotation-only form (no live link):

```markdown
> ↗ See also: `ch:regime_map` — referenced here but target volume/chapter not confirmed; likely Vol 1 Ch.7 Regime Map. Verify against Vol 1 taxonomy.
```

Dangling annotations appear in:
- `ch07-stellar-interiors/index.md` — `ch:regime_map`
- `ch11-thermodynamics/transmon-decoherence.md` — `fig:transmon_decoherence`
- `ch11-thermodynamics/baryon-asymmetry-derivation.md` — `ch:fundamental_axioms`, `ch:baryons`
- `ch11-thermodynamics/index.md` — `ch:quantum_computing` (×2)
- `ch11-thermodynamics/phase-transitions-impedance.md` — `fig:casimir_superconductor`
- `ch15-black-hole-orbitals/index.md` — `sec:kerr_q_correction`, `ch:engine_architecture`

### Intra-volume optional cross-references

Optional suggestions use `> ↗ See also:` without `→ Primary:`:

```markdown
> ↗ See also: [Ch.9 Superconducting Transition](../../condensed-matter/ch09-condensed-matter-superconductivity/critical-field-validation.md) — phase transition analogy
```

---

## 5. Shared Content Decision: Translation Tables

**Recommendation: (a) Dedicated page at `ave-kb/common/translation-tables.md`**

**Reasoning:**

The survey confirms that three translation files (`translation_gravity.tex`, `translation_cosmology.tex`, `translation_condensed_matter.tex`) appear in two places in the source: once in their respective chapters (Ch.2 `sec:gr_ave_translation`, Ch.9 `sec:cm_ave_translation`) and once in backmatter App A. This duplication is structural in the manuscript but should NOT be replicated in the KB.

The KB serves agent navigation. An agent asking "what is the GR↔AVE translation?" should land at one canonical location. Duplication across vol-specific leaves would create two paths to the same content — one of which may become stale if the source is updated.

**Decision:** Create `ave-kb/common/translation-tables.md` as the single verbatim home for all translation tables from `translation_*.tex`. Chapter-level leaves (Ch.2 `gr-ave-translation-dictionary.md`, Ch.9 `cm-ave-translation.md`) carry a `> → Primary:` pointer to `ave-kb/common/translation-tables.md` rather than duplicating content. The chapter leaves contain only section-context prose (introductory framing) plus the pointer; the tables themselves live once in `common/`.

**Scope of `common/`:** Limited to genuinely shared content that appears verbatim in multiple volume chapters. Do not expand `common/` to be a general reference area — that risks it growing into an unnavigable miscellany.

---

## 6. Acceptance Criteria

The following properties must hold when Vol 3's KB section is complete and before Phase 2 begins.

**1. Up-link completeness**
```
find manuscript/ave-kb/vol3 -name "*.md" | xargs grep -L '^\[↑ '
```
Must return empty (zero files missing up-links). Exception: `vol3/index.md` itself carries `[↑ AVE Knowledge Base](../entry-point.md)` and passes. `entry-point.md` and `CLAUDE.md` are excluded from this search.

**2. Entry-point token budget**
```
wc -w manuscript/ave-kb/entry-point.md
```
Must be under 2200 words (conservative proxy for 3000 tokens).

**3. Maximum hierarchy depth**
```
find manuscript/ave-kb/vol3 -name "*.md" | awk -F/ '{print NF}' | sort -n | tail -1
```
Must not exceed 8 path components (entry-point.md is at depth 2; vol3 leaves are at depth 6 = `manuscript/ave-kb/vol3/{domain}/{chapter}/{leaf}.md`). No file exceeds 8.

**4. Leaf marker presence**
```
find manuscript/ave-kb/vol3 -name "*.md" | xargs grep -L '^<!-- leaf:' | grep -v index.md
```
Must return empty. Every non-index `.md` file must carry `<!-- leaf: verbatim -->` or `<!-- leaf: placeholder -->` on line 2.

**5. No summarization in verbatim leaves**
```
find manuscript/ave-kb/vol3 -name "*.md" | xargs grep -l '^## Summary\|^## Overview' | grep -v index.md
```
Must return empty. `## Summary` and `## Overview` headings are index-level constructs; their presence in a leaf file signals the distiller has summarized rather than translated.

**6. Key Results propagation — domain level**
Each domain index (`gravity/index.md`, `cosmology/index.md`, `condensed-matter/index.md`, `applied-physics/index.md`) must contain a `## Key Results` section with at least one entry linking to a leaf in each chapter below it. Verify by inspection: count `## Key Results` entries per chapter slug in each domain index.

**7. Three confirmed outbound references resolved**
The following three files must contain `> → Primary:` blockquotes linking to the target volume:
- `ave-kb/vol3/gravity/ch02-general-relativity/k4-tlm-lensing-validation.md` → Vol 4
- `ave-kb/vol3/condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md` → Vol 5
- `ave-kb/vol3/condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md` → Vol 7

**8. Clean slug for Ch.5**
```
find manuscript/ave-kb/vol3 -type d -name "*v7*"
```
Must return empty. The legacy `ch:cosmology_v7` label must not appear as a directory name. The correct slug is `ch05-dark-sector`.

**9. Translation table singularity**
```
find manuscript/ave-kb -name "translation-tables.md" | wc -l
```
Must equal 1 (exactly one canonical translation table file, at `ave-kb/common/translation-tables.md`). No vol-specific leaf should contain verbatim table content from `translation_*.tex`.

**10. Resultbox coverage floor**
The total count of `[leaf — verbatim]` files across all Ch.11 leaves must be at least 15 (survey reports 17 resultboxes; placeholder files cover the remainder). Verify by:
```
find manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics -name "*.md" | grep -v index | wc -l
```
Must be ≥ 16 (15 content leaves + 1 placeholder minimum).

---

## 7. Anomaly Handling Notes

| Anomaly | Handling |
|---|---|
| Merged ch.9 (former ch6+ch9) | KB slug `ch09-condensed-matter-superconductivity`; chapter index notes merge history; leaf structure covers merged content as a unit |
| Legacy label `ch:cosmology_v7` on Ch.5 | KB slug `ch05-dark-sector`; no `_v7` appears anywhere in directory names or file names |
| 11 dangling refs | 3 confirmed outbound get `> → Primary:` pointers; 8 unresolvable get `> ↗ See also:` annotation-only markers; listed at §4 above |
| Ch.11 outlier length (341 lines, 17 resultboxes) | 16 individual leaf files enumerated in skeleton (7 resultbox leaves + 8 section leaves + 1 placeholder); subsection-granularity decomposition applied |
| Ch.15 outlier length (339 lines, 9 resultboxes) | 12 individual leaf files enumerated; no fifth hierarchy level needed |
| Ch.1 result density (14 resultboxes in 196 lines) | 11 individual leaf files; 1 placeholder for remaining; foundational numerical results surface in gravity domain Key Results |
| Ch.14 unlabeled opening regime table | Captured as `orbital-regime-table.md` leaf with note: no label in source |
| `\vacuum` macro mismatch | CLAUDE.md invariant `mathcal_M_A` covers this; distillers must write `\mathcal{M}_A` not `M_A` |
| Translation table duplication (chapter + App A) | Resolved by `ave-kb/common/translation-tables.md` canonical location; chapter leaves point to it |
| `\cite{nilsson2026llcp}` in Ch.11 | Verbatim leaf captures the citation as-is; no KB action needed |
| `app:dcve` unreferenced from chapters | Not modeled in the chapter hierarchy; covered if App D is extracted as a shared appendix leaf (out of scope for vol3 taxonomy) |
| No objectivebox/simbox/axiombox in vol3 | Leaf environments: only resultbox (90), summarybox (15), exercisebox (15). Skeleton reflects this. |
