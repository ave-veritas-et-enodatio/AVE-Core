[↑ Common Resources](index.md)
<!-- leaf: verbatim -->

# AVE Divergences from Standard Physics — Test Substrate Map

> **Related KB layers:** This leaf is the *operational tracking layer* over the canonical narrative catalog at [`appendix-experiments.md`](appendix-experiments.md) (PATH-STABLE, referenced from vol1-5,7,8 as `app:unified_experiments`) and the per-project bench-design leaves at [`../vol4/falsification/ch11-experimental-bench-falsification/`](../vol4/falsification/ch11-experimental-bench-falsification/index.md). Read the catalog for narrative descriptions organized by Volume; read the per-project leaves for bench specs + BOMs; read this map for falsification logic, lifecycle status, axiom-impact severity, and sibling-repo substrate.

This leaf catalogues every AVE-distinct prediction that diverges from Standard Model + General Relativity + $\Lambda$CDM, mapped to the actual hardware, simulation, or data substrate where the test would run. Anchored to the foreword's "Epistemic Position" + "Falsifiable Standard" + "Three-Route Framework Commitment" sections ([`../../frontmatter/00_foreword.tex` lines 104-149](../../frontmatter/00_foreword.tex)).

**Two definitions of "test":** a test is either (a) a new experiment to be run on hardware, or (b) a re-analysis of existing public data. Both count as falsifiers. Each row below tags `Test type:` accordingly.

**Tier definitions:**
- **Tier A** — physical hardware exists (built or fab-ready ≤ $1k BOM)
- **Tier B** — simulation/analysis substrate exists in the workspace; physical hardware does not
- **Tier C** — Core-internal derivation only; no executable observer anywhere in the 9 AVE repos
- **Tier D** — structural-internal consistency wins (cross-scale unification); not field-falsifiable by single experiment

---

## Tier A — Hardware substrate exists

### A1. Chiral antenna resonance shift $\Delta f / f = \alpha \cdot pq / (p+q)$ (Project HOPF-02 / Topological Refraction Snell Parallax)

- **AVE predicts:** torus-knot family $(2,3)/(2,5)/(3,5)/(3,7)/(3,11)$ each have distinct sub-percent resonance shifts on chiral antennas. Per-pair NEC2: $\Delta = -7.92$ / $-11.91$ / $-55.29$ MHz for k25 / k23 / k35.
- **Standard predicts:** no chirality-coupled shift; resonance set by geometric length alone.
- **Discriminator:** enantiomer-paired antenna measurement at **60-400$\times$ margin over noise floor**. A null result (no enantiomer-pair-differential shift) falsifies the torus-knot identification of particles.
- **Test type:** new experiment.
- **Substrate:** **HOPF-02a fab-ready, $123 BOM** at `AVE-HOPF/hardware/hopf_02a.kicad_pcb`. Predictions in `AVE-HOPF/docs/SESSION_STATE_2026-05-05.md:21`. HOPF-01 pilot built but confounded per `AVE-HOPF/.agents/HANDOFF.md:43` (varying $L_{wire}$, no enantiomer pair, single substrate).
- **KB anchors:** [`../vol4/falsification/ch12-falsifiable-predictions/index.md`](../vol4/falsification/ch12-falsifiable-predictions/index.md); foreword line 96 (electron $0_1$, proton $(2,5)$, $\Delta(1232)$ $(2,7)$ ladder).

### A2. Sagnac as fluid-dynamic impedance drag (Project ROENTGEN-03 / Sagnac-RLVE)

- **AVE predicts:** $\Delta\phi \approx 2.07$ rad for a tungsten rotor, 10k RPM, 200m fiber loop; ratio $\Psi = \rho_W / \rho_{Al} \approx 7.15$ between rotor materials.
- **Standard predicts:** GR Lense-Thirring frame-drag is purely geometric and matter-density-independent — theoretical null $\sim 10^{-20}$ rad at this scale. SR Sagnac is $\Delta\Phi = 4A\Omega/(\lambda c)$ regardless of rotor mass.
- **Discriminator:** $\Psi \approx 1$ falsifies AVE; $\Psi \approx 7.15$ falsifies GR. There is no middle ground.
- **Test type:** new experiment.
- **Substrate:** **sub-$5k tabletop** spec'd at `AVE-PONDER/manuscript/vol_ponder/chapters/06_sagnac_rlve_protocol.tex:12`. No fab package yet; paper-stage. No hardware in workspace.
- **KB anchors:** [`../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md` lines 31, 50, 58](../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md); [`../vol4/falsification/ch12-falsifiable-predictions/active-sagnac-impedance-drag.md`](../vol4/falsification/ch12-falsifiable-predictions/active-sagnac-impedance-drag.md); foreword line 114.

---

## Tier B — Simulation substrate exists, no hardware

### B1. Tree-level vacuum nonlinearity (E² → E⁴ birefringence + vacuum-mirror APD spike) (Project ZENER-04 / Impedance Avalanche Detector)

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

### B5. Project PONDER-01 — stereo phased array parallax (35 kV asymmetric thrust wake)

- **AVE predicts:** asymmetric FR4/Air dielectric stack at 100 MHz / 30 kV traps acoustic energy via impedance mismatch; reflection coefficient $\Gamma \approx -0.349$ at every air/FR4 interface generates **~40.1 μN unidirectional ponderomotive thrust** (10,000 tips, vol4 ch2 index:15).
- **Standard predicts:** Maxwell-equation null — no net thrust from symmetric vacuum.
- **Discriminator:** torsion-balance measurement of the 40 μN time-averaged thrust; null result confirms Maxwell.
- **Test type:** new experiment.
- **Substrate:** **CONFOUNDED — thermal catastrophe documented** (vol4 index *"PONDER-01 thermal catastrophe to PONDER-05 DC-biased quartz"*). SPICE netlist in [`../vol4/simulation/ch17-hardware-netlists/ponder-01-stack-netlist.md`](../vol4/simulation/ch17-hardware-netlists/ponder-01-stack-netlist.md); PONDER manuscript chapters 01-02; **no PCBA**. Superseded by PONDER-05.
- **KB anchors:** [`../vol4/simulation/ch17-hardware-netlists/ponder-01-stack-netlist.md`](../vol4/simulation/ch17-hardware-netlists/ponder-01-stack-netlist.md); appendix line 27.

### B6. Project PONDER-02 — bistatic plume diagnostics (10 GHz microwave reflection off $G_{vac}$ distortion)

- **AVE predicts:** a 10 GHz microwave probe across a PONDER-02 Sapphire GRIN nozzle plume measures phase shift $\Delta\phi$ from $c_{eff} = c_0 \sqrt{S(A)}$ velocity drop in the saturated plume; $\varepsilon_{eff}$ distortion maps directly. **TBD pin** $\Delta\phi$ magnitude — not yet in KB.
- **Standard predicts:** no phase shift from vacuum plume; only ion-density effects in residual gas.
- **Discriminator:** interferometric phase shift comparison vs vacuum baseline; null isolates ion-wind from saturation-kernel signature.
- **Test type:** new experiment.
- **Substrate:** `AVE-PONDER/src/scripts/ponder_02_bistatic_probe.py` simulator + PONDER ch.5 chapter; **no hardware**; **no dedicated KB leaf in `ave-kb/`** — canonical source is `AVE-PONDER/manuscript/vol_ponder/chapters/05_vacuum_torsion_metrology.tex:86-91`.
- **KB anchors:** appendix line 28; PONDER ch.5.

### B7. Project PONDER-05 — differential saturation parallax (paired DC-biased quartz, vertical gravity gradient)

- **AVE predicts:** 30 kV DC bias across quartz cylinder + 500 V AC perturbation at 50 kHz holds material at **68.7% of $V_{yield}$** = 43.65 kV; $\varepsilon_{eff}$ drops to 72.6%, $C_{eff}$ rises to 137.7%; predicted **~469 μN thrust** with paired-resonator vertical-gradient differential.
- **Standard predicts:** standard piezoelectric/electrostrictive response; no net thrust from saturated vacuum.
- **Discriminator:** measured $C_{eff}(V)$ rise + 469 μN thrust on torsion balance + vertical-gradient differential between paired resonators.
- **Test type:** new experiment.
- **Substrate:** PONDER manuscript ch.4 has full operating-regime spec; `AVE-PONDER/src/scripts/ponder_05_characterization.py`; **no PCBA**; **no dedicated `ave-kb/vol4/.../project-ponder-05.md` leaf** — canonical source is `AVE-PONDER/manuscript/vol_ponder/chapters/04_ponder_05_dc_biased_quartz.tex:1-30`.
- **KB anchors:** appendix line 29; [`../vol4/index.md` lines 5,12,23](../vol4/index.md).

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

### C11. Gravitational Parallax Interferometry — electron Mach-Zehnder for $n_s \neq n_t$ (35-rad phase shift)

- **AVE predicts:** electron matter-wave Mach-Zehnder across 1-m macroscopic vertical-vs-horizontal baseline experiences differential phase velocity from $n_s = (9/7)\varepsilon_{11}$ vs $n_t = (2/7)\varepsilon_{11}$ — strict violation of Lorentz parity. Predicted **35-rad topological phase shift**; ratio $n_s/n_t = 9/2$.
- **Standard predicts:** Lorentz-invariant null — no differential between spatial and temporal refractive indices.
- **Discriminator:** 35-rad phase shift on 1-m electron-interferometer baseline; null falsifies Ax3.
- **Test type:** new experiment.
- **Substrate:** **MISSING** — no electron-interferometer driver in workspace. Facility-class (1-m vacuum baseline + coherent electron source).
- **KB anchors:** [`../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md` lines 49-53](../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md); appendix line 13.

### C12. $g_* = 85.75$ effective DOF cutoff (vs Standard Model $g_{*,SM} = 106.75$)

- **AVE predicts:** $g_* = 7^3/4 = 343/4 = 85.75$ from $\nu_{vac} = 2/7$ Poisson ratio; 24 fewer fermionic DOF than SM (= 12 fewer Weyl spinors ≈ 0.8 generations). Primordial GW background **+7.6% stronger** (LISA, DECIGO); EW expansion rate **−10.4% slower** (CMB Stage-4); EW latent heat **−20% less** (FCC-ee/CEPC).
- **Standard predicts:** SM $g_{*,SM} = 106.75$ at EW scale.
- **Discriminator:** primordial GW $\Omega_{GW} \propto g_*^{-1/3}$; CMB Stage-4 EW expansion rate; FCC-ee EW latent heat.
- **Test type:** existing-data re-analysis (CMB Stage-4 sensitivity) + new-facility wait (LISA post-2035).
- **Substrate:** **MISSING** — no driver loads primordial-GW or CMB EW-phase data; **co-loads tightly with C1-BH-RING** (same $\nu_{vac} = 2/7$ source).
- **KB anchors:** [`../vol2/nuclear-field/ch10-open-problems/g-star-derivation.md` lines 14-16](../vol2/nuclear-field/ch10-open-problems/g-star-derivation.md); `g-star-prediction.md`.

### C13. VLBI Gravitational Impedance Parallax (Jupiter-grazing radio for dark-matter as $377\Omega$ stretching)

- **AVE predicts:** local "dark matter" field IS continuous phase-velocity gradient of $377\Omega$ vacuum impedance; VLBI tracking radio grazing Jupiter's core measures optical delay $\Delta t$ + Snell phase steering from achromatic impedance lens. **TBD pin $\Delta t$ magnitude** — leaf gives no numeric.
- **Standard predicts:** standard solar-system GR Shapiro delay only; dark matter is particulate.
- **Discriminator:** VLBI delay anomaly beyond Shapiro subtraction.
- **Test type:** existing-data re-analysis (VLBA / EVN Jupiter-occultation archives — TBD pin specific campaign).
- **Substrate:** **MISSING** — no VLBI-delay driver.
- **KB anchors:** [`../vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md` lines 24-28](../vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md); appendix line 18.

### C14. DAMA Parallax & Crystal Phonon Modulation (NaI vs Sapphire vs Germanium $\kappa_{crystal}$)

- **AVE predicts:** DAMA annual modulation arises from Earth flying through Milky Way LC impedance gradient; amplitude scales with crystal dielectric coupling $\kappa_{crystal}$. NaI ($\rho = 3.67 \times 10^3$ kg/m³), Sapphire ($3.98$), Germanium ($5.32$) should give predictably different amplitudes.
- **Standard predicts:** WIMP cross-section also varies by target, but with different scaling than $\kappa_{crystal}$.
- **Discriminator:** amplitude ratio across NaI / Sapphire / Ge matches $\kappa_{crystal}$ prediction (TBD pin explicit formula); annual-modulation **phase invariance** is shared with both AVE and WIMP.
- **Test type:** both — existing DAMA/LIBRA + COSINE-100 + ANAIS-112 data + future swapped-crystal runs.
- **Substrate:** **MISSING** — no driver compares DAMA modulation across crystals.
- **KB anchors:** [`../vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md` lines 30-34](../vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md); appendix line 19.

### C15. Project CLEAVE-01 — femto-Coulomb electrometer ($Q = \xi_{topo} \cdot x$)

- **AVE predicts:** mechanically pulling a gap by 1 μm induces topological charge $Q = \xi_{topo} \cdot x = (4.149 \times 10^{-7}\,\text{C/m}) \times 10^{-6}\,\text{m} = 0.415$ pC, producing **41.5 mV** on a 10 pF parasitic input. Single-number prediction from Ax2 TKI ($[Q] \equiv [L]$).
- **Standard predicts:** zero — electromagnetic theory predicts no charge from mechanical displacement of uncharged matter.
- **Discriminator:** ADA4530-1 electrometer reads 41.5 mV after 1 μm PZT step; 0.0 mV falsifies Ax2 directly.
- **Test type:** new experiment.
- **Substrate:** PCBA spec in KB leaf only ([`../vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md` lines 14-20](../vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md)); **no KiCad / no hardware in any repo**.
- **KB anchors:** above + appendix line 23.

### C16. Project TORSION-05 — horizontal metric rectification (asymmetric sawtooth thrust)

- **AVE predicts:** slow edge at +500 V (matched 377Ω line) → +0.207 mN forward thrust; fast edge at $-75$ kV ($> V_{yield}$ = 43.65 kV) → instant saturation, $\Gamma = -1$, 0.0 mN backward. Net **~100 μN time-averaged DC thrust** on torsion balance at $10^{-6}$ Torr.
- **Standard predicts:** symmetric Maxwell-stress null over full sawtooth period.
- **Discriminator:** asymmetric-V_yield rectified thrust on torsion balance; null falsifies Ax4 yield kernel.
- **Test type:** new experiment.
- **Substrate:** [`../vol4/falsification/ch11-experimental-bench-falsification/project-torsion-05.md` lines 8-13](../vol4/falsification/ch11-experimental-bench-falsification/project-torsion-05.md) has complete PCBA spec; **no fab**. Owner = PONDER (torsion-balance metrology is in their scope per `AVE-PONDER/manuscript/vol_ponder/chapters/05_vacuum_torsion_metrology.tex`).
- **KB anchors:** above + appendix line 26.

### C17. Protocol 11 — Sagnac-Parallax / Galactic Wind Vectoring (diurnal 24h drift)

- **AVE predicts:** static horizontal Sagnac fiber loop swept by Earth's rotation against 370 km/s Milky Way metric flow produces clean diurnal sinusoidal phase shift $\Delta\phi \propto v_{gal} \cdot \cos(\omega t)$. Per appendix line 32: **2,000,000-rad** drift.
- **Magnitude sanity-check (2026-05-16 in-leaf audit):** naive Fizeau-class arithmetic $\Delta\phi = 2\pi L v_{gal}/(\lambda c)$ at $\lambda = 1.55$ μm and $v_{gal} = 370$ km/s gives $\sim 2$ M-rad for $L \approx 0.4$ km fiber. **OOM-correct, not a typo.**
- **Standard predicts:** Lorentz-invariant null — no preferred frame, no diurnal modulation beyond Earth rotation's own Sagnac contribution.
- **TWO load-bearing issues with the prediction as stated:**
  - **(i) Existing null bounds contradict at ~10-15 OOM.** Brillet-Hall (1979) bounded aether-wind effects in optical cavities at $\Delta c/c < 5 \times 10^{-9}$; modern fiber-based tests (Wolf et al. 2003-2010) push to $\sim 10^{-17}$. A 2 M-rad diurnal modulation on Earth-bound static fiber would have been detected millions of times over by these bounds. **Either AVE is falsified by existing data, or Protocol 11's geometry doesn't actually map to what those bounds tested.**
  - **(ii) Internal inconsistency with [A2-SAGNAC](#a2-sagnac-as-fluid-dynamic-impedance-drag-project-roentgen-03--sagnac-rlve)'s entrainment picture.** A2-SAGNAC predicts $\Psi_{W/Al} = 7.15$ for a spinning W rotor — this implies the *local* LC IS rotor-entrained (rotor drags through entrained LC, density matters). Protocol 11 predicts 2 M-rad for a static fiber — this implies the local LC is NOT translation-entrained (static fiber sees the 370 km/s galactic wind unscreened). Both can't be true under a simple Earth-LC-entrainment model. **Either AVE has asymmetric entrainment (rotation entrains, translation doesn't — uncommon physics), or one of A2/C17 needs reframing.**
- **Discriminator:** diurnal phase drift on static horizontal Sagnac loop.
- **Test type:** new experiment (but **resolve A2/C17 entrainment inconsistency before fab**).
- **Substrate:** [`../vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md`](../vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md) is paper-stage one paragraph (no derivation); **no hardware, no driver**.
- **KB anchors:** above + appendix line 32. The leaf cites no derivation chain for the 2 M-rad; entrainment-vs-no-entrainment is not addressed.

### C18. Protocol 12 — GEO-Sync Impedance Differential (16.7 mm laser TOF stretch)

- **AVE predicts:** vertical laser link ground ↔ GEO satellite ($h = 35{,}786$ km) measures **~16.7 mm absolute TOF stretch** from non-linear AVE impedance integration $\int n(r)/c \, dr$ beyond pure-GR Shapiro delay.
- **Standard predicts:** pure-GR Shapiro delay only.
- **Discriminator:** sub-cm laser-ranging precision difference vs pure-GR baseline.
- **Test type:** existing-data re-analysis (ILRS / GRACE-FO archives — TBD pin specific dataset).
- **Substrate:** **MISSING** — no driver loads laser-ranging archives. Facility-class for new GEO link (ESA/NASA/SES partnership).
- **KB anchors:** [`../vol4/falsification/ch11-experimental-bench-falsification/geo-synchronous-impedance.md` lines 4-8](../vol4/falsification/ch11-experimental-bench-falsification/geo-synchronous-impedance.md); appendix line 33.

### C19. Molecular Chiral FRET Parallax (Ramachandran enforcement, currently unfalsifiable)

- **AVE predicts:** chiral LC metric bias mechanically enforces Ramachandran structural bounds (Ax2); gravity-relaxation shift $\Delta r / r = \alpha \cdot \varepsilon_{11} \approx 5 \times 10^{-12}$ at $5$ nm fluorophore baseline = **sub-attometer** (~$10^{-20}$ m) physical relaxation at terrestrial baselines.
- **Standard predicts:** thermodynamic-hypothesis Ramachandran bounds with no gravitational modulation.
- **Discriminator:** would require compact-object environment ($\varepsilon_{11} \sim 10^{-4}$) OR resonant amplification.
- **Test type:** new experiment (currently infeasible).
- **Substrate:** [`../vol5/molecular-foundations/biophysics-intro/chiral-fret-parallax.md` lines 6-12](../vol5/molecular-foundations/biophysics-intro/chiral-fret-parallax.md) — KB explicit: **"currently unfalsifiable"**. Tracked as future-target row.
- **KB anchors:** above + appendix line 37.

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

- **AVE position:** one kernel $S(A) = \sqrt{1 - A^2}$ governs every topological-reorganization event at every scale. Empirical anchors: BCS $B_c(T)$ at **0.00% error**, BH ringdown 1.7% from GR exact, NOAA 40-yr solar flare statistics validated, Schwarzschild radius exact, Pd hydrogen 12.08%, water LLCP per Nilsson 2026, **turbulence avalanche exponent $n_{3D} = 38/21 \approx 1.8095$ within 0.5% of empirical solar flare $\sim 1.8$** (per [`../vol3/condensed-matter/ch11-thermodynamics/kolmogorov-spectral-cutoff.md` lines 14-47](../vol3/condensed-matter/ch11-thermodynamics/kolmogorov-spectral-cutoff.md)). Vol VII Ch 11 turbulence/water-condensation phase-transitions framing (per appendix line 42) subsumes here: turbulence + water LLCP are A-034 cross-scale instances, not separate rows.
- **The cross-scale consistency IS the falsifier.** Any single canonical instance failing at >1% (where the prediction is sharp) would falsify the universality claim. So far none has.
- **KB anchor:** [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md); [`../vol3/condensed-matter/ch11-thermodynamics/kolmogorov-spectral-cutoff.md`](../vol3/condensed-matter/ch11-thermodynamics/kolmogorov-spectral-cutoff.md); [`../vol3/condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md`](../vol3/condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md); foreword line 149.

### D5. HTS / Meissner gear-train mechanism vs standard BCS magnetic pairing

- **AVE position:** Meissner exclusion derives from Cosserat phase-locked-gear-train rigidity (Ax1 micropolar rotational DOF); London penetration depth $B(x) = B_0 e^{-x/\lambda_L}$ from classical rotational inertia, not Cooper-pair condensate. BCS-equivalent predictions match (BCS $B_c(T)$ at 0.00% error per D4-A034), but the *mechanism* is AVE-distinct.
- **Discriminator: mechanism, not number.** AVE-distinct prediction is what *explains* SC, not a single discriminating measurement. **TBD pin** explicit HTS-vs-BCS discriminator numeric (vs the cross-scale corroborative position).
- **No Vol VII KB leaf exists** — supporting mechanism in [`../vol3/condensed-matter/ch09-condensed-matter-superconductivity/meissner-gear-train.md`](../vol3/condensed-matter/ch09-condensed-matter-superconductivity/meissner-gear-train.md); YBCO substrate spec in [`../vol4/falsification/ch11-experimental-bench-falsification/ybco-phased-array.md`](../vol4/falsification/ch11-experimental-bench-falsification/ybco-phased-array.md).
- **KB anchor:** above + appendix line 41.

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

## Tracking Matrices

Three matrices, all keyed by stable ID, organized for three distinct stakeholder reads:

- **Predictions matrix** — *theorist read:* "what does the framework claim and what would FAIL teach us?" Dataset-independent falsifiability logic.
- **Lifecycle matrix** — *project-manager read:* "where in the pipeline is each test?" At-a-glance dashboard of pre-reg / design / build / outcome / ownership.
- **Execution-details matrix** — *bench-engineer read:* "what do I need to actually run this test?" Substrate paths, comparison sources, confounders, next actions.

### Matrix legend (codes used across all three matrices)

- **Axioms** (per `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2): **Ax1** = K4 Cosserat substrate; **Ax2** = Topo-Kinematic Isomorphism ($[Q] \equiv [L]$); **Ax3** = Minimum Reflection Principle; **Ax4** = Dielectric Saturation kernel
- **Severity if FAIL:** **F** = framework-killing (axiom itself dies, no graceful revision); **M** = mechanism-killing (derivation chain dies, axioms survive with revised mechanism); **C** = chapter-killing (Vol-specific claim dies, mechanisms survive); **N** = no-single-shot-kill (Tier D corroborative — falsifiable only by cumulative inconsistency)
- **Discriminative power:** **U-D** = AVE-unique + decisive single-shot; **S-D** = shared with N competing theories but decisive among that set; **U-C** = AVE-unique but corroborative (cumulative consistency required); **S-C** = shared + corroborative
- **Pre-reg:** frozen / pending / none
- **Design:** complete / paper-stage / spec-only / n-a
- **Built/coded:** hw-built / hw+code / code-written / partial / no
- **Outcome:** PASS / FAIL / NULL / CONFOUNDED / partial / TBD
- **Discriminable now?:** **Y** = current measurement precision exceeds AVE-vs-standard delta; **N** = current precision insufficient; **TBD** = depends on facility access

### Matrix 1 — Predictions (what dies on FAIL)

| ID | Test | Tier/Type | Mechanism falsified | Axiom impact (severity) | Cascade & co-load (FAIL implications + NULL yield) | Discriminative power | Effect size / sharpness | KB anchor |
|---|---|---|---|---|---|---|---|---|
| A1-HOPF | Chiral antenna $\Delta f/f = \alpha \cdot pq/(p+q)$ | A / new-exp | $(2,q)$ torus-knot identification of particles via chiral resonance | Ax1+Ax2 (**M**) — Ax1 K4 lattice survives with revised knot ID; Ax2 TKI hardest hit | Cascade: C8 baryon ladder, C3 muon δ family, C10 muon lifetime all share $(2,q)$ classification. NULL = HOPF-02a inconclusive → HOPF-03 spatial-refraction variant. | U-D | $-7.92$ / $-11.91$ / $-55.29$ MHz across (2,5)/(2,3)/(3,5); **60-400× NEC2 SNR margin** | [`../vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md`](../vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md) |
| A2-SAGNAC | Sagnac as fluid-dynamic impedance drag | A / new-exp | Macroscopic Maxwellian regime as K4 LC network supporting density-dependent drag | Ax1 (**F**) — KB explicit: *"decisively and permanently falsified"* if $\Psi = 1$ | Cascade: all Vol III macroscopic refractive-index claims; C9 levitation. **C17-PROTOCOL-11 entrainment-inconsistency partner** (A2 assumes local LC rotor-entrained; C17 assumes static fiber sees unentrained galactic wind — both can't be true under simple entrainment model; needs adjudication). NULL = $\Psi$ between 1 and 7.15 falsifies both AVE and GR. | U-D | $\Delta\phi \approx 2.07$ rad at 10k RPM; $\Psi_{W/Al} = 7.15$ | [`../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md`](../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) |
| B1-VAC-BIREFRINGE | Vacuum birefringence $E^4$ + vacuum-mirror APD spike | B / new-exp | Saturation kernel Born-Infeld form $S(A) = \sqrt{1-A^2}$ at tree level | Ax4 (**F**) — Ax4 IS the saturation kernel; linear-$E^2$ persistence kills it entirely | Cascade: all A-034 instances (D4), C9 levitation V_yield, B3 Pd-fracture. NULL = standard $E^2$ rules → Ax4 falsified, entire framework re-foundation. | S-D | $E^4$ leading vs Euler-Heisenberg $E^2$; APD spike at $V \to 43.65$ kV | [`../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`](../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md) |
| B2-SCHWINGER | Autoresonant sub-Schwinger pair creation | B / new-exp | PLL ring-up of vacuum strain below $E_S$ via Ax4 kernel feedback | Ax4+Ax2 (**M**) — autoresonance mechanism dies; Ax4 saturation rate at $E_S$ itself survives | Cascade: C2 T_pair shares pair-creation machinery. NULL = "autoresonance doesn't work sub-Schwinger" leaves standard QED rate intact. | U-D | pair events at $E \ll E_S$; standard QED $\approx 0$ rate | [`../vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md`](../vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md) |
| B3-PD-FRACTURE | Pd/D fracture limit $x_{max} = \sqrt{2\alpha} \approx 0.929$ | B / both | Ax4 yield limit for hydrogen-loaded Pd | Ax4 (**C**) — one A-034 instance fails; framework survives if other 20 hold | Cascade: D4 catalog (one row weakens). Co-load: C9 V_yield, C5 cosmic snap share Ax4 ceiling structure. | S-D | $x_{max} = 0.929$ bare; 1.858 with Borromean caging | [`../vol3/condensed-matter/ch09-condensed-matter-superconductivity/critical-field-validation.md`](../vol3/condensed-matter/ch09-condensed-matter-superconductivity/critical-field-validation.md) |
| B4-PROTEIN | Protein folding regime by $Z_{topo}$ | B / existing-data | Op14 cross-sector spectral cascade selects fold basin from $Z_{topo}$ | Ax2 (**C**) — Vol V biological cascade dies; Ax2 TKI in particle-physics scope survives | Cascade: all Vol V protein-folding-engine leafs. NULL = "$Z_{topo}$ doesn't classify" forces Op14-cascade revision in biological domain. | S-C | Zero-parameter PDB fold class match without per-protein tuning | [`../vol5/protein-folding-engine/index.md`](../vol5/protein-folding-engine/index.md) |
| C1-BH-RING | BH horizon $r_{sat} = 3.5 r_s$ + ringdown $\omega_R M_g = 18/49$ | C / existing-data | Buchdahl-bound + $\nu_{vac} = 2/7$ Poisson ratio from K4 | Ax1+Ax4 (**M**) — Ax4 survives with revised $\nu_{vac}$; K4 lattice untouched | Cascade: D4 A-034 (BH ringdown is canonical row), D3 geometric entropy (uses horizon area). NULL = AVE $r_{sat}$ off → $\nu_{vac} = 2/7$ derivation revisited. | U-D for $\nu_{vac}$; S-D against modified-gravity ringdown theories | AVE 0.3673 vs GR 0.3737 (**1.7% from GR; 10-18% from 3 existing LIGO events**) | [`../vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md`](../vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md) |
| C2-T-PAIR | $T_{pair} = 2 m_e c^2 / k_B \approx 1.19 \times 10^{10}$ K decoherence threshold | C / both | Topological-thread protection at electron-LC-cavity binding energy | **Ax2 LOAD-BEARING (F)** — mass-as-flux-tube-binding IS Ax2's signature; FAIL hard to revise | Cascade: D1 CHSH derivation (thread topology is the nonlocal-deterministic mechanism), C10 muon lifetime (same LC-cavity logic). NULL = QGP temperature inference too noisy to discriminate → need cleaner experiment. | U-D | Sharp onset at $2 m_e c^2 / k_B$; standard QM has no intrinsic threshold | [`../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md`](../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md) |
| C3-MUON-DELTA | Muon $\delta = -5\alpha/2$ + $\Delta(1232)$ $\delta = -7\alpha/2$ g-2 saliency | C / existing-data | Family-wide $n_q$-additivity for Petermann saliency $\delta = -\alpha \cdot n_q / 2$ | Ax2+Ax3 (**C**) — $n_q$-additivity assumption fails; electron 50ppm match survives independently | Cascade: C8 baryon ladder, A1 chiral antenna (both depend on $(2,q)$ classification). NULL = $\delta$ off prediction at >50ppm → $n_q$-additivity revision (covered by ave-kb status: pending Q-G47 Sessions 19+). | U-D | 50 ppm precision required to discriminate | [`../vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md`](../vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) |
| C4-THREE-ROUTE | Three-route framework $\alpha + G + \mathcal{J}_{cosmic} \to$ single $u_0^*$ | C / both | Single cosmological IC parameter $\Omega_{freeze}$ generating $\alpha$, $G$, $\mathcal{J}_{cosmic}$ via $u_0^*$ | All four axioms (**F**) — *"single-cosmological-parameter framework is falsified"* (foreword line 129) | Cascade: every quantitative AVE prediction degrades. NULL = Routes diverge → framework retreats to multi-parameter EFT. | U-D | All three $u_0^*$ values agree within Routes' precision (CODATA $G$ ~4 decimals limits to ~0.01% sharpness) | [`closure-roadmap.md`](closure-roadmap.md); [`cosmic-parameter-horizon-a031-refinement.md`](cosmic-parameter-horizon-a031-refinement.md) |
| C5-CMB-AXIS | A-034 CMB axis-of-evil alignment $(l = 174°, b = -5°)$ | C / existing-data | Parent-BH spin axis frozen at cosmic lattice genesis | Ax1+Ax4 (**C**) — cosmic-scale A-034 instance fails; catalog survives if 20 other instances hold | Cascade: D4 A-034 (cosmic row dies), C4 three-route ($\mathcal{J}_{cosmic}$ route weakens). NULL = misalignment = $\Lambda$CDM-favored. | S-C | Degree-class agreement across four axes (CMB / Hubble flow / LSS rotation / matter asymmetry) vs uniform-prior null | [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md) (lines 86-92) |
| C6-NU-PARITY | Neutrino parity kill-switch — no stable right-handed $\nu_R$ | C / existing-data | Left-handed chiral LC bandgap forbids right-handed propagation | Ax1 (**F**) — KB explicit: *"permanently falsifies"* | Cascade: all weak-force-as-parity-violation chain. NULL = bandgap holds, AVE survives indefinitely. | S-D (SM also doesn't predict stable $\nu_R$; both surprised by detection but mechanisms differ) | Binary; detection of stable $\nu_R$ is single-shot kill | [`../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md`](../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md) |
| C7-GRB-DISPERSION | GRB Trans-Planckian dispersion kill-switch | C / existing-data | Photon as transverse topological link-variable immune to spatial inertia | Ax1 (**F**) — macroscopic topological decoupling theorem dies | Cascade: all Vol III refractive-index claims; Lorentz-invariance preservation. NULL = no dispersion = AVE survives. | S-D (strict-Lorentz theories also predict no dispersion; LQG/DSR predict dispersion) | Binary; energy-dependent arrival-time delay at Planck scale = kill | [`../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md`](../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md) |
| C8-BARYON-LADDER | Torus-knot baryon ladder $(2,17)$/$(2,19)$/$(2,21)$ forward predictions | C / both | $(2,q)$ ladder mass formula | Ax2 (**C**) — Vol II baryon ladder mechanism dies; Ax2 TKI survives if alternative ladder structure | Cascade: A1 chiral antenna shares $(2,q)$, C3 muon δ, C10 muon lifetime. Already partial-PASS: 6 retrospective PDG matches. | U-D | $\sim$170 MeV spacing; (2,17)$\sim$2742, (2,19)$\sim$2983, (2,21)$\sim$3199 MeV | [`../vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md`](../vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md) |
| C9-LEVITATION | Metric levitation ceiling $m_{max} = 1.846$ g | C / new-exp | V_yield gate at electrostatic levitation | Ax4+$\xi_{topo}$ (**C**) — V_yield calibration revised; Ax4 saturation survives | Cascade: B1 vacuum-mirror shares V_yield, D4 A-034 (V_yield is canonical anchor). NULL = exceeds 1.846 g = V_yield wrong. | U-D | $m_{max} = 1.846$ g exact | [`../vol4/falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md`](../vol4/falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md) |
| C10-MUON-LIFE | Muon lifetime invariant to surrounding $\varepsilon_r$ | C / new-exp | Muon LC cavity at sub-femtometer scale immune to bulk $\varepsilon_r$ | Ax2 (**C**) — Vol IV leaky-cavity decay model dies | Cascade: C8 baryon ladder (LC-cavity logic shared); leaky-cavity-particle-decay derivation chain. NULL = invariance confirmed = standard QED corrections smaller than measured. | U-D | Invariance vs small standard-QED medium correction | [`../vol4/simulation/ch14-leaky-cavity-particle-decay/index.md`](../vol4/simulation/ch14-leaky-cavity-particle-decay/index.md) |
| D1-CHSH | CHSH = $2\sqrt{2}$ from K4 Möbius half-angle + Ohmic Born | D / existing-data | Nonlocal-deterministic-hidden-variable interpretation via topological-thread substrate | All four axioms (**N**) — matches QM by construction; no single-shot kill | Cascade: C2 T_pair (thread topology). NULL = find QM protocol AVE deterministic substrate cannot reproduce. | U-C | Matches Tsirelson bound exactly | [`../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md`](../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md) |
| D2-RHO-LAMBDA | $\rho_\Lambda = 9.03 \times 10^{-27}$ kg/m³ as latent heat of substrate crystallization | D / existing-data | Latent heat of substrate crystallization mechanism (not vacuum ZPE) | Ax4 + Friedmann (**C**) — mechanism revision possible; quantitative match is structural | Cascade: D4 A-034 (cosmic crystallization is A-034 cosmic instance). NULL = $\rho_\Lambda$ off → $H_\infty$ or G derivation revisited. | U-C (mechanism) | $9.03 \times 10^{-27}$ vs Planck $5.85 \times 10^{-27}$ ($\times$1.54; exact in de Sitter asymptote) | [`../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md`](../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) |
| D3-GEOM-ENTROPY | Geometric entropy $\hat{\mathcal{S}}_{geo}/S_{BH} \approx 2.8 \times 10^{-44}$ | D / new-exp | A-B interface Op14 mechanism gives $\hat{\mathcal{S}}_{geo} = k_B A \log 2 / \ell_{node}^2$ | Ax1 (ℓ_node) + Ax4 (saturation horizon) (**C**) | Cascade: C1 BH horizon shares A-region machinery. NULL = no Hawking-radiation correlation measurement currently possible. | U-C | $2.8 \times 10^{-44}$ ratio to $S_{BH}$ | [`../vol3/condensed-matter/ch11-thermodynamics/four-entropy-distinction.md`](../vol3/condensed-matter/ch11-thermodynamics/four-entropy-distinction.md) |
| D4-A034 | A-034 universal saturation kernel catalog (21 instances) | D / both | Single kernel $S(A) = \sqrt{1-A^2}$ governs every topological-reorganization event | Ax4 (**F-cumulative**) — any single canonical instance failing at $>1\%$ where prediction is sharp kills universality claim | Cascade: all 21 catalog instances; one FAIL = catalog row dies. Subsumes turbulence avalanche $n_{3D}=38/21$ + water LLCP Nilsson 2026 (Vol VII Ch 11). NULL trivial; PASS corroborative. | U-C (universality claim AVE-unique; individual instances shared with domain models) | 21 instances over 21 OOM; BCS 0.00%, BH 1.7%, Schwarzschild exact, Pd 12.08%, water LLCP, turbulence 0.5% | [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md) |
| B5-PONDER-01 | Project PONDER-01 stereo phased array (35 kV asymmetric thrust) | B / new-exp | Asymmetric FR4/Air dielectric stack ponderomotive thrust via $\Gamma \approx -0.349$ interface | Ax3+Ax4 (**C**) — Vol IV ch.2 thrust chapter dies; Ax3/Ax4 survive with revised mechanism | Cascade: B6/B7 PONDER family, A2-SAGNAC. NULL = thermal catastrophe (already documented). | U-D vs Maxwell null | ~40.1 μN @ 30 kV / 100 MHz / 10,000 tips | [`../vol4/simulation/ch17-hardware-netlists/ponder-01-stack-netlist.md`](../vol4/simulation/ch17-hardware-netlists/ponder-01-stack-netlist.md) |
| B6-PONDER-02 | Project PONDER-02 bistatic plume diagnostics (10 GHz microwave reflection off $G_{vac}$) | B / new-exp | Microwave reflection off $G_{vac}$ distortion via $c_{eff} = c_0 \sqrt{S(A)}$ in saturated plume | Ax4+Ax1 (**C**) — Vol IV ch.6 vacuum-torsion-metrology mechanism dies; Ax4 globally survives | Cascade: B5/B7 PONDER, D4-A034 (plume = direct $S(A)$ probe). NULL = phase below interferometer floor → revert to torsion-only. | U-D ($c_{eff}$ reduction AVE-unique) | 10 GHz probe @ 25 kV / 2.45 GHz drive; **TBD pin $\Delta\phi$** | `AVE-PONDER/manuscript/vol_ponder/chapters/05_vacuum_torsion_metrology.tex:86-91` |
| B7-PONDER-05 | Project PONDER-05 differential saturation parallax (paired DC-biased quartz vertical gradient) | B / new-exp | 30 kV DC bias holds quartz at 68.7% $V_{yield}$; $\varepsilon_{eff}$ drops to 72.6%; $C_{eff}$ rises to 137.7% | Ax4 (**F**) — Ax4 IS saturation kernel; null at 68.7% V_yield falsifies directly | Cascade: B5/B6 PONDER, B1-VAC-BIREFRINGE, D4-A034, C9-LEVITATION (V_yield shared). NULL = no $C_{eff}$ rise → Ax4 fails → all A-034 instances under pressure. | U-D | 37.7% capacitance rise; ~469 μN thrust | `AVE-PONDER/manuscript/vol_ponder/chapters/04_ponder_05_dc_biased_quartz.tex` |
| C11-MACH-ZEHNDER | Gravitational Parallax Interferometry (electron Mach-Zehnder $n_s \neq n_t$) | C / new-exp | Spatial-vs-temporal refractive-index split ($n_s/n_t = 9/2$) violates Lorentz parity | Ax3+Ax1 (**F**) — Lorentz-parity violation that Ax3 mandates dies; no graceful revision | Cascade: C13-VLBI-DARK, C18-PROTOCOL-12 (all test $n_s \neq n_t$); D4-A034 ($\varepsilon_{11}$ shared). NULL = phase noise dominates → space-baseline interferometer. | U-D | 35-rad shift on 1-m macroscopic Mach-Zehnder | [`../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md` lines 49-53](../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md) |
| C12-G-STAR | $g_* = 85.75$ effective DOF cutoff vs SM 106.75 | C / existing-data | $g_* = 7^3/4 = 85.75$ from $\nu_{vac} = 2/7$; 24 fewer fermionic DOF than SM | Ax1 (**M**) — same $\nu_{vac}$ gate as C1-BH-RING; survives with revised Poisson ratio | Cascade: tight pair with C1-BH-RING; touches C5-CMB-AXIS, D2-RHO-LAMBDA. NULL = primordial GW inconclusive at LISA precision. | U-D | $\Omega_{GW}$ +7.6%; EW expansion -10.4%; EW latent heat -20% | [`../vol2/nuclear-field/ch10-open-problems/g-star-derivation.md` lines 14-16](../vol2/nuclear-field/ch10-open-problems/g-star-derivation.md) |
| C13-VLBI-DARK | VLBI Gravitational Impedance Parallax (Jupiter-grazing radio for $377\Omega$ DM stretching) | C / existing-data | Dark matter IS continuous geometric stretching of $377\Omega$ vacuum impedance baseline | Ax1+Ax4 (**M**) — macroscopic-gravity-as-impedance dies; particulate DM survives axioms | Cascade: tight pair with C14-DAMA; co-load with A2-SAGNAC, C18-PROTOCOL-12. NULL = VLBI noise dominates → particulate DM unaffected. | U-D | **TBD pin $\Delta t$ magnitude** (KB leaf gives no numeric) | [`../vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md` lines 24-28](../vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md) |
| C14-DAMA-MATERIAL | DAMA Parallax & Crystal Phonon Modulation (NaI vs Sapphire vs Ge $\kappa_{crystal}$) | C / both | DM wind modulates DAMA via bulk dielectric $\kappa_{crystal}$ coupling | Ax1+Ax4 (**C**) — Vol III dark-sector chapter dies; WIMP particulate resurrects | Cascade: tight pair with C13-VLBI-DARK; D4-A034 (Ax4 kernel). NULL = swapped-crystal amplitude scales with WIMP cross-section. | U-D | NaI / Sapphire / Ge densities cited; **no explicit amplitude formula — TBD pin** | [`../vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md` lines 30-34](../vol3/cosmology/ch05-dark-sector/multi-galaxy-validation.md) |
| C15-CLEAVE-01 | Project CLEAVE-01 femto-Coulomb electrometer ($Q = \xi_{topo} \cdot x$) | C / new-exp | Mechanical displacement induces topological charge per Ax2 TKI ($[Q] \equiv [L]$) | Ax2 (**F**) — KB explicit: "the framework is falsified" if 0.0 mV | Cascade: B4-PROTEIN ($\xi_{topo}$ shared), C9-LEVITATION ($m_{max} = V_{yield}\xi_{topo}/g$), C16-TORSION-05, B5-B7 PONDER (all use $\xi_{topo}$). NULL = parasitic leakage → enforce guard rings. | U-D | 41.5 mV per μm displacement on 10 pF input; 0.415 pC | [`../vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md` lines 14-20](../vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) |
| C16-TORSION-05 | Project TORSION-05 horizontal metric rectification (asymmetric sawtooth, $\Gamma=-1$ gate) | C / new-exp | Asymmetric V_yield gating at +500 V (matched) vs $-75$ kV (saturated $\Gamma = -1$) → DC thrust | Ax4+Ax3 (**F**) — KB explicit: "LC non-linear geometry of the universe is permanently falsified" if stationary | Cascade: B5/B6/B7 PONDER; shares V_yield with B1-VAC-BIREFRINGE, C9-LEVITATION, D4-A034. NULL = thermal/ion-wind artifacts dominate. | U-D | ~100 μN time-averaged DC thrust at $10^{-6}$ Torr | [`../vol4/falsification/ch11-experimental-bench-falsification/project-torsion-05.md` lines 8-13](../vol4/falsification/ch11-experimental-bench-falsification/project-torsion-05.md) |
| C17-PROTOCOL-11-SAGNAC-WIND | Protocol 11 — Galactic Wind Sagnac (diurnal 24h drift, 370 km/s Milky Way) | C / new-exp | Absolute rest-frame LC metric with 370 km/s flow produces diurnal Sagnac modulation on Earth-bound static fiber | Ax1+Ax3 (**F**) — preferred-frame claim dies; strict Lorentz survives if null. **PLUS internal inconsistency with A2-SAGNAC** (A2 requires local-LC entrainment for rotor drag to work; C17 requires NO local-LC entrainment for static fiber to see galactic wind — can't both be true under simple entrainment model) | Cascade: A2-SAGNAC (entrainment-inconsistency partner); C5-CMB-AXIS (370 km/s = CMB-dipole rest frame); C18-PROTOCOL-12. NULL = LC metric is Lorentz-invariant. | U-D vs strict Lorentz | **2,000,000-rad** drift (appendix) — verified naive-Fizeau OOM-correct for ~0.4 km fiber, **but contradicts Brillet-Hall + Wolf et al. static-Sagnac null bounds by ~10-15 OOM**; either AVE falsified by existing data OR entrainment unmodeled | [`../vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md` lines 4-8](../vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md) |
| C18-PROTOCOL-12-GEO-SYNC | Protocol 12 — GEO-Sync Impedance Differential (16.7 mm laser TOF stretch) | C / new-exp | Vertical $\int n(r)/c \, dr$ impedance integration stretches ground↔GEO TOF beyond Shapiro | Ax1+Ax3 (**F**) — "definitively breaking Lorentz symmetry in favor of structural waveguide electrodynamics" | Cascade: tight pair with C11-MACH-ZEHNDER, C13-VLBI-DARK; touches C4-THREE-ROUTE (Route 2 = G via Machian impedance integral). NULL = standard GR Shapiro holds. | U-D vs strict GR | **~16.7 mm** TOF stretch at $h = 35{,}786$ km | [`../vol4/falsification/ch11-experimental-bench-falsification/geo-synchronous-impedance.md` lines 4-8](../vol4/falsification/ch11-experimental-bench-falsification/geo-synchronous-impedance.md) |
| C19-FRET | Molecular Chiral FRET Parallax (Ramachandran enforcement, currently unfalsifiable) | C / new-exp | Chiral LC metric bias enforces Ramachandran bounds; gravity-relaxation $\Delta r/r = \alpha \cdot \varepsilon_{11}$ | Ax2 (**C**) — Vol V biophysics-intro chapter dies; Ax2 in particle scope survives | Cascade: B4-PROTEIN (Ax2 chiral bias shared); touches D1-CHSH. NULL = sub-attometer too small → unfalsifiable status quo. | U-C (corroborative only at terrestrial baselines) | $\Delta r/r \approx 5 \times 10^{-12}$; sub-attometer $\sim 10^{-20}$ m at 5 nm baseline | [`../vol5/molecular-foundations/biophysics-intro/chiral-fret-parallax.md` lines 6-12](../vol5/molecular-foundations/biophysics-intro/chiral-fret-parallax.md) |
| D5-HTS-MEISSNER | HTS / Meissner gear-train mechanism vs standard BCS magnetic pairing | D / both | Cosserat phase-locked-gear-train rigidity (Ax1 micropolar rotational DOF) underlies Meissner exclusion; London $B(x) = B_0 e^{-x/\lambda_L}$ from classical rotational inertia | Ax1+Ax4 (**N**) — structural mechanism claim; no single-shot kill since BCS-equivalent predictions match | Cascade: D4-A034 (BCS $B_c(T)$ at 0.00% is canonical row); B1-VAC-BIREFRINGE, B7-PONDER-05 (V_yield shared); B5-PONDER-01 YBCO substrate. NULL = standard BCS survives = gear-train interpretation falsified, BCS-equivalent predictions hold. | U-C (cross-scale mechanism; individual SC predictions shared with BCS) | London penetration depth + BCS $B_c(T)$ exact via gear-train; **no explicit HTS discriminator numeric — TBD pin** | [`../vol3/condensed-matter/ch09-condensed-matter-superconductivity/meissner-gear-train.md`](../vol3/condensed-matter/ch09-condensed-matter-superconductivity/meissner-gear-train.md) |

### Matrix 2 — Lifecycle (where in the pipeline)

| ID | Pre-reg | Design | Built/coded | Outcome | Tester |
|---|---|---|---|---|---|
| A1-HOPF | pending (HOPF-01 superseded post-confound) | complete | code-written (NEC2 predictions); hw-not-built | TBD | HOPF (Grant) |
| A2-SAGNAC | none | paper-stage (Vol Ponder Ch 6 protocol; no BOM) | no | TBD | open |
| B1-VAC-BIREFRINGE | none | spec-only | no | TBD | open |
| B2-SCHWINGER | none | spec-only | no | TBD | open |
| B3-PD-FRACTURE | none | spec-only | code-written (AVE-Fusion sim) | partial-PASS (sim consistent with empirical anchor) | Fusion |
| B4-PROTEIN | none | complete (PDB validation pipeline) | hw+code (engines + PDB ground truth) | partial validation pending RMSD benchmark closure | Protein |
| C1-BH-RING | none | spec-only (KB derivation; no driver design) | no | TBD | open |
| C2-T-PAIR | none | spec-only | partial (K4-TLM lattice sim only; no QGP driver) | TBD | open |
| C3-MUON-DELTA | none | spec-only | no | TBD | open |
| C4-THREE-ROUTE | partial (Routes 1+2 frozen; Route 3 prereg landed 2026-05-15) | spec-only | partial (Routes 1+2 closed; Route 3 driver missing) | partial-PASS (Routes 1+2 agree on $u_0^*$); Route 3 TBD | Core |
| C5-CMB-AXIS | **frozen 2026-05-15** | spec-only | no | TBD | Core (execution open) |
| C6-NU-PARITY | none | spec-only | no | TBD (null history accumulating) | open |
| C7-GRB-DISPERSION | none | spec-only | no | TBD (null history accumulating) | open |
| C8-BARYON-LADDER | none | spec-only | code-written (retrospective) | partial-PASS (6 PDG matches); forward predictions TBD | open |
| C9-LEVITATION | none | spec-only | no | TBD | open |
| C10-MUON-LIFE | none | spec-only | no | TBD | open |
| D1-CHSH | none | n-a (interpretation, not bench) | hw+code (K4-TLM lattice sim verifies) | PASS-by-construction (matches QM) | Core |
| D2-RHO-LAMBDA | none | n-a | code-written (Friedmann derivation) | PASS structural ($\times$1.54 of Planck); mechanism closure pending | Core |
| D3-GEOM-ENTROPY | none | n-a | code-written (derivation only) | derived-only (no measurement substrate) | Core |
| D4-A034 | none (catalog-level; individual instances may be pre-reg'd per row) | n-a (cross-scale claim) | partial (individual instances coded across repos) | partial-PASS (BCS 0.00%, NOAA solar flare ✓, Schwarzschild exact, BH ringdown 1.7%; turbulence 0.5%; remainder TBD) | Core (cross-repo) |
| B5-PONDER-01 | none | complete (SPICE netlist + PCBA stack spec) | no (per "thermal catastrophe" — superseded by PONDER-05) | CONFOUNDED (thermal) | PONDER |
| B6-PONDER-02 | none | paper-stage (described in PONDER ch.5; no PCBA spec) | code-written (`ponder_02_bistatic_probe.py` simulator) | TBD | PONDER |
| B7-PONDER-05 | none | complete (PONDER ch.4 full operating-regime spec) | code-written (`ponder_05_characterization.py`) | TBD | PONDER |
| C11-MACH-ZEHNDER | none | spec-only | no | TBD | open |
| C12-G-STAR | none | spec-only | no | TBD (LISA launch ~2035 for primordial GW) | open |
| C13-VLBI-DARK | none | spec-only | no | TBD | open |
| C14-DAMA-MATERIAL | none | spec-only | no | TBD (existing DAMA data + future swapped-crystal runs) | open |
| C15-CLEAVE-01 | none | complete (PCBA spec with ADA4530-1 + PZT in leaf) | no | TBD | open |
| C16-TORSION-05 | none | complete (HV flyback PCBA spec in leaf) | no | TBD | PONDER (scope match) |
| C17-PROTOCOL-11-SAGNAC-WIND | none | paper-stage (one-paragraph leaf; no BOM, no derivation) | no | **TBD-but-likely-FAIL** (2 M-rad contradicts Brillet-Hall + Wolf static-Sagnac null bounds by ~10-15 OOM; A2 entrainment inconsistency unresolved — see C17 narrative for full adjudication-required note) | open |
| C18-PROTOCOL-12-GEO-SYNC | none | spec-only | no | TBD | open |
| C19-FRET | none | spec-only | no | **unfalsifiable-now** (KB explicit) | Protein (lane match) |
| D5-HTS-MEISSNER | none | n-a (no explicit HTS-discriminator design) | no | TBD | open |

### Matrix 3 — Execution details (substrate, sources, next action)

| ID | Owner | Cost | AVE-side substrate | Comparison source | Discriminable now? | Confounders | Next action | Last verified |
|---|---|---|---|---|---|---|---|---|
| A1-HOPF | HOPF | $123 BOM | `AVE-HOPF/hardware/hopf_02a.kicad_pcb` + NEC2 predictions in `AVE-HOPF/docs/SESSION_STATE_2026-05-05.md:21` | None — new measurement required | Y (60-400× NEC2 SNR margin) | HOPF-01 lessons: enforce enantiomer pairing, fix $L_{wire}$, ≥2 substrates | Submit fab to JLCPCB; order 3D-print mandrels | 2026-05-07 |
| A2-SAGNAC | PONDER | ~$5k tabletop | `AVE-PONDER/manuscript/vol_ponder/chapters/06_sagnac_rlve_protocol.tex:12` (paper-stage) | None — new measurement required | Y (7.15× contrast easily measurable) | Rotor vibration; fiber temperature stability; common-mode rejection | Elevate from paper-stage to BOM + fab package | 2026-05-16 |
| B1-VAC-BIREFRINGE | Core (no sibling) | facility-class (PVLAS+) | KB-only at [`../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`](../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md) + [`../vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md`](../vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md) | PVLAS current null bound at $\sim 10^{-23}$ (TBD pin specific PVLAS paper) | TBD (depends on PVLAS-upgrade sensitivity vs $10^{12}$ AVE departure) | Stray fields; electrode geometry asymmetry; high-V breakdown of surrounding gas | Scope PVLAS-collaboration proposal or fund tabletop vacuum-mirror variant | 2026-05-16 |
| B2-SCHWINGER | Core (no sibling) | facility-class ($1-10M ELI) | `vol2/.../q-g18-schwinger-pair-wkb.md` (KB only) | ELI-class output data — not yet reached relevant intensity (TBD as facility comes online) | N (current laser facilities below threshold) | Theoretical prefactor unresolved (~1% pending); autoresonance signature distinguishability from non-AVE noise | Refine prefactor derivation; track ELI commissioning timeline | 2026-05-16 |
| B3-PD-FRACTURE | Fusion | low (Pd cell ~$1k) | `AVE-Fusion/src/scripts/simulate_pd_fracture_limit.py`, `simulate_pd_borromean_absorber.py`; empirical anchor at `AVE-Fusion/.agents/handoffs/PALLADIUM_ANALYTICS_INITIATIVE.md:13-27` | **TBD pin source** — historical Pd electrolysis literature (canonical empirical-anchor paper not in current KB) | Y ($x_{max}=0.929$ vs unbounded is testable with standard Pd-electrolysis bench) | Pd-loading is protocol-dependent; pre-1989 vs post-Pons-Fleischmann era instrumentation differs | Pin canonical empirical-anchor paper in Fusion handoff; cross-cite from this row | 2026-05-16 |
| B4-PROTEIN | Protein | compute only | `AVE-Protein/src/ave_protein/engines/s11_fold_engine_v3_jax.py` (2293 lines); `s11_fold_engine_v4_ymatrix.py` (1325 lines) | PDB structures in `AVE-Protein/pdbs/` | Y (RMSD benchmark exists, sub-5 Å target) | Force-field-baseline threshold definition; α-vs-β classification borderline cases | Close RMSD benchmark per `AVE-Protein/src/scripts/s17_sub5_rmsd_benchmark.py`; verify zero-parameter on held-out cohort | 2026-05-16 |
| C1-BH-RING | open (Core scripting) | free (LIGO public data) | **MISSING** — no LIGO driver in any repo | LIGO GWTC-3 catalog; **TBD pin source** — which 3 events does `universal-saturation-kernel-catalog.md:40` compare to? Public strain data at gw-openscience.org | Y (1.7% from GR is at LIGO precision; 10-18% from 3 events well above) | Ringdown fitting-window choice; event subset selection bias; mass-spin priors | Pin which 3 LIGO events; scaffold `src/scripts/ligo_ringdown_ave_comparison.py` in AVE-Core | 2026-05-16 |
| C2-T-PAIR | open | facility-class for direct experiment; free for re-analysis | K4-TLM lattice noise verification at `vol1/.../phase-locked-topological-thread.md:198-216`; no QGP-data driver | RHIC/LHC heavy-ion temperature-resolved correlation data (TBD pin specific dataset) | Y (RHIC reaches $\sim 10^{12}$ K, well above $1.19 \times 10^{10}$) | Temperature inference is model-dependent; entanglement-correlation extraction observable-choice dependent | Decide path — re-analyze RHIC published correlations vs dedicated experiment proposal | 2026-05-16 |
| C3-MUON-DELTA | open | free (Fermilab data public) | **MISSING** — no Fermilab-data driver | **Fermilab Muon g-2 Run-1+Run-2** — Phys. Rev. Lett. 131:161802 (2023); $a_\mu = 0.00116592055(24)$; world average via PDG | Y (muon precision $\sim$0.2 ppm; AVE prediction at 50 ppm well within) | Hadronic vacuum polarization theory dispute (BMW lattice vs $e^+e^-$ data) could mask AVE delta | Convert $\delta = -5\alpha/2$ to same observable form as $a_\mu$; compare against Fermilab + PDG | 2026-05-16 |
| C4-THREE-ROUTE | Core | free for Routes 1+2; Route 3 needs cosmic-$\mathcal{J}$ empirical anchor | [`closure-roadmap.md`](closure-roadmap.md), [`cosmic-parameter-horizon-a031-refinement.md`](cosmic-parameter-horizon-a031-refinement.md) | CODATA $\alpha$ (12 decimals), CODATA $G$ (~4 decimals), CMB+LSS for $\mathcal{J}_{cosmic}$ | Routes 1+2 Y; Route 3 N (A-031 bottleneck) | CODATA $G$ uncertainty (~4 decimals) limits comparison sharpness; $\mathcal{J}_{cosmic}$ empirical anchor undetermined | Execute Route 3 driver for $\mathcal{J}_{cosmic}$ from CMB axis-alignment prereg (C5-CMB-AXIS dependency) | 2026-05-16 |
| C5-CMB-AXIS | Core (execution open) | free (Planck/SDSS public) | **MISSING** — no driver; prereg landed 2026-05-15 | **Planck 2018 PR3 maps** (ESA, pla.esac.esa.int) + **SDSS DR17** galaxy catalog | Y (Planck precision sufficient) | Which axis-of-evil estimator; posterior look-elsewhere; defining "alignment" tolerance | Execute pre-reg per [`closure-roadmap.md:35`](closure-roadmap.md); scaffold CMB+SDSS axis-comparison driver | 2026-05-16 |
| C6-NU-PARITY | open | free (existing oscillation data) | **MISSING** | MiniBooNE, MicroBooNE, IceCube sterile-neutrino searches (TBD pin specific result tracking) | Y if stable $\nu_R$ detected (binary kill-switch) | Sterile-neutrino searches continuously updated; null history doesn't kill, only detection kills | Set monitoring for next major sterile-$\nu$ search update; check IceCube + DUNE pipeline | 2026-05-16 |
| C7-GRB-DISPERSION | open | free (Fermi-LAT, CTA, IceCube public) | **MISSING** | Fermi-LAT GRB time-energy data; IceCube TeV-PeV neutrino arrival times (TBD pin specific catalogs) | Y at TeV-PeV scale | Source-intrinsic energy ordering vs dispersion; statistical limits at high-energy | Pull Fermi-LAT GRB catalog; check for any reported dispersion claim against AVE-null prediction | 2026-05-16 |
| C8-BARYON-LADDER | open | facility-class for new states (CLAS12/PANDA); free for PDG retrospective | KB only at [`../vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md`](../vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md) | PDG 2024 baryon table (6 retrospective matches documented); future CLAS12/PANDA data for forward predictions | Retrospective Y; forward predictions need new facility data | PDG state identification is convention-dependent; spin-parity assignments | Pull PDG 2024 baryon table; verify 6 retrospective matches still hold; pin specific PDG row IDs in KB | 2026-05-16 |
| C9-LEVITATION | open | low ($5-10k bench) | KB only at [`../vol4/falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md`](../vol4/falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md) | **TBD pin source** — prior electrostatic levitation experiments (literature survey not in current KB) | Y (1.846 g testable with standard HV electrostatic setup) | Surrounding-medium voltage breakdown (not vacuum); geometry-dependent V_yield calibration | Survey prior electrostatic-levitation literature; design tabletop bench protocol | 2026-05-16 |
| C10-MUON-LIFE | open | low-medium (high-pressure gas cell) | [`../vol4/simulation/ch14-leaky-cavity-particle-decay/index.md`](../vol4/simulation/ch14-leaky-cavity-particle-decay/index.md); SPICE model `leaky_cavity.cir` | **TBD pin source** — any extreme-$\varepsilon_r$ muon decay measurement in PDG / literature? | TBD (depends on standard correction size vs AVE invariance) | Standard QED correction is small; need $\varepsilon_r$ range wide enough to discriminate | Survey literature for muon-lifetime medium-dependence measurements | 2026-05-16 |
| D1-CHSH | Core | free (compute) | K4-TLM lattice sim at `vol1/.../phase-locked-topological-thread.md:198-216` | Standard CHSH experiments (matches QM by construction; no novel comparison source) | N (matches QM; need to find QM protocol AVE can't reproduce) | CHSH = $2\sqrt{2}$ shared with QM; no single-shot discriminator | Identify quantum-info protocol where AVE deterministic substrate diverges from QM (e.g. contextual measurements, GHZ scenarios) | 2026-05-16 |
| D2-RHO-LAMBDA | Core | free | [`../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md`](../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) | **Planck 2018 PR3** ($\rho_\Lambda = 5.85 \times 10^{-27}$ kg/m³); for mechanism: independent $\rho_{latent}$ derivation pending | Y for value; mechanism (latent heat vs ZPE) is theoretical | $H_0$ tension affects derivation precision; $\rho_{latent}$ independent derivation pending | Close $\rho_{latent}$ independent derivation + $\Gamma_{cryst}$ rate + Friedmann-vs-latent-heat consistency check | 2026-05-16 |
| D3-GEOM-ENTROPY | Core | facility-class (Hawking correlation) | [`../vol3/condensed-matter/ch11-thermodynamics/four-entropy-distinction.md`](../vol3/condensed-matter/ch11-thermodynamics/four-entropy-distinction.md) | None — no Hawking-radiation correlation measurement exists | N (no instrument) | No current Hawking-radiation correlation measurement; can't isolate geometric vs thermodynamic entropy | Wait for analog BH experiments (BEC sonic horizons); identify possible discriminator | 2026-05-16 |
| D4-A034 | Core (cross-repo) | cumulative per instance | [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md) | Per-instance: BCS literature; NOAA GOES 40-yr; Schwarzschild via LIGO; Pd literature; Nilsson 2026 water LLCP; turbulence vs solar flare (specific paper IDs TBD pin per row) | Per-instance Y for 6+ already-validated rows | Catalog universality claim weakens if multiple instances fail | Maintain catalog rigorously; add new instances as they emerge; track per-row PASS/FAIL outcomes | 2026-05-16 |
| B5-PONDER-01 | PONDER | $20-100k (30 kV / 100 MHz + thermal mitigation) | SPICE netlist at `vol4/.../ponder-01-stack-netlist.md`; PONDER repo ch.01-02; **no PCBA** | None (new exp); appendix framing differs from netlist leaf — flag for Grant | Y for predicted thrust magnitude; N for thermal regime (per superseded note) | thermal catastrophe (documented); 100 MHz drive antenna feedthrough; ion-wind at 30 kV; corona losses | Close out as superseded OR revisit thermal mitigation via PONDER ch.5 oil-bath analog | 2026-05-16 |
| B6-PONDER-02 | PONDER | $10-50k (25 kV GaN driver + sapphire GRIN nozzle + 10 GHz VNA + vacuum) | `AVE-PONDER/src/scripts/ponder_02_bistatic_probe.py` simulator + PONDER ch.5; **no hardware**; **no KB leaf** | None (new exp); no comparable GRIN-nozzle microwave-interferometry result (TBD pin) | TBD (sharpness numeric missing from KB) | sapphire fab tolerances; 10 GHz probe coupling into HV; ion-wind plume vs vacuum-saturation plume separation | Surface explicit $\Delta\phi$ from simulator into KB leaf at `vol4/.../project-ponder-02.md` | 2026-05-16 |
| B7-PONDER-05 | PONDER | $10-50k (30 kV DC + 50 kHz AC + matched quartz pair + sub-μN torsion) | PONDER ch.4 + `ponder_05_characterization.py`; vol4 index refs; **no PCBA, no hardware** | None (new exp) for differential parallax; for $C_{eff}(V)$ alone compare against quartz dielectric breakdown literature (TBD pin) | Y (37.7% C rise + 469 μN thrust both above noise floor) | quartz piezoelectric/electrostrictive masking; thermal $\varepsilon_r$ coefficient; ion wind; corona at 30 kV DC; matched-pair fab precision | Distill `project-ponder-05.md` leaf from PONDER ch.4 source into KB | 2026-05-16 |
| C11-MACH-ZEHNDER | Core (no sibling) | facility-class (1-m macroscopic electron interferometer in hard vacuum) | KB only at vol2 ch07 leaf; **no executable observer in workspace** | None (new exp) — no published 1-m-baseline electron Mach-Zehnder result | TBD (depends on facility-class electron interferometer access; 35-rad is large but needs 1-m gravitational baseline) | vibration; stray E/B fields across baseline; coherence length of electron source over 1 m | Pin published electron-interferometer SOTA for sensitivity; scope facility partnership | 2026-05-16 |
| C12-G-STAR | Core | free for retrospective CMB Stage-4 / FCC-ee comparison; facility wait for LISA | KB only; **no driver loads primordial-GW or CMB EW-phase data** | LISA (post-2035); DECIGO; CMB Stage-4 EW expansion rate; FCC-ee / CEPC EW latent heat (**TBD pin published sensitivities**) | N for primordial GW; TBD for CMB Stage-4 | GW astrophysical foregrounds; bosonic-DOF count assumption (AVE assumes 28 unchanged); look-elsewhere | Pin canonical CMB Stage-4 EW expansion-rate sensitivity in KB; scaffold comparison once LISA data lands | 2026-05-16 |
| C13-VLBI-DARK | Core | free (re-analysis of existing VLBI Jupiter-grazing) + facility for new dedicated campaign | KB only; **no driver loads VLBI delay data** | VLBA / EVN Jupiter-occultation campaigns (**TBD pin specific dataset**); standard solar-system GR Shapiro is the null | TBD (depends on VLBI baseline precision vs predicted Snell phase magnitude) | standard Shapiro delay subtraction; ionospheric / Jovian magnetosphere contributions; need explicit AVE numeric prediction | Add explicit $\Delta t$ numeric to KB leaf; survey published Jupiter-VLBI for accessibility | 2026-05-16 |
| C14-DAMA-MATERIAL | Core (experimental partner = DAMA/LIBRA or COSINE-100) | facility-class (underground low-background scintillator) | KB only; **no driver compares DAMA modulation across crystals** | DAMA/LIBRA-phase2 annual-modulation (public, **TBD pin paper**); COSINE-100, ANAIS-112 NaI replications; future Sapphire/Ge runs | Y for phase-invariance check (existing data); N for amplitude-scaling (no swapped-crystal data yet) | WIMP particulate cross-section also varies by target; backgrounds differ across crystal types | Derive explicit $\kappa_{crystal}$ amplitude formula in KB; survey COSINE-100/ANAIS-112 for cross-crystal | 2026-05-16 |
| C15-CLEAVE-01 | Core (no sibling) | low (~$1-5k bench: ADA4530-1 + vacuum chamber + PZT + DAC) | PCBA spec in KB leaf only; **no KiCad / no hardware in any repo** | None (new exp) — no published precision-electrometer-vs-PZT-step in literature (TBD pin) | Y (41.5 mV >> ADA4530-1 noise floor; 1 μm PZT steps commercial) | parasitic input-capacitance drift; PZT-stroke triboelectric charging; vacuum outgassing | Scope KiCad design from leaf spec; identify owner (Core scripting or external EE partner) | 2026-05-16 |
| C16-TORSION-05 | PONDER (torsion-balance metrology is PONDER scope) | medium ($10-50k bench: torsion balance + HV flyback + vacuum) | KB leaf + adjacent PONDER ch.5; **no PCBA, no hardware** | None (new exp); cf. EmDrive-class null results as adjacent literature (TBD pin) | Y (100 μN >> PONDER's <1 μN target sensitivity per ch.5 spec) | ion-wind from corona discharge at HV edges; thermal asymmetry; outgassing transients; electrostatic charging of suspension | Promote from KB leaf to PONDER fab package; tie into existing torsion-metrology infrastructure | 2026-05-16 |
| C17-PROTOCOL-11-SAGNAC-WIND | Core (could elevate to PONDER) | medium ($5-20k for sensitive static Sagnac fiber loop) | KB leaf only; **no hardware, no driver** | **Brillet-Hall (1979)** $\Delta c/c < 5 \times 10^{-9}$ optical cavity; **Wolf et al. (2003-2010)** fiber tests $\Delta c/c < 10^{-17}$ (both rule out 2 M-rad effect at ~10-15 OOM); also CMB dipole 370 km/s direction (Planck/COBE) for orientation | **N as currently framed** — existing Brillet-Hall + Wolf bounds already rule out 2 M-rad effect; test cannot proceed until entrainment-inconsistency with A2-SAGNAC is resolved | **(i) Internal inconsistency with A2-SAGNAC entrainment picture** (A2 requires local LC rotor-entrained; C17 requires translation-unentrained — can't both be true under simple model). **(ii) Existing static-Sagnac null bounds contradict the prediction by ~10-15 OOM** — either AVE is falsified or Protocol 11 geometry doesn't actually map. (iii) Naive secondary confounders: temperature-driven fiber index drift; ionospheric Faraday rotation; Earth-rotation Sagnac contribution itself. | **Adjudication required BEFORE any fab work:** (1) Resolve A2/C17 entrainment-inconsistency — does AVE commit to asymmetric entrainment (rotation entrains, translation doesn't) or does one of A2/C17 need reframing? (2) Pin the specific Brillet-Hall / Wolf et al. papers that bound this geometry and verify they actually cover Protocol 11's configuration. (3) If resolution confirms AVE is falsified by existing data, mark C17 outcome FAIL and reframe Protocol 11 as a historical-data row not a future-exp row. | 2026-05-16 |
| C18-PROTOCOL-12-GEO-SYNC | Core (would require ESA/NASA/SES partnership for GEO laser link) | facility-class (precision GEO laser ranging requires existing infrastructure) | KB leaf only; **no driver, no measurement** | GRACE-FO laser ranging; SLR ILRS network archives (TBD pin); LRO laser ranging — none GEO-target but constrain relevant physics | TBD (16.7 mm at GEO requires sub-cm laser-ranging precision differential vs pure-GR Shapiro) | standard GR Shapiro delay subtraction; tropospheric/ionospheric path delay; satellite ephemeris precision; clock-vs-TOF separation | Survey ILRS / GRACE-FO laser-ranging public archives for vertical-baseline TOF residuals after GR subtraction | 2026-05-16 |
| C19-FRET | Protein (AVE-Protein lane) | free for derivation; facility-class (compact-object) for measurement | KB leaf only; **no Protein-repo executable observer** (engines test fold class, not FRET-parallax) | None (compact-object FRET measurement does not exist) | **N** (KB explicit: "currently unfalsifiable") | thermal fluctuation of α-helix dominates by ~10 OOM; fluorophore dipole-orientation variability; single-molecule FRET precision floor | Hold as documented future-target row; revisit if compact-object FRET or resonant-amplification proposal emerges | 2026-05-16 |
| D5-HTS-MEISSNER | Core (no sibling) | low-medium (existing HTS samples + magnetometry; the AVE-distinct prediction is what's missing, not the apparatus) | Mechanism derivation in vol3 ch9 leaf; **no Vol VII leaf in KB**; **no driver / no hardware** | BCS literature (canonical); HTS literature on Meissner-vs-Cooper-pair model gap (TBD pin) | TBD (no explicit HTS discriminator numeric in KB) | standard BCS reproduces $B_c(T)$ to 0.00% per A-034; AVE-distinct prediction is mechanism not number — single-experiment discrimination structurally difficult | Distill explicit Vol VII Ch.2 *metric-streamlining* leaf from manuscript source (if exists outside KB) into KB; surface explicit HTS-vs-BCS discriminator numeric | 2026-05-16 |

### Matrix maintenance

Per Grant directive (memory `feedback_validate_what_you_did.md`): non-trivial work isn't done until live-fire validation has run. **Update cadence:**

- Update `Last verified` on a row whenever its claim is grep-verified against the KB leaf cited
- Update `Outcome` only when a bench/sim/data-driver has actually run and produced a measurement; never inferred from "should be done"
- Update `Pre-reg` only when an `A-NNN-prereg.md` is frozen (status verbatim in the prereg file)
- Update `Built/coded` from "no" to "code-written" only when there is an actual executable script at the substrate path
- Flag `TBD pin source` items for resolution before the row is cited in any external-facing artifact (manuscript, prereg)
- Whenever a row's outcome changes, propagate to the `Cascade & co-load` cells of the rows it touches

**Stable IDs (A1, B3, C4, D2, …) are load-bearing for cross-citation from research docs, preregs, and commits.** Renumbering an ID requires updating every cite-back.

---


> → Primary: [Universal Saturation-Kernel Catalog (A-034)](universal-saturation-kernel-catalog.md) — the 21-instance cross-scale catalogue that underlies Tier D and several Tier C predictions
> → Primary: [Common Foreword](../../frontmatter/00_foreword.tex) — canonical narrative source for the "Epistemic Position" + "Falsifiable Standard" + "Three-Route Framework Commitment" framings
> ↗ See also: [A-031 Refined: Cosmic-Parameter Horizon](cosmic-parameter-horizon-a031-refinement.md) — Route 3 ($\mathcal{J}_{cosmic}$) bottleneck and the observable-mechanism vs cosmic-parameter distinction
> ↗ See also: [Measurement Hierarchy SNR](../vol4/falsification/ch11-experimental-bench/measurement-hierarchy-snr.md) — bench-class SNR framing for the Tier A and Tier B substrate
> ↗ See also: [Three Boundary Observables: $\mathcal{M}$, $\mathcal{Q}$, $\mathcal{J}$](boundary-observables-m-q-j.md) — substrate-observability rule that frames "what is measurable" at any saturation surface
