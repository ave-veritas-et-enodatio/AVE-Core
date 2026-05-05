[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: w6kk5y -->

## Hierarchical Cascade Correction


When the adjacent inner shell is a pure $s$-shell ($n_\text{adjacent} = 1$), it contains a single K$_2$ Hopf pair with its own bonding mode.  The SIR boundary model (\Ssec:sir_atom) does not apply because the inner torus is not Pauli-saturated with $p$-states---it has only two electrons.  Instead, the inner pair's bonding mode *absorbs* a portion of the outer pair's mutual Hopf coupling.

### Nuclear Precedent: Hierarchical Binding

In the nuclear domain, the function `hierarchical\_binding()` in `coupled\_resonator.py` models a multi-level cascade of alpha clusters.  The inner cluster's bonding mode frequency shifts the base frequency for the outer cluster's coupling.  The atomic correction is the exact scale-invariant analog.

### Derivation

For two nested $s$-shells, the inner pair at $(n_\text{in}, N_\text{in} = 2)$ has coupling:
$$
    k_\text{inner} = \frac{2}{Z_\text{eff, in}}\left(1 - \frac{P_C}{2}\right)
    
$$
where $Z_\text{eff, in}$ is the screened charge seen by the inner pair.  The bonding mode eigenfrequency of this inner pair is $\omega_\text{bond} = \omega_0 / \sqrt{1 + k_\text{inner}}$.

The outer pair's coupling $k_\text{pair}$ is modified because the inner pair's bonding mode has already ``used'' part of the mutual inductance budget.  The K$_2$ eigenvalue-to-coupling mapping ($\omega \propto Z^2$, $k \propto 1/Z$) gives a $1/4$ power law for the coupling absorption:
> **[Resultbox]** *Hierarchical Cascade (Correction~A)*
>
> $$
>     \boxed{k_\text{eff} = \frac{k_\text{pair}}{(1 + k_\text{inner})^{1/4}}}
>     
> $$

**Derivation of the $1/4$ power:**
For the Rydberg eigenvalue $E_0 \propto Z_\text{eff}^2$, the Hopf coupling $k \propto 2/Z_\text{eff}$ scales as the inverse of the effective charge.  When the inner pair reduces the nuclear attraction through bonding mode absorption, the eigenvalue contribution scales as $(1 + k_\text{inner})^{1/2}$ (normal mode splitting).  The coupling correction enters as the square root of the eigenvalue correction: $(1 + k_\text{inner})^{1/4}$.

**Gate condition:**  $n_\text{adjacent} = 1$ (the nearest inner shell is a pure $s$-shell at $n = 1$).  This correction is mutually exclusive with the SIR boundary correction (\Ssec:sir_correction).

**Worked example: Beryllium ($Z = 4$, $1s^2\,2s^2$).**
$$ 
\begin{aligned}
    Z_\text{eff, in} &= 4 - 0 = 4   & \text{(inner 1s$^2$: no deeper shells)} \\
    k_\text{inner} &= \frac{2}{4}\left(1 - 0.0917\right) = 0.454 \\
    k_\text{pair} &= \frac{2}{2.408}\left(1 - 0.0917\right) = 0.754   & \text{($Z_\text{eff,out} = 4 - 2 \times J_{1s} = 2.408$)} \\
    k_\text{eff} &= \frac{0.754}{(1 + 0.454)^{0.25}} = \frac{0.754}{1.098} = 0.687
\end{aligned}
 $$
$$
    IE_\text{Be} = E_\text{base} \times \left(\frac{2}{\sqrt{1 + k_\text{eff}}} - 1\right) = 9.28\;\text{eV}
$$
> **[Resultbox]** *Beryllium IE: Hierarchical Cascade*
>
> $$
>     IE_\text{Be, AVE} = 9.28\;\text{eV} \quad (\text{exp: } 9.322\;\text{eV}, \quad \Delta = -0.45\%)
> $$
This resolves the Beryllium residual from $-7.1\%$ to $-0.45\%$ with zero free parameters.

% ===================================================================
% UPDATED IE VALIDATION TABLE
% ===================================================================
