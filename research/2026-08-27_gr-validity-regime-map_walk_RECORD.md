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

## §4 — ★ THE DELTAS — what the sweep shows is NOT in canon

## §5 — The program consequence

## §6 — The GR-domain numbers: what I could source and what I could not

## §7 — ★ AUDIT CHARTER (attack instructions + kill conditions)

## §8 — What this record does NOT do

## §9 — METHOD, and its blind spots
