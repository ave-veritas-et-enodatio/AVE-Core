[↑ Ch.23: Physical Fabrication](./index.md)
<!-- leaf: verbatim -->

# Phase Dispersion Characterization

The fabrication tolerance of the dielectric constant $\kappa_{topo}$ directly determines the phase coherence yield $\eta_{PY}$. Across a computation path of length $L$, substrate non-uniformity $\Delta\kappa_{topo}$ accumulates phase dispersion:

$$\Delta\phi = \int_L \frac{\omega}{2c_0\sqrt{\kappa_{topo}}} \Delta\kappa_{topo}(x)\,dx$$

For the APU to maintain $\eta_{PY} > 1 - 10^{-6}$, the phase walk across the characteristic computation length must satisfy $\Delta\phi < \pi/10$. SOI substrates with foundry-grade uniformity ($\Delta\kappa/\kappa < 10^{-4}$) achieve this requirement over $10\,\text{mm}$ paths.

> **[Resultbox]** *Chapter 23 Summary*
>
> Creating spatial calculation units demands abandoning the $I^2R$ mechanics of chemical foundries entirely. Whether routing utilizing specialized PTFE planar microwave arrays, extreme-node Silicon Photonics, or Silicon Nitride substrates — the decisive criterion is the loss tangent at THz operating frequencies.
