[↑ Vol 4: Falsification](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-5s5b0d, clm-7tynm2, clm-baoa36, clm-bdualb, clm-cltls0, clm-clvchn, clm-cwjd8t, clm-fh6w3y, clm-fuajdb, clm-gw2wgc, clm-h55fy1, clm-iz3svl, clm-k9up5c, clm-kl1ern, clm-oiw6cb, clm-om0rtq, clm-p12mem, clm-pp3qwf, clm-pvlas1, clm-qsgl7d, clm-ui3m8a, clm-wzezvt, clm-ydksh6, clm-yr6tu4]
subtree-experiments: [exp-0n5p16, exp-1ddtr0, exp-1up5ww, exp-6kwkx7, exp-71uhr0, exp-742kv5, exp-7jekc6, exp-ct4cts, exp-onqclb, exp-po1a0v, exp-rth12t, exp-v6nzcq]
-->

# Ch.11: Experimental Bench Falsification

<!-- Note: Ch.11 has NO \label{ch:...} at its \chapter{} command -->

> **🔴 SCOPE-CORRECTION (2026-06-15, keystone $\alpha$-verdict + zero-parameter register reconciliation; Rule 12 — the lead description below is PRESERVED unedited; this dated banner supersedes two of its scope claims and resolves the self-contradiction against the Key-Results ``$\sqrt{\alpha}$ yield limit'' row below).** Two corrections, both propagating already-merged `origin/main` rulings (the keystone $\alpha$-verdict and the 26→3 parameter register) to this lagging leaf:
> 1. **Not a *single* calibration constant, and not *zero* free parameters at top level.** The "$\sqrt{\alpha}$ yield limit" row in the Key Results table below ($V_{yield} = \sqrt{\alpha}\times 511\,\text{kV} = 43.65\,\text{kV}$) itself consumes **$\alpha$** AND **$m_e c^2 = 511$ kV** as inputs, so "single calibration constant $l_{node}$ with zero free parameters" is self-undercut. Honest scope: AVE reduces the Standard Model's $\sim$26 empirical parameters to **3 interlocked calibration inputs $\{m_e, \alpha, G\}$ + 4 axioms**, from which the predictions catalogued here follow with **zero free parameters *beyond those 3 inputs*** (foreword honest-scope register; manuscript `backmatter/03_geometric_inevitability.tex` Scope-correction 2026-06-14).
> 2. **$R\cdot r = 1/4$ is NOT a quantity the substrate independently selects.** The keystone $\alpha$-verdict (auditor-gated 2026-06-14) rules $\alpha$ one of the 3 *retained inputs*, not a derived output: $\alpha^{-1} = 4\pi^3+\pi^2+\pi$ is a **Class-B named geometric identification** whose *scale* ($\sim$1/137) is forced by the Compton-resonance trapping condition but whose *exact value* rests on the single identification $R\cdot r = 1/4$ — shared across the $(2,q)$ bound-resonator ladder, not electron-specific — which **the substrate does not independently select** (both named lift-routes closed; the honest kinematic route absorbs $\alpha$, forcing $R \cdot r \to 4\pi^2\alpha \neq 1/4$). A value-scoped synonym is **"echo at the value level,"** recorded *beneath* the canonical Class-B label and never as a bare standalone "echo." The "substrate-mechanism for $R \cdot r = 1/4$" wording below names the Class-B provenance machinery (Axiom-4 self-saturation + Op14 Meissner-asymmetric + the phasor-area$=$Nyquist-cell-area identification), which remains canonical — but it does **not** upgrade the *value* to substrate-selected. Canonical scope: [`../../../vol1/ch8-alpha-golden-torus.md`](../../../vol1/ch8-alpha-golden-torus.md) (line 11); in-volume anchor: [`../../circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md`](../../circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) (line 19).

Comprehensive catalogue of tabletop falsification experiments, existing experimental signatures supporting the AVE framework, open-source hardware build guides, engineering scale-up architectures, and advanced telemetry concepts. All predictions derive from the single calibration constant $l_{node}$ with zero free parameters at **Class B substrate-mechanism manifestation level per Q-EMBED-SEL-1 Phase 1+2+3 (2026-05-31)** — substrate-mechanism for $R \cdot r = 1/4$ via Axiom-4 self-saturation + Op14 Meissner-asymmetric + named phasor-area-equals-Nyquist-cell-area identification, see [`../../../vol1/ch8-alpha-golden-torus.md`](../../../vol1/ch8-alpha-golden-torus.md) §"Substrate-mechanism provenance of regime (c)".

## Key Results

| Result | Expression | Source |
|---|---|---|
| Sagnac-RLVE phase shift | $\Delta\phi = 4\pi L_{fiber} v_{network}/(\lambda c) \approx 2.07\,\text{Rad}$ (Tungsten rotor, 200 m fiber, 10k RPM) | sagnac-rlve |
| Metric mutual inductance ratio | $\Psi = \rho_W/\rho_{Al} \approx 7.15$ (density-dependent, not geometry-dependent) | sagnac-rlve |
| VFDT null result | $v_{vac} \approx 1.33 \times 10^{-13}\,\text{m/s}$; phase shift $\sim 10^{-14}\,\text{rad}$ (undetectable) | tabletop-graveyard |
| RVR scalar gap | $\delta_L \approx 7.4 \times 10^{-26}$; requires $Q \ge 2.7 \times 10^{25}$ (impossible) | tabletop-graveyard |
| CLEAVE-01 charge prediction | $Q = \xi_{topo} \cdot x = 0.415\,\text{pC}$ per $\mu\text{m}$; $V = 41.5\,\text{mV}$ | project-cleave-01 |
| CLEAVE-01 apparatus floors (derived) | $dV/dx = \xi_{topo}/C_{in} = 41.49\,\text{nV/pm}$; binding noise = 1/f+drift (~0.61 µV rms), $\sigma_Q \le \delta\times414.9$ fC; CPD swing 19.97% of floor | cleave-01-requirements-boundary-conditions |
| Levitation limit | $m_{max} = V_{yield} \xi_{topo}/g = 1.846\,\text{g}$ | metric-levitation-limit |
| $\sqrt{\alpha}$ yield limit | $V_{yield} = \sqrt{\alpha} \times 511\,\text{kV} = 43.65\,\text{kV}$ | zero-parameter-derivations |
| YBCO phased array thrust | $F_{total} = 10^6 \times 0.02448\,\text{N} = 24{,}480\,\text{N}$ (2.5 metric tons) | ybco-phased-array |
| $c^2$ multiplier acceleration | $a = c^2 \nabla n = 1{,}283\,\text{m/s}^2$ (130 G's) from $\Delta n = 1.42 \times 10^{-17}$ | metric-refraction-capacitor |
| Sapphire phonon centrifuge | $a_{LT} = v_{vac}^2/r = 62.3\,\text{m/s}^2$ (6.35 G's) | sapphire-phonon-centrifuge |
| Achromatic impedance lens | $Z_{gravity} = \sqrt{\mu(r)/\varepsilon(r)} = Z_0$; zero reflection at all angles | achromatic-lens-test |
| Vacuum impedance mirror | $\Gamma(V) = [(1-(V/V_{yield})^2)^{-1/4} - 1]/[(1-(V/V_{yield})^2)^{-1/4} + 1]$; $\Gamma \to 1$ as $V \to V_{yield}$ | vacuum-impedance-mirror |
| C11-MACH-ZEHNDER parallax shift | $\Delta\Phi \approx 250\,\text{rad}$ on 1-m baseline at 100-eV electron energy; $n_s = 1 + (9/7)\varepsilon_{11}$ vs $n_t = 1 + (2/7)\varepsilon_{11}$, $\Delta n = \varepsilon_{11} = 7GM/c^2r$ | project-c11-mach-zehnder |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Epistemology of Falsification](epistemology-of-falsification.md) | Three binary kill-switches: Neutrino Parity, GRB Dispersion, Birefringence COEFFICIENT ($\sim 10^6\times$ QED; ~~$E^2$ vs $E^4$~~ slope retracted, Rule-12 clm-pp3qwf) |
| [Tabletop Graveyard](tabletop-graveyard.md) | VFDT null result (inertial anchor); RVR scalar gap ($G/c^2$ suppression) |
| [Sagnac-RLVE](sagnac-rlve.md) | Definitive sub-\$5k test; exact derivation ($\Delta\phi \approx 2.07\,\text{Rad}$); hardware spec; $\Psi$ ratio |
| [Existing Experimental Signatures](existing-experimental-signatures.md) | Proton radius puzzle; neutron lifetime anomaly; Hubble tension; LIGO echoes; vortex core limits |
| [Project CLEAVE-01](project-cleave-01.md) | Femto-coulomb electrometer; $Q = \xi_{topo} x$; 41.5 mV per micron |
| [CLEAVE-01 Requirements / Boundary Conditions](cleave-01-requirements-boundary-conditions.md) | **Derived** apparatus floors (all work shown): 41.49 nV/pm position→charge coupling; 1/f+drift binding-noise model; ENOB/level-stability math; parametric in $\delta$ and $C_{in}$. Physics — solidity-tagged `clm-fuajdb` |
| [CLEAVE-01 Trade Study / Decision Register](cleave-01-trade-study-decision-register.md) | **OPEN decision-record (`no-claim`, STATUS:OPEN)**: every make-vs-buy + 6 design-knobs as worked option sets (team-aware build-feasibility); cross-linked to Q-C15. **Selects nothing** |
| [Project HOPF-02](project-hopf-02.md) | S-parameter VNA falsification; anomalous chiral $S_{11}$ notch; Snell parallax test |
| [Project ROENTGEN-03](project-roentgen-03.md) | Solid-state Sagnac induction; 4.2 pT Lock-In detection — RETIRED to corroborative-null (2026-06-03) |
| [Project ZENER-04](project-zener-04.md) | Impedance avalanche detector; Marx generator; avalanche knee at 43.65 kV |
| [Metric Levitation Limit](metric-levitation-limit.md) | $m_{max} = 1.846\,\text{g}$; dielectric death spiral; topological rocket equation |
| [Project TORSION-05](project-torsion-05.md) | Horizontal metric rectification; asymmetric flyback; $\sim 100\,\mu\text{N}$ DC thrust |
| [Project C11-MACH-ZEHNDER](project-c11-mach-zehnder.md) | Electron Mach-Zehnder gravitational-parallax interferometry; $\sim 250\,\text{rad}$ phase shift on 1-m macroscopic baseline at 100 eV; tests $n_s$ vs $n_t$ spatial/temporal refractive split from $\varepsilon_{11} = 7GM/c^2r$ |
| [YBCO Phased Array](ybco-phased-array.md) | $10^6$-node micro-inductor array; 2.5 metric tons lift per m$^2$ |
| [Metric Refraction Capacitor](metric-refraction-capacitor.md) | $BaTiO_3$ high-$k$ graded dielectric; $c^2$ multiplier; 130 G's from $10^{-17}$ index shift |
| [Sapphire Phonon Centrifuge](sapphire-phonon-centrifuge.md) | Acoustic vortex at 11,100 m/s; 6.35 G artificial gravity; Beltrami inductive shield |
| [Applied Telemetry](applied-telemetry.md) | Hull boundary sensors; Schwinger redline monitors; sonoluminescence FOC isomorphism |
| [Open-Source Hardware](open-source-hardware.md) | HOPF-01 build guide (FR-4 torus knots, VNA protocol); PONDER-01 build guide (MLCC array, avalanche transistor) |
| [Zero-Parameter Derivations](zero-parameter-derivations.md) | $\sqrt{\alpha}$ yield limit; nuclear fusion limit alignment; levitation limit alignment |
| [Horsemen of Falsification](horsemen-of-falsification.md) | LHC paradox (dielectric relaxation time); LIGO paradox (lossless transmission line) |
| [Achromatic Lens Test](achromatic-lens-test.md) | Protocol 9: metamaterial impedance lens; $\Gamma = 0$ across all angles |
| [Boundary Trapping Test](boundary-trapping-test.md) | Protocol 10: asteroid belt and Oort Cloud as impedance termination shocks |
| [Vacuum Impedance Mirror](vacuum-impedance-mirror.md) | Induced $Z_{local} \to \infty$ via asymmetric saturation; APD back-scatter detection; full $\Gamma(V)$ derivation |
| [PVLAS Static-B Verdict](pvlas-static-b-verdict.md) | Static-B null is CONSISTENT with AVE (not a falsification); $\mu$ = ideal relativistic inductor (circulation-keyed) → $\delta n_\mu=0$ exactly under static B; bold side-prediction = no static-B birefringence; E-route ($3.75\pi/\alpha^2\approx2.2\times10^5$, v3 single instantaneous footing, OPTION-B 2026-07-07; the mixed footing over cycle-averaged $\alpha/15\pi$ doubles it to $7.5\pi/\alpha^2\approx4.42\times10^5$, convention history) is the real test |
| [Sagnac-Parallax](sagnac-parallax.md) | Protocol 11: 24-hour galactic wind vectoring via static Sagnac loop |
| [GEO-Synchronous Impedance](geo-synchronous-impedance.md) | Protocol 12: vertical laser TOF anomaly mapping Earth's LC saturation envelope |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---
