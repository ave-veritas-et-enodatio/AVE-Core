[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Broader Biological Research Avenues

The transmission line framework developed for protein folding is not specific to proteins. Every biological system that propagates signals through structured media --- axons, ion channels, DNA, developing tissue --- is a candidate for the same impedance/saturation/reflection operator chain.

## Research Avenues Table

Biological phenomena amenable to AVE transmission-line analysis. Each row identifies the primary AVE operator, the biological system, and a parameter-free testable prediction.

| **Operator** | **System** | **Observable** | **Prediction** |
|---|---|---|---|
| Op 1 (Z) | Myelinated axon | Conduction velocity | $v = 1/\sqrt{LC}$ from membrane $R_m, C_m$, axon radius |
| Op 2 (S) | Ion channel gating | Conductance vs. voltage | $G(V) = G_0 \sqrt{1 - (V/V_\text{gate})^2}$; sigmoid gating emerges from saturation |
| Op 3 ($\Gamma$) | Drug--receptor binding | Binding affinity | $K_d \propto |\Gamma|^2$ where $\Gamma = (Z_\text{drug} - Z_\text{site})/(Z_\text{drug} + Z_\text{site})$ |
| Op 4 (U) | Enzyme catalysis | Activation energy | Transition state is the impedance peak of the substrate--enzyme TL junction |
| Op 5 (Y$\to$S) | Neural network | Memory capacity | $N_\text{modes} = \text{rank}(S^\dagger S)$ of the cortical Y-matrix |
| Op 6 ($\lambda_\text{min}$) | Morphogenesis | Pattern wavelength | Tissue standing waves: $\lambda = 2L/n$ where $L$ is the diffusion cavity length |
| Op 7 (FFT) | EEG spectral analysis | Cognitive state | Band power ratios from cortical cavity mode spectrum |

## DNA as a Digital Transmission Line

The double helix is a twisted-pair transmission line where each base pair is a lumped impedance element. The four bases (A, T, G, C) map to four impedance values via $Z_\text{base} = \sqrt{m_\text{base}/n_e}$ (identical to the protein bond solver). Codon recognition becomes impedance matching between the mRNA "source" and the tRNA "load" --- mismatches produce reflections that destabilise the ribosomal complex.

## Morphogenesis as Standing Wave Patterning

Turing patterns (stripes, spots, spirals) in developing tissue may arise from standing waves in a 2D impedance network. The pattern wavelength is set by the cavity dimensions and the tissue impedance: $\lambda = v/f_0$ where $v$ is the signal propagation velocity through gap junctions and $f_0$ is the resonant frequency of the local LC network (cell membrane $C$ and cytoplasmic $L$).

## Enzyme Catalysis as Impedance-Matched Energy Transfer

An enzyme active site can be modelled as a stub-tuned impedance matching network. The substrate approaches along a transmission line (the binding channel); the active site geometry creates an impedance taper that minimises $|S_{11}|^2$ at the transition state. Catalytic efficiency ($k_\text{cat}/K_M$) should correlate with the minimum $|S_{11}|^2$ achievable at the substrate--enzyme junction --- computable from $Z_\text{topo}$ values already in the engine.

---
