# RESULT — X37: junction-parasitic extraction — **the srs vertex is a REACTIVE LOW-PASS; the ceiling is EXTENT-DOMINATED → BRANCH (iii)**

**Date:** 2026-07-10 · **Branch:** `analysis/x37-junction-parasitics` (off main @ ba662d57) · **Task:** X37 (Grant-fired, D-I route after #613/X36 was BLOCKED for installing)
**Prereg (FROZEN):** [`2026-07-10_x37-junction-parasitics_prereg_FROZEN.md`](2026-07-10_x37-junction-parasitics_prereg_FROZEN.md) — commit `167f28ce`, **pushed 2026-07-10T06:38:47Z BEFORE any driver code** (freeze verifiable by commit ordering).
**Derivation:** [`2026-07-10_x37-junction-parasitics_derivation.md`](2026-07-10_x37-junction-parasitics_derivation.md)
**Extraction module:** `src/ave/core/junction_parasitics.py` · **Driver:** `src/scripts/vol_1_foundations/x37_junction_parasitics.py` · **Tests:** `src/tests/test_x37_junction_parasitics.py`
**Data:** `src/scripts/vol_1_foundations/_output/x37_junction_parasitics.json` · **Figure:** `src/scripts/vol_1_foundations/_output/x37_junction_parasitics.png` (WHITE, house style)

**SECTOR HEADER.** MODE = linear small-signal band structure. REGIME = cold, sub-yield, lossless (reactive-only). SECTOR = scalar / compression channel (Phase 1); vertex DOF = the breathing/dilatational compliance of the junction region. Vector/torsion scoped out (§6).

**CLASS (consistency-vs-emergence).** **MIXED.** The g-factor VALUE is **derived-geometric** (the extraction module imports NO physical scale — MU_0/EPSILON_0/ℓ_node cancel; g is a pure number). The SCALE `ω_C = c/ℓ_node` is **dimensional-forced / identity** and appears only as the reporting unit. "Ceiling near ω_C" is dimensionally forced and gets NO credit; the deliverable is the topology class + the extent-sensitivity.

---

> **⚠ RESTATED 2026-07-10 after the PR #616 adversarial review (17 findings; most disclosures held, a repair set survives). See the Correction Log (§0a). This TL;DR is the corrected form; the superseded verbs ("EXTRACTED/DERIVED, not installed", the unscoped "no lift", "canon fixes no transverse bond scale") are quoted there.**

## 0. TL;DR — the verdict

The srs vertex is modeled as a **leading-order lumped TL discontinuity equivalent (Marcuvitz-style)**: a **shunt accumulator** `C_j = s_C·ε₀·d` + a **series throat** `L_j = s_L·μ₀·d` over a junction extent `d = f·ℓ_node`, inserted into the memoryless srs nodal-KCL dispersion. **The circuit FORM is a disclosed modeling choice, NOT a from-geometry derivation** (Correction Log C1): the prereg's promise to COMPUTE `s_L, s_C` from the 120° convergence + srs twist was **not delivered** — `s_L=s_C=1` is assumed, and the 120°/twist enter **no shipped equation** (only the coordination `z=3` does; the identical circuit follows for **any 3-regular network**).

- **TOPOLOGY CLASS = REACTIVE LOW-PASS — as a PASSIVITY result, not a computed junction field.** For **any** positive two-element form (`s_L, s_C > 0`) every stored-energy channel lowers the cutoff, so the ceiling is pinned DOWN and a zone-edge stop-band opens. **Scope of the "no lift" claim (C2):** no lift **within this leading-order positive-element lumped class**. A fuller vertex model (evanescent-mode stub / finite junction volume = a resonant shunt branch) is **NOT excluded** and is exactly what could present a bypass; and for `f > f_crit ≈ 0.184` the junction resonance `ω_vertex` sits **inside** the band, where the quasi-static lumped separation **self-invalidates** — **most of the 31.4 % swing accrues there.**
- **g_scalar recovers #604 as f→0** (loaded solver at f=1e-5 converges to π√3=5.441398 ω_C within 1e-4; G-B now exercises the solver, not an early-return — C3), and drops to **3.7304 ω_C at the Wigner–Seitz probe f=0.5** at `s_L=s_C=1`. **This floor is DOUBLY conditional (f≤0.5 AND s=1):** sweeping `s_L,s_C∈[0.3,3]²` gives `g(0.5)∈[2.13, 4.74]` — the bracket floor is **2.13**, not 3.73 (R5). The **swing over f∈[0,0.5] is 31.4 %** of π√3, above the 10 % branch-(iii) threshold.
- **Reciprocity identity (R4):** at the reported `s_L=s_C=1`, the shunt accumulator has **EXACTLY ZERO effect** — the combined ceiling equals the pure-throat ceiling to 8e-13 on every `g(f)`. "Both channels lower" is true per-channel, but at s=1 the connected ceiling is set by the throat alone.
- **⇒ BRANCH (iii): the junction question is NOT closable WITHOUT a sector-ownership ruling (R6).** The FORM `ω_vertex = g·c/ℓ_node`, `g = O(1)`, is derived; the MAGNITUDE is **extent-dominated**, and canon's transverse scales are **soliton/core-sector** (§4). Three candidate closures for `f`: **(a)** the tube radius `ℓ_node/(2π)` (constants.py:76) → `f≈0.159`; **(b)** the core-tube thickness `d ≡ 1 ℓ_node` (constants.py:189) → `f≈1`; **(c)** neither applies to the bare bond (extent stays an import). This is a **sharpened PENDING-GRANT walk question**, not a closed number.
- **All four gates PASS, each with a planted-violation proof (G-D); the topology detector is now two-axis (lift VISIBLE, C3).** 24 tests pass; `make verify` green.

---

## 0a. Correction log (2026-07-10, PR #616 adversarial review — KEEP-BOTH, superseded text quoted)

The review returned 17 findings, 0 refuted; most DOWNGRADED on verify (the in-doc disclosures held), a repair set survives. The freeze-before-driver ordering was verified genuine via `gh api`. Code+gates repair landed in commit `1186c891` (R2/R3/R4/R5/R8); this doc restatement covers R1/R6/R7/R9 + the deviation ledger. Nothing is silently erased.

- **C1 (R1, MAJOR — canon-bound wording).** *Superseded:* §0 "The srs vertex equivalent circuit is **EXTRACTED, not installed**" and §8.1 "This is the **DERIVED (not installed)** answer to the X36 question." *Correction:* it is a **leading-order lumped TL discontinuity equivalent (Marcuvitz-style)**. The LOW-PASS class follows from **PASSIVITY** of the assumed positive two-element form (any `s_L,s_C>0`), not from a computed junction field. **The circuit FORM is a disclosed modeling choice** — the prereg's "COMPUTED from 120° convergence + twist" promise was **not delivered**: `s_L=s_C=1` is assumed, the 120°/twist enter **no shipped equation** (only `z=3` does), and the **identical circuit follows for any 3-regular network**. X37's honest win over X36 is that the parasitic *magnitude* is not installed (it is swept and shown extent-dominated), not that the circuit *form* was derived from the vertex geometry.
- **C2 (R1 — scope the no-lift claim).** *Superseded:* §0 "**NOT** a parallel-bypass (it does **not** lift) … **refutes** any 'junction lifts the ceiling'." *Correction:* no lift **within the leading-order positive-element lumped class only**. A fuller vertex model (evanescent-mode stub / finite junction volume = a resonant shunt branch) is **not excluded** and could present a bypass. And `f_crit≈0.184` puts `ω_vertex` **inside** the band for `f>0.184`, where the quasi-static lumped separation self-invalidates — most of the 31.4 % swing accrues in that regime.
- **C3 (R3 — G-B fireability + instrument blindness, fixed in code `1186c891`).** *Superseded:* §0 "g_scalar recovers #604 exactly as f→0 (5.441398 ω_C, err **2e-16**)." That 2e-16 was float roundoff of π√3 computed two ways — the loaded solver hit an early-return and was never exercised. *Correction:* G-B now drives the loaded solver at f=1e-5 (full crossing scan) → π√3 within 1e-4. The topology detector now scans past π so a **lift is visible** (a planted negative-reactance loading reads `lift`); a resolution guard stops a small-f razor dip from silently reading as a lift.
- **C4 (R6 — the categorical premise was wrong).** *Superseded:* §0/§4 "**canon fixes no transverse bond scale**." *Correction:* canon **does** carry transverse scales — a **tube radius `ℓ_node/(2π)`** (constants.py:76, the electron loop) and a **core-tube thickness `d ≡ 1 ℓ_node`** (constants.py:189, the (2,3) trefoil) — but both are **soliton/core-sector** objects; adopting either for the bare vacuum bond would be a **sector-ownership crosswire**. Branch (iii) is therefore "not closable **without a sector-ownership ruling**," with the three candidate `f`-closures listed in §0/§4.
- **C5 (R4 — reciprocity identity).** The §4a "tracks the stronger channel" understates it: at `s_L=s_C=1` the shunt has **exactly zero** effect (combined = pure-throat to 8e-13).
- **C6 (R5 — bracket honesty).** The `g(0.5)=3.73` floor is **doubly conditional** (`f≤0.5` AND `s=1`); over `s∈[0.3,3]²`, `g(0.5)∈[2.13,4.74]`.
- **C7 (R9 — overstatement).** The derivation's "matches the exact solve to **<0.1 %** for a single channel" is corrected to **0.26 %** (measured at f=0.05; the citing test enforces 0.5 %). See the derivation doc's dated note.
- **Deviation ledger (R2):** every frozen-prereg deviation is named in the prereg's appended **Post-freeze deviation log** (1D two-node check now SHIPPED; 4-site BCC solve deviation-noted; the `s_L`-lifts expectation was sign-inverted; the §5 pure-shunt anchor coefficient `s_C`→`(2/3)s_C`; the derivation's pre-driver drop numbers ~18 %/~38 % vs shipped 16.4 %/31.4 %).

---

## 1. The lumped-equivalent vertex circuit (leading-order model — see C1)

| Quantity | Value | Provenance / status |
|---|---|---|
| shunt accumulator `C_j` | `s_C · ε₀ · d`, `d = f·ℓ_node` | assumed positive shunt element; the breathing mode couples here (symmetric-mode argument) |
| series throat `L_j` | `s_L · μ₀ · d` | assumed positive series element |
| shape factors `s_L, s_C` | O(1); **`= 1` assumed (equivalent-length normalization — a MODELING CHOICE, not computed; C1)** | a first-principles value needs a transverse bond field profile; canon's transverse scales are soliton-sector (§4, C4) |
| junction self-resonance | `ω_vertex = ω_C / (√(s_L s_C)·f)` | pure ratio; `= 2 ω_C` at f=0.5 |
| crossover (ω_vertex = π√3 ω_C) | `f_crit ≈ 0.184` (s=1) | below f_crit `ω_vertex` sits ABOVE the band (memoryless ~intact); above it `ω_vertex` is IN-BAND and the quasi-static lumped separation self-invalidates (C2) |
| topology class | reactive low-pass (**passivity result**, C1) | holds for any positive `s_L,s_C`; NOT a computed junction field; lift excluded only within this class (C2) |
| 1D two-node cross-check (prereg §3.4) | closed-form `cos(k a)`, `g_1d(f=0)=π`; both channels lower | SHIPPED (`band_top_1d`; was a frozen promise — R2) |

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

## 3. Driver-time finding (Rule 10) — the combined ceiling is NON-ADDITIVE; the shunt has ZERO effect at s=1

The exact solver surfaced a subtlety the O(f) linearization hides (derivation §4a): `κ = s_L + (2/3)s_C` is the correct LOCAL-μ slope and matches the exact solve to **0.26 % (measured at f=0.05; corrected from the earlier "<0.1 %" overstatement — R9)** for a **single** active channel, but the combined ceiling **tracks the stronger (throat) channel, not the sum** — because once `s_C>0` the loaded `μ(θ)` goes non-monotonic near the zone edge (dips below the adjacency floor at the throat-set first crossing, then recovers into the re-entrant sliver up to `μ(π) = −3 + s_L s_C f²π² > −3`). The accumulator's extra loading is absorbed into the re-entrant gap ABOVE the first crossing.

**Sharpened to an exact identity (R4):** at the reported normalization `s_L=s_C=1` the shunt accumulator has **EXACTLY ZERO effect** — the combined `g(f)` equals the pure-throat `g(f)` to **8e-13** on every f (`test_shunt_has_exactly_zero_effect_at_s_equal_1`). So the connected ceiling at s=1 is set by the throat **alone**; "both channels lower" is a per-channel statement, not additive at the ceiling.

## 4. Why BRANCH (iii): the closability finding (the honest core — restated per R6)

- **Canon-faithful limit `f → 0`:** 1D-line bonds ⇒ point junction ⇒ parasitic → 0 ⇒ memoryless π√3 ω_C exact. Not a rescue — what the canonical geometry literally implies.
- **Canon DOES carry transverse scales, but they are soliton/core-sector (R6 — the earlier "constants.py fixes NO transverse bond scale" was factually wrong; C4).** Specifically: a **tube radius `ℓ_node/(2π)`** (constants.py:76 — the electron minimal-energy loop) and a **core-tube thickness `d ≡ 1 ℓ_node`** (constants.py:189 — the (2,3) trefoil on the discrete grid). **Neither is the bare vacuum bond's transverse extent**; wiring a soliton core scale into the bare bond would be a **sector-ownership crosswire** (A1/Cosserat sector-ownership discipline). So the bare bond's extent `f` and the shape factors `s_L,s_C` remain **undetermined without a sector-ownership ruling**.
- The ceiling shift swings 31 % over the plausible `f∈[0,0.5]` ⇒ **extent-dominated ⇒ branch (iii): NOT closable without a sector-ownership ruling.** Three candidate closures for `f`: **(a)** the tube radius → `f = 1/(2π) ≈ 0.159` (notably right at `f_crit≈0.184`, where `ω_vertex ≈ π√3`); **(b)** the core-tube thickness → `f ≈ 1`; **(c)** neither applies to the bare bond (extent stays an import). The g-FORM and the passivity-class topology stand; the number does not.
- **This is why X36 (#613) had to install a scale** — canon underdetermines the *bare-bond* vertex reactance. X37 surfaces the underdetermination (and sharpens it to a 3-way sector-ownership question) instead of hiding it in an installed tank.

**Axiom-1 relationship (R7).** The memoryless `f→0` baseline treats the node as a **passive junction** (KCL, no stored energy). Axiom-1's reading of the node as an **intrinsic LC oscillator** (a node that carries its own reactive tank) is a **competing reading** of the same node. X37 takes **no position** between them — the X33 / #613 record governs that question; X37 only asks what a *finite-extent passive* junction does to the band.

**What would flip it to branch (i)** (surfaced pre-test-physics question, §2 prereg): if a sector-ownership ruling supplies a bare-bond transverse scale making `f ≲ 0.02`, the ceiling recovers π√3 within tolerance and the vertex clock = the walk clock (the X33 two-clock question closes in-engine). That is a Grant/corpus anchor, not a lane decision — flag-don't-fix.

## 5. Gate ledger (all PASS; every gate consumes a COMPUTED quantity with a firing tolerance — G-D)

| Gate | Condition (frozen) | Result | Planted-violation proof | Pass |
|---|---|---|---|---|
| **G-A anti-install** | extraction module references none of {OMEGA_C, M_E, L_CELL, C_CELL}, imports no `ave.core.constants`, AND carries no forbidden numeric LITERAL (AST scan — symbol + import + literal; R8) | name_hits `[]`, import_hits `[]`, literal_hits `[]` | `OMEGA_C` by SYMBOL and by NUMERIC LITERAL both FLAGGED (`test_gate_A_planted_violation_fires`, `test_gate_A_numeric_literal_scan_fires`); docstring mentions ignored. Disclosed limitation: arithmetic on allowed literals is not literal-caught (structural guarantee = the no-scale-import invariant) | ✅ |
| **G-B independent-reference recovery** | LOADED solver at small nonzero f (1e-5) converges to the FROZEN #604 top π√3 (hard-coded FROM `..._srs-band-survey_result.md:18`, cited; **the solver is exercised, not an early-return — R3/C3**) | g(1e-5) = 5.441344, rel err **1.0e-5 < 1e-4**; memoryless f=0 identity recorded separately | +1% offset loaded output → rel err ≥ 1e-4, gate FAILS (`test_gate_B_planted_violation_fires`) | ✅ |
| **G-C vertex-extent honesty** | extent derived + swept; branch by frozen rule | swing **31.4% > 10%** → branch **(iii)** | flat (control) ceiling NOT flagged; real f-dependent IS flagged (`test_gate_C_planted_detector_discriminates`) | ✅ |
| **G-D gates-can-fire** | every gate consumes a computed quantity with a failing tolerance | all three plants FIRE; no-op control does not | (the three above) | ✅ |

**24 tests pass** (`src/tests/test_x37_junction_parasitics.py`), incl. topology-class, monotonicity, single-channel-anchor, the reciprocity identity (R4), the lift-reachability + resolution-guard (R3), the 1D closed-form cross-check (R2), the shape-factor bracket (R5), the numeric-literal G-A scan (R8), junction-resonance-ratio, and the M6 FORM check (`g = O(1)` — no "ceiling near ω_C" credit).

## 6. Scope / what is deferred (honest tractability, prereg §8)

- **Phase 1 delivered:** the SCALAR/compression channel — full extraction, topology class, g_scalar, extent sweep, gates.
- **Vector/torsion channels SCOPED OUT** as the named follow-on. The vector vertex DOF is the **flywheel** (rotational inertia of the vertex plane) engaged by torsion; shear may largely bypass. That needs the 3-DOF (Cosserat) port scatter + the per-branch (longitudinal/transverse) network velocity gates — a full follow-on arc (matches the #604 §5 / srs-vector-survey deferral). Channel-anisotropic ceilings from ONE geometry would speak to the #607 lifted-vector question; not attempted here. An honest Phase-1-only result beats an overreached full one.
- **The shape factors `s_L, s_C`** are set to the equivalent-length normalization `= 1` (a MODELING CHOICE, C1); a first-principles value needs the transverse bond field profile, and canon's transverse scales are soliton-sector (the branch-(iii) sector-ownership obstruction, §4). Flagged, not fudged.
- **The circuit FORM itself** (positive shunt + positive series) is the leading-order Marcuvitz lumped equivalent, not a from-geometry derivation (C1); a fuller vertex model (evanescent-mode / finite-volume resonant branch) is the named model-fidelity follow-on that could reopen the lift question (C2).

## 7. Reproduce / outputs

```
make verify        # -> "[Verify] ALL PHYSICS PROTOCOLS PASSED."
PYTHONPATH=src python3 -m pytest src/tests/test_x37_junction_parasitics.py -q   # -> 24 passed
PYTHONPATH=src python3 src/scripts/vol_1_foundations/x37_junction_parasitics.py # -> ledger + JSON + WHITE figure
```

Driver ledger (stdout — current):
```
  #604 memoryless top   : 5.441398 omega_C (2.7805 MeV)  [research/2026-07-09_srs-band-survey_result.md:18]
  topology class        : reactive-low-pass (positive-element class: stored-energy channels pin the ceiling DOWN; zone-edge gap opens)
  vertex circuit @f*=0.5: L_j=0.500 mu_0 ell, C_j=0.500 eps_0 ell, omega_vertex=2.000 omega_C
  g_scalar(f=0)         : 5.441398 omega_C  (memoryless identity)
  g_scalar(f*=0.5)      : 3.730401 omega_C  (s=1)
  extent swing [0,0.5]  : 31.4% of pi*sqrt3
  BRANCH FIRED          : (iii)
  DISCLOSURES (adversarial review):
   R5 bracket g(0.5), s in [0.3,3]^2 : [2.129, 4.740] omega_C (DOUBLY conditional: f<=0.5 AND s=1)
   R4 reciprocity: max|combined - pure-throat| = 7.89e-13 (shunt has ZERO effect at s=1: True)
   R2 1D cross-check g_1d(f=0)=3.1416 (=pi), combined f=0.2 -> 2.4986, f=0.5 -> 1.7850
   R3 lift-detector self-test: passive=low-pass, planted-neg=lift (lift reachable: True)
  [PASS] G-A / G-A(sym+literal) / G-B(loaded) / G-B planted / G-C / G-C planted
```

## 8. Corpus-state consequences (for the auditor to land — lane discipline; NOT landed here)

Surfaced to the auditor's manuscript / COLLABORATION_NOTES queue (the manual entries are the auditor's to land):
1. **The srs vertex presents a REACTIVE LOW-PASS** for the scalar/compression channel (shunt accumulator + series throat). **This is a PASSIVITY result of the leading-order lumped (Marcuvitz) equivalent, not a from-geometry derivation** (C1): the circuit FORM is a disclosed modeling choice (`s_L=s_C=1` assumed; 120°/twist in no shipped equation, only `z=3`; identical for any 3-regular network). The "no lift" holds **within the positive-element lumped class only** (C2). What X37 genuinely delivers over X36: the parasitic *magnitude* is swept and shown extent-dominated, **not installed**.
2. **The junction clock's SCALE is not closable WITHOUT a sector-ownership ruling** (branch iii; R6/C4): canon's transverse scales — tube radius `ℓ_node/(2π)` (constants.py:76) and core-tube thickness `ℓ_node` (constants.py:189) — are **soliton/core-sector**, and adopting either for the bare bond is a crosswire. **Sharpened pre-test-physics question for Grant:** which (if any) sets the bare-bond extent `f` — (a) tube radius → f≈0.159, (b) core-tube thickness → f≈1, or (c) neither (extent stays an import)?
3. **X33 consumer:** the two-clock (walk-pins vs vertex-clock) fork is NOT settled by X37 — TYPED as extent-conditional. It closes to ONE clock iff the sector-ownership ruling gives `f ≲ 0.02`; otherwise the vertex clock is a genuine (extent-dominated) second scale. (Note: whether the node is a passive junction or an Axiom-1 intrinsic LC oscillator is a **competing reading** X37 does not adjudicate — §4, R7.)
4. **Methodological:** the anti-install gate (G-A — AST scan of the extraction path for forbidden SYMBOLS, imports, AND numeric LITERALS + planted-violation proofs; R8) is a reusable machine-check of the #613 lesson — candidate for the driver-honesty / substrate-native-check toolkit. Disclosed limit: arithmetic on allowed literals is not literal-caught (structural guarantee = the no-scale-import invariant + the dimensionless-cancellation proof).

**No leaf edit from this lane.** These are ledger rows + a Grant-anchor question, surfaced for the auditor.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
