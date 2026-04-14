# Volume 4 Surgical Plan: Section-by-Section Triage

> [!IMPORTANT]
> This is the most invasive partition in the entire AVE-Core manuscript.
> Volume 4 is the "Engineering" application volume—the place where the theory deliberately
> operationalizes into hardware test protocols. The majority of chapters 11 and 12 are
> dominated by proprietary APU thrust/propulsion IP. This plan maps **every section** to
> one of three dispositions: **KEEP**, **EXTRACT**, or **SCRUB**.

## Disposition Legend

| Tag | Meaning |
|-----|---------|
| ✅ KEEP | Section remains in public `AVE-Core` untouched |
| 🔴 EXTRACT | Entire section migrates to private `AVE-Hardware` repo |
| 🟡 SCRUB | Section stays but specific terminology is renamed |

---

## Chapter 01: `01_vacuum_circuit_analysis.tex` (723 lines)

This chapter is the crown jewel—the Topo-Kinematic Identity, VCA Smith Chart, constitutive
models, S-parameter analysis, and IMD spectroscopy. It is almost entirely clean.

| Lines | Section | Disposition | Notes |
|-------|---------|-------------|-------|
| 1–101 | Topo-Kinematic Identity & 6-Row Table | ✅ KEEP | Pure theory |
| 122–224 | Constitutive Circuit Models (Varactor, Inductor, TVS, Memristor) | ✅ KEEP | Core physics |
| 226–250 | Zero-Impedance Skin Effect | ✅ KEEP | Generic theory |
| 251–366 | Impedance of Free Space, Gravitational Stealth, Horizon Mirror | ✅ KEEP | Core physics |
| 368–376 | Periodic Table SPICE Mappings | ✅ KEEP | Cross-ref to Vol 6 |
| 391–500 | Topological Defects as LC Solitons, Pauli Exclusion | ✅ KEEP | Core physics |
| 502–560 | Real vs Reactive Power (Orbital Friction Paradox) | ✅ KEEP | Core physics |
| 561–656 | IMD Spectroscopy | ✅ KEEP | Falsifiable prediction |
| 658–707 | Solver Selection | 🟡 SCRUB | Line 692: rename `Ponderomotive thrust (PONDER)` → `Non-linear dielectric stress` |
| | | | Line 696: rename `Warp metric CFD (superluminal transit)` → `High-strain impedance CFD` |
| 4–9 | Objective Box | 🟡 SCRUB | Line 8: `Compute ponderomotive thrust` → `Compute macroscopic non-linear topological stress` |

**Summary: 2 minor scrubs. No extractions needed.**

---

## Chapter 11: `11_experimental_falsification.tex` (645 lines)

This is the most complex chapter. It mixes brilliant, universally valuable falsification
epistemology with deeply specific hardware test-vehicle blueprints. The surgery must
preserve the intellectual framework while excising the proprietary implementations.

| Lines | Section | Disposition | Notes |
|-------|---------|-------------|-------|
| 1–11 | Objective Box | ✅ KEEP | Generic falsification epistemology |
| 12–24 | Epistemology of Falsification (Neutrino, GRB, Birefringence) | ✅ KEEP | Core kill-switches |
| 26–31 | Birefringence Kill Switch figure | ✅ KEEP | |
| 31–57 | Tabletop Graveyard (VFDT, RVR null results) | 🟡 SCRUB | Lines 48-49: Remove "Tungsten rotor" specifics, keep the Q×δ_L analysis as a generic "dense metallic mass" |
| 58–147 | **Sagnac-RLVE** (rotor specs, fiber specs, $\Psi$ ratio, FOG discussion) | 🔴 EXTRACT | This is a complete, specific hardware test protocol with exact BOM, dimensions, RPM. **Entire section → AVE-Hardware.** Public core gets a 2-paragraph stub: "The Sagnac mutual inductance experiment is detailed in the companion Hardware Testing Manual." |
| 151–196 | Existing Experimental Signatures (Proton Radius, Neutron Lifetime, Hubble Tension, LIGO Echoes, Vortex Cores) | ✅ KEEP | Brilliant retrospective analyses. Pure theory. |
| 197–208 | **Project CLEAVE-01** (Femto-Coulomb Electrometer) | ✅ KEEP | This is a solid-state EE experiment. No thrust, no rotors. Generic PCBA metrology. Safe for public. |
| 210–222 | **Project HOPF-02** (S-Parameter VNA Falsification + Snell Parallax) | ✅ KEEP | Solid-state antenna S₁₁ measurement. No thrust. |
| 224–229 | **Project ROENTGEN-03** (Solid-State Sagnac Induction) | 🔴 EXTRACT | Involves spinning ceramic disk at 10,000 RPM + 4.2 pT field synthesis. Hardware-specific. → AVE-Hardware |
| 231–244 | **Project ZENER-04** (Impedance Avalanche Detector) | ✅ KEEP | Generic Marx Generator electrode test. No thrust. Solid-state falsification. |
| 246–270 | **Levitation Limit & Dielectric Death Spiral** | 🟡 SCRUB | The 1.846g derivation is **pure theory** and should stay. Remove the "Transient Asymmetric Metric Drive (TAMD)" hardware implementation details (lines 265–270). Keep the mathematical limit. |
| 272–288 | **Project TORSION-05** (Horizontal Metric Rectification) | 🔴 EXTRACT | Explicit macroscopic DC thrust on a Cavendish torsion balance. **Entire section → AVE-Hardware** |
| 289–300 | **YBCO Phased Array** (beating 2.5g limit via 1M micro-inductors) | 🔴 EXTRACT | Spacecraft hull PCBA design. **Entire section → AVE-Hardware** |
| 302–327 | **Metric Refraction Capacitor** ($c^2$ Multiplier, 130 G's) | 🔴 EXTRACT | BaTiO₃ warp drive capacitor. **Entire section → AVE-Hardware.** The $a = c^2 \nabla n$ provenance paragraph (lines 313-318) is standard GR and could stay as a standalone derivation. |
| 328–346 | **Sapphire Phonon Centrifuge** (artificial gravity, 6.35 G's) | 🔴 EXTRACT | Artificial gravity centrifuge. **Entire section → AVE-Hardware** |
| 353–363 | **Metric Boundary Layer Sensors & Redline Gauges** | 🔴 EXTRACT | Spacecraft telemetry. **Entire section → AVE-Hardware** |
| 364–373 | Sonoluminescence FOC Isomorphism | ✅ KEEP | Pure physics (bubble dynamics). No hardware. |
| 375–413 | **Open-Source Hardware: HOPF-01 & PONDER-01 Build Guides** | 🔴 EXTRACT | Complete PCBA fabrication instructions with exact part numbers, trace routing, avalanche transistor specs. **Entire section → AVE-Hardware** |
| 414–433 | Zero-Parameter Derivations ($\sqrt{\alpha}$ yield, fusion limit, levitation limit) | ✅ KEEP | Pure axiomatic derivations. |
| 435–455 | Horsemen of Falsification (LHC Paradox, LIGO Paradox) | ✅ KEEP | Brilliant theoretical rebuttals. |
| 456–576 | Protocols 9–12 (Achromatic Lens, Boundary Trapping, Vacuum Mirror, Sagnac-Parallax, GEO Impedance) | ✅ KEEP | These are theoretical predictions and experimental *concepts*, not detailed hardware builds. |
| 577–629 | Protocols 13–14 (Amphoteric GaAs, Thermal Rigidity) | ✅ KEEP | Semiconductor falsification protocols. Pure solid-state physics. |
| 631–645 | Summary & Exercises | ✅ KEEP | |

**Summary: 8 full section extractions. 2 scrubs. ~200 lines migrated to AVE-Hardware.**

---

## Chapter 12: `12_falsifiable_predictions.tex` (273 lines)

| Lines | Section | Disposition | Notes |
|-------|---------|-------------|-------|
| 1–46 | EE Bench: Macroscopic Dielectric Plateau | ✅ KEEP | Generic solid-state capacitance measurement. |
| 48–100 | **Ponder-01: Asymmetric Maxwell Stress Rectification** | 🔴 EXTRACT | Explicit unidirectional macro-thrust via torsion balance. Dark Wake tensor. **Entire section → AVE-Hardware** |
| 102–108 | Epistemology of Falsification (brief reprise) | ✅ KEEP | Duplicates Ch.11 §1 but harmless. |
| 110–184 | **Sagnac RLVG Entrainment Law + Telemetry** | 🔴 EXTRACT | Density-dependent Sagnac anomalies, differential Sagnac arrays, 3D metric gradient compass, Dark Wake sensor, chiral torsion sensor. **All spacecraft navigation IP → AVE-Hardware** |
| 186–192 | Helicity Injection (Hopf coupling theory) | ✅ KEEP | Pure EM theory of torus knot coupling. |
| 194–201 | Autoresonant Dielectric Rupture (Schwinger Limit) | ✅ KEEP | Generic nonlinear dynamics / Duffing oscillator theory. |
| 202–233 | Binary Kill-Switches + Vacuum Birefringence $E^4$ | ✅ KEEP | Core falsification criteria. |
| 235–258 | Torus Knot Ladder: Baryon Mass Predictions | ✅ KEEP | Zero-parameter particle physics prediction. |
| 259–273 | Summary & Exercises | ✅ KEEP | |

**Summary: 2 full section extractions. ~135 lines migrated.**

---

## Chapter 13: `13_future_geometries.tex` (474 lines)

| Lines | Section | Disposition | Notes |
|-------|---------|-------------|-------|
| 1–12 | Objective Box | ✅ KEEP | |
| 14 | Opening paragraph | 🟡 SCRUB | `PONDER-01 asymmetric PCBA` → `asymmetric high-voltage array` |
| 18–70 | Toroidal/Poloidal Fusion, Vector Scaling vs Knot Volumetrics | 🟡 SCRUB | Lines 41, 47, 78: Replace `thrust` with `topological stress`, `PONDER-01` with `asymmetric dielectric array`. Keep the physics of Hopf helicity injection. |
| 72–95 | Acoustic Back-Reaction Analogy + Thruster Topology Table | 🔴 EXTRACT | The table explicitly compares "thrust (1 kW)" across topologies. Migration target: AVE-Hardware. Keep the acoustic back-reaction *concept* but strip the thrust numbers. |
| 97–172 | High-Q Chiral Impedance Antenna (FoM, RX/TX, Matching Network, Sensitivity) | ✅ KEEP | Pure RF antenna engineering. No thrust. |
| 174–304 | CEM Solver Survey (MoM, FDTD, FEM, TLM, CMA, PO/GO) | ✅ KEEP | Pure computational electromagnetics pedagogy. Excellent. |
| 320–456 | K4-TLM Simulator (Scattering Matrix, Validation, 3D Antenna) | ✅ KEEP | Core physics engine documentation. |
| 458–474 | Summary & Exercises | ✅ KEEP | |

**Summary: 1 extraction, 2 scrubs. ~25 lines migrated.**

---

## `_manifest.tex` (27 lines)

| Lines | Section | Disposition | Notes |
|-------|---------|-------------|-------|
| 7 | `% Chapters 02–06: ... → AVE-PONDER, AVE-HOPF (private)` | 🟡 SCRUB | Remove private repo names. Replace with `% Chapters 02–06: Extracted to companion volumes` |
| 21 | `% Chapter 17: Hardware SPICE → AVE-APU (private)` | 🟡 SCRUB | Same treatment |
| 22 | `% Chapter 18: Active metamaterials → AVE-Metamaterials (private)` | 🟡 SCRUB | Same treatment |

---

## Aggregate Migration Summary

| Chapter | KEEP | EXTRACT | SCRUB |
|---------|------|---------|-------|
| Ch.01 VCA | ~710 lines | 0 lines | ~13 lines |
| Ch.11 Experimental | ~370 lines | ~200 lines | ~15 lines |
| Ch.12 Predictions | ~170 lines | ~135 lines | 0 lines |
| Ch.13 Future Geometries | ~420 lines | ~25 lines | ~10 lines |
| `_manifest.tex` | 24 lines | 0 lines | 3 lines |
| **TOTAL** | **~1694 lines** | **~360 lines** | **~41 lines** |

> [!WARNING]
> The ~360 extracted lines contain the most commercially sensitive IP in the entire repository:
> specific PCBA layouts, BOM part numbers, thrust-to-power ratios, spacecraft hull designs,
> and engine safety telemetry. These must be migrated to a private repo **before** any
> public release of AVE-Core.

## Execution Order

1. **Create receiving stubs** in `AVE-Hardware` repo for each extracted section
2. **Copy** (not move) the extracted LaTeX blocks into the hardware repo
3. **Replace** each extracted section in AVE-Core with a 2-line stub:
   ```latex
   \subsection*{[Section Title]}
   \textit{The detailed hardware implementation is documented in the AVE Hardware Testing Manual (companion volume).}
   ```
4. **Apply scrubs** (terminology renames) across all files
5. **Verify build** — ensure `latexmk` compiles cleanly with stubs
6. **Commit** with message: `feat(vol4): partition hardware IP to AVE-Hardware`
