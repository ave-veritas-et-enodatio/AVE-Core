[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: w6kk5y -->

## Stage E1: Same-Shell Bonding Mode

Within each shell of principal quantum number $n$, all $N_n$ electrons are identical LC resonators at frequency $\omega_n$ with pairwise coupling $k_n$ (Hopf or orthogonal, from Stage C).

**Derivation from Stage D.** For $N$ identical nodes, the Y-matrix from Stage D has self-admittance $Y_{ii} = 1/Z_{LC} + (N{-}1)\,y$ and mutual $Y_{ij} = -y$, with $y = k/Z_{LC}$. This matrix can be written:

$$
[Y] = \left(\frac{1}{Z_{LC}} + Ny\right)\,\mathbf{I} \;-\; y\,\mathbf{J}
$$

where $\mathbf{I}$ is the identity and $\mathbf{J}$ is the all-ones matrix. The eigenvalues of $\mathbf{J}$ are $N$ (eigenvector: all in-phase) and $0$ ($N{-}1$ fold degenerate: out-of-phase modes).

The bonding mode has the **lowest admittance** (highest impedance) — it is the mode where all $N$ current rings oscillate in phase, and the mutual coupling effectively increases the inertia of each node.

In LC terms: the in-phase mode sees an effective capacitance $C_{\text{eff}} = C_0(1 + k(N{-}1))$, while the inductance $L_0$ is unchanged. Therefore:

$$
\omega_{\text{bond}} = \frac{1}{\sqrt{L_0\,C_{\text{eff}}}} = \frac{\omega_0}{\sqrt{1 + k(N{-}1)}}
$$

The bonding mode energy follows from the virial theorem and the standing wave condition:

$$
E_{n,\text{bond}} = \frac{Z^2 R_y / n^2}{\sqrt{1 + k_n(N_n - 1)}}
$$

where $k_n$ is the per-pair coupling coefficient for shell $n$. The antibonding modes are unoccupied (they represent an excited configuration).

*Verification (He):* $Z=2$, $n=1$, $N_1 = 2$, $k_1 = (2/2)(1 - p_c/2) = 0.9083$:

$$
E_{\text{bond}} = \frac{4 R_y}{\sqrt{1.9083}} = 39.40\,\text{eV}, \quad E_{\text{total}}(2) = 2 \times 39.40 = 78.79\,\text{eV}
$$

$\text{IE} = 78.79 - 54.42 = 24.37\,\text{eV}$. $\checkmark$

---
