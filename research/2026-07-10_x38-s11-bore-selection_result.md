# RESULT — X38: S₁₁-minimization bore selection — **the substrate does NOT select a bore; Op6 picks the POINT JUNCTION → BRANCH (ii)**

**Date:** 2026-07-10 · **Branch:** `analysis/x38-s11-bore-selection` (off main @ 85f8b3d5, incl. #615) · **Task:** X38 (Grant-fired 2026-07-10, "fire x38 with the S11 route" — route d for the bond-bore fork X37/#616 sharpened)
**Prereg (FROZEN):** [`2026-07-10_x38-s11-bore-selection_prereg_FROZEN.md`](2026-07-10_x38-s11-bore-selection_prereg_FROZEN.md) — commit `cc386be1`, **committed 2026-07-10T14:46:25Z / pushed 14:46:55Z BEFORE any driver code** (freeze verifiable by commit ordering + `gh api`).
**Derivation:** [`2026-07-10_x38-s11-bore-selection_derivation.md`](2026-07-10_x38-s11-bore-selection_derivation.md)
**S₁₁ module:** `src/ave/core/junction_scattering.py` · **Driver:** `src/scripts/vol_1_foundations/x38_s11_bore_selection.py` · **Tests:** `src/tests/test_x38_s11_bore_selection.py`
**Data:** `src/scripts/vol_1_foundations/_output/x38_s11_bore_selection.json` · **Figure:** `..._output/x38_s11_bore_selection.png` (WHITE, house style)

**SECTOR HEADER.** MODE = linear small-signal (S-parameters). REGIME = cold, sub-yield, lossless (reactive-only). SECTOR = bare-bond network primitive (scalar/compression channel, Phase 1); soliton scales are frozen comparison marks only. Vector/torsion scoped out (§6).

**CLASS (consistency-vs-emergence).** **MIXED.** The selected `f*` is **derived-geometric** (the S₁₁ module imports NO physical scale — MU_0/EPSILON_0/ℓ_node cancel; the argmin is a pure number). The **SCALE** `ω_C = c/ℓ_node` is **dimensional-forced / identity** and appears only as the reporting unit. The deliverable is which branch fired + the objective spread; no emergent-scale headline (the branch is `f* = 0`).

---

## 0. TL;DR — the verdict

Applying canon's OWN geometry-selection operator (**Universal Operator #6**, `λ_min(S†S) → 0`, [`eigenvalue-target.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/eigenvalue-target.md) `clm-gdd70j` — the operator that selected the trefoil `R·r = 1/4`) at the srs vertex: **the substrate does NOT select a nontrivial bore. All three frozen objectives pick `f* = 0` — the POINT JUNCTION → BRANCH (ii).**

- **BARE-JUNCTION MISMATCH VERIFIED.** A wave down one srs bond sees the other two in parallel (`Z₀/2`), so `Γ = S₁₁ = (2−z)/z = −1/3` for `z=3`: the memoryless junction back-scatters `|Γ|² = 1/9` of the power and is **NOT matched**. Recovered analytically AND through the LOADED S₁₁ path (`f→0`, no early return) to `0.0e+00` rel error.
- **THE L-MATCH OBSERVATION: CONFIRMED AS A NETWORK FACT, REFUTED AT THE VERTEX.** The 2:1 step has `Q = √(2−1) = 1`, and the ideal 2-element L-match nulls `|S₁₁|→0` — verified. **But the substrate's parasitic geometry is the OPPOSITE orientation** (accumulator/shunt-C at the low-Z node, throat/series-L in the arms = the step-DOWN L), and **C₃ᵥ symmetry forbids a privileged one-arm shunt** — so the matching network is unavailable at the vertex. **The bore NEVER dips `|S₁₁|` below the bare `1/3`; it only adds reflection** (`|S₁₁| ≥ 1/3` for all θ, all f, all `s>0`, proven analytically and numerically).
- **THE Op6 REFLECTIONLESS TARGET IS UNREACHABLE.** `min_θ |S₁₁|² = 1/9` for **ALL** `f` (the trivial `θ→0` floor, shared by every extent) — `λ_min → 0` is never reached. **The srs vertex is an intrinsic `1/9`-power branch-back-scatterer — a structural feature of `z = 3`** (a `z=2` through-junction matches perfectly, `S₁₁ = 0`). Op6 cannot zero the vertex reflection; it can only pick the LEAST-reflecting realizable bore, which is `f = 0`.
- **f\* = 0 ROBUSTLY.** obj-1 (Op6 primary), obj-2 (band-integrated), obj-3 (single-freq) all give `f* = 0` with **spread = 0** at `s=1`; the PRIMARY objective gives `f* = 0` for **every** `(s_L, s_C) ∈ [0.3,3]²` (worst-case `f* = 0.010` is a float-tie on comparator obj-2's flat plateau — depth `6e-10`; still `< 0.02` robust). `f* = 0 < f_crit ≈ 0.184` → the lumped abstraction is self-consistent at its minimum (**does NOT self-invalidate**). `f* = 0` matches NEITHER soliton mark (`1/2π ≈ 0.159`, `1`) → **branch (i) identity candidate does NOT fire**.
- **⇒ BRANCH (ii): closure (c).** The matched junction is the point junction; the walk ceiling `π√3` (X37 `g(0)`) is exact; **the bore stays a non-object at this abstraction.** The X37 bond-bore fork is dissolved by the substrate's own operator: it does not want a bore.
- **All six gates PASS, each with a planted-violation proof (G-D).** 22 tests pass; `make verify` green.

---

## 1. What the substrate says (the honest core)

X37 sharpened the fork: is the bare-bond junction extent `f` (a) the tube radius `1/2π ≈ 0.159`, (b) the core-tube thickness `1`, or (c) neither (extent an import)? Adopting a soliton scale was a sector-ownership crosswire; X37 could not close it without a ruling. **X38 asks the substrate directly, using canon's own selection operator.** The answer is a fourth thing the X37 fork did not enumerate: **the operator selects `f = 0` — the extent that makes the junction reflect LEAST is no extent at all.** The bore is not scale-(a), not scale-(b), not an unresolved import — it is a **non-object**: any positive bore only adds reflection, so the reflection-minimizing vertex is the sharp point junction. This is closure (c) of the frozen branch set, reached constructively.

**Why (the plumber picture, confirmed).** In a real 3-way tee a surge partially reflects off the branch (the two other pipes = a lower combined impedance, `Z₀/2`). Rounding the tee — adding the accumulator volume + the throat — is on the WRONG side to cancel that: the accumulator sits at the low-impedance node and the throat is in the arms, which is the impedance step-DOWN L-network, the opposite of the step-UP L that would raise `Z₀/2` back to `Z₀`. And the tee's 3-fold symmetry forbids putting the fillet on one privileged arm. So the sharpest tee reflects least, and the reflection you cannot remove — the `1/9`-power branch back-scatter — is the structural price of `z = 3` branching.

---

## 2. Bare-junction Γ = −1/3 + the L-match confirmation/refutation (frozen expectations, §5 prereg)

| Frozen analytic expectation (M6) | Verdict | Evidence |
|---|---|---|
| **BARE MISMATCH** `S₁₁(f=0) = (2−z)/z = −1/3` (`z=3`), memoryless NOT matched | **CONFIRMED** | analytic `bare_junction_s11(3) = −0.3333…`; loaded S₁₁ `f→0` recovers `|S₁₁| = 1/3` to `0.0e+00` (G-B) |
| **L-MATCH** `Q = √(Z_hi/Z_lo − 1) = 1`; ideal 2-element network nulls `|S₁₁|→0` | **CONFIRMED as a network fact** | `test_l_match_ideal_null_is_reachable_Q_equals_one` — the correct-orientation L (series toward the `Z₀/2` load + shunt on the HIGH/source side) nulls to `< 1e-9` |
| **L-MATCH at the physical vertex** — does `|S₁₁|` dip below `1/3`? | **REFUTED** | orientation (accumulator on low-Z node) + C₃ᵥ (no privileged one-arm shunt) ⇒ `min_θ,f,s |S₁₁| ≥ 1/3`; small-θ expansion `|S₁₁|² = (¼+b²)/(9/4+b²)`, `b=[(3/2)s_L−(¼)s_C]fθ`, monotone in `b²` |

**The small-θ expansion is the analytic backbone:** `|S₁₁|² = (¼ + b²)/(9/4 + b²)` is monotone increasing in `b²`, minimized at `b = 0` (`θ=0` or `f=0`) where `|S₁₁|² = 1/9`. Any `f>0` makes the reactance `b ≠ 0` across the band ⇒ `|S₁₁| > 1/3` everywhere except the trivial DC point. (Matches the exact S₁₁ to 6 digits at `θ=10⁻³`.)

---

## 3. f* under each objective + the s-sweep + which branch fired (G-C first-class)

`f* = argmin_{f∈[0,0.5]}` (dense boundary-inclusive grid; `f=0` is a candidate — no dead-actuator):

| Objective (prereg §4) | `f*` (s=1) | J(f*) | note |
|---|---|---|---|
| **obj-1 (canonical Op6, PRIMARY)** `\|S₁₁(π;f)\|²` via `universal_eigenvalue_target` | **0.0000** | `1/9` | band-top mode `θ=π`; canonical code path |
| **obj-2 (band-integrated, comparator)** `⟨\|S₁₁\|²⟩` over connected band | **0.0000** | `1/9` | integrates over `θ_top(f)` (X37 loaded ceiling) |
| **obj-3 (single-freq, comparator)** `\|S₁₁(π/2;f)\|²` | **0.0000** | `1/9` | mid-band |
| **objective SPREAD** (branch-iv detector) | **0.0000** | — | `< 0.02` robust ⇒ NOT branch (iv) |

**s-sweep** `s_L,s_C ∈ {0.3,0.5,1,2,3}²` (X37 R5 lesson — the bracket was doubly conditional): **PRIMARY obj-1 gives `f* = 0` at EVERY cell.** Worst-case `f*` over all objectives/cells `= 0.010`, max spread `= 0.010` — a **float-tie** on comparator obj-2's flat plateau at the strong-accumulator cell (`s_L=1, s_C=3`), where obj-2 is flat to `6e-10` over `f∈[0,0.02]`; the argmin lands at `0.010` by floating-point tie-break, not a physical selection. Both `< 0.02` (robust). **`f* = 0` is robust to the shape factors** — the X37 doubly-conditional bracket does NOT reopen the selection.

**Which branch fired: (ii).** `f* = 0` (boundary minimum) robustly ⇒ the matched junction is the point junction ⇒ **closure (c)**: the walk ceiling `π√3` is exact, the bore stays a non-object at this abstraction. `f* = 0 < f_crit = 0.184` ⇒ self-consistent (does NOT self-invalidate). `f* = 0 ∉ {1/2π, 1}` ⇒ branch (i) does NOT fire; the winding-is-the-wire identity candidate is not triggered.

**HONEST near-degeneracy disclosure (visible in the figure Panel B).** obj-1 `|S₁₁(π;f)|²` has a **near-degenerate SECOND local minimum at `f ≈ 0.45`** (the vertex self-resonance brings `|S₁₁(π)|` back toward `1/3`) reaching `+2.7e-08` above the `f=0` floor. It **does NOT beat `f=0`** (f=0 is the global argmin) AND it sits at **`f = 0.45 > f_crit = 0.184`** — the regime where the quasi-static lumped separation self-invalidates (X37 C2) — so it is **not a physical competitor**. Surfaced first (a reviewer will see the dip); `f* = 0` stands.

---

## 4. Gate ledger (all PASS; each consumes a COMPUTED quantity with a firing tolerance — G-D)

| Gate | Condition (frozen) | Result | Planted-violation proof | Pass |
|---|---|---|---|---|
| **G-A anti-install** | S₁₁ module references none of `{OMEGA_C,M_E,L_CELL,C_CELL}`, imports no `ave.core.constants`, carries no forbidden numeric LITERAL (AST scan — symbol+import+literal, ported from X37 R8) | name_hits `[]`, import_hits `[]`, literal_hits `[]` | `OMEGA_C` by SYMBOL and by NUMERIC LITERAL both FLAGGED (`test_gate_A_planted_symbol_and_literal_both_fire`). Disclosed limit: arithmetic on allowed literals not literal-caught (structural guarantee = no-scale-import invariant + §3 cancellation) | ✅ |
| **G-B independent-reference recovery** | LOADED path recovers (i) bare `\|S₁₁\|=1/3` AND (ii) `π√3` ceiling (hard-coded FROM #604:18, cited) — exercised, not an early-return (X37 R3) | bare rel `0.0e+00`, ceiling rel `0.0e+00`, both `< 1e-4` | +1% offset on BOTH loaded recoveries → both FAIL (`test_gate_B_planted_offset_fires`) | ✅ |
| **G-C objective-robustness (branch-iv detector)** | `f*` under all three objectives; spread reported first-class; branch by frozen rule | spread `0.0`, branch **(ii)** | divergent bogus objective (maximise reflection → `f≠0`) pushes spread across the scatter threshold; the 3 real objectives (control) do NOT (`test_gate_C_planted_divergent_objective_fires_scatter_detector`) | ✅ |
| **G-D gates-can-fire** | every gate consumes a computed quantity with a failing tolerance | all plants FIRE; no-op controls do not | (the three above) | ✅ |

**22 tests pass** (`src/tests/test_x38_s11_bore_selection.py`), incl. the bare Γ=−1/3 + general `(2−z)/z`, the canonical-operator equality (`op6_lambda_min == |S₁₁|²` via `universal_eigenvalue_target`), the Op6-target-unreachable identity (`deepest_notch = 1/9 ∀f`), the L-match confirm + refute, the small-θ expansion, the three-objective argmin, the s-grid robustness, the near-degeneracy disclosure, and the four gates + planted proofs.

---

## 5. Post-freeze deviation log (named, none silent — X37 R2 discipline)

- **D1 — G-B recovery route (prereg §6 "via the X37 module").** *Frozen:* recover `π√3` "via the X37 module." *Shipped:* **X37's `junction_parasitics.py` is UNMERGED on main** (main @ 85f8b3d5 does not contain it), so it cannot be imported. The `π√3` ceiling is recovered through the X37 **loaded-μ form PORTED** into `junction_scattering.connected_band_top_theta` (cited to the origin branch + derivation §1) — identical parasitics (`x=s_L f θ`, `p=s_C f θ`), so the cross-check of my elements against X37's ceiling stands. Recovery is exact (`0.0e+00` rel). Disclosed, not silent.
- **D2 — G-A scan provenance (prereg §6 "reuse X37's `scan_forbidden_inputs`").** Same cause (X37 unmerged): `scan_forbidden_inputs` / `_FORBIDDEN_MAGNITUDES` are **PORTED with an explicit provenance citation** to the X37 driver (origin branch, commit `1186c891`, review R8) in the X38 driver — a cited port, not a silent fork-copy, and not an import (the module isn't on main).
- **D3 — obj-1 near-degenerate interior dip (not anticipated in the prereg).** Surfaced at driver time (Rule 10): obj-1 has a second local minimum at `f≈0.45` within `2.7e-8` of the `f=0` floor. Does not beat `f=0`; beyond `f_crit`; disclosed §3 + tested. Does not change the branch call.
- **D4 — s-sweep worst-case `f*=0.010` (float-tie).** The comparator obj-2 is flat to `6e-10` at the `s_L=1,s_C=3` cell, so its grid-argmin tie-breaks to `f=0.010`; the PRIMARY obj-1 is exactly `f*=0` everywhere. Reported raw (not massaged); `< 0.02` robust.

---

## 6. Scope / what is deferred (honest tractability, prereg §8)

- **Phase 1 delivered:** the SCALAR/compression channel S₁₁ — the exact symmetric 3-port reflection, the canonical Op6 argmin, the L-match refutation, the three-objective robustness, the s-sweep, the gates.
- **The closure is scoped to the leading-order positive-element lumped class** (X37 C2). A fuller vertex model (evanescent-mode stub / finite-volume resonant shunt branch presenting a NEGATIVE-reactance or resonant bypass) is NOT modeled here and is the only thing that could, in principle, present a matching notch — the named model-fidelity follow-on. Within this class the `f*=0` refutation is exact.
- **Vector/torsion channels SCOPED OUT** (vertex flywheel; shear) — matches the #604 §5 / X37 deferral.
- **The shape factors `s_L,s_C`** are the equivalent-length normalization `=1` (X37's flagged modeling choice) with the `[0.3,3]²` sweep as the honesty check; `f*=0` is robust to them.

## 7. Reproduce / outputs

```
make verify        # -> "[Verify] ALL PHYSICS PROTOCOLS PASSED."
PYTHONPATH=src python3 -m pytest src/tests/test_x38_s11_bore_selection.py -q   # -> 22 passed
PYTHONPATH=src python3 src/scripts/vol_1_foundations/x38_s11_bore_selection.py # -> ledger + JSON + WHITE figure
```

Driver ledger (stdout — current):
```
  objective (canon)     : Op6 lambda_min(S†S)->0  [eigenvalue-target.md clm-gdd70j]
  bare junction z=3     : S11 = -0.3333  (|S11|=1/3; memoryless NOT matched)
  L-match Q (2:1)       : 1.000  -> ideal null reachable; REFUTED at vertex (wrong orientation + C3v)
  Op6 reflectionless    : UNREACHABLE (min|S11|^2 = 1/9 for ALL f -> z=3 intrinsic backscatter)
  f* obj-1 Op6 (primary): 0.0000
  f* obj-2 band-int     : 0.0000
  f* obj-3 single-freq  : 0.0000
  objective spread      : 0.0000  (robust < 0.02; scatter >= 0.05)
  BRANCH FIRED          : (ii)   [f*=0 => point junction; walk ceiling pi*sqrt3 exact]
  f* vs f_crit          : f*=0 < f_crit=0.184 -> self-consistent (does NOT self-invalidate)
  vs soliton marks      : f*=0 != 1/2pi=0.159, != 1 -> branch (i) does NOT fire
  s-sweep [0.3,3]^2     : worst-case f*=0.010, max spread=0.0100 (f*=0 robust to s)
  obj-1 near-degeneracy : interior dip at f=0.450 is +2.73e-08 vs f=0 floor (beats f=0: False; beyond f_crit: True)
  G-B recovery (loaded) : bare|S11|=0.333333 (rel 0.0e+00), ceiling=5.441398 (rel 0.0e+00)
  [PASS] G-A / G-A planted / G-B / G-B planted / G-C / G-C planted
```

## 8. Corpus-state consequences (for the auditor to land — lane discipline; NOT landed here)

Surfaced to the auditor's manuscript / COLLABORATION_NOTES queue (the manual entries are the auditor's to land):
1. **The X37 bond-bore fork is DISSOLVED by the substrate's own operator (route d):** applying Universal Operator #6 (`λ_min(S†S)→0`) at the srs vertex selects `f* = 0` — the POINT JUNCTION — robustly across all three objectives and `s∈[0.3,3]²`. The bore is neither soliton scale (a)/(b) nor an unresolved import (c) but a **non-object**: any positive bore only adds reflection. **The X37 walk ceiling `π√3 ω_C` (g(0)) is thereby the Op6-SELECTED ceiling, exact** — the sector-ownership crosswire is avoided because the operator wants no bare-bond bore.
2. **NEW derived structural fact (flag for Grant — pre-test-physics answer):** the srs vertex is an **intrinsic `1/9`-power branch back-scatterer** — `S₁₁ = (2−z)/z = −1/3` for `z=3`, a structural property of the `z=3` coordination that NO bore can remove (Op6's reflectionless target is unreachable at the vertex; a `z=2` through-junction would match perfectly). **Grant question (ontology):** is this residual `Γ=−1/3` a physical, real back-scatter at every vacuum vertex (a per-vertex reflection loss in the network), or an idealization of the bare 3-port star that a distributed merge smooths out (which would require the named out-of-class evanescent/resonant vertex model)? Not silently resolved.
3. **Methodological (candidate for the driver-honesty toolkit):** X38 demonstrates the **canonical-operator-as-selector** pattern — pull the canonical Op (here Op6 via `universal_eigenvalue_target`), apply it to the substrate geometry, and let the argmin adjudicate a fork the walk could not close. The objective-robustness gate (G-C, spread across ≥3 readings = the branch-(iv) detector, with a planted divergent-objective proof) is a reusable machine-check that the selection is not an artifact of one arbitrary functional reading.

**No leaf edit from this lane.** These are ledger rows + a Grant-anchor question, surfaced for the auditor.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
