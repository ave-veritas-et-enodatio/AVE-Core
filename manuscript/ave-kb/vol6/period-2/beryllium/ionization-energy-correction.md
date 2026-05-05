[↑ Up](../index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: 7tk051 -->

## Ionization Energy: Hierarchical Cascade Correction


Beryllium ($Z = 4$, $1s^2\,2s^2$) presents a unique challenge for the ionization energy solver.  The nearest inner shell ($n = 1$) is a pure $s$-shell containing only a K$_2$ Hopf pair.  Unlike period~3 atoms where the inner torus is Pauli-saturated with $p$-states and reflects via the SIR boundary correction, the inner $1s^2$ pair's bonding mode **absorbs** a portion of the outer pair's mutual Hopf coupling.

**Physical mechanism.**
The inner K$_2$ pair has its own Hopf coupling $k_\text{inner} = (2/Z_\text{eff,in})(1 - P_C/2) = 0.454$.  This bonding mode shifts the base frequency of the nuclear impedance well, effectively reducing the coupling available to the outer $2s^2$ pair.  The correction follows the K$_2$ eigenvalue-to-coupling mapping ($\omega \propto Z^2$, $k \propto 1/Z$), yielding:
$$
    k_\text{eff} = \frac{k_\text{pair}}{(1 + k_\text{inner})^{1/4}} = \frac{0.754}{(1.454)^{0.25}} = 0.687
$$
This is the scale-invariant analog of `hierarchical\_binding()` in the nuclear coupled resonator---the same operator at both scales.

**Result.**
> **[Resultbox]** *Beryllium First Ionization Energy*
>
> $$
>     IE_\text{Be} = 9.28\;\text{eV} \quad (\text{exp: } 9.322\;\text{eV}, \quad \Delta = -0.45\%)
> $$
 This resolves the prior $-7.1\%$ residual with zero free parameters.  The correction is gated to $n_\text{adjacent} = 1$ (pure $s$-shell inner core), ensuring it does not fire for period~3 atoms where the SIR boundary model applies (see Vol. 2).

\begin{summarybox}
\begin{itemize}
    \item Beryllium-9 is the degenerate dual-core limiting case: two Alpha particles bridged by a single neutron, with one coupling pair and zero structural margin.
    \item The notoriously narrow stability of $^9$Be (removal of the neutron causes instant fission into $2\alpha$ in $\sim 10^{-16}$~s) is a direct mechanical consequence of its single-junction, zero-margin topology.
    \item The first ionization energy ($9.28$~eV, $-0.45\%$) is resolved by the hierarchical cascade correction: the inner $1s^2$ bonding mode absorbs outer Hopf coupling via $k_\text{eff} = k_\text{pair}/(1+k_\text{inner})^{1/4}$.
\end{itemize}
\end{summarybox}

\begin{exercisebox}
\begin{enumerate}
    \item Explain why removing one neutron from $^9$Be causes immediate fission into two Alpha particles, using the concept of structural margin from the semiconductor binding model.
    \item Compute the $V_R/V_{BR}$ ratio for the $2\alpha$ pair in Beryllium-9 and confirm it lies deep in the Small Signal regime.
\end{enumerate}
\end{exercisebox}
