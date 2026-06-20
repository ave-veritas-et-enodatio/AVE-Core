# Electrical-vs-Mechanical Projection-Conflation Map

> **Tracked artifact** for PR #297 (`analysis/2026-06-19-electron-Q-coupled-network`).
> Scope: catalogue every seam where an electrical (Ω, EM) quantity and a mechanical
> (ρc, bulk/shear) quantity get projected onto each other in the electron-Q
> coupled-network work, and tag each by resolution status. **This is a HYGIENE map,
> not a derivation.** Created from the audit verdict; verify-before-cite walked on
> branch tip `37c3cf20` (anchors re-grepped 2026-06-19).

## Cluster verdict

**NOT one artifact to dissolve.** The cluster is **one fixed units-conflation
artifact + six genuine physical distinctions the corpus already holds.** The
seductive read — "electrical and mechanical are the same projection seen twice;
unify the network and α falls out" — is **wrong on two counts**:

1. **EM ↔ mechanical is a real impedance-DOMAIN boundary**, not a separation to
   resolve away. The two ports live in different units (Ω vs ρc); a domain-crossing
   coupling needs a **TRANSDUCER** (an electro-mechanical change-of-reference,
   the ξ_topo / TKI bridge — `Z_mech = ξ_topo² · Z_elec`), **NOT a direct wire**.
   The transducer **changes units**; it does not erase the boundary. This is the
   ONE place the cluster is genuinely a units-bookkeeping artifact (seam 1), and
   it is the ONE thing a unified network actually buys: consistent unit bookkeeping
   across the domain boundary.

2. **bulk ↔ shear is SAME-domain** (both mechanical, both ρ×speed). It couples
   through a **conserved** inter-grade Hamiltonian pair (`H_couple`, energize-lock,
   no-pump) — never a shared `(V_inc, V_ref)` phasor (the A1⊥T2 fence). This is a
   genuine intra-mechanical coupling problem, distinct in kind from the EM↔mechanical
   domain crossing.

**What the unification buys: HYGIENE, not a derivation.** Drawing the vacuum as one
wired three-channel network (EM / shear / bulk) with a transducer on the EM port is a
**CONSISTENCY re-expression** of the already-canonical three-impedance law — it makes
the unit bookkeeping honest and one-place. It does **NOT** derive α and it supplies
**NO new energy store**: the TKI-transformer (`def-tk1xfm`) is **lossless, gain-1,
pole-less** by its own ceiling — it transduces units, it does not host a pole, a Q, or
a coupling mechanism (those live in the resonator `H(s)`, not the transformer).

**α STAYS ECHO** (value level). The α→2α invariance proof in the Build-A result
(`|dQ/Q| = 2×10⁻¹⁰`) is the load-bearing demonstration that there is NO α-leak in the
mechanical network. Nothing in this map moves any chord/echo bin.

**THE TRAP** to guard against is the inverse of the seductive read: **collapsing the
six genuine distinctions** into "one projection artifact." Erasing the EM↔mechanical
domain boundary, or co-locating the two "3"s, or re-opening the refuted M/J/Q bijection,
would each manufacture a phantom unification. Every seam below is tagged by resolution
status precisely so the genuine distinctions are not silently dissolved.

## The 7-seam table

*(skeleton — filled per commit)*

## TKI bridge state

*(skeleton — filled per commit)*

## #39 implication

*(skeleton — filled per commit)*
