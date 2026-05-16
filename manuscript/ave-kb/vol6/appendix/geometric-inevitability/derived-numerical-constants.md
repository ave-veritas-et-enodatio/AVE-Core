[↑ Geometric Inevitability](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-ome498]
-->

<!-- PATH-STABLE: sec:derived_numerology -->
<!-- Cross-volume refs in this leaf:

  eq:H_infinity → vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md
  sec:galactic_saturation → vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md
  sec:membrane_phase_buffering → vol5/protein-folding-engine/ (exact path TBD)
-->

## Derived Numerical Constants

Beyond the classical "magic numbers" of nuclear physics, the AVE framework derives several numerical constants that govern phenomena across vastly different scales. Each is a ratio, product, or geometric projection of two or more independently derived quantities. None is fitted; all emerge from the axioms.

| Constant | Formula | Value | Physical Meaning |
|---|---|---|---|
| $\delta_{th}$ | $\dfrac{1}{14\pi^2} = \dfrac{\nu_{vac}}{\kappa_{cold}} \cdot \dfrac{2}{\pi}$ | 0.00724 | Residual thermal softening |
| $K_{mut}$ | $\dfrac{5\pi}{2}\cdot\dfrac{\alpha\hbar c}{1-\alpha/3}$ | 11.34 MeV$\cdot$fm | Nuclear mutual inductance |
| $d_p$ | $\dfrac{4\hbar}{m_p c}$ | 0.841 fm | Proton charge radius |
| $a_0$ | $\dfrac{c \cdot H_\infty}{2\pi}$ | $1.07\times10^{-10}$ m/s$^2$ | MOND acceleration scale |
| $V_{halo}$ | Skew-line integral of Borromean link | 2.0 | Toroidal crossing volume |
| $V_{GW}/V_{snap}$ | $\dfrac{h \cdot c \cdot \ell_{node} \cdot 2\pi f}{V_{snap}}$ | $1.42\times10^{-28}$ | GW linearity ratio ($h=10^{-21}$) |
| $\Gamma_{tach}$ | $\dfrac{Z_{rad} - Z_{conv}}{Z_{rad} + Z_{conv}}$ | 0.818 $\approx$ 9/11 | Tachocline reflection |
| $r_s(\odot)$ | $\dfrac{2GM_\odot}{c^2}$ | 2954 m | Solar Schwarzschild radius |
| $\beta_\text{fold}$ | $\ln(3) \times 3/7$ | 0.471 | Protein folding barrier exponent |
| $E_{yield}$ | $\dfrac{V_{yield}}{\ell_{node}} = \dfrac{\sqrt{\alpha}\, m_e^2 c^3}{e\, \hbar}$ | $1.13\times10^{17}$ V/m | Dielectric yield field ($\sqrt{\alpha}\times E_S$) |
| $\varphi$ | $\dfrac{\pi\sqrt{2}}{6}$ | 0.7405 | FCC lattice packing fraction |
| $1 - \varphi$ | $1 - \dfrac{\pi\sqrt{2}}{6}$ | 0.2595 | Void fraction (Op10 drain floor) |
| $Y_c$ | $1 - \sqrt{1 - \varphi}$ | 0.4906 | Drain $\to$ floor transition |
| $n_{coop}$ | $6_{edges} \times \dfrac{D}{D-1} = 7 \times (1+\nu)$ | 9 | Cooperative phase amplification |
| $E_{HB}$ | $U_{\text{Op4,raw}} \times (1 - \varphi)$ | 0.2158 eV | Hydrogen bond energy |
| $T_c^{\text{water}}$ | $\dfrac{E_{HB}}{n_{coop} \cdot k_B}$ | 278.3 K (5.1$^\circ$C) | Cooperative yield temperature |
| $k_{hb}$ | $\dfrac{2 E_{HB}}{d_{hb}^2}$ | 2.248 N/m | H-bond spring constant (Op4 curvature) |
| $k_{OH}$ | Coulomb bond solver | 791 N/m | O--H covalent spring constant |
| $T_m$ | $\dfrac{\hbar}{k_B}\sqrt{\dfrac{k_{hb}}{m_H}}$ | 279.5 K ($+6.3^\circ$C) | Water melting eigenmode ($+2.3\%$) |
| $\theta_{HOH}$ | $\arccos\!\left(\dfrac{-1}{3(1+\Gamma)}\right)$ | $104.48^\circ$ | H-O-H bond angle ($+0.03^\circ$) |
| $V_{II}$ | $V_I \times \varphi_{FCC}$ | $23.11\ \text{\AA}^3$ | Topological cell collapse (State II) |

### Thermal Softening ($\delta_{th} = 1/(14\pi^2)$)

The proton's core temperature $\sim m_p c^2 / k_B \approx 10^{13}$ K softens the quartic Skyrme repulsion by partially averaging out the gradient tensor. With the lattice gradient saturation (Axiom 4) now handled inside the energy functional, the residual softening fraction is the RMS noise averaging:

$$
\delta_{th} = \frac{\nu_{vac}}{\kappa_{cold}} \cdot \frac{2}{\pi} = \frac{2/7}{8\pi} \cdot \frac{2}{\pi} = \frac{1}{14\pi^2} \approx 0.00724
$$

Both $\nu_{vac}$ and $\kappa_{cold}$ are pure geometric constants derived independently; the $2/\pi$ factor is the mean-to-peak ratio of rectified sinusoidal thermal noise.

### Nuclear Mutual Inductance ($K_{mut}$)

The pairwise binding between nucleons is governed by:

$$
K_{mut} = \frac{5\pi}{2} \cdot \frac{\alpha \hbar c}{1 - \alpha/3} \approx 11.337\;\text{MeV}\cdot\text{fm}
$$

The factor $5\pi/2$ arises from five crossings of the proton's $(2,5)$ cinquefoil knot, each contributing a $\pi/2$ phase advance to the flux-linkage integral. The $(1 - \alpha/3)^{-1}$ correction is the first-order proximity enhancement at nuclear separations, analogous to a transformer vertex correction.

### Proton Charge Radius ($d_p = 4\hbar/(m_p c)$)

The proton charge radius is four times the proton reduced Compton wavelength --- the RMS vibration amplitude of the centre-of-mass standing wave confined within the saturated ($0\,\Omega$) cavity boundary of one lattice cell:

$$
d_p = 4 \cdot \frac{\hbar}{m_p \, c} \approx 0.841\;\text{fm}
$$

### MOND Acceleration Scale ($a_0 = c H_\infty / (2\pi)$)

The cosmological acceleration below which galactic rotation curves flatten is derived from the asymptotic Hubble parameter:

$$
a_0 = \frac{c \cdot H_\infty}{2\pi} \approx 1.07 \times 10^{-10}\;\text{m/s}^2
$$

where $H_\infty = 28\pi m_e^3 c G / (\hbar^2 \alpha^2)$ (see Eq. `eq:H_infinity`). At this scale, the vacuum lattice's mutual inductance begins to saturate, and the Axiom 4 saturation term produces flat rotation curves identical to the Deep MOND asymptote $g_{eff} \to \sqrt{g_N \cdot a_0}$ (see $\S$ `sec:galactic_saturation`).

### Toroidal Halo Volume ($V_{halo} = 2$)

The geometric volume of the 3D orthogonal tensor crossings of the Borromean link is computed analytically from the signed intersection integral of three great circles on $S^2$:

$$
V_{halo} = 2.0
$$

This is a purely topological constant; it sets the fraction of the Skyrme soliton's energy that resides in the inter-braid halo rather than the core.

### Protein Folding Barrier ($\beta = \ln(3) \times 3/7 = 0.471$)

The folding timescale of a two-state protein is (Volume V, Chapter 5):

$$
\tau_\text{fold} = Q^2 \cdot N \cdot \tau_\text{water} \cdot \exp\!\bigl(\beta \cdot N \cdot \text{CO}\bigr)
$$

where $N$ is the chain length, CO is the relative contact order, and the barrier exponent combines three axiom-derived quantities:

$$
\beta = \ln(3) \times \frac{d}{n} = \ln(3) \times \frac{3}{7} = 0.471
$$

- $\ln(3)$: entropy cost of selecting 1 from 3 Ramachandran basins;
- $3/7 = d/n$: spatial compliance projection (same ratio as $\alpha_s = \alpha^{3/7}$);
- $Q^2 = 49$: double ring-down (propagation $\times$ evaluation);
- $\tau_\text{water} = 8.3$ ps: solvent rate-limiting.

Empirical barrier: $b_\text{emp} = 0.452$. Derived: $\beta = 0.471$. **Error: 4.1%.**
Validated across 15 two-state folders: $R = 0.87$, 12/15 within $\pm$2 decades.

### FCC Packing Fraction ($\varphi = \pi\sqrt{2}/6$)

The $K = 2G$ identity (Axiom 2) selects body-centred close-packing of the lattice nodes. The FCC packing fraction for equal spheres is:

$$
\varphi = \frac{\pi\sqrt{2}}{6} \approx 0.7405
$$

The complementary **void fraction** $1 - \varphi \approx 0.2595$ is the interstitial space between packed nodes---geometrically inaccessible to junction-based Op10 drain.

**Dual role across regimes.** At **nuclear scale** (Regime I, $S \to 0$): the packing fraction determines the saturated zone geometry that confines topological defects. The crossing number $c$ partitions the Faddeev-Skyrme coupling via $r_\text{opt} = \kappa/c$ --- the soliton cannot radiate past the packed lattice boundary.

At **atomic scale** (Regime II, $S \approx 1$): Op10 drain $Y = c/(2\pi^2)$ acts on nodal phase space (fraction $\varphi$). When $(1 - Y)^2 < 1 - \varphi$, the void fraction sets a floor:

$$
\text{IE} \geq E_\text{base} \times (1 - \varphi) \qquad \text{(void floor)}
$$

The threshold is $Y_c = 1 - \sqrt{1 - \varphi} \approx 0.49$. This correction fixes F ($+0.2\%$) and Ne ($+0.9\%$) with zero free parameters (see Volume IV, Chapter 16).

### Dielectric Yield Field ($E_{yield} = \sqrt{\alpha}\, E_S$)

The Axiom 4 yield voltage $V_{yield} = \sqrt{\alpha}\, V_{snap} \approx 43.65$ kV applies across a single lattice node of spacing $\ell_{node} = \hbar/(m_e c) = 3.862 \times 10^{-13}$ m. The corresponding electric field threshold is:

$$
E_{yield} = \frac{V_{yield}}{\ell_{node}} = \frac{\sqrt{\alpha}\, m_e^2 c^3}{e\, \hbar} \approx 1.13 \times 10^{17}\;\text{V/m}
$$

This is exactly $\sqrt{\alpha}$ times the Schwinger critical field of QED ($E_S = m_e^2 c^3 / (e\hbar) \approx 1.32 \times 10^{18}$ V/m). The strongest sustained laboratory fields ($\sim 10^{10}$ V/m in ultrafast laser foci) are seven orders of magnitude below $E_{yield}$. Consequently, all macroscopic electromagnetic devices operate in **Regime I** (linear vacuum, $\varepsilon_{eff} = \varepsilon_0$). Axiom 4 saturation is physically operative only at sub-femtometer separations---within particle cores, nuclear scattering events, and event horizons (see Volume IV, Chapter 2).

### Cooperative Lattice Amplification ($n_{coop} = 9$)

The cooperative phase transition within hydrogen-bonded lattices is governed by a dimensionless amplification number $n_{coop}$ that converts single-bond energy into cooperative lattice yield strain. This constant admits two independent, convergent derivations.

**Path A: Tetrahedral Edge Count (Axiom 1)**

The hydrogen-bond network in water forms a tetrahedral coordination polyhedron. The cooperative unit is not the individual H-bond (vertex connection) but the **edge**---the pairwise coupling between two adjacent molecules. The tetrahedron has 4 vertices and **6 edges**.

Each edge is a one-dimensional coupling embedded in $D = 3$ spatial dimensions. The isotropic projection factor for a 2-body correlation in $D$ dimensions is $D/(D-1) = 3/2$. Therefore:

$$
n_{coop} = E_{\text{edges}} \times \frac{D}{D-1} = 6 \times \frac{3}{2} = 9
$$

**Path B: Compliance Mode Amplification (Axiom 2)**

The Poisson ratio $\nu_{vac} = 2/7$ implies **7 independent compliance modes** per lattice node ($\S$ `sec:g_star_derivation`). The bulk-shear coupling factor from the $K = 2G$ identity is $(1 + \nu_{vac}) = 9/7$. The cooperative amplification is then:

$$
n_{coop} = 7 \times (1 + \nu_{vac}) = 7 \times \frac{9}{7} = 9
$$

The exact algebraic identity $6 \times 3/2 = 7 \times 9/7 = 9$ confirms the structural consistency between the lattice geometry (Axiom 1) and the elastic compliance (Axiom 2).

**Cross-Validation: Water +4$^\circ$C Density Anomaly**

The cooperative yield temperature $T_c$ is the point where the cooperative thermal strain amplitude $A = n_{coop} \cdot k_B T / E_{HB}$ reaches unity (i.e., the saturation operator yields):

$$
T_c = \frac{E_{HB}}{n_{coop} \cdot k_B} = \frac{0.2158\;\text{eV}}{9 \times 8.617 \times 10^{-5}\;\text{eV/K}} \approx 278.3\;\text{K} = +5.1^\circ\text{C}
$$

The measured anomalous density maximum of water occurs at $+4.0^\circ$C $= 277.15$ K.

**Error: 0.40%.** Zero free parameters.

**Biological Application: Cholesterol Phase Buffering**

In lipid bilayer membranes, the cooperative yield boundary at $T_c \approx 5^\circ$C governs the $V_I \to V_{II}$ gel-to-fluid transition. Cholesterol's rigid $sp^3$ 4-ring wedge raises the effective yield limit by the FCC packing fraction:

$$
A_{yield}^{\text{buffered}} = 1 + \varphi = 1 + \frac{\pi\sqrt{2}}{6} \approx 1.7405
$$

This pushes the catastrophic phase snap far outside the biological operating range ($-20^\circ$C to $+60^\circ$C), holding the membrane permanently at the $K = 2G$ structural yield threshold---pliant enough for wave propagation, rigid enough for allosteric state-switching in embedded protein circuits (Volume V, Chapter 2, $\S$ `sec:membrane_phase_buffering`).

---
