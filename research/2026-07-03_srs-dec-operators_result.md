# RESULT — the srs DEC operator set (DEC MINI-ARC)

**Status:** DELIVERED — a valid ∂₂ is constructible on the srs girth-10 faces;
the ∂∂=0 identities hold at machine precision (exact integer for ∂₁∂₂); THE
THEOREM is stated with its scope box; the harmonic dimensions are (b0,b1,b2) =
(1, 3, over-complete). Minimal-2-complex **UNIQUENESS FAILS** on the full 10-ring
face set (a valid ∂₂ exists; a unique one is not forced — the honest partial).
**Classification (`consistency-vs-emergence`):** DERIVATION / INFRASTRUCTURE. This
is a mathematical (combinatorial-topology) result on the srs connect-map; ∂₁, ∂₂
are integer matrices carrying no physical constant. No emergence claim is minted.

**Charter:** Grant-chartered 2026-07-03, "iii) let's do it" — upgrade the just-
ratified cold-linear-static-local closure of the {∇×ω, ω} curl-coupling class from
"a property of an engineering-choice operator pair" to THEOREM grade for the entire
curl-coupling class.
**Branch:** `analysis/srs-dec-operators` (off `origin/main` @ `6b696c80`). NO self-merge.
**Module:** [`src/ave/topological/srs_dec.py`](../src/ave/topological/srs_dec.py).
**Tests:** [`src/tests/test_srs_dec_operators.py`](../src/tests/test_srs_dec_operators.py) — 14 gating keepers, ~0.5 s.

---

## §0. Prereg-lite (FROZEN intent — closure-discipline short note)

This is derivation/infrastructure, not an empirical bin test, so a short frozen
intent suffices (per closure-discipline). **What would count as failure:** *no
valid ∂₂ constructible on the srs 10-rings* — i.e. either (a) the girth-10 ring
set does not close ∂₁∂₂=0 under any consistent orientation, or (b) the resulting
H₁ is wrong (≠ the periodic-torus b₁), so the "complex" would be an artifact, not
the srs topology. Either would be **booked honestly** as a negative and the mini-
arc closed without a theorem. A *partial* result — "a valid ∂₂ exists on this face
subset but uniqueness fails" — was pre-declared a legitimate deliverable; do NOT
force false uniqueness.

**Outcome vs intent:** ∂₁∂₂=0 holds (exact integer); H₁ = b₁ = 3 = the periodic
3-torus wraps (correct). The complex is VALID. Uniqueness FAILS on the full 10-ring
set (b₂ over-complete) — the pre-declared partial. Booked as such below.

---

## §1. The srs 2-complex + the CHOICE LEDGER

Nodes (0-cells) and bonds (1-cells) are GIVEN by `build_srs_net`
(`src/ave/core/chiral_lattice.py` srs branch — the z=3 chiral Laves / (10,3)-a /
Sunada-K4 net). The design decision is the 2-cells. The srs net's natural minimal
cycles are the **girth-10 rings** (srs = girth-10 / (10,3)-a — EXTERNAL MATHEMATICS,
`chiral_lattice.py:19-23`, asserted only by executable keepers). The faces are the
10-rings, enumerated algorithmically (deterministic DFS, `enumerate_girth_faces`).

### Corpus grep (per ave-prereg, before positing geometry)

`grep -niE "10-ring|ten-ring|girth"` over `manuscript/ave-kb/` + `research/` +
`src/` returns the girth-10 canon in `chiral_lattice.py:19-23` (the docstring
citing Sunada 2008 / RCSR `srs` / Wells (10,3)-a) and the smoke keeper
`net_ring_writhe`'s girth re-confirmation (`min_len/max_len` == 10). **No prior
DEC / cochain / incidence-matrix / Betti / Hodge canon exists** (grep for
"discrete exterior | cochain | coboundary | betti | hodge | incidence matrix"
returns nothing tracked) — this module is genuinely new infrastructure.

### The choice ledger (each choice tagged)

| # | Choice | Tag | Rationale |
|---|--------|-----|-----------|
| C1 | 2-cells = girth-10 rings | **GEOMETRY-FORCED** | The srs net IS girth-10; the minimal cycles are the natural 2-cells. Canon-cited (`chiral_lattice.py:19-23`). |
| C2 | Supercell edge **L ≥ 3** | **GEOMETRY-FORCED** | Empirically (Rule-10 driver check): at **L=2** the periodic wrap folds the girth-10 rings into **spurious 8-rings** (the shortest cycle through every edge is length 8, not 10). L≥3 recovers girth-10 everywhere (verified L=3, L=4). `build_srs_dec` hard-errors on L<3 (flag-don't-fix; not a silent clamp). |
| C3 | Edge orientation `u<v` (head at larger index) | **ENGINEERING-CHOICE** (conventional) | Any consistent orientation works; `u<v` is deterministic and matches the solver's `unique_bonds`. The physics (∂∂=0, Betti) is orientation-independent. |
| C4 | Face orientation from the cyclic ring order | **GEOMETRY-FORCED** (up to a per-face sign) | The cyclic node order fixes each face's boundary consistently so ∂₁∂₂=0 holds exactly; the global per-face sign is a gauge (does not affect the identities or Betti). |
| C5 | Use the **FULL** 10-ring face set (not a minimal subset) | **ENGINEERING-CHOICE** | The full set is canonical (every girth-10 cycle), deterministic, and closes ∂₁∂₂=0 with the correct H₁=3. **Cost:** it is OVER-COMPLETE — b₂ ≫ 3 (many linear dependencies among face boundaries), so a *minimal* 2-complex (b₂=3) is NOT uniquely singled out. A minimal spanning-face subset exists (rank(∂₂)=106 at L=3 ⇒ 106 independent faces span the boundary image) but choosing one requires an arbitrary basis pick. **UNIQUENESS FAILS — booked honestly, not forced.** The full-set choice is preferred because it is canonical and gives the exact-integer identity for the whole class; the theorem (below) needs only that ∂₂'s IMAGE be curl-exact, which the full set delivers. |

### Complex sizes (deterministic)

| L | V (nodes) | E (bonds) | F (10-ring faces) | faces/edge | girth |
|---|-----------|-----------|-------------------|------------|-------|
| 2 | 64  | 96  | — (8-rings, INVALID) | — | **8** (PBC artifact) |
| 3 | 216 | 324 | 324 | 10 (every edge) | 10 |
| 4 | 512 | 768 | 768 | 10 (every edge) | 10 |

---

## §2. The operator set + the machine-precision identities

From the complex (`SrsDEC`):

```
grad     = d0 = ∂₁ᵀ        nodes → edges     (potential differences)
div      = −∂₁             edges → nodes     (exact negative adjoint of grad)
curl     = d1 = ∂₂ᵀ        edges → faces     (circulation per face)
curl_adj = ∂₂              faces → edges     (adjoint curl)
L0       = div∘grad = −∂₁∂₁ᵀ   nodes → nodes  (scalar graph Laplacian)
```

### The identities (L=3, seeded random fields, 64 draws each)

| Identity | Statement | Measured | Meaning |
|----------|-----------|----------|---------|
| **∂₁∂₂ = 0** | exact integer matrix product | `max|∂₁∂₂| = 0` (**int64, EXACT — not roundoff**) | the combinatorial core: ∂∂=0 holds for the OPERATORS, hence for every field |
| **div∘curl_adj ≡ 0** | `= −∂₁∂₂` on any face field | `max ≈ 2.7e-15` (float sparse product) | THE THEOREM operator: every `F=curl_adj(c)` is divergence-free |
| **curl∘grad ≡ 0** | `= (∂₁∂₂)ᵀ` on any node field | `max ≈ 1.1e-15` | the dual identity |
| **div = −gradᵀ** | matrix equality | `array_equal` **exact** | the adjoint relation the Stage-1b pair **lacked** |

Contrast the Stage-1b operators (`_srs_curl_nodes`, `_srs_node_divergence`,
pinned in `test_stage1b_operator_pair_is_NOT_a_dec_pair`): `div∘curl` on a random
field has **RMS ≈ 0.35** (re-confirmed here) — decisively NOT a machine zero. The
Stage-1b pair are per-node **Cartesian-embedded 3-vector** heuristics; the DEC
operators are **coordinate-free cochains**, and the Cartesian embedding is exactly
what broke adjointness (phase-space-coordinate-check: the fix is to measure in the
lattice-intrinsic cochain coordinates, not the ambient x/y/z projection).

### Laplacian reconciliation (RECONCILED, not re-derived)

The existing solver's graph Laplacian is
`srs_cage_winding.assemble_L_srs(D≡1) = Bᵀ B`, where `B = build_incidence` has
shape `(E×V)` with `B[e,u]=+1, B[e,v]=−1` for the SAME oriented edge `(u,v), u<v`.
Hence `B = −∂₁ᵀ`, so:

> **`Bᵀ B = ∂₁ ∂₁ᵀ = −L0`  EXACTLY** (`max|BᵀB − (−L0)| = 0.0`, verified).

**Same operator.** They differ ONLY by the `div=−∂₁` sign convention: `BᵀB` is
the +PSD combinatorial graph Laplacian; `L0 = div∘grad = −∂₁∂₁ᵀ` is its negative
(the −PSD analyst's sign). The edge sets are identical
(`oriented_edges == unique_bonds`, verified edge-for-edge). For a non-trivial bond
weight `D_bond`, `Bᵀ diag(D) B = ∂₁ diag(D) ∂₁ᵀ = −(weighted div∘grad)` — the same
relation carries through the weighting (the D-weighting is the Op14-saturated case
and is OUT OF SCOPE for the cold theorem below, but the operator reconciliation is
weight-agnostic).

---

## §3. THE THEOREM

> **Theorem (srs curl-class charge-neutrality, cold-linear-static-local).**
> On the srs DEC 2-complex (nodes = srs 0-cells, edges = srs bonds, faces = srs
> girth-10 rings; L ≥ 3), let `div = −∂₁` and `curl_adj = ∂₂` be the DEC operators
> above. Then for **any** 2-cochain `c` (any face field whatsoever),
>
> **`div(curl_adj(c)) = −∂₁∂₂ c = 0`  identically (exact),**
>
> because `∂₁∂₂ = 0` is a combinatorial identity of the complex (boundary-of-a-
> boundary). Consequently **every edge field `F = curl_adj(c)` in the entire curl
> class is divergence-free**, so its net node-divergence over any closed region is
> zero — **zero enclosed charge at every radius** — as a *structural identity*, not
> a numerical near-zero and not a property of a particular operator pair.

This is the class-level upgrade: it is true of the WHOLE curl class `{F =
curl_adj(anything)}`, of which the Stage-1b `{∇×ω, ω}` members are two instances,
not just of the two tested operators.

### SCOPE BOX (verbatim from Grant's ratified cell — what it does NOT say)

The theorem closes the **cold-linear-static-local CURL-CLASS cell** at theorem
grade. It says **NOTHING** about:

- **Non-curl couplings.** `∇·ω ≠ 0` in general — a divergence coupling (`div(ω)`
  for a node/edge field that is NOT `curl_adj` of anything) is a **measured, non-
  identity zero-or-nonzero**, NOT covered by ∂∂=0. **Distinguish:** the curl-class
  zero is a THEOREM (∂∂=0); a `∇·ω` zero, if observed, is an EMPIRICAL near-zero of
  a specific field, not a structural identity. (This is precisely the trap the
  Stage-1b headline fell into — attributing a readout-antisymmetry zero to a curl
  identity that did not hold for those operators.)
- **S(A)-modulated couplings.** The theorem is for the **unweighted** (cold, S≡1)
  complex. ∂∂=0 is metric-independent so it survives a *diagonal* bond weight, but
  the moment saturation makes the coupling itself `S(A)`-dependent (Op14 on), the
  *coupling* is no longer a fixed cochain map and the class statement does not
  transfer without re-derivation.
- **Self-consistent nonlinear statics.** Lagged-nonlinearity or back-reaction is
  out of scope.
- **Dynamics.** Time-domain / LC-reactance evolution is out of scope.
- **Topology (the winding / linking Z).** The theorem is about the LOCAL exact part
  (div of a curl); the winding's charge label `Q = Link(∂Ω, F) ∈ ℤ`
  (`clm-ze4clw`) lives in the HARMONIC / non-exact part (§4), which the theorem
  explicitly does NOT annihilate.
- **The operator PAIR.** This SUPERSEDES the pair-scoped closure — it is now a
  class theorem — but it does not retroactively validate the Stage-1b pair as a
  DEC pair (they are not; pinned as a regression).

---

## §4. What DOES have nonzero divergence — the Hodge / cycle structure

The theorem kills the **exact** part (`im ∂₂` = curl-exact edge fields). By the
Hodge decomposition of 1-cochains, the space that div does NOT annihilate is the
orthogonal complement: the **co-exact part** (`im grad = im ∂₁ᵀ`, the gradient
fields — these carry the divergence / the Coulomb potential, `clm-4r4jiy`) plus the
**harmonic part** (`H₁ = ker∂₁ ∩ ker∂₂ᵀ`, the non-contractible cycles).

**A field can source a net divergence iff it has a co-exact (gradient) component.**
Pure-curl fields cannot (the theorem). This is the DEC statement of "only the
potential/gradient sector carries charge; the circulation sector is charge-neutral."

### The harmonic dimensions (measured)

| quantity | L=3 | L=4 | invariant? | meaning |
|----------|-----|-----|------------|---------|
| **b₀** (H₀) | 1 | 1 | yes | connected (the constant node-mode; nullspace of L0) |
| **b₁** (H₁) | **3** | **3** | **yes (L-independent)** | the **harmonic 1-cochain dimension** = the 3 non-contractible loops of the periodic 3-torus (one per supercell axis) |
| **b₂** (H₂) | 218 | 514 | **no (grows with L)** | OVER-COMPLETE on the full 10-ring face set — the linear-dependence count among face boundaries; **minimal-2-complex uniqueness FAILS** |

`b₁ = 3` is confirmed two independent ways: (i) the rank–nullity chain
`b₁ = E − rank(∂₁) − rank(∂₂) = 324 − 215 − 106 = 3`; (ii) the nullity of the Hodge
1-Laplacian `L1 = ∂₁ᵀ∂₁ + ∂₂∂₂ᵀ` = 3. It is L-independent (3 at L=3 and L=4) — a
genuine topological invariant of the periodic supercell, not an L=3 accident.

> **🟡 FLAGGED PARAGRAPH (topological-lane interpretation — one paragraph, no
> further interpretation).** The engine-architecture epic's topological-Z lane
> carries a fluxoid-style hypothesis (the winding charge as a topological flux
> threading a non-contractible cycle). The DEC complex supplies the exact object
> such a hypothesis needs: a **3-dimensional harmonic 1-cochain space** (`H₁`,
> `b₁=3`), spanned by the three periodic-supercell wraps, that is EXACTLY the part
> of the field the curl-class theorem does NOT annihilate. Physically: the
> curl-class theorem forbids a *local* monopole from a pure circulation (div of a
> curl = 0), but leaves open a *global* topological charge carried on `H₁` — the
> winding's `Q = Link(∂Ω, F) ∈ ℤ` (`clm-ze4clw`) would live here, in the harmonic
> sector, not in the exact sector the theorem kills. I report this as the harmonic
> finding and stop; whether the fluxoid hypothesis actually lands its charge on
> `H₁` is a separate test (surfaced to Grant / the topological lane, not decided
> here).

---

## §5. Closure-upgrade language for the claim spine

The Stage-1b closure (the cold-linear-static-local `{∇×ω, ω}` cell, previously
scoped as an **operator-pair property** because the two operators were shown NOT
to be a DEC pair — `research/2026-07-03_em-readout-vsector-stage1_result.md`
PANEL-FINDINGS §Blocker-2) gets a **STRENGTHEN-BY row**:

> **🟢 STRENGTHENS (2026-07-03, DEC MINI-ARC; no retraction).** The cold-linear-
> static-local closure of the CURL-COUPLING CLASS is upgraded from "a property of
> the (`_srs_curl_nodes`, `_srs_node_divergence`) engineering-choice operator pair"
> to a **∂∂=0 STRUCTURAL IDENTITY** on the srs DEC 2-complex
> (`ave.topological.srs_dec`; `research/2026-07-03_srs-dec-operators_result.md`).
> On the DEC operators `div=−∂₁`, `curl_adj=∂₂`, **every** field `F=curl_adj(c)`
> has `div F ≡ 0` (exact integer ∂₁∂₂=0), so **zero enclosed charge at every
> radius for the entire curl class**, not just the two tested members. Scope
> boundary (§3 box): NOTHING is claimed for non-curl couplings (`∇·ω` remains a
> measured non-identity), S(A)-modulated couplings, self-consistent nonlinear
> statics, dynamics, topology, or the pair-as-DEC-pair (they are not).

**Claim-id trail (verify-before-cite):**
- `clm-ze4clw` — `Q = Link(∂Ω, F_substrate) ∈ ℤ` = charge, the boundary linking-
  number dictionary (`manuscript/ave-kb/common/boundary-observables-m-q-j.md:20`).
  The theorem sharpens its LOCAL sector: a pure-curl (exact) `F` carries zero
  Gauss/enclosed charge as an identity; the `Q` label lives in the harmonic sector
  (§4).
- `clm-4r4jiy` — the `A_geom ∝ 1/r` Coulomb POTENTIAL in the gapless EM-ε channel
  (`manuscript/ave-kb/vol4/claim-quality.md:1302`). This is the CO-EXACT (gradient)
  sector — the part that DOES source divergence (§4), complementary to the
  curl-class zero.

**Auditor-lane handoff (I surface, the auditor lands):** the STRENGTHENS row above
is the manuscript / KB entry the auditor lane should land against the Stage-1b
closure claim + `clm-ze4clw`. I do NOT draft the KB leaf edit here (lane discipline).

---

## §6. Substrate-native + discipline walk (applied-set)

- **substrate-native-check** (fired before code): K4/srs ✓ (z=3 chiral Laves net,
  NOT cubic, NOT diamond z=4); Cosserat/Op14 ✓ (cold S≡1, saturation OUT of scope
  and explicitly excluded); phase-space-vs-real-space ✓ (coordinate-free cochains
  replace the Cartesian per-node 3-vector embedding that broke Stage-1b); no
  SM/QED default (no Lagrangian, no continuum-Helmholtz — pure combinatorial ∂).
- **phase-space-coordinate-check**: the corpus zero was mis-measured in ambient
  Cartesian projection; DEC measures in the matching lattice-intrinsic cochain
  coordinates. ✓
- **consistency-vs-emergence**: tagged DERIVATION / INFRASTRUCTURE (combinatorial
  math on the connect-map; integer operators; no CODATA input; no emergence claim).
- **Rule 10** (empirical-driver): the L=2 8-ring PBC artifact was caught by running
  the ring-enumerator early, before positing the face set — it is now a hard guard.
- **flag-don't-fix**: the uniqueness failure (b₂ over-complete) is surfaced as a
  choice-ledger partial (C5), not silently resolved by forcing a minimal basis.
