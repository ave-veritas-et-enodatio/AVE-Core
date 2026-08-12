# The A₁ common mode's continuum image — full derivation, circuit reading, and audit targets (2026-08-12)

**Class:** research / derivation. **Grade: UN-AUDITED, single-session analytic.** Written to be
audited: every step is numbered, every input is named as DERIVED / GEOMETRIC-INPUT / CANON-INPUT,
and §7 lists the claims to attack in the order they carry weight. **Mints nothing. Edits no leaf,
axiom, register, ruling, or engine file. Moves no solidity. Rules nothing.**

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

For any coordination whose bond directions sum to zero — **GEOMETRIC-INPUT G1: Σᵢ d̂ᵢ = 0**, true
for the tetrahedral z = 4 set and for a planar set of three at 120° — this gives

  **A₁ ≡ 0, identically, for every displacement field.**

So under reading (a) the common mode does not exist. Canon carries it as a live mode with a
scattering eigenvalue of +1 (§5). **Reading (a) is excluded**, and with it the intuition that the
common mode "moves the node": it cannot, by symmetry. *(This is the same fact that makes A₁
orthogonal to the T₂ translation triplet.)*

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

## §4 — STEP 3: THE COORDINATION TENSOR, BY CARRIER [DERIVED, on GEOMETRIC-INPUT]

**Case A — an isotropic direction set (spherical 2-design).** Isotropy forces M ∝ I; the trace
identity fixes the constant:

  **M = (N/3) I**  ⇒  M : ∇u = (N/3) tr(∇u) = (N/3) θ,  θ ≡ ∇·u.

  **Σᵢ aᵢ = (N ℓ / 3) · θ.**   … (2)

**GEOMETRIC-INPUT G2:** the tetrahedral 4-direction set is isotropic (a spherical 2-design). For
**z = 4**: M = (4/3) I and **A₁ ∝ (4ℓ/3) θ**.

**Case B — a planar set of three at 120°, plane normal n̂.** The set spans only the plane, so M is
proportional to the in-plane projector (**I** − **n̂**⊗**n̂**); the trace identity (tr = N, and the
projector has trace 2) fixes the constant:

  **M = (N/2)(I − n̂ ⊗ n̂)**  ⇒  M : ∇u = (N/2)( θ − n̂·∇u·n̂ ).

  **Σᵢ aᵢ = (N ℓ / 2)( θ − n̂·∇u·n̂ ).**   … (3)

**GEOMETRIC-INPUT G3 (load-bearing, audit first):** the srs / Laves (K4-graph) net is
3-coordinated with its three bonds **coplanar at 120°** at every vertex. For **z = 3**:
M = (3/2)(I − n̂n̂) and **A₁ ∝ (3ℓ/2)(θ − n̂·∇u·n̂)** — the **in-plane dilatation only**. The
out-of-plane direction is untouched by an in-phase stretch, and full θ is recovered only after
averaging **n̂**⊗**n̂** over sublattices with differently-oriented normals (⟨n̂n̂⟩ = I/3 for an
isotropic distribution of normals restores M = I).

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

**The shunt-selectivity theorem [DERIVED, and this is the physical content].** A differential
(T₂ / E) pattern has Σᵢ aᵢ = 0 by construction, hence **zero net current into the node**, hence it
does not drive any shunt element there. Therefore:

  **The node's intrinsic LC tank (Axiom 1) is driven by the common mode and by nothing else.**

## §6 — STEP 5: WHAT THE RESULT SAYS

**5.1 The fork resolves; both arms were half right.** A₁ is the trivial irrep, so its continuum
image must be a **scalar**. `u∥` is a vector component and cannot be the image of a trivial irrep;
**θ = ∇·u is a scalar and is** — Eq. (2)/(3). So `k4-port-irrep-decomposition.md:25` names the right
*sector* (the u sector, not a separate field) and the wrong *object*; it should read θ = ∇·u.
And Eq. (5) says the node potential *is* the A₁ combination, so
`03_pin_port_configuration.tex:56`'s "K4 port voltage" and the KCL construction are the same
statement in the circuit dialect. **V ↔ θ is the TKI bridge for this mode. Canon never wrote it.**

**5.2 The DC/AC split falls out of the circuit.** At DC the shunt capacitance is an open: the
common mode's net flux cannot pass and accumulates as a potential — an elliptic/Poisson solve, which
is Axiom 5 clause G. At AC the tank has finite impedance and the common mode drives it — which is
the small-signal analysis Axiom 5 (c1) declares owed. **One circuit, two regimes, and the axiom's
standing debt is the second one.**

**5.3 The sharpened problem (this is not a resolution).** If A₁ ↔ θ = ∇·u mechanically, and TKI maps
u ↔ A, then the same mode maps to ∇·A electrically — while canon states *"∇·u propagates; ∇·A is
gauge"* (`vocabulary-register.md:870`, SOLID). One mode cannot be both dynamical and gauge. Canon's
escape is `def-uatk1s`'s declared constitutive-stencil exception — TKI breaking in exactly this
channel — whose justification is ½K(∇·u)² **at K = 2G**, the operating-point readout R52
reclassified. **The one place the isomorphism is licensed to break rests on the number R52
demoted.** Recorded as the live consequence; not adjudicated here.

**5.4 ★ The carrier finding.** The decomposition **A₁ ⊕ T₂ = 1 + 3** is a **z = 4 tetrahedral**
result. Axiom 1 (`eq_axiom_1.tex:37`, D1-ratified at `:43`) names **z = 3 srs** as the production
carrier and re-tags z = 4 diamond a *"non-canonical instrument"*, with the engine migration
*"chartered but not yet executed"*. On z = 3 the port space is 3-dimensional and splits as
**A₁ ⊕ E = 1 + 2**, not 1 + 3 — and by Eq. (3) the common mode's continuum image is the *in-plane*
dilatation per node, isotropic only after sublattice averaging. **Three standing artifacts lean on
the 1+3 form:** #957's refutation of M1 (the "four ports, so a three-wire analogy is wrong"
argument), R51 §1.2's common-mode-tank carve, and #962's walk. None is *overturned* by this — the
common mode exists on any coordination, being the trivial irrep — but each is stated on the
engine's superseded carrier while the axiom names another. **Routed, not fixed.**

## §7 — AUDIT TARGETS, IN ORDER OF LOAD

1. **★ G3 — is srs 3-coordination coplanar at 120°?** This is the single geometric input the z = 3
   result stands on. If the three bonds are *not* coplanar, Eq. (3) is wrong and the z = 3 image may
   be isotropic after all. **Attack this first.**
2. **The irrep count on z = 3.** Does the 3-port amplitude space at an srs vertex decompose as
   1 + 2 under the actual site symmetry? Name the site group from the space group `I4₁32` at the
   Wyckoff position the corpus uses, and decompose properly rather than by analogy.
3. **G1 and G2** — Σd̂ᵢ = 0 and the tetrahedral set's isotropy (spherical-2-design property).
   Standard, but they are inputs, not results.
4. **Eq. (1) and the trace identity** — the continuum expansion and the prefactor fixing. Check the
   O(ℓ²) term is genuinely subleading for the intended regime and that no chirality term enters at
   first order on a *chiral* net.
5. **Eq. (4)/(5) against the corpus's own TLM convention.** The shunt-node scattering matrix and the
   node-voltage relation are standard TLM, but the corpus may normalise V_inc differently; verify
   against `kirchhoff-network-method.md` and `vacuum-varactor-scatter-operator.md:64-65` rather than
   against textbook TLM.
6. **The shunt-selectivity theorem.** Σaᵢ = 0 ⇒ no net current ⇒ no shunt drive. Check whether the
   corpus's node model has any element a differential mode *can* see (a series element, a
   couple-stress term, a chiral cross-coupling) that would break the selectivity.
7. **§5.4's carrier claim** — that the 1+3 decomposition is z = 4 and the ratified carrier is z = 3.
   Verify the D1 ruling's scope and whether `k4-port-irrep-decomposition.md` declares its carrier.
8. **Contradicts-hunt.** Find anything in canon that *contradicts* V ↔ θ for this mode, or that
   already states it. A result that reconciles two canonical arms is exactly the kind to distrust.

## §8 — WHAT THIS DOES NOT CLAIM

It does not adjudicate FORK-1 (momentum vs configuration), does not rule on the 6-vs-7 enumeration,
does not touch `def-l0ngdu`'s gauge statement, does not value or re-derive K, and does not license
any change to the engine. §5.3 and §5.4 are **routed consequences**, not verdicts. The whole
document is single-session analytic work with no independent reader, and §7 exists because that is
the appropriate confidence level for it.
