[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Summary: Zero-Parameter Count

The engine contains:

- **0** trainable / fitted parameters
- **0** empirical structural data (PDB coordinates enter only as comparison targets)
- **21** derived physical constants (Table in [Axiom-Derived Constants](./axiom-derived-constants.md) + $R_\text{damp}$, $f_0$, $\varepsilon_\infty$), all traceable to Axioms 1--4
- **4** measured boundary conditions ($D_\text{SS}$, $\tau_\text{D}$, $\varepsilon_s$, amino acid masses) --- not derivable from AVE axioms
- **20** complex $Z_{topo}$ values (Table in [Z Topo Complex Table](./z-topo-complex-table.md)), computed *ab initio* via $Z_{topo} = \sqrt{L_R/C_R}/\sqrt{L_\text{bb}/C_\text{bb}}$
- **7** universal operators (Table below), shared with nuclear and antenna domains
- **1** objective function: $\lambda_{\min}(S^\dagger S)$ with Axiom 4 packing saturation
- **11** physics layers composing the loss (8 core + 3 v4 extensions)

The force on each residue $\mathbf{F}_i = -\partial \mathcal{L} / \partial \mathbf{r}_i$ is computed exactly by reverse-mode automatic differentiation in a single forward--backward pass. No finite-difference approximation, no force constants, no statistical potentials.

## Universal Operator Cross-Reference

Unified mapping of all seven universal operators to the AVE axioms, applicable regimes, regime boundary conditions, and application domains. Each operator is implemented once in the physics engine and called at every scale.

Regime boundaries: $r_1 = \sqrt{2\alpha} \approx 0.121$ (linear limit), $r_2 = \sqrt{3}/2 \approx 0.866$ (yield onset), $r_3 = 1.0$ (topology destroyed).

| **Op** | **Name** | **Formula** | **Axiom** | **Regimes** | **Applications** |
|---|---|---|---|---|---|
| 1 | Impedance | $Z = \sqrt{\mu/\varepsilon}$ | 1 | I--IV (invariant under symmetric sat.) | Vacuum, plasma, seismic, gravity, protein, antenna, fluid, galactic |
| 2 | Saturation | $S = \sqrt{1-r^2}$ | 4 | II--III ($r_1 < r < r_3$); trivial in I, singular in IV | BCS, pair production, galactic rotation, Bingham yield, confinement |
| 3 | Reflection | $\Gamma = (Z_2{-}Z_1)/(Z_2{+}Z_1)$ | 1, 2 | I--IV (at every impedance boundary) | Pauli exclusion, Moho, antenna $S_{11}$, seismic, neutrino mixing |
| 4 | Pairwise energy | $U = -(K/r)(1-2\Gamma^2)$ | 1, 2 | I--III ($r < r_3$); repulsive when $r \geq 1$ | Nuclear binding, covalent bonds, molecular solitons |
| 5 | Y$\to$S matrix | $(I+Y/Y_0)^{-1}(I-Y/Y_0)$ | 1 | I--IV (multiport generalisation of Op 3) | Nuclear $K_\text{MUTUAL}$, protein fold, antenna network |
| 6 | Eigenvalue target | $\lambda_{\min}(S^\dagger S)$ | 1 | I--III (ground state at $\lambda \to 0$) | Nuclear binding, protein native fold, antenna match |
| 7 | Spectral analysis | FFT + PSD + autocorr | 1, 2 | I--IV (frequency-domain complement to time-domain SPICE) | SS prediction, contact order, impedance profile diagnostics |

## Regime Boundary Conditions

The three regime boundaries gate which operators are active:

- **$r < r_1 = \sqrt{2\alpha}$ (Regime I, Linear):**
  Op 2 (saturation) is sub-$\alpha$ and ignorable. Ops 1, 3--7 operate with standard constitutive parameters. Protein folding (biological temperature) operates here.

- **$r_1 \leq r < r_2 = \sqrt{3}/2$ (Regime II, Nonlinear):**
  Op 2 active; $\varepsilon_\text{eff}, \mu_\text{eff}$ modified. Quality factor $Q(r) = 1/S(r) < 2$. Nuclear binding, BCS operation.

- **$r_2 \leq r < r_3 = 1$ (Regime III, Yield):**
  $Q \geq 2$ --- energy trapping dominates. Op 4 transitions from attractive to repulsive. Phase transitions, particle confinement.

- **$r \geq r_3 = 1$ (Regime IV, Ruptured):**
  $S = 0$; Op 2 singular. Topology destroyed (pair production, event horizon, deconfinement).

**Key design principle:** the protein folding solver operates entirely in **Regime I**. The biological operating point ($r \approx 10^{-6}$) is deep in the linear regime, where $S \approx 1$ and all operators reduce to their standard (unmodified) forms. The saturation operator (Op 2) enters only through the Axiom 4 packing factor $S_\text{pack} = \sqrt{1 - (\eta/P_C)^2}$, which enforces global equilibrium density --- not local field saturation.

## Axiom 4 Saturation Operators

The engine contains five Axiom 4 saturation operators, each governing a distinct coupling regime:

| **#** | **Operator** | **Formula** | **Regime** |
|---|---|---|---|
| 1 | C$_\text{sat}$ | $1/\sqrt{1-r^2}$ | Contact boost (Lorentz $\gamma$) |
| 2 | Saturation envelope | $\sqrt{1-(d/R)^2}$ | Long-range cutoff |
| 3 | Q-decay | $e^{-\Delta i / 2\pi Q}$ | Sequence attenuation |
| 4 | $S(\eta)$ global | $\sqrt{1-(\eta/P_C)^2}$ | Packing saturation |
| 5 | $S_{11}$ trace reversal | $S_{11}\sqrt{1-S_{11}^2}$ | Loss saturation |

Operator 1 (Lorentz boost) is the only operator that *diverges*: $C_\text{sat} \to \infty$ at contact distance $d = d_0$, requiring a numerical clip at $r = 0.95$. All other operators are bounded. Testing a unified galactic-form profile $\sqrt{x(2-x)}$ (which peaks finitely at $d_0$) confirmed that this boost is necessary for sufficient compaction under the current architecture---removing it causes loss to increase $5\times$ and SS to vanish.

---
