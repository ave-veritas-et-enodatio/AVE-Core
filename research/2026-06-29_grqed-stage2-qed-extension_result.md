# RESULT — Stage-2 QED-Extension: the ℓ_node UV cutoff + the E-route birefringence ON the linear QED core

**Date:** 2026-06-29 · **Lane:** implementer · **Branch:** `analysis/grqed-stage2-qed-extension`
**Status:** Stage-2 increment landed (code + both two-test doctrines + distinct-cutoff discipline + FORM/VALUE guards; both test lanes green)
**Scope:** Two corrections ON the inherited QED / Maxwell solver — the FIRST is the **Brillouin-cutoff
propagator** (a FORM-derived 1-loop regulator from the Axiom-1 lattice pitch), the SECOND is the **E-route
vacuum birefringence** (the bankable chord, clm-pp3qwf, reusing the saturating-ε already in `fdtd_3d`). Both
are **dormant in the QED regime** (recover-QED at low momentum / low field). The inherited continuum QED core
is the low-momentum / weak-field limit and is NOT re-derived here.

---

## 0 · One-paragraph summary

The vacuum is a real discrete lattice with a finite pitch ℓ_node. Two consequences ride ON the inherited
continuum-QED solver, both dormant in the QED regime. **(1) The Brillouin-cutoff propagator** — the EXACT
discrete-Hilbert commutator (DCVE App-E, `dcve-specification.md`:36-42) gives `p_disc=(ℏ/iℓ)sin(kℓ)` ⇒
`[x,p]=iℏcos(kℓ)=iℏ√(1−(ℓp/ℏ)²)`, so the lattice supplies a **PHYSICAL momentum cutoff** at the Brillouin
edge `|k|≤k_max=π/ℓ_node` — **no counterterm**. A 1-loop integral over the FIRST Brillouin zone is **FINITE
by mode-count** (`loop_integral_brillouin_zone` → 1.25e14, converged N=48≈N=72); the same integrand in the
continuum **DIVERGES** with the cutoff (7.1e13 → 7.8e14 as Λ goes 1→8×k_max, ~Λ³). At `qℓ≪1` the lattice
dispersion `(2/ℓ²)Σ_b(1−cos(k·b̂·ℓ))→|k|²` (the continuum QED propagator) to the `(kℓ)²/12` Taylor remainder
— **recover-QED**. **(2) The E-route birefringence** — REUSING the canonical Op14 kernel `S(A)=√(1−A²)` (the
SAME `saturation_factor` `fdtd_3d._compute_local_epsilon` applies), the static-E-driven ε-grade gives uniaxial
eigen-indices `n_⊥=(1−A²)^(1/4)`, `n_∥=√[(1−2A²)/√(1−A²)]`, differential `δn_bir=n_∥−n_⊥≈−½A²` with
`A=E/E_yield`. At `E≪E_yield`, `δn_bir→0` (no tree birefringence — **recover-QED**); at high E the O(1)
differential appears. **The CHORD is the EXISTENCE** of a tree-level O(1) birefringence-bearing structure QED
LACKS (QED's is an α²-loop effect); the **MAGNITUDE** `7.5/α³≈1.93×10⁷` is an **α-ECHO** (value-level, α
imported). Both two-test legs pass; the **distinct-cutoff discipline** (spatial `k_max=π/ℓ_node` loop bound vs
temporal `ω_C=c/ℓ_node` μ bound, ratio exactly π) is declared and guard-tested.

**Honest framing (the two halves sit at DIFFERENT rungs — do NOT present co-equal):** the **ℓ_node cutoff FORM
is genuinely FORM-DERIVED** (Axiom-1 lattice pitch → the exact discrete-Hilbert commutator — the
more-principled-than-dim-reg half). The **saturating-ε is FORM-POSTULATED** (it IS Axiom 4). And **α is QED's
coupling — it is IMPORTED here** (a VALUE-import, expected for a QED-extension; the birefringence magnitude
rides α⁻³). See the FORM/VALUE ledger (§8) and the F4 self-energy honesty (§9).

---

## 1 · Spec (what was built)

| Element | Spec | Where |
|---|---|---|
| Inherited continuum QED core (NOT re-derived) | continuum propagator `|k|²−ω²/c²`; the low-momentum / weak-field limit | (inherited; recovered at `qℓ≪1` / `E≪E_yield`) |
| ★ The BZ-cutoff propagator (FORM-DERIVED) | lattice denominator `(2/ℓ²)Σ_b(1−cos(k·b̂·ℓ))−ω²/c²`; loop integral over the FIRST BZ `|k|≤k_max=π/ℓ_node` | `qed/brillouin_cutoff.py`: `lattice_dispersion_denominator`, `loop_integral_brillouin_zone` |
| Continuum contrast (the divergence) | `∫_{|k|<Λ} d³k/(k²+m²)` grows ~Λ³ — the UV divergence the cutoff removes (no AVE claim) | `qed/brillouin_cutoff.py`: `continuum_loop_integral` |
| Distinct-cutoff discipline | SPATIAL `k_max=π/ℓ_node` (LOOP bound) vs TEMPORAL `ω_C=c/ℓ_node` (μ bound); ratio exactly π | `K_MAX_SPATIAL` (DECLARED); constants.py:286-294 |
| The E-route birefringence (the chord) | `A=E/E_yield`; `n_⊥=(1−A²)^(1/4)`, `n_∥=√[(1−2A²)/√(1−A²)]`, `δn_bir=n_∥−n_⊥≈−½A²` | `qed/birefringence.py`: `birefringence_dn`, `birefringence_eigenindices` |
| The ONE kernel (REUSED, not minted) | `S(A)=√(1−A²)` via `scale_invariant.saturation_factor` — the SAME `fdtd_3d._compute_local_epsilon` uses | `qed/birefringence.py` (imports `saturation_factor`) |
| The α-echo magnitude | `δn_AVE/δn_QED=(1/2)/((3/45)α²)·(E_crit/E_yield)²=7.5/α³≈1.93×10⁷` | `qed/birefringence.py`: `chord_magnitude_ratio` |
| Two-test doctrine ×2 | recover-QED (consistency) + activate (manifestation) for BOTH corrections | §4-§5 (propagator), §6 (birefringence) |

## 2 · Substrate-native-check (walked before numerical code)

- **K4 / k-space mode-count.** The loop integral is a **sum over the FINITE set of first-Brillouin-zone modes**
  (N = V/ℓ³), NOT a continuum-Helmholtz operator and NOT a Lagrangian / energy-functional minimization. The
  dispersion denominator is the cubic-bond sum `(2/ℓ²)Σ_b(1−cos(k·b̂·ℓ))` (the K4 diamond stencil shares the
  same small-k limit). Finiteness is by **mode-count**, not by a counterterm. The continuum `∫d³k` is never the
  AVE claim — it is provided only to exhibit the divergence.
- **Sector ownership.** The loop regulator lives in the **k-space dispersion** (the propagator denominator).
  The birefringence lives in the **ε-grade** (the V-keyed varactor, Op14 saturating-ε). The μ-grade is a
  spectator under a static drive (circulation-keyed inductor, `S_μ=1`) — so the birefringence is ASYM
  (ε loads, μ linear). Never cross-wired.
- **Op14.** The ONE canonical kernel `S(A)=(1−A²)^(1/2)` is REUSED via `scale_invariant.saturation_factor`
  (the SAME function `fdtd_3d._compute_local_epsilon` calls). `n_⊥=√S=(1−A²)^(1/4)` is built FROM it; no
  second kernel is minted.
- **phase-space vs real-space (A46).** Neither correction makes a (V_inc, V_ref) Clifford-torus phase-space
  claim. The propagator claim is in **real k-space** (the Brillouin zone) and is measured there; the
  birefringence claim is in **field-amplitude / refractive-index space** (n vs E) and is measured there.
  Coordinate-discipline clean.
- **consistency-vs-emergence (A47).** Propagator recover-QED = **Class C consistency** (reproduce the continuum
  QED propagator at `qℓ≪1`); activate-at-cutoff = **Class B manifestation** (the Brillouin edge is Axiom-1 in
  k-space). Birefringence recover-QED = **Class C consistency** (`δn→0`, no tree birefringence). The CHORD
  (existence) is the AVE-distinct content; the MAGNITUDE `7.5/α³` is an **α-ECHO** (value-level, α imported —
  symmetric standard: QED's `a_EH α²` is equally α-rooted). Full ledger in §8.
- **Checkpoint 9 (heuristic-vs-dynamical), honest.** Both observables are **analytic/algebraic** (a BZ
  quadrature; an ε→n map), NOT dynamically evolved through `engine.step()`. This is correct for a
  loop-regulator / index demonstration (the spec asks for the loop-integral STRUCTURE and the index map), and
  the birefringence reuses the *existing* `_compute_local_epsilon` ε(A) kernel as a closed-form. Stated, not
  papered over (§9 flag 3).

## 3 · Code delivered (file:line)

New QED-extension package `src/ave/qed/` (distinct from the GR-extension which lives in `src/ave/gravity/`):

| Function | Role |
|---|---|
| `brillouin_cutoff.K_MAX_SPATIAL` | the DECLARED spatial loop bound `k_max=π/ℓ_node≈8.135e12 /m` (NOT `ω_C`) |
| `brillouin_cutoff.lattice_dispersion_denominator(k, *, ell, omega_over_c)` | the lattice propagator denominator `(2/ℓ²)Σ_b(1−cos(k·b̂·ℓ))−ω²/c²`; recover-QED at `kℓ≪1`, band-limits at the BZ edge |
| `brillouin_cutoff.loop_integral_brillouin_zone(*, m_sq, ell, n_grid)` | the 1-loop integral over the FIRST BZ — FINITE by mode-count (no counterterm) |
| `brillouin_cutoff.continuum_loop_integral(cutoff_lambda, *, m_sq, n_radial)` | the continuum contrast `∫_{|k|<Λ} d³k/(k²+m²)` — DIVERGES ~Λ³ (no AVE claim) |
| `birefringence.birefringence_eigenindices(A)` | the uniaxial eigen-indices; `n_⊥` built from the REUSED canonical `S(A)` |
| `birefringence.birefringence_dn(E, *, e_yield)` | the par−perp differential `δn_bir(E)≈−½A²` (the polarimeter observable) |
| `birefringence.chord_magnitude_ratio()` | the α-echo magnitude `7.5/α³≈1.93×10⁷` (NOT the chord — the chord is the existence) |

Tests live in `src/tests/test_grqed_stage2_qed_extension.py` (26 tests); the heavy BZ convergence /
finite-vs-continuum quadrature sweeps are routed to the `engine_sim` lane via `src/tests/conftest.py`
(`_ENGINE_SIM_TESTS`, #411 cost+role discipline). The brillouin_cutoff regulator is **α-CLEAN** — a source-level
guard test asserts no `ALPHA`/`Q_TANK` reaches it (the regulator FORM is purely geometric, ℓ_node only).

## 4 · Test (1)(i) — BZ propagator RECOVER-QED (consistency-class) ✅

At `qℓ≪1`: `cos(kℓ)→1−½(kℓ)²`, so the lattice dispersion `(2/ℓ²)Σ_b(1−cos(k·b̂·ℓ))→|k|²` — the **continuum
QED propagator denominator**. The relative error is the Taylor remainder `(kℓ)²/12`.

| `kℓ` (on-axis) | lattice vs continuum rel. err | Taylor `(kℓ)²/12` |
|---|---|---|
| `10⁻³` | `8.335×10⁻⁸` | `8.333×10⁻⁸` |
| `10⁻²` | `8.333×10⁻⁶` | `8.333×10⁻⁶` |
| `10⁻¹` | `8.331×10⁻⁴` | `8.333×10⁻⁴` |

- The error is **quadratic in `kℓ`** (halving `kℓ` quarters it: `e(2×10⁻²)/e(10⁻²)=4.0` to rtol 2%) — the
  signature of the `cos→1−½(kℓ)²` expansion.
- Holds **off-axis** too (the `(1,1,1)/√3` diagonal recovers to `<10⁻³` at `kℓ=10⁻²`).

**Verdict: PASS** — the lattice propagator collapses to the inherited continuum-QED propagator at low
momentum. This leg is **consistency-class** (reproduce a known theory at its limit), NOT an emergence claim.

## 5 · Test (1)(ii) — BZ propagator ACTIVATE-AT-CUTOFF (manifestation-class) ✅

The dispersion **band-limits** at the Brillouin edge, and the 1-loop integral over the FIRST Brillouin zone is
**FINITE by mode-count** — while the same integrand in the continuum DIVERGES.

| Check | Result |
|---|---|
| dispersion at BZ edge `k=π/ℓ` (one axis) | `4.000/ℓ²` (band-limit; saturates) |
| dispersion at `(π,π,π)` corner | `12.000/ℓ²` (band maximum) |
| dispersion bounded over the whole BZ | `0 ≤ D_lat ≤ 12/ℓ²` everywhere (10k random k) |
| ★ BZ loop integral `∫_{BZ} d³k/(D_lat+m²)` | `1.245345×10¹⁴` — **FINITE**, converged N=32≈48≈72 |
| continuum `∫_{|k|<Λ} d³k/(k²+m²)`, Λ=1·k_max | `7.118×10¹³` |
| Λ=2·k_max | `1.709×10¹⁴` |
| Λ=4·k_max | `3.741×10¹⁴` |
| Λ=8·k_max | `7.824×10¹⁴` (still growing — ~Λ³, **divergent**) |

The contrast is the whole point: **SAME integrand**, FINITE on the compact Brillouin zone (a finite mode
count), ARBITRARILY LARGE in the continuum as the cutoff is lifted (8× Λ → 11× the integral, no plateau). The
BZ integral needs **no counterterm** — the lattice pitch ℓ_node is the regulator.

**Verdict: PASS** — the band-limited Brillouin-zone dispersion makes the loop integral finite by construction;
the continuum divergence it removes is exhibited side-by-side. This leg is **manifestation-class** (the
Brillouin edge is Axiom-1 expressed in k-space). The cutoff FORM is **FORM-DERIVED** (the exact discrete-Hilbert
commutator; §8).

## 6 · Test (2) — E-route birefringence: RECOVER-QED + ACTIVATE ✅

**(2)(i) RECOVER-QED (consistency-class).** At `E≪E_yield` (`A=E/E_yield→0`), `δn_bir→0` — NO tree-level
birefringence, exactly as QED at tree level. The leading term is `−½A²` (E²-leading):

| `E/E_yield` | `δn_bir` | `−½A²` |
|---|---|---|
| `10⁻⁴` | `−5.000000×10⁻⁹` | `−5.000000×10⁻⁹` |
| `10⁻³` | `−5.000005×10⁻⁷` | `−5.000000×10⁻⁷` |
| `10⁻²` | `−5.000500×10⁻⁵` | `−5.000000×10⁻⁵` |

The differential is **E²-leading, NOT E⁴** (halving E quarters `δn`): this is the **corrected clm-pp3qwf
discriminator** — an E² slope does NOT falsify AVE (QED is also E²-leading). The historical "E⁴" was a `√ε`
conflation, retracted 2026-06-04 (Rule 12; §7).

**(2)(ii) ACTIVATE (manifestation-class).** As E approaches E_yield the O(1) differential appears:

| `A=E/E_yield` | `n_⊥` | `n_∥` | `δn_bir` |
|---|---|---|---|
| `0.1` | `0.99749` | `0.99244` | `−5.051×10⁻³` |
| `0.3` | `0.97670` | `0.92714` | `−4.956×10⁻²` |
| `0.5` | `0.93060` | `0.75984` | `−1.708×10⁻¹` |
| `0.7` | `0.84507` | `0.16735` | `−6.777×10⁻¹` |

The two probe eigen-indices split (uniaxial), and `n_⊥=(1−A²)^(1/4)=√S(A)` is built from the **REUSED**
canonical Op14 kernel — bit-identical (`n_⊥²=S(A)`) to the `fdtd_3d._compute_local_epsilon` ε-softening
(guard-tested).

**Verdict: PASS** — `δn_bir→0` at low field (recover-QED), O(1) at high field (activate). The CHORD framing
(existence, not magnitude) is §7.

## 7 · ★ THE CHORD (framed precisely) + the distinct-cutoff declaration

**The CHORD is the EXISTENCE, not the magnitude.** The AVE-distinct content of the E-route birefringence is
that the vacuum **saturates at all** — a **tree-level O(1)** birefringence-bearing structure that the QED
vacuum **LACKS** (QED's birefringence is an `α²`-loop Euler-Heisenberg effect). **QED-with-a-cutoff does NOT
reproduce it**: the Stage-2 cutoff (correction 1) makes loops finite but adds no tree-level birefringence; the
birefringence comes from the saturating-ε (Axiom 4), a structure QED has no analog for at tree level. That
existence is the chord.

**The MAGNITUDE is an α-ECHO.** `δn_AVE/δn_QED = (1/2)/((3/45)α²)·(E_crit/E_yield)² = (45/6)/α³ = 7.5/α³ ≈
1.930×10⁷`, using `E_crit=α^(−1/2)E_yield` so `(E_crit/E_yield)²=1/α=137.036` (verified to rtol 1e-9). This
number **rides α⁻³** — and **AVE imports α** (it is QED's coupling; §8), so the magnitude is a **value-level
echo**, NOT a chord. **Symmetric standard:** QED's `a_EH α²` is **equally** α-rooted — QED does not derive α
either. Do NOT headline the magnitude as a chord (canonical: `vacuum-birefringence-e4.md`:43, "Chord vs echo").

**The discriminator is the E-route. Static-B is a corroborative null.** A static B has `∂B/∂t=0`, so the
μ-grade (a circulation-keyed relativistic inductor) stays unloaded (`S_μ=1`, `δn_μ=0` **exactly**) — the
PVLAS/BMV static-B null is **consistent** with AVE, not a falsifier (canonical:
`pvlas-static-b-verdict.md`:84, "The discriminating measurement is the E-route"). Do **NOT** claim static-B as
the falsifier.

**Distinct-cutoff declaration (constants.py:286-294).** Two distinct k-space ceilings, NOT conflated:

| Cutoff | Value | Role |
|---|---|---|
| SPATIAL `k_max=π/ℓ_node` | `8.135×10¹² /m` | **the LOOP-INTEGRAL bound** (this build, `K_MAX_SPATIAL`) |
| TEMPORAL `ω_C=c/ℓ_node` (`=1/ℓ_node` in 1/m) | `2.590×10¹² /m` | the μ-grade (circulation-rate) ceiling — NOT used in the loop quadrature |

ratio `k_max/(ω_C/c)=π` exactly (`3.14159265…`, verified rtol 1e-12). **The loop integral is bounded by the
SPATIAL `k_max=π/ℓ_node`** (the BZ quadrature domain edge is at `k_max`, where the dispersion saturates at
`4/ℓ²`); `ω_C` is the μ-saturation ceiling and does not enter. Conflating them is a factor-π error — guarded
by `TestDistinctCutoffDiscipline`.

## 8 · ★ FORM / VALUE ledger (the two halves sit at DIFFERENT rungs — NOT co-equal)

The load-bearing honesty point: the two corrections are at **different epistemic rungs**, and α is **imported**.

| Item | Rung | Why |
|---|---|---|
| **The ℓ_node cutoff FORM** | **FORM-DERIVED** (the more-principled-than-dim-reg half) | The momentum cutoff is NOT imposed by hand. It falls out of the EXACT discrete-Hilbert commutator (Axiom-1 lattice pitch → `p_disc=(ℏ/iℓ)sin(kℓ)` ⇒ `[x,p]=iℏ√(1−(ℓp/ℏ)²)`, `dcve-specification.md`:36-42). The Brillouin edge `k_max=π/ℓ_node` is a physical lattice fact, not a subtraction. The regulator is **α-CLEAN** (purely geometric, guard-tested). |
| **The saturating-ε (birefringence kernel)** | **FORM-POSTULATED** | The kernel `S(A)=√(1−A²)` IS Axiom 4. It is not derived from a deeper structure here; it is the postulated non-linearity. (REUSED from `scale_invariant`, not re-minted.) |
| **α (the coupling)** | **VALUE-IMPORTED** | α is QED's coupling. AVE does not derive α (Class-B echo at the value level, per the corpus α-keystone resolution). For a QED-extension this is **EXPECTED** — flagged, not pretended-clean like the gravity sector. The birefringence magnitude `7.5/α³` rides α⁻³, so it inherits the import. |

**Do NOT present the two corrections co-equal.** Correction (1)'s cutoff FORM is genuinely derived (the
strong half); correction (2)'s kernel is postulated (Axiom 4) and its magnitude imports α (the value-echo
half). The **birefringence FORM** (`δn_bir≈−½A²`, the existence of a tree-level O(1) structure) IS
substrate-native — it is only the **magnitude** that imports α. So: cutoff-FORM derived, birefringence-FORM
(existence) substrate-native, birefringence-MAGNITUDE an α-echo. Three distinct statuses, not one.

## 9 · ★ F4 HONESTY — the Lamb self-energy is the trap (do NOT write "AVE predicts the Lamb shift")

The BZ cutoff makes the **self-energy FINITE** — a **real structural win** (no renormalization, no
counterterm, the loop is finite by mode-count as §5 demonstrates). **BUT the MAGNITUDE is MATCHED, not
predicted.** Specifically, the "Bethe-log" that lands in the self-energy is structurally `ln(1/α²)` = **the
LOG OF THE CUTOFF RATIO**, NOT a dynamical Bethe logarithm, and it sits **~3.5× off** QED's real value.

- **What IS true (claim it):** the lattice cutoff regulates the self-energy to a finite value *without
  renormalization* — the divergence-removal is structural (Axiom 1).
- **What is NOT true (do NOT claim it):** "AVE predicts the Lamb shift." The numeric agreement, where it
  exists, is a **matched cutoff-ratio log**, not a derived dynamical Bethe logarithm, and it is ~3.5× off.

**This result doc makes NO Lamb-shift prediction.** (The corpus Lamb-leaf walk-back — the 137× `1/ℓ_node`
contradiction + the matched-not-predicted rescope — is a SEPARATE corpus task, not this build. This build does
not reproduce the overclaim; it only demonstrates the **finite-by-cutoff** structural property of the loop, §5.)

## 10 · How this integrates + honest flags

**Integration: QED's linear core + the ℓ_node cutoff + the saturating-ε birefringence.** Stage-2 is a
**correction ON the inherited QED/Maxwell solver**, not a replacement. The continuum propagator
(`|k|²−ω²/c²`) is the low-momentum limit and is recovered identically at `qℓ≪1` (§4). The two Stage-2
additions are: (1) the **Brillouin-zone cutoff** — at low momentum the lattice dispersion → continuum (QED
recovered, consistency); at the BZ edge the dispersion band-limits and loops go finite (the regulator,
manifestation); and (2) the **saturating-ε birefringence** — at low field `δn_bir→0` (no tree birefringence,
consistency); at high field the tree-level O(1) differential appears (the chord, manifestation). Stage-2 is
the second rung of the GR/QED-extension engine; it shares the canonical Op14 kernel and the ℓ_node scale with
the rest of the framework (and with Stage-1's GR-extension, which uses the SAME `S(A)`).

**Honest flags + spec deviations:**

1. **No spec deviations on the load-bearing requirements.** The cutoff FORM is FORM-DERIVED from the exact
   commutator (§8); the saturating-ε is REUSED, not re-minted (the module imports the SAME
   `scale_invariant.saturation_factor` that `fdtd_3d._compute_local_epsilon` uses — guard-tested
   `n_⊥²=S(A)` bit-identical); the distinct-cutoff discipline is declared (loop bound = SPATIAL `k_max=π/ℓ_node`,
   NOT `ω_C`, ratio π — guard-tested); the chord is framed as **existence** (the magnitude is flagged an
   α-echo, §7-§8); the F4 Lamb honesty is carried verbatim (§9).
2. **The continuum branch carries no AVE claim.** `continuum_loop_integral` exists ONLY to exhibit the
   divergence the BZ cutoff removes (the side-by-side contrast in §5). It is not an AVE prediction; the AVE
   content is the finite BZ integral.
3. **Both observables are analytic, not engine-dynamically-evolved (Checkpoint 9).** The loop integral is a
   BZ quadrature; the birefringence is an ε→n algebraic map reusing the existing `_compute_local_epsilon`
   kernel. This is correct for a loop-regulator / index DEMONSTRATION (the spec asks for the loop-integral
   STRUCTURE and the index map, not a time-marched FDTD birefringence run). Stated for transparency — a
   time-domain FDTD birefringence driver (with reactance-pair tracking, Checkpoint 6) would be a separate,
   heavier build if a dynamical confirmation is later wanted.
4. **The bond sum uses the 3 cubic axes (the simplest BZ).** `lattice_dispersion_denominator` sums over the
   three cubic axes; the K4 diamond stencil shares the same `kℓ≪1` continuum limit (the recover-QED leg is
   stencil-independent at leading order). The exact BZ shape (cubic vs K4-diamond) affects only the
   sub-leading band structure and the precise finite value of the loop integral, not the FINITE-vs-DIVERGENT
   contrast or the recover-QED limit. A K4-diamond BZ refinement is deferred (it would not change either
   two-test verdict).
5. **α-echo, flagged not hidden.** The `7.5/α³` magnitude is an α-echo (§8); the result doc headlines the
   **existence** chord, never the magnitude, per the canonical `vacuum-birefringence-e4.md`:43 "Chord vs echo"
   split and the symmetric standard (QED's `a_EH α²` is equally α-rooted).

---

**Branch:** `analysis/grqed-stage2-qed-extension` · **next:** Grant merges via reviewed PR (not merged here).
