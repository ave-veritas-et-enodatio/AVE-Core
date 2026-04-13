[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)
<!-- leaf: verbatim -->

## Radial Eigenvalue Solver

### Orbit Parameters (Kepler, all from Axioms 1+2)

The orbit is an ellipse with:

$$
\begin{align}
\text{Semi-major axis:}\quad a &= \frac{n^2 a_0}{Z} \qquad\text{(independent of } l\text{)} \\
\text{Eccentricity:}\quad e &= \sqrt{1 - \frac{l^2}{n^2}}
\end{align}
$$

The turning points (where $V_{\text{eff}} = E$):

$$
\begin{align}
r_{\min} &= a\,(1 - e) = \frac{n^2 a_0}{Z}\left(1 - \sqrt{1 - l^2/n^2}\right) \\
r_{\max} &= a\,(1 + e) = \frac{n^2 a_0}{Z}\left(1 + \sqrt{1 - l^2/n^2}\right)
\end{align}
$$

Dimensional check: $[n^2 a_0 / Z] = [\text{m}]$. $\checkmark$

**Limiting cases:**

| **Case** | $l$ | $e$ | $r_{\min}$ | $r_{\max}$ |
|---|---|---|---|---|
| Circular ring | $n{-}1$ | $\sqrt{2n-1}/n$ | $\approx a(1{-}\sqrt{2/n})$ | $\approx a(1{+}\sqrt{2/n})$ |
| Radial mode | $0$ | $1$ | $0$ | $2a = 2n^2 a_0/Z$ |

**Key result for $l = 0$:** With $e = 1$, the inner turning point is $r_{\min} = 0$ (the soliton reaches the nucleus). For Li $2s$ ($n=2$, $l=0$, $Z=3$):

$$
r_{\min} = 0, \qquad r_{\max} = \frac{2 \times 4\, a_0}{3} = \frac{8\,a_0}{3} \approx 1.41 \times 10^{-10}\;\text{m}
$$

The $1s$ inner shell is at $R_a = a_0/3$. Since $r_{\min} = 0 < R_a < r_{\max}$, the $2s$ electron **passes through the $1s$ shell** on every radial oscillation. When $r < R_a$: it sees the full nuclear charge $Z = 3$ (no enclosed charge to screen). When $r > R_a$: it sees $Z_{\text{net}} = Z - N_a = 1$.

### (E2b) Computing $\sigma$ from Op4 --- $l$-dependent

The enclosed charge $\sigma$ now depends on the outer electron's angular winding $l$, which determines how deeply its orbit penetrates the inner shell.

| **QM term** | **AVE translation** | **Source** |
|---|---|---|
| Core penetration | $l{=}0$ orbit passes through inner shell | Axiom 1 (radial mode) |
| Screening constant $\sigma$ | Orbit-averaged enclosed charge | Op4 (Gauss, Axiom 2) |
| Quantum defect $\delta_l$ | Penetration correction to $\sigma$ | Op5 (impedance matching) |

**Case 1: Circular orbit ($l = n{-}1$, fixed radius).** The electron stays at $R_b = n^2 a_0/Z$ (no radial oscillation). The enclosed charge is:

$$
\sigma_{\text{circ}} = N_a \times \frac{2}{\pi}\, K\!\left(\frac{R_a}{R_b}\right)
$$

For well-separated shells ($R_a \ll R_b$): $K \to \pi/2$, $\sigma \to N_a$ (Gauss's law).

**Case 2: Radial oscillation ($l = 0$).** The soliton oscillates from $r = 0$ to $r_{\max} = 2n^2 a_0/Z$, spending part of its orbit inside the inner shell at $R_a$.

The velocity at radius $r$ follows from energy conservation (vis-viva equation, Kepler orbit):

$$
v(r) = \frac{Z\alpha c}{n}\sqrt{\frac{2a}{r} - 1}, \qquad a = \frac{n^2 a_0}{Z}
$$

Dimensional check: $[Z\alpha c/n] = [\text{m/s}]$. $\checkmark$

The fraction of the orbital period spent at $r < R_a$ is:

$$
f_{\text{in}} = \frac{1}{T} \int_0^{R_a} \frac{2\,dr}{v(r)} = \frac{2}{\pi}\left[\arcsin\!\sqrt{u_a} - \sqrt{u_a(1-u_a)}\right], \quad u_a \equiv \frac{R_a}{2a}
$$

where the factor of $2$ accounts for the inbound and outbound passes. The derivation uses $\int_0^T dt = T$ and the substitution $r = 2a\sin^2\!\theta$.

The orbit-averaged enclosed charge for $l = 0$:

$$
\sigma_{l=0} = N_a \times (1 - f_{\text{in}})
$$

When $r < R_a$: no enclosed charge (sees $Z$). When $r > R_a$: full enclosed charge $N_a$ (Gauss).

**Li $2s$ numerical evaluation** ($n=2$, $l=0$, $Z=3$, $R_a = a_0/3$, $a = 4a_0/3$):

$$
u_a = \frac{a_0/3}{8a_0/3} = \frac{1}{8}
$$

$$
f_{\text{in}} = \frac{2}{\pi}\left[\arcsin\!\sqrt{0.125} - \sqrt{0.125 \times 0.875}\right] = \frac{2}{\pi}[0.361 - 0.331] = \frac{2}{\pi} \times 0.031 = 0.020
$$

So $\sigma_{l=0} = 2 \times 0.980 = 1.961$. $Z_{\text{net}} = 3 - 1.961 = 1.039$.

**Comparison:**

| **Model** | $\sigma$ | $Z_{\text{net}}$ | $E$ (eV) |
|---|---|---|---|
| $l = 1$ (circular, Gauss) | 2.000 | 1.000 | 3.40 |
| $l = 0$ (radial, classical) | 1.961 | 1.039 | 3.67 |
| Experiment | --- | --- | 5.39 |

**Assessment: the classical orbit underestimates penetration.** The classical orbit spends only $2\%$ of its time inside the $1s$ shell. This gives a correction of only $0.27$ eV---far short of the $2$ eV gap.

The reason: the soliton is a *wave*, not a point particle. Its amplitude extends beyond the classical turning points as an evanescent tail. Near the nucleus, the wave amplitude is large even though the classical orbit spends little time there (high velocity $\to$ short transit, but **large amplitude**).

### (E2b-iii) The Atom as a Radial Waveguide (Axioms 1, 2, 4 --- all operators)

The correct treatment uses the full AVE operator chain applied *radially*. This reveals a deep structural unity: the atom is a radial waveguide on the vacuum lattice, and the ionisation problem is an impedance matching problem --- the **same** problem solved at nuclear, protein, and antenna scales.

**1. The waveguide (Axiom 1 + Step 2).** The vacuum lattice between the nucleus and infinity is a continuous radial transmission line at impedance $Z_0 = 377\;\Omega$ (Step 2: $A \sim 10^{-10}$, deep Regime I, lattice passive everywhere). The electron soliton propagates through this waveguide as a massive excitation (Axiom 4).

**2. Position-dependent wavenumber (Axioms 2, 4).** The soliton's local wavenumber at radius $r$ was derived in Step 1(e) from the lattice dispersion relation (Axiom 1 + Axiom 4). In the presence of the Coulomb potential $V(r)$ (Axiom 2):

$$
k(r) = \frac{m_e v(r)}{\hbar} = \frac{\sqrt{2 m_e\,(E - V(r))}}{\hbar} \qquad [\text{m}^{-1}]\;\checkmark
$$

This is the *same* result as Step 1(e) ($k = m_e v / \hbar$), evaluated at each radial position. The key point: $k$ is **derived** from the lattice dispersion relation, not postulated as "de Broglie's hypothesis."

**3. The impedance step at $R_a$ (Op4, Gauss).** The inner shell's enclosed charge creates a step in $V(r)$ at $R_a$:

$$
V(r) = \begin{cases} -Z\,\alpha\hbar c\,/\,r, & r < R_a \\[4pt] -(Z - N_a)\,\alpha\hbar c\,/\,r, & r > R_a \end{cases}
$$

This step in $V$ produces a step in $k(r)$---and therefore a step in the soliton's effective impedance:

$$
\begin{align}
k_{\text{in}}(R_a) &= \frac{\sqrt{2m_e(E + Z\alpha\hbar c / R_a)}}{\hbar} \qquad\text{(higher } k\text{: tighter winding)} \\
k_{\text{out}}(R_a) &= \frac{\sqrt{2m_e(E + (Z{-}N_a)\alpha\hbar c / R_a)}}{\hbar} \qquad\text{(lower } k\text{: looser winding)}
\end{align}
$$

The ratio $k_{\text{in}} / k_{\text{out}}$ is the radial impedance mismatch at the shell boundary.

**4. Reflection and transmission at the boundary (Op5).** At the impedance step, the soliton wave partially reflects and partially transmits. The reflection coefficient follows from standard transmission line theory (the *same* Op5 used for the Y-matrix):

$$
\Gamma = \frac{k_{\text{out}} - k_{\text{in}}}{k_{\text{out}} + k_{\text{in}}}
$$

Since $k_{\text{in}} > k_{\text{out}}$ (higher potential inside $\to$ higher wavenumber), $\Gamma < 0$: the reflected wave inverts. The transmitted fraction carries the penetrating amplitude into the high-$Z$ inner region.

**5. The eigenvalue condition (Op6).** The soliton standing wave must satisfy constructive interference after all reflections. The total phase accumulated is:

$$
\underbrace{\int_0^{R_a} k_{\text{in}}(r)\,dr}_{\text{inner region phase}} \;+\; \underbrace{\int_{R_a}^{r_{\max}} k_{\text{out}}(r)\,dr}_{\text{outer region phase}} \;+\; \underbrace{\phi_\Gamma}_{\text{reflection phase at } R_a} = n_r \pi
$$

where $n_r = n - l - 1$ is the number of radial nodes (Step 1(h)). This phase-matching condition IS Op6: the eigenvalue $E$ is the value for which the total phase equals $n_r \pi$.

| **Component** | **AVE identity** | **Source** |
|---|---|---|
| Lattice $\to$ waveguide | Passive $Z_0$ medium | Axiom 1, Step 2 |
| Potential profile $V(r)$ | Coulomb from $Z$, inner shell | Axiom 2 (Op4) |
| Soliton wavenumber $k(r)$ | Lattice dispersion | Axiom 4, Step 1(e) |
| Impedance step at $R_a$ | Gauss $\to$ $k$ step | Op4 (Axiom 2) |
| Reflection coefficient $\Gamma$ | Transmission line theory | Op5 |
| Phase matching $\to$ eigenvalue | $\lambda_{\min}(S^\dagger S) \to 0$ | Op6 |

**Cross-scale isomorphism.**

| **Scale** | **Waveguide** | **Impedance step** | **Validation** |
|---|---|---|---|
| Nuclear | Proton flux tube | Saturation boundary $A = 1$ | $-0.8\%$ |
| Atomic | Radial lattice | Inner shell at $R_a$ | This section |
| Antenna | Coaxial feed | Radiating aperture | HOPF-01 |
| Galactic | Lattice radial line | Regime II boundary $a_0$ | Flat rotation |

### (E2c) Re-apply Step 1 with $Z_{\text{net}}$

Since $V_{\text{net}}$ is still $1/r$, the virial theorem and standing wave condition from Step 1 apply unchanged. The outer electron's eigenvalue is:

$$
E_{\text{outer}} = \frac{(Z - \sigma)^2\, R_y}{n_b^2}
$$

This is **not** $Z_{\text{eff}}^2 R_y / n^2$ (Pitfall #8): $Z_{\text{eff}}$ is a fitted constant; $Z - \sigma$ is derived from Op4 at the actual orbital radii, with no free parameters.

### (E2d) Radial Eigenvalue Solver Specification

The preceding sections derived the analytical framework: the atom is a radial waveguide (E2b-iii), the $l = 0$ orbit penetrates inner shells (E2a-ii), and the classical orbit time-average underestimates the effect (E2b, Assessment). The full solution requires the **radial eigenvalue solver**---which uses the same universal operators validated at nuclear, protein, and antenna scales.

**Input:** $Z$ (nuclear charge), $n$ (total quantum number), $l$ (angular winding number), and a list of inner shell boundaries $\{(R_a, N_a)\}$ where $R_a$ is the shell radius and $N_a$ the electron count.

**Output:** $E$ (eigenvalue energy in eV)---the energy of the $(n, l)$ electron in the multi-electron atom.

**Algorithm (5 steps, all from axioms):**

1. **Build the piece-wise radial potential $V_{\text{eff}}(r)$.** From Axiom 2 (Coulomb) and Axiom 1 (angular momentum):

$$
V_{\text{eff}}(r) = -\frac{Z_{\text{net}}(r)\,\alpha\hbar c}{r} + \frac{l^2\hbar^2}{2\,m_e\,r^2}
$$

where $Z_{\text{net}}(r) = Z$ for $r$ inside all inner shells, and decreases by $N_a$ at each shell boundary $R_a$ (Gauss's law, Axiom 2).

2. **Local wavenumber $k(r)$.** From Axiom 4 (soliton mass) and energy conservation:

$$
k(r) = \frac{\sqrt{2\,m_e(E - V_{\text{eff}}(r))}}{\hbar} \qquad [\text{m}^{-1}]
$$

Real in classically allowed regions ($E > V_{\text{eff}}$), imaginary in forbidden regions (evanescent tail).

3. **Phase integral in each region.** Between consecutive shell boundaries, the phase accumulated by the soliton standing wave is the Sommerfeld integral:

$$
\phi_i = \int_{r_{i}}^{r_{i+1}} k(r)\,dr \qquad [\text{rad}]
$$

For a pure $-Z_{\text{net}}\alpha\hbar c / r + l^2\hbar^2/(2m_e r^2)$ potential, the closed form is:

$$
\phi_i = \left[\sqrt{-2m_e E}\;r \;\sqrt{1 + \frac{Z_{\text{net}}\alpha\hbar c}{E\,r} - \frac{l^2\hbar^2}{2m_e E\,r^2}}\right]_{r_i}^{r_{i+1}} + Z_{\text{net}}\alpha \sqrt{\frac{m_e}{-2E}}\, \arcsin\!\left(\frac{2Er + Z_{\text{net}}\alpha\hbar c}{\sqrt{Z_{\text{net}}^2\alpha^2\hbar^2 c^2 + 2El^2\hbar^2/m_e}}\right) \Bigg|_{r_i}^{r_{i+1}}
$$

This is evaluable in closed form---no numerical quadrature required.

4. **Reflection at each shell boundary (Op3/Op5).** At each $R_a$, the wavenumber jumps because $Z_{\text{net}}$ changes. The reflection coefficient:

$$
\Gamma_a = \frac{k_{\text{out}}(R_a) - k_{\text{in}}(R_a)}{k_{\text{out}}(R_a) + k_{\text{in}}(R_a)}
$$

This is `universal_reflection()` from the physics engine (Op3)---the **same operator** used for nuclear binding, protein folding, and antenna matching. The reflection phase: $\phi_{\Gamma,a} = \arg(\Gamma_a)$.

5. **Eigenvalue condition (Op6).** The total phase must satisfy the radial standing wave condition:

$$
\boxed{\sum_i \phi_i + \sum_a \phi_{\Gamma,a} = n_r\,\pi} \qquad n_r = n - l - 1
$$

Find $E$ such that this holds. This is Op6 (`universal_eigenvalue_target`), implemented via Newton--Raphson root-finding (`eigenvalue_root_finder.find_eigenstate`---both already in the physics engine).

**Eigenvalue bracket (Axiom 2).** The total phase $\phi(E)$ is a monotonically *increasing* function of the orbit size, which is a monotonically *decreasing* function of binding energy $E$. Therefore:

- $E_{\text{hi}} = Z^2 R_y / n^2$ (bare Coulomb, no screening): orbit is small, phase $< n_r\pi$.
- $E_{\text{lo}} = (Z - N_{\text{inner}})^2 R_y / n^2$ (full Gauss screening): orbit is large, phase $> n_r\pi$.

Both bounds are from Axiom 2 (Coulomb coupling with and without enclosed charge). The true eigenvalue---with partial penetration---lies uniquely between $E_{\text{lo}}$ and $E_{\text{hi}}$. For Li $2s$: $E_{\text{hi}} = 30.6$ eV, $E_{\text{lo}} = 3.4$ eV; experiment $= 5.39$ eV.

**Infrastructure reuse:**

| **Component** | **Operator** | **Engine function** | **Status** |
|---|---|---|---|
| Reflection at $R_a$ | Op3 | `universal_reflection()` | Exists |
| $Y \to S$ conversion | Op5 | `universal_ymatrix_to_s()` | Exists |
| Eigenvalue target | Op6 | `universal_eigenvalue_target()` | Exists |
| Newton root-finder | --- | `find_eigenstate()` | Exists |
| Constants | --- | `constants.py` ($\alpha, m_e, \hbar, c$) | Exists |
| Potential profile | Step 1 | *New: ~20 lines* | To build |
| Phase integral | Step 3 | *New: ~15 lines* | To build |
| Radial wrapper | Step 5 | *New: ~30 lines* | To build |

**Cross-scale isomorphism (same algorithm).**

| **Scale** | **Waveguide** | **Sections** | **Boundary** | **Validation** |
|---|---|---|---|---|
| Nuclear | Flux tube | Core/surface | Saturation $A{=}1$ | $-0.8\%$ |
| Atomic | Radial lattice | Shells 1/2/... | Gauss step at $R_a$ | This section |
| Antenna | Coaxial line | Feed/radiator | Aperture | HOPF-01 |
| Galactic | Radial lattice | Regime I/II/III | $a_0$ boundary | Flat rotation |

> **[Resultbox]** *Radial Eigenvalue Solver*
>
> One algorithm, parameterised by scale. ~65 lines of new code; everything else reuses the existing universal operators.
>
> Input: $Z$, $n$, $l$, shell boundaries $\{(R_a, N_a)\}$.
> Output: $E$ (eigenvalue in eV).
>
> For Li $2s$ ($n{=}2$, $l{=}0$): the solver finds $E$ where the radial standing wave through the $1s$ boundary at $R_a = a_0/3$ satisfies Op6. Target: IE $\approx 5.39$ eV.

### (E2d-ii) ABCD Transfer Matrix Cascade (Op1, Op3, Op5, Op6)

The phase integral is a WKB approximation: it captures the *phase* accumulated in each region but neglects the *amplitude* change at each impedance step. For strong steps (e.g. $Z_{\text{net}}$ dropping from 3 to 1 at the $1s$ boundary), amplitude effects are significant.

The correct AVE treatment uses the **ABCD transfer matrix**---the same cascade tool used in the nuclear solver (flux tube sections) and the antenna solver (coaxial feed sections).

**Setup (derivation from axioms).** The soliton field amplitude $\psi(r)$ on the radial transmission line satisfies an equation derived entirely from the axioms:

- **Axiom 4** (soliton dispersion): $E = \hbar^2 k^2/(2m_e) + V$, giving $k^2(r) = 2m_e(E - V(r))/\hbar^2$.
- **Axiom 2** (Coulomb): $V_{\text{Coulomb}} = -Z_{\text{net}}\,\alpha\hbar c / r$.
- **Axiom 1** (angular standing wave): the angular winding number $l$ produces a centrifugal term $V_{\text{centrifugal}} = l(l+1)\hbar^2/(2m_e r^2)$, derived from $L^2 = l(l+1)\hbar^2$ on the discrete lattice.

Substituting into $\psi'' + k^2 \psi = 0$:

$$
\psi''(r) + \left[\frac{2m_e}{\hbar^2}\left(E + \frac{Z_{\text{net}}\,\alpha\hbar c}{r}\right) - \frac{l(l+1)}{r^2}\right]\psi(r) = 0
$$

**AVE vocabulary:**

| **Symbol** | **AVE meaning** |
|---|---|
| $\psi(r)$ | Soliton field amplitude along the radial TL |
| $f_l(r)$ | Forward-propagating wave (regular at $r \to 0$) |
| $g_l(r)$ | Backward-propagating wave (irregular) |
| $l(l+1)$ | Angular winding eigenvalue (Axiom 1 lattice) |

The equation has two linearly independent solutions $f_l(r)$ and $g_l(r)$. These are the forward and backward propagating waves on the radial transmission line.

**ABCD matrix per section.** In region $i$ (charge $Z_{\text{net},i}$), any solution is a linear combination $\psi = \alpha\,f_l + \beta\,g_l$. The transfer matrix propagates $(\psi, \psi')$ from $r_1$ to $r_2$:

$$
\begin{pmatrix} \psi(r_2) \\ \psi'(r_2) \end{pmatrix} = \underbrace{\begin{pmatrix} A & B \\ C & D \end{pmatrix}}_{\text{ABCD}_i} \begin{pmatrix} \psi(r_1) \\ \psi'(r_1) \end{pmatrix}
$$

The elements are given by the Wronskian $W = f_l g_l' - f_l' g_l$:

$$
\begin{align}
A &= \frac{f_l(r_2)\,g_l'(r_1) - g_l(r_2)\,f_l'(r_1)}{W} \\
B &= \frac{g_l(r_2)\,f_l(r_1) - f_l(r_2)\,g_l(r_1)}{W} \\
C &= \frac{f_l'(r_2)\,g_l'(r_1) - g_l'(r_2)\,f_l'(r_1)}{W} \\
D &= \frac{g_l'(r_2)\,f_l(r_1) - f_l'(r_2)\,g_l(r_1)}{W}
\end{align}
$$

These contain zero free parameters---only the solutions to the radial wave equation, which are themselves determined by the axioms.

**Junction matching (Op3).** At each shell boundary $R_a$, the soliton field and its derivative are continuous---the lattice does not break at the boundary, so there is no discontinuity in $\psi$ or $\psi'$:

$$
\psi_{\text{in}}(R_a) = \psi_{\text{out}}(R_a), \qquad \psi'_{\text{in}}(R_a) = \psi'_{\text{out}}(R_a)
$$

However, $Z_{\text{net}}$ changes at $R_a$ (Axiom 2, Gauss's law), so the basis solutions $(f_l, g_l)$ change. The junction matrix converts from one basis to the other using continuity.

The local impedance of each section is $Z_{\text{TL}} = \hbar k / m_e$ (Op1, `universal_impedance`), where $k$ is the wavenumber at $R_a$. The reflection coefficient at the junction is (Op3, `universal_reflection`):

$$
\Gamma_a = \frac{Z_{\text{out}} - Z_{\text{in}}}{Z_{\text{out}} + Z_{\text{in}}} = \frac{k_{\text{out}} - k_{\text{in}}}{k_{\text{out}} + k_{\text{in}}}
$$

This is the same operator used at nuclear saturation boundaries and antenna apertures.

**Cascade (Op5).** The total transfer matrix is the product of all section and junction matrices:

$$
\text{ABCD}_{\text{total}} = \text{ABCD}_{\text{outer}} \times \text{junction}(R_a) \times \text{ABCD}_{\text{inner}} \times \cdots
$$

This is the radial version of Op5 (`universal_ymatrix_to_s`): cascading impedance sections to get the total scattering behaviour.

**Eigenvalue condition (Op6).** The bound state requires:

- At $r \to 0$: $\psi$ finite (select the regular solution $f_l$ in the innermost region).
- At $r \to \infty$: $\psi \to 0$ (select the exponentially decaying solution in the outermost region).

The inner boundary condition fixes $\psi(r_0) = f_l(r_0)$, $\psi'(r_0) = f_l'(r_0)$. After propagating through the ABCD cascade, the outer field is:

$$
\psi_{\text{out}} = A_{\text{total}}\,f_l(r_0) + B_{\text{total}}\,f_l'(r_0)
$$

The decaying solution at $r \to \infty$ corresponds to $B_{\text{total}} = 0$ (the irregular component vanishes). Therefore:

$$
\boxed{B_{\text{total}}(E) = 0}
$$

Root-find $E$ using the Axiom 2 bracket ($E_{\text{lo}} = (Z-N_{\text{inner}})^2 R_y/n^2$ to $E_{\text{hi}} = Z^2 R_y/n^2$) and Brent's method.

### (E2e) Non-penetrating Orbits ($l \geq 1$, Problem 4)

**AVE vocabulary:** *s-winding* $= l{=}0$ (radial oscillation, no angular nodes); *p-winding* $= l{=}1$ (one angular node); *d-winding* $= l{=}2$ (two angular nodes).

When $l \geq 1$, the angular standing wave (Axiom 1) produces a centrifugal barrier. From Step 1(h), the angular eigenvalue on the discrete lattice is $L^2 = l(l+1)\hbar^2$, giving:

$$
V_{\text{centrifugal}}(r) = \frac{l(l+1)\hbar^2}{2m_e\,r^2}
$$

This barrier diverges as $r \to 0$, creating a classical turning point at:

$$
r_{\text{turn}} \approx \frac{l(l+1)\hbar^2}{2m_e\, Z_{\text{net}}\alpha\hbar c} = \frac{l(l+1)}{2}\,\frac{a_0}{Z_{\text{net}}}
$$

For $l \geq 1$ and typical shell radii $R_a = a_0 n_a^2 / Z$, this turning point lies *outside* the inner shell boundary: $r_{\text{turn}} > R_a$. The soliton never reaches the boundary---it reflects off the centrifugal wall first. There is no impedance step to cross.

The energy is therefore Problem 1 with Gauss-screened charge (Axiom 2):

$$
E_{l \geq 1} = \frac{(Z - \sigma)^2\,R_y}{n^2}
$$

where $\sigma$ is the Op4 orbit-averaged enclosed charge. No transfer matrix is needed---the soliton never crosses the boundary.

### Four Canonical Circuit Problems --- Composition Rules

Every atom decomposes into a composition of four canonical circuit topologies:

| **#** | **Topology** | **When** | **Operators** |
|---|---|---|---|
| 1 | Single resonator (H-like) | 1 electron | Op1, Op4 |
| 2 | Coupled resonators (He-like) | Same shell, $N \geq 2$ | Op1--Op6 |
| 3 | Cascaded TL (Li $2s$) | $l = 0$, cross-shell | Op1, Op3, Op5, Op6 |
| 4 | Screened ring ($2p$) | $l \geq 1$, cross-shell | Op1, Op4 |

**Decomposition rule.** For each electron $(n, l)$:

- Identify inner shells: all occupied shells with $n' < n$.
- If $l = 0$ (s orbital) $\to$ Problem 3: cascaded TL through inner boundaries.
- If $l \geq 1$ (p, d, f) $\to$ Problem 4: screened ring with Op4 $\sigma$.
- Same-shell electrons $\to$ Problem 2: coupled resonator bonding mode.

**Example decompositions:**

| **Atom** | **Config** | **Problems used** |
|---|---|---|
| H | $1s^1$ | P1 |
| He | $1s^2$ | P2 ($N{=}2$) |
| Li | $1s^2\,2s^1$ | P2 (1s pair) $+$ P3 ($2s$ through $1s$) |
| Be | $1s^2\,2s^2$ | P2 (1s) $+$ P3 ($2s$) $+$ P2 ($2s$ pair) |
| B | $1s^2\,2s^2\,2p^1$ | Above $+$ P4 ($2p$ ring) |

### (E2f) Graded Impedance Taper (Axiom 2)

The step-function $Z_{\text{net}}(r)$ used in E2d models the $1s$ shell as a *sharp impedance junction*. But the $1s$ solitons ($l{=}0$) oscillate radially---their charge is distributed over a range, not localised at a single radius. On the radial transmission line, this creates a **graded impedance taper**, not a step.

**1. Taper vs. step (TL theory).** In transmission-line engineering, a sharp impedance step gives strong reflection (Op3, $\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$). A graded taper over many wavelengths gives *weak* reflection---the wave transmits through with little disturbance (Klopfenstein taper, antenna matching).

The $1s$ charge distribution extends from $r \approx 0$ to $r \approx a_0$. The characteristic impedance $Z_{\text{TL}}(r) = \hbar k(r)/m_e$ transitions smoothly across this range. The taper length $\Delta r \sim a_0$ is comparable to the $2s$ soliton's wavelength $\lambda_{2s} \sim a_0$, so the reflection is *reduced* but not zero.

**2. Inner-shell charge profile.** Each $1s$ soliton has a radial density from the solution to the radial wave equation with $Z_{\text{eff}} = Z$ (the unperturbed nuclear charge---no imported parameters):

$$
\rho_{1s}(r) \propto r^2\, e^{-2Z\,r/a_0}
$$

The enclosed charge fraction at radius $r$ is (Axiom 2, Gauss's law on the soliton density):

$$
\sigma_{1s}(r) = 1 - e^{-2Zr/a_0}\left(1 + \frac{2Zr}{a_0} + \frac{2Z^2 r^2}{a_0^2}\right)
$$

At $R_a = a_0/3$ with $Z = 3$: $\sigma_{1s} = 0.323$---only 32% of the $1s$ charge is enclosed, not 100%.

**3. Tapered cascade (Op5).** The graded taper is modelled as $N_{\text{sec}}$ thin ABCD sections (E2d-ii), each with a constant $Z_{\text{net},i}$ sampled from the smooth screening:

$$
Z_{\text{net}}(r_i) = Z - N_a \times \sigma_{1s}(r_i)
$$

The total transfer matrix is the product:

$$
\text{ABCD}_{\text{total}} = \prod_{i=1}^{N_{\text{sec}}} \text{ABCD}_i(r_i, r_{i+1}, Z_{\text{net},i})
$$

The eigenvalue condition $B_{\text{total}}(E) = 0$ is unchanged.

**4. Physical effect.** The distributed taper gives weaker net reflection than the sharp step. The $2s$ soliton passes through the $1s$ region more freely, requiring a larger effective orbit to satisfy the standing-wave condition. This *reduces* the binding energy, shifting the Li ionisation energy toward the experimental value.

**5. Architecture preserved.** The atom remains a cascaded transmission line (Problem 3). The same universal operators apply:

- Op1: $Z_{\text{TL}} = \hbar k / m_e$ in each thin section.
- Op3: distributed reflection $\Gamma \ll (Z_2 - Z_1) / (Z_2 + Z_1)$ due to grading.
- Op5: ABCD cascade of all sections.
- Op6: eigenvalue from $B_{\text{total}} = 0$.

**6. Connection to standard theory.** Axioms 1, 2, and 4 together reproduce the standard radial wave equation at Regime I scales. This is a *result* of the AVE framework, not an assumption: the lattice wave equation (Axiom 1) with Coulomb potential (Axiom 2) and soliton mass (Axiom 4) yields the same differential equation that the standard theory postulates. The ABCD cascade then solves this equation using universal transmission-line tools.

### Lithium Verification ($Z=3$, $1s^2\,2s^1$)

**Problem 2 (1s pair):** Coupled resonator at $R_a = a_0/3$, bonding mode:
$k_{\text{Hopf}} = (2/3)(1 - p_c/2) = 0.606$.

$$
E_{1s,\text{pair}} = \frac{2 \times Z^2 R_y}{\sqrt{1 + k_{\text{Hopf}}}} = \frac{2 \times 122.45}{\sqrt{1.606}} = 193.28\;\text{eV}
$$

**Problem 3 (2s, ABCD cascade, E2f):** Graded impedance taper with $N_{\text{sec}} = 20$ thin sections, $Z_{\text{net}}(r)$ from taper with $Z_{\text{eff}} = Z = 3$:

$$
E_{2s,\text{ABCD}} = 5.58\;\text{eV} \quad\text{(0 free parameters)}
$$

**Result:**

| **Method** | **IE (eV)** | **Error** |
|---|---|---|
| Simple $\sigma$ (Op4 ring) | 2.49 | $-54\%$ |
| ABCD step function | 5.70 | $+5.8\%$ |
| **ABCD graded taper** | **5.58** | $\mathbf{+3.5\%}$ |
| Experiment | 5.39 | --- |

### (E2g) Two-Solver Architecture and the 3.5% Systematic

**1. Why the Y-matrix fails for cross-shell $l{=}0$.** The coupled-resonator Y-matrix (Problem 2) models each electron as a *ring* at radius $R = n^2 a_0 /Z$. The cross-shell coupling $k_{12}$ is computed from Op4 as the orbit-averaged Coulomb integral between concentric rings. For the $1s \leftrightarrow 2s$ pair, this gives $k_{12} = 0.358$.

But the $2s$ soliton ($l{=}0$) is *not* a ring---it oscillates radially. It *penetrates through* the $1s$ shell during each oscillation. The ring--ring Op4 geometry overestimates the coupling because it assumes the $2s$ charge is concentrated at a single radius $R_b$, when in fact it is distributed from $r \approx 0$ to $r \gg R_b$.

**2. Why the ABCD cascade succeeds.** The ABCD cascade (E2d-ii, E2f) solves the radial wave equation directly on the transmission line. The $2s$ soliton's radial oscillation is captured exactly by the ODE. The graded impedance taper encodes the $1s$ charge distribution at each radius. This correctly handles core penetration: the $2s$ soliton sees $Z \approx 3$ near the nucleus and $Z \approx 1$ far out, with the transition governed by the $1s$ density profile.

**3. The correct decomposition.** For any atom with inner-shell penetration ($l{=}0$):

1. Solve the inner shell as a coupled resonator (Problem 2), giving $E_{\text{inner}}$.
2. Solve the outer $l{=}0$ electron as an ABCD cascade through the graded taper (Problem 3), giving $E_{\text{outer}}$.
3. The ionisation energy is $E_{\text{outer}}$ directly (the inner shell remains bound in both the neutral atom and the ion).

The two problems are solved *independently*---the inner-shell energy does not appear in the IE. The coupling between them enters only through the taper profile $\sigma_{1s}(r)$, which is determined by the inner-shell density.

**4. Remaining 3.5% systematic.** The graded taper treats the $1s$ pair as a *passive charge distribution*. In reality, the $1s$ solitons are coupled resonators that can *polarise* in response to the $2s$ soliton's passage. This back-reaction (dynamic polarisation of the $1s$ pair) is a higher-order coupling between Problems 2 and 3:

- The $1s$ pair is a resonant stub on the $2s$ transmission line.
- Its resonant frequency (~245 eV) is far detuned from the $2s$ energy (~5 eV): the frequency ratio $\omega_{2s}/\omega_{1s} = 1/8$.
- The large detuning ensures the stub loading is a small perturbation, consistent with the observed 3.5%.
- The *exact* correction requires solving the coupled 3-soliton problem on the lattice---a multi-body extension of the single-soliton ABCD cascade.

### (E2h) Lattice Fluid Mechanics and the Coupled-Soliton Problem

The radial wave equation, derived from Axioms 1, 2, 4, has a second interpretation via the **Madelung transformation**. Write $\psi = \sqrt{\rho}\; e^{iS/\hbar}$, where $\rho = |\psi|^2$ is the soliton field intensity and $v = \nabla S / m_e$ is the phase-gradient velocity. The wave equation splits into two real equations:

**1. Continuity (charge conservation):**

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho\,\mathbf{v}) = 0
$$

**2. Euler equation (lattice momentum):**

$$
\frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla)\mathbf{v} = -\frac{\nabla V}{m_e} - \frac{\nabla Q}{m_e}
$$

where

$$
Q = -\frac{\hbar^2}{2m_e} \frac{\nabla^2 \sqrt{\rho}}{\sqrt{\rho}}
$$

is the **lattice dispersion pressure**.

**3. Axiom mapping.**

| **Fluid quantity** | **AVE origin** |
|---|---|
| Density $\rho$ | Soliton field $|\psi|^2$ (Axiom 4) |
| Velocity $\mathbf{v}$ | Phase gradient $\nabla S / m_e$ (Axiom 4) |
| Pressure $Q$ | Lattice dispersion (Axiom 1) |
| External force $-\nabla V$ | Coulomb potential (Axiom 2) |
| Vortex | Topological soliton (electron) |

The lattice pressure $Q$ arises from Axiom 1: the discrete vacuum lattice resists compression of the soliton field. It has no counterpart in classical fluid theory---it is the AVE-native term that distinguishes soliton mechanics from ordinary hydrodynamics.

**4. The coupled-soliton problem.** The $N$-electron atom is $N$ coupled vortices in the vacuum lattice fluid. Each vortex creates a $1/r$ flow field (Axiom 2, Coulomb). The nonlinear term $(\mathbf{v} \cdot \nabla)\mathbf{v}$ couples all vortices simultaneously.

The ABCD cascade (E2d-ii, E2f) solves the *linearised* problem: one vortex (the $2s$ soliton) propagates through the static field of the others (the $1s$ taper). The 3.5% systematic is the *nonlinear advection correction*---the back-reaction of the $2s$ flow field on the $1s$ vortices.

**5. Self-consistent iteration.** The steady-state ($\partial/\partial t = 0$) solution is found by iterating the lattice Euler equation:

1. Solve the $1s$ density $\rho_{1s}(r)$ from the ODE.
2. Compute $\sigma_{1s}(r) = \int_0^r \rho_{1s}\,4\pi r'^2\,dr'$ (numerical Gauss integral, Axiom 2).
3. ABCD cascade for the $2s$ soliton with $Z_{\text{net}}(r) = Z - N_a\,\sigma_{1s}(r)$.
4. Extract $\rho_{2s}(r)$ from the $2s$ solution.
5. Update $1s$ potential: $V_{1s}(r) = -Z\,\alpha\hbar c/r + \sigma_{2s}(r)\,\alpha\hbar c/r + \sigma_{1s,\text{other}}(r)\,\alpha\hbar c/r$.
6. Re-solve $1s$ density, re-run ABCD cascade.
7. Iterate until $|\Delta E_{2s}| < 0.001$ eV.

This uses **zero new physics**---the same ODE, the same ABCD cascade, and the same Axiom 2 Coulomb potential. The iteration is the standard technique for solving steady-state fluid equations: update the flow field, re-solve the velocity, repeat.

### (E2i) Op2 Crossing Correction for Penetrating Orbits

The ABCD cascade (E2f) treats the $1s$ pair as a passive charge distribution but ignores the **topological crossing** between the $2s$ soliton and the $1s$ solitons at the shell-penetration radius.

**1. Same-shell reference.** For the $1s$ Hopf-linked pair (E1), Op2 modifies the coupling coefficient: $k_{\text{Hopf}} = (2/Z)(1 - P_C/2)$, where $P_C = 8\pi\alpha$ is the lattice packing fraction (Axiom 3). This Op2 correction accounts for the repulsive topological energy at each crossing of the Hopf link.

**2. Cross-shell l=0 crossings.** The $2s$ soliton ($l{=}0$) oscillates radially through the $1s$ shell. On each radial period it passes through the $1s$ region *twice* (once inward, once outward). Only the **same-phase** $1s$ dipole string contributes a topological crossing (the anti-phase soliton is orthogonal on the lattice and does not cross).

For Li ($1s^2\,2s^1$) with one same-phase inner string:

- Number of same-phase crossings per period: $n_{\text{cross}} = 2$.
- Each crossing carries the same Op2 cost $P_C$ as the Hopf link.

**3. Crossing correction.** The Op2 repulsive energy from the $2s$ soliton crossing one same-phase inner string is:

$$
\delta E_{\text{Op2}} = E_{\text{ABCD}} \times \frac{P_C}{4} = E_{\text{ABCD}} \times 2\pi\alpha
$$

The factor $1/4$ arises from: $P_C/2$ per crossing at a Hopf-link vertex (same as E1), divided by 2 because only one out of two inner strings shares the $2s$ phase.

For Li:

$$
\delta E_{\text{Op2}} = 5.58 \times \frac{8\pi\alpha}{4} = 5.58 \times 0.0459 = 0.256\;\text{eV}
$$

Corrected ionisation energy:

$$
E_{\text{IE}} = E_{\text{ABCD}} - \delta E_{\text{Op2}} = 5.58 - 0.26 = 5.32\;\text{eV}
$$

**Updated result:**

| **Method** | **IE (eV)** | **Error** |
|---|---|---|
| Simple $\sigma$ (Op4 ring) | 2.49 | $-54\%$ |
| ABCD step function | 5.70 | $+5.8\%$ |
| ABCD graded taper | 5.58 | $+3.5\%$ |
| **ABCD taper + Op2 crossing** | **5.32** | $\mathbf{-1.2\%}$ |
| Experiment | 5.39 | --- |

**4. Operator chain.** The complete Li solver uses *all six* universal operators:

- Op1: $Z_{\text{TL}} = \hbar k/m_e$ (impedance per section).
- Op2: $\delta E = E \times P_C/4$ (crossing repulsion at penetration).
- Op3: distributed $\Gamma$ through graded taper.
- Op4: Coulomb $V = -Z_{\text{net}}\alpha\hbar c / r$.
- Op5: ABCD cascade of 20 thin sections.
- Op6: eigenvalue from $B_{\text{total}} = 0$.

Result: IE $= 5.32$ eV vs. 5.39 eV (1.2% error, 0 free parameters, 0 imported numbers).

### (E2j) Same-Shell Interactions as Coupled Transmission Lines

The ABCD cascade (E2d-ii, E2f) models inner-shell screening via Gauss's law: the $1s$ charge distribution reduces the effective nuclear charge seen by the $2s$ soliton. This works because the $1s$ and $2s$ shells are **spatially separated**---the $1s$ density is concentrated at $r \approx a_0/Z$, while the $2s$ orbit extends to $r \approx 4a_0/Z$. Gauss's law applies whenever the charge is enclosed inside a surface.

For electrons in the **same shell** (e.g. the $2s$ and $2p$ orbitals in B, C, N), the situation is fundamentally different: the orbitals *overlap spatially*. One electron is not enclosed inside the other. Gauss screening is the wrong model.

**1. The EE analog: coupled microstrip.** In electrical engineering, when two transmission lines run through the *same* dielectric medium (neither enclosed by the other), they are modelled as **coupled lines** with even and odd mode impedances:

$$
Z_{\rm even} = Z_0 \sqrt{\frac{1+k}{1-k}}, \qquad Z_{\rm odd} = Z_0 \sqrt{\frac{1-k}{1+k}}
$$

where $k$ is the mutual coupling coefficient from electromagnetic field overlap. The key property: neither line "screens" the other --- both lines experience a *modified impedance* due to the presence of the other.

This is a standard, well-understood formalism. It appears at three scales in the AVE framework:

| **Scale** | **Coupled lines** | **Coupling source** |
|---|---|---|
| Atom | $2s + 2p$ in same shell | Coulomb overlap integral |
| Protein | $\beta$-sheet strands | H-bond mutual admittance |
| Antenna | Coupled microstrip | Fringe-field capacitance |

The protein engine already uses coupled-line even/odd impedances for $\beta$-sheet inter-strand coupling (Vol. V). The atomic instantiation is identical: two electron orbitals running through the same nuclear field are coupled by mutual Coulomb repulsion.

**2. Same-shell coupling coefficient.** The coupling between two electrons in the same shell (at radius $R_n = n^2 a_0 / Z$) but different angular momentum states follows from Op4:

$$
k_{\rm same} = \frac{V_{\rm rep}}{E_0} = \frac{\alpha\hbar c \; / \; \langle r_{12} \rangle}{Z_{\rm eff}^2 \, R_y \, / \, n^2}
$$

where $\langle r_{12} \rangle$ is the mean inter-electron distance on the shell (Axiom 2, Coulomb integral) and $Z_{\rm eff}$ is the effective charge after cross-shell screening.

For same-$n$, different-$l$ orbitals (e.g. $2s + 2p$ in B): the overlap integral is *partial* --- the $2s$ density is spherically symmetric while the $2p$ density is axially concentrated. The coupling is therefore **weaker** than for same-$l$ same-$n$ pairs (the Hopf-link case).

**3. Why Gauss fails for same-shell.** If one naively models $2s^2$ as a Gauss screen for the $2p$ electron (assigning $N_{\rm inner} = 4$ instead of $N_{\rm inner} = 2$ in the ABCD cascade), the ionisation energy is grossly wrong:

| **B screening model** | $N_{\rm inner}$ | **IE (eV)** | **Error** |
|---|---|---|---|
| 1s$^2$ only | 2 | 32.4 | $+291\%$ |
| 1s$^2$ + 2s$^2$ (Gauss) | 4 | 3.5 | $-58\%$ |
| Experiment | --- | 8.30 | --- |

Screening by $1s^2$ alone under-screens (too much charge visible); adding $2s^2$ as Gauss over-screens (too little charge visible). The true answer lies between the two extremes, because $2s$ and $2p$ **partially overlap** --- neither limit is physical.

The coupled-line formalism resolves this: $2s$ and $2p$ are not screened from each other; they shift each other's effective impedance through mutual coupling, and the correct eigenvalue emerges from the coupled-mode splitting, not from an effective nuclear charge.

**4. Multi-atom solver architecture.** The complete solver for atoms $Z \geq 3$ requires three components, each from a different universal operator:

1. **ABCD cascade (P3):** Cross-shell screening from inner shells via the discrete Gauss step $Z_{\rm net}(r) = Z - N_{\rm inner}$. Uses Op1, Op3--Op6.
2. **Coupled-line splitting (P2):** Same-shell interactions via even/odd mode impedances. Uses Op3, Op5, Op6.
3. **Op2 crossing correction:** Topological penalty at shell-penetration crossings ($l{=}0$ only), giving $\delta E = E \times P_C/4$.

Each component is domain-agnostic (the same operators appear in protein folding and antenna design). No effective charges, no screening constants, no fitted parameters.

**5. Current validation.**

| **Atom** | $Z$ | **Method** | **IE (eV)** | **Error** |
|---|---|---|---|---|
| H | 1 | P1 (exact hydrogenic) | 13.61 | $0.1\%$ |
| He | 2 | P2 (circuit, Hopf link) | 24.37 | $0.9\%$ |
| Li | 3 | P3 + Op2 (ABCD taper) | 5.32 | $1.2\%$ |
| Be | 4 | P3 + P2 (ABCD + Hopf) | 8.21 | $11.9\%$ |
| B | 5 | P3 + coupled-line | *not yet implemented* | |

H, He, and Li each test *one* component in isolation and pass at $< 1.5\%$. Be and B remain open: the corrections are applied *outside* the phase integral, violating the action principle.

### (E2k) Complete Phase Integral: All Operators Inside $V(r)$

The fundamental problem with E2d--E2j is architectural: the ABCD cascade finds the eigenvalue from a phase integral $\oint k(r)\,dr = n\pi$, but Op2 crossings and same-shell coupling are applied *after* the eigenvalue as multiplicative corrections. These corrections change the energy but do not enter the potential $V(r)$ that determines $k(r)$. The soliton's action does not minimise through them.

In AVE, the ground state is the configuration where the phase integral exactly satisfies the standing-wave condition ($B_{\text{total}} = 0$, Op6). **Every** interaction that changes the soliton's energy must appear inside $V(r)$, so that the phase integral accounts for it.

**1. Operator decomposition of electron-electron interactions.** Every interaction between solitons maps to a specific universal operator, lattice mechanism, and entry point in the cascade. Three channels are involved, each at a distinct scale:

| **Interaction** | **Op** | **EE Analog** | **Scale** | **Enters cascade as** |
|---|---|---|---|---|
| Nuclear Coulomb | Op1 | Voltage source | All | $V = -Z\alpha\hbar c/r$ |
| Enclosed-charge screening (all shells, incl. same-$n$) | Op3 | Mutual capacitance $C_m$ | Orbital | $+N_k\sigma_k(r)\alpha\hbar c/r$ |
| Hopf link back-EMF (same-$l$ partners) | Op7+Op9 | Mutual inductance $M$ | Knot$\to$Orbital | Modify $k(r)$ at $R_n$ |
| Flux tube crossing ($I \neq 0$ only) | Op2+Op4 | Junction shunt $Y$ | Knot | $\delta(r{-}r_{\times})\times V_0$ |
| Centrifugal barrier | Op1 | Reactive impedance | Orbital | $+l(l{+}1)\hbar^2/(2m_e r^2)$ |
| Pauli exclusion | Op2 | Open circuit $\Gamma{=}{-}1$ | Knot | Constraint (not energy) |

**Key distinction:** The Gauss CDF $\sigma_k(r)$ and the Hopf link back-EMF are *independent* interactions at different scales. The CDF modifies the *potential* $V(r)$ (capacitive, orbital scale, Regime I linear). The Hopf link modifies the *propagation constant* $k(r)$ (inductive, knot scale projected to orbital, Regime II nonlinear). In the lumped regime (He), these combine into a single coupling coefficient $k_{\text{pair}}$; in the distributed regime ($Z \geq 3$), they must be separated.

**Linking vs. crossing.** Two same-$l$ solitons (identical winding numbers) have intersection number $I = 0$---they do not cross on the torus surface. Instead they form a *Hopf link*: each flux tube threads through the other's poloidal loop. This topological linking creates mutual inductance $M$ (Op7, back-EMF), not a crossing potential $V_{\rm cross}$ (Op2+Op4). Two different-$l$ solitons (e.g. $2s$--$2p$, $I = 2$) *do* cross on the surface, creating localised $V_{\rm cross}$ shunts.

**2. Complete effective potential and propagation constant.** The cascade eigenvalue is $B_{\rm total}(E) = 0$ (Op6), where $k(r)$ includes *all* interactions:

$$
\boxed{k^2(r) = \frac{2 m_e}{\hbar^2}\;\frac{E - V_{\rm eff}(r)}{1 + \kappa_{\rm Hopf}(r)}}
$$

with

$$
\boxed{V_{\rm eff}(r) = \underbrace{-\frac{Z\,\alpha\hbar c}{r}}_{\text{nuclear (Ax. 2)}} + \underbrace{\sum_k \frac{N_k\,\sigma_k(r)\,\alpha\hbar c}{r}}_{\text{screening (Op3, all shells)}} + \underbrace{V_{\rm cross}(r)}_{\text{crossings (Op2+Op4)}} + \underbrace{\frac{l(l+1)\hbar^2}{2 m_e r^2}}_{\text{angular (Op1)}}}
$$

and the Hopf link back-EMF coupling:

$$
\kappa_{\rm Hopf}(r) = N_{\rm Hopf} \times \frac{P_C}{2} \times \sigma_{\rm partner}(r)
$$

where $N_{\rm Hopf}$ is the number of same-$l$ Hopf-linked partners, $P_C/2$ is the Op2 saturation at the linking point (Axiom 4), and $\sigma_{\rm partner}(r)$ is the partner's enclosed-charge fraction (the same CDF used for screening, but here governing the spatial extent of the inductive coupling).

Each term:

- **Nuclear Coulomb** (Axiom 2): bare charge $Z$, exact $1/r$.
- **Enclosed-charge screening** (Op3): one term per shell $k$ (including same-$n$ co-radial partners), with $N_k$ solitons and enclosed-charge fraction $\sigma_k(r)$ computed from the standing-wave density of shell $k$.
- **Crossing potential** (Op2+Op4): a localised repulsive $\delta$-function at each radius where the outer soliton's flux tube crosses another soliton's flux tube (intersection number $I \neq 0$).
- **Hopf link back-EMF** (Op7+Op9): mutual inductance between linked flux tubes, modifying the wave's propagation constant. This is *not* a potential in $V_{\rm eff}$---it enters the *denominator* of $k^2(r)$.
- **Centrifugal barrier** (Op1): angular standing-wave condition.

**2. Layered screening densities.** The enclosed-charge fraction $\sigma_k(r)$ must use the effective charge *seen by shell $k$*, not bare $Z$. Each shell is screened by all shells inside it:

$$
Z_{\rm eff}^{(k)} = Z - \sum_{j < k} N_j
$$

For Li ($1s^2\,2s^1$): the $1s$ pair sees bare $Z = 3$; the $2s$ sees $Z_{\rm eff} = 3 - 2 = 1$. This is not iteration---it is Gauss's law applied sequentially, inside-out. The result is exact for complete inner shells.

For B ($1s^2\,2s^2\,2p^1$): the $2s$ pair sees $Z_{\rm eff}^{(2s)} = 5 - 2 = 3$. Their standing-wave density $\sigma_{2s}(r)$ is therefore more diffuse than at bare $Z = 5$, providing stronger screening of the $2p$ at intermediate radii.

**3. Torus knot crossing geometry.** Each soliton is a torus knot with winding numbers $(p, q)$ on the torus of major radius $R = r_n$ and tube radius $a = \ell_{\rm node}$:

| **Mode** | $l$ | $(p, q)$ | **Description** |
|---|---|---|---|
| $ns$ | 0 | $(n, 0)$ | Poloidal (radial) |
| $np$ | 1 | $(n, 1)$ | Toroidal + poloidal |
| $nd$ | 2 | $(n, 2)$ | 2 toroidal wraps |

Two solitons with winding numbers $(p_1, q_1)$ and $(p_2, q_2)$ on the *same* torus have intersection number:

$$
I = |p_1 q_2 - p_2 q_1|
$$

This is a topological invariant: it counts the number of crossings on the torus surface.

For $2s$--$2p$: $I = |2 \times 1 - 0 \times 2| = 2$. Two crossings---the same count as the Hopf link ($1s$--$1s$).

**4. Crossing angle from torus geometry.** The tangent vectors of the two curves at a crossing determine the flux-tube angle $\theta$. On a torus with aspect ratio $\mathcal{R} \equiv R/a = n^2/(Z\alpha)$:

$$
\cos\theta = \frac{p_1 p_2 + q_1 q_2\,\mathcal{R}^2}{\sqrt{p_1^2 + q_1^2\,\mathcal{R}^2}\;\sqrt{p_2^2 + q_2^2\,\mathcal{R}^2}}
$$

For $2s$--$2p$ in B ($Z = 5$, $n = 2$): $\mathcal{R} = 4/(5\alpha) \approx 110$, giving $\cos\theta \approx 0.018$, $\theta \approx 89^\circ$. The crossings are orthogonal because $\mathcal{R} \gg 1$ (the torus is very thin at atomic scales).

**5. Crossing potential.** At each crossing, the total strain is (Axiom 4):

$$
A_{\rm total}^2 = A_1^2 + A_2^2 + 2 A_1 A_2 \cos\theta
$$

For identical solitons ($A_1 = A_2 = A$):

- Parallel ($\theta = 0$): $A^2 = 4A^2$ (Hopf link, $1s$-$1s$).
- Orthogonal ($\theta = 90^\circ$): $A^2 = 2A^2$ (half the parallel cost).
- Antiparallel ($\theta = 180^\circ$): $A^2 = 0$ (healed---Pauli exclusion).

The Op2 energy at each crossing is $\delta E = E \times P_C / c_{\rm link}$, where $c_{\rm link}$ is the crossing number of the link. For orthogonal crossings the cost is halved relative to parallel:

$$
V_{\rm cross}(r) = \sum_{\text{crossings}} \frac{P_C}{2c} \times \frac{\alpha\hbar c}{r_{\rm cross}} \times \delta(r - r_{\rm cross})
$$

The $\delta$-function maps directly to a lumped shunt admittance $Y = -2m_e V_0/\hbar^2$ in the ABCD cascade, requiring no spatial smearing. This is the EE-native representation: a point coupling between two transmission lines is a lumped reactive element, not a distributed perturbation.

**6. Crossing radius.** Where does the crossing occur? The intersection of the $(n,0)$ and $(n,1)$ curves on the torus occurs at the poloidal angle where the toroidal curve crosses the poloidal circle. In the radial coordinate, this maps to:

$$
r_{\rm cross} = R_n = \frac{n^2 a_0}{Z_{\rm eff}}
$$

where $R_n$ is the Bohr radius of shell $n$ at the effective charge seen by that shell. The crossing is localised at the orbital radius---exactly where the two solitons share the same mean distance from the nucleus.

**7. Phase integral with complete $V(r)$.** The ABCD cascade (E2f) integrates the radial ODE through the potential. The eigenvalue condition $B_{\text{total}} = 0$ (Op6) gives the energy $E$ at which the total accumulated phase equals $n\pi$. No post-hoc corrections are needed: every interaction---nuclear, screening, crossing, angular---is inside the phase integral.

The soliton's action minimises naturally through the eigenvalue condition.

> **[Resultbox]** *Approach 24: Complete Phase Integral*
>
> All universal operators enter the effective potential $V_{\rm eff}(r)$ directly. The ABCD cascade computes the eigenvalue in one pass. Screening is layered ($Z_{\rm eff}^{(k)} = Z - \sum_{j<k} N_j$). Crossing potentials are localised at $r = R_n$ with magnitudes from Axiom 4 and crossing angles from torus knot geometry. No correction factors. One phase integral. One eigenvalue.

---
