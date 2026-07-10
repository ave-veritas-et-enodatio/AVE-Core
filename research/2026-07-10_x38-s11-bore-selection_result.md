# RESULT — X38: S₁₁-minimization bore selection — **TWO-AXIS: the frozen-primary Op6 objective is EXACTLY DEGENERATE (branch iv); the band-integrated comparator uniquely selects the POINT JUNCTION (branch ii)**

> **⚠ RESTATED 2026-07-10 after the PR #619 adversarial review (16 confirmed findings, 1 refuted; verdict = REPAIR-AND-BANK — branch (ii) survives on the broadband axis, but the demonstration was broken). See the Correction Log (§0a). This header + TL;DR are the corrected form; the superseded verbs ("all three objectives pick f*=0 → branch (ii)", "near-degenerate +2.7e-8", "the SAME operator that selected the trefoil", "NEW structural fact", "no bore can remove", the evanescent-stub escape) are quoted there. KEEP-BOTH.**

**Date:** 2026-07-10 · **Branch:** `analysis/x38-s11-bore-selection` (off main; merged current main incl. #616/#617 during the PR #619 repair) · **Task:** X38 (Grant-fired 2026-07-10, "fire x38 with the S11 route" — route d for the bond-bore fork X37/#616 sharpened)
**Prereg (FROZEN):** [`2026-07-10_x38-s11-bore-selection_prereg_FROZEN.md`](2026-07-10_x38-s11-bore-selection_prereg_FROZEN.md) — commit `cc386be1`, **committed 2026-07-10T14:46:25Z / pushed 14:46:55Z BEFORE any driver code** (freeze verifiable by commit ordering + `gh api`).
**Derivation:** [`2026-07-10_x38-s11-bore-selection_derivation.md`](2026-07-10_x38-s11-bore-selection_derivation.md)
**S₁₁ module:** `src/ave/core/junction_scattering.py` · **Driver:** `src/scripts/vol_1_foundations/x38_s11_bore_selection.py` · **Tests:** `src/tests/test_x38_s11_bore_selection.py`
**Data:** `src/scripts/vol_1_foundations/_output/x38_s11_bore_selection.json` · **Figure:** `..._output/x38_s11_bore_selection.png` (WHITE, house style)

**SECTOR HEADER.** MODE = linear small-signal (S-parameters). REGIME = cold, sub-yield, lossless (reactive-only). SECTOR = bare-bond network primitive (scalar/compression channel, Phase 1); soliton scales are frozen comparison marks only. Vector/torsion scoped out (§6).

**CLASS (consistency-vs-emergence).** **MIXED.** The selected `f*` is **derived-geometric** (the S₁₁ module imports NO physical scale — MU_0/EPSILON_0/ℓ_node cancel; the argmin is a pure number). The **SCALE** `ω_C = c/ℓ_node` is **dimensional-forced / identity** and appears only as the reporting unit. The deliverable is which branch fired + the objective spread; no emergent-scale headline (the branch is `f* = 0`).

---

## 0. TL;DR — the verdict (RESTATED, two-axis)

Applying canon's OWN geometry-selection operator — **Universal Operator #6**, `λ_min(S†S) → 0` ([`eigenvalue-target.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/eigenvalue-target.md) `clm-gdd70j`), **applied at the vertex as a CANDIDATE selector** (per canon's OWN honest-scope note it did NOT select the trefoil `R·r` — C6/R6) — the verdict is **TWO-AXIS**: **the frozen-PRIMARY single-frequency Op6 objective is EXACTLY DEGENERATE (branch iv); ONLY the band-integrated comparator uniquely selects `f* = 0`, the POINT JUNCTION (branch ii).**

- **THE LOAD-BEARING CORRECTION (C1/R1).** Symbolically (sympy, perfect-square numerator): `|S₁₁(π;f)|² − 1/9 = 8t²(s_C·s_L²·t² + s_C − 3s_L)² / [...]`, `t = fπ`. So obj-1 `|S₁₁(π)|²` touches the `1/9` floor **EXACTLY** (machine zero, `−4.2e-17`) — not only at `θ→0` but at the finite **half-wave-invisible** extent `f_touch = √(3s_L−s_C)/(π√s_C·s_L)` (= `√2/π ≈ 0.450` at `s=1`), where the junction section is half-wave at the band-top tone and thus impedance-transparent there. **obj-1 has co-equal global minima `{0, f_touch}` → it is EXACTLY DEGENERATE; under the FROZEN branch rule (degenerate clause) the PRIMARY objective fires BRANCH (iv), not (ii).** obj-3 (single-freq at `π/2`) shares this structure (touch at `2·f_touch = 0.900`, out of `[0,0.5]` at `s=1`). **ONLY obj-2 (band-integrated) uniquely selects `f* = 0`** — the half-wave trick is single-tone; broadband matching cannot use it. The physical reading: **a half-wave-invisible bore family** exists on the single-frequency axes, but the broadband vertex still prefers no bore.
- **BARE-JUNCTION MISMATCH VERIFIED.** A wave down one srs bond sees the other two in parallel (`Z₀/2`), so `Γ = S₁₁ = (2−z)/z = −1/3` for `z=3`: the memoryless junction reactively back-scatters `|Γ|² = 1/9` of the power and is **NOT matched**. Recovered analytically AND through the LOADED S₁₁ path (`f→0`) to `0.0e+00` rel error.
- **THE L-MATCH: CONFIRMED AS A NETWORK FACT, REFUTED AT THE LOSSLESS-RECIPROCAL VERTEX.** `Q = √(2−1) = 1`; the ideal 2-element L-match nulls `|S₁₁|→0` — verified. But the substrate's parasitic geometry is the OPPOSITE (step-DOWN) orientation (accumulator/shunt-C at the low-Z node; throat in the arms), and C₃ᵥ forbids a privileged one-arm shunt — so `|S₁₁| ≥ 1/3` for all θ, f, `s>0` (proven).
- **THE 1/3 FLOOR = THE CLASSIC THREE-PORT THEOREM (C5/R5), scoped to the LOSSLESS RECIPROCAL class (C3/R3).** `min_θ |S₁₁|² = 1/9` for **ALL** `f` — the classic matched-lossless-reciprocal-3-port theorem (Pozar §7.1 class; `|S₁₁| ≥ 1/3` symmetric corollary), **confirmed at the vertex** (provable, not numerical). The Op6 reflectionless target is UNREACHABLE **by any bore of the lossless-reciprocal class** — an intrinsic `z=3` reactive back-scatter/redistribution (no dissipation). **NON-RECIPROCAL escape (C4/R4):** matched lossless C₃-symmetric 3-ports DO exist (the ideal circulator: unitary, `S₁₁=0`, non-reciprocal). Any lossless+reciprocal+C₃ network — incl. the evanescent-stub model named earlier — obeys the theorem, so **that escape is DEAD; the ONLY escape class is non-reciprocity**, which needs a T-breaking bias (candidate: frozen-bias sector `u₀*/Ω_freeze`) — **PENDING-GRANT**, asserted nowhere.
- **BRANCH (i) UNADJUDICATED on the degenerate locus (C2/R2).** At swept cell `(s_L,s_C)=(2,3)`, `f_touch = 1/(2π)` **EXACTLY**, INSIDE `f_crit ≈ 0.184` — an exact obj-1 co-minimum ON the tube-radius (branch-i) mark in the self-consistent regime. This is a formula locus (s-cell-dependent), **NOT asserted as branch (i)** and **NOT dismissed** — **PENDING-GRANT**.
- **⇒ TWO-AXIS BANKED:** `f* = 0` is uniquely selected **only on the broadband (obj-2) axis** → branch (ii) there; the frozen-primary single-frequency objectives are exactly degenerate → branch (iv). The X37 bond-bore fork is dissolved on the broadband axis (the operator wants no bore; the walk ceiling `π√3` is the obj-2-selected ceiling) — **demonstrated (entailed by the model class), not adjudicated** (R7).
- **All six gates PASS, each with a planted-violation proof (G-D); the G-B gate now has an f-sensitive leg + a parasitics-disabled sabotage proof (R8); the objective code IMPORTS the canonical X37 routine (R10).** 26 tests pass; `make verify` green.

---

## 0a. Correction Log (2026-07-10, PR #619 adversarial review — KEEP-BOTH, superseded text quoted)

The review returned 16 confirmed findings (1 refuted); verdict REPAIR-AND-BANK. Nothing is silently erased. Code+gates+import repair + this restatement land on the same branch.

- **C1 (R1, load-bearing — TWO-AXIS RESTATEMENT).** *Superseded:* §0 "**All three frozen objectives pick `f* = 0` → BRANCH (ii)**" and §3 "obj-1/2/3 all give `f* = 0`, spread 0". *Correction:* obj-1 `|S₁₁(π;f)|² − 1/9` is a PERFECT SQUARE `8t²(s_C s_L² t² + s_C − 3s_L)²/[...]`; it touches `1/9` EXACTLY at `f_touch(π) = √(3s_L−s_C)/(π√s_C s_L)` (= `√2/π` at s=1, obj-1@touch − 1/9 = `−4.2e-17`). obj-1 is thus EXACTLY DEGENERATE `{0, f_touch}` and (frozen degenerate clause) the PRIMARY fires **branch (iv)**; obj-3 co-degenerate at `2·f_touch`; **ONLY obj-2 uniquely selects `f*=0` (branch ii)**. The earlier grid-argmin "f*=0 for obj-1" was resolution luck (the touch at 0.450158 fell between 501-grid points).
- **C1b (R1 — D3 mischaracterization).** *Superseded:* §3 "obj-1 has a **near-degenerate** interior local min at `f≈0.45` (+2.7e-8 above the floor)". *Correction:* it is an **EXACT** touch (machine zero at `f_touch = √2/π`), i.e. a genuine second global minimum, not a near-miss. The `+2.7e-8` was the nearest 501-grid sample, not the touch.
- **C2 (R2 — the (2,3) co-minimum on the branch-i mark).** *Superseded:* §0/§3 "`f* = 0` matches NEITHER soliton mark → **branch (i) does NOT fire**". *Correction:* at cell `(2,3)`, `f_touch = 1/(2π)` EXACTLY, INSIDE `f_crit` — an exact obj-1 co-minimum ON the tube-radius mark in the self-consistent regime. Branch (i) is **UNADJUDICATED PENDING-GRANT** on this degenerate locus (a formula locus, not romanced, not asserted).
- **C3 (R3 — reciprocity scope + circulator).** Every "no bore matches" / "1/3 floor" / "unreachable" claim is scoped to the **LOSSLESS RECIPROCAL** vertex class. Matched lossless C₃ 3-ports exist non-reciprocally (circulator witness). The lattice is chiral at Axiom-1 (right-handed I4₁32, `axiom-definitions.md:16`) — parity broken — but circulation needs a T-breaking bias (candidate `u₀*/Ω_freeze`): PENDING-GRANT.
- **C4 (R4 — the evanescent-stub escape is DEAD).** *Superseded:* §6 "a fuller vertex model (evanescent-mode stub / finite-volume resonant branch) … could present a matching notch". *Correction:* any lossless+reciprocal+C₃ network obeys the theorem; the ONLY escape class is **non-reciprocity**. **Cross-flag HANDLED:** X37's merged Correction-Log C2 named the same now-dead stub escape — the correction landed as **[PR #620](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/620)** ("fix(x37): C2 escape clause correction — reciprocal vertex class is theorem-bound"), now in Grant's pending-orchestrator queue. Cited, not re-flagged; X37's merged docs are NOT edited from this lane.
- **C5 (R5 — attribution).** *Superseded:* §8 "**NEW structural fact**: the `z=3` vertex is an intrinsic `1/9`-power back-scatterer". *Correction:* the classic matched-lossless-reciprocal-3-port theorem (Pozar §7.1 class; `|S₁₁| ≥ 1/3` symmetric corollary), **confirmed at the vertex** — provable, which STRENGTHENS the bound.
- **C6 (R6 — Op6 legitimacy).** *Superseded:* everywhere "the SAME operator that **selected** the trefoil `R·r = 1/4`". *Correction:* per canon's OWN honest-scope note (`constants.py`, HONEST SCOPE 2026-06-14) the S₁₁ landscape is FLAT in `R·r` and "S₁₁ minimization does NOT select `R·r = 1/4`". Op6 is here a **candidate selector applied at the vertex**; it did not select the trefoil geometry. (This premise entered via the orchestrator brief.)
- **C7 (R7 — entailment framing).** "the substrate decides / adjudicates" → **"demonstrated / entailed by the model class"** (third instance of the #613 MAJOR-11 pattern).
- **C8 (R8 — gates).** G-B given an f-SENSITIVE active leg (`|S₁₁(π,0.2)| > 1/3`; `g(0.2) < π√3`) + a PARASITICS-DISABLED sabotage proof (the old `f→0`-only probe was f-insensitive by the deepest-notch result and passed the sabotage spuriously). D4 recharacterized: the ~6e-10 obj-2 non-monotonicity was an integration-cutoff systematic (`θ_top`-shrink + `1e-6` lower bound), now FIXED by integrating from `θ=0` exactly.
- **C9 (R9 — vocabulary).** "per-vertex reflection **LOSS**" → "reactive **back-scatter / redistribution**" (Ax3 lossless: no dissipation).
- **C10 (R10 — canonical import).** #616 is merged; the ported loaded-μ code is REPLACED by an IMPORT of the canonical `junction_parasitics.connected_band_top_theta` / `g_scalar`.
- **REFUTED (1):** the one finding the review itself did not sustain is recorded as such by the reviewer; no doc change.

---

## 1. What the substrate says (the honest core)

X37 sharpened the fork: is the bare-bond junction extent `f` (a) the tube radius `1/2π ≈ 0.159`, (b) the core-tube thickness `1`, or (c) neither (extent an import)? Adopting a soliton scale was a sector-ownership crosswire; X37 could not close it without a ruling. **X38 asks the substrate directly, using canon's own selection operator as a CANDIDATE selector (per canon it did not select the trefoil — R6).** The answer is TWO-AXIS: **on the broadband (band-integrated) axis the operator selects `f = 0`** (the bore is a non-object — any positive bore raises the band-averaged reflection); **but the frozen-primary single-frequency Op6 objective is EXACTLY DEGENERATE** `{0, f_touch = √2/π}` — a half-wave-invisible bore family. So "the operator wants no bore" is true only under a broadband reading; single-frequency matching admits the transparent-at-one-tone bore. *[Superseded (R1): "the operator selects `f = 0` … it is a non-object … closure (c), reached constructively" — corrected to the two-axis form above.]*

**Why (the plumber picture).** In a real 3-way tee a surge partially reflects off the branch (the two other pipes = a lower combined impedance, `Z₀/2`). Rounding the tee — adding the accumulator volume + the throat — is on the WRONG side to cancel that (step-DOWN orientation; and C₃ᵥ forbids a privileged-arm shunt), so the broadband reflection only rises: the sharpest tee reflects least on average. The one exception is the **half-wave-invisible** section: a bore that is exactly half-wave at the probe tone is transparent AT that tone (this is the obj-1/obj-3 degeneracy at `f_touch`) — but that trick works at a single frequency only. The reflection you cannot remove without breaking reciprocity — the `1/9`-power reactive back-scatter (R9: no dissipation) — is the classic three-port theorem (Pozar §7.1; R5), the structural price of `z = 3` branching in a **lossless reciprocal** vertex (R3; a non-reciprocal circulator vertex WOULD match — R4, PENDING-GRANT).

---

## 2. Bare-junction Γ = −1/3 + the L-match confirmation/refutation (frozen expectations, §5 prereg)

| Frozen analytic expectation (M6) | Verdict | Evidence |
|---|---|---|
| **BARE MISMATCH** `S₁₁(f=0) = (2−z)/z = −1/3` (`z=3`), memoryless NOT matched | **CONFIRMED** | analytic `bare_junction_s11(3) = −0.3333…`; loaded S₁₁ `f→0` recovers `|S₁₁| = 1/3` to `0.0e+00` (G-B) |
| **L-MATCH** `Q = √(Z_hi/Z_lo − 1) = 1`; ideal 2-element network nulls `|S₁₁|→0` | **CONFIRMED as a network fact** | `test_l_match_ideal_null_is_reachable_Q_equals_one` — the correct-orientation L (series toward the `Z₀/2` load + shunt on the HIGH/source side) nulls to `< 1e-9` |
| **L-MATCH at the physical vertex** — does `|S₁₁|` dip below `1/3`? | **REFUTED (`|S₁₁| ≥ 1/3`)** | orientation (accumulator on low-Z node) + C₃ᵥ (no privileged one-arm shunt) ⇒ `|S₁₁| ≥ 1/3` for all θ,f,s (lossless reciprocal); equality on the half-wave-invisible locus — see R1 |

**The exact identity (R1) is the analytic backbone:** sympy gives `|S₁₁(θ;f)|² − 1/9 = 8t²(s_C s_L² t² + s_C − 3s_L)²/[...]`, `t=fθ` — a PERFECT SQUARE ⇒ `|S₁₁| ≥ 1/3` **always**, with equality at `θ=0` AND on the half-wave-invisible locus `t² = (3s_L−s_C)/(s_C s_L²)`. *[Superseded: "`|S₁₁| > 1/3` everywhere except the trivial DC point" — the small-θ expansion `|S₁₁|²=(¼+b²)/(9/4+b²)`, `b=[(3/2)s_L−(¼)s_C]fθ` is valid only near `θ→0` and misses the second (θ=π) touch; corrected by the exact identity above.]* So the L-match dip below `1/3` is REFUTED (the bore never beats the bare floor), but the floor is TOUCHED (not merely approached) at `f_touch` — the source of the obj-1/obj-3 degeneracy (§3).

---

## 3. f* under each objective + the s-sweep + which branch fired (G-C first-class)

`f* = argmin_{f∈[0,0.5]}` (dense boundary-inclusive grid; `f=0` is a candidate — no dead-actuator):

| Objective (prereg §4) | in-domain `f*` (s=1) | EXACT structure | axis verdict |
|---|---|---|---|
| **obj-1 (canonical Op6, PRIMARY)** `\|S₁₁(π;f)\|²` via `universal_eigenvalue_target` | grid→`0` (resolution luck) | co-equal minima `{0, f_touch=√2/π≈0.450}`, `−4.2e-17` at touch | **EXACTLY DEGENERATE → branch (iv)** |
| **obj-2 (band-integrated, comparator)** `⟨\|S₁₁\|²⟩` over connected band | **`0.0000`** (unique) | `>1/9` for every `f>0` (half-wave trick washed out) | **UNIQUE `f*=0` → branch (ii)** |
| **obj-3 (single-freq, comparator)** `\|S₁₁(π/2;f)\|²` | `0` (in-domain) | co-min at `2·f_touch=0.900` (OUT of `[0,0.5]` at s=1) | degeneracy structure, out-of-domain at s=1 |

**s-sweep** `s_L,s_C ∈ {0.3,0.5,1,2,3}²` (X37 R5 lesson): **obj-2 uniquely selects `f*=0` at EVERY cell** (the load-bearing broadband axis). obj-1 is EXACTLY DEGENERATE wherever `f_touch(π) ∈ (0,0.5]`. **Branch-(i) PENDING-GRANT locus (R2):** cell `(s_L,s_C)=(2,3)` puts `f_touch = 1/(2π)` EXACTLY, INSIDE `f_crit` — an exact obj-1 co-minimum ON the tube-radius mark in the self-consistent regime.

**Which branch fired — TWO-AXIS (R1).** The frozen-PRIMARY single-frequency objective (obj-1) is exactly degenerate ⇒ **branch (iv)**; the band-integrated comparator (obj-2) uniquely selects `f*=0` ⇒ **branch (ii)** on the broadband axis. **BANKED:** `f*=0` is real but selected ONLY on the broadband axis; the single-frequency objectives admit the **half-wave-invisible bore family** `{0, f_touch}`. Demonstrated (entailed by the model class), not adjudicated (R7). Branch (i) UNADJUDICATED PENDING-GRANT on the `(2,3)` locus (R2).

**EXACT-degeneracy disclosure (R1; visible in the figure Panel B — the blue obj-1 curve dives back to the `1/9` floor at `f_touch`).** obj-1 `|S₁₁(π;f)|²` touches `1/9` **EXACTLY** (machine zero `−4.2e-17`) at the half-wave-invisible extent `f_touch = √2/π` — a genuine second global minimum (NOT the "+2.7e-8 near-degenerate dip" first shipped; that was the nearest 501-grid sample). At `s=1` it sits at `f_touch > f_crit` (self-invalidated regime); at cell `(2,3)` it sits INSIDE `f_crit` on the tube-radius mark.

---

## 4. Gate ledger (all PASS; each consumes a COMPUTED quantity with a firing tolerance — G-D)

| Gate | Condition | Result | Planted-violation proof | Pass |
|---|---|---|---|---|
| **G-A anti-install** | S₁₁ module references none of `{OMEGA_C,M_E,L_CELL,C_CELL}`, imports no `ave.core.constants`, no forbidden numeric LITERAL (AST scan; X37 R8) | name/import/literal hits `[]` (the `junction_parasitics` import is module `ave.core`, not `ave.core.constants` — clean) | `OMEGA_C` by SYMBOL and by LITERAL both FLAGGED (`test_gate_A_planted_symbol_and_literal_both_fire`) | ✅ |
| **G-B recovery + f-sensitive legs (R8)** | memoryless legs recover bare `\|S₁₁\|=1/3` AND `π√3` (via CANONICAL `jp.g_scalar`, #616/R10); **ACTIVE legs** confirm the parasitics bite (`\|S₁₁(π,0.2)\| > 1/3`; `g(0.2) < π√3`) | bare rel `0e0`, ceiling rel `1e-5`; both active legs `True` | (a) +1% offset FAILS the reference tol; (b) a PARASITICS-DISABLED sabotage FAILS the active legs (`test_gate_B_planted_offset_and_sabotage_fire`) — the sabotage the old `f→0`-only gate passed spuriously | ✅ |
| **G-C two-axis (R1)** | per-objective EXACT degeneracy + spread; two-axis branch assignment | obj-1 degenerate → primary **(iv)**; obj-2 unique → **(ii)** | (a) degeneracy detector: obj-1 touches `1/9` at `f_touch`, obj-2 does not; (b) divergent bogus objective fires the scatter detector; control does not (`test_gate_C_planted_degeneracy_and_scatter_detectors_fire`) | ✅ |
| **G-D gates-can-fire** | every gate consumes a computed quantity with a failing tolerance | all plants FIRE; controls do not | (the three above) | ✅ |

**26 tests pass** (`src/tests/test_x38_s11_bore_selection.py`), incl. the bare Γ=−1/3 + general `(2−z)/z`, the canonical-operator equality, the perfect-square exact touch (`obj-1@f_touch − 1/9 = 0` to `1e-12`), obj-1-degenerate/obj-2-unique, the `(2,3)`→`1/(2π)` locus, the circulator escape (unitary/`S₁₁=0`/non-reciprocal/C₃), the Pozar `|S₁₁|≥1/3` theorem, the D4 no-cutoff-systematic, the canonical `jp.g_scalar` recovery, and the four gates + planted proofs (incl. the G-B sabotage).

---

## 5. Post-freeze deviation log (named, none silent — X37 R2 discipline) — RESTATED per PR #619

- **D1/D2 (SUPERSEDED by the merge — R10).** *Originally shipped:* "X37's `junction_parasitics.py` is UNMERGED on main, so it cannot be imported; the `π√3` recovery + G-A scan are PORTED with citation." *Now (PR #619 repair):* **#616 is MERGED**; the branch merged current `origin/main`, and the loaded-μ ceiling is recovered via an IMPORT of the CANONICAL `junction_parasitics.g_scalar` / `connected_band_top_theta` (R10). The G-A scanner logic is kept inline in the driver (the X37 driver is a `src/scripts` script, not a package) with provenance to X37 R8.
- **D3 (RECHARACTERIZED — R1).** *Originally shipped:* "obj-1 near-degenerate interior dip at `f≈0.45`, `+2.7e-8` above the floor, does not beat f=0." *Correction:* it is an **EXACT** touch (machine zero at `f_touch = √2/π`) — a genuine second global minimum ⇒ obj-1 EXACTLY DEGENERATE ⇒ frozen-primary branch (iv). The `+2.7e-8` was the nearest 501-grid sample.
- **D4 (RECHARACTERIZED + FIXED — R8).** *Originally shipped:* "s-sweep worst-case `f*=0.010` is a float-tie on obj-2's flat plateau." *Correction:* it was a genuine **integration-cutoff systematic** (obj-2's `θ_top`-shrink + the `1e-6` lower bound), NOT a float tie. **FIXED** by integrating obj-2 from `θ=0` exactly ⇒ obj-2 now uniquely selects `f*=0` at every cell with no interior artifact.

---

## 6. Scope / what is deferred (honest tractability, prereg §8)

- **Phase 1 delivered:** the SCALAR/compression channel S₁₁ — the exact symmetric 3-port reflection, the canonical Op6 candidate-selector (two-axis), the L-match refutation, the objective-degeneracy analysis, the s-sweep, the gates.
- **The result is scoped to the LOSSLESS RECIPROCAL class (R3).** *Superseded:* "a fuller vertex model (evanescent-mode stub) could present a matching notch." **Correction (R4):** any lossless+reciprocal+C₃ network obeys the `|S₁₁|≥1/3` theorem — the evanescent-stub escape is DEAD. **The ONLY escape class is non-reciprocity** (circulator-like), which needs a T-breaking bias (candidate frozen-bias sector `u₀*/Ω_freeze`) — PENDING-GRANT, the named follow-on.
- **Vector/torsion channels SCOPED OUT** (vertex flywheel; shear) — matches #604 §5 / X37.
- **The shape factors `s_L,s_C`** are the equivalent-length normalization `=1` with the `[0.3,3]²` sweep as the honesty check.

## 7. Reproduce / outputs

```
make verify        # -> "[Verify] ALL PHYSICS PROTOCOLS PASSED."
PYTHONPATH=src python3 -m pytest src/tests/test_x38_s11_bore_selection.py -q   # -> 26 passed
PYTHONPATH=src python3 src/scripts/vol_1_foundations/x38_s11_bore_selection.py # -> ledger + JSON + WHITE figure
```

Driver ledger (stdout — current, PR #619 repair):
```
  objective (canon)     : Op6 lambda_min(S†S)->0 [candidate selector; NOT the trefoil selector, R6]
  bare junction z=3     : S11 = -0.3333  (|S11|=1/3; memoryless NOT matched)
  L-match Q (2:1)       : 1.000  -> ideal null reachable; REFUTED at lossless-recip vertex
  1/3 floor (R5)        : classic matched-lossless-RECIPROCAL-3-port theorem (Pozar §7.1), confirmed
  non-recip escape (R3) : circulator S11=0 (unitary, C3, NON-recip) -> T-break PENDING-GRANT
  TWO-AXIS VERDICT (R1):
    obj-1 (primary, pi)  : EXACTLY degenerate {0, f_touch=0.4502} (obj1@touch-1/9=-4.2e-17) -> frozen BRANCH (iv)
    obj-3 (pi/2)         : f_touch=0.900 OUT of [0,0.5] at s=1
    obj-2 (band-integ.)  : uniquely f*=0.000 -> BRANCH (ii)
    BANKED               : f*=0 selected ONLY on the broadband axis; single-freq objectives degenerate
  s-sweep [0.3,3]^2     : obj-2 uniquely f*=0 all cells = True; branch-(i) PENDING-GRANT loci: [(2.0, 3.0)]
  G-B (R8)              : mem bare|S11|=0.3333 rel 0e+00, ceiling=5.4413 rel 1e-05; f-sensitive legs bare=True/ceiling=True
  [PASS] G-A / G-A planted / G-B / G-B planted / G-C / G-C planted
```

## 8. Corpus-state consequences (for the auditor to land — lane discipline; NOT landed here) — RESTATED per PR #619

Surfaced to the auditor's manuscript / COLLABORATION_NOTES queue (the manual entries are the auditor's to land):
1. **The X37 bond-bore fork is dissolved ON THE BROADBAND AXIS (route d):** the band-integrated Op6 comparator uniquely selects `f* = 0` (point junction) at every `(s_L,s_C)∈[0.3,3]²`, so the X37 walk ceiling `π√3 ω_C` (g(0)) is the broadband-selected ceiling. **BUT the frozen-primary single-frequency Op6 objective is EXACTLY DEGENERATE** `{0, f_touch=√2/π}` (branch iv) — a **half-wave-invisible bore family**. So the substrate's own operator does not UNIQUELY reject a bore; it does so only under a broadband reading. Op6 is a **candidate selector applied at the vertex — NOT "the operator that selected the trefoil"** (per canon's own honest-scope note, S₁₁-min is FLAT in R·r; C6/R6). "Demonstrated (entailed by the model class), not adjudicated" (R7).
2. **The 1/3 floor = the classic three-port theorem, confirmed at the vertex (C5/R5), scoped to the LOSSLESS RECIPROCAL class (C3/R3).** `|S₁₁| ≥ 1/3` for the symmetric lossless reciprocal 3-port (Pozar §7.1 class) — a reactive back-scatter/redistribution (R9: no dissipation), not a "loss". **Grant question (ontology + the non-reciprocal escape, C4/R4):** matched lossless C₃ 3-ports EXIST but ONLY non-reciprocally (circulator witness). The lattice is chiral at Axiom-1 (I4₁32) — parity broken — but a matched vertex needs a **TIME-REVERSAL-breaking bias** (candidate: frozen-bias sector `u₀*/Ω_freeze`). Is that T-breaker physically present at the vacuum vertex (giving a circulator-like matched, chirality-sorting junction), or is the vertex a genuine reciprocal `1/9` back-scatterer? PENDING-GRANT.
3. **Branch (i) UNADJUDICATED on a degenerate locus (C2/R2):** at swept cell `(s_L,s_C)=(2,3)`, the exact obj-1 co-minimum `f_touch = 1/(2π)` lands ON the tube-radius (branch-i) mark INSIDE `f_crit`. A formula locus, surfaced for Grant — neither asserted nor dismissed.
4. **X37-C2 cross-flag HANDLED (C4/R4):** X37's merged Correction-Log C2 named the same now-dead evanescent-stub escape (any lossless+reciprocal+C₃ network obeys the theorem). The correction landed as **[PR #620](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/620)** (in Grant's pending-orchestrator queue) — cited, not re-flagged.
5. **Methodological:** the canonical-operator-as-CANDIDATE-selector pattern + the two-axis objective detector (single-freq degeneracy vs broadband uniqueness) + the G-B f-sensitivity/sabotage leg are reusable driver-honesty checks.

**No leaf edit from this lane.** These are ledger rows + Grant-anchor questions (the X37-C2 correction is landed as PR #620), surfaced for the auditor.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
