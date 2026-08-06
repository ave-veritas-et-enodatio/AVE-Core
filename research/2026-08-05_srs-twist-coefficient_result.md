# RESULT — the srs compression→twist coefficient: the squeeze does NOT twist at leading order

**Date:** 2026-08-05 · **Lane:** implementer (`research/srs-twist-coefficient`) · **SVA pilot case 6**
**Prereg (FROZEN):** [`research/2026-08-05_srs-twist-coefficient_prereg-FROZEN.md`](2026-08-05_srs-twist-coefficient_prereg-FROZEN.md) @ `ffdc4130` (freeze-alone: one file in the commit)
**Driver:** `src/scripts/vol_1_foundations/srs_twist_coefficient.py`
**Shipped run:** `research/drivers/srs_twist_coefficient_results.json`
**Deterministic double-run digest:** `sha256 = 366959c9634f8c0debc611af4c17926656a330498f44d2aeab0f249f051557ad` (identical on two consecutive runs)
**Carrier declaration (D1 policy):** RATIFIED chiral **srs-z3** (`build_srs_net`, `I4₁32`, Wyckoff-8a, z=3, `carrier="srs-z3"` asserted at load). The diamond-z4 net appears ONLY as the achiral negative control.

---

## VERDICT BOX

> **PRIMARY BIN: `NO-TWIST`**, compound with a **sized `O(q²)` gradient residual**.
>
> A homogeneous squeeze of the chiral srs-z3 cell induces **NO macroscopic
> micro-rotation at all**: `τ ≡ |φ̄|/ε = 3.3×10⁻³³` (isotropic) and `1.2×10⁻¹⁷` (uniaxial
> `[001]`) at `ρ_bond=1` — machine zero on every load, both enantiomorphs, both operating
> points. This is not a small number, it is a **symmetry theorem**: point group **432 is the
> one non-centrosymmetric crystal class that is not piezoelectric**, and because 432 contains
> only proper rotations its **axial** rank-3 tensor `d_ijk ε_ij φ_k` vanishes with its polar
> one. No homogeneous strain of any symmetry can turn the srs carrier.
>
> The chirality **is** there, and it **is** parity-odd and diamond-null — but it enters two
> gradient orders down. The measured law is
>
> $$\frac{\kappa}{\varepsilon} \;=\; \hat c_2\,\frac{q^2}{\ell_{node}},\qquad \hat c_2^{[001]} = +6.3377\times10^{-3}\ (\rho_{bond}{=}1),\ \ +5.5671\times10^{-2}\ (\rho^*{=}9.7734)$$
>
> with the exponent **fitted, not assumed**: `2.0009 / 1.9983 / 1.9869` along `[001]/[110]/[111]`.
> `ĉ₂` flips sign exactly under enantiomorph swap (`ĉ₂(left) = −ĉ₂(right)`, residual `5.6×10⁻¹²`
> relative) and is **identically 0.0** on the achiral diamond control.
>
> **The lockstep therefore FAILS, and not narrowly.** With `A_μ/A_ε = ĉ₂ (qℓ_node)²`, the
> fractional-reactance ratio `(δL/L)/(δC/C) = (A_μ/A_ε)²` is `4.0×10⁻⁵` at the **absolute
> physical ceiling** `qℓ_node = 1` (a gradient that turns over in one node) and
> `≈ 8×10⁻⁷¹` at a solar `r_sat = 7GM/c²`. **`S_κ(wall) = 0.99998` at the ceiling and
> `1.000000000000000` at every gravitational gradient scale** — the inductive branch does
> not collapse when the capacitive branch does.
>
> **`LOCKSTEP-EXACT` is REJECTED. `LOCKSTEP-APPROX` is REJECTED** — the residual is not a
> small offset on a lockstep, there is no lockstep to offset. **`ROLL-OFF-EARLY` is
> REJECTED** — there is no leading-order object to roll off (and the `O(q²)` residual grows
> ~23× toward the wall rather than saturating, which does not rescue it from 60+ orders of
> magnitude). **`UNDERDETERMINED` is REJECTED for the physics**, and recorded for **one
> normalisation only** (`ω_yield`, §7).

**What this does NOT say.** It does **not** falsify canon's SYM gravity class. Canon's SYM
realization is *source-side* (a mass-soliton carrying internal **E** *and* **B**, or a
symmetric bulk strain — `CLAUDE.md` INVARIANT-S2). This lane tested the *new, geometry-side*
mechanism the 2026-08-05 ruling proposed as the thing *beneath* SYM, and that mechanism does
not fire. SYM stands or falls on its existing grounds, untouched. It also does **not** retract
`clm-acgyr1` — it **confirms** that leaf's object and adds its static-response order.

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** A1 translational dilatation = the **capacitive C-side** load; Cosserat
  micro-rotation `φ` / wryness `κ` = the **inductive L-side** response
  (`translation-circuit.md`:35). Not the Cosserat (2,3) winding charge; not the Axiom-4
  "T2 bow" coordinate (`axiom-register.md`:193 homonym guard). No cross-wiring.
- **REGIME:** STATIC, cold linear, sub-yield, saturation OFF. Near-yield entered ONLY via the
  canon-forced swapped-spring `ρ_eff = ρ_cold·(S_axial/S_shear)`, MODEL SCOPE inherited.
- **COORDS (A46):** real-space / spatial-Brillouin throughout. The claim under test is a
  real-space mechanical statement; `φ̄/ε` and `κ/ε` are real-space. Coordinates match.
- **LEDGER:** entirely RIM — lossless static energy minimisation on a closed periodic cell.
  No port, no radiation, no detector. **No loss word appears in this result.**
- **CLASS:** CONSISTENCY / DC-internal. **α-CLEAN**: every headline is a dimensionless ratio
  in units of `k_s` and the NN bond; no CODATA, no SI substitution, no `Q_TANK`.

---

## 1. GATES — the literal state of every one (UNRUN ≠ PASSED)

| # | Gate | State | Receipt |
|---|---|---|---|
| **G1** | carrier + bond-list rebuild | ✅ **PASS** | 8 nodes, degree 3/3, girth **10** (on `L=4`), NN bond `1.0000000000000002` = `a_cell·√2/4`; **added sub-check**: the `k=0` Hessian equals the exact energy to `rel = 0.0` (bit-exact) |
| **G2** | Stage-1 regression (`ρ*=9.7734`) | ❌ **FAIL AS WRITTEN** — diagnosed, not retuned | see §2 |
| **G3** | objectivity | ✅ **PASS** | `E(rigid rotation) = 0.0` **exactly** at `lever=1`; `3.13×10⁻⁶` at `lever=0`, `7.83×10⁻⁷` at `lever=0.5`, `3.13×10⁻⁶` at `lever=2` |
| **G4** | rotational gap | ✅ **PASS (either outcome)** — verdict **GAPPED** | Rayleigh quotient of the uniform-`φ` vector = **1.0** at `lever=1` (and `0.0` at `lever=0`). **This contradicts a docstring in merged canon — see FLAG-1** |
| **G5** | achiral null control (diamond-z4) | ✅ **PASS** | `max|κ/ε| = 0.0`, `max|ĉ₂| = 0.0`, `max τ = 0.0` — **exact**, not thresholded |
| **G6** | mechanism null control (`k_s=0`) | ❌ **FAIL AS WRITTEN** — specification defect named | see §3 |
| **G7** | rank-2 feasibility **STOP-GATE** | ✅ **PASS (a and b)** | see §4 |
| **G8** | conditioning | ✅ **PASS** | see §5 |

Negative controls G5/G6 were run and reported **before** any srs number was read, per the
frozen ordering.

## 2. G2 — FAILED AS WRITTEN, and the failure is informative

The frozen G2 compares my **symmetric-strain** elastic tensor against Stage-1's
**acoustic-slope** `Γ`. Those are the same object only in a rotationally-objective model.
Measured, at `ρ*=9.7734`:

| Reading | `C11` / `Γ_zz` | `C44` / `Γ_transverse` | vs Stage-1 |
|---|---|---|---|
| symmetric-strain elastic tensor (as G2 froze it) | `0.7278554` | `0.1603681` | `C11` matches to `6.3×10⁻⁶`; `C44/C11` off by **35.5 %** |
| **acoustic-slope `Γ(q̂=[001])`** (KEEP-BOTH companion) | `0.7278554` | `0.2487564` (both transverse eigenvalues) | `6.26×10⁻⁶` and `1.44×10⁻⁵` — **reproduces the certified predecessor** |

**So the machinery is validated against the certified predecessor** (Stage-1's
`C11=0.72786`, `C44=0.24876`, both to `~10⁻⁵`), and the frozen gate compared two genuinely
different readings. **The gate is NOT rewritten and NOT re-thresholded** (Rule 11): it is
recorded FAILED-AS-WRITTEN with its specification defect named, and the correct comparison
is shipped alongside it in the same JSON (KEEP-BOTH).

The 35.5 % gap is not noise — it is exactly the **standing FLAG-4 axis** already on the
record (`_orchestration/docket-entries/2026-08-02-biased-tensor-scoping.md`:8, verbatim:
*"the corpus **already measured** the Born-model rotation cost (#802 `:70`, verbatim:
`E(rigid rotation, 1e-3) = 1.984e-3 > 0`) and canonizes the **opposite** reading
(`translation-circuit.md`:360 …); the two readings are different physics and **Grant
adjudicates**"*). This lane's G3 supplies a **new, decisive datum for that open fork**:
at the geometry-fixed `lever = 1` the 6-DOF micropolar model **is exactly objective**
(`E(rigid) = 0.0`), and the rotation cost `#802` measured is the `lever = 0` value
(`3.13×10⁻⁶` here, same sign and order). **The Born rotation cost is a `lever=0` artifact,
not a property of the canon-geometry model.** Surfaced; **not** adjudicated here.

## 3. G6 — FAILED AS WRITTEN, and the frozen observable was the wrong one

The frozen threshold is on `c_twist = |κ/ε|/q`. On a *true* null, `|κ/ε|` is a round-off
floor, and dividing a floor by `q` **diverges as `q → 0`** — so the gate as specified cannot
be passed by any genuine null. Reported FAILED-AS-WRITTEN (`max c_twist = 9.32`), **not**
retuned.

The mechanism observable is `κ/ε`. At the **best-conditioned** `q = 0.2221`:

| model | `\|κ/ε\|` |
|---|---|
| `k_s = 0` (purely central — no transverse force, so the lever makes no torque) | `2.2397×10⁻¹⁵` |
| `k_s = 1` (canon Born) | `2.7407×10⁻⁴` |

**11.09 orders of magnitude of suppression** — the mechanism null holds. This also
independently reproduces Stage-2's finding (`2026-07-04_srs-chiral-micropolar_result.md` §2a,
verbatim: *"The purely-central control (`k_s=0`) correctly gives `B=0` (no transverse force
→ no moment arm)"*).

## 4. G7 — the STOP-GATE, and the rank-2 independence receipt

PR #884's disclosed blocker is reproduced **literally**:

| object at an srs site | spectrum | rank |
|---|---|---|
| central-force site tensor `Σ_b d̂⊗d̂` | `{3.70×10⁻¹⁶, 1.4999999999999996, 1.5}` | **2** |
| canon Born site tensor (`k_a=k_s=1`) | `{3.0, 3.0, 3.0}` | **3** |
| global `k=0` stiffness at `lever=1, γ=6k_s` | — | nullity **exactly 3** |

The rank-2 object is the **`k_s = 0` central-force** property of the coplanar trivalent star
(`2026-07-04_srs-chiral-micropolar_result.md` §3: *"the single srs node … is COPLANAR (det of
the 3 bond directions = 0 exactly)"*). The engine-native Born tensor carries the non-central
`k_s` term and is full rank; the global reduced stiffness has exactly the 3 expected zero
modes (uniform translations). **The direct stiffness assembly is well-posed and the blocker
does not bind it. The method at no point needed the rank-3 machinery, so no net was
switched and no STOP was required.**

⚑ **Numbering discrepancy, flagged not reconciled.** The dispatch brief calls this "PR #884's
FLAG-3". PR #884's numbered **FLAG-3** is a different item — verbatim: *"the canonical
Cosserat operator runs on the **z=4 diamond CONTROL** net (`chiral_lattice.py`:240), not the
D1-ratified `srs-z3` carrier (`:231`)"* — while the rank-2 blocker is that PR's separately
listed *"Disclosed pre-reg deviation G7a→G7b"*. Both are read; the brief's intent (the rank-2
blocker) is what G7 tests.

## 5. G8 — conditioning

| receipt | value |
|---|---|
| deterministic double-run digest | `366959c9…51557ad`, **identical** twice |
| `cond(K_b)` across the whole load-path-B `q` sweep | `4.35×10¹` – `4.37×10¹` (flat — no `q→0` blow-up, because the micro-rotation is gapped) |
| linear-solve residual | `6.2×10⁻²³` – `6.7×10⁻¹⁷` |
| `mpmath` cross-check at 60 dps (`[001]`, `q`-decades 1/4/7) | float64-vs-mp relative deviation `1.78×10⁻¹⁵`, `1.98×10⁻¹⁵`, `1.58×10⁻¹⁵` |
| imaginary-part control on `ĉ₂` (must be numerical zero) | `3.0×10⁻¹¹` vs signal `6.3×10⁻³` — **8 OOM below** |
| `ĉ₂` plateau relative spread over the last 4 `q`-decades | `9.2×10⁻⁴` (`[001]`), `1.7×10⁻³` (`[110]`), `1.3×10⁻²` (`[111]`) |
| internal Hessian definiteness at `ρ_bond=1` | **positive definite** on the reduced space (`indefinite = false`), `cond = 36.2` |

**Disclosed:** the canon `K<0` instability at `ρ_bond=1`
(`parent-condition-match-forces-balance.md`:71,74) does **not** make the *internal-relaxation*
Hessian indefinite — bulk-modulus negativity is a property of the macroscopic `C_ij`
combination, not of the internal subspace. The ρ-family was run regardless, so no conclusion
rests on `ρ=1` alone.

**Convergence caveat, stated:** `[111]` is the least converged direction (plateau spread
`1.3×10⁻²`, parity residual `4.2×10⁻⁵` vs `<10⁻¹¹` for `[001]`/`[110]`). It does not carry
any verdict; the headline coefficient is `[001]`.

---

## 6. THE COEFFICIENT

### 6.1 Load path A — the `k=0` affine squeeze: exactly nothing

`τ ≡ |φ̄|/ε` (net micro-rotation per unit strain) and `τ_rms` (the internal-only pattern),
both enantiomorphs, both operating points, `ε = 10⁻³`:

| operating point | load | `τ` (right) | `τ` (left) | `τ_rms` (right) | `τ_rms` (left) |
|---|---|---|---|---|---|
| `ρ_bond=1` | A-ISO (hydrostatic) | `3.31×10⁻³³` | `1.29×10⁻³²` | `1.270×10⁻¹⁷` | `1.258×10⁻¹⁷` |
| `ρ_bond=1` | A-UNI `[001]` | `1.18×10⁻¹⁷` | `1.70×10⁻¹⁷` | `1.450×10⁻²` | `1.450×10⁻²` |
| `ρ_bond=1` | A-UNI `[111]` | `1.29×10⁻¹⁷` | `1.56×10⁻¹⁷` | `8.461×10⁻³` | `8.461×10⁻³` |
| `ρ*=9.7734` | A-ISO | `3.84×10⁻¹⁶` | `3.84×10⁻¹⁶` | `3.86×10⁻¹⁶` | `3.88×10⁻¹⁶` |
| `ρ*=9.7734` | A-UNI `[001]` | `5.87×10⁻¹⁷` | `5.53×10⁻¹⁷` | `1.862×10⁻²` | `1.862×10⁻²` |
| `ρ*=9.7734` | A-UNI `[111]` | `2.22×10⁻¹⁶` | `1.83×10⁻¹⁶` | `1.529×10⁻²` | `1.529×10⁻²` |

Three separate facts, and all three were pre-registered:

1. **`τ = 0` on every load** (P1 ✓, P2 ✓). The **432 non-piezoelectricity** argument. A
   homogeneous strain cannot turn this carrier, at any stiffness ratio, in either hand.
2. **`τ_rms = 0` under hydrostatic load** (P3 ✓) — there is *no internal relaxation at all*.
   That is the **Wyckoff-8a** fact: the srs nodes sit at a fixed special position of `I4₁32`
   with **zero free positional parameters**, so a symmetry-preserving load admits no
   symmetry-preserving internal displacement. A hydrostatic squeeze of the srs cell is
   **exactly affine**.
3. **`τ_rms ≠ 0` under uniaxial load, and it is parity-EVEN** (right = left to all printed
   digits). It is an achiral internal-strain pattern with zero net rotation — an
   **optical-mode relaxation, not a twist**. Reported separately and never summed with `τ`.

### 6.2 Load path B — the gradient squeeze: where the chirality actually lives

Fitted law and coefficient (right enantiomorph; `ℓ_node = 1` in driver units, G1 receipt):

| operating point | direction | `ĉ₂` (right) | `ĉ₂` (left) | parity sum | parity-odd? | fitted power of `q` |
|---|---|---|---|---|---|---|
| `ρ_bond=1` | `[001]` | `+6.337710×10⁻³` | `−6.337710×10⁻³` | `+5.6×10⁻¹²` | ✅ | `2.0009` |
| `ρ_bond=1` | `[110]` | `−1.394091×10⁻³` | `+1.394091×10⁻³` | `+1.4×10⁻¹¹` | ✅ | `1.9983` |
| `ρ_bond=1` | `[111]` | `−4.001880×10⁻³` | `+3.960034×10⁻³` | `−4.2×10⁻⁵` | ~ (see §5) | `1.9869` |
| `ρ*=9.7734` | `[001]` | `+5.567133×10⁻²` | `−5.567133×10⁻²` | `+1.2×10⁻¹⁰` | ✅ | `2.0001` |
| `ρ*=9.7734` | `[110]` | `−2.896293×10⁻²` | `+2.895997×10⁻²` | `−3.0×10⁻⁶` | ~ | `1.9991` |
| `ρ*=9.7734` | `[111]` | `−5.717227×10⁻²` | `+5.713383×10⁻²` | `−3.8×10⁻⁵` | ~ | `1.9995` |

`ĉ₂` is a **tensor, not a scalar** — it changes sign between `[001]` and `[110]`/`[111]`.
The handedness receipt is exact where the numerics are converged.

### 6.3 Why the order is `q²` and not `q` — the mechanism, in circuit terms

The constitutive chiral term is the standard one, and it is present:
`W ⊃ B·(tr ε)(tr κ)`. Were the micro-rotation a **free** coordinate, minimising would give
`κ = −(B/D)·tr ε` — a **`q`-independent** compression→twist coupling, and the ruling would be
right. It is not free. **G4 measured the gap**: at the geometry-fixed `lever = 1` a uniform
micro-rotation with zero displacement costs energy (Rayleigh quotient `1.0`), i.e. the
relative-rotation modulus is nonzero:

$$\alpha \;=\; 0.3535533905932737 \;=\; \tfrac{1}{2\sqrt2}\ k_s \quad\text{(exact, both operating points)}$$

A longitudinal squeeze carries **no macroscopic rotation** (`ω_macro = ½∇×u = 0`), so the
micro-rotation's restoring term is the bare `½αφ²`. Minimising `½αφ² + B ε κ` with
`ε = iqA`, `κ = iqΦ` gives `Φ = −iqBε/α` and hence

$$\boxed{\ \frac{\kappa}{\varepsilon} \;=\; \frac{B}{\alpha}\,q^2\ }\qquad \hat c_2 \equiv \frac{B}{\alpha\,\ell_{node}}$$

— **exactly the measured exponent `2.000`**, from an independent route. Back-solving the
constitutive coupling itself:

| operating point | `α` (relative-rotation modulus) | `ĉ₂` `[001]` | **`B` (chiral coupling, stress × length)** |
|---|---|---|---|
| `ρ_bond=1` | `0.35355339` | `+6.337710×10⁻³` | `+2.2407×10⁻³` |
| `ρ*=9.7734` | `0.35355339` | `+5.567133×10⁻²` | `+1.9683×10⁻²` |

**The plumber's statement.** The twist coil is not open — it is **shorted by a stiff spring
to the lattice frame**. The chiral transformer between the compression branch and the
rotation branch is real and wired (`B ≠ 0`, parity-odd, dead on the achiral net), but its
secondary is clamped by `α`, so it only develops an output when the primary is *changing
across the cell* — twice over. A DC squeeze, however hard, drives nothing through it.

`B ≈ 2.2×10⁻³ … 2.0×10⁻²` sits in the same band as the canonized `B_signed ≈ 5.995×10⁻³`
of `clm-acgyr1` (`chiral-mechanical-gyrotropy.md`:33) — **noted as consistent, NOT claimed
identical**: that object is the `k`-linear pseudo-tensor block of a Bloch eigensolve, this
one is a static constitutive modulus, and the two are not shown here to be the same number.

### 6.4 The roll-off toward yield — no leading-order object to roll off

Entered through the canon-forced swapped-spring composition
`ρ_eff = ρ_cold·(S_axial/S_shear)` with the **axial** channel loaded by the squeeze
(`ρ_cold = 1`), sweeping the wall amplitude:

| `A_wall` | `S` | `ρ_eff` | `τ` (iso) | `τ` (uni `[001]`) | `ĉ₂` `[001]` |
|---|---|---|---|---|---|
| `0.000` | `1.0000` | `1.0000` | `3.3×10⁻³³` | `1.2×10⁻¹⁷` | `6.34×10⁻³` |
| `0.600` | `0.8000` | `0.8000` | `1.0×10⁻¹⁷` | `6.3×10⁻¹⁸` | `4.23×10⁻³` |
| `0.900` | `0.4359` | `0.4359` | `5.4×10⁻¹⁸` | `2.7×10⁻¹⁷` | `3.78×10⁻²` |
| `0.990` | `0.1411` | `0.1411` | `9.1×10⁻¹⁸` | `2.4×10⁻¹⁷` | `1.03×10⁻¹` |
| `0.999` | `0.0447` | `0.0447` | `1.7×10⁻¹⁷` | `3.5×10⁻¹⁷` | `1.47×10⁻¹` |

(The sweep is **not monotone** — `ĉ₂` dips to `4.20×10⁻³` at `A=0.3` before rising; the
`ρ_eff`-dependence of `B/α` is not a simple power. Reported as measured.)

**`τ` stays at machine zero all the way to the wall.** The symmetry theorem is a statement
about the point group, so it does not care what the stiffnesses are: **zero at every `ρ`,
hence zero at every amplitude in this model.** There is no leading-order lockstep to break,
so "until a point" has no object.

The `O(q²)` residual does grow toward the wall — `ĉ₂` rises ~23× from `6.3×10⁻³` to
`1.5×10⁻¹` as `A → 0.999` (the axial channel softens, `B/α` rises). **That is a real
roll-*on*, not a roll-off — and it is 60+ orders short of mattering** (§7). Recorded because
it was pre-registered, not because it rescues anything.

**Fence, inherited verbatim:** the swapped-spring model is *"a cold tensor with each bond
spring softened by its per-channel `S(A)` at FIXED geometry"*; *"initial/residual
(pre-)stress from bias pre-loading and bias-induced geometry change are OMITTED and remain
OPEN"* (`2026-07-04_saturated-elastic-tensor_result.md`). A finite-strain, geometry-updating
computation is **not** what was run and could in principle lower the symmetry — but only at
`O(ε²)`, and an axial vector cannot be built from a single symmetric tensor, so the leading
symmetry-allowed second-order term vanishes for hydrostatic and uniaxial loads too. Stated
as reasoning, not as a measured result.

## 7. THE LOCKSTEP ADJUDICATION

**The operational definition, exactly as frozen before computing (prereg §0 row 3):**

$$\frac{\delta L}{L}\Big/\frac{\delta C}{C} = 1 \quad\Longleftrightarrow\quad S_\mu = S_\varepsilon \quad\Longleftrightarrow\quad \Gamma_{EM}=0$$

with `L ∝ μ_eff = μ_0 S_μ` and `C ∝ ε_eff = ε_0 S_ε` — **total cell branch reactances**, not
series slots; the A1 longitudinal bond compliance `C_eff = C_0/S` is declared NOT the `C` of
this ratio. Cold-expanding `S = √(1−A²) ≈ 1 − A²/2` gives `δL/L ≈ −A_μ²/2` and
`δC/C ≈ −A_ε²/2`, so the lockstep ratio is `(A_μ/A_ε)²`. With
`A²_μ = κ²/ω_yield²` and `A²_ε = ε²/ε_yield²` (`cosserat_field_3d.py`:586-587,618-619):

$$\frac{A_\mu}{A_\varepsilon} \;=\; \hat c_2\,(q\,\ell_{node})^2 \qquad\text{under}\qquad \omega_{yield}\equiv\varepsilon_{yield}/\ell_{node}$$

| gradient scale | `qℓ_node` | `A_μ/A_ε` (`ρ=1`) | `(δL/L)/(δC/C)` | **`S_κ(wall)`** |
|---|---|---|---|---|
| `qℓ_node = 1` — one node (the **absolute ceiling**) | `1` | `6.338×10⁻³` | `4.02×10⁻⁵` | `0.999979916516139` |
| same, at `ρ*=9.7734` | `1` | `5.567×10⁻²` | `3.10×10⁻³` | `0.998449148919932` |
| 1 mm | `3.86×10⁻¹⁰` | `9.45×10⁻²²` | `8.9×10⁻⁴³` | `1.000000000000000` |
| 1 m | `3.86×10⁻¹³` | `9.45×10⁻²⁸` | `8.9×10⁻⁵⁵` | `1.000000000000000` |
| solar `r_sat = 7GM/c² = 1.03×10⁴ m` | `3.73×10⁻¹⁷` | `8.84×10⁻³⁶` | `7.8×10⁻⁷¹` | `1.000000000000000` |
| Earth radius | `6.06×10⁻²⁰` | `2.33×10⁻⁴¹` | `5.4×10⁻⁸²` | `1.000000000000000` |

**`S_κ` at the wall — the leak number the kernel-collapse ruling needs — is `1`.** At the
`ε` wall (`A_ε → 1`, `S_ε → 0`) the `μ` budget carries `A_μ = ĉ₂(qℓ)²`, so
`S_κ(wall) = √(1 − A_μ²)`. Even under the most generous possible reading — a gravitational
grading that turns over inside a single node, which is not a physical configuration — the
inductive branch retains `S_κ = 0.99998`. At any real gradient it is `1` to every digit
double precision carries. **The `μ` branch does not collapse with the `ε` branch. The wall is
maximally ASYMMETRIC, not SYM.**

⚑ **`ω_yield` — the one UNDERDETERMINED input, enumerated (SVA row 5 + §9 receipt).** There
is no canonical `ω_yield`. The table uses the **dimensionally forced** identification
`ω_yield ≡ ε_yield/ℓ_node`. This choice is load-bearing for the *absolute* leak only, and
the verdict is robust to it by **57 orders of magnitude**: flipping to the other engine
literal (`ω_yield = π` vs `1.0`) moves the ratio by `π`, and reaching lockstep from
`8.8×10⁻³⁶` would require an `ω_yield` wrong by 35 decades.

## 8. RELATIONSHIP TO THE BIFURCATION WORDING AND THE COUNTER-RECEIPTS

**Stated as a relationship only. No leaf is edited, no reconciliation text is minted, no
claim-id is touched.**

**(a) `axiom-register.md`:189 — the load-response-bifurcation wording.** Canon reads, verbatim
`[sic]`: *"the kernel is a **load-response bifurcation** (axial A1 dilatation load →
transverse T2 bow response; `A²+S²=arc*²` is a *single fixed-length constraint*, not a norm
over co-equal grades — the DP-3 L∞-vs-normalized-L2 fork was the wrong question…)"*.

This result is **consonant with that wording and orthogonal to its subject.** Consonant:
the register's picture is that a load in one grade produces a *response* in a **different
coordinate of the same strut**, with no aggregation rule needed — and this lane finds exactly
that structure, with the response strictly gradient-order. Orthogonal: the register's "T2 bow"
is the **mechanical bow coordinate of the strut**, explicitly *not* a micro-rotation
(`axiom-register.md`:193 homonym guard, quoted in full in the prereg). The squeeze-twist
ruling proposed a **third** channel — A1 load → **Cosserat `φ`** response — and it is that
third channel, not the register's, that measures zero at leading order. **The register's
bifurcation wording is untouched by this result; it neither gains nor loses support.**

**(b) The FLAG-COMBINE-SPLIT counter-receipts.** `trampoline-framework.md`:255 records the
per-yield-normalized combine (DP-3, Grant-ratified), verbatim `[sic]`: *"the operative engine
`cosserat_field_3d.py`:411,600 computes `A²=ε²/ε_yield²+κ²/ω_yield²` (per-yield-normalized)
with **separate `S_μ,S_ε` kernels** — L2-sum *within* a grade, L∞ (first grade to `S→0`)
*across* grades"*; `axiom-register.md`:232 carries *"**cross-grade combine rule**
underdetermined at `O(α)` (**PR #457**)"*.

The dispatching ruling's position was that the chiral twist makes the aggregation question
moot — *"both kernel budgets load under a 'pure' squeeze; the geometry does the cross-grade
coupling, no aggregation rule required."* **This result removes that route.** Under a pure
squeeze the `κ` budget is loaded at `(qℓ_node)²`, i.e. not at all, so a "pure" squeeze loads
**one** budget. **The counter-receipts are not reframed by geometry — they stand exactly as
written, and the cross-grade combine rule stays open on its existing terms.** The `L∞`
(first-grade-to-yield) reading that the engine implements is, if anything, *reinforced*: when
one grade is loaded 60+ orders harder than the other, `L∞` and normalized-`L2` are
numerically indistinguishable and the first grade to reach `S→0` is unambiguously `ε`.

**(c) Consequence for the ruling's own consequent, stated plainly.** The ruling recorded that
*"the 2026-08-05 kernel-collapse ruling's premise is RESTORED AT LEADING ORDER"* and that
*"the residual leak demotes from an open fork to an O(offset) computable."* **Measured, the
premise is not restored: there is no leading order.** The leak is computable — it is
`S_κ(wall) = 1 − O(10⁻⁵)` at an unphysical ceiling and `1` in practice — and what it says is
that the two budgets are decoupled under a pure squeeze, not co-loaded. **Whether that
retires or re-scopes the kernel-collapse ruling is Grant's call and is not taken here.**

## 9. TWO-METHOD RECEIPTS (regex engine named at every use)

**(1) `ω_yield` has no canonical value.**
- *Method 1 — Python `re`* (`re.search(r'(?i)omega_?yield')` over `src/ave/core/constants.py`): **0 hits**.
- *Method 2 — POSIX ERE, `grep -REn 'omega_?yield|ω_yield' manuscript/ave-kb src/ave/core/constants.py`*: **1 hit**, and it is a **false positive** — `genesis-chord-falsification-ledger.md`:47 matches on *"the **ω**-shear wave + Axiom-4 saturation"*, not on the symbol.
- *Method 2b — `grep -REn 'omega_yield *= *[0-9np.]' src/`*: the engine literals **disagree**: `np.pi` (`test_phase4_asymmetric_saturation.py`:129,202,257,273,325; `rrad_l_counterprop_chiral.py`:144) vs `1.0` (`lattice_decoration_discriminator.py`:113).
- **Conclusion: no `constants.py` symbol, no KB home, two disagreeing engine literals.** Recorded as the lane's single UNDERDETERMINED input.

**(2) No prior corpus computation of a `k=0` compression→twist coefficient on srs.**
- *Method 1 — POSIX ERE, `grep -REn 'compression.?twist|twist.per.strain|squeeze.*twist|twist.*per.*unit.*strain' manuscript/ research/ _orchestration/`*: **0 hits**.
- *Method 2 — Python `re`, `re.IGNORECASE`, widened alternation adding `dilatation.{0,20}micro-?rotation`*: **5 hits** — `vocabulary-register.md`:516, `node-up-small-large-signal.md`:327, `2026-06-20_mass-sector-characterization_synthesis.md`:97, `2026-06-10_foreword-proposal_two-deletions.md`:223, `_orchestration/2026-06-15_wall-branch-fork.md`:57. **All five are sector-**ownership** statements** ("A1 dilatation ⟂ Cosserat micro-rotation"); none computes a coefficient.
- **The two methods disagree in count (0 vs 5), which is precisely why two are required** — and the disagreement is fully accounted for. Prior art that *does* exist is cited, not re-derived: `clm-acgyr1` (`chiral-mechanical-gyrotropy.md`) and the two 2026-07-04 srs elastic-tensor arcs (PRs #506/#508).

## 10. FLAGS (raised verbatim; none silently resolved, none fixed)

**FLAG-1 — a merged, canonized module asserts a zero mode this lane measures as gapped.**
`src/ave/core/micropolar_bloch.py`:175-184, `_acoustic_rotational_subspaces`, verbatim
`[sic]`: *"Uniform micro-rotation about axis al: phi=e_al at every node, u=0 … **Both are
exact zero-eigenvectors of Phi0 for any centro/non-centro lattice (a rigid body costs no
energy).**"* Measured at the geometry-fixed `lever = 1`: the Rayleigh quotient of that exact
vector is **`1.0`**, not `0`. The docstring's parenthetical is the reason it is wrong — a
uniform micro-rotation with `u = 0` is **not** a rigid-body motion (the rigid motion is
`u_n = θ×r_n` *and* `φ_n = θ`, which G3 confirms costs exactly `0.0`). The claim is correct
only at `lever = 0`, where the module measures `0.0`. **Possible consequence, stated as a
question and NOT as a finding:** `micropolar_longwave` places the uniform micro-rotation in
the `Ea` "acoustic + rotational" nullspace and Schur-complements it with an `M_rr` taken from
the `O(k²)` block — if the mode is in fact gapped at `O(k⁰)`, that elimination may overstate
the rotational back-reaction, and the back-reaction is what
`2026-07-04_srs-chiral-micropolar_result.md` reports as *"Δν = +0.10 to +1.1"*. **Not
investigated here, not fixed here, and no claim of an error in that result is made** — the
two computations answer different questions and were not run against each other. Routed.

**FLAG-2 — stale cite in a frozen record.** `2026-07-04_srs-chiral-micropolar_result.md`:93
cites `ℓ_c²=γ/G=6` at `constants.py:298`. At HEAD, `:298` is inside the `OMEGA_C` comment
block and carries no `ℓ_c` content; the content is at `constants.py:338`
(`ELL_C: float = np.sqrt(6.0) * L_NODE`). Line-drift class. The source is a frozen record and
is **byte-untouched** by this lane.

**FLAG-3 — the brief's "PR #884's FLAG-3" names a different item than PR #884's numbered
FLAG-3.** Documented in §4. Read as the rank-2 blocker; the numbering is surfaced, not
reconciled.

**FLAG-4 (inherited, and this lane adds a datum) — the Born absolute-frame rotation fork.**
§2. At `lever = 1` the model is exactly objective; the `#802` rotation cost is the `lever = 0`
value. Grant adjudicates; not adjudicated here.

**FLAG-5 — two gates FAILED AS WRITTEN and were neither retuned nor dropped.** G2 (§2) and
G6 (§3). Both defects are in the gate *specification*, not in the physics, and both are
recorded with the correct comparison shipped alongside (KEEP-BOTH). **No adjudication
criterion was dropped post-hoc to convert a ❌ to a ✅.**

## 11. WHAT THIS LANE DOES NOT LICENSE

- **No propagation.** No manuscript edit, no KB edit, no `src/ave/` edit, no claim-id minted,
  no solidity moved. Canonical propagation is **GATED** on Tier-2 + Grant.
- **No headline.** Per mechanism-claims discipline, nothing here is surfaced as a prediction
  or a chord from a first lane.
- **No statement about canon's SYM gravity class**, which rests on a different (source-side)
  mechanism and is untouched.
- **No statement about `clm-acgyr1`'s magnitude or its `k`-linear pseudo-tensor** — the
  constitutive `B` here is *consistent in band*, not shown identical.
- **No finite-strain claim.** Everything is cold linear plus the canon-forced swapped-spring
  softening at fixed geometry, with that model's fence inherited verbatim.
- **No `Γ_EM` number.** This lane computes the input to `Γ`, not `Γ`.

## Cross-references

- Frozen prereg: `research/2026-08-05_srs-twist-coefficient_prereg-FROZEN.md`
- Ruling record: `_orchestration/docket-entries/2026-08-05-ruling-squeeze-twist.md` (PR #889 branch)
- Parent arcs: `research/2026-07-04_srs-elastic-tensor_result.md` (PR #506), `research/2026-07-04_srs-chiral-micropolar_result.md` (PR #508)
- Canonized sibling object: `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/chiral-mechanical-gyrotropy.md` (`clm-acgyr1`)
- Kernel budgets + `Γ_EM`: `src/ave/topological/cosserat_field_3d.py`:586-587,618-619
- Sector ownership: `manuscript/ave-kb/common/translation-tables/translation-circuit.md`:35
