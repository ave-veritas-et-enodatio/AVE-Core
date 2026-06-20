# Result — Fork-B "Saturation-Tank Mass Confinement" Gate

**Prereg (frozen FIRST):** `research/2026-06-20_fork-b-saturation-tank-confinement_prereg.md`
(frozen commit `4ea29667`, the first commit of branch
`analysis/2026-06-20-fork-b-saturation-tank-confinement`).
**Built off:** `origin/main @ 19d55266` (PR#305 varactor scatter kernel on main).
**Solver:** `src/ave/solvers/fork_b_saturation_tank.py`.
**Tests:** `src/tests/test_fork_b_saturation_tank.py` (21 passed).
**Figures:** `research/figures/2026-06-20-fork-b-saturation-tank/` (3, from the actual run).
**Lane:** implementer. Auditor lands the KB/manual entries.

---

## VERDICT: **ECHO** (the pre-committed, expected, successful outcome)

> confined (canonical partial short, NOT floor-dropped) **AND** scramble
> de-confines (ARM-A AND ARM-B, real S-dependent, NOT a tautology) **BUT**
> shape-generic (quarter-arc Δ/L gap ~0 ≪ 10%) **AND** no electron anchor
> (connect-map ω is lattice-band-structure-set, NOT a converged 2.87)
> ⇒ **FORM-chord / consistency**, peer-mapped no-worse-than-SM.

This is exactly the PRE-COMMITTED PREDICTION (prereg §0). A clean ECHO is the
expected, successful result. **No CHORD was manufactured.**

| Bin item | Result |
|---|---|
| GATE1 confined (core_frac ≥ 0.50, gapped+discrete, Im(ω) bound, A1-scalar) | **PASS** |
| GATE2 scramble de-confines (ARM-A AND ARM-B, margin ≥ 0.30) | **PASS** (de-confines) |
| GATE2 ARM-B survives ⇒ AUTO-VOID | **False** (NOT a tautology) |
| GATE3 shape gap > 10% (size-converged, null-control, floor-persisting) | **False** (gap ~0, shape-generic) |
| Electron anchor (ω→2.87 α-free, converged) | **False** (NOT reproduced) |
| α-free structural (α→2α invariance) | **PASS** (rel = 0.0 exactly) |
| DEC-5 anti-coincidence (ω ≠ Z_RADIATION 29.98) | **PASS** |
| validate-on-known (i) PR#305 varactor PASS | **PASS** |

---

## 1. ARCHITECTURE (as built — the load-bearing correction honored)

Confinement was tested as a property of the **SPATIAL STIFFNESS operator**
`L = adjoint_div(D ∇)`, `D = 1/S(A)`, EXTENDED onto the **native connect-map** as
the graph-stiffness operator `L = Bᵀ diag(D_bond) B` (B = signed node-bond
incidence; the divergence-form Laplacian on the lattice's OWN bond graph). The
PR#305 scatter operator was NOT eigensolved for confinement (it is orthogonal,
unit-modulus, no bound states); its canonical `S(A)` kernel was IMPORTED as the
single source-of-truth (`vacuum_varactor_scatter.saturation_kernel` →
`crystal_engine.saturation_kernel`, ave-canonical-source).

**A load-bearing physics flag surfaced by the run (RF-2/RF-3):** the varactor
stiffness convention `D = 1/S → ∞` at the saturated core means the bound mode is a
**HIGH-frequency mode gapped ABOVE the continuum band top** (a stiff-core
breather), NOT below it. The spectral-gap witness measures separation from the
nearest band edge (the TOP here), resolved explicitly — not assumed.

---

## 2. GATE 1 — CONFINEMENT (necessary): **PASS**

The connect-map stiffness operator has a gapped, discrete, core-localized
A1-scalar bound mode at the canonical binding-operator floor.

| net | L | n_nodes | core_frac | ω_bound | gap_above (ω²) | spacing (ω²) | Im(ω) bound | confined |
|---|---|---|---|---|---|---|---|---|
| diamond | 8 | 128 | 0.758 | 3.029 | 1.400 | 0.015 | ✓ (lossless) | **True** |
| srs | 4 | 512 | 1.000 | 3.264 | 3.035 | 0.005 | ✓ (lossless) | **True** |
| srs | 6 | 1728 | 1.000 | 3.560 | 3.131 | 0.002 | ✓ (lossless) | **True** |

- **(a) core_frac ≥ 0.50** [RF-1]: the live selector's `>0.05` floor was OVERRIDDEN
  to `≥0.50`; the bound mode carries 0.758–1.000 of its `|ψ|²` on the core.
- **(b) gapped + discrete** [RF-2]: a CLUSTER-AWARE spectral-gap witness built INTO
  the eigensolve selector — the bound LEVEL (degeneracy-aware) sits above the band
  top by a margin ≫ the continuum level spacing. The time-domain `_bulk.py:443`
  `peak_mean` ringdown observable was NOT cited; `ω_guess=2.87` was replaced by a
  band-derived (highest-ω core-localized) selector.
- **(c) Im(ω) sign RESOLVED** [RF-3]: a sign-preserving open-matched-port readout,
  with the convention ANCHORED by a known port-coupled continuum mode that decays
  (Im < 0 in e^{−iωt}). The bound mode is core-localized ⇒ lossless (Im ≈ 0, NOT
  growing) ⇒ bound branch confirmed, not assumed. The bound-vs-growing criterion
  did NOT invert (the deep stiff-core mode is the lossless reactive limit, matching
  the mass-cage closed-port Q=∞).

**DEPTH (RF-3) — the partial short binds, NO floor-dropping needed.** ONE S_min was
chosen for the binding operator; `gamma_from_S_floor(S_min)` gives the canonical
reachable Γ (gamma_bulk convention `crystal_engine.py:478`). The
confinement-vs-Γ-depth curve (fig1a) shows the diamond L=8 core binds (core_frac =
0.758) at ALL floors from S_min = 0.5 (Γ = −0.17, a SHALLOW partial short) down to
S_min = 1e-4 (Γ = −0.98). **A partial short binds at the canonical floor; binding
does NOT need floor-dropping.** (fig1b: the A_cap kernel clip controls the well
depth — binds for A_cap ≳ 0.8, the canonical 0.99 binds.) Reported prominently per
the prereg: this is the GOOD case, not the floor-dropped-only case.

**Sector-projection guard (CP2):** the bound mode lives in the A1 dilatation-scalar
grade by construction — the operator carries 1 scalar DOF/node, with NO shear /
micro-rotation grade for the mode to leak into (the (2,3) CHARGE-"3" couple-stress
would be a SEPARATE 3-vector operator, not built). A1 ⊥ T2 (master-equation.md:20).

---

## 3. GATE 2 — SCRAMBLE (anti-tautology, necessary): **PASS (de-confines, NOT VOID)**

The confinement is **S-STRUCTURE-decided**, NOT BC/projector-decided — the
structural successor to Fork-A's `verdict_is_projector_tautology` is clean.

| net | L | baseline core_frac | ARM-A (S→1) | ARM-A margin | ARM-B (permute) | ARM-B margin | ARM-B survives | ctrl no-op |
|---|---|---|---|---|---|---|---|---|
| diamond | 8 | 0.758 | 0.063 | 0.695 | 0.077 | 0.681 | **False** | True |
| srs | 4 | 1.000 | 0.068 | 0.932 | 0.000 | 1.000 | **False** | True |
| srs | 6 | 1.000 | 0.066 | 0.934 | 0.000 | 1.000 | **False** | True |

- **ARM-A (S→1 uniform):** core_frac collapses to ~0.06 — de-confines.
- **ARM-B (LOAD-BEARING — permute the per-bond S field, HISTOGRAM FIXED):**
  core_frac collapses to ~0.0–0.08 — de-confines. The S-multiset is preserved
  (`np.sort(S)` invariant asserted); only the SPATIAL S-structure is destroyed.
  **ARM-B does NOT survive** (no mode with core_frac ≥ 0.50 gapped after the
  permutation) ⇒ NOT a tautology ⇒ NOT VOID.
- **Negative control (permute a CONSTANT S field):** a no-op (operator unchanged,
  atol 1e-12) — the scramble machinery is not a blunt instrument.
- De-confinement margins (0.68–1.00) all exceed the frozen ≥ 0.30 threshold.

This is the anti-tautology gate passing decisively (fig2).

---

## 4. GATE 3 — QUARTER-ARC SHAPE (headline): **shape-generic (gap ~0 ≪ 10%) ⇒ ECHO**

The canonical AVE kernel `S = √(1−A²)` (p = 0.5) **IS the quarter-circle exactly**
(`∫₀¹ √(1−A²) dA = π/4`). The discriminator: does its bound-mode Δ/L differ from a
same-family comparator `(1−A²)^p`, p ≠ 0.5, matched on BOTH norm AND depth, by
> 10%? **It does not — the gap is ~0.000.**

| net | L | Δ/L canonical | Δ/L comparator | shape gap | null gap | depth-matched | norm-match ok |
|---|---|---|---|---|---|---|---|
| diamond | 8 | 0.1453 | 0.1453 | 0.000 | 0.000 | True | True |
| srs | 4 | 0.0699 | 0.0699 | 0.000 | 0.000 | True | True |
| srs | 6 | 0.0466 | 0.0466 | 0.000 | 0.000 | True | True |

- **RF-5 retirement honored:** the endpoint-tanh comparator (sup-norm 0.5 < π/4 =
  norm-INFEASIBLE) was RETIRED. The norm-feasible same-family comparator's brentq
  norm-match SUCCEEDS (asserted before freezing; the π/4 target recovers p = 0.5
  exactly).
- **Depth-invariant metric:** Δ/L = √(Σ r²|ψ|² / Σ|ψ|²) / L, with BOTH norm
  (brentq) AND well-depth (rescale) matched, so the metric reads CURVATURE, not
  floor-saturation. The shapes are genuinely DIFFERENT (max |ΔS| ≈ 0.022 at
  intermediate A) yet give the SAME Δ/L — the bound-mode RMS radius is insensitive
  to the shape exponent once norm+depth are matched. **Generic saturable-NLS.**
- **Null-shape control PASSES** (null gap = 0.000 ≪ 10%): the metric reads SHAPE,
  not DEPTH. This gate passes BEFORE any cross-family gap could count.
- **Floor-artifact guard:** the gap stays ~0 across S_min = 1e-1 … 1e-5 (never
  exceeds 10%) — verdict "floor-artifact-or-shape-generic (ECHO)".
- **Size-convergence (fig3b):** the gap stays ~0% across the connect-map ladder
  (L = 2/4/6) — size-stably below threshold.

---

## 5. ELECTRON ANCHOR (CHORD-required, NOT bonus, NOT expected): **NOT reproduced**

The converged connect-map bound mode does **NOT** reproduce the cold-cage
`ω_cutoff ≈ 2.87` α-free:

| net | ω(L=2) | ω(L=4) | ω(L=6 or 8) | converged in L | within 10% of 2.87 | reproduced |
|---|---|---|---|---|---|---|
| srs | 2.703 | 3.264 | 3.560 | **False** (diverges up) | False | **False** |
| diamond | — | — | 3.029 (L=8 only) | — (1 size) | — | **False** |

The connect-map bound-mode ω is set by the **lattice's own band structure** (degree,
geometry, the graph-Laplacian normalization), NOT a universal 2.87. On srs it
DIVERGES upward with L (2.70 → 3.26 → 3.56), crossing the 2.87 line rather than
converging to it. The cold-cage 2.87 was a property of a specific Cartesian-FDTD
`dx/dt` normalization; the connect-map has no fixed `dx/dt` to pin an absolute
frequency. **The anchor is NOT a converged α-free structural constant.** This caps
the verdict at ECHO — exactly as pre-committed (prereg §0: "the anchor is REQUIRED,
not bonus; and it is NOT expected").

---

## 6. STENCIL NOTE (structural-null-stencil-lens) — the verdict is on the NATIVE connect-map

The verdict was computed on the REAL `build_srs_net` / `build_diamond_net`
CONNECT-MAP (native graph-stiffness `L = Bᵀ diag(D_bond) B`). The shipped
`graded_vacuum_network.py` L is on a Cartesian `(N,N,N)` cube; it was used ONLY as a
**FLAGGED Cartesian-embedded sensitivity**, NOT the verdict basis:

| stencil | ω_bound | core_frac | confined |
|---|---|---|---|
| connect-map diamond L=8 (NATIVE, verdict) | 3.03 | 0.758 | True |
| connect-map srs L=4/6 (NATIVE, verdict) | 3.26 / 3.56 | 1.000 | True |
| Cartesian cube N=24/32 (FLAGGED approx) | 1.13 / 1.20 | 0.981 / 0.997 | True |

Cross-stencil consistency: BOTH stencils confine (high core_frac), and NEITHER pins
ω to a universal 2.87 (cube ≈ 1.1, connect-map ≈ 3.0–3.6, FDTD = 2.87 — three
different normalizations). This REINFORCES the no-anchor ECHO finding: confinement
is stencil-robust, but the absolute frequency (and hence any 2.87 anchor) is
normalization-dependent, not a derived structural constant.

---

## 7. VALIDATE-ON-KNOWN

- **(i)** PR#305 `varactor_validate_on_known()` → **PASS** (kernel source-of-truth sound).
- **(ii)** Cold-cage = "gapped-mode-EXISTS" anchor ONLY. The live `_COLD` config
  (`frac=0.9, S_min=1e-3, sigma_port=2.0`) gives the lossless-confined eigenframe
  (Q ≫ 45, GATE1-FAIL-by-design — the eigenframe-Q is a different observable from
  the driven ringdown-Q). The connect-map confinement (this gate) is the
  gapped-mode-EXISTS property, consistent with that anchor.
- **(iii)** DEC-5 anti-coincidence: ω_bound = 3.03 ≠ Z_RADIATION 29.98 (|ω − 29.98|
  > 1.0). PASS.
- **(iv)** α-FREE STRUCTURAL: ALPHA cancels in the dimensionless A = |V|/V_yield;
  ALPHA is NOT reachable in the module; α→2α leaves ω and Δ/L EXACTLY unchanged
  (rel = 0.0). PASS. Import-guards (ALPHA / Q_TANK / ELECTRON / RHO_BULK) hold.

---

## 8. HONEST CLOSURE (Rule 11) + symmetric-standard framing

A single mechanism explains the ECHO: **the saturation tank genuinely confines a
posited A1 mass (S-structure-decided, not a tautology), but the confinement is a
generic saturable-NLS phenomenon — the quarter-arc shape is not load-bearing, and
the absolute bound-mode frequency is lattice-normalization-dependent, not a derived
2.87 anchor.** That is a FORM-chord / consistency result.

Per **consensus-bias-symmetric-standard**: this FORM-chord ceiling is **no worse
than the SM**, which does not derive α, fits the Yukawas, and does not explain
charge quantization or mass values either. The ECHO is peer-mapped-honestly, not an
AVE-comedown — AVE forces the FORM (a saturation tank DOES confine a mass), and
imports the VALUE (the absolute frequency / any 2.87).

**Branch closed at ECHO.** The wrong reaction would be to debug toward a rescue
(re-tune the lattice normalization to hit 2.87, or hunt a shape gap by un-matching
depth). The right reaction: record the clean ECHO, name the mechanism, close the
branch. The tests pin the ECHO outcome so it cannot be silently re-tuned.

### Open follow-ups (surfaced for the auditor, NOT landed here)
- The absolute-frequency normalization question (what `dx/dt` would map the
  connect-map ω onto a physical scale) is a SEPARATE calibration question, NOT a
  confinement question — flagged, not pursued.
- Whether a DEEPER core (frac → A_cap, fully floor-clipped) sharpens any shape gap
  is closed-negative here (floor-lift guard: gap ~0 at all S_min); a fundamentally
  different comparator FAMILY (not `(1−A²)^p`) is the only remaining shape lever,
  but the null-control + same-family-generic result strongly predicts shape-generic.

