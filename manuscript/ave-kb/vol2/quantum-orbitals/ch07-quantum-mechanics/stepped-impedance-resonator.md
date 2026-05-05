[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [oltvwy]
-->

## The Atom as a Stepped Impedance Resonator


The Phase~A cavity ODE computes $E_\text{base}$ using a continuous impedance taper $Z_\text{net}(r)$ from smooth hydrogenic screening CDFs (Axiom~2).  However, a filled inner shell is not a gradual taper---it is a Pauli-saturated torus (Axiom~3) that presents a **discrete impedance step** at the shell boundary.  When the smooth CDF underestimates this step, the outer soliton's inner-lobe amplitude is overestimated, inflating $E_\text{base}$.

This section derives the correction analytically from the existing universal operators.

### Impedance Contrast at the Saturated-Torus Boundary

Consider an atom with nuclear charge $Z$ whose inner shells at principal quantum numbers $n_1, n_2, \ldots$ are fully occupied.  At the boundary of the $n_k$-th saturated torus, the Gauss-screened effective charges on either side are:
$$ 
\begin{aligned}
    Z_\text{in}  &= Z - N_\text{deeper}  & \text{(screened only by shells below $n_k$)} \\
    Z_\text{out} &= Z - N_\text{deeper} - N_k & \text{(screened by shell $n_k$ as well)}
\end{aligned}
 $$
where $N_\text{deeper}$ is the total electron count in all shells below $n_k$, and $N_k$ is the electron count in shell $n_k$.

### Op3 Reflection at the Boundary


The impedance mismatch at this discrete step produces a reflection coefficient (Op3, Axiom~2):
> **[Resultbox]** *Op3 Reflection at Saturated Torus*
>
> $$
>     \Gamma = \frac{Z_\text{out} - Z_\text{in}}{Z_\text{out} + Z_\text{in}}
>     
> $$
This is the same operator at every scale: antenna port reflection ($S_{11}$), seismic Moho discontinuity ($\Gamma \approx 0.17$), and particle Pauli exclusion ($\Gamma \to -1$).  The operator is implemented in `scale\_invariant.py:reflection\_coefficient()`.

**Dimensional check:** $[Z_\text{out}]$ = $[Z_\text{in}]$ = dimensionless charge numbers, so $\Gamma$ is dimensionless.~$\checkmark$

### Crossing Scattering at the Impedance Step


The power reflected at the boundary is $|\Gamma|^2$.  Not all of this reflected power is lost from the eigenvalue---only the fraction that scatters into non-resonant lattice modes at the topological crossing.  From Axiom~3, the crossing scattering fraction at a Hopf link intersection is:
$$
    \frac{P_C}{2} = 4\pi\alpha = 0.0917\ldots
    
$$
where $P_C = 8\pi\alpha$ is the packing fraction and the factor $1/2$ arises from the Hopf link crossing number $c = 2$.  This is the *same* $P_C/2$ that appears in the Hopf coupling coefficient $k_\text{pair} = (2/Z_\text{eff})(1 - P_C/2)$ and in the shell-penetration crossing energy $\delta E = E \times P_C/4$.

**Dimensional check:** $[P_C/2]$ = dimensionless (ratio).~$\checkmark$

### The SIR Energy Correction


Combining the Op3 reflection with the crossing scattering fraction, the energy removed from $E_\text{base}$ by the discrete impedance step is:
> **[Resultbox]** *SIR Boundary Correction (Correction~B)*
>
> $$
>     \boxed{E_\text{base, corrected} = E_\text{base} \times \left(1 - |\Gamma|^2 \times \frac{P_C}{2}\right)}
>     
> $$

**Physical interpretation:** The outer soliton's inner lobe penetrates through the saturated torus boundary.  The smooth CDF treats this as a gradual taper with no scattering.  In reality, the discrete step reflects a fraction $|\Gamma|^2$ of the lobe's energy, and crossing scattering removes $P_C/2$ of that reflected energy from the eigenvalue.

**Dimensional check:** $[|\Gamma|^2 \times P_C/2 \times E_\text{base}] = [1] \times [1] \times [\text{eV}] = [\text{eV}]$.~$\checkmark$

**Gate condition:**  This correction applies only when the adjacent inner shell has $p$-subshells ($n_\text{adjacent} \geq 2$), i.e., the inner torus is Pauli-saturated with $2n^2 > 2$ electrons.  When $n_\text{adjacent} = 1$ (pure $s$-shell), the inner torus is a simple K$_2$ pair and the hierarchical cascade correction (\Ssec:hierarchical_cascade_correction) applies instead.

**Worked example: Magnesium ($Z = 12$, $[\text{Ne**]\,3s^2$).}
$$ 
\begin{aligned}
    Z_\text{in}  &= 12 - 2 = 10      & \text{(1s$^2$ screened)} \\
    Z_\text{out} &= 12 - 2 - 8 = 2   & \text{(1s$^2$ + 2s$^2$2p$^6$ screened)} \\
    \Gamma &= \frac{2 - 10}{2 + 10} = -\frac{2}{3} \\
    |\Gamma|^2 &= \frac{4}{9} = 0.444 \\
    \Delta E &= -0.444 \times 0.0917 \times 17.671 = -0.720\;\text{eV}
\end{aligned}
 $$
After applying the Hopf mode splitting ($k_\text{pair} = 0.908$, with the standard formula for $N_s = 2$):
$$
    IE_\text{Mg} = (17.671 - 0.720) \times \left(\frac{2}{\sqrt{1 + 0.908}} - 1\right) = 7.59\;\text{eV}
$$
> **[Resultbox]** *Magnesium IE: SIR Correction*
>
> $$
>     IE_\text{Mg, AVE} = 7.59\;\text{eV} \quad (\text{exp: } 7.646\;\text{eV}, \quad \Delta = -0.7\%)
> $$
This resolves the Magnesium residual from $+3.5\%$ to $-0.7\%$ with zero free parameters.

% ===================================================================
% HIERARCHICAL CASCADE
% ===================================================================
