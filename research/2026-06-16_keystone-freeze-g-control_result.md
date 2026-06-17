# Keystone FREEZE-G Control (+ direct-R accounting) — RUNG-2 Decider RESULT

**2026-06-16 · engine-lane (independent verification).** Decides whether the
RUNG-2 `SUBSTRATE-PUMP` verdict (ladder `4a90944c`, `R∞/R0=0.842`) is a genuine
substrate negative or a fixable `WINDOW-MODEL-PUMP` (the dropped `∂g/∂V`
moving-window residual `R=κ̃∫ġVΞ` derived in the PIECE-1 proof,
`research/2026-06-16_keystone-coupling-continuum-conservation-proof.md` §5–6).

## Verdict

**BIN: `SUBSTRATE-PUMP` — CONFIRMED (doubly: freeze-g plateau persists AND direct-R accounts for <1%).**

The RUNG-2 EXCESS plateau is NOT the moving-window residual `R=κ̃∫ġVΞ`. Freezing
`g` (removing `ġVΞ` by construction) leaves the plateau **unchanged** (99.6% of the
moving `R∞` survives), with the coupling still firing; and the directly-measured
residual `ΣR·dt` accounts for only **0.77%** of the EXCESS pump. The keystone
leans **NEGATIVE**: the substrate does not losslessly close the energize-LOCK loop
even with a variationally-consistent (frozen-g) coupling. The fixable
`WINDOW-MODEL-PUMP` escape hatch the PIECE-1 proof opened is **closed by data**.

## The two prongs

### Prong A — freeze-g control (live-g vs frozen-g)
Re-ran the SAME RUNG-2 forced-overlap config (`couple_on`,
`coupling_support='saturated_interior'`, `project_alive`, `wall_off`, EXCESS
ON−OFF basis, B_int interior witness) over the same dt→0 sweep, TWICE:
- **MOVING-g** (`ġ≠0`, ladder default — `_front_window` recomputed from live `A_V` each step);
- **FROZEN-g** (`ġ≡0` — `g` captured once at t0 after seeding, held static via a
  monkey-patch of `_front_window`, freezing `g` coherently in BOTH the coupling
  force `f_V=−κ̃gΞ`, `f_ω=−κ̃∇†(gV)` AND the `H_c=κ̃∫gVΞ` witness).

| branch | `R∞/R0` | plateau (≥0.10)? | coupling fires? | `g` drift over window |
|---|---|---|---|---|
| MOVING-g (`ġ≠0`) | **1.0499** | YES | — (live) | 0.136 (`g` genuinely moves) |
| FROZEN-g (`ġ≡0`) | **1.0497** | YES (persists) | YES (`f_V`min=5.2e-4, `f_ω`min=1.0e-2) | 0.000 (truly frozen) |

The two `R∞/R0` are **identical to 3 decimals** (1.0499 vs 1.0497); 99.6% of the
moving `R∞` survives freezing `g`. The plateau does **not** vanish under `ġ≡0`.

**Cheat-check (load-bearing) — PASS:** under frozen-g the coupling STILL FIRES
(`f_V` min 5.2e-4, `f_ω` min 1.0e-2 over the window, both ≫ 0 on alive cells), so
the persistence is real, NOT a coupling-removed artifact. And the MOVING-g `g`
genuinely drifts (max 0.136 over the window) — the freeze is a real contrast, not
a no-op. NOT `FREEZE-G-CONFOUNDED`.

### Prong B — direct-R accounting (the proof §6 cleanest closure)
On the LIVE-g ON run, measured the PIECE-1 residual each step
`R_t = κ̃ Σ_Bint ġ·V·Ξ` (`ġ=(g_t−g_{t−1})/dt`, same masked window, same `V`,
same tetrahedral curl `Ξ` the witness uses), integrated `ΣR·dt` over `T_win`,
compared to the measured EXCESS H-climb (`rate_excess·T_win`):

| quantity | value |
|---|---|
| `ΣR·dt` (direct residual integral, B_int, coarsest dt) | **+1.957e-3** |
| EXCESS ΔH (`rate_excess·T_win`) | **+2.550e-1** |
| **accounted_frac = `ΣR·dt` / EXCESS ΔH** | **+0.0077 (0.77%)** |
| `R_t` series range over window | [−2.3e-3, +7.3e-3] (well-behaved, no blow-up) |

The directly-measured moving-window residual accounts for **<1%** of the EXCESS
H-climb. The pump is essentially entirely something else (the bulk self-trap /
two-grid temporal mismatch the ladder's EXCESS basis isolates from the coupling
self-trap), NOT the dropped-`∂g/∂V` term.

## Lean config (DECLARED before running, ladder-matched threshold)
`N=16`, `dx=1`, `PML=0`, B_int half=5 (**1331 box cells**, guard=3 cells low /
2 cells high), `T_win=2.0`, 4-pt dt sweep `dt_base/2^k`, `k=0..3`
(`dt_base=3.873e-2`), plateau threshold **0.10** (ladder-matched).
**α-free**: `wall_on=False`, `κ̃=6/5=pq/(p+q)` (geometric exchange ratio, NOT α);
no `ALPHA`/`KAPPA` in the update path (provenance gate asserts canonical
constants module + κ̃≠α). EXCESS (ON−OFF) decision basis + B_int interior-box
witness, identical to the ladder RUNG-2. Cost: minutes (vs the 4-hr N=32 sweep) —
this is a COMPARISON (does freezing `g` change the plateau), robust to box size.

dt sweep (the plateau, both branches):

| k | dt | EXCESS (moving) | EXCESS (frozen) |
|---|---|---|---|
| 0 | 3.873e-2 | +1.27524e-1 | +1.27071e-1 |
| 1 | 1.937e-2 | +1.30990e-1 | +1.30528e-1 |
| 2 | 9.683e-3 | +1.32167e-1 | +1.31679e-1 |
| 3 | 4.841e-3 | +1.33028e-1 | +1.32535e-1 |

The EXCESS converges to a finite dt→0 limit (`R∞`≈+1.334e-1 moving, +1.334e-1
frozen) — a plateau, NOT a vanishing dt-artifact. Moving and frozen track each
other to ≤0.4% at every dt. (`monotone↓=False` is expected: the EXCESS rises
slightly toward its plateau as dt→0, the dt-INDEPENDENT-pump signature — the
ladder's RUNG-2 showed the same rise-to-plateau, distinct from a dt→0 vanishing
integrator artifact.)

## Reading
Both prongs converge on the same answer, independently:

1. **The moving-window residual is real but NEGLIGIBLE.** Prong B measures it
   directly: `R=κ̃∫ġVΞ` integrates to 0.77% of the EXCESS pump. The PIECE-1 proof's
   algebra is vindicated (`R` exists, is dt-independent, `g` genuinely moves —
   drift 0.136) but its MAGNITUDE here is <1% — it cannot be the pump.
2. **Removing the residual entirely (freeze-g) does not remove the pump.** Prong A:
   with `ġ≡0` the EXCESS plateau is unchanged (1.0497 vs 1.0499), 99.6% survives,
   coupling still firing. If the residual WERE the pump, freezing `g` would have
   collapsed the plateau below 0.10 — it did not move at all.
3. **Therefore the pump is substrate, not window-model.** The fixable
   `WINDOW-MODEL-PUMP` hypothesis the proof raised is falsified by data. The
   keystone's SUBSTRATE-PUMP verdict stands: the energize-LOCK loop is NOT
   losslessly closeable by this conservative coupling, even after the coupling is
   made variationally consistent (frozen-g = exact gradient of its own energy).

**Consequence for winding-emergence:** the next-stage winding-emergence work does
NOT get to run on a freeze-g-corrected (conservative) coupling that closes the
loop — because freezing `g` does NOT close it. The pump is intrinsic to the
forced-overlap (`saturated_interior`) coupling stencil itself, independent of the
window's motion. (NOTE: this is a verdict on the FORCED-OVERLAP RUNG-2 variant.
The DEFAULT `'front'` coupling has disjoint `g`/`Ξ` support → `R≡0` → conservative
*and inert*, per the proof §4 / Layer-b finding — a different, separately-tracked
fork.)

## Framing flags
1. **B_int causal isolation over the FULL window — common-mode, cancels (not a
   defect).** The per-OUTER-STEP guard band is VALID per the spec formula:
   `guard(2) ≥ stencil_radius(1) + n_sub_cos·c·dt(0.095) = 1.095` at the coarsest
   dt. BUT the CUMULATIVE signal travel over `T_win=2.0` is ~4.9 cells (>guard),
   so the box-H witness is NOT causally isolated from the grid edge over the full
   window. This does **not** undermine the verdict: every decision is a DIFFERENCE
   at matched geometry — EXCESS (ON−OFF) and moving-vs-frozen both share the
   identical box/guard/seed, so any boundary leakage is **common-mode and cancels**.
   The same is true of the ladder RUNG-2 (same witness design). Prong-B's `R` is
   an intrinsic in-box residual, unaffected. Flagged for the auditor as a
   methodological note, not a rescue lever.
2. **Independent-lane corroboration.** This lane's SUBSTRATE-PUMP **agrees** with
   the sibling freeze-g lane (`analysis/2026-06-16-keystone-freezeg`, N=20/32,
   Prong-A only, also SUBSTRATE-PUMP-CONFIRMED) and adds the Prong-B direct-R
   closure that lane did not measure. Two independent drivers + the analytic proof
   now triangulate. NOT a shared-narrative blind spot: the prongs are
   methodologically distinct (freeze-g removes the residual structurally;
   direct-R measures it numerically) and both land at <1%.
3. **`monotone↓` flag is informational, not a failure.** The EXCESS rises toward
   its plateau as dt→0; the driver's `monotone↓=False` is the dt-INDEPENDENT-pump
   tell (the ladder bins on `R∞/R0≥THRESH`, which this passes), not an
   integrator-artifact (which would DECREASE toward zero). No action needed.

## Provenance
- Driver: `src/scripts/vol_1_foundations/keystone_freeze_g_control.py`
- Results: `src/scripts/vol_1_foundations/keystone_freeze_g_control_results.json`
- Branch: `analysis/2026-06-16-keystone-freeze-g-control` off ladder tip `4a90944c`.
- PIECE-1 proof (residual derivation + freeze-g spec):
  `research/2026-06-16_keystone-coupling-continuum-conservation-proof.md`
  (branch `analysis/2026-06-16-keystone-discriminator-proof`, tip `f5672881`).
- Sibling freeze-g lane (Prong-A only, N=20/32): branch
  `analysis/2026-06-16-keystone-freezeg`.
