[↑ Ch.2 Topological Thrust Mechanics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [0vxzfu, trgqtf, 7tynm2]
-->

## Regimes of Operation
<!-- claim-quality: trgqtf -->

Before deriving the thrust mechanism, it is essential to establish *which operating regime* a laboratory-scale device occupies within the Axiom 4 saturation landscape. The constitutive circuit models define the yield voltage as $V_{yield} = \sqrt{\alpha}\,V_{snap} \approx 43.65$ kV. This yield applies *per lattice node*, i.e., across a single node spacing $\ell_{node} = \hbar / (m_e c) = 3.862 \times 10^{-13}$ m.

The corresponding electric field yield threshold is therefore:

> **[Resultbox]** *Dielectric Yield Field Strength*
>
> $$
> E_{yield} = \frac{V_{yield}}{\ell_{node}} = \frac{\sqrt{\alpha}\, m_e^2 c^3}{e\, \hbar} \approx 1.13 \times 10^{17} \text{ V/m}
> $$

This field strength exceeds the classical Schwinger limit of QED ($E_S = m_e^2 c^3 / e\hbar \approx 1.32 \times 10^{18}$ V/m) by a factor of $\sqrt{\alpha}$. For comparison, the strongest sustained laboratory fields are $\sim 10^{10}$ V/m (ultrafast laser foci), seven orders of magnitude below $E_{yield}$.

**Regime Classification.** The saturation factor $S(E) = \sqrt{1 - (E/E_{yield})^2}$ defines four operating regimes:

| **Regime** | $E / E_{yield}$ | $\varepsilon_{eff} / \varepsilon_0$ | **Physics** |
|---|---|---|---|
| I. Linear | $< 0.1$ | $> 0.995$ | Standard Maxwell |
| II. Weakly non-linear | $0.1$--$0.5$ | $0.87$--$0.995$ | Euler--Heisenberg analogue |
| III. Strongly non-linear | $0.5$--$1.0$ | $0$--$0.87$ | Metric varactor |
| IV. TVS breakdown | $\geq 1.0$ | $0$ | Phase transition |

**Implication for PONDER-01.** An asymmetric capacitor driven at 30 kV with a 1 mm gap produces $E \approx 3 \times 10^7$ V/m. The saturation ratio $E/E_{yield} \approx 2.7 \times 10^{-10}$ places the device firmly in **Regime I** (linear vacuum). The bulk dielectric permittivity $\varepsilon_0$ is essentially unperturbed. Consequently, *bulk $\varepsilon$-saturation is not the operative thrust mechanism*. The field gradients do not approach the levels required to produce measurable non-linear vacuum permittivity.

**Where saturation is physical.** Regime III and IV are reached only at sub-femtometer separations---i.e., within particle cores, at nuclear scattering boundaries, and at event horizons. This is consistent with the role of Axiom 4 in producing the Pauli exclusion wall, the nuclear repulsive core, and the photon sphere, as derived in Volume II.

<!-- claim-quality: 7tynm2 (this paragraph identifies PONDER-01 chiral acoustic rectification — the $F_{total} = N \cdot \nu_{vac} \cdot \delta(Q,\beta) \cdot P_{in}/c$ thrust mechanism — as the operative channel given the linear-regime regime classification above) -->
The operative thrust mechanism must therefore arise from a different physical channel: the *chiral topology* of the HOPF-01 torus knot antenna producing asymmetric acoustic emission into the lattice.

### Yield Threshold Selection: $V_{yield}$ vs $V_{snap}$
<!-- claim-quality: 0vxzfu -->

The AVE framework defines two physically distinct voltage thresholds:

| Threshold | Value | Physical Meaning |
|---|---|---|
| $V_{snap}$ | 511 kV ($m_e c^2/e$) | Absolute topological node destruction |
| $V_{yield}$ | 43.65 kV ($\sqrt{\alpha}\,V_{snap}$) | Macroscopic nonlinear onset |

$V_{snap}$ is the correct yield for subatomic simulations (bond energy, confinement, nuclear scattering). $V_{yield}$ is the macroscopic onset — analogous to the distinction between theoretical crystal shear strength and engineering yield stress.

**Engine defaults**: macroscopic solvers (`fdtd_3d`, `k4_tlm`, `saturation.py`) → $V_{yield}$; scale-invariant primitives (`scale_invariant.py`) → $V_{snap}$.

| Domain | Yield Parameter | Rationale |
|---|---|---|
| Engineering (PONDER, antennas, IMD) | $V_{yield}$ (default) | Macroscopic $\varepsilon$-saturation onset |
| Gravitational wave propagation | $V_{snap}$ | Tests against absolute topological limit |
| Particle physics (confinement, decay) | $V_{snap}$ | Voltage applied at lattice pitch |
| Nuclear bond energy | $V_{snap}$ | Sub-node scale |

### Numerical Convergence: $V_{yield}$ vs $V_{snap}$

At PONDER field strengths (≤ 1 MV/m), both yields produce **identical results to 4+ significant figures**:

| Amplitude | Strain ($V_{snap}$) | Strain ($V_{yield}$) | Energy Ratio |
|---|---|---|---|
| 100 kV/m | $1.06 \times 10^{-4}$ | $1.24 \times 10^{-3}$ | 1.000000 |
| 1 MV/m | $1.06 \times 10^{-3}$ | $1.24 \times 10^{-2}$ | 0.999933 |
| 5 MV/m | $5.31 \times 10^{-3}$ | $6.21 \times 10^{-2}$ | 0.998334 |

The $V_{yield}$ default is an axiomatic correctness fix — it flags nonlinearity 11.7× earlier without altering existing predictions.

---
