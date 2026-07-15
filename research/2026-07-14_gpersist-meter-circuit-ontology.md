# G-PERSIST meter — circuit-ontology completion (Ruling 2 addendum)

**Date:** 2026-07-14 · **Branch:** `analysis/gpersist-meter-ontology` ·
**Driver:** [`src/scripts/vol_1_foundations/gpersist_localization_observable.py`](../src/scripts/vol_1_foundations/gpersist_localization_observable.py) ·
**Parent RESULT (banked, NOT edited — this doc is its addendum):**
[`2026-07-14_gpersist-localization-observable_RESULT.md`](2026-07-14_gpersist-localization-observable_RESULT.md) ·
**FROZEN prereg:** [`2026-07-14_gpersist-localization-observable_prereg_FROZEN.md`](2026-07-14_gpersist-localization-observable_prereg_FROZEN.md) ·
**Gate:** Grant **Ruling 2** (2026-07-14, in-chat) — complete + fully label the circuit
ontology, then the KEEP-BOTH path is unblocked.

**Class:** meter-completion addendum. Completes the #689 RESULT **finding #3 (ESCALATED)** —
the frozen meter read the **potential register only**, omitting the Cosserat **kinetic**
register (~44 % of H). This doc labels **both** registers, pins the attribution + sponge-
exclusion conventions, banks the KEEP-BOTH split, and reports the before/after.

**Settled, NOT re-opened by anything here:** the enclosure fork is **RULED Reading A**
(wake-feeding; Grant 2026-07-14) and **G-PERSIST is ★RULED**. The fork is scored on the
**torus** `pair`+`graded_a0` cells (no sponge); **both registers read LOOP-FILLING there**, so
the RULED verdict is **unchanged**. One boundary-corroboration finding is surfaced for
adjudication (§7) — it does **not** move the torus fork verdict.

---

## Sector header (mandatory)

MODE = driven genesis on the saturable K4⊗Cosserat lattice, fixed-\(N\), rank-4 carrier,
re-run through the #689 instrumented mirror loop (Rule-14: same primitives, no new
engine/stepper/retune). REGIME = at/above-yield launch (`n_drive_mult=0.5`) → anhysteretic
quiet-window relaxation (`n_quiet_mult=1.5`), the banked #670 D2 schedule. PHASE-STATE = seed
→ de-energize → does the ENERGY blob concentrate or stay distributed. **Which sector carries
the DOF?** The energy blob is an **A1** two-register LC store (below); the **T2/Φ_link**
winding channel is measured separately and **never summed** into A1. **Cold vs saturated?**
Saturated launch (`use_memristive_saturation=True`), anhysteretic relaxation.
consistency-vs-emergence = **consistency-check / fork-discriminator** (no CODATA/manuscript
target; no emergence claim). phase-space-coordinate-check = the fork's self-tightening-vs-
spreading claim is **real-space**; the meter is real-space lattice coordinates (matched); φ is
the phase-space/gauge scalar, carried separately.

---

## 1 · The circuit ontology — the energy blob is a two-register LC store

The enclosure fork asks about the **energy blob**. On the K4⊗Cosserat lattice the engine
Hamiltonian is a mechanical LC store, split into a **potential** (capacitor / charge /
displacement) register and a **kinetic** (inductor / current / velocity) register. The engine's
own total (kinetic-**inclusive**) Hamiltonian —
`H = k4_energy() + cosserat_kinetic_energy() + cosserat_energy() + coupling_energy()`
([`k4_cosserat_coupling.py:944-946`](../src/ave/topological/k4_cosserat_coupling.py)); the
`E_persist` H-ratio is this quantity ([`genesis_v18_coupled.py:145-148`](../src/ave/core/genesis_v18_coupled.py))
— is exactly this two-register sum plus the cross-coupling term.

| register | circuit role | engine expression | code path | node/bond |
|---|---|---|---|---|
| **POTENTIAL** (K4 V-sector) | node capacitor charge — TLM voltage-pulse storage | `Σ_port (V_inc² + V_ref²)` per site | [`k4_tlm.py:528-530`](../src/ave/core/k4_tlm.py) `get_energy_density()` | per-port pulses summed to the **home node** |
| **POTENTIAL** (Cosserat elastic) | strain/curvature spring energy — translational displacement + rotational storage | `(strain + curvature)` potential density | [`cosserat_field_3d.py:1427`](../src/ave/topological/cosserat_field_3d.py) `energy_density()` | **node** (u, ω node fields) |
| **KINETIC** (Cosserat) | inductor currents — velocity + microrotation-rate storage | `½ρ Σ_c u̇_c² + ½I_ω Σ_c ω̇_c²` per site | [`cosserat_field_3d.py:1789-1794`](../src/ave/topological/cosserat_field_3d.py) `kinetic_energy()` | **node** (u̇, ω̇ *velocity fields conjugate to (u, ω)*, [`:913-918`](../src/ave/topological/cosserat_field_3d.py)) |
| *T2/Φ_link (NOT A1)* | flux linkage / winding — accumulated lap count | `Σ_port Phi_link²` per site | [`k4_tlm.py:400`](../src/ave/core/k4_tlm.py) (monotone accumulation) | per-**bond** (4 ports) summed to home node |

**Two-method verification of the register claim** (verify-before-cite):

1. **Grep, code path.** `grep -n "def kinetic_energy" cosserat_field_3d.py` → `1789:    def
   kinetic_energy(self)`; body = `½·rho·Σ(u_dot·mask)² + ½·I_omega·Σ(omega_dot·mask)²`
   ([`:1790-1794`](../src/ave/topological/cosserat_field_3d.py)). The frozen #689 meter summed
   `get_energy_density() + cos.energy_density()` — the **potential** rows above — and did
   **not** add this kinetic row.
2. **Numeric identity.** The per-node kinetic density (this addendum's
   `_cosserat_kinetic_density`) sums to the engine scalar `cos.kinetic_energy()` at **rel-diff
   0.00e+00** (test-locked, [`src/tests/test_gpersist_meter_ontology.py::test_kinetic_density_sums_to_engine_scalar`](../src/tests/test_gpersist_meter_ontology.py));
   its interior-mask share of H is **~44 %** on the torus `pair` fork cell (43.1 % at smoke) —
   the register the frozen meter dropped.

The **completed full-register A1 density** is `E_full = E_pot + E_kin` (potential rows +
kinetic row); T2/Φ_link stays orthogonal (A1 ⊥ T2, never summed).

---

## 2 · The three convention disclosures (verbatim — ENGINEERING-CHOICE tags)

> **Disclosure #1 — REGISTER LABELS.** The A1 energy blob is a two-register LC store.
> The **POTENTIAL** register (node-capacitor charge / displacement storage) =
> `k4.get_energy_density()` (K4 V-sector, `Σ_port V_inc²+V_ref²`, `k4_tlm.py:528-530`) +
> `cos.energy_density()` (Cosserat strain+curvature potential, `cosserat_field_3d.py:1427`) —
> this is the ONLY register the frozen #689 meter read. The **KINETIC** register (inductor
> currents / velocity storage) = `½ρ|u̇|² + ½I_ω|ω̇|²` (Cosserat velocity u̇=`cos.u_dot` +
> microrotation rate ω̇=`cos.omega_dot`, `cosserat_field_3d.py:1789-1794`), ~44 % of H at the
> read step on the banked fork cells — ADDED here. The completed forward A1 density is the sum
> `E_full = E_pot + E_kin`; the T2/Φ_link winding channel (`Σ_port Phi_link²`, `k4_tlm.py:400`)
> is NEVER summed into A1 (A1 ⊥ T2).

> **Disclosure #2 — BOND-ENERGY ATTRIBUTION.** The inductive/kinetic register is attributed
> with the ENGINE-NATIVE per-node register; NO synthetic bond-to-endpoint (half-to-each-
> endpoint) split is introduced. Rationale: the velocity u̇ and microrotation rate ω̇ are
> node-resident vector fields *conjugate to (u, ω)* on the Cosserat continuum
> (`cosserat_field_3d.py:913-918`, shape (N,N,N,3)), so the kinetic energy is already node-local
> by construction — unlike the genuinely per-bond (4-port) Φ_link/T2 flux. This per-site kinetic
> density sums EXACTLY to the engine scalar `cos.kinetic_energy()` at rel-diff 0.00e+00. The K4
> V-sector potential is likewise per-port pulse energy summed to its home node
> (`get_energy_density`, engine-native). ENGINEERING-CHOICE tag: engine-native per-node kinetic
> attribution — no bond split synthesized.

> **Disclosure #3 — SPONGE EXCLUSION.** For the kinetic-inclusive read on the PML box, the
> read region is the frozen #689 PML-excluded interior mask (`_interior_mask`,
> `k4_cosserat_coupling.py:469`, which already drops the absorbing region where cos_pml_mask<1,
> `cosserat_field_3d.py:898-905`) FURTHER eroded by `SPONGE_GUARD = 1` kinetic-transit ring per
> face — the first interior ring adjacent to the sponge carries outbound velocity/rotation-rate
> TRANSIT current heading into the absorber, which is not "the blob." On the torus (pml=0) there
> is NO sponge, so the read region is the whole periodic lattice for every guard — the fork-
> scored torus cells are untouched by this choice. The guard is a disclosed engineering choice;
> the guard-sensitivity (0/1/2) is recorded as a diagnostic, and a guard-DEPENDENT bin is flagged
> `guard_sensitive` (a read-region/PML-drain artifact, not a boundary-clean signal — §5/§7).

---

## 3 · Live-fire parity (unperturbed trajectory)

The completed meter is measured on the **identical field trajectory** as banked #689/#670: the
mirror-loop `E_persist`/`φ_persist` reproduce `run_loop_gap_probe` at **0.00e+00** relative
(driver `--parity`; smoke S1 and the production cell both PASS). Adding the kinetic readout and
the sponge-guard read region does NOT touch the stepper — only the readout. So the before/after
is a pure **instrument** change on one trajectory.

---

## 4 · Before/after — banked potential-only vs completed full-register

`ROW-KEY` — **BANKED** = frozen #689 instrument (`energy_pot`, potential register, interior
mask; the RESULT §2 table). **FULL** = completed forward instrument (`energy_full` = potential +
Cosserat kinetic, sponge-excluded at `SPONGE_GUARD=1`). Both use the min-image CF ball on the
torus (#689 finding #1). PR / CF = `rel_trend` (PR) / `CF_peak_2.0` (CF); θ=0.10.

**Two statistics per cell (review MAJOR 1 — the instrument fix).** The core is a driven LC
tank; it sloshes pot↔kin 2–3× per recorded step, so the single **endpoint** (drive-off → final
quiet step) is a **phase moment**. Every cell is therefore reported under **both** a phase-robust
**quiet-window mean** (`rel_qmean`: the last-half quiet window time-averaged vs the drive-off
start) — the **PRIMARY** read for the PML box — **and** the **endpoint** (`rel_trend`), kept as a
disclosed companion. The endpoint remains the frozen fork gate on the torus (the fork cells are
phase-robust — both statistics agree, see below). The `_trend` `slope_norm` non-monotone guard
(added in the prior review for this mirage class, previously consumed by nothing) is now routed
through the classifier (`_nonmonotone_flag`) and flags a register whose resolvable endpoint points
opposite the window drift.

**(A) ENDPOINT `rel_trend` — the frozen fork gate.**

| N | boundary | mode | fid | BANKED (pot-only) PR / CF → sig | FULL (pot+kin) PR / CF → sig | bin move |
|---|---|---|---|---|---|---|
| 14 | torus | **pair** | prod | +0.410 / −0.158 → **LOOP-FILLING** | +0.376 / −0.420 → **LOOP-FILLING** | **none (fork cell)** |
| 14 | torus | **graded_a0** | prod | +0.397 / −0.101 → **LOOP-FILLING** | +0.354 / −0.409 → **LOOP-FILLING** | **none (fork cell)** |
| 14 | torus | photon_lock | prod | −0.072 / +0.417 → CONCENTRATING\* | +1.426 / −0.471 → LOOP-FILLING | CONCENTRATING\*→LOOP-FILLING |
| 14 | PML | pair | prod | +0.084 / −0.364 → LOOP-FILLING‡ | −0.067 / +0.679 → CONCENTRATING§ | LOOP-FILLING→CONCENTRATING |
| 14 | PML | graded_a0 | prod | +0.102 / −0.316 → LOOP-FILLING‡ | −0.038 / +0.594 → CONCENTRATING§ | LOOP-FILLING→CONCENTRATING |
| 14 | PML | photon_lock | prod | +0.219 / −0.269 → LOOP-FILLING | −0.015 / +0.025 → INCONCLUSIVE | LOOP-FILLING→INCONCLUSIVE |
| 14 | torus | pair | smoke | +11.781 / −0.867 → LOOP-FILLING | +11.781 / −0.867 → LOOP-FILLING | none |
| 14 | torus | graded_a0 | smoke | +11.499 / −0.864 → LOOP-FILLING | +11.499 / −0.864 → LOOP-FILLING | none |

**(B) QUIET-WINDOW MEAN `rel_qmean` — the phase-robust PRIMARY read (PML box).**

| N | boundary | mode | fid | BANKED (pot-only) PR / CF → sig | FULL (pot+kin) PR / CF → sig |
|---|---|---|---|---|---|
| 14 | torus | **pair** | prod | +0.400 / −0.183 → **LOOP-FILLING** | +0.282 / −0.244 → **LOOP-FILLING** |
| 14 | torus | **graded_a0** | prod | +0.384 / −0.156 → **LOOP-FILLING** | +0.260 / −0.257 → **LOOP-FILLING** |
| 14 | torus | photon_lock | prod | −0.119 / +0.670 → CONCENTRATING | +0.449 / +0.023 → LOOP-FILLING |
| 14 | PML | pair | prod | −0.089 / +0.107 → CONCENTRATING | −0.090 / +0.977 → CONCENTRATING |
| 14 | PML | graded_a0 | prod | −0.081 / +0.097 → INCONCLUSIVE | −0.080 / +0.896 → CONCENTRATING |
| 14 | PML | photon_lock | prod | −0.047 / +0.118 → CONCENTRATING | −0.123 / +0.160 → CONCENTRATING |

`*` #689 §4 CF-alone false-positive (structure-dead control) — **dissolves** under the full
register (photon energy is dominantly kinetic; once included, correctly seen as delocalized).
`‡` the endpoint LOOP-FILLING on the PML pot register is a **phase moment**: `_nonmonotone_flag`
fires (`CF_peak_2.0`: endpoint CF −0.364 opposes the upward window drift `slope_norm` +0.003), and
the phase-robust quiet-mean re-reads CONCENTRATING (pair) / INCONCLUSIVE (graded). See §5/§7.
`§` the PML full-register CONCENTRATING holds under **both** statistics; it is a **boundary-
dependent** read (torus vs PML disagree), restated §5/§7 — **not** a fork-cell move and **not** a
Reading-B revival (the fork is scored on the torus, where both statistics read LOOP-FILLING).

**The fork cells (torus `pair`+`graded_a0`) are PHASE-ROBUST: LOOP-FILLING on both registers under
BOTH statistics** (endpoint pair FULL +0.376/−0.420, graded +0.354/−0.409; quiet-mean pair FULL
+0.282/−0.244, graded +0.260/−0.257). The completion makes them disperse *harder* on CF, and the
center-free PR still rises. `fork_bin_forward = fork_bin_banked = LOOP-FILLING` under the wired-in
triggers. **RULED Reading A stands, phase-robustly.** The two register-completion *benefits* banked
here are (i) the structure-dead `photon_lock` CF-alone false-positive dissolves on the torus
endpoint, and (ii) both fork cells clear the two-statistic **conjunction** (`signature_conj`).

---

## 5 · Sponge exclusion — the honest result (does exclusion restore the PML read?)

**No — and the "why not" is the finding.** On the PML box the full-register read is
**read-region-dependent**, the fingerprint of a boundary artifact, not a clean physical signal:

| PML pair, full register | guard 0 (interior mask) | guard 1 (**shipped**) | guard 2 |
|---|---|---|---|
| PR rel | −0.010 | −0.067 | −0.277 |
| CF rel | +0.061 | **+0.679** | **+0.801** |
| signature | INCONCLUSIVE | CONCENTRATING | CONCENTRATING |

The CONCENTRATING signal **strengthens monotonically with guard width** (0→INCONCLUSIVE,
1→+0.679, 2→+0.801). A genuine physical concentration is roughly guard-independent; this
guard-dependence is the signature of the **PML peripheral-drain**: the sponge absorbs the
outbound (kinetic-dominated) wake, draining the outer interior shells faster than the core, so
the residual kinetic field *looks* more core-concentrated the deeper you read — with no finite
guard removing it. Decisive discriminator (`gpersist_localization_observable.py`, guard sweep):

- **POTENTIAL register stays LOOP-FILLING at every guard** (CF still falls: −0.364 / −0.311 /
  −0.128). If guard-erosion were a pure cropping artifact it would flip **both** registers; it
  does not. The CONCENTRATING signal is **kinetic-register-specific**.
- **KINETIC register is boundary-sensitive on the absorbing boundary** — swamped by transit at
  guard 0 (INCONCLUSIVE), drain-biased to CONCENTRATING once the transit ring is excluded.

So the sponge exclusion does **not** restore the PML twins to a clean LOOP-FILLING read; instead
it **exposes** that the **potential** register is the boundary-clean instrument (LOOP-FILLING on
both boundaries) while the **kinetic** register cannot be read boundary-cleanly on the wake-
absorbing box. The driver flags every guard-dependent full-register bin `guard_sensitive=True`;
the torus fork cells are `guard_sensitive=False` (guard is a no-op there — boundary-clean).

---

## 6 · The meter answers the fork

The enclosure fork asks about the **ENERGY blob** — and the blob is a two-register LC store
(§1). The frozen meter read the **potential** register only; but the scalar it claimed to
parallel — `E_persist` — is a kinetic-**inclusive** H-ratio
([`genesis_v18_coupled.py:145-148`](../src/ave/core/genesis_v18_coupled.py)), so it was measuring
a different register than that scalar (#689 finding #3). **The labeled full-register meter
(`energy_full`) is therefore the correct instrument for the fork** — it reads the same two-
register store the `E_persist` scalar sums. On the **torus** — where the fork is scored and there is no sponge to
contaminate the kinetic register — the completed full-register meter reads **LOOP-FILLING** on
both fork cells (energy disperses, harder on CF than the potential-only read), agreeing with the
RULED Reading A. The frozen **potential-only** meter remains **banked** for the historical #689
run (KEEP-BOTH, §8): it is a correct read of the *potential* register, and the #689 RESULT is
its provenance record — this addendum neither edits nor retracts it.

---

## 7 · Surfaced for adjudication (flag-don't-fix) — PML boundary corroboration

**Not a fork-cell move; surfaced, not silently resolved.** Under the completed full-register
meter the **PML twins' boundary-insensitivity corroboration inverts**: the #689 RESULT TL;DR
item 2 ("the PML twins read the SAME sign → LOOP-FILLING under pml=3 too") holds on the
**potential-only** meter but **not** on the full-register meter (PML twins → CONCENTRATING† at
the shipped guard, or INCONCLUSIVE at guard 0). Per §5 this is a **PML-drain read-region
artifact** in the Cosserat **kinetic** register (guard-dependent; the potential register stays
boundary-clean LOOP-FILLING), **not** a revival of Reading B:

- The fork is scored on the **torus** cells (no sponge); they read LOOP-FILLING on **both**
  registers and are `guard_sensitive=False`. **The RULED Reading A is untouched.**
- A naive read of "PML twin CONCENTRATES" could *appear* fork-adjacent; it is not — it is
  boundary-absorption of the outbound kinetic wake, diagnosed by the guard-dependence and by the
  potential register's boundary-clean LOOP-FILLING. G-PERSIST ★RULED (fork-independent PML
  φ-trend) is likewise untouched.

**What changes:** the boundary-**insensitivity** claim is now **register-explicit** — it is the
**potential** register that is boundary-clean; the full-register PML read is kinetic-drain-
contaminated and is **not** admissible as boundary corroboration. This is a corroboration-level
restatement for the auditor's manual/queue (the auditor lands it), **not** a fork verdict change.

---

## 8 · KEEP-BOTH banking statement (formal)

- **BANKED (frozen) instrument — `energy_pot` (potential-only, interior mask):** the instrument
  of record for the **#689 run**. It is a correct read of the **potential** register; the #689
  RESULT §2 table is its provenance and is **NOT** edited or retracted by this addendum. It stays
  available (`BANKED_SECTOR="energy_pot"`) for reproduction of the historical read.
- **COMPLETED (forward) instrument — `energy_full` (potential + Cosserat kinetic, sponge-
  excluded):** the **MANDATORY** instrument for **all future meter use**, and **especially for
  any CONCENTRATING claim** — a concentration claim must be scored on the full register (both LC
  registers), with the two-statistic conjunction (`signature_conj`), the torus-native min-image
  CF ball, and the `guard_sensitive` honesty flag. Potential-only CONCENTRATING claims are
  **not** admissible going forward.
- **KEEP-BOTH, not a swap:** both instruments ship in the driver (`SECTORS` roster); the frozen
  read is preserved for the historical run, the completed read governs the future. This satisfies
  Grant's Ruling 2 unblock condition (map completed + fully labeled ⇒ KEEP-BOTH unblocked).

---

## 9 · Provenance / reproduction

- Driver: [`gpersist_localization_observable.py`](../src/scripts/vol_1_foundations/gpersist_localization_observable.py)
  (`--parity` / `--cell` / `--plant` / `--aggregate`). Same primitives as `run_loop_gap_probe`
  (Rule-14); parity 0.00e+00.
- Unit tests: [`src/tests/test_gpersist_meter_ontology.py`](../src/tests/test_gpersist_meter_ontology.py)
  — attribution identity (kinetic density → engine scalar, rel-diff 0.00e+00) + sponge-exclusion
  geometry (torus no-op, PML centered-block erosion) + the phase-robust statistic (quiet-window
  mean inverts an endpoint phase moment, `_nonmonotone_flag` fires on endpoint-vs-drift disagreement,
  `_sector_signature` stat selector); 8 pass, driver-confirmed (`src/scripts/vol_1_foundations/gpersist_localization_observable.py`).
- Per-cell JSON + summary: `assets/sim_outputs/gpersist_localization_observable/` (**gitignored**;
  regenerate with the driver — deterministic, byte-for-byte from the frozen carrier).
- Shipped code paths for every §4/§5 number (review MINOR 3): the potential-register guard sweep
  is emitted by the `energy_pot` / `energy_pot_g1` / `energy_pot_g2` diagnostic sectors (guards
  0/1/2), and the phase-robust quiet-window mean by `rel_qmean` on every sector — so both the
  endpoint and the quiet-mean pot-guard series regenerate from the shipped `SECTORS` roster.
- Gate-faithful KEEP-BOTH banking (review MINOR 6): `fork_bin_banked` now runs the SAME three
  bin-determining MIXED triggers as `fork_bin_forward` (`_mixed_triggers` on the banked signatures
  + `twin_sigs_banked`), not an empty reasons list. It still yields **LOOP-FILLING** on this data.
- Settled verdicts untouched: enclosure fork = **RULED Reading A** (Grant 2026-07-14); G-PERSIST
  **★RULED**. Nothing in this addendum re-opens either.
