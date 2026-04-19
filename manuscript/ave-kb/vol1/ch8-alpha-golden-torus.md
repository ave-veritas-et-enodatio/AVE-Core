[↑ Vol 1: Foundations](index.md)
<!-- leaf: verbatim -->

# Ch.8: Zero-Parameter Closure — $\alpha$ from the Golden Torus

**Source:** [`manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex`](../../vol_1_foundations/chapters/08_alpha_golden_torus.tex)

**Scripts:**
- [`derive_alpha_from_golden_torus.py`](../../../src/scripts/vol_1_foundations/derive_alpha_from_golden_torus.py) — multipole evaluation, renders Fig. of trefoil at Golden Torus
- [`verify_clifford_half_cover.py`](../../../src/scripts/vol_1_foundations/verify_clifford_half_cover.py) — rigorous 5-step derivation of $\Lambda_{\text{surf}} = \pi^2$ from spin-1/2 half-cover
- [`ropelength_trefoil_golden_torus.py`](../../../src/scripts/vol_1_foundations/ropelength_trefoil_golden_torus.py) — numerical convergence of composite ropelength + screening objective to Golden Torus
- [`verify_golden_torus_s11.py`](../../../src/scripts/vol_1_foundations/verify_golden_torus_s11.py) — ABCD cascade infrastructure + algebraic verification

**Engine constants** (from [`ave.core.constants`](../../../src/ave/core/constants.py)):
- `ALPHA_COLD_INV` $= 4\pi^3 + \pi^2 + \pi \approx 137.0363038$
- `ALPHA_COLD` $= 1/\text{ALPHA\_COLD\_INV}$
- `DELTA_STRAIN` $\approx 2.225 \times 10^{-6}$ (CMB thermal correction)

## Derivation Summary (Three-Regime Rigor)

Following the PMNS angle derivation pattern ([Vol 2 Ch 3 §Step 2](../vol2/particle-physics/ch03-neutrino-sector/pmns-eigenvalues.md)) — which rigorously produces three mixing-angle values by identifying three distinct physical regimes — the trefoil's geometric constraints partition into three regimes, each producing one independent equation in the unknowns $(R, r, d)$:

| Regime | Physical principle | Equation |
|---|---|---|
| **(a) Nyquist** | Discrete lattice sampling cutoff (Axiom 1); smallest stable soliton = trefoil | $d = 1\,\ell_{\text{node}}$ |
| **(b) Crossings** | Transverse self-avoidance at topologically-marked trefoil crossings (Axiom 2 dielectric rupture) | $2(R-r) = d \Rightarrow R - r = 1/2$ |
| **(c) Screening** | Spin-1/2 half-cover of the standard Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ (SU(2) double-cover of SO(3)) | $(2\pi R)(2\pi r) = \pi^2 \Rightarrow R \cdot r = 1/4$ |

**Rigor for regime (c):** The standard Clifford torus $(z_1, z_2) = (r_1 e^{i\theta_1}, r_2 e^{i\theta_2})$ at $r_1 = r_2 = 1/\sqrt{2}$ on $S^3$ has total surface area $A_{\text{standard}} = 2\pi^2$ (theorem of complex geometry on $S^3$). The electron's spin-1/2 structure — the same SU(2) double-cover that introduces the $4\pi$ temporal factor in $\Lambda_{\text{vol}}$ — implies only half of the Clifford torus corresponds to physically distinct observables (the other half is the spin-conjugate image). Therefore $\Lambda_{\text{surf}} = \tfrac{1}{2} A_{\text{standard}} = \pi^2$, exact and forced by topology.

**Solving (b) ∧ (c):** substitute $r = R - 1/2$ into $R \cdot r = 1/4$:
$$
R(R - 1/2) = 1/4 \implies 2R^2 - R - 1/2 = 0 \implies R = \frac{1 + \sqrt{5}}{4} = \frac{\varphi}{2}
$$
giving the **Golden Torus**: $R = \varphi/2 \approx 0.809$, $r = (\varphi-1)/2 \approx 0.309$.

## Holomorphic Multipole Decomposition

At the Golden Torus, the holomorphic impedance decomposes into three orthogonal geometric dimensions. With $R \cdot r = 1/4$ and $d = 1$:

| Shape factor | Formula | Value | Physical meaning |
|---|---|---|---|
| $\Lambda_{\text{vol}}$ | $(2\pi R)(2\pi r)(2\pi \cdot 2) = 16\pi^3(R \cdot r)$ | $4\pi^3 \approx 124.025$ | 3-torus phase volume with spin-1/2 $4\pi$ double-cover |
| $\Lambda_{\text{surf}}$ | $(2\pi R)(2\pi r) = 4\pi^2(R \cdot r)$ | $\pi^2 \approx 9.870$ | Clifford torus ($S^1 \times S^1$) half-cover |
| $\Lambda_{\text{line}}$ | $\pi \cdot d$ | $\pi \approx 3.142$ | Core-loop magnetic moment at min. node thickness $d = 1$ |

> **[Resultbox]** *Cold-Lattice Fine-Structure Constant*
>
> $$
> \alpha^{-1}_{\text{ideal}} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038
> $$

## CMB Thermal Correction (Running $\alpha$)

The experimentally measured CODATA value is $\alpha^{-1}_{\text{exp}} = 137.035999$. This is below the cold-lattice asymptote by a fractional amount identified as the Vacuum Strain Coefficient:

$$
\delta_{\text{strain}} = 1 - \frac{137.035999}{137.036304} \approx 2.225 \times 10^{-6}
$$

This is the thermal expansion of the spatial metric at the current cosmological epoch ($T_{\text{CMB}} \approx 2.7\,$K).

**Falsifiable prediction:** $\alpha$ is a literal mechanical property of the vacuum LC lattice and must act as a running coupling constant. In regions of extreme localized thermal energy (collider cores, early universe), $\alpha^{-1}$ decreases further below 137.036. The cold-lattice $137.0363038$ is the absolute-zero mathematical asymptote.

This is distinct from the proton thermal softening $\delta_{th} = 1/(14\pi^2) \approx 7.21 \times 10^{-3}$ at the $10^{13}$ K proton core — different temperature regime, different physical quantity (Skyrme coupling $\kappa_{FS}$), not $\alpha$ directly.

## Mathematical Closure

Axiom 1 calibrates $\ell_{\text{node}}$ to the ground-state rest-mass of the smallest topologically stable soliton (the electron ≡ unknot phase winding on the trefoil). Because the electron is the absolute structural failure mode of the lattice, its geometric packing Q-factor (137.036) *physically becomes* the macroscopic non-linear saturation limit for the rest of the universe. This is why $\alpha$ serves identically as the dielectric saturation bound in Axiom 4.

The framework is **genuinely zero free parameters**: all 26 Standard Model constants are determined by four axioms plus the topological requirement that the smallest stable soliton is the trefoil ($3_1$).

---

> → Primary: [Calibration and Cutoff Scales](./axioms-and-lattice/ch1-fundamental-axioms/calibration-cutoff-scales.md) — prerequisite framing of $\ell_{\text{node}}$, $\alpha$, $G$
>
> → Primary: [Zero-Parameter Universe](./axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md) — original EMT-chain framing; this chapter provides the closure
>
> → Primary: [Full Derivation Chain](../common/full-derivation-chain.md) — Layer 8 Zero-Parameter Closure
>
> ↗ See also: [Vol 2 Ch 3 PMNS eigenvalues](../vol2/particle-physics/ch03-neutrino-sector/pmns-eigenvalues.md) — the three-regime rigor pattern this chapter applies
