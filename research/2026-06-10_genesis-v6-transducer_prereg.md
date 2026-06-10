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
