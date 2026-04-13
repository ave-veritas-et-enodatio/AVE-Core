[↑ Ch.26: Performance Benchmarking](./index.md)
<!-- leaf: verbatim -->

# Metric II: Viscous Drag Loss ($P_{drag}$)

**Replaces:** Power Dissipation ($P = I^2 R$)

In a Topo-Kinematic waveguide, no charge drifts. Instead, the propagating wave exerts *rotational torque* on the molecular bonds of the dielectric. The resulting molecular friction is characterized by the loss tangent $\tan\delta$. Integrating volumetrically:

$$P_{drag} = \omega\,\mu_{visc}\,\kappa_{topo}\,\tan(\delta) \iiint_{V} |S(\mathbf{r})|^2\, dV$$

The critical distinction: $P_{drag} \propto \omega$, the operational frequency. Unlike $I^2R$, which can be reduced by lowering resistance, Viscous Drag scales *linearly with clock rate*. This is the fundamental reason FR-4 substrates are thermally unsuitable at $1.8\,\text{THz}$: the molecular bonds rotate at $1.8 \times 10^{12}$ times per second, generating kilowatts of friction before the dielectric melts.

SOI Photonics ($\tan\delta = 0.0001$) generates $\approx 19.8\,\text{W}$ — well within a standard $250\,\text{W}$ socket.
