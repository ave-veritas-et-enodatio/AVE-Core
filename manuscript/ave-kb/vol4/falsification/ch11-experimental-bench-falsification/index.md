[↑ Vol 4: Falsification](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [5s5b0d, 7tynm2, baoa36, cltls0, cwjd8t, fh6w3y, gw2wgc, h55fy1, iz3svl, k9up5c, kl1ern, oiw6cb, om0rtq, p12mem, pp3qwf, qsgl7d, ui3m8a, wqmb19, wzezvt, ydksh6]
-->

# Ch.11: Experimental Bench Falsification

<!-- Note: Ch.11 has NO \label{ch:...} at its \chapter{} command -->

Comprehensive catalogue of tabletop falsification experiments, existing experimental signatures supporting the AVE framework, open-source hardware build guides, engineering scale-up architectures, and advanced telemetry concepts. All predictions derive from the single calibration constant $l_{node}$ with zero free parameters.

## Key Results

| Result | Expression | Source |
|---|---|---|
| Sagnac-RLVE phase shift | $\Delta\phi = 4\pi L_{fiber} v_{network}/(\lambda c) \approx 2.07\,\text{Rad}$ (Tungsten rotor, 200 m fiber, 10k RPM) | sagnac-rlve |
| Metric mutual inductance ratio | $\Psi = \rho_W/\rho_{Al} \approx 7.15$ (density-dependent, not geometry-dependent) | sagnac-rlve |
| VFDT null result | $v_{vac} \approx 1.33 \times 10^{-13}\,\text{m/s}$; phase shift $\sim 10^{-14}\,\text{rad}$ (undetectable) | tabletop-graveyard |
| RVR scalar gap | $\delta_L \approx 7.4 \times 10^{-26}$; requires $Q \ge 2.7 \times 10^{25}$ (impossible) | tabletop-graveyard |
| CLEAVE-01 charge prediction | $Q = \xi_{topo} \cdot x = 0.415\,\text{pC}$ per $\mu\text{m}$; $V = 41.5\,\text{mV}$ | project-cleave-01 |
| Levitation limit | $m_{max} = V_{yield} \xi_{topo}/g = 1.846\,\text{g}$ | metric-levitation-limit |
| $\sqrt{\alpha}$ yield limit | $V_{yield} = \sqrt{\alpha} \times 511\,\text{kV} = 43.65\,\text{kV}$ | zero-parameter-derivations |
| YBCO phased array thrust | $F_{total} = 10^6 \times 0.02448\,\text{N} = 24{,}480\,\text{N}$ (2.5 metric tons) | ybco-phased-array |
| $c^2$ multiplier acceleration | $a = c^2 \nabla n = 1{,}283\,\text{m/s}^2$ (130 G's) from $\Delta n = 1.42 \times 10^{-17}$ | metric-refraction-capacitor |
| Sapphire phonon centrifuge | $a_{LT} = v_{vac}^2/r = 62.3\,\text{m/s}^2$ (6.35 G's) | sapphire-phonon-centrifuge |
| Achromatic impedance lens | $Z_{gravity} = \sqrt{\mu(r)/\varepsilon(r)} = Z_0$; zero reflection at all angles | achromatic-lens-test |
| Vacuum impedance mirror | $\Gamma(V) = [(1-(V/V_{yield})^2)^{-1/4} - 1]/[(1-(V/V_{yield})^2)^{-1/4} + 1]$; $\Gamma \to 1$ as $V \to V_{yield}$ | vacuum-impedance-mirror |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Epistemology of Falsification](epistemology-of-falsification.md) | Three binary kill-switches: Neutrino Parity, GRB Dispersion, Birefringence ($E^2$ vs $E^4$) |
| [Tabletop Graveyard](tabletop-graveyard.md) | VFDT null result (inertial anchor); RVR scalar gap ($G/c^2$ suppression) |
| [Sagnac-RLVE](sagnac-rlve.md) | Definitive sub-\$5k test; exact derivation ($\Delta\phi \approx 2.07\,\text{Rad}$); hardware spec; $\Psi$ ratio |
| [Existing Experimental Signatures](existing-experimental-signatures.md) | Proton radius puzzle; neutron lifetime anomaly; Hubble tension; LIGO echoes; vortex core limits |
| [Project CLEAVE-01](project-cleave-01.md) | Femto-coulomb electrometer; $Q = \xi_{topo} x$; 41.5 mV per micron |
| [Project HOPF-02](project-hopf-02.md) | S-parameter VNA falsification; anomalous chiral $S_{11}$ notch; Snell parallax test |
| [Project ROENTGEN-03](project-roentgen-03.md) | Solid-state Sagnac induction; 4.2 pT Lock-In detection |
| [Project ZENER-04](project-zener-04.md) | Impedance avalanche detector; Marx generator; avalanche knee at 43.65 kV |
| [Metric Levitation Limit](metric-levitation-limit.md) | $m_{max} = 1.846\,\text{g}$; dielectric death spiral; topological rocket equation |
| [Project TORSION-05](project-torsion-05.md) | Horizontal metric rectification; asymmetric flyback; $\sim 100\,\mu\text{N}$ DC thrust |
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
| [Sagnac-Parallax](sagnac-parallax.md) | Protocol 11: 24-hour galactic wind vectoring via static Sagnac loop |
| [GEO-Synchronous Impedance](geo-synchronous-impedance.md) | Protocol 12: vertical laser TOF anomaly mapping Earth's LC saturation envelope |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---
