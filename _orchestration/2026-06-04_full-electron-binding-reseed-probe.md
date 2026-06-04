# Full-electron binding — re-seed probe brief (2026-06-04)

**Status:** PENDING — implementor dispatch (worktree-isolated, branch off main).
**Orchestrator:** this brief + the fork-discrimination logic; implementor runs the driver.
**Origin:** the `phase3f` electron-torus-knot attempt (2026-05-18) FAILED — the (2,3) knot
dispersed worse than random (20.9% vs 56.3% retention). Diagnosis (phase3f §Factor 5): the seed
put the (2,3) winding in REAL space, but the canonical electron carries it in the **(V_inc, V_ref)
phasor phase-space** (`leaky-cavity-particle-decay/theory.md:16`). That is the A46 /
phase-space-coordinate-check failure. The thread then pivoted to cosmic-cooling and never retried.
This probe re-seeds correctly + discriminates a load-bearing fork.

---

## §1 Target + physical picture (Step 1.5)

**Target:** Does the full-vector Maxwell FDTD engine (`src/ave/core/fdtd_3d.py`) autonomously host a
bound **(2,3)-knotted electron** — mass + spin + charge — when seeded with the canonical placement
(unknot in real space, (2,3) winding in the (V_inc,V_ref) characteristic phasor)?

**Picture (mechanical/topological):**
1. **Layer 1 — mass** = a real-space **Beltrami loop** (the horn-torus unknot, R=r=ℓ_node/2π):
   ∇×A=kA, B∥A force-free, |E|=c|B|, E⊥B feeding around the loop (`electron-unknot.md:9`).
2. **Layer 2 — spin** = the B field, automatic via Maxwell curl in `fdtd_3d.py` (Cosserat ω = B per
   Axiom 1).
3. **Layer 3 — charge** = the **(2,3) Clifford-torus winding in the (V_inc, V_ref) phasor TRAJECTORY**
   (a temporal Lissajous winding 2:3), where the candidate continuum mapping is the transmission-line
   characteristic decomposition **V_inc = E + Z·H, V_ref = E − Z·H**. Handedness sets charge sign
   (LH Beltrami = e⁻, RH = e⁺, `pair-production-axiom-derivation.md:77`).
4. **Confinement** = at amplitude → V_snap the local Z→∞, Γ→−1 mirror reflects the wave into the
   core (self-trap). The kernel c_eff(V)=c₀/√S engages near A→1.
5. **The discriminating fork** (the whole point): is (V_inc,V_ref) the continuum characteristic
   decomposition of (E,H) — which `fdtd_3d.py` already carries (→ re-seed binds) — or the genuinely
   DISCRETE K4 4-port bond structure (→ a continuum field can't host it; need K4-TLM + c_eff)?

---

## §2 Skill-selection plan (looked at each skill; APPLY set for the implementor)

**Load-bearing (MUST apply, in order):**
- **ave-prereg** — corpus-grep + frozen prereg BEFORE the driver. (Orchestrator pre-grepped §3; confirm + extend.)
- **substrate-native-check** — walk `fdtd_3d.py` (E/H Yee grid, nonlinear ε(E)/μ(H), Mur/CPML) before the seed: name the sector, the coordinate system (phase-space vs real-space — Checkpoint 4 is THE one), the reactance pair (E↔H), the saturation-modulated clock (c_eff at A→1), PML exclusion in sampling.
- **phase-space-coordinate-check** — THE fix. The (2,3) MUST be placed in (V_inc,V_ref)=(E±Z·H) phasor coordinates, NOT real-space field direction. Verify the seed + the winding-number OBSERVABLE both live in the phasor coordinates the corpus claim lives in.
- **ave-canonical-source** — import `V_YIELD`, `V_SNAP`, `L_NODE`, `Z_0`, `ALPHA_COLD_INV` from `ave.core.constants`; NO hardcoded literals; add a verify-constants cross-check before any plot/verdict.
- **ave-canonical-leaf-pull** — pull the bound-state/Beltrami/(2,3)-knot/Q-factor class: `theory.md:16` ((2,3) in phasor), `electron-unknot.md:9` (Beltrami), `pair-production-axiom-derivation.md:77` (LH/RH handedness), `theorem-3-1-q-factor.md` (Q=α⁻¹ boundary observable), L3 doc 70 (Beltrami-bound-pair recipe), `electron-unknot-cosserat-seeder.md`.
- **ave-driver-script-honesty** — the driver asserts "the electron binds." Run the four-discriminator check: (a) canonical-import not hardcoded; (b) FORWARD prediction not a fit-to-target (no Nelder-Mead onto a known answer); (c) no internal print-vs-compute contradiction; (d) no silent overclaim (plotting the seed as if it were the converged result).
- **consistency-vs-emergence** — classify the test. It's a Class-D-style DYNAMIC engine test (does the engine autonomously host the bound state). FLAG any α-injection in the seed geometry (R=r=ℓ_node/2π is geometry, not α; but if any seed parameter routes through α, name it). This is NOT an α-emergence claim (that's closed Class B — `ch8:11`); it's a topology-binding test.
- **ave-fundamental-ground-up-implementation** — the PASS thresholds (retention %, winding tolerance, persistence steps, Q-factor rel-err) must be substrate-derived or honestly tagged engineering-choice — NOT arbitrary bars. Critically: fix phase3f Factor-2 — the baseline must be a **matched-amplitude-distribution topologically-trivial** seed, NOT a random-direction seed (random gave larger single-component amplitudes → more saturation → spurious "better" retention).
- **ave-evidence-framing-discipline** — precision on the result claim; "binds" requires all PASS criteria, not just persistence.
- **ave-ee-first-mapping** — adjudicate the continuum-vs-discrete (V_inc,V_ref) question EE-first: is the (2,3) phasor the forward/backward characteristic split of (E,H) (continuum, transmission-line Riemann invariants) or the discrete K4 4-port? Document which the seed assumes + why.

**Secondary (apply if triggered):**
- **ave-infinity-discipline** — the c_eff→∞ / NaN-blowup at A→1 (the phase3f Factor-3 failure at 0.85·V_yield/dx); use the S_min floor + lattice cutoff, document the clip.
- **pre-test-physics-check** — surface any NEW plumber-physical question to Grant (via orchestrator) BEFORE locking the seed; do NOT free-build past an ambiguity.
- **ave-discrimination-check** — only if framing the binding as an AVE-distinct forward claim (it's an internal engine test; likely N/A).
- **ave-audit** — request an auditor pass on the result before declaring Mode I.
- **verify-before-cite** — every file:line + every "binds/disperses" status claim verified to source.

**Skip (looked, not relevant):** ave-cavity-class-identification (no cross-phenomenon shared-mechanism claim), ave-independence-check (single test), ave-ip-divide-discipline (core engine), ave-sweep-audit (single driver), ave-walk-back (no retirement), ave-newly-created-skill-self-audit (no new skill), ave-power-category-check / ave-analytical-tool-selection (bound-state class understood), ave-directory-enumeration-discipline / ave-module-library-discipline (infra), ave-handoff-canonical-locale + ave-worktree-paths (orchestrator-side, handled).

---

## §3 Corpus-grounded recipe (orchestrator pre-grep — confirm + build on)

- **Canonical (2,3) placement:** `vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md:16` — *"unknot in real space carrying a (2,3) Clifford-torus winding in phase space… the (V_inc,V_ref) phasor trajectory, NOT the real-space flux-tube topology."*
- **Beltrami construction:** `vol2/particle-physics/ch01-topological-matter/electron-unknot.md:9` (∇×A=kA, E⊥B closed loop); L3 doc 70 §"Applied to pair-nucleation" (Beltrami-bound-pair: ω_A=−√2·p̂ LH, ω_B=+√2·p̂ RH, Φ_link=±1.0); `electron-unknot-cosserat-seeder.md` + `cosserat_field_3d.py:initialize_electron_unknot_sector()`.
- **Characteristic mapping candidate:** `radial-eigenvalue-solver.md:311` (forward/backward propagating waves on the TL); standard TL: V± = (E ± Z·H)/2.
- **Engine:** `fdtd_3d.py` (full-vector Maxwell, nonlinear ε(E)=ε₀√(1−(E·dx/V_yield)²), μ(H)=μ₀√(1−(B/B_yield)²), Mur/CPML); the prior FAIL: `test_fdtd3d_electron_torus_knot_seed.py`; prereg: `2026-05-18_fundamental-topology-verification-program.md`.

---

## §4 Adjudication + the FORK (the deliverable)

PASS criteria (Mode I) — substrate-derived, matched-baseline:
- **Knot retention > matched-distribution trivial baseline** (NOT random — same per-component amplitude statistics, topologically trivial).
- **(2,3) winding number conserved** in the (V_inc,V_ref) phasor (toroidal 2, poloidal 3) to a substrate-justified tolerance.
- **n(r) gradient** measurable outside the core (the gravity halo).
- **Bound-state persistence** ≥ the v14 window without amplitude decay past threshold (breathing allowed — use the mean-V_peak breather criterion per doc 113, not the strict stationary one).
- **Q-factor integral** ≈ α⁻¹ (the integrated boundary observable, per v14 §14.7).

**Fork-discrimination verdict (the load-bearing output):**
- **Mode I (binds, winding conserved on `fdtd_3d.py`)** → the (V_inc,V_ref) phase-space IS the continuum characteristic decomposition of (E,H); the full electron hosts on the existing engine; CONTINUUM hypothesis confirmed.
- **Mode III (disperses even with the correct phasor seed + Beltrami pair + near-V_snap amplitude, across ≥3 seed parameterizations)** → strong evidence the DISCRETE K4 4-port is genuinely load-bearing; the continuum engine cannot host the (2,3); the path forward is K4-TLM + c_eff(V) (doc 111 Path A). Report this as the fork verdict — it is as valuable as a PASS.
- **Mode II (binds but winding/observables off)** → partial; seed-construction or operating-point issue; diagnose.

## §5 Deliverables
- `src/scripts/vol_1_foundations/r10_fdtd3d_electron_binding_v2_reseed.py` (the driver; incremental commits — skeleton first, then one section per commit per the incremental-write discipline).
- `research/2026-06-04_full-electron-binding-reseed-result.md` (prereg + result + the fork verdict).
- Push the branch; do NOT merge (orchestrator merges after auditor pass).
- Surface to orchestrator (do not self-resolve) any framing ambiguity that needs Grant.
