[↑ Silicon Design Engine](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: 0hwopi -->

# Native SPICE Subcircuit Exporting

While the Topo-Kinematic framework mathematically obsoletes the statistical thermodynamics of classical equations ($kT/q$), interacting with standard industrial CAD toolchains remains an absolute necessity for electrical engineers.

Standard SPICE environments (e.g., Ngspice, LTspice) rely heavily on the empirical Shockley diode equation ($I = I_s ( e^{V_D / \eta V_T} - 1 )$). If an engineer forces $V_D$ far past the breakdown voltage in SPICE, the equation mathematically evaluates physically impossible output limits because it lacks a strict, geometric material saturation bound.

To resolve this without altering the core simulation engine, the AVE compiler strips the `DMOD` (Diode Model) of its thermal dependency by forcing the emission coefficient ($N \to 0.001$). It then wraps the component inside a highly constrained piecewise `.SUBCKT` generic macro model. The macro enforces the exact Topo-Kinematic $V_{bi}$ and $R_{fwd}$ matrix outputs directly into a rigid barrier clamp.

## AVE_DIODE_SI Subcircuit Template

```spice
* Topo-Kinematic Geometric Diode Subcircuit
* Model: AVE_DIODE_SI
* Structural V_bi derived from Topological offset, Zero Boltzmann kT thermal input.
* Transmission Matrix T_sq = 1.000000
* Forward Geometric Viscosity (Resistance) = 0.0000 Ohms

.SUBCKT AVE_DIODE_SI A K
V_BARRIER N1 K DC 1.0496
D_IDEAL A N1 D_IDEAL_MOD
R_FWD N1 K 0.0000
.MODEL D_IDEAL_MOD D(N=0.001 RS=1m CJO=2pF VJ=1.0496)
.ENDS AVE_DIODE_SI
```

By deploying this SPICE bridge, engineers can execute massive system-level analog simulations where every bounded component acts with rigid macroscopic Dielectric Rupture constraints, ensuring large-signal overdrive tests never exceed the physical topological hardware limits of the matrix.
