# Node-Scattering Multiplicity / Containment Gate — PREREG (scope b only)

**Date:** 2026-06-20
**Branch:** `analysis/2026-06-20-node-scattering-multiplicity-gate`
**Frozen-commit:** (this file's commit — the FIRST commit of the branch; predictions
pre-committed BEFORE any operator is built)
**Scope:** **(b) ONLY — the multiplicity / sector test (Fork A).** Forks B / C / D
are DEFERRED (see §7).

> **Discipline lane:** implementer. This prereg freezes the Fork-A prediction,
> the chord/echo/refute mapping, and the validate-on-known anchors BEFORE the
> operator exists, so the verdict cannot be reverse-fit. Disciplines walked:
> `substrate-native-check` (operator on the bond-graph, not the grid),
> `phase-space-coordinate-check` (port-space vs real-space, map SHOWN),
> `ave-discrimination-check` (embedding > DOF-counting), `consensus-bias-
> symmetric-standard`, `verify-before-cite` (all file:line greps run on HEAD
> 8fed90db), `ave-canonical-source` (import constants, never hardcode).

> 🔴 **POST-FREEZE RULE-12 AMENDMENT (2026-06-20, adversarial-auditor surfaced —
> the frozen prediction below is PRESERVED UNCHANGED; this is an appended note,
> not an edit).** Once the Fork-A test was BUILT, it proved **NON-DISCRIMINATING**:
> the verdict logic reads only `S_n = (2/n)J − I` projector quantities
> (`differential_scalar_content`, `common_mode_scalar_content`), which are
> **scramble-invariant** — randomizing every `bond_unit` vector leaves them
> bit-unchanged — so the verdict could only ever come out **R3**, for any lattice,
> with no physics in the decision. The Fork-A prediction frozen in §3/§4 was
> therefore testing a **MISCAST premise**: it presupposed that longitudinal
> confinement is a *differential-sector* question, but an isotropic/longitudinal
> A1 scalar IS the +1 common mode by projector construction, orthogonal to the
> entire −1 differential sector BY DEFINITION. R3 is TRUE but **true by
> construction, not by a discriminating test.** The pre-committed Fork-A prediction
> stands frozen as written; this amendment records that, once built, it was found
> to test a non-discriminating premise. See the result doc
> `research/2026-06-20_node-scattering-containment-gate_result.md` §2/§5 (Rule-12
> corrections) and the regression marker
> `src/tests/test_node_scattering_multiplicity.py::test_fork_a_verdict_is_invariant_under_bond_unit_scramble`.
> The bedrock (§1) and the four validate-on-known anchors (§2a–2d) are SOUND and
> UNAFFECTED — they remain the genuine deliverables of this gate.

---

## 0. ONE-LINE THESIS

The vacuum's confinement multiplicity is set by the **node valence** of the
lattice's own bond-graph. The degree-3 chiral `srs` net and the degree-4
`diamond` net give **structurally distinct** scattering operators
`S_n = (2/n)J − I` whose **differential (−1) eigenspace** has multiplicity
`n − 1` (2 for srs, 3 for diamond). FORK A asks whether confining the electron's
**longitudinal A1/V-sector** bound mode REQUIRES the diamond's **3rd**
differential mode — i.e. whether a normalizable confined longitudinal mode
exists on n=4 but NOT on n=3.

---

## (skeleton — sections filled incrementally per commit)

## 1. BEDROCK — graph-spectral first (the most fundamental first move)

The operator is assembled from the **lattice's own bond-graph CONNECT map**, NOT
a Cartesian grid and NOT the dense `TETRA_OFFSETS` cube. Concretely:

- `chiral_lattice.scatter_matrix(n)` = `(2/n)J − I` (the Op5 shunt-junction
  reduction, `chiral_lattice.py:81-102`), instantiated at **n=3** (srs, degree-3)
  AND **n=4** (diamond, degree-4).
- `chiral_lattice.build_srs_net(L)` / `build_diamond_net(L)` supply the periodic
  net: positions, `neighbors`, `reverse_port`, and `connect_index()` (the
  directed-edge CONNECT, `chiral_lattice.py:133-147`).
- The **global scattering operator** `𝓢` acts on the per-port amplitude vector
  `V ∈ ℝ^(N·d)`: scatter each node locally by `S_n`, then CONNECT (permute
  ref→inc along the reverse-port map). `𝓢 = C · (I_N ⊗ S_n)` where `C` is the
  CONNECT permutation from `connect_index()`. Because srs has N nodes of degree 3
  and diamond has N′ nodes of degree 4 with DIFFERENT connectivity, `𝓢_srs` and
  `𝓢_diamond` are **structurally different operators** — different dimension,
  different permutation, different spectrum.

**THE BUG THIS FIXES.** `graded_vacuum_network.py` (the prior build) hardwires the
dense `TETRA_OFFSETS` 4-diagonal cube for BOTH the diamond AND srs paths
(`graded_vacuum_network.py:30-36,87`), collapsing the valence distinction; and
`build_srs_net` currently has **zero solver call-sites** (verified §8). This gate
is the first solver to read the actual degree-3 srs CONNECT map.

> `substrate-native-check`: the operator is built FROM the graph
> (`connect_index`), not imposed on a grid. K4 checkpoint ✔ (S_n is the Op5
> reduction). Cosserat checkpoint: the winding sector is validated separately via
> `charge_quantization.py` (ω-grade only). phase-space-vs-real-space: see §2's
> port→grade map (SHOWN, not assumed).

## 2. VALIDATE-ON-KNOWN (wired FIRST, three anchors)

### 2a. Bare-spectrum anchor (local S_n, the distinctness witness)
Eigendecompose the single-node `S_n` and confirm:

| n | net     | degree | predicted spectrum        | differential (−1) mult |
|---|---------|--------|---------------------------|------------------------|
| 3 | srs     | 3      | `{+1×1, −1×2}`            | **2**                  |
| 4 | diamond | 4      | `{+1×1, −1×3}`            | **3**                  |

`S_n = (2/n)J − I` is a rank-1 perturbation of `−I`: the all-ones vector is the
single `+1` eigenvector (common mode = the symmetric breathing port-sum), and its
orthogonal complement is the `−1` eigenspace of dimension `n−1` (the
**differential** modes). The differing −1 multiplicity (**2 vs 3**) IS the
structural distinctness. `S_n² = I` (orthogonal reflection).

### 2b. Photon corpus anchor (the n=3 differential multiplicity = 2)
The srs differential multiplicity = **2** must match the photon's **2 transverse
polarizations**. Corpus anchors (verified §8):
- `src/tests/engine_acceptance/test_l1_photon.py:243-268` — the vector-TLM on the
  srs grid carries **exactly 2 transverse polarizations**, no longitudinal leak
  (`V0.shape[2] == 2`). *(post-freeze path-prefix hygiene fix, 2026-06-20: the
  `engine_acceptance/` subdir had been dropped; content + line range are correct.)*
- `engine-acceptance-suite.md:178` / `vol9/claim-quality.md:573` — "the srs
  vector-TLM carried 2 transverse DOF only."

PASS iff `srs −1 multiplicity == 2 == photon transverse DOF`.

### 2c. Winding-sector anchor (validate-on-known the DIFFERENTIAL sector's integer)
Per Grant's ruling, do NOT scope-to-mass-only: build the **winding** anchor too.
Seed a known `(p,q)` winding on the Cosserat ω-grade and confirm the charge gate's
differential operator reproduces the integer `Q`:
- `charge_quantization.seed_pq_winding(N, p, q, R, r)` plants the winding;
  `compute_Q_link` reads the **poloidal linking integer** (= q for a (p,q)
  winding). For the canonical electron `(2,3)`: `Q_link == 3` (the charge-"3"
  winding integer, α-free, ω-grade only).
- Known-negative: `ω ≡ 0` → `Q == 0`.

PASS iff the seeded `(2,3)` reproduces `Q_link == 3` and the null gives `0`.

### 2d. ALPHA-FREE invariance (the load-bearing, frame-independent anchor)
Re-run every spectral quantity under `α → 2α` (double `ALPHA` in `constants`,
re-import, re-solve). PASS iff `|dQ/Q| < 1e-6` for the winding integer AND the
S_n spectrum is literally α-independent (it contains no α). This is the anchor
that survives the eigen-vs-driven mismatch that sank the prior prereg's GATE1
(see the Rule-12 retraction in
`research/2026-06-19_electron-Q-coupled-network_prereg.md`).

### 2e. THE PORT→GRADE MAP (phase-space-coordinate-check — SHOWN, not assumed)
`S_n`'s eigenvectors live in **n-PORT space** (one amplitude per directed bond).
The A1 dilatation MASS-"3" and the Cosserat micro-rotation CHARGE-"3" live in
**real-space** (scalar field / ω-vector field). The map from port-space to grade
is the **bond-direction embedding** `bond_unit[u][p]` (the unit vector of port p
at node u, `chiral_lattice.py:114`) — equivalently the `TETRA_OFFSETS` directions
for diamond. The differential (−1) port-modes project to real-space grades via
this `(N, d, 3)` embedding. **This prereg COMMITS to displaying that map
explicitly** (Stage 2 must show the `port → bond_unit → real-space-grade`
projection matrix, not assert the correspondence). If the longitudinal-confinement
question forces wiring the A1 scalar seed INTO a differential-port phasor, that is
the genesis-24 double-count (`master-equation.md:20`, A1 ⊥ T2) and must be FLAGGED
as a coordinate clash, NOT silently resolved.
## 3. FORK A — the multiplicity observable + the PRE-COMMITTED prediction

**CORE-FREE** (the multiplicity is core-independent; no posited Gaussian core —
that sidesteps the Cartesian-core risk that the prior `saturated_core_strain`
build carried).

1. Build the **differential projector** `P₋₁` from `S_n`'s −1 eigenvectors (fix
   the sector FROM THE OPERATOR first, before any physics).
2. Solve the electron's **bound/confined longitudinal (A1 / V-sector, converter
   OFF)** mode on each distinct lattice operator `𝓢_srs` (n=3) and `𝓢_diamond`
   (n=4).
3. Ask:
   - **(a)** does the bound longitudinal mode live in the differential sector
     `P₋₁` (projection fraction `‖P₋₁ ψ‖² / ‖ψ‖² → 1`)?
   - **(b)** does **confining** the longitudinal excitation REQUIRE the n=4 net's
     **3rd** differential mode — i.e. is there **NO normalizable confined
     longitudinal mode on n=3 (2 differential modes), but YES on n=4 (3
     differential modes)**?

**PRE-COMMITTED FORK-A PREDICTION (frozen, the chord hypothesis):**
> A normalizable confined longitudinal A1 mode exists on the **degree-4 diamond**
> (3 differential modes available) and does **NOT** exist on the **degree-3 srs**
> (only 2 differential modes — the longitudinal scalar has no spare differential
> channel to localize in after the 2 transverse photon DOF are accounted). The
> 3rd differential mode is the **longitudinal-confinement channel**; its absence
> on n=3 is why the photon (transverse, 2 DOF) propagates on srs but a confined
> longitudinal mass-mode does not.

This is a genuine pre-registered prediction: it could fail in three ways (both
nets host a confined mode; neither does; or n=3 hosts one but n=4 does not). The
prediction is FALSIFIABLE before the operator is built.

## 4. CHORD / ECHO / REFUTE mapping (FROZEN — no post-hoc movement)

**CHORD** (all must hold):
- C1. Bedrock validate-on-known §2a–2d all PASS (distinct operators, correct
  spectra, photon-2 and winding-3 anchors, α-invariant).
- C2. Fork-A prediction holds: confined longitudinal mode on n=4, NONE on n=3,
  AND it lives in `P₋₁` (the differential sector).
- C3. **Embedding > DOF-counting** (§6): the port→real-space embedding is DERIVED
  from `bond_unit`/`TETRA_OFFSETS` and the result does MORE than reproduce the
  polarization count — it predicts the confinement asymmetry (n=4 yes / n=3 no)
  that pure DOF-counting does not give.

**ECHO** (the honest down-bin):
- E1. The 2-vs-3 multiplicity is REAL and distinct, but the result merely
  re-expresses the SM massless(2)/massive(3) vector-DOF count — the embedding adds
  nothing the polarization count did not already give (§6 fails). Bin **ECHO**:
  "node-valence reproduces the DOF count; AVE-distinct content not demonstrated."
- E2. Confinement asymmetry holds but is traceable to the core posit / boundary
  choice, not the differential multiplicity (core-free check fails).

**REFUTE** (the prediction is wrong, clean negative):
- R1. A normalizable confined longitudinal mode exists on **n=3** (srs, 2
  differential modes) — the "needs the 3rd mode" hypothesis is false.
- R2. NO confined longitudinal mode on **either** net — confinement is not a
  differential-sector phenomenon at all.
- R3. The bound mode does NOT live in `P₋₁` — the longitudinal sector is the
  common-mode `+1` eigenspace, not the differential `−1` (this would re-route the
  whole containment picture; FLAG and report).

## 5. HALT conditions (STOP and report — do NOT build on a broken operator)

- **H1.** n=3 and n=4 assemble the **IDENTICAL** operator (collapse not fixed) →
  HALT. Witness: `𝓢_srs` and `𝓢_diamond` have the same dimension / spectrum.
- **H2.** The bare spectrum is NOT `{+1, −1×(n−1)}` for either n → HALT (operator
  mis-assembled).
- **H3.** Any driven cross-check lands at **~137** (α-leak) or **~3** (bin-1
  artifact / off-by-one) where it should not → HALT.
- **H4.** The winding anchor `(2,3)` does NOT reproduce `Q == 3`, or the null is
  non-zero → HALT (charge-gate operator broken in this context).
- **H5.** α→2α moves any spectral quantity by `≥ 1e-6` → HALT (α-leak).

On HALT: STOP at Stage 1, write the result doc with the HALT reason, do **NOT**
build Stage 2. A HALT at the bedrock is a SUCCESSFUL gate outcome (it told us the
operator is wrong before we built physics on it).

## 6. SYMMETRIC-STANDARD pre-commitment (consensus-bias check)

The 2-vs-3 differential multiplicity LOOKS like the SM's massless-vector (2 DOF)
vs massive-vector (3 DOF) count. Pre-committed assessment rule:

- **PASS-as-chord** ONLY IF the port→real-space embedding (`bond_unit` /
  `TETRA_OFFSETS`) is DERIVED (not posited) AND the result predicts something the
  bare DOF count does not — specifically the **confinement asymmetry** (a
  normalizable longitudinal mode on n=4 but not n=3). The embedding must carry the
  geometry, not just the counting.
- **LABEL-as-echo** IF the result reduces to "node valence n → n−1 differential
  modes → matches 2/3 polarization count" with no extra predictive content. In
  that case the SM gets the same pass (it also puts the 2/3 count in by the
  massless/massive distinction; AVE would merely re-derive the count from valence,
  which is a CHORD of structure but an ECHO of the DOF number).

Symmetric-standard note: the SM does NOT derive WHY the photon has 2 and a massive
vector has 3 from a lattice — it is a representation-theory input. If AVE derives
the count from node valence AND adds the confinement asymmetry, that is genuinely
more than the SM. If AVE only re-derives the count, it is at parity, not ahead —
and we say so.
## 7. DEFERRED forks (B / C / D) — NOT built this session

Per Grant's ruling, scope is **(b) only**. The following are noted for the record
and explicitly **NOT** built here:

- **FORK B — the Γ=+1 saturation-bag arm (Grant's bulk-saturation framing).**
  Grant's framing, carried verbatim into the record: the **common mode** (the
  `+1` eigenvector of `S_n`, the symmetric port-sum / breathing channel) =
  **bulk saturation / volumetric compression**. The `+1` saturation-bag arm is the
  **unbuilt `Z_core → ∞` operator** — an OPEN (reflecting) confinement boundary
  on the common-mode channel, dual to the `Γ = −1` mu-load short on the
  differential channel. Where Fork A asks whether confinement needs the
  differential 3rd mode, Fork B asks whether the **common-mode** (bulk-saturation)
  channel hosts the longitudinal mass via a `Z_core → ∞` open-bag boundary. This
  operator is **NOT** built this session; it is the natural next arm because the
  A1 dilatation-MASS-"3" is a *compression* scalar (bulk), which physically maps
  to the `+1` common mode, not the `−1` differential sector. Fork A's `P₋₁`
  result will inform whether Fork B is even necessary (if the bound mode lands in
  `+1`, that is Fork A's R3 → Fork B becomes the primary arm).

- **FORK C / FORK D — DEFERRED, not framed here.** Reserved for the result-doc /
  follow-up. Not built.

> Note the LIVE TENSION pre-committed for honesty: the A1 dilatation MASS is a
> bulk *compression* scalar (master-equation.md two-"3"s: "mₑc² = trapped
> acoustic compression energy"), which leans toward the **common mode (+1 = bulk
> saturation, Fork B)**, while the differential `−1` sector is the natural home of
> the *transverse* photon DOF. Fork A's pre-committed prediction (longitudinal
> confinement needs the differential 3rd mode) is therefore NOT the only physical
> reading — the competing reading (longitudinal = common-mode bulk, Fork B) is
> live. Fork A's `P₋₁` projection test (§3a) DISCRIMINATES: if the bound
> longitudinal mode projects onto `+1` not `−1`, that is R3 and points at Fork B.
> This tension is pre-registered so the verdict cannot be reverse-fit either way.

## 8. Citation ledger (verified on HEAD 8fed90db via grep, `verify-before-cite`)

| Claim | Anchor | Verified content |
|---|---|---|
| `S_n = (2/n)J − I`, n=4→canonical diamond | `chiral_lattice.py:81-102` | scatter_matrix(n); n=3 gives (2/3)J−I, orthogonal S²=I |
| CONNECT directed-edge map | `chiral_lattice.py:133-147` | `connect_index()` (src→dst flat arrays) |
| srs net (degree-3, chiral) | `chiral_lattice.py:199-218` | `build_srs_net` |
| diamond net (degree-4) | `chiral_lattice.py:227-275` | `build_diamond_net` |
| bond-direction embedding | `chiral_lattice.py:114` | `bond_unit[u][p]` min-image unit vector |
| dense TETRA_OFFSETS collapse (the BUG) | `graded_vacuum_network.py:30-36,87` | hardwires TETRA_OFFSETS for both paths |
| photon = 2 transverse polarizations | `test_l1_photon.py:243-268` | `V0.shape[2] == 2`, no longitudinal leak |
| srs vector-TLM carried 2 transverse DOF | `engine-acceptance-suite.md:178` | verbatim |
| winding seeder + Q_link integer | `charge_quantization.py:486-511, 257-303` | seed_pq_winding, compute_Q_link (q=poloidal) |
| A1 ⊥ T2, no-phasor-wire (two-"3"s) | `master-equation.md:20` | genesis-24 double-count caution |
| prior prereg GATE1 = FAIL (driven≠eigen) | `test_graded_vacuum_network_isolation.py:9-24` | lossless eigen-Q→∞; 30.8 is driven-frame |

> **Reconciliation flag (surfaced, not silently fixed):** the prior prereg
> `research/2026-06-19_electron-Q-coupled-network_prereg.md:40` claimed "GATE1
> passed FIRST" — contradicted by `test_graded_vacuum_network_isolation.py:9-24`
> (GATE1 = FAIL). RETRACTED in that file via Rule 12 in this same commit (body
> preserved, red header, anchor replaced with the α-free invariance anchor, no
> substituted number).

---

**END PREREG (scope b). Predictions frozen at this commit.**

