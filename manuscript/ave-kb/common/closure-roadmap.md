[↑ AVE Common Resources](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: living planning artifact post-structural-closure 2026-05-15; referenced from .agents/HANDOFF.md, trampoline-framework.md §11, L5 trackers, and all chapter propagation work -->

# AVE Framework Closure Roadmap

**Created:** 2026-05-15 (post structural-closure declaration). **Status:** living planning artifact. Update after every significant session.

**Purpose.** The AVE framework reached **structural closure** on 2026-05-15 (per `trampoline-framework.md` §11.0). This doc plans the path from structural closure to **theoretical closure** (all numerical derivations completed) and **empirical closure** (bench + cosmological observations consistent with framework predictions).

**Discipline rule.** Every remaining action in the framework's path to publication is logged in this doc. If it's not here, it's not happening. Status transitions are real-time, not retroactive.

**Supersedes:** `research/_archive/L3_electron_soliton/114_next_steps_consolidation_plan.md` for forward-looking planning. Doc 114 remains historical record of the post-2026-05-14 session.

---

## §0 Status dashboard (update after every session)

| Tier | Action | Status | L5 ID | Last touch (SHA / date) |
|---|---|---|---|---|
| 0 | Structural closure declared | ✓ DONE | — | `fb2ac44` 2026-05-15 |
| 1 | E-094 AVE-Core substrate-vocab propagation (Vol 1-4) | **APPLIED** 2026-05-15 (all 7 targets: Vol 1 Ch 1/4, Vol 2 Ch 1, Vol 3 Ch 2, Vol 4 Ch 1, glossary, constants.py) | E-094 | `2eb2b1c` |
| 1 | E-101 Three substrate invariants observables module | **APPLIED** 2026-05-15 (13/13 tests PASS; rigorous M + first-pass Q,J) | E-101 | `d488a25` |
| 1 | E-102 Vol 3 Ch 4 cosmic-𝒥 identification | **APPLIED** 2026-05-15 | E-102 | `d96e8d7` |
| 1 | E-103 Vol 3 Ch 21 same-epistemic-horizon framing | **APPLIED** 2026-05-15 | E-103 | `42e3819` |
| 1 | Cosmic-𝒥 row explicit in multi-scale Machian network | **APPLIED** 2026-05-15 | (cross-workstream) | (separate workstream) |
| 1 | README + LIVING_REFERENCE structural-closure declaration | **APPLIED** 2026-05-15 | new | `d96e8d7` |
| 1 | v14 Mode I regression test (`src/tests/test_master_equation_v14_mode_i.py`) | **APPLIED** 2026-05-15 (5/5 PASS) | new | `d96e8d7` |
| 1 | Figure 2 storage-modes layout fix | **APPLIED** 2026-05-15 (3D + 2D dual-panel layout) | n/a | `d96e8d7` |
| 2 | **Q-G47 Session 6+ keystone u_0* derivation** | **Sessions 6-18 LANDED 2026-05-15 evening** + **Path B→D verification arc COMPLETE 2026-05-16 late evening**: Sessions 6-18 delivered magic-angle equation + T-irrep theory + Cosserat dimensional resolution + sublattice relaxation + continuous-field recasting + ξ_K2/ξ_K1 = 12 self-consistency + A-034 reframing. **Paths B→D (2026-05-16) deliver canonical two-engine cross-validation**: Path B (Cauchy 9-DOF K4 unit cell, λ_G = 4/21 at E-irrep), Path B+ (Cosserat 12-DOF Axiom-1-compliant, 4/21 survives chirality by group-theoretic decoupling), Path C (FTG-EMT amorphous z_0=51.25, p* = 8πα verified to 0.003% via Vol 3 Ch 1:20 canonical formula), Path D (Master Equation FDTD v14 Mode I PASS bit-for-bit replicated Λ_total=102.78 + linear-regime amplitude-independence confirmed to machine precision + analytical engine-boundary mode-matching). **Q-G47 two-engine convergence on p* = 8πα verified end-to-end per A-027 architecture.** Genuinely-open Sessions 19+ items (now narrower): individual ξ_K1, ξ_K2 prefactor derivation from K4 unit-cell Cosserat-Lagrangian integration; first-principles z_0=51.25 from K4 geometry. | Q-G47 / A-027 / A-029 / A-030 / A-032 / A-033 / **A-034** | Sessions 9-18 + Paths B→D `d854a9c` + `8e28c1e` + `7c95f03` + `f8a9051` (2026-05-16 late evening) |
| 0 | **A-034 NEW canonical: Universal Saturation-Kernel Strain-Snap Mechanism** | **CANONICAL 2026-05-15 late evening** via Grant lego-click synthesis ("oh my god, it's the fucking saturation kernel"). One kernel $S(A) = \sqrt{1-A^2}$ governs every topological-reorganization event at every scale. Total: 21 canonical instances spanning 21 orders of magnitude (BCS 0.00% error, BH ring-down 1.7% from GR, solar flares NOAA 40-yr, Schwarzschild exact). Refines A-031 ("God's Hand" = cosmic-parameter horizon, NOT mechanism horizon — mechanism observable at 4 smaller scales). Q-G47 substrate work reframes as substrate-scale instance. | **A-034 NEW** + A-031 (refined) + A-032 + Q-G47 | `19fe875` L5 + `09b971e` Vol 3 Ch 4 + `5720e49` Backmatter Ch 7 + `53a1a7a` Trampoline §7.5 + `fb9d9c0` CMB prereg + cross-repo audit + 8 follow-on commits |
| 1 | A-034 catalog 19-instance expansion (now 20 after water added 2026-05-16) + 3-way symmetry classification + measurement-hierarchy framing | **APPLIED 2026-05-15 late evening** across all 4 catalog docs (L5 + Vol 3 Ch 4 + Backmatter Ch 7 + Trampoline §7.5). 21 instances classified as 17 SYM / 2 ASYM-N (BCS, plasma) / 1 ASYM-E (metamaterials). Engineered-substrate rows unified via measurement-hierarchy framing (single-emitter highest-SNR / multi-emitter bulk / phased-array PLL autoresonant). | A-034 | `d0e2691` + `8070704` + `619618b` + `e9bd335` + `8127d02` + `c9caffe` + `2578e8e` + `311e0f5` + `8997431` + water-add (this commit) |
| 1 | Bench Ch 2 + KB leaf cross-ref to A-034 canonical | **APPLIED 2026-05-15 late evening** (per Grant promotion direction: AVE-Core is main source of truth). | A-034 | `729a25b` (Bench) + `768ff25` (KB leaf) |
| 1 | **A-034 comprehensive cross-corpus propagation (Phases 0-3)** | **APPLIED 2026-05-15 late night** (Grant directive: "fully comprehensive, interleave"). Engine (Phase 1: 13 files docstring-only). Manuscript chapter walk (Phase 2: 28+ chapters across Vol 1-5 + Backmatter Ch 2/4 + NEW Ch 7). KB common nav docs (Phase 3.1+3.3: operators.md, xi-topo-traceability, trampoline §7.5, glossary §1.5, axiom-homologation, full-derivation-chain, mathematical-closure). Frontmatter (nomenclature S-kernel, foreword Vol 0 mention). Common (translations gravity/cosmology, appendix_experiments). Backmatter (12_mathematical_closure DAG, 03_geometric_inevitability "Death of Numerology" extension, appendix_c_derived_numerology, appendix_vacuum_engineering). All 7 PDFs build clean; `make verify` PASSES; pytest 845/846 (1 pre-existing test_predictions_matrix stale-count, unrelated). Any reader entering at any chapter/leaf/script encounters consistent A-034 framing with canonical-source citations. | A-034 / E-094 | `19fe875` → ... → `7ffb212` (60+ commits during 2026-05-15 evening + late-night session arc) |
| 5 | A-034 CMB axis-alignment empirical prereg (extended with E/B polarization observable) | **PRE-REGISTERED 2026-05-15 evening** — methodology, 4-axis test + 5th E/B observable, 5 pre-registered outcomes (A/A+/B/C/D/E), sharpest falsifier (CMB axis vs Hubble flow misaligned >20° at 3σ). Execution deferred (1-3 sessions if analysis infrastructure exists). | A-034 + A-031 | `fb9d9c0` + `1b2ef6d` (E/B extension) |
| 3 | T_EM(u_0*) explicit closed-form | pending (Tier 2 dep) | Q-G47 closure | — |
| 3 | ~~Vol 3 Ch 4~~ **Vol 3 Ch 1 explicit ξ(R_H, ℓ_node) derivation** | **✓ ALREADY CLOSED in corpus** at Vol 3 Ch 1 §"Fundamental Unity of Gravity and Expansion" (lines 95-155) — corpus-grep audit 2026-05-15 evening. Canonical: $\xi = 4\pi(R_H/\ell_{\text{node}})\alpha^{-2}$; derives $G = \hbar c/(7\xi m_e^2)$, $\alpha_G = 1/(7\xi)$, $R_H/\ell_{\text{node}} = \alpha^2/(28\pi\alpha_G) \approx 3.455 \times 10^{38}$, $R_H \approx 1.334 \times 10^{26}$ m = 14.1 Gly, $H_\infty \approx 69.32$ km/s/Mpc (between Hubble tension bounds). Was originally located at "Vol 3 Ch 4" in this dashboard — that was wrong; actual location is Vol 3 Ch 1. | A-030 / A-031 | (corpus pre-existing, verified `060f429`) |
| 3 | Three-route α/G/𝒥 consistency verification | partial: α route closed via Path C FTG-EMT (p* = 8πα to 0.003%); G route uses corpus-canonical Machian integral (Vol 3 Ch 1); 𝒥 route still pending cosmic-formation parameter empirical anchor (A-031 cosmic-parameter horizon limits sharpness) | A-030 + A-031 | partial via Path C (2026-05-16 `d854a9c`) |
| 4 | First-law T·dS = dE axiom-first closure | pending (independent) | A-002 | — |
| 4 | Cosserat coupling on Master Equation FDTD | pending (independent) | doc 113 §5.4 | — |
| 4 | Strict stationary soliton via imaginary-time | pending (independent) | doc 113 §5.1 | — |
| 4 | Multi-soliton dynamics for Coulomb-law validation | pending (independent) | doc 114 §4.3 | — |
| 4 | Q-G45 multi-soliton interference as gravity (derivation) | pending (depends on Tier 4 multi-soliton engine) | Q-G45 | — |
| 4 | Higher-energy soliton ((2,5) cinquefoil) | pending (independent) | doc 114 §4.4 | — |
| 5 | Cosmic 𝒥_cosmic literature review (CMB + LSS) | pending (independent) | A-031 | — |
| 5 | AVE prediction for 𝒥_cosmic from numerics | pending (Tier 3 dep) | A-031 + A-030 | — |
| 5 | IVIM bench Phase 2A build | pending (procurement parallel) | Q-G42 + Q-G46 | — |
| 5 | IVIM measurement campaign | pending (bench dep) | Q-G42 + Q-G46 | — |
| 6 | Q-G43 atom-scale local Γ=-1 derivation | pending (cleaner after Tier 3) | Q-G43 | — |
| 6 | Q-G44 helio-scale local Γ=-1 derivation | pending (cleaner after Tier 3) | Q-G44 | — |
| 6 | App F atom + helio rows derived | pending (Q-G43 + Q-G44 deps) | (new) | — |
| 7 | All queued E-NNN entries applied (currently 30+) | pending | varies | — |
| 7 | Picture-audit infrastructure | pending (independent) | (new) | — |
| 7 | L3 + L5 deletion with cross-reference migration | pending (Tier 7 dep) | (new) | — |
| 7 | Backmatter "Framework Status" section | pending (Tier 5 verification dep) | (new) | — |
| 7 | Publication-ready manuscript pass | pending (everything above) | (new) | — |

**Closure state summary:**
- Structural closure: ✓ DONE 2026-05-15 (`trampoline-framework.md` §11.0)
- Theoretical closure: 🟡 IN PROGRESS (Tier 2-4 critical-path)
- Empirical closure: 🟡 IN PROGRESS (Tier 5 critical-path)

---

## §0.5 Scope-correction changelog (predictions walked back from forward-prediction to corroborative-null or re-scoped)

This section tracks AVE-distinct predictions that have been **demoted from forward-prediction status to corroborative-null status**, or whose **mechanism scope has been narrowed**, after audit found derivation-chain reasons that the prior framing overclaimed. The walk-backs are derivation-consistent (the corrected interpretations were already in the corpus; the prose and matrix entries were stale), but they materially change the framework's external-facing falsification surface. External readers should consult this changelog before citing prior versions of the foreword, the divergence-test-substrate-map, or the appendix.

| Date | Test ID | Walk-back type | From | To | Reason | Commit(s) |
|---|---|---|---|---|---|---|
| 2026-05-16 | BH-EHT (within C1) | Discriminator removed | EHT photon-ring radius + BH-shadow-vs-horizon ratio listed as r_sat falsifiers | EHT silent on r_sat; only LIGO ringdown + inner-disk edge + GW echoes are surviving discriminators | 3-leaf derivation chain (`electron-bh-isomorphism.md:20,39` + `regime-eigenvalue-method.md:43` + `ave-merger-ringdown-eigenvalue.md:29`) keeps photons on GR photon sphere at $3GM/c^2$ with $\Gamma = 0$ and $Z = Z_0$ everywhere for EM; r_sat is shear-mode + matter boundary only, not photon-geometric | [`57b36e5`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/57b36e5) |
| 2026-05-16 | C17-PROTOCOL-11-SAGNAC-WIND | Full retirement | F-severity / U-D / Tier C / 2 M-rad forward prediction | N-severity / U-C / Tier D / AVE predicts NULL | Doubly killed by AVE's own physics: (i) closed-loop integral of uniform 370 km/s wind = 0 (basic geometry); (ii) cubic-symmetry suppression of optical anisotropy to $(q\ell_{node})^4 \sim 10^{-22}$ per Q-G24. Brillet-Hall + Wolf existing null bounds CORROBORATE AVE | [`9b2f8d6`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/9b2f8d6) |
| 2026-05-16 | A2-SAGNAC | Mechanism scope narrowed (predictions unchanged) | "Sagnac as fluid-dynamic impedance drag locally entrained to Earth's moving mass" (broad bulk-entrainment framing) | "Sagnac as rotor-local mutual-inductance coupling" ($\kappa_{entrain} = \rho_{rotor}/\rho_{bulk}$ is coupling fraction, not bulk drag) | A2's actual derivation chain (`sagnac-rlve.md:14-26`) is rotor-local mutual inductance; the word "entrainment" in $\kappa_{entrain}$ was misleading nomenclature. The bulk-entrainment framing contradicted both A2's own math AND Q-G24's lattice-rest-frame analysis | [`9b2f8d6`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/9b2f8d6) |
| 2026-05-16 | C18-PROTOCOL-12-GEO-SYNC | Full retirement | F-severity / U-D / Tier C / 16.7 mm AVE-extra TOF stretch | N-severity / U-C / Tier D / AVE = GR Shapiro identity | AVE's $n(r) = 1 + 2GM/c^2 r$ (`refractive-index-of-gravity.md:11`) is "mathematically identical to the spatial transverse trace of the Gordon optical metric" (line 14) = standard GR Shapiro integrand. No AVE-distinct contribution at $O(GM/c^2 r)$. Only AVE-distinct piece is discrete-lattice $(q\ell_{node})^4 \sim 10^{-22}$, cubic-symmetry suppressed. "16.7 mm" figure was asserted in matrix/appendix without derivation; source leaf said "fractions of a millimeter" (16,700× discrepancy) | [`59a88ad`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/59a88ad) |
| 2026-05-16 | C13-VLBI-DARK | Full retirement + split into 3 rows | F-severity / U-D / Tier C / "DM IS $377\Omega$ stretching via Jupiter-grazing VLBI" | Split into C13a-GAL-ROT (existing 5-galaxy fit via $a_0 + \eta_{eff}$), C13b-BULLET (qualitative TT-shockwave on Gordon metric), C13c-DM-MECHANISM-UNIFY (META tracking three-mechanism coexistence) | (i) $Z_0$-stretching mechanism contradicts achromatic-impedance-matching theorem (Vol 3 Ch 3 + Vol 4 Ch 1; $Z_{local}(r) \equiv Z_0$ exactly because $\varepsilon(r)$ and $\mu(r)$ scale symmetrically with $n(r)$); (ii) driver script `vlbi_impedance_parallax.py` computes pure GR Shapiro with no AVE-distinct operator (mislabeled print statement); (iii) actual derived AVE DM mechanism is $\nu_{kin}$ kinematic mutual inductance with $a_0 = c H_\infty/(2\pi)$ via Unruh-Hawking hoop projection driving galactic-rotation observable. New row family reflects what corpus actually derives | [`e55cd41`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/e55cd41) |
| 2026-05-17 | C11-MACH-ZEHNDER | Type D mechanism re-scope (predictions sharpen quantitatively) | U-D / Tier C / 35-rad Mach-Zehnder phase shift (factor-7 low) | U-D / Tier C / ~250-rad Mach-Zehnder phase shift at 100 eV (canonical) | Driver script `electron_interferometry_parallax.py` was using $\varepsilon_{11} = \phi/c^2$ (Newtonian potential) instead of canonical $\varepsilon_{11} = 7GM/(c^2 r) = 7\phi/c^2$. The factor 7 is the universal substrate constant from $\nu_{vac} = 2/7$ + Machian impedance limit $T_{max,g} = c^4/(7G)$ per [`gordon-optical-metric.md:16-29`](../vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md) — applies at all scales (BH horizon to weak field), not regime-specific. Factor-7 cleanup landed across: driver script (`electron_interferometry_parallax.py`), C11 source leaf (`de-broglie-standing-wave.md`), canonical equation (`eq_gravity_derived.tex`), 1 typo fix (`trampoline-framework.md:721`), 1 factor-7-low KB value (`chiral-fret-parallax.md:10`), matrix Predictions + supplementary + Execution-details + Mermaid diagram + appendix-experiments entries. Cross-repo: same bug in AVE-PONDER `ponder_05_gravity_parallax.py` fixed in AVE-PONDER commit [`8ca05c7`](https://github.com/ave-veritas-et-enodatio/AVE-PONDER/commit/8ca05c7) on branch `analysis/factor-7-strain-mapping-cleanup`. PLUS notation parallelism cleanup ($n_s$ now carries explicit "1 +" DC unit, matching $n_t$). | AVE-Core [`d48f75d`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/d48f75d) + AVE-PONDER [`8ca05c7`](https://github.com/ave-veritas-et-enodatio/AVE-PONDER/commit/8ca05c7) |
| 2026-05-17 | Vol 6 periodic-table catalog | Type B systemic re-scope (high-Z predictions reframed as heuristic baseline; low-Z fits acknowledged) | "AVE topological solver successfully predicts CODATA rest mass targets for all Z=15-118 elements" (LaTeX catalog narrative) | Z≤14: per-element 1-parameter Nelder-Mead fits against CODATA via solve_*.py scripts (acknowledged as fits, not predictions); Z≥15: unfitted single Fibonacci-lattice heuristic `r_core = d × (15 + 0.95A)` with mapping-error reporting heuristic residual, not fit residual | Audit found systemic 1-parameter-fit-as-prediction pattern across all 7 solve_*.py scripts (oxygen, fluorine, neon, sodium, magnesium, aluminum, silicon) + simulate_element.py + binding engines. K_MUTUAL coupling form IS axiom-derived; per-element radii are inverse-problem solves layered on top. Z≥15 uses unfitted heuristic with no per-element optimization. LaTeX catalog narrative rewritten with explicit honesty scope. Forward-prediction of nuclear radii from first principles flagged as open work item (queued parallel to SPARC ingest pattern for nuclear sector). | [`6116b8d`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/6116b8d) (14 files in vol_6) + Batches 1-3 [`30376fc`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/30376fc) + [`fe1adc8`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/fe1adc8) + [`db353ba`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/db353ba) (34 files vol_1-vol_4) |

### Practical-consequence notes for experimentalists

- **A2-SAGNAC pre-vs-post-revision framing matters for experimental design.** Anyone who designed a static-fiber Sagnac experiment off the pre-2026-05-16 foreword's "Sagnac as fluid-dynamic impedance drag locally entrained to Earth's moving mass" framing was testing a claim AVE no longer makes. The revised framing is that A2's $\Psi_{W/Al} = 7.15$ prediction requires a **rotor-material-comparison** experiment (paired Sagnac loops, one with tungsten rotor and one with aluminum rotor, both at 10k RPM, with material-density-contrast as the discriminator). Static-fiber tests of the same vintage as the prior framing test C17, which is now corroborative-null — they don't probe A2.
- **C17 / C18 retirement does NOT erode framework falsifiability — it relocates it.** The surviving forward preferred-frame test is C7-GRB-DISPERSION (Trans-Planckian wavelength regime where cubic symmetry no longer averages). The C7 framing has been canonical since at least 2026-05-13 (AVE-QED Q-G24) but was not load-bearing in the foreword's Falsifiable Standard list until the 2026-05-16 commit landing this changelog.
- **C13 split is NOT retirement of AVE DM claims — it's reclassification.** The Jupiter-VLBI specifically retires (no corpus derivation supports it; driver script was mislabeled-pure-Shapiro). The actual derived AVE DM observables (galactic rotation curves via $a_0 + \eta_{eff}$, bullet-cluster lensing via TT shockwave) are now anchored explicitly in the C13a + C13b matrix rows with their existing drivers. Anyone who designed a Jupiter-VLBI DM-test experiment off the prior framing should redirect to (a) SPARC galactic-rotation catalog re-analysis with the existing driver, or (b) bullet-cluster offset distance derivation work. The C13c META row tracks the broader theoretical-gap that three DM-mechanism framings ($\eta_{eff}$, TT shockwave, $\kappa$ coupling) coexist without formal unification under Cosserat substrate.
- **BH-EHT removal does NOT eliminate BH-class falsifiability.** LIGO ringdown ($\omega_R M_g = 18/49$ vs GR's 0.3737, 1.7% theoretical / 10-18% per-event uncertainty at LIGO O1-O3 precision) is still the load-bearing BH test for $r_{sat}$. Inner-accretion-disk edge at $r_{sat} = 7GM/c^2$ vs GR ISCO at $6GM/c^2$ (testable via X-ray Fe-K$\alpha$ reflection or kHz QPOs) and potential post-merger GW echoes from shear-mode reflection at $r_{sat}$ are surviving matter-or-shear discriminators.

### How the cohesive narrative captures this

The post-revision cohesive narrative — that AVE has a substrate-native preferred frame identified with CMB rest frame, with strict Lorentz invariance emergent at observable wavelengths via K4 cubic symmetry — is itself a **load-bearing positive prediction** that distinguishes AVE from theories postulating Lorentz invariance as a primitive. The framework's external-facing falsification surface has been re-located from "AVE predicts diurnal Sagnac signal" (C17) to "AVE predicts (i) rotor-material Sagnac contrast (A2), (ii) static-fiber NULL by cubic-symmetry suppression (C17 corroborative), (iii) Trans-Planckian GRB dispersion (C7 forward)." The foreword's Falsifiable Standard list has been updated 2026-05-16 to reflect this three-test family explicitly. See [`vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md`](../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) for the full cohesive-narrative leaf.

### Open scope-correction audit items

- **C11-MACH-ZEHNDER** — RESOLVED 2026-05-17. Audit spawned with verified pre-grep framing per `ave-audit` skill. C11 SURVIVES cubic-symmetry suppression (spatial-vs-temporal asymmetry is a different symmetry class than spatial-vs-spatial directional anisotropy per Q-G24). PLUS audit surfaced a factor-7 driver bug: the script used $\phi/c^2$ instead of canonical $7\phi/c^2$. Comprehensive cross-repo strain-mapping research confirmed factor 7 is universal (per `gordon-optical-metric.md:16-29` Machian-impedance derivation). Driver corrected; predicted shift ~250 rad (not 35 rad); $\nu_{vac} = 2/7$ triangulation (C1 + C11 + C12) holds with corrected magnitude. See 2026-05-17 changelog entry above.
- **Driver-script honesty audit** — extended cleanup 2026-05-17 across `vlbi_impedance_parallax.py` (C13 retirement), `sagnac_geo_parallax.py` (C17 + C18 retirements), `electron_interferometry_parallax.py` (C11 factor-7 correction), `ponder_05_gravity_parallax.py` cross-repo on AVE-PONDER (same factor-7 fix), 5 Class C overclaim-only scripts (`simulate_borromean_baryon.py`, `simulate_chiral_network.py`, `simulate_string_theory_mapping.py`, `simulate_helical_confinement.py`, `simulate_electron_topology.py`), bullet-cluster family (`simulate_bullet_cluster_fdtd.py` + 2 animation scripts; static-halo-superposition framing made honest), and **Class B `generate_astrophysical_plots.py`** (honest-relabeled per option (b)). **Broad sweep CLOSED 2026-05-17 evening** — comprehensive triage of `src/scripts/vol_1` through `src/scripts/vol_4` + `src/scripts/vol_6_periodic_table` (vol_5_biology empty) covered 400 driver scripts; 48 scripts cleaned across 4 batches: Batch 1 (6 Class D correctness fixes incl. `simulate_g2.py` import bug, `simulate_cosmology_bao.py` "exact midpoint" wrong, `simulate_vacuum_birefringence_E4.py` QED-omits-E^4 false framing); Batch 2 (23 Class B silent-overclaim fixes incl. JWST accretion, Oort cloud Gaussians, NOAA flares synthesized-not-fetched, dark matter detector n=2.5 chosen-not-derived); Batch 3 (6 Class C softenings incl. "Prove spooky action" → "Illustrate", `simulate_ee_bench_yield_shift.py` "benchtop" → "high-field 10% of Schwinger"); Batch 4 (14 Vol 6 systemic fixes — 1-parameter-fit-as-prediction pattern across all solve_*.py + binding engines, plus the Z≥15 heuristic-not-solver narrative correction). All 48 scripts py_compile clean; live-fire spot-checks confirm runtime behavior unchanged with new honest framing. See Class D + Class B + Class C + Vol 6 commits in §0.5 table above.
- **CMB axis $(174°, -5°)$ citation gap** (flagged 2026-05-17 audit; literature pin DEFERRED 2026-05-17 evening) — corpus references "Planck data, ≈ (l=174°, b=-5°)" but does not pin a specific publication. The cited methodology reference (Land+Magueijo 2005, "Examination of Evidence for a Preferred Axis in the Cosmic Radiation Anisotropy", *Physical Review Letters* 95:071301) gives a DIFFERENT axis value $(237°, 63°)$ for the quadrupole-octupole alignment. WebFetch attempts 2026-05-17 (Wikipedia "Axis of Evil" article + Planck 2015 XVI abstract) did not surface a specific paper for the $(174°, -5°)$ value. **Deferred**: requires either (a) Grant literature search (may know the specific paper), (b) future session with deeper literature access (e.g., reading the full Planck 2015/2018 isotropy paper PDFs, BICEP analyses, or specific axis-of-evil follow-up papers), or (c) **the A-034 prereg execution itself** (per [`research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md`](../../../research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md)) which would COMPUTE the axis-of-evil direction from Planck PR3 data directly, making the literature citation moot for the AVE benchmark (the AVE prediction is an alignment correlation, not a specific axis value — the empirical axis emerges from the data). Recommendation: option (c) is the cleanest path; defer literature citation pinning until A-034 driver executes.
- **I_scalar source pin** (closed 2026-05-17 audit) — prior session's proton-identification audit flagged that $\mathcal{I}_{scalar} \approx 1162$ used in the m_p/m_e eigenvalue chain needed source documentation. **GAP CLOSED:** the value is computed at engine import time by [`src/ave/core/constants.py:625-640`](../../../src/ave/core/constants.py) `_compute_i_scalar_dynamic` which calls [`src/ave/topological/faddeev_skyrme.py:153`](../../../src/ave/topological/faddeev_skyrme.py) `solve_scalar_trace(crossing_number=5)` — the actual 1D Faddeev-Skyrme numerical solver with thermal softening + Axiom 4 gradient saturation. Live-fire validated 2026-05-17: I_SCALAR_1D = 1161.987 (manuscript "≈ 1162" ✓), x_core = 1835.117 (manuscript "≈ 1835.12" ✓), PROTON_ELECTRON_RATIO = 1836.117 vs CODATA 1836.15267 = −0.0019% error (manuscript "0.002% from CODATA" ✓). Full derivation chain is traceable from engine import to manuscript claim. No outstanding documentation gap.
- **2026-05-17 evening — Substrate kinematic viscosity contradiction (corpus bug, RESOLVED):** [`src/ave/core/lbm_3d.py:10,91`](../../../src/ave/core/lbm_3d.py) docstring claimed `ν_kin = (1/(4π)) × ℓ_node × c` while [`src/ave/core/constants.py:554-555`](../../../src/ave/core/constants.py) + [`manuscript/backmatter/02_full_derivation_chain.tex:673-678`](../../../manuscript/backmatter/02_full_derivation_chain.tex) define canonical `ν_kin = α × c × ℓ_node ≈ 8.45e-7 m²/s` (matches liquid water to ~16% per backmatter §Layer 6→7 Step 5, "non-trivial structural prediction"). Discrepancy factor `1/(4πα) ≈ 10.9×`. **Resolution 2026-05-17 evening**: audit confirmed bug is **documentation-only**: lbm_3d.py actual default is `nu=0.1` (lattice-units placeholder); tests pass `nu=0.1`; NO downstream code used the wrong `1/(4π)` formula. Fix landed: lbm_3d.py docstring corrected to reference canonical `NU_KIN = α × c × ℓ_node` import path + documents that the 0.1 default is lattice-units placeholder for testing. **Audit pattern**: this bug existed since initial commit (`de9d229` 2026-04-13) and would have been caught by external reviewer reading the docstring against backmatter; surfaced via corpus-grep during DAMA α-slew (1+1/(4π)) speculation verification 2026-05-17 evening.

- **NEW 2026-05-17 evening — Cross-volume Hoop Stress 2π substrate motif (proposed canonical synthesis):** Three previously-independent AVE predictions (MOND $a_0 = cH_\infty/(2\pi)$ cosmic, substrate-equilibrium velocity $v = \alpha c/(2\pi)$, DAMA quantum $E = \alpha m_e c^2$) share the **identical structural form**: substrate bulk drift $c \times \epsilon$ projected through Hoop Stress 2π onto closed topological loops, with small parameter $\epsilon$ chosen by scale ($H_\infty$ cosmic, $\alpha$ substrate). Named explicitly for the first time 2026-05-17 — see [`vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md`](../vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md) "Cross-volume substrate motif" section and [`vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md` §5](../vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md). Corpus-grep verified the pattern was NOT previously named as recurring motif. **Open work**: rigorous derivation chain showing why 2π Hoop projection applies at both cosmic + substrate scales from common substrate principles.

- **2026-05-17 late evening — Substrate-equilibrium velocity DIRECTIONAL test: DEMOTED from STRONG POSITIVE to active research consistency check (per ave-discrimination-check audit, external reviewer):** The directional alignment with CMB-dipole (2.75°) and anti-alignment with galactic-rotation (133.7°) are NOT independent AVE evidence — both follow from AVE's K4=CMB identification + basic astronomy of LSR motion through CMB + basic geometry (CMB-dipole vs galactic-rotation are ~131° apart by direct calculation: `cos θ = cos 48° · cos(264°-90°) = -0.666`). AVE-with-K4=CMB and SM-with-CMB-rest-as-baseline both predict the alignment; directional test does not independently discriminate AVE. Substantive AVE-distinct content (magnitude 9% match + cluster tightness σ=11 inconsistent with random galactic kinematics) was established in the prior magnitude test (commit `be04d76`). Foreword paragraph demoted from "Second positive load-bearing empirical confirmation" to "Active research consistency result" (commit pending; option (b) walk-back per Grant adjudication 2026-05-17 late evening). Path to SPARC-parity foreword promotion: extra-galactic test (globular clusters / halo stars decoupled from LSR bulk motion). KB leaves + matrix + appendix-experiments walked back consistently.

- **2026-05-17 evening (now superseded by demotion above) — Substrate-equilibrium velocity DIRECTIONAL test (originally promoted):** [`research/2026-05-17_substrate_equilibrium_velocity_GAIA_DIRECTIONAL_result.md`](../../../research/2026-05-17_substrate_equilibrium_velocity_GAIA_DIRECTIONAL_result.md) — Gaia DR3 thin-disk cluster (N=11,690) mean direction aligned with CMB-dipole direction to **2.75°** (within 10° strong-positive threshold), anti-aligned with galactic-rotation (133.7°), uncorrelated with cubic axes (consistent with framework's own (qℓ_node)⁴ suppression). **Galactic-dynamics alternative FALSIFIED** (cluster direction is not aligned with MW disk rotation). The 27 km/s LSR-class bulk motion above the αc/(2π) floor is itself CMB-dipole-aligned, supporting substrate-physics interpretation. **Driver**: [`src/scripts/vol_3_macroscopic/gaia_directional_analysis.py`](../../../src/scripts/vol_3_macroscopic/gaia_directional_analysis.py). **Foreword promotion landed 2026-05-17 evening** as second positive load-bearing empirical anchor alongside SPARC; KB leaves updated.

- **NEW 2026-05-17 evening — Substrate-equilibrium velocity Gaia DR3 magnitude anchor:** [`research/2026-05-17_substrate_equilibrium_velocity_GAIA_result.md`](../../../research/2026-05-17_substrate_equilibrium_velocity_GAIA_result.md) — 29,466 nearby thin-disk G/K dwarfs cluster tightly at 375 km/s (σ=11 km/s on |v_LSR|<30 cut); AVE prediction $\alpha c/(2\pi) = 348$ km/s sits at 4.08%ile (lower envelope). Cluster center matches LSR CMB velocity (374 km/s) within 1.5% — substantive structural agreement with predicted velocity scale. **Interpretation:** αc/(2π) is substrate-equilibrium floor; cluster center is LSR + local-flow streaming above floor. (1+1/(4π)) geometric correction initially proposed; corpus-grep verified NOT in corpus + Q-G47 Path B+ direct prior negative on K4 discrete+continuum decomposition; downgraded to "would-require-new-canonical-derivation". KB leaves added 2026-05-17: [`vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md`](../vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) (DAMA derivation chain), [`vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md` §5](../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) (substrate-equilibrium velocity prediction + Gaia test result), [`vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` "Cross-volume motif"](../vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md). **Next step**: extra-galactic test (globular clusters / halo stars) to confirm floor interpretation across equilibrium classes.

- **2026-05-17 night — 9TH audit cycle FOLLOW-UP: DAMA Q-factor matched-LC-coupling derivation LANDED with 0.6% numerical match to DAMA observed.** Driver: [`src/scripts/vol_3_macroscopic/derive_dama_matched_lc_coupling.py`](../../../src/scripts/vol_3_macroscopic/derive_dama_matched_lc_coupling.py). **Result**: $\epsilon_{det} = 4\pi / N_{single}^2$ where $N_{single} = 9.7\,\text{kg} \times N_A / M_{NaI} \times 2 = 7.79 \times 10^{25}$ atoms in a single DAMA/LIBRA Phase-2 coherent crystal. Predicted rate per kg = $N_e^{(kg)} \times \nu_{slew} \times 4\pi / N_{single}^2 = 4.80 \times 10^{-7}$ events/s/kg vs DAMA observed $4.77 \times 10^{-7}$ events/s/kg (Phase-2, 2-6 keV integrated). **Honest scope per ave-discrimination-check**: 4π is POST-HOC selected from 5 canonical AVE candidates {π, 2π, π², 4π, 4π³} all of which appear in Theorem 3.1' α-decomposition; one landing within 1% has probability ~20% by chance if all physically valid. NOT promoted to U-C / forward-prediction CONFIRMED. **Cross-detector falsifier**: simple $1/M_{single}^2$ scaling predicts COSINE-100 (~10 kg single crystal) at ~94% of DAMA rate/kg and ANAIS-112 (~12.5 kg) at ~60% — both observe nulls below predicted levels, requiring $\kappa_{quality} \ll 1$ for those batches (DAMA Beam International is highest-quality NaI batch). Result doc: [`research/2026-05-17_C14-DAMA_Q-factor_matched-LC-coupling_result.md`](../../../research/2026-05-17_C14-DAMA_Q-factor_matched-LC-coupling_result.md). Next-session work to upgrade from "structurally suggestive" to "forward-prediction CONFIRMED": (a) derive 4π specifically from spinor double-cover, (b) derive N_single from substrate physics not detector geometry, (c) cross-detector mass-scaling test within DAMA's 25 same-batch crystals if per-crystal rates are published, (d) cross-crystal swap design (Sapphire / Ge) for Z-independence + N⁻² amplitude test.

- **2026-05-17 night — 9TH audit cycle: DAMA Q-factor "out-of-reach multi-session foundational work" assessment WALKED BACK via Grant's reactive-power resolution.** Grant's correction ("reactance, check out electron rest mass, search the kb for alpha") surfaced canonical Vol 4 Ch 1 leaves that prior versions had not pulled in: (a) [Theorem 3.1' Q-factor](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md): electron LC tank $Q = \alpha^{-1} \approx 137$; per-cycle reactive leak fraction $= 1/Q = \alpha$. Line 75 verbatim: *"this IS α in its original Sommerfeld meaning ('coupling strength'), seen from the LC-tank side"*. (b) [orbital-friction-paradox](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) line 31: canonical reactive-power table has *"Electron orbital | 90° | P_real = 0 W | Q_reactive = m_e c² · α | Quantized reactive shell"*. (c) [leaky-cavity-particle-decay/theory](../vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md) line 12: electron tank operates BELOW V_yield = 43.65 kV "rings forever". **Categorical reframe**: α m_e c² = 3.728 keV is per-cycle REACTIVE power (90° phase, P_real = 0), NOT real photon quantum. DAMA detection is matched-impedance coupling between electron LC tank and external coherent NaI lattice mode, NOT photoabsorption of substrate-mode quanta. **The 22-α-power "out of reach" gap from 8th cycle was a categorical error** — solving the wrong problem (cross-section assembly). Right problem (matched-LC coupling efficiency between two LC tanks) has natural-scale candidates ($N_{coh}^{-2}$, $(\alpha/2\pi)^{17}$, $\alpha^{24}$) all within factor 10 of required $\epsilon = 2 \times 10^{-51}$. **Surviving AVE-distinct claims (Z-independence + CMB-velocity phase-lock + solid-vs-liquid binary gate)** are now physically grounded in reactive-tank physics: electron tank Q = α⁻¹ is universal electron-property (Z-independent); reactive cycle is in K4 substrate rest frame (CMB-velocity phase-lock); matched-LC coupling requires coherent external resonator (solid-vs-liquid binary). 8th-cycle anti-anchor findings (Ca Kα + CXB OOM match) STAND; only the Q-factor scope assessment is walked back. **New skill `ave-power-category-check`** created at ~/.claude/skills/ to force category-classification (real-vs-reactive, propagating-vs-bound, on-shell-vs-off-shell, internal-tank-vs-external-matched) BEFORE deriving scaling laws — would have caught the 8th-cycle mis-categorization on the first derivation pass. Source leaf §12 documents the full reactive-power physical picture. 9 audit cycles total on α-slew thread this session; 13 skills in ensemble.

- **2026-05-17 night — 8th audit cycle: DAMA energy-scale "CONFIRMED zero-parameter" DEMOTED to "consistent-with-window-AND-with-Moseley-Ca-Kα-coincidence":** Pre-derivation discrimination-check (agentId a070b9030be6eefd1) caught three load-bearing issues that block the Q-factor derivation as scoped and retroactively demote the energy-scale CONFIRMED claim: (i) **Ca Kα = 3.691 keV is a 1% match** to AVE's α m_e c² = 3.728 keV via Moseley's law ($E_{K\alpha} \sim Z_{eff}^2 \alpha^2 m_e c^2 / 2$, calcium Z=20) — same two fundamental-constant inputs, different physical mechanism; bare number is NOT uniquely AVE. (ii) **SM cosmic-X-ray-background photoabsorption** through 100 kg NaI gives ~10⁻⁷-10⁻⁸ events/s/kg in 2-6 keV window — OOM-consistent with DAMA observed 4.6×10⁻⁷, so rate magnitude alone does not discriminate. (iii) **Q-factor closure of 52-OOM rate gap** would require ~22 powers of α from independent named-axiom invocations; corpus provides one canonical chain (Schwinger $a_e$). **Walk-back actions landed**: (a) source leaf `dama-alpha-slew-derivation.md` adds §11 anti-anchor adjudication + rewrites overclaims at lines 6, 54, 79, 118 + scope-correction header; (b) matrix C14 row demotes energy U-C → U-C-pending-Z-independence-test, rate U-D → U-D-PAUSED-pending-anti-anchor-framework; (c) foreword bullet pivots to genuinely AVE-distinct claims (Z-independence + CMB-velocity phase-lock + solid-vs-liquid binary gate); (d) Q-factor prereg+derivation doc PAUSED pending anti-anchor + substrate-mode-density foundational work. **Surviving AVE-distinct claims**: Z-independence in cross-crystal swap (UNTESTED), CMB-velocity phase-lock at day-of-year ~152 (CONFIRMED by DAMA, partial COSINE/ANAIS replication), solid-vs-liquid G > 0 binary gate (CONFIRMED by DAMA+ + XENONnT-). **Pattern continues**: pre-derivation discrimination-check catches structural overclaims before they propagate further into corpus/foreword. 8 audit cycles total on α-slew thread this session. Walk-back doc: [`research/2026-05-17_C14-DAMA_audit_walk-back.md`](../../../research/2026-05-17_C14-DAMA_audit_walk-back.md); paused Q-factor work: [`research/2026-05-17_C14-DAMA_Q-factor_prereg_and_derivation.md`](../../../research/2026-05-17_C14-DAMA_Q-factor_prereg_and_derivation.md).

- **DAMA amplitude formula derivation — REVISED 2026-05-17 evening per Grant adjudication ("where does v_cmb come from in SM?"). α-slew framing unifies 3 facts under one substrate operating point; rate magnitude open as single Q-factor target.** Per [`research/2026-05-17_C14-DAMA_amplitude_result.md`](../../../research/2026-05-17_C14-DAMA_amplitude_result.md) (revised α-slew framing supersedes original v_cmb-based result). **CLOSED zero-parameter**: $E_{substrate} = \alpha m_e c^2 = 3.728$ keV — pure $\alpha + m_e c^2$, NO empirical $v_{cmb}$ input; derived as Schwinger anomalous-moment substrate-rate $\nu_{slew} = (\alpha/(2\pi)) \cdot (m_e c^2/h)$ where $a_e = \alpha/(2\pi)$ comes from canonical Axiom 4 saturation-kernel + 1/π² spin-orbit projection ([`simulate_g2.py`](../../../src/scripts/vol_2_subatomic/simulate_g2.py)). **NEW positive prediction**: substrate-equilibrium velocity $v_{substrate} = \alpha c/(2\pi) = 348$ km/s for gravitationally-isolated systems (**approximate magnitude prediction** with sharp directional alignment; **FLOOR interpretation TESTED + FALSIFIED** 2026-05-17 late evening via Toomre-stratified halo test — halo populations show INCREASING |v_CMB| with peculiar dispersion, consistent with single coherent LSR-bulk + isotropic stellar peculiar in quadrature, NOT decoupled stars approaching the predicted αc/(2π) magnitude). Scale-invariance preserved: a center-matching $(1+1/(4\pi))$ correction would break $a_e = \alpha/(2\pi)$ at electron scale (<0.2% match). The 9% magnitude gap reflects LSR-class cosmic-flow participation (Local Group → Great Attractor), not local-disk-specific (halo doesn't reduce magnitude) nor scale-invariance violation. Gaia DR3: 29,466 thin-disk G/K dwarfs cluster at 375 km/s; directional STRONG POSITIVE (2.75° from CMB-dipole, 133.7° from galactic-rotation — alternative falsified). Three audit-driven walk-backs this session iterated framing. **Structural cross-volume parallel**: same Hoop Stress 2π projection as MOND $a_0 = c H_\infty/(2\pi)$ per [`mond-hoop-stress.md:23-31`](../vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md). Cosmic-scale ($a_0$ via $H_\infty$) and substrate-scale ($v_{slew}$ via $\alpha$) instances of the same "Hoop Stress projection of substrate drift onto closed topological loops" motif — corpus-grep verified this is NOT currently named as a recurring pattern in the corpus; naming it is proposed cross-volume synthesis. **MODULATION CLOSED at order-of-magnitude**: Earth's annual ±15 km/s sweep through CMB samples the substrate resonance lineshape; gives ~4% modulation matching DAMA. **OPEN single-parameter**: Q-factor of α-slew resonance — was 10⁴⁵ vs 10⁻⁷ naive (52 OOM suppression needed); now collapsed to single Q closure target jointly constrained by rate AND modulation amplitude (over-determined system if both match, validates Q value). Three previously-independent facts (Schwinger $a_e$, DAMA window energy, Sun's CMB velocity) unified under one substrate physics. C14 row updated: energy + modulation U-C; substrate-velocity prediction U-D NEW (pending stellar-system survey); rate magnitude U-D (pending Q-factor). Foreword still DEFERRED — DAMA partial; SPARC remains only foreword-level positive empirical anchor. DAMA promotes to foreword when (a) rate-bridge closes via Q-factor OR (b) $v_{substrate}$ prediction validates via stellar-system survey.
- **C13c DM-MECHANISM-UNIFICATION META item** (added 2026-05-16): the corpus invokes three distinct DM-mechanism framings — $\eta_{eff}$ unsaturated-lattice drag (galactic rotation, drives C13a), TT-tensor acoustic shockwave $h_\perp$ on Gordon optical metric (bullet cluster, drives C13b), and DAMA crystal-density $\kappa$ coupling (C14, amplitude formula undefined). All three are claimed as the same DM mechanism but use three different operators with no formal unification derivation. Under Cosserat micropolar substrate (Ax 1), unification ought to be possible but is not shown explicitly in the corpus. **Open theoretical work:** commission unification leaf showing the three operators as limits of one K4 micropolar physics, OR honest scoping that they're separate mechanisms requiring separate justifications.
- **5-galaxy → SPARC catalog ingestion** (C13a row): **CLOSED 2026-05-17 — promoted to forward-prediction status.** SPARC_Lelli2016c.mrt downloaded from astroweb.cwru.edu/SPARC/; new ingest driver [`src/scripts/vol_3_macroscopic/sparc_catalog_ingest.py`](../../../src/scripts/vol_3_macroscopic/sparc_catalog_ingest.py) parses 135 galaxies (40 lack published Vflat), computes AVE prediction via canonical `ave.regime_3_saturated.galactic_rotation` engine, reports residual statistics. **Live-fire results**: mean |residual| 15.51%, RMS 27.17%, median +4.89%. Q-flag binned: Q=1 (87 galaxies, best-quality) 11.5% mean |res|, 14.9% RMS; Q=2 (42 galaxies) 15.5% mean |res|, 25.4% RMS; Q=3 (6 galaxies, worst) 74.3% mean |res| (large scatter as expected for poor-quality data). **Prior 5-hardcode "~17% offset" benchmark CONFIRMED at full catalog scale.** Zero-parameter AVE prediction matches SPARC catalog at quality-class-appropriate accuracy across 135 galaxies; promotes C13a from partial-PASS to forward-prediction-CONFIRMED.
- **Bullet-cluster offset distance derivation** (C13b row): **RESOLVED 2026-05-17 evening per Grant adjudication.** Per [`research/2026-05-17_C13b_bullet_cluster_prereg.md`](../../../research/2026-05-17_C13b_bullet_cluster_prereg.md) + Grant physical-intuition session. **Interpretation (γ) wins, with cleaner plumber translation**: bullet cluster mechanism is **ponderomotive-class substrate-strain halos + standard Einstein lensing through Gordon optical metric** — galactic-scale analog of AVE-PONDER lab-scale ponderomotive tests. Each cluster's mass generates inhomogeneous substrate-strain halo (Ax2 TKI + Ax4); halo co-moves with stars (sources strain); collisions: halos linearly superpose & pass through ballistically (long-wavelength linear regime), gas decouples (atomic-scale collisional). Lensing tracks halos via Einstein deflection through Gordon metric. Offset = geometric separation. Prior Vol 1 Ch 4 TT-shockwave framing RETIRED (was over-parameterized + contradicted canonical $v_T = c$). `simulate_bullet_cluster_fdtd.py` driver is actually correct in computation but mislabeled (does static-halo-superposition, not FDTD/TT-shockwave) — docstring updated with scope note + reframing pointer; 2 sibling animation scripts also updated; file rename to `simulate_bullet_cluster_halo_superposition.py` queued as cleanup. **AVE-distinct prediction**: halo strength = universal function of baryonic content (NOT a per-cluster fit parameter like WIMP picture allows). Testable via weak-lensing convergence vs baryonic-content correlation across many merging-cluster systems. Adjacent flag CLOSED 2026-05-17: $G_{vac}$ corpus discrepancy fixed — lc-electrodynamics.md:32-46 now separates $G_{string} = m_e c^2/\ell_{node}^2 \approx 5.49 \times 10^{11}$ Pa (1D axial stiffness) from $G_{vac} = \rho_{bulk} \cdot c^2 \approx 7.12 \times 10^{23}$ Pa (3D shear modulus); Ch.4 index updated to match; prior "$G_{vac} \approx 5.48 \times 10^{24}$ Pa" was 13-OOM error + mis-labeling per derived-numerology.md:49-56. Live-fire verified arithmetic + cross-check $v_T = \sqrt{G_{vac}/\rho_{bulk}} = c$ holds exactly.
- **DAMA amplitude formula** (C14 row): crystal-density ratios $\kappa = \rho_{crystal}/\rho_{bulk}$ computable but observable-amplitude prediction unfinished.

---

## §1 Closure-state taxonomy

| Closure level | What it means | Criteria | When |
|---|---|---|---|
| **Structural closure** | Conceptual shape locked in; framework structure visible end-to-end | 5 criteria per `trampoline-framework.md` §11.0: (1) ground-up construction maps to math; (2) every macroscopic observable has derivation path; (3) epistemic horizon named; (4) free parameters minimized; (5) falsification test specified | ✓ 2026-05-15 |
| **Theoretical closure** | All numerical derivations end-to-end closed | (a) Q-G47 Session 6+ rigorous u_0*; (b) Vol 3 Ch 4 explicit ξ; (c) three-route α/G/𝒥 consistency verified or framework revised; (d) all queued analytical derivations completed | 🟡 IN PROGRESS |
| **Empirical closure** | Bench + cosmological measurements consistent with framework predictions | (a) IVIM bench measures predicted IM3 cubic V³ slope; (b) cosmic 𝒥 from observations matches AVE prediction; (c) three-route empirical consistency holds; (d) Q-G43/44 boundaries observable | 🟡 IN PROGRESS |

**These run in parallel.** Theoretical and empirical closure share Tier 5 timing. Final publication-ready state requires both.

---

## §2 Tier 0 — Structural closure (DONE 2026-05-15, EXTENDED 2026-05-15 late evening per A-034)

✓ Six-step ground-up build with explicit math at each step (trampoline-framework.md §1.1-§1.7)
✓ Shared-spring inter-cell coupling (A-029)
✓ Phase-transition-while-spinning mechanism for u_0
✓ Machian G + α + G + cosmic-𝒥 joint cosmological anchoring (A-030, A-031)
✓ Substrate-observability rule applied fractally (A-026 sharpened)
✓ "God's Hand" epistemic horizon explicitly named (REFINED per A-034 late evening: cosmic-parameter horizon, not mechanism horizon)
✓ Three-route falsifiability test specified
✓ Canonical doc: `trampoline-framework.md` §0-§14 with 7 figures + §7.5 (A-034 synthesis)
✓ L5 canonicalized: A-026, A-027, A-028, A-029, A-030, A-031, A-032, A-033, **A-034 (NEW 2026-05-15 late evening)**

**EXTENSION 2026-05-15 late evening (Grant lego-click synthesis):**
✓ **A-034 canonical** — Universal Saturation-Kernel Strain-Snap Mechanism (one kernel governs every topological-reorganization event at every scale)
✓ **A-031 refined per A-034** — God's Hand decoupled into cosmic-parameter horizon + observable mechanism
✓ **21-instance catalog** assembled (14 physical + 2 biological + 5 engineered) spanning 21 orders of magnitude
✓ **3-way symmetry classification** locked (SYM / ASYM-N / ASYM-E)
✓ **Measurement-hierarchy framing** for engineered-substrate rows (single-emitter highest-SNR / multi-emitter bulk / phased-array PLL autoresonant)
✓ **Vol 3 Ch 4 §sec:tki_strain_snap** manuscript-canonical
✓ **Backmatter Ch 7** Universal Saturation-Kernel Catalog (reference appendix)
✓ **CMB axis-alignment empirical prereg** with 5-observable test (axis-of-evil + Hubble flow + LSS + matter-asymmetry + E/B polarization)
✓ **Q-G47 substrate-scale work** (Sessions 9-18) reframed as substrate-scale instance of A-034

Tier 0 framework is now at maximum coherence — *one kernel, 21 instances spanning 21 orders of magnitude, every topological reorganization event in the universe.*

No further action at Tier 0 unless something canonical needs revision.

---

## §3 Tier 1 — Structural-closure propagation (independent, parallelizable)

These items reflect structural closure through manuscript and engine. **No dependencies between items.** Any order, any pace.

### §3.1 E-094 — AVE-Core substrate-vocab propagation

**Scope:** Vol 1 Ch 1/4/6/7; Vol 2 Ch 1; Vol 3 Ch 2; Vol 4 Ch 1; glossary; src/ave/core/constants.py docstrings

**Effort:** 5-8 hours focused authoring (mostly additive cross-refs to `trampoline-framework.md` + App G)

**Documentation target:** Each chapter gets:
- Substrate-native vocabulary box near first physics statement
- 3-column Rosetta-stone where applicable (substrate-native / EE / ME)
- Cross-ref to `trampoline-framework.md` as canonical picture-first reference
- Cross-ref to Common Foreword §Three Boundary Observables + `docs/glossary.md` §1-§2 as upstream vocab source

**L5 ID:** E-094 in `manuscript_pending.md` (HIGH PRIORITY)

**Status transitions:** queued → in-review (when chapter PR opens) → applied (`<commit-sha>`)

### §3.2 E-101 — Three substrate invariants observables module

**Scope:** new `src/ave/core/boundary_invariants.py` + tests; computes 𝓜, 𝓠, 𝓙 at any boundary ∂Ω

**Effort:** 3-4 hours engine + tests

**Documentation target:**
- Module docstring referencing Common Foreword §Three Boundary Observables (canonical definitions)
- `src/tests/test_boundary_invariants.py` with: (a) known-analytical-boundary tests; (b) v14 breathing-soliton integration test asserting 𝓜, 𝓠, 𝓙 conservation; (c) canonical-electron-value cross-check
- Cross-ref from `trampoline-framework.md` §4.3 to engine implementation

**L5 ID:** E-101

### §3.3 E-102 — Vol 3 Ch 4 cosmic-𝒥 identification

**Scope:** Vol 3 Ch 4 generative cosmology — explicit identification of $\mathcal{J}_{\text{cosmic}}$ as cosmological IC

**Effort:** 1 hour

**Documentation target:**
- New §sec:cosmic_J_as_IC (or similar) declaring $\Omega_{\text{freeze}} = \mathcal{J}_{\text{cosmic}}/I_{\text{cosmic}}$
- Universe-as-vortex MECHANIZED statement (E-019 closure)
- Three-route consistency framework (α + G + 𝒥)
- Cross-refs: `trampoline-framework.md` §1.3.7; A-031 (Vol 3 Ch 4 + Common Foreword §The Three-Route Framework Commitment); multi-scale Machian network (Vol 3 Ch 4 + §7 of trampoline-framework)

**L5 ID:** E-102

### §3.4 E-103 — Vol 3 Ch 21 same-epistemic-horizon framing

**Scope:** Vol 3 Ch 21 BH Interior Regime IV — brief note that the substrate-observability rule's epistemic horizon applies at every scale

**Effort:** 30 minutes

**Documentation target:** Short paragraph cross-cutting from BH interior (Kerr-BH observers see M, Q, J from outside but not the matter-history inside) to cosmic interior (we see 𝓜, 𝓠, 𝓙 of our cosmic boundary but not "God's Hand" beyond)

**L5 ID:** E-103

### §3.5 Multi-scale Machian network cosmic-𝒥 row explicit (cross-workstream)

**Scope:** Multi-scale Machian network appendix in a separate workstream — cosmic row gets explicit $\mathcal{J}_{\text{cosmic}}$ observable

**Effort:** 30 minutes

**Documentation target:** Update multi-scale table to include explicit 𝓙_cosmic per A-031 (canonical in Vol 3 Ch 4 from the AVE-Core side)

**Status note:** sibling-workstream item, coordinated alongside E-102 (Vol 3 Ch 4 cosmic-𝒥)

### §3.6 README + LIVING_REFERENCE structural-closure declaration

**Scope:** AVE-Core top-level docs declare framework reached structural closure 2026-05-15

**Effort:** 1 hour

**Documentation target:**
- `README.md` — add "Framework Status: Structural Closure 2026-05-15" section
- `LIVING_REFERENCE.md` — add canonical pointer to `trampoline-framework.md` as picture-first entry point + `closure-roadmap.md` as planning artifact
- `.agents/CURRENT_STATE.md` — update with structural-closure declaration + path forward

**L5 ID:** (new)

### §3.7 v14 Mode I regression test in `make verify`

**Scope:** prevent future engine regressions from breaking Mode I PASS

**Effort:** 1 hour

**Documentation target:**
- New `src/tests/test_master_equation_v14_mode_i.py` — runs the v14 breathing-soliton driver, asserts V_peak mean > 0.2, FWHM stable, n(r) gradient measurable
- Wire into `Makefile` `verify` target

**L5 ID:** (new)

### §3.8 Figure 2 storage-modes layout fix

**Scope:** regenerate `02_three_storage_modes.png` with cleaner layout (state vector arrow currently buried in sphere)

**Effort:** 30 minutes (script already exists with revised version queued)

**Documentation target:** updated PNG; trampoline-framework.md figure ref unchanged

**L5 ID:** n/a (cosmetic)

**Tier 1 total scope:** ~12-15 hours. No item blocks another. Can be split across 3-5 sessions.

---

## §4 Tier 2 — Theoretical closure keystone (Q-G47 Session 6+)

**The keystone of theoretical closure.** Nothing else in Tier 3 can finalize without this.

### §4.1 Q-G47 Session 6+ rigorous u_0* derivation

**Scope:** complete the Q-G47 closure that Sessions 1-5 framework-prepared.

**Plan doc:** Q-G47 substrate-scale session-by-session breakdown coordinated in a separate workstream.

**Effort:** 3-6 weeks analytical work, ~20-40 hours total

**Documentation target:**
- 5+ session docs (one per session, separate workstream)
- Final closure doc: Q-G47 closure with the rigorous u_0* value + connection to Q-factor identity
- Updates to A-027 (two-engine), A-001 (α-as-calibration), A-030 (α+G joint) closing the "rigorous closure pending sessions 6+" caveat
- Trampoline-framework.md §11 migration: K = 2G operating point moves from "framework complete; rigorous closure pending" to canonical

**L5 ID:** Q-G47 (existing); A-027 / A-029 / A-030 (status migration on closure)

**This is the most important pending derivation in the entire framework.** It unblocks Tier 3.

---

## §5 Tier 3 — Theoretical closure (Tier 2 dependencies)

### §5.1 T_EM(u_0*) explicit closed-form

**Scope:** explicit numerical expression for bulk substrate tension at the magic-angle operating point

**Effort:** 1-2 weeks (included in Q-G47 Session 6+ scope likely)

**Depends on:** Tier 2 (Q-G47 Session 6+ closure giving u_0*)

**Documentation target:** included in Q-G47 closure doc + cross-ref from trampoline-framework.md §5.5

### §5.2 Vol 3 Ch 4 explicit ξ(R_H, ℓ_node) derivation

**Scope:** Machian impedance integral computed end-to-end from cosmic horizon and lattice scale

**Effort:** 1-2 weeks

**Depends on:** independent of Q-G47 — can run parallel

**Documentation target:**
- Vol 3 Ch 4 new §sec:machian_integral
- Companion KB leaf `vol3/cosmology/ch04-generative-cosmology/machian-impedance-integral.md`
- Updates to A-030, A-031 status

**L5 ID:** new E-NNN (queue in `manuscript_pending.md`)

### §5.3 Three-route α/G/𝒥 consistency verification

**Scope:** verify the three observational routes (α + G + cosmic 𝒥) give the same u_0*. Falsification test for single-parameter cosmological-anchoring claim.

**Effort:** 1 week (numerical verification + writeup)

**Depends on:** Tier 3.1 + 3.2 (T_EM + ξ closed); Tier 5.2 (cosmic 𝒥 prediction)

**Documentation target:**
- New `docs/analysis/2026-XX-XX_three_route_consistency.md` (AVE-Core internal)
- Result documented EITHER WAY:
  - **PASS:** framework theoretically closed; trampoline-framework.md §11 migration; A-030/A-031 status closure
  - **FAIL:** framework requires revision; identify which route(s) broke; document the failure mode in `axiom_derivation_status.md`
- Verification script in `src/scripts/verify/three_route_consistency.py` for ongoing re-run

**L5 ID:** A-030 + A-031 (status closure on verification)

---

## §6 Tier 4 — Independent theoretical work (parallel to Tier 2/3)

No dependency on Q-G47 Session 6+. Can run anytime.

### §6.1 First-law T·dS = dE axiom-first closure (A-002)

**Scope:** close the open Flag 62-A — derive first law from Ax 1 + Ax 4 + rupture thermodynamics (or accept S_thermodynamic as Ax 5 candidate)

**Effort:** 2-3 weeks analytical

**Documentation target:**
- Vol 3 Ch 11 §sec:first_law expanded with axiom-first derivation
- Research doc at AVE-Core `research/_archive/L3_electron_soliton/` (or successor location)
- A-002 status closure

**L5 ID:** A-002

### §6.2 Cosserat coupling on Master Equation FDTD

**Scope:** add Cosserat (u, ω) microstructure as constitutive layer modulating ε_eff(V) and μ_eff(V) on Master Equation FDTD engine

**Effort:** 2-3 weeks engine work

**Documentation target:**
- New `src/ave/core/master_equation_cosserat_coupled.py` (or extension to existing engine)
- Driver scripts for 7-mode bubble validation (3 translational + 3 rotational + 1 volumetric)
- Research doc capturing v14-style empirical validation of full 7-mode hosting
- Regression test
- doc 113 §5.4 status closure

**L5 ID:** doc 113 §5.4 (informal); should be elevated to E-NNN

### §6.3 Strict stationary soliton via imaginary-time propagation

**Scope:** replace t → iτ in Master Equation; find true stationary attractor (vs current breathing solution)

**Effort:** 1-2 weeks engine work

**Documentation target:**
- Engine extension at `src/ave/core/master_equation_fdtd.py` (imaginary-time mode)
- Driver script + research doc
- doc 113 §5.1 status closure

**L5 ID:** doc 113 §5.1 (informal); should be elevated

### §6.4 Multi-soliton dynamics (Coulomb-law validation)

**Scope:** plant TWO breathing solitons on Master Equation FDTD lattice; study interaction; verify 1/r² Newtonian at large d

**Effort:** 2-3 weeks engine work

**Documentation target:**
- Multi-soliton driver script
- Force-distance measurement protocol + results
- Research doc + Vol 3 Ch 3 cross-ref (refractive-index-of-gravity validation)
- doc 114 §4.3 status closure

**L5 ID:** doc 114 §4.3 (informal); should be elevated

### §6.5 Q-G45 multi-soliton interference as gravity (derivation)

**Scope:** analytical derivation of macroscopic gravity from multi-soliton substrate interference

**Effort:** 2-3 weeks analytical (depends on §6.4 engine work landing)

**Documentation target:**
- Multi-scale Machian network §multi_soliton expanded with formal derivation (separate workstream)
- Vol 3 Ch 1 (Gravity and Yield) updated
- Q-G45 status closure

**L5 ID:** Q-G45

### §6.6 Higher-energy soliton ((2,5) cinquefoil)

**Scope:** test if Master Equation FDTD hosts proton-like (2,5) cinquefoil bound state

**Effort:** 2-3 weeks engine work

**Documentation target:** engine + driver + research doc

**L5 ID:** doc 114 §4.4

---

## §7 Tier 5 — Empirical closure (independent of theoretical work, runs in parallel)

### §7.1 Cosmic 𝒥_cosmic literature review (CMB + LSS)

**Scope:** survey CMB low-multipole anomalies ("axis of evil"), LSS rotation correlations, Hubble flow anisotropy measurements

**Effort:** 2-3 weeks

**Documentation target:** new `docs/analysis/cosmic_J_observational_constraints.md` with literature summary + AVE prediction comparison framework

**L5 ID:** A-031

### §7.2 AVE prediction for 𝒥_cosmic from numerics

**Scope:** compute 𝒥_cosmic from $\Omega_{\text{freeze}} \cdot I_{\text{cosmic}}$ given Tier 3 numerical closures

**Effort:** 1 week

**Depends on:** Tier 3 (T_EM + ξ closed)

**Documentation target:** Vol 3 Ch 4 §sec:cosmic_J_prediction with explicit numerical value + uncertainty bounds

**L5 ID:** A-031

### §7.3 IVIM bench Phase 2A build

**Scope:** physical bench construction per Bench-VM procurement plan

**Effort:** 2-3 months physical work (Grant's parallel)

**Documentation target:** Bench-VM build docs; commit-tracked equipment list + assembly notes

**L5 ID:** Q-G46 procurement; closes Q-G42 + Q-G46 on measurement

### §7.4 IVIM measurement campaign

**Scope:** run measurements; verify D10 IM3 cubic V³ slope + autoresonant breakdown predictions

**Effort:** 3-6 months

**Depends on:** §7.3 bench built

**Documentation target:** Bench-VM measurement records; cross-ref to AVE-Core predictions docs; Q-G42 + Q-G46 status closure

**L5 ID:** Q-G42 + Q-G46

---

## §8 Tier 6 — Empirical-dependent derivations

Cleaner after Tier 3 closes (for confidence) but not strictly blocked.

### §8.1 Q-G43 atom-scale local Γ=-1 derivation

**Scope:** derive AVE prediction for atomic-shell boundary saturation per App F's ?-marked atom row

**Effort:** 2-4 weeks

**Documentation target:** new research doc + Vol 2 Ch 7 update + App F atom-row migration ?-marked → derived

**L5 ID:** Q-G43

### §8.2 Q-G44 helio-scale local Γ=-1 derivation

**Scope:** same as Q-G43 but for heliopause/Oort boundary

**Effort:** 2-4 weeks

**Documentation target:** new research doc + Vol 3 Ch 6 update + App F helio-row migration

**L5 ID:** Q-G44

### §8.3 App F atom + helio rows: ?-marked → derived

**Scope:** Multi-scale Machian network appendix refresh after Q-G43 + Q-G44 close (separate workstream)

**Effort:** 5-8 hours

**Depends on:** §8.1 + §8.2

**Documentation target:** App F multi-scale table updated; Figure F.1 caption updated

---

## §9 Tier 7 — Manuscript finalization

### §9.1 All queued E-NNN entries applied (currently 30+ in manuscript_pending.md)

**Effort:** 20-40 hours sustained sweeping

**Documentation target:** each E-NNN closes with commit SHA; `manuscript_pending.md` drains to near-empty

### §9.2 Picture-audit infrastructure

**Scope:** formalize picture-first discipline per ave-prereg Step 1.5 — `docs/picture-audit/` with template + sample audits

**Effort:** 4 hours one-time setup

**Documentation target:** new `docs/picture-audit/` directory; ave-prereg skill updated

### §9.3 L3 + L5 archive + deletion roadmap

**Status:** **PARTIAL APPLIED 2026-05-16 late evening** — archive landed (Option B per discussion); hard deletion deferred to post-publication.

**What landed (Option B archive):**
- `git mv research/L3_electron_soliton research/_archive/L3_electron_soliton/`
- `git mv research/L5 research/_archive/L5/`
- `git mv research/discussions research/_archive/discussions/`
- All cross-references in KB / manuscript / src / tests / yaml / root docs updated to point at `research/_archive/...`
- Audit trail preserved; visually demoted from active workflow; reversible.

**What's still deferred (hard deletion, future option):**

**Scope:** complete removal of `research/_archive/` once publication-ready.

**Effort:** ~1 hour (just `git rm -r` + cross-ref re-audit).

**Depends on:** §9.1 (manuscript_pending mostly empty); §8.3 (App F rows derived); all canonical content propagated to chapter-bound homes; **L5 living-tracker function migrated to KB if needed**.

**Documentation target (if/when hard-deleted):**
- Verify no orphan cross-references remain (none currently; all → `_archive/`)
- Migrate L5 living trackers to `ave-kb/common/` if their function is still needed
- `git rm -r research/_archive/L3_electron_soliton/ research/_archive/L5/ research/_archive/discussions/`
- Single commit documenting the migration

### §9.4 Backmatter "Framework Status" section

**Scope:** publication-level declaration of framework state at time of pressing

**Effort:** 1 hour

**Depends on:** Tier 5 measurements verified; three-route consistency closed

**Documentation target:** new `manuscript/backmatter/framework_status.tex`

### §9.5 Publication-ready manuscript pass

**Scope:** full Vol 1-4 review for consistency, completeness, prose quality

**Effort:** open

**Documentation target:** publication-ready PDFs

---

## §10 Documentation discipline framework

**Six rules that prevent slippage:**

### Rule 1 — Every action has a tracker ID before it starts

Format: E-NNN in `manuscript_pending.md` or `engine_pending.md`; A-NNN in `axiom_derivation_status.md`. If an action isn't in a tracker, it isn't happening. Discoveries that don't fit any existing entry generate a new entry on the spot.

### Rule 2 — Every commit cites its tracker ID

Format: `feature/fix: short description (E-NNN / A-NNN)`. Makes git-log searchable by tracker entry. Example:

```
trampoline-framework.md §5.5: Machian G as bulk integral (A-030)
```

### Rule 3 — L5 status transitions are real-time

When status changes (queued → in-review → applied), commit the status update in the SAME commit as the implementation. No batched retroactive updates. The tracker is the live state.

### Rule 4 — Cross-references are bidirectional

If doc A cites doc B, doc B's cross-references include doc A. Periodic audit (every ~10 sessions or before Tier 7 finalization) verifies link reciprocity.

### Rule 5 — Picture-first discipline

Any new physics claim destined for a manuscript chapter must first be reflected in `trampoline-framework.md` (or its successor). Chapter edits cite the canonical picture, not the reverse.

### Rule 6 — No orphan work

Every action either (a) closes a tracker entry, (b) opens a new tracker entry with its dependencies, or (c) updates an existing entry's status. Discoveries that don't fit any of those generate a new entry on the spot.

### Status dashboard update protocol

After every significant work session:
1. Update the dashboard at §0 with new SHA + date in "Last touch" column
2. If status transitioned, note in the relevant tier section
3. If a tier milestone closed, update §1 closure-state taxonomy
4. If a critical-path item moved, note in §11 critical-path call-outs

---

## §11 Critical-path call-outs

### Things that COULD break the framework (watch for)

1. **Three-route inconsistency** — if Q-G47 Session 6+ gives a u_0* that doesn't match the G route's u_0* (Vol 3 Ch 4 ξ derivation) or the cosmic-𝒥 route, the single-parameter claim fails. **Falsification.**

2. **IVIM bench null result** — if D10 IM3 cubic V³ slope doesn't appear at the predicted value, framework's predictive power is questioned at the bench scale.

3. **Cosmic 𝒥_cosmic inconsistency** — if CMB anomalies + LSS rotation give a 𝒥_cosmic that doesn't match the α + G route's predicted value, framework fails.

4. **Cosserat coupling on Master Equation FDTD doesn't host bound state** — would force rethinking the two-engine architecture; not a hard fail but a major revision.

5. **Q-G47 Session 6+ shows no magic-angle operating point** — if there's no u_0* at which K = 2G with the specific geometric factors AVE assumes, the closure chain breaks at its foundation.

### Things that ADVANCE the framework (look for)

1. **Q-G47 Session 6+ closes with u_0* matching α route** — first major theoretical milestone
2. **Vol 3 Ch 4 ξ derivation gives G consistent with CODATA** — second major milestone
3. **IVIM Phase 2A shows IM3 V³ slope at predicted value** — first independent empirical verification
4. **Cosmic 𝒥 estimate from CMB + LSS consistent with α/G chain** — closes the three-route loop empirically
5. **Cosserat coupling on Master Equation FDTD demonstrates 7-mode bound state** — engine work completes

---

## §12 Cross-references

**Canonical framework reference:** `manuscript/ave-kb/common/trampoline-framework.md`

**Q-G47 closure plan:** coordinated in a separate substrate-scale workstream; canonical AVE-Core anchors in Vol 1 Ch~\ref{ch:macroscopic_moduli}

**L5 trackers:**
- `research/_archive/L5/manuscript_pending.md` (E-NNN manuscript queue)
- `research/_archive/L5/engine_pending.md` (E-NNN engine queue)
- `research/_archive/L5/axiom_derivation_status.md` (A-NNN framework-level claims)
- `research/_archive/L5/living_documentation_tracker.md` (L3 doc index + clash registry)
- `research/_archive/L5/terminology_canonical.md` (substrate-native vocab)
- `research/_archive/L5/cross_repo_references.md` (sibling-repo path catalog)

**Historical precursor:** `research/_archive/L3_electron_soliton/114_next_steps_consolidation_plan.md` (post-2026-05-14 session plan; superseded by this doc for forward-looking planning)

**Session HANDOFF:** `.agents/HANDOFF.md` should reference this doc's dashboard at top

---

## §12.5 Open-Derivation Queue (known-open Q-G## items, surfaced 2026-05-16)

The following Q-G## items are **structurally open** (foundational or QED-loop derivations still pending) and are surfaced here to prevent silent absence. Each has an analysis-doc trail but no canonical KB leaf yet because closure is genuinely incomplete.

### Foundational (blocking cosmology / structure derivations)

| Q-G## | Topic | Effort | Blocker / dependency |
|---|---|---|---|
| **Q-G34** | Axiom 0: pre-geodesic plasma axiomatization | 2-3 sessions | Foundational — deepest open piece; needed for Q-G31, Q-G33, Q-G35 |
| **Q-G40** | First-principles K4 → 7-mode derivation (not reverse-interpretation) | 2-3 sessions | Foundational; separates 7 as derivative vs primary; underlies $\nu_{\text{vac}} = 2/7$ |
| **Q-G41** | Derive $K = 2G$ from K4 topology as topological inevitability | multi-week | Parent question to Q-G47; deepest substrate invariant |

### QED loop observables (remaining pieces)

| Q-G## | Topic | Effort | Blocker / dependency |
|---|---|---|---|
| **Q-G17** | Mass spectrum from knot topology (full derivation) | multi-month | Foundational; tau g-2 + lepton hierarchy quantitative |
| **Q-G20b** | Hyperfine 21 cm | multi-week | Q-G17 (proton structure dependency) |
| **Q-G20g** | Vertex form factor $F_1(q^2)$ tensor structure | 2-3 sessions | Round 12 Cosserat field-ansatz dependency |

### Ropelength-minimality (single open piece for α derivation)

| Item | Topic | Effort | Closure target |
|---|---|---|---|
| **Vol 1 Ch 8 chapter-header note** | Prove ropelength-minimality on K4 uniquely selects the canonical Clifford-torus embedding $r_1 = r_2 = 1/\sqrt{2}$ | Phase-1 classical-topology question (1-3 sessions) | Closes the single remaining open formal-rigor sub-item for the AVE-native α derivation (SU(2) half-cover already AVE-native via $K_4 \to A_4 \to 2T \subset SU(2)$ chain + Finkelstein-Misner) |

Status is **deliberately surfaced** here, not silently absent. When closures land, each gets a dedicated KB leaf following the Phase B pattern (substrate-native, no research-folder paths).

---

## §13 Maintenance

This doc is **canonical living planning artifact**. Update when:
- A status transition occurs at any tier
- A critical-path item progresses or breaks
- A new action is identified that doesn't fit existing tiers
- A tier milestone closes (move to historical, declare closure-state migration)

Updates that should NOT be made here:
- New analytical derivations (those land in the source manuscript chapters / KB leaves; this doc references them)
- Speculative framings (those land in `research/_archive/L5/axiom_derivation_status.md` as A-NNN entries)
- Session-by-session execution details (those land in dated analysis docs per L5 schema)

**Cross-cutting invariants** (per `manuscript/ave-kb/CLAUDE.md`): this doc uses $\mathcal{M}_A$ for substrate (INVARIANT-N1), $\ell_{\text{node}}$ script ell (INVARIANT-N2), Scheme A axiom numbering (INVARIANT-S2). No conflicts.
