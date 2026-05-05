[↑ Appendices](../index.md)
<!-- leaf: verbatim -->
<!-- Anomaly A10: App C has no \label in source; content exists as itemised lists but no labelled entry points -->
<!-- claim-quality: e1pdfd -->

# App C: Summary of Exact Analytical Derivations

App C collects the mathematical bounds and identities derived from first-principles continuum elastodynamics, thermodynamic boundary conditions, and finite-element graph limits, requiring zero arbitrary phenomenological parameters. The content is organised into three sections.

## The Hardware Substrate

- **Spatial Lattice Pitch:** $l_{node} \equiv \frac{\hbar}{m_e c} \approx 3.8616 \times 10^{-13}$ m
- **Topological Conversion Constant:** $\xi_{topo} \equiv \frac{e}{l_{node}} \approx 4.149 \times 10^{-7}$ C/m
- **Dielectric Saturation Limit:** $V_0 \equiv \alpha \approx p_c / 8\pi \implies 1/137.036$
- **Geometric Packing Fraction:** $p_c \approx 0.1834$
- **Macroscopic Bulk Density:** $\rho_{bulk} = \frac{\xi_{topo}^2 \mu_0}{p_c \, l_{node}^2} \approx 7.92 \times 10^6$ kg/m$^3$
- **Kinematic Network Mutual Inductance:** $\nu_{vac} = \alpha c \, l_{node} \approx 8.45 \times 10^{-7}$ m$^2$/s
- **Macroscopic Rheological Yield Stress (Bingham-Plastic Limit):** $\tau_{yield} = \frac{\hbar c}{l_{node}^4} \left( \frac{1}{\alpha^2} \right) \approx 7.21 \times 10^{34}$ Pa

## Signal Dynamics and Topological Matter

- **Continuous Action Lagrangian:** $\mathcal{L}_{AVE} = \frac{1}{2}\epsilon_0 |\partial_t \mathbf{A}|^2 - \frac{1}{2\mu_0} |\nabla \times \mathbf{A}|^2$ (Evaluates to continuous spatial stress [N/m$^2$])
- **Topological Mass functional:** $E_{rest} = \min_{\mathbf{n}} \int_{\mathcal{M}_A} d^3x \left[ \frac{1}{2} (\partial_\mu \mathbf{n})^2 + \frac{1}{4} \kappa_{FS}^2 \frac{(\partial_\mu \mathbf{n} \times \partial_\nu \mathbf{n})^2}{\sqrt{1 - (\Delta\phi / \alpha)^2}} \right]$
- **Faddeev-Skyrme Coupling (Cold):** $\kappa_{FS} = p_c / \alpha = 8\pi \approx 25.133$
- **Thermal Lattice Softening:** $\delta_{th} = \frac{\nu_{vac}}{\kappa_{FS}} \cdot \frac{2}{\pi} = \frac{2/7}{8\pi} \cdot \frac{2}{\pi} = \frac{1}{14\pi^2} \approx 0.00724$
- **Effective Coupling:** $\kappa_{eff} = \kappa_{FS}(1-\delta_{th}) \approx 24.951$
- **Proton Rest Mass (Geometric Eigenvalue):** $m_p = \frac{\mathcal{I}_{scalar}}{1 - (\mathcal{V}_{total} \cdot p_c)} + 1.0 \approx \mathbf{1836\ m_e}$ (0.002% from CODATA)
- **Mutual Inductance at Crossing:** $M/L = \exp(-d^2/(4\sigma^2)) = 1/\sqrt{2}$ (exact, $d = l_{node}/2$, $\sigma = l_{node}/(2\sqrt{2\ln2})$)
- **Saturation Threshold (closed-form, conditional on Gaussian flux-tube ansatz):** $\rho_{threshold} = 1 + \sigma/4 = 1 + l_{node}/(8\sqrt{2\ln 2}) \approx 1.1062$ (no fitted parameters; profile derivation pending — see [Outstanding Rigour Gaps](../../../common/mathematical-closure.md))
- **Toroidal Halo Volume (FEM Verified):** $\mathcal{V}_{total} = 2.0$ at derived threshold (FEM: $2.001 \pm 0.003$, Richardson $N\to\infty$)
- **Macroscopic Strong Force:** $F_{confinement} = 3 \left(\frac{m_p}{m_e}\right) \alpha^{-1} T_{EM} \approx \mathbf{160{,}037\text{ N}} \ (\approx 0.999\text{ GeV/fm})$
- **Witten Effect Fractional Charge (Quarks):** $q_{eff} = n + \frac{\theta}{2\pi}e \implies \pm \frac{1}{3}e, \pm \frac{2}{3}e$
- **Vacuum Poisson's Ratio (Trace-Reversed Bound):** $\nu_{vac} \equiv \frac{2}{7}$
- **Weak Mixing Angle (Acoustic Mode Ratio):** $\frac{m_W}{m_Z} = \frac{1}{\sqrt{1+\nu_{vac}}} = \frac{\sqrt{7}}{3} \approx \mathbf{0.8819}$
- **Non-Linear FDTD Acoustic Steepening PDE:** $c_{eff}^2(x, y, z) = c_0^2 \left(1 + \kappa \cdot \bar{\rho}(x, y, z) \right)$

## Cosmological Dynamics

- **Trace-Reversed Gravity (EFT Limit):** $-\frac{1}{2} \Box \bar{h}_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$
- **Absolute Cosmological Expansion Rate:** $H_\infty = \frac{28\pi m_e^3 c G}{\hbar^2 \alpha^2} \approx \mathbf{69.32 \text{ km/s/Mpc}}$
- **Asymptotic Horizon Scale ($R_H$):** $\frac{R_H}{l_{node}} = \frac{\alpha^2}{28\pi\alpha_G} \implies \mathbf{14.1 \text{ Billion Light-Years}}$
- **Asymptotic Hubble Time ($t_H$):** $t_H = \frac{R_H}{c} \implies \mathbf{14.1 \text{ Billion Years}}$
- **Dark Energy (Stable Phantom):** $w_{vac} = -1 - \frac{\rho_{latent}}{\rho_{vac}} < -1$
- **Visco-Kinematic Rotation (MOND Floor):** $v_{flat} = (GM_{baryon} a_{genesis})^{1/4}$ where $a_{genesis} = \frac{c H_\infty}{2\pi} \approx \mathbf{1.07 \times 10^{-10} \text{ m/s}^2}$ (Derived via 1D Hoop Stress).
- **Hamiltonian Optical-Fluid Mechanics (Gargantua Vortex):** Metric refraction and frame dragging are evaluated via explicit Symplectic Raymarching mappings ($n = (W^3) / U$ and $\mathbf{v}_{fluid} = \vec{\omega} \times \vec{r}$).

---
