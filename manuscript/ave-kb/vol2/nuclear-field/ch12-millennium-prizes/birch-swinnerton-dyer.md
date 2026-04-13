[↑ Ch. 12: Mathematical Limits and the Millennium Prizes](./index.md)
<!-- leaf: verbatim -->

## The Birch and Swinnerton-Dyer Conjecture

### The Mathematical Paradox (What Clay Asks)

Relate the number of rational points on an elliptic curve (its "rank") to the order of vanishing of its associated $L$-function at $s=1$.

### Step 1: Elliptic Curve as Torus

An elliptic curve $E$ over $\mathbb{C}$ is topologically a 2-torus $T^2 = S^1 \times S^1$. In AVE, every stable particle is a $(2,q)$ torus knot --- a standing wave wound on $T^2$ embedded in the 3D vacuum lattice. The torus arises from Axiom 1 (discrete lattice with periodic boundary conditions on compact topological defects).

### Step 2: Rational Points as Phase-Locked Winding Orbits

A straight-line orbit on $T^2$ with slope $p/q$ (rational) closes after $p$ windings in $\theta_1$ and $q$ windings in $\theta_2$. Only orbits with **rational** slope close and satisfy the phase-matching condition. A "rational point" on the elliptic curve is a **phase-locked winding orbit** on $T^2$.

### Step 3: Rank from the Mutual Inductance Matrix

Each closed orbit on $T^2$ is a current loop --- an inductor wound on the torus. Multiple orbits couple through their shared magnetic flux. The mutual inductance $M_{ij}$ is computed from the same coupled resonator framework used for nuclear binding:

$$
M_{ij} = \frac{K_\mathrm{MUTUAL}}{d_{ij}}
$$

For $N$ independent winding orbits, the coupling forms an $N \times N$ mutual inductance matrix $\mathbf{M}$:

> **[Resultbox]** *BSD Rank from Coupled Inductors*
>
> $$
> \mathrm{rank}(E(\mathbb{Q})) = \mathrm{rank}(\mathbf{M})
> $$

### Step 4: $L$-Function as Weighted Spectral Response

The $L$-function encodes the lattice spectral response weighted by the knot's scattering:

$$
L(E, s) = \sum_{n=1}^{\infty} a_n \, n^{-s} = \prod_{p\;\mathrm{prime}} L_p(E, s)^{-1}
$$

The functional equation relates $L(E,s)$ to $L(E, 2-s)$:

> **[Resultbox]** *$L$-Function Reciprocity (Weight 1)*
>
> $$
> \Lambda(E, s) = \Lambda(E, 2-s) \qquad \text{(symmetry axis at } s = 1\text{)}
> $$

The symmetry centre shifts from $\sigma = 1/2$ (Riemann, weight 0) to $s = 1$ (elliptic, weight 1) because the knot topology adds one factor of $n$ to the spectral density.

### Step 5: Order of Vanishing at $s = 1$

At $s = 1$, the order of vanishing of $L(E, s)$ counts the number of independent resonances at the spectral boundary. Each independent orbit contributes one zero:

$$
\mathrm{ord}_{s=1}\, L(E, s) = \mathrm{rank}(\mathbf{M}) = \mathrm{rank}(E(\mathbb{Q}))
$$

The lattice additionally imposes an **upper bound** on the rank via the confinement equation $r_\mathrm{opt} = \kappa_\mathrm{FS}/c \geq \ell_\mathrm{node}$:

$$
c_\mathrm{max} = \lfloor \kappa_\mathrm{FS} \rfloor \approx \lfloor 8\pi \rfloor = 25
$$

---
