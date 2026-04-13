[↑ Ch.26: Performance Benchmarking](./index.md)
<!-- leaf: verbatim -->

# Metric I: Carrier Coherence Frequency ($f_{CC}$)

**Replaces:** Clock Speed (GHz)

In the APU, the "clock" is not imposed — it is an eigenvalue of the substrate geometry. A resonance cavity of length $L$ in a dielectric with compliance $\kappa_{topo}$ supports a standing wave at frequency:

$$f_{CC} = \frac{c_0}{2L\sqrt{\kappa_{topo}}}$$

This is not programmable in the software sense. Changing $f_{CC}$ means physically remanufacturing $L$. The fabrication tolerance *is* the clock specification. For the TSMC 3nm node ($L = 24\,\text{nm}$, $\kappa_{topo} = 3.9$):

$$f_{CC} = \frac{2.998 \times 10^8}{2 \times 24 \times 10^{-9} \times \sqrt{3.9}} \approx 1.832\,\text{THz}$$
