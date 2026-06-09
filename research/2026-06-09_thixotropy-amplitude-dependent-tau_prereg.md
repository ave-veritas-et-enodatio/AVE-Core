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

## 3. substrate-native-check (FIRST)

- **Sector / dynamics:** time-domain LC relaxation of the saturation state S(t) toward S_eq(A); first-order memristive ODE (`tau-relax-derivation.md:78`). NOT a minimization, NOT continuum-Helmholtz.
- **The load-bearing distinction:** τ(A) (instantaneous, single-valued function of current amplitude) vs τ(A, sign dA/dt) (a true memory/state variable). Only the latter rectifies. The canonical first-order ODE has the former; the question is whether near-saturation L_eff(A) dynamics *promote* it to the latter.
- **Coordinate system:** real-space strain amplitude A and its rate dA/dt; the rectification observable is the cycle integral ∮ over a symmetric drive period (real-space, time-domain — matches the corpus claim's coordinates).
- **Reactance pair / conservation:** any time-domain verdict must track the C-state/L-state reactance pair and H=T+V over the cycle (substrate-native-check Checkpoint 6) — a "rectified" net that violates H-conservation is a numerical artifact, not a finding.

## 4. Prediction (pre-committed)

I expect: τ_relax(A) **does** rise near saturation (L_eff grows as the kernel stiffens), so τ is amplitude-dependent. **But** I predict the leading correction makes τ a function of *instantaneous A only*, not of sign(dA/dt) — so under a symmetric drive the loading and unloading paths traverse the **same** τ(A) at each A, the loop closes symmetrically, and **∮ net-rectification = 0 → OUTCOME B**. Genuine rectification requires the near-saturation dynamics to introduce an intrinsic **sign-dependence** (fast onset / slow recovery — the STZ liquefy-fast/refreeze-slow picture made quantitative). The crack where A could happen: if saturation **onset** is abrupt (Γ→−1 rupture is fast) while **recovery** is gradual (re-freeze is diffusive), that IS a sign-dependence the first-order ODE doesn't capture.

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
- **Limits from canon, not tuned** — τ_relax = ℓ_node/c, L_eff(A) near-saturation form from `#59` / Op14 canon, not fitted.

## 8. Skills + deliverables

- **Skills:** substrate-native-check (FIRST) · ave-canonical-leaf-pull (Time-domain / Saturation classes — τ_relax, memristive ODE, Op14 L_eff) · ave-canonical-source (τ_relax, ℓ_node, c from constants.py) · ave-driver-script-honesty (∮ + H-conservation reported every run) · consistency-vs-emergence + ave-discrimination-check (is intrinsic rectification AVE-distinct, or does it reduce to ordinary anelastic/standard-rheology hysteresis?).
- **Deliverables:** `2026-06-09_thixotropy-amplitude-dependent-tau_result.md` (A/B/C + ∮ + H-trace + DERIVED/VERIFIED/BLOCKED); analytic derivation of τ_relax(A) near saturation from `#59`/Op14 canon, then (if Outcome C) a coupled-engine driver. Commit on this branch; do NOT push/merge — orchestration handles the PR.
