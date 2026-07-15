# NOTE — Op4 Ladder-Integral Check (Ruling-11 registered check)

**Date:** 2026-07-15 · **Lane:** OP4 LADDER-INTEGRAL CHECK (registered check closing Ruling-11's last loose end)
· **Driver (this check):** [`src/scripts/vol_1_foundations/op4_ladder_integral_check.py`](../src/scripts/vol_1_foundations/op4_ladder_integral_check.py)
· **Kernel imported UNMODIFIED:** `ave.core.universal_operators.universal_saturation` (Op2/Ax4, `S(A)=√(1−(A/A_yield)²)`, `universal_operators.py:75-115`)
· **Op4 under test:** `universal_operators.universal_pairwise_energy` — docstring form `:160-163`, JAX face `:229` (`Z_eff/Z₀ = 1/(1−(d_sat/r)²)^{1/4}`), impl `:182-189`
· **Ruling-11 provenance:** the **step-register ruling**, docket continuation on branch `docs/2026-07-15-walk-batch` (UNMERGED at this HEAD — the branch currently points at `origin/main` `6f203072`, so the ruling text is not yet a distinct committed doc; **cited by branch per the task charter**). Physics content of Ruling-11 as registered: each radial cell is constitutively biased by the **LOCAL FIELD-strain** `A_E(s) = (d_sat/s)²`.
· **Precedent this SHARPENS:** the **field-vs-voltage strain fork** flagged in [`research/2026-07-14_knee-contour-check_NOTE.md`](2026-07-14_knee-contour-check_NOTE.md) `:66-72,240-244` — this check lifts that fork from the *amplitude* level to the *port-expression* level.
· **Register corpus this check consumes:** [`research/2026-07-14_qed-trace-beta-gate_RESULT.md`](2026-07-14_qed-trace-beta-gate_RESULT.md) `:62` (prose — the reactive dress is a local `√(L/C)` impedance ratio) vs `:108,:112` (code/result — reactive register `p≈2.10`, transfer register `p≈4.25`; the `register_flip` sign tension = the open **Q3**).

> **Ordering discipline (no answer-shaping).** This note is committed **hypothesis-first**:
> §1 (hypothesis) + §2 (verdict classes) + §3 (method) are frozen and committed BEFORE the driver is
> run; §4 (results), §5 (what Op4 equals), §6 (implications + downstream flags) are appended in a
> SEPARATE, later commit. The verdict-class thresholds live in the driver's `classify()` (declared in
> code before the run). Git history carries the split. (Same discipline as the knee-check precedent,
> `2026-07-14_knee-contour-check_NOTE.md:10-14`.)

---

## Sector header

**MODE** static two-body **REACTIVE** register — the local **impedance dress** `Z(r)` of the pairwise
line, NOT the through-coupling force (the TRANSFER register `α_eff=F/F_Coulomb` is a separate object,
`qed_trace_beta_gate.py:88`; it is not what Op4's `Z`-form is). **REGIME** cold, **KERNEL ON**
(Op14/Ax4 saturation `S=√(1−A²)` sets each cell's line impedance). **PHASE-STATE** sub-yield / dynamic
regime (`r > d_sat`, strictly OUTSIDE the Pauli wall over the whole test window `r/d_sat ∈ [2,300]`;
the saturated wall `r ≤ d_sat` is out of scope). **SECTOR** E-sector static reactive transmission line
(a graded radial LC line; `Z_local = √(L/C)` per cell). Does the engine carry this DOF? Yes — Op14 is
the per-cell impedance dress and Op4 is its documented radial closed form; this check does not add an
engine, it re-expresses the existing operator as a ladder and integrates it.

**Consistency-vs-emergence tag: CONSISTENCY / CHARACTERIZATION.** No value is minted, no emergence is
headlined. The earnable content is a **functional-form identity**: whether one canonical closed form
(Op4) is the integrated port of one canonical per-cell law (Op14 biased by the Ruling-11 field-strain).
The comparison is `K`-independent (the `K/r` prefactor cancels; only the dimensionless dress `Z/Z₀`
vs `r/d_sat` is compared). This is a self-consistency check of a canonical operator, not a discriminating
gate against data — **no freeze-by-push is required**; hypothesis-first ordering IS required.

---

## 1. Hypothesis (stated FIRST, before any number)

**Op4's impedance dress is the integrated port face of the Ruling-11 field-strain ladder.** Precisely:
build a graded radial lossless transmission line whose cell at radius `s` has local characteristic
impedance dressed by the canonical Ax4 kernel evaluated on the **LOCAL FIELD-strain**:

```
A_E(s)      = (d_sat/s)²                        # Ruling-11 constitutive register; #693/knee-check convention
Z_local(s)  = Z₀ · S(A_E(s))^(±1/2),  S(A)=√(1−A²)   # per-cell line impedance, BOTH sign variants carried
```

Then the **input impedance** `Z_in(r)` seen looking into that graded line from radius `r` out to the far
field (`s → ∞`, where `A_E → 0`, `Z_local → Z₀`) reproduces Op4's documented closed form

```
Z_Op4(r)/Z₀ = 1 / (1 − (d_sat/r)²)^{1/4}       # universal_operators.py:229 ; pairwise-potential.md:20
```

within discretization error over `r/d_sat ∈ [2, 300]`. If the hypothesis holds, the field-vs-voltage
strain fork (knee-check `:66-72`) **closes in Op4's favour**: Op4's `(d_sat/r)²` argument is the *derived
port face* of the field-biased ladder, not an independent voltage-strain choice.

**Amplitude discipline (load-bearing — do NOT invent a strain measure).** Two strains are in play and they
are NOT interchangeable:

- **FIELD-strain** `A_E(s) = (d_sat/s)²` (`∝ 1/s²`) — the amplitude the #693 kernel actually consumes
  (`knee-check NOTE:61-64`: for a unit probe `|E|=K/s²`, `E_yield=K/d_sat²`, so `A=|E|/E_yield=(d_sat/s)²`).
  This is Ruling-11's per-cell bias.
- **VOLTAGE/displacement-strain** `A_V(r) = d_sat/r` (`∝ 1/r`) — the strain Op4's OWN docstring uses
  (`universal_operators.py:160`: *"A(r) = d_sat/r (strain amplitude…)"*).

Op4's argument `(d_sat/r)²` is `A_V²` (voltage-strain squared), NOT `A_E` (field-strain). The hypothesis
under test is whether **integrating a FIELD-strain-biased ladder recovers Op4's argument anyway** — i.e.
whether the ladder integration transforms the `∝1/s²` per-cell bias into Op4's `∝1/r²` port argument.
The rival outcome (rejecting the hypothesis) is that the field ladder integrates to a `(d_sat/r)⁴`-argument
port and Op4 is instead the *local voltage-strain dress*, a structurally different object.

---

## 2. Verdict classes (DECLARED before the computation)

Comparison basis: the exact-ladder port `Z_in(r)` (and its analytic WKB limit) of the **FIELD-strain**
ladder, versus Op4's closed form, over `r/d_sat ∈ [2, 300]`, under BOTH sign variants (`±1/2`, Q3 not
resolved). The primary discriminator is the **recovered argument exponent** `p` in the family
`Z/Z₀ = (1 − (d_sat/r)^p)^{q}` fit to the ladder port (Op4 is `p=2, q=−1/4`; a field-strain dress is
`p=4, q=±1/4`), cross-checked by the pointwise deviation `|Z_in/Z_Op4 − 1|` over the window.

| Class | Criterion | Reading |
|---|---|---|
| **MATCH-FORM** | field-ladder port has `\|p−2\|≤MATCH_P_TOL` **and** `max\|Z_in/Z_Op4−1\| ≤ MATCH_REL` over the window, under BOTH sign variants | Op4's voltage argument IS the derived port face of the field-biased ladder — the fork closes |
| **MATCH-UP-TO-SIGN** | the MATCH-FORM criterion holds under **one** sign variant only | Op4 correct modulo the open Q3 sign selector |
| **PARTIAL** | far zone (`r ≥ FAR_CUT`) agrees within `MATCH_REL` with recovered far-zone `\|p−2\|≤MATCH_P_TOL`, but the near zone (`r ≤ NEAR_CUT`) deviates `> PARTIAL_NEAR_REL` | same family, near-zone dress physics differs — report where/how (the near zone is where the dress lives) |
| **NO-MATCH** | field-ladder port has `\|p−4\|≤FIELD_P_TOL` (or `\|p−2\|>MATCH_P_TOL` structurally) — the WKB limit gives `Z ∝ (1−(d_sat/r)⁴)^{±1/4}`, not `(1−(d_sat/r)²)` | Op4's argument is NOT the integrated field ladder — a genuine register finding on a canonical operator; report what object Op4 DOES equal (candidate: the local voltage-strain dress) + flag downstream consumers |

**Frozen thresholds (in driver `classify()`, declared before the run):**
`MATCH_P_TOL = 0.3` (|p−2|), `FIELD_P_TOL = 0.4` (|p−4|), `MATCH_REL = 2e-2` (pointwise, ~ discretization
band), `PARTIAL_NEAR_REL = 1e-2`, `FAR_CUT = 30.0 d_sat`, `NEAR_CUT = 5.0 d_sat`. Window `R_LO=2.0`,
`R_HI=300.0`. Sample radii for the reported table: `{2, 5, 10, 30, 300} d_sat`.

---

## 3. Method

All physics from `ave.core`: kernel `universal_saturation` (imported unmodified), `Z_0`, `EPS_CLIP` from
`ave.core.constants`. `d_sat = 1.0` is a **native scale normalization** (the operator is scale-free in
`d_sat`; the window is the dimensionless `r/d_sat` — this is not a smuggled physical literal, and the
physical instantiations `D_PROTON` / Slater / `L_NODE` map 1:1 onto it, `knee-check NOTE:74-79`).

1. **Local dress (both registers, both signs).** `Z_local(s) = Z₀·S(A(s))^{sign·½}` with
   `S = universal_saturation(A, 1.0)`; `sign=−1` = rising `S^{−½}` (the Op4 direction, `Z↑→∞` at the
   wall); `sign=+1` = falling `S^{+½}` (the `ε`-load `C_eff=C₀/S ⇒ Z=Z₀√S`, `Z↓→0`). Two strain
   registers: **field** `A_E=(d_sat/s)²` (Ruling-11) and **voltage** `A_V=d_sat/s` (Op4-docstring,
   run as the CONTROL). Q3 is **parameterized, not resolved** (`cosserat_field_3d.py:419-423` flag +
   `qed_trace RESULT:108` register-flip).
2. **(a) Exact ladder recursion.** Graded lossless transmission-line cascade. Log-spaced radial nodes
   `r → R_far`; matched far-field termination `Z_L = Z_local(R_far)`; march INWARD cell-by-cell with the
   line impedance-transform `Z_in = Z_c·(Z_L + iZ_c·tanθ)/(Z_c + iZ_L·tanθ)`, `Z_c = Z_local(cell
   midpoint)`, `θ` = per-cell electrical length. Sweep discretization (`N` cells, `θ`) for convergence;
   report `Re(Z_in(r))` and the residual `|Z_in − Z_local|`.
3. **(b) Adiabatic / WKB limit — derived analytically.** For a slowly-graded lossless line the
   reflection integral (Born/WKB) is `Γ(r) ≈ ½∫_r^∞ (d ln Z_c/ds) e^{−2iβ(s−r)} ds`; when the grading
   scale ≫ wavelength this oscillatory integral → 0, so **the line is reflectionless and `Z_in(r) →
   Z_local(r)`** (the transmission-line adiabatic invariant — an impedance-matched taper presents its
   local characteristic impedance at the port). Hence the analytic port of the FIELD ladder is
   `Z_local(r) = Z₀(1−(d_sat/r)⁴)^{±¼}` and of the VOLTAGE ladder is `Z₀(1−(d_sat/r)²)^{−¼}`. Step (a)
   is the empirical confirmation (Rule 10) that the exact recursion actually reaches this limit.
4. **Recovered exponent.** Fit `p` in `(1−(d_sat/r)^p)^{q}` to each ladder port (log-space LSQ, `q`
   pinned per sign at `±¼`), over the window. Op4 target: `p=2`.
5. **Pointwise comparison.** Op4's dress reconstructed via the canonical kernel
   `Z_Op4/Z₀ = universal_saturation(d_sat/r, 1)^{−½}`, asserted equal to the documented `(1−(d_sat/r)²)^{−¼}`
   to machine precision (the `:229` identity). Report `Z_in` (both field-sign variants) vs `Z_Op4` at the
   5 sample radii, plus the max relative deviation and its radial location; and the VOLTAGE-ladder control
   (should recover Op4, `p=2`).
6. **Verdict** = `classify(...)` on the frozen thresholds. If NO-MATCH/PARTIAL: name the object Op4
   equals, and FLAG (do NOT edit — flag-don't-fix) the downstream Op4/Op14 consumers.
