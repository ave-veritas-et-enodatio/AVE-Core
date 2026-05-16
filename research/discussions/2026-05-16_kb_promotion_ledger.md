# AVE-Core KB Promotion Ledger — 2026-05-16

**Source:** ave-auditor agent (background id `a2b26102957e2a96c`), 2026-05-16. Per Grant directive: "i want all derivations in core kb."

**Lane note:** Auditor recommendations; implementer execution drives the actual landings.

## Summary counts

- **PROMOTE-T1**: 14 (load-bearing core derivations missing from KB)
- **PROMOTE-T2**: 18 (solid AVE-Core-scoped derivations, lower priority)
- **AC** (already canonical): 11
- **SUPERSEDED**: 4
- **FALSIFIED**: 2
- **EXPLORE**: 6
- **SUBORDINATED**: 9

## Execution status (live ledger)

### PROMOTE-T1 (14 total; 13 DONE as of 2026-05-16, 1 deferred)

| Doc | Topic | Status | Landed KB path |
|---|---|---|---|
| L5 A-034 | Universal saturation-kernel 19-instance cross-scale catalog | **DONE** | `common/universal-saturation-kernel-catalog.md` (commit 849b2d2) |
| doc 113 | v14 Mode I PASS — breathing soliton on Master Equation FDTD | **DONE** | `vol1/dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md` (commit 5487ede) |
| doc 41 §2-§3 (F1) | Cosserat mass-gap `m² = 4·G_c/I_ω` (0.35% confirmed) | **DONE** | `vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md` (commit 849b2d2) |
| doc 103 | Substrate-perspective view of canonical electron | **DONE** | `vol2/particle-physics/ch01-topological-matter/substrate-perspective-electron.md` (commit 849b2d2) |
| doc 45 | Lattice impedance decomposition (Z_0/Z_cell/Z_eff/Z_local) | **DONE** | `vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md` (commit 849b2d2) |
| A-010 + docs 16/17 | Op14 local clock modulation `ω_local(r) = ω_global·√(1−A²(r))` | **DONE** | `vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md` (this commit) |
| docs 53, 54 | Pair production = saturated flux-tube rupture (4-axiom derivation) | **DONE** | `vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md` (commit 849b2d2) |
| docs 16, 17, 24, 27 | Theorem 3.1 v2 — α⁻¹ as phase-space Q-factor of electron LC tank at TIR boundary | **DONE** | `vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` (commit 849b2d2) |
| A-032 + doc 22 | \|T\|=12 universality across K4 4×3 mode spaces (four-route convergence) | **SUFFICIENT** | existing `vol1/axioms-and-lattice/ch1-fundamental-axioms/tetrahedral-t-universality.md` already comprehensive (all 4 routes + Q-G47 cross-ref); auditor's PARTIAL flag was Session 19+ rigorous $\xi_{K1}, \xi_{K2}$ derivation pending — research-tier, not KB-tier gap |
| docs 30, 107 | Photon = T₂-only Cosserat ω microrotation (single-sector canonical) | **DONE** | `vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md` (commit 849b2d2) |
| doc 106 | Photon propagation v_meas/c = √2 cardinal-axis baseline empirical | **DONE** | `vol1/dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md` (commit 849b2d2) |
| doc 109 §13-§15 | Boundary-envelope reformulation (substrate observes boundary, not interior) | **DONE** | augmented `common/boundary-observables-m-q-j.md` §"Implications" (commit 5487ede) |
| doc 79 §6.7 + doc 54 §6 + A-015 | Meissner-asymmetric magnetic-moment generator (κ_chiral = 1.2·α) | **DONE** | covered in `vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md` §6 (commit 5487ede) |
| docs 49, 80, 85 | Dark wake + back-EMF + FOC d-q axiom-grounded derivation | **DEFER** | cross-repo synthesis (AVE-PONDER + AVE-Propulsion + AVE-Fusion); awaiting Grant adjudication on sibling-repo scope (Q2 below) |

### PROMOTE-T2 (18 total; 0 done)

| Doc | Topic | KB target |
|---|---|---|
| doc 47 §2 | Thermal lattice noise σ_V/σ_ω equipartition + T_V-rupt | `vol1/dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md` |
| doc 47 §2.2 + E-042 | T_V-rupt = 3.44 MK vacuum-rupture temperature | `vol4/circuit-theory/ch1-vacuum-circuit-analysis/vacuum-rupture-temperature.md` |
| doc 59 §1 + E-029 | τ_relax = ℓ_node/c per-cell K4 Lagrangian | `vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md` |
| doc 64 §1 + E-025 | Area theorem δA ≥ 0 axiom-first | `vol3/cosmology/ch15-black-hole-orbitals/area-theorem-axiom-derivation.md` |
| doc 64 + E-023 | r_sat = 7GM/c² = 3.5·r_s BH horizon prediction | `vol3/cosmology/ch15-black-hole-orbitals/seven-gm-horizon-prediction.md` |
| doc 62 §10 + E-022 | Four-entropy distinction at BH horizon | `vol3/condensed-matter/ch11-thermodynamics/four-entropy-distinction.md` |
| doc 65 §6-§9 | Discrete-lattice Ŝ_horizon ≈ 8.7·k_B universal constant | `vol3/condensed-matter/ch11-thermodynamics/discrete-lattice-entropy-constant.md` |
| doc 100 §25 + docs 101+102 (A-024) | Bracket-Golden-Torus reframe canonical operationalization | `vol2/particle-physics/ch01-topological-matter/electron-unknot-cosserat-seeder.md` |
| doc 78 + A-014 | L3 branch closure: 10-test Mode III canonical (negative empirical) | partly in `l3-electron-soliton-synthesis.md` §8 |
| doc 79 §3.5 + A-017 | Rest energy m_e c² is structural Virial-sum at bond-pair LC tank | partly in `l3-electron-soliton-synthesis.md` §3 |
| doc 75 §6 + A-012 | Op14 cross-sector trading (ρ = -0.990) | `vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md` |
| doc 22 §1-§5 | K4 rotation group T = A_4, \|T\|=12 with irrep decomposition | `vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md` |
| doc 30 §1 | K4 4-port = A_1 ⊕ T_2 irrep decomposition + S-matrix eigenvalues | `vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md` |
| doc 25 §15-§20 | (2,3) torus knot uniqueness from knot theory | `vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md` |
| doc 03 §6 | α⁻¹ = 4π³ + π² + π via Λ_vol/Λ_surf/Λ_line at R·r = 1/4 | extension of `vol1/ch8-alpha-golden-torus.md` |
| doc 110 + E-098 | Cubic K4 anisotropy at saturation collapse | `vol1/axioms-and-lattice/ch1-fundamental-axioms/cubic-k4-empirical-anisotropy.md` |
| doc 114 §1 | A-034 measurement hierarchy: single/bulk/phased-array PLL SNR | `vol4/falsification/ch11-experimental-bench/measurement-hierarchy-snr.md` |
| Entries 001 + 002 (discussions) | Ω_freeze cascade through nested rotators + orbital-plane alignment | `vol3/cosmology/ch04-generative-cosmology/omega-freeze-nested-rotators.md` (Grant adjudication first) |

### AC (already canonical, grep-confirmed)

| Item | KB location |
|---|---|
| A-024 electron-is-unknot | `vol1/ch8-alpha-golden-torus.md` |
| A-026 + A-028 M/Q/J substrate-observability | `common/boundary-observables-m-q-j.md` |
| A-027 two-engine architecture | `common/two-engine-architecture-a027.md` |
| A-029 secondary scale r_sec/d ≈ 1.187 | `vol1/axioms-and-lattice/ch2-macroscopic-moduli/secondary-scale-shared-b-node.md` |
| A-030 + A-031 refined | `common/cosmic-parameter-horizon-a031-refinement.md` |
| A-032 (partial) | `common/q-g47-substrate-scale-cosserat-closure.md` |
| A-033 (partial) | `vol1/axioms-and-lattice/ch1-fundamental-axioms/tetrahedral-t-universality.md` |
| Trampoline framework | `common/trampoline-framework.md` |
| Cosmological constant 10^122 closure | `vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md` (commit 8495c4b) |
| BCS B_c(T) universal saturation duality | `vol3/condensed-matter/ch09-condensed-matter-superconductivity/universal-saturation-operator.md` |
| Solar flares LED avalanche | `vol3/cosmology/ch14-orbital-mechanics/solar-flares-led-avalanche.md` |

### Open questions for Grant

1. **A-034 catalog leaf scoping** — `common/` (cross-volume) OR `vol1/axioms-and-lattice/` (Axiom 4 extension) OR `vol3/cosmology/ch04-generative-cosmology/` (cosmology home per A-031)? Recommend `common/`.
2. **Sibling-repo derivation scope** — AVE-PONDER/Propulsion/Fusion/Metamaterials have AVE-Core-relevant chunks. Conservative reading: each sibling repo retains its own; AVE-Core gets a `common/cross-repo-derivation-index.md` pointing to canonical sibling-repo files.
3. **A-018/A-019/A-022 methodology infrastructure** (PR template, SHA-anchoring manifest, CI gates) — workflow discipline, not substrate-physics derivations. Excluded from PROMOTE.
4. **Discussions entries 001 + 002** (Ω_freeze nested rotators + orbital-plane alignment) — flagged `open` pending Grant escalation adjudication.
