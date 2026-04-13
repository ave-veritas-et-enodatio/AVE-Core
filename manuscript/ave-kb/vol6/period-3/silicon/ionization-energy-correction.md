[↑ Up](../index.md)
<!-- leaf: verbatim -->

## Ionization Energy: Op10 Junction Projection (Correction~C)


Silicon ($Z = 14$, $[\text{Ne}]\,3s^2\,3p^2$) shares the same co-resonant $n = 2$ shell boundary as Aluminum.  The same Correction~C (Op10 junction projection) applies:

**Equivalent circuit.**
\begin{center}
\small
\begin{tabular}{lccc}
\toprule
**Section** & **$Z_\text{net**$} & **Content** & **Solver path** \\
\midrule
Inner ($r < r_2$) & $14 - 2 = 12$ & $1s^2$ & Smooth CDF \\
Boundary ($r = r_2$) & step: $12 \to 4$ & $2s^2 2p^6$ saturated & **Impedance step** \\
Outer ($r > r_2$) & $14 - 10 = 4$ & $3s^2\,3p^2$ & MCL loading \\
\bottomrule
\end{tabular}
\end{center}

**Correction~C derivation.**
\begin{enumerate}
    \item **Axiom~2 (Gauss screening):**  $Z_\text{in} = 12$, $Z_\text{out} = 4$ at the $n = 2$ boundary.
    \item **Op3 (Reflection):**  $|\Gamma|^2 = (4-12)^2/(4+12)^2 = 64/256 = 0.250$ (25.0\% power reflection).
    \item **Op3 $\to$ Op10 bridge:**  $\cos\theta = 1 - 2 \times 0.250 = 0.500$, giving $\theta = 60.0^\circ$.
    \item **Op10 (Junction projection):**  $Y = 2 \times (1 - 0.500)/(2\pi^2) = 0.0507$.
    \item **Axiom~1 (Quadratic dispersion):**  $E_\text{eff} = 43.22 \times (1 - 0.0507)^2 = 43.22 \times 0.901 = 38.95$~eV.
\end{enumerate}

The MCL loading then gives:
\[
    IE = 38.95 \times 0.2092 = 8.147~\text{eV}
\]
against $8.152$~eV experimental: $\boxed{-0.06\%}$ error.

**Pattern confirmation.**
The $-0.06\%$ result for Silicon confirms the systematic pattern identified from Aluminum: both period-3 $p$-block residuals arise from the uncompensated impedance step at the co-resonant $n = 2$ boundary, and both are resolved by the same Op10 junction projection correction (Correction~C).  The smaller $|\Gamma|^2$ for Silicon (0.250 vs 0.327 for Al) correctly produces a smaller correction, consistent with the lower initial residual ($+10.9\%$ vs $+13.7\%$).

\begin{summarybox}
\begin{itemize}
    \item Silicon-28 closes the $7\alpha$ pentagonal bipyramid shell, representing the last stable Small Signal element before the onset of avalanche multiplication.
    \item The semiconductor boundary at Silicon quantitatively explains why Silicon is the foundational material of the electronics industry: it is the heaviest symmetric alpha-cluster element that operates in the fully linear regime.
    \item **Resolved:** The first ionization energy ($8.147$~eV vs $8.152$~eV, $-0.06\%$) is reproduced by Op10 junction projection at the co-resonant $n = 2$ shell boundary (Correction~C), confirming the systematic pattern from Aluminum.
\end{itemize}
\end{summarybox}

\begin{exercisebox}
\begin{enumerate}
    \item Explain the physical significance of Silicon-28 sitting at the semiconductor boundary ($V_R/V_{BR}$ approaching the avalanche threshold) and relate this to its industrial importance.
    \item Compare the $7\alpha$ bipyramid geometry of Silicon-28 with the $5\alpha$ bipyramid of Neon-20 and discuss the structural homology.
    \item Verify that Silicon's Op10 crossing angle ($\theta = 60^\circ$) produces a smaller correction than Aluminum's ($\theta = 69.7^\circ$), and explain why $|\Gamma|^2 = 0.250 < 0.327$ gives $\theta_\text{Si} < \theta_\text{Al}$.
\end{enumerate}
\end{exercisebox}
