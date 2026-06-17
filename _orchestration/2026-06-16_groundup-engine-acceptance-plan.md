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

## §7 — Architecture corrections + chirality grounding (Grant 2026-06-16; investigation `w7etm1msb`)

**CORRECTION A — L0 is the AXIOM-COMPLIANCE suite (Grant).** L0 is not "T0.1–T0.4 (behaviour)"; it unit-tests all **four axioms** — the medium is valid iff it faithfully expresses each. This sharpens chord-vs-echo: **L0 = "are the axioms implemented?" (definitional/identity — axioms IN); L1+ = "does the axiom-compliant medium PRODUCE the physics?" (emergent — consistency + chord).** A forced dimensionless number at L1+ is a genuine chord precisely because L0 certified only the axioms went in.

L0 axiom-test groups:
- **Axiom 1 — Substrate Topology:** I4₁32 chiral K4/srs graph (connectivity + coordination), 6 DOF/node (3 translational + 3 micro-rotational), intrinsic LC (Z₀=√(μ₀/ε₀)), and **chirality EXPRESSED losslessly** (Correction B).
- **Axiom 2 — TKI:** [Q]≡[L] dimensional identity, ξ_topo=e/ℓ_node (canonical-constant check), dislocation-hosting capacity. *(Subtle at L0 — charge proper is L4-emergent; the L0 form is the dimensional identity + hosting.)*
- **Axiom 3 — Minimum Reflection:** lossless reactive cycling (unitary scatter, energy conserved) AND |Γ|² minimization (matched region → Γ→0).
- **Axiom 4 — Universal Saturation Kernel:** the constitutive law S(A)=√(1−(A/A_yield)²), C_eff=C₀/S, ε_eff=ε₀S, μ_eff=μ₀S (drive a node, verify the quarter-arc). L2 achromatic lensing then EMERGES from it.

**CORRECTION B — chirality is fundamental (Axiom 1), expressed in L0, not an L4 add-on (Grant).** The current build ran all photon tests κ=0 / `chiral_rotation=False` = geometrically-chiral but dynamically-achiral = not the AVE vacuum. The chirality channel must be lossless + ON at L0.

**Chirality leak verdict (investigation `w7etm1msb`):** the T1.5 ~92% energy bleed is a **2-line NumPy view-aliasing bug**, NOT physics, NOT a theory statement. `chiral_lattice_vector.py:43-46` rotates in-place on numpy VIEWS (the 2nd write reads the already-overwritten column → non-norm-preserving). **Fix = copy-first** (`v0=V_ref[...,0].copy()`); verified drift **0.92 → 1.6e-13** (lossless recovered), angle observable **unchanged** (so the P2/P3/P4 chirality verdicts stand). Contradicts Axiom 3 losslessness → the fix makes sim match theory. **Blast radius:** identical bug in 3 sisters (`chiral_lattice_vector_sat.py:89-91`, `chiral_lattice_v11.py:123-125`, `chiral_lattice_v13.py:138-140`). **Gate gap:** the P1 losslessness gate runs `chiral_rotation=False`, so it never hit the bug — **add an energy-conservation test WITH rotation ON** (Axiom-3 L0).

**Handedness = EMERGENT-from-the-lattice (answers the seed-vs-emergent question; a real chord on sign/null).** A linear (zero injected helicity, comp1_E=0) wave on srs gets its polarization rotated by the **lattice**: dθ/step = −0.0409 (srs-R) / +0.0409 (srs-L) / **exactly 0.0** (achiral diamond); rate = the lattice writhe. The substrate FORCES a signed, reflection-odd optical activity with an exact null on the achiral net — emergent (not seeded), **chord on sign/null** (magnitude is calibration). **Scope-limit:** this is optical-activity gyrotropy, NOT the localized charge e⁻/e⁺ sign — that still needs the BIN-G / CVR self-trap test. (K4 contrast: there helicity is *seeded* via `seed_cosserat_photon(helicity=±1)`.)

**Vocabulary locks before L4 (investigation LENS 3):** chirality (def-7c3f9e, ambiguous) / winding=the-3 (def-5d2b8a) / longitudinal (def-9a4f07) are locked + engine matches. **MISSING def-nodes:** optical-activity (= a GYRATOR / reciprocal-Faraday SO(2) polarization-plane rotation, EE-native; status SOLID-on-result #195 ±75.46°/unit), writhe (the reflection-odd geometric source pseudoscalar of the lattice circuits), helicity. **Live conflation:** the engine's bare token "rotation"/`rot_per_node` (optical-activity, a TRANSVERSE observable) shares the root word with the Cosserat **micro-rotation** (= the (2,3) winding = CHARGE) — declared ORTHOGONAL (A1⊥T2) but NOT def-fenced. **Fence before L4** (mint the def-nodes; Grant fork: rename the engine token off bare "rotation").

**Open forks → Grant:** (1) charge-SIGN — the rotation channel forces emergent optical activity (chord on sign/null) but cannot pin a localized charge's e⁻/e⁺ alone; is the BIN-G/CVR self-trap test the charge-sign discriminator before L4? (2) engine-token rename (`rot_per_node` → `optical_activity`/`gyro_rotation`) so grep never collides with the charge DOF.
