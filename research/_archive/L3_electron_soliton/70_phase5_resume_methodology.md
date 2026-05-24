# 70 — Phase 5 PairNucleationGate resumption: ansatz-initialization methodology per Round 6 closure

**Status:** 2026-04-25. Round 6 single-electron-validation arc closed empirically (10 commits a53ce1c→c830f07 + manual r8.5 at 00cb22c). Per Grant 2026-04-25: *"single-electron precondition was methodology gap, now characterized; topology can be encoded via ansatz initialization in pair-nucleation context too."* This doc frames the Phase 5 resumption — applying Round 6's ansatz-initialization finding to the pair-nucleation gate-firing problem.

**Read after:** [doc 67_ §17-§26](67_lc_coupling_reciprocity_audit.md), [doc 68_](68_phase_quadrature_methodology.md), [doc 69_](69_bootstrap_chain_calibration.md). [STAGE6_V4_HANDOFF.md §R6.9-§R7](.agents/handoffs/STAGE6_V4_HANDOFF.md) carries the closure summary.

---

## 1. Round 6 closure summary

The F17-K methodology arc closes empirically with 5 audit findings + bootstrap-chain validation:

**Audit findings:**
- **A28** — engine had double-counted K4↔Cosserat coupling since Phase 4. Op14 z_local IS the coupling channel; legacy `_compute_coupling_force_on_cosserat` was redundant. Six prior failure modes unified under one bug. Closed.
- **A29** — F17-I three-mode framing was Axiom-3 noncompliant. Φ_link is a derived flux observable in K4-TLM, not an independent dynamical state. Closed.
- **A30** — corpus-duality (Cosserat-energy ≈ S₁₁ co-locate at Golden Torus per Vol 1 Ch 8) FALSIFIED at coupled-engine scale: dual descent under saturation pin gave R/r=3.40 (energy) vs R/r=1.03 (S₁₁), neither at φ²=2.62. Closed.
- **A31** — F17-K Phase 6 sparse eigensolver methodology characterized as load-bearing for empirical bound-state validation. Open, deferred to Round 7 Stage 1 (fresh session, properly preregistered).
- **A32** — v3 (i) X4b linear-stability test: Golden Torus seed UNSTABLE under coupled S₁₁ (5.3× perturbation growth in 30 iters), MARGINAL under Cosserat-energy. Cosserat-only X4b stability does not extend to coupled engine. Closed.

**Empirical anchor:**
[Doc 03_ §4.3](03_existence_proof.md#L4) verbatim:
> "R·r = 1/4: topologically quantized, NOT dynamically derived... the Lagrangian must be *consistent with* but does not by itself produce."

Empirically validated at both global-flow (v2-v2) and linear-stability (v3 (i)) levels at coupled-engine scale.

**Bootstrap-chain anchor:**
[Doc 69_](69_bootstrap_chain_calibration.md): Q = 1/α = 137.036 holds to machine precision (rel_err 6.5×10⁻¹¹) via the algebraic chain ℓ_node → ξ_topo → L_e → ω_C·L_e = ℏ/e² → Q = (ℏ/e²)/(Z_0/(4π)). Tautologically self-consistent. Bare K4-TLM ≠ LC tank — kinetic inductance lives in Cosserat sector.

**Methodology characterization:**
The single-electron precondition was a **methodology gap, not a simulation result**. Topology is encoded by **ansatz initialization** (doc 34_ X4 algebraic-pin pattern, doc 28_ phase-space framing), NOT by dynamical descent. Pure descent (energy or S₁₁) on coupled K4+Cosserat cannot reach Golden Torus from arbitrary seed because R·r=1/4 is a topological identity selected from a continuous family of (2,3) stationary states.

---

## 2. Phase 5 pre-Round-6 state

Per [VACUUM_ENGINE_MANUAL.md §13.5](VACUUM_ENGINE_MANUAL.md):

**PairNucleationGate status (commit `9ecc2ca`):**
- Code landed with 32-test suite + Bingham-capsule framing
- Gate logic: C1 (saturation: A²_μ(r_A) ≥ 0.95 AND A²_μ(r_B) ≥ 0.95) AND C2 (autoresonant lock: |Ω_node − ω_drive| < ω_drive·α)
- On C1 ∧ C2: inject Beltrami-bound-pair (ω_A = -√2·p̂_bond LH, ω_B = +√2·p̂_bond RH; Φ_link = ±Φ_critical = ±1.0)
- Re-fire prevention via `_nucleated_bonds` set

**Last empirical run (`phase5_pair_nucleation.py`, commit `3f9569b`):**
- Config: N=24, amp=0.5·V_SNAP, autoresonant collision, λ=3.5
- **Verdict: NO-FIRE** (0 firings across 50 Compton periods)
- **C1 undershoot:** max A²_μ ≈ 0.75-0.91 vs sat_frac=0.95 threshold
- C2 moot (couldn't be evaluated without C1 satisfied first)

**R5.10 Readings 1-4 of C2 condition** (suspended pre-Round-6):
1. Compton-lock-is-rupture (frequency lock vs voltage rupture boundary)
2. PLL-chirps-past-lock (phase-locked-loop stability margin)
3. Drive-health-boolean (source validity check)
4. Parity-chirality-coincidence (topological alignment)

**Suspension reason:** the engine couldn't stage one bound electron yet (Path A falsified, Path B blocked); debating triggers for two bound electrons was premature.

**Phase 5e cool-from-above driver** (`phase5e_cool_from_above.py`, commits `1805d14`+`098d430`+`d0609ad`): two-phase saturation+cool. First empirical cool-through-yield observed (S_min=0.507 → 0.983 post-drive). Gate still NO-FIRE because Cosserat A²_μ peaked at 0.012 (K4→Cosserat coupling weakness; Step 5a finding).

---

## 3. Round 6 finding applied to pair-nucleation context

The pair-nucleation gate has the same structural problem as F17-K's bound-state finder: **dynamical thresholds (C1/C2) won't necessarily fire from any starting point**, even under driven excitation. Per Round 6:

- Cosserat saturation A²_μ peaked at 0.012 in Phase 5e → coupling alone is insufficient drive
- Even at higher amplitude (Phase III-B v2 at A²=1.009), 0/20 seeds crossed Regime IV → autoresonant pumping is operational regime, not bound-state finder
- Ansatz initialization (doc 34_ X4 + phase-coherent seeding per doc 68_) decouples bound-state existence from threshold-chase

**Applied to pair-nucleation:** seed the **expected post-firing state** (Beltrami-bound-pair at bond endpoints) directly, with drive present. This decouples three orthogonal questions:

(α) **Does the gate mechanism work?** I.e., given a configuration that satisfies C1 AND C2 by construction (or via explicit `_inject_pair` call), does the gate fire and produce the registered Beltrami injection?

(β) **Does the seeded pair persist post-drive?** I.e., once drive turns off, does the Φ_link[A→B] retain its critical magnitude (Kelvin topological-protection per Bingham-plastic framing)?

(γ) **Does the C1/C2 threshold get reached under drive?** This was the original Phase 5 question. Pre-Round-6 answer: NO at registered config (N=24, amp=0.5·V_SNAP). Post-Round-6: this is a SEPARATE empirical question from (α)+(β); they don't all need to pass at the same parameter set for Phase 5 to advance.

The R5.10 Readings 1-4 were arguing about how to interpret C2 in the case where C1 IS reached but C2 ambiguous. Round 6's framing **pre-empts** this debate: don't argue about C1/C2 interpretation; build a driver that decouples gate-mechanism (α) from threshold-chase (γ), validate (α)+(β) directly, then return to (γ) with a tested gate.

---

## 4. Phase 5 ansatz-seeded methodology

The corpus-canonical pattern for "encode topology + verify dynamics" is doc 34_ X4 framing applied to the bound state. doc 34_ X4a swept amplitude at fixed Golden Torus geometry; X4b ran `relax_s11` at the X4a-best amplitude to verify stationarity. The PHASE-COHERENT extension (per doc 68_) seeds (V_inc, V_ref) at 90° quadrature with (2,3) phase-space pattern.

For pair-nucleation, the analog is:
- Initialize at the post-firing state (pair already nucleated, Beltrami ω at endpoints, Φ_link = ±Φ_critical)
- Apply hard saturation pin (`_project_omega_to_saturation` from coupled_s11_eigenmode.py) to keep peak |ω| at saturation onset (0.3π) per F17-K v2-v2 finding
- Drive present (autoresonant CW source at amp=0.5·V_SNAP, same as registered config)
- Observe gate behavior and post-drive persistence

**Reusable infrastructure from F17-K:**
- `tlm_electron_soliton_eigenmode.py:initialize_quadrature_2_3_eigenmode` — phase-coherent (V_inc, V_ref) seeder (doc 68_ / Phase 5a infrastructure)
- `coupled_s11_eigenmode.py:_project_omega_to_saturation` — hard projection onto saturation manifold (Round 6 v2-v2 finding)
- `vacuum_engine.py:PairNucleationGate` — gate code unchanged (sound)
- `vacuum_engine.py:AutoresonantCWSource` — drive infrastructure (commit aa7a337, A7-closed PLL)

**Reusable seeders:**
- `cosserat_field_3d.py:initialize_electron_2_3_sector` — Cosserat ω hedgehog (doc 34_ X4a baseline)
- `tlm_electron_soliton_eigenmode.py:initialize_phi_link_2_3_ansatz` — K4 Φ_link seeder
- `cosserat_field_3d.py:initialize_u_displacement_2_3_sector` — Cosserat u seeder

---

## 5. Concrete next experiment — `phase5_ansatz_seeded_nucleation.py` driver

**Scope:** ~150 LOC new driver in `src/scripts/vol_1_foundations/`. NO changes to PairNucleationGate code or to F17-K research infrastructure (those are closed audit trails).

**Driver protocol:**
1. Build VacuumEngine3D at N=24 (matches registered Phase 5 config)
2. Find a candidate A-B bond near center
3. Seed Beltrami-bound-pair ansatz at bond endpoints:
   - At A: Cosserat ω = -√2·p̂_bond + (2,3) hedgehog envelope (LH chirality, sub-saturation)
   - At B: Cosserat ω = +√2·p̂_bond + (2,3) hedgehog envelope (RH chirality)
   - K4: Φ_link[A→B] = Φ_critical, Φ_link[B→A] = -Φ_critical (matching gate's post-firing injection)
   - V_inc: phase-quadrature seed at modest amplitude (`initialize_quadrature_2_3_eigenmode` at V_amp ≈ 0.05·V_SNAP)
4. Project omega onto saturation manifold so peak|ω| = 0.3π by construction
5. Apply autoresonant drive at amp=0.5·V_SNAP for ~15 Compton periods
6. Stop drive; observe:
   - Did `_nucleated_bonds` register the seeded bond? (If yes, gate self-consistency check)
   - What's max A²_μ during drive? (If approaches 0.95, threshold-chase question gets data)
   - Post-drive peak|ω| and Φ_link[A→B] magnitudes
   - Topology preservation (c_cos via `engine.cos.extract_crossing_count()`)

**Driver outputs (per registered Phase 5 prediction `P_phase5_nucleation`):**
- Per-step gate firing log
- A²_μ trajectory at A and B
- Φ_link[A→B] post-drive vs initial (persistence ratio)
- Topology trajectory c_cos(t)
- (R, r) of seeded pair shell vs Golden Torus geometry

**Run wall time:** ~1-3 minutes at N=24, ~50 Compton-period total run.

---

## 6. What this resolves and what stays open

**Resolves (this session):**
- (α) Gate mechanism validation: does PairNucleationGate fire under ansatz seed when C1∧C2 satisfied by construction? (Validates gate logic separately from threshold-chase)
- (β) Kelvin topological-protection: does the seeded pair persist post-drive? (Tests Bingham-plastic framing claim empirically)
- Methodology bridge: Round 6 finding applied to pair-nucleation context with a concrete driver run

**Pre-empts (Round 5 R5.10 Readings 1-4):**
- The four C2-interpretation Readings become moot if (α) shows the gate mechanism works under explicit threshold satisfaction. The C2 reading question is about INTERPRETATION of an ambiguous threshold; if the gate fires correctly under unambiguous (because seeded) thresholds, the interpretation question is at the C1/C2 LOGIC level, not the Reading level.

**Stays open:**
- (γ) C1/C2 threshold reach under drive at registered config (N=24, amp=0.5·V_SNAP) — original Phase 5 question. Pre-Round-6 answer: NO. Post-(α)+(β) work, this becomes a parameter-sweep question (try larger N, higher amplitude, longer drive) with a validated gate as the diagnostic.
- A31 — F17-K Phase 6 sparse eigensolver methodology — Round 7 Stage 1, fresh session.
- Flag 62-A first-law closure (orthogonal).
- Flag 65-A WKB vs dimensional Γ at horizon (non-blocking).

---

## 7. Empirical run result + adjudication — case (b) with G-13 implication

[`phase5_ansatz_seeded_nucleation.py`](../../src/scripts/vol_1_foundations/phase5_ansatz_seeded_nucleation.py) ran at registered config (N=24, amp=0.5·V_SNAP, λ=3.5, head-on autoresonant collision). Seeded Beltrami-bound-pair at central A=(10,10,10), B=(11,11,11), port 0; bond marked already-nucleated.

### 7.1 Drive-on result

```
                seed         drive-end       post-drive
|ω|_A           1.414        0.013 (0.01×)   0.091 (0.06×)
|ω|_B           1.414        0.013 (0.01×)   0.091 (0.06×)
Φ_link[A→B]    +1.000       +0.998 (1.00×)  +1.000 (1.00×)
peak|ω|_global                               0.091
peak|V|_global                               0.003
c_cos                                        1
E_cos                                        1.89
Other-bond firings during drive: 0           [no cascade]
```

**Verdict: case (b) — seeded pair dissolves during drive.** Cosserat ω at A,B collapses 99% during drive duration (1.414 → 0.013 = 0.01×). |ω|_A,B never recovers post-drive (0.06× of seed). Φ_link reads constant 1.000 throughout.

### 7.2 No-drive sanity check

To distinguish drive-induced dissolution from intrinsic seed-instability, ran the same seed with **no drive at all** (just engine.step() after seeding):

```
step 0  (seed):  |ω|_A = 1.4142   Φ_link = +1.000
step 1:          |ω|_A = 0.1023   Φ_link = +1.000   [93% loss in ONE step]
step 5:          |ω|_A = 0.8495   Φ_link = +1.000
step 10:         |ω|_A = 0.0535   Φ_link = +1.000
step 20:         |ω|_A = 0.1896   Φ_link = +1.000
step 50:         |ω|_A = 0.0958   Φ_link = +1.000
step 100:        |ω|_A = 0.1688   Φ_link = +1.000
```

|ω|_A drops 93% in ONE Velocity-Verlet step, then oscillates chaotically between 0.05-0.85 — NEVER recovers seed value. **The dissolution is intrinsic to engine self-dynamics; drive is irrelevant.** The point-rotation Beltrami is not a stationary state of Cosserat self-dynamics.

### 7.3 Two findings

**Finding A: Gate's `_inject_pair` profile is fundamentally unstable.** Point-rotation Beltrami (single ω vector at A,B + Φ_link) is not a topologically-protected configuration. Velocity-Verlet kick step alone scatters 93% of the seeded ω in one step, regardless of drive presence. The configuration has no mechanism to maintain its localized ω structure — Cosserat self-terms (k_op10, k_hopf, k_refl auto-suppressed under A28) don't stabilize unprotected localized rotation.

**Finding B: Φ_link "persistence" is a measurement artifact.** Φ_link reads exactly +1.000 throughout drive AND no-drive runs. Per A29 (commit `a53ce1c` doc 67_ §17-§18, doc 70_ §1 ref): Φ_link is a derived flux observable in K4-TLM, not a primary dynamical state. Direct seeding leaves a value that doesn't couple to V_inc evolution. The constancy is "nothing in the K4 dynamics is touching this slot" — NOT "Kelvin topological-protection at work."

### 7.4 Adjudication implications

The plan's case (b) framing was "C1/C2 logic itself needs revision (R5.10 Readings reopen at threshold-revision level)." The actual finding is more specific:

**Case (b'): the gate's INJECTION PROFILE needs upgrade, not the C1/C2 threshold logic.** This empirically activates **VACUUM_ENGINE_MANUAL §9 G-13** — a contingency flagged at PairNucleationGate landing:

> "if Beltrami pair dissipates faster than 10 Compton periods post-drive-shutoff (pre-registered P_phase5_nucleation), upgrade to localized Hopf fibration or (2,3) torus-knot injection."

The pre-Round-6 plan deferred this upgrade behind "test point-rotation first." Phase 5 ansatz-seeded driver tested point-rotation directly (no drive-threshold-chase confound) and **falsified Kelvin protection at this injection profile**: dissolution timescale ~1 step, far shorter than 10 Compton periods.

**Connection to F17-K Round 6 finding (consistent):** dynamics don't stabilize topology; topology must be encoded as a persistent structural feature (ansatz). Round 6 showed this for the (2,3) electron eigenmode (Cosserat ω hedgehog dissolves after ~step 11 ~ 2 Compton periods). Phase 5 ansatz-seeded shows the same physics at the pair scale — point-rotation Beltrami dissolves in 1 step. **Same root cause: Cosserat self-terms don't stabilize unprotected localized ω configurations.**

### 7.5 What this resolves and what stays open

**Resolved:**
- ✓ Gate `_inject_pair` profile (point-rotation Beltrami + Φ_link) is fundamentally unstable under engine dynamics (G-13 contingency activated empirically)
- ✓ Φ_link "persistence" disambiguated as measurement artifact, NOT physical Kelvin protection
- ✓ Round 6 finding extends to pair scale — point-component seeds don't stabilize either
- ✓ Phase 5 mechanism question is at the INJECTION-PROFILE level, not the threshold level

**Stays open:**
- (γ) C1/C2 threshold-reach question — unaffected by this finding; gate logic might work if injection profile is upgraded to Hopf or (2,3) topology
- **R5.10 Readings 1-4 — two-level status (clarification per external audit 2026-04-25):**
  - **PRE-EMPTED at original Round 5 framing.** The four Readings (Compton-lock-is-rupture, PLL-chirps-past-lock, drive-health-boolean, parity-chirality-coincidence) argued about how to INTERPRET C2 under ambiguous threshold satisfaction. The ansatz-seed approach made thresholds unambiguous-by-construction, retiring the interpretation debate at this level (this is what §3 / commit `01bbec3` body framing referred to).
  - **MAY REOPEN at threshold-revision level** — a DIFFERENT question at a higher epistemic level — after a topologically-protected injection profile is implemented and tested. Once point-rotation Beltrami is replaced with (2,3) torus-knot or Hopf fibration, the C1/C2 thresholds may need revision to suit the new injection profile (e.g., what saturation level is "sufficient" for Hopf-injection vs Beltrami-injection?). That revision work re-engages parts of the C2 territory but at a different level than the original Reading interpretations (this is what §7.4 / commit `ede4008` body framing referred to).
  - Net: not "dead" but not "pending in original form" either. Two separate questions at two different levels.
- A31 F17-K Phase 6 sparse eigensolver — Round 7 Stage 1 (separate concern; eigensolver is for single-electron eigenmode, not pair injection profile)

### 7.6 Next concrete experiment (Round 7 candidate Stage 2)

Build `phase5_topological_pair_injection.py`: replace point-rotation Beltrami with **(2,3) torus-knot OR Hopf fibration** at each endpoint A, B (chirality-matched: LH at A, RH at B). Test whether topologically-richer ansatz survives Cosserat self-dynamics.

Reuse F17-K + Round 6 infrastructure:
- `cosserat_field_3d.py:initialize_electron_2_3_sector` — (2,3) hedgehog at one endpoint
- `tlm_electron_soliton_eigenmode.py:initialize_quadrature_2_3_eigenmode` — phase-coherent V_inc/V_ref seed
- `coupled_s11_eigenmode.py:_project_omega_to_saturation` — saturation-pin (peak |ω|=0.3π)
- Apply at TWO bond endpoints with opposite chirality

Estimated scope: ~200 LOC new driver. Defer to fresh session (Round 7 Stage 2).

---

*§7 added 2026-04-25 — Phase 5 ansatz-seeded driver result. Case (b'): gate's injection profile (point-rotation Beltrami) is unstable in Cosserat self-dynamics — dissolves 93% in one step regardless of drive. G-13 contingency activated empirically. Φ_link "persistence" is measurement artifact (per A29). Round 6 finding extends to pair scale: topology must be encoded as persistent structural feature, not single-component injection. Round 7 Stage 2 candidate: topologically-protected (2,3)/Hopf injection profile.*

*Doc 70_ added 2026-04-25 — Phase 5 pair-nucleation work resumes per Round 6 closure. Ansatz-initialization methodology applied at pair scale via §7 driver run. Case (b) outcome empirically motivates VACUUM_ENGINE_MANUAL §9 G-13 injection-profile upgrade. F17-K Phase 6 sparse eigensolver remains Round 7 Stage 1; topological-pair-injection becomes Round 7 Stage 2 candidate.*
