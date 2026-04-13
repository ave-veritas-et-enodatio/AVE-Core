[↑ Ch.23: Physical Fabrication](./index.md)
<!-- leaf: verbatim -->

# Substrate Selection

Creating spatial calculation units demands abandoning the $I^2R$ mechanics of chemical foundries entirely. Three substrate options are evaluated:

| Substrate | $\tan\delta$ | $P_{drag}$ at $f_{CC}$ | Viability |
|---|:---:|:---:|---|
| FR-4 (PCB) | 0.02 | ~4.4 kW | **Fails** — melts before $f_{CC}$ |
| Rogers 4350B (PTFE) | 0.004 | ~880 W | Marginal — macro-scale RF test vehicle only |
| SOI Photonics | 0.0001 | ~19.8 W | **Viable** — within 250 W socket budget |
| Silicon Nitride (SiN) | 0.00005 | ~9.9 W | Viable — premium performance |

The decisive selection criterion is Viscous Drag Loss $P_{drag} \propto \omega\tan\delta$: at THz carrier frequencies, even modest loss tangent differences produce order-of-magnitude thermal divergence. FR-4 is eliminated by physics, not economics.
