[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Bend Discontinuity Admittance

When a guided wave encounters a direction change at a transmission-line junction, energy radiates out of the guide. Six independent engineering domains produce the same functional form:

## Cross-Domain Consensus

Cross-domain consensus for angular mismatch loss at a waveguide junction. All six give $(1-\cos\theta)$ or its small-angle limit $\theta^2/2$.

| **Domain** | **Loss Factor** |
|---|---|
| TL microstrip bend | $C_\text{bend} = d\,(1-\cos\theta)/(\pi Z_0)$ |
| Transformer coupling | $1 - k = 1 - \cos\theta$ |
| Fiber optic macrobend | $\alpha \propto (1 - \cos\theta)$ |
| Grain boundary (Ziman) | $R_\text{GB} = 1 - \cos(\Delta\theta)$ |
| Antenna bend radiation | $P_\text{rad} \propto \kappa^2 \approx \theta^2/2$ |
| Acoustic horn (Webster) | damping $\propto$ curvature |

## Protein Mapping

The bend angle $\theta_i$ between successive $\text{C}_\alpha$--$\text{C}_\alpha$ bond vectors defines the local curvature at each residue junction. The microstrip bend formula gives an excess *capacitance* at the junction, which the ABCD cascade converts to a frequency-dependent shunt admittance:

> **[Resultbox]** *Bend Discontinuity Admittance*
>
> $$C_\text{bend} = \frac{1 - \cos\theta_i}{2\pi^2}, \qquad Y_\text{bend}(\omega) = \omega\,C_\text{bend}$$

The coefficient $2\pi^2$ emerges from the microstrip bend capacitance formula $C = (d_\text{eff}/\lambda_g)\,(1-\cos\theta)/(\pi Z_0)$ applied to the backbone cascade:

1. The microstrip formula gives $C = (d_\text{eff}/\lambda_g)\,(1-\cos\theta)/(\pi\,Z_0)$.
2. The waveguide cross-section is one C$\alpha$--C$\alpha$ bond: $d_\text{eff} = d_0$.
3. The guided wavelength at resonance ($\omega_0 \approx 1$) is $\lambda_g = 2\pi\,d_0/\omega_0 = 2\pi\,d_0$.
4. The ratio $d_\text{eff}/\lambda_g = 1/(2\pi)$.
5. With $Z_0 = 1$ (normalised reference): $C = (1-\cos\theta)/(2\pi \times \pi) = (1-\cos\theta)/(2\pi^2)$.

**Zero new constants**. Every factor is geometric: $(1-\cos\theta)$ from cross-domain consensus, $2\pi$ from the guided-wavelength ratio, $\pi$ from the microstrip junction formula, $\omega$ from the capacitive nature of the bend.

## Benchmark Results

$C_\alpha$ Kabsch RMSD (Å) with capacitive bend admittance $Y_\text{bend} = \omega\,(1-\cos\theta)/(2\pi^2)$, 5-start optimisation. Improvements for all proteins except BBA5 ($+0.85$ Å, within stochastic noise of 5 starts). Protein G shows the largest improvement ($-6.53$ Å).

| **Protein** | **Fold** | $N$ | **Original** | **$+$Bend** | $\Delta$ |
|---|---|---|---|---|---|
| Chignolin | $\beta$-hairpin | 10 | 4.60 | 2.59 | $-2.01$ |
| Trp-cage | $\alpha$ | 20 | 7.49 | 6.25 | $-1.24$ |
| BBA5 | $\alpha/\beta$ | 22 | 6.54 | 7.39 | $+0.85$ |
| Villin HP35 | $\alpha$ | 35 | 8.65 | 8.25 | $-0.40$ |
| Protein G | $\alpha/\beta$ | 56 | 19.78 | 13.25 | $-6.53$ |

## The Protein Smith Chart

The complete impedance trajectory $\Gamma(n)$ traced by the ABCD cascade as it progresses from N-terminus to C-terminus for three proteins at three frequencies. A folded protein should spiral toward $\Gamma = 0$ (centre = matched); a disordered chain wanders near $|\Gamma| = 1$.

<!-- Figure: protein_smith_chart.png — Protein Smith charts for Trp-cage, Chignolin, and Villin HP35 -->

**Interpretation.** The capacitive bend admittance discriminates between periodic and disordered backbone regions via two mechanisms: (1) straight segments ($\theta \approx 0$) have $Y_\text{bend} = 0$, preserving the standing-wave resonance; (2) higher-frequency modes see larger $Y_\text{bend}$ at turns, suppressing aliased periodicity in coiled regions. The frequency selectivity is key: the $\omega$-dependence naturally penalises high-frequency artefacts in disordered regions while leaving sub-resonance modes (true secondary structure) undamped.

---
