# Deep-Rail k-Scaling Adjudicator — FROZEN pre-registration (ρ_N(k·r_core): the gravitational-sector survival measurement)

**Date:** 2026-07-20
**Class:** DERIVATION + lattice-derived research-driver (research-doc; **forms derived, values calibration/observation-imported and tagged; mints no `clm-`, propagates to no KB/tex leaf**). This is COMMIT 1 — the pre-registration ALONE, frozen and pushed before any derivation or driver code (the #761/#767/#770 frozen-first discipline).
**Provenance:** Grant-fired 2026-07-20 (verbatim `[sic]`: `"word"`, item-2 `"Proceed"`). THE decisive adjudicator discharging merged **#770**'s §8.2 owed follow-on (which discharges #767 §6.2-1). #770 re-banked its BIN-1-CLEAN kill to **WALL-CLASS / RAIL-DEPTH-CONDITIONAL → REOPENED**: the canon bulk-only wall IS realizable (`Γ_bulk→−1` with `c_S` finite `0.177` at `S_RAIL→0`), and at deep rail `ρ_N` plateaus `~0.3` (flat-to-falling `N4→N8`) while `κ_ensemble²` sits `78–152×` over the bound at ALL measured depths. The fork #767 left open REMAINS OPEN; #770 named the decisive adjudicator as the deep-rail frozen-first program. This lane is that program.
**★THE decisive question (the single measurement the sector turns on):** **how does `ρ_N` scale with `k·r_core`?** The lattice runs at `k·r_core ~ O(1)`; the physical regime is `~10⁻²⁵`. If the per-core Lloyd suppression carries a falling power law `ρ_N ∝ (k·r_core)^p` (`p>0`) into the ensemble, physical-scale `ρ_N` is astronomically below the survival threshold (§1) ⇒ BIN-2 / Reading-B re-open grounds. If the plateau is `k`-independent, the `78×` floor stands ⇒ the kill banks clean at every level.
**Lane fences:** DERIVATION lane only. Engine `src/ave` **BYTE-UNTOUCHED** (imports read-only; all cage/ensemble/driven dynamics live in the driver under `research/drivers/`). **No** `manuscript/` or `manuscript/ave-kb/` `.tex`/`.md` leaf edits; **no** port-register edit; **no** un-revert; **no** falsification-ledger edit — regardless of outcome. Consequence ROUTED to Grant only. Every `[canon]` input content-verified two-method at base HEAD `d3203d37` (verify-before-cite). #770/#767/#761 content cited from merged `origin/main`. Pulsar figures `[import]`-tagged.

> **FREEZE STATEMENT.** This document freezes: (i) the survival THRESHOLD `ρ_N ≤ κ_max²/κ_env²` recomputed exactly from the banked numbers (§1); (ii) the four verdict BINS + the CONSISTENCY GATE (shear) + the ANTI-SEDUCTION FENCE (both ways) + the CONVERGENCE GATE + the ROUTE-COLLAPSE consistency check (§2); (iii) the `k·r_core` DEFINITION + the frozen candidate SCALING FORMS + the frozen MODEL-COMPARISON criterion (§3); (iv) the per-LEG frozen discriminators (§4, feasibility-assessed); (v) the UNDETERMINED fork guard (§5). Nothing below §5 is a result — the derivation and driver land in later commits. **The verdict may cite ONLY the frozen criteria's outputs.**

---

## §0 — REGIME / SECTOR / PHASE-STATE header + substrate-native walk + phase-space check

**MODE.** A non-relativistic compact binary (Hulse-Taylor B1913+16, `v/c~10⁻³`; double pulsar J0737-3039A/B, `v/c~2×10⁻³`) as a **source**. The object under test is the ENSEMBLE of ~`10⁵⁷` constituent solitons, each canonically carrying a **bulk-only `Γ_bulk=−1` cage at its knot core** (`electron-bh-isomorphism.md:26` `[canon]`). Contrast column: the observed `Ṗ_b` matched to the GR shear-quadrupole `[import]`.

**REGIME.** Regime-I cold-linear far field (`V_GW/V_snap~10⁻²⁵`); **caged sources** realized by CONSTITUTIVE GRADING of the bond stiffnesses toward the rail (`S(A)→0`) on a `~1`-node shell — NOT a kinematic pin (the #767/#770 lesson). At DEEP rail (`S_RAIL ≤ 1e-4`, `Γ_bulk ≤ −0.95`) the cage is the near-melt bulk-only wall.

**PHASE-STATE.** Cold-reactive far field (Ax3-lossless-reactive), saturated cage shells (`S(A)→0` at the cage contour). Far-field radiation is a legal Ax3 loss channel (port-not-valve) — in the driven Leg-K primitive it is emulated by an outer graded-damping SPONGE ring (the outgoing-radiation port), never a numerical valve inside the measured region.

**SECTOR.** Observed GW = **T2 transverse shear** at `c`. Channel under test = **A1 bulk/compression** (mass sector), radiative P-branch. **Sector-ownership discipline (do NOT cross-wire):** A1 owns compression/mass/dilatation; T2 owns shear/GW; the `(2,3)` Cosserat winding owns charge/spin (`master-equation.md:20` `[canon]`). The A1⊥T2 knot-core sector-ownership question (which impedances collapse — Fork W) is the un-derived residual #770 routed to Grant; this lane does NOT pick it.

**A46 PHASE-SPACE-COORDINATE CHECK.** The Lloyd claim under test (walk RECORD §6-3 `[walk-level]`, verbatim: *"a compression source against its own `Γ=−1` (stress-release) boundary has its long-wavelength radiative moment cancelled by its inverted image … with residuals suppressed by powers of `(k·r_core)`; **the static texture `∝M` is untouched**"*) is a **RADIATIVE-MOMENT** claim, in the **longitudinal (`∇·u`, radial) vs transverse (`∇×u`, tangential) energy partition of the RADIATED field**. ★A46-critical distinction this lane freezes: the Lloyd suppression acts on the **radiative (drive-frequency) moment ONLY** — the **static/DC texture (the mass) is EXPLICITLY untouched**. Therefore the k-scaling MUST be measured on the **radiative** compression moment (isolated at the drive frequency `Ω` by lock-in — Leg K), NOT on a static-release shell energy (which is dominated by the untouched texture and does NOT test Lloyd — Leg K-static is the fenced texture control). `κ² ≡ F_∥/F_⊥` in the channel basis. A46-clean.

**SUBSTRATE-NATIVE WALK (fired before scaffolding any primitive; Rule-14 reuse).**
1. **K4 connectivity.** Rule-14 reuse of the #770 / `srs_band_survey` rank-2 bond model on the chiral srs-z3 net (`ave.core.chiral_lattice._SRS_8A/_NN`; `Φ_b = k_a d̂⊗d̂ + k_s(I−d̂⊗d̂)`; derived `ρ*=9.77337` from `ν_Hill=2/7`). No new stencil; NOT a Cartesian Laplacian.
2. **Cosserat / channel basis.** Partition radiated + static fields into radial (longitudinal, P — compression/A1) AND tangential (transverse, S — shear/T2). S-branch survival is the consistency gate.
3. **Op14 saturation — the deep-rail cage.** `S(A)=√(1−(A/A_yield)²)→0` grades the local bond stiffness toward the rail (`eq_axiom_4.tex:7` `[canon]`). Realized as a static constitutive grade on the bond tensors; DEEP rail (`S_RAIL ≤ 1e-4`) drives `Γ_bulk→−1` (the #770 review-repair ladder — now justified as canon-realizable).
4. **Phase-space vs real-space (A46).** Observable = channel-basis dilatation/energy partition of the RADIATIVE moment (above); NOT a `φ²` proxy.
5. **Checkpoint 8 (emergence/hosting) — FALLBACK.** A self-bound saturated soliton is INFEASIBLE on the lossless engine (electron-lock arc). Cages are constitutive grades; interiors driven/seeded by FREE dynamics (a body-force drive or an initial condition — NO kinematic pin on the source path).
6. **Checkpoint 10 (boundary-not-bulk).** The cage is a bounded operating-point BIAS on the coefficients (a graded shell, `~1` node thick), NOT a bulk force.

**PRE-TEST PHYSICS CHECK (Rule 16; one plumber-physical question surfaced to Grant BEFORE the framing locks).** *Grant — plumber-physically: the Lloyd image-cancellation is a LONG-WAVELENGTH (quasistatic, `k·r_core→0`) theorem — a source and its inverted image merge into a `(k·r_core)²`-suppressed multipole only when the wavelength dwarfs the cage. On the lattice we can only reach `k·r_core ~ O(1)`, where a deep-rail (`Γ_bulk=−1`) cage is a RESONANT CAVITY (first trapped-mode resonance at `k·r_core ≈ π`), not a quasistatic Lloyd mirror. So the lattice samples the RESONANT regime, the real system the QUASISTATIC regime — two qualitatively different regimes on opposite sides of the fundamental cage resonance. Is the honest deliverable therefore (a) an ANALYTIC derivation of the quasistatic `p` (Leg A) that the lattice can only bracket/bound, not validate; or (b) do you read a plateau/enhancement over the accessible `O(1)` band as itself decisive?* Surfaced now, not after the run.

---

## §1 — THE SURVIVAL THRESHOLD (recomputed exactly from the banked numbers)

**Effective-coupling definition (frozen, #770-parity).** `κ² ≡ F_bulk/F_shear`, the channel-basis flux ratio the orbiting ensemble's net mass moment presents to the compression (P) channel; the extra fractional orbital-energy-loss the pulsar over-determines is `ΔṖ_b/Ṗ_b = κ²`.

**The suppression ratio (the k-scan observable).** `ρ_N ≡ F_bulk^caged(N)/F_bulk^uncaged(N)` — the caged/uncaged far-field compression at identical source geometry (the cage is the only difference ⇒ `ρ_N` removes the fixed geometry). Then `κ_ensemble² = ρ_N · κ_env²`.

**Frozen imports (`[import]`, WebFetch-verified in q1 §2.2, banked in #767/#770):**

| Bound | `κ_max² = δ` | Source `[import]` |
|---|---|---|
| **Double pulsar J0737 (BINDING)** | **`1.3×10⁻⁴`** | Kramer et al. 2021, PRX 11, 041050 (arXiv:2112.06795) |
| Hulse-Taylor B1913+16 (cross-check) | `1.6×10⁻³` | Weisberg & Huang 2016, ApJ 829, 55 (arXiv:1606.02744) |

**Uncaged coarse-grained baseline (`[canon-#767]`):** `κ_env² = 0.034`.

$$\boxed{\ \rho_N^{\rm survive} \;\le\; \frac{\kappa_{\max}^2}{\kappa_{\rm env}^2} \;=\; \frac{1.3\times10^{-4}}{0.034} \;=\; 3.82\times10^{-3}\ \ \text{(double-pulsar, binding)}\ }$$

Cross-check (HT, looser): `ρ_N^survive ≤ 1.6×10⁻³/0.034 = 4.7×10⁻²`. **The `78×` floor arithmetic (frozen):** the #770 deep-rail static plateau `ρ_N ~ 0.30` gives `κ_ensemble² = 0.30·0.034 = 0.0102 = 78×` over `κ_max²`; the shallow `ρ_N ~ 0.58` gives `152×`. Survival requires `ρ_N` fall by `≥ 78×` (to `≤ 3.82×10⁻³`) from the deep-rail static floor — the `(k·r_core)^p` scaling is the only route to that fall.

---

## §2 — THE FROZEN BINS + gates + anti-seduction fence

**BIN 1 — SCALING-SUPPRESSED.** The verdict-controlling RADIATIVE `ρ_N(k·r_core)` (Leg K) FALLS with a frozen-form fit (Lloyd `(k·r)²`-class or another positive power `p>0`) whose extrapolation at the physical `k·r_core ~ 10⁻²⁵` lands **below the survival threshold** (§1), AND the shear stays at full coupling (consistency gate) ⇒ a DERIVED suppression EXISTS ⇒ Reading-B re-open grounds. **CONSEQUENCE ROUTED TO GRANT ONLY** — no port-register/ledger edit, no un-revert. This lane executes NOTHING; it surfaces the mechanism + the driver's frozen outputs.

**BIN 2 — SCALING-FLAT.** `ρ_N` is `k`-independent within the frozen tolerance across the achievable range (the fit prefers the constant form; no positive power is resolved) ⇒ the `78×` floor stands ⇒ the kill is confirmed at every level, the fork CLOSED. *Consequence: the standing Reading-A exclusion + reverted Q1 ruling STAND; #767's "structurally unreachable" strengthening becomes EARNED at the constituent k-scaling level. Routed, not executed.*

**BIN 3 — MIXED / FORM-UNDETERMINED.** The data cannot discriminate the frozen candidate forms — because (any of): the achievable `k·r_core` band is confined to the RESONANT regime (`k·r_core ≳ π`) where the deep-rail cage cavity dominates; the low-`k` (quasistatic) points fail the CONVERGENCE GATE (sponge-radiation-port fails at wavelengths `≳` sponge thickness); the two routes (vary `Ω` vs vary `r_cage`) do NOT collapse; or no frozen form fits within the model-comparison tolerance ⇒ **state EXACTLY what range/precision/box would discriminate them** (and let the analytic Leg A carry the quasistatic form with declared un-validated scope). NOT a rescue; NOT a kill; the honest "the decisive measurement is not lattice-accessible in the quasistatic regime."

**BIN 4 — UNDETERMINED.** An unforced verdict-controlling choice (which observable — radiative vs static; which cage realization; which fit space) not forced by the substrate ⇒ STOP, state the fork precisely (§5), do NOT pick by fiat.

**★THE CONSISTENCY GATE (frozen, shear).** In every configuration read as a BIN-1 (suppression), the observed SHEAR (transverse) far-field coupling MUST stay at the uncaged rate within the resolvable window — the channel-asymmetry (compression suppressed, shear alive) IS the BIN-1 signature and the canon bulk-only wall (`electron-bh-isomorphism.md:26`: `Γ_bulk=−1`, shear un-melted). Operationally: the shear ratio `σ_N ≡ F_shear^caged/F_shear^uncaged` must satisfy `σ_N ≥ 1 − τ_shear` with `τ_shear` frozen (§4 Leg S) in the verdict configurations. **The symmetric (full-rail) wall is EXPECTED to kill BOTH channels** — wall-class data, FENCED from being read as a falsification.

**★ANTI-SEDUCTION FENCE, BOTH WAYS (frozen; the #770 lesson NAMED).** Three prior lanes in this arc landed kill-direction with load-bearing defects caught by review (#761 window mechanics; #767 star-strawman; **#770 inverted theorem + a FABRICATED `"ROBUST … pressure-tested"` robustness string hard-coded into the driver JSON while no scan was run**). Kill-momentum is a DEMONSTRATED failure mode. AND the suppression direction now carries its OWN seduction — the walk's Lloyd picture "winning" twice (#770 reopened toward realizability). **This lane is inside BOTH blast radii.** Two frozen rules:
1. **EVERY scan claimed MUST ship its data AND its code path** (the deterministic driver + `_results.json`) — NO prose-string conclusions (the #770 lesson, named). The verdict cites ONLY frozen-criteria outputs read from the shipped JSON.
2. The verdict section may cite ONLY: the §1 threshold; the Leg-K RADIATIVE `ρ_N(k·r_core)` fit + its model-comparison output + the convergence-gate + route-collapse flags; the Leg-W rail-depth ladder (`run_c2_speeds`); the Leg-C1 converged charged-line; the consistency-gate shear. Every other measurement is POST-HOC characterization, labeled and quarantined.

**★THE CONVERGENCE GATE (frozen — the empirical-driver-discipline deliverable, thrice-owed).** A driven Leg-K point is ADMISSIBLE to the fit ONLY if BOTH: (i) the steady-state energy-drift over the lock-in window `|ΔH/H|_win ≤ 0.30`; (ii) `ρ_N` is stable vs settle-time (`|ρ_N(settle=7·t_cross) − ρ_N(settle=5·t_cross)| ≤ 0.05` at the reference point). Points failing (i) are marked NON-ADMISSIBLE (typically the low-`Ω`, longest-wavelength points where the finite sponge under-absorbs) and EXCLUDED from the fit — DISCLOSED, never silently dropped. **The energy-drift `|ΔH/H|_win` and the seed/drive transverse fraction ARE reported for every configuration** (the twice-dropped #770 deliverables — third time is a pattern).

**★THE ROUTE-COLLAPSE CONSISTENCY CHECK (frozen).** `k·r_core` is a dimensionless ratio reachable by two independent knobs: vary the drive frequency `Ω` (Route Ω) and vary the core radius `r_cage` (Route r). If `k·r_core` is the controlling variable, the two routes must COLLAPSE onto a single `ρ_N(k·r_core)` curve within `30%` at matched `k·r_core`. **Non-collapse ⇒ the dimensionless ratio is NOT the controlling variable on the lattice ⇒ FORM-UNDETERMINED (BIN 3), stated, not forced into a fit.**

---

## §3 — THE `k·r_core` DEFINITION + frozen candidate forms + frozen model-comparison

**★`k·r_core` DEFINITION (frozen).** For the RADIATIVE (driven) measurement: `k·r_core ≡ Ω·r_cage / c_P,cold`, where `Ω` is the harmonic drive angular frequency, `r_cage` the cage contour radius, and `c_P,cold` the cold-lattice longitudinal Bloch speed from `run_c2_speeds(ρ*, k_s)` (the frozen normalizing speed — reported once). For the STATIC texture control: `k·r_core ≡ r_cage/σ` with `σ` the seed scale (declared as the texture-control coordinate; it is NOT the verdict coordinate — the static observable does not test Lloyd, §0 A46). The first cage cavity resonance sits at `k·r_core ≈ π`; the SUB-RESONANT band `k·r_core < π` is the Lloyd-relevant band.

**★FROZEN CANDIDATE SCALING FORMS (fit ALL; the fit is on the RADIATIVE `ρ_N`, Leg K, admissible points only).**
- **F0 — constant:** `ρ_N = a` (the plateau / `k`-independent = BIN-2 shape).
- **F2 — Lloyd:** `ρ_N = a·(k·r_core)²` (the derived quasistatic power, Leg A prediction).
- **Fp — free power:** `ρ_N = a·(k·r_core)^p` (`p` free).
- **Fap — plateau+power:** `ρ_N = a + b·(k·r_core)^p` (a floor plus a scaling residual).

**★FROZEN MODEL-COMPARISON CRITERION.** Fit each form by least-squares on `log ρ_N` vs `log(k·r_core)` (the power forms are linear there; F0 is a constant in `log ρ_N`; Fap fit in linear `ρ_N`, its residual mapped to `log ρ_N` for comparability), over the ADMISSIBLE points (convergence-gate pass) from BOTH routes pooled. Compare by **corrected Akaike information `AICc = n·ln(RSS/n) + 2k + 2k(k+1)/(n−k−1)`** (small-sample AIC; `k` = #params incl. variance). The preferred form is min-AICc; report `ΔAICc` vs each competitor and the best-fit `p` (Fp) with its 1σ. **Discriminator (frozen):**
- Fp/F2 preferred with `p` resolved `> 0` at `>2σ` AND the F2/Fp extrapolation to `k·r_core=10⁻²⁵` `< 3.82×10⁻³` ⇒ **BIN 1 (SCALING-SUPPRESSED)** (consistency gate must also pass).
- F0 preferred (or `p` consistent with `0` within `2σ`, or `b≈0` in Fap) within `ΔAICc < 2` of the alternatives ⇒ **BIN 2 (SCALING-FLAT)**.
- No form preferred at `ΔAICc ≥ 2`, OR `< 4` admissible points, OR routes fail collapse, OR convergence gate voids the sub-resonant band ⇒ **BIN 3 (MIXED/FORM-UNDETERMINED)**.

---

## §4 — FROZEN LEG CRITERIA (feasibility-assessed; refined and frozen before the verdict run)

**Grid FROZEN.** Driven Leg-K primitive: `L=24` supercell (baseline; `N=1` isolated core centered), outer graded-damping SPONGE ring (thickness `sponge_w=6`, quadratic profile `γ(r)=γ₀((|x|−edge)/sponge_w)²`, `γ₀=4`), radiative lock-in shell at `r_meas` INSIDE the sponge (`r_meas ≤ half − sponge_w − 1.5`; PML-excluded — the shell never lies in a damped cell), `cfl=0.2`, harmonic radial body-force drive (a compression source, NO kinematic pin) with a smooth half-cosine ramp over the first half of the settle, lock-in of the shell radial (`F_bulk`) and tangential (`F_shear`) displacement onto `sin Ωt`/`cos Ωt`. Settle `= 5·t_cross` (reference-point convergence probe also at `7·t_cross`), lock-in `= 8` drive periods. **Determinism (frozen):** fixed seed (`run_c2_speeds` seed=1; no per-step RNG in the dynamics); reruns bit-identical.

### Leg K — THE CENTERPIECE: `ρ_N(k·r_core)` scan (RADIATIVE, driven + lock-in)
Deep rail only (`S_RAIL = 1e-4`, `Γ_bulk ≤ −0.95`; `1e-6` cross-check). `N=1` isolated core (the Leg-A single-core Lloyd test) is the frozen verdict class (feasibility: the driven ensemble `N=4` does not fit the sponge+shell inside `L=24`; `N=4` radiative sampling is a declared best-effort at larger `L` if compute allows, else the STATIC `N=1..8` ensemble `ρ_N` (below) carries the aggregation question and Leg A carries "does aggregation preserve `p`?"). Scan `k·r_core` across the achievable band via **Route Ω** (vary `Ω`, `r_cage=1.6`) AND **Route r** (vary `r_cage`, fix `Ω`). Report per point: `ρ_N`, `F_bulk`, `F_shear`, `σ_N` (shear ratio), `|ΔH/H|_win`, drive transverse fraction, admissible-flag. Fit the frozen forms over admissible points; model-comparison per §3. **Frozen static texture control (reuse `leg5_ensemble_scaling`, `k·r_core=r_cage/σ`):** the STATIC-release `ρ_N` at deep rail for `N=1,2,4,8` and a `(σ, r_cage)` grid — this is the "untouched texture" (walk §6-3) and its plateau is EXPECTED and FENCED from the Lloyd verdict (§0 A46); it also delivers the aggregation `ρ_N(N)` at deep rail.

### Leg A — ANALYTIC Lloyd (the frozen FORM the data tests)
Derive the per-core image-cancellation scaling for a `Γ_bulk=−1` free (pressure-release) cage — the pressure-release image theory on the lattice / continuum acoustic analog: the predicted `p` for the residual radiative compression moment of a compact source inside its own `Γ_bulk=−1` shell, in the sub-resonant (`k·r_core < π`) quasistatic limit; the soft-sphere (Dirichlet) monopole-cancellation structure. Then the ENSEMBLE version: does aggregation of `N` per-core residuals PRESERVE `p` (incoherent sum, `ρ_N` `N`-independent and `∝(k·r_core)^p`) or does an uncancelled coarse-grained texture emerge (`ρ_N → const`)? This is the frozen FORM (F2) the Leg-K data tests + the extrapolation vehicle to `10⁻²⁵`.

### Leg W — WALL DEPTH ladder (`run_c2_speeds`, both classes)
The frozen `S_RAIL` ladder `0.03 / 0.003 / 1e-4 / 1e-6 / 0` with shipped scan data (the #770 review-repair ladder redone under freeze): bulk-only (`k_a→rail`, `k_s` full) AND symmetric (both) `Γ_bulk`, `Γ_shear`, `c_P`, `c_S`, `c_P/c_S`. **Frozen deliverable:** confirm bulk-only `Γ_bulk → −1` with `c_S` finite as `S→0` (the canon bulk-only wall realizable); confirm symmetric `c_P/c_S` frozen `1.813` (degree-0 grade-lock); ship the shear transmission `1+Γ_shear`.

### Leg C1 — CONVERGED charged-line (redo #770 Leg-1 under FROZEN convergence criteria)
Single deep-rail cage, interior energized by a curl-free dilatation seed (FREE dynamics, no pin), measure exterior DC `∇·u` at the far shell. **Frozen convergence criteria:** window-half agreement tolerance (`|ratio(first half) − ratio(second half)|/mean ≤ 0.25`) AND relaxation residual threshold (report the trend across `r_meas ∈ {5,6,7}`). **Deliverable:** report the CONVERGED exterior DC `∇·u` (caged/uncaged) OR honestly report NON-CONVERGENCE (the #770 Leg-1 swung `0.33→1.60` across window halves — unconverged) and fall back to the frozen BINARY discriminator (does exterior `∇·u → 0`? charged vs uncharged line) only.

### Leg S — SHEAR-GATE diagnosis (understand BEFORE gating)
Diagnose the #770 `0.60×`/`0.23×` bulk-only shear readings (`σ_N`) BEFORE applying the consistency gate: near-field contamination (vary `r_meas`), wall shear-transmission (Leg-W `1+Γ_shear` at deep rail), N-dependence (`σ_N(N)`). Set the frozen tolerance `τ_shear` from the diagnosis (the wall's intrinsic `1+Γ_shear` at deep rail is the floor the gate must not mistake for a cage effect). Then apply the gate: shear at full coupling within `τ_shear` in the verdict configurations.

**DISCLOSE all deviations** per the now-standard §-deviations pattern; energy-drift `|ΔH/H|` + seed/drive transverse fraction reported for every configuration (the twice-dropped #770 deliverables).

---

## §5 — THE UNDETERMINED FORK GUARD (state precisely; do NOT pick by fiat)

**Fork R — regime (the verdict-controlling one).** The Lloyd `(k·r_core)²` suppression is a QUASISTATIC (`k·r_core→0`) theorem; the lattice reaches only `k·r_core ~ O(1)`, straddling the fundamental cage cavity resonance (`k·r_core ≈ π`). If the achievable admissible band lies in the resonant regime (or the convergence gate voids the sub-resonant band), the lattice CANNOT validate the quasistatic form ⇒ BIN 3, with Leg A carrying the analytic `p` at declared un-validated scope. **Frozen resolution rule:** the model-comparison (§3) + the convergence gate + the route-collapse check decide it empirically; a clean sub-resonant power law forces BIN 1, a clean plateau BIN 2, an un-discriminable/resonance-dominated/non-collapsing band BIN 3.

**Fork O — observable (radiative vs static).** The Lloyd claim is about the RADIATIVE moment; the static texture is EXPLICITLY untouched (walk §6-3). The verdict coordinate is FROZEN as the RADIATIVE (driven, lock-in) `ρ_N` (§0 A46). A static-release plateau is EXPECTED and is NOT a BIN-2 flat verdict — it is the texture control. **Frozen resolution rule:** if the radiative measurement is inadmissible (convergence gate) and only the static plateau survives, that is BIN 3 (the correct observable is not accessible), NOT BIN 2 — do NOT let the static texture masquerade as the radiative flat.

**Fork W — which `Γ` a knot core presents to each channel (the ASYMMETRY PARADOX, from #770, unchanged).** The derived `S(A)` kernel grades bulk AND shear together (degree-0, `electron-bh-isomorphism.md:38`/PR#521); canon ASSERTS the constituent wall is bulk-only (`:26`). #770 showed the bulk-only wall IS impedance-realizable at deep rail (`k_a`-only rail ⇒ `Γ_bulk→−1`, `c_S` finite) but the physical MODE/GEOMETRY mechanism is un-derived. **Frozen resolution rule:** this lane uses the `k_a`-only surrogate (canon-realizable per #770) and does NOT pick the sector-ownership mechanism; if the verdict turns on it, route to Grant.

---

## §6 — Calibration-vs-derived ledger (tags frozen) + owed follow-ons fence

**Ledger tags (`consistency-vs-emergence`, frozen).** `κ_max` is `[derived]` from `[import]` pulsar `δ` (MANIFESTATION given the imports). `κ_env²=0.034` is `[canon-#767]`. The survival threshold `ρ_N ≤ 3.82×10⁻³` is `[derived]` arithmetic of the imports. The cage `Γ_bulk=−1=pressure-release`, the image-inversion, and the Lloyd `(k·r_core)^p` FORM are `[derived]` (theorem of the `Z_bulk→0` boundary + the mechanical impedance analogy `×` `[canon-read]` `master-equation.md:107`; `electron-bh-isomorphism.md:26`). The bulk-only wall's channel-asymmetry is `[assumed]`-surrogate (un-derived mechanism; canon-asserted `:26`; impedance-realizable per #770). The `c_P/c_S` speeds are CONSISTENCY-class (`K=2G` GR-imported, PR#261). Leg-K `ρ_N(k·r_core)` + the fitted `p` are `[derived]` (lattice-measured, dimensionless). **No emergence-class claim headlined.**

**Owed follow-ons (fenced; NOT executed here — Rule 12; slot NOT refilled with an assertion).**
1. If BIN 1: the derived channel-asymmetric suppression + its extrapolation becomes a NEW derivation with its own version + verification chain; the re-open of the reverted Q1 ruling is Grant's alone; the auditor lands any port-register/ledger edit. This lane surfaces + routes.
2. If BIN 2: the standing Reading-A exclusion + reverted ruling STAND; #767's "structurally unreachable" strengthening becomes EARNED at the k-scaling level; the auditor may land it — this lane surfaces, does not land.
3. If BIN 3: state the regime gap with the analytic Leg-A form + the exact range/precision/box that would discriminate; route to Grant; no side picked; no rescue minted (Rule 11/12).
4. If BIN 4: the fork is stated; corpus + Grant consulted before any methodology pivot (Rule 16); no fiat pick.

---

> **Pre-registration provenance.** Fired by Grant 2026-07-20 (`"word"`, item-2 `"Proceed"` `[sic]`). This is COMMIT 1 — the prereg ALONE, frozen and pushed before any derivation or driver (the #761/#767/#770 frozen-first discipline). All `[canon]` citations content-verified two-method at base HEAD `d3203d37` (verify-before-cite); #770/#767/#761 content from merged `origin/main`; pulsar figures `[import]`, WebFetch-verified in q1 §2.2. Survival threshold `ρ_N ≤ 3.82×10⁻³` recomputed from the banked `κ_max²=1.3×10⁻⁴` / `κ_env²=0.034` by this lane's driver, not chat. **Attribution:** Grant-verbatim fire; the deep-rail k-scaling formulation, the radiative-vs-static observable split, the driven-lock-in primitive, the convergence-gate + route-collapse design, and the regime-gap (Fork R) framing are this lane's (tested against #770's §8.2 owed program). Mints no `clm-`; propagates to no leaf; engine byte-untouched; port-register/ledger untouched regardless of outcome. Companions: merged **#770** (`research/2026-07-20_constituent-cage-ensemble_result.md` §8.2, `_prereg-FROZEN.md`, `_derivation.md`, driver `research/drivers/constituent_cage_ensemble.py`), merged **#767**/#761, the walk RECORD (`research/2026-07-20_envelope-boundary-walk_RECORD.md` §6-3), the q1 hardening (`research/2026-07-20_q1-pulsar-hardening.md` §2.2), `electron-bh-isomorphism.md:26`, the port register P9/Q1, and the docket continuation (`### ENTRY 2026-07-20-deep-rail-kscaling`).
