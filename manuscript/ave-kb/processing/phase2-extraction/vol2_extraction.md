# Phase 2 Extraction Report — Vol 2 (Subatomic Physics)

**Volume:** `manuscript/vol_2_subatomic/`
**Taxonomy reference:** `.claude/phase1-taxonomy/vol2_taxonomy.md`
**Extraction date:** 2026-04-02
**Status:** Complete — all skeleton positions mapped

---

## 1. Source Directory Listing

```
vol_2_subatomic/
├── main.tex                          (48 lines)
├── frontmatter/
│   └── 00_title.tex
├── chapters/
│   ├── _manifest.tex                 (16 lines)
│   ├── 01_topological_matter.tex     (~153 lines)
│   ├── 02_baryon_sector.tex          (~382 lines)
│   ├── 03_neutrino_sector.tex        (~274 lines)
│   ├── 04_quantum_spin.tex           (~82 lines)
│   ├── 05_electroweak_gauge_theory.tex (~161 lines)
│   ├── 06_electroweak_and_higgs.tex  (~313 lines)
│   ├── 07_quantum_mechanics_and_orbitals.tex (~3753 lines)
│   ├── 08_planck_and_string_theory.tex (~103 lines)
│   ├── 09_computational_proof.tex    (~243 lines)
│   ├── 10_open_problems.tex          (~393 lines)
│   ├── 11_standard_model_overdrive.tex (~127 lines)
│   └── 12_the_millennium_prizes.tex  (~679 lines)
└── (shared backmatter via main.tex):
    ├── ../backmatter/01_appendices.tex       (~213 lines)
    └── ../backmatter/05_universal_solver_toolchain.tex (~592 lines)
```

Note: `../backmatter/02_full_derivation_chain.tex` exists on disk but is NOT `\input`-ted by vol_2 `main.tex` — see Anomaly A5.

---

## 2. Domain Structure — Chapter Labels Confirmed

| Chapter file | `\label` confirmed | Chapter title |
|---|---|---|
| 01_topological_matter.tex | `ch:topological_matter` | Topological Matter |
| 02_baryon_sector.tex | `ch:baryons` | The Baryon Sector |
| 03_neutrino_sector.tex | `ch:neutrino_sector` | The Neutrino Sector |
| 04_quantum_spin.tex | `ch:quantum_spin` | Quantum Spin |
| 05_electroweak_gauge_theory.tex | `ch:electroweak` | Electroweak Gauge Theory |
| 06_electroweak_and_higgs.tex | `ch:electroweak_higgs` | Electroweak and the Higgs |
| 07_quantum_mechanics_and_orbitals.tex | `ch:quantum_orbitals` | Quantum Mechanics and Atomic Orbitals |
| 08_planck_and_string_theory.tex | `ch:string_theory` | Planck Scale and String Theory |
| 09_computational_proof.tex | `ch:computational_proof` | Computational Proof |
| 10_open_problems.tex | `ch:open_problems` | Open Problems |
| 11_standard_model_overdrive.tex | `ch:overdrive` | Standard Model Overdrive |
| 12_the_millennium_prizes.tex | `ch:millennium_prizes` | The Millennium Prizes |

---

## 3. PATH-STABLE Anchor Confirmation

**Taxonomy requirement:** `vol2/quantum-orbitals/ch7-quantum-mechanics/index.md` is a PATH-STABLE anchor, referenced from Vol 5 as `ch:quantum_mechanics`.

**Source label at ch07 line 2:**
```latex
\chapter{Quantum Mechanics and Atomic Orbitals}
\label{ch:quantum_orbitals}
```

**STATUS: CONFIRMED with label mismatch.**

- The vol_2 source defines `\label{ch:quantum_orbitals}` (not `ch:quantum_mechanics`).
- Vol 5 cross-reference uses `ch:quantum_mechanics` — this label does NOT exist in vol_2.
- Resolution: The KB index node `vol2/quantum-orbitals/ch7-quantum-mechanics/index.md` must include a metadata annotation noting both the source label (`ch:quantum_orbitals`) and the Vol 5 cross-reference label (`ch:quantum_mechanics`) so the taxonomy architect can wire the cross-volume link explicitly.
- The PATH is stable as specified; the label discrepancy is a documentation issue, not a structural problem.

---

## 4. Skeleton-to-Source Mapping

### Domain A: Particle Physics (`vol2/particle-physics/`)

#### A.1 — Chapter 1: Topological Matter (`ch1-topological-matter/`)

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch01 chapter node | lines 1–10 | `ch:topological_matter` | Summary position |
| `mathematical-topology-of-mass.md` | §1.1 Mathematical Topology of Mass | lines 11–30 | no label | Leaf |
| `newtonian-inertia-as-lenz.md` | §1.2 Newtonian Inertia as Macroscopic Lenz's Law | lines 31–50 | no label | Leaf |
| `electron-unknot.md` | §1.3 Electron Unknot | lines 51–80 | `eq:dynamic_capacitance_yield` (~line 64) | Leaf |
| `regime-classification.md` | §1.4 Regime Classification | lines 81–100 | no label | Leaf |
| `torus-knot-ladder.md` | §1.5 Torus Knot Ladder | lines 101–130 | no label | Leaf |
| `chirality-and-antimatter.md` | §1.6 Chirality and Antimatter | lines 131–153 | no label | Leaf |

#### A.2 — Chapter 2: Baryon Sector (`ch2-baryon-sector/`)

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch02 chapter node | lines 1–20 | `ch:baryons` | Summary position |
| `topological-fractionalization.md` | §2.1 Topological Fractionalization (includes quark flavor content) | lines 100–244 | no label | Leaf — see Ambiguity A-M1 |
| `quark-flavors.md` | No distinct source section | — | — | GAP — see Ambiguity A-M1 |
| `self-consistent-mass-oscillator.md` | §2.2 Self-Consistent Mass Oscillator | lines 114–165 | no label | Leaf — Anomaly A2: duplicate subsection titles at lines 114 and 166 |
| `thermal-softening.md` | §2.? Thermal Softening | ~line 61 | `sec:thermal_softening` | Leaf |
| `torus-knot-ladder-baryons.md` | §2.? Torus Knot Ladder (in ch02) | ~line 213 | `eq:torus_knot_ladder` | Leaf |
| `proton-neutron-mass-split.md` | §2.? Proton/Neutron Mass Split | lines 244–382 | no label | Leaf — content in second half of ch02 |

#### A.3 — Chapter 3: Neutrino Sector (`ch3-neutrino-sector/`)

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch03 chapter node | lines 1–15 | `ch:neutrino_sector` | Summary position |
| `chiral-screening.md` | §3.? Chiral Screening | ~line 134 | `sec:chiral_screening`, `eq:chiral_threshold` | Leaf |
| `pmns-eigenvalues.md` | §3.? PMNS Eigenvalues | ~line 154 | `sec:pmns_eigenvalues`, `eq:theta12_leading`, `eq:theta23_leading`, `eq:theta13` | Leaf |
| `pmns-junction-model.md` | §3.? PMNS Junction | ~line 191 | `sec:pmns_junction`, `eq:pmns_13`, `eq:pmns_12`, `eq:pmns_23` | Leaf |
| `delta-cp-violation.md` | §3.? Delta CP | ~line 205 | `sec:delta_cp`, `eq:delta_cp_pmns` | Leaf |
| `neutrino-translation-table.md` | §3.? Translation table (via `\input{../common/translation_neutrino.tex}`) | ~line 260–274 | no label | Leaf → pointer to `ave-kb/common/translation-neutrino.md` |

#### A.4 — Chapter 4: Quantum Spin (`ch4-quantum-spin/`)

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch04 chapter node | lines 1–10 | `ch:quantum_spin` | Summary position |
| `spin-as-precession.md` | §4 intro / §4.1 | lines 11–40 | no label | Leaf |
| `larmor-derivation.md` | §4.? Larmor derivation | lines 41–65 | no label | Leaf |
| `visual-equivalence.md` | §4.? Visual Equivalence | lines 66–82 | no label | Leaf |

#### A.5 — Chapter 5: Electroweak Gauge Theory (`ch5-electroweak-gauge/`)

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch05 chapter node | lines 1–15 | `ch:electroweak` | Summary position |
| `gauge-boson-masses.md` | §5.? Gauge Boson Masses | lines 16–50 | no label | Leaf |
| `weinberg-angle.md` | §5.? Weinberg Angle | lines 51–90 | no label | Leaf |
| `weak-coupling.md` | §5.? Weak Coupling | lines 91–130 | no label | Leaf |
| `forward-to-ch6.md` | §5.? Forward reference to ch6 Higgs | lines 131–161 | no label | Leaf — content is a forward-reference section to ch06 |

#### A.6 — Chapter 6: Electroweak and Higgs (`ch6-electroweak-higgs/`)

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch06 chapter node | lines 1–15 | `ch:electroweak_higgs` | Summary position |
| `higgs-mechanism.md` | §6.1–6.2 Higgs mechanism content | lines 16–100 | no label | Leaf |
| `spontaneous-symmetry-breaking.md` | §6.3–6.4 SSB | lines 101–165 | no label | Leaf |
| `lepton-spectrum.md` | §6.5 Lepton Spectrum | ~lines 160–200 | `eq:muon_twist_angle` (~line 167) | Leaf — note: `eq:muon_twist_angle` is in §6.5, NOT §6.2 as taxonomy implied |
| `higgs-mass.md` | §6.6–6.7 Higgs mass derivation | lines 200–300 | no label | Leaf |
| `sm-ave-translation.md` | §6.8 SM/AVE translation table | ~lines 301–313 | `sec:sm_ave_translation`, `\input{../common/translation_particle_physics.tex}` | Leaf → pointer to `ave-kb/common/translation-particle-physics.md` |

---

### Domain B: Quantum Orbitals (`vol2/quantum-orbitals/`) — PATH-STABLE DOMAIN

This is the largest domain in the volume. Chapter 7 is ~3753 lines.

#### B.1 — Chapter 7: Quantum Mechanics (`ch7-quantum-mechanics/`)

**Chapter label:** `\label{ch:quantum_orbitals}` at line 2 — CONFIRMED PATH-STABLE anchor.

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch07 chapter node | lines 1–30 | `ch:quantum_orbitals` | Summary / PATH-STABLE anchor |
| `de-broglie-standing-wave.md` | §7 intro through Step 1 derivation | lines 30–400 | no section label on intro | Leaf — covers objectivebox + Steps 1a–1h |
| `de-broglie-n.md` | Inside `sec:radial_tl_eigenvalue` | ~line 401 | `eq:de_broglie_n`, `sec:radial_tl_eigenvalue` | Leaf — hydrogen standing wave quantization |
| `screening-rule.md` | Inside Step 1 / sec:radial_tl_eigenvalue | ~line 448 | `eq:screening_rule` | Leaf — core screening formula |
| `ode-verification.md` | ODE orbital verification section | after line 448 | `sec:ode_orbital_verification` | Leaf — numerical ODE check |
| `helium-symmetric-cavity.md` | Helium symmetric cavity section | — | `sec:helium_symmetric_cavity` | Leaf — multi-electron introduction |
| `qm-ave-translation.md` | Subsection inside helium section | — | `sec:qm_ave_translation` | Leaf → pointer to `ave-kb/common/translation-qm.md` — see Ambiguity A-M2 |
| `analog-ladder-filter.md` | Analog ladder filter section | — | `sec:analog_ladder_filter` | Leaf |
| `macro-cavity-saturation.md` | Macro cavity saturation section | — | `sec:macro_cavity_saturation` | Leaf |
| `geometry-pipeline.md` | Geometry pipeline section | — | `sec:geometry_pipeline` | Leaf |
| `scale-separation.md` | §Scale Separation: Knot Topology vs Orbital Geometry | lines 3430–3485 | `sec:scale_separation` | Leaf — knot vs orbital two-scale framework |
| `subshell-junction-scattering.md` | §Phase 5: Sub-Shell Junction Scattering | lines 3486–3515 | no label on subsection | Leaf — Op10 boron drop derivation |
| `helium-coupling-first-principles.md` | §Helium Coupling from First Principles | lines 3592–3670 | `sec:lattice_js2` | Leaf — He $J_{s^2}$ derivation |
| `knot-vs-orbital-table.md` | Table: Knot topology vs orbital geometry | lines 3519–3549 | `tab:knot_vs_orbital` | Leaf — see Anomaly A4 resolution below |
| `operator-domain-table.md` | Table: Operator domain assignment for IE solver | lines 3554–3571 | `tab:operator_domain` | Leaf |
| `chiral-factor.md` | §Chiral Factor: $p_c$ as Topological Coupling | lines 3671–3735 | `sec:chiral_factor` | Leaf |
| `bonding-mode-formula.md` | Stage E1 derivation, eq:omega\_bond\_derived | lines 1269–1340 | `eq:omega_bond_derived`, `eq:bonding_mode` | Leaf |
| `complete-solver-architecture.md` | resultbox: Complete Solver Architecture | lines 1449–1457 | no label (resultbox) | Leaf |
| `radial-eigenvalue-solver.md` | ABCD cascade / radial eigenvalue solver | lines 2096–2110 | resultbox: Radial Eigenvalue Solver, `eq:radial_eigenvalue_condition` | Leaf |
| `dual-formalism-architecture.md` | resultbox: E2 Summary — Dual-Formalism Architecture | lines 2612–2638 | no label (resultbox) | Leaf |
| `atom-as-radial-waveguide.md` | resultbox: The Atom as a Radial Waveguide | lines 1873–1895 | no label (resultbox) | Leaf — connects Steps 1+2 to waveguide picture |

**Ch07 section labels confirmed:**

| Label | Line (approx) | Description |
|---|---|---|
| `sec:radial_tl_eigenvalue` | ~401 vicinity | Radial TL eigenvalue |
| `sec:ode_orbital_verification` | mid-chapter | ODE verification |
| `sec:helium_symmetric_cavity` | mid-chapter | Helium cavity section |
| `sec:qm_ave_translation` | subsection inside helium | QM/AVE translation table |
| `sec:analog_ladder_filter` | mid-chapter | Analog ladder |
| `sec:macro_cavity_saturation` | mid-chapter | Macro cavity saturation |
| `sec:geometry_pipeline` | mid-chapter | Geometry pipeline |
| `sec:scale_separation` | ~3431 | Knot/orbital scale separation |
| `sec:lattice_js2` | ~3593 | Helium coupling |
| `sec:chiral_factor` | ~3671 | Chiral factor |

**Ch07 equation labels confirmed:**

`eq:de_broglie_n`, `eq:screening_rule`, `eq:ring_radius` (~1067), `eq:y_hopf` (~1144), `eq:y_perp` (~1156), `eq:ring_coulomb` (~1176), `eq:k_cross` (~1188), `eq:y_cross` (~1194), `eq:omega_bond_derived` (~1313), `eq:bonding_mode` (~1334), `eq:V_net` (~1484), `eq:V_eff` (~1514), `eq:semi_major` (~1547), `eq:eccentricity` (~1550), `eq:r_min` (~1555), `eq:r_max` (~1560), `eq:sigma_op4` (~1634), `eq:f_in` (~1664), `eq:sigma_l0` (~1675), `eq:vis_viva` (~1650), `eq:k_radial` (~1751), `eq:V_step` (~1769), `eq:reflection_coeff` (~1795), `eq:radial_eigenvalue` (~1817), `eq:radial_eigenvalue_condition` (~2013), `eq:abcd_section` (~2186), `eq:abcd_elements` (~2205), `eq:abcd_cascade` (~2253), `eq:abcd_eigenvalue` (~2282), `eq:centrifugal_barrier` (~2305), `eq:centrifugal_turning` (~2315), `eq:E_screened` (~2330), `eq:coupled_line_zo_ze` (~2898), `eq:k_same_shell` (~2944), `eq:k_complete` (~3173), `eq:V_complete` (~3185), `eq:kappa_hopf` (~3192), `eq:z_layered` (~3235), `eq:intersection_number` (~3275), `eq:crossing_angle` (~3295), `eq:V_crossing` (~3333), `eq:scale_ratio` (~3464), `eq:junction_loss` (~3496), `eq:k_perp` (~3407), `eq:k_bare_he` (~3623), `eq:k_hopf_he` (~3640), `tab:knot_vs_orbital` (~3522), `tab:operator_domain` (~3557)

---

### Domain C: Nuclear and Field Physics (`vol2/nuclear-field/`)

#### C.1 — Chapter 8: Planck Scale / String Theory (`ch8-planck-string/`)

| Skeleton leaf | Source section | Line range | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch08 chapter node | lines 1–10 | `ch:string_theory` | Summary position — ANOMALY: chapter label is `ch:string_theory`, NOT `ch:planck_scale` as taxonomy may assume |
| `planck-scale-derivation.md` | §8 Planck scale content | lines 11–50 | no label | Leaf |
| `string-theory-translation.md` | §8 String theory AVE translation | lines 51–103 | no label | Leaf |

#### C.2 — Chapter 10: Open Problems (`ch10-open-problems/`)

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch10 chapter node | lines 1–20 | `ch:open_problems` | Summary position |
| `mass-gap-problem.md` | §10.? Mass Gap | — | `sec:mass_gap` | Leaf — references `ch:mass_gap` (undefined in vol_2, Anomaly A6) |
| `navier-stokes-problem.md` | §10.? Navier-Stokes | — | `sec:navier_stokes` | Leaf — references `ch:navier_stokes` (undefined in vol_2, Anomaly A6) |
| `baryon-asymmetry.md` | §10.? Baryon Asymmetry | — | `sec:baryon_asymmetry`, `eq:eta_baryon` | Leaf |
| `hierarchy-problem.md` | §10.? Hierarchy Problem | — | `sec:hierarchy_problem` | Leaf |
| `dark-matter.md` | §10.? Dark Matter | — | `sec:dark_matter` | Leaf |
| `unification.md` | §10.? Unification | — | `sec:unification` | Leaf |
| `g-star-derivation.md` | §10.? g-star derivation | — | `eq:g_star_ave` | Leaf |
| `scale-invariance-table.md` | §10.? Scale invariance | — | `tab:scale_invariance` | Leaf |

#### C.3 — Chapter 12: Millennium Prizes (`ch12-millennium-prizes/`)

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch12 chapter node | lines 1–20 | `ch:millennium_prizes` | Summary position |
| `yang-mills-steps1-2.md` | §12.? Yang-Mills Mass Gap Steps 1–2 | lines 60–145 | `eq:lattice_dispersion` (~103), `eq:bogomolnyi_bound` (~144) | Leaf — Anomaly A3 revised: ONE occurrence of `eq:bogomolnyi_bound`, not two |
| `yang-mills-steps3-5.md` | §12.? Yang-Mills Steps 3–5 | lines 145–220 | no eq label | Leaf |
| `riemann-hypothesis.md` | §12.? Riemann | — | `sec:riemann_hypothesis` | Leaf |
| `p-vs-np.md` | §12.? P vs NP | — | `sec:p_vs_np` | Leaf |
| `navier-stokes-prize.md` | §12.? Navier-Stokes Prize | — | `sec:navier_stokes_prize` | Leaf |
| `birch-swinnerton-dyer.md` | §12.? Birch and Swinnerton-Dyer | — | `sec:birch_sd` | Leaf |
| `hodge-conjecture.md` | §12.? Hodge | — | `sec:hodge` | Leaf |
| `poincare-conjecture.md` | §12.? Poincaré | — | `sec:poincare` | Leaf |
| `knot-vs-orbital-table-ch12.md` | — | — | — | GAP — `tab:knot_vs_orbital` is at ch07 lines 3519–3549; NOT found in ch12; see Anomaly A4 |

---

### Domain D: Proofs and Computation (`vol2/proofs-computation/`)

#### D.1 — Chapter 9: Computational Proof (`ch9-computational-proof/`)

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch09 chapter node | lines 1–15 | `ch:computational_proof` | Summary position |
| `anomaly-catalog.md` | §9.? Anomaly Catalog | — | `sec:anomaly_catalog` | Leaf |
| `precision-policy.md` | §9.? Precision Policy | — | `sec:precision_policy` | Leaf |
| `methodological-contamination.md` | §9.? Methodological Contamination | — | `sec:methodological_contamination` | Leaf |
| `computational-graph.md` | §9.? Computational graph content | lines 16–220 | no section label | Leaf — Anomaly A7: line ~220 uses `\ref{ch:quantum_mechanics_and_orbitals}` (undefined; typo for `ch:quantum_orbitals`) |

#### D.2 — Chapter 11: Standard Model Overdrive (`ch11-overdrive/`)

| Skeleton leaf | Source section | Line range (approx) | `\label` / key marker | Notes |
|---|---|---|---|---|
| `index.md` | ch11 chapter node | lines 1–10 | `ch:overdrive` | Summary position |
| `overdrive-nuclear.md` | §11 Nuclear overdrive | — | `sec:overdrive_nuclear` | Leaf |
| `overdrive-protein.md` | §11 Protein overdrive | — | `sec:overdrive_protein` | Leaf |
| `overdrive-comparison.md` | §11 Comparison table | — | `tab:overdrive_comparison` | Leaf |
| `universal-energy.md` | §11 Universal energy formula | — | `eq:universal_energy` | Leaf |
| `axiom-survey.md` | — | — | — | GAP — No `axiombox` environments found in ch11 — see Ambiguity A-M3 |

---

### Domain E: Appendices (`vol2/appendices/`)

**All appendices A–E are in a single file:** `../backmatter/01_appendices.tex`
**Appendix F is in:** `../backmatter/05_universal_solver_toolchain.tex`

#### E.1 — App A: Translation Matrix (`app-a-translation-matrix/`)

| Skeleton leaf | Source | `\label` | Notes |
|---|---|---|---|
| `index.md` | `01_appendices.tex` App A | `app:translation_matrix` | Summary — contains 8 `\input` calls to `../common/translation_*.tex` |
| Each translation table leaf | → `ave-kb/common/` | — | Pointer leaves only — actual content in common/ |

The 8 translation table `\input` calls in App A:
- `../common/translation_particle_physics.tex`
- `../common/translation_qm.tex`
- `../common/translation_neutrino.tex`
- `../common/translation_gravity.tex`
- `../common/translation_nuclear.tex`
- `../common/translation_proteins.tex`
- `../common/translation_circuits.tex`
- `../common/translation_knot.tex`

#### E.2 — App B: Resolving Paradoxes (`app-b-paradoxes/`)

| Skeleton leaf | Source | `\label` | Notes |
|---|---|---|---|
| `index.md` | `01_appendices.tex` App B | `app:resolving_paradoxes` | Summary |
| `spin-half-paradox.md` | App B §1 Spin-1/2 | no section label | Leaf |
| `holographic-paradox.md` | App B §2 Holographic | no section label | Leaf |
| `peierls-nabarro-paradox.md` | App B §3 Peierls-Nabarro | no section label | Leaf |

#### E.3 — App C: Exact Analytical Derivations (`app-c-derivations/`)

| Skeleton leaf | Source | `\label` | Notes |
|---|---|---|---|
| `index.md` | `01_appendices.tex` App C | NO `\label` confirmed | Summary — Anomaly: App C has no `\label` in source |

#### E.4 — App D: Computational Graph (`app-d-computational-graph/`)

| Skeleton leaf | Source | `\label` | Notes |
|---|---|---|---|
| `index.md` | `01_appendices.tex` App D | `app:computational_graph` | Summary |
| `graph-architecture.md` | App D content | no section labels | Leaf |

#### E.5 — App E: DCVE Specification (`app-e-dcve/`)

| Skeleton leaf | Source | `\label` | Notes |
|---|---|---|---|
| `index.md` | `01_appendices.tex` App E | `app:dcve` | Summary |
| `dcve-specification.md` | App E content | no section labels | Leaf |

#### E.6 — App F: Universal Solver Toolchain (`app-f-solver-toolchain/`)

Source file: `../backmatter/05_universal_solver_toolchain.tex` (~592 lines)
Chapter label: `\label{app:solver_toolchain}` (line 2)

| Skeleton leaf | Source section | Line range | `\label` | Notes |
|---|---|---|---|---|
| `index.md` | App F chapter node | lines 1–5 | `app:solver_toolchain` | Summary position |
| `regime-eigenvalue-method.md` | §1 Regime-Boundary Eigenvalue Method | lines 6–76 | `sec:regime_eigenvalue` | Leaf — universal 5-step procedure + Schwarzschild worked example |
| `kerr-q-correction.md` | §1.1 Kerr Q Correction | lines 77–136 | `sec:kerr_q_correction`, `eq:kerr_q`, `eq:r_omega` | Leaf |
| `lattice-phase-transition.md` | §1.2 Lattice Phase Transition | lines 138–159 | no section label | Leaf |
| `protein-eigenvalue.md` | §2 Protein Backbone Eigenvalue | lines 161–217 | `sec:protein_eigenvalue`, `eq:flory`, `eq:protein_ell` | Leaf |
| `nuclear-eigenvalue.md` | §3 Nuclear Eigenvalue | lines 244–313 | `sec:nuclear_eigenvalue` | Leaf |
| `torus-knot-ladder-toolchain.md` | §4 Torus Knot Ladder | lines 278–313 | `sec:knot_ladder` | Leaf |
| `semiconductor-junction-analogy.md` | §5 Semiconductor Junction Analogy | lines 315–360 | `sec:junction_analogy` | Leaf |
| `universal-constants-exchange.md` | §6 Universal Constants as Currency Exchange | lines 362–384 | `sec:currency_exchange_solver` | Leaf |
| `cross-scale-isomorphism-table.md` | §7 Cross-Scale Isomorphism Table | lines 386–420 | `sec:solver_isomorphism` | Leaf |
| `knot-mode-isomorphism.md` | §8 Knot Crossing Number / Mode Number Isomorphism | lines 423–445 | `sec:knot_mode_isomorphism` | Leaf |
| `sm-translation-toolchain.md` | §9 Standard Model Translation | lines 448–487 | `sec:sm_translation` | Leaf — contains GR and QM sub-tables |
| `derived-numerology.md` | §10 Derived Numerology | lines 489–546 | `sec:qnm_numerology`, `eq:universal_eigenvalue`, `eq:ave_qnm_Q` | Leaf |
| `cross-domain-physics-mappings.md` | §11 Cross-Domain Physics Mappings | lines 548–592 | `sec:cross_domain_mappings` | Leaf — K4-TLM, semiconductors, RF/proteins subsections |

---

## 5. Empty Skeleton Positions (Gaps)

| Skeleton position | Status | Explanation |
|---|---|---|
| `particle-physics/ch2-baryon-sector/quark-flavors.md` | GAP | No distinct source section; quark flavor content is embedded in `\section{Topological Fractionalization}` — see Ambiguity A-M1 |
| `nuclear-field/ch12-millennium-prizes/knot-vs-orbital-table-ch12.md` | GAP — WRONG VOLUME | `tab:knot_vs_orbital` is at ch07 lines 3519–3549, NOT in ch12 — Anomaly A4 resolution |
| `proofs-computation/ch11-overdrive/axiom-survey.md` | GAP | No `axiombox` environments found in ch11 — see Ambiguity A-M3 |
| `appendices/app-c-derivations/[leaf]` | PARTIAL GAP | App C has no `\label`; content exists but no labelled entry points |

---

## 6. Leaf Boundary Notes

**Ch07 special cases:**

1. **Lines 1–400 (Steps 1a–1h):** The opening of ch07 spans from the chapter declaration through approximately 8–10 stepped derivation subparagraphs labeled Step 1(a) through Step 1(h). These cover the standing wave derivation, Bohr radius emergence, and single-electron eigenvalue. The taxonomy skeleton maps these to a single leaf (`de-broglie-standing-wave.md`), but the source content is ~400 lines and could be subdivided. Current recommendation: keep as one leaf; the distiller can partition internally.

2. **Lines 1449–1457 resultbox (`Complete Solver Architecture`) through lines 2638 (`E2 Summary — Dual-Formalism Architecture`):** These two resultboxes bracket ~1200 lines of detailed ABCD cascade derivation. The skeleton maps these to ~6 leaves covering the cascade sub-stages. Boundary identification is clean: each named resultbox or labeled subparagraph (E2d, E2f, E2g, etc.) forms a natural unit.

3. **`sec:qm_ave_translation` inside `sec:helium_symmetric_cavity`:** This translation table subsection is nested within the helium section, not a standalone top-level section as taxonomy §3 implied. The leaf `qm-ave-translation.md` should note its structural position. Content is `\input{../common/translation_qm.tex}` — leaf is a pointer only.

4. **Lines 3430–3753 (Scale Separation through end of chapter):** This terminal block of ch07 contains `sec:scale_separation`, Phase 5 junction scattering, `sec:lattice_js2` (helium coupling), `tab:knot_vs_orbital`, `tab:operator_domain`, and `sec:chiral_factor`. The taxonomy maps these to 6–7 leaves. Boundaries between leaves are clean at subsection / table delimiters.

**Ch02 special case (Anomaly A2):**
Two subsections titled "The Self-Consistent Mass Oscillator (The Structural Eigenvalue)" appear at lines ~114 and ~166. The taxonomy leaf `self-consistent-mass-oscillator.md` should map to the FIRST occurrence (lines ~114–165), treating the second as a variant or correction of the same derivation. The distiller should flag this duplication in the leaf metadata.

---

## 7. Notation and Macro Notes

All custom macros are defined in `../structure/commands.tex` using `\providecommand` (safe to re-input). The following macros appear in vol_2 source and require Markdown translation at distillation time:

| Macro | Definition | Markdown rendering |
|---|---|---|
| `\Lvac` | Vacuum inductance per unit length | `$L_{\text{vac}}$` |
| `\Cvac` | Vacuum capacitance per unit length | `$C_{\text{vac}}$` |
| `\Zvac` | Vacuum impedance | `$Z_{\text{vac}}$` |
| `\Wcut` | Cutoff frequency | `$\omega_{\text{cut}}$` |
| `\lp` | Lattice pitch | `$\ell_p$` |
| `\vacuum` | Vacuum lattice symbol | `$\mathcal{V}$` |
| `\slew` | Slew rate | `$\dot{V}$` |
| `\planck` | Planck constant | `$\hbar$` |
| `\permeability` | Permeability | `$\mu_0$` |
| `\permittivity` | Permittivity | `$\varepsilon_0$` |
| `\impedance` | Impedance symbol | `$Z_0$` |

**tcolorbox environments** (all unlabelled — no `\label` support):
- `resultbox{Title}` → rendered as a titled callout block in Markdown
- `objectivebox` → opening chapter objectives
- `examplebox` → worked example block
- `axiombox/axiom` → axiom statement block
- `summarybox` → NOT used in vol_2 (see below)
- `exercisebox` → NOT used in vol_2 (see below)

**Vol 2 summarybox/exercisebox exception:**
All 12 chapters of vol_2 use `\section*{Chapter Summary}` and `\section*{Exercises}` (unnumbered LaTeX sections), NOT the `summarybox`/`exercisebox` tcolorbox environments. This contradicts the shared-volume INVARIANT in the taxonomy. Ch07 confirmed: `\section*{Chapter Summary}` at line 3740, `\section*{Exercises}` at line 3748.

---

## 8. Ambiguities — Requiring Taxonomy Architect Decision

### A-M1: Quark Flavors leaf has no distinct source section
**Skeleton position:** `vol2/particle-physics/ch2-baryon-sector/quark-flavors.md`
**Issue:** The taxonomy assumes a section on quark flavors at ch02 §2.2.1. In source, quark flavor content is embedded inside `\section{Topological Fractionalization}` (~line 245) with no subsection break.
**Recommendation:** Merge `quark-flavors.md` into `topological-fractionalization.md` and update the skeleton. Alternatively, distiller can extract only the quark flavor paragraphs as a standalone leaf with manual boundary annotation.

### A-M2: `sec:qm_ave_translation` is nested inside `sec:helium_symmetric_cavity`
**Skeleton position:** `vol2/quantum-orbitals/ch7-quantum-mechanics/qm-ave-translation.md`
**Issue:** Taxonomy §3 implied `sec:qm_ave_translation` was a standalone §7.5. In source it is a subsection inside the helium section. The label is correct; the structural position is one level deeper than expected.
**Resolution:** No skeleton change needed. The leaf still maps cleanly to `sec:qm_ave_translation`. Note in leaf metadata: parent section is `sec:helium_symmetric_cavity`.

### A-M3: No axiombox in ch11
**Skeleton position:** `vol2/proofs-computation/ch11-overdrive/axiom-survey.md`
**Issue:** No `axiombox` tcolorbox environments found in `11_standard_model_overdrive.tex`.
**Recommendation:** DROP this leaf position or reassign to a textual survey of axiom applications in ch11, sourced from the narrative paragraphs in the `sec:overdrive_nuclear` and `sec:overdrive_protein` sections.

### A-M4: `tab:knot_vs_orbital` is in ch07, NOT ch12
**Skeleton position (as written in taxonomy):** `vol2/nuclear-field/ch12-millennium-prizes/knot-vs-orbital-table-ch12.md`
**Actual source location:** ch07 lines 3519–3549, `\label{tab:knot_vs_orbital}`
**Recommendation:** MOVE this leaf position to Domain B (quantum-orbitals/ch7-quantum-mechanics/), creating `knot-vs-orbital-table.md` there. The ch12 skeleton position should be removed or reassigned to a different ch12 content unit.

### A-M5: App C has no `\label`
**Source:** `01_appendices.tex`, App C "Summary of Exact Analytical Derivations"
**Issue:** No `\label{app:...}` found on App C chapter/section command.
**Recommendation:** KB index node for App C should note the missing label and reference only by content location (backmatter/01_appendices.tex, App C block). Cross-references from other volumes to App C by label will fail.

### A-M6: Ch08 label is `ch:string_theory`, not `ch:planck_scale`
**Source:** `08_planck_and_string_theory.tex`, confirmed `\label{ch:string_theory}`
**Issue:** Taxonomy domain/skeleton uses "planck-string" path segment (correct), but any internal reference expecting `ch:planck_scale` will fail.
**Recommendation:** KB index for ch08 must document the actual label `ch:string_theory` explicitly.

---

## 9. Confirmed Anomalies from Survey Phase

All anomalies from the Phase 0 survey (A1–A10) have been verified against source. Updated status:

| ID | Description | Status |
|---|---|---|
| A1 | Large chapter 7 (~3500+ lines) | CONFIRMED — 3753 lines total |
| A2 | Duplicate subsection title in ch02 | CONFIRMED — lines ~114 and ~166 |
| A3 | `eq:bogomolnyi_bound` duplication | REVISED — ONE occurrence at ch12 line ~144 (not two) |
| A4 | `tab:knot_vs_orbital` location | RESOLVED — table is in ch07 (3519–3549), NOT ch12 |
| A5 | `02_full_derivation_chain.tex` not included | CONFIRMED — file exists, not `\input`-ted by vol_2 main.tex |
| A6 | `ch:mass_gap`, `ch:navier_stokes` undefined | CONFIRMED — referenced in ch10 intro, defined nowhere in vol_2 |
| A7 | `\ref{ch:quantum_mechanics_and_orbitals}` typo in ch09 | CONFIRMED — line ~220, undefined label, should be `ch:quantum_orbitals` |
| A8 | `app:full_derivation_chain` dangling | CONFIRMED — referenced in ch03, backmatter file not included |
| A9 | Vol 5 cross-reference label mismatch | CONFIRMED — Vol 5 uses `ch:quantum_mechanics`, source has `ch:quantum_orbitals` |
| A10 | No `\label` on App C | CONFIRMED — App C block has no label |

---

## 10. Cross-Volume References Requiring Coordinator Attention

| Reference in vol_2 source | Vol_2 label used | Target volume | Status |
|---|---|---|---|
| Vol 5 uses `ch:quantum_mechanics` → ch07 | `ch:quantum_orbitals` | Vol 5 | LABEL MISMATCH — coordinator must align |
| ch10 §10.? refs `ch:mass_gap` | undefined in vol_2 | Unknown (Vol 3 or later vol) | DANGLING |
| ch10 §10.? refs `ch:navier_stokes` | undefined in vol_2 | Unknown (Vol 3 or later vol) | DANGLING |
| ch07 line ~2931 refs `ch:network_solver` (Vol V) | undefined in vol_2 | Vol 5 | FORWARD REF |
| ch03 refs `app:full_derivation_chain` | file exists but not included | backmatter/02_full_derivation_chain.tex | DANGLING |

---

## 11. Estimated Confirmed Leaf Count

| Domain | Index nodes | Leaf nodes | Notes |
|---|---|---|---|
| A: Particle Physics (ch1–6) | 7 | ~35 | All mapped |
| B: Quantum Orbitals (ch7) | 2 | ~21 | All mapped; ch07 is the dominant chapter |
| C: Nuclear and Field (ch8, ch10, ch12) | 4 | ~20 | ch12 has 1 GAP (`knot-vs-orbital-table-ch12`) |
| D: Proofs and Computation (ch9, ch11) | 3 | ~10 | 1 GAP (`axiom-survey`) |
| E: Appendices (A–F) | 7 | ~25 | App C has no label; App F fully mapped |
| **Total** | **23** | **~111** | 3 confirmed GAPs |

---

*End of Phase 2 Extraction Report — Vol 2*
