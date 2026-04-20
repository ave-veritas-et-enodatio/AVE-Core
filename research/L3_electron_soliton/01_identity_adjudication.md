# Phase 1 — Identity Adjudication: $\hat{\mathbf{n}} \leftrightarrow \boldsymbol{\omega}$

**Status:** Phase 1, adjudication document. Physics-first analysis (per user direction, 2026-04-19). Awaiting user adjudication of the final recommendation.
**Prerequisite:** [`00_scoping.md`](00_scoping.md) §2 (Cosserat canonization), §4 (identity gap).

This document ranks the four candidate identities between the Faddeev-Skyrme orientation field $\hat{\mathbf{n}}(\mathbf{r}) \in S^2$ and the Cosserat microrotation field $\boldsymbol{\omega}(\mathbf{r}) \in \mathbb{R}^3$, argued from AVE-internal physics (spin-1/2 structure, Ch 8 Golden Torus derivation, Axiom 4 Nyquist cutoff) rather than external literature. A subsequent document ([`02_literature_pressure_test.md`](02_literature_pressure_test.md)) will pressure-test the result against external literature.

The four candidates are restated, then each is analyzed along five axes: topology, Golden-Torus compatibility, Lagrangian structure, physical interpretation, and pathologies. A side question — what "(2,3) phase winding" means topologically — is flagged as a remaining open question and delegated for user adjudication at the end of the document.

---

## §1  Common framework

Across all candidates, the Cosserat microrotation field $\boldsymbol{\omega}(\mathbf{r})$ is a vector in $\mathbb{R}^3$ at each point. Physically, under the standard axis-angle interpretation of SO(3) (and its double cover SU(2)):

- The magnitude $|\boldsymbol{\omega}|$ is a rotation angle (radians).
- The direction $\hat{\boldsymbol{\omega}} = \boldsymbol{\omega}/|\boldsymbol{\omega}|$ is the rotation axis.

The exponential maps associated with this interpretation are:

$$R(\boldsymbol{\omega}) = \exp(\boldsymbol{\omega} \times \cdot) \in SO(3), \qquad U(\boldsymbol{\omega}) = \exp(i\,\boldsymbol{\sigma}\cdot\boldsymbol{\omega}/2) \in SU(2)$$

with $\boldsymbol{\sigma}$ the Pauli matrices. These maps are standard; each is injective on $|\boldsymbol{\omega}| \in [0, \pi]$ (the "principal chart") and becomes surjective onto the full group for $|\boldsymbol{\omega}| \in [0, \pi]$ (SO(3)) or $|\boldsymbol{\omega}| \in [0, 2\pi]$ (SU(2)).

**Axiom-4 observation.** The Nyquist cutoff of Axiom 4 enforces $|\nabla\boldsymbol{\omega}| \leq \pi/\ell_{\text{node}}$, i.e., no more than a half-rotation per lattice cell. In natural units with $\ell_{\text{node}} = 1$, this is $|\nabla\boldsymbol{\omega}| \leq \pi$. The coincidence of this Nyquist cap with the natural domain boundary of the $SO(3)$ exponential chart is a structural alignment worth noting; it will recur below.

The FS field $\hat{\mathbf{n}}(\mathbf{r})$ is $S^2$-valued. Its topological invariant for smooth maps $\mathbb{R}^3 \to S^2$ with rapid decay at infinity (i.e., $S^3 \to S^2$) is the **Hopf invariant** $Q_H \in \pi_3(S^2) = \mathbb{Z}$, which counts how pairs of preimages link as curves in $\mathbb{R}^3$.

The SU(2) field $U(\mathbf{r})$ is $S^3$-valued. Its topological invariant for maps $S^3 \to S^3$ is the **winding number** (Skyrme / baryon number) $B \in \pi_3(S^3) = \mathbb{Z}$.

These are different invariants. Which one corresponds to AVE's "(2,3) phase winding" for the electron is itself an open sub-question — see §7.

---

## §2  Candidate C1 — Unit-vector projection

**Definition:** $\hat{\mathbf{n}}(\mathbf{r}) = \boldsymbol{\omega}(\mathbf{r}) / |\boldsymbol{\omega}(\mathbf{r})|$.

Under C1, the FS field is literally the direction of the Cosserat microrotation. Magnitude is discarded. Equivalently, $\boldsymbol{\omega}(\mathbf{r}) = f(\mathbf{r})\,\hat{\mathbf{n}}(\mathbf{r})$ where $f = |\boldsymbol{\omega}|$ is an independent scalar DOF.

**Topology.** Winding is preserved iff $f > 0$ everywhere; zeros of $\boldsymbol{\omega}$ would collapse the projection and are thus forbidden topologically. The Hopf invariant $Q_H$ is inherited entirely from $\hat{\mathbf{n}}$.

**Golden Torus.** The $(R, r)$ geometry of Ch 8 is inherited from $\hat{\mathbf{n}}$; $f$ plays no role. The multipole decomposition and $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ recovery is structurally identical to the pure-FS case.

**Lagrangian.** The Cosserat bending term decomposes:
$$|\nabla\boldsymbol{\omega}|^2 = |\nabla f|^2 + f^2 |\nabla\hat{\mathbf{n}}|^2$$
This introduces two kinetic terms: one for $f$, one for $\hat{\mathbf{n}}$. The $f$-kinetic is an independent scalar field without Ch-8 counterpart.

**Physical interpretation.** $f(\mathbf{r})$ would be interpreted as the "local amount of microrotation" — how much twist is dialed in at each point. Unconstrained in C1.

**Pathologies.**
- $f$ has no natural boundary value. It could be zero on sets of positive measure (where $\boldsymbol{\omega} = 0$), making $\hat{\mathbf{n}}$ undefined there. Avoiding this requires ad-hoc potentials on $f$.
- No physical mechanism fixes $f$ to match the Ch 8 prediction. To recover Ch 8, we would need $f$ constrained to (say) $f \equiv \pi$ everywhere — which is a constraint, not an emergent result.
- The magnitude-as-extra-DOF breaks the elegant one-to-one correspondence between $\boldsymbol{\omega}$ and the FS formulation. Adds, rather than unifies.

**Verdict.** Simplest map, but weakest physics. Introduces an unconstrained scalar that does not appear in Ch 8. **Rejected.**

---

## §3  Candidate C2 — Axis-angle in SO(3)

**Definition:** $\boldsymbol{\omega}(\mathbf{r})$ is the axis-angle parameterization of a local SO(3) rotation $R(\mathbf{r}) = \exp(\boldsymbol{\omega}\times \cdot)$. The FS field is derived as $\hat{\mathbf{n}}(\mathbf{r}) = R(\mathbf{r})\,\hat{\mathbf{z}}$ (or any fixed reference direction).

**Topology.** The map $R \mapsto R\hat{\mathbf{z}}$ is the standard fibration $SO(3) \to S^2$ with fibre $SO(2) \cong S^1$. $\pi_3(SO(3)) = \mathbb{Z}_2$ (twisted) while $\pi_3(S^2) = \mathbb{Z}$ (Hopf). The topology of $\boldsymbol{\omega}$ as an SO(3)-valued field is coarser than the topology of its $S^2$ projection.

**Golden Torus.** Inherited from $\hat{\mathbf{n}}$. The Ch-8 derivation goes through unchanged in the S² sector.

**Lagrangian.** The Cosserat bending term decomposes into two parts:
$$|\nabla\boldsymbol{\omega}|^2 \supset |\nabla\hat{\mathbf{n}}|^2 + |\nabla\alpha_\parallel|^2$$
where $\alpha_\parallel(\mathbf{r})$ is the local rotation angle *about* $\hat{\mathbf{n}}(\mathbf{r})$ — the stabilizer direction, the SO(2) fibre. This "$\alpha_\parallel$" is an independent phase DOF that does not appear in the pure-FS description.

**Physical interpretation.** This is where C2 becomes interesting. The stabilizer-direction phase $\alpha_\parallel$ is a physical internal phase — the electron's rotation *about* its own orientation axis. For a spin-1/2 object, this is exactly the phase that requires a $4\pi$ (not $2\pi$) rotation to return to identity. Ch 8's $\pi^2$ factor from the "spin-1/2 half-cover of the Clifford torus" is native structure of the SO(3) → SU(2) double cover, not an ad-hoc insertion.

However, $\pi_1(SO(3)) = \mathbb{Z}_2$ — spin-1/2 is NOT faithfully representable in SO(3); you need SU(2). C2 is therefore *almost* right but fails to capture spin-1/2 at the group level. The SO(2) fibre provides the phase, but SO(3) is the wrong global cover.

**Pathologies.**
- $\pi_1(SO(3)) = \mathbb{Z}_2$: spin-1/2 is a $\mathbb{Z}_2$-twisted section of SO(3), not a proper representation. For AVE's electron as a faithful spin-1/2 object, this is insufficient.
- The exponential map $\exp: \mathfrak{so}(3) \to SO(3)$ is two-to-one in the sense that $\boldsymbol{\omega}$ and $\boldsymbol{\omega}'$ with $|\boldsymbol{\omega}| = |\boldsymbol{\omega}'| = \pi$ but opposite direction map to the same SO(3) element. This degeneracy at $|\boldsymbol{\omega}| = \pi$ creates a topological defect at the Nyquist boundary.

**Verdict.** Structurally rich (captures internal phase) but spin-content-wrong (SO(3) is a single cover, not double). Lifting to SU(2) (candidate C3) fixes this. **Not preferred; use C3.**

---

## §4  Candidate C3 — SU(2) embedding

**Definition:** $U(\mathbf{r}) = \exp(i\,\boldsymbol{\sigma}\cdot\boldsymbol{\omega}(\mathbf{r})/2) \in SU(2)$. The FS field is $\hat{n}^a(\mathbf{r}) = \tfrac{1}{2}\text{tr}\big(\sigma^a\,U(\mathbf{r})\,\sigma^3\,U^\dagger(\mathbf{r})\big)$ (Hopf fibration $SU(2) \to S^2$ with fibre $U(1)$).

**Topology.** SU(2) as a group is $S^3$. $\pi_3(SU(2)) = \pi_3(S^3) = \mathbb{Z}$ — the Skyrme / baryon winding number $B$. The projected $\hat{\mathbf{n}}$ carries the Hopf invariant $Q_H \in \pi_3(S^2) = \mathbb{Z}$. These are *different* invariants. The U(1) fibre direction also carries a winding $w_{U(1)}$.

**Golden Torus.** Inherited cleanly from $\hat{\mathbf{n}}$ — Ch 8 derivation goes through. The $\pi^2$ factor from "spin-1/2 half-cover of the Clifford torus" is now structural, not assumed: SU(2) *is* the double cover of SO(3), so the half-cover prefactor $\Lambda_{\text{surf}} = \pi^2$ falls out of the SU(2) → SO(3) 2-to-1 map. Ch 8 §2.1.2 ("Rigorous Derivation of $\Lambda_{\text{surf}} = \pi^2$ from Spin-1/2 Half-Cover") becomes the *definition* of the SU(2) projection, not a special-case argument.

**Lagrangian.** The Cosserat bending term:
$$|\nabla\boldsymbol{\omega}|^2 \supset |\nabla\hat{\mathbf{n}}|^2 + |\nabla\alpha_\parallel|^2$$
with $\alpha_\parallel$ now the U(1) fibre phase (SU(2) → S²). Two kinetic sectors: the $\hat{\mathbf{n}}$ gradient (ordinary FS / σ-model) and the U(1) gauge-phase gradient.

The U(1) sector is a natural home for an additional AVE coupling: it could carry the electromagnetic gauge structure, or the "(2,3)" phase-winding index, or both. Phase-1 sub-work.

**Physical interpretation.**
- SU(2) is the correct global cover for spin-1/2. The electron is a genuine spin-1/2 representation, not a $\mathbb{Z}_2$-twisted section.
- The U(1) fibre phase is the internal spin phase requiring $4\pi$ to close — exactly the phenomenon Ch 8's $\Lambda_{\text{vol}} = 4\pi^3$ captures via "temporal double-cover."
- The Skyrme number $B$ is a natural topological charge for nucleon-like solitons (proton/neutron — (2,5) cinquefoil in AVE). The Hopf invariant $Q_H$ is the natural topological charge for lepton-like solitons (electron — unknot with (2,3) phase winding). SU(2) supports both, with $B$ coming from the full SU(2) winding and $Q_H$ from the S² projection. **This is a direct structural match to AVE's lepton/baryon distinction.**

**Pathologies.**
- The map $\boldsymbol{\omega} \mapsto U$ has domain boundary at $|\boldsymbol{\omega}| = 2\pi$ (after which it cycles). The Nyquist cutoff $|\nabla\boldsymbol{\omega}| \leq \pi/\ell_{\text{node}}$ is *half* this boundary, suggesting: if $\boldsymbol{\omega}$ itself (not just its gradient) is bounded by the Cosserat yield, the natural cap $|\boldsymbol{\omega}|_{\max} = \pi$ gives the SO(3) chart, not the full SU(2) cycle. The $|\boldsymbol{\omega}|_{\max} = 2\pi$ cap gives SU(2). Which is AVE's physical intent? Sub-question for Phase-1 numerics.
- Projection $U \mapsto \hat{\mathbf{n}}$ loses information — the U(1) fibre. A purely $\hat{\mathbf{n}}$-based description is an *incomplete* representation of the Cosserat field. This is a feature, not a bug: existing AVE code [`faddeev_skyrme.py`](../../src/ave/topological/faddeev_skyrme.py) can be read as "the $\hat{\mathbf{n}}$-sector projection of the full SU(2) Cosserat field," with the U(1) sector awaiting exposure.

**Verdict.** **C3 is the natural answer.** SU(2) matches spin-1/2 at the group level, recovers Ch 8's $\pi^2$ half-cover structurally, supports both lepton and baryon topological charges from one field, and naturally carries the U(1) internal-phase DOF that Ch 8's temporal-double-cover implies. **Recommended as the Phase-1 canonical identity.**

---

## §5  Candidate C4 — $\boldsymbol{\omega}$ primary, $\hat{\mathbf{n}}$ derived

**Definition:** $\boldsymbol{\omega}(\mathbf{r})$ is the primary dynamical field. $\hat{\mathbf{n}}$ is a *derived* pedagogical quantity, not a separate field. The Lagrangian is written strictly in Cosserat variables.

**Topology.** If $\boldsymbol{\omega}$-space is compactified via $\boldsymbol{\omega} \to 0$ at infinity plus the identification $|\boldsymbol{\omega}| = 2\pi \sim 0$ (SU(2) cover), the field is $S^3$-valued and carries Skyrme number $B \in \mathbb{Z}$. In practice, C4 is C3 without explicitly constructing the $\hat{\mathbf{n}}$ projection.

**Golden Torus.** Recoverable via the same projection as C3, but the projection is treated as a calculational convenience, not an additional structure. The $(R, r) = (\varphi/2, (\varphi-1)/2)$ geometry is read off the $|\boldsymbol{\omega}|$ level-sets (or the analogous invariants of $\boldsymbol{\omega}$).

**Lagrangian.** Strictly Cosserat. The FS energy functional $\int|\nabla\hat{\mathbf{n}}|^2 + \kappa^2|\nabla\hat{\mathbf{n}} \wedge \nabla\hat{\mathbf{n}}|^2$ must be re-derived in $\boldsymbol{\omega}$ variables. The Skyrme four-derivative term becomes a specific combination of $|\nabla\boldsymbol{\omega}|^2$ and $|\nabla\boldsymbol{\omega}|^4$ or the analogue. This is a concrete Phase-1 calculation and is non-trivial but standard (pattern: re-deriving Skyrme energy in axis-angle variables is textbook Manton-Sutcliffe material).

**Physical interpretation.** Identical to C3. The difference is bookkeeping — C4 eliminates the redundancy of tracking two fields when one suffices.

**Pathologies.** Loses the direct bridge to existing Faddeev-Skyrme literature (all of which is $\hat{\mathbf{n}}$-based). Any external citation requires a translation step back to C3. This is a practical cost, not a physical one.

**Verdict.** **C4 is C3 in Cosserat-native dress.** It is a reformulation, not a distinct candidate. The question of C3 vs C4 is purely stylistic: expose the projection explicitly (C3) or keep it implicit (C4). C3 is better for Phase-1 write-up (literature bridges, pedagogy). C4 may be better for Phase-3 numerical implementation (leaner state vector, no redundancy).

**Recommendation:** Adopt **C3 as the canonical identity for the Phase-1 Lagrangian derivation**. Use **C4 as the computational convention for Phase-3 numerics** if it produces materially leaner code; otherwise keep C3 for uniformity.

---

## §6  Ranking summary

| Candidate | Captures spin-1/2 | Recovers Ch 8 $\pi^2$ | Supports lepton + baryon | Axiom 4 natural | Verdict |
|---|---|---|---|---|---|
| C1 (unit-vector) | no (discards magnitude) | only via ad-hoc constraint | no (one invariant only) | no | **reject** |
| C2 (SO(3) axis-angle) | partial ($\mathbb{Z}_2$-twist) | yes | partial (no SU(2) structure) | chart boundary aligns at $|\omega|=\pi$ | **supersede by C3** |
| C3 (SU(2) embedding) | yes (native) | yes (structural) | yes ($B$ for baryon, $Q_H$ for lepton) | cap at $|\omega|=2\pi$ or $\pi$ — TBD | **canonical** |
| C4 (Cosserat-native) | yes | yes | yes | as C3 | **C3 in lean form; use for Phase 3 if leaner** |

---

## §7  Remaining open question — what is "(2,3) phase winding" topologically?

AVE refers to the electron's topological structure as "unknot with (2,3) phase winding." Three distinct topological readings of this phrase are consistent with the corpus as it stands:

**Reading (a): Hopf number.**
$(2,3)$ indexes the torus-knot type of preimage curves in a Hopfion with $Q_H = 2 \times 3 = 6$. Under this reading, the electron is a Hopf-6 soliton whose generic preimage curves are $(2,3)$-type torus knots (trefoils) linked pairwise. This is the Sutcliffe-2007 convention.

**Reading (b): Bi-winding U(1) on the toroidal shell.**
On the Clifford torus $\mathbb{T}^2 = S^1 \times S^1 \subset S^3$, the phase field has winding number 2 around the major axis and 3 around the minor axis. The topological charge is $(w_1, w_2) = (2, 3)$ in $\pi_1(\mathbb{T}^2) = \mathbb{Z}^2$. The "spatial unknot" is the core ring of the toroidal neighborhood; the $(2,3)$ winding is the U(1)-phase winding on the enveloping shell. Under C3, this U(1) is precisely the SU(2) → S² fibre phase $\alpha_\parallel$ from §4.

**Reading (c): $(Q_H, w_{U(1)}) = (2, 3)$ joint invariant.**
SU(2) fields carry *two* natural invariants when projected: the S² Hopf number $Q_H$ and the U(1)-fibre winding $w_{U(1)}$. Under this reading, "(2,3)" is the pair $(Q_H, w_{U(1)}) = (2, 3)$. Neither alone, but both together, define the electron.

Each reading has different consequences:

- Reading (a) matches the Sutcliffe torus-knot soliton literature and the AVE Ch 8 language ("trefoil knot"). The spatial unknot is a coarse description (the *centerline* of the Hopfion is unknotted, but the knotted structure exists in the preimage curves).
- Reading (b) matches the AVE Clifford-torus $\Lambda_{\text{surf}}$ derivation directly — the screening constraint $R \cdot r = 1/4$ is a statement about two phases at radii $R$ and $r$. It naturally maps onto the SU(2) fibre + SO(3) phase projection.
- Reading (c) would predict additional quantized structure — e.g., some observable that distinguishes $(Q_H, w) = (2,3)$ from $(3,2)$ or $(1,6)$. AVE would need such an observable for this reading to carry its weight.

**I recommend Reading (b)** as the most consistent with Ch 8's math (Clifford-torus half-cover, two independent winding directions at radii $R$ and $r$) and the C3 identity (the $(2,3)$ becomes the dual winding of the SO(3) direction and the SU(2) fibre phase). But this is a physics judgment call, and you adjudicate.

**Flagged for your resolution before Phase-1 Lagrangian derivation proceeds.**

---

## §8  Consequences for Phase 1 if C3 + Reading (b) is adopted

- The Lagrangian is written in $\boldsymbol{\omega}$ and $\mathbf{u}$ with the Cosserat constitutive equations of `00_scoping.md` §3.3.
- The topological boundary condition for the electron ground state is: on the toroidal-shell $\mathbb{T}^2$ at the trefoil's ropelength boundary, the SO(3) direction $\hat{\mathbf{n}}$ winds 2× around the major axis and the U(1) fibre phase $\alpha_\parallel$ winds 3× around the minor axis (or the other way — convention choice).
- The Ch-8 multipole decomposition becomes an emergent result: the three terms $\Lambda_{\text{vol}}$, $\Lambda_{\text{surf}}$, $\Lambda_{\text{line}}$ correspond to the SU(2) double-cover volume prefactor, the S² Hopf-area surface prefactor, and the core-tube line prefactor, respectively.
- Existence proof: a winding-3 U(1)-sector ground state on the Clifford torus exists trivially (it's a harmonic map); the C3 identity promotes this to a full Cosserat ground state by embedding into SU(2).
- Uniqueness: follows from the K = 2G moduli constraint + the Nyquist cutoff fixing the domain of $\boldsymbol{\omega}$, modulo rigid-body isometries.

If Reading (a) or (c) is adopted instead, the Lagrangian derivation is similar but the topological boundary condition and the invariants change correspondingly. The Phase-1 Lagrangian skeleton is structurally robust to the reading choice; only the boundary-condition spelling shifts.

---

## §9  What this document defers

- **Explicit Lagrangian:** To be produced in [`02_lagrangian_derivation.md`](02_lagrangian_derivation.md) after user adjudication of C3 + reading.
- **External literature pressure test:** [`02_literature_pressure_test.md`](02_literature_pressure_test.md) (alternate filename depending on sequencing).
- **Existence proof formal statement:** Phase-1 deliverable.
- **Cosserat moduli values (numerics):** Phase-1 — pinned from K = 2G plus Ch 8 geometric constraints.
- **Ch 8 footnote:** queued in `DOCUMENTATION_UPDATES_QUEUE.md` item [1].

---

## §10  User adjudication required

Two questions:

1. **C3 as the canonical identity?** My recommendation is C3 (with C4 as the lean Phase-3 computational convention). If you prefer C2 or one of the others, I'll re-argue — but C1 is genuinely dead.
2. **Reading (a), (b), or (c) for "(2,3) phase winding"?** My recommendation is Reading (b). This is a physics judgment — if your original intent was Reading (a) (Sutcliffe torus-knot Hopfion, $Q_H = 6$) or Reading (c) (joint invariant), please adjudicate.

Phase-1 Lagrangian derivation begins once both are answered.
