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

> **TL;DR (verdict §4.3): `PARTIAL`.** Field-strain `s_knee = 2.877 d_sat` vs 90%-correction radius
> `r90 = 1.257 d_sat` → ratio `2.29` (resolution-stable, `2–5` band). The knee is the same *order* as
> the collar but a factor `~2.3` OUTSIDE the correction bulk. Richer finding: the knee coincides with
> the `r99` **outer envelope** of the correction cloud (ratio `1.06`) — a coupling-interface reading
> consistent with the deficit-knee-as-LOADING-BC ruling; while the correction bulk (`r50`/`r90`) sits at
> the near-SATURATED wall (`A ≈ 0.63`, `S ≈ 0.77`, `ΔS ≈ 31α`), NOT at the knee's `ΔS = α`. Two flags
> surfaced: field-vs-voltage strain (voltage-knee `8.28` ≈ review `NEAR_R = 10`), and the Γ sign
> convention (§5). No VALUE minted this wave (report-only per the ruling).

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

---

## 4. Results

**Driver as-run:** `alpha0 = 0.03`, profile at `R = 1000 d_sat`, collar at `R = 30 d_sat`
(frozen-window minimum → densest near-wall shells), `n_orient = 4`, `n_cut = 40`, frozen mesh
`n_r = 16` + refined `n_r = 48`. Output `assets/sim_outputs/knee_contour_check.{json,png}` (gitignored,
regenerable). All physics constants imported (`ALPHA`, `L_NODE`, `R_I`); `make verify` green at HEAD.

### 4.1 The knee (field-strain, PRIMARY)

The measured single-probe `A(s)` tracks the bare field-strain `(d_sat/s)²` to `< 10⁻⁴` (the dipole
dress is a perturbative correction near the probe), so the knee is crisp:

| quantity | value (d_sat) | value (ℓ_node) | value (SI) |
|---|---:|---:|---:|
| **`s_knee` field-strain (PRIMARY)** | **2.877** | **2.877** | **≈ 1.11 pm** |
| `s_knee` bare closed-form `(2α)^{−1/4}` | 2.877 | — | — |
| `s_knee` **voltage-strain (⚑ FLAGGED)** | 8.278 | 8.278 | ≈ 3.20 pm |

Discretization sensitivity of `s_knee` (frozen 16 vs refined 32 shells): **`4.5×10⁻⁵`** — negligible
(the knee is set by the bare `1/s²`, not the mesh). Unit map `1 d_sat = 1 ℓ_node`
(`methodological-contamination.md:46`), so both columns are numerically identical.

### 4.2 The collar (enclosed coupling-correction), `R = 30 d_sat`, `dep_full = 0.0456`

The coupling correction is **overwhelmingly carried by the near-SATURATED inner shell at the Pauli
wall** (where `A → 1` and `χ_sat = 1/√(1−A²) − 1` diverges): the innermost shell (`r_mid ≈ 1.17 d_sat`)
alone carries **91.5%** of the whole transfer departure; the enclosed fraction then rises slowly to `1`.
Because the correction is a **step function on the shell radii**, `r50`/`r90` are interpolated *within*
that first near-wall shell (hence their `~1.1–1.26 d_sat` values and the disclosed `~9%` discretization
sensitivity); the qualitative fact — the bulk is at the wall, not at the knee — is resolution-robust.

| radius | frozen `n_r=16` (d_sat) | refined `n_r=48` (d_sat) | disc. sensitivity |
|---|---:|---:|---:|
| `r50` (50% enclosed) | 1.208 | 1.101 | ~9% |
| **`r90` (90% enclosed) — verdict basis** | **1.257** | **1.144** | **~9%** |
| `r99` (99% enclosed) | 2.725 | 2.261 | ~17% |
| review `NEAR_R` cut | 10.0 | 10.0 | (fixed) |

The `s⁻⁶` induced-dipole-density falloff onset is `1.31 d_sat` (frozen) / `3.52` (refined) — the
crossover from near-wall saturation (`χ` diverges) to the linear `χ ≈ A²/2` regime (density `∝ s⁻⁶`);
resolution-sensitive but bracketing the same near-wall region, **inside** the knee.

### 4.3 Verdict

**PRIMARY (declared basis: field-strain `s_knee` vs `r90`): `PARTIAL`.**
`ratio = 2.877 / 1.257 = 2.29` (frozen), `= 2.51` (refined) — both land in the `2–5` PARTIAL band,
**resolution-stable**. The knee and the 90%-correction radius are the **same order** but **not
identical**: the knee sits a factor `~2.3` OUTSIDE the radius that carries the bulk of the correction.

Secondary reported comparisons (NOT the declared verdict basis, reported per class rules):

- **Field-knee vs `r99` (the OUTER edge of the correction cloud): near-identity, `ratio 1.06` (frozen)
  / `1.27` (refined) — MATCH-level, resolution-stable.** The `A = √(2α)` knee coincides with the radius
  enclosing the LAST 1% of the coupling correction — i.e. it marks the **outer envelope** of the
  screening cloud, the radius beyond which the medium's coupling contribution has effectively vanished.
- Field-knee vs `NEAR_R = 10`: `PARTIAL` (ratio 3.48) — the review's `10 d_sat` cut is over-generous
  (99% is already enclosed by `~2.7 d_sat`).
- **⚑ voltage-strain knee (8.278) vs `NEAR_R = 10`: `ratio 1.21` — MATCH-level (a SECOND coincidence,
  flag-don't-fix).** The review's chosen `10 d_sat` near-cloud cut is close to the *voltage*-strain knee.
  But voltage-knee vs `r90` is `NO-MATCH` (ratio 6.6).

---

## 5. The honest inverse read — what S and Γ the collar edge sits at

At the **declared collar edge `r90 = 1.257 d_sat`** the field-strain amplitude is `A = 0.633`
(voltage-strain `A_V = 0.796`), so:

- **`S = √(1−A²) = 0.774`** — i.e. `ΔS = 1 − S = 0.226 ≈ 31α`, a **NEAR-SATURATED** amplitude, roughly
  `5×` the deficit-knee amplitude and `~31×` its `ΔS`. **The collar edge is NOT set by the `√(2α)`
  knee** — it is set by the near-wall divergence of `χ_sat` (the inner shell at `A → 1`, i.e. approaching
  the RUPTURE amplitude `R_III = 1`, not the regime-I knee `R_I = √(2α)`).
- **`Γ = (1−√S)/(1+√S) = +0.064`** (E-sector static-dielectric convention).

For contrast, **at the deficit knee itself** (`A = √(2α)`): `S = 0.99268`, `ΔS = 1 − S = 0.00732 = α`
(the proportional limit, exactly), and `Γ = +0.00184`.

> **⚑ FLAG — Γ SIGN CONVENTION vs the Wall-A ruling.** The Wall-A ROLE-3 ruling
> (`rulings-docket:543`) reports **`Γ ≈ −0.002`** at the deficit knee (auditor arithmetic). This check's
> `Γ = +0.00184` **corroborates the MAGNITUDE** (`α/4 ≈ 0.00183 ≈ |−0.002|`) but carries the **opposite
> sign**, from the reflection convention: this check uses the static-E asymmetric load
> `Z_eff = Z₀/√S > Z₀ ⇒ Γ = (Z_eff−Z₀)/(Z_eff+Z₀) > 0` (a *capacitive-dielectric-loaded* boundary
> reflects with the `Γ>0` sign under this convention). Surfaced for the auditor to reconcile the sign
> convention with the ruling; the magnitude (`≈ α/4`) agrees.

---

## 6. Implications

**Verdict PARTIAL — the knee is the OUTER envelope of the screening cloud, not its dress-bulk edge.**
Under the declared basis (field-strain knee vs 90%-correction radius) the two surfaces are the same
order but a factor `~2.3` apart, resolution-stably. The richer, honest structure the numbers force:

1. **The deficit-knee surface acquires a MEASURED VALUE candidate — but a specific one.** The `A = √(2α)`
   contour (the FORM the KB lane is minting per the **Wall-A ROLE-3 "deficit knee"** ruling,
   `rulings-docket:540-568`) coincides with the **`r99` outer edge** of a real, converged
   self-consistent screening cloud (`ratio 1.06–1.27`, resolution-stable) — i.e. the knee's numeric
   address is **`s_knee ≈ 2.877 d_sat = 2.877 ℓ_node ≈ 1.11 pm`**, read as the **outer envelope** of the
   coupling-correction cloud, NOT the `r90` dress-bulk edge and NOT the review's `10 d_sat` cut.
   **This is a coupling-interface reading**, consistent with the ruling's identification of the deficit
   knee as the **LOADING BC / port** (the coupling/matching interface, `rulings-docket:556`): the knee
   bounds where the medium's coupling contribution lives.
2. **Per the ruling, the VALUE stays gate-measured — this wave reports, the mint does not consume the
   number.** The KB lane mints the deficit-knee FORM; this check supplies a measured VALUE *candidate*
   (`2.877 d_sat`, as the `r99` outer envelope). It is NOT landed into the KB and NOT a MATCH-class
   "the-knee-IS-the-dress-edge" claim (the declared `r90` verdict is PARTIAL). Routed to the auditor.
3. **This check builds the `A(r)` profile the deficit-knee ruling flagged as "the missing leg."** The
   ruling recorded that "no `A(r)` profile" was built (`rulings-docket:548`, fluxoid step-0 note:100).
   This check provides a converged `A(s)` profile **around a unit charge in the #693 screening cloud**
   (a distinct object from the electron soliton itself, but the first built `A`-vs-radius profile in this
   thread) and confirms it is the FIELD-strain `(d_sat/s)²` the kernel consumes.
4. **Two flagged forks are surfaced, not resolved (flag-don't-fix):** (a) the **field-vs-voltage strain**
   ambiguity — the driver kernel consumes field-strain `(d_sat/s)²` (knee at `2.877`), while the
   canonical `methodological-contamination.md:48-52` uses voltage-strain `d_sat/r` (knee at `8.278`,
   which happens to sit at the review's `NEAR_R = 10` cut); (b) the **Γ sign convention** vs the ruling's
   `Γ ≈ −0.002` (§5, magnitude corroborated). Both are Grant/auditor adjudication items.

**Consistency-vs-emergence tag: CONSISTENCY.** No value is minted, no emergence headlined; the earnable
content is the geometric characterization (a radius) of the charge-agnostic Op14 screening cloud. The
`s_knee = 2.877 d_sat` VALUE candidate rides the `α`-echo (it is `(2α)^{−1/4}` in native units) — it is
a consistency-class measured address, not an independent prediction.

