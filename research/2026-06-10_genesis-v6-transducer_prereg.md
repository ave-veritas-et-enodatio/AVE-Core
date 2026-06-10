# PREREG — Genesis-v6: the CHIRAL-BOUNDARY TRANSDUCER + the self-limiting snap + the pump fix (PHASE 1 = HYGIENE)

**Date (frozen):** 2026-06-10
**Branch:** `analysis/2026-06-10-genesis-v6-transducer` (worktree `/tmp/ave-v6`, off `analysis/2026-06-10-genesis-v5-seeded-snap` @ `93da170e`; do NOT push/merge — the orchestrator PRs at the end only)
**Engine lineage (subclassed, inherited physics unchanged BY DEFAULT):** `UnifiedGenesisEngine` (`src/ave/core/unified_genesis_engine.py`) ← `CrystalGraftV4` ← V3 ← V2 ← `CrystalEngine`. Every v6 engine addition is behind a NEW parameter that DEFAULTS to the v5 byte-identical path (the existing snap-machine smoke ladder `src/tests/test_unified_snap_machine.py` must stay green).
**Governing discipline:** `ave-apparatus-floor-attribution v1.1` (ORDERED BINS — floor-check gates every positive; PROBE-CAPABILITY — every discriminating probe validated on a known-different reference with a keeper unit test; every new knob inventoried + swept). **§210-COMPLIANCE GATE: the run phase executes every sweep this prereg mandates, or states the deviation explicitly BEFORE running and re-bins. A positive whose governing knob was unswept is CLIP by this prereg's own law.**
**Skills fired at design time:** `substrate-native-check` (CP1/CP2/CP9/CP10 walked §1), `ave-conserved-vs-pumped` (the vent kick is a PUMP into standing-V — the Class-C detonation; the absorbed mode restores energize-lock — §3.D11), `ave-apparatus-floor-attribution v1.1` (governing; the floors §2, the swept knobs §4), `ave-representation-capability-check v1.1` incl. (C) conservation-by-channel (which energy functional is the master-equation invariant — §1 CP2), `phase-space-coordinate-check` (the D9 transducer's helicity-exchange is read in the photon-helicity / bulk-ω channels — PHASE 2), `ave-driver-script-honesty` (every number below comes FROM the evolved field / the dumped JSON), `verify-before-cite` (every v5 anchor grep-confirmed), `flag-don't-fix` (the v5 SNAP-LOCKED demotion is INHERITED, not re-litigated; this prereg adjudicates it formally — §5).

---

## 0. INHERITED VERDICTS (from the adjudicated v5 panel ruling, recorded verbatim-class — `research/2026-06-10_genesis-v5-seeded-snap_result.md` 🔴 ADDENDUM @ `93da170e`)

- **NOT-ELECTRON (T1 detonates) — STANDS.** v6 does NOT reopen the electron claim; it builds the missing primitive (the transducer) and fixes the two hygiene blockers (the pump, the deflagration) that gate any future T1 retest.
- **D-PERM = THE MOTION-LOCK — CONFIRMED.** Permanence = conserved circulation + losslessness (`L_bulk` drive-off ratio 0.97–0.99 ALL arms incl. no-snap; ν_art-INVARIANT across the K1 50× sweep). v6 does NOT ask the snap to hold anything; it asks the circulation to. The snap's certified role is the BIRTH FLASH ONLY (D6: ~160 bursts 3–6 OOM above the known-null floor, onset step 2849).
- **SNAP-LOCKED = UNRESOLVED (construction-dependent).** The v5 "pocket holds under P2" was construction-guaranteed, not measured: `snap_payback_rate=1.0` + `delta_heal=0.0` NEITHER swept; §210 violated (N2 Δ_heal `prereg:198`, K3 stop-time `prereg:206` never run). PHASE-1 JOB 3 runs exactly that sweep.
- **THE TRANSDUCER IS THE MISSING PRIMITIVE (A44: engine coupling-family gap, NOT a missing axiom).** v5 measured the drive's handedness NEVER coupling into the bulk — four arms byte-identical (pocket 5968, ρ_core −0.618, Γ 80.75, L_bulk 139360). The §F named blocking component: "a real photon-helicity → bulk-circulation/ω coupling channel."

## 0.1 THE V6 DESIGN (Grant-ratified from the v5 verdicts; recorded verbatim-class — PHASE 2 is GATED behind PHASE 1)

- **D9 — THE TRANSDUCER (the centerpiece; PHASE 2).** A CHIRAL BOUNDARY CONDITION at the wall/pocket surface: per-bounce spin-orbit exchange — a wave reflecting off the chiral wall exchanges a quantum of angular momentum between the photon's helicity and the trapped ω/bulk circulation (the ADD-2 compression→rotation buckle class; the polar-conjugate mechanism — a chiral mirror torques the angular pair per bounce). CONSERVATION BY CONSTRUCTION: the exchanged L comes FROM the photon (helicity depletes per bounce — bounded, no trilinear bulk potential, no refilled source). HELICITY-ODD; ZERO for achiral drive. CP10: the coupling lives ON the boundary (every bulk-coupling architecture v5-detonated or nulled — no bulk terms).
- **D10 — SELF-LIMITING SNAP (PHASE 1 JOB 2; the deflagration fix).** TWO renderings, both built, swept against each other: **(a) VENT-ABSORBED** — the vented latent goes into a conservative store (removed from dynamics; ledger must close); **(b) MEISSNER-HARDENING** — each snapped cell RAISES neighbors' snap threshold (negative feedback; real condensation nucleates-and-stops). Both must (i) bound E_V on the v5 cascade config AND (ii) preserve single-cell snap + the D6 birth-flash (the known-positive).
- **D11 — THE PUMP FIX (PHASE 1 JOB 1; gate for any T1 retest).** Isolate the v5 +283% H_total source (suspects: GAP-C vent re-injection / drive normalization / snap accounting); fix to ledger-closure above the measured floor BEFORE the genesis arm runs. **If unfixable, the genesis arm does not run (honest block).**
- **D12 — FAIL-FAST ASSERTIONS (PHASE 2 cheap gate).** (i) after the transducer is enabled, RH-drive and LH-drive must NOT be byte-identical within 200 steps (else TRANSDUCER-DEAD: abort the matrix); (ii) the achiral arm shows zero net helicity transfer (the known-null).

---

## 1. SUBSTRATE-NATIVE CHECKPOINTS WALKED (before the first line of v6 numerical code)

- **CP1 (dynamical, no minimization):** unchanged — FDTD leapfrog (V/w/ω) + RK2 (ρ̄/u). No energy-basin descent.
- **CP2 / representation-capability (C) conservation-by-channel — THE LOAD-BEARING CHECK FOR D11.** The master equation is `∂_t²V = c_eff²(V)∇²V`. Its conserved invariant is the c_eff²-weighted energy `½∫(∂_tV)²/c_eff² + ½∫|∇V|²` (`crystal_engine.py:380 bulk_energy_conserved`, docstring: "the honest ledger… NOT the naive ½c0²|∇V|² which the nonlinear breather grows"). The v5 `H_total` used the NAIVE `bulk_energy` (`:354`) — an SM-default (naive-Hamiltonian) leak that OVER-reports the saturated-core breather. D11 reports H_total in the conserved functional. **Prediction frozen: a large fraction of the v5 "+283%" is a wrong-functional measurement artifact; the genuine residual is a separate, smaller term.** (Falsifier: conserved-H pumps just as hard ⇒ the functional is exonerated, the pump is dynamical.)
- **CP9 (dynamical integration, not algebraic):** ρ̄ integrated by continuity; the deficit EMERGES. Unchanged.
- **CP10 (boundary, not bulk):** the snap is a per-cell BOUNDARY state machine. BOTH D10 renderings stay on the boundary — (a) the vent-absorbed store is a snap-ledger scalar (not a bulk source); (b) Meissner hardening is a per-cell THRESHOLD field modification (not a bulk force/potential). No bulk term is added (the v5 detonation lesson).

---

## 2. FLOORS (ORDERED BINS — floor-check FIRST, gates every positive; ave-apparatus-floor-attribution v1.1)

- **F-CLOSE (the D11 pump gate) — the conservation canary.** Measured on a KNOWN-NULL: a no-snap, drive-off run over the persistence window; the floor = the max POSITIVE fractional excursion `max_t ΔH_total^cons/H` it shows (the free PML/numeric drift). **GATE: post-fix, the MAIN-config drive-off H_total^cons must show NO positive excursion above F-CLOSE** (a dissipative residual is physical and ALLOWED — a snapped void + open PML boundary is a one-way sink; only NET CREATION is the pump). A residual that is a SINK at the floor sign passes; a SOURCE above the floor fails.
- **F-EV (the D10 deflagration gate).** The quiet-build dilatation added-mass level `E_V ≈ 13` (v5 plateau, steps 200–2800). DEFLAGRATION = `E_V` rising ≥ 10× above F-EV by run-end. **GATE: each D10 rendering keeps `E_V` bounded (< 10× F-EV) on the v5 cascade config.**
- **F-BURST (the D6 known-positive; inherited F0d).** The longitudinal-burst floor = the free-run (excited, no-snap) scatter of the bulk pressure-integral (`longitudinal_burst_detector.py:54 calibrate_floor`). **GATE: each D10 rendering must PRESERVE a single-cell snap + a burst clearing F-BURST×3** (the birth flash survives the deflagration fix — a fix that kills the flash is over-corrected).
- **F-PROBE (PROBE-CAPABILITY, keeper unit tests).** Each new discriminating probe is validated on a known-DIFFERENT reference: the de-double-count probe verified against the legacy double-count (latent collapses if the shock-KE was double-booked); the Meissner probe verified that `meissner_harden=0` reproduces the legacy cascade byte-for-byte. Encoded as `src/tests/test_unified_snap_machine_v6.py` keeper tests.

---

## 3. PHASE 1 — THE THREE HYGIENE JOBS (each a separate commit; the prereg is committed ALONE first)

**JOB 1 — D11 PUMP ISOLATION + FIX.** Instrument the v5 MAIN-config build H_total per recording step (component-split: E_V naive + E_V conserved, shear, ω, coupling, bulk-KE, bulk-U, + the snap/vent ledgers). BISECT the three suspects by switching each OFF: GAP-C vent (kick→sink), the deep seed (on/off), the snap machine (on/off); AND the energy functional (naive vs conserved). NAME the mechanism with evidence. FIX it. Demonstrate post-fix MAIN-config DRIVE-OFF ledger closure vs F-CLOSE. (ave-conserved-vs-pumped: the suspected mechanism — a vent ∂_tV kick into the deep-saturated seed — is precisely the forbidden CW pump into the standing-V; the fix returns it to a conservative store.)

**JOB 2 — D10 SELF-LIMITING SNAP (both renderings).** Implement (a) VENT-ABSORBED (the conservative store; = the D11 fix generalized) and (b) MEISSNER-HARDENING (per-cell threshold field, hardening increment SWEPT). On the v5 cascade config, demonstrate EACH bounds `E_V` (< F-EV×10) AND preserves the single-cell snap + D6 birth-flash (clears F-BURST×3). Report the cascade behavior (pocket-vs-t) of each.

**JOB 3 — SNAP-CHANNEL ADJUDICATION SWEEP (Rule-11-safe).** On the v5 artifacts/config, the pocket-persistence-under-P2 claim vs the grid `Δ_heal × snap_payback_rate × K3 stop-time` (the two §210-skipped knobs + the stop-time). VERDICT: the v5 SNAP-LOCKED claim is PHYSICS (pocket-persistence invariant across the grid) / CLIP (tracks the knobs) / MIXED. This adjudicates the LOCK claim ONLY (the electron claim is closed NOT-ELECTRON — Rule 11).

---

## 4. APPARATUS INVENTORY — the v6 CLIP suspects (every new knob inventoried + swept; §210)

| knob | sweep (PHASE 1) | CLIP telltale |
|---|---|---|
| `vent_mode` ∈ {kick, absorbed} | JOB 1 bisect + JOB 2 rendering (a) | the pump tracks `kick` |
| seed on/off, snap on/off | JOB 1 bisect | the pump tracks the seed / the snap cascade |
| energy functional ∈ {naive, conserved} | JOB 1 bisect | the "+283%" tracks the wrong functional |
| `snap_accounting` ∈ {legacy, conservative} | JOB 1 fix | the held-latent tracks the double-count (latent → ~0 under de-double-count) |
| `meissner_harden` (hardening increment) | JOB 2 sweep {0, …} | the bounded pocket tracks the increment (expected — it is the control parameter; reported, not hidden) |
| **N2 `Δ_heal`** (re-entry width) | **JOB 3 sweep** (the §210-skipped knob) | pocket-persistence tracks Δ_heal (built-in irreversibility) |
| **`snap_payback_rate`** | **JOB 3 sweep** (the §210-pinned knob) | pocket-persistence tracks payback (pinned-at-1.0 was the construction) |
| **K3 stop-time** | **JOB 3 sweep** | the "converged" pocket value tracks stop-time (the graft-v4 stop-time lesson; the pocket GREW +27% under P1 in v5) |

---

## 5. CORPUS STATE + ADJUDICATION DISCIPLINE

- **OPEN.** PHASE 1 is hygiene: it does NOT promote any candidate-claim. The NOT-ELECTRON verdict is unchanged. The pump-fix and deflagration-fix are engine-hygiene; the snap-channel sweep formally resolves the v5 UNRESOLVED bin.
- **Rule 11:** JOB 3 adjudicates the LOCK, not the electron. A CLIP verdict is the discipline working (the v5 demotion was correct); a PHYSICS verdict is a new positive worth its own tracked entry; MIXED is reported honestly with the invariant-vs-tracking split named.
- **Rule 12:** the v5 SNAP-LOCKED slot already carries its 🔴 demotion; this prereg does NOT refill it — JOB 3 either confirms UNRESOLVED→CLIP or promotes a NEW (sweep-backed) positive with its own verification chain.
- **The auditor lands the manual entry; this prereg + the JOB results SURFACE the empirical finding only.**
