# Motion-stability BEMF probe — does a moving self-trap's back-EMF stabilize it? — PREREG + RESULT

**Date**: 2026-06-04
**Branch**: `analysis/motion-stability-bemf` (off main `adb26859`)
**Brief / prereg**: [`_orchestration/motion-stability-bemf.md`](../_orchestration/motion-stability-bemf.md) (frozen)
**Driver**: [`src/scripts/vol_1_foundations/motion_stability_bemf_probe.py`](../src/scripts/vol_1_foundations/motion_stability_bemf_probe.py)
**Results JSON**: [`src/scripts/vol_1_foundations/motion_stability_bemf_probe_results.json`](../src/scripts/vol_1_foundations/motion_stability_bemf_probe_results.json)
**Engine**: [`src/ave/core/fdtd_3d.py`](../src/ave/core/fdtd_3d.py) (full-vector Maxwell, nonlinear ε(E)/μ(H) per Axiom 4, CPML)
**Base self-trap (validated)**: [`r10_fdtd3d_transverse_photon_selftrap.py`](../src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap.py) — retention 0.580 vs 0.389 matched baseline ([`2026-06-04_full-electron-transverse-selftrap-result.md`](2026-06-04_full-electron-transverse-selftrap-result.md))

**Status**: COMPLETE. Awaiting auditor pass before merge.

---

## §0 HEADLINE (the deliverable)

**The hypothesis (Grant 2026-06-04, GREEN-FIELD — corpus default CONTRADICTS it):** topological stability FROM motion. A static self-trap decays; a *moving* one is held together by its own back-reaction — the dark wake `τ_zx` (the mutual-inductance / back-EMF the moving trap drags behind it). Differential prediction: **retention(v) − retention(0) > 0, monotonic in v, stability-gain tracks `τ_zx`.**

**VERDICT: NULL → leaning CONTRADICTS. The hypothesis is NOT supported.**

In one line: on the continuum Maxwell engine, **a moving self-trap is NOT stabilized by its back-EMF.** The co-moving retention *does* rise with v — but a sub-saturation **LINEAR control rises just as much (more) at the same v**, so the rise is **generic transport, not the bemf** (the AVE-distinct discriminator FAILS). Worse for the hypothesis: the trap's **saturation depth DECREASES with v** (peak_A_max 0.93→0.60 — the *static* v=0 trap saturates deepest), the r10-comparable peak-field retention is essentially flat, and the measured **`τ_zx` ANTI-correlates with the "gain" (corr = −0.81)**. Every trap-integrity metric favors the **static** trap — i.e. the canonical static-saturation-knot default ([`resonant-lc-solitons.md:23,27`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md)), not Grant's cross.

This is a clean structural finding (a null/contradicts is informative for a CP8 emergence test, prereg §5): **the "dark wake = momentum trail" corpus framing does NOT extend to "dark wake = stabilizer" on this engine.** The forward-predicted sign was locked before the run (Grant=POSITIVE-tracking-`τ_zx`; canonical=FLAT/NEGATIVE); the data lands on canonical.

---

## §1 LOAD-BEARING METHOD FINDING — the PML-advection confound (surfaced + fixed mid-run)

**This is the one plumber-physical issue that materially shaped the result; it is reported, not buried (flag-don't-fix).**

The hypothesis requires comparing retention at v=0 vs v>0. But a *moving* trap **drifts toward the +x PML and is absorbed there**, which would crush retention(v) purely from box geometry — a false NEGATIVE mimicking the canonical default. This was flagged a-priori (prereg §1d) and then **empirically bit the first run**:

- **First run (static window, lock at step 80):** measured retention ≈ 0.13 and **NEGATIVE v (−0.24c)**. Tracing the dynamics showed why: the boosted trap forms + peaks at ~step 20, translates +x reaching the PML edge (cell ~42) by ~step 63, gets **absorbed** (interior energy collapses 1.5e6 → 2.2e5 over steps 80→100), and the energy-centroid **snaps back** to the low-amplitude stationary residue near the seed center — read out as "negative v" + "13% retention." Both were PML artifacts, not physics.

- **Fix (co-moving early window):** lock the core at `T_LOCK=18` (post-formation, peak_A near its max), and measure retention in a **co-moving box** (half-width 8 cells) tracking the centroid over `[18, 54]` — a window that ends **before** the fastest arm's core reaches the PML. A `window_pml_clean` gate verifies this per arm. After the fix, **v is POSITIVE and monotonic (0.047 → 0.472 → 0.709 c)** and the SELF-TRAP/LINEAR arms are PML-clean (`pml_contact_step = None`).

**Base-fidelity cross-validation (the fix did not break the self-trap):** at v=0 the SELF-TRAP `peakE_retention` = **0.576**, matching the validated r10 C-EMERGE `peak_E_retention` = **0.580** to within 0.7%, and `peak_A_max` = 0.93 (deep saturation, well past the Op14 bar √(2α)=0.121). The boosted seed at δ=0 reproduces the validated self-trap.

**`τ_zx` (back-EMF) observable on fdtd_3d.py.** `DarkWakeObserver` lives on `VacuumEngine3D` (K4-TLM+Cosserat). Its canonical formula `τ_zx ∝ Z_local·∂_x[|V|²/V_SNAP²]` ([DarkWakeObserver docstring](../src/ave/topological/vacuum_engine.py)) ports to the E/H sector via the FDTD bridge `dV²/dz ≈ ℓ_node²∇|E|²` ([`2026-05-31_FT-darkwake-crossscale_result.md:117`](2026-05-31_FT-darkwake-crossscale_result.md)): on the Yee engine `τ_zx = Z_0·S(A)·∂_x[A²]`, the longitudinal energy-gradient back-reaction (the engine's own ponderomotive x-component, re-scaled). **Honesty caveat:** this is the **E/H projection** of the canonical Cosserat-side τ_zx — the longitudinal-shear back-EMF as it appears in the Maxwell sector. The full Cosserat shear tensor needs `VacuumEngine3D` (auditor queue item 1).

---

## §2 THE TEST AS RUN (CP8 emergence test — v-sweep × 3 arms)

**Velocity boost (substrate-native-check CP8 — momentum operator on the GENERATIVE PRECURSOR, not a planted end-state):** the validated self-trap = two counter-prop focused CP transverse pulses with zero net momentum. Boost by breaking the amplitude symmetry — pulse A (+x) × (1+δ), pulse B (−x) × (1−δ) — then **renormalize to FIXED peak |E|** so the v-sweep varies ONLY momentum, NOT saturation depth (raw (1±δ) bias would raise peak_A → confound "motion stabilizes" with "more saturation stabilizes," and breach the A>1 rupture at δ=0.55). Verified: seed peak_A = 0.687 held constant across δ; net x-momentum proxy monotonic in δ; v MEASURED via centroid drift (NOT tuned to a target — `ave-driver-script-honesty`).

| Arm | role | amplitude | what it tests |
|---|---|---|---|
| **SELF-TRAP(v)** | hypothesis | deep-sat 0.7·V_SNAP/dx (peak_A→0.93) | the boosted validated self-trap |
| **LINEAR(v)** | AVE-distinct discriminator (SM-counterfactual) | sub-sat 0.05·V_SNAP/dx (peak_A→0.07) | a pulse with NO self-trap — disperses regardless of v → retention should NOT rise *because of saturation* |
| **BASELINE(v)** | matched-saturation-depth control | peak-matched phase-scramble of the self-trap | coherence destroyed at matched saturation depth (avoids the (ii) global-norm A=1-clamp confound) |

δ ∈ {0, 0.30, 0.55} → v ∈ {0.047, 0.472, 0.709} c (measured). A-trajectory (peak_A every probe step) instrumented THROUGHOUT (ii-audit lesson 1).

---

## §3 RESULT — the numbers

### §3.1 Retention(v), 3 arms (co-moving box energy, PML-clean window)

| v/c (measured) | **SELF-TRAP** | **LINEAR** | **BASELINE** | LINEAR − SELF-TRAP |
|---|---|---|---|---|
| 0.047 | 0.478 | 0.507 | 0.398 | **+0.029** |
| 0.472 | 0.695 | 0.739 | 0.411 | **+0.044** |
| 0.709 | 0.865 | 0.906 | 0.433 | **+0.041** |
| **slope vs v** | **+0.576** | **+0.596** | (≈flat) | — |

**The discriminator decides it.** SELF-TRAP retention rises with v — but **LINEAR rises as much (slope +0.596 ≥ +0.576) and retains MORE at every v.** A sub-saturation pulse, with no self-trap and no engaged saturation kernel, shows the *same* retention(v) rise. So the rise is **generic transport** — a faster-moving packet disperses less out of a fixed-duration co-moving window — **NOT the self-trap's back-EMF.** (`ave-discrimination-check`: velocity transports in linear engines too; it is not AVE-distinct. The claim was stability-gain, and the gain is not self-trap-specific.) `discriminator_clean = False`.

### §3.2 Trap integrity vs v — the static trap saturates DEEPEST (against the hypothesis)

| v/c | peak_A_max | peak_A_min | stayed_saturated (A>√2α throughout) | peakE_retention (r10-comparable) |
|---|---|---|---|---|
| 0.047 | **0.932** | 0.268 | True | 0.576 |
| 0.472 | 0.723 | 0.271 | True | 0.626 |
| 0.709 | 0.601 | 0.282 | True | 0.639 |

- **The self-trap STAYS saturated while moving** (peak_A_min ≈ 0.27 > the 0.121 Op14 bar at every v) — so this is a genuine *moving saturated trap*, not a desaturated one (the ii-audit failure mode is avoided; the A-instrument confirms it). **But** `peak_A_max` **DECREASES monotonically with v** (0.93 → 0.60): the **static (v=0) trap reaches the deepest saturation (closest to Γ→−1).** Motion does not deepen the trap's confinement — it shallows it.
- The r10-comparable `peakE_retention` (peak-field-amplitude retention — the trap-integrity metric, not the co-moving-window metric) is **nearly flat** (0.576 → 0.639); the small rise is the same transport effect §3.1 isolates as non-specific.

### §3.3 `τ_zx` (back-EMF) vs stability-gain — ANTI-correlated

| v/c | max\|τ_zx\| (at core) | backward-wake peak | retention gain vs v=0 |
|---|---|---|---|
| 0.047 | **580.1** | 92624 | 0.000 |
| 0.472 | 380.0 | 87569 | +0.218 |
| 0.709 | 416.9 | 100941 | +0.387 |

- **corr(max\|τ_zx\|, gain) = −0.81** — the back-EMF at the core **FALLS** as the comoving "gain" rises. The hypothesis predicted POSITIVE tracking; the data shows the **opposite sign**. (max|τ_zx| is largest at v=0, where the saturation is deepest — consistent with τ_zx ∝ S(A)·∂_x|E|² being driven by the static trap's steep saturated core, not by motion.)
- corr(backward-wake, gain) = +0.56 — weak, and not a clean tracker (the backward-wake amplitude is dominated by the seed's residual structure, barely moving across the sweep). Neither τ_zx channel tracks the stability-gain as predicted.

---

## §4 VERDICT, framed exactly as strong as the data (`ave-evidence-framing-discipline`)

**NULL on the comoving-transport metric; CONTRADICTS on every trap-integrity metric. The motion-stabilizes-via-bemf hypothesis is NOT supported on `fdtd_3d.py`.**

Three independent reads, all pointing the same way:
1. **Discriminator (load-bearing):** the retention(v) rise is reproduced by a sub-saturation LINEAR pulse → **generic transport, not the bemf.** This alone defeats the AVE-distinct claim.
2. **Trap integrity:** saturation depth (peak_A_max) and peak-field retention favor the **static** trap. Motion shallows the saturation.
3. **Back-EMF tracking:** `τ_zx` **anti-correlates** (−0.81) with the gain. The predicted positive tracking is absent (wrong sign).

**This lands on the canonical default**, which the hypothesis set out to overturn:
- Confinement is the **static** saturation knot: *"the localized wave-packet does not instantly disperse … geometric stability is mathematically guaranteed by the extreme flux crowding at the particle's boundary … perfect macroscopic impedance mismatch"* — driven by the **static topological twist** ([`resonant-lc-solitons.md:23,27`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md)). Motion is not part of the confinement story.
- A moving (2,3) "requires **SUSTAINED EXTERNAL DRIVE**" ([`axiom_derivation_status.md:178`](_archive/L5/axiom_derivation_status.md)) — i.e. motion is a *cost* to be paid for, not a free stabilizer. Consistent with peak_A_max FALLING with v (the moving trap is harder to hold, not easier).

**What the dark-wake canon DOES say (and what we did NOT overturn):** the dark wake `τ_zx` is real and present (max|τ_zx| ≈ 580 at the saturated core) and it IS the Newton-3rd-law momentum-trail / back-reaction ([`2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md:114-116`](2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md) §6, Lenz `V_BEMF = −L_eff dI/dt`). The corpus framing "momentum trail" survives. **Grant's CROSS — "momentum trail ⇒ stabilizer" — does not.** The wake carries reaction momentum *away*; it does not feed cohesion *back* into the core (on this engine, in this regime).

### Honest scope / what could move the verdict
- **Engine:** `fdtd_3d.py` is the continuum-Maxwell projection (E/H only). The canonical `τ_zx` is a **Cosserat** longitudinal-shear quantity; this engine carries only its E/H projection. A genuine bemf-stabilization mechanism that lives in the Cosserat sector (the SU(2) fibre / ω field) would be **invisible here** — exactly the structural-capability gap that put the (2,3) poloidal-"3" out of reach in the r10 study. So this is a CONTRADICTS **on the continuum engine**, not a framework-wide refutation. The discriminating follow-up is the same one r10 named: re-run on `VacuumEngine3D` (K4-TLM + Cosserat + native `DarkWakeObserver`), where the full τ_zx and any Cosserat-sector back-reaction are present. (auditor queue 1)
- **Regime:** v ≲ 0.71c, deep-saturation seed, short PML-clean window (36 steps). A bemf-cohesion effect that only switches on at relativistic v, or over many oscillation periods, is outside this window. But the *prediction was monotonic-from-v=0*, and the v=0→0.71 trend is the wrong sign for trap integrity — so the simplest reading is no effect (transport-only), not "effect hidden above 0.71c."
- **Co-moving-window transport floor:** the +0.58 comoving slope is a real artifact of the metric (a moving packet disperses less out of a fixed-step tracking box). It is shared by LINEAR, which is why the LINEAR control is load-bearing. The peakE_retention metric (which does NOT have this floor) is flat — corroborating "no real stability gain."

---

## §5 FORWARD-PREDICTED SIGN vs OBSERVED (driver-honesty)

| | Forward-predicted (locked pre-run) | Observed |
|---|---|---|
| **Grant (hypothesis)** | retention(v) slope **> 0, monotonic, tracking τ_zx** | comoving slope +0.58 (but **transport, not bemf**); peak-field flat; saturation depth FALLS; τ_zx **anti**-tracks (−0.81) |
| **Canonical default** | slope **≤ 0** / motion irrelevant-to-destabilizing; static trap holds | **borne out**: static trap saturates deepest, peak-field retention flat, τ_zx largest at v=0 |

Observed lands on **canonical default**. v was NOT tuned to a target (measured centroid drift; monotonic in the boost δ). No fit; every reported number is computed from the run (`verify_constants()` passes; no print-vs-compute mismatch).

---

## §6 AUDITOR QUEUE

- [ ] **τ_zx projection fidelity (the decisive follow-up):** re-run on `VacuumEngine3D` (K4-TLM + Cosserat + native `DarkWakeObserver`). The canonical τ_zx is a Cosserat longitudinal-shear quantity; `fdtd_3d.py` carries only its E/H projection. A bemf-stabilization that lives in the Cosserat sector would be invisible here — so this CONTRADICTS is engine-scoped, not framework-wide. This is the same structural-capability gap r10 named (Mode II: discrete K4 + Cosserat load-bearing).
- [ ] **Co-moving-window transport floor:** confirm the +0.58 comoving slope is a metric artifact (shared by LINEAR) and that the flat `peakE_retention` is the trap-integrity-faithful read. Consider a third metric (e.g. fixed-lab-frame energy in a box centered on the *final* core position) as a tie-breaker.
- [ ] **BASELINE momentum:** the phase-scramble killed net momentum (v ≈ 0 for BASELINE; `pml_contact_step` = 0/51, not PML-clean) — so BASELINE is only a matched-saturation-depth control at v≈0, NOT a moving control. The LINEAR arm is the load-bearing moving discriminator. Is a momentum-preserving scrambled control needed, or does LINEAR suffice? (LINEAR is the cleaner discriminator anyway — it isolates saturation-vs-no-saturation at matched v.)
- [ ] **Window sensitivity:** verify the verdict is robust to T_LOCK / T_END / COMOVE_HALF (the window was calibrated to the δ=0.55 PML-transit; a shorter window or larger box should not flip the LINEAR≈SELF-TRAP discriminator).
- [ ] **Verdict strength:** is "NULL leaning CONTRADICTS, engine-scoped" the right strength, or does the −0.81 τ_zx anti-correlation + the falling saturation depth justify a cleaner CONTRADICTS (on this engine)?

---

## §7 GREEN-FIELD STATUS + CANON CITED (for the record)

**Green-field / prove-or-disprove:** the hypothesis is a NOVEL cross the corpus default CONTRADICTS (prereg §0). Classified as an EMERGENCE test (`consistency-vs-emergence`), not a consistency check. A null/contradicts is a clean structural finding (CP8).

**Canon cited:**
- Static-saturation-knot confinement default (CONTRADICTED-by-hypothesis, SUPPORTED-by-data): [`resonant-lc-solitons.md:23,27`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md).
- Moving-(2,3)-requires-sustained-drive default: [`axiom_derivation_status.md:178`](_archive/L5/axiom_derivation_status.md).
- Dark-wake / bemf canon (the structural seed Grant crossed from — "momentum trail," which SURVIVES; "stabilizer," which does NOT): [`2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md:114-116`](2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md) §6; [DarkWakeObserver](../src/ave/topological/vacuum_engine.py) (τ_zx ∝ Z_local·∂_x|V|²); FDTD bridge [`2026-05-31_FT-darkwake-crossscale_result.md:117`](2026-05-31_FT-darkwake-crossscale_result.md).
- Validated base self-trap: [`2026-06-04_full-electron-transverse-selftrap-result.md`](2026-06-04_full-electron-transverse-selftrap-result.md) (retention 0.580; peak_A_max 0.179 cross-validated).

**Discipline applied:** substrate-native-check CP8, consistency-vs-emergence (EMERGENCE), ave-discrimination-check (LINEAR = SM-counterfactual, the decider), ave-canonical-source (`verify_constants`), ave-driver-script-honesty (forward-predicted sign; no fit; measured v), ave-evidence-framing-discipline (NULL/CONTRADICTS framed exactly as strong as the data; engine-scoped), pre-test-physics-check (PML-advection confound surfaced + fixed). Pure-AVE-corpus.
