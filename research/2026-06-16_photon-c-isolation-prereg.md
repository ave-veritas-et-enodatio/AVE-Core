# Prereg-lite (FROZEN) — T₂-photon group velocity isolated from the √2c A₁/CFL precursor

**Status:** FROZEN at scaffold time (bins + adjudication criteria fixed before the driver runs).
**Date:** 2026-06-16. **Branch:** `analysis/2026-06-16-photon-c-isolation`. **Grounded against** `origin/main` @ `1ad1e7fc`.
**Class:** DOCUMENTATION run (Grant: DEC-01 / weak-C ruled; "just to document it"). Not a discriminator-for-decision; documents the mode-identity of the √2c front.
**Lane:** implementer. **Skills fired:** `substrate-native-check` (CP1–CP4, CP7), `phase-space-coordinate-check` (the √2 trap), `verify-before-cite`, `pre-test-physics-check`.

---

## 0. What this closes

The `_orchestration/2026-06-14_photon-ontology-vocabulary-adjudication-handoff.md` Amendment-2 RESIDUAL OPEN (verified verbatim, handoff:16):

> the front is **√2·c, not c**, and `project_T2` on=off gave identical speed in the cardinal sweep → the measurement plausibly catches the **A₁/CFL bulk front (√2c), not the resolved T₂-photon group velocity (which should be c)** … the **mode-identity of the √2c front (bulk-precursor vs photon) is still unisolated**.

This prereg isolates the T₂-envelope group velocity from the A₁ longitudinal bulk front and runs a causality (information-front) check.

---

## 1. Substrate-native walk (recorded BEFORE the driver — CP1–CP4, CP7)

- **CP1 dynamics:** K4-TLM scatter+connect wave propagation. A propagation-speed measurement, native to the lattice. NOT minimization/eigensolve.
- **CP2 sector:** the A₁ longitudinal common-mode (`(1,1,1,1)`, scatter eigenvalue **+1**, verified `np.linalg.eigvals(0.5·𝟙−I)` → `[-1,-1,-1,+1]`) vs the T₂ transverse triplet (eigenvalue **−1**) is the load-bearing split. Cross-coupling (Op14) is OFF (linear vacuum, sub-yield) — pure V-sector.
- **CP3 objective:** measure two real-space speeds (peak-arrival of the T₂ envelope; leading-edge of the A₁ compression front) — NOT an energy functional.
- **CP4 — THE √2 TRAP (load-bearing).** Verified the √2 has THREE lattice-geometry origins, all coincident, none a physical anisotropy (handoff §2 + Amendment-2; `k4_tlm.py:183`):
  1. **dt CFL convention:** `dt = dx/(c·√2)` (`k4_tlm.py:183`). The cardinal-x front marches **exactly 1 cardinal cell per step** because every connect-shift has x-component ±1 (`k4_tlm.py:378–383`, verified). So `v_cardinal = dx/dt = c·√2` by construction — a **clock convention baked into dt**, mode-blind.
  2. **per-port distance-count convention:** counting a `(1,1,1)` port hop as "one diagonal unit" → c. The diagonal-arm run (handoff Amendment-2) found v_diag ≈ √2c too in **real-space Euclidean** distance → A ≈ 1, isotropic. The cardinal/diagonal split is a distance-COUNTING artifact.
  3. **A₁ bulk mode speed** √(K/ρ)=√2c (K=2G), `constants.py` `V_LONG=√(2·G_VAC/RHO_BULK)`.
  - **Discipline (this prereg):** measure in **physical lattice distance (cardinal cells of dx) over physical time (steps × dt)** and report `v/c`. Do NOT re-introduce the per-port distance count. The mode-separation is carried by the **group velocity** (envelope peak-arrival), because A₁ (eigenvalue +1, non-dispersive DC front) and T₂ (eigenvalue −1, carries a per-step −1 phase → distinct dω/dk) accumulate phase differently under scatter even though the connect-shift is shared. The envelope tracks dω/dk; the A₁ leading edge tracks the fastest non-dispersive channel.
- **CP7 sampling:** PML-cell exclusion on all front/peak extraction (`pml ≤ {i,j,k} ≤ N−pml−1`); leading-edge front = first interior plane where slab-energy exceeds a fixed fraction of its own lifetime max; envelope peak = argmax of the slab-energy time-series at a reference plane.

**Coordinate-system match (`phase-space-coordinate-check`):** the corpus claim being tested is a **propagation SPEED** (real-space distance / real-time), NOT a phase-space (V_inc,V_ref) topology claim. The correct coordinate system is **real-space Euclidean (cardinal-cell) distance over physical (dt-scaled) time** — which the canonical `v=(x_b−x_a)·dx/(t_b−t_a)` already uses. The √2 is the coordinate/sampling artifact the skill warns of; the test divides it out by reporting `v/c` in dt-scaled physical time (where the fastest channel = √2c by the dt convention) and separating modes by the group/front split, NOT by a per-port re-count. MATCH confirmed.

---

## 2. The test

### Test 1 — T₂ group velocity vs A₁ bulk front (mode isolation)

Three source configurations on the SAME empty linear-vacuum K4-TLM lattice, +x̂ plane source:

- **PURE-T₂:** `project_T2=True` (Σw=0, the canonical photon launcher). Measures the T₂ envelope group velocity.
- **PURE-A₁:** an A₁-only source `w=(1,1,1,1)·norm` (forward common-mode). Measures the A₁ longitudinal bulk front.
- **MIXED:** raw forward weights (~50% A₁ + ~50% T₂) — the historical default that produced the √2c reading; included to reproduce the unisolated baseline.

For each: record at every step the slab energy `Σ_{y,z}|V|²(x)` over interior planes (PML-excluded). Extract:
- **v_group** = peak-arrival speed of the slab-energy ENVELOPE between two interior reference planes x_a, x_b (the group-velocity observable).
- **v_front** = leading-edge speed (first-arrival at 10%-of-lifetime-max threshold) between the same planes (the front observable).

All speeds reported as **v/c** in dt-scaled physical time.

### Test 2 — causality / information front

Launch a **sharp on/off step** (the carrier abruptly switched on at t₀, no Gaussian ramp) into the PURE-T₂ configuration. The information front = the first interior plane at which a disturbance carrying the step is detectable above a fixed noise floor. Track first-detectable-arrival vs x. Verify the **information front does not exceed c** in dt-scaled physical time (distinct from any √2c precursor AMPLITUDE that may run ahead).

Note the substrate subtlety to be documented: the connect-shift marches 1 cardinal cell/step → the *bare front* is √2c by the dt convention. The causality question is whether the **step-carrying information** (the modulation that encodes "signal turned on") rides at c or at the bare-front √2c. This is the load-bearing causal observable.

---

## 3. FROZEN BINS (adjudication criteria fixed now)

Let R_T2 = v_group(PURE-T₂)/c, R_A1 = v_front(PURE-A₁)/c. "≈ c" means within ±15% of 1.0; "≈ √2c" means within ±15% of 1.414.

- **BIN T2-RIDES-AT-c** — `R_T2 ≈ c` AND `R_A1 ≈ √2c` AND `R_A1 > R_T2` by > 15% (A₁ front demonstrably ahead of the T₂ envelope). ⇒ photon = c, √2c = a SEPARATE bulk precursor → **weak-C reconciliation documented** (continuum transverse-energy photon at c; √2c is the bulk forerunner ahead of it).
- **BIN T2-RIDES-AT-√2c** — `R_T2 ≈ √2c` (the T₂ envelope itself rides at √2c, not c). ⇒ the transverse photon itself is √2c → **weak-C complicated, FLAG to Grant** (do not silently reconcile).
- **BIN UNISOLABLE-ON-THIS-ENGINE** — PURE-T₂, PURE-A₁, MIXED group velocities are statistically indistinguishable (all within ±15% of each other) AND no front/envelope separation is resolvable. ⇒ A₁ and T₂ cannot be separated on this engine → **document the limitation** (the connect-shift dt convention pins all single-front peak-arrivals to √2c; mode-identity not resolvable by propagation speed alone — consistent with the handoff's "propagation speed cannot separate them, only causality can").

**Causality sub-result (Test 2), reported alongside the bin:**
- **CAUSAL-OK** — information front ≤ c (within +15%). ⇒ supports weak-C (signal respects c; √2c is precursor-amplitude only).
- **CAUSAL-VIOLATION** — information front demonstrably > c. ⇒ FLAG to Grant (would contradict `photon-propagation-baseline.md:50` "NOT faster than c").

---

## 4. Honest-closure commitments (Rule 11 / Rule 12)

- The bin is read mechanically off the frozen criteria in §3. No post-hoc criterion drift to convert a bin.
- If PURE-T₂ rides at √2c (BIN T2-RIDES-AT-√2c) or causality violates, that is FLAGGED to Grant, not reconciled.
- If UNISOLABLE: that is itself the documented result (a clean engine-capability finding consistent with the handoff's reframe that propagation speed cannot separate continuous-sampled from discrete-transfer). It is NOT a falsification of weak-C — it documents that THIS engine's speed measurement cannot adjudicate it, leaving causality (Test 2) as the discriminator.
- This is a DOCUMENTATION run: the deliverable is the bin + the two speeds + the causality result. No corpus claim is edited; any baseline-leaf correction is surfaced for the auditor lane to land.

---

## 5. Surfaced physics question (pre-test-physics-check)

**Plumber-physical question (documented, non-blocking):** the connect-shift marches the wavefront 1 cardinal cell/step independent of mode, and dt fixes that to √2c. So the *bare front* of EVERY mode is √2c. The genuine mode-separation must live in the **group velocity** (envelope), where the T₂'s per-step scatter sign-flip (−1 eigenvalue) gives it a distinct dω/dk from the A₁ DC front (+1 eigenvalue). The driver tests whether that group-velocity split is large enough to resolve on this engine, or whether the dt convention swamps it (→ UNISOLABLE). Either outcome is a clean documented result; this question is what the driver answers, not a framing call for Grant pre-design.
