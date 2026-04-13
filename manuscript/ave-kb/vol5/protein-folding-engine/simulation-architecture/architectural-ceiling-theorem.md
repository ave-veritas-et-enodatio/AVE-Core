[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Architectural Ceiling Theorem

## Theorem: 1D Cascade SS Ceiling

In a 1D ABCD cascade with shunt admittances at junctions, secondary structure (standing-wave resonance) can emerge only from adjacent-junction coupling. Non-local contacts, modelled as $Y_\text{shunt}$ at backbone nodes, provide damping but not resonance.

**Proof (by construction).** Consider a shunt admittance $Y$ at junction $i$. The ABCD matrix is:

$$M_Y = \begin{bmatrix} 1 & 0 \\ Y & 1 \end{bmatrix}$$

This matrix has $|A| = |D| = 1$, $B = 0$: it adds no phase delay, only resistive damping ($C = Y$). A standing wave requires a reflected wave with specific phase---but $Y_\text{shunt}$ provides only amplitude modulation, never phase-coherent reflection.

In contrast, a transmission line stub of length $\ell$ and impedance $Z_s$ contributes:

$$Y_\text{stub}(\omega) = \frac{\tanh(\gamma\ell)}{Z_s}$$

which is frequency-dependent and creates phase-coherent constructive/destructive interference---the mechanism for standing waves.

Therefore: $Y_\text{shunt}$ (scalar admittance) $\Rightarrow$ damping only; TL stub $\Rightarrow$ resonance possible. $\square$

## Ceiling Evidence

Approaches tested within the 1D cascade. All non-local modifications fail because $Y_\text{shunt}$ cannot create resonance.

| **Approach** | **SS** | **$R_g$ err** | **Outcome** |
|---|---|---|---|
| Baseline (global $S(\eta)$) | 7.5% | 1.6% | No Q-decay $\Rightarrow$ N$^2$ overwhelms |
| Q-decay on hydrophobic | **22.8%** | 6.0% | **Best result: reinstates Q balance** |
| Q-decay + tertiary | 17/30% | 4.8/3.3% | Mixed: helps $N>35$, hurts $N<20$ |
| Flat $\nu_\text{vac} = 2/7$ | 9% | 8.7% | Over-attenuates ALL coupling |
| Per-residue $S(\eta_i)$ | 8.5% | 9.3% | Helix contacts $\Rightarrow$ helix suppressed |
| Unified $\sqrt{x(2-x)}$ profile | 0% | 18% | Too weak without Lorentz boost |

The Q-decay result (SS$=$22.8%) represents the *architectural ceiling* of the 1D cascade: it is the maximum SS achievable within axiom compliance using only $Y_\text{shunt}$ couplings. The local peptide-plane coupling (adjacent-junction, not $Y_\text{shunt}$) is the sole SS driver, and Q-decay prevents the N$^2$-scaling hydrophobic damping from overwhelming it.

The path to higher SS is the 1.5D stub architecture (Chapter 4): H-bonds modeled as transmission line stubs with their own $Z_\text{HB}$, $\gamma_\text{HB}$, and propagation delay, enabling frequency-selective resonance between non-adjacent backbone positions.

---
