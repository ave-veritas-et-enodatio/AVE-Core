# PREREG (FROZEN) — THE MATTER-STIFFENING DERIVATION: does asymmetric channel loading drive ρ_eff = k_a,eff/k_s,eff from the Ax3 cold point (ρ=1) toward the stiff-matter point (ρ*≈9.77)?

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/matter-stiffening-rho`
**Grant-fired:** 2026-07-04 ("go" — third plumber hypothesis of the day).
**Status when frozen:** design + bins + knife locked BEFORE any ρ_eff number is read.

> **FROZEN.** No adjudication axis, bin definition, ledger row, or knife below is edited after
> the driver runs. Both-results-recorded. Retract-by-Rule-12 if falsified; do NOT refill.

---

## 0. THE HYPOTHESIS UNDER TEST (Grant, test-blind)

Matter = standing / self-trapped waves = DC bias = per-channel saturation = **local stiffening**;
radiation = pure AC = zero time-averaged bias (the proven pump-nulls) = **no stiffening**.

If quantitative, this dissolves the two-operating-point tension (ρ=1 vacuum photon point / ρ≈9.77
matter point) into a **STATE DIAGRAM** (ρ=1 vacuum ground state ↔ ρ≈9.77 matter-loaded state) and
gives the /7 sector a candidate MECHANISM.

**The two anchor points (both cited from their branches, merge-state noted):**
- **Cold point ρ_bond = k_a/k_s = 1**, Ax3-forced KNOB-FREE — `research/2026-07-04_parent-condition-match-forces-balance_result.md`
  (PR #516, **UNMERGED at this HEAD**; cited from `origin/analysis/match-forces-balance`).
- **Stiff-matter point ρ* ≈ 9.7734** = the ν=2/7 ⟺ K=2G locus, **GR-imported** (NOT lattice-forced)
  — `research/2026-07-04_srs-elastic-tensor_result.md` (on main at this HEAD). **ρ* is K=2G
  RE-IMPORTED**; the crystalline substrate does not select it. This is the pre-registered knife:
  9.77 is a VISIBLE TARGET, so nothing is proven unless every input is canon-forced.

Both docs use the SAME definition ρ = k_a/k_s (verified: `srs-elastic-tensor:19`, `PR516:24`).

---

## 1. SUBSTRATE-FIRST SECTOR HEADER (declared before design)

- **SECTOR:** translational-u elastic sector of the ratified chiral srs-z3 net. RANK-2 bond tensor
  `Φ_b = k_a·d̂⊗d̂ + k_s·(I−d̂⊗d̂)` (`srs_bloch_dispersion.py:80`), NOT a Cartesian Laplacian.
  BOTH k_a (axial/longitudinal-compliance spring) and k_s (shear/bending spring) are
  **translational-u / capacitive** (PR516:81-88 — NOT the ε-vs-μ photon pair). ρ_eff modulates
  when the two capacitive springs saturate at DIFFERENT operating amplitudes.
- **REGIME:** this is an ANALYTIC / direct-kernel derivation (evaluate the canon saturation forms
  at declared operating points), NOT an fdtd or eigensolve run. Cold reference is A=0 ⟹ S=1 ⟹ ρ=1.
  Matter is the saturated operating point. Radiation control is the pure-AC (⟨A⟩=0) limit.
- **COORDS (A46):** ρ_eff is a dimensionless STIFFNESS RATIO; the kernel arguments A_axial, A_shear
  are phase-space/reactance operating-point amplitudes on the Ax4 arc (node-up §1 A46 note),
  NOT real-space lattice-Cartesian field magnitudes. Coordinate-clean.
- **CLASS (consistency-vs-emergence):** the direction/mechanism is a **MANIFESTATION** candidate
  (does Ax4 saturation drive ρ_eff the right way). The VALUE 9.77 is GR-imported (PR#506) — so an
  **EMERGENCE** grade (9.77 falls out knob-free) is only earned if the crossing amplitude is
  canon-distinguished. If the crossing amplitude is a free knob tuned toward 9.77, that is the
  import in a costume — booked as CONSISTENCY/QUALITATIVE, NOT emergence.

---

## 2. THE DERIVATION CHAIN (frozen — the canon-forced composition)

### Step 1 — HOW k_a and k_s saturate (per-channel S factors, canon-forced)

**Axial spring k_a** (longitudinal-A1 stretch compliance):
- TKI Capacitance↔Compliance identity: `C = ξ²·κ = ξ²/k` (`natural-units-cheatsheet.md:86`,
  `EE_TO_TOPO_CAPACITANCE`; `resonant-lc-solitons.md:12` `C_e ≡ ξ_topo²·k⁻¹`) — an IDENTITY
  statement ("not an approximation, not an analogy", `translation-circuit.md:41`).
- Divergent compliance form (Grant-ratified Q1=(B), `research/2026-06-15_ceff-epsilon-monotonicity_result.md`;
  `nonlinear-vacuum-capacitance.md:27`): `C_eff = C_0/S_axial`.
- ⟹ **k_a = ξ²/C_eff = k_{a,0}·S_axial** (axial stiffness SOFTENS as S_axial drops; the varactor
  runaway is the bond going compliant).

**Shear spring k_s** (deviatoric-G shear/bending):
- Shear modulus saturation (verbatim, `scale_invariant.shear_modulus_ratio`): `G/G_0 = S_shear`.
- Shear-grade speed (port map, `CLAUDE.md`:75): `c_shear = c_0·√S_shear`, and c² ∝ k_s/ρ.
- ⟹ **k_s = k_{s,0}·S_shear** (shear stiffness ALSO softens as S_shear drops).

**COMPOSITION (canon-derived, not guessed):**
> **ρ_eff = k_a,eff / k_s,eff = ρ_cold · (S_axial / S_shear)**

ρ_cold = 1 (Ax3-forced, PR#516). The ratio moves ONLY when S_axial ≠ S_shear — i.e. ONLY under
**asymmetric channel loading** (exactly Grant's hypothesis). Symmetric loading (S_axial = S_shear,
the R1 INVARIANT-S2 case, node-up §2) leaves ρ_eff = ρ_cold IDENTICALLY.

**EXPONENT-DEFECT FORK (carried, not resolved — flag-don't-fix).** The corpus carries a documented
`S^{0.25}` (engine) vs `S^{0.5}` (physical) exponent tension for the reflection index
(`cvr-reflection-smith.md:68`, `resonant-lc-solitons.md:112`). Both the axial-`C_0/S` and the
shear-`G/G_0=S` forms above are `S^{1}` in the STIFFNESS (linear), so the composition ρ_eff =
S_axial/S_shear is exponent-fork-independent at the stiffness level. Recorded; not silently picked.

### Step 2 — evaluate at the electron's canon operating points (BOTH channel-assignments, blind)

def-vyvsn1 (Grant-ratified 2026-06-30) fixes the operating points:
- **A1 mass core** operates at **A = V_yield/V_snap = √α ≈ 0.0854** (sub-saturated; S(√α) = √(1−α)
  ≈ 0.9963) — that is WHY it binds (the S→0 varactor runaway never fires on the mass channel).
- **T2 Cosserat self-trap wall** at **V_yield** (the confining Γ=−1 wall), which in the wall's own
  normalization is the **near-yield A→1** channel.

**Because the physical channel-assignment (which spring loads near-yield) is a framing fork
surfaced to Grant, run BOTH blind and report both profiles — do NOT pre-pick the one giving 9.77:**
- **Assignment SHEAR-LOADS (Grant-lean):** shear channel near-yield (S_shear = S(A_wall), A_wall→1);
  axial channel sub-saturated (S_axial = S(√α) ≈ 0.9963). ⟹ ρ_eff = 0.9963/S_shear (RISES).
- **Assignment AXIAL-LOADS (the anti-lean control):** axial near-yield (S_axial = S(A_wall));
  shear sub-saturated (S_shear = S(√α)). ⟹ ρ_eff = S_axial/0.9963 (FALLS toward 0).

Sweep A_wall over a canon-honest near-yield ladder approaching yield (report the PROFILE, not one
cherry-picked point). Use the same wall-amplitude ladder the corpus uses for near-yield regularization
(the nonlinear-vacuum-capacitance table: 0.5, 0.9, 0.99, 0.999, and interpolants).

### Step 3 — report

- DIRECTION (stiffening / softening) for each assignment.
- MAGNITUDE PROFILE ρ_eff(A_wall) for each assignment.
- The ρ*=9.77 CROSSING point IF any: at what A_wall does each assignment cross 9.77?
  Is that A_wall **canon-distinguished** (e.g. √α, or a def-vyvsn1 ladder rung) or **arbitrary**
  (a value only special because it hits 9.77)? — THE HONEST QUESTION, pre-registered.

### Step 4 — the radiation control (analytic)

Confirm that a **pure-AC traveling wave** (zero time-averaged amplitude ⟨A⟩=0) gives ρ_eff = ρ_cold
**identically**. Mechanism: the loading argument is the DC-bias operating point; a pure AC drive
pumps zero time-averaged displacement charge across the channel (`clm-clvchn`, displacement-PUMP
NULL-CONFIRMED-FINAL 2026-07-02, `project-cleave-01.md:40-59`) and, being symmetric-internal (R1,
node-up §2), gives S_axial = S_shear ⟹ ρ_eff = ρ_cold. Cite the pump-null provenance.

---

## 3. THE KNIFE (armed maximally — frozen)

ρ*≈9.77 is a VISIBLE TARGET. This derivation proves NOTHING unless every input is canon-forced.
**Ledger EVERY term** as canon-forced vs engineering-choice:
- kernel S(A) = √(1−(A/A_yield)²) — canon (Ax4).
- axial S mapping (C=ξ²/k, C_0/S) — canon (TKI identity + Q1=(B) ratification).
- shear S mapping (G/G_0=S, c=c_0√S) — canon (scale_invariant + port map).
- composition ρ_eff = S_axial/S_shear — DERIVED from the two mappings (not guessed).
- operating amplitudes (√α core; A_wall→1 wall) — canon (def-vyvsn1).
- **ANY free parameter tuned toward 9.77 = the import in yet another costume; book it as such.**
  In particular: if the 9.77 crossing lands at an A_wall that is NOT √α and NOT a def-vyvsn1 rung
  and NOT otherwise canon-distinguished, the crossing amplitude is a FREE KNOB — the value 9.77 is
  imported, and the strong (emergence/quantitative) bin is FORBIDDEN.

**½/¼ over-determination tell:** watch for a crossing that lands at exactly √α or 1−α or a clean
½/¼ — per `feedback_challenge_canonical_negative`, a suspiciously round crossing is a coincidence
tell to be scrutinized, not celebrated.

---

## 4. BINS (frozen)

- **[DRIVES-STIFF-QUANTITATIVE]** — right direction (ρ_eff rises) AND the 9.77 crossing at a
  **canon-distinguished** A_wall (√α, a def-vyvsn1 rung, or otherwise forced). The state-diagram
  reading lands. **Enormous if true — triple-check the ledger before claiming this.**
- **[DRIVES-STIFF-QUALITATIVE]** — right direction, crossing at an **arbitrary** A_wall.
  Mechanism candidate; VALUE still imported. (CONSISTENCY-class.)
- **[WRONG-DIRECTION]** — the canon composition softens where the hypothesis predicts stiffening.
- **[NO-SHIFT]** — ρ_eff = ρ_cold identically (symmetric loading / no asymmetry mechanism).
- **[STUCK-FRAMING → Grant]** — the channel-assignment fork or the composition cannot be closed
  from canon without a Grant framing ruling.

**Compound bins allowed** (e.g. SHEAR-LOADS = QUANTITATIVE while AXIAL-LOADS = WRONG-DIRECTION is
a legitimate both-recorded outcome — the substrate distinguishing the assignments IS a result).

---

## 5. VALIDATION HARNESS (frozen — Rule 10, run BEFORE reading the verdict)

1. **Cold recovery:** at A_axial = A_shear = 0, ρ_eff = 1.0 to machine precision (both assignments).
2. **Symmetric-loading null:** S_axial = S_shear (any A) ⟹ ρ_eff = ρ_cold = 1 identically (the
   R1/INVARIANT-S2 / radiation-control check).
3. **Kernel identity:** S(√α) = √(1−α) reproduced from `scale_invariant.saturation_factor`.
4. **Monotonicity:** ρ_eff(A_wall) monotone in A_wall for each assignment (no non-physical folds).
5. **Composition cross-check:** k_a = ξ²/C_eff with C_eff = C_0/S reproduces k_a = k_0·S
   independently (guards the compliance-inversion sign — the one place a sign error hides).
6. **Anti-tune guard:** the driver takes NO free ρ*-target parameter; 9.77 enters ONLY as a
   read-off comparison constant, never as an input the sweep is fit to.

All numerics through the validation harness; HALT if any validate-on-known fails.

---

## 6. CITES (verified at HEAD 2a09dc82, grep-checked 2026-07-04)

- Cold anchor ρ=1 (PR#516, unmerged): `origin/analysis/match-forces-balance:research/2026-07-04_parent-condition-match-forces-balance_result.md`
- Stiff anchor ρ*≈9.77 GR-imported (PR#506, on main): `research/2026-07-04_srs-elastic-tensor_result.md:19,94,119`
- Port map / per-channel S factors: `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md:45-51`
- TKI C=ξ²/k identity: `manuscript/ave-kb/common/natural-units-cheatsheet.md:86`; `resonant-lc-solitons.md:12`
- Axial C_0/S + Q1=(B): `nonlinear-vacuum-capacitance.md:27`; `research/2026-06-15_ceff-epsilon-monotonicity_result.md:81`
- Shear G/G_0=S: `src/ave/axioms/scale_invariant.py:56` (`shear_modulus_ratio`)
- def-vyvsn1 operating points (√α core / T2 wall): `nonlinear-vacuum-capacitance.md:18,36,40`
- Kernel S(A): `src/ave/axioms/scale_invariant.py:38` (`saturation_factor`)
- Pump-null (radiation control): `clm-clvchn`, `project-cleave-01.md:40-59`
- Bond tensor Φ_b: `src/scripts/vol_4_engineering/srs_bloch_dispersion.py:80`
- Exponent-defect fork (carried): `cvr-reflection-smith.md:68`; `resonant-lc-solitons.md:112`
