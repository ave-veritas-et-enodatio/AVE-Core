# PRE-REG (FROZEN) — Electron self-braced UNIFIER: DERIVE + co-compress-MEASURE the field self-energy pull `p`

**Date:** 2026-07-01 · **Lane:** implementer · **Branch:** `analysis/electron-unifier-cocompress`
(worktree `/private/tmp/electron-unifier`, off `main` @ `e1e14572` — the MERGE of PR #441).
**Type:** DERIVATION (Part 1, symbolic/sympy) + SIMULATION (Part 2, co-compressing time-domain).
**Freeze-before-run:** this prereg is committed BEFORE the Part-2 co-compress driver runs. The
pass/fail (§ADJUDICATION) is frozen here; Part 1 (the Derrick derivation) is symbolic analysis that
precedes and INFORMS the frozen sim criteria (it is not a fit to sim data). Per Rule 11 no criterion is
dropped/weakened post-hoc to convert a NEGATIVE into a CONFIRMED.

**SHA-pin (this file, frozen commit):** `9f388305` — the derivation (Part 1) and co-compress driver
(Part 2) are built AFTER this commit and cite it. (This edit adds only the pin; the frozen §ADJUDICATION
criteria are unchanged from `9f388305`.)

---

## 0. WHY THIS RUN EXISTS (what the prior three attempts each got wrong)

This is the **4th** unification attempt. Prior odds held HIGH that it fails.

1. **Front-freeze (Stage-2)** — FAILED: seeded A1 precursor disperses (Mode-III).
2. **Coupled eigensolve (#415/#417)** — DOES-NOT-EXIST: no bound eigenstate carries BOTH mass and the
   (2,3) winding (gate-d FAIL, `bw_on_torus≈0.0001`).
3. **Bind-sim (PR #442, `2026-06-30_electron-bind-sim_result.md`)** — INCONCLUSIVE (resolution-limited).
   Its own §4/§5 name the three defects THIS run fixes:
   - **Wrong pull measured.** It measured the **varactor ponderomotive** pull `P=−∂⟨½Q²S(A)/C_0⟩/∂r`,
     which is NULL at `A=√α` (`S(√α)=0.996`, S-range 0.35% ⇒ `⟨S⟩` flat to <1%; the fitted `p` flipped
     5.23↔−0.06 with grid = the gradient of noise). Its §4 FLAG: the derivation invokes TWO pulls under
     one name — the varactor `dS/dr` pull (null) vs a **field self-energy** pull (§5.2, asserted, NOT
     modeled). **THIS run measures the FIELD SELF-ENERGY pull.**
   - **Two decoupled coordinates.** The A1 envelope sweep and the winding-loop sweep were SEPARATE; the
     derivation's single collective `r*` was never realized. **THIS run co-compresses ONE collective `R`.**
   - **`L_w` 17% drift.** The winding seed was fixed-per-cell, so the circulation store scaled with loop
     VOLUME, not as conserved-circulation-in-a-shrinking-loop. **THIS run seeds `Γ_w=∮ω·dl` conserved.**

**Reference (verify-before-cite, both greped this session):**
- Derivation: `research/2026-06-30_electron-portmap-derivation_result.md` (merged PR #441; §5 BIND now
  **SYMBOLIC-ONLY / sim-untested** per the PR #442 caveat-fold, commit `4cdaeb36`).
- Bind-sim: `research/2026-06-30_electron-bind-sim_result.md` (INCONCLUSIVE; commit `efb5b8ef`).

---

## SECTOR HEADER (stated before any standard-physics word)

- **MODE:** standing electron — **EXISTENCE**, not genesis. Does a bound state hold together as ONE
  self-braced object? The twice-falsified self-formation slot stays BARRED (A47 v11b). TRAP-not-CREATE.
- **REGIME / PHASE-STATE:** sub-saturated A1 mass core at `A=V_yield/V_snap=√α≈0.085` (Grant
  def-vyvsn1=T2 ruling; `S(√α)=√(1−α)≈0.996`). Lossless reactive self-braced balance. The (2,3) winding
  runs a locked circulation (pre-existing, conserved).
- **THE ONE COLLECTIVE COORDINATE:** a single collective radius **`R`** scaling BOTH the A1 dilatation
  envelope AND the (2,3) winding loop TOGETHER (the derivation's single `r*`). This is the FIX for the
  prior two-decoupled-coordinate defect.
- **SECTORS + ownership (A1⊥T2 cross-wiring watch):** A1 = dilatation = MASS envelope (capacitive bulk).
  (2,3) Cosserat winding = CHARGE (inductive shear). μ-sign = selector. NEVER cross-wired.

**Guard against SM/QED leak:** the equilibrium is a **reactive pressure / Derrick force balance** at a
self-set operating point, NOT a Lagrangian minimization, gradient-descent-on-energy-basin, or continuum-
Helmholtz eigensolve. The energy functional is READ OFF the engine's own Hermitian generator, not a
posited continuum action. Ports/operators are native Cosserat K4 (`L_D=adjoint_div(D∇)` on
`TETRA_OFFSETS`), NOT Cartesian 7-pt stencils.

---

## PART 1 — DERIVE the field self-energy pull exponent `p` (symbolic; PRECEDES the sim)

**The substrate energy functional** = the expectation `⟨x|H|x⟩` of the ACTUAL engine Hermitian generator
(`coupled_cage_winding._assemble_H`, verify-before-cite `coupled_cage_winding.py:325–358`):
`H_A1 = ω_b·I − c_A1²·L_D`, `H_bω = ω_s·I − c_ω²·L_D`, `L_D = adjoint_div(D·∇)`, `D = 1/S(A)`
(`native_cage_imex.py:148`, `graded_vacuum_network.py:245`). Integrating by parts, the physical field
energy has four terms:

| term | functional | meaning |
|---|---|---|
| A1 gradient | `E = c_A1² ∫ |∇a|²/S(A) dV` | A1 dilatation self-energy (flux-crowding cost) |
| winding gradient | `E = c_ω² ∫ |∇b|²/S(A) dV` | (2,3) winding circulation gradient energy |
| A1 mass-tank | `E = ω_b ∫ |a|² dV` | the A1 on-site rest-store |
| winding LC-tank | `E = ω_s ∫ |b|² dV` | the winding on-site LC store |

**Derrick scaling** (`R→λR`, d=3) with the load-bearing constraints held: enclosed reactive charge
`Q=∫|a|²=const` (⇒ `A²∝R⁻³`), conserved circulation `Γ_w=∮ω·dl=const` (⇒ `B∝R⁻¹`). At `A=√α`,
`1/S(A)≈1.004=const` contributes NO λ-dependence (this is the whole point: the field self-energy is a
GRADIENT-GEOMETRY term, independent of the saturation `dS/dr` the prior sim found null). **Symbolic
(sympy) — this analysis is DONE and pinned in this branch's Part-1 derivation section; stated here so
the frozen sim criteria are informed by it, not fit to it:**

- A1 gradient: `E ∝ R⁻²` → force `+2Qc²k_S/R³` = **OUTWARD brace, p=3**.
- winding gradient: `E ∝ R⁻¹` → force `+Γ²c²k_S/R²` = **OUTWARD brace, p=2**.
- A1 mass-tank: fixed-Q ⇒ **inert**.
- winding LC-tank: `E ∝ +R` → force `−Γ²ω_s` = **INWARD pull, p=0**.

**DERIVED prediction (the crux):** the inward (collapse) pull is the winding LC-tank, **`p_derived = 0`**;
the steepest brace is the A1 gradient self-energy, **`p_brace = 3`**. Because in 3D the STEEPEST force any
gradient-class self-energy can produce is exactly `R⁻³` (the fixed-charge limit) and it points OUTWARD,
**no field self-energy pull can out-steepen the `r⁻³` brace ⇒ `p<3` is FORCED at the derivation level.**
`F_R(R)=2Qc²k_S/R³+Γ²c²k_S/R²−Γ²ω_s` has EXACTLY ONE zero `R*>0`, and `dF_R/dR<0` everywhere ⇒ a **stable
well**.

**FLAG-DON'T-FIX (surfaced, NOT resolved — Grant adjudicates the mechanism-headline):** derivation §5.2
(`2026-06-30_electron-portmap-derivation_result.md:363`) asserts the *field self-energy* IS the *inward*
pull ("Coulomb-class `p∈[1,2]`"). The substrate says the gradient self-energy is *outward* (a brace);
the inward binder is the winding LC-tank (`ω_s∫|b|²`, p=0). **The `p<3` verdict is IDENTICAL under both
readings** — this flag changes the mechanism NAME, not the pass/fail. Recorded verbatim in the result.

### PART-1 DECISION GATE (frozen)

- **If the DERIVED steepest inward pull `p_derived ≥ 3`** → the pull can out-shallow / match the `r⁻³`
  brace → UNIFIER **MARGINAL/DEAD at the derivation level** → honest NEGATIVE. (Part 2 then runs a
  minimal confirmation-of-negative.) — _the derivation above returns `p_derived=0 < 3`, so we PROCEED,
  but the gate is stated so a NEGATIVE would have been bankable._
- **If `p_derived < 3`** → PROCEED to Part 2 to confirm the co-compressing dynamics realize it.

---

## PART 2 — CO-COMPRESSING instrument (the frozen measurement)

Build a driver where ONE collective radius `R` compresses BOTH sectors together, with the winding seeded
so `Γ_w=∮ω·dl` (circulation) is GENUINELY CONSERVED as `R` shrinks (fix the 17% drift: scale the seed
amplitude as `B∝1/R` — conserved-circulation-in-a-shrinking-loop, NOT fixed-per-cell). Measure, sweeping
the collective `R`:

1. **The field self-energy pull `P(R)` and its slope `p`** — from the MEASURED gradient energy
   `E_grad(R)=∫(c_A1²|∇a|²+c_ω²|∇b|²)/S dV` over the co-compressed field (the substrate's own term, NOT
   the varactor `⟨S⟩`). Also the winding-LC-tank inward term `ω_s∫|b|²`. `p = −dln|F|/dlnR`.
2. **The `r⁻³` circulation brace `B(R)`** — now actually exercised by co-compression + conserved `Γ_w`.
3. **The force balance `dF_net/dR` at the equilibrium `R*`** → sign = stable vs unstable.
4. **`Γ_w` conservation** — verify <few% drift over the recording window; CONTRAST the prior 17%.

**Coordinate discipline (phase-space-coordinate-check):** `p` and the balance live in the COLLECTIVE
ENVELOPE RADIUS `R` (the soliton SIZE), matching the derivation's `r*`. The (2,3) Link stays in its
phase-space home (the topological integer on the frozen template direction); the DIMENSIONFUL circulation
`Γ_w` is the co-compressed conserved quantity. No φ²/real-space mismatch.

### GUARDS (frozen, learned from the prior sim)

| Guard | Requirement |
|---|---|
| FIELD SELF-ENERGY pull, NOT varactor | measure `E_grad=∫|∇·|²/S`, the gradient term; the varactor `⟨S⟩` is a red herring at `A=√α` and is NOT the pass observable |
| CO-COMPRESSING (one collective `R`) | the A1 envelope AND the winding loop compress together; NOT two decoupled coordinates |
| `Γ_w` genuinely conserved | seed amplitude `B∝1/R`; verify circulation drift <5% (contrast prior 17%) |
| Tellegen-LOSSLESS | `port_sigma=0`; `|dH/H|` at solver tol; a damping term = FAIL not fix (#83) |
| TRAP-not-CREATE | winding pre-exists (seeded, conserved by construction); existence not genesis |
| Resolution-robust | ≥2 grids; the verdict must NOT flip with grid (prior INCONCLUSIVE was a grid-flip) |
| HOLD REAL ODDS IT FAILS | `p≥3` (measured) → bank bifurcated; NO rescue-narrate; NO manufacture of `p<3` |
| Class-C | FORM-derived; `m_e`/α/`A=√α` imported/echo, never claimed as emergence |

---

## ADJUDICATION CRITERIA (FROZEN — pass/fail locked before the Part-2 run)

Let `p_derived` = the Part-1 symbolic steepest-inward-pull exponent; `p_measured` = the Part-2 fitted
pull exponent (the FIELD SELF-ENERGY gradient force slope), resolution-robust across ≥2 grids;
`b_measured` = the fitted brace exponent (expect ≈3); `dF_net/dR` at the crossing.

- **UNIFIER-CONFIRMED** (the electron IS one self-braced object) **iff ALL:**
  - (U1) `p_derived < 3` (Part 1), AND
  - (U2) `p_measured < 3` **resolution-robust** (does NOT flip `<3`↔`>3` across the ≥2 grids; the fit has
    real dynamic range, r² adequate), AND
  - (U3) `dF_net/dR` at `R*` has the STABLE sign (outward force weakens with expansion; equivalently the
    derivation's `dF_net/dr>0`), resolution-robust, AND
  - (U4) `Γ_w` conserved to <5% drift over the window (the co-compress fix landed), AND
  - (U5) Tellegen-lossless (`|dH/H|` at solver tol; NO dissipative term).

- **UNIFIER-DEAD** (marginal/implodes → bank the bifurcated electron; existence still secure via the
  independent T2/charge WALL, `resonant-lc-solitons.md:136`) **if:**
  - (D1) `p_derived ≥ 3` (Part-1 gate fails — the derivation-level NEGATIVE), OR
  - (D2) `p_measured ≥ 3` resolution-robust (the co-compress dynamics realize a pull that out-steepens
    the `r⁻³` brace), OR
  - (D3) `∄ R*` finite (brace never balances the pull), OR `dF_net/dR` UNSTABLE at `R*`, resolution-robust.

- **INCONCLUSIVE** (say what's still missing — Rule 11) **if:**
  - (I1) `p_measured` FLIPS `<3`↔`>3` with grid (verdict not resolution-robust), OR
  - (I2) the co-compress instrument still fails to exercise the pull/brace contest (dynamic range too
    small to place `p` relative to 3), OR
  - (I3) `Γ_w` still drifts ≥5% (the co-compress fix did NOT land) — the measurement premise unmet.

**Anti-rescue guards (frozen):**
- The pass observable is the FIELD SELF-ENERGY gradient force, NOT the varactor `⟨S⟩` (which is null at
  `A=√α` by construction — measuring it again and calling a null a pass is BARRED).
- No dissipative term may be introduced to force a balance (#83 lesson; a damping fix = FAIL).
- No new hypothesis refills a DEAD slot (A47 v11b substitution-not-retraction).
- If all failure paths point to one mechanism, that is Rule-11 honest closure — name it, close it.
- `m_e`/α/`A=√α` are calibrated/imported; only the FORM (the pull/brace exponents + the stability sign)
  is derived. NO emergence-class claim (A47 v17 family).

---

## CLASSIFICATION (consistency-vs-emergence — pre-committed)

**Class C — CONSISTENCY / FORM-chord.** The mechanism (a reactive brace out-steepening a self-energy
pull under one collective radius) is at best a FORM-chord peer-with-SM: it gives the SM-absent mechanism
for a stable localized electron, but the SIZE `R*` is a scale tied to imported `L_NODE=ℏ/(m_e c)`, and
`A=√α` is a Class-B α-echo (`V_yield=√α V_snap`, `constants.py:464`). NO dimensionless observable is
computed free of the target ⇒ NOT Class-D emergence. A UNIFIER-DEAD verdict is a legitimate Class-C
consistency NEGATIVE with a named mechanism, not a failure to debug toward binding.

## DELIVERABLE

`research/2026-07-01_electron-unifier-cocompress_result.md`: the DERIVED `p` (Part 1, with the
flag-don't-fix contradiction surfaced) + the MEASURED `p` (Part 2) + `dF_net/dR` + `Γ_w` drift, and the
VERDICT (UNIFIER-CONFIRMED vs UNIFIER-DEAD vs INCONCLUSIVE) with honest solidity + open items. NO
KB/manuscript edits (research/ only). Incremental commits (prereg → Part-1 derivation → co-compress
driver → result). Push branch, STOP (orchestrator opens the PR after an independent verify).
