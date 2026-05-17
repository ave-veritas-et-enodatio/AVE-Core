[↑ Common Resources](index.md)
<!-- leaf: verbatim -->

# AVE Divergences from Standard Physics — Test Substrate Map

This leaf catalogues every AVE-distinct prediction that diverges from Standard Model + General Relativity + $\Lambda$CDM, mapped to the actual hardware, simulation, or data substrate where the test would run. Anchored to the foreword's "Epistemic Position" + "Falsifiable Standard" + "Three-Route Framework Commitment" sections ([`../../frontmatter/00_foreword.tex` lines 104-149](../../frontmatter/00_foreword.tex)).

**Two definitions of "test":** a test is either (a) a new experiment to be run on hardware, or (b) a re-analysis of existing public data. Both count as falsifiers. Each row below tags `Test type:` accordingly.

**Tier definitions:**
- **Tier A** — physical hardware exists (built or fab-ready ≤ $1k BOM)
- **Tier B** — simulation/analysis substrate exists in the workspace; physical hardware does not
- **Tier C** — Core-internal derivation only; no executable observer anywhere in the 9 AVE repos
- **Tier D** — structural-internal consistency wins (cross-scale unification); not field-falsifiable by single experiment

---

## Tier A — Hardware substrate exists

### A1. Chiral antenna resonance shift $\Delta f / f = \alpha \cdot pq / (p+q)$

- **AVE predicts:** torus-knot family $(2,3)/(2,5)/(3,5)/(3,7)/(3,11)$ each have distinct sub-percent resonance shifts on chiral antennas. Per-pair NEC2: $\Delta = -7.92$ / $-11.91$ / $-55.29$ MHz for k25 / k23 / k35.
- **Standard predicts:** no chirality-coupled shift; resonance set by geometric length alone.
- **Discriminator:** enantiomer-paired antenna measurement at **60-400$\times$ margin over noise floor**. A null result (no enantiomer-pair-differential shift) falsifies the torus-knot identification of particles.
- **Test type:** new experiment.
- **Substrate:** **HOPF-02a fab-ready, $123 BOM** at `AVE-HOPF/hardware/hopf_02a.kicad_pcb`. Predictions in `AVE-HOPF/docs/SESSION_STATE_2026-05-05.md:21`. HOPF-01 pilot built but confounded per `AVE-HOPF/.agents/HANDOFF.md:43` (varying $L_{wire}$, no enantiomer pair, single substrate).
- **KB anchors:** [`../vol4/falsification/ch12-falsifiable-predictions/index.md`](../vol4/falsification/ch12-falsifiable-predictions/index.md); foreword line 96 (electron $0_1$, proton $(2,5)$, $\Delta(1232)$ $(2,7)$ ladder).

### A2. Sagnac as fluid-dynamic impedance drag

- **AVE predicts:** $\Delta\phi \approx 2.07$ rad for a tungsten rotor, 10k RPM, 200m fiber loop; ratio $\Psi = \rho_W / \rho_{Al} \approx 7.15$ between rotor materials.
- **Standard predicts:** GR Lense-Thirring frame-drag is purely geometric and matter-density-independent — theoretical null $\sim 10^{-20}$ rad at this scale. SR Sagnac is $\Delta\Phi = 4A\Omega/(\lambda c)$ regardless of rotor mass.
- **Discriminator:** $\Psi \approx 1$ falsifies AVE; $\Psi \approx 7.15$ falsifies GR. There is no middle ground.
- **Test type:** new experiment.
- **Substrate:** **sub-$5k tabletop** spec'd at `AVE-PONDER/manuscript/vol_ponder/chapters/06_sagnac_rlve_protocol.tex:12`. No fab package yet; paper-stage. No hardware in workspace.
- **KB anchors:** [`../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md` lines 31, 50, 58](../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md); [`../vol4/falsification/ch12-falsifiable-predictions/active-sagnac-impedance-drag.md`](../vol4/falsification/ch12-falsifiable-predictions/active-sagnac-impedance-drag.md); foreword line 114.

---

## Tier B — Simulation substrate exists, no hardware

### B1. Tree-level vacuum nonlinearity (E² → E⁴ birefringence + vacuum-mirror APD spike)

- **AVE predicts:** $\Delta n_{eff} = 1 - \sqrt{1 - (E/E_{yield})^2}$ — Taylor expansion gives leading $E^4$ term. Vacuum-mirror reflection coefficient $\Gamma(V) = [(1-(V/V_{yield})^2)^{-1/4} - 1] / [(1-(V/V_{yield})^2)^{-1/4} + 1] \to 1$ as $V \to 43.65$ kV.
- **Standard predicts:** Euler-Heisenberg polynomial in $E^2$ (PVLAS limit $\sim 10^{-23}$); no APD-detectable back-scatter from DC vacuum.
- **Discriminator:** *"If the slope remains $E^2$, AVE is falsified."* APD back-scatter spike at 35-43 kV DC sweep on asymmetric-electrode vacuum-mirror geometry. Departure from QED at $\sim 10^{12}$ level per foreword line 106.
- **Test type:** new experiment.
- **Substrate:** no sibling-repo executable observer; bench specs in KB only. PVLAS-class or HV-DC infrastructure required.
- **KB anchors:** [`../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md` lines 8, 20](../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md); [`../vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md` lines 60, 83](../vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md).

### B2. Autoresonant sub-Schwinger pair creation

- **AVE predicts:** phase-locked-loop ring-up of vacuum strain produces measurable pair events at $E \ll E_S$ via Axiom-4 saturation kernel feedback.
- **QED predicts:** essentially zero rate below Schwinger field; rate $\propto \exp(-\pi E_S/E)$ smooth in $E$.
- **Discriminator:** sub-Schwinger pair-creation rate at autoresonant frequencies. ELI-class ($1-10M) facility required to reach the regime.
- **Test type:** new experiment.
- **Substrate:** structural derivation in KB. No sibling-repo observer; no compatible facility in workspace.
- **KB anchor:** [`../vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md` lines 46-58, 61](../vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md).

### B3. Pd/D fracture limit $x_{max} = \sqrt{2\alpha} \approx 0.929$

- **AVE predicts:** cold-fusion irreproducibility traces to Axiom-4 topological yield at $x_{max} = 0.929$ Pd-D ratio ($\Delta V / V_0 \approx 12.08\%$ volumetric strain). Borromean caging factor $\eta_B$ lifts it to $x = 1.858$.
- **Standard predicts:** no structural ceiling on Pd loading; cold-fusion irreproducibility framed as either statistical fluctuation or pseudoscience.
- **Discriminator:** measured Pd/D ratio at fracture across diverse cell geometries should cluster at $0.929$ (bare) or $1.858$ (Borromean). Single Pd/D > 1.858 observation falsifies.
- **Test type:** both — existing-data re-analysis of historical Pd-electrolysis runs; new experiment for cleaner ratio measurement.
- **Substrate:** **9 sim scripts in `AVE-Fusion/src/scripts/`** including `simulate_pd_fracture_limit.py`, `simulate_pd_borromean_absorber.py`, `simulate_pd_impedance_match.py`. Empirical anchor at `AVE-Fusion/.agents/handoffs/PALLADIUM_ANALYTICS_INITIATIVE.md:13-27`. No hardware.
- **KB anchors:** [`universal-saturation-kernel-catalog.md` line 31](universal-saturation-kernel-catalog.md); [`../vol3/condensed-matter/ch09-condensed-matter-superconductivity/critical-field-validation.md`](../vol3/condensed-matter/ch09-condensed-matter-superconductivity/critical-field-validation.md).

### B4. Protein folding regime classification by $Z_{topo}$

- **AVE predicts:** $\alpha$-helix / $\beta$-sheet / coil basin selection follows from per-residue $Z_{topo}$ spectral weight via Op14 cascade; zero-parameter (no Levinthal random search).
- **Standard predicts:** Anfinsen's thermodynamic hypothesis + Levinthal-paradox-resolved-by-funnel landscapes; requires force-field parameterization.
- **Discriminator:** AVE Z_topo prediction should match PDB ground truth fold class across a held-out cohort with RMSD below the force-field-baseline threshold without per-protein tuning.
- **Test type:** existing-data re-analysis.
- **Substrate:** **2 production folding engines in `AVE-Protein/src/ave_protein/engines/`**: `s11_fold_engine_v3_jax.py` (2,293 lines), `s11_fold_engine_v4_ymatrix.py` (1,325 lines). PDB ground truth in `AVE-Protein/pdbs/`. Validation scripts in `AVE-Protein/src/scripts/` (`s17_sub5_rmsd_benchmark.py`, `rmsd_benchmark.py`, etc.).
- **KB anchors:** [`../vol5/protein-folding-engine/index.md`](../vol5/protein-folding-engine/index.md); [`../vol5/protein-folding-engine/regime-classification.md`](../vol5/protein-folding-engine/regime-classification.md); [`../vol5/protein-folding-engine/z-topo-definition.md`](../vol5/protein-folding-engine/z-topo-definition.md).

---

## Tier C — Core-only, no executable substrate anywhere in workspace

These predictions live as derivations in the KB. None has an actual driver/observer script that would compute the discriminator against real data. Most are weekend Core-scripting tasks if the data is public (LIGO, EHT, Planck); some need facility-class infrastructure (RHIC/LHC, Fermilab g-2).

### C1. BH horizon $r_{sat} = 3.5 \cdot r_s$ and ringdown $\omega_R M_g = 18/49$

- **AVE predicts:** saturation-boundary horizon at $r_{sat} = 7GM/c^2 = 3.5 \cdot r_s$ (factor 7 from $\nu_{vac} = 2/7$ Poisson ratio). Area $196\pi G^2 M^2 / c^4$ — 12.25$\times$ standard. Ringdown $\omega_R M_g = 18/49 \approx 0.3673$.
- **Standard predicts:** $r_s = 2GM/c^2$ (Schwarzschild); $\omega_R M_g = 0.3737$ (Schwarzschild exact).
- **Discriminator:** 1.7% from GR; **10-18% from three existing LIGO events** per [`universal-saturation-kernel-catalog.md` line 40](universal-saturation-kernel-catalog.md). EHT photon-ring radius, ISCO frequency shift, BH-shadow-vs-horizon ratio in radio interferometry all discriminate $r_{sat}/r_s = 3.5$ from the standard value of 1.
- **Test type:** existing-data re-analysis (LIGO O1-O3 ringdown fits; EHT M87* + Sgr A* image data are public).
- **Substrate:** **MISSING.** No script in any repo loads LIGO strain data or EHT visibility data. Could be implemented as a new AVE-Core analysis driver.
- **KB anchor:** [`../vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md` lines 13, 17, 74-79](../vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md).

### C2. Entanglement decoherence threshold $T_{pair} = 2 m_e c^2 / k_B \approx 1.19 \times 10^{10}$ K

- **AVE predicts:** sharp decoherence onset at the pair-creation temperature; topologically-protected entanglement thread becomes vulnerable to spontaneous pair creation above this threshold.
- **Standard predicts:** *"Decoherence is governed by environmental coupling strength alone, with no intrinsic temperature threshold tied to $2 m_e c^2$"*.
- **Discriminator:** entanglement-correlation onset/offset traced across QGP temperature window in heavy-ion collisions (RHIC reaches $\sim 10^{12}$ K).
- **Test type:** existing-data re-analysis (RHIC/LHC heavy-ion datasets contain temperature-resolved correlation measurements); could also be a new dedicated experiment.
- **Substrate:** **MISSING.** K4-TLM lattice verification exists at $32^3$ for noise-coupling scenarios but no QGP-data driver.
- **KB anchor:** [`../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md` lines 53, 60, 62, 198-216](../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md).

### C3. Muon $\delta = -5\alpha/2$ and $\Delta(1232)$ $\delta = -7\alpha/2$ g-2 saliency at 50 ppm

- **AVE predicts:** family-wide saliency $\delta = -\alpha \cdot n_q / 2$ for $(2,q)$ torus-knot particles. Electron $(2,3)$ matches Petermann to 50 ppm ($C_2^{AVE} = -0.32846$ vs QED $-0.32848$).
- **QED predicts:** Petermann coefficients computed per-particle from 2-loop Feynman diagrams; no across-family geometric relation.
- **Discriminator:** *"if a $(2,q)$ particle's Petermann-like coefficient saliency $\neq -q\alpha/2$ at 50 ppm precision, the $n_q$-additivity assumption is falsified."*
- **Test type:** existing-data re-analysis (Fermilab Muon g-2 collaboration data already exists at sub-ppm precision; AVE prediction is a structural relation across the lepton/baryon family).
- **Substrate:** **MISSING.** No driver loads Fermilab g-2 data and compares to AVE's $-5\alpha/2$ prediction.
- **KB anchor:** [`../vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md` lines 80-83, 95-96, 103-109](../vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md).

### C4. Three-route framework commitment $\alpha + G + \mathcal{J}_{cosmic} \to$ single $u_0^*$

- **AVE predicts:** all three observational windows resolve to the same magic-angle operating point $u_0^*$ derived from one cosmological parameter $\Omega_{freeze}$. Route 1 (electromagnetic): CODATA $\alpha$ via Q-factor closure. Route 2 (gravitational): CODATA $G$ via Machian impedance integral $G = c^4 / (7\xi T_{EM}(u_0^*))$. Route 3 (cosmological): CMB / LSS measurement of $\mathcal{J}_{cosmic}$.
- **Standard predicts:** no relation between $\alpha$, $G$, and any cosmic-boundary quantity.
- **Discriminator:** *"All three routes must give the same operating point $u_0^*$, or the single-cosmological-parameter framework is falsified."* — foreword line 129.
- **Test type:** both — Route 1 + 2 are calculation (closed); Route 3 needs CMB / LSS axis-of-evil empirical anchor.
- **Substrate:** Route 1 closed (Path C FTG-EMT $p^* = 8\pi\alpha$ to 0.003%); Route 2 corpus-canonical via Vol 3 Ch 1; **Route 3 pending CMB-data re-analysis driver**. CMB axis-alignment prereg landed 2026-05-15 per [`closure-roadmap.md` line 35](closure-roadmap.md).
- **KB anchors:** [`closure-roadmap.md` lines 30, 38, 557](closure-roadmap.md); [`cosmic-parameter-horizon-a031-refinement.md` lines 60-64](cosmic-parameter-horizon-a031-refinement.md); foreword lines 121-129.

### C5. A-034 CMB axis-of-evil alignment at $(l = 174^\circ, b = -5^\circ)$

- **AVE predicts:** CMB axis should align with the Hubble-flow direction, large-scale-structure rotation axis, and matter-asymmetry direction — all four shared because all four trace back to the parent-BH spin axis frozen at cosmic lattice genesis.
- **Standard predicts:** $\Lambda$CDM has no mechanism for alignment; the CMB axis-of-evil anomaly is treated as a statistical fluke.
- **Discriminator:** angular separation between the four axes; AVE predicts $\lesssim$ degree-class agreement, standard cosmology has uniform prior.
- **Test type:** existing-data re-analysis (Planck CMB + SDSS galaxy survey are public).
- **Substrate:** **MISSING.** CMB axis-alignment prereg PRE-REGISTERED 2026-05-15 ([`closure-roadmap.md` line 35](closure-roadmap.md)); execution deferred. No driver loads Planck maps + SDSS catalog.
- **KB anchors:** [`universal-saturation-kernel-catalog.md` lines 86-92](universal-saturation-kernel-catalog.md); foreword line 149.

### C6. Neutrino parity kill-switch — no stable right-handed neutrino

- **AVE predicts:** the substrate is woven from right-handed helical flux channels; left-handed torsional input propagates preferentially. A stable right-handed sterile neutrino would falsify the chiral LC bandgap that derives weak-force parity violation.
- **Standard predicts:** SM allows $\nu_R$; sterile-neutrino searches are open.
- **Discriminator:** observation of a stable, freely propagating right-handed neutrino.
- **Test type:** existing-data re-analysis (MiniBooNE, MicroBooNE, future searches).
- **Substrate:** **MISSING.** No driver loads neutrino-oscillation data.
- **KB anchor:** [`../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md` line 8](../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md).

### C7. GRB Trans-Planckian dispersion kill-switch — no photon mass / lattice dispersion

- **AVE predicts:** photons are purely transverse massless topological link-variables, immune to spatial inertia. No energy-dependent arrival time delay at Trans-Planckian energies.
- **Standard predicts:** several QG approaches (DSR, LQG phenomenology) predict small Lorentz-invariance violation at Planck scale.
- **Discriminator:** *"If future ultra-high-energy Trans-Planckian observations (e.g., extreme Gamma Ray Bursts) definitively show a strict energy-dependent arrival time delay (lattice dispersion), the macroscopic mathematical topological decoupling theorem is physically falsified."*
- **Test type:** existing-data re-analysis (Fermi-LAT, CTA, IceCube TeV-PeV neutrinos).
- **Substrate:** **MISSING.**
- **KB anchor:** [`../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md` line 9](../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md).

### C8. Torus-knot baryon ladder forward predictions

- **AVE predicts:** $(2,17)$ at $\sim 2742$ MeV; $(2,19)$ at $\sim 2983$ MeV; $(2,21)$ at $\sim 3199$ MeV — uniform $\sim 170$ MeV spacing on the $(2,q)$ ladder.
- **Standard predicts:** lattice QCD computes baryon spectrum per state; no geometric ladder structure imposed.
- **Discriminator:** observation of baryons at the predicted masses, with the predicted family relations.
- **Test type:** new experiment (CLAS12 / PANDA / future hadron facilities).
- **Substrate:** structural prediction in KB; 6 retrospective matches against existing PDG already documented.
- **KB anchors:** [`../vol4/falsification/ch12-falsifiable-predictions/index.md` line 14](../vol4/falsification/ch12-falsifiable-predictions/index.md); [`../vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md`](../vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md).

### C9. Metric levitation hard ceiling $m_{max} = 1.846$ g

- **AVE predicts:** electrostatic levitation has a fundamental ceiling at $m_{max} = V_{yield} \cdot \xi_{topo} / g = 1.846$ g — beyond this, V_yield gates dielectric snap and the geometry collapses.
- **Standard predicts:** no fundamental upper limit on electrostatic levitation; only practical limits from voltage breakdown of the surrounding medium.
- **Discriminator:** demonstration of stable electrostatic levitation of a mass exceeding 1.846 g in vacuum.
- **Test type:** new experiment.
- **Substrate:** **MISSING.** Bench design specs in KB only.
- **KB anchor:** [`../vol4/falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md`](../vol4/falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md).

### C10. Muon lifetime invariant to surrounding-medium $\varepsilon_r$

- **AVE predicts:** muon decay rate is set by the standing-wave $V > V_{yield}$ threshold at the muon's own LC cavity geometry; bulk dielectric of the surrounding medium cannot alter this sub-femtometer M_A yield limit.
- **Standard predicts:** electromagnetic environment can in principle modify decay rates through medium-dependent corrections (small but nonzero).
- **Discriminator:** measure muon lifetime in extreme-$\varepsilon_r$ media (e.g., high-pressure dielectric gas, condensed-matter substrates). AVE: invariant. Standard: small correction expected.
- **Test type:** new experiment.
- **Substrate:** **MISSING.** SPICE-modeled `leaky_cavity.cir` for the structural prediction; no comparison-to-data driver.
- **KB anchor:** [`../vol4/simulation/ch14-leaky-cavity-particle-decay/index.md` line 13](../vol4/simulation/ch14-leaky-cavity-particle-decay/index.md).

---

## Tier D — Structural-internal consistency wins (not field-falsifiable by single experiment)

These claims are load-bearing for the framework's philosophical position but won't be discriminated by an isolated experiment. They live or die by *cross-scale* consistency.

### D1. CHSH $|S|_{max} = 2\sqrt{2}$ and singlet $-\cos\theta_{ab}$ from K4 Möbius half-angle + Ohmic Born rule

- **AVE position:** Tsirelson bound recovered exactly from K4 chirality's Möbius half-angle coupling, binary outcomes at $\Gamma = -1$ saturation boundary, and Ohmic Born rule $P(\text{click}|x_n) = |\partial_t A(x_n)|^2 / \int |\partial_t A|^2 d^3 x$. Framework is nonlocal-deterministic-hidden-variable, with substrate nonlocality realized at the topological-thread level rather than via wavefunction collapse.
- **Not falsifiable by a single CHSH experiment** (matches QM by construction). Falsifiable by demonstrating any quantum-information protocol that AVE's deterministic substrate cannot reproduce.
- **KB anchors:** [`../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md` lines 122, 124, 143, 155](../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md); [`../vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md` line 25](../vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md); foreword line 97.

### D2. Cosmological constant $\rho_\Lambda = 9.03 \times 10^{-27}$ kg/m³ as latent heat of substrate crystallization

- **AVE position:** matches Planck-2018 within $\times 1.54$ (exact in de Sitter asymptote). Mechanism: latent heat of substrate crystallization, not vacuum zero-point energy.
- **QED position:** naive ZPE $\rho \sim 10^{96}$ kg/m³ — off by $10^{122}$.
- **The quantitative win is structural** (Friedmann translation from corpus-canonical $H_\infty$); the AVE-distinct mechanism (latent heat) needs independent $\rho_{latent}$ derivation + $\Gamma_{cryst}$ rate + Friedmann-vs-latent-heat consistency check — listed as open in [`../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md` lines 105-111](../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md).
- **KB anchor:** [`../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md` lines 7, 13, 51, 55, 95, 117-125](../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md); foreword line 106.

### D3. Geometric entropy $\hat{\mathcal{S}}_{geo} / S_{BH} \approx 2.8 \times 10^{-44}$ Machian dilution

- **AVE position:** AVE-native geometric entropy at the BH horizon (via A-B interface Op14 mechanism) is $\hat{\mathcal{S}}_{geo} = k_B \cdot A \log 2 / \ell_{node}^2$, a factor $\sim 2.8 \times 10^{-44}$ smaller than standard Bekenstein-Hawking.
- **Discriminator:** *"Any observational test sensitive to the AVE-native geometric entropy (as opposed to thermodynamic $S_{BH}$) would distinguish. Specifically: Hawking radiation modes that depend on the interface structure."* Not a current-instrument test.
- **KB anchor:** [`../vol3/condensed-matter/ch11-thermodynamics/four-entropy-distinction.md` lines 13, 17, 62, 74, 122, 128-132](../vol3/condensed-matter/ch11-thermodynamics/four-entropy-distinction.md); foreword line 116.

### D4. A-034 universal saturation kernel — 21 instances across 21 OOM

- **AVE position:** one kernel $S(A) = \sqrt{1 - A^2}$ governs every topological-reorganization event at every scale. Empirical anchors: BCS $B_c(T)$ at **0.00% error**, BH ringdown 1.7% from GR exact, NOAA 40-yr solar flare statistics validated, Schwarzschild radius exact, Pd hydrogen 12.08%, water LLCP per Nilsson 2026.
- **The cross-scale consistency IS the falsifier.** Any single canonical instance failing at >1% (where the prediction is sharp) would falsify the universality claim. So far none has.
- **KB anchor:** [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md); foreword line 149.

---

## Soft cross-repo contradiction worth knowing

Per `AVE-HOPF/AGENTS.md` line 82 (sibling-repo authority): the AVE-Propulsion $k(p,q) = 0.15 \to 0.95$ figure is *"confirmed aspirational caption-only figure"* — closed Q3 on 2026-05-06. If AVE-Core ever cites this number as a derived prediction, the citation is stale. Current scan (2026-05-16) found no such citation; flagged for future authors.

---

## Two gaps surfaced by this map

1. **No executable observer for any Tier C headline prediction.** $r_{sat}$, $\omega_R M_g$, vacuum birefringence, $T_{pair}$, muon $\delta$, $\Delta$ $\delta$ — all live as derivations in the KB with no script anywhere in the 9 repos that would compute the discriminator against real data. The closest existing infrastructure is AVE-HOPF's `verify_local_universe.py` AST anti-cheat scanner (which guards against smuggled constants but doesn't run predictions against observation). **If Tier C is to advance, it's primarily a Core-side scripting workstream, not a sibling-repo task.**

2. **Three-route framework commitment is the framework's sharpest empirical commitment** (foreword line 121-129), but its Route 3 ($\mathcal{J}_{cosmic}$) currently bottlenecks on the A-031 cosmic-parameter-horizon limit (see [`cosmic-parameter-horizon-a031-refinement.md`](cosmic-parameter-horizon-a031-refinement.md)). The KB acknowledges this. Routes 1 and 2 closing alone is not yet the full commitment — the framework's strongest claim awaits Route 3 substrate.

---

## Priority order for action (Grant-plumber perspective)

Ranked by *AVE-distinctness × accessibility × decisiveness*:

1. **HOPF-02a fab + measure** — already designed, ~$123, 60-400$\times$ predicted SNR margin. Single decisive shot at the chiral antenna shift law. Order package at `AVE-HOPF/hardware/hopf_02a.kicad_pcb`.
2. **Sagnac-RLVE tabletop fab package** — sub-$5k spec exists in PONDER manuscript; two-rotor null (W vs Al) gives 7.15$\times$ contrast that's unambiguous. Needs the fab package elevated from paper-stage to BOM.
3. **LIGO ringdown re-analysis driver** — no hardware, all public data, 10-18% predicted miss on three existing events. KB framing exists at [`universal-saturation-kernel-catalog.md` line 40](universal-saturation-kernel-catalog.md); the executable observer is the missing piece.
4. **CMB axis-alignment driver** — prereg already landed 2026-05-15; execution deferred. Pure public-data analysis (Planck + SDSS).
5. **Muon g-2 family-saliency comparison driver** — Fermilab Muon g-2 collaboration data is public; AVE's $\delta = -5\alpha/2$ prediction is a single-number comparison.

The rest (Schwinger autoresonance, vacuum birefringence at $10^{12}$, BH photon-ring, baryon-ladder forward predictions) need facility-class infrastructure outside the current workspace.

---

> → Primary: [Closure Roadmap](closure-roadmap.md) — Q-G47 + A-027 + A-031 + A-034 status tracking that this map cross-references for "open" / "closed" / "pending" classifications
> → Primary: [Universal Saturation-Kernel Catalog (A-034)](universal-saturation-kernel-catalog.md) — the 21-instance cross-scale catalogue that underlies Tier D and several Tier C predictions
> → Primary: [Common Foreword](../../frontmatter/00_foreword.tex) — canonical narrative source for the "Epistemic Position" + "Falsifiable Standard" + "Three-Route Framework Commitment" framings
> ↗ See also: [A-031 Refined: Cosmic-Parameter Horizon](cosmic-parameter-horizon-a031-refinement.md) — Route 3 ($\mathcal{J}_{cosmic}$) bottleneck and the observable-mechanism vs cosmic-parameter distinction
> ↗ See also: [Measurement Hierarchy SNR](../vol4/falsification/ch11-experimental-bench/measurement-hierarchy-snr.md) — bench-class SNR framing for the Tier A and Tier B substrate
> ↗ See also: [Three Boundary Observables: $\mathcal{M}$, $\mathcal{Q}$, $\mathcal{J}$](boundary-observables-m-q-j.md) — substrate-observability rule that frames "what is measurable" at any saturation surface
