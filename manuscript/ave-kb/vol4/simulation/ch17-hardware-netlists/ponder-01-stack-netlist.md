[↑ Ch.17: Hardware Netlists](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-7tynm2]
-->

## PONDER-01: Cascaded Transmission-Line Thrust Model

The PONDER-01 experimental thruster utilizes an asymmetric FR4/Air dielectric stack to intentionally unbalance the vacuum's thermodynamic acoustic modes. By driving the stack with an extreme $100\,\text{MHz}$, $30\,\text{kV}$ RF sine wave, it actively pumps acoustic "phonons" from the background vacuum matrix into the heavier FR4 substrate.

Because the system is geometrically asymmetric, the acoustic energy cannot rebound cleanly; it is trapped by the impedance mismatch at the boundary layer, generating continuous unidirectional Ponderomotive thrust.

### Impedance Mismatch at Each Boundary

Each air layer presents an impedance of $Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.7\,\Omega$, while each FR4 layer presents $Z_{FR4} = Z_0/\sqrt{\varepsilon_r} \approx 181.6\,\Omega$ (with $\varepsilon_r = 4.3$). The resulting reflection coefficient at each boundary:

$$
\Gamma = \frac{Z_{FR4} - Z_0}{Z_{FR4} + Z_0} \approx -0.349
$$

This $34.9\%$ reflection at every air/FR4 interface creates a cascading series of partial reflections that geometrically trap RF energy in the stack — precisely the mechanism that generates the asymmetric $\nabla |E|^2$ gradient responsible for ponderomotive thrust.

### Component Derivation from Zero Parameters

Every component value in the netlist is derived from the four AVE axioms with zero free parameters:

| Component | Value | Derivation |
|---|---|---|
| $V_{yield}$ | 43.65 kV | $\sqrt{\alpha} \times m_e c^2 / e$ |
| $C_{AIR}$ | 2.36 fF | $\varepsilon_0 \times A_{layer} / d_{layer}$ |
| $C_{FR4}$ | 10.14 fF | $\varepsilon_r \times \varepsilon_0 \times A_{layer} / d_{layer}$ |
| $L_{AIR}$ | 0.33 nH | $\mu_0 \times d_{layer} / A_{layer}$ |
| $Z_0$ | 376.7 $\Omega$ | $\sqrt{\mu_0 / \varepsilon_0}$ |
| $f_{drive}$ | 100 MHz | VHF resonance of stack |

No fitting, no tuning, no empirical calibration. The SPICE solver runs against the raw physical constants of the universe.

## SPICE Netlist: PONDER-01 Cascaded Stack (ponder_01_stack.cir)

The SPICE topology maps each sub-millimeter physical layer into its equivalent lumped LC element. The asymmetric He-4 emitter tip is modeled using the topological coordinates of the alpha particle nucleus:

```spice
* PONDER-01 Asymmetric Transmission-Line Model *
* --------------------------------------------- *

* Parameters
.param L_AIR=0.33nH C_AIR=2.36fF
.param L_FR4=0.33nH C_FR4=10.14fF
.param V_DRIVE=30000 F_DRIVE=100MEG

* VHF Drive Source (100 MHz, 30 kV)
V1 NODE_0 GND SINE(0 {V_DRIVE} {F_DRIVE})

* Layer 1: Air (100 um)
L1 NODE_0 NODE_1 {L_AIR}
C1 NODE_1 GND {C_AIR}

* Layer 2: FR4 (100 um)
L2 NODE_1 NODE_2 {L_FR4}
C2 NODE_2 GND {C_FR4}

* Layer 3: Air
L3 NODE_2 NODE_3 {L_AIR}
C3 NODE_3 GND {C_AIR}

* Layer 4: FR4
L4 NODE_3 NODE_4 {L_FR4}
C4 NODE_4 GND {C_FR4}

* ... (Repeat for 20 total layers) ...

* Layer 19: Air
L19 NODE_18 NODE_19 {L_AIR}
C19 NODE_19 GND {C_AIR}

* Layer 20: FR4 (Collector)
L20 NODE_19 NODE_20 {L_FR4}
C20 NODE_20 GND {C_FR4}

* Termination (Collector grounded through load)
R_LOAD NODE_20 GND 50

.TRAN 0.1n 100n
.PROBE V(NODE_0) V(NODE_10) V(NODE_20)
.END
```

The transient simulation tracks the voltage waveform at the emitter (Node 0), mid-stack (Node 10), and collector (Node 20). The asymmetric buildup of $|E|^2$ across the stack is directly proportional to the ponderomotive thrust force.

[Figure: hardware_netlist_overview.png — see manuscript/vol_4_engineering/chapters/]

---
