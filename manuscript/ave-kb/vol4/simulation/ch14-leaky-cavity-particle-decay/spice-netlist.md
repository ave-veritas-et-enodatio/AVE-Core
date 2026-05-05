[↑ Ch.14: Leaky Cavity Particle Decay](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [c54kdd]
-->

## SPICE Netlist: Particle Decay (leaky_cavity.cir)

```spice
* Leaky Cavity (Particle Decay) SPICE Model *
* ----------------------------------------- *

* The Topological Knot
C1 N_TOP GND 1nF IC=150kV ; Initial Muon Pump Energy
L1 N_TOP GND 1mH

* The Vacuum Breakdown Boundary
* SW switches from R_OFF (1G) to R_ON (50) if V(N_TOP) > 43.65kV
S1 N_TOP GND N_TOP GND VAC_BREAKDOWN
.MODEL VAC_BREAKDOWN VSWITCH(Ron=50 Roff=1G Von=43650 Voff=43640)

* Symmetrical Negative Breakdown (for the negative AC swing)
S2 N_TOP GND GND N_TOP VAC_BREAKBACK
.MODEL VAC_BREAKBACK VSWITCH(Ron=50 Roff=1G Von=43650 Voff=43640)

.TRAN 10ns 200us UIC
.END
```

---
