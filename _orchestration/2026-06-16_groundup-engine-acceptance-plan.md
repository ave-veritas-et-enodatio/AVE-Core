# Ground-Up Substrate Engine — Acceptance-Test-Driven Build (orchestration plan)

**2026-06-16 · orchestration · DRAFT (persist → `_orchestration/` on branch + PR when Bash returns)**
**Supersedes for execution:** the LOOP-GAP harness pivot (2026-06-12) and the genesis-on-K4 arc. Those are not deleted — they are the *negative results* this plan is built on.

---

## §0 — Why ground-up, now (the diagnosis)

The engine map (`engine-capability-map.md`) is the verdict on the old approach: a **complete electron needs 7 DOF**, **no engine carries more than 1–2**, three of the splits are **canon-forced incompatibilities**, the **unified engine is a design proposal that does not exist**, and even the **binding wall (Γ=−1) is not demonstrated**. On top of that, the 2026-06-16 genesis arc (keystone / freeze-g / handedness / winding-emergence) ran on `a1_cosserat_convergence_engine` — the **K4-diamond grid with chirality parked (`:334` "achiral-OK")** — which by incompatibility #2 **structurally cannot carry the (2,q) winding's handedness = the charge**. We were testing the hardest object (electron charge-genesis) on the one grid that provably can't host charge.

So we stop patching incompatible engines and **build one engine from the medium up, one excitation-layer at a time, each gated by a falsifiable acceptance test** — TDD for the physics engine. Build order is the engine map's own §5 DAG, started honestly from L0.

## §1 — The principle (acceptance-test-driven, consistency-vs-chord labeled)

Every layer ships with **unit tests that are physics claims** (pass/fail). Two labels, machine-tracked:

- **CONSISTENCY tests** — reproduce *known* physics (lossless propagation, dispersion, achromatic deflection). The engine MUST pass these to be a valid medium. They are not chords; failing one means the engine is wrong.
- **CHORD tests** — force a *dimensionless number we did not input* (the charge integer, a mass ratio). These are where chord-vs-echo is decided (per the deepest-question logic: dimensionful = calibration, forms = true-by-construction, only forced dimensionless numbers can't be faked).

Low layers (L0–L2) are mostly CONSISTENCY — the foundation. The CHORDS live at L3–L5. A run that passes L0–L2 (valid medium) **and** forces a dimensionless number at L4/L5 is the real chord.

## §2 — The build ladder (each = a fundamental block + its acceptance tests)

### L0 — The medium (LC/TLM lattice)
Block: node + scatter/connect on the **chiral srs grid** (the map's step 1; chirality native from the start so L4/L5 are reachable).
- **T0.1** energy conservation: bare-lattice wave conserves energy (Γ²+T²=1 every scatter; total H flat over a long run). *[CONSISTENCY]*
- **T0.2** impedance: Z₀ = √(μ₀/ε₀) = 376.7 Ω uniform. *[CONSISTENCY]*
- **T0.3** isotropy: wave speed isotropic up to the characterized lattice-projection factor (√2 cardinal / √3 diagonal — already mapped; the diagonal=c claim is being corrected). *[CONSISTENCY]*
- **T0.4** chirality present: the srs grid carries optical activity (handedness is in the medium, not added later). *[CONSISTENCY → enables CHORD at L4]*

### L1 — The photon (2 transverse-shear DOF; the free propagating mode)
Block: a transverse wave packet.
- **T1.1 photon propagates losslessly** — N-cell travel, no amplitude decay, energy conserved, Γ=0 matched. *[CONSISTENCY — the foundational test]*
- **T1.2 different frequencies supported** — sweep ω; ω=ck across a band; characterize zone-edge dispersion onset (the continuum photon sampled by the lattice). *[CONSISTENCY]*
- **T1.3** transversality — E⊥B⊥k; exactly 2 polarizations; no spurious longitudinal leak in the free photon. *[CONSISTENCY]*
- **T1.4** speed + causality — info front at c₀; no superluminal signal (the photon-c result, already banked, folds in here). *[CONSISTENCY]*
- **T1.5** optical activity — polarization rotates by the predicted ±angle/cell on the chiral grid. *[borderline CHORD — a forced rotation-per-cell is dimensionless]*

### L2 — EM in a biased medium (operating-point / varactor modulation)
Block: a region at saturation operating-point A₀ modulating ε_eff, μ_eff.
- **T2.1** refractive index — biased region gives n(A₀)=1/S(A₀); packet slows/bends correctly (Op14). *[CONSISTENCY]*
- **T2.2 achromatic lensing** — a SYM gradient (ε·μ co-scale → Z=Z₀, Γ=0) bends light with **frequency-INDEPENDENT** deflection (gravity-as-achromatic-lens). Acceptance: deflection angle equal across the band. *[CHORD — AVE-distinct vs chromatic media]*
- **T2.3** asymmetric mirror — static-E-only bias loads ε only → Z changes → Γ≠0 reflection (Op14 Meissner / vacuum-impedance-mirror), distinct from T2.2. *[CHORD]*
- **T2.4** α-invariance under SYM — α stays invariant under SYM scaling (the c_EM/c_shear asymmetry). *[CONSISTENCY of the canonical claim]*

### L3 — The longitudinal-bulk mode (the A1 scalar; the mass precursor)
Block: the longitudinal compression mode (the QED-deleted scalar) + the c_eff(V) stiffening kernel.
- **T3.1** longitudinal mode is real — a propagating longitudinal compression exists (not Gauss-deleted). *[CHORD — AVE-distinct vs QED]*
- **T3.2** c_eff(V) stiffening — c_eff→∞ as A→A_yield (the cage forms), driven by S(A). *[Axiom-4 manifestation]*
- **T3.3 binding wall reaches Γ=−1** — the saturated core self-creates a Γ=−1 short (the TIR cage). **The map says −1 is NOT demonstrated** — this is the make-or-break "does mass exist" test. *[CHORD/make-or-break]*
- **T3.4** mass = cutoff frequency — the trapped longitudinal resonance has ω₀ = the mass gap. *[the mass identity]*

### L4 — The micro-rotation / winding (charge; needs the chiral grid)
Block: the Cosserat micro-rotation field on the chiral srs grid.
- **T4.1** winding forms/persists — a (2,q) winding is stable on the chiral grid. *[CONSISTENCY-of-existence]*
- **T4.2 charge = integer winding** — charge is the topological winding NUMBER (±1), forced by topology. **The unfakeable integer.** *[CHORD — the cleanest decider]*
- **T4.3 handedness matters** — e⁻ vs e⁺ = helicity sign; the chiral grid distinguishes them (candidate-(c) re-test, ON the chiral grid — the achiral version was confounded). *[CHORD]*

### L5 — Binding / the electron (mode conversion + trap; genesis done right)
Block: the energize-LOCK / mode-conversion coupling (transverse photon → longitudinal bulk + winding), on the UNIFIED chiral+cage engine.
- **T5.1** coupling conserves energy — the keystone, re-run on the *unified* engine (the K4 result was scoped to the wrong grid). *[CONSISTENCY/Axiom-3]*
- **T5.2** electron self-assembles — generic seed → trapped longitudinal bulk (mass) + (2,q) winding (charge), no planting. *[CHORD — genesis]*
- **T5.3 forced mass ratio** — m_μ/m_e falls out of the (2,q) family, forced not fit. **THE chord-decider.** *[CHORD]*

## §3 — Key decisions for Grant (the orchestration choices)

- **D-A (grid):** build on the **chiral srs grid from L0** (chirality native), not K4-then-retrofit. The srs grid (v9) is "transverse-only / frozen" — so L0–L1 may run on it largely as-is; the build is *adding the longitudinal+cage (L3)* and the *winding dynamics (L4)* to it. RECOMMEND: yes, srs from L0.
- **D-B (harness):** stand up a **pytest-style acceptance suite** (`tests/engine_acceptance/`), one test per Ti.j, each labeled CONSISTENCY/CHORD, run as the engine's regression gate. RECOMMEND: yes — it's the spine of the whole approach.
- **D-C (reuse vs rebuild):** the existing engines have validated *pieces* (Master-Equation = the c_eff cage; srs v9 = the chiral grid; the harness = Cosserat/channels). **Consume the pieces that pass the acceptance tests; rebuild where they don't.** This is consolidation onto one grid, NOT a from-scratch rewrite. RECOMMEND: yes.
- **D-D (scope of "first"):** L0–L1 (photon, lossless propagation, frequencies) is the immediate target — your "photons first." L2 (achromatic lensing) is the first CHORD and the gravity bridge. STOP and report after L1 passes before committing to L3+.

## §4 — What this does to the open arcs (recording / walk-back)

- **Keystone energize-LOCK negative — KEEP, SCOPE.** Real for the energize-LOCK loop *on the K4 engine*; **not** the last word on genesis (wrong grid for charge). Re-runs as T5.1 on the unified srs engine.
- **Candidate-(c) handedness — RE-OPEN.** The "symmetric → reference-independent" refutation was confounded by the achiral grid. Re-tested as T4.3 on the chiral grid.
- **Genesis-arc (winding-emergence on K4) — SUPERSEDED.** Folded into L4/L5 on the right grid; do not run the queued K4 winding-emergence expecting a chord-decider.
- **Stranded retractions — MERGE.** `analysis/2026-06-16-stage16-rerun-amendments` (Stage-1.5 (b) retraction + (c) CONTESTED marker) must land on main (Grant approves; pre-merge audit first).
- **Photon-c (PR #275), keystone-freezeg branch — record then fold.** The photon-c result is L1.4; the keystone branch carries L5.1's K4-scoped negative.

## §5 — First concrete step (when Bash returns)

1. Persist this plan to `_orchestration/2026-06-16_groundup-engine-acceptance-plan.md` on a branch + PR; add a 2026-06-16 reconciliation section to `_orchestration/index.md`.
2. Scaffold `tests/engine_acceptance/` with T0.1–T1.4 as the first acceptance batch (CONSISTENCY), pointed at the srs-grid medium.
3. Run T1.1 ("does a photon propagate losslessly") as the first gate. Report pass/fail before building L2.

## §6 — The honest framing

L0–L2 are mostly "reproduce known physics" — not glamorous, but they are the proof the engine is a *valid medium* before we ask it for chords. The chords (forced dimensionless numbers) live at L3–L5: the binding wall (T3.3), the charge integer (T4.2), the mass ratio (T5.3). If the engine passes L0–L2 and forces even one of those, that is the chord the whole framework has been reaching for. If it passes L0–L2 and every L3–L5 number is imported or fit, that is the honest echo verdict — earned cleanly, on the right grid, for the first time.
