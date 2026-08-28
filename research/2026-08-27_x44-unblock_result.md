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
