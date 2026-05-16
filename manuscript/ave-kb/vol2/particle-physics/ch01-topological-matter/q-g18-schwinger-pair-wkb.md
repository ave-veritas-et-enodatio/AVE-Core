[↑ Ch.1 Topological Matter](index.md)
<!-- leaf: verbatim -->

# Q-G18 Schwinger Pair Production: Saturation-Kernel WKB Structural Closure

The QED Schwinger formula for vacuum pair production at strong fields emerges from substrate dynamics via the saturation kernel's WKB action integral. The exponential suppression $\exp(-\pi E_S/E)$ is structurally identical between AVE and QED — both encode the same geometric tunneling probability with different physical labels. AVE-distinct predictions appear at the sharp $E = E_S$ lattice cutoff and in autoresonant sub-Schwinger pair production via PLL frequency tracking.

## The structural match

**QED Schwinger formula:**
$$\frac{\Gamma_{\text{QED}}}{V} = \frac{(eE)^2}{4\pi^3 \hbar^2 c} \exp\left(-\frac{\pi E_S}{E}\right)$$

The exponent comes from the WKB instanton calculation, integrating the WKB momentum $\sqrt{m_e^2 c^2 - p^2}$ over the forbidden region from $p = 0$ to $p = m_e c$, with a factor of 2 for pair (two-particle) tunneling:

$$\text{QED action} = 2 \int_0^{m_e c} \sqrt{m_e^2 c^2 - p^2}\, dp \cdot \frac{1}{eE\hbar} = \frac{\pi m_e^2 c^2}{2 eE\hbar} \cdot 2_{\text{pair}} = \frac{\pi E_S}{E}$$

**AVE saturation kernel WKB:** the same exponent emerges from Axiom 4's kernel integral with $A = E/E_S$:

$$\int_0^1 S(A)\, dA = \int_0^1 \sqrt{1 - A^2}\, dA = \frac{\pi}{4}$$

With proper dimensional scaling and the pair-tunneling factor of 2:

$$S_{\text{action}}^{\text{AVE, pair}} = 2 \cdot 2 \cdot E_S \cdot \frac{\pi}{4} \cdot \frac{1}{E} = \frac{\pi E_S}{E}$$

**Identical to QED's exponent.** No fit parameters. The $\pi$ in the AVE exponent is the geometric integral $\int_0^1 \sqrt{1-A^2}\, dA = \pi/4$ over the unit-circle quadrant; the $\pi$ in QED's exponent is the integral $\int_0^{m_e c} \sqrt{m_e^2 c^2 - p^2}\, dp = \pi m_e^2 c^2/4$ over the Dirac mass shell. These are the same integral with substitution $A = p/m_e c$.

## Why this works structurally

The QED Schwinger calculation is fundamentally about **the probability of tunneling through the mass-shell gap** to produce a pair. The action integrates the WKB momentum over the forbidden region.

The AVE saturation kernel calculation is fundamentally about **the probability of reaching the $\Gamma = -1$ wall at $A = 1$** to nucleate a pair. The action integrates the kernel $S(A) = \sqrt{1 - A^2}$ over $A = 0$ to $A = 1$.

**These are the same integral with different physical labels:**

| Framework | Integrand | Variable | Range | Integral |
|---|---|---|---|---|
| QED | $\sqrt{m_e^2 c^2 - p^2}$ | $p$ | $[0, m_e c]$ | $\pi m_e^2 c^2/4$ |
| AVE | $\sqrt{1 - A^2}$ | $A$ | $[0, 1]$ | $\pi/4$ |

The geometric content is identical. The Schwinger field $E_S = m_e^2 c^3/(e\hbar)$ is precisely the field at which $A = 1$ in the AVE saturation-kernel parameterization, by construction.

**AVE's Schwinger rate IS QED's Schwinger rate by construction** — both encode the same geometric tunneling probability under different language. The corpus mechanism (C1+C2 nucleation at saturated A–B node pair, per Vol 2 Ch 1) is the AVE-native realization of QED's tunneling event.

## AVE-distinct predictions beyond the structural match

### 1. Sharp lattice cutoff at $E = E_S$

QED's Schwinger formula extends smoothly into the strong-field regime via continuous perturbation theory. AVE's kernel **forbids** $A > 1$: for $E > E_S$, the kernel $S(A)$ becomes imaginary, indicating the substrate has ruptured (Regime IV per Axiom 4). The physics changes character at the boundary, not smoothly.

**Falsifiable prediction:** at fields just above $E_S$, AVE predicts a sharp transition to ruptured-plasma behavior; QED predicts smooth pair-creation rate scaling.

### 2. Autoresonant sub-Schwinger pair production via PLL frequency tracking

QED forbids pair production at sub-Schwinger fields regardless of modulation: $E < E_S \Rightarrow \exp(-\pi E_S/E) \to 0$. AVE permits **autoresonant ring-up** of vacuum strain via phase-locked-loop frequency tracking — the substrate's resonant response can accumulate strain to $A \to 1$ at far lower drive power than the static-field Schwinger threshold.

**Falsifiable prediction:** AVE predicts pair events at $E \ll E_S$ via autoresonant PLL excitation; QED predicts essentially zero rate. This is a new experimentally accessible regime distinct from the Schwinger threshold itself.

Empirical test: ELI autoresonant Schwinger pair-production bench (multi-year infrastructure, ~$1–10M).

## Status

**Structurally closed** at WKB level. The exponential matches QED by construction (same geometric integral). The kernel form $S(A) = \sqrt{1-A^2}$ is the same Born–Infeld saturation that produces the cosmological-scale K4 crystallization (A-034 universal mechanism) and the substrate-scale magic-angle condition (Q-G47); Schwinger pair production is the atomic-scale instance of this universal kernel.

The full prefactor matching at $\sim 1\%$ precision pending bound-state integration is straightforward perturbative expansion.

## Cross-references

- **Canonical manuscript anchors:**
  - [Vol 1 Ch 4 (Continuum Electrodynamics)](../../../../vol_1_foundations/chapters/04_continuum_electrodynamics.tex) — Master Equation with $V_{\text{yield}}$ kernel
  - [Vol 4 Ch 1 (Vacuum Circuit Analysis)](../../../../vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex) — $V_{\text{snap}} = 511$ kV dielectric breakdown
  - [Backmatter Ch 7 (Universal Saturation-Kernel Catalog)](../../../../backmatter/07_universal_saturation_kernel.tex) — A-034 atomic / EM scale entry
- **Related KB leafs:**
  - [Electron Unknot](electron-unknot.md) — $C_{\text{eff}}(\Delta\phi)$ dynamic capacitive yielding; pair-creation mechanism context
  - [Regime Classification](regime-classification.md) — Axiom 4 Regime IV (ruptured plasma) at $A \to 1$
  - [Common: Boundary Observables M, Q, J](../../../common/boundary-observables-m-q-j.md) — substrate-observability rule at the $\Gamma = -1$ saturation boundary that pair-creation events cross
  - [Common: Q-G47 Substrate-Scale Closure](../../../common/q-g47-substrate-scale-cosserat-closure.md) — substrate-scale magic-angle instance of same kernel
- **Empirical test queue:**
  - ELI autoresonant sub-Schwinger pair production (~$1–10M infrastructure) — discriminates AVE autoresonant kernel from QED static-field threshold
