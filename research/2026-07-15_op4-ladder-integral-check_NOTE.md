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

---

## 4. Results

**Driver as-run:** window `r/d_sat ∈ [2,300]`, far-field termination `R_far=3000 d_sat`, discretization
sweep `N ∈ {400,1200,4000,12000}` at per-cell electrical length `θ=0.30`, both `S^{±1/2}` sign variants,
both strain registers. Output `assets/sim_outputs/op4_ladder_integral_check.{json,png}` (gitignored,
regenerable). Kernel `universal_saturation` imported unmodified; `Z_0`/`EPS_CLIP` from `ave.core.constants`;
`make verify` green at HEAD; the test `src/tests/test_op4_ladder_integral_check.py` (6 cases) green.

> **TL;DR (verdict §4.4): `NO-MATCH`.** The FIELD-strain ladder (Ruling-11 register) integrates to a port
> of exponent **`p = 4.000`** — `Z_in(r) = Z₀(1−(d_sat/r)⁴)^{±¼}` — under **both** sign variants, whereas
> Op4 is **`p = 2`** — `Z₀(1−(d_sat/r)²)^{−¼}`. The exponents are structurally different (quartic vs
> quadratic argument), and the mismatch is **sign-independent** (the Op4-direction rise variant is still
> `p=4`), so `MATCH-UP-TO-SIGN` does not apply. Op4's argument is **NOT** the integrated field ladder.
> §5 identifies what Op4 *does* equal (the local VOLTAGE-strain dress, `p=2`, reproduced exactly by the
> voltage-register control ladder). No value minted (CONSISTENCY class).

### 4.1 The exact ladder converges to the local WKB dress (adiabatic invariant, confirmed empirically — Rule 10)

The exact transmission-line cascade `Re(Z_in(r))` converges monotonically to the analytic WKB local
dress `Z_local(r)` as the discretization refines, in **both** registers — confirming step (3)'s derivation
that a matched adiabatic taper presents its local characteristic impedance at the port, and that **no
ladder-integration transforms the per-cell argument**:

| register (@ `r=2 d_sat`) | WKB local `Z_local` | `N=400` resid | `N=1200` | `N=4000` | `N=12000` |
|---|---:|---:|---:|---:|---:|
| field-strain rise `S^{−½}` | 382.858 Ω (= 1.01626 `Z₀`) | 9.83e-2 | 1.11e-2 | 1.00e-3 | **1.12e-4** |
| VOLTAGE control `S^{−½}` (= Op4) | 404.823 Ω (= 1.07457 `Z₀`) | 1.67e-1 | 1.88e-2 | 1.70e-3 | **1.88e-4** |

The field ladder reaches `(1−(d/r)⁴)^{−¼}·Z₀`; the voltage ladder reaches Op4. The recursion is faithful
to the local dress in each case — the difference between them is entirely in the per-cell strain, not in
any integration effect.

### 4.2 Recovered argument exponent `p` in `(1−(d_sat/r)^p)^q`

| register / sign | recovered `p` (q pinned) | fit SSE | vs Op4 (`p=2`) |
|---|---:|---:|---|
| field-strain rise `S^{−½}` | **4.000** | 3.9e-31 | `p=4 ≠ 2` |
| field-strain fall `S^{+½}` | **4.000** | 5.8e-31 | `p=4 ≠ 2` |
| VOLTAGE control (Op4's own register) | **2.000** | 3.4e-31 | `p=2` — recovers Op4 |

### 4.3 Pointwise port table (5 sample radii, `Z_in/Z₀`)

| `r/d_sat` | Op4 (`p=2`, voltage) | field-rise ladder (`p=4`, `S^{−½}`) | field-fall ladder (`p=4`, `S^{+½}`) | voltage-ctrl ladder |
|---:|---:|---:|---:|---:|
| 2   | 1.074570 | 1.016263 | 0.983997 | 1.074565 |
| 5   | 1.010258 | 1.000400 | 0.999600 | 1.010257 |
| 10  | 1.002516 | 1.000025 | 0.999975 | 1.002516 |
| 30  | 1.000278 | 1.000000 | 1.000000 | 1.000278 |
| 300 | 1.000003 | 1.000000 | 1.000000 | 1.000003 |

Max relative deviation of the field dress from Op4: **rise 5.43e-2 @ `r=2`** (near zone), 2.62e-4 in the
far zone (`r≥30`); **fall 8.43e-2 @ `r=2`**, 2.63e-4 far. The deviation grows monotonically toward the
wall and vanishes far. The voltage-control ladder reproduces Op4 to `~5e-6` (validating the recursion).

### 4.4 Verdict — `NO-MATCH`

`classify()` → **NO-MATCH**. The field-strain ladder port is `p=4.000` (both signs, fit exact to `1e-31`),
structurally distinct from Op4's `p=2`. Neither sign variant reaches Op4 — the argument mismatch (quartic
vs quadratic in `d_sat/r`) is orthogonal to the `S^{±½}` sign, so the finding is decisively NO-MATCH, not
MATCH-UP-TO-SIGN. This is precisely the NO-MATCH example the class definition anticipated: *"the WKB limit
gives `Z ∝ (1−(d/r)⁴)^{±1/4}` from the local field-strain, not `(1−(d/r)²)`."*

---

## 5. What object Op4 DOES equal (the honest identification)

**Op4's `Z₀(1−(d_sat/r)²)^{−¼}` is exactly the LOCAL VOLTAGE-strain dress.** With the voltage/displacement
strain `A_V = d_sat/r` fed *directly* into the canonical kernel, `Z = Z₀·S(A_V)^{−½} = Z₀(1−(d_sat/r)²)^{−¼}`
— Op4, identically (`test_op4_ladder_integral_check.py::test_op4_dress_is_canonical_kernel_identity`, `rtol=1e-12`).
The voltage-register **control ladder** integrates to this same form (`p=2.000`, reproduced to `~5e-6`, §4.1/4.3),
so Op4 **is** a legitimate ladder port — but of the **VOLTAGE/displacement register** (`A ∝ 1/r`), NOT of
Ruling-11's **FIELD register** (`A_E ∝ 1/r²`). This is self-consistent with Op4's own provenance:

- Op4 docstring `universal_operators.py:160` — *"A(r) = d_sat/r (strain amplitude…)"* — voltage-strain.
- qed-trace expansion `2026-07-14_qed-trace-beta-gate_RESULT.md:112` — *"`Z/Z₀−1 ≈ ¼(d_sat/r)²` ⇒ reactive `p=2`"*.

The far-field agreement between the two dresses (both `→ Z₀`) is the **trivial** `dress→Z₀` limit every
dress shares — it is NOT a form match; the distinguishing structure (the argument exponent) differs across
the entire window.

---

## 6. Implications + downstream flags (flag-don't-fix)

**The register question is NOT ruled by this check.** It establishes the *fact*: the FIELD-strain ladder
(Ruling-11) and the VOLTAGE-strain dress (Op4/Op14 as-built) are structurally different port objects
(`p=4` vs `p=2`), and Op4 sits on the voltage side. **Whether Op4's voltage argument is a genuine register
defect** (the pairwise potential *should* be biased by the field-strain the #693 kernel consumes) **or a
legitimate register choice** (the pairwise potential is intrinsically a displacement/voltage-strain object)
is a **Grant/auditor physics adjudication** — this check surfaces it, sharpened from the knee-check
*amplitude*-level flag (`2026-07-14_knee-contour-check_NOTE.md:66-72`) to the **port-expression** level.

**Downstream consumers of the `p=2` voltage-strain form (FLAGGED — do NOT edit; auditor/Grant adjudicate):**

1. `src/ave/core/universal_operators.py:184` — `S_quarter = (1.0 - ratio_sq) ** 0.25` with
   `ratio_sq=(d_sat/r)²` (the `p=2` voltage argument); docstring `:229` `Z_eff/Z₀ = 1/(1−(d_sat/r)²)^{1/4}`.
2. `src/scripts/vol_2_subatomic/qed_trace_beta_gate.py:103,108` — `reactive_alpha`,
   `Z(r)/Z0 = 1/(1−(d_sat/r)²)^{1/4}`, `p=2` (the reactive register the beta gate reads).
3. `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/pairwise-potential.md:20` —
   `Z(r) = Z₀/(1−(d_sat/r)²)^{1/4}`.
4. `src/ave/topological/cosserat_field_3d.py:419-423` — the pre-existing Op14 exponent/sign reconciliation
   flag (`Z0/√S` vs `Z0/S^{1/4}` vs `Z0·√(S_μ/S_ε)`). **This check adds a distinct THIRD axis to that
   flag:** beyond the *outer* exponent and the *sign*, there is the **strain-register** axis — which strain
   (field `∝1/r²` vs voltage `∝1/r`) feeds the kernel. The `p=2`-vs-`p=4` argument fork is orthogonal to
   the outer `√S`-vs-`S^{1/4}` fork and to the `S^{±½}` sign fork.

**The flag is NOT "Op4 is arithmetically wrong."** Op4 is internally consistent as the voltage-strain dress
and its ladder port reproduces it exactly. The flag is: **Op4/Op14 encode the VOLTAGE register; Ruling-11
registers the FIELD register; these integrate to different port forms; the register choice for the pairwise
potential is unadjudicated.**

**Consistency-vs-emergence: CONSISTENCY.** No value minted, no emergence headlined; the earnable content is
a functional-form (register) characterization of a canonical operator, `K`-independent.

