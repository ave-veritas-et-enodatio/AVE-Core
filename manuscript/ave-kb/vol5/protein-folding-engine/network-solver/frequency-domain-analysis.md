[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Frequency-Domain Analysis (Operator 7)

The SPICE transient integrator operates in the *time domain*. A complementary set of tools from digital signal processing (DSP) operates in the *frequency domain*, providing instant analytical results without time-stepping.

## Spatial FFT of Impedance Profile

The amino acid sequence defines a 1D impedance profile $Z(n) = |Z_\text{TOPO}[\text{aa}_n]|$ for $n = 1,\ldots,N$. The spatial discrete Fourier transform:

$$\hat{Z}(k) = \text{FFT}[Z(n)] = \sum_{n=0}^{N-1} Z(n)\, e^{-2\pi j k n / N}$$

decomposes the impedance landscape into resonant spatial modes. Peaks in the power spectrum $P(k) = |\hat{Z}(k)|^2$ directly predict secondary structure:

| **Spatial period** $N/k$ | **SS Element** | **Physical Origin** |
|---|---|---|
| $\approx 3.7$ residues | $\alpha$-helix | $Q/2$ standing wave (i$\to$i+4 H-bond) |
| $\approx 2.0$ residues | $\beta$-sheet | Alternating H-bond topology |
| $\approx 3{-}4$ residues | PPII helix | Polyproline pitch |

## Autocorrelation and Contact Order

The Wiener-Khinchin theorem gives the spatial autocorrelation:

$$R_Z(m) = \text{IFFT}\bigl[|\hat{Z}(k)|^2\bigr]$$

The first zero-crossing of $R_Z(m)$ is the impedance correlation length --- the average separation between impedance-matched residues. This is the purely analytical predictor of *contact order*.

**Implementation.** Function `universal_spectral_analysis()` in `universal_operators.py` (Operator 7). Returns the spectrum, PSD, autocorrelation, and the 5 dominant spatial periods in $O(N \log N)$ time.

## Spectral Analysis Results

FFT spectral analysis of protein impedance profiles. $P_\alpha/P_\beta$ is the power ratio at the helix vs. sheet spatial frequencies. CV is the coefficient of variation of $|Z_\text{topo}|$ along the sequence (impedance contrast).

| **Protein** | $N$ | **CV(%)** | **Dominant period** | $P_\alpha/P_\beta$ | **Prediction** |
|---|---|---|---|---|---|
| Chignolin | 10 | 23.3 | 3.3 res ($k\!=\!3$) | 36.0 | $\alpha$/PPII |
| Trp-cage | 20 | 27.3 | 4.0 res ($k\!=\!5$) | 247 | $\alpha$/PPII |
| Villin HP35 | 35 | 20.9 | 11.7 res ($k\!=\!3$) | 1.5 | Mixed |
| GB1 hairpin | 16 | 21.6 | 3.2 res ($k\!=\!5$) | 26.9 | $\alpha$/PPII |
| Poly-A | 10 | 0.0 | --- (flat) | 0.0 | No preference |
| Poly-G | 10 | 0.0 | --- (flat) | 0.0 | No preference |
| Alt. A-D | 10 | 25.5 | 2.0 res ($k\!=\!5$) | 0.0 | $\beta$-sheet |

Four observations emerge from the spectral decomposition:

1. **Alternating sequences** (A-D-A-D...) concentrate 100% of non-DC power at $k = N/2$ (period = 2 residues), exactly the $\beta$-sheet periodicity.
2. **Homopolymers** (poly-A, poly-G) have zero impedance contrast $\to$ flat spectrum $\to$ no preferential SS. SS is determined entirely by the EM driving force (H-bonds, solvent coupling), not by the impedance profile.
3. **Heteropolymers** (Chignolin, Trp-cage) show dominant peaks near 3.3--4.0 residue periods, matching known $\alpha$-helix ($Q/2 \approx 3.7$) and PPII ($3.0$) periodicities.
4. **The impedance CV** ($\sigma/\bar{Z}$) measures the total spectral energy available for SS selection. CV $>$ 20% provides sufficient driving contrast; CV $=$ 0% leaves SS entirely to kinetic (SPICE) physics.

## FFT-Guided Basin Initialisation

The spectral power distribution directly informs the initial $(\varphi, \psi)$ basin selection. For each residue $i$, a sliding window of width $Q$ ($\approx 7$ residues) is centred on position $i$, and the local power at the helix frequency ($k_\alpha = \lfloor W/3.7 \rceil$) and sheet frequency ($k_\beta = \lfloor W/2.0 \rceil$) is computed. The per-residue basin probability is:

$$p_\alpha^{(i)} \propto \frac{P(k_\alpha)}{P(k_\alpha) + P(k_\beta)} + (1 - |Z_i|), \qquad p_\beta^{(i)} \propto \frac{P(k_\beta)}{P(k_\alpha) + P(k_\beta)} + |Z_i|$$

where the impedance magnitude bias ($|Z_i|$) encodes Axiom 1: low-impedance sidechains (Ala, Gly, Leu) fit tight helix turns; high-impedance sidechains (Asp, Trp, Glu) prefer extended $\beta$ conformations.

## FFT-Guided Initialisation Benchmark

"Random" uses uniform basin selection; "Spectral" uses the FFT-guided formula.

| **Protein** | Random $f(\theta)$ | Random $R_g$ (Å) | Spectral $f(\theta)$ | Spectral $R_g$ (Å) |
|---|---|---|---|---|
| Chignolin ($N\!=\!10$) | 0.0448 | 6.9 | **0.0361** | **5.5** |
| Trp-cage ($N\!=\!20$) | 0.0636 | 12.1 | **0.0527** | **6.1** |

The spectral initialisation improves both the eigenvalue target ($f(\theta)$) and the radius of gyration for both test proteins. Trp-cage $R_g$ drops from 12.1 Å to 6.1 Å (experimental: 7.3 Å), a 50% improvement from a single $O(N \log N)$ pre-analysis step.

---
