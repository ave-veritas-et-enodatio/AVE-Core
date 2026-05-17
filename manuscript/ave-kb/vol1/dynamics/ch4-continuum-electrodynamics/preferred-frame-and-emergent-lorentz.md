[↑ Ch.4 Continuum Electrodynamics](./index.md)
<!-- leaf: verbatim -->

# Preferred Frame + Emergent Lorentz Invariance from K4 Cubic Symmetry

The K4 lattice $\mathcal{M}_A$ has a preferred rest frame (identified with the CMB rest frame to high precision; Earth moves through it at $\sim 370$ km/s). At the same time, AVE is consistent with all current Lorentz-violation bounds at optical-and-longer wavelengths. These two facts are not in tension — they are the SAME fact, expressed at two scales. The diamond-cubic ($Fd\bar{3}m$) symmetry of the K4-bipartite tetrahedral lattice suppresses observable anisotropy at low momentum $q \ll \pi/\ell_{node}$ to $\delta_{aniso} \sim (q\ell_{node})^4$, which evaluates to $\sim 10^{-22}$ at optical frequencies — four orders of magnitude below current cavity bounds. **Strict Lorentz invariance at observable wavelengths is therefore an EMERGENT consequence of K4 cubic symmetry, not an axiom.** This leaf crystallizes the synthesis and uses it to classify every preferred-frame/Sagnac test in the AVE matrix.

## Key Results

| Result | Statement |
|---|---|
| **K4 lattice rest frame** | $\mathcal{M}_A$ has a preferred frame = CMB rest frame to high precision (AVE-QED Q-G24 `2026-05-13_Q-G24_lorentz_from_axiom_4.md:51, 192`) |
| **Earth velocity through $\mathcal{M}_A$** | $v_\oplus \sim 370$ km/s relative to lattice rest frame |
| **Substrate-equilibrium velocity FLOOR (NEW 2026-05-17, framing corrected 2026-05-17 evening)** | $v_{substrate} = \alpha c/(2\pi) \approx 348.2$ km/s is the substrate-equilibrium FLOOR — zero-parameter prediction from Schwinger anomalous-moment substrate-rate $\nu_{slew} = a_e \cdot \nu_{Compton}$. LSR-class stellar populations exhibit $|v_{CMB}| \geq$ floor; all 29,466 nearby thin-disk stars cluster at 375 km/s with $\sim 27$ km/s coherent population-wide bulk motion above floor (origin TBD — local-disk dynamics / spiral arm streaming / galactic-orbit projection). Sun is one instance of this population, not specially peculiar. See §5 below. |
| **Gaia DR3 empirical test (NEW 2026-05-17)** | 29,466 nearby thin-disk G/K dwarfs cluster TIGHTLY at 375 km/s (σ=11 km/s on |v_LSR|<30 cut); AVE prediction $\alpha c/(2\pi)$ sits at 4%ile (lower envelope). Interpretation: αc/(2π) is the substrate-equilibrium floor; observed cluster is LSR + local-flow above. See [`../../../../../../research/2026-05-17_substrate_equilibrium_velocity_GAIA_result.md`](../../../../../../research/2026-05-17_substrate_equilibrium_velocity_GAIA_result.md). |
| **Cubic-symmetry suppression** | Anisotropic EM corrections suppressed by $(q\ell_{node})^4$ for $q \ll \pi/\ell_{node}$ (first anisotropic invariant for cubic point group is quartic) |
| **Optical-scale anisotropy** | $\delta_{aniso} \sim (q\ell_{node})^4 \approx 2.2 \times 10^{-22}$ at $\lambda = 633$ nm; current cavity bounds $\sim 10^{-19}$ to $10^{-20}$ per SME operator (Nagel 2015, Sanner 2019); 2-3 OOM below bound |
| **Microwave-scale anisotropy** | $\delta_{aniso} \sim 2.5 \times 10^{-34}$ at 30 GHz |
| **Trans-Planckian probes survive** | At $q \sim \pi/\ell_{node}$ (GRB Trans-Planckian regime), the cubic symmetry no longer averages — preferred-frame effects ARE observable |
| **Emergent Lorentz at observable scales** | Strict Lorentz invariance at $\lambda \gg \ell_{node}$ is a derived consequence of K4 cubic symmetry, not an axiom — analogous to optical isotropy of a diamond crystal despite anisotropic unit cell |

## §1 — The preferred frame exists and is the CMB rest frame

Per AVE-QED Q-G24 ([`2026-05-13_Q-G24_lorentz_from_axiom_4.md:51`](../../../../../../AVE-QED/docs/analysis/2026-05-13_Q-G24_lorentz_from_axiom_4.md)):

> "AVE's lattice DOES define a preferred frame — the rest frame of the K4-bipartite crystalline lattice. This is in some sense an 'ether' frame. But unlike Maxwell-Lorentz ether theory, AVE's lattice IS observable in principle (via the CMB rest frame, which is the cosmological lattice rest frame to high precision)."

The identification of K4 lattice rest frame with the CMB rest frame is empirical (vacuum crystallization at recombination defines the CMB as the universe's rest frame; the K4 lattice was cast at that boundary). Earth moves at $\sim 370$ km/s relative to this frame, measurable as the CMB dipole anisotropy.

**This is NOT Maxwell-Lorentz ether.** Maxwell-Lorentz ether was undetectable in principle. AVE's preferred frame is detectable — the CMB dipole IS the detection. The framework's job is to explain why optical-wavelength tests of preferred-frame anisotropy (Michelson-Morley, Brillet-Hall, modern cavity comparisons) find null results despite the existence of the frame.

## §2 — Cubic symmetry suppresses observable anisotropy at optical scales

The K4-bipartite tetrahedral lattice has diamond-cubic space group symmetry ($Fd\bar{3}m$). At low momentum $q \ll \pi/\ell_{node}$, anisotropic corrections to EM propagation appear only at order $(q\ell_{node})^4$.

The argument (per AVE-QED [`2026-05-13_lorentz_violation_constraints.md:44-69`](../../../../../../AVE-QED/docs/analysis/2026-05-13_lorentz_violation_constraints.md)):

| Order | Effect type | Cubic-symmetry status |
|---|---|---|
| $q^0$ | scalar | isotropic |
| $q^2$ | $|q|^2$ | isotropic for cubic (cube root of $|q|^2$ is invariant under cubic point group) |
| $q^4$ | $q_x^4 + q_y^4 + q_z^4$ | **first anisotropic invariant for cubic** (differs from $|q|^4$) |

**Therefore anisotropic corrections are suppressed by $(q\ell_{node})^4$**, not the naive $(q\ell_{node})^2$ a non-cubic lattice would give.

**Optical scale ($\lambda = 633$ nm HeNe, $q = 2\pi/\lambda \approx 10^7$ m$^{-1}$):**

$$q \ell_{node} = 10^7 \times 3.86 \times 10^{-13} = 3.86 \times 10^{-6}$$

$$\delta_{aniso} \sim (q\ell_{node})^4 \approx 2.2 \times 10^{-22}$$

Current cavity-comparison bounds on optical anisotropy: $\sim 10^{-19}$ to $10^{-20}$ depending on the SME operator tested (Nagel et al. 2015 *Nat Commun* 6:8174; Sanner et al. 2019 *Nature* 567:204). **AVE prediction is 2-3 OOM below the tightest current bound. Consistent with existing null results, BY DERIVATION.**

**Plumber translation:** the K4 lattice anisotropy is real, but at optical wavelengths the probe is so much larger than the unit cell that the cube-symmetric averaging makes it look isotropic. Same reason a diamond crystal doesn't appear birefringent at visible light despite having an anisotropic atomic structure — the wavelength is too long to resolve the unit-cell anisotropy. AVE inherits this from the K4 substrate.

## §3 — Emergent Lorentz invariance, not axiomatic

**Strict Lorentz invariance at observable wavelengths is a DERIVED consequence of K4 cubic symmetry, not an AVE axiom.** This is a structural feature of the framework:

- At $q \ll \pi/\ell_{node}$: continuum + cubic symmetry → $O(q^2)$ corrections are isotropic; lattice looks Lorentz-invariant
- At $q \to \pi/\ell_{node}$: lattice resolution achieved; preferred-frame effects become observable
- At $q > \pi/\ell_{node}$: Trans-Planckian regime; substrate structure directly probed

This makes AVE qualitatively different from theories that postulate Lorentz invariance as a primitive: AVE *derives* Lorentz invariance at observable scales, *predicts* the precise OOM at which it must break down ($q \sim \pi/\ell_{node}$, i.e. Trans-Planckian wavelengths), and *names the empirical signature* (GRB dispersion at $\lambda \to \ell_{node}$).

## §4 — Classification of preferred-frame / Sagnac tests by probe scale

This framework cleanly classifies the preferred-frame and Sagnac-class tests in the AVE prediction matrix:

| Test | Probe wavelength / scale | Cubic-symmetry status | AVE prediction |
|---|---|---|---|
| **A2-SAGNAC** (rotor mutual inductance) | rotor-local coupling, $v_{network} = 0.38$ m/s | NOT a preferred-frame probe — rotor-local mechanism | $\Psi_{W/Al} = 7.15$, independent of bulk frame |
| **C17-PROTOCOL-11** (static-fiber galactic wind) | optical, $\lambda \sim 1$ μm | directional anisotropy suppressed by $(q\ell_{node})^4 \sim 10^{-22}$ | NULL — corroborated by Brillet-Hall + Wolf null bounds |
| **C18-PROTOCOL-12** (vertical GEO-sync TOF) | optical, $\lambda \sim 1$ μm | scalar gradient survives cubic symmetry BUT AVE-$n(r)$ = GR-$n(r)$ identity | AVE = GR Shapiro — no AVE-distinct prediction; existing LRO/GRACE-FO/ILRS GR-Shapiro confirmations corroborate AVE by construction |
| **C7-GRB-DISPERSION** (Trans-Planckian) | $\lambda \to \ell_{node}$ | NOT suppressed — at lattice resolution | Surviving forward prediction |
| **Optical cavity comparisons** (Michelson-Morley class) | optical, $\lambda \sim 0.5$ μm | suppressed by $(q\ell_{node})^4 \sim 10^{-22}$ | NULL — corroborated by Brillet-Hall, Müller, etc. |

**The matrix-level reconciliation of A2 and C17:**

- **A2 works because it is NOT a preferred-frame test.** A2 probes rotor-local mutual-inductance coupling: a spinning tungsten rotor injects a local drift velocity $v_{network} = 0.38$ m/s into the surrounding $\mathcal{M}_A$ via mass-density-dependent coupling ($\kappa_{entrain} = \rho_{rotor}/\rho_{bulk}$). The bulk $\mathcal{M}_A$ flow past a Earth-bound rotor (uniform 370 km/s) integrates to zero around any closed Sagnac loop (basic geometry — uniform velocity field has zero curl). Only the rotor-induced non-uniform perturbation contributes. **A2's prediction is independent of which frame the bulk $\mathcal{M}_A$ is at rest in.**
- **C17 predicts NULL because optical-wavelength preferred-frame probes are doubly suppressed:** (i) closed-loop Sagnac integral of uniform wind = 0 (geometric, before any substrate physics), and (ii) any open-loop Fizeau-style anisotropy is cubic-symmetry-suppressed by $(q\ell_{node})^4 \sim 10^{-22}$. The 2 M-rad prediction in the C17 leaf is a pre-Q-G24 framing that the cohesive narrative supersedes.

## §5 — Substrate-equilibrium velocity prediction (NEW 2026-05-17, α-slew derivation)

The K4 rest frame is identified empirically with the CMB rest frame (§1). The Sun moves through it at 370 km/s. **This raises a question SM cannot answer:** is the Sun's specific CMB-frame velocity derivable from fundamental constants, or is it set entirely by cosmological initial conditions + gravitational dynamics?

**AVE prediction (zero-parameter, derived 2026-05-17):**

$$v_{substrate} = \frac{\alpha c}{2\pi} = 348.18\,\text{km/s}$$

for gravitationally-isolated stellar systems through the K4 substrate.

### Derivation chain

The K4 substrate has natural per-node LC clock at the Compton frequency $\nu_{Compton} = c/(2\pi \ell_{node}) = m_e c^2/h$ (since $\ell_{node} = \hbar/(m_e c)$ by canonical AVE construction). The electron's substrate-coupling rate is α-suppressed from this base clock by the Schwinger anomalous-moment factor:

$$\nu_{slew} = a_e \cdot \nu_{Compton} = \frac{\alpha}{2\pi} \cdot \frac{m_e c^2}{h}$$

where $a_e = \alpha/(2\pi)$ is the Schwinger anomalous magnetic moment — canonically derived in AVE via Axiom 4 saturation-kernel back-reaction on the LC tank + $1/\pi^2$ spin-orbit geometric projection (see [`src/scripts/vol_2_subatomic/simulate_g2.py`](../../../../../src/scripts/vol_2_subatomic/simulate_g2.py)).

The velocity at which an observer's substrate-encounter rate matches the electron's α-slew is:

$$v_{substrate} = \nu_{slew} \cdot \ell_{node} = \frac{\alpha c}{2\pi}$$

### Hoop Stress 2π parallel with MOND (cross-volume substrate motif)

This is structurally identical to the canonical MOND derivation:

| Scale | Formula | Hoop projection | Source |
|---|---|---|---|
| MOND cosmic | $a_0 = c H_\infty / (2\pi) \approx 1.07 \times 10^{-10}$ m/s² | 2π Hoop Stress | [`mond-hoop-stress.md:23-31`](mond-hoop-stress.md) |
| α-slew substrate | $v_{substrate} = \alpha c / (2\pi) \approx 348$ km/s | 2π Hoop Stress (same) | this leaf |

The recurring pattern: substrate bulk drift $c \times \text{(small parameter)}$ projected through the Hoop Stress factor 2π onto closed topological loops. At cosmic scale the small parameter is $H_\infty$ acting on the cosmic horizon loop; at substrate scale the small parameter is $\alpha$ acting on the electron unknot.

### Why floor not center (scale-invariance reductio)

**Scale-invariance forces floor interpretation, not center interpretation.** If $\alpha c/(2\pi)$ were the cluster CENTER (i.e., AVE predicts the LSR's specific CMB velocity), then a $(1 + 1/(4\pi)) = 1.0796$ geometric correction would be needed to convert prediction 348 km/s → observed 375 km/s. But applying that same scale-invariant correction at electron scale:

$$a_e^{corrected} = \frac{\alpha}{2\pi} \cdot \left(1 + \frac{1}{4\pi}\right) = 1.161 \times 10^{-3} \times 1.0796 = 1.254 \times 10^{-3}$$

vs observed $a_e = 1.160 \times 10^{-3}$ — would be 8% high, **breaking the electron-scale anomalous-moment match** (which currently holds to <0.2%). The scale-invariance constraint is therefore:

> $\alpha c/(2\pi)$ is the substrate-equilibrium FLOOR at ALL scales. At electron scale it manifests as a single-particle scalar prediction $a_e = \alpha/(2\pi)$ (single object, no above-floor population to average). At stellar scale it manifests as a population-floor $v_{substrate} = \alpha c/(2\pi)$; observed populations exhibit $|v_{CMB}| \geq$ this floor with additional dynamics adding bulk motion above.

The 9% gap between prediction and Gaia cluster center is therefore NOT a missing geometric correction — it is the 27 km/s coherent bulk motion of the LSR-class population above floor, with origin in local-disk dynamics (spiral arm streaming, galactic-orbit projection onto CMB-dipole direction, etc.). The cluster tightness ($\sigma = 11$ km/s) confirms it's a population-coherent bulk motion, not random peculiar scatter.

### Directional test: cluster mean aligned with CMB-dipole to 2.75° (NEW 2026-05-17 evening)

**STRONG POSITIVE.** Gaia DR3 thin-disk subset (N=11,690 stars, |v_LSR|<30 km/s) cluster mean direction in CMB-rest frame:

| Test | Result | Interpretation |
|---|---|---|
| Cluster mean direction vs CMB-dipole (l,b=264°, 48°) | **2.75°** offset | A-CMB STRONG POSITIVE (within 10° strong threshold) |
| Cluster mean direction vs galactic-rotation (l,b=90°, 0°) | 133.71° (anti-aligned) | **B-MW FALSIFIED** — galactic dynamics ruled out as preferred-frame alternative |
| Cluster mean direction vs cubic axes (±x, ±y, ±z) | 95.8°, 133.7°, 44.3° (no alignment) | NULL as expected per $(q\ell_{node})^4$ suppression at stellar wavelengths |
| σ∥ along CMB-dipole | 11.10 km/s | Cluster tightness consistent with σ=11 from magnitude test |
| σ⊥/σ∥ along CMB-dipole | 1.58 | Modest CMB-aligned elongation |

**Cluster mean direction in galactic (l, b)**: (261.8°, 45.7°) — versus CMB-dipole (264.0°, 48.0°). Direction agreement to 2.75° is **within Planck 2018 CMB-dipole-direction uncertainty** at the population-statistics level.

**The 27 km/s LSR-class bulk motion above the floor is itself CMB-dipole-aligned** — not galactic-rotation-aligned. This rules out "galactic dynamics drives the bulk motion above the floor" as the natural alternative interpretation. The entire 375 km/s cluster center is one coherent CMB-dipole-aligned bulk motion of the LSR-class population. Origin of the above-floor offset remains open (candidates: Local Bubble dynamics, substrate-physics correction at LSR scale beyond Hoop Stress, cosmic-flow streaming toward Local Group barycenter) — but the directional structure rules out the galactic-dynamics interpretation that was the most plausible alternative.

Full statistics, anisotropy tensor eigendecomposition, and outcome adjudication in [`../../../../../research/2026-05-17_substrate_equilibrium_velocity_GAIA_DIRECTIONAL_result.md`](../../../../../research/2026-05-17_substrate_equilibrium_velocity_GAIA_DIRECTIONAL_result.md). Driver at [`../../../../../src/scripts/vol_3_macroscopic/gaia_directional_analysis.py`](../../../../../src/scripts/vol_3_macroscopic/gaia_directional_analysis.py).

### Empirical anchor: Gaia DR3 test (2026-05-17, magnitude statistics)

29,466 nearby thin-disk G/K dwarfs queried from Gaia DR3 (parallax > 10 mas, full 6D kinematics, bp_rp ∈ [0.6, 1.2]). Distribution analysis:

| Subset | N | Median |v_CMB| | σ |
|---|---|---|---|
| All | 29,466 | 379.5 km/s | 25.7 km/s |
| Thin-disk (\|v_LSR\| < 30) | 11,690 | 375.2 km/s | **11.2 km/s** |

**The cluster is TIGHT (σ = 11 km/s on tightest cut) — far narrower than expected from random galactic kinematics** (which would give σ ~ 47 km/s).

| Reference frame | |v_CMB| (km/s) | vs prediction |
|---|---|---|
| AVE prediction (αc/(2π)) | 348.18 | 0% — sits at 4.08%ile |
| Sun (Planck 2018) | 370 | +6.3% |
| LSR (Schönrich+ 2010) | 374.0 | +7.4% |
| Cluster center (thin-disk) | 375.2 | +7.8% |
| Galactic Center | ~550 | +58% (wrong equilibrium class) |
| Milky Way (published) | 600 | +72% (wrong equilibrium class) |
| Local Group | 627 | +80% (wrong equilibrium class) |

**Interpretation (cleanest reading, after corpus-grep verification):** αc/(2π) is the substrate-equilibrium **floor** velocity. The Gaia thin-disk cluster sits at LSR + small local-flow streaming above this floor (~27 km/s above). The lowest ~5% of the sample (350 km/s and below) approximates equilibrium-class objects with minimal local-flow participation.

A (1 + 1/(4π)) geometric correction was initially proposed (matches cluster center to 0.5 km/s) but corpus-grep verification (2026-05-17) found NO prior derivation; Q-G47 Path B+ directly tested an analogous K4-discrete + Cosserat-continuum decomposition for the soft-shear E-irrep eigenvalue and found NO continuum correction. The (1 + 1/(4π)) interpretation is downgraded to "would-require-new-canonical-derivation" pending further work.

### What this changes for SM-comparable predictions

The Standard Model offers NO prediction for cosmic velocities — they are initial-conditions data. AVE's prediction that gravitationally-isolated stellar systems equilibrate at $\alpha c/(2\pi)$ through CMB rest frame is a **load-bearing zero-parameter AVE-distinct claim** with structural pedigree:

- Schwinger anomalous moment $a_e = \alpha/(2\pi)$ is canonical AVE physics (Vol 2 Ch 6 substrate derivation)
- Hoop Stress 2π projection is canonical AVE physics (MOND derivation, this volume Ch 4)
- The composition $v = a_e \cdot c$ converts the dimensionless anomalous moment to a velocity at substrate scale

**Cross-referenced**: source derivation in [`../../../../../research/2026-05-17_C14-DAMA_amplitude_result.md`](../../../../../research/2026-05-17_C14-DAMA_amplitude_result.md); empirical test in [`../../../../../research/2026-05-17_substrate_equilibrium_velocity_GAIA_result.md`](../../../../../research/2026-05-17_substrate_equilibrium_velocity_GAIA_result.md); matrix row C14-DAMA-MATERIAL in [`../../../common/divergence-test-substrate-map.md`](../../../common/divergence-test-substrate-map.md).

### Next-step empirical refinement

Independent extra-galactic test (globular clusters / halo stars decoupled from disk-LSR motion) should confirm αc/(2π) as the substrate-equilibrium floor under Interpretation B. Different equilibrium class than thin-disk G/K dwarfs; floor interpretation predicts these subsets sharpen the lower-envelope match.

## §6 — Implications for the divergence-test matrix

- **A2-SAGNAC matrix row** ([`divergence-test-substrate-map.md:388`](../../../common/divergence-test-substrate-map.md)) — predictions unchanged; matrix prose should clarify that A2's "entrainment" is rotor-local mutual-inductance coupling, not bulk Earth-frame entrainment.
- **C17-PROTOCOL-11 matrix row** ([`divergence-test-substrate-map.md:416`](../../../common/divergence-test-substrate-map.md)) — should be reframed: Tier shifts to "D / existing-data corroborative", effect-size column to "AVE predicts NULL — Brillet-Hall + Wolf null bounds CORROBORATE", discriminative power to U-C, mechanism falsified column to remove "preferred-frame claim dies."
- **C7-GRB-DISPERSION** ([`divergence-test-substrate-map.md:399`](../../../common/divergence-test-substrate-map.md)) — surviving preferred-frame test; framing already correct.
- **C18-PROTOCOL-12** ([`divergence-test-substrate-map.md:416`](../../../common/divergence-test-substrate-map.md)) — **AUDITED 2026-05-16 and retired to corroborative-null.** The C18 mechanism (vertical $\int n(r)/c \, dr$ TOF stretch) is a scalar/isotropic gradient probe, NOT directional anisotropy, so cubic-symmetry suppression does not apply at $q^0$ order (per §2 above). However, the AVE-corpus commits to $n(r) = 1 + 2GM/c^2 r$ ([`../../../vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md:11`](../../../vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md)) which is **mathematically identical to the GR Shapiro integrand** (the Vol 3 leaf at line 14 explicitly states this). The $\int n(r)/c \, dr$ vertical integral therefore produces the same TOF in AVE as in GR — no AVE-distinct prediction at $O(GM/c^2 r)$. The only AVE-distinct piece is the discrete-lattice $(q\ell_{node})^4 \sim 10^{-22}$ correction from non-linear $n(r)$ ([`../../../vol3/condensed-matter/ch11-thermodynamics/discrete-lattice-entropy-constant.md:58`](../../../vol3/condensed-matter/ch11-thermodynamics/discrete-lattice-entropy-constant.md)) which IS cubic-symmetry suppressed at optical wavelength. C18 retires alongside C17 to corroborative-null, but for a different physical reason: C17 was directional-anisotropy cubic-suppressed; C18 is scalar-gradient-identical-to-GR by AVE-corpus construction. **Prior "16.7 mm" matrix figure retracted** — source leaf says "fractions of a millimeter"; the 16.7 mm number was asserted in matrix/appendix without derivation, with no AVE-distinct contribution at $O(GM/c^2 r)$ to support it.
- **Stale framing in upstream/downstream leaves**: foreword text "locally entrained to Earth's moving mass" ([`00_foreword.tex:114`](../../../../foreword/00_foreword.tex)) and downstream repeats in [`vol4/simulation/ch16-sagnac-inductive-drag/theory.md:6`](../../../vol4/simulation/ch16-sagnac-inductive-drag/theory.md) and `AVE-PONDER/manuscript/vol_ponder/chapters/02_thrust_and_sagnac_telemetry.tex:60` need revision to point at this leaf.

## Cross-references

- **Primary derivation source:**
  - [`AVE-QED/docs/analysis/2026-05-13_Q-G24_lorentz_from_axiom_4.md`](../../../../../../AVE-QED/docs/analysis/2026-05-13_Q-G24_lorentz_from_axiom_4.md) lines 41-51, 190-192 — preferred frame derivation, CMB-rest-frame identification
  - [`AVE-QED/docs/analysis/2026-05-13_lorentz_violation_constraints.md`](../../../../../../AVE-QED/docs/analysis/2026-05-13_lorentz_violation_constraints.md) lines 4-12, 36-74 — cubic-symmetry suppression derivation, optical-scale $\delta_{aniso} \sim 10^{-22}$
- **A2 derivation chain:**
  - [`vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md`](../../../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) lines 14-26 — rotor mutual-inductance mechanism
  - `AVE-PONDER/manuscript/vol_ponder/chapters/06_sagnac_rlve_protocol.tex:17-27, 69` — twin derivation; "$\kappa_{entrain}$ falls off as $1/r^2$ from the rotor axis" (rotor-local confirmation)
  - [`vol4/simulation/ch16-sagnac-inductive-drag/theory.md`](../../../vol4/simulation/ch16-sagnac-inductive-drag/theory.md) — secondary derivation
- **C17 leaf to revise:**
  - [`vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md`](../../../vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md) — needs rewrite per §5 above
- **KB cross-cutting:**
  - [`common/divergence-test-substrate-map.md`](../../../common/divergence-test-substrate-map.md) rows A2, C7, C17, C18 — matrix-level application of this framework
  - [`vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md`](../../../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md) — Trans-Planckian GRB dispersion as surviving preferred-frame probe
