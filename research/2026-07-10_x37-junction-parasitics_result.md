# RESULT — X37: junction-parasitic extraction — **the srs vertex is a REACTIVE LOW-PASS; the ceiling is EXTENT-DOMINATED → BRANCH (iii)**

**Date:** 2026-07-10 · **Branch:** `analysis/x37-junction-parasitics` (off main @ ba662d57) · **Task:** X37 (Grant-fired, D-I route after #613/X36 was BLOCKED for installing)
**Prereg (FROZEN):** [`2026-07-10_x37-junction-parasitics_prereg_FROZEN.md`](2026-07-10_x37-junction-parasitics_prereg_FROZEN.md) — commit `167f28ce`, **pushed 2026-07-10T06:38:47Z BEFORE any driver code** (freeze verifiable by commit ordering).
**Derivation:** [`2026-07-10_x37-junction-parasitics_derivation.md`](2026-07-10_x37-junction-parasitics_derivation.md)
**Extraction module:** `src/ave/core/junction_parasitics.py` · **Driver:** `src/scripts/vol_1_foundations/x37_junction_parasitics.py` · **Tests:** `src/tests/test_x37_junction_parasitics.py`
**Data:** `src/scripts/vol_1_foundations/_output/x37_junction_parasitics.json` · **Figure:** `src/scripts/vol_1_foundations/_output/x37_junction_parasitics.png` (WHITE, house style)

**SECTOR HEADER.** MODE = linear small-signal band structure. REGIME = cold, sub-yield, lossless (reactive-only). SECTOR = scalar / compression channel (Phase 1); vertex DOF = the breathing/dilatational compliance of the junction region. Vector/torsion scoped out (§6).

**CLASS (consistency-vs-emergence).** **MIXED.** The g-factor VALUE is **derived-geometric** (the extraction module imports NO physical scale — MU_0/EPSILON_0/ℓ_node cancel; g is a pure number). The SCALE `ω_C = c/ℓ_node` is **dimensional-forced / identity** and appears only as the reporting unit. "Ceiling near ω_C" is dimensionally forced and gets NO credit; the deliverable is the topology class + the extent-sensitivity.

---

## 0. TL;DR — the verdict

The srs vertex equivalent circuit is **EXTRACTED, not installed**: a quasi-static TL discontinuity analysis of three 120° bonds gives a **shunt accumulator** `C_j = s_C·ε₀·d` + a **series throat** `L_j = s_L·μ₀·d` over a junction extent `d = f·ℓ_node`. Inserted into the memoryless srs nodal-KCL dispersion:

- **TOPOLOGY CLASS = REACTIVE LOW-PASS.** Both the accumulator and the throat **LOWER the connected-band ceiling** (pin it DOWN) by **opening a zone-edge stop-band**. It is **NOT** a resonant series-trap in the through-path, **NOT** a parallel-bypass (it does **not** lift), **NOT** a clean partitioned-η. This **confirms** the walk's "compression engages the shunt compliance" lean, **adds** the series throat, and **refutes** any "junction lifts the ceiling."
- **g_scalar recovers #604 exactly as f→0** (5.441398 ω_C, err 2e-16; G-B), and drops to **3.7304 ω_C at the Wigner–Seitz probe f=0.5** (s_L=s_C=1). The **swing over f∈[0,0.5] is 31.4%** of π√3 — far above the 10% branch-(iii) threshold.
- **⇒ BRANCH (iii): the junction question is NOT closable at the TL-abstraction level.** The FORM `ω_vertex = g·c/ℓ_node`, `g = O(1)`, is derived; the MAGNITUDE is **extent-dominated** because **canon fixes no transverse bond scale** to pin the extent `f`. This is precisely why X36 had to install a scale — and precisely what X37 refuses to do.
- **All four gates PASS, each with a planted-violation proof (G-D).** 17 tests pass; `make verify` green.

---

## 1. The extracted vertex equivalent circuit (the deliverable)

| Quantity | Value | Provenance |
|---|---|---|
| shunt accumulator `C_j` | `s_C · ε₀ · d`, `d = f·ℓ_node` | excess compression-compliance of the merge volume (symmetric/breathing mode couples here) |
| series throat `L_j` | `s_L · μ₀ · d` | excess flux-crowding inertia in each arm |
| shape factors `s_L, s_C` | O(1); **`= 1` (equivalent-length normalization, flagged modeling choice)** | need a transverse bond profile canon does NOT provide (§4) |
| junction self-resonance | `ω_vertex = ω_C / (√(s_L s_C)·f)` | pure ratio; `= 2 ω_C` at f=0.5 |
| crossover (ω_vertex = π√3 ω_C) | `f_crit ≈ 0.184` (s=1) | below f_crit the junction resonance sits ABOVE the band (memoryless ~intact); above it, the junction caps the band |

Loaded srs nodal-KCL dispersion (exact lumped-equivalent ABCD): `μ = 3[cosθ − (x/2)sinθ] − p[sinθ + x cosθ − (x²/4)sinθ]`, `x = s_L f θ`, `p = s_C f θ`, `θ = arccos`-branch bond electrical length, `ω = √3 ω_C · θ`. `f=0 ⇒ μ = 3cosθ` (the #604 memoryless map).

**Topology class, stated precisely:** the vertex opens a **re-entrant zone-edge gap**; the CONNECTED-band ceiling is set by the **first `μ=−3` crossing** (the stronger reactive channel), and the FULL spectrum acquires a thin re-entrant sliver up to the isolated H-point. Reactive low-pass; ceiling pinned DOWN ∝ extent.

## 2. g_scalar + the extent-sensitivity sweep (G-C first-class result)

`g_scalar(f) = ω_top/ω_C` at `s_L = s_C = 1` (exact connected-band solve):

| f (= d/ℓ_node) | g_scalar (ω_C) | drop vs π√3 | ω_vertex (ω_C) |
|---|---|---|---|
| 0.00 (canon-faithful) | **5.4414** | 0.0% | ∞ (point junction) |
| 0.04 | 5.2324 | 3.8% | 25.0 |
| 0.10 | 4.9498 | 9.0% | 10.0 |
| 0.20 | 4.5513 | 16.4% | 5.0 |
| 0.30 | 4.2260 | 22.3% | 3.33 |
| 0.50 (Wigner–Seitz probe) | **3.7304** | 31.4% | 2.0 |

**Extent swing |g(0) − g(0.5)| / π√3 = 31.4% ≫ 10% (branch-iii threshold).** The ceiling is not robust to the extent → the junction question is not closable at TL abstraction (§4). Figure Panel A also shows the **channel decomposition** (pure-throat vs pure-accumulator) and the **non-additive** combined curve (§3); Panel B shows `ω_vertex(f)` crossing π√3 at `f_crit ≈ 0.184`.

## 3. Driver-time finding (Rule 10) — the combined ceiling is NON-ADDITIVE

The exact solver surfaced a subtlety the O(f) linearization hides (derivation §4a): `κ = s_L + (2/3)s_C` is the correct LOCAL-μ slope and matches the exact solve to <0.1% for a **single** active channel, but the combined ceiling **tracks the stronger (throat) channel, not the sum** — because once `s_C>0` the loaded `μ(θ)` goes non-monotonic near the zone edge (dips below the adjacency floor at the throat-set first crossing, then recovers into the re-entrant sliver up to `μ(π) = −3 + s_L s_C f²π² > −3`). The accumulator's extra loading is absorbed into the re-entrant gap ABOVE the first crossing. Headline unchanged; topology sharpened. Validated by `test_combined_channel_is_non_additive`.

## 4. Why BRANCH (iii): the closability finding (the honest core)

- **Canon-faithful limit `f → 0`:** 1D-line bonds ⇒ point junction ⇒ parasitic → 0 ⇒ memoryless π√3 ω_C exact. Not a rescue — what the canonical geometry literally implies.
- **The parasitic exists only for `d > 0`, and `constants.py` fixes NO transverse bond scale** (only `ℓ_node` and the *larger* `ℓ_c = √6·ℓ_node`; no bond radius, core radius, or filling fraction). So both the extent `f` AND the shape factors `s_L, s_C` are O(1) numbers **not determined by canon**.
- The ceiling shift is `O(κ f)` and swings 31% over the plausible `f∈[0,0.5]` ⇒ **extent-dominated ⇒ branch (iii): the junction clock's SCALE is not closable at the TL abstraction level.** The g-FORM and the topology class stand; the number does not.
- **This is exactly why X36 (#613) had to install a scale** — canon underdetermines the vertex reactance. X37 surfaces the underdetermination honestly instead of hiding it in an installed tank.

**What would flip it to branch (i)** (surfaced pre-test-physics question, §2 prereg): if canon or Grant supplies a bond transverse scale making `f ≲ 0.02`, the ceiling recovers π√3 within tolerance and the vertex clock = the walk clock (the X33 two-clock question closes in-engine). That is a Grant/corpus anchor, not a lane decision — flag-don't-fix.

## 5. Gate ledger (all PASS; every gate consumes a COMPUTED quantity with a firing tolerance — G-D)

| Gate | Condition (frozen) | Result | Planted-violation proof | Pass |
|---|---|---|---|---|
| **G-A anti-install** | extraction module references none of {OMEGA_C, M_E, L_CELL, C_CELL}, imports no `ave.core.constants` (AST scan) | name_hits `[]`, import_hits `[]` | `OMEGA_C`-in-body snippet → scanner FLAGS it (`test_gate_A_planted_violation_fires`); docstring mentions ignored (`test_gate_A_scanner_ignores_docstrings`) | ✅ |
| **G-B independent-reference recovery** | g(f=0) = FROZEN #604 top π√3 (hard-coded FROM `..._srs-band-survey_result.md:18`, cited; not self-recomputed) | 5.441398092702652 vs 5.441398092702653, rel err **2.0e-16 < 1e-3** | +1% offset f→0 → rel err 1e-2 ≥ 1e-3, gate FAILS (`test_gate_B_planted_violation_fires`) | ✅ |
| **G-C vertex-extent honesty** | extent derived + swept; branch by frozen rule | swing **31.4% > 10%** → branch **(iii)** | flat (control) ceiling NOT flagged; real f-dependent IS flagged (`test_gate_C_planted_detector_discriminates`) | ✅ |
| **G-D gates-can-fire** | every gate consumes a computed quantity with a failing tolerance | all three plants FIRE; no-op control does not | (the three above) | ✅ |

**17 tests pass** (`src/tests/test_x37_junction_parasitics.py`), incl. topology-class, monotonicity, single-channel-anchor, non-additivity, junction-resonance-ratio, and the M6 FORM check (`g = O(1)` — no "ceiling near ω_C" credit).

## 6. Scope / what is deferred (honest tractability, prereg §8)

- **Phase 1 delivered:** the SCALAR/compression channel — full extraction, topology class, g_scalar, extent sweep, gates.
- **Vector/torsion channels SCOPED OUT** as the named follow-on. The vector vertex DOF is the **flywheel** (rotational inertia of the vertex plane) engaged by torsion; shear may largely bypass. That needs the 3-DOF (Cosserat) port scatter + the per-branch (longitudinal/transverse) network velocity gates — a full follow-on arc (matches the #604 §5 / srs-vector-survey deferral). Channel-anisotropic ceilings from ONE geometry would speak to the #607 lifted-vector question; not attempted here. An honest Phase-1-only result beats an overreached full one.
- **The shape factors `s_L, s_C`** are set to the equivalent-length normalization `= 1`; a first-principles value needs the transverse bond profile (the branch-(iii) obstruction). Flagged, not fudged.

## 7. Reproduce / outputs

```
make verify        # -> "[Verify] ALL PHYSICS PROTOCOLS PASSED."
PYTHONPATH=src python3 -m pytest src/tests/test_x37_junction_parasitics.py -q   # -> 17 passed
PYTHONPATH=src python3 src/scripts/vol_1_foundations/x37_junction_parasitics.py # -> ledger + JSON + WHITE figure
```

Driver ledger (stdout):
```
  #604 memoryless top   : 5.441398 omega_C (2.7805 MeV)  [research/2026-07-09_srs-band-survey_result.md:18]
  topology class        : reactive-low-pass (accumulator+throat pin the ceiling DOWN; zone-edge gap opens)
  vertex circuit @f*=0.5: L_j=0.500 mu_0 ell, C_j=0.500 eps_0 ell, omega_vertex=2.000 omega_C
  g_scalar(f=0)         : 5.441398 omega_C  (must = #604)
  g_scalar(f*=0.5)      : 3.730401 omega_C
  extent swing [0,0.5]  : 31.4% of pi*sqrt3
  BRANCH FIRED          : (iii)
  [PASS] G-A / G-A planted / G-B / G-B planted / G-C / G-C planted
```

## 8. Corpus-state consequences (for the auditor to land — lane discipline; NOT landed here)

Surfaced to the auditor's manuscript / COLLABORATION_NOTES queue (the manual entries are the auditor's to land):
1. **The srs vertex is a REACTIVE LOW-PASS** for the scalar/compression channel (shunt accumulator + series throat, both pin the ceiling DOWN by opening a zone-edge gap). This is the DERIVED (not installed) answer to the X36 question; it confirms the walk's shunt-compliance lean and refutes a "lift."
2. **The junction clock's SCALE is not closable at the TL-abstraction level** (branch iii): canon fixes no transverse bond scale, so the ceiling is extent-dominated (31% swing over f∈[0,0.5]). This is a **pre-test-physics question for Grant**: does the vacuum bond have a transverse extent (and what fixes it), or is the vertex a true point-junction (parasitic → 0, memoryless π√3 exact, and the X33 two-clock question then closes in-engine)?
3. **X33 consumer:** the two-clock (walk-pins vs vertex-clock) fork is NOT settled by X37 — it is TYPED as extent-conditional. It closes to ONE clock iff the bond transverse scale gives `f ≲ 0.02`; otherwise the vertex clock is a genuine (extent-dominated) second scale.
4. **Methodological:** the anti-install gate (G-A, AST scan of the extraction path for forbidden scales + planted-violation proof) is a reusable machine-check of the #613 lesson — candidate for the driver-honesty / substrate-native-check toolkit.

**No leaf edit from this lane.** These are ledger rows + a Grant-anchor question, surfaced for the auditor.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
