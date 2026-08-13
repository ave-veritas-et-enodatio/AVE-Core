# The A₁ common mode's continuum image — full derivation, circuit reading, and audit targets (2026-08-12)

**Class:** research / derivation. **Grade: ADVERSARIALLY AUDITED 2026-08-12 (PR #963 review) —
one novelty claim RETRACTED, one theorem NARROWED on two counts, one sector cross-wire REPAIRED;
the load-bearing geometry survived exactly.** Every step is numbered, every input is named as
DERIVED / GEOMETRIC-INPUT / CANON-INPUT / CANON-INPUT-with-test, and §7 lists the claims that were
attacked, in the order they carry weight, each now stamped with its audit disposition. **Mints
nothing. Edits no leaf, axiom, register, ruling, or engine file. Moves no solidity. Rules nothing.**

**★ WHAT THIS DOCUMENT CONTRIBUTES — re-scoped 2026-08-12 post-audit.** Three things, each verified
independently against the corpus's own generator (`ave.core.chiral_lattice`), and nothing else:

1. **The `z = 3` coordination-tensor evaluation:** `M ≡ Σᵢ d̂ᵢ⊗d̂ᵢ = (3/2)(I − n̂n̂)` at *every* srs
   vertex — eigenvalues `{0, 3/2, 3/2}`, all 512 nodes of an `L = 4` build (§4, Case B).
2. **The per-node A₁ amplitude is therefore the IN-PLANE dilatation** `(θ − n̂·∇u·n̂)`, **not** `θ`.
   Full `θ` is recovered only after averaging over a complete ⟨111⟩ normal orbit — **≥ 4 nodes, a
   supercell, not a node** (§4, G3). Scoped to `kℓ ≪ 1` (§3, REGIME).
3. **The carrier mismatch:** `A₁ ⊕ T₂ = 1 + 3` is a `z = 4` / `T_d` result while D1 ratifies `z = 3`,
   on which the split is `A₁ ⊕ E = 1 + 2` (§5.4) — plus the internal `:13`-vs-`:41` contradiction
   inside `k4-port-irrep-decomposition.md` itself.

**Everything else here is a re-derivation of standing canon, not an addition to it.** §2's Step 1 is
`node-scattering-multiplicity.md:100-106` (with engine code and a regression marker); §5's Eq.
(4)/(5) is `vacuum-varactor-scatter-operator.md:57,64-65,69`; and **§6 5.1's `V ↔ θ` novelty claim is
RETRACTED — see the 🔴 block there.** Two consequences are routed, not ruled: the `aᵢ`-referent gap
(§6a, a STUCK-POINT for Grant) and the 6-vs-7 mode enumeration (§6b).

**Question (the open fork of the 2026-08-12 layer-carve walk record, #962 §5):** is the A₁ common
mode's continuum image the longitudinal displacement `u∥`, or the node potential `V`? Canon asserts
both and reconciles neither — `k4-port-irrep-decomposition.md:25` ("A₁ Cosserat mapping |
Translational u (isotropic, longitudinal)") versus `kirchhoff-network-method.md:18,34-41` and
`vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex:56` ("K4 port voltage (pressure /
stored potential)").

---

## §1 — SETUP AND NOTATION

Node `n` at position **x**ₙ. It has `N` neighbours at **x**ₙ + ℓ **d̂**ᵢ, i = 1…N, with |**d̂**ᵢ| = 1
and ℓ = ℓ_node the lattice pitch. **u**(**x**) is the displacement field. Port amplitudes are
written aᵢ, one per bond. The A₁ (common / trivial-irrep) combination is the in-phase sum,
normalised as convenient:

  A₁ ≡ (1/√N) Σᵢ aᵢ.

Two candidate readings of aᵢ are on the table:

  **(a)** aᵢ = **u**(n) · **d̂**ᵢ   — the node's own displacement projected on the bond
  **(b)** aᵢ = [**u**(n+i) − **u**(n)] · **d̂**ᵢ   — the bond *stretch*

## §2 — STEP 1: READING (a) IS EXCLUDED [DERIVED]

  A₁ = (1/√N) **u**(n) · Σᵢ **d̂**ᵢ.

For any coordination whose bond directions sum to zero — **CANON-INPUT-with-test G1: Σᵢ d̂ᵢ = 0**
(*retagged 2026-08-12: this is not a free geometric input, it is written into the engine —*
`src/ave/solvers/node_scattering_multiplicity.py:315`, *"a force-balanced node: Σ_p bond_unit = 0"*;
audit-reproduced as `|Σ d̂| = 0.0` exactly on both nets) — this gives

  **A₁ ≡ 0, identically, for every displacement field.**

So under reading (a) the common mode does not exist. Canon carries it as a live mode with a
scattering eigenvalue of +1 (§5). **Reading (a) is excluded**, and with it the intuition that the
common mode "moves the node": it cannot, by symmetry. *(This is the same fact that makes A₁
orthogonal to the T₂ translation triplet.)*

**⚠ NOT NEW — this step re-derives standing canon (audit finding, 2026-08-12).**
`manuscript/ave-kb/vol9/ch3-pin-port-configuration/node-scattering-multiplicity.md:100-106` already
carries it: *"The longitudinal A1 dilatation **scalar IS the $+1$ common mode** … the $+1$
common-mode port-vector projects to a real-space **scalar** … with **zero** real-space vector grade
on a force-balanced node"* — with engine code
(`src/ave/solvers/node_scattering_multiplicity.py:305-317`) and a regression marker
(`src/tests/test_node_scattering_multiplicity.py::test_fork_a_verdict_is_invariant_under_bond_unit_scramble`,
cited at that leaf `:112`). Canon separates translation from breathing at the datasheet too:
`03_pin_port_configuration.tex:54` assigns translational **u** to *"part of $A_1 \oplus T_2$ valence;
**couples $T_2$**"*. **The corpus may not cite §2 as a new result.**

## §3 — STEP 2: EXPAND READING (b) [DERIVED]

Taylor-expand the neighbour displacement to first order in ℓ:

  **u**(n+i) = **u**(n) + ℓ (**d̂**ᵢ · ∇) **u** + O(ℓ²).

Then

  aᵢ = ℓ (**d̂**ᵢ · ∇)**u** · **d̂**ᵢ = ℓ d̂ᵢ_j d̂ᵢ_k ∂_j u_k,

and summing,

  **Σᵢ aᵢ = ℓ M : ∇u,  with  M ≡ Σᵢ d̂ᵢ ⊗ d̂ᵢ.**   … (1)

`M` is the **coordination tensor**. Everything below is the evaluation of `M`.

**Trace identity [DERIVED]:** tr(M) = Σᵢ |**d̂**ᵢ|² = **N**, for any coordination whatsoever. This is
the check that fixes the prefactor in both cases below.

**★ REGIME — this is a long-wavelength identification, and the correction is NOT symmetry-forbidden
[DERIVED; added 2026-08-12 post-audit].** The second-order term of the same expansion is
`(ℓ²/2) T : ∇∇u` with the **third moment** `T ≡ Σᵢ d̂ᵢ⊗d̂ᵢ⊗d̂ᵢ`. `T` does **not** vanish at a node:
measured on the corpus's own generator, `max|T| = 0.354` (srs `z = 3`, `L = 4`, 512 nodes) and
`max|T| = 0.770` (**diamond `z = 4`** — the *larger* correction of the two). So:

  **A₁ ↔ θ holds for `kℓ ≪ 1` and degrades toward the zone edge, where the non-vanishing third
  moment is the leading correction.** `|O(ℓ²)/O(ℓ)|` scales linearly in `ℓ`.

This matters because the corpus's own zone-edge work
(`research/2026-06-16_k4-zone-edge-nyquist-settle_prereg_FROZEN.md`) lives exactly where this
expansion fails. What *does* vanish is the **net-averaged** third moment: `max|⟨T⟩| = 2.96e−18` over
the srs net, so nothing at second order survives sublattice averaging either.

**No chirality enters Σᵢ aᵢ, and the reason is stronger than symmetry of `M` [DERIVED].** Two
independent facts:

- `M` is symmetric, so `M : ∇u` contracts only the **symmetric** part of `∇u`; the rigid-rotation
  part drops identically.
- **Cosserat microrotation contributes exactly zero to an axial stretch:** for a microrotation `φ`,
  the induced bond-end displacement is `φ × d̂`, and

    **(φ × d̂) · d̂ ≡ 0**   — identically, for *any* `φ` and *any* `d̂`.

  This is **coordination-independent** and does not appeal to any property of the net. It — not the
  symmetry of `M` — is the actual reason the chirality worry on a *chiral* carrier is void.

## §4 — STEP 3: THE COORDINATION TENSOR, BY CARRIER [DERIVED, on GEOMETRIC-INPUT + CANON-INPUT-with-test]

**Case A — an isotropic direction set (spherical 2-design).** Isotropy forces M ∝ I; the trace
identity fixes the constant:

  **M = (N/3) I**  ⇒  M : ∇u = (N/3) tr(∇u) = (N/3) θ,  θ ≡ ∇·u.

  **Σᵢ aᵢ = (N ℓ / 3) · θ.**   … (2)

**CANON-INPUT-with-test G2** *(retagged 2026-08-12: also not a free input)***:** the tetrahedral
4-direction set is isotropic (a spherical 2-design). Canon states it with an executable keeper —
`manuscript/ave-kb/vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md:101`: *"The
tetrahedral 2nd-moment $\sum_b(\hat q\!\cdot\!\hat b)^2 = 4/3$ for EVERY direction
(`test_tetrahedral_second_moment_isotropic`)"*. For **z = 4**: M = (4/3) I (audit-reproduced:
eigenvalues `{4/3, 4/3, 4/3}`) and **A₁ ∝ (4ℓ/3) θ**.

**Case B — a planar set of three at 120°, plane normal n̂.** The set spans only the plane, so M is
proportional to the in-plane projector (**I** − **n̂**⊗**n̂**); the trace identity (tr = N, and the
projector has trace 2) fixes the constant:

  **M = (N/2)(I − n̂ ⊗ n̂)**  ⇒  M : ∇u = (N/2)( θ − n̂·∇u·n̂ ).

  **Σᵢ aᵢ = (N ℓ / 2)( θ − n̂·∇u·n̂ ).**   … (3)

**GEOMETRIC-INPUT G3 (load-bearing; ✅ AUDIT-CONFIRMED EXACTLY 2026-08-12):** the srs / Laves
(K4-graph) net is 3-coordinated with its three bonds **coplanar at 120°** at every vertex. Measured
on `ave.core.chiral_lattice.build_srs_net`, **both enantiomorphs** (`right` and `left`), all 512
nodes of an `L = 4` build: pairwise bond angle `min = max = 120.000000°`, `|d̂₁×d̂₂·d̂₃| ≤ 2.3e−17`
(machine zero), direction-matrix rank `2` at every node (never 3). For **z = 3**:
M = (3/2)(I − n̂n̂) — reproduced as per-node eigenvalues `{0, 1.5, 1.5}` at every vertex, identical
in both enantiomorphs — and **A₁ ∝ (3ℓ/2)(θ − n̂·∇u·n̂)** — the **in-plane dilatation only**. The
out-of-plane direction is untouched by an in-phase stretch.

**The averaging clause, with the exact structure (corrected 2026-08-12 post-audit — the previous
wording said "an isotropic distribution of normals", which is loose).** The srs has **exactly four
distinct plane-normal axes** — the four ⟨111⟩ cube diagonals, **128 nodes each** in an `L = 4` build
— and those four axes form a **spherical 2-design**: `⟨n̂ ⊗ n̂⟩ = I/3` **exactly** (measured
`max|⟨n̂n̂⟩ − I/3| = 9.4e−16`; `⟨M⟩ = I` to 1e-16). It is the same structure that makes G2 work, not
a statistical isotropy argument. The operational consequence:

  **θ is recovered only over a complete ⟨111⟩ normal orbit — ≥ 4 nodes, i.e. a supercell, not a
  node.** A single-node reading of the A₁ amplitude is the in-plane dilatation and nothing more.

## §5 — STEP 4: THE CIRCUIT [DERIVED, on CANON-INPUT]

**The junction.** `N` matched transmission lines of equal characteristic admittance meeting at a
lossless shunt node, with no additional shunt load, have the TLM scattering matrix

  **S = (2/N) J − I**,  J ≡ the all-ones matrix.   … (4)

**Eigenvalues [DERIVED]:** J has eigenvalue N on the all-ones vector and 0 on its orthogonal
complement (N−1 fold). Hence

  S eigenvalue on **A₁** (all-ones) = (2/N)·N − 1 = **+1**,
  S eigenvalue on the complement = (2/N)·0 − 1 = **−1**  (N−1 fold).

**CANON-INPUT C1 (consistency check, not an input to the result):** at N = 4 this is
S = (1/2)J − I with eigenvalues {+1, −1, −1, −1} — which is what
`k4-port-irrep-decomposition.md:11` states verbatim. The derivation reproduces canon's matrix.

**Circuit meaning [DERIVED]:** Γ = +1 is an **open**; Γ = −1 is a **short**. So at a *bare*
junction the common mode sees an open and the differential modes see a short.

**The node potential [DERIVED].** For the same junction, the node voltage is the in-phase average
of the incident waves,

  **V = (2/N) Σᵢ Vᵢ^inc**,   … (5)

i.e. **V is proportional to the A₁ combination and to nothing else.**

**The shunt-selectivity theorem [DERIVED — NARROWED 2026-08-12 post-audit; the previous statement
is struck below].**

  ~~A differential (T₂ / E) pattern has Σᵢ aᵢ = 0 by construction, hence zero net current into the
  node, hence it does not drive any shunt element there. Therefore: the node's intrinsic LC tank
  (Axiom 1) is driven by the common mode and by nothing else.~~

**🔴 STRUCK 2026-08-12 (PR #963 adversarial audit) — two independent defects, one of them a sector
cross-wire.**

- **(a) SECTOR CROSS-WIRE.** "The node's intrinsic LC tank (Axiom 1)" names the **wrong tank**.
  Axiom 1's intrinsic LC tank is defined at `manuscript/common_equations/eq_axiom_1.tex:37` as *"The
  intrinsic translation $\leftrightarrow$ E, rotation $\leftrightarrow$ B coupling makes every node a
  native LC oscillator"* — a **translation↔microrotation (E↔B) object**, which is **T₂'s home, not
  A₁'s**. Assigning it to the common mode cross-wires A₁ and T₂ against the standing fence at
  `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20` (*"TWO
  DISTINCT objects, orthogonal (A1 ⊥ T2)"*, Grant-ratified).
- **(b) IT IS AN UNSTRAINED / UNIFORM-ADMITTANCE RESULT, and canon's own operator is the general
  case.** With per-port admittances `Yᵢ` — canon's varactor form,
  `vacuum-varactor-scatter-operator.md:71`, `S_{ij} = 2Y_j/Σ_k Y_k − δ_{ij}` — the all-ones vector
  stays the `+1` eigenvector, but the `−1` eigenspace becomes the **Y-weighted** zero-sum space
  `{a : y·a = 0}`, **not** `{a : Σᵢ aᵢ = 0}`. A geometrically-differential pattern therefore **does**
  carry net current, and **does** drive the shunt, as soon as the node is strained (audit-computed at
  `n = 3` and `n = 4`: `Σaᵢ = 0` with `Y·a` nonzero; reproduced here at both `n`). Op14 saturation is
  exactly that case — and the engine says so: `src/ave/core/chiral_lattice.py:97-99`, *"`z_local` is
  reserved for the strained-vacuum (Op14) case; Phase-0 is unstrained (`z_local == 1.0`). Uniform
  per-port admittance cancels, so the unstrained form holds for any uniform `z_local`."* The struck
  theorem is a Phase-0 statement.
- **(c) The 6-DOF Cosserat node DOES carry a differential-sector storage element.** The
  microrotational inertia `I_ω` and couple-stress `G_c` give the gapped mode at
  `k4-port-irrep-decomposition.md:146` (*"mass-gap $4G_c/I_\omega$"*). "Does not drive **any** shunt
  element there" is false for the Cosserat node; it is true only for the scalar single-V junction.

**✅ THE NARROW STATEMENT THAT SURVIVES — and it is sharper and falsifiable [DERIVED].** Add a shunt
load `Y_sh` at the junction of `n` lines of equal characteristic admittance `Y`. Then
`S = (2Y/(nY + Y_sh)) J − I`, and:

  **Γ_common = (nY − Y_sh) / (nY + Y_sh),  while the differential eigenvalues stay exactly −1,
  independent of `Y_sh`.**

That is the whole of the selectivity content: **the common-mode reflection is entirely `Y_sh`-set;
the differential reflection cannot see `Y_sh` at all.** Verified numerically at `n = 3` and `n = 4`
for `Y_sh ∈ {0, 0.7, 3.3}` with `Y = 1` (e.g. `n = 3, Y_sh = 0.7` → eigenvalues
`{−1, −1, +0.621622}` against the predicted `Γ_common = 2.3/3.7 = 0.621622`), and independently
verified by the PR-#963 audit at `n = 3` and `n = 4`. The `Y_sh → 0` limit recovers Eq. (4).

**Scope, stated once:** uniform per-port admittance, unstrained operating point. Off that point,
(b) applies and selectivity is a `Y`-weighted statement, not a `Σaᵢ` statement.

**And the driven element is named correctly as:** the **A₁ bulk / dilatation compliance** — the
`½K(∇·u)²` bulk store on the A₁ channel — **not** Axiom 1's intrinsic (T₂ / E↔B) LC tank.

## §6 — STEP 5: WHAT THE RESULT SAYS

**5.1 The fork resolves; both arms were half right.** A₁ is the trivial irrep, so its continuum
image must be a **scalar**. `u∥` is a vector component and cannot be the image of a trivial irrep;
**θ = ∇·u is a scalar and is** — Eq. (2)/(3). So `k4-port-irrep-decomposition.md:25` names the right
*sector* (the u sector, not a separate field) and the wrong *object*; it should read θ = ∇·u.
And Eq. (5) says the node potential *is* the A₁ combination, so
`03_pin_port_configuration.tex:56`'s "K4 port voltage" and the KCL construction are the same
statement in the circuit dialect. ~~**V ↔ θ is the TKI bridge for this mode. Canon never wrote it.**~~

> ### 🔴 RETRACTED 2026-08-12 — "Canon never wrote it" is FALSE
>
> **What is retracted:** the sentence struck immediately above, in full — *"V ↔ θ is the TKI bridge
> for this mode. Canon never wrote it."* Retracted per A47 v11b: this is a **retraction, not a
> rewording**, and **no softer novelty claim is substituted in its place**. The mechanical content
> (A₁ ↔ θ = ∇·u, and the node potential being the A₁ combination) is **correct** — it is simply
> **already canon**, merged, and in one case Grant-ratified SOLID. The document does not own it and
> **the corpus may not cite this document for it.** Cite the five sites below instead.
>
> **The five canon sites, all grep-confirmed verbatim:**
>
> 1. **`research/2026-07-20_mechanical-commonmode-derivation_result.md:46`** (#761, merged
>    **23 days before this document**) — *"The decisive fact (`[derived]`): the A1-dilatation
>    `θ = ∇·u` is the **longitudinal polarization of the vector displacement field** … It is **NOT a
>    separate scalar DOF; it is a projection of the same 3-vector `u`**"*. This is §6 5.1's
>    conclusion, derived and merged first, and this document's phrasing *"the u sector, not a
>    separate field"* is near-verbatim that line.
> 2. **`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:26`** — the
>    2026-07-20 KEEP-BOTH sector-dynamics tag routed from #761, on the canonical A1 leaf: *"with
>    **u = the node displacement field**, θ = ∇·u is its volumetric/compression projection"*.
> 3. **`manuscript/ave-kb/common/vocabulary-register.md:589`** (`def-9a4f07`, id line `:584`) —
>    *"**dimension/type:** scalar potential grade $V$ (the A1 dilatation channel)"*. **The bridge is
>    the def-node's declared type.**
> 4. **`manuscript/ave-kb/common/vocabulary-register.md:594`** — the **★SHARPENED 2026-08-07** clause
>    adopting #761 §1.1 verbatim into the def-node, and recording *"Def-node half discharged;
>    canon-line half remains Grant's call."* — i.e. this section's own recommendation (*"`:25` should
>    read θ = ∇·u"*) is an **already-routed, half-discharged item**, not a new finding.
> 5. **`manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex:56`** — **this
>    document's own cited support** already carries the bridge in one table row: `Volumetric breathing
>    ($A_1$, radial dilation)` | `$A_1$ trivial rep (1-dim)` | `K4 port voltage (pressure / stored
>    potential)` | store `$V^2$`.
>
> Plus a receipted downstream consumer: `research/2026-08-07_a1-port-sourcing_result.md:184` quotes
> #761's line as a load-bearing receipt (*"R2 (#761 §1.1, verbatim `[sic]`)"*).
>
> **Why this happened, named plainly.** A single-session analytic document asserted "canon never
> wrote it" **without running the corpus sweep that A43 v2 requires before that assertion ships**.
> The sweep, run at audit, returned five hits in minutes. The failure is the missing sweep, not the
> physics.
>
> **What survives as this document's genuine contribution** is the header's three-item list — the
> `z = 3` coordination-tensor evaluation, the in-plane-dilatation consequence with its ⟨111⟩-orbit
> scope, and the carrier mismatch. Smaller and sharper than the original framing.

**5.2 The DC/AC split falls out of the circuit.** At DC the shunt capacitance is an open: the
common mode's net flux cannot pass and accumulates as a potential — an elliptic/Poisson solve, which
is Axiom 5 clause G. At AC the tank has finite impedance and the common mode drives it — which is
the small-signal analysis Axiom 5 (c1) declares owed. **One circuit, two regimes, and the axiom's
standing debt is the second one.**

**5.3 ~~The sharpened problem (this is not a resolution).~~ 🔴 REFUTED AND STRUCK 2026-08-12.**

  ~~If A₁ ↔ θ = ∇·u mechanically, and TKI maps u ↔ A, then the same mode maps to ∇·A electrically —
  while canon states "∇·u propagates; ∇·A is gauge" (`vocabulary-register.md:870`, SOLID). One mode
  cannot be both dynamical and gauge. Canon's escape is `def-uatk1s`'s declared constitutive-stencil
  exception — TKI breaking in exactly this channel — whose justification is ½K(∇·u)² **at K = 2G**,
  the operating-point readout R52 reclassified. **The one place the isomorphism is licensed to break
  rests on the number R52 demoted.**~~

**Both halves fail. There was no sharpened problem.**

- **The dilemma is false — it presupposes one field.** *"One mode cannot be both dynamical and
  gauge"* only bites if `u` and `A` are the same field. They are not, and canon adjudicates it:
  `manuscript/ave-kb/common/vocabulary-register.md:882+` (`def-uatk1s`, **status SOLID, Grant-ratified
  2026-07-21**) — `u` and `A` are *"**COUNTERPART SECTOR VARIABLES** — isomorphic structure … **NOT
  one field**"*, differing in *"**constitutive stencil**"*: *"the longitudinal $\mathbf{u}_\parallel$
  carries the K-spring … the longitudinal $\mathbf{A}_\parallel$ has **no** restoring force
  (gauge)"*. There are two modes on two fields, not one mode wearing two hats. The
  constitutive-stencil clause is not an *escape* bolted on to rescue a crisis; it **is** the
  adjudicated content of the def-node.
- **The R52 hook is wrong on the facts.** The exception does not rest on the number R52 demoted.
  `research/2026-07-20_mechanical-commonmode-derivation_result.md:62` states it explicitly: *"only
  **`K ≠ 0`** (any nonzero bulk modulus) is load-bearing for the structural block below; the specific
  value `2G` is not."* R52's reclassification of `K = 2G` as an operating-point readout therefore
  **does not touch** the constitutive-stencil exception, which needs only `K ≠ 0`.

**Net:** this document's §5.3 raised a non-problem and hung it on a non-dependency. Struck. Nothing
is routed from it.

**5.4 ★ The carrier finding.** The decomposition **A₁ ⊕ T₂ = 1 + 3** is a **z = 4 tetrahedral**
result. Axiom 1 (`eq_axiom_1.tex:37`, D1-ratified at `:43`) names **z = 3 srs** as the production
carrier and re-tags z = 4 diamond a *"non-canonical instrument"*, with the engine migration
*"chartered but not yet executed"*. On z = 3 the port space is 3-dimensional and splits as
**A₁ ⊕ E = 1 + 2**, not 1 + 3 — and by Eq. (3) the common mode's continuum image is the *in-plane*
dilatation per node, isotropic only after averaging a complete ⟨111⟩ normal orbit.

*(Audit-confirmed 2026-08-12 by brute-force site-group enumeration rather than by analogy: of the 24
proper cubic rotations about an srs vertex, exactly 6 map the periodic point set to itself, orders
`[1,2,2,2,3,3]` = **D₃ / "32"**, matching Wyckoff 8a of `I4₁32`; the induced port permutations are
the full `S₃`; character decomposition gives `⟨χ,χ⟩ = 2` and `⟨χ,triv⟩ = 1` ⇒ exactly two irreps,
one A₁ copy ⇒ **A₁ ⊕ E**. The `1 + 2` split itself is already canon —
`node-scattering-multiplicity.md:60`, *"**$S_3$**: $\{+1\times 1,\ -1\times 2\}$ → differential
multiplicity **2**"*; the **E label** is what is new.)*

**★ SHARPER THAN "stated on the superseded carrier": `k4-port-irrep-decomposition.md` CONTRADICTS
ITSELF** (added 2026-08-12 post-audit). The leaf declares **both** carriers, four lines apart in the
same section:

- `:13` — *"Here 'substrate' refers to the Chiral LC Network of Axiom 1, corresponding to a **chiral
  Laves K4** Cosserat crystal at the substrate level."* — a **z = 3** chiral declaration.
- `:41` — *"Under the tetrahedral point group $T_d$ (**the symmetry of the four tetrahedral
  neighbors on K4**)"* — an explicit **z = 4 / T_d** declaration.

A chiral Laves K4 net is z = 3 with proper-rotation site group D₃ (order 6, computed above). It
**cannot** carry `T_d`, which contains **reflections the chiral net lacks** — the corpus already
knows this and says so at `_orchestration/2026-06-20_carrier-sector-charter.md:97`: *"without the
**reflections the chiral I4₁32 net lacks**"*. The two lines cannot both be true.

**A second internal inconsistency, inside one volume:**
`manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex:52` heads its table column
`\textbf{$T_d$ irrep}` (z = 4) while `01_general_description.tex:18` in the **same volume** declares
*"the \texttt{srs} net ($z=3$, $I4_132$; the ratified production carrier per D1, Grant 2026-07-03)"*.

**Both are canon-edit items and need a Grant ruling. Surfaced, not resolved** — this document edits
no leaf and no tex.

### BLAST RADIUS — what actually consumes the 1 + 3 form

**🔴 The previous three-item list is STRUCK and REPLACED (2026-08-12 post-audit).** It was
*materially incomplete*, it named **no engine file at all**, and **two of its three items were
un-merged PRs** at the time of writing (#957 `analysis/dof-vs-port-ontology` and #962
`records/2026-08-12-walk-layer-carve`, both OPEN / `mergedAt` null) — i.e. it listed un-landed
records and omitted the landed ones.

  ~~**Three standing artifacts lean on the 1+3 form:** #957's refutation of M1 (the "four ports, so
  a three-wire analogy is wrong" argument), R51 §1.2's common-mode-tank carve, and #962's walk.~~

**The real enumeration.** **48 tracked files** carry an `A₁ ⊕ T₂` token (49 including this document;
count cross-checked two ways — `git grep -lE` and an independent `python3` pass over an explicit
`git ls-files` list of 5176 entries — per the standing grep-completeness discipline). The
load-bearing consumers, by class:

**Canonical KB leaves — the real blast radius:**
- `vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md:11,21,41,43,47`
  — the source leaf; `:47` hardcodes the basis `$(1,1,1,1)/2$`; claims `clm-j550uh`, `clm-9kd2t3`
- `vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md` (7 hits) — the photon identification
- `vol1/dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md` (2)
- `vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md:27` — *"the K4 diamond lattice has 4 ports per node"*
- `vol1/axioms-and-lattice/ch1-fundamental-axioms/cubic-k4-empirical-anisotropy.md`
- `vol1/operators-and-regimes/ch6-universal-operators/pairwise-potential.md`
- `common/port-register.md`, `common/trampoline-framework.md` (3), `common/vocabulary-register.md`,
  `common/translation-tables/translation-circuit.md` (2)
- `vol2/particle-physics/ch01-topological-matter/electron-identification.md`
- `vol9/ch1-general-description/index.md`, `vol9/ch3-pin-port-configuration/index.md`,
  `vol9/ch11-topological-characteristics/index.md`
- `.index/claims.jsonl`, `.index/depends-on.jsonl`, `vol1/claim-quality.md` (7), `vol9/claim-quality.md` (2)
- `vol1/dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md:33` — `$V_{\text{inc}}[i,n]$`
  ***"(4 ports per node)"***; and `clm-viawy9`'s own rationale (solidity **0.63**, build-band
  **input-only**) already names *"'per port' mode-counting (4 ports/node) … is asserted rather than
  worked"* as its solidity limiter

**Manuscript tex:** `vol_9_vacuum_datasheet/chapters/01_general_description.tex`,
`03_pin_port_configuration.tex` (2), `11_topological_characteristics.tex`,
`figures/k4_irrep_decomposition.tex`

**Engine / code — the struck list named none of these:**
- `src/scripts/vol_1_foundations/photon_propagation.py` (3 hits, `:51-60`, `:113-114`)
- `src/ave/core/k4_tlm.py:101-119` — `class K4Lattice3D`, whose docstring hard-codes the four
  tetrahedral connection vectors `p0…p3` as the node's port set (`:109-115`) — and `:64-93`,
  `build_scattering_matrix(z_local)`, which hard-codes `N = 4` and returns
  `S_ij = 0.5 − δ_ij`. This is the concrete 4-port implementation.
  *(⚠ CITE HYGIENE, flagged not fixed: the PR-#963 audit named this port set `_DIAMOND_PORTS` "in
  `k4_tlm.py`", and two corpus sites do the same — `vol9/ch18-experimental-prints/index.md:18`
  (*"engine `_DIAMOND_PORTS`"*) and `src/scripts/vol_1_foundations/generate_vacuum_lattice_stl.py:16`
  (*"Tetrahedral ports from ``_DIAMOND_PORTS`` (k4_tlm.py)"*). **The symbol `_DIAMOND_PORTS` is not
  in `k4_tlm.py`; it is at
  `src/ave/core/chiral_lattice.py:236`.** Same class of drift at
  `vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md:101`, which places
  `K4_BOND_DIRECTIONS` at `k4_tlm.py:110-117`; the symbol is at
  `src/ave/core/vacuum_node_circuit.py:72`. Three mis-attributions of the same port set to the wrong
  module — surfaced for an auditor-lane re-pin, not touched here.)*
- `src/ave/solvers/node_scattering_multiplicity.py` — the one solver already **carrier-parametric**
  (`S_n = (2/n)J − I` on both nets); **this is the migration-target pattern**

**Rulings:** `_orchestration/docket-entries/2026-08-12-ruling-r51-a1-two-objects-carve.md:30-31`
(uses `(1,1,1,1)/2` explicitly) and `:109` (*"1+3 bond-port split (A₁ dilatation ⊕ T₂ translations —
mass sector, this record)"*).

**Cite correction (2026-08-12):** the struck list cited *"R51 §1.2"*. **R51 has no §1.2** (its
sections are §1–§7); the common-mode-tank carve is **R51 §1 item 2, lines 26-35**.

**Nothing here is *overturned*** — the common mode exists on any coordination, being the trivial
irrep. But each consumer is written on the engine's superseded carrier while the axiom names
another. **Routed, not fixed.**

## §6a — ★ STUCK-POINT: `aᵢ` CHANGES REFERENT BETWEEN §4 AND §5

*(Added 2026-08-12 post-audit. §7 did not list this gap; it should have. Surfacing, not resolving —
this is a Grant question.)*

**The gap.** `aᵢ` is defined in §1 as *"Port amplitudes … one per bond"*, and **both** candidate
readings offered there are **mechanical**: `u·d̂` (reading a) and the bond **stretch** (reading b).
§4's Eq. (1)/(2)/(3) are entirely about the mechanical stretch. But §5's Eq. (5) is about
`Vᵢ^inc` — **incident wave voltages**. **The two are silently identified, and nothing in this
document justifies the identification.**

`V ↔ θ` composes only if `Vᵢ^inc ∝ stretchᵢ`. **No corpus line states that** — and canon's own
dictionary points the other way:

- `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md:19`
  — *"**Struts = Inductors ($L$):** Each edge carries a vector Current $I_{ij}$ (representing
  inductive flux or physical **lattice strain** between nodes)."* — strain maps to **current**, not
  to incident voltage.
- `:40` — `V_new = V_old + (Δt/C)(Σ I_in − Σ I_out)` — i.e. **dV/dt ∝ Σ(bond strains) ∝ θ**, which
  makes the node capacitor an **integrator of the strain current**, not a readout of the strain.

**★ THE ONE PLUMBER-PHYSICAL QUESTION FOR GRANT:**

> **At a vacuum node, is the node voltage the *compression itself*, or the *integral of the
> compression current flowing in*?**

**Candidate readings — both un-endorsed, deliberately:**

- **(i) `V ∝ θ`** — the node voltage **is** the dilatation. This is what §5/§6 5.1 assert. It
  requires the unstated identification `Vᵢ^inc ∝ stretchᵢ`.
- **(ii) `V ∝ ∫θ dt`** — canon's KCL reading (`kirchhoff-network-method.md:19,:40`): the node
  capacitor **integrates** the strain-current. Under (ii), `V ↔ θ` becomes `V ↔ ∫θ dt` and §5.2's
  DC/AC story is an integrator relation, not a proportionality.

**Honest note against this document's own interest:** **§5.2's DC-accumulation picture reads more
naturally under (ii) than under the (i) it asserts.** "The common mode's net flux cannot pass and
**accumulates** as a potential" is literally an integrator statement. The corpus does not resolve
this, and this document does not either.

**Attempts before stopping: 2** (searched the corpus TKI dictionary; searched for any explicit
port-amplitude ↔ bond-stretch identification). Neither returned a licensing line. Stopped and asked
rather than picking one.

## §6b — ★ ROUTED CONSEQUENCE: THIS DOCUMENT *DOES* BEAR ON THE 6-vs-7 ENUMERATION

*(Added 2026-08-12 post-audit. §8 previously disclaimed this. **The disclaimer was wrong** — §6 5.1
decides it — and §8 is corrected below. Routed to Grant; **not ruled here**.)*

**The chain, in three steps:**

1. `A₁ ↔ θ = ∇·u` — **canon**, per `research/2026-07-20_mechanical-commonmode-derivation_result.md:46`
   and `master-equation.md:26`.
2. That same canon line says what `θ` **is**: *"**NOT a separate scalar DOF; it is a projection of
   the same 3-vector `u`**"*.
3. **A projection of the 3 translational DOF is not a 7th kinematic mode.** So the seven-mode count
   — `3 translational + 3 microrotational + 1 volumetric breathing` — **double-counts**: the 7th is
   a projection of the first 3, not an independent coordinate.

**The one escape, named precisely.** The 7-count survives **iff** the node is an *extended object
with an independent internal radius coordinate* — a **bubble** whose radius can change while `∇·u`
of the node-centre field does not. That is a real, physical, and testable alternative; it is simply
not what the current cite supplies.

**⚠ THE SUPPORTING CITE DOES NOT SUPPLY IT — re-pin or vacate.**
`manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex:45` justifies *"seven
kinematic modes in total"* as *"canonical at `common/trampoline-framework.md`:200, the 7-mode bubble
compliance"*. But `trampoline-framework.md:200` reads *"Microrotation $\omega_z(r,t)$ develops —
bonds rotating about z-axis"* — step 4 of the **springs-realign mechanism walk** (`:196-202`), **not
a mode enumeration**. The phrase *"The 7-mode bubble compliance (3 translational + 3 rotational + 1
volumetric) lives here"* is at **`:204`**, and it is an **engine-location statement** about
`src/ave/topological/cosserat_field_3d.py` — it names the count, it does not derive an independent
radius coordinate. **The `:200` cite needs re-pinning or vacating**, and even re-pinned to `:204` it
does not establish the bubble escape.

**Recorded for Grant — this is his standing 6-vs-7 question.** The corpus's internal split, for the
record (audit-enumerated): **seven-counting = 2 chapters** (`03_pin_port_configuration.tex:42,45,59`;
`18_experimental_prints.tex:61,65,67-70,72,125`); **six-counting = 6 chapters** (ch1 `:18,43`,
ch6 `:29`, ch7 `:45`, ch9 `:18`, ch10 `:19`, ch11 `:7,23`). **ch5 is NOT one of them** — its "six"
hits are *"the six **views**"* / *"The six computed CVR views"* (`05_ac_electrical_characteristics.tex:121,189,207`),
six computed CVR views, not six per-node DOF; do not add it to this list.
No chapter *denies* the breathing mode — the six-counting chapters restate Axiom 1's
6 DOF and are silent, and the seven-counting chapters explicitly reconcile (*"6 spatial DOF **plus**
1 A1 breathing mode"*). **The contradiction is not between chapters; it is between the 7-count and
the canon identification `A₁ = ∇·u`.** *(Wording hazard for anyone grepping: `01_general_description.tex:18`
and `07_saturation_characteristics.tex:45` both say **"not a seventh spatial DOF"** about a
**different object** — the saturation state `A`, not the breathing mode.)*

**Not ruled here. Canon-edit item; needs Grant.**

## §7 — AUDIT TARGETS, IN ORDER OF LOAD — WITH DISPOSITIONS (audit run 2026-08-12, PR #963)

*(Targets as written pre-audit; each now carries the verdict the adversarial pass returned.)*

1. **★ G3 — is srs 3-coordination coplanar at 120°?** This is the single geometric input the z = 3
   result stands on. If the three bonds are *not* coplanar, Eq. (3) is wrong and the z = 3 image may
   be isotropic after all. **Attack this first.**
   → **✅ CONFIRMED EXACTLY.** 120.000000° and `|triple product| ≤ 2.3e−17` at all 512 nodes, both
   enantiomorphs; per-node `M` eigenvalues `{0, 3/2, 3/2}`. Eq. (3) verified by the audit against a
   random constant `∇u` (`Σaᵢ/ℓ`: measured `−0.7170112186` vs predicted `−0.7170112186`, diff 3.3e-16;
   diamond Eq. (2) likewise, diff 4.4e-16). Geometry re-run in this fix pass — see §9.
2. **The irrep count on z = 3.** Does the 3-port amplitude space at an srs vertex decompose as
   1 + 2 under the actual site symmetry? Name the site group from the space group `I4₁32` at the
   Wyckoff position the corpus uses, and decompose properly rather than by analogy.
   → **✅ CONFIRMED**, by brute-force stabilizer enumeration, not analogy: site group **D₃** (order
   6, Wyckoff 8a), full `S₃` port action, `⟨χ,χ⟩ = 2`, `⟨χ,triv⟩ = 1` ⇒ **A₁ ⊕ E**. *The 1+2 split
   is already canon (`node-scattering-multiplicity.md:60`); the **E label** is the new part.*
3. **G1 and G2** — Σd̂ᵢ = 0 and the tetrahedral set's isotropy (spherical-2-design property).
   Standard, but they are inputs, not results.
   → **✅ CONFIRMED**, and **RETAGGED**: both are **CANON-INPUT-with-test**, not free geometric
   inputs — `node_scattering_multiplicity.py:315` and
   `per-dof-vacuum-node-circuit.md:101` (`test_tetrahedral_second_moment_isotropic`). See §2 and §4.
4. **Eq. (1) and the trace identity** — the continuum expansion and the prefactor fixing. Check the
   O(ℓ²) term is genuinely subleading for the intended regime and that no chirality term enters at
   first order on a *chiral* net.
   → **Eq. (1) + tr(M) = N: ✅ CONFIRMED exactly** (audit, numeric against an exact quadratic
   displacement field: residual `−1.4e-17` srs, `+4.0e-17` diamond).
   → **O(ℓ²): ⚠ DOWNGRADED — scope was missing.** The third moment does **not** vanish at a node
   (`max|T| = 0.354` srs, `0.770` diamond); subleading only for `kℓ ≪ 1`. **Regime line added to §3.**
   → **Chirality: ✅ CONFIRMED**, and replaced with the stronger coordination-independent identity
   `(φ × d̂)·d̂ ≡ 0` (§3).
5. **Eq. (4)/(5) against the corpus's own TLM convention.** The shunt-node scattering matrix and the
   node-voltage relation are standard TLM, but the corpus may normalise V_inc differently; verify
   against `kirchhoff-network-method.md` and `vacuum-varactor-scatter-operator.md:64-65` rather than
   against textbook TLM.
   → **✅ CONFIRMED — the derivation reproduces canon rather than assuming it.**
   `vacuum-varactor-scatter-operator.md:57` (`S^bedrock_{ij} = 2/n − δ_{ij}`), `:64-65` (the shunt +
   KCL pair), `:69` (`V = 2Σ_j Y_j V_j^inc / Σ_k Y_k` → uniform-Y gives **exactly Eq. (5)**); third
   independent site `src/ave/core/chiral_lattice.py:81-104`.
6. **The shunt-selectivity theorem.** Σaᵢ = 0 ⇒ no net current ⇒ no shunt drive. Check whether the
   corpus's node model has any element a differential mode *can* see (a series element, a
   couple-stress term, a chiral cross-coupling) that would break the selectivity.
   → **🔴 DOWNGRADED on two independent counts, one of them a SECTOR CROSS-WIRE.** It named the
   wrong tank (Axiom 1's intrinsic LC tank is T₂'s E↔B object), and it is an unstrained /
   uniform-admittance result; the corpus node *does* carry a differential-sector store
   (`I_ω`, `G_c`; `k4-port-irrep-decomposition.md:146`). **Struck and replaced in §5** with the
   `Y_sh`-independence statement.
7. **§5.4's carrier claim** — that the 1+3 decomposition is z = 4 and the ratified carrier is z = 3.
   Verify the D1 ruling's scope and whether `k4-port-irrep-decomposition.md` declares its carrier.
   → **✅ CONFIRMED, and strengthened:** the leaf declares **both** carriers and **contradicts
   itself** (`:13` chiral Laves K4 = z = 3 vs `:41` `T_d` = z = 4). Blast-radius list **replaced**
   (the original three-item list was materially incomplete and two of its three items were un-merged
   PRs). See §5.4.
8. **Contradicts-hunt.** Find anything in canon that *contradicts* V ↔ θ for this mode, or that
   already states it. A result that reconciles two canonical arms is exactly the kind to distrust.
   → **🔴 ★ THE NOVELTY CLAIM IS REFUTED — five independent merged canon sites already state it.**
   **RETRACTED at §6 5.1.** Nothing *contradicts* V ↔ θ; the failure is the opposite one — the
   corpus wrote it first, and this document did not run the sweep before claiming otherwise.
9. *(unlisted, found at audit)* **`aᵢ` changes referent between §4 and §5.** → **STUCK-POINT, §6a.**
   This should have been target 0.

## §8 — WHAT THIS DOES NOT CLAIM

It does not adjudicate FORK-1 (momentum vs configuration), does not touch `def-l0ngdu`'s gauge
statement, does not value or re-derive K, and does not license any change to the engine. §5.4, §6a
and §6b are **routed consequences**, not verdicts. It edits no leaf, no axiom, no register, no
ruling and no engine file — including the `k4-port-irrep-decomposition.md:13`-vs-`:41` contradiction
and the vol-9 mode-count item, both of which are **canon-edit items needing a Grant ruling**.

**🔴 CORRECTED 2026-08-12 (post-audit).** This section previously read *"does not rule on the 6-vs-7
enumeration"*. **That disclaimer was wrong**: §6 5.1's identification `A₁ ↔ θ = ∇·u` — which is
canon, not this document's — **does** bear on the enumeration, because a projection of the 3
translational DOF is not a 7th kinematic mode. The consequence is now stated openly at §6b and
**routed to Grant**. It is still not *ruled* here. Disclaiming a consequence one's own result
produces is the failure mode this correction closes.

**Grade note.** §5.3's "sharpened problem" was **refuted and struck** — it was a false dilemma
resting on a non-dependency. The document was single-session analytic work with no independent
reader when §7 was written; it has since had one, and §7 now carries that reader's verdicts.

## §9 — METHOD AND RECEIPTS (added 2026-08-12 with the post-audit fix pass)

**What was actually run, and with what.** Every geometric number quoted in §3, §4 and §7 was
produced by **numpy** against the corpus's own generator — `ave.core.chiral_lattice.build_srs_net`
and `build_diamond_net`, imported **read-only**; no engine file was touched, no fixture was added.
Reproduced independently in this fix pass, `L = 4`:

```
srs   z=3, 512 nodes, BOTH enantiomorphs (identical to the digit):
                      bond angles min = max = 120.000000 deg ;  |d̂₁×d̂₂·d̂₃| ≤ 2.3e-17 ;  rank = 2
                      M eigenvalues {0, 1.5, 1.5} at EVERY node ;  |Σ d̂| = 0.0 ;
                      max|T| = 0.3535533906 ;  max|⟨T⟩| = 2.96e-18 ;
                      max|⟨n̂n̂⟩ − I/3| = 9.4e-16 ;  4 distinct ⟨111⟩ normal axes, 128 nodes each
diamond z=4,  16 nodes: M = (4/3)I ;  |Σ d̂| = 0.0 ;  max|T| = 0.7698003589
shunt-loaded junction  S = (2Y/(nY+Y_sh))J − I :
  n=3, Y=1, Y_sh=0.7 → eig {−1, −1, +0.621622},  Γ_common pred = 2.3/3.7 = 0.621622
  n=3, Y=1, Y_sh=3.3 → eig {−1, −1, −0.047619}   n=4, Y=1, Y_sh=3.3 → eig {−1,−1,−1, +0.095890}
nonuniform Y, Σaᵢ = 0 exactly → Y·a ≠ 0 at both n=3 and n=4 (the differential pattern DOES
  carry net current once per-port admittances differ)
```

**⚠ TOOLING HONESTY — no sympy verification is claimed for the series expansion.** The PR-#963 audit
reports that `sympy.series` returned unevaluated `Subs(Derivative(...))` objects that would not
simplify against `diff`, and that it therefore **switched to a direct numeric check against an exact
quadratic displacement field** `u(x) = Gᵀx + ½H:xx`. That is the check whose residuals (`−1.4e-17`
srs, `+4.0e-17` diamond) are quoted. **This document claims a numeric verification, not a symbolic
one.** The single exact-symbolic result claimed anywhere here is the algebraic identity
`(φ × d̂)·d̂ ≡ 0`, which is a one-line vector-triple-product fact and needs no CAS.

**Attribution.** The site-group brute force (24 proper cubic rotations, character decomposition),
the `Σaᵢ` vs Eq. (1)/(2)/(3) residual checks, the corpus-wide contradicts-hunt and the blast-radius
enumeration are the **PR-#963 adversarial audit's** work, re-verified here where the numbers are
quoted in the body. The coordination-tensor, third-moment, normal-orbit and shunt-eigenvalue numbers
in the block above were re-run in this fix pass and agree.

**Corpus-token count method.** The `A₁ ⊕ T₂` file count (48 excluding this document, 49 including)
was cross-checked **two ways** — `git grep -lE` and an independent `python3` pass over an explicit
`git ls-files` list of 5176 entries — per the standing discipline that a single grep engine's
"complete / all-sites" claim is not trustworthy on its own.
