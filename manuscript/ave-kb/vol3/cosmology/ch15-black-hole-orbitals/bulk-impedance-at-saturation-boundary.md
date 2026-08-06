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

### Four channels, one boundary

The boundary is **four channel views** of the **same** physical surface at $r_{\text{sat}}$. It was tabulated with three rows until 2026-08-05; the historical name *"three-valued boundary"* (vocab-operator-unification audit §4d, 2026-06-11) is preserved as a **quotation of that audit**, not as a live count. Row 4 is the Cosserat micro-rotation channel, and it is the row on which this surface is **not** a wall:

| Channel | Impedance | $\Gamma$ at $r_{\text{sat}}$ | Mechanism |
|---|---|---|---|
| EM-transverse $Z_{EM} \equiv Z_0$ | $\sqrt{\mu/\varepsilon}$ invariant under SYM scaling | $\Gamma_{EM} = 0$ | Symmetric gravity: $\mu$ and $\varepsilon$ scale together ([`electron-bh-isomorphism.md`](electron-bh-isomorphism.md) §Symmetric Gravity) |
| Shear $Z_{shear} = \rho\,c_{shear}$ | $G_{shear} \to 0$ | $\Gamma_{shear} = -1$ | Phase transition eliminates shear restoring force; $c_{shear} \to 0$ |
| Bulk $Z_{bulk} = \rho\,c_{bulk}$ | Snap / rupture | $\Gamma_{bulk} = -1$ | $c_{bulk} \to 0$ at dielectric rupture (this leaf) |
| **Cosserat micro-rotation / wryness** (couple-stress; the $(2,3)$ winding) — [`port-register.md`](../../../common/port-register.md) channel 4 | couple-stress transport $\gamma\,S_\kappa$ | **NO WALL AT $r_{\text{sat}}$** — the channel is *unwalled* here; its own wall is a $\kappa$-**amplitude** surface | **Transport SURVIVES the wall.** The DC bias here is a *strain* grading and it does not load the curvature budget: $S_\kappa$ at the wall is measured `1` to every digit double precision carries at physical gradients (`0.999979916516139` only at an unphysical one-node ceiling). The $u\!\leftrightarrow\!\phi$ **door** rides the strain kernel and therefore **CLOSES** at the wall, so shear$\to$rotation conversion is an **APPROACH** question, not a wall question. **⚑ This row is CONDITIONAL on the separate-kernel (L∞-across-grades) member of an open fork — cross-grade fence in the ROW 4 note below; do not read the row without it** |

**BH-echo yes/no is therefore a channel question.** EM-channel: transparent ($\Gamma_{EM} = 0$, no converged WKB echo under SYM scaling). Shear/bulk channels: reflecting ($\Gamma = -1$). Statements that "the horizon is a perfect absorber" (EM) and "the horizon reflects shear/GW modes" are **not contradictory** once channel subscripts are explicit.

> **⚑ ROW 4 ADDED 2026-08-05 (upgrade wave) — provenance, content and fences.** Until this date this table had **three** rows while [`port-register.md`](../../../common/port-register.md):47–50 carried **four** canonical channels, and [`research/2026-08-05_last-bond-kernel-collapse_result.md`](../../../../../research/2026-08-05_last-bond-kernel-collapse_result.md):31 recorded the gap with a two-method absence receipt (*"Cosserat", "couple-stress" and "micro-rotation" occurred **zero** times in this entire file*). **The content of row 4 is INVERTED relative to what the earlier squeeze-twist reading expected**, and that inversion is the measurement: the twist-coefficient lane returned **`NO-TWIST` by symmetry theorem**, Tier-2-verified, with **$S_\kappa(\text{wall}) = 1$** at physical gradients ([`research/2026-08-05_srs-twist-coefficient_result.md`](../../../../../research/2026-08-05_srs-twist-coefficient_result.md):318,:325; PR #890) — so rotational transport arrives at the wall untouched instead of collapsing with the strain grades. Ruled scope: the channel-scoped kernel-collapse ruling (**PR #897**, `[REVIEW: CLEARED]`), under which the strain-kernel channels (rows 2 and 3, plus the $u\!\leftrightarrow\!\phi$ coupling $G_c$) mirror while the rotational channel is **carved out**. **Fences.** The **approach leak** — shear$\to$rotation conversion in the graded taper where $G_c S_\varepsilon$ is finite — is **one computable number that no lane has computed**; it is routed, and **no size is asserted here**. The strain-kernel row is **`ROW-NOT-CERTIFIED`** pending the named `G-RHO2` repair, while the three load-bearing theorems are measured **exact**. This row adjudicates **no** fork, mints **no** id, moves **no** solidity, and carries **no** frontier reading about what the rotational channel does on the far side. **★ CROSS-GRADE FENCE — the condition row 4 rides on, and it is NOT in #897's ruled text (added by the doc lane 2026-08-05; the omission at the ruling is routed to Grant).** Row 4 holds on the **separate-kernel (L∞-across-grades)** member of an **open** fork: canon records the **cross-grade combine rule as underdetermined at $O(\alpha)$** ([`common/axiom-register.md`](../../../common/axiom-register.md):190,:232). Under L∞ — *"the wall is whichever grade reaches `S→0` first"*, the member the engine codes ([`cosserat_field_3d.py`](../../../../../src/ave/topological/cosserat_field_3d.py):761–762,:767–768: separate `S_eps_sq`/`S_kappa_sq`, with $G,G_c$ on the strain kernel and $\gamma$ on its own) — the strain grade sets this wall and $S_\kappa$ is untouched, so the row stands. Under **normalized-L2-across-grades** every grade rides ONE kernel and the row does **NOT** stand. The primary receipt *"does not choose the member"* ([`last-bond`](../../../../../research/2026-08-05_last-bond-kernel-collapse_result.md):29) and the twist lane leaves *"the cross-grade combine rule … open on its existing terms"* ([`srs-twist`](../../../../../research/2026-08-05_srs-twist-coefficient_result.md):372) while reporting the L∞ reading *"if anything, reinforced"* (`:373`) — **reinforced is not closed**. Canonical: [`common/wall-taxonomy.md`](../../../common/wall-taxonomy.md) §10.2.

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

### Channel discipline — tensile vs compressive bulk (FLAG)

**Do not conflate** astrophysical BH **compressive melt** ($c_{bulk} \to 0$ at exterior rupture) with electron **constructive interior** TIR / cavitation wall ($\Gamma_{bulk} \to -1$ at confinement boundary). Same $Z_{bulk} = \rho\,c_{bulk}$ law; **opposite thermodynamic branch** on the bulk EOS. This leaf assigns **BH exterior at $r_{\text{sat}}$** only. Electron confinement bulk reads route through harness rank-1b + [`device-circuit-models.md`](../../../vol9/ch3-pin-port-configuration/device-circuit-models.md) — not this melt assignment.

> ↗ See also: [`electron-bh-isomorphism.md`](electron-bh-isomorphism.md) — shear phase transition (updated with $\Gamma_{shear}$); [`ave-bh-horizon-area-theorem.md`](ave-bh-horizon-area-theorem.md) — $r_{\text{sat}}$ derivation; [`substrate-hysteresis-index.md`](../../../common/substrate-hysteresis-index.md) §5b — LOOP GAP vs $\Omega_{\text{freeze}}$ (engine memory vs remanence).

### Discipline audit (2026-06-12)

| Skill | Pass |
|---|---|
| `verify-before-cite` | Channel assignments grep-verified against [`electron-bh-isomorphism.md`](electron-bh-isomorphism.md):35–45; $Z_{bulk}=\rho c_{bulk}$ at `constants.py`:646–658 |
| `consistency-vs-emergence` | **Class B** render — no new primitive; closes vocab-audit §4(b) gap only |
| `ave-dimensional-provenance-check` | $Z_{bulk}$ is bulk-channel impedance ($\rho\times$ speed), not a dimensionless coupling |

---

---

> **⚑ Sign-relativity declaration (Grant ruling 2026-08-04; [`wall-taxonomy.md`](../../../common/wall-taxonomy.md) §10; PR #869 FLAG-W).** The Resultbox (:36–40) and the Bulk row of the channel table above (**three rows when this declaration was written 2026-08-04; four since the 2026-08-05 row-4 insert**) are stated (i) at the **LOAD plane** — the level-set itself, not the input plane outside the gradient skin (a quarter-wave of skin inverts the sign); (ii) on the **SHUNT-graded projection**; (iii) under the **constant-density (RHO-A) profile**: the step $Z_{bulk}=\rho_{bulk}\,c_{bulk}\to0$ multiplies the vanishing speed by a constant $\rho$. Under canon's $\rho_{eff}=\rho_0/S^3$ ([`saturating-modulus-and-backreaction.md`](../../gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md):73; FORK-3(b), fenced, axial run in flight) the same $c_{bulk}\to0$ coexists with $Z_{bulk}=\sqrt{K\,\rho_{eff}}\to\infty$. The signed value here is therefore profile-conditional and **computed-not-chosen** (branch-derived wall row = authority); the apparent conflict with the bulk-stiffening line ([`saturating-modulus-and-backreaction.md`](../../gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md):59) is plane/projection/profile relativity, not a contradiction. Body above preserved per Rule 12.
