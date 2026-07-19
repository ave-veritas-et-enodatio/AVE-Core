# PREREG — Thixotropy door: is there a SUBSTRATE-INTRINSIC relaxation-time asymmetry?

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-saturation-temporal-preregs` (off `main` @ f1f927c8)
**Status:** FROZEN pre-registration (corpus-grep done; no derivation run yet). The last un-refuted rectification door from the dark-wake arc (Phases 1–5).
**Companion prereg:** `2026-06-09_per-node-time-dilation-saturation-feedback_prereg.md` (the other temporal behavior of the same kernel).

---

## 1. Target (one sentence)

Does the **amplitude-dependence of the relaxation time near saturation** — τ_relax(A), the deferred `#59:77` nonlinear correction to the canonical single-τ = ℓ_node/c — produce a **genuine path-asymmetry** (effective τ on the loading path A↑ ≠ effective τ on the unloading path A↓) capable of rectifying a **symmetric** cyclic drive into net directional momentum — OR is substrate relaxation closed as **time-symmetric**, which would close the rectification-thrust space *by derivation* (an upgrade from dead-by-default to dead-by-proof)?

## 1.5 Physical picture (mechanical, no equations)

- The canonical saturation kernel S(A)=√(1−A²) is **instantaneous, memoryless, even in A** → it provably cannot rectify (the Phase 1–5 result; `substrate-hysteresis-index.md:12`).
- Canon adds **one** relaxation time: the kernel relaxes toward S_eq via a first-order ODE with τ_relax = ℓ_node/c (single, time-symmetric — `tau-relax-derivation.md:11`). The hysteresis loop ∮S dr is finite-**single**-τ lag, not two time-constants.
- Thixotropy in the strict sense = **fast-liquefy / slow-refreeze**: a relaxation time that depends on the *sign of dA/dt* (loading vs unloading), τ_load ≠ τ_unload. That is a genuine **temporal** symmetry-breaker — exactly the ingredient Phases 1–5 lacked.
- The only place it could hide: near the saturation knee, `L_eff` is itself amplitude-dependent (`#59:77`), so τ_relax(A) is no longer the constant ℓ_node/c. The question is whether that A-dependence carries a **sign(dA/dt) memory** (true thixotropy → rectifies) or is merely an **instantaneous τ(A)** (symmetric → does not rectify).
- **Must stay clear of the refuted route:** the dark-wake slow-grip/fast-slip rectification used an *externally-imposed asymmetric drive waveform* (flyback quench, `03_acoustic_rectification.tex:13`) riding the even branch-stiffness nonlinearity. That asymmetry is *put in by hand*. This prereg drives the substrate with a **symmetric** waveform — any rectification must be substrate-intrinsic.

## 2. Corpus state — GREEN-FIELD (for a substrate-intrinsic τ-asymmetry)

Per the 2026-06-09 corpus-grep (both AVE-Core mains + worktrees + siblings):

- **Single-τ symmetric is CANON.** `tau-relax-derivation.md:11` (clm-n3un96, ON MAIN): *"the per-cell saturation kernel S(A) relaxes toward its equilibrium … via a first-order ODE with time constant τ_relax = ℓ_node/c ≈ 1.288×10⁻²¹ s. The substrate is therefore memristive (path-dependent), not purely algebraic, even though the kernel form is symmetric in r."* `:84-89`: up-crossing → S>S_eq, down-crossing → S<S_eq, **both governed by the same τ_relax**. → CONTRADICTS the premise that an asymmetry already exists.
- **"Thixotropic" in canon = single-τ memristor, NOT two-τ.** `nonlinear-vacuum-capacitance.md:41-61` (clm-8nkvwy, ON MAIN) titles a section "The Vacuum Memristor (Thixotropic Hysteresis)" but the crossover frequency is set by the *single* τ_relax. `peierls-nabarro-paradox.md:12` (clm-ghs75o, ON MAIN) gives the qualitative liquefy/refreeze picture (*"mechanically liquefies … thixotropically re-freezes behind it"*) but assigns **no time constants** to liquefy vs refreeze. `temporal-saturation-regime-classifier.md:186` stick-slip = static-vs-kinetic **amplitude** asymmetry, not τ.
- **The one open seam.** `research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md:77` (ON MAIN): *"Near saturation (Op14 regime), L_eff is itself time-varying. In principle this creates a self-consistency feedback where τ_relax near saturation could differ from ℓ_node/c. For the first-order derivation here, we use the linear-regime τ_relax; nonlinear corrections are higher-order…"* — flagged, deferred, **never derived**. This is the green-field seam.
- **The hysteresis index** (`substrate-hysteresis-index.md`, **OFF-MAIN** — `AVE-Core-hysteresis-wt` / PR #145) gives the reversible-envelope vs hysteretic-crossing taxonomy, but even its "hysteretic-crossing (Level 2)" class is single-τ; its §3 explicitly flags the off-branch rrad-L rectification thread as *not yet canon*.

**Verdict:** dead-by-default on current canon (single-τ symmetric), but **not closed by derivation**. The amplitude-dependent-τ seam has never been probed.

## 2.6 Regime / phase-state scope (Grant 2026-06-09) — do NOT test in the achromatic regime

Grant's guardrail: *"look at why transverse waves have achromatic propagation in the tensor regime… apply the different regimes and states of phase."* The transverse achromaticity **localizes where thixotropy can live** — it is the control, not the test:

- **Transverse (EM/shear) propagation is ACHROMATIC** in the tensor/SYM regime: symmetric scaling μ'=n·μ₀, ε'=n·ε₀ keeps **Z=Z₀ invariant**, so *"transverse light bends through deep gravity wells without chromatic dispersion, internal scattering, or boundary back-reflection"* (`achromatic-impedance-matching.md`, clm-rd9cjm). Achromatic = frequency-independent = index set by the DC strain STATE, not frequency = **no rate-dependence**. **The transverse/shear sector is therefore structurally thixotropy-FREE** — a test there returns a guaranteed B that says nothing. **Do not look there.**
- **The BULK (longitudinal/volumetric) mode is self-steepening / dispersive.** The ρ̄ relation `c_eff²=c₀²(1+ρ̄/(1−ρ̄²))` makes c rise with compression → crest outruns trough (self-steepening, `04_superluminal_transit.tex:89`) → intrinsically nonlinear, NOT achromatic. **Thixotropy, if anywhere, lives in the bulk mode** — consistent with the temporal taxonomy (the sat/desat asymmetry is the bulk channel; companion doc §5).
- **Only near the LIMITS.** Within the bulk mode the rate-asymmetry can only appear near the compression ceiling ρ̄→+1 and the cavitation floor ρ̄_cav=−1/φ, where `#59:77`'s amplitude-dependent τ_relax(ρ̄) + self-steepening are strong — the **near-yield / nonlinear → ruptured/plasma ("black-hole pre-geodesic vacuum plasma") phase.** In the linear small-ρ̄ acoustic regime even the bulk mode is ~achromatic single-τ → no thixotropy. Dispersion onset is canonically the trans-Planckian / cubic-symmetry-breakdown scale (C7-GRB-DISPERSION) — the same lattice-scale band where achromaticity breaks.

**Phase-state map for the derivation:** Linear (achromatic, single-τ, NO thixotropy — the control) → **Nonlinear / near-yield (amplitude-dependent τ, self-steepening — the thixotropy candidate; RUN HERE)** → Ruptured / plasma / pre-geodesic (Γ=−1, pair-production — the extreme). The bulk sat/desat derivation must be done in the **near-yield bulk band**, not the linear or transverse regime.

## 3. substrate-native-check (FIRST)

- **Sector / dynamics:** time-domain LC relaxation of the saturation state S(t) toward S_eq(A); first-order memristive ODE (`tau-relax-derivation.md:78`). NOT a minimization, NOT continuum-Helmholtz.
- **The load-bearing distinction:** τ(A) (instantaneous, single-valued function of current amplitude) vs τ(A, sign dA/dt) (a true memory/state variable). Only the latter rectifies. The canonical first-order ODE has the former; the question is whether near-saturation L_eff(A) dynamics *promote* it to the latter.
- **Coordinate system:** real-space strain amplitude A and its rate dA/dt; the rectification observable is the cycle integral ∮ over a symmetric drive period (real-space, time-domain — matches the corpus claim's coordinates).
- **Reactance pair / conservation:** any time-domain verdict must track the C-state/L-state reactance pair and H=T+V over the cycle (substrate-native-check Checkpoint 6) — a "rectified" net that violates H-conservation is a numerical artifact, not a finding.

## 4. Prediction (pre-committed)

Now cast in the **bulk mode** (§2.6). τ_relax(ρ̄) **does** become amplitude-dependent near the limits (L_eff grows as the kernel stiffens). The prediction is genuinely **less confidently B than the shear case**, because the bulk mode has a concrete physical sign-asymmetry that the shear/transverse mode lacks: **self-steepening.** Because c_eff rises with compression, a **compression front sharpens** (shock-like, fast — the sat stroke) while a **rarefaction front spreads** (slow — the desat stroke). That IS the fast-liquefy/slow-refreeze picture, mechanically, and it depends on sign(dρ̄/dt). So:

- **The crack for A:** if the self-steepening compression-sharpen / rarefaction-spread asymmetry survives into a net ∮ over a symmetric drive cycle, with H conserved, then τ_bulk,sat ≠ τ_bulk,desat is real → Outcome A (rectification door open in the bulk mode).
- **Why it may still be B:** self-steepening is a *reversible* nonlinearity (it's in the conservative c_eff(ρ̄) relation, not a dissipative memory term). A reversible front-shape asymmetry can still integrate to **∮ = 0** over a closed symmetric cycle (the front sharpens on compression and re-spreads on the return — no net). It rectifies only if a genuinely **dissipative / irreversible** step (a τ that lags differently up vs down, the #59:77 amplitude-dependent τ) breaks the cycle's reversibility. The derivation's job: separate the reversible self-steepening (∮=0) from any irreversible τ-asymmetry (∮≠0).

Pre-committed lean: **50/50 A-vs-B** — the self-steepening makes this a real contest, not a foregone B. That is exactly why it's worth running.

## 5. Discriminating outcomes

- **A — REAL (new finding):** near-saturation L_eff(A) dynamics yield τ_load ≠ τ_unload (sign-dependent) → a **symmetric** cyclic drive rectifies, with H conserved. The last door is OPEN — a genuine substrate-intrinsic temporal symmetry-breaker. *Caveat before any thrust claim:* the pump/momentum ledger must still close, and it must be shown the asymmetry is NOT smuggled drive-asymmetry in disguise. This reopens a rectification route — carefully.
- **B — DEAD (closes the space by proof):** near-saturation τ depends on instantaneous A only (or the asymmetry integrates to zero over a symmetric cycle) → no intrinsic rectification → the rectification-thrust space is closed **by derivation**, upgrading the clm-7tynm2 walk-back from empirical (Phases 1–5) to structural. Clean and valuable.
- **C — NEEDS THE ENGINE:** the near-saturation L_eff(A) dynamics aren't analytically tractable → defer to a coupled-engine numerical driver (report it, don't fake an analytic answer).

## 6. Falsifier

If the canonical single-τ = ℓ_node/c is exact through the saturation knee (no A-dependence that breaks sign-symmetry), the thixotropy hypothesis is false → B. Conversely, if a symmetric-drive cycle on the amplitude-dependent-τ model encloses **nonzero** net area with H conserved, the dead-by-default verdict is wrong → A.

## 7. Guards

- **Symmetric drive only.** Any externally-imposed waveform asymmetry (fast-up/slow-down ramp, flyback quench) is the *refuted* route (`03_acoustic_rectification.tex:13`) and is banned — the drive must be a pure symmetric oscillation so any rectification is substrate-intrinsic.
- **τ(A) vs τ(sign dA/dt).** Explicitly separate instantaneous-amplitude dependence (symmetric, does not rectify) from sign-of-rate dependence (memory, rectifies). Conflating them manufactures a false A.
- **H-conservation gate.** Net rectification that doesn't conserve H=T+V over the cycle is an artifact, not a finding (Checkpoint 6).
- **Right regime (§2.6).** Run in the **near-yield BULK** band. Do NOT run in the linear or transverse/shear regime — those are achromatic (frequency-independent), hence rate-asymmetry-free by construction; a B there is vacuous. Apply the explicit phase-state (Linear → Nonlinear/near-yield → Ruptured/plasma).
- **Reversible vs dissipative (the A/B discriminator).** Self-steepening is a *reversible* (conservative) nonlinearity and can give ∮=0 even while looking asymmetric. Only an *irreversible/dissipative* τ-asymmetry (the #59:77 amplitude-dependent τ lagging differently up vs down) yields ∮≠0. The derivation MUST separate these — a front-shape asymmetry is not a rectifier unless it survives a closed symmetric cycle with net ∮≠0.
- **Limits from canon, not tuned** — τ_relax = ℓ_node/c, L_eff(A) near-saturation form from `#59` / Op14 canon, the ρ̄ relation from `04_superluminal_transit.tex:86`, not fitted.

## 8. Skills + deliverables

- **Skills:** substrate-native-check (FIRST) · ave-canonical-leaf-pull (Time-domain / Saturation classes — τ_relax, memristive ODE, Op14 L_eff) · ave-canonical-source (τ_relax, ℓ_node, c from constants.py) · ave-driver-script-honesty (∮ + H-conservation reported every run) · consistency-vs-emergence + ave-discrimination-check (is intrinsic rectification AVE-distinct, or does it reduce to ordinary anelastic/standard-rheology hysteresis?).
- **Deliverables:** `2026-06-09_thixotropy-amplitude-dependent-tau_result.md` (A/B/C + ∮ + H-trace + DERIVED/VERIFIED/BLOCKED); analytic derivation of τ_relax(A) near saturation from `#59`/Op14 canon, then (if Outcome C) a coupled-engine driver. Commit on this branch; do NOT push/merge — orchestration handles the PR.

---

## PROTOCOL-COMPLETION AMENDMENT — 2026-07-19 (Leg A of the yield-fork discriminator lane)

**Status:** FROZEN amendment, bottom-appended. Pushed **before** any driver code (RAILS: freeze-then-run). This section enumerates every choice the frozen §1–§8 above left to the implementer, so the driver has zero post-hoc degrees of freedom. It changes **no** §1–§8 commitment; it only *completes* them. Authored in the implementer lane per the yield-fork discriminator dispatch (Grant 2026-07-19); the fork ruling (`research/2026-07-17_regime-iv-dissipation-audit.md` §5) stays Grant's — this leg RUNS the test, it does not close the fork.

### A.0 What §4/§6 already resolved (and what this leg therefore is)

The prereg's own §6 falsifier is the operative A/B criterion: **A ⇔ a symmetric-drive cycle encloses non-zero NET area *with H conserved*; B ⇔ the asymmetry integrates to zero OR the enclosed area is dissipative (loss, not H-conserving reactance).** The §7 guard "Reversible vs dissipative" and the §5-A caveat ("the pump/momentum ledger must still close … NOT smuggled drive-asymmetry") make explicit that a *dissipative* loop (∮≠0 but H not conserved) is **loss, not rectification** → B. So Leg A is a **sign(dr/dt)-memory + H-conservation** test, not a bare loop-area test (that bare loop-area is Leg B).

### A.1 Substrate / sector / regime declaration

- **SECTOR:** longitudinal-A1 bulk (volumetric) saturation state `S(t)`. NOT transverse/shear (§2.6: achromatic → rate-asymmetry-free by construction → a null there is vacuous; banned).
- **MODE / PHASE-STATE:** driven, time-domain, **near-yield crossing = Regime II→III** in the engine's V_SNAP-referenced three-regime convention (`k4_tlm.py:308–311`: Regime I `A<√(2α)≈0.121`, Regime II `0.121<A<√3/2≈0.866`, Regime III `A>0.866→A=1` rupture). The registered operating point (A.3) drives `A∈[0.4,1.0]`, spanning II into III/rupture — the band §2.6/§40 mandates.
- **REGIME VALIDITY GATE (fail-closed, checked FIRST each run):** if the drive never enters Regime III (max strain `<√3/2`) the run is **VACUOUS-REGIME → excluded** (a B there says nothing, per §2.6). If any state is non-finite the run is **BLOWN-UP → INSTRUMENT flag** (blow-up = instrument, not physics). Only runs that (i) reach Regime III and (ii) stay finite are adjudicated.

### A.2 Canonical kernel + integrator (byte-locked to the engine; engine itself byte-UNTOUCHED)

- Equilibrium kernel: `S_eq(r) = √(max(0, 1 − min(r,1)²))` — verbatim `k4_tlm.py:283`.
- Level-2 ODE (Eq 2.1 / `tau-relax-derivation.md:78`): `dS/dt = (S_eq(r(t)) − S)/τ_relax`.
- Integrator: **backward Euler**, `S_{n+1} = (S_n·τ + dt·S_eq)/(τ + dt)` — verbatim `k4_tlm.py:291` (unconditionally stable). The driver reproduces this formula and a pinned test asserts it is **bit-identical** to a live `K4Lattice3D(use_memristive_saturation=True)` driven at one site (validates the driver IS the engine kernel; `test_memristive_op14.py:150` pattern). **No engine byte is edited.**
- **Units:** engine-native (`c=1`, `ℓ_node=1`, `V_SNAP=1`, `m_e c²=1`), so `r ≡ V/V_SNAP`, `τ_relax = TAU_RELAX_NATIVE = 1.0` (constants.py:453, asserted in-driver), and `ω·τ_relax = ω`.

### A.3 Drive (symmetric-only, per §7) and operating point

- Waveform: `r(t) = r_0 + Δr·sin(ω t)` — a **pure symmetric** oscillation (§7: any fast-up/slow-down or flyback asymmetry is the *refuted* route and is BANNED; the driver asserts the waveform's first-half and second-half are time-mirror-symmetric before adjudicating).
- Registered operating point (from `#59` §6.4/§11, the same point that fixes the 0.9 peak): **`r_0 = 0.7`, `Δr = 0.3`** (native V_SNAP units) → `r∈[0.4,1.0]`, top-of-stroke grazes `r=1` (near-yield crossing).
- Primary drive rate: **`ω·τ_relax = 0.9`** (the predicted peak-lag regime where any sign-memory asymmetry is largest). Secondary robustness rates (reported, not adjudicated): `ω·τ ∈ {0.3, 1.8}`.
- Timing: `dt = min(2π/ω / N_ppp, τ/50)` with `N_ppp = 512` points-per-period; settle for `max(8 periods, 20 τ)` before the measured window; measure over the **last full period** at steady state.

### A.4 The three registered observables (all on the SAME symmetric steady-state cycle)

1. **Sign-memory probe `Δτ_rel` (the §7 core discriminator).** Effective relaxation time fitted separately on the up-stroke (`dr/dt>0`) and down-stroke (`dr/dt<0`) from the local lag `S−S_eq`. `Δτ_rel ≡ |τ_up − τ_down| / τ_relax`. Single-τ canon ⇒ `Δτ_rel → 0` (no memory); an explicit two-τ ⇒ `Δτ_rel > 0`.
2. **Directional rectification asymmetry `R`.** With `D_up = ∫_{dr/dt>0}(S−S_eq)dr`, `D_down = ∫_{dr/dt<0}(S−S_eq)dr` (both ≥0; their sum is the Leg-B loop area), `R ≡ (D_up − D_down)/(D_up + D_down)`. `R≈0` ⇒ up/down dissipate equally ⇒ no directional preference.
3. **H-conservation / net-work gate `W_cycle`.** `W_cycle ≡ ∮ S dr` over the closed cycle (canon: `tau-relax-derivation.md:24,:89` = dissipated energy per cycle). `W_cycle > tol` ⇒ **dissipative** (H not conserved, drive pumps net energy per cycle); `W_cycle ≤ tol` ⇒ **reactive/lossless** (H conserved). `tol` is the Leg-B integrator floor (imported from the Leg-B amendment A.6; identical numerics).

### A.5 Frozen classifier tree + precedence (evaluated top-down; first match wins)

0. **GATE (A.1):** not-Regime-III → VACUOUS-REGIME (excluded); non-finite → INSTRUMENT (excluded). Else continue.
1. `Δτ_rel ≤ tol_mem` **AND** `|R| ≤ tol_R` → **B (DEAD-BY-PROOF):** no sign-of-rate memory, no directional asymmetry → symmetric single-τ → a symmetric drive does **not** rectify. (Expected for the canonical kernel and for any *even* `τ(A)` amplitude-dependence.)
2. `Δτ_rel > tol_mem` (sign-memory present) **AND** `W_cycle ≤ tol` (H conserved) **AND** `|R| > tol_R` → **A (REAL):** a genuine *reactive* rectifier — the last door opens (route carefully; the momentum/pump ledger must still be shown closed and not a smuggled drive-asymmetry).
3. `Δτ_rel > tol_mem` **AND** `W_cycle > tol` (dissipative) → **B-anelastic:** the "rectification" is ordinary anelastic/rheological loss, **not** AVE-distinct reactive thrust (§8 ave-discrimination-check) → the door stays closed; flagged as the anelastic sub-case, not A.
4. analytic branch intractable / non-finite mid-cycle → **C (NEEDS-ENGINE):** report, do not fake an analytic A.

- `tol_mem = 1e-3`, `tol_R = 1e-3` (relative; both well above the backward-Euler round-off floor demonstrated by the A.7 positive control's null-arm, below the two-τ control's live signal). `tol` per A.6.

### A.6 Positive control (instrument-liveness; mandatory per "a null where the effect can't exist = ARTIFACT")

Alongside the canonical single-τ run, the driver runs an **explicit two-τ model** `τ(sign dr/dt) = τ_up on dr/dt>0, τ_down on dr/dt<0` with `τ_down = 3·τ_up` (a hand-built fast-liquefy/slow-refreeze memory) on the *identical* symmetric drive. Required outcome: `Δτ_rel ≈ 2` and `|R| ≫ tol_R` — proving the instrument **detects** sign-memory when present. A canonical-model B is only banked if the two-τ control fires (else the null is a dead-instrument artifact and the leg banks **INSTRUMENT-DEAD**, not B).

### A.7 The `τ(A)` amplitude-dependence arm (directly answers §1's load-bearing distinction)

To separate §7's "τ(A) [even, symmetric, does not rectify]" from "τ(sign dr/dt) [memory, rectifies]", a third arm drives the **amplitude-dependent** `τ(A) = τ_relax·(1 + κ·A²)` (the `#59` Flag-A near-saturation `L_eff(A)` stiffening cast as an *even* function of A, `κ = 1` as a representative non-zero coefficient — an engineering probe value, **tagged as such**, not a canonical magnitude). Required outcome: `Δτ_rel ≈ 0`, `|R| ≤ tol_R` → **even τ(A) alone does NOT rectify**, confirming amplitude-dependence is not sign-memory. This is the arm that upgrades §2's "dead-by-default" toward "dead-by-proof."

### A.8 Scope disclosure (0D kernel; self-steepening out-of-scope BY the prereg's own guard)

The driver is **0D** (single-cell temporal kernel) — it captures the *temporal* τ-dynamics, which §4/§7 identify as the **only** rectifier candidate. The *spatial* self-steepening (compression-front-sharpen / rarefaction-spread) is, per §4 and the §7 "Reversible vs dissipative" guard, a **reversible** (conservative) effect that integrates to `∮=0` and is explicitly **not** the rectifier; a 1D spatial front would test that reversible effect, which cannot flip the A/B verdict (which hinges on τ sign-memory). Excluding it is faithful, not a gap; disclosed here.
