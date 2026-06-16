# Grid-definition cartography — axiom -> continuum -> lattice -> engine -> observable

**Status: DRAFT / DIAGNOSTIC — navigational map, not a ruling.**

This document maps every AVE vacuum-grid definition framing (axioms, calibration
inputs, micropolar / phase / real / chiral / crystal / amorphous framings) to
its actual simulation implementation, file:line grounded. It is a navigational
map of how each grid-definition framing lands on the implementation stack — it
does **not** resolve any seam. Where a framing or a pair of framings collides,
the collision is documented as an `unadjudicated-seam` and flagged OPEN, with a
pointer at where it gets ruled. It picks no side. These artifacts are diagnostic
/ decision-staging only and MUST NOT be cited as adjudicating any open question.

This is a research-tier (ungated) doc, like
`research/2026-06-10_field-symbol-registry.md` — not a gated KB leaf.

**Provenance:** built from the `wfj1kwh22` grounded-8-reader + adversarial
citation-check workflow (8/8 ground readers returned; 27 framings + 8 seams
citation-checked). Of the framings carried, 8 were downgraded to seams by a
`supported=false` verdict and 3 were status-corrected upward; of the 8 seams,
7 verified and 1 disputed. All file:line citations below are carried from that
workflow's verified findings; a sample (`eq_axiom_1.tex:23-24`,
`01_fundamental_axioms.tex:53,:220`, `depends-on.jsonl:289`, `k4_tlm.py:97`)
was re-opened verbatim when producing this doc.

**Status vocabulary** (the spec's own tags): `grounded-canon` (leaf + code both
opened by a reader and match), `engineering-choice` (tractability / discipline
decision the corpus rationalizes), `unadjudicated-seam` (the corpus itself flags
OPEN or carries both sides verbatim with no reconciling marker).

---

## 1. The layer stack (L0 -> L4 + SR-calib rail)

The grid is read as a six-element stack: a five-layer vertical (L0 physical-axiom
-> L1 continuum-field -> L2 discretized-lattice -> L3 engine-code -> L4
observable-coords) plus a calibration-input side rail (SR-calib) that feeds every
layer from `constants.py`.

- **L0 — Physical-axiom (what the vacuum IS).** Axiom 1's identity statement: the
  vacuum IS a chiral Laves K4 Cosserat crystal M_A, micropolar nodes (6 DOF: 3
  translational -> E, 3 microrotational -> B), right-handed I4_1 32 chiral space
  group, z=4 diamond connectivity in the production engine. Single source of truth
  at `eq_axiom_1.tex:23-24`. Declares the two orthogonal "3"s (A1 dilatation-mass
  scalar vs Cosserat (2,3) micro-rotation winding=charge). Also hosts the
  crystal-vs-amorphous seam: the same chapter says "crystallised substrate"
  (`01_fundamental_axioms.tex:53`) and "amorphous disordered network"
  (`01_fundamental_axioms.tex:220`).

- **L1 — Continuum-field (Cosserat/micropolar + Trace-Reversed Chiral LC
  Network).** The macroscopic continuum limit of Axiom 1: a Cosserat micropolar
  field with independent translation u and SO(3) micro-rotation omega,
  L = 1/2 rho|u_dot|^2 + 1/2 I_omega|omega_dot|^2 - W(u,omega). Hosts the mass-gap
  m^2 = 4 G_c / I_omega, the K=2G magic-angle moduli lock (nu_vac=2/7), the
  FTG-EMT amorphous secondary network (z0~51.25), and the Cosserat coupling-length
  sqrt(6)*ell_node. The corpus's own "continuous-springs reframing" (Grant
  2026-05-15) declares this the PHYSICS layer and the discrete lattice merely its
  discretization / sampling.

- **L2 — Discretized-lattice (K4-TLM bond-LC realization).** The discrete
  real-space lattice the production engine computes on: bipartite-FCC z=4 DIAMOND
  lattice of 4-port LC junctions, scatter matrix S = 1/2*1 - I, scatter-then-connect
  propagation. One node holds per-port V_inc/V_ref (4-vector) + per-bond Phi_link;
  one bond is a directed A->B (+/-1,+/-1,+/-1) tetrahedral hop. The sqrt(2)
  cardinal-axis speed is a port-step-vs-Euclidean lattice-projection artifact
  (dt = dx/(c*sqrt2)). The INSTRUMENT path (z=3 srs/Laves) lives here too as a
  separate builder. The central K4-name seam lives here.

- **L3 — Engine-code (the simulation classes).** The actual Python solver classes
  under `src/ave`: K4Lattice3D (TLM scatter/connect), MasterEquationFDTD (scalar V
  leapfrog, calibration-FREE native units), CosseratField3D (full SO(3) vector
  micropolar continuum solver), CoupledK4Cosserat / VacuumEngine3D (hybrid
  K4-phasor + Cosserat real-space), the crystal_engine / crystal_graft_v2-v4 /
  unified_genesis / annihilation lineage, plus FDTD3DEngine and the analytic
  rupture/gravity solvers. The chirality realization splits here: dynamical
  kappa_chiral scalar (achiral diamond) vs geometric I4_1 32 srs builder.

- **L4 — Observable-coords (phase-space readout vs real-space evolution).** The
  coordinate frame in which observables are read. `observable_battery.py` Coord
  enum {REAL, PHASE, SCALAR, REAL_VS_PHASE} is the implementation-level
  enforcement. Hosts the real-vs-phase disambiguation: the electron is the 0_1
  unknot in REAL space carrying a (2,3) Clifford-torus winding in PHASE space
  (V_inc, V_ref). The EVOLVE-vs-READOUT boundary: `k4_tlm.py` evolves the phasor
  as state; `master_fdtd_phasor_bridge.py` projects it read-only post-step from a
  real-space scalar. The (2,3) glyph collides across frames; Gamma/Smith-chart,
  I/Q quadrature, Lissajous all live here.

- **SR-calib — Calibration-inputs (side rail).** The side rail feeding all layers
  from `constants.py`. {m_e, alpha, G} per the historical label; {ell_node, alpha,
  G} per the standard framing; "one scale + Omega_freeze + 4 axioms" per the
  current structural-closure framing — three coexisting count-framings in one file.
  alpha appears in BOTH real-space (sqrt(alpha) seed amplitude / R_I cutoff) AND
  phase-space (1/Q_TANK). m_e <-> ell_node 1:1 scale. G is MIXED (form-derived /7
  PPN + value-fitted xi). z0=51.25, R*r=1/4, kappa_chiral=alpha*kappa_tilde,
  Q_TANK=1/alpha, nu_vac=2/7 all enter here as derived / echo values.

---

## 2. Framings table

Status is the post-verification status. The note column carries the condensed
`[CHECK ...]` verify-finding where the workflow downgraded, upgraded, or
qualified a framing. Citations are abbreviated; full paths live in the anchors.

| # | Framing | Primary layer | Spans | Status | Corpus anchor | Code anchor | Verify note |
|---|---------|---------------|-------|--------|---------------|-------------|-------------|
| 1 | Axiom 1 (what the vacuum IS) | L0 | L0 | unadjudicated-seam | `eq_axiom_1.tex:23-42`; `01_fundamental_axioms.tex:53`; `axiom-definitions.md:16` | `k4_tlm.py:1-19,101-119`; `cosserat_field_3d.py`; `k4_cosserat_coupling.py` | DOWNGRADED grounded-canon -> seam: corpus half grounded, but chiral I4_1 32 NOT structurally realized in production (K4Lattice3D is achiral Fd-3m diamond; chirality enters dynamically, `k4_cosserat_coupling.py:249`). "single source of truth/production engine" itself a seam: `constants.py:81-82` names two canonical engines. |
| 2 | Micropolar/Cosserat continuum (u + SO(3) omega, 6 DOF) | L1 | L0,L1,L3 | unadjudicated-seam | `cosserat-mass-gap.md:11,28-38,51`; `CLAUDE.md:55` | `cosserat_field_3d.py:766,827-828,175,189,610,617-625` | DOWNGRADED: bare 6-DOF u+omega kinematics grounded, but (a) corpus_anchor mis-pathed; (b) E/B mapping grounded in `CLAUDE.md:55` not the cited leaf; (c) leaf:11 says (2,3) winding is phase-space yet code:1021 seeds it onto real-space u; (d) clm-4mmwb6 held at 0.8 by 34% group-velocity error. "cleanest mapping" superlative is inference at the seams. |
| 3 | Cosserat mass-gap m^2 = 4 G_c / I_omega | L1 | L1 | grounded-canon | `cosserat-mass-gap.md:9,17-22,44-61,78-82` | `cosserat_field_3d.py:1808-1825,617-625`; driver `cosserat_wave_test.py` | Structural mass mechanism; validated standalone (T_theory=pi vs T_measured=3.1307, 0.35%). |
| 4 | K=2G magic-angle / nu_vac = 2/7 | L1 | L1,SR | unadjudicated-seam | `vacuum-poisson-ratio.md:10-14`; `q-g47-substrate-scale-cosserat-closure.md:20-30,49-58` | `constants.py:532,319,672-676`; `q_g47_sessions_19_xi_K_derivation.py` | DOWNGRADED engineering-choice -> seam: hard-coding MATCHES, but causal framing refuted at HEAD by `2026-06-14_magic-angle-provenance`: chain is three links of different solidity — nu_vac=2/7-from-K=2G FIRM, K=2G itself IMPORTED (matched to GR), u0*~0.187 is ECHO under active Rule-12 RETRACT per "retract magic-angle." So 2/7 follows ALGEBRAICALLY from imported K=2G, not from the magic-angle locus. |
| 5 | FTG-EMT amorphous secondary network z0 ~ 51.25 | L1 | L1,SR | unadjudicated-seam | `01_fundamental_axioms.tex:197,220`; `q-g47-...closure.md:100-112`; `topological-packing-fraction.md:16` | `constants.py:508-520,522-525`; `q_g47_path_c_emt_canonical.py` | Second amorphous coordination scale (z0~51.25 at p*=8*pi*alpha) distinct from primary z=4 diamond; alpha-circular (z0 inverted FROM alpha, doesn't independently fix it). |
| 6 | The two homonymous "3"s (A1 dilatation-mass vs Cosserat (2,3) winding=charge) | L0 | L0,L4 | grounded-canon | `master-equation.md:20` (Rule-12 ratified); `cosserat-mass-gap.md:108-110`; `resonant-lc-solitons.md:96` | `master_equation_fdtd.py:42-47`; `cosserat_field_3d.py:610,2122,451-486`; `helicity_observer.py:39-59,53-70` | Two orthogonal objects (A1 perp T2): A1 dilatation MASS (Heaviside scalar V) vs Cosserat micro-rotation (2,3) WINDING (charge=Beltrami helicity); never wire winding into the breather's phasor. |
| 7 | k_chi / I4_1 32 chiral space group vs Fd-3m supergroup (dynamical chirality) | L3 | L0,L3,SR | grounded-canon | `eq_axiom_1.tex:24,35`; `translation-circuit.md:652`; `omega-freeze-cosmic-grain-cascade.md:197,201` | `cosserat_field_3d.py:115-124,131,522-523,582-583`; `chiral_lattice_v10.py:283` | Production chirality is an EXCITED k_chi Cosserat order-parameter (kappa_chiral scalar) on the ACHIRAL Fd-3m diamond, asymmetrically loading mu-up/eps-down; NOT a literal space-group transform. |
| 8 | Geometric I4_1 32 srs instrument (structural chirality) | L2 | L2,L3 | grounded-canon | `eq_axiom_1.tex:35`; `chiral_lattice.py:2,11-13`; `2026-06-12_lattice-d1-adjudication-memo.md:44,75,105` | `chiral_lattice.py:44-75,199-217,227-269`; `chiral_lattice_v17.py:288` | UPGRADED seam -> grounded-canon. z=3 srs/Laves/Sunada-K4 Wyckoff-8a motif (right=I4_1 32, left-mirror=I4_3 32, achiral Fd-3m diamond CONTROL); validated structural-chirality INSTRUMENT, NOT the engine substrate. |
| 9 | Spin-1/2 from K4 -> A_4 -> 2T -> SU(2) chain | L0 | L0,SR | unadjudicated-seam | `k4-rotation-group.md:9-11,116-136`; `finkelstein-misner-spin-half-derivation.md` | code footprint `constants.py:181,713` (r_phase=2 phase-cycle factor); `cosserat_field_3d.py:134-158` (TETRA_OFFSETS) | DOWNGRADED inference -> seam: corpus chain grounded, but "not exercised by any running solver / grep-empty" REFUTED: `chiral_orbital_holonomy.py` (749 lines, Wahba/Kabsch + SO(3)->SU(2) lift) IS a running solver with a logged result (CONSISTENCY-class, 0/400 achiral vs 127/400 chiral, dot(q(2pi),q(0))=-1.0); SU(2) double-cover also at `cosserat_field_3d.py:1088,1155`, `boundary_invariants.py:11,81,208`, `axioms/yang_mills.py:188-235`. Seam between corpus open-work flag and logged solver result. |
| 10 | K4-TLM bond LC tank (V_inc <-> Phi_link conjugate pair) | L2 | L2 | engineering-choice | `kirchhoff-network-method.md:14-43`; `lc-electrodynamics.md:8-52`; `lc-condensate-vacuum.md:8` | `k4_tlm.py:192-206,385-400`; `Z_0` at `constants.py:98` NOT imported | DOWNGRADED grounded-canon -> engineering-choice: code grounded, but corpus anchors FAIL — `kirchhoff-network-method.md` describes a DIFFERENT pair (V_i, I_ij) in a different solver; `lc-electrodynamics.md` is the rho_bulk/shear derivation; `lc-condensate-vacuum.md:8` is a section heading. Phase-space TLM scattering pair framed by lines that define a real-space Kirchhoff state pair — engineering/tractability choice asserted-as-canon via wrong anchors. |
| 11 | K4-TLM scattering (4 ports, S = 1/2*1 - I, scatter-then-connect) | L2 | L2,L3 | grounded-canon | `k4-port-irrep-decomposition.md:9-11,57-61,19-29` | `k4_tlm.py:64-93,298-353,355-459,461-465` | 4-port scattering; S=1/2*1-I (eigenvalues +1,-1,-1,-1, A_1 + T_2 irreps), byte-identical corpus<->code; scatter (V_ref=S*V_inc) then connect (np.roll port hop). |
| 12 | K4Lattice3D data structure + diamond/bipartite embedding | L2 | L2,L3 | engineering-choice | `eq_axiom_1.tex` (chiral Laves K4 / I4_1 32); continuous-springs reframing `k4_tlm.py:35-39` | `k4_tlm.py:101-118,191-217,215-217` | z=4 bipartite-FCC DIAMOND lattice (mask_A=all-even, mask_B=all-odd); node holds 4-port phasors + Phi_link + z_local + S_field; bond=directed A->B tetrahedral hop. |
| 13 | sqrt(2) cardinal speed (port-step-vs-Euclidean lattice-projection artifact) | L2 | L2,L1 | grounded-canon | `photon-propagation-baseline.md:9-11,45-50,38-41`; `cubic-k4-empirical-anisotropy.md:71-80` | `k4_tlm.py:181-189,378-383`; `k4_cosserat_coupling.py:301-302` | Cardinal-axis v=c*sqrt(2) is a port-step-vs-Euclidean projection artifact (body-diagonal sqrt(3)*dx hop in dt=dx/(c*sqrt2)); corpus ALSO ties same sqrt(2) to continuum v_A1/v_T2=sqrt(K/G) at K=2G. |
| 14 | MasterEquationFDTD (scalar V leapfrog, calibration-free native) | L3 | L3,L4 | grounded-canon | `master-equation.md:75-78`; `resonant-lc-solitons.md:10`; `electron-unknot-cosserat-seeder.md:89-97` | `master_equation_fdtd.py:42-100,150-250,91-94`; NO ALPHA/M_E/L_NODE/G import | Scalar 3D FDTD (c_eff^2=c0^2/S(A)); evolves a REAL-space scalar V; ingests NO calibration input (native, CFL timestep); canonical autonomous-electron host (Mode I). |
| 15 | CosseratField3D (standalone SO(3) vector micropolar solver) | L1 | L1,L3 | unadjudicated-seam | `cosserat-mass-gap.md` (Lagrangian); `electron-unknot-cosserat-seeder.md:11,17-23,47` | `cosserat_field_3d.py:766,827-828,1065-1164,921-1012` | DOWNGRADED: solver-structure half grounded (independent u/omega; JAX-grad velocity-Verlet; unknot seeder MATCH), but "(2,3) sector" clause cited to :921-1012 is a real-space/phase-space seam BOTH corpus and code's own docstring refute — leaf:11 + seeder:20,43 say (2,3) is PHASE-space Clifford-torus winding; `initialize_electron_2_3_sector:932-945` carries a DEPRECATION NOTE calling its real-space (2,3) write "misleading", valid for proton 5_1/5_2 NOT canonical electron; :1093-1095 confirms canonical (2,3) "lives in K4 V-tank, NOT in scope of Cosserat sector." |
| 16 | CoupledK4Cosserat / VacuumEngine3D (hybrid coordinate engine) | L3 | L3,L4 | unadjudicated-seam | `q-g47-...closure.md:74-87`; "A-027 two-engine architecture"; `CLAUDE.md:60` | `k4_cosserat_coupling.py:400-500,550-750`; `vacuum_engine.py:1540-1650,1700-1900`; `cross_sector_coupling.py:39-134` | DOWNGRADED engineering-choice -> seam: code verifies S1-D form + wrapper, but ALL THREE corpus anchors mis-cited (q-g47:74-87 is the magic-angle table, CLAUDE.md:60 is a loop-gap skill bullet, A-027's two engines are K4-TLM + Master Equation FDTD NOT this hybrid). Two code seams: "production hybrid" overstates (cited symmetric S1-D form tagged "Legacy ... Retained"; EngineConfig defaults ship use_asymmetric_saturation=True; V->omega W_refl gradient "NOT used (A28 double-counting/runaway)"); `cross_sector_coupling.py:39-134` is the gyrotropic+trilinear converter, opt-in default off. |
| 17 | Crystal-engine lineage (crystal_engine -> graft_v2/v3/v4 -> unified_genesis -> annihilation) | L3 | L3 | grounded-canon | `2026-06-09_crystal-engine-elastodynamic-graft_design-prereg.md`; `2026-06-10_crystal-graft-v4_physics-changes_adjudication.md`; `2026-06-10_genesis-v5-seeded-snap_prereg.md` | `crystal_engine.py:7,51`; `crystal_graft_v4.py:74-150,200-350`; `unified_genesis_engine.py:67-150`; `annihilation_engine.py:48-120` | Real-space elastodynamic-graft family: two operating branches (bulk V=electron, shear w=photon) at nu_vac=2/7 (+ optional third Cosserat omega branch; class docstring at `crystal_engine.py:7` self-describes as "three-branch chiral micropolar (I4_1 32)"); v4 adds chi-from-photon + Woltjer/Taylor helicity-lock; genesis adds rarefaction bulk sector; byte-identical inheritance discipline. |
| 18 | LoopGapHarness (rank-parameterized unified harness, v18+) | L3 | L3 | grounded-canon | `_orchestration/2026-06-12_loop-gap-engine-dag.md`; `_orchestration/2026-06-12_loop-gap-unified-harness.md` | `loop_gap_harness.py:1-60,60-99,100-200` | Rank-parameterized (1=container..4=remanence) unified harness on VacuumEngine3D replacing per-version genesis silos; srs v9..17 FROZEN as falsifiers; advance via rank not version number. |
| 19 | FDTD3DEngine + analytic rupture/gravity/specialized solvers | L3 | L3 | grounded-canon | `fdtd_3d.py:1-46`; `rupture_solver.py:1-56`; `gw_propagation.py:1-56` | `fdtd_3d.py:28-120,150-350`; `rupture_solver.py:60-150`; `gw_propagation.py:40-130`; `lbm_3d.py:1-150` | Yee-cell Maxwell with dual Axiom-4 saturation (eps_eff AND mu_eff), plus analytic non-time-stepping solvers: RuptureSolver (Regime IV), gw_propagation (symmetric Z-invariant), CausticSolver, LBM3D (non-AVE-native kinetic). |
| 20 | Real-space vs phase-space coordinate frames (0_1 unknot vs (2,3) Clifford-torus) | L4 | L4 | unadjudicated-seam | `electron-identification.md:23,77`; `ch8-alpha-golden-torus.md:29`; `vocabulary-register.md:113-123,194-205` | `observable_battery.py:138-146,159`; `r10_2_3_winding_extractor_coordinate.py:16-63` | DOWNGRADED: prose half grounded, but STATUS over-reads and code seam contradicts the phase-space half — both cited def-nodes (def-69f472, def-3638f2) are status:ambiguous (A46 size-leak), AND `observable_battery.py:159` tags winding_2_3 as coord=REAL (OPPOSITE of "trefoil lives in phase space"); extractor reads a MIXED frame (base "2" real-space, fibre "3" phase). Citation drift: "leaky-cavity theory.md:12" is actually :16; "trefoil lives in phase space" is at `vocabulary-register.md:117` not `electron-identification.md:23`. |
| 21 | EVOLVE-vs-READOUT boundary (k4_tlm phasor-as-state vs phasor-bridge read-only projection) | L3 | L3,L4 | grounded-canon | `cvr-phasor-reactance.md:16`; `dual-reactance-storage-taxonomy.md:29-30,35-37`; `master-equation.md:30-36` | `k4_tlm.py:340,459,192-193`; `master_fdtd_phasor_bridge.py:10-12,42,72,87-90` | Same V_inc/V_ref glyph, two ontologies: EVOLVED dynamical DOF in `k4_tlm.py` vs READ-ONLY post-step projection of a real-space scalar V in `master_fdtd_phasor_bridge.py` (Z0=1 TLM split, does not alter dynamics). |
| 22 | Gamma reflection coefficient / Smith chart (\|Gamma\|^2 = 1-alpha) | L4 | L4,SR | grounded-canon | `cvr-reflection-smith.md:8,24-36`; `dual-reactance-storage-taxonomy.md:30` | `master_fdtd_phasor_bridge.py:138,154-190`; `cvr_model.py:72`; `observable_battery.py:154` | Phase-space impedance-plane headline observable: Gamma=(z_b-z_a)/(z_b+z_a), \|Gamma\|^2=1-alpha (wall falls short of unit circle by per-cycle radiative leak alpha). |
| 23 | Golden-Torus R/r phase-space aspect coordinates (R*r=1/4) | L4 | L4,SR | grounded-canon | `ch8-alpha-golden-torus.md:113-118,29`; `electron-identification.md:23`; `constants.py:191-207` (HONEST SCOPE: echo at value) | `constants.py:217-220,222`; `r9_canonical_phase_space_phasor.py` | UPGRADED seam -> grounded-canon. (R=phi/2, r=(phi-1)/2, R*r=1/4) are PHASE-SPACE Clifford-torus aspect coordinates (NOT real-space torus dimensions); coordinate-frame status grounded, AND value-is-echo is a grounded-canon HONEST-SCOPE corpus annotation (scale forced, value is a calibration identity). |
| 24 | alpha into real-space lattice (sqrt(alpha) seed amplitude / R_I cutoff) | SR | SR,L3 | grounded-canon | `constants.py:421,427,447-449,400` | `chiral_lattice_v10.py:77`; `genesis_v18_coupled.py:236`; `loop_gap_harness.py:588-590`; `master_equation_fdtd.py:70-94` (NO alpha — calibration-free) | alpha parameterizes real-space runs as a sqrt(alpha)-scaled SEED AMPLITUDE and regime cutoff (R_I=sqrt(2*alpha)), NOT as a Q-factor or lattice stiffness; same number, different coordinate system than 1/Q_TANK. |
| 25 | Q_TANK = 1/alpha (electron-instance Q, NOT universal default) | SR | SR,L4 | grounded-canon | `resonant-lc-solitons.md:83-85`; `theorem-3-1-q-factor.md:15` | `cvr_model.py:64-72` (Q_TANK=1/ALPHA, "MUST NOT default as universal"); poles()/H_scalar()/H_chiral() use keyword-only required Q | UPGRADED seam -> grounded-canon. Electron's instance Q (1/alpha~137.036) is a calibration identity, deliberately INSTANCE-scoped in a script (NOT baked into any engine as universal); FORM functions hardened to require explicit per-instance Q. (memory's :58 now :72; :58 now holds OMEGA_C.) |
| 26 | m_e calibration input (scale handle on ell_node) | SR | SR | unadjudicated-seam | `constants.py:53-62,128-131,256-257` | `constants.py:129,257,361,374`; `galactic_mond_drag.py:14-22` | m_e <-> ell_node 1:1 invertible (ell_node=hbar/(m_e*c)); sets master length NUMBER + native<->SI conversion, NOT a lattice stiffness in any running sim; called both "Input 1" (:128) and "NOT an independent input" (:53) in one file. |
| 27 | G calibration input (MIXED: form-derived /7 PPN + value-fitted xi) | SR | SR,L3 | unadjudicated-seam | `constants.py:155-156,529,532,541-556`; MEMORY: G=MIXED, xi=8.15e43 clean label | `constants.py:556` (XI_MACHIAN=hbar*c/(7*G*m_e^2)); `gravity/__init__.py:38,188,228` (7G/c^2, 4G/c^2 PPN); `gw_propagation.py:55` | G is MIXED: the /7 PPN coupling FORM is derived (1/7, 2/7 projections), but the VALUE enters as CODATA G with xi_Machian inverted OUT (comment "Class E circularity intentional"); independent G derivation OPEN. |
| 28 | Cosserat coupling-length ell_c = sqrt(6)*ell_node + G_vac shear modulus | L1 | L1,SR | grounded-canon | `constants.py:259-273,266-272,670-676` | `constants.py:273,672`; `test_vacuum_moduli_and_channels.py:39-87`; `rrad_l_counterprop_chiral.py:130` | Discrete<->continuum bridge ratio ell_c=sqrt(6)*ell_node (from xi_K2/(2*xi_K1)=6); G_vac=rho_bulk*c^2 sets a NUMBER ONLY with ZERO consumers in any real-space engine (only test asserts + a sqrt(2) P-wave ratio in 2 drivers). |
| 29 | Existing cartography matrices (field-symbol-registry, translation-circuit, divergence-test-substrate-map) | L4 | L4,L1 | unadjudicated-seam | `2026-06-10_field-symbol-registry.md:1-4,23-35` (DRAFT); `translation-circuit.md:17-24,95-146`; `divergence-test-substrate-map.md:25-29` | field-symbol-registry cites `master_fdtd_phasor_bridge.py:16-19`, `cavitation_flow.py:64`, `unified_genesis_engine.py`; divergence-map cites `s11_fold_engine_v3_jax.py`, `ligo_ringdown_driver.py` | NO existing matrix carries the full axiom->continuum->lattice->engine->observable vertical: field-symbol-registry (real/phase/bridge w/ engine file:lines) is research-DRAFT/not-canon; translation-circuit is substrate->EE-analogy; divergence-test-substrate-map is prediction->test-substrate (one layer above grid internals). |
| 30 | Vocabulary debt: 6 of 7 load-bearing terms have ZERO def-nodes | L0 | L0,L4 | unadjudicated-seam | `2026-06-14_photon-ontology-vocabulary-adjudication-handoff.md:83-97`; `vocabulary-register.md:113-120,194-205` | handoff cites `k4_tlm.py:539-552,101-119`; `z0_first_principles_attempt.py:300` ("inverse-EMT in disguise, NOT first-principles") | K4, chirality, c, longitudinal, the-3, dark-wake have NO verifier-gated def-node; phase-space (def-69f472) is the only registered one and it is status=ambiguous (conflated with a SIZE — the A46 leak). |

---

## 3. The 8 seams

Each seam carries side A, side B, the verify verdict, and a condensed
why-it-matters. All eight are flagged OPEN. The corpus self-flags several at
`the-abandoned-interior.md:183` (flag-don't-fix) and the D1 memo / photon-ontology
handoff; final adjudication is Grant + auditor lane, not this doc.

### Seam 1 — Crystal vs amorphous (the foundational substrate-ontology seam) — VERIFIED

- **Side A (crystal):** Axiom 1 says the vacuum IS a chiral Laves K4 Cosserat
  CRYSTAL with the I4_1 32 chiral space group (a space group is periodic
  crystalline order by definition). `eq_axiom_1.tex:23-24`;
  `01_fundamental_axioms.tex:53` "crystallised substrate"; `axiom-definitions.md:16`.
  Realized in every production engine as a periodic real-space lattice
  (np.roll/np.mod): K4Lattice3D, CrystalEngine, `chiral_lattice.py` LatticeNet.
- **Side B (amorphous):** the SAME Vol1 Ch1 chapter (line 220) plus the Vol3
  gravity/EMT chain calls the substrate a "3D AMORPHOUS (disordered,
  non-crystalline) network" with non-integer statistical-mean coordination
  z0~51.25; `trace-reversal-mechanism.md:10-20`;
  `topological-packing-fraction.md:16`; `cauchy-implosion-resolution.md:14`.
  Realized in code ONLY as random-point-cloud derivation drivers (np.random.uniform
  in `derive_alpha_m4_pro.py:17-25`, `simulate_rigidity_percolation.py`), NEVER as
  a production dynamical engine.
- **Why it matters:** FOUR coordination numbers coexist unreconciled (z=3 Laves name
  / z=4 diamond engine / z0=51.25 EMT / z0>=6 rigidity floor). Both sides confirmed
  verbatim including the same-chapter co-occurrence (:53 crystal vs :220 amorphous).
  The asserted crystal-micro/amorphous-meso bridge (secondary links to
  1.187*ell_node, `dielectric-snap-limit.md:32`) is ASSERTED not DERIVED — the
  corpus logs "first-principles z0 from K4 geometry currently OPEN, alpha-circular"
  (`trace-reversal-mechanism.md:22`; `closure-roadmap.md:32`). No canonical home
  leaf adjudicates this. The genuine non-crystalline Regime-IV ruptured plasma
  (`eq_axiom_1.tex:30`) is a SEPARATE notion and must not be conflated with the EMT
  "amorphous" label on the current crystallized vacuum. Two minor path corrections:
  `cauchy-implosion-resolution.md` is at vol3/gravity/CH03-macroscopic-relativity/
  (content matches).

### Seam 2 — The clm-ghs75o inversion (a claim cites Axiom 1 as saying the OPPOSITE of its own text) — VERIFIED

- **Side A:** Axiom 1 verbatim: "The physical vacuum IS a chiral Laves K4 Cosserat
  crystal M_A ... governed by the right-handed I4_1 32 chiral space group"
  (`eq_axiom_1.tex:24`). The word "amorphous" appears NOWHERE in the axiom text.
- **Side B:** `depends-on.jsonl:289` materializes clm-ghs75o -> axiom-1 with context
  "amorphous dielectric-saturation-plastic network, not a rigid periodic crystal."
  `peierls-nabarro-paradox.md:12` and `claim-quality.md:943,954` repeat it, citing
  Axiom 1 itself as authority for "not a cold rigid periodic crystal."
- **Why it matters:** VERIFIED INVERSION — all five cited file:lines opened and
  quoted verbatim. A do-not-build claim (confidence 0.30, solidity 0.30, build_band
  "do-not-build", `claims.jsonl:122`) cites the crystal axiom as authority for "not
  a rigid periodic crystal." The sharpest single-point manifestation of the
  crystal-vs-amorphous seam and the highest-priority unadjudicated item. The
  charitable Axiom-4-yield-regime reconciliation does NOT dissolve it: the
  amorphous-context edge specifically targets axiom-1 and directly negates Axiom 1's
  static crystal definition. Caveat: the "no engine implements the STZ/slipstream
  mechanism" sub-claim rests on the corpus self-caveat
  (`claim-quality.md:946,957`), not an independent src/ave grep this turn.

### Seam 3 — Phase-space vs real-space (the readout/evolution boundary; the A46 failure axis) — VERIFIED

- **Side A (phase-space):** the (V_inc,V_ref)/Clifford-torus phasor coordinate
  space; the (2,3) winding, R/r=phi^2 aspect ratio, Gamma/Smith-chart, Lissajous/I-Q.
  `electron-identification.md:23` "the trefoil lives in phase space";
  `vocabulary-register.md:113-123` (def-69f472, status ambiguous, A46 size-leak
  forbidden).
- **Side B (real-space):** the lattice-Cartesian (nx,ny,nz) evolution; the 0_1
  unknot soliton curve; the Cosserat micro-rotation omega read via Beltrami
  helicity; the (2,3) winding's BASE axis (S^2 polarization). The (2,3) glyph
  COLLIDES: phase-space Clifford-torus winding (def-3638f2) vs real-space Cosserat
  micro-rotation winding (`helicity_observer.py`) are BOTH labeled (2,3) but are
  different objects in different frames.
- **Why it matters:** SEAM CONFIRMED REAL on both axes; every cited file:line
  verbatim. THE recurring failure axis (Round 7+8 arc: 30+ commits measuring
  real-space (R,r) against a phase-space phi^2 prediction). The correct (2,3) read
  is a HYBRID: real-space shell-walk acquisition projected into (base-azimuth,
  fibre-phase) axes (`r10_2_3_winding_extractor_coordinate.py:16-63`). The
  observable_battery Coord enum + REAL_VS_PHASE channel are the implementation-level
  enforcement; `master-equation.md:20` (Rule-12) forbids wiring the winding into
  (V_inc,V_ref). Corpus already flags this as a flag-don't-fix open seam
  (`the-abandoned-interior.md:183`). Framing note: verbatim "trefoil lives in phase
  space" is at `vocabulary-register.md:117`, not `electron-identification.md:23`
  (which carries the substance, MATCH-on-substance).

### Seam 4 — Axiom-K4 vs engine-K4 (the load-bearing K4-name overload) — VERIFIED

- **Side A:** the AXIOM NAME is "chiral Laves K4" = the degree-3 srs/Sunada-K4 net
  (Sunada's K4, I4_1 32, girth-10). `chiral_lattice.py:2,11-13`. The D1 memo confirms
  srs carries a real structural-chirality channel.
- **Side B:** the ENGINE "K4" = degree-4 DIAMOND: `k4_tlm.py:97` literally titles
  itself "K4 (DIAMOND) LATTICE" and is achiral Fd-3m (bipartite FCC, mask_A
  even/mask_B odd). The production alpha/Lorentz/photon drivers all compute on this
  z=4 diamond. A THIRD referent is the rotation GROUP K4 -> A_4. The handoff (§3)
  flags: the photon engine runs the ACHIRAL diamond while Axiom 1 names the CHIRAL
  Laves.
- **Why it matters:** SEAM CONFIRMED REAL on every cited axis. One word "K4"
  overloaded across THREE referents (srs net / diamond engine / A_4 group); grep
  confirms photon/alpha/Lorentz all import the diamond K4Lattice3D, srs importers
  are exclusively genesis/instrument scripts. The D1 memo (2026-06-12) is itself
  SESSION-RECORD / FRAMING-OPEN: default (B) (srs=instrument, diamond=engine) is
  PROVISIONAL pending Grant confirm; "(A) substrate challenge" (migrate to srs)
  remains a live falsification axis. Engine and axiom AGREE on diamond for
  production; the residual mismatch is the NAME "Laves K4" (P0 walk-back queued,
  `eq_axiom_1.tex:20`) plus the orthogonal crystal/amorphous tension. "K4" has ZERO
  def-node — highest-priority vocabulary debt. Precision note: the "K4 (DIAMOND)
  LATTICE" string is a section-comment banner at `k4_tlm.py:97`, not the module
  docstring title; claim holds.

### Seam 5 — Statistical vs crystallographic chirality (dynamical kappa_chiral vs geometric I4_1 32) — VERIFIED

- **Side A (dynamical):** an excited k_chi Cosserat order-parameter realized as the
  kappa_chiral=alpha*kappa_tilde scalar on the ACHIRAL Fd-3m diamond, asymmetrically
  loading mu-up/eps-down by local helicity. `eq_axiom_1.tex:35` says the PRODUCTION
  engine uses this; `cosserat_field_3d.py:115-124,522-523`. Chirality strength
  inherits the alpha calibration.
- **Side B (geometric/structural):** the literal I4_1 32 Wyckoff-8a atomic motif
  built in `chiral_lattice.py` (right=I4_1 32, left-mirror=I4_3 32). The srs net
  "models that decoration's geometric content" (`eq_axiom_1.tex:35`) — the
  INSTRUMENT path, not the substrate. `k4_tlm.py:535-548` asserts a port-handedness
  on the bipartite diamond, distinct from a true chiral space group.
- **Why it matters:** SEAM CONFIRMED REAL — both sides verbatim; the corpus already
  flags the broader question as an open structural seam (`the-abandoned-interior.md:183`,
  flag-don't-fix). The Fd-3m=k_chi=0 supergroup framing (`closure-roadmap:191`,
  Foundation Item 10) makes the NARROWER chiral-vs-centrosymmetric space-group
  question a closed FALSE POSITIVE (turn k_chi on, chiral subgroup appears beneath
  achiral supergroup). Whether the port-handed bipartite diamond genuinely realizes
  Axiom-1's CHIRAL I4_1 32 vs is an achiral-diamond-with-port-handedness is NOT
  settled in any code read — the code asserts "native chirality of the bipartite
  mapping" by fiat. "chirality" carries ZERO vocabulary def-node — THE load-bearing
  vocabulary gap. Citation precision: `translation-circuit.md:652` corroborates the
  supergroup/k_chi=0 line in a piezoelectric table row, not the instrument-vs-
  production split itself.

### Seam 6 — nu_vac = 2/7 axiom provenance (code "Axiom 2" label vs KB attribution) — DISPUTED (PARTIAL)

- **Side A:** `constants.py:319` labels N_NU=2/7 as "Poisson ratio (Axiom 2)" and
  :344 says "The K=2G lattice (Axiom 2)."
- **Side B:** the canonical KB axiom split puts K4-Cosserat MODULI structure under
  Axiom 1 (`CLAUDE.md:55`); Axiom 2 = Topo-Kinematic Isomorphism / charge-as-
  dislocation. The Poisson-ratio leaf derives 2/7 from K=2G which the closure leaf
  attributes to Vol1 Ch2 macroscopic moduli.
- **Why it matters:** DISPUTED — the seam is REAL but side_B is overstated/misread.
  Side_A confirmed verbatim. Side_B's claim that the leaf attribution is UNIFORMLY
  Axiom 1 / Vol1 Ch2 is WRONG: the KB itself repeatedly attributes the 2/7 K=2G
  provenance to Axiom 2 (`appendix-derived-numerology.md:22,62`;
  `mathematical-closure.md:94`; `dielectric-snap-limit.md:32`;
  `derived-numerical-constants.md:116`; `scale-separation.md:49`). The KB's
  consistent gloss is a TWO-AXIOM INTERLINK (Axiom 1 LC mechanism + Axiom 2
  alpha-value at which K=2G locks), which the code comment at :344 actually MATCHES.
  The genuine underlying seam is that "Axiom 2" ITSELF has two attested meanings:
  `axiom-homologation.md:391` records Grant's 2026-04-20 variant "Axiom 2: Wave
  propagation, K=2G" as "a SUBTLE VARIANT", and :397 states the CLAUDE.md
  INVARIANT-S2 correction is a QUEUED-but-unfinished item — an explicitly
  unadjudicated naming reconciliation, not unilateral code drift. Compounding
  sub-claims BOTH CONFIRMED: (1) double-definition N_NU:319 and NU_VAC:532 both 2/7;
  (2) stale comment :1036 reads "already defined at line 514" while the real NU_VAC
  def is at :532.

### Seam 7 — Calibration-input COUNT (three coexisting framings in one file) — VERIFIED

- **Side A:** STANDARD framing (pre-2026-05-15): three calibration inputs {ell_node,
  alpha, G} (`constants.py:11`). HISTORICAL label: {m_e, alpha, G}
  (`constants.py:114`, Input-1/2/3 blocks).
- **Side B:** CURRENT structural-closure framing: "one scale (ell_node) + one
  cosmological initial-data parameter (Omega_freeze) + four axioms"
  (`constants.py:12-13`) — i.e. NOT three calibration inputs at all. AND m_e is
  called both "Input 1" (:128) and "NOT an independent input" (:53) in the same file.
- **Why it matters:** SEAM REAL; all 5 constants.py citations open verbatim. THREE
  different count-framings coexist in ONE file, and m_e carries locally-contradictory
  labels resolved only by the scale-vs-derived distinction the file itself states at
  :130 (m_e operationalizes ell_node). Per the alpha-keystone finding (echo at the
  value level), even calling alpha "independent" is contested. The "interlock
  register" referred to elsewhere is this docstring prose (:5-51 + :110-127), not a
  code object — no object named "interlock register" exists in code, confirmed. An
  adjacent crystal-vs-amorphous sub-seam is also real and is an ASYMMETRIC seam
  (amorphous claim is confidence 0.3 "do not build on").

### Seam 8 — Axiom-1's per-node 6-DOF vs the scalar K4-TLM engine — VERIFIED

- **Side A:** Axiom 1 / `CLAUDE.md:55` asserts each K4 node carries 6 micropolar DOF
  (3 translational -> E + 3 microrotational -> B); the micro-rotation IS the
  substrate-native spin origin.
- **Side B:** `k4_tlm.py` does NOT implement a per-node 6-DOF micropolar tensor — it
  uses a scalar |V|^2 structural energy (`k4_tlm.py:529`) and self-describes
  (`k4_tlm.py:36`) as merely a DISCRETIZATION of the continuum Cosserat field. The
  micro-rotation omega lives in the SEPARATE continuum solver
  `cosserat_field_3d.py`, and is REDUCED to a SCALAR in
  `cosserat_master_equation_fdtd.py` (an explicit tractability choice).
- **Why it matters:** SEAM IS REAL (MATCH). Both sides verbatim; they genuinely
  conflict. The "micro-rotation IS a per-node DOF of the K4 lattice engine" reading
  of Axiom 1 is NOT literally realized in the K4-TLM engine. The corpus's own
  "continuous-springs reframing" (Grant 2026-05-15) is the stated rationale:
  K4=sampling, Cosserat continuum=physics. The 6-DOF node is realized ONLY in the
  dedicated CoupledK4Cosserat module (`k4_cosserat_coupling.py:185`) keeping K4
  photon-sector scalars + CosseratField3D (u,omega) in separate state — an
  engineering-choice split, not a single 6-DOF lattice node. Also
  `kirchhoff-network-method.md:16` says "3 mutual inductive struts"/node (z=3) while
  k4_tlm uses 4 ports (z=4) — two distinct corpus network mappings, both
  corpus-sanctioned per the D1 adjudication. The embedded crystal-vs-amorphous
  sub-part is RECONCILABLE (words conflict but scope to different scales).
  CORRECTIONS: (1) side_A path is `manuscript/ave-kb/CLAUDE.md:55`, NOT repo-root
  CLAUDE.md; (2) the named §1.5 explicit-Euler solver
  `simulate_ponder_01_srs_lc_mesh.py` does NOT exist anywhere under AVE-Core/src
  (find + grep = zero hits) — it is referenced only as a name at
  `kirchhoff-network-method.md:12` (likely a PONDER-repo or absent artifact), so its
  "DIFFERENT engine" claim is structurally correct but unverifiable line-by-line in
  Core.

---

## 4. Engine inventory

The L3 solver classes the grid actually computes on. "Represents" carries the
layer(s) each engine occupies plus its role.

| Engine | Lattice type | Periodic | Represents | File |
|--------|--------------|----------|------------|------|
| K4Lattice3D | z=4 bipartite-FCC diamond (achiral Fd-3m), 4-port TLM, S=1/2*1-I | periodic (np.roll; severable boundaries) | L2+L3: production K4-TLM substrate; phase-space V_inc phasor per 4 ports indexed by real-space site; carries Phi_link bond flux but NOT a per-node 6-DOF micropolar tensor (scalar \|V\|^2 energy) | `src/ave/core/k4_tlm.py:101-119,191-217,461-465` |
| MasterEquationFDTD | scalar Cartesian Yee-like grid (c_eff^2=c0^2/S(A)) | periodic or PML-absorbing | L3+L4: real-space scalar V leapfrog; calibration-FREE (native dx=c0=V_yield=1, CFL timestep); the A1 dilatation-mass channel; canonical autonomous-electron host (Mode I) | `src/ave/core/master_equation_fdtd.py:42-100,150-250,91-94` |
| CosseratField3D | continuum micropolar field on Cartesian grid (u + SO(3) omega both (...,3)) | periodic or PML-absorbing | L1+L3: genuine standalone SO(3)-vector Cosserat solver; mass-gap validation; hosts electron-unknot + (2,3) seeders; the charge-"3" Beltrami-helicity readout source | `src/ave/topological/cosserat_field_3d.py:766,827-828,1808-1825,1065-1164` |
| CoupledK4Cosserat | hybrid: K4 diamond (phase-space ports) + Cosserat continuum (real-space u,omega) | K4 periodic; Cosserat periodic or PML | L3: S1-D coupling L_c=(V^2/V_SNAP^2)*W_refl (zero new params, pure Axiom-4 reuse); locus where the A1-scalar/K4 and micro-rotation/Cosserat sectors meet; Q measured not projected (S6=A) | `src/ave/topological/k4_cosserat_coupling.py:400-500,550-750,844-888` |
| VacuumEngine3D | hybrid K4+Cosserat (wraps CoupledK4Cosserat) with composable sources/observers | K4 periodic; Cosserat periodic or PML; T=0 deterministic or T>0 Maxwell-Boltzmann | L3+L4: clean user-facing API; AutoresonantCWSource (G-12 varactor PLL), Beltrami helical source; observers tag REAL vs PHASE coords; the loop-gap harness host | `src/ave/topological/vacuum_engine.py:1540-1650,1700-1900` |
| CrystalEngine + crystal_graft_v2/v3/v4 | two operating branches bulk V + shear w (+ optional third Cosserat omega branch; class docstring at `crystal_engine.py:7` self-describes as "three-branch chiral micropolar (I4_1 32)"), I4_1 32 chiral | periodic or PML-absorbing | L3: real-space electron-genesis (bulk V trap=electron, shear w=photon) at nu_vac=2/7; v2 adds mass-gapped omega + kappa_chiral=alpha*kappa_tilde winding; v4 adds chi-from-photon + Woltjer/Taylor helicity-lock (alpha-free geometry) | `src/ave/core/crystal_engine.py:7,51; src/ave/core/crystal_graft_v4.py:74-150,200-350` |
| UnifiedGenesisEngine + AnnihilationEngine | crystal-graft-v4 + rarefaction bulk-density sector (rho_bar, u_adv) on Cartesian grid | periodic or PML-absorbing | L3: genesis-v5 seeded-snap carrier; rarefaction EOS OPPOSITE saturation (core saturates A->1 c_eff->inf, bulk rarefies rho_bar->-1/phi c_bulk->0); annihilation inherits step() byte-identical, adds drift-IC imprint + per-object windowed observers | `src/ave/core/unified_genesis_engine.py:67-150,200-400; src/ave/core/annihilation_engine.py:48-120` |
| chiral_lattice.py (srs instrument path) + v9..v17 | z=3 srs/Laves/Sunada-K4 (I4_1 32 Wyckoff-8a, both enantiomorphs) + achiral diamond CONTROL | periodic box (np.mod, cKDTree minimum-image) | L2+L3: geometric-chirality INSTRUMENT (NOT the production substrate); FROZEN at v17 as falsifiers only; build_srs_net degree-3, build_diamond_net degree-4 achiral Fd-3m control | `src/ave/core/chiral_lattice.py:199-217,227-269; src/ave/core/chiral_lattice_v17.py:288` |
| LoopGapHarness (v18+) | rank-parameterized config atop VacuumEngine3D (K4+Cosserat loop-gap probe) | inherits VacuumEngine3D (K4 periodic, Cosserat periodic/PML) | L3: unified harness (ranks 1=container..4=remanence) replacing per-version genesis silos; advance via rank not version number; alpha enters only as sqrt(alpha) seed amplitude | `src/ave/core/loop_gap_harness.py:60-99,100-200,588-590` |
| FDTD3DEngine + analytic solvers (Rupture/GW/Caustic/LBM) | Yee staggered E/H grid (dual eps_eff+mu_eff saturation); analytic non-time-stepping reference for rupture/GW | FDTD periodic or Mur/PML; rupture/GW are analytic (no grid) | L3: FDTD3DEngine standalone 6-component E/H (not K4/Cosserat-coupled); RuptureSolver=Regime-IV kinematics (asymmetric c_EM=c0/sqrt(S) vs symmetric Z-invariant); gw_propagation=symmetric refractive lensing (Gamma=0); LBM3D=non-AVE-native kinetic | `src/ave/core/fdtd_3d.py:28-120,150-350; src/ave/regime_4_rupture/rupture_solver.py:60-150; src/ave/gravity/gw_propagation.py:40-130` |
| master_fdtd_phasor_bridge (read-only observer) | per-bond TLM projection of MasterEquationFDTD scalar V at Z0=1 | follows the underlying MasterEquationFDTD grid | L4: canonical real->phase observer bridge; computes V_inc/V_ref/Gamma POST-step from a real-space scalar; explicitly does NOT alter dynamics; the implementation embodiment of the EVOLVE-vs-READOUT boundary | `src/ave/core/master_fdtd_phasor_bridge.py:10-12,42,72,87-90,138` |

---

## 5. Closing note — what this doc fills, and the vocabulary debt

**No existing matrix carried this full axiom -> continuum -> lattice -> engine ->
observable vertical.** The three closest existing artifacts each cover a different
slice:

- `research/2026-06-10_field-symbol-registry.md` — the only one carrying real/phase/
  bridge with engine file:lines, but it is research-DRAFT / not-canon and is
  substrate-symbol-only (`:1-4,23-35`).
- `translation-circuit.md` — substrate -> EE-analogy mapping (`:17-24,95-146`).
- `divergence-test-substrate-map.md` — prediction -> test-substrate, one layer above
  grid internals (`:25-29`).

This document fills that gap by carrying the full vertical for ~30 framings, and
extends `research/2026-06-10_field-symbol-registry.md` (the substrate-symbol DRAFT)
to the layer-stack + seam-inventory level.

**Vocabulary debt (carried from the spec, flagged OPEN):** of 7 load-bearing
cluster terms, 6 — K4, chirality, c, longitudinal, the-3, dark-wake — have ZERO
verifier-gated def-node. The 7th, phase-space (def-69f472), is the only registered
one and it is status=ambiguous (conflated with a SIZE — the A46 leak). K4 and
chirality are flagged highest-priority (physics-axis). Ruling venue:
`_orchestration/2026-06-14_photon-ontology-vocabulary-adjudication-handoff.md:83-97`,
Grant + auditor lane.

**Discipline reminder:** the seams are the payload. They are reported here verbatim
and flagged OPEN — this doc resolves none of them. Adjudication venues, as flagged
by the corpus itself: `the-abandoned-interior.md:183` (flag-don't-fix open seams),
the D1 memo (`2026-06-12_lattice-d1-adjudication-memo.md`), the magic-angle
provenance audit (`2026-06-14_magic-angle-provenance`, "retract magic-angle"
ruling), and the photon-ontology vocabulary handoff. Grant + auditor lane rule;
this cartography only stages the decision.
