[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [oltvwy]
-->

## Ionization Energy Validation: $Z = 1$ to $14$


The complete first-ionization-energy sweep demonstrates the accuracy of the three-phase pipeline (Phase~A cavity eigenvalue, Phase~B Hopf mode splitting with corrections A/B/C, Phase~C crossing scattering).  All values are computed using the engine solver `ionization\_energy\_e2k(Z)` with zero free parameters.

\begin{center}
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{clrrcl}
\toprule
**$Z$** & **Element** & **AVE [eV]** & **Exp [eV]** & **$\Delta$** & **Correction** \\
\midrule
1  & H  & 13.606 & 13.598 & $+0.06\%$ & --- \\
2  & He & 24.370 & 24.587 & $-0.88\%$ & --- \\
3  & Li &  5.525 &  5.392 & $+2.46\%$ & --- \\
4  & Be &  9.280 &  9.322 & $-0.45\%$ & A (cascade) \\
5  & B  &  8.065 &  8.298 & $-2.80\%$ & --- \\
6  & C  & 11.406 & 11.260 & $+1.30\%$ & --- \\
7  & N  & 14.465 & 14.534 & $-0.48\%$ & --- \\
8  & O  & 13.618 & 13.618 & $-0.00\%$ & --- \\
9  & F  & 17.194 & 17.423 & $-1.31\%$ & --- \\
10 & Ne & 21.789 & 21.565 & $+1.04\%$ & --- \\
11 & Na &  5.071 &  5.139 & $-1.33\%$ & --- \\
12 & Mg &  7.591 &  7.646 & $-0.73\%$ & B (SIR) \\
13 & Al &  5.937 &  5.986 & $-0.82\%$ & C (Op10) \\
14 & Si &  8.147 &  8.152 & $-0.06\%$ & C (Op10) \\
\bottomrule
\end{tabular}
\end{center}

**Discussion.**
For $Z = 1$ through $14$ (Hydrogen to Silicon), the solver achieves $\pm 2.8\%$ maximum error with zero adjustable parameters.  Four distinct regimes of accuracy emerge:
\begin{itemize}
    \item **Hydrogen ($Z = 1$):** Exact to $0.06\%$---single-electron eigenvalue, no corrections needed.
    \item **Period 2 ($Z = 2$--$10$):** Within $\pm2.8\%$---the Hopf mode splitting and MCL loading produce accurate predictions across the $s$- and $p$-blocks.
    \item **Period 3 $s$-block ($Z = 11$--$12$):** Within $\pm1.3\%$---the SIR boundary correction (Mg) resolves the impedance step at the saturated $n = 2$ torus.
    \item **Period 3 $p$-block ($Z = 13$--$14$):** Within $\pm0.8\%$---Op10 junction projection at the co-resonant $n = 2$ shell boundary resolves the impedance step overshoot.
\end{itemize}

**Resolved: Aluminum and Silicon (Correction~C).**
The $3p$ soliton crosses the Pauli-saturated $n = 2$ torus boundary twice per radial oscillation ($c = 2$).  The SIR nesting gate rejects ($n_\text{out}^2/n_\text{inner}^2 = 9/4 = 2.25 < 4$), because the $n = 2$ shell is co-resonant, not deeply nested.  Op10 junction projection provides the lighter correction: $|\Gamma|^2$ from Op3 maps to a crossing angle $\theta$ via Malus's law ($\cos\theta = 1 - 2|\Gamma|^2$), giving $Y = c(1-\cos\theta)/(2\pi^2)$ and $E_\text{eff} = E_\text{base} \times (1-Y)^2$ (quadratic dispersion).  Full derivation and worked examples for Al ($-0.82\%$) and Si ($-0.06\%$) are in Vol.~VI, Chapters~15--16.
