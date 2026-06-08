# Path C — z₀ from K4 Amorphous Geometry, ALPHA-FREE — Result

**Date**: 2026-06-08
**Pre-registration**: [`2026-06-08_pathc-z0-amorphous-emt-prereg.md`](2026-06-08_pathc-z0-amorphous-emt-prereg.md) (FROZEN before computation, SHA `6b94b2cc`)
**Script**: [`src/scripts/vol_1_foundations/pathc_amorphous_z0.py`](../src/scripts/vol_1_foundations/pathc_amorphous_z0.py)
**Branch**: `analysis/2026-06-08-pathc-z0-amorphous-emt`
**Lane**: implementer

## TL;DR — Outcome D (model-dependent, with a directional signal); α NOT derived

**Coordination-preserving amorphous disorder of the K4 lattice DOES reduce the effective coordination z₀ from the crystalline 52 into a band [50.87, 51.67] that STRADDLES the EMT-canonical 51.25 — fully α-free, via an identified mechanism (4-ring formation merging 2-hop endpoints). BUT no α-free principle selects 51.25: the value is set by the (free) disorder strength, and the most-principled disorder-independent high-disorder steady-state lands at z₀ ≈ 51.65 (1/α = 138.0), not 51.25.**

- This is **not Outcome A** (DERIVED): there is no α-free fixed point at 51.25; hitting 51.25 exactly requires choosing a specific, un-derived disorder amount.
- This is **not Outcome C** (CIRCULAR): the whole z₀ band was reached with **zero α / SI / 1.187 input** — the α-free guard held (verified: `'ave.core' in modules: False`, no 1.187 anywhere).
- It is **Outcome D**: amorphous z₀ depends on the disorder model; no natural α-free selection of 51.25.
- **The α-derivation claim does NOT survive. α stays Class-B (honest-α relabel preserved).**

But the result is a genuine advance over the 2026-05-18 attempt: that found amorphous (Gaussian-position) disorder collapses z₀ to 4–5 — the WRONG direction. This finds the **right direction and the right magnitude** with an α-free mechanism, halving the crystalline-to-CODATA gap (1.38% → 0.74%) at steady-state.

## Method (α-free; prereg §3–4)

Radius-free / topology-only. The over-bracing radius 1.187 is **forbidden** because the corpus's own chain `C_ratio = (p_cauchy/p_c)^{1/3}, p_c = 8πα` makes it α-derived (`trace-reversal-mechanism.md:22`, `graph-architecture.md:31`). So:

1. Build a diamond/K4 supercell (N = 512, L = 4, unit pitch — no radius), take the **4-nearest-neighbour bond graph** (the K4 coordination, pure topology).
2. **Crystalline baseline**: measure ⟨z₂⟩ = mean count of distinct nodes at graph-distance exactly 2. Canonical path-count z₀ = z_primary·(1 + |T|) with |T| ≡ ⟨z₂⟩.
3. **Amorphous ensemble**: WWW bond-switching (every node held at degree 4 — coordination-preserving, the substrate-native disorder; NOT the coordination-breaking position-smear prior Model 3 already falsified). Sweep disorder strength (accepted switches per node), 8 seeds each. Re-measure ⟨z₂⟩.
4. **EMT readout** (α OUT): p_c = (10z₀−12)/(z₀(z₀+2)); implied 1/α = 8π/p_c. CODATA 1/137.036 used only in a one-way external comparison, never fed back.

## α-free input trace (the load-bearing guard)

Every quantity entering z₀, verified in-run:

| Input | Value | α-free? |
|---|---|---|
| K4/diamond coordination | 4 | yes (topological) |
| \|T\| (proper tetrahedral rotation group order) | 12 | yes (group order) |
| WWW disorder strength | switches/node | yes (geometric move count) |
| 8π (EMT readout) | 25.1327 | yes (pure geometry, **not** 8πα) |
| r_secondary = 1.187 / C_ratio | — | **ABSENT** (corpus-confirmed α-derived → forbidden) |
| `ave.core.constants` import | — | **ABSENT** (`'ave.core' in modules: False`) |
| e, ε₀, ħ, Z₀, c (SI) | — | **ABSENT** |

No α-leak. The band was reached α-free.

**Scanner/guard interplay (flag, not a conflict)**: the DAG anti-cheat scan (`verify_universe.py`) forbids a hardcoded 137.036, while the Path-C α-free guard forbids importing α from `constants.py`. Both are honoured by keeping the CODATA comparison **in this result doc only** — the script reports the *implied* 1/α = 8π/p_c(z₀) (α-free, computed from geometry) and contains zero α in any form (no literal, no import). The script verifies `MATHEMATICALLY PURE` under the anti-cheat scan. The CODATA numbers below never enter any z₀ computation.

## Results

**Crystalline (α-free baseline)**: ⟨z₂⟩ = 12.0000 ± 0.0000 (= |T| exactly; zero short rings) → z₀ = 52.000 → **1/α = 138.92** (dev **+1.38%** vs CODATA).

**Amorphous (coordination-preserving WWW; mean ± std over 8 seeds)**:

```
switch/node     <z2>            z0              1/alpha       4-ring/node
   0.25     11.861 ± 0.04   51.443 ± 0.16   137.53 ± 0.40      0.14
   0.50     11.735 ± 0.04   50.941 ± 0.17   136.27 ± 0.42      0.26
   1.00     11.718 ± 0.03   50.873 ± 0.13   136.10 ± 0.33      0.28
   2.00     11.788 ± 0.03   51.150 ± 0.14   136.79 ± 0.35      0.21
   4.00     11.896 ± 0.02   51.584 ± 0.09   137.88 ± 0.23      0.10
   8.00     11.918 ± 0.02   51.672 ± 0.09   138.10 ± 0.22      0.08
  16.00     11.908 ± 0.02   51.631 ± 0.09   138.00 ± 0.23      0.09
```

Error bars are tight (±0.1–0.17 in z₀): the disorder-dependence is **real, not noise**.

- **Mechanism identified (α-free)**: disorder forms **4-rings** (count rises 0→0.28/node then relaxes to ~0.09/node). A 4-ring merges two 2-hop paths onto one atom, so ⟨z₂⟩ drops below 12. This is the over-bracing/secondary-network reduction, derived from topology alone.
- **Target 51.25 needs ⟨z₂⟩ = 11.8125** (remove 0.1875 second-neighbours/node). The amorphous band [11.72, 11.92] **brackets** this, crossing 51.25 twice (descending ~0.4 switch/node, re-ascending ~2.5 switch/node).
- **High-disorder steady-state** (the disorder-independent asymptote, switch/node ≥ 8): z₀ ≈ **51.65**, 1/α ≈ **138.05** (dev **+0.74%**). This is the most-principled value (no tuned strength), and it is **not** 51.25 — it halves the crystalline gap but does not close it.

## Outcome classification (prereg §7)

**Primary: Outcome D (MODEL-DEPENDENT), with a directional + magnitude signal.**

- **A (DERIVED)** — NOT met. No α-free fixed point at 51.25; the steady-state asymptote is 51.65; hitting 51.25 needs a tuned disorder strength.
- **B (GAP REAL)** — partially. Crystalline z₀ = 52 (gap real there), but disorder *does* move z₀ — so the pure "stuck at 52" form of B is superseded.
- **C (CIRCULAR)** — NOT met (the positive result, on the guard). The 51.x band was reached fully α-free; α did **not** sneak in.
- **D (MODEL-DEPENDENT)** — MET. z₀ ∈ [50.87, 51.67] depends on disorder strength; steady-state 51.65; no α-free principle selects 51.25.

**Consistency-vs-emergence tag**: this was an **emergence** attempt. Result = **failed emergence test** — the substrate does not α-free-*select* α. What it shows is a partial **manifestation**: an α-free mechanism constrains z₀ to ≈ [50.9, 51.7] (1/α ≈ [136.1, 138.1]), bracketing CODATA but not pinning it.

## What this means for the α-circularity question

- **The circularity is NOT broken.** 51.25 (1/α = 137.04) is still selected only by α-input. α stays **Class-B**; the honest-α relabel (2026-06-02) is preserved, not lifted.
- **But the gap is re-characterized.** Before: "z₀ = 52 from path-count vs 51.25 from α-inversion, with NO α-free mechanism bridging them." Now: "an α-free, coordination-preserving amorphous mechanism (4-ring 2-hop-merging) carries z₀ from 52 into a band that contains 51.25; the steady-state lands at 51.65 (0.74% from CODATA)." The residual gap is no longer "no mechanism" — it is **"which disorder / which ring statistics selects the exact value,"** which maps to the energy-relaxed CRN below.
- **Anti-rescue (Rule 11) honored.** The flagged coincidence 52 − 51.25 = 0.75 = 3/4 = η (K4 mesh forward-scatter efficiency) is **NOT reproduced** by the mechanism: the steady-state removes only ~0.35 second-neighbours/node (z₀ 52 → 51.65), not 0.75. I did not invoke 3/4, and did not tune disorder to manufacture 51.25.

## Caveats (scope honesty)

1. **No energy relaxation.** This is a *maximally-randomized topological* ensemble (WWW bond-switching with a no-3-ring constraint), NOT an energy-minimized a-Si-style CRN (Keating/Wooten-Winer-Weaire with a strain potential). A physically-relaxed network has a *specific* equilibrium ring statistics that could pin a *specific* ⟨z₂⟩. That relaxed-CRN computation is the multi-week work the 2026-05-18 doc flagged — and is the natural next step (below). The steady-state 51.65 here is the *topological-random* asymptote, an upper bracket on z₀, not the relaxed value.
2. **Finite size** (N = 512). The 4-ring density (hence ⟨z₂⟩ reduction) has finite-size sensitivity; a size sweep (L = 4, 6, 8) is needed to confirm the steady-state asymptote.
3. **Path-count convention.** z₀ = z_primary·(1 + |T|) = 4·13 is the corpus-canonical form (4·13); identifying the amorphous |T|_eff with ⟨z₂⟩ is a modeling choice. An alternative convention (distinct 2-hop ball = 4 + ⟨z₂⟩ = 16) gives a different EMT readout entirely — the EMT z₀ ≈ 51 only matches the multiplicative 4·(1+⟨z₂⟩) form, which is itself a corpus assumption, not independently forced.

## Path forward (scope for the multi-week close)

1. **Energy-relaxed CRN** — build a real Keating/WWW a-Si-class K4 network with strain-energy relaxation; read the *equilibrium* ⟨z₂⟩ and ring statistics; test whether the relaxed (disorder-independent, α-free) z₀ pins 51.25 or settles at 51.6. This is the decisive Path-C test; this first-pass is the scaffold + null bracket for it.
2. **Finite-size sweep** (L = 4/6/8) to nail the steady-state asymptote.
3. **Path-count convention audit** — adjudicate (Grant/auditor) whether z₀ = 4·(1+|T|) vs 4+|T| is the correct EMT coordination, since the two give 1/α = 138.9 vs an entirely different value. This convention is currently a corpus assumption, not derived — and it is *load-bearing* for whether the EMT readout is even the right map.

## Falsifier discipline

Pre-reg frozen before computation (SHA `6b94b2cc`); result logged regardless of outcome; no post-hoc rewrite of the outcome categories. Predicted Outcome D prior was ~20%; the directional+magnitude positive signal inside D was not specifically pre-registered but is reported as found. The α-derivation falsifier (prereg §7) returns: **α NOT derived; circularity not broken; α stays Class-B.**

## Cross-references

- Prior attempt: [`2026-05-18_z0-first-principles-attempt-result.md`](2026-05-18_z0-first-principles-attempt-result.md)
- Honest-α relabel (z₀ α-circular): `manuscript/backmatter/appendix_c_derived_numerology.tex:74-76`, `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md:22`
- Closure roadmap §0 row 2 (first-principles z₀ open): `manuscript/ave-kb/claim-quality-closure-roadmap.md`
- |T| = 12 four-routes leaf: `manuscript/ave-kb/common/claim-quality.md:1028`
