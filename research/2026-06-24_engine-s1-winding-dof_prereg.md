# S1 — The (2,3) Winding as a Separately-Conserved DOF: Dynamical Winding-Conservation Gate

**Status:** **FROZEN PRE-REG** (orchestrator-finalized; the three Grant forks are RULED, see §7). Frozen pre-run — the falsifier below is fixed before any build executes.
**Date:** 2026-06-24
**Epic:** AVE engine RE-ROUTE (post Stage-2 bulk-self-trap FALSIFICATION, PRs #403→#404 merged; electron localization re-routed to BOUNDARY/TOPOLOGICAL).
**Pathway parent:** `_orchestration/2026-06-24_engine-reroute-pathway.md` (S1 row, pathway:58).
**Supersedes:** nothing (new gate). **Does NOT touch:** mass=A1 (PR#260, UNTOUCHED).
**Provenance:** all file:line grep-confirmed at `b33b3299` (PR#405 merged, clean tree). Re-pin the pathway-doc footer SHA when S1 lands.

---

## 0. SCOPE-LOCK + the ruled configuration

S1 is launched with the following configuration (Grant go, 2026-06-24; forks ruled in §7):
- **Coordinate category = real-space Cosserat ω-grade.** Charge = the Beltrami helicity `H_bel = ∫ ω·(∇×ω)`. RATIONALE (load-bearing): the phase-space `(V_inc, V_ref)` Clifford torus is the **mass-breather's own portrait** — `V_ref` is a *read-only projection of the same scalar `V`* (master-equation.md:20), so that torus is NOT an independent DOF and CANNOT host the "separately-conserved" winding S1 needs. The real-space `ω` field is the only genuinely independent DOF (own field + own momentum `I_ω·ω̇`, cosserat_field_3d.py:934,948). So the independent charge necessarily lives in real-space `ω`.
- **Channel = intra-Cosserat ω↔ω.** The make-or-break is **single-knot conservation under genuine evolution + a local winding-current continuity law**. Literal two-soliton transfer is **DEFERRED** (V/EM is dead by grade-orthogonality; two stable, separated electrons do not overlap their ω-fields to hop; transfer is meaningful only in a pair-creation / reconnection process — a later stage, not S1).
- **Classification = CONSISTENCY gate** (asserted-CLASS → derived-REAL upgrade), NOT the α-free chord (that is S4). **The Q=137 slot stays EMPTY** (gate `wmighcz1z`). S1 must NOT pre-contaminate S4.

Standing constraints (inherited, load-bearing):
- **genesis-24 guard:** the winding gets its OWN field/momentum/LC; NEVER wired into / read off the A1 `(V_inc, V_ref)` phasor (master-equation.md:20). Doing so self-inflicts the `w_pol = 0` double-count.
- **coordinate-category (A46):** spin-½ (real-space 720° SU(2) on the unknot BODY) ≠ the (2,3) winding (the charge). TWO different "2"s; never conflate ((2)×(2)=4 trap).
- **α-clean host:** `src/tests/engine_acceptance/_winding_host.py` (κ̃=6/5; selective import :56-61; live `assert 'ALPHA' not in globals()` :69). The α-AWARE `src/ave/topological/cosserat_field_3d.py` imports `ALPHA` (:56) + `KAPPA_CHIRAL_ELECTRON = ALPHA·κ̃` (:131) + golden-torus Q (:2422) — FORBIDDEN on the chord-deciding path. `k4_cosserat_coupling.py:73` imports `KAPPA_CHIRAL_ELECTRON`; `crystal_graft_v4_run.py:34` imports `ALPHA_COLD_INV, PHI` — reuse v4 for STRUCTURAL arms only; keep α off the readout.

---

## 1. WHAT S1 ACTUALLY IS (refute-by-default verification of the framing)

The pathway's structural premise is **VERIFIED ACCURATE** (grep-confirmed @ b33b3299):
- The (2,3) winding is **currently only a STATIC real-space holonomy SIGN + a static linking integer** read off the Cosserat ω micro-rotation field; it has **NO own field/momentum/LC across engine steps**. Engine state is `(u, omega, u_dot, omega_dot)` only (cosserat_field_3d.py:910-918); `step()` (:2022) is a bulk-Lagrangian velocity-Verlet with no winding field/transfer term.
- Coupled-engine ruling **S6=A: "Q conservation Soft/diagnostic only … Q measured, not enforced"** (k4_cosserat_coupling.py:16-17,21).
- **`winding` is an UNBUILT chord-DOF** at the L3-L5 rungs (engine-capability-map.md:46).
- "A1-sustains-rotation" is currently a **CLASS (asserted)**, not REAL (derived). S1 is the upgrade.

**THREE corrections to the pathway's secondary framing (refute-by-default surfaced these):**
1. **S1 is TWO sub-claims, not one** — single-knot conservation (the S1 make-or-break, BUILDABLE NOW) vs two-soliton transfer (DEFERRED, see §6).
2. **A PARTIAL winding-transfer mechanism ALREADY EXISTS** — node_circulator_coupling.py (PR#321, device-circuit-models.md:203): bounded, lossless, winding-acting, helicity-TRANSFERRING shear↔bulk coupling, passes CONSERVE/TRANSFER/LOCK-ON-WINDING; ONLY the non-reciprocity MAGNITUDE is imposed (echo). BUT it is a **reduced M=2 complex-amplitude ODE** (`a_bulk, a_shear` scalars, node_circulator_coupling.py:25,170-171), **NOT** the field-resolved engine. Do NOT mis-read as "S1 already built" (anti-substitution).
3. **The conserved quantity the corpus has demonstrated TRANSFERRING is the 0-form CHARGE (= Beltrami helicity), NOT the (2,3) phase-space WINDING.** The corpus keeps these separate (crystal-engine_result.md:210 "carries the CHARGE, not the WINDING"). The ONLY corpus result on the genuine winding side is the **w_pol=0 NEGATIVE** (genesis-v7, SWAMPED/NO-LOCK).

---

## 2. CLASSIFICATION: consistency-vs-emergence

**S1 = CONSISTENCY-class.** It upgrades "A1-sustains-rotation" from asserted-CLASS to derived-REAL by demonstrating the winding is a separately-conserved DOF under dynamical evolution. **It is NOT the α-free CHORD** (that is S4). S1 routes its reads through the α-clean `_winding_host` and must NOT pre-contaminate S4. **The Q=137 slot stays EMPTY.**

---

## 3. THE MAKE-OR-BREAK (pre-stated falsifier — launched config)

S1 PASSES iff, in the **real-space ω-grade** coordinate (ruled) and on the **α-clean carrier** (κ̃=6/5; NEVER `KAPPA_CHIRAL`/`V_SNAP`/`L_NODE`/`M_E` on the readout), under the engine's **ACTUAL `step()`** (NOT static `deform_continuous`), ALL of (a)-(c),(e),(f) hold:

- **(a) NON-VACUITY** — ω genuinely evolved under its OWN wave equation (`a_omega = c_omega^2*laplacian(omega) - omega_gap^2*omega`, crystal_graft_v4.py:240-241) with its own `I_omega*omega_dot` momentum; gated by `real_dynamics_ran` (crystal_graft_v4_run.py:202). Frozen-field "conservation" = AUTO-FAIL.
- **(b) KNOWN-SIGNAL RECOVERY** — the extractor recovers a known-imposed (2,3) integer first (`seed_omega_known_2_3`; `compute_Q_link` returns Q_link=3). "An extractor that cannot see a known-imposed (2,3) cannot certify its absence."
- **(c) CONSERVATION-UNDER-EVOLUTION + LOCAL CONTINUITY** — the total winding integer is conserved across N steps to a pre-stated drift tolerance, measured on the RETAINED RAW float trajectory (`w_pol_raw_list`) with alias canary `alias_frac <= 0.34` (NOT the snapped int alone); AND `|ΔH_bel|/H_bel` below tolerance pre/post the lock substep (`_Hbel_pre_lock/_Hbel_post_lock`, crystal_graft_v4.py:259-262); AND **a local winding-current continuity check** — the interior winding integer changes ONLY via helicity flux through the boundary (`∂_t W + ∇·J_W ≈ 0`; interior non-conservation beyond tolerance, not accounted by the boundary ledger, = FAIL). This is the substrate-native statement of "winding is a conserved current," and it does NOT require a second soliton.
- **(e) LIVE NEGATIVE CONTROL** — a pre-stated lock-OFF arm that DOES pump `|L_omega|` / destroy topology must FIRE (the GX3 analogue). A conservation PASS is vacuous unless this arm can break it.
- **(f) GENESIS-24 POSITIVE CONTROL** — the `slaved_omega` arm (ω := grad(V), crystal_graft_v4.py:280-293) MUST return independence-gate = False (demonstrated-reachable-False, crystal_graft_v4_run.py:209-211). A gate that cannot fail on the slaved arm = AUTO-VOID.

**DEFERRED (NOT an S1 requirement):** (d) two-soliton winding-TRANSFER. Reason: the V/EM transfer channel is dead by grade-orthogonality (cross_sector_pump_result.md:15, V→ω = 7.3e-18 machine-zero) and detonates as an indefinite trilinear (cross_sector_coupling.py:133-135, H_bel −4107) — Rule-12 DO-NOT-REOPEN; and intra-Cosserat carrier-to-carrier hopping requires two ω-fields to overlap/reconnect, which two stable separated electrons do not. Literal transfer is therefore only physical in a pair-creation / reconnection process — a later stage. The S1-equivalent of "winding is a conserved current" is the **local continuity** check in (c), not a two-body hop.

**S1 FAILS** if any of (a)-(c),(e),(f) does not hold. **S1 is INCONCLUSIVE (report, do not rescue — Rule 11)** if the integrator cannot carry the dynamics to a clean verdict (the Stage-2 precedent: explicit stepper went secularly unstable → reported INCONCLUSIVE, did not fake a verdict).

---

## 4. VALIDATE-ON-KNOWN

**PRIMARY (the honest floor):** STATIC planted-integer recovery in `src/ave/topological/charge_quantization.py` — `compute_Q_link` (:257) → `Q_int = int(np.round(Q_link_raw))` (:290) MUST read Q_link=3 on a seeded canonical (2,3); invariance under `deform_continuous` (:378) is the STRUCTURAL-on-planted-winding known-good (GUARD 3 :39-41). **The new dynamical gate MUST reproduce this exact static integer in the frozen limit, THEN show it conserved under `step()`.**

**DO NOT borrow as the (2,3)-winding known-good (coordinate-category traps, A46):**
- the crystal-engine 0-form-CHARGE bootstrap `max|w|=0.975` / parity-odd selection (crystal-engine_result.md:80-81) — that file says ":210 carries the CHARGE, not the WINDING", ":223 the (2,3) WINDING … absent". Using it = the genesis-24 / w_pol=0 double-count the guard exists to prevent.
- the chiral-srs lattice writhe `±0.04087` (chiral-srs-optical-activity_result.md:339) — a REAL-SPACE CRYSTAL-NET pseudoscalar, a different coordinate object from the electron-soliton winding.

**KNOWN-NEGATIVE the gate must OVERCOME (not borrow):** `w_pol = 0` (genesis-v7-quadrature_result.md — full assembly SWAMPED / decoheres 3→1 / NO LOCK) — the canonical demonstration that the isolated LC tank has no nonlinear quantizer to protect a deposited winding. **NOTE:** there is NO existing PASSING test of dynamical (2,3)-winding-integer conservation; the pathway table's S1 validate-on-known column has NO green predecessor; the static planted-integer read is the only recoverable-in-limit floor.

**Resolution-ceiling arithmetic (A47):** charge_quantization.py:61 resolves windings "up to q ~ 4 at this diagnostic scale (2πr/q cells/turn)". Canonical q=3 is safely resolved AT SEED; the S1 dynamical gate MUST re-verify the per-turn cell count stays ≥ ~3-4 cells THROUGHOUT evolution — if the knot stiffens/shrinks under `step()`, q-resolution degrades mid-run and manufactures a false winding-loss. Assert lattice-resolution-held-throughout, or run on a finer lattice.

---

## 5. FALSE-POSITIVE TRAPS + GUARDS (the Stage-2 immune system)

Most of this immune system ALREADY EXISTS in the crystal_graft_v2/v4 lineage — S1's task is PORT-to-α-clean-host + run, **not green-field build** (anti-rebuild, Rule 14).

| # | Trap | Guard (file:line) |
|---|------|-------------------|
| 1 | VACUOUS CONSERVATION (frozen field) | `real_dynamics_ran` flag (crystal_graft_v4_run.py:202); own ω wave eq (crystal_graft_v4.py:240-241) |
| 2 | INTEGER-SNAPPING (rounded float hides drift) | retain raw trajectory `w_pol_raw_list` (fast_winding_extractor.py:255-256) + alias canary `alias_frac<=0.34` (crystal_graft_v4_run.py:102-108) |
| 3 | A1-SLAVING (genesis-24 false-positive) | `slaved_omega` positive-control (crystal_graft_v4.py:103-107,280-293); independence-gate MUST be False (crystal_graft_v4_run.py:209-211) |
| 4 | NO-ACTUAL-CURRENT (trivial static sum) | the local continuity check `∂_t W + ∇·J_W ≈ 0` + the helicity ledger close-by-deficit (crystal_graft_v4.py:350-372) |
| 5 | BOUNDARY-LEAKAGE MASKED | ledger radiated-by-DEFICIT canary (crystal_graft_v4.py:356-372) |
| 6 | VACUOUS HERO-CANARY | **S1 hero-canary = `|ΔH_bel|/H_bel` drift gate** (crystal_graft_v4.py:259-262) WITH live lock-OFF negative control (GX3 analogue) |
| 7 | COORDINATE-CATEGORY MISMATCH (A46, (2)×(2)=4) | coordinate DECLARED real-space ω-grade (charge_quantization GUARD 4 :42-44); the read IS the real-space curl integral — consistent with the ruled scope |
| 8 | ALPHA-RECONTAMINATION | route readout through `_winding_host` (κ̃=6/5; :69 `assert 'ALPHA' not in globals()`); NEVER `KAPPA_CHIRAL`/`V_SNAP`/`L_NODE`/`M_E` |

**The S1 winding/energy canary (the Stage-2 energy-gate analogue):** the Beltrami-helicity drift gate `|ΔH_bel|/H_bel` (H_bel = ∫ ω·(∇×ω); charge=helicity per master-equation.md:20), run pre/post the lock substep, WITH a live lock-OFF negative control AND the slaved positive-control, in the declared real-space coordinate, on the α-clean host. Without all three (fireable canary + positive control + correct coordinate) an S1 PASS is vacuous in exactly the way Stage-2's energy gate was built to prevent.

---

## 6. BUILDABILITY: RULED — SUB-CLAIM A is S1 (buildable now); SUB-CLAIM B deferred

- **SUB-CLAIM A — single-knot conservation (= the S1 make-or-break):** **BUILDABLE NOW**, intra-Cosserat. DOF + momentum/LC exist (cosserat_field_3d.py:934,948); V-free evolution exists (step(), :2022); observable exists (compute_Q_link); trap-immune-system exists (crystal_graft_v2/v4). No TKI, no new field, no genesis-24 violation. Needs: run under step() (not deform_continuous), port readout to α-clean host, real-space coordinate (ruled), add the local continuity check.
- **SUB-CLAIM B — two-soliton TRANSFER:** **DEFERRED** (see §3 (d)). If ever built, intra-Cosserat only; the V/EM route is FALSIFIED (Rule-12 DO-NOT-REOPEN: machine-zero V→ω + indefinite-trilinear detonation).

---

## 7. GRANT FRAMING DECISIONS — RULED (2026-06-24)

- **Fork 1 (channel): RULED → intra-Cosserat ω↔ω, and the S1 make-or-break is single-knot conservation + local continuity (transfer deferred).** The V/EM channel is dead by grade-orthogonality (V→ω = 7.3e-18) and detonates; two stable separated electrons don't overlap ω-fields. "Winding is a conserved current" is properly tested by local continuity, not a two-body hop.
- **Fork 2 (coordinate, A46): RULED → real-space ω-grade.** Decided by physics, not convenience: the phase-space `(V_inc, V_ref)` torus is `V`'s read-only projection (master-equation.md:20) → not an independent DOF → cannot host the separately-conserved winding. The real-space `ω` is the only genuinely independent DOF (own momentum `I_ω·ω̇`). Charge therefore lives in real-space `ω`; the phase-space torus is the mass-breather's portrait.
- **Fork 3 (V-tank DOF): MOOT** (only fired if Fork 2 = phase-space).

**FLAGGED, not banked (candidate for a later stage):** if the soliton is self-consistent, the real-space helicity integer (`∫ ω·∇×ω`) and the phase-space `(2,3)` lock integer must AGREE. That forced agreement is a non-trivial consistency condition — a possible later discriminator. Logged, not claimed.

---

## 8. REPRODUCE / GATE PLAN

1. **Port** the crystal_graft_v2/v4 trap-guard set (slaved_omega, real_dynamics_ran, alias canary, H_bel pre/post-lock, helicity ledger) onto `_winding_host` (κ̃=6/5; verify `assert 'ALPHA' not in globals()` holds on the readout path).
2. **Seed** a known (2,3) (`seed_omega_known_2_3`, p=2,q=3); confirm `compute_Q_link` reads Q_link=3 (validate-on-known floor, §4).
3. **Frozen limit:** confirm the dynamical gate reproduces the static integer with no evolution.
4. **Evolve** under `step()` for N steps; assert (a) `real_dynamics_ran` True; (b) `|ΔH_bel|/H_bel` < tol on the raw trajectory; (c) `alias_frac <= 0.34`; (c') local continuity `∂_t W + ∇·J_W ≈ 0` (interior change accounted by boundary flux); (d) lattice-resolution ≥ ~3-4 cells/turn held throughout.
5. **Negative control:** lock-OFF arm pumps `|L_omega|` / breaks topology (canary FIRES).
6. **Positive control:** `slaved_omega` arm returns independence-gate = False.
7. **(DEFERRED)** two-soliton transfer — not built in S1.
8. **CI / cross-tree discipline:** SHA-pin the result to HEAD; record the axiom-chain (charge = Beltrami helicity, master-equation.md:20) in the solver docstring; gate the conservation tolerance in CI. Re-pin the pathway-doc footer SHA when S1 lands. **NEVER self-merge** — branch only; Grant merges.

**Conservative caveats (do NOT over-claim):**
- S1 is CONSISTENCY-class, NOT the α-free chord. The Q=137 slot stays EMPTY.
- "A1-sustains-rotation" is currently asserted-CLASS; an S1 PASS upgrades it to derived-REAL ONLY for the declared (real-space ω) coordinate and the single-knot conservation claim — not globally, and not for transfer.
- No existing PASSING test of dynamical (2,3)-winding conservation exists to recover in a limit; the static planted-integer read is the only floor.
- mass=A1 (PR#260) is RATIFIED-CONSISTENCY; S1 does NOT touch it.
