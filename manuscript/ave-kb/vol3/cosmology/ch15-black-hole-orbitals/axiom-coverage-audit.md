[↑ Ch.15 Black Hole Orbitals](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-395gps]
-->

## Axiom Coverage Audit

The following table records which AVE axioms are fully exercised in the current black hole orbital model, and which require deeper integration:

| **Axiom** | **Statement** | **Status** | **Coverage** |
|---|---|---|---|
| 1 | LC lattice, $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ | **Full** | Symmetric Gravity ($Z = Z_0$) |
| 2 | Topological defects (self-trapped $\gamma$) | **Full** | BH-electron isomorphism |
| 3 | Gravity = dielectric strain $n(r)$ | **Full** | Kerr saturation boundary, QPOs |
| 4 | Saturation ($V_{SNAP}$, viscosity) | **Full** | Phase transition, $Q = \ell$ (cold $a_*=0$ anchor — B1), $\tau_{ring}$ |

### Axiom 4 Saturation: Phase Transition and $Q = \ell$

At the saturation boundary ($\varepsilon_{11} = 1$), the lattice undergoes a **solid $\to$ fluid phase transition**. The shear modulus $G_{shear} \to 0$, eliminating transverse wave propagation in the interior. Gravitational waves, being transverse shear perturbations of the LC lattice, are **perfectly reflected** at this phase boundary.

The quality factor follows from the topological mode structure: with $\ell$ wavelengths fitting around the circumference, each releases $\sim 1/\ell$ of the mode energy per cycle via curvature radiation:

> **[Resultbox]** *QNM Quality Factor from Lattice Phase Transition*
>
> $$
> Q = \ell, \qquad \omega_I = \frac{\omega_R}{2\ell} = \frac{9}{98}\,\frac{c}{M_g}
> $$

For $\ell = 2$: $Q = 2$, $\omega_I M = 9/98 = 0.0918$ (GR exact: $0.0890$, error $3.2\%$).

> **🟩 SPIN-SCOPE — this $Q = \ell$ is the cold $a_* = 0$ anchor (Grant Ruling B1, 2026-07-21; propagated
> 2026-07-31).** $\ell$ is an integer **mode count** — cavity-deformable (def-quant3 sense (1),
> `common/vocabulary-register.md:261` (def-quant3), sense (1) at `:271`, *"Failure mode: ionization destroys them"*), **not** a
> deformation-invariant winding. **The discriminator is its INTEGRALITY, not its sense class:** an integer
> cannot drift continuously with strain — it can only jump discretely — while
> the physical $Q = \omega_R/2\omega_I$ is an impedance ratio that moves *continuously* with the strain
> profile. An integer that can only jump cannot track a ratio that moves smoothly: the equality is a
> **zero-spin coincidence, not a law**, and the banked $\bar D_Q = -38\%$ at catalog spins is what that
> looks like (corrected-Kerr $Q$ rises $3.07 \to 3.49$). The spin story is the
> m$\Omega$ law $\omega_I = (\omega_R - m\Omega)/(2\ell)$
> ([`ave-merger-ringdown-eigenvalue.md` § Kerr Quality Factor](ave-merger-ringdown-eigenvalue.md)); flat
> $Q = \ell$ is its $\Omega \to 0$ limit. *(Physical reading = orchestrator-walk provenance 2026-07-31, not
> canon.)* Model banner: [`vol3/claim-quality.md`](../../claim-quality.md) `clm-395gps` at `:204`; scoping doc
> `research/2026-07-30_qlaw-derivation_scoping.md` §1.5. Chapter-canonical scope banner:
> [`qnm-quality-factor.md`](qnm-quality-factor.md).
>
> **[#808 scoping F7/F8 — OPEN FLAG, not a ruling; B1 did not adjudicate this.]** Even the cold value is
> convention: the $1/\ell$-per-cycle leak constant is a *scaling assertion* set to 1 by the
> $2\pi$-divides-out convention, never a computed radiated power. The cold-$Q$ derivation is the named
> next work. Source `research/2026-07-30_qlaw-derivation_scoping.md` §1.5 — surfaced, unadjudicated.

This is the gravitational-scale manifestation of the **knot crossing number $\leftrightarrow$ mode number** isomorphism: the crossing number $c$ at the particle scale (confinement radius $r = \kappa/c$) plays the identical role to the angular mode number $\ell$ at the gravitational scale ($Q = \ell$). Each additional topological winding adds one unit of confinement stability.

Comparison against three LIGO events:

| **Event** | $a_*$ | $Q$ | $\tau$ AVE [ms] | $\tau$ obs [ms] | Error |
|---|---|---|---|---|---|
| GW150914 | 0.67 | 2 | 2.3 | 4.0 | 43% |
| GW170104 | 0.64 | 2 | 1.9 | 3.0 | 38% |
| GW190521 | 0.72 | 2 | 5.0 | 15.0 | $\dagger$ |

The Schwarzschild $Q = \ell = 2$ is used for all events; the Kerr correction to $Q$ (which increases Q for spinning remnants) is not yet included and accounts for the remaining $\tau$ discrepancy.

> **🟩 SPIN-SCOPE — the table above applies the cold $a_* = 0$ anchor *outside its scope* (Ruling B1,
> 2026-07-21; propagated 2026-07-31; the table itself is preserved per Rule 12).** All three events sit at
> $a_* = 0.64$–$0.72$, so the flat $Q = \ell = 2$ column is the cold anchor read through at catalog spins —
> exactly the reading B1 scoped out, and the 38–43% $\tau$ errors are its signature (banked on the
> frame-independent comparator as $\bar D_Q = -38\%$; corrected-Kerr $Q$ rises $3.07 \to 3.49$). The
> "not yet included" clause is a **scoping lag**: under B1 the standing spin story is the m$\Omega$ law
> $\omega_I = (\omega_R - m\Omega)/(2\ell)$, which is computed and banked at $-5.44\%$ (Resultbox) /
> $-4.57\%$ (ZAMO) — an OPEN near-miss tension, the named next ringdown work, not an un-attempted correction.
> **Nothing here is re-adjudicated** — the numbers above stay as the record. Model banner:
> [`vol3/claim-quality.md`](../../claim-quality.md) `:204`; Q-LAW COMMITMENT:
> [`ave-merger-ringdown-eigenvalue.md` § GRANT RULING B1](ave-merger-ringdown-eigenvalue.md); receipts
> `research/2026-07-20_v1-spin-mapping-adjudication_result.md`.

---
