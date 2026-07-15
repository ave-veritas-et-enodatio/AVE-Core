# NOTE — Knee-Contour vs #693 Collar-Edge Check (F5-walk registered check)

**Date:** 2026-07-14 · **Lane:** KNEE-CHECK (Wave 0, registered check from Grant's F5 walk)
· **Driver (this check):** [`src/scripts/vol_2_subatomic/knee_contour_check.py`](../src/scripts/vol_2_subatomic/knee_contour_check.py)
· **Solver imported UNMODIFIED:** [`src/scripts/vol_2_subatomic/qed_trace_screening_sum_gate.py`](../src/scripts/vol_2_subatomic/qed_trace_screening_sum_gate.py) (#693)
· **#693 RESULT:** [`research/2026-07-14_screening-sum-gate_RESULT.md`](2026-07-14_screening-sum-gate_RESULT.md)
· **Contour authority:** `src/ave/core/chiral_lattice_v10.py:29-30` (`A_YIELD_SQ = 2·ALPHA`), kernel `S=√(1−A²)` at `:56` (= `constants.R_I`)
· **Prior ruling this corroborates:** the **Wall-A ROLE-3 "deficit knee"** ruling (Grant, 2026-07-14) — `_orchestration/2026-07-10_rulings-docket.md:540-568,608`

> **Ordering discipline (no answer-shaping).** This note was committed **hypothesis-first**:
> §1 (hypothesis) + §2 (verdict classes) + §3 (method) were frozen and committed BEFORE the
> driver was run; §4 (results), §5 (inverse read), §6 (implications) were appended in a
> SEPARATE, later commit. The verdict-class thresholds live in the driver's `classify()`
> (declared in code before the run). Git history carries the split.

---

## Sector header

MODE static two-body **TRANSFER** coupling between two seeded windings through a self-consistent
polarizable medium (the #693 gate, imported unmodified); REGIME cold, **KERNEL ON** (Op14/Ax4
saturation sets the per-cell polarizability); PHASE-STATE sub-yield perturbative; SECTOR **E-sector
static dielectric** — the induced-dipole screening cloud around a unit probe. No new ENGINE: this is a
pure re-analysis of the merged #693 solver. Class (consistency-vs-emergence): **CONSISTENCY** — the
Op14 kernel is charge-agnostic; the earnable content is a **geometric characterization** of the #693
gate (a radius), not a value. No emergence is headlined, and **no VALUE is minted this wave** (per the
deficit-knee ruling the KB lane mints the FORM; this check reports a measured VALUE *candidate* only).

---

## 1. Hypothesis (stated FIRST, before any number)

**The knee contour is the collar edge.** Specifically: the **knee contour** — the radius `s_knee` where
a unit probe's local field amplitude crosses `A = √(2α)` (`A² = 2α`, the `ΔS = α` proportional limit;
engine authority `chiral_lattice_v10.py:29-30` `A_YIELD_SQ = 2·ALPHA`, kernel `S = √(1−A²)`; =
`constants.R_I`, the Linear→Non-Linear regime-I boundary) — **coincides with the empirically-observed
collar structure of the #693 screening-sum gate**: the near dress, the region within `~10 d_sat` of each
probe that carries `~100%` of the coupling correction, with the induced-dipole density falling `~s⁻⁶`
beyond it.

If true, the deficit-knee surface (the FORM the KB lane is minting per the Wall-A ROLE-3 ruling,
`rulings-docket:540-568`) acquires a **measured VALUE candidate** — the collar radius of a real,
converged self-consistent screening cloud becomes the numeric address of the `A = √(2α)` contour, so a
FORM-only surface becomes a *measured surface*.

**Amplitude discipline (load-bearing — do NOT invent a field measure).** The `A(s)` this check measures
is the **exact amplitude the #693 kernel consumes**:

- driver `qed_trace_screening_sum_gate.py:236` — `A = |E_total| / E_yield`
- driver `:219` — `E_yield = K / d_sat²`

so for a unit probe (`|E_probe| = K/s²`) the kernel-consumed amplitude is the **FIELD-strain**
`A = (d_sat/s)²`. The `_chi_sat` kernel (driver `:189-191`, `χ = 1/√(1−A²) − 1`) and the yield kernel
`S = √(1−A²)` both zero at `A = 1` (rupture, `R_III`); the KNEE at `A = R_I = √(2α)` is where
`S = √(1−2α) ≈ 1−α`, i.e. `ΔS = α` — the proportional limit. This FIELD-strain reading is **PRIMARY**.

> **⚑ FLAGGED FORK (flag-don't-fix).** The canonical corpus leaf
> `vol2/proofs-computation/ch09-computational-proof/methodological-contamination.md:48-52` defines the
> strain as the **VOLTAGE-strain** `A_V = V/V_snap = d_sat/r` (`∝ 1/r`) and compares *that* to the same
> `√(2α)` knee. Field-strain (`∝1/r²`, driver kernel) and voltage-strain (`∝1/r`, that leaf) give
> **different knee radii**. This check reports BOTH but the PRIMARY is the driver's kernel-consumed
> field-strain (the amplitude-discipline rule above). The fork is surfaced for Grant, not silently
> resolved.

**Unit map (VERIFIED from corpus, NOT assumed).** The #693 driver is scale-free in `d_sat` (`d_sat = 1`
native; it never pins a physical length). The physical identification is canonical:
`methodological-contamination.md:46` — *"The topological saturation radius of the electron defines its
structural limit as `d_sat = l_node`."* So **`1 d_sat = 1 ℓ_node` exactly** (a 1:1 map); the `s_knee`
value is numerically identical in the two systems, and `ℓ_node ≈ 3.86×10⁻¹³ m` (imported `L_NODE`) is
the SI readout.

---

## 2. Verdict classes (DECLARED before the computation)

Primary comparison: field-strain `s_knee` vs the **90%-enclosed-coupling-correction radius `r90`**
(the enclosed-correction profile is computed from the SAME `transfer_alpha` masking machinery as the
#693 `genuineness_decomposition`). Classes:

| Class | Criterion | Reading |
|---|---|---|
| **MATCH** | `s_knee` within a factor `~2` of `r90` | the knee **IS** the dress edge — the contour becomes a measured surface |
| **PARTIAL** | same order, factor `2–5` | related but not identical; report both numbers |
| **NO-MATCH** | `>5×` apart | the collar is set by something else; report what amplitude the collar edge corresponds to |

Frozen thresholds: `MATCH_FACTOR = 2.0`, `PARTIAL_FACTOR = 5.0` (driver `classify()`). Primary
resolution = the **frozen #693 mesh** (`n_r = 16`, `n_ang = 24`); the discretization sensitivity of
every radius is reported at a refined mesh (the #693 review flagged single-resolution sensitivity).
Secondary reported comparisons (not the primary basis): `s_knee` vs the review's `NEAR_R = 10 d_sat`
cut; the FLAGGED voltage-strain knee vs `r90`; and the `r50/r99` enclosed radii for the full anatomy.

---

## 3. Method

1. **`A(s)` around a single probe.** Build the #693 two-probe mesh (`build_cells`) at a well-separated
   `R` inside the frozen `[30,3000]` window; run the driver's own `solve(..., q=(1,0))` (only probe-1
   sources the probe field — the driver's own single-probe isolation, kernel ON, self-consistent).
   Read `A = |E_total|/E_yield` at each cell of probe-1's own cloud (driver `:236`, the exact
   kernel-consumed amplitude). Report `A(s)` vs the bare `(d_sat/s)²`.
2. **`s_knee`.** Log-log interpolate the radius where the measured `A(s)` crosses `√(2α)` (`= R_I`);
   cross-check against the bare-field closed form `s_knee = d_sat·(2α)^{−1/4}`. Report both, plus the
   FLAGGED voltage-strain knee `d_sat/√(2α)`, plus discretization sensitivity (frozen vs refined mesh).
3. **`s⁻⁶` falloff onset.** From the same single-probe solve, the induced-dipole DENSITY `|p|/vol` vs
   `s`; the onset radius where its local log-log slope reaches `−6` (below it the near-wall response is
   saturated, `χ` diverges; at/above it `χ → A²/2` and density `~ s⁻⁶`).
4. **Enclosed-correction collar radii (`r50/r90/r99`).** From the driver's `transfer_alpha` with a
   radial keep-mask `dmin ≤ s_cut` (the #693 decomposition machinery): `enclosed(s_cut) =
   (α_eff(dmin≤s_cut) − 1)/(α_eff_full − 1)`, orientation-averaged. `R` chosen at the frozen-window
   **minimum** (`30`) so the log-radial shells are densest near the Pauli wall (the near-wall region
   carries the correction); `n_r` swept frozen (16) vs refined (48) for the discretization report.
5. **Verdict** = `classify(s_knee_field, r90)`; plus the secondary comparisons above.
6. **Inverse read (the honest inverse question).** At the measured collar edge (`r90`): the field-strain
   amplitude `A`, the kernel `S = √(1−A²)`, and the E-sector static-dielectric reflection
   `Γ = (1−√S)/(1+√S)` (Op14 Meissner-asymmetric static-E load: `ε_eff = ε₀S`, `μ` unloaded ⇒
   `Z_eff = Z₀/√S`; convention stated, reconciled against the ruling's `Γ ≈ −0.002` at the knee).

<!-- RESULTS-BELOW-APPENDED-IN-A-SEPARATE-COMMIT (no-answer-shaping ordering) -->
