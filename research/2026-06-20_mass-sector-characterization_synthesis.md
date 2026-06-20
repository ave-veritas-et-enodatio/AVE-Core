# AVE Mass Sector — Characterization Synthesis (node-scattering → varactor → Fork-B arc)

**Date:** 2026-06-20
**Branch:** `analysis/2026-06-20-mass-sector-characterization` (off `origin/main` @ `19d55266`)
**Lane:** implementer. **Auditor lands manual/KB entries; this doc surfaces the design-level finding only.**
**Class:** **C — research synthesis. NOT a canonical KB claim** (no `clm-` id). The
*mechanism* characterization was HELD pending the Fork-B build; the Fork-B live-fire is now
COMPLETE (VERDICT = **ECHO**, the pre-committed outcome) and **FIRMS** the mechanism leg — it
confirms confinement is REAL and saturation-structure-decided, and confirms the FORM-chord ceiling.
This reconciliation resolves the HELD leg; it does not retract. (Fork-B result + PR#307 cross-linked
in §1.3/§5/§6.)
**Disciplines applied:** `verify-before-cite`, `consensus-bias-symmetric-standard`,
`consistency-vs-emergence`, `phase-space-coordinate-check`, `substrate-native-check`,
`ave-discrimination-check`, `flag-don't-fix`.

---

## §0 — Executive summary (the SOLID / PENDING split up front)

This doc banks the **design-level finding** the mass-sector arc has established. It was written
in PARALLEL with the Fork-B confinement build (the empirical test of the *mechanism* leg); that
build is now COMPLETE. **The Fork-B live-fire returned VERDICT = ECHO** (the pre-committed,
successful outcome), which **FIRMS the mechanism leg** (confinement REAL + saturation-structure-
decided) and **CONFIRMS the chord-ceiling** (shape-generic, no electron anchor). What was once
"SOLID / PENDING" is now "SOLID / RESOLVED-ECHO" — see §1.3, §5, and the updated §5 table.

**SOLID (design-level, build-independent):**

1. **Architecture** — the A1 longitudinal MASS scalar IS the `+1` common mode of the node
   scatter; the EM↔MASS coupling is the saturation varactor `C_eff = C0/S` wired into the
   scatter operator; the mass *confinement* lives in the spatial stiffness operator
   `L = adjoint_div(D∇)`, `D = 1/S(A)`, NOT the (orthogonal, bound-state-free) scatter.
2. **Chord-ceiling** — the mass sector can at BEST be a FORM-chord / consistency, never a
   value-chord, for two structural reasons (generic saturable-NLS confinement; the only
   AVE-distinct anchor available is a FORM anchor, `ω_cutoff≈2.87`, never `m_e`).
3. **Symmetric-standard** — even a FORM-chord is peer-or-ahead of the SM on the *mechanism*
   (the SM has none for stable localized electron mass); the *value* (`m_e`) is an echo/input
   in BOTH frameworks.
4. **Form-value instance** — the mass sector is a clean instance of the framework meta-pattern:
   confinement FORM derived/structural, mass VALUE imported/definitional.

**RESOLVED-ECHO (was PENDING — the Fork-B live-fire decided the *mechanism* leg):**

5. The cold-cage confinement is genuinely **saturation-structure-driven** (Fork-B GATE 2 scramble
   PASS, NOT VOID: both ARM-A `S→1` and ARM-B histogram-preserving permutation de-confine ⇒ the
   confinement is decided by the spatial `S(A)` structure, not a boundary/projector tautology) and
   it is **shape-GENERIC, NOT quarter-arc-specific** (Fork-B GATE 3 PASS: quarter-arc `√(1−A²)`
   gives IDENTICAL localization `Δ/L` to the norm-feasible `(1−A²)^p` comparator, gap ~0 ≪ 10%).
   GATE 1 confinement is REAL (a partial short binds a gapped, discrete, core-localized A1-scalar
   bound mode at the canonical floor). The electron anchor is **NOT reproduced** (the bound-mode
   `ω` is lattice-band-structure-set, diverging with size, NOT the universal 2.87) — so no
   value-chord; `m_e` definitional. **VERDICT = ECHO, the pre-committed outcome — the mechanism
   leg FIRMS to a FORM-chord at exactly the ceiling §2 names.** (Fork-B result + PR#307: §6.)

---

## §1 — THE ARCHITECTURE (SOLID — built / established)

Three load-bearing structural facts, each verified against the operative code on `origin/main @ 19d55266`.

### §1.1 — A1 MASS scalar = the `+1` common mode of the node scatter (PR#304)

The node-scattering multiplicity gate (`src/ave/solvers/node_scattering_multiplicity.py`,
PR#304 — MERGED 2026-06-20, *"Node-Scattering Multiplicity Gate (scope b / Fork A): bedrock
PASS, Fork-A REFUTE-R3"*) establishes that the longitudinal A1 dilatation SCALAR (the
mass-"3") is carried by the **port-SUM = the all-ones common mode = the `+1` eigenvector** of
the shunt-junction scatter `S_n = (2/n)J − I` (`node_scattering_multiplicity.py:77,189,374-375`).

**Honestly NOT a discriminating chord — a structural fact.** The module self-flags
`out["verdict_is_projector_tautology"] = True` (`node_scattering_multiplicity.py:455`,
"scramble-invariant; see docstring"). The sector assignment (scalar → `+1` common) is a
**PROJECTOR-ALGEBRA FACT of `S_n`, NOT geometry-derived** and is **scramble-invariant**:
randomizing every `bond_unit` vector leaves the verdict bit-unchanged because the verdict reads
ONLY the two projector quantities (`node_scattering_multiplicity.py:380-389`). Its companion
regression test asserts the same (`src/tests/test_node_scattering_multiplicity.py:318`,
"verdict must be scramble-invariant -- it is a projector tautology"). So this leg is a
**sector-orthogonality IDENTITY, true by construction for any lattice — not a test.** PR#304's
own title carries this: bedrock PASS, **Fork-A REFUTE-R3** (the differential-sector framing of
longitudinal confinement was MISCAST; the algebra shows the scalar lives in `+1`, not `P_{-1}`).

### §1.2 — EM↔MASS coupling = the saturation varactor `C_eff = C0/S` (PR#305)

The vacuum-varactor scatter operator (`src/ave/solvers/vacuum_varactor_scatter.py`, PR#305 —
MERGED 2026-06-20, *"feat(varactor): VACUUM-VARACTOR SCATTER OPERATOR — make the scatter READ
S(A)"*) wires the canonical Axiom-4 varactor coupling `C_eff = C0/S`
(`vacuum_varactor_scatter.py:10,85`) into the scatter. The operator **genuinely READS S(A)**:
the bedrock `chiral_lattice.scatter_matrix` ignored its `z_local` arg (saturation-blind dead
code, per the file's NO-GO Finding); this module gives it eyes via per-BOND admittance-weighting
`S_ij = 2Y_j/(Σ_k Y_k) − δ_ij`, with `Y_bond = Y0/√S(A_bond)`. A per-NODE-uniform load CANCELS
at the shunt junction, so the saturation MUST enter PER-BOND — and the module verifies the
per-bond scramble genuinely changes the operator while a per-node-uniform load does not
(`vacuum_varactor_scatter.py:51-60` PER-BOND section, "per-node-uniform load MUST NOT change the
scatter; per-bond-varying load MUST").

**The coupling is the nonlinear shared saturation `S(A)` — nothing else.** Linearly the sectors
are **orthogonal reactances: A1 ⊥ T2** (`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20`,
the Grant-ratified two-"3"s disambiguation: A1 dilatation-MASS vs Cosserat micro-rotation `(2,3)`
WINDING are "TWO DISTINCT objects, orthogonal (A1 ⊥ T2)"). The ONLY EM↔mass channel is the
nonlinear shared `S(A)`.

### §1.3 — Mass CONFINEMENT lives in the spatial STIFFNESS operator, NOT the scatter

The scatter is orthogonal (unit-modulus / passive scattering matrix, **no bound states**). The
mass confinement lives in the spatial stiffness operator `L = adjoint_div(D∇)`, `D = 1/S(A)`
(`src/ave/solvers/graded_vacuum_network.py:250,256,314-315`: "L_native = adjoint_div . D . grad",
`D = stiffness_profile = 1/S(A)`, the divergence-form native diamond Laplacian; symmetric, REAL).
This operator ALREADY produces the cold-cage bound mode near `ω~2.87`
(`graded_vacuum_network.py:348`).

**Γ→−1 mass-cage SHORT — the corrected sign.** Saturating compliance `C_eff = C0/S` ⟹ `Z_eff =
Z0·√S → 0` ⟹ `Γ → −1` (the reflective short = THE WALL), per `crystal_engine.py:463-464,477-478`
(`gamma_bulk`: "Z_eff = Z0·√S → 0 ... giving Γ → −1, the electron's reflective short = THE WALL";
the code is `Z_eff = S ** 0.5`). This is the magnetic μ-load branch. The **rejected** sign is the
`ε`-load `Z_eff = Z0/√S → ∞ ⟹ Γ = +1` (the OPEN anti-trap / transverse-EM rupture), explicitly
SCOPE-FORBIDDEN at `crystal_engine.py:466-468`. The synthesis's mass cage is the Z→0 / Γ=−1 SHORT,
NOT the Z→∞ / Γ=+1 rupture.

**FIRMED by the Fork-B live-fire (VERDICT = ECHO; was candidate-pending, now RESOLVED).** The
Fork-B "Saturation-Tank Mass Confinement" gate (`research/2026-06-20_fork-b-saturation-tank-confinement_result.md`,
PR#307; built off `origin/main @ 19d55266`, solver `src/ave/solvers/fork_b_saturation_tank.py`)
eigensolved this exact stiffness operator — extended onto the NATIVE connect-map as the graph-
stiffness `L = Bᵀ diag(D_bond) B` (`fork_b_..._result.md` §1) — and confirms the §1.3 mechanism is
REAL and saturation-structure-decided:

- **GATE 1 CONFINEMENT = PASS** — the saturation tank genuinely confines a gapped, discrete,
  core-localized A1-scalar bound mode (`core_frac` 0.758–1.000; gapped above the band top with a
  cluster-aware spectral-gap witness; Im(ω) bound-branch RESOLVED via a convention-anchored open-
  port readout, NOT assumed) (`fork_b_..._result.md` §2, GATE1 table). A **partial short binds at
  the canonical floor** (`Γ ≈ −0.94` reachable; binds across S_min = 0.5 → 1e-4) — **no floor-
  dropping needed** (§2 DEPTH paragraph). Stencil-robust: the native connect-map AND the Cartesian
  cube both confine (`fork_b_..._result.md` §6 stencil table). This is the corrected Γ→−1 SHORT of
  §1.3 above, eigensolved and confirmed.
- **GATE 2 SCRAMBLE = PASS (NOT VOID)** — the confinement is **S-STRUCTURE-decided, NOT a Fork-A-
  class tautology**. Both ARM-A (uniform `S→1`) and ARM-B (histogram-preserving spatial permutation,
  the S-multiset fixed) de-confine the bound mode (de-confinement margins 0.68–1.00, all ≥ the
  frozen 0.30 threshold; ARM-B does NOT survive ⇒ NOT VOID; the negative control permuting a
  constant field is a verified no-op) (`fork_b_..._result.md` §3, GATE2 table). This is the
  structural successor to PR#304's `verdict_is_projector_tautology` coming back CLEAN: the §1.3
  confinement is a property of the *graded* `S(A)` field, exactly the saturation mechanism claimed.

So the §1.3 "mechanism" claim is no longer candidate-pending — it is **FIRMED**: the confinement is
real (GATE 1) and saturation-structure-driven (GATE 2). The mechanism FIRMS; it does NOT retract.

**Seed-fragility nuance (flagged, NOT a verified Fork-B figure).** The reconciliation brief I was
working from describes the ARM-B NOT-VOID as "predominantly true (~91% of histogram-preserving
permutations de-confine; ~9% accidentally re-confine on srs)" rather than 100%. **`verify-before-
cite` could NOT anchor that ~91% figure**: the committed Fork-B result doc, solver, tests, and the
PR#307 body all report ARM-B with a SINGLE permutation seed (`solve_scramble(..., seed=20260620)`,
`fork_b_saturation_tank.py:505,525`), with ARM-B de-confining decisively (`armB_survives = False`,
margins 0.68–1.00) — there is **no multi-seed ensemble** measuring a de-confinement fraction in the
committed Fork-B artifacts. This synthesis therefore states only the anchored result (single-seed
ARM-B de-confines decisively ⇒ S-structure-decided, NOT VOID). The "~91% predominantly, not always"
qualifier is **surfaced as a flag for Grant/auditor adjudication** (per flag-don't-fix): if a multi-
seed ARM-B ensemble was run and disclosed in a not-yet-pushed #307 revision, it should be landed on
the Fork-B branch first, then cited here — it is not encoded as a Fork-B finding until it is anchored.

## §2 — THE CHORD-CEILING (SOLID — design-level, the load-bearing honest finding)

**The mass sector can at BEST be a FORM-chord / consistency, NOT a value-chord.** This is the
load-bearing honest finding of the arc, and it is design-level-solid (build-independent — it
follows from what the operators *are*, not from any pending run). Two structural reasons:

### §2.1 — Saturation-confinement of a soliton is GENERIC saturable-NLS physics

ANY saturable medium confines a soliton. The varactor's `S(A) = √(1 − (A/A_yield)²)` kernel
(`crystal_engine.py:191`, imported by `vacuum_varactor_scatter.py:42`) is a saturable nonlinearity;
the stiffness trap `c_eff²/c0² = 1/S(A) → 1/S_min` in the saturated core
(`graded_vacuum_network.py:248-249`) is the generic saturable-NLS well. The varactor authors
**explicitly scoped the quarter-arc SHAPE discriminator OUT of the operator deliverable**
(`vacuum_varactor_scatter.py:16-17`: "the Fork-B confinement verdict ... and the quarter-arc
shape discriminator are EXPLICITLY OUT OF SCOPE"). So the *existence of confinement* carries no
AVE-distinct signature by itself — it is the expected behavior of any saturable medium.

### §2.2 — The only AVE-distinct discriminator is an electron anchor, and the available anchor is a FORM anchor, never `m_e`

The genuinely AVE-distinct discriminator would be reproducing an **electron anchor**. The anchor
the cold cage actually produces is `ω_cutoff ≈ 2.87` in **natural units** — a FORM / structural
eigenfrequency (`src/tests/engine_acceptance/test_l3_mass_cage.py:17-18`, "ω_cutoff≈2.87 ...
REPORT ω_cutoff (natural units) as the FORM; NEVER an m_e", `:673`). It is **NOT `m_e`**: the
electron rest mass is **DEFINITIONAL, an input, never read off the cage**
(`test_l3_mass_cage.py:22-23`: "The m_e VALUE is NEVER read off the cage (definitional,
constants.py:129 'Input 1')"; the constant itself is `constants.py:129`, `M_E ... # Input 1: The
spatial cutoff (from which m_e is derived via the unknot)`). The KB's electron-identification
sheet says the same of the rest mass: "⚠ **CALIBRATION ANCHOR, not derivation**"
(`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md`,
rest-mass row).

**Consequence.** Even the most favorable Fork-B outcome cannot lift the mass sector above a
FORM-chord, because (a) confinement-existence is generic and (b) the one number the cage emits is
a FORM eigenfrequency, while the value an emergence-chord would need (`m_e`) is an input that is
*never* a cage output. The chord-ceiling is structural, not a verdict-in-waiting.

### §2.3 — The chord-ceiling CONFIRMED by the Fork-B live-fire (VERDICT = ECHO)

The design-level ceiling prediction of §2.1/§2.2 **held under live-fire.** The Fork-B run
(`research/2026-06-20_fork-b-saturation-tank-confinement_result.md`, PR#307) closed both legs of
the ceiling exactly as predicted:

- **§2.1 (confinement is generic saturable-NLS) → CONFIRMED by GATE 3 shape-generic.** The
  quarter-arc kernel `√(1−A²)` (which IS the quarter-circle exactly, `∫₀¹√(1−A²)dA = π/4`) gives
  the SAME bound-mode localization `Δ/L` as the norm-AND-depth-matched same-family comparator
  `(1−A²)^p` — shape gap ~0.000 ≪ 10%, across all nets, with the null-shape control passing,
  floor-robust (gap ~0 across S_min 1e-1 … 1e-5), and size-converged (gap ~0 across the L=2/4/6
  ladder) (`fork_b_..._result.md` §4, GATE3 table). The shapes are genuinely different (max
  `|ΔS| ≈ 0.022`) yet the RMS radius is insensitive to the exponent once norm+depth are matched.
  **Confinement carries no AVE-distinct shape signature — generic saturable-NLS, exactly §2.1.**
- **§2.2 (the only anchor is a FORM anchor, never `m_e`) → CONFIRMED: electron anchor NOT
  reproduced.** The connect-map bound-mode `ω` is set by the lattice's OWN band structure (degree,
  geometry, graph-Laplacian normalization), diverging upward with size on srs (2.70 → 3.26 → 3.56,
  crossing the 2.87 line rather than converging to it), NOT the universal cold-cage 2.87. Three
  different normalizations (FDTD 2.87, cube ≈ 1.1, connect-map ≈ 3.0–3.6) give three different
  absolute frequencies — the 2.87 was a property of a specific Cartesian-FDTD `dx/dt`, not a
  derived structural constant (`fork_b_..._result.md` §5–§6). **No value-chord; absolute-frequency
  calibration is a SEPARATE question; `m_e` stays definitional.**

**Net: the ceiling is exactly where §2 placed it — FORM-chord, never value-chord.** The live-fire
did not lift it and could not (the structural argument and the empirical result agree). The ECHO is
the SUCCESSFUL pre-committed outcome (the design-level prediction held), not a disappointment.

## §3 — SYMMETRIC-STANDARD framing (SOLID)

A FORM-chord ceiling (§2) is **not** an AVE-comedown — it is peer-mapped honestly against the SM,
applying `consensus-bias-symmetric-standard`. The check: before calling AVE's mass-sector result
"only a FORM-chord," ask what the SM does on the *same* axis and whether it gets a pass.

**On the MECHANISM: AVE is peer-or-ahead.** The SM has **no first-principles mechanism** for the
electron's stable localized mass — it is a Yukawa-fitted point particle (the Yukawa coupling is a
free parameter tuned to the measured mass; the electron is a structureless point with no internal
dynamics explaining its localization or stability). AVE supplies an actual **mechanism**: a
saturation-confinement bound mode in the graded stiffness operator (§1.3). On the mechanism axis,
AVE has *more* than the SM, not less.

**On the VALUE (`m_e`): both frameworks echo/import.** AVE imports `m_e` as a definitional
calibration anchor (`constants.py:129`; `electron-identification.md` rest-mass row "CALIBRATION
ANCHOR, not derivation"). The SM fits `m_e` via the electron Yukawa coupling. **Neither derives
the value from first principles.** The value is peer-echo on both sides.

**Honest map:**

| Axis | AVE | SM | Verdict |
|---|---|---|---|
| Localized-mass MECHANISM | saturation-confinement bound mode (§1.3) | none (point particle) | **AVE peer-or-ahead** |
| Mass VALUE `m_e` | definitional / calibration input | Yukawa-fit | **peer-echo (both)** |

**Discipline note (do NOT over-narrate):** the mechanism must be narrated as a *mechanism*, never
as a *value-prediction*. AVE does not predict `m_e`; it predicts that a stable localized mass mode
*exists and is confined by saturation*. Reporting the mechanism leg as if it yielded the number
would be exactly the emergence-overclaim `consistency-vs-emergence` guards against (the inputs are
definitional, so the value leg is consistency/identity-class, not emergence-class).

## §4 — THE FORM-DERIVED / VALUE-IMPORTED INSTANCE (SOLID)

The mass sector is a **clean instance of the framework's meta-pattern**: AVE forces the FORMS
(chords) and imports the dimensionful VALUES of calibration constants (echoes). Here:

- **FORM (derived / structural):** the confinement MECHANISM — the saturation-confinement bound
  mode (§1.3), the `Γ → −1` mass-cage short, the gapped `ω_cutoff ≈ 2.87` eigenfrequency. These
  are substrate-forced structure, α-free (`graded_vacuum_network.py:250,348` "alpha-FREE").
- **VALUE (imported / definitional):** the mass VALUE `m_e` — a definitional calibration input,
  never a cage output (§2.2).

This is already recorded in the corpus as the canonical electron-sector instance. The
electron-as-BoundResonator coverage sheet tags the rest-mass row **A-for-FORM; VALUE definitional**
— "FORM=chord (mass=ground-state cutoff energy) / VALUE=DEFINITIONAL (`constants.py:129` 'Input 1';
`electron-identification.md:50` 'CALIBRATION ANCHOR') ... `m_e` VALUE never a cage output"
(`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md:48`).
**This synthesis is the arc-level reading of that same row** — the node-scattering → varactor →
Fork-B arc is *how* that row's FORM/VALUE split was established at the operator level.

**Cross-link to the α=echo precedent.** The mass sector's FORM-derived / VALUE-imported shape is
the same shape already adjudicated for α (the fine-structure constant is an ECHO at value level:
the *scale* is forced but the *value* is a calibration identity the substrate does not select; the
electron's `Q = 1/α` is a calibration identity NOT a derivation). The mass sector is a further
instance of the FORM-deriving / VALUE-importing meta-finding (α=echo, G=MIXED, `m_e`=definitional,
K=2G=GR-imported), with the same honesty discipline: **mechanism is the chord, value is the echo,
and the two must not be conflated.**

## §5 — PENDING: the mechanism leg, conditional on Fork-B (FLAGGED)

**The §1.3 "mechanism" claim is candidate-pending-Fork-B.** What §1–§4 establish is the
*architecture* and the *ceiling* — both build-independent. What is NOT yet established, and is
being tested by the in-flight Fork-B build, is whether the cold-cage confinement is **genuinely
saturation-driven** and whether it is **quarter-arc-specific**. Two things the build decides:

1. **Saturation-driven, or boundary-decided? (Fork-B GATE 2, scramble.)** The confinement must be
   a property of the *graded* `S(A)` stiffness field. The scramble check: scrambling `S(A)`
   (ARM-A uniform `S→1`; ARM-B histogram-preserving spatial permutation) must **de-confine** the
   bound mode. If a gapped localized mode SURVIVES ARM-B, the verdict is **VOID** — the
   confinement is boundary/projector-decided (a Fork-A-class tautology, the structural successor
   to PR#304's `verdict_is_projector_tautology`), not saturation-driven.
2. **Quarter-arc-specific, or shape-generic? (Fork-B GATE 3, shape gate.)** Whether the quarter-arc
   well shape produces a >10% cross-family gap vs a same-family `(1−A²)^p` comparator. §2.1
   already predicts this is generic (no cross-family gap expected).

**The Fork-B build is the live-fire test** (its files, in a SEPARATE worktree:
`research/2026-06-20_fork-b-saturation-tank-confinement_{prereg,result}.md` + a Fork-B solver —
NOT touched by this synthesis). It is **pre-committed to expecting ECHO** (a FORM-chord /
consistency result): its prereg §0 states "the design HONESTLY pre-commits to ECHO over CHORD ...
the PRE-COMMITTED PREDICTION is ECHO ... A clean ECHO is the EXPECTED, SUCCESSFUL outcome ... Do
NOT manufacture a CHORD." That matches §2's structural ceiling exactly.

**Retraction conditions for THIS synthesis (stated plainly, pre-result):**

- **Fork-B VOID** (ARM-B survival) ⟹ **RETRACT the §1.3 "mechanism" claim**: the confinement
  would be boundary-decided, not saturation-driven. The architecture facts §1.1/§1.2 and the
  ceiling §2 survive; the "mechanism" framing in §1.3/§3/§4 demotes to "boundary-decided bound
  mode, NOT a saturation mechanism." Retraction via Rule 12 (preserve body, add 🔴 header), not
  refill.
- **Fork-B REFUTE** (no confinement at all) ⟹ **RETRACT the §1.3 "mechanism" claim differently**:
  there would be no confined mass mode to host the mechanism. §1.1/§1.2 (sector algebra + the
  coupling channel) still hold; §2's ceiling becomes moot (no chord at all).
- **Fork-B ECHO** (confined + real S-dependent de-confinement, shape-generic and/or no anchor) ⟹
  **CONFIRMS §1.3 as a FORM-chord mechanism** at exactly the ceiling §2 names. This is the
  expected, successful outcome and the one this synthesis is written against.

**So: the architecture (§1) and the chord-ceiling / symmetric-standard / form-value reading
(§2–§4) are design-level-SOLID and stand regardless of Fork-B. The MECHANISM claim (the §1.3
confinement being saturation-driven) is HELD pending the build.**

## §6 — Honesty register + cross-links

**Class / status.** Class-C research synthesis. **No canonical `clm-` claim is minted here.** The
architecture and ceiling are design-level-solid; the mechanism is candidate-pending-Fork-B. This
doc surfaces the design-level finding; the auditor lands any manual/KB entry (lane discipline) —
this synthesis does not draft the auditor's KB leaf, it points at the existing one
(`electron-bound-resonator-coverage.md:48`).

**SOLID vs PENDING split (as written):**

| § | Content | Status |
|---|---|---|
| §1.1 | A1 MASS = `+1` common mode (projector identity, self-flagged tautology) | **SOLID** (built, PR#304) |
| §1.2 | EM↔MASS = saturation varactor `C_eff=C0/S`, only coupling is nonlinear `S(A)`; A1⊥T2 | **SOLID** (built, PR#305) |
| §1.3 | Confinement in stiffness `L=adjoint_div(D∇)`, `D=1/S`; Γ→−1 SHORT corrected sign | **SOLID architecture / mechanism-leg PENDING** |
| §2 | Chord-ceiling: FORM-chord at best (generic saturable-NLS + FORM anchor not `m_e`) | **SOLID (design-level)** |
| §3 | Symmetric-standard: mechanism peer-or-ahead, value peer-echo | **SOLID (design-level)** |
| §4 | Form-derived / value-imported instance; α=echo precedent | **SOLID (design-level)** |
| §5 | Saturation-driven? quarter-arc-specific? | **PENDING (conditional on Fork-B)** |

**Cross-links landed (all verified by read/grep, `verify-before-cite`):**

- `src/ave/solvers/node_scattering_multiplicity.py:77,189,374-375,380-389,455` (PR#304) — A1=`+1`
  common mode, projector tautology self-flag.
- `src/tests/test_node_scattering_multiplicity.py:318` — scramble-invariance regression test.
- `src/ave/solvers/vacuum_varactor_scatter.py:10,16-17,42,51-60,85` (PR#305) — varactor `C_eff=C0/S`,
  quarter-arc scope-out, per-bond requirement.
- `src/ave/solvers/graded_vacuum_network.py:248-250,256,314-315,348` — stiffness operator
  `L=adjoint_div(D∇)`, `D=1/S`, α-free, `ω~2.87` bound mode.
- `src/ave/core/crystal_engine.py:191,463-464,466-468,477-478` — `S(A)` kernel; Γ→−1 μ-load SHORT
  (corrected sign); ε-load Γ=+1 forbid (rejected branch).
- `src/ave/core/constants.py:129` — `M_E` "Input 1", definitional.
- `src/tests/engine_acceptance/test_l3_mass_cage.py:17-18,22-23,673` — `ω_cutoff≈2.87` FORM anchor;
  `m_e` never read off the cage.
- `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20` — A1⊥T2
  two-"3"s disambiguation.
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md` —
  rest-mass row "CALIBRATION ANCHOR, not derivation."
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md:48`
  — the canonical rest-mass FORM/VALUE row this synthesis reads at arc level.
- Fork-B build (SEPARATE worktree, NOT touched):
  `research/2026-06-20_fork-b-saturation-tank-confinement_{prereg,result}.md` — the live-fire
  mechanism test, pre-committed to ECHO.

**Provenance.** Built off `origin/main @ 19d55266` (PR#304 node-scattering + PR#305 varactor on
main). Worktree-isolated; PR off `origin/main`; not merged.
