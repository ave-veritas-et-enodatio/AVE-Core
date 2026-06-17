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

## §1.5 — ID-scheme (locked default)

The KB metadata spine is the **single identification system** (INVARIANT-S11: extend, don't reinvent). The verified node-id regex (`tools/kb_index_lib.py:115`) admits exactly `clm | exp | sup | def | ilk`. For the acceptance suite:

- **Sims / acceptance-tests register as `sup-` nodes, NOT `exp-`.** Per **INVARIANT-S9** (`CLAUDE.md:182`): a simulation is NOT an experiment — it feeds a claim's *derivation* confidence (the min-branch), never its *experimental* solidity; `exp-` is reserved for a physical apparatus **we design, originate, and control**. A sim is categorically a `sup-` (INVARIANT-S10).
- **Figures carry NO spine id.** There is no `fig-` prefix in the regex, and S11 says don't spin one up for a non-knowledge entity. Figures are REFERENCED, not ID'd — each debug PNG is named by its **test-id stem** (that IS its identifier; it inherits the test's `sup-` provenance through the leaf). KB markdown uses an image-embed; Vol 9 `.tex` uses `\includegraphics`.
- **Engine code is cited via `\kbleaf{src/ave/...:line}` + the Vol 9 Canonical-Source column.** The "code-provenance index" named in INVARIANT-S12 / `SCHEMA.md` is **NAMED-NOT-BUILT** — grep confirms no `sim-` / `code-` node-type is materialized anywhere in the tools. Do **NOT** mint one ad-hoc: a first-class code-provenance node-type is a deliberate SCHEMA-extension decision **reserved for Grant**, not an implementer default. Track engine DOF-coverage via the existing `common/figures/engine_capability_matrix.yaml`.

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

## §2.5 — Target/precursor claims for the GAP layers (the chord-hunt's aim points)

The GAP layers L3–L5 are unbuilt; these are the verified KB precursor/target claims each layer would have to validate against (all ids grep-confirmed at KB HEAD). They are the aim points, **not** present backing — the §9 Spine column flags them `(precursor)`.

**L3 mass-cage / Γ=−1 / cutoff-mass:**
- `clm-rtdmsn` "Theorem 3.1′ — Electron Q-Factor from LC Tank at TIR Boundary" (vol4:1193, sol **0.85**, OK-TO-BUILD) — **strongest** TIR-boundary backing.
- `clm-i4p11y` "Electron = Photon + TIR Confinement" (vol1:1296, sol 0.45, INPUT-ONLY) — weak cage-as-TIR precursor.
- `clm-ka5zdx` "Mass-Closure Theorem mc²=E_reactive" (vol2:1200, sol 0.50, INPUT-ONLY) — the cutoff-mass = trapped-reactive-energy precursor.
- `clm-crbl60` "Vacuum Bulk Mass Density + Shear Modulus" (vol1:636, sol 0.62) + `clm-iouqn9` "K4 Magic-Angle K=2G" (common:1002, sol 0.55; provenance MERGED PR#261) — the c_bulk=√(K/ρ) constitutive T1.7 names as missing.
- **CAUTION (Γ=−1 wall):** `clm-lv3uw1` "Magnetic-Branch Confinement vs Electric-Branch Rupture" (vol1:260, sol 0.50, INPUT-ONLY) — the magnetic-branch is **B3-DEGENERATE** and "magnetic PRIMARY" is **asserted-not-derived** (H3 wall-branch fork, PR#260). Do NOT scope L3 on a settled magnetic-primary.

**L4 charge = winding / the (2,3):**
- `clm-67jn9o` "Quark Charges via Witten Effect on ℤ₃ Borromean" (vol2:272, sol **0.75**) — highest-solidity charge-quantization target.
- `clm-8c3yhs` "(2,3) Torus-Knot Uniqueness" (vol2:1310, sol 0.70) — strongest (2,3) backing.
- `clm-h9aqmt` "Electron as Topological Unknot 0₁" (vol2:10, sol 0.70).
- `clm-unk0bd` "Electron Body Topology 0₁ + (2,3) Winding" (vol1:10, sol 0.65, OK-WITH-CAVEATS) — primary charge=winding seat.
- `clm-oygz1i` "Topological Mass: Faddeev-Skyrme + Hopf Charge" (vol2:640, sol 0.60).
- Locked vocabulary: `def-3638f2` winding (:195) + `def-5d2b8a` the-3 (:416) + `def-9a4f07` longitudinal (:395). The micro-rotation charge seat is `master-equation.md:20` (the Grant-ratified TWO-3s disambiguation).

**L5 genesis / mass-spectrum (WEAKEST layer — NO solid precursor today):**
- `clm-8zpicx` "L3 (2,q) Particle Family" (vol2:1169, confidence **0.40**, **DO-NOT-BUILD-REWORK-NEEDED**) — the family-spectrum target, currently in rework; it is the **closest** target and it is below the build threshold.
- `clm-c54kdd` "SPICE Particle Decay — Qualitative Muon Model" (vol4:442, sol 0.70) — best muon backing but only QUALITATIVE.
- `clm-zw6mut` "Universal Spatial-Tension Mass Scaling" (vol1:516, sol 0.60) — the mass-ratio scaling target.
- `clm-pf84ng` "Genesis Algorithm + Chiral LC Over-Bracing" (vol2:995, sol 0.50).
- `clm-llqd1n` "Mass-Defect: Fitted Geometry NOT Ab-Initio" (vol6:10, sol 0.60) — the HONEST-LIMITS anchor (masses are fitted-geometry, not ab-initio).
- `clm-8niffj` "Q-G27 Muon Cosserat Torsion" (vol2:1450, sol 0.45).
- **CAUTION (genesis dynamics):** `common/genesis-chord-falsification-ledger.md` records the genesis **self-trap dynamics-class as FALSIFIED** — only the boundary-confinement operator is untested (engine-gap, not missing-axiom). An L5 acceptance layer has **no solid precursor to validate against today**.

## §2.6 — Strain/yield regime taxonomy (the "can this effect exist here?" gate)

**Why this section exists:** an acceptance test that runs in the WRONG REGIME for the effect it asks about returns a null that is an **ARTIFACT, not a falsification** (the dark-wake lesson: Phases 1–5 ran sub-yield-linear, where the rate-asymmetric / chiral effect cannot exist by construction — `ave-regime-phase-state-check`). Each layer's tests must declare which regime they operate in BEFORE the bins are frozen, and a null only falsifies if the effect could have existed in that regime.

**Strain coordinate + kernel (Axiom 4).** Strain coordinate `r = A / A_yield ∈ [0,1]`; the saturation kernel `S(r) = √(1 − r²)` (so `S=1` at `r=0`, `S=0` at `r=1`). The boundaries below are **grounded in `src/ave/core/regime_map.py`** (verify-before-cite — NOT invented):

- **Regime I — linear / sub-yield** (`r < r1 = √(2α) ≈ 0.1208`, `regime_map.py:68`). `S → 1`; all sector exponents collapse to `c/c₀ = 1`; the nonlinear correction `ΔS ≈ r²/2` is sub-α (unresolvable). Small-signal / DC-bias regime (EE: linearized `g_m`). **Rectification, asymmetric-grip, near-yield stiffening are ABSENT here by construction** — a null is expected, not informative.
- **Regime II — near-yield** (`r1 < r < r2 = √3/2 ≈ 0.8660`, `regime_map.py:69`). The cage stiffens (`c_eff → ∞` as `r → r_yield`); the sector exponents fan out monotonically. **This is the ONLY regime where rectification + asymmetric-grip live** (large-signal / switching, saturation onset; EE: Miller multiplication onset). A bulk near-yield compression cycle is the regime the L3 mass-cage actually exercises.
- **Regime III–IV — rupture** (`r ≥ r2`; `r3 = 1.0` exact at `regime_map.py:70`). `S → 0`; the binding wall reaches `Γ = −1` (the saturated short); the avalanche factor `M = 1/S²` (Op22 canonical, A43-v11 — NOT doc-81's `1/(1−S)`) `→ ∞`; topology destroyed at `r=1`. EE: junction breakdown, `M → ∞`. The Op-tier black-hole operating point is a Regime-IV instance.

**MODE × REGIME grid (can-this-effect-exist-here).** Three substrate MODES × four regimes. `✓` = the effect can exist + is meaningful to test; `lin` = present but linear/degenerate (the distinguishing constitutive is dormant); `—` = absent-by-construction (a null here is an artifact, not a falsification):

| MODE \ REGIME | I (linear) | II (near-yield) | III (avalanche) | IV (rupture) |
|---|---|---|---|---|
| **EM-transverse** (`c_EM = c₀/S`) | lin (`c≈c₀`) | ✓ index bends, achromatic SYM lens | ✓ high-Z wall builds | ✓ `Z → ∞` |
| **shear** (`c_shear = c₀√S`) | lin (`c≈c₀`) | ✓ `c_shear` freezes (mass-clock) | ✓ `Γ_shear → −1` | ✓ `c_shear → 0` |
| **bulk** (`c_bulk = √(K/ρ)`, `K=2G`) | lin (`c≈√2·c₀`) | ✓ rectification + asym-grip ONLY here | ✓ cavitation onset | ✓ `Γ = −1` short, avalanche `M=1/S²` |

**Standing guard (load-bearing):** *a null where the effect cannot exist in that regime is an ARTIFACT, not a falsification.* Before freezing any layer's bins, name the MODE, the REGIME, and the PHASE-STATE; if the pre-registered effect lives only in Regime II/III–IV, a Regime-I run cannot falsify it (it can only confirm the dormancy). This is the dark-wake correction made first-class.

**Regime-coverage map (tested vs gap, as of the 2026-06-17 L0–L2 + Op-tier arc):**
- **Tested — Regime I (linear/sub-yield):** L0-medium, L0-axioms (A1a/A1b/A2/A3b; A4 sweeps the kernel as a constitutive identity across operating points but the *downstream* modes run linear), L1 (all free modes, `S=1`), L2 (operating-point `A₀` modulation — the EM-transverse index does bend, but the SYM/ASYM contrast is the Regime-II-edge it reaches).
- **Tested — Regime IV (rupture) instance:** the Op-tier black-hole operating point (`test_operators.py`, `r ≥ 1 → S = 0`) — but as a **closed-form Op kernel evaluation**, not a time-domain bulk integrator (no detonation risk; CP10).
- **GAP — the load-bearing cells:** Regime-II **bulk** rectification + asymmetric-grip (the L3 mass-cage near-yield compression cycle) and the Regime-III–IV **bulk** `Γ=−1` short (T3.3, the make-or-break chord-decider) are entirely UNTESTED. The cavity/resonance/conserved-vs-pumped skill cluster (§8.5) is correctly dormant in the linear L0–L2 rungs and becomes first-class exactly at these Regime-II/III–IV bulk cells.

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

**Chirality leak verdict (investigation `w7etm1msb`):** the T1.5 ~92% energy bleed is a **2-line NumPy view-aliasing bug**, NOT physics, NOT a theory statement. `chiral_lattice_vector.py` rotates in-place on numpy VIEWS (the 2nd write reads the already-overwritten column → non-norm-preserving). **Fix = copy-first** (`v0=V_ref[...,0].copy()`).

> **🔴 [2026-06-17 Rule-12 update — STALE-then-RESOLVED] (verify `w0855uvzt`).** The clause below originally read "**DESIGNED + monkeypatch-verified, NOT YET APPLIED**" and cited the pre-fix lines `chiral_lattice_vector.py:43-46`/`:43` plus the 3 sisters under `src/ave/topological/…`. That was stale by ~19 min: the `.copy()` fix was **APPLIED at commit `484cecfc`** and is now LIVE at `chiral_lattice_vector.py:49-58`, with the 3 sisters all fixed under `src/ave/core/` (NOT `src/ave/topological/`): `chiral_lattice_vector_sat.py:91`, `chiral_lattice_v11.py:125`, `chiral_lattice_v13.py:140`. The §9 rows A1b/T1.5 ("`.copy()` fix applied") and the Ch17 leaf row 11 (cites `:49-58`) are correct; this §7 paragraph lagged them (A43-v2 stale-belief). Body preserved below per Rule-12; the **APPLIED** state above is the live truth.

The **0.92 → 1.6e-13** figure is the investigation's *monkeypatched* copy-first step (proof the fix works); it is now an applied code change. T1.5 has been FLIPPED from a leak-asserting FINDING to an Axiom-3 consistency gate (rotation-ON energy drift < 1e-8); the angle observable is unchanged either way (P2/P3/P4 verdicts stand). Contradicts Axiom 3 losslessness if NOT applied → applying the fix makes sim match theory. **Blast radius (now resolved):** the identical bug in the 3 sisters is fixed. **Gate gap:** the P1 losslessness gate runs `chiral_rotation=False`, so it never hit the bug — the new energy-conservation test WITH rotation ON (A1b / T1.5, Axiom-3 L0) closes it.

**Handedness = EMERGENT-from-the-lattice (answers the seed-vs-emergent question; a real chord on sign/null).** A linear (zero injected helicity, comp1_E=0) wave on srs gets its polarization rotated by the **lattice**: dθ/step = −0.0409 (srs-R) / +0.0409 (srs-L) / **exactly 0.0** (achiral diamond); rate = the lattice writhe. The substrate FORCES a signed, reflection-odd optical activity with an exact null on the achiral net — emergent (not seeded), **chord on sign/null** (magnitude is calibration). **Scope-limit:** this is optical-activity gyrotropy, NOT the localized charge e⁻/e⁺ sign — that still needs the BIN-G / CVR self-trap test. (K4 contrast: there helicity is *seeded* via `seed_cosserat_photon(helicity=±1)`.)

**Vocabulary locks before L4 (investigation LENS 3):** chirality (def-7c3f9e, ambiguous) / winding=the-3 (def-5d2b8a) / longitudinal (def-9a4f07) are locked + engine matches. **MISSING def-nodes:** optical-activity (= a GYRATOR / reciprocal-Faraday SO(2) polarization-plane rotation, EE-native; status SOLID-on-result #195 ±75.46°/unit), writhe (the reflection-odd geometric source pseudoscalar of the lattice circuits), helicity. **Live conflation:** the engine's bare token "rotation"/`rot_per_node` (optical-activity, a TRANSVERSE observable) shares the root word with the Cosserat **micro-rotation** (= the (2,3) winding = CHARGE) — declared ORTHOGONAL (A1⊥T2) but NOT def-fenced. **Fence before L4** (mint the def-nodes; Grant fork: rename the engine token off bare "rotation").

**Open forks → Grant:** (1) charge-SIGN — the rotation channel forces emergent optical activity (chord on sign/null) but cannot pin a localized charge's e⁻/e⁺ alone; is the BIN-G/CVR self-trap test the charge-sign discriminator before L4? (2) engine-token rename (`rot_per_node` → `optical_activity`/`gyro_rotation`) so grep never collides with the charge DOF.

## §8 — Full epic review (review `wzi4infks`, 2026-06-17): matrix, gaps, ritual, Vol 9, forks

**Honest scorecard:** the 12 built tests (L0 ×3, L1 ×5, L2 ×4) prove the engine is a **VALID MEDIUM** (L0–L2 consistency, all green) and force **ZERO chords** — the chords live at L3–L5, unbuilt. The implementer's tag downgrades are MORE correct than plan §2: **T2.2 + T2.3 are CONSISTENCY-of-mechanism, NOT chord** (magnitude rides input A₀(x); chord-question OPEN). Adopt those tags.

**The #1 gap — the §7 re-scope is the least-built layer.** Built L0 (T0.1–T0.3) is the OLD *behaviour*-L0, NOT the §7 *axiom-compliance* L0. **Split the ladder: L0-medium (built) vs L0-axioms (the §7 batch, GATE before L3+).** The L0-axiom batch is entirely GAP:
- **Ax1**: 6-DOF/node (3 transl→E + 3 microrot→B) + I4₁32 connectivity (T0.2 covers only the LC/Z₀ prong); + **chirality-lossless rotation-ON** (apply the .copy() fix → flip T1.5 from FINDING to an Ax-3 consistency gate).
- **Ax2 (TKI)**: NO test — [Q]≡[L] + ξ_topo=e/ℓ_node + dislocation-hosting (grep empty).
- **Ax3**: |Γ|²-minimization prong (matched→Γ→0) untested (T0.1 covers only the lossless-cycling prong).
- **Ax4**: saturation kernel S(A) only USED in L2, never VERIFIED as an L0 axiom-compliance gate.

**MULTI-WAVE-TYPE gap (Grant):** L1 currently tests only the **transverse photon**. The substrate carries a wave *family* — transverse-EM (c_EM=c₀/S), transverse-shear (c_shear=c₀√S), longitudinal-bulk (the A1 "3"), Cosserat-micro-rotation (gapped optical branch). **L1 = ALL free propagating modes**, each its own propagation/dispersion/speed test (Vol 9 Ch 5 AC + Ch 9 mechanical + Ch 10 microrotational). The wave types thread the ladder: each has a FREE form (L1) and a BOUND form (L3 bulk→mass-cage / L4 micro-rotation→winding=charge / L5 composite). Speeds c_EM/c_shear/c_bulk must be def-locked (the n=1/S, self-trapped-photon conflations).

**DOF / scope gaps:** the engine-map's 7 DOF — the ladder tests 5; **constitutive-loop/remanence (R10) + boost-covariance get NO layer** → add an L6+ frontier OR explicitly de-scope to Vols 1–6 cites (Grant fork).

**Vol 9 integration (all 17 chapters mapped).** Populated by the ladder: Ch1/Ch3 (axioms/DOF table), Ch4 (DC: Z₀, c₀ — T0.1/0.2/0.3), Ch5 (AC: propagation/dispersion/c_EM — L1/T2.1), Ch7 (saturation kernel — L2/Ax4), Ch11 (topology/(2,3) — L4), Ch12 (gravity FORM-bridge — T2.2, value=ECHO), Ch17 (engine-requirements — THE home). **Unaddressed by the ladder:** Ch6 temperature (no finite-T layer; δ_strain magnitude closed-negative), Ch8 breakdown-rupture (beyond L3), Ch9 bulk/couple-stress moduli (need L3), Ch10 conserving-rotation (needs the chirality fix), Ch12 cosmological *values* (echo axes), Ch15 falsification (orthogonal bench axis), Ch16 lookup. → ladder-scope fork (Grant).

**Ch17 rows to ADD (this arc's lessons):** (1) chiral-rotation must be unitary (no view-aliasing) + losslessness gate must run rotation-ON; (2) chirality/charge on the chiral srs grid, not achiral K4; (3) propagation tests use a localized one-way packet, not a Bloch standing wave; (4) use c_EM=c₀/S for the transverse photon — do NOT import the A1 1/S varactor as the EM index; (5) the keystone conserved-coupling confirmation.

**STANDING PER-LAYER COMPLETION RITUAL** (run before each layer's PR):
0. **DECLARE MODE + REGIME + PHASE-STATE before freezing the layer's tests** (`ave-regime-phase-state-check` first-class). For each test, name (a) the MODE (EM-transverse / shear / bulk), (b) the REGIME per §2.6 (I linear · II near-yield · III avalanche · IV rupture), and (c) the PHASE-STATE (saturation ON/OFF, seeded/cold). Cross-check the §2.6 MODE×REGIME grid: if the pre-registered effect cannot exist in the declared regime (e.g. rectification / asymmetric-grip outside Regime II–IV), a null is an ARTIFACT, not a falsification — re-scope the test or the regime BEFORE freezing the bins (the dark-wake lesson). Record the declaration in the §9 Regime column + the test docstring.
1. tests green (frozen pre-registered bins; tag each axiom-compliance/emergent/consistency/chord);
1.5. **MAP-TO-SPINE** — wire each green test into the KB claim-DAG as a derivation-support node (KB = source of truth). For each test in the layer:
   1. grep the corpus for the clm-/def- id(s) the test bears on (per `verify-before-cite` + `ave-prereg` corpus-grep) — the §9 Spine column is the human-readable index of these;
   2. author a `sup-` node in the suite's KB leaf with a `supports:` fan-out (`clm-<id>: <fraction>` per beneficiary), authoring **quality + every fan-out fraction as `*pending*`** until the test's local rigor + on-point relevance is scored (a `*pending*` support contributes NOTHING to a beneficiary and **must NEVER drag a beneficiary with otherwise-valid quality to pending** — cite **INVARIANT-S10** CRITICAL clause, `manuscript/ave-kb/CLAUDE.md:235`);
   3. add the matching `<!-- id: sup-xxxxxx -->` `### Quality` entry in a `claim-quality.md` register (the same register shape as a claim, `quality:` in place of `confidence:`);
   4. run `make refresh-kb-metadata` + `make verify-kb-metadata` so the `sup-` node materializes and the `.index/` regenerates clean.
2. figures captured (`KF_VIZ=1` regen off the same stepper);
3. Vol 9 doc — write the characteristic-chapter leaf(s) the layer populates + add the Ch17 requirement row(s);
4. manuscript figure capture — copy figures into `manuscript/vol_9_vacuum_datasheet/figures/` + `\includegraphics` in the chapter `.tex` (NOTE: close the wiring gap first — `main.tex:7 \graphicspath` does not include `research/figures/engine_acceptance/`);
5. engine-capability-map update — flip the now-tested DOF/characteristic row in `engine-capability-map.md` (+ the `engine_capability_matrix.yaml` cell `status: have|partial|absent`, re-render the PNG);
6. **Vol 9 LaTeX rebuild-to-validate** — `make vol9` from repo root (Makefile:255-256; pdflatex 3-pass + margin check) — clean build is the gate; **AND** `make verify-kb-metadata` (the spine drift-gate) so an orphan/dangling `sup-` or `def-` fails loudly alongside `make vol9`;
7. PR (branch off main, no self-merge); flag any chord-vs-echo verdict for Grant.
8. **ENGINES-ON-SPINE re-ask (standing per-layer directive, fork-2 / task #10).** At EACH layer completion, re-ask: *has the value of first-class engine nodes arisen yet?* The default answer remains **(a) cite engine code via `\kbleaf` per §1.5** (engine code is a `\kbleaf{src/ave/...:line}` reference + the Vol 9 Canonical-Source column, NOT a first-class spine node). Option **(b) — mint a code-provenance / `sim-` node-type via a deliberate SCHEMA extension** — is revisited ONLY if *code-coverage-of-claims* becomes a first-class query (e.g. "which clm- has engine-code backing, and at what line?" needs to be greppable as a graph edge rather than a prose cite). Minting a node-type is a Grant SCHEMA decision (§1.5, FLAGS (iii)), never an implementer default; this step just keeps the trigger condition under review per rung instead of deciding it once at L0.

**Recommended plan edits applied / pending:** §7 T1.5 "fixed" claim CORRECTED above (designed+monkeypatch-verified, not applied); fix the dangling `__init__.py:6` plan-pointer when the plan merges; adopt the T2.2/T2.3 consistency downgrades; the L0-medium/L0-axioms split + the multi-wave L1 + the ritual are recorded here.

**FORKS → Grant:** (a) **ladder scope** — add temperature/breakdown/cosmological layers for full-datasheet coverage, or scope to L0–L5 + leave those as Vols 1–6 cites? (b) **7-vs-5 DOF** — L6+ frontier for constitutive-loop + boost-covariance, or de-scope? (c) charge-sign (BIN-G/CVR) + engine-token rename (from §7).

**FLAGS / open-items (KB-claim-ID spine mapping arc, 2026-06-17 — record, do not resolve):**

- **(i) fork #1 RESOLVED-as-stale.** The earlier "plan doc absent on the suite branch" finding (cited at `__init__.py:6`) was a **stale-ref artifact**: the plan was MERGED to `main` (PR #276) and the suite branch was simply ~7 commits behind. Merged `origin/main` into `analysis/2026-06-16-engine-acceptance-l0l1` here; the plan doc is now present on the suite branch. No action needed beyond this merge.
- **(ii) fork OPEN → Grant: refractive_index exponent (flag-don't-fix).** `master_equation_fdtd.py:165-168` returns `S**0.25` while `c_eff_squared` (`:148-151`) implies n = `S**0.5`. **Do not fix** — adjudicate first. Must be resolved **before any L3/L4 build that consumes n or c_shear**, and it collides with the **T1.6 `c_shear=c₀·S^(1/4)` def-lock** (the same 1/4-vs-1/2 ambiguity). Physics-review item for Grant/auditor.
- **(iii) fork OPEN → Grant: are engines first-class on the spine?** Keep the `\kbleaf{src/ave/...:line}` default (per §1.5), OR mint a code-provenance node-type via a deliberate SCHEMA extension. The "code-provenance index" is named in S12/`SCHEMA.md` but NOT materialized — minting a `sim-`/`code-` prefix is a Grant decision, not an implementer default.
- **(iv) fork OPEN → Grant: is L5-genesis in-scope now?** Its closest target `clm-8zpicx` is sol **0.40 / DO-NOT-BUILD** and the genesis self-trap **dynamics-class is FALSIFIED** in the ledger (only the boundary-confinement operator is untested). There is **no solid precursor** to validate an L5 acceptance layer against today.

## §8.5 — Per-layer skill-selection (the 60-sec plan, mandatory per rung)

Per `feedback_skill_selection_planning`: write a **60-sec skill-selection plan BEFORE each rung is dispatched**, and run a **retroactive pass before commit if the applied set drifts** from the plan. The built L0–L2 files already DEMONSTRATE this discipline (the per-file `substrate-native-check` walk + consistency/chord class tags + the A46 coordinate note ARE the written-down plan); the plan doc mandates the same header on every future L3–L5 rung. The per-layer recommended firing map:

- **L0-medium (T0.1/T0.2/T0.3):** `substrate-native-check` (already walked, `__init__.py:96-119`); `ave-canonical-source` (Z₀, constants import); `consistency-vs-emergence` (T0.2 Class-A identity, T0.1/T0.3 Class-C); `phase-space-coordinate-check` (real-space correct here); `verify-before-cite`; `ave-apparatus-floor-attribution` (grid back-scatter floor).
- **L0-axioms (A1a/A1b/A2/A3b/A4):** `substrate-native-check` (CP6/7/9/10); `ave-representation-capability-check` (A1a carried_dof==2 vs axiom_dof==6 carrier-DOF FINDING); `consistency-vs-emergence` (per-axiom class tags; charge INTEGER = L4-out-of-scope); `ave-dimensional-provenance-check` (A2 [Q]≡[L] ξ_topo round-trip); `ave-apparatus-floor-attribution` (A4 S_min/A_cap sweep, R_SYM back-scatter floor); `ave-canonical-source` (A4 reads the canonical c_eff_squared kernel); `verify-before-cite`. NB: this layer's S\*\*0.25-vs-S\*\*0.5 flag (A4) is a live physics-review item (see FLAGS).
- **L1 free-modes (T1.1–T1.8):** `substrate-native-check`; `ave-regime-phase-state-check` (MODE/DOF/SPEED table + c_EM-vs-c_shear category guard — declares linear/achromatic so dispersion/rectification correctly ABSENT-by-construction); `ave-discipline-translate` (the c_shear=c₀·S^(1/4) corpus-form catch); `ave-representation-capability-check` (which-mode-on-which-DOF, two-3s); `consistency-vs-emergence` (all Class-C); `phase-space-coordinate-check`; `ave-apparatus-floor-attribution` (amplitude-decay/cross-pol-leak/front-edge floors); `ave-analytical-tool-selection` (Mode-analysis class).
- **L2 EM-in-media (T2.1–T2.4):** `ave-regime-phase-state-check` (operating-point A₀, SYM Γ=0 vs ASYM static-E Γ≠0); `ave-asymmetric-grip` (T2.3 static-E-ONLY = the asymmetric element breaking the SYM match); `consistency-vs-emergence` (T2.4 cites clm-3zz0f6; lensing MAGNITUDE left chord-OPEN); `ave-discrimination-check` (T2.2 achromatic-lensing = gravity bridge, magnitude OPEN not headlined); `ave-discipline-translate` (n=1/S(A₀) varactor framing); `ave-canonical-source`; `verify-before-cite` (clm-3zz0f6); `ave-cavity-class-identification` (precursor to L3).
- **L3 mass-cage (GAP — HIGH-VALUE skill cluster, NOT exercised in built L0–L2):** `substrate-native-check` (CP8 generative-precursor + CP10 boundary-not-bulk — the cage is a Γ-bounded boundary NOT a detonating bulk well); `ave-cavity-class-identification` (which sub-network hosts the bound eigenmode — load-bearing rung-specific); `ave-analytical-tool-selection` (pull Resonance + Boundary/TIR + Mode classes as a SET); `ave-resonant-amplification-check` (Q=α⁻¹ cavity must be BUILT or the A²≈O(α) stuck-floor recurs — founding failure of every prior L3 attempt); `ave-conserved-vs-pumped` (mass = A1 dilatation is energize+lock, not pump-to-threshold); `ave-regime-phase-state-check` (near-yield Regime-II); `ave-apparatus-floor-attribution` (winding-extractor poloidal r≈1.1-cell floor); `phase-space-coordinate-check` (R/r, (2,3), Clifford-torus = PHASE-SPACE not lattice-Cartesian); `consistency-vs-emergence` + `ave-discrimination-check` (cage chord tagging).
- **L4 charge (GAP):** `ave-representation-capability-check` (charge = winding INTEGER ±1, the (2,3) "second 3" micro-rotation NOT the A1 scalar — a scalar can't wind); `ave-conserved-vs-pumped` (charge/helicity/winding = conserved topological invariant, energize+lock, pumping nulls/detonates); `phase-space-coordinate-check` ((2,3) + writhe/helicity in phasor coords); `ave-cavity-class-identification` (charge sub-network vs mass sub-network); `substrate-native-check` (CP8 seed precursor, don't plant finished winding); `consistency-vs-emergence` (charge-quantization chord tag); `ave-asymmetric-grip` (Γ=−1 hardened-wall chiral buckle); `verify-before-cite` (two-threes / SECTOR⊥GAUGE anchors at `master-equation.md:20`).
- **L5 genesis (GAP — WEAKEST-backed layer, target clm-8zpicx confidence 0.40 / DO-NOT-BUILD):** `substrate-native-check` CP8 (seed the simplest autonomous action, let dynamics build the composite — do NOT plant the finished electron and test persistence); `ave-conserved-vs-pumped` (the entire 2026-06-09 V→ω-pump detonation arc was THIS one error); `ave-resonant-amplification-check` (Q=α⁻¹ self-lock cavity); `ave-cavity-class-identification` (which eigenmode self-generates); `ave-loop-gap-harness-discipline` (frozen-platform, advance-ranks, mandatory engine DAG ablations); `ave-regime-phase-state-check` (Regime-IV rupture, pair-production boundary); `ave-discriminator-before-synthesis` ("one device N observables" convergence-feeling = stop + name the splitter); `ave-engineering-program-rigor` (sensitivity sweep = robust-self-lock vs tuned-knife-edge); `consistency-vs-emergence` + `ave-discrimination-check` (genesis IS the chord — SM-counterfactual mandatory). PRECURSOR REALITY: the genesis self-trap dynamics-class is FALSIFIED in the ledger; only the boundary-confinement operator is untested.
- **Op-primitive/scale tier (BUILT, `test_operators.py`):** `substrate-native-check`; `ave-canonical-source` (Op22 canonical M=1/S² NOT doc-81's 1/(1−S), A43-v11 flag honored); `consistency-vs-emergence` (CODATA sub-targets consistency-class NOT headlined emergence); `ave-analytical-tool-selection` (toolkit-index 11-class taxonomy IS the Op-class map); `ave-power-category-check` (real-vs-reactive Axis-A); `ave-regime-phase-state-check` (scale-invariance instance: same Op path electron-scale + BH-scale); `ave-independence-check` (cross-scale instances = SAME kernel, not N independent confirmations); `verify-before-cite`.

**HIGH-VALUE note (do not let clean L0–L2 create false confidence the skill-baking is done):** the cavity/resonance/regime/conserved-vs-pumped cluster — `ave-cavity-class-identification`, `ave-resonant-amplification-check`, `ave-conserved-vs-pumped`, `ave-regime-phase-state-check` — is **correctly DORMANT in the linear/sub-yield/achromatic L0–L2 rungs** (those effects are absent-by-construction there) but becomes **FIRST-CLASS load-bearing the moment the L3 cage / L4 charge / L5 genesis rungs are built**. Those skills' FOUNDING failure-modes (the A²≈O(α) stuck-floor, the V→ω pump detonations, the winding-extractor poloidal floor) all live precisely at the unbuilt rungs, and nothing in the current suite forces them. The clean L0–L2 discipline must NOT inherit the "these don't fire here" posture into L3–L5.

## §9 — COMPLETENESS MATRIX (LIVE CHECKLIST)

**This is the single live tracker.** Status updated per the §8 completion ritual (a row flips to ✅ only after: tests green + figures + Vol 9 leaf/Ch17 row + engine-map flip + `make vol9` clean). Legend: ✅ built-green (positive: a mode/value confirmed PRESENT) · ⊘ absence-finding (the test PASSES iff a DOF/mode is confirmed ABSENT — an honest gap-record, NOT a positive; inverted-regression semantics) · 🔧 fix-pending · ⬜ GAP (not built) · 🚩 frontier (gated on Grant). Tag = axiom-compliance / emergent / consistency / chord / finding (DOF-absence). **Regime column (§2.6, KEEP-BOTH):** the strain/yield regime each test operates in — I linear/sub-yield · II near-yield · III avalanche · IV rupture; the built L0–L2 rungs are Regime I (L2 reaches the Regime-II operating-point/SYM-bias edge), the Op-tier is a Regime-IV instance, and the L3–L5 GAP rows are tagged with the regime they WILL exercise (the standing guard: a null where the effect cannot exist in that regime is an ARTIFACT, not a falsification).

| Layer | Test | Tag | Characteristic / DOF | Vol 9 | Spine (clm-/def- backing) | Regime (§2.6) | Status |
|---|---|---|---|---|---|---|---|
| **L0-medium** | T0.1 energy/unitary-scatter | axiom (Ax3 lossless) | medium unitarity | Ch4/Ch3 | clm-hd9bee | I (linear) | ✅ |
| L0-medium | T0.2 Z₀=√(μ₀/ε₀) | axiom (Ax1 LC identity) | port impedance | Ch4 | — (medium-validity, no clm-) | I (linear) | ✅ |
| L0-medium | T0.3 isotropy | consistency | medium validity | Ch4/Ch9 | — (medium-validity, no clm-) | I (linear) | ✅ |
| **L0-axioms** | A1a 6-DOF/node + I4₁32 connectivity | axiom (Ax1 topology) | 6 DOF, chiral grid | Ch1/Ch3/Ch11 | — (medium-validity, no clm-) | I (structural) | ✅ (DOF finding) |
| L0-axioms | A1b chirality lossless (rotation ON) | axiom (Ax1 chirality) | optical-activity DOF | Ch1/Ch11 | def-7c3f9e | I (linear) | ✅ (sup-zf5d1t; .copy() fix applied) |
| L0-axioms | A2 TKI [Q]≡[L], ξ_topo, dislocation | axiom (Ax2) | charge=geometry | Ch4/Ch11 | clm-dfaiwj | I (identity) | ✅ (sup-u7r3vu) |
| L0-axioms | A3b \|Γ\|²-minimization (matched→Γ→0) | axiom (Ax3 min-refl) | min-reflection | Ch3 | clm-8nkvwy | I (linear) | ✅ (sup-l2ah0k) |
| L0-axioms | A4 saturation kernel S(A) verified | axiom (Ax4) | saturation | Ch7/Ch14 | clm-gz7ryg; clm-8nkvwy | I→IV (kernel sweep) | ✅ (sup-2qja9z) |
| **L1 free modes** | T1.1 transverse-EM (photon) lossless | consistency | photon, c_EM | Ch5/Ch4 | clm-3npynp; clm-djpx2v | I (linear) | ✅ (hardened) |
| L1 free modes | T1.2 dispersionless band ω=ck | consistency | photon dispersion | Ch5 | clm-djpx2v | I (linear) | ✅ |
| L1 free modes | T1.3 transversality (2-pol, no leak) | consistency | 2 transverse DOF | Ch3 | clm-3npynp; clm-j550uh | I (linear) | ✅ |
| L1 free modes | T1.4 causality / front-speed | consistency | no superluminal | Ch4 | clm-yr6tu4 | I (linear) | ✅ |
| L1 free modes | T1.5 optical-activity (chiral channel) | consistency-gate (post-fix) | optical activity | Ch5/Ch10/Ch11 | def-7c3f9e; def-0pt1ac | I (linear) | ✅ (sup-w6tjvs; .copy() fix applied) |
| L1 free modes | T1.6 transverse-SHEAR wave (c_shear=c₀√S) | consistency | shear mode | Ch5/Ch9 | clm-crbl60; clm-8nkvwy | I (linear; c_shear dormant) | ✅ (sup-oicgzy; constitutive gap REPORTED) |
| L1 free modes | T1.7 longitudinal-BULK wave (the "3") | finding (DOF-absence) | bulk mode, c_bulk | Ch5/Ch9 | finding (no positive clm-); precursor clm-iouqn9, clm-crbl60 | I (linear; DOF absent) | ⊘ (absence-finding: mode NOT carried = L3 gap) |
| L1 free modes | T1.8 Cosserat micro-rotation wave (gapped) | finding (DOF-absence) | micro-rotation mode | Ch5/Ch10 | finding (no positive clm-); precursor clm-3npynp; def-0pt1ac | I (linear; DOF absent) | ⊘ (absence-finding: mode NOT carried = L4 gap) |
| **L2 EM-in-media** | T2.1 refractive index c_EM=c₀/S | consistency (Op14) | operating-point | Ch5/Ch7 | clm-8nkvwy | II (operating-point A₀) | ✅ |
| L2 EM-in-media | T2.2 achromatic lensing | consistency-of-mechanism | SYM gradient (gravity) | Ch12/Ch5 | clm-k9up5c; clm-07kd5v | II (SYM bias) | ✅ |
| L2 EM-in-media | T2.3 asymmetric mirror Γ≠0 | consistency | Meissner-asym | Ch3/Ch7 | clm-8nkvwy; clm-5s5b0d | II (ASYM bias) | ✅ |
| L2 EM-in-media | T2.4 α-invariance under SYM | consistency (clm-3zz0f6) | α-invariance | Ch5/Ch12 | clm-3zz0f6; clm-8nkvwy | II (SYM scaling) | ✅ |
| **L3 mass-cage** | T3.1 longitudinal-mode-is-real | chord (vs QED) | A1 bulk DOF | Ch9/Ch4 | clm-crbl60 (precursor) | I→II (bulk) | ⬜ |
| L3 mass-cage | T3.2 c_eff(V) stiffening →∞ | emergent (Ax4) | mass-cage | Ch8/Ch14 | clm-gz7ryg (precursor) | II (near-yield) | ⬜ |
| L3 mass-cage | T3.3 binding-wall Γ=−1 (make-or-break) | chord | Γ=−1 TIR wall | Ch3/Ch2 | clm-rtdmsn; clm-lv3uw1 (precursor) | III–IV (rupture, Γ=−1) | ⬜ ⭐ |
| L3 mass-cage | T3.4 mass = cutoff freq ω₀ | emergent | mass observable | Ch2/Ch9 | clm-ka5zdx (precursor) | II→III (near-yield→trap) | ⬜ |
| **L4 charge/winding** | T4.1 (2,q) winding forms/persists | consistency-of-existence | winding DOF | Ch11 | clm-unk0bd; clm-8c3yhs (precursor) | II–III (near-yield buckle) | ⬜ |
| L4 charge/winding | T4.2 charge = integer winding ±1 | chord (unfakeable int) | charge | Ch11/Ch10 | clm-67jn9o; def-3638f2 (precursor) | III (hardened wall) | ⬜ ⭐ |
| L4 charge/winding | T4.3 handedness e⁻/e⁺ | chord (candidate-c) | charge sign | Ch11/Ch10 | clm-h9aqmt; def-h3l1c7 (precursor) | III (hardened wall) | ⬜ (→fork c) |
| **L5 coupling/genesis** | T5.1 coupling conserves energy (keystone, unified) | consistency (Ax3) | mode-conversion | Ch17 | clm-pf84ng (precursor) | II (near-yield lock) | ⬜ |
| L5 coupling/genesis | T5.2 electron self-assembles (no plant) | chord (genesis) | mass+charge co-emerge | Ch11 | clm-8zpicx (precursor; sol 0.40 DO-NOT-BUILD) | II→III (genesis cycle) | ⬜ |
| L5 coupling/genesis | T5.3 forced m_μ/m_e from (2,q) | chord (THE decider) | forced mass ratio | Ch11/Ch13 | clm-zw6mut; clm-c54kdd (precursor) | III (family spectrum) | ⬜ ⭐ |
| **L6+ frontier** | constitutive-loop / remanence (R10) | — | DOF (7-of-7) | Ch10 | — (medium-validity, no clm-) | II (hysteresis loop) | 🚩 (fork b) |
| L6+ frontier | boost-covariance (Lorentz) | — | DOF (7-of-7) | — | clm-yr6tu4 (precursor) | I (linear) | 🚩 (fork b) |
| L6+ frontier | node-creation (pair production) | — | DOF / genesis | Ch8 | — (medium-validity, no clm-) | IV (rupture) | 🚩 (fork a) |

> **Spine cell = theoretical backing (clm-/def-).** The sup-\<id\> that materializes each test as a derivation-support node is minted at completion-ritual time (see §8 step 1.5), not here.

⭐ = the three chord-deciders (Γ=−1 mass wall · integer charge · forced mass ratio). **Vol 9 chapters with no ladder row** (fork a): Ch6 temperature, Ch8 breakdown-rupture, Ch12 cosmological-values, Ch15 falsification (orthogonal bench axis), Ch16 lookup. **Score (completion-ritual run 2026-06-17, glyph-split 2026-06-17 per verify w0855uvzt): 18 ✅ positive / 2 ⊘ absence-finding / 0 🔧 / 10 ⬜ / 3 🚩 (total 33) — valid medium, zero chords forced yet.** The two ⊘ rows (T1.7 bulk / T1.8 Cosserat micro-rotation) are absence-findings: the test PASSES iff the DOF is confirmed ABSENT, recording the precise L3/L4 medium-extension gap — they are split out of the positive-✅ bucket so the headline tally cannot be misread as "bulk + Cosserat wave validated." The ritual flipped **9 cells** to a green-confirmed status — **7 from ⬜ (A1a, A2, A3b, A4, T1.6, T1.7, T1.8) and 2 from 🔧 (A1b, T1.5)** — of which 7 are positive-✅ and the 2 absence-findings (T1.7/T1.8) now carry ⊘. (A prior pre-flip score line read "12 ✅" but a direct symbol-count of that matrix was 11 ✅ — it over-counted ✅ by 1, which is the root of the earlier "flipped 8" off-by-one; the **TIP totals (20 green-confirmed = 18 ✅ + 2 ⊘ / 0 🔧 / 10 ⬜ / 3 🚩 across 33 rows) are arithmetically correct**, independently recounted.) The copy-first `.copy()` fix is APPLIED (A1b/T1.5 green with rotation ON). **The Op-primitive + scale-invariance tier (`test_operators.py`, `sup-evhfcd` → `clm-sysqaf`, `clm-m7qd0w`) is also GREEN-confirmed** (it is not a §9 matrix row — it runs ALONGSIDE the L-ladder). The chord-deciders ⭐ (T3.3 Γ=−1 · T4.2 integer charge · T5.3 forced mass ratio) and all L3/L4/L5 GAP rows remain ⬜/🚩 — Grant-gated, NOT flipped.
