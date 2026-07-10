[↑ Operators and Regimes](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-9kd2t3, clm-bnd5rq, clm-bore2x, clm-gdd70j, clm-j550uh, clm-k6quve, clm-nxc9gy, clm-v3port]
subtree-experiments: []
-->

# Ch.6: Universal Operators: Z, $S$, $\Gamma$

Eight universal operators govern physics at all spatial scales without domain-specific modifications or fitting parameters. The characteristic impedance $Z = \sqrt{\mu/\varepsilon}$ is the single structural invariant. The saturation factor $S = \sqrt{1-(A/A_c)^2}$ appears in dielectric saturation, BCS critical field, galactic rotation, and relativistic mass-energy. The reflection coefficient $\Gamma = (Z_2-Z_1)/(Z_2+Z_1)$ applies identically from Pauli exclusion to seismic discontinuities.

## Key Results

| Result | Statement |
|---|---|
| Universal Impedance Operator | $Z = \sqrt{\mu/\varepsilon}$; single structural invariant across all scales |
| Universal Saturation Factor | $S(A,A_c) = \sqrt{1-(A/A_c)^2}$ |
| Universal Reflection Coefficient | $\Gamma = (Z_2-Z_1)/(Z_2+Z_1)$ |
| Universal Pairwise Potential | $U(r) = -(K/r)(T^2-\Gamma^2)$ |
| Multiport S-Matrix | $[S] = (I+[Y]/Y_0)^{-1}\cdot(I-[Y]/Y_0)$ |
| Eigenvalue Target | $\lambda_{\min}(S^\dagger S) \to 0$ |
| Packing Reflection Coefficient | $\Gamma_{pack} = (R_g - R_{g,target})/(R_g + R_{g,target})$ |
| srs $z=3$ Vertex Floor | $\Gamma = (2-z)/z = -1/3$; lossless-reciprocal 3-port $|S_{11}| \ge 1/3$ (circulator escape non-reciprocal) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Impedance Operator](./impedance-operator.md) | Scale Invariance theorem, cross-scale constitutive mapping (8-row table) |
| [Saturation Operator](./saturation-operator.md) | $S(A,A_c)$ across four domains: dielectric, BCS, galactic, relativistic |
| [Reflection Coefficient](./reflection-coefficient.md) | $\Gamma$ at sub-nuclear, laboratory, and planetary boundaries |
| [Pairwise Potential](./pairwise-potential.md) | Composed from operators 1--3; three-regime behaviour table |
| [Y-to-S Conversion](./y-to-s-conversion.md) | Multiport S-matrix generalisation |
| [Eigenvalue Target](./eigenvalue-target.md) | Ground state as zero singular value of $[S]$ |
| [Spectral Analyser](./spectral-analyser.md) | Spatial Fourier transform of impedance sequences |
| [Packing Reflection](./packing-reflection.md) | Equilibrium packing fraction, $R_{g,target}$, $\Gamma_{pack}$ |
| [Lattice Impedance Decomposition](./lattice-impedance-decomposition.md) | Canonical six-fold decomposition $Z_0$ / $Z_{\text{cell}}$ / $Z_{\text{eff}}(r)$ / $\eta_{\text{vac}}$ / $Z_{\text{mech}}$ / $Z_{\text{EH}}$; lattice-native units ($V_{\text{YIELD}} = 1$) |
| [K4 4-Port Irrep Decomposition ($A_1 \oplus T_2$)](./k4-port-irrep-decomposition.md) | Under $T_d$ the 4-port space is $A_1 \oplus T_2$; the K4-TLM scattering matrix has eigenvalues $\{+1, -1, -1, -1\}$; $A_1$ dissipates, $T_2$ survives as the photon |
| [srs Band Structure](./srs-band-structure.md) | The srs vacuum-net linear band structure: scalar 4-band top $\pi\sqrt3\,\omega_C$ at $H$, vector 12-band top BRACKET $[5.441, 17.011]\,\omega_C$, NO internal gap either channel; the transmission-line arccos map is substrate-native (graph-Laplacian $\omega=\sqrt\lambda$ fails the $1/\sqrt3$ gate) |
| [srs Vertex Scattering](./srs-vertex-scattering.md) | The srs $z=3$ vertex reflection floor: bare $\Gamma=(2-z)/z=-1/3$ (counting fact), the lossless-reciprocal 3-port theorem $\|S_{11}\|\ge 1/3$ (Pozar-class, confirmed at the vertex), the sole escape = non-reciprocity (circulator witness, T-breaking PENDING-GRANT), and the two-axis Op6 bore verdict (broadband $f^{*}=0$ unique; single-frequency $\{0, f_{\text{touch}}\}$ degenerate) |
