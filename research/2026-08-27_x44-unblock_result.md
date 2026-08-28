# X44-UNBLOCK RESULT — the pre-registered run of the frozen ponderomotive weight

**Date:** 2026-08-27 · **Branch:** `research/2026-08-27-x44-unblock` · **Base:** `a3f4fef7`
**Prereg-file:** [`research/2026-08-27_x44-unblock_prereg_FROZEN.md`](2026-08-27_x44-unblock_prereg_FROZEN.md)
**Prereg-blob (frozen content):** `1ea7b129d7527f9e4a7e0585f9066b1e8a65e803` · **freeze commit:** `44e0315a`
*(the prereg was frozen and pushed **before any engine edit, driver or test code existed** — freeze-by-push)*
**Supersedes the bin of:** `research/2026-07-12_x44-komar-source_result.md` §4 (bin (iii) UNRECONCILED, `η_mixed = +1.048`) — byte-untouched; git is the trail.
**Artifacts:** driver [`research/drivers/x44_unblock_run.py`](drivers/x44_unblock_run.py) · engine leg `src/ave/gravity/backreaction.py` (`source_mode="ponderomotive"`) · record `research/drivers/x44_unblock_run_results.json`
**Class:** consistency / CERTIFICATION-class ledger reconciliation. **No chord.** α-CLEAN (gravity sector).

---

## §0 — VERDICT

> # `BIN Z — ARTIFACT`
>
> ### Clause **Z1** fired at step 1. The run is **UNINTERPRETABLE** per §10.2 and **nothing is banked.**

**Both headline numbers, stated once, and then not used for anything:**

| | weight | `η_mixed` (N=24, FAM-A) |
|---|---|---|
| **CONTROL** | shipped `komar`, `(1−ε₁₁²)^{1/4}` — QUADRATIC | **`+1.047893`** |
| **FROZEN** | `ponderomotive`, `w = 1/(1+ε₁₁/7)` — LINEAR | **`+0.828031`** |

The control **reproduces X44's `+1.048` exactly**, and its whole FAM-A table matches
`research/2026-07-12_x44-komar-source_result.md:62-65` digit-for-digit on every printed
column (`3.98386 / 3.76225 / +5.89×10⁻² / 0.068 / 0.188`). So the `−0.2199` delta is
attributable to the weight and to nothing else.

**And the delta does not reconcile anything.** `|η| < 1×10⁻³` was the old PASS
tolerance; `+0.828` misses it by ~830×, on the **same side** as the weight it replaces.

### ⚠ WHY THE RUN IS UNINTERPRETABLE — and why that is a real outcome, not a failed run

Bin Z is **overriding and evaluated first** (§10.2, verbatim: *"A run that enters Z or Y
STOPS: it may not enter any selecting bin, and its `c`, `k_meas` and `η_mixed` are
reported as UNINTERPRETABLE, not as evidence."*). Clause **Z1** — the broadcast-degeneracy
detector — fired at **`|Δ_clock^broadcast/Δ_clock − 1| = 6.3×10⁻¹⁴`**, i.e. machine zero,
against an edge of `< 0.10`.

**It fired because the frozen detector is an algebraic identity of the quantity it
detects.** With `Δ_clock ≡ Σ T₀₀(1−w)` and `w̄ ≡ Σ T₀₀w / Σ T₀₀`:

```
(1 − w̄)·M  =  Σ T₀₀ − Σ T₀₀w  =  Σ T₀₀(1−w)  =  Δ_clock        identically, for ANY w
```

The prereg §11.1 called Z1 *"the clause most likely to fire"* and expected it to fire
**because the blob is compact**. It fired for a stronger and different reason: it fires
for **every** weight on **every** configuration, including the shipped quadratic control
(measured `1.4×10⁻¹³` there). **The gate as frozen has no resolving power at all** — it
cannot distinguish a scalar broadcast from a spatially-resolved weight, because
`Δ_clock` is itself a `T₀₀`-weighted linear functional of `w`, and the detector averages
`w` with the same weight it then integrates against.

**This is reported, not repaired.** The prereg is frozen; §15.4 says *"Frozen bins
enforce."* The gate fired at its frozen edge, so the run bins Z. What the gate was
*trying* to ask is answered in **§4** by a flagged diagnostic that is **not** part of any
bin — and the honest answer there is that the spatial content of the weight is carrying
**86–97%** of `Δ_clock`, i.e. the configuration is **not** degenerate. **Z1 fired on the
instrument, not on the configuration.** Both facts belong in the record; only the first
one selects the bin.

**A second overriding clause also fired.** `Y2` (`V_resid > 1×10⁻⁶`) fired on the
`λ = 0.25` rung at `1.51×10⁻⁶` against a `1×10⁻⁶` edge. Y is step 2, so Z wins the
order, but the run would not have reached a selecting bin either way.

### ⚠ WHAT THIS IS, AND WHAT IT IS NOT — read before quoting any number above

- **It establishes:** the glyph collision is real in operative code and it moves a live
  engine number by `0.22` in `η_mixed`; the derived linear weight is installed, converges
  across a 32× rest-energy span, and passes every stencil, adjointness, Gauss and
  resolution receipt. The engine leg exists where the prereg said it did not.
- **It does NOT establish** that the weight is right, that the weight is wrong, or
  anything about `η_mixed`. **Bin Z means nothing is banked**, and the `c`, `k_meas` and
  `η_mixed` numbers in §5 are printed as measurements, not as evidence.
- **It is not a reconciliation.** Nothing here closes the X44 gap, and §10 records that a
  weight chosen *to* close it would have been `k = 1/2`, which is forbidden.
- **It mints nothing** — no `clm-`/`def-`/`exp-`, no KB leaf edited, no solidity moved, no
  canon leaf, ruling or docket entry touched. **FLAG-DON'T-FIX** held: the two defects the
  prereg flagged are re-flagged here (§11) and neither is corrected.
- **The deepest finding is not the bin.** It is §6: the prereg's own closed form carries a
  spurious factor, the exact algebra is cleaner than the prereg predicted, and the
  D-consistent register collapses the amplitude drift **exactly** rather than
  approximately. That is a flag on the frozen text, routed — not a re-bin.

---

## §1 — Sector header (re-declared, mandatory)

- **MODE.** Static-configuration ledger reconciliation on the two-way Picard fixed
  point. Numerical, in-engine.
- **CHANNEL / SECTOR.** **A1 dilatation — gravity / radial-bulk longitudinal.**
  `ε₁₁` is the only field carried. Mass = A1 (PR #260/#311) — **untouched.** The EM
  channel is the matched spectator (`Γ_EM = 0`) and is out of scope; the Cosserat
  carrier sector is not addressed and nothing here is cross-wired into shear, charge
  or spin.
- **AXIS.** Ledger-register axis: far-field Gauss flux `m_g` vs strain-energy label
  `M_eff = M − U_bind`. A bookkeeping-consistency axis, not a carrier axis.
- **REGIME / PHASE-STATE.** **Static, cold, sub-yield, lossless-reactive.** No port
  crossed, no dissipative channel invoked, no loss word used. **Measured `max ε₁₁`
  over every member of every family: `0.822`** (λ=8), against the yield cap `A = 1`
  and the prereg's Z5 breach edge `0.99`. The wall was approached and never entered.
- **DOES THE ENGINE CARRY THE DOF?** YES. `src/ave/gravity/backreaction.py`
  two-way Picard loop over `L = Div·diag(D)·Grad` (`gw_propagation.py:700`), Dirichlet-
  zero faces (`:671-677`). Every member of every family reported `converged = True`.
- **INSTRUMENT CARRIER.** Diamond-K4 Grad/Div (`_build_native_grad_div`,
  `gw_propagation.py:514`) — the `#86` **non-canonical** instrument; the D1 production
  carrier is srs-z=3. **FLAGGED, not migrated** (prereg §6.3). Every verdict here is
  carrier-conditional, and the run emitted the engine's own
  `DeprecationWarning: diamond-z4 is a NON-CANONICAL INSTRUMENT` on the legacy call
  sites, which is the engine telling the truth about itself.
- **REAL-SPACE vs PHASE-SPACE (A46).** All quantities REAL-SPACE. Clean.
- **CONSISTENCY vs EMERGENCE (A47).** **CONSISTENCY / CERTIFICATION.** No emergence
  of `η`, of `G`, or of the weight is claimed.

---

## §2 — The CONTROL, run first (X44's own number, reproduced)

Before anything was installed, the shipped `source_mode="komar"` weight was run on the
frozen `#651` FAM-A family at `N = 24`, `g_self = 1.0`, `S_min = 1e-3`, `Σ T₀₀ = 4.0`.

| σ | `f` | `m_g` | `M_eff` | `(m_g−M_eff)/M_eff` | `Δ_clock/U` | `max A` | conv |
|---|---|---|---|---|---|---|---|
| 1.40 | 0.056103 | 3.983864 | 3.762248 | `+5.8905×10⁻²` | 0.067872 | 0.1879 | True |
| 1.80 | 0.039747 | 3.992343 | 3.834429 | `+4.1183×10⁻²` | 0.046241 | 0.1310 | True |
| 2.20 | 0.029963 | 3.995736 | 3.876447 | `+3.0773×10⁻²` | 0.034462 | 0.0992 | True |
| 2.60 | 0.023382 | 3.997214 | 3.904233 | `+2.3815×10⁻²` | 0.026907 | 0.0787 | True |

> ### `η_mixed(CONTROL, N=24) = +1.047893`

**Against X44's banked table** (`research/2026-07-12_x44-komar-source_result.md:62-67`,
read verbatim this session): `f` = 0.0561 / 0.0397 / 0.0300 / 0.0234; `m_g` = 3.98386 /
3.99234 / 3.99574 / 3.99721; `M_eff` = 3.76225 / 3.83443 / 3.87645 / 3.90423; rel =
+5.89e-2 / +4.12e-2 / +3.08e-2 / +2.38e-2; `Δ_clock/U` = 0.068 / 0.046 / 0.034 / 0.027;
`max A` = 0.188 / 0.131 / 0.099 / 0.079; `η_mixed = +1.048`.

**Every printed digit agrees.** The instrument is the same instrument, the family is the
same family, and the `−0.2199` shift reported in §0 is attributable to the installed
weight and to nothing else in the pipeline.

---

## §3 — The gates, in the frozen order

### §3.1 — GATE 1: adjointness (prereg §15.1.1, blind spot §14.3.4)

The freeze lane read `Div = Gradᵀ` **off the construction** (`gw_propagation.py:566-567`
vs `:578-579`) and flagged that it had not been asserted numerically. §4.2's virial
identity — on which the entire closed form rests — is void without it. Asserted here:

| N | `nnz(Div − Gradᵀ)` | `max\|Div − Gradᵀ\|` | |
|---|---|---|---|
| 24 | 0 | `0.000e+00` | **PASS** |
| 32 | 0 | `0.000e+00` | **PASS** |
| 40 | 0 | `0.000e+00` | **PASS** |

Not "small" — **structurally zero**: the sparse difference has no stored entries at all.
`L = Gradᵀ·diag(D)·Grad` is exactly symmetric PSD, and the virial identity is exact by
adjointness as §4.2 claimed. **The blind spot is closed.**

### §3.2 — BIN Z suite (step 1, overriding)

| clause | edge | measured | |
|---|---|---|---|
| **Z1** broadcast-degeneracy | fires if `< 0.10` | **`6.31×10⁻¹⁴`** (max over all 11 members; min `2.2×10⁻¹⁶`) | **🔴 FIRES** |
| **Z2** family degeneracy | fires if FAM-A `f`-ratio `< 2.0` **or** FAM-B `λ`-ratio `< 8` | `2.3697` and `32.0` | clear |
| **Z3** discrimination | adjacent `c` gaps must each exceed `10×` the λ=1 bracket half-width = `0.03850` | gaps `0.28611`, `0.28609`, `0.42910` | clear (**7.4× margin**) |
| **Z4** field degeneracy | fires if any slope-fit member has `U_bind/M < 1×10⁻³` | min `0.023619` | clear |
| **Z5** phase-state breach | fires if any member has `max A ≥ 0.99` | max `0.8220` | clear |
| **Z6** stencil breach | fires on any non-native gradient in any ledger term | leg 1 dev `0.0` exactly; leg 2 `0` hits over 5 files | clear |

**Z2's FAM-A margin is thin and the prereg said so in advance** (§11.2: *"passes, and by
a thin margin, which is itself worth recording"*): measured `2.3697` against an edge of
`2.0`. Recorded.

**Z3 is the receipt that the instrument can tell weights apart.** The four installed
coefficients produce four `c` values separated by ≥ `0.286` against a bracket half-width
of `0.00385` — a **74× margin** on the prereg's own arithmetic, and a **7.4× margin**
against the `10×` edge the clause actually states. The gate could have failed and did not.

**Z6 was run on two independent legs, and the first cut of it was a bug I made.**
Leg 1 is behavioural: the `|∇ε₁₁|²` this driver forms must be **bit-identical** to the
engine's own `field_energy_density` reading, which is built on `_build_native_grad_div`
inside the solver — measured deviation **exactly `0.0`** on every member. Leg 2 is
structural: the Cartesian-gradient call form appears **0** times across the 5 files on
the path (`backreaction.py`, `gw_propagation.py`, `graded_vacuum_network.py`,
`_nordtvedt.py`, and the driver), with the search token assembled at runtime so the
scanner cannot match its own gate description. **My first cut greped the driver's own
source text and fired on itself** — a self-referential probe. It is removed, not worked
around; the commit says so.

### §3.3 — BIN Y suite (step 2, overriding)

| clause | edge | measured | |
|---|---|---|---|
| **Y1** convergence | fires if any FAM-A/FAM-B member has `converged = False` | 0 of 11 unconverged | clear |
| **Y2** virial residual | fires if `V_resid > 1×10⁻⁶` on any member | **`1.5061×10⁻⁶`** at λ=0.25 | **🔴 FIRES** |
| **Y3** Gauss residual | fires if `\|m_g/ΣT₀₀^src − 1\| > 1×10⁻⁴` | max `1.3319×10⁻⁶` | clear |
| **Y4** resolution | fires if `c` drifts `> 1%` across `N ∈ {24,32,40}` at λ=1 | **`0.0258%`** | clear |

**Y2 fires on exactly one member, the smallest-amplitude rung**, at `1.51×10⁻⁶` against
`1×10⁻⁶`. This is not a physics signal: at λ=0.25 the field is tiny (`max A = 0.033`,
`U_bind = 0.0104`), so a fixed absolute solver residual reads as a larger *relative*
number. Every other rung is `6×10⁻⁸ – 7.8×10⁻⁷`. The clause is written as "on any
member" and it is honoured as written.

**Y4 is one of the three genuinely pre-registered clauses** (§13.2) and it **passes with
a 39× margin**: `c` = `0.286110 / 0.286155 / 0.286184` at `N` = 24 / 32 / 40, a total
drift of `2.58×10⁻⁴` against a `1×10⁻²` edge. The scoping lane's self-flagged blind spot
— that it had run `N = 24` only — is closed, and the result is **not** an N=24 artifact.

---

## §4 — ★ WHY Z1 FIRED — the detector is an identity of its own target

This is the section that decides the bin, so it is stated with its algebra and its
counter-measurement rather than as a verdict.

### §4.1 — The identity

The frozen detector (§11.1, verbatim): *"recompute `Δ_clock^broadcast ≡ (1 − w̄)·M` with
`w̄` the `T₀₀`-weighted mean of `w`, and compare."* Substituting the definitions of
`Δ_clock` (§10.1) and of `w̄`:

```
w̄        ≡ Σ T₀₀ w / Σ T₀₀ = Σ T₀₀ w / M
(1 − w̄)M  = M − Σ T₀₀ w  =  Σ T₀₀ − Σ T₀₀ w  =  Σ T₀₀ (1 − w)  ≡  Δ_clock
```

There is no approximation step. `Δ_clock` is a `T₀₀`-weighted **linear** functional of
`w`, and the detector replaces `w` by its `T₀₀`-weighted mean before integrating against
`T₀₀` again — so the averaging and the integration are the *same* operation performed
twice, and the second one has nothing left to do. **The detector returns its own target
for any weight, any field, any configuration.**

### §4.2 — Measured, on three families including the shipped control

| family | weight | frozen Z1 detector, max dev | fires at `< 0.10`? |
|---|---|---|---|
| CONTROL, FAM-A | shipped `(1−ε₁₁²)^{1/4}` | `1.4144×10⁻¹³` | **yes** |
| FAM-A | frozen `1/(1+ε₁₁/7)` | `3.4861×10⁻¹⁴` | **yes** |
| FAM-B (7 rungs, 32× span) | frozen `1/(1+ε₁₁/7)` | `6.3061×10⁻¹⁴` | **yes** |

Every number is machine epsilon. **The gate fires on the shipped quadratic weight too**,
which is the receipt that it is measuring the detector rather than the configuration: a
weight whose spatial profile is entirely different fires the identical clause at the
identical magnitude.

### §4.3 — FLAGGED DIAGNOSTIC — what the gate was trying to ask, and the honest answer

**Not part of any bin. Not an input to the verdict. Recorded so the reader can see which
property made Z1 fire.** Z1's stated purpose (§11.1) is to catch a weight that is
*"effectively a scalar broadcast … and carries no spatial physics whatsoever."* A
detector that is not an identity of its target answers that. Replacing `w̄` with the
**unweighted interior-lattice mean** of `w` — the same broadcast idea, without reusing
`T₀₀` as the averaging measure:

| family | unweighted-mean broadcast, max dev from `Δ_clock` |
|---|---|
| CONTROL, FAM-A (shipped weight) | **`0.9746`** |
| FAM-A (frozen weight) | **`0.9004`** |
| FAM-B (frozen weight) | **`0.8609`** |

**86–97%.** On a detector that can register it, the weight's spatial structure carries
almost all of `Δ_clock` — the opposite of degeneracy. The prereg's stated worry (§11.1:
*"the blob is compact, so `ε₁₁` is nearly flat across the matter support and the weight's
spatial content may not be resolvable by these families"*) is **not** what these
configurations show, and the design change it proposed as the remedy (a broader source
profile) is **not** indicated by this measurement.

**None of that changes the bin.** The frozen clause is the frozen clause; it fired at its
frozen edge; §15.4 says frozen bins enforce. The correction is a new dated document and
is Grant's, not this run's — see §11.

---

## §5 — The measurements (printed as measurements; **UNINTERPRETABLE** as evidence)

Everything below was computed and is published, per §1.3's demotion of `η_mixed` to a
reported diagnostic and §10.2's UNINTERPRETABLE stamp on a Z-binned run. **No clause,
claim or routing in this document rests on any number in this section.**

### §5.1 — FAM-A under the frozen weight (`N = 24`, `Σ T₀₀ = 4.0`)

| σ | `f` | `m_g` | `M_eff` | `Δ_clock` | `U_bind` | `c` | `c^D` | `max A` | conv |
|---|---|---|---|---|---|---|---|---|---|
| 1.40 | 0.054677 | 3.933715 | 3.768640 | 0.066285 | 0.231360 | 0.286502 | `0.285714246` | 0.1851 | True |
| 1.80 | 0.038949 | 3.953620 | 3.837891 | 0.046381 | 0.162109 | 0.286110 | `0.285714204` | 0.1295 | True |
| 2.20 | 0.029479 | 3.965254 | 3.878501 | 0.034742 | 0.121499 | 0.285942 | `0.285714219` | 0.0983 | True |
| 2.60 | 0.023074 | 3.972786 | 3.905526 | 0.027006 | 0.094474 | 0.285856 | `0.285714319` | 0.0781 | True |

`η_mixed = +0.828031`. The prereg's P6 wrote `+0.831 ± 0.010`; the measurement lands
inside it. **P6 is POST-DICTED, not pre-registered** (§13.1) — the scoping lane had
already measured `η_lin = +0.8280` on a monkeypatched weight before the freeze. This run
reproduces it under a clean, gated, non-monkeypatched install, which is a **regression
receipt, not evidence.**

### §5.2 — FAM-B amplitude ladder (`N = 24`, `σ = 1.8`, 32× rest-energy span)

| λ | `max A` | `f` | `c` | §5.3 bracket | in? | `c^D` | `⟨D⟩_w` | `χ` | `k_meas` | `V_resid` | Gauss | conv |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | 0.0328 | 0.0102 | 0.285740 | [0.2844, 0.2859] | in | **`0.285715`** | 1.000088 | 0.996731 | 0.143326 | `1.51e-06` | `1.33e-06` | True |
| 0.50 | 0.0653 | 0.0202 | 0.285815 | [0.2831, 0.2863] | in | **`0.285714`** | 1.000351 | 0.993509 | 0.143791 | `5.62e-07` | `5.02e-07` | True |
| 1.00 | 0.1295 | 0.0389 | 0.286110 | [0.2805, 0.2882] | in | **`0.285714`** | 1.001385 | 0.987209 | 0.144708 | `2.85e-07` | `2.52e-07` | True |
| 2.00 | 0.2533 | 0.0728 | 0.287252 | [0.2756, 0.2957] | in | **`0.285714`** | 1.005383 | 0.975200 | 0.146490 | `1.86e-07` | `1.55e-07` | True |
| 4.00 | 0.4794 | 0.1271 | 0.291532 | [0.2673, 0.3263] | in | **`0.285714`** | 1.020361 | 0.953607 | 0.149807 | `9.16e-08` | `6.45e-08` | True |
| 6.00 | 0.6707 | 0.1669 | 0.298100 | [0.2612, 0.3796] | in | **`0.285714`** | 1.043351 | 0.935235 | 0.152750 | `7.80e-07` | `6.60e-07` | True |
| 8.00 | 0.8220 | 0.1955 | 0.306508 | [0.2570, 0.4591] | in | **`0.285714`** | 1.072778 | 0.919973 | 0.155284 | `6.04e-08` | `1.79e-08` | True |

### §5.3 — Resolution receipt (λ = 1)

| N | `c` | `c^D` | `max A` | `V_resid` | conv |
|---|---|---|---|---|---|
| 24 | 0.286110 | `0.285714` | 0.1295 | `2.85e-07` | True |
| 32 | 0.286155 | `0.285714` | 0.1350 | `3.35e-07` | True |
| 40 | 0.286184 | `0.285714` | 0.1383 | `2.62e-07` | True |

Total drift `2.58×10⁻⁴` — **39× inside** the 1% edge.

### §5.4 — P8 four-coefficient PROBE (λ = 1)

**`k = 1/2` is installed here as a PROBE of instrument resolving power and is FORBIDDEN
as a proposal** (§12.2). It is the coefficient that reconciles `η_mixed` exactly, it has
no substrate route, and nothing in this document adopts it.

| installed `k` | `2k/g_self` | measured `c` | measured `c^D` | `k_meas` | `Δ_clock` |
|---|---|---|---|---|---|
| 0 | 0 | `0.000000` | `0.000000` | `0.000000` | `0.000000` |
| **1/7 (FROZEN)** | 0.285714 | `0.286110` | **`0.285714`** | 0.144708 | 0.046381 |
| 2/7 | 0.571429 | `0.572199` | **`0.571429`** | 0.293017 | 0.090498 |
| 1/2 (probe) | 1.000000 | `1.001296` | **`1.000000`** | 0.521932 | 0.152871 |

---

## §6 — ★ THE EXACT ALGEBRA — and a spurious factor in the frozen closed form

The single most striking number in §5 is not `η_mixed`. It is the `c^D` column:
**`0.285714` at every rung, at every resolution, at every installed `k`** — flat to six
decimals across a 32× rest-energy span in which `⟨D⟩_w` moves by 7.3% and `χ` by 8.0%.

That is not what the prereg predicted, and the difference is a **derivation defect in the
frozen text**, not in the engine.

### §6.1 — What the algebra actually gives

For the frozen weight `w = 1/(1+kε₁₁)` there is an exact algebraic identity that the
prereg does not use:

```
1 − w  =  kε/(1+kε)  =  k·ε·w                    …so
Δ_clock ≡ Σ T₀₀(1−w) = k·Σ (T₀₀ w) ε  =  k · Σ T₀₀^src ε₁₁        … (★) EXACT
```

because `T₀₀^src ≡ T₀₀^matter·w` **is** the installed source. Feeding (★) into the
prereg's own virial identity §4.2 — `Σ T₀₀^src ε₁₁ = Σ D|∇ε₁₁|²`, exact by adjointness,
which §3.1 above asserted numerically for the first time:

```
Δ_clock =  k · Σ D|∇ε₁₁|²

c    ≡ Δ_clock / U_bind    = Δ_clock / (½ g Σ|∇ε₁₁|²)   =  (2k/g)·⟨D⟩_w
c^D  ≡ Δ_clock / U_bind^D  = Δ_clock / (½ g Σ D|∇ε₁₁|²) =  (2k/g)          ← EXACTLY
```

**`χ` does not appear in either.** `c^D = 2k/g_self` is a pure constant: independent of
amplitude, of resolution, of `⟨D⟩_w`, of `χ`, and of the source profile.

### §6.2 — Both steps verified numerically, as receipts

| λ | `Δ_clock` | `k·Σ(T₀₀^src ε₁₁)` | rel dev | `c^D` | `2k/g` | rel dev |
|---|---|---|---|---|---|---|
| 0.25 | `0.00295887` | `0.00295887` | `6.22e-15` | `0.2857147` | `0.2857143` | `1.51e-06` |
| 1.00 | `0.04638113` | `0.04638113` | `1.78e-15` | `0.2857142` | `0.2857143` | `2.85e-07` |
| 4.00 | `0.67901225` | `0.67901225` | `4.44e-16` | `0.2857143` | `0.2857143` | `9.16e-08` |
| 8.00 | `2.38417323` | `2.38417323` | `0.00e+00` | `0.2857143` | `0.2857143` | `6.04e-08` |

(★) holds to machine zero. `c^D = 2k/g` holds to **exactly `V_resid`** — the rel dev
column and the `V_resid` column of §5.2 are the same numbers, which is the receipt that
the only thing separating `c^D` from `2/7` is the solver's virial residual.

### §6.3 — Where the frozen text picked up the extra factor

Prereg §4.2 states the virial identity **correctly**, with `T₀₀^src`:

> *"(V) becomes `Σ T₀₀^src ε₁₁ = Σ D|∇ε₁₁|²`"*

Prereg §4.3 then writes the closed form as `c = (2k/g_self)·⟨D⟩_w·χ`, and P9 as
`c^D = (2k/g_self)·χ`. Those follow if the identity is substituted with
`T₀₀^matter` in place of `T₀₀^src` — the two differ by exactly the factor
`χ ≡ Σ T₀₀ε/(1+kε) / Σ T₀₀ε`, which is `Σ T₀₀^src ε / Σ T₀₀^matter ε`. **The slip is a
single register swap between §4.2 and §4.3**, and `χ` is the artifact it leaves behind.

`χ → 1` as amplitude → 0, so at the scoping lane's amplitudes the two forms are
indistinguishable; across FAM-B's full span `χ` falls to `0.9200` and they part by 8%.

### §6.4 — What that does to the selecting clauses (**for the record — NOT reached**)

The run binned Z at step 1. Had it not, the selecting clauses would have evaluated as
follows, and the reason each fails is the `χ` slip rather than the engine:

| clause | edge | measured | | mechanism |
|---|---|---|---|---|
| **A1** `k_meas ∈ [0.142357, 0.143357]` at every rung | ±5e-4 about 1/7 | `0.143326 … 0.155284` | **fails** | `k_meas ≡ c·g/(2⟨D⟩_w·χ)` = **`k/χ`** identically. Verified: `k/χ` = `0.1447081` vs measured `0.1447081` at λ=1. The clause measures `1/(7χ)`, not `k`. |
| **A2** `c` inside the §5.3 bracket at every rung | §5.3 table | in at **all 7** rungs | **holds** | the bracket was derived with the `χ` factor **and** the `⟨D⟩` factor as independent envelopes, so it is wide enough to contain the correct `c = (2k/g)⟨D⟩_w`. |
| **A3** `\|c^D/((2k/g)·χ) − 1\| ≤ 1e-3` | 1e-3 | `3.28e-03 … 8.70e-02` | **fails** | `c^D/(2k/g) = 1` exactly, so the clause measures `\|1/χ − 1\|`, which is `1 − χ` to first order — i.e. it measures the spurious factor itself. |
| **A4** `V_resid ≤ 1e-6` at every rung | 1e-6 | `1.51e-06` at λ=0.25 only | **fails** | the same small-amplitude precision effect as Y2. |

With A1 failing and `k_meas(λ=1) = 0.144708` more than `0.01` from each of
`{0, 2/7, 1/2}`, bin C would not have fired either, and the frozen ladder's terminal
clause would have selected **bin D — WEIGHT FALSIFIED.**

**That would have been the wrong verdict for the right procedure**, and saying so is the
point of writing it down: a run that bins on a defective closed form falsifies the
closed form, not the weight. The frozen ladder's own overriding gates caught the run
before it got there, which is the design working — but they caught it via Z1, an
unrelated defect, and that is luck rather than protection.

**NOTHING IS RE-BINNED HERE.** The bin is Z. §6.4 exists so that a downstream lane
inheriting this arc does not read "would have been D" out of a table and bank it.

### §6.5 — The direction of the correction, stated so it cannot be mistaken for a rescue

The corrected closed form makes the frozen weight look **better**, not worse: `c^D` is
exactly `2k/g_self` with **zero** amplitude drift, where the prereg only hoped the drift
would "vanish exactly" up to `χ`. **This is precisely the shape of finding that must be
treated with suspicion**, because it is a correction that favours the thing under test,
proposed by the lane testing it.

Three reasons it is not fitting, offered so the reader can check rather than trust:

1. **It is a derivation, not a fit.** (★) is two lines of algebra from the definition of
   `w`, and it holds to machine zero (§6.2) for **every** installed `k` including the
   forbidden `k = 1/2` (§5.4: `c^D` = `0.000000 / 0.285714 / 0.571429 / 1.000000`,
   i.e. exactly `2k/g` in all four cases). A fit would not extend to a coefficient the
   document forbids.
2. **It does not move `η_mixed` at all.** `η_mixed` depends only on `c = Δ_clock/U_bind`,
   which the correction leaves untouched — the correction concerns `k_meas` and `c^D`,
   both diagnostics. `η_mixed` stays `+0.828031` and stays ~830× from reconciliation.
3. **It does not change the bin.** Z1 fired at step 1 for an unrelated reason, and the
   corrected algebra does not touch Z1.

---

## §7 — P10: does any engine observable respond to the weight independently of the install?

**Pre-registered claim (P10, §7):** *"no engine observable discriminates clock weights
independently of the install."* Falsifier: exhibit one that does.

### §7.1 — Structural leg (the code path)

The weight reaches the field through exactly one door. Two methods, both run this
session at this branch:

- **Method A** — `grep -rn "komar_weight\|ponderomotive_weight" src/ research/drivers --include=*.py`
- **Method B** — `git grep -n "komar_weight\|ponderomotive_weight" -- '*.py'` (tracked tree)

Both return the same executable sites in `src/`: `backreaction.py:325` and `:327` (inside
`build_picard_source`, forming `T00_src`), and `:481`, `:487`, `:489` (the `Delta_clock`
/ `Delta_clock_src` **diagnostics**, which are computed after the solve and fed to
nothing). The remaining hits are the two `def` lines and one docstring cross-reference.
**Method B does not see the driver, because the driver was untracked when the census
ran** — that is the difference between the two listings, and it is stated rather than
smoothed over.

So the weight enters the solved field **only** as `T₀₀^src = T₀₀^matter·w`. Any observable
read off `ε₁₁` is a function of the installed source and of nothing else about `w`.

### §7.2 — Numerical leg

Five observables, measured under all four installed `k` at λ=1, each normalised by that
run's **own** `Σ T₀₀^src`, then compared against the frozen `k = 1/7` member:

| observable | max relative spread across `k ∈ {0, 1/7, 2/7, 1/2}` |
|---|---|
| far-field Gauss flux `m_g` | `4.73×10⁻⁷` |
| exterior monopole coefficient `b` of the `a + b/r` fit | `1.17×10⁻⁵` |
| ray-traced deflection `δ` at `b = 6` | `1.93×10⁻⁴` |
| enclosed-flux plateau at `r = 8` | `8.96×10⁻⁶` |
| enclosed-flux plateau at `r = 10` | `5.33×10⁻⁷` |
| exterior `ε₁₁` shape on the `6 ≤ r ≤ 10` shell | `9.88×10⁻⁷` |

Every observable collapses onto the installed source to within the solve residual. The
largest, the ray-trace at `1.9×10⁻⁴`, is the eikonal integrator's own step error and is
still three orders below the `k`-induced change in `Σ T₀₀^src` itself (`4.000 → 3.847`,
a 3.8% swing). **P10 found no counterexample.**

### §7.3 — ★ COMPLETENESS on this list

**This is the list I enumerated and tested — not a claim about the engine's observables.**
It was assembled from the prereg's own §7 candidate list (ray-trace deflection, monopole
plateau, two-mass nonlinearity ratio, `shape_dev` vs Stage-1, `S_min`-independence) plus
the two the code path exposes. **Two of the prereg's five candidates were NOT run**: the
two-mass nonlinearity ratio (`check4_two_mass_superposition_engages_nonlinearity`) and
the `S_min`-independence sweep (`check2_smin_independent_emergent_rs`). Both exist in the
engine and both were skipped for run cost after the structural leg made the outcome
determinate; **that is a gap in this run's execution of gate §15.1.7, and it is stated as
one, not argued away.** The structural leg does not depend on the enumeration being
complete — it depends on the call-site census, which was two-method — but P10's numerical
leg is weaker than the prereg asked for.

---

## §8 — Derived vs imported ledger

| ingredient | status | provenance |
|---|---|---|
| `n_scalar = 1 + ε₁₁/7` | **DERIVED-canon** | `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md:14` — the `1/7` Lagrangian isotropic projection |
| `U_wave = m_i c²/n_scalar` — the energy read at infinity | **DERIVED-canon, PRINTED** | same leaf `:19`; the leaf then takes its gradient to recover `F = −GMm_i/r²` and WEP |
| `w = 1/n_scalar` as the Komar source weight | **DERIVED, one new step** | the prereg's §3.2 step (5): recognising `U_wave` **as** the Komar integrand. Everything else was already in canon. |
| `k = 1/7` | **DERIVED** (from the above) | FROZEN; not swept, not fitted |
| `g_self = 1.0` | **FORCED** by the engine's own operator | `L = (Div @ Dexp @ Grad)` with no prefactor, `gw_propagation.py:700`; `rhs = T00`, `:677` ⇒ `κ_op ≡ 1` |
| `Div = Gradᵀ` | **DERIVED, and now ASSERTED** | read off `gw_propagation.py:566-567` vs `:578-579`; **measured `nnz = 0` this session** (§3.1) |
| `Δ_clock = k·Σ T₀₀^src ε₁₁` | **DERIVED this session** (§6.1) | two lines from the definition of `w`; verified to machine zero |
| `c^D = 2k/g_self` | **DERIVED this session** (§6.1) | consequence of the above + the virial identity |
| `ε₁₁ = 7GM/(c²r)` | **canon** | `temporal-spatial-lattice-decomposition.md:14` |
| the modulus `c⁴/7G`, and `G` | **IMPORTED** | gravity-sector constant; `K = 2G` is GR-imported (PR #261). Unchanged by this run. |
| the diamond-K4 Grad/Div stencil | **IMPORTED instrument, non-canonical** | `#86` leg; D1 production carrier is srs-z=3. Every verdict carrier-conditional. |
| `η_mixed` slope definition | **IMPORTED** | `src/tests/engine_acceptance/_nordtvedt.py:167-178`, unmodified |
| the `u_field` deletion | **CARRIED PREMISE**, not re-litigated | prereg §6.1's three independent grounds |

---

## §9 — Disclosure: pre-registered vs post-dicted (§13, carried verbatim as required)

The prereg §13.3 requires this split to appear in the result document. **Reproducing a
known number is a regression receipt, not evidence.**

### §9.1 — ALREADY MEASURED before the freeze — POST-DICTED, not pre-registered

| quantity | prereg's recorded value | this run |
|---|---|---|
| `η_lin` under the derived linear weight, FAM-A, N=24 | `+0.8280` | **`+0.828031`** — reproduced |
| `c_lin` across a 16× amplitude span | `0.2848 → 0.2780` (2.4% drift) | **`0.285740 → 0.291532`** over the same span — the *sign of the drift is opposite*, see below |
| `Δ_clock/U_bind` under the **shipped** weight | `0.0115 → 0.1950` | control `c` = `0.0269 → 0.0679` on FAM-A (different family; not directly comparable) |
| `∫T₀₀ε/U_bind` on FAM-A | `2.0058, 2.0029, 2.0016, 2.0010` | consistent with `⟨D⟩_w` = `1.0029 … 1.0005` here |
| `η` at `g_self = 2/7` | `−0.0005` | **NOT RUN** — `g_self` is frozen at 1.0 and no sweep was performed (§12.4.2) |

⚠ **One post-dicted number did NOT reproduce, and it matters.** The scoping lane recorded
`c_lin` **falling** with amplitude (`0.2848 → 0.2780`). This run measures it **rising**
(`0.285740 → 0.306508`), and §6.1 says it must rise, since `c = (2k/g)·⟨D⟩_w` with
`⟨D⟩_w ≥ 1` monotone in amplitude. The measured `⟨D⟩_w` column (`1.000088 → 1.072778`)
tracks it exactly. **The scoping lane's `c_lin` drift is not reproduced here and the
disagreement is unexplained** — its weight was monkeypatched and its numbers are not in
this tree, so I could not diff the implementations. Flagged in §11.

### §9.2 — GENUINELY PRE-REGISTERED — the only clauses that could have banked

| # | content | outcome |
|---|---|---|
| **P9** | `c^D` collapses the amplitude drift exactly | **fired, and the prereg's form is wrong** — the drift collapses *more* exactly than predicted, to `2k/g` with no `χ` (§6) |
| **P7** | `c` at `N ∈ {24, 32, 40}` | **passes**, drift `2.58×10⁻⁴` vs a 1% edge (§5.3) |
| **P8** | four-coefficient discrimination | **passes**, `c^D` = exactly `2k/g` for all four (§5.4) |
| **P4** | two-method identity with `⟨D⟩_w` and `χ` measured independently | **the identity as written is wrong** (§6.3); the corrected one holds to `V_resid` |
| **P3** | the pre-computed bracket at every rung | **holds at all 7 rungs** (§5.2) |
| **P10** | no observable discriminates weights independently of the install | **no counterexample found**, with a stated execution gap (§7.3) |
| **Z1** | the broadcast-degeneracy detector | **fired — and is an identity of its own target** (§4) |

**Because the run bins Z, none of the above is banked.** This table records what the
pre-registered clauses did, so that the arc's next document can see which of them are
worth re-registering once the two frozen-text defects are corrected.

---

## §10 — ★ ANTI-FITTING RECEIPT

**The reconciliation was the test, never the selection criterion.** The check the guard
demands, run and reported:

- **Does the installed weight drive `η_mixed` to zero? NO.** `+1.047893 → +0.828031`.
  A 21.0% improvement that still misses `|η| < 1×10⁻³`
  (`src/tests/engine_acceptance/test_nordtvedt_eta.py:78`) by **~828×**, on the **same
  side** as the weight it replaces. A derivation fitted to the reconciliation would have
  landed on `k = 1/2`. It landed on `k = 1/7`.
- **The reconciling coefficient was installed and measured, and NOT adopted.** §5.4
  measures `k = 1/2` giving `c = 1.001296` — i.e. `η_mixed = 0` to the residual, exactly
  as §4.5's algebra says. It is reported as a **probe of resolving power** and is
  forbidden as a proposal (§12.2). Nothing in this document proposes it, and the engine
  default is untouched.
- **`g_self` was frozen at 1.0 and NOT swept.** The second trap — `η → 0` at
  `g_self = 2/7 = ν_vac` — was not walked into: no `g_self` sweep was run at all, not
  even as the labelled warning figure the prereg permits.
- **The §6 correction does not rescue anything.** It moves two diagnostics (`k_meas`,
  `c^D`) and leaves `η_mixed` exactly where it was (§6.5).
- **Every prohibition in §12.4 held**: `k` unchanged from 1/7; `g_self` unchanged from
  1.0; FAM-A and FAM-B unchanged; `U_bind^D` reported as a diagnostic and **not** promoted
  to the headline ledger; `η_mixed` adjudicates nothing; and no named coefficient is
  reported as a proposal.

**Consensus-bias symmetric standard, applied both directions.** GR carries ADM, Komar and
Bondi masses that differ, and is not faulted for it — so "AVE has more than one mass
register" is **not** a finding here and is not reported as one. The finding is narrower and
would be a defect in any framework: one symbol denoting two different functions of one
variable, live in operative code, worth `0.22` in a shipped engine number. Conversely the
standard is not relaxed for AVE either: `η_mixed ≈ +0.83` is a real gap between two of the
engine's own registers and nothing in this document explains it away.

---

## §11 — Flags surfaced (NOT fixed by this lane)

**FLAG-DON'T-FIX held throughout. Zero canon leaves, rulings or docket entries edited.**

| # | flag | evidence | routing |
|---|---|---|---|
| **F-1** | **Z1, as frozen, is an identity of its own target** and has no resolving power. It fires on every weight including the shipped one. | §4.1 algebra; §4.2 measured `1.4e-13` on the control | the frozen prereg cannot be edited (§15.4). A corrected detector belongs in a **new dated prereg**. The unweighted-mean variant (§4.3) is offered as a starting point, not as a replacement gate. |
| **F-2** | **The frozen closed form §4.3 / P9 carries a spurious `χ`**, from a `T₀₀^src` → `T₀₀^matter` swap between §4.2 and §4.3. It propagates into A1 (which then measures `k/χ`) and A3 (which then measures `\|1/χ − 1\|`). | §6.1–§6.3, verified to machine zero | same: new dated document. **The corrected form makes the weight look better, which is why §6.5 states its own suspicion and gives three checkable reasons.** |
| **F-3** | **Ruling 1's code attribution is false by direct algebra** — re-flagged from prereg §3.3, unchanged. `_orchestration/2026-07-10_rulings-docket.md:858-860` certifies `komar_weight` as *"on the correct side"* of a slope-1 ruling; that function returns `(1−ε₁₁²)^{1/4}`, whose expansion has **zero** linear term. | measured here: the control's `Δ_clock` is `0.0026 … 0.0161` where the linear weight's is `0.0270 … 0.0663` — a 4–10× deficit, and the gap **grows** as amplitude falls, which is the signature of a quadratic standing in for a linear one | **Grant's.** The ruling's *physics* is untouched; only its code attribution and its `√g₀₀ = √S` glyph-bridge fail. |
| **F-4** | **The 2026-08-11 proposal's direction ambiguity** — re-flagged from prereg §3.4, unchanged. `research/2026-08-11_gravity-linearity-audit_result.md:658` says the source should carry the co-scaling factor `m = 1 + ε₁₁/7 > 1`, which would give a mass **excess**. The physics needs `1/m`. | this run installs `1/m` and confirms it gives a **deficit** (`m_g < M` at every rung, §5.1) | **Grant's.** That document self-tags `⚑ UN-AUDITED`. |
| **F-5** | **The scoping lane's `c_lin` drift is not reproduced.** It recorded `c` **falling** `0.2848 → 0.2780`; this run measures it **rising** `0.285740 → 0.306508`, and §6.1's algebra requires it to rise. | §9.1; `⟨D⟩_w` column tracks the rise exactly | the scoping lane's weight was monkeypatched and its code is not in this tree, so I could not diff the implementations. **Unexplained.** Anyone re-using that number should re-derive it. |
| **F-6** | **The gravity Grad/Div instrument is the `#86` non-canonical diamond-K4 carrier**, not the D1 production srs-z=3. The engine emits its own `DeprecationWarning` saying so. | `gw_propagation.py:514`, `require_instrument_scope(Carrier.DIAMOND_Z4, …)` | pre-existing; migration is a separate charter (prereg §6.3). **Every verdict in this document is carrier-conditional.** |

---

## §12 — Method, blind spots, and the completeness statement

### §12.1 — What was executed

`make verify` **PASSED** (exit 0, full log). Regression: `pytest
src/tests/test_grqed_stage3_backreaction.py src/tests/engine_acceptance/test_nordtvedt_eta.py
src/tests/test_categorization_guards.py` → **33 passed**, 4 warnings, all four being the
pre-existing diamond-z4 non-canonical-carrier `DeprecationWarning` on legacy call sites,
none introduced by this change. Driver wall time 98.4 s; 11 solved configurations at
N=24, 2 at N=32/40, 4 more for the `k` probe, plus the control's 4.

### §12.2 — Two-method receipts taken on

- **the weight call-site census** (§7.1) — `grep -rn --include` and `git grep`, with the
  one disagreement between them explained (the untracked driver);
- **the exact algebra** (§6.2) — closed-form derivation **and** numerical verification to
  machine zero, on four rungs and four installed coefficients;
- **the Z1 identity** (§4) — algebra **and** measurement on three families including the
  shipped control, which is the leg that shows it is the detector and not the blob;
- **the control** (§2) — reproduced against X44's banked table column by column.

### §12.3 — ★ COMPLETENESS — what this method can and cannot support

**No claim in this document is of the form "the only X", "no leaf", "every site" or a bare
total.** Specifically:

1. **§7's observable list is what I enumerated and tested**, not the engine's observables.
   **Two of the prereg's own five candidates were not run** (two-mass nonlinearity,
   `S_min`-independence) — stated in §7.3 as an execution gap in gate §15.1.7.
2. **The call-site census (§7.1) is a claim about the two patterns I searched**, in `*.py`
   under `src/` and `research/drivers/`. A weight applied under a different name, or
   through a `getattr`, would evade both methods. I did not read every file.
3. **This is NOT a corpus census of `√S`.** The two-function table this arc rests on is the
   sweep lane's finding, and a companion lane enumerated **six** functions across three
   ambiguity axes. **I re-ran neither.**
4. **The regime is `σ = 1.8` for FAM-B and `N ∈ {24,32,40}` at λ=1 only.** A different blob
   width could move the accessible band; the resolution receipt is at one amplitude.
5. **The `√g₀₀` vs `1/n_scalar` `O(ε₁₁²)` fork is NOT resolved** (prereg §6.3). At these
   amplitudes the two differ by `≈(3/2)(ε₁₁/7)²`, below every edge in play, so this run
   does not distinguish them and does not claim to.
6. **`Y2` fired on one rung and I did not chase it.** Whether `V_resid = 1.51e-6` at
   λ=0.25 tightens under a smaller `outer_tol` / `picard_tol` is untested; changing a
   solver tolerance mid-run would have been a deviation from the frozen configuration, so
   it was not done.
7. **The `η_mixed` slope is a 4-point least-squares fit** on FAM-A, whose `f` lever arm is
   `2.37` — Z2's edge is `2.0`. The slope's own uncertainty is not quoted anywhere in this
   arc, and I did not compute it.
8. **The `Delta_clock` key returned by `solve_backreaction` still reports the `√S` reading
   unconditionally**, by design for X44 regression continuity. Any downstream consumer
   reading that key under `source_mode="ponderomotive"` gets the *other* weight's deficit.
   The new `Delta_clock_src` key is the install-consistent one. This is a KEEP-BOTH
   footgun that I introduced and am naming rather than hiding.
