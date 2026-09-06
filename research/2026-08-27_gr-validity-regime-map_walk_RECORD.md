# WALK RECORD — where GR is validated on the strain-regime ladder (2026-08-27)

**Status: WALK-GRADE, UNAUDITED. Nothing here is a claim, a ruling, or a
solidity move.** The audit charter is §7 and the routing item is
[`_orchestration/open-items/2026-08-27-gr-regime-map-audit.md`](../_orchestration/open-items/2026-08-27-gr-regime-map-audit.md).
This record **supersedes nothing**; only Grant rules.

**Provenance.** Grant, in chat 2026-08-27: *"regimes of strain? GR is valid for
linear?"* The orchestrator answered at walk grade; this lane was dispatched to
**sweep canon first and document only the delta**.

**Grading key.** `[CANON]` verified at file:line on this branch ·
`[MEASURED-ELSEWHERE]` a sibling lane's result, cited to its branch ·
`[WALK]` the orchestrator's reading, unaudited ·
`[EXTERNAL]` outside-corpus numbers, sourced or marked unsourced ·
`[ARITH]` computed on this branch from canon's own definitions.

---

## §0 — SWEEP VERDICT: canon already had most of this

**The one-line answer to the dispatch's key question:** canon **does** map bodies
that GR is tested on onto its own regime ladder, with numbers, in
[`domain-catalog.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md)
§Gravitational and §Gravitational Waves. What no site my method reached does is
attach **GR's measurement PRECISION** to those rows, or state the program
consequence that follows. **So this record is a delta record, not a lens
record**, and it is written short.

**Of the orchestrator's four walk items:**

| item | disposition |
|---|---|
| **1** — GR's validated domain is the weak field | **canon has the substrate half**, not the precision half (§1, §6) |
| **2** — clause G is nonlinear by construction, linearizes at `D(A)→1` | **★ ALREADY CANON, verbatim, in two places** — stands down (§2). One framing residue survives |
| **3** — the four-row map | **three of four rows are canon**; row 2 is mis-bound to the wrong nonlinearity (§3) |
| **4** — the program consequence | **canon states it for the BH rung**; the ladder-wide form is new (§5) |

**What is genuinely new is in §4, and it is not what the walk proposed.** Three
findings, all from reading canon against itself: a boundary-radius arithmetic
canon never writes down (**DELTA-1**), a same-leaf coordinate collision that
puts one object in Regime I and Regime IV (**DELTA-2**), and a wrong regime
assignment on the flagship GR test in canon's own GR-observable regime table
(**DELTA-3**). DELTA-2 and DELTA-3 are surfaced, not fixed.

**Success shape.** The dispatch said that if canon already carries the whole
thing, the deliverable is a pointer and that is a success. Canon carries most of
it. The record is written accordingly: §1–§3 are mostly pointers, §4 is the
payload.

## §1 — What canon carries (the ladder, and where GR's bodies sit on it)

**Pointers, not restatement.** Every row below was opened and read on this
branch.

**The ladder itself** — [`four-regimes.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md):26–29,
claims `clm-b2anl4` / `clm-2dwzib`, **solidity 0.63, build-band `input-only`**
(`manuscript/ave-kb/.index/claims.jsonl`). Verbatim names and cuts: `[CANON]`

| I | Linear | `r < √(2α)` | `S > 0.993` | **Standard equations** |
| II | Nonlinear | `√(2α) ≤ r < √3/2` | | **Axiom 4 active** |
| III | Yield | `√3/2 ≤ r < 1` | | Phase transition |
| IV | Ruptured | `r ≥ 1.0` | `S = 0` | Topology destroyed |

with `r ≡ A/A_c` and `S(r) = √(1−r²)`. Note the names: **II is "Nonlinear" and
III is "Yield"** — §4 DELTA-3 turns on this.

**Where GR's test bodies already sit** — [`domain-catalog.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md)
§Gravitational (`A = ε₁₁ = 7GM/c²r`, `A_c = 1`), claim `clm-82dxbj`, **solidity
0.63, `input-only`**: `[CANON]`

- `:50` Solar surface `ε₁₁ = 1.486×10⁻⁵` — **Regime I**
- `:51` White dwarf (Sirius B) `≈1.81×10⁻³` — **Regime I**
- `:52` *"Neutron star (1.4 M⊙, R = 10 km): ε₁₁ ≈ 1.46 --- Regime IV"*
- `:53` Black hole at `r_s`: `ε₁₁ = 7/2 = 3.5` — **Regime IV**

and §Gravitational Waves (`A = h`, `A_c = h_yield = √α ≈ 0.0854`), `:120`:
*"LIGO detections (h ~ 10⁻²¹) correspond to r ~ 10⁻²⁰ --- the most deeply linear
measurement in physics. A neutron star merger at the surface (h ~ 0.01) reaches
r = 0.117 < √(2α) = 0.121 --- still in Regime I. … A strong merger at h ~ 0.02
(r = 0.23) enters Regime II."*

**So canon already answers the dispatch's key question in the affirmative for
the SUBSTRATE side.** It places solar-surface, white-dwarf, neutron-star,
black-hole and LIGO on the ladder with numbers. **What it does not do at any
site my method reached is attach GR's measurement precision to those rows** —
see §6 and the method statement in §9.

**Two adjacent taxonomies swept, both orthogonal to this question:**

- [`temporal-saturation-regime-classifier.md`](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md)
  (`clm-f0jwtk`, **solidity 0.50, `input-only`**) — the lossless/cyclic/lossy
  **temporal** axis. Its §Operational-note table already reads *"Solar system at
  `A_gm ~ 10⁻³⁴` → Regime I"*, and its own honesty rider grades the whole leaf
  **Class 1 (definitional construct)**, *"TAXONOMIC, not derivational."* `[CANON]`
- [`wall-taxonomy.md`](../manuscript/ave-kb/common/wall-taxonomy.md) §4 —
  organizes by **axis** (space / amplitude / frequency / length-scale) and
  **channel**, and its operational rule is the relevant discipline here,
  verbatim: *"Before asserting a wall anywhere: name (i) the **channel**, (ii)
  the **axis** it lives on, and (iii) the **phase-state** (cold/sub-yield vs
  saturated)."* `[CANON]`

**And canon states the whole-program consequence for one rung already** —
[`lattice-extreme-bh-rationality.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md):74,
verbatim: *"A faithful substrate must recover GR where GR is established. …
**the lattice is rational at its limit** (CONSISTENCY). It is NOT a new
prediction … The framework's *own* content lives in the **departures**."*
`[CANON]` §5 is what is left over after that sentence.

## §2 — Item 2 (the structural reading) — STANDS DOWN to canon, with one residue

The walk's item 2 was flagged as *"the part most likely to be new."* **It is
not.** Both halves are canon, byte-verified on this branch.

**(a) The equation, including the `4π`.** `[CANON]`
[`manuscript/common_equations/eq_axiom_5.tex`](../manuscript/common_equations/eq_axiom_5.tex):75–77,
the ratified Substrate DC Bias clause **G**, verbatim:

```latex
    \mathbf{u}_0 = -\mathcal{A}_g\nabla\varepsilon_{11},\qquad
    -\nabla\cdot\!\left[\kappa\, D(A)\,\nabla\varepsilon_{11}\right] = 4\pi\,T_{00},\qquad
    \kappa = \frac{c^4}{7G}
```

The walk's stated form matches this, `4π` included.

> **⚑ Do not "fix" the KB relay.** [`axiom-register.md`](../manuscript/ave-kb/common/axiom-register.md):361
> still reads `−∇·[κD(A)∇ε₁₁] = T₀₀` with a **bare `T₀₀`**. That is a *verbatim
> quotation of the pre-R49(a) ratified text and is deliberately byte-untouched*
> — the carve is stated in `eq_axiom_5.tex`'s own R49(a) dated fragment
> (*"the CANONICAL file is corrected in place with the fragment as its audit
> trail, while every VERBATIM QUOTATION of the ratified clause is left
> byte-untouched"*). The same fragment carries an **already-open** flag to the
> ruling author about whether that carve was authorised. Nothing here reopens it.

**(b) The `D(A)→1` linearization.** `[CANON]`
[`saturating-modulus-and-backreaction.md`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md):64,
verbatim: *"In the weak field ($r\gg r_{\text{sat}}$: $A\to0$, $S\to1$, $D\to1$)
the correction **vanishes** and the linear GR core is reproduced identically
(**consistency**)."* The same leaf's §1 opens by calling the linear chain *"the
**weak-field limit**"* in its own words. `eq_axiom_5.tex`'s phase-structure
paragraph says it a third way: *"(b) At the saturation boundary: $D(A)$ carries
clause G's response into the graded regime."*

**And canon carves the regime condition apart from the state condition
explicitly** — `eq_axiom_5.tex`, clause Q, verbatim: *"Clause Q is a statement
about the substrate's **state**; it is not a claim that small-signal
linearisation is valid, which is a **separate, separately-declared regime
condition**."* `[CANON]` That sentence is the corpus already holding the
distinction the walk proposed.

### ⚑ The walk's premise is mis-attributed — flag, not fix

The walk states: *"Prior lanes described it as 'linear Poisson with a constant
modulus,' which is the cold-regime LIMIT, not the equation."*

**The prior lane read the site it cited correctly.** That phrase is
[`research/2026-08-11_gravity-linearity-audit_result.md`](2026-08-11_gravity-linearity-audit_result.md):188,
and it labels **`gordon-optical-metric.md`:25**, which is
`-\left(\frac{c^{4}}{7G}\right)\nabla^{2}\epsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)`
— **byte-verified on this branch; there is no `D(A)` in it.** *"Linear Poisson
with a CONSTANT modulus"* is an accurate description of that equation.

**The same audit separately licenses the kernel form and says so.** `:215`
licenses `backreaction.md`:50–53 (`D = 1/S`) as *"Kernel on the **MODULUS**.
Correct role, correct place … No conflict"*, and `:195` quotes the `D→1`
sentence and adds *"This site does not *compete* with the linear chain — it
explicitly **defers** to it."*

**So the real structure is two written equations at two sites, not one equation
misread**: a linear-Poisson site that canon uses for the weak-field observable
chain, and a `D(A)`-graded site that reduces to it. Whether canon *should* carry
one law with two spellings is a live question — it is **not** a defect of the
prior lane's reading, and the record does not carry it as one.

### ⚠ Status caveat that must ride with any use of `D(A) = 1/S`

`saturating-modulus-and-backreaction.md`:59 (the **BULK stiffens**, `D=1/S→∞`
row) carries **🔴 DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION**. The
demotion's own scope note, verbatim: *"The static elliptic `D(A)` dress profile
itself survives (bound-response FORM)"* — what is demoted is the **divergent-
bulk-modulus-halts-the-collapse stability argument**, whose carrier (a
propagating A1/bulk branch) clause G replaces with a bound response. `[CANON]`

### The one residue that survives as new

`[WALK]` **The LOCATION contrast: GR puts its nonlinearity in the FIELD
EQUATION (`G_μν` nonlinear in `g`); AVE puts its in the CONSTITUTIVE LAW (the
saturation kernel grading the conductance `κD(A)`).** I found no corpus site
stating this contrast (§9 states the search and its blind spot). It is a
**framing claim, not a result** — it produces no number and predicts nothing on
its own. Audit item **A2**.

## §3 — THE MAP, row by row, regraded

The walk proposed a four-row map. Three rows survive; one is mis-bound.

### Row 1 — cold / linear / sub-yield

`[CANON]` **AVE side:** Regime I is *"Standard equations"*
([`four-regimes.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md):26),
and every solar-system and binary-pulsar body sits there by canon's own
`ε₁₁ = 7GM/c²r` (§1, and §4 DELTA-1 for the boundary).

`[MEASURED-ELSEWHERE]` **The AVE-must-match half is where the live work is.**
`research/2026-08-27_ppn-tensor-derivation_result.md` on branch
`research/2026-08-27-ppn-tensor-derivation` @ `50cb25c7` reports `γ_light = 1`
(pass), `γ_matter = 0` and `β = 3/2` (refuted), and its ★ FORWARD POINTER
records a repair on the sibling branch `research/2026-08-27-two-knob-gravity-repair`
@ `849f6a97`. **Cited, not restated** — those lanes own their evidence, and the
repair's own caveat rides with it, verbatim: *"`(a₁, b₁, b₂) = (2, 1, ½)`
currently WORKS. Nothing yet FORCES it."*

### Row 2 — ⚑ MIS-BOUND: two different nonlinearities in one row

The walk pairs *"nonlinear approach — ~10% (LIGO)"* with *"`a₂ = 2` vs GR
`9/4`."* **Those are not the same nonlinearity, and only one of them is a regime
statement.**

- **`a₂` is a post-Newtonian ORDER coefficient in the weak field.**
  `[MEASURED-ELSEWHERE]` `research/2026-08-27_two-knob-gravity-repair_result.md`
  @ `849f6a97`:214 — *"exact isotropic Schwarzschild has grading exponents
  `(a₁, a₂, b₁, b₂) = (2, 9/4, 1, ½)`"*, against the exponential ansatz's
  `a₂ = 2`. The expansion is in `U = GM/c²r` with `U ≪ 1`. On canon's gravity
  ladder that is **Regime I** — the same row as row 1, not a second row.
- **And the same lane says the divergence is invisible to a slow orbit**, `:96`
  verbatim: *"**`a₂` drops out of the NR precession entirely.** … So GR's exact
  isotropic `a₂ = 9/4` and the exponential repair's `a₂ = 2` are indistinguishable
  here — a real difference that shows up only at relativistic speeds."*
- **The Axiom-4 saturation nonlinearity is a different object** — it is
  `Regime II`, `A ≥ √(2α) = 0.1208`, `Axiom 4 active`, and canon already places
  a strong merger there via the GW-strain domain (`domain-catalog.md`:120).

**Regraded row 2:** the AVE-distinct content at *post-Newtonian order* is
`a₂ = 2` vs `9/4`, unmeasured and only reachable at relativistic orbital speeds;
the AVE-distinct content at *saturation order* is the Regime-II entry canon
already writes. **Keeping them in one row is the mistake `wall-taxonomy.md` §4's
operational rule exists to prevent** — it mixes the *amplitude* question with an
*expansion-order* question and calls both "nonlinear."

### Row 3 — saturated: `r_sat = 7GM/c² = 3.5 r_s`

`[CANON]` and **the fence the dispatch asked for is already written**, in
[`wall-taxonomy.md`](../manuscript/ave-kb/common/wall-taxonomy.md):168, verbatim:

> *"the owning claim is **`clm-law1ho`, solidity 0.55, build-band `input-only`**
> — canon's own wording, *"use as input only, don't build deeper"* — and canon
> **scopes the falsifier itself**: `r_sat = 3.5 r_s` is a **shear-mode + matter**
> boundary, **NOT photon-geometric**; *"EHT shadow / photon-ring radius do NOT
> discriminate `r_sat` from `r_s` (prior EHT-falsifier overclaim retracted
> 2026-05-16 per Grant audit)."* **Do not read the falsifiability line as an
> open observational test on the photon channel.**"*

The two-channel reconciliation behind it is
[`lattice-extreme-bh-rationality.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md)
§6: `r_s = 2GM/c²` is where the **transverse/EM** quantity `n−1` reaches 1;
`r_sat = 7GM/c²` is where the **shear+bulk** `ε₁₁` reaches 1. **The "factor-3.5
disagreement" is therefore not one quantity disagreeing — it is two channels'
walls, and canon says so.** `[CANON]`

### Row 4 — ruptured

`[CANON]` on the ladder (`r ≥ 1`, `S = 0`, *"Topology destroyed"*). ⚑ **But the
walk's spelling — `> V_snap` — puts row 4 on the AMPLITUDE axis while row 3 is
on the SPACE axis**, and lands inside a threshold question canon has already
flagged open: `four-regimes.md`:60 identifies `r₃ = 1.0` with **`V_yield`**,
while the leaf's own `:82`–`:89` residue notes that the 2026-06-30 `def-vyvsn1`
adjudication places Schwinger/pair-nucleation at **`V_snap`**, and flags two of
its own lines as honesty-lag against it. **Anyone carrying row 4 must carry that
flag; this record does not resolve it.**

## §4 — ★ THE DELTAS — what the sweep shows is NOT in canon

Three findings. None is what the walk proposed. **DELTA-2 and DELTA-3 are
surfaced, not fixed** (flag-don't-fix); neither is adjudicated here.

### DELTA-1 `[ARITH]` — canon's gravity-ladder boundaries, expressed as radii

Canon writes the ladder in `r = A/A_c` and the gravity amplitude as
`ε₁₁ = 7GM/c²r` with `A_c = 1`. **Composing them gives a radius for each
boundary. I found no site that writes those radii down** (method + blind spot:
§9). Arithmetic on canon's own two definitions, `α = 7.2973525693e-3` from
`src/ave/core/constants.py`:163:

| landmark | `ε₁₁` | `r` in `GM/c²` | `r/r_s` |
|---|---|---|---|
| **Regime I → II** (`ε₁₁ = √(2α)`) | `0.120809` | `57.943` | **`28.97`** |
| **Regime II → III** (`ε₁₁ = √3/2`) | `0.866025` | `8.0829` | **`4.042`** |
| **Regime III → IV** (`ε₁₁ = 1`) `= r_sat` | `1.000000` | `7.0000` | **`3.500`** |
| ISCO, Schwarzschild `a* = 0` | `1.1667` | `6` | `3` |
| photon sphere | `2.3333` | `3` | `1.5` |
| horizon `r_s` | `3.5` | `2` | `1` |

**Three readings that fall straight out and that I did not find stated anywhere:**

1. **Regime I ends at ~29 `r_s`** — far outside the horizon, and far outside
   anything GR is precision-tested on. `[ARITH]`
2. **Regime III (Yield) is a thin shell**, `3.500 r_s` to `4.042 r_s` — about
   half a Schwarzschild radius thick. Regime II owns the whole span from
   `4.04 r_s` out to `28.97 r_s`. `[ARITH]`
3. **ISCO and the photon sphere are both INSIDE `r_sat`** on this ladder, i.e.
   both sit in Regime IV. `[ARITH]` This is arithmetic, not a claim about
   observables — and it must be read through the §3 row-3 fence, which scopes
   `r_sat` to the **shear + matter** channel. Anyone tempted to turn it into an
   observational statement should read `wall-taxonomy.md`:168 first.

> ### ⚠ THE CAVEAT THAT MUST RIDE WITH DELTA-1 — stated before the audit finds it
>
> **`ε₁₁ = 7GM/c²r` is the Green's-function solution of the LINEAR equation**
> (`D = 1`; `gordon-optical-metric.md`:25, and `saturating-modulus-and-backreaction.md`
> §1 calls that chain *"the **weak-field limit**"*). Using it to locate a boundary
> where `D ≠ 1` **uses the weak-field profile outside its own validity.** Quantified
> `[ARITH]`:
>
> | boundary | `A` | `D(A) = 1/√(1−A²)` | is the linear profile OK there? |
> |---|---|---|---|
> | I → II | `0.1208` | `1.0074` | **yes** — modulus off by 0.7% |
> | II → III | `0.8660` | `2.0000` | **no** — the modulus has doubled |
> | III → IV (`r_sat`) | `1` | `→ ∞` | **no** — the equation is singular there |
>
> **So the `28.97 r_s` row is self-consistent and the two inner rows are
> idealizations.** They are *canon's own* idealization — `domain-catalog.md`:53
> computes `ε₁₁ = 3.5` at `r_s` from the same linear profile, and `r_sat = 7GM/c²`
> is *defined* that way — so DELTA-1 inherits the corpus's convention rather than
> introducing one. **But no row inboard of `~29 r_s` should be quoted as a solved
> radius of the graded equation.** Audit item **A7**; the graded profile is what
> `src/ave/gravity/backreaction.py` relaxes for, and nothing in this record ran it.

**Cross-check that the arithmetic is canon's, not mine:** the same formula at
the solar surface returns `ε₁₁ = 1.4862×10⁻⁵`, which reproduces
`domain-catalog.md`:50's corrected value; and at `r_s` it returns `7/2 = 3.5`,
reproducing `:53`. `[ARITH]` + `[CANON]`

### DELTA-2 ⚑ `[CANON]` — the gravity sector has at least FOUR control parameters, and they are compared against ONE boundary

Enumerated by reading the leaves named below, not by pattern-matching (§9):

| # | control parameter `A` | `A_c` | site | a worked value |
|---|---|---|---|---|
| 1 | `ε₁₁ = 7GM/c²r` — static radial bias, near zone | `1` | `domain-catalog.md`:45–47 | solar surface `1.486×10⁻⁵` |
| 2 | `h` — GW strain, **far** zone | `√α = 0.0854` | `domain-catalog.md`:116–118 | LIGO `r ~ 10⁻²⁰` |
| 3 | `g_N/a₀` — Newtonian accel. vs MOND scale | `a₀` | `domain-catalog.md`:126–128 | galactic rotation |
| 4 | `A_gm` — gravitomagnetic (Lense–Thirring) phase-strain | (vs `0.121`) | `orbital-lc-friction-paradox.md`:12,:18 | solar system `~10⁻³⁴` |

**The reader hazard, in one line: the SAME PLACE reads Regime I on one parameter
and Regime IV on another, and no leaf my method reached carries a sentence
saying so.**

- **The Sun**: `ε₁₁ = 1.49×10⁻⁵` (#1) versus `A_gm ~ 10⁻³⁴` (#4). Both verdicts
  are "Regime I" — but they are **29 orders of magnitude apart in
  distance-from-the-boundary**, and `orbital-lc-friction-paradox.md`:14 reads the
  smaller one as *"infinitely deep inside Regime I."*
- **A neutron-star surface**: `domain-catalog.md`:52 — *"Neutron star (1.4 M⊙,
  R = 10 km): `ε₁₁ ≈ 1.46` --- **Regime IV**"*; `:120` — *"A neutron star merger
  **at the surface** (`h ~ 0.01`) reaches `r = 0.117 < √(2α) = 0.121` --- still
  in **Regime I**."* **Same leaf, same body, same words "at the surface,"
  opposite regimes.**

**This is not a contradiction** — the leaf is organised per-domain and each
domain is internally self-consistent; `h` is a far-zone radiated amplitude and
`ε₁₁` is a near-zone static bias, and they are entitled to differ. **It is a
missing reconciling sentence on a leaf whose whole job is regime
classification**, and it is exactly the failure `wall-taxonomy.md` §4's
operational rule exists to prevent (*"name (i) the channel, (ii) the axis …
(iii) the phase-state"*).

**And it bites this very walk.** The walk's row-2 entry *"LIGO merger peak
`U ~ 0.1–0.3`"* is a **near-zone compactness** statement; canon's LIGO row is a
**far-zone wave strain**. Two different coordinates, and the walk read them as
one row. `[WALK]` → corrected in §3.

### DELTA-3 ⚑ `[CANON]` — canon's GR-observable regime table puts Mercury in the wrong regime, under the wrong name

[`orbital-regime-table.md`](../manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/orbital-regime-table.md):16
(claim `clm-qyn8t0`, **solidity 0.55, `input-only`**), verbatim:

```
| Mercury precession | II (Yield) | $\Delta\phi$ = 43''/century | Exact match with GR |
```

**Two independent defects on one line.**

1. **The NAME is wrong against the canonical ladder.**
   `four-regimes.md`:27–28 names Regime **II "Nonlinear"** and Regime **III
   "Yield."** The same table's next rows carry the same off-by-one — `:18` reads
   *"III (Rupture)"* where `:29` names IV "Ruptured."
2. **The ASSIGNMENT is wrong by about six orders of magnitude.** On canon's own
   gravity control parameter, Mercury's orbit `a = 5.7909×10¹⁰ m` gives
   `ε₁₁ = 7GM_⊙/(c²a) = 1.785×10⁻⁷` `[ARITH]`, i.e. `1.5×10⁻⁶` of the way to the
   Regime I/II boundary at `0.1208`. **Mercury is deep Regime I.**

**Why it matters more than a typo:** this is the one table my search found that
maps a *GR observable* to an AVE regime, and it mis-files **the flagship
solar-system GR test**. A reader answering Grant's question from that table gets
"the classic GR test is nonlinear/yield," which inverts the answer.

⚑ **Routed, not fixed.** Both defects are surfaced with receipts; neither is
edited by this lane, and the owning leaf's author reading `four-regimes.md`
decides the repair.

### Residue from §2 `[WALK]`

The nonlinearity-**location** contrast (GR: field equation; AVE: constitutive
law) is the one framing statement I found no corpus site making. It is audit
item **A2** and produces no number.

### Homonym warning, noted in passing `[CANON]`

`r_sat` names **two different radii** in canon: `7GM/c²` (the BH saturation
boundary, this record) and `√(GM_⊙/a₀) ≈ 7,400 AU` (the solar Axiom-4 onset
radius, `vol3/cosmology/ch06-solar-system/index.md`:11, whose Oort-containment
framing was **retracted 2026-08-03**). Do not fuse them.

## §5 — The program consequence

**Canon already states it for one rung.** `[CANON]`
[`lattice-extreme-bh-rationality.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md):74,
verbatim: *"A faithful substrate must recover GR where GR is established. …
**the lattice is rational at its limit** (CONSISTENCY). It is NOT a new
prediction; the ringdown match in particular is consistency, not confirmation.
The framework's *own* content lives in the **departures**."* The same leaf's §7
names the departures: *"$2/7$ compactness, $\Gamma_{shear}=-1$ echoes, $7GM$
Iron-K$\alpha$ inner edge."*

**The ladder-wide form is what §4 buys.** `[WALK]`, and audit item **A5**:

> The row with data precise enough to distinguish anything is **Regime I** — and
> by DELTA-1 that row runs from **`28.97 r_s` outward**. AVE's own content, by
> canon's own sentence above, lives **inboard of that**, in Regimes II–IV, where
> `wall-taxonomy.md`:168 records that the surviving falsifiers are
> **shear + matter** channels only and the photon channel is silent.

**Consequence for how agreement should be read.** `[MEASURED-ELSEWHERE]` The
sibling lane
`research/2026-08-27_ppn-tensor-derivation_result.md` (**not on this branch** — link deliberately omitted)
on branch `research/2026-08-27-ppn-tensor-derivation` @ `50cb25c7` builds the
per-step derived-vs-imported ledger for the solar-system chain (its §1.1 shared
trunk, rows **T1 / T3 / T5 / T7**, each tagged `IMPORTED` at the site with its
own receipt). **Cross-referenced, not restated** — that lane owns its evidence
and its §1.4 states its own conclusion in its own words.

> ⚑ **One dispatch phrasing I could not reproduce verbatim.** The dispatch says
> the corpus *"anchors gravity to GR at **three separate points**, all in the
> linear row."* **I found no such sentence, and no such count, in that result
> doc** (searched: the string `three`, and the string `anchor`, over the whole
> file; §9 states the method). The ledger it points at tags **four** shared-trunk
> rows `IMPORTED`, of which two (`K = 2G`, `κ = c⁴/7G`) are GR-value imports, one
> is the posited source law and one is Gordon 1923. **The count is the reader's
> to take from the ledger; this record does not assert one.** Recorded as a
> partial reproduction rather than silently restated, per flag-don't-fix.

**What the consequence is NOT.** It is not a claim that agreement in Regime I is
worthless — recovering a well-tested theory in its own regime is the minimum
bar, and canon's own sentence says so. It is a claim about **where a
discriminating test can live**, and DELTA-1 gives that region a radius for the
first time in the corpus my method reached.

## §6 — The GR-domain numbers: what I could source and what I could not

The dispatch said to verify these myself and mark any I could not source.
**External retrieval was NOT performed** — this program routes prior-art
retrieval through a gated pipeline, and self-fetching would bypass that gate.
So every external figure below is either **arithmetic I ran**, **second-hand
from a sibling lane that itself declined to re-fetch**, or **marked unsourced
and routed**.

| walk figure | status | basis |
|---|---|---|
| solar system `U = GM/rc² ~ 10⁻⁶ … 10⁻⁸` | **`[ARITH]` CONFIRMED** | `U(R_⊙) = 2.123×10⁻⁶`, `U(1 AU) = 9.874×10⁻⁹`, `U(Mercury a) = 2.551×10⁻⁸`. Inputs `G`, `c`, `M_SUN` from `src/ave/core/constants.py`:110,:132; `R_⊙ = 6.957×10⁸ m` IAU nominal, the same value `domain-catalog.md`:55 uses |
| binary pulsars `~10⁻⁶` | **`[ARITH]` on UNRETRIEVED inputs** | `2.14×10⁻⁶` for `M_tot = 2.828 M_⊙`, `a = 1.950×10⁹ m` (PSR B1913+16). **The orbital elements are carried from discipline knowledge and were NOT retrieved this lane.** The arithmetic is mine; the inputs are not receipted |
| LIGO merger peak `U ~ 0.1–0.3` | **`[ARITH]` GEOMETRIC, conditional** | `U = 1/2` at `r = r_s`, `1/4` at `2 r_s`, `1/6` at `3 r_s`. The band `0.1–0.3` is separations `≈1.7–5 r_s`. **That mergers peak in that separation band is discipline knowledge, not retrieved** |
| LIGO **"~10% waveform precision"** | ★ **`[EXTERNAL]` UNSOURCED** | **I could not source this and did not retrieve it.** Routed to the gated external-retrieval pipeline as audit item **A4**. Nothing in this record depends on it |
| "GR's `10⁻⁵`-precision domain" | **`[EXTERNAL]` SECOND-HAND** | Cassini `γ − 1 = (2.1 ± 2.3)×10⁻⁵` appears at `research/2026-08-27_ppn-tensor-derivation_result.md` §1.2 row L7 (branch `research/2026-08-27-ppn-tensor-derivation` @ `50cb25c7`), where it is itself tagged `IMPORTED` with the site's own note *"Not re-fetched by this lane"*. LLR `β = 1 ± 1.1×10⁻⁴` from the same doc's §0 table. **Second-hand at two removes; treat as tentative-standing** |
| "nothing measured inside a horizon" | **DEFINITIONAL** | no causal signal reaches an exterior observer from inside; not an empirical claim requiring a source |

**GR-test precision figures inside the KB.** My search (tokens `Cassini`,
`Lunar Laser`, `LLR`, `Bertotti` over `manuscript/ave-kb`) returned figures of
this class at **one** KB site:
[`translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md):156
— *"WEP-CMRR `~10⁻¹⁵` (Eötvös / MICROSCOPE), SEP-CMRR `~10⁻⁴` (LLR-Nordtvedt,
finite)"*. `[CANON]` **That is a statement about my search, not about the
corpus**: a leaf stating a precision without any of those four tokens would not
be returned. §9.

**Net for the walk's item 1.** The claim *"GR's `10⁻⁵`-precision domain IS the
linear regime"* is **supportable on the substrate side and second-hand on the
GR side**. The substrate half is §1 + DELTA-1 and is receipted. The GR half
rides two unreceipted externals and one unsourced figure. **Do not headline item
1 until A4 closes.**

## §7 — ★ AUDIT CHARTER (attack instructions + kill conditions)

Nothing in §4 or §5 reaches a prereg, a leaf, or a solidity move before this
runs. Every item carries **what would kill it**.

| # | claim | class | how to attack it | ★ KILL CONDITION |
|---|---|---|---|---|
| **A1** | DELTA-1's boundary radii (`28.97 / 4.042 / 3.500 r_s`) are correct arithmetic **and** are not written at any canon site | `[ARITH]` + COMPLETENESS | re-run the arithmetic independently. Then search for the radii by a **different method than §9's** — e.g. read `ch7-regime-map/` and `vol3/gravity/ch01-gravity-yield/` end to end rather than grepping | **KILLED (novelty)** if any site states the I→II or II→III boundary as a radius. **KILLED (arithmetic)** if `7/√(2α) ≠ 57.94 GM/c²`. The two kills are separate; report which |
| **A2** | The nonlinearity-**location** contrast (GR: field equation / AVE: constitutive law) is real and not in canon | `[WALK]` FRAMING | sweep for it. Then attack it **adversarially**: analogue-gravity recasts GR's nonlinearity as an effective medium and Gordon's own metric is that move — so is the "location" a structural fact or a choice of formulation? Apply the **consensus-bias symmetric standard** | **KILLED** if the contrast is formulation-dependent, i.e. if one can exhibit the same physics written either way. A framing that survives only in one gauge is not a structural statement |
| **A3** | DELTA-2: four gravity control parameters, one boundary, and **no reconciling sentence** on the leaf | CANON READING | read [`domain-catalog.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md) and the whole `ch7-regime-map/` index **end to end**, not by search | **KILLED** if a reconciling sentence exists anywhere in ch7. **PARTIALLY KILLED** if the four-parameter enumeration is wrong — report the corrected set, do not just say "more than four" |
| **A4** | The LIGO "~10% waveform precision" figure | `[EXTERNAL]` UNSOURCED | route through the **gated external-retrieval pipeline**; do not self-fetch | Not kill/survive — **it either sources or it stays unsourced**. But if the real figure is far from 10%, §3 row 2's *"unmeasured"* framing has to move, and this record is wrong about it |
| **A5** | The ladder-wide program consequence (§5) | LOGIC + DISCRIMINATION | apply **`ave-discrimination-check`**: does this buy a number, organizing power, or neither? Apply the **consensus-bias symmetric standard**: SM/QED also calibrate in the tested regime and claim content outside it — would this be flagged there? | ★ **KILLED AS A FINDING** if it reduces to *"AVE is untested"*. A statement that the distinctive content lives where no data exists is a restatement of untestedness unless a **reachable** observable is named. **Name one or record the kill** |
| **A6** | DELTA-3: `orbital-regime-table.md`:16 is wrong on both the regime NAME and the ASSIGNMENT | CANON READING | verify both. Then check whether an **alternate naming convention was in force** when that leaf landed (git log the leaf; check `regimes-of-operation.md`, which uses *"Weakly non-linear / Strongly non-linear / TVS breakdown"*) | **DEFECT (1) KILLED** if a documented alternate convention covers it. **DEFECT (2) SURVIVES REGARDLESS** — `ε₁₁ = 1.785×10⁻⁷` is six orders from the boundary under every convention in the corpus |
| **A7** | DELTA-1's inner rows, and the ISCO / photon-sphere reading | NUMERICAL | ★ **read-and-run**: relax [`src/ave/gravity/backreaction.py`](../src/ave/gravity/backreaction.py) and get the **graded** `ε₁₁(r)` profile. Compare the actual `A = √(2α)`, `√3/2` and `A → 1` radii against the linear-profile values in the table | **KILLED** if the graded radii differ materially from `4.042 / 3.500 r_s`. The `28.97 r_s` row should survive (`D = 1.0074` there); **if it does not, DELTA-1 fails entirely** |
| **A8** | This record's own §2 mis-attribution finding | LOGIC | check that `gordon-optical-metric.md`:25 really carries no `D(A)`, and that the 2026-08-11 audit really licenses both sites. Then ask the harder question this record ducked: **should canon carry one bias law with two spellings?** | **KILLED** if the two sites are in fact one equation and the prior lane did mis-read it — in which case the walk's item-2 premise is right and §2 is wrong |

**Also required of the audit, per standing discipline:** the
**structural-null stencil lens** on A7 (a graded elliptic solve on a Cartesian
stencil is not the K4 operator — `saturating-modulus-and-backreaction.md` §3
states the native-`Grad` requirement), and **PML/interior-cell exclusion** if any
field-density extraction is done.

## §8 — What this record does NOT do

- It **mints nothing, moves no solidity, edits no canonical file.**
- It **does not fix** DELTA-2 or DELTA-3. Both are surfaced with receipts and
  routed to their leaves' owners and to Grant.
- It **does not adjudicate** the `V_yield`/`V_snap` residue at
  `four-regimes.md`:82–89, the `4π` relay carve at `axiom-register.md`:361, or
  the R40-B2a `D(A)` demotion. All three are pre-existing, all three are cited
  where they bear.
- It **does not restate** the PPN or two-knob lanes' evidence. Those lanes own
  their results; this record points.
- It **does not claim** that Regime-I agreement is worthless, nor that AVE
  predicts anything in Regimes II–IV. §5 is a statement about **where a test
  could live**, gated on **A5**.
- It **asserts no completeness.** Every "I found no site" is a statement about
  the method in §9.

## §9 — METHOD, and its blind spots

**What was read end to end** (12 files): `four-regimes.md`,
`domain-catalog.md`, `temporal-saturation-regime-classifier.md`,
`orbital-regime-table.md`, `regimes-of-operation.md` (first 60 lines, then the
regime tables), `strain-registers.md` (§0–§3), `eq_axiom_5.tex` clause block +
its R49(a) fragment + derivation-grade note, `saturating-modulus-and-backreaction.md`
§1–§3 + the R40-B2a demotion block, `lattice-extreme-bh-rationality.md` §4–§7,
`wall-taxonomy.md` §4–§6, `research/2026-08-25_autonomous-harmonic-balance-lens_RECORD.md`
(structure mirror), and `research/2026-08-11_gravity-linearity-audit_result.md`
§3.

**What was read in neighbourhoods only**: `axiom-register.md` (the clause-G
region and the Axiom-5 row), `research/2026-08-27_ppn-tensor-derivation_result.md`
(§0, §1.1–§1.4, §5.3, §6), `research/2026-08-27_two-knob-gravity-repair_result.md`
(the `a₂` neighbourhoods), `manuscript/ave-kb/.index/claims.jsonl` (solidity
lookups), `src/ave/core/regime_map.py` (the domain-example block),
`src/ave/core/constants.py` (the named constants).

**What was searched, and with what.** `grep -rn` over `manuscript/`, `research/`
and `src/` for: `Clause G`; `clm-law1ho`; GR-validity phrasings
(`GR (is|remains|stays) (valid|correct|exact|recovered)`, `where GR (is|breaks)`,
`GR'?s? (validated|tested|validity|domain of validity)`); nonlinearity-location
phrasings; `Cassini|Lunar Laser|LLR|Bertotti`; the numeric tokens `28.9`,
`57.94`, `8.083`, `4.042`; and a two-method cross-check for DELTA-1's absence
(numeric-token grep **and** a per-file scan for leaves co-mentioning `r_sat` with
`√(2α)`/`0.121`, which returned 15 files, each inspected).

**Blind spots, named.**

1. **A leaf stating a GR-test precision without the tokens `Cassini`, `LLR`,
   `Lunar Laser`, `Bertotti` would not be returned by §6's search.** The §6 KB
   result is a statement about that search.
2. **DELTA-1's absence claim rests on token and co-mention searches**, not on
   reading `ch7-regime-map/` and `vol3/gravity/` end to end. A leaf writing
   `r = 57.94 GM/c²` in a different normalization (e.g. `29 r_g`, or in `ℓ_node`)
   would be missed. That is exactly what **A1** must close by a different method.
3. **DELTA-2's "four control parameters" is an enumeration from the leaves I
   read**, not a corpus census. There may be more. **A3** must enumerate, not
   confirm.
4. **No engine was run.** Every number here is closed-form arithmetic on canon's
   written definitions. The graded profile that **A7** needs is unrun.
5. **`git grep` pathspec globs and shell-escaped `$…$` patterns are a measured
   false-negative source in this workspace.** Where a search underpins a
   negative claim above, a second method is stated; where it is not, the claim is
   phrased as a statement about the search.
6. **The PPN and two-knob lanes' numbers were accepted as reported**, not
   reproduced. They are tagged `[MEASURED-ELSEWHERE]` with branch and SHA.
