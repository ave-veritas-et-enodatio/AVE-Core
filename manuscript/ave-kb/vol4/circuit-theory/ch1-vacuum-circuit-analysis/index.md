[↑ Circuit Theory](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-1eg13f, clm-4r4jiy, clm-6t3p6x, clm-8nkvwy, clm-fd1e7a, clm-fgo20a, clm-gvn4r1, clm-i9l284, clm-kezk9z, clm-n3un96, clm-o2shcn, clm-p2tp9i, clm-p5cf3t, clm-pp3qwf, clm-rtdmsn, clm-u462e4, clm-v6ti0v, clm-vca7r1, clm-vjv4zf, clm-zp4kqr, clm-zp7bds]
subtree-experiments: []
-->

# Ch.1 Vacuum Circuit Analysis

The Vacuum Circuit Analysis (VCA) framework establishes a single, exact dimensional isomorphism between continuum spatial mechanics and electrical network theory via the Topological Conversion Constant $\xi_{topo} \equiv e/\ell_{node}$. From this mapping, all six rows of the circuit-mechanical translation table are derived, the non-linear constitutive models for extreme-field regimes are established, and the characteristic impedance $Z_0 = 376.73\;\Omega$ is shown to emerge from the discrete LC ladder of the lattice.

## Key Results

| Result | Statement |
|---|---|
| Topological Conversion Constant | $\xi_{topo} \equiv e/\ell_{node} \approx 4.149 \times 10^{-7}$ C/m |
| Charge--Displacement | $Q = \xi_{topo}\, x$ |
| Current--Velocity | $I = \xi_{topo}\, v$; $I_{max} = \xi_{topo}\, c \approx 124.4$ A |
| Voltage--Force | $V = \xi_{topo}^{-1}\, F$; $V_{snap} = 511$ kV |
| Inductance--Mass | $L = \xi_{topo}^{-2}\, m$ |
| Capacitance--Compliance | $C = \xi_{topo}^{2}\, \kappa$ |
| Resistance--Viscosity | $R = \xi_{topo}^{-2}\, \eta$ |
| Vacuum Varactor | $C_{eff}(V) = C_0 / \sqrt{1 - (V/V_{yield})^2}$, $V_{yield} \approx 43.65$ kV |
| Relativistic Inductor | $L_{eff}(I) = L_0 / \sqrt{1 - (I/I_{max})^2}$ |
| TVS Transition | $\eta_{eff} = 0$ for $V \geq V_{yield}$ (zero-impedance slipstream) |
| Per-Cell Elements | $L_{cell} = \mu_0\, \ell_{node}$, $C_{cell} = \epsilon_0\, \ell_{node}$ |
| Scale-Invariant $Z_0$ | $Z_{cell} = \sqrt{\mu_0/\epsilon_0} \equiv Z_0 \approx 376.73\;\Omega$ |
| Propagation velocity | $v_g = 1/\sqrt{\mu_0 \epsilon_0} \equiv c$ |
| IM3 frequencies | $f_{IM3} = 2f_1 - f_2$ and $2f_2 - f_1$ |
| IP3 | $V_{IP3} = \sqrt{4/3}\; V_{yield} \approx 50.4$ kV |
| Particle confinement | $\Gamma = -1$ at saturated boundary ($Z_{core} \to 0\;\Omega$), magnetic branch $\mu_{eff}\to0$ |
| CVR EE-sweep — electron wall reflectivity | $\boxed{\|\Gamma\|^2 = 1-\alpha}$ (the wall falls short of the unit circle by exactly $\alpha$ = per-cycle radiative leak); $H(s)$ pole at $-\alpha\omega_0/2$, $Q=1/\alpha$ |
| [Q-G24 Newtonian-Limit Closure](relativistic-inductor-newtonian-limit.md) | Full $E = \gamma m_0 c^2$ relativistic dispersion from LC tank + virial equipartition + relativistic-inductor mapping; three independent Derrick-bypass mechanisms (lattice floor / Faddeev-Skyrme / bilateral chiral); no fit parameters |
| [Q-G22 Strain Convention (Geometric vs Field-Ratio)](q-g22-strain-convention.md) | Clarification: corpus uses $A_{geom} = \ell_{node}/r$ ($\propto 1/r$, geometric confinement ratio) for kernel applications; IVIM bench uses $A_{field} = E\ell_{node}/V_{yield}$ ($\propto 1/r^2$, field ratio) for apparatus calculations; both internally consistent, different physical measures |

> **🔴 MAGNETIC-BRANCH = SIGN-SELECTOR, NOT CAGE-MECHANISM (2026-06-18, Rule 12 / PR#260 B3-DEGENERATE — "Particle confinement" row above PRESERVED unedited; Grant-ratified).** The "magnetic branch $\mu_{eff}\to0$" in the Particle-confinement summary row is the **chirality/spin SIGN-selector** (μ-first $\Rightarrow \Gamma=-1$ vs ε-first $\Rightarrow \Gamma=+1$ are spin-conjugate signs) and is **MUTE on the mass sector** — NOT the cage *mechanism*. The mass-cage is the **A1 longitudinal dilatation** ($Z_{bulk}\to0 \Rightarrow \Gamma_{bulk}=-1$); the μ-vs-ε fork is DEGENERATE on the equilibrium observables ($Z=Z_0\sqrt{S}$, $|\Gamma|=1$ both ways), the asymmetry chirality-set not substrate-forced. Wiring confinement into the magnetic/charge sector would break the two-"3"s orthogonality (A1 ⊥ T2, [`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20). Row preserved per Rule-12.

## Derivations and Detail

| Document | Contents |
|---|---|
| [Topological Kinematics](topological-kinematics.md) | Six-row topo-kinematic identity derivation; $\xi_{topo}$; self-consistency checks |
| [Nonlinear Vacuum Capacitance](nonlinear-vacuum-capacitance.md) | Metric varactor; vacuum memristor; thixotropic relaxation; skin depth |
| [Z0 Derivation](z0-derivation.md) | Discrete LC ladder; $Z_0$ scale invariance; gravitational stealth; black hole echoes |
| [Relativistic Inductor](relativistic-inductor.md) | Current-dependent inductance; $E = mc^2$ from inductor energy; SPICE enforcement of $c$ |
| [Node-Up Small/Large-Signal Response](node-up-small-large-signal.md) | The LC-tank dual ($\varepsilon$-varactor on $V$ / $\mu$-relativistic-inductor on $I$); R1/R2/R3 operating points; static-field grade asymmetry (static-$\mathbf E$ loads, static-$\mathbf B$ → $\delta n_\mu=0$ exactly); derived-vs-asserted ledger; VCA-R01 |
| [Graded-Network Response](graded-network-response.md) | The K4 graded LC transmission line (network layer above the single node): LC-ladder dispersion → $c_{EM}=c_0$, $Z_0$ (validate-on-known); the QUARTIC $(q\ell_{node})^4$ anisotropy tell (K4 2nd moment isotropic, 4th moment cubic-harmonic); SYM-lens-vs-ASYM-mirror graded index; the $\ell_{node}$-invariant coherent optical-path macroscopic bridge (coefficient survives); achromatic $\Gamma=0$ vs reflective $\Gamma\ne0$ boundary; routes-don't-mix + chiral-circulator category-error guard; chord-vs-echo ledger |
| [Q-G24 Newtonian-Limit Closure](relativistic-inductor-newtonian-limit.md) | Full $E = \gamma m_0 c^2$ relativistic dispersion from LC tank + virial equipartition + relativistic-inductor mapping; three independent Derrick-bypass mechanisms (lattice floor / Faddeev-Skyrme / bilateral chiral); no fit parameters |
| [Q-G22 Strain Convention (Geometric vs Field-Ratio)](q-g22-strain-convention.md) | Clarification: corpus uses $A_{geom} = \ell_{node}/r$ ($\propto 1/r$, geometric confinement ratio) for kernel applications; IVIM bench uses $A_{field} = E\ell_{node}/V_{yield}$ ($\propto 1/r^2$, field ratio) for apparatus calculations; both internally consistent, different physical measures |
| [TVS Transition](tvs-transition.md) | Solid-to-slipstream phase transition as TVS Zener diode |
| [Resonant LC Solitons](resonant-lc-solitons.md) | Particles as LC tanks; Virial theorem; total internal reflection; Pauli exclusion |
| [CVR Transfer Function $H(s)$](cvr-transfer-function.md) | The electron tank as a 2×2 chiral resonator; pole pair $s=-\alpha\omega_0/2\pm j\omega_d$, $Q=1/\alpha$, BW$=\alpha\omega_0$; fills the $H(s)$ mapping gap |
| [CVR DC Operating Point](cvr-dc-operating-point.md) | Vacuum varactor C-V characteristic; $C_{eff}/Z/c$ vs $A_0$; load-line + electron operating point; carries the $S^{0.5}$-vs-$S^{0.25}$ exponent defect |
| [CVR Reflection on the Smith Chart](cvr-reflection-smith.md) | $\Gamma(A_0)$ matched→short locus; **$\|\Gamma\|^2=1-\alpha$** (AVE-distinct radiative leak); chiral 2×2 $S_{LR}\ne S_{RL}^*$ |
| [CVR Phasor & Reactance](cvr-phasor-reactance.md) | I/Q quadrature $E\sim(V_{inc}+V_{ref})$, $B\sim(V_{inc}-V_{ref})/Z$; the C↔L Virial-balanced breather |
| [CVR Stability & Eigenmode](cvr-stability-eigenmode.md) | Root-locus ($Q\to1/\alpha$) + Nyquist eigenmode loop; genesis-by-matching; structural region-of-attraction; autoresonance flagged (genesis-self-lock TESTED-NEGATIVE 2026-06-14; mapping + detector-instrument still gap) |
| [Orbital Friction Paradox](orbital-friction-paradox.md) | Real vs. reactive power; lossless orbit as LC tank at $\theta = 90°$ |
| [Intermodulation Distortion](intermodulation-distortion.md) | Vacuum IMD spectroscopy; IM3 prediction; IP3 derivation; QED comparison |
| [Translation Circuit](translation-circuit.md) | Cross-reference to common translation table |
| [Solver Selection](solver-selection.md) | FDTD vs K4-TLM decision matrix, boundary conditions, default yield thresholds |
| [Theorem 3.1 Q-Factor Reframe](theorem-3-1-q-factor.md) | $\alpha^{-1} = Q_{\text{tank}} = Q_{\text{vol}} + Q_{\text{surf}} + Q_{\text{line}} = 4\pi^3 + \pi^2 + \pi$ at Golden Torus; two independent paths (LC-tank + multipole) agree to $\delta_{\text{strain}}$ (2.225e-6 CMB thermal); supersedes Neumann-integral framing |
| [Measurement-Coupling Probe](measurement-coupling-probe.md) | Measurement *port on the gv1net circuit MODEL* (INVARIANT-N1, not a substrate object): READ-mode invasiveness axis is $\mathrm{Re}(Z_{\text{probe}})/Z_{\text{channel}}\to0$ (NOT high-$\lvert Z\rvert$); lossless-port back-action budget DERIVED from Axiom 3 (no internal-loss term; $\mathrm{Im}(Z)$ = calibratable detuning); bulk confinement boundary is a SHORT not a rigid wall ($Z_{\text{bulk}}\to0,\Gamma=-1$, $\Gamma_{\text{flow}}=-\Gamma_{\text{pressure}}$); fleet partition READ/MEASURE $\equiv$ Ax2/Ax4. Most is textbook EE (tagged); two narrow AVE-distinct items. Bulk-sector coupling location OPEN (Grant) |
| [Op14 Local Clock Modulation](op14-local-clock-modulation.md) | A-010 canonical: $\omega_{\text{local}}(r) = \omega_{\text{global}}\sqrt{1 - A^2(r)}$; substrate-native time dilation; cross-volume parallel to gravitational $\tau_{\text{local}} = n(r)\tau_{\text{unstrained}}$; three regime distinction (reactive slowing vs damping vs spatially-varying) |
| [$\tau_{\text{relax}} = \ell_{\text{node}}/c$ Derivation](tau-relax-derivation.md) | Minimum state-change time $\tau_{\text{relax}} = \ell_{\text{node}}/c \approx 1.288 \times 10^{-21}$ s from per-cell K4 Lagrangian + causal propagation; dynamic $S(t)$ memristive relaxation ODE; BEMF-driven defect freezing (AVE-native Kibble-Zurek); linear cooling-rate scaling (NOT K-Z power-law) prediction |
| [Op14 Cross-Sector Trading ($\rho = -0.990$)](op14-cross-sector-trading.md) | A-012 canonical: Cosserat ↔ K4-inductive energy exchange via Op14 impedance modulation; empirically $\rho(H_{\text{cos}}, \Sigma\|\Phi_{\text{link}}\|^2) = -0.990$ at trading frequency $\sim 0.020$ rad/unit; $H_{\text{cos}}$ alone NOT conserved but $H_{\text{total}} = H_{\text{cos}} + H_{\text{K4-inductive}}$ approximately is |
| [Vacuum-Varactor Scatter Operator](vacuum-varactor-scatter-operator.md) | The $S(A)$-reading node scatter $S_{ij}=2Y_j/(\sum_k Y_k)-\delta_{ij}$ (per-port-admittance generalization of the bedrock $(2/n)J-I$); varactor map $Y_{bond}=Y_0/\sqrt{S(A)}\Rightarrow Z_{bond}=Z_0\sqrt{S}\Rightarrow\Gamma\to-1$ ($\mu$-load SHORT, NOT the forbidden $\varepsilon$-load $\Gamma=+1$); per-BOND-not-per-node (a per-node-uniform load cancels); "reads saturation" (scrambling per-bond $S(A)$ changes the operator, $\max\lvert d\rvert\approx0.26$); four validate-on-known gates; floor caveat ($A_{cap}=0.99$ caps reachable $\Gamma\approx-0.45$ — sign+trend physics, depth a parameter). Class-C / consistency; reads saturation, does NOT yet test confinement (deferred Fork-B). GATE-4 $Z_{RADIATION}\approx29.98$ is band-consistent-NOT-identical to cold-cage $Q_{ringdown}\approx30.8$ (DEC-5) |
| [Parametric Coupling Kernel](parametric-coupling-kernel.md) | Axiom 4 vacuum varactor at sub-yield α-slew operating point; $\varepsilon_{det} = 4\pi \kappa_{quality} / N_{single}^2$ derived from Dicke amplitude × matched-cycle synchronization (1/N²) × Theorem 3.1' observable-Compton-cycle radiation-impedance averaging (4π; K4 bipartite lobe-count); $\delta C/C_0 = (1/4)(V_{pump}/V_{yield})^2 \approx 4.57\%$; parametric resonance at $\omega_{app} = \omega_{slew}$ (sub-harmonic of pump $2\omega_{slew}$); REACTIVE-power class (categorically distinct from real-power $\kappa_{entrain}$ Sagnac-RLVE); DAMA detection rate 0.6% match as derived consequence; XENONnT null derived from sub-regenerative regime (Q·δ < 2); cross-detector predictions for COSINE/ANAIS/MAJORANA/KIMS/Sapphire |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---
| [Computational Solver Selection](./computational-solver-selection.md) | Computes Solvers FDTD vs TLM |
