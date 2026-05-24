[↑ Ch. 11: The Standard Model Overdrive](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-dboxok]
-->

## Computational Scaling Comparison

| Method | Scaling | Parameters | Hardware |
|---|---|---|---|
| Lattice QCD (nuclear) | $O(N^3)$+ | $\sim$6 | Supercomputer (months) |
| AlphaFold (protein) | $O(N^2)$ | $\sim 10^8$ (NN weights) | GPU cluster (hours) |
| DFT (molecular) | $O(N^3)$ | $\sim$10 (XC functional) | HPC (days) |
| **AVE Universal** | $O(N^2)$ | **0** | Single core (seconds) |

The critical distinction is the "Parameters" column. Lattice QCD requires input quark masses, QCD coupling, and lattice spacing. AlphaFold requires $\sim 10^8$ trained neural network weights derived from the PDB. DFT requires an exchange-correlation functional. The AVE engine requires **zero adjustable parameters** --- every coupling constant is derived from the three calibration inputs ($l_{node}$, $\alpha$, $G$).

---
