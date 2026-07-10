# PREREG (FROZEN) — X38: S₁₁-minimization bore selection (does the substrate SELECT the bond's junction extent f?)

**Date:** 2026-07-10 · **Branch:** `analysis/x38-s11-bore-selection` (off main @ 85f8b3d5, includes merged #615) · **Task:** X38 (Grant-fired 2026-07-10, "fire x38 with the S11 route") — the resolution route for the bond-bore fork X37 (#616, repaired) sharpened.
**Consumes (frozen references):**
- [`research/2026-07-10_x37-junction-parasitics_result.md`](2026-07-10_x37-junction-parasitics_result.md) — X37 (PR #616, repaired): the srs vertex as a leading-order lumped TL discontinuity (shunt accumulator `C_j = s_C·ε₀·d`, series throat `L_j = s_L·μ₀·d`, extent `d = f·ℓ_node`), giving a REACTIVE LOW-PASS ceiling `g(f)·ω_C` with `g(0) = π√3`, EXTENT-DOMINATED. **Its module `src/ave/core/junction_parasitics.py` is the substrate; its `scan_forbidden_inputs` / `_FORBIDDEN_MAGNITUDES` (driver) are reused for G-A.**
- [`research/2026-07-09_srs-band-survey_result.md:18`](2026-07-09_srs-band-survey_result.md) — merged **#604**: scalar band top **π√3 ω_C = 5.4414 ω_C** at H, closed form `π / ANALYTIC_NETWORK_FACTOR`. **This is the G-B independent-reference number.**
- [`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/eigenvalue-target.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/eigenvalue-target.md) (claim `clm-gdd70j`) — **Universal Operator #6**, `λ_min(S†S) → 0` (the ground state = the config where one mode is perfectly absorbed / reflectionless). Code path `universal_operators.universal_eigenvalue_target(S)` (`src/ave/core/universal_operators.py:322`). **This is the canonical objective functional (obj-1) — NOT invented here.**
- [`manuscript/ave-kb/common/operators.md`](../manuscript/ave-kb/common/operators.md) §2 (Op6 row, line 46, CANONICAL) + `src/ave/core/constants.py:191-206` — how the trefoil derivation APPLIED Op6: S₁₁ minimization enforced `R − r = 1/2` and `R · r = 1/4` (Golden Torus / α chain). X38 applies the SAME operator at the vertex.

**Supersedes the approach of:** X36 / PR #613 (BLOCKED for INSTALLING a lumped vertex tank). X38 does not install a scale, nor adopt a soliton scale for the bare bond; it asks whether canon's OWN geometry-selection operator (Op6) selects `f` from `{L′, C′, z, θ, f, s_L, s_C}` alone.

**Class (consistency-vs-emergence):** **MIXED — declared per component.** The **selected `f*` (and its s-dependence) is DERIVED-GEOMETRIC** (a pure-number argmin of a dimensionless reflection functional; `MU_0/EPSILON_0/ℓ_node` cancel from every product — §3.3; no CODATA, no α, no `M_E`). The **SCALE** `ω_C = c/ℓ_node` (and the MeV of any reported ceiling) is **dimensional-forced / identity-class** (`ℓ_node ≡ ℏ/(m_e c)`) and appears **only in REPORTING**. "Ceiling near ω_C" is dimensionally forced → **NO credit** (M6). Which branch fires is the deliverable; if `f* = 0` fires, the honest headline is "the point junction is Op6-optimal," not a new emergent scale.

---

## §0. SKILL-SELECTION PLAN (60-second, per pre-workstream planning discipline)

Applied set, declared before any code (retro-checked before each commit):

| Skill | Where it fires | What it guards |
|---|---|---|
| **ave-prereg** | this doc | freeze-before-driver (commit-ordering proof, the #613/X37 lesson); no post-hoc axis drop |
| **ave-canonical-leaf-pull** | §4 | pull Op6 `λ_min(S†S)→0` (eigenvalue-target.md) + the trefoil `R·r=1/4` application (constants.py:191-206) BEFORE deriving; use ITS functional form, don't invent |
| **ave-canonical-source** | §3 inputs | every geometric input by SYMBOL; the reference π√3 hard-coded FROM #604:18 (cited), not self-recomputed |
| **substrate-native-check** | §1 | K4/srs TL scatter; S₁₁ = a reflection at an impedance boundary (Op3/Op6), the EE-native way; NOT Lagrangian/Helmholtz/energy-basin |
| **ave-ee-first-mapping (trigger 2, new-derivation)** | whole doc | S-matrix / L-match / reflection-minimization IS the substrate-native language |
| **phase-space-coordinate-check (A46)** | §1 | the observable (a reflection coefficient in the impedance plane) and the objective (Op6 on that reflection) are BOTH in the same S/impedance coordinates — matching |
| **consistency-vs-emergence** | header, §4 | f* selection = derived-geometric; SCALE = dimensional-forced/identity; tag each verdict |
| **ave-driver-script-honesty** | §6, driver | gates consume COMPUTED quantities; planted-violation proofs; no dead-actuator |
| **ave-evidence-framing-discipline** | §5, §7 | "ceiling near ω_C" gets no credit; deliverable = which branch + the objective spread |

Retro-pass rule: if the applied set drifts during implementation, note it in the result doc before the commit that drifts.

---

## §0.5 SECTOR HEADER (mandatory, before any standard-physics word)

- **MODE:** linear small-signal (S-parameters of the cold, linear vertex).
- **REGIME:** cold, sub-yield, lossless (A ≪ 1; Op14 saturation OFF; reactive-only — the parasitics store energy, none dissipates).
- **SECTOR:** **bare-bond network primitive.** The object is the vacuum bond's own 3-way vertex (scalar / compression channel, Phase 1), NOT a soliton or core. The soliton transverse scales (tube radius `ℓ_node/2π`, core-tube thickness `1·ℓ_node`) appear ONLY as **frozen comparison marks** (§5), never as inputs.
- **Which sector owns the DOF:** compression = A1 dilatation on the bond TLs; the vertex reflection is a reactance-boundary property of THAT channel, not a charge/spin (Cosserat-winding) object. No sector cross-wiring; adopting a soliton scale for the bare bond would BE a crosswire (X37 R6/C4), which is exactly the fork X38 tries to dissolve by asking the substrate.

---

## §1. substrate-native-check (done BEFORE any numerical code, per Operating Principle 1)

- **Dynamics:** K4/srs distributed **transmission-line network**. Bonds are TLs (`L′ = μ₀`, `C′ = ε₀` ⇒ `c = 1/√(L′C′)`, `Z₀ = √(L′/C′)`). The vertex is a **TL discontinuity**; its **reflection coefficient S₁₁** (a wave down one bond, the other two bonds match-terminated as semi-infinite lines) is the substrate-native observable. NOT a Lagrangian, NOT gradient-descent, NOT continuum-Helmholtz, NOT an energy-basin.
- **The selection operator is CANON's, not invented:** Universal Operator #6, `λ_min(S†S) → 0` (eigenvalue-target.md), the SAME operator that selected the trefoil `R−r=1/2`, `R·r=1/4` (constants.py:191-206). X38 applies it AT THE VERTEX. The physical WHY (fast-sector-settling): a lossless medium's fast channels settle toward the reflectionless configuration.
- **Coords (A46):** both the observable (S₁₁, a point in the impedance/reflection plane) and the objective (Op6 = `λ_min(S†S)` on the reflection block) live in the SAME S-plane / impedance coordinates. No real-space-Cartesian-vs-φ² mismatch.
- **Clock:** `θ = ωℓ_node/c` is the dimensionless bond electrical length (the free variable). `ω_C = c/ℓ_node` is the REPORTING unit only.

## §2. pre-test-physics-check (one plumber question, surfaced to Grant BEFORE design)

**In a real 3-way pipe tee, a surge down one pipe partially reflects off the branch** (the other two pipes present a lower combined impedance — for three identical lines, `Z₀/2`, so `Γ = (Z₀/2 − Z₀)/(Z₀/2 + Z₀) = −1/3`, a fixed 1/9-power backscatter, independent of any bore). **The X38 question in plumber terms: does rounding the tee (adding the junction bore — the accumulator volume + the throat) REDUCE that branch-reflection, or not?** My pre-design reading of the vacuum tee: the bore's accumulator (shunt C) sits AT the node (the low-impedance side) and the throat (series L) sits in the arms — this is the impedance step-DOWN orientation, the *opposite* of the L-match orientation (shunt-on-high-side) that would cancel a 2:1 step-up mismatch; and the vertex's C₃ᵥ symmetry forbids a privileged one-arm shunt. So the bore looks structurally UNABLE to cancel the branch reflection — the sharpest (point) junction should reflect least. **The load-bearing sub-question for Grant:** is that intrinsic `Γ = −1/3` branch-reflection a physical, real backscatter at every vacuum vertex (a `z=3` structural feature — a `z=2` through-junction would match perfectly), and is the point-junction-reflects-least reading the intended vacuum-vertex picture — or does canon expect the bore to smooth the tee (which would require a mechanism outside the leading-order lumped class)? Surfaced, not silently resolved; the driver measures it (G-C), Grant adjudicates the ontology.

---

## §3. THE EXTRACTION — the S₁₁ algebra, inputs, and the anti-install boundary (G-A)

### 3.1 Allowed inputs (the ONLY things the S₁₁ path may consume)

`{ L′ = μ₀ (MU_0), C′ = ε₀ (EPSILON_0) — which CANCEL, the coordination z=3, θ = ωℓ_node/c (dimensionless), the extent fraction f = d/ℓ_node, the shape factors s_L, s_C }`.

### 3.2 Forbidden inputs (G-A automatic FAIL if any appears in the S₁₁ computation)

`OMEGA_C`, `ω_C`, `M_E`, `L_CELL`/`C_CELL`, and any assignment setting `1/√(L_j C_j) = ω_C` (the #613 install). `ω_C = c/ℓ_node` may appear **only in REPORTING**. Enforced by the reused `scan_forbidden_inputs` / `_FORBIDDEN_MAGNITUDES` (X37 driver, cited + extended — symbol + `ave.core.constants` import + numeric-literal scan), applied to the new S₁₁ extraction module.

### 3.3 The exact symmetric 3-port S₁₁ (frozen algebra; μ₀, ε₀, ℓ cancel)

The vertex is `z` identical lines meeting at a node. Junction parasitics (X37, leading-order lumped): series throat `L_j = s_L·μ₀·d` in each arm, shunt accumulator `C_j = s_C·ε₀·d` at the node, `d = f·ℓ_node`. Normalize impedances to `Z₀`; the junction enters ONLY through the dimensionless products
```
x = ωL_j/Z₀ = s_L·f·θ        (series reactance / Z₀,  arm throat)
p = ωC_j·Z₀ = s_C·f·θ        (shunt susceptance · Z₀, node accumulator)
```
**MU_0 and EPSILON_0 cancel; ℓ_node folds into θ = ω/ω_C.** A wave incident down port 1 (the other `z−1` arms are semi-infinite matched lines of normalized impedance 1):
```
z_far  = 1 + j x                       (each far arm: series throat then matched line)
y_node = (z−1)/z_far + j p             (z−1 far arms in parallel + shunt accumulator)
z_in   = j x + 1/y_node                (series throat on the incident arm + node)
S₁₁    = (z_in − 1)/(z_in + 1)
```
**Bare-junction check (analytic, frozen — §5):** at `θ→0` (or `f→0`), `x,p→0` ⇒ `y_node = (z−1)`, `z_in = 1/(z−1)`, `S₁₁ = (1/(z−1) − 1)/(1/(z−1) + 1) = (2−z)/z`. For `z=3`: **S₁₁ = −1/3** (`|S₁₁| = 1/3`; the memoryless star `S_ij = 2/3 − δ_ij` gives the same). The memoryless junction is NOT matched — this is why a nontrivial `f*` COULD exist.

### 3.4 Anti-install proof (frozen)

The S₁₁ above is a pure function of `(θ, f, s_L, s_C, z)` — all geometric. No physical scale is an input. The S₁₁ module imports NO scale from `constants.py`; obj-1 uses the canonical `universal_operators.universal_eigenvalue_target` (Op6, a linear-algebra operator on the dimensionless S-block — importing it introduces no physical scale; the per-file G-A AST scan sees only this module's Names/imports). G-A is enforced at code level (§6).

---

## §4. THE CANONICAL OBJECTIVE (Op6) + THE THREE FROZEN OBJECTIVES

**The objective is NOT ours to invent.** Universal Operator #6 (eigenvalue-target.md, `clm-gdd70j`): `λ_min(S†S) → 0` — the ground state is the config where at least one mode is perfectly absorbed (reflectionless). The trefoil derivation applied it as **S₁₁ minimization** at the self-avoidance boundary → `R·r = 1/4` (constants.py:191-206). At the vertex, the reflection block is the 1×1 `[S₁₁(θ;f)]` (other ports match-terminated, radiating power away — so `λ_min(S†S) = |S₁₁|²` CAN reach 0; a lossless FULL 3×3 `S` is unitary ⇒ `λ_min ≡ 1`, degenerate — see the NAMED AMBIGUITY).

**NAMED AMBIGUITY / LIMITATION (frozen).** Op6's leaf gives the TARGET (`λ_min→0`) but not (a) which S-block, nor (b) the frequency to evaluate it at a *broadband* vertex site. Our frozen readings:
- (a) **S-block:** the 1×1 reflection `[S₁₁]` (the vertex as a 1-port load; the trefoil used the reflection at a boundary, not a unitary multiport). The full-3×3 reading is degenerate (`λ_min ≡ 1`) and is reported as a diagnostic, not the objective.
- (b) **frequency:** obj-1 evaluates Op6 at the band-top mode `θ = π` (`μ = −3`, the load-bearing ceiling mode X37/X33 care about, f-independent, unambiguous). The literal "deepest-notch" reading `min_θ λ_min` is reported SEPARATELY as a diagnostic (it is pinned at the trivial `θ→0` floor `((2−z)/z)²` shared by all f — evidence the reflectionless target is UNREACHABLE at the vertex).

**The three frozen objectives (obj-1 primary; obj-2/obj-3 = robustness comparators ONLY):**
- **obj-1 (canonical Op6, PRIMARY):** `J₁(f) = universal_eigenvalue_target([S₁₁(θ=π; f)]) = |S₁₁(π; f)|²`. `f* = argmin_f J₁`.
- **obj-2 (band-integrated, comparator):** `J₂(f) = (1/θ_top)∫₀^{θ_top} |S₁₁(θ; f)|² dθ` over the connected band (`θ_top` = X37's connected-band ceiling). `f* = argmin_f J₂`.
- **obj-3 (single-frequency, comparator):** `J₃(f) = |S₁₁(θ=π/2; f)|²` at fixed mid-band `θ=π/2`. `f* = argmin_f J₃`.

The argmin is over `f ∈ [0, 0.5]` (the X37 range: 0 = point junction, 0.5 = Wigner–Seitz upper bound). Reported for `s_L=s_C=1` (flagged modeling choice) AND swept over `s_L,s_C ∈ [0.3,3]²` (X37 R5 lesson).

---

## §5. FROZEN ANALYTIC EXPECTATIONS (M6 — written BEFORE any driver code; each verified in the derivation)

- **FORM (forced, NO CREDIT):** any ceiling reported in MeV via `ω_C` is dimensionally guaranteed and earns nothing. The deliverable is the dimensionless `f*` + branch + objective-spread.
- **BARE-JUNCTION MISMATCH (analytic, hand-derived §3.3):** `S₁₁(f=0) = (2−z)/z = −1/3` for `z=3` ⇒ `|S₁₁| = 1/3`. The memoryless junction is NOT matched; this is the reason a nontrivial `f*` can exist. **Verified analytically; the driver must recover it through the LOADED path (G-B, no early return).**
- **THE L-MATCH OBSERVATION (picture-predicted, to CONFIRM or REFUTE):** the parasitic pair (series L on the arm, shunt C at the node) has the L-match *element count* for a 2:1 ratio, `Q = √(Z_hi/Z_lo − 1) = √(2−1) = 1`. The classic L-match nulls `|S₁₁|→0` at one frequency. **Frozen prediction to be tested:** whether `|S₁₁|(θ; f)` dips BELOW the bare `1/3` at finite `f`. **Registered orientation caveat (to be confirmed by the driver, not assumed):** the accumulator sits at the node (low-Z side) and the throat in the arms — the step-DOWN orientation, *opposite* the L-match orientation (shunt on the high-Z side) that would null a 2:1 step-UP; and C₃ᵥ symmetry forbids a privileged one-arm shunt. So the caveat predicts the dip does NOT occur for the physical vertex (the bore only adds reflection) — the driver adjudicates.
- **SELF-CONSISTENCY MARK (frozen reporting):** report where `f*` sits vs `f_crit ≈ 0.184` (X37: the lumped quasi-static separation self-invalidates for `f > f_crit`). **If `f* > f_crit` the answer self-invalidates and I SAY SO.**
- **SOLITON COMPARISON MARKS (frozen, NOT inputs):** `1/(2π) ≈ 0.159` (tube radius, constants.py:76) and `1` (core-tube thickness, constants.py:189). Note the X37-repaired unasserted observation that `1/(2π) ≈ f_crit` where `ω_vertex ≈ π√3`. These are comparison marks for the branch-(i) test only.

---

## §6. GATES (all pre-registered; each consumes a COMPUTED quantity with a firing tolerance; planted-violation proof for each — G-D)

| Gate | Condition (frozen) | Tolerance / firing threshold | Planted-violation proof |
|---|---|---|---|
| **G-A anti-install** | the S₁₁ extraction module consumes ONLY the §3.1 allowed set; none of `{OMEGA_C, M_E, L_CELL, C_CELL}`, no `ave.core.constants` import, no forbidden numeric LITERAL (reuse X37's `scan_forbidden_inputs` / `_FORBIDDEN_MAGNITUDES`, cited + extended) | symbol + import + literal hits **= 0** (AST scan) | plant `OMEGA_C` by SYMBOL and by NUMERIC LITERAL → both FLAGGED |
| **G-B independent-reference recovery** | (i) the LOADED S₁₁ path at `f→0` (small nonzero f, full solve, **no early return** — X37 R3) recovers the bare-junction baseline `|S₁₁| = 1/3`; (ii) via the X37 module the LOADED dispersion at `f→0` recovers the **π√3 ceiling** hard-coded FROM #604:18 (cited) | `|S₁₁(f→0)| − 1/3| < 1e-4` AND `|g(f→0) − π√3|/π√3 < 1e-4` | plant a +1% offset on each loaded output → assert both FAIL |
| **G-C objective-robustness** | `f*` computed under all three frozen objectives; the SPREAD `max(f*)−min(f*)` reported first-class; branch assigned by the frozen rule below | spread `< 0.02` ⇒ robust selection; spread `≥ 0.05` ⇒ objective-dependent scatter ⇒ branch (iv) | plant a DIVERGENT bogus objective (selects `f*≠` the real value) → assert the spread-detector fires (crosses the branch-(iv) threshold); the 3 real objectives (control) do NOT |
| **G-D gates-can-fire** | every gate above consumes a computed quantity with a failing tolerance | each planted violation FIRES its gate; a no-op control does NOT | the plants above + a no-op control |

**Frozen branch-assignment rule (§ frozen branches, NO preferred outcome, NO post-hoc relaxation):**
- **Branch (i)** iff (primary obj-1) `|f* − 1/(2π)| < 0.02` AND robust (G-C spread `< 0.02`) → the matched bore COINCIDES with the unknot tube radius → **identity CANDIDATE** (flag for Grant, do NOT canonize).
- **Branch (ii)** iff `f* = 0` (boundary minimum) AND robust → the matched junction is the point junction → **closure (c)**: the walk ceiling `π√3` is exact, the bore stays a non-object at this abstraction.
- **Branch (iii)** iff `f*` = a definite interior value (`f* ∉ {0, 1/(2π)}`, `|f*−1/(2π)|≥0.02`, `f*>0.02`) AND robust → a **NEW derived scale**; report `g(f*)` and its MeV as a conditional (lumped-class) number.
- **Branch (iv)** iff the objective is degenerate/flat OR the objectives SCATTER (G-C spread `≥ 0.05`) → **no robust selection at this abstraction → honest null**; the fork stays with Grant's three closures.

Driver-honesty (Rule 10): closed S-parameter / argmin computation — no PML, no dead-actuator, no time-domain snapshot ambiguity; the loaded S₁₁ and the objectives are built and minimized directly. Reactance-pair N/A (frequency-domain S, not a time-domain LC snapshot). The bare Γ=−1/3 and the X37 π√3 ceiling are the two independent cross-checks.

---

## §7. OBSERVABLES + DELIVERABLES

- **S₁₁(θ; f, s_L, s_C)** — the exact symmetric 3-port reflection; the `|S₁₁|(ω, f)` landscape.
- **f\*** = argmin under obj-1 (primary), obj-2, obj-3 + the objective SPREAD (G-C first-class).
- **The bare Γ = −1/3 verification** + the **L-match confirmation/refutation** (does `|S₁₁|` dip below 1/3?).
- **Which branch fired** (i / ii / iii / iv) by the §6 rule; where `f*` sits vs `f_crit`; the s-sweep of `f*` over `[0.3,3]²`.
- **Gate ledger** incl. the four planted-violation proofs.
- Deliverables: this prereg (FROZEN, pushed first) → derivation doc → S₁₁ module `src/ave/core/junction_scattering.py` + driver `src/scripts/vol_1_foundations/x38_s11_bore_selection.py` + test `src/tests/test_x38_s11_bore_selection.py` → result doc + JSON + WHITE figure (`ave.viz.style.apply`/`save`; Okabe-Ito; honest axes+units; legend outside data; no on-figure title): the `|S₁₁|(ω,f)` landscape + the objective curves + the `f*` verdict + s-sweep + the branch that fired. `make verify` + test tier outputs pasted in the result doc. PR `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`, no self-merge.

## §8. SCOPE (honest tractability)

Phase 1 = the scalar/compression channel S₁₁ only (this dispatch). Vector/torsion (vertex flywheel; shear) scoped out — matches the X37 / #604 §5 deferral. The shape factors `s_L, s_C` are the equivalent-length normalization `= 1` (X37's flagged modeling choice) with the `[0.3,3]²` sweep as the honesty check. A fuller vertex model (evanescent-mode stub / finite-volume resonant branch — X37 C2) that could present a bypass is NOT modeled here; if `f*=0` fires, the closure is scoped to the leading-order positive-element lumped class. **An honest Phase-1-only result beats an overreached full one.**

---

**FROZEN 2026-07-10. No adjudication axis is dropped or relaxed post-hoc (Rule 11 / Rule 12). This freeze is verifiable by commit ordering: this commit is pushed BEFORE any driver code (the standing rule after #613; proven by X37).**

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
