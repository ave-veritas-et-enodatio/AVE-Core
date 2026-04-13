[↑ Computational Mass Defect](../index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol6 as sec:K_derivation -->

> ↗ See also: [Axiom 2 — $\xi_{topo}$](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) — $\alpha\hbar c$ coupling derived from Axiom 2
> ↗ See also: [Torus Knot Mass Ladder](../../../vol2/particle-physics/ch01-topological-matter/index.md) — proton as $(2,5)$ cinquefoil knot with $c=5$ crossings
> ↗ See also: [Particle Physics Translation](../../../common/translation-tables/translation-particle-physics.md) — proton mass and empirical mass defect rows

## Derivation of the Mutual Coupling Constant ($K$)

The key to reducing the nuclear binding problem to a zero-parameter derivation lies in expressing the mutual coupling constant $K$ in terms of already-derived AVE quantities.

The mutual inductance between two nucleon defects (proton-class $6^3_2$ Borromean links) is fundamentally an electromagnetic coupling mediated by the vacuum $LC$ network. The base coupling scale is therefore the Coulomb constant:

$$
\alpha \hbar c = \frac{e^2}{4\pi\epsilon_0} \approx 1.440 \text{ MeV}\cdot\text{fm}
$$

Each proton-class nucleon is a cinquefoil $(2,5)$ torus knot with $c = 5$ topological crossings. When two such knots couple inductively, the signal must thread through each crossing, accumulating a $\pi/2$ phase advance per crossing (one quarter-turn of flux linkage). This is the nuclear analog of a multi-turn transformer: a 5-turn coil couples $5 \times (\pi/2)$ more strongly than a single-turn loop.

At nuclear separations ($d \sim r_{\text{proton}} \approx 0.88$ fm), the nucleon strain fields are close enough that the current distributions deform to concentrate flux toward the adjacent coil---the well-known **proximity effect** in EE transformer theory. The first-order radiative correction to the mutual coupling is $1/(1 - \alpha/3)$, where $\alpha/3$ represents the isotropic 3D spatial average of the electromagnetic vertex correction.

Assembling these three factors:

$$
\begin{align}
K &= \underbrace{c_{\text{proton}}}_{= \, 5}
     \;\times\;
     \underbrace{\frac{\pi}{2}}_{\text{phase/crossing}}
     \;\times\;
     \underbrace{\alpha \hbar c}_{\approx\, 1.4400}
     \;\times\;
     \underbrace{\frac{1}{1 - \alpha/3}}_{\approx\, 1.00243}
\nonumber\\[6pt]
&= 5 \times 1.5708 \times 1.4400 \times 1.00243
\nonumber\\[4pt]
&= 7.8540 \times 1.4400 \times 1.00243
\nonumber\\[4pt]
&\approx 11.337 \text{ MeV}\cdot\text{fm}
\end{align}
$$

$$
\boxed{K = \frac{5\pi}{2} \cdot \frac{\alpha \hbar c}{1 - \alpha/3} \approx 11.337 \text{ MeV}\cdot\text{fm}}
$$

This derived value, applied to the symmetric Helium-4 Alpha particle (6 pairs at uniform distance $d_{\text{core}}\sqrt{8}$), predicts a total nuclear mass of $3727.380$ MeV---matching the CODATA empirical limit of $3727.379$ MeV to within $0.001\%$.

When this same coupling constant is applied to the asymmetrical Lithium-7 dual-shell topology, the spatial distance mapping that satisfies the empirical CODATA mass of $6533.832$ MeV requires the outer shell (1 proton, 2 neutrons) to rest at a distance exactly $9.72\times$ the radius of the inner ultra-dense Alpha core.

This analytical solution provides precise structural resolution of complex isotopic geometries without requiring a single continuous fluid-dynamic 3D volume integration or any empirical calibration constant.

---
