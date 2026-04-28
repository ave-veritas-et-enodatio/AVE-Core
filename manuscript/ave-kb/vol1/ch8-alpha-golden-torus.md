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

**Identification step.** The sum decomposition

$$
\alpha^{-1}_{\text{ideal}} \;\equiv\; \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}
$$

is the *identification* of the three orthogonal codimensions of the Clifford torus embedding (3-torus phase volume, 2-torus surface, 1-loop line) with the three independent contributions to the dimensionless self-impedance of the trefoil soliton. Orthogonality of the three sectors — volumetric phase ($\propto R\,r\,r_{\text{phase}}$), surface area ($\propto R\,r$), and line magnetic moment ($\propto d$) — is what justifies the absence of cross-terms; each sector saturates a different geometric codimension. This is a *multipole identification*, parallel in spirit to the multipole expansion of any extended electromagnetic source, and not an additional derivation step beyond the three-regime closure above.

**Unified axiomatic origin of the $4\pi$ and $\pi^2$ factors.** Both the temporal double-cover (factor $4\pi$ in $\Lambda_{\text{vol}}$, via $r_{\text{phase}} = 2$) and the spatial half-cover (factor $\pi^2$ in $\Lambda_{\text{surf}}$) derive from the *same* structural fact: spin-1/2 is a representation of $SU(2)$, the double cover of $SO(3)$. The electron's internal phase space must traverse $4\pi$ of temporal phase to return to its initial spinorial state, but only $2\pi$ of spatial phase to close the spatial loop. The $4\pi$ factor in $\Lambda_{\text{vol}}$ and the half-cover in $\Lambda_{\text{surf}}$ are temporal and spatial expressions of the identical SU(2) double-cover structure — parallel, not ad hoc.

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

This is interpreted as the thermal expansion of the spatial metric at the current cosmological epoch ($T_{\text{CMB}} \approx 2.725\,$K).

**Status disclosure (current edition; predicted/fitted split).**

- *Predicted (axiom-derived):* the cold-lattice asymptote $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$; the existence of a positive thermal running of $\alpha^{-1}$ below this asymptote at any $T > 0$; the sign and the falsifiable claim that $\alpha^{-1}$ decreases further in regions of higher local thermal energy (collider cores, early universe).
- *Fitted (one scalar at $T_{\text{CMB}}$):* the numerical magnitude $\delta_{strain} \approx 2.225\times 10^{-6}$, computed by back-subtraction from CODATA: $\delta_{strain} \equiv 1 - \alpha^{-1}_{\text{CODATA}}/\alpha^{-1}_{\text{ideal}}$, definitional given the engine's `DELTA_STRAIN = 1 - (1/ALPHA)/ALPHA_COLD_INV` (`src/ave/core/constants.py`). The attribution to spatial-metric thermal expansion at $T_{\text{CMB}} = 2.725\,$K is a physical narrative consistent with the predicted sign; it is not yet a derivation of the magnitude from $T_{\text{CMB}}$ + a lattice elastic modulus.
- *Tested:* that **one** thermal scalar suffices to bridge the cold-lattice asymptote to the CODATA value. Multiple-temperature measurements of $\alpha$ (collider cores, primordial nucleosynthesis $\alpha$, ultracold cavity experiments) test the same one-scalar structural claim at different $T$.

This is the same disclosure pattern as Vol 6 (one fitted scalar per nucleus, with predicted topology + parameter count): structure predicted, magnitude fitted, falsifiable across the relevant variable. To upgrade $\delta_{strain}$ from a one-scalar fit to a true zero-parameter prediction, the chain needs to compute the lattice's effective thermal expansion coefficient from first principles — the bulk modulus $G_{vac}$ (Vol 1 Ch 4) and the equipartition energy at $T_{\text{CMB}}$ — and verify that the predicted $\delta_{strain}$ matches the back-subtracted value within tolerance. That magnitude-derivation does not currently appear in the corpus.

**Falsifiable prediction:** $\alpha$ is a literal mechanical property of the vacuum LC lattice and must act as a running coupling constant. In regions of extreme localized thermal energy (collider cores, early universe), $\alpha^{-1}$ decreases further below 137.036. The cold-lattice $137.0363038$ is the absolute-zero mathematical asymptote.

This is distinct from the proton thermal softening $\delta_{th} = 1/(14\pi^2) \approx 7.21 \times 10^{-3}$ at the $10^{13}$ K proton core — different temperature regime, different physical quantity (Skyrme coupling $\kappa_{FS}$), not $\alpha$ directly.

## Mathematical Closure

Axiom 1 calibrates $\ell_{\text{node}}$ to the ground-state rest-mass of the smallest topologically stable soliton (the electron ≡ unknot phase winding on the trefoil). Because the electron is the absolute structural failure mode of the lattice, its geometric packing Q-factor (137.036) *physically becomes* the macroscopic non-linear saturation limit for the rest of the universe. This is why $\alpha$ serves identically as the dielectric saturation bound in Axiom 4.

**Closure status (honest).** The framework reduces 26 Standard Model parameters to a 3-element bounding set $\{m_e, \alpha, G\}$ + four axioms. The "zero free parameters" claim depends on Layer 8 closure of those three, which itself rests on:
- (a) the Golden Torus $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi$ derivation above at the cold-lattice asymptote (the three regimes are independently grounded; the sum decomposition relies on identifying $\Lambda_{\text{vol}}$, $\Lambda_{\text{surf}}$, $\Lambda_{\text{line}}$ as the three orthogonal contributions);
- (b) the thermal running $\alpha^{-1}(T) = \alpha^{-1}_{\text{ideal}}(1 - \delta_{strain}(T))$: the existence and sign are predicted (positive $\delta_{strain}$ at $T > 0$); the magnitude at $T_{\text{CMB}}$ is currently one fitted scalar (back-subtracted from CODATA — see status disclosure above);
- (c) one of $\{m_e, \ell_{node}\}$ being computable from the other via the unknot ground state (the other remaining as the input mass scale).

Conditional on (a)–(c), the framework is zero-free-parameters at the SM level. Under the present edition, the cold-lattice asymptote and the existence + sign of the thermal running are predicted; the magnitude of $\delta_{strain}$ at $T_{\text{CMB}}$ is one fitted scalar — same predicted/fitted disclosure pattern as Vol 6 (predicted: structure; fitted: one scalar). See the [Full Derivation Chain](../common/full-derivation-chain.md) scorecard for the precise accounting.

---

> → Primary: [Calibration and Cutoff Scales](./axioms-and-lattice/ch1-fundamental-axioms/calibration-cutoff-scales.md) — prerequisite framing of $\ell_{\text{node}}$, $\alpha$, $G$
>
> → Primary: [Zero-Parameter Universe](./axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md) — original EMT-chain framing; this chapter provides the closure
>
> → Primary: [Full Derivation Chain](../common/full-derivation-chain.md) — Layer 8 Zero-Parameter Closure
>
> ↗ See also: [Vol 2 Ch 3 PMNS eigenvalues](../vol2/particle-physics/ch03-neutrino-sector/pmns-eigenvalues.md) — the three-regime rigor pattern this chapter applies
