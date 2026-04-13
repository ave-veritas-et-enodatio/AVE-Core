[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Tier 3: Physics Layers (Layers 5--8)

## Layer 5: Multi-Frequency Integration

The $S_{11}$ is averaged over five frequencies spanning the backbone resonance $\pm$ harmonics:

$$\overline{|S_{11}|^2} = \frac{1}{5} \sum_{k=1}^{5} |S_{11}(\omega_k)|^2, \qquad \omega_k / \omega_0 \in \{0.5,\; 0.8,\; 1.0,\; 1.3,\; 2.0\}$$

This prevents the optimizer from "gaming" a single frequency and ensures broadband impedance matching---the physical requirement for a structure bathed in broadband thermal noise.

## Layer 6: Non-Reciprocal Chirality Phase

The AVE vacuum lattice (SRS/K4 net) is intrinsically chiral. This enters the ABCD cascade as a non-reciprocal phase correction:

$$\delta_\chi^{(i)} = \frac{0.35}{Q} \cdot w_\text{helix}^{(i)} \cdot \tanh\!\left(\frac{\chi_i}{\chi_0}\right)$$

where:

- $\chi_i = (\mathbf{b}_{i} \times \mathbf{b}_{i+1}) \cdot \mathbf{b}_{i+2}$ is the scalar triple product of consecutive bond vectors (positive for right-handed twist)
- $w_\text{helix}^{(i)} = \max(0, 1 - \bar{Z}^{(i)}/2)$ suppresses chirality for sheet-forming segments
- $\chi_0 = d_0^3 / 11 \approx 5.0$ \AA$^3$ normalises the triple product
- $\tanh$ saturates the signal to $[-1, 1]$

This is the sole source of L/D selectivity in the engine: right-handed helices receive a phase bonus ($\delta_\chi > 0$) that lowers their electrical length and reduces $S_{11}$.

## Layer 7: Cross-Coupled Cavity Filter

A folded protein is a set of coupled resonant cavities, not a single cascade. The engine identifies segment boundaries via the local reflection coefficient:

$$\Gamma_j = \frac{|Z_{j+1}| - |Z_j|}{|Z_{j+1}| + |Z_j|}, \qquad \text{turn indicator: } t_j = \sigma(20(\Gamma_j - 0.3))$$

### Layer 7a: Adjacent Junction Coupling

At each detected turn, the transmission between adjacent segments is:

$$S_{21}^{(j)} = (1 - \Gamma_j^2) \cdot \frac{2\bar{Z}_L \bar{Z}_R}{\bar{Z}_L^2 + \bar{Z}_R^2} \cdot \exp\!\left(-\frac{|\mathbf{c}_L - \mathbf{c}_R|}{R_\text{burial}}\right)$$

where $\bar{Z}_{L,R}$ and $\mathbf{c}_{L,R}$ are the mean impedance and centroid of the left/right segments.

### Layer 7b: Non-Adjacent Cross-Coupling

For all segment pairs $(p, q)$ with $|p - q| \geq 2$ (skipping the nearest neighbour):

$$S_{21}^{(p,q)} = \frac{2\bar{Z}_p \bar{Z}_q}{\bar{Z}_p^2 + \bar{Z}_q^2} \cdot \exp\!\left(-\frac{|\mathbf{c}_p - \mathbf{c}_q|}{R_\text{burial}}\right)$$

The port coupling loss rewards high $|S_{21}|^2$:

$$\mathcal{L}_\text{port} = \underbrace{\frac{1}{N}\sum_j t_j(|S_\text{self}|^2 - |S_{21}|^2)}_{\text{junction loss}} - \underbrace{\frac{1}{N}\sum_{p<q, |p-q|\geq 2} |S_{21}^{(p,q)}|^2}_{\text{cross-coupling bonus}}$$

## Layer 8: Bond Integrity and Steric Exclusion

Two hard physical constraints are added as regularisation penalties:

$$\begin{align}
\mathcal{L}_\text{bond}    &= \frac{2}{N} \sum_{i=0}^{N-2} (d_{i,i+1} - d_0)^2 \\
\mathcal{L}_\text{steric}  &= \frac{1}{N} \sum_{\substack{i < j \\ |i-j| \geq 3}} \max(0,\; r_\text{steric} - d_{ij})^2
\end{align}$$

These are not "forces"---they are smooth, differentiable loss terms whose gradients enforce backbone connectivity ($d_i \approx 3.8$ \AA) and prevent chain self-intersection ($d_{ij} > 3.4$ \AA).

---
