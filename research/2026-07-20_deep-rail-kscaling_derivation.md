# Deep-Rail k-Scaling — analytic Leg A (the Lloyd form) + the regime-gap statement

**Date:** 2026-07-20
**Class:** DERIVATION (analytic companion to `research/2026-07-20_deep-rail-kscaling_prereg-FROZEN.md` and the driver `research/drivers/deep_rail_kscaling.py`). Forms `[derived]`; canon inputs `[canon-read]` two-method at base HEAD `d3203d37`. Mints no `clm-`; propagates to no leaf.
**Scope:** Leg A is ANALYTIC — it derives the FROZEN candidate form F2 (`ρ_N ∝ (k·r_core)²`) the Leg-K lattice data tests, and states precisely the REGIME GAP (Fork R) that decides whether the lattice can validate it. Legs W/C1/S/K are the lattice-derived empirical legs (driver + result).

---

## §1 — LEG A: the pressure-release (Γ_bulk=−1) image / Lloyd scaling `[derived]`

**The claim under test (walk RECORD §6-3 `[walk-level]`, verbatim `[sic]`):** *"a compression source against its own `Γ = −1` (stress-release) boundary has its long-wavelength radiative moment cancelled by its inverted image (textbook underwater-acoustics anchor), with residuals suppressed by powers of `(k·r_core)`; the static texture `∝ M` is untouched."*

**Setup (the acoustic analog on the srs A1/compression channel).** A compact curl-free (dilatation) compression source of characteristic size `~σ` sits inside its own cage — a shell at radius `r_core` where the bond stiffness grades to the rail (`S(A)→0 ⇒ Z_bulk = ρc_P ∝ √K → 0`). By the convention freeze (prereg §0; `master-equation.md:107` `[canon]`, `Z→0 ⇒ Γ→−1` "short-circuit"), the shell is a **pressure-release (free-surface) boundary** to the exterior compression channel: `Γ_bulk = −1`, the acoustic Dirichlet (soft) boundary `p = 0` on the contour.

**Step 1 — the image / multipole cancellation (`p = 2`).** Two equivalent readings, both giving the leading residual `∝ (k·r_core)²`:
- **Lloyd's-mirror (planar) reading.** A monopole source at distance `d ~ r_core` from a pressure-release plane has an *inverted* image monopole (`Γ_stress = −1`). Source + inverted image = an acoustic DIPOLE of arm `2d`. The radiated compression power of a dipole relative to the un-imaged monopole is `∝ (kd)² = (k·r_core)²` in the long-wavelength (`kd ≪ 1`) limit — the textbook underwater-acoustics baffle result. The DC/static near-field texture (the `∝ M` monopole *store*) is NOT radiated and is untouched (it is the reactive added-mass field, the P9 halo object).
- **Spherical-cavity (soft-sphere) reading.** For a source at the exact center of a `p = 0` shell of radius `r_core`, the exterior compression is *perfectly* shielded below the fundamental cavity resonance (`k·r_core < π`) — `ρ_N → 0`. A source displaced from center by `~r_core` (a realistic constituent, not perfectly centered) leaks its leading uncancelled multipole with amplitude `∝ (k·r_core)`, hence radiated POWER `∝ (k·r_core)²`. Same exponent.

$$\boxed{\ \text{Leg A (single core, sub-resonant quasistatic):}\quad \rho_1(k\,r_{\rm core}) \;\propto\; (k\,r_{\rm core})^{2}\ \ (p = 2)\ }$$

This is the frozen form **F2**. At the physical `k·r_core ~ 10⁻²⁵`, `ρ_1 ~ 10⁻⁵⁰` — astronomically below the survival threshold `ρ_N ≤ 3.82×10⁻³` (prereg §1). IF this per-core suppression holds AND survives aggregation, the pulsar kill is evaded (BIN-1 SCALING-SUPPRESSED).

**Step 2 — does aggregation preserve `p`? (the ensemble fork).** `N` cores, each with its residual dipole `∝ (k·r_core)²`:
- **Incoherent (dipoles uncorrelated in orientation).** Ensemble radiated power `= N ×` per-core; uncaged ensemble `= N ×` uncaged per-core; so `ρ_N = ρ_1 ∝ (k·r_core)²`, **`N`-independent — `p` PRESERVED.** BIN-1 route (i): image-cancelled sum.
- **Coarse-grained-texture (an uncancelled net compression emerges between/across cores).** If the inter-core medium compresses coherently as the whole ensemble accelerates — a net monopole no single cage shields — that texture radiates with NO `(k·r_core)²` suppression, and `ρ_N → const` (a `k`-independent plateau, the `78×` floor). BIN-2 route (ii): coarse-grained texture.

**The fork is empirical:** `ρ_N(k·r_core)` — falling power (F2/Fp) = image-cancelled sum survives; plateau (F0) = texture emerges. This is exactly the frozen model-comparison the Leg-K data feeds (prereg §3).

**★A46-critical distinction (frozen).** The Lloyd suppression acts on the **RADIATIVE** (drive-frequency `Ω`) moment ONLY. The **static/DC texture (the mass `∝ M`) is EXPLICITLY untouched** — it is the reactive near-field store, the thing that gravitates (the `7GM/c²r` refractive strain, `electron-bh-isomorphism.md:19`), not a radiated compression wave. Therefore the k-scaling that tests Lloyd MUST be the RADIATIVE moment (driven + lock-in, Leg K), NOT a static-release shell energy — the static-release `ρ_N` measures the untouched texture (its plateau `~0.3` is EXPECTED and is the fenced texture control, NOT a BIN-2 flat verdict).

---

## §2 — The REGIME GAP (Fork R): why the lattice may not validate F2 `[derived]`

**The Lloyd `(k·r_core)²` is a LONG-WAVELENGTH (quasistatic, `k·r_core → 0`) theorem.** Its derivation (Step 1) assumes `k·r_core ≪ 1`: the wavelength dwarfs the cage, so source + image merge into a single suppressed multipole. The residual is `(k·r_core)²` **below the fundamental cage cavity resonance**, which sits at `k·r_core ≈ π` (the first `p = 0` interior standing mode `k r_core = π`).

**The lattice is confined to `k·r_core ~ O(1)`** by the finite box (`L`): the drive frequency `Ω` cannot go below `~2π/(reflection-free window)` without the outgoing-radiation sponge failing (its thickness must exceed the wavelength to absorb), and `r_core` cannot go below `~1` lattice unit (the shell must be resolved). So the achievable band straddles `k·r_core ≈ π` — the fundamental cage resonance — NOT the deep quasistatic regime.

**Consequence (the crux).** At `k·r_core ~ O(1)` a deep-rail (`Γ_bulk ≈ −1`) cage is a HIGH-Q RESONANT CAVITY, not a quasistatic Lloyd mirror. The far-field compression coupling is a RESONANCE COMB (peaks where `k r_core ≈ nπ`, troughs between), NOT the smooth `(k·r_core)²` envelope. The two regimes are on OPPOSITE SIDES of the fundamental resonance:

| regime | `k·r_core` | cage behaves as | `ρ_N` |
|---|---|---|---|
| **physical (real NS constituents)** | `~10⁻²⁵` | quasistatic Lloyd mirror | `∝ (k·r_core)² → 0` (F2, IF aggregation preserves) |
| **lattice (accessible)** | `~O(1)`, straddles `π` | high-Q resonant cavity | resonance comb `~0.3–1.2` (NOT a clean power law) |

**★This is why Leg K is expected to land BIN-3 (MIXED/FORM-UNDETERMINED):** the lattice samples the RESONANT regime; it cannot reach the SUB-RESONANT quasistatic regime where F2 holds. The analytic Leg A gives the quasistatic `p = 2`, but the lattice — being out of that regime — can neither validate nor refute it. **The verdict then turns on whether the quasistatic Lloyd suppression is PHYSICALLY REALIZED (an analytic + aggregation question), which the lattice cannot decide.** What WOULD decide it empirically: reach `k·r_core ≪ π` with a sponge thicker than the (long) wavelength — requiring a box `L ≳ O(10²–10³)` (infeasible on this class of machine), OR a spherically-symmetric continuum radial solver (a different lane) that reaches the quasistatic limit analytically-cleanly.

**★Anti-seduction (both ways, applied to Leg A).** Leg A's `p = 2` is SEDUCTIVE toward BIN-1 (the walk's Lloyd picture): it predicts astronomical suppression at `10⁻²⁵`. But it is a QUASISTATIC-limit analytic form the lattice CANNOT validate, AND it does NOT settle the aggregation fork (Step 2). So Leg A must NOT be read as a backdoor BIN-1: it supplies the FORM the data tests, not a verdict. Symmetrically, the lattice's non-suppressed resonant band (`ρ_N ~ 0.3–1.2`) must NOT be read as a clean BIN-2 kill — it is the WRONG regime for the Lloyd test. The honest landing is BIN-3 with both fences held.

---

## §3 — What each leg validates / cannot establish (honest scope) `[derived]`

- **Leg W (rail ladder, `run_c2_speeds`):** VALIDATES the canon bulk-only wall is impedance-realizable at deep rail (`Γ_bulk → −1` with `c_S` finite as `S_RAIL → 0`; the #770 review-repair finding, redone under freeze). This is the ANTECEDENT the whole k-scan needs (a real `Γ_bulk = −1` cage exists). CANNOT establish the mode/geometry mechanism (Fork W, routed to Grant).
- **Leg C1 (converged charged-line):** VALIDATES whether the exterior DC `∇·u` of a deep-rail cage converges (the #770 `0.65` was unconverged, halves swung `0.33→1.60`) and whether it → 0 (uncharged/shielded, BIN-2 shape) or stays finite (charged line, BIN-1 shape). This is the STATIC shielding, a different observable from the radiative Lloyd (§1 A46).
- **Leg S (shear diagnosis):** VALIDATES the intrinsic wall shear-transmission (`1+Γ_shear` at deep rail, Leg W) and the near-field/N-dependence of `σ_N`, setting the frozen `τ_shear` so the consistency gate does not mistake the wall's intrinsic shear behavior for a cage effect. (The DRIVEN `σ_N` is uninformative — the radial compression drive is curl-free by construction, `drive_transverse_frac ~ 10⁻³²`, so the driven shear ratio is a ratio of numerical-noise and is fenced; the gate uses the static Leg-S `σ_N`.)
- **Leg K (driven `ρ_N(k·r_core)`):** the CENTERPIECE — but confined to `k·r_core ~ O(1)` (the resonant regime, §2). CANNOT establish the quasistatic F2 law; it ships the resonance-structured `ρ_N`, the convergence-gate flags, and the route-collapse check that GROUND the FORM-UNDETERMINED reading.
- **NOT establishable from an `L=24` lattice:** the sub-resonant quasistatic (`k·r_core ≪ π`) Lloyd scaling and its aggregation `p`. Leg A carries the analytic form at DECLARED un-validated scope; the decisive empirical resolution needs a box/solver that reaches `k·r_core ≪ 1` (result §-owed-follow-on).

---

> **Derivation provenance.** Analytic companion to the FROZEN prereg (`_prereg-FROZEN.md`) and the driver. Leg A derives the frozen form F2 (`ρ_N ∝ (k·r_core)²`) the Leg-K data tests, and the regime-gap (Fork R) that decides whether the lattice can validate it. `[canon-read]` two-method at base `d3203d37`: `master-equation.md:107` (`Z→0 ⇒ Γ=−1` short-circuit), `electron-bh-isomorphism.md:19,26` (refractive strain; bulk-channel TIR), the walk RECORD §6-3 (the Lloyd claim). Mints no `clm-`; propagates to no leaf; engine byte-untouched.
