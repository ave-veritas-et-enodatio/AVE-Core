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

---

## 6. PHASE 2 — THE D9 TRANSDUCER SMOKE (THE GATE; this mini-prereg FROZEN before any run artifact)

**Status when frozen:** PHASE 1 hygiene CLOSED (JOB 1 pump-fix PASS @ `fee2ccb6`; JOB 2 both renderings @ `49520541`; JOB 3 snap-channel CLIP @ `e3a4eef8`). The D11 pump-gate is PASS (drive-off H_total^cons monotone non-increasing, max positive excursion 0.0000% ≤ F-CLOSE +0.184%), so PHASE 2 is UNGATED to run. The genesis/T1 arm remains NOT run (NOT-ELECTRON stands); PHASE 2 builds + smokes the missing PRIMITIVE only.

### 6.1 THE D9 OPERATOR (substrate-walked; derivation stated)

A **chiral boundary condition on the wall shell** — the polar-conjugate of the snap reflector. The snap reflects the RADIAL pair (Z_bulk→0); D9 makes the SAME wall **chiral** so it torques the ANGULAR pair per traversal. Substrate-native checkpoints walked before the first line:

- **CP10 boundary-not-bulk (THE load-bearing constraint — every v5 bulk-coupling architecture detonated or nulled):** the exchange acts ONLY on the `_wall_window()` g_wall shell (A≈`wall_center`=R_II, the Γ=−1 saturation front of the planted pocket), interior-masked. It is a per-cell BOUNDARY operation applied in `step()` AFTER the inherited V/w/ω + bulk substeps — NOT a term added to any field's acceleration/EOM. No bulk trilinear potential is introduced (so the indefinite-Hamiltonian pump that detonated `photon_deplete=True` cannot recur).
- **The payer (photon helicity ledger) = the photon's axial mechanical SPIN** `S_φ ≡ ∫ (w × ∂_tw)·n̂ dV` (n̂ = the FOC/drive axis). For a CP shear photon `S_φ ∝ −h·k·∫|w|²` (HELICITY-ODD by construction); for a linear-pol (achiral, helicity=0) photon `w` has one transverse component ⇒ `S_φ ≡ 0` (the achiral null is structural, from the field — not dialed).
- **The recipient (the bulk circulation) = `u_adv` orbital AM** `L_bulk ≡ ∫ ρ̄_full (r×u_adv)·n̂ dV` — the EXACT channel v5 measured as NEVER coupling (four arms byte-identical L_bulk 139360). D9's whole job is to make the photon handedness land here.
- **Conservation-by-channel (ave-representation-capability-check v1.1 (C); ave-conserved-vs-pumped):** per step at the wall the operator (1) extracts per-cell spin `Δs(r)=χ̃·g_wall(r)·s_density(r)` by scaling π_w←π_w·(1−χ̃·g_wall) — since `s_density=(w×π_w)·n̂` is LINEAR in π_w, the spin removed equals `Σ Δs·dV ≡ δL` EXACTLY; (2) deposits exactly δL into `u_adv` as a wall-localized azimuthal increment `δu=Ω_add·(n̂×r)·g_wall` with `Ω_add=δL/I_wall`, `I_wall=Σ ρ̄_full·g_wall·r_⊥² dV` ⇒ `ΔL_bulk≡δL` EXACTLY. **AM ledger closes 1:1 BY CONSTRUCTION** (the exchanged L comes FROM the photon; bounded; no refilled source — δL→0 as S_φ drains). The ENERGY ledger is tracked, NOT assumed conservative: the photon spin-scaling removes `E_ph_loss=½Σ|π_w|²(1−(1−χ̃g)²)dV`, the deposit adds `E_bulk_gain=½Σρ̄_full|δu|²dV`; the remainder `E_absorb=E_ph_loss−E_bulk_gain` is a passive lossy-mirror sink. **GATE on the channel: `E_absorb ≥ 0` (the wall is PASSIVE — never creates energy) and H_total not increased** (the D11 discipline, re-applied to the transducer).
- **DERIVATION of δL form / the swept coefficient:** the FORM `δL ∝ κ̃·h·g_wall·(photon spin)` is the ADD-2 canonical velocity-space rotation (`crystal_engine.py:33-37`: a chirality-signed angle θ_χ=κ̃·h·g_front rotating the conjugate velocity pair, conserving the sum of squares) — applied to the ANGULAR pair (photon spin ↔ bulk orbital) instead of the (∂_tV,∂_tw) pair. The residual magnitude is the dimensionless per-step wall-extraction fraction `χ̃≡chi_exch` (the SWEPT knob); the κ̃-anchored value `χ̃=κ̃·dt·ω_ref` is run as one sweep point. **The verdict must be coefficient-ROBUST** (sign/oddness/null/depletion invariant across the χ̃ sweep; |ΔL_bulk| scales ~linearly with χ̃ — the expected, reported control-parameter scaling).
- **phase-space-coordinate-check:** the measured quantities (S_φ, L_bulk) are REAL-SPACE axial angular momenta — the native coordinate for an AM-transfer claim. No φ²/winding claim is made here, so no Park-along-contours extractor is invoked (that gate binds winding claims, A46).

### 6.2 THE SMOKE SETUP (a formed pocket + a bouncing chiral wave packet)

- N=40 (the MAIN config), `bulk_density_on=True` (so `u_adv` exists to receive orbital AM), **`buckle_on=False`** (ISOLATE D9 as the ONLY w↔bulk channel — the inherited bulk buckle is silenced so the transfer is unambiguous), `omega_sector_on=False` for the gate (focus the channel; ω-recipient is future-work). Snap optional (the saturated seed IS the trap/pocket).
- Planted pocket: `seed_bulk(frac=0.95)` — a saturated V blob whose A crosses `wall_center` ⇒ a g_wall shell (the chiral wall). `freeze_wall_window()` so the shell is a fixed geometric boundary.
- Chiral packet: `drive_chiral_photon(helicity=±1)` (CP) and `helicity=0` (achiral/linear control), seeded at center, propagating along the axis; it traverses the g_wall shell repeatedly (reflecting off the PML/box) — each traversal = a wall interaction (a "bounce").
- `u_adv` starts at REST (no energized column) ⇒ ΔL_bulk measures the transfer from ZERO (clean). With D9 off (`chi_exch=0`), nothing sources u_adv ⇒ ΔL_bulk≡0 (the structural known-null floor).

### 6.3 MEASUREMENTS (numbers FROM the evolved field — ave-driver-script-honesty)

(i) **d(L_transferred)/d(bounce)** = cumulative ΔL_bulk / N_bounce, with floor; (ii) **RH-vs-LH sign reversal** (helicity-odd, quantitative: the odd-part fraction); (iii) **the photon helicity ledger depleting 1:1** (cumulative S_φ_removed vs L_transferred ratio; AND the photon's MEASURED axial spin S_φ(t) depleting beyond the free-drift baseline); (iv) **the achiral null** (helicity=0 ⇒ ΔL_bulk at floor); (v) **knob sweeps** (chi_exch, bounce_thresh, wall_width).

### 6.4 FLOORS (ORDERED BINS — floor-check FIRST; ave-apparatus-floor-attribution v1.1)

- **F-EXCHANGE (the known-null):** the chi_exch=0 (transducer-OFF) run's |ΔL_bulk| (= structural zero + numeric noise). Every positive ΔL_bulk is gated on |ΔL_bulk| ≥ 100× F-EXCHANGE.
- **F-DRIFT (the free-spin baseline):** the chi_exch=0 run's |ΔS_φ| over the window (how much the photon's axial spin drifts from free propagation/dispersion/PML alone). A depletion claim must show |ΔS_φ(on)| exceeds F-DRIFT.
- **F-PROBE (PROBE-CAPABILITY keeper, the m-even lesson):** the spin probe S_φ must DISTINGUISH ±helicity on a KNOWN reference BEFORE any dynamics — a freshly-seeded RH photon gives S_φ of one sign, LH the opposite sign, achiral ≈0. Encoded as a keeper unit test (`test_unified_transducer_v6.py`). A probe that cannot separate ±h on the known seed is DISQUALIFIED (the verdict is CLIP).

### 6.5 APPARATUS INVENTORY — every D9 knob inventoried + swept (§210-COMPLIANCE GATE)

| knob | sweep | CLIP telltale |
|---|---|---|
| `chi_exch` (exchange coeff) | {0, 0.005, 0.02 (default), 0.08, κ̃-anchored} | the verdict (sign/oddness/null) tracks the magnitude (it must NOT — only \|ΔL_bulk\| scales ~linearly) |
| `bounce_thresh` (bounce detector) | {1.2, 1.5 (default), 2.0}× median I_wall | the TOTAL ΔL tracks the threshold (it must NOT — only the cosmetic N_bounce count tracks it) |
| `wall_width` (wall sharpness) | {0.06, 0.12 (default), 0.20} A-units | the verdict tracks the shell sharpness (sign/oddness must be invariant) |
| `helicity` ∈ {+1, −1, 0} | the helicity-odd + achiral-null axes | (this IS the discriminator, not a CLIP suspect) |

**§210 deviation policy:** the run executes EVERY sweep above, or states the deviation explicitly BEFORE running and re-bins. A positive whose governing knob was unswept is CLIP by this prereg's own law.

### 6.6 GATE BINS (FROZEN — Rule 11; no post-hoc criterion drop)

- **TRANSDUCER-LIVE** iff ALL: **(L1)** |ΔL_bulk(RH)| ≥ 100×F-EXCHANGE at default χ̃; **(L2)** helicity-odd — sign(ΔL_bulk(RH)) = −sign(ΔL_bulk(LH)) AND odd-part fraction |RH−LH|/(|RH|+|LH|) > 0.9 (near-perfect reversal); **(L3)** depleting + no pump — AM ledger 1:1 (|S_φ_removed/L_transferred − 1| < 1e-6) AND measured |ΔS_φ(on)| > F-DRIFT with the depletion sign AND E_absorb ≥ 0 AND H_total not increased; **(L4)** achiral null — |ΔL_bulk(helicity=0)| ≤ 3×F-EXCHANGE AND the F-PROBE keeper passes; **(L5)** coefficient/sharpness-robust — L1,L2,L4 invariant across the χ̃ and wall_width sweeps, |ΔL_bulk|∝χ̃, and total ΔL invariant across bounce_thresh (only N_bounce tracks it).
- **TRANSDUCER-DEAD** iff: D12(i) fires (RH≡LH byte-identical within 200 steps) OR |ΔL_bulk(RH)| < 10×F-EXCHANGE (no transfer above floor).
- **UNRESOLVED**: anything else (above floor but not helicity-odd; achiral not null; a pump detected; or a knob-tracking that cannot be separated into physics-vs-count).

### 6.7 D12 FAIL-FAST ASSERTIONS (cheap, early — run BEFORE the full matrix)

(i) after the transducer is enabled, RH-drive and LH-drive `u_adv` must NOT be byte-identical within 200 steps — if they are, the coupling is DEAD: ABORT the matrix, report TRANSDUCER-DEAD; (ii) the achiral arm must show |ΔL_bulk| at the F-EXCHANGE floor (the known-null) within the same window.

### 6.8 CORPUS STATE

- **OPEN.** This smoke is the GATE for the Run phase (the full T1–T6 spec-sheet matrix is GATED on TRANSDUCER-LIVE). It does NOT promote the electron claim (NOT-ELECTRON stands). The auditor lands any manual entry; this prereg + the smoke result SURFACE the empirical finding only.

---

## 7. PHASE 3 — THE GENESIS-RUN MATRIX (the full T1–T6 spec-sheet under the LIVE transducer; FROZEN before any run artifact — PREREG COMMITTED ALONE)

**Status when frozen (verify-before-cite, all grep/JSON-confirmed this session):** PHASE 1 hygiene CLOSED (JOB 1 D11 pump-fix PASS @ `fee2ccb6`; JOB 2 D10 both renderings @ `49520541`; JOB 3 snap-channel CLIP @ `e3a4eef8`). PHASE 2 D9 transducer smoke = **TRANSDUCER-LIVE** @ `3f2d914b` (all §6.6 L1–L5 + D12 pass; ΔL_bulk(RH) = −1.30084, odd-fraction 1.000, AM ledger 1:1, E_absorb +0.3195 ≥ 0, achiral ≡ 0; keepers 36/36 green). The smoke is the GATE; it is now PASSED, so the full Run matrix is **UN-gated**. **This is the FREEZE of that Run matrix.** It does NOT promote the electron claim — NOT-ELECTRON (the v5 panel ruling) STANDS until this Run returns; v6 asks the NEW question: *with the missing primitive (D9) now LIVE and the two hygiene blockers (D11 pump, D10 deflagration) fixed, does the assembly pass the spec-sheet — and is the lock the MOTION (D-PERM) as v5 certified?*

**Skills fired at this freeze (recorded):** `ave-apparatus-floor-attribution v1.1` (governing — ORDERED BINS §7.7, PROBE-CAPABILITY keepers §7.5, every knob inventoried+swept §7.6), `substrate-native-check` (CP2 conserved functional / CP10 boundary, walked §1 — re-applied to the Run config), `ave-conserved-vs-pumped` (the seed-V + Γ are energize+locked, the transducer depletes-not-pumps — §7.1 D9/D11), `ave-representation-capability-check v1.1` incl. (C) conservation-by-channel (the AM ledger closes 1:1; the ω recipient now wired — §7.2), `phase-space-coordinate-check` (T2 charge read in the `(V_inc,V_ref)` phase-space via Park-along-contours, r≥3 cells — §7.5), `ave-driver-script-honesty` (every Run number must come FROM the evolved field/JSON), `verify-before-cite` (every v5/smoke/hygiene anchor grep/JSON-confirmed), `flag-don't-fix` (the C-transducer-OFF byte-identity contamination flag §7.3).

### 7.1 THE V6 DESIGN — D-PERM / D9 / D10 / D11 / D12 (recorded verbatim-class from the adjudicated v5 verdicts; FROZEN, Rule 11)

> Recorded verbatim-class from the directive's V6 design block — itself the Grant-ratified reading of the v5 panel verdicts. FROZEN at this commit; the design INTENT does not change post-run.

- **D-PERM (inherited, CONFIRMED).** Permanence = THE MOTION-LOCK — conserved circulation + losslessness (`L_bulk` drive-off 0.97–0.99 ALL arms, ν_art-invariant across the 50× sweep, v5-panel-certified; JOB 3 re-confirmed the snap is NOT the lock — CLIP). **v6 does NOT ask the snap to hold anything; it asks the circulation to.**
- **D9 — THE TRANSDUCER (the centerpiece; the component that blocked six architectures; LIVE @ `3f2d914b`).** A CHIRAL BOUNDARY CONDITION at the wall/pocket surface — per-bounce spin-orbit exchange: a wave reflecting off the chiral wall exchanges a quantum of angular momentum between the photon's polarization/helicity and the trapped ω/bulk circulation (the ADD-2 compression→rotation buckle class, canonical; the polar-conjugate mechanism — the mirror reflects the radial pair, a CHIRAL mirror torques the angular pair per bounce; the frame-dragging SELECTIVE result is the validated direction). CONSERVATION BY CONSTRUCTION: the exchanged L comes FROM the photon (helicity depletes per bounce — bounded, no trilinear bulk potential, no refilled source — the depleting coupling the BEMF smoke demanded, achieved at a BOUNDARY not in the bulk). HELICITY-ODD by construction (reverses sign with photon handedness); ZERO for achiral drive. CP10 throughout: the coupling lives ON the boundary; every bulk-coupling architecture detonated or nulled — no bulk terms.
- **D10 — SELF-LIMITING SNAP (the deflagration fix; both renderings built + swept, JOB 2).** (a) VENT-ABSORBED — the vented latent goes into a conservative store (removed from dynamics; ledger must close); (b) MEISSNER-HARDENING — each snapped cell RAISES neighbors' snap threshold (negative feedback; real condensation nucleates-and-stops). The snap's role = the BIRTH FLASH only (the D6 burst detector, which WORKED in v5 — ~160 bursts 3–6 OOM above floor — rides again unchanged).
- **D11 — THE PUMP FIX (gate for any T1 retest; PASS @ `fee2ccb6`).** Isolated the v5 +283% H_total to GAP-C vent re-injection → the genesis-24 seed-V breather; fixed (`vent_mode="absorbed"` + `snap_accounting="conservative"` + H reported in `bulk_energy_conserved`) to ledger-closure above F-CLOSE (post-fix MAIN drive-off max positive excursion 0.0000% ≤ F-CLOSE +0.184%). **If the MAIN build does not close the ledger above F-CLOSE at run-time, the genesis arm does not run (honest block).**
- **D12 — FAIL-FAST ASSERTIONS (cheap, early; run BEFORE the full matrix).** (i) after the transducer is enabled, RH-drive and LH-drive arms must NOT be byte-identical within 200 steps — if they are, the coupling is dead: ABORT the matrix, report TRANSDUCER-DEAD (do not burn the full run); (ii) the achiral arm must show zero net helicity transfer (the known-null).

### 7.2 THE MAIN CONFIG (the assembled object) + the config DELTAS from the smoke (floors RECALIBRATE)

The MAIN object = **seed + self-limited snap + chiral drive + transducer ON**, with the **Cosserat-ω recipient wired back on** (the smoke's flag #2: it validated the `u_adv` recipient only; T2/T3 charge+spin live in the Cosserat `(2,3)` winding, so the Run wires the transducer deposit onto the ω circulation as well — the natural next channel the smoke named):

- **seed:** `seed_bulk(frac=0.85)` (the v5 deep-saturation operating point; K4 swept §7.6);
- **snap (the better hygiene rendering):** `vent_mode="absorbed"` ⊕ `meissner_harden=0.05` ⊕ `snap_accounting="conservative"` (JOB 2: bounds BOTH channels — E_V 13.1 AND pocket 1704 — birth-flash preserved; increment 0.05 is the saturated best);
- **drive:** `drive_chiral_photon(helicity=+1)` (RH; the FOC d/q chiral transverse photon, D5);
- **transducer:** `transducer_on=True`, `chi_exch=0.02` (default), the ω + `u_adv` recipient wired;
- **sectors:** `omega_sector_on=True`, `buckle_on=True` (the Run RE-ENABLES the inherited winding/buckle sectors the smoke silenced to isolate D9); `H_total` reported in `bulk_energy_conserved` (CP2/D11);
- `N=48` (§7.9), `n_build=3200`, `n_persist=1200`, seed `20260610`.

**Config DELTAS from the smoke ⇒ floors RECALIBRATE** (the directive: *"the v5 floors inherit where configs match; recalibrate where they don't"*). The Run differs from the smoke in (1) `N=40→48`, (2) `omega_sector_on`/`buckle_on` RE-enabled, (3) the longer 4400-step window, (4) the self-limited snap active. THEREFORE every inherited floor — F-CLOSE, F-EV, F-BURST/F0d, F-DRIFT, F0e drift, F-PROBE — is RE-MEASURED by its own known-null run at the Run config BEFORE any binning (ave-apparatus-floor-attribution v1.1: a floor carried over from a different config is invalid). The STRUCTURAL zeros (F-EXCHANGE at `chi_exch=0`; achiral `S_φ≡0`) remain structural and are re-CONFIRMED, not re-measured.

### 7.3 THE ARM MATRIX (FROZEN — Rule 11; evaluated under BOTH P1/P2)

| arm | seed | snap (self-limited D10) | drive chirality | transducer | purpose / frozen expectation |
|---|---|---|---|---|---|
| **MAIN (RH)** | yes (Lane-1 V) | yes (absorbed ⊕ meissner 0.05) | chiral RH (h=+1) | ON | the v6 build claim — does the LIVE transducer assemble a spec-sheet object? |
| **C-transducer-OFF** | yes | yes | chiral RH | **OFF** | **the v5 reproduction** — handedness must NOT couple (the four-arms-byte-identical bulk); the KNOWN-NULL for the whole v6 thesis (the only difference vs MAIN is D9) |
| **C-achiral** | yes | yes | achiral (h=0, linear-pol) | ON | NULL — zero net helicity transfer (D12-ii); the **sharpened-T5 known-null** (the twin must be SYMMETRIC here) |
| **C-LH** | yes | yes | chiral LH (h=−1) | ON | SIGN-REVERSAL — charge/winding/twin sign must FLIP vs MAIN (helicity-odd; smoke: ΔL_bulk +1.3008 = −RH) |
| **C-no-seed** | **NO** | yes | chiral RH | ON | must FAIL/HEAL — no Lane-1 V source (the genesis-23 `V≡0` free-space pair-production prohibition) |
| **C-no-snap / P1** | yes | **NO** | chiral RH | ON | **the D-PERM-only discriminator** — does a snapless pocket + circulation + LIVE transducer still pass T1? (motion-lock alone, no birth-flash); persistence here = the rival POSITIVE |
| **C-no-snap / P2** | yes | **NO** | chiral RH | ON | control — expect HEAL under forced de-spin |
| **C-τzx-on** | yes | yes | chiral RH | ON | Fork-A — literal `τ_zx` radiation-reaction feedback ON (its own arm) |
| **C-τzx-off** | yes | yes | chiral RH | ON | Fork-A baseline — `τ_zx` feedback OFF (contrast for C-τzx-on) |

**The load-bearing v6 contrast:** MAIN vs C-transducer-OFF. v5's headline was four arms byte-identical in the bulk (the handedness never coupled). v6's thesis is that D9 BREAKS that byte-identity — MAIN must DIFFER from C-transducer-OFF in the winding/charge/twin channels, and C-transducer-OFF must REPRODUCE v5 (byte-identical across handedness with D9 off). **FLAG (flag-don't-fix):** if C-transducer-OFF is NOT byte-identical across handedness, the contrast is contaminated (a leak outside D9) — surfaced before binning, not silently fixed.

### 7.4 PERSISTENCE P1 / P2 (per v5 D8; the D-PERM test)

Every arm is built, then run under **P1** (drive-off, L-conserved, dissipation-minimized + the ν_art sweep §7.6) AND **P2** (forced de-spin), exactly as v5. P1 = the electron's actual situation (circulation never stops); the D-PERM prediction = pocket+winding persist on the conservation clock with any decay TRACKING ν_art (→ apparatus) or PLATEAUING (→ physics, the v5 deficit −0.0516 INVARIANT). P2 = the static test (the snap's domain — now CLIP per JOB 3). The `C-no-snap / P1` arm is the MOTION-LOCK discriminator (persistence there = the rival positive, NOT a control failure); `C-no-snap / P2` is the must-heal control.

### 7.5 THE SPEC SHEET T1–T6 + the SHARPENED T5 (floors ORDERED FIRST — ave-apparatus-floor-attribution v1.1; FROZEN bins, Rule 11)

| test | FLOOR-CHECK (FIRST — gates the positive) | POSITIVE bin (only if the floor passes) | NEGATIVE / false-positive bin | class |
|---|---|---|---|---|
| **T1 mass (primary)** | `H_total^cons` (the CP2/D11 CONSERVED functional, NOT the naive) window-converged within F0e drift-floor AND `E_V` bounded < 10×F-EV (no deflagration — D10) | `H_total^cons →` const SET BY the dynamics (not = the seed input, not still-rising) | still-rising / detonates / tracks seed amplitude (the v5 `E_V 13→50339` falsifier) | emergence vs manifestation |
| **T2 charge** | F0b `r≥3` cells + phase-space Park-along-contours read (NOT lattice-Cartesian) | integer `(2,3)` winding, sign = handedness, FLIPS RH↔LH (now POSSIBLE — D9 wires photon-helicity→ω, the channel v5 found inert) | `w_pol≡0` (the channel still builds no poloidal winding) → the NAMED residual (A44 coupling-family gap) | emergence (de-novo) vs manifestation |
| **T3 spin** | F0c reactance-pair every step + CP5 local-clock (`A²_local` reported); the DERIVED ½-pole-pair form | locked `L_ω` at the ½-pole-pair value WITHOUT dialing `lock_eta` (η-invariant) | unlocked / `L_ω` tracks `lock_eta` (the v5 CLIP, `5.38→0.067` over η) | emergence vs consistency |
| **T4 kick** | F0a interior + re-run T1–T3 post-perturbation | T1–T3 RE-VERIFY post-kick | any of T1–T3 fails post-kick (or "passes" only as robustness-of-runaway — the v5 MOOT) | manifestation |
| **T5 twin — SHARPENED to the CHIRAL twin** | **the C-achiral arm is the KNOWN-NULL: the twin-asymmetry probe MUST read ≈0 on C-achiral** (the m-even PROBE-CAPABILITY keeper for T5) | the counter-rotating partner / pocket-split asymmetry is PRESENT in MAIN & C-LH, FLIPS sign RH↔LH, AND is ABSENT/symmetric in C-achiral, beyond the calibrated floor | a twin BYTE-IDENTICAL across chiral AND achiral arms = **GEOMETRIC — the v5 NAMED FALSE POSITIVE** (`RH=2608/LH=1040` identical in achiral); binned BLIND, not a positive | emergence; absence ≠ failure-of-discipline |
| **T6 de Broglie** | F0a + translate the locked state at ≥2 momenta; **weight-bearing ONLY if T1 passes** (the v5 caveat: a flat-λ read on a detonating object carries no weight) | `λ∝1/p` (exponent −1) within fit-floor | no `1/p` scaling | consistency |

**The sharpened-T5 keeper (PROBE-CAPABILITY, the m-even lesson):** the twin-asymmetry probe is validated on the C-achiral known-null — it MUST return ≈0 there (zero net helicity ⇒ no chiral twin). A probe that reports a "twin" on the achiral arm is reading the rotation-column GEOMETRY (the v5 false positive — `RH=2608/LH=1040` byte-identical across MAIN/achiral/opp-helicity) and is DISQUALIFIED (the chiral-twin verdict is CLIP). Encoded as a keeper unit test alongside the F-PROBE m-even keeper.

**SPEC-SHEET verdict bins (FROZEN, inherited from v5 §4.2):**
- **ELECTRON-CLASS** — T1 (primary) passes AND ≥4 of T2–T6 pass at their floors, with NO spec-sheet positive sitting at a clip value.
- **PARTIAL** — T1 passes but the winder/spin/twin localizes (a NAMED residual — e.g. a surviving `w_pol≡0` winder gap DESPITE the live transducer) — report the named missing primitive (A44: an engine coupling-family gap, NOT a missing axiom; NOT auto-pivoted).
- **NOT-ELECTRON** — T1 fails (mass does not converge) → transient/pump; clean negative, branch closes (Rule 11), mechanism named.
- **VOID** — a forbidden seeder fired / a non-null C-no-seed / a winding read below F0b / C-transducer-OFF not byte-identical across handedness → not reported as a positive.

**D-PERM bins (the persistence verdict, inherited + re-confirmed):** MOTION-LOCKED (P1 `L_bulk` ratio→1, ν_art-invariant) / apparatus (decay ∝ ν_art). **Chiral-twin bins:** SELECTIVE (chiral ≠ achiral beyond floor; twin flips RH↔LH) / GEOMETRIC (chiral ≡ achiral — the v5 false positive) / BLIND / UNRESOLVED.

**HARD CONSTRAINT (Rule 11 honest closure):** a positive at a clip value is APPARATUS. Do NOT debug toward a positive; do NOT drop an adjudication criterion post-hoc to convert a negative to a positive. A clean negative with a named mechanism is the discipline at full strength.

### 7.6 THE MANDATED-SWEEP LIST (§210-COMPLIANCE GATE — every knob the bins depend on, EXPLICITLY ENUMERATED; FROZEN)

**The run MUST execute every sweep below, OR state the deviation explicitly BEFORE running and re-bin. A positive whose governing knob was unswept is CLIP by this prereg's own law (the v5 lesson, now structural).** The SIX directive-mandated sweeps:

| # | knob | swept grid | which bin it gates | CLIP telltale |
|---|---|---|---|---|
| 1 | **exchange coefficient** `chi_exch` | {0, 9e-4 (κ̃-anchored), 0.005, 0.02 (default), 0.08} | the D9 transducer-coupling bins — T2/T3/T5 (the whole v6 thesis) | the VERDICT (sign/oddness/null/twin) tracks the magnitude — it must NOT; only \|ΔL\| scales ~linearly with χ̃ |
| 2 | **`Δ_heal`** (re-entry width) | {0.0, 0.02, 0.05} | the snap-channel persistence / the D-PERM-vs-snap split | pocket-persistence tracks Δ_heal (built-in irreversibility — the §210-skipped v5 knob) |
| 3 | **payback** `snap_payback_rate` | {0.0, 1.0, 5.0} | the persistence/lock bin (re-confirms JOB 3 CLIP under the LIVE-transducer config) | pocket-persistence tracks payback (pinned-at-1.0 was the v5 construction) |
| 4 | **K3 stop-time** `n_build`/`n_persist` | build {2400, 3200, 4000}; persist {300, 600, 1200} | T1 `H_total^cons` convergence (the "converged value tracks stop-time" falsifier) | the T1 "converged" mass / the pocket tracks when the run STOPS |
| 5 | **D10 hardening increment** `meissner_harden` | {0.0, 0.02, 0.05, 0.10} | the D10 deflagration containment (E_V / pocket bound) | the bounded pocket tracks the increment (EXPECTED — it is the control parameter; reported, not hidden) |
| 6 | **`ν_art`** artificial viscosity | {1e-4, 5e-4, 1e-3, 2e-3, 5e-3} (50× span) | D-PERM / the P1 motion-lock (the D8 attribution knob) | P1 heal/decay rate ∝ ν_art ⇒ apparatus; plateau as ν_art→0 ⇒ physics (v5: deficit −0.0516 INVARIANT) |

**ALSO mandated (§210 "every knob the bins depend on" — additional inventoried CLIP-suspects, swept):**

| knob | swept grid | gates | CLIP telltale |
|---|---|---|---|
| **K2 `N` resolution** | {40, 48 (primary), 56} | T1 / snap-onset (the standing v5 K2 CLIP suspect) | the T1 verdict or onset tracks N (the under-resolved pocket) — the headline must be N-robust |
| **`wall_width`** (transducer shell sharpness) | {0.06, 0.12, 0.20} | the D9 L5 robustness (RE-swept: the Run re-enables ω/buckle vs the smoke) | sign/oddness/twin tracks shell sharpness |
| **`lock_eta`** (rigid-rotation lock; κ_L=6/5 BEMF) | {0, 0.05, 0.08, 0.12} | T3 spin (must be η-invariant) | the locked `L_ω` VALUE tracks η (the v5 T3 CLIP) |
| **K4 seed `frac`** (saturation depth) | {0.30, 0.60, 0.85 (default), 0.95} | the regime gate (a positive only at shallow frac = sub-saturation artifact) | a spec-sheet positive seen ONLY at shallow frac |

**§210 DEVIATION POLICY (the v5 lesson, structural):** the run executes EVERY sweep above, OR states the deviation explicitly BEFORE running and re-bins. The PHASE-2 smoke already logged one HONEST such deviation (the per-bounce metric is degenerate at the CFL dt — continuous spin-drain, not ballistic bounces — so `bounce_thresh` was swept and confirmed cosmetic via the THRESHOLD-INVARIANT total ΔL; the §210 purpose was served, the deviation stated, not papered over). The Run carries that caveat forward for any per-bounce reporting; the headline transducer transfer is the cumulative ΔL into the ω/`u_adv` channel.

### 7.7 THE FROZEN BINS — FLOOR-CHECKS ORDERED FIRST (Rule 11; the coax bin-65/67 + m-even lessons)

**FLOOR-0 (the universal gate, evaluated BEFORE any §7.5 spec bin — inherited from v5 §4.0, RECALIBRATED at the Run config §7.2):**
- **F0a interior-only** — PML+sponge excluded (`pml_thickness ≤ {i,j,k} ≤ N−pml_thickness−1`), sampled at energy-density PEAKS (top-K |field|²), NOT centroid (CP7).
- **F0b extractor floor** — the winding read (T2) requires `r_meas ≥ 3` cells (the graft-v4 floor); below it the read is VOID.
- **F0c reactance-pair completeness** — C-state (V_inc/ω) AND L-state (Φ_link/ω_dot) recorded EVERY step (A-Rule-10); a single-phase snapshot is UNRESOLVED for any lock-vs-oscillator-at-peak question.
- **F0d burst-detector calibration** — the D6 flash floor (F-BURST) re-measured on a Run-config known-null free run; a burst below it is UNRESOLVED.
- **F0e conservation canary** — `L_bulk`/Γ drift in the QUIET phase within the free-floor; secular drift ⇒ dissipation-contaminated, FLAGGED before binning.
- **F-CLOSE (the D11 pump pre-gate)** — re-measured at the Run config; the MAIN build `H_total^cons` must show NO positive excursion above F-CLOSE, else the genesis arm does NOT run (honest block).
- **F-EXCHANGE / F-DRIFT / F-PROBE (the transducer floors)** — the structural zeros re-confirmed; the F-PROBE m-even keeper (±h separable on the known seed) AND the sharpened-T5 twin-probe keeper (≈0 on C-achiral) must PASS or the relevant verdict is CLIP.

**ORDERING RULE (HARD CONSTRAINT):** for EVERY observable the FLOOR-CHECK is evaluated FIRST and GATES the positive. A signal below its own calibrated floor → UNRESOLVED (cannot be a positive). A positive that TRACKS a §7.6 knob → CLIP, named by the knob. The frozen spec/persistence/twin bins are §7.5; FLOOR-0 gates them all.

### 7.8 THE FAIL-FAST ASSERTIONS (D12 — cheap, early; run BEFORE the full matrix)

1. **D12(i) — transducer-alive.** After the transducer is enabled (MAIN config), RH-drive and LH-drive (`u_adv` AND the ω channel) must NOT be byte-identical within 200 steps. If they are, the coupling is DEAD: **ABORT the matrix, report TRANSDUCER-DEAD** (do not burn the full run). [Smoke precedent: max|u_RH−u_LH|@200 = 2.7e-3 > 0 — alive.]
2. **D12(ii) — achiral known-null.** The C-achiral arm must show |ΔL_bulk| ≤ 3×F-EXCHANGE (zero net helicity transfer) within the same window.
3. **D11 pre-gate — the pump block.** Before the genesis matrix runs, the MAIN-config build `H_total^cons` must close above F-CLOSE (no positive excursion). If it pumps, the genesis arm does NOT run (honest block — the directive's D11 condition).

### 7.9 SCALE / BUDGET (the §8 N³ law governs; N frozen)

v5 ran **N=40 in 481 s** (`n_build=3200` + `n_persist=1200` = 4400 steps/arm). The §8 cost law `~9.4e-8·N³ s/step` (verified live, v5 §8) gives per-step / per-full-arm-run (4400 steps):

| N | ms/step | s / full arm | memory/engine |
|---|---|---|---|
| 40 | 6.0 | 26 | ~12 MB |
| **48 (frozen)** | **10.4** | **46** | **~20 MB** |
| 56 | 16.5 | 73 | ~31 MB |
| 64 | 24.3 | 107 | ~46 MB |

The `genesis_parallel_runner.py` (ProcessPool, **5.0× effective** at 12 workers, determinism `serial==parallel` CONFIRMED) fans the matrix; `fast_winding_extractor.py` (25.8×, float64-mandatory) accelerates the T2 reads. The full mandated matrix ≈ 9 arms (build + P1 + P2 continuations) + the §7.6 sweeps (chi_exch 5, ν_art 5, Δ_heal×payback 3×3, K3 3, meissner 4, K2 3, wall_width 3, lock_eta 4, K4 4) ≈ **~55 build-equivalents**. At N=48: 55 × 46 s ≈ 2530 s serial / 5× ≈ **~8.5 min wall**; at N=64 ≈ 20 min — both within a single-session budget.

**FROZEN: N=48 primary.** Budget is NOT the binding constraint (even N=72 fits < 30 min); the BINDING constraint is the HARD floor-inheritance rule. N=48 is the disciplined "largest N the budget allows": (1) it is a genuine resolution bump over the v5/smoke N=40 baseline — so the K2 CLIP-check {40, 48, 56} has something to test (the v5 K2 lesson: snap onset tracks N); (2) it keeps the N=40-validated transducer keepers within ONE resolution step (de-risks re-validating the D9 operator at a far-off N); (3) all inherited floors (§7.2) recalibrate cheaply at N=48. The K2 sweep {40, 48, 56} brackets the headline so any N-tracking is caught and binned CLIP. (Going to N=64+ is affordable but multiplies the floor-recalibration + keeper-revalidation surface for a marginal resolution gain — recorded as the explicit reason N is frozen at 48, not higher.)

**EXCLUDED (honesty):** f32 dtype — physically forbidden (the conservation canaries operate at 1e-3, the winding gate needs 1e-12; f32 desyncs the ledger). `np.roll→slicing` — microbenchmarked NEGATIVE (v5 §8).

### 7.10 CORPUS STATE + DISCIPLINE

- **OPEN.** This freeze does NOT promote the electron claim — NOT-ELECTRON (the v5 panel) STANDS until the Run returns. The Run asks the NEW v6 question (D9 LIVE + the two hygiene blockers fixed).
- **Rule 11:** the bins (§7.5/§7.7) are frozen; floor-checks gate every positive; a clip-valued positive is APPARATUS; a clean negative with a named mechanism is the discipline working. No post-hoc criterion drop, no debugging toward a rescue.
- **Rule 12:** the v5 SNAP-LOCKED slot's 🔴 demotion (→ CLIP, JOB 3) stands; this freeze does NOT refill it. A v6 spec-sheet positive (should one survive) is a NEW hypothesis with its own verification chain (this prereg + the Run result).
- **The auditor lands any manual entry; this prereg + the Run result SURFACE the empirical finding only.** Do not draft the auditor's manual; do not draft Ax-5 candidates (the diagnosis is engine-coupling-family, A44, not a missing axiom).
