[↑ Ch.16: Sagnac Inductive Drag](../index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: cbwd77 -->

## SPICE Netlist: Sagnac Inductive Drag (sagnac_ring.cir) — Single Node

```spice
* Sagnac Effect SPICE Model (Node N Segment) *
* ------------------------------------------ *

* Parameters
.param L0=1uH C0=1pF S_DRAG=0.05

* Node Capacitance
C_N NODE_N GND {C0}

* Directional Inductor linking Node N to Node N+1
* A Behavioral Current Source is used to model V = L * di/dt
* where L depends on the sign of the current (I_sense)
V_SENSE NODE_N NODE_INT 0  ; 0V source to measure current
B_IND NODE_INT NODE_N_PLUS_1 I = sdt( V(NODE_INT, NODE_N_PLUS_1) /
+ { IF( I(V_SENSE) > 0, L0*(1 - S_DRAG), L0*(1 + S_DRAG) ) } )

* (This pattern repeats for all 50 nodes in a closed circle)

.TRAN 1ns 2us
.END
```

---
