# S2 — `H_couple` locking A1↔ω conservatively (winding stays independent)

**Status:** **FROZEN PRE-REG** (orchestrator-finalized; both forks RULED — see §RULED forks). Frozen pre-run.
**Date:** 2026-06-24
**Epic:** AVE engine RE-ROUTE (`_orchestration/2026-06-24_engine-reroute-pathway.md`, S2 row :59).
**Checkout/provenance:** AVE-Core @ `origin/main 1d4eae9c` (PR#407 merged, S1 landed). All file:line citations re-verified at this HEAD on freeze-day.
**Supersedes:** nothing.
**Class:** CONSISTENCY-class. **S2 is NOT the α-free chord** (the chord-decider is S4). A green S2 must NOT be narrated as the chord.
**Scope-lock:** S2 tests ONLY whether a conservative skew-Hermitian `H_couple` locks the A1 bulk-dilatation breather (mass) to the Cosserat micro-rotation winding (charge) on the SAME nodes *without leaking* and *keeping ω an independent DOF*. It does NOT test confinement (S3), boundary observables (S4), or the non-reciprocity MAGNITUDE (corpus-flagged ECHO).

## Ruled configuration (Grant go, 2026-06-24)
- **FORK A = (a) intra-mechanical saturation-front.** `H_couple` lives in the bulk(A1)↔shear(ω) pair, gated by the saturation front `S(A)`; **NO TKI transducer.** Rationale (Grant's saturation-port question + grounding): the cutoff energy at a saturating node is handled *reactively* — the `S(A)`-gated reactance modulation IS the coupling port (the same varactor knob as gravity); the kernel has no internal sink (`saturation.py`, all reactive), and the EM/V route is dead + Rule-12 DO-NOT-REOPEN (`V→ω = 7.3e-18`, `cross-sector-pump-confirmation_result.md:15,67`). Confirmed operative: `cross_sector_coupling.py:76` `H_couple = κ̃∫ g V Ω_w` gated by `saturation_front_window g(A)`; `device-circuit-models.md:207` puts bulk↔shear WITHIN one mechanical domain.
- **FORK B = (b) own-conserved-DOF, not-slaved, splitting EXPECTED.** Independence = ω keeps its OWN conserved winding integer + own field/momentum/LC and is NOT slaved to A1 — NOT zero-frequency-shift. Rationale (physics, not taste): any norm-preserving coupling that *transfers* MUST normal-mode-split (resonant split = `2·Ω` exactly; `node_circulator_coupling.py:124-157`); horn (a) "zero eigenfrequency shift" is UNSATISFIABLE for any real transferring coupling and would make S2 a guaranteed FAIL. Frequency-pull is the `S(A)` modulation working — the same modulation that, with a spatial gradient, *is* gravity. Independence is operationalized by the S1 reachable-False slaved-arm discriminator.

## Physical frame
Post-Stage-2 composition picture: mass = A1 (longitudinal dilatation breather, disperses alone — Stage-2 falsified) and charge = ω (Cosserat micro-rotation winding) live on the same nodes. The post-Stage-2 MUTUAL-PINNING hypothesis is that the charge topology pins the dispersing A1 core. S2 audits the conservative coupling `H_couple` that locks A1↔ω WITHOUT leaking, keeping ω independent. S2 does NOT itself prove pinning — it proves the COUPLING is conservative + non-vacuous + independence-preserving (the prerequisite for the pinning test in S3).

**Ontology note (Grant 2026-06-24, label-independent):** from the vacuum's standpoint the "real-space ω director-phase" coordinate is the spatial profile of one component of the vacuum's *state* (its phase configuration), and 3D space is the base it is indexed over. This is a clarifying relabel — the S2 conservation/independence reads are well-defined on the DECLARED cut regardless of ontological label, exactly as S1's were. Orthogonal to the build.

## Make-or-break (pre-stated falsifier)
A **field-resolved** skew-Hermitian (anti-Hermitian-by-construction) `H_couple` in the A1↔ω sector pair, on the α-clean host, gated by `S(A)` (FORK A=(a)), PASSES iff ALL hold against the thresholds below; FAIL on any one ⇒ S2 falsified. INCONCLUSIVE is a legit landing (Rule 11) if the integrator can't carry it cleanly — do NOT rescue.
1. **CONSERVATION.** Joint `H = E_A1 + E_ω + H_couple` drifts `|dH/H| < 1e-8` over a long closed-system window (precedent `test_l1_photon.py:285`). Strict precedent target: the PR#321 reduced generator already meets `norm_drift ≈ 1.1e-12`.
2. **NON-VACUITY (load-bearing).** The coupling TRANSFERS: `a_shear`/ω starts EMPTY and fills measurably (the bounded-inert ~2% arm of `cross_sector_coupling.py`, `photon_deplete=False`, FAILS this) AND the `|L_ω|` pump canary stays BOUNDED (`spin_L_omega`, `crystal_graft_v2.py:300-302`).
3. **INDEPENDENCE (FORK B=(b)).** ω keeps its OWN conserved winding integer `(w_tor, w_pol)` robust under a V-perturbation on the REAL arm, while the SLAVED arm (ω := F(V)) returns independence = False (`s1_winding_conservation_gate.py:439`, reachable-False / `AUTO_VOID`). **Normal-mode splitting of the eigenfrequency is DECLARED EXPECTED + bounded — NOT a violation.**
4. **REDUCED-LIMIT.** `H_couple` recovers the 2-mode circulator generator (`node_circulator_coupling.py:124-157`) in its 2-mode limit.

No TKI-transducer precondition gate (FORK A=(a) intra-mechanical). The Q=137 slot stays EMPTY.

## Validate-on-known (recover-in-limit)
- **Primary target:** `src/scripts/vol_9_device/node_circulator_coupling.py:124-157` (`circulator_generator`); exact-unitary propagator `:160-165`; in-driver hard gate `:664-689`. Conservation EXACT by construction (`:30-32`). Reproduced live @ `1d4eae9c`: Gate-A `norm_drift = 1.128e-12` / 40k steps.
- **DUAL-canary precedents (reuse, do not re-derive):** (i) `|dH/H| < 1e-8` — `test_l1_photon.py:285`; (ii) `|L_ω|` pump canary — `crystal_graft_v2.py:300-302`, reachable-FAIL shown by S1's live negative control (`research/2026-06-24_engine-s1-winding-dof_result.md:26`, lock-OFF pumps 9.5×).
- **Independence discriminator precedent:** `s1_winding_conservation_gate.py:403-405,439`.
- **Closest FIELD-RESOLVED conserving precedent — FORM only, WRONG sector pair:** `crystal_engine.py:222-250` (ADD-2, conserves `E_V + E_w + H_couple`) couples bulk↔shear-DISPLACEMENT (V↔w), NOT bulk↔Cosserat-ω. Recovering it does NOT count as recovering S2.
- **NOTE (anti-substitution):** the PR#321 generator is a reduced 2-mode complex-amplitude ODE, NOT the field-resolved engine — S2 must BUILD the field-resolved A1↔ω coupling and recover the ODE in its limit (genuine new work, like S1).

## False-positive traps + guards (the immune system)
The **S2 dual canary** = `|dH/H| < 1e-8` (conservation) AND `|L_ω|` pump-bounded (non-detonation), each with a demonstrated reachable-FAIL on a negative control in the SAME harness.
- **T1 VACUOUS-CONSERVATION** — unitary conserves by construction. *Guard:* require the MEASURED transfer gate (criterion 2); the ~2% inert arm FAILS it.
- **T2 CONSERVED-BY-DAMPING** — a loss-port hides a leak. *Guard:* ledger on a CLOSED system (GATE2/GATE4 closed-port Hermitian); do NOT route through the bare matched loss-port (`graded_vacuum_network.py:209-217`, explicitly NOT a transducer).
- **T3 INDEPENDENT-BY-DECOUPLING** — uncoupled V,ω ⇒ vacuous robustness. *Guard:* probe on the COUPLED arm (`lock_on=True`); require `real_dynamics_ran=True` (`s1_...:411-413`).
- **T4 SLAVING / genesis-24 collapse** — ω := F(V). *Guard:* slaved arm MUST return independence = False; can't-fail ⇒ `AUTO_VOID` (`s1_...:398-440`).
- **T5 DETONATION** — the indefinite trilinear `H = κ̃∫ g V [w·(∇×ω)]`, `photon_deplete=True`, unbounded-below, H_bel −4107. *Guard:* stay on the skew-Hermitian path; NEVER set `photon_deplete=True` (`cross_sector_coupling.py:130-141`); `|L_ω|` is the live detonation detector.
- **T6 DUAL-CANARY UNFIREABILITY** — both canaries pass-only ⇒ decorative. *Guard:* ship the negative controls; each leg must demonstrate reachable-FAIL.
- **T7 ANTI-SUBSTITUTION** — re-using the PR#321 2-mode ODE as the deliverable. *Guard:* S2 is field-resolved and RECOVERS the ODE in its limit.
- **WRONG-SECTOR-PAIR** — recovering ADD-2 (V↔w). *Guard:* S2 target is A1↔Cosserat-ω; `a_shear` = LOCAL (ω,π_ω) LC quadrature (`node_circulator_coupling.py:43-46`).
- **FORK-B FALSE-VIOLATION** — scoring normal-mode splitting as a violation. *Guard (RULED B=(b)):* splitting EXPECTED + bounded; independence = winding-integer + slaved-arm-False, NOT frequency-invariance.

## Genesis-24 / coupling guard
ω stays a SEPARATE DOF by owning its field/momentum/LC, NEVER wired into / read off the A1 `(V_inc, V_ref)` phasor (`master-equation.md:20`). The charge "3" lives in the LOCAL `(ω, π_ω)` LC quadrature — a zero-net-L pattern, SEPARABLE from the A1 dilatation mode (`crystal_graft_v4.py:46-48`) and distinct from the orthogonal global rigid rotation `L_ω`. `H_couple` is a SKEW off-diagonal exchanging between two independent stores, its off-diagonal sourced by lattice chirality (a structural phase), NOT by reading ω off V. Enforced by the S1 reachable-False discriminator. Normal-mode splitting does NOT violate this guard (coupled-eigenfrequency vs DOF-ownership are different criteria).

## Buildability verdict
**BUILDABLE-NOW** (forks ruled to the corpus lean): both A1 and ω are elastic mechanical grades ⇒ coupling WITHIN one mechanical domain, NO transducer (`device-circuit-models.md:207`); FORM de-risked on main (PR#321); genesis-24 guard satisfied via the LOCAL LC quadrature; dual canaries + live negative controls exist. The build is a NEW field-resolved skew-Hermitian `H_couple` in the A1↔ω pair (no existing field-resolved coupling in that exact pair — ADD-2 is V↔w). The Q=137 slot stays EMPTY (`device-circuit-models.md:197`).

## α-clean discipline (inherited, load-bearing)
Build on the α-clean host `src/tests/engine_acceptance/_winding_host.py` (κ̃ = 6/5; live `assert 'ALPHA' not in globals()`). FORBIDDEN on the S2 path: `cosserat_field_3d.py` (`ALPHA`, `KAPPA_CHIRAL_ELECTRON = ALPHA·κ̃`), `k4_cosserat_coupling.py`, `crystal_graft_v4_run.py` α-imports — reuse v4 for STRUCTURAL arms only, keep α off the readout. HYGIENE: drop any dead α-routing import on the S2 path so a central-guard grep returns clean.

## Reproduce / gate plan
1. Re-run the validate-on-known target (`node_circulator_coupling.py`) — confirm 4 gates PASS, `norm_drift ≈ 1.1e-12` @ HEAD.
2. Build field-resolved `H_couple` in the A1↔ω pair on the α-clean host, `S(A)`-gated; assert skew-Hermitian (generator anti-Hermitian / propagator Hermitian-H, unitary); evolve closed-system.
3. Gate: criterion 1 (`|dH/H|<1e-8`), criterion 2 (transfer measurable + `|L_ω|` bounded), criterion 3 (real-arm winding-robust + slaved-arm-False/`AUTO_VOID`; splitting allowed), criterion 4 (reduced-limit recovers the 2-mode generator).
4. Ship negative controls: lock-OFF / `photon_deplete=True` arm MUST fire the `|L_ω|` pump; open/lossy arm MUST fire `|dH/H|`. Both canaries demonstrate reachable-FAIL.
5. pytest acceptance test (frozen-bin docstring, Rule 11) + result doc with PASS/FAIL/INCONCLUSIVE verdict. Branch-only; NEVER self-merge (Grant merges).

## Consistency-vs-emergence classification
CONSISTENCY-class. A green S2 demonstrates a substrate-consistent conservative lock; it does NOT emit an AVE-distinct chord. The non-reciprocity magnitude the circulator carries is corpus-flagged ECHO-at-magnitude (`research/2026-06-20_node-circulator-coupling.md:11`, verdict PARTIAL) and is OUT OF SCOPE for S2.

## Corpus-hygiene corrections carried in this pre-reg (auditor flags, applied)
- The `7.3e-18 V→ω machine-zero` is attributed to `cross-sector-pump-confirmation_result.md:15,67` (mechanism: `relu(−Γ)` clamp-gate sector-gating, NOT generic grade-orthogonality); the S1 pre-reg only CITES it.
- The skew-Hermitian / H_bel −4107 framing is anchored to `cross_sector_coupling.py:130-141` + `cage-winding-engine-charter.md:15` (the session run-id `w8rzk9dkt` is NOT a corpus claim-id and is not cited).
