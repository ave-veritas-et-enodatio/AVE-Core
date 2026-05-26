[↑ Ch.1 Topological Matter](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-salw2h]
path-stable: "referenced from spin-half-paradox + k4-rotation-group + ch8-alpha-golden-torus regime (c) + spin-gyroscopic-isomorphism as canonical FM-on-K4 explicit derivation host; depends-on from clm-unk0bd (Phase 2 sub-item 3, 2026-05-25) + clm-zuf7g1 (Phase 1 clm-zuf7g1-strengthen workstream, 2026-05-26 — supplies the spin-1/2 Möbius half-angle coupling for the Bell-correlation derivation)"
-->

# Finkelstein-Misner Spin-½ Derivation on the K4 Substrate
<!-- claim-quality: clm-salw2h -->

This leaf carries the **explicit derivation** of electron spin-½ from K4-substrate physics via the Finkelstein-Misner (FM) kink mechanism on the extended $0_1$ unknot defect. It is the detail-derivation host for `clm-salw2h` (the spin-½-as-macroscopic-gyroscopic-precession claim canonically hosted in [spin-half-paradox.md](../../appendices/app-b-paradoxes/spin-half-paradox.md) + [spin-gyroscopic-isomorphism.md](spin-gyroscopic-isomorphism.md)), spelling out the K4-native mechanism beyond the brief paragraph in spin-half-paradox.md.

**Resolves**: clm-0ktpcn strengthen-by item 2 ("Spell out the Finkelstein–Misner spin-1/2 derivation from the $K_4 \to A_4 \to 2T \subset SU(2)$ chain explicitly in the leaves").

## §1 The question — why is spin-½ a paradox to resolve in AVE?

Standard solid-state mechanics: continuum elastic media with $SO(3)$ rotational geometry support only integer-spin point defects (spin-1, spin-2). Electrons are spin-½ ($SU(2)$ geometry, $4\pi$ rotation to return to original state). A chiral Laves K4 Cosserat crystal with $SO(3)$ continuum geometry should not support spin-½ point defects — apparent falsification.

**The mistake**: treating the electron as a *point defect*. Per Axiom 1 and per the canonical electron identification at [electron-unknot.md](electron-unknot.md), the electron is **NOT a point defect** — it is an **extended** $0_1$ unknot soliton: the simplest closed continuous topological flux tube loop with no real-space crossings, embedded across multiple bonds of the K4 substrate.

For extended topological defects in $SO(3)$ manifolds, the Finkelstein-Misner kink mechanism (1959 classical differential topology, also known as the Dirac belt-trick) provides $SU(2)$ spinor behavior — without invoking quantum mechanics. The chiral Laves K4 Cosserat crystal IS the $SO(3)$ base manifold the FM theorem requires; the unknot IS the extended defect; the $4\pi$ double-cover IS classical topology of extended objects in 3D space.

## §2 The Finkelstein-Misner / Dirac belt-trick mechanism

### §2.1 General mechanism (classical topology of extended defects)

Consider an extended object (a belt, a string loop, a knotted flux tube) connected at both ends to a fixed reference frame. Apply a $2\pi$ rotation to one end while holding the other fixed:

- The object acquires a **TWIST** that cannot be removed without passing the object through itself
- Apply ANOTHER $2\pi$ rotation (total $4\pi$): the twist **unwinds** through the object's body, returning to untwisted state without intersection
- This is classically demonstrable with any belt or rope (Dirac's belt-trick)

**Mathematical content**: extended objects connected to their environment have a **2-to-1 cover** of the $SO(3)$ rotation group. $2\pi$ gives a topologically distinct state; $4\pi$ returns to the original. Standard differential topology, no quantum mechanics required.

### §2.2 Application to the K4 unknot soliton

The electron, per Axiom 1, is the simplest extended topological defect on the K4 lattice — the $0_1$ unknot at minimum ropelength $= 2\pi$. The unknot is a **closed loop** embedded in the 3D K4 substrate, with its ends "connected" by the closure condition.

Under a $2\pi$ rotation in 3D:
- The unknot loop rotates as a whole
- Its **embedding in the K4 substrate twists** relative to the lattice (the Finkelstein-Misner kink)
- The twist is topologically non-trivial — cannot be removed without cutting the loop

Under a $4\pi$ rotation:
- The accumulated twist **unwinds** through the loop's structure (the substrate provides the topological "room" to untwist)
- The embedding returns to its original state
- This is the topological double-cover, derived from K4 + extended-defect topology

This is the AVE-native spin-½ mechanism. It is **classical topology of the extended K4 soliton**, not $SU(2)$ representation theory imported from QFT.

## §3 Group-theoretic anchor — the $K_4 \to A_4 \to 2T \subset SU(2)$ chain

The mechanism above is *physical*; the chain that connects it to the standard $SU(2)$ formalism is *group-theoretic*. Per [k4-rotation-group.md](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) §6 (clm-rkisb8):

1. **K4 rotation symmetry**: the rotation group of the K4 tetrahedral lattice is $T = A_4$, order 12 (rigorous derivation via faithful representation in §1-§4 of k4-rotation-group.md)
2. **Double cover**: the binary tetrahedral group $2T$ has order 24 and sits inside $SU(2)$ as a discrete subgroup
3. **Exact sequence**: $1 \to \mathbb{Z}_2 \to 2T \to A_4 \to 1$. The $\mathbb{Z}_2$ quotient is the $4\pi$ double-cover: each $A_4$ element has two preimages in $2T$ differing by the central element $-I \in SU(2)$
4. **The double-cover lift**: a $2\pi$ rotation in $SO(3)$ lifts to $-I$ in $SU(2)$ (sign flip); only $4\pi$ lifts to $+I$

For spin-½ to be K4-derived (not imported from QM), physical fields on the K4 lattice must transform under $2T$ rather than $T$. The Finkelstein-Misner mechanism on the extended $0_1$ unknot defect (per §2 above) is what realizes this: the *extended* nature of the defect is what picks up the $2T$ double-cover rather than the trivial $T$ action.

## §4 The gyroscopic-isomorphism numerical anchor

The mechanism in §2 + the group-theoretic chain in §3 establish that the K4 extended-unknot picks up a $4\pi$ double-cover. The companion numerical fact — that the resulting dynamics are **mathematically identical** to standard quantum spinor evolution — is established by the gyroscopic-isomorphism leaf at [spin-gyroscopic-isomorphism.md](spin-gyroscopic-isomorphism.md).

The two ODEs:

$$\text{Classical: } \quad \frac{d\mathbf{L}}{dt} = \gamma\,\mathbf{L} \times \mathbf{B}$$

$$\text{Quantum: } \quad i\,\frac{d|\psi\rangle}{dt} = -\tfrac{1}{2}\gamma\,\boldsymbol{\sigma} \cdot \mathbf{B}\,|\psi\rangle$$

Numerically integrated under identical RF field $\mathbf{B}(t) = (B_1 \cos\omega t,\, B_1 \sin\omega t,\, B_0)$, the maximum time-domain deviation is at numerical-integration tolerance:

$$\max_t \big| L_z(t) - \langle S_z \rangle(t) \big| \sim 10^{-8}$$

The script implementing this is at [`src/scripts/vol_2_subatomic/simulate_gyroscopic_spin.py`](../../../../../src/scripts/vol_2_subatomic/simulate_gyroscopic_spin.py). It defines Pauli matrices explicitly, integrates both ODEs under identical field, and verifies the deviation.

**The two formalisms describe the same physics.** Per the AVE interpretation, Pauli matrices are *the 2D projection of 3D Lenz's-law cross-product dynamics*. The "quantum" features (4π double-cover, spinor structure, sign flip under 2π) are CLASSICAL features of the extended unknot's gyroscopic precession on the K4 substrate. The translation-table mapping at [translation-qm.md](../../../common/translation-tables/translation-qm.md) captures the encoding cleanly:

> **Spin** ↔ Unknot chirality ↔ Two orientations of the unknot twist: $\pm 1/2$.

The $\pm 1/2$ chirality (encoding) and the $4\pi$ double-cover (mechanism) are complementary properties of the same extended unknot defect: the chirality is the discrete twist orientation; the double-cover is the dynamic property under continuous rotation.

## §5 K4-native vs imported standard math — explicit decomposition

This decomposition follows the doc-23 §4 pattern and is recommended as a corpus-wide convention for any AVE derivation that uses borrowed mathematical formalism. It keeps clear which parts of the formalism are K4-native physics and which are imported calculational scaffolding.

**K4-NATIVE (derivable from Axioms + K4 + classical topology):**

1. The unknot as smallest stable extended defect (Axiom 1)
2. The $4\pi$ double-cover via Finkelstein-Misner kink on extended defects (classical topology of §2.2)
3. Gyroscopic precession dynamics on the K4 substrate (classical mechanics)
4. The mathematical equivalence to $SU(2)$ spinor evolution at $10^{-8}$ tolerance (Pauli matrices = 2D projection of Lenz's-law cross-product dynamics)
5. Consistency between this $4\pi$ double-cover factor and the $4\pi$ factor appearing in $R_{TIR} = Z_0/(4\pi)$ at [theorem-3-1-q-factor.md](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) Theorem 3.1 v2 — same 3D-Euclidean-topology root, not an SI unit artifact (see §7). The Vol 4 theorem's $4\pi$ has its own derivation context; the cross-volume consistency with the FM-mechanism here is an implication, not an attribution claim of FM-on-unknot as the source.

**IMPORTED (acceptable standard math, used as calculational tool):**

1. The Finkelstein-Misner topological theorem itself (Finkelstein & Misner, 1959 — classical differential topology of extended defects in $SO(3)$ manifolds)
2. Lie group $SU(2)$ language for describing the dynamics (group theory)
3. Pauli matrix algebra as a calculational tool (linear algebra)

**The distinction**: AVE uses standard math (Lie groups, topology, linear algebra) to DESCRIBE the K4-native physics. The PHYSICS (extended-unknot gyroscopic precession with $4\pi$ double-cover) is K4-native; the MATH LANGUAGE ($SU(2)$, Pauli matrices, $2T$ group structure) is imported but applies to genuinely K4-native dynamics. Analogous to using calculus to describe Newton's laws — calculus is imported math, but $F = ma$ is genuine physics.

## §6 Substrate-native origin of intrinsic spin

The Cosserat microrotational DOF per K4 node (Axiom 1, three rotational coordinates alongside the three translational ones) IS the substrate-native origin of intrinsic spin. Per the canonical statement at [`manuscript/ave-kb/CLAUDE.md`](../../../CLAUDE.md) INVARIANT-S2:

> "The Cosserat rotational DOF IS the substrate-native origin of intrinsic spin: macroscopic angular momentum, the EM magnetic field $B$, and QM electron spin are three projections of the same per-node rotational coordinate."

The FM mechanism above shows **how** the per-node rotational DOF, when integrated across the extended $0_1$ unknot defect, picks up the $4\pi$ double-cover that distinguishes spin-½ from integer-spin. The Cosserat character provides the local rotational DOF; the extended-defect topology provides the global $SU(2) \to SO(3)$ 2-to-1 cover.

## §6.5 Why photons do NOT inherit the 4π closure

A natural concern: if the K4 substrate's Cosserat micro-rotational DOF is the substrate-native origin of spin and the $4\pi$ double-cover is a property of that DOF on extended defects, would open transverse EM waves (photons) propagating on the same K4 substrate also inherit the $4\pi$ closure? Empirically, photons exhibit $2\pi$ closure (standard SO(3) behavior). If the AVE framework forced photons to carry $4\pi$, it would be falsified at the lab bench.

**The resolution is structural**: the $4\pi$ double-cover applies **only to closed extended defects**, not to open propagating waves. Photons are open propagating waves. Therefore photons cannot carry $4\pi$ closure even in principle.

### §6.5.1 The extended-defect requirement is load-bearing

Per [spin-half-paradox.md:12](../../appendices/app-b-paradoxes/spin-half-paradox.md) verbatim:

> "If the electron were modeled as a microscopic point-defect (a missing node), the framework would indeed fail. However, the AVE framework defines the electron as an extended, macroscopic $0_1$ Unknot (a closed, continuous topological flux tube loop). **In topological mathematics, an extended knotted line defect embedded in an $SO(3)$ manifold exhibits $SU(2)$ spinor behaviour through the generation of a Finkelstein-Misner Kink**. The continuous geometric extension of the topological loop provides a double-cover over the $SO(3)$ background, reproducing Spin-1/2 quantum statistics without violating macroscopic solid-state geometry."

And §2.1 above (FM mechanism, verbatim): *"extended objects connected to their environment have a 2-to-1 cover of the $SO(3)$ rotation group. $2\pi$ gives a topologically distinct state; $4\pi$ returns to the original. Standard differential topology, no quantum mechanics required."*

The mechanism explicitly requires the object to be (i) **extended** (has body, not a point) and (ii) **closed** (loop topology, has the "twist that propagates around the body" property of the belt trick). Open EM waves satisfy neither condition: they are propagating disturbances of the Cosserat ω-field, not extended defects, not closed loops in SO(3). The FM theorem simply does not apply to them.

### §6.5.2 The Hopf-fibration projection argument (per L3 doc 06)

A second independent argument addresses the same question via projection-level analysis. Per `research/_archive/L3_electron_soliton/06_winding_index_projection.md` (Phase 1 winding-index projection, 2026-04-20), the full AVE description of an electron lives at Level 1 of a 5-level chain:

| Level | Object | Carries $(w_1, w_2) = (2,3)$? |
|---|---|---|
| 0 | Cosserat $\boldsymbol{\omega}(\mathbf{r}) \in \mathbb{R}^3$ field | yes (full SU(2) information) |
| 1 | $U(\mathbf{r}) \in SU(2)$ via $U = \exp(i\boldsymbol{\sigma}\cdot\boldsymbol{\omega}/2)$ | yes (full SU(2) information) |
| 2 | $\hat{\mathbf{n}}(\mathbf{r}) \in S^2$ via Hopf fibration $SU(2) \to S^2$ | **$w_1=2$ survives, $w_2=3$ DROPPED (lives in U(1) fibre)** |
| 3 | EM polarization $\mathbf{E}(\mathbf{r},t)$ via $\hat{\mathbf{n}} \leftrightarrow$ E-direction | no (already lost at Level 2) |
| 4 | Photon-wavefront path in $\mathbb{R}^3$ | no |

The Hopf fibration $SU(2) \to S^2$ has $U(1)$ fibre. The U(1) fibre phase is precisely what carries the $4\pi$ closure: a $2\pi$ SO(3) rotation lifts to the central element $-I \in SU(2)$ (a sign flip in the U(1) phase), and only $4\pi$ returns to $+I$. **Photons live at Level 3 (E-field polarization $\in S^2$), having already been projected through the Hopf fibration from Level 1 to Level 2. The U(1) fibre phase — and with it the $4\pi$ closure — was dropped at the projection step.** What photons see is the $S^2$-level $w_1=2$ winding (which under standard SO(3) closes at $2\pi$), not the SU(2)-level fibre that distinguishes $2\pi$ from $4\pi$.

This is fully consistent with the §6.5.1 extended-defect argument: photons are non-closed propagating modes that exist at the SO(3) projection level, where the SU(2) double-cover information has been integrated out. The two arguments are different lenses on the same structural fact.

### §6.5.3 Net result

Open transverse EM waves (photons) on the K4 substrate close at $2\pi$, not $4\pi$. The substrate's $4\pi$ structure is a property of closed extended defects (electrons + other torus-knot solitons), not of propagating modes. The empirical fact that photons do NOT exhibit $4\pi$ closure is consistent with — not in tension with — the FM-on-extended-unknot derivation in this leaf.

**Scope clarification, not retraction**: the Möbius / $720°$ structure is canonical for the electron's chiral $K_4$ extended-defect topology (see [`phase-locked-topological-thread.md:112`](../../../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md), clm-zuf7g1: *"Spin-1/2 as Möbius topology (Axiom 1). The electron unknot ($0_1$) is a Beltrami standing wave on the chiral $K_4$ graph."*). What was loosely phrased — that the $K_4$ substrate-as-a-whole carries the $4\pi$ structure, with the implication that every wave on it would inherit $4\pi$ — is the framing this section corrects. The $4\pi$ lives on the extended-unknot defect's topology in $SO(3)$, not on bulk propagation modes; photons are not extended-unknot defects; therefore photons do not inherit $4\pi$.

**Scope note on the projection-chain argument (§6.5.2)**: the Hopf-fibration argument imported from L3 doc 06 uses the $(w_1, w_2)$ winding-pair framing. Per doc 06's own amendment (2026-04-20), the corpus-cleaner framing for ELECTRON identification uses the scalar crossing count $c$ (electron $c = 3$, photon trajectory $c = 0$; see [`07_universal_operator_invariants.md`](../../../../../research/_archive/L3_electron_soliton/07_universal_operator_invariants.md)). For the SPECIFIC question here — does an open EM wave inherit $4\pi$ — the projection-level argument stands regardless of which invariant convention is used: $4\pi$ closure is carried by the U(1) fibre of $SU(2)$, photons exist at the Hopf-projected $S^2$ level, U(1) information is dropped at the projection step. The doc 06 amendment doesn't supersede the §6.5.2 conclusion, only the (w_1, w_2)-vs-scalar-c framing convention.

**This closes sub-item 3 of clm-0ktpcn's strengthen-by list.** No new claim id introduced; the result is a corollary of clm-salw2h's existing scope (FM derivation establishes WHERE the $4\pi$ lives, and equally WHERE it doesn't).

## §7 The 4π is physical, not an SI unit artifact

A prior concern: the $4\pi$ in $R_{TIR} = Z_0/(4\pi)$ of [theorem-3-1-q-factor.md](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) Theorem 3.1 v2 might be a SI-vs-Gaussian unit convention factor, not physical content (since SI uses $4\pi\varepsilon_0 = 1/k_C$ for Coulomb).

**Resolution (plausibility-strong, theorem-pending)**: the $4\pi$ is genuinely physical via the gyroscopic-isomorphism + the FM topological double-cover. It happens to coincide with the SI convention's $4\pi\varepsilon_0$ because both are consequences of 3D Euclidean topology: $4\pi$ is the spherical solid-angle integration factor for 3D and ALSO the extended-defect $SU(2) \to SO(3)$ double-cover factor. These appear to both be manifestations of 3D-Euclidean topology applied to extended objects — a single common 3D-Euclidean root rather than two independent $4\pi$ coincidences — but a rigorous theorem proving the identification is not provided here; the argument at this level is plausibility-strong, not theorem-rigorous.

The $4\pi$ is plausibly BOTH the spherical solid-angle factor AND the extended-defect double-cover factor. The fact that SI happens to also use $4\pi$ in $4\pi\varepsilon_0$ is consistent: same 3D-Euclidean-topology root. Closing this to theorem-rigor (showing the two $4\pi$ appearances are necessarily one factor under a unified extended-object-in-3D-Euclidean-space framework, rather than coincidental) is open work; flagged here for transparency.

## §8 What this derivation does NOT do

For honest scope-correction:

- **Does NOT** provide a discrete-lattice computation of the Finkelstein-Misner kink on K4 — would require full extended-defect simulation, not currently in the K4-TLM or Master Equation FDTD engines. Numerical anchor is via the gyroscopic-isomorphism (single-particle in external field), not via direct lattice simulation of the FM kink itself.
- **Does NOT** demonstrate dynamical stability of the FM kink under K4-lattice perturbation. The gyroscopic-isomorphism numerical anchor (§4) is single-particle in continuum (Pauli ODE under RF field), not a discrete K4-lattice evolution of the extended unknot defect under finite perturbation. Engine-level FM-kink simulation on the K4 lattice would require full extended-defect dynamics (not currently in K4-TLM or Master Equation FDTD); flagged as open work for a future Phase.
- **Does NOT** derive the specific Pauli matrix algebra from K4 geometry — the gyroscopic-isomorphism shows Pauli is equivalent to classical Lenz's-law cross-product dynamics, but it doesn't *derive* the matrix form from substrate primitives.
- **Does NOT** address the (2,3) phase-space winding selection mechanism here — that is closed via cross-ref to [torus-knot-uniqueness.md](torus-knot-uniqueness.md) (clm-8c3yhs), the canonical home of the coprimality + minimality argument; clm-unk0bd's depends-on graph wires this in (2026-05-25 Phase 2 sub-item 1).
- **PREVIOUSLY DID NOT, NOW DOES address the photon-720° compatibility question** — see §6.5 above. Closes sub-item 3 of clm-0ktpcn's strengthen-by list via the FM extended-defect requirement + Hopf-fibration projection argument (2026-05-25 Phase 2 sub-item 3).
- **Does NOT** address the topological-protection question (real-space-trivially-knotted vs phase-space-winding-as-protection) — that is closed in the protection-mechanism leaf [phase-locked-topological-thread.md](../../../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md) (clm-zuf7g1), which provides the K4-TLM empirical demonstration that the (2,3) phase-space winding is protected against continuous deformations below the Schwinger pair-creation threshold; clm-unk0bd's depends-on graph wires this in (2026-05-25 Phase 2 sub-item 4).

## §9 Coordinate-system discipline

Per `phase-space-coordinate-check` discipline: this derivation lives in **real-space coordinates** (the FM kink is on the extended unknot defect embedded in the 3D K4 substrate; the Cosserat micro-rotational DOF is per-node real-space rotation). The (2,3) winding pattern in [ch8-alpha-golden-torus.md](../../../vol1/ch8-alpha-golden-torus.md) regime (c) lives in **phase-space coordinates** (Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$). These are different coordinate systems for different aspects of the same electron soliton; the FM mechanism establishes the real-space $SU(2)$ structure, the (2,3) winding establishes the phase-space topology that produces the Golden Torus geometry.

## §10 Source

This derivation distills the work in `research/_archive/L3_electron_soliton/23_step2_spin_half_from_k4.md` (the K4-native FM-on-extended-unknot derivation with gyroscopic-isomorphism numerical anchor) and promotes it to a canonical KB leaf per `ave-prereg` Phase 0 corpus survey 2026-05-25 (which identified doc 23 as the strongest existing derivation, with the KB asserting-by-import only at spin-half-paradox.md).

## Cross-references

- **Canonical KB anchors:**
  - [spin-half-paradox](../../appendices/app-b-paradoxes/spin-half-paradox.md) — high-level resolution position (clm-salw2h co-host)
  - [spin-gyroscopic-isomorphism](spin-gyroscopic-isomorphism.md) — numerical anchor leaf (clm-salw2h co-host)
  - [k4-rotation-group](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) §6 — group-theoretic chain $T = A_4 \to 2T \subset SU(2)$ (clm-rkisb8)
  - [electron-unknot](electron-unknot.md) — the $0_1$ unknot identification of the electron
  - [electron-identification](electron-identification.md) — canonical electron identification with spin-½ row
- **Translation:** [translation-qm](../../../common/translation-tables/translation-qm.md) — Spin ↔ Unknot chirality ↔ ±1/2 twist orientations
- **Standalone Golden Torus α derivation** (where this derivation feeds into regime (c) screening): [ch8-alpha-golden-torus](../../../vol1/ch8-alpha-golden-torus.md) regime (c) — "Spin-1/2 half-cover of the standard Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$" derivation now anchored here
- **Source:** [`research/_archive/L3_electron_soliton/23_step2_spin_half_from_k4.md`](../../../../../research/_archive/L3_electron_soliton/23_step2_spin_half_from_k4.md) — original K4-native derivation with full gyroscopic-isomorphism analysis
- **Numerical script:** [`src/scripts/vol_2_subatomic/simulate_gyroscopic_spin.py`](../../../../../src/scripts/vol_2_subatomic/simulate_gyroscopic_spin.py) — gyroscopic ≡ Pauli evolution at $10^{-8}$ deviation
- **Standard references:**
  - Finkelstein & Misner, *Some new conservation laws*, Annals of Physics 6:230 (1959) — original FM theorem
  - Hall, *The Theory of Groups* Ch 12 — tetrahedral group $T = A_4$
  - Standard $SU(2)$ representation theory — binary tetrahedral group $2T$ as discrete $SU(2)$ subgroup
