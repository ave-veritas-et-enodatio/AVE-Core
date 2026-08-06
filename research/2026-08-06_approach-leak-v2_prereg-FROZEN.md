# PRE-REGISTRATION (FROZEN) — APPROACH-LEAK v2: **ONE negative-control tolerance re-anchored SEED-AWARE**, and the bins v1's global consequence clause suppressed

**Date:** 2026-08-06
**Branch:** `research/approach-leak-v2`
**Written against `origin/main` =** `c4fdced0`; **branched from** `research/approach-leak` @ `5e2694c0`.
**Class:** DERIVATION prereg — a **VERSIONED SUPERSEDE of ONE GATE** of a cleared-but-unmerged lane.
**Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; propagates to no KB/manuscript leaf; changes no
solidity; edits no falsification ledger; engine `src/ave` byte-untouched and never imported.**
**SVA pilot case 9.**

**PREDECESSOR (branch `research/approach-leak`, PR #903, `[REVIEW: CLEARED]`, UNMERGED — the ONLY
source of every parameter, gate, tolerance, bin and sweep member below):**

- prereg: [`research/2026-08-05_approach-leak_prereg-FROZEN.md`](2026-08-05_approach-leak_prereg-FROZEN.md) — §2 the derivation, §4 the frozen sweep, §5.3 the gate table, §6 the self-tests, §7 the bins
- result: [`research/2026-08-05_approach-leak_result.md`](2026-08-05_approach-leak_result.md) — §1.3 the `G-NC-SLAST` diagnosis and its NAMED repair, §1.4 the two disclosed implementation infidelities, §7 `FLAG-FREEZE`
- driver: [`research/drivers/approach_leak.py`](drivers/approach_leak.py) → [`research/drivers/approach_leak_results.json`](drivers/approach_leak_results.json)
- number-check: [`research/drivers/approach_leak_number_check.py`](drivers/approach_leak_number_check.py)

**THE PREDECESSOR OF THE PREDECESSOR (read-only; the source of the comparand this lane re-anchors
against):** [`research/drivers/last_bond_kernel_collapse_results.json`](drivers/last_bond_kernel_collapse_results.json),
field `task3_continuum.ladder[0]`; and its driver
[`research/drivers/last_bond_kernel_collapse.py`](drivers/last_bond_kernel_collapse.py):59.

> **THIS FILE IS FROZEN AND PUSHED ALONE**, before any v2 code exists and before any number produced
> by the v2 instrument exists. **No gate, tolerance, bin boundary, frozen numeric parameter,
> comparison-set definition, verdict wording or method element of §2–§8 may be changed after any
> number produced by this lane's instrument is seen. UNRUN ≠ PASSED.**

**WHAT THIS LANE MAY AND MAY NOT DO.** It may re-anchor **exactly one** negative-control tolerance,
in the class the predecessor's own §1.3 named, and — on a full-green table — adjudicate the bins
**exactly as the predecessor froze them**. It may **NOT** move any other tolerance, add a gate to
the physics-certification set, drop a criterion, touch a bin boundary, re-weight a sweep member,
re-open a fork, or edit **any** predecessor artifact. **Every v1 and v0 artifact is BYTE-UNTOUCHED
by this lane, and that is itself gated (§3, `NC-BYTES`).**

---

## §0 — Standard Vacuum Analysis header (SVA v0.2, 11 rows)

 1. **SECTOR / OWNERSHIP:** unchanged from the predecessor and **re-declared, not inherited by
    silence**. The incident/reflected wave is **shear (T2-translational, the `G`-bond channel)**; the
    converted quantity is the **Cosserat micro-rotation `ω`** (channel 4 of `port-register.md`:50,
    the couple-stress / `(2,3)`-winding channel); the conversion operator is the `G_c`
    antisymmetric-strain bond and **nothing else**. **Cross-wiring check re-run:** mass is A1
    dilatation and is NOT in this lane; charge is the Cosserat winding INTEGER and is NOT in this
    lane; the gap `m² = 4G_c/I_ω` is the T2/ω **flywheel clock gap**, explicitly re-scoped away from
    the rest-mass store (`cosserat-mass-gap.md`:149). **★ AND THE SECTOR OF THE OBJECT THIS LANE
    ACTUALLY RE-MEASURES:** `G-NC-SLAST` is a **negative control**, not a physics gate. Its object
    is **an artifact's representation precision**, not a substrate quantity. It owns no sector, it
    crosses no port, and its re-anchoring cannot change one digit of the physics — which is exactly
    why it can be re-anchored without touching anything else.
 2. **★ REGIME / PHASE-STATE — AND THE DOMAIN OF VALIDITY OF THE STATEMENT BEING RE-MEASURED
    (the row-2 discipline this rerun inherits from SVA pilot case 8,
    `2026-08-05_last-bond-g-rho2-rerun_prereg-FROZEN.md` §0 row 2):**
    **MODE / REGIME / PHASE-STATE for the physics** are unchanged and re-declared: small-signal AC,
    a scattering problem at REAL drive frequency, not an eigenvalue problem; sub-yield
    lossless-reactive on `r > r_sat`; the `A ≥ 1` interior is Regime IV and **is not in the domain**;
    cold lattice, Op14 ON as a static constitutive grade, `A(r) = r_sat/r`.
    **★ AND THE REGIME THAT IS THE ENTIRE REPAIR.** A **reproduction gate** is a statement with a
    **domain of validity**, and that domain is bounded **by the precision at which the SOURCE
    SHIPPED its comparand** — not by the precision at which the CONSUMER computes. Demanding a
    reproduction tighter than the source's own shipping precision is **unsatisfiable by any correct
    instrument**: it is an **ARTIFACT-class failure, not a falsification of reproducibility**, in
    exactly the sense this SVA row uses that word.
    **Where the prior measurement sat.** v1 froze `G-NC-SLAST` at `1e-40` relative
    (`2026-08-05_approach-leak_prereg-FROZEN.md` §5.3) against a comparand whose own representation
    ladder tops out at **30 significant decimal digits**, seeded from a rung that carries **17
    significant decimal digits** (§2.1 below). **v1 therefore measured 13 to 23 orders of magnitude
    outside the domain of validity of its own gate.** Its measured `2.04408e-17` is the correct
    reading of a WRONG-REGIME probe: it reports the seed's precision, faithfully, and says nothing
    about whether the reproduction succeeded. This lane's sole content is putting the probe **inside
    the domain**, and then reading the table v1's global consequence clause suppressed.
 3. **CIRCUIT STATEMENT:** unchanged and re-declared. Two coupled reactive ladders sharing a per-cell
    mutual element; ladder 1 (shear) is the certified `[L=ρ][C=1/μ]` line; ladder 2 (rotation) is a
    **series-resonant cutoff line whose cutoff IS the gap**. **A tap into a cutoff line is a reactive
    stub — it stores and returns, it does not carry.** The observable is the **total** relative
    micro-rotation `ε_antisym = A_macro − ω_micro` (one terminal quantity), never the two rotations
    separately. **This lane computes no new circuit quantity**: every physics number it reports is
    **reproduced from the v1 instrument**, not recomputed by a second implementation (§3).
 4. **PLANE & PROJECTION:** unchanged. **NO Γ and NO Z at a wall plane** are declared, so the lane
    inherits no sign convention and reports an **amplitude RATIO and an INTEGER CELL COUNT**, both
    plane-invariant. Nodes at `x_n = (n−1+θ)ℓ_node` outward from `r_sat`, `n = 1` the innermost
    intact cell, byte-identical to the echo-delay v2 placement. **The re-anchored gate's plane** is
    the same innermost intact cell, `n = 1`, `M_ref = 62 M_⊙`, `θ = 1` — **not moved**.
 5. **CONSTITUTIVE PROVENANCE:** every constitutive tag of the predecessor stands **unchanged and
    unre-litigated**: `S(A) = (1−A²)^{1/2}` DERIVED (Ax 4); `A(r) = r_sat/r` DERIVED-FORM /
    VALUE-IMPORTED; `ℓ_node = ħ/(m_ec)` IMPORTED-VALUE / DEFINITIONAL; `ω_C = c₀/ℓ_node` IDENTITY;
    `G_c/I_ω = ω_C²` RULED (A-008 §3.3); `c_R = √2 c₀` DERIVED-ENGINE-FAITHFUL / Grant-ratified;
    `a` and `b` (hence `p`) **UNDETERMINED-CANON and BRACKETED**; FORK-3(b) **OPEN**; the vector band
    top **BRACKETED(pending-ruling)**; the rotational band top **UNDETERMINED-CANON**.
    **★ THE ONE NEW PROVENANCE TAG THIS LANE MINTS, AND IT IS ABOUT AN ARTIFACT, NOT A SUBSTRATE:**
    the predecessor-of-predecessor rung `ell_over_rsat = "6.0238983090250982e-19"` is a **hard-coded
    frozen STRING LITERAL** (`last_bond_kernel_collapse.py`:59), consumed by `mp.mpf(str)` — a
    **decimal** parse. Its upstream provenance is **NOT AUDITABLE from any shipped artifact** (§2.1),
    so it is tagged **`REPRESENTATION-BOUNDED (17 significant decimal digits)`** and **nothing
    stronger is assumed about it anywhere in this lane**.
 6. **ENERGY LEDGER:** **RIM.** Unchanged. Every quantity is a within-system reactive exchange
    between two lossless reactive ladders. **No port is crossed and no loss word is used anywhere in
    this lane.** The re-anchored gate crosses no port because it is a comparison of two decimal
    renderings. The zero-time-averaged-power theorem and its one empirical input (the sign of
    `ω_m² − ω²`, gated by `G-REAL`) are **reproduced, not re-derived**.
 7. **CALIBRATABILITY:** unchanged. `ζ_max` is a dimensionless amplitude ratio; `N_open` is an
    integer; margins are in orders of magnitude of a ratio. **The one place an absolute-modulus ratio
    enters (`2(G_c/G)` in the residual back-action) stays quarantined in its own output field and its
    own bin, exactly as v1 froze it.** **★ And the re-anchored gate is itself ratio-only**: both legs
    of §2 are **relative** separations, and both tolerances are derived from **digit counts**, not
    from any physical scale.
 8. **DISCRIMINATION CLASS:** **DC-internal for the re-anchor** (a reproduction control produces no
    observable); **DC→AC coupling for the physics being adjudicated** (a static DC bias modulating an
    AC transport property). **Tautology filter, run at freeze on the re-anchor itself:** it would be
    circular to re-anchor a gate to a tolerance chosen so that the already-seen `2.04408e-17` fits
    under it. **This lane therefore derives both tolerances from DIGIT COUNTS OF THE SHIPPED STRINGS
    ALONE (§2), states the headroom factor, and freezes them BEFORE running** — and it declares here
    that `2.04408e-17` is **not an input to either derivation**, is not compared against either
    tolerance as a design step, and appears in this file only as the WRONG-REGIME reading it is.
    **SM/GR counterfactual:** unchanged — GR + a matter field has no saturating modulus and no
    rotational gap riding it; the question does not arise there. **Fence:** nothing here is surfaced
    as an AVE-vs-competitor discriminator; the ECO free-reflectivity degeneracy stands (§8).
 9. **CERTIFICATION PLAN:** the re-anchored gate (§2), its **mandatory** fireability self-test (§4.2),
    the negative-control battery (§3) and the determinism gate (§4.3) are frozen here **before any
    line of v2 code exists and before any number produced by the v2 instrument exists. UNRUN ≠
    PASSED.** **★ AND THE ROW-9 SUB-CLAUSE THE PREDECESSOR ROUTED IS APPLIED HERE, WHICH IS THE
    WHOLE POINT:** the pre-freeze second-method check is **extended to the negative-control
    tolerance** — §2.4 evaluates each tolerance's error budget **two independent ways** before any
    run. That extension is the repair `FLAG-FREEZE` named
    (`2026-08-05_approach-leak_result.md`:524-527) and this lane **executes** it rather than
    re-routing it.
10. **ADJUDICATION ROUTING:** **this lane settles exactly two things.** (i) Whether the
    approach-leak lane **certifies** with a correctly-anchored negative control. (ii) On a full-green
    table, **which of the predecessor's four frozen bins fire, on which bracket members** — using the
    predecessor's §7 bin definitions and §7 bin-arithmetic **verbatim and unmodified**. **Nothing
    else is updated.** No fork is adjudicated; no predecessor bin is revisited; no flag is repaired.
    **The propagation consequence** — what the channel-scoped ruling's leak clause resolves to — is
    **RECORDED for the gated propagation pass and NOT EXECUTED here** (§6.3): this lane edits no KB
    leaf, no manuscript file, no solidity, no matrix row, no falsification ledger and no docket other
    than its own fragment. **On any failure in the correct regime, that is reported plainly, with no
    retuning, no re-siting and no second attempt in this lane (Rule 11).**
11. **★ NUMERICAL CONDITIONING:** **NAMED CANCELLATIONS.** All three of the predecessor's are
    inherited **and none is re-implemented** — this lane reaches them through the v1 module itself
    (§3.2), so the two instruments cannot silently diverge: (i) `1 − A²` at the innermost node is
    never formed naively (`ℓ_node/r_sat ≈ 6e-19`; the naive float64 route returns exactly `0` and is
    gated as such by the reproduced `G-COND`); (ii) `1 − (ω/ω_m)²` is formed as a ratio of squares,
    never as a difference of near-equal numbers; (iii) `Σ_n (n−1+θ)^{-2p}` is compared against
    `ψ'(θ)` rather than truncated. **★ AND THE ONE NEW CANCELLATION THIS LANE INTRODUCES, NAMED
    BEFORE IT IS MET:** LEG-A of §2.2 compares two numbers that agree to `~30` significant digits, so
    the **relative** separation `|S_A − S_shipped|/S_shipped` destroys `~30` of the `60` carried
    digits — `30` survive, against a tolerance at `1e-27`, i.e. **`3` decades of surviving precision
    below the tolerance**. That is why the working precision is `dps = 60` and why LEG-A's tolerance
    is not pushed below `1e-27`: **the floor is this cancellation, and it is named here, before it is
    met.** **DYNAMIC RANGE.** Unchanged for the reproduced physics; for the re-anchor:
    `x ~ 6e-19`, `S ~ 1.1e-9`, relative separations in `[1e-58, 1e-12]`. **WORKING PRECISION.**
    mpmath `dps = 60`, obtained by **importing the v1 module's own `mp` configuration** rather than
    re-setting it. float64 appears **nowhere on a verdict path**. **ERROR-PROPAGATION MODEL AND ITS
    METRIC:** unchanged and re-declared — **this lane has no iterated map**; every reported quantity
    is a closed form evaluated once, or a string reproduced from the v1 instrument. The error model
    is round-off-only, bounded by `10^{-58}` relative, and the metric it contracts in is the trivial
    one. **A successor that adds a cascade inherits no contraction argument from here.**
    **REGEX ENGINES NAMED:** METHOD A = `git grep -P` (PCRE, ASCII `\w`); METHOD B = Python `re` on
    `str` (Unicode `\w`); **no pattern in the battery uses `\b`** — inherited by construction,
    because the battery is not re-written, it is re-run through the v1 module (§3.2).

---

## §1 — REFERENTIAL INTEGRITY DECLARATION (frozen before code)

**UNCHANGED from v1 — every one of these is reproduced BYTE-EXACT as a negative control (§3):**

`G-CANON`, `G-NC-BAND`, `G-COND`, `G-COUNT`, `G-ZID`, `G-REAL`, `G-KNIFE`, `G-SUM`, `G-SCAN`,
`G-DET`, `G-RHO-SPECTATOR`, and the entire self-test battery
`FT-COUNT`, `FT-ZID`, `FT-REAL`, `FT-KNIFE`, `FT-COND`, `FT-SCAN`.
**Every tolerance. Every bin boundary and every bin definition. Every frozen numeric parameter.
Every sweep member: the `4`-mass grid, both `θ`, the `65`-point band, all six `p`, both `ρ`-branches,
the `β` bracket, the three-member rotational-top bracket. The whole `6240`-row grid. The whole
pattern battery `P1`–`P5` and its scan surface.**

**CHANGED — exactly ONE thing, and it is a tolerance on a NEGATIVE CONTROL, not on a physics gate:**

> `G-NC-SLAST`: the frozen `1e-40` relative single-leg comparison is **re-anchored SEED-AWARE** to a
> two-leg comparison with tolerances **derived from the digit counts of the shipped strings** (§2).

**ADDED — exactly THREE gate-level things, all three mandated by the rerun brief and all three
declared here (the forced build-wiring change is §1.1, and is not a gate):**

| id | what | why it is not scope creep |
|---|---|---|
| **`FT-SLAST`** | the fireability self-test the re-anchored gate must have (§4.2) | *a gate that cannot fail is not a gate*; v1's `G-NC-SLAST` had **no** self-test, which is a second-order contributor to the freeze error |
| **`G-NC-REPRO`** | byte-exact reproduction of the entire v1 record (§3) | the brief's negative-control requirement; it **adds no physics gate** — it asserts the v1 instrument is unchanged |
| **`G-DET-V2`** | two full v2 runs, identical digest (§4.3) | determinism of the v2 instrument, the direct analogue of v1's `G-DET` |

### §1.1 — ★ THE FORCED SECOND CHANGE, AND WHY IT IS BUILD WIRING AND NOT A GATE CHANGE

**Found while drafting this freeze, before any v2 gate existed, and disclosed here rather than
discovered later.** v1's `make verify` target `verify-approach-leak-number-check` **machine-gates
`G-DET` by re-running the v1 driver via `subprocess` and requiring digest equality**
(`approach_leak_number_check.py`:172-189). The v1 driver's scan surface is
`git ls-files manuscript research src` **minus v1's own six artifacts** — so the shipped digest
`2af8acfe23aabb96` is a function of **how many tracked files exist under those three directories.**

**Consequence, measured at freeze-drafting time with only this prereg added to the tree** (the exact
seven-leaf delta, quoted so a reviewer need not re-run it): `_digest` `2af8acfe23aabb96` →
`973458b3a1648c2a`; `G-SCAN.n_files_scanned` `4418` → `4419`; `scan.P5` hits `5` → `6` on **both**
methods, the sixth being this prereg's own §0 row-5 line. **`make verify` therefore goes RED on any
tree that adds a single tracked file under `manuscript/`, `research/` or `src/` — this lane's, any
concurrently-open lane's, or main's after the merge.** It is `FLAG-SCANFRAG` (§7), it is a **v1
defect and not a v2 one**, and this lane **surfaces it and does not repair it.**

**The forced change, frozen:** in the `Makefile`, `verify-approach-leak-number-check` is **retained
verbatim as a standalone target** (it remains correct, and correct only, on a v1-shaped tree) and is
**replaced in the `verify:` prerequisite list by `verify-approach-leak-v2-number-check`**, which runs
**every check the v1 target ran** — v1's doc-numeral registry, v1's gate-verdict reconciliations,
v1's three-mutation receipt, and v1's `G-DET` machine-gate — by **calling the v1 number-check's own
functions**, with `G-DET` executed **in-process under the §3.2 wrapper**, and adds v2's own checks on
top. **It is a STRICT SUPERSET: no check is dropped, no tolerance is moved, no gate is weakened, and
the v1 number-check module is byte-untouched.** This is **build wiring**, not a gate, tolerance, bin
or clause — and it is named here, before any v2 number exists, so that it cannot later be read as a
convenience.

> ★ **AND THE CONSEQUENCE FOR THIS FILE'S OWN "PUSHED ALONE" DISCIPLINE, DISCLOSED RATHER THAN
> QUIETLY HANDLED.** **The freeze commit is itself the commit that trips `FLAG-SCANFRAG`** — staging
> this prereg puts it in `git ls-files`, which is what the v1 digest gate counts. A literally-alone
> commit would therefore land RED on the repo's own `make verify`. **This prereg is consequently
> pushed with EXACTLY ONE forced build-wiring line and NO code**: the `verify:` prerequisite list
> drops `verify-approach-leak-number-check` for **one commit**, with an inline comment naming this
> flag, and the **next** commit restores it as the strict superset above. **No v2 instrument, no v2
> driver and no v2 number exists at freeze time** — which is the substance the "pushed ALONE" rule
> protects — and the one-commit gate window is named here, before it is opened.

**NOT TOUCHED, and gated as such (`NC-BYTES`, §3.3):** every predecessor artifact, byte-for-byte —
the v1 prereg, v1 driver, v1 results JSON, v1 number-check, v1 result doc, v1 docket fragment, and
the v0 last-bond driver, results JSON, number-check and result doc.

**NOT DRAFTED HERE, BY LANE DISCIPLINE:** the SVA row-9 amendment `FLAG-FREEZE` routed. This lane
**executes** the repair inside its own freeze (§2.4, §0 row 9). **The auditor lands SVA amendments**;
this lane does not draft one.

---

## §2 — ★ THE SEED-AWARE RE-ANCHOR, DERIVED FROM THE SHIPPED ARTIFACTS' REPRESENTATION ALONE

### §2.1 — The comparand's representation ladder (countable by inspection; no computation)

The object `G-NC-SLAST` reproduces is the last-bond lane's shipped `S_last`. Its provenance chain,
read from the shipped artifacts and quoted:

**Rung 0 — the seed.** `last_bond_kernel_collapse.py`:59, verbatim:

```
ELL_OVER_RSAT_LADDER = ["6.0238983090250982e-19", "1e-12", "1e-6", "1e-3"]
```

and `:343-346`, verbatim:

```
for ell_str in ELL_OVER_RSAT_LADDER:
    ell = mp.mpf(ell_str)
    s2_last = s_squared_exact(ell)
```

So the seed is a **hard-coded frozen STRING LITERAL** consumed by `mp.mpf(str)` — a **DECIMAL**
parse at `dps = 60`, not a float64 bit-pattern. **It carries 17 significant decimal digits:
`60238983090250982`.**

> ⚑ **AND WHAT IS *NOT* AUDITABLE, DECLARED AT FREEZE BEFORE IT CAN BE CONVENIENT.** v1's §1.3
> diagnosis attributes this literal to *"the float64 literal `6.0238983090250982e-19` (a
> 17-significant-figure `repr`)"*. **That specific attribution is not supported by any shipped
> artifact:** the string is not the shortest round-tripping `repr` of any IEEE-754 double (the
> shortest repr of the nearest double is `6.023898309025099e-19`, **16** digits), and no shipped
> artifact records how the literal was produced. **v1's diagnosis is correct in KIND — the limiting
> error is the SOURCE's input precision — and unsupported in its specific attribution.** This is
> surfaced, not repaired: it is `FLAG-RUNGPROV` (§7), and the consequence for this lane is that
> **the only defensible bound is the literal's REPRESENTATION precision (17 significant decimal
> digits), with a stated safety factor for the unaudited upstream chain.** No stronger assumption is
> made anywhere below.

**Rung 1 — the comparand.** `last_bond_kernel_collapse.py`:353 renders `S_last_from_exact_S2` through
`_s`, and `:71-73`, verbatim:

```
def _s(x) -> str:
    """mpf -> full-precision decimal string (never a float)."""
    return mp.nstr(x, 30, strip_zeros=False)
```

The shipped string is `0.00000000109762455411903921151585733431` — **30 significant decimal digits:
`109762455411903921151585733431`.**

**★ THE DOMAIN OF VALIDITY, STATED AS A NUMBER.** A reproduction of `S_last` cannot be certified
tighter than `~5×10^{-30}` relative **against the comparand's own rendering**, and cannot be
certified tighter than `~5×10^{-17}` relative **against the seed's own rendering** if the seed is
re-derived rather than re-read. **v1's `1e-40` sat below BOTH floors** — by `10` orders against the
comparand's and by `23` against the seed's. **No correct instrument could ever have passed it.**

### §2.2 — LEG-A: the SEED-EXACT comparison (primary; the reproduction that is actually possible)

**Form, frozen.** Read the seed **PROGRAMMATICALLY** from the shipped JSON field
`task3_continuum.ladder[0].ell_over_rsat`, parse it as `mp.mpf` at `dps = 60`, and push it through
the **algebraically identical** cancellation-free form the v1 module already carries — evaluated by
calling **v1's own `S2_exact` with `r_sat = 1`**, which is `s_squared_exact` of the last-bond driver
term for term:

```
x_r  =  mp.mpf( shipped["task3_continuum"]["ladder"][0]["ell_over_rsat"] )
S_A  =  sqrt( v1.S2_exact(x_r, 1) )   ==   sqrt( x_r*(2 + x_r)/(1 + x_r)^2 )
LEG-A residual  ==  | S_A - mpf(shipped_S_last) | / mpf(shipped_S_last)
```

**Error budget, frozen (two independent evaluations in §2.4):**

| contribution | bound | source |
|---|---|---|
| rendering of the shipped `S_last` at 30 significant digits | `5×10^{-30}` rel | ½ unit in the 30th significant digit |
| mpmath round-off at `dps = 60`, ≤ 8 operations | `< 10^{-58}` rel | round-off-only error model, row 11 |
| **TOTAL BOUND `B_A`** | **`5×10^{-30}` rel** | dominated by the rendering |

**FROZEN TOLERANCE `T_A = 1×10^{-27}` relative. Headroom factor = `T_A/B_A` = `200×`.**
The tolerance is **not** pushed to `B_A`: a gate sited AT its own error bound is a coin flip, and the
`3` surviving decades named in row 11 are the stated margin.

### §2.3 — LEG-B: the SEED-BOUNDED comparison (secondary; the cross-check v1 attempted)

**Form, frozen.** This lane's own `x_ref = ℓ_node/r_sat(62 M_⊙)` at `dps = 60`, computed by the v1
module's own constants and `r_sat()`, compared against the shipped seed; and the corresponding
`S_1 = sqrt(S2_exact(θ ℓ_node, r_sat))` at `θ = 1` compared against the shipped `S_last`:

```
LEG-B(x) residual  ==  | x_ref - x_r | / x_r
LEG-B(S) residual  ==  | S_1   - mpf(shipped_S_last) | / mpf(shipped_S_last)
```

**Error budget, frozen (two independent evaluations in §2.4):**

| contribution | bound | source |
|---|---|---|
| the seed's rendering: ½ unit in the 17th significant decimal digit | `5×10^{-17}` rel on `x` | §2.1 rung 0, digit count |
| the seed's **unaudited upstream chain** (`FLAG-RUNGPROV`) | safety factor **`10×`**, i.e. it absorbs up to `≈450` float64 ulps at `2^{-53} = 1.11×10^{-16}` each | declared, not measured; the chain is not auditable from any artifact |
| **TOTAL BOUND `B_B(x)`** | **`5×10^{-16}` rel** | |
| propagation to `S`: near the wall `S → √(2θx)` so `∂ln S/∂ln x = ½` | **`B_B(S) = 2.5×10^{-16}` rel** | §2.1 of the v1 prereg, near-wall form |

**FROZEN TOLERANCE `T_B = 5×10^{-16}` relative, applied to BOTH LEG-B residuals.**
**Headroom = `1×` on `B_B(x)` (the tolerance IS that bound, the safety factor already being inside
it) and `2×` on `B_B(S)`.**

> **Declared at freeze:** LEG-B is **deliberately the loose leg**. Its job is to certify *"the two
> lanes are talking about the same physical input, to the precision the source published it in"* —
> nothing more. **The reproduction work is done by LEG-A**, at `1e-27`, and the gate rides on both.

### §2.4 — ★ THE PRE-FREEZE SECOND-METHOD CHECK, EXTENDED TO THE NEGATIVE-CONTROL TOLERANCES

*(This is `FLAG-FREEZE`'s named repair, executed. v1's §5.2 covered `p_crit`, `ζ_max` and the `ψ'`
sum and **not** the negative-control tolerances — which is exactly where its error landed.)*

| tolerance | METHOD 1 | METHOD 2 | agree? |
|---|---|---|---|
| `B_A = 5×10^{-30}` | digit count: `mp.nstr(·, 30)` ⇒ ½ ulp at the 30th significant digit ⇒ `0.5×10^{1-30}` | information content: the shipped string has `30` decimal digits, so it partitions the reals into bins of relative width `10^{-29}`; the half-width is `5×10^{-30}` | **YES, identically** |
| `B_B(x) = 5×10^{-16}` | digit count: `17` significant digits ⇒ ½ ulp at the 17th ⇒ `0.5×10^{1-17} = 5×10^{-17}`, × the declared `10` safety | ulp count: an unaudited float64 chain of `k` operations is bounded by `k·2^{-53}`; `5×10^{-16}/1.11×10^{-16} = 4.5`, so the tolerance covers a `4`-operation chain at full half-ulp each, or `450` operations at the `1 %` cancellation level typical of a multiply-divide chain | **YES — and METHOD 2 exposes that a chain longer than `≈4` fully-adverse operations would exceed it, which is the residual risk this lane ACCEPTS and NAMES** |
| `B_B(S) = 2.5×10^{-16}` | `∂ln S/∂ln x = ½` on the near-wall floor `S → √(2θx)` | direct: `S = √(x(2+x)/(1+x)²)`, `d ln S/d ln x = ½·[1 + x/(2+x) − 2x/(1+x)] → ½` as `x → 0` | **YES** |

**Frozen:** `no tolerance in section 2 may be changed after any number produced by this lane's`
`instrument is seen. If LEG-B fails, the FINDING is that the two lanes' inputs differ by more than`
`the source's published precision -- which would be a REAL and REPORTABLE discrepancy about the`
`corpus, not a tolerance to retune (Rule 11).`

---

## §3 — THE NEGATIVE CONTROLS (frozen): byte-exact reproduction of the ENTIRE v1 record

### §3.1 — The criterion

| control | frozen criterion | class |
|---|---|---|
| **`G-NC-REPRO`** ★ | the v1 instrument, re-executed on this branch, reproduces the shipped `approach_leak_results.json` with **EXACT STRING EQUALITY on every leaf**, apart from `_runtime_sec` alone; **`1432` leaves compared, `0` mismatches required**, and the recomputed `_digest` must equal the shipped `2af8acfe23aabb96` | RECOMPUTED |
| **`NC-GATES`** | within `G-NC-REPRO`: every gate block reproduces, **including the `9` gates shipped `pass: true`**, the `1` shipped `pass: false` (`G-NC-SLAST` at v1's own `1e-40` siting — reproducing v1's FAILING value byte-exact is the strongest available proof that only the ANCHOR moved and not the instrument), and the `2` shipped `pass: null` | RECOMPUTED |
| **`NC-FT`** | within `G-NC-REPRO`: **all `6`** self-test blocks reproduce, every field, and every `fires` flag reproduces as `true` | RECOMPUTED |
| **`NC-SCAN`** | within `G-NC-REPRO`: `G-SCAN`'s `n_files_scanned` reproduces as **`4418`** and every `P1`–`P5` hit count, agreement flag and union-hit list reproduces — **so the `I_ω(A)` absence receipt that `UNDERDETERMINED-CANON` rests on is RE-VERIFIED on this branch, not inherited** | RECOMPUTED |
| **`NC-V1DOC`** | the v1 result doc's numerals still reconcile against the v1 shipped JSON, and the v1 gate-verdict reconciliations still hold, **by calling the v1 number-check's own `registry()`, `_scan_doc()` and `ALLOWED_LITERAL`** — so the v1 target's content is preserved under the §1.1 supersession, not dropped | RECOMPUTED-VIA-V1-MODULE |
| **`NC-V1MUT`** | the v1 number-check's own three-mutation receipt still reports every mutation CAUGHT, **by calling `nc1.mutation()` verbatim** | REPLAYED-VERBATIM |
| **`NC-BYTES`** | the SHA-256 of each of the **ten** read-only predecessor artifacts equals its blob hash at `5e2694c0` — this lane touched none of them | FILE-HASH |

**Frozen:** `any single mismatch in any control above => this lane reports LEAK-NOT-CERTIFIED-V2,`
`adjudicates NO bin, and routes to a successor with a new version number.`

### §3.2 — The method, and the ONE declared intervention

**Frozen method.** The v2 driver **imports the v1 driver module unmodified** and calls **its own
`main()`** with `APPROACH_LEAK_OUT` redirected to a temporary path. **No v1 computation is
re-implemented anywhere in this lane** — not the sweep, not the closed forms, not the knife, not the
scan, not the residual sum, not the constants parse. The comparison is `==` on rendered strings, leaf
by leaf, over the whole JSON tree.

> ★ **THE ONE INTERVENTION, DECLARED AT FREEZE.** The v1 scan surface is `git ls-files` over
> `manuscript/ research/ src/` with **v1's own six artifacts excluded by construction** (the pilot-5
> `G-SCAN` repair). **This lane adds five tracked files inside that tree** (its prereg, driver,
> number-check, results JSON and result doc), which would inflate `n_files_scanned` above `4418` and
> destroy the reproduction for a reason that carries **no information**. The v2 driver therefore
> wraps **`v1._tracked_files`** with a filter that additionally drops **this lane's own six
> artifacts** — restoring the v1 scan surface **exactly** — and **changes nothing else in the v1
> module.** The wrapper is the pilot-5 self-reference repair applied to a second lane, not a new
> method. **It is disclosed in the shipped v2 JSON, verbatim, in its own field.**
> **Consequence, frozen:** `n_files_scanned` **must** reproduce as `4418`. If it does not, the
> intervention is wrong and `G-NC-REPRO` **fails** — the wrapper is therefore itself gated, not
> assumed.
> **Empirical necessity, established at freeze-drafting time and quoted in §1.1**: without the
> wrapper the delta is exactly seven leaves, and two of them (`n_files_scanned`, `scan.P5`) are pure
> self-reference. **The wrapper removes information-free noise and nothing else, and the `4418` gate
> is what makes that claim checkable rather than assertable.**

### §3.2.1 — The structural repair this lane NAMES and does NOT execute

The wrapper fixes **this** lane. It does not fix the **next** one: a third lane adding a tracked file
under the three scan directories breaks the reproduction again, one generation later. **The
structural repair is to pin the scan surface to a COMMIT rather than to the worktree** — enumerate
the surface with `git ls-tree -r <ship-commit>` restricted to the scan directories, which is
deterministic forever and immune to any later addition. **That repair belongs in the v1 driver, which
this lane may not edit, so it is NAMED here, ROUTED as `FLAG-SCANFRAG`, and NOT EXECUTED.**

### §3.3 — The read-only artifact roster (`NC-BYTES`)

`research/2026-08-05_approach-leak_prereg-FROZEN.md`,
`research/2026-08-05_approach-leak_result.md`,
`research/drivers/approach_leak.py`,
`research/drivers/approach_leak_results.json`,
`research/drivers/approach_leak_number_check.py`,
`_orchestration/docket-entries/2026-08-05-approach-leak.md`,
`research/drivers/last_bond_kernel_collapse.py`,
`research/drivers/last_bond_kernel_collapse_results.json`,
`research/drivers/last_bond_kernel_collapse_number_check.py`,
`research/2026-08-05_last-bond-kernel-collapse_result.md`.

---

## §4 — THE GATE TABLE (frozen; **UNRUN ≠ PASSED**)

### §4.1 — The re-anchored gate

| gate | frozen criterion | tolerance |
|---|---|---|
| **`G-NC-SLAST`** (v2) ★ | **LEG-A** — `S_last` recomputed from the shipped seed through the identical cancellation-free form reproduces the shipped `S_last` | **`1×10^{-27}` rel** (§2.2) |
| | **LEG-B(x)** — this lane's mass-derived `ℓ_node/r_sat` at `62 M_⊙` reproduces the shipped seed | **`5×10^{-16}` rel** (§2.3) |
| | **LEG-B(S)** — this lane's `S_1` at `M_ref, θ = 1` reproduces the shipped `S_last` | **`5×10^{-16}` rel** (§2.3) |
| | **VERDICT** | **PASS iff ALL THREE legs pass.** Any leg failing ⇒ the gate FAILS. |

**Also reported, NON-GATED:** whether `mp.nstr(S_A, 30)` is **string-identical** to the shipped
`S_last` rendering. **This is a diagnostic and the gate does not ride on it** — a 30-digit rendering
can tie at its last digit, and freezing a gate on a tie is exactly the class of error this lane
exists to repair.

### §4.2 — The fireability self-test (MANDATORY; a gate that cannot fail is not a gate)

| self-test | frozen firing condition |
|---|---|
| **`FT-SLAST`** ★ | **two parts, BOTH required to fire.** **(i) COARSE** — perturbing the shipped seed by a relative `1×10^{-12}` must make **LEG-A FAIL** (expected residual `≈5×10^{-13}`, `15` decades above `T_A`) **and LEG-B(x) FAIL** (expected `≈1×10^{-12}`, `3.3` decades above `T_B`). **(ii) FINE** — perturbing the shipped `S_last` comparand by a relative `1×10^{-26}` must make **LEG-A FAIL** (`1` decade above `T_A`) while **LEG-B is untouched and still passes** — which proves `T_A` is **non-vacuous at its own scale** and not merely satisfied by a comparison that can never separate. |

### §4.3 — Determinism

| gate | frozen criterion |
|---|---|
| **`G-DET-V2`** | two full v2 runs, identical digest, byte-identical output apart from `_runtime_sec`; **machine-gated on every `make verify`** by the v2 number-check re-running the v2 driver into a temporary path |
| **`G-DET-V1-WRAPPED`** | v1's own `G-DET` machine-gate, preserved under the §1.1 supersession: the v1 driver re-run **in-process under the §3.2 wrapper** must reproduce the shipped digest `2af8acfe23aabb96`. **This is the same criterion the v1 Makefile target enforced, at the same tolerance (identity), executed where it can still be true.** |

---

## §5 — THE CERTIFICATION DECISION (frozen wording; applied mechanically)

**The approach-leak lane certifies as `LEAK-CERTIFIED-V2` if and ONLY if ALL of the following hold:**

1. `G-NC-SLAST` (v2) passes on **all three legs**;
2. `FT-SLAST` **FIRES on both parts**;
3. `G-NC-REPRO` reports **zero mismatches** over all `1432` leaves, and the recomputed digest equals
   `2af8acfe23aabb96` (which is simultaneously `G-DET-V1-WRAPPED`);
4. within it, **every one of the `9`** v1 gates shipped `pass: true` reproduces as `true`, **all `6`**
   self-tests reproduce as `fires: true`, and `n_files_scanned` reproduces as `4418`;
5. `NC-V1DOC` and `NC-V1MUT` pass — **the v1 target's content is preserved, not dropped, under the
   §1.1 supersession**;
6. `NC-BYTES` passes on all ten read-only artifacts;
7. `G-DET-V2` passes.

**Otherwise this lane reports `LEAK-NOT-CERTIFIED-V2`, adjudicates NO bin, and routes to a successor
with a new version number. No tolerance is retuned after a number is seen.**

### §5.1 — ★ THE CONSEQUENCE CLAUSE — a v2 CHOICE, stated as such, and NOT a retro-edit

v1's frozen consequence (`2026-08-05_approach-leak_prereg-FROZEN.md` §5.3) is **GLOBAL**, verbatim:

> *"any RUN gate FAILS, or any self-test fails to fire, or any gate is UNRUN ⇒ this lane reports
> `LEAK-NOT-CERTIFIED`, adjudicates NO bin, and routes to a successor with a new version number. No
> tolerance is retuned after a number is seen."*

**That clause STANDS AS FROZEN IN v1 and is not edited, annotated or reinterpreted by this lane.**
v1 honoured it and this lane does not second-guess that.

**v2 elects to RETAIN the GLOBAL form of the consequence, unweakened.** This is a **v2 choice**,
recorded here before any v2 number exists, and it is the **stricter** of the two options the corpus
norm allows: with a correctly-anchored tolerance there is no reason to buy an escape hatch, and a
per-task scoping frozen *by the lane that would benefit from it* is exactly the shape of a
post-hoc criterion drop. **The one and only carve, and it is a DEFINITION of the comparison set
rather than an exemption from a consequence:** the `own_artifacts_excluded` roster question is
**settled at freeze by §3.2's gated wrapper**, so there is no declared-different field at all and no
leaf is exempt from `G-NC-REPRO`.

---

## §6 — THE ADJUDICATION PROTOCOL ON A FULL-GREEN TABLE (frozen)

**The bins are the predecessor's, used VERBATIM.** `GAP-CLOSED` / `CHANNEL-OPENS` /
`SCALE-UNDERDETERMINED` / `UNDERDETERMINED-CANON`, defined at
`2026-08-05_approach-leak_prereg-FROZEN.md` §7. **No boundary is moved. No bin is added, renamed or
merged. No member of the `p` bracket is preferred.**

**The bin-arithmetic is the predecessor's, used VERBATIM** (`ibid.` §7):

> *"if different members of the `p` bracket land in different bins, the result doc reports BOTH bins,
> states exactly which members give which, and reports `UNDERDETERMINED-CANON` as a co-firing bin
> naming the exponent that decides it. It does NOT pick a member. It does NOT report a single
> headline bin unless every member of the bracket agrees."*

### §6.1 — What this lane may award, mechanically

1. **Per-member bins**, read off the reproduced `sweep.per_p` block: a member with `N_open = 0` at
   every one of its swept rows is `GAP-CLOSED`; a member with `N_open ≥ 1` at any row is
   `CHANNEL-OPENS`. **A member whose verdict SPLITS on a swept parameter is reported as SPLIT, with
   the splitting parameter named** — it is not collapsed to either bin.
2. **`UNDERDETERMINED-CANON` co-fires** iff the `NC-SCAN`-re-verified absence receipts show a needed
   grading law absent; the missing laws are **ENUMERATED exactly** with the two-method receipts and
   both engines named.
3. **`SCALE-UNDERDETERMINED` co-fires on the residual back-action field and on that field alone**,
   exactly as v1 quarantined it (`ibid.` §2.6 frozen block). **It is not extended to any other
   field**, and the result doc must state that every other number in the lane is ratio-only.
4. **The `p ≥ 2` members are quoted with their ANALOGY declaration at every site**, per the v1
   freeze: *"the RHO-B analogy for `I_omega` is DECLARED HERE AS AN ANALOGY AND NOT AS CANON"*.
5. **The rotational-top bracket is reported MOOT where it is moot** rather than silently dropped, per
   the v1 freeze.

### §6.2 — Hand-evaluated at freeze, so the adjudication is read as a CHECK

**Frozen expectation, stated before the v2 run:** the reproduction is byte-exact, so the bins follow
from v1's already-shipped `sweep.per_p` block with no new physics. The expected award is
**`GAP-CLOSED` co-firing with `UNDERDETERMINED-CANON`** on the below-knife family — **every member
canon or the engine actually states** (the dispatch's `p = 1/2`, the engine's coded `p = 1`, and the
`p = 1.5` filler) — with **`CHANNEL-OPENS` on `p = 2.5` and `p = 3`**, both of which require an
`I_ω ∝ S^{-3}` law that appears nowhere, and **`p = 2` SPLIT on `θ` alone**, decided by the frozen
criterion `Ω < 4θ`. **`SCALE-UNDERDETERMINED` co-fires on the residual prefactor `2(G_c/G)` and
nowhere else.** **Any departure from this hand-evaluation is an instrument finding requiring
diagnosis, and is reported as such rather than absorbed.**

### §6.3 — The propagation consequence: RECORDED, NOT EXECUTED

On a full-green table the channel-scoped kernel-collapse ruling's leak clause
(`_orchestration/docket-entries/2026-08-05-ruling-kernel-collapse-rescope.md`:16-18) resolves to **the
bounded evanescent form, with the knife-edge caveat**. **The exact resolved wording is RECORDED in
the v2 result doc for the gated propagation pass and is NOT EXECUTED here.** This lane edits **no**
KB leaf, **no** manuscript file, **no** ruling docket entry, **no** solidity, **no** matrix row and
**no** falsification ledger. **The auditor lands corpus-state entries; this lane surfaces the
finding.**

---

## §7 — FLAGS (frozen policy: carried by POINTER, not restated, not repaired)

**Carried forward UNCHANGED and UNREPAIRED, by pointer to their v1 bodies at
`2026-08-05_approach-leak_result.md` §7:** `FLAG-EXP`, `FLAG-IOMEGA`, `FLAG-MECH`, `FLAG-ROTTOP`.
**This lane does not restate them, does not re-litigate them, and does not fix them.** The v1 bodies
are the citable text.

**`FLAG-FREEZE` is DISCHARGED by this lane** — its named repair is executed in §2.4 and §4.2. **Its
v1 body stays byte-untouched** (Rule 12: the v1 record is the v1 record); the discharge is recorded
in the v2 result doc, not written back into v1.

**`FLAG-SCANFRAG` — NEW, minted at freeze in §1.1, surfaced and NOT repaired.** v1's `G-DET`
machine-gate makes `make verify` a function of the number of tracked files under `manuscript/`,
`research/` and `src/`. **Any** later commit adding one anywhere in that tree turns it RED — this
lane's, a concurrent lane's, or main's after merge. **The named structural repair (§3.2.1: pin the
scan surface to a commit, not to the worktree) belongs in the v1 driver, which this lane may not
edit.** ROUTED to the orchestrator. **Flag-don't-fix:** this lane wraps its own reproduction and
supersedes the build wiring with a strict superset (§1.1); it does **not** patch v1's driver, does
**not** regenerate v1's shipped JSON, and does **not** relax v1's digest criterion.

**`FLAG-RUNGPROV` — NEW, minted at freeze in §2.1, surfaced and NOT repaired.** The last-bond rung
literal's upstream provenance is not auditable from any shipped artifact, and v1's "float64 `repr`"
attribution is not supported by one. **Flag-don't-fix:** this lane bounds by representation and names
the residual risk (§2.4 METHOD 2); it does **not** patch the last-bond driver, does **not** re-derive
the rung, and does **not** edit v1's diagnosis.

---

## §8 — THE FENCE (frozen; what this lane does NOT license)

1. **Nothing about the rotational channel AT or INSIDE `r_sat`.** The domain stops at the innermost
   intact cell. The ruling's carve-out and its ROUTED penetrating-radiation frontier item are
   untouched; **MeV-scale rotational radiation is OUT OF SCOPE** — one cross-reference line, as v1.
2. **No adjudication of the cross-grade aggregation fork** (L∞ vs normalized-L2), of FORK-3(b), of
   the `β` bracket, of the `K(A)` fork, of `FLAG-CAUSAL`, or of any predecessor's bins.
3. **No promotion of the engine's coded `a = 2` to canon**, and **no invention of an `I_ω(A)` law**.
   The `p ≥ 2` members exist to bracket. The RHO-B `1/S³` grading is applied to the micro-inertia
   **by ANALOGY and is labelled an analogy at every site it appears.**
4. **No AVE-vs-competitor discrimination claim.** The ECO free-reflectivity degeneracy carried at
   `2026-08-05_echo-delay-v2-reach-through_result.md`'s headline applies here unchanged.
5. **No KB, manuscript, ruling-docket or `src/ave` edit; no predecessor-artifact edit.**
6. **No claim minted.** No `clm-`/`def-`/`exp-`/`sup-`/`ilk-`. No solidity moved.
7. **No SVA amendment drafted.** Routed to the auditor lane, as v1 routed it.

**Deliverables — the COMPLETE list of files this lane may create or modify:**

- this prereg (frozen, pushed **ALONE**, before any v2 code exists);
- `research/drivers/approach_leak_v2.py` + `research/drivers/approach_leak_v2_results.json`;
- `research/drivers/approach_leak_v2_number_check.py` (gating, with a mutation receipt);
- `research/2026-08-06_approach-leak-v2_result.md`;
- `_orchestration/docket-entries/2026-08-06-approach-leak-v2.md`;
- `Makefile` — one appended target, the §1.1 `verify:` prerequisite supersession, and the shared
  lines whose union-conflict class is DISCLOSED (the docket fragment records it verbatim).

**Nothing else. Any file outside this list appearing in the diff is a freeze violation.**
