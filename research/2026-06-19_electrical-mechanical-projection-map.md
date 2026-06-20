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

Anchors re-grepped on branch tip `37c3cf20`. **Resolution status legend:**
`RESOLVED-by-unification` = the unified-network bookkeeping genuinely closes it;
`GENUINE-distinction` = a real physical distinction the corpus holds (do NOT collapse);
`OPEN` = an un-adjudicated fork awaiting Grant.

| # | Seam | file:line | Nature | Resolution status |
|---|------|-----------|--------|-------------------|
| 1 | **`Z_bulk = √2·Z_0` units mis-scope** — a bulk mechanical impedance was scoped against the EM reference `Z_0` (Ω) instead of its own ρc axis | fixed in #296 `c4632a1b`; the bookkeeping the network buys: `Z_mech = ξ_topo²·Z_elec`, `isomorphism.py:53` (`ohms_to_kinematic`, `:49`) | The **ONE genuine units artifact** — a domain-reference mis-scope, not a physics error | **RESOLVED** (units-conflation, fixed) |
| 2 | **EM ↔ mechanical = domain boundary needing a TRANSDUCER not a wire** — two ports in different units (Ω vs ρc) cannot be directly wired; the crossing requires an electro-mechanical change-of-reference | `device-circuit-models.md`:199–202 | **GENUINE** impedance-DOMAIN boundary; the transducer changes units, does not erase the boundary | **GENUINE-distinction** |
| 3 | **DEC-4 EM-as-bare-loss-port** — the EM channel modelled as a bare matched radiative loss-port (`Γ_EM=0`), NOT a coupled transducer; a proper coupled EM gives a DIFFERENT observable (the **loaded** Q) | prereg `DEC-4`, `2026-06-19_electron-Q-coupled-network_prereg.md`:115; solver header `graded_vacuum_network.py` (Stage-2 note, header lines ~16–23) | **GENUINE scoping choice** — the route-around is correct discipline until the transducer is ratified | **GENUINE-distinction** (scoping) |
| 4 | **`1.826 = √(10/3)` vs `2.582 = √2·√(10/3)` bulk/shear ratio** — the `√2` IS exactly the EM-photon `√(K/G)` reference compounded into a mechanical-shear ratio (confirmed to machine zero); both **α-free**, both **α-invariant** | result `2026-06-19_electron-Q-coupled-network_result.md`:112–142; solver `RATIO_BULK_SHEAR_MECH = √(10/3)` `graded_vacuum_network.py:122`, `RATIO_BULK_SHEAR_PHOTON = √2·√(10/3)` `:124` | **GENUINE α-free projection-split** — moves NO chord/echo bin, only the bulk/shear gap LOCATION; auditor LEAN = `1.826` channel-correct for two-mechanical-channels; frozen prereg `2.582` PRESERVED verbatim | **OPEN** (Grant pick pending) |
| 5 | **stability ⊥ interaction** — intrinsic Q→∞ (mechanical confinement, EM-port closed ⇒ Hermitian) is ORTHOGONAL to loaded Q=1/α (EM coupling). Mechanical owns the lifetime; electrical owns the coupling coefficient | `theorem-3-1-q-factor.md`:145 (Amendment), :153–154 (STABILITY/INTERACTION table) | **GENUINE** — the projection made into the right answer; `137` re-attributed to the LOADED/radiative Q, intrinsic Q is infinite/stable; **retracts NOTHING**, α stays echo | **GENUINE-distinction** |
| 6 | **charge = `[Q] ≡ [L]`** — the TKI bridge FOUNDATION (`clm-dfaiwj`, solidity 0.80, "ok to build on, see caveats") | `master-equation.md`:20 (two-3s orthogonality fence); claim `clm-dfaiwj` `vol1/claim-quality.md` | **GENUINE** — resolving it is a **category error**: CHARGE-3 (Cosserat micro-rotation) ⊥ MASS-3 (A1 dilatation), never one `(V_inc,V_ref)` phasor (genesis-24 double-count guard) | **GENUINE-distinction** (foundation) |
| 7 | **M/J/Q refuted bijection** — the clean "3 hairs = 3 channels" map is REFUTED: J and Q CO-LOCATE in the Cosserat sector; EM is the matched **radiative PORT**, not an observable's home | `device-circuit-models.md`:163 (§6.4 header), :165, :178 | **GENUINE / honestly-held** — two independent triples exist, NO leaf cross-identifies them | **GENUINE-distinction** |

**Seam-1 naming note (verify-before-cite).** The reverse converter in `isomorphism.py`
is named **`mechanical_to_electrical`** (`:79`), with `impedance_electrical_to_mechanical`
(`:79`/alias of `ohms_to_kinematic` at `:70`) on the forward side — there is **no
function literally named `kinematic_to_ohms`** on the branch tip. Cite
`ohms_to_kinematic` (`:49`) / `mechanical_to_electrical` (`:79`) by their actual names.

**Seam-1/5 leak-anchor note (verify-before-cite).** The `|Γ_EM|² = 1 − α` radiative-leak
RETURN is at `cvr_model.py:169` (`return 1.0 - alpha`); `:161` is the `def gamma_mag_sq_leak`
line. Existing #297 docs that cite `:161` are pointing at the function head; the *return
relation* is `:169`.

## TKI bridge state

The Topo-Kinematic Isomorphism (Axiom 2, `clm-dfaiwj`) is the candidate
electro-mechanical transducer that would sit on the EM↔mechanical seam (seam 2). Its
implementation state:

- **Partially implemented as a unit-conversion dictionary.** `isomorphism.py` exposes
  `ohms_to_kinematic` (`:49`, `Z_mech = ξ_topo² · Z_elec`), `mechanical_to_electrical`
  (`:79`), `charge_to_length`/`length_to_charge` (`:19`/`:34`), and
  `vector_potential_to_mass_flow` (`:88`). These are **dimensional conversion functions**
  only.
- **NOT wired into any compute path** as the `def-tk1xfm` gain-1 transformer. No solver
  or eigensolve imports these to *couple* the EM port to the mechanical channels — the
  Build-A solver explicitly routes AROUND it (DEC-4, EM-as-bare-loss-port).
- **NOT ratified.** `def-tk1xfm` is `status:proposed`, awaiting auditor + Grant
  ratification.

### WIRING GATE (must clear BEFORE `def-tk1xfm` is ever wired into a compute path)

Two preconditions, both currently UNMET:

1. **`def-tk1xfm` must move `proposed → SOLID`** (Grant ratify). Until then it is a
   candidate, not an adjudicated wire.
2. **The ceiling must be ported into `isomorphism.py`'s docstring.** The strength
   ceiling — *"identity-by-translation, NOT a derivation"* (the lossless / gain-1 /
   pole-less bound; the `translation-circuit.md:660` piezo over-claim guard) — is
   **CONFIRMED ABSENT** from the module today. The `isomorphism.py` module docstring
   (lines 1–14) says only *"This module provides exact dimensional conversion functions
   between electrical and mechanical domains."* — it states the dimensional identity but
   carries **no** "not-a-derivation / no-pole / no-new-store" caveat. A future agent
   reading the module could mistake the gain-1 unit dictionary for a derived coupling
   mechanism. Porting the ceiling into the docstring is a hard precondition of wiring.

**Until both clear, DEC-4's route-around (EM-as-bare-loss-port) is the correct
discipline** — not a workaround to be eliminated. Wiring an un-ratified, ceiling-free
transducer into the compute path would silently convert a units-bookkeeping identity
into an apparent derivation (the seductive-unification trap, manufacturing a phantom α).

## #39 implication

*(skeleton — filled per commit)*
