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
