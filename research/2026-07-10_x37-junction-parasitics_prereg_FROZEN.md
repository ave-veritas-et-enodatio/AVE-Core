# PREREG (FROZEN) — X37: junction-parasitic extraction (the srs vertex equivalent circuit DERIVED from bond geometry)

**Date:** 2026-07-10 · **Branch:** `analysis/x37-junction-parasitics` (off main @ ba662d57) · **Task:** X37 (Grant-fired, D-I route)
**Consumes (frozen references):**
- [`research/2026-07-09_srs-band-survey_result.md`](2026-07-09_srs-band-survey_result.md) — the merged **#604** result: scalar band top **π√3 ω_C = 5.4414 ω_C** at H, distributed-TL arccos map `ω = ω_link·arccos(μ/3)`, `ω_link = √3 ω_C`. **This is the G-B independent-reference number.**
- [`research/2026-07-09_x33-clock-architecture_result.md`](2026-07-09_x33-clock-architecture_result.md) — the two-clock (walk-PINS vs continuum-LIFTS) fork X37's branch (i) can close.
**Supersedes the approach of:** X36 / PR #613 (BLOCKED for INSTALLING a lumped vertex tank instead of computing it). X37 EXTRACTS the vertex reactance from geometry; it installs nothing.

**Class (consistency-vs-emergence):** **MIXED — declared per component.** The vertex **g-factor VALUE is DERIVED-GEOMETRIC** (a pure number out of the 120° convergence + srs twist + the extent fraction; MU_0/EPSILON_0 and ℓ_node cancel from every dimensionless dispersion product — see §3.3). The **SCALE** `ω_C = c/ℓ_node` is **dimensional-forced / identity-class** (ℓ_node ≡ ℏ/(m_e c), constants.py:282 — carries the CODATA/m_e content) and appears **only in REPORTING as the unit of g**, never in the derivation chain. No α / Q_TANK / CODATA on any verdict path. "Ceiling near ω_C" is dimensionally forced and gets **no credit** (M6).

---

## §0. SKILL-SELECTION PLAN (60-second, per pre-workstream planning discipline)

Applied set, declared before any code (retro-checked before each commit):

| Skill | Where it fires | What it guards |
|---|---|---|
| **ave-prereg** | this doc | freeze-before-driver (commit-ordering proof, the #613 lesson); no post-hoc axis drop |
| **ave-canonical-source** | §3 inputs | every number by SYMBOL from `constants.py` / a merged leaf; nothing hard-coded |
| **ave-canonical-leaf-pull** | §1, §3 | pull the K4/srs geometry + translation-circuit + #604 band leaf BEFORE deriving |
| **substrate-native-check** | §1 | K4/srs-TLM scatter+connect; phase-space-vs-real-space; NOT Lagrangian/Helmholtz/energy-basin |
| **ave-ee-first-mapping (trigger 2, new-derivation territory)** | whole doc | this IS an EE extraction — TL discontinuity / mode-matching is the substrate-native language |
| **consistency-vs-emergence** | header, §6 | g VALUE = derived-geometric; SCALE = dimensional-forced/identity; tag each verdict |
| **ave-driver-script-honesty** | §7, driver | gates consume COMPUTED quantities; planted-violation proofs; no dead-actuator |
| **ave-evidence-framing-discipline** | §5, §6 | "ceiling near ω_C" gets no credit; the deliverable is topology-class + g + extent-sensitivity |
| **phase-space-coordinate-check (A46)** | §1 | observable is a dispersion ceiling ω_top(k) vs a dispersion ceiling — matching coordinates |

Retro-pass rule: if the applied set drifts during implementation, note it in the result doc before the commit that drifts.

---

## §0.5 SECTOR HEADER (mandatory, before any standard-physics word)

- **MODE:** linear small-signal band structure (eigen-dispersion of the cold network).
- **REGIME:** cold, sub-yield, lossless (A ≪ 1; Op14 saturation OFF; no dissipation — reactive-only extraction).
- **SECTOR:** **scalar / compression channel (Phase 1).** The vertex DOF engaged: the **breathing / dilatational** compliance of the junction region (the fully-symmetric 3-arm mode). Vector/torsion channels (vertex flywheel = rotational inertia of the vertex plane; shear bypass) are **scoped out of Phase 1** (see §9) — attempted only if genuinely tractable this session.
- **Which sector owns the DOF:** compression = A1 dilatation on the bond TLs; the vertex parasitic is a reactance of THAT channel, not a charge/spin (Cosserat-winding) object. No sector cross-wiring.

---

## §1. substrate-native-check (done BEFORE any numerical code, per Operating Principle 1)

- **Dynamics:** K4/srs distributed **transmission-line network** (Op5 scatter+connect is the memoryless limit). The bonds are **distributed TLs** with per-unit-length `L' = μ₀`, `C' = ε₀` (⇒ `c = 1/√(L'C') = c₀`, `Z_0 = √(L'/C')`). The vertex is a **TL discontinuity**, analysed by **mode-matching / junction-scattering** — the standard EE way to EXTRACT (not install) a junction equivalent circuit. NOT a Lagrangian, NOT gradient-descent, NOT continuum-Helmholtz, NOT an energy-basin.
- **Layout is frozen in canon:** srs embedding (I4₁32, z=3), **3 bonds per vertex at 120° in the local vertex plane**, chirality twist along the network, bond length `ℓ_node` (constants.py:282). The vertex parasitics are therefore **already determined by this geometry** — the job is to compute them.
- **Coords (A46, phase-space-coordinate-check):** the observable is a **dispersion ceiling ω_top(k)** — the top of the connected band manifold. The memoryless reference (#604) is the same object (band top at H). Ceiling-vs-ceiling ⇒ **matching coordinates**; no real-space-Cartesian-vs-φ² mismatch.
- **Clock:** the bond TL sets `ω_C = c/ℓ_node` as the natural frequency unit. This is the REPORTING unit only (§3.3); it is not an input to any L/C.

## §2. pre-test-physics-check (one plumber question, surfaced to Grant BEFORE design)

**Is the 120° vacuum vertex, for the scalar/compression channel, an ACCUMULATOR or a THROAT?** In real plumbing a tee with a sudden extra volume is a **shunt accumulator** (a compliance to ground — it low-passes water-hammer and CAPS the pass-band); a constriction is a **series inertance** (a throat the surge pushes past — it lifts the cutoff). The vacuum vertex is where three compression lines merge: it is *both* a little extra volume to squeeze (shunt C) *and* a little throat where the flux crowds (series L), and the **topology class of the ceiling turns entirely on which dominates.** The walk leans accumulator (compression engages the shunt compliance). **The load-bearing sub-question for Grant:** canon gives the vertex a LENGTH (`ℓ_node`) but **no transverse SIZE** (there is no bond radius / core radius / filling fraction in `constants.py` — only `ℓ_node` and the *larger* `ℓ_c = √6·ℓ_node`). A TL junction of zero-width lines has **zero** discontinuity parasitic; the parasitic is entirely a finite-width effect. **Does canon intend the bond to have a transverse extent (and if so, what fixes it), or is the vertex a true point-junction (parasitic → 0, memoryless exact)?** This is exactly the closability question G-C measures; it is surfaced, not silently resolved.

---

## §3. THE EXTRACTION — inputs, method, and the anti-install boundary (G-A)

### 3.1 Allowed inputs (the ONLY things the extraction path may consume)

`{ L' = μ₀ (MU_0), C' = ε₀ (EPSILON_0), the 120° bond angles, the srs twist/chirality, ℓ_node as the bond length, the DERIVED vertex extent d = f·ℓ_node }`.

### 3.2 Forbidden inputs (G-A automatic FAIL if any appears in the vertex L/C computation)

`OMEGA_C`, `ω_C`, `M_E`, `L_CELL`/`C_CELL` used as a tank, or **any assignment setting `1/√(L_j C_j) = ω_C`** (that is the #613 install). `ω_C = c/ℓ_node` may appear **only in REPORTING** as the unit of g.

### 3.3 Why the extraction is genuinely dimensionless (the anti-install proof, frozen)

The junction of extent `d = f·ℓ` is a lump of the SAME medium: excess series inductance `L_j = s_L · μ₀ d`, excess shunt capacitance `C_j = s_C · ε₀ d`, with `s_L, s_C = O(1)` geometric shape factors set by the 120° convergence + twist (COMPUTED in the derivation, not assumed). The loaded-line Bloch dispersion depends on the junction only through the dimensionless products
```
B·Z_0 = (ω C_j)(√(μ₀/ε₀)) = ω s_C ε₀ f ℓ √(μ₀/ε₀) = s_C f · (ωℓ√(μ₀ε₀)) = s_C f · βℓ
X·Y_0 = (ω L_j)(√(ε₀/μ₀)) = ω s_L μ₀ f ℓ √(ε₀/μ₀) = s_L f · (ωℓ√(μ₀ε₀)) = s_L f · βℓ
```
**MU_0 and EPSILON_0 cancel identically; ℓ_node cancels into βℓ = ω/ω_C.** The dispersion is a pure function of `(βℓ, f, s_L, s_C)` — all geometric. The g-factor `g = ω_top/ω_C` is a pure number. This is the substrate-native reason the value is derived-geometric and the scale is a reporting unit (header MIXED class). **G-A is implemented at code level:** the vertex-parasitic module imports **no physical scale** from `constants.py` (only geometry); a test greps/AST-inspects the extraction functions for `{OMEGA_C, M_E, L_CELL, C_CELL}` and a planted-violation test proves the gate fires.

### 3.4 Method (frozen)

1. **Memoryless baseline (Rule-14 reuse of the validated #604/x33 srs pipeline):** `ω = ω_link·arccos(μ/3)`, `ω_link = √3 ω_C`, top = π√3 ω_C at μ=−3. Recompute-free reference (G-B hard-codes π√3 FROM #604, not from this code path).
2. **Junction equivalent circuit:** quasi-static energy extraction of the merge region (extent d = f·ℓ) → `(L_j, C_j)` and the symmetric-mode **series/shunt split** `(s_L, s_C)`. Topology class read off the split.
3. **Insert into the dispersion:** the shunt susceptance `jB = jωC_j` and series reactance `jX = jωL_j` modify the nodal KCL → a loaded arccos / ABCD-Bloch map. Solve the loaded band top vs f.
4. **1D two-node chain** as the exactly-solvable cross-check (closed-form band edges), plus the srs 4-site BCC cell for the real 3D number.

---

## §4. VERTEX-EXTENT DERIVATION + SWEEP (G-C, first-class result)

The junction has parasitics only because it has finite extent `d` where the three bond fields merge. **Canon provides no transverse bond scale** (§2), so:
- **Canon-faithful limit:** `f → 0` (1D-line bonds ⇒ point junction ⇒ parasitic → 0 ⇒ memoryless π√3 ω_C exact). This is not a rescue; it is what the canonical 1D-line geometry literally implies.
- **Extent derivation (stated, then swept):** the largest defensible junction region is the **Wigner–Seitz half-bond** — the node "owns" the medium out to each bond midpoint — giving an UPPER-BOUND probe `f = 0.5`. A geometry-only central estimate from the 120° field-merge overlap is derived in the derivation doc; it is a **modeling choice, not a canonical number** (flagged).
- **Sweep (frozen):** compute `g_scalar(f)` over `f ∈ [0, 0.5]` and REPORT the ceiling sensitivity `dg/df` as a first-class result. **If the ceiling swings hard with f, the derivation is not closed — say so plainly (branch iii).**

---

## §5. FROZEN ANALYTIC EXPECTATIONS (M6 — written BEFORE any driver code)

- **FORM (forced, NO CREDIT):** `ω_vertex = g·c/ℓ_node`, `g = O(1)`. Any "ceiling near ω_C" is dimensionally guaranteed and earns nothing.
- **Topology-class expectation (stated to be confirmed/refuted):** the walk leans **accumulator** → the junction is a **shunt-compliance low-pass**. Circuit consequence, hand-derived for the exactly-solvable 1D pure-shunt-C chain and FROZEN as the check: the shunt compliance opens a **zone-edge stop-band** and **pins the connected-band ceiling DOWN linearly in f**:
  ```
  g_scalar(f) = π√3 · (1 − s_C f)        (srs;  1D analogue: g = π(1 − s_C f))
  ```
  i.e. **compression → shunt accumulator → ceiling LOWERED ∝ f** (extra compliance = softer = lower cutoff). A non-negligible **series arm-inductance** `s_L` pushes the ceiling back UP (`+ s_L f`-type term); the NET `g` and the `s_L/s_C` split are the COMPUTED deliverable, not an input.

- **THE REGISTERED OPEN QUESTION (three branches, NO preferred outcome):**
  - **(i)** `g_scalar → π√3` within tol (top robust to the extent, e.g. shunt-transparent-at-top and/or series/shunt cancellation) ⇒ **the walk clock and the vertex clock are ONE geometry-derived clock ⇒ the X33 two-clock question closes IN-ENGINE after all** (because nothing was installed).
  - **(ii)** `g_scalar =` some OTHER definite O(1) (converged, small swing) ⇒ **a NEW derived spectral feature — two real clocks — X33 sharpened with a derived second scale.**
  - **(iii)** extraction is **extent-dominated** (G-C fires) ⇒ **the junction question is not closable at the TL-abstraction level** (canon gives no bond width) — **bank that honestly.**

---

## §6. GATES (all pre-registered; each consumes a COMPUTED quantity with a tolerance that can FAIL; planted-violation proof for each — G-D)

| Gate | Condition (frozen) | Tolerance / firing threshold | Planted-violation proof |
|---|---|---|---|
| **G-A anti-install** | the vertex-parasitic extraction path imports/consumes ONLY the §3.1 allowed set; none of `{OMEGA_C, M_E, L_CELL, C_CELL, ω_C-set-to-1/√(LC)}` appears | forbidden-symbol count in the extraction module/functions **= 0** (AST + source scan) | plant `OMEGA_C` into the extraction path → assert the gate RAISES |
| **G-B independent-reference recovery** | as `f → 0` the loaded model recovers the FROZEN #604 memoryless top | `|g_scalar(f=0) − π√3| / π√3 < 1e-3`, compared against the **hard-coded π√3 FROM #604** (cited), NOT a self-recompute | plant a perturbed `f→0` limit (offset the baseline) → assert G-B FAILS |
| **G-C extent-honesty** | vertex extent DERIVED, then ceiling swept; sensitivity reported | branch assignment by the frozen rule below; the swing `Δg = g(0) − g(0.5)` is REPORTED (first-class), not hidden | plant an f-independent ceiling → assert the "extent-dominated" detector does NOT misfire, and vice-versa |
| **G-D gates-can-fire** | every gate above consumes a computed quantity with a failing tolerance | each planted violation FIRES its gate; a null-perturbation does NOT | the three plants above + a no-op control |

**Frozen branch-assignment rule (§5 open question, no post-hoc relaxation):**
- **Branch (i)** iff `|g_scalar(f*) − π√3|/π√3 < 0.02` **AND** swing `|g(0) − g(0.5)|/π√3 < 0.05`.
- **Branch (iii)** iff swing `|g(0) − g(0.5)|/π√3 > 0.10` (extent-dominated).
- **Branch (ii)** iff `g_scalar(f*)` converges (swing < 0.05) to a definite value with `|g_scalar(f*) − π√3|/π√3 ≥ 0.02`.
- `f* = 0.5` (the Wigner–Seitz upper-bound probe) is the reported central; the whole `g(f)` curve is banked so the reader can re-anchor f.

Driver-honesty (Rule 10): closed spectral/linear-algebra solve — no PML, no dead-actuator, no time-domain snapshot ambiguity; the loaded dispersion is built and solved directly. Reactance-pair N/A (spectral, not time-domain). The 1D closed-form band edges cross-check the srs numerics.

---

## §7. OBSERVABLES + DELIVERABLES

- **g_scalar** = ω_top/ω_C for the loaded srs band (and 1D chain), as a function of extent f.
- **(s_L, s_C)** the series/shunt split ⇒ the **topology class** (series-trap / shunt-accumulator-low-pass / partitioned).
- **The vertex equivalent circuit** (S(ω) or the shunt-B + series-X lumped equivalent) written explicitly.
- **The extent-sensitivity sweep** g(f) over [0, 0.5] + Δg.
- **Which branch fired** (i / ii / iii) by the §6 rule.
- **Gate ledger** incl. the four planted-violation proofs.
- Deliverables: this prereg (FROZEN, pushed first) → derivation doc → driver `src/scripts/vol_1_foundations/x37_junction_parasitics.py` + test `src/tests/test_x37_junction_parasitics.py` → result doc + JSON + WHITE figure (`ave.viz.style.apply`/`save`; Okabe-Ito; honest axes+units; legend outside data; no on-figure title). `make verify` + test tier outputs pasted in the result doc. PR `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`, no self-merge.

## §8. SCOPE (honest tractability)

Phase 1 = the scalar/compression channel only (this dispatch). Vector/torsion (vertex flywheel; shear bypass) attempted ONLY if genuinely tractable this session; otherwise scoped out explicitly in the result doc as the named follow-on. **An honest Phase-1-only result beats an overreached full result.**

---

**FROZEN 2026-07-10. No adjudication axis is dropped or relaxed post-hoc (Rule 11 / Rule 12). This freeze is verifiable by commit ordering: this commit is pushed BEFORE any driver code (the new standing rule after #613's single-commit landing made its freeze unclaimable).**

---

## POST-FREEZE DEVIATION LOG (2026-07-10, PR #616 adversarial review R2 — KEEP-BOTH, frozen text quoted; the freeze above is NOT edited)

Every deviation between this frozen prereg and the shipped result is named here — none stays silent. The frozen text is quoted; the shipped reality follows.

- **D1 — the (s_L, s_C) split was ASSUMED, not COMPUTED (the load-bearing one).** *Frozen (§3.3):* "the series/shunt split `(s_L, s_C)` … COMPUTED in the derivation, not assumed"; (§3.4) "the series/shunt split (topology class) is a computed output, not an input." *Shipped:* `s_L=s_C=1` is **assumed** (equivalent-length normalization); the 120° convergence + srs twist enter **no shipped equation** (only the coordination `z=3` does; the identical circuit follows for any 3-regular network). The circuit FORM is a leading-order Marcuvitz lumped equivalent, a disclosed modeling choice; the LOW-PASS class is a **passivity** result, not a computed junction field. (Result doc Correction Log C1.)
- **D2 — the `s_L`-lifts expectation was SIGN-INVERTED.** *Frozen (§5):* "A non-negligible **series arm-inductance `s_L`** pushes the ceiling back **UP** (`+ s_L f`-type term)." *Shipped:* the derivation and exact solve show the series throat **LOWERS** the ceiling (`κ = s_L + (2/3)s_C`, both terms positive → both lower). The frozen "pushes UP" expectation is **refuted**; both channels are reactive stores that pin the cutoff DOWN.
- **D3 — the pure-shunt anchor coefficient changed.** *Frozen (§5):* "`g_scalar(f) = π√3·(1 − s_C f)`" (coefficient `s_C`). *Shipped (derivation §4):* the srs pure-shunt slope is `(2/3)s_C` (the `2/3` from the z=3 node), i.e. `g = π√3(1 − (2/3)s_C f)`; the `1D analogue g = π(1 − s_C f)` frozen alongside used the z=2 coefficient and is superseded by the shipped `band_top_1d` closed form (D4).
- **D4 — the promised cross-checks: 1D SHIPPED, 4-site DEVIATION-NOTED.** *Frozen (§3.4):* "The **1D two-node chain** as the exactly-solvable cross-check (closed-form band edges), plus the **srs 4-site BCC cell** for the real 3D number." *Shipped:* the **1D two-node closed-form check is SHIPPED** (`loaded_cos_ka_1d` / `band_top_1d`, transfer-matrix trace; review R2). The **explicit srs 4-site BCC dynamical-matrix diagonalization was NOT shipped**: the srs result uses the reduced single-branch loaded arccos map (μ swept over the adjacency range [−3, 3]), which captures the band **top** (the H-point `μ=−3`, achieved by real k) but does not compute the full 4-band structure. Deviation noted; the reduced model is sufficient for the ceiling (the sole Phase-1 observable) but the 4-band solve is a named follow-on.
- **D5 — the "2e-16 recovery" was float roundoff, not a solver exercise (fixed in code `1186c891`).** *Frozen (§6 G-B):* "compared against the hard-coded π√3 FROM #604". *Shipped fix:* G-B now drives the LOADED solver at f=1e-5 (converges to π√3 within 1e-4); the f=0 memoryless identity is recorded separately. (Review R3.)
- **D6 — the "no transverse scale in canon" premise (§2 / §4) was factually incomplete.** *Frozen (§2):* "canon gives the vertex a LENGTH (`ℓ_node`) but **no transverse SIZE** (there is no bond radius / core radius / filling fraction in `constants.py` — only `ℓ_node` and the *larger* `ℓ_c`)." *Correction (review R6):* canon **does** carry transverse scales — **tube radius `ℓ_node/(2π)`** (constants.py:76) and **core-tube thickness `ℓ_node`** (constants.py:189) — but both are **soliton/core-sector** objects, so the bare-bond extent is not fixed **without a sector-ownership ruling** (three candidate closures in the result doc §4). The plumber question is thereby **sharpened**, not answered.

Code+gates repair: commit `1186c891` (R2/R3/R4/R5/R8). Docs restatement: this log + the derivation dated notes + the result Correction Log.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
