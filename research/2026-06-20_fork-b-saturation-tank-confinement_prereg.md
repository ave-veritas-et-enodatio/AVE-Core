# Pre-Registration — Fork-B "Saturation-Tank Mass Confinement" Gate

**Frozen:** 2026-06-20 (this file is the FIRST commit of branch
`analysis/2026-06-20-fork-b-saturation-tank-confinement`; the frozen commit hash
is recorded in the result doc once committed).
**Built off:** `origin/main @ 19d55266` (PR#305 — the varactor scatter kernel is
on main; this branch extends `graded_vacuum_network.py`, NOT the scatter matrix).
**Lane:** implementer. **Auditor lands manual/KB entries; this doc surfaces the
empirical finding only.**

---

## 0. THE HONEST PRE-COMMITMENT (read this first — Rule 11 / consensus-bias-symmetric-standard)

This gate is built **eyes-open that the design HONESTLY pre-commits to ECHO over
CHORD** (Grant chose option A: build it, scoped tight). The pre-committed
expectation, stated BEFORE the run so it cannot be moved:

- **Confinement EXISTS** (high confidence) — the cold-cage already produces a
  gapped bound mode (`test_l3_mass_cage.py:17-18`, ω_cutoff≈2.87). GATE 1 is
  expected to PASS.
- **Scramble DE-CONFINES** (high confidence, *not* a tautology) — the bound mode
  is a property of the *graded* stiffness field S(A); destroying the spatial
  S-structure (ARM-A uniform, ARM-B histogram-preserving permutation) should
  remove the gapped localized mode. If it does NOT, the verdict is **VOID**
  (BC/projector-decided tautology), not a negative.
- **Shape gap is expected BELOW 10%** — the quarter-arc is a *generic saturable-NLS*
  well shape; a same-family comparator `(1−A²)^p` is expected to reproduce the
  Δ/L within the null-control band. The CHORD requires a >10% cross-family gap
  AND the electron anchor; **neither is expected.**
- **The electron anchor is REQUIRED for CHORD, not bonus, and is NOT expected** —
  the converged bound mode must reproduce the cold-cage `ω_cutoff≈2.87` WITHOUT
  α-import. This is a FORM/structural anchor, NOT m_e (which is definitional).

**Therefore the PRE-COMMITTED PREDICTION is ECHO** (confined + real S-dependent
de-confinement, but shape-generic and/or no-anchor → a FORM-chord / consistency
result, peer-mapped no-worse-than-SM). A clean ECHO is the EXPECTED, SUCCESSFUL
outcome. A VOID or REFUTE is also a valid honest result. **Do NOT manufacture a
CHORD.**

Symmetric-standard note (consensus-bias-symmetric-standard): a FORM-chord ceiling
here is no worse than the SM, which does NOT derive α, fits the Yukawas, and does
not explain charge quantization. The ECHO label is peer-mapped-honestly, not an
AVE-comedown.

---

## 1. SCOPE & ARCHITECTURE (the load-bearing correction — do NOT get this wrong)

**Confinement** (normalizable / gapped / Im(ω)) is a property of the **SPATIAL
STIFFNESS operator** `L = adjoint_div(D ∇)`, `D = 1/S(A)` — which ALREADY reads
S(A) and ALREADY produces the cold-cage bound mode (`graded_vacuum_network.py`,
the divergence-form native Laplacian). This gate **EXTENDS its eigensolve onto
the native connect-map.**

The PR#305 scatter operator (`vacuum_varactor_scatter.py`) is **ORTHOGONAL**: its
spectrum is unit-modulus (a unitary/passive scattering matrix), it has **NO bound
states**. We do **NOT** eigensolve the scatter matrix for confinement. We import
the PR#305 canonical `S(A)` kernel (`crystal_engine.saturation_kernel` via
`vacuum_varactor_scatter.saturation_kernel`) as the **SINGLE S(A)
source-of-truth** (ave-canonical-source).

**Operator scope (substrate-native-check):** the eigensolve is built on the REAL
`build_srs_net` / `build_diamond_net` **CONNECT-MAP** (native graph-Laplacian
`L = Bᵀ diag(D_bond) B`, B the signed node-bond incidence). The shipped
`graded_vacuum` L is on a Cartesian `(N,N,N)` cube (`TETRA_OFFSETS` + `np.roll`,
Cartesian-Gaussian core); if used at all it is scoped EXPLICITLY as a
Cartesian-embedded approximation and FLAGGED (structural-null-stencil-lens).

**Sector-projection guard:** the bound mode must live in the common-mode / scalar
A1 grade (the dilatation MASS-"3"), NOT leaked into the differential / shear
(micro-rotation CHARGE-"3"). A1 ⊥ T2 (master-equation.md:20). Explicit check:
the operator acts on a SCALAR node field; we confirm the bound eigenvector is a
common-mode (sign-coherent radial) profile, not a shear/curl pattern.

---

## 2. THE THREE ORDERED GATES (VOID-check first, then REFUTE, then CHORD-requires-all)

### GATE 1 — CONFINEMENT (necessary)

Eigensolve `L` on the **saturated core** (a localized region where A→A_yield,
S→0, Γ→−1). **CONFINED** requires ALL three:

- **(a) core_frac ≥ 0.50** — *[RF-1: OVERRIDE the live selector floor `core_frac>0.05`
  at `graded_vacuum_network.py:425,514` — too loose; use ≥0.50.]* The bound-mode
  eigenvector's `|ψ|²`-fraction inside the saturated-core support must be ≥ 0.50.
- **(b) SPECTRALLY GAPPED + discrete** — *[RF-2: BUILD the spectral-gap + discreteness
  witness IN the eigensolve selector; do NOT cite the time-domain '456' peak/mean
  — that is a ringdown observable (`_bulk.py:443 peak_mean`), not an eigensolve
  one. Replace `omega_guess=2.87` with a saturated-mode-derived guess or
  guess-ladder.]* Witness: the bound eigenvalue `ω²_bound` sits in the gap below
  the lowest continuum band edge `ω²_cont_min` by a margin
  `gap = (ω²_cont_min − ω²_bound)/ω²_cont_min`; AND the bound level is isolated
  (`discreteness = (ω²_next − ω²_bound)/ω²_bound` exceeds the mean continuum
  level-spacing). Both computed from the eigensolve spectrum, NOT the FFT.
- **(c) Im(ω) sign correct** — *[RF-3: the live solver DISCARDS the sign via
  `abs(w.imag)` at `:459,527`. ADD a sign-preserving readout and CONFIRM the
  decay/bound convention against `test_l3_mass_cage`. FLAG that the
  bound-vs-growing criterion may invert — RESOLVE it, do not assume.]* The
  sign-preserving `Im(ω)` is read out and the bound (decaying/lossless) vs growing
  convention is resolved against the mass-cage closed-port lossless limit
  (Im(ω)=0, Q=∞) and the matched-port decay direction.

**DEPTH** *[RF-3 cont.]*: the binding operator's `IsolationConfig` default is
`S_min=1e-3 → Γ≈−0.94` (near-total short), NOT the scatter's `A_cap=0.99 →
Γ≈−0.45`. We pick **ONE S_min for the binding operator** and recompute the
canonical reachable Γ against THAT floor (Γ = (√S_floor − 1)/(√S_floor + 1),
gamma_bulk convention `crystal_engine.py:478`). We sweep the `A_cap` clip
(`crystal_engine.py:194`) AND `S_min` — NOT `A_core` past 0.99 (which clips to a
NO-OP). We report a **confinement-vs-Γ-depth curve** and state explicitly whether
a **partial short binds** or **binding needs floor-dropping** (flagged
prominently if only floor-dropped). A floor-dropped-only bind is reported as
"confined (honestly-flagged floor-dropped)" per the binning.

### GATE 2 — SCRAMBLE (anti-tautology, necessary)

*[RF-4: BUILD the scramble arms as code — absent from graded_vacuum.]*

- **ARM-A: S→1 uniform** (must de-confine). The graded field is replaced by the
  vacuum value everywhere; the gapped localized mode must vanish.
- **ARM-B (LOAD-BEARING): spatially PERMUTE the per-bond S field holding the
  S-histogram FIXED** (must de-confine). A mode surviving ARM-B with `core_frac
  ≥ 0.50` gapped is **BC/projector-decided = AUTO-VOID** (the structural successor
  to Fork-A's `verdict_is_projector_tautology`).
- **Negative control:** a uniform-field scramble (permute a CONSTANT field) is a
  no-op — the operator must be UNCHANGED (proves the scramble machinery is not a
  blunt instrument).

Freeze the de-confinement margin: **≥ 0.30** drop in `core_frac` (or loss of the
gap) vs the ARM-A flat baseline. Both ARM-A and ARM-B must de-confine for the
CHORD/ECHO bins; ARM-B survival → VOID.

### GATE 3 — QUARTER-ARC SHAPE (headline, but CANNOT earn CHORD alone)

*[RF-5: RETIRE the endpoint-tanh comparator — sup-norm 0.5 < π/4 = norm-INFEASIBLE,
no brentq root.]* Use the **norm-feasible SAME-FAMILY comparator**
`S_comp(A) = (1 − A²)^p` with `p ≠ 0.5`. The same-family RMS-arc-length norms
(p=0.6→0.757, p=0.75→0.719, p=1.0→0.667) **OVERLAP** the quarter-arc π/4≈0.785,
so a `brentq` norm-match has a bracketed root. **Assert the brentq norm-match
SUCCEEDS before freezing the comparator** (HALT if no root).

- **DEPTH-INVARIANT metric:** match BOTH the integral norm AND the well depth
  (min S = D_max) between shapes, OR normalize Δ/L by well depth — so the metric
  reads CURVATURE, not floor-saturation.
- **Δ/L = √(Σ r²|ψ|² / Σ|ψ|²) / L** — the bound-mode RMS radius over box size L.
- **NULL-SHAPE CONTROL (gate before any cross-family gap counts):** two
  same-family shapes matched norm+depth must give Δ/L within **≪ 10%** (proves the
  metric reads SHAPE not DEPTH). This control PASSES before any cross-family >10%
  gap is allowed to count toward CHORD.
- **FLOOR-ARTIFACT GUARD:** require the gap to PERSIST as `S_min → 0` (floor
  lifted). If the gap VANISHES when neither shape clips, it was a floor artifact →
  **ECHO** (not CHORD).
- **SIZE-CONVERGENCE:** `L = 2/4/6` on the connect-map AND `N = 24/32/48` on the
  cube; the gap must be **MONOTONE-CONVERGING** (not a finite-size accident).

---

## 3. BINNING (frozen — no post-hoc movement)

- **CHORD** = confined (canonical short OR honestly-flagged floor-dropped) **AND**
  scramble de-confines (ARM-A AND ARM-B) **AND** quarter-arc Δ/L differs from the
  norm-feasible depth-matched comparator **>10% size-converged-monotone passing
  the null control** **AND** the **ELECTRON ANCHOR is reproduced** (the converged
  bound mode reproduces the cold-cage `ω_cutoff≈2.87` WITHOUT α-import — the anchor
  is REQUIRED, not bonus; a FORM/structural anchor, NOT m_e which is definitional).
- **ECHO** = confined + scramble-de-confines (real, S-dependent) BUT (shape-generic
  OR no anchor) → FORM-chord / consistency, peer-mapped no-worse-than-SM.
- **REFUTE** = NOT confined even floor-dropped.
- **VOID** = confined but scramble-INVARIANT (tautology) — discarded, NOT a
  negative. (BC/projector-decided; the structural successor to Fork-A's
  `verdict_is_projector_tautology`.)

**Pre-committed bin: ECHO.**

---

## 4. VALIDATE-ON-KNOWN

- **(i)** PR#305 `varactor_validate_on_known()` returns **PASS** (the S(A) kernel
  source-of-truth is sound).
- **(ii)** The cold-cage is a **"gapped-mode-EXISTS" anchor ONLY** — its GATE1 is a
  **pinned FAIL** (Q ≫ 45 lossless-confined, NOT in [20,45]; the eigenframe-Q is a
  different observable from the driven ringdown-Q). Re-pin to the **LIVE `_COLD`
  config** (`frac=0.9, S_min=1e-3, sigma_port=2.0` at
  `test_graded_vacuum_network_isolation.py:47`); do NOT use `frac=0.999 / σ=3.0`.
- **(iii)** DEC-5 anti-coincidence pin: `abs(Q − 29.98) > 1.0` (the only ~30 is
  band-consistent `Z_RADIATION`, never an identity).
- **(iv)** **α-free STRUCTURAL** — ALPHA cancels in the dimensionless `A = |V|/V_yield`;
  keep import-guards (`ALPHA`/`Q_TANK`/`ELECTRON` not reachable; α→2α invariance
  `|dΔ/L|/Δ/L < 1e-6`).

---

## 5. DISCIPLINE LENSES APPLIED

- **substrate-native-check** — connect-map graph-Laplacian (native), NOT cube;
  divergence-form stiffness operator (boundary-condition Γ=−1 short, CP10), NOT
  energy-basin minimization; A1 scalar sector (CP2); local-clock D=1/S in the
  coefficient (CP5); the planted saturated core is CONSISTENCY-class (CP8 flagged,
  not emergence).
- **phase-space-coordinate-check** — confinement is the REAL-space spatial
  operator's complex-ω + eigenvector localization, coordinate-matched (not a φ²
  phase-space claim).
- **no-phasor-wire** — the A1 scalar stays common-mode; the winding is NOT wired
  into the breather's own (V_inc,V_ref) phasor (master-equation.md:20).
- **consensus-bias-symmetric-standard** — FORM-chord ceiling unless the anchor;
  ECHO peer-mapped no-worse-than-SM.
- **verify-before-cite / ave-canonical-source** — every file:line cited has been
  grepped live; S(A) is IMPORTED from the canonical kernel, never re-hardcoded.

---

## 6. FALSIFIERS (what would move each bin)

- GATE1 fails even floor-dropped → REFUTE (the saturation tank does NOT confine
  the A1 mass — a clean negative).
- GATE2 ARM-B survives → VOID (the "confinement" was a BC/projector artifact).
- GATE3 null-control fails (same-family shapes differ >10%) → the metric reads
  DEPTH not SHAPE; the quarter-arc gap is uninformative → cannot earn CHORD.
- GATE3 gap vanishes at S_min→0 → floor artifact → ECHO.
- The electron anchor (ω_cutoff≈2.87) is NOT reproduced α-free → no CHORD
  (ceiling at ECHO/FORM-chord).

