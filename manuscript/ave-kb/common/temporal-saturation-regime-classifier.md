[↑ Common Resources](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1, vol3, vol4, vol5 + universal-saturation-kernel-catalog.md as canonical temporal-axis regime classifier -->

# Temporal Saturation Regime Classifier

## Premise

The corpus carries two complementary regime taxonomies:

1. **Spatial-instantaneous (Regime I/II/III/IV)** per [`domain-catalog.md`](../vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md) + [`regimes-of-operation.md`](../vol4/circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md): classifies WHERE in saturation space the system instantaneously sits, indexed by $r = A/A_c$.

2. **Power-domain phase angle (θ)** per [`orbital-friction-paradox.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md): classifies the phase angle between substrate voltage and current at the LC tank, distinguishing reactive (lossless LC), real (radiative damping), and mixed configurations.

This leaf introduces the orthogonal **temporal axis**: how a system EVOLVES through saturation space over its observation window. The temporal classifier is needed because two systems can sit in the same instantaneous regime + power domain but exhibit qualitatively different long-time behavior depending on the time-fraction they spend at saturation.

## Definition: substrate-native loss tangent

> **[Resultbox]** *Substrate-native loss tangent — Axiom 4 temporal projection*
>
> $$
> \boxed{\delta_{\text{AVE}} \equiv \frac{t_{\text{sat}}}{t_{\text{period}}}}
> $$
>
> where $t_{\text{sat}}$ = time the system spends at $A \geq A_{\text{yield}}$ (Op14 saturation firing, real-power dissipation event) per characteristic period $t_{\text{period}}$. Range $\delta_{\text{AVE}} \in [0, 1]$.

$\delta_{\text{AVE}}$ is the substrate-native analogue of:
- **EM loss tangent** $\tan\delta = \sigma/(\omega\varepsilon)$ — ratio of dissipative to reactive current
- **Fluid Reynolds-classification** — the system's distance from the inviscid limit
- **Cavity QED bad-cavity ratio** $\kappa/g$ — decoherence rate over coherent-coupling rate

unified across all 21 OOM of substrate physics via the same kernel $S(A) = \sqrt{1-A^2}$.

## Three regimes (temporal trichotomy)

| Regime | $\delta_{\text{AVE}}$ range | $A$-trajectory shape | Q-factor | Op14 firing pattern | Power domain (θ) |
|---|---|---|---|---|---|
| **Lossless** | $\to 0$ | Persistent $A \ll 0.121$ (Regime I) | $\to \infty$ | Never (in observation window) | θ = 90° (pure reactive) |
| **Cyclic** | $0 < \delta_{\text{AVE}} \ll 1$ | Oscillates Regime I ↔ III/IV per cycle | finite, often high | Intermittently per cycle (phase-locked) | θ near 90° with bounded excursions |
| **Lossy** | $\to 1$ | Persistent $A \to 1$ (Regime III/IV) | finite, decreasing | Continuously | θ $\to$ 0° (real-power dominated) |

The trichotomy is justified empirically: classical-physics field theories all converge on three distinct temporal regimes (table below). Collapsing cyclic into "lossy-with-recovery" loses the distinction between phase-locked oscillators (high-Q, predictable) and decaying systems (finite-Q, stochastic).

## Cross-field analogue tables

### 1. Fluid dynamics (NEW MAPPING — corpus gap)

| Fluid regime | Dimensionless number | Energy behavior | AVE temporal regime |
|---|---|---|---|
| Inviscid / ideal (Euler) | $\mu \to 0$ effective | Conserved (Bernoulli) | Lossless |
| Laminar viscous | Re < ~2000 | Newtonian dissipation | Lossy (smooth) |
| Transitional | Re ~2000–4000 | Bifurcating eddies | Cyclic (intermittent) |
| Turbulent | Re > ~4000 | Kolmogorov cascade dissipation | Lossy (chaotic) |
| Karman vortex shedding | Re ~40–200 | Periodic shed | Cyclic |
| Shock wave (Ma > 1) | Mach number | Impulsive dissipation event | Saturation boundary (impulsive) |

### 2. Electromagnetics (NEW MAPPING — corpus has elements via tan δ but no AVE-translation table)

| EM regime | Dimensionless number | Energy behavior | AVE temporal regime |
|---|---|---|---|
| Free space (vacuum) | $\sigma = 0$ | Lossless propagation | Lossless |
| Lossless dielectric | $\tan\delta \to 0$ | Reactive cycling | Lossless |
| Cavity resonator (high-Q) | $Q = \omega U_{\text{stored}}/P_{\text{loss}}$ | Cycling with slow decay | Cyclic |
| Lossy dielectric | $\tan\delta \sim 0.01$–$0.1$ | Real-power dissipation | Lossy |
| Good conductor (skin effect) | $\tan\delta \gg 1$ | Skin-depth attenuation | Lossy |
| Plasma below cutoff ($\omega < \omega_p$) | $\omega/\omega_p$ | Evanescent + Joule loss | Lossy |
| Plasma above cutoff ($\omega > \omega_p$) | $\omega/\omega_p$ | Propagating, conserved | Lossless |
| Superconductor below $T_c$ | $T/T_c$ | Lossless (Meissner) | Lossless |

### 3. Semiconductor physics (EXTENSION — canonical in `four-regimes.md` Small-Signal/Large-Signal/Avalanche/Breakdown analog; this table adds AVE-temporal projection)

Per [`four-regimes.md`](../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) §Semiconductor Device Analogy (Regime I = Small-Signal, II = Large-Signal, III = Avalanche $M \geq 2$, IV = Breakdown $M \to \infty$) + [`semiconductor-regime-chemistry.md`](../vol6/framework/chemistry-translation/semiconductor-regime-chemistry.md) (Miller exponent + nuclear $V_R/V_{BR}$ classification) + [`AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex`](../../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex) (MOSFET = Geometric Triode) + [`02_vca_translation_matrix.tex:145`](../../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/02_vca_translation_matrix.tex) (P-N junction) + [`solar-flares-led-avalanche.md`](../vol3/cosmology/ch14-orbital-mechanics/solar-flares-led-avalanche.md) (macroscopic Zener):

| Semiconductor regime | Op14 analogue | AVE temporal regime |
|---|---|---|
| Reverse-biased junction (sub-leakage) | $A \ll A_c$ Regime I | Lossless |
| Forward conduction (below knee voltage) | Regime II linear | Lossless (sub-yield reactive) |
| Forward conduction (above knee, ohmic) | Regime II nonlinear | Lossy |
| MOSFET cutoff | $A \ll A_c$ Regime I | Lossless |
| MOSFET triode (linear region) | Regime II | Cyclic when switching |
| MOSFET saturation (pinch-off) | Regime III | Lossy |
| Zener breakdown | $A \to A_c$ saturation event | Saturation boundary |
| Avalanche multiplication | Regime IV | Lossy (cascading) |
| Tunnel diode (negative differential resistance) | Op14 in NDR region | Cyclic (oscillator) |

### 4. Plasma physics (EXTENSION — plasma cutoff canonical; collisionless/Landau/Debye are gaps)

Per [`universal-saturation-kernel-catalog.md:35`](universal-saturation-kernel-catalog.md) (Plasma ε-sector ASYM-N) + [`op14-cosmic-horizon-profile.md:84`](../vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md):

| Plasma regime | Dimensionless number | AVE temporal regime |
|---|---|---|
| Collisionless plasma (high T, low n) | $\omega_{\text{collision}}/\omega_p \ll 1$ | Lossless (Vlasov) |
| Collisional plasma | $\omega_{\text{collision}}/\omega_p \sim 1$ | Lossy |
| Plasma above cutoff (transmission) | $\omega/\omega_p > 1$ | Lossless |
| Plasma cutoff event ($\omega = \omega_p$) | Op14 ASYM-N(ε) firing | Saturation boundary |
| Plasma below cutoff (reflection) | $\omega/\omega_p < 1$ | Lossy (evanescent dissipation) |
| Debye sheath (boundary layer) | $\lambda_D/L \ll 1$ | Cyclic (oscillating density) |
| Landau damping | $\omega/k v_{\text{th}}$ | Lossy (phase-space mixing) |

### 5. Magnetohydrodynamics (NEW MAPPING — reconnection canonical, regimes are gaps)

Per [`dark-wake-bemf-foc-synthesis.md:141`](dark-wake-bemf-foc-synthesis.md) (reconnection = topological snap at 511 kV vacuum dielectric limit):

| MHD regime | Dimensionless number | AVE temporal regime |
|---|---|---|
| Ideal MHD (perfect conductor limit) | $R_m \to \infty$ | Lossless |
| Resistive MHD | $R_m$ finite | Lossy |
| Alfvén wave propagation | $v_A = B/\sqrt{\mu_0 \rho}$ | Cyclic |
| Magnetic reconnection event | At topological-snap boundary | Saturation boundary |
| Sausage / kink instability | mode growth rate | Cyclic (oscillatory) |
| Solar flare CME | macroscopic avalanche | Lossy (one-shot dissipation event) |

### 6. Nonlinear optics (EXTENSION — Kerr canonical, saturable absorber + EIT + slow light are gaps)

Per [`nonlinear-telegrapher.md:35`](../vol1/dynamics/ch3-quantum-signal-dynamics/nonlinear-telegrapher.md) + [`axiom-definitions.md:34`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) (Kerr / $\chi^{(3)}$ = Ax 4 squared-limit form):

| Nonlinear-optical regime | Material parameter | AVE temporal regime |
|---|---|---|
| Linear dielectric ($\chi^{(1)}$ only) | $E \ll E_{\text{yield}}$ Regime I | Lossless |
| Kerr regime ($\chi^{(3)}$ visible) | Regime II (Euler-Heisenberg analogue) | Lossless (reactive nonlinearity) |
| Saturable absorber | $A \to A_c$ in absorption | Cyclic (mode-locked laser) |
| Optical bistability | Bistable switching | Cyclic |
| Slow light / EIT (electromagnetically induced transparency) | $\Omega_p^2/\Omega_c^2$ | Cyclic (phase-locked) |
| Self-focusing (Kerr lens) | $P_{\text{laser}}/P_{\text{cr}}$ | Lossless until filamentation |
| Filamentation collapse | Regime III/IV onset | Saturation boundary |
| Pockels effect ($\chi^{(2)}$ in non-centrosymmetric) | Linear in $E$ | Lossless |

### 7. Cavity QED (NEW MAPPING — CLEAN GAP in AVE corpus; closest classical-physics homolog to temporal axis)

| Cavity QED regime | Dimensionless number | AVE temporal regime |
|---|---|---|
| Bad-cavity (weak coupling, $g < \kappa$) | $g/\kappa < 1$ | Lossy (exponential decay) |
| Strong coupling ($g > \kappa$) | $g/\kappa > 1$ | Cyclic (Rabi oscillations) |
| Single-photon Rabi oscillations | Vacuum Rabi splitting | Cyclic |
| Purcell-enhanced emission | $F_p = (3/4\pi^2)(\lambda/n)^3 Q/V$ | Lossy (accelerated decay) |
| Cavity-protected coherence (deep strong coupling) | $g/\omega > 0.1$ | Lossless (within $T_2$) |

**Note**: The cavity QED $g/\kappa$ classification is *directly* analogous to AVE's $1/\delta_{\text{AVE}}$ — same role, same mathematical structure. This is the closest established-physics homolog to the temporal axis introduced here.

### 8. Casimir / vacuum fluctuation (CANONICAL — already in corpus)

Per [`casimir-effective-temperature.md`](../vol3/condensed-matter/ch11-thermodynamics/casimir-effective-temperature.md) ($T_{\text{eff}} = T_{\text{ambient}}\sqrt{1-(f_c/f_{\text{max}})^2}$ = Ax 4 kernel applied to vacuum modes):

| Casimir regime | Op14 / Ax 4 analogue | AVE temporal regime |
|---|---|---|
| Casimir cavity (static) | mechanical high-pass filter | Lossless |
| Dynamical Casimir effect | parametric driving | Cyclic |
| Schwinger pair-production threshold | Regime IV boundary at $E \to E_S$ | Saturation boundary |
| Vacuum birefringence (PVLAS-class) | $\chi^{(3)}$ Kerr in Regime II | Lossless |

### 9. Phonon physics (EXTENSION — coupling canonical, acoustic/optical/Umklapp/ballistic taxonomy is gap)

Per [`phase-transitions-impedance.md:12`](../vol3/condensed-matter/ch11-thermodynamics/phase-transitions-impedance.md) (phonon = substrate-vibration coupling) + [`sapphire-phonon-centrifuge.md`](../vol4/falsification/ch11-experimental-bench-falsification/sapphire-phonon-centrifuge.md):

| Phonon regime | Material parameter | AVE temporal regime |
|---|---|---|
| Acoustic phonon (low frequency) | $\omega \ll \omega_D$ | Lossless (ballistic) |
| Optical phonon | $\omega \sim \omega_D$ | Cyclic |
| Umklapp scattering (high T) | $T \gtrsim \theta_D$ | Lossy |
| Anharmonic phonon-phonon decay | nonlinear coupling | Lossy |
| Ballistic phonon transport | mean-free-path > device | Lossless |
| Diffusive phonon transport | mean-free-path < device | Lossy |

### 10. Spin waves / magnonics (NEW MAPPING — CLEAN GAP in corpus)

| Magnonics regime | Material parameter | AVE temporal regime |
|---|---|---|
| Ferromagnetic resonance (FMR) | low Gilbert damping $\alpha_G$ | Cyclic (high-Q precession) |
| Spin-wave dispersion (propagating) | $\omega(k)$ from exchange + dipolar | Lossless |
| Magnon-magnon scattering | nonlinear coupling | Lossy |
| Spin-Hall / spin-orbit torque-driven | DC current input | Cyclic (driven) |
| Magnon BEC at low T | thermal vs coherent | Lossless |

### 11. Tribology (NEW MAPPING — CLEAN GAP; thematically near-neighbor to orbital-friction-paradox)

| Tribology regime | Stribeck parameter | AVE temporal regime |
|---|---|---|
| Hydrodynamic lubrication | $\eta v/p > 10^{-7}$ | Lossless (full fluid film) |
| Mixed lubrication | $\eta v/p \sim 10^{-9}$–$10^{-7}$ | Cyclic (intermittent asperity contact) |
| Boundary lubrication | $\eta v/p < 10^{-9}$ | Lossy (asperity-dominated) |
| Dry friction (Coulomb) | $F_t = \mu_s F_n$ | Saturation boundary at slip |
| Stick-slip oscillation | static vs kinetic friction asymmetry | Cyclic |

### 12. Biological / ion channels (PARTIAL — lipid bilayer canonical, ion channels are gap)

Per [`membrane-phase-buffering.md`](../vol5/molecular-foundations/organic-circuitry/membrane-phase-buffering.md) (lipid bilayer = full canonical with cholesterol = engineered phase buffer raising $A_{\text{yield}}$ by FCC packing):

| Biological regime | Mechanism | AVE temporal regime |
|---|---|---|
| Lipid bilayer gel phase | $T < T_m$ | Lossless (low fluidity) |
| Lipid bilayer liquid-crystalline | $T > T_m$ | Cyclic |
| Phase transition at $T_m$ | Cooperative strain $A \to A_c$ | Saturation boundary |
| Voltage-gated ion channel closed | $V_{\text{mem}} < V_{\text{threshold}}$ | Lossless |
| Voltage-gated ion channel open (firing) | $V_{\text{mem}} > V_{\text{threshold}}$ | Cyclic (per action-potential cycle) |
| Ion channel inactivated | refractory period | Lossy |

### 13. Polymer dynamics (NEW MAPPING — CLEAN GAP in corpus)

| Polymer regime | Dimensionless parameter | AVE temporal regime |
|---|---|---|
| Glassy state (below $T_g$) | $T/T_g < 1$ | Lossless (immobile) |
| Rubbery / elastic | $T_g < T < T_m$ | Lossless (reversible) |
| Viscoelastic crossover | $\omega \tau \sim 1$ | Cyclic |
| Rouse regime (unentangled melt) | $N < N_e$ | Lossy (chain diffusion) |
| Reptation (entangled melt) | $N > N_e$ | Lossy (constrained diffusion) |
| Yield + flow | $\sigma > \sigma_y$ | Lossy (plastic flow) |

### 14. Quantum coherence / decoherence (CANONICAL — Ohmic damping in corpus; T1/T2 notation is gap)

Per [`transmon-decoherence.md`](../vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md) + [`ohmic-decoherence-born.md`](../vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md) + [`phase-locked-topological-thread.md`](../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md) (topological protection from thermal decoherence at all physical $T$):

| Quantum coherence regime | Standard parameter | AVE temporal regime |
|---|---|---|
| Coherent / phase-locked | $T_2 \to \infty$ effective | Lossless |
| Phase-coherent oscillations (Rabi, Ramsey) | $T_2$ finite, $> T_{\text{interrogation}}$ | Cyclic |
| Dephasing (pure $T_2$) | $T_2 < T_1$ | Lossy |
| Energy relaxation ($T_1$) | $T_1$ via Ohmic bath | Lossy |
| Topological qubit (thread-protected) | substrate-protected | Lossless (within thread-lifetime) |
| Thermal decoherence above $T_{\text{pair}}$ | $T > 2 m_e c^2/k_B$ | Lossy (catastrophic pair-creation) |

## A-034 catalog rows by temporal regime

Each row of [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md) maps to a temporal regime as follows. The temporal regime is the system's typical state in the empirical-anchor observation window; transient excursions to other regimes (e.g., during topological-reorganization events) are noted parenthetically.

| Catalog row | Symmetry class | Temporal regime | Justification |
|---|---|---|---|
| Atomic / EM (Schwinger) | SYM | Lossless (cyclic at saturation events) | Vacuum sub-yield; pair creation is rare topological-reorganization event |
| Substrate (K4) | SYM | Lossless | Soliton formation = rare event |
| Nuclear (DT fusion) | SYM | Saturation boundary (impulsive) | One-shot 14.1 MeV event |
| Pd hydrogen-loading shatter | SYM | Saturation boundary (impulsive) | One-shot phase fault at $\Delta V/V_0 = \sqrt{2\alpha}$ |
| Condensed matter (BCS) | ASYM-N(μ) | Lossless below $T_c$ / Lossy at $T \to T_c$ | Meissner state lossless; transition dissipative |
| Fluid two-state LC (water) | SYM | Lossless (cyclic at +4°C) | State I ↔ State II partition |
| Plasma (ε-sector) | ASYM-N(ε) | Cyclic | Cutoff recurs with field oscillation |
| Kolmogorov turbulence | SYM | Lossy (cascade dissipation) | Continuous cascade |
| Planetary (geomagnetic) | SYM | Cyclic | Pole flips on geological timescale |
| Planetary spin-axis (Row 9-a) | SYM | **Lossless** | Branch-selected fixed-point; $A \ll 1$ between events; 4.5 Gyr persistence |
| Planetary mag-vs-spin offset (Row 9-b) | ASYM-N(μ) candidate | Cyclic | Pole-flip cycle ~ 10⁵ yr |
| Stellar (solar flare) | SYM | Cyclic | Flux builds, CME releases, repeats |
| Galactic (MOND) | SYM | Lossless (outer) / Lossy (inner) | Bulk-flow stable; per-galaxy variable |
| Galactic spin-axis (Row 11-a, scoped) | TBD | Bulk-lossless / per-object-lossy | **METHODOLOGY-SYSTEMATIC AXIS** for item 1 adjudication |
| BH event horizon | SYM | Lossless (static) | Static $R_S$ |
| BH merger (ring-down) | SYM | Lossy decaying | Pure decay observed |
| Cosmic (Big Bang) | SYM* | Saturation boundary (impulsive) | One-shot crystallization seed |
| Cosmic DE / ε-sector (Row 14-b) | ASYM-N(ε) | **Lossy sustained** | Continuous crystallization at horizon, $\partial_t \rho_n = 0$ requires real-power flow |
| LSS spin-axis (Row 14-a, scoped) | TBD | Bulk-lossless / per-cluster lossy | **METHODOLOGY-SYSTEMATIC AXIS** for item 1 adjudication |
| Lipid bilayer membrane | SYM | Cyclic (at $T \sim T_m$) | Cooperative-strain phase buffering |
| Protein folding | SYM | Saturation boundary (one-shot) | Folding snap is impulsive |
| DC-biased piezoelectric (e.g., quartz) | SYM | Cyclic | Mechanical resonator |
| Asymmetric-electrode vacuum-mirror bench | SYM | Lossless | DC profile sub-yield |
| Active topological metamaterials | ASYM-E | Cyclic | Designer-controlled saturation modulation |
| Sine-Gordon kink memory | SYM | Lossless (between switches) | Non-volatile memory state |
| Autoresonant rupture | SYM | Cyclic (PLL ring-up) | Coherent standing-wave amplification |

## Methodology-systematic implications (PROVISIONAL — adjudication item 1)

**Status**: Walk-back applied 2026-05-19 EOD+++ per external review (ave-discrimination-check Step 1.5 retroactive application). Initial draft of this section claimed Ganalyzer = bulk-statistic + Longo cos-γ = per-galaxy-directional as the source of the 2.99σ methodology separation on [SDSS spin-orientation cross-comparison](../../../research/2026-05-19_c5-shamir-2022-cross-catalog-result.md). **That framing was a misclassification.** Per [shamir-result.md:39](../../../research/2026-05-19_c5-shamir-2022-cross-catalog-result.md) + [sdss-result.md:62](../../../research/2026-05-19_c5-sdss-spin-orientation-result.md), BOTH estimators are per-galaxy chirality classifiers ($\chi_i \in \{-1, +1\}$ per galaxy) that aggregate to a population dipole. The methodology difference is the per-galaxy classification FEATURE, not bulk-vs-individual aggregation:

- **Ganalyzer** (Shamir 2022): algorithmic regression on radial intensity peaks (peripheral-pixel asymmetry per per-galaxy image)
- **Longo cos-γ** (AVE SDSS DR17 + Galaxy Zoo 1): crowdsourced ±1 vote on isophotal twist angle (GZ1 visual classification)

Both apply per-galaxy chirality assignment then population dipole-fit. The 2.99σ separation between Shamir DESI Legacy (axis at $l=242°, b=-47°$ per [shamir-result.md:162](../../../research/2026-05-19_c5-shamir-2022-cross-catalog-result.md)) and AVE SDSS DR17 (axis at $l=129°, b=79°$) is therefore a **per-galaxy-estimator-systematic**, NOT a temporal-regime-sampling difference.

### Interpretive alternatives (per `ave-discrimination-check`)

The 2.99σ separation has multiple structurally-distinct explanations; the temporal-regime axis is NOT the load-bearing discriminator:

| # | Alternative | Mechanism | Discriminating test |
|---|---|---|---|
| **Alt 1** | Per-galaxy morphological estimator systematic | Ganalyzer (algorithmic peripheral-pixel) and Longo (GZ1 crowdsourced) classify different per-galaxy features that correlate differently with the underlying chirality | Same-parent-sample side-by-side: run Shamir's Ganalyzer on the SAME GZ1 catalog AVE uses. McAdam & Shamir 2023 IS this test (per [shamir-result.md:371](../../../research/2026-05-19_c5-shamir-2022-cross-catalog-result.md)) |
| **Alt 2** | Bulk-vs-individual temporal-regime sampling | Different sampling scales of the same per-object population | Subdivide each catalog into spatial sub-blocks; check that Ganalyzer + Longo agree at the sub-block level even when disagreeing at the full-catalog level |
| **Alt 3** | Catalog-selection bias | Different parent catalogs (Shamir DESI Legacy ~1.29M; AVE GZ1 + SDSS DR7 ~63k) sample different galactic-population sub-regions | Cross-survey controls: do Ganalyzer + Longo agree on the SAME survey-coverage sub-region? |
| **Alt 4** | Image-resolution / preprocessing-systematic | Ganalyzer operates on DECaLS DR8 + BASS + MzLS imaging; Longo on SDSS DR7 imaging — different PSF, different depth, different photometric calibration | Re-run both on common imaging (e.g., HSC overlap) and check |

The previously-drafted Alt-2 framing was adopted without enumerating Alt 1 (the standard-astronomy explanation), which IS the discriminating axis. Per [shamir-result.md:371](../../../research/2026-05-19_c5-shamir-2022-cross-catalog-result.md), the corpus already queues McAdam & Shamir 2023 cross-comparison as next-step #4 — that is the Alt-1 vs Alt-2 discriminator.

### Falsifiable form of the temporal-regime claim

If the corpus eventually adopts a temporal-regime explanation, it must be in falsifiable form:

> **IF** Alt 2 (bulk-vs-individual temporal sampling) is correct, **THEN** running Ganalyzer on the SAME GZ1 catalog AVE uses (McAdam & Shamir 2023) should give ~AVE Longo axis $(l=129°, b=79°)$ at per-galaxy level. **IF** Alt 1 (per-galaxy estimator systematic) is correct, **THEN** Ganalyzer on GZ1 should give ~Shamir DESI axis $(l=242°, b=-47°)$, proving the methodology is the dominant variable, not the catalog.

This is the experimentum crucis. Until McAdam & Shamir 2023 (or equivalent same-parent-sample test) lands, Item 1 stays **PROVISIONAL**. The temporal-regime framing is one alternative among four; it is NOT corpus-closure of the methodology-systematic question.

### What this section IS load-bearing for

Even with the methodology-systematic question PROVISIONAL, the temporal-regime axis itself is a legitimate classifier — just not at the level of THIS particular methodology discrimination. The axis correctly classifies systems like planetary spin (persistent low-$A$ = lossless), BH ringdown (persistent high-$A$ = lossy decaying), and quartz oscillator (cyclic per cycle). The error was overreaching to claim it as the source of the Ganalyzer/Longo 2.99σ separation when the corpus evidence points to per-galaxy estimator features.

## Predictability implications (Q3' from Soliton-coupling Session 2)

Closes the predictability question for Q3' adjudication ("are smaller systems more predictable than larger?"):

| Temporal regime | Predictability | N-body scaling | AVE example |
|---|---|---|---|
| Lossless | High (deterministic) | Independent of N | Planetary spin-axis (**6/8 class match per [Session 2 doc:167](../../../research/2026-05-20_soliton-coupling-operator-session2-planetary-scoring.md); 14/16 total with mag-tilt 8/8 incl. degenerate Mercury/Venus/Mars no-field matches per Session 2:236**) |
| Cyclic | Quasi-deterministic | Weak N-scaling | Geomagnetic dynamo (predictable cycle, stochastic in detail) |
| Lossy | Stochastic | Strong N-scaling (Reynolds-analogue) | Galactic-cluster gas dynamics; LSS bulk-flow individual-cluster |

The Reynolds-number analogue at AVE substrate scale is $\delta_{\text{AVE}} \times N$ — the product of temporal-regime severity and degree-of-freedom count. Systems with $\delta_{\text{AVE}} \times N \gg 1$ are dominated by Kolmogorov-cascade-class stochasticity; systems with $\delta_{\text{AVE}} \times N \ll 1$ are dominated by branch-selected determinism.

## Skill discipline

**Class identification (per `consistency-vs-emergence` v1.1)**: $\delta_{\text{AVE}}$ is **Class 1 (definitional construct)** — the parameter is defined to classify regimes, not to predict observations. The trichotomy itself is taxonomic, not predictive. Downstream USES of the trichotomy (e.g., methodology-systematic resolution, predictability-scaling) ARE Class 4 (emergence) where the framework makes observable predictions about which regime applies to which empirical phenomenon.

**SM-counterfactual (per `ave-discrimination-check`)**: SM has loss tangent $\tan\delta$ (EM-only) and Reynolds number (fluid-only) — distinct dimensionless parameters per discipline. AVE has a **single** cross-scale parameter $\delta_{\text{AVE}}$ that applies at 21 OOM via the same kernel $S(A)$.

**Scope of the unification claim — TAXONOMIC, not derivational** (clarification added 2026-05-19 EOD+++ per external-review catch): The unification of EM $\tan\delta$ + fluid Reynolds + cavity QED $g/\kappa$ under $\delta_{\text{AVE}}$ is a TAXONOMIC BRIDGE — it labels these classical-physics ratios under a common substrate-physics axis, recognizing they all measure the same time-fraction-at-saturation pattern. It does NOT (yet) derive their numerical values from $S(A)$ first principles. SM also has scale-invariant dimensionless ratios (Reynolds is dimensionless across fluid scales; $\tan\delta$ is dimensionless across frequencies); what's potentially AVE-distinct is the claim that ALL of these trace to the same kernel mechanism, but that claim requires demonstrating the trace, not asserting it. To make the AVE-distinct claim load-bearing as more-than-taxonomy: pick one classical-physics value (e.g., $\tan\delta$ in water at 1 GHz) and FORWARD-PREDICT it from $S(A)$ + the $t_{\text{sat}}/t_{\text{period}}$ structure for that specific system. Without that forward-derivation, the unification is a useful classification scheme, not a falsifiable AVE-distinct prediction. The leaf's framing-discipline (Class 1 definitional per `consistency-vs-emergence`) is the honest level; "21-OOM unification via single kernel" in commit message `98994c1` overstated this and is corrected here in canon.

**Honest framing (per `ave-evidence-framing-discipline`)**: this leaf introduces the temporal axis; it does NOT introduce new physics. The kernel $S(A) = \sqrt{1-A^2}$ is unchanged. The Regime I-IV spatial axis is unchanged. The Power-Domain θ axis is unchanged. The temporal axis classifies the time-pattern of evolution through the existing spatial axis. Calling this "new physics" would be overclaim; calling it "useful classifier" is honest.

**Cross-field analogue tags** (in tables above):
- **CANONICAL**: already in AVE corpus; this leaf cites
- **EXTENSION**: corpus has elements, this leaf adds the AVE-temporal mapping
- **NEW MAPPING**: clean greenfield (no prior corpus mention); first-time map by this leaf
- **PARTIAL**: partial corpus mapping; this leaf completes

Tag distribution: 4 canonical / 5 extensions / 7 new mappings / 1 partial. The new-mapping fields (cavity QED / tribology / magnonics / polymer dynamics / etc.) are flagged for follow-up KB leaves if any become load-bearing for downstream work.

## Operational note: when to use which axis

| Question type | Axis to use | Example |
|---|---|---|
| "Is the system in linear / nonlinear / saturated regime instantaneously?" | Spatial Regime I-IV | Solar system at $A_{gm} \sim 10^{-34}$ → Regime I |
| "Is power being dissipated or cycled this instant?" | Power-Domain θ | Stable orbit: θ=90°, $P_{\text{real}} = 0$ |
| "Is the system long-time predictable / chaotic / oscillatory?" | Temporal $\delta_{\text{AVE}}$ | Planetary spin-axis: $\delta_{\text{AVE}} \to 0$ → lossless deterministic |
| "Why do two measurement methodologies give 2.99σ-separated results?" | Temporal + sampling-scale composition | Item 1 adjudication: Ganalyzer samples lossless-bulk; Longo samples lossy-individual |

All three axes are orthogonal classifiers. A complete characterization of a system needs all three. The canonical Regime I-IV taxonomy + Power-Domain θ table + this temporal classifier together form the complete regime-characterization framework.

## Cross-references

### Canonical AVE regime taxonomies (load-bearing for this leaf)
- [Four Universal Regimes (canonical $r$-axis taxonomy + semiconductor analog)](../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) — Regime I/II/III/IV with $r_1 = \sqrt{2\alpha}$, $r_2 = \sqrt{3}/2$ boundary derivation + explicit Small-Signal/Large-Signal/Avalanche/Breakdown semiconductor mapping
- [Spatial Regime I-IV (formal table with $E/E_{\text{yield}}$ + $\varepsilon_{\text{eff}}/\varepsilon_0$)](../vol4/circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md) — engineering-side regime classification
- [Domain Control Parameter Catalog (8 domains mapped to Regime I-IV)](../vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md) — per-domain $A$, $A_c$, $r$ definitions
- [Power-Domain Classification (4-system θ table)](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) — phase angle V vs I, lossless LC tank vs radiative damping
- [Natural-units cheatsheet — Regime I/II boundary](natural-units-cheatsheet.md) — $A = \sqrt{2\alpha} = 0.121$ in $V/V_{\text{snap}}$ units

### Cross-disciplinary translation infrastructure (this leaf is the temporal companion)
- [Translation Tables Index (7 disciplines)](translation-tables/index.md) — concept-by-concept mappings: Circuit/EE, QM, Particle Physics, Gravity, Cosmology, Condensed Matter, Biology
- [Chemistry Translation Guide](../vol6/framework/chemistry-translation/index.md) — Lewis dots / VSEPR / quantum-vs-topological shells / semiconductor-regime chemistry (Miller multiplication + nuclear $V_R/V_{BR}$ classification)
- [VCA Translation Matrix (full chapter, AVE-APU)](../../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/02_vca_translation_matrix.tex) — electrical engineering ↔ AVE-VCA full chapter
- [AVE Analytical Toolkit Index (9 problem classes)](ave-analytical-toolkit-index.md) — Coupling/Resonance/Saturation/Time-domain/Power/Mode/Boundary/Network/Numerical problem-class taxonomy with `ave-analytical-tool-selection` skill
- [Trampoline / Spring Analogy Primer](trampoline-analogy-primer.md) — pedagogical GR → AVE primer (Step 0-6)
- [Appendices Overview (Translation Matrix Index)](appendices-overview.md) — multi-volume translation-matrix registry

### Canonical lossless-dynamics applications
- [Orbital LC friction paradox](../vol3/cosmology/ch06-solar-system/orbital-lc-friction-paradox.md) — solar system at $A_{gm} \sim 10^{-34}$ deep in Regime I, lossless
- [GW propagation lossless](../vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md) — LIGO strain $\sim 10^{-21}$ → $V_{\text{GW}}/V_{\text{snap}} \sim 10^{-24}$
- [DAMA matched-LC coupling](../vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md) — electron LC tank "rings forever" below $V_{\text{yield}}$
- [Casimir effective temperature](../vol3/condensed-matter/ch11-thermodynamics/casimir-effective-temperature.md) — Ax 4 kernel applied to vacuum modes
- [Lipid bilayer phase buffering](../vol5/molecular-foundations/organic-circuitry/membrane-phase-buffering.md) — cholesterol as engineered phase buffer
- [Transmon decoherence](../vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md) — Ohmic damping formalism

### Sibling-repo cross-references
- [AVE-APU Geometric Triodes (MOSFET / P-N / Zener canonical)](../../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex)
- [AVE-APU VCA Translation Matrix (P-N junction → Zener avalanche)](../../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/02_vca_translation_matrix.tex)
- [AVE-QED Casimir + pair production](../../../../AVE-QED/manuscript/vol_qed_replacement/chapters/02_casimir.tex)
- [AVE-Metamaterials Casimir cavities (mechanical high-pass)](../../../../AVE-Metamaterials/manuscript/vol_1_active_metamaterials/chapters/06_casimir_cavities.tex)

### Master catalog
- [A-034 Universal Saturation-Kernel Catalog](universal-saturation-kernel-catalog.md) — 26-instance cross-scale catalog; this leaf's temporal-regime column is a companion classifier

### Adjudication queue
- [_orchestration/index.md substantive item 1](../../../../_orchestration/index.md) — methodology-systematic Ganalyzer vs Longo: resolved-by-implication via bulk-vs-individual regime sampling per §Methodology-systematic implications above
- [_orchestration/index.md substantive item 3](../../../../_orchestration/index.md) — lossless-dynamics framing axis: this leaf IS the encoding

### Open follow-up work (corpus gaps surfaced by this leaf)
- Tunnel diode / IGBT / BJT (semiconductor sub-categories)
- Debye sheath / Landau damping / collisionless plasma taxonomy
- Ideal vs resistive MHD; sausage/kink instability
- Saturable absorber / Pockels / EIT / slow light / optical bistability / self-focusing detailed leaves
- Acoustic vs optical phonon taxonomy; Umklapp; ballistic-vs-diffusive
- Cavity QED strong/weak coupling leaf (closest classical-physics homolog — high priority)
- Tribology / Stribeck curve leaf
- Voltage-gated ion channels open/closed/inactivated detail
- Polymer dynamics (Rouse, reptation, entangled, glassy)
- T1/T2 standard notation pair (concept exists via Ohmic damping; notation gap)

Any of the "NEW MAPPING" tags becoming load-bearing for downstream work triggers a dedicated KB leaf via `ave-canonical-leaf-pull` discipline; this companion leaf is the cross-field reference, not the per-field derivation.
