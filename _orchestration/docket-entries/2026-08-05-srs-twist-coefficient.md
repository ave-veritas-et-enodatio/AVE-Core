# Lane return — the srs compression→twist coefficient (2026-08-05)

**Key:** `srs-twist-coefficient` · **Branch:** `research/srs-twist-coefficient` ·
**Dispatched by:** the 2026-08-05 squeeze-twist ruling
([`2026-08-05-ruling-squeeze-twist.md`](2026-08-05-ruling-squeeze-twist.md), PR #889 branch),
Grant verbatim `[sic]` *"1 and 2, go"*. **SVA pilot case 6.**

**BIN: `NO-TWIST`**, compound with a sized `O(q²)` gradient residual.
**`LOCKSTEP-EXACT` REJECTED · `LOCKSTEP-APPROX` REJECTED · `ROLL-OFF-EARLY` REJECTED.**

---

## What was measured

A homogeneous squeeze of the chiral srs-z3 unit cell induces **no macroscopic
micro-rotation at all** — `τ = |φ̄|/ε` is machine zero (`3.3×10⁻³³` isotropic, `1.2×10⁻¹⁷`
uniaxial) on **every** load, **both** enantiomorphs, **both** operating points
(`ρ_bond=1`, `ρ*=9.7734`). Not a small number: a **symmetry theorem**. Class **432 is the
one non-centrosymmetric class that is not piezoelectric**, and since 432 has only proper
rotations its **axial** rank-3 tensor vanishes with its polar one — no homogeneous strain of
any symmetry can turn this carrier. Under hydrostatic load there is not even an internal
relaxation, because **Wyckoff 8a has zero free positional parameters**: the squeeze is
*exactly affine*.

The chirality is real but enters two gradient orders down:
`κ/ε = ĉ₂ q²/ℓ_node`, exponent **fitted** at `2.0009 / 1.9983 / 1.9869`
(`[001]/[110]/[111]`), with `ĉ₂^[001] = +6.337710×10⁻³` (`ρ=1`) and `+5.567133×10⁻²`
(`ρ*`), **exactly sign-flipped** under enantiomorph swap and **identically 0.0** on the
achiral diamond control.

**Mechanism, and why the order is `q²`.** The chiral constitutive coupling `B·(tr ε)(tr κ)`
is present (`B = +2.24×10⁻³` at `ρ=1`, `+1.97×10⁻²` at `ρ*`), but the micro-rotation is
**gapped**: the relative-rotation modulus is `α = 1/(2√2) k_s` exactly (measured, G4). A
longitudinal squeeze carries no macroscopic rotation, so minimising `½αφ² + Bεκ` gives
`κ/ε = (B/α)q²` — the measured exponent, from an independent route. **The twist transformer
is wired but its secondary is shorted to the lattice frame; a DC squeeze drives nothing
through it.**

## The lockstep verdict, against the definition frozen before computing

Operational definition (prereg §0 row 3, frozen): `(δL/L)/(δC/C) = 1 ⟺ S_μ = S_ε ⟺ Γ_EM = 0`,
with `L ∝ μ_0 S_μ`, `C ∝ ε_0 S_ε` as **total cell branch reactances** (the A1 longitudinal
compliance `C_eff = C_0/S` explicitly declared *not* the `C` of this ratio).

| gradient scale | `A_μ/A_ε` | `(δL/L)/(δC/C)` | **`S_κ(wall)`** |
|---|---|---|---|
| `qℓ_node = 1` (one node — the **absolute ceiling**, unphysical) | `6.34×10⁻³` | `4.02×10⁻⁵` | `0.999979916516139` |
| solar `r_sat = 7GM/c²` | `8.84×10⁻³⁶` | `7.8×10⁻⁷¹` | `1.000000000000000` |

**`S_κ(wall) = 1`.** The inductive branch does not collapse when the capacitive branch does.
The wall is maximally **ASYMMETRIC**, not SYM. `τ` stays at machine zero all the way to the
wall (the symmetry theorem is ρ-independent, hence amplitude-independent in this model), so
**"until a point" has no leading-order object to break**. The `O(q²)` residual *grows* ~23×
toward the wall (`ĉ₂ → 1.47×10⁻¹` at `A=0.999`) — a roll-*on*, still 60+ orders short.

## Relationship statements (RELATIONSHIP ONLY — no leaf edited, no text minted)

- **`axiom-register.md`:189 (load-response bifurcation).** **Consonant and orthogonal.**
  Consonant in structure (a load in one grade → a response in a different coordinate, no
  aggregation rule). Orthogonal in subject: the register's "T2 bow" is the strut's mechanical
  bow coordinate, explicitly *not* a micro-rotation (`:193` homonym guard). The ruling
  proposed a **third** channel, A1 → Cosserat `φ`, and that is what measures zero.
  **The register's wording neither gains nor loses support.**
- **FLAG-COMBINE-SPLIT counter-receipts (`trampoline-framework.md`:255,
  `axiom-register.md`:232).** The ruling's position was that the chiral twist makes the
  aggregation question moot. **This result removes that route** — a "pure" squeeze loads
  **one** budget. The counter-receipts **stand exactly as written**; the cross-grade combine
  rule stays open on its existing terms. If anything the engine's `L∞` reading is reinforced:
  at 60+ orders of separation, `L∞` and normalized-`L2` are indistinguishable.
- **The ruling's own consequent.** It recorded the kernel-collapse premise as *"RESTORED AT
  LEADING ORDER"*. **Measured, there is no leading order.** Whether that retires or re-scopes
  the kernel-collapse ruling is **Grant's call and is not taken here.**
- **Canon's SYM gravity class is UNTOUCHED** — it rests on a source-side mechanism (soliton
  carrying internal **E** and **B**), not on this one. **`clm-acgyr1` is not retracted** — it
  is confirmed and given its static-response order.

## Discipline receipts

- **Freeze-alone:** prereg `ffdc4130`, one file in the commit, pushed before any derivation code.
- **SVA §0:** all eleven rows filled (ten pilot declarations + numerical conditioning).
- **Method independence:** G7 reproduces PR #884's rank-2 srs site spectrum `{0, 1.5, 1.5}`
  literally, shows the `k_s>0` Born site tensor is rank 3 and the global nullity is exactly 3.
  **The direct stiffness assembly never needed the rank-3 machinery** — no net switched, no STOP.
- **Negative controls first:** diamond-z4 exact `0.0`; `k_s=0` suppressed **11.09 OOM**.
- **Conditioning:** deterministic double-run digest `366959c9…51557ad` identical; `cond(K_b)`
  flat at `~43` across 7 `q`-decades; `mpmath` 60-dps cross-check deviating `~1.8×10⁻¹⁵`.
- **Number-check + mutation receipt:** `make verify-srs-twist-number-check` — 25 load-bearing
  numerals re-derived from the shipped JSON; all 6 mutations trip the checker.
  **Disclosed union-conflict class:** the `.PHONY` line and the `verify:` prerequisite line
  are shared with every other lane's number-check; correct resolution is the **UNION**.
- **Two-method receipts** with the regex engine named at each use (Python `re` / POSIX ERE
  `grep -REn`), including a documented **count disagreement (0 vs 5)** that is fully accounted
  for — which is exactly why two methods are required.

## Flags (verbatim in the result doc §10; none fixed here)

1. **FLAG-1 — merged canon asserts a zero mode this lane measures as gapped.**
   `micropolar_bloch.py`:175-184 states the uniform micro-rotation is *"an exact
   zero-eigenvector of Phi0"*; measured Rayleigh quotient at the geometry-fixed `lever=1` is
   **`1.0`**. True only at `lever=0`. A **question** (not a finding) about whether
   `micropolar_longwave`'s Schur elimination overstates the rotational back-reaction reported
   in PR #508 is routed, **not investigated and not fixed**.
2. **FLAG-2 — stale cite in a frozen record:** `2026-07-04_srs-chiral-micropolar_result.md`:93
   cites `ℓ_c²=γ/G=6` at `constants.py:298`; content is at `:338`. Line-drift; source byte-untouched.
3. **FLAG-3 — brief-vs-PR numbering:** the brief's "PR #884's FLAG-3" names the rank-2 blocker,
   which PR #884 lists as its *"Disclosed pre-reg deviation G7a→G7b"*; its numbered FLAG-3 is
   the diamond-carrier item. Surfaced, not reconciled.
4. **FLAG-4 (inherited, with a new datum):** at `lever=1` the micropolar model is **exactly
   objective** (`E(rigid) = 0.0`); the `#802` Born rotation cost is the `lever=0` value.
   Grant adjudicates the standing fork; **not adjudicated here.**
5. **FLAG-5 — two gates FAILED AS WRITTEN, neither retuned nor dropped.** G2 compared the
   symmetric-strain tensor to an acoustic-slope reading; G6's frozen observable divides a
   round-off floor by `q` and cannot be passed by any true null. Both defects are in the gate
   *specification*; both carry the correct comparison alongside (KEEP-BOTH). **No adjudication
   criterion was dropped post-hoc to convert a ❌ to a ✅.**

## Scope fence

`research/` + this docket fragment only. **No manuscript edit, no KB edit, no `src/ave/` edit,
no claim-id minted, no solidity moved.** PR #889's branch untouched; predecessor artifacts
byte-untouched. Canonical propagation (wall-taxonomy §10, the SYM-mechanism cross-refs, the
FLAG-CANON repair, the ch15 fourth-channel row) remains **GATED** on Tier-2 + Grant.
