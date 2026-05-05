[↑ App F: Universal Solver Toolchain](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: d9ivj1 -->

## Cross-Scale Isomorphism Table

The same solver applies at every scale:

| | BH QNM | Electron | Nuclear | Protein | Antenna | Tokamak | BLDC Motor |
|---|---|---|---|---|---|---|---|
| Saturation | $\varepsilon_{11} = 1$ | $V = \alpha$ | $V_R / V_{BR} \to 1$ | Pauli exclusion | $V_{\mathrm{SNAP}}$ | $\beta$ limit | Back-EMF = $V_{supply}$ |
| $r_{\mathrm{sat}}$ | $7M_g$ | $l_{node}$ | $V_{BR} = 6\alpha\hbar c/D$ | $d_0 = 3.80$ A | Stub length | Wall radius | Stall current |
| $\nu$ correction | 2/7 | $\alpha$ | $\alpha$ | 2/7 | 2/7 | 2/7 | Winding factor |
| Mode $\ell$ | 2 (GW) | $n,l$ | 5 (cinquefoil) | 7 ($d_0/a_0$) | $\lambda/4$ | Alfven | Pole pairs |
| $Q$ source | $Q = \ell$ | Spectral width | Miller stages | $Q = 7$ | BW | Confinement | $Q = \ell$ (mech.) |
| Co-rotation | Frame drag $\Omega$ | --- | Shell rotation | --- | --- | Plasma rot. | Rotor $\theta_r$ (FOC) |
| Regime I | Flat space | Bound | Sub-critical | Folded | Short | Core | Motoring |
| Regime II | Curved | Free | Avalanche | Unfolded | Open | SOL | Generating |

For each domain, the procedure is identical:

1. Map the domain's strain field to $\varepsilon_{11}$.
2. Find where $S = 0$ (regime boundary).
3. Apply $r_{\mathrm{eff}} = r_{\mathrm{sat}}/(1 + \nu_{\mathrm{vac}})$.
4. Compute $\omega = \ell \cdot v_{\mathrm{wave}} / r_{\mathrm{eff}}$.
5. Extract $Q = \ell$ from the lattice phase transition.
6. If rotating: apply co-rotating frame decomposition $\omega_I = (\omega_R - m\Omega)/(2\ell)$.

Step 6 is the Park transform (FOC) generalisation, applicable whenever the system has a co-rotating component (BH spin, nuclear shell rotation, motor rotor, tokamak plasma rotation).

---
