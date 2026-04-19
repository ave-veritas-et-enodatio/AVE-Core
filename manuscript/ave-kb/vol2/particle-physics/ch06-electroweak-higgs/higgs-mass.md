[↑ Ch.6 — Electroweak and Higgs](index.md)
<!-- leaf: verbatim -->

## The Neutrino Mass Spectrum

The neutrino is a pure torsional (screw) defect---a propagating twist wave in the Cosserat sector. Its mass is set by the ratio of torsional to translational coupling, multiplied by the dielectric compliance:

$$
m_\nu = m_e \cdot \alpha \cdot \frac{m_e}{M_W}
$$

**Physical meaning:** $m_e/M_W$ is the ratio of translational to torsional energy scale, and $\alpha$ is the dielectric coupling between sectors. Together, the neutrino mass is suppressed by $\alpha \times (m_e/M_W)$ relative to the electron. Evaluating:

$$
m_\nu \approx 0.024 \text{ eV per flavor}
$$

### Flavor Splitting via the Torus Knot Ladder

Three neutrino flavors arise from the torus knot ladder: each flavor pairs with a baryon resonance via the crossing number. The mass splitting scales as $1/c$ where $c$ is the crossing number:

| Flavor | Baryon Partner | Crossing $c$ | Mass (meV) |
|---|---|---|---|
| $\nu_1$ | Proton $(2,5)$ | 5 | $\sim 24$ |
| $\nu_2$ | $\Delta(1232)$ $(2,7)$ | 7 | $\sim 17$ |
| $\nu_3$ | $\Delta(1620)$ $(2,9)$ | 9 | $\sim 13$ |
| $\sum m_\nu$ | | | $\sim 0.054$ eV |

**Comparison:** The Planck 2018 cosmological bound is $\sum m_\nu < 0.12 \text{ eV}$, with hints at $\sim 0.06 \text{ eV}$. The AVE prediction of $0.054 \text{ eV}$ sits comfortably within this window.

## Schwinger's Anomalous Magnetic Moment ($g-2$)

The anomalous magnetic moment of the electron is derived from the on-site impedance correction of the hopping unknot.

When the unknot visits a lattice node, all $m_e c^2$ is stored in that cell as EM field energy, split equally between E and B:

$$
U_E = \frac{1}{2}\epsilon_0 E_{\text{peak}}^2 \ell^3 = \frac{m_e c^2}{2}
$$

Solving for the peak electric strain:

$$
\left(\frac{V_{\text{peak}}}{V_{\text{snap}}}\right)^2 = 4\pi\alpha \quad [\text{EXACT}]
$$

This is an identity: $\alpha$ *is* the on-site electric strain. The Axiom 4 nonlinear saturation modifies the node capacitance (*not* the constitutive permittivity):

$$
C_{node} = \frac{C_0}{\sqrt{1 - (V/V_{snap})^2}} \;\to\; \infty
$$

Time-averaged over the LC oscillation ($\langle\sin^2\rangle = 1/2$):

$$
\langle\delta C / C\rangle = \pi\alpha
$$

This shifts the LC resonance frequency by $\delta\omega/\omega = \pi\alpha/2$. The anomalous magnetic moment is the fraction of this correction that falls within the ring's topological domain (the form factor). The ring has diameter $2R = \ell/\pi$ (from $R = \ell/(2\pi)$, Axiom 1). Its effective cross-section in the cell face is:

$$
F = \frac{A_{\text{ring}}}{A_{\text{cell}}} = \frac{(2R)^2}{\ell^2} = \frac{1}{\pi^2}
$$

The full on-site correction $\pi\alpha/2$ decomposes:

$$
a_e = \frac{1}{\pi^2} \times \frac{\pi\alpha}{2} = \frac{\alpha}{2\pi} \approx 0.001161
$$

**This is Schwinger's result (1948).** The AVE framework derives it from three structural constants: the Axiom 4 squared saturation operator, the unknot ropelength, and the lattice pitch. No Feynman diagrams or renormalization are required.

## Summary of Electroweak Predictions

| Quantity | AVE Prediction | Experiment | Deviation |
|---|---|---|---|
| $\sin^2\theta_W$ (on-shell) | 0.2222 | 0.2230 | $-0.35\%$ |
| $M_W$ | 79,923 MeV | 80,379 MeV | $-0.57\%$ |
| $M_Z$ | 90,624 MeV | 91,188 MeV | $-0.62\%$ |
| $m_\mu$ | 107.0 MeV | 105.66 MeV | $+1.24\%$ |
| $m_\tau$ | 1,760 MeV | 1,776.9 MeV | $-0.95\%$ |
| $\sum m_\nu$ | $\sim 0.054$ eV | $<0.12$ eV | Within bound |
| $a_e$ (Schwinger) | $\alpha/(2\pi) = 0.001161$ | 0.001160 | $+0.09\%$ |

Every entry in this table is computed from the same three canonical hardware scales ($m_e$, $\alpha$, $G$ — all three themselves derived; see [Vol 1 Ch.8 Golden Torus α derivation](../../../vol1/ch8-alpha-golden-torus.md)) plus the Poisson ratio $\nu_{vac} = 2/7$ and the packing fraction $p_c = 8\pi\alpha$. No Standard Model parameters (Yukawa couplings, CKM matrix elements, or Higgs VEV) are used.

---
