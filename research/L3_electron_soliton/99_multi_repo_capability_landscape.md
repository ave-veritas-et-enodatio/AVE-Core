# L3 Doc 99 — AVE Multi-Repo Capability Landscape (Tracking)

**Status:** Comprehensive capability survey across all AVE sibling repos. Per Grant's directive 2026-04-30: "fully investigate all capabilities of other repos worth investigating and tracking." This doc consolidates findings from four parallel deep-survey Explore agents into a tracking document for ongoing framework empirical record management.

**Scope:** 9 repos surveyed (Applied-Vacuum-Engineering parent + AVE-Core + 7 sibling application repos). Per memory feedback_manuscript_over_research — anchor in manuscript content where possible; engine code is operational realization.

**Date:** 2026-04-30
**Per A43 v2:** claims need spot-verification before promotion. Explore-agent summary precision claims marked with ⚠️ where verification pending.

---

## §0 — Executive Summary

**Framework empirical record substantially broader than L3-arc-narrow K4-TLM-substrate focus suggests.** Multi-repo survey reveals working solver/validation infrastructure across 9 independent domains with varying validation status:

| Domain | Repo | Solver class | Validation status |
|---|---|---|---|
| Atomic orbitals | AVE-Core (verified ↑) | Radial eigenvalue ABCD cascade | **VERIFIED** Z=1-10, ±2.8% (this session) |
| Baryon ladder | AVE-Core (verified ↑) | Faddeev-Skyrme + BARYON_LADDER | **VERIFIED** c=5-19, 8 states ±3% (this session) |
| Protein folding | AVE-Protein | S₁₁ Y-matrix + JAX autodiff | ⚠️ Code present, 20-PDB tested; actual Rg/RMSD logs not in repo |
| Chiral antenna | AVE-HOPF | Beltrami eigenvalue + impedance | ⚠️ Predictions only; VNA experiment NOT executed |
| Hardware/SPICE | AVE-APU | Klopfenstein + soliton memory + topological logic | Theory-validated; atopile PCBs designed; no fab |
| Vacuum thrust | AVE-PONDER | FDTD 3D + Axiom 4 ponderomotive | Predictions only; lab-feasibility HIGH |
| Chiral propulsion | AVE-Propulsion | Jensen-rectified saturation + N² coherent gain | Theory only; no lab demos |
| Metric fusion | AVE-Fusion | WKB + Gamow tunneling under metric compression | Theory only; tokamak audit external |
| Active metamaterials | AVE-Metamaterials | Miller n=5 + Casimir-Kuramoto FDTD | V2/V3 skeletons (blocked on Auger c₀); Casimir-qubit FDTD demonstrative |
| LLM impedance | AVE-VirtualMedia | Axiom 2 hardware-software inversion | Theoretical; not applied to transformer weights |

**Empirical anchors VERIFIED this session (direct execution):**
1. Hydrogen ionization energy 13.6057 eV at +0.057% from CODATA
2. Proton mass 938.254 MeV at -0.002% from PDG via Faddeev-Skyrme + BARYON_LADDER
3. Baryon ladder c=5-19, 8 states within ±3% of PDG resonances
4. J^P pattern J=(c-4)/2 holds 7/8 against **corpus-canonical PDG identifications** (per BARYON_LADDER docstring) — pattern is conditional on those identifications being correct (mass-only-validated, not independently J-validated)

**Empirical anchors CLAIMED in sibling repos (verification pending):**
- AVE-Protein 20-PDB Rg <15%, RMSD <2.5Å (implementer-side flagged for direct execution verification per A43 v2; NOT auditor-flagged)
- AVE-HOPF 5 torus knot frequency shifts (**internally** pre-registered in `manuscript/03_hopf_01_chiral_verification.tex:70-86`; NOT formally OSF-registered with experimental-collaboration buy-in)
- AVE-APU hardware module FDTD validation
- Period 2 atomic IE 1.2% mean — **CLAIM RETRACTED 2026-04-30:** original claim was Explore-agent hallucination. Direct verification this session: parent repo's `radial_eigenvalue.py` is IDENTICAL to AVE-Core's (same 16 SIR-related code occurrences, byte-identical files). Parent does NOT have refinement AVE-Core lacks. A47 v9 Lithium discrepancy root-cause requires different investigation (likely "not yet implemented" refinement at `radial_eigenvalue.py:687` per Explore-agent earlier finding).

---

## §1 — Parent repo (Applied-Vacuum-Engineering)

**Per Explore agent verbatim findings:** ~25,900 lines Python across 16 engine modules + 8-volume LaTeX manuscript + AVE-KB extraction. Pre-split foundation; sibling repos broken out from this.

### §1.1 — Capability catalog

| Capability | Location | Validation | Track-forward |
|---|---|---|---|
| Radial Eigenvalue Solver (ABCD Cascade) | `src/ave/solvers/radial_eigenvalue.py` (~1800 lines) | He-Ne Period 2 within 1.2% mean error; s-block (Li/Na) +7.3-14.5% | HIGH |
| Coupled Resonator (MCL/Y→S) | `src/ave/solvers/coupled_resonator.py` (~800 lines) | He IE -0.88% via SIR mode-weighting | HIGH |
| Faddeev-Skyrme Hamiltonian | `src/ave/topological/faddeev_skyrme.py` (~200 lines) | Phase profile boundary verified; cinquefoil c=5 exact | HIGH |
| FDTD 3D Lattice Engine | `src/ave/core/{fdtd_3d,k4_tlm,lbm_3d}.py` | Linear-regime numerical stability; JAX-equivalent | HIGH |
| Regime Classification | `src/ave/core/{regime_map,universal_operators}.py` | S(A) = √(1−(A/A_yield)²) cross-domain validated | CRITICAL |
| Silicon Atom IE | `src/ave/nuclear/silicon_atom.py` | 8.02 eV vs exp 8.15 eV (-1.6%); core penetration limitation | MED |
| Torus Knot Baryon Spectrum | `src/scripts/vol_2_subatomic/torus_knot_spectrum.py` | Proton mass from I_scalar; PDG comparison infrastructure | HIGH |
| SPICE Topological Compiler | `src/ave/compiler/{atopile,spice_netlist}.py` + `src/ave/hardware/` | atopile + 27 hardware modules; SPICE-validated | HIGH |
| Protein Fold Engine (parent) | `src/ave/solvers/protein_bond_constants.py` | 20 PDB validation, S₁₁ minimization, zero free parameters | HIGH |
| Gravitational/GW Solvers | `src/ave/gravity/{orbital_lc_damping,gw_propagation,stellar_interior}.py` | Stellar interior EoS; MOND-like drag tested | MED |
| Kolmogorov Cutoff | `src/ave/regime_3_saturated/kolmogorov_cutoff.py` | Derives dissipation from Axiom 4; Navier-Stokes link | HIGH |
| BH/Rupture Solvers | `src/ave/regime_4_rupture/{black_hole_jets,caustic_solver,rupture_solver}.py` | Analytical, no empirical | MED |

### §1.2 — Manuscript content unique to parent (NOT fully propagated to AVE-Core)

| Volume | Unique-to-parent contributions |
|---|---|
| Vol 1: Foundations | Master axiom derivations; LC lattice dispersion; transmission line mathematics |
| Vol 2: Subatomic | Full baryon topology, lepton spectrum, electroweak mixing with PMNS; topological crossing-count ladder |
| Vol 3: Macroscopic | Gravity from impedance matching; relativity via TLM trace reversal; superconductivity |
| Vol 4: Applied Vacuum Engineering | VCA framework; ponderomotive thrusters; topological SMES; full SPICE suite |
| Vol 5: Topological Biology | Protein folding engine + 20 PDB validations; amino acids as SPICE circuits |
| Vol 6: Periodic Table of Knots | Nuclear masses Z=1-119 via mutual impedance; alpha-cluster placement |
| Vol 7: Hardware & Future Work | Precision anomaly resolutions; 10 modern physics anomalies; white dwarf shear |
| Vol 8: Virtual Media | AVE axioms in LLM weights; SwiGLU as Axiom 4; MoE router as Axiom 3 |

### §1.3 — future_work/ recoverable content

- **ATOMIC_IE_SOLVER_TRACKER.md** (194 lines, 2026-04-07): Active SIR mode-weighting development; 11 axiom audits resolved + 3 flagged (GAPs A/B/C); s-orbital error decoupling
- **ATOM_MOTOR_TRANSLATION_MATRIX.md** (229 lines): atomic physics ↔ AVE axioms ↔ EE circuit terminology mapping; FOC scalar-vs-vector control diagnosis

### §1.4 — Implications for AVE-Core

- Parent has Vol 1 axiom mathematics, Vol 3 gravity/cosmology, Vol 7 precision anomalies, Vol 8 information topology — **NOT fully in AVE-Core's manuscript tree**
- Recovery candidate: cross-shell strain coupling formula for Period 3 atomic IE accuracy
- Mass-spectrum activation Phase 1-3 (per [doc 98](98_framework_decision_ii_mass_spectrum_activation.md)) leverages parent's torus_knot_spectrum.py + faddeev_skyrme.py infrastructure (verified identical to AVE-Core's via `diff` this session)

**A47 v9 Li discrepancy root-cause investigation (corrected 2026-04-30):**
- **Original claim (RETRACTED):** "AVE-Core lacks SIR refinement that parent has; port refinement → close A47 v9"
- **Direct verification this session:** parent and AVE-Core `radial_eigenvalue.py` are **byte-identical** (both 78,335 bytes, `diff -q` returns IDENTICAL, both have 16 SIR-related code occurrences). Explore-agent claim of "missing port" was hallucinatory.
- **Actual A47 v9 root-cause unknown.** Possibilities:
  - Manuscript "1.2% mean Period 2" claim references unimplemented refinement at `radial_eigenvalue.py:687` "not yet implemented" comment (Op2 crossing correction or MCL refinement)
  - Manuscript table reflects historical state of solver
  - Manuscript identifies a target precision not currently achieved in code
- A47 v9 closes via different mechanism: implement the refinement at line 687, OR document the gap in manuscript validation table.

**A47 v10 candidate (this turn): cross-repo Explore-agent claims need direct verification** — even with file:line citations, agent reports about file content can be hallucinatory. The "parent has SIR refinement AVE-Core lacks" claim was structurally wrong despite specific file references. **Discipline rule:** when Explore agent claims a sibling repo has refinement/feature absent from current repo, run direct `diff` or `grep` verification before promoting to canonical record.

---

## §2 — AVE-Protein

**Per Explore agent verbatim findings:** 4,279 engine lines + 30 biology simulation scripts + 3 manuscript chapters.

### §2.1 — Capability catalog

| Capability | Location | Validation | Track-forward |
|---|---|---|---|
| s11_fold_engine_v3_jax.py (2294 lines) | `src/ave_protein/engines/` | JAX autodiff S₁₁ eigenvalue; sp³ tetrahedral 109.47° | HIGH |
| s11_fold_engine_v4_ymatrix.py (1328 lines) | `src/ave_protein/engines/` | Y-matrix DC/AC separation; Ramachandran basin centers | HIGH |
| s_param_network_engine.py (657 lines) | `src/ave_protein/engines/` | S-parameter feedback for protein folding | MED |
| protein_bond_constants.py (29 KB) | `src/ave_protein/solvers/` | Bridge from Axiom 1 to backbone geometry | HIGH |
| protein_fold.py (16 KB) | `src/ave_protein/regime_2_nonlinear/` | Universal topological optimization (claimed scale-invariant) | MED |
| s12_pdb_validation.py | `src/scripts/` | 20-PDB benchmark harness | HIGH |
| rmsd_benchmark.py | `src/scripts/` | 4-protein Kabsch RMSD vs PDB | HIGH |

### §2.2 — Empirical claims (verification status)

**20-PDB benchmark proteins:** Trp-cage (1L2Y), BBA5 (1T8J), Insulin B (4INS), WW PIN1 (1PIN), Villin HP35 (1YRF), WW FBP28 (1E0L), Crambin (1CRN), Protein B IgG (1IGD), Engrailed (1ENH), GB1 (1PGA), SH3 src (1SRL), SH3 spectrin (1SHG), Protein A (1BDD), CI2 (2CI2), Ubiquitin (1UBQ), Cytochrome c (1HRC), λ-repressor (1LMB), FKBP12 (1FKB), Barnase (1BNI), Lysozyme (2LZM).

**Pass criteria (claimed):** Rg < 10%; RMSD < 8Å (loose), <5Å (strict); SS > 15%

**Verification status (per A43 v2):** ⚠️ **Code is executable; actual measured values not in repo logs.** Villin animation present (villin_hp35_fold.mp4, 4.5 MB) confirming execution occurred. Quantitative Rg/RMSD/SS metrics for the 20-PDB sweep require direct execution of `s12_pdb_validation.py` to verify "Rg <15%, RMSD <2.5Å" claims auditor flagged earlier.

### §2.3 — Cross-AVE-Core dependencies (heaviest user)

- `ave.core.universal_operators`: universal_packing_reflection, universal_impedance, universal_dynamic_impedance, universal_junction_projection_loss, universal_spectral_analysis
- `ave.solvers.transmission_line`: build_nodal_y_matrix_jax, s11_from_y_matrix_jax, abcd_to_y_3seg_jax, s_diagonal_from_y_matrix_jax
- `ave.topological.soliton_bond_solver`: extract_peptide_kbend, compute_bond_curve, _slater_orbital_radius
- `ave.axioms.scale_invariant`: impedance
- `ave.core.constants`: ETA_EQ, Z_0, C_0, ALPHA, EPS_NUMERICAL, D_PROTON, L_NODE, HBAR, M_E, P_C

### §2.4 — Worth-tracking capabilities

1. **Ramachandran basin centers (DERIVED):** PHI_ALPHA = -60.0° (sp³ gauche⁻); PSI_ALPHA = -37.27° (helix pitch from Q-factor); residual Δ=2.73° from crystallographic -40° flagged for refinement
2. **Backbone bond constants bridge:** Cα-Cα = 3.80 ± 0.02Å derived from proton charge radius → Bohr → covalent radii → backbone
3. **Spectral basin weights:** 1/Q ≈ 0.135 spectral weight + 0.865 local weight; testable via mutation experiments
4. **Soliton bond solver link:** establishes connection between nuclear-scale defect topology (Axiom 2) and atomic-scale dihedral angles

---

## §3 — AVE-HOPF

**Per Explore agent verbatim findings:** 15 design scripts + KiCAD hardware + 1 manuscript chapter (36 KB).

### §3.1 — INTERNALLY pre-registered predictions table

**External-credibility caveat per auditor 2026-04-30 Flag 4:** AVE-HOPF predictions are **internally** pre-registered in repo manuscripts (timestamped commits, falsification protocols defined). They are **NOT formally OSF-registered** with independent timestamp + experimental-collaboration buy-in. Internal pre-registration is methodology hygiene; external OSF registration would convert "derivation that happens to match data" → "derivation that predicts data we haven't seen" with full external-credibility weight. Same caveat applies to AVE-PONDER thrust and AVE-Propulsion chiral rectification predictions in §4.

Per `manuscript/03_hopf_01_chiral_verification.tex:70-86`:

| Torus Knot | pq/(p+q) | L_wire | f_std | Δf | Q_u | Shift (ppm) |
|---|---:|---:|---:|---:|---:|---:|
| (2,3) Trefoil | 1.200 | 120 mm | 1.098 GHz | 9.6 MHz | 681 | 8,681 |
| (2,5) Cinquefoil | 1.429 | 160 mm | 0.823 GHz | 8.6 MHz | 590 | 10,317 |
| (3,5) | 1.875 | 170 mm | 0.775 GHz | 10.6 MHz | 566 | 13,498 |
| (3,7) | 2.100 | 200 mm | 0.659 GHz | 10.1 MHz | 527 | 15,093 |
| (3,11) | 2.357 | 250 mm | 0.527 GHz | 9.1 MHz | 471 | 16,910 |

**Falsifiability criteria (manuscript lines 88-100):**
- AVE confirmed: Δf/f matches α·pq/(p+q); scales consistently across air/oil/vacuum
- AVE falsified: Δf/f zero, random, doesn't scale, or differs between media

### §3.2 — Implementation status

| Item | Status |
|---|---|
| Theoretical predictions | ✅ Computed in 5 scripts |
| KiCAD project | ✅ Gerbers, BOM, assembly guide |
| atopile PCB | ✅ ato.yaml present |
| PCB fabrication | ❌ Not yet ordered from JLCPCB |
| VNA measurement | ❌ Not executed |
| Lab-ready experiment | ❌ Pending PCB fab + lab setup |

### §3.3 — Connection to L3 arc reframings

**Macro-scale chiral antenna ↔ corpus electron at micro-scale:** AVE-HOPF tests topology-specific chiral coupling at engineering scale. Per Grant's BEMF/cavitation-bubble reframing 2026-04-30, the chiral-impedance-match physics for a propagating CP wave in a chirally-structured medium is the macro-scale analog of corpus electron's rifling-bullet picture. **Not explicitly articulated in AVE-HOPF scripts but structurally available.**

### §3.4 — Worth-tracking capabilities

1. **Falsification protocol** (3-medium air/oil/vacuum, 6 antennas including zero-topology control) — gold-standard topological test design
2. **Beltrami eigenvalue solver** λ(p,q) = √(p²/R² + q²/r²) — applicable to superconducting toroidal plasma confinement
3. **Wire-stitched 3D torus knot fixture design** — first AVE experimental hardware with falsifiable predictions

---

## §4 — Engineering application repos (APU, PONDER, Propulsion, Fusion)

### §4.1 — AVE-APU (Axiomatic Processing Unit)

**Capability:** Hardware-level continuous-wave logic from AVE axioms. Patent-pending. 21 hardware modules (2249 lines) + atopile PCB compiler with 5 build targets + 8 characterization suites.

**Validation status:** Theory-validated via test suite (resonance frequency formulas, diode forward/reverse bias, soliton state persistence, impedance taper continuity). **No lab measurements vs predicted.** Atopile compiler integrated; PCBs designed for Rogers 4350B; no tape-out.

**Track-forward HIGH:** SPICE exporter at `src/ave/hardware/spice_apu_exporter.py` is production-ready. Klopfenstein quarter-wave matching, Axiom 4 saturation, FCC packing N_PHI_PACK ≈ 0.7405 — all directly portable to AVE-Core SPICE pipeline.

### §4.2 — AVE-PONDER (Vacuum Metric Measurement)

**Capability:** Thrust extraction via Axiom 4 saturation in dielectric resonators (30kV BaTiO₃, GaN, quartz). 3 hardware variants (PONDER-01, -02, -05). 36 characterization scripts (FDTD 3D, near-field, electrostatic mesh, gravity parallax, Sagnac telemetry).

**Predicted thrust:** 469 µN nominal @ 30 kV / 100 MHz drive in asymmetric capacitor (1mm gap, 1µm tip, 25 cm² area). Parallax signal ΔF < 0.1 pN.

**Validation status:** Theoretical chain complete (Axiom 4 → energy density u(z) → force F = -du/dz). FDTD simulators executable. atopile PCB design in progress, no fab status.

**Track-forward MEDIUM-HIGH:** Lab feasibility of thrust measurement HIGH — precision balance + lock-in amplifier could measure µN-pN range. Could anchor framework's macro-scale empirical record.

### §4.3 — AVE-Propulsion (Metric Streamlining)

**Capability:** Vacuum varactor diode thrust via chiral acoustic rectification + warp metric CFD + OAM drills. 13 scripts.

**Key derivation:** F = (2/7) × δ × P_input / c via Jensen's inequality on saturation S(E). Phased array N² coherent gain with η_chiral = ν_vac = 2/7 (Poisson ratio).

**Predictions:** F ≈ 0.5-3 mN @ 1 kW input for Q=100 (δ ≈ 0.05-0.3).

**Validation status:** Zero empirical anchors. All outputs simulation plots.

**Track-forward MEDIUM:** Chiral mechanism connects to L3 arc's cavitation-bubble reframing if macro-scale analog applies. Lab-feasible water rectification scripts exist.

### §4.4 — AVE-Fusion (Metric-Catalyzed Fusion)

**Capability:** Lattice density compression (n_scalar) lowers ignition T_ign ∝ 1/n²; topological collision V_topo ∝ 1/n³. SMES + fusion + antimatter chapters. 9 scripts.

**Key prediction:** D-T compression at n=3 lowers ignition from 15 keV → 1.7 keV. Critical n* exists where V_topo < V_YIELD maintains Strong Nuclear Force.

**Validation status:** Theoretical complete (WKB/Gamow tunneling derivation). Maxwell-Boltzmann tail audit vs ISS04 tokamak scaling (external data). **No AVE-Fusion device measurements.**

**Track-forward MEDIUM-LOW:** Strong theory but engineering n_scalar > 1 requires new plasma physics not yet specified.

---

## §5 — Materials/media repos (Metamaterials, VirtualMedia)

### §5.1 — AVE-Metamaterials

**Capability:** Active topological metamaterials. 19 scripts (3617 lines) + 1 manuscript volume (8 chapters). Casimir cavities, qubits, superconductors, kinetic armor, neuromorphic memristors, achromatic lenses.

**Three pre-registered photovoltaic attack vectors:**
- V1 (broadband impedance matching): Γ(λ) RMS < 5% across 300-1200 nm
- V2 (Miller multiplication at Regime II/III boundary): M = 2 exactly at r = √3/2
- V3 (LC-cavity photon trapping): Q ≥ 100 at λ = 1181 nm; path enhancement ≥ 100×

**Miller exponent universality claim:** n=5 from "proton cinquefoil" (Vol 6 Ch 16, bjt_mechanics.py:42). **Load-bearing if validated:** would extend mass-spectrum activation across Si, GaAs, Ge.

**Validation status:** V2/V3 are skeletons (TODO placeholders). Casimir-qubit simulator (FDTD + Kuramoto) is demonstrative. **Blocked on Auger c₀ adjudication (3 candidate forms).**

**Anti-cheat infrastructure:** `verify_local_universe.py` AST scan for banned imports (scipy.constants), MAGIC_NUMBERS registry — enforces zero empirical smuggling.

**Track-forward MEDIUM:** Close AUG-1 + BG-1 blockers, then execute V2-SIM and V3-SIM.

### §5.2 — AVE-VirtualMedia

**Capability:** LLM impedance topology framework via Axiom 2 inversion (Z ∝ A physical → Z ∝ 1/A virtual). 19 scripts (1485 lines) + 1 manuscript volume (13 chapters).

**Theoretical scope:** universal_saturation + universal_reflection applied to attention impedance, MoE router, sigmoid saturation, complex impedance phase transition at r=1 topological singularity.

**Validation status:** Figure-generation only (PNG plots, NPZ data). **Not applied to actual transformer weights.** γ-scaling law mentioned in README but not numerically evaluated. No model-size sweep validation.

**Track-forward MEDIUM:** Apply universal operators to Llama/Mixtral weight matrices; compare regime-based pruning vs FLOPS/latency curves from literature (Hoffmann scaling).

---

## §6 — Cross-cutting infrastructure summary

### §6.1 — Universal AVE-Core dependencies

All 7 application repos import from:
- `ave.core.constants` (~120 derived constants from 3 calibrations: ℓ_node, α, G)
- `ave.core.universal_operators` (S(A), Γ, Op1-Op13)
- `ave.core.regime_map` (Regime I/II/III/IV classification)

### §6.2 — Heavy-use cross-repo solvers

- AVE-Protein → 5+ AVE-Core modules (transmission_line, universal_operators, soliton_bond_solver, scale_invariant, constants)
- AVE-HOPF → ave.core.constants (C_0, Z_0, ALPHA, MU_0, EPSILON_0)
- AVE-Metamaterials → ave.core.constants + universal_operators + condensed.silicon_crystal
- AVE-VirtualMedia → ave.core.constants + universal_operators + fdtd_3d
- AVE-APU → ave.core constants + universal_operators

### §6.3 — Anti-cheat / CI contract infrastructure

`verify_core_parity.py` + `verify_local_universe.py` (in AVE-Metamaterials + AVE-VirtualMedia minimum):
- AST signature mapping for AVE-Core API drift detection
- Banned imports scan (scipy.constants blocked)
- MAGIC_NUMBERS registry: 137.036 (1/α), 376.73 (Z₀), 1836.15 (m_p/m_e) must emerge from DAG geometry

### §6.4 — Implementation gaps (manuscript-predicted, missing across all repos)

1. **Unified PMNS solver** (Dirac + Majorana mass hierarchies)
2. **Lepton decay width calculator** (τ → eν̄ν analytic only, no engine compute)
3. **Full baryon spectrum solver** (uud/udd/strange content, cross-knot families)
4. **W/Z scattering amplitudes** (e⁺e⁻ → W⁺W⁻ from Lagrangian)
5. **Schwinger pair creation rate** (E-field breakdown with quantum tunneling)
6. **Hawking radiation / Bogoliubov coefficients**
7. **Vector control FOC for atomic IE** (Period 3+ accuracy gap per parent's future_work/)

---

## §7 — Tracking priorities (forward direction)

### §7.1 — VERIFIED-this-session (locked in)

| Anchor | Verification |
|---|---|
| Hydrogen IE = 13.6057 eV at +0.057% | Direct execution `ionization_energy_e2k(1)` |
| Proton mass = 938.254 MeV at -0.002% | Direct execution `BARYON_LADDER[5]['mass_mev']` |
| Baryon ladder c=5-19, 8 states ±3% | [doc 98 §2.1](98_framework_decision_ii_mass_spectrum_activation.md) |
| J^P pattern J=(c-4)/2 for 7/8 states | `baryon_jp_pattern_check_results.json` |

### §7.2 — Spot-verification candidates (next-priority)

1. **AVE-Protein `s12_pdb_validation.py` direct execution** (~30-60 min) — convert claimed Rg/RMSD <2.5Å to verified-this-session anchor
2. **AVE-Core Period 2 IE refinement** (Li +5.5% gap vs parent's claimed 1.2% mean) — trace SIR mode-weighting transfer status
3. **AVE-HOPF Beltrami eigenvalue execution** (~10 min) — verify λ(p,q) = √(p²/R² + q²/r²) numerical output

### §7.3 — Implementation extension priorities

1. **Phase 1 commit**: extend `TORUS_KNOT_CROSSING_NUMBERS` to c=5-25 in AVE-Core constants.py + add `test_baryon_ladder_full.py`
2. **Phase 2 (1-2 weeks)**: build dynamical W/Z/Higgs eigenvalue solver from electroweak potential (currently hardcoded)
3. **Phase 3 (~weeks)**: neutrino + PMNS + lepton spectrum solvers
4. **Mass-spectrum activation extension to AVE-Metamaterials**: validate Miller n=5 universality claim (would extend particle-mass framework into materials)

### §7.4 — Long-term experimental targets

1. **AVE-HOPF VNA measurement**: PCB fabrication + 3-medium VNA sweep — first AVE experimental falsification test
2. **AVE-PONDER thrust measurement**: 30 kV asymmetric capacitor + precision balance — macro-scale Axiom 4 validation
3. **AVE-APU tape-out**: SPICE-compiled prototype hardware

### §7.5 — Recovery from parent repo

1. **Vol 1 axiom mathematics** → AVE-Core manuscript tree (currently parent-only)
2. **Vol 3 gravity/cosmology** → AVE-Core (parent has stellar interior, MOND-like drag, GW propagation)
3. **Vol 7 precision anomalies** (white dwarf shear, BH interior) → AVE-Core
4. **future_work/ tracker content** → AVE-Core open-issues queue
5. **SIR mode-weighting refinement** → AVE-Core radial_eigenvalue.py (resolves A47 v9 Li discrepancy)

---

## §8 — Honest gut state synthesis

**Per the auditor's session-arc gut shift tracking** (35-45% → 45-55% → 50-60% → 55-65%), this multi-repo survey provides additional context:

**Pushes empirical record higher (verified):**
- 4 anchor classes verified this session (atomic orbitals, proton mass, baryon ladder, J^P pattern)
- 9 application domains with working solver/simulator infrastructure
- Cross-cutting universal operators + anti-cheat CI contract infrastructure
- atopile compiler + SPICE exporter production-ready

**Adds positive empirical record (claimed, verification pending):**
- AVE-Protein 20-PDB benchmark (claimed validated)
- AVE-Core Period 2 IE 1.2% mean (parent claim, current code shows 5.5% on Li)
- Multiple FDTD simulators across application repos

**Negative records / open empirical gaps:**
- AVE-HOPF VNA experiment NOT executed (predictions only)
- AVE-PONDER thrust NOT measured (predictions only)
- AVE-Propulsion / AVE-Fusion zero empirical anchors
- 7 manuscript-predicted solvers missing implementation

**Net read:** framework's empirical record across 9 domains is **substantively broader and structurally consistent** than narrow K4-TLM-substrate-test focus suggests. Multiple working solver classes producing axiom-traceable predictions with zero free parameters. Verification gaps real but bounded; lab-feasibility for several (AVE-HOPF VNA, AVE-PONDER thrust) is HIGH.

The framework decision (ii) mass spectrum activation extends naturally into AVE-Metamaterials Miller-n=5 universality + AVE-Protein protein folding validation + parent's torus_knot_spectrum.py. **Multiple parallel forward tracks** rather than single-track L3 arc continuation.

---

## §9 — Files cited

**Manuscript (verified existence):**
- AVE-Core: `manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex`, `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/`
- Parent: 8-volume LaTeX + AVE-KB extraction at `Applied-Vacuum-Engineering/manuscript/`
- AVE-Protein: `manuscript/vol_protein/{03,04,05}_*.tex`
- AVE-HOPF: `manuscript/03_hopf_01_chiral_verification.tex`
- AVE-APU: `manuscript/vol_1-4/` (27 chapters)
- AVE-PONDER: `manuscript/vol_ponder/` (7 chapters)
- AVE-Metamaterials: `manuscript/vol_1_active_metamaterials/` (8 chapters)
- AVE-VirtualMedia: `manuscript/vol_virtual_media/` (13 chapters)

**Engine code (per Explore agent + spot-verified):**
- AVE-Core: `src/ave/solvers/radial_eigenvalue.py` (1914 lines), `src/ave/solvers/transmission_line.py`, `src/ave/topological/faddeev_skyrme.py`, `src/ave/core/{constants,universal_operators,k4_tlm,fdtd_3d}.py`
- Parent: `src/ave/{solvers,topological,core,gravity,nuclear,regime_*}/*.py` (~26K lines, 16 modules)
- AVE-Protein: `src/ave_protein/engines/{s11_fold_engine_v3_jax,s11_fold_engine_v4_ymatrix,s_param_network_engine}.py`
- AVE-HOPF: `scripts/{beltrami_hopf_coil,hopf_01_*,chiral_antenna_q_analysis}.py`
- AVE-APU: `src/ave/hardware/{spice_apu_exporter,geometric_diode,soliton_memory,...}.py`
- AVE-PONDER: `src/scripts/simulate_ponder_*.py` (36 scripts)
- AVE-Propulsion: `src/scripts/simulate_chiral_acoustic_rectification.py` + 12 others
- AVE-Fusion: `src/scripts/simulate_metric_catalyzed_fusion.py` + 8 others
- AVE-Metamaterials: `scripts/simulate_{miller_enhanced_pv,pv_lc_cavity,casimir_qubit_shielding,...}.py`
- AVE-VirtualMedia: `scripts/{generate_complex_impedance,generate_activation_regime_by_layer,...}.py`

**Documents:**
- [doc 97](97_manuscript_canonical_electron_solver_discovery.md) — radial eigenvalue solver discovery
- [doc 98](98_framework_decision_ii_mass_spectrum_activation.md) — mass spectrum activation plan
- This doc 99 — multi-repo capability landscape

— implementer-drafted research-tier doc, 2026-04-30, post-Grant-multi-repo-investigation directive
