[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: oltvwy -->

## The Atom as an Analog Ladder Filter

Each filled shell acts as an independent AC motor winding, with asynchronous frequency decoupling eliminating cross-shell mutual inductance. This insight admits a powerful restatement: **each filled shell is a filter section in a passive analog ladder network.**

### Screening as Frequency-Dependent Filtering

The nuclear Coulomb field $V(r) = Ze^2/(4\pi\epsilon_0 r)$ is a broadband source. An inner filled shell does not statically subtract charge from $Z$; it *filters* the nuclear field before it reaches the outer electron, with a frequency-dependent transfer function $H(\omega)$:

```
NUCLEUS → 1s² filter section → 2s² filter section → 2p^N filter section → VALENCE PORT → Z_eff → IE
```

Static screening rules ($\sigma \approx 2.0$) are the DC limit of this transfer function. The full frequency-dependent filter captures effects that no static constant can encode: resonant enhancement between shells, passband structure of the emission spectrum, and the harmonic stability of closed-shell configurations.

### LC Components of the $1s$ Flux Loop

Each electron flux loop ($0_1$ unknot, major radius $R = r_n$, tube radius $a = l_{node}$) has three circuit parameters derivable entirely from engine constants.

**Self-Inductance.** The inductance of a circular current loop in free space:

$$
L_n = \mu_0 R_n \left[\ln\!\left(\frac{8R_n}{l_{node}}\right) - 2\right]
$$

For the $1s$ shell with $R_1 = a_0/Z_\text{eff}$ and $Z_\text{eff} = 27/16$: $L_1 = 1.764 \times 10^{-16}$ H.

**Orbital Frequency.** From the phase-locking condition $v_n = Z_\text{eff} \alpha c / n$:

$$
\omega_1 = \frac{Z_\text{eff} \alpha c}{a_0} = 6.976 \times 10^{16} \text{ rad/s}
$$

**Coulomb Capacitance.** From the resonance condition $\omega_1 = 1/\sqrt{L_1 C_1}$:

$$
C_1 = \frac{1}{\omega_1^2 L_1} = 1.165 \times 10^{-18} \text{ F}
$$

**Characteristic Impedance.** The flux loop's own impedance:

$$
Z_{LC} = \sqrt{\frac{L_1}{C_1}} = 12.31 \text{ $\Omega$}
$$

This is *not* 377 $\Omega$. The electron interacts with the vacuum's bulk modulus (acoustic impedance), not the shear modulus (electromagnetic impedance). This $Z_{LC} = 12$ $\Omega$ is the reason atomic physics operates in the *low-impedance* regime — the electron's circuit impedance is $Z_{LC}/Z_0 \approx 0.033 = \alpha/\pi$, consistent with the fine structure constant governing all electromagnetic coupling.

**Electromagnetic Self-Energy.** The energy stored in the self-inductance with orbital current $I = e\omega_1/(2\pi)$:

$$
E_L = \tfrac{1}{2}L_1 I^2 = 0.0017 \text{ eV}
$$

This confirms: the electromagnetic self-energy is $\alpha^4$-scale ($\sim 10^{-4}$ Ry), negligible for gross binding.

### Intra-Shell Coupling: Coulomb Capacitance, Not Mutual Inductance

The two $1s$ flux-loop charge quanta in Helium are *not* separate loops with mutual inductance. They are two charges on the **same** flux ring, separated by angle $\phi$. Their coupling is **Coulomb repulsion** — a coupling *capacitance* $C_\text{rep}$, not a mutual inductance $M$.

At equilibrium ($\phi = \pi$, antipodal):

$$
V_\text{rep}(\pi) = \frac{\alpha \hbar c}{2R_1} = \frac{Z_\text{eff}}{2}\,E_H = 22.96 \text{ eV}
$$

This corresponds to $J = 1/2$ (the geometric floor for antipodal point charges). The topological phase-jitter correction elevates this to $J_{s^2} = \frac{1}{2}(1 + p_c) = 0.5917$.

### Multi-Shell Filter Cascade

For atoms with $Z \geq 3$, each filled subshell adds one filter section to the ladder. The total transfer function is the ABCD cascade product:

$$
\mathbf{T}_\text{total} = \prod_{k=1}^{N_\text{shells}} \mathbf{T}_k, \qquad \mathbf{T}_k = \begin{bmatrix} 1 + Z_k Y_k & Z_k \\ Y_k & 1 \end{bmatrix}
$$

where $Z_k = j\omega L_k$ is the series impedance (inertia of the flux loop) and $Y_k = j\omega C_k$ is the shunt admittance (Coulomb coupling to the nucleus) of the $k$-th shell.

The effective nuclear charge seen by the valence electron emerges from the voltage transfer ratio at the output port:

$$
Z_\text{eff}(\omega) = Z \cdot |H(\omega_\text{valence})| = Z \cdot \left|\frac{1}{A + B/Z_\text{term}}\right|
$$

This filter framework naturally produces:
- **Energy levels as filter poles.** The resonant frequencies of each section correspond to the orbital energy levels.
- **Spectral lines as passband peaks.** Photon emission/absorption occurs at frequencies where $|H(\omega)|$ has maxima.
- **Selection rules as filter symmetry.** The $\Delta \ell = \pm 1$ selection rule arises from the orthogonality of the filter section transfer functions.
- **Noble gas stability as maximum filter Q.** Fully balanced filter sections present minimum coupling to external perturbations.

---
