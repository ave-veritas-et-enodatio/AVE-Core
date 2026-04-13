[↑ Up](../index.md)
<!-- leaf: verbatim -->

## Ionization Energy: Op10 Junction Projection (Correction~C)


Aluminum ($Z = 13$, $[\text{Ne}]\,3s^2\,3p^1$) is the first $p$-block element in period~3.  The radial transmission line has a large impedance step at the $n = 2$ boundary:

**Equivalent circuit.**
\begin{center}
\small
\begin{tabular}{lccc}
\toprule
**Section** & **$Z_\text{net**$} & **Content** & **Solver path** \\
\midrule
Inner ($r < r_2$) & $13 - 2 = 11$ & $1s^2$ & Smooth CDF \\
Boundary ($r = r_2$) & step: $11 \to 3$ & $2s^2 2p^6$ saturated & **Impedance step** \\
Outer ($r > r_2$) & $13 - 10 = 3$ & $3s^2\,3p^1$ & MCL loading \\
\bottomrule
\end{tabular}
\end{center}

**Why the SIR nesting gate rejects.**
The SIR mode-weighting applies when the inner shell is deeply nested: $n_\text{out}^2/n_\text{inner}^2 \geq 4$.  For Al: $9/4 = 2.25 < 4$---the $n = 2$ shell is co-resonant with the $n = 3$ valence, not enclosed by it.  Full SIR mode-weighting overcorrects by $\sim 40\%$ because it strips all core phase from $E_\text{base}$.

**Correction~C: Op10 junction projection.**
The $3p$ soliton crosses the saturated $n = 2$ torus boundary *twice* per radial oscillation (inward and outward passages).  Each crossing is a junction in the Op10 sense.  The correction chain uses five operators with zero free parameters:

\begin{enumerate}
    \item **Axiom~2 (Gauss screening):**  $Z_\text{in} = 11$, $Z_\text{out} = 3$ at the $n = 2$ boundary.
    \item **Op3 (Reflection):**  $|\Gamma|^2 = (3-11)^2/(3+11)^2 = 64/196 = 0.327$ (32.7\% power reflection).
    \item **Op3 $\to$ Op10 bridge (Malus's law):**  The reflected power fraction maps to a complementary projection angle: $\cos\theta = 1 - 2|\Gamma|^2 = 0.347$, giving $\theta = 69.7^\circ$.
    \item **Op10 (Junction projection):**  $Y = c(1 - \cos\theta)/(2\pi^2)$ with $c = 2$ crossings: $Y = 2 \times 0.653 / 19.74 = 0.0662$.
    \item **Axiom~1 (Quadratic dispersion):**  $E_\text{eff} = E_\text{base} \times (1 - Y)^2 = 25.88 \times 0.872 = 22.57$~eV.
\end{enumerate}

The MCL loading then gives:
\[
    IE = E_\text{eff} \times [N_\text{eff}\,T^2(N_\text{eff}) - N_{\text{eff}-1}\,T^2(N_{\text{eff}-1})] = 22.57 \times 0.263 = 5.937~\text{eV}
\]
against $5.986$~eV experimental: $\boxed{-0.82\%}$ error.

**Scale-invariant precedent.**
The same Op10 formula $(1-\cos\theta)/(2\pi^2)$ appears at three other scales in the AVE framework: protein backbone bends ($\theta = 109.47^\circ$, $c = 1$), Borromean baryon crossings ($\theta = 90^\circ$, $c = 6$), and nuclear hierarchical binding (where the Level-1 bonding mode becomes the Level-2 base frequency, exact analog of the co-resonant shell modifying $E_\text{base}$).

**Period-2 regression check.**
For period-2 $p$-block atoms (B--Ne), the inner shell is $1s^2$ with $|\Gamma|^2 < 0.063$.  The Op10 correction is $<1.3\%$---well within existing error bars.  The SIR nesting gate passes for these shells ($n_\text{out}^2/n_\text{inner}^2 = 4 \geq 4$), so the Op10 path is never entered.  Zero regression.

\begin{summarybox}
\begin{itemize}
    \item Aluminum-27 is the $6\alpha + 1$ halo analogue to Fluorine-19's $4\alpha + 1$ structure, with $R_{\text{halo}} = 53d$ demonstrating the geometric plateau of post-transition metals.
    \item The Sodium-to-Aluminum halo shift of only $2.4d$ proves that the $5\alpha \to 6\alpha$ core expansion has negligible effect on halo proximity---the octahedral core saturates core--halo attraction.
    \item **Resolved:** The first ionization energy ($5.937$~eV vs $5.986$~eV, $-0.82\%$) is reproduced by Op10 junction projection at the co-resonant $n = 2$ shell boundary (Correction~C), using the same operator that governs protein backbone bend loss.
\end{itemize}
\end{summarybox}

\begin{exercisebox}
\begin{enumerate}
    \item Explain why the halo distance stabilises near $50$--$53d$ for Sodium and Aluminum despite a $5\alpha \to 6\alpha$ core expansion.
    \item Use the $R_{\text{halo}}$ plateau to predict why post-transition metals (Al, Ga, In) share moderate, similar electronegativities.
    \item Derive the Op10 crossing angle $\theta = 69.7^\circ$ for Aluminum from $|\Gamma|^2 = 0.327$ and verify that the resulting IE matches the NIST value.
\end{enumerate}
\end{exercisebox}
