[↑ Ch.6 Universal Operators](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-gdd70j]
path-stable: "referenced from vol1 as sec:universal_eigenvalue"
-->

## Section 6.6: The Universal Eigenvalue Target

The ground state of any impedance network is the configuration where at least one mode is perfectly absorbed:

> **[Resultbox]** *Eigenvalue Target*
>
> <!-- eq:eigenvalue_target -->
>
> $$
> \lambda_{\min}\bigl(S^\dagger S\bigr) \to 0
> $$

When $\lambda_{\min} = 0$, the network has found an eigenstate---a zero singular value of $[S]$ means one mode passes through the system with no reflection.

Code path: `universal_operators.universal_eigenvalue_target(S)`.

---
