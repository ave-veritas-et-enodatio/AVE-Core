[↑ Condensed Matter](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-eaiqj1, clm-hk81zp, clm-jpfbm6, clm-refjr6, clm-t05mvx, clm-uu6dl5]
-->

# Ch.11: Thermodynamics and The Arrow of Time

Temperature redefined as RMS electromagnetic noise on the LC lattice; entropy as geometric spherical spreading; the Fluctuation-Dissipation Theorem as Nyquist noise applied to lattice impedance; lattice-derived $g_* = 85.75$ fixing heat capacity and baryon asymmetry; thermal softening of topological structures as a zero-parameter correction; phase transitions as impedance matching catastrophes; and water anomalies from a two-state LC partition framework.

Cross-volume dependencies:
> → Primary: [H-Bond Op4 Equilibrium](../../../vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md) — sec:hbond_derivation; the O--O distance $d_{OO} = 2.727$ Angstrom used in the water anomaly derivation is derived in Vol. V, Ch. 2.

> → Primary: [Melting Eigenmode](../../../vol7/condensed-matter/ch4-phase-transitions/s03-melting-eigenmode.md) — sec:melting_eigenmode; the melting temperature $T_m = 279.5$ K derived as proton transfer eigenmode lives in Vol. VII, Ch. 11.

## Key Results

| Result | Statement |
|---|---|
| Macroscopic Temperature as LC Noise | $T \propto \langle U_{noise} \rangle = \langle \frac{1}{2}\epsilon_0 |\mathbf{E}|^2 + \frac{1}{2}\mu_0 |\mathbf{H}|^2 \rangle = \frac{3}{2} k_B T$ |
| Vacuum Nyquist Baseline | $\langle V^2_{vac}(f) \rangle = 4 k_B T \, Z_0 \, \Delta f$ |
| Effective DoF $g_*$ | $g_* = 7^3/4 = 85.75$ (lattice geometry, no particle catalog) |
| Vacuum Heat Capacity | $c_v = (g_*/2) \cdot k_B / \ell_{node}^3 \approx 42.875 \cdot k_B / \ell_{node}^3$ |
| Baryon Asymmetry | $\eta = 6.08 \times 10^{-10}$; observed $6.1 \times 10^{-10}$; error 0.38% |
| Thermal Softening Correction | $\delta_{th} = 1/(14\pi^2) \approx 0.00721$; zero-parameter result |
| Casimir Effective Temperature | $T_{eff} = T_{ambient} \cdot \sqrt{1 - (f_c/f_{max})^2}$ |
| Superconducting Impedance Transition | $Z_{eff} \to 0\;\Omega$, $|\Gamma| \to 1$ |
| Macroscopic Transition Boundary | $S(r) = f_{\text{yield}} \cdot \sqrt{1 - (r_{\text{th}}/r_{\text{crit}})^2}$, $r_{\text{crit}} = \sqrt{2\alpha}$ |
| Nyquist Thermal Voltage Noise | $\langle V^2(f) \rangle = 4 k_B T R \, \Delta f$ |
| Boundary Reflection Coefficient | $\Gamma = (Z_0 - Z_{int})/(Z_0 + Z_{int})$ |
| Dissipation Power | $P_{diss} = \langle V^2 \rangle / (4R) = k_B T \, \Delta f$ |
| Ohmic Damping Coefficient | $\gamma = \frac{1}{2} Z_0 / (\omega_0 L_{eff})$ |
| Axiom 4 Gradient Saturation Kernel | $(\partial\phi/\partial r)_{eff} = (\partial\phi/\partial r)\sqrt{1 - (|\partial_r\phi|/(\pi/\ell_{node}))^2}$ |
| Thermal Softening of Skyrme Coupling | $\kappa_{FS}^{(T)} = 8\pi(1 - 1/(14\pi^2))$ |
| Transmitted Noise Power | $P_{transmitted} = (1 - |\Gamma|^2) \cdot P_{incident}$ |
| Kolmogorov Spectral Cutoff | $k_{\max} = \pi / \ell_{node}$; bounded enstrophy via Axiom 4 Nyquist limit [Kolmogorov](./kolmogorov-spectral-cutoff.md) |
| Avalanche Exponent (3D) | $n_{3D} = 38/21 \approx 1.8095$; from $\nu_{vac} = 2/7$ Poisson correction [Kolmogorov](./kolmogorov-spectral-cutoff.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Entropy Redefinition](./entropy-redefinition.md) | Entropy as geometric spreading; temperature as LC noise; thermal jitter |
| [Resultbox: Macroscopic Temperature as LC Noise](./macroscopic-temperature-lc-noise.md) | Temperature-noise equivalence formula |
| [The Arrow of Time](./arrow-of-time.md) | Irreversibility from spherical FDTD wave propagation |
| [Fluctuation-Dissipation Theorem](./nyquist-noise-fdt.md) | Nyquist noise; vacuum baseline; boundary-impedance thermalization |
| [Resultbox: Vacuum Nyquist Baseline](./vacuum-nyquist-baseline.md) | Vacuum noise spectral density |
| [Transmon Qubit Decoherence](./transmon-decoherence.md) | Boundary noise injection; Ohmic damping; dissipation power |
| [Mode Counting and Heat Capacity](./mode-counting-heat-capacity.md) | 7-mode compliance manifold; $g_*$ derivation; equipartition; Dulong-Petit limit |
| [Resultbox: Effective DoF $g_*$](./effective-dof-g-star.md) | $g_* = 7^3/4 = 85.75$ |
| [Resultbox: Vacuum Heat Capacity](./vacuum-heat-capacity.md) | $c_v$ formula |
| [Resultbox: Baryon Asymmetry](./baryon-asymmetry.md) | $\eta = 6.08 \times 10^{-10}$ |
| [Baryon Asymmetry Derivation](./baryon-asymmetry-derivation.md) | Verification of $g_* = 85.75$ via observed $\eta$ |
| [Resultbox: Thermal Softening Correction](./thermal-softening-correction.md) | $\kappa_{FS}^{(T)}$ and $\delta_{th}$ formulae |
| [Thermal Softening of Topological Structures](./thermal-softening-skyrme.md) | Skyrme coupling correction; gradient saturation; physical interpretation |
| [Resultbox: Casimir Effective Temperature](./casimir-effective-temperature.md) | Geometric phase transition via cavity cutoff |
| [Phase Transitions as Impedance Matching](./phase-transitions-impedance.md) | Superconducting transition; Casimir cooling; impedance catastrophes |
| [Water Anomaly: Two-State LC Partition](./water-anomaly-lc-partition.md) | $+4\,^{\circ}\text{C}$ density maximum; LLCP validation; Kirkwood-Frohlich dielectric |
| [General Classification of Phase Transitions](./phase-transition-classification.md) | Impedance mapping table for all classical phase transitions |
| [Remaining Ch.11 Resultboxes](./ch11-remaining-resultboxes.md) | Completion manifest: all ch11 resultboxes assigned to named leaves; no unassigned resultboxes remain |
| [Kolmogorov Spectral Cutoff](./kolmogorov-spectral-cutoff.md) | Nyquist hard cutoff at $k_{\max} = \pi/\ell_{node}$; saturated energy spectrum $E(k) \cdot S(k/k_{\max})$; AVALANCHE_N $= 38/21$; bounded enstrophy proof |

> ↗ See also: [Ch.10: Quantum Computing and Topological Immunity](../../../vol4/advanced-applications/ch10-quantum-computing/index.md) — transmon decoherence and Casimir cooling context

NOTE: summarybox and exercisebox environments are not extracted as leaves.

---
