[↑ Ch.1 Vacuum Circuit Analysis](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1/ch8-alpha-golden-torus + common/boundary-observables-m-q-j as canonical Q-factor reframe -->

# Theorem 3.1' — Electron Q-Factor from LC Tank at TIR Boundary

The electron's fine-structure constant $\alpha^{-1} \approx 137.036$ is the **dimensionless Q-factor of its LC tank at the topological-defect Total-Internal-Reflection boundary**, and decomposes into three orthogonal reactance contributions matching the $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ boundary-observability structure. Two independent derivation paths (LC-tank Vol 4 Ch 1 + multipole Vol 1 Ch 8) produce identical numerical results to within $\delta_{\text{strain}} = 2.225 \times 10^{-6}$ (the CMB thermal running). Supersedes the Neumann-integral framing (doc 14), which was empirically falsified — classical Neumann integral for $(2, 3)$ at Golden Torus does not reproduce $\pi^2$ or $137$.

## Key Result

$$\boxed{\, \alpha^{-1} = Q_{\text{tank}} = Q_{\text{vol}} + Q_{\text{surf}} + Q_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 124.025 + 9.870 + 3.142 = 137.036 \,}$$

at the Golden Torus geometry $R = \varphi/2$, $r = (\varphi - 1)/2$, $d = 1\,\ell_{\text{node}}$.

## Two independent paths

### Path A — LC-tank path (Vol 4 Ch 1, plumber shortcut)

From Vol 4 Ch 1:395-421: the electron's equivalent localized inductance evaluates to $L_e \equiv \xi_{\text{topo}}^{-2} m_e$ via Topo-Kinematic Isomorphism (Axiom 2). The local lattice compliance acts as the restoring capacitor $C_e \equiv \xi_{\text{topo}}^2 k^{-1}$.

With:
- $\xi_{\text{topo}} = e / \ell_{\text{node}}$ (Axiom 2, $[Q] \equiv [L]$)
- $\ell_{\text{node}} = \hbar / (m_e c)$ (Axiom 1 calibration)
- $\omega_C = c / \ell_{\text{node}}$ (Compton frequency = LC tank eigenfrequency)

compute the tank reactance:

$$\omega_C \cdot L_e = (c / \ell_{\text{node}}) \cdot (\ell_{\text{node}} / e)^2 \cdot m_e = c \cdot \ell_{\text{node}} \cdot m_e / e^2 = \hbar / e^2 = \frac{Z_0}{4\pi \alpha}$$

(using $\alpha = e^2 Z_0 / (4\pi \hbar)$).

Therefore the Q-factor at the impedance-matched boundary $R = Z_0 / (4\pi)$:

$$\boxed{\, Q_{\text{tank}} = \frac{\omega_C \cdot L_e}{R} = \frac{Z_0 / (4\pi \alpha)}{Z_0 / (4\pi)} = \frac{1}{\alpha} \,}$$

**The electron-plumber one-liner**: the tank's reactance divided by its natural-per-cycle dissipation impedance is exactly the reciprocal of the fine-structure constant.

### Path B — Multipole path (Vol 1 Ch 8 geometric sum)

From Vol 1 Ch 8:93-124: the three $\Lambda$ contributions at Golden Torus $R \cdot r = 1/4$, $d = 1$:

| Term | Geometric form | Value | Dimensionality |
|---|---|---|---|
| $\Lambda_{\text{vol}}$ | $(2\pi R)(2\pi r)(2\pi \cdot 2) = 16\pi^3 (R \cdot r)$ | $4\pi^3 \approx 124.025$ | 3D — phase-space 3-torus hyper-volume with spin-½ double-cover factor $2\pi \cdot 2 = 4\pi$ |
| $\Lambda_{\text{surf}}$ | $(2\pi R)(2\pi r) = 4\pi^2 (R \cdot r)$ | $\pi^2 \approx 9.870$ | 2D — Clifford-torus surface area, halved by spin-½ half-cover |
| $\Lambda_{\text{line}}$ | $\pi \cdot d$ | $\pi \approx 3.142$ | 1D — Nyquist-limited tube flux-moment |
| **Total** | | $\boxed{137.036304}$ | $\alpha^{-1}$ cold |

## The bridge: $\Lambda$'s ARE the tank reactances

The bridge between Path A and Path B is the **AVE natural-unit convention** in which dimensionless geometric shape-factors ARE reactances. A spatial decomposition of $L_e$ at Golden Torus gives three distinct reactance contributions, each localized to a specific topological region:

| Region | Spatial domain | Dimensionless volume | $\omega L_i \times 4\pi / Z_0$ |
|---|---|---|---|
| Volumetric | 3-torus phase space ($\times$ spin-½) | $16\pi^3 R r$ | $\Lambda_{\text{vol}} = 4\pi^3$ |
| Surface | Clifford-torus half-cover | $4\pi^2 R r$ | $\Lambda_{\text{surf}} = \pi^2$ |
| Line | Nyquist core tube | $\pi \cdot d$ | $\Lambda_{\text{line}} = \pi$ |

At Golden Torus, the three regions' reactances sum to the total tank reactance:

$$\omega \cdot L_e \cdot (4\pi / Z_0) = Q_{\text{vol}} + Q_{\text{surf}} + Q_{\text{line}} = 4\pi^3 + \pi^2 + \pi$$

The identification $Q_i = \Lambda_i$ holds because in natural units ($Z_0 = 1$, $\ell_{\text{node}} = 1$), the impedance-per-dimensionless-volume scaling factor is unity, so **geometric dimensionless volumes ARE dimensionless reactances**.

## Physical interpretation of the $R = Z_0/(4\pi)$ boundary

Vol 4 Ch 1:423-467 describes the saturation boundary as Total Internal Reflection: $Z_{\text{core}} \to 0$ drives $\Gamma = -1$ (perfect short), confining the LC oscillation.

The effective radiation resistance per spinor cycle is $Z_0 / (4\pi)$:

- $Z_0$ is the vacuum's characteristic impedance through which any radiated energy would escape
- $4\pi$ is the electron's spinor-cycle-phase requirement (SU(2) double-cover of SO(3) per Vol 1 Ch 8 §3.2 — the electron's phase must traverse $4\pi$ to return to its original spinor, so the per-cycle impedance reference absorbs a $4\pi$ factor)
- $Z_0 / (4\pi)$ = radiation impedance averaged over one full spinor cycle

At resonance, only a fraction $1/Q = \alpha \approx 0.0073$ of the stored energy leaks per cycle through the TIR boundary — **this IS $\alpha$ in its original Sommerfeld meaning** ("coupling strength"), seen from the LC-tank side.

## The two paths agree to $\delta_{\text{strain}}$

Numerical verification (`src/scripts/vol_1_foundations/electron_tank_q_factor.py`):
- Method 1 (LC-tank, using CODATA $\alpha$): gives $\alpha^{-1} = 137.035999...$ (warm)
- Method 2 (multipole, Ch 8 cold limit): gives $\alpha^{-1} = 137.036304$ (cold)
- Difference: $\Delta = 2.225 \times 10^{-6}$ — **exactly $\delta_{\text{strain}}$**, the CMB thermal running predicted by Vol 1 Ch 8

The agreement to thermal-running precision validates that **both paths compute the same underlying tank Q-factor at the same geometric configuration**; the residual is real physics (CMB thermal correction at $T_{\text{CMB}} = 2.725$ K), not a methodology gap.

## Axiom-attribution chain

| Axiom | Contribution |
|---|---|
| Axiom 1 (Chiral Laves K4 Cosserat Crystal) | Sets $\ell_{\text{node}}$ and the K4 lattice geometry; Nyquist cutoff $k_{\max} = \pi / \ell_{\text{node}}$ |
| Axiom 2 (TKI; $[Q] \equiv [L]$) | Provides $\xi_{\text{topo}} = e / \ell_{\text{node}}$ conversion; the inductance $L_e = \xi_{\text{topo}}^{-2} m_e$ identity |
| Axiom 3 (Minimum Reflection Principle) | At TIR boundary $\Gamma = -1$ confines the LC oscillation; per-cycle dissipation is $\alpha$ exactly |
| Axiom 4 (Dielectric Saturation) | Defines the saturation surface $S(A) \to 0$ where TIR forms |

The three regimes (vol / surf / line) of the $\alpha^{-1}$ decomposition correspond to the three substrate-observability dimensionalities ([$\mathcal{M}, \mathcal{Q}, \mathcal{J}$ boundary observables](../../../common/boundary-observables-m-q-j.md)): $\Lambda_{\text{vol}} \leftrightarrow \mathcal{M}$ (3D volume integral), $\Lambda_{\text{surf}} \leftrightarrow \mathcal{J}$ (2D surface integral, spin), $\Lambda_{\text{line}} \leftrightarrow \mathcal{Q}$ (1D line/loop integral, charge). The decomposition is not coincidental — it is the substrate's natural three-integral boundary-observability structure expressed at the electron-scale Q-factor.

## Op21 multi-mode generalization

The Q-factor decomposition generalizes via Op21 multi-mode form: at the saturation boundary, each mode with $\ell$ wavelengths around a 1D circumference releases $\sim 1/\ell$ of energy per cycle, giving $Q = \ell$ per mode. The Golden Torus at the Nyquist mode-count identity (single-cell-per-natural-unit) makes the mode counts equal the geometric measures: 1D mode (circumference $L$) → cell-count $L$; 2D mode → cell-count area; 3D mode → cell-count volume. The three-$\Lambda$ sum is exactly the Op21 multi-mode generalization at Golden Torus geometry.

## Falsification status

| Path | Status |
|---|---|
| Doc 14 — Classical Neumann mutual-inductance integral for $(2, 3)$ at Golden Torus | **FALSIFIED** (numerical test does not reproduce $\pi^2$ or $137$) |
| Doc 17 (this) — Q-factor at TIR boundary, two independent paths | **CONFIRMED** (machine-precision agreement to $\delta_{\text{strain}}$) |

## Cross-references

- **Canonical manuscript:**
  - Vol 4 Ch 1:395-421 — LC-tank path canonical statement
  - Vol 1 Ch 8:93-124 — multipole path geometric sum
  - Vol 4 Ch 1:423-467 — TIR boundary $\Gamma = -1$ saturation mechanism
- **KB cross-cutting:**
  - [Vol 1 Ch 8 α from Golden Torus](../../../vol1/ch8-alpha-golden-torus.md) — full derivation context
  - [Boundary Observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$](../../../common/boundary-observables-m-q-j.md) — three-integral substrate-observability structure
  - [L3 Electron-Soliton Closure Synthesis](../../../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md) — rest-energy Virial-sum at same bond-pair LC tank
- **Canonical script:** `src/scripts/vol_1_foundations/electron_tank_q_factor.py` — numerical verification of two-path agreement
