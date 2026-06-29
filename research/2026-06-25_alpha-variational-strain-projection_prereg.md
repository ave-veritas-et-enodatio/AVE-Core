# PRE-REG (FROZEN) — Open A: variational strain-projection route to α's value

**Date frozen:** 2026-06-25 · **Lane:** implementor · **Origin:** scoping memo `research/2026-06-25_alpha-strain-projection-variational-route.md` (branch `research/alpha-strain-projection-variational`, commit `3422d164`)

**Driver (to run):** `src/scripts/verify/alpha_variational_strain_projection.py`

**Corpus-grep (ave-prereg Step 1):** no prior `variational` / `marginal-stabil` / `strain-transmission efficiency` derivation of α exists. Closed-negative routes: Maxwell–Calladine counting (`2026-06-15_alpha-crystal-mc-count_result.md`), golden-torus named identifications (Class B), thermal δ_strain (FT-1). Related but distinct: `2026-05-18_z0-first-principles-attempt-result.md` (z₀ path-count → 52, 1.5% gap; NOT variational).

---

## Question

Does a **substrate-native variational / marginal-stability** functional on the over-braced K4 amorphous network **select** the operating packing `p* ≈ 0.1834` (hence `α = p*/(8π) ≈ 1/137`) **without α-hiding** on the verdict path?

## Substrate-native setup (frozen)

**MODE:** A1 bulk dilatation + FTG-EMT amorphous central-force network (continuum effective medium of the over-braced secondary link ensemble — NOT discrete K4 MC counting, which closed negative).

**REGIME:** cold linear, S=1 (packing geometry only; no saturation dynamics).

**α-free inputs on verdict path:**

| Symbol | Value | Provenance |
|---|---|---|
| `z_primary` | 4 | K4 Axiom-1 coordination |
| `\|T\|` | 12 | tetrahedral rotation group order (Q-G47 route #1) |
| `z_0` | `4·(1+\|T\|) = 52` | K4 path-count convention (`2026-05-18_z0-first-principles-attempt-result.md` Model 2) |
| `p_cauchy` | 0.3068 | Delaunay amorphous reference (standard network geometry; NOT AVE-specific) |
| `K/G_target` | 2 | trace-reversal gravity-lock **form** (GR-imported value; used as stability criterion, flagged) |

**FTG-EMT moduli ratio** (canonical, `q_g47_path_c_emt_canonical.py`):

\[
\frac{K(p)}{G(p)} = \frac{(z_0 p - 2)(z_0 - 6)}{(z_0 p - 6)(z_0 - 2)}
\]

**Over-bracing dilution** (volume scaling):

\[
p(u) = \frac{p_{\text{cauchy}}}{(1+u)^3}, \quad u \ge 0
\]

**Poisson ratio from K/G:** \(\nu = (3K/G - 2)/(2(3K/G + 1))\). At K/G=2: \(\nu = 2/7\).

**Strain-projection factor:** \(\Pi = 1/7\) **only** at the trace-reversal point K/G=2 (Vol 3 Ch 1 one-seventh impedance projection).

## Three frozen functionals (Routes A1–A3)

### A1 — K/G crossing (constraint, not variational)

Solve `K/G(p(u), z_0=52) = 2` for `u*`. Forward read: `p* = p(u*)`, `α_pred = p*/(8π)`. Compare to CODATA **only after** solve.

### A2 — Marginal strain-transmission efficiency (variational)

\[
\eta(u) = \underbrace{\max\!\left(0,\frac{p(u)-p_G}{p_G}\right)}_{\text{rigidity margin}} \times \underbrace{\max\!\left(0,\frac{p_{\text{cauchy}}-p(u)}{p_{\text{cauchy}}}\right)}_{\text{Cauchy clearance}} \times \underbrace{\exp\!\left(-\left|\ln\frac{K/G(p(u))}{2}\right|\right)}_{\text{K/G=2 proximity}}
\]

with `p_G = 6/z_0`. **Argmax** `η(u)` on `u ∈ [0, 0.6]`. Forward read at `u_opt`.

### A3 — Goldilocks midpoint (variational baseline)

Maximize `(p - p_G)(p_cauchy - p)` on `p ∈ (p_G, p_cauchy)` **without** K/G weighting. Check whether optimum sits at K/G=2 crossing.

## α-hiding guard (Fork-A P3 analog)

**BANNED on verdict path:** `ALPHA`, `P_C`, `8πα`, `Z_COORDINATION` from `constants.py`, any CODATA α in the solve. CODATA `α⁻¹ = 137.035999084` is **comparison target only**, loaded after forward prediction.

## Frozen outcome map (Rule 11)

| Outcome | Condition |
|---|---|
| **CHORD** | A1 or A2 forward `α_pred` within `δ_strain` tolerance (`|α_pred/α_CODATA - 1| < 2.225e-6`) AND no α-hiding trace on load-bearing constants |
| **PARTIAL** | Forward prediction within **1.5%** of CODATA (matches z₀=52 structural gap band from 2026-05-18) but not within δ_strain |
| **ECHO** | Optimum/crossing requires α-circular input (e.g. must import `P_C` or invert given α) OR functional has no unique extremum OR α_pred off by >1.5% |
| **FORK-for-Grant** | Unique extremum lands near target but K/G=2 criterion is doing all the work (relabel of EMT crossing, not distinct from counting route) |

## Discipline tags

- **consistency-vs-emergence:** target is **Class D emergence** if CHORD; otherwise **Class C consistency** or **ECHO confirmation**
- **substrate-native-check:** FTG-EMT on amorphous network, not Cartesian minimization; no gradient descent on energy landscape
- **ave-driver-script-honesty:** forward solve only; CODATA comparison separated
- **ave-evidence-framing-discipline:** report measured `α_pred` and `% error` from tool output, not rounded claims

## Expected pre-registration stance

**Expect ECHO or PARTIAL, not CHORD.** K/G=2 is GR-imported; z₀=52 already known to land ~1.5% off (`2026-05-18` result). The test distinguishes whether a **variational** functional adds anything beyond the EMT crossing constraint. A unique η-maximum at the same point as A1 = **FORK-for-Grant** (relabel). A different optimum = informative negative.
