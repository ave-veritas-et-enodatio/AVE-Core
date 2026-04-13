[↑ Up](../index.md)
<!-- leaf: verbatim -->

## Ionization Energy: SIR Boundary Correction


Magnesium ($Z = 12$, $[\text{Ne}]\,3s^2$) is the first $s$-block atom in period~3.  Its ionization energy requires the SIR boundary correction because the nearest inner shell ($n = 2$, containing $2s^2 2p^6 = 8$ electrons) is Pauli-saturated with $p$-subshells.

**The equivalent circuit.**
The Mg atom, viewed as a radial transmission line, has a discrete impedance step at the $n = 2$ torus boundary:
\begin{center}
\small
\begin{tabular}{lccc}
\toprule
**Section** & **$Z_\text{net**$} & **Electron content** & **Boundary type** \\
\midrule
Inner ($r < r_2$) & $12 - 2 = 10$ & $1s^2$ & Smooth CDF \\
Boundary ($r = r_2$) & step: $10 \to 2$ & $2s^2 2p^6$ saturated torus & **Discrete step (SIR)** \\
Outer ($r > r_2$) & $12 - 10 = 2$ & $3s^2$ valence pair & ODE cavity \\
\bottomrule
\end{tabular}
\end{center}

**Op3 reflection.**
The impedance contrast at the saturated $n = 2$ boundary:
$$ 
\begin{aligned}
    \Gamma &= \frac{Z_\text{out} - Z_\text{in}}{Z_\text{out} + Z_\text{in}} = \frac{2 - 10}{2 + 10} = -\frac{2}{3}  \\
    |\Gamma|^2 &= \frac{4}{9} = 0.444
\end{aligned}
 $$
The crossing scattering at this step removes $|\Gamma|^2 \times P_C/2 = 0.444 \times 0.0917 = 0.0407$ of $E_\text{base}$:
$$
    E_\text{base, corrected} = 17.671 \times (1 - 0.0407) = 16.951\;\text{eV}
$$
After Hopf mode splitting ($k_\text{pair} = 0.908$, $N_s = 2$):
$$
    IE_\text{Mg} = 16.951 \times \left(\frac{2}{\sqrt{1 + 0.908}} - 1\right) = 7.59\;\text{eV}
$$

> **[Resultbox]** *Magnesium First Ionization Energy*
>
> $$
>     IE_\text{Mg, AVE} = 7.59\;\text{eV} \quad (\text{exp: } 7.646\;\text{eV}, \quad \Delta = -0.7\%)
> $$
 This resolves the prior $+3.5\%$ residual with zero free parameters.  The correction is gated to $n_\text{adjacent} \geq 2$ (inner shell has $p$-subshells), ensuring mutual exclusivity with the Be-type hierarchical cascade.  See Vol.~II, \Ssec:sir_atom for the full derivation.

\begin{summarybox}
\begin{itemize}
    \item Magnesium-24 closes the $6\alpha$ octahedral shell, demonstrating the systematic escalation of $V_R/V_{BR}$ from Carbon-12 ($0.019$) through Oxygen ($0.030$), Neon ($0.032$), to $0.040$.
    \item The progression toward the avalanche threshold foreshadows the Large Signal transition at Sulfur-32 ($8\alpha$, $V_R/V_{BR} = 0.994$).
    \item The first ionization energy ($7.59$~eV, $-0.7\%$) is resolved by the SIR boundary correction: the Pauli-saturated $n = 2$ torus creates a discrete impedance step ($|\Gamma|^2 = 4/9$) whose crossing scattering reduces $E_\text{base}$.
\end{itemize}
\end{summarybox}

\begin{exercisebox}
\begin{enumerate}
    \item Plot the $V_R/V_{BR}$ progression from Carbon-12 to Magnesium-24 and extrapolate to predict the element at which the Small Signal regime breaks down.
    \item Explain why the $6\alpha$ octahedral geometry of Magnesium-24 has 15 inter-alpha coupling pairs and compute the total mutual impedance contribution.
\end{enumerate}
\end{exercisebox}
