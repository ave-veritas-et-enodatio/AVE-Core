[↑ Ch.15 Black Hole Orbitals](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "channel-scoped astrophysical assignment closing vocab-audit §4(b) AMBIGUOUS gap — renders existing engine-scale Z_bulk statements at r_sat; no new physics primitive"
-->

## Bulk-Longitudinal Impedance at the Saturation Boundary

The three-impedance law (field-symbol registry §3.11; vocab-operator-unification audit §4a) assigns every reflection statement a **channel subscript**. At an astrophysical black-hole saturation boundary, the bulk-longitudinal row was **engine-scale only** until this leaf: the snap-state machine, coax-ring closure, and sonic-horizon runs state `Z_bulk = \rho\,c_{bulk} \to 0` at rupture, but no vol3 cosmology/gravity leaf had written the astrophysical assignment at $r_{\text{sat}}$.

This leaf closes that gap. It **renders** the existing bulk channel at the AVE saturation radius $r_{\text{sat}} = 7GM/c^2$; it introduces no new EOS, no new operator, and no new free parameter.

### The bulk impedance law

At the K/G = 2 operating point ($K_{bulk} = 2G_{vac}$), the bulk-longitudinal acoustic impedance is:

> **[Resultbox]** *Bulk-longitudinal impedance*
>
> $$
> Z_{bulk} = \rho_{bulk}\,c_{bulk}
> $$

with $\rho_{bulk}$ and $G_{vac} = \rho_{bulk}\,c_0^2$ from `constants.py`, and $c_{bulk}$ the bulk dilatational speed (canonical three-speed split: $c_{bulk}$ freezes at the cavitation floor; at dielectric rupture $c_{bulk} \to 0$).

### Assignment at $r_{\text{sat}}$

At the saturation boundary where $\varepsilon_{11}(r_{\text{sat}}) = 1$ ([`ave-bh-horizon-area-theorem.md`](ave-bh-horizon-area-theorem.md)), the lattice undergoes the same phase transition documented in [`electron-bh-isomorphism.md`](electron-bh-isomorphism.md):

- $G_{shear} \to 0$ (shear modulus vanishes)
- $c_{bulk} \to 0$ (bulk dilatational speed vanishes at snap / rupture)
- Therefore $Z_{bulk} = \rho_{bulk}\,c_{bulk} \to 0$

By Op3 at the bulk port:

> **[Resultbox]** *Bulk reflection at the saturation boundary*
>
> $$
> \Gamma_{bulk} = \frac{Z_{bulk,2} - Z_{bulk,1}}{Z_{bulk,2} + Z_{bulk,1}} \to -1 \quad \text{as } Z_{bulk} \to 0
> $$

The saturated interior is a **bulk-longitudinal perfect reflector** — the sonic-horizon / pressure-release boundary ($p = 0$ at the wall) identified in the sonic-horizon closure and coax-ring derivations.

### Three channels, one boundary

The "three-valued boundary" (vocab-operator-unification audit §4d, 2026-06-11) is three **channel views** of the **same** physical surface at $r_{\text{sat}}$:

| Channel | Impedance | $\Gamma$ at $r_{\text{sat}}$ | Mechanism |
|---|---|---|---|
| EM-transverse $Z_{EM} \equiv Z_0$ | $\sqrt{\mu/\varepsilon}$ invariant under SYM scaling | $\Gamma_{EM} = 0$ | Symmetric gravity: $\mu$ and $\varepsilon$ scale together ([`electron-bh-isomorphism.md`](electron-bh-isomorphism.md) §Symmetric Gravity) |
| Shear $Z_{shear} = \rho\,c_{shear}$ | $G_{shear} \to 0$ | $\Gamma_{shear} = -1$ | Phase transition eliminates shear restoring force; $c_{shear} \to 0$ |
| Bulk $Z_{bulk} = \rho\,c_{bulk}$ | Snap / rupture | $\Gamma_{bulk} = -1$ | $c_{bulk} \to 0$ at dielectric rupture (this leaf) |

**BH-echo yes/no is therefore a channel question.** EM-channel: transparent ($\Gamma_{EM} = 0$, no converged WKB echo under SYM scaling). Shear/bulk channels: reflecting ($\Gamma = -1$). Statements that "the horizon is a perfect absorber" (EM) and "the horizon reflects shear/GW modes" are **not contradictory** once channel subscripts are explicit.

### Engine-scale anchors (pre-existing)

| Anchor | Statement |
|---|---|
| Field-symbol registry §3.11 | $Z_{bulk}$ bulk-longitudinal row; $Z_0 \equiv Z_{EM}$ only |
| `registry:197` / snap state machine | $Z_{bulk} = \rho c \to 0$ at snap |
| `bubble-physics:107` | $\Gamma = -1$ shell = impedance collapse $Z_{bulk} \to 0$ |
| `sonic-horizon-closure_result.md` §7 | $c^2 = 0$ locus $\Rightarrow$ $Z_{bulk} \to 0$ pressure-release reflector |
| `coax-ring-secondary_result.md` Block 2 | Radial $Z_{bulk}$ vanishes at inner radius |

### Comparison table (updated)

| **Property** | **Electron** | **Black Hole at $r_{\text{sat}}$** |
|---|---|---|
| Confinement boundary | $\ell_{node}$ | $r_{\text{sat}} = 7GM/c^2$ |
| EM channel | $Z_{EM} = Z_0$ (matched vacuum); confinement is **not** EM-short | $Z_{EM} = Z_0$ (SYM) $\Rightarrow \Gamma_{EM} = 0$ |
| Shear channel | — | $Z_{shear} \to 0$ $\Rightarrow \Gamma_{shear} = -1$ |
| Bulk channel | $Z_{bulk} \to 0$ at TIR wall $\Rightarrow \Gamma_{bulk} = -1$ | $Z_{bulk} \to 0$ at rupture $\Rightarrow \Gamma_{bulk} = -1$ |
| Interior physics | Constructive (topology preserved) | Destructive (topology melts) |

> ↗ See also: [`electron-bh-isomorphism.md`](electron-bh-isomorphism.md) — shear phase transition (updated with $\Gamma_{shear}$); [`ave-bh-horizon-area-theorem.md`](ave-bh-horizon-area-theorem.md) — $r_{\text{sat}}$ derivation; [`substrate-hysteresis-index.md`](../../../common/substrate-hysteresis-index.md) §5b — LOOP GAP vs $\Omega_{\text{freeze}}$ (engine memory vs remanence).

### Discipline audit (2026-06-12)

| Skill | Pass |
|---|---|
| `verify-before-cite` | Channel assignments grep-verified against [`electron-bh-isomorphism.md`](electron-bh-isomorphism.md):35–45; $Z_{bulk}=\rho c_{bulk}$ at `constants.py`:646–658 |
| `consistency-vs-emergence` | **Class B** render — no new primitive; closes vocab-audit §4(b) gap only |
| `ave-dimensional-provenance-check` | $Z_{bulk}$ is bulk-channel impedance ($\rho\times$ speed), not a dimensionless coupling |

---
