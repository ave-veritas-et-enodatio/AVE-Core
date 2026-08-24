[↑ Ch. 10: Three Open Problems from Lattice Topology](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-gfs4j8]
-->

## The Strong CP Problem

### The Problem

The QCD Lagrangian contains a CP-violating term:

$$
\mathcal{L}_\theta = \frac{\theta\, g^2}{32\pi^2}\, F^a_{\mu\nu} \tilde{F}^{a,\mu\nu}
$$

Any $\theta \ne 0$ gives the neutron an electric dipole moment $d_n \propto \theta$. The experimental bound $|d_n| < 10^{-26}$ e$\cdot$cm implies $|\theta| < 10^{-10}$.

**Why is $\theta$ so small?** Standard QCD allows any $\theta \in [0, 2\pi)$. The Peccei-Quinn solution posits a new symmetry and predicts the axion --- a particle not yet observed.

### AVE Resolution: Topological Quantization

**Theorem (Strong CP):** On the AVE lattice, the vacuum angle $\theta = 0$ exactly. No axion is needed.

**Proof.**

1. The AVE vacuum is the *unique* ground state with $\mathbf{E}_n = \mathbf{B}_n = 0$ for all lattice nodes $n$. This state has zero topological charge: $Q_{top} = 0$.
2. The vacuum angle $\theta$ parameterizes superpositions of topologically distinct vacua. In QCD, these are the $|\nu\rangle$ states related by large gauge transformations.
3. In AVE, the gauge structure emerges from $(2,q)$ torus knots (Section [Section Removed]). Each torus knot has quantized phase winding $\Phi = q\pi$.
4. A transition between topologically distinct vacua requires creating a topological defect, which costs energy $E \ge \Delta > 0$ (the mass gap).
5. Therefore, the vacuum cannot tunnel between $\theta$-sectors: the barrier is the mass gap itself. The ground state is $|\theta = 0\rangle$ with probability 1. $\square$

### Comparison with Peccei-Quinn

| **Feature** | **Peccei-Quinn** | **AVE** |
|---|---|---|
| Mechanism | New U(1)$_{PQ}$ symmetry | Unique vacuum topology |
| New particle | Axion (unobserved) | None |
| $\theta$ | Dynamically relaxed to 0 | Exactly 0 (ground state) |
| Free parameters | $f_a$ (axion scale) | Zero |

---

> 🔴 **Dated scope carve 2026-08-23 (θ-fork adjudication, Grant rulings (a)+(b); docket
> `2026-08-23-theta-fork-ruling`). Body above preserved unedited (Rule 12).**
>
> 1. **Scope: the θ of this theorem is the GLOBAL vacuum angle** — the angle of the
>    defect-free, asymptotic ground state (proof step 1's E=B=0 state). The corpus also
>    carries a **distinct** θ-labeled object: the discrete dressing values
>    θ ∈ {0, ±2π/3, ±4π/3} inside the baryon Borromean cage
>    (`../../particle-physics/ch02-baryon-sector/topological-fractionalization.md`), which
>    per the Grant-ratified 2026-06-23 reconciliation (clm-w8jn3q) is the body-angular-momentum
>    𝒥-dressing of the integer charge — not a state of the vacuum, and not the object this
>    theorem constrains. The two share a symbol only; see the symbol-collision warning at the
>    clm-gfs4j8 register entry. This theorem is untouched by the cage-interior object — and,
>    conversely, offers it no protection or threat: the same mass-gap barrier the proof
>    invokes (step 4) is what pins any topologically-trapped state, global or local.
> 2. **Dead cross-reference on record:** proof step 3 cites "(Section [Section Removed])" —
>    a removed section, uncorrected since import. The (2,q)-torus-knot gauge-structure claim
>    it points at is carried today by the **Axiom-2 (TKI)** operational signatures per
>    INVARIANT-S2 — "(2,q) torus knot" is an Ax-2 signature, not Ax-1; the register's own
>    depends-on line ("Axiom 1 (gauge structure from (2,q) torus knots…)") is itself suspect
>    against that split. The claim is also carried by the
>    ch12 Yang-Mills leaves (framework-conditional per their own scope corrections). The dead
>    pointer is flagged, not silently rewritten.
> 3. Standing weaknesses restated from the register (unchanged by this note): step-1
>    uniqueness is asserted-not-proven (clm-gfs4j8, solidity 0.50 input-only) and the
>    closure-roadmap carries a kb_audit circularity flag on the proof's shape.
