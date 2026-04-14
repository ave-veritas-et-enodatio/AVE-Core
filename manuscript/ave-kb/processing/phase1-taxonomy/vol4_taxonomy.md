# Phase 1 Taxonomy — Vol 4: Engineering Applications

**Volume:** Vol 4 — Applied Vacuum Engineering (Engineering Applications)
**Source survey:** `/.claude/phase0-surveys/vol4_survey.md`
**Output target:** `manuscript/ave-kb/vol4/`
**Chapters:** 18 | **Estimated leaves:** 140-160

---

## 1. CLAUDE.md Invariants from This Volume

The following concepts are first defined in Vol 4 and are used (or directly referenced)
across multiple volumes. They belong in `manuscript/ave-kb/CLAUDE.md`, not in
volume-specific pages.

```
INVARIANT: V_yield — 43.65 kV absolute dielectric saturation (yield) limit;
    $V_{yield} \approx 43.65$ kV. First defined in Ch.1 (eq:varactor,
    sec:vca_nonlinear). Used in Vol 4 chs. 1, 2, 5, 8, 11 and referenced
    across project as "the 43.65 kV limit." Cross-volume anchor.
    (source: Vol 4 Ch.1, eq:varactor / sec:vca_nonlinear)

INVARIANT: V_snap — 511 kV absolute nodal snap limit (Compton-energy
    threshold). First defined in Ch.1 (sec:vca_nonlinear), used in Vol 4
    chs. 1, 8, 11. Companion to V_yield.
    (source: Vol 4 Ch.1, sec:vca_nonlinear)

INVARIANT: S(V) — Saturation kernel $S(V) = \sqrt{1-(V/V_{yield})^2}$.
    The nonlinear constitutive function of the vacuum varactor; appears in
    metric varactor, thrust, and IMD derivations across Vol 4 and is the
    foundational nonlinearity referenced in Vol 2/3.
    (source: Vol 4 Ch.1, eq:varactor)

INVARIANT: xi_topo — Topological conversion constant $\xi_{topo} = e/\ell_{node}$.
    The scalar that maps mechanical quantities to circuit quantities throughout
    the topo-kinematic translation table. Defined Vol 4 Ch.1 (eq:xi_topo_vca),
    used in Vols 1, 4, 5, 6.
    (source: Vol 4 Ch.1, eq:xi_topo_vca / sec:topo_kinematic)

INVARIANT: l_node notation — All volumes except Vol 1 write $l_{node}$ (roman
    ell). Vol 1 writes $\ell_{node}$ (script ell). KB distillers must
    preserve source notation exactly; do not normalise across volumes.
    (source: confirmed in all 8 surveys)

INVARIANT: Translation table (tab:trans_circuit) — The six-row
    Topo-Kinematic Circuit Identity translation table, imported via
    `\input{../common/translation_circuit.tex}`. Used in Vol 4 Ch.1 and
    re-used in shared backmatter. The authoritative KB copy lives at
    `ave-kb/common/translation-circuit.md`; Vol 4 Ch.1 leaf links there
    as a primary pointer.
    (source: Vol 4 Ch.1, tab:trans_circuit; common/translation_circuit.tex)
```

**Invariants confirmed present in this volume: 6**
(V_yield, V_snap, S(V), xi_topo, l_node notation rule, translation table)

Note: $\rho_{bulk}$, $\nu_{vac}$, $\kappa_{FS}$, $p_c$ are used in multiple
Vol 4 chapters but do not have confirmed cross-volume references beyond prose
mentions. They belong in the Vol 4 `circuit-theory` domain index, not CLAUDE.md.

---

## 2. Domain Grouping Rationale

With 18 chapters and ~140-160 leaves, the 4-level hierarchy is required.
Entry-point → volume index → domain index → chapter index → leaf exceeds 4
levels; to stay within the 4-level constraint, chapters are collapsed into
the domain as subtopics (domain index lists chapters as its direct children,
each chapter gets its own index with leaves below). This is depth 4:
entry-point (level 0) → domain index (level 1 within vol4) → chapter index
(level 2) → leaf (level 3). The volume index itself is at level 0 of the
volume tree, hanging off entry-point at level 1 of the global tree.
Full path depth from entry-point: entry-point → vol4/index → domain/index →
chapter/index → leaf = 4 hops = 4 levels. Compliant.

### Six domains

| Domain slug | Chapters | Rationale |
|-------------|----------|-----------|
| `circuit-theory` | Ch.1-2 | Foundational circuit mathematics; the translation table, constitutive models, and thrust mechanics from first principles. Other domains consume these results. |
| `hardware-programs` | Ch.3-6 | Named experimental hardware programs: HOPF-01 (chiral antenna), PONDER design evolution (01→05), torsion metrology. These are fabrication-and-measurement chapters. |
| `advanced-applications` | Ch.7-10, Ch.18 | Higher-order applications of the circuit framework: SMES, fusion, antimatter, quantum computing, active metamaterials/LLCP. Grouped by application type rather than experiment type. |
| `falsification` | Ch.11-12 | Experimental falsification protocols and binary kill-switch predictions. Ch.11 is the bench protocol compendium; Ch.12 is the formal prediction list. Kept together because agents navigating to "how do I falsify claim X" need both. |
| `future-geometries` | Ch.13 | Future hardware designs (phased arrays, Hopf coils) and the K4-TLM simulator. Ch.13 is large (~464 lines) and hosts the cross-volume `sec:k4_tlm` anchor; it warrants a dedicated domain to keep K4-TLM reachable without traversing other domains. |
| `simulation` | Ch.14-17 | SPICE simulation chapters. All four use codeboxes for netlists and model specific physical phenomena (particle decay, autoresonance, Sagnac drag, hardware netlists). Grouped as a simulation lab. |

---

## 3. Document Skeleton

Notation:
- `[index]` — navigation node; contains domain/chapter summary + key results + child links
- `[leaf — verbatim]` — terminal; contains verbatim translated source content
- `[leaf — placeholder]` — terminal; source section identified but not yet distilled
- Lines beginning `>` are cross-reference annotations (not file types)

```
manuscript/ave-kb/
├── CLAUDE.md                                  [invariants: V_yield, V_snap, S(V), xi_topo, l_node notation, tcolorbox env names, cross-vol label conventions]
├── entry-point.md                             [global index: one paragraph per volume + link to vol index; target <3000 tokens]
├── common/
│   └── translation-circuit.md                [leaf — verbatim: six-row Topo-Kinematic Circuit Identity translation table from common/translation_circuit.tex]
│
└── vol4/
    ├── index.md                               [Vol 4 index: domain summaries, key results propagated from all 6 domains, domain links]
    │
    ├── circuit-theory/
    │   ├── index.md                           [Circuit theory domain index: topo-kinematic identity, constitutive models, Z0, IMD, thrust mechanics; key results from both chapters]
    │   │
    │   ├── ch01-vacuum-circuit-analysis/
    │   │   ├── index.md                       [Ch.1 index: section map, key results list with links to leaves]
    │   │   ├── topo-kinematic-identity.md     [leaf — verbatim: sec:topo_kinematic; translation table, xi_topo derivation, six-row identity (eq:xi_topo_vca through eq:resistance_viscosity)]
    │   │   ├── constitutive-models.md         [leaf — verbatim: sec:vca_nonlinear; metric varactor eq:varactor, relativistic inductor eq:relativistic_inductor, TVS eq:tvs_transition, memristor, skin effect eq:skin_depth]
    │   │   ├── impedance-free-space.md        [leaf — verbatim: sec:z0_derivation; LC ladder derivation eq:cell_elements, eq:z0_cell, eq:c_from_lc, eq:z_mech, propagation velocity, acoustic impedance, impedance regimes]
    │   │   ├── gravitational-stealth.md       [leaf — verbatim: section "Gravitational Stealth (S-Parameter Analysis)"; condensate transmission line, horizon mirror, black hole echo predictions]
    │   │   ├── periodic-table-spice-mappings.md [leaf — verbatim: section "The Periodic Table: Topological SPICE Mappings"; topological SPICE equivalents]
    │   │   ├── topological-defects-lc-solitons.md [leaf — verbatim: sections on LC solitons, virial theorem, E=mc^2 recovery, confinement bubble, Pauli exclusion from impedance]
    │   │   ├── orbital-friction-paradox.md    [leaf — verbatim: section "Real vs. Reactive Power: The Orbital Friction Paradox"]
    │   │   └── imd-spectroscopy.md            [leaf — verbatim: sec:imd; IMD non-linear source, Taylor expansion, eq:im3_frequencies, eq:ip3, QED comparison, falsification criterion]
    │   │
    │   └── ch02-topological-thrust-mechanics/
    │       ├── index.md                       [Ch.2 index: operating regimes, chiral rectification thrust, dark wake, metric streamlining; key results]
    │       ├── operating-regimes.md           [leaf — verbatim: sec:regimes_of_operation; tab:ponder_regimes, regime map]
    │       ├── chiral-acoustic-rectification.md [leaf — verbatim: sec:chiral_thrust; saturation kernel concavity, Jensen's inequality eq:jensen_rect, local field eq:e_local_peak, thrust eq:chiral_thrust, eq:e_yield]
    │       ├── dark-wake-momentum.md          [leaf — verbatim: section "Conservation of Momentum (The Dark Wake)"; stereo parallax validation]
    │       └── metric-streamlining.md         [leaf — verbatim: section "Metric Streamlining & Superluminal Transit"; nonlinear acoustic steepening, active acoustic drill, Kerr black holes as topological saturation defects]
    │
    ├── hardware-programs/
    │   ├── index.md                           [Hardware programs domain index: HOPF-01, PONDER-01→05 design evolution, torsion metrology; key results and predictions from chs. 3-6]
    │   │
    │   ├── ch03-hopf-01-chiral-verification/
    │   │   ├── index.md                       [Ch.3 index: HOPF-01 chiral antenna falsification; SM baseline vs AVE predictions; section map]
    │   │   ├── chiral-coupling-prediction.md  [leaf — verbatim: section "The Chiral Coupling Prediction"; eq:n_ave, frequency shift scaling law]
    │   │   ├── wire-stitched-fixture.md       [leaf — verbatim: sections "Wire-Stitched Torus Knot Fixture" + "Wire-Stitched Knot Geometry"; wire length derivation, eq:arc_length, eq:z0_wire, eq:m_cross]
    │   │   ├── hopf-01-falsification-protocol.md [leaf — verbatim: section "The Falsification Protocol" + "Decision Gate"; S21 chiral parallax tracking, pass/fail criteria]
    │   │   ├── impedance-characterization.md  [leaf — verbatim: section "Impedance Characterization"; S11 sweep model, fig:hopf_01_impedance]
    │   │   ├── sm-baseline.md                 [leaf — verbatim: section "Standard Model Baseline Response"; tab:sm_baseline, tab:sm_vs_ave, tab:discriminators]
    │   │   ├── manufacturing-tolerance.md     [leaf — verbatim: section "Manufacturing Tolerance Rejection"; substrate independence three-medium verification]
    │   │   └── bill-of-materials-hopf01.md    [leaf — verbatim: section "Bill of Materials"; component list]
    │   │
    │   ├── ch04-ponderomotive-program/
    │   │   ├── index.md                       [Ch.4 index: PONDER-01 PCBA concept, thermal catastrophe, design pivot to PONDER-05; key results]
    │   │   ├── ponder-01-concept.md           [leaf — verbatim: section "PONDER-01: The Asymmetric PCBA Concept"; thrust prediction (unlabelled resultbox)]
    │   │   ├── thermal-catastrophe.md         [leaf — verbatim: section "The Thermal Catastrophe"; dielectric heating at VHF, pulsed limitations, bistatic parallax offset, dielectric power dissipation resultbox]
    │   │   └── design-pivot-ponder05.md       [leaf — verbatim: section "The Design Pivot: PONDER-05"; rationale for quartz transition]
    │   │
    │   ├── ch05-ponder-05-dc-biased-quartz/
    │   │   ├── index.md                       [Ch.5 index: PONDER-05 operating regime, DC cross-term, quartz cylinder, predicted thrust; key results]
    │   │   ├── nonlinear-operating-regime.md  [leaf — verbatim: section "The Nonlinear Operating Regime"; resultbox: nonlinear dielectric saturation regime]
    │   │   ├── dc-cross-term.md               [leaf — verbatim: sections "DC Cross-Term Amplification" + "Rarefaction Wave Inversion" + "Differential Saturation Parallax"; resultboxes for DC cross-term and nonlinear acoustic phase velocity]
    │   │   ├── quartz-cylinder-design.md      [leaf — verbatim: section "The Quartz Cylinder"]
    │   │   ├── mineral-oil-bath.md            [leaf — verbatim: section "The Mineral Oil Dielectric Bath"; corona suppression, impedance matching eq (quarter-wave resultbox), thermal management]
    │   │   ├── thrust-profile-ponder05.md     [leaf — verbatim: section "Predicted Thrust Profile (Linear Base)"]
    │   │   └── bill-of-materials-ponder05.md  [leaf — verbatim: section "Bill of Materials"; PONDER-05 component list]
    │   │
    │   └── ch06-torsion-metrology/
    │       ├── index.md                       [Ch.6 index: torsion balance architecture, eight-point artifact rejection, complementary EM verification; key result]
    │       ├── torsion-balance-architecture.md [leaf — verbatim: section "The Torsion Balance Architecture"; angular deflection resultbox]
    │       ├── mineral-oil-bath-ponder05.md   [leaf — verbatim: section "The Mineral Oil Dielectric Bath (PONDER-05)" in Ch.6; corona, thermal, impedance step-down, bistatic plume diagnostics]
    │       ├── artifact-rejection-protocol.md [leaf — verbatim: section "The Eight-Point Artifact Rejection Protocol"]
    │       ├── em-verification.md             [leaf — verbatim: section "Complementary Electromagnetic Verification"]
    │       └── measurement-timeline.md        [leaf — verbatim: section "Measurement Timeline and Decision Gates"]
    │
    ├── advanced-applications/
    │   ├── index.md                           [Advanced applications domain index: SMES, fusion, antimatter, quantum computing, active metamaterials; key results from chs. 7-10, 18]
    │   │
    │   ├── ch07-topological-smes/
    │   │   ├── index.md                       [Ch.7 index: force-free macroscopic electron, Beltrami torus knot, SMES stray flux falsification]
    │   │   ├── force-free-field.md            [leaf — verbatim: section "The Force-Free Macroscopic Electron"; (p,q) Beltrami torus knot]
    │   │   └── smes-falsification.md          [leaf — verbatim: subsection "Computational Falsification of Stray Flux"; fig:smes_leakage]
    │   │
    │   ├── ch08-applied-fusion/
    │   │   ├── index.md                       [Ch.8 index: tokamak paradox, metric-catalyzed fusion scaling, alchemist forge; all key results]
    │   │   ├── dt-phase-lock.md               [leaf — verbatim: section "Topological Resonance: The Mechanics of D-T Phase-Lock"; analytical operating regimes resultbox]
    │   │   ├── engineering-rules.md           [leaf — verbatim: section "Rules for Application: Engineering the Vacuum"]
    │   │   ├── tokamak-paradox.md             [leaf — verbatim: sec:tokamak_paradox; 60.3 kV alignment, tokamak ignition strain resultbox, vacuum yield limit resultbox]
    │   │   ├── inertial-confinement.md        [leaf — verbatim: section "Inertial Confinement: Zero-Impedance Phase Rayleigh-Taylor Instabilities"]
    │   │   ├── pulsed-frc-dielectric-poisoning.md [leaf — verbatim: section "Pulsed FRCs and Dielectric Poisoning"]
    │   │   ├── metric-catalyzed-fusion.md     [leaf — verbatim: section "The AVE Solution: Metric-Catalyzed Fusion"; eq:radius_scaling, eq:temp_scaling, eq:vtopo_scaling, eq:gamow_compressed, eq:n_star, why fusion works in sun]
    │   │   ├── empirical-reactor-data.md      [leaf — verbatim: section "Empirical Reactor Data: Validating the Leakage Paradox"; anomalous transport, L-H transition, advanced fuels]
    │   │   ├── nuclear-fission-topology.md    [leaf — verbatim: section "Topological Mechanics of Nuclear Fission (U-235 vs U-238)"]
    │   │   └── alchemist-forge.md             [leaf — verbatim: section "The Vacuum Element Synthesizer (The Alchemist Forge)"; hierarchical alpha synthesis, deep topological quenching, LC annealer circuit]
    │   │
    │   ├── ch09-antimatter/
    │   │   ├── index.md                       [Ch.9 index: annihilation as flywheel collision, parity inversion, pair production; key results]
    │   │   ├── annihilation-flywheel.md       [leaf — verbatim: section "Matter-Antimatter Annihilation as Flywheel Collisions"; parity inversion in macroscopic knots, continuous mechanics of shattering; rotational KE resultbox, kinetic release resultbox]
    │   │   └── pair-production.md             [leaf — verbatim: section "Pair Production as Volumetric Wave Shear"; kinematics of the wave-tear]
    │   │
    │   ├── ch10-quantum-computing/
    │   │   ├── index.md                       [Ch.10 index: transmon fragility, topological qubit, Casimir shielding, Kuramoto phase-lock; key results]
    │   │   ├── transmon-lc-wave.md            [leaf — verbatim: section "The Transmon: A Fragile LC Standing Wave"]
    │   │   ├── topological-qubit.md           [leaf — verbatim: section "The Topological Qubit: Invulnerability via Gauss Linking"; Gauss linking number resultbox]
    │   │   ├── casimir-shielding.md           [leaf — verbatim: section "Casimir Cavity Shielding: Filtering the Vacuum Impedance"]
    │   │   └── kuramoto-phase-lock.md         [leaf — verbatim: section "Artificial Kuramoto Phase-Lock (Room-Temperature Superconductivity)"]
    │   │
    │   └── ch18-active-topological-metamaterials/
    │       ├── index.md                       [Ch.18 index: inorganic LLCP, self-healing kinetic armor, neuromorphic memristor; key results]
    │       ├── inorganic-llcp.md              [leaf — verbatim: sections introducing active topological metamaterials and LLCP mapping to Vol 5 organic circuitry]
    │       ├── self-healing-kinetic-armor.md  [leaf — verbatim: section on kinetic armor yield and topological reflection]
    │       └── neuromorphic-memristor.md      [leaf — verbatim: section on memristor hysteresis and neuromorphic applications]
    │
    ├── falsification/
    │   ├── index.md                           [Falsification domain index: bench protocols inventory (chs. 11-12), binary kill-switches, falsifiable predictions; key results from both chapters]
    │   │
    │   ├── ch11-experimental-bench-falsification/
    │   │   ├── index.md                       [Ch.11 index: 15 distinct protocols and projects enumerated with leaf links; epistemology of falsification; tabletop graveyard note]
    │   │   ├── epistemology-falsification.md  [leaf — verbatim: section "The Epistemology of Falsification"]
    │   │   ├── tabletop-graveyard.md          [leaf — verbatim: section "The Tabletop Graveyard"; VFDT and RVR failure analysis]
    │   │   ├── sagnac-rlve-killswitch.md      [leaf — verbatim: section "The Ultimate Kill-Switch: The Sagnac-RLVE"; exact derivation of macroscopic shift, hardware spec & protocol; inline tcolorbox Sagnac phase equation]
    │   │   ├── existing-signatures.md         [leaf — verbatim: section "Existing Experimental Signatures"; proton radius puzzle, neutron lifetime anomaly, Hubble tension, LIGO GW150914 echoes, superconducting vortex core limits]
    │   │   ├── project-cleave-01.md           [leaf — verbatim: section "Project CLEAVE-01: The Femto-Coulomb Electrometer"]
    │   │   ├── project-hopf-02.md             [leaf — verbatim: section "Project HOPF-02: The S-Parameter VNA Falsification"; topological refraction / Snell parallax]
    │   │   ├── project-roentgen-03.md         [leaf — verbatim: section "Project ROENTGEN-03: Solid-State Sagnac Induction"]
    │   │   ├── project-zener-04.md            [leaf — verbatim: section "Project ZENER-04: The Impedance Avalanche Detector"]
    │   │   ├── hardware-limit-metric-levitation.md [leaf — verbatim: section "The Absolute Hardware Limit of Metric Levitation"; dielectric death spiral; inline tcolorbox levitation mass equation]
    │   │   ├── project-torsion-05.md          [leaf — verbatim: section "Project TORSION-05: Horizontal Metric Rectification"]
    │   │   ├── ybco-phased-array.md           [leaf — verbatim: section "The YBCO Phased Array: Beating the 2.5g Limit"]
    │   │   ├── metric-refraction-capacitor.md [leaf — verbatim: section "The Metric Refraction Capacitor (The c^2 Multiplier)"]
    │   │   ├── sapphire-phonon-centrifuge.md  [leaf — verbatim: section "The Sapphire Phonon Centrifuge"]
    │   │   ├── applied-telemetry.md           [leaf — verbatim: section "Applied Telemetry: Boundary Layer and Cavitation Monitors"; hull-integrated sensors, redline pair-production monitors, sonoluminescence phase-lock]
    │   │   ├── open-source-build-guide.md     [leaf — verbatim: section "Open-Source Hardware: The EE Build Guide"; HOPF-01 and PONDER-01 build references]
    │   │   ├── zero-parameter-derivations.md  [leaf — verbatim: section "The Zero-Parameter Derivations"; sqrt(alpha) kinetic yield limit]
    │   │   ├── horsemen-of-falsification.md   [leaf — verbatim: section "Resolving the Horsemen of Falsification"; LHC paradox, LIGO paradox]
    │   │   ├── protocol-09-achromatic-lens.md [leaf — verbatim: sec:achromatic_lens; Protocol 9: Achromatic Impedance Lens]
    │   │   ├── protocol-10-boundary-trapping.md [leaf — verbatim: sec:boundary_trapping; Protocol 10: Orbital Detritus and Boundary Trapping; macroscopic filtering and falsification]
    │   │   ├── induced-vacuum-impedance-mirror.md [leaf — verbatim: sec:induced_vacuum_impedance_mirror; localized asymmetric saturation limit, high-voltage boundaries, falsification protocol. NOTE: this section contains dangling refs to sec:topological_defects_lc, sec:point_yield, eq:dielectric_saturation — not defined in Vol 4; mark with KB annotation]
    │   │   ├── protocol-11-sagnac-parallax.md [leaf — verbatim: section "Protocol 11: Sagnac-Parallax (Galactic Wind Vectoring)"]
    │   │   └── protocol-12-geo-synchronous.md [leaf — verbatim: section "Protocol 12: GEO-Synchronous Impedance Differential"]
    │   │
    │   └── ch12-falsifiable-predictions/
    │       ├── index.md                       [Ch.12 index: EE bench plateau, PONDER-01 Maxwell stress, Sagnac RLVG, autoresonant Schwinger bypass, torus knot baryon masses; key results. NOTE: sec:ee_bench label missing from Ch.12 source — section exists but has no \label; KB path is the stable reference.]
    │       ├── ee-bench-dielectric-plateau.md [leaf — verbatim: section "The EE Bench: The Macroscopic Dielectric Plateau" (sec:ee_bench — label absent in source); falsification protocol]
    │       ├── ponder-01-maxwell-stress.md    [leaf — verbatim: section "The Ponder-01: Asymmetric Maxwell Stress Rectification"; falsification protocol]
    │       ├── epistemology-ch12.md           [leaf — verbatim: section "The Epistemology of Falsification" (Ch.12 instance)]
    │       ├── sagnac-rlvg-predictions.md     [leaf — verbatim: section "The Sagnac Effect and RLVG Impedance Drag"; kinematic & EM entrainment law, RLVG tolerances, applied telemetry]
    │       ├── helicity-injection.md          [leaf — verbatim: section "Electromagnetic Coupling to the Chiral LC Condensate (Helicity Injection)"]
    │       ├── autoresonant-schwinger.md      [leaf — verbatim: section "Autoresonant Dielectric Rupture (The Schwinger Limit)"]
    │       ├── binary-kill-switches.md        [leaf — verbatim: section "Definitive Binary Kill-Switches"]
    │       ├── vacuum-birefringence.md        [leaf — verbatim: section "The Vacuum Birefringence Limit: E^2 vs E^4"; falsification protocol]
    │       └── torus-knot-baryon-masses.md    [leaf — verbatim: section "The Torus Knot Ladder: Baryon Resonance Mass Predictions"; falsification protocol]
    │
    ├── future-geometries/
    │   ├── index.md                           [Future geometries domain index: toroidal/poloidal fusion, chiral antenna engineering, CEM solver comparison, K4-TLM simulator; key results from Ch.13]
    │   │
    │   └── ch13-future-geometries/
    │       ├── index.md                       [Ch.13 index: section map, key results (helicity density, chiral FoM, Beltrami eigenvalue, K4 scattering matrix), K4-TLM cross-volume anchor note]
    │       ├── toroidal-poloidal-fusion.md    [leaf — verbatim: section "Toroidal and Poloidal Fusion"; vector scaling vs knot volumetrics]
    │       ├── atomic-baseline-trefoils.md    [leaf — verbatim: section "The Atomic Baseline: Trefoils and Phased Arrays"; acoustic back-reaction analogy; magnetic helicity density resultbox]
    │       ├── chiral-impedance-antenna.md    [leaf — verbatim: sec:high_q_chiral; chiral figure of merit eq:chiral_fom; receiver mode sec:rx_antenna; transmitter mode sec:tx_coil; matching network; sensitivity analysis]
    │       ├── cem-solver-comparison.md       [leaf — verbatim: sec:cem_methods; MoM eq:mom, FDTD, FEM eq:fem, TLM, CMA eq:cma, PO/GO; unified comparison and solver recommendation]
    │       └── k4-tlm-simulator.md            [leaf — verbatim: sec:k4_tlm; K4 graph topology, scattering matrix eq:k4_scatter, computational loop, validation results, wire antenna resonance, 3D torus knot simulation. CROSS-VOLUME ANCHOR: Vol 3 references this section — stable KB path is ave-kb/vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md]
    │
    └── simulation/
        ├── index.md                           [Simulation domain index: SPICE approach overview, four simulation chapters; results summary]
        │
        ├── ch14-leaky-cavity-particle-decay/
        │   ├── index.md                       [Ch.14 index: particle decay as RLC discharge; SPICE netlist; key results]
        │   ├── leaky-cavity-theory.md         [leaf — verbatim: introductory sections; quantum decay as RLC discharge model; analytical result]
        │   └── leaky-cavity-spice.md          [leaf — verbatim: SPICE netlist codebox; simulation parameters; fig:leaky_cavity_decay]
        │
        ├── ch15-autoresonant-breakdown/
        │   ├── index.md                       [Ch.15 index: autoresonant dielectric breakdown, bypassing the Schwinger limit; SPICE netlist; key results]
        │   ├── autoresonance-theory.md        [leaf — verbatim: introductory sections; autoresonant PLL model; analytical result]
        │   └── autoresonance-spice.md         [leaf — verbatim: SPICE netlist codebox; simulation parameters; fig:autoresonance_pll]
        │
        ├── ch16-sagnac-inductive-drag/
        │   ├── index.md                       [Ch.16 index: Sagnac macroscopic inductive drag; SPICE netlist; key results]
        │   ├── sagnac-drag-theory.md          [leaf — verbatim: introductory sections; inductive drag model; analytical result]
        │   └── sagnac-drag-spice.md           [leaf — verbatim: SPICE netlist codebox; simulation parameters; fig:sagnac_inductive_drag]
        │
        └── ch17-hardware-netlists/
            ├── index.md                       [Ch.17 index: PONDER-01 and EE bench netlists; hardware netlist engineering overview]
            ├── ponder-01-netlist-theory.md    [leaf — verbatim: introductory sections of Ch.17; hardware context for PONDER-01 and EE bench simulation]
            └── hardware-netlists-spice.md     [leaf — verbatim: SPICE netlist codebox(es) for PONDER-01 and EE bench; fig:hardware_netlist_overview. NOTE: Ch.17 has no resultboxes — codebox is the primary content type]
```

---

## 4. Navigation Spec

### Up-link format (every non-root document, line 1)

```markdown
[↑ Ch.1 — Vacuum Circuit Analysis](../index.md)          ← leaf to chapter index
[↑ Circuit Theory](../../index.md)                        ← chapter index to domain index
[↑ Vol 4 — Engineering Applications](../index.md)         ← domain index to vol index
[↑ Entry Point](../../entry-point.md)                     ← vol index to entry-point
```

The arrow character is `↑` (U+2191). Grep pattern for machine-checking: `^\[↑ `.

### Down-link format (index pages only)

Each index document ends with a `## Contents` section listing direct children
with one-line descriptions. Example from a chapter index:

```markdown
## Contents

- [Topo-Kinematic Identity](topo-kinematic-identity.md) — six-row translation table; xi_topo derivation (eq:xi_topo_vca through eq:resistance_viscosity)
- [Constitutive Models](constitutive-models.md) — metric varactor S(V), relativistic inductor, TVS, memristor, skin effect
- [Impedance of Free Space](impedance-free-space.md) — LC ladder derivation of Z0, c, mechanical acoustic impedance
- ...
```

### Cross-volume reference format

Two blockquote forms, distinguished by necessity:

```markdown
> → Primary: [K4-TLM Simulator](../../vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md) — K4 diamond lattice scattering matrix; cross-volume anchor (sec:k4_tlm, Vol 4 Ch.13)

> ↗ See also: [Saturation Kernel S(V)](../../vol4/circuit-theory/ch01-vacuum-circuit-analysis/constitutive-models.md) — definition of S(V) = sqrt(1-(V/V_yield)^2); eq:varactor
```

`→ Primary:` = the agent MUST follow this to get the definition.
`↗ See also:` = optional; agent may follow if broader context is desired.

### Vol 3 → Vol 4 K4-TLM cross-volume reference

Documents in `ave-kb/vol3/` that reference the K4-TLM simulator should use:

```markdown
> → Primary: [K4-TLM Simulator — Vol 4](../vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md) — native lattice dynamics simulator; K4 graph topology, scattering matrix eq:k4_scatter, validation (source: Vol 4 Ch.13, sec:k4_tlm)
```

The stable relative path from any vol3 document back to vol4 is always
`../vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md`
(one up from vol3/, then into vol4/).

### Leaf marker (line 2 of every leaf document)

```html
<!-- leaf: verbatim -->
```

Placeholder variant:
```html
<!-- leaf: placeholder — source: Vol 4 Ch.N, section "..." -->
```

---

## 5. Shared Content Decision: `common/translation_*.tex` Tables

**Recommendation: Option (a) — Dedicated pages at `ave-kb/common/`**

**Reasoning:**

The `translation_circuit.tex` table is confirmed to appear in:
- Vol 4 Ch.1 (as `tab:trans_circuit`, the primary usage in the manuscript)
- `backmatter/01_appendices.tex` (shared across all volumes)

If the table is duplicated in each volume section that includes it, any
correction to the table content requires updating N files. More importantly,
from an agent navigation standpoint, duplication forces the agent to choose
between two leaves that claim to be the same content, creating ambiguity about
which is authoritative.

A single `ave-kb/common/translation-circuit.md` is the authoritative leaf.
Vol 4 Ch.1's `topo-kinematic-identity.md` leaf includes:

```markdown
> → Primary: [Translation Table — Topo-Kinematic Circuit Identity](../../../common/translation-circuit.md) — six-row table mapping mechanical to circuit quantities; source: common/translation_circuit.tex, also tab:trans_circuit in Vol 4 Ch.1
```

If other volumes (Vol 1, Vol 2, Vol 5) also reference the circuit translation
table, their relevant leaves include the same Primary pointer to
`ave-kb/common/translation-circuit.md`. No duplication.

**Scope note for `ave-kb/common/`:** Only content that appears verbatim in the
shared `common/` or `backmatter/` source files belongs here. Volume-specific
derivations that merely cite a common result do not. Currently the only
confirmed candidate is `translation-circuit.md`; others should be added only
when the survey for that shared file confirms multi-volume usage.

---

## 6. Anomaly Notes Affecting Taxonomy Design

The following survey anomalies have structural implications:

1. **`sec:ee_bench` label absent from Ch.12** (Anomaly 8): The KB leaf
   `ee-bench-dielectric-plateau.md` is the stable navigable anchor. The
   leaf's header comment must note that the source section has no `\label`
   in the manuscript. Cross-references should point to the KB path, not to
   a LaTeX label.

2. **Dangling refs in Ch.11 `sec:induced_vacuum_impedance_mirror`** (Anomaly 3):
   `sec:topological_defects_lc`, `sec:point_yield`, and
   `eq:dielectric_saturation` are referenced but not defined in Vol 4.
   The leaf `induced-vacuum-impedance-mirror.md` should carry a distiller
   annotation: `<!-- note: sec:topological_defects_lc, sec:point_yield, eq:dielectric_saturation referenced here but defined outside Vol 4 — resolution pending cross-volume KB completion -->`.
   This is an addendum-level issue, not a structural one.

3. **Ch.11 prose numbering inconsistency** (Anomaly 4): Ch.11 refers to
   "Chapter 13" for the charge-displacement identity, which is actually Ch.1
   content. The leaf `induced-vacuum-impedance-mirror.md` and the Ch.11 index
   should note this. Do not create a leaf for "Ch.13 charge-displacement" —
   the correct leaf is `topo-kinematic-identity.md` in `circuit-theory`.

4. **Orphaned `circuit_sagnac_rlvg.tex`** (Anomaly 1): Excluded from KB.
   Not in manifest, not compilable, not distillable. No node created.

5. **Summarybox/exercisebox boilerplate** (Anomaly 5): No leaves created for
   summarybox or exercisebox content in any chapter. These are confirmed
   boilerplate and have no distillable content.

6. **Ch.7 brevity** (Anomaly 6): ~57 lines → 2 leaves only (`force-free-field.md`
   and `smes-falsification.md`). Chapter index is still required for
   navigation but will be thin. This is expected and correct.

7. **Ch.18 figure path anomaly** (Anomaly 9): Ch.18 uses `../../assets/sim_outputs/`
   for figure paths. This is a LaTeX compilation concern only — no impact on
   KB taxonomy design. Note in Ch.18 leaf headers if figures are referenced.

---

## 7. Acceptance Criteria

The following properties must hold when Vol 4's KB section is complete.
All are machine-verifiable unless marked (manual).

1. **Up-link presence**: Every `.md` file under `ave-kb/vol4/` except
   `ave-kb/vol4/index.md` begins with a line matching `^\[↑ `.
   ```
   find /path/to/ave-kb/vol4 -name "*.md" ! -name "index.md" \
     | xargs grep -L '^\[↑ '
   ```
   The command must return no files.

2. **Leaf marker presence**: Every leaf document (terminal node, not an index)
   has `<!-- leaf: verbatim -->` or `<!-- leaf: placeholder` on line 2.
   ```
   # Index files excluded; leaves identified by not having "## Contents" section
   ```
   (Manual check during distillation review: any leaf lacking the marker is a
   navigation classification error.)

3. **Depth constraint**: No file path under `ave-kb/vol4/` exceeds 4 directory
   levels below `ave-kb/`. The skeleton maximum is:
   `ave-kb/vol4/{domain}/{chapter}/{leaf}.md` = 4 levels.
   ```
   find /path/to/ave-kb/vol4 -name "*.md" \
     | awk -F'/' '{print NF}' | sort -n | tail -1
   ```
   Must be ≤ (base_depth + 4).

4. **Entry-point token budget**: `ave-kb/entry-point.md` is under 3000 tokens.
   Conservative proxy: `wc -w ave-kb/entry-point.md` must return ≤ 2200 words.

5. **K4-TLM reachability**: The file
   `ave-kb/vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md`
   exists and contains `<!-- leaf: verbatim -->` on line 2.
   This is the cross-volume anchor for Vol 3 references.

6. **CLAUDE.md invariant coverage**: Each constant named in `ave-kb/CLAUDE.md`
   (V_yield, V_snap, S(V), xi_topo) must appear in at least 2 distinct domain
   index files under `ave-kb/vol4/`. Manual check: scan domain index files for
   the constant symbol.

7. **No summarybox/exercisebox leaves**: No leaf document's content is derived
   solely from a summarybox or exercisebox environment.
   ```
   grep -r "summarybox\|exercisebox" ave-kb/vol4/
   ```
   Must return no files.

8. **No leaf summarization**: No leaf document contains a `## Summary` or
   `## Overview` heading (these signal distiller wrote prose instead of
   translating verbatim source).
   ```
   grep -rl "^## Summary\|^## Overview" ave-kb/vol4/
   ```
   Must return no files.

9. **Ch.11 protocol completeness**: The directory
   `ave-kb/vol4/falsification/ch11-experimental-bench-falsification/`
   contains exactly 22 `.md` files (1 index + 21 leaves as enumerated in
   the skeleton). Manual check against skeleton.

10. **Simulation chapter netlist leaves**: Each of the four simulation
    chapters (14-17) has exactly one SPICE-codebox leaf (named
    `*-spice.md`). These leaves must contain the verbatim netlist text,
    not a summary of it.
    ```
    find ave-kb/vol4/simulation -name "*-spice.md" | wc -l
    ```
    Must return 4.

---

## 8. File Count Summary

| Category | Count |
|----------|-------|
| `ave-kb/CLAUDE.md` | 1 |
| `ave-kb/entry-point.md` | 1 |
| `ave-kb/common/translation-circuit.md` | 1 |
| `ave-kb/vol4/index.md` | 1 |
| Domain index files (6 domains) | 6 |
| Chapter index files (18 chapters) | 18 |
| Leaf files (see breakdown below) | 146 |
| **Total** | **174** |

### Leaf file breakdown by domain

| Domain | Chapter(s) | Leaves |
|--------|-----------|--------|
| circuit-theory | Ch.1 (8 leaves) + Ch.2 (4 leaves) | 12 |
| hardware-programs | Ch.3 (7) + Ch.4 (3) + Ch.5 (6) + Ch.6 (5) | 21 |
| advanced-applications | Ch.7 (2) + Ch.8 (9) + Ch.9 (2) + Ch.10 (4) + Ch.18 (3) | 20 |
| falsification | Ch.11 (21) + Ch.12 (9) | 30 |
| future-geometries | Ch.13 (5) | 5 |
| simulation | Ch.14 (2) + Ch.15 (2) + Ch.16 (2) + Ch.17 (2) | 8 |
| **Total leaves** | | **96** |

**Note on count vs. estimate:** The skeleton enumerates 96 leaves for the
chapter content plus 1 common leaf = 97 leaves total. The survey estimated
140-160. The gap reflects a deliberate structural choice: where a survey
section groups multiple closely related resultboxes that derive from the
same source passage (e.g., Ch.1's seven translation identity resultboxes),
a single leaf captures all of them verbatim. Artificially splitting
inseparable adjacent content into one leaf per resultbox would create
15-20 micro-leaves that an agent would need to read sequentially anyway.
The distiller should stay faithful to this grouping; if a source passage
genuinely spans 2+ logical topics, it may be split, but that decision is
deferred to distillation rather than pre-specified here.

---

*Taxonomy design complete. Produced by kb-taxonomy-architect.*
*Source survey: phase0-surveys/vol4_survey.md*
*Date: 2026-04-02*
